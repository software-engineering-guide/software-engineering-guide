# 7.6 Realtidsdata och strömmande data

## Översikt och motivation

Det mesta du vet om datapipelines förutsätter att datan ligger still. Du samlar en dags poster, kör ett jobb över natten och läser resultaten på morgonen. Realtidsdata och strömmande data vänder på det antagandet. I stället för att bearbeta en färdig hög av data bearbetar du ett oändligt flöde av händelser när de anländer, och du producerar svar kontinuerligt. Det är skillnaden mellan [batchbearbetning](https://en.wikipedia.org/wiki/Batch_processing), som verkar på en avgränsad, komplett datamängd, och [strömbearbetning](https://en.wikipedia.org/wiki/Stream_processing), som verkar på ett obegränsat, aldrig avslutat flöde.

För stora team dyker strömning upp i samma ögonblick som latens börjar spela roll för verksamheten. Ett bedrägeribeslut som kommer en timme för sent är värdelöst. En personaliseringssignal som landar i morgon personaliserar ingenting. En operativ panel som ligger efter verkligheten ett skift vilseleder dem som bevakar den. Kapitel 7.2 (datateknik) argumenterar att du ska välja batch som standard och sträcka dig efter strömning bara där latens genuint lönar sig, och det här kapitlet tar dig resten av vägen: när realtid förtjänar sin kostnad och hur du bygger den utan att sätta eld på din driftbudget. Strömning ligger nära de händelsedrivna meddelandemönstren i kapitel 3.12 (händelsedriven arkitektur och meddelandehantering), lagringsvalen i kapitel 3.4 (dataarkitektur och lagring) och telemetripraxis i kapitel 9.2 (observerbarhet och telemetri).

Företags- och myndighetsmiljöer höjer insatserna. En bank poängsätter transaktioner för bedrägeri på den tid det tar en kortläsare att blinka. En trafikmyndighet följer fordon och förutsäger ankomster för miljontals resenärer. En bidragsmyndighet bevakar avvikelser i ansökningar samtidigt som den för ett granskningsbart register över varje beslut. I alla dessa kommer värdet av att agera på data medan den fortfarande är färsk, och risken kommer av att agera på data som är felaktig, ofullständig eller omöjlig att rekonstruera senare. Det här kapitlet har bestämda åsikter om båda.

## Nyckelprinciper

- Sträck dig efter strömning bara när latens har ett tydligt affärsvärde. Batch är billigare och enklare.
- Skilj avgränsad (ändlig) data från obegränsad (oändlig) data och designa därefter.
- Behandla händelsetid, inte ankomsttid, som sanningskälla och planera för sen och oordnad data.
- Fönster och vattenstämplar är hur du får ändliga svar ur oändliga strömmar.
- Föredra effektivt-en-gång-resultat genom idempotenta mottagare framför sköra exakt-en-gång-löften.
- Tillståndsbärande bearbetning behöver kontrollpunkter så att den kan återhämta sig utan att förlora eller dubbelräkna.
- Designa för mottryck och ombearbetning från dag ett, inte som en eftertanke.
- Håll strömningslogik observerbar och granskningsbar. En tyst ström är värre än ett fallerat batchjobb.

## Rekommendationer

### Motivera realtid innan du bygger den

Det viktigaste strömningsbeslutet är om du ska strömma alls. Realtid ungefär fördubblar din driftkomplexitet och kostnad, eftersom du byter ett jobb som kör och stannar mot ett system som måste vara friskt varje sekund. Innan du binder dig, namnge beslutet som färsk data möjliggör och kostnaden för att det beslutet anländer sent. Bedrägeripoängsättning, operativ larmning och personalisering i realtid klarar vanligen ribban. En panel som en människa tittar på två gånger om dagen gör det nästan aldrig, hur tillfredsställande "realtid" än låter på ett planeringsmöte. Skriv ner latenskravet som ett tal, i sekunder eller minuter, och kontrollera det mot verkligheten. Mycket av det människor kallar realtid tillgodoses väl av mikrobatchar som körs var några minuter till en bråkdel av kostnaden.

### Designa kring händelsetid, inte bearbetningstid

Den enskilt svåraste idén i strömning är att händelser inträffar vid ett ögonblick och bearbetas vid ett annat. Händelsetid är när saken faktiskt inträffade, till exempel när en resenär tryckte kortet. Bearbetningstid är när ditt system kom sig för att hantera den. De glider isär hela tiden: en telefon tappar signalen i en tunnel och laddar upp tre minuters tryck på en gång, ett nätverksproblem ordnar om meddelanden, en partition halkar efter. Om du beräknar på bearbetningstid vacklar dina tal med din infrastruktur snarare än att spegla världen. Det här problemet med sena och oordnade data är disciplinens hjärta, och det kopplar direkt till händelsemodelleringen i [händelsedriven arkitektur](https://en.wikipedia.org/wiki/Event-driven_architecture). Stämpla varje händelse med dess händelsetid vid källan, bär den tidsstämpeln genom hela pipelinen och beräkna dina resultat mot den.

### Använd fönster och vattenstämplar för att få ändliga svar

En obegränsad ström tar aldrig slut, så "räkna händelserna" har inget svar förrän du avgränsar den. Fönster gör den avgränsningen. Tumlande fönster hackar tiden i fasta, icke överlappande hinkar, till exempel varje minut. Glidande fönster överlappar, så ett femminutersfönster som avancerar varje minut ger dig en jämn rörlig siffra. Sessionsfönster grupperar skurar av aktivitet åtskilda av pauser, vilket passar användarsessioner väl. När du har fönster måste du avgöra när ett fönster är klart, eftersom sen data fortfarande kan anlända. En vattenstämpel är systemets uppskattning att det sannolikt har sett alla händelser upp till en given händelsetid. När vattenstämpeln passerar ett fönsters slut skickar du ut resultatet. Justera hur länge du väntar: håll fönster öppna längre och du tolererar mer försening på bekostnad av latens och minne, stäng dem fortare och du riskerar att tappa eftersläntrare. Avgör uttryckligen vad som händer med data som anländer efter att ett fönster stängts, om du släpper den, loggar den eller skickar ut en rättelse.

### Gör mottagare idempotenta och föredra effektivt-en-gång

Leveransgarantier låter enkla och är det inte. Minst-en-gång-leverans betyder att varje händelse bearbetas, men vissa kan bearbetas mer än en gång efter ett omförsök, så antal kan blåsas upp. Exakt-en-gång låter idealiskt men är dyrt och, tagen bokstavligt över godtyckliga externa system, ofta omöjligt. Det praktiska målet är effektivt-en-gång: det observerbara resultatet är som om varje händelse bearbetades en gång, även om maskineriet försökte om under ytan. Du kommer dit genom att göra dina [idempotenta](https://en.wikipedia.org/wiki/Idempotence) mottagare säkra att skriva till upprepade gånger, med deterministiska nycklar och upserts så att en omspelad händelse skriver över snarare än duplicerar. Kombinera minst-en-gång-leverans med idempotenta skrivningar och du får korrekta resultat utan att betala för tung transaktionell samordning överallt. Reservera äkta exakt-en-gång-maskineri för de snäva ställen som genuint behöver det.

### Sätt kontrollpunkter på tillståndsbärande bearbetning så att den kan återhämta sig

Många användbara strömningsberäkningar är tillståndsbärande: löpande antal, joins över strömmar, deduplicering, bedrägerimodeller som minns nyligt beteende. Det tillståndet lever i minnet och skulle försvinna när en process startar om. Kontrollpunkter tar periodvis en ögonblicksbild av tillståndet och strömpositionen tillsammans, så att systemet efter en krasch återupptar från en konsekvent punkt i stället för att spela om allt eller förlora sitt minne. Dimensionera ditt tillstånd medvetet, eftersom obegränsat tillstånd är ett vanligt sätt att köra slut på minne i ett strömningsjobb i produktion. Använd utgång och livslängd på tillstånd du inte längre behöver och övervaka tillståndsstorlek som ett förstklassigt mått. Återhämtningstid efter ett fel är en verklig servicenivåfråga, så testa den innan dina användare gör det.

### Strömma från operativa databaser med change data capture

Du vill ofta reagera på ändringar i en databas som aldrig designades för att sända ut händelser. [Change data capture](https://en.wikipedia.org/wiki/Change_data_capture) (CDC) löser detta genom att läsa databasens transaktionslogg och förvandla varje insert, update och delete till en ström av ändringshändelser. Det är långt bättre än att polla tabellen på en timer, vilket är långsamt, missar mellanliggande tillstånd och hamrar på källan. CDC låter dig hålla ett sökindex, en cache, ett analyslager eller en nedströmstjänst kontinuerligt synkroniserad med ett system i vilket sanningen finns, och gör det utan ingripande förändringar i applikationen. Behandla ändringsströmmen som en förstklassig dataprodukt: versionera dess schema, dokumentera dess betydelse och bevaka dess eftersläpning, eftersom allt nedströms ärver den eftersläpningen.

### Föredra en strömning-först-arkitektur framför att underhålla två kodbaser

Den klassiska [Lambda-arkitekturen](https://en.wikipedia.org/wiki/Lambda_architecture) kör ett batchlager för korrekt, komplett historik vid sidan av ett snabblager för färska, approximativa resultat och slår sedan ihop dem. Den fungerar, men den får dig att skriva och underhålla samma affärslogik två gånger, i två system, och avstämma skillnaderna för evigt. Kappa-arkitekturen kollapsar detta: håll en varaktig, omspelbar logg av händelser och kör all bearbetning som strömbearbetning, och bearbeta om historik genom att spela om loggen när logik ändras. Branschen har glidit mot den här strömning-först-formen eftersom en enda kodbas är dramatiskt billigare att underhålla och resonera om. Om du kan uttrycka dina batchbehov som omspelningar över en bevarad händelselogg undviker du tvåkodbasskatten helt. Använd loggbaserade mäklare som bevarar historik så att ombearbetning är en fråga om att spola tillbaka, inte bygga om.

### Exponera strömmar som SQL, materialiserade vyer och OLAP i realtid

Alla som behöver strömning ska inte behöva skriva lågnivåkod för strömbearbetning. Ström-SQL låter analytiker och ingenjörer uttrycka fönster, joins och aggregeringar i ett språk de redan kan, och håller resultaten kontinuerligt uppdaterade som materialiserade vyer. För analysfrågor med låg latens över färsk data inhämtar ett [OLAP](https://en.wikipedia.org/wiki/Online_analytical_processing)-lager (online analytical processing) i realtid strömmen och besvarar skiv-och-tärna-frågor på millisekunder, vilket är det som driver en genuint levande operativ panel. Para dessa med produktanalyspraxis i kapitel 7.4 (produktanalys och experimentering) när målet är snabb återkoppling på funktioner och experiment. Välj dessa verktyg på högre nivå där de passar och spara handskrivna strömprocessorer för logik de inte kan uttrycka.

### Planera för mottryck och ombearbetning från start

En ström kan anlända fortare än du kan bearbeta den. Mottryck är mekanismen som låter en långsam konsument signalera uppströms att sakta ner snarare än att falla över eller tyst tappa data. Se till att varje steg i din pipeline respekterar det och övervaka konsumenteftersläpning som ett rubrikmått, eftersom växande eftersläpning är den tidigaste varningen för att du förlorar loppet. Ombearbetning är den andra förmågan människor önskar att de hade byggt in. När du hittar en bugg eller ändrar en regel vill du spela om historik genom den rättade logiken. Det är bara möjligt om din händelselogg bevarar tillräckligt med historik och dina mottagare är idempotenta nog att absorbera omspelningen. Designa in båda från dag ett. Att eftermontera dem under incidenttryck är eländigt.

## Avvägningar: för- och nackdelar

| Val | Fördelar | Nackdelar | Bäst passform |
| --- | --- | --- | --- |
| Batch | Enkelt, billigt, lätt att testa och fylla på i efterhand | Hög latens, inaktuellt mellan körningar | Rapportering, det mesta av analys |
| Mikrobatch (minuter) | Nära realtid, långt enklare än strömning | Inte riktigt omedelbart | "Realtids"-paneler |
| Äkta strömning (under en sekund) | Omedelbar reaktion, kontinuerliga resultat | Komplext, kostsamt, svårt att testa | Bedrägeri, larmning, personalisering i realtid |
| Minst-en-gång + idempotent mottagare | Korrekta resultat, överkomligt, motståndskraftigt | Kräver disciplinerad nyckeldesign | De flesta strömningspipelines |
| Exakt-en-gång-maskineri | Stark garanti från början till slut | Dyrt, begränsat över system | Snäva vägar med höga insatser |
| Lambda (batch + snabb) | Korrekt historik plus färsk vy | Två kodbaser att underhålla | Äldre migreringar |
| Kappa (strömning först) | En kodbas, omspelbar | Kräver bevarad, varaktig logg | Nya strömningsplattformar |

Den centrala spänningen är latens mot komplexitet. Varje steg mot realtid kostar dig i driftbörda, testsvårighet och pengar, och avkastningen är inte linjär: att gå från dagligt till varje par minuter är billigt och ofta tillräckligt, medan att gå från minuter till under en sekund är där kostnaden koncentreras. Lös spänningen genom att prissätta beslutet, inte tekniken. Fråga vilken handling färskheten möjliggör och vad sen leverans kostar och köp sedan bara så mycket latensminskning som den handlingen motiverar. När du behöver strömning, lita på minst-en-gång-leverans med idempotenta mottagare och en strömning-först-logg, eftersom den kombinationen ger dig korrekthet och omspelbarhet utan de tyngsta garantierna.

## Frågor att diskutera med ditt team

1. **Vilket beslut möjliggör realtidsdata faktiskt för oss, och vad kostar det när den datan anländer en minut sent i stället för omedelbart?** Detta är frågan som bör grinda varje strömningsprojekt, eftersom strömning ungefär fördubblar er driftkostnad och komplexitet jämfört med batch. Ett stort team kan bränna kvartal på att bygga en realtidsplattform som betjänar paneler en människa kollar två gånger om dagen, vilket är pengar man bränner. Ta med den konkreta handling datan driver, vare sig det är att blockera en bedräglig transaktion, larma en operatör eller ändra vad en användare ser, och sätt ett tal på latensens kostnad för var och en. Om det ärliga svaret är att en femminuters mikrobatch skulle tillgodose behovet är det ett fynd värt att fira, inte gömma. Svaret bör direkt ändra om ni bygger äkta strömning, nöjer er med mikrobatchar eller stannar i batch.

2. **Hur hanterar vi sena och oordnade händelser, och vad händer med data som anländer efter att ett fönster stängts?** Sen och oordnad data är den svåra delen av strömning, och team som hoppar över den frågan upptäcker den i produktion när deras tal vägrar stämma av. De konkurrerande trycken är latens och korrekthet: håll fönster öppna längre för att fånga eftersläntrare och ni fördröjer varje resultat och förbrukar mer minne, stäng dem fortare och ni tappar tyst verklig data. Ta med belägg om hur sent er data faktiskt anländer, mätt som gapet mellan händelsetid och bearbetningstid över era källor, eftersom en mobil källa i tunnlar beter sig mycket annorlunda än en serversidehändelse. Avgör uttryckligen om sen data släpps, loggas eller utlöser en rättelse och se till att alla nedströms vet vilket. I ett myndighetssammanhang där siffror måste vara försvarbara kan tyst tappande av sena händelser vara ett regelefterlevnadsproblem, så policyn måste vara medveten och dokumenterad.

3. **Är våra mottagare idempotenta nog att vi säkert kan spela om historik, och bevarar vår händelselogg tillräckligt för att göra omspelning möjlig?** Ombearbetning är den förmåga team oftast önskar att de hade byggt in och oftast inte gjorde, och den beror på att två saker fungerar tillsammans: idempotenta mottagare som absorberar omspelade händelser utan att duplicera och en varaktig logg som bevarar tillräckligt med historik att spela om från. Utan båda betyder att rätta en logikbugg att ni inte rent kan räkna om den påverkade perioden, och ni sitter fast med att lappa tal för hand under tryck. Ta med ert nuvarande bevarandefönster och ett konkret test: välj en verklig bugg från senaste kvartalet och fråga om ni hade kunnat spela om den rättade logiken över den påverkade datan. Draget mot detta är kostnad, eftersom att bevara historik och designa idempotenta skrivningar tar lagring och disciplin i förväg. Men alternativet dyker upp i värsta möjliga ögonblick, under en incident, så svaret formar hur mycket ni investerar i omspelbarhet innan ni behöver den.

4. **När ett strömningsjobb kraschar, hur snabbt måste det återhämta sig, hur mycket tillstånd får det hålla, och har vi faktiskt tidtagit en återhämtning under produktionslast?** Ett batchjobb som dör kan köras om i morgon, men en alltid-på-ström som dör är ett pågående avbrott, och tillståndsbärande jobb som håller löpande antal, joins eller bedrägerimodeller kan förlora minuter av minne eller ta lång tid att ladda om tillstånd efter en omstart. För ett stort team är det här där en oglamorös detalj i tysthet sätter er verkliga tillgänglighet: obegränsat tillstånd växer tills ett jobb tar slut på minne, och en långsam återställning av kontrollpunkt förvandlar ett tio sekunders hack till ett tio minuters. De konkurrerande trycken är färskhet mot säkerhet, eftersom tätare kontrollpunkter förkortar återhämtningen men lägger till overhead, och generös tillståndsbevarande förbättrar noggrannheten men riskerar minnesutmattning. Ta med ett konkret mål för återhämtningstid, er nuvarande tillståndsstorlek och dess tillväxtkurva, ert kontrollpunktsintervall och resultaten av en verklig failover-övning snarare än en hoppfull uppskattning. I företags- och myndighetssammanhang där strömmen stöder bedrägeripoängsättning eller ett flöde för allmän säkerhet är en otestad återhämtningsväg en driftrisk ni har accepterat utan att mäta, så behandla övningen som ett krav, inte ett trevligt tillägg.

5. **Kör vi en strömning-först-kodbas eller ett separat batchlager och snabblager, och vad kostar det oss faktiskt att hålla de två avstämda?** Lambda-mönstret med ett batchlager för korrekt historik plus ett snabblager för färska resultat tvingar er att skriva samma affärslogik två gånger, i två system, och avstämma deras svar för evigt, medan en strömning-först-form (Kappa) håller en varaktig, omspelbar logg och kör all bearbetning som strömbearbetning. För en stor organisation är den duplicerade logiken där drift och omstridda tal föds, eftersom en regel ändras i ett lager och inte i det andra, och ingenjörer lägger verklig tid på att förklara varför de två är oense. Draget mot att behålla båda är tröghet och tryggheten i ett beprövat batchlager, så väg det mot underhållsskatten ärligt. Ta med listan över beräkningar ni kör på båda ställena i dag, de incidenter som orsakats av att de två lagren är oense och en bedömning av om er händelselogg bevarar tillräckligt med historik för att uttrycka batchbehov som omspelningar. I myndighets- och reviderade företagssammanhang är två lager som kan rapportera olika siffror för samma period i sig en regelefterlevnadsskuld, eftersom ni måste kunna säga vilket tal som är auktoritativt och varför.

6. **Vem driver det här alltid-på-systemet när det går sönder klockan tre på natten, och har vi budgeterat jourbördan och de specialistkunskaper det kräver, eller antar vi batchformad bemanning?** Strömning flyttar kostnad från bygge till drift: systemet måste vara friskt varje sekund, vilket betyder verklig jourtäckning, ingenjörer flytande i händelsetid, vattenstämplar, tillstånd och leveranssemantik och testning som är svårare än för ett jobb som kör och stannar. Team godkänner rutinmässigt en strömningsplattform på styrkan av dess förmågor och finansierar aldrig de människor som håller den vid liv, så plattformen försämras och förtroendet urholkas. Avvägningen är omfattning mot hållbarhet: varje ytterligare realtidspipeline är ännu en sak som kan larma någon, så frågan är om latensen den köper motiverar ett permanent driftåtagande. Ta med en ärlig inventering över vem som äger varje ström i produktion, er nuvarande jourrotation och dess marginal och var händelsetidskompetensen faktiskt sitter, vare sig det är en anställning, en partner eller en hanterad tjänst. För en offentlig myndighet eller ett stort företag, lägg till ledtider för upphandling och rekrytering och alla alternativ med hanterade tjänster, eftersom en realtidsplattform som beror på knapp kompetens ni inte kan rekrytera eller behålla är en plan för att köra ett avbrottsbenäget system underbemannat.

## Sektorsperspektiv

**Startup.** Strömning är sällan ditt första drag, och att sätta upp en tung plattform kan sänka ett litet team. Välj den enda signal som rör ditt kärnvärde, lägg händelser på en enda bevarande loggbaserad mäklare och kör en lättviktig processor med nyckelade, idempotenta mottagare så att ett minst-en-gång-omförsök aldrig dubbelräknar. Behåll några dagars historik så att du kan spela om genom rättad logik och föredra en hanterad strömningstjänst framför att driva ditt eget kluster, eftersom din knappaste resurs är ingenjörsuppmärksamhet.

**Småföretag.** Du har sannolikt ingen strömningsspecialist och ingen lust att driva alltid-på-infrastruktur, så behandla realtid som något du köper inuti verktyg du redan använder snarare än ett system du bemannar. Ramma in behovet som en latensfråga med ett tal bifogat, och i de flesta fall tillgodoses det av en mikrobatch som uppdateras var några minuter till en bråkdel av kostnaden och risken. Välj leverantörer vars realtidsfunktioner är transparenta om eftersläpning och lätta att falla tillbaka från och reservera skräddarsydd strömning för det sällsynta fall där färsk data direkt driver intäkter eller säkerhet.

**Storföretag.** Problemet är konsekvens och kostnad över många team: en gemensam loggbaserad plattform, en standardiserad policy för händelsetid och sen data och idempotenta mottagare så att grupper slutar uppfinna sköra pipelines på nytt. Budgetera alltid-på-driften och jourbördan uttryckligen, standardisera på en strömning-först-logg så att ni undviker en duplicerad batchkodbas och hantera strömmar som styrda dataprodukter med ägare, schemaversionering och övervakad eftersläpning snarare än en spridning av skräddarsydda jobb. Följ latens, återhämtningstid och kostnad per ström som portföljmått.

**Offentlig sektor.** Granskningsbarhet och offentlig ansvarsskyldighet formar varje val. Bevara varje bearbetad händelse i en varaktig logg så att siffror som rapporteras till tillsynsorgan, resandeantal, avvikelser i bidrag, bedrägeribeslut, kan rekonstrueras exakt, och gör policyn för sen data uttrycklig och dokumenterad snarare än att tyst tappa händelser. Upphandling bör kräva dataportabilitet och redovisning av en hanterad tjänsts leverans- och lagringsgarantier, och varje omräkning efter en regeländring bör vara en försvarbar omspelning genom rättad logik, inte en manuell lapp ingen kan spåra.

## Exempel

**Startup.** En konsumentapp vill visa användare ett levande aktivitetsflöde och flagga misstänkta inloggningar när de sker. Teamet motstår att sätta upp en tung strömningsplattform. De lägger händelser på en enda bevarande loggbaserad mäklare, kör en lättviktig strömprocessor för inloggningsrisklogiken och matar ett OLAP-lager i realtid som driver aktivitetsflödet. Varje mottagare är nyckelad och idempotent, så ett minst-en-gång-omförsök dubbelräknar aldrig. När de senare hittar en bugg i riskregeln spelar de helt enkelt om loggen genom den rättade logiken över natten, eftersom de behöll en veckas historik och aldrig behövde en andra batchkodbas.

**Storföretag.** En detaljhandelsbank poängsätter varje korttransaktion för bedrägeri inom auktoriseringsfönstret och joinar den levande transaktionsströmmen mot en tillståndsbärande modell av nyligt kontobeteende. Kontrollpunkter låter poängsättningstjänsten återhämta sig från en nodförlust på sekunder utan att förlora sitt minne av de senaste minuterna. Separat strömmar change data capture uppdateringar från kärnbankdatabasen till ett sökindex och en personaliseringstjänst och håller båda färska utan pollning. Operativa paneler läser från ett OLAP-lager i realtid så att risk- och driftteam bevakar verksamheten medan den rör sig, och hela pipelinen sänder ut den eftersläpnings- och genomströmningstelemetri som beskrivs i kapitel 9.2.

**Offentlig sektor.** En storstads trafikmyndighet inhämtar fordonspositioner och biljetttryck för att förutsäga ankomster och övervaka trängsel i realtid, och matar både publika appar och ett driftcentrum. Eftersom resenärer i tunnlar laddar upp tryck i försenade skurar beräknar teamet resandeantal på händelsetid med vattenstämplar justerade efter den observerade förseningen och loggar varje händelse som anländer efter att dess fönster stängts i stället för att tyst tappa den. Varje bearbetad händelse bevaras i en granskningsbar logg så att resandesiffror som rapporteras till tillsynsorgan kan rekonstrueras exakt. När en biljettregel ändras spelar de om den påverkade perioden genom den rättade logiken och producerar en försvarbar omräkning.

## Affärsnytta: motiv, ROI och TCO

Avkastningen på realtidsdata kommer av att agera medan handling fortfarande spelar roll. Bedrägeri som fångas under auktorisering förhindrar en förlust som en nattlig batch bara skulle rapportera. Personalisering som svarar inom en session höjer konvertering på ett sätt morgondagens rekommendation inte kan. Operativ övervakning som speglar nuet låter er ingripa innan ett litet problem blir ett avbrott eller en offentlig incident. I varje fall är värdet deltat mellan att agera nu och att agera senare, och det deltat är vad ni bör kvantifiera när ni driver ärendet.

Den totala ägandekostnaden är högre än för batch, och ärlighet om det skyddar din trovärdighet. Du betalar för alltid-på-infrastruktur, för ingenjörer som förstår händelsetid, vattenstämplar, tillstånd och leveranssemantik och för den svårare testningen och jourbördan hos ett system som måste vara friskt kontinuerligt snarare än köra och stanna. En strömning-först-arkitektur på en bevarad logg sänker den löpande kostnaden genom att spara er en duplicerad batchkodbas, och att välja minst-en-gång med idempotenta mottagare undviker utgiften för exakt-en-gång-maskineri från början till slut. Det dyraste misstaget är att bygga realtid där mikrobatch eller batch skulle räcka, så det starkaste kostnadsargumentet är ofta ett beslut att inte strömma. Ramma in pitchen till ledningen kring specifika latenskänsliga beslut och deras mätbara utdelning och var lika tydlig om var att stanna i batch sparar pengar utan förlust av värde.

## Antimönster och fallgropar

- Att bygga strömning av prestige när en mikrobatch var några minuter skulle tillgodose behovet.
- Att beräkna på bearbetningstid, så att dina tal vacklar med din infrastruktur i stället för med världen.
- Att ignorera sen och oordnad data tills avstämningen fallerar i produktion.
- Att jaga bokstavlig exakt-en-gång överallt i stället för minst-en-gång med idempotenta mottagare.
- Obegränsat tillstånd utan utgång, som i tysthet växer tills ett jobb tar slut på minne.
- Inga kontrollpunkter, så en omstart förlorar tillstånd eller tvingar en full omspelning.
- Att polla operativa databaser på en timer i stället för att använda change data capture.
- Att underhålla ett Lambda-batchlager och snabblager med duplicerad, driftande logik.
- Ett bevarandefönster för kort för att spela om historik när du hittar en bugg.
- Strömmar utan mått för eftersläpning, genomströmning eller färskhet, som fallerar tyst.

## Mognadsmodell

- **Nivå 1, Initiera:** Allt är batch, eller några handbyggda strömningsjobb körs reaktivt utan övervakning. Tal beräknas på bearbetningstid, sen data ignoreras och en omstart förlorar tillstånd. Ingen kan spela om historik för att rätta en bugg, och problem upptäcks när nedströmssiffror vägrar stämma av.
- **Nivå 2, Utveckla:** Vissa team kör centrala strömningspipelines på en loggbaserad mäklare med kontrollpunkter, och de skiljer händelsetid från bearbetningstid och använder grundläggande fönster. Praxis är inkonsekvent från team till team: leveransen är minst-en-gång men inte alla mottagare är idempotenta, hanteringen av sen data är improviserad och eftersläpning bevakas informellt snarare än larmas på.
- **Nivå 3, Standardisera:** Händelsetid, vattenstämplar och en uttrycklig policy för sen data är dokumenterade och tillämpade i hela organisationen. Mottagare är idempotenta för effektivt-en-gång-resultat, tillstånd har utgång och change data capture matar nedströmssystem som konvention. En bevarad logg stöder omspelning, och eftersläpning, genomströmning och färskhet övervakas med larm som en standard för hela organisationen snarare än en vana per team.
- **Nivå 4, Hantera:** Strömningsegendomen mäts och styrs mot utgångslägen. Varje pipeline bär servicenivåmål för latens från början till slut, konsumenteftersläpning, återhämtningstid, skev händelsetid, andel sena händelser, tillståndsstorlek och kostnad per miljon händelser, alla följda mot överenskomna mål och larmande vid regression. Återhämtning övas och tidtas snarare än antas, mottryckets marginal och tillståndstillväxt bevakas som kapacitetssignaler och en ny ström måste klara dessa mått innan den går i produktion.
- **Nivå 5, Orkestrera:** En strömning-först-arkitektur betjänar både färska och historiska behov från en omspelbar logg, och ström-SQL, materialiserade vyer och OLAP i realtid gör färsk data brett tillgänglig. Ombearbetning är rutin och testad, plattformen autoskalar och balanserar om mot uppmätt last och kostnad, och strömmar avvecklas, omdefinieras eller ersätts på belägg. Strömning är integrerad med affärs- och riskplanering, och varje ström är observerbar och granskningsbar från början till slut när last- och kostnadsbilden skiftar.

## Idéer för diskussion

1. Var i er stack förtjänar "realtid" faktiskt sin kostnad, och var är det en ogranskad önskan?
2. Hur stort är gapet mellan händelsetid och bearbetningstid över era källor, och mäter ni det?
3. Kunde ni kollapsa en Lambda-uppsättning med batch och snabblager till en enda strömning-först-kodbas, och vad skulle hindra det?
4. Vilka av era mottagare är genuint idempotenta, och kunde ni säkert spela om förra kvartalets data genom rättad logik i dag?
5. Vad är er policy för data som anländer efter att ett fönster stängts, och vet alla nedströms om den?
6. Hur skulle change data capture ändra sättet ni håller sök, cacher och analys synkroniserade?

## Viktigaste punkter

- Sträck dig efter strömning bara när ett latenskänsligt beslut betalar för det. Batch och mikrobatch är billigare standardval.
- Beräkna på händelsetid och behandla sen och oordnad data som kärnproblemet, hanterat med fönster och vattenstämplar.
- Föredra minst-en-gång-leverans med idempotenta mottagare för effektivt-en-gång-resultat framför bokstavlig exakt-en-gång överallt.
- Sätt kontrollpunkter på tillståndsbärande bearbetning, begränsa ditt tillstånd och övervaka konsumenteftersläpning som ett rubrikmått.
- Använd change data capture för att strömma från operativa databaser i stället för att polla.
- Föredra en strömning-först-arkitektur på en bevarad, omspelbar logg framför att underhålla två kodbaser.
- Exponera strömmar genom ström-SQL, materialiserade vyer och OLAP i realtid och håll varje ström observerbar och granskningsbar.

## Referenser och vidare läsning

- Tyler Akidau, Slava Chernyak, and Reuven Lax, "Streaming Systems."
- Martin Kleppmann, "Designing Data-Intensive Applications."
- Nathan Marz and James Warren, "Big Data" (Lambda architecture).
- Jay Kreps, "Questioning the Lambda Architecture" (O'Reilly Radar).
- Fabian Hueske and Vasiliki Kalavri, "Stream Processing with Apache Flink."
- Ben Stopford, "Designing Event-Driven Systems."
- Tyler Akidau and colleagues, "The Dataflow Model" (VLDB paper on windowing and watermarks).
