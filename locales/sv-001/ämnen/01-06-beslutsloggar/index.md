# 1.6 Beslutsloggar

## Översikt och motivation

En **beslutspost** är ett dokument som fångar ett viktigt beslut tillsammans med dess sammanhang och konsekvenser. Den mest kända formen är **[arkitekturbeslutsposten](https://en.wikipedia.org/wiki/Architectural_decision) (ADR)**, en kort anteckning, helst oföränderlig, som dokumenterar ett arkitektoniskt betydande val, varför det gjordes och vad som följer av det. Ett projekts hela uppsättning poster är dess **beslutslogg (ADL)**, och disciplinen att föra dem är en del av **hantering av arkitekturkunskap (AKM)**. Det här kapitlet bygger på praxis för beslutsfattande och styrning i kapitel 1.5 och fokuserar på hur du skriver, lagrar och vidmakthåller beslutsposter i stor skala.

Motivet är enkelt och smärtsamt att lära sig den hårda vägen. I ett långlivat system är den dyraste frågan "varför i all världen byggdes det så här?", ställd månader eller år senare av människor som inte var med i rummet. Koden visar *vad* systemet gör. Testerna visar att det *fungerar*. Men ingen av dem fångar *varför* du valde den här vägen framför de alternativ du övervägde och förkastade. Utan beslutsposter förångas det resonemanget med personalomsättningen. Team prövar avgjorda frågor på nytt, river upp goda beslut av dåliga skäl eller behåller dåliga beslut av rädsla. En beslutspost är ett billigt brev till framtiden som bevarar resonemanget.

För stora team är detta lika mycket ett samordningsverktyg som ett minnesstöd. Företag har dussintals team som gör överlappande val. En gemensam beslutslogg förvandlar ett teams hårt förvärvade resonemang till en återanvändbar tillgång och förhindrar divergerande, oförenliga beslut. I offentlig och reglerad verksamhet är beslutsposter nästan obligatoriska. Revisorer, tillsynsorgan och efterföljande konsulter behöver alla en spårbar motivering som kopplar arkitektoniskt betydande krav till de val som gjorts mot dem. En väl förd beslutslogg är ofta skillnaden mellan ett system du kan säkerställa och revidera och ett du inte kan.

## Nyckelprinciper

- **Dokumentera *varför*, inte bara *vad*.** Sammanhang och förkastade alternativ är poängen.
- **Ett beslut per post.** Håll varje post specifik och självständig.
- **Litet och lätt slår heltäckande och oanvänt.** En post på en sida som finns slår en rapport som aldrig skrivs.
- **Tidsstämpla allt.** Kostnader, begränsningar och leverantörer ändras. Datera varje påstående.
- **Föredra en levande logg, pragmatiskt.** Oföränderlighet är idealet. I praktiken, komplettera med daterade noteringar.
- **Ord framför förkortningar.** "Beslut" inbjuder till mer bidrag än "ADR:er".
- **Gör beslut sökbara och, där det går, testbara.** Visa rätt post i rätt ögonblick. Säkerställ den med anpassningsfunktioner.

## Rekommendationer

### Fånga den väsentliga strukturen

En bra beslutspost har några väsentliga avsnitt. Anpassa en känd mall i stället för att uppfinna en:

- **Titel:** en kort fras i imperativ, presens ("Använd [PostgreSQL](https://en.wikipedia.org/wiki/PostgreSQL) för huvudboken").
- **Status:** föreslagen, godkänd, ersatt, avvecklad.
- **Sammanhang:** situationen, krafterna, affärsprioriteringarna och begränsningarna som gör beslutet nödvändigt. Ta med det arkitektoniskt betydande kravet det adresserar.
- **Beslut:** det gjorda valet, uttryckt tydligt.
- **Konsekvenser:** vad som blir enklare och vad som blir svårare, följdbeslut som utlöses och risker som accepteras.

Populära mallar inkluderar Michael Nygards (enkel och vitt använd), Tyrees och Akermans (mer utarbetad, med viktade alternativ), MADR (Markdown Any Decision Records, stark på alternativ och deras för- och nackdelar) och Y-statements (en strukturerad form på en mening). Standardisera på en per organisation, så att poster går att jämföra. Se kapitel 12.3 för en mall att kopiera.

### Skriv poster som är specifika, daterade och nästan oföränderliga

Håll varje post till exakt ett beslut. Tidsstämpla enskilda påståenden, särskilt allt som driver: prissättning, skalningstal, leverantörers förmågor, licensvillkor. I teorin bör en post vara oföränderlig. När ett beslut ändras skriver du en *ny* post som ersätter den gamla och bevarar historiken. I praktiken tycker många team att ett **levande dokument** fungerar bättre: infoga ny information i den befintliga posten med en datumstämpel och en notering att den kom efter beslutet. Båda är legitima. Den oföränderliga stilen är starkare för revisionsspår. Den levande stilen är bättre för vardaglig teamkunskap. Välj medvetet och var konsekvent.

### Lagra poster där arbetet sker

Lägg beslutsposter i [versionshantering](https://en.wikipedia.org/wiki/Version_control) tillsammans med koden: en `decisions/`-katalog (eller `adr/`) med [Markdown](https://en.wikipedia.org/wiki/Markdown)-filer, en per beslut, namngivna med en gemen, bindestrecksseparerad imperativfras (`choose-database.md`, `format-timestamps.md`). Det ger dig historik, granskning och diffar på köpet och håller motiveringen intill det den förklarar. Om ditt team hellre använder [wikis](https://en.wikipedia.org/wiki/Wiki), Google Docs eller ett Jira-liknande ärendesystem, använd dem i stället. Verktyget spelar mycket mindre roll än vanan. Ett lätt kommandoradsverktyg (som `adr-tools`) kan skapa och indexera poster.

### Kalla dem "beslut" och bredda bortom arkitektur

En praktisk insikt från många team: etiketten spelar roll. Vissa utvecklare och chefer rynkar på näsan åt ordet "arkitektur", och "post" kan kännas som pappersarbete i efterhand. Att helt enkelt döpa om katalogen till "decisions" vänder ofta på en strömbrytare. Team börjar dokumentera leverantörsval, planeringsbeslut, schemabeslut, data- och regelefterlevnadsbeslut, allt med samma mall. Människor lär sig snabbare av ord än av förkortningar, och de bidrar mer när ramen är "hjälp dina framtida kollegor att tänka" snarare än "fyll i det obligatoriska formuläret".

### Definiera livscykeln och styrningen

För att beslutsposter ska skala, kom överens om den omgivande processen (här möter kapitel 1.5:s styrning praktiken):

- **Vem kan väcka en, och vad motiverar det:** vanligen vilken insatt bidragsgivare som helst. Väck en post när framtida utvecklare kommer att behöva *varför*, och hoppa över den för lågriskiga, självständiga eller redan dokumenterade val.
- **Livscykel:** ett enkelt flöde som *Initiera → Undersöka → Utvärdera → Genomföra → Underhålla → Avveckla*, med godkännandekriterier för att gå mellan stegen (problemet formulerat, alternativ övervägda, avvägningar dokumenterade, intressenter hörda).
- **Roller:** förslagsställare, undersökare, granskare, godkännare och en ansvarig underhållare som granskar posten periodiskt (minst årligen) och driver den eventuella avvecklingen.
- **Styrning:** hur konsensus, konflikt, eskalering och veto fungerar, och eventuella regelefterlevnadsbegränsningar. Luta dig mot principer som *benägenhet att handla* och *[disagree-and-commit](https://en.wikipedia.org/wiki/Disagree_and_commit)*, och reservera tyngre process för irreversibla beslut med stor sprängradie ("envägsdörr").

### Gör beslut testbara och sökbara

En beslutspost *dokumenterar* ett beslut. En **anpassningsfunktion** *säkerställer* det: en automatiserad kontroll, körd i [kontinuerlig integration](https://en.wikipedia.org/wiki/Continuous_integration) (CI), som verifierar att beslutet fortfarande gäller ("alla tillståndsändringar måste skicka händelser", "ingen modul får importera över dessa gränser", med verktyg som ArchUnit). Det förvandlar styrning från periodisk manuell granskning till kontinuerlig, skalbar efterlevnad, särskilt värdefullt för mål kring regelefterlevnad och revision (kapitel 3.1, 4.6, 8.5). Visa sedan *rätt* post i *rätt* ögonblick. Verktyg som bifogar relevanta beslut till en pull request, när en utvecklare rör den kod de styr, slår att hoppas att människor läser en dokumentmapp.

## Avvägningar: för- och nackdelar

| Val | Fördelar | Nackdelar |
|---|---|---|
| **Lätta ADR:er (Nygard/MADR)** | Snabba att skriva, blir faktiskt skrivna. Lite ceremoni | Mindre stringens för högriskbeslut under strid |
| **Tunga mallar (Tyree-Akerman)** | Viktade alternativ. Starka för stora, kostsamma val | Långsammare. Kan avskräcka från rutindokumentation |
| **Oföränderlig + ersätt** | Rent revisionsspår. Historik bevarad | Fler poster. Läsare måste följa kedjor |
| **Levande dokument (daterade tillägg)** | En enda aktuell sanningskälla. Lätt att underhålla | Svagare revisionsberättelse. Risk för tysta ändringar |
| **Markdown i repot** | Versionshanterat, granskningsbart, intill koden | Mindre vänligt för icke-utvecklare |
| **Wiki / dokumentverktyg** | Tillgängligt för alla roller | Svagare historik och granskning. Driver från koden |

Den centrala spänningen är **stringens mot användning**. Det mest stringenta system som ingen använder dokumenterar ingenting. Det lättaste system som alla använder växer i värde. Välj lätt som standard, och reservera tyngre process för de få beslut som är dyra och svåra att vända.

## Frågor att diskutera med ditt team

1. **Hur når rätt beslutspost en utvecklare i det ögonblick de rör koden den styr, i stället för att ligga i en mapp ingen öppnar?** En logg som bara skrivs dokumenterar resonemang som aldrig ändrar beteende, vilket är det vanligaste sättet beslutsposter misslyckas på: de finns, och ingen läser dem när det gäller. Den motstridiga hänsynen är arbetsinsats, eftersom att visa poster automatiskt (bifoga dem till en pull request när någon redigerar den styrda koden) kräver verktygsinvestering som en wiki eller dokumentmapp inte gör. Ta med belägg till diskussionen: när någon nyligen vände eller prövade om en avgjord fråga, var den relevanta posten sökbar i det ögonblicket, eller begravd? För en stor organisation med dussintals team är sökbarhet det som förvandlar ett teams hårt förvärvade resonemang till en återanvändbar tillgång i stället för ett privat arkiv. Besluta om du ska lagra poster i versionshantering intill koden och koppla in dem i pull request-flödet, så att posten dyker upp där arbetet sker.

2. **Vem är ansvarig underhållare för varje post, och vad hindrar din logg från att förfalla till självsäker felinformation?** En beslutslogs farliga felläge är inte en tom mapp, utan en mapp full av poster vars kostnader, leverantörsförmågor och begränsningar i det tysta blev inaktuella för år sedan. Varje post behöver en ansvarig ägare som granskar den med jämna mellanrum (minst årligen) och driver ersättning eller avveckling, annars ruttnar loggen till folklore människor citerar selektivt och litar lite på. Ta med belägg: hur många av era poster är odaterade, hur många beskriver en leverantör eller ett pris som sedan ändrats och när varje granskades senast. I offentliga och reglerade miljöer är detta skarpare, eftersom en oföränderlig, ersatt kedja är precis vad revisorer och efterföljande konsulter förlitar sig på för en spårbar motivering. Bestäm uttryckligen er livscykel, tidsstämpla enskilda påståenden som driver och utse underhållare, så att loggen förblir en levande tillgång snarare än en kyrkogård.

3. **Bör ni standardisera på en mall över alla team, och hur mycket stringens behöver era mest högriskbeslut faktiskt?** Jämförbarhet är en verklig fördel: när varje team använder samma form (Nygard, MADR eller liknande) kan ett nytt team hitta tre tidigare poster och anta resonemanget på en eftermiddag i stället för en månads debatt. Den centrala spänningen är stringens mot användning, eftersom den tyngsta mall som ingen använder dokumenterar ingenting, medan den lättaste som alla använder växer i värde. Ta med belägg: blir poster faktiskt skrivna, och separat, har några stora, omstridda, dyra beslut analyserats för lite därför att den lätta formen hoppade över att väga alternativ? För företag som samordnar överlappande val över team förhindrar en gemensam mall plus ett sökbart index divergerande, oförenliga beslut. Välj lätt för det vanliga fallet och kom överens i förväg om vilka envägsdörr-beslut som motiverar en tyngre form med viktade alternativ.

4. **Vad motiverar egentligen att väcka en beslutspost, och vem har befogenhet att säga att ett val inte behöver någon?** Sätt ribban för högt och resonemanget bakom avgörande val förångas. Sätt den för lågt och loggen fylls med bagateller som begraver de poster människor verkligen behöver. För en stor organisation betyder en oklar tröskel att varje team improviserar sin egen, så täckningen blir ojämn och ingen kan lita på att en saknad post signalerar ett oviktigt beslut. Ta med belägg till diskussionen: en handfull nyliga beslut som dokumenterades men inte behövde vara det, och smärtsamma som förblev odokumenterade och senare kostade en återupptäckt. Kom överens om ett enkelt test, till exempel att dokumentera när en framtida utvecklare kommer att behöva *varför* och hoppa över lågriskiga, självständiga eller redan dokumenterade val. I reglerade och offentliga miljöer förskjuts kalkylen, eftersom ett revisionsmandat kan kräva en post för varje arkitektoniskt betydande krav oavsett om teamet bedömer det värt att skriva, så namnge i förväg vilka beslut som är icke förhandlingsbara.

5. **Är era poster verkligt resonemang fångat i beslutsögonblicket, eller pappersarbete skrivet efteråt för att uppfylla ett mandat?** En post som produceras i efterhand för att stänga ett ärende tenderar att tvätta det valda alternativet och i det tysta utelämna de alternativ som faktiskt vägdes, vilket är just den information en framtida läsare behöver mest. Det motstridiga trycket är verkligt: att skriva *varför* före eller under ett beslut känns långsammare än att leverera, och att erkänna de förkastade vägarna skriftligt kräver en psykologisk trygghet som vissa team saknar. Ta med ett urval av nyliga poster till bordet och fråga ärligt om sammanhanget och de förkastade alternativen läses som verkligt övervägande eller som efterhandskonstruerad rättfärdigande. För ett stort team är ihåliga poster värre än inga, eftersom de lär människor att loggen inte går att lita på. Vid företags- och myndighetsrevision är skillnaden skarp: tillsynsorgan och efterföljande konsulter är beroende av en motivering som speglar vad som verkligen övervägdes, och en post som läses som teater undergräver den säkerhet loggen finns för att ge.

6. **Vilka av era mest högriskbeslut kan ni säkerställa med en automatiserad anpassningsfunktion, i stället för att lita på att periodisk manuell granskning fångar en överträdelse?** En beslutspost dokumenterar ett val, men bara en automatiserad kontroll körd i kontinuerlig integration hindrar det valet från att tyst eroderas när dussintals utvecklare rör koden under åratal. Avvägningen är investering, eftersom att skriva och underhålla anpassningsfunktioner (med verktyg som ArchUnit) kostar utvecklingstid, och många beslut, särskilt process- eller leverantörsval, inte alls går att testa mekaniskt. Ta med belägg: vilka gränsbeslut (moduleberoenden, händelseutskick, dataåtkomstregler) har i det tysta överträtts och fångats först sent i granskning eller i produktion. För ett företag med många team förvandlar anpassningsfunktioner styrning från en central flaskhals till kontinuerlig efterlevnad som skalar utan att sakta ner alla. I reglerade och offentliga sammanhang är en automatiserad, ständigt aktiv kontroll ett långt starkare revisionsbelägg än en signatur på en granskning, eftersom den bevisar att beslutet fortfarande gäller i dag snarare än att någon en gång godkände det.

## Sektorsperspektiv

**Startup.** Håll dig till vanan och inget annat: en `decisions/`-mapp i ditt huvudrepo och en anteckning i två delar (sammanhang och val) när du gör ett val ditt framtida jag kommer att ifrågasätta. Hoppa över livscykel, roller och godkännare helt, eftersom process du inte kan upprätthålla är process du kommer att överge. Den enda posten som besparar din första anställda från att fråga varför systemet är byggt så här betalar redan för hela praktiken.

**Småföretag.** Utan särskild arkitekt och med lite tid, lägg poster där ditt team redan arbetar, vare sig det är en wiki, ett delat dokument eller repot, i stället för att köpa ett dedikerat verktyg. Vanan spelar mycket större roll än verktygen, så sänk tröskeln: döp katalogen till `decisions` i stället för `adr` och dokumentera leverantörs- och bygga-mot-köpa-val i samma andetag som tekniska. När du lutar dig mot externa konsulter är en kort daterad post om varför du valde en leverantör eller plattform billig försäkring mot att bli inlåst i ett val ingen senare kan förklara.

**Storföretag.** Arbetet är samordning över många team: standardisera på en mall, publicera ett sökbart index över team och säkra viktiga gränsbeslut med anpassningsfunktioner så att överträdelser fäller bygget i stället för att vänta på granskning. Tilldela en ansvarig underhållare till varje post med en granskningstakt, så att loggen förblir en levande tillgång i stället för att förfalla till folklore. Väl gjort blir ett teams resonemang om ett svårt val en tillgång nästa team antar på en eftermiddag i stället för att pröva om.

**Offentlig sektor.** Upphandlingsregler, transparens och offentlig ansvarsskyldighet gör beslutsposter nästan obligatoriska. Kräv en oföränderlig, ersatt post för varje arkitektoniskt betydande krav, var och en med koppling mellan valet och det mandat eller den regelefterlevnadskontroll den uppfyller, så att tillsynsorgan hittar en spårbar motivering snarare än en rekonstruktion. Eftersom offentliga system har fleråriga livslängder med flera leverantörer är en väl förd logg ofta det som låter en efterföljande konsult förstå varför systemet har sin form och fortsätta arbetet utan att pröva avgjord mark på nytt.

## Exempel

**Startup.** En startup med fem personer lägger till en enkel `decisions/`-mapp i sitt huvudrepo, med en anteckning i två delar (sammanhang och val) när någon gör ett val deras framtida jag kommer att ifrågasätta. Det finns ingen livscykel, inga roller och inga godkännare: bara vanan att skriva *varför* intill koden. När deras första anställda börjar sex månader senare läser hon hela mappen på en timme och slutar fråga "varför är det byggt så här?" Den lätta loggen kostar minuter per post och besparar dem den återupptäcktsskatt som biter långt innan ett team blir stort.

**Storföretag.** En detaljhandlare med 30 utvecklingsteam standardiserar på poster i MADR-format i varje repo, plus ett sökbart centralt index. När ett nytt team står inför "[monorepo](https://en.wikipedia.org/wiki/Monorepo) mot multirepo" hittar de tre tidigare poster med sammanhang och konsekvenser och antar resonemanget på en eftermiddag i stället för en månads debatt. Viktiga gränsbeslut (tjänsteägarskap, dataåtkomstregler) säkras med ArchUnit-anpassningsfunktioner, så överträdelser fäller bygget i stället för att fångas i granskning. Det är styrning som skalar utan en central flaskhals.

**Offentlig sektor.** En myndighet som moderniserar ett bidragssystem kräver en ADR för varje arkitektoniskt betydande krav, var och en med koppling mellan beslutet och det mandat eller den regelefterlevnadskontroll det uppfyller (tillgänglighet, dataplacering, spårbarhet). Posterna är oföränderliga och ersätts, vilket ger en spårbar logg som klarar tillsynsgranskning. Avgörande är att den också låter en efterföljande konsult förstå *varför* systemet har sin form, vilket bevarar kontinuiteten över de fleråriga, flerleverantörslivslängder som är typiska för offentliga program (kapitel 4.6, 10.4).

## Affärsnytta: motiv, ROI och TCO

En beslutspost tar minuter att skriva och några fler att granska. Avkastningen är undvikd kostnad för *ombeslut* och undvikd kostnad för *felaktig vändning*, båda stora och återkommande i långlivade system. Varje gång ett team prövar en avgjord fråga på nytt, eller vänder ett sunt val därför att ingen mindes begränsningen bakom det, betalar de i seniora ingenjörers tid och ofta i en incident. En beslutslogg omvandlar den återkommande skatten till en engångsskrivning.

För **total ägandekostnad** hör beslutsposter till den mest hävstångsstarka dokumentation du kan föra, eftersom de riktar sig mot den enskilt mest personalomsättningskänsliga tillgången: motiveringen. Introduktionen blir snabbare (nyanställda läser *varför*, inte bara koden). Moderniseringen blir säkrare (kapitel 3.6: du kan skilja väsentliga beslut från tillfälliga). Revisioner blir billigare (beläggen finns redan). Kostnaden för att *inte* föra dem är osynlig på varje instrumentpanel och växer tyst för varje avgång. För att övertyga ledningen, peka på en nylig dyr återupptäckt, eller ett vänt beslut som orsakade en incident, och notera att åtgärden kostar nästan ingenting att införa.

## Antimönster och fallgropar

- **Att dokumentera *vad* utan *varför*:** att utelämna sammanhang och förkastade alternativ, hela poängen.
- **Pappersarbete i efterhand:** poster skrivna för att uppfylla ett mandat, inte för att tänka. De läses som ihåliga och ingen litar på dem.
- **Megadokument med många beslut:** en enda jättesida ingen kan navigera eller ersätta rent.
- **Odaterade påståenden:** kostnader och begränsningar som en gång var sanna, presenterade som tidlösa.
- **Tysta ändringar:** att ändra ett besluts historik utan daterad notering och förstöra revisionsspåret.
- **Skrivbara loggar:** poster som skapas och aldrig visas i det ögonblick de är relevanta, så de påverkar inte beteende.
- **Förkortningsgrindvaktande:** att insistera på "ADR" och "arkitektur" och därmed avskräcka från bidrag.
- **Ingen livscykel:** poster som aldrig granskas, ersätts eller avvecklas och förfaller till felinformation.

## Mognadsmodell

- **Nivå 1 (Initiera):** Beslut bor i människors huvuden, chattrådar och commit-meddelanden. Dokumentationen är reaktiv och ad hoc, och motiveringen går rutinmässigt förlorad med personalomsättning.
- **Nivå 2 (Utveckla):** Vissa team för poster, i varierande format och mallar, när någon individ kommer ihåg det. Praxis är inkonsekvent över team, utan gemensam logg, namngivning eller process.
- **Nivå 3 (Standardisera):** En enda mall, lagring i repot och en definierad livscykel och styrning (kriterier för att väcka eller hoppa över, roller, granskningstakt) är dokumenterade och tillämpas konsekvent i hela organisationen. Poster granskas och ersätts snarare än redigeras tyst.
- **Nivå 4 (Hantera):** Beslutsloggen mäts mot utgångslägen: täckning (andelen arkitektoniskt betydande beslut som har en post), aktualitet (andelen poster granskade inom sin takt, plus antalet odaterade eller inaktuella påståenden) och sökbarhet (hur ofta en relevant post faktiskt nådde utvecklaren som ändrade den styrda koden). Ansvariga underhållare agerar på dessa mått, ersätter inaktuella poster och stänger täckningsluckor på grundval av belägg snarare än anekdoter.
- **Nivå 5 (Orkestrera):** En sökbar beslutslogg över team är integrerad i det dagliga arbetet: relevanta poster visas automatiskt på de ändringar de styr, viktiga beslut säkerställs av anpassningsfunktioner i kontinuerlig integration och loggen matar introduktion, modernisering och revision som en levande tillgång. Organisationen förbättrar kontinuerligt själva praktiken, avvecklar, ersätter och omdefinierar poster när systemet och dess begränsningar förskjuts och omfördelar var den investerar stringens när beslutsportföljen växer.

## Idéer för diskussion

1. Vilket var det senaste beslut ditt team vände eller prövade om därför att ingen mindes det ursprungliga resonemanget?
2. Skulle det ändra vem som bidrar och vad som dokumenteras om ni döpte om er `adr/`-katalog till `decisions/`?
3. Vilka av era kritiska beslut skulle kunna säkerställas av en automatiserad anpassningsfunktion i dag?
4. Oföränderligt-och-ersätt eller levande dokument: vilket passar era revisionsskyldigheter och er kultur, och varför?
5. Hur skulle en nyanställd (eller en efterföljande konsult) i dag upptäcka *varför* ert system har den form det har?
6. Vad motiverar att väcka en beslutspost i ditt team, och vad motiverar att *inte* väcka en?

## Viktigaste punkter

- En beslutspost fångar ett viktigt beslut med dess **sammanhang och konsekvenser**: *varför*, inte bara *vad*.
- Håll poster **specifika, tidsstämplade och lätta**. Standardisera på en mall (Nygard, MADR eller liknande).
- Lagra dem **i versionshantering intill koden**. Överväg att kalla dem "beslut" för att bredda bidragen.
- Definiera en **livscykel och styrning** (kriterier för att väcka eller hoppa över, roller, granskningstakt). Reservera tung process för envägsdörr-beslut.
- Gör beslut **sökbara** i ögonblicket för ändring och, där det går, **testbara** via anpassningsfunktioner.
- ROI är undvikd återupptäckt och undvikd kostnad för felaktig vändning. TCO-argumentet är starkast där personalomsättning, modernisering och revision spelar störst roll. Se kapitel 1.5 (beslutsfattande och styrning) och kapitel 3.1 (arkitekturens grunder).

## Referenser och vidare läsning

- Michael Nygard, "Documenting Architecture Decisions" (2011): the foundational lightweight ADR.
- MADR: Markdown Any Decision Records project (adr.github.io/madr).
- Jeff Tyree and Art Akerman, "Architecture Decisions: Demystifying Architecture" (*IEEE Software*, 2005).
- Olaf Zimmermann, "Y-Statements" and "Architectural Decision Making" (ozimmer.ch).
- Joel Parker Henderson, *Architecture Decision Record (ADR)*: templates, examples, and teamwork guidance (github.com/joelparkerhenderson/architecture-decision-record).
- ThoughtWorks Technology Radar: "Lightweight Architecture Decision Records."
- Neal Ford, Rebecca Parsons, Patrick Kua, Pramod Sadalage, *Building Evolutionary Architectures* (fitness functions).
- AWS Prescriptive Guidance, "ADR process"; Red Hat, "Why you should use ADRs."
- Wikipedia, "Architectural decision" and "Architecturally significant requirements."
