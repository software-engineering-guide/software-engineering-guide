# 8.5 Test- och processautomatisering

## Översikt och motivation

Test- och processautomatisering är praktiken att ersätta repetitivt, manuellt ingenjörs- och driftarbete med pålitliga, maskinutförda arbetsflöden. På testsidan betyder det [testautomatisering](https://en.wikipedia.org/wiki/Test_automation): automatiska testsviter som körs kontinuerligt för att verifiera korrekthet, prestanda och säkerhet. På processidan sträcker det sig till det omgivande maskineriet för programvaruleverans och drift: att samla regelefterlevnadsbelägg, köra operativa körböcker, avhjälpa kända problem och upprätthålla styrnings-, säkerhets- och kostnadskontroller. Den enande idén är enkel. Allt som görs upprepat och förutsägbart bör kodifieras, så att det körs konsekvent, snabbt och utan mänskligt slit.

För stora team är automatisering det enda sättet att hindra kvalitet och kontroll från att kollapsa i skala. Manuell testning kan inte hålla jämna steg med hundratals ingenjörer som gör tusentals ändringar. Den blir en flaskhals, och dess täckning blir inkonsekvent och opålitlig. Manuella driftprocedurer lider också. Att starta om en tjänst, rotera en inloggningsuppgift och samla revisionsbelägg blir alla långsamt och felbenäget när trötta människor gör det under press över en stor egendom. Att automatisera det här arbetet gör utfall upprepbara. Det frigör också skickliga ingenjörer att fokusera på de omdömeskrävande problem som genuint behöver mänsklig insikt.

I företags- och myndighetssammanhang är automatisering också nyckeln till att göra regelefterlevnad hållbar. Reglerade organisationer måste kontinuerligt visa att kontroller finns på plats och att belägg samlas in. Att göra detta för hand är dyrt, långsamt och benäget för luckor. Att automatisera insamling av belägg och upprätthållande av kontroller förvandlar regelefterlevnad från en periodisk brandövning till en kontinuerlig, verifierbar egenskap hos systemet. Detta "regelefterlevnad som kod"-tillvägagångssätt både minskar kostnaden och stärker den försäkran som revisorer och tillsynsmyndigheter kräver.

## Nyckelprinciper

- Automatisera arbete som är upprepat, förutsägbart och regelbaserat. Reservera mänsklig insats för omdöme.
- Gör automatiska tester snabba, pålitliga och deterministiska, annars ignoreras de.
- Kör tester parallellt och flytta dem tidigare så att återkopplingen förblir snabb när sviten växer.
- Kodifiera operativa procedurer som [körböcker](https://en.wikipedia.org/wiki/Runbook) som kod så att de är versionerade, testbara och körbara.
- Föredra välintegrerad automatisering framför sköra skript som fästs vid system utifrån.
- Generera regelefterlevnadsbelägg automatiskt som en biprodukt av normala arbetsflöden.
- Behåll en människa i loopen för högriskåtgärder. Automatisera det säkra och rutinmässiga först.

## Rekommendationer

### Bygg snabb, pålitlig, parallell testinfrastruktur

En testsvit är bara värdefull om ingenjörer litar på den och den ger återkoppling snabbt. Investera i testinfrastruktur som kör sviter parallellt över många arbetare, så att den totala klocktiden förblir låg även när antalet tester växer till tusentals. Strukturera sviten som en pyramid: många snabba [enhetstester](https://en.wikipedia.org/wiki/Unit_testing), färre integrationstester och ett litet antal helhetstester. Då anländer det mesta av återkopplingen på sekunder. Eliminera instabila tester skoningslöst. Ett test som fallerar intermittent är värre än inget test, eftersom det lär ingenjörer att ignorera fel. Tillhandahåll efemära testmiljöer på begäran så att integrations- och helhetstester körs mot realistisk, isolerad infrastruktur.

### Automatisera release, regelefterlevnad och insamling av belägg

Utvidga automatiseringen bortom testning in i release- och regelefterlevnadsarbetsflödet. Låt pipelinen automatiskt producera de artefakter revisorer behöver: register över vem som godkände en ändring, vilka tester som kördes och passerade, vad säkerhetsskanningar fann och exakt vilken artefakt som driftsattes. Behandla kontroller som kod, så att obligatoriska kontroller upprätthålls enhetligt och deras resultat loggas. Denna "regelefterlevnad som kod" förvandlar insamling av belägg från en manuell kapplöpning före en revision till ett kontinuerligt, alltid aktuellt register. Den gör också systemets regelefterlevnadsställning observerbar när som helst.

### Anta ChatOps och körböcker som kod

Kodifiera operativa procedurer som körbara körböcker hållna i versionshantering, i stället för som prosadokument som driftar ur tiden. Där en procedur är säker och väl förstådd, koppla in den i automatisering som kan köra den på begäran. ChatOps för in dessa operationer i ett gemensamt chattgränssnitt, så att operatörer utlöser och observerar automatiska åtgärder i ett transparent, samarbetande, loggat samtal. Det gör driften synlig för hela teamet och skapar ett automatiskt register över vad som gjordes. Det sänker också tröskeln för mindre erfarna ingenjörer att köra procedurer säkert, eftersom automatiseringen kodar de korrekta stegen.

### Implementera automatisk avhjälpning försiktigt

För välförstådda, återkommande problem, bygg automatisk avhjälpning som upptäcker ett tillstånd och tillämpar en känd rättelse, som att starta om en fallerad process, skala upp under last, rensa en full disk eller växla över en komponent. Börja med lågrisk-, högtilltroende-avhjälpningar. Kräv mänsklig bekräftelse för allt med betydande sprängradie. Automatisk avhjälpning minskar genomsnittlig tid till återhämtning och eliminerar repetitiv larmtrötthet. Men den måste byggas på solid detektering och inkludera säkerhetsmekanismer, eftersom automatisering som agerar på en falsk signal kan förstärka en incident. Logga varje automatisk åtgärd, så att operatörer behåller full insyn och kan gripa in.

### Placera robotiserad processautomatisering (RPA) rätt

[Robotiserad processautomatisering](https://en.wikipedia.org/wiki/Robotic_process_automation) styr befintliga användargränssnitt och applikationer för att automatisera uppgifter och härmar de klick och tangenttryckningar en människa skulle utföra. RPA har en legitim plats som en brygga för äldre eller tredjepartssystem som saknar API och inte kan integreras på något annat sätt. Använd den pragmatiskt för sådana fall, men känn till dess gränser. Gränssnittsdriven automatisering är i sig skör: den går sönder så fort gränssnittet ändras, och den åtgärdar inte den underliggande bristen på integration. Där ett riktigt API eller en integration finns tillgänglig, föredra den. Behandla RPA som en taktisk nödlösning, inte en strategisk grund, och planera att ersätta den när system moderniseras.

### Automatisera styrnings-, säkerhets- och kostnadskontroller

Koda organisatoriska kontroller som automatiska kontroller som körs kontinuerligt: policy som kod för infrastrukturens skyddsräcken, automatisk säkerhetsskanning i pipelines och automatisk detektering av kostnadsavvikelser och lediga resurser. Att automatisera styrning gör kontroller enhetliga och omöjliga att kringgå, och det skalar till en volym av förändring som manuell granskning aldrig kunde täcka. Samma tillvägagångssätt som upprätthåller en säkerhetspolicy kan flagga en skenande molnräkning eller en saknad obligatorisk tagg. Styrning skiftar från en periodisk manuell revision till ett kontinuerligt automatiskt skyddsräcke.

## Avvägningar: för- och nackdelar

| Val | Fördelar | Nackdelar | Bäst passform |
|---|---|---|---|
| Bred automatisk testning | Snabb, konsekvent återkoppling. Möjliggör förändring | Bygg- och underhållskostnad. Risk för instabilitet | Alla team i skala |
| Regelefterlevnad som kod | Kontinuerliga, revisionsklara belägg | Ingenjörsinsats i förväg för att kodifiera kontroller | Reglerade organisationer |
| Körböcker som kod + ChatOps | Upprepbar, synlig, loggad drift | Insats för att kodifiera och underhålla | Team med verklig driftbelastning |
| Automatisk avhjälpning | Snabbare återhämtning. Mindre slit | Risk om detekteringen är fel | Välförstådda återkommande problem |
| RPA (gränssnittsautomatisering) | Bryggar system utan API | Skör. Maskerar integrationsluckor | Äldre system som nödlösning |
| Automatisk styrning | Enhetliga, ofrånkomliga kontroller | Insats för att skriva och justera policy | Stora, styrda egendomar |

Den centrala avvägningen är investering i förväg mot löpande slit och risk. Automatisering kostar alltid insats att bygga och underhålla. Dåligt byggd automatisering, vare sig instabila tester, sköra RPA eller avhjälpning utlöst av dåliga signaler, kan vara värre än ingen, eftersom den urholkar förtroende eller förstärker fel. Disciplinen är trefaldig: automatisera det genuint upprepbara och pålitliga, investera i att göra den automatiseringen pålitlig och behåll människor i loopen där omdöme eller hög risk kräver det. Väl gjort betalar automatisering sig många gånger om. Vårdslöst gjord blir den en skuld i sig.

## Frågor att diskutera med ditt team

1. **Körs era integrations- och helhetstester mot realistiska, efemära miljöer, eller mot en delad staginglåda alla slåss om?** Isolerade miljöer på begäran per pull request låter integrations- och helhetstester utöva realistisk infrastruktur utan att team blockerar varandra eller förorenar delat tillstånd. En enda delad stagingmiljö blir en flaskhals och en källa till instabila, ordningsberoende fel när fler team hopar sig. Avgör om ni kan starta efemära miljöer, vad de kostar och vilka tester som genuint behöver dem mot en snabb ersättning i minnet. Ta med data: hur ofta staging är omstridd, hur många fel som kan spåras till störning i delad miljö och nuvarande klocktid för integrationsnivån. Svaret formar både er testtillförlitlighet och hur snabbt pyramidens övre lager ger återkoppling.

2. **Är operativa procedurer kodifierade som körböcker som kod och framlyfta genom ChatOps, eller bor de fortfarande som prosa som driftar ur tiden?** Kodifierade, versionshanterade körböcker är testbara och körbara, och att köra dem genom ett gemensamt chattgränssnitt gör varje åtgärd synlig och automatiskt loggad. Det sänker tröskeln för en mindre erfaren jourhavande ingenjör att agera säkert, eftersom automatiseringen kodar de korrekta stegen i stället för att förlita sig på tyst kunskap. Avgör vilka procedurer som är säkra och väl förstådda nog att kopplas in först och hur ni håller människan i stånd att gripa in. För en stor egendom fungerar denna transparens även som ett revisionsregister över vem som gjorde vad och när. Ta med era nuvarande körböcker, notera vilka som är inaktuella och identifiera de två eller tre mest körda procedurerna att kodifiera först.

3. **Vilka säkerhetsskanningar och policykontroller blockerar en sammanslagning i er pipeline, och vilka varnar bara?** Automatisk styrning är värd att bygga bara om kontrollerna är ofrånkomliga, eftersom en kontroll som bara varnar ignoreras under tidspress precis som en wikipolicy. Avgör, kontroll för kontroll, vad som blockerar och vad som varnar: en kritisk sårbarhet eller en saknad krypteringstagg blockerar sannolikt, medan ett stilfynd av lägre allvarlighetsgrad kanske varnar. I skala är det så ni upprätthåller säkerhets- och kostnadsskyddsräcken enhetligt över en volym av förändring ingen manuell granskning kunde täcka. Ta med er nuvarande kontrollinventering och markera varje som blockerande eller rådgivande och diskutera sedan andelen falska positiva, eftersom en bullrig blockerande kontroll lär människor att kräva undantag. Gränsen mellan blockera och varna är där er styrning antingen har tänder eller inte.

4. **Vilka automatiska avhjälpningar är vi villiga att låta agera utan att en människa först bekräftar, och vad är sprängradien om detekteringen är fel?** Automatisk avhjälpning skär återhämtningstid och larmtrötthet, men en rättelse utlöst av en falsk signal kan förvandla ett mindre hack till ett fullt avbrott, så beslutet om vad som körs obevakat är ett riskbeslut, inte en bekvämlighet. Väg de konkurrerande dragen: obevakad åtgärd är snabbast men riskfylldast, medan bekräftelse med människa i loopen är säkrare men återinför den fördröjning och det slit ni ville ta bort. Ta med kandidatavhjälpningarna rangordnade efter frekvens och efter värsta tänkbara sprängradie, den historiska andelen falska positiva för detekteringen bakom var och en och om varje åtgärd är loggad och reversibel. För en stor företags- eller myndighetsegendom, lägg till en formell ändringsbefogenhet och återställningsplan för allt som rör produktionsdata eller medborgarvända tjänster, eftersom en automatisk avhjälpning som inte kan granskas eller ångras är en som en tillsynsmyndighet kommer att tvinga er att stänga av.

5. **Hur finansierar och tilldelar vi ägarskap för att underhålla vår automatisering så att den inte förfaller till en skuld?** Tester, körböcker, policykontroller och RPA-botar ruttnar alla när systemen runt dem förändras, och försummad automatisering är värre än ingen: en inaktuell körbok ger falsk tillförsikt i en kris och en trasig RPA-bot tappar tyst arbete. Spänningen är att underhåll konkurrerar med funktionsarbete om samma ingenjörer, och det är osynligt tills något går sönder, så det är det första som skärs bort under tidspress. Ta med den nuvarande inventeringen av automatiseringstillgångar, kön av instabila tester och trasiga botar och en ärlig uppskattning av de ingenjörstimmar som redan går åt till underhåll mot vad som är budgeterat. I ett företags- eller myndighetssammanhang, namnge den ansvariga ägaren för varje kritisk automatisering och finansiera dess underhåll som en uttrycklig budgetpost, eftersom revisorer och incidentgranskningar kommer att fråga vem som var ansvarig när en ounderhållen kontroll tyst fallerade.

6. **För varje äldre system vi automatiserar med RPA, vad är den konkreta planen och utlösaren för att avveckla den RPA till förmån för en riktig integration?** RPA är en legitim brygga för system som saknar API, men en brygga utan utgångsplan hårdnar i tysthet till permanent, skör infrastruktur som går sönder vid varje gränssnittsändring och befäster just den integrationslucka den var tänkt att överbrygga. Avvägningen är verklig: RPA levererar värde snabbt och billigt nu, medan en riktig API-integration kostar mer i förväg men är varaktig, så disciplinen är att behandla RPA som ett daterat lån, inte ett köp. Ta med listan över RPA-botar i produktion, de system var och en beror på, hur ofta var och en går sönder och om en moderniserings- eller integrationsinsats faktiskt är finansierad och schemalagd för det underliggande systemet. För företags- och myndighetsegendomar som bär årtionden gamla kärnapplikationer, knyt varje RPA-bot till en namngiven moderniseringsmilstolpe, eftersom RPA som i tysthet blivit kritisk utan avvecklingsdatum är teknisk skuld som förstärks varje år det gränssnitt den skrapar fortsätter ändras.

## Sektorsperspektiv

**Startup.** Med två eller tre ingenjörer och ingen tid att bygga infrastruktur, behåll en liten, snabb testpyramid som körs på ett par minuter vid varje ändring och behandla varje instabilt test som en verklig bugg att rätta eller radera samma vecka. Hoppa över tungt regelefterlevnadsverktyg och policy som kod du ännu inte behöver, och kodifiera bara dina två eller tre mest körda operativa rättelser som enkla skript utlösta från chatt. Automatisera det som tar bort dagligt slit och stå emot att bygga styrningsmaskineri innan du har ett styrningsproblem.

**Småföretag.** Utan dedikerad test- eller plattformsspecialist, lita på automatisering inbakad i verktyg du redan betalar för: CI-tjänstens inbyggda testkörare, dess skanningstillägg och hanterade miljöer snarare än ett skräddarsytt bygge av testinfrastruktur. Ramma in valet köpa-mot-bygga kring underhåll du realistiskt kan upprätthålla, eftersom en klurig skräddarsydd pipeline ingen kan underhålla är ett sämre utfall än en enklare hostad. Använd RPA sparsamt och bara där ett leverantörsverktyg bryggar ett system du inte kan integrera på något annat sätt.

**Storföretag.** Över många team är målet enhetliga, ofrånkomliga kontroller i en skala manuell granskning inte kan täcka: gemensam parallell testinfrastruktur med efemära miljöer, skyddsräcken som policy som kod och regelefterlevnadsbelägg genererade automatiskt från varje pipelinekörning. Standardisera gränssnitten så att team återanvänder avhjälpnings- och körboksverktyg i stället för att var och en uppfinner sköra skript på nytt och hantera automatisering som en ägd, finansierad portfölj med tydliga underhållsbudgetar. Se upp så att en kontroll som bara varnar i ett team inte behandlas som blockerande i ett annat, eftersom inkonsekvent upprätthållande undergräver den försäkran ni betalar för.

**Offentlig sektor.** Upphandlingsregler, transparensskyldigheter och mandat om kontinuerlig övervakning gör regelefterlevnad som kod nästan nödvändig: varje pipelinekörning bör registrera de kontroller som kontrollerats, de skanningar som utförts och de godkännanden som beviljats som manipuleringssäkra, revisionsklara belägg. Föredra öppen, portabel automatisering framför proprietär inlåsning så att ett framtida avtal kan flytta till en annan leverantör och behåll en människa ansvarig för varje avhjälpning som rör medborgarvända tjänster. Där ett årtionden gammalt system tvingar fram RPA, dokumentera det som en medveten, tillfällig brygga med en publik moderniseringsplan och håll styrningskontroller till den påbjudna säkerhetsbasen vid varje ändring.

## Exempel

**Startup.** Ett startup på sju personer håller en slimmad testpyramid av mestadels snabba enhetstester plus några integrationstester, alla körda parallellt så att hela sviten är klar på under tre minuter vid varje pull request. När ett test börjar fladdra behandlar de det som en verklig bugg och rättar eller raderar det samma vecka, eftersom ett enda ignorerat rött bygge i ett så litet team skulle urholka förtroendet för hela sviten. De kodifierar också sina två vanligaste operativa rättelser, att starta om en fastnad arbetare och rensa en full disk, som små skript utlösta från Slack, så att den som är jourhavande kan köra dem säkert utan att larma den enda ingenjör som skrev dem.

**Storföretag.** Ett stort e-handelsföretag kör en testsvit på tiotusentals tester, parallelliserad över en flotta av arbetare så att hela sviten är klar på minuter. Efemära miljöer startas per pull request för realistisk integrationstestning. Driften går genom ChatOps: jourhavande ingenjörer utlöser kodifierade körböcker från chatt, och vanliga fel som en överbelastad tjänst avhjälps automatiskt, med åtgärden loggad för granskning. Pipelinen samlar säkerhetsskannings- och godkännandebelägg automatiskt, så den årliga revisionen bygger på ett alltid aktuellt register snarare än en manuell jakt på belägg.

**Offentlig sektor.** En offentlig myndighet underkastad strikta krav på kontinuerlig övervakning implementerar regelefterlevnad som kod. Varje pipelinekörning registrerar de kontroller som kontrollerats, de skanningar som utförts och de godkännanden som beviljats och producerar manipuleringssäkra belägg som tillfredsställer revisorer på begäran. Eftersom ett av dess kärnsystem är en årtionden gammal applikation utan API använder myndigheten RPA som en medveten brygga för att automatisera datainmatning i det medan en moderniseringsinsats pågår, med en uttrycklig plan att avveckla RPA när en riktig integration finns. Automatiska styrningskontroller upprätthåller den påbjudna säkerhetsbasen vid varje infrastrukturändring.

## Affärsnytta: motiv, ROI och TCO

Avkastningen på test- och processautomatisering syns som återvunnen ingenjörstid, snabbare och säkrare leverans, snabbare incidentåterhämtning och dramatiskt lägre regelefterlevnadskostnad. Automatisk testning möjliggör den snabba, trygga förändring som ligger under leveransprestation. Automatisk drift och avhjälpning skär det slit och de driftstopp som tär på team och budgetar. Regelefterlevnad som kod kan förvandla en revision från veckor av manuell förberedelse till en rutinfråga, en besparing som är både finansiell och anseendemässig.

TCO-jämförelsen väger den verkliga, löpande kostnaden för att bygga och underhålla automatisering mot kostnaden för att inte automatisera. Manuell testning och drift kostar inte bara de timmar som läggs. De kostar också de defekter som slipper igenom, de incidenter som drar ut, de revisioner som förbrukar specialistpersonal och utbrändheten hos ingenjörer som gör repetitivt slit. För ledningen är argumentet enkelt: automatisering omvandlar återkommande driftkostnad och risk till en engångs-plus-underhållsinvestering som skalar, och den gör kvalitet och regelefterlevnad kontinuerliga snarare än episodiska. En brasklapp är värd att säga rakt ut. Automatisering måste underhållas och litas på. Ofinansierad, försummad automatisering förfaller till en skuld.

## Antimönster och fallgropar

- **Tolererade instabila tester.** Intermittenta fel förstör förtroende och lär ingenjörer att ignorera röda resultat.
- **Att automatisera en trasig process.** Att automatisera ett dåligt arbetsflöde får bara röran att ske fortare. Rätta processen först.
- **RPA som strategi.** Att förlita sig på skör gränssnittsautomatisering som permanent lösning maskerar och befäster integrationsluckor.
- **Avhjälpning utan solid detektering.** Automatiska rättelser utlösta av dåliga signaler kan förstärka en incident.
- **Körböcker som inaktuell prosa.** Procedurer som bor i föråldrade dokument ger falsk tillförsikt i en kris.
- **Regelefterlevnadsbelägg insamlade manuellt.** Periodiska manuella jakter på belägg är kostsamma och lämnar luckor mellan revisioner.
- **Ingen människa i loopen för högriskåtgärder.** Full automatisering av farliga operationer tar bort det omdöme som förhindrar katastrofer.

## Mognadsmodell

**Nivå 1, Initiera.** Testning och drift är till stor del manuella och reaktiva. Täckning är ad hoc, procedurer bor i människors huvuden eller inaktuella dokument, avhjälpning sker för hand under incidenter och regelefterlevnadsbelägg sätts ihop i en kapplöpning före varje revision.

**Nivå 2, Utveckla.** Automatiska tester finns men är långsamma, instabila eller körs inkonsekvent, och praxis varierar kraftigt mellan team. Vissa operativa skript och körböcker finns i fickor, men avhjälpning är fortfarande manuell och styrning upprätthålls genom periodisk granskning snarare än kontinuerliga kontroller.

**Nivå 3, Standardisera.** Snabb, parallell, pålitlig testinfrastruktur är den dokumenterade standarden i hela organisationen. Körböcker som kod och ChatOps är i allmänt bruk, regelefterlevnadsbelägg genereras automatiskt från pipelinekörningar och styrningskontroller körs som upprätthållna automatiska kontroller tillämpade konsekvent över team.

**Nivå 4, Hantera.** Själva automatiseringen mäts och styrs mot utgångslägen. Ni följer andel instabila tester, svitens klocktid, genomsnittlig tid till återhämtning för automatiskt avhjälpta incidenter, andelen kontroller med automatiska belägg och andelen falska positiva på blockerande kontroller, och ni håller varje mått till ett överenskommet mål. Avhjälpnings- och täckningsbeslut drivs av denna data, och varje automatisk åtgärd loggas så att trender och regressioner är synliga snarare än gissade.

**Nivå 5, Orkestrera.** Automatisering förbättras kontinuerligt och är integrerad i hela organisationen. Automatisk avhjälpning hanterar rutinincidenter med beprövade säkerhetsmekanismer, regelefterlevnad är kontinuerlig och alltid revisionsklar och test-, drift- och styrningsverktygskedjorna anpassas när system förändras, med RPA-bryggor som aktivt avvecklas när integrationer mognar. Människor fokuserar på omdöme medan maskiner hanterar det upprepbara, och hela systemet balanserar om på belägg.

## Idéer för diskussion

- Vilka operativa procedurer är säkra att automatisera fullt ut, och vilka måste behålla en människa i loopen?
- Hur håller ni en stor testsvit snabb och fri från instabilitet när den växer?
- Var är RPA en motiverad brygga för era äldre system, och vad är planen för att avveckla den?
- Vilka kontroller kunde ni omvandla från manuell revision till kontinuerlig regelefterlevnad som kod först?
- Hur bygger ni förtroende för automatisk avhjälpning utan att riskera förstärkta incidenter?
- Hur finansierar ni det löpande underhåll automatisering kräver så att den inte förfaller till en skuld?

## Viktigaste punkter

- Automatisera det upprepade, förutsägbara och regelbaserade. Reservera mänsklig insats för omdöme och högriskbeslut.
- Gör automatiska tester snabba, parallella och pålitliga och eliminera instabilitet skoningslöst.
- Kodifiera drift som körböcker som kod och lyft fram dem genom ChatOps för synlighet och register.
- Generera regelefterlevnadsbelägg automatiskt så att revisioner bygger på ett kontinuerligt, aktuellt register.
- Använd RPA bara som en medveten, tillfällig brygga för system utan API och planera dess avveckling.
- Upprätthåll styrnings-, säkerhets- och kostnadskontroller som kontinuerliga automatiska kontroller, med människor som övervakar de riskfyllda åtgärderna.

## Referenser och vidare läsning

- Lisa Crispin and Janet Gregory, *Agile Testing: A Practical Guide for Testers and Agile Teams*.
- Jez Humble and David Farley, *Continuous Delivery*.
- Betsy Beyer, Chris Jones, Jennifer Petoff, and Niall Richard Murphy (eds.), *Site Reliability Engineering* (see the chapter on eliminating toil).
- Gene Kim, Jez Humble, Patrick Debois, and John Willis, *The DevOps Handbook*.
- Nicole Forsgren, Jez Humble, and Gene Kim, *Accelerate*.
- NIST Special Publication 800-53 and 800-137 (continuous monitoring).
- Open Policy Agent documentation (policy as code).
