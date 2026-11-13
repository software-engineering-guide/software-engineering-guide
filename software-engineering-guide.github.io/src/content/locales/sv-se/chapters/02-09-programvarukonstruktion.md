# 2.9 Programvarukonstruktion

## Översikt och motivation

[Programvarukonstruktion](https://en.wikipedia.org/wiki/Software_construction) är där design blir körande kod. Det är det detaljerade arbetet med kodning, verifiering, [enhetstestning](https://en.wikipedia.org/wiki/Unit_testing), [integrationstestning](https://en.wikipedia.org/wiki/Integration_testing) och [felsökning](https://en.wikipedia.org/wiki/Debugging). Guiden [Software Engineering Body of Knowledge](https://en.wikipedia.org/wiki/Software_Engineering_Body_of_Knowledge) (SWEBOK) behandlar konstruktion som ett eget kunskapsområde, och med goda skäl: det är här det mesta av ditt dagliga arbete sker. De val du gör rad för rad (hur du håller komplexitet i schack, hur du hanterar fel, hur läsbart du lämnar saker) avgör om ett system kan förstås, ändras och litas på under många år.

I ett stort team är konstruktion en gruppinsats, inte en solouppgift. Hundratals ingenjörer skriver in i en gemensam kodbas som kommer att överleva vilken enskild persons tid i teamet. Ribban är därför inte "fungerar det på min maskin i dag". Den är "kan en främling säkert ändra det här om fem år". Konstruktion hänger uppåt ihop med krav (kapitel 2.8) och design (kapitel 2.2), som talar om vad som ska byggas och dess form. Den hänger sidledes ihop med kodstandarder (kapitel 2.1), testning (kapitel 2.4) och kodgranskning (kapitel 2.5), som formar hur arbetet uttrycks, verifieras och granskas. God konstruktion förvandlar en sund design till en underhållbar tillgång. Dålig konstruktion förvandlar även en god design till en belastning.

I företags- och myndighetsmiljöer väger konstruktion extra tungt. Dessa system är långlivade, starkt reglerade och ofta säkerhets- eller medborgarkritiska. [Defensiv kodning](https://en.wikipedia.org/wiki/Defensive_programming), disciplinerad felhantering och kod som uppenbart är korrekt är här inga trevligheter. De är krav för försäkran, revision och kontinuitet över decennier och personalomsättning. Målet är kod som förmedlar sin avsikt, motstår fel och kan verifieras. Kod som bara körs räcker inte.

## Nyckelprinciper

- Minimera komplexitet framför allt. Den främsta fienden i storskalig konstruktion är kod ingen fullt ut kan förstå.
- Förutse förändring. Konstruera så att sannolika framtida ändringar blir lokala och billiga.
- Konstruera för verifiering. Skriv kod vars korrekthet är lätt att kontrollera med tester, granskning och resonemang.
- Återanvänd medvetet. Bygg på betrodda befintliga komponenter snarare än att uppfinna om, men undvik koppling till fel abstraktioner.
- Följ standarder. Enhetlighet över en kodbas minskar den kognitiva kostnaden för varje framtida ändring.
- Hantera fel och ogiltiga tillstånd uttryckligen. Gör felmönster synliga snarare än tysta.
- Håll koden läsbar. Konstruktion är kommunikation med framtida underhållare först och kompilatorn sedan.

## Rekommendationer

### Minimera komplexitet som den primära disciplinen

Gör att minska komplexitet, både väsentlig och oavsiktlig, till ditt centrala mål. Skriv små funktioner och moduler med ett enda syfte. Föredra tydliga namn framför klurigheter. Håll nästling grund och kontrollflöde linjärt. Lokalisera beslut så att förståelsen av en kodbit inte tvingar dig att hålla hela systemet i huvudet. Komplexitet är det som gör stora kodbaser långsamma att ändra och farliga att röra, så väg varje val mot om det lägger till komplexitet eller tar bort den. Tillämpa designprinciperna i kapitel 2.2 på den lilla skalan också: hög sammanhållning, låg koppling och tydlig [åtskillnad av ansvarsområden](https://en.wikipedia.org/wiki/Separation_of_concerns) spelar lika stor roll i en enskild funktion som i en arkitektur.

### Konstruera för förändring och för verifiering

Tänk framåt på de ändringar som med störst sannolikhet kommer (nya affärsregler, nya integrationer, ny reglering) och isolera dem bakom stabila gränssnitt så att förändringen förblir lokal. Skriv samtidigt kod som är lätt att verifiera: [rena funktioner](https://en.wikipedia.org/wiki/Pure_function) (samma indata ger alltid samma utdata, utan sidoeffekter) där du kan, minimalt dolt tillstånd och beroenden gjorda uttryckliga så att tester kan ersätta dem. Kod som är svår att testa är vanligen kod som är svår att förstå och ändra. Testbarhet (kapitel 2.4) är en designsignal, inte bara en QA-angelägenhet.

### Återanvänd medvetet och standardisera

Sträck dig efter väl underhållna, betrodda bibliotek och interna komponenter innan du skriver om grundläggande logik, och använd dem genom tydliga gränssnitt (kapitel 2.3). Bygg återanvändbara komponenter bara när ett genuint andra användningsfall finns, eftersom att generalisera för tidigt är en egen form av komplexitet. Tillämpa din organisations kodstandarder och stil (kapitel 2.1) enhetligt, helst upprätthållna av automatiska formaterare och [linters](https://en.wikipedia.org/wiki/Lint_(software)), så att hela kodbasen läses som om en noggrann författare skrivit den.

### Praktisera defensiv programmering med omdöme

Validera indata vid förtroendegränser (externa begäranden, fil- och nätverks-I/O, användarindata) och behandla alla data som korsar de gränserna som fientliga tills motsatsen bevisats. Inom en väl testad modul, däremot, kväv inte varje rad i redundanta kontroller som döljer logiken och undertrycker verkliga fel. Regeln är enkel: försvara vid gränserna, lita inuti dem. Använd [påståenden (assertions)](https://en.wikipedia.org/wiki/Assertion_(software_development)) för att dokumentera och upprätthålla invarianter som aldrig ska vara falska i ett korrekt program. Använd [undantag](https://en.wikipedia.org/wiki/Exception_handling) och felhantering för villkor som legitimt kan inträffa vid körning. Håll de två åtskilda: påståenden vaktar programmerarens antaganden, felhantering hanterar förväntade fel.

### Hantera fel uttryckligen och fall säkert

För varje fel, besluta medvetet vad du ska göra: återhämta, försöka om, vidarebefordra eller fall snabbt. Svälj aldrig ett undantag tyst eller ignorera ett returnerat fel. Ett undertryckt fel kommer tillbaka som en mystisk defekt senare. Behåll sammanhang i dina felmeddelanden och loggar så att fel kan diagnostiseras. I säkerhets- och medborgarkritiska system, fall in i ett säkert, känt tillstånd snarare än att fortsätta i ett korrumperat. Ge felvägen lika mycket eftertanke som den lyckade vägen, för i produktion är det på felvägen förtroende vinns eller förloras.

### Bygg in kvalitet under konstruktionen

Kvalitet byggs in, den inspekteras inte in efteråt. Skriv enhetstester vid sidan av koden, kör [statisk analys](https://en.wikipedia.org/wiki/Static_program_analysis) och linters kontinuerligt och håll funktioner tillräckligt små för att resonera om. Använd självförklarande namn och struktur så att dina kommentarer kan förklara varför, inte vad. [Omstrukturera](https://en.wikipedia.org/wiki/Code_refactoring) allteftersom för att hålla koden beboelig. Kodgranskning (kapitel 2.5) är det mänskliga skyddsnätet, men det mesta av kvaliteten måste finnas där redan innan granskningen börjar.

### Välj och standardisera konstruktionsverktyg

Standardisera verktygskedjan (kompilatorer, byggsystem, formaterare, linters, statiska analysverktyg, felsökare, beroendehanterare och IDE-konfigurationer) så att varje ingenjör arbetar i en konsekvent, reproducerbar miljö. Koppla in verktygen i pipelinen så att kvalitetskontroller inte är valfria. Ta in AI-stödda kodverktyg medvetet och behandla deras utdata som ett utkast som måste klara samma standarder, granskning och tester som all annan kod.

## Avvägningar: för- och nackdelar

| Praxis | Fördelar | Nackdelar |
|---|---|---|
| Aggressiv komplexitetsminimering | Läsbart, förändringsbart, låg defektfrekvens | Kan kännas långsamt. Risk för överabstraktion om det tillämpas fel |
| Omfattande defensiva kontroller | Fångar dåliga tillstånd tidigt, robusta gränser | Belamrar logiken. Kan dölja verkliga buggar om det överdrivs |
| Påståenden för invarianter | Dokumenterar och upprätthåller antaganden | Avstängda i vissa produktionsbyggen. Inte felhantering |
| Omfattande återanvändning av bibliotek | Mindre kod att äga. Snabbare leverans | Beroenderisk, koppling, exponering i leveranskedjan |
| Strikta standarder och linting | Enhetlig kodbas med låg friktion | Uppsättning i förväg. Kan kännas stel för individer |
| Konstruktion för testbarhet | Verifierbar, förändringsbar kod | Kan lägga till indirektion som vissa ser som ceremoni |

Den centrala avvägningen i konstruktion är kortsiktig hastighet mot långsiktig förändringsbarhet. Att ta genvägar (hoppa över felhantering, tolerera komplexitet, ignorera standarder) känns snabbare i stunden, och är nästan alltid dyrare över systemets liv. Det motsatta felet är överkonstruktion: för mycket defensivitet, spekulativ abstraktion och generalitet ingen behöver. Skicklig konstruktion ligger i mitten: så enkel som möjligt, så defensiv som gränserna kräver och inte mer.

## Frågor att diskutera med ditt team

1. **Vad är vår gemensamma, konkreta definition av "för komplex", och var upprätthåller vi den före sammanslagning?** "Minimera komplexitet" är konstruktionens centrala disciplin, men som slagord förlorar det varje argument mot en deadline. I ett stort team där hundratals människor skriver in i en kodbas måste komplexitet vara mätbar, så kom överens om signaler ni faktiskt kommer att agera på: funktionslängd, nästlingsdjup, cyklomatisk komplexitet och antalet saker en läsare måste hålla i huvudet för att förstå en ändring. Ta med ert värsta fall till mötet och fråga om er nuvarande granskning skulle ha fångat det. Svaret bör bli en pipelinegrind eller en punkt på en granskningschecklista, eftersom en tröskel som upprätthålls av ett verktyg är värd mer än en princip som upprätthålls av viljestyrka, och den besparar din nästa anställda den långsamma ackumulationen av kod ingen säkert kan röra.

2. **Beter sig våra felvägar i produktion som vi designade dem, och när övade vi senast en medvetet?** Konstruktionsrådet säger ge felvägen lika mycket eftertanke som den lyckade vägen, men felvägen är vanligen den minst testade kod ni äger, och i ett medborgarkritiskt eller säkerhetskritiskt system är det där förtroende vinns eller förloras. Ett undertryckt undantag eller en ignorerad returkod blir en mystisk defekt veckor senare, och "fall in i ett säkert tillstånd" är ett löfte ni inte kan hålla om ni aldrig sett det hända. Ta med er incidenthistorik: hur många tidigare avbrott kunde spåras tillbaka till ett svalt fel eller en otestad återhämtningsväg? Åtgärden är att testa fel medvetet (injicera det avvisade kortet, tidsgränsen, felformade indata) och att kräva att varje fel hanteras, loggas med sammanhang eller vidarebefordras, aldrig tyst tappas.

3. **Vilka delar av vår kodbas är svåra att testa, och vad säger den svårigheten oss om designen?** Kod som motstår testning är nästan alltid kod som döljer tillstånd, kopplar till fel beroenden eller gör för mycket, så testbarhet är en designsignal, inte en QA-eftertanke. I ett långlivat företagssystem spelar det roll eftersom de moduler som är smärtsamma att testa i dag är de en främling kommer att vara rädd för att ändra om fem år. Ta med klassen eller tjänsten ditt team fruktar att skriva tester för och fråga varför: är tillståndet dolt, är beroendena omöjliga att ersätta, gör funktionen tre jobb? Svaret bör driva omstrukturering mot rena funktioner, uttryckliga beroenden och små enheter med ett enda syfte, eftersom att göra koden verifierbar är samma arbete som att göra den begriplig och billig att ändra.

4. **När återanvänder vi ett externt bibliotek mot att bygga förmågan själva, och vem äger den leveranskedjerisk vi tar på oss?** Att sträcka sig efter ett betrott bibliotek är snabbare än att uppfinna om grundläggande logik, men varje beroende ni lägger till är kod ni inte kontrollerar, inte lätt kan revidera och måste patcha den dag den komprometteras. I ett stort team är faran att hundra ingenjörer var och en drar in sina egna transitiva beroenden tills ingen kan säga vad kodbasen faktiskt kör. Ta med er beroendeinventering och fråga tre konkreta saker: hur många bibliotek som inte längre underhålls, hur många som bär kända sårbarheter och hur många som omsluter logik enkel nog att äga rakt av. Den motstridiga hänsynen är verklig, för att skriva egen kryptografi eller datumhantering är nästan alltid sämre än ett beprövat bibliotek, så målet är en medveten policy för återanvändning snarare än generell undvikande. I företags- och myndighetsmiljöer, lägg till upphandlings- och licensefterlevnadsvinkeln, eftersom ett ogranskat beroende kan bära en licens oförenlig med era skyldigheter eller ett ursprung ingen revisor accepterar.

5. **Hur håller vi AI-genererad kod till samma konstruktionsstandarder som mänskligt skriven kod, och kan vi skilja de två åt när det spelar roll?** AI-kodassistenter producerar trovärdiga utkast snabbt, och frestelsen är att behandla deras utdata som färdigt eftersom det kompilerar och ser idiomatiskt ut. Kapitlets regel är att genererad kod klarar samma granskning, tester och standarder som allt annat, och ett stort team måste göra den regeln operativ snarare än aspirationell. Ta med exempel på AI-stödda ändringar som nyligen levererats och fråga om var och en bar tester, klarade statisk analys och verkligen förstods av människan som lämnade in den, eller om den vinkades igenom på tillit. Det motstridiga trycket är hastighet, eftersom assistenterna är genuint produktiva och att sakta ner varje förslag till ett krypande kastar bort nyttan. I reglerade och offentliga sammanhang, lägg till ursprungs- och ansvarsvinkeln, eftersom ni kan behöva intyga vem som ansvarar för en kodrad och om ett genererat fragment bär en licens- eller upphovsrättsfråga ni inte kan besvara.

6. **Är vår konstruktionsverktygskedja faktiskt standardiserad och upprätthållen i pipelinen, eller arbetar individer fortfarande i oförenliga uppsättningar?** En gemensam verktygskedja av formaterare, linter, statisk analysator, byggsystem och beroendehanterare låter en ingenjör röra sig tryggt över obekanta tjänster, eftersom koden läses som en röst och kontrollerna är identiska överallt. När den driver uppfinner varje team sin egen konfiguration, granskningstid läggs på att gräla om stil och defekter som ett teams analysator skulle ha fångat slinker igenom hos ett annat. Ta med listan över repositorier som inte kör standardkontrollerna vid varje commit och fråga varför var och en valde bort dem. Spänningen är att en enda föreskriven uppsättning kan kännas stel för team med genuint olika behov, så besluta var enhetlighet är värd friktionen och var ett dokumenterat undantag är i sin ordning. För ett stort företag eller offentligt organ, knyt detta till reproducerbarhet och revision, för ett bygge ni inte kan reproducera byte för byte från en kontrollerad verktygskedja är ett ni inte kan försvara inför en bedömare år senare.

## Sektorsperspektiv

**Startup.** Hastighet vinner, så sätt en gemensam formaterare och linter på plats dag ett, validera indata vid din enda externa gräns och håll den interna koden ren snarare än defensiv på varje rad. Hoppa över spekulativ abstraktion och tung process: med två eller tre ingenjörer håller hela teamet kodbasen i huvudet, och den verkliga risken är komplexitet som överlever det delade minnet. Lita på betrodda bibliotek för allt grundläggande så att du skriver så lite kod du kan äga väl.

**Småföretag.** Utan särskild byggingenjör och med snäv budget, föredra konventioner dina befintliga verktyg upprätthåller gratis: en formaterare och linter som levereras med språket, vettiga standardvärden och en liten uppsättning regler alla kan komma ihåg. Köp eller anta väl underhållna bibliotek snarare än att bygga infrastruktur du inte kan bemanna för att underhålla. Lägg din begränsade disciplin på de två saker som gör mest ont när de försummas: att validera indata vid gränsen och att aldrig svälja ett fel tyst.

**Storföretag.** Med hundratals ingenjörer som skriver in i delad kod är prioriteten enhetlighet och upprätthållande: en standardverktygskedja inkopplad i pipelinen, grindar för statisk analys och regler för gränsvalidering tillämpade överallt så att människor rör sig tryggt mellan tjänster. Hantera beroende- och leveranskedjerisk som en styrd process snarare än improvisation per team, och använd påståenden för att koda domäninvarianter som måste hålla över varje team. Behandla konstruktionsstandarder som det substrat som håller en kodbas beboelig över decennier och personalomsättning.

**Offentlig sektor.** Långlivade, medborgarkritiska system gör disciplinerad konstruktion till en fråga om försäkran och ansvarsskyldighet. Isolera föränderliga regler som lagstiftning bakom stabila gränssnitt så att förändring förblir lokal och spårbar till krav, fall in i säkra kända tillstånd snarare än att fortsätta i ett korrumperat, och leverera varje modul med tester som fungerar som revisionsbelägg. Upphandlings- och transparensskyldigheter betyder att er verktygskedja, era beroenden och er felhantering måste vara dokumenterade tillräckligt väl för att en tjänsteman som anländer år senare, eller en extern revisor, kan verifiera att koden är korrekt.

## Exempel

**Startup.** En startup med tre ingenjörer kopplar in en gemensam formaterare och linter dag ett och kör dem vid varje commit, så att kodbasen läses som en röst även när de lägger till konsulter. De validerar indata vid sin API-gräns och behandlar allt utifrån som fientligt, men håller den interna logiken ren snarare än att kväva den i redundanta kontroller. När en betalningswebhook börjar fallera går rättelsen snabbt eftersom inget undantag någonsin tyst svaldes och felmeddelandet bär nog med sammanhang för att peka rakt på orsaken. Hela uppsättningen tog en eftermiddag och besparade dem den långsamma ackumulationen av komplexitet som skulle ha gjort deras nästa anställdas första vecka eländig.

**Storföretag.** Ett globalt betalningsföretag upprätthåller en gemensam verktygskedja över hundratals ingenjörer: automatisk formatering och linting vid varje commit, grindar för statisk analys i pipelinen och en regel att alla externa indata valideras vid tjänstegränser. Domänlogik använder påståenden för att upprätthålla invarianter som "en huvudbokspost balanserar alltid", medan körtidsvillkor som ett avvisat kort hanteras som uttryckliga, loggade utfall. Eftersom standarderna är enhetliga och fel aldrig tyst sväljs rör sig ingenjörer tryggt över obekanta tjänster, och produktionsincidenter kan diagnostiseras rakt ur loggarna.

**Offentlig sektor.** En nationell skattemyndighet bygger ett långlivat bedömningssystem som förväntas köras i decennier under föränderlig lagstiftning. Konstruktionen isolerar varje skatteregel bakom ett stabilt gränssnitt, så att årliga lagändringar förblir lokala och spårbara till krav (kapitel 2.8). Defensiv validering vaktar varje medborgarvänt indata. Felvägar faller in i ett säkert tillstånd som aldrig i tysthet utfärdar en felaktig bedömning. Varje modul levereras med enhetstester som revisionsbelägg. Eftersom konstruktionen är standardiserad och väldokumenterad kan nya tjänstemän säkert underhålla kod skriven av företrädare som lämnade för länge sedan.

## Affärsnytta: motiv, ROI och TCO

Avkastningen på disciplinerad konstruktion är den bestående förmågan att ändra programvara billigt och säkert, och det är där det mesta av ett systems totala ägandekostnad avgörs. Studier av programvaruekonomi visar konsekvent att det mesta av ett systems livstidskostnad är underhåll, och underhållskostnaden dominerar av hur begriplig och förändringsbar koden är. Att minimera komplexitet, hantera fel uttryckligen och följa standarder sänker direkt kostnaden för varje framtida ändring och varje produktionsincident.

Kostnaden för att införa är måttlig och mest i förväg: sätt standarderna, koppla in linters och analysverktyg och bygg vanan att skriva verifierbar, defensiv kod. Kostnaden för försummelse, å andra sidan, växer. Komplexitet ackumuleras till kod som är långsam att ändra och riskabel att röra. Tysta fel förvandlas till dyra produktionsincidenter. Inkonsekvent stil multiplicerar insatsen för varje granskning och varje introduktion. För att argumentera inför ledningen, koppla konstruktionskvalitet till andel misslyckade ändringar, genomsnittlig återställningstid, andel undkomna defekter och introduktionstid, som alla konstruktionsdisciplin direkt förbättrar.

## Antimönster och fallgropar

- **Komplexitetskrypning:** att ackumulera klurig, djupt nästlad eller vidsträckt kod tills ingen förstår den.
- **Tyst sväljande av fel:** tomma catch-block och ignorerade returkoder som förvandlar fel till framtida mysterier.
- **Överdriven defensiv programmering:** redundanta kontroller överallt som begraver logiken och maskerar verkliga defekter.
- **Att förväxla påståenden med felhantering:** att använda påståenden för körtidsvillkor, eller undantag för programmerarinvarianter.
- **Kopiera-och-klistra-konstruktion:** att duplicera logik i stället för att återanvända, så att rättelser måste göras på många ställen.
- **Spekulativ generalitet:** att bygga abstraktioner och konfigurerbarhet för behov som aldrig kommer.
- **Att ignorera standarder:** varje ingenjör kodar på sitt eget sätt, vilket multiplicerar kognitiv belastning över kodbasen.
- **Otestad konstruktion:** att skriva kod utan medföljande tester och skjuta verifieringen till en fas som aldrig kommer.

## Mognadsmodell

- **Nivå 1 (Initiera):** Konstruktion är ad hoc och reaktiv. Komplexitet och felhantering varierar med individ. Få standarder finns och tysta fel är vanliga.
- **Nivå 2 (Utveckla):** Kodstandarder, formaterare och linters finns, och grundläggande felhantering och enhetstestning förväntas, men praxis är inkonsekvent och varje team tillämpar den olika.
- **Nivå 3 (Standardisera):** Komplexitetsminimering, gränsvalidering, uttrycklig felhantering och testbarhet är dokumenterade och upprätthålls i hela organisationen, i pipelinen och i granskning, så att hela kodbasen läses som om en noggrann författare skrivit den.
- **Nivå 4 (Hantera):** Konstruktionskvaliteten mäts mot utgångslägen. Teamet följer cyklomatisk komplexitet, andel undkomna defekter, andel misslyckade ändringar, täckning av testade felvägar och fynd i kodgranskning, och agerar på trenderna snarare än på åsikt.
- **Nivå 5 (Orkestrera):** Konstruktion förbättras kontinuerligt och är integrerad i hela organisationen. Defensiva mönster, standarder och mått matar tillbaka till omstrukturering och verktyg. AI-stödda verktyg körs under samma kvalitetsgrindar, och praxis anpassas när språk, reglering och risker förändras.

## Idéer för diskussion

- Var ackumuleras oavsiktlig komplexitet mest i er kodbas, och vilka konstruktionsvanor skapar den?
- Vilken är ert teams faktiska regel för var indata valideras och var de litas på?
- Skiljer era ingenjörer påståenden från felhantering, och är den skillnaden konsekvent?
- Hur mycket av er kvalitet byggs in under konstruktionen mot fångas senare i granskning eller testning?
- Hur avgör ni när ni ska återanvända ett bibliotek mot att bygga, med tanke på leveranskedjerisk?
- Hur bör AI-genererad kod hållas till samma konstruktionsstandarder som mänskligt skriven kod?

## Viktigaste punkter

- Konstruktion är där design blir underhållbar kod. Att minimera komplexitet är dess centrala disciplin.
- Konstruera för förändring och för verifiering: testbar, förändringsbar kod är begriplig kod.
- Försvara vid förtroendegränser, lita inuti dem och svälj aldrig fel tyst.
- Använd påståenden för invarianter och felhantering för förväntade körtidsvillkor. Förväxla dem inte.
- Standardisera verktyg och stil, återanvänd medvetet och bygg in kvalitet i stället för att inspektera den efteråt.

## Referenser och vidare läsning

- IEEE Computer Society, *SWEBOK Guide (Guide to the Software Engineering Body of Knowledge)*, Software Construction knowledge area
- Steve McConnell, *Code Complete: A Practical Handbook of Software Construction*
- Robert C. Martin, *Clean Code: A Handbook of Agile Software Craftsmanship*
- Andrew Hunt and David Thomas, *The Pragmatic Programmer*
- Martin Fowler, *Refactoring: Improving the Design of Existing Code*
- John Ousterhout, *A Philosophy of Software Design*
