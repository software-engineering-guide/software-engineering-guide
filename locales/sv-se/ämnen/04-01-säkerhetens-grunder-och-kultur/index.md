# 4.1 Säkerhetens grunder och kultur

## Översikt och motivation

Säkerhet är inte en funktion du skruvar på i slutet, och det är inte jobbet för ett specialiserat team som sitter vid sidan av utvecklingen. I en stor organisation är säkerhet en egenskap hos hur hela systemet designas, byggs, drivs och styrs. När tusentals ingenjörer levererar kod över hundratals tjänster avgör den svagaste länken hur stor skada en incident kan göra. En enda felkonfigurerad lagringshink, ett opatchat beroende eller ett överprivilegierat tjänstekonto kan exponera miljontals poster. Grunder och kultur är det som hindrar det från att hända i skala.

För företag är insatserna finansiella och anseendemässiga: intrångskostnader, regulatoriska viten, förlorade kunder och sänkta värderingar. För myndigheter sträcker de sig till nationell säkerhet, offentligt förtroende och kontinuiteten i samhällsviktiga tjänster. Båda sammanhangen delar en hård sanning: du kan inte upprätthålla säkerhet enbart genom kontroller och grindar. Den måste internaliseras av de människor som gör arbetet. En kultur där ingenjörer förstår hot, känner ägarskap och belönas för att lyfta farhågor ger långt bättre utfall än en som lutar sig mot ett överarbetat säkerhetsteam som spelar målvakt.

Det här kapitlet lägger fram de mentala modeller och kulturella praxis som underbygger varje annat säkerhetskapitel i den här guiden. Det behandlar att göra säkerhet till allas jobb, [hotmodellering](https://en.wikipedia.org/wiki/Threat_model), livscykeln för säker utveckling, grundläggande arkitekturprinciper som [försvar på djupet](https://en.wikipedia.org/wiki/Defense_in_depth_(computing)) och [nolltillit](https://en.wikipedia.org/wiki/Zero_trust_security_model) samt hur man prioriterar säkerhetsarbete efter verklig risk snarare än rädsla eller mode.

*Se även:* kapitel 4.2 (applikationssäkerhet), kapitel 4.3 (infrastruktur- och molnsäkerhet), kapitel 4.4 (säkerhetsdrift) och kapitel 4.6 (regelefterlevnad och styrning) bygger på dessa grunder.

## Nyckelprinciper

- **Säkerhet är allas jobb.** Varje ingenjör, produktansvarig och operatör äger säkerheten i det de bygger. Säkerhetsteamet möjliggör, rådger och granskar. Det gör inte och kan inte göra arbetet ensamt.
- **Anta intrång.** Designa som om angripare redan är inne. Minimera vad en komprometterad komponent kan nå.
- **Försvar på djupet.** Ingen enskild kontroll räcker. Lagra oberoende kontroller så att fel i en inte betyder fel i alla.
- **[Minsta behörighet](https://en.wikipedia.org/wiki/Principle_of_least_privilege).** Ge den minsta åtkomst som behövs, under minsta möjliga tid, och återkalla den automatiskt när den inte längre behövs.
- **Skifta åt vänster.** Hitta och rätta problem så tidigt som möjligt, när de är billigast att åtgärda.
- **Riskbaserad prioritering.** Lägg insatsen där kombinationen av sannolikhet och konsekvens är högst, vägledd av CIA-triaden (konfidentialitet, integritet och tillgänglighet), inte på det som kom i nyheterna den här veckan.
- **Skuldfritt lärande.** Behandla säkerhetsincidenter och nästan-olyckor som tillfällen att lära, inte som anledningar till bestraffning.

## Rekommendationer

### Inrätta ett program för säkerhetsambassadörer

Placera en utsedd säkerhetsambassadör (security champion) i varje utvecklingsteam. Ambassadörer är inga heltidsspecialister på säkerhet. De är ingenjörer med extra utbildning och en direkt linje till det centrala säkerhetsteamet. De granskar designer, triagerar fynd, besvarar kollegors frågor och bär med sig säkerhetskontext in i planeringen. Det skalar säkerhetsexpertis över organisationen utan att anställa en specialist för varje team, och det bygger förtroende, eftersom rådet kommer från en kollega som faktiskt känner kodbasen.

Ge ambassadörerna verkligt stöd: ett regelbundet forum att dela vad de lär sig, budget för utbildning och konferenser, erkännande i medarbetarsamtal och tid utskuren ur deras leveransåtaganden. Ett ambassadörsprogram som bara finns på pappret ger ingenting.

### Praktisera hotmodellering rutinmässigt

Hotmodellering är den disciplinerade vanan att fråga "vad kan gå fel?" innan du bygger. Gör det för nya tjänster, större funktioner och varje ändring av förtroendegränser. Håll det tillräckligt lätt för att det faktiskt sker ofta.

- **[STRIDE](https://en.wikipedia.org/wiki/STRIDE_model)** är en praktisk checklista kopplad till säkerhetsegenskaper: Spoofing (autentisering), Tampering (integritet), Repudiation (oavvislighet), Information disclosure (konfidentialitet), Denial of service (tillgänglighet) och Elevation of privilege (auktorisering). Gå igenom varje dataflöde och fråga hur varje kategori tillämpas.
- **PASTA** (Process for Attack Simulation and Threat Analysis) är en tyngre, riskcentrerad metod i sju steg som knyter tekniska hot till affärskonsekvens. Använd den för högvärdiga system.
- **[Angreppsträd](https://en.wikipedia.org/wiki/Attack_tree)** bryter ned ett mål ("stjäl kunddata") i de förgrenade steg en angripare skulle ta, vilket hjälper dig att hitta och beskära vägar.

Håll hotmodeller som levande dokument bredvid koden och ompröva dem närhelst arkitekturen ändras.

### Bygg en livscykel för säker programvaruutveckling

Väv in säkerhet i varje fas i stället för att behandla den som en slutgrind:

- **Krav:** fånga säkerhets- och integritetskrav vid sidan av funktionella.
- **Design:** hotmodellera och granska förtroendegränser.
- **Implementation:** upprätthåll standarder för säker kodning, kodgranskning och hemlighetsskanning före incheckning.
- **Testning:** kör [SAST](https://en.wikipedia.org/wiki/Static_application_security_testing) (statisk applikationssäkerhetstestning), [DAST](https://en.wikipedia.org/wiki/Dynamic_application_security_testing) (dynamisk applikationssäkerhetstestning) och beroendeskanning i pipelinen (se kapitel 4.4).
- **Release:** verifiera proveniens, signera artefakter och kontrollera konfiguration.
- **Drift:** övervaka, patcha och svara.

Poängen med att skifta åt vänster är inte att stapla allt arbete tidigare och överväldiga ingenjörer. Den är att fånga de sorters defekter som är långt billigare att rätta tidigt.

### Anta arkitekturprinciper för nolltillit

Traditionell perimetersäkerhet antar att allt innanför nätverket är pålitligt. Det antagandet fallerar i samma stund en angripare får fotfäste. Nolltillit ersätter implicit nätverkstillit med uttrycklig, kontinuerlig verifiering: autentisera och auktorisera varje begäran utifrån identitet, enhetens tillstånd och kontext, oavsett var på nätverket den kommer ifrån. Kombinera stark identitet, auktorisering med minsta behörighet, mikrosegmentering och [kryptering](https://en.wikipedia.org/wiki/Encryption) överallt. Nolltillit är en resa, inte en produkt, så ta det ett steg i taget.

### Prioritera efter risk med CIA-triaden

Ramma in varje tillgång och kontroll kring **Konfidentialitet**, **Integritet** och **Tillgänglighet** (CIA, Confidentiality, Integrity, Availability). Inte all data behöver samma skydd: en publik marknadsföringssida och en databas med hälsojournaler har vitt skilda konfidentialitetsbehov. Klassificera dina tillgångar, uppskatta sannolikhet och konsekvens av komprometterande och rikta knapp säkerhetsinsats mot de högsta riskkombinationerna. Skriv ner dina riskbeslut så att andra kan granska och försvara dem senare.

## Avvägningar: för- och nackdelar

| Tillvägagångssätt | Fördelar | Nackdelar |
|---|---|---|
| Centralt säkerhetsteam äger all säkerhet | Djup expertis, konsekventa standarder | Flaskhals, ingenjörer tappar engagemang, skalar inte |
| Distribuerad säkerhet (ambassadörer) | Skalar, bygger ägarskap, snabbare återkoppling | Kräver investering, ojämn kompetens, behöver samordning |
| Tung hotmodellering i förväg för allt | Grundlig, fångar designbrister | Bromsar leverans, kan bli kryssande av rutor |
| Lätt, riskinriktad hotmodellering | Snabb, fokuserad på det som spelar roll | Kan missa hot i "lågriskiga" system |
| Strikta grindar som blockerar releaser | Upprätthåller regelefterlevnad | Friktion, uppmuntrar kringgående |

Den centrala spänningen är mellan hastighet och säkring. Luta för långt mot grindar och central kontroll och du skapar friktion som ingenjörer går runt, vilket föder skuggor-IT och förbittring. Luta för långt mot autonomi utan stöd och du får inkonsekvent, ogranskad säkerhet. Det hållbara svaret är en stark kultur med möjliggörande skyddsräcken: automatiserade där du kan, mänskliga där omdöme krävs och alltid förklarade snarare än bara pådyvlade.

## Frågor att diskutera med ditt team

1. **Vilka av era system förtjänar tung hotmodellering, och vem avgör nivån?** I en stor egendom kan ni inte köra en PASTA-analys i sju steg på varje tjänst, så ni behöver en uttrycklig regel för när en STRIDE-genomgång på 30 minuter räcker och när ett högvärdigt system förtjänar djup, affärskonsekvensdriven modellering. Förankra beslutet i er CIA-klassificering: system som håller reglerade register, betalningsflöden eller autentiseringslogik ligger högst upp, och en publik marknadsföringssida gör det inte. För företags- och myndighetsarbete kommer en revisor att be er försvara varför ett givet system modellerades som det gjordes, så skriv ner nivåkriterierna och namnge ägaren som tillämpar dem. Ta med er nuvarande tillgångsklassificering och en lista över tjänster utan hotmodell till mötet, eftersom klyftan mellan dem är er verkliga risk. Om ni inte kan enas om ribban hamnar ni som standard i att modellera allt lätt eller inget djupt, och båda sviker er.

2. **När en säkerhetsambassadör och en leveransdeadline kolliderar, vem kan faktiskt stoppa releasen?** Ett ambassadörsprogram ändrar bara utfall om ambassadören bär verklig auktoritet, inte bara extra utbildning och goda avsikter. Besluta i förväg om en ambassadör kan blockera en leverans, om de eskalerar till det centrala AppSec-teamet och vilken allvarlighetsgrad på ett fynd som motiverar att stoppa leveransen mot att spåra det. Det spelar störst roll under tryck, när en produktansvarig vill efterskänka en designbrist veckan före lansering, vilket är exakt när obearbetade brister är dyrast att rätta. Ta med ett nyligt exempel där en säkerhetsfarhåga mötte en deadline och spåra vem som avgjorde och hur, eftersom den berättelsen avslöjar er verkliga eskaleringsväg. Om det ärliga svaret är att leveransen alltid vinner är era ambassadörer dekorativa, och ni bör rätta incitamentet innan ni lägger till fler av dem.

3. **Vad ändrar "anta intrång" konkret i er nästa designgranskning?** Principen är lätt att nicka åt och svår att operationalisera, så fäst den vid specifika åtaganden: vilka förtroendegränser ni ska skärpa, var ni ska lägga till mikrosegmentering och hur ni ska krympa vad ett enda komprometterat tjänstekonto kan nå. För ett stort team är utdelningen minskad sprängradie, så att en angripare som landar i en tjänst inte kan svänga vidare till datalagret bakom. I företags- och myndighetssammanhang formar detta också era beslut om minsta behörighet och kortlivade uppgifter, som är billiga att designa in och smärtsamma att eftermontera. Ta med ett verkligt tjänstediagram och fråga vad en angripare gör efter att ha tagit webbnivån, och förbind er sedan till två begränsningsändringar det här kvartalet. Vag enighet om att intrång sker är värdelös om den inte flyttar en behörighet, en nätverksregel eller en uppgifts livslängd.

4. **Hur ska ni veta att er säkerhetskultur faktiskt förbättras, och vilket mått skulle ni försvara inför styrelsen?** Andel slutförd utbildning och antal ärenden är lätta att samla in och nästan värdelösa, eftersom de mäter aktivitet snarare än riskminskning, och en stor organisation drunknar i dem. Välj utfallsmått ni faktiskt skulle satsa en budget på: median tid att åtgärda fynd med hög allvarlighetsgrad, andelen tjänster med en aktuell hotmodell, andelen incidenter som fångas före produktion och frekvensen av självrapporterade nästan-olyckor, som bör stiga när förtroendet växer snarare än falla. Den motstridiga hänsynen är att varje bra mått kan manipuleras, så para varje med ett motmått och granska trenden snarare än ögonblicksbilden. Ta med er nuvarande panel och fråga vilka tal som skulle ändras om säkerheten genuint blev sämre. Alla som inte skulle det är dekoration. I företags- och myndighetssammanhang kommer en tillsynsmyndighet eller en revisionskommitté att be om belägg för att kontroller fungerar, så välj mått ni kan försvara under granskning snarare än sådana som bara ser gröna ut.

5. **Vad händer faktiskt nästa gång en ingenjör rapporterar ett misstag, och är er process skuldfri i praktiken eller bara på bilden?** Skuldfritt lärande är den princip som oftast bekänns och minst ofta efterlevs, eftersom den första allvarliga incidenten prövar om ledningen verkligen menar det. Besluta i förväg hur ni skiljer ansvar för att rätta ett problem från bestraffning för att ha orsakat det, och vem som leder efterhandsgranskningen så att den handlar om trasiga system snarare än namngivna individer. Spänningen är verklig: intressenter vill att någon hålls ansvarig, men att straffa den som rapporterar garanterar att nästa misstag förblir dolt tills det blir ett intrång. Ta med era två senaste incidentgranskningar och kontrollera om de skyllde på en person eller en kontroll, och om ingenjören som slog larm blev tackad eller i tysthet sidosatt. För myndigheter och reglerade företag höjer obligatoriska regler om anmälan av intrång insatserna ytterligare, eftersom en kultur som döljer misstag också kommer att missa de rapporteringsfrister som bär rättsliga påföljder.

6. **Vem äger friktionen i era skifta-åt-vänster-verktyg, och köper ni det, bygger det eller drunknar i det?** Automatiserad statisk och dynamisk analys, beroendeskanning och hemlighetsskanning är ryggraden i en livscykel för säker utveckling, men en pipeline som översvämmar ingenjörer med falska positiva lär dem att ignorera säkerhetsutdata, vilket är värre än ingen skanning alls. Besluta vem som justerar verktygen, vem som triagerar fynden och om ni köper en integrerad plattform eller sätter ihop skannrar med öppen källkod som ni sedan själva måste underhålla. De konkurrerande hänsynen är täckning mot brus och kontroll mot kostnad: en billig skanner som ropar varg bränner det förtroende ett ambassadörsprogram tillbringade år med att bygga. Ta med er nuvarande andel falska positiva, den genomsnittliga tid ingenjörer väntar på en blockerande kontroll och listan över team som i tysthet stängt av en grind. I stora företag och myndigheter, lägg till upphandlings- och verktygsspridningsvinkeln, eftersom tio team som var och en köper sin egen skanner ger inkonsekvent täckning som ingen revisor kan stämma av.

## Sektorsperspektiv

**Startup.** Utan säkerhetsteam och med liten löptid är kultur din enda överkomliga kontroll. Gör en whiteboardgenomgång på 30 minuter för hotmodellering till vana före varje funktion som rör autentisering eller betalningar, slå på minsta behörighet och MFA överallt eftersom de inte kostar något och håll en skuldfri kanal där vem som helst kan flagga en oro. Hoppa över tung process och verktyg. De grundande ingenjörerna kan inte underhålla det, och disciplinen du bygger nu är det som låter företagsköpare lita på dig senare.

**Småföretag.** Du har ingen dedikerad säkerhetsspecialist och en snäv budget, så lita på säkra standardinställningar i de verktyg du redan köper snarare än att resa din egen pipeline. Föredra hanterade plattformar som upprätthåller MFA, patchning och minsta behörighet åt dig, och behandla säkerhet som en datahygienfråga: vet vilken känslig data du håller och vem som kan nå den. När du måste välja mellan bygg och köp, köp, eftersom en hanterad kontroll du håller aktuell slår en skräddarsydd du låter ruttna.

**Storföretag.** I skala med hundratals tjänster och tusentals ingenjörer är utmaningen konsekvens och styrning över många team. Kör ett program för säkerhetsambassadörer, standardisera hotmodelleringsnivåer knutna till CIA-klassificering och tillhandahåll mallar på upptrampad stig och automatiserade pipelinekontroller så att varje team ärver goda standardvärden. Följ åtgärds- och täckningsmått mot utgångslägen och behåll ett revisionsspår som visar varför varje system modellerades och kontrollerades som det gjordes.

**Offentlig sektor.** Upphandlingsregler, transparensskyldigheter och offentlig ansvarsskyldighet formar varje val. Principer för nolltillit och kortlivade uppgifter är ofta föreskrivna genom politik på högsta nivå, och du måste kunna visa en revisor en dokumenterad, riskbaserad motivering för var härdningsbudgeten gick. Prioritera de system som håller de känsligaste medborgarregistren först, publicera skyddsåtgärderna där allmänheten har rätt att veta och kräv att leverantörer redovisar begränsningar snarare än att acceptera ogenomskinliga svarta lådor.

## Exempel

**Startup.** En startup på tio personer har inget säkerhetsteam och ingen budget för ett, så de två grundande ingenjörerna gör hotmodellering till en whiteboardvana på 30 minuter före varje funktion som rör autentisering eller betalningar och frågar vad som kan gå fel och vem som skulle vilja att det gjorde det. De antar några grundläggande vanor som inte kostar något: minsta behörighet på varje molnroll, MFA på varje konto och en skuldfri kanal där vem som helst kan lyfta en oro utan rädsla för skuld. När de senare tar in en finansieringsrunda och företagsköpare frågar hur de hanterar säkerhet låter den tidiga kulturen dem svara ärligt i stället för att kapplöpa för att uppfinna en.

**Storföretag.** En global bank med 6 000 ingenjörer kör ett program för säkerhetsambassadörer med en utbildad ambassadör per skvadron. Ambassadörerna deltar i ett månatligt gille, genomför kvartalsutbildning och leder hotmodellering för varje ny tjänst med STRIDE. Det centrala AppSec-teamet underhåller mallar på upptrampad stig och automatiserade pipelinekontroller. Under två år föll mediantiden att åtgärda fynd med hög allvarlighetsgrad från 45 dagar till 9, och hotmodellering i designskedet fångade en auktoriseringsbrist i ett betalnings-API innan den nådde produktion, vilket undvek en trolig rapporteringspliktig incident.

**Offentlig sektor.** En nationell skattemyndighet som moderniserar äldre system antar principer för nolltillit föreskrivna av politik på högsta nivå. Varje internt tjänsteanrop autentiseras med kortlivade uppgifter och auktoriseras per begäran. Nätverkssegment ger inte längre tillit. Myndigheten hotmodellerar varje medborgarvänd tjänst mot angreppsträd med rot i "exfiltrera skattebetalares register" och "ändra en deklaration". Riskbaserad prioritering, justerad efter CIA-konsekvensnivåer, riktar härdningsbudgeten mot de system som håller de känsligaste registren först.

## Affärsnytta: motiv, ROI och TCO

Kostnaden för att bygga en säkerhetskultur är verklig: ambassadörernas tid, utbildning, verktyg och den måttliga belastningen av att göra hotmodellering och granskningar. Men den kostnaden är liten jämfört med kostnaden för att inte göra det. Det genomsnittliga större dataintrånget går på miljoner när man räknar utredning, underrättelse, åtgärd, regulatoriska viten, rättslig exponering och förlorad verksamhet. Myndighetsintrång lägger till uppdragsstörning och urholkning av offentligt förtroende som ingen faktura fullt ut fångar.

Avkastningen på säkerhetsinvesteringen kommer från tre ställen: **undvikna incidenter** (intrånget som aldrig sker), **minskad åtgärdskostnad** (defekter som rättas vid designtillfället kostar en bråkdel av dem som rättas i produktion) och **snabbare leverans** (upptrampade stigar och automatiserade kontroller låter team leverera med tillförsikt i stället för att vänta på manuell granskning). När du driver ärendet inför ledningen, ramma in säkerhet som riskhantering med en prislapp, inte som ett abstrakt gott. Visa den förväntade förlusten (sannolikhet gånger konsekvens) för de främsta riskerna, kostnaden för att minska dem och den risk som ändå återstår. Chefer finansierar riskminskning de kan mäta.

## Antimönster och fallgropar

- **Säkerhetsteater.** Kontroller som ser imponerande ut men inte minskar någon verklig risk, antagna för att tillfredsställa en revision snarare än för att skydda något.
- **Säkerhetsteamet som grind i slutet.** Att upptäcka designbrister veckan före lansering, när de är dyrast att rätta och mest sannolikt efterskänks.
- **Skuldkultur.** Att straffa ingenjören som rapporterar ett misstag garanterar att nästa misstag förblir dolt.
- **Kryssrutehotmodellering.** Att fylla i en mall ingen läser och producera dokument frikopplade från den verkliga arkitekturen.
- **Kontroller i en storlek för alla.** Att tillämpa samma tunga process på en publik webbplats och ett betalningssystem, vilket slösar insats och föder förbittring.
- **Rädsledriven prioritering.** Att jaga den sårbarhet som just nu trendar i nyheterna snarare än det som faktiskt hotar dina tillgångar.
- **Ambassadörer bara till namnet.** Att utse ambassadörer utan att ge dem tid, utbildning eller auktoritet.

## Mognadsmodell

**Nivå 1: Initiera.** Säkerhet är reaktiv och centraliserad. Granskningar sker sent om alls, och det finns ingen hotmodellering. Incidenter driver ad hoc-rättelser. Ingenjörer ser säkerhet som någon annans problem, och ingen gemensam standard finns.

**Nivå 2: Utveckla.** Ett säkerhetsteam finns och definierar standarder, men praxis är inkonsekvent över team. Viss hotmodellering sker på större projekt och ingen på andra. Grundläggande utbildning finns tillgänglig. Säkerhet uppfattas fortfarande som en grind, och att skifta åt vänster är en ambition snarare än verklighet.

**Nivå 3: Standardisera.** Säkerhetsambassadörer är inbäddade i varje team. Hotmodellering är rutin för nya tjänster, indelad i nivåer mot CIA-klassificering, och livscykeln för säker utveckling är dokumenterad och upprätthållen i hela organisationen. Riskbaserad prioritering vägleder arbetet, standarder för säker kodning och pipelinekontroller är den upptrampade standardstigen och skuldfria efterhandsgranskningar är norm.

**Nivå 4: Hantera.** Säkerhetsutfall mäts och styrs mot utgångslägen. Organisationen följer mediantid att åtgärda fynd med hög allvarlighetsgrad, täckning av hotmodeller, andelen incidenter som fångas före produktion och rapporteringsfrekvens för nästan-olyckor, uppdelat per team. Ambassadörernas auktoritet att stoppa en release är definierad och faktiskt utövad. Riskbeslut kvantifieras som sannolikhet gånger konsekvens, registreras och granskas med fast takt, så att kontrolluckor visar sig som data snarare än som överraskningar.

**Nivå 5: Orkestrera.** Säkerhet är genuint allas jobb och integrerad med leverans, risk och affärsplanering. Hotmodellering och säker design är invanda och lätta, och principer för nolltillit är i stort sett förverkligade. Mått driver kontinuerlig förbättring, organisationen lär av nästan-olyckor över team och kontroller anpassas automatiskt när hotbilden och arkitekturen förändras.

## Idéer för diskussion

1. Hur mäter ni om en säkerhetskultur faktiskt förbättras, utöver att räkna slutförd utbildning?
2. Var går den rätta gränsen mellan vad säkerhetsambassadörer hanterar och vad det centrala teamet äger?
3. Hur håller ni hotmodellering värdefull utan att låta den bli en byråkratisk kryssruta?
4. Är en fullständig nolltillitsarkitektur realistisk för er äldre egendom, och om inte, vilken är den pragmatiska delmängden?
5. Hur bör säkerhetsarbete prioriteras mot funktionsleverans när båda konkurrerar om samma ingenjörer?
6. Vilka incitament ändrar faktiskt ingenjörers beteende mot säkerhetsägarskap?

## Viktigaste punkter

- Säkerhet är en kulturell egenskap hos stora organisationer, inte en uppgift delegerad till ett team.
- Säkerhetsambassadörer skalar expertis och ägarskap över utvecklingen.
- Hotmodellering (STRIDE, PASTA, angreppsträd) blottlägger designbrister tidigt och billigt.
- En säker utvecklingslivscykel och en skifta-åt-vänster-hållning fångar defekter när de kostar minst.
- Försvar på djupet, minsta behörighet och nolltillit är de grundläggande arkitekturprinciperna.
- CIA-triaden och riskbaserad prioritering styr knapp insats dit den spelar störst roll.
- Kostnaden för att bygga säkerhetskultur är långt mindre än kostnaden för de intrång den förhindrar.

## Referenser och vidare läsning

- Adam Shostack, *Threat Modelling: Designing for Security*
- Ross Anderson, *Security Engineering: A Guide to Building Dependable Distributed Systems*
- Michael Howard and Steve Lipner, *The Security Development Lifecycle*
- Betsy Beyer et al. (Google), *Building Secure and Reliable Systems*
- National Institute of Standards and Technology, *SP 800-207: Zero Trust Architecture*
- National Institute of Standards and Technology, *Secure Software Development Framework (SSDF), SP 800-218*
- OWASP, *Threat Modelling* and *Security Champions* guidance
