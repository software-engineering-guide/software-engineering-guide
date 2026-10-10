# 4.3 Infrastruktur- och molnsäkerhet

## Översikt och motivation

Applikationer körs på infrastruktur, och numera är den infrastrukturen till stor del molnbaserad, programvarudefinierad och ständigt föränderlig. En enda ingenjör kan nu provisionera en databas, öppna en nätverksväg eller bevilja en behörighet med ett kommando, i en skala och hastighet som traditionell ändringskontroll aldrig förutsåg. Den kraften är precis varför felkonfiguration, inte exotiska exploateringar, är den ledande orsaken till molnintrång. En av misstag publik lagringshink eller en alltför bred åtkomstroll kan exponera en hel organisations data på sekunder.

För stora företag spänner molninfrastruktur över flera leverantörer, tusentals konton och en blandning av hanterade tjänster, containrar och serverlösa funktioner. Angreppsytan är ingen statisk perimeter. Den är en levande, vidsträckt samling resurser och identiteter. För myndigheter möter samma komplexitet strikta godkännanderegimer, krav på dataplacering och klassificeringsgränser som formar varje arkitekturval. I båda har identitetslagret blivit den nya perimetern: vem som kan göra vad, med vilken resurs, under vilka villkor.

Det här kapitlet behandlar hur man säkrar den grunden: [identitets- och åtkomsthantering](https://en.wikipedia.org/wiki/Identity_management) (IAM), [nätverkssegmentering](https://en.wikipedia.org/wiki/Network_segmentation), [kryptering](https://en.wikipedia.org/wiki/Encryption) och [nyckelhantering](https://en.wikipedia.org/wiki/Key_management), säkerheten hos containrar och [serverlösa](https://en.wikipedia.org/wiki/Serverless_computing) arbetslaster samt den kontinuerliga hantering av säkerhetsläget som hindrar en snabbrörlig molnegendom från att driva in i fara.

## Nyckelprinciper

- **Identitet är perimetern.** Åtkomstbeslut hänger på stark identitet och finkornig auktorisering, inte nätverksplats.
- **Minsta behörighet, alltid.** Varje identitet, mänsklig eller maskin, får de minsta behörigheter som behövs och inte fler.
- **Segmentera för att begränsa.** Dela upp nätverk och arbetslaster så att ett intrång i ett område inte fritt kan sprida sig.
- **Kryptera överallt.** Skydda data under överföring och i vila som standard, med välhanterade nycklar.
- **Oföränderligt och deklarativt.** Definiera infrastruktur som kod (IaC), driftsätt oföränderligt och behandla drift som en defekt.
- **Kontinuerlig verifiering.** Säkerhetsläget är inte en engångsrevision. Skanna och upprätthåll kontinuerligt.
- **Säker standardkonfiguration.** Standardtillståndet för varje resurs bör vara låst, inte öppet.

## Rekommendationer

### Designa identitets- och åtkomsthantering medvetet

IAM är den viktigaste delen av molnsäkerhet, och den som oftast hanteras fel.

- Använd **[rollbaserad åtkomstkontroll](https://en.wikipedia.org/wiki/Role-based_access_control) (RBAC)** för att ge behörigheter efter arbetsfunktion, och **[attributbaserad åtkomstkontroll](https://en.wikipedia.org/wiki/Attribute-based_access_control) (ABAC)** där finkornigare, kontextmedvetna beslut behövs (baserade på taggar, miljö, dataklassificering eller tid).
- Eliminera långlivade statiska uppgifter till förmån för kortlivade, automatiskt utfärdade tokens och federation av arbetslastidentitet.
- Upprätthåll [MFA](https://en.wikipedia.org/wiki/Multi-factor_authentication) (flerfaktorsautentisering) för all mänsklig åtkomst och kräv stark autentisering för privilegierade åtgärder.
- Tillämpa minsta behörighet rigoröst: börja från noll och lägg till behörigheter medvetet. Granska och beskär oanvända behörigheter regelbundet, eftersom åtkomst tenderar att ackumuleras.
- Separera ansvarsområden så att ingen enskild identitet både kan göra och godkänna känsliga ändringar.
- Använd dedikerade konton eller projekt för att skapa hårda gränser mellan miljöer (produktion, staging, utveckling) och mellan affärsenheter.

### Segmentera nätverk och mikrosegmentera arbetslaster

Platta nätverk låter angripare röra sig i sidled när de väl är inne. Dela upp och begränsa.

- Segmentera på nätverksnivå i nivåer och zoner och tillåt bara den trafik varje nivå legitimt behöver.
- Tillämpa **mikrosegmentering** så att enskilda arbetslaster bara kommunicerar med de specifika kamrater de kräver, upprätthållet av identitetsmedveten policy snarare än breda delnätsregler.
- Neka öst-väst-trafik som standard. Kräv uttryckliga tillåtregler.
- Placera känsliga datalager i privata delnät utan direkt internetexponering, nådda endast genom kontrollerade vägar.
- Använd privat anslutning till hanterade tjänster i stället för att dirigera över det publika internet där det är möjligt.

### Kryptera data och hantera nycklar ordentligt

Kryptering är aldrig starkare än nyckelhanteringen bakom den.

- Kryptera **under överföring** med aktuell [TLS](https://en.wikipedia.org/wiki/Transport_Layer_Security) (Transport Layer Security) överallt, inklusive intern trafik mellan tjänster.
- Kryptera **i vila** som standard för all lagring, alla databaser och säkerhetskopior.
- Hantera nycklar med en **nyckelhanteringstjänst (KMS)** och använd en **[hårdvarusäkerhetsmodul](https://en.wikipedia.org/wiki/Hardware_security_module) (HSM)** för nycklar med högst säkring och för regulatoriska krav.
- Rotera nycklar enligt schema och stöd snabb rotation vid misstänkt komprometterande.
- Kontrollera och granska vem som kan använda och hantera nycklar separat från vem som kan komma åt datan, så att nyckelförvaring upprätthåller åtskillnad av ansvarsområden.
- Överväg kundhanterade nycklar där reglering eller avtalsenligt förtroende kräver att organisationen håller nycklarna snarare än leverantören.

### Säkra containrar, Kubernetes och serverlöst

Varje beräkningsmodell för med sig sina egna risker.

- **Containrar:** bygg från minimala, betrodda basavbilder. Skanna avbilder efter sårbarheter före driftsättning. Kör som icke-root. Gör filsystem skrivskyddade där det är möjligt. Baka aldrig in hemligheter i avbilder.
- **[Kubernetes](https://en.wikipedia.org/wiki/Kubernetes):** slå på RBAC och avgränsa tjänstekonton snävt. Tillämpa nätverkspolicyer för mikrosegmentering. Använd tillträdeskontroller och policymotorer för att upprätthålla standarder. Begränsa privilegierade containrar. Isolera känsliga arbetslaster. Håll kontrollplanet och noderna patchade.
- **Serverlöst:** tillämpa minsta behörighet på varje funktions exekveringsroll (en vanlig källa till överbehörighet). Validera all händelseindata. Hantera hemligheter genom plattformens hemlighetslager. Övervaka avvikande anropsmönster.

Oavsett modell, håll körmiljön patchad och avbilderna färska. En container är bara så säker som programvaran inuti den.

### Hantera molnets säkerhetsläge kontinuerligt

Molnet förändras långt för snabbt för att periodiska manuella revisioner ska hänga med.

- Anta verktyg för **Cloud Security Posture Management (CSPM)** för att kontinuerligt upptäcka felkonfigurationer, publik exponering och policyöverträdelser över konton.
- Definiera säkerhetspolicy som kod och upprätthåll den vid driftsättning så att dåliga konfigurationer blockeras innan de landar.
- Föredra förebyggande (skyddsräcken som stoppar felkonfiguration) framför detekterande (larm i efterhand), och kombinera båda.
- Underhåll en korrekt inventering av resurser och identiteter. Du kan inte säkra det du inte kan se.
- Följ och åtgärda drift mellan deklarerad infrastruktur som kod och det faktiska körande tillståndet.

## Avvägningar: för- och nackdelar

| Beslut | Fördelar | Nackdelar |
|---|---|---|
| RBAC | Enkelt, begripligt, lätt att granska | Grovkornigt, rollexplosion i skala |
| ABAC | Finkornigt, kontextmedvetet, skalar med taggar | Komplext att designa och resonera om |
| Leverantörshanterade nycklar (KMS) | Enkelt, integrerat, låg driftbörda | Leverantören håller förvaringen. Mindre kontroll |
| Kundhanterade nycklar/HSM | Full kontroll, möter strikta krav | Driftoverhead, risk att förlora nycklar |
| Förebyggande skyddsräcken | Stoppar felkonfiguration innan den sker | Kan blockera legitimt arbete, behöver justeras |
| Enbart detekterande CSPM | Flexibelt, icke-blockerande | Skada kan ske före upptäckt |
| Mikrosegmentering | Stark begränsning av lateral rörelse | Driftkomplexitet, policyspridning |

Den dominerande avvägningen är kontroll mot driftbörda. Snävare kontroller (kundhanterade nycklar, strikt mikrosegmentering, ABAC) minskar risken, men de kräver expertis och underhåll som små team har svårt att upprätthålla. Rätt nivå beror på hur känslig datan är och vilka regleringar som gäller. Ett pragmatiskt tillvägagångssätt lagrar starka säkra standardvärden för alla och reserverar sedan extra rigor för de högriskigaste systemen, och det föredrar automatiserade skyddsräcken som gör det säkra valet till standard snarare än en manuell disciplin.

## Frågor att diskutera med ditt team

1. **Var ska ni dra hårda konto- eller projektgränser, och vad hör hemma inom var och en?** Dedikerade konton och projekt skapar den starkaste begränsning molnet erbjuder, så att ett intrång i utveckling inte kan nå produktion och en affärsenhet inte kan röra en annans data. Besluta er gränsstruktur innan er egendom växer till tusentals konton, eftersom att eftermontera isolering på en platt struktur är långsamt och riskabelt. För företags- och myndighetsarbete mappar dessa gränser också rent till miljöseparation, dataklassificering och de begränsningar av sprängradie som revisorer förväntar sig att se. Ta med ett aktuellt diagram över vilka arbetslaster som delar ett konto i dag och markera var en enda alltför bred roll spänner över produktion och icke-produktion. Om känslig data sitter i samma konto som experimentella arbetslaster är det gränsen att rätta först.

2. **Vilken är er standard för vem som kan hantera nycklar mot vem som kan komma åt den krypterade datan?** Kryptering är bara så stark som nyckelhanteringen, och att skilja nyckelförvaring från dataåtkomst gör er KMS till en efterlevnadspunkt för åtskillnad av ansvarsområden. Besluta vem som får skapa, rotera och använda nycklar, och se till att den mängden inte överlappar de människor som kan läsa datan nycklarna skyddar. För reglerade system och myndighetssystem driver detta ofta valet mellan leverantörshanterade nycklar och kundhanterade nycklar eller HSM, som bär mer kontroll och mer driftrisk att förlora nycklar. Ta med era nuvarande nyckelpolicyer och kontrollera om någon enskild identitet både kan hantera en nyckel och läsa datan bakom den, eftersom det är en vanlig tyst lucka. Om förvaring och åtkomst inte är delade skyddar kryptering i vila er mindre än panelen antyder.

3. **Hur ska ni göra säkra standardvärden ofrånkomliga i er landningszon snarare än bara rekommenderade?** Felkonfiguration, inte exotiska exploateringar, är den ledande orsaken till molnintrång, och åtgärden är förebyggande skyddsräcken som blockerar en publik databas eller en okrypterad hink innan den landar, inte larm i efterhand. Besluta vilka policyer ni ska upprätthålla vid driftsättning (ingen publik lagring, kryptering påslagen som standard, obligatoriska taggar) och vilka ni bara ska upptäcka och rapportera. För ett stort team betyder att koda in dessa i landningszoner och mallar för infrastruktur som kod att varje nytt konto ärver skydd utan insats per team, vilket förvandlar säkerhet från en återkommande skatt till en engångsinvestering. Ta med den senaste månadens fynd av felkonfiguration och fråga vilka ett förebyggande skyddsräcke hade stoppat helt. Om er hantering av säkerhetsläget bara är detekterande kan skada ske innan någon ser larmet, så flytta de mest konsekvensfulla kontrollerna till förebyggande.

4. **Hur eliminerar ni långlivade statiska uppgifter utan att bryta den automation som i tysthet beror på dem?** Inbäddade åtkomstnycklar som aldrig löper ut är bland de vanligaste orsakerna till molnintrång, eftersom en enda läckt nyckel i ett skript, en logg eller ett repositorium ger en angripare varaktig åtkomst. Det motstridiga draget är operativt: äldre CI-jobb, cron-uppgifter och tredjepartsintegrationer antar ofta att en statisk nyckel finns, och att byta över dem till kortlivade tokens eller federation av arbetslastidentitet tar ingenjörstid ingen schemalade. För ett stort team förhindrar en gemensam migreringsväg (utfärda tokens automatiskt, sätt en utgångsstandard och larma på varje ny långlivad nyckel) att varje grupp uppfinner sitt eget svagare svar. Ta med en inventering av varje statisk uppgift i bruk, dess ålder, dess sprängradie och om systemet den matar kan ta emot federerad identitet i dag. I företags- och myndighetssammanhang, knyt deadlinen till revisions- och godkännandecykler, eftersom en uppgift som överlever personen som skapade den är precis det fynd som stoppar en kontinuerlig auktorisering.

5. **När en resurs är felkonfigurerad eller en nyckel komprometterad, hur snabbt kan ni upptäcka, begränsa och åtgärda det, och har ni mätt det?** En publik hink eller en alltför bred roll är bara så farlig som fönstret den förblir öppen, så mediantid att upptäcka och åtgärda är talet som faktiskt begränsar er exponering. Spänningen är mellan förebyggande skyddsräcken som stoppar misstaget vid driftsättning och detekterande hantering av säkerhetsläget som fångar det som slinker igenom, och ni behöver ärliga siffror för båda snarare än ett tröstande antagande att skyddsräcken täcker allt. Ta med det senaste kvartalets fynd av felkonfiguration och drift med tidsstämplar, mediantiden från introduktion till åtgärd och övningsregistret för en nyckelrotation vid komprometterande. För företags- och myndighetsegendomar som spänner över tusentals konton, kom överens om vem som äger åtgärden av ett fynd ingen teams uppenbara ansvar, eftersom ett larm utan ansvarig svarare är ett larm som åldras till en incident.

6. **Hur ska ni hålla säkerhetsläget konsekvent över flera moln, konton och team utan att sakta ned alla till ett krypande?** Miljöer med flera moln och flera konton fragmenteras snabbt: varje leverantör har sin egen IAM-modell, sina egna standardvärden och sina egna verktyg för säkerhetsläge, så en policy som upprätthålls på ett ställe förfaller i tysthet på ett annat. Avvägningen är mellan central kontroll som garanterar konsekvens och lokal autonomi som låter team röra sig snabbt, och att luta för långt åt endera hållet antingen skapar flaskhals i leveransen eller låter standarder driva. Ta med er nuvarande täckningskarta: vilka konton som ärver skyddsräcken från landningszonen, vilka som är ohanterade och var samma kontroll uttrycks på tre olika sätt över leverantörer. För en stor eller offentlig organisation, lägg till revisionsvinkeln, eftersom revisorer förväntar sig en försvarbar standard tillämpad överallt, och en kontroll som finns i ert primära moln men inte i ert sekundära är en lucka som en målmedveten angripare eller bedömare hittar först.

## Sektorsperspektiv

**Startup.** Hastighet och överlevnad vinner, så lita helt på säkra standardvärden som levereras gratis: kryptering i vila påslagen, lagring privat om inte en människa öppnar den, MFA på rotkontot och leverantörens inbyggda arbetslastidentitet i stället för inklistrade åtkomstnycklar. Res inte en CSPM-plattform eller handrulla mikrosegmentering du inte kan underhålla. Ett enda skyddsräcke som blockerar en databas öppnad mot internet köper det mesta av skyddet för en eftermiddags arbete. Håll allt i infrastruktur som kod från start så att härdningen skalar med dig i stället för att bli en senare omskrivning.

**Småföretag.** Utan dedikerad säkerhetsingenjör och med snäv budget, föredra hanterade tjänster vars standardvärden redan är härdade och vars nyckelhantering sköts åt dig, snarare än att bygga din egen KMS-disciplin. Behandla molnsäkerhet som en konfigurationshygienfråga: vet vilka hinkar och databaser som finns, håll dem privata, kräv MFA och slå på leverantörens inbyggda kontroller av säkerhetsläget som kommer utan extra kostnad. När du köper verktyg, föredra sådana som flaggar publik exponering och okrypterad lagring direkt, eftersom dessa två misstag orsakar de flesta undvikbara intrång.

**Storföretag.** Det verkliga problemet är konsekvens över tusentals konton och många team, så arbetet är plattformsarbete: landningszoner som provisionerar varje konto härdat, skyddsräcken upprätthållna som policy som kod och CSPM som skannar kontinuerligt efter drift. Standardisera IAM-modellen, reglerna för nyckelförvaring och segmenteringsbaslinjen så att grupper slutar uppfinna svagare versioner, och mät säkerhetsläget över egendomen snarare än att lita på varje teams ord. Budgetera den löpande tekniken för att hålla policyer aktuella när leverantörer lägger till tjänster och när egendomen växer.

**Offentlig sektor.** Upphandlingsregler, krav på dataplacering och godkännanderegimer formar varje val, så säkerhetskontroller fungerar även som revisionsbelägg. Föredra FIPS-validerad nyckelhantering med förvaring skild från dataåtkomst, isolerade regioner som håller data inom nationella gränser samt signerade, skannade containeravbilder med strikt tillträdeskontroll. Publicera de skyddsåtgärder du kan, mata kontinuerlig hantering av säkerhetsläget direkt in i löpande auktorisering och kräv att leverantörer redovisar sina konfigurationsstandardvärden och stöder de segmenterings- och nyckelförvaringskontroller dina klassificeringsgränser kräver.

## Exempel

**Startup.** En liten startup kör allt i ett molnkonto och kan inte bemanna ett plattformsteam, så den lutar sig mot standardvärden som levereras säkra: kryptering i vila påslagen som standard, lagringshinkar privata om inte en människa uttryckligen öppnar dem och MFA krävt på rotkontot. I stället för långlivade åtkomstnycklar inklistrade i CI använder den leverantörens inbyggda arbetslastidentitet så att pipelinen får kortlivade uppgifter automatiskt. Ett enda gratis skyddsräcke som flaggar varje databas öppnad mot internet räddar dem från det vanligaste och dyraste molnmisstaget, till en kostnad av en eftermiddag att sätta upp.

**Storföretag.** Ett mediebolag som kör tusentals konton över två molnleverantörer upprätthåller ett landningszonsmönster: varje konto provisioneras från en mall med kryptering i vila påslagen som standard, ingen publik åtkomst på lagring, obligatoriska taggar och en baslinje av skyddsräckespolicyer. CSPM skannar kontinuerligt efter drift, och federation av arbetslastidentitet har eliminerat långlivade nycklar för CI-system. När en utvecklare av misstag försöker öppna en databas mot internet blockerar en förebyggande policy ändringen och skapar ett ärende automatiskt.

**Offentlig sektor.** En försvarsnära myndighet verkar i en isolerad molnregion med dataplacering upprätthållen av policy så att ingen data lämnar nationella gränser. De känsligaste nycklarna bor i FIPS-validerade (Federal Information Processing Standards) HSM, med nyckelförvaring skild från dataåtkomst för att upprätthålla åtskillnad av ansvarsområden. Kubernetes-kluster använder strikta nätverkspolicyer och tillträdeskontroller. Varje containeravbild skannas och signeras innan den får köras. Kontinuerlig hantering av säkerhetsläget matar direkt in i myndighetens löpande auktorisationsbelägg.

## Affärsnytta: motiv, ROI och TCO

Infrastruktur- och molnsäkerhet är där en liten investering avvärjer katastrofala förluster på rubriknivå. Den totala ägandekostnaden inkluderar CSPM-verktyg, nyckelhanteringstjänster, ingenjörstiden för att designa IAM med minsta behörighet och segmentering och den löpande insatsen för att hålla policyer aktuella. Dessa kostnader är verkliga men måttliga. Kostnaden för att hoppa över dem är en enda felkonfigurerad resurs som exponerar en hel kunddatabas, tillsammans med de regulatoriska viten, underrättelsekostnader och varaktiga anseendeskador som följer. Intrång genom molnfelkonfiguration är bland de vanligaste och mest förebyggbara incidenterna i branschen.

Automation och återanvändning förstärker ROI. Koda in säkra standardvärden i landningszoner och mallar för infrastruktur som kod, så ärver varje nytt konto och varje arbetslast skydd utan insats per team, vilket förvandlar säkerhet från en återkommande manuell skatt till en engångsinvestering i plattformen. För myndigheter och reglerade företag sänker stark hantering av säkerhetsläget också kostnaden för revisioner och kontinuerlig auktorisering genom att producera belägg automatiskt. När du driver ärendet inför ledningen, betona att identitets- och konfigurationslagret nu är den primära intrångsvektorn, att felkonfiguration är förebyggbar och att skyddsräcken skär ned både risken och friktionen i manuell granskning.

## Antimönster och fallgropar

- **Jokerbehörigheter.** Att ge breda `*`-åtkomster "för att få saker att fungera" och aldrig skärpa dem.
- **Långlivade statiska nycklar.** Åtkomstnycklar inbäddade i skript och CI som aldrig löper ut och så småningom läcker.
- **Platta nätverk.** Ingen segmentering, så att en komprometterad värd når allt.
- **Publikt av misstag.** Lagring och databaser exponerade mot internet genom standardinställningar eller slarviga inställningar.
- **Kryptering utan nyckeldisciplin.** Att slå på kryptering men lämna nyckelåtkomsten vidöppen eller aldrig rotera.
- **Hemligheter inbakade i avbilder.** Uppgifter inbäddade i containeravbilder som sprids överallt avbilden körs.
- **Överbehöriga serverlösa roller.** Funktioner som får långt mer än de behöver eftersom avgränsningen hoppades över.
- **Hantering av säkerhetsläge bara för granskning.** Att upptäcka felkonfigurationer i efterhand i stället för att förhindra dem vid driftsättning.
- **Att ignorera drift.** Att låta den körande miljön avvika från infrastruktur som kod tills ingen vet det verkliga tillståndet.

## Mognadsmodell

**Nivå 1: Initiera.** Manuell provisionering driven av den som behöver en resurs. Breda jokerbehörigheter och långlivade statiska nycklar. Platta nätverk utan segmentering. Kryptering tillämpad inkonsekvent, om alls. Ingen hantering av säkerhetsläge. Felkonfigurationer visar sig först efter att en incident tvingar fram frågan.

**Nivå 2: Utveckla.** Vissa IAM-roller och MFA dyker upp, och kryptering i vila är påslagen för de stora lagren, men praxis varierar team för team. Grundläggande nätverksnivåer finns utan neka-som-standard. Konfigurationsgranskningar sker periodiskt och för hand. Infrastruktur är delvis definierad som kod, så härdningen beror på vilken grupp som provisionerade kontot.

**Nivå 3: Standardisera.** RBAC och ABAC med minsta behörighet och kortlivade uppgifter är dokumenterade och upprätthållna i hela organisationen. Segmenteringen använder neka-som-standard för öst-väst. Kryptering under överföring och i vila är påslagen som standard, med nycklar i KMS på ett rotationsschema och förvaring skild från dataåtkomst. Härdning av containrar och Kubernetes är en standard, och CSPM körs mot definierade policyer tillämpade konsekvent över varje konto.

**Nivå 4: Hantera.** Säkerhetsläget mäts, antas inte. Du följer namngivna mått mot utgångslägen och mål: andelen identiteter inom sin baslinje för minsta behörighet, mediantid att upptäcka och åtgärda felkonfigurationer och drift, täckning av skyddsräcken och CSPM över konton, efterlevnad av nyckelrotation och antalet kvarvarande långlivade uppgifter. Fynd triageras efter sprängradie, åtgärd har en ägare och ett servicenivåmål, och trenddata för dessa tal driver var nästa härdningsinsats går.

**Nivå 5: Orkestrera.** Säkra standardvärden är inbakade i landningszoner och infrastruktur som kod så att varje resurs föds härdad, och kontrollerna anpassas när egendomen och hotbilden skiftar. Mikrosegmentering använder identitetsmedveten policy. Kundhanterade nycklar och HSM skyddar systemen med högst säkring med åtskild förvaring. Förebyggande skyddsräcken blockerar felkonfiguration vid driftsättning, drift upptäcks och åtgärdas automatiskt och belägg för säkerhetsläget matar kontinuerlig auktorisering automatiskt. Säkerhet är integrerad med leverans och riskplanering, och organisationen avvecklar och omdefinierar rutinmässigt kontroller när leverantörer, tjänster och regleringar förändras.

## Idéer för diskussion

1. Var är ABAC värt sin komplexitet mot att hålla sig till RBAC i er miljö?
2. Hur eliminerar ni långlivade uppgifter utan att bryta äldre automation?
3. Vilken är den rätta fördelningen mellan förebyggande skyddsräcken och detekterande hantering av säkerhetsläge?
4. Vilka system motiverar kundhanterade nycklar eller HSM med tanke på deras driftkostnad?
5. Hur hindrar ni behörigheter med minsta behörighet från att i tysthet ackumuleras tillbaka till överbehörighet?
6. Hur bör komplexitet med flera moln ändra ert tillvägagångssätt för konsekvent säkerhetsläge och policy?

## Viktigaste punkter

- Identitet är den nya perimetern. Investera i IAM med minsta behörighet och kortlivade uppgifter.
- Segmentera nätverk och mikrosegmentera arbetslaster för att begränsa komprometterande.
- Kryptera under överföring och i vila som standard och hantera nycklar med KMS/HSM och åtskild förvaring.
- Härda containrar, Kubernetes och serverlöst. Håll körmiljöer och avbilder patchade.
- Föredra förebyggande skyddsräcken framför detektering i efterhand och hantera säkerhetsläget kontinuerligt.
- Baka in säkra standardvärden i landningszoner och infrastruktur som kod så att skyddet skalar automatiskt.
- Felkonfiguration, inte exotiska exploateringar, är den ledande orsaken till molnintrång, och den är förebyggbar.

## Referenser och vidare läsning

- National Institute of Standards and Technology, *SP 800-207: Zero Trust Architecture*
- Centre for Internet Security, *CIS Benchmarks* (cloud providers, Kubernetes, Docker)
- Cloud Security Alliance, *Cloud Controls Matrix* and *Security Guidance for Cloud Computing*
- NIST, *SP 800-190: Application Container Security Guide*
- Liz Rice, *Container Security*
- Marco Lancini and others, *Cloud security posture and detection* engineering literature
- Provider Well-Architected security pillars (as vendor-neutral architectural guidance)
