# 6.3 Generativ AI og LLM-applikationer

## Overblik og motivation

[Generativ AI](https://en.wikipedia.org/wiki/Generative_artificial_intelligence), og [store sprogmodeller](https://en.wikipedia.org/wiki/Large_language_model) (LLM'er) i særdeleshed, kan producere flydende tekst, kode, resuméer og struktureret data ud fra instruktioner i naturligt sprog. Det gør dem til kraftfulde byggeklodser til assistenter, søgning, dokumentbehandling og automatisering. Men de styrker kommer med en særegen risikoprofil. LLM'er er probabilistiske. De kan producere selvsikre falskheder ([hallucinationer](https://en.wikipedia.org/wiki/Hallucination_(artificial_intelligence))). De er følsomme over for, hvordan du prompter dem. Og de åbner nye angrebsflader såsom [prompt injection](https://en.wikipedia.org/wiki/Prompt_injection) (ondsindede instruktioner smuglet ind i input for at kapre modellens adfærd). At bygge pålidelige LLM-applikationer handler derfor mindre om modellen og mere om den ingeniørkunst, der omgiver den: hvordan I leverer kontekst, forankrer svar i troværdig viden, afgrænser output og evaluerer kvalitet.

For store teams kalder LLM-applikationer på nye mønstre, der adskiller sig fra både traditionel software og klassisk maskinlæring. Der er ofte intet træningstrin. I stedet formes adfærd af prompts, hentet kontekst, værktøjsdefinitioner og rækværk (kontroller ved kørsel, der afgrænser modellens input og output). Det flytter ingeniørindsatsen mod konteksthåndtering, hentningskvalitet, orkestrering og evaluering. Virksomheder, der adopterer LLM'er i skala, har brug for fælles mønstre, så hvert team ikke genopdager de samme fejlformer på den hårde måde.

Offentlige og regulerede organisationer står over for ekstra krav. En LLM, der fabrikerer en politikcitation eller lækker følsomme data, er ikke blot en fejl; den kan være en juridisk eller sikkerhedsmæssig hændelse. Disse sammenhænge har brug for forankring i autoritative kilder, streng outputvalidering, menneskeligt tilsyn for væsentlige output og klare optegnelser over, hvad systemet blev spurgt om, og hvad det producerede. Teknikkerne i dette kapitel (retrieval-augmented generation, rækværk og stringent evaluering) er det, der gør LLM'er sikre nok til at udrulle i højindsatssammenhænge. Anthropics Claude-modeller er én førende mulighed blandt flere kapable udbydere; praksisserne her gælder uanset, hvilken model I vælger.

## Grundprincipper

- Forankr modellen i troværdig viden frem for at stole på det, den har husket.
- Behandl prompts og kontekst som udviklede, versionerede artefakter, ikke kasserede strenge.
- Antag at modellen kan tage fejl eller blive manipuleret; validér output og afgræns handlinger.
- Giv kun modellen den kontekst og de værktøjer, den har brug for, ikke mere, for at reducere fejl og angrebsflade.
- Evaluér kontinuerligt med offline-testsæt, online-målinger og menneskelig dømmekraft.
- Hold mennesker i løkken for væsentlige output.
- Design til modellen som en ubetroet komponent i et betroet system.

## Anbefalinger

### Udvikl prompts og styr kontekst bevidst

Behandl prompts som kode: gem dem i versionsstyring, gennemgå ændringer og test dem mod en suite af eksempler. Strukturér hver prompt klart: rolle og opgave, begrænsninger, formatkrav og eksempler, hvor de hjælper. Behandl kontekstvinduet (den faste tekstspændvidde, modellen kan overveje på én gang) som en knap ressource. Inkluder de mest relevante oplysninger, ordn dem omtænksomt, og strip støj ud, fordi irrelevant eller overdreven kontekst forringer kvaliteten og hæver omkostningen. For applikationer med flere runder så styr samtaletilstand eksplicit, opsummér eller afkort historik for at holde jer inden for grænserne og samtidig bevare det, der betyder noget. Foretræk klare instruktioner og few-shot-eksempler (en håndfuld udarbejdede demonstrationer inkluderet i prompten) frem for omstændelige tricks, der går i stykker i det øjeblik, en model skifter.

### Forankr svar med retrieval-augmented generation (RAG)

For vidensintensive opgaver så hent relevante dokumenter fra et troværdigt korpus og forsyn modellen med dem som kontekst, og bed den svare kun ud fra det materiale og citere sine kilder. RAG holder viden aktuel uden gentræning, begrænser svar til godkendt indhold og muliggør citation og verifikation. Invester i hentningskvalitet: del dokumenter fornuftigt i bidder, vælg [embeddings](https://en.wikipedia.org/wiki/Word_embedding) (numeriske vektorrepræsentationer, der placerer lignende betydninger tæt på hinanden) egnede til jeres domæne, og tjek, om de hentede passager faktisk indeholder svaret, for et flydende svar bygget på den forkerte passage er værre end intet svar. Og når intet relevant dukker op, så få systemet til at sige det frem for at opfinde indhold.

### Byg agenter og værktøjsbrug med tilbageholdenhed

LLM'er kan kalde værktøjer (søgning, databaser, regnemaskiner, interne API'er) og kan sammensættes til agenter, der planlægger og handler over flere trin. Det tilføjer reel kapacitet, men det multiplicerer også risiko: hvert værktøj er endnu en måde, en forkert eller manipuleret model kan forårsage skade på. Definér værktøjer med præcise skemaer, validér hvert argument, anvend mindste privilegium, og kræv bekræftelse eller menneskelig godkendelse til væsentlige handlinger såsom at sende kommunikation eller flytte penge. Hold agentløkker afgrænsede, observerbare og afbrydelige. Begynd med snævert afgrænsede enkeltformålsværktøjer, før I rækker ud efter åben autonomi.

### Tilføj rækværk, og validér output

Pak modellen ind i lag af forsvar. På vej ind så filtrér og detektér prompt injection, især når ubetroet indhold (websider, brugerdokumenter) kommer ind i konteksten. På vej ud så validér struktur mod et skema, tjek påstande mod kilder, filtrér usikkert eller ikke-overensstemmende indhold, og afvis eller prøv igen, når validering fejler. For strukturerede output så parse og verificér frem for at stole på modellens formatering. Lad aldrig rå modeloutput udløse uigenkaldelige handlinger uden validering. Behandl afbødning af hallucinationer som en systemegenskab, I opnår gennem forankring, citation, validering og menneskelig gennemgang, ikke noget modellen styrer selv.

### Evaluér offline, online og med mennesker

Byg en evalueringssuite af repræsentative input med kendt-gode eller rubrik-scorede output, og kør den ved hver prompt- eller modelændring (offline-evaluering). Mål reel adfærd i produktion med målinger som opgavesucces, eskaleringsrate og brugerfeedback (online-evaluering). For subjektiv kvalitet så brug menneskelige gennemgåere og, forsigtigt, modelbaseret bedømmelse. Evaluering er sikkerhedsnettet, der lader jer ændre prompts og modeller med tillid. Uden den flyver I blindt.

## Afvejninger: fordele og ulemper

| Valg | Fordele | Ulemper | Bedst når |
|---|---|---|---|
| Ren prompting | Simpel, hurtig, billig at ændre | Begrænset forankring, kan hallucinere | Brede opgaver, lav indsats |
| RAG | Aktuel, forankret, citerbar | Hentning er svær at få rigtig | Vidensintensive, faktuelle opgaver |
| Agenter med værktøjer | Kraftfulde, kan handle | Større angrebsflade, sværere at kontrollere | Veldefineret automatisering med rækværk |
| Større, stærkere model | Bedre kvalitet og ræsonnement | Højere omkostning og latens | Komplekse eller højindsatsopgaver |
| Mindre, billigere model | Hurtig og billig | Svagere på svære opgaver | Højt volumen, simple opgaver |

Den centrale spænding er kapacitet versus kontrol og omkostning. Mere autonomi og større modeller leverer mere værdi, men de kræver mere rækværk, mere evaluering og flere penge. Forankring via RAG forbedrer troværdigheden til prisen af hentningsudvikling. Den rette balance afhænger af indsatsen: højindsatsapplikationer læner sig mod forankring, validering og menneskeligt tilsyn, selv når det koster mere.

## Spørgsmål til drøftelse med dit team

1. **Hvilken barre for nøjagtighed og forankring skal en LLM-funktion klare, før den møder offentligheden, og hvem godkender?** Et flydende svar, der citerer den forkerte kilde eller opfinder en politik, er værre end intet svar, og i det offentlige er en fabrikeret citation en juridisk hændelse, ikke en fejl. For et stort team forhindrer en eksplicit barre, at hver gruppe sætter sin egen private tærskel efter fornemmelse. Tag jeres definition af "forankret nok" med: om hver påstand skal kunne spores til en hentet, verificeret kilde, om systemet skal nægte, når hentning kommer tomhændet tilbage, og hvad jeres adversarielle evalueringssæt faktisk dækker. Signalet at holde øje med er, om nogen i øjeblikket kan levere en promptændring direkte til brugere uden en regressionskørsel. Hvis indsatsen er juridisk eller sikkerhedsmæssig, bør svaret dirigere output med højest risiko gennem en menneskelig gennemgår med reel autoritet før udgivelse.

2. **Hvilke af vores LLM-funktioner er i hemmelighed agenter, og har hvert værktøj fået mindste privilegium og en menneskelig port for uigenkaldelige handlinger?** Enhver funktion, der lader modellen kalde værktøjer eller handle over flere trin, er gået ind i agentterritorium, og hvert værktøj er endnu en måde, en forkert eller manipuleret model forårsager skade. For virksomheder, der kobler LLM'er til interne API'er, afdækker dette spørgsmål risiko, som en "simpel assistent"-etiket skjuler. Tag en opgørelse over hvert værktøj, modellen kan kalde, dets argumentvalidering, dets privilegieomfang og hvilke handlinger (at sende kommunikation, flytte penge, ændre poster) der kræver bekræftelse. Drøft, om agentløkker er afgrænsede, observerbare og afbrydelige. Svaret bør stramme omfang og tilføje menneskelige godkendelsesporte, overalt hvor en væsentlig eller uigenkaldelig handling i øjeblikket kan nås uden en.

3. **Hvordan ville vi inden for en dag vide, at vores hentningskvalitet er faldet, når et selvsikkert svar bygget på den forkerte passage ser fint ud?** RAG gør kun svar troværdige, når hentning faktisk bringer den passage frem, der indeholder svaret, og hentning rådner stille, efterhånden som dokumenter ændrer sig, bidder bliver forældede, eller embeddings driver fra jeres domæne. Fordi modellen stadig skriver flydende over dårlig kontekst, klager brugere måske ikke, før tilliden allerede er tabt. Tag jeres nuværende målinger af hentningslatens og recall, hvordan I tjekker, om hentede passager virkelig indeholder svaret, og hvordan indeksfriskhed holder trit med dokumentændringer, med. For højindsats- eller offentlige udrulninger så drøft logning af hentede kilder til revision, så I kan spore et dårligt svar til dets dårlige passage. Hvis I slet ingen hentningsevaluering har, forankrer I på tro.

4. **Behandler vi prompts, kontekst og evalueringssæt som versionerede, gennemgåede artefakter, eller som strenge spredt over notebooks og chatlogs?** Når prompts spredes på tværs af teams uversionerede og duplikerede, når en rettelse ét sted aldrig de andre, og ingen kan reproducere, hvad systemet blev bedt om at gøre sidste kvartal. For et stort team er et fælles promptregister og en regressionssuite, der kører ved hver ændring, det, der lader jer bytte en model eller redigere en instruktion uden stille at bryde en funktion to teams væk. Det modstridende træk er hastighed: ingeniører itererer hurtigst, når de indsætter en prompt og leverer, så aftal, hvor linjen går mellem hurtige eksperimenter og alt, der rører brugere. Tag, hvor jeres prompts faktisk bor i dag, om et evalueringssæt lukker porten for ændringer, og hvordan I versionerer hentningskorpusset sammen med prompten, med. I virksomheds- og offentlige sammenhænge så tilføj revisionskravet: I kan få brug for at vise præcis, hvilken prompt og hvilke kilder der producerede et givet output måneder senere, og en prompt, I ikke kan rekonstruere, er en optegnelse, I ikke kan forsvare.

5. **Når volumen vokser, hvordan kontrollerer vi inferensomkostning uden stille at forringe kvaliteten, og hvem ejer modelvalgsbeslutningen?** TCO for LLM-funktioner domineres af inferens pr. kald, og omkostninger, der ser trivielle ud i en pilot, akkumulerer hurtigt i produktionsskala og frister teams til stille at falde ned til en svagere model og håbe, at ingen lægger mærke til kvalitetsglidningen. For en stor organisation producerer det at lade hvert team vælge modeller og omkostningsgrænser efter fornemmelse både overraskelsesregninger og inkonsistent kvalitet. Den ægte afvejning er kapacitet versus omkostning og latens: en større model ræsonnerer bedre på svære opgaver, en mindre er billigere og hurtigere på simple, og caching, routing og hentningsomfang flytter alle tallet. Tag omkostning pr. løst opgave, kvalitet pr. modelniveau på jeres evalueringssæt og hvor prompt- eller kontekstoppustning blæser tokenforbruget op, med. I virksomheds- og offentlig budgettering så navngiv, hvem der godkender modelvalget og udgiftsloftet, for en omkostningspost, ingen ejer, er en, ingen kontrollerer, når trafikken tredobles.

6. **Hvilke følsomme data kan nå modellen, hvor går de data hen, og kan vi bevise, at de blev inden for grænserne?** Hver prompt, hentet dokument og værktøjsresultat kan bære personlige eller fortrolige data ind i modellen og, med en hostet udbyder, ud af jeres perimeter, og et læk her er en juridisk eller sikkerhedsmæssig hændelse, ikke en fejlsag. For et stort team, der kobler LLM'er til interne systemer, gemmer risikoen sig i rørføringen: et hentningskorpus, der inkluderer poster, en given bruger aldrig bør se, eller logs, der indfanger rå input. Spændingen er kapacitet versus eksponering, da redigering og stram afgrænsning kan sløve den funktion, I forsøger at bygge. Tag et dataflowkort over, hvad der kommer ind i konteksten, udbyderens opbevarings- og træningsvilkår og hvordan I redigerer, afgrænser og logger følsomme felter, med. I regulerede og offentlige sammenhænge så bind dette til dataresidensregler, journalopbevaringspligter og kontraktlige grænser for, hvordan en leverandør må bruge jeres data, for tilsyn, I ikke kan dokumentere, er tilsyn, I ikke har.

## Sektorperspektiv

**Startup.** Lever én snæver LLM-funktion, der rører jeres kerneværdi, bygget på en hostet model med hentning over jeres eget indhold, og hold prompts i git bag en tynd grænseflade, så I kan bytte udbyder. Kør en lille evalueringsfil af reelle spørgsmål før hver ændring, filtrér indsat brugertekst for at sløve prompt injection, og sæt et hårdt månedligt udgiftsloft. Modstå agenter og selvhosting: en ubegrænset værktøjskaldeløkke, I ikke kan overvåge, er et ansvar, ikke en demo.

**Lille virksomhed.** I har sandsynligvis ingen ML-specialist, så køb LLM-funktioner indlejret i værktøjer, I allerede bruger, frem for at bemande en bygning. Ram risikoen ind som et almindeligt spørgsmål: hvor ville et selvsikkert forkert svar koste jer en kunde, og hvem tjekker outputtet, før det går ud. Foretræk leverandører, der viser deres kilder, lader jer beholde et menneske i løkken og gør AI'en let at slå fra, når den opfører sig dårligt.

**Stor virksomhed.** Problemet er skala på tværs af mange teams: offentliggør fælles mønstre for RAG, rækværk og værktøjsskemaer, plus en fælles evalueringsramme og et promptregister, så hver gruppe holder op med at genopdage de samme fejlformer. Budgettér inferensomkostning og menneskelig gennemgang eksplicit, standardisér grænsefladelaget, så modeller forbliver udskiftelige, og styr agenter centralt med mindste privilegium, afgrænsede løkker og revisionslogning. Styr LLM-funktioner som en portefølje med målinger og dræbekriterier, ikke en spredning af piloter.

**Offentlig sektor.** Åbenhed, indkøbsregler og ansvarlighed former hvert valg. Forankr strengt i godkendte kilder med citater, nægt, når hentning kommer tomhændet tilbage, og forbyd modellen at angive lov, den ikke kan citere. Hold en ansvarlig embedsmand til at gennemgå væsentlige output, log input og hentede kilder til revision, kør et adversarielt evalueringssæt før hver udgivelse, og kræv oplysning om modelbegrænsninger og datahåndteringsvilkår i kontrakten.

## Eksempler

**Startup.** Et udviklerværktøjsstartup på tre personer tilføjede en chathjælper over sin egen dokumentation, så brugere kunne holde op med at maile grundlæggende spørgsmål. Det brugte RAG, så hvert svar citerede en specifik dokumentside, instruerede modellen i at sige "Jeg er ikke sikker, her er hvem du kan spørge", når hentning kom tomhændet tilbage, og holdt sine prompts i git. Før hver ændring kørte det prompterne mod en lille fil med reelle brugerspørgsmål for at fange regressioner, og det filtrerede brugerindsat tekst for at sløve prompt injection. Hjælperen håndterede de almindelige spørgsmål og sendte stille resten videre til grundlæggernes fælles indbakke.

**Stor virksomhed.** Et softwarefirma byggede en intern supportassistent over sin produktdokumentation. Det brugte [RAG](https://en.wikipedia.org/wiki/Retrieval-augmented_generation), så svar citerer specifikke dokumentsider, bad modellen sige "Jeg ved det ikke", når hentning fejlede, og verificerede, at hver citeret kilde faktisk fandtes. Prompts var versionsstyrede og testet mod en suite af reelle supportspørgsmål ved hver ændring. Assistenten afviste rutinesager og eskalerede alt med lav sikkerhed til menneskelige agenter, mens online-målinger fulgte løsnings- og rettelsesrater.

**Offentlig sektor.** Et offentligt agentur udrullede en LLM-assistent til at hjælpe medarbejdere med at udarbejde svar på borgerhenvendelser. Forankringen var streng: modellen kunne kun komponere svar ud fra godkendt vejledning med citater, og den var forbudt at angive politik, der ikke fandtes i de hentede kilder. En ansvarlig embedsmand gennemgik hvert udkast, før det gik ud. Inputfiltrering værnede mod prompt injection fra borgerindsendte dokumenter, output blev logget til revision, og et evalueringssæt af adversarielle og grænsetilfældeforespørgsler kørte før hver udgivelse for at bekræfte, at systemet nægtede at spekulere i juridiske anliggender.

## Business case: motivation, ROI og TCO

LLM-applikationer leverer ROI ved at automatisere sprogtungt arbejde: at besvare spørgsmål, opsummere dokumenter, udarbejde indhold og udtrække struktur fra ustruktureret tekst. Værdi viser sig som afviste sager, hurtigere udarbejdelse, mindre manuel gennemgang og nye selvbetjeningsevner. Fordi der ofte ikke er noget træningstrin, er tiden til første værdi kort, en stor tiltrækning.

TCO domineres dog af løbende inferensomkostning, hentningsinfrastruktur, evalueringspipelines, rækværkssystemer og menneskelig gennemgang. Omkostninger pr. kald løber hurtigt op i skala, og en uovervåget applikation kan drive ind i usikker eller dyr adfærd. Omkostningen ved ikke at adoptere er at sakke bagud i servicekvalitet og medarbejderproduktivitet. Omkostningen ved at adoptere skødesløst er en offentlig hallucinationshændelse eller et datalæk. Før sagen over for ledelsen ved at parre et konkret produktivitetsmål med en konkret sikkerheds- og evalueringsplan og ved at budgettere det rækværk og det menneskelige tilsyn, der gør værdien varig.

## Anti-mønstre og faldgruber

- **At stole på flydende output.** At forveksle selvsikker, velskrevet tekst med korrekt tekst.
- **RAG uden hentningsevaluering.** At antage, at hentning virker, og aldrig tjekke, om den bringer de rette passager frem.
- **Blindhed over for prompt injection.** At fodre ubetroet indhold ind i prompts uden forsvar.
- **Ubegrænsede agenter.** At lade agenter foretage væsentlige handlinger uden grænser eller menneskelig godkendelse.
- **Ingen evalueringsramme.** At ændre prompts og modeller efter fornemmelse, uden regressionstest.
- **Promptvildtvækst.** Prompts spredt, uversionerede og duplikerede på tværs af teams.
- **Overautomatisering.** At fjerne mennesker fra beslutninger, der bærer juridisk eller sikkerhedsmæssig vægt.

## Modenhedsmodel

1. **Opstart.** Ad hoc-prompting i isolerede projekter; ingen forankring, rækværk eller evaluering; prompts bor, hvor nogen indsatte dem, og hallucinationer opdages i produktion.
2. **Udvikling.** Nogle teams tilføjer RAG og promptversionering, grundlæggende outputvalidering og et lille manuelt evalueringssæt, men praksis varierer fra team til team og hviler på individuelle fortalere frem for fælles forventning.
3. **Standardisering.** Dokumenterede mønstre for RAG, rækværk, værktøjsskemaer og promptversionering er håndhævet i hele organisationen; automatiseret offline-evaluering kører ved hver prompt- eller modelændring; højindsatsflows bærer online-målinger og menneskelig gennemgang.
4. **Styring.** Porteføljen måles mod baselines: hentnings-recall, hallucinations- og afvisningsrater, dækning af forsvar mod injection, omkostning og latens pr. kald samt eskalerings- og rettelsesrater følges på dashboards; udgivelsesporte og dræbekriterier udløses på dokumentation frem for mening, og en regressionskørsel blokerer enhver ændring, der flytter en måling i den forkerte retning.
5. **Orkestrering.** Kontinuerlig offline- og online-evaluering er knyttet til forretningsudfald; forsvar mod injection, agenter og forankring er styrede og observerbare; organisationen pensionerer, justerer og omafgrænser rutinemæssigt LLM-funktioner og bytter modeller, efterhånden som kvalitet, omkostning og risiko skifter.

## Idéer til drøftelse

- Hvordan afgør I, hvilke output der kræver menneskelig gennemgang før brug?
- Hvad er jeres standard for "forankret nok", før et svar kan vises for brugere?
- Hvordan forsvarer I mod prompt injection, når ubetroet indhold må ind i konteksten?
- Hvornår er en agent sin ekstra risiko værd versus et simplere design med ét kald?
- Hvordan evaluerer I subjektiv kvalitet i skala uden at stole for meget på modelbaseret bedømmelse?
- Hvordan holder I prompts vedligeholdelige og ensartede på tværs af mange teams?

## Vigtigste pointer

- Pålidelighed kommer af ingeniørkunsten omkring modellen: kontekst, forankring, rækværk og evaluering.
- RAG forankrer svar i troværdige kilder og muliggør citation og verifikation.
- Behandl modellen som en ubetroet komponent; validér output og afgræns værktøjsbrug.
- Giv agenter mindste privilegium, afgrænsede løkker og menneskelig godkendelse til væsentlige handlinger.
- Evaluér offline, online og med mennesker kontinuerligt; det er det, der gør forandring sikker.

## Referencer og videre læsning

- Patrick Lewis et al., *Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks*.
- Jason Wei et al., *Chain-of-Thought Prompting Elicits Reasoning in Large Language Models*.
- OWASP Foundation, *OWASP Top 10 for Large Language Model Applications*.
- Chip Huyen, *AI Engineering: Building Applications with Foundation Models*.
- Anthropic, *Building Effective Agents* (engineering guidance).
- Louis-François Bouchard and Louie Peters, *Building LLMs for Production*.
