# 7.7 Datamodellering och det semantiska lagret

## Översikt och motivation

En [datamodell](https://en.wikipedia.org/wiki/Data_model) är ett beslut om vad din data betyder, fattat innan du avgör var datan bor. Den namnger de saker din verksamhet bryr sig om, de attribut som beskriver dem och relationerna mellan dem. Lagring, index, filformat och frågemotorer kommer alla senare. Den ordningen spelar roll eftersom din datas betydelse överlever varje teknik du använder för att hålla den. Datalager byts ut, tabellformat förändras och frågemotorer kommer och går, men "kund", "order" och "aktiv användare" måste betyda detsamma över alla dem, i åratal.

För ett litet team är modellering ofta implicit. En ingenjör håller hela schemat i huvudet, och en gemensam förståelse av "intäkt" överlever eftersom det bara finns tre personer att vara oeniga. I skalan hos stora utvecklingsorganisationer, företag och myndigheter kollapsar den informaliteten på exakt det sätt som beskrivs i kapitel 7.1 (datastrategi och datastyrning). Dussintals team bygger hundratals tabeller, var och en med sin egen idé om vad en "session" är eller när en användare räknas som "aktiv". Två paneler visar två olika tal för samma vecka, och ett ledningsmöte förvandlas till ett argument om vems fråga som är rätt i stället för vad man ska göra härnäst. Dålig modellering annonserar inte sig själv. Den dyker upp månader senare som avstämningsarbete, misslyckade revisioner och beslut fattade på siffror ingen kan försvara.

Det här kapitlet handlar om att göra det arbetet medvetet. Det behandlar konceptuella, logiska och fysiska modeller, entitets-relationsmodellering, när man ska normalisera och när man ska denormalisera, hur modellering skiljer sig för transaktionella mot analytiska arbetslaster, dimensionell modellering med fakta och dimensioner och det semantiska lager som håller den enda styrda definitionen av varje affärsmått. Utdelningen är inte elegans för sin egen skull. Den är att "aktiv användare" och "intäkt" betyder en sak överallt, så att dina team kan lita på talen och röra sig fortare tack vare det.

*Se även:* kapitel 3.4 (dataarkitektur och lagring), kapitel 7.3 (analys och business intelligence) och kapitel 11.5 (nyckeltal).

## Nyckelprinciper

- Avgör vad data betyder innan du avgör var den bor.
- Modellera på tre nivåer: konceptuell (verksamhet), logisk (struktur), fysisk (implementering).
- Normalisera för att skydda korrekthet i transaktionella system. Denormalisera medvetet för analytisk hastighet.
- Matcha modellen mot arbetslasten: transaktioner och analys har motsatta behov.
- Varje affärsmått har exakt en styrd definition, och den bor i det semantiska lagret.
- Konformerade dimensioner låter oberoende team joina och jämföra data säkert.
- Granularitet är ett designbeslut du fattar med avsikt, inte en slump i en fråga.
- Modeller är levande tillgångar: namnge dem väl, dokumentera dem och håll dem utvecklingsbara.

## Rekommendationer

### Modellera på tre nivåer, i ordning

Arbeta från betydelsen och utåt. Börja med en konceptuell modell: de entiteter din verksamhet bryr sig om och hur de relaterar, skrivna på klarspråk en domänexpert kan kontrollera. "En kund lägger många ordrar. En order innehåller många orderrader. Varje orderrad refererar till en produkt." Inga nycklar, inga typer, inga tabeller ännu. Bygg sedan en logisk modell som lägger till struktur: attribut, primär- och främmande nycklar, kardinaliteter och begränsningar, fortfarande oberoende av någon specifik databas. [Entitets-relationsmodellering](https://en.wikipedia.org/wiki/Entity%E2%80%93relationship_model) är standardnotationen här, och ett entitets-relationsdiagram är artefakten du granskar med både ingenjörer och verksamhetsintressenter. Först därefter producerar du den fysiska modellen: de faktiska tabellerna, kolumnerna, datatyperna, indexen, partitionerna och lagringslayouten för din valda motor. Att hoppa till fysisk design är det vanligaste modelleringsmisstaget, eftersom det bakar in dagens teknikval i beslut som borde överleva dem.

### Normalisera transaktionella system, denormalisera analytiska medvetet

För system som registrerar transaktioner, föredra [databasnormalisering](https://en.wikipedia.org/wiki/Database_normalization). Normalformer tar bort redundans så att varje faktum lagras en gång, vilket förhindrar uppdateringsanomalier och håller skrivningar korrekta när många användare ändrar data samtidigt. Det är rätt standard för [onlinetransaktionsbearbetning](https://en.wikipedia.org/wiki/Online_transaction_processing) (OLTP), där korrekthet under samtidiga skrivningar spelar större roll än hastigheten hos någon enskild analysfråga. Analytiska system har motsatta prioriteringar. De är läs-tunga, de skannar och aggregerar enorma intervall, och att joina dussintals normaliserade tabeller vid frågetillfället är långsamt och svårt att resonera om. Där denormaliserar du med avsikt och slår ihop relaterade attribut så att frågor blir enklare och snabbare. Disciplinen är att denormalisera medvetet, med en dokumenterad anledning, snarare än att låta redundans smyga sig in av misstag. Kapitel 3.4 (dataarkitektur och lagring) behandlar de motorer som får varje mönster att prestera.

### Använd dimensionell modellering för analys

För analytiska arbetslaster, anta [dimensionell modellering](https://en.wikipedia.org/wiki/Dimensional_modeling), ansatsen populariserad av Ralph Kimball. Du delar världen i fakta och dimensioner. En faktatabell håller mätningarna av en affärsprocess: beloppet i en försäljning, längden på ett samtal, den levererade kvantiteten. Dimensionstabeller håller det beskrivande sammanhang du filtrerar och grupperar efter: kunden, produkten, butiken, datumet. Ordna en faktatabell omgiven av sina dimensioner och du har ett [stjärnschema](https://en.wikipedia.org/wiki/Star_schema), som är lätt för analytiker att förstå och snabbt för motorer att fråga. Normalisera dessa dimensioner i undertabeller och du får ett snöflingeschema, som sparar en del lagring på bekostnad av fler joins och mer komplexitet. Föredra stjärnan om du inte har en konkret anledning. För mycket stora, starkt reglerade miljöer där granskningsbarhet och källspårning dominerar modellerar ett data vault-tillvägagångssätt nav, länkar och satelliter för att fånga historik och ursprung aggressivt, på bekostnad av fler tabeller och en brantare inlärningskurva. De flesta team bör börja med stjärnor i Kimball-stil och sträcka sig efter data vault först när revisionskraven motiverar det.

### Fastställ granularitet och hantera föränderliga dimensioner uttryckligen

Innan du lägger till en enda kolumn i en faktatabell, ange dess granularitet: exakt vad en rad representerar. "En rad per orderrad." "En rad per användare per dag." Granularitet är grunden för en korrekt modell, eftersom varje mått och varje dimension antingen passar den granulariteten eller inte hör hemma i tabellen. Att blanda granulariteter är hur du får dubbelräknade intäkter. Avgör sedan hur dimensioner förändras över tid. En kund flyttar till en ny stad. Skriver du över det gamla värdet, behåller full historik eller spårar bara det nuvarande och föregående värdet? Det är de standardiserade mönstren för [långsamt föränderliga dimensioner](https://en.wikipedia.org/wiki/Slowly_changing_dimension), och att välja fel betyder att dina historiska rapporter i tysthet skriver om det förflutna. Avgör granularitet och förändringsstrategi i förväg, skriv in dem i modellens dokumentation och håll linjen i granskningen.

### Bygg ett semantiskt lager som den enda definitionen av varje mått

Detta är rekommendationen som betalar för hela kapitlet. Ett [semantiskt lager](https://en.wikipedia.org/wiki/Semantic_layer) sitter mellan dina fysiska tabeller och varje verktyg som konsumerar dem, och det håller den enda styrda definitionen av varje affärsmått. "Aktiv användare" definieras en gång, som kod, med sin exakta logik: vilka händelser som räknas, över vilket fönster, med exkludering av vilka interna konton. "Intäkt" definieras en gång, inklusive hur återbetalningar, rabatter och valutaomräkning hanteras. Varje panel, anteckningsbok, rapport och reverse-ETL-jobb läser den definitionen i stället för att implementera den på nytt i en skräddarsydd fråga. När definitionen ändras ändras den på ett ställe och varje konsument uppdateras tillsammans. Det är mekanismen som gör styrda måttdefinitioner verkliga snarare än ambitiösa, och den är den direkta implementeringen av vad kapitel 11.5 (nyckeltal) ber om. Behandla måttdefinitioner som versionerad kod med ägare, granskning och tester, precis som kapitel 7.1 ber dig behandla data som en produkt.

### Etablera konventioner, namngivning och dokumentation

Konsekvens är en funktion. Anta namnkonventioner och upprätthåll dem: en konvention för tabellnamn, en konvention för nycklar, en standard för datumkolumner, en regel för hur du markerar ett faktum mot en dimension. Avgör en gång för alla om du använder singular eller plural för entitetsnamn och blanda aldrig. Dokumentera varje modell där de som använder den kommer att leta: betydelsen av varje tabell, granulariteten hos varje fakta, definitionen av varje mått och ägaren till vart och ett. God namngivning och dokumentation är det som låter en ny analytiker klara sig själv i stället för att avbryta teamet, och det är det som låter en revisor spåra ett tal från en styrelsepresentation tillbaka till dess källa utan en guidad tur.

### Håll modeller utvecklingsbara

Din modell kommer att förändras, så designa för förändring. Lägg till kolumner i stället för att ändra användning av befintliga. Använd surrogatnycklar så att en förändring i ett källsystems naturliga nyckel inte ger krusningar genom ditt datalager. Versionera måttdefinitioner och avveckla dem med varsel i stället för att i tysthet ändra dem under pågående paneler. Håll transformationer i versionshantering, testade och granskade, så att en ändring av vad "aktiv användare" betyder är en pull request med en diff och en godkännare, inte en tyst redigering i ett BI-verktyg. En modell du inte säkert kan utveckla blir en modell människor går runt, och skuggdefinitioner är hur den enda sanningskällan dör.

## Avvägningar: för- och nackdelar

| Tillvägagångssätt | Fördelar | Nackdelar | Bäst passform |
|---|---|---|---|
| Normaliserad (3NF) | Korrekta skrivningar, ingen redundans, flexibel | Långsamma analytiska joins, komplexa frågor | OLTP och operativa system |
| Stjärnschema (Kimball) | Snabbt, intuitivt, analytikervänligt | Viss redundans, ETL att underhålla | De flesta analyser och BI |
| Snöflingeschema | Mindre lagring, renare dimensioner | Fler joins, mer komplexitet | Stora, hårt styrda dimensioner |
| Data vault | Full historik, granskningsbart, agila laddningar | Många tabeller, brant inlärningskurva | Starkt reglerat, granskningstungt |
| Semantiskt lager över modeller | En definition överallt, verktygsoberoende | Bygge i förväg, behöver ägarskap | Flerteams- och fleraverktygsorganisationer |

Den centrala spänningen är hastigheten hos en enskild fråga mot korrekthet och flexibilitet över hela egendomen. Normalisering skyddar korrekthet och betalar för det i frågekomplexitet. Dimensionella modeller köper frågehastighet och tydlighet och betalar för det med ETL och viss hanterad redundans. Det finns ingen universell vinnare, vilket är varför du matchar modellen mot arbetslasten i stället för att välja en favorit. Det semantiska lagret löser den andra spänningen, mellan många team och många verktyg, genom att göra måttdefinitionen oberoende av något enskilt av dem. Misstaget är att behandla dessa som ideologiska läger. En frisk organisation kör normaliserade OLTP-system, dimensionella analysmodeller matade från dem och ett semantiskt lager ovanpå, var och en gör det jobb den är bra på.

## Frågor att diskutera med ditt team

1. **När två paneler visar olika tal för samma mått, vems definition vinner, och var bor den definitionen fysiskt?** Den här frågan avslöjar om ni faktiskt har en enda sanningskälla eller bara tror det. I de flesta stora team är det ärliga svaret att "aktiv användare" omdefinieras i ett dussin olika frågor, och vinnaren är den som argumenterar högst på mötet. Ta med verkliga belägg: välj ett mått, hitta varje ställe det beräknas och jämför logiken rad för rad. Ni kommer nästan säkert att hitta tysta oenigheter om fönster, exkluderingar och gränsfall. Svaret bör driva ett beslut att bygga ett semantiskt lager där varje mått definieras en gång, som granskad kod, så att frågan slutar handla om människor och börjar handla om en versionerad artefakt. Tills den definitionen har ett enda fysiskt hem är varje avstämning tillfällig.

2. **Vad är granulariteten hos er viktigaste faktatabell, och kan alla i rummet ange den på samma sätt?** Granularitet är den tysta grunden som de flesta modelleringsfel kan spåras tillbaka till. Om hälften av teamet säger "en rad per order" och den andra hälften säger "en rad per orderrad" har ni en dubbelräkningsbugg som väntar på att dyka upp i en intäktsrapport. Ta med den faktiska tabellen och be var och en beskriva en rad i en enda mening. Oenighet här är inte ett kommunikationsproblem att släta över. Det är en designdefekt att rätta innan fler mått hopas ovanpå den. Svaret bör skrivas in i modellens dokumentation och upprätthållas i granskning, eftersom när analytiker väl bygger frågor på en tvetydig granularitet sprider sig tvetydigheten fortare än ni kan rätta den.

3. **Hur kommer den här modellen att absorbera förändring, och vad händer med förra årets rapporter när en definition skiftar?** Varje modell möter föränderliga källsystem, föränderliga affärsregler och föränderliga måttdefinitioner, så den verkliga frågan är om förändring är en kontrollerad pull request eller en tyst redigering som skriver om historiken. Ta med ett nyligt exempel: ett mått vars definition ändrades eller en källnyckel som döptes om, och spåra vad som hände med befintliga paneler. Om en långsamt föränderlig dimension hanterades genom överskrivning kan era historiska rapporter i tysthet ha ändrat sina tidigare värden, vilket är ett allvarligt problem för alla som gör trendanalys eller reglerad rapportering. Svaret bör driva er mot surrogatnycklar, versionerade måttdefinitioner, uttryckliga förändringsstrategier och transformationer hållna i versionshantering med granskning. En modell ingen säkert kan ändra blir en modell människor överger.

4. **Vilka dimensioner måste betyda detsamma över varje team, och vem är ansvarig för att äga var och en?** Konformerade dimensioner är det som låter marknadsföring, ekonomi och drift joina sin data och få jämförbara svar, men bara när "kund", "produkt", "region" och "datum" bär en överenskommen definition i stället för en privat kopia per team. Det konkurrerande draget är autonomi: varje team vill modellera sin egen värld i sin egen takt, och att tvinga fram en gemensam dimension saktar ner dem på kort sikt medan den betalar sig över hela egendomen. Ta med de två eller tre dimensioner som dyker upp i flest rapporter över team, lista varje version av var och en som finns i dag och se hur långt deras nycklar och attribut faktiskt divergerar. Namnge en ägare för varje konformerad dimension, eftersom en gemensam dimension utan ägare glider tillbaka till privata kopior inom ett kvartal. I företags- och myndighetssammanhang, där en siffra från en avdelning jämförs med en annan offentligt, är en okonformerad dimension skillnaden mellan en ärlig jämförelse och en oavsiktlig osanning, så avgör tidigt vilka dimensioner som styrs centralt och vilka som förblir lokala.

5. **Var går gränsen mellan era normaliserade transaktionella system och era denormaliserade analytiska modeller, och är varje denormalisering ett medvetet beslut?** Att matcha modellen mot arbetslasten är kärndisciplinen, men gränsen är just där det suddas ut: en analytiker denormaliserar en lagertabell för hastighet, en ingenjör normaliserar en rapporttabell av vana och ingen skrev ner vilken sida varje val hör till. Spänningen är hastigheten hos en enskild fråga mot korrekthet och flexibilitet över allt, och förnuftiga människor landar olika beroende på om de äger skrivningar eller läsningar. Ta med er långsammaste analysfråga och er mest omstridda transaktionella tabell och fråga för varje redundant kolumn om dess redundans valdes med en dokumenterad anledning eller smög sig in av misstag. Målet är en skriftlig regel för när denormalisering är tillåten och vem som godkänner, inte en renhetstävling. För stora eller reglerade organisationer avgör denna gräns också var personuppgifter dupliceras, så en odokumenterad denormalisering är både en prestandafråga och en dataexponering i styrningen som någon till slut måste förklara för en revisor.

6. **Ska ni bygga eller köpa det semantiska lagret, och vem är ansvarig för att hålla varje måttdefinition aktuell när det väl finns?** Ett semantiskt lager levererar en enda sanningskälla bara när det ägs och underhålls, så valet av verktyg spelar mindre roll än svaret på vem som granskar en ändring av vad "intäkt" betyder och vem som är ansvarig när en definition blir inaktuell. De konkurrerande hänsynen är verkliga: ett bygge ger er kontroll och passar er stack men lägger till en ingenjörsbörda, medan att köpa ett måttverktyg är snabbare men riskerar inlåsning och ett definitionsspråk ni inte fullt ut kontrollerar. Ta med era handfull mått med högst insatser, de verktyg som konsumerar dem i dag och en ärlig läsning av om någon för närvarande äger de definitionerna eller de bara finns. Avgör i förväg om definitioner bor som versionerad kod med namngivna ägare och tester, eftersom ett semantiskt lager ingen underhåller ruttnar till samma utspridda definitioner det var tänkt att ersätta. I företags- och myndighetsrapportering, där ett mått på en offentlig panel måste kunna spåras till en dokumenterad, granskad definition, är det ägarskapet och förmågan att bevisa ursprunget hos ett tal det som förvandlar det semantiska lagret från en bekvämlighet till en granskningsbar kontroll.

## Sektorsperspektiv

**Startup.** Modellering kan vänta, men definitioner kan inte. Med två ingenjörer och ingen livslängd att bygga ett datalager, lägg ett litet semantiskt lager i ditt transformationsverktyg och definiera de två eller tre mått din styrelse faktiskt bevakar, "aktiv användare" och "intäkt", en gång som testad kod. Hoppa över data vault och genomarbetade dimensionella scheman: en tunn stjärna och en handfull styrda definitioner köper dig konsekventa tal utan att sakta ner leveransen. Utdelningen är att styrelseförberedelser slutar vara ett argument om vems fråga som är rätt.

**Småföretag.** Du har ingen datamodellerare och ingen budget för en måttplattform, så lita på de definitioner som är inbyggda i de verktyg du redan kör och skriv ner de få som spelar roll i ett gemensamt dokument alla läser. Föredra att köpa analys inbäddad i din befintliga programvara framför att sätta upp ett datalager du inte kan bemanna. Där du modellerar, håll det enkelt och namnge saker konsekvent, eftersom den som underhåller det nästa år kan vara den som inte kan minnas varför "kund" betydde två saker. Konsekvens är billigare än avstämning.

**Storföretag.** Problemet är många team och många verktyg som glider in i privata definitioner, så investera i konformerade dimensioner, ett styrt semantiskt lager och måttdefinitioner hållna som versionerad kod med ägare och granskning. Standardisera namngivning, granularitetsdeklarationer och strategier för långsamt föränderliga dimensioner över egendomen så att ett tal i ett verktyg matchar samma tal i ett annat. Behandla det semantiska lagret som en produkt med en färdplan och ett ägande team och mät hur mycket avstämningstid det tar bort. Avkastningen är pålitliga tal i hela verksamheten och revisioner som spårar rent från en styrelsepresentation tillbaka till källan.

**Offentlig sektor.** Transparens och jämförbarhet mellan myndigheter formar arbetet: kanonisk referensdata för geografi och demografi, styrda definitioner av kärnindikatorer och publicerad metodik med versionerade releaser så att allmänheten kan spåra vilken siffra som helst tillbaka till en dokumenterad definition. Upphandlingsregler kan kräva att era modeller och definitioner förblir portabla och leverantörsneutrala, så undvik ett semantiskt lager inlåst i ett proprietärt verktyg. Låt enskilda myndigheter modellera sin operativa data fritt samtidigt som de konformerar till gemensamma dimensioner för allt som rapporteras nationellt. En publicerad indikator som inte kan spåras till en versionerad definition är lika mycket ett ansvarsfel som ett datafel.

## Exempel

**Startup.** Ett företag i serie A hade tre definitioner av "aktiv användare" på tre ställen: produktanalysverktyget, ekonomins kalkylblad och investerarpresentationen. Talen stämde aldrig, och varje styrelseförberedelse blev en kapplöpning. Två ingenjörer införde ett litet semantiskt lager i sitt transformationsverktyg och definierade "aktiv användare" och "månatligt återkommande intäkt" en gång som testad kod, med de exakta fönstren och exkluderingarna nedskrivna. Varje panel läser nu de definitionerna. Styrelseförberedelseargumentet försvann, och att introducera en ny analytiker gick från en vecka av tyst kunskap till att läsa en dokumenterad modell. Detta kopplar direkt till den disciplin som beskrivs i kapitel 7.4 (produktanalys och experimentering), där en stabil definition av "aktiv" är det som gör experimentresultat jämförbara.

**Storföretag.** En global detaljhandlare körde fem business intelligence-verktyg över marknadsföring, ekonomi, leveranskedja, sortiment och butiker, och vart och ett hade uppfunnit "bruttomarginal" något olika. De byggde ett semantiskt lager ovanpå ett datalager i Kimball-stil med konformerade dimensioner, så att "produkt", "butik" och "datum" betydde detsamma över varje faktatabell och varje verktyg. Varje mått definierades en gång och konsumerades överallt. Avstämningsmöten som brukade äta dagar per kvartal försvann mestadels, och när ekonomi ändrade hur returer påverkade marginalen spreds ändringen till alla fem verktyg på en gång. De konformerade dimensionerna var det som lät oberoende team joina sin data med förtroende i stället för misstro.

**Offentlig sektor.** En nationell regering behövde jämförbar rapportering över hälso-, arbetsmarknads- och utbildningsmyndigheter, som alla historiskt definierat "hushåll", "region" och "sysselsättning" på sitt eget sätt. Ett myndighetsövergripande organ etablerade gemensam referensdata och standarddefinitioner: kanoniska dimensionstabeller för geografi och demografi och styrda definitioner av kärnindikatorer, publicerade med metodik och versionerade releaser. Enskilda myndigheter modellerar sin egen operativa data men konformerar till de gemensamma dimensionerna och definitionerna för allt som rapporteras nationellt. Resultatet är att en siffra från en myndighet kan jämföras med en annan ärligt, och allmänheten kan spåra vilken publicerad indikator som helst tillbaka till en dokumenterad definition, vilket stöder de transparensskyldigheter som behandlas i kapitel 7.1.

## Affärsnytta: motiv, ROI och TCO

Avkastningen på god modellering och ett semantiskt lager är mestadels återvunnen tid och undvikna fel. I många organisationer lägger analytiker majoriteten av sin tid på att hitta data, avstämma motstridiga tal och bygga om definitioner andra redan skrivit. En enda styrd definition av varje mått förvandlar det upprepade arbetet till en engångsinvestering. Den tar också bort en hel kategori dyra fel: det felaktiga talet i en styrelsepresentation, den felrapporterade siffran som utlöser en revisionsanmärkning, det kvartalslånga avstämningsprojektet som bara finns för att två team definierade "intäkt" olika. När definitionen bor på ett granskat ställe upphör de felen i stort sett att inträffa.

Kostnaden är verklig och värd att namnge. Du investerar i förväg i konceptuell och logisk modellering, i att bygga och fylla det semantiska lagret och i det löpande ägarskap som håller definitioner aktuella. Total ägandekostnad (TCO) inkluderar verktygen, modellerings- och analysteknik-tiden och styrningen för att hindra modellen från att driva. Väg det mot kostnaden för att inte göra det, som är större men dold: den visar sig som duplicerade pipelines, analytiker som mänskliga avstämningsmotorer och chefer som fattar självsäkra beslut på siffror ingen kan försvara. Driv ärendet inför ledningen på deras villkor. En pålitlig definition av varje mått är det som låter dem jämföra över verksamheten, lita på panelerna och svara tillsynsmyndigheter utan en brandövning. Börja där avstämningssmärtan är värst, definiera de få måtten en gång och låt den återvunna tiden finansiera resten.

## Antimönster och fallgropar

- Att hoppa direkt till fysiska tabeller och baka in dagens teknik i beslut som borde överleva den.
- Att definiera samma mått oberoende i varje panel, så att inga två tal stämmer.
- Att lämna granularitet ospecificerad och sedan upptäcka dubbelräknade mått i en intäktsrapport.
- Att denormalisera analytiska tabeller av misstag i stället för genom ett dokumenterat beslut.
- Att normalisera ett analytiskt datalager tills varje fråga är en tolvtabellsjoin ingen förstår.
- Att hantera långsamt föränderliga dimensioner genom överskrivning, så att historiska rapporter i tysthet skriver om det förflutna.
- Att använda naturliga nycklar överallt, så att en ändring av en källsystemnyckel ger krusningar genom hela datalagret.
- Att bygga ett semantiskt lager utan ägare, så att definitioner driver och förtroendet urholkas.
- Att behandla modellen som klar vid lansering i stället för en levande tillgång som måste förbli utvecklingsbar.

## Mognadsmodell

- **Nivå 1, Initiera:** Modellering är implicit och reaktiv. Tabeller designas fysiskt först av den som behöver dem. Mått omdefinieras i varje rapport, och tal står rutinmässigt i konflikt. Granularitet är odokumenterad, och ingen äger definitionerna.
- **Nivå 2, Utveckla:** Vissa analytiska tabeller följer ett dimensionellt mönster, och några nyckelmått har skrivna definitioner, men de bor i en wiki och upprätthålls inte. Namnkonventioner finns på papper. Praxis varierar team för team, och avstämning är fortfarande frekvent och manuell.
- **Nivå 3, Standardisera:** Konceptuella, logiska och fysiska modeller är separata och granskade. Ett semantiskt lager definierar kärnmått en gång, som versionerad kod med ägare. Konformerade dimensioner låter team joina säkert. Granularitet och strategier för långsamt föränderliga dimensioner är dokumenterade och upprätthålls i granskning över organisationen.
- **Nivå 4, Hantera:** Modellegendomen mäts mot utgångslägen. Ni följer täckning av måttdefinitioner (andelen rapporterade mått som betjänas av det semantiska lagret), antalet dubbla eller skuggdefinitioner som fortfarande används, avstämningstimmar per kvartal och frekvensen av granularitets- och ursprungsdefekter som fångas i granskning mot i produktion. Definitionsändringar flödar genom granskade pull requests med tester, och färskhet, godkännandefrekvens för tester och drift bevakas på paneler. När ett mått divergerar eller en dimension slutar konformera lyfter mätningen fram det innan ett styrelsemöte gör det.
- **Nivå 5, Orkestrera:** Varje viktigt mått har en styrd definition som konsumeras av alla verktyg och team, och det semantiska lagret är integrerat med analys, experimentering och reglerad rapportering. Modeller är utvecklingsbara genom design och förfinas kontinuerligt, definitioner är betrodda i hela organisationen och avstämningsarbetet har i stort sett försvunnit. Organisationen avvecklar, omdefinierar och konformerar rutinmässigt nya dimensioner när verksamheten förändras och balanserar om modellegendomen som en adaptiv tillgång.

## Idéer för diskussion

1. Välj era tre viktigaste mått. Hur många distinkta definitioner av vart och ett finns över era verktyg i dag, och vad skulle krävas för att kollapsa dem till en?
2. Var har en ospecificerad granularitet orsakat ett verkligt rapporteringsfel, och hur lång tid tog det att märka?
3. Vilka av era dimensioner bör konformeras över team först, och vem äger dem?
4. Ligger era måttdefinitioner i versionshantering med granskning, eller kan de redigeras tyst inuti ett BI-verktyg?
5. När skrev en långsamt föränderlig dimension senast om er historik utan att någon märkte, och hur skulle ni fånga det nästa gång?
6. Om ni bytte ut er datalagermotor i morgon, hur mycket av er modells betydelse skulle överleva flytten?

## Viktigaste punkter

- Datamodellering är att avgöra vad data betyder, och den betydelsen överlever varje lagringsteknik ni väljer.
- Modellera på tre nivåer i ordning: konceptuell, sedan logisk, sedan fysisk.
- Normalisera transaktionella system för korrekthet. Denormalisera analytiska medvetet för hastighet.
- Använd dimensionell modellering med fakta, dimensioner och en angiven granularitet för analys.
- Bygg ett semantiskt lager så att varje affärsmått har en enda styrd definition överallt.
- Konformerade dimensioner låter oberoende team joina och jämföra sin data med förtroende.
- Namnge väl, dokumentera, använd surrogatnycklar och versionera definitioner så att modellen förblir utvecklingsbar.

## Referenser och vidare läsning

- Ralph Kimball and Margy Ross, *The Data Warehouse Toolkit: The Definitive Guide to Dimensional Modelling*.
- Bill Inmon, *Building the Data Warehouse*.
- Dan Linstedt and Michael Olschimke, *Building a Scalable Data Warehouse with Data Vault 2.0*.
- Peter Chen, "The Entity-Relationship Model: Toward a Unified View of Data," ACM Transactions on Database Systems.
- E. F. Codd, "A Relational Model of Data for Large Shared Data Banks," Communications of the ACM.
- C. J. Date, *An Introduction to Database Systems*.
- Lars Rönnbäck and colleagues, writings on anchor modelling.
- DAMA International, *DAMA-DMBOK: Data Management Body of Knowledge*.
