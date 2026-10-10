# 1.5 Beslutsfattande och styrning

## Översikt och motivation

Varje programvarusystem är summan av tusentals beslut: vilken [databas](https://en.wikipedia.org/wiki/Database), vilken arkitektur, vilket bibliotek, om du ska bygga eller köpa, när du ska ta på dig skuld och när du ska betala av den. Styrning är hur du fattar de här besluten väl och konsekvent, involverar rätt människor utan att skapa flaskhalsar och bevarar resonemanget så att framtida team inte är dömda att lära sig om det. I ett litet team sker beslut i samtal och lever i delat minne. I stor skala förångas det minnet. Människor slutar, team omorganiseras och "varför" bakom ett kritiskt val går förlorat, så att efterträdare antingen kopierar det blint eller rycker ut det blint. God styrning är maskineriet som gör beslut synliga, medvetna och varaktiga över en stor och föränderlig organisation.

Den centrala utmaningen för stora team är att balansera autonomi mot samstämmighet. Skjut alla beslut uppåt till en central nämnd, och du får enhetlighet, men till priset av förlamande flaskhalsar och maktlösa team. Skjut alla beslut nedåt, och du får hastighet, men till priset av kaos: oförenliga tekniker, dubbelarbete och upprepade misstag. Det mogna svaret är varken centralisering eller anarki. Det är en lagerindelad modell. Team bestämmer det mesta lokalt inom en väl markerad "upptrampad stig", medan en lätt, transparent process styr de verkligt tvärgående och svåråterkalleliga valen. Målet är att göra goda beslut till den enkla standarden och att spendera knapp styrningsuppmärksamhet bara där den verkligen spelar roll.

Företag och myndigheter bär högre insatser. De måste tillfredsställa revisorer, tillsynsmyndigheter och granskande organ som kräver dokumenterade, försvarbara beslut. De arbetar över långa tidsperspektiv, där ett dåligt arkitekturval eller en ohanterad hög av [teknisk skuld](https://en.wikipedia.org/wiki/Technical_debt) kan tynga dem i ett decennium. Och deras upphandlings- och regelefterlevnadsskyldigheter gör beslut om bygga eller köpa särskilt avgörande och svåra att vända. För de här organisationerna är disciplinerat, väl dokumenterat beslutsfattande inte byråkrati för sin egen skull. Det är riskhantering, institutionellt minne och grunden för ansvarsskyldighet.

## Nyckelprinciper

- Dokumentera beslut och deras resonemang. Ett beslut utan motivering är en belastning.
- Skjut beslut till den lägsta nivå som har sammanhanget, inom tydliga skyddsräcken.
- Anpassa processens tyngd till beslutets tyngd och återkallelighet.
- Skilj reversibla ("tvåvägsdörr") från irreversibla ("envägsdörr") beslut och styr dem olika.
- Föredra upptrampade stigar och standardval framför godkännanden fall för fall.
- Behandla teknisk skuld som en hanterad portfölj, inte ett moraliskt fel att dölja.
- Gör styrningen transparent. Dolt beslutsfattande föder misstro och omarbete.

## Rekommendationer

### Inför arkitekturbeslutsloggar och en rätt dimensionerad RFC-process

En [arkitekturbeslutslogg](https://en.wikipedia.org/wiki/Architectural_decision) (Architecture Decision Record, ADR) är ett kort, oföränderligt dokument som fångar ett betydande beslut: dess sammanhang, de övervägda alternativen, det gjorda valet och konsekvenserna. Lagra ADR:er i versionshantering tillsammans med koden, så att resonemanget följer med systemet. För beslut som behöver synpunkter innan de fattas, använd en lätt [RFC](https://en.wikipedia.org/wiki/Request_for_Comments)-process (request for comments): sprid ett förslag, bjud in till kommentarer under en avgränsad period, besluta och dokumentera sedan. Håll båda lätta. Värdet ligger i tänkandet och det varaktiga registret, inte i omständliga mallar. Tillsammans förvandlar ADR:er och RFC:er tyst, bortglömt resonemang till ett sökbart institutionellt minne.

### Styr genom upptrampade stigar, inte grindvakter

I stället för att granska varje beslut ett i taget, investera i en "upptrampad stig": en uppsättning godkända, väl stödda standardval, godkända språk, ramverk, driftsättningspipelines och mönster, som team kan anta med liten friktion och gott stöd. Team som håller sig på den upptrampade stigen behöver lite styrning, eftersom det säkra, regelföljande valet också är det enkla. Team med ett verkligt skäl att lämna den kan göra det, men tar på sig det extra ansvaret och en lätt granskning. Den här "gyllene stig"-modellen skalar mycket bättre än en central nämnd som godkänner allt, eftersom den flyttar styrningen från grindvaktande fall för fall till väl utformade standardval.

### Använd arkitekturgranskningsnämnder sparsamt och transparent

En arkitekturgranskningsnämnd, eller dess motsvarighet, har en legitim roll för de största, mest tvärgående eller mest irreversibla besluten, och för att sätta de standarder som definierar den upptrampade stigen. Håll dess omfattning snäv, dess kriterier publicerade och dess process snabb och rådgivande, inte en obligatorisk flaskhals för rutinarbete. Nämndens uppgift är att förvalta sammanhang och dela kunskap, inte att godkänna varje val. När en nämnd blir en kö som varje projekt måste vänta i har den misslyckats. Delegera offensivt och reservera central granskning för de få beslut som verkligen motiverar det.

### Gör bygga-mot-köpa-mot-anta till en medveten analys

För varje betydande förmåga, väg tre vägar: bygg den internt, köp en kommersiell produkt eller anta en [öppen källkod](https://en.wikipedia.org/wiki/Open-source_software)-lösning. Bygg när förmågan är en verklig differentierare och central för ditt uppdrag. Köp eller anta de odifferentierade förmågor som andra gör bättre. Räkna [total ägandekostnad](https://en.wikipedia.org/wiki/Total_cost_of_ownership) (TCO), inte bara priset i förväg. Att köpa medför licens-, integrations- och [inlåsningskostnader](https://en.wikipedia.org/wiki/Vendor_lock-in). Att bygga medför ständigt underhåll och bemanning. Att anta öppen källkod medför skyldigheter kring support och säkerhetsbevakning. Dokumentera beslutet och dess antaganden som en ADR, så att du kan ompröva det när omständigheterna ändras.

### Hantera teknisk skuld som en portfölj

Teknisk skuld är inte i sig dålig. Ibland är det rätt val att ta på sig den för att leverera tidigare. Det som är dåligt är ohanterad, osynlig, bortglömd skuld. För en uttrycklig förteckning över betydande skuld. För varje post, notera den kostnad den medför (den löpande "räntan") och kostnaden för att åtgärda den. Hantera den sedan som en finansiell portfölj. Betala av högränteskuld som bromsar teamet varje dag. Tolerera lågränteskuld i stabila hörn. Fatta skuldbeslut medvetet snarare än av en slump. Avsätt en stående andel av kapaciteten för att betala av skuld, så att den aldrig ackumuleras till en kris.

### Skilj reversibla från irreversibla beslut

Alla beslut förtjänar inte lika mycket övervägande. Reversibla "tvåvägsdörr"-beslut är lätta att ångra, så fatta dem snabbt och lokalt, av teamet, med en lutning mot handling. Att älta dem slösar tid och bromsar lärande. Irreversibla eller kostsamma att vända "envägsdörr"-beslut, ett publikt [API](https://en.wikipedia.org/wiki/API)-kontrakt, en datamodell i stor skala, ett fleråriga leverantörsåtagande, förtjänar långsamt, noggrant, seniort övervägande och en dokumenterad motivering. Att klassificera beslut på det här sättet är en av de mest hävstångsstarka styrningsvanor du har. Den riktar knapp granskning dit den lönar sig och frigör allt annat.

## Avvägningar: för- och nackdelar

| Styrningssätt | Fördelar | Nackdelar |
| --- | --- | --- |
| Central granskningsnämnd för allt | Maximal enhetlighet och insyn | Allvarlig flaskhals. Maktlöst för team. Långsamt |
| Upptrampad stig med lokal autonomi | Skalar, snabbt, säker standard, stärker team | Kräver plattformsinvestering i förväg. En del avvikelser från stigen |
| Full teamautonomi, ingen styrning | Snabbt, högt ägarskap | Fragmentering, dubbelarbete, upprepade misstag |
| ADR:er / RFC:er | Varaktigt minne, bättre beslut, transparens | Skrivoverhead. Ignoreras om de inte underhålls |

| Anskaffningsval | Fördelar | Nackdelar |
| --- | --- | --- |
| Bygg | Full kontroll, passar exakt, kan differentiera | Ständig underhålls- och bemanningskostnad |
| Köp | Snabbt, stött, någon annan underhåller | Licenskostnad, inlåsning, ofullkomlig passform |
| Anta (öppen källkod) | Ingen licensavgift, granskningsbar, community | Support- och säkerhetsbördan faller på dig |

Den förenande avvägningen är kontroll mot hastighet, och central enhetlighet mot lokal autonomi. Varje styrningsval ligger på det här spektrumet. Den rekommenderade hållningen, upptrampade stigar plus delegering utifrån återkallelighet, köper medvetet det mesta av autonomins hastighet och behåller den enhetlighet som spelar roll. Den gör det genom att göra det samstämmiga valet till det enkla och reservera tung process för det sällsynta irreversibla beslutet.

## Frågor att diskutera med ditt team

1. **Vem avgör om ett visst beslut är en envägsdörr, och hur fångar du felklassificeringar i båda riktningarna?** Att klassificera beslut efter återkallelighet är en av de mest hävstångsstarka styrningsvanorna, och dess värde rasar om du sätter fel etikett: behandlar du ett reversibelt val som irreversibelt dränker du det i övervägande, behandlar du ett irreversibelt som reversibelt levererar du en datamodell eller ett publikt API-kontrakt du inte billigt kan ångra. Den motstridiga risken är att personen närmast arbetet kan luta mot hastighet, medan en central nämnd kan luta mot försiktighet. Ta med konkreta exempel till diskussionen: vad skulle det faktiskt kosta, i tid och pengar, att vända varje beslut, och vem bär den kostnaden. I företags- och myndighetsmiljöer förvandlar upphandlingsåtaganden och data i stor skala många val till envägsdörrar som såg reversibla ut i förväg. Kom överens om vem som klassificerar, och bygg en vana av en snabb andra åsikt på allt nära gränsen, så att knapp granskning hamnar där en vändning är verkligt dyr.

2. **Vem äger, finansierar och bemannar den upptrampade stigen, och vad hindrar den från att förfalla till en grindvakt?** En upptrampad stig fungerar bara om de godkända standardvalen är verkligt väl stödda och enklare än alternativen, och det kräver ihållande investering som lätt blir underfinansierad. Avvägningen är skarp: en underresurssatt upptrampad stig blir en samling påbud utan stöd, vilket är precis den grindvaktning modellen var tänkt att ersätta, och team går då runt den. Ta med belägg för stigens hälsa: användningsgrad, hur aktuella de godkända verktygen är, hur snabbt plattformsteamet svarar och hur ofta team ansöker om att gå utanför stigen. För stora och reglerade organisationer är den upptrampade stigen också hur det regelföljande valet blir det enkla, så dess finansiering är en regelefterlevnadsinvestering, inte bara en bekvämlighet. Besluta om en tydlig ägare och en stående budget, och mät om team väljer stigen därför att den verkligen är den enklaste vägen.

3. **Var går team runt er styrning, och vad säger den skugg-IT:n er?** Team undviker den sanktionerade vägen när den är mer smärtsam än kringgåendet, så utbredd skugg-IT är mindre ett disciplinproblem än ett designutlåtande om er styrning. Hänsynen är verkliga: en del undvikande är hänsynslöst, och mycket av det är rationell flykt från en granskningsnämnd som blivit en kö på flera veckor. Ta med beläggen: vilka godkännanden som hoppas över, vilka inofficiella verktyg som i det tysta spridit sig och hur lång tid den officiella vägen faktiskt tar. I företags- och myndighetssammanhang är insatserna högre, eftersom osanktionerade verktyg kan bryta mot revisions-, säkerhets- och upphandlingsskyldigheter som har rättslig tyngd. Om mönstret visar att människor går runt en flaskhals är åtgärden att göra den upptrampade stigen snabbare och bredare och krympa nämndens omfattning till de få tvärgående, irreversibla besluten, inte att lägga till fler godkännanden.

4. **Hur stor del av vår leveranskapacitet går faktiskt till att betala av teknisk skuld, och kan vi namnge de högsta ränteposterna den bör ta först?** Teknisk skuld beter sig som ränta på ränta, en tyst skatt på varje framtida ändring, och en stor organisation kan bära den i åratal innan någon märker att systemet blivit långsamt och skört att ändra. Det motstridiga trycket är rakt: varje timme på skuld är en timme som inte läggs på funktioner ledningen kan se, så avbetalning är det första som skärs ned när en deadline krymper. Ta med verkliga belägg till diskussionen, en skriftlig förteckning över betydande skuld, en ärlig uppskattning av den löpande kostnad varje post medför och kostnaden för att åtgärda den, och den faktiska andel av den senaste kapaciteten som gick till avbetalning mot nytt arbete. För företag och myndigheter med tioåriga tidsperspektiv tvingar ohanterad skuld så småningom fram en kostsam omskrivning eller ett revisionsfynd, så behandla en stående avbetalningsallokering som riskhantering och besluta vem som vaktar den när scheman glider.

5. **När vi behöver resonemanget bakom ett beslut som fattades för två år sedan, kan vi faktiskt hitta det, och håller någon det registret vid liv?** Hela värdet av en arkitekturbeslutslogg är att resonemanget överlever de människor som fattade det, och det värdet rasar om ADR:er skrivs en gång, aldrig söks och i det tysta driver ur aktualitet. Spänningen ligger mellan den skrivdisciplin det kräver att fånga sammanhang, alternativ och konsekvenser i beslutsögonblicket och det dagliga trycket att bara leverera och gå vidare. Ta med konkreta tester till diskussionen: välj tre viktiga nyliga beslut och se om någon kan hitta den dokumenterade motiveringen på minuter, och kontrollera om ersatta ADR:er är markerade som sådana i stället för att tyst motsäga gällande praxis. I företags- och myndighetsmiljöer är det sökbara registret precis det försvarbara belägg revisorer och tillsynsorgan kräver, så besluta var ADR:er bor, vem som granskar dem och vad som gör ett beslut betydande nog att dokumentera.

6. **När öppnade vi senast ett större beslut om bygga eller köpa mot dess ursprungliga antaganden, och skulle vi ens märka när de antagandena löper ut?** Anskaffningsval är bland de dyraste och svåraste att vända beslut du fattar, och antagandena bakom dem (en leverantörs prissättning, din egen bemanning, mognaden hos ett öppen källkod-alternativ) blir i det tysta inaktuella medan beslutet står fastfruset. Hänsynen väger den sjunkna kostnaden och störningen av att byta mot den växande kostnaden för inlåsning, ofullkomlig passform eller en underhållsbörda du inte längre vill ha. Ta med den ursprungliga ADR:n och dess angivna antaganden, en aktuell TCO-uppskattning för varje väg inklusive licens, integration, bemanning och utträdeskostnad, och varje signal, en prisändring eller en nedgradering av support, att en premiss har förskjutits. För myndigheter och reglerade köpare gör upphandlingsregler och fleråriga avtal dessa envägsdörrar särskilt bindande, så kom överens i förväg om de utlösare och den takt som tvingar fram ett medvetet omtag i stället för en blind förnyelse.

## Sektorsperspektiv

**Startup.** Styr nästan ingenting och lita hårt på hastighet: för reversibla tvåvägsdörr-val, besluta vid skrivbordet och gå vidare. Reservera din enda styrningsvana för de få envägsdörrarna, en central datamodell eller en grundläggande leverantör, och fånga var och en i ett enda stycke så att en framtida kollega inte prövar frågan från noll igen. Hoppa över granskningsnämnder och upptrampade stigar helt, eftersom de i din storlek är overhead du inte har råd med och hela teamet redan delar sammanhanget.

**Småföretag.** Utan arkitekt i personalen, gör bygga-mot-köpa till din centrala styrningsfråga och besvara den utifrån total ägandekostnad snarare än preferens. Välj som standard att köpa eller anta väl stödda verktyg för allt som inte är din centrala differentierare, eftersom ständigt underhåll är den kostnad du har minst råd att bära. För en lätt beslutslogg så att resonemanget bakom dina få avgörande val överlever att en nyckelperson slutar.

**Storföretag.** Ditt problem är att balansera autonomi mot samstämmighet över många team, så investera i en finansierad upptrampad stig och reservera en snäv, snabb arkitekturgranskningsnämnd för de verkligt tvärgående och irreversibla besluten. Standardisera ADR:er så att resonemang blir sökbart institutionellt minne, och hantera teknisk skuld och anskaffningsval som portföljer med stående budgetar. Mät om team väljer stigen därför att den är enklast, och krymp varje nämnd som förfallit till en kö.

**Offentlig sektor.** Dokumenterade, försvarbara beslut är inte valfria här: revisorer och tillsynsorgan förväntar sig att se resonemanget, de alternativ som vägts och antagandena bakom varje avgörande val. Kör bygga-mot-köpa som en dokumenterad TCO-analys, respektera upphandlingsregler som begränsar inlåsning vid direktupphandling och behåll ADR:er som det revisionsklara beviskedjan. Ta de långa tidsperspektiven på allvar, eftersom en datamodell eller ett leverantörsåtagande som görs i dag kan binda organisationen i ett decennium, så klassificera det som en envägsdörr och överväg därefter.

## Exempel

**Startup.** En startup med fyra personer fattar de flesta beslut på minuter vid ett delat skrivbord, och för reversibla tvåvägsdörr-val är den hastigheten en verklig fördel, så de stretar emot all styrningsoverhead. Men när de väljer en databas och en datamodell som blir smärtsam att ändra senare (en envägsdörr) pausar de för att skriva en enstycksnotering: alternativen, valet och antagandena bakom det. Ett år senare, när de når skalningsgränser, räddar den enda noteringen dem från att pröva frågan från noll igen. De styr nästan ingenting och reserverar sin enda lätta vana för de få besluten som är verkligt kostsamma att vända.

**Storföretag.** Ett stort företags plattformsteam var förlamade av en arkitekturgranskningsnämnd som måste godkänna varje teknikval, vilket skapade köer på flera veckor. Företaget omstrukturerade styrningen kring en upptrampad stig: en kuraterad katalog över godkända, fullt stödda språk, datalager och pipelines som team kunde anta direkt. ADR:er dokumenterade varje beslut att avvika, och en snabb, rådgivande granskning hanterade bara val utanför stigen. Nämndens omfattning krympte till standardsättning och de få verkligt tvärgående besluten. Leveransen accelererade kraftigt. Enhetligheten förbättrades faktiskt, eftersom den enkla vägen nu var den regelföljande. Och ADR-arkivet gav organisationen ett sökbart register över varför saker byggts som de byggts.

**Offentlig sektor.** Ett statligt departement stod inför ett stort beslut om bygga eller köpa för en ärendehanteringsplattform under strikta upphandlings- och revisionsregler. I stället för att besluta utifrån preferens körde det en dokumenterad TCO-analys över tre alternativ: bygga skräddarsytt, köpa en kommersiell produkt och anta en öppen källkod-bas. Det vägde licens, integration, långsiktigt underhåll, bemanning och inlåsning, och dokumenterade beslutet och dess antaganden som en ADR. År senare, när en leverantörs villkor ändrades, öppnade departementet den ADR:n igen, fann att de ursprungliga antagandena inte längre höll och beslutade om med full kännedom om det tidigare resonemanget, och undvek därmed en blind och kostsam migrering. Den dokumenterade motiveringen var också precis det försvarbara belägg revisorerna krävde.

## Affärsnytta: motiv, ROI och TCO

Beslut är programvarans mest hävstångsstarka och minst synliga kostnad. Ett enda dåligt, irreversibelt arkitektur- eller anskaffningsval kan medföra år av släp eller en sanering på nio siffror. Att styra det väl, några timmars övervägande och ett skriftligt register, kostar nästan ingenting i jämförelse. Avkastningen på ADR:er och delegering utifrån återkallelighet kommer från två källor: att undvika dyra misstag på envägsdörr-besluten och att undvika bortslösat övervägande och omarbete på allt annat. Dokumenterad motivering sänker också den återkommande kostnaden för att pröva avgjorda frågor på nytt och för att team baklängeskonstruerar avsikten bakom ärvda system.

Teknisk skuld gör TCO-argumentet konkret. Ohanterad skuld beter sig precis som ränta på ränta: en växande skatt på varje framtida ändring, tills systemet blir i praktiken ounderhållbart och kräver en kostsam omskrivning. Att hantera skuld som en portfölj, med en stående kapacitetsallokering för att betala av högränteposterna, är långt billigare än den slutliga krisen. God styrning är billig att införa, mest disciplinen att skriva ner beslut och investeringen i förväg i en upptrampad stig. Att hoppa över den är dyrt: du betalar i undvikbara omskrivningar, inlåsningsöverraskningar, revisionsmisslyckanden och förlorat institutionellt minne. För att övertyga ledningen, rama in styrning på deras språk: riskminskning, undvikit omarbete, snabbare leverans via den upptrampade stigen och revisionsklar försvarbarhet. Visa att målet inte är mer process utan bättre riktad process, tung granskning bara där en vändning är kostsam och friktionsfri hastighet överallt annars.

## Antimönster och fallgropar

- Odokumenterade beslut: resonemang som försvinner i samma stund som de som fattade det lämnar.
- Godkännandenämnd som flaskhals: ett centralt organ som varje projekt måste köa bakom.
- Enhetsprocess: att tvinga triviala reversibla beslut genom tung granskning.
- Analysförlamning: att älta lätt reversibla tvåvägsdörr-beslut.
- [Skugg-IT](https://en.wikipedia.org/wiki/Shadow_IT): team som helt undviker styrning eftersom den sanktionerade vägen är för smärtsam.
- Osynlig teknisk skuld: skuld som aldrig förtecknas, aldrig betalas av och i det tysta ackumuleras.
- Bygg-allt- eller köp-allt-reflexer: anskaffning av vana snarare än TCO-analys.
- Styrningsteater: dokument och nämnder som finns för sken men inte formar beslut.

## Mognadsmodell

- Nivå 1 (Initiera): Beslut är ad hoc och odokumenterade. Styrning saknas eller är en genomgående flaskhals. Teknisk skuld är osynlig och resonemanget bakom val förångas när människor slutar.
- Nivå 2 (Utveckla): Vissa beslut dokumenteras och viss granskning finns, men praxis är inkonsekvent över team och processen är ofta illa anpassad till beslutets tyngd och återkallelighet.
- Nivå 3 (Standardisera): ADR:er, en upptrampad stig, delegering utifrån återkallelighet och en skuldförteckning är dokumenterade och upprätthålls i hela organisationen, så att det regelföljande valet är den enkla standarden och resonemang är sökbart.
- Nivå 4 (Hantera): Styrningen mäts mot utgångslägen: användning av den upptrampade stigen, ADR-täckning, beslutscykeltid, skuld som andel av kapaciteten och frekvensen av undantag utanför stigen följs, och beslut att betala av skuld eller ompröva anskaffning utlöses av det belägget snarare än av kris.
- Nivå 5 (Orkestrera): Styrningen trimmas kontinuerligt och är integrerad med leverans- och riskplanering. Granskningen riktas exakt mot irreversibla beslut, skuld och anskaffningsval omfördelas aktivt som portföljer och beslutas om på nytt utifrån belägg när omständigheterna förskjuts.

## Idéer för diskussion

- Kan vi för våra viktigaste nyliga beslut hitta det dokumenterade resonemanget bakom dem?
- Var är vår styrning en flaskhals, och var saknas den när den behövs?
- Vilka av våra nuvarande beslut är envägsdörrar, och behandlar vi dem så?
- Hur mycket av vår kapacitet går till att betala av teknisk skuld, och är det tillräckligt?
- Följer våra team den upptrampade stigen därför att den verkligen är den enklaste vägen, eller går de runt den?
- När omprövade vi senast ett större beslut om bygga eller köpa mot dess ursprungliga antaganden?

## Viktigaste punkter

- Dokumentera betydande beslut och deras motivering med ADR:er. Gör resonemanget varaktigt.
- Styr genom upptrampade stigar och standardval, inte grindvaktande fall för fall.
- Anpassa processens tyngd till beslutets tyngd och återkallelighet. Delegera tvåvägsdörrar, överväg noga envägsdörrar.
- Analysera bygga mot köpa mot anta utifrån total ägandekostnad, och dokumentera antagandena.
- Hantera teknisk skuld som en uttrycklig portfölj med en stående avbetalningsallokering.
- Håll styrningen transparent och lätt. Rikta knapp granskning mot det som är kostsamt att vända.

## Referenser och vidare läsning

- Michael Nygard, "Documenting Architecture Decisions" (the original ADR pattern)
- Gregor Hohpe, "The Software Architect Elevator" and "37 Things One Architect Knows"
- Amazon shareholder letters on Type 1 vs Type 2 (one-way vs two-way door) decisions
- Ward Cunningham, the original "technical debt" metaphor
- Martin Fowler, writings on technical debt and evolutionary architecture
- Neal Ford, Rebecca Parsons, Patrick Kua, "Building Evolutionary Architectures"
- Nicole Forsgren, Jez Humble, Gene Kim, "Accelerate" (loosely coupled architecture and autonomy)
- ISO/IEC/IEEE 42010 on architecture description
