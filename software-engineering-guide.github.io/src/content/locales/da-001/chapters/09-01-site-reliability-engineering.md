# 9.1 Site reliability engineering

## Overblik og motivation

[Site reliability engineering](https://en.wikipedia.org/wiki/Site_reliability_engineering) (SRE) anvender softwareudviklingspraksisser på at drive produktionssystemer. I stedet for at behandle drift som manuelt, ticketdrevet arbejde holdt adskilt fra udvikling behandler SRE pålidelighed som et ingeniørproblem, I løser med kode, måling og klare servicemål. Kerneidéen, populariseret af Google men nu udbredt, er enkel: de mennesker, der holder systemer kørende, bør bruge det meste af deres tid på at bygge automatisering og forbedre systemer, ikke på at slukke de samme fejl i hånden igen og igen.

For store teams har det betydning, fordi skala hæver både værdien af pålidelighed og omkostningen ved at gøre det forkert. Når én tjeneste understøtter millioner af brugere eller tusinder af interne forbrugere, betyder en times nedetid tabt omsætning, missede transaktioner og eroderet tillid. Manuel drift, der fungerer fint for en håndfuld servere, falder fra hinanden under hundredvis af tjenester og [kontinuerlig udrulning](https://en.wikipedia.org/wiki/Continuous_deployment). SRE giver jer et fælles sprog for pålidelighed, en måde at gøre afvejningen mellem at levere funktioner og at holde tingene stabile eksplicit og en måde at holde den linje ensartet på tværs af mange teams.

Virksomheds- og offentlige sammenhænge tilføjer yderligere vægt. Regulerede brancher som bank, sundhed og offentlige tjenester bærer ofte juridiske eller kontraktuelle tilgængelighedsforpligtelser, revisionskrav og lille tolerance for udfald, der påvirker borgere eller sikkerhed. Offentlige digitale tjenester offentliggør i stigende grad deres pålidelighedsmål og ydeevnedata åbent. SRE giver jer en stringent, dokumentationsbaseret måde at definere, hvad "pålidelig nok" betyder, måle det ærligt og forsvare ingeniørprioriteter over for ledelse og tilsynsorganer med data frem for mening.

*Se også:* kapitel 9.2 (observerbarhed og overvågning), kapitel 9.3 (hændelseshåndtering) og kapitel 3.5 (skalerbarhed, ydeevne og robusthed).

## Grundprincipper

- **Pålidelighed er den vigtigste funktion.** Et system, der ikke virker, er værdiløst, uanset hvor mange funktioner det har, men perfekt pålidelighed er hverken opnåelig eller dens omkostning værd.
- **Definér pålidelighed med målbare mål.** Service level-indikatorer (SLI'er), -mål (SLO'er) og -aftaler (SLA'er) forvandler vage forventninger til tal, alle kan blive enige om.
- **100 procent er det forkerte mål.** Brugere kan ikke se forskel på et meget pålideligt system og et perfekt pålideligt, så sigt efter "pålidelig nok", og brug det resterende budget på fart.
- **Fejlbudgetter afstemmer incitamenter.** Hullet mellem SLO'en og 100 procent er et budget for risiko, udviklere og driftsfolk deler, og erstatter diskussioner med regnestykker.
- **Toil er fjenden.** Gentaget, manuelt, automatiserbart driftsarbejde bør måles, loftes og systematisk elimineres.
- **Automatisér bevidst.** Automatisering er, hvordan et lille team driver et stort system; at investere i den er en førsteklasses ingeniøraktivitet.
- **Skyldfri læring.** Fejl behandles som muligheder for at forbedre systemer og processer, ikke for at straffe enkeltpersoner.

## Anbefalinger

### Definér SLI'er, SLO'er og SLA'er bevidst

Begynd fra brugerens perspektiv. En **[service level-indikator](https://en.wikipedia.org/wiki/Service-level_indicator)** er en kvantitativ måling af en tjenestes adfærd, såsom andelen af forespørgsler serveret på under 300 millisekunder eller brøkdelen af vellykkede svar. Vælg et lille antal SLI'er, der reelt afspejler brugertilfredshed: tilgængelighed, latens, korrekthed og friskhed er almindelige. Et **[service level-mål](https://en.wikipedia.org/wiki/Service-level_objective)** er en målværdi eller et interval for en SLI, for eksempel "99,9 procent af forespørgsler lykkes over et rullende 28-dages vindue." En **[service level-aftale](https://en.wikipedia.org/wiki/Service-level_agreement)** er en kontrakt med konsekvenser (refusioner, bøder) knyttet til et lovet niveau. Hold jeres SLO'er strengere end jeres SLA'er, så I får en advarsel, før I bryder en forpligtelse. Offentliggør jeres SLO'er, gennemgå dem kvartalsvis, og behandl dem som levende dokumenter, der strammes eller løsnes, efterhånden som I lærer.

### Adoptér fejlbudgetter, og håndhæv dem

Fejlbudgettet er `100% minus SLO'en`. Hvis jeres SLO er 99,9 procent, er jeres budget 0,1 procent upålidelighed pr. vindue, omkring 43 minutter om måneden. Brug det på planlagt risiko: aggressive releases, eksperimenter og kontrollerede fejltests. Når budgettet er sundt, kan teams levere hurtigt. Når det løber tør, bør politikken automatisk skifte prioriteter mod pålidelighedsarbejde og sætte risikable ændringer på pause, til systemet har rettet sig. Styrken ved fejlbudgettet er, at I aftaler det på forhånd, så det tager følelserne og politikken ud af øjeblikket under et udfald.

### Mål og reducér toil

Toil er driftsarbejde, der er manuelt, gentaget, automatiserbart, taktisk og vokser i takt med systemet. Følg procentdelen af SRE-tid brugt på toil, og sæt et loft, almindeligvis omkring 50 procent, så mindst halvdelen af jeres ingeniørtid går til varige forbedringer. Hold et efterslæb af toilreducerende projekter, prioritér efter frekvens gange omkostning, og fejr at dræbe en tilbagevendende opgave lige så meget som at levere en ny funktion. Et **automatiseringsmandat** gør dette eksplicit: enhver manuel procedure, I udfører mere end et fastsat antal gange, bliver en kandidat til automatisering eller selvbetjent værktøj.

### Planlæg kapacitet, og prognosticér efterspørgsel

Modellér jeres forventede belastning ud fra historiske tendenser, planlagte lanceringer og forretningsprognoser. Kombinér prognoser for organisk vækst med enkeltstående begivenheder som marketingkampagner, skattefrister eller ydelsestilmeldingsperioder, der betyder meget i det offentlige. Hold luft over spidsbelastning, belastningstest for at tjekke jeres antagelser, og automatisér skalering, hvor I kan, mens I beholder en menneskegennemgået [kapacitetsplan](https://en.wikipedia.org/wiki/Capacity_planning) til store forpligtelser. Følg ledetider for provisionering, så en mangel aldrig overrasker jer.

### Behandl pålidelighed som en funktion med reel omkostning

Hver ekstra "niner" af tilgængelighed koster som regel langt mere i redundans, test og driftsmæssig sofistikering end den forrige. Gør omkostningen ved niner eksplicit, så produktejere vælger målet med åbne øjne. Design til elegant nedgradering, så delvise fejl giver reduceret service frem for totale udfald. Invester i redundans og failover i forhold til SLO'en, ikke jævnt på tværs af hver komponent.

### Vælg en organisatorisk SRE-model

Der er ingen enkelt korrekt struktur. Et **centraliseret** SRE-team giver jer ensartethed, dyb ekspertise og fælles værktøj, men det kan blive en flaskehals eller en losseplads for andres problemer. En **indlejret** model placerer SRE'er inde i produktteams for tæt samarbejde, men risikerer inkonsistens og isolation. Mange store organisationer bruger en hybrid: en central platforms- og standardgruppe plus indlejrede pålidelighedsingeniører, med en klar engagementmodel, der definerer, hvornår en tjeneste kvalificerer sig til SRE-støtte, og hvilken produktionsparathedsoverligger den først skal klare.

## Afvejninger: fordele og ulemper

| Beslutning | Fordele | Ulemper |
|---|---|---|
| Strenge SLO'er (flere niner) | Højere brugertillid, opfylder kontrakter | Stigende omkostning, langsommere funktionslevering |
| Løse SLO'er (færre niner) | Hurtigere levering, lavere omkostning | Risiko for brugerfrafald og SLA-bøder |
| Centraliseret SRE | Ensartethed, fælles ekspertise | Flaskehalse, afstand til produktet |
| Indlejret SRE | Tæt samarbejde, kontekst | Inkonsistens, svær at bemande |
| Tung automatiseringsinvestering | Skalerer, reducerer toil | Omkostning på forhånd, automatisering kan selv fejle |

Pålidelighedsingeniørarbejde handler egentlig om at bruge endelige ressourcer klogt. At jagte en ekstra niner, brugere ikke engang kan mærke, spilder penge, der kunne finansiere funktioner eller sænke priser. Gå den anden vej og underinvester i et system, hvis fejl forårsager reel skade, og det er uforsvarligt. Fejlbudgetrammeværket findes netop for at gøre denne afvejning synlig og forhandlingsbar frem for implicit og konfliktfyldt. Afvejningen i den organisatoriske model er lige så reel: det rette svar afhænger af virksomhedens størrelse, ingeniørmodenhed og hvor ensartede jeres tjenester er.

## Spørgsmål til drøftelse med dit team

1. **Hvilken præcis SLI afspejler det, jeres brugere faktisk mærker, og kan I vise, at den ikke er en forfængelighedsmåling?** Vælg den forkerte indikator, og hvert dashboard ser grønt ud, mens brugere lider, hvilket er forfængeligheds-SLI-fælden, dette kapitel advarer om. Tag reelle data med til drøftelsen: mål den samme brugerrejse fra en reel forespørgselssti (login til dashboard, kasse til bekræftelse) frem for server-CPU eller et backend-sundhedstjek. For et stort team udbredes én dårlig SLI: dusinvis af tjenester arver den, alarmer udløses på det forkerte, og fejlbudgettet holder op med at betyde noget. I virksomheds- og offentlige sammenhænge, hvor en SLA bærer refusioner eller borgerpåvirkning, er jeres SLI den dokumentation, I forsvarer over for revisorer, så den skal kunne spores direkte til brugersynlig succes. Hvis I ikke kan trække en linje fra tallet til en brugers oplevelse, så udskift tallet.

2. **Hvad skal en tjeneste bevise, før jeres SRE-team tager den på vagt, og hvem siger nej?** Uden en produktionsparathedsoverligger bliver et centralt SRE-team en losseplads for hver ustabil tjeneste og drukner i andres tekniske gæld. Skriv optagelseskriterierne ned: en ejet SLO, fungerende runbooks, handlingsbare alarmer, kapacitetsluft og en påvist udrulnings- og tilbagerulningsvej. For en stor organisation er denne engagementmodel, hvad forhindrer pålidelighedsteamet i at blive en flaskehals, der sinker alle. I regulerede sammenhænge fungerer parathedsgennemgangen også som en kontrol, I kan vise tilsynsorganer. Afgør, hvem der har autoriteten til at afvise onboarding, for en overligger, ingen håndhæver, er ikke en overligger, og svaret ændrer, om SRE skalerer eller kollapser under nedarvet smerte.

3. **Hvor langt i forvejen forhåndsprovisionerer I til jeres største forudsigelige spidsbelastning, og kender I jeres provisioneringsledetid?** At antage, at cloudelasticitet er øjeblikkelig og uendelig, inviterer til mangler netop under de spidsbelastninger, der betyder mest, og de spidsbelastninger (skattefrister, tilmeldingsvinduer, udsalgsbegivenheder) er de øjeblikke, hvor fejl er mest synlig og mest kostbar. Tag tallene med: historisk spidsbelastning, prognosticeret vækst, den multiplikator I belastningstest til, og den reelle ledetid på at skaffe stor reserveret kapacitet eller specialiserede instanser. For offentlige sæsontjenester kan spidsbelastningen være flere gange normal belastning og er politisk umulig at overse, så forhåndsprovisionering uger i forvejen slår at håbe, at autoskalering følger med. Svaret bør sætte en konkret kalender: hvornår I belastningstest, hvornår I låser kapacitet, og hvem der ejer go-beslutningen.

4. **Når jeres fejlbudget løber tør, hvad sker der så egentlig, og hvem har beføjelsen til at håndhæve det?** Et fejlbudget, der aldrig handles på, når det er udtømt, er blot pynt, og øjeblikket under et udfald er det værste tidspunkt at forhandle politikken fra bunden. Det modstridende træk er reelt: en forpligtet lancering, en omsætningsfrist eller en offentlig annoncering vil presse hårdt mod en frysning af risikable ændringer. Tag forbrændingsratedata, den på forhånd aftalte politiktekst og en optegnelse over de sidste par gange, budgettet blev brudt, med, så I kan se, om frysningen faktisk holdt. For et stort team afstemmer budgettet kun incitamenter, hvis hver gruppe arver den samme håndhævelse, så afgør på forhånd, hvem der underskriver en tilsidesættelse, og hvordan den undtagelse logges. I virksomheds- og offentlige sammenhænge, hvor en SLA bærer bøder eller borgerpåvirkning, bliver tilsidesættelsessporet et revisionsartefakt, så navngiv den ansvarlige ejer nu frem for at improvisere, når budgettet allerede er væk.

5. **Hvilken brøkdel af jeres SRE-teams uge er toil, og er det et målt tal eller en fornemmelse?** Toil, ingen tæller, udvider sig tavst, til teamet bruger al sin tid på at slukke brande og ingen på at bygge varige forbedringer, hvilket netop er den fælde, SRE findes for at slippe ud af. Spændingen er, at det i sig selv er arbejde at måle toil, og ingeniører under deadlinepres modsætter sig at logge, hvor deres timer går hen. Tag en ærlig stikprøve med: en uge eller to af sporet tid mod en fælles definition af toil (manuelt, gentaget, automatiserbart, taktisk og skalerende med systemet), plus efterslæbet af automatiseringsprojekter rangeret efter frekvens gange omkostning. For en stor organisation betyder et loft på 50 procent kun noget, hvis det rapporteres og forsvares team for team, så aftal, hvem der gennemgår tallet, og hvad der sker, når et team bryder det. I regulerede og offentlige sammenhænge frigør et loft over toil knappe specialister til det kontrol- og revisionsarbejde, manuel drift fortrænger, så behandl toiltallet som et kapacitetssignal, ledelsen bør se.

6. **Hvilken organisatorisk SRE-model kører I, og hvilken dokumentation ville fortælle jer, at den er holdt op med at passe?** Et centraliseret team giver ensartethed og fælles værktøj, men kan blive en flaskehals; en indlejret model giver kontekst, men driver mod inkonsistens; den hybrid, de fleste store organisationer lander på, har brug for en klar engagementmodel, ellers arver den begge svagheder. Tag signalerne, der afslører belastning, med: hvor lang tid tjenester venter på SRE-støtte, hvor meget pålidelighedspraksis varierer mellem teams, og om indlejrede ingeniører føler sig afskåret fra et fagligt fællesskab. Det rette svar afhænger af virksomhedens størrelse, ingeniørmodenhed og hvor ensartede jeres tjenester er, så gensyn det, når de ændrer sig, frem for at behandle det første valg som permanent. For en virksomhed eller et offentligt organ med mange teams og strenge ensartethedskrav balancerer en central standard- og platformsgruppe plus indlejrede pålidelighedsingeniører som regel ensartethed mod lokal kontekst, men kun hvis engagementmodellen og produktionsparathedsoverliggeren er skrevet ned, og nogen ejer dem.

## Sektorperspektiv

**Startup.** Med en håndfuld ingeniører og ingen runway til et dedikeret pålidelighedsteam så vælg en enkelt SLO på den brugerrejse, der betyder mest, og del vagten på tværs af hele teamet. Støt jer til jeres cloududbyders administrerede tjenester og indbyggede overvågning frem for at bygge observerbarhedsinfrastruktur, og skriv korte postmortems i et fælles dokument, så rettelser holder. Fart betyder mere end proces her: en løs SLO, I faktisk håndhæver, slår en omstændelig, ingen iagttager.

**Lille virksomhed.** Uden en specialist til at drive pålidelighed så behandl den som en disciplin, I køber ind i gennem jeres platform: hostet oppetidsovervågning, administrerede databaser og statussideværktøj i stedet for en skræddersyet stak. Sæt en eller to SLO'er knyttet til de transaktioner, der betaler regningerne, og afgør ærligt, hvilke fejl der ville koste jer en kunde. Køb robusthed, hvor det er billigere end at bygge den, og hold driftsbyrden let nok til, at jeres eksisterende ingeniører kan bære den ved siden af funktionsarbejde.

**Stor virksomhed.** Udfordringen er ensartethed på tværs af mange teams: et fælles SLO-ordforråd, en fælles fejlbudgetpolitik og en produktionsparathedsoverligger, hver tjeneste klarer, før SRE tager den på vagt. En central platforms- og standardgruppe plus indlejrede pålidelighedsingeniører holder praksis ensartet uden at blive en flaskehals, og styring har brug for fejlbudgetter rapporteret og håndhævet på samme måde overalt. Budgettér observerbarhedsinfrastrukturen og automatiseringsinvesteringen eksplicit, og styr pålidelighed som en portefølje med målinger, ledelsen kan se.

**Offentlig sektor.** Offentlige tjenester bærer ofte offentliggjorte tilgængelighedsmål, lovbestemte forpligtelser og revisionspligter, så SLO'er og fejlbudgetbeslutninger bliver optegnelser, I forsvarer over for tilsynsorganer. Indkøbsregler kan begrænse, hvilken overvågning og hosting I kan bruge, og åbenhedsforventninger skubber jer til at offentliggøre pålidelighedsdata på et offentligt statusdashboard. Planlæg for ekstreme sæsonspidser som skattefrister og ydelsestilmeldingsvinduer uger i forvejen, og hold en skyldfri postmortemkultur, så offentlige fejl driver systemforbedring frem for individuel skyld.

## Eksempler

**Startup.** Et startup på ti personer kører en enkelt webapp og deler vagten på tværs af tre ingeniører. I stedet for at bygge et pålidelighedsteam, det ikke har råd til, vælger det én meningsfuld SLO: 99,5 procent succes på login-til-dashboard-flowet, målt fra reelle brugerforespørgsler. Da en ustabil tredjeparts-API begynder at æde det budget, bruger teamet en fredag på at tilføje et genforsøg og en cache i stedet for at levere næste funktion, og skriver så en postmortem på to afsnit i et fælles dokument, så rettelsen holder.

**Stor virksomhed.** En global betalingsvirksomhed sætter en tilgængeligheds-SLO på 99,99 procent for sin transaktions-API, hvilket giver et fejlbudget på omkring fire minutter om måneden. Et centralt SRE-platformsteam ejer fælles [observerbarhed](https://en.wikipedia.org/wiki/Observability_(software)), hændelsesværktøj og fejlbudgetpolitikken, mens indlejrede pålidelighedsingeniører arbejder inde i hver produktgruppe. Da en ny svindeldetektionsfunktion forbrænder halvdelen af det månedlige budget på en uge, fryser den på forhånd aftalte politik ikke-kritiske releases, til pålidelighedsarbejde har genskabt luft. Ledere accepterer det uden diskussion, fordi de ratificerede politikken på forhånd.

**Offentlig sektor.** En national skattemyndighed driver en online indberetningstjeneste med ekstreme sæsonspidser omkring den årlige frist. Dens SRE-team prognosticerer efterspørgsel ud fra tidligere år plus befolknings- og politikændringer, belastningstester til flere gange normal spidsbelastning og forhåndsprovisionerer kapacitet uger i forvejen. Offentlige SLO'er for tilgængelighed og sidelatens kommer op på et statusdashboard. En skyldfri [postmortem](https://en.wikipedia.org/wiki/Postmortem_documentation)-kultur (at gennemgå fejl for at forbedre systemer frem for at tildele individuel skyld) og et automatiseringsmandat skærer støt de manuelle indgreb, der engang dominerede indberetningssæsonen, og frigør personale til at forbedre systemet frem for at pleje det gennem hver frist.

## Business case: motivation, ROI og TCO

Afkastet af SRE kommer fra tre kilder: undgået nedetid, mindre driftsarbejdskraft og hurtigere sikker levering. Nedetid for en stor tjeneste kan koste tusinder til millioner pr. time i tabt omsætning, bøder og afhjælpning, så selv beskedne pålidelighedsgevinster betaler et team hurtigt. Toilreduktion forvandler tilbagevendende manuel omkostning til en engangsautomatiseringsinvestering, så den samlede ejeromkostning falder, efterhånden som skalaen vokser, frem for at stige i takt med den. Fejlbudgetter lader forretningen levere hurtigere, når pålideligheden er sund, og indfanger funktionsværdi, som alt for forsigtig drift ville lade ligge.

Adoptionsomkostningen er reel. SRE kræver dygtige ingeniører, observerbarhedsinfrastruktur og kulturel forandring, der konkurrerer med funktionsdeadlines. Men omkostningen ved ikke at adoptere er højere i skala: ubegrænset driftsbemanding, uforudsigelige udfald, medarbejderudbrændthed og -afgang og omdømmeskade, der er svær at kvantificere, men let at lide. For at fremlægge sagen for ledelsen så ram SRE ind som risikostyring med målbare afkast. Præsentér den nuværende omkostning ved hændelser og manuel drift, de SLO-mål, der er knyttet til forretningsforpligtelser, og den forventede reduktion i begge. Forankr argumentet i fejlbudgettet som et styringsværktøj, der giver ledelsen en løftestang over afvejningen mellem pålidelighed og fart.

## Anti-mønstre og faldgruber

- **SRE som omdøbt drift.** At omdøbe et driftsteam uden ingeniørtiden, automatiseringsmandatet og autoriteten til at skubbe tilbage ændrer intet.
- **At sigte mod 100 procent.** At jagte perfekt pålidelighed spilder penge og blokerer levering for gevinster, brugere ikke kan mærke.
- **Forfængeligheds-SLI'er.** At måle server-CPU i stedet for brugersynlig succes giver tal, der ser godt ud, mens brugere lider.
- **Fejlbudgetter uden tænder.** Et budget, der aldrig håndhæves, når det er udtømt, er blot pynt.
- **Toil uden måling.** Hvis I ikke følger toil, æder det stille teamet, til intet forbedringsarbejde sker.
- **SRE som losseplads.** Centraliserede teams, der arver hver ustabil tjeneste uden en parathedsoverligger, drukner i andres tekniske gæld.
- **At ignorere kapacitetsledetider.** At antage, at cloudelasticitet er øjeblikkelig og uendelig, inviterer til mangler netop under de spidsbelastninger, der betyder mest.

## Modenhedsmodel

**Niveau 1, Opstart.** Drift er manuel og reaktiv. Der er ingen formelle SLO'er, pålidelighed er en meningssag, og de samme hændelser gentager sig, mens brandslukning dominerer. Enhver automatisering er tilfældig, og ingen ejer pålidelighed som et ingeniøranliggende.

**Niveau 2, Udvikling.** Nogle tjenester har basale SLI'er og SLO'er og rudimentær overvågning og alarmering, men praksis varierer vidt mellem teams. Toil anerkendes, men måles ikke, automatisering er ad hoc, og postmortems sker inkonsistent. Pålidelighed forbedres i de lommer, hvor enkeltpersoner presser på, ikke fordi organisationen kræver det.

**Niveau 3, Standardisering.** SLI'er, SLO'er og en fejlbudgetpolitik er dokumenteret og anvendt ensartet på tværs af teams. Toil er defineret og følges, kapacitetsplanlægning er rutine, en SRE-engagementmodel med produktionsparathedsgennemgange findes, og automatisering er en finansieret arbejdsstrøm frem for et sideprojekt. Pålidelighedspraksis er skrevet ned og håndhævet i hele organisationen.

**Niveau 4, Styring.** Pålidelighedsprogrammet måles og styres med data mod baselines. Fejlbudgetforbrændingsrate, toilprocent, SLO-opfyldelse, gennemsnitlig genoprettelsestid og provisioneringsledetider følges som målinger, gennemgås efter en fast kadence og bruges til at holde teams til deres mål. Budgetbrud udløser den aftalte frysning, kapacitet prognosticeres mod efterspørgselsmodeller, og hver go/no-go-beslutning hviler på dokumentation frem for mening.

**Niveau 5, Orkestrering.** Pålidelighedsingeniørarbejde er integreret på tværs af organisationen og løbende forbedret. Fejlbudgetpolitik er automatiseret og respekteret overalt, det meste drift er selvbetjent, kapacitet provisioneres proaktivt, og pålidelighedsdata driver adaptive afvejninger mellem fart og stabilitet. Organisationen omafgrænser rutinemæssigt SLO'er, pensionerer toil og rebalancerer pålidelighedsinvestering, efterhånden som forretnings- og risikobilledet skifter.

## Idéer til drøftelse

- Hvordan bør en organisation sætte sine første SLO'er, når den ikke har historiske pålidelighedsdata at forankre dem i?
- Når fejlbudgettet er udtømt, men en større lancering er forpligtet, hvem har autoritet til at tilsidesætte frysningen, og hvordan registreres den beslutning?
- Er en centraliseret, indlejret eller hybrid SRE-model den rette for jeres organisation, og hvad ville udløse en ændring?
- Hvordan værdisætter I en ekstra niner af tilgængelighed mod de funktioner, den samme investering kunne finansiere?
- Hvad tæller som toil i jeres kontekst, og hvor går linjen mellem værdifuld manuel dømmekraft og eliminerbar gentagelse?
- Hvordan bør pålidelighedsmål adskille sig mellem borgervendte offentlige tjenester og interne virksomhedsværktøjer?

## Vigtigste pointer

- SRE anvender softwareudvikling på drift og behandler pålidelighed som en målbar, finansierbar funktion.
- SLI'er, SLO'er og SLA'er forvandler pålidelighed fra mening til aftalte tal; hold SLO'er strengere end SLA'er.
- Fejlbudgettet afstemmer udviklere og driftsfolk ved at gøre afvejningen mellem pålidelighed og fart eksplicit og forhåndsforhandlet.
- Mål og loft toil, og behandl automatisering som førsteklasses ingeniørarbejde, så driften skalerer under-lineært.
- Planlæg kapacitet ud fra efterspørgselsprognoser, og respektér provisioneringsledetider, især ved sæsonspidser.
- Vælg en organisatorisk SRE-model bevidst, og definér en klar engagementmodel og produktionsparathedsoverligger.

## Referencer og videre læsning

- Betsy Beyer, Chris Jones, Jennifer Petoff, Niall Richard Murphy, *Site Reliability Engineering: How Google Runs Production Systems*
- Betsy Beyer, Niall Richard Murphy, David K. Rensin, Kent Kawahara, Stephen Thorne, *The Site Reliability Workbook: Practical Ways to Implement SRE*
- David N. Blank-Edelman (editor), *Seeking SRE: Conversations About Running Production Systems at Scale*
- Thomas A. Limoncelli, Strata R. Chalup, Christina J. Hogan, *The Practice of Cloud System Administration*
- Nicole Forsgren, Jez Humble, Gene Kim, *Accelerate: The Science of Lean Software and DevOps*
