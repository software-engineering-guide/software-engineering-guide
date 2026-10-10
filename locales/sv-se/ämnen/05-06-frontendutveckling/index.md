# 5.6 Frontendutveckling

## Översikt och motivation

Frontendutveckling är disciplinen att bygga programvarans klientvända lager: koden som körs i webbläsaren eller på enheten och förvandlar design, innehåll och data till ett fungerande gränssnitt. Den spänner över val av ramverk och arkitektur, renderingsstrategi, tillståndshantering, prestanda och motståndskraft över den enorma mångfalden av webbläsare, enheter och nätverksförhållanden i den verkliga världen. Frontenden är där allt uppströmsarbete (UX, design, innehåll, tillgänglighet, internationalisering) antingen når användaren framgångsrikt eller faller samman.

För stora team är frontenden unikt utmanande, eftersom den exponeras för en miljö organisationen inte kontrollerar. Användares webbläsare, enheter, uppkopplingar och inställningar varierar vilt, och plattformen (webben) utvecklas kontinuerligt. I skala ackumuleras arkitekturval. Ett ramverk valt i dag begränsar rekrytering, prestanda och underhållbarhet i åratal, och tusentals små beslut om paketstorlek och rendering summerar till den upplevelse användare faktiskt får. Gemensamma standarder, komponentbibliotek, prestandabudgetar och arkitekturmönster är det som hindrar många oberoende team från att producera en långsam, inkonsekvent, skör helhet.

Relevansen för företag och myndigheter är akut. Företag underhåller långlivade applikationer där ramverkens livslängd och underhållbarhet spelar större roll än nyhet, och där många team måste samverka. Myndigheter betjänar hela allmänheten, inklusive människor på gamla enheter, långsamma eller datamätta uppkopplingar och hjälpmedel. Det gör prestanda, [progressiv förbättring](https://en.wikipedia.org/wiki/Progressive_enhancement) och motståndskraft till inte valfri polering utan skillnaden mellan en tjänst som fungerar för alla och en som utesluter de mest missgynnade. En myndighetstjänst som bara fungerar på den senaste telefonen med en snabb uppkoppling sviker sitt uppdrag.

## Nyckelprinciper

- Frontenden körs i en miljö du inte kontrollerar. Designa för variation och fel.
- Välj tråkig, varaktig teknik för långlivade system. Optimera för underhållbarhet och rekrytering.
- Prestanda är en funktion och för många användare en förutsättning för tillgång.
- Progressiv förbättring: leverera en fungerande kärnupplevelse först och lägg sedan förbättringar i lager.
- Skicka mindre kod. Den snabbaste och mest pålitliga koden är den du inte levererar.
- Matcha renderingsstrategi mot innehållstyp och användarbehov, inte mot mode.
- Motståndskraft: gränssnittet bör degraderas elegant, inte gå sönder, när saker går fel.
- Standarder och plattformsfunktioner överlever ramverk. Lita på plattformen.

## Rekommendationer

### Välj ramverk för livslängd och passform, inte för hype

Välj frontendteknik utifrån problemet, teamet, underhållshorisonten och rekryteringsmarknaden, inte utifrån vad som trendar. För långlivade företags- och myndighetssystem, föredra mogna, väl stödda tekniker med stora talangpooler, stabila releasepraxis och tydliga uppgraderingsvägar. Väg den totala kostnaden för ramverksomsättning: omskrivningar är dyra och riskabla. Föredra ansatser som lutar sig mot [webbstandarder](https://en.wikipedia.org/wiki/Web_standards) så att din investering överlever ramverksskiften, och isolera ramverksspecifik kod bakom gränser så att applikationen inte är gisslan åt ett biblioteks livscykel.

### Matcha renderingsstrategin mot behovet

De huvudsakliga renderingsstrategierna passar olika innehåll. Serversidig rendering (SSR) ger snabb första ritning och god SEO ([sökmotoroptimering](https://en.wikipedia.org/wiki/Search_engine_optimization)) och fungerar utan JavaScript på klienten, vilket passar innehållstunga och publikt vända sidor. [Statisk webbplatsgenerering](https://en.wikipedia.org/wiki/Static_site_generator) (SSG) förrenderar vid byggtid för maximal hastighet och cachebarhet, idealiskt för innehåll som sällan ändras. Klientsidig rendering (CSR) passar högt interaktiva, appliknande upplevelser bakom autentisering. Strömning och progressiv hydrering skickar och aktiverar sidan stegvis så att användare ser och använder innehåll tidigare. Många stora system blandar dessa per rutt snarare än att välja en globalt. Hantera tillstånd medvetet: håll serverns tillstånd, URL-tillstånd och lokalt UI-tillstånd åtskilda och undvik att överförstora allt till ett tungt globalt lager.

### Behandla prestanda som en budgeterad, mätt disciplin

Anta prestandabudgetar (uttryckliga gränser för paketstorlek, antal förfrågningar och nyckelmått) och upprätthåll dem i CI så att regressioner fäller bygget. Följ Core Web Vitals (laddning, interaktivitet och visuell stabilitet) med övervakning av verkliga användare från faktiska enheter och nätverk, inte bara labbtester på snabba maskiner. Minska JavaScript aggressivt: koddela och [ladda lätt](https://en.wikipedia.org/wiki/Lazy_loading) (lazy-load) så att användare bara laddar ned det en given vy behöver, skjut upp icke-kritiskt arbete och föredra plattformsfunktioner framför tunga bibliotek. Optimera bilder och typsnitt, cachelagra effektivt och mät på representativa enheter med låg prestanda och långsamma uppkopplingar.

### Bygg med progressiv förbättring och motståndskraft

Börja från en baslinje som fungerar med semantisk HTML och minimalt eller inget JavaScript och förbättra sedan för kapabla klienter. Det säkerställer att kärnuppgiften förblir möjlig när skript inte laddas, en enhet är gammal eller ett nätverk är ostadigt, en vanlig verklighet snarare än ett gränsfall. Hantera fel elegant: visa användbara tillstånd för laddning, tomt, fel och offline snarare än tomma skärmar eller oändliga snurror. För tjänster människor är beroende av, överväg offline-först-tekniker så att appen förblir användbar genom ryckig uppkoppling och synkroniserar när anslutningen återvänder.

### Säkerställ kompatibilitet över webbläsare, enheter och hjälpmedel

Testa över de webbläsare, enheter och hjälpmedel dina användare faktiskt har, informerat av verklig analys snarare än teamets egna maskiner. Använd progressiv förbättring och funktionsdetektering i stället för att anta att de nyaste plattformsfunktionerna finns överallt. Bygg [responsivt](https://en.wikipedia.org/wiki/Responsive_web_design) (se designsystemkapitlet) så att en kodbas betjänar telefoner till datorer. Integrera tillgänglighet och internationalisering i frontendarkitekturen från start, inte som senare omgångar.

### Styr frontenden som gemensam infrastruktur

Tillhandahåll gemensamma komponentbibliotek, linting, formatering och byggverktyg så att team är konsekventa och produktiva. Etablera arkitekturriktlinjer (hur man strukturerar applikationer, hanterar tillstånd och delar paket) och prestandabudgetar upprätthållna i CI. För mycket stora frontends, överväg modulära eller mikrofrontend-arkitekturer som låter team driftsätta oberoende, men väg den tillagda komplexiteten och prestandakostnaden noga, eftersom de inte är gratis.

## Avvägningar: för- och nackdelar

| Beslut | Fördelar | Nackdelar |
|---|---|---|
| Populärt moget ramverk | Stor talangpool, stabilt, stött | Kan bära äldre tyngd. Långsammare att anta de nyaste funktionerna |
| Nyaste ramverket | Moderna funktioner, prestandavinster | Risk för omsättning, liten talangpool, osäker livslängd |
| SSR / SSG | Snabb första ritning, SEO, fungerar utan JS | Server- eller byggkomplexitet, cachningsutmaningar |
| CSR (SPA) | Rik interaktivitet, appkänsla | Långsam första laddning, JS-beroende, kostnad för SEO och motståndskraft |
| Tungt klientsidigt JavaScript | Rika funktioner | Dålig prestanda på enheter med låg prestanda, skört |
| Progressiv förbättring | Motståndskraftigt, inkluderande, fungerar överallt | Mer designinsats för att definiera en fungerande baslinje |
| Mikrofrontends | Oberoende driftsättningar för team, skala | Komplexitet, duplicerade beroenden, prestandaoverhead |

Den återkommande avvägningen är rikedom och utvecklarbekvämlighet mot räckvidd, prestanda och motståndskraft. Tunga klientsidiga ansatser är trevliga att bygga och demonstrera på snabba maskiner, men de utesluter användare på svaga enheter och nätverk. För företags- och särskilt myndighetspublik, luta balansen mot prestanda, progressiv förbättring och varaktighet, eftersom kostnaden för att utesluta användare är hög och ofta icke förhandlingsbar.

## Frågor att diskutera med ditt team

1. **Hur isolerar vi ramverksspecifik kod så att applikationen inte är gisslan åt ett biblioteks livscykel?** För långlivade företags- och myndighetssystem är ramverksomsättning den största undvikbara utgiften: en omskrivning är dyr och riskabel, och dagens trendande bibliotek begränsar rekrytering och underhåll i åratal. Att luta sig mot webbstandarder och lägga ramverksspecifik kod bakom tydliga gränser betyder att er affärslogik och ert innehåll överlever nästa ramverksskifte. Besluta var dessa sömmar går och om en ny ingenjör kunde skilja plattformskod från ramverkskod. Ta med en uppskattning av vad er senaste ramverksmigrering kostade, eller vad den annalkande kommer att kosta. Om er kärnlogik är fastsvetsad vid ett biblioteks API:er, prissätt den kopplingen innan ni försvarar ramverksvalet.

2. **Matchar vi renderingsstrategi per rutt, eller tvingar vi en strategi på hela produkten?** Serversidig rendering ger snabb första ritning och fungerar utan JavaScript på klienten för publikt innehåll, statisk generering maximerar hastigheten för sidor som sällan ändras och klientrendering passar interaktiva, appliknande ytor bakom inloggning. Att tvinga en globalt antingen saktar ned publika sidor med tungt JavaScript eller överkonstruerar en enkel innehållssida. Det här är en räckviddsfråga för myndigheter, där en tjänst som bara fungerar efter att ett stort paket laddats utesluter användare på gamla enheter och långsamma uppkopplingar. Ta med era viktigaste rutter och märk var och en med den strategi den faktiskt använder i dag. Om en publikt vänd sida behöver JavaScript för att visa sitt innehåll, avgör om det är ett medvetet val eller en olycka.

3. **Hur disciplinerad är vår tillståndshantering, och överförstorar vi allt till ett tungt globalt lager?** Att hålla serverns tillstånd, URL-tillstånd och lokalt UI-tillstånd åtskilda förhindrar den koppling och de omrenderingsstormar som gör stora frontends långsamma och sköra, men den frestande standarden är att dumpa allt i ett globalt lager. Det här ackumuleras i skala, där många team som rör ett gemensamt lager skapar dolda beroenden och oförutsägbar prestanda. Kom överens om var varje slags tillstånd hör hemma och vad som inte hör hemma i det globala lagret. Ta med en komponent som renderas om mer än den borde och spåra varför. Om svaret är ett svullet centralt lager, besluta gränserna innan kopplingen härdar.

4. **Vilka är våra prestandabudgetar, fäller de bygget i CI och mäts de på de enheter våra användare faktiskt har?** En budget ingen upprätthåller är en önskan, och en budget mätt bara på teamets snabba bärbara datorer beskriver en användare som inte finns. För en stor organisation är budgetar den enda mekanism som håller paketstorlek och Core Web Vitals i schack när dussintals team lägger till funktioner på en gemensam yta, eftersom ingen enskild granskare kan fånga varje regression med blotta ögat. Det konkurrerande trycket är leveranshastighet: ett hårt byggfel över några kilobyte känns hindrande tills ni prissätter det övergivande det förhindrar. Ta med era nuvarande budgetar, övervakningsdata från verkliga användare från enheter med låg prestanda och långsamma uppkopplingar och listan över releaser där en regression slank igenom. I myndigheter, där uppdraget är att betjäna hela allmänheten inklusive människor på gamla telefoner och datamätt abonnemang, knyt budgeten till den långsammaste tiondelen av era användare snarare än medianen och gör CI-grinden icke förhandlingsbar.

5. **Vilka av våra tjänster måste fortsätta fungera utan JavaScript på klienten, och har vi faktiskt testat den vägen?** Progressiv förbättring är lätt att påstå och lätt att i tysthet bryta, eftersom den förbättrade vägen är den utvecklare använder varje dag medan baslinjen ruttnar otestad. Att avgöra detta medvetet spelar roll i skala, eftersom många team som levererar till en plattform var och en antar att skript alltid laddas om inte en gemensam standard säger annat, och ett enda hårt beroende kan bryta kärnuppgiften för alla vars paket misslyckas. Avvägningen är verklig: en fungerande baslinje utan JavaScript kostar designinsats och begränsar hur ni bygger interaktivitet. Ta med era kritiska användarresor, ett test som laddar var och en med skript avstängda eller misslyckade och belägg för hur ofta skript genuint misslyckas ladda i fält. För en offentlig tjänst är en bidrags- eller skatteblankett som kollapsar när ett skript får tidsgränsfel inte en degraderad upplevelse, det är en medborgare som inte kan fullgöra en rättslig skyldighet, så behandla baslinjen som ett regelefterlevnadskrav, inte en trevlighet.

6. **När lönar sig mikrofrontends verkligen för sin komplexitet, och vem avgör innan ett team sträcker sig efter en?** Oberoende driftsättningar för team är attraktiva, men mikrofrontends bär komplexiteten hos distribuerade system, duplicerade beroenden och en prestandaskatt användare betalar i långsammare laddningar. Utan en gemensam beslutspunkt antar ambitiösa team dem för organisatorisk bekvämlighet långt innan skalan motiverar kostnaden, och hela produkten ärver overheaden. Den konkurrerande hänsynen är autonomi: team som levererar på en gemensam kodbas kan blockera varandra, och i genuin skala är den kopplingen ett eget dyrt problem. Ta med antalet team som rör ytan, den driftsättningskonkurrens ni faktiskt upplever i dag och en uppmätt uppskattning av den duplicering av nyttolast en uppdelning skulle införa. För företags- och myndighetsplattformar, där arkitekturbeslut binder många team i åratal och måste överleva revision och överlämning, kräv en uttrycklig, dokumenterad tröskel och en ägare som godkänner steget, snarare än att låta varje team avgöra isolerat.

## Sektorsperspektiv

**Startup.** Hastighet och räckvidd spelar båda roll när varje registrering räknas, så stå emot den tunga ensidesappen för publika sidor. Serverrendera din marknadsföring och ditt registreringsflöde så att de laddas snabbt på de mellanklasstelefoner och den ryckiga data dina tidiga kunder använder, och reservera klientsidig interaktivitet för appen bakom inloggning. Sätt en enkel paketstorleksbudget i CI så att ett slarvigt beroende inte i tysthet kan svälla sidan och lita på webbstandarder för att hålla en liten kodbas underhållbar när du anställer.

**Småföretag.** Utan dedikerad frontendspecialist och med snäv budget, föredra ett väl stött vanligt ramverk eller en hostad webbplatsbyggare framför något skräddarsytt, så att du rekryterar från en stor talangpool och köper underhåll snarare än bemannar det. Ramma in valet som varaktighet: det billigaste alternativet är det du inte tvingas skriva om om två år. Insistera på snabba, mobilvänliga sidor och tillgänglig märkning direkt, eftersom en långsam eller trasig kassa kostar dig kunder du inte har råd att förlora.

**Storföretag.** Problemet är konsekvens över många team: ett gemensamt komponentbibliotek, överenskomna arkitekturmönster, linting och byggverktyg samt prestandabudgetar upprätthållna i CI så att inget team i tysthet kan försämra helheten. Välj ramverk för livslängd och rekrytering snarare än nyhet, isolera ramverksspecifik kod bakom gränser för att överleva nästa migrering och matcha renderingsstrategi per yta. Hantera frontenden som gemensam infrastruktur med övervakning av verkliga användare, styrning och ett granskningsbart register över varför varje arkitekturval gjordes.

**Offentlig sektor.** Du betjänar hela allmänheten, inklusive människor på gamla enheter, långsamma eller datamätta uppkopplingar och hjälpmedel, så progressiv förbättring och prestanda är skyldigheter, inte polering. Gör en fungerande baslinje utan JavaScript till en hård regel för medborgarvända tjänster, budgetera sidor mot de långsammaste användarna snarare än medianen och håll kärnuppgiften genomförbar när ett skript fallerar. Upphandling och transparens gäller: föredra varaktig, standardlutande teknik som undviker inlåsning hos en enda leverantör, dokumentera krav på tillgänglighet och prestanda i avtal och kunna visa att tjänsten fungerar för den mest missgynnade användaren, inte bara demoenheten.

## Exempel

**Startup.** En startup i såddfasen frestades att bygga sin marknadsföringssajt och sitt registreringsflöde som en tung ensidesapp, men deras målkunder var shoppare ofta på mellanklasstelefoner över ryckig mobildata. De två grundarna serverrenderade i stället de publika sidorna så att de laddades snabbt och fungerade innan något JavaScript körts och reserverade klientsidig interaktivitet för appen bakom inloggning. De satte en enkel paketstorleksbudget i CI så att ett slarvigt beroende inte i tysthet kunde svälla sidan. Den slimmade, snabba första laddningen förbättrade mätbart registreringarna, och att luta sig mot webbstandarder höll deras lilla kodbas lätt att underhålla när de anställde.

**Storföretag.** Ett finansiellt tjänsteföretag moderniserade en vidsträckt uppsättning interna applikationer och kundapplikationer genom att standardisera på ett moget ramverk, ett gemensamt komponentbibliotek och upprätthållna prestandabudgetar i CI. Renderingsstrategin valdes per yta: serverrenderade, cachebara sidor för publik marknadsföring och innehåll och en klientrenderad applikation bakom inloggning för interaktiva paneler. Paketbudgetar och övervakning av verkliga användare fångade regressioner före release, höll laddningstider snabba över företagets många team och minskade den risk för ramverksomsättning som tidigare tvingat fram kostsamma omskrivningar.

**Offentlig sektor.** Ett nationellt digitalt tjänsteteam byggde medborgarvända tjänster med progressiv förbättring som en hård regel: varje tjänst fungerar med semantisk HTML och serverrendering först, och JavaScript förbättrar bara. Det garanterar att tjänsten fungerar på gamla telefoner, långsamma landsbygdsuppkopplingar och hjälpmedel, befolkningar en regering inte kan utesluta. Prestandabudgetar håller sidor lätta och snabba på enheter med låg prestanda, och elegant degradering betyder att ett misslyckat skript aldrig blockerar någon från att slutföra en bidragsansökan. Resultatet är en tjänst som är snabb, motståndskraftig, tillgänglig och användbar för hela allmänheten.

## Affärsnytta: motiv, ROI och TCO

Frontendval driver intäkter, räckvidd och kostnad. Prestanda är direkt knuten till konvertering, engagemang och uppgiftsslutförande. Snabbare upplevelser överträffar mätbart långsammare, och för användare på svaga enheter är prestanda gränsen mellan att använda tjänsten och att överge den. Progressiv förbättring och stöd över enheter vidgar den adresserbara publiken, vilket för myndigheter är ett uppdrag och för företag är marknadsandel. Sunda ramverks- och arkitekturval minskar frekvensen och kostnaden för omskrivningar, den största undvikbara utgiften i frontendutveckling.

Vad gäller total ägandekostnad är kostnaderna för att anta disciplinen med prestandabudgetar och testning, insatsen för progressiv förbättring och investeringen i gemensamma verktyg och komponentbibliotek. Kostnaden för att inte anta betalas i långsamma upplevelser som förlorar användare och intäkter, uteslutning av användare med låg prestanda och hjälpmedel (med rättslig exponering inom myndigheter), sköra applikationer som går sönder i fält och dyr ramverksomsättning och omskrivningar drivna av att jaga trender. Frontendproblem visar sig som diffust övergivande och supportbörda snarare än en enskild kostnadspost, så de är lätta att underinvestera i.

För att driva ärendet inför ledningen, koppla Core Web Vitals och laddningstider till konverterings- och slutförandetrattar, kvantifiera de användare som utesluts av tunga klientsidiga ansatser och prissätt kostnaden för tidigare eller annalkande omskrivningar mot stabiliteten i en varaktig, standardlutande arkitektur. Ramma in prestandabudgetar och progressiv förbättring som riskminskning och räckviddsexpansion.

## Antimönster och fallgropar

- **Ramverksjakt**: att skriva om på det senaste biblioteket och ådra sig omsättning utan användarnytta.
- **Upplevelser enbart med JavaScript**: ingenting fungerar förrän ett stort paket laddats och körts, vilket utesluter många användare.
- **Att bara testa på snabba enheter**: teamets flaggskeppsdatorer döljer den verkliga användarupplevelsen.
- **Att ignorera paketstorlek**: obegränsad tillväxt av beroenden tills sidor är långsamma överallt.
- **Ingen prestandabudget**: regressioner ackumuleras i tysthet release för release.
- **Fel med tom skärm**: inga tillstånd för laddning, tomt, fel eller offline. En misslyckad begäran bryter sidan.
- **Överförstorat globalt tillstånd**: allt i ett lager, vilket skapar koppling och omrenderingsstormar.
- **För tidiga mikrofrontends**: komplexitet hos distribuerade system och duplicerade nyttolaster utan skalan att motivera dem.
- **Att försumma tillgänglighet och i18n i arkitekturen**: att skruva på dem senare till hög kostnad.

## Mognadsmodell

**Nivå 1: Initiera.** Ad hoc-frontend byggd per team utan gemensamma standarder. Tung klientsidig kod, inga prestandabudgetar, testad bara på teamets egna enheter. Ramverksval görs efter preferens eller hype, och ett misslyckat skript kan lämna användare stirrande på en tom skärm.

**Nivå 2: Utveckla.** Vissa team antar gemensamma verktyg och ett komponentbibliotek, men praxis är inkonsekvent över organisationen. Prestanda mäts ibland snarare än budgeteras eller upprätthålls. Renderingsstrategin är ofta enhetlig oavsett innehållstyp, och testning över enheter är begränsad och manuell.

**Nivå 3: Standardisera.** Ramverk och arkitektur väljs medvetet för livslängd, och valen är dokumenterade och upprätthållna i hela organisationen. Renderingsstrategin matchas per yta, progressiv förbättring och elegant degradering är standard, och gemensamma komponentbibliotek, linting och byggverktyg gäller för varje team. Stöd över webbläsare, tillgänglighet och internationalisering är inbyggda snarare än påskruvade.

**Nivå 4: Hantera.** Frontenden mäts och styrs med data. Prestandabudgetar upprätthålls i CI så att regressioner fäller bygget, och Core Web Vitals följs med övervakning av verkliga användare från faktiska enheter med låg prestanda och långsamma uppkopplingar mot uttryckliga utgångslägen. Paketstorlek, täckning av fel- och offlinetillstånd och andelen användare som betjänas på de långsammaste uppkopplingarna rapporteras och granskas, så att beslut vilar på belägg snarare än åsikt.

**Nivå 5: Orkestrera.** Prestanda, motståndskraft och räckvidd förbättras kontinuerligt och knyts till affärsutfall i hela organisationen. Frontenden lutar sig mot webbstandarder för varaktighet, isolerar ramverksberoenden så att migreringar är billiga och utvecklar arkitekturen adaptivt när enheter, plattformen och data från verkliga användare skiftar. Hela allmänheten och alla enheter är förstklassiga, och frontendpraxis är integrerad med design, tillgänglighet och produktplanering snarare än behandlad som en separat fråga.

## Idéer för diskussion

- Hur avgör ni när en ramverksmigrering är värd sin kostnad och risk?
- Vilka Core Web Vitals och paketbudgetar bör vara hårda byggfällande trösklar?
- Var är progressiv förbättring väsentlig, och var är en klientsidig app acceptabel?
- Hur håller ni frontendarkitekturen konsekvent över många autonoma team?
- När lönar sig mikrofrontends verkligen för sin komplexitet?
- Hur bör testning på verkliga enheter och långsamma nätverk byggas in i pipelinen?

## Viktigaste punkter

- Frontenden körs i en miljö du inte kontrollerar: designa för variation och fel.
- Välj varaktig, väl stödd teknik för långlivade system. Lita på webbstandarder.
- Matcha renderingsstrategi (SSR, SSG, CSR, strömning) mot innehåll och behov, ofta blandad per rutt.
- Behandla prestanda som en budgeterad, mätt disciplin upprätthållen i CI med data från verkliga användare.
- Bygg med progressiv förbättring så att kärnupplevelsen fungerar överallt.
- Skicka mindre JavaScript: koddela, ladda lätt och föredra plattformsfunktioner.
- För myndigheter särskilt är prestanda och motståndskraft förutsättningar för jämlik tillgång.

## Referenser och vidare läsning

- Jeremy Keith, *Resilient Web Design*
- Aaron Gustafson, *Adaptive Web Design* (progressive enhancement)
- Steve Souders, *High Performance Web Sites*
- Ilya Grigorik, *High Performance Browser Networking*
- Addy Osmani, writings on performance, code-splitting, and the cost of JavaScript
- Google, *Web Vitals* and web.dev performance guidance
- MDN Web Docs, web platform and progressive enhancement references
- Alex Russell, essays on the cost of JavaScript and device diversity
- UK Government Digital Service, progressive enhancement and frontend guidance
- WHATWG HTML Living Standard and W3C web platform specifications
