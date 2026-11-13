# 3.2 Arkitekturstilar och mönster

## Översikt och motivation

En arkitekturstil är en bred, återanvändbar form för att organisera ett system: hur det delas upp, hur delarna kommunicerar och var gränserna går. Att välja en är ett av de mest avgörande (och mest missförstådda) beslut en stor organisation fattar. Alltför ofta följer valet modet ("alla kör [mikrotjänster](https://en.wikipedia.org/wiki/Microservices)") i stället för teamets, domänens och driftens verkliga begränsningar. Du slutar med en av två röror: ett distribuerat system organisationen inte kan driva, eller en trasslig [monolit](https://en.wikipedia.org/wiki/Monolithic_application) ingen kan ändra säkert. Ingen av dem är stilens fel. Båda kommer av att stilen anpassades fel till situationen.

För stora utvecklingsteam spelar stilar roll framför allt på grund av [Conways lag](https://en.wikipedia.org/wiki/Conway%27s_law): ett systems struktur tenderar att spegla kommunikationsstrukturen hos den organisation som bygger det. En arkitekturstil är därför också ett organisationsdesignbeslut. Att dela ett system i tjänster är egentligen ett beslut om att dela team, ägarskap och jouransvar. Företag med hundratals ingenjörer kan ha råd med (och behöver ofta) finkorniga tjänster med oberoende driftsättning, eftersom det oberoendet är hur många team levererar utan att blockera varandra. Tvinga samma mönster på ett enda litet team och det ärver all driftskatt utan någon av de organisatoriska fördelarna.

Myndighets- och företagsmiljöer lägger på fler begränsningar: långa systemlivslängder, strikt ändringskontroll, upphandlingscykler, integration med förankrade register-system och granskningsbarhet. De gynnar stilar som håller gränser uttryckliga och beroenden lätta att inspektera. Det här kapitlet överblickar de stora stilarna: monolit genom mikrotjänster, [händelsedrivna arkitekturer](https://en.wikipedia.org/wiki/Event-driven_architecture) med [CQRS](https://en.wikipedia.org/wiki/Command_Query_Responsibility_Segregation) och händelselagring, [tjänstenät](https://en.wikipedia.org/wiki/Service_mesh) och gatewaymönster, [serverlös](https://en.wikipedia.org/wiki/Serverless_computing) och de inre disciplinerna hos [hexagonal](https://en.wikipedia.org/wiki/Hexagonal_architecture_(software)) och ren arkitektur. Än viktigare är att det hjälper dig avgöra när var och en passar.

*Se även:* kapitel 2.2 (principer för programvarudesign, inklusive [domändriven design](https://en.wikipedia.org/wiki/Domain-driven_design)), kapitel 3.1 (arkitekturens grunder) och kapitel 3.3 (distribuerade system).

## Nyckelprinciper

- **Stil följer krafter, inte mode.** Välj utifrån teamstorlek, domänkomplexitet, belastning och driftmognad, aldrig därför att en teknik är populär.
- **Koppling är den verkliga fienden, inte antalet driftsättningsbara enheter.** En väl modulariserad monolit slår en distribuerad stor lerklump.
- **Distribution är en kostnad du betalar för oberoende.** Dela bara när värdet av oberoende driftsättning, skalning eller felisolering överstiger kostnaden för nätverksanrop, partiellt fel och datakonsistens över tjänster.
- **Gränser bör följa affärsdomänen.** Justera tjänster och moduler efter avgränsade kontexter (var och en en självständig domänmodell med sin egen uttryckliga gräns), inte efter tekniska lager.
- **Designa insidan väl oavsett utsidan.** Hexagonal/ren skiktning håller affärslogiken oberoende av ramverk och infrastruktur i varje stil.
- **Conways lag är oundviklig, så använd den.** Designa teamgränser och arkitektur tillsammans.
- **Börja enklare än du tror att du behöver.** Du kan extrahera tjänster ur en bra modulär monolit. Att avdistribuera en förhastad mikrotjänströrig är långt svårare.

## Rekommendationer

### Välj en modulär monolit som standard, dela med belägg

Börja de flesta system som en enda driftsättningsbar enhet med starka interna modulgränser: tydliga gränssnitt, ingen räckvidd in i en annan moduls data och upprätthållna beroenderegler. Du får enkla transaktioner, lätt omstrukturering och en sak att driftsätta och observera. Dela ut en modul till en egen tjänst först när du har ett konkret skäl: en del som måste skalas för sig, ett team som behöver driftsätta i sin egen takt, ett felområde du måste isolera eller ett teknikkrav som skiljer sig från resten. När du delar, dela längs avgränsade kontexters linjer så att varje tjänst äger sina data och exponerar ett stabilt kontrakt.

### Vet när mikrotjänster förtjänar sin plats

Mikrotjänster ger dig oberoende driftsättningsbarhet, oberoende skalning, felisolering och friheten att blanda tekniker. I gengäld kräver de mogen CI/CD (kontinuerlig integration och kontinuerlig leverans), automatiserad infrastruktur, distribuerad spårning, tjänsteupptäckt och en jourkultur. Fråga dig själv ärligt: kan din organisation köra dussintals oberoende driftsatta tjänster i produktion pålitligt? Om plattformen och driftmognaden inte finns där multiplicerar mikrotjänster bara dina felmönster utan att leverera sina fördelar. Många organisationer klarar sig bäst med en handfull grovkorniga tjänster justerade efter större domäner snarare än en svärm av små.

### Använd händelsedriven arkitektur där frikoppling och asynkronitet betalar sig

Händelsedriven arkitektur låter producenter sända fakta utan att veta vem som konsumerar dem. Det köper dig lös koppling, en buffert för belastningstoppar och ett enkelt sätt att lägga till nya konsumenter. Använd den där arbetsflöden är naturligt asynkrona och reaktiva. **CQRS** (Command Query Responsibility Segregation) skiljer skrivmodellen från en eller flera läsmodeller, vilket hjälper när läs- och skrivbelastningar eller former skiljer sig kraftigt. **Händelselagring** lagrar tillstånd som en endast-tilläggs-logg av händelser snarare än som aktuellt tillstånd, vilket ger dig ett perfekt revisionsspår och tidsresor. Det är kraftfullt för finans och myndigheter, där "hur kom vi fram till det här värdet?" är en rättslig fråga, men det lägger till verklig komplexitet i versionering av händelser, återuppbyggnad av projektioner och resonemang om eventuell konsistens. Sträck dig efter dessa med avsikt, inte som standard.

### Tillämpa gateway-, BFF- och nätmönster för att hantera många tjänster

En **API-gateway** ger externa klienter en enda ingång och hanterar autentisering, hastighetsbegränsning, routing och [TLS](https://en.wikipedia.org/wiki/Transport_Layer_Security)-terminering (Transport Layer Security). En **Backend-for-Frontend (BFF)** ger varje klienttyp (webb, mobil, partner-API) sitt eget skräddarsydda aggregeringslager, så att du undviker ett uppsvällt API som ska passa alla. Ett **tjänstenät** flyttar tvärgående angelägenheter (ömsesidig TLS, omförsök, tidsgränser, trafikomläggning och telemetri) till ett sidovagnsinfrastrukturlager, så att applikationsteam inte behöver implementera dem på nytt. Lägg till ett nät först när antalet tjänster gör det ohanterligt att hantera dessa angelägenheter per tjänst. För några få tjänster är ett nät mer driftsvikt än det är värt.

### Väg serverlös ärligt

Function-as-a-service och hanterade serverlösa plattformar tar serverhantering från ditt bord, skalar till noll och faktureras per användning, vilket är utmärkt för stötvisa, händelsedrivna eller lågbasbelastade arbetsbelastningar och för små team. Avvägningarna är verkliga: kallstartslatens, begränsningar i körtid och resurser, svårare lokal testning, möjlig leverantörsinlåsning och en kostnad som kan överstiga provisionerad infrastruktur vid ihållande hög volym. Använd serverlös där dess ekonomi och driftenkelhet tydligt vinner. Tvinga inte in stadiga, högt genomströmmande kärnsystem i den av entusiasm.

### Håll affärslogiken ren inuti varje tjänst

Vilken yttre stil det än är, håll insidan ren med **hexagonal (portar och adaptrar)** eller **ren arkitektur**: affärsregler i centrum, beroende bara av abstraktioner. Ramverk, databaser och meddelandehantering vid kanterna som utbytbara adaptrar. Det håller din värdefulla domänlogik testbar utan infrastruktur och portabel över teknikbyten: en avgörande fördel för långlivade myndighets- och företagssystem som kommer att överleva flera generationer av ramverk.

## Avvägningar: för- och nackdelar

| Stil | Bäst när | Fördelar | Nackdelar |
|---|---|---|---|
| Modulär monolit | De flesta system, särskilt tidiga | Enkel drift, enkla transaktioner och omstrukturering | En driftsättningsenhet. Skalar som en. Risk för erosion |
| Mikrotjänster | Många team, hög skala, mogen plattform | Oberoende driftsättning/skalning, felisolering | Distribuerad komplexitet, datakonsistens, hög driftskostnad |
| Händelsedriven / CQRS / händelselagring | Asynkrona arbetsflöden, revisionsbehov, divergerande läsning/skrivning | Lös koppling, granskningsbarhet, skalbar läsning | Eventuell konsistens, händelseversionering, svårare felsökning |
| Serverlös | Stötvis eller lågbaserat, händelsedrivet arbete | Ingen serverhantering, skalar till noll, betala-per-användning | Kallstarter, begränsningar, inlåsning, kostnad vid hög ihållande belastning |

Det återkommande temat: du köper flexibilitet och oberoende med drifts- och kognitiv komplexitet. Distribuerade och händelsedrivna stilar ger upp enkelheten i en enda anropsstack och en enda transaktion i utbyte mot förmågan att skala, driftsätta och fallera oberoende. Den affären betalar sig i skala och med en mogen plattform. Utan en är den ruinerande. De inre disciplinerna (hexagonal/ren) är nästan alltid värda det, eftersom de kostar lite och håller dina alternativ öppna att byta stil senare.

## Frågor att diskutera med ditt team

1. **Innan ni delar ut nästa tjänst, delar ni det team som äger den, och vem har befogenhet att göra det?** Conways lag betyder att en tjänstegräns egentligen är en teamgräns, så en delning som organisationsschemat inte stöder producerar en distribuerad monolit: två driftsättningsbara enheter, ett releasetåg, delad jour. I ett stort företag ligger befogenheten att omforma team vanligen ovanför utvecklingen, hos rapporteringslinjer, ekonomi och HR, vilket är därför arkitektur och organisationsdesign måste beslutas tillsammans. Ta med belägg till diskussionen: har den föreslagna tjänsten ett team som kan äga den från början till slut, bemanna sin egen jour och driftsätta i sin egen takt? Om svaret är nej, finansiera antingen teamet eller behåll förmågan som en modul i monoliten. Att dela kod utan att dela ägarskap köper varje kostnad för distribution och inget av oberoendet.

2. **Kan ni driftsätta var och en av era tjänster oberoende i dag, eller levereras de i hemlighet i takt?** Den distribuerade monoliten är det sämsta utfallet i det här kapitlet: du betalar för nätverksanrop, partiellt fel och datakonsistens över tjänster, men kan ändå inte släppa en utan de andra. Avslöjande tecken är en delad databas, ett delat bibliotek som tvingar fram samordnade uppgraderingar och integrationstester som måste köra hela egendomen tillsammans. För ett stort team begränsar detta i det tysta genomströmningen, eftersom varje team köar bakom en release även om diagrammet visar oberoende. Ta en nylig ändring och räkna hur många tjänster som behövde driftsättas tillsammans för att göra den säker. Om det talet är större än ett för en ändring som rörde en enda förmåga är era gränser fel. Åtgärden är vanligen att ge varje tjänst sina egna data och ett stabilt, versionerat kontrakt, inte att lägga till fler tjänster.

3. **Vilka av era befintliga tjänstedelningar har slutat betala sig, och skulle ni konsolidera tillbaka dem?** Kapitlets mest avancerade vana är att behandla stilbeslut som reversibla: extrahera när en drivkraft dyker upp och slå ihop igen när drivkraften försvinner. De flesta organisationer delar bara, så nanotjänster och pratsamma entitetstjänster ackumuleras tills orkestrering och nätverksoverhead överstiger det arbete varje tjänst gör. Leta efter tjänster som alltid driftsätts tillsammans, som finns på grund av en databastabell snarare än en affärsförmåga eller vars nätverkshopp nu dominerar en begärans latens. I företags- och myndighetsegendomar, där bemanning och budgetar granskas, är att vika tillbaka två tunna tjänster till en grovkornig tjänst ett legitimt, kostnadsbesparande drag, inte ett erkännande av misslyckande. Lägg återkonsolidering på bordet lika öppet som extrahering och besluta båda med samma belägg.

4. **Stöder er plattform och jourmognad faktiskt den stil ni föreslår, och kan ni namnge de specifika luckorna innan ni förbinder er?** Mikrotjänster, nät och händelsedrivna ryggrader levererar bara sina fördelar ovanpå mogen CI/CD, distribuerad spårning, tjänsteupptäckt och en jourkultur som kan resonera om partiellt fel. En stor organisation tenderar att besluta målstilen i ett arkitekturforum och upptäcka den saknade plattformen senare, när dussintals tjänster redan är i produktion och varje incident tar timmar att diagnostisera. Väg lockelsen i oberoende driftsättning och skalning mot den nyktra frågan om vem som driver det klockan tre på natten: samma delning som frigör team att leverera parallellt multiplicerar också de felmönster varje team måste förstå. Ta med en ärlig inventering till diskussionen: nuvarande driftsättningsfrekvens, genomsnittlig återställningstid, om ni har spårning över tjänstegränser och hur många tjänster ett enskilt team realistiskt kan driva. I företags- och myndighetsmiljöer, lägg till upphandlings- och rekryteringsledtider för de plattformsförmågor ni saknar, eftersom en stil som förutsätter ett nät och ett plattformsteam ni inte har finansierat är en plan för att köra en ohållbar egendom.

5. **För vilka delar av domänen är ett fullständigt händelselagrat revisionsspår ett rättsligt krav snarare än en bekvämlighet, och vem har befogenhet att avgöra?** Händelselagring och CQRS köper dig en perfekt, rekonstruerbar historik och läsmodeller som skalar på egen hand, men de kostar dig händelseversionering, återuppbyggnad av projektioner och resonemang om eventuell konsistens under systemets hela liv. Tillämpad på en domän som aldrig behövde revisionsspåret är den komplexiteten ren skatt. Undanhållen från en domän där "hur kom vi fram till det här värdet?" är en rättslig fråga är dess frånvaro ett regelefterlevnadsmisslyckande. De motstridiga hänsynen är granskningsbarhet och frågeskalbarhet å ena sidan, och felsökningssvårighet och utvecklarnas kognitiva belastning å den andra, så beslutet hör hemma hos människor som förstår både den regulatoriska skyldigheten och den operativa bördan, inte hos den som är mest entusiastisk över mönstret. Ta med de specifika rättsliga eller avtalsmässiga krav på bevarande och rekonstruktion, den förväntade händelsevolymen och en ärlig uppskattning av versionerings- och projektionsarbetet. Inom finans, skatt och myndigheter, där att rekonstruera ett beslut år senare kan vara en lagstadgad plikt, namnge den ansvarige ägare som godkänner att en given avgränsad kontext gör, eller inte gör, krav på en oföränderlig händelselogg.

6. **Hur hindrar ni den modulära monoliten från att eroderas så att senare extrahering förblir billig, och vad kommer att upprätthålla gränserna?** Hela argumentet för att börja med en modulär monolit vilar på löftet att rena interna gränser gör senare tjänsteextrahering prisvärd, men de gränserna förfaller tyst i samma stund en deadline frestar en modul att sträcka sig in i en annans data. För ett stort team med många bidragsgivare håller goda avsikter och kodgranskning ensamma inte linjen. Utan en upprätthållande mekanism blir monoliten i det tysta den stora lerklump stilen var tänkt att undvika. Väg friktionen av upprätthållna beroenderegler och modulgränssnitt mot kostnaden för att år senare upptäcka att ingen gräns är verklig och varje extrahering betyder att reda ut delat tillstånd. Ta med belägg: upprätthålls modulgränser av byggverktyg, statisk analys eller paketstruktur, eller är de bara dokumenterade konventioner de senaste sex sammanslagningarna ignorerade? I långlivade företags- och myndighetssystem som måste överleva strikt ändringskontroll och flera ramverksgenerationer, behandla gränsupprätthållande som en granskningsbar kontroll, så att alternativet att distribuera senare är ett ni faktiskt har bevarat snarare än ett ni antar att ni fortfarande håller.

## Sektorsperspektiv

**Startup.** Välj en enda modulär monolit som standard och stå emot dragningen mot mikrotjänster, eftersom din knappaste resurs är utvecklingsuppmärksamhet och en svärm av tjänster är driftskatt du inte har råd med före produkt-marknadspassning. Behåll rena modulgränser så att du kan extrahera senare, och sträck dig efter serverlös där skalning till noll och betala-per-användning passar din stötvisa, lågbasbelastade last. Dela exakt en sak bara när en konkret drivkraft dyker upp, som en stötvis aviseringssändare, och aldrig tidigare.

**Småföretag.** Utan plattformsteam och med snäv budget, föredra en monolit eller en handfull grova tjänster på en hanterad plattform, och köp hostad infrastruktur snarare än att bygga nät, spårning och tjänsteupptäckt själv. Väg serverlös och hanterade databaser som ett sätt att undvika att köra servrar alls, och var försiktig med en distribuerad design vars driftsbörda du inte har någon att bära. Rätt arkitektur är den en eller två personer faktiskt kan driftsätta, observera och återhämta.

**Storföretag.** Det verkliga problemet är många team och Conways lag: justera grovkorniga tjänster efter avgränsade kontexter och teamägarskap och investera medvetet i plattformen (CI/CD, spårning, nät och tjänsteupptäckt) som gör distribution säker. Standardisera gateway-, BFF- och intern ren-arkitektur-mönster så att grupper slutar uppfinna dem på nytt, och styr extrahering och återkonsolidering som belägg-baserade portföljbeslut snarare än lokal preferens. Budgetera driftskostnaden för varje delning uttryckligen, för i din skala är den distribuerade monolitens misslyckande dyrt och långsamt att lösa upp.

**Offentlig sektor.** Långa systemlivslängder, strikt ändringskontroll, upphandlingscykler och granskningsbarhet formar valet: föredra stilar med uttryckliga, inspekterbara gränser och varaktiga kontrakt som överlever leverantörer och ramverksgenerationer. Händelselagring förtjänar sin komplexitet där att rekonstruera ett medborgarvänt beslut är en lagstadgad plikt, så använd den medvetet för kärnhuvudböcker och behåll ren arkitektur inuti varje tjänst för att isolera regler som ändras med varje budget. Behandla portabilitet och utträde ur proprietära serverlösa eller leverantörsplattformar som upphandlingskrav, inte eftertankar.

## Exempel

**Startup.** En startup med fyra personer som bygger en schemaläggningsprodukt känner tryck att börja med mikrotjänster eftersom en konkurrent bloggade om dem, men stretar emot. De levererar en enda modulär monolit med tydliga interna gränser (schemaläggning, fakturering, aviseringar) som separata moduler i en driftsättningsenhet, så att en ingenjör kan köra hela saken lokalt och en release är en push. När produkten får fäste dras bara aviseringssändaren, som fläktar ut till e-post och SMS under stötvis belastning, ut i en egen tjänst. De ärver ingen av driftskatten för ett dussin tjänster medan de fortfarande jagar produkt-marknadspassning.

**Storföretag.** Ett stort e-handelsföretag börjar som en modulär monolit. När trafiken växer och teamen mångfaldigas drar det ut de mest högbelastade, mest oberoende utvecklande domänerna (katalog, varukorg, kassa och sökning) i separata tjänster, var och en med sina egna data. Kassan sänder händelser som lager, uppfyllnad och analys konsumerar genom en händelseryggrad, så att nya konsumenter (bedrägeridetektering, lojalitet) kan kopplas in utan att röra kassan. En API-gateway hanterar autentisering och hastighetsbegränsning, och en BFF skräddarsyr nyttolaster för mobil. De återstående mindre trafikerade domänerna stannar i monoliten, vilket undviker onödig fragmentering.

**Offentlig sektor.** En skattemyndighet bygger en bedömningsplattform på händelselagring för kärnhuvudboken, eftersom varje ändring av en skattskyldigs skuld måste vara rekonstruerbar och rättsligt granskningsbar i åratal. Kommandon (lämna deklaration, tillämpa betalning, utfärda justering) producerar oföränderliga händelser, och läsmodeller projicerar aktuella saldon för handläggare och medborgare. CQRS låter den publikt vända frågesidan skala på egen hand för toppsäsongen för deklarationer utan att riskera skrivsidan. Inuti följer varje tjänst ren arkitektur, så att bedömningsreglerna, som ändras med varje budget, förblir isolerade från teknikerna för persistens och meddelandehantering.

## Affärsnytta: motiv, ROI och TCO

Pengarna som står på spel i ett stilval är enorma, eftersom beslutet är dyrt att vända. Anta mikrotjänster för tidigt och du blåser upp den totala ägandekostnaden genom plattformsuppbyggnad, duplicerad infrastruktur, distribuerad felsökning och en tyngre driftsbörda: kostnader som stannar hos dig under systemets liv. Vägra dela en genuint överbelastad monolit och du sätter tak på leveransgenomströmningen: team köar bakom en delad release, och varje ändring sätter hela systemet i riskzonen. ROI-samtalet handlar egentligen om att matcha driftsutgift mot organisatoriskt behov.

Driv ärendet inför ledningen i termer av genomströmning och risk, inte teknik. Oberoende driftsättningsbarhet betyder fler team som levererar parallellt och kortare ledtider: mätbar affärshastighet. Felisolering betyder färre totala avbrott och en mindre sprängradie: mätbar tillgänglighet i drift och anseendeskydd. Men var lika ärlig om den plattformsinvestering varje stil kräver: ett nät, spårning och CI/CD-mognad är förutsättningar, inte valfria extra, och deras kostnad hör hemma i TCO. För många organisationer är den billigaste vägen en väl modulariserad monolit nu, med rena interna gränser som gör senare extrahering billig. Det köper dig alternativet att distribuera utan att betala för det innan du behöver det.

## Antimönster och fallgropar

- **Distribuerad monolit.** Tjänster som måste driftsättas tillsammans och delar en databas: all kostnad för distribution, inget av oberoendet.
- **Nanotjänster.** Tjänster så finkorniga att orkestrering och nätverksoverhead överstiger det arbete de gör.
- **Mikrotjänster utan plattform.** Att dela innan du har CI/CD, spårning och jourmognad. Felmönster multipliceras.
- **Entitetstjänster.** Att dela efter databastabell ("Användartjänst", "Ordertjänst") i stället för efter affärsförmåga, vilket tvingar fram pratsamma anrop mellan tjänster för varje operation.
- **Händelselagring överallt.** Att tillämpa den på domäner som inte behöver ett revisionsspår och betala komplexitetsskatten utan nytta.
- **Gateway som monolit.** Att lägga affärslogik i API-gatewayn och återskapa en central flaskhals.
- **Ramverkskopplad kärna.** Affärslogik trasslad med webb- eller ORM-ramverket (objekt-relationell mappning), vilket gör både testning och teknikbyte smärtsamma.

## Mognadsmodell

- **Nivå 1: Initiera.** Stil väljs efter mode eller slump. Du har en trasslig monolit eller en oavsiktlig distribuerad röra, gränser följer tekniska lager eller historia snarare än domänen och delningar sker reaktivt när något går sönder.
- **Nivå 2: Utveckla.** Vissa team drar medvetna modulgränser inuti monoliten eller sätter upp några grova tjänster, och vissa tvärgående angelägenheter hanteras konsekvent. Praxis är ojämn: en grupp justerar tjänster efter avgränsade kontexter medan en annan fortfarande delar efter databastabell, och extrahering förblir ad hoc.
- **Nivå 3: Standardisera.** Ett dokumenterat tillvägagångssätt upprätthålls i hela organisationen: tjänster justeras efter avgränsade kontexter och äger sina data, gateway- och BFF-mönster används där det är lämpligt, intern ren eller hexagonal skiktning är standarden och varje delning kräver en angiven drivkraft. Modulgränser upprätthålls av verktyg, inte bara konvention.
- **Nivå 4: Hantera.** Stilbeslut mäts och styrs mot utgångslägen. Du följer driftsättningsfrekvens och ledtid per tjänst, genomsnittlig återställningstid, hur många tjänster som måste driftsättas tillsammans för en typisk ändring och nätverkshoppens latens, och du jämför varje delnings kostnad mot det oberoende den var tänkt att köpa. Belägg, inte preferens, avgör om en gräns överlever, och drift mot en distribuerad monolit fångas av mått snarare än av ett avbrott.
- **Nivå 5: Orkestrera.** Arkitekturen är integrerad med organisationsdesign och kontinuerligt anpassad. En mogen plattform (CI/CD, spårning och nät där det är motiverat) gör både distribution och återkonsolidering billig, team extraherar rutinmässigt när en drivkraft dyker upp och viker tillbaka tjänster när en försvinner, och stilval omfördelas när teamtopologi, belastning och riskbilden förskjuts över hela egendomen.

## Idéer för diskussion

1. Var i ert system är en monolit faktiskt en styrka, och var är den en genuin flaskhals?
2. Vilken konkret drivkraft skulle motivera att extrahera er nästa tjänst, och kan ni namnge den innan ni bygger den?
3. Har er organisation den driftmognad mikrotjänster kräver? Vad saknas?
4. För vilka delar av er domän är ett fullständigt händelselagrat revisionsspår en rättslig eller affärsmässig nödvändighet mot ett trevligt-att-ha?
5. Hur väl speglar era nuvarande tjänstegränser era teamgränser, och hjälper eller skadar den justeringen?
6. Om ni måste byta ert webbramverk eller er databas nästa år, hur mycket av er affärslogik skulle ni behöva skriva om?

## Viktigaste punkter

- Välj arkitekturstil utifrån verkliga krafter (teamstorlek, domän, belastning, driftmognad), inte utifrån mode.
- En modulär monolit är rätt standard för de flesta system. Extrahera tjänster bara med en konkret drivkraft och längs avgränsade kontexters linjer.
- Mikrotjänster byter drifts- och kognitiv komplexitet mot oberoende driftsättning, skalning och felisolering. De kräver en mogen plattform.
- Händelsedriven, CQRS och händelselagring erbjuder frikoppling och granskningsbarhet till priset av eventuell konsistens och versioneringskomplexitet. Anta dem medvetet.
- Gateways, BFF:er och nät tämjer egendomar med många tjänster men lägger till vikt. Inför dem när skalan kräver, inte tidigare.
- Tillämpa hexagonal/ren arkitektur inuti varje tjänst för att hålla värdefull affärslogik testbar och varaktig över teknikbyte.

## Referenser och vidare läsning

- Sam Newman, *Building Microservices* and *Monolith to Microservices*
- Chris Richardson, *Microservices Patterns*
- Eric Evans, *Domain-Driven Design*
- Vaughn Vernon, *Implementing Domain-Driven Design*
- Robert C. Martin, *Clean Architecture*
- Alistair Cockburn, "Hexagonal Architecture (Ports and Adapters)"
- Gregor Hohpe and Bobby Woolf, *Enterprise Integration Patterns*
- Martin Fowler, *Patterns of Enterprise Application Architecture* (and articles on CQRS and Event Sourcing)
- Matthew Skelton and Manuel Pais, *Team Topologies*
