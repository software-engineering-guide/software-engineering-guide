# 5.3 Tillgänglighet

## Översikt och motivation

[Tillgänglighet](https://en.wikipedia.org/wiki/Accessibility) (ofta förkortat "a11y") är praxisen att bygga programvara som människor med funktionsnedsättning kan uppfatta, förstå, navigera i och använda. Det omfattar människor som är blinda eller har nedsatt syn, som är döva eller hörselskadade, som har motoriska nedsättningar, som har kognitiva eller inlärningsmässiga skillnader och som möter tillfälliga eller situationsbundna begränsningar som en bruten arm, starkt solljus eller ett bullrigt rum. Ungefär var femte människa har en funktionsnedsättning, och alla drar nytta av tillgänglig design någon gång. Det här är inte en nischad anpassning. Det är en kvalitetsbaslinje.

För stora team måste tillgänglighet byggas in i systemet, inte överlåtas åt enskilda goda avsikter. När många team levererar in i en produkt kan en enda otillgänglig komponent (ett oetiketterat formulärfält, en färgenbart statusindikator, en tangentbordsfälla i en modal) stänga ute användare med funktionsnedsättning från en hel resa. Att bygga in tillgänglighet i gemensamma komponenter, designtokens, testpipelines och definitioner av färdig är det enda sättet att göra den pålitlig i skala. Att eftermontera den i efterhand är dyrt och felbenäget. Att designa in den är billigt och varaktigt.

För myndigheter är tillgänglighet ett rättsligt krav och en medborgerlig skyldighet, inte en trevlighet. Offentliga tjänster måste betjäna varje medlem av allmänheten, och medborgare med funktionsnedsättning har ofta ingen alternativ leverantör: om myndighetens webbplats är otillgänglig kan de inte få sitt bidrag, sitt tillstånd eller sin röst avgiven på något annat sätt. Lagar och standarder världen över gör tillgänglighet obligatorisk för offentliga organ, och alltmer för den privata sektorn också. Det här kapitlet behandlar tillgänglighet som tre saker på en gång: en rättslig plikt, en etisk plikt och helt enkelt god design.

*Se även:* kapitel 5.2 (UI-design och designsystem), kapitel 5.6 (frontendteknik) och kapitel 5.1 (UX-grunder).

## Nyckelprinciper

- Tillgänglighet är en grundläggande kvalitetsegenskap, som säkerhet och prestanda, inte en valfri funktion.
- POUR-principerna: gränssnitt måste vara Perceivable (uppfattbara), Operable (hanterbara), Understandable (begripliga) och Robust (robusta).
- [Semantisk HTML](https://en.wikipedia.org/wiki/Semantic_HTML) först. Använd [ARIA](https://en.wikipedia.org/wiki/WAI-ARIA) bara för att fylla genuina luckor, aldrig som ersättning för inbyggda element.
- Allt som går att använda med en mus måste gå att använda med enbart tangentbord.
- Förmedla inte information enbart genom färg, form eller position.
- Automatiska verktyg fångar bara en bråkdel av problemen. Manuell testning och testning med [hjälpmedel](https://en.wikipedia.org/wiki/Assistive_technology) är nödvändig.
- Tillgänglig design är bättre design för alla (["trottoarkanteffekten"](https://en.wikipedia.org/wiki/Curb_cut), där funktioner byggda för människor med funktionsnedsättning gynnar alla användare).
- Designa och testa med människor med funktionsnedsättning, inte bara för dem.

## Rekommendationer

### Designa och bygg enligt WCAG, med den aktuella standarden som mål

[Web Content Accessibility Guidelines](https://en.wikipedia.org/wiki/Web_Content_Accessibility_Guidelines) (WCAG) är den internationella referensen. WCAG 2.1 och 2.2 är organiserade under de fyra POUR-principerna, med testbara framgångskriterier på överensstämmelsenivåerna A, AA och AAA. Sikta på nivå AA som din baslinje. Det är den de flesta lagar hänvisar till. WCAG 2.2 lägger till kriterier för fokussynlighet, målstorlek och minskad kognitiv belastning. WCAG 3.0 är en framväxande efterföljare, strukturerad annorlunda och fortfarande under utveckling. Bevaka den, men bygg mot 2.2 AA i dag. Behandla riktlinjerna som ett golv, inte ett tak: att klara varje kriterium garanterar inte en genuint användbar upplevelse.

### Använd semantisk HTML och korrekt ARIA

Inbyggda HTML-element (knappar, länkar, formulärkontroller, rubriker, listor, landmärken) kommer med inbyggd tillgänglighetssemantik, tangentbordsbeteende och stöd för hjälpmedel. Använd dem först. Sträck dig efter ARIA-roller (Accessible Rich Internet Applications), tillstånd och egenskaper bara för att beskriva egna widgetar som HTML inte kan uttrycka, och följ ARIA Authoring Practices. Den första regeln för ARIA är enkel: använd inte ARIA om ett inbyggt element duger. Felaktig ARIA är värre än ingen: den vilseleder aktivt [skärmläsare](https://en.wikipedia.org/wiki/Screen_reader). Ge sidan en logisk rubrikstruktur, meningsfulla etiketter, alternativ text för bilder, textning och transkript för media och en programmatisk koppling mellan varje etikett och dess kontroll.

### Garantera hantering med tangentbord och hjälpmedel

Varje interaktivt element måste gå att nå och hantera med enbart tangentbord, i logisk ordning, med en tydligt synlig fokusindikator. Undvik tangentbordsfällor. Hantera fokus medvetet när innehåll ändras: flytta fokus till en dialog när den öppnas, återför det när dialogen stängs och annonsera dynamiska uppdateringar genom live-regioner. Testa med verkliga hjälpmedel, inklusive skärmläsare på dator och mobil, skärmförstoring, röststyrning och brytarstyrning. Och respektera användarpreferenser som minskad rörelse och ökad kontrast.

### Testa med automatiska verktyg, manuell granskning och verkliga användare

Automatiska tillgänglighetsskannrar är värdefulla, och de bör köras i pipelinen vid varje ändring. Men studier visar konsekvent att de fångar bara en minoritet av verkliga problem, ungefär en tredjedel. Resten kräver mänskligt omdöme: tangentbordsgenomgångar, skärmläsartestning, kontrastkontroller och att fråga om innehållet faktiskt är begripligt. Viktigast av allt, inkludera människor med funktionsnedsättning i användbarhetstestning. Bygg in tillgänglighetsacceptanskriterier i definitionen av färdig så att problem fångas per berättelse snarare än i en revision före lansering.

### Gör tillgänglighet organisatorisk, inte heroisk

Baka in tillgänglighet i designsystemet så att komponenter levereras tillgängliga som standard. Erbjud utbildning så att designers, ingenjörer, innehållsskribenter och produktansvariga var och en vet vad de ansvarar för. Etablera en tillgänglighetsstandard, en ägare eller ett kompetenscentrum och en åtgärdsprocess. Publicera en tillgänglighetsredogörelse och ge användare ett sätt att rapportera hinder. Och upphandla tillgängligt: kräv att leverantörer och tredjepartskomponenter uppfyller kraven och att de tillhandahåller belägg (som en tillgänglighetsrapport).

## Avvägningar: för- och nackdelar

| Tillvägagångssätt | Fördelar | Nackdelar |
|---|---|---|
| Bygg in tillgänglighet från start | Billigast, varaktigt, bättre för alla | Kräver utbildning och disciplin i förväg |
| Eftermontera / åtgärda senare | Skjuter upp insats, frigör en snabb lansering | Långt dyrare, skört, rättslig exponering under tiden |
| Enbart automatisk testning | Snabb, billig, fångar regressioner i CI | Missar ~två tredjedelar av problemen. Falsk tillförsikt |
| Manuell testning + testning med hjälpmedel | Fångar verkliga användbarhetshinder | Långsammare, kräver skickliga testare och enheter |
| Testning med användare med funktionsnedsättning | Grundsanning om verklig upplevelse | Rekryteringsinsats och kostnad, måste göras respektfullt |

Den centrala avvägningen är disciplin i förväg mot uppskjuten kostnad. Tillgänglighet som byggs in är billig och förbättrar kvaliteten för alla. Tillgänglighet som eftermonteras under rättsligt tryck är dyr, ofullständig och stressande. På lång sikt finns ingen verklig avvägning mot "hastighet": otillgänglig programvara fungerar helt enkelt inte för en femtedel av dina användare. Det är en defekt, inte en besparing.

## Frågor att diskutera med ditt team

1. **Fäller tillgänglighetsregressioner vårt bygge på samma sätt som ett trasigt test gör, och om inte, varför inte?** Automatiska skannrar fångar bara ungefär en tredjedel av problemen, men de som de fångar (saknade etiketter, kontrastfel, oetiketterade kontroller) är billiga att fånga i CI och dyra att hitta i en revision före lansering. Att behandla en regression som ett byggfel är vad som flyttar tillgänglighet från heroisk individuell insats till en pålitlig systemegenskap, vilket är det enda som fungerar när många team levererar in i en produkt. Besluta vilka kontroller som är blockerande, vilka som är rådgivande och vem som kan åsidosätta ett fel. Ta med era nuvarande skannerresultat och er definition av färdig till mötet. Om tillgänglighetskriterier inte är nedskrivna i definitionen av färdig per berättelse kommer de att nedprioriteras i samma stund en deadline stramas åt.

2. **Vilken är vår regel för egna widgetar, och vem granskar ARIA innan den levereras?** Inbyggda HTML-element kommer med tangentbordsbeteende och stöd för hjälpmedel gratis, och felaktig ARIA är värre än ingen eftersom den aktivt vilseleder skärmläsare. Kom överens om att semantisk HTML är standard och att varje egen widget (en skräddarsydd rullgardinsmeny, datumväljare eller modal) kräver en genomgång med tangentbord och skärmläsare före sammanslagning, enligt ARIA Authoring Practices. Detta spelar störst roll för de interaktiva komponenter många team återanvänder, eftersom en trasig modal med en tangentbordsfälla kan stänga ute användare med funktionsnedsättning från en hel resa. Ta med en lista över era egna widgetar och fråga vilka som har testats med en faktisk skärmläsare. Alla som inte har det är skulder som gömmer sig i gemensam kod.

3. **Vilken är vår policy för tillgänglighetsöverlägg, och tror någon att de är en verklig lösning?** Överlägg marknadsförs som ett skript på en rad som gör en webbplats överensstämmande, och de är frestande när rättsligt tryck anländer och en deadline hotar. De levererar inte genuin överensstämmelse, de kan försämra upplevelsen för användare av hjälpmedel och för myndigheter lämnar de den underliggande rättsliga plikten ouppfylld. Besluta uttryckligen att ni ska investera i semantisk märkning, tangentbordsstöd och testning med människor med funktionsnedsättning snarare än köpa en widget som breder över problemet. Ta med kostnaden för en prenumeration på ett överlägg och jämför den med att bygga in tillgänglighet i era komponenter och er pipeline en gång. Att ramma in detta tidigt förhindrar ett panikslaget upphandlingsbeslut senare som spenderar pengar och rättar ingenting.

4. **Är människor med funktionsnedsättning en del av vår design och testning, eller designar vi fortfarande för en inbillad användare vi har hittat på?** Automatiska skannrar och till och med expertrevisioner talar om huruvida märkning överensstämmer. De talar inte om huruvida en blind användare faktiskt kan slutföra er kassa eller en person med kognitiv funktionsnedsättning kan förstå era felmeddelanden. Att involvera deltagare med funktionsnedsättning är den enda källan till grundsanning, och det ändrar vad ni bygger, men det väcker verkliga frågor om hur ni rekryterar rättvist, hur ni ersätter människor för deras tid och hur ni undviker att behandla en deltagare som talesperson för varje funktionsnedsättning. Ta med er nuvarande forskningslista, era rekryterings- och betalningspraxis och ett ärligt antal på hur många studier det senaste året som inkluderade deltagare med funktionsnedsättning. För en stor organisation är en återkommande panel med rättvis ersättning och täckning över syn-, hörsel-, motoriska och kognitiva behov det som förvandlar detta från en engångsgest till en pålitlig indata. I myndigheter är det att involvera allmänheten ni tjänar ofta en del av den rättsliga och medborgerliga skyldigheten, inte en valfri trevlighet.

5. **När vi köper eller bäddar in en tredjepartskomponent, kräver vi bevis på tillgänglighet, och vem kontrollerar det?** Mycket av det som levereras i en stor produkt är inte skrivet internt: en datumväljare från ett bibliotek, en betalningswidget i en iframe, ett diagrampaket, en hel SaaS-modul. En enda otillgänglig inbäddad komponent kan fälla en hel resa oavsett hur ren er egen kod är, och när den väl är inkopplad är det dyrt att byta ut den. Besluta att tillgänglighet är ett upphandlingskrav, att leverantörer måste lämna en tillgänglighetsrapport (ett dokument som en VPAT som anger hur en produkt mäter sig mot WCAG) och att någon teknisk validerar påståendet snarare än arkiverar det. Ta med en inventering av era tredjepartskomponenter och fråga vilka som har aktuella, trovärdiga belägg för överensstämmelse. I företags- och myndighetsupphandling, skriv in WCAG 2.2 AA-överensstämmelse och en rätt till åtgärd i avtalet, eftersom ett löfte givet före undertecknande är långt billigare att driva igenom än ett hinder som upptäcks efter driftstart.

6. **Vilken är vår målnivå för överensstämmelse, vem äger den och hur håller vi den aktuell när standarder rör sig?** WCAG 2.2 AA är dagens golv och de flesta lagar hänvisar till det, men 2.2 lade till kriterier många team inte har antagit, och WCAG 3.0 är på väg med en annan struktur. Utan en namngiven ägare driver standarden: olika team siktar på olika versioner, ingen följer klyftan och överensstämmelsen ruttnar i tysthet mellan revisioner. Besluta den exakta version och nivå ni bygger mot, vem som har befogenhet att höja den och hur nya kriterier når designsystemet och definitionen av färdig. Ta med ert nuvarande uttalade mål, belägg för var team faktiskt uppfyller det och en kort färdplan för att anta de 2.2-kriterier ni hoppat över. För en stor eller offentlig organisation är en tillgänglighetsägare eller ett kompetenscentrum, en publicerad tillgänglighetsredogörelse och en dokumenterad plan för nästa standardversion det som låter er svara en tillsynsmyndighet eller en domstol med belägg snarare än goda avsikter.

## Sektorsperspektiv

**Startup.** Hastighet gynnar dig här, eftersom tillgänglighet är billigast när kodbasen är liten. Lägg till en automatisk skanner i CI och en tangentbordsgenomgång i din checklista för pull requests från första sprinten och lita på semantisk HTML så att du får tangentbords- och skärmläsarstöd gratis. Hoppa över överlägg och tunga verktyg. Utdelningen är att när en kunds upphandlingsteam ber om en överensstämmelserapport mitt i en försäljning kan du svara på dagar i stället för att kapplöpa.

**Småföretag.** Utan tillgänglighetsspecialist och med snäv budget, köp tillgänglighet snarare än bygg den: välj en plattform, ett tema eller ett komponentbibliotek som redan överensstämmer och säger det, och föredra leverantörer som publicerar en tillgänglighetsredogörelse. Täck de högvärdiga grunderna själv med gratisverktyg, kontroller med enbart tangentbord, en kontrastkontroll och tydliga etiketter på varje fält, eftersom de fångar de fel som oftast utesluter kunder. Behandla ett felaktigt eller oanvändbart automatiskt flöde som en förlorad kund, eftersom ett litet företag sällan erbjuder en assisterad kanal att falla tillbaka på.

**Storföretag.** I skala är arbetet att göra tillgänglighet till en systemegenskap över många team. Leverera tillgängliga komponenter som standard i designsystemet, grinda regressioner i CI och res en ägare eller ett kompetenscentrum med en åtgärdsprocess och utbildning för designers, ingenjörer och innehållsskribenter. Följ överensstämmelse över tid som ett mått, skriv in WCAG-överensstämmelse i upphandling och hantera tredjepartskomponenter som en portfölj så att en inbäddad widget inte i tysthet kan fälla en gemensam resa.

**Offentlig sektor.** Tillgänglighet är ett rättsligt krav och en medborgerlig plikt, eftersom medborgare med funktionsnedsättning ofta saknar alternativ leverantör för ett bidrag, ett tillstånd eller en röst. Bygg mot den standard din jurisdiktion hänvisar till (till exempel Section 508, EN 301 549 eller den europeiska tillgänglighetsakten mappad till WCAG 2.2 AA), publicera en tillgänglighetsredogörelse med en väg att rapportera hinder och testa med den allmänhet med funktionsnedsättning ni tjänar. Avvisa överlägg som ersättning för verklig överensstämmelse och kräv att leverantörer lämnar trovärdiga belägg och en rätt till åtgärd i avtalet.

## Exempel

**Startup.** En startup på tre personer som byggde ett rekryteringsverktyg lade till en tillgänglighetsskanner i sitt bygge och en snabb tangentbordsgenomgång i sin checklista för pull requests redan från första sprinten, med resonemanget att det var billigare att förbli tillgängliga än att rätta senare. När en medelstor kunds upphandlingsteam bad om en tillgänglighetsrapport under en säljcykel använde startupen redan semantisk HTML, etiketterade varje fält och hade synligt fokus överallt, så de svarade på dagar i stället för att kapplöpa. Den beredskapen vann en affär som en konkurrent förlorade på samma krav.

**Storföretag.** En stor detaljhandlare mötte en grupptalan eftersom blinda kunder inte kunde slutföra kassan med en skärmläsare. Utöver förlikningen och de juridiska avgifterna måste företaget åtgärda under en domstolsövervakad tidslinje. Efteråt byggde det om tillgänglighet i sitt designsystem och sin CI-pipeline, lade till skärmläsartestning i definitionen av färdig och utbildade sina team. Den ombyggda, tillgängliga kassan förbättrade också konverteringen och minskade supportkontakter för alla: rättelserna som hjälpte användare av skärmläsare (tydliga etiketter, felmeddelanden, logisk ordning) hjälpte alla användare.

**Offentlig sektor.** En bidragsmyndighet var rättsligt skyldig att uppfylla WCAG 2.1 AA för sin onlineansökan. Tidig testning med blinda och synsvaga användare, användare med enbart tangentbord och användare med kognitiva funktionsnedsättningar avslöjade att en färgenbart indikator för "obligatoriskt fält", en otillgänglig datumväljare och oannonserade valideringsfel hindrade människor från att slutföra. Att rätta dessa, genom semantisk märkning, synligt fokus, felannonseringar i live-regioner och hjälp i [klarspråk](https://en.wikipedia.org/wiki/Plain_language), lät medborgare med funktionsnedsättning ansöka på egen hand för första gången. Det minskade beroendet av hjälp på plats och sänkte kostnaden att betjäna, samtidigt som det rättsliga kravet uppfylldes.

## Affärsnytta: motiv, ROI och TCO

Affärsärendet vilar på marknadsräckvidd, rättslig risk, kostnad att betjäna och kvalitet. Människor med funktionsnedsättning och deras familjer har betydande köpkraft. Att utesluta dem ger upp den. Tillgängliga tjänster minskar behovet av dyra assisterade kanaler (telefon och hjälp på plats), vilket är en direkt driftbesparing, särskilt för myndigheter. Och eftersom tillgänglighetsförbättringar (tydliga etiketter, tangentbordsstöd, läsbart innehåll, robust märkning) hjälper alla höjer de typiskt den övergripande slutförandegraden och nöjdheten.

Vad gäller total ägandekostnad är kostnaden för att anta utbildning, verktyg och att bygga in tillgänglighet i komponenter och pipelines, allt måttligt när du gör det från början. Kostnaden för att inte anta är svår och kommer från flera håll: rättsligt ansvar (stämningar, förlikningar, domstolsbeslutad åtgärd, regulatoriska viten), den långt högre kostnaden för att eftermontera under deadlinetryck, anseendeskada och den löpande kostnaden för att betjäna uteslutna användare genom dyrare kanaler. Eftermontering kostar typiskt flera gånger vad att designa in hade gjort.

För att driva ärendet inför ledningen, inled med den rättsliga skyldigheten där den gäller (den är icke förhandlingsbar för myndigheter och alltmer för den privata sektorn). Kvantifiera sedan den adresserbara befolkning ni utesluter, kostnaden för assisterade kanaler som uteslutningen ger upphov till och "trottoarkant"-vinsterna för alla användare. Placera tillgänglighet som riskhantering plus kvalitet, inte välgörenhet.

## Antimönster och fallgropar

- **Tillgänglighet som kryssruta före lansering**: en revision i slutet i stället för kontinuerlig praxis, vilket garanterar dyrt omarbete i sista minuten.
- **"Div-soppa"**: icke-semantisk märkning med klickhanterare på generiska element, osynlig för hjälpmedel.
- **ARIA-missbruk**: att skruva ARIA på trasig märkning, vilket vilseleder skärmläsare mer än vanlig märkning skulle göra.
- **Information enbart genom färg**: status visad enbart med färg, osynlig för färgblinda.
- **Osynligt fokus**: att ta bort fokusramar av estetiska skäl och lämna tangentbordsanvändare strandsatta.
- **Tangentbordsfällor**: modaler och widgetar som fångar eller tappar fokus.
- **Självbelåtenhet efter automatisk skanning**: att klara en skanner och anta att produkten är tillgänglig.
- **Tillgänglighetsöverlägg**: tredjepartswidgetar med "rättelse på en rad" som inte levererar verklig överensstämmelse och kan försämra upplevelsen.
- **Att utesluta användare med funktionsnedsättning från forskning**: att designa för en inbillad användare med funktionsnedsättning i stället för att testa med verkliga.

## Mognadsmodell

**Nivå 1: Initiera.** Ingen tillgänglighetspraxis. Problem upptäcks först när en användare klagar eller en stämning anländer, och svaret är reaktivt. Märkningen är icke-semantisk och otestad, och ingen äger problemet.

**Nivå 2: Utveckla.** Medvetenhet finns och vissa team agerar på den: en automatisk skanner i ett bygge här, en tangentbordsgenomgång där, en revision före lansering inför en stor release. Praxis är grundläggande och inkonsekvent över team, tillgänglighet är fortfarande en checklista i sent skede och den nedprioriteras ofta under schematryck.

**Nivå 3: Standardisera.** WCAG 2.2 AA är den dokumenterade standarden, upprätthållen i hela organisationen. Tillgänglighet är inbyggd i designsystemet så att komponenter levereras tillgängliga som standard, testade automatiskt och manuellt och nedskrivna i definitionen av färdig. Team är utbildade, en ägare eller ett kompetenscentrum finns och en åtgärdsprocess är definierad.

**Nivå 4: Hantera.** Tillgänglighet mäts och styrs med data mot utgångslägen. Organisationen följer överensstämmelsemått över tid (andel godkända skanningar, antalet öppna hinder per allvarlighetsgrad, skärmläsartestad täckning av kritiska resor och tid till åtgärd), rapporterar dem per team på en panel och behandlar regressioner som byggfel snarare än rådgivande varningar. Mål sätts mot ett utgångsläge och framsteg granskas, så att ett team som halkar efter syns innan en revision hittar det.

**Nivå 5: Orkestrera.** Tillgänglighet förbättras kontinuerligt och är integrerad i hela organisationen. Människor med funktionsnedsättning är en del av forskning och testning återkommande, och tillgänglighet är inbäddad i upphandling, designtokens och CI. Organisationen anpassar sig när standarder rör sig (antar nya WCAG-kriterier och förbereder sig för WCAG 3.0) och den påverkar leverantörer och partner så att hela leveranskedjan överensstämmer.

## Idéer för diskussion

- Hur hindrar ni tillgänglighet från att nedprioriteras när deadlines stramas åt?
- Vilken är den rätta blandningen av automatisk, manuell och användartestning för er riskprofil?
- Hur bör tillgänglighetsöverensstämmelse skrivas in i leverantörsavtal och upphandling?
- Hur hanterar ni klyftan mellan WCAG-överensstämmelse och genuin användbarhet för människor med funktionsnedsättning?
- Hur bör team förbereda sig för WCAG 3.0 samtidigt som de bygger mot 2.2 i dag?
- Hur rekryterar och ersätter ni deltagare med funktionsnedsättning i forskning rättvist och respektfullt?

## Viktigaste punkter

- Tillgänglighet är en grundläggande kvalitetsegenskap och, för myndigheter, ett rättsligt krav.
- Designa mot WCAG 2.2 AA som ett golv. Använd POUR-principerna som mental modell.
- Semantisk HTML först. ARIA bara för att fylla verkliga luckor, gjord korrekt.
- Automatiska verktyg fångar ungefär en tredjedel av problemen. Manuell testning och testning med hjälpmedel är nödvändig.
- Testa med människor med funktionsnedsättning, inte bara för dem.
- Att bygga in tillgänglighet är billigt och varaktigt. Att eftermontera är dyrt och skört.
- Tillgänglig design är bättre design för alla: trottoarkanteffekten är verklig.

## Referenser och vidare läsning

- W3C, *Web Content Accessibility Guidelines (WCAG) 2.2* and supporting Understanding/Techniques documents
- W3C, *WAI-ARIA Authoring Practices Guide*
- W3C Web Accessibility Initiative (WAI), introductory and tutorial materials
- Laura Kalbag, *Accessibility for Everyone*
- Sarah Horton and Whitney Quesenbery, *A Web for Everyone*
- Regine Gilbert, *Inclusive Design for a Digital World*
- U.S. Section 508 standards and Section508.gov guidance
- European standard EN 301 549 and the European Accessibility Act
- Government accessibility guidance (e.g., UK GDS accessibility manual)
- WebAIM, research and articles including the annual accessibility analyses
