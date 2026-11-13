# 3.9 Systemteknik

## Översikt och motivation

[Systemteknik](https://en.wikipedia.org/wiki/Systems_engineering) är disciplinen att konstruera ett helt komplext system från början till slut, så att alla dess delar fungerar tillsammans för att möta ett verkligt behov. Delarna omfattar mycket mer än programvara. Ett modernt system kombinerar vanligen programvara, hårdvara, människor, data och processer, och det måste verka i en rörig verklighet. Systemteknik håller allt detta justerat över systemets hela liv.

Det här skiljer sig från programvaruarkitektur. Programvaruarkitektur (kapitel 3.1) avgör hur programvarukomponenter struktureras och hur de talar med varandra. Systemteknik sitter en nivå högre. Den frågar vad systemet som helhet måste göra, hur programvara och hårdvara och mänskliga operatörer delar på arbetet och hur du ska bevisa att det färdiga fungerar. Dess professionella hem är [INCOSE](https://en.wikipedia.org/wiki/International_Council_on_Systems_Engineering), International Council on Systems Engineering, och dess ankarstandard är [ISO/IEC/IEEE 15288](https://en.wikipedia.org/wiki/ISO/IEC_15288), som definierar processerna för ett systems liv.

Det här spelar roll för stora företags- och myndighetsprogram eftersom deras system är stora, långlivade och säkerhetskritiska eller uppdragskritiska. En försvarsplattform, ett flygledningssystem eller en satellitkonstellation blandar skräddarsydd hårdvara, tredjepartsdelar, inbyggd och molnbaserad programvara och mänskliga operatörer, och inget enskilt team kan hålla hela saken i huvudet. Du bygger också ofta ett [system av system](https://en.wikipedia.org/wiki/System_of_systems): många oberoende system, vart och ett användbart för sig, som måste samarbeta för att leverera en större förmåga.

Det här kapitlet hänger ihop med programvarukrav (kapitel 2.8), arkitekturens grunder (kapitel 3.1), programvarumodeller och metoder (kapitel 2.12), interoperabilitet och öppna standarder (kapitel 3.8) och projektledning (kapitel 10.6).

## Nyckelprinciper

- **Konstruera helheten, inte delarna.** Ett system lyckas eller fallerar som helhet, så att optimera ett delsystem isolerat kan göra helheten sämre.
- **Följ livscykeln.** Ett system har ett liv från första koncept till slutlig avveckling. Planera för hela det, inte bara bygget.
- **Spåra varje krav.** Varje behov bör kartläggas till ett krav, ett designelement och ett test. Om du inte kan spåra det kan du inte bevisa det.
- **Hantera gränssnitt med avsikt.** De flesta fel sker vid gränserna mellan delar, så gränssnitt förtjänar uttryckligt ägarskap och kontroll.
- **Verifiera och validera var för sig.** Att bygga saken rätt (verifiering) och att bygga rätt sak (validering) är olika frågor, och du behöver båda svaren.
- **Förvänta framväxande beteende.** Att kombinera delar skapar beteende ingen enskild del visar. En del av det är poängen, och en del är en otrevlig överraskning.
- **Samkonstruera hårdvara och programvara.** När båda är skräddarsydda begränsar beslut i den ena den andra, så planera dem tillsammans.

## Rekommendationer

### Hantera systemets hela livscykel

Behandla systemet som att det har ett helt liv och planera varje skede. En vanlig livscykel går: **koncept** (förstå behovet och utforska alternativ), **krav** (ange exakt vad systemet måste göra), **design** (besluta arkitekturen och delarna), **integration** (föra samman delarna), **verifiering och validering** (bevisa att det fungerar och är rätt system), **drift** (köra och underhålla det) och **avveckling** (avveckla det säkert, inklusive data och bortskaffande). ISO/IEC/IEEE 15288 ger dig ett processramverk för detta. Skedena behöver inte vara ett stelt vattenfall. Du kan iterera, prototypa och leverera i steg. Poängen är att du medvetet adresserar varje skede, inklusive de dyra senare som tidiga planer ofta ignorerar.

### Fånga intressenters behov och allokera krav med spårbarhet

Börja från de människor som bryr sig om systemet: användare, operatörer, ägare, tillsynsmyndigheter och allmänheten. Samla deras **behov** i klartext och omvandla sedan behoven till konstruerade **krav** som är specifika och testbara (se kapitel 2.8). Därnäst kommer **kravallokering**: att tilldela varje krav på systemnivå till ett specifikt delsystem, så att du vet vilken del som ansvarar för att uppfylla det. För en **[spårbarhetsmatris](https://en.wikipedia.org/wiki/Requirements_traceability)**, ett levande register som länkar varje behov till dess krav, till designelementet som uppfyller det och till testet som verifierar det. Den låter dig bevisa när som helst att varje behov är täckt och varje del finns av ett skäl.

### Hantera gränssnitt uttryckligen

Gränssnitt är där delar möts, och där system oftast går sönder. Ett gränssnitt kan vara en fysisk kontakt, ett nätverksprotokoll, ett dataformat eller en mänsklig procedur. För var och ett, skriv ett **Interface Control Document** (ICD): en överenskommen specifikation av exakt hur två delar kopplas och utbyter information. Ge varje gränssnitt en tydlig ägare på varje sida. Att förlita sig på gemensamma, publicerade specifikationer snarare än engångskontakter gör integration långt lättare, vilket är interoperabilitetsargumentet i kapitel 3.8. Frys gränssnitt tidigt där du kan, för en sen ändring ger krusningar i varje del som rör vid det.

### Integrera och sedan verifiera och validera

**Systemintegration** kombinerar delsystem till den fungerande helheten, vanligen i steg snarare än allt på en gång, så att du hittar problem medan de fortfarande är små. Efter integration kommer **[verifiering och validering](https://en.wikipedia.org/wiki/Verification_and_validation)** (V&V), två skilda kontroller. **Verifiering** frågar: byggde vi systemet rätt, det vill säga uppfyller det sina specificerade krav? Du verifierar genom inspektion, analys, demonstration och test. **Validering** frågar: byggde vi rätt system, det vill säga möter det intressenternas verkliga behov i verklig användning? Ett system kan klara verifiering (det uppfyller specifikationen) men falla på validering (specifikationen var fel). Planera båda tidigt, och skriv krav och gränssnitt så att de över huvud taget kan verifieras.

### Anta modellbaserad systemteknik

Traditionell systemteknik producerade berg av dokument som drev ur takt. **[Modellbaserad systemteknik](https://en.wikipedia.org/wiki/Model-based_systems_engineering)** (MBSE) ersätter högen med en enda, delad, formell modell av systemet, ur vilken vyer och rapporter genereras. Det vanliga modelleringsspråket är **[SysML](https://en.wikipedia.org/wiki/Systems_Modeling_Language)** (Systems Modelling Language), ett grafiskt språk för att beskriva ett systems krav, struktur, beteende och begränsningar. Eftersom allt lever i en sammanhängande modell uppdaterar en ändring överallt, och spårbarhet blir en fråga snarare än en manuell jakt. MBSE hänger ihop med modelleringsidéerna i kapitel 2.12. Anta det gradvis, med start i de högriskigaste delarna där en delad modell betalar sig snabbast.

### Tillämpa systemtänkande på framväxande beteende

Praktisera [systemtänkande](https://en.wikipedia.org/wiki/Systems_thinking): resonera om helheten och relationerna mellan delar, inte bara delarna en i taget. Det är hur du förutser **[framväxande beteende](https://en.wikipedia.org/wiki/Emergence)**: egenskaper som bara uppstår när delar kombineras och som ingen enskild del visar. Gott framväxande beteende är ofta systemets syfte (en flock drönare täcker ett område ingen enskild drönare kunde). Dåligt framväxande beteende är den överraskande felet (två säkra delsystem samverkar och skapar ett farligt tillstånd). Du kan inte testa bort framväxande beteende ur ett system du aldrig modellerade, så använd simulering och strukturerad riskanalys för att hitta det före drift.

### Samkonstruera hårdvara och programvara

När ett system inkluderar skräddarsydd hårdvara, konstruera hårdvaran och programvaran tillsammans, en praxis kallad **[samdesign av hårdvara och programvara](https://en.wikipedia.org/wiki/Hardware/software_co-design)**. Besluten binder varandra: hårdvaran sätter timing-, minnes- och effektgränser programvaran måste leva inom, och programvarans behov formar vad hårdvaran måste tillhandahålla. Långa ledtider för hårdvara driver också tidsplanen. Besluta tidigt vilka funktioner som bor i hårdvara och vilka i programvara, och ompröva den uppdelningen när begränsningar framträder.

## Avvägningar: för- och nackdelar

| Tillvägagångssätt | Fördelar | Nackdelar / kostnad |
|---|---|---|
| Full systemteknisk stringens | Färre sena överraskningar, stark spårbarhet, säkrare och granskningsbart | Hög kostnad i förväg, långsammare start, tung process |
| Lätt / enbart programvarutillvägagångssätt | Snabbt, billigt, flexibelt för liten omfattning | Bryter ihop på stora system med flera discipliner, missar gränssnitt och framväxande beteende |
| Modellbaserad (MBSE) | Enda sanningskälla, enkel spårbarhet, konsekventa vyer | Verktygs- och utbildningskostnad, kulturförändring, inlärningskurva |
| Dokumentbaserad systemteknik | Välbekant, låg verktygskostnad, lätt att dela | Dokument driver ur takt, spårbarhet är manuell och felbenägen |

Den centrala avvägningen är stringens mot hastighet. Full systemteknik lägger insats i förväg på koncept, krav och gränssnittsarbete. Den insatsen betalar sig många gånger om på stora, långlivade, säkerhetskritiska system, där en defekt som hittas i drift kan kosta tusentals gånger mer än samma defekt hittad i kraven. På en liten, kortlivad, enbart programvarubaserad produkt är den stringensen överkill. Anpassa tyngden i din process till systemets storlek, livslängd och risk. Felmönstret är att tillämpa engångsprojektvanor på ett system som kommer att köras i trettio år och bära verklig risk.

## Frågor att diskutera med ditt team

1. **Var har ni byggt exakt vad specifikationen krävde och ändå levererat fel system, och vad skulle ha fångat det?** Verifiering (byggde vi det rätt) och validering (byggde vi rätt sak) besvarar olika frågor, och ett system kan klara varje verifieringstest medan det faller på validering eftersom själva specifikationen var fel. På stora program slås de två ihop till "testning", så ingen validerar mot verkligt operatörsbehov förrän sent, när en rättelse kostar tusentals gånger mer än en kravändring. Ta med ett tidigare exempel där det levererade systemet uppfyllde sina krav men missade det faktiska behovet, och fråga vilken valideringsaktivitet (en simulering med verkliga operatörer, en tidig prototyp i fält) som skulle ha blottlagt det tidigare. Planera båda kontrollerna från början, och skriv krav och gränssnitt så att de över huvud taget kan verifieras. Skillnaden avgör var ni spenderar knapp granskningsinsats.

2. **Hur jagar ni dåligt framväxande beteende före systemet är i drift, inte efter?** Att kombinera säkra delsystem kan skapa farliga tillstånd ingen enskild del uppvisar, och ni kan inte testa bort framväxande beteende ur ett system ni aldrig modellerade. För ett säkerhetskritiskt eller uppdragskritiskt program är den överraskande interaktionen den som skadar någon eller fäller uppdraget, så den måste hittas före levande drift. Ta med ert sätt att modellera helheten (simulering, strukturerad riskanalys, en SysML-modell som fångar interaktioner) och fråga vilka beteenden över delsystem ni faktiskt har utforskat mot antagit bort. Gott framväxande beteende är ofta systemets syfte och värt att designa mot. Dåligt framväxande beteende är felet ni måste konstruera mot. Om er enda integrationsstrategi är att koppla ihop delarna och se vad som händer planerar ni att upptäcka framväxande beteende i produktion.

3. **När måste de hårdvarubeslut med lång ledtid frysas, och hur driver den deadlinen er programvarutidsplan?** När ett system inkluderar skräddarsydd hårdvara måste de två samkonstrueras: chipet sätter timing-, minnes- och effekttak programvaran lever inom, och hårdvaruledtider dominerar ofta hela tidsplanen. Team som behandlar programvara som separabel optimerar lokalt och krockar sedan med hårdvarubegränsningar vid integration och förlorar månader. Ta med hårdvaruledtiderna och datumet då uppdelningen av funktioner mellan hårdvara och programvara måste beslutas, och ompröva den uppdelningen när begränsningar framträder i stället för att frysa den blint. Ju tidigare ni beslutar vilka funktioner som bor i kisel och vilka i programvara, desto färre dyra vändningar möter ni. Gränssnitten mellan de två förtjänar ett Interface Control Document och en ägare på varje sida, eftersom en sen ändring där ger krusningar genom allt som rör vid det.

4. **Kan ni spåra ett enskilt intressentbehov hela vägen till kravet, designelementet och testet som bevisar det, och vem håller den länken vid liv?** Spårbarhet är det som låter er visa när som helst att varje behov är täckt och varje del finns av ett skäl, men i ett stort program ruttnar matrisen i samma stund ingen äger den. Det motstridiga draget är verkligt: ingenjörer upplever spårbarhet som byråkratisk overhead, och en matris underhållen för hand driver ur takt snabbare än designen ändras. Ta med en äkta tråd från ett pågående program och försök gå den från början till slut i rummet, från ett namngivet intressentbehov, till det allokerade kravet, till delsystemet och designelementet som uppfyller det, till verifieringstestet, och notera var kedjan bryts. Besluta vem som äger matrisen och om den bör bo i en modell där spårbarhet är en fråga snarare än en manuell jakt. För företags- och myndighetsprogram är matrisen också den revisionsartefakt tillsynsmyndigheter och upphandlande myndigheter kräver, så en bruten kedja gör mer än att bromsa tekniken: den kan stoppa certifiering eller betalning.

5. **Är ett modellbaserat tillvägagångssätt värt sin verktygs- och kulturkostnad för er, eller skulle det bli dyr hyllvara?** Dokumentbaserad systemteknik är välbekant och billig att utrusta, men dess dokument driver ur takt och dess spårbarhet är manuell och felbenägen. MBSE ersätter högen med en sammankopplad modell, till priset av verktyg, utbildning och en genuin kulturförändring. Endera ytterligheten är dyr: hoppa över MBSE på ett stort program med flera discipliner och ni betalar i integrationsöverraskningar, anta det utan disciplinen att hålla modellen aktuell och det ruttnar till hyllvara värre än ingen modell alls. Ta med en ärlig läsning av er verktygsmognad, vem i teamet som faktiskt kan författa och underhålla en SysML-modell och vilket ett högrisksdelsystem som kunde pilota ansatsen där en delad modell betalar sig snabbast. Besluta gradvis snarare än att föreskriva hela organisationen på en gång. För ett stort företags- eller myndighetsprogram med många leverantörer, väg om en delad modell är det enda realistiska sättet att hålla krav, gränssnitt och tester konsekventa över entreprenörer som annars utbyter inaktuella dokument.

6. **Finansierar er livscykelplan på allvar drift och avveckling, eller stannar den i det tysta vid lansering?** De skeden som dominerar ett långlivat systems totala kostnad, att köra det i decennier och avveckla det säkert, är de tidiga planer rutinmässigt ignorerar, eftersom trycket alltid är att leverera. Den motstridiga hänsynen är att pengar och uppmärksamhet är knappast just när dessa senare skeden känns som mest avlägsna, så drift, underhåll, datamigrering och bortskaffande skjuts upp tills de blir en dyr, riskfylld kapplöpning. Ta med den nuvarande livscykelplanen och kontrollera om den namnger ägare, budgetar och utträdeskriterier för drift och avveckling, eller om den behandlar lanseringen som mållinjen. Fråga vad som händer med data och hårdvara vid livets slut, och vem som betalar för åren av underhåll däremellan. För företags- och myndighetssystem som måste köras i tjugo eller trettio år och sedan avvecklas under offentlig granskning kan en oplanerad avveckling bryta mot regulatoriska, miljömässiga eller bevarandeskyldigheter för handlingar, så avveckling hör hemma i planen och budgeten från den första konceptgranskningen.

## Sektorsperspektiv

**Startup.** Ett pyttelitet team kan inte köra ett formellt systemtekniskt program och bör inte försöka, men det kan ändå behandla firmware, app och moln som ett system snarare än tre separata projekt. Skriv ett kort gränssnittsdokument som fastnaglar hur delarna talar, för en enkel tabell som länkar varje kundbehov till den del som uppfyller det och hoppa över den tunga processen. Din knappa resurs är utvecklingsuppmärksamhet, så lägg spårbarhetsinsats bara där ett felaktigt antagande vid en gräns i det tysta skulle bryta produkten i fält.

**Småföretag.** Utan särskild systemingenjör och med snäv budget, lita på publicerade standarder och köpta delsystem snarare än skräddarsydd integration du måste designa och verifiera själv. Föredra leverantörer som exponerar tydliga gränssnittsspecifikationer så att delarna passar utan en anpassad kontakt du måste äga för alltid. Rama in valet köp mot bygg kring vilka gränssnitt du realistiskt kan kontrollera och verifiera över produktens liv, och köp resten.

**Storföretag.** I stor skala är problemet enhetlighet över många team och leverantörer: en gemensam livscykelprocess justerad efter ISO/IEC/IEEE 15288, ett Interface Control Document och en namngiven ägare för varje leverantörsgräns och spårbarhet från början till slut så att en komponentändring inte utlöser en programomfattande kapplöpning. Investera i MBSE där en delad modell håller krav, gränssnitt och tester justerade över entreprenörer. Styr processen så att verifiering och validering förblir skilda och varje krav allokeras till en ansvarig del.

**Offentlig sektor.** Upphandlingsregler, transparens och offentlig ansvarsskyldighet formar varje val. Specificera systemteknisk process, spårbarhet och V&V-belägg i avtalet, kräv att leverantörer levererar gränssnittskontrolldokument och livscykelartefakter ni kan granska och reservera säkerhets- och uppdragsvalidering för oberoende granskning med verkliga operatörer före varje levande övergång. Planera och finansiera drift och avveckling uttryckligen, eftersom ett offentligt program är ansvarigt för hela livscykeln, inklusive säker avveckling och bevarande av handlingar.

## Exempel

**Startup.** En hårdvarustartup med fyra personer som bygger en uppkopplad sensor har inte råd med ett formellt systemtekniskt program, men den behandlar ändå produkten som ett system av firmware, en mobilapp och en molnbackend snarare än tre separata projekt. De skriver ett kort gränssnittsdokument som fastnaglar hur enheten, appen och servern talar (meddelandeformat, enheter, felkoder) och för en enkel tabell som länkar varje kundbehov till den del som uppfyller det. När ett billigare sensorchip tvingar fram en firmwareändring visar det delade gränssnittet omedelbart vad appen och backend måste justera, så att ett komponentbyte inte i det tysta bryter produkten i fält.

**Storföretag.** En global biltillverkare bygger en ny elbilsplattform: ett system av programvara (batterihantering, förarassistans, infotainment), hårdvara (motorer, sensorer, chip) och mänskliga faktorer, plus många leverantörer som var och en levererar delsystem. Företaget kör ett systemtekniskt program. Intressentbehov matar allokerade krav, varje leverantörsgränssnitt har ett Interface Control Document och en SysML-modell binder krav till design till tester. När en battericellsleverantör ändrar en komponent visar spårbarhetsmodellen exakt vilka krav, gränssnitt och tester som berörs, så att ändringen begränsas i stället för att utlösa en programomfattande kapplöpning.

**Offentlig sektor.** En nationell flygnavigeringsmyndighet moderniserar sitt flygledningssystem, ett säkerhetskritiskt system av system som spänner över radar, förarbetsstationer, kommunikation och programvara, drivet dygnet runt. Programmet följer ISO/IEC/IEEE 15288 över hela livscykeln. Verifiering bevisar att varje delsystem uppfyller sin specifikation, och validering genom simulering med verkliga flygledare bevisar att det integrerade systemet stöder säker drift innan någon levande trafik beror på det. Rigorös V&V låter myndigheten gå över i steg, med reservlösning vid varje steg, eftersom ett otestat framväxande fel här är en folksäkerhetshändelse.

## Affärsnytta: motiv, ROI och TCO

Motivet är att defekter blir exponentiellt dyrare ju senare du hittar dem. Ett kravfel fångat under kravskedet kostar nästan ingenting att åtgärda. Samma fel fångat i drift kan kosta tusentals gånger mer, och i ett säkerhetskritiskt system kan det kosta liv, återkallelser eller ett misslyckat uppdrag. Systemteknik flyttar defektupptäckt till de billiga tidiga skedena.

För **avkastning** (ROI, värde vunnet jämfört med kostnad spenderad) är utdelningen undvikt omarbete, färre integrationsfel och program som håller tidsplan och budget i stället för att överskrida. Branschstudier av stora program finner upprepade gånger att stark systemteknisk insats korrelerar med mindre överskridanden. För **total ägandekostnad** (TCO, den fulla livstidskostnaden för att bygga, driva och avveckla ett system) tar systemteknik hänsyn till drift- och avvecklingsskeden som dominerar långsiktig kostnad men som ad hoc-projekt ignorerar. Att designa för underhållbarhet, gränssnitt och bortskaffande från början sänker kostnaden för de decennier systemet tillbringar i drift. Se projektledning (kapitel 10.6).

## Antimönster och fallgropar

- **Stor design i förväg utan iteration.** Att behandla livscykeln som ett stelt envägsvattenfall, så att du lär dig att kraven var fel först efter att ha byggt allt.
- **Krav utan spårbarhet.** En hög krav ingen länkar till design eller tester, så du kan inte bevisa täckning eller motivera någon del.
- **Att ignorera gränssnitt.** Att anta att delsystem bara kommer att passa ihop och sedan förlora månader vid integration på gränsfel ingen ägde.
- **Verifiering utan validering.** Att bevisa att systemet uppfyller sin specifikation utan att någonsin kontrollera att specifikationen matchade verkliga behov, och sedan leverera fel system.
- **Att behandla programvara som separat.** Programvaruteam som optimerar lokalt medan de ignorerar hårdvarubegränsningar, timing och mänskliga operatörer.
- **MBSE som hyllvara.** Att bygga en modell en gång och sedan låta den ruttna ur takt så att den blir värre än ingen modell.
- **Att hoppa över avvecklingsplanering.** Ingen plan för avveckling, datamigrering eller bortskaffande, så att livets slut blir en dyr, riskfylld kapplöpning.

## Mognadsmodell

**Nivå 1: Initiera.** Systemteknik är ad hoc och reaktiv. Krav bor i utspridda dokument, gränssnitt upptäcks vid integration och verifiering är den testning som råkar bli gjord. Stora program överskrider regelbundet och överraskar teamet sent.

**Nivå 2: Utveckla.** Grundläggande praxis finns på större program. Krav fångas och sätts som baslinjer, nyckelgränssnitt har kontrolldokument och det finns en verifieringsplan. Praxis är inkonsekvent mellan team och beror på individer snarare än en gemensam metod.

**Nivå 3: Standardisera.** Systemteknik är en dokumenterad disciplin för hela organisationen justerad efter ISO/IEC/IEEE 15288 och upprätthållen över team. Hela livscykeln är planerad, spårbarhet underhålls från början till slut, gränssnitt kontrolleras formellt och verifiering och validering är skilda och planerade. MBSE används på komplexa program.

**Nivå 4: Hantera.** Systemteknik mäts och styrs med data. Organisationen följer mått mot utgångslägen: kravvolatilitet och spårbarhetstäckning, gränssnittsdefekter som hittats vid integration, andel V&V som klaras och defektläckage per livscykelskede (hur många defekter som slipper ut ur varje skede för att fångas senare till högre kostnad). Granskningar styr program utifrån dessa tal, och trösklar utlöser korrigerande åtgärd i stället för brandkårsutryckning i efterhand.

**Nivå 5: Orkestrera.** Systemteknik förbättras kontinuerligt och är integrerad i hela organisationen. En levande MBSE-modell är den enda sanningskällan, spårbarhet är automatiserad, simulering förutsäger framväxande beteende före bygget och mått från tidigare program matar nästa. Hårdvara och programvara samkonstrueras som en självklarhet, och processen anpassas när program, leverantörer och risker förskjuts.

## Idéer för diskussion

- Var går gränsen mellan systemteknik och programvaruarkitektur i er organisation, och vem äger utrymmet mellan dem?
- På ert största program, kan ni spåra ett enskilt intressentbehov hela vägen till testet som verifierar det? Om inte, vad skulle det krävas?
- Vilka av era senaste misslyckanden hände vid ett gränssnitt, och vem ägde det?
- Skulle MBSE betala sig för er, eller skulle det bli dyr hyllvara med tanke på er kultur och era verktyg?
- Adresserar er livscykelplan på allvar drift och avveckling, eller stannar den i det tysta vid lansering?

## Viktigaste punkter

- Systemteknik konstruerar hela systemet (programvara, hårdvara, människor och processer) från början till slut, och skiljer sig från programvaruarkitektur.
- Planera hela livscykeln, från koncept genom krav, design, integration, V&V, drift och avveckling.
- Spåra varje behov till ett krav, ett designelement och ett test, och allokera varje krav till en ansvarig del.
- Hantera gränssnitt uttryckligen med tydligt ägarskap och kontrolldokument, för gränser är där system går sönder.
- Verifiering (byggde det rätt) och validering (byggde rätt sak) är olika kontroller, och du behöver båda.
- Använd MBSE och SysML för en sammankopplad sanningskälla, och använd systemtänkande för att förutse framväxande beteende.
- Anpassa tyngden i din process till systemets storlek, livslängd och risk.

## Referenser och vidare läsning

- INCOSE, *INCOSE Systems Engineering Handbook: A Guide for System Life Cycle Processes and Activities*
- ISO/IEC/IEEE 15288, *Systems and Software Engineering: System Life Cycle Processes*
- ISO/IEC/IEEE 29148, *Systems and Software Engineering: Requirements Engineering*
- Sanford Friedenthal, Alan Moore, and Rick Steiner, *A Practical Guide to SysML: The Systems Modelling Language*
- NASA, *NASA Systems Engineering Handbook* (NASA/SP-2016-6105)
- Andrew P. Sage and William B. Rouse, *Handbook of Systems Engineering and Management*
- Dennis M. Buede and William D. Miller, *The Engineering Design of Systems: Models and Methods*
- Donella H. Meadows, *Thinking in Systems: A Primer*
- Eberhardt Rechtin and Mark W. Maier, *The Art of Systems Architecting*
- U.S. Department of Defence, *Defence Acquisition Guidebook* (systems engineering guidance)
