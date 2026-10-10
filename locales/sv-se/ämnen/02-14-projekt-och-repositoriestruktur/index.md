# 2.14 Projekt- och repositoriestruktur

## Översikt och motivation

Projekt- och repositoriestruktur är den fysiska organisationen av en kodbas: mapparna, filerna och namnkonventionerna som avgör var en given sak bor. Ett *repositorie* (ofta förkortat "repo") är den [versionshanterade](https://en.wikipedia.org/wiki/Version_control) behållare som rymmer ett projekts filer och deras historik. Ett *projekt*, ibland kallat en *lösning* när det grupperar flera relaterade komponenter, är den logiska enhet av programvara du bygger. Struktur är kartan du använder för att hitta, förstå och ändra den programvaran.

I ett litet team kan en person hålla hela layouten i huvudet. I ett stort team, med hundratals eller tusentals ingenjörer, täta byten mellan team och konsulter som kommer och går, tar varje repositorie som är organiserat annorlunda ut en ny kognitiv skatt vid varje läsning, varje granskning och varje introduktion. När du öppnar ett obekant repo bör du kunna gissa var källkoden, testerna, dokumentationen och driftsättningskonfigurationen bor, utan att läsa en manual. När varje repo svarar på de frågorna på samma sätt är rörlighet billig och introduktion snabb. När varje repo är ett snöflingeexemplar blir varje kontextbyte ett litet forskningsprojekt.

I företags- och myndighetsmiljöer är enhetlig struktur också en kontroll- och försäkransfråga. Revisorer, säkerhetsgranskare och långsiktiga underhållare, som ofta arbetar år efter att de ursprungliga författarna har gått, behöver pålitligt kunna hitta specifikationsdokument, licensfiler, säkerhetspolicyer och byggdefinitioner. En förutsägbar layout låter också automatiserade verktyg (skannrar, beroendeanalysverktyg, regelefterlevnadskontroller) fungera på samma sätt över en hel portfölj av system. Det här kapitlet behandlar därför struktur som en konvention du beslutar en gång och tillämpar överallt. Det hänger nära ihop med kodstandarder och stil (kapitel 2.1), versionshantering och källkodshantering (kapitel 2.6) och dokumentation (kapitel 2.7).

## Nyckelprinciper

- Följ *[principen om minsta överraskning](https://en.wikipedia.org/wiki/Principle_of_least_astonishment)*: layouten ska matcha vad en erfaren ingenjör förväntar sig, så att inget behöver memoreras.
- Enhetlighet över repositorier slår lokal klurighet. En tillräckligt enhetlig struktur överallt är värd mer än den perfekta strukturen på ett ställe.
- [README](https://en.wikipedia.org/wiki/README) är ytterdörren. En nykomling bör orientera sig enbart utifrån den.
- Gör strukturen självbeskrivande genom namngivning, så att mappar och filer annonserar sitt syfte.
- Upprätthåll struktur med grundstommar och mallar, inte med viljestyrka och granskningskommentarer.
- Skilj ansvarsområden fysiskt åt: källkod, tester, dokumentation, bygge och driftsättning hör hemma på skilda, förutsägbara platser.
- Organisera beroenden så att de flödar i en riktning, från stabila kärnor mot föränderliga kanter.

## Rekommendationer

### Anta en enhetlig layout på toppnivå

Definiera en standarduppsättning av mappar på toppnivå som varje repositorie använder där det är tillämpligt, och dokumentera vad var och en är till för. En vanlig, leverantörsneutral konvention inkluderar: en källkodsmapp (ofta `src`) för produktionskod, en testmapp (ofta `test` eller `tests`) för automatiserade tester, en `docs`-mapp för dokumentation, en `build`-mapp för byggdefinitioner och utdata, en `deploy`-mapp för driftsättning och *[infrastruktur som kod](https://en.wikipedia.org/wiki/Infrastructure_as_code)* (maskinläsbara definitioner av servrar, nätverk och tjänster, som behandlas i kapitel 8.2), en `scripts`-mapp för automatisering och utvecklarverktyg, en `examples`-mapp för körbara exempel och en `spec`- eller `specification`-mapp för krav- och designspecifikationer. Inte varje repo behöver varje mapp, men där en angelägenhet finns bör den bo på den förväntade platsen med det förväntade namnet.

### Gör README till ingången

Kräv en README-fil i repositoriets rot som den enda, kanoniska startpunkten. Den bör ange vad projektet är, hur man bygger och kör det, hur man kör testerna, var man hittar djupare dokumentation, vem som äger det och hur man bidrar. README är inte hela dokumentationsuppsättningen. Den är indexet som pekar på resten (kapitel 2.7). Behandla en saknad eller inaktuell README som en defekt, för det är det första varje ny ingenjör, revisor eller integratör kommer att läsa.

### Standardisera editor- och konfigurationsfiler

Checka in gemensam editor- och verktygskonfiguration i repositoriet så att varje bidragsgivare får konsekvent beteende automatiskt. En `.editorconfig`-fil (en enkel, editoroberoende fil som definierar regler för blanksteg, indrag och radslut) håller grundläggande formatering enhetlig över olika editorer och operativsystem. Lägg till en ignorerafil för versionshanteringssystemet (så att byggutdata och lokala artefakter aldrig checkas in), tillsammans med de gemensamma formaterings- och linterkonfigurationer som beskrivs i kapitel 2.1. Dessa filer gör repositoriets konventioner aktiva, inte bara dokumenterade.

### Definiera namn- och mappkonventioner

Kom överens om konventioner för namngivning av mappar och filer (skiftläge, avgränsare, singular mot plural och krävda ändelser som de som markerar tester) och tillämpa dem enhetligt. Namn bör avslöja avsikt och matcha det domänvokabulär som används någon annanstans i organisationen. Målet är enkelt: en sökväg bör förmedla mening, så att att läsa ett mapp- eller filnamn talar om vad som finns inuti utan att öppna den.

### Organisera lager och beroenden medvetet

Strukturera kodbasen så att dess arkitektoniska lager syns i mappstrukturen, och så att beroenden flödar i en enda, vettig riktning. Policy på högre nivå bör inte bero på detaljer på låg nivå. Gemensam, stabil kod bör ligga där många moduler kan nå den utan att skapa cykler. När du gör lagerindelningen fysisk, återspeglad i katalogträdet, är det mer sannolikt att ingenjörer respekterar den, och överträdelser är lättare att upptäcka i granskning och i automatiska beroendekontroller.

### Upprätthåll struktur med grundstommar och mallar

Tillhandahåll *[grundstommar](https://en.wikipedia.org/wiki/Scaffold_%28programming%29)*, den automatiska genereringen av ett startprojekt, så att nya repositorier börjar redan korrekta. En *mall* eller *cookiecutter* (ett parametriserat projektskelett som genererar ett färdigt repositorie utifrån svar på några frågor) kodar standardlayouten, README, konfigurationsfilerna och [CI](https://en.wikipedia.org/wiki/Continuous_integration)-uppsättningen på ett ställe. När ingenjörer skapar nya tjänster från en gemensam mall blir enhetlighet standard i stället för en ambition, och förbättringar av mallen flödar till framtida projekt.

### Håll struktur konsekvent över många repositorier i stor skala

Behandla själva layouten som en styrd standard: underhållen centralt som varje annan teknisk standard (kapitel 1.7) och versionshanterad som kod (kapitel 2.6). Publicera den, tillhandahåll mallarna som implementerar den och tillåt avvikelser bara genom en dokumenterad undantagsprocess, så att "standarden" behåller sin betydelse. I portföljskala kommer nästan allt värde av struktur från dess enhetlighet över repositorier, så drift är den främsta risken att hantera.

### Låt struktur informera valet mellan monorepo och flera repon

Relatera struktur till beslutet om repositoriegräns som behandlas i kapitel 2.6. Ett *[monorepo](https://en.wikipedia.org/wiki/Monorepo)* (ett repositorie som rymmer många projekt) behöver en tydlig intern konvention för att skilja projekt och deras gemensamma kod åt, så att det enda trädet förblir navigerbart. Ett *flerrepo*-angreppssätt (många små repositorier, ett per projekt eller tjänst) behöver stark enhetlighet mellan repon, så att varje repo känns välbekant även om det står för sig självt. Hur som helst är en dokumenterad, mallad struktur det som håller navigeringen förutsägbar. Gränsvalet ändrar var du tillämpar konventionen, inte om du behöver en.

## Avvägningar: för- och nackdelar

| Val | Fördelar | Nackdelar |
|---|---|---|
| Strikt standardlayout för hela organisationen | Omedelbar igenkänning. Portabla ingenjörer. Enhetliga verktyg | Ibland dålig passform för ovanliga projekt. Behöver styrning |
| Frihet i layout per team | Lokal optimering. Hög autonomi | Fragmentering. Kostsamma kontextbyten. Inkonsekventa verktyg |
| Grundstommar och mallar | Repon korrekta som standard. Ändringar sprids | Mallunderhåll. Risk för drift från genererade repon |
| Djup, lagerindelad mapphierarki | Uttrycklig struktur. Tydliga gränser | Navigeringsoverhead. Långa sökvägar. Risk för överkonstruktion |
| Platt, grund layout | Lätt att skumma. Lite ceremoni | Dålig åtskillnad. Bryter ihop när projektet växer |

Den dominerande avvägningen är enhetlighet mot autonomi. En enda standardlayout tar bort friktion för de många ingenjörer som rör sig mellan kodbaser, till priset av det enstaka projekt vars behov inte passar formen snyggt. I en stor organisation överväger den kollektiva vinsten av igenkänning nästan alltid den lokala förlusten. Därför är den rekommenderade hållningen ett starkt standardval plus en dokumenterad undantagsväg (kapitel 1.7), snarare än antingen stel enhetlighet eller ohanterad frihet. En sekundär avvägning är djup mot enkelhet: tillräckligt med struktur för att skilja verkliga angelägenheter åt, men inte så mycket att navigering blir en vandring genom tomma mappar.

## Frågor att diskutera med ditt team

1. **När en ingenjör flyttar till ett obekant repo hos oss, hur lång tid tar det tills hen kan hitta testerna, driftsättningskonfigurationen och ägaren?** Det här är den navigeringsskatt som struktur finns för att eliminera, och i portföljskala betalas den tusentals gånger om året i små steg som summerar till allvarlig förlorad ingenjörstid. Poängen med principen om minsta överraskning är att en erfaren ingenjör ska kunna gissa var källkod, tester, dokumentation och driftsättning bor utan att läsa en manual, så det ärliga testet är om den gissningen lyckas över era repon. Ta med ett verkligt tal till mötet: ta tid på er själva när ni orienterar er i två eller tre obekanta interna repositorier, eller hämta introduktionsdata om hur lång tid nyanställda tar på sig att göra en första ändring. Om svaret mäts i dagar av efterforskning snarare än minuter av igenkänning har ni kvantifierat kostnaden för snöflingerepon, och det motiverar engångsinvesteringen i en standardlayout som varje repo delar.

2. **Syns våra arkitektoniska lager i mappträdet, eller gömmer sig beroendecykler i en platt layout?** Struktur handlar om mer än sökbarhet: när du gör lagerindelning fysisk respekterar ingenjörer den och granskare och automatiska beroendekontroller kan upptäcka överträdelser, medan en platt hög låter olämplig koppling och cykler smyga sig in obemärkt tills förändring blir farlig. I ett stort, långlivat system är det här det som håller policy på högre nivå från att i det tysta bero på detaljer på låg nivå, och det är precis den sortens erosion som är billig att förhindra och dyr att lösa upp. Ta med er beroendegraf eller kör en snabb kontroll: finns det cykler, och beror något stabilt på något föränderligt? Svaret bör driva er mot att återspegla lager i kataloger och att lägga till automatiska kontroller av beroenderiktning, så att gränserna är synliga i trädet och upprätthålls i pipelinen snarare än att bara leva i någons mentala modell.

3. **Börjar våra nya repositorier korrekta från en mall, eller förlitar vi oss på en wikisida och goda avsikter?** Struktur som upprätthålls av grundstommar är standard. Struktur som beskrivs i ett dokument driver, eftersom verkligheten följer det som genererar repon, inte det en sida säger att de ska se ut. För en stor eller reglerad organisation är det också en försäkransfråga: när varje repo genereras från en gemensam mall hittar säkerhetsskannrar, beroendeanalysverktyg och revisorer licensen, säkerhetspolicyn, specifikationen och byggdefinitionen på samma ställe varje gång, över leverantörer och över år. Ta med beläggen: hur många av era senaste repon skapades med grundstomme från standardmallen mot sammansattes för hand, och hur långt har de mallade sedan dess drivit? Åtgärden är att göra mallen till det enda enkla sättet att starta ett repo, styra den som en versionshanterad standard med en dokumenterad undantagsväg och upptäcka drift automatiskt, för enhetlighet är där nästan allt värde av struktur bor.

4. **Har vi bestämt om vår standard spänner över ett monorepo eller många separata repositorier, och håller samma konvention faktiskt på båda sidor av den gränsen?** Valet av repositoriegräns ändrar var du tillämpar konventionen, inte om du behöver en, och att få det fel betyder ett enda gigantiskt träd ingen kan navigera eller en spridning av repon som var och en känns främmande. Ett monorepo behöver en tydlig intern konvention för att skilja projekt och deras gemensamma kod åt så att det enda trädet förblir navigerbart, medan ett flerrepo-angreppssätt behöver stark enhetlighet mellan repon så att varje fristående repo ändå känns välbekant. Ta med den nuvarande inventeringen: hur många repon ni har, hur gemensam kod separeras inuti ett monorepo och ett tidtaget test av om en ingenjör kan hitta ett projekt inuti det stora trädet lika snabbt som hen hittar ett i ett fristående repo. För ett stort företag eller ett myndighetsprogram där olika leverantörer levererar separata repositorier, besluta medvetet vilka delar av konventionen som är universella och vilka som är gränsspecifika, eftersom revisorer och plattformsverktyg måste fungera på samma sätt oavsett om koden anländer som ett träd eller femtio.

5. **Vem äger vår strukturstandard, och vad händer egentligen när ett projekt genuint inte passar den?** I portföljskala kommer nästan allt värde av struktur från enhetlighet, så de verkliga riskerna är en ägarlös standard som ruttnar och en undantagsväg så vag att varje team i det tysta uppfinner sin egen layout. Spänningen är mellan stel enhetlighet som inte passar något ovanligt projekt och ohanterad frihet som fragmenterar allt, och det sunda svaret är ett starkt standardval plus en dokumenterad, granskningsbar undantagsprocess styrd av en namngiven ägare och versionshanterad som kod. Ta med beläggen: finns det en enda ansvarig ägare, ett versionshanterat standarddokument med en ändringslogg, ett register över beviljade undantag och varför, och ett antal odokumenterade avvikelser ni kan hitta i det fria. I företags- och myndighetsmiljöer är ett undantag som ingen registrerade är en kontrolllucka, så knyt varje avvikelse till en skriftlig motivering och ett granskningsdatum, och se till att upphandlingsavtal som föreskriver layouten också namnger vem som får godkänna avsteg från den.

6. **Gör vår README och våra incheckade konfigurationsfiler våra konventioner aktiva, eller är de dekorativa?** En README är ytterdörren och den incheckade `.editorconfig`, ignorerafilen och linterkonfigurationen är det som gör konventioner självupprätthållande, men dessa är det första som blir inaktuellt och det sista någon märker tills en revisor eller en nyanställd inte kan få projektet att bygga. Spänningen är mellan en slimmad README som förblir aktuell och en utförlig som driver, och mellan att lita på att människor formaterar kod korrekt och att låta gemensam konfiguration upprätthålla det automatiskt. Ta med ett urval: hämta fem repon och kontrollera hur många READMEs som faktiskt anger vad projektet är, hur man bygger, testar och kör det och vem som äger det, och hur många som bär de gemensamma konfigurationsfilerna i stället för att förlita sig på individuella vanor. För en stor eller reglerad organisation, där integratörer, säkerhetsgranskare och långsiktiga underhållare läser README före allt annat, behandla en saknad eller inaktuell ytterdörr som en defekt med en ägare, och kontrollera förekomsten av konfigurationsfiler automatiskt så att efterlevnad inte beror på välvilja.

## Sektorsperspektiv

**Startup.** Hastighet vinner, så kom överens om en enkel, tillräckligt platt layout för ditt första repo (src, test, docs, scripts, en ifylld README, en `.editorconfig` och ignorerafiler) och spara den som en lätt mall samma eftermiddag. Generera den andra tjänsten från den så att båda repon känns välbekanta och en ny konsult introduceras på timmar snarare än att baklängeskonstruera ett snöflingeexemplar. Stå emot djupa hierarkier och tung styrning du inte behöver ännu. Hela avkastningen här är att två grundare och en konsult delar en karta.

**Småföretag.** Utan plattformsspecialist och med snäv budget, anta den konventionella layout ditt språk eller ramverk redan förutsätter i stället för att uppfinna en, så att färdiga verktyg och varje nyanställd anländer förtränade på den. Köp grundstommar (en ramverksgenerator eller en cookiecutter-mall) i stället för att bygga din egen, och lägg din knappa insats på att hålla en ifylld README aktuell. Den README:n är den billigaste försäkring du har för den dag den enda person som kunde layouten går vidare.

**Storföretag.** Över många team och hundratals repositorier är målet enhetlighet: publicera en versionshanterad strukturstandard, generera varje ny tjänst från gemensamma mallar, upptäck drift automatiskt och tillåt avvikelser bara genom en dokumenterad undantagsprocess. Eftersom varje repo ser likadant ut är en ingenjör som omplaceras till ett nytt team produktiv inom timmar, och säkerhets- och beroendeskannrar över hela portföljen hittar licensen, säkerhetspolicyn och byggdefinitionen på samma ställe varje gång. Budgetera mallunderhållet och driftupptäckten uttryckligen, för den skötseln är det som håller standarden meningsfull i stor skala.

**Offentlig sektor.** Upphandling, transparens och långsiktig ansvarsskyldighet formar layouten, så föreskriv en gemensam struktur i de leveransstandarder som binder varje leverantör. Kräv en `specification`-mapp som länkar kod till godkända krav, en licens- och säkerhetspolicyfil i roten och en `deploy`-mapp som rymmer definitionerna av infrastruktur som kod, så att revisorer hittar regelefterlevnadsartefakter på samma sätt i varje system. Eftersom konsulter från olika leverantörer alla följer en karta kostar underhåll efter att ett avtal tagit slut långt mindre, och allmänheten får ett försvarbart, granskningsbart spår från krav till körande kod.

## Exempel

**Startup.** En startup med tre personer kommer överens om en enkel standardlayout för sitt första repo (src, test, docs, scripts, en ifylld README, en .editorconfig och ignorerafiler) och sparar den som en lätt mall. När de startar sin andra tjänst en månad senare genererar de den från den mallen, så båda repon känns redan välbekanta och den nya konsulten introduceras på en eftermiddag. De står emot djupa mapphierarkier de inte behöver ännu och håller trädet tillräckligt platt för att skumma med en blick. Kostnaden var en eftermiddags uppsättning, och den besparar dem den snöflingespridning som annars skulle ha gjort varje framtida repo till ett litet forskningsprojekt.

**Storföretag.** En multinationell detaljhandlare kör hundratals tjänster i flera språk. Dess plattformsteam publicerar en versionshanterad standard för repositoriestruktur och en uppsättning projektmallar som implementerar den. Varje ny tjänst genereras från en mall, så den anländer med standardmapparna `src`, `test`, `docs`, `deploy` och `scripts`, en ifylld README, en `.editorconfig`, ignorerafiler och en fungerande CI-pipeline. Eftersom varje repositorie ser likadant ut är en ingenjör som omplaceras till ett nytt team produktiv inom timmar, och säkerhets- och beroendeskannrar över hela organisationen körs enhetligt eftersom de alltid hittar filer där de förväntar sig dem.

**Offentlig sektor.** En nationell myndighet som moderniserar äldre system föreskriver en gemensam repositorielayout som en del av sina leveransstandarder för alla leverantörer. Varje repositorie måste innehålla en `specification`-mapp som länkar kod till godkända krav, en dokumenterad README, en licens- och säkerhetspolicyfil i roten och en `deploy`-mapp som rymmer definitionerna av infrastruktur som kod (kapitel 8.2). Eftersom konsulter från olika leverantörer alla följer samma struktur kan myndighetens revisorer hitta regelefterlevnadsartefakter på samma sätt i varje system, och långsiktigt underhåll efter att ett avtal tagit slut kostar långt mindre eftersom inkommande underhållare redan känner kartan.

## Affärsnytta: motiv, ROI och TCO

Kostnaden för att införa en strukturstandard är mest engångs: att enas om layouten, bygga mallarna och dokumentera konventionen. Den återkommande kostnaden är låg, koncentrerad till att underhålla mallarna och styra undantag. Kostnaden för att *inte* ha en standard är återkommande och växande: varje ingenjör som öppnar ett obekant repo betalar en navigeringsskatt, varje introduktion går långsammare och automatiserade verktyg måste konfigureras per repo eftersom ingenting finns där du förväntar dig. Över en stor organisation multipliceras dessa små friktioner till allvarliga förluster av ingenjörstid.

Avkastningen syns som snabbare introduktion, billigare rörlighet mellan team, högre signal från verktyg över hela portföljen och, i reglerade miljöer, lägre revisions- och långsiktiga underhållskostnader, eftersom artefakter alltid går att hitta. Den *totala ägandekostnaden* (TCO, den fulla livstidskostnaden för att bygga, driva och underhålla ett system) sjunker mest i långlivade system, där de underhållare som drar nytta av förutsägbar struktur vanligen inte är de författare som skapade den. För att argumentera inför ledningen, rama in struktur som en billig, hävstångsstark standard som förbättrar utvecklarproduktivitet och revisionsberedskap, och sätt ett tal på dagens kostnad för inkonsekvens med hjälp av data om introduktionstid och den insats som läggs på att leta efter saker i obekanta repositorier.

## Antimönster och fallgropar

- **Snöflingerepositoriet:** varje repo organiserat olika, så att vart och ett måste läras om från grunden.
- **Den saknade eller inaktuella README:** ingen ytterdörr, vilket tvingar nykomlingar att baklängeskonstruera hur projektet byggs och körs.
- **Struktur genom dokument, inte genom mall:** en wikisida beskriver standardlayouten, men inget genererar eller upprätthåller den, så verkligheten driver bort från den.
- **Malldrift:** repositorier genererade från en mall divergerar över tid och förbättringar av mallen når dem aldrig.
- **Överkonstruerad hierarki:** djupa nästlingar av nästan tomma mappar som lägger till ceremoni utan att underlätta navigering.
- **Blandade ansvarsområden:** källkod, tester, byggutdata och hemligheter blandade utan tydlig åtskillnad.
- **Incheckade byggutdata och lokala artefakter:** genererade filer incheckade därför att ignorerareglerna aldrig sattes upp, vilket smutsar ned historik och diffar.
- **Lageröverträdelser dolda av platt struktur:** inga fysiska gränser, så beroendecykler och olämplig koppling smyger sig in obemärkt.

## Mognadsmodell

- **Nivå 1 (Initiera):** Varje repositorie organiseras ad hoc av sina författare, reagerar på vad stunden behöver. Layouter varierar vitt. READMEs saknas eller är opålitliga. Nykomlingar måste guidas genom varje repo för hand.
- **Nivå 2 (Utveckla):** Grundläggande konventioner finns informellt och många repon liknar varandra. Vissa team har en egen startlayout. Men det finns ingen auktoritativ standard, ingen gemensam grundstomme och strukturen driver märkbart från ett team till nästa.
- **Nivå 3 (Standardisera):** En dokumenterad, versionshanterad strukturstandard upprätthålls i hela organisationen. Nya repositorier genereras från gemensamma mallar som bär en standardlayout, README, konfigurationsfiler och CI. Avvikelser går genom en dokumenterad undantagsprocess i stället för att ske i tysthet.
- **Nivå 4 (Hantera):** Efterlevnad av standarden mäts och styrs med data: automatiska kontroller rapporterar hur stor andel av repon som matchar layouten, hur långt mallade repon har drivit, README-fullständighet och överträdelser av beroenderiktning, allt följt mot utgångslägen. Introduktions- och navigeringstider mäts. Undantag loggas och granskas, och malländringar godkänns på grundval av belägg snarare än åsikt.
- **Nivå 5 (Orkestrera):** Struktur förbättras kontinuerligt och är adaptiv: mallförbättringar sprids automatiskt till befintliga repositorier, strukturstyrning är integrerad med säkerhets-, regelefterlevnads- och plattformsverktyg och standarden utvecklas medvetet när språk, arkitekturer och portföljen förskjuts, och håller enhetligheten hög medan organisationen förändras runt den.

## Idéer för diskussion

- Vilka mappar på toppnivå bör vara verkligt universella i er organisation, och vilka bör vara valfria?
- Hur hindrar ni repositorier genererade från en mall från att driva bort från den över tid?
- Var går gränsen mellan en hjälpsam, lagerindelad hierarki och överkonstruerad mappceremoni?
- Hur bör er strukturstandard skilja sig, om alls, mellan ett monorepo och ett flerrepo-angreppssätt?
- Vilken är rätt undantagsprocess för ett projekt vars genuina behov inte passar standardlayouten?
- Hur mycket av er struktur kan kontrolleras automatiskt, och vad förlitar sig fortfarande på mänsklig granskning?
- Vem äger strukturstandarden och dess mallar, och hur föreslås och rullas ändringar ut?

## Viktigaste punkter

- Organisera varje repositorie så att vilken ingenjör som helst kan navigera i vilken kodbas som helst efter förväntan, enligt principen om minsta överraskning.
- Anta en enhetlig layout på toppnivå (källkod, test, docs, bygge, driftsättning, scripts, exempel, specifikation) och gör README till ingången.
- Checka in editor- och verktygskonfiguration (som `.editorconfig`) så att konventioner är aktiva, inte bara nedskrivna.
- Upprätthåll struktur med grundstommar och mallar så att nya repositorier är korrekta som standard.
- I stor skala ligger värdet i enhetlighet: styr standarden, hantera drift och tillåt avvikelser bara genom dokumenterat undantag.

## Referenser och vidare läsning

- Robert C. Martin, *Clean Architecture: A Craftsman's Guide to Software Structure and Design*
- Steve McConnell, *Code Complete: A Practical Handbook of Software Construction*
- Andrew Hunt and David Thomas, *The Pragmatic Programmer*
- Titus Winters, Tom Manshreck, and Hyrum Wright (eds.), *Software Engineering at Google*
- Scott Chacon and Ben Straub, *Pro Git*
- EditorConfig project documentation (as a reference standard for editor configuration)
