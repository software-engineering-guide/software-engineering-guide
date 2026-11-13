# 10.18 Kontor för öppen källkod (OSPO) och bidrag uppströms

## Översikt och motivation

Er organisation kör redan på [öppen källkod](https://en.wikipedia.org/wiki/Open-source_software): operativsystemen, språken, databaserna och biblioteken som bär er produkt är mestadels skrivna av människor som inte arbetar för er. Kapitel 10.3 behandlar upphandling och licensefterlevnad, och kapitel 10.12 behandlar valet mellan öppet och slutet. Det här kapitlet handlar om den funktion som gör allt det sammanhängande: ett [kontor för öppen källkod](https://en.wikipedia.org/wiki/Open_Source_Program_Office) (OSPO, open source program office), teamet som äger hur företaget konsumerar, bidrar till och släpper öppen källkod. Ett OSPO är tyngdpunkten för en relation som annars är utspridd över varje ingenjör som skriver `import`.

De flesta organisationer backar in i öppen källkod ett beroende i taget och upptäcker sedan den ackumulerade exponeringen på en gång: en licensfråga under due diligence vid ett förvärv, ett kritiskt bibliotek med en utmattad underhållare, ett säkerhetsmeddelande i kod ingen visste att de levererade. Ett OSPO förvandlar den villervallan till en hanterad förmåga. Det sätter konsumtionspolicy som möjliggör snarare än blockerar, avgör när bidrag uppströms tjänar verksamheten, förvaltar de projekt ni släpper och tillämpar öppet samarbete inom företaget genom [InnerSource](https://en.wikipedia.org/wiki/Inner_source). Detta är en strategisk funktion, kopplad till era värderingar inom programvaruutveckling (kapitel 1.1), inte en efterlevnadskryssruta.

För företag är drivkraften skala: tusentals beroenden, export- och licensskyldigheter över jurisdiktioner och hundratals ingenjörer som var och en fattar små beslut om öppen källkod varje dag. Ett enda kontor ger den vildvuxna mängden en ryggrad. För myndigheter är drivkraften policy och allmänhetens förtroende. "Öppen källkod som standard" och "offentliga pengar, offentlig kod" är alltmer lag, så offentliga organ behöver någon som kan publicera kod säkert, återanvända mellan myndigheter och hålla leverantörer till öppna standarder. I båda miljöerna betalar sig OSPO genom att omvandla osynlig, oprissatt risk till medvetet, budgeterat arbete.

## Nyckelprinciper

- **Öppen källkod är en tvåvägsrelation, inte ett gratis lager.** Ni konsumerar, ni bidrar och ni släpper, och ett OSPO äger alla tre.
- **Bidrag är strategi, inte välgörenhet.** Att skicka uppströms minskar kostnaden för att bära privata patchar och köper inflytande.
- **Möjliggör den snabba vägen, vakta inte grinden.** En policy som är långsammare än att kopiera kod kommer att ignoreras, så gör den efterlevande vägen till den snabbaste.
- **Finansiera underhållarna ni beror på.** Allmänningen är inte självförsörjande, och ert mest kritiska bibliotek kan ha en enda obetald upphovsperson.
- **Förvalta det ni släpper, eller släpp det inte.** Ett övergivet projekt skadar ert anseende mer än inget projekt någonsin skulle göra.
- **Mät engagemang så att ni kan förbättra det.** Räkna bidrag, beroendehälsa och tid till godkännande, inte pressmeddelanden.
- **I myndigheter, öppet som standard och publicera som standard.** Öppenhet är normen, slutenhet det dokumenterade undantaget.

## Rekommendationer

### Bygg upp ett OSPO i storlek med er verklighet

Ni behöver inte ett stort team för att börja. I ett startup kan ett OSPO vara en ingenjör med ett skriftligt mandat och några timmar i veckan. I ett företag är det en liten central grupp plus ett federerat nätverk av förkämpar inbäddade i produktteam. Oavsett storlek, ge det en tydlig stadga som täcker fyra ansvarsområden: konsumtionspolicy och efterlevnad, bidrag uppströms, att släppa och förvalta egna projekt samt gemenskaps- och finansieringsrelationer. Placera det där det kan se både teknik och juridik, ofta rapporterande till CTO eller en teknikchef med en streckad linje till juridik och säkerhet. Felläget är ett OSPO som bor helt inom juridik och blir en broms. Botemedlet är att bemanna det med ingenjörer som levererar, så att dess vägledning bär trovärdighet hos de team det tjänar.

### Konsumera ansvarsfullt och gör den säkra vägen till den enkla vägen

Konsumtion är där det mesta av risken kommer in, så gör gott beteende mödolöst. Tillhandahåll en kurerad intern katalog över förgranskade komponenter, automatiserad licens- och sårbarhetsskanning i pipelinen och tydliga standardval en utvecklare kan följa utan att skapa ett ärende. Luta er mot licensdisciplinen i kapitel 10.3 och praxisen för leveranskedja och beroendehälsa i kapitel 2.18: fäst versioner, generera en materialförteckning för programvara (SBOM), bevaka [programvaruleveranskedjan](https://en.wikipedia.org/wiki/Software_supply_chain) efter komprometterade eller övergivna paket och följ end-of-life innan det tvingar fram en migrering. OSPO:ts uppgift är inte att godkänna varje beroende för hand. Den är att bygga skyddsräckena så att nittiofem procent av valen är säkra automatiskt och bara de genuint ovanliga fallen når en människa.

### Bidra uppströms för att det lönar sig, inte för att det är snällt

Behandla bidrag uppströms som ett ekonomiskt beslut. Varje privat patch ni bär mot ett beroende är en skatt ni betalar vid varje uppgradering, för alltid, tills ändringen landar uppströms eller förgreningen divergerar så långt att ni äger den fullt ut. Att bidra med rättelsen tillbaka tar bort den skatten. Att skicka uppströms köper också inflytande över riktningen, så att färdplanen för en komponent ni förlitar er på böjer sig mot era behov, och det signalerar kompetens till de ingenjörer ni vill anställa. Ge era utvecklare en snabb, dokumenterad väg: ett förhandsgodkänt bidragsgivaravtal eller Developer Certificate of Origin, ett lättviktigt godkännande som bekräftar att ändringen är säker att dela och ledningstid budgeterad för arbetet. När alternativet är att underhålla en permanent [förgrening](https://en.wikipedia.org/wiki/Fork_(software_development)) av ett projekt ni inte kontrollerar är det nästan alltid billigare att bidra tillbaka.

### Släpp era egna projekt med verklig styrning

När ni släpper programvara ni byggt med öppen källkod, gör det medvetet eller inte alls. Avgör först om koden är en vara värd att dela eller en särskiljare värd att hålla sluten, med resonemanget i kapitel 10.12. Om ni släpper, välj en licens som matchar er avsikt (permissiv för att maximera adoption, copyleft för att hålla ekosystemet ömsesidigt), dokumentera vem som avgör vad genom en skriftlig styrningsmodell och registrera [varumärket](https://en.wikipedia.org/wiki/Trademark) på projektnamnet så att ni kan skydda det mot missbruk medan koden förblir fri. Förbind er till verklig förvaltning: en offentlig ärendehanterare, en bidragsguide, en uppförandekod och en säkerhetspolicy med koordinerat utlämnande så att rapportörer vet hur de når er (kapitel 4.2). Namnge en underhållare och budgetera hens tid. Ett projekt ni lanserar med pompa och överger om ett år gör mer skada för ert anseende än ett ni aldrig levererade.

### Tillämpa InnerSource för att samarbeta inom företaget

Vanorna som får öppen källkod att fungera (offentliga förvar, tydliga bidragsguider, granskning på meriter, låga trösklar för en första patch) fungerar lika bra bakom brandväggen. InnerSource betyder att varje ingenjör kan hitta, använda och förbättra vilket internt projekt som helst och skicka en pull request över teamgränser i stället för att skapa ett ärende och vänta. Det bryter ned silor, sprider koddelning och tränar era människor i exakt det arbetsflöde de kommer att använda när de bidrar externt. OSPO är det naturliga hemmet för InnerSource eftersom det redan äger verktygen och den kulturella spelboken. Börja med några högvärdiga delade bibliotek, publicera deras bidragsguider internt och belöna team som tar emot yttre patchar med god min.

### Finansiera och vidmakthåll underhållarna ni beror på

Ert produktionssystem kan vila på ett bibliotek som underhålls av en person på sin fritid. Det är en leveranskedjerisk, och det ärliga svaret är att hjälpa till att bära lasten. Identifiera era mest kritiska beroenden från materialförteckningen, hitta de med en tunn underhållarbas och välj en respons för var och en: sponsra underhållaren direkt, bidra med ingenjörstid, gå med i en stiftelse som finansierar projektet eller, som sista utväg, förbered er på att förgrena eller ersätta. Att finansiera allmänningen är billigare än nödläget som följer på dess kollaps, och det håller komponenterna ni förlitar er på friska och rörliga i en riktning ni kan påverka.

### Sätt bidragspolicy som godkänner snabbt

En bidragspolicy finns för att säga ja snabbt, inte för att säga nej långsamt. Specificera vad en ingenjör får bidra med utan att fråga (buggrättelser, dokumentation, små funktioner till projekt ni redan använder), vad som behöver en lätt kontroll (allt som rör en särskiljare eller ett patent) och hur immateriell egendom och bidragsgivaravtal hanteras en gång, centralt, snarare än per bidrag. Automatisera de tråkiga delarna: licenskontroller, ett förhandssignerat företagsbidragsavtal och en bot som flaggar den sällsynta inlämning som behöver mänskliga ögon. Mät tid till godkännande och behandla en långsam kö som en bugg i policyn.

## Avvägningar: för- och nackdelar

| Tillvägagångssätt | Fördelar | Nackdelar |
| --- | --- | --- |
| Centralt OSPO | Konsekvent policy, djup expertis, tydligt ägarskap | Kan bli en flaskhals om det bara vaktar och aldrig möjliggör |
| Federerat OSPO (förkämpar i team) | Skalar, håller beslut nära ingenjörerna | Behöver stark samordning, annars driver policyn isär |
| Bidra uppströms | Tar bort skatten på privata patchar, köper inflytande, hjälper rekrytering | Löpande insats, IP-granskning, arbete på någon annans schema |
| Bära privata förgreningar | Full kontroll, leverans på egen tidslinje | Permanent underhållsskatt, driver från säkerhetsrättelser uppströms |
| Släpp ett eget projekt | Ekosystem, anseende, delat underhåll | Verklig förvaltningskostnad. Övergivande skadar anseendet |
| Finansiera underhållare | Skyddar kritiska beroenden, köper välvilja | Direkt kostnad, och att välja vem som finansieras är politiskt |
| Inget OSPO (ad hoc) | Noll uppsättningskostnad | Osynlig juridisk, säkerhets- och hållbarhetsskuld |

Den centrala spänningen är mellan kontroll och möjliggörande. Ett OSPO som granskar varje beroende och varje bidrag för hand känns tryggt, men det blir det ingenjörer går runt, vilket producerar de osynliga skuggberoenden ni försökte förhindra. Ett OSPO som bara publicerar glättig vägledning utan automatiserad tillämpning ignoreras i samma stund en deadline hotar. Lösningen är densamma som löper genom kapitel 10.3: automatisera det vanliga fallet så att den efterlevande vägen är den snabbaste, och reservera mänskligt omdöme för det genuint nya. Få balansen rätt och kontoret är en kraftmultiplikator. Få den fel åt endera hållet och det är antingen en broms eller en dekoration.

## Frågor att diskutera med ditt team

1. **Vem äger er relation till öppen källkod i dag, och skulle hen kunna besvara en svår fråga i morgon?** Om en tänkbar köpares jurister bad om er licensinventering, eller en reporter frågade vilket underhållslöst bibliotek som sitter i er betalningsväg, finns det ett namn knutet till svaret? För de flesta organisationer är det ärliga svaret "ingen", vilket betyder att varje ingenjör i tysthet gör policy och ingen är ansvarig för summan. Ta med belägg till mötet: försök ta fram listan över godkända licenser, materialförteckningen och personen som skulle ta en copyleft-fråga under due diligence. Om de artefakterna inte finns eller pekar på ingen har ni hittat er första OSPO-uppgift. Beslutet att fatta är inte om ni ska ha funktionen utan vem som äger den och vilket mandat hen bär, även om kontoret är en person en dag i veckan.

2. **Bär ni privata patchar ni kunde skicka uppströms, och vad kostar det er?** Många team underhåller en tyst hög av lokala ändringar mot sina beroenden, tillämpar dem för hand på nytt vid varje uppgradering och absorberar sammanslagningssmärtan som vore den en naturlag. Varje sådan patch är en återkommande skatt, och var och en är en kandidat att bidra tillbaka så att skatten försvinner. Ta med detaljerna: lista förgreningarna och de lokala patchar ert bygge faktiskt bär, uppskatta ingenjörstimmarna var och en kostar per år och notera vilka uppströmsprojekt som sannolikt skulle acceptera ändringen. Den konkurrerande hänsynen är verklig, eftersom att skicka uppströms tar insats nu och går på underhållarens schema, men jämförelsen är mot att betala patchskatten för alltid. Svaret bör förvandla "vi tillämpar den bara på nytt" till ett medvetet val, med en bidragsväg tillräckligt snabb för att ingenjörer använder den.

3. **Vilket beroende skulle skada mest om dess underhållare gick sin väg, och vad gör ni åt det?** Någonstans i er stack finns en komponent som skulle stoppa en intäkts- eller uppdragskritisk tjänst om den gick sönder, underhållen av en person eller en handfull människor ni aldrig har finansierat eller tackat. Allmänningen känns gratis ända till ögonblicket den inte är det, och den dyra versionen av den läxan är en villervalla efter övergivande eller en olappad sårbarhet. Ta med er materialförteckning och rangordna beroenden efter sprängradie, notera sedan underhållarantal och finansieringsstatus för de översta. För varje kritiskt, tunt bemannat beroende, avgör i förväg om ni ska sponsra, bidra med tid, gå med i en stiftelse eller förbereda ersättning. Det omvandlar en latent enskild felpunkt till en hanterad relation, hållen till samma standard som vilken annan driftrisk som helst (kapitel 2.18).

4. **Innan ni släpper nästa interna verktyg med öppen källkod, är ni redo att förvalta det i år, eller levererar ni en lansering och en eventuell ursäkt?** En offentlig release är ett stående åtagande: en ärendehanterare någon måste triagera, en säkerhetsinkorg någon måste bevaka och ett namn någon måste försvara. Team griper efter öppen källkod för att hjälpa rekrytering eller välvilja och upptäcker sedan att ett övergivet projekt med gamla ärenden skadar anseendet de hoppades bygga, mer än att leverera ingenting hade gjort. Ta med belägg: lista projekten ni redan släppt och visa för varje ärendenas ålder, om en namngiven underhållare har budgeterade timmar, om det har en styrningsmodell, ett registrerat varumärke och en policy för koordinerat utlämnande, och om koden är en vara värd att dela eller en särskiljare ni bör hålla sluten (kapitel 10.12). Den konkurrerande hänsynen är att verklig förvaltning kostar ingenjörstid ni kunde lägga på produkten, så det ärliga valet är ofta att släppa färre saker och förvalta dem ordentligt. För ett företag betyder det juridisk granskning och varumärkesgranskning före lansering. För en myndighet betyder det att varumärket, utlämnandekanalen och undantagsprocessen för publicera-som-standard är avklarade innan förvaret blir offentligt.

5. **Hur lång tid tar det egentligen för en ingenjör att få ett beroende godkänt eller ett bidrag klarerat, och är det långsammare än att gå runt er?** En policy för öppen källkod konkurrerar direkt med den snabbaste genväg en ingenjör kan hitta, och varje process långsammare än att kopiera koden förbigås och producerar de osynliga skuggberoenden kontoret var tänkt att förhindra. Spänningen är kontroll mot möjliggörande: varje manuell granskning lägger till ett revisionsspår och fångar det sällsynta genuina problemet, men den lägger också till latens som skjuter medianfallet av den efterlevande vägen. Ta med siffrorna till mötet: den uppmätta tiden till godkännande för ett standardberoende och ett standardbidrag, andelen beslut som hanteras automatiskt mot av en människa och antalet undantag som verkligen behövde omdöme förra kvartalet. I ett företag med hundratals ingenjörer som var och en fattar små beslut dagligen blir en tvådagarskö i tysthet tusentals förbigångna granskningar. I en myndighet krockar samma latens med upphandlings- och revisionsskyldigheter som kräver det pappersspår genvägen hoppar över, så åtgärden är att automatisera det vanliga fallet snarare än att bemanna en större grind.

6. **Vilka interna projekt skulle ha mest nytta av InnerSource, och vad hindrar ett annat team från att skicka er en pull request i dag?** Praxisen som får öppen källkod att fungera (offentliga förvar, bidragsguider, granskning på meriter, en låg tröskel för en första patch) lönar sig bakom brandväggen genom att bryta ned silor, sprida återanvändning och träna människor i exakt det arbetsflöde de kommer att använda för att bidra externt. Den konkurrerande hänsynen är att öppna ett internt projekt kräver en bidragsguide, ledig granskningskapacitet och ett beslut om vilken kod som måste förbli begränsad av säkerhets- eller regulatoriska skäl. Ta med detaljerna: namnge de högvärdiga delade biblioteken, notera vilka som redan publicerar en intern bidragsguide och beskriv hur en pull request över teamgränser hanteras i dag, om den välkomnas eller försvinner i en kö. För ett företag mäts nyttan i undvikna dubbla interna byggen över många team. För en myndighet sträcker sig samma vana över myndighetsgränser som återanvändning mellan myndigheter, så att publicera-som-standard och delade komponenter minskar dubblerade offentliga utgifter snarare än multiplicerar dem.

## Sektorsperspektiv

**Startup.** Ge kontoret till en namngiven ingenjör några timmar i veckan med en enkelsidig stadga, inte en kommitté. Använd permissiva licenser som standard med en skanner i pipelinen, skicka uppströms bara de få privata patchar som faktiskt gör ont vid varje uppgradering och sätt upp en liten månatlig sponsring för det enmansunderhållna bibliotek ni genuint inte kan leva utan. Fart spelar större roll än täckning här: en efterlevande väg snabbare än att kopiera kod slår en grundlig policy ingen följer.

**Småföretag.** Ni kommer inte att bemanna ett dedikerat OSPO, så köp förmågan inbyggd i verktyg ni redan kör: en skanner som flaggar licens- och sårbarhetsproblem och en kurerad katalog över förgranskade komponenter. Ramma in arbetet som licensefterlevnad och beroendehygien snarare än ett program: veta vad som finns i er materialförteckning, veta vad varje licens förpliktar till och veta vilket enmansunderhållet beroende som skulle skada om det försvann. Föredra att köpa skanning och katalogisering framför att bygga egen.

**Storföretag.** Kör ett litet centralt kontor plus ett federerat nätverk av förkämpar inbäddade i produktteam, så att policyn förblir konsekvent medan besluten förblir nära ingenjörerna. Automatisera licens-, sårbarhets- och exportskanning, täck varje ingenjör med ett förhandsgodkänt bidragsgivaravtal och följ tid till godkännande som ett rapporterat mått. Finansiera stiftelserna bakom era kritiska beroenden, kör InnerSource över många förvar och hantera hela beståndet som en portfölj med hälso- och engagemangsmått snarare än en spridning av enskilda beslut.

**Offentlig sektor.** Verka under öppen källkod som standard och offentliga pengar, offentlig kod: publicera nya tjänster i ett offentligt förvar om inte ett dokumenterat säkerhets- eller integritetsundantag gäller. Kör en katalog över myndigheter så att team återanvänder före de bygger, skriv in krav på öppen källkod och öppna standarder i upphandlingen så att leverantörer levererar återanvändbar kod med rättigheterna bevarade och hantera koordinerat utlämnande för det ni publicerar. Finansiera underhåll av delade bibliotek flera myndigheter beror på, så att inget enskilt team i tysthet äger infrastruktur hela staten förlitar sig på.

## Exempel

**Startup.** Ett startup på tjugo personer gör sin ledande plattformsingenjör till OSPO-ägare på deltid med en enkelsidig stadga. Hon sätter en enkel konsumtionspolicy (permissiva licenser förgodkända, copyleft granskas, skanner i pipelinen) och märker att teamet bär tre privata patchar mot ett könbibliotek med öppen källkod, smärtsamt tillämpade på nytt vid varje uppgradering. Hon skickar alla tre uppströms. Två accepteras inom en månad och tar för gott bort uppgraderingsskatten. Hon släpper ett litet internt verktyg med öppen källkod med en riktig README, en licens och en säkerhetskontakt, mest för att locka ingenjörer, och hon sätter upp en månatlig sponsring för den enmansunderhållna parser produkten beror på. Inget av detta kräver nyanställning, bara en namngiven ägare och ett tydligt mandat.

**Storföretag.** En global bank driver ett centralt OSPO på sex personer plus ett federerat nätverk av förkämpar för öppen källkod inbäddade i varje produktgrupp. Det centrala teamet äger policyn, den automatiserade licens- och exportefterlevnadsskanningen och bidragsgivaravtalet som varje ingenjör täcks av från dag ett. Förkämparna hanterar lokal granskning och coachar sina team i bidrag. Banken finansierar flera stiftelser vars projekt ligger under dess handelssystem, bidrar med rättelser uppströms till ett vitt använt dataramverk så att den slutar underhålla en förgrening och kör InnerSource över två hundra interna förvar så att vilket team som helst kan skicka en pull request till vilket annat som helst. Tid till godkännande för ett standardbidrag är under två dagar, följt som ett mått OSPO rapporterar kvartalsvis.

**Offentlig sektor.** En nationell digitaliseringsmyndighet verkar under ett mandat om "öppen källkod som standard" och offentliga pengar, offentlig kod. Dess OSPO publicerar nya tjänster i ett offentligt förvar om inte ett dokumenterat undantag gäller för säkerhet eller integritet, kör en katalog över hela staten så att myndigheter återanvänder kod innan de bygger den och skriver in krav på öppen källkod och öppna standarder i upphandlingen så att leverantörer levererar återanvändbar, väldokumenterad kod med staten kvar som rättighetshavare. Kontoret hanterar också koordinerat säkerhetsutlämnande för koden det publicerar och finansierar underhåll av ett delat identitetsbibliotek flera myndigheter nu beror på, så att inget enskilt team i tysthet äger en komponent hela staten förlitar sig på.

## Affärsnytta: motiv, ROI och TCO

Den tydligaste avkastningen är eliminering av undvikbara, dyra överraskningar. Ohanterad öppen källkod producerar kriser som anländer på eget schema: ett copyleft-brott som dyker upp under due diligence vid ett förvärv, en nödmigrering från en död komponent, ett intrång spårat till ett beroende ingen inventering listade. Ett OSPO omvandlar dessa händelser med låg sannolikhet och hög kostnad till jämnt, budgeterat arbete. Lägg därtill de återkommande besparingarna från att skicka uppströms: varje privat patch ni avvecklar slutar beskatta varje framtida uppgradering, och över ett stort bestånd ackumuleras det till verklig ingenjörskapacitet som återgår till produktarbete.

På huvudboken för [total ägandekostnad](https://en.wikipedia.org/wiki/Total_cost_of_ownership) är kontoret billigt i förhållande till vad det skyddar. Dess kostnad är ett litet team, lite skannings- och katalogverktyg och blygsam finansiering av underhållare. Ställ det mot kostnaden för att inte ha det: juridiskt ansvar, misslyckad eller försenad due diligence, säkerhetsincidenter, dubbla interna byggen av saker som redan finns som öppen källkod och den långsamma blödningen från förgreningar ingen valde att behålla. Det finns också uppsidor som är svårare att prissätta men verkliga: inflytande över riktningen för komponenter ni beror på, en rekryterings- och anseendefördel av en trovärdig närvaro inom öppen källkod och snabbare leverans eftersom ingenjörer återanvänder i stället för att bygga om. När ni driver ärendet inför ledningen, ramma in OSPO som leveranskedjehantering för majoriteten av er kodbas, med en strategisk utdelning ovanpå. I myndigheter, lägg till efterlevnadsdimensionen, eftersom öppenhet ofta är mandaterad och att göra det väl undviker både bristande efterlevnad och dubblerade offentliga utgifter.

## Antimönster och fallgropar

- **OSPO som grind.** Ett kontor som bara granskar och blockerar, aldrig möjliggör, blir förbigånget och producerar de skuggberoenden det var tänkt att förhindra.
- **Bidragsteater.** Att tillkännage en strategi för öppen källkod medan godkännandeprocessen görs så långsam att ingen faktiskt bidrar.
- **Den övergivna releasen.** Att publicera ett projekt med ett lanseringsblogginlägg och sedan aldrig triagera ett ärende, vilket skadar ert anseende mer än tystnad hade gjort.
- **Förgrena och glömma.** Att förgrena ett beroende för en rättelse och sedan bära det för alltid, driftande bort från säkerhetspatchar uppströms.
- **Snålskjuts på sköra underhållare.** Att bero på ett kritiskt enmansunderhållet bibliotek och aldrig finansiera, tacka eller hjälpa personen bakom.
- **Varumärkesförsummelse.** Att släppa ett projekt utan att skydda dess namn och sedan se en förgrening eller leverantör handla på ert anseende.
- **Enbart juridiskt ägarskap.** Att placera OSPO helt inom juridik så att dess vägledning saknar ingenjörstrovärdighet och team stänger av.
- **Fåfängemått.** Att räkna stjärnor och pressomnämnanden i stället för beroendehälsa, tid till godkännande och avvecklade privata patchar.

## Mognadsmodell

- **Nivå 1, Initiera:** Ingenjörer lägger till, patchar och släpper ibland öppen källkod utan policy och utan ägare. Konsumtion, bidrag och release är reaktiva och ad hoc, drivna av individuellt initiativ. Privata förgreningar ackumuleras obemärkt, ingen finansierar något uppströmsprojekt och ingen kunde besvara en licensfråga under due diligence.
- **Nivå 2, Utveckla:** Grundläggande praxis dyker upp men varierar mellan team. En grov konsumtionspolicy och en lista över godkända licenser finns, och någon är löst ansvarig, men bidrag är långsamma och fall för fall och vissa grupper gör långt mer än andra. Några kritiska beroenden är kända, men hållbarhet, releaser och förvaltning förblir inkonsekventa.
- **Nivå 3, Standardisera:** Ett stadgat OSPO äger konsumtion, bidrag, release och gemenskap, och praxisen är dokumenterad och upprätthållen i hela organisationen. Skanning och en materialförteckning är automatiserade, ett förhandsgodkänt bidragsgivaravtal och en snabb godkännandeväg finns, släppta projekt bär verklig styrning, varumärken och säkerhetspolicyer och InnerSource sprider sig. Myndighetsteam publicerar som standard.
- **Nivå 4, Hantera:** Funktionen för öppen källkod mäts och styrs mot utgångslägen. Tid till godkännande följs mot ett mål, bidragsvolym och uppströms acceptansgrad rapporteras, paneler för beroendehälsa och underhållarantal flaggar enskilda felpunkter, finansierad underhållartäckning av de högst riskutsatta beroendena övervakas och inventariet av privata patchar och förgreningar trendar nedåt kvartal för kvartal. Släppta projekt har uppmätta svarstider på ärenden, undantag granskas med en takt och fåfängemått som stjärnor överges till förmån för dessa.
- **Nivå 5, Orkestrera:** Öppen källkod är en hanterad strategisk förmåga, integrerad med teknik-, juridik-, säkerhets- och upphandlingsplanering och anpassad kontinuerligt. Bidrag är rutin, kritiska underhållare och stiftelser finansieras, organisationen förvaltar välskötta projekt och styr de ekosystem den beror på och InnerSource är normen. Engagemangs- och hälsomått matar kontinuerlig förbättring, och portföljen balanseras om när beroenden, risker och mandat skiftar.

## Idéer för diskussion

1. Var går gränsen mellan ett OSPO som möjliggör och ett som vaktar, och hur skulle ni utifrån veta vilket ni har byggt?
2. Vilka av era privata patchar eller förgreningar bär ni av vana snarare än nödvändighet, och vad skulle krävas för att skicka de tre främsta uppströms?
3. Hur bör ni avgöra vilka underhållare och stiftelser som ska finansieras när listan över kritiska beroenden är längre än budgeten?
4. Vad skulle genuint ändras i er nästa release om ni måste publicera den med verklig styrning, ett varumärke och en policy för koordinerat utlämnande från dag ett?
5. För läsare i offentlig sektor, vad är en försvarbar process för att undanta kod från publicera-som-standard utan att i tysthet urholka principen?
6. Vilka interna bibliotek skulle ha mest nytta av InnerSource, och vad hindrar ett annat team från att skicka er en pull request i dag?

## Viktigaste punkter

- Ett OSPO äger hela relationen till öppen källkod: att konsumera ansvarsfullt, bidra uppströms, släppa egna projekt och vidmakthålla de underhållare ni beror på.
- Att bidra uppströms är strategi, inte välgörenhet. Det tar bort den återkommande skatten på privata patchar, köper inflytande över riktningen och hjälper er rekrytera.
- Gör den efterlevande vägen till den snabbaste genom automatisering och kurering, så att kontoret möjliggör för ingenjörer i stället för att vakta dem.
- Släpp era egna projekt bara med verklig styrning, en vald licens, ett skyddat varumärke och koordinerat säkerhetsutlämnande, eller släpp dem inte alls.
- Finansiera och hjälp de kritiska underhållare ert produktionssystem vilar på, eftersom allmänningen inte är självförsörjande.
- Tillämpa InnerSource för att föra samarbetet från öppen källkod in i företaget, och i myndigheter, var öppna som standard, publicera som standard och återanvänd innan ni bygger.

## Referenser och vidare läsning

- Nadia Eghbal, *Working in Public: The Making and Maintenance of Open Source Software*
- Nadia Eghbal, *Roads and Bridges: The Unseen Labour Behind Our Digital Infrastructure*
- Karl Fogel, *Producing Open Source Software: How to Run a Successful Free Software Project*
- Danese Cooper and Klaas-Jan Stol (editors), *Adopting InnerSource: Principles and Case Studies*
- The Linux Foundation and TODO Group, *OSPO guides and Open Source Program Office resources*
- The Linux Foundation and TODO Group, *State of OSPOs and Open Source Management* (annual survey series)
- Heather Meeker, *Open (Source) for Business*
- Open Source Initiative, *The Open Source Definition* and approved-licence list
- Free Software Foundation Europe, *Public Money, Public Code* campaign materials
- U.S. Federal Source Code Policy and Code.gov guidance
