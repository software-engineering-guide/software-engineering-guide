# 4.10 Penetrationstestning och red team-övningar

## Översikt och motivation

Du kan bygga varje kontroll din hotmodell kräver och ändå inte veta om de fungerar. Dokumentationen säger att brandväggen blockerar den porten, kodgranskningen säger att indata valideras, policyn säger att minsta behörighet upprätthålls. Offensiv säkerhet är hur du får veta om något av det är sant när en motiverad angripare trycker på. Det här kapitlet handlar om att medvetet angripa dina egna system, med tillstånd, för att hitta svagheterna innan en verklig motståndare gör det.

Disciplinen löper längs ett spektrum. I den lätta änden finns [sårbarhetsskanning](https://en.wikipedia.org/wiki/Vulnerability_scanner): automatiska verktyg som sonderar efter kända brister och felkonfigurationer. I mitten finns [penetrationstestning](https://en.wikipedia.org/wiki/Penetration_test): en skicklig människa som kedjar ihop svagheter för att bevisa utnyttjningsbarhet mot ett definierat mål. I den bortre änden finns [red team-övningar](https://en.wikipedia.org/wiki/Red_team): en målstyrd kampanj som efterliknar en verklig motståndare över människor, process och teknik, och som testar din förmåga att upptäcka och svara, inte bara din förmåga att förebygga. Var och en besvarar en annan fråga, och att blanda ihop dem är det vanligaste sättet organisationer slösar pengar och tröstar sig med falsk säkring.

Det här kapitlet står medvetet vid sidan av sina grannar. Kapitel 4.4 behandlar säkerhetsdrift: den defensiva, övervakande sidan som bevakar hot och svarar på dem. Det här kapitlet är den offensiva motsvarigheten som testar om det försvaret faktiskt fungerar. Kapitel 4.9 behandlar livscykeln för säker programvaruutveckling, där säkerhet byggs in i hur kod designas och levereras. Offensiv testning validerar produkten av den livscykeln utifrån. Det bygger också på grunderna och kulturen i kapitel 4.1 och applikationssäkerhetspraxis i kapitel 4.2.

För stora företag är offensiv testning både ett riskminskningsverktyg och en regulatorisk skyldighet. Betalningsförmedlare, banker och vårdgivare möter uttryckliga krav på att testa. För myndigheter når insatserna nationell säkerhet och offentligt förtroende: motståndarna här är resursstarka nationalstater, och systemen de angriper driver val, bidrag och samhällsviktig infrastruktur. I båda sammanhangen kommer värdet inte från rapporten utan från vad du rättar och hur mycket snabbare du lär dig upptäcka nästa intrång.

## Nyckelprinciper

- Matcha uppdraget mot frågan: skanning, pentestning och red team-övningar besvarar olika saker.
- Skaffa skriftligt tillstånd och tydliga spelregler innan någon rör ett system.
- Fynd är värdelösa tills de är åtgärdade och omtestade. Följ dem som vilket annat arbete som helst.
- Ett red team finns för att göra blue team bättre, inte för att vinna.
- Efterlikna verkliga motståndare och deras tekniker, inte generiska checklistor.
- Mät detektering och svar, inte bara antalet funna sårbarheter.
- Se upp för teater: ett uppdrag avgränsat för att klara sig ser imponerande ut och bevisar ingenting.

## Rekommendationer

### Förstå spektrumet av offensiv säkerhet

Börja med att namnge vad du köper. Sårbarhetsskanning är bred, automatisk och billig. Kör den kontinuerligt mot din egendom för att fånga kända [Common Vulnerabilities and Exposures](https://en.wikipedia.org/wiki/Common_Vulnerabilities_and_Exposures) (CVE) och felkonfigurationer. Den producerar volym och falska positiva, och den kan inte säga om en brist verkligen är utnyttjningsbar i sitt sammanhang. Penetrationstestning ställer en skicklig testare mot ett definierat mål under ett fast fönster, kedjar ihop svagheter för att visa verklig konsekvens: det här skannerfyndet, kombinerat med den där svaga behörigheten, ger domänadministratör. Den besvarar "kan just den här saken brytas, och hur illa."

Red team-övningar besvarar en större fråga: "om en målmedveten motståndare riktade sig mot oss, skulle vi märka det, och kunde vi stoppa dem." Den är målorienterad (exfiltrera den här datamängden, nå det här styrsystemet), täcker hela angreppsytan inklusive människor och fysisk åtkomst och körs vanligen utan att varna försvararna. [Purple team-övningar](https://en.wikipedia.org/wiki/Red_team#Purple_team) rasar muren: red och blue arbetar tillsammans i samma rum, angriparen kör en teknik och försvararen ser om deras verktyg fångar den och justerar detekteringar i realtid. Purple team-övningar ger ofta mer defensiv förbättring per krona än ett dolt red team, eftersom varje åtgärd blir ett lärandetillfälle.

### Välj svart, grå eller vit låda medvetet

Hur mycket du berättar för testaren formar vad du lär dig. Svartlådetestning ger dem inget annat än ett mål och simulerar en extern angripare utan insiderkunskap. Den är realistisk men långsam, och testare kan lägga hela budgeten på rekognosering som en verklig motståndare skulle ta månader på. Vitlådetestning överlämnar källkod, arkitekturdiagram och uppgifter och låter testaren gå på djupet och täcka mer mark på den tid som finns. Gråbox sitter emellan: viss kunskap, vissa uppgifter, som efterliknar en angripare som gjort sin hemläxa eller en illasinnad insider.

För det mesta av applikationstestning ger grå eller vit låda bättre avkastning, eftersom du betalar för djup i analysen, inte för att testaren ska återupptäcka din delnätslayout. Reservera svart låda för när realismen i upptäcktsfasen i sig är det du vill testa, som att mäta hur mycket en utomstående kan lära sig av ditt publika fotavtryck. Var uttrycklig om vilken du beställer, eftersom en svartlåderapport som hittar lite kan betyda att du är säker eller att testaren fick slut på tid vid perimetern.

### Avgränsa noggrant och skriv spelreglerna

Avgränsningen är där uppdrag lyckas eller misslyckas. Ett dokument med [spelregler](https://en.wikipedia.org/wiki/Rules_of_engagement) (rules of engagement) definierar vad som är inom gränserna och vad som inte är det, vilka tekniker som är tillåtna, testfönstret, de system och nätverk som omfattas, krav på datahantering och nödkontakter på båda sidor. Det namnger de produktionssystem som är förbjudna eller kräver försiktighet, sätter en regel för att stanna om testaren hittar något aktivt farligt och definierar vad som händer om de snubblar över verklig angriparaktivitet eller genuint känslig data.

Skriv ned eskaleringsvägar och ett "kom ut ur fängelset gratis"-brev: ett tillstånd testaren kan visa upp om säkerhetspersonal eller rättsväsende ifrågasätter dem mitt under uppdraget. Kom överens i förväg om hur fynd lagras och överförs, eftersom en pentestrapport är en karta över hur man bryter sig in hos dig och måste skyddas därefter. Snäv avgränsning ger djupa fynd på en liten yta. Bred avgränsning ger ytlig täckning av en stor. Välj med avsikt, och låt aldrig avgränsningen i tysthet växa under uppdraget utan ny auktorisering.

### Behandla tillstånd som gränsen mellan testning och brott

Den enda handling som skiljer en penetrationstestare från en brottsling är tillstånd. Att komma åt system du inte har tillstånd att komma åt är ett brott enligt lagar som [Computer Fraud and Abuse Act](https://en.wikipedia.org/wiki/Computer_Fraud_and_Abuse_Act) i USA och motsvarigheter på andra håll, och goda avsikter är inget försvar. Tillståndet måste komma skriftligen från någon med den faktiska befogenheten att bevilja det, täcka exakt de system och tekniker som ingår och vara undertecknat innan arbetet börjar.

Tredjepartssystem komplicerar detta. Din molnleverantör, dina leverantörer av programvara som tjänst och all delad infrastruktur kan ha egna testpolicyer, och du kan inte auktorisera en attack mot tillgångar du inte äger. Kontrollera leverantörens regler, begär tillstånd där det krävs och håll testningen inom din egen tenant. Social manipulation riktad mot anställda väcker etiska och rättsliga frågor om samtycke och psykisk skada som du måste tänka igenom i förväg. När du är osäker, involvera juridiskt biträde. Kostnaden för ett samtal är trivial mot kostnaden för en incident med obehörig åtkomst.

### Väg interna team mot tredjepartstestare

Ett internt red team känner din miljö, bygger relationer med försvarare och kan testa kontinuerligt snarare än i årliga skurar. Den förtrogenheten är också en begränsning: de delar dina blinda fläckar och organisatoriska antaganden, och deras oberoende kan ifrågasättas när de rapporterar till samma ledning som systemen de testar. Tredjepartsföretag ger nya ögon, specialiserade färdigheter och det oberoende som revisorer och tillsynsmyndigheter ofta kräver, men de kommer långsamt i gång, kostar mer per uppdrag och lämnar när rapporten är levererad.

De flesta mogna program använder båda. Interna team hanterar kontinuerlig motståndaremulering, detekteringsjustering och den djupa miljökännedom som gör purple team-övningar produktiva. Externa företag ger periodisk oberoende validering, uppfyller oberoendekraven i standarder som PCI DSS och sonderar de områden era egna människor har slutat se. Vilket du än använder, insistera på att testarna är kvalificerade: certifieringar som OSCP (Offensive Security Certified Professional) och påvisad erfarenhet betyder mer än en polerad säljpresentation.

### Driv bug bounty-program och samordnat utlämnande

Ett [bug bounty](https://en.wikipedia.org/wiki/Bug_bounty_program)-program bjuder in externa forskare att hitta och rapportera sårbarheter i utbyte mot erkännande och betalning. Det ger dig kontinuerlig, folkmassebaserad testning över en bredd av färdigheter du aldrig kunde anställa på en gång, och du betalar bara för verkliga fynd. Det är ingen ersättning för strukturerad pentestning, eftersom forskare jagar det som betalar och kan ignorera hela kategorier, men det är ett kraftfullt komplement som blottlägger kreativa attacker.

Innan du kör ett betalt bounty behöver du en policy för [samordnat utlämnande av sårbarheter](https://en.wikipedia.org/wiki/Coordinated_vulnerability_disclosure): ett publicerat, lätt hittat sätt för vem som helst att rapportera ett säkerhetsproblem säkert, ett åtagande att inte rättsligt förfölja forskare i god tro, definierade svarstider och en intern process för att triagera och rätta det som kommer in. En security.txt-fil och en tydlig rapporteringsadress är minimum. Myndigheter föreskriver alltmer policyer för utlämnande av sårbarheter för publikt vända system, och att sakna en kanal hindrar inte forskare från att hitta buggar. Det hindrar dem bara från att berätta för dig på ett säkert sätt.

### Använd antaget intrång och motståndaremulering

Testning enbart av perimetern antar att angriparen börjar utanför, men verkliga intrång börjar ofta med en nätfiskad uppgift eller en komprometterad bärbar dator som redan är inne. En övning med [antaget intrång](https://en.wikipedia.org/wiki/Breach_and_attack_simulation) startar testaren med ett fotfäste, som åtkomst som en vanlig anställd, och frågar hur långt de kan nå därifrån. Det testar direkt er interna segmentering, detektering och kontroller av sprängradie, snarare än att satsa allt på en perimeter som så småningom kommer att korsas. Det är vanligen en bättre användning av ett red teams tid än att se dem slita mot en härdad kant.

Förankra kampanjen i verkligt motståndarbeteende med [MITRE ATT&CK](https://en.wikipedia.org/wiki/MITRE_ATT%26CK), en publik kunskapsbas över de taktiker och tekniker angripare faktiskt använder, organiserade från första åtkomst till exfiltrering. Motståndaremulering väljer en hotaktör känd för att rikta in sig på din sektor, återskapar deras dokumenterade tekniker och testar om du upptäcker och stoppar varje steg. Detta är långt mer användbart än en generisk attack, eftersom det mappar dina försvar mot de specifika motståndare du möter och producerar fynd din hotunderrättelse kan prioritera.

### Mata fynd till blue team och detekteringsteknik

Poängen med offensiv är bättre försvar. Varje red team-åtgärd är ett tillfälle att fråga: genererade våra verktyg en signal, såg någon den och svarade de rätt. Kör uppdrag så att varje teknik mappar mot en detektering ni antingen har, behöver bygga eller behöver justera. Detta är detekteringsteknik: att förvandla angriparbeteende till pålitliga larm, och det är där red team-värdet ackumuleras. Ett fynd att "vi upptäcktes inte under lateral rörelse" bör bli en ny detekteringsregel, testad genom att köra om tekniken.

Bordsövningar utvidgar detta till beslutsfattande. Samla de människor som skulle svara på en verklig incident och gå igenom ett realistiskt scenario på papper: vem utropar incidenten, vem talar med juridik, vem beslutar att ta ett system offline. Bordsövningar är billiga, blottlägger luckor i roller och kommunikation som tekniska tester missar och förbereder de människor som spelar störst roll när incidenthanteringen i kapitel 9.3 går live. Para tekniska red team-övningar med regelbundna bordsövningar så att både era verktyg och era människor övas.

### Följ åtgärd och omtesta

En sårbarhetsrapport som ingen agerar på är en skuld, eftersom ni nu medvetet kör en brist en revisor kan citera. Mata varje fynd in i ert vanliga arbetsspårningssystem med en ägare, en allvarlighetsgrad och ett förfallodatum knutet till risk. Kritiska fynd får akut behandling. Lägre fynd ansluter till eftersläpningen med ärlig prioritet. Måttet som räknas är tid till åtgärd, inte tid till rapport.

Omtestning stänger loopen. Efter att en rättelse levererats bekräftar testaren (eller en automatisk kontroll) att sårbarheten faktiskt är borta och att rättelsen inte öppnade ett nytt hål. Utan omtestning är "åtgärdad" ett hopp, inte ett faktum, och många fynd återkommer eftersom en rättelse var ofullständig eller en regression återinförde dem. Standarder som PCI DSS kräver denna loop uttryckligen. Bygg in omtestning i uppdragsavtalet så att den inte är en bortglömd eftertanke.

## Avvägningar: för- och nackdelar

| Tillvägagångssätt | Bäst för | Fördelar | Nackdelar |
|---|---|---|---|
| Sårbarhetsskanning | Kontinuerlig täckning av kända brister | Billig, bred, automatisk, frekvent | Brusig. Kan inte bevisa utnyttjningsbarhet |
| Penetrationstestning | Bevisa konsekvens mot ett definierat mål | Djup, mänsklig insikt. Verkliga exploateringskedjor | Vid en tidpunkt. Snävt avgränsad. Kostsam |
| Red team-övningar | Testa detektering och svar | Realistisk. Övar människor och process | Dyr. Långsam. Kräver moget blue team |
| Purple team-övningar | Förbättra detekteringar snabbt | Mycket lärande per krona. Samarbetsinriktad | Mindre realistisk. Kräver att båda team är tillgängliga |
| Bug bounty | Löpande folkmassebaserad upptäckt | Betala per fynd. Varierande färdigheter | Ojämn täckning. Triagebörda. Kräver process |

Den centrala spänningen är realism mot inlärningshastighet. Ett dolt red team är det mest realistiska test du kan köra, men dess lärdomar anländer långsamt och först efter en hel kampanj, och ett omoget blue team lär sig lite av att i tysthet bli besegrat. Purple team-övningar offrar överraskning för att maximera hur snabbt försvarare förbättras. En andra spänning är bredd mot djup: skanning täcker allt ytligt, medan ett pentest täcker en skiva på djupet. Mogna program lagerindelar dessa i stället för att välja en, och kör kontinuerlig skanning under periodisk djup testning och enstaka red team-kampanjer med full omfattning. Det felaktiga draget är att köpa ett enda årligt pentest, arkivera rapporten och kalla problemet löst.

## Frågor att diskutera med ditt team

1. **När vi beställer offensiv testning, är vi tydliga med vilken fråga vi faktiskt ställer, och matchar uppdraget den?** Många organisationer köper ett "penetrationstest" och får en sårbarhetsskanning med en människoskriven sammanfattning, och tror sedan att de har testat sina försvar när de bara har kontrollerat efter kända brister. Andra beställer ett red team när deras detekteringsförmåga är så omogen att övningen bara bevisar det alla redan visste. Ta med era tre senaste uppdragsavgränsningar och de resulterande rapporterna och fråga om var och en besvarade den fråga ni behövde besvarad: täckning av kända sårbarheter, utnyttjningsbarhet hos ett specifikt mål eller förmåga att upptäcka och svara på ett intrång. Svaret bör forma en medveten blandning av skanning, pentestning och red eller purple team-övningar matchad mot er mognad.

2. **Vad händer med ett fynd efter att rapporten landar, och hur skulle vi bevisa att det rättades?** Värdet av offensiv säkerhet ligger helt i åtgärd, men många program mäter framgång efter rapportens storlek snarare än riskens krympning. Spåra ett verkligt fynd från ert senaste uppdrag: vem ägde det, hur prioriterades det mot funktionsarbete, när rättades det och bekräftade någon att rättelsen faktiskt fungerade? Om ni inte kan ta fram det spåret genererar er testning kunskap ni inte agerar på, vilket är värre än att inte veta, eftersom ni nu medvetet är exponerade. Utfallet av denna diskussion bör vara ett spårat åtgärdsarbetsflöde med ägare, riskbaserade deadlines och obligatorisk omtestning inbyggd i varje avtal.

3. **Gör vårt red team vårt blue team bättre, eller håller det bara poäng?** Ett red team som firar oupptäckta segrar och hamstrar sina tekniker är underhållande och värdelöst. Relationen bör vara samarbetsinriktad under den motståndarmässiga ytan: varje teknik som går oupptäckt bör bli en ny detekteringsregel, varje lyckad väg bör informera segmenteringen och de två teamen bör debriefa tillsammans. Fråga era försvarare vad de lärde sig av det senaste red team-uppdraget och om någon konkret detektering eller kontroll ändrades som ett resultat. Om det ärliga svaret är ingenting betalar ni för teater, och ni bör skifta mot purple team-övningar och motståndaremulering uttryckligen knuten till detekteringsteknik.

4. **Före vårt nästa uppdrag, har vi skriftligt tillstånd för varje tillgång i omfattningen, inklusive de vi inte äger?** Tillstånd är linjen mellan ett penetrationstest och en datorbrottsincident, och i en stor organisation sitter de system en testare kommer att röra sällan inom en enda ägandegräns: de spänner över molntenants, plattformar för programvara som tjänst, hanterade nätverk och delad infrastruktur som en partner eller leverantör kontrollerar. Det konkurrerande trycket är hastighet, eftersom att jaga undertecknat tillstånd och leverantörers testpolicyer är långsamt och frestande att hoppa över när en deadline hotar. Ta med utkastet till spelregler, tillgångsinventeringen med en ägare namngiven mot varje system, relevanta moln- och leverantörstestpolicyer och tillståndsbrevet testaren kan visa upp om de ifrågasätts mitt under uppdraget. För företags- och myndighetsarbete är exponeringen akut: en obehörig sondering mot en delad plattform kan bryta avtal, utlösa regulatorisk rapportering eller, för en offentlig myndighet, bli en rubrik om att staten angrep system den inte hade rätt att röra, så juridiskt biträde bör godkänna innan någon börjar.

5. **Investerar vi i ett internt red team, externa företag eller båda, och matchar den fördelningen det vi faktiskt behöver?** Detta är ett avgörande mellan bygg och köp med verkliga pengar och konsekvenser på flera år: ett internt team kostar löner och verktyg och levererar kontinuerlig motståndaremulering och djup miljökännedom, medan externa företag kostar mer per uppdrag men ger nya ögon, specialiserade färdigheter och det oberoende som revisorer och tillsynsmyndigheter kräver. Spänningen är att var och en täcker den andras blinda fläck, så att behandla dem som substitut snarare än komplement lämnar vanligen en lucka. Ta med er nuvarande utgift för varje, certifieringarna och den påvisade meritlistan hos människorna som utför arbetet, takten på uppdragen och de oberoendekrav era standarder ställer. I ett reglerat företag kan PCI DSS och liknande regimer tvinga fram extern oberoende testning oavsett hur bra ert interna team är. I myndigheter gör upphandlingsregler och behovet av att visa en bedömning på armlängds avstånd före ett tillstånd att driva ofta en ackrediterad tredje part obligatorisk, inte valfri.

6. **Har vi en säker kanal för externa forskare att rapportera sårbarheter, och är vi redo att hantera det som kommer in?** En stor publikt vänd organisation sonderas redan av forskare vare sig den bjuder in dem eller inte, och den enda frågan är om de kan berätta för er säkert eller tvingas publicera eller sälja det de hittar. Den konkurrerande hänsynen är beredskap: att öppna en policy för samordnat utlämnande eller ett betalt bug bounty genererar inkommande rapporter och en triagebörda, och ett program som betalar för fynd det aldrig rättar är värre än inget. Ta med er nuvarande security.txt-fil och rapporteringsadress om ni har någon, er mottagnings- och triageprocess, de svarstider ni ärligt kan åta er och eftersläpningskapaciteten att åtgärda det som anländer. För myndigheter är en policy för utlämnande av sårbarheter på publika system alltmer ett direktiv snarare än en artighet, och för företag är ett välskött bounty både en källa till kreativa fynd och belägg för mognad under kundernas due diligence, så beslutet handlar mindre om att ha en kanal än om ni är bemannade för att hedra den.

## Sektorsperspektiv

**Startup.** Du har inte råd med ett internt red team, så lagerindela billig täckning i stället. Koppla in sårbarhetsskanning i din driftsättningspipeline för att fånga kända beroendebrister vid varje bygge, publicera en security.txt-fil och en enkel policy för samordnat utlämnande så att forskare kan nå dig och beställ ett enda gråbox-penetrationstest från ett välrenommerat företag före din första företagsaffär, och följ varje fynd till en bekräftad rättelse. Hastighet spelar större roll än ett brett program: välj det ena test som låser upp en försäljning eller stänger din största risk och hoppa över resten tills du växer.

**Småföretag.** Utan säkerhetsspecialist i personalen och med snäv budget, köp snarare än bygg. Använd en hanterad skanningstjänst och anlita ett externt pentestföretag med blygsam takt i stället för att resa någon intern förmåga, och se till att ditt avtal inkluderar en omtestning så att "åtgärdat" är bevisat, inte antaget. Ditt mest värdefulla, billigaste drag är ett publicerat sätt för vem som helst att rapportera en brist plus disciplinen att patcha snabbt, eftersom det mesta av verklig komprometterande av ett företag i din storlek kommer genom kända, opatchade svagheter.

**Storföretag.** I skala är utmaningen styrning över många team. Kör kontinuerlig skanning under periodiska oberoende externa pentester som uppfyller standarder som PCI DSS, underhåll ett internt red team för kontinuerlig motståndaremulering och purple team-övningar och hantera åtgärd som en spårad portfölj med ägare, riskbaserade deadlines och obligatorisk omtestning. Mata varje oupptäckt teknik in i detekteringsteknik och producera de revisionsbelägg, den täckning, de tidslinjer och de stängningsfrekvenser som regelefterlevnad och din styrelse förväntar sig.

**Offentlig sektor.** Upphandlingsregler, transparens och offentlig ansvarsskyldighet formar hela programmet. Underhåll en policy för utlämnande av sårbarheter på publikt vända system, som direktiv alltmer kräver, använd ackrediterade oberoende bedömare för den penetrationstestning som grindar ett systems tillstånd att driva och modellera motståndaremulering på de specifika nationalstatsaktörer dina underrättelsepartner flaggar. Behandla tillstånd, avgränsning och datahantering med extra stringens eftersom systemen driver val, bidrag och samhällsviktig infrastruktur, och gör omtestning till en förutsättning för att hålla något system i drift.

## Exempel

**Startup.** En fintechstartup på tjugo personer har inte råd med ett internt red team, så den lagerindelar det den kan. Automatisk sårbarhetsskanning körs vid varje driftsättning genom pipelinen och fångar kända beroendebrister tidigt. Den publicerar en security.txt-fil och en enkel policy för samordnat utlämnande, och öppnar sedan ett blygsamt bug bounty på en publik plattform när produkten stabiliserats och betalar verkliga forskare för verkliga buggar. Före sin första företagskund beställer den ett gråbox-penetrationstest av applikationen från ett välrenommerat företag, följer varje fynd till avslut i sitt vanliga ärendehanteringssystem och betalar för en omtestning för att bekräfta rättelserna. Detta lagerindelade tillvägagångssätt ger trovärdig säkerhetstäckning till en kostnad startupen kan upprätthålla, och pentestrapporten blir belägg den kan dela under kunders due diligence.

**Storföretag.** En multinationell detaljhandlare som behandlar kortbetalningar måste uppfylla PCI DSS, som kräver både intern och extern penetrationstestning minst årligen och efter betydande ändringar, plus segmenteringstestning för att bevisa att kortinnehavarmiljön är isolerad. Den kör kontinuerlig skanning över tusentals tillgångar, beställer oberoende externa pentester för att uppfylla standarden och underhåller ett internt red team som kör övningar med antaget intrång förankrade i MITRE ATT&CK mot hotaktörer kända för att rikta in sig på detaljhandel. Red team arbetar nära säkerhetsdriftfunktionen i kapitel 4.4: varje oupptäckt teknik blir ett ärende för detekteringsteknik, och kvartalsvisa purple team-möten justerar larmen. Åtgärd följs med riskbaserade deadlines, och hela programmet producerar de revisionsbelägg som regelefterlevnaden i kapitel 4.6 kräver.

**Offentlig sektor.** En nationell myndighet som driver medborgarsystem för bidrag möter nationalstatsmotståndare och ett offentligt uppdrag att skydda känsliga personuppgifter. Den underhåller en policy för utlämnande av sårbarheter på alla publikt vända system, som myndighetsdirektiv alltmer kräver, och ger forskare en säker kanal att rapportera brister. Oberoende tredjepartsbedömare genomför penetrationstester som en del av godkännandeprocessen innan något system går live, och kontinuerlig övervakning inkluderar löpande skanning. Myndigheten kör motståndaremulering modellerad på de specifika hotgrupper dess underrättelsepartner flaggar, och regelbundna bordsövningar repeterar det incidentsvar och den juridiska samordning ett verkligt intrång skulle kräva. Fynd matar ett formellt åtgärdsprogram med föreskrivna tidslinjer, och omtestning är en förutsättning för att behålla ett systems tillstånd att driva.

## Affärsnytta: motiv, ROI och TCO

Avkastningen på offensiv säkerhet är intrånget du inte drabbades av. Ett allvarligt dataintrång kostar miljoner i direkt svar, regulatoriska viten, rättsligt ansvar, kundavhopp och anseendeskada, och den enskilt dyraste faktorn är hur länge ett intrång förblir oupptäckt. Red team- och purple team-övningar angriper det talet direkt genom att krympa klyftan mellan komprometterande och detektering. Ett penetrationstest som hittar en utnyttjningsbar väg till din kunddatabas, rättad innan en angripare hittar den, betalar för hela programmet många gånger om i en enda undviken incident.

Det finns hårda drivkrafter också. PCI DSS föreskriver penetrationstestning för alla som hanterar kortdata. Ramverk och myndighetsregimer för godkännande kräver oberoende bedömning före och under drift. Företagskunder kräver färska pentestrapporter som villkor i avtal. I dessa fall är testningen inte valfri, och frågan är bara om du utvinner verkligt säkerhetsvärde ur pengar du ändå måste spendera.

Den totala ägandekostnaden inkluderar mer än uppdragsavgiften. Budgetera för verktygen och personalen i ett internt team om du bygger ett, triagebördan i ett bug bounty och framför allt åtgärdsarbetet fynd genererar, som är där den verkliga utgiften landar. Ett program som beställer tester men underfinansierar rättelser är det sämsta av två världar: det betalar för de dåliga nyheterna och betalar sedan igen när det ignorerade fyndet utnyttjas. För att driva ärendet inför ledningen, koppla testning till mått de följer: genomsnittlig tid att upptäcka, genomsnittlig tid att åtgärda, stängda revisionsfynd och riskminskningen på dina mest kritiska tillgångar.

## Antimönster och fallgropar

- **Skanna-och-döp-om:** att sälja en sårbarhetsskanning som ett penetrationstest och leverera ett verktygs utdata utan mänsklig validering eller kedjning av exploateringar.
- **Rapportera och glöm:** att behandla leveransen som målet, arkivera fynden och aldrig följa åtgärd eller omtesta.
- **Avgränsa för att klara:** att snäva in uppdraget så att de system som mest sannolikt faller bekvämt ligger utanför gränserna och producera en ren rapport som inte betyder något.
- **Red team som resultattavla:** ett motståndarteam som hamstrar tekniker och firar segrar i stället för att göra försvarare bättre.
- **Att dolt testa ett omoget blue team:** att köra ett smygande red team innan ni har någon detekteringsförmåga, så att övningen bara bevisar det ni redan visste.
- **Inget tillstånd eller vag avgränsning:** att börja arbeta utan skriftligt tillstånd, eller låta avgränsningen krypa in i system ni inte äger och inbjuda till rättslig katastrof.
- **Perimeterbesatthet:** att bara testa den externa kanten medan verkligheten med antaget intrång ignoreras, där angripare börjar inne.
- **Att ignorera utlämnandekanalen:** att inte ha något säkert sätt för externa forskare att rapportera buggar, så att de publicerar offentligt eller säljer i stället.
- **Teatermått:** att räkna funna sårbarheter snarare än minskad risk, förbättrad detektering och förkortad tid till åtgärd.

## Mognadsmodell

- **Nivå 1, Initiera:** Testning är tillfällig och reaktiv, ofta ett enda årligt pentest gjort för att kryssa en ruta, eller utlöst först efter en incident. Rapporter arkiveras med liten uppföljning, åtgärd är ospårad, det finns ingen utlämnandekanal och detektering av ett verkligt intrång är otestad och sannolikt frånvarande.
- **Nivå 2, Utveckla:** Sårbarhetsskanning och penetrationstestning finns men är inkonsekventa över team, där vissa grupper skannar kontinuerligt och andra inte alls. Fynd fångas någonstans, fast ägare och deadlines är fläckiga, omtestning är ad hoc och en kanal för samordnat utlämnande kan finnas för vissa system men inte hela egendomen.
- **Nivå 3, Standardisera:** Offensiv testning är ett dokumenterat program som upprätthålls i hela organisationen, inte en händelse. Skanning körs kontinuerligt under schemalagda penetrationstester beställda med definierad takt och efter större ändringar, spelregler och tillstånd är standardpraxis, varje fynd följs till avslut med en ägare och en riskbaserad deadline, omtestning är obligatorisk och en policy för samordnat utlämnande täcker alla publikt vända system.
- **Nivå 4, Hantera:** Programmet mäts och styrs mot utgångslägen. Ni följer genomsnittlig tid att upptäcka och genomsnittlig tid att åtgärda, andelen red team-tekniker som gav en signal, detekteringstäckning mot de MITRE ATT&CK-tekniker som är relevanta för er sektor, återkommande fynd och svarstider för utlämnande, och ni håller varje mått mot ett mål och agerar när det driver. Övningar med antaget intrång och motståndaremulering är rutin, ett red team verkar kontinuerligt, fynd matar detekteringsteknik och beslut att gå eller inte gå vilar på belägg snarare än åsikt.
- **Nivå 5, Orkestrera:** Red team- och purple team-övningar är integrerade i hela organisationen och adaptiva. Varje teknik mappar mot en testad detektering, motståndaremulering följer de specifika hotaktörer som för närvarande riktar in sig på din sektor när underrättelser skiftar och programmet förfinar kontinuerligt sin avgränsning, sina tekniker och sina mått medan det lär sig. Offensiv testning, säkerhetsdrift, detekteringsteknik och incidentsvar verkar som en loop som mätbart krymper klyftan mellan komprometterande och detektering över tid.

## Idéer för diskussion

1. Om en verklig angripare fick fotfäste som en vanlig anställd i dag, hur långt kunde de nå innan någon märkte det, och hur vet ni det?
2. Vilka av era senaste uppdrag var genuint realistiska, och vilka var avgränsade så att de troliga felen bekvämt låg utanför gränserna?
3. Hur många fynd från ert förra test är fortfarande öppna, och vad säger det om huruvida testning eller åtgärd är er verkliga flaskhals?
4. Har externa forskare ett säkert, tydligt sätt att rapportera en sårbarhet till er, och vad händer när en rapport anländer?
5. När övade era incidentsvarare senast ett intrång på papper, och blottlade bordsövningen luckor era tekniska tester missade?
6. Mäter ni funna sårbarheter, eller mäter ni förbättrad detektering och minskad risk?

## Viktigaste punkter

- Offensiv säkerhet är ett spektrum: skanning hittar kända brister, pentestning bevisar utnyttjningsbarhet och red team-övningar testar detektering och svar. Matcha uppdraget mot frågan.
- Skriftligt tillstånd och tydliga spelregler är linjen mellan säkerhetstestning och brott. Hoppa aldrig över dem, särskilt på system du inte fullt ut äger.
- Värdet ligger i åtgärd och omtestning, inte rapporten. Följ varje fynd med en ägare, en riskbaserad deadline och en bekräftad rättelse.
- Ett red team finns för att göra blue team bättre. Mata fynd in i detekteringsteknik, föredra purple team-övningar och övningar med antaget intrång och förankra kampanjer i verkliga motståndartekniker via MITRE ATT&CK.
- Mät detektering och svar, inte bara antal sårbarheter, och se upp för uppdrag avgränsade för att klara, som producerar komfort utan säkerhet.

## Referenser och vidare läsning

- Georgia Weidman, *Penetration Testing: A Hands-On Introduction to Hacking*
- Peter Kim, *The Hacker Playbook 3: Practical Guide to Penetration Testing*
- Jim O'Gorman, Devon Kearns, and Mati Aharoni, *Metasploit: The Penetration Tester's Guide*
- Joe Vest and James Tubberville, *Red Team Development and Operations: A Practical Guide*
- MITRE, *MITRE ATT&CK* framework and knowledge base
- Payment Card Industry Security Standards Council, *PCI DSS Requirements and Testing Procedures* and *Penetration Testing Guidance*
- National Institute of Standards and Technology, *NIST SP 800-115: Technical Guide to Information Security Testing and Assessment*
- Dafydd Stuttard and Marcus Pinto, *The Web Application Hacker's Handbook*
