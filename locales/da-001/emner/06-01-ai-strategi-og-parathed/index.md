# 6.1 AI-strategi og parathed

## Overblik og motivation

[Kunstig intelligens](https://en.wikipedia.org/wiki/Artificial_intelligence) er gået fra forskningsnyhed til en kernefunktion, som store organisationer nu forventes at udrulle ansvarligt og i skala. For virksomheder og offentlige agenturer er det reelle spørgsmål ikke længere, om AI kan gøre noget imponerende i en demo. Det er, om en specifik investering løser et reelt problem bedre end alternativerne, kan drives sikkert i årevis og kan overleve revision, indkøb og offentlig granskning. AI-strategi er disciplinen at beslutte, hvor AI skal anvendes, hvor den skal undgås, og hvilke fundamenter I har brug for, før den første model når produktion.

For store teams hæver skala og inerti indsatsen. Et dårligt formuleret initiativ kan brænde budgetter, aflede talentfulde ingeniører og udhule tilliden hos tilsynsmyndigheder og borgere, når det fejler offentligt. Et velvalgt kan automatisere trummerum, afdække indsigt fra data, I aldrig før kunne nå, og frigøre dygtige mennesker til arbejde med højere værdi. Forskellen er sjældent selve modellen. Det kommer an på, hvor godt I formulerer problemet, hvor parate jeres data og talent er, og hvor ærlig jeres business case er.

Offentlige og regulerede sammenhænge tilføjer flere begrænsninger. Offentlige organer skal begrunde udgifter, garantere åbenhed, undgå ulovlig diskrimination og forblive ansvarlige over for folkevalgte og offentligheden. Indkøbsregler kan forbyde indlåsning hos en enkelt leverandør, kræve forklarlighed og kræve, at leverandører blotlægger modeladfærd. Behandl her compliance, reviderbarhed og udtrædelsesmuligheder som førsteklasses krav, ikke eftertanker.

## Grundprincipper

- Start fra et problem, der er værd at løse, ikke fra en teknologi, der leder efter en anvendelse.
- Foretræk den simpleste tilgang, der opfylder behovet; AI er én mulighed blandt mange og ofte ikke den bedste.
- Behandl datakundskab, talent og platformsmodenhed som forudsætninger, ikke parallelle arbejdsstrømme, der skal ordnes senere.
- Træf køb-versus-byg-beslutninger eksplicit, og genbesøg dem, efterhånden som markedet og jeres evner ændrer sig.
- Kvantificér de totale ejeromkostninger, herunder drift, overvågning og eventuel udskiftning, ikke blot licensen eller piloten.
- Design til udtrædelse fra dag ét: undgå arkitekturer, der gør det uoverkommeligt dyrt at skifte leverandør eller model.
- I regulerede og offentlige sammenhænge behandl åbenhed, indkøbsoverensstemmelse og ansvarlighed som designbegrænsninger.
- Mål omkostningen ved *ikke* at handle ved siden af omkostningen ved at handle.

## Anbefalinger

### Ram problemet ind, før du vælger en teknologi

Skriv en problemformulering på én side. Navngiv den beslutning eller opgave, I vil forbedre, den nuværende baseline, det målbare udfald, I ønsker, og hvad der sker, når systemet får det forkert. Spørg så, om problemet overhovedet passer til AI. Er der nok relevante data? Er opgaven mønsterbaseret frem for regelbaseret? Kan I tåle probabilistiske svar? Kan et menneske tjekke outputtet? Mange problemer løses bedre med deterministisk software, bedre procesdesign eller blot bedre datahygiejne. Skriv eksplicit ned, hvor AI *ikke* passer: for eksempel beslutninger, der ved lov skal kunne forklares perfekt, eller hvor omkostningen ved en sjælden fejl er katastrofal og umulig at fange.

### Brug et beslutningstræ: byg, køb, finjustér eller prompt

Bevæg jer fra billigst og hurtigst til dyrest og mest kontrolleret:

1. **Prompt en eksisterende hostet model.** Hvis en alment anvendelig model (såsom Anthropics Claude eller tilsvarende tilbud fra andre udbydere) løser problemet med omhyggelig prompting og hentning, så gør det først. Laveste omkostning, hurtigste iteration, ingen træningsinfrastruktur.
2. **Udvid med hentning eller værktøjer.** Hvis hullet er viden eller handlinger, så tilføj [retrieval-augmented generation](https://en.wikipedia.org/wiki/Retrieval-augmented_generation) (RAG), som henter relevante dokumenter ved forespørgselstidspunktet og forsyner modellen med dem som kontekst, og værktøjsbrug, før I rører modelvægte.
3. **Finjustér eller tilpas.** Hvis prompting ikke konsekvent kan opnå den nødvendige nøjagtighed, tone eller format, så [finjustér](https://en.wikipedia.org/wiki/Fine-tuning_(deep_learning)) en mindre model på jeres data: altså videretræn en fortrænet model på jeres eksempler for at specialisere den. Det køber kontrol til prisen af en [MLOps](https://en.wikipedia.org/wiki/MLOps)- (machine learning operations) pipeline.
4. **Køb et specialiseret produkt.** For veldefinerede domæner (dokumentbehandling, svindelscoring) kan et modent leverandørprodukt slå alt, I bygger.
5. **Byg fra bunden.** Forbehold træning af [fundamentmodeller](https://en.wikipedia.org/wiki/Foundation_model) (store modeller fortrænet på brede data og tilpasselige til mange opgaver) til organisationer med unikke data, dyb talentmasse og strategiske grunde. For næsten alle virksomheder og agenturer er dette det forkerte valg.

### Etablér forudsætninger for data, talent og platform

Revidér jeres data for tilgængelighed, kvalitet, mærkning, afstamning og retsgrundlag for brug. Bekræft, at I faktisk har ret til at bruge dem til AI, herunder personlige data og tredjepartsdata. Vurdér talent ærligt: I har brug for dataforskere og også ML-ingeniører, dataingeniører, produktchefer der forstår probabilistiske systemer, og gennemgåere der kan evaluere output. Før I skalerer, opstil en platformsbaseline: eksperimentsporing, et modelregister (systemet af autoritet for trænede modelversioner og deres godkendelsesstatus), overvågning og sikker serving, så hver ny anvendelse ikke genopfinder driften.

### Håndtér regulerede og offentlige sammenhænge bevidst

Inddrag indkøbs-, jura- og risikoteams tidligt. Kræv at leverandører oplyser modelproveniens, træningsdatapraksis, evalueringsresultater og kendte begrænsninger. Foretræk kontrakter, der giver portabilitet af jeres data og prompts, og undgå proprietære formater, der fanger jer. Hvor det er passende, offentliggør formålet med og sikkerhedsforanstaltningerne for offentligt vendte AI-systemer, og giv folk en kanal til at anfægte automatiserede afgørelser. Afstem til anerkendte rammeværker (se kapitel 6.5), så revisioner finder en dokumenteret, forsvarlig proces.

### Beregn totale ejeromkostninger, og beskyt mod indlåsning

Modellér hele livscyklusomkostningen: inferens eller licensering, datapipelines, menneskelig gennemgang, overvågning, gentræning, hændelsesrespons og afvikling. Sammenlign den med omkostningen ved status quo og ved alternativerne. Reducér indlåsning ved at placere modellen bag en intern grænseflade, holde prompts og evalueringsdatasæt portable og af og til teste en anden udbyder.

## Afvejninger: fordele og ulemper

| Tilgang | Fordele | Ulemper | Bedst når |
|---|---|---|---|
| Prompt hostet model | Hurtig, billig, ingen infrastruktur, let at skifte | Mindre kontrol, omkostning pr. kald, spørgsmål om datadeling | Prototyper, brede opgaver, usikre krav |
| Hentningsudvidelse | Forankrer svar i jeres data, opdaterbar | Hentningskvalitet er svær, tilføjer infrastruktur | Vidensintensive opgaver |
| Finjustér mindre model | Kontrol, lavere omkostning pr. kald i skala, on-prem-mulighed | Kræver MLOps, data og vedligeholdelse | Stabile, højvolumen, specialiserede opgaver |
| Køb et produkt | Gennemprøvet, understøttet, hurtigt til værdi | Licensomkostning, indlåsning, begrænset pasform | Veldefinerede standardproblemer |
| Byg fundamentmodel | Maksimal kontrol og differentiering | Enorm omkostning, sjældent talent, høj risiko | Næsten aldrig, uden for frontlaboratorier |

Den dominerende afvejning er kontrol versus omkostning og hastighed. Prompting giver mest hastighed og fleksibilitet, men mindst kontrol; at bygge giver mest kontrol, men kræver ressourcer, få organisationer bør bruge. De fleste store teams bør leve i midten: prompt og hent først, finjustér selektivt og køb til standardbehov. Indlåsning bytter kortsigtet bekvemmelighed for langsigtet risiko, og det betyder især noget i det offentlige, hvor flerårige udtrædelsesforpligtelser er almindelige.

## Spørgsmål til drøftelse med dit team

1. **Hvor sidder hver af vores tre øverste kandidatanvendelser på stigen prompt-så-hent-så-finjustér-så-køb-så-byg, og hvilken dokumentation ville flytte den et trin?** Det betyder noget, fordi det meste spildte AI-forbrug kommer af at starte et trin for højt: at træne en model, når omhyggelig prompting ville have virket. For et stort team forhindrer det at aftale stigen som en fælles standard, at hver gruppe genopfinder en dyr pipeline. Tag problemformuleringen på én side for hver kandidat, den nuværende baseline og en ærlig vurdering af, om hullet er viden (hentning), konsistens (finjustering) eller et løst standardproblem (køb), med. I virksomheds- og offentlige sammenhænge så tilføj indkøbs- og revisionsomkostningen for hvert trin, da en finjusteret model slæber en MLOps-byrde med sig, som et hostet kald ikke gør. Svaret bør lade jer dræbe eller nedgradere mindst ét overomfangsrigt projekt i rummet.

2. **Hvad er vores konkrete udtrædelsesplan for den leverandør eller model, vi afhænger mest af, og har vi faktisk testet den?** Indlåsning er billig at acceptere og dyr at afvikle, og i det offentlige kan I bære flerårige udtrædelsesforpligtelser, I ikke kan opfylde, hvis I aldrig har øvet. Tag listen over proprietære funktioner, I støtter jer til, om prompts og evalueringsdatasæt er portable, og hvordan modellen sidder bag en intern grænseflade (eller ikke gør), med. Signalet at holde øje med er, om nogen nogensinde har kørt jeres evalueringssuite mod en anden udbyder; hvis ikke, er jeres udtrædelsesplan et håb, ikke en plan. Hvis det ærlige svar er, at det ville tage måneder at skifte og kræve omskrivning af kernekode, så behandl det som en designdefekt, der skal rettes nu, ikke en bro, der skal krydses senere.

3. **Hvad siger et ærligt parathedsscorekort om vores dataret, og hvilke anvendelser diskvalificerer det i dag?** At springe datakundskab over er den fejl, der stille sænker piloter: modellen virker, men I havde aldrig retsgrundlaget til at bruge dataene, eller de er ikke mærkede og uden afstamning. For en stor organisation rejser personlige data og tredjepartsdata samtykke- og kontraktgrænser, der varierer efter jurisdiktion og datasæt. Tag en revision af tilgængelighed, kvalitet, mærkning, afstamning og retsgrundlag for hver kandidat med, og vær villige til at markere nogle anvendelser som blokerede, til datafundamenter findes. I regulerede og offentlige sammenhænge er et ubrugeligt retsgrundlag ikke en forsinkelse, det er et hårdt stop, og at finansiere parathedsarbejdet bør være en eksplicit linje i planen frem for en eftertanke.

4. **Hvordan ved vi, at en live AI-anvendelse faktisk virker, og hvilken dokumentation ville få os til at dræbe den?** De fleste AI-porteføljer akkumulerer zombier: piloter, der blev leveret, imponerede nogen og nu kører for evigt, uden at nogen tjekker, om de stadig tjener deres omkostning. Aftal baseline og succesmåling før lancering, og sæt så en eksplicit dræbetærskel, så beslutningen om at stoppe træffes på forhånd frem for at blive forsvaret i øjeblikket. Tag den nuværende måling, omkostningen til menneskeligt tilsyn pr. udfald og den drift, I har set siden lancering, med. For virksomheds- og offentlige porteføljer så navngiv, hvem der gennemgår hvert system efter en fast kadence, og hvem der har autoritet til at pensionere det; en anvendelse, ingen er ansvarlig for at gennemgå, er en, ingen nogensinde vil slå fra.

5. **Hvor bliver et menneske i løkken, hvad koster det tilsyn, og har vi faktisk budgetteret det?** De billigst udseende AI-anvendelser er dem, der stille antager fuld automatisering og så lækker omkostning gennem den gennemgang, rettelse og eskalering, virkeligheden tvinger tilbage. Beslut bevidst, hvilke beslutninger et menneske skal bekræfte, hvilke modellen må tage alene, og hvilke den aldrig må tage, og prissæt så den menneskelige tid, det indebærer. Tag volumenet af lavsikkerhedstilfælde, omkostningen ved et forkert svar og den nuværende eskaleringssti med. I regulerede og offentlige sammenhænge så bind hver automatiseret beslutning til en ansvarlig embedsmand og en klageadgang, for tilsyn, I ikke kan beskrive, er tilsyn, I ikke har.

6. **Har vi talentet og platformen til at drive det, vi foreslår, eller antager vi stille kapacitet, vi mangler?** Ambitiøse AI-planer fejler mindre på modellen end på de uglamourøse fundamenter: ingen til at vedligeholde pipelinen, ingen der kan evaluere output, ingen platform at udrulle på. Afstem hver kandidatanvendelse med de færdigheder og den infrastruktur, den faktisk har brug for, og vær ærlige, hvor hullet er en ansættelse, en partner eller en grund til ikke at bygge. Tag en opgørelse over, hvem der kan eje hvert system i produktion, hvilken platform det vil køre på, og hvilke evner I ville skulle købe, med. For en stor eller offentlig organisation så tilføj indkøbs- og ansættelsesledetider, da en plan, der afhænger af talent, I ikke kan rekruttere i det relevante vindue, er en plan om at underlevere.

## Sektorperspektiv

**Startup.** Hastighed og overlevelse dominerer. Vælg én snæver anvendelse, der rører jeres kerneværdi, lever den på en hostet model bag en tynd grænseflade, og sæt et hårdt loft på udgiften. Undgå at bygge infrastruktur eller træne modeller: jeres knappeste ressource er ingeniøropmærksomhed, og en finjusteret pipeline, I ikke kan vedligeholde, er et ansvar, ikke en voldgrav. Hold det billigt at skifte, så I kan følge et hurtigt bevægende marked.

**Lille virksomhed.** I har sandsynligvis ingen dataforskere og et stramt budget, så behandl AI som noget, I køber indlejret i værktøjer, I allerede bruger, ikke et program, I bemander. Ram parathed ind som et datahygiejne- og privatlivsspørgsmål frem for et maskinlæringsprojekt: vid hvilke kundedata I holder, hvad I må gøre med dem, og hvor et forkert automatiseret svar ville koste jer en kunde. Foretræk leverandører, der gør AI'en valgfri, gennemsigtig og let at slå fra.

**Stor virksomhed.** Problemet er porteføljestyring på tværs af mange teams: en fælles køb-versus-byg-stige, ensartede parathedsvurderinger og indlåsnings- og totalomkostningsanalyse, så grupper holder op med at genopfinde dyre pipelines. Budgettér MLOps- og tilsynsbyrden eksplicit, standardisér grænsefladelaget, så udbydere forbliver udskiftelige, og styr AI-anvendelser som en portefølje med klare målinger og dræbekriterier frem for en spredning af piloter.

**Offentlig sektor.** Åbenhed, indkøbsregler og ansvarlighed former hvert valg. Foretræk systemer, der citerer officielle kilder frem for at generere politik, hold et menneske ansvarligt for væsentlige afgørelser, og kræv dataportabilitet og oplysning om modelbegrænsninger i kontrakter. Offentliggør en beskrivelse i almindeligt sprog og en klageadgang, overhold eventuelle flerårige udtrædelsesforpligtelser, I underskriver, og hold AI ude af endelige vurderingsafgørelser, der skal hvile hos en ansvarlig embedsmand.

## Eksempler

**Startup.** Et planlægningsstartup på fem personer ville tilføje en "book et møde til mig"-funktion i naturligt sprog uden at trække sine to ingeniører væk fra kerneproduktet. Det valgte det mindste problem, der betød noget, at fortolke en anmodning til et foreslået tidspunkt, og leverede det med en hostet model bag en tynd intern API, så det kunne skifte udbyder senere. Teamet satte et hårdt månedligt udgiftsloft, fulgte om brugere accepterede de foreslåede tidspunkter og aftalte kun at genbesøge en finjusteret model, hvis volumen nogensinde retfærdiggjorde det ekstra arbejde.

**Stor virksomhed.** Et multinationalt forsikringsselskab ville fremskynde skadestriage. I stedet for at træne en skræddersyet model rammede det problemet snævert ind (dirigér og opsummér indkommende skader), prototypede med en hostet model plus hentning over sine policedokumenter og målte mod menneskelig håndteringstid og nøjagtighed. Først efter at have bevist værdi finjusterede det en mindre model til den skadestype med højest volumen for at skære omkostningen pr. kald. Det holdt modellen bag en intern API, så det kunne bytte udbydere, og modellerede en treårig TCO, der inkluderede menneskelig gennemgang af lavsikkerhedstilfælde.

**Offentlig sektor.** En national skattemyndighed overvejede en AI-assistent til at hjælpe medarbejdere med at besvare borgerhenvendelser. Fordi disse svar rørte juridiske forpligtelser, insisterede agenturet på åbenhed: systemet kunne kun fremvise officiel vejledning med citater, aldrig opfinde politik, og et menneske gennemgik hvert automatiseret forslag, før det gik ud. Indkøb krævede, at leverandøren oplyste modelbegrænsninger og gav dataportabilitet, og agenturet offentliggjorde en beskrivelse i almindeligt sprog af systemet og en klageadgang. Det holdt AI helt ude af endelige vurderingsafgørelser og forbeholdt dem ansvarlige embedsmænd.

## Business case: motivation, ROI og TCO

AI-strategi findes for at hjælpe jer med at undgå to spejlvendte fejl: at overinvestere i AI, der aldrig betaler sig, og at underinvestere, mens konkurrenter eller sammenlignelige agenturer trækker fra. ROI kommer fra sparet arbejdskraft, reduceret gennemløbstid, sænkede fejlrater og muliggjorte nye evner. Mål disse mod en ægte baseline, og regn fra for den reelle omkostning ved menneskeligt tilsyn, som sjældent forsvinder.

TCO skal inkludere de uglamourøse linjeposter: datapipelines, overvågning, gentræning, efterhånden som verden driver, sikkerhedsgennemgang og eventuel afvikling. En pilot, der ser billig ud, kan blive dyr, når den kører i skala i årevis. Præsentér også omkostningen ved *ikke* at adoptere: langsommere service, højere manuel omkostning og strategisk drift. Før sagen over for ledelsen med et porteføljesyn: nogle få højsikkerhedsvæddemål, klare succesmålinger, dræbekriterier for fejl og en parathedsvurdering, der viser, at data- og talentfundamenter findes. Bed ledere om at finansiere parathed eksplicit; spring det over, og I garanterer dyrt omarbejde.

## Anti-mønstre og faldgruber

- **Løsning på jagt efter et problem.** At købe AI, fordi jævnaldrende gjorde, og så jage en anvendelse.
- **At springe datakundskab over.** At lancere modeller på data, der er utilgængelige, ikke mærkede eller juridisk ubrugelige.
- **Demodrevne beslutninger.** At forpligte sig på grundlag af en poleret demo uden en evaluering af produktionskvalitet.
- **At ignorere den menneskelige løkke.** At antage fuld automatisering og underbudgettere gennemgang, hvor det meste omkostning gemmer sig.
- **Stille indlåsning.** At bygge dybt på én leverandørs proprietære funktioner uden udtrædelsesplan.
- **At undervurdere drift.** At behandle udrulning som målstregen frem for begyndelsen på en vedligeholdelsesforpligtelse.
- **Compliance som en eftertanke.** At eftermontere åbenhed og reviderbarhed efter design, til multipla af omkostningen.

## Modenhedsmodel

1. **Opstart.** Ad hoc-eksperimenter, ingen fælles strategi, beslutninger drevet af hype og individuel entusiasme.
2. **Udvikling.** Problemformulering findes for nogle projekter; en første platformsbaseline dukker op; køb-versus-byg diskuteres, men er inkonsistent.
3. **Standardisering.** En portefølje af AI-anvendelser med klare målinger, et dokumenteret beslutningstræ, parathedsvurderinger og indlåsnings- og TCO-analyse, anvendt ensartet på tværs af teams.
4. **Styring.** Porteføljen måles: parathed, ROI, TCO og omkostning til menneskeligt tilsyn følges mod baselines; dræbekriterier håndhæves på dokumentation; leverings- og kvalitetspåvirkning driver hver go/no-go-beslutning.
5. **Orkestrering.** AI-strategi er integreret med forretnings- og risikoplanlægning; parathed vedligeholdes løbende; organisationen pensionerer, erstatter og omafgrænser rutinemæssigt AI-systemer på dokumentation og genbalancerer porteføljen, efterhånden som markedet og risikobilledet skifter.

## Idéer til drøftelse

- Hvordan afgør I, hvornår et problem reelt er uegnet til AI, og hvem har autoriteten til at sige nej?
- Hvilken parathedstærskel bør lukke porten for et projekt fra pilot til produktion?
- Hvor megen indlåsning er acceptabel til gengæld for hurtigere tid til værdi?
- I det offentlige, hvordan bør åbenhedsforpligtelser forme køb-versus-byg-valget?
- Hvordan holder I TCO-estimater ærlige, når leverandører og entusiaster har incitamenter til at undervurdere dem?
- Hvem ejer AI-porteføljen, og hvordan træffes dræbebeslutninger?

## Vigtigste pointer

- Strategi begynder med et reelt problem og en ærlig baseline, ikke med en teknologi.
- Foretræk den simpleste mulighed: prompt, så hent, så finjustér, så køb, og byg sjældent fra bunden.
- Data-, talent- og platformsparathed er forudsætninger; at finansiere dem er en del af planen.
- Regulerede og offentlige sammenhænge kræver åbenhed, indkøbsoverensstemmelse og udtrædelsesmuligheder ved design.
- Modellér de fulde TCO og omkostningen ved inaktivitet, og beskyt mod leverandørindlåsning fra den første arkitekturbeslutning.

## Referencer og videre læsning

- Ajay Agrawal, Joshua Gans, and Avi Goldfarb, *Prediction Machines: The Simple Economics of Artificial Intelligence*.
- Eric Siegel, *The AI Playbook: Mastering the Rare Art of Machine Learning Deployment*.
- Andriy Burkov, *The Hundred-Page Machine Learning Book*.
- National Institute of Standards and Technology, *AI Risk Management Framework (AI RMF 1.0)*.
- Organisation for Economic Co-operation and Development, *OECD AI Principles*.
- Thomas H. Davenport, *The AI Advantage: How to Put the Artificial Intelligence Revolution to Work*.
