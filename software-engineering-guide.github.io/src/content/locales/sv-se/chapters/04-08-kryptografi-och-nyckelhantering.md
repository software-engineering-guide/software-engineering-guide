# 4.8 Kryptografi och nyckelhantering

## Översikt och motivation

Nästan varje system du bygger beror redan på [kryptografi](https://en.wikipedia.org/wiki/Cryptography), praxisen att skydda information med matematiska tekniker så att bara de avsedda parterna kan läsa eller lita på den. Din webbtrafik färdas över krypterade kanaler, dina lösenord hashas, dina programvaruuppdateringar signeras och din kunddata ligger krypterad på disk. Det goda beskedet för de flesta ingenjörer är att du inte ombeds uppfinna något av detta. Det svåra är inte matematiken. Det är att använda beprövade byggstenar korrekt och, framför allt, att hantera de nycklar byggstenarna beror på.

Det här kapitlet är skrivet för ingenjörer som inte är kryptografer, vilket är nästan alla av oss. Du behöver tillräcklig förståelse för att göra sunda val, veta vad varje verktyg garanterar och undvika de misstag som förvandlar starka algoritmer till falsk trygghet. Kapitel 4.3 (infrastruktur- och molnsäkerhet) nämner kryptering och nyckelhantering i förbigående. Här går vi djupare in på vad som ska krypteras, hur och hur man driver den nyckellivscykel som gör det verkligt.

För stora företag sprider sig kryptografi över tusentals tjänster, certifikat och nycklar, och ett enda utgånget certifikat eller en förlorad nyckel kan ta ner ett kritiskt system eller läcka ett datalager. För myndigheter är kryptografi ofta föreskriven, validerad och granskad, med dataklassificeringsregler som dikterar exakt vilka nycklar som skyddar vilka hemligheter och vem som får hålla dem. I båda sammanhangen är det återkommande felet detsamma: goda algoritmer som förstörs av slarvig nyckelhantering.

## Nyckelprinciper

- **Rulla inte din egen kryptografi.** Använd beprövade, brett granskade bibliotek och standardalgoritmer. Nya scheman fallerar på sätt bara experter fångar.
- **Algoritmer är den lätta delen. Nycklar är den svåra.** Nyckelns livscykel är där de flesta verkliga fel bor.
- **Vet vad varje primitiv garanterar.** Konfidentialitet, integritet och autenticitet är olika egenskaper som kräver olika verktyg.
- **Kryptera under överföring och i vila som standard.** Gör skydd till standarden, inte ett val.
- **Skilj nyckelförvaring från dataåtkomst.** Den som hanterar en nyckel bör inte automatiskt kunna läsa datan den skyddar.
- **Planera för förändring.** Algoritmer försvagas, nycklar läcker och standarder utvecklas. Bygg för rotation och migrering från dag ett.
- **Föredra validerade implementationer där det spelar roll.** För reglerat arbete och myndighetsarbete, välj moduler med erkänd validering.

## Rekommendationer

### Rulla inte din egen kryptografi

Detta är den gyllene regeln och värd att nämna först. Designa aldrig din egen krypteringsalgoritm, uppfinn aldrig ditt eget protokoll och implementera aldrig en primitiv för hand från en artikel. Fungerande kryptografi ser enkel ut och döljer subtila felmönster (tidssidokanaler, paddingorakel, svag slumpmässighet) som bara överlever år av expertgranskning. Använd etablerade bibliotek som din plattforms standardmodul för kryptografi eller ett väl ansett bibliotek, och använd dem på den högsta abstraktionsnivå som finns. Sträck dig efter autentiserade krypteringslägen och "enkla" gränssnitt som gör det säkra valet till standard, snarare än att sätta ihop lågnivådelar själv.

### Matcha primitiven mot den garanti du behöver

Olika verktyg ger olika garantier, och att blanda ihop dem är ett vanligt och farligt misstag. Lär dig de tre huvudfamiljerna.

- **[Symmetrisk nyckel](https://en.wikipedia.org/wiki/Symmetric-key_algorithm)**-kryptografi använder en delad hemlig nyckel för att både kryptera och dekryptera. Den är snabb och skyddar **konfidentialitet**, men båda parter måste redan dela nyckeln. AES är standardens arbetshäst.
- **[Publik nyckel](https://en.wikipedia.org/wiki/Public-key_cryptography)**-kryptografi använder ett matematiskt länkat nyckelpar: en publik nyckel vem som helst kan hålla och en privat nyckel du håller hemlig. Den löser nyckeldistribution och möjliggör **digitala signaturer**, som bevisar **autenticitet** (vem som skickade det) och **integritet** (att det inte ändrades).
- En **[kryptografisk hashfunktion](https://en.wikipedia.org/wiki/Cryptographic_hash_function)** producerar ett fingeravtryck av fast storlek av data och ger kontroll av **integritet**. Hashning är enkelriktad och är inte kryptering. För att lagra lösenord, använd en långsam, saltad lösenordshashfunktion, aldrig en vanlig snabb hash (se kapitel 4.2 om applikationssäkerhet).

Den praktiska läxan: kryptering döljer data men bevisar inte vem som skickade den, och en hash upptäcker manipulering men döljer ingenting. De flesta verkliga system kombinerar dem, vilket är precis varför du bör lita på bibliotek som buntar dessa korrekt.

### Kryptera under överföring med aktuell TLS

Skydda varje nätverkshopp med [Transport Layer Security](https://en.wikipedia.org/wiki/Transport_Layer_Security) (TLS), protokollet som säkrar data när den rör sig mellan system. Kräv moderna TLS-versioner, stäng av föråldrade, välj starka chiffersviter och validera certifikat ordentligt snarare än att stänga av kontroller för att "få det att fungera". Kryptera även intern trafik mellan tjänster, inte bara den publika kanten, eftersom en nolltillitshållning antar att det interna nätverket är fientligt. Automatisera utfärdande och förnyelse av certifikat så att TLS är den friktionsfria standarden överallt.

### Kryptera i vila med kuvertkryptering

Kryptera lagrad data som standard: databaser, objektlagring, säkerhetskopior och loggar. Standardmönstret är **kuvertkryptering (envelope encryption)**, där en **datakrypteringsnyckel (DEK)** krypterar själva datan och en **nyckelkrypteringsnyckel (KEK)** hållen i en nyckelhanteringstjänst krypterar DEK. Det låter dig rotera huvudnyckeln utan att omkryptera terabyte data, och det håller den mäktiga rotnyckeln innanför en härdad gräns. Lagra bara den inslagna DEK bredvid datan och hämta och packa upp den vid användning.

### Driv nyckelns livscykel medvetet

Nyckelns livscykel är den genuint svåra delen av kryptografi, och där de flesta intrång och avbrott har sitt ursprung. Hantera varje steg med avsikt:

- **Generering:** skapa nycklar från en stark slumpkälla, med lämplig styrka.
- **Distribution:** få nycklar till de system som behöver dem utan att exponera dem i kod, konfigurationsfiler eller chatt.
- **Rotation:** ersätt nycklar enligt schema och kunna rotera snabbt vid misstänkt komprometterande.
- **Återkallelse:** ogiltigförklara en komprometterad nyckel eller ett certifikat snabbt och se till att system hedrar återkallelsen.
- **Förstörelse:** gallra gammalt nyckelmaterial säkert så att det inte kan återskapas.

Använd en **nyckelhanteringstjänst (KMS)** för att centralisera detta, och använd en [hårdvarusäkerhetsmodul](https://en.wikipedia.org/wiki/Hardware_security_module) (HSM), en manipuleringsresistent enhet som genererar och vaktar nycklar så att de aldrig lämnar i klartext, för dina nycklar med högst säkring. Skilj vem som kan hantera nycklar från vem som kan läsa den skyddade datan, så att nyckelförvaring upprätthåller åtskillnad av ansvarsområden. Detta hänger direkt ihop med dataklassificering och förvaringsregler i kapitel 4.5 (integritet och dataskydd).

### Skilj hemlighetshantering från nyckelhantering

Dessa överlappar men är inte detsamma. **Nyckelhantering** styr kryptografiska nycklar och deras livscykel, vanligen inuti en KMS eller HSM som utför kryptografiska operationer åt dig så att råa nyckeln aldrig lämnar. **Hemlighetshantering** styr applikationsuppgifter (databaslösenord, API-tokens, certifikat) som tjänster behöver hämta och använda i klartext, vanligen från ett hemlighetsvalv med kortlivad, granskad åtkomst. Använd en KMS för nycklar, en hemlighetshanterare för uppgifter och klistra aldrig in någotdera i källkod eller miljöfiler som checkats in i versionshantering.

### Automatisera PKI och certifikatens livscykler

**Infrastruktur för publika nycklar (PKI)** är systemet av certifikatutfärdare, certifikat och förtroendekedjor som binder publika nycklar till identiteter. I skala är den dominerande PKI-risken det överraskande certifikatutgången som tar ner en tjänst. Underhåll en inventering av varje certifikat, övervaka utgångsdatum och automatisera utfärdande och förnyelse så att ingen människa behöver minnas. Kortlivade certifikat som förnyas automatiskt är säkrare än långlivade som vårdas för hand, eftersom automation tar bort den mänskliga enskilda felpunkten. Standardprotokoll här stöder interoperabilitet över leverantörer (kapitel 3.8 om interoperabilitet och öppna standarder).

### Bygg för kryptografisk smidighet och post-kvantmigrering

Algoritmer försvagas över tid, och standarder rör sig. **Kryptografisk smidighet (cryptographic agility)** betyder att designa system så att du kan byta algoritmer och nyckelstorlekar utan en smärtsam omskrivning: abstrahera kryptografi bakom ett litet gränssnitt, versionera din krypterade data så att du vet vilken algoritm som producerade den och för en kryptografiinventering över vad du använder var. Detta spelar roll nu på grund av [post-kvantkryptografi](https://en.wikipedia.org/wiki/Post-quantum_cryptography), den nya familjen av algoritmer designade för att motstå framtida kvantdatorer. Motståndare kan skörda krypterad data i dag för att dekryptera senare, så långlivade hemligheter behöver en migreringsplan. Du behöver inte få panik, men du bör känna till din inventering och vara redo att anta de standardiserade post-kvantalgoritmerna när plattformar levererar dem.

### Föredra validerade implementationer där det krävs

För reglerade system och myndighetssystem räcker det inte att använda en stark algoritm. Implementationen måste vara validerad. **FIPS 140** (Federal Information Processing Standard 140) är den amerikanska standarden för validering av kryptografiska moduler, och många avtal kräver FIPS-validerad kryptografi. Myndighetsarbete kan också följa nationell vägledning som NSA:s Commercial National Security Algorithm (CNSA)-svit för sekretessbelagda system. Kontrollera vilken regim som gäller innan du bygger, eftersom att eftermontera validerade moduler sent är dyrt. Detta knyter an till belägg för regelefterlevnad och styrning (kapitel 4.6).

## Avvägningar: för- och nackdelar

| Beslut | Fördelar | Nackdelar |
|---|---|---|
| Leverantörshanterad KMS | Enkelt, integrerat, låg driftbörda | Leverantören håller förvaringen. Mindre direkt kontroll |
| Kundhanterade nycklar / HSM | Full förvaring, möter strikta krav | Driftoverhead, risk att förlora nycklar |
| Automatiserade kortlivade certifikat | Inga överraskande utgångar, snabb återkallelse | Kräver automationsinvestering i förväg |
| Långlivade certifikat | Enkelt, färre rörliga delar | Mänskligt hanterade utgångsdatum orsakar avbrott |
| Kuvertkryptering | Billig nyckelrotation, skyddar huvudnyckeln | Fler rörliga delar att förstå |
| Kryptografisk smidighet i förväg | Billiga framtida migreringar | Extra abstraktion och designinsats nu |
| Tidigt antagande av post-kvant | Skyddar långlivade hemligheter | Omogna verktyg, större nycklar, viss risk |

Den centrala spänningen är kontroll mot driftbörda. Att hålla egna nycklar i en HSM ger maximal förvaring och uppfyller de strängaste kraven, men det kräver expertis och skapar en ny katastrofal risk: förlora nyckeln och du förlorar datan, oåterkalleligt. Leverantörshanterade tjänster tar bort den bördan men placerar förvaringen hos leverantören. Lös det genom att lagerindela: använd hanterade tjänster med förnuftiga standardvärden för de flesta system och reservera kundhanterade nycklar och HSM för data med högst klassificering där den extra kontrollen är värd kostnaden och risken.

## Frågor att diskutera med ditt team

1. **Har ni en fullständig inventering av era nycklar, certifikat och de algoritmer ni förlitar er på?** Ni kan inte rotera, migrera eller granska det ni inte kan se, och de flesta organisationer upptäcker att de har långt mer kryptografiskt material utspritt över tjänster än någon följer. En inventering är förutsättningen för varje senare beslut: övervakning av certifikatutgång, nyckelrotation, FIPS-avgränsning och post-kvantplanering beror alla på den. Ta med en lista över era nuvarande certifikat och deras utgångsdatum och fråga vem som äger varje och vad som går sönder när det löper ut. För en stor egendom är det ärliga svaret vanligen att ingen enskild sanningskälla finns, och att bygga en är det mest hävstångsstarka första steget. Om ni inte kan räkna upp er kryptografi i dag är smidighet och rotation ambitioner, inte förmågor.

2. **Kan ni rotera eller återkalla en komprometterad nyckel snabbt, och har ni någonsin övat det?** Rotation och återkallelse är de delar av nyckelns livscykel som bara spelar roll under tryck, och team upptäcker rutinmässigt under en incident att en nyckel är hårdkodad på ett dussin ställen eller att återkallelse faktiskt inte propagerar. Besluta ert måltid för att rotera en nyckel och återkalla ett certifikat och öva det sedan innan ni behöver det. Ta med berättelsen om er senaste uppgiftsexponering och gå igenom vad rotationen krävde i praktiken. För företags- och myndighetssystem kan en oövad rotation betyda att välja mellan en förlängd exponering och ett självförvållat avbrott. Om rotation aldrig har testats, anta att den inte fungerar.

3. **Var sitter nyckelförvaringen, och upprätthåller den åtskillnad av ansvarsområden?** Den som kan hantera en nyckel och den som kan läsa datan den skyddar bör inte vara samma person, eftersom att slå samman dessa befogenheter i tysthet motverkar syftet med kryptering i vila. Det här valet driver också om ni använder leverantörshanterade nycklar, kundhanterade nycklar eller HSM, var och en med olika kontroll och olika driftrisk. Ta med era nuvarande nyckelpolicyer och kontrollera om någon enskild identitet både kan administrera en nyckel och komma åt klartexten bakom den, vilket är en vanlig tyst lucka. För reglerad och sekretessbelagd data kan förvaringsregler dikteras av dataklassificering (kapitel 4.5) och av föreskrifter. Om förvaring och åtkomst inte är åtskilda skyddar er kryptering er mindre än panelen antyder.

4. **Hur skulle ni återhämta er om huvudnyckeln som skyddar er kuvertkryptering förlorades eller förstördes?** Kundhanterade nycklar och HSM ger er förvaring, men de ger er ett nytt katastrofalt felmönster: förlora nyckelkrypteringsnyckeln och varje datakrypteringsnyckel den slår in blir permanent oläsbar, tillsammans med datan bakom dem. Väg detta mot den motsatta risken av en alltför bred säkerhetskopia som i tysthet återskapar just det förvaringsproblem ni försökte lösa. Ta med era nuvarande arrangemang för nyckelsäkerhetskopiering och deponering, sprängradien för varje huvudnyckel och belägg för att en återställning faktiskt har utförts snarare än bara dokumenterats. För företags- och myndighetsegendomar, knyt detta till era dataklassificeringsregler: de känsligaste nycklarna förbjuder ofta tillfälliga kopior, så återhämtning måste designas medvetet, testas enligt schema och förenas med varje regulatoriskt krav på att bevisa att pensionerat nyckelmaterial förstördes.

5. **Hur redo är era system för en post-kvantmigrering, och vilka långlivade hemligheter skulle ni migrera först?** Motståndare kan skörda krypterad trafik och arkiv i dag och dekryptera dem när kvantdatorer mognar, så varje hemlighet som måste förbli konfidentiell i åratal är redan exponerad för en framtid ni inte kan se. Det konkurrerande trycket är att post-kvantverktyg fortfarande är unga, nycklarna är större och att röra sig för tidigt riskerar att satsa på en algoritm som skiftar innan den sätter sig. Ta med er kryptografiinventering, en lista över hemligheter rangordnade efter hur länge de måste förbli konfidentiella och en ärlig läsning av om er arkitektur kan byta algoritmer utan en omskrivning. För myndighets- och reglerat arbete gör handlingar med konfidentialitetskrav på flera decennier detta konkret snarare än teoretiskt, och upphandling kan snart kräva en dokumenterad migreringsplan och stöd för de standardiserade post-kvantalgoritmerna.

6. **När reglering kräver validerad kryptografi, vet ni exakt vilka moduler som omfattas och om de kvalificerar sig?** Att använda en stark algoritm är inte detsamma som att använda en validerad implementation, och team upptäcker rutinmässigt sent att ett bibliotek, en språkkörmiljö eller en molntjänst inte täcks av den FIPS 140-gräns ett avtal kräver. Spänningen är att validerade moduler kan ligga efter aktuella bibliotek i funktioner och hastighet, så att välja dem begränsar er stack på sätt som spelar roll för tekniken. Ta med listan över kryptografiska moduler varje reglerat system faktiskt anropar, de valideringscertifikat som täcker dem och det specifika kravet (FIPS 140, CNSA eller en sektorsregel) som gäller. För företags- och myndighetsprogram, besluta detta innan ni bygger, eftersom att eftermontera validerade moduler och återauktorisera ett system i efterhand är dyrt, långsamt och ofta tvingar fram en omdesign av just de komponenter ni trodde var färdiga.

## Sektorsperspektiv

**Startup.** Lita helt på din plattforms beprövade standardvärden och lägg noll ingenjörstid på egen kryptografi. Slå på hanterad kryptering i vila, avsluta TLS med automatiskt förnyade certifikat, hasha lösenord med en vanlig långsam funktion och håll hemligheter i plattformens hemlighetshanterare snarare än repositoriet. Ditt enda designbeslut är ett tunt gränssnitt runt den handfull fält du krypterar i applikationen, så att ett framtida byte bort från leverantörshanterade nycklar inte är en omskrivning.

**Småföretag.** Du har ingen kryptograf och liten lust att driva en HSM, så köp förvaring snarare än att bygga den: använd den leverantörshanterade KMS och hemlighetshanterare som följer med ditt moln eller dina SaaS-verktyg. Ramma in arbetet som hygien, det vill säga inga nycklar i kod, kryptering påslagen överallt som standard och certifikatutgångar övervakade så att inget förfaller av överraskning. Reservera kundhanterade nycklar för den sällsynta data ett avtal eller en tillsynsmyndighet genuint kräver dem för.

**Storföretag.** Problemet är skala och konsekvens över tusentals tjänster, certifikat och nycklar. Kör en centraliserad KMS med kuvertkryptering, automatisera hela certifikatlivscykeln så att inget utgångsdatum vårdas för hand och underhåll en enda kryptografiinventering som matar rotation, FIPS-avgränsning och post-kvantplanering. Skilj nyckelförvaring från dataåtkomst som en kontroll för hela organisationen och gör kryptering till en plattformsförmåga varje team ärver snarare än en uppgift varje team uppfinner på nytt.

**Offentlig sektor.** Upphandling, validering och revision formar varje val. Använd FIPS 140-validerade moduler och följ nationell vägledning som CNSA för sekretessbelagda system, knyt nyckelförvaring till dataklassificering så att de känsligaste nycklarna sitter hos säkerhetsprövad personal under strikt åtskillnad av ansvarsområden och generera kontinuerliga belägg för validerad kryptografi för löpande auktorisering. Dokumentera en post-kvantmigreringsplan för handlingar som måste förbli konfidentiella i decennier och kräv att leverantörer redovisar vilka moduler som är validerade innan ni binder er.

## Exempel

**Startup.** Ett litet team som bygger en hälsospårningsapp lutar sig helt mot beprövade standardvärden. De avslutar TLS med automatiskt förnyade certifikat, slår på kryptering i vila på sin hanterade databas och objektlagring med leverantörens KMS och hashar lösenord med en långsam, saltad funktion från ett standardbibliotek. I stället för att skriva någon kryptografi själva använder de ett autentiserat krypteringsanrop på hög nivå för det enda fält de måste kryptera i applikationen. Hemligheter bor i plattformens hemlighetshanterare, aldrig i repositoriet. Det kostar några eftermiddagar och tar bort en hel kategori katastrofala misstag.

**Storföretag.** En global bank kör en centraliserad KMS och en flotta HSM, med en kryptografiinventering som följer varje nyckel och certifikat över tusentals tjänster. Kuvertkryptering skyddar kunddata, med datanycklar inslagna av huvudnycklar som roteras enligt schema medan datan stannar kvar. Utfärdande och förnyelse av certifikat är helt automatiserade efter att ett publikt vänt avbrott lärde dem kostnaden för ett enda utgånget certifikat. Nyckeladministratörer är ett separat team från applikationsingenjörer, så att förvaring upprätthåller åtskillnad av ansvarsområden, och ett lager för kryptografisk smidighet låter dem börja pilota post-kvantalgoritmer för långlivade arkiv.

**Offentlig sektor.** En nationell myndighet som hanterar sekretessbelagda handlingar använder enbart FIPS 140-validerade kryptografiska moduler och följer NSA:s CNSA-vägledning för sina system med högst klassificering. Nycklar genereras och hålls i HSM som aldrig släpper ut nyckelmaterial i klartext, och förvaringen är knuten till dataklassificering så att de känsligaste nycklarna sitter hos säkerhetsprövad personal under strikt åtskillnad av ansvarsområden. Certifikat körs på en hanterad intern PKI med automatiserade livscykler, och kontinuerliga belägg för validerad kryptografi matar myndighetens löpande auktorisering. En dokumenterad post-kvantmigreringsplan skyddar handlingar som måste förbli konfidentiella i decennier.

## Affärsnytta: motiv, ROI och TCO

Kryptografi är ytterligare ett område där en blygsam investering förhindrar katastrofala förluster på rubriknivå. Den totala ägandekostnaden inkluderar en KMS eller HSM, verktyg för hemlighets- och certifikathantering och ingenjörstiden för att designa livscykler och hålla en inventering aktuell. Dessa kostnader är verkliga men begränsade. Kostnaden för att hoppa över dem är ett intrång i okrypterad data, ett avbrott på flera timmar från ett utgånget certifikat eller en oåterkallelig dataförlust från en felhanterad nyckel, var och en med regulatoriska viten, underrättelsekostnader och varaktig anseendeskada.

Den starkaste ROI kommer av automation och återanvändning. Automatiserade certifikatlivscykler eliminerar det enskilt vanligaste självförvållade avbrottet. Centraliserad nyckelhantering med förnuftiga standardvärden betyder att varje ny tjänst ärver kryptering under överföring och i vila utan insats per team, vilket förvandlar kryptografi från en återkommande skatt till en plattformsförmåga. För reglerat arbete och myndighetsarbete sänker validerade moduler och automatiserade belägg också kostnaden för revisioner och auktorisering. När du driver ärendet inför ledningen, ramma in det rakt: algoritmerna är gratis och beprövade, risken bor i nyckelhantering och certifikatdrift, och en liten, automatiserad investering där förhindrar de dyra felen.

## Antimönster och fallgropar

- **Att rulla egen kryptografi.** Egna algoritmer eller handbyggda protokoll som fallerar på subtila, expertbara sätt.
- **Hårdkodade nycklar och hemligheter.** Uppgifter inklistrade i källkod, konfigurationsfiler eller chatt, där de läcker och inte kan roteras.
- **Kryptering utan nyckeldisciplin.** Att slå på kryptering men lämna nyckelåtkomsten vidöppen eller aldrig rotera.
- **Att blanda ihop hashning med kryptering.** Att behandla en hash som reversibel, eller lagra lösenord med en snabb hash i stället för en långsam, saltad.
- **Certifikatroulette.** Ingen inventering, ingen övervakning av utgångsdatum och periodiska överraskande avbrott när ett certifikat löper ut.
- **Sammanslagen nyckelförvaring och dataåtkomst.** En identitet som både kan hantera en nyckel och läsa datan den skyddar.
- **Ingen rotationsplan.** Nycklar som aldrig roterats och inte kan roteras snabbt under tryck.
- **Kryptografi utan smidighet.** Algoritmer kopplade så djupt att byte kräver en omskrivning och blockerar varje framtida migrering.
- **Att ignorera valideringskrav.** Att använda starka algoritmer i ovaliderade moduler där FIPS eller liknande validering krävs.

## Mognadsmodell

- **Nivå 1, Initiera:** Kryptering är inkonsekvent och ofta frånvarande, tillämpad reaktivt när någon märker en lucka. Nycklar och hemligheter är hårdkodade eller delas informellt över chatt och konfigurationsfiler. Det finns ingen inventering, ingen rotation och certifikat löper ut av överraskning, och team skriver ibland egen kryptografi.
- **Nivå 2, Utveckla:** TLS och kryptering i vila är påslagna för de stora systemen och en KMS eller hemlighetshanterare finns, men användningen är ojämn och varierar team för team. Vissa certifikat övervakas medan andra inte gör det, rotation är manuell och sällsynt och ingen fullständig kryptografiinventering binder ihop det.
- **Nivå 3, Standardisera:** Kryptering under överföring och i vila är den dokumenterade standarden som upprätthålls i hela organisationen. Nycklar bor i en KMS med schemalagd rotation och kuvertkryptering, nyckelförvaring är skild från dataåtkomst, certifikatlivscykler är automatiserade, en kryptografiinventering underhålls och validerade moduler används överallt där reglering kräver dem.
- **Nivå 4, Hantera:** Kryptoegendomen mäts och styrs mot utgångslägen. Ni följer ledtid för certifikatutgång, andelen nycklar roterade enligt schema, genomsnittlig tid att återkalla en komprometterad nyckel, detekteringar av hemligheter i kod per period och inventeringstäckning och granskar dessa mått mot mål. Rotation och återkallelse övas med fast takt med registrerade tider, och avvikelser utlöser korrigerande åtgärd i stället för att gå obemärkta förbi.
- **Nivå 5, Orkestrera:** Kryptografi är en plattformsförmåga varje tjänst ärver som standard, och den förbättras kontinuerligt och är integrerad i hela organisationen. Rotation och återkallelse är snabba och rutinmässigt utövade, HSM skyddar nycklarna med högst säkring och kryptografisk smidighet plus en aktiv post-kvantmigreringsplan håller egendomen adaptiv när algoritmer och krav skiftar. Belägg för regelefterlevnad produceras automatiskt och matar löpande auktorisering.

## Idéer för diskussion

1. Vilka system i er egendom motiverar kundhanterade nycklar eller HSM med tanke på deras driftkostnad och risk för katastrofal förlust?
2. Hur skulle ni bygga och underhålla en enda sanningskälla för varje nyckel och certifikat ni äger?
3. Vad är er realistiska tid att rotera en komprometterad nyckel i dag, och vad gör den långsam?
4. Var gör er arkitektur det svårt att byta en kryptografisk algoritm, och hur skulle ni rätta det före en påtvingad migrering?
5. Vilka av era långlivade hemligheter skulle spela roll om en motståndare skördade dem nu och dekrypterade dem år senare?
6. Hamnar hemligheter och nycklar någonsin i kod, konfiguration eller loggar, och hur skulle ni veta det?

## Viktigaste punkter

- **Rulla inte din egen kryptografi.** Använd beprövade bibliotek och standardalgoritmer på högsta säkra abstraktion.
- **Algoritmer är lätta. Nyckelhantering är svår.** Nyckelns livscykel (generering, distribution, rotation, återkallelse, förstörelse) är där verkliga fel bor.
- **Känn dina garantier:** symmetrisk kryptering och kryptering med publik nyckel skyddar konfidentialitet, signaturer bevisar autenticitet och integritet och hashning upptäcker manipulering men är inte kryptering.
- **Kryptera under överföring med aktuell TLS och i vila med kuvertkryptering**, som standard för varje system.
- **Skilj nyckelförvaring från dataåtkomst**, använd en KMS för nycklar och en hemlighetshanterare för uppgifter och hårdkoda aldrig någotdera.
- **Automatisera certifikatlivscykler** för att döda avbrottet av överraskande utgång och för en kryptografiinventering.
- **Bygg för kryptografisk smidighet** och starta en post-kvantmigreringsplan för långlivade hemligheter.
- **Föredra validerade implementationer** (FIPS 140 och tillämplig nationell vägledning) där reglering eller klassificering kräver dem.

## Referenser och vidare läsning

- National Institute of Standards and Technology, *FIPS 140-3: Security Requirements for Cryptographic Modules*.
- National Institute of Standards and Technology, *SP 800-57: Recommendation for Key Management*.
- National Institute of Standards and Technology, *SP 800-131A: Transitioning the Use of Cryptographic Algorithms and Key Lengths*.
- National Institute of Standards and Technology, post-quantum cryptography standards (FIPS 203, 204, and 205).
- Niels Ferguson, Bruce Schneier, and Tadayoshi Kohno, *Cryptography Engineering*.
- Jean-Philippe Aumasson, *Serious Cryptography*.
- David Wong, *Real-World Cryptography*.
- Internet Engineering Task Force, *RFC 8446: The Transport Layer Security (TLS) Protocol Version 1.3*.
- Open Web Application Security Project, *Cryptographic Storage Cheat Sheet* and *Transport Layer Protection Cheat Sheet*.
- National Security Agency, *Commercial National Security Algorithm (CNSA) Suite* guidance.
