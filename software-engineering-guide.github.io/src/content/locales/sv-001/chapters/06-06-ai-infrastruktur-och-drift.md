# 6.6 AI-infrastruktur och drift

## Översikt och motivation

AI-infrastruktur och drift är disciplinen att provisionera, schemalägga och driva de specialiserade beräknings-, lagrings- och driftsystem som AI-arbetslaster kräver, och att göra det kostnadseffektivt, pålitligt och observerbart. Modern AI är dyr att driva. Att träna och driva stora modeller kräver knappa acceleratorer ([GPU:er](https://en.wikipedia.org/wiki/Graphics_processing_unit) och [TPU:er](https://en.wikipedia.org/wiki/Tensor_Processing_Unit)), nätverk med hög bandbredd, storskalig vektorlagring för återvinning (att indexera data som numeriska vektorer så att liknande objekt snabbt kan hittas) och driftlager trimmade för latens och genomströmning. Att få den här infrastrukturen rätt är skillnaden mellan AI som skalar hållbart och AI som i tysthet förbrukar en budget medan den underpresterar.

För stora team är kärnproblemen skala, knapphet och kostnad. Acceleratorer är begränsade och dyra, så schemaläggning och beläggning spelar enorm roll. Overksamma GPU:er är brända pengar, och dåligt batchad inferens multiplicerar kostnaden per begäran. Återvinningstunga applikationer behöver [vektordatabaser](https://en.wikipedia.org/wiki/Vector_database) som förblir snabba när de växer. Generativa AI-applikationer behöver promptversionering, utvärderingspipelines och observerbarhet (ibland kallat LLMOps) för att drivas säkert och förbättras över tid. Utan gemensam infrastruktur och driftdisciplin utkämpar varje team samma strider och kostnaderna skenar.

Myndigheter och reglerade organisationer lägger till krav kring datasuveränitet, säkerhet och förutsägbara utgifter. De kan behöva lokal eller suverän molndriftsättning så att känslig data och modeller aldrig lämnar kontrollerade gränser. De måste prognostisera och motivera infrastrukturutgifter och möta säkerhets- och tillgänglighetsstandarder. AI-infrastrukturbeslut i dessa miljöer bär fleråriga konsekvenser, så fatta dem med upphandling, säkerhet och utträde i åtanke.

## Nyckelprinciper

- Behandla acceleratorberäkning som en knapp, dyr resurs att schemalägga och utnyttja, inte hamstra.
- Optimera kostnad per användbar arbetsenhet, inte rå kapacitet.
- Dimensionera modeller och hårdvara efter uppgiften. Det största alternativet är sällan det mest kostnadseffektiva.
- Designa drift för latens och genomströmning med batchning och cachning som förstklassiga tekniker.
- Gör AI-system observerbara: följ kostnad, latens, kvalitet och fel kontinuerligt.
- Versionera och utvärdera prompter och modeller med samma stringens som kod.
- Planera för portabilitet och undvik inlåsning i infrastruktur- och driftval.

## Rekommendationer

### Planera och kontrollera acceleratorberäkning

Prognostisera efterfrågan för träning och inferens var för sig, eftersom de har olika former. Träning är skurvis och schemaläggningsbar. Inferens är kontinuerlig och latenskänslig. Använd schemaläggare och kvoter för att dela knappa GPU:er och TPU:er över team, prioritera arbetslaster och driva upp beläggningen. Mät beläggning och behandla kronisk overksamhet som ett problem att rätta. Blanda reserverad kapacitet för baslast med on-demand- eller spotkapacitet för toppar för att kontrollera kostnad. Överväg om billigare eller mindre acceleratorer, eller CPU-inferens för lätta modeller, skulle räcka. Välj mellan moln, lokalt och hybrid utifrån kostnad i er skala, behov av datasuveränitet och topmönster, och behåll en utträdesväg.

### Bygg återvinningsinfrastruktur: inbäddningar och vektordatabaser

För applikationer med återvinning, res infrastruktur för att generera [inbäddningar](https://en.wikipedia.org/wiki/Word_embedding) (numeriska vektorrepresentationer som placerar liknande objekt nära varandra) och lagra dem i en vektordatabas som stöder snabb [approximativ närmaste-granne-sökning](https://en.wikipedia.org/wiki/Nearest_neighbor_search) (att hitta de mest lika vektorerna utan att uttömmande jämföra varje) i er skala. Planera för tre saker: kostnaden och latensen för inbäddningsgenerering, indexets färskhet när dokument ändras och driftbördan av att hålla index konsekventa. Utvärdera om en dedikerad vektordatabas, ett vektorkapabelt tillägg till en befintlig databas eller en hanterad tjänst bäst passar er skala och er tolerans för inlåsning. Övervaka återvinningslatens och täckning, eftersom återvinningskvalitet direkt avgör applikationskvaliteten.

### Optimera modelldrift: batchning, cachning och latens

Drift är där inferenskostnad och användarupplevelse avgörs. Använd **batchning** för att bearbeta flera begäranden tillsammans och höja acceleratorns genomströmning, och balansera batchstorlek mot latens. Använd **cachning** aggressivt: cacha identiska eller semantiskt liknande begäranden, cacha inbäddningar och utnyttja prompt- eller prefixcachning där plattformen stöder det för att undvika att räkna om delad kontext. Sätt tydliga latensmål och mät svanslatens, inte bara genomsnitt. Dirigera begäranden till rätt dimensionerade modeller: en liten modell för enkla fall, en större bara när det behövs. Autoskala driften efter efterfrågan och belastningstesta före lansering så att ni känner er kapacitets- och kostnadskurva.

### Praktisera LLMOps: promptversionering, utvärderingspipelines och observerbarhet

Behandla prompter som versionerade artefakter i källkodshantering, med granskning och förmågan att rulla tillbaka. Bygg utvärderingspipelines som kör offline-testsviter automatiskt närhelst prompter eller modeller ändras, så att ni fångar regressioner före release. Instrumentera produktion omfattande: logga indata, utdata, latens, tokenanvändning, kostnad och fel, med sampling och integritetsskydd. Följ kvalitetssignaler och användarfeedback online. Den observerbarheten låter er fånga försämring, kontrollera kostnad, felsöka fel och förbättra system säkert: den operativa ryggraden i generativ AI i produktion.

### Hantera kostnad skoningslöst och observerbart

Tillskriv AI-utgifter till team och användningsfall så att kostnaden är synlig och ägd. Sätt budgetar och larm, övervaka kostnad per begäran och per utfall och granska de största kostnadsdrivarna regelbundet. Dra i de spakar ni har: dimensionering av modeller, cachning, batchning, trimning av prompt och kontext och val av den billigaste driftsättning som möter kraven. AI-kostnader kan skala med användning på överraskande sätt, så kontinuerlig kostnadsobserverbarhet är väsentlig för att undvika obehagliga överraskningar.

## Avvägningar: för- och nackdelar

| Beslut | Alternativ A | Alternativ B | Avvägning |
|---|---|---|---|
| Beräkningsplats | Moln | Lokalt | Elasticitet och låg kostnad i förväg mot kontroll, suveränitet och ekonomi i stabilt tillstånd |
| Kapacitet | Reserverad | On-demand/spot | Förutsägbar kostnad mot flexibilitet och avbrottsrisk |
| Batchstorlek | Stora batchar | Små batchar | Genomströmning och kostnad mot latens |
| Modellstorlek | Stor modell | Liten modell | Kvalitet mot kostnad och hastighet |
| Vektorlager | Dedikerad databas | Tillägg till befintlig databas | Prestanda i skala mot enkelhet och färre system |
| Cachning | Aggressiv | Minimal | Lägre kostnad och latens mot färskhet och komplexitet |

Den dominerande avvägningen är kostnad mot latens och kvalitet. Batchning, cachning och mindre modeller skär kostnad men kan lägga till latens eller minska kvalitet. Rätt balans beror på din applikations tolerans. Lokalt mot moln byter kontroll och ekonomi i stabilt tillstånd mot elasticitet och låg bindning, ett beslut starkt format av behov av datasuveränitet och skala.

## Frågor att diskutera med ditt team

1. **Vad är vår kostnad per användbart utfall i dag, och vilken spak skulle flytta den mest?** Rå kapacitet och genomsnitt per begäran döljer det tal som spelar roll: vad det kostar att leverera en verklig enhet värde och hur det skalar med användning. För ett stort team är klyftan mellan en optimerad och en ooptimerad driftsättning ofta flerfaldig i utgifter, så den här frågan förvandlar en vag oro över räkningen till en rangordnad lista över rättelser. Ta med nuvarande kostnadstillskrivning per team och användningsfall, trender per begäran och per utfall och de största kostnadsdrivarna. Diskutera spakarna i ordning efter utdelning: dimensionering av modeller, cachning (inklusive prefix- och semantisk cachning), batchning och trimning av prompt eller kontext. I myndigheter, lägg till trycket att prognostisera och motivera fleråriga utgifter. Svaret bör tilldela varje främsta kostnadsdrivare en ägare och en spak, inte en axelryckning.

2. **Om vår nuvarande inferensleverantör fördubblade sitt pris eller gick ner i morgon, hur snabbt kunde vi byta?** Tyst inlåsning är lätt att bygga och smärtsam att fly, och driftstackar är där den gömmer sig djupast. För företag och särskilt myndigheter är portabilitet ett upphandlings- och kontinuitetskrav, inte en trevlighet. Ta med din arkitektur: om modeller sitter bakom ett internt gränssnitt, om prompter och utvärderingssviter är portabla och hur mycket leverantörsspecifikt driftbeteende ni beror på. Signalen att bevaka är om någon någonsin kört er utvärderingssvit mot en andra leverantör eller ett andra driftsättningsmål. Om byte skulle ta månader och skriva om kärnvägar, behandla det som en designdefekt att åtgärda nu, eftersom suveräna och lokala alternativ kan bli obligatoriska med kort varsel.

3. **Vad är vår acceleratorbeläggning just nu, och hur mycket brinner overksamma GPU:er och obatchad inferens?** Acceleratorer är knappa och dyra, så kronisk overksamhet och drift per begäran dränerar i tysthet budgetar som kunde finansiera mer förmåga. För en stor organisation som delar GPU:er över team exponerar den här frågan om schemaläggning, kvoter och prioriteringar faktiskt håller beläggningen hög eller om hamstrad, underutnyttjad hårdvara är normen. Ta med verkliga beläggningssiffror, er batchnings- och cachningsställning och era mätningar av svanslatens, inte bara genomsnitt, eftersom användare känner den långsamma svansen. Diskutera om efterfrågan på träning och inferens prognostiseras var för sig, med tanke på deras olika former, och om en mindre modell eller CPU-inferens skulle räcka för lätta fall. Svaret bör peka på specifik overksam kapacitet att återta och specifika begäranden att batcha eller dirigera till en rätt dimensionerad modell.

4. **När en prompt- eller modelländring levereras, vad hindrar en tyst kvalitets- eller kostnadsregression från att nå användare?** En driftstack kan se frisk ut på latens och drifttid medan svaren den returnerar i tysthet blir sämre eller en ny prompt fördubblar tokenanvändningen per begäran. För ett stort team där många grupper redigerar prompter och byter modeller oberoende är en ogrindad ändring en produktionsincident som väntar på att hända, och sprängradien växer med varje team på den gemensamma plattformen. Ta med din utvärderingstäckning: vilka prompter och modeller som har offline-testsviter, om de sviterna körs automatiskt vid varje ändring, vilka kvalitets- och kostnadströsklar som grindar en release och hur snabbt ni kan rulla tillbaka. Diskutera om prompter bor i källkodshantering med granskning, eller om någon fortfarande kan redigera en levande systemprompt för hand. I företags- och myndighetssammanhang, knyt varje ändring till ett revisionsspår och en namngiven godkännare, eftersom en tillsynsmyndighet som frågar "vem ändrade det här och vad testade ni" behöver ett svar som är registrerat, inte ihågkommet.

5. **Hur avgör vi mellan moln, lokalt och suverän driftsättning, och har vi prissatt den verkliga ekonomin i stabilt tillstånd snarare än piloten?** Valet av beräkningsplats sätter er kostnadskurva, er datasuveränitetsställning och era utträdesalternativ i åratal, men det görs ofta på en pilots molnräkning som inte liknar produktion i skala. För en stor organisation är elastisk molnkapacitet billig att börja med och kan bli den största enskilda posten när inferens körs kontinuerligt, medan lokalt byter låg bindning mot kontroll och ekonomi i stabilt tillstånd. Ta med prognostiserade trännings- och inferensvolymer, break even-punkten där reserverad eller ägd hårdvara slår on-demand, era krav på dataplacering och säkerhet och de topmönster som talar för hybrid. I myndigheter och reglerade miljöer, väg krav på suveränt moln eller lokal drift som kan bli obligatoriska med kort varsel och bekräfta att arkitekturen håller modeller bakom ett internt gränssnitt så att ett påtvingat byte inte skriver om kärnvägar.

6. **Äger vi faktiskt våra AI-utgifter, och kan varje team se och svara för den kostnad det driver?** AI-kostnader skalar med användning på sätt som överraskar människor, och utan tillskrivning landar räkningen som ett enda ogenomskinligt tal ingen team känner ansvar för att krympa. I en stor organisation är kostnad ingen äger kostnad ingen optimerar, så frågan är om utgifter taggas till team och användningsfall med budgetar, larm och trender per utfall, eller om de upptäcks först när ekonomi eskalerar. Ta med din kostnadstillskrivningsmodell, de största drivarna per team och de spakar varje ägare kontrollerar: dimensionering, cachning, batchning och trimning av kontext. För företags- och myndighetsbudgetar, lägg till disciplinen att prognostisera och motivera fleråriga infrastrukturutgifter, eftersom ett offentligt organ som inte kan förklara sin beräkningsräkning rad för rad kommer att ha svårt att försvara den vid granskning.

## Sektorsperspektiv

**Startup.** Äg ingen infrastruktur du kan undvika. Anropa ett hostat inferens-API, dirigera enkla begäranden till en liten billig modell och reservera en större för svåra fall och cacha aggressivt så att upprepade prompter inte kostar något. Använd en hanterad vektordatabas snarare än att driva din egen, håll prompter i git med ett kort utvärderingsskript före varje ändring och logga kostnad per begäran så att en skenande räkning syns innan den gör ont. Din knappaste resurs är utvecklingsuppmärksamhet, så köp driftbarhet och håll bytet billigt.

**Småföretag.** Utan plattformsteam, behandla drift, återvinning och observerbarhet som saker du köper inuti verktyg du redan använder, inte system du bemannar. Föredra hanterad inferens och hanterad vektorsökning med transparent, förutsägbar prissättning och sätt ett hårt utgiftstak och ett faktureringslarm från dag ett. Ramma in beslutet som bygg mot köp ärligt: att driva GPU:er eller ett vektorindex lönar sig sällan i din volym, och en liten modell bakom ett hostat API möter vanligen behovet till en bråkdel av insatsen.

**Storföretag.** Problemet är en gemensam plattform på upptrampad stig över många team: poolade acceleratorer med schemaläggare, kvoter och prioriteringar för att driva upp beläggningen, standardiserad batchning och cachning, routrar som dimensionerar rätt och kostnad tillskriven varje team och användningsfall. Grinda prompt- och modelländringar med automatiska utvärderingssviter, standardisera gränssnittslagret så att leverantörer och driftsättningsmål förblir utbytbara och hantera kostnad per utfall som ett förstklassigt mått snarare än att varje grupp uppfinner kostsam, underutnyttjad infrastruktur på nytt.

**Offentlig sektor.** Datasuveränitet, säkerhet och förutsägbara utgifter formar varje val. Föredra lokal eller suverän molndriftsättning så att känslig data och modeller stannar inom kontrollerade gränser, schemalägg knappa GPU:er över avdelningar med kvoter ni kan motivera i upphandling och prognostisera kapacitet för att försvara fleråriga utgifter rad för rad. Versionera och utvärdera prompter och modeller med ett registrerat revisionsspår, behåll omfattande observerbarhet över kostnad och kvalitet och håll modeller bakom ett internt gränssnitt så att ett påtvingat byte till en ny leverantör eller en suverän plattform inte strandsätter er.

## Exempel

**Startup.** En liten startup som körde en AI-skrivfunktion höll sin räkning förnuftig utan att äga några GPU:er. Den anropade ett hostat inferens-API, dirigerade enkla begäranden till en billigare liten modell och sparade den större till svåra fall och cachade svar på upprepade prompter. Den lagrade sina prompter i git med ett kort utvärderingsskript som körde före varje ändring, använde en hanterad vektordatabas för återvinning så att den slapp driva en och loggade kostnad per begäran så att grundarna kunde se utgifterna stiga innan det blev en överraskning.

**Storföretag.** Ett mediebolag som körde en LLM-funktion med hög trafik skar inferenskostnaderna avsevärt. Det dirigerade enkla begäranden till en liten modell och reserverade en större för svåra. Det cachade svar på upprepade frågor och aktiverade prefixcachning för sin gemensamma systemprompt. Det körde GPU:er genom en gemensam schemaläggare för att hålla beläggningen hög, versionerade alla prompter i git med en automatisk utvärderingssvit som grindade ändringar och instrumenterade kostnad per begäran så att varje produktteam ägde sina utgifter.

**Offentlig sektor.** En nationell myndighet med strikta regler om datasuveränitet driftsatte sina AI-system lokalt så att känslig data och modeller aldrig lämnade dess kontrollerade miljö. Den schemalade knappa GPU:er över avdelningar med kvoter och prioriteringar, prognostiserade kapacitet för att motivera fleråriga upphandlingar och byggde en plattform för vektorsökning för återvinning över officiella dokument. Prompter och modeller versionerades och utvärderades före release. Omfattande observerbarhet följde kostnad och kvalitet, och arkitekturen höll modeller bakom ett internt gränssnitt för att bevara en utträdesväg och undvika inlåsning.

## Affärsnytta: motiv, ROI och TCO

Motivet för disciplinerad AI-infrastruktur är enkelt. AI i skala är kostsam, och klyftan mellan en optimerad och en ooptimerad driftsättning är ofta flerfaldig i utgifter. ROI kommer av högre acceleratorbeläggning, lägre kostnad per begäran genom batchning och cachning, rätt dimensionerade modeller och undvikande av överprovisionering. Observerbarhet och utvärderingspipelines betalar sig genom att förhindra kostsamma incidenter och möjliggöra säker iteration.

Den totala ägandekostnaden spänner över acceleratorberäkning (den största raden för många arbetslaster), vektorlagring, driftinfrastruktur, nätverk och plattforms- och driftpersonalen för att driva det. Väg detta mot kostnaden för att inte investera: skenande inferensräkningar, dålig latens som undergräver antagande och oförmåga att skala. För myndigheter, lägg till kostnaden för att misslyckas med krav på suveränitet eller säkerhet. Driv ärendet inför ledningen genom att visa trender för kostnad per utfall och en plattform på upptrampad stig som låter många team driftsätta AI effektivt, snarare än att var och en bygger kostsam, underutnyttjad infrastruktur.

## Antimönster och fallgropar

- **Overksamma acceleratorer.** Att dedikera knappa GPU:er till team som lämnar dem underutnyttjade.
- **Ingen batchning eller cachning.** Att betjäna varje begäran för sig och räkna om delad kontext.
- **Största modellen som standard.** Att använda en dyr modell där en liten skulle duga.
- **Kostnadsblindhet.** Ingen tillskrivning, inga budgetar eller synlighet av kostnad per begäran förrän räkningen anländer.
- **Oversionerade prompter.** Att ändra prompter i produktion utan versionering eller utvärderingsgrind.
- **Försummad svanslatens.** Att optimera genomsnittlig latens medan användare lider av långsamma svansar.
- **Tyst inlåsning.** Att bygga djupt på en leverantörs driftstack utan portabilitet.

## Mognadsmodell

1. **Initiera.** Ad hoc-allokering av GPU:er som reagerar på den som ber högljuddast, ingen batchning eller cachning, ingen kostnadssynlighet förrän räkningen anländer, prompter redigerade live och oversionerade, minimal övervakning.
2. **Utveckla.** Vissa team antar gemensam schemaläggning, cachning och versionshanterade prompter, men praxis är inkonsekvent över organisationen: en grupp batchar och utvärderar medan en annan fortfarande betjänar varje begäran för sig och ändrar prompter för hand.
3. **Standardisera.** En dokumenterad plattform på upptrampad stig upprätthålls i hela organisationen: gemensam schemaläggning med kvoter och prioriteringar, standardiserad batchning, cachning och rätt dimensionering, vektorinfrastruktur för återvinning, automatiska utvärderingspipelines som grindar varje prompt- eller modelländring och kostnadstillskrivning till team och användningsfall.
4. **Hantera.** Plattformen mäts och styrs mot utgångslägen: acceleratorbeläggning, kostnad per användbart utfall, svanslatens, återvinningstäckning och kvalitetsregressioner per ändring följs med larm och trösklar, kostnad ägs av varje team och beslut att gå eller inte gå på en ändring fattas på belägg snarare än intuition.
5. **Orkestrera.** Infrastrukturen förbättras och anpassas kontinuerligt: dirigering, batchning och skalning justerar sig själva mot levande kostnads- och kvalitetssignaler, kapacitet balanseras om mellan team och mellan moln, lokalt och suveräna mål när efterfrågan och begränsningar skiftar, portabilitet övas och infrastrukturplaneringen är integrerad med produkt, säkerhet och upphandling.

## Idéer för diskussion

- Hur driver ni upp acceleratorbeläggningen utan att svälta prioriterade arbetslaster?
- Var går den rätta balansen mellan batchning och cachning för era latenskrav?
- När motiverar lokal eller suverän driftsättning sin kostnad över moln?
- Hur tillskriver och kontrollerar ni AI-utgifter över många team?
- Vad bör grinda en prompt- eller modelländring från att nå produktion?
- Hur håller ni driftinfrastruktur portabel nog att byta leverantör?

## Viktigaste punkter

- Acceleratorer är knappa och dyra. Schemalägg, dela och utnyttja dem medvetet.
- Batchning, cachning och rätt dimensionering av modeller är de primära spakarna för kostnad och latens.
- Återvinningsapplikationer behöver väl drivna inbäddnings- och vektorsökningsinfrastruktur.
- LLMOps (promptversionering, utvärderingspipelines och observerbarhet) är den operativa ryggraden i generativ AI.
- Hantera kostnad observerbart och bevara portabilitet för att undvika inlåsning.

## Referenser och vidare läsning

- Chip Huyen, *Designing Machine Learning Systems*.
- Google, *Site Reliability Engineering* (Beyer, Jones, Petoff, Murphy, editors).
- Jared Kaplan et al., *Scaling Laws for Neural Language Models*.
- Reza Yazdani Aminabadi et al., *DeepSpeed Inference: Enabling Efficient Inference of Transformer Models at Unprecedented Scale*.
- Woosuk Kwon et al., *Efficient Memory Management for Large Language Model Serving with PagedAttention* (vLLM).
- Andriy Burkov, *Machine Learning Engineering*.
