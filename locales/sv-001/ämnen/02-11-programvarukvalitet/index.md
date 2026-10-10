# 2.11 Programvarukvalitet

## Översikt och motivation

[Programvarukvalitet](https://en.wikipedia.org/wiki/Software_quality) är hur väl ett system uppfyller uttalade behov och rimliga förväntningar. Det betyder mer än om det fungerar: det betyder om systemet är pålitligt, säkert, underhållbart, användbart, presterande och lämpat för sitt syfte över tid. Kvalitet är bredare än testning. Testning (kapitel 2.4) är en aktivitet som blottlägger defekter. Kvalitet är hela disciplinen att bygga rätt sak väl, och att veta, med belägg, att du har gjort det. Ett system kan klara varje test och ändå vara av låg kvalitet om det är ounderhållbart, otillgängligt eller dåligt anpassat till vad användare faktiskt behöver.

I ett stort team kan kvalitet inte bo i en persons huvud eller ett teams vanor. Hundratals ingenjörer, flera produkter och långlivade system behöver en gemensam definition av kvalitet, uttryckliga processer för att säkra den och mått som talar om för dig om den blir bättre eller sämre. Utan det blir "kvalitet" en vag ambition som förlorar varje argument mot en deadline, och defekter hopar sig tills förändring blir långsam och riskfylld.

I företags- och myndighetsmiljöer stiger insatserna ytterligare. Reglerade, säkerhetskritiska och medborgarvända system måste visa kvalitet, inte bara hävda den: dokumenterade processer, spårbara belägg och oberoende verifiering är ofta obligatoriska. Dålig kvalitet bär direkt ekonomisk, rättslig och anseendemässig kostnad, och i vissa domäner utsätter den människor för fara. En medveten kvalitetsdisciplin, byggd av modeller, processer, mätning och kultur, är det som förvandlar kvalitet från en olycka till ett hanterat utfall.

## Nyckelprinciper

- Kvalitet är lämplighet för syftet plus överensstämmelse med krav. Definiera båda uttryckligen.
- Kvalitet byggs in, den testas inte in. Verifiering hittar defekter, men förebyggande undviker dem.
- Skilj [kvalitetssäkring](https://en.wikipedia.org/wiki/Quality_assurance) (är våra processer sunda?) från [kvalitetskontroll](https://en.wikipedia.org/wiki/Quality_control) (är den här produkten bra?).
- Verifiering frågar "byggde vi det rätt?". Validering frågar "byggde vi rätt sak?"
- Mät kvalitet med en liten uppsättning meningsfulla mått. Behandla mått som signaler, inte mål.
- Kostnaden för en defekt stiger ju senare den hittas, så flytta kvalitetsaktiviteter tidigare.
- Kvalitet är en egenskap hos hela organisationen och dess kultur, inte en grind i slutet.

## Rekommendationer

### Anta en gemensam kvalitetsmodell som ISO/IEC 25010

Ge din organisation ett gemensamt ordförråd för kvalitet genom att anta en erkänd modell för produktkvalitet. [ISO/IEC 25010](https://en.wikipedia.org/wiki/ISO/IEC_25010) definierar egenskaper som funktionell lämplighet, prestandaeffektivitet, kompatibilitet, användbarhet, tillförlitlighet, säkerhet, underhållbarhet och portabilitet. Använd den för att göra kvalitet konkret: för varje system, besluta vilka egenskaper som spelar störst roll och vad "tillräckligt bra" betyder för var och en. Dessa produktkvalitetsegenskaper är samma **kvalitetsegenskaper** som driver arkitekturen (kapitel 3.1). Kvalitet och arkitektur är två vyer av en angelägenhet, så låt dem dela en lista över prioriteringar snarare än två konkurrerande.

### Skilj kvalitetssäkring från kvalitetskontroll

Behandla kvalitetssäkring (QA) och kvalitetskontroll (QC) som skilda men kompletterande aktiviteter. QA är processorienterad och förebyggande: den förbättrar sättet arbete utförs på, genom standarder, granskningar, definitioner av färdigt och utbildning, så att defekter är mindre sannolika att dyka upp från första början. QC är produktorienterad och upptäckande: den inspekterar faktiska arbetsprodukter, som testning, [kodgranskning](https://en.wikipedia.org/wiki/Code_review) och revisioner, för att fånga defekter som verkligen kom in. En mogen organisation investerar i båda, men lutar åt QA, eftersom att förebygga defekter är billigare än att hitta och åtgärda dem.

### Kör uttryckliga processer för programvarukvalitetshantering

Gör kvalitet till en hanterad process, inte ett tyst hopp. För betydande arbete, skriv en kvalitetsplan som anger de önskade kvalitetsegenskaperna, säkrings- och kontrollaktiviteterna, acceptanskriterierna och vem som är ansvarig. Väv in den i praxis du redan har: kodgranskning (kapitel 2.5) som både en kontroll och ett sätt att dela kunskap, teststrategi (kapitel 2.4) som det automatiserade skyddsnätet och [statisk analys](https://en.wikipedia.org/wiki/Static_program_analysis) som kontinuerlig inspektion. Granska kvalitetsdata regelbundet och agera på trender i stället för att bara reagera på incidenter.

### Praktisera verifiering och validering som skilda discipliner

Verifiering bekräftar att arbetsprodukter uppfyller sina specifikationer, så att rätt indata till varje steg ger rätt utdata, genom granskningar, statisk analys och testning mot krav. Validering bekräftar att det färdiga systemet faktiskt möter användarbehov och sitt avsedda bruk, genom användartestning, acceptanstestning, pilotprojekt och återkoppling från fältet. Du behöver båda. Ett system kan vara korrekt mot en felaktig specifikation (verifierat men inte giltigt), eller det kan möta ett verkligt behov och ändå innehålla defekter (giltigt men inte verifierat). I reglerade miljöer kan oberoende [verifiering och validering](https://en.wikipedia.org/wiki/Verification_and_validation) (IV&V) av en part skild från utvecklarna krävas.

### Mät kvalitet med meningsfulla mått

Välj en liten uppsättning mått som speglar kvalitetsutfall och deras drivkrafter, och bevaka dem över tid. Användbara mått inkluderar defekttäthet, andel undkomna defekter (defekter funna i produktion mot före release), genomsnittlig tid att upptäcka och åtgärda, andel misslyckade ändringar, kodhälsosignaler som komplexitet och duplicering samt valideringssignaler som användarrapporterade problem och tillgänglighetsöverensstämmelse. Håll dig borta från fåfängemått och mått som går att manipulera: ett mått som blir ett mål slutar mäta verkligheten. Para talen med kvalitativa signaler från granskningar och användarrespons.

### Karakterisera och hantera defekter systematiskt

Behandla defekter som data, inte bara bränder att släcka. Klassificera dem efter allvarlighetsgrad, typ och grundorsak. Följ dem från upptäckt till lösning. Leta efter mönster så att du kan förebygga återfall. Använd tekniker som [grundorsaksanalys](https://en.wikipedia.org/wiki/Root_cause_analysis) och defektkategorisering för att skilja engångsmisstag från systematiska svagheter. Mata tillbaka det du lär dig till QA, genom uppdaterade standarder, tillagda tester och förbättrade granskningar, så att samma klass av defekt inte återvänder. En defekt som åtgärdats utan att orsaken förståtts är en defekt du har bjudit tillbaka.

### Hantera kvalitetens kostnad medvetet

Förstå kvalitetsekonomi genom de klassiska kategorierna: förebyggandekostnader (utbildning, standarder, god design, verktyg), bedömningskostnader (granskningar, testning, revisioner) och felkostnader (internt omarbete före release, plus externa fel funna av användare, som kostar långt mer). Flytta din investering mot förebyggande och tidig bedömning, eftersom varje krona där undviker många kronor av felkostnad senare. Gör dessa kostnader synliga så att "vi har inte tid för kvalitet" ses för vad det är: ett val att spendera mer på fel i stället.

### Bygg en kvalitetskultur

Gör kvalitet till allas ansvar, ägt av teamen som bygger programvaran, snarare än överlämnat till en efterföljande QA-avdelning som inspekterar den i slutet. Ledare bör belöna kvalitetsutfall, göra det tryggt att rapportera defekter och nästan-olyckor och behandla kvalitetsdata som ett lärverktyg snarare än en käpp. Ett skuldfritt förhållningssätt till defekter för problem fram i ljuset tidigt. Ett skuldbelägande döljer dem tills de är dyra.

## Avvägningar: för- och nackdelar

| Praxis / val | Fördelar | Nackdelar |
|---|---|---|
| Formell kvalitetsmodell (ISO 25010) | Gemensamt ordförråd. Uttryckliga prioriteringar | Overhead om den tillämpas dogmatiskt |
| Tung kvalitetssäkring (förebyggande) | Färre defekter. Lägre totalkostnad | Investering i förväg. Långsammare att visa utdelning |
| Tung kvalitetskontroll (inspektion) | Fångar defekter som slinker igenom | Dyr. Hittar defekter sent |
| Oberoende V&V | Hög försäkran. Objektiv | Kostsam. Långsammare. Kan kännas konfrontativ |
| Rika kvalitetsmått | Synlighet. Tidig varning | Risk för manipulation. Mätoverhead |
| Dedikerat QA-team | Fokus och expertis | Kan avlasta ansvar från utvecklare |
| Kvalitet ägd av teamen | Ägarskap. Snabb återkoppling | Kräver disciplin och skicklighet överallt |

Den centrala avvägningen är investering mot försäkran, formad av tidpunkt. Förebyggande kostar pengar nu för att undvika större felkostnader senare. Den ekonomiskt rätta kvalitetsnivån är därför inte maximum, utan punkten där marginalkostnaden för mer försäkran motsvarar felkostnaden den undviker. Den punkten ligger högt för säkerhetskritiska system och lägre för lågriskiga interna verktyg. Den andra återkommande spänningen är ägarskap. Centrala QA-grupper bygger expertis men kan låta utvecklare avlasta ansvar. Teamägd kvalitet bygger ägarskap men kräver skicklighet och disciplin överallt.

## Frågor att diskutera med ditt team

1. **När samma klass av defekt dyker upp två gånger, kör vi grundorsaksanalys, eller åtgärdar vi den bara igen?** En defekt som åtgärdats utan att orsaken förståtts är en defekt ni har bjudit tillbaka, och i ett stort team kan samma grundorsak dyka upp över många tjänster innan någon kopplar ihop prickarna. Att behandla defekter som data (klassificerade efter allvarlighetsgrad, typ och orsak, och sedan utvunna för mönster) är det som skiljer ett team som blir stadigt mer pålitligt från ett som förblir upptaget med att åtgärda samma misstag om och om igen. Ta med er defektregistrering till mötet och leta efter återkommande signaturer: hur många nyliga incidenter delar en orsak ni aldrig åtgärdade systematiskt? Svaret bör mata förebyggande, så att en återkommande orsak driver en uppdaterad standard, en ny gemensam hjälpfunktion, ett tillagt test eller en bättre granskningschecklista, för det är så en rättelse på ett ställe hindrar hela klassen från att återvända.

2. **Är det tryggt i vårt team att rapportera en defekt eller en nästan-olycka, och vad händer med personen som lyfter en?** Kvalitet är en egenskap hos kulturen, och ett skuldfritt förhållningssätt för problem fram i ljuset tidigt medan ett skuldbelägande döljer dem tills de är dyra, vilket i ett reglerat eller medborgarvänt system kan betyda ett offentligt misslyckande eller ett vite. Det här spelar störst roll i stor skala, där ingenjören närmast en risk ofta är junior och incitamentet att tiga är starkt. Ta med ärliga signaler: loggas och diskuteras nästan-olyckor, eller försvinner de? Namnger efterhandsgranskningar orsaker eller namnger de personer? Åtgärden är att göra kvalitetsdata till ett lärverktyg snarare än en käpp, belöna dem som lyfter problem och köra skuldfria efterhandsgranskningar, för ni kan inte förebygga det ert team är rädda att rapportera.

3. **Kan validering faktiskt stoppa en release, och vem har den befogenheten när en deadline närmar sig?** Verifiering (byggde vi det rätt?) och validering (byggde vi rätt sak?) är skilda discipliner, och validering har bara tänder om en misslyckad tillgänglighetskontroll, ett misslyckat acceptanstest eller dömande användarforskning verkligen kan blockera leverans. I företags- och myndighetsmiljöer är detta ofta obligatoriskt, ibland genom oberoende verifiering och validering av en part skild från utvecklarna, och "vi levererade ändå" är inte ett svar ett tillsynsorgan accepterar. Ta med era senaste releaser: stoppade någon kvalitetssignal någonsin en, eller viker grinden alltid för datumet? Om validering aldrig har blockerat en release är den dekoration, och åtgärden är att skriva in acceptanskriterier i kvalitetsplanen i förväg, namnge vem som äger beslutet att gå eller inte gå vidare och ge det beslutet verklig befogenhet oberoende av leveranstrycket.

4. **Känner vi faktiskt till vår kostnad för dålig kvalitet, och flyttar vi medvetet utgifter från fel mot förebyggande?** Kostnaden för dålig kvalitet (COPQ) är de pengar som förloras på internt omarbete, produktionsincidenter, nödrättelser, supportbelastning, förlorade användare och vite, och den är nästan alltid större än den synliga utgiften för granskningar och testning. I ett stort team är felkostnaderna utspridda över incidentkanaler, supportköer och omarbete ingen loggar som omarbete, så de förblir osynliga tills någon summerar dem. Spänningen är att förebyggande kostar pengar nu, i en budgetcykel, för att undvika felkostnader som landar senare och landar på någon annans budget, vilket gör bytet lätt att skjuta upp för alltid. Ta med verkliga siffror: incidentantal och kostnad, omarbetstimmar, andel undkomna defekter och den nuvarande fördelningen av utgifter över förebyggande, bedömning och fel, och besluta sedan om blandningen bör flyttas tidigare. För företags- och myndighetssystem, där det mesta av livstidskostnaden landar efter första release, lägg COPQ framför dem som håller i budgeten, för ett tal ett tillsynsorgan kan se är långt svårare att byta bort än en vag vädjan om "kvalitet".

5. **Vilka av våra kvalitetsmått har i det tysta blivit mål, och vilket beteende driver de nu?** Ett mått som blir ett mål slutar mäta verkligheten: jaga en täckningsprocent och du får tester skrivna för att flytta talet, inte tester som fångar defekter. I stor skala är detta farligt, eftersom en rubrikinstrumentpanel delad över dussintals team sätter incitamenten för dem alla, och ett mått som går att manipulera sprider manipulationen överallt på en gång. Den motstridiga hänsynen är att ni fortfarande behöver mätning, så svaret är sällan "släpp måttet" utan "para det med en motsignal och läs det vid sidan av kvalitativa belägg från granskningar och användare". Ta med er nuvarande måttuppsättning och fråga för vart och ett vad någon under press skulle kunna göra för att flytta det utan att förbättra kvaliteten, och om ni har sett det hända. I reglerade och medborgarvända miljöer, var särskilt vaksam mot överensstämmelsemått som ser gröna ut medan den underliggande valideringen (tillgänglighet, verkliga användarutfall) aldrig verkligen utövades, eftersom en revisor till slut kommer att testa verkligheten bakom talet.

6. **Vem äger kvalitet här: teamen som skriver koden, eller en separat grupp i slutet, och vilken resurssätter vi faktiskt?** Ägarskap formar allt nedströms, eftersom en efterföljande QA-silo låter utvecklare avlasta ansvaret för koden de skriver, medan teamägd kvalitet bygger ägarskap till priset av att kräva skicklighet och disciplin i varje team. I ett stort team är detta inte antingen eller: det hållbara mönstret är vanligen att team äger kvalitet genom kodgranskning och automatiska tester, stödda av en liten central grupp som underhåller standarder, kör kvalitetssäkring som processförbättring och coachar, snarare än att inspektera in kvalitet i slutet. Ta med en ärlig karta över var kvalitetsarbete just nu sker, vem som är ansvarig när en defekt slipper ut och var budget och bemanning faktiskt finns mot var retoriken säger att kvalitet bor. För företags- och myndighetsorganisationer, lägg till kravet på oberoende verifiering och validering: vissa försäkransregimer föreskriver en separat part, så besluta medvetet vilka kontroller som hör hemma hos leveransteamen och vilka som måste förbli oberoende för att tillfredsställa revisionen.

## Sektorsperspektiv

**Startup.** Hastighet spelar större roll än ceremoni, så namnge de två eller tre kvalitetsegenskaper som faktiskt skyddar din produkt, vanligen tillförlitlighet och underhållbarhet, och låt polish vänta. Äg kvalitet i hela teamet med kodgranskning och en måttlig automatiserad testsvit snarare än att inrätta en separat QA-grupp du inte kan bemanna. När samma klass av bugg dyker upp två gånger, lägg tjugo minuter på grundorsak och lägg till en gemensam hjälpfunktion plus ett test, så att förebyggande förblir billigt och din andel misslyckade ändringar förblir låg medan du rör dig snabbt.

**Småföretag.** Utan särskild kvalitetsspecialist och med snäv budget, lita på kvalitet som är inbyggd i de verktyg och plattformar du köper snarare än en process du måste köra. När du väljer programvara, behandla leverantörens kvalitetsbelägg som en del av köpet: säkerhetsläge, tillgänglighet, supportens svarstid och hur ofta deras releaser går sönder. Följ en handfull billiga, ärliga signaler (produktionsincidenter, kundrapporterade problem, tid att åtgärda) i stället för ett utarbetat mätprogram du inte har någon att underhålla.

**Storföretag.** Arbetet är enhetlighet över många team: anta en gemensam kvalitetsmodell som ISO/IEC 25010, skilj kvalitetssäkring (process) från kvalitetskontroll (produkt) och kör granskningar av kvalitetskostnad som flyttar utgifter mot förebyggande. Håll kvalitet ägd av leveransteamen, stödda av en liten central grupp som underhåller standarder och instrumentpaneler för andel undkomna defekter, andel misslyckade ändringar och trender i kodhälsa. Standardisera ordförrådet och grindarna så att grupper slutar uppfinna om kvalitetspraxis, medan teamen lämnas utrymme att möta de ribborna på sitt eget sätt.

**Offentlig sektor.** Upphandling, transparens och offentlig ansvarsskyldighet sätter ramen, så skriv in kvalitetskrav i avtal och kräv dokumenterade, spårbara kvalitetsbelägg snarare än påståenden. Räkna med oberoende verifiering och validering av en part skild från utvecklarna, obligatorisk tillgänglighetsöverensstämmelse och defektregister med allvarlighetsgrad och grundorsak bevarade som en del av revisionsspåret. Rapportera siffror för kostnad för dålig kvalitet (omarbete, överklaganden, tjänstefel) till tillsynsorgan, och ge validering verklig befogenhet att blockera en release som skulle svika de medborgare som är beroende av den.

## Exempel

**Startup.** En startup med fem personer beslutar att för sin tidiga produkt är tillförlitlighet och underhållbarhet de kvalitetsegenskaper som spelar roll, och låter pixelperfekt polish vänta. Kvalitet ägs av hela teamet: kodgranskning och en måttlig automatiserad testsvit är kontrollerna, och det finns ingen separat QA-grupp att lämna över defekter till. När samma klass av bugg dyker upp två gånger lägger de tjugo minuter på en snabb grundorsaksblick och lägger till en gemensam hjälpfunktion plus ett test, så att det slutar återkomma i stället för att åtgärdas för hand varje gång. Den lilla vanan av förebyggande håller deras andel misslyckade ändringar låg medan de fortfarande rör sig snabbt.

**Storföretag.** Ett stort finansiellt tjänsteföretag antar ISO/IEC 25010 som sitt kvalitetsordförråd och registrerar för varje produkt målnivåer för tillförlitlighet, säkerhet och underhållbarhet. Team äger kvalitet: kodgranskning och automatiska tester är kontroller i pipelinen, medan en liten central grupp kör QA genom att underhålla standarder och coacha. En kvalitetsinstrumentpanel följer andel undkomna defekter, andel misslyckade ändringar och trender i kodhälsa. Defekter klassificeras och grundorsaksanalyseras, och återkommande orsaker driver uppdateringar av gemensamma bibliotek och checklistor. Ledningen granskar kvalitetskostnadsdata kvartalsvis och har flyttat utgifter mot förebyggande, vilket skär både produktionsincidenter och kostnaden för att åtgärda dem.

**Offentlig sektor.** En nationell myndighet som levererar en medborgarvänd bidragsplattform arbetar under en försäkransregim som kräver dokumenterade kvalitetsbelägg. Den kör en formell kvalitetshanteringsprocess med en kvalitetsplan per release, plus oberoende verifiering och validering av ett team skilt från utvecklarna. Verifiering kontrollerar varje arbetsprodukt mot krav spårade till policy. Validering inkluderar tillgänglighetsprovning och användarforskning med verkliga medborgare, och endera kan blockera en release. Defekter spåras med allvarlighetsgrad och grundorsak som en del av revisionsspåret, och siffror för kostnad för dålig kvalitet (omarbete, överklaganden och tjänstefel) går till tillsynsorgan för att motivera fortsatt investering i förebyggande.

## Affärsnytta: motiv, ROI och TCO

Avkastningen på kvalitet är lägre total ägandekostnad och stabil leveranshastighet. Kvalitetens kostnad har två sidor. Den goda utgiften, förebyggande och bedömning, är synlig och styrbar: design, standarder, granskningar, testning och verktyg. Kostnaden för dålig kvalitet (COPQ) är större men ofta dold: internt omarbete, produktionsincidenter, nödrättelser, kundsupport, förlorade användare, regulatoriska vite och anseendeskada. Studier som går tillbaka till Crosbys "Quality Is Free" har konsekvent funnit att den totala kostnaden för dålig kvalitet överstiger kostnaden för att förebygga den med råge, och att defekter blir långt dyrare ju senare du fångar dem: ett problem funnet i design kostar en bråkdel av samma problem funnet i produktion.

För ledningen är argumentet inte "spendera mer på kvalitet". Det är "spendera tidigare för att spendera mindre totalt". Kvantifiera COPQ från din egen data (incidentantal och kostnad, omarbetstimmar, andel undkomna defekter) och visa hur förebyggande och tidig bedömning sänker den. Koppla kvalitet till affärsutfall: tillförlitlighet behåller kunder, underhållbarhet håller framtida förändring billig och säkerhet och tillgänglighet håller dig borta från rättslig trubbel. I långlivade företags- och myndighetssystem, där det mesta av kostnaden landar efter första release, dominerar kvalitetens underhållbarhets- och tillförlitlighetsdimensioner livstidskostnaden. Det gör tidig kvalitetsinvestering till ett av de mest hävstångsstarka beslut du kan fatta.

## Antimönster och fallgropar

- **Kvalitet som en slutgrind:** att inspektera in kvalitet i slutet i stället för att bygga in den, så att defekter hittas när de är som dyrast.
- **Att förväxla testning med kvalitet:** att anta att godkända tester betyder hög kvalitet och ignorera underhållbarhet, användbarhet och lämplighet för syftet.
- **QA som separat silo:** ett efterföljande team som "äger kvalitet", vilket låter utvecklare avlasta ansvaret för koden de skriver.
- **Måtteater:** att jaga täckningsprocent eller defektantal som mål, vilket inbjuder till manipulation och döljer verklig kvalitet.
- **Verifiering utan validering:** att bygga specifikationen korrekt utan att någonsin kontrollera att specifikationen möter verkliga behov.
- **Ingen grundorsaksanalys:** att åtgärda defekter en och en utan att ta itu med den systematiska orsaken, så att samma klass återkommer.
- **Att ignorera kostnaden för dålig kvalitet:** att behandla kvalitet som ren kostnad eftersom felkostnaderna är dolda och omätta.

## Mognadsmodell

**Nivå 1 (Initiera).** Kvalitet är odefinierad och ad hoc. Den vilar på individuell flit, kontrolleras främst genom manuell testning i slutet och defekter hanteras reaktivt när de dyker upp. Det finns ingen gemensam modell, inga mått och ingen skiljelinje mellan säkring och kontroll.

**Nivå 2 (Utveckla).** Grundläggande praxis dyker upp: kodgranskning, automatiska tester och en defektregistrering. Viss kvalitetsdata samlas in, men ojämnt, och varje team gör det på sitt eget sätt. Kvalitet ses fortfarande mest som testning, förebyggande är minimalt, verifiering sker och validering är informell.

**Nivå 3 (Standardisera).** Organisationen antar en gemensam kvalitetsmodell (som ISO/IEC 25010), skiljer QA från QC och kör kvalitetshanteringsprocesser med kvalitetsplaner och acceptanskriterier, dokumenterade och tillämpade konsekvent över team. Verifiering och validering är skilda och medvetna, och defekter klassificeras och grundorsaksanalyseras enligt ett överenskommet schema.

**Nivå 4 (Hantera).** Kvalitet mäts och styrs mot utgångslägen. En liten uppsättning meningsfulla mått följs över tid (defekttäthet, andel undkomna defekter, genomsnittlig tid att upptäcka och åtgärda, andel misslyckade ändringar och kodhälsosignaler som komplexitet och duplicering), och kvalitetskostnad kvantifieras över förebyggande, bedömning och fel. Acceptans- och kvalitetsgrindar upprätthålls på grundval av belägg snarare än åsikt, trender granskas i en fast takt och validering kan verkligen blockera en release.

**Nivå 5 (Orkestrera).** Kvalitet är en kontinuerligt förbättrad, kulturellt ägd disciplin integrerad med affärs- och riskplanering. Förebyggande är tyngdpunkten, kvalitetskostnadsdata styr var investeringen går och grundorsaksfynd förhindrar systematiskt återfall. Team äger kvalitet från början till slut, mått matar kontinuerlig förbättring och organisationen anpassar sin kvalitetspraxis när produkter, risker och reglering förskjuts. Detta stämmer med de högre nivåerna i mognadsmodellerna i kapitel 10.8.

## Idéer för diskussion

- Vilka kvalitetsegenskaper i ISO/IEC 25010 spelar störst roll för era system, och vad är "tillräckligt bra" för var och en?
- Var ligger er organisation i fördelningen av utgifter mellan förebyggande, bedömning och fel, och bör den flyttas?
- Skiljer ni verifiering från validering i praktiken, eller slår ni ihop båda till "testning"?
- Ägs kvalitet av teamen som bygger programvaran, eller delegeras den till en separat grupp, och vad skulle ändras om ni flyttade den?
- Vad är er sanna kostnad för dålig kvalitet, och kunde ni mäta den tillräckligt väl för att göra affärscaset?
- Vilka av era kvalitetsmått är genuina signaler, och vilka har blivit mål som går att manipulera?

## Viktigaste punkter

- Kvalitet är bredare än testning: det är lämplighet för syftet plus överensstämmelse, över egenskaper som tillförlitlighet, säkerhet och underhållbarhet.
- Använd en gemensam kvalitetsmodell (ISO/IEC 25010) så att kvalitetsegenskaper är uttryckliga och i linje med arkitekturen (kapitel 3.1).
- Skilj kvalitetssäkring (förebygg, process) från kvalitetskontroll (upptäck, produkt), och luta åt förebyggande.
- Praktisera verifiering (byggde det rätt) och validering (byggde rätt sak) som skilda discipliner.
- Mät kvalitet med några få meningsfulla mått och karakterisera defekter efter allvarlighetsgrad och grundorsak för att förebygga återfall.
- Hantera kvalitetens kostnad: förebyggande och tidig bedömning är långt billigare än fel, särskilt i långlivade system.
- Bygg en skuldfri kvalitetskultur där team äger kvalitet, stödda av kodgranskning (kapitel 2.5) och teststrategi (kapitel 2.4).

## Referenser och vidare läsning

- IEEE Computer Society, *SWEBOK Guide (Guide to the Software Engineering Body of Knowledge)*, Software Quality knowledge area.
- ISO/IEC 25010, *Systems and software engineering: Systems and software Quality Requirements and Evaluation (SQuaRE): System and software quality models*.
- ISO/IEC 25000 series (SQuaRE), *Software product quality requirements and evaluation*.
- Philip B. Crosby, *Quality Is Free: The Art of Making Quality Certain*.
- W. Edwards Deming, *Out of the Crisis*.
- Capers Jones and Olivier Bonsignour, *The Economics of Software Quality*.
- Gerald Weinberg, *Quality Software Management*.
- ISO/IEC/IEEE 12207, *Systems and software engineering: Software life cycle processes* (quality assurance and V&V process context).
