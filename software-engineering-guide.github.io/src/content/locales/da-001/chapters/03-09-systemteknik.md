# 3.9 Systemteknik

## Overblik og motivation

[Systemteknik](https://en.wikipedia.org/wiki/Systems_engineering) (systems engineering) er disciplinen at konstruere et helt komplekst system fra ende til anden, så alle dets dele arbejder sammen om at opfylde et reelt behov. Delene omfatter langt mere end software. Et moderne system kombinerer som regel software, hardware, mennesker, data og processer, og det skal operere i en rodet virkelig verden. Systemteknik holder alt dette afstemt gennem systemets hele liv.

Dette er forskelligt fra softwarearkitektur. Softwarearkitektur (kapitel 3.1) afgør, hvordan softwarekomponenter struktureres, og hvordan de taler med hinanden. Systemteknik sidder ét niveau højere. Den spørger, hvad systemet som helhed skal gøre, hvordan software og hardware og menneskelige operatører deler arbejdet, og hvordan du vil bevise, at det færdige virker. Dens faglige hjem er [INCOSE](https://en.wikipedia.org/wiki/International_Council_on_Systems_Engineering), International Council on Systems Engineering, og dens forankringsstandard er [ISO/IEC/IEEE 15288](https://en.wikipedia.org/wiki/ISO/IEC_15288), som definerer processerne for et systems liv.

Dette betyder noget for store virksomheds- og offentlige programmer, fordi deres systemer er store, langlivede og sikkerheds- eller missionskritiske. En forsvarsplatform, et flytrafiksystem eller en satellitkonstellation blander specialbygget hardware, tredjepartsdele, indlejret og cloud-software og menneskelige operatører, og intet enkelt team kan holde det hele i hovedet. Du bygger også ofte et [system af systemer](https://en.wikipedia.org/wiki/System_of_systems): mange uafhængige systemer, hvert nyttigt for sig, der skal samarbejde om at levere en større kapacitet.

Dette kapitel hænger sammen med softwarekrav (kapitel 2.8), grundlæggende arkitektur (kapitel 3.1), softwaremodeller og metoder (kapitel 2.12), interoperabilitet og åbne standarder (kapitel 3.8) og projektledelse (kapitel 10.6).

## Grundprincipper

- **Konstruér helheden, ikke delene.** Et system lykkes eller fejler som helhed, så at optimere ét delsystem isoleret kan gøre helheden værre.
- **Følg livscyklussen.** Et system har et liv fra første koncept til endelig pensionering. Planlæg for hele det, ikke kun bygningen.
- **Spor hvert krav.** Hvert behov bør afbildes til et krav, et designelement og en test. Hvis du ikke kan spore det, kan du ikke bevise det.
- **Styr grænseflader med vilje.** De fleste fejl sker ved grænserne mellem delene, så grænseflader fortjener eksplicit ejerskab og kontrol.
- **Verificér og validér hver for sig.** At bygge tingen rigtigt (verifikation) og at bygge den rigtige ting (validering) er forskellige spørgsmål, og du har brug for begge svar.
- **Forvent emergent adfærd.** At kombinere dele skaber adfærd, ingen enkelt del viser. Noget af det er pointen, og noget er en ubehagelig overraskelse.
- **Co-konstruér hardware og software.** Når begge er specialbygget, begrænser beslutninger i den ene den anden, så planlæg dem sammen.

## Anbefalinger

### Styr systemets fulde livscyklus

Behandl systemet som havende et helt liv, og planlæg hvert trin. En almindelig livscyklus løber: **koncept** (forstå behovet og udforsk muligheder), **krav** (angiv præcist, hvad systemet skal gøre), **design** (beslut arkitekturen og delene), **integration** (bring delene sammen), **verifikation og validering** (bevis at det virker og er det rette system), **drift** (kør og vedligehold det) og **pensionering** (afvikl det sikkert, herunder data og bortskaffelse). ISO/IEC/IEEE 15288 giver dig en procesramme for dette. Trinnene behøver ikke være et stift vandfald; du kan iterere, prototype og levere inkrementer. Pointen er, at du bevidst adresserer hvert trin, herunder de dyre senere, som tidlige planer ofte ignorerer.

### Fang interessentbehov og allokér krav med sporbarhed

Begynd fra de mennesker, der bekymrer sig om systemet: brugere, operatører, ejere, tilsynsmyndigheder og offentligheden. Indsaml deres **behov** på almindeligt sprog, og omsæt derefter disse behov til konstruerede **krav**, der er specifikke og testbare (se kapitel 2.8). Dernæst kommer **kravallokering**: at tildele hvert krav på systemniveau til et bestemt delsystem, så du ved, hvilken del der er ansvarlig for at opfylde det. Hold en **[sporbarheds](https://en.wikipedia.org/wiki/Requirements_traceability)matrix**, en levende optegnelse, der knytter hvert behov til dets krav, til det designelement, der opfylder det, og til den test, der verificerer det. Den lader dig bevise når som helst, at hvert behov er dækket, og at hver del findes af en grund.

### Styr grænseflader eksplicit

Grænseflader er der, hvor dele mødes, og hvor systemer oftest går i stykker. En grænseflade kan være et fysisk stik, en netværksprotokol, et dataformat eller en menneskelig procedure. For hver så skriv et **Interface Control Document** (ICD): en aftalt specifikation af præcis, hvordan to dele forbindes og udveksler information. Giv hver grænseflade en klar ejer på hver side. At støtte sig til fælles, offentliggjorte specifikationer frem for engangskonnektorer gør integration langt lettere, hvilket er interoperabilitetsargumentet i kapitel 3.8. Frys grænseflader tidligt, hvor du kan, for en sen ændring bølger ind i hver del, der rører den.

### Integrér, og verificér og validér derefter

**Systemintegration** kombinerer delsystemer til den fungerende helhed, som regel i trin frem for alt på én gang, så du finder problemer, mens de stadig er små. Efter integration kommer **[verifikation og validering](https://en.wikipedia.org/wiki/Verification_and_validation)** (V&V), to adskilte kontroller. **Verifikation** spørger: byggede vi systemet rigtigt, altså opfylder det sine specificerede krav? Du verificerer gennem inspektion, analyse, demonstration og test. **Validering** spørger: byggede vi det rigtige system, altså opfylder det interessenternes reelle behov i reel brug? Et system kan bestå verifikation (det opfylder specifikationen) og alligevel dumpe validering (specifikationen var forkert). Planlæg begge tidligt, og skriv krav og grænseflader, så de overhovedet kan verificeres.

### Adoptér modelbaseret systemteknik

Traditionel systemteknik producerede bjerge af dokumenter, der drev ud af trit. **[Modelbaseret systemteknik](https://en.wikipedia.org/wiki/Model-based_systems_engineering)** (MBSE) erstatter den bunke med en enkelt, fælles, formel model af systemet, hvorfra visninger og rapporter genereres. Det almindelige modelleringssprog er **[SysML](https://en.wikipedia.org/wiki/Systems_Modeling_Language)** (Systems Modelling Language), et grafisk sprog til at beskrive et systems krav, struktur, adfærd og begrænsninger. Fordi alt bor i én forbundet model, opdaterer en ændring overalt, og sporbarhed bliver en forespørgsel frem for en manuel jagt. MBSE hænger sammen med modelleringsidéerne i kapitel 2.12. Adoptér det gradvist, begyndende med de højest-risiko dele, hvor en fælles model betaler sig hurtigst.

### Anvend systemtænkning på emergent adfærd

Praktisér [systemtænkning](https://en.wikipedia.org/wiki/Systems_thinking): ræsonnér om helheden og relationerne mellem delene, ikke blot delene én ad gangen. Sådan forudser du **[emergent adfærd](https://en.wikipedia.org/wiki/Emergence)**: egenskaber, der kun opstår, når dele kombineres, og som ingen enkelt del viser. God emergens er ofte systemets formål (en sværm af droner dækker et område, ingen enkelt drone kunne). Dårlig emergens er den overraskende fejl (to sikre delsystemer interagerer og skaber en farlig tilstand). Du kan ikke teste emergens ud af et system, du aldrig modellerede, så brug simulering og struktureret fareanalyse til at finde den før drift.

### Co-konstruér hardware og software

Når et system inkluderer specialbygget hardware, så konstruér hardwaren og softwaren sammen, en praksis kaldet **[hardware/software co-design](https://en.wikipedia.org/wiki/Hardware/software_co-design)**. Beslutninger binder hinanden: hardwaren sætter timing-, hukommelses- og strømgrænser, softwaren skal leve inden for, og softwarens behov former, hvad hardwaren skal levere. Lange hardwareledetider driver også tidsplanen. Beslut tidligt, hvilke funktioner der bor i hardware, og hvilke i software, og genbesøg den opdeling, efterhånden som begrænsninger opstår.

## Afvejninger: fordele og ulemper

| Tilgang | Fordele | Ulemper / omkostning |
|---|---|---|
| Fuld systemteknisk stringens | Færre sene overraskelser, stærk sporbarhed, sikrere og reviderbar | Høj omkostning på forhånd, langsommere start, tung proces |
| Let / kun-software-tilgang | Hurtig, billig, fleksibel til lille omfang | Bryder sammen på store tværfaglige systemer, overser grænseflader og emergens |
| Modelbaseret (MBSE) | Én sandhedskilde, let sporbarhed, ensartede visninger | Omkostning til værktøj og uddannelse, kulturændring, indlæringskurve |
| Dokumentbaseret systemteknik | Velkendt, lav værktøjsomkostning, let at dele | Dokumenter driver ud af trit, sporbarhed er manuel og fejlbehæftet |

Den centrale afvejning er stringens versus hastighed. Fuld systemteknik lægger indsats på forhånd i koncept-, krav- og grænsefladearbejde. Den indsats betaler sig mange gange på store, langlivede, sikkerhedskritiske systemer, hvor en fejl fundet i drift kan koste tusindvis af gange mere end den samme fejl fundet i krav. På et lille, kortlivet, kun-software-produkt er den stringens overkill. Afstem vægten af din proces efter systemets størrelse, levetid og risiko. Fejlformen er at anvende engangsprojektvaner på et system, der vil køre i tredive år og bære reel risiko.

## Spørgsmål til drøftelse med dit team

1. **Hvor har I bygget præcis det, specifikationen krævede, og alligevel leveret det forkerte system, og hvad ville have fanget det?** Verifikation (byggede vi det rigtigt) og validering (byggede vi det rigtige) besvarer forskellige spørgsmål, og et system kan bestå hver verifikationstest, mens det dumper validering, fordi selve specifikationen var forkert. På store programmer bliver de to slået sammen til "test", så ingen validerer mod reelle operatørbehov før sent, når en rettelse koster tusindvis af gange mere end en kravændring. Tag et tidligere eksempel med, hvor det leverede system opfyldte sine krav, men missede det faktiske behov, og spørg hvilken valideringsaktivitet (en simulering med rigtige operatører, en tidlig prototype i marken) der ville have afsløret det tidligere. Planlæg begge kontroller fra starten, og skriv krav og grænseflader, så de overhovedet kan verificeres. Distinktionen afgør, hvor I bruger knap gennemgangsindsats.

2. **Hvordan jager I dårlig emergent adfærd, før systemet er i drift, ikke efter?** At kombinere sikre delsystemer kan skabe farlige tilstande, ingen enkelt del udviser, og I kan ikke teste emergens ud af et system, I aldrig modellerede. For et sikkerhedskritisk eller missionskritisk program er den overraskende interaktion den, der skader nogen eller fejler missionen, så den skal findes før live drift. Tag jeres tilgang til at modellere helheden med (simulering, struktureret fareanalyse, en SysML-model der fanger interaktioner) og spørg, hvilke adfærdsmønstre på tværs af delsystemer I faktisk har udforsket versus antaget væk. God emergens er ofte systemets formål og værd at designe mod; dårlig emergens er den fejl, I må konstruere mod. Hvis jeres eneste integrationsstrategi er at koble delene sammen og se, hvad der sker, planlægger I at opdage emergens i produktion.

3. **Hvornår skal de hardwarebeslutninger med lang ledetid fryses, og hvordan driver den deadline jeres softwaretidsplan?** Når et system inkluderer specialbygget hardware, skal de to co-konstrueres: chippen sætter timing-, hukommelses- og strømlofter, softwaren lever inden for, og hardwareledetider dominerer ofte hele tidsplanen. Teams, der behandler software som adskillelig, optimerer lokalt og kolliderer så med hardwarebegrænsninger ved integration og taber måneder. Tag hardwareledetiderne og datoen med, hvor hardware/software-funktionsopdelingen skal besluttes, og genbesøg den opdeling, efterhånden som begrænsninger opstår, frem for at fryse den blindt. Jo tidligere I beslutter, hvilke funktioner der bor i silicium, og hvilke i software, desto færre dyre omvendinger står I over for. Grænsefladerne mellem de to fortjener et Interface Control Document og en ejer på hver side, fordi en sen ændring dér bølger gennem alt, der rører den.

4. **Kan I spore ét enkelt interessentbehov hele vejen til kravet, designelementet og den test, der beviser det, og hvem holder det link i live?** Sporbarhed er det, der lader jer vise når som helst, at hvert behov er dækket, og hver del findes af en grund, men på et stort program rådner matricen i det øjeblik, ingen ejer den. Det modstridende træk er reelt: ingeniører oplever sporbarhed som bureaukratisk overhead, og en matrice vedligeholdt i hånden driver ud af dato hurtigere end designet ændrer sig. Tag en reel tråd fra et nuværende program med og prøv at gå den fra ende til anden i rummet, fra et navngivet interessentbehov, til det allokerede krav, til det delsystem og designelement, der opfylder det, til verifikationstesten, og notér hvor kæden knækker. Beslut, hvem der ejer matricen, og om den bør bo i en model, hvor sporbarhed er en forespørgsel frem for en manuel jagt. For virksomheds- og offentlige programmer er matricen også det revisionsartefakt, tilsynsmyndigheder og anskaffelsesmyndigheder kræver, så en knækket kæde gør mere end at sinke ingeniørarbejdet; den kan standse certificering eller betaling.

5. **Er en modelbaseret tilgang værd at betale for værktøj og kultur, eller ville den blive dyr hyldevare?** Dokumentbaseret systemteknik er velkendt og billig at udstyre med værktøj, men dens dokumenter driver ud af trit, og dens sporbarhed er manuel og fejlbehæftet; MBSE erstatter bunken med én forbundet model, til prisen af værktøj, uddannelse og en reel kulturændring. Begge ekstremer er dyre: spring MBSE over på et stort tværfagligt program, og I betaler i integrationsoverraskelser, adoptér det uden disciplinen til at holde modellen aktuel, og den rådner til hyldevare, værre end ingen model. Tag en ærlig aflæsning af jeres værktøjsmodenhed med, hvem på teamet der faktisk kan forfatte og vedligeholde en SysML-model, og hvilket ene højrisiko-delsystem der kunne pilotere tilgangen, hvor en fælles model betaler sig hurtigst. Beslut gradvist frem for at påbyde hele organisationen på én gang. For et stort virksomheds- eller offentligt program med mange leverandører så vej, om en fælles model er den eneste realistiske måde at holde krav, grænseflader og tests ensartede på tværs af konsulenter, der ellers udveksler forældede dokumenter.

6. **Finansierer jeres livscyklusplan seriøst drift og pensionering, eller stopper den stille ved lancering?** De trin, der dominerer et langlivet systems totale omkostning, at drive det i årtier og afvikle det sikkert, er dem, tidlige planer rutinemæssigt ignorerer, fordi presset altid er at levere. Det modstridende hensyn er, at penge og opmærksomhed er knappest netop, når disse senere trin føles fjernest, så drift, vedligeholdelse, datamigrering og bortskaffelse udskydes, til de bliver en dyr, risikabel panik. Tag den nuværende livscyklusplan med og tjek, om den navngiver ejere, budgetter og udgangskriterier for drift og pensionering, eller om den behandler lancering som målstregen. Spørg hvad der sker med dataene og hardwaren ved levetidens udløb, og hvem der betaler for årene med vedligeholdelse imellem. For virksomheds- og offentlige systemer, der skal køre i tyve eller tredive år og så pensioneres under offentlig granskning, kan en uplanlagt afvikling bryde regulatoriske, miljømæssige eller journalopbevaringsforpligtelser, så pensionering hører hjemme i planen og budgettet fra den første konceptgennemgang.

## Sektorperspektiv

**Startup.** Et lille team kan ikke køre et formelt systemteknisk program og bør ikke prøve, men det kan stadig behandle firmware, app og cloud som ét system frem for tre separate projekter. Skriv ét kort grænsefladedokument, der fastlåser hvordan delene taler sammen, hold en simpel tabel, der knytter hvert kundebehov til den del, der opfylder det, og spring den tunge proces over. Din knappeste ressource er ingeniørernes opmærksomhed, så brug kun sporbarhedsindsats, hvor en forkert antagelse ved en grænse stille ville ødelægge produktet i marken.

**Lille virksomhed.** Uden en dedikeret systemingeniør og med et stramt budget så støt dig til offentliggjorte standarder og købte delsystemer frem for skræddersyet integration, du selv skal designe og verificere. Foretræk leverandører, der eksponerer klare grænsefladespecifikationer, så delene passer uden en specialkonnektor, du skal eje for evigt. Ram køb-versus-byg-valget ind omkring, hvilke grænseflader du realistisk kan kontrollere og verificere gennem produktets liv, og køb resten.

**Stor virksomhed.** I stor skala er problemet ensartethed på tværs af mange teams og leverandører: en fælles livscyklusproces afstemt med ISO/IEC/IEEE 15288, et Interface Control Document og en navngiven ejer for hver leverandørgrænse og sporbarhed fra ende til anden, så en komponentændring ikke udløser en programdækkende panik. Invester i MBSE, hvor en fælles model holder krav, grænseflader og tests afstemt på tværs af konsulenter. Styr processen, så verifikation og validering forbliver adskilte, og hvert krav er allokeret til en ansvarlig del.

**Offentlig sektor.** Indkøbsregler, åbenhed og offentlig ansvarlighed former hvert valg. Specificér systemteknisk proces, sporbarhed og V&V-dokumentation i kontrakten, kræv at leverandører afleverer grænsefladekontroldokumenter og livscyklusartefakter, I kan revidere, og forbehold sikkerheds- og missionsvalidering til uafhængig gennemgang med rigtige operatører før enhver live omstilling. Planlæg og finansiér drift og pensionering eksplicit, fordi et offentligt program er ansvarligt for hele livscyklussen, herunder sikker afvikling og journalopbevaring.

## Eksempler

**Startup.** Et hardwarestartup med fire medarbejdere, der bygger en forbundet sensor, har ikke råd til et formelt systemteknisk program, men behandler stadig produktet som ét system af firmware, en mobilapp og en cloud-backend frem for tre separate projekter. De skriver ét kort grænsefladedokument, der fastlåser, hvordan enhed, app og server taler sammen (beskedformater, enheder, fejlkoder), og holder en simpel tabel, der knytter hvert kundebehov til den del, der opfylder det. Da en billigere sensorchip tvinger en firmwareændring, viser den fælles grænseflade straks, hvad app og backend må justere, så et komponentskift ikke stille ødelægger produktet i marken.

**Stor virksomhed.** En global bilproducent bygger en ny elbilsplatform: et system af software (batteristyring, førerassistance, infotainment), hardware (motorer, sensorer, chips) og menneskelige faktorer, plus mange leverandører, der hver leverer delsystemer. Virksomheden kører et systemteknisk program. Interessentbehov fodrer allokerede krav, hver leverandørgrænseflade har et Interface Control Document, og en SysML-model knytter krav til design til tests. Da en battericelleleverandør ændrer en komponent, viser sporbarhedsmodellen præcis, hvilke krav, grænseflader og tests der er berørt, så ændringen indeholdes i stedet for at udløse en programdækkende panik.

**Offentlig sektor.** En national flynavigationsmyndighed moderniserer sit flytrafikstyringssystem, et sikkerhedskritisk system af systemer, der spænder over radarer, flyveledelsesarbejdsstationer, kommunikation og software, drevet døgnet rundt. Programmet følger ISO/IEC/IEEE 15288 gennem hele livscyklussen. Verifikation beviser, at hvert delsystem opfylder sin specifikation, og validering gennem simulering med rigtige flyveledere beviser, at det integrerede system understøtter sikker drift, før nogen live trafik afhænger af det. Stringent V&V lader myndigheden skifte over i trin, med tilbagefald ved hvert skridt, fordi en utestet emergent fejl her er en offentlig sikkerhedshændelse.

## Business case: motivation, ROI og TCO

Motivationen er, at fejl bliver eksponentielt dyrere, jo senere du finder dem. En kravfejl fanget under kravfasen koster næsten intet at rette. Den samme fejl fanget i drift kan koste tusindvis af gange mere, og på et sikkerhedskritisk system kan den koste liv, tilbagekaldelser eller en fejlslagen mission. Systemteknik flytter fejlopdagelse ind i de billige tidlige trin.

For **return on investment** (ROI, værdi opnået sammenlignet med omkostning brugt) er gevinsten undgået omarbejde, færre integrationsfejl og programmer, der rammer tidsplan og budget i stedet for at overskride. Brancheundersøgelser af store programmer finder gentagne gange, at stærk systemteknisk indsats korrelerer med mindre overskridelser. For **totale ejeromkostninger** (TCO, den fulde livstidsomkostning ved at bygge, drive og pensionere et system) tager systemteknik højde for drifts- og pensioneringstrinnene, der dominerer den langsigtede omkostning, men som ad hoc-projekter ignorerer. At designe til vedligeholdelighed, grænseflader og bortskaffelse fra begyndelsen sænker omkostningen ved de årtier, systemet bruger i drift. Se projektledelse (kapitel 10.6).

## Anti-mønstre og faldgruber

- **Stort design på forhånd uden iteration.** At behandle livscyklussen som et stift envejs vandfald, så du først lærer, at kravene var forkerte, efter du har bygget alt.
- **Krav uden sporbarhed.** En bunke krav, ingen knytter til design eller tests, så du ikke kan bevise dækning eller retfærdiggøre nogen del.
- **At ignorere grænseflader.** At antage at delsystemer bare vil passe sammen og så miste måneder ved integration til grænseuoverensstemmelser, ingen ejede.
- **Verifikation uden validering.** At bevise at systemet opfylder sin specifikation, mens man aldrig tjekker, at specifikationen matchede reelle behov, og så levere det forkerte system.
- **At behandle software som adskilt.** Softwareteams, der optimerer lokalt, mens de ignorerer hardwarebegrænsninger, timing og menneskelige operatører.
- **MBSE som hyldevare.** At bygge en model én gang og så lade den rådne ud af trit, så den bliver værre end ingen model.
- **At springe pensioneringsplanlægning over.** Ingen plan for afvikling, datamigrering eller bortskaffelse, så levetidens udløb bliver en dyr, risikabel panik.

## Modenhedsmodel

**Niveau 1: Opstart.** Systemteknik er ad hoc og reaktiv. Krav lever i spredte dokumenter, grænseflader opdages ved integration, og verifikation er, hvad testning der nu tilfældigvis bliver gjort. Store programmer overskrider rutinemæssigt og overrasker teamet sent.

**Niveau 2: Udvikling.** Grundlæggende praksis findes på større programmer. Krav fanges og baselines, nøglegrænseflader har kontroldokumenter, og der er en verifikationsplan. Praksis er inkonsistent mellem teams og afhænger af enkeltpersoner frem for en fælles metode.

**Niveau 3: Standardisering.** Systemteknik er en dokumenteret disciplin for hele organisationen afstemt med ISO/IEC/IEEE 15288 og håndhævet på tværs af teams. Hele livscyklussen planlægges, sporbarhed vedligeholdes fra ende til anden, grænseflader kontrolleres formelt, og verifikation og validering er adskilte og planlagte. MBSE bruges på komplekse programmer.

**Niveau 4: Styring.** Systemteknik måles og styres med data. Organisationen følger målinger mod baselines: kravvolatilitet og sporbarhedsdækning, grænsefladefejl fundet ved integration, bestå-rater for verifikation og validering og fejllækage pr. livscyklustrin (hvor mange fejl der slipper ud af hvert trin for at blive fanget senere til højere omkostning). Gennemgange styrer programmer efter disse tal, og tærskler udløser korrigerende handling frem for brandslukning bagefter.

**Niveau 5: Orkestrering.** Systemteknik forbedres løbende og er integreret i hele organisationen. En levende MBSE-model er den enkelte sandhedskilde, sporbarhed er automatiseret, simulering forudsiger emergent adfærd før bygning, og målinger fra tidligere programmer føder det næste. Hardware og software co-konstrueres som en selvfølge, og processen tilpasser sig, efterhånden som programmer, leverandører og risici skifter.

## Idéer til drøftelse

- Hvor går grænsen mellem systemteknik og softwarearkitektur i jeres organisation, og hvem ejer rummet imellem?
- Kan I på jeres største program spore ét enkelt interessentbehov hele vejen til den test, der verificerer det? Hvis ikke, hvad ville der skulle til?
- Hvilke af jeres seneste fejl skete ved en grænseflade, og hvem ejede den?
- Ville MBSE betale sig for jer, eller ville det blive dyr hyldevare, givet jeres kultur og værktøj?
- Adresserer jeres livscyklusplan seriøst drift og pensionering, eller stopper den stille ved lancering?

## Vigtigste pointer

- Systemteknik konstruerer hele systemet (software, hardware, mennesker og processer) fra ende til anden og er adskilt fra softwarearkitektur.
- Planlæg hele livscyklussen, fra koncept over krav, design, integration, V&V, drift og pensionering.
- Spor hvert behov til et krav, et designelement og en test, og allokér hvert krav til en ansvarlig del.
- Styr grænseflader eksplicit med klart ejerskab og kontroldokumenter, fordi grænser er, hvor systemer går i stykker.
- Verifikation (byggede det rigtigt) og validering (byggede det rigtige) er forskellige kontroller, og I har brug for begge.
- Brug MBSE og SysML til én forbundet sandhedskilde, og brug systemtænkning til at forudse emergent adfærd.
- Afstem vægten af din proces efter systemets størrelse, levetid og risiko.

## Referencer og videre læsning

- INCOSE, *INCOSE Systems Engineering Handbook: A Guide for System Life Cycle Processes and Activities*
- ISO/IEC/IEEE 15288, *Systems and Software Engineering: System Life Cycle Processes*
- ISO/IEC/IEEE 29148, *Systems and Software Engineering: Requirements Engineering*
- Sanford Friedenthal, Alan Moore, and Rick Steiner, *A Practical Guide to SysML: The Systems Modelling Language*
- NASA, *NASA Systems Engineering Handbook* (NASA/SP-2016-6105)
- Andrew P. Sage and William B. Rouse, *Handbook of Systems Engineering and Management*
- Dennis M. Buede and William D. Miller, *The Engineering Design of Systems: Models and Methods*
- Donella H. Meadows, *Thinking in Systems: A Primer*
- Eberhardt Rechtin and Mark W. Maier, *The Art of Systems Architecting*
- U.S. Department of Defence, *Defence Acquisition Guidebook* (systems engineering guidance)
