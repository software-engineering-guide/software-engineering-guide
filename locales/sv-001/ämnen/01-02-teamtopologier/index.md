# 1.2 Teamtopologier och organisationsdesign

## Översikt och motivation

Hur du delar upp människor i team avgör vilken programvara du kan bygga och hur snabbt du kan bygga den. Det är ingen metafor. Det är en nästan mekanisk följd känd som [Conways lag](https://en.wikipedia.org/wiki/Conway%27s_law): organisationer designar system som speglar deras egna kommunikationsstrukturer. Om tre team bygger en [kompilator](https://en.wikipedia.org/wiki/Compiler) får du en kompilator i tre pass. Om din betalningslogik är uppdelad på ett frontendteam, ett backendteam och ett databasteam kräver varje betalningsändring samordning mellan tre parter. För en liten organisation är det hanterbart. För en stor blir organisationsschemats form den dominerande begränsningen för din utveckling, din arkitektur, din leveranshastighet och din kvalitet. Att utforma teamstrukturen är därför en förstklassig teknisk aktivitet, inte en HR-eftertanke.

Teamtopologier ger dig ett medvetet ordförråd för den designen. I stället för att låta strukturen växa fram av en slump genom omorganisationer och bemanning väljer mogna organisationer teamtyper och interaktionssätt med avsikt, och de omprövar valen när systemet och verksamheten utvecklas. Målet är att hålla varje teams [kognitiva belastning](https://en.wikipedia.org/wiki/Cognitive_load) låg, den totala mängd ett team måste ha i huvudet för att vara effektivt, så att team kan äga sin domän från början till slut och leverera ett jämnt flöde av värde utan att ständigt vänta på andra.

För företag och myndigheter är den här disciplinen avgörande. Stora organisationer breder naturligt ut sig i djupa hierarkier, delade tjänster med långa köer och överlämningskedjor som förvandlar en tvådagarsändring till ett tvåmånadersprojekt. Offentlig sektor lägger till upphandlingsgränser, konsultteam och föreskrivna [funktionsuppdelningar](https://en.wikipedia.org/wiki/Separation_of_duties) som splittrar ägarskapet ytterligare. Uttrycklig topologidesign är hur de här organisationerna återvinner flödet: justera team efter värdeströmmar, bygg plattformar som minskar den kognitiva belastningen och välj interaktionsmönster som gör beroenden synliga och avsiktliga i stället för dolda och ständiga.

## Nyckelprinciper

- Conways lag är oundviklig. Utforma team så att de matchar den programvaruutveckling du vill ha ("den omvända manövern").
- Optimera för teamets kognitiva belastning, inte för maximalt utnyttjande av individer.
- Föredra strömjusterade team som äger en del av värdet från början till slut.
- Plattformar finns för att minska de strömjusterade teamens kognitiva belastning, inte för att vara grindvakter.
- Gör teaminteraktioner uttryckliga och få: samarbete, X-som-en-tjänst eller stödjande.
- Minimera beroenden. Varje överlämning mellan team är en kö och en risk.
- Teamstrukturen är en levande design som måste utvecklas när systemet och verksamheten förändras.

## Rekommendationer

### Använd de fyra grundläggande teamtyperna

Teamtopologier definierar fyra teamtyper som täcker de flesta behov. Strömjusterade team är standarden: vart och ett äger ett kontinuerligt arbetsflöde för en viss produkt, tjänst eller användarresa, från början till slut. Plattformsteam tillhandahåller interna produkter (beräkning, driftsättning, datapipelines, identitet) som strömjusterade team använder via självbetjäning, vilket sänker deras kognitiva belastning. Stödjande team är specialister (testning, säkerhet, observerbarhet) som coachar strömjusterade team att bygga en förmåga och sedan drar sig tillbaka. Team för komplicerade delsystem äger komponenter som kräver djup specialistkunskap (en prismotor, en [videokodek](https://en.wikipedia.org/wiki/Video_codec), en kryptografisk modul), där det inte är meningsfullt att varje team bär den kunskapen. De flesta av dina team bör vara strömjusterade. De andra tre typerna finns för att stödja dem.

### Tillämpa den omvända Conway-manövern

Eftersom programvara speglar organisationens struktur, forma dina team så att de producerar den programvara du vill ha. Vill du ha löst kopplade tjänster med tydliga gränser? Skapa löst kopplade team med tydliga ägarskapsgränser. Vill du ha en betalningsförmåga som levereras enligt sitt eget schema? Bilda ett betalningsteam som äger den från början till slut. Bekämpa inte Conways lag med heroisk samordning. Dra om teamgränserna så att den arkitektur du vill ha blir den väg som kräver minst motstånd.

### Hantera kognitiv belastning uttryckligt

Ett team kan bara bemästra så mycket. Kognitiv belastning omfattar domänkomplexiteten, teknikerna, driftbördan och bredden på intressenter. När ett team äger för många orelaterade tjänster rasar både kvalitet och hastighet. Avgränsa därför varje teams ansvar till en domän det verkligen kan bemästra, och använd plattformar och stödjande team för att ta bort odifferentierad komplexitet från deras bord. Håll team på ungefär fem till nio personer: små nog att kommunicera lätt och, så att säga, mättas av ett par pizzor.

### Välj interaktionssätt medvetet

Begränsa teaminteraktioner till tre sätt. Samarbete är nära arbete med hög bandbredd mellan två team under en bestämd period. Det är kraftfullt för upptäckt men dyrt, så håll det tillfälligt. X-som-en-tjänst är en ren leverantörs-och-konsumentrelation med ett väldefinierat gränssnitt, idealisk för plattformsanvändning i stor skala. Stödjande är när ett team hjälper ett annat att lära sig, vilket är vad stödjande team gör. Namnge sättet för varje viktig relation mellan team, och läs långvarigt samarbete mellan samma två team som en signal att deras gräns ligger fel.

### Välj en driftsmodell för tvärgående funktioner

Säkerhet, data, design och liknande discipliner kan organiseras på tre sätt: centraliserat (ett team äger det åt alla), federerat (specialister inbäddade på deltid som samordnar sig genom ett gille) eller inbäddat (en dedikerad specialist inom varje strömjusterat team). Centraliserat ger enhetlighet och djup men blir en flaskhals. Inbäddat ger hastighet och sammanhang men riskerar inkonsekvens och dubbelarbete. Federerat (ofta en nav-och-ekrar- eller [praktikgemenskapsmodell](https://en.wikipedia.org/wiki/Community_of_practice)) ligger mellan de två. Välj per funktion och per skala. De flesta stora organisationer landar i federerat för de här disciplinerna, med en liten central kärna som sätter standarder.

### Investera i inner source

[Inner source](https://en.wikipedia.org/wiki/Inner_source) tar [öppen källkod](https://en.wikipedia.org/wiki/Open-source_software)-mönster för samarbete in i organisationen: delade interna repositorier, publicerade riktlinjer för bidrag, [kodgranskning](https://en.wikipedia.org/wiki/Code_review) över teamgränser och tydliga underhållare. När ett team behöver en ändring i ett annat teams komponent kan det bidra med ändringen direkt i stället för att skriva ett ärende och vänta i en kö. Det lättar beroenden mellan team utan att upplösa ägarskapet, och sprider kunskap och standarder naturligt över en stor ingenjörspopulation.

## Avvägningar: för- och nackdelar

| Modell för tvärgående funktioner | Fördelar | Nackdelar |
| --- | --- | --- |
| Centraliserad (ett team för alla) | Enhetlighet, djup expertis, tydliga standarder | Flaskhals, köer, förlorat produktsammanhang |
| Federerad (nav-och-ekrar, gillen) | Balanserar enhetlighet och hastighet, delar kunskap | Kräver samordningsdisciplin. Ansvaret kan suddas ut |
| Inbäddad (specialist per team) | Snabb, rik på sammanhang, högt ägarskap | Dubbelarbete, inkonsekvens, svårt att bemanna i stor skala |

| Teamtyp | Bäst för | Risk om den överanvänds |
| --- | --- | --- |
| Strömjusterad | Det mesta av produkt- och tjänsteleverans | Ingen. Den här ska dominera |
| Plattform | Att minska delad kognitiv belastning | Blir en grindvakt i ett elfenbenstorn |
| Stödjande | Att tillfälligt sprida en förmåga | Förvandlas till ett permanent beroende |
| Komplicerat delsystem | Verkligt djupa specialistdomäner | Används som ursäkt för att hamstra vanligt arbete |

Den återkommande avvägningen är autonomi mot enhetlighet. Helt autonoma team rör sig snabbt men glider isär i standarder, verktyg och säkerhetsnivå. Helt centraliserad kontroll håller saker enhetliga men kvävs flödet. God topologidesign hittar skarven: autonomi för strömjusterad leverans, plus tunna centrala standarder och plattformar med upptrampade stigar (välstödda standardverktyg som gör det regelföljande valet till det enkla) för det som verkligen måste vara enhetligt.

## Frågor att diskutera med ditt team

1. **Vilka konkreta signaler talar om för dig att ett teams kognitiva belastning är för hög, innan kvaliteten kollapsar?** "Avgränsa varje team till en domän det kan bemästra" är lätt att säga och svårt att agera på utan belägg, eftersom kognitiv belastning förblir osynlig tills leverans och tillförlitlighet försämras. Titta efter mätbara symptom: antalet orelaterade tjänster eller repositorier ett team äger, hur lång tid introduktion tar, hur många domäner en enskild ingenjör måste växla mellan under en vecka och stigande incidentfrekvens i hörnen av ett teams ansvar. För en stor organisation spelar detta roll eftersom överbelastade team tyst blir flaskhalsar som inget organisationsschema förutsäger. Ta med de här siffrorna till diskussionen, plus teamets egen känsla av vad de kan och inte kan hålla i huvudet. Om signalerna säger överbelastad är åtgärden att avlasta odifferentierat arbete till en plattform eller ett stödjande team, inte att kräva mer heroism.

2. **Är en omorganisation verkligen värd störningen här, eller matar du ett omorganiseringsberoende?** Att dra om gränser för att tillämpa den omvända Conway-manövern är kraftfullt, och varje omorganisation förstör också den stabilitet team behöver för att svetsas samman och nollställer hårt förvärvad domänkunskap. Avvägningarna är den löpande samordningsskatten i nuvarande struktur mot engångskostnaden och moralstödet av att ändra den. I företags- och myndighetsmiljöer gör upphandlingsgränser, konsultteam och föreskrivna funktionsuppdelningar omorganisationer långsammare och dyrare, så ribban bör vara högre. Ta med belägg för beroendedrivna förseningar: hur många initiativ som blockeras i väntan på ett annat team, och hur länge. Omorganisera när väntan är strukturell och stor, och motstå omblandning när smärtan är tillfällig eller skulle vara billigare att lösa med inner source-bidrag och tydligare gränssnitt.

3. **För säkerhet, data och design, vilken händelse utlöser en flytt mellan inbäddat, federerat och centraliserat?** Kapitlets rekommendation är att välja per funktion och per skala, och den svårare disciplinen är att på förhand besluta vilken tillväxt eller risk som får dig att omvärdera valet. En modell som passar femtio ingenjörer kan bli en flaskhals eller en enhetlighetskatastrof vid femhundra, och företag och myndigheter behöver särskilt namnge de standarder en liten central kärna alltid håller. Ta med nuvarande köer och enhetlighetsluckor för varje funktion: ett centralt säkerhetsteam med granskningsköer på flera veckor är en signal att federera, medan inbäddade specialister som producerar oförenliga datamodeller är en signal att lägga till en central standardkärna. Besluta utlösaren nu, till exempel en kölängdströskel eller ett revisionsfynd, så att förändringen blir en planerad utveckling i stället för en krisreaktion. Svaret avgör var du investerar i upptrampade stigar och champions mot ett centralt nav.

4. **Hur vet du om ditt plattformsteam verkligen sänker den kognitiva belastningen eller i det tysta blir en grindvakt?** En plattform finns för att göra det regelföljande, pålitliga valet till det enkla genom självbetjäning, och samma team kan glida mot att påtvinga verktyg, handgranska varje begäran och lägga till den friktion det var tänkt att ta bort. För en stor organisation avgör distinktionen om plattformsinvesteringen betalar sig eller blir en central flaskhals som varje strömjusterat team köar bakom. Avvägningarna är enhetlighet och kontroll å ena sidan mot konsumentens autonomi och flöde å andra. Ta med belägg en konsument skulle känna igen: hur lång tid det tar för ett strömjusterat team att själv skaffa en ny miljö eller pipeline utan att skriva ett ärende, förhållandet mellan självbetjäningsåtgärder och mänskligt förmedlade och plattformsanvändning mätt som team som väljer den i stället för team som tvingas på den. I företags- och myndighetsmiljöer, kräv att plattformen genererar revisions- och regelefterlevnadsbevis automatiskt snarare än genom manuella grindar, för en plattform som uppfyller funktionsuppdelningskrav genom att sätta in en mänsklig granskare har återskapat den flaskhals den finansierades för att lösa upp.

5. **Vilka av era relationer mellan team har lagt sig i permanent samarbete, och vad skulle omvandla var och en till ett rent tjänstegränssnitt eller en omdragen gräns?** Samarbetsläget är tänkt att vara intensivt och tillfälligt, och ett samarbete som aldrig tar slut är oftast en signal att ägarskapet ligger fel eller att gränssnittet mellan två team aldrig gjordes uttryckligt. Det spelar roll i stor skala eftersom onämnt, stående samarbete är där samordningskostnaden gömmer sig: det syns inte i något organisationsschema men beskattar varje ändring de två teamen rör vid. Avvägningarna är upptäcktsvärdet av att stanna nära mot det flöde du vinner genom att göra relationen till ett X-som-en-tjänst-avtal med ett definierat gränssnitt, eller genom att slå ihop ansvaret i ett enda team. Ta med listan över teampar som har samarbetat kontinuerligt i mer än ett kvartal, ändringarna som under de senaste månaderna krävde båda teamen och om ett stabilt gränssnitt mellan dem skulle kunna skrivas ner. I företags- och myndighetssammanhang, där konsultgränser och upphandlingslotter kan frysa en överlämning på plats i åratal, namnge vilka relationer du kan omvandla med ett gränssnitt och inner source-bidrag och vilka som är avtalsmässigt låsta och måste hanteras som uttryckliga beroenden.

6. **När ett stödjande team hjälper ett annat team att bygga en förmåga, hur vet du att det har lyckats och kan dra sig tillbaka i stället för att bli ett permanent beroende?** Stödjande team är tänkta att coacha ett strömjusterat team att bemästra testning, säkerhet eller observerbarhet och sedan gå vidare, och utan ett uttryckligt avslutsvillkor stelnar coachningsrelationen till en stående tjänst som det strömjusterade teamet aldrig tar över. För en stor organisation är det skillnaden mellan att sprida en förmåga över dussintals team och att skapa en ny delad flaskhals som skalar sämre för varje år. Avvägningarna är det djup och den enhetlighet ett specialistteam ger mot den autonomi och det ägarskap från början till slut du försöker bygga in i strömjusterade team. Ta med belägg för förmågeöverföring: om det mottagande teamet nu hanterar arbetet utan att det stödjande teamet är närvarande, hur många team en fast stödjande grupp är åtagen åt samtidigt och hur länge varje insats har pågått efter sin avsedda överlämning. I företags- och myndighetsmiljöer, där en knapp specialistkompetens kan ligga bakom ett enda centralt team eller ett enda avtal, besluta på förhand hur du finansierar förmågeöverföring och champions så att expertisen sprids in i leveransteamen i stället för att förbli inlåst bakom en kö som varje revision och release måste vänta på.

## Sektorsperspektiv

**Startup.** Med en handfull ingenjörer och kort löptid är rätt topologi ett enda strömjusterat team som äger hela produkten, och disciplinen är att vägra skapa silos innan du behöver dem. Motstå att anställa en ensam "DevOps"- eller "QA"-person som blir en grind. Väv in de färdigheterna i det enda teamet som en inbäddad förmåga. Låt Conways lag arbeta för dig genom att hålla organisationen platt, så att arkitekturen förblir lika enkel och föränderlig som teamet.

**Småföretag.** Du kommer inte att bemanna ett särskilt plattforms- eller stödjande team, så köp plattformen: använd hanterade molntjänster, hostade pipelines och färdiga säkerhetsverktyg för att ta odifferentierad kognitiv belastning från dina ett eller två team. Rama in tvärgående frågor som säkerhet och data som något du konfigurerar och förbrukar snarare än en funktion du bygger. Reservera eget ägarskap för det enda komplicerade delsystem som verkligen differentierar dig, och låt leverantörer bära resten.

**Storföretag.** I stor skala är problemet samordningskostnaden över många team, så gör topologin till en uttrycklig, styrd design: en gemensam taxonomi för de fyra teamtyperna, namngivna interaktionssätt, en plattform med upptrampade stigar och inner source för att lätta köer mellan team. Följ beroendedrivna förseningar och teamens kognitiva belastning som portföljmått, och genomför omorganisationer som medvetna utvecklingssteg med hög ribba snarare än som en årlig reflex. En tunn central kärna håller de standarder som måste vara enhetliga, medan strömjusterade team behåller autonomin över leveransen.

**Offentlig sektor.** Upphandlingsregler, konsultgränser och föreskrivna funktionsuppdelningar splittrar ägarskapet, så utforma topologin för att möta de begränsningarna genom verktyg och tydliga gränssnitt snarare än mänskliga överlämningar. Föredra federerade modeller med en liten standardkärna och en plattform som genererar revisions- och regelefterlevnadsbevis automatiskt, så att funktionsuppdelning upprätthålls av pipelines snarare än granskningsköer. Dokumentera teamgränser, interaktionssätt och driftsmodellen öppet, så att strukturen är transparent för revisorer, tillsynsorgan och den allmänhet som finansierar den.

## Exempel

**Startup.** En startup med tio personer har ett enda strömjusterat team som äger hela produkten från början till slut, vilket är precis rätt i dess skala: inga överlämningar, ingen samordningsskatt, alla delar samma sammanhang. Problem uppstår när de anställer en dedikerad "DevOps-person" och en separat "QA-person" och av misstag återskapar funktionella silos, så att varje release nu väntar på två individer. De korrigerar kursen genom att behandla de anställningarna som en inbäddad plattforms- och testförmåga inom det enda teamet, snarare än grindar som arbetet måste passera. I den storleken är den billigaste topologin den som håller alla i ett enda flöde.

**Storföretag.** En stor detaljhandlares kassa var långsam att ändra eftersom frontend-, backend- och uppfyllnadslogik var splittrad över tre funktionsorganiserade team, vilket tvingade varje ändring genom tre backloggar. Med den omvända Conway-manövern omorganiserade de sig i strömjusterade team kring kundresor ("bläddra", "varukorg och kassa", "efter köp"), vart och ett ägde sin del från början till slut, med stöd av ett plattformsteam som tillhandahöll driftsättning och observerbarhet som en tjänst. Kassaändringar som förut tog ett kvartal började levereras på dagar, eftersom samordningen som förut spände över team nu skedde inom ett.

**Offentlig sektor.** En skattemyndighet drev ett centralt säkerhetsteam som granskade varje release, vilket skapade en kö på flera veckor som försenade kritiska rättelser. De gick över till en federerad modell: en liten central säkerhetsfunktion satte standarder och tillhandahöll en "upptrampad stig" av förgodkända, automatiskt skannade pipelines, medan säkerhetschampions inbäddade på deltid i varje leveransteam hanterade de dagliga besluten. Plattformen genererade regelefterlevnadsbevis automatiskt. Föreskrivna krav på funktionsuppdelning uppfylldes fortfarande, men genom verktyg och tydliga gränssnitt snarare än en mänsklig flaskhals, vilket kraftigt minskade ledtiden för release samtidigt som revisionsberedskapen förbättrades.

## Affärsnytta: motiv, ROI och TCO

Du betalar för dålig teamdesign i samordningsöverhead, och den överheaden växer snabbare än linjärt med antalet team som måste synkronisera för en typisk ändring. Varje överlämning är en kö med väntetid, en kontextöverföring som tappar information och en ny chans att missförstå. När en rutinändring kräver att tre team justerar sina färdplaner är den verkliga kostnaden inte summan av deras arbete. Det är den långt större kostnaden för schemaläggning, väntan och omarbete. Dra om gränserna så att de flesta ändringar ryms inom ett teams ägarskap, så försvinner den överheaden helt enkelt.

Införandekostnaden är verklig. Omorganisationer är störande, och att bygga plattformar och inner source-praxis kräver investering i förväg innan utdelningen kommer. Men kostnaden för att inte införa växer över tid. Organisationer som låter strukturen växa fram av en slump hopar överlämningskedjor, delade flaskhalsteam med köer på ett kvartal och arkitekturer som stelnat efter organisationsschemat. För att övertyga ledningen, mät beroendedrivna förseningar: hur många pågående initiativ som blockeras i väntan på ett annat team, och hur länge. Plattforms- och topologiinvesteringar betalar sig vanligen genom att förvandla väntan till flöde, vilket syns som kortare ledtider och högre genomströmning utan att lägga till personal.

## Antimönster och fallgropar

- Att ignorera Conways lag: att designa en arkitektur som organisationsstrukturen inte kan leverera.
- Funktionella silos: separata frontend-, backend-, QA- och driftteam som måste samordnas för varje ändring.
- Flaskhals i delade tjänster: ett centralt team som varje projekt måste köa bakom.
- Plattform som grindvakt: ett plattformsteam som påtvingar i stället för att tjäna och lägger till friktion i stället för att ta bort den.
- Kognitiv överbelastning: team som äger vidsträckta, orelaterade system de inte kan bemästra.
- Permanent "samarbete": två team som ständigt är intrasslade, vilket signalerar en felplacerad gräns.
- Omorganiseringsberoende: ständig omblandning som förstör den stabilitet team behöver för att svetsas samman.

## Mognadsmodell

- **Nivå 1, Initiera.** Team bildas av en slump, bemanning eller äldre hierarki. Ingen namnger teamtyper eller interaktionssätt. Funktionella silos och flaskhalsar i delade tjänster finns överallt och beroenden är dolda tills de blockerar en release.
- **Nivå 2, Utveckla.** Några strömjusterade team finns och ett första plattforms- eller inner source-initiativ dyker upp, men mönstret tillämpas ojämnt: ett fåtal team äger sin del från början till slut medan andra fortfarande köar bakom centrala funktioner, och kognitiv belastning diskuteras anekdotiskt snarare än hanteras.
- **Nivå 3, Standardisera.** De fyra teamtyperna och de tre interaktionssätten är dokumenterade och används medvetet över organisationen. Plattformar och inner source lättar beroenden mellan team. En driftsmodell för säkerhet, data och design är vald och nedskriven, och nya team bildas efter de här standarderna snarare än genom improvisation.
- **Nivå 4, Hantera.** Topologin mäts och styrs mot utgångslägen: team följer kognitiv belastning, beroendedrivna förseningar (initiativ som blockeras i väntan på ett annat team, och hur länge), plattformars självbetjäningsgrad och användning, interaktionssätts varaktighet och leveransflödesmått som ledtid och ändringsfrekvens. Trösklar utlöser åtgärder, till exempel en kölängd som tvingar en funktion att federera eller ett stående samarbete som flaggar en felplacerad gräns, så att besluten vilar på belägg snarare än åsikter.
- **Nivå 5, Orkestrera.** Teamdesignen förbättras kontinuerligt och är integrerad med arkitektur-, produkt- och riskplanering. Organisationen omformar gränser när systemet och verksamheten utvecklas, avslutar stödjande insatser när förmågan har överförts och omfördelar plattformsinvesteringar när kognitiv belastning förskjuts, så att snabbt flöde förblir en adaptiv, stående egenskap snarare än en engångsomorganisation.

## Idéer för diskussion

- För en typisk ändring, hur många team måste samordna sig, och varför?
- Vilka av våra team bär för mycket kognitiv belastning, och vad skulle en plattform kunna avlasta?
- Var kämpar vi mot Conways lag i stället för att dra om gränser?
- Tjänar våra plattformsteam de strömjusterade teamen eller vaktar de dem?
- Bör säkerhet, data och design vara centraliserade, federerade eller inbäddade för oss just nu?
- Vilka "tillfälliga" samarbeten har i det tysta blivit permanenta beroenden?

## Viktigaste punkter

- Organisationsstrukturen avgör arkitektur och leveranshastighet. Utforma den medvetet.
- Använd de fyra teamtyperna, med strömjusterad som standard och de övriga som stöd.
- Tillämpa den omvända Conway-manövern för att göra den önskade arkitekturen till den enkla vägen.
- Hantera kognitiv belastning. Avgränsa varje team till en domän det kan bemästra.
- Begränsa och namnge interaktionssätt mellan team. Behandla kvardröjande beroenden som gränsfel.
- Välj centraliserade, federerade eller inbäddade modeller för tvärgående funktioner per skala, och använd inner source för att lätta köer.

## Referenser och vidare läsning

- Matthew Skelton and Manuel Pais, "Team Topologies: Organising Business and Technology Teams for Fast Flow"
- Melvin Conway, "How Do Committees Invent?" (the origin of Conway's Law)
- Nicole Forsgren, Jez Humble, Gene Kim, "Accelerate"
- Will Larson, "An Elegant Puzzle: Systems of Engineering Management"
- Sam Newman, "Building Microservices" (on aligning services to teams)
- Danese Cooper and Klaas-Jan Stol, "Adopting InnerSource," and the InnerSource Commons patterns
- Frederick Brooks, "The Mythical Man-Month" (communication overhead)
