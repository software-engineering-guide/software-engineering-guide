# 6.7 AI-agenter och agentiska system

## Översikt och motivation

En **AI-agent** är en [stor språkmodell](https://en.wikipedia.org/wiki/Large_language_model) (LLM) inlindad i en loop: den får ett mål, den kan anropa verktyg, den håller visst minne av vad den har gjort och den avgör själv sitt nästa steg tills målet är nått eller den ger upp. Den loopen är hela skillnaden mellan en agent och de enkla prompt-svar-anropen i kapitel 6.3. Ett enda anrop besvarar en fråga. En agent läser sin e-post, söker i en databas, skapar ett ärende, kontrollerar resultatet och försöker igen. Modellen producerar inte längre bara text. Den väljer åtgärder i era system.

Det skiftet ändrar ingenjörsproblemet. När en modell bara skriver ord är en dålig utdata en dålig mening. När en modell styr verktyg kan en dålig utdata skicka ett felaktigt meddelande, radera en post eller flytta pengar. Så en [intelligent agent](https://en.wikipedia.org/wiki/Intelligent_agent) förstås bäst som en opålitlig planerare inuti ett betrott system, och det mesta av ert arbete går åt till att begränsa vad den planeraren får göra. Det här kapitlet bygger direkt på LLM-grunderna i kapitel 6.3, tillits- och ansvarsfrågorna i kapitel 6.5 och plattformspraxis i kapitel 6.6.

För stora team är insatserna lika mycket organisatoriska som tekniska. Företag vill ha agenter kopplade till verkliga interna system (ärendehantering, ekonomi, kundregister), vilket betyder att agenter ärver verkliga åtkomstkontroller och verkliga skyldigheter kring ändringshantering. Myndigheter lägger till offentlig ansvarsskyldighet: en autonom åtgärd som påverkar en medborgare måste vara förklarbar, överskådlig och granskningsbar i efterhand. Mönstret är kraftfullt. Driftsatt utan disciplin är det ett snabbt sätt att automatisera misstag.

## Nyckelprinciper

- En agent är en modell plus en loop, verktyg, minne och ett mål. Risken bor i loopen, inte i prosan.
- Begränsa autonomin till uppgiften. Ge den minsta frihet som får jobbet gjort.
- Föredra ett fast arbetsflöde när stegen är kända. Sträck dig efter öppen autonomi först när de inte är det.
- Behandla varje verktyg som angreppsyta och ge det den minsta behörighet det kan fungera med.
- Sätt en människa i loopen för konsekvensfulla eller oåterkalleliga åtgärder och gör återställning billig.
- Utvärdera på uppgiftsframgång, inte på hur transkriptet läses.
- Spåra varje körning. En åtgärd ni inte kan rekonstruera är en åtgärd ni inte kan styra.
- Den enklaste design som fungerar är vanligen den rätta. Ofta är det inte en agent alls.

## Rekommendationer

### Börja med ett arbetsflöde, lägg till autonomi bara där du måste

Det vanligaste misstaget är att sträcka sig efter en autonom agent när en fast pipeline skulle duga. Om ni redan känner stegen (extrahera fält, validera dem, slå upp en post, utforma ett svar), skriv det som ett orkestrerat arbetsflöde där modellen fyller specifika platser. Autonomi förtjänar sin plats när vägen genuint inte kan förutbestämmas, till exempel öppen forskning eller triage över många möjliga verktyg. Begränsa autonomin till uppgiften: sätt tak på antalet steg, begränsa verktygsuppsättningen till vad det här målet behöver och sätt ett tydligt stoppvillkor. En god regel är att ge modellen exakt så mycket frihet som problemet kräver och inte en grad mer.

### Gör verktygsanvändning till kärnförmågan och gör den säker

Verktygsanvändning (även kallad funktionsanrop) är det som förvandlar en modell till en agent. Definiera varje verktyg med ett precist schema, validera varje argument modellen levererar och tillämpa [principen om minsta behörighet](https://en.wikipedia.org/wiki/Principle_of_least_privilege): en skrivskyddad rapporteringsagent får skrivskyddade uppgifter, aldrig skrivåtkomst den kunde missbruka. Kör verktyg inuti en [sandlåda](https://en.wikipedia.org/wiki/Sandbox_(computer_security)) så att ett dåligt anrop inte kan nå bortom sin sprängradie. Föredra många snäva verktyg för ett enda syfte framför några få breda, eftersom ett snävt verktyg är lättare att resonera om, ge behörigheter och granska. Det är samma återhållsamhet kapitel 6.3 uppmanar till för LLM-verktygsanvändning, gjord central.

### Använd uttryckliga resonemangs- och planeringsmönster

Agenter fungerar bättre när deras tänkande är strukturerat. I ett mönster med resonera-och-agera (populariserat av ReAct-forskningen) alternerar modellen mellan att resonera om situationen och vidta en åtgärd, och observerar sedan resultatet innan den resonerar igen. För svårare mål, låt modellen planera först (dela upp i deluppgifter) och sedan utföra, så att ni kan inspektera och till och med godkänna planen innan något verktyg körs. Håll dessa loopar observerbara och avbrytbara. En plan du kan läsa är en plan du kan stoppa.

### Behåll människor i loopen för konsekvensfulla åtgärder

Besluta, per verktyg och per åtgärd, om modellen får agera ensam eller måste fråga först. Reversibla åtgärder med låga insatser (sökning, utformning) kan köras obevakat. Konsekvensfulla eller oåterkalleliga (att skicka extern kommunikation, flytta pengar, ändra produktionsdata, avgöra en medborgares ärende) behöver en [människa-i-loopen](https://en.wikipedia.org/wiki/Human-in-the-loop)-grind med verklig befogenhet att säga nej. Designa för reversibilitet där ni kan: föredra att iscensätta en ändring framför att checka in den och gör ångra till en förstklassig funktion så att en felaktig åtgärd kostar minuter, inte en incident.

### Behandla säkerhetsmodellen som motståndarmässig

Agenter vidgar angreppsytan som beskrivs i kapitel 4.2. Det främsta hotet är [promptinjektion](https://en.wikipedia.org/wiki/Prompt_injection): skadliga instruktioner gömda i en webbsida, ett dokument eller ett e-postmeddelande som agenten läser och lyder. Närbesläktat är [problemet med den förvirrade delegaten](https://en.wikipedia.org/wiki/Confused_deputy_problem) (confused deputy), där en angripare lurar en privilegierad agent att missbruka sin egen legitima åtkomst, till exempel genom att exfiltrera data via ett verktyg agenten får anropa. Anta att allt innehåll agenten tar in kan vara fientligt. Skilj betrodda instruktioner från opålitlig data, begränsa verktyg så att en kapad agent inte kan nå känsliga system och låt aldrig rå modellutdata utlösa en oåterkallelig åtgärd utan validering.

### Utvärdera på uppgiftsframgång och regressionstesta icke-determinismen

Bedöm agenter efter om de utför uppgiften, inte efter om transkriptet låter smart. Bygg en utvärderingsmängd av representativa mål med kontrollerbara framgångskriterier (fick ärendet rätt prioritet, matchade återbetalningen policyn) och kör den vid varje prompt-, modell- eller verktygsändring. Eftersom agenter är icke-deterministiska bevisar en enda körning lite: kör varje fall flera gånger och följ en framgångsfrekvens, inte godkänd eller underkänd. Det utvidgar disciplinen kring offline- och onlineutvärdering i kapitel 6.3 och 6.2 (maskininlärningsteknik och MLOps) till system vars utdata är en sekvens av åtgärder.

### Instrumentera körningar för observerbarhet, kostnad och felhantering

Du kan inte styra det du inte kan se. Spåra varje agentkörning från början till slut (kapitel 6.6): målet, varje resonemangssteg, varje verktygsanrop med dess argument och resultat, de tokens som gått åt och det slutliga utfallet. Den spårningen är er felsökare, ert revisionsspår och er kostnadsmätare på en gång. Sätt hårda budgetar på steg, tid och utgifter, eftersom en agent som loopar kan bränna latens och pengar snabbt. Hantera fel uttryckligen: gör om tillfälliga verktygsfel med backoff, men upptäck loopar där modellen upprepar en misslyckad åtgärd och fallera säkert snarare än att pulsa.

## Avvägningar: för- och nackdelar

| Val | Fördelar | Nackdelar | Bäst när |
|---|---|---|---|
| Fast arbetsflöde (modellen fyller platser) | Förutsägbart, billigt, lätt att testa och granska | Stelt. Går sönder på oförutsedda vägar | Stegen är kända i förväg |
| Autonom enskild agent | Flexibel. Hanterar öppna mål | Svårare att kontrollera, utvärdera och begränsa | Vägen kan inte förutbestämmas |
| Orkestrering med flera agenter | Parallellism. Specialiserade roller | Samordningskostnad, ackumulerande fel, högre utgifter | En uppgift verkligen delas i oberoende delar |
| Obevakad åtgärd | Snabb, låg friktion | Misstag utförs utan kontroll | Åtgärder är reversibla och har låga insatser |
| Människa-i-loopen-grind | Säkerhet, ansvarsskyldighet, reversibilitet | Långsammare. Behöver granskarkapacitet | Åtgärder är konsekvensfulla eller oåterkalleliga |

Den centrala spänningen är autonomi mot kontroll. Mer autonomi hanterar fler situationer men kräver fler skyddsräcken, mer utvärdering och mer pengar, och den fallerar på sätt som är svårare att förutsäga. Designer med flera agenter lockar team med elegans, men varje ytterligare agent lägger till samordningsoverhead och ytterligare ett ställe där ett litet fel kan ackumuleras till ett felaktigt resultat. Lös spänningen genom att börja med den minsta autonomi som löser problemet och lägga till frihet först när en konkret uppgift tvingar er, alltid parad med ett matchande skyddsräcke.

## Frågor att diskutera med ditt team

1. **Behöver den här funktionen verkligen en agent, eller vore ett fast arbetsflöde säkrare och billigare?** Autonomi är förledande, men de flesta jobb har kända steg som en orkestrerad pipeline hanterar med långt mindre risk. För ett stort team betyder en standard av agenter att varje grupp tar på sig utvärderings-, spårnings- och säkerhetsbördor som en enklare design skulle undvika. Ta med den specifika uppgiften och fråga om dess steg kan förutbestämmas. Om de kan är en agent sannolikt överkonstruktion. Reservera öppen autonomi för mål där vägen genuint varierar per fall. Svaret bör knuffa de flesta funktioner mot ett arbetsflöde och lämna en liten, medveten mängd som äkta agenter.

2. **För varje verktyg vår agent kan anropa, vad är det värsta en kapad agent kunde göra med det, och vad stoppar det?** Promptinjektion och attacker med förvirrad delegat vänder agentens egen legitima åtkomst mot er, så den rätta linsen är motståndarmässig (kapitel 4.2). Inventera varje verktyg, dess behörighetsomfång och om en skadlig instruktion smugglad genom inhämtat innehåll kunde nå det. För företag som kopplar agenter till interna system är det här där minsta behörighet, sandlådor och mänskliga grindar på oåterkalleliga åtgärder blir verkliga. Ta med listan över verktyg och de uppgifter var och en håller. Om någon konsekvensfull åtgärd är nåbar utan validering eller en mänsklig kontroll är det det första att rätta.

3. **Hur skulle vi veta att en agents framgångsfrekvens sjönk, med tanke på att varje körning ser trovärdig ut?** Agenter är icke-deterministiska, så ett transkript som läses väl kan ändå ha vidtagit fel åtgärd, och en grön körning bevisar ingenting. Fråga om ni har en utvärderingsmängd av mål med kontrollerbara utfall, körd många gånger per fall för att producera en framgångsfrekvens snarare än en enda godkänd. För driftsättningar med höga insatser eller publika, diskutera hur körningsspår låter er rekonstruera exakt vad som hände när något går fel (kapitel 6.5 och 6.6). Om er enda signal är användarklagomål är ni redan för sena. Svaret bör finansiera en utvärderingssele före skalning, inte efter en incident.

4. **Vilka av den här agentens åtgärder är verkligen oåterkalleliga, vem har befogenhet att godkänna dem och har vi granskarkapaciteten att bemanna den grinden?** Frestelsen är att låta modellen agera obevakat överallt, men en mänsklig grind är bara verklig om en namngiven person med befogenhet att säga nej är tillgänglig när agenten frågar. För ett stort team blir en godkännandekö ingen äger i tysthet en gummistämpel, och den säkerhet ni designade förångas under volym. Ta med hela listan över åtgärder agenten kan vidta, markera var och en som reversibel eller oåterkallelig och uppskatta den dagliga volymen av fall med låg säkerhet som skulle landa hos en granskare. Väg friktionen och bemanningskostnaden för en grind mot sprängradien av ett obevakat misstag och föredra att omdesigna en oåterkallelig åtgärd till en iscensatt, ångringsbar framför att lägga till ännu en granskare. I företags- och myndighetssammanhang, knyt varje konsekvensfull åtgärd till en ansvarig tjänsteman och ett ändringshanteringsregister, eftersom en autonom åtgärd som påverkar en medborgare eller en kund som ingen människa godkände är exakt det fel en revision hittar.

5. **Sträcker vi oss efter en design med flera agenter för att uppgiften genuint delas upp, eller för att den ser elegant ut?** Att dela arbete över specialiserade agenter är förledande, men varje extra agent lägger till samordningsoverhead och ytterligare ett ställe där ett litet fel ackumuleras till ett felaktigt resultat. För en stor organisation är kostnaden inte bara utgifter och latens: ett system med flera agenter är långt svårare att spåra, utvärdera och resonera om när det fallerar, så styrningsbördan multipliceras med varje roll ni lägger till. Ta med uppgiften och visa konkret vilka delar som körs oberoende och parallellt och jämför sedan den uppmätta framgångsfrekvensen och kostnaden för en version med flera agenter mot en enskild agent på samma utvärderingsmängd. Om den enskilda agenten vinner eller är jämbördig är den eleganta designen överkonstruktion. För reglerade eller offentliga driftsättningar, kom ihåg att varje agent i kedjan är ytterligare en komponent ett tillsynsorgan måste kunna inspektera, så tillagd struktur ni inte kan motivera är tillagd skuld.

6. **Vilka är de hårda budgetarna för en agents steg, tid och utgifter, och hur skulle en loopande agent fångas innan den driver upp kostnad eller latens?** En agent som upprepar en misslyckad åtgärd kan bränna pengar och tid utan förvarning, så obegränsad autonomi är en finansiell risk lika mycket som en säkerhetsrisk. För ett stort team som kör många agenter kan en enda felbeteende loop spränga en molnräkning eller uttömma en hastighetsgräns som svälter varje annan arbetslast, vilket gör tak per körning till en gemensam driftfråga snarare än ett teams problem. Ta med de nuvarande steg-, tid- och tokenbudgetarna för varje agent, larmen som utlöses när en körning överskrider dem och loopdetekteringen som fallerar säkert snarare än pulsar. Väg snäva budgetar, som kan skära av en legitimt svår uppgift, mot lösa som låter kostnaden skena. I företags- och myndighetssammanhang där utgifter måste prognostiseras och motiveras är en agent vars kostnad är obegränsad en post ni inte kan försvara i en budgetgranskning eller en revision.

## Sektorsperspektiv

**Startup.** Leverera en snäv agent som rör ditt kärnvärde, på en hostad modell, med den minsta verktygsuppsättning som gör jobbet och ett hårt tak på steg och utgifter. Stå emot demonstrationen med flera agenter: din knappa utvecklingsuppmärksamhet är bättre använd på att begränsa en enskild agents autonomi och spåra dess körningar än på att samordna roller du inte kan underhålla. Håll varje konsekvensfull åtgärd bakom en enda grind "utforma, skicka aldrig" så att ett misstag kostar ett klick att ångra, inte en incident.

**Småföretag.** Du har ingen som kan köra en utvärderingssele eller en sandlåda, så föredra agenter inbäddade i verktyg du redan litar på och slå bara på den autonomi du kan övervaka med blotta ögat. Behandla varje agent som kan skicka, betala eller radera för din räkning som något att hålla avstängt tills en person bekräftar varje åtgärd, eftersom ett felaktigt automatiskt meddelande till en kund kostar dig relationen. Föredra leverantörer som visar dig vad agenten gjorde och låter dig stänga av automationen.

**Storföretag.** Problemet är att styra agenter över många team: gemensamma mönster för att begränsa autonomi, verktygsuppgifter med minsta behörighet, sandlådor, människa-i-loopen-grindar och spårning från början till slut så att ingen grupp uppfinner skyddsräckena på nytt. Koppla agenter till interna system under samma åtkomstkontroller en människa skulle ha, grinda oåterkalleliga åtgärder bakom namngivna godkännare och ändringshantering och hantera portföljen med mått på framgångsfrekvens, budgetar per körning och motståndsmässig injektionstestning. Standardisera spårnings- och utvärderingslagret så att vilken agents beteende som helst kan rekonstrueras och granskas.

**Offentlig sektor.** Upphandling, transparens och offentlig ansvarsskyldighet begränsar varje val. Håll agenter till att samla fakta och utforma, och reservera varje beslut som påverkar en medborgare för en ansvarig människa, eftersom ansvar för ett offentligt beslut inte kan delegeras till en modell. Logga varje körning så att ett tillsynsorgan kan se vilka källor som konsulterades och vad som gjordes, kräv att leverantörer redovisar agentens verktyg och begränsningar och bevisa genom en motståndsutvärderingsmängd att agenten vägrar agera utöver sitt avgränsade uppdrag.

## Exempel

**Startup.** En analysstartup på fem personer bygger en triageagent för support. Den läser ett inkommande ärende, söker i dokumenten och antingen utformar ett svar eller dirigerar ärendet till en människa, och det är hela verktygsuppsättningen. Uppgifterna är skrivskyddade plus en enda åtgärd "skapa utkast" som aldrig skickar utan att en person klickar på skicka. Varje körning spåras så att grundarna kan se varför ett ärende dirigerades dit det gjorde, och en nattlig utvärderingsmängd av femtio verkliga ärenden kör agenten fem gånger vardera för att följa en dirigeringsnoggrannhet. När en konkurrents klyftiga demonstration med flera agenter lockar dem stannar de på en enskild agent eftersom deras uppgift inte delas upp.

**Storföretag.** En bank bygger en agent för att hjälpa driftpersonal att stämma av misslyckade betalningar. Den integreras med interna system under samma åtkomstkontroller en mänsklig tjänsteman har, beviljade genom tjänsteuppgifter med minsta behörighet avgränsade till avstämning enbart. Agenten får undersöka fritt (läsa huvudböcker, söka transaktionshistorik) men varje åtgärd som flyttar pengar eller redigerar en post iscensätts och kräver en namngiven mänsklig godkännare, vilket uppfyller ändringshantering. Inhämtade dokument behandlas som opålitliga för att trubba av promptinjektion, verktyg körs i sandlåda och varje körning spåras från början till slut för revision. En offlineutvärderingsmängd grindar varje modell- eller promptändring, och budgetar per körning sätter tak på steg och utgifter så att en loopande agent inte kan driva upp kostnad eller latens.

**Offentlig sektor.** En bidragsmyndighet pilotkör en agent för att hjälpa handläggare att sammanställa fakta för ett anspråk: hämta register, kontrollera berättigaanderegler och utforma en sammanfattning. Myndigheten drar en hård gräns: agenten samlar och utformar, men en mänsklig handläggare fattar och äger varje beslut som påverkar en medborgare, eftersom ansvar för offentliga beslut inte kan delegeras till en modell (kapitel 6.5). Varje körning loggas fullständigt och visar vilka källor som konsulterades och vad som utformades, så att ett tillsynsorgan kan granska vilket ärende som helst. Autonomin är medvetet begränsad till läs-och-utforma, verktyg har minsta behörighet och körs i sandlåda och en motståndsutvärderingsmängd bekräftar att agenten vägrar agera utöver att samla fakta.

## Affärsnytta: motiv, ROI och TCO

Agenter levererar avkastning genom att automatisera arbete i flera steg som tidigare behövde en person som klickade mellan system: triage, avstämning, forskning och rutindrift. Värdet syns som arbete slutfört utan en människa i varje steg, snabbare cykeltider och personal frigjord för omdömestunga uppgifter. Eftersom agenter bygger på befintliga LLM och verktyg är tiden till en fungerande prototyp kort, vilket är exakt varför team överbygger.

Den totala ägandekostnaden är där agenter skiljer sig från vanliga LLM-funktioner. Utöver inferenskostnad betalar ni för verktygsintegrationer, sandlådor och behörighetsrörmokeri, utvärderingsselen, spårnings- och observerbarhetsstacken (kapitel 6.6) och de mänskliga granskare som bemannar godkännandegrindarna. En loopande eller dåligt begränsad agent lägger till en rörlig kostnad som kan spika utan förvarning, så budgetar på steg och utgifter är en del av designen, inte en eftertanke. Kostnaden för att inte anta är långsammare drift och manuellt slit era konkurrenter automatiserar. Kostnaden för att anta vårdslöst är en autonom åtgärd som skickar fel meddelande, läcker data eller fattar ett oansvarigt beslut. Driv ärendet inför ledningen genom att para ett konkret automationsmål med en konkret plan för skyddsräcken, utvärdering och mänsklig tillsyn, och genom att vara ärlig med att skyddsräckena är det mesta av kostnaden.

## Antimönster och fallgropar

- **Agent när ett arbetsflöde skulle duga.** Att ta på sig autonomins fulla risk för en uppgift vars steg var kända.
- **För breda verktyg och uppgifter.** Ett "gör vad som helst"-verktyg i stället för snäva verktyg med minsta behörighet.
- **Blindhet för promptinjektion.** Att mata opålitligt innehåll till en agent som håller verkliga privilegier.
- **Ingen mänsklig grind på oåterkalleliga åtgärder.** Att låta modellen skicka, betala eller radera utan kontroll.
- **Teater med flera agenter.** Att dela en enkel uppgift över agenter och betala samordningskostnad utan vinst.
- **Utvärdering på känsla.** Att bedöma efter hur transkriptet läses i stället för framgångsfrekvens för uppgiften.
- **Obegränsade loopar.** Inget tak på steg, tid eller utgifter, så att en fastnad agent bränner pengar och latens.
- **Ospårade körningar.** Inget register över vad agenten gjorde, vilket lämnar er oförmögna att felsöka, granska eller redovisa.

## Mognadsmodell

- **Nivå 1, Initiera:** Agenter prototypas ad hoc med bred verktygsåtkomst och inga gränser. Framgång bedöms efter demonstrationer, reaktivt, efter att något gått sönder. Det finns ingen utvärderingsmängd, ingen spårning och ingen mänsklig grind på konsekvensfulla åtgärder.
- **Nivå 2, Utveckla:** Vissa agenter har begränsade loopar och verktyg med minsta behörighet, och grundläggande spårning finns, men praxis varierar team för team. En manuell utvärderingsmängd fångar grova regressioner i några projekt medan andra saknar en. Mänskligt godkännande vaktar de mest uppenbara oåterkalleliga åtgärderna, men täckningen är ojämn och odokumenterad.
- **Nivå 3, Standardisera:** Gemensamma mönster styr autonomi, verktygsbehörigheter, sandlådor och människa-i-loopen-grindar, dokumenterade och upprätthållna över varje team. Varje konsekvensfull åtgärd grindas eller valideras, agenter spåras från början till slut och en automatisk utvärderingsmängd med poängsättning av framgångsfrekvens körs vid varje ändring. Promptinjektion behandlas som ett ständigt hot med ett definierat svar.
- **Nivå 4, Hantera:** Agentportföljen mäts och styrs mot utgångslägen. Framgångsfrekvens per uppgift, andel godkända injektionsförsvar, kostnad och stegantal per körning, latens för mänskligt godkännande och loop- eller felincidenter följs som mått. Återrullnings- och nedläggningströsklar upprätthålls på de beläggen snarare än klagomål. Budgetar per körning på steg, tid och utgifter övervakas, och en regression i något mått utlöser åtgärd före skalning, inte efter en incident.
- **Nivå 5, Orkestrera:** Autonomi matchas mot uppgiftens risk av policy och justeras kontinuerligt när resultat kommer in. Löpande offline- och onlineutvärdering knyter agentbeteende till affärsutfall, och organisationen avvecklar, omdefinierar eller ger om behörigheter åt agenter rutinmässigt när riskbilden skiftar. Spårning, kostnadsbudgetar och revisionsspår är enhetliga över portföljen. Försvar mot injektion och förvirrad delegat testas motståndsmässigt. Ansvarsskyldighet för autonoma åtgärder är tydlig och granskningsbar.

## Idéer för diskussion

1. Vilka av era nuvarande LLM-funktioner har i tysthet blivit agenter, och har var och ens autonomi begränsats med avsikt?
2. För varje agentverktyg, vad är det billigaste sättet för en angripare att missbruka det genom injicerat innehåll, och vad stoppar det?
3. Var har ni valt design med flera agenter, och kan ni visa att samordningskostnaden lönade sig jämfört med en enskild agent?
4. Vilka agentåtgärder är verkligen oåterkalleliga, och kunde var och en omdesignas till att vara reversibel eller iscensatt?
5. Om en agent vidtog en skadlig åtgärd i morgon, kunde ni rekonstruera exakt vad den gjorde och vem som var ansvarig?

## Viktigaste punkter

- En agent är en LLM i en loop med verktyg, minne och ett mål. Risken bor i loopen och verktygen, inte i texten.
- Föredra ett fast arbetsflöde när stegen är kända. Reservera autonomi för genuint öppna mål och begränsa den snävt.
- Verktygsanvändning är kärnförmågan. Ge varje verktyg minsta behörighet, ett validerat schema och en sandlåda.
- Grinda konsekvensfulla och oåterkalleliga åtgärder bakom en människa med verklig befogenhet och designa för billig återställning.
- Behandla agenter som motståndarmässiga: försvara mot promptinjektion och missbruk via förvirrad delegat (kapitel 4.2).
- Utvärdera på framgångsfrekvens för uppgiften över många körningar och spåra varje körning för felsökning, kostnadskontroll och revision (kapitel 6.5 och 6.6).
- Ofta är det rätta svaret att inte bygga en agent alls.

## Referenser och vidare läsning

- Shunyu Yao et al., *ReAct: Synergising Reasoning and Acting in Language Models*.
- Timo Schick et al., *Toolformer: Language Models Can Teach Themselves to Use Tools*.
- Anthropic, *Building Effective Agents* (engineering guidance on workflows versus agents).
- OWASP Foundation, *OWASP Top 10 for Large Language Model Applications* (including prompt injection and excessive agency).
- Simon Willison, writing on prompt injection and the "lethal trifecta" for AI agents.
- Norman Hardy, *The Confused Deputy* (the classic statement of the confused-deputy problem).
- Chip Huyen, *AI Engineering: Building Applications with Foundation Models*.
- Stuart Russell and Peter Norvig, *Artificial Intelligence: A Modern Approach* (intelligent agents and rational action).
