# 9.1 Site reliability engineering

## Översikt och motivation

[Site reliability engineering](https://en.wikipedia.org/wiki/Site_reliability_engineering) (SRE) tillämpar programvaruingenjörspraxis på att driva produktionssystem. I stället för att behandla drift som manuellt, ärendedrivet arbete skilt från utveckling behandlar SRE tillförlitlighet som ett ingenjörsproblem ni löser med kod, mätning och tydliga servicenivåmål. Kärnidén, populariserad av Google men nu utbredd, är enkel: de som håller system igång bör lägga större delen av sin tid på att bygga automatisering och förbättra system, inte på att för hand brandbekämpa samma fel om och om igen.

För stora team spelar detta roll eftersom skala höjer både värdet av tillförlitlighet och kostnaden för att göra fel. När en tjänst stöder miljontals användare eller tusentals interna konsumenter betyder en timmes avbrott förlorade intäkter, missade transaktioner och urholkat förtroende. Manuell drift som fungerar bra för en handfull servrar faller samman under hundratals tjänster och [kontinuerlig driftsättning](https://en.wikipedia.org/wiki/Continuous_deployment). SRE ger er ett gemensamt språk för tillförlitlighet, ett sätt att göra avvägningen mellan att leverera funktioner och att hålla saker stabila uttrycklig och ett sätt att hålla den linjen konsekvent över många team.

Företags- och myndighetssammanhang lägger ytterligare tyngd. Reglerade branscher som bank, sjukvård och offentliga tjänster bär ofta rättsliga eller avtalsmässiga tillgänglighetsåtaganden, revisionskrav och liten tolerans för avbrott som påverkar medborgare eller säkerhet. Statliga digitala tjänster publicerar alltmer sina tillförlitlighetsmål och prestandadata öppet. SRE ger er ett rigoröst, belägg-baserat sätt att definiera vad "tillräckligt tillförlitligt" betyder, mäta det ärligt och försvara ingenjörsprioriteringar inför ledning och tillsynsorgan med data snarare än åsikt.

*Se även:* kapitel 9.2 (observerbarhet och övervakning), kapitel 9.3 (incidenthantering) och kapitel 3.5 (skalbarhet, prestanda och motståndskraft).

## Nyckelprinciper

- **Tillförlitlighet är den viktigaste funktionen.** Ett system som inte fungerar är värdelöst oavsett hur många funktioner det har, men perfekt tillförlitlighet är varken uppnåelig eller värd sin kostnad.
- **Definiera tillförlitlighet med mätbara mål.** Servicenivåindikatorer (SLI:er), mål (SLO:er) och avtal (SLA:er) förvandlar vaga förväntningar till tal alla kan enas om.
- **100 procent är fel mål.** Användare kan inte se skillnad på ett mycket tillförlitligt system och ett perfekt tillförlitligt, så sikta på "tillräckligt tillförlitligt" och spendera den återstående budgeten på fart.
- **Felbudgetar linjerar incitament.** Gapet mellan SLO:n och 100 procent är en budget för risk som utvecklare och driftare delar och som ersätter argument med aritmetik.
- **Slit är fienden.** Repetitivt, manuellt, automatiserbart driftarbete bör mätas, begränsas och systematiskt elimineras.
- **Automatisera medvetet.** Automatisering är hur ett litet team driver ett stort system. Att investera i den är en förstklassig ingenjörsaktivitet.
- **Skuldfritt lärande.** Fel behandlas som tillfällen att förbättra system och processer, inte att straffa individer.

## Rekommendationer

### Definiera SLI:er, SLO:er och SLA:er medvetet

Börja från användarens perspektiv. En **[servicenivåindikator](https://en.wikipedia.org/wiki/Service-level_indicator)** är ett kvantitativt mått på en tjänsts beteende, som andelen begäranden som betjänas på under 300 millisekunder eller andelen lyckade svar. Välj ett litet antal SLI:er som genuint speglar användares nöjdhet: tillgänglighet, latens, korrekthet och färskhet är vanliga. Ett **[servicenivåmål](https://en.wikipedia.org/wiki/Service-level_objective)** är ett målvärde eller intervall för en SLI, till exempel "99,9 procent av begärandena lyckas över ett rullande 28-dagarsfönster." Ett **[servicenivåavtal](https://en.wikipedia.org/wiki/Service-level_agreement)** är ett kontrakt med konsekvenser (återbetalningar, viten) knutna till en lovad nivå. Håll era SLO:er strängare än era SLA:er, så att ni får en varning innan ni bryter ett åtagande. Publicera era SLO:er, granska dem kvartalsvis och behandla dem som levande dokument som skärps eller lättas när ni lär er.

### Anta felbudgetar och upprätthåll dem

Felbudgeten är `100 % minus SLO:n`. Om din SLO är 99,9 procent är din budget 0,1 procent otillförlitlighet per fönster, ungefär 43 minuter per månad. Spendera den på planerad risk: offensiva releaser, experiment och kontrollerade feltester. När budgeten är frisk kan team leverera snabbt. När den tar slut bör policyn automatiskt flytta prioriteringarna mot tillförlitlighetsarbete och pausa riskfyllda ändringar tills systemet återhämtat sig. Felbudgetens kraft är att ni kommer överens om den i förväg, så att den tar bort känslorna och politiken ur avbrottets ögonblick.

### Mät och minska slit

Slit är driftarbete som är manuellt, repetitivt, automatiserbart, taktiskt och växer i takt med systemet. Följ andelen SRE-tid som går åt till slit och sätt ett tak, vanligen runt 50 procent, så att minst hälften av er ingenjörstid går till varaktiga förbättringar. Håll en backlogg av slitminskande projekt, prioritera efter frekvens gånger kostnad och fira att döda en återkommande uppgift lika mycket som att leverera en ny funktion. Ett **automatiseringsmandat** gör detta uttryckligt: varje manuell procedur ni utför fler än ett satt antal gånger blir en kandidat för automatisering eller självbetjäningsverktyg.

### Planera kapacitet och prognostisera efterfrågan

Modellera din förväntade last utifrån historiska trender, planerade lanseringar och affärsprojektioner. Kombinera prognoser för organisk tillväxt med engångshändelser som marknadsföringskampanjer, deklarationsfrister eller bidragsansökningsperioder som spelar stor roll i myndigheter. Behåll marginal över toppen, belastningstesta för att kontrollera dina antaganden och automatisera skalning där du kan samtidigt som du behåller en människogranskad [kapacitetsplan](https://en.wikipedia.org/wiki/Capacity_planning) för stora åtaganden. Följ ledtider för provisionering så att en brist aldrig tar dig på sängen.

### Behandla tillförlitlighet som en funktion med verklig kostnad

Varje extra "nia" av tillgänglighet kostar vanligen långt mer i redundans, testning och driftsofistikering än den förra. Gör kostnaden för niorna uttrycklig, så att produktägare väljer målet med öppna ögon. Designa för graciös degradering, så att partiella fel ger reducerad tjänst snarare än totala avbrott. Investera i redundans och failover i proportion till SLO:n, inte jämnt över varje komponent.

### Välj en SRE-organisationsmodell

Det finns ingen enda korrekt struktur. Ett **centraliserat** SRE-team ger konsekvens, djup expertis och gemensamma verktyg, men det kan bli en flaskhals eller en soptipp för andras problem. En **inbäddad** modell placerar SRE:er inuti produktteam för nära samarbete, men riskerar inkonsekvens och isolering. Många stora organisationer använder en hybrid: ett centralt plattforms- och standardteam plus inbäddade tillförlitlighetsingenjörer, med en tydlig engagemangsmodell som definierar när en tjänst kvalificerar sig för SRE-stöd och vilken produktionsberedskapsribba den måste klara först.

## Avvägningar: för- och nackdelar

| Beslut | Fördelar | Nackdelar |
|---|---|---|
| Strikta SLO:er (fler nior) | Högre användarförtroende, uppfyller avtal | Stigande kostnad, långsammare funktionsleverans |
| Lösa SLO:er (färre nior) | Snabbare leverans, lägre kostnad | Risk för användaravhopp och SLA-viten |
| Centraliserad SRE | Konsekvens, gemensam expertis | Flaskhalsar, avstånd från produkten |
| Inbäddad SRE | Nära samarbete, sammanhang | Inkonsekvens, svårt att bemanna |
| Tung automatiseringsinvestering | Skalar, minskar slit | Kostnad i förväg, automatisering kan själv fallera |

Tillförlitlighetsteknik handlar egentligen om att spendera ändliga resurser klokt. Att jaga en extra nia användare inte ens kan uppfatta slösar pengar som kunde finansiera funktioner eller sänka priser. Gå åt andra hållet och underinvestera i ett system vars fel orsakar verklig skada, och det är vårdslöst. Felbudgetramverket finns just för att göra den avvägningen synlig och förhandlingsbar snarare än implicit och kontroversiell. Avvägningen kring organisationsmodell är lika verklig: det rätta svaret beror på företagets storlek, ingenjörsmognad och hur enhetliga era tjänster är.

## Frågor att diskutera med ditt team

1. **Vilken exakt SLI speglar det era användare faktiskt känner, och kan ni visa att den inte är ett fåfängemått?** Välj fel indikator och varje panel ser grön ut medan användare lider, vilket är fåfänge-SLI-fällan det här kapitlet varnar för. Ta med verklig data till diskussionen: mät samma användarresa från en verklig begäransväg (inloggning till panel, kassa till bekräftelse) snarare än serverns CPU eller en backend-hälsokontroll. För ett stort team sprider sig en dålig SLI: dussintals tjänster ärver den, larm slår till på fel sak och felbudgeten slutar betyda något. I företags- och myndighetssammanhang där ett SLA bär återbetalningar eller medborgarpåverkan är er SLI det belägg ni försvarar inför revisorer, så den måste spåra direkt till användarsynlig framgång. Om ni inte kan dra en linje från talet till en användares upplevelse, byt ut talet.

2. **Vad måste en tjänst bevisa innan ert SRE-team tar den i jour, och vem säger nej?** Utan en produktionsberedskapsribba blir ett centralt SRE-team en soptipp för varje instabil tjänst och drunknar i andras tekniska skuld. Skriv ner inträdeskriterierna: en ägd SLO, fungerande körböcker, åtgärdbara larm, kapacitetsmarginal och en demonstrerad väg för driftsättning och återställning. För en stor organisation är denna engagemangsmodell det som hindrar tillförlitlighetsteamet från att bli en flaskhals som saktar ner alla. I reglerade sammanhang fungerar beredskapsgranskningen även som en kontroll ni kan visa tillsynsorgan. Avgör vem som har befogenhet att vägra introduktion, eftersom en ribba ingen upprätthåller inte är en ribba, och svaret avgör om SRE skalar eller kollapsar under ärvd smärta.

3. **Hur långt i förväg förprovisionerar ni för er enskilt största förutsägbara topp, och känner ni till er provisioneringsledtid?** Att anta att molnelasticitet är omedelbar och oändlig inbjuder till brist under just de toppar som spelar störst roll, och de topparna (deklarationsfrister, ansökningsperioder, rea) är de ögonblick då fel är mest synligt och mest kostsamt. Ta med talen: historisk topplast, prognostiserad tillväxt, multipeln ni belastningstestar till och den verkliga ledtiden för att skaffa stor reserverad kapacitet eller specialiserade instanser. För statliga säsongstjänster kan toppen vara flera gånger normal last och är politiskt omöjlig att missa, så förprovisionering veckor i förväg slår att hoppas att autoskalning hänger med. Svaret bör sätta en konkret kalender: när ni belastningstestar, när ni låser kapacitet och vem som äger go-beslutet.

4. **När er felbudget tar slut, vad händer faktiskt, och vem har stånd att upprätthålla den?** En felbudget som aldrig agerades på när den förbrukats är bara dekoration, och ögonblicket för ett avbrott är den sämsta tidpunkten att förhandla policyn från grunden. Det konkurrerande draget är verkligt: en bunden lansering, en intäktsfrist eller ett offentligt tillkännagivande kommer att pressa hårt mot en frysning av riskfyllda ändringar. Ta med förbränningstakten, den förhandsöverenskomna policytexten och ett register över de senaste gångerna budgeten överskreds, så att ni kan se om frysningen faktiskt höll. För ett stort team linjerar budgeten bara incitament om varje grupp ärver samma upprätthållande, så avgör i förväg vem som godkänner ett undantag och hur det undantaget loggas. I företags- och myndighetssammanhang där ett SLA bär viten eller medborgarpåverkan blir undantagsspåret en revisionsartefakt, så namnge den ansvariga ägaren nu snarare än att improvisera när budgeten redan är borta.

5. **Hur stor andel av ert SRE-teams vecka är slit, och är det ett uppmätt tal eller en känsla?** Slit ingen räknar expanderar i tysthet tills teamet lägger all sin tid på brandbekämpning och ingen på att bygga varaktiga förbättringar, vilket är just den fälla SRE finns för att fly. Spänningen är att mätning av slit är arbete i sig, och ingenjörer under tidspress motsätter sig att logga var deras timmar går. Ta med ett ärligt urval: en eller två veckors spårad tid mot en gemensam definition av slit (manuellt, repetitivt, automatiserbart, taktiskt och skalande med systemet), plus backloggen av automatiseringsprojekt rangordnade efter frekvens gånger kostnad. För en stor organisation betyder ett tak på 50 procent bara något om det rapporteras och försvaras team för team, så kom överens om vem som granskar talet och vad som händer när ett team överskrider det. I reglerade och myndighetssammanhang frigör ett tak på slit knappa specialister för det kontroll- och revisionsarbete manuell drift tränger undan, så behandla slittalet som en kapacitetssignal ledningen bör se.

6. **Vilken SRE-organisationsmodell kör ni, och vilka belägg skulle tala om för er att den har slutat passa?** Ett centraliserat team ger konsekvens och gemensamma verktyg men kan bli en flaskhals. En inbäddad modell ger sammanhang men driftar mot inkonsekvens. Hybriden de flesta stora organisationer landar i behöver en tydlig engagemangsmodell, annars ärver den båda svagheterna. Ta med signalerna som avslöjar påfrestning: hur länge tjänster väntar på SRE-stöd, hur mycket tillförlitlighetspraxis varierar mellan team och om inbäddade ingenjörer känner sig avskurna från en professionell gemenskap. Det rätta svaret beror på företagets storlek, ingenjörsmognad och hur enhetliga era tjänster är, så omvärdera det när de förändras snarare än att behandla det första valet som permanent. För en företags- eller myndighetsorganisation med många team och strikta enhetlighetskrav balanserar en central standard- och plattformsgrupp plus inbäddade tillförlitlighetsingenjörer vanligen konsekvens mot lokalt sammanhang, men bara om engagemangsmodellen och produktionsberedskapsribban är nedskrivna och någon äger dem.

## Sektorsperspektiv

**Startup.** Med en handfull ingenjörer och ingen livslängd för ett dedikerat tillförlitlighetsteam, välj en enda SLO på den användarresa som spelar störst roll och dela jouren över hela teamet. Lita på din molnleverantörs hanterade tjänster och inbyggda övervakning i stället för att bygga observerbarhetsinfrastruktur och skriv korta efterhandsgranskningar i ett gemensamt dokument så att rättelserna fastnar. Fart spelar större roll än process här: en lös SLO ni faktiskt upprätthåller slår en genomarbetad ingen bevakar.

**Småföretag.** Utan specialist som driver tillförlitlighet, behandla det som en disciplin ni köper in er i genom er plattform: hostad drifttidsövervakning, hanterade databaser och statussidesverktyg i stället för en skräddarsydd stack. Sätt en eller två SLO:er knutna till de transaktioner som betalar räkningarna och avgör ärligt vilka fel som skulle kosta er en kund. Köp motståndskraft där det är billigare än att bygga den och håll driftbördan lätt nog för att era befintliga ingenjörer kan bära den vid sidan av funktionsarbete.

**Storföretag.** Utmaningen är konsekvens över många team: ett gemensamt SLO-ordförråd, en gemensam felbudgetpolicy och en produktionsberedskapsribba varje tjänst klarar innan SRE tar den i jour. En central plattforms- och standardgrupp plus inbäddade tillförlitlighetsingenjörer håller praxis enhetlig utan att bli en flaskhals, och styrning kräver felbudgetar rapporterade och upprätthållna på samma sätt överallt. Budgetera observerbarhetsinfrastrukturen och automatiseringsinvesteringen uttryckligen och hantera tillförlitlighet som en portfölj med mått ledningen kan se.

**Offentlig sektor.** Offentliga tjänster bär ofta publicerade tillgänglighetsmål, lagstadgade åtaganden och revisionsskyldigheter, så SLO:er och felbudgetbeslut blir register ni försvarar inför tillsynsorgan. Upphandlingsregler kan begränsa vilken övervakning och hosting ni får använda, och transparensförväntningar driver er att publicera tillförlitlighetsdata på en publik statuspanel. Planera för extrema säsongstoppar som deklarationsfrister och ansökningsperioder veckor i förväg och behåll en skuldfri efterhandsgranskningskultur så att offentliga fel driver systemförbättring snarare än individuell skuld.

## Exempel

**Startup.** Ett startup på tio personer driver en enda webbapp och delar jouren över tre ingenjörer. I stället för att bygga ett tillförlitlighetsteam det inte har råd med väljer det en meningsfull SLO: 99,5 procent framgång på flödet inloggning-till-panel, mätt från verkliga användarbegäranden. När ett instabilt tredjeparts-API börjar äta den budgeten lägger teamet en fredag på att lägga till ett omförsök och en cache i stället för att leverera nästa funktion och skriver sedan en efterhandsgranskning på två stycken i ett gemensamt dokument så att rättelsen fastnar.

**Storföretag.** Ett globalt betalföretag sätter en tillgänglighets-SLO på 99,99 procent för sitt transaktions-API, vilket ger en felbudget på ungefär fyra minuter per månad. Ett centralt SRE-plattformsteam äger gemensam [observerbarhet](https://en.wikipedia.org/wiki/Observability_(software)), incidentverktyg och felbudgetpolicyn, medan inbäddade tillförlitlighetsingenjörer arbetar inuti varje produktgrupp. När en ny bedrägeriupptäcktsfunktion bränner halva månadsbudgeten på en vecka fryser den förhandsöverenskomna policyn icke-kritiska releaser tills tillförlitlighetsarbete återställer marginalen. Chefer accepterar detta utan debatt, eftersom de ratificerade policyn i förväg.

**Offentlig sektor.** En nationell skattemyndighet driver en deklarationstjänst online med extrema säsongstoppar runt den årliga fristen. Dess SRE-team prognostiserar efterfrågan från tidigare år plus befolknings- och policyförändringar, belastningstestar till flera gånger normal topp och förprovisionerar kapacitet veckor i förväg. Publika SLO:er för tillgänglighet och sidlatens läggs upp på en statuspanel. En skuldfri [efterhandsgranskning](https://en.wikipedia.org/wiki/Postmortem_documentation)skultur (att granska fel för att förbättra system snarare än tilldela individuell skuld) och ett automatiseringsmandat skär stadigt ned de manuella ingrepp som en gång dominerade deklarationssäsongen och frigör personal att förbättra systemet i stället för att amma det genom varje frist.

## Affärsnytta: motiv, ROI och TCO

Avkastningen på SRE kommer från tre källor: undvikna avbrott, mindre driftarbete och snabbare säker leverans. Avbrott för en stor tjänst kan kosta tusentals till miljoner per timme i förlorade intäkter, viten och avhjälpning, så även måttliga tillförlitlighetsvinster betalar snabbt för ett team. Slitminskning förvandlar återkommande manuell kostnad till en engångsinvestering i automatisering, så total ägandekostnad faller när skalan växer snarare än att klättra i takt med den. Felbudgetar låter verksamheten leverera fortare när tillförlitligheten är frisk och fångar funktionsvärde som alltför försiktig drift skulle lämna på bordet.

Adoptionskostnaden är verklig. SRE behöver skickliga ingenjörer, observerbarhetsinfrastruktur och kulturförändring som konkurrerar med funktionsfrister. Men kostnaden för att inte anta är högre i skala: obegränsad driftbemanning, oförutsägbara avbrott, personalutbrändhet och avgångar samt anseendeskada som är svår att kvantifiera men lätt att drabbas av. För att driva ärendet inför ledningen, ramma in SRE som riskhantering med mätbar avkastning. Presentera den nuvarande kostnaden för incidenter och manuell drift, SLO-målen knutna till affärsåtaganden och den prognostiserade minskningen av båda. Förankra argumentet i felbudgeten som ett styrningsverktyg som ger ledningen en spak över avvägningen tillförlitlighet mot fart.

## Antimönster och fallgropar

- **SRE som omdöpt drift.** Att döpa om ett driftteam utan ingenjörstiden, automatiseringsmandatet och befogenheten att säga ifrån ändrar ingenting.
- **Att sikta på 100 procent.** Att jaga perfekt tillförlitlighet slösar pengar och blockerar leverans för vinster användare inte kan uppfatta.
- **Fåfänge-SLI:er.** Att mäta serverns CPU i stället för användarsynlig framgång ger tal som ser bra ut medan användare lider.
- **Felbudgetar utan tänder.** En budget som aldrig upprätthålls när den förbrukats är bara en dekoration.
- **Slit utan mätning.** Om ni inte följer slit förbrukar det i tysthet teamet tills inget förbättringsarbete sker.
- **SRE som soptipp.** Centraliserade team som ärver varje instabil tjänst utan en beredskapsribba drunknar i andras tekniska skuld.
- **Att ignorera kapacitetsledtider.** Att anta att molnelasticitet är omedelbar och oändlig inbjuder till brist under just de toppar som spelar störst roll.

## Mognadsmodell

**Nivå 1, Initiera.** Drift är manuell och reaktiv. Det finns inga formella SLO:er, tillförlitlighet är en åsiktsfråga och samma incidenter återkommer medan brandbekämpning dominerar. All automatisering är tillfällig, och ingen äger tillförlitlighet som en ingenjörsfråga.

**Nivå 2, Utveckla.** Vissa tjänster har grundläggande SLI:er och SLO:er och rudimentär övervakning och larmning, men praxis varierar kraftigt mellan team. Slit erkänns men mäts inte, automatisering är ad hoc och efterhandsgranskningar sker inkonsekvent. Tillförlitligheten förbättras i de fickor där individer driver på den, inte för att organisationen kräver det.

**Nivå 3, Standardisera.** SLI:er, SLO:er och en felbudgetpolicy är dokumenterade och tillämpade konsekvent över team. Slit är definierat och följs, kapacitetsplanering är rutin, en SRE-engagemangsmodell med produktionsberedskapsgranskningar finns och automatisering är ett finansierat arbetsflöde snarare än ett sidoprojekt. Tillförlitlighetspraxis är nedskriven och upprätthållen i hela organisationen.

**Nivå 4, Hantera.** Tillförlitlighetsprogrammet mäts och styrs med data mot utgångslägen. Felbudgetens förbränningstakt, slitprocent, SLO-uppfyllnad, genomsnittlig tid till återhämtning och provisioneringsledtider följs som mått, granskas med fast takt och används för att hålla team till sina mål. Budgetöverskridanden utlöser den överenskomna frysningen, kapacitet prognostiseras mot efterfrågemodeller och varje go- eller no-go-beslut vilar på belägg snarare än åsikt.

**Nivå 5, Orkestrera.** Tillförlitlighetsteknik är integrerad i hela organisationen och kontinuerligt förbättrad. Felbudgetpolicyn är automatiserad och respekterad överallt, det mesta av driften är självbetjäning, kapacitet provisioneras proaktivt och tillförlitlighetsdata driver adaptiva avvägningar mellan fart och stabilitet. Organisationen omdefinierar rutinmässigt SLO:er, avvecklar slit och balanserar om tillförlitlighetsinvesteringen när verksamheten och riskbilden skiftar.

## Idéer för diskussion

- Hur bör en organisation sätta sina första SLO:er när den saknar historisk tillförlitlighetsdata att förankra dem i?
- När felbudgeten är förbrukad men en stor lansering är bunden, vem har befogenhet att åsidosätta frysningen, och hur registreras det beslutet?
- Är en centraliserad, inbäddad eller hybrid SRE-modell rätt för er organisation, och vad skulle utlösa en förändring?
- Hur värderar ni en extra nia av tillgänglighet mot de funktioner samma investering kunde finansiera?
- Vad räknas som slit i ert sammanhang, och var går gränsen mellan värdefullt manuellt omdöme och eliminerbar repetition?
- Hur bör tillförlitlighetsmål skilja sig mellan medborgarvända myndighetstjänster och interna företagsverktyg?

## Viktigaste punkter

- SRE tillämpar programvaruteknik på drift och behandlar tillförlitlighet som en mätbar, finansierbar funktion.
- SLI:er, SLO:er och SLA:er förvandlar tillförlitlighet från åsikt till överenskomna tal. Håll SLO:er strängare än SLA:er.
- Felbudgeten linjerar utvecklare och driftare genom att göra avvägningen tillförlitlighet mot fart uttrycklig och förhandlad i förväg.
- Mät och begränsa slit och behandla automatisering som förstklassig ingenjörskonst så att drift skalar sublinjärt.
- Planera kapacitet utifrån efterfrågeprognoser och respektera provisioneringsledtider, särskilt för säsongstoppar.
- Välj en SRE-organisationsmodell medvetet och definiera en tydlig engagemangs- och produktionsberedskapsribba.

## Referenser och vidare läsning

- Betsy Beyer, Chris Jones, Jennifer Petoff, Niall Richard Murphy, *Site Reliability Engineering: How Google Runs Production Systems*
- Betsy Beyer, Niall Richard Murphy, David K. Rensin, Kent Kawahara, Stephen Thorne, *The Site Reliability Workbook: Practical Ways to Implement SRE*
- David N. Blank-Edelman (editor), *Seeking SRE: Conversations About Running Production Systems at Scale*
- Thomas A. Limoncelli, Strata R. Chalup, Christina J. Hogan, *The Practice of Cloud System Administration*
- Nicole Forsgren, Jez Humble, Gene Kim, *Accelerate: The Science of Lean Software and DevOps*
