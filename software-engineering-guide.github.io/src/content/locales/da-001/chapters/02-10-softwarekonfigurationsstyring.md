# 2.10 Softwarekonfigurationsstyring

## Overblik og motivation

[Softwarekonfigurationsstyring](https://en.wikipedia.org/wiki/Software_configuration_management) (SCM) er disciplinen at identificere komponenterne i et softwaresystem, kontrollere hvordan de ændrer sig, registrere tilstanden af hver ændring og verificere, at det, du byggede og leverede, svarer til det, du havde til hensigt. Den besvarer et spørgsmål, der lyder enkelt, men bliver svært i stor skala: hvad er der præcis i denne udgivelse, hvordan kom det dertil, og hvem godkendte det? [SWEBOK](https://en.wikipedia.org/wiki/Software_Engineering_Body_of_Knowledge) behandler SCM som et grundlæggende vidensområde af en klar grund: enhver anden ingeniøraktivitet har brug for en stabil, kendt konfiguration at arbejde mod.

I et stort team er SCM bindevævet, der holder tusindvis af bevægelige dele sammenhængende. Kildekode, biblioteker, containerbilleder, infrastrukturdefinitioner, konfigurationsdata, dokumentation og testartefakter ændrer sig alle på deres eget ur, og et leveret system er én bestemt kombination af bestemte versioner af dem alle. Uden bevidst konfigurationsstyring er den kombination ukendt og kan ikke reproduceres. Du kan ikke genskabe en tidligere udgivelse, spore en fejl til den ændring, der forårsagede den, eller sige med tillid, hvad der kører i produktion.

Virksomheds- og offentlige sammenhænge hæver indsatsen. Regulerede og offentlige programmer skal vise, at ændringer var autoriserede, gennemgåede og registrerede; at et leveret build kan spores tilbage til godkendte krav og kildekode; og at intet kom ind i systemet ukontrolleret. Her er SCM lige så meget et dokumentationssystem som et ingeniørsystem. [Versionsstyring](https://en.wikipedia.org/wiki/Version_control) (kapitel 2.6) styrer kildehistorik; SCM styrer hele konfigurationen og den kontrollerede proces, hvormed den ændrer sig. Den er tæt knyttet til [infrastruktur som kode](https://en.wikipedia.org/wiki/Infrastructure_as_code) (kapitel 8.2), leveringspipelines (kapitel 8.1) og revision og sikring (kapitel 10.2).

## Grundprincipper

- Alt, der bestemmer systemets adfærd, er et [konfigurationselement](https://en.wikipedia.org/wiki/Configuration_item) under kontrol, ikke kun kildekode.
- En [baseline](https://en.wikipedia.org/wiki/Baseline_(configuration_management)) er et kendt, aftalt referencepunkt; ændringer foretages mod baselines bevidst, ikke tilfældigt.
- Ændring kontrolleres og registreres, ikke forhindres; målet er autoriseret, sporbar ændring.
- Statusregistrering betyder, at du altid kan besvare, hvad der er i en konfiguration, og hvad dens ændringshistorik er.
- Revisioner verificerer, at det byggede og leverede system svarer til den registrerede konfiguration og godkendte krav.
- Reproducerbarhed er ufravigelig: enhver udgivet version skal kunne genopbygges fra kontrollerede input.
- Automatisér identifikation, registrering og verifikation; manuel bogføring skalerer ikke og overlever ikke revision.

## Anbefalinger

### Definér SCM-processen og tildel ejerskab

Skriv en SCM-plan, der angiver, hvad der er under konfigurationskontrol, hvordan elementer identificeres, hvordan ændringer foreslås og godkendes, og hvordan status registreres og revideres. Tildel klart ejerskab, såsom en konfigurationsansvarlig eller et ansvarligt team, så SCM ikke er alles job og derfor ingens. Skalér processen efter risikoen: et lille internt værktøj har brug for let kontrol, mens et sikkerhedskritisk eller reguleret system har brug for formelle udvalg og optegnelser. Forankr planen i en anerkendt standard som IEEE 828, så revisorer og partnere kan følge den.

### Identificér konfigurationselementer og etablér baselines

List de konfigurationselementer, der bestemmer, hvordan systemet opfører sig: kildekode, afhængigheder, byggescripts, containerbilleder, infrastrukturdefinitioner, konfigurationsdata, skemaer og nøgledokumenter. Giv hvert en stabil identifikator og et versioneringsskema. Sæt baselines på meningsfulde punkter (en udgivet version, et godkendt kravsæt, et certificeret build), så du har en aftalt reference at ændre mod og vende tilbage til. En baseline er uforanderlig: når du har erklæret den, redigerer du den ikke. Du afløser den kun med en ny baseline skabt gennem ændringsprocessen.

### Kontrollér ændring gennem en defineret proces og passende udvalg

Dirigér ændringer til kontrollerede elementer gennem en defineret sti: forslag, konsekvensvurdering, godkendelse, implementering og verifikation. For elementer med højere risiko så brug et [ændringskontroludvalg](https://en.wikipedia.org/wiki/Change_control_board) (CCB), der vejer omkostning, risiko og tidsplan, før det autoriserer en ændring. Dimensionér udvalget rigtigt: en let automatisk port til rutinemæssige kodeændringer og et formelt tværfagligt CCB til ændringer, der rører baselines, grænseflader eller reguleret adfærd. Registrér hver beslutning og begrundelsen bag den, og knyt betydelige konfigurationsbeslutninger til beslutningsregistre (kapitel 1.6), så begrundelsen overlever.

### Vedligehold konfigurationsstatusregistrering

Hold en nøjagtig, forespørgselsbar optegnelse over hvert konfigurationselement: dets nuværende version, hvilken baseline det tilhører, og de ændringsanmodninger, der er anvendt på det. Denne statusregistrering er det, der lader dig besvare, når som helst, hvad en udgivelse indeholder, og hvordan den kom dertil. Generér optegnelsen automatisk fra dine registreringsværktøjer (versionsstyring, pipeline, artefaktregister) i stedet for at vedligeholde et parallelt regneark, der driver fra virkeligheden. Denne optegnelse er rygraden i sporbarhed fra krav til ændring til build til udrulning.

### Gennemfør konfigurationsrevisioner

Verificér to ting efter en regelmæssig plan. En funktionel konfigurationsrevision bekræfter, at konfigurationen yder, som dens krav angiver. En fysisk konfigurationsrevision bekræfter, at de leverede artefakter svarer til den registrerede konfiguration: at bygget kom fra den registrerede kildekode og de registrerede afhængigheder og ikke indeholder noget uforklaret. Automatisér så meget af dette, du kan: [reproducerbare builds](https://en.wikipedia.org/wiki/Reproducible_builds), artefakt-tjeksummer, software bills of materials (SBOM'er) og proveniensattestationer forvandler revision fra manuel inspektion til en løbende kontrol.

### Styr udgivelser og levering som kontrollerede begivenheder

Behandl en udgivelse som en specifik, identificeret baseline leveret gennem en gentagelig proces. Versionér dine udgivelser eksplicit, producér et manifest eller en bill of materials, der beskriver præcis, hvad der er inkluderet, og registrér afbildningen fra udgivelse til kilderevision til udrullet artefakt. Signér og tjeksum udgivne artefakter, så alle nedstrøms kan verificere deres integritet. Bind udgivelsesstyring ind i leveringspipelinen (kapitel 8.1), så fremrykning gennem miljøer i sig selv er kontrolleret, registreret og reversibel.

### Vælg og integrér SCM-værktøj

Støt dig til værktøjer, der automatiserer identifikation, kontrol, registrering og revision, frem for kun at stole på disciplin: versionsstyring til kildekode, artefakt- og billedregistre til binære filer, en uforanderlig pipeline til builds, infrastruktur som kode til miljøer og afhængigheds- og SBOM-værktøj til proveniens. Forbind dem, så en enkelt ændring flyder sporbart fra commit til udrullet udgivelse. Det, du er ude efter, er en værktøjskæde, hvor konfigurationsoptegnelsen er et biprodukt af at udføre arbejdet, ikke en separat administrativ pligt.

## Afvejninger: fordele og ulemper

| Valg | Fordele | Ulemper |
|---|---|---|
| Formelle ændringskontroludvalg | Stærk autorisation og revisionsspor; risiko vejet før ændring | Lavere gennemløb; overhead hvis anvendt på rutineændringer |
| Lette automatiske porte | Hurtigt flow; lavt overhead; skalerer til mange ændringer | Svagere for baselines med høj risiko; mindre overvejelse |
| Strenge uforanderlige baselines | Reproducerbare, reviderbare referencepunkter | Kræver disciplin og værktøj; gnidning hvis overbrugt |
| Automatiseret statusregistrering | Nøjagtig, altid aktuel optegnelse; revisionsparat | Værktøj og integration kræver investering på forhånd |
| Manuelle konfigurationsoptegnelser | Enkle at starte; intet værktøj nødvendigt | Driver fra virkeligheden; fejler i stor skala og under revision |

Den centrale afvejning er kontrol versus flow. Tung ændringskontrol giver stærk sikkerhed, men sinker leveringen. Let kontrol flyder hurtigt, men svækker sporbarheden. Svaret er ikke at vælge ét globalt; det er at lagdele kontrol efter risiko: automatisér rutineændringer gennem hurtige porte, og spar formelle udvalg og uforanderlige baselines til de elementer, hvor autorisation og reviderbarhed reelt betyder noget. Den anden afvejning er investering i værktøj på forhånd versus løbende administrative omkostninger og revisionsrisiko. Automatiseret registrering koster mere at sætte op og langt mindre at leve med.

## Spørgsmål til drøftelse med dit team

1. **Hvad hører præcis hjemme på vores liste over konfigurationselementer, og hvem ejer beslutningen, når noget nyt dukker op?** SCM virker kun, hvis listen over kontrollerede elementer svarer til det sæt af ting, der faktisk bestemmer adfærd, og på et stort system er det sæt større, end de fleste teams tror: kildekode, afhængigheder, byggescripts, containerbilleder, infrastrukturdefinitioner, skemaer, feature flags og den konfigurationsdata, der stille ændrer, hvad softwaren gør. Hvis ingen ejer listen, bliver den forældet, og det element, der tog jer ned i produktion, viser sig at være det ene, ingen tænkte på at kontrollere. Tag jeres nuværende opgørelse med til mødet og led efter adfærdsbestemmende elementer, der mangler i den. Tildel en ansvarlig ejer (en konfigurationsansvarlig eller et navngivet team), så tilføjelse af et nyt element er en bevidst beslutning, ikke et uheld, for SCM, der er alles job, er ingens job.

2. **Kan vi bevise, at et udrullet artefakt kom fra den kildekode og pipeline, vi tror, og ville det bevis overleve manipulation?** Reproducerbarhed og sporbarhed er hele pointen med SCM, og den skarpe version af spørgsmålet er, om I kan knytte den kørende binære fil tilbage til en bestemt commit og buildkørsel med dokumentation, ikke påstand. I et reguleret eller højværdisystem er dette også jeres forsvar i forsyningskæden: signerede proveniensattestationer, artefakt-tjeksummer og en software bill of materials forvandler "vi er ret sikre" til noget, en revisor eller en hændelsesansvarlig kan verificere. Tag jeres seneste udgivelse og prøv at gå den baglæns fra det udrullede artefakt til den godkendte ændring. Hvis noget led er en manuel påstand frem for et registreret, verificerbart link, er det der, en angriber eller en ærlig fejl kan slippe noget ind ubemærket, og at lukke det betyder at koble signering og proveniens ind i pipelinen, så optegnelsen er et biprodukt af levering.

3. **Kan nogen i dag redigere en udgivelse på stedet, og hvad ville det gøre ved vores evne til at stole på den?** En baseline er kun nyttig, hvis den er uforanderlig: i det øjeblik "udgivelsen" kan redigeres bagefter, kan I ikke længere reproducere den eller støtte jer til den som reference, og hver nedstrøms revision bliver arkæologi. Den klassiske fejl er konfiguration redigeret direkte i produktion eller et tag, der stille flyttes, hvilket er netop den genvej, der føles harmløs og gør en udgivelse umulig at rekonstruere senere. Tag det ærlige svar med til mødet: hvem har adgang til at ændre en udrullet baseline uden at gå gennem ændringsprocessen, og er det sket? Rettelsen er at gøre baselines reelt uforanderlige og at dirigere hver ændring gennem forslag, konsekvensvurdering, godkendelse og verifikation og lagdele stringensen, så rutineændringer flyder gennem hurtige automatiske porte, mens baseline- og regulerede ændringer går til et udvalg.

4. **Genereres vores konfigurationsstatusregistrering automatisk fra vores registreringsværktøjer, eller vedligeholdes den i hånden, og hvor langt er den drevet fra det, der faktisk er udrullet?** Statusregistrering er den optegnelse, der lader jer besvare, når som helst, hvad en udgivelse indeholder, og hvordan den kom dertil, og på et stort system er optegnelsen kun pålidelig, hvis den falder ud af arbejdet frem for at blive tastet ind i et parallelt regneark. Det modstridende træk er, at et håndholdt register føles billigt at starte og fleksibelt, mens at automatisere det betyder at integrere versionsstyring, pipelinen og artefaktregistret, så optegnelsen bliver et biprodukt af levering. Tag det register, I støtter jer til i dag, vælg tre nylige udgivelser tilfældigt og tjek, om de registrerede versioner, baselines og anvendte ændringsanmodninger svarer til, hvad værktøjet siger blev leveret. For et virksomheds- eller offentligt program er en statusoptegnelse, der afviger fra virkeligheden, ikke et ordentlighedsproblem, det er et revisionsfund, der venter på at ske, fordi en revisor, der fanger ét hul, holder op med at stole på hele redegørelsen og beder jer rekonstruere den i hånden.

5. **Er vores ændringskontrol lagdelt efter risiko, eller styrer det samme niveau af ceremoni hver ændring uanset hvad den rører?** Kontrol og flow trækker mod hinanden: et formelt ændringskontroludvalg vejer omkostning, risiko og tidsplan, før det autoriserer en ændring, men at anvende den ceremoni på en rutinemæssig kodejustering tilføjer bare forsinkelse, mens at presse en fælles baseline eller et reguleret betalingsflow gennem en hurtig automatisk port fjerner overvejelse netop, hvor I har brug for den. Fejlformerne er symmetriske, ensartet tunghed, som folk lærer at omgå, eller ensartet slaphed, der lader en højrisikoændring glide igennem uundersøgt. Tag en stikprøve af sidste kvartals ændringer sorteret efter, hvad hver rørte, og tjek, om den stringens, den fik, faktisk matchede dens risiko. I en reguleret eller offentlig sammenhæng så navngiv, hvilke elementklasser der skal nå et tværfagligt udvalg, og hvilke der må flyde gennem automatiske porte, og registrér den lagdeling eksplicit, for "vi bruger skøn" er ikke en kontrol, en revisor eller et tilsynsorgan kan verificere.

6. **Hvornår kørte vi sidst en funktionel og en fysisk konfigurationsrevision, og hvor stor en del af dokumentationen ville være en levende optegnelse frem for en rekonstruktion?** En funktionel konfigurationsrevision bekræfter, at systemet yder, som dets krav angiver, og en fysisk konfigurationsrevision bekræfter, at de leverede artefakter svarer til den registrerede konfiguration og ikke indeholder noget uforklaret; springer I dem over, stoler I på, at jeres baselines og statusregistrering er ærlige, uden nogensinde at tjekke. Spændingen er omkostning: manuelle revisioner er langsomme og smertefulde, hvilket netop er grunden til, at teams udskyder dem, og vejen ud er at automatisere kontrollerne med reproducerbare builds, artefakt-tjeksummer, software bills of materials og proveniensattestationer, så verifikation bliver løbende. Tag jeres seneste udgivelse og prøv at producere, på stedet, sporet fra krav til ændring til build til udrulning og beviset fra artefakt til kildekode. For virksomheds- og offentlige programmer er dette dokumentationsspor, hvad certificering og tilsyn kræver, så det ærlige spørgsmål er, om morgendagens revision ville blive besvaret fra optegnelser, I allerede har, eller fra en arkæologisk øvelse, I ikke har råd til.

## Sektorperspektiv

**Startup.** Hold SCM let, men reel. Læg kildekode, infrastrukturdefinitioner og konfigurationsdata i versionsstyring, og gør hver udgivelse til et tagget build produceret af én pipeline frem for et håndsamlet artefakt. Spring ændringskontroludvalg og formelle baselines over, som er overkill i jeres størrelse, men lad aldrig nogen redigere konfiguration direkte i produktion, for den ene genvej er det, der gør en udgivelse umulig at reproducere, når en kunde rammer en fejl næste tirsdag.

**Lille virksomhed.** Uden en konfigurationsansvarlig og med et stramt budget så støt dig til værktøjer, der giver dig SCM næsten gratis: en hostet versionsstyringsplatform, dens indbyggede pipeline og et artefaktregister, så konfigurationsoptegnelsen er et biprodukt frem for et job, du skal bemande. Køb denne evne indlejret i værktøjer, du allerede betaler for, i stedet for at bygge en skræddersyet proces. Brug din knappe opmærksomhed på de to vaner, der betyder mest, reproducerbare taggede udgivelser og at holde adfærdsændrende konfiguration ude af manuelle produktionsredigeringer.

**Stor virksomhed.** Problemet er ensartethed på tværs af mange teams: en fælles SCM-plan, en fælles taksonomi for konfigurationselementer, lagdelt ændringskontrol og statusregistrering genereret automatisk fra versionsstyring, artefaktregistret og pipelinen. Spar formelle ændringskontroludvalg og uforanderlige baselines til fælles platforme og regulerede flows, lad rutineændringer flyde gennem automatiske porte, og standardisér signeret proveniens og SBOM'er, så ethvert teams udgivelse kan spores, og enhver revisor kan forespørge en levende optegnelse i stedet for at bestille en rekonstruktion.

**Offentlig sektor.** Indkøbsregler, åbenhed og offentlig ansvarlighed former processen. Følg en formel SCM-plan afstemt med en anerkendt standard som IEEE 828, baseline konfigurationselementer ved kontraktlige milepæle, og dirigér hver ændring af en kontrolleret baseline gennem et udvalg, der registrerer konsekvens, beslutning og begrundelse. Kræv, at leverede artefakter kan reproduceres fra kontrollerede input, er tjeksummet og kan spores fra ende til anden fra godkendt krav til leveret build, fordi det dokumenterede dokumentationsspor er netop, hvad certificering, revision og offentligt tilsyn kræver.

## Eksempler

**Startup.** Et startup med seks medarbejdere holder sin SCM let, men reel: kildekode, infrastrukturdefinitioner og konfigurationsdata ligger alle i versionsstyring, og hver udgivelse er et tagget, versioneret build produceret af den samme pipeline frem for samlet i hånden. Da en kunde melder en fejl, der opstod sidste tirsdag, sporer de det udrullede artefakt tilbage til den præcise commit på minutter i stedet for at gætte. De springer ændringskontroludvalg og formelle baselines over, som ville være overkill i deres størrelse, men de nægter at lade nogen redigere konfiguration direkte i produktion, for den ene genvej er det, der gør en udgivelse umulig at reproducere senere.

**Stor virksomhed.** Et stort finansielt servicefirma placerer alle udrullelige artefakter, infrastrukturdefinitioner og konfigurationsdata under konfigurationskontrol. Hver udgivelse er en uforanderlig, versioneret baseline med en genereret software bill of materials, og hvert udrullet artefakt bærer en signeret proveniensattestation, der knytter det til en bestemt kilderevision og pipelinekørsel. Rutinemæssige applikationsændringer flyder gennem automatiske pipelineporte, mens ændringer af fælles platformsbaselines eller regulerede betalingsflows går til et ændringskontroludvalg. Statusregistrering genereres automatisk fra versionsstyring, artefaktregistret og pipelinen, så revisorer forespørger en levende optegnelse i stedet for at bede om en rekonstruktion.

**Offentlig sektor.** Et forsvarsprogram følger en formel SCM-plan afstemt med IEEE 828. Konfigurationselementer listes og baselines ved kontraktlige milepæle, og et ændringskontroludvalg autoriserer hver ændring af en kontrolleret baseline og registrerer konsekvens, beslutning og begrundelse. Funktionelle konfigurationsrevisioner bekræfter, at det leverede system opfylder de specificerede krav, og fysiske konfigurationsrevisioner bekræfter, at leverede artefakter præcist svarer til den registrerede konfiguration. Udgivelser kan reproduceres fra kontrollerede input, er tjeksummet og kan spores fra ende til anden, fra godkendt krav gennem ændringsanmodning til leveret build, hvilket netop er det dokumentationsspor, certificering og tilsyn kræver.

## Business case: motivation, ROI og TCO

SCM findes for at kontrollere risiko og omkostning gennem et systems liv. Afkastet kommer fra reproducerbarhed og sporbarhed: du kan genskabe enhver udgivelse, spore fejl til de ændringer, der forårsagede dem, og besvare revisionsspørgsmål fra optegnelser i stedet for arkæologi. Det skærer hændelsesdiagnosetiden, reducerer omkostningen og længden af revisioner og forebygger den dyre klasse af fejl, hvor ingen kan sige, hvad der kører, eller hvordan det genopbygges.

De totale ejeromkostninger favoriserer automatisering. Manuelle konfigurationsoptegnelser er billige at starte og stadig dyrere at vedligeholde, og de fejler netop, når du har mest brug for dem, under en hændelse eller en revision, fordi de er drevet fra virkeligheden. Automatiseret identifikation, registrering og revision koster mere på forhånd, men forvandler konfigurationsoptegnelsen til et næsten gratis biprodukt af leveringspipelinen. For at argumentere over for ledelsen, ram SCM ind som den kontrol, der gør udgivelser reproducerbare og ændringer reviderbare, og vej den mod omkostningen ved ikke-reproducerbare udgivelser, forlængede revisioner og compliance-risikoen ved ukontrolleret ændring.

## Anti-mønstre og faldgruber

- **Konfiguration ved stammeviden:** udgivelsens sande indhold bor kun i en ingeniørs hoved, ikke i nogen optegnelse.
- **Foranderlige baselines:** "udgivelsen" redigeres på stedet, så den ikke længere kan reproduceres eller stoles på som reference.
- **Ukontrolleret konfigurationsdata:** koden er versionsstyret, men den konfiguration, der ændrer dens adfærd, redigeres ad hoc i produktion.
- **Ændringskontrolteater:** et udvalg, der gummistempler alt, hvilket tilføjer forsinkelse uden reel granskning.
- **Manuel statusregistrering:** et regneark med versioner, der stille afviger fra det, der faktisk er udrullet.
- **Ikke-reproducerbare builds:** udgivelser, der ikke kan genopbygges fra kontrollerede input, så revisioner og genopbygninger bliver gætværk.
- **Usporbare udgivelser:** ingen afbildning fra udrullet artefakt tilbage til kilderevision, ændringsanmodning og godkendelse.

## Modenhedsmodel

- **Niveau 1 (Opstart):** SCM er ad hoc og reaktiv. Kun kildekode er kontrolleret; udgivelser samles i hånden; der er ingen baselines, ingen pålidelig optegnelse over, hvad der er udrullet, og ingen måde at reproducere et tidligere build.
- **Niveau 2 (Udvikling):** Grundlæggende praksis findes, men varierer fra team til team. Nogle systemer definerer konfigurationselementer og en ændringsproces og versionerer deres udgivelser, baselines findes her og der, men optegnelser er delvis manuelle, og kontrolstringensen er inkonsistent på tværs af organisationen.
- **Niveau 3 (Standardisering):** Praksis er dokumenteret og håndhævet i hele organisationen. En fælles taksonomi for konfigurationselementer, uforanderlige baselines, lagdelt ændringskontrol og statusregistrering er etableret og i vid udstrækning automatiseret; udgivelser er reproducerbare og sporbare, og revisioner understøttes af værktøj frem for af hukommelse.
- **Niveau 4 (Styring):** SCM måles og styres med data. Reproducerbarhedsrate, sporbarhedsdækning fra krav til udrullet artefakt, ændringsledetid gennem hvert kontrolniveau, hændelser med konfigurationsdrift og revisionsfund følges mod baselines og mål. Afvigelser udløser korrektion, og hver go/no-go-beslutning hviler på denne dokumentation frem for på påstand.
- **Niveau 5 (Orkestrering):** SCM forbedres løbende og er integreret i hele organisationen. Fuldt automatiseret og løbende verificeret med reproducerbare builds, SBOM'er, proveniensattestationer og levende statusregistrering er processen vævet ind i levering, sikkerhed og revision, og den tilpasser sig, efterhånden som risiko og leveringsresultater skifter, og afvikler og genafgrænser kontroller på dokumentation.

## Idéer til drøftelse

- Kan I reproducere jeres seneste udgivelse præcist fra kontrollerede input i dag, og hvor lang tid ville det tage?
- Hvilke konfigurationselementer bestemmer adfærd, men er ikke faktisk under kontrol, især konfigurationsdata og infrastruktur?
- Er jeres ændringskontrol lagdelt efter risiko, eller tilføjer den ensartet overhead eller ensartet slaphed overalt?
- Hvor bor jeres konfigurationsoptegnelse, og hvor langt er den drevet fra det, der faktisk er udrullet?
- Hvilken dokumentation kunne I producere i en revision i morgen, og hvor meget af den ville være rekonstruktion frem for optegnelse?
- Hvordan ændrer reproducerbare builds, SBOM'er og proveniens, hvad jeres revisioner kan verificere automatisk?

## Vigtigste pointer

- SCM kontrollerer hele konfigurationen (kode, afhængigheder, infrastruktur og konfigurationsdata), ikke kun kildekode.
- Baselines er uforanderlige referencepunkter; ændring autoriseres og registreres mod dem, ikke forhindres.
- Statusregistrering skal lade jer besvare, når som helst, hvad en udgivelse indeholder, og hvordan den kom dertil.
- Revisioner verificerer, at det, der blev bygget og leveret, svarer til den registrerede konfiguration og godkendte krav.
- Lagdel kontrol efter risiko og automatisér identifikation, registrering og revision, så optegnelsen er et biprodukt af levering.

## Referencer og videre læsning

- IEEE Computer Society, *SWEBOK Guide (Guide to the Software Engineering Body of Knowledge)*, Software Configuration Management knowledge area
- IEEE Std 828, *Standard for Configuration Management in Systems and Software Engineering*
- ISO/IEC/IEEE 12207, *Systems and software engineering: Software life cycle processes* (configuration management process)
- Jez Humble and David Farley, *Continuous Delivery*
- Bob Aiello and Leslie Sachs, *Configuration Management Best Practices: Practical Methods that Work in the Real World*
- NIST guidance on software supply chain security, software bills of materials (SBOM), and artifact provenance
- CNCF and open standards for build provenance and attestation (as reference frameworks)
