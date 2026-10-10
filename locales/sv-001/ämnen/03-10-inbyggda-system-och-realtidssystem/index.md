# 3.10 Inbyggda system och realtidssystem

## Översikt och motivation

Ett [inbyggt system](https://en.wikipedia.org/wiki/Embedded_system) är programvara som körs på en enhet snarare än på en generell dator. Det lever inuti en bil, en pacemaker, en termostat, en fabriksrobot eller en styrenhet. Programvaran är dedikerad till den enheten, och enheten har vanligen snäva gränser för minne, processorkraft och energi. Du kan inte alltid lägga till fler resurser med ett knapptryck i en molnkonsol. Det du levererar är ofta det som körs i åratal.

Ett [realtidssystem](https://en.wikipedia.org/wiki/Real-time_computing) är ett där korrektheten beror på timing, inte bara på att producera rätt svar. En krockkuddsstyrenhet som beräknar ett perfekt utlösningskommando en sekund för sent har misslyckats totalt. Realtidsarbete lägger en svår fråga på varje uppgift: blir den klar inom sin deadline, varje gång, i värsta fall? Det är en annan disciplin än det genomströmningsfokuserade tänkande som är vanligt inom webb- och molnprogramvara.

För en stor organisation spelar det här större roll än det först verkar. Företag bygger uppkopplade bilar, medicintekniska produkter, industriella styrenheter och miljarder [sakernas internet](https://en.wikipedia.org/wiki/Internet_of_things) (IoT)-enheter. Myndigheter driver försvarsplattformar, flygelektronik, styrsystem för elnät och medicinska tillsynsmyndigheter. I dessa domäner kan en programvarudefekt skada människor, stoppa en produktionslinje eller äventyra nationell säkerhet. Reglerna här är strängare, testningen svårare och standarderna rättsligt bindande. Det här kapitlet hjälper dig att bygga programvara som är korrekt, snabb, säker och trygg under verkliga begränsningar. Det hänger ihop med programvarukonstruktion (kapitel 2.9), distribuerade system (kapitel 3.3), skalbarhet och prestanda (kapitel 3.5), infrastruktur- och molnsäkerhet (kapitel 4.3) samt programvaruunderhåll (kapitel 3.7).

## Nyckelprinciper

- **Timing är ett korrekthetskrav, inte en prestandatrevlighet.** Ett sent svar kan vara ett felaktigt svar.
- **Designa för värsta fallet, inte genomsnittsfallet.** Realtidsgarantier vilar på beteende i värsta fall, inte typisk hastighet.
- **Determinism slår rå hastighet.** Ett förutsägbart system som alltid möter sin deadline slår ett snabbare som ibland missar.
- **Resurser är ändliga och fasta.** Budgetera minne, CPU-cykler och energi lika medvetet som du budgeterar pengar.
- **Säkerhet och skydd konstrueras in, de läggs inte till senare.** I reglerade domäner måste du visa ditt arbete, inte bara påstå kvalitet.
- **Hårdvaran är en del av systemet.** Du kan inte resonera om programvaran utan att resonera om chipet, sensorerna och fysiken.
- **Fältuppdateringar är en livscykelförmåga, inte en eftertanke.** Enheter ute i världen behöver ett säkert sätt att ta emot rättelser.

## Rekommendationer

### Klassificera varje timingkrav som hårt, fast eller mjukt

Alla deadlines är inte lika. En hård realtidsdeadline får aldrig missas, eftersom en miss orsakar systemfel eller skada: tänk motorstyrning eller roderytor. En fast deadline tolererar sällsynta missar, men ett sent resultat är värdelöst och kasseras. En mjuk realtidsdeadline försämrar värdet gradvis: en videobildruta som anländer lite sent sänker kvaliteten men orsakar ingen katastrof. Märk varje timingkänslig uppgift med sin klass, eftersom insats, teststringens och kostnad skiljer enormt. Två egenskaper beskriver timingbeteende. [Latens](https://en.wikipedia.org/wiki/Latency_%28engineering%29) är fördröjningen mellan en händelse och svaret. [Jitter](https://en.wikipedia.org/wiki/Jitter) är variationen i den latensen från en förekomst till nästa. Hårda realtidssystem bryr sig lika mycket om att begränsa jitter som om att sänka latens, eftersom förutsägbarhet är det som låter dig bevisa att en deadline alltid möts.

### Välj din exekveringsgrund medvetet: RTOS eller bar metall

Du har två huvudgrunder. Firmware på bar metall körs direkt på hårdvaran utan operativsystem, med en enkel loop och avbrottshanterare. Det är det minsta och mest förutsägbara alternativet och passar små enheter med ett tydligt jobb. Ett [realtidsoperativsystem](https://en.wikipedia.org/wiki/Real-time_operating_system) (RTOS) är ett litet operativsystem som schemalägger uppgifter efter prioritet och garanterar timinggränser. Det ger dig flera uppgifter, en schemaläggare och tjänster som timers och meddelandeköer, samtidigt som timingen hålls förutsägbar. Välj ett RTOS när du har flera samtidiga uppgifter med olika deadlines. Välj bar metall när enheten är mycket begränsad eller timingen måste vara bevisligen enkel. För hårt realtidsarbete, föredra en förträngande prioritetsbaserad schemaläggare och analysera den med en metod som frekvensmonoton schemaläggning (rate-monotonic scheduling), som tilldelar prioriteter efter uppgiftens frekvens och låter dig bevisa att uppgiftsmängden är schemaläggningsbar.

### Budgetera minne, CPU och effekt som förstklassiga resurser

Behandla varje knapp resurs som en budget med ett hårt tak. För minne, föredra statisk allokering framför dynamisk allokering på heapen, eftersom dynamiskt minne kan fragmenteras och kan misslyckas oförutsägbart i värsta ögonblicket. Många säkerhetsstandarder begränsar eller förbjuder heapanvändning efter uppstart av just det skälet. För CPU, mät [exekveringstid i värsta fall](https://en.wikipedia.org/wiki/Worst-case_execution_time) (WCET), den längsta tid en uppgift kan ta, och schemalägg mot det talet, inte genomsnittet. För effekt, kom ihåg att många enheter går på batteri eller skördar energi, så designa arbetscykler, viloägen och uppvakningshändelser för att nå en energibudget som måste räcka i månader eller år. Skriv ner dessa budgetar och granska dem som vilket annat krav som helst.

### Hantera avbrott och samtidighet med strikt disciplin

Ett [avbrott](https://en.wikipedia.org/wiki/Interrupt) är en hårdvarusignal som pausar det pågående arbetet för att köra en hanterare omedelbart. Avbrott är hur enheter reagerar direkt på omvärlden, och de är en stor källa till subtila buggar. Håll hanterare så korta som möjligt: kvittera händelsen, lagra minimal data och skjut det verkliga arbetet till en vanlig uppgift. Eftersom ett avbrott kan utlösas mellan två godtyckliga instruktioner måste du skydda delad data mot [kapplöpningstillstånd](https://en.wikipedia.org/wiki/Race_condition) med omsorg. Använd låsfria tekniker, korta kritiska sektioner eller väl förstådda primitiver, och skydda dig mot prioritetsinversion, där en lågprioriterad uppgift som håller ett lås blockerar en högprioriterad. Den här samtidigheten delar resonemanget i kapitel 3.3, men med snävare timing och inget utrymme för ett nytt försök.

### Skriv drivrutiner som isolerar hårdvarudetaljer

En [drivrutin](https://en.wikipedia.org/wiki/Device_driver) är det programvarulager som talar med en specifik hårdvarudel: en sensor, en radio, en motorstyrenhet. Håll hårdvaruspecifik kod bakom ett rent gränssnitt, så att resten av din programvara beror på en stabil abstraktion snarare än på registeradresser. Det gör koden testbar utanför målet, lättare att portera när ett chip tar slut och enklare att resonera om. Dokumentera varje antagande om timing, byteordning och hårdvarugrillar, eftersom det är detaljerna som orsakar fel i fält. Det här är konstruktionsdisciplinen i kapitel 2.9 tillämpad där en fel bit kan stoppa en motor.

### Anta den funktionssäkerhetsstandard som styr din domän

Om din enhet kan skada människor eller egendom gäller sannolikt en [funktionssäkerhets](https://en.wikipedia.org/wiki/Functional_safety)standard, och den är ofta lag. IEC 61508 är den allmänna standarden för säkerhet hos elektroniska system och förälder till flera andra. [ISO 26262](https://en.wikipedia.org/wiki/ISO_26262) styr säkerhet för vägfordon. [DO-178C](https://en.wikipedia.org/wiki/DO-178C) styr programvara i luftfartyg inom civil luftfart. IEC 62304 styr programvara i medicintekniska produkter. För kodning är [MISRA C](https://en.wikipedia.org/wiki/MISRA_C) en vitt använd regeluppsättning som begränsar riskabla funktioner i språket C för att göra kod säkrare och mer analyserbar. Dessa standarder kräver spårbarhet från krav till kod till test, definierade processer och belägg du kan lämna till en revisor eller tillsynsmyndighet. Anta rätt standard tidigt, eftersom att eftermontera pappersspåret senare är smärtsamt och ibland omöjligt.

### Testa med simulering och hårdvara i loopen

Du kan inte testa inbyggd programvara på det sätt du testar en webbapp. Bygg en lagerindelad strategi. Kör enhetstester på en vanlig dator mot hårdvaruabstraktionsgränssnittet. Använd simulering för att modellera enheten och dess omgivning när riktig hårdvara är knapp eller farlig att köra. Använd sedan [hårdvara-i-loopen](https://en.wikipedia.org/wiki/Hardware-in-the-loop_simulation)-testning (HIL), där den verkliga styrenheten körs mot en simulerad version av det fysiska system den styr, så att du säkert kan testa felförhållanden som en fastnad sensor eller en plötslig last. Automatisera dessa tester i din pipeline så att varje ändring kontrolleras under realistiska förhållanden innan den når en enhet.

### Designa trådlösa uppdateringar och enhetssäkerhet från dag ett

Enheter i fält kommer att behöva rättelser, så planera för trådlösa uppdateringar (OTA, over-the-air): ett sätt att leverera ny firmware säkert över ett nätverk. En säker OTA-design signerar varje uppdatering kryptografiskt, verifierar signaturen före installation, uppdaterar atomärt och kan rulla tillbaka till en känd fungerande avbild om den nya inte startar. Para detta med säkerhetsprinciperna i kapitel 4.3, anpassade för begränsad hårdvara. Använd en hårdvarubaserad förtroenderot och säker uppstart så att bara signerad firmware körs. Kryptera data under överföring och i vila. Byt standarduppgifter och stäng av oanvända gränssnitt. En IoT-flotta är ett distribuerat system med en enorm angreppsyta, och ett enda svagt standardlösenord kan äventyra miljontals enheter på en gång.

## Avvägningar: för- och nackdelar

| Val | Fördelar | Nackdelar / kostnad |
|---|---|---|
| RTOS | Multitasking, prioritetsschemaläggning, timingtjänster | Overhead, större fotavtryck, inlärningskurva |
| Bar metall | Minst, mest förutsägbart, full kontroll | Svårt att skala till många uppgifter, mer manuellt arbete |
| Statisk allokering | Förutsägbar, ingen fragmentering, säkerhetsvänlig | Mindre flexibel, allt måste dimensioneras i förväg |
| Formell säkerhetscertifiering | Laglig marknadstillgång, rigorösa belägg, högre förtroende | Stor tids- och pengakostnad, långsammare iteration |
| OTA-uppdateringar | Rätta och förbättra enheter i fält, förläng livslängden | Uppdateringsinfrastruktur, säkerhetsbörda, återrullningsrisk |

Den huvudsakliga avvägningen är mellan förutsägbarhet och flexibilitet. Allt som gör ett generellt system bekvämt (dynamiskt minne, skräpinsamling i bakgrunden, bästa-möjliga schemaläggning, elastiska resurser) motverkar garantin att en uppgift alltid blir klar i tid inom ett fast fotavtryck. Inbyggd och realtidsteknik ger medvetet upp flexibilitet för att köpa determinism och säkerhet. Konsten är att spendera den avvägningen bara där deadlinen eller risken verkligen kräver det, och att hålla de flexibla, snabbrörliga delarna (som en enhets molnbackend) på andra sidan en ren gräns.

## Frågor att diskutera med ditt team

1. **Mäter ni jitter, eller bara genomsnittlig latens, på era timingkritiska vägar?** Hård realtidskorrekthet vilar på att begränsa variationen i svarstid (jitter), inte bara på att sänka den typiska latensen, eftersom förutsägbarhet är det som låter er bevisa att en deadline alltid möts. En reglerloop med lågt genomsnitt men tillfälliga stora toppar kan ändå missa sin deadline och orsaka skada, och genomsnittet döljer det. Ta med mätningar av spridningen, värsta fallet inkluderat, för varje timingkritisk uppgift, och märk var och en som hård, fast eller mjuk så att teststringensen matchar konsekvensen av en miss. Allt bekvämt i generella system (dynamiskt minne, skräpinsamling, bästa-möjliga schemaläggning) angriper förutsägbarheten, så det stannar utanför den hårda vägen. Om ni bara rapporterar genomsnitt kan ni inte ärligt påstå att en hård deadline möts.

2. **Är ert val mellan RTOS och bar metall fortfarande rätt, och kan ni bevisa att uppgiftsmängden är schemaläggningsbar?** Exekveringsgrunden är ett beslut att ompröva när enheten växer: bar metall är minst och mest förutsägbart för ett tydligt jobb, medan ett RTOS förtjänar sin overhead när ni har flera samtidiga uppgifter med olika deadlines. För hårt realtidsarbete pekar kapitlet på en förträngande prioritetsbaserad schemaläggare analyserad med en metod som frekvensmonoton schemaläggning, vilket låter er bevisa att uppgifterna ryms i stället för att hoppas. Ta med den nuvarande uppgiftsmängden, deras frekvenser och deras exekveringstider i värsta fall, och kontrollera om schemaläggningsbarheten faktiskt håller eller om uppgifter i det tysta har ackumulerats förbi vad grunden kan garantera. Skydda er mot prioritetsinversion, där en lågprioriterad uppgift som håller ett lås stoppar en högprioriterad. Att välja grund av vana snarare än efter uppgiftsmängden är hur timinggarantier i det tysta eroderar.

3. **Var går exakt gränsen mellan den deterministiska enheten och den flexibla molnbackenden, och är den ren nog att röra sig snabbt på ena sidan utan att äventyra den andra?** Kapitlets huvudavvägning ger upp flexibilitet för att köpa determinism och säkerhet, och konsten är att spendera den avvägningen bara där deadlinen eller risken verkligen kräver det. En ren gräns låter den säkerhetskritiska firmwaren förbli konservativ och certifierad medan molnbackenden itererar snabbt, så att de två utvecklas i sin egen säkra takt. Ta med er arkitektur och lokalisera den sömmen: vad som måste bevisas deterministiskt och uppdateras via en signerad, verifierad väg, mot vad som kan ändras varje vecka på servern. Att sudda ut gränsen drar molnvanor (dynamisk allokering, bästa-möjliga timing) in i styrvägen, eller bromsar i onödan backenden till firmwarens takt. Att få gränsen rätt är det som håller både säkerhetsbeläggen och leveranshastigheten intakta.

4. **Vilken funktionssäkerhetsstandard styr varje produkt, och hur långt är nuvarande belägg från vad en revisor skulle acceptera?** Standarden (IEC 61508, ISO 26262 för vägfordon, DO-178C för luftburen programvara, IEC 62304 för medicintekniska produkter) är ofta lag, och den kräver spårbarhet från krav till kod till test som ni inte kan fejka i slutet. För ett stort team är risken att grupper antar pappersspåret ojämnt, så att en produktlinje är revisionsklar medan en annan halvvägs genom certifieringen upptäcker att dess krav aldrig spårats. Det motstridiga draget är hastighet: full spårbarhet och MISRA C-efterlevnad bromsar den dagliga iterationen, och ett team under deadlinetryck frestas skjuta beläggen till "senare". Ta med den nuvarande spårbarhetsmatrisen, de statiska analysfynd som fortfarande är öppna och en ärlig luckanalys mot målnivån för säkerhetssäkring. I företags- och myndighetssammanhang, lägg till certifieringens ledtid och revisorns förväntningar, eftersom att eftermontera belägg efter designen är långsamt, kostsamt och ibland omöjligt, och en försenad certifiering kan blockera marknadstillträdet helt.

5. **Om en allvarlig defekt hittades i en enhet i fält i morgon, hur snabbt kunde ni rätta den säkert över hela flottan, och har ni övat återrullningen?** En enhet ni inte kan patcha blir en permanent säkerhets- och skyddsskuld, och en fysisk återkallelse kostar storleksordningar mer än en signerad trådlös uppdatering. Spänningen är att en slarvig uppdateringsmekanism i sig är en angreppsyta och en risk för att göra enheter obrukbara: en OTA-väg som installerar osignerade avbilder, eller som inte kan rulla tillbaka en dålig uppstart, kan förvandla en dålig release till miljontals döda enheter. Ta med er uppdateringsdesign (kryptografisk signering, signaturverifiering före installation, atomär installation, automatisk återrullning till en känd fungerande avbild), status för säker uppstart och hårdvarubaserad förtroenderot och senaste gången någon faktiskt övade en återrullning på riktig hårdvara. För en företags- eller offentlig flotta, lägg till vem som är ansvarig för signeringsnycklarna och hur ni skulle återkalla en komprometterad, eftersom en läckt nyckel eller en delad standarduppgift kan äventyra hela flottan på en gång.

6. **Är era minnes-, CPU- och effektbudgetar nedskrivna med hårda tak, och övar er teststrategi både simulering och riktig hårdvara?** Realtidsgarantier vilar på exekveringstid i värsta fall och ett fast resursfotavtryck, inte genomsnittligt beteende, så en obudgeterad heapallokering eller en otestad värstafallslast är där determinismen i det tysta eroderar. För ett stort team är faran drift: uppgifter ackumuleras, minnet kryper uppåt och ingen äger budgeten förrän en enhet fallerar i fält efter veckor av drifttid. Avvägningen är täckning mot kostnad, eftersom en hårdvara-i-loopen-rigg som injicerar fel som en fastnad sensor är dyr att bygga, medan ren simulering döljer timingbuggar som bara visar sig på det riktiga chipet. Ta med de dokumenterade budgetarna, de uppmätta exekveringstiderna i värsta fall mot dem och belägg för att er pipeline kör enhetstester på abstraktionslagret, simulering och hårdvara-i-loopen före en release. I reglerade och offentliga miljöer, knyt detta till den strukturella testtäckning standarden kräver, eftersom en revisor vill ha bevis på att felförhållanden övades, inte en försäkran om att genomsnittsfallet såg bra ut.

## Sektorsperspektiv

**Startup.** Hastighet och överlevnad dominerar, så välj ett lätt RTOS eller en enkel loop på bar metall, förbjud dynamisk allokering efter uppstart och mät värstafallstiden för din enda kritiska loop i stället för att jaga en certifieringsbudget du inte har. Hoppa över formella funktionssäkerhetsprocesser om inte din marknad tvingar fram dem, men hoppa aldrig över signerade trådlösa uppdateringar med automatisk återrullning: ett ungt företag överlever inte en återkallelse i fält, och en fjärrrättelse är skillnaden mellan en dålig natt och en död produkt. Håll enhetens firmware liten och konservativ så att dina knappa ingenjörer inte underhåller en pipeline de inte har råd med.

**Småföretag.** Utan inbyggd specialist i personalen, lita på beprövade moduler, referensdesigner och leverantörers RTOS-distributioner snarare än att rulla en egen schemaläggare eller starthanterare. Rama in valet köp mot bygg kring vem som ska patcha enheten under det kommande decenniet: en köpt säkerhets- och uppdateringsstack du kan lita på slår en skräddarsydd som ingen kvarvarande kan underhålla. Behandla standardlösenord, öppna felsökningsgränssnitt och osignerade uppdateringar som de fel som troligast skadar dig, eftersom de är billiga att förebygga och ödesdigra att upptäcka i fält.

**Storföretag.** Problemet är enhetlighet över många produktlinjer och team: en gemensam policy för exekveringsgrund, gemensamma mallar för resursbudgetar, upprätthållen MISRA C och statisk analys samt en certifierad plattform för trådlösa uppdateringar och säker uppstart så att varje grupp inte uppfinner den på nytt. Budgetera funktionssäkerhets- och hårdvara-i-loopen-bördan uttryckligen, standardisera hårdvaruabstraktionsgränssnittet så att ett chip som tar slut inte strandsätter en produkt och hantera flottans timingbelägg, säkerhetsartefakter och skyddsläge som styrda tillgångar snarare än folklore per team. En enda svag standarduppgift över flottan är en skuld i företagsskala, så centralisera hanteringen av uppgifter och nycklar.

**Offentlig sektor.** Upphandlingsregler, transparens och offentlig ansvarsskyldighet formar varje val. Kräv att leverantörer utvecklar luftburen, medicinsk eller försvarsprogramvara enligt den styrande standarden (DO-178C, IEC 62304, IEC 61508) på den säkringsnivå som matchar faran, och att de överlämnar spårbarhets- och strukturtäckningsbelägg som revisorer granskar. Kräv säker uppstart, en hårdvarubaserad förtroenderot och en kontrollerad, signerad fältuppdateringsprocess, eftersom en overifierad uppdatering av ett flyg- eller elnätssystem är oacceptabel. Föredra avtal som ger rätt till källkod, säkerhetsartefakter och möjlighet att omcertifiera med en andra leverantör, så att en leverantör som går i konkurs inte strandsätter ett system allmänheten är beroende av i decennier.

## Exempel

**Startup.** En liten hårdvarustartup som bygger en batteridriven luftkvalitetsmätare skriver sin firmware mot ett lätt RTOS med en fast uppsättning uppgifter och ingen dynamisk allokering efter uppstart, så att enheten som levereras är den som körs i åratal på ett knappcellsbatteri. Även utan certifieringsbudget mäter teamet värstafallstiden för sin sensoravläsningsloop och testar enheten mot injicerade felförhållanden på en bänkrigg före varje release. Signerade trådlösa uppdateringar med automatisk återrullning låter dem rätta en defekt över varje levererad enhet, så att en felaktig avläsning i fält inte betyder en återkallelse som det unga företaget inte skulle överleva.

**Storföretag.** En tillverkare av uppkopplade fordon bygger en elektronisk bromsstyrenhet. Den hårda realtidsstyrloopen körs på ett RTOS med frekvensmonoton schemaläggning och statiskt minne, och varje uppgift bär en uppmätt exekveringstid i värsta fall. Teamet utvecklar enligt ISO 26262 med full spårbarhet från krav till kod till test och upprätthåller MISRA C med statisk analys vid varje incheckning. En hårdvara-i-loopen-rigg spelar upp tusentals vägscenarier, inklusive injicerade sensorfel, innan någon firmware levereras. Signerade OTA-uppdateringar låter företaget rätta en defekt över hela flottan utan en kostsam återkallelse, med automatisk återrullning om en bil inte startar den nya avbilden.

**Offentlig sektor.** En nationell luftfartsmyndighet certifierar en ny flygledningsdator. Leverantören utvecklar den luftburna programvaran enligt DO-178C på den säkringsnivå som matchar faran och producerar belägg för kravtäckning och strukturell testtäckning som revisorer granskar. Timingen bevisas deterministisk under värstafallslast, med begränsad avbrottslatens och ingen dynamisk allokering efter uppstart. Säker uppstart och en hårdvarubaserad förtroenderot säkerställer att bara signerad, certifierad firmware körs. Fältuppdateringar följer en kontrollerad, signerad process, eftersom en overifierad uppdatering av ett flygsystem är oacceptabel.

## Affärsnytta: motiv, ROI och TCO

Affärsärendet domineras av kostnaden för fel och kostnaden för marknadstillträde. I reglerade domäner kan du inte sälja produkten alls utan säkerhetscertifieringen, så processkostnaden är helt enkelt inträdesbiljetten. Utöver det är defekter i hårdvara i fält extraordinärt dyra: en fysisk återkallelse kostar långt mer än en molnrättelse, och en säkerhetshändelse bär ansvar, regulatoriska viten och anseendeskada som kan avsluta en produktlinje. Att bygga in säkerhet, determinism och uppdateringsbarhet från start är billigt jämfört med att upptäcka deras frånvaro i fält.

Rama in avkastningen kring undvikna återkallelser, snabbare certifiering och längre enhetslivslängd. En robust OTA-förmåga omvandlar många tänkbara återkallelser till billiga fjärrrättelser, och varje undviken återkallelse kan betala för hela uppdateringsprogrammet. Rigorös WCET-analys och resursbudgetering låter dig leverera på billigare hårdvara med tillförsikt, vilket sänker kostnaden per enhet över en stor flotta. För total ägandekostnad, kom ihåg att dessa enheter lever i år eller decennier: underhålls-, säkerhetspatchnings- och supportbördan (kapitel 3.7) överskuggar det första bygget. Att designa för uppdateringsbarhet, tydlig hårdvaruabstraktion och dokumenterade budgetar är det som håller den långa svansen prisvärd.

## Antimönster och fallgropar

- **Att optimera för genomsnittsfallet.** Att möta deadlinen "vanligtvis" är att misslyckas med ett hårt realtidskrav.
- **Dynamisk allokering i styrvägen.** Heapfragmentering orsakar ett fel som bara visar sig efter veckors drifttid.
- **Feta avbrottshanterare.** Att lägga tung bearbetning inuti ett avbrott spräcker din timingbudget och skapar kapplöpningstillstånd.
- **Att ignorera standarden till revisionen.** Att eftermontera spårbarhet och belägg sent är långsamt, kostsamt och ibland omöjligt.
- **Att leverera utan uppdateringsväg.** En enhet du inte kan patcha blir en permanent säkerhets- och skyddsskuld.
- **Standardlösenord och öppna gränssnitt.** En enda svag uppgift förvandlar en IoT-flotta till ett botnät.
- **Att testa bara på en simulator eller bara på hårdvara.** Var och en döljer buggar som den andra skulle fånga. Du behöver båda.
- **Att behandla hårdvaran som någon annans problem.** Timing, byteordning och sensorgrillar är programvarufrågor här.

## Mognadsmodell

- **Nivå 1: Initiera.** Timing hoppas på, inte analyseras. Minne allokeras dynamiskt efter behag. Ingen funktionssäkerhetsstandard följs. Testning är manuell och enbart på enheten. Enheter kan inte uppdateras efter leverans, så en defekt i fält betyder en återkallelse eller en permanent skuld.
- **Nivå 2: Utveckla.** Vissa uppgifter har uppmätt timing och ett grundläggande RTOS eller en strukturerad loop finns, men praxis varierar team för team. Kodriktlinjer finns men upprätthålls inte. Testning inkluderar viss simulering. En manuell, riskabel uppdateringsväg finns på vissa produkter men inte andra. Goda vanor finns men är inkonsekventa, och inget garanterar att nästa produktlinje ärver dem.
- **Nivå 3: Standardisera.** Timingkrav klassificeras som hårda, fasta eller mjuka och analyseras med exekveringstid i värsta fall och en schemaläggningsmetod, dokumenterat och upprätthållet i hela organisationen. Resursbudgetar för minne, CPU och effekt är nedskrivna med hårda tak. Den styrande funktionssäkerhetsstandarden följs med spårbarhet från krav till kod till test, och MISRA C eller motsvarande upprätthålls av statisk analys vid varje incheckning. Hårdvara-i-loopen-testning körs i pipelinen. Signerade, atomära trådlösa uppdateringar med återrullning och säker uppstart är den krävda baslinjen överallt.
- **Nivå 4: Hantera.** Organisationen mäter och styr sin inbyggda egendom mot utgångslägen. Den följer marginaler för exekveringstid i värsta fall, jitterfördelningar, andel missade deadlines, minnes- och effektutrymme, öppna fynd från statisk analys, täckning av certifieringsbelägg samt framgångs- och återrullningsfrekvens för trådlösa uppdateringar, och jämför dem med överenskomna mål. Drift mot en resurs- eller timingbudget utlöser åtgärd innan en enhet fallerar i fält, och beslut att släppa eller inte vilar på dessa data snarare än på bedömning i stunden. Chefer kan se vilka produktlinjer som är revisionsklara och vilka som är på väg mot en missad deadline eller en spräckt budget.
- **Nivå 5: Orkestrera.** Determinism, säkerhetsbelägg och skydd verifieras kontinuerligt och automatiskt. Felinjicering och hårdvara-i-loopen körs vid varje ändring, och certifieringsartefakter genereras som en biprodukt av processen. Flottan övervakas, patchas och uppdateras säkert i stor skala under en lång driftlivslängd. Organisationen anpassar sina exekveringsgrunder, resursbudgetar och standardantagande när chip tar slut, hot utvecklas och regleringar ändras, och omfördelar hela enhetsportföljen på belägg snarare än att reagera på varje kris för sig.

## Idéer för diskussion

1. Vilka av din enhets uppgifter är verkligt hårda realtid, och kan du bevisa att var och en alltid möter sin deadline?
2. Känner du till exekveringstiden i värsta fall för din kritiska styrloop, eller bara dess genomsnitt?
3. Vilken funktionssäkerhetsstandard styr din produkt, och hur långt är dina nuvarande belägg från vad den kräver?
4. Om en allvarlig defekt hittades i en enhet i fält i morgon, hur skulle ni rätta den, och hur snabbt?
5. Var finns dynamisk minnesallokering fortfarande kvar i din styrväg, och vad händer om den misslyckas vid timme 1000?
6. Hur skulle din IoT-flotta klara en angripare som hittade en enda delad standarduppgift?

## Viktigaste punkter

- Inbyggd programvara körs på begränsad hårdvara, och realtidskorrekthet beror på timing, inte bara på rätt svar.
- Klassificera varje deadline som hård, fast eller mjuk, och designa för timing i värsta fall, begränsat jitter och determinism framför rå hastighet.
- Välj RTOS eller bar metall medvetet, och budgetera minne, CPU och effekt som fasta, förstklassiga resurser.
- Håll avbrottshanterare små, skydda delad data och isolera hårdvara bakom rena, testbara drivrutinsgränssnitt.
- Anta tidigt den funktionssäkerhetsstandard din domän kräver (IEC 61508, ISO 26262, DO-178C, IEC 62304, MISRA C), med full spårbarhet.
- Testa med simulering och hårdvara i loopen, och bygg säkra, signerade, återrullningsbara OTA-uppdateringar och enhetssäkerhet från dag ett.

## Referenser och vidare läsning

- IEC 61508, *Functional Safety of Electrical/Electronic/Programmable Electronic Safety-related Systems*
- ISO 26262, *Road Vehicles: Functional Safety*
- RTCA DO-178C, *Software Considerations in Airborne Systems and Equipment Certification*
- IEC 62304, *Medical Device Software: Software Life Cycle Processes*
- MISRA, *MISRA C: Guidelines for the Use of the C Language in Critical Systems*
- Michael Barr and Anthony Massa, *Programming Embedded Systems*
- Elecia White, *Making Embedded Systems*
- Jane W. S. Liu, *Real-Time Systems*
- Giorgio Buttazzo, *Hard Real-Time Computing Systems: Predictable Scheduling Algorithms and Applications*
- Colin Walls, *Embedded Software: The Works*
- Philip Koopman, *Better Embedded System Software*
- OWASP Internet of Things (IoT) security guidance
