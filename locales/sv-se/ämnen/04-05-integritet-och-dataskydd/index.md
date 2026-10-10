# 4.5 Integritet och dataskydd

## Översikt och motivation

Säkerhet skyddar data från obehörig åtkomst. Integritet ställer en annan fråga: bör du överhuvudtaget samla in, använda och behålla den datan, och får de människor den beskriver säga sitt? De två överlappar, men de är inte detsamma. Du kan vara fullkomligt säker och ändå kränka integriteten. Du gör det genom att hamstra data du inte har någon rätt att hålla, använda den för ändamål människor aldrig samtyckt till eller flytta den över gränser på sätt lagen förbjuder. För stora team är integritet en designbegränsning. Den berör varje tjänst som hanterar personuppgifter, vilket i dag betyder nästan alla.

Insatserna är höga och stigande. Integritetsreglering har spridit sig världen över. Den bär viten som skalar med intäkter och ger individer verkställbara rättigheter över sin data. För företag inbjuder felhantering av personuppgifter till regulatoriska åtgärder, grupptalan och förlust av kundförtroende som är dyrt att bygga upp igen. För myndigheter är plikten tyngre än så. Medborgare kan inte välja en annan leverantör av sina skatte-, hälso- eller bidragsdata, så staten har en särskild omsorgsplikt mot dem. Och integritetsfel urholkar det offentliga förtroende myndigheter är beroende av.

Det här kapitlet behandlar integritet som en ingenjörsdisciplin. Vi behandlar att designa för integritet från start, minimera och lagra data ansvarsfullt, klassificera och skydda känsliga kategorier som [PII](https://en.wikipedia.org/wiki/Personally_identifiable_information) (personuppgifter) och [PHI](https://en.wikipedia.org/wiki/Protected_health_information) (skyddad hälsoinformation), hantera samtycke och rättslig grund samt hantera de krav på överföring över gränser och dataplacering som alltmer formar arkitekturen.

*Se även:* kapitel 4.6 (regelefterlevnad och styrning), kapitel 7.1 (datastrategi och styrning) och kapitel 4.1 (säkerhetens grunder och kultur).

## Nyckelprinciper

- **[Inbyggd integritet](https://en.wikipedia.org/wiki/Privacy_by_design) (privacy by design) och som standard.** Bygg in integritet från början och gör den mest integritetsskyddande inställningen till standard.
- **[Dataminimering](https://en.wikipedia.org/wiki/Data_minimization).** Samla in bara det du verkligen behöver, behåll det bara så länge du behöver det och dela det bara som nödvändigt.
- **Ändamålsbegränsning.** Använd data bara för de specifika ändamål som angavs när den samlades in.
- **Rättslig grund.** Ha en giltig rättslig motivering för varje behandling.
- **Individens rättigheter.** Hedra människors rätt att komma åt, rätta, radera och flytta sin data.
- **Transparens.** Tala om för människor i klartext vad du samlar in, varför och med vem du delar det.
- **Ansvarsskyldighet.** Kunna visa efterlevnad, inte bara påstå den.

## Rekommendationer

### Designa för integritet från start

Integritet påskruvad på ett färdigt system är dyr och ofullständig. Baka in den från början.

- Genomför **[konsekvensbedömningar avseende dataskydd](https://en.wikipedia.org/wiki/Data_protection_impact_assessment) (DPIA)** för nya system och funktioner som behandlar personuppgifter i stor skala eller bär högre risk, och identifiera och mildra integritetsrisker innan du bygger.
- Gör standardvärden integritetsskyddande: opt-in snarare än opt-out för icke-väsentlig behandling, minimala datafält och kortast rimliga lagring.
- Involvera integritetsexpertis tidigt i designen, vid sidan av hotmodellering för säkerhet, så att båda beaktas vid förtroendegränsstadiet.
- Underhåll en **datakarta eller inventering**: vilka personuppgifter du håller, var de bor, varför och vart de flödar. Du kan inte skydda eller redovisa data du inte kan se.

### Minimera, lagra och radera ansvarsfullt

Varje bit personuppgift du håller är lika mycket en skuld som en tillgång.

- **Minimera insamling:** utmana varje fält. Om du inte behöver det för ett angivet ändamål, samla inte in det.
- **Sätt lagringsscheman** per datatyp och ändamål och upprätthåll dem med automatisk radering. Data som behålls "för säkerhets skull" är data som väntar på att bli intrångsdrabbad eller stämd.
- **Stöd rätten till radering:** bygg förmågan att hitta och radera en individs data över alla system, inklusive säkerhetskopior och kopior nedströms, inom rättsliga frister. Detta är långt lättare när det designas in än när det skruvas på.
- **[Anonymisera](https://en.wikipedia.org/wiki/Data_anonymization) eller aggregera** data för analys och testning så att identifierbar data inte sprids in i sekundära miljöer.

### Klassificera och skydda känslig data

Inte alla personuppgifter bär samma risk, och vissa kategorier bär särskild rättslig vikt.

- Klassificera data i nivåer och skilj **PII** (personuppgifter), **PHI** (skyddad hälsoinformation), finansiell data och särskilda kategorier (som ras, religion, hälsa, biometri eller sexualitet) som bär förhöjt rättsligt skydd.
- Tillämpa skydd proportionellt mot känsligheten: starkare åtkomstkontroller, kryptering och övervakning för de mest känsliga nivåerna.
- Använd **[tokenisering](https://en.wikipedia.org/wiki/Tokenization_(data_security))** för att ersätta känsliga värden (som kortnummer eller nationella identifierare) med icke-känsliga tokens, vilket krymper de system som någonsin rör rådatan och därmed krymper efterlevnadsomfattningen.
- Använd **[pseudonymisering](https://en.wikipedia.org/wiki/Pseudonymization)** för att skilja identifierare från resten av en post så att data är mindre direkt hänförlig, vilket minskar risken samtidigt som nyttan behålls.
- Maskera känslig data i loggar, felmeddelanden, analys och icke-produktionsmiljöer.

### Hantera samtycke och rättslig grund korrekt

Behandling av personuppgifter kräver en giltig rättslig grund, och samtycke är bara en av flera.

- Identifiera och dokumentera den **rättsliga grunden** för varje behandling: samtycke, avtal, rättslig förpliktelse, grundläggande intressen, uppgift av allmänt intresse eller berättigade intressen, beroende på tillämplig regim.
- Där samtycke är grunden, gör det **frivilligt, specifikt, informerat och otvetydigt**, med ett lika enkelt sätt att dra tillbaka det. Förbockade rutor och buntat samtycke är inte giltiga.
- Registrera samtycke: vad personen gick med på, när och på vilka villkor, så att du kan visa det.
- Respektera **ändamålsbegränsning**: använd inte data för något oförenligt med varför den samlades in utan en ny grund.
- Hedra signaler som [Do Not Track](https://en.wikipedia.org/wiki/Do_Not_Track) / [Global Privacy Control](https://en.wikipedia.org/wiki/Global_Privacy_Control) och begäranden om avanmälan där lagar kräver det.

### Hantera överföring över gränser och dataplacering

Var data fysiskt bor och rör sig är nu en förstklassig arkitekturfråga.

- Förstå krav på **dataplacering**: vissa jurisdiktioner kräver att viss data stannar inom nationella gränser, och viss myndighetsdata måste stanna i specifika suveräna eller ackrediterade miljöer.
- För **överföringar över gränser**, säkerställ att en giltig rättslig mekanism (beslut om adekvat skyddsnivå, standardavtalsklausuler eller motsvarande) finns på plats och är dokumenterad.
- Arkitektera för dataplacering från start: regionfäst lagring, datalokalisering och noggrann kontroll av vart säkerhetskopior, loggar och analysdata flödar, eftersom dessa ofta läcker data över gränser obemärkt.
- Följ underbiträden och tredje parter. En leverantör som flyttar data utomlands kan bryta mot skyldigheter om dataplacering å dina vägnar.

## Avvägningar: för- och nackdelar

| Beslut | Fördelar | Nackdelar |
|---|---|---|
| Aggressiv dataminimering | Mindre risk, mindre intrångskonsekvens, enklare regelefterlevnad | Kan begränsa analys och framtida produktval |
| Lång lagring | Rik historik för analys, ML, tvister | Större skuld, intrångsexponering, raderingskomplexitet |
| Tokenisering | Krymper efterlevnadsomfattning, skyddar rådata | Tillagd systemkomplexitet, tokenvalv att säkra |
| Opt-in-standardvärden | Starkare förtroende, tydlig regelefterlevnad | Lägre datavolymer, svårare tillväxtmått |
| Regional dataplacering | Möter rättsliga krav, bygger suveränitetsförtroende | Arkitektonisk komplexitet, högre kostnad, duplicerad infrastruktur |
| Centraliserad datasjö | Analyskraft, en enda källa | Koncentrerad risk, svårare ändamålsbegränsning |

Den centrala spänningen är mellan verksamhetens aptit på data och den skuld datan representerar. Produkt- och analysteam vill naturligt samla in mer och behålla det längre. Integritetsdisciplin drar åt andra hållet. Den mogna lösningen omformulerar data som en skuld att motivera, inte en tillgång att hamstra. Varje beslut om insamling och lagring måste förtjäna sin plats mot den risk det skapar. Dataplacering lägger till en dimension av kostnad mot regelefterlevnad. Att möta suveränitetskrav kan multiplicera infrastruktur, men det är helt enkelt icke förhandlingsbart på vissa marknader och i myndighetssammanhang.

## Frågor att diskutera med ditt team

1. **Vilket är ert lagringsschema för varje klass av personuppgifter, och vad upprätthåller radering?** Data som behålls "för säkerhets skull" är data som väntar på att bli intrångsdrabbad eller stämd, så varje fält och varje post behöver en definierad livslängd knuten till sitt ändamål. Besluta schemat per datatyp och upprätthåll det sedan med automatisk radering snarare än att lita på att någon minns. För företag krymper detta intrångsexponering och lagringskostnad på en gång, och för myndigheter stämmer det med lagstadgade skyldigheter att hålla medborgardata inte längre än lagen tillåter. Ta med ett urval av era äldsta lagrade poster och fråga vem som fortfarande behöver dem och på vilken grund, eftersom det ärliga svaret ofta är ingen. Om radering är manuell eller obefintlig ackumuleras data för evigt och er skuld växer tyst på balansräkningen.

2. **Vilka känsliga fält kan ni tokenisera eller pseudonymisera för att krympa både risk och efterlevnadsomfattning?** Att ersätta kortnummer eller nationella identifierare med tokens begränsar rådatavärdena till ett litet, tätt kontrollerat valv, vilket kraftigt skär ned de system som omfattas av revisioner som PCI-DSS. Pseudonymisering skiljer identifierare från resten av en post och sänker risken samtidigt som datan förblir användbar för analys och testning. Besluta vilka högkänsliga värden som motiverar ett tokenvalv (tillagd komplexitet, ett valv att säkra) och vilka som bara behöver maskeras i loggar och icke-produktion. Ta med en karta över var råa känsliga värden flödar i dag, eftersom varje system som rör dem är ett system ni måste skydda och granska. För reglerad data och myndighetsdata är denna omfattningsminskning ett av få drag som sänker både kostnad och risk, så rikta in er på era känsligaste fält först.

3. **Innan er nästa funktion levereras, vad utlöser en konsekvensbedömning avseende dataskydd och vem kör den?** Integritet påskruvad på ett färdigt system är dyr och ofullständig, så en DPIA måste köras tidigt, vid sidan av hotmodellering för säkerhet, när ni fortfarande kan ändra designen billigt. Besluta utlösaren (ny behandling i stor skala, data i särskilda kategorier, ett nytt ändamål) och namnge vem som äger bedömningen så att den inte faller mellan stolarna under leveranstryck. En verklig DPIA kan fånga överinsamling före lansering, till exempel genom att byta exakt plats mot grov regiondata utan produktförlust. Ta med en kommande funktion och gå igenom den: vilka personuppgifter den samlar in, varför och om en mindre ingripande design uppnår samma mål. För myndighetstjänster medborgare inte kan välja bort är denna tidiga kontroll en del av omsorgsplikten, så gör den till en grind, inte en eftertanke.

4. **När personuppgifter korsar en gräns, inklusive genom säkerhetskopior, loggar och underbiträden, vilken rättslig mekanism täcker varje gränsövergång, och kan ni bevisa det?** Regler om dataplacering och överföring formar nu arkitekturen lika mycket som vilket prestandakrav som helst, och de gränsövergångar som fångar team är sällan de uppenbara: en logg skickad till ett utländskt observerbarhetsverktyg, en säkerhetskopia replikerad till en billigare region eller ett underbiträde som i tysthet flyttar data utomlands. För en stor organisation är de konkurrerande trycken verkliga, eftersom regionfäst infrastruktur kostar mer och duplicerar drift, men en enda olaglig överföring kan ogiltigförklara ett marknadsinträde eller utlösa ett verkställighetsföreläggande. Ta med en aktuell dataflödeskarta som namnger varje plats där personuppgifter fysiskt vilar eller färdas, den rättsliga mekanismen för varje gräns de korsar (beslut om adekvat skyddsnivå, standardavtalsklausuler eller motsvarande) och listan över underbiträden med deras platser. I myndighets- och suveränitetsdatasammanhang, behandla dataplacering som en hård arkitekturbegränsning snarare än en avtalsklausul, eftersom vissa register aldrig får lämna ackrediterade nationella miljöer, och det ansvariga organet kan inte delegera den plikten till en leverantör.

5. **Vilken rättslig grund backar upp varje behandling, och kunde ni försvara det valet inför en tillsynsmyndighet i morgon?** Samtycke är bara en av flera rättsliga grunder, och team väljer ofta det som standard när avtal, rättslig förpliktelse, uppgift av allmänt intresse eller berättigade intressen skulle vara både ärligare och mer varaktiga. Detta spelar roll i skala eftersom en svag eller felaktigt vald grund kan ogiltigförklara en hel pipeline, och att reda ut behandling ni inte hade rätt att utföra är långt dyrare än att välja rätt grund i förväg. Väg de konkurrerande hänsynen öppet: samtycke ger individer kontroll men kan dras tillbaka och måste vara frivilligt, specifikt och obuntat, medan en grund som berättigade intressen undviker samtyckeströtthet men kräver ett dokumenterat avvägningstest. Ta med ett register som mappar varje behandling till dess påstådda grund, beläggen som stöder den och hur ni skulle dra tillbaka eller byta om ni utmanades. I myndigheter vilar den mesta kärnbehandlingen på uppgift av allmänt intresse snarare än samtycke, så var exakta med var valfritt, återkallbart samtycke börjar, eftersom att sudda ut de två urholkar det förtroende medborgare inte har något val än att ge.

6. **Om en person utövade sin rätt till tillgång, radering eller portabilitet i dag, kunde ni uppfylla det över varje system inom den rättsliga fristen?** Individens rättigheter är lätta att lova i en integritetspolicy och svåra att hedra i en arkitektur som spridit kopior av personuppgifter in i säkerhetskopior, cacher, analyslager och nedströmstjänster. För ett stort team är detta ögonblicket då abstrakt regelefterlevnad blir ett konkret ingenjörstest, och en missad lagstadgad frist är både ett rapporteringspliktigt fel och en signal om att ni inte faktiskt kan se er egen data. Den konkurrerande hänsynen är kostnad och komplexitet, eftersom att bygga genuin radering och export över system är verkligt arbete, men alternativet är manuell, långsam, felbenägen uppfyllelse som inte skalar och i tysthet bryter mot lagen. Ta med en ärlig genomgång av en verklig begäran från mottagning till slutförande, inklusive hur säkerhetskopior och tredje parter nås, och ta tid på den mot den rättsliga fristen. För myndighetstjänster människor inte kan lämna, behandla självbetjäning, fullständig och granskningsbar uppfyllelse av rättigheter som en del av omsorgsplikten, inte en funktion att schemalägga för senare.

## Sektorsperspektiv

**Startup.** Med ett pyttelitet team och liten löptid, behandla integritet som billig försäkring snarare än ett program du inte kan bemanna. Samla in bara de fält din kärnfunktion behöver, håll ett lätt kalkylbladsbaserat datakarta så att du faktiskt kan besvara en raderingsbegäran och håll e-postadresser och tokens utanför dina loggar. Ett tydligt samtyckesflöde och verklig radering kostar en eftermiddag nu. Att eftermontera dem efter att din första företagskund eller tillsynsmyndighet frågar kostar långt mer, och överinsamlad data är en skuld du inte vinner något på att hålla.

**Småföretag.** Utan dedikerad integritetsspecialist och med snäv budget, lita på de integritetskontroller som redan är inbyggda i de verktyg du köper och föredra leverantörer som gör datahantering transparent och dataplacering tydlig. Ramma in beslutet som köp mot bygg: du bygger nästan aldrig tokenisering eller uppfyllelse av rättigheter själv, så välj plattformar som erbjuder lagringsregler, export och radering direkt. Vet vilka personuppgifter du håller och var en felaktig eller förlorad post skulle kosta dig en kund, och skriv ned en rättslig grund för varje användning även om dokumentet är kort.

**Storföretag.** I skala är problemet konsekvens över många team: en gemensam datakarta, standardiserade klassificeringsnivåer och upprätthållen lagring så att ingen enskild grupp blir den svaga länken. Budgetera tekniken för radering över system, tokenvalv och dataplaceringsmedveten arkitektur uttryckligen och styr underbiträden centralt så att en leverantör inte kan bryta mot en överföringsskyldighet å dina vägnar. Gör DPIA till en grind i leveransprocessen och mät integritetsläget, eftersom revisorer och tillsynsmyndigheter kommer att be dig visa efterlevnad, inte bara påstå den.

**Offentlig sektor.** Upphandlingsregler, transparensplikter och offentlig ansvarsskyldighet formar varje val, och medborgare kan inte ta sina skatte-, hälso- eller bidragsdata någon annanstans, så omsorgsplikten är förhöjd. Förankra känsliga register i ackrediterade nationella miljöer inklusive säkerhetskopior och analys, bind varje leverantör avtalsenligt till samma skyldigheter om dataplacering och radering och dokumentera en rättslig grund (ofta uppgift av allmänt intresse) för kärnbehandling medan valfria användningar hålls åtskilda under återkallbart samtycke. Publicera beskrivningar i klarspråk av vad du samlar in och varför, och gör uppfyllelse av rättigheter pålitlig inom lagstadgade tidsfrister, eftersom ett integritetsfel här urholkar det offentliga förtroende tjänsten är beroende av.

## Exempel

**Startup.** En tidig konsumentapp samlar bara in de data den verkligen behöver, eftersom varje extra fält är en skuld den hellre inte försvarar senare. Den håller ett enkelt kalkylblad som datakarta över var personuppgifter bor så att den faktiskt kan besvara en raderingsbegäran, håller e-postadresser och tokens utanför sina loggar och sätter en grundläggande lagringsregel för att rensa data från sedan länge döda konton. Att bygga ett tydligt samtyckesflöde och verklig radering nu kostar en eftermiddag. Att eftermontera dem efter att den första företagskunden eller tillsynsmyndigheten frågar kostar långt mer.

**Storföretag.** En global konsumentapp genomför en DPIA innan den lanserar en ny rekommendationsfunktion och upptäcker att den skulle samla in exakt plats i onödan. Teamet byter till grov regiondata och minskar risken utan produktförlust. Kortnummer tokeniseras så att bara ett litet, tätt kontrollerat valv någonsin håller rådatavärden, vilket skär ned företagets [PCI](https://en.wikipedia.org/wiki/Payment_Card_Industry_Data_Security_Standard)-omfattning (betalkortsbranschen) dramatiskt. Automatiska lagringsregler rensar data från inaktiva konton enligt schema, och ett självbetjäningsflöde låter användare exportera och radera sin data inom den rättsliga fristen över alla system inklusive säkerhetskopior.

**Offentlig sektor.** En nationell hälso- och sjukvårdstjänst klassificerar alla patientjournaler som PHI och data i särskilda kategorier och upprätthåller strikta åtkomstkontroller, kryptering och revisionsloggning. Policy för dataplacering håller alla register inom nationella gränser, inklusive säkerhetskopior och analys, och varje leverantör är avtalsenligt bunden till detsamma. Medborgare har en dokumenterad rättslig grund (uppgift av allmänt intresse) för kärnbehandling, medan valfria forskningsanvändningar kräver separat, återkallbart samtycke som registreras och hedras. En datakarta underbygger förmågan att besvara begäranden om tillgång och radering inom lagstadgade tidsfrister.

## Affärsnytta: motiv, ROI och TCO

Integritetsinvesteringar ramas ofta in som ren regelefterlevnadskostnad, men det underskattar dem. Den totala ägandekostnaden inkluderar DPIA-processer, verktyg för datakartläggning och inventering, tokeniserings- och lagringsinfrastruktur samt tekniken för att stödja individens rättigheter och dataplacering. Väg det mot kostnaden för att inte investera, som är svår och alltmer sannolik. Integritetsviten når nu procent av global omsättning, grupptalan följer efter större intrång och tillsynsmyndigheter har visat att de kommer att agera. Utöver viten förstör felhanterad integritet det kundförtroende som bär intäkterna. Och att åtgärda ett integritetsfel i efterhand (eftermontera radering, reda ut olagliga dataflöden) kostar långt mer än att bygga in det.

ROI har också en verklig uppsida. Stark integritet är en konkurrensfördel, och på reglerade marknader och myndighetsmarknader är den en förutsättning för att alls vinna affärer. Dataminimering minskar direkt intrångsexponering och lagringskostnad, och tokenisering krymper den dyra omfattningen av revisioner som PCI-DSS. När du driver ärendet inför ledningen, presentera integritet på två sätt: som riskjusterad skuldhantering med verklig regulatorisk exponering och som en förtroendetillgång som öppnar marknader. Betona att inbyggd integritet är billig jämfört med integritet genom rättstvist, och att data hamstrad utan ändamål är en skuld som sitter på balansräkningen och väntar på att realiseras.

## Antimönster och fallgropar

- **Samla in allt, besluta senare.** Att hamstra data utan ändamål, maximera skuld utan nytta.
- **Lagring genom försummelse.** Att aldrig radera något eftersom inget schema finns, så att data ackumuleras för evigt.
- **Samtyckesteater.** Förbockade rutor, buntat samtycke eller mörka mönster som är rättsligt ogiltiga och urholkar förtroendet.
- **Radering som missar säkerhetskopior.** Att radera från primärlagret men lämna kopior i säkerhetskopior, loggar och analys.
- **Personuppgifter i loggar och testdata.** Att sprida känslig data in i miljöer med lite kontroll där den lätt exponeras.
- **Att ignorera dataflöden.** Att förbise att loggar, säkerhetskopior, analys och underbiträden flyttar data över gränser.
- **Integritet som enbart en juridisk fråga.** Att behandla den som pappersarbete snarare än en ingenjörsmässig designbegränsning.
- **Ingen datakarta.** Att inte kunna svara på var personuppgifter bor, vilket gör begäranden om rättigheter och intrångssvar omöjliga.

## Mognadsmodell

**Nivå 1: Initiera.** Integritet hanteras reaktivt, om alls. Personuppgifter samlas in fritt utan inventering, minimering eller lagringsgränser. Samtycke är en eftertanke, det finns ingen process för begäranden om tillgång eller radering och var data fysiskt bor är obeaktat.

**Nivå 2: Utveckla.** Grundläggande praxis dyker upp men varierar per team. En integritetspolicy finns och grundläggande samtycke fångas, med viss medvetenhet om lagring. Begäranden om rättigheter hanteras manuellt och långsamt, dataklassificering är informell och ett team kan kartlägga sin data medan ett annat samlar in fritt. Inget upprätthålls konsekvent över organisationen.

**Nivå 3: Standardisera.** Inbyggd integritet är dokumenterad och upprätthållen i hela organisationen. DPIA körs för projekt med högre risk, data är kartlagd och klassificerad i nivåer och lagringsscheman upprätthålls med automatisk radering. En rättslig grund är dokumenterad för varje behandling, giltiga samtyckesmekanismer finns på plats, begäranden om rättigheter uppfylls inom frister och dataplacering hanteras för reglerad data.

**Nivå 4: Hantera.** Integritetsprogrammet mäts och styrs mot utgångslägen. Du följer tid för uppfyllelse av rättighetsbegäranden mot lagstadgade frister, täckning av lagringspolicy och åldern på de äldsta posterna, antalet personuppgiftsfält i omfattning och hur många som är tokeniserade eller pseudonymiserade, andelen genomförda DPIA för kvalificerande funktioner och antalet ohanterade flöden över gränser som hittats vid revisioner. Mått matar definierade trösklar, så att ett brott mot ett mål (en rättighetsbegäran som närmar sig sin frist, en oväntad överföring, lagringsdrift) utlöser ett dokumenterat svar i stället för att gå obemärkt förbi.

**Nivå 5: Orkestrera.** Integritet är en standardmässig ingenjörsbegränsning som förbättras kontinuerligt och är integrerad i hela organisationen. Minimering, tokenisering och automatisk lagring är standard, begäranden om rättigheter är självbetjäning och fullständiga över alla system inklusive säkerhetskopior, och dataflöden och dataplacering spåras och upprätthålls kontinuerligt. Integritetsläget anpassas när reglering, marknader och arkitektur skiftar och matar lärdomar tillbaka in i designen så att baslinjen fortsätter stiga snarare än bara hålla.

## Idéer för diskussion

1. Hur löser ni spänningen mellan analysteam som vill ha mer data och integritet som vill ha mindre?
2. Vilken är en realistisk arkitektur för att hedra radering över primärlager, säkerhetskopior och kopior nedströms?
3. Vilken rättslig grund passar var och en av era behandlingar, och kan ni försvara valet?
4. Hur håller ni personuppgifter utanför loggar och icke-produktionsmiljöer utan att hindra felsökning?
5. Vilka krav på dataplacering gäller för era marknader, och hur komplicerar säkerhetskopior och analys dem?
6. Hur bör hotmodellering för integritet och säkerhet kombineras till en enda designaktivitet?

## Viktigaste punkter

- Integritet styr om och hur du använder personuppgifter. Den är skild från och kompletterar säkerhet.
- Designa in integritet från start med DPIA och integritetsskyddande standardvärden.
- Minimera insamling, upprätthåll lagringsscheman och bygg genuin raderingsförmåga.
- Klassificera PII, PHI och särskilda kategorier och skydda dem proportionellt med tokenisering och maskering.
- Etablera och dokumentera en rättslig grund. Gör samtycke frivilligt, specifikt och återkallbart.
- Behandla dataplacering och överföring över gränser som förstklassiga arkitekturbegränsningar.
- Data är en skuld såväl som en tillgång. Att hamstra den utan ändamål är risk som väntar på att realiseras.

## Referenser och vidare läsning

- Ann Cavoukian, *Privacy by Design: The 7 Foundational Principles*
- European Union, *General Data Protection Regulation (GDPR)* text and guidance
- National Institute of Standards and Technology, *Privacy Framework* and *SP 800-122* (Guide to Protecting PII)
- ISO/IEC 27701, *Privacy Information Management*
- Daniel Solove, *Understanding Privacy*
- OECD, *Privacy Guidelines* and *Fair Information Practice Principles (FIPPs)*
- California Consumer Privacy Act (CCPA/CPRA) statutory text and regulator guidance
