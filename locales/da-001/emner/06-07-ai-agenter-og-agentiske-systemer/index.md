# 6.7 AI-agenter og agentiske systemer

## Overblik og motivation

En **AI-agent** er en [stor sprogmodel](https://en.wikipedia.org/wiki/Large_language_model) (LLM) pakket ind i en løkke: den får et mål, den kan kalde værktøjer, den beholder noget hukommelse om, hvad den har gjort, og den afgør selv sit næste skridt, til målet er nået, eller den giver op. Den løkke er hele forskellen mellem en agent og de almindelige prompt-svar-kald i kapitel 6.3. Et enkelt kald besvarer et spørgsmål. En agent læser sin e-mail, søger i en database, opretter en sag, tjekker resultatet og prøver igen. Modellen producerer ikke længere blot tekst; den vælger handlinger i jeres systemer.

Det skifte ændrer ingeniørproblemet. Når en model kun skriver ord, er et dårligt output en dårlig sætning. Når en model driver værktøjer, kan et dårligt output sende en forkert besked, slette en post eller flytte penge. Så en [intelligent agent](https://en.wikipedia.org/wiki/Intelligent_agent) forstås bedst som en ubetroet planlægger siddende inde i et betroet system, og det meste af jeres arbejde går med at afgrænse, hvad den planlægger må gøre. Dette kapitel bygger direkte på LLM-grundlaget i kapitel 6.3, tillids- og ansvarlighedsanliggenderne i kapitel 6.5 og platformspraksisserne i kapitel 6.6.

For store teams er indsatsen lige så organisatorisk som teknisk. Virksomheder vil have agenter koblet til reelle interne systemer (ticketing, økonomi, kundeposter), hvilket betyder, at agenter arver reelle adgangskontroller og reelle ændringsstyringsforpligtelser. Det offentlige tilføjer offentlig ansvarlighed: en autonom handling, der berører en borger, skal kunne forklares, overvåges og revideres bagefter. Mønstret er kraftfuldt. Udrullet uden disciplin er det en hurtig måde at automatisere fejl på.

## Grundprincipper

- En agent er en model plus en løkke, værktøjer, hukommelse og et mål. Risikoen bor i løkken, ikke i prosaen.
- Afgræns autonomi til opgaven. Giv den mindste mængde frihed, der får arbejdet gjort.
- Foretræk en fast arbejdsgang, når trinnene er kendt. Ræk kun ud efter åben autonomi, når de ikke er.
- Behandl hvert værktøj som angrebsflade, og giv det det mindste privilegium, det kan arbejde med.
- Sæt et menneske i løkken for væsentlige eller uigenkaldelige handlinger, og gør omgørelse billig.
- Evaluér på opgavesucces, ikke på hvordan udskriften læses.
- Spor hver kørsel. En handling, I ikke kan rekonstruere, er en handling, I ikke kan styre.
- Det simpleste design, der virker, er som regel det rette. Ofte er det slet ikke en agent.

## Anbefalinger

### Begynd med en arbejdsgang, tilføj kun autonomi, hvor I må

Den mest almindelige fejl er at række ud efter en autonom agent, når en fast pipeline ville række. Hvis I allerede kender trinnene (udtræk felter, validér dem, slå en post op, udarbejd et svar), så skriv det som en orkestreret arbejdsgang, hvor modellen udfylder specifikke pladser. Autonomi tjener sit brød, når stien reelt ikke kan forudbestemmes, for eksempel åben research eller triage på tværs af mange mulige værktøjer. Afgræns autonomien til opgaven: begræns antallet af trin, begræns værktøjssættet til det, dette mål har brug for, og sæt en klar stopbetingelse. En god regel er at give modellen præcis så meget frihed, som problemet kræver, og ikke en grad mere.

### Gør værktøjsbrug til kernekapaciteten, og gør den sikker

Værktøjsbrug (også kaldet funktionskald) er det, der forvandler en model til en agent. Definér hvert værktøj med et præcist skema, validér hvert argument, modellen leverer, og anvend [princippet om mindste privilegium](https://en.wikipedia.org/wiki/Principle_of_least_privilege): en skrivebeskyttet rapporteringsagent får skrivebeskyttede legitimationer, aldrig skriveadgang, den kunne misbruge. Kør værktøjer inde i en [sandbox](https://en.wikipedia.org/wiki/Sandbox_(computer_security)), så et dårligt kald ikke kan nå ud over sin sprængradius. Foretræk mange snævre enkeltformålsværktøjer frem for nogle få brede, fordi et snævert værktøj er lettere at ræsonnere om, tildele tilladelser og revidere. Det er den samme tilbageholdenhed, kapitel 6.3 opfordrer til for LLM-værktøjsbrug, gjort central.

### Brug eksplicitte ræsonnerings- og planlægningsmønstre

Agenter virker bedre, når deres tænkning er struktureret. I et ræsonner-og-handl-mønster (populariseret af ReAct-forskningen) skifter modellen mellem at ræsonnere om situationen og foretage en handling og observerer så resultatet, før den ræsonnerer igen. Til sværere mål så få modellen til at planlægge først (nedbryd i delopgaver) og derefter udføre, så I kan inspicere og endda godkende planen, før noget værktøj kører. Hold disse løkker observerbare og afbrydelige. En plan, I kan læse, er en plan, I kan stoppe.

### Hold mennesker i løkken for væsentlige handlinger

Beslut, pr. værktøj og pr. handling, om modellen må handle alene eller skal spørge først. Reversible handlinger med lav indsats (søgning, udarbejdelse) kan køre uden opsyn. Væsentlige eller uigenkaldelige (at sende ekstern kommunikation, flytte penge, ændre produktionsdata, afgøre en borgers sag) har brug for en [menneske-i-løkken](https://en.wikipedia.org/wiki/Human-in-the-loop)-port med reel autoritet til at sige nej. Design for reversibilitet, hvor I kan: foretræk at iscenesætte en ændring frem for at committe den, og gør fortryd til en førsteklasses funktion, så en fejlagtig handling koster minutter, ikke en hændelse.

### Behandl sikkerhedsmodellen som fjendtlig

Agenter udvider den angrebsflade, der er beskrevet i kapitel 4.2. Den centrale trussel er [prompt injection](https://en.wikipedia.org/wiki/Prompt_injection): ondsindede instruktioner skjult i en webside, et dokument eller en e-mail, som agenten læser og adlyder. Nært beslægtet er [confused deputy-problemet](https://en.wikipedia.org/wiki/Confused_deputy_problem), hvor en angriber narrer en privilegeret agent til at misbruge sin egen legitime adgang, for eksempel ved at eksfiltrere data gennem et værktøj, agenten har lov til at kalde. Antag at alt indhold, agenten indtager, kan være fjendtligt. Adskil betroede instruktioner fra ubetroede data, afgræns værktøjer, så en kapret agent ikke kan nå følsomme systemer, og lad aldrig rå modeloutput udløse en uigenkaldelig handling uden validering.

### Evaluér på opgavesucces, og regressionstest ikke-determinismen

Bedøm agenter på, om de udfører opgaven, ikke på om udskriften lyder klog. Byg et evalueringssæt af repræsentative mål med kontrollerbare succeskriterier (fik sagen den rette prioritet, matchede refusionen politikken), og kør det ved hver prompt-, model- eller værktøjsændring. Fordi agenter er ikke-deterministiske, beviser en enkelt kørsel lidt: kør hvert tilfælde flere gange og følg en succesrate, ikke bestået eller fejlet. Det udvider offline- og online-evalueringsdisciplinen fra kapitel 6.3 og 6.2 (maskinlæringsudvikling og MLOps) til systemer, hvis output er en sekvens af handlinger.

### Instrumentér kørsler til observerbarhed, omkostning og fejlhåndtering

I kan ikke styre, hvad I ikke kan se. Spor hver agentkørsel fra ende til anden (kapitel 6.6): målet, hvert ræsonnementstrin, hvert værktøjskald med dets argumenter og resultat, de brugte tokens og det endelige udfald. Denne sporing er jeres debugger, jeres revisionsspor og jeres omkostningsmåler på én gang. Sæt hårde budgetter på trin, tid og udgift, for en agent, der looper, kan brænde latens og penge hurtigt. Håndtér fejl eksplicit: prøv forbigående værktøjsfejl igen med backoff, men opdag løkker, hvor modellen gentager en fejlende handling, og fejl sikkert frem for at spinde i ring.

## Afvejninger: fordele og ulemper

| Valg | Fordele | Ulemper | Bedst når |
|---|---|---|---|
| Fast arbejdsgang (modellen udfylder pladser) | Forudsigelig, billig, let at teste og revidere | Stiv; går i stykker på uforudsete stier | Trinnene er kendt på forhånd |
| Autonom enkeltagent | Fleksibel; håndterer åbne mål | Sværere at kontrollere, evaluere og afgrænse | Stien kan ikke forudbestemmes |
| Multi-agent-orkestrering | Parallelisme; specialiserede roller | Koordinationsomkostning, akkumulerende fejl, højere udgift | En opgave reelt nedbrydes i uafhængige dele |
| Handling uden opsyn | Hurtig, lav gnidning | Fejl udføres uden tjek | Handlinger er reversible og har lav indsats |
| Menneske-i-løkken-port | Sikkerhed, ansvarlighed, reversibilitet | Langsommere; kræver gennemgangskapacitet | Handlinger er væsentlige eller uigenkaldelige |

Den centrale spænding er autonomi versus kontrol. Mere autonomi håndterer flere situationer, men kræver mere rækværk, mere evaluering og flere penge, og den fejler på måder, der er sværere at forudsige. Multi-agent-designs frister teams med elegance, men hver ekstra agent tilføjer koordinationsoverhead og endnu et sted, hvor en lille fejl kan akkumulere til et forkert resultat. Løs spændingen ved at begynde med den mindste autonomi, der løser problemet, og tilføje frihed kun, når en konkret opgave tvinger jer, altid parret med et tilsvarende rækværk.

## Spørgsmål til drøftelse med dit team

1. **Har denne funktion faktisk brug for en agent, eller ville en fast arbejdsgang være sikrere og billigere?** Autonomi er forførende, men de fleste jobs har kendelige trin, som en orkestreret pipeline håndterer med langt mindre risiko. For et stort team betyder det at vælge agenter som standard, at hver gruppe påtager sig evaluerings-, sporings- og sikkerhedsbyrder, et simplere design ville undgå. Tag den specifikke opgave med og spørg, om dens trin kan forudbestemmes; hvis de kan, er en agent sandsynligvis overkonstruktion. Forbehold åben autonomi til mål, hvor stien reelt varierer fra sag til sag. Svaret bør skubbe de fleste funktioner mod en arbejdsgang og efterlade et lille, bevidst sæt som ægte agenter.

2. **For hvert værktøj vores agent kan kalde, hvad er det værste, en kapret agent kunne gøre med det, og hvad forhindrer det?** Prompt injection og confused deputy-angreb vender agentens egen legitime adgang imod jer, så den rette linse er fjendtlig (kapitel 4.2). Lav en opgørelse over hvert værktøj, dets privilegieomfang og om en ondsindet instruktion smuglet ind gennem indtaget indhold kunne nå det. For virksomheder, der kobler agenter til interne systemer, er det her, mindste privilegium, sandboxing og menneskelige porte på uigenkaldelige handlinger bliver virkelige. Tag listen over værktøjer og de legitimationer, hvert holder, med. Hvis nogen væsentlig handling kan nås uden validering eller et menneskeligt tjek, er det det første, der skal rettes.

3. **Hvordan ville vi vide, at en agents succesrate faldt, når hver kørsel ser plausibel ud?** Agenter er ikke-deterministiske, så en udskrift, der læses godt, kan stadig have foretaget den forkerte handling, og én grøn kørsel beviser intet. Spørg, om I har et evalueringssæt af mål med kontrollerbare udfald, kørt mange gange pr. tilfælde for at producere en succesrate frem for en enkelt bestået. For højindsats- eller offentlige udrulninger så drøft, hvordan kørselssporinger lader jer rekonstruere præcis, hvad der skete, når noget går galt (kapitel 6.5 og 6.6). Hvis jeres eneste signal er brugerklager, er I allerede for sent på den. Svaret bør finansiere en evalueringsramme før skala, ikke efter en hændelse.

4. **Hvilke af denne agents handlinger er reelt uigenkaldelige, hvem har autoriteten til at godkende dem, og har vi gennemgangskapaciteten til at bemande den port?** Fristelsen er at lade modellen handle uden opsyn overalt, men en menneskelig port er kun reel, hvis en navngiven person med autoritet til at sige nej er tilgængelig, når agenten spørger. For et stort team bliver en godkendelseskø, ingen ejer, stille til et gummistempel, og den sikkerhed, I designede, fordamper under volumen. Tag den fulde liste over handlinger, agenten kan foretage, markér hver reversibel eller uigenkaldelig, og estimér den daglige volumen af lavsikkerhedstilfælde, der ville lande hos en gennemgår. Vej gnidningen og bemandingsomkostningen ved en port mod sprængradius af en fejl uden opsyn, og foretræk at redesigne en uigenkaldelig handling til en iscenesat, fortrydelig frem for at tilføje endnu en gennemgår. I virksomheds- og offentlige sammenhænge så bind hver væsentlig handling til en ansvarlig embedsmand og en ændringsstyringsregistrering, for en autonom handling, der berører en borger eller en kunde, som intet menneske godkendte, er præcis den fejl, en revision vil finde.

5. **Rækker vi ud efter et multi-agent-design, fordi opgaven reelt nedbrydes, eller fordi det ser elegant ud?** At dele arbejde på tværs af specialiserede agenter er forførende, men hver ekstra agent tilføjer koordinationsoverhead og endnu et sted, hvor en lille fejl akkumulerer til et forkert resultat. For en stor organisation er omkostningen ikke blot udgift og latens: et multi-agent-system er langt sværere at spore, evaluere og ræsonnere om, når det fejler, så styringsbyrden multipliceres med hver rolle, I tilføjer. Tag opgaven med og vis konkret, hvilke dele der kører uafhængigt og parallelt, og sammenlign så den målte succesrate og omkostning for en multi-agent-version mod en enkeltagent på det samme evalueringssæt. Hvis enkeltagenten vinder eller uafgjort, er det elegante design overkonstruktion. For regulerede eller offentlige udrulninger husk at hver agent i kæden er endnu en komponent, et tilsynsorgan skal kunne inspicere, så tilføjet struktur, I ikke kan begrunde, er tilføjet ansvar.

6. **Hvad er de hårde budgetter på en agents trin, tid og udgift, og hvordan ville en agent i en uendelig løkke blive fanget, før den løber op i omkostning eller latens?** En agent, der gentager en fejlende handling, kan brænde penge og tid uden varsel, så ubegrænset autonomi er en økonomisk risiko såvel som en sikkerhedsmæssig. For et stort team, der kører mange agenter, kan en enkelt dårligt opførende løkke give spidser i en cloudregning eller udtømme en hastighedsgrænse, der sulter hver anden arbejdsbyrde, hvilket gør grænser pr. kørsel til et fælles driftsanliggende frem for ét teams problem. Tag de nuværende trin-, tids- og tokenbudgetter for hver agent, den alarmering, der udløses, når en kørsel overskrider dem, og den løkkedetektion, der fejler sikkert frem for at spinde i ring, med. Vej stramme budgetter, som kan afskære en legitimt svær opgave, mod løse, der lader omkostning løbe løbsk. I virksomheds- og offentlige sammenhænge, hvor udgift skal forudsiges og begrundes, er en agent med ubegrænset omkostning en linjepost, I ikke kan forsvare i en budgetgennemgang eller en revision.

## Sektorperspektiv

**Startup.** Lever én snæver agent, der rører jeres kerneværdi, på en hostet model, med det mindste værktøjssæt, der gør jobbet, og et hårdt loft på trin og udgift. Modstå multi-agent-demoen: jeres knappe ingeniøropmærksomhed er bedre brugt på at afgrænse en enkelt agents autonomi og spore dens kørsler end på at koordinere roller, I ikke kan vedligeholde. Hold hver væsentlig handling bag en enkelt "udarbejd, send aldrig"-port, så en fejl koster et klik at fortryde, ikke en hændelse.

**Lille virksomhed.** I har ingen til at køre en evalueringsramme eller en sandbox, så foretræk agenter indlejret i værktøjer, I allerede stoler på, og slå kun den autonomi til, I kan føre opsyn med med øjnene. Behandl enhver agent, der kan sende, betale eller slette på jeres vegne, som noget, der skal holdes slukket, til et menneske bekræfter hver handling, fordi en forkert automatiseret besked til en kunde koster jer forholdet. Foretræk leverandører, der viser jer, hvad agenten gjorde, og lader jer slå automatiseringen fra.

**Stor virksomhed.** Problemet er at styre agenter på tværs af mange teams: fælles mønstre til at afgrænse autonomi, værktøjslegitimationer efter mindste privilegium, sandboxing, menneske-i-løkken-porte og sporing fra ende til anden, så ingen gruppe genopfinder rækværket. Kobl agenter til interne systemer under de samme adgangskontroller, et menneske ville holde, luk porten for uigenkaldelige handlinger bag navngivne godkendere og ændringsstyring, og styr porteføljen med succesratemålinger, budgetter pr. kørsel og adversarielle injektionstests. Standardisér sporings- og evalueringslaget, så enhver agents adfærd kan rekonstrueres og revideres.

**Offentlig sektor.** Indkøb, åbenhed og offentlig ansvarlighed afgrænser hvert valg. Hold agenter til at indsamle fakta og udarbejde, og forbehold hver afgørelse, der berører en borger, til et ansvarligt menneske, fordi ansvaret for en offentlig afgørelse ikke kan uddelegeres til en model. Log hver kørsel, så et tilsynsorgan kan se, hvilke kilder der blev konsulteret, og hvad der blev gjort, kræv at leverandører oplyser agentens værktøjer og begrænsninger, og bevis gennem et adversarielt evalueringssæt, at agenten nægter at handle ud over sit afgrænsede mandat.

## Eksempler

**Startup.** Et analysestartup på fem personer bygger en supporttriageagent. Den læser en indkommende sag, søger i dokumentationen og enten udarbejder et svar eller dirigerer sagen til et menneske, og det er hele værktøjssættet. Legitimationerne er skrivebeskyttede plus en enkelt "opret udkast"-handling, der aldrig sender uden at et menneske klikker send. Hver kørsel spores, så grundlæggerne kan se, hvorfor en sag blev dirigeret derhen, og et natligt evalueringssæt af halvtreds reelle sager kører agenten fem gange hver for at følge en dirigeringsnøjagtighedsrate. Da en konkurrents kløgtige multi-agent-demo frister dem, bliver de ved enkeltagenten, fordi deres opgave ikke nedbrydes.

**Stor virksomhed.** En bank bygger en agent til at hjælpe driftsmedarbejdere med at afstemme fejlede betalinger. Den integrerer med interne systemer under de samme adgangskontroller, en menneskelig ekspedient har, givet gennem tjenestelegitimationer efter mindste privilegium afgrænset kun til afstemning. Agenten må undersøge frit (læse hovedbøger, søge i transaktionshistorik), men enhver handling, der flytter penge eller redigerer en post, iscenesættes og kræver en navngiven menneskelig godkender, hvilket tilfredsstiller ændringsstyring. Indtagne dokumenter behandles som ubetroede for at sløve prompt injection, værktøjer kører i sandbox, og hver kørsel spores fra ende til anden til revision. Et offline evalueringssæt lukker porten for hver model- eller promptændring, og budgetter pr. kørsel begrænser trin og udgift, så en agent i en uendelig løkke ikke kan løbe op i omkostning eller latens.

**Offentlig sektor.** Et ydelsesagentur piloterer en agent til at hjælpe sagsbehandlere med at samle fakta til en sag: at hente poster, tjekke berettigelsesregler og udarbejde en opsummering. Agenturet trækker en hård linje: agenten indsamler og udarbejder, men en menneskelig sagsbehandler træffer og ejer hver afgørelse, der berører en borger, fordi ansvarlighed for offentlige afgørelser ikke kan uddelegeres til en model (kapitel 6.5). Hver kørsel logges fuldt og viser, hvilke kilder der blev konsulteret, og hvad der blev udarbejdet, så et tilsynsorgan kan revidere enhver sag. Autonomi er bevidst afgrænset til læs-og-udarbejd, værktøjer er efter mindste privilegium og i sandbox, og et adversarielt evalueringssæt bekræfter, at agenten nægter at handle ud over at indsamle fakta.

## Business case: motivation, ROI og TCO

Agenter leverer afkast ved at automatisere flertrinsarbejde, der før krævede et menneske til at klikke mellem systemer: triage, afstemning, research og rutinedrift. Værdien viser sig som arbejde udført uden et menneske i hvert trin, hurtigere gennemløbstider og medarbejdere frigjort til dømmekraftstunge opgaver. Fordi agenter bygger på eksisterende LLM'er og værktøjer, er tiden til en fungerende prototype kort, hvilket netop er grunden til, at teams overbygger.

De totale ejeromkostninger er der, hvor agenter adskiller sig fra almindelige LLM-funktioner. Oven i inferensomkostning betaler I for værktøjsintegrationerne, sandboxing- og tilladelsesrørføringen, evalueringsrammen, sporings- og observerbarhedsstakken (kapitel 6.6) og de menneskelige gennemgåere, der bemander godkendelsesportene. En agent, der går i løkke, eller en dårligt afgrænset agent tilføjer en variabel omkostning, der kan spidse uden varsel, så budgetter på trin og udgift er en del af designet, ikke en eftertanke. Omkostningen ved ikke at adoptere er langsommere drift og manuelt slid, jeres konkurrenter automatiserer. Omkostningen ved at adoptere skødesløst er en autonom handling, der sender den forkerte besked, lækker data eller træffer en uansvarlig afgørelse. Før sagen over for ledelsen ved at parre ét konkret automatiseringsmål med en konkret plan for rækværk, evaluering og menneskeligt tilsyn og ved at være ærlige om, at rækværket er det meste af omkostningen.

## Anti-mønstre og faldgruber

- **Agent, når en arbejdsgang ville række.** At påtage sig autonomiens fulde risiko for en opgave, hvis trin var kendelige.
- **For brede værktøjer og legitimationer.** Ét "gør hvad som helst"-værktøj i stedet for snævre, efter mindste privilegium.
- **Blindhed over for prompt injection.** At fodre ubetroet indhold til en agent, der holder reelle privilegier.
- **Ingen menneskelig port på uigenkaldelige handlinger.** At lade modellen sende, betale eller slette uden et tjek.
- **Multi-agent-teater.** At dele en simpel opgave på tværs af agenter og betale koordinationsomkostning uden gevinst.
- **Fornemmelsesbaseret evaluering.** At bedømme efter hvordan udskriften læses i stedet for opgavesuccesrate.
- **Ubegrænsede løkker.** Ingen grænse på trin, tid eller udgift, så en fastlåst agent brænder penge og latens.
- **Usporede kørsler.** Ingen optegnelse over, hvad agenten gjorde, hvilket efterlader jer ude af stand til at fejlsøge, revidere eller stå til ansvar.

## Modenhedsmodel

- **Niveau 1, Opstart:** Agenter prototypes ad hoc med bred værktøjsadgang og ingen grænser. Succes bedømmes ved demoer, reaktivt, efter noget går i stykker. Der er intet evalueringssæt, ingen sporing og ingen menneskelig port på væsentlige handlinger.
- **Niveau 2, Udvikling:** Nogle agenter har afgrænsede løkker og værktøjer efter mindste privilegium, og grundlæggende sporing findes, men praksis varierer fra team til team. Et manuelt evalueringssæt fanger grove regressioner i nogle få projekter, mens andre ingen har. Menneskelig godkendelse beskytter de mest åbenlyse uigenkaldelige handlinger, men dækningen er ujævn og udokumenteret.
- **Niveau 3, Standardisering:** Fælles mønstre styrer autonomi, værktøjstilladelser, sandboxing og menneske-i-løkken-porte, dokumenteret og håndhævet på tværs af hvert team. Hver væsentlig handling er lukket af en port eller valideret, agenter spores fra ende til anden, og et automatiseret evalueringssæt med succesratescoring kører ved hver ændring. Prompt injection behandles som en stående trussel med en defineret respons.
- **Niveau 4, Styring:** Agentporteføljen måles og styres mod baselines. Succesrate pr. opgave, beståelsesrate for injektionsforsvar, omkostning og trinantal pr. kørsel, menneskelig godkendelseslatens og løkke- eller fejlhændelser følges som målinger; tilbagerulnings- og dræbetærskler håndhæves på den dokumentation frem for på klager. Budgetter pr. kørsel på trin, tid og udgift overvåges, og en regression i enhver måling udløser handling før skala, ikke efter en hændelse.
- **Niveau 5, Orkestrering:** Autonomi afstemmes med opgaverisiko ved politik og justeres løbende, efterhånden som resultater kommer ind. Løbende offline- og online-evaluering knytter agentadfærd til forretningsudfald, og organisationen pensionerer, omafgrænser eller gentildeler rutinemæssigt tilladelser til agenter, efterhånden som risikobilledet skifter. Sporing, omkostningsbudgetter og revisionsspor er ensartede på tværs af porteføljen; forsvar mod injection og confused deputy testes adversarielt; ansvarlighed for autonome handlinger er klar og reviderbar.

## Idéer til drøftelse

1. Hvilke af jeres nuværende LLM-funktioner er stille blevet til agenter, og er hver enkelts autonomi blevet afgrænset med vilje?
2. For hvert agentværktøj, hvad er den billigste måde, en angriber kunne misbruge det på gennem injiceret indhold, og hvad forhindrer det?
3. Hvor har I valgt multi-agent-designs, og kan I vise, at koordinationsomkostningen betalte sig versus en enkeltagent?
4. Hvilke agenthandlinger er reelt uigenkaldelige, og kunne hver af dem redesignes til at være reversible eller iscenesatte?
5. Hvis en agent foretog en skadelig handling i morgen, kunne I så rekonstruere præcis, hvad den gjorde, og hvem der var ansvarlig?

## Vigtigste pointer

- En agent er en LLM i en løkke med værktøjer, hukommelse og et mål. Risikoen bor i løkken og værktøjerne, ikke teksten.
- Foretræk en fast arbejdsgang, når trinnene er kendt; forbehold autonomi til reelt åbne mål, og afgræns den stramt.
- Værktøjsbrug er kernekapaciteten. Giv hvert værktøj mindste privilegium, et valideret skema og en sandbox.
- Luk porten for væsentlige og uigenkaldelige handlinger bag et menneske med reel autoritet, og design til billig omgørelse.
- Behandl agenter som fjendtlige: forsvar mod prompt injection og confused deputy-misbrug (kapitel 4.2).
- Evaluér på opgavesuccesrate over mange kørsler, og spor hver kørsel til fejlsøgning, omkostningskontrol og revision (kapitel 6.5 og 6.6).
- Ofte er det rette svar slet ikke at bygge en agent.

## Referencer og videre læsning

- Shunyu Yao et al., *ReAct: Synergising Reasoning and Acting in Language Models*.
- Timo Schick et al., *Toolformer: Language Models Can Teach Themselves to Use Tools*.
- Anthropic, *Building Effective Agents* (engineering guidance on workflows versus agents).
- OWASP Foundation, *OWASP Top 10 for Large Language Model Applications* (including prompt injection and excessive agency).
- Simon Willison, writing on prompt injection and the "lethal trifecta" for AI agents.
- Norman Hardy, *The Confused Deputy* (the classic statement of the confused-deputy problem).
- Chip Huyen, *AI Engineering: Building Applications with Foundation Models*.
- Stuart Russell and Peter Norvig, *Artificial Intelligence: A Modern Approach* (intelligent agents and rational action).
