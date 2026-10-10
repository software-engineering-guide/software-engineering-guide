# 5.5 Internationalisering och lokalisering

## Översikt och motivation

[Internationalisering](https://en.wikipedia.org/wiki/Internationalization_and_localization) (i18n) är det tekniska arbetet att bygga programvara så att den kan anpassas till vilket språk, vilken region och vilken kultur som helst utan att koden ändras. Lokalisering (l10n) är arbetet som följer: att faktiskt anpassa en produkt för en specifik språkversion genom att översätta text, formatera datum och tal, justera layout och ta hänsyn till kulturella förväntningar. De två är olika. Internationalisering görs en gång, i arkitekturen. Lokalisering görs många gånger, i innehållet. Få arkitekturen rätt i förväg och varje lokalisering blir billig. Få den fel och varje blir en smärtsam, felbenägen eftermontering.

För stora team är i18n ett grundläggande arkitekturbeslut. Det berör varje lager: datalagring, stränghantering, layout och innehållspipelines. Om du inte etablerar det tidigt och upprätthåller det genom gemensamma bibliotek och lint-regler hårdkodar team engelska strängar, sammanfogar översatta fragment och antar latinska skriftsystem. Den skulden måste lösas upp innan produkten kan gå in på någon ny marknad. Ett gemensamt i18n-ramverk och ett lokaliseringsarbetsflöde låter dussintals team leverera en produkt på många språk utan att var och en uppfinner rörmokeriet på nytt.

Relevansen för företag och myndigheter är direkt. Multinationella företag måste betjäna kunder och anställda över länder, språk och regelverk. Myndigheter måste betjäna språkligt mångskiftande befolkningar. Många länder är officiellt flerspråkiga, och många är rättsligt skyldiga att tillhandahålla tjänster på flera språk, inklusive skriftsystem från [höger till vänster](https://en.wikipedia.org/wiki/Bidirectional_text) och urfolks- eller minoritetsspråk. För offentliga tjänster är språktillgång en fråga om jämlikhet och lag: en medborgare som inte kan läsa det enda tillgängliga språket nekas i praktiken tjänsten.

## Nyckelprinciper

- Internationalisera arkitekturen en gång. Lokalisera innehållet många gånger.
- Hårdkoda aldrig användarvänd text. Flytta ut alla strängar i hanterade resurser.
- Använd [Unicode](https://en.wikipedia.org/wiki/Unicode) (UTF-8) överallt. Anta att text kan vara på vilket skriftsystem som helst.
- Sammanfoga aldrig översatta fragment. Grammatik och ordföljd skiljer sig mellan språk.
- Planera för textexpansion, skriftsystem från höger till vänster och komplexa plural- och genusregler.
- Formatera datum, tal, valutor och namn efter språkversion, inte efter kod.
- Skilj översättningsbart innehåll från kod så att översättare aldrig rör källkoden.
- Lokalisering är kulturell, inte bara språklig: färger, bilder och exempel spelar roll.

## Rekommendationer

### Bygg en sund internationaliseringsarkitektur

Lagra och bearbeta all text som Unicode (UTF-8) från början till slut (databas, API:er och UI) så att vilket skriftsystem som helst kan representeras. Flytta ut varje användarvänd sträng i resursfiler eller en meddelandekatalog nycklad med identifierare, aldrig inbäddad i kod eller märkning. Representera en språkversion (locale) som språk plus region (och skriftsystem där det behövs) så att du kan skilja, till exempel, ett språks varianter över länder. Håll formateringslogik i ett väl testat internationaliseringsbibliotek snarare än att handrulla formatering av datum, tal och valuta. Lagra data i neutrala, otvetydiga former (UTC-tidsstämplar, ISO-land- och valutakoder, basenheter) och formatera först i presentationslagret.

### Hantera språklig komplexitet korrekt

Anta inte textlängd. Tillåt generöst utrymme eftersom översättningar ofta blir mycket längre än engelska, och designa layouter som flödar om snarare än trunkerar eller överlappar. Stöd dubbelriktade (höger-till-vänster) skriftsystem genom att använda logiska snarare än fysiska layoutegenskaper och spegla gränssnittet där det är lämpligt. Använd språkversionens pluralregler via ditt i18n-bibliotek (språk har allt från en till sex pluralformer) i stället för naiv singular/plural-logik. Hantera genus och grammatisk kongruens där språket kräver det. Bygg aldrig meningar genom sammanfogning. Använd kompletta, parametriserade meddelandemallar så att översättare styr ordföljden.

### Etablera ett lokaliseringsarbetsflöde och översättningshantering

Behandla lokalisering som en kontinuerlig pipeline, inte en sats före lansering. Extrahera strängar automatiskt, skicka dem till ett [översättningshanteringssystem](https://en.wikipedia.org/wiki/Translation_management_system) och hämta tillbaka färdiga översättningar, helst integrerat med CI så att nya strängar flaggas och lokaliserade versioner hålls synkroniserade. Ge översättare kontext: skärmdumpar, beskrivningar, teckengränser och en ordlista och stilguide per språk för att hålla terminologi och ton konsekventa. Använd [översättningsminne](https://en.wikipedia.org/wiki/Translation_memory) för att återanvända tidigare arbete och skära kostnad. Besluta medvetet var [maskinöversättning](https://en.wikipedia.org/wiki/Machine_translation) är acceptabel (innehåll med låg risk och hög volym) och var mänsklig översättning och granskning krävs (juridiskt, medicinskt, säkerhetskritiskt, varumärkeskritiskt). [Pseudolokalisera](https://en.wikipedia.org/wiki/Pseudolocalization) tidigt, och ersätt strängar med förlängda, accentuerade platshållare, för att fånga hårdkodade strängar, trunkering och kodningsbuggar innan verklig översättning börjar.

### Lokalisera format, kultur och innehåll, inte bara ord

Formatera datum, tider, tal, valutor, adresser, telefonnummer och namn per språkversion och respektera lokala konventioner (datumordning, decimal- och grupperingsavskiljare, valutaplacering, namnordning). Anpassa bilder, ikoner, färger, exempel och metaforer till lokal kulturell betydelse, eftersom symboler och färger bär olika konnotationer över kulturer. Ta hänsyn till lokala skillnader i juridiskt och regulatoriskt innehåll. Skilj global konsekvens (varumärke, kärnfunktionalitet) från regional anpassning (innehåll, exempel, regelefterlevnad) och besluta uttryckligen vilka delar som är fasta och vilka som böjer sig.

### Styr i18n som gemensam infrastruktur

Tillhandahåll ett gemensamt i18n-bibliotek, lint-regler för att flytta ut strängar och en standardmekanism för att avgöra språkversion så att team inte av misstag kan hårdkoda text. Etablera ägarskap av lokaliseringspipelinen och ordlistorna. Testa i flera språkversioner i CI, inklusive en höger-till-vänster-språkversion och en pseudolokal med lång text, så att regressioner fångas automatiskt.

## Avvägningar: för- och nackdelar

| Beslut | Fördelar | Nackdelar |
|---|---|---|
| Internationalisera från dag ett | Billigt marknadsinträde senare, ingen eftermontering | Kostnad i förväg även innan en andra språkversion behövs |
| Eftermontera i18n senare | Skjuter upp kostnad om globalt behov är osäkert | Mycket dyrt och riskabelt att lösa upp hårdkodade antaganden |
| Mänsklig översättning | Hög kvalitet, kulturellt korrekt | Långsammare och dyrare |
| Maskinöversättning | Snabb, billig, skalar till enorm volym | Kvalitets- och noggrannhetsrisk. Olämplig för innehåll med höga insatser |
| Kontinuerlig lokaliseringspipeline | Språkversioner förblir synkroniserade, ingen lanseringskrasch | Verktygs- och processinvestering |
| Djup kulturell anpassning per region | Bättre lokal passform och förtroende | Fler innehållsvarianter att bygga och underhålla |

Den avgörande avvägningen är när man ska investera i internationalisering. Att eftermontera i18n i en produkt full av hårdkodad, sammanfogad, latin-antagande kod är en av de dyrare formerna av teknisk skuld att betala av. För varje organisation med rimliga internationella eller flerspråkiga ambitioner, vilket inkluderar i stort sett alla stora företag och flerspråkiga myndigheter, är det långt billigare att internationalisera arkitekturen tidigt än att eftermontera, även om utdelningen är uppskjuten.

## Frågor att diskutera med ditt team

1. **Upprätthåller vi utflyttning av strängar med lint-regler, och körs pseudolokalisering i CI före någon verklig översättning?** Skulden som gör internationalisering dyr (hårdkodade engelska strängar, sammanfogade meningsfragment, antaganden om latinskt skriftsystem) ackumuleras tyst om inte verktyg stoppar den vid incheckning. Lint-regler som flaggar hårdkodad användartext, plus en accentuerad pseudolokal med lång text körd i CI, fångar trunkering, överlappning och kodningsbuggar medan de är billiga att rätta. Det är vad som låter dussintals team leverera en produkt på många språk utan att var och en uppfinner rörmokeriet på nytt eller löser upp antaganden under en deadline senare. Ta med en sökning efter hårdkodade strängar och fråga om något team av misstag kunde leverera en i dag. Om inget i pipelinen skulle fånga det är det luckan att stänga först.

2. **Var lagrar vi kanonisk data, och är formatering begränsad till presentationslagret?** Att lagra tidsstämplar som UTC, länder och valutor som ISO-koder och belopp i basenheter betyder att vilken språkversion som helst kan formatera dem korrekt vid kanten, medan formateringslogik inbakad i datalagret ger buggar som är smärtsamma att lösa upp. Kom överens om att datum, tal, valutor, adresser och namn formateras bara vid presentation, genom ett väl testat bibliotek snarare än handrullad kod. Det här spelar roll för multinationella företag och flerspråkiga myndigheter där en medborgare måste se korrekt datumordning, decimalavskiljare och namnordning i sin egen konvention. Ta med ett exempel på ett värde ert system lagrar redan formaterat och spåra vad som går sönder när en ny språkversion behöver det annorlunda. Om data och presentation är trasslade, besluta hur ni reder ut dem innan ni lägger till språkversioner.

3. **Var exakt är maskinöversättning acceptabel, och hur hålls vår lokaliseringspipeline kontinuerlig snarare än satsvis?** Maskinöversättning är snabb och billig för innehåll med låg risk och hög volym men olämplig för juridisk, medicinsk, säkerhetskritisk eller varumärkeskritisk text där en felöversättning orsakar verklig skada, så gränsen måste vara en uttrycklig policy, inte en gissning per team. Lika väl garanterar behandling av lokalisering som en sats före lansering en översättningskrasch, medan automatisk extrahering av strängar och synkronisering genom ett översättningshanteringssystem håller varje språkversion aktuell. Besluta vem som äger pipelinen, ordlistorna och grinden för mänsklig granskning av strängar med höga insatser. Ta med en nylig release och fråga hur lång tid dess nya strängar tog att dyka upp på alla språk. Om språkversioner driver isär mellan releaser är er pipeline satsvis i förklädnad.

4. **Testar vi en höger-till-vänster-språkversion och en pseudolokal med lång text automatiskt, eller antar vi i tysthet latinska skriftsystem och layouter med engelsk textlängd?** Stöd för dubbelriktat (höger-till-vänster) och textexpansion är de antaganden som bryts mest synligt på en ny marknad: speglade gränssnitt som aldrig speglades och knappar som trunkeras när tyska eller finska löper fyrtio procent längre än engelska. Det konkurrerande draget är hastighet, eftersom att bygga på logiska snarare än fysiska layoutegenskaper och koppla in en accentuerad pseudolokal i kontinuerlig integration (CI) kostar insats innan någon verklig kund behöver det. Ta med en skärmdump av era mest trafikerade skärmar renderade i en höger-till-vänster-språkversion och i en förlängd pseudolokal och räkna överlappningarna, klippta etiketter och fastnade pilar. För ett multinationellt företag eller en myndighet rättsligt skyldig att betjäna ett höger-till-vänster- eller minoritetsspråk är en layout som inte kan spegla inte ett kosmetiskt fel, det är en marknad eller en lagstadgad skyldighet ni inte kan uppfylla utan en ombyggnad.

5. **Vilka delar av produkten är globalt fasta och vilka böjer sig efter region, och vem har befogenhet att avgöra?** Lokalisering är kulturell, inte bara språklig, så färger, bilder, exempel, tilltalsformer och till och med vilka funktioner som erbjuds kan skilja sig per marknad, men varje regional variant ni tillåter är ytterligare en artefakt att bygga, översätta, granska och underhålla för alltid. Spänningen är mellan lokal passform, som bygger förtroende och konvertering, och konsekvens, som håller varumärket sammanhängande och underhållsbördan begränsad. Ta med en konkret lista över vad en föreslagen ny språkversion skulle ändra utöver översatta strängar och prissätt det löpande underhållet av varje variant, inte bara dess första bygge. I ett stort företag behöver detta beslut en namngiven ägare så att regionala team inte kan förgrena produkten ad hoc, och i myndigheter måste det respektera rättsligt och tillgänglighetsmässigt innehållskrav som varierar per jurisdiktion och inte är valfria.

6. **Vilka språkversioner förbinder vi oss faktiskt till, hur håller vi terminologin konsekvent över dem och vilka belägg driver den listan?** Att lägga till ett språk är lätt att lova och dyrt att upprätthålla, eftersom varje kräver en ordlista, en stilguide, mänsklig granskning av strängar med höga insatser och korrekt hantering av plural och genus som naiv singular-eller-plural-logik får fel på de flesta språk. De konkurrerande hänsynen är räckvidd mot kostnad: en marknad eller befolkning som betjänas dåligt kan vara värre än en som inte betjänas alls. Ta med befolkningen eller intäkterna bakom varje kandidatspråkversion, den täckning av pluralregler och formatering ert bibliotek ger för den och vem som äger dess ordlista. För ett multinationellt företag är drivkraften adresserbar marknad och supportkostnad per språk, medan den för myndigheter är rättslig skyldighet om språktillgång och jämlikhet, kvantifierad av antalet invånare som bara kan göra sina ärenden på det språket.

## Sektorsperspektiv

**Startup.** Gör de billiga arkitekturvalen dag ett och stanna där: UTF-8 från början till slut, varje användarvänd sträng i en meddelandekatalog och datum, tal och valutor formaterade genom ett språkversionsmedvetet bibliotek. Dessa kostar nästan ingenting medan du levererar på ett språk och sparar en omskrivning när din första stora kund vill ha ett andra. Res inte en översättningspipeline eller stöd språkversioner ingen ännu betalar för. Håll dörren öppen, inte hela huset möblerat.

**Småföretag.** Utan internationaliseringsspecialist och med snäv budget, lita på de i18n-funktioner som redan finns i ditt ramverk och en hostad översättningshanteringstjänst snarare än att bygga pipelines själv. Använd maskinöversättning för innehåll med låg risk och hög volym och betala för mänsklig översättning bara där ett misstag skulle kosta dig en kund eller bryta mot en regel, som juridisk, säkerhetskritisk eller faktureringstext. Förbind dig till en språkversion först när en specifik marknad tydligt motiverar den löpande översättnings- och granskningskostnaden.

**Storföretag.** Problemet är styrning över många team: ett gemensamt i18n-bibliotek, lint-regler som avvisar hårdkodade strängar, en kontinuerlig lokaliseringspipeline med översättningsminne och ordlistor per språk samt CI med flera språkversioner som inkluderar en höger-till-vänster- och en pseudolokal med lång text. Driv lokalisering som gemensam infrastruktur med en tydlig ägare så att grupper slutar uppfinna rörmokeriet på nytt eller driva ur synk. Mät språktäckning, lokaliseringskvalitet och tid att lansera en ny språkversion och hantera portföljen av språkversioner mot dessa tal snarare än att lansera marknader ad hoc.

**Offentlig sektor.** Språktillgång är ofta en rättslig skyldighet, som omfattar officiella språk, höger-till-vänster-skriftsystem och urfolks- eller minoritetsspråk, så transparens och jämlikhet formar varje val. Bygg ett gemensamt i18n-ramverk och översättningsarbetsflöde över myndigheter, kräv mänsklig granskning av juridisk och säkerhetskritisk terminologi och publicera ordlistor så att termer förblir konsekventa mellan tjänster. Upphandling bör kräva stöd för språkversioner, höger-till-vänster och tillgänglighet i avtal, och befolkningen som betjänas på varje språk är måttet som motiverar utgiften inför allmänheten.

## Exempel

**Startup.** En liten startup som bara levererade på engelska gjorde ändå några billiga arkitekturval dag ett: UTF-8 överallt, varje användarvänd sträng flyttad ut i en meddelandekatalog i stället för hårdkodad och datum och valutor formaterade genom ett språkversionsmedvetet bibliotek. Det kostade dem nästan ingenting medan de hade ett språk. Ett år senare, när deras största prospekt bad om en fransk och en tysk version, var det mest en översättningsövning lämnad till en entreprenör att lägga till de språkversionerna, inte en omskrivning, och de stängde affären på veckor i stället för att skjuta upp den ett kvartal av ingenjörsarbete.

**Storföretag.** Ett globalt e-handelsföretag internationaliserade sin plattform tidigt: UTF-8 genomgående, utflyttade strängar, ett språkversionsmedvetet formateringsbibliotek och en kontinuerlig lokaliseringspipeline med översättningsminne och ordlistor per språk. Att gå in på en ny marknad blev till stor del en innehållsövning (översätta, granska, justera bilder) snarare än ett tekniskt projekt, vilket lät företaget lansera i nya språkversioner på veckor. Stöd för höger-till-vänster byggt på logiska layoutegenskaper betydde att arabiska och hebreiska marknader krävde lite nytt UI-arbete.

**Offentlig sektor.** En nationell regering rättsligt skyldig att leverera tjänster på flera officiella språk, inklusive ett höger-till-vänster-skriftsystem och minoritetsspråk, byggde ett gemensamt i18n-ramverk och översättningsarbetsflöde som användes över myndigheter. Pseudolokalisering i CI fångade hårdkodade strängar och trunkering före lansering. En gemensam ordlista höll juridisk terminologi konsekvent över tjänster och språk. Medborgare kan slutföra skatte-, hälso- och bidragstransaktioner på sitt eget språk med korrekt formatering av datum, tal och namn, vilket uppfyller lag om språktillgång och förbättrar jämlikheten för talare av andra språk än majoritetsspråket.

## Affärsnytta: motiv, ROI och TCO

ROI på internationalisering är marknadstillgång och hastighet. En väl internationaliserad produkt kan gå in i nya länder och språkmarknader snabbt och billigt och förvandla varje ny språkversion till inkrementella intäkter eller medborgarräckvidd snarare än ett större projekt. Lokaliseringskvalitet driver konvertering, förtroende och supportkostnad på varje marknad: användare gör fler transaktioner och kontaktar support mindre när produkten talar deras språk korrekt och respekterar deras konventioner.

Vad gäller total ägandekostnad är kostnaden för att anta den tekniska insatsen i förväg för att internationalisera, plus löpande översättnings- och pipelinekostnader. Kostnaden för att inte anta är den dyra eftermonteringen: att lösa upp hårdkodade strängar, sammanfogning, kodningsbuggar och layoutantaganden över en hel kodbas, ofta under en deadline driven av ett marknads- eller lagkrav. Dålig lokalisering bär också dolda kostnader: förlorad försäljning på marknader som betjänas dåligt, supportbörda från förvirrande format och rättslig eller anseendemässig skada från felöversatt innehåll med höga insatser. Kontinuerlig lokalisering undviker kostsamma översättningskrascher före lansering.

För att driva ärendet inför ledningen, ramma in internationalisering som en option på framtida marknader. Det är en måttlig investering i förväg som dramatiskt sänker kostnaden och tiden för varje framtida marknadsinträde. För myndigheter är drivkraften rättslig skyldighet om språktillgång och jämlikhet, kvantifierad av befolkningen som betjänas på varje språk.

## Antimönster och fallgropar

- **Hårdkodade strängar**: användartext inbakad i koden, vilket tvingar kodändringar per språkversion.
- **Strängsammanfogning**: att bygga meningar av fragment, vilket bryter grammatik och ordföljd.
- **Icke-Unicode-antaganden**: kodningsbuggar, [mojibake](https://en.wikipedia.org/wiki/Mojibake) (förvrängd text från felmatchade teckenkodningar) och oförmåga att representera skriftsystem.
- **Att anta engelsk textlängd**: layouter som trunkerar eller överlappar när de översätts.
- **Att ignorera höger-till-vänster**: användning av fysisk vänster/höger-layout som inte kan spegla.
- **Naiv pluralisering**: singular/plural-logik som är fel på de flesta språk.
- **Språkversionsblind formatering**: hårdkodade format för datum, tal och valuta.
- **Översättning utan kontext**: översättare som gissar betydelse och producerar fel.
- **Satsvis lokalisering i sista minuten**: en krasch före lansering i stället för en kontinuerlig pipeline.
- **Kulturell tondövhet**: bilder, färger eller exempel som kränker eller förvirrar lokalt.

## Mognadsmodell

**Nivå 1: Initiera.** Ett språk, hårdkodade strängar, icke-Unicode-antaganden och text byggd genom sammanfogning. Internationalisering är reaktiv: varje ny språkversion betyder att koden ändras, och kodnings- och layoutbuggar hittas av en slump i produktion.

**Nivå 2: Utveckla.** Vissa strängar är utflyttade och Unicode används på ställen, men praxis är inkonsekvent över team. Lokalisering är en manuell, satsvis insats före lansering, och formatering, pluralhantering och stöd för höger-till-vänster hanteras olika (eller inte alls) från ett team till nästa.

**Nivå 3: Standardisera.** En gemensam i18n-arkitektur och ett språkversionsmedvetet formateringsbibliotek är den dokumenterade, upprätthållna standarden i hela organisationen. Utflyttning av strängar kontrolleras med lint-regler, ett översättningshanteringssystem och en kontinuerlig pipeline finns med ordlistor och översättningsminne, och pseudolokalisering plus testning i flera språkversioner (inklusive en höger-till-vänster- och en med lång text) körs i CI.

**Nivå 4: Hantera.** Lokaliseringsprogrammet mäts och styrs mot utgångslägen. Team följer språktäckning, lokaliseringskvalitet och defektfrekvens, synkroniseringsfördröjning för strängar från incheckning till översatt release, trunkerings- och höger-till-vänster-renderingsdefekter som fångas per release, översättningskostnad per språkversion och tid att lansera en ny språkversion, och dessa mått grindar releaser och driver var man ska investera mänsklig granskning mot maskinöversättning.

**Nivå 5: Orkestrera.** Internationalisering och lokalisering förbättras kontinuerligt och är integrerade i hela organisationen. Lokalisering är kontinuerlig, maskin- och mänsklig översättning väljs medvetet per innehållsklass och kulturell anpassning är systematisk. Organisationen lägger till, avvecklar och omdefinierar språkversioner utifrån belägg om marknad och jämlikhet, och nya språkversioner lanseras snabbt med hög kvalitet utan en eftermontering.

## Idéer för diskussion

- Hur tidigt bör en produkt internationaliseras om den internationella efterfrågan är osäker?
- Var är maskinöversättning acceptabel, och var måste människor granska?
- Hur håller ni terminologin konsekvent över många språk och team?
- Hur mycket regional kulturell anpassning är värd det tillagda variantunderhållet?
- Hur bör stöd för höger-till-vänster och minoritetsspråk prioriteras och testas?
- Hur ger ni översättare tillräcklig kontext utan att bromsa pipelinen?

## Viktigaste punkter

- Internationalisera arkitekturen en gång. Lokalisera innehållet många gånger.
- Använd Unicode överallt, flytta ut alla strängar och sammanfoga aldrig översättningar.
- Planera för textexpansion, höger-till-vänster-skriftsystem och språkversionsspecifika plural- och formateringsregler.
- Kör en kontinuerlig lokaliseringspipeline med översättningsminne, ordlistor och kontext.
- Pseudolokalisera tidigt i CI för att fånga i18n-buggar före verklig översättning.
- Lokalisering är kulturell, inte bara språklig.
- Tidig internationalisering är långt billigare än eftermontering. För myndigheter är det ett rättsligt krav på jämlikhet.

## Referenser och vidare läsning

- The Unicode Consortium, *The Unicode Standard* and Common Locale Data Repository (CLDR)
- W3C Internationalisation (i18n) Activity, techniques and best practices
- Richard Ishida, W3C internationalisation articles and tutorials
- Bert Esselink, *A Practical Guide to Localisation*
- John Yunker, *Beyond Borders: Web Globalisation Strategies*
- Unicode Technical Standard #35 (locale data markup) and ICU library documentation
- IETF BCP 47 language tags
- Government multilingual service and language-access guidance
- Nielsen Norman Group and W3C articles on RTL, text expansion, and localisation UX
