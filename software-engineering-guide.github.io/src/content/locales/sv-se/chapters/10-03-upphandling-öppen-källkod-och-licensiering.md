# 10.3 Upphandling, öppen källkod och licensiering

## Översikt och motivation

Nästan varje modernt programvarusystem är till största delen sammansatt av komponenter någon annan skrev. [Programvara med öppen källkod](https://en.wikipedia.org/wiki/Open-source_software) bildar grunden för operativsystem, språk, ramverk, databaser och molninfrastruktur. Den kommer in i företaget på två sätt: genom medveten [upphandling](https://en.wikipedia.org/wiki/Procurement) och genom enskilda utvecklares tillfälliga `import`-satser. Det här kapitlet handlar om att göra den konsumtionen (och, där det passar, bidraget) medvetet. Det betyder en strategi, licensefterlevnad, en förståelse för skyldigheter och copyleft-risk och en plan för det oundvikliga [livscykelslutet](https://en.wikipedia.org/wiki/End-of-life_(product)) för de komponenter ni beror på.

För stora team är insatserna rättsliga, operativa och strategiska på en gång. Rättsligt är [licenser](https://en.wikipedia.org/wiki/Software_license) för öppen källkod verkställbara avtal med verkliga skyldigheter. Att göra [copyleft](https://en.wikipedia.org/wiki/Copyleft) (licensiering som kan kräva att härledda verk delas på samma villkor) fel kan i värsta fall tvinga fram utlämnande av proprietär källkod eller utlösa rättsprocess. Licensöverträdelser kan till och med blockera ett förvärv eller en börsnotering under [due diligence](https://en.wikipedia.org/wiki/Due_diligence). Operativt ruttnar ohanterade beroenden: komponenter blir ounderhållna, ackumulerar sårbarheter och når livscykelslut medan de fortfarande ligger djupt begravda i produktion. Strategiskt är öppen källkod mer än en kostnadsbesparande insats. Det är ett sätt att undvika [inlåsning](https://en.wikipedia.org/wiki/Vendor_lock-in), attrahera talang och forma de ekosystem ni beror på, fördelar ni bara fångar om ni engagerar er med avsikt.

Myndigheter har en tillagd dimension. Många jurisdiktioner har nu uttryckliga policyer som gynnar öppen källkod, öppna standarder och koddelning mellan myndigheter. Dessa uttrycks ofta som "offentliga pengar, offentlig kod": principen att programvara finansierad av skattebetalarna som standard bör vara tillgänglig för allmänheten. Så ingenjörer i offentlig sektor måste navigera både licensefterlevnad och aktiva mandat att föredra, publicera och återanvända öppen källkod. Det här kapitlet syftar till att göra allt detta hanterbart i skala.

## Nyckelprinciper

- **Öppen källkod är en leveranskedja, inte gratisgrejer.** Behandla konsumerade komponenter med samma stringens som vilken kritisk leverantör som helst.
- **Licenser är skyldigheter, inte tillstånd att ignorera.** Varje beroende bär villkor. Känn till dem innan ni levererar.
- **Copyleft är en designbegränsning, inte ett tabu.** Copyleft-licenser är användbara och värdefulla. De kräver bara att ni förstår hur ni kombinerar och distribuerar programvara.
- **Konsumera medvetet, bidra strategiskt.** Avgör vad ni ska föra in och, där det tjänar er, investera i att skicka uppströms snarare än att förgrena.
- **Inventera allt.** Ni kan inte följa, säkra eller uppdatera det ni inte kan se. En SBOM (materiallista för programvara, en fullständig inventering av komponenterna i er programvara) är minimikrav.
- **Planera för livscykelslut från början.** Varje beroende blir en dag ounderhållet. Känn till din utväg innan du tvingas ut.
- **I myndigheter, välj öppet som standard.** Föredra [öppna standarder](https://en.wikipedia.org/wiki/Open_standard) och öppen källkod och publicera kod för offentliga pengar om det inte finns ett specifikt skäl att inte göra det.

## Rekommendationer

### Sätt en strategi för öppen källkod och en konsumtionspolicy

Publicera en tydlig policy för hur utvecklare får föra in öppen källkod i organisationen: vilka licenser som är förgodkända, vilka som kräver granskning och vilka som är förbjudna för era användningsfall. Tillhandahåll en snabb godkännandeväg med låg friktion. En policy långsammare än att kopiera kod kommer helt enkelt att ignoreras. Skilj på sammanhang, eftersom samma licens beter sig olika när en komponent används internt som en tjänst, bäddas in i en distribuerad produkt eller länkas in i en proprietär applikation. Gör den enkla vägen till den regelefterlevande vägen: ett kurerat internt repositorium av granskade komponenter, automatisk skanning i pipelinen och tydlig vägledning utvecklare kan följa utan att ringa en jurist för rutinfall.

### Hantera licensefterlevnad, skyldigheter och copyleft-risk

Lär känna licensfamiljerna och deras skyldigheter. [Permissiva licenser](https://en.wikipedia.org/wiki/Permissive_software_license) (som MIT, BSD och Apache 2.0) kräver främst erkännande och bevarande av meddelanden. Apache 2.0 lägger till ett uttryckligt patentmedgivande. Svag copyleft (som [LGPL](https://en.wikipedia.org/wiki/GNU_Lesser_General_Public_License) och MPL) kräver att ni delar ändringar av de omfattade filerna men låter er i allmänhet kombinera med proprietär kod. Stark copyleft (som [GPL](https://en.wikipedia.org/wiki/GNU_General_Public_License)) kan kräva att hela det distribuerade verket erbjuds på samma villkor. Nätverks-copyleft ([AGPL](https://en.wikipedia.org/wiki/GNU_Affero_General_Public_License)) utvidgar den skyldigheten till programvara som erbjuds över ett nätverk, inte bara distribueras som binärer. De skyldigheter som spelar mest roll hänger på två saker: om ni distribuerar programvaran och hur tätt ni kombinerar komponenter. Automatisera efterlevnad: skanna beroenden för licenser, generera och leverera de erkännande- och meddelandefiler som krävs och grinda bygget på policy så att en förbjuden licens inte i tysthet kan komma in i produktion.

### Etablera ett kontor för öppen källkod (OSPO)

Om ni konsumerar öppen källkod i skala, skapa en samlingspunkt, ett OSPO, som äger strategi för öppen källkod, policy, efterlevnadsverktyg, bidragsstyrning och gemenskapsrelationer. OSPO:t tämjer kaoset av att varje team fattar egna beslut. Det ger expertis enskilda team inte kan upprätthålla. Och det fångar strategiskt värde: att avgöra vilka projekt man ska investera i, när man ska bidra uppströms och hur man släpper sina egna projekt med öppen källkod väl. Även ett litet OSPO (ibland en person plus en tvärfunktionell arbetsgrupp) förbättrar konsekvens dramatiskt och minskar rättslig risk jämfört med ett fritt fram.

### Styr bidrag och, där det passar, publicering

Avgör medvetet när ni ska bidra tillbaka. Att skicka rättelser och funktioner uppströms till projekt ni beror på minskar er underhållsbörda, eftersom ni slutar bära privata lappar. Det bygger också välvilja och inflytande och stärker komponenter som är kritiska för er. Ge utvecklare en tydlig, snabb process för godkända bidrag, inklusive hur immateriella rättigheter och bidragsgivaravtal hanteras. När ni släpper egna projekt med öppen källkod, gör det ordentligt: välj en lämplig licens, dokumentera styrning och förbind er till förvaltarskap. Ett övergivet projekt skadar ert rykte mer än inget projekt.

### Uppfyll myndigheters mandat om öppen källkod och "offentliga pengar, offentlig kod"

Team i offentlig sektor bör behandla öppenhet som standard. Föredra öppna standarder för att undvika inlåsning och för att arbeta över myndigheter och leverantörer. Publicera källkod utvecklad med offentliga medel öppet, om inte ett specifikt, dokumenterat undantag gäller: för säkerhetskänsliga komponenter, tredje parts rättigheter eller integritetsfrågor. Återanvänd innan ni bygger: kontrollera om en annan myndighet redan släppt lämplig kod. Baka in dessa förväntningar i upphandlingen, så att leverantörer levererar öppen, återanvändbar, väldokumenterad kod med staten behållande lämpliga rättigheter, snarare än proprietära svarta lådor myndigheten inte kan underhålla eller dela.

### Hantera beroenden och programvara vid livscykelslut

Underhåll en levande inventering (SBOM) av varje komponent och dess version, licens och underhållsstatus. Håll beroenden rimligt aktuella. Små, frekventa uppdateringar är långt billigare och säkrare än sällsynta, stora språng. Bevaka uppströmsprojekt för tillkännagivanden om livscykelslut och säkerhetsstödsfönster och planera migreringar innan stödet tar slut, inte efter att en sårbarhet tvingar fram en kapplöpning. För kritiska komponenter med risk för övergivande, avgör i förväg om ni ska finansiera underhållaren, bidra med underhåll själva, förgrena eller ersätta. Följ livscykelslut för både kommersiell programvara och öppen källkod och håll att ta slut på stöd till samma standard som vilken annan operativ risk som helst.

## Avvägningar: för- och nackdelar

| Val | Fördelar | Nackdelar |
|---|---|---|
| Konsumera öppen källkod fritt | Snabb leverans. Enorm hävstång. Inga licensavgifter | Licens-, säkerhets- och underhållsskyldigheter ni nu äger |
| Strikt tillåtelselista för licenser | Låg rättslig risk. Förutsägbart | Saktar ner team. Kan utesluta genuint användbara komponenter |
| Endast permissiva licenser | Minimala skyldigheter. Lätt att kombinera | Avstår från värdefulla copyleft-projekt. Mindre ömsesidighet |
| Acceptera copyleft där det passar | Tillgång till starka ekosystem. Fördelar av ömsesidighet | Kräver omsorg vid kombination och distribution |
| Bidra uppströms | Mindre börda av privata lappar. Inflytande. Välvilja | Löpande insats. Overhead för IP och process |
| Bygg proprietärt i stället | Full kontroll. Inga externa skyldigheter | Hög kostnad. Uppfinner standardvara på nytt. Ni underhåller det för evigt |
| Myndigheters publicering som standard | Transparens. Återanvändning. Undviker inlåsning | Publiceringsinsats. Säkerhetsgranskning. Bibehållet förvaltarskap |

Den centrala spänningen är mellan utvecklarfart och kontroll. Lås allt bakom tung granskning och utvecklare går runt policyn. Det skapar ohanterade skuggberoenden, som är värre än ett tillåtande-men-synligt tillvägagångssätt. Lämna det helt okontrollerat och ni ackumulerar rättslig och säkerhetsskuld osynligt. Lösningen är automatisering och kuratering: gör den regelefterlevande vägen till den snabbaste vägen, genom förgranskade komponenter, pipelineskanning och tydliga standardvärden, så att ni får kontroll utan friktion. Vad gäller copyleft är avvägningen inte "riskabelt mot säkert" utan "förstått mot inte". Copyleft är helt användbart när ni vet hur ni kombinerar och distribuerar.

## Frågor att diskutera med ditt team

1. **Vad är er uttryckliga regel för stark copyleft och nätverks-copyleft över interna, distribuerade och nätverksbetjänade sammanhang?** Copyleft är en designbegränsning, inte ett tabu, och skyldigheterna hänger på två saker: om ni distribuerar programvaran och hur tätt ni kombinerar komponenter. GPL i ett internt verktyg beter sig mycket annorlunda än GPL länkad in i en produkt ni levererar, och AGPL utvidgar utlämnandeskyldigheter till programvara ni bara erbjuder över ett nätverk, vilket ändrar er kalkyl bygga-mot-anta för allt ni kör som en tjänst. Skriv ner regeln per sammanhang, så att en utvecklare utan att ringa en jurist vet att (till exempel) permissiv är förgodkänd överallt, stark copyleft är okej internt men blockerad från den levererade produkten och AGPL behöver granskning innan den rör en nätverksbetjänad tjänst. Ta med belägg: skanna ert nuvarande beroendeträd och hitta var copyleft-komponenter redan sitter i förhållande till er distributionsgräns. Grinda sedan bygget på den policyn, eftersom en regel ingen skanner upprätthåller är en regel utvecklare av misstag kommer att bryta.

2. **Behöver ni ett kontor för öppen källkod, och vem äger licenspolicy, skanning och bidragsbeslut i dag?** Om det ärliga svaret är "ingen" eller "varje team avgör" kör ni ett fritt fram som ackumulerar rättslig och säkerhetsskuld osynligt. Ett OSPO, även en person plus en tvärfunktionell arbetsgrupp, tämjer det kaoset och fångar strategiskt värde: vilka uppströmsprojekt man ska investera i, när man ska bidra och hur man släpper sina egna projekt väl. Ta med belägg till mötet: kan någon producera den nuvarande godkända licenslistan, SBOM:en och namnet på personen som skulle besvara en copyleft-fråga under due diligence vid förvärv? Svaret bör tilldela tydligt ägarskap och göra den regelefterlevande vägen till den snabbaste vägen, genom förgranskade komponenter och pipelineskanning, så att utvecklare får kontroll utan friktion. En policy långsammare än att kopiera kod kommer helt enkelt att ignoreras.

3. **Vilka beroenden skulle skada mest om de övergavs i morgon, och vad är ert förbestämda svar för var och en?** Varje beroende når livscykelslut så småningom, och den dyra versionen av den händelsen är att upptäcka att en kärnkomponent förlorade stöd för månader sedan, först när en sårbarhet tvingar fram uppmärksamhet. För era kritiska komponenter med risk för övergivande, avgör i förväg om ni ska finansiera underhållaren, bidra med underhåll själva, förgrena eller ersätta. Ta med belägg: från er SBOM, lista de komponenter vars fel skulle stoppa en intäkts- eller uppdragskritisk tjänst och notera var och ens underhållsstatus och säkerhetsstödsfönster. Svaret bör förvandla livscykelslut från en överraskning till en spårad operativ risk med en planerad migrering, hållen till samma standard som vilken annan risk som helst. Att hålla beroenden aktuella i små, frekventa steg är långt billigare än det sällsynta, stora, påtvingade språnget.

4. **Kan ni producera en fullständig, aktuell SBOM som når hela vägen ned i ert transitiva beroendeträd, och hur fort?** När en rubriksättande sårbarhet landar i ett vitt använt bibliotek är den första frågan ledningen ställer "är vi exponerade, och var?" Ett team som inte kan svara inom timmar ligger redan efter, eftersom den verkliga risken vanligen gömmer sig flera lager ned i beroenden ingen valde med avsikt. Den konkurrerande hänsynen är kostnad och brus: fullständig transitiv inventering över många tjänster genererar en stor, skiftande lista, och överlarmning lär människor att ignorera den, så ni måste avgöra vilket djup och vilken allvarlighetsgrad som faktiskt utlöser åtgärd. Ta med belägg till diskussionen: försök generera en färsk SBOM för en produktionstjänst just nu, räkna hur många komponenter som är direkta mot transitiva och tidta hur lång tid det tog. För ett företag eller en myndighet, knyt detta till ett konkret mål för incidentsvar och till varje rättslig skyldighet att redovisa berörda komponenter, eftersom ett mandat att rapportera exponering ni inte kan räkna upp är ett mandat ni kommer att bryta.

5. **När är ett kritiskt beroende värt att finansiera, bidra till eller förvalta, snarare än behandla som gratis?** De flesta organisationer konsumerar öppen källkod som om den vore ett allmännyttigt verk, och blir sedan chockade när en komponent som bär en intäktstjänst visar sig vara en obetald volontär. Att medvetet besluta att finansiera en underhållare, skicka rättelser uppströms eller släppa och förvalta ett eget projekt förvandlar en skör gratisinsats till en varaktig, påverkad en, och det hindrar era ingenjörer från att bära privata lappar genom varje uppgradering. Spänningen är att bidrag och förvaltarskap kostar verklig, löpande ingenjörstid och bär overhead för immateriella rättigheter och process, så ni kan inte göra det för allt. Ta med belägg: från er SBOM, markera de få komponenter vars fel skulle stoppa en uppdragskritisk tjänst och notera var och ens antal underhållare, finansiering och hur många privata lappar ni redan bär mot den. För en stor eller offentlig organisation, väg anseendekostnaden för en övergiven öppen källkodsrelease ni publicerade med pompa och ståt och i myndigheter, behandla bibehållet förvaltarskap av publicerad kod för offentliga pengar som en del av leveransen, inte ett valfritt tillägg.

6. **Levererar er upphandling faktiskt öppen, återanvändbar, väldokumenterad kod med de rättigheter ni behöver, eller proprietära svarta lådor ni inte kan underhålla eller lämna?** Avtal skrivna utan expertis i öppen källkod lämnar rutinmässigt en leverantör kontroll ni kommer att ångra: slutna format, ingen rätt att publicera eller ändra och beroenden myndigheten inte kan lappa när leverantören går vidare. Att få detta rätt tidigt är långt billigare än att upptäcka vid förnyelse att ni inte kan lämna. De konkurrerande hänsynen är fart och leverantörsval: att kräva öppna leveranser och portabilitet kan snäva in fältet och sakta ner en tilldelning, och vissa genuint användbara leverantörer motsätter sig det. Ta med belägg: dra två nyliga avtal och kontrollera om de specificerar licensvillkor, leverans av källkod, dokumentationsstandarder, tillhandahållande av SBOM och de rättigheter organisationen behåller. För företagsupphandling, koppla detta till inlåsning och analys av total kostnad. För myndigheter, koppla det till öppet som standard och mandat om "offentliga pengar, offentlig kod" och till den dokumenterade undantagsprocess som låter er stänga bara de säkerhetskänsliga delarna snarare än hela systemet.

## Sektorsperspektiv

**Startup.** Du sätter ihop nästan allt från öppen källkod och har ingen jurist, så håll regeln till en sida: permissiva licenser som MIT och Apache 2.0 är förgodkända, stark copyleft är okej för internt verktyg men blockerad från den levererade produkten och allt udda får en snabb grundargranskning. Lägg till en licens- och sårbarhetsskanning i pipelinen och håll en SBOM från dag ett, eftersom det billigaste ögonblicket att få detta rätt är före en förvärvares due diligence kammar ditt beroendeträd. Förbjud inte copyleft av rädsla. Förstå det och gå vidare.

**Småföretag.** Utan specialist på öppen källkod och med snäv budget, lita på verktyg snarare än personal: en skanner i bygget och en kort lista över godkända licenser gör det mesta av det en person skulle göra. Ramma in konsumtion som köpa-mot-bygga ärligt, eftersom att uppfinna en välunderhållen öppen komponent på nytt vanligen är det dyra valet, men det är också att bero på en du aldrig inventerar. Håll ett enkelt register över vad du använder och under vilken licens, så att ett kundens säkerhetsformulär eller ett sårbarhetslarm inte blir en kapplöpning.

**Storföretag.** I skala är problemet konsekvens över många team, så sätt upp ett OSPO som äger policy, automatisk skanning, generering av erkännanden och bidragsstyrning och gör den regelefterlevande vägen till den snabbaste vägen genom kurerade, förgranskade komponenter. Upprätthåll copyleft-regler per sammanhang i pipelinen, underhåll SBOM:er över tjänster och hantera beroendens aktualitet och livscykelslut som spårad operativ risk. Behandla öppen källkod som leveranskedjehantering för majoriteten av din kodbas, med revisionsklara belägg för due diligence vid förvärv.

**Offentlig sektor.** Öppenhet är ofta påbjuden, inte valfri, så välj öppna standarder som standard och publicera kod för offentliga pengar om inte ett dokumenterat undantag gäller för säkerhet, tredje parts rättigheter eller integritet. Återanvänd innan du bygger genom att kontrollera en katalog över myndigheter, och baka in öppna, återanvändbara, väldokumenterade leveranser och behållna rättigheter i upphandlingen så att du får underhållbar kod snarare än proprietära svarta lådor. Håll publicerad kod till verkligt förvaltarskap och håll undantagsprocessen snäv och transparent så att den stänger bara det den måste.

## Exempel

**Startup.** Ett startup på fyra personer som bygger en mobilapp sätter ihop nästan allt från öppen källkod och har ingen jurist anställd. I stället för att förbjuda copyleft av rädsla skriver grundarna en policy på en sida: permissiva licenser som MIT och Apache 2.0 är förgodkända, stark copyleft som GPL är okej för internt verktyg men blockerad från den levererade appen för att undvika utlämnandeskyldigheter och allt ovanligt får en snabb grundargranskning. De lägger till en licens- och sårbarhetsskanning i pipelinen så att en förbjuden licens inte kan slinka in i en release, håller en SBOM från dag ett och skickar en liten rättelse uppströms till ett kritiskt bibliotek så att de slutar bära en privat lapp genom varje uppgradering. Att få detta rätt tidigt besparar dem också en smärtsam överraskning när en förvärvares due diligence så småningom kammar beroendeträdet.

**Storföretag.** En programvaruleverantör som levererar en distribuerad produkt driver ett OSPO. OSPO:t underhåller en godkänd licenslista, ett internt kurerat komponentrepositorium och automatisk licens- och sårbarhetsskanning i varje pipeline. När en utvecklare drar in ett nytt beroende kontrollerar pipelinen dess licens mot policy, genererar de erkännanden som levereras med produkten och flaggar allt som kräver granskning. Komponenter med stark copyleft tillåts för internt verktyg men blockeras från den distribuerade produkten, för att undvika utlämnandeskyldigheter. Företaget skickar rättelser uppströms till några kritiska beroenden. Det eliminerade en backlogg av privata lappar dess ingenjörer brukade bära över varje uppgradering.

**Offentlig sektor.** En nationell digital tjänst verkar under en policy om "offentliga pengar, offentlig kod". Nya tjänster byggs på öppna standarder, utvecklas öppet i ett publikt kodrepositorium som standard och återanvänds över myndigheter. Dess upphandlingsmallar kräver att leverantörer levererar öppen, väldokumenterad, återanvändbar kod, med staten behållande rättigheter att publicera och ändra. Innan en ny komponent påbörjas söker team i en katalog över myndigheter efter befintlig återanvändbar kod. Säkerhetskänsliga moduler undantas från publicering genom en dokumenterad process, snarare än genom att göra hela systemet slutet.

## Affärsnytta: motiv, ROI och TCO

Att hantera öppen källkod väl är skillnaden mellan att fånga dess enorma hävstång och att betala för dess dolda kostnader. Öppen källkod låter en stor organisation stå på en grund den aldrig hade råd att bygga. Men [total ägandekostnad](https://en.wikipedia.org/wiki/Total_cost_of_ownership) inkluderar efterlevnad, säkerhetspatchning och eventuell migrering, kostnader som anländer oavsett om ni planerar för dem. Medveten hantering omvandlar oförutsägbara, dyra kriser till små, jämna, planerade kostnader. Dessa kriser inkluderar en copyleft-överträdelse funnen under due diligence vid förvärv, en akut migrering bort från en övergiven komponent eller en sårbarhet i ett beroende ingen visste fanns.

Adoptionskostnaden är blygsam jämfört med exponeringen: ett OSPO eller en arbetsgrupp, skanningsverktyg och disciplinen att hålla en inventering. Kostnaden för att *inte* anta visar sig som rättsligt ansvar, misslyckad due diligence, säkerhetsincidenter spårade till opatchade beroenden och den ackumulerande utgiften för uppskjutna uppgraderingar som så småningom tvingar fram smärtsamma big bang-migreringar. När ni driver ärendet inför ledningen, ramma in hantering av öppen källkod som leveranskedjehantering för majoriteten av er kodbas. Notera även den strategiska uppsidan: undviken inlåsning, snabbare leverans, talangattraktion och inflytande över de ekosystem ni beror på. I myndigheter, lägg till mandatdimensionen. Öppenhet krävs ofta, är inte valfri, och att göra det väl undviker både bristande efterlevnad och duplicerade offentliga utgifter.

## Antimönster och fallgropar

- **Kopiera-klistra-licensiering.** Utvecklare som drar in komponenter utan licenskontroll och upptäcker skyldigheter först vid revision eller förvärv.
- **Ingen inventering.** Att inte kunna besvara "vad använder vi och under vilken licens?" när en sårbarhet eller licensfråga bryter ut.
- **Copyleft-panik.** Att förbjuda all copyleft av rädsla snarare än förståelse och avstå från värdefulla ekosystem.
- **Den övergivna öppna källkodsreleasen.** Att publicera ett projekt med pompa och ståt och sedan aldrig underhålla det, vilket skadar anseendet.
- **Att ignorera transitiva beroenden.** Att granska direkta beroenden medan den verkliga risken gömmer sig flera lager ned.
- **Överraskning vid livscykelslut.** Att upptäcka att en kärnkomponent förlorade stöd för månader sedan, först när en sårbarhet tvingar fram uppmärksamhet.
- **Policy långsammare än att kopiera.** En efterlevnadsprocess så tung att utvecklare går runt den och skapar osynliga skuggberoenden.
- **Myndigheters svarta lådor.** Att upphandla proprietära system myndigheten inte kan underhålla, dela eller lämna, i strid med principerna om öppet som standard.

## Mognadsmodell

**Nivå 1: Initiera.** Utvecklare lägger fritt till öppen källkod utan policy eller inventering. Licenser är ogranskade och copyleft-skyldigheter okända. Livscykelslut upptäcks av en slump, vanligen när en sårbarhet tvingar fram uppmärksamhet. Ingen äger strategin för öppen källkod.

**Nivå 2: Utveckla.** En grundläggande policy och en godkänd licenslista finns, och vissa team följer dem. Skanning sker, men ofta manuellt, sent eller bara på några få projekt. En inventering hålls för stora system medan transitiva beroenden förblir okartlagda. Bidrag och hantering av livscykelslut är ad hoc och inkonsekventa mellan team.

**Nivå 3: Standardisera.** Ett OSPO eller motsvarande äger strategi, policy och verktyg i hela organisationen. Licens- och sårbarhetsskanning är automatisk i varje pipeline, erkännande- och meddelandefiler genereras automatiskt och bygget grindas så att en förbjuden licens inte kan komma in. SBOM:er underhålls ned i det transitiva trädet, bidrag följer en dokumenterad process, livscykelslut spåras med planerade migreringar och myndighetsteam publicerar som standard.

**Nivå 4: Hantera.** Programmet mäts och styrs mot utgångslägen. Ni följer policyskanningstäckning över tjänster, genomsnittlig tid att patcha en offentliggjord beroendesårbarhet, andelen komponenter inom sitt säkerhetsstödsfönster, licensöverträdelsers undkomstfrekvens, eftersläpning i beroendens aktualitet och antalet privata lappar skickade uppströms. Placeringen av copyleft i förhållande till distributionsgränsen övervakas, och mått mot mål driver varje go- eller no-go-beslut snarare än åsikt.

**Nivå 5: Orkestrera.** Öppen källkod är en kontinuerligt förbättrad strategisk tillgång integrerad i hela organisationen. Efterlevnad är helt automatiserad och icke-efterlevande komponenter kan inte nå produktion. Ni investerar medvetet i kritiska uppströmsprojekt, bidrar rutinmässigt och förvaltar egna välskötta projekt. Beroendens aktualitet och livscykelslut hanteras adaptivt när risk och mått skiftar, och öppenhet blir en genuin konkurrens- och medborgerlig fördel.

## Idéer för diskussion

- Var går den rätta gränsen mellan ett snabbt permissivt standardval och den kontroll som behövs för att undvika rättslig och säkerhetsskuld?
- När bör en organisation finansiera eller underhålla ett kritiskt uppströmsberoende snarare än behandla det som gratis?
- Hur avgör ni vilka av era egna komponenter som är värda att släppas och förvaltas som öppen källkod?
- För myndigheter, vad är en försvarbar process för att undanta komponenter från publicering som standard utan att urholka principen?
- Hur djupt in i transitiva beroenden måste licens- och säkerhetsgranskning realistiskt gå?
- Ändrar nätverks-copyleft (AGPL) er kalkyl bygga-mot-anta för programvara ni erbjuder som en tjänst?

## Viktigaste punkter

- Öppen källkod är majoriteten av de flesta kodbaser och måste hanteras som en leveranskedja, inte behandlas som gratis och utan konsekvenser.
- Licenser bär verkliga skyldigheter. Förstå familjerna permissiv, svag copyleft, stark copyleft och nätverks-copyleft och hur distribution och kombination utlöser plikter.
- Gör den regelefterlevande vägen till den snabbaste vägen genom kuratering, automatisk skanning och tydliga standardvärden, annars går utvecklare runt policyn.
- Sätt upp ett OSPO som äger strategi, efterlevnad, bidrag och förvaltarskap i skala.
- Underhåll en SBOM, håll beroenden aktuella i små steg och planera för livscykelslut innan det tvingar fram en kris.
- I myndigheter, välj öppna standarder som standard och publicera kod för offentliga pengar, återanvänd innan du bygger.

## Referenser och vidare läsning

- Heather Meeker, *Open (Source) for Business* and *Open Source for Business*
- Van Lindberg, *Intellectual Property and Open Source*
- The Linux Foundation and TODO Group, *OSPO guides* and *Open Source Program Office resources*
- OpenChain (ISO/IEC 5230), *Open Source Licence Compliance*
- Software Package Data Exchange (SPDX, ISO/IEC 5962) specification
- CycloneDX SBOM specification
- Free Software Foundation, *GNU General Public Licence* and *GPL FAQ*
- Open Source Initiative, *The Open Source Definition* and approved licence list
- Free Software Foundation Europe, *Public Money, Public Code*
- U.S. Federal Source Code Policy and Code.gov guidance
- UK Government, *Technology Code of Practice* and open-standards principles
