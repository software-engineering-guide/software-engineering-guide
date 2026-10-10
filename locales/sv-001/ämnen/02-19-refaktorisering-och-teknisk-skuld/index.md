# 2.19 Refaktorisering och teknisk skuld

## Översikt och motivation

[Refaktorisering](https://en.wikipedia.org/wiki/Code_refactoring) är att ändra kodens inre struktur utan att ändra vad den gör utifrån. Du byter namn på en variabel, delar en lång funktion, extraherar en klass, slår ihop en härva av villkor till något en läsare kan följa, och programmet beter sig precis som förut. Den sista delen är hela disciplinen. Refaktorisering är beteendebevarande per definition, och i samma stund du också ändrar beteende refaktoriserar du inte längre, du gör två riskfyllda saker på en gång och döljer var och en bakom den andra. Det här kapitlet behandlar dessa som skilda handlingar med avsikt, eftersom förväxlingen mellan dem är där det mesta av refaktoriseringen går fel.

I ett stort team spelar detta större roll än för en ensam utvecklare, eftersom koden du städar är kod hundratals andra läser, är beroende av och är rädda att röra. Refaktorisering är hur en gemensam kodbas förblir beboelig över år och personalomsättning. Den hänger direkt ihop med programvarukonstruktion (kapitel 2.9), där den dagliga kodkvaliteten sätts, och med teststrategi (kapitel 2.4), som är det skyddsnät som över huvud taget gör refaktorisering säker. Den hänger också ihop med den svårare frågan om [teknisk skuld](https://en.wikipedia.org/wiki/Technical_debt): den ackumulerade kostnaden för genvägar, åldrande designer och uppskjuten städning som gör varje framtida ändring långsammare. Refaktorisering är det främsta sättet du betalar av den skulden, så de två ämnena hör hemma i ett kapitel.

I företags- och myndighetsmiljöer stiger insatserna. Dessa system är långlivade, ofta decennier gamla, och står ofta under revisions- och ändringskontrollregimer som behandlar varje kodändring som en styrd händelse. Du kan inte bara skriva om ett medborgarsystem för bidrag under en lång helg. Du moderniserar det i små, reversibla, belägg-baserade steg, vilket är exakt vad disciplinerad refaktorisering ger dig. Att samordna det arbetet över många team och långlivade system (kapitel 10.4) är en av storskalig utvecklings avgörande utmaningar, och att få det fel är hur organisationer hamnar frusna, oförmögna att ändra programvara de inte längre förstår.

## Nyckelprinciper

- Refaktorisering bevarar beteende. Om du ändrar vad koden gör är det en separat ändring, som görs separat.
- En pålitlig testsvit är förutsättningen för säker refaktorisering, inte ett valfritt extra.
- Arbeta i små, namngivna, reversibla steg och håll koden fungerande efter varje.
- Gör teknisk skuld synlig och spårad, och finansiera sedan avbetalning som stadig kapacitet snarare än hjältedåd.
- Refaktorisera den kod du redan ändrar, där städningen förtjänar sin plats.
- Inte all skuld är värd att betala. Stabil, sällan rörd eller snart avvecklad kod kan lämnas ifred.
- Mät intern kvalitet för att informera omdöme, aldrig som ett mål att manipulera.

## Rekommendationer

### Håll refaktorisering och beteendeändring strikt åtskilda

Besluta innan du börjar vilken av dem du gör, och sudda aldrig ut de två i en enda commit. När du refaktoriserar måste de tester som passerade före passera efter, oförändrade, eftersom det observerbara beteendet inte har rört sig. När du ändrar beteende, gör det som en egen commit med egna tester. Skälet är praktiskt: om en blandad ändring bryter något kan du inte avgöra om din omstrukturering introducerade buggen eller din beteendeändring gjorde det, och i kodgranskning (kapitel 2.5) kan en granskare inte resonera om endera hälften rent. Vanan som fungerar är tvåhattsregeln från Martin Fowler: du bär alltid antingen refaktoriseringshatten eller funktionshatten, du vet vilken och du byter medvetet. Separata commits gör också [versionshanteringens](https://en.wikipedia.org/wiki/Version_control) historik läsbar, så att en ingenjör som bisekterar ett fel kan hoppa över de rena refaktoriseringscommitsen med tillförsikt.

### Upprätta ett pålitligt skyddsnät innan du omstrukturerar

Refaktorisering utan tester är bara redigering och hopp. Innan du omstrukturerar något av betydelse behöver du en svit du litar på för att fånga en beteendeändring om du orsakar en, vilket är kärnargumentet i teststrategi (kapitel 2.4). För kod som redan har bra täckning, kör testerna, refaktorisera i små steg och kör dem igen efter varje steg. För äldre kod utan tester är det ärliga greppet att skriva [karakteriseringstester](https://en.wikipedia.org/wiki/Characterization_test) först. Ett karakteriseringstest hävdar inte vad koden bör göra. Det fångar vad koden faktiskt gör just nu, inklusive dess egenheter, så att varje ändring i beteende syns som ett fallerande test. Michael Feathers populariserade detta tillvägagångssätt för just den situation stora organisationer lever i: kod som fungerar, spelar roll och saknar tester. När det nuvarande beteendet är fastnaglat kan du refaktorisera under det säkert, och först då ändra beteende ovanpå.

### Lär dig känna igen kodlukter och tillämpa små namngivna refaktoriseringar

En [kodlukt](https://en.wikipedia.org/wiki/Code_smell) är ett ytligt tecken på att något under ytan kan behöva uppmärksamhet: en funktion som vuxit för lång, en klass som vet för mycket, duplicerad logik, en lång parameterlista, namn som ljuger om vad de gör. En lukt är en antydan, inte en dom, så du undersöker snarare än lyder den blint. Svaret är en liten, namngiven refaktorisering ur Fowlers katalog: Extrahera funktion, Byt namn på variabel, Flytta metod, Ersätt villkor med polymorfism och dussintals fler. Värdet av att använda namngivna drag är att vart och ett är litet, förstått, mekaniskt säkert och ofta direkt stött av din IDE. Du komponerar stora förbättringar av många små pålitliga steg och håller koden grön hela vägen, i stället för att göra ett stort språng du inte kan verifiera.

### Föredra opportunistisk refaktorisering och reservera kampanjer för verkligt strukturellt behov

Det mesta av refaktoriseringen bör vara opportunistisk, invävd i det arbete du redan gör. Scoutregeln fångar det: lämna koden lite renare än du fann den. När du rör en fil för att lägga till en funktion eller åtgärda en bugg förstår du redan det hörnet, och små städningar där växer över tid utan att behöva någons tillstånd eller en separat budget. Planerade refaktoriseringskampanjer, där ett team stoppar funktionsarbete för att omstrukturera ett stort område, är ibland nödvändiga, men de är dyra, svåra att schemalägga mot produkttryck och riskfyllda om området är dåligt testat. Reservera kampanjer för strukturella problem opportunistisk städning inte kan nå, och driv ärendet med belägg om den ändringskostnad du betalar. Föredra det stadiga droppet av små städningar. Det är mer varaktigt än den enstaka heroiska omskrivningen.

### Använd kvävarfikonmönstret för stora strukturella förändringar

När ett helt delsystem behöver ersättas, försök inte med en storskalig omskrivning som pågår i ett år och slås ihop i slutet. Det är hur moderniseringsprojekt dör. Använd [kvävarfikonmönstret](https://en.wikipedia.org/wiki/Strangler_fig_pattern), uppkallat av Martin Fowler efter vinrankan som växer runt ett träd och gradvis ersätter det. Du sätter en fasad framför det gamla systemet, leder en bit funktionalitet i taget till ny kod bakom den fasaden, verifierar den i produktion och upprepar tills det gamla systemet är helt omslutet och kan tas bort. Varje bit är liten, levererbar och reversibel, så risken förblir avgränsad och värde anländer kontinuerligt. En nära kusin, gren-via-abstraktion, gör detsamma inom en enda kodbas: du inför ett abstraktionslager över det du vill ersätta, bygger den nya implementationen bakom det medan båda samexisterar, byter konsumenter gradvis och raderar den gamla implementationen när inget längre beror på den. Båda låter ett [äldre system](https://en.wikipedia.org/wiki/Legacy_system) utvecklas medan det förblir vid liv, vilket är det enda slag av modernisering de flesta stora organisationer faktiskt har råd med.

### Behandla teknisk skuld som en portfölj och gör den synlig

Skuldmetaforn, myntad av Ward Cunningham, skiljer två saker åt: kapitalet (den röriga koden eller genvägen själv) och räntan (den extra insats varje framtida ändring betalar på grund av den). Inte all skuld är lika. Fowlers kvadrant sorterar den längs två axlar: medveten mot oavsiktlig och förståndig mot hänsynslös. Förståndig-medveten skuld ("vi levererar nu och städar nästa sprint, och vi känner kostnaden") är ett legitimt affärsbeslut. Hänsynslös-oavsiktlig skuld ("vad är ett designmönster?") är bara skada. Förvaltningsuppgiften, som hänger ihop med beslutsfattande och styrning (kapitel 1.5) och dess behandling av skuld som en portfölj, är att göra skulden synlig så att den kan resoneras om: följ betydande poster där arbetet bor, tagga koden och registrera den ränta du betalar så att avbetalning konkurrerar om kapacitet på belägg snarare än på vem som klagar högst. Skuld du inte kan se kan du inte hantera.

### Finansiera avbetalning som stadig kapacitet, inte hjältedåd

Felmönstret är att behandla städning som något du ska göra "när det lugnat sig", vilket aldrig händer. Det varaktiga mönstret är en fast, skyddad kapacitet för avbetalning: en uttrycklig del av varje cykel, eller en stående överenskommelse att städning följer med funktionsarbete i samma område. Det som inte fungerar är den periodiska heroiska sprinten där någon bränner en helg för att åtgärda allt, eftersom den är ohållbar, ogranskad och vanligen gör sig själv ogjord. Stadig kapacitet håller ränteutbetalningarna nere och undviker högkonjunktur-lågkonjunktur-cykeln där skuld ackumuleras tills en kris tvingar fram en dyr omskrivning. Det är ett ledningsåtagande lika mycket som en teknisk praxis, och det hör hemma i hur du planerar programvaruunderhåll (kapitel 3.7) över ett systems liv.

### Mät intern kvalitet, men låt inte måttet bli målet

Du kan mäta intern kvalitet med signaler som [cyklomatisk komplexitet](https://en.wikipedia.org/wiki/Cyclomatic_complexity) (ett antal oberoende vägar genom en funktion), duplicering, testtäckning, andel misslyckade ändringar och hur lång tid ändringar tar i de områden du misstänker. Dessa tal är användbara för att upptäcka var skuld koncentreras och för att bevaka en trend över tid. Faran är Goodharts lag: när ett mått blir ett mål slutar det mäta något verkligt. Föreskriv ett täckningstal och du får tester som inte hävdar något. Belöna låga komplexitetspoäng och du får logik utsmetad över fler funktioner för att undvika måttet. Använd mått för att starta samtal och lokalisera heta punkter, och koppla aldrig ett kvalitetsmått till en grind som människor är motiverade att manipulera.

### Vet när du inte ska refaktorisera

Refaktorisering är en investering, och viss kod kommer aldrig att betala tillbaka den. Om en modul är stabil, sällan rörd och förstådd tillräckligt väl för att ändras de sällsynta gånger du måste, är att städa den insats lagd på ränta du inte betalade. Om koden är avsedd att avvecklas är att refaktorisera den att polera något du håller på att kasta. Disciplinen är att lägga din städbudget där förändring är frekvent och smärtsam, vilket är där en minskning av räntan faktiskt växer, och att lämna de tysta hörnen ifred.

## Avvägningar: för- och nackdelar

| Tillvägagångssätt | Fördelar | Nackdelar |
| --- | --- | --- |
| Opportunistisk refaktorisering (scoutregeln) | Billig, kontinuerlig, ingen separat budget, växer över tid | Ojämn täckning. Heta filer förbättras medan kalla ruttnar |
| Planerad refaktoriseringskampanj | Åtgärdar strukturella problem städning inte når | Dyr. Konkurrerar med funktioner. Riskabel utan bra tester |
| Kvävarfikon / gren-via-abstraktion | Inkrementell, reversibel, håller systemet levande, begränsar risk | Långsammare än en omskrivning på pappret. Kräver disciplin att slutföra |
| Storskalig omskrivning | Ren tavla. Inga äldre begränsningar | Hög felfrekvens. Lång tid till värde. Beteendeluckor |
| Medveten förståndig skuld | Levererar värde nu. Uttrycklig, planerad avbetalning | Blir hänsynslös om avbetalningen aldrig schemaläggs |
| Måttgrindad kvalitet | Objektiv, synlig, fångar drift tidigt | Inbjuder till manipulation. Straffar nyans. Kan försämra verklig kvalitet |

Den centrala spänningen är hastighet nu mot förändringsbarhet senare, och den är verklig. Att leverera en genväg kan vara rätt val när deadlinen är genuin och skulden är förståndig och spårad. Misstaget är att låtsas att skulden är gratis, eller att låta den ackumuleras osynligt tills systemet är för dyrt att ändra. Lös det genom att göra avvägningen uttrycklig varje gång: namnge skulden, uppskatta räntan, besluta medvetet och dokumentera beslutet så att avbetalning kan schemaläggas snarare än glömmas. Ett team som lånar medvetet och betalar jämnt förblir snabbt i åratal. Ett team som lånar blint tvärstannar.

## Frågor att diskutera med ditt team

1. **Hur hindrar vi refaktorisering och beteendeändring från att blöda in i samma commit, och upprätthåller vår granskning det faktiskt?** Det här är kapitlets grunddisciplin, och den som oftast bryts under deadlinetryck, eftersom det känns effektivt att "städa upp det här medan jag ändå är här" och leverera allt tillsammans. Kostnaden landar senare: när en blandad commit bryter produktion kan ingen avgöra om omstruktureringen eller funktionen orsakade det, och en bisektion genom er historik slutar vara pålitlig. Ta med en handfull nyliga pull requests och kontrollera ärligt hur många som blandade de två hattarna. Den motstridiga hänsynen är friktion, eftersom att dela upp arbete i separata commits är lite mer insats i förväg. Svaret bör forma era commitkonventioner och er granskningschecklista.

2. **Var finns vår tekniska skuld, hur mycket ränta betalar vi på den och vem avgör vad som betalas av?** De flesta team kan inte besvara detta, vilket är det egentliga problemet, eftersom skuld du inte kan se hanteras av den som klagar högst snarare än av var kostnaden verkligen finns. Att göra den synlig betyder att följa betydande poster, tagga koden och samla belägg om vilka områden som gör ändringar långsamma och felbenägna. Det motstridiga draget är att varje timme på avbetalning är en timme som inte läggs på funktioner, så beslutet måste vara ett portföljbeslut fattat med ledningen, kopplat till hur ni styr tekniskt arbete (kapitel 1.5). Ta med era data om misslyckade ändringar och er lista över filerna alla fruktar att röra. Svaret bör bli en skyddad, stadig avbetalningskapacitet, inte en vag föresats att städa när det lugnat sig.

3. **Vilka delar av vår kodbas bör vi medvetet inte refaktorisera, och hur skulle vi veta?** Att refaktorisera allt är lika mycket ett misslyckande som att refaktorisera ingenting, eftersom insats lagd på att städa stabil, sällan rörd eller snart avvecklad kod är ränta på ett lån ni inte var skyldiga. Omdömet är verkligt: en modul kan se ful ut och ändå vara fel ställe att investera i om ingen någonsin ändrar den. Ta med era data om ändringsfrekvens vid sidan av era komplexitetssignaler, eftersom skärningen mellan hög omsättning och hög komplexitet är där städning växer, medan kod med låg omsättning vanligen bäst lämnas ifred. Den motstridiga risken är att "vi lämnar den" blir en ursäkt att aldrig röra något svårt. Svaret bör ge er en uttrycklig kortlista över heta punkter värda investering och tillåtelse att ignorera de tysta hörnen.

4. **Litar vi tillräckligt på vår testsvit för att refaktorisera den kod vi mest behöver ändra, och var skulle vi behöva skriva karakteriseringstester först?** Ett skyddsnät ni inte kan lita på förvandlar refaktorisering till redigering och hopp, och i ett stort team är den mest skrämmande koden vanligen den minst testade, vilket är exakt där städning skulle betala sig mest. Ta med täcknings- och misslyckade-ändringar-data för era heta punkter och var ärliga med vilka kritiska moduler som inte skulle ge er någon varning om en omstrukturering ändrade beteende. Den motstridiga hänsynen är att skriva karakteriseringstester för äldre kod är långsamt, oglamoröst arbete som inte levererar någon funktion, så det är lätt att skjuta upp för alltid. I företags- och myndighetssystem under revision och ändringskontroll är de fastnaglade testerna också beläggen för att en ändring bevarade beteende, så att finansiera dem är en säkerhetsåtgärd och en regelefterlevnadsåtgärd på en gång. Svaret bör namnge vilka områden som får ett testskelett innan någon rör dem.

5. **När ett delsystem verkligen behöver ersättas, hur avgör vi mellan ett inkrementellt kvävarfikonangreppssätt och en omskrivning, och vem har befogenhet att säga nej till omskrivningen?** Den storskaliga omskrivningen är det mest förföriska och mest felbenägna alternativet på bordet, eftersom en ren tavla alltid ser billigare ut på pappret än att leva med de gamla begränsningarna. För en stor organisation håller den inkrementella vägen (en fasad, en bit i taget, verifierad i produktion) systemet vid liv och begränsar risk, men den är långsammare, kräver disciplin att slutföra och konkurrerar med aptiten för ett nytt avstamp. Ta med ändringsfrekvenskartan för delsystemet, en ärlig uppskattning av hur länge en omskrivning skulle pågå innan den levererade värde och de beteendeluckor en parallell omskrivning skulle behöva stänga. I myndigheter och reglerade miljöer är en flerårig omskrivning som slås ihop i slutet sällan överlevbar under revision, så svaret bör som standard vara kvävarfikon eller gren-via-abstraktion och behandla varje omskrivning som ett undantag som måste argumenteras för med belägg.

6. **Hur använder vi interna kvalitetsmått för att hitta var skuld koncentreras utan att låta ett tal bli ett mål som människor manipulerar?** Mått som komplexitet, duplicering, täckning och andel misslyckade ändringar är det enda sätt en stor organisation kan se över kod ingen enskild person läser, men i samma stund ett är kopplat till en grind eller en prestationsbedömning tar Goodharts lag över och talet slutar mäta något verkligt. Ta med exempel på där ett mått redan driver beteende, och fråga om det startar samtal eller i det tysta belönar tester som inte hävdar något och logik utsmetad över funktioner för att undvika en tröskel. Det motstridiga draget är att ledningen vill ha ett enkelt instrumentpanelstal, och "använd omdöme" är en svårare sälj än en grön stapel. I företags- och myndighetssammanhang där mått matar styrningsrapportering, var uttryckliga med att kvalitetssignaler informerar investering och lokaliserar heta punkter men aldrig grindar individer. Svaret bör dra en fast linje mellan att mäta för att lära och att mäta för att döma.

## Sektorsperspektiv

**Startup.** Med en handfull ingenjörer och ingen löptid att undvara, refaktorisera bara opportunistiskt: bär en hatt per commit så att historiken förblir bisekterbar och för en kort ärlig lista över genvägarna du tog med avsikt. Starta inte städkampanjer och polera inte stabila moduler. Lägg din knappa uppmärksamhet på den fil alla fruktar, och skriv karakteriseringstester bara där en ändring faktiskt skrämmer dig. Medveten, synlig skuld är fin i det här skedet. Hänsynslös osynlig skuld är det som dödar dig.

**Småföretag.** Utan särskild plattforms- eller verktygsspecialist och med snäv budget, lita på det din IDE och ditt språkekosystem ger gratis: automatiska omdöpnings- och extraheringsdrag, en linter och en grundläggande täckningssignal. Behandla det mesta av skulden som något du hanterar i det normala arbetets gång snarare än något du anlitar en konsult för att åtgärda, och föredra att köpa välunderhållna bibliotek framför att bygga och sedan behöva refaktorisera dina egna. Reservera den sällsynta betalda insatsen för det enda system vars långsamhet direkt kostar dig kunder.

**Storföretag.** Över många team är problemet portföljstyrning: ett gemensamt skuldregister, konsekvent taggning av heta punkter efter ändringsfrekvens och komplexitet och en skyddad del av varje teams kapacitet för avbetalning så att städning slutar förlora mot funktioner som standard. Standardisera tvåhattsdisciplinen och karakteriseringstestpraxisen så att varje ingenjör som rör sig mellan team finner samma regler, och använd kvävarfikon och gren-via-abstraktion för strukturell förändring samordnad över grupper. Håll kvalitetsmått informationsmässiga så att de lokaliserar skuld utan att manipuleras i prestationsbedömningar.

**Offentlig sektor.** Långlivade system under strikt revision och ändringskontroll gör disciplinerad refaktorisering till en regelefterlevnadstillgång, inte bara en teknisk: att hålla omstrukturering strikt åtskild från beteendeändring låter revisorer se exakt vilka commits som ändrade beteende och vilka som bara städade. Upphandlings- och transparensregler gynnar små, reversibla, belägg-baserade steg framför storskaliga omskrivningar, så välj som standard kvävarfikon med karakteriseringstester som dokumenterar att beteende bevaras. Gör skuldregistret och dess avbetalningsplan till en del av systemets underhållsregister så att tillsynsorgan får den spårbarhet de kräver.

## Exempel

**Startup.** En startup med sex personer levererar snabbt och vet att den tar på sig skuld, så den gör två billiga saker väl. Varje pull request bär en hatt: refaktoriseringscommits är åtskilda från funktionscommits, vilket håller deras historik bisekterbar även vid hög hastighet. Och de för en kort, ärlig lista över genvägarna de tog med avsikt, med en rad om räntan var och en kostar. När en betalningsmodul blir den fil alla fruktar motiverar den listan plus deras historik över misslyckade ändringar två dagar för att extrahera en renare gräns. De skriver karakteriseringstester för att fastnagla det nuvarande beteendet, refaktoriserar under det med IDE:ns omdöpnings- och extraheringsdrag och rör aldrig de stabila modulerna som ingen ändrar. Skulden de bär är medveten och synlig, så den blir aldrig den hänsynslösa sorten.

**Storföretag.** Ett globalt logistikföretag kör ett femton år gammalt ordersystem som många team ändrar varje vecka. I stället för en omskrivning antar de kvävarfikonmönstret: en fasad står framför monoliten, och en avgränsad förmåga i taget leds om till nya tjänster bakom den, verifierad i produktion innan nästa bit börjar. Att samordna detta över team och ett långlivat system (kapitel 10.4) är det svåra, så de upprätthåller ett gemensamt skuldregister, taggar heta punkter efter ändringsfrekvens och komplexitet och reserverar en fast del av varje teams kapacitet för avbetalning. Interna kvalitetsmått informerar var man ska leta men grindar aldrig någons prestationsbedömning, vilket håller talen ärliga. Över två år krymper monoliten stadigt och ingen enskild ändring riskerar någonsin hela systemet.

**Offentlig sektor.** En nationell skattemyndighet måste modernisera en decennier gammal bedömningsplattform under strikta revisions- och ändringskontrollregler, där varje kodändring är en styrd, belägg-baserad händelse. En storskalig omskrivning är omöjlig, så de använder gren-via-abstraktion: ett abstraktionslager införs över den äldre beräkningsmotorn, en ny implementation byggs bakom det och konsumenter migreras en skatteregel i taget, varje migrering dokumenterad som en liten, reversibel ändring med karakteriseringstester som bevisar att beteendet är oförändrat. Eftersom refaktorisering hålls strikt åtskild från varje lagstiftningsmässig beteendeändring kan revisorer se exakt vilka commits som ändrade beteende och vilka som bara omstrukturerade. Skuldregistret och dess avbetalningsplan blir en del av systemets underhållsregister (kapitel 3.7), vilket ger tillsynsorgan den spårbarhet de kräver.

## Affärsnytta: motiv, ROI och TCO

Avkastningen på refaktorisering och skuldavbetalning är den bestående förmågan att ändra programvara billigt, och för de flesta system är merparten av livstidskostnaden underhåll, så det är här den totala ägandekostnaden till stor del avgörs. Räntan på teknisk skuld betalas i den valuta ledningen redan följer: långsammare leverans, högre andel misslyckade ändringar, längre tid att återhämta sig från incidenter och ingenjörer som undviker den mest skrämmande koden. När du gör skulden synlig och finansierar avbetalning stadigt sänker du kostnaden för varje framtida ändring i de områden som spelar störst roll, och undviker högkonjunktur-lågkonjunktur-mönstret där försummad skuld tvingar fram en dyr nödomskrivning.

Kostnaden för att införa är måttlig och mest kulturell: etablera tvåhattsdisciplinen, bygg skyddsnätet där du behöver refaktorisera, för ett skuldregister och skydda en stadig del av kapaciteten för avbetalning. Kostnaden för försummelse växer tyst. Ränta ackumuleras på varje ändring tills hastigheten kollapsar och organisationen finner sig frusen, oförmögen att säkert ändra ett system den inte längre förstår, vilket är det dyraste utfallet av alla. För att argumentera inför ledningen, koppla skuld direkt till leveransmått de redan bryr sig om, och rama in avbetalning som ett portföljbeslut med en mätbar utdelning, inte som ingenjörer som ber om tid att städa.

## Antimönster och fallgropar

- **Att blanda refaktorisering med beteendeändring:** en commit gör båda, så ett brott kan inte tillskrivas och historiken blir opålitlig.
- **Refaktorisering utan skyddsnät:** att omstrukturera otestad kod och hoppas, vilket är redigering på tro.
- **Den storskaliga omskrivningen:** att ersätta ett fungerande system på en gång, ett mönster med hög felfrekvens och lång tid till värde.
- **Refaktorisering som en heroisk helg:** ogranskad, ohållbar städning som gör sig själv ogjord i stället för stadig kapacitet.
- **Osynlig skuld:** genvägar ingen följer, så avbetalning drivs av klagomålsvolym snarare än verklig kostnad.
- **Manipulation av kvalitetsmått:** att nå ett täcknings- eller komplexitetsmål medan verklig kvalitet sjunker, eftersom måttet blev målet.
- **Att refaktorisera fel kod:** att polera stabila eller snart avvecklade moduler medan de verkliga heta punkterna fortsätter kosta dig.
- **Ständig refaktorisering:** ändlös omstrukturering som aldrig levererar värde, spegelbilden av att aldrig städa.

## Mognadsmodell

- **Nivå 1, Initiera:** Refaktorisering är ad hoc och reaktiv, ofta blandad med beteendeändring i samma commit. Det finns inget pålitligt skyddsnät, teknisk skuld är osynlig och ospårad och städning sker bara i enstaka heroiska utbrott eller inte alls.
- **Nivå 2, Utveckla:** Vissa team skiljer refaktorisering från beteendeändring och lutar sig mot tester där de finns, och namngivna refaktoriseringar och karakteriseringstester dyker upp i fickor. Praxis är inkonsekvent över team, skuld diskuteras och loggas ibland och avbetalning konkurrerar ad hoc mot funktioner och förlorar vanligen.
- **Nivå 3, Standardisera:** Tvåhattsdisciplinen, karakteriseringstester för äldre kod och små namngivna refaktoriseringar är dokumenterade och förväntade i hela organisationen. Skuld spåras i ett gemensamt register som skiljer kapital från ränta, och en skyddad kapacitet för avbetalning planeras varje cykel och upprätthålls i granskning.
- **Nivå 4, Hantera:** Skuld och städning mäts och styrs med data mot utgångslägen. Du följer ändringsfrekvens och komplexitet för att lokalisera heta punkter, bevakar andel misslyckade ändringar och ledtid för ändringar i refaktoriserade områden och registrerar räntan varje betydande post kostar, så att avbetalningsbeslut vilar på belägg och avveckla-eller-investera-beslut fattas utifrån trender snarare än klagomålsvolym. Kvalitetssignaler informerar investering utan att kopplas till grindar människor kan manipulera.
- **Nivå 5, Orkestrera:** Skuld hanteras som en kontinuerligt omfördelad portfölj integrerad med produkt- och underhållsplanering i hela organisationen. Strukturell förändring använder rutinmässigt kvävarfikon och gren-via-abstraktion samordnat över team, avbetalning är kontinuerlig och matchad mot var förändring är frekvent och smärtsam, och praxis anpassas när systemet och dess riskbild förskjuts, så att långlivad kod förblir förändringsbar över decennier.

## Idéer för diskussion

1. Vilken är ert teams faktiska, upprätthållna regel för att hålla refaktorisering åtskild från beteendeändring, och var bryter den ihop under deadlinetryck?
2. Hur avgör ni, med belägg, vilken kod som förtjänar städning och vilken som bäst lämnas ifred?
3. Var skulle karakteriseringstester låta er säkert refaktorisera ett äldre område ni för närvarande undviker?
4. För er nästa större modernisering, hur skulle ett kvävarfikonangreppssätt se ut, och vilken fasad eller abstraktion skulle ni införa först?
5. Vem äger registret över teknisk skuld, och hur vinner avbetalning faktiskt kapacitet mot funktionsarbete?

## Viktigaste punkter

- Refaktorisering bevarar beteende. Håll den strikt åtskild från beteendeändring, i separata commits.
- En pålitlig testsvit är förutsättningen för säker refaktorisering, och karakteriseringstester ger äldre kod en.
- Arbeta i små, namngivna, reversibla steg, föredra opportunistisk städning och använd kvävarfikon eller gren-via-abstraktion för stor strukturell förändring.
- Gör teknisk skuld synlig, skilj kapital från ränta och finansiera avbetalning som stadig kapacitet snarare än hjältedåd.
- Mät intern kvalitet för att vägleda omdöme, aldrig som ett mål att manipulera, och refaktorisera inte kod som är stabil eller avsedd att avvecklas.

## Referenser och vidare läsning

- Martin Fowler, *Refactoring: Improving the Design of Existing Code*, second edition
- Michael Feathers, *Working Effectively with Legacy Code*
- Ward Cunningham, *The WyCash Portfolio Management System* (OOPSLA 1992 experience report, origin of the debt metaphor)
- Martin Fowler, "TechnicalDebtQuadrant" and "StranglerFigApplication" (martinfowler.com)
- Kent Beck, *Tidy First? A Personal Exercise in Empirical Software Design*
- Steve McConnell, *Code Complete: A Practical Handbook of Software Construction*
- Robert C. Martin, *Clean Code: A Handbook of Agile Software Craftsmanship*
