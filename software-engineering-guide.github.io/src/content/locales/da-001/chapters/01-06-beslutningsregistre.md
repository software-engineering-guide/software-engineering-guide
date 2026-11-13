# 1.6 Beslutningsregistre

## Overblik og motivation

Et **beslutningsregister** er et dokument, der fastholder en vigtig beslutning sammen med dens kontekst og konsekvenser. Den bedst kendte form er **[arkitekturbeslutningsregistret](https://en.wikipedia.org/wiki/Architectural_decision) (ADR)**, en kort, helst uforanderlig note, der registrerer ét arkitektonisk væsentligt valg, hvorfor det blev truffet, og hvad der følger af det. Et projekts fulde sæt af registre er dets **beslutningslog (ADL)**, og disciplinen at føre dem er en del af **arkitekturviden-styring (AKM)**. Dette kapitel bygger på praksis for beslutningstagning og styring fra kapitel 1.5 og fokuserer på, hvordan du skriver, opbevarer og vedligeholder beslutningsregistre i stor skala.

Motivationen er enkel og smertefuld at lære på den hårde måde. På ethvert langlivet system er det dyreste spørgsmål "hvorfor i alverden blev det bygget sådan?", stillet måneder eller år senere af folk, der ikke var i rummet. Koden viser, *hvad* systemet gør. Tests viser, at det *virker*. Men ingen af dem fastholder, *hvorfor* du valgte denne vej frem for de alternativer, du overvejede og afviste. Uden beslutningsregistre fordamper den begrundelse med personaleudskiftning. Teams forhandler afgjorte spørgsmål forfra, omstøder gode beslutninger af dårlige grunde eller beholder dårlige beslutninger af frygt. Et beslutningsregister er et billigt brev til fremtiden, der bevarer begrundelsen.

For store teams er dette lige så meget et koordineringsværktøj som en hukommelseshjælp. Virksomheder har dusinvis af teams, der træffer overlappende valg. En fælles beslutningslog gør ét teams hårdt tjente begrundelse til et genbrugeligt aktiv og forebygger divergerende, uforenelige beslutninger. I offentlige og regulerede sammenhænge er beslutningsregistre tæt på obligatoriske. Revisorer, tilsynsorganer og efterfølgende konsulenter har alle brug for en sporbar begrundelse, der forbinder arkitektonisk væsentlige krav med de valg, der er truffet mod dem. En velført beslutningslog er ofte forskellen mellem et system, du kan sikre og revidere, og et, du ikke kan.

## Grundprincipper

- **Registrér *hvorfor*, ikke kun *hvad*.** Kontekst og afviste alternativer er pointen.
- **Én beslutning pr. register.** Hold hvert register specifikt og selvstændigt.
- **Lille og let slår omfattende og ubrugt.** Et register på én side, der findes, slår en rapport, der aldrig bliver skrevet.
- **Tidsstempl alt.** Omkostninger, begrænsninger og leverandører ændrer sig; datér hver påstand.
- **Foretræk en levende log, pragmatisk.** Uforanderlighed er idealet; i praksis så ret med daterede noter.
- **Ord frem for forkortelser.** "Beslutninger" inviterer til flere bidrag end "ADR'er."
- **Gør beslutninger synlige og, hvor muligt, testbare.** Bring det rette register frem i det rette øjeblik; sikr det med fitness functions.

## Anbefalinger

### Fang den væsentlige struktur

Et godt beslutningsregister har nogle få væsentlige afsnit. Tilpas en kendt skabelon frem for at opfinde en:

- **Titel:** en kort imperativ sætning i nutid ("Brug [PostgreSQL](https://en.wikipedia.org/wiki/PostgreSQL) til hovedbogen").
- **Status:** foreslået, accepteret, erstattet, forældet.
- **Kontekst:** situationen, kræfterne, forretningsprioriteterne og begrænsningerne, der gør denne beslutning nødvendig; medtag det arkitektonisk væsentlige krav, den adresserer.
- **Beslutning:** det valg, der er truffet, angivet klart.
- **Konsekvenser:** hvad der bliver lettere, og hvad der bliver sværere, opfølgende beslutninger der udløses, og accepterede risici.

Populære skabeloner omfatter Michael Nygards (enkel og bredt anvendt), Tyree og Akermans (mere omstændelig, med vægtede alternativer), MADR (Markdown Any Decision Records, stærk på muligheder og deres fordele/ulemper) og Y-statements (en strukturet form i én sætning). Standardisér på én pr. organisation, så registre er sammenlignelige. Se kapitel 12.3 for en copy-paste-skabelon.

### Skriv registre, der er specifikke, daterede og næsten uforanderlige

Hold hvert register til netop én beslutning. Tidsstempl enkelte påstande, især alt der driver: priser, skaleringstal, leverandørers kapabiliteter, licensvilkår. I teorien bør et register være uforanderligt. Når en beslutning ændrer sig, skriver du et *nyt* register, der erstatter det gamle og bevarer historikken. I praksis finder mange teams, at en **levende dokument**-tilgang virker bedre: indsæt ny information i det eksisterende register med et datostempel og en note om, at den kom efter beslutningen. Begge er legitime. Den uforanderlige stil er stærkere til revisionsspor; den levende stil er bedre til daglig teamviden. Vælg bevidst og vær konsekvent.

### Opbevar registre, hvor arbejdet foregår

Læg beslutningsregistre i [versionsstyring](https://en.wikipedia.org/wiki/Version_control) sammen med koden: et `decisions/`- (eller `adr/`-) bibliotek med [Markdown](https://en.wikipedia.org/wiki/Markdown)-filer, én pr. beslutning, navngivet med en imperativ verbalfrase med små bogstaver og bindestreger (`choose-database.md`, `format-timestamps.md`). Det giver dig historik, gennemgang og diffing gratis og holder begrundelsen ved siden af det, den forklarer. Hvis dit team foretrækker [wikier](https://en.wikipedia.org/wiki/Wiki), Google Docs eller en Jira-lignende tracker, så brug dem i stedet. Værktøjet betyder langt mindre end vanen. Et let kommandolinjeværktøj (som `adr-tools`) kan stilladsere og indeksere registre.

### Kald dem "beslutninger", og udvid ud over arkitektur

En praktisk indsigt fra mange teams: betegnelsen betyder noget. Nogle udviklere og ledere bliver stikkende på ordet "arkitektur", og "register" kan føle sig som papirarbejde bagefter. At omdøbe biblioteket blot til "decisions" vender ofte en kontakt. Teams begynder at registrere leverandørvalg, planlægningsbeslutninger, tidsplansbeslutninger, data- og compliancebeslutninger, alt med den samme skabelon. Folk lærer hurtigere af ord end af forkortelser, og de bidrager mere, når rammen er "hjælp dine fremtidige kolleger med at tænke" frem for "udfyld den obligatoriske formular".

### Definér livscyklussen og styringen

For at beslutningsregistre skal skalere, så aftal den omgivende proces (det er her, kapitel 1.5s styring møder praksis):

- **Hvem kan rejse et, og hvad retfærdiggør det:** typisk enhver vidende bidragyder; rejs et register, når fremtidige udviklere får brug for *hvorfor*, og spring det over for lavrisiko-, selvstændige eller allerede dokumenterede valg.
- **Livscyklus:** et simpelt flow som *Igangsætning → Undersøgelse → Evaluering → Implementering → Vedligeholdelse → Udfasning*, med acceptkriterier for at gå mellem trin (problem formuleret, alternativer overvejet, afvejninger dokumenteret, interessenter hørt).
- **Roller:** forslagsstiller, undersøger, gennemgår, godkender og en ansvarlig vedligeholder, der gennemgår registret periodisk (mindst årligt) og driver den endelige udfasning.
- **Styring:** hvordan konsensus, konflikt, eskalering og veto fungerer, og eventuelle compliance-begrænsninger. Læn dig op ad principper som *bias for action* og *[disagree-and-commit](https://en.wikipedia.org/wiki/Disagree_and_commit)*, og forbehold tungere proces til irreversible beslutninger med stor sprængradius ("envejsdør").

### Gør beslutninger testbare og synlige

Et beslutningsregister *dokumenterer* en beslutning; en **fitness function** *sikrer* den: en automatisk kontrol, kørt i [continuous integration](https://en.wikipedia.org/wiki/Continuous_integration) (CI), der verificerer, at beslutningen stadig holder ("alle tilstandsændringer skal udsende hændelser", "intet modul må importere på tværs af disse grænser", med værktøjer som ArchUnit). Det gør styring fra periodisk manuel gennemgang til kontinuerlig, skalerbar håndhævelse, hvilket er særligt værdifuldt for regulatoriske mål og revisionsmål (kapitel 3.1, 4.6, 8.5). Bring derefter det *rette* register frem i det *rette* øjeblik. Værktøjer, der knytter relevante beslutninger til en pull request, når en udvikler rører koden, de styrer, slår at håbe, at folk læser en dokumentationsmappe.

## Afvejninger: fordele og ulemper

| Valg | Fordele | Ulemper |
|---|---|---|
| **Lette ADR'er (Nygard/MADR)** | Hurtige at skrive, bliver faktisk skrevet; lav ceremoni | Mindre stringens for højrisiko, omstridte beslutninger |
| **Tunge skabeloner (Tyree-Akerman)** | Vægtede alternativer; stærk til store, dyre valg | Langsommere; kan afskrække rutinemæssig registrering |
| **Uforanderlig + erstat** | Rent revisionsspor; historik bevaret | Flere registre; læsere må følge kæder |
| **Levende dokument (daterede rettelser)** | Én aktuel sandhedskilde; let at vedligeholde | Svagere revisionshistorie; risiko for stille redigeringer |
| **Markdown i repo** | Versioneret, kan gennemgås, ved siden af koden | Mindre venligt for ikke-udviklere |
| **Wiki / dokumentværktøj** | Tilgængeligt for alle roller | Svagere historik og gennemgang; driver væk fra koden |

Den centrale spænding er **stringens versus udbredelse**. Det mest stringente system, ingen bruger, registrerer intet. Det letteste system, alle bruger, vokser i værdi. Vælg som standard let, og forbehold tungere proces til de få beslutninger, der er dyre og svære at fortryde.

## Spørgsmål til drøftelse med dit team

1. **Hvordan når det rette beslutningsregister frem til en udvikler i det øjeblik, vedkommende rører den kode, det styrer, i stedet for at ligge i en mappe, ingen åbner?** En skrive-kun-log registrerer begrundelse, der aldrig ændrer adfærd, hvilket er den almindeligste måde, beslutningsregistre fejler på: de findes, og ingen læser dem, når det gælder. Det modstridende hensyn er indsats, for at bringe registre frem automatisk (ved at knytte dem til en pull request, når nogen redigerer den styrede kode) kræver en værktøjsinvestering, som en wiki eller dokumentmappe ikke gør. Tag dokumentation med til drøftelsen: da nogen for nylig omstødte eller genforhandlede et afgjort spørgsmål, var det relevante register da synligt i det øjeblik, eller begravet? For en stor organisation med dusinvis af teams er synlighed det, der gør ét teams hårdt tjente begrundelse til et genbrugeligt aktiv i stedet for et privat arkiv. Beslut, om du vil opbevare registre i versionsstyring ved siden af koden og koble dem ind i pull-request-flowet, så registret vises, hvor arbejdet foregår.

2. **Hvem er den ansvarlige vedligeholder af hvert register, og hvad forhindrer din log i at forfalde til selvsikker misinformation?** En beslutningslogs farlige fejlform er ikke en tom mappe, det er en mappe fuld af registre, hvis omkostninger, leverandørkapabiliteter og begrænsninger stille blev forældede for år siden. Hvert register har brug for en ansvarlig ejer, der gennemgår det efter en kadence (mindst årligt) og driver erstatning eller udfasning, ellers rådner loggen til folklore, folk citerer selektivt og stoler lidt på. Tag dokumentation med: hvor mange af dine registre er udaterede, hvor mange beskriver en leverandør eller pris, der siden er ændret, og hvornår blev hvert sidst gennemgået. I offentlige og regulerede sammenhænge er dette skarpere, fordi en uforanderlig, erstattet kæde netop er, hvad revisorer og efterfølgende konsulenter bruger til en sporbar begrundelse. Beslut din livscyklus eksplicit, tidsstempl enkelte påstande, der driver, og tildel vedligeholdere, så loggen forbliver et levende aktiv frem for en kirkegård.

3. **Bør I standardisere på én skabelon på tværs af alle teams, og hvor meget stringens har jeres højrisiko-beslutninger faktisk brug for?** Sammenlignelighed er en reel fordel: når hvert team bruger den samme form (Nygard, MADR eller lignende), kan et nyt team finde tre tidligere registre og adoptere begrundelsen på en eftermiddag i stedet for en måned med debat. Den centrale spænding er stringens versus udbredelse, fordi den tungeste skabelon, ingen bruger, registrerer intet, mens den letteste, alle bruger, vokser i værdi. Tag dokumentation med: bliver registre faktisk skrevet, og har store, omstridte, dyre beslutninger separat været underanalyserede, fordi den lette form sprang afvejning af alternativer over? For virksomheder, der koordinerer overlappende valg på tværs af teams, forebygger en fælles skabelon plus et søgbart indeks divergerende, uforenelige beslutninger. Vælg som standard let i det almindelige tilfælde, og aftal på forhånd, hvilke envejsdør-beslutninger der fortjener en tungere form med vægtede alternativer.

4. **Hvad retfærdiggør faktisk at rejse et beslutningsregister, og hvem har autoritet til at sige, at et valg ikke behøver et?** Sæt barren for højt, og begrundelsen bag væsentlige valg fordamper; sæt den for lavt, og loggen fyldes med bagateller, der begraver de registre, folk reelt har brug for. For en stor organisation betyder en uklar tærskel, at hvert team improviserer sin egen, så dækningen bliver ujævn, og ingen kan stole på, at et manglende register signalerer en uvigtig beslutning. Tag dokumentation med til drøftelsen: en håndfuld nylige beslutninger, der blev registreret, men ikke behøvede det, og smertefulde, der ikke blev registreret og senere kostede jer en genopdagelse. Aftal en enkel test, for eksempel at registrere, når en fremtidig udvikler får brug for *hvorfor*, og springe lavrisiko-, selvstændige eller allerede dokumenterede valg over. I regulerede og offentlige sammenhænge ændrer regnestykket sig, fordi et revisionsmandat kan kræve et register for hvert arkitektonisk væsentligt krav, uanset om teamet finder det værd at skrive, så navngiv på forhånd, hvilke beslutninger der er ikke til forhandling.

5. **Er jeres registre ægte begrundelse fanget i beslutningens øjeblik, eller papirarbejde skrevet bagefter for at opfylde et mandat?** Et register produceret bagefter for at lukke en sag har tendens til at hvidvaske det valgte alternativ og stille udelade de alternativer, der faktisk blev vejet, hvilket netop er den information, en fremtidig læser har mest brug for. Det modstridende pres er reelt: at skrive *hvorfor* før eller under en beslutning føles langsommere end at udgive, og at indrømme de afviste veje skriftligt kræver psykologisk tryghed, som nogle teams mangler. Tag et udsnit af nylige registre med til bordet og spørg ærligt, om konteksten og de afviste alternativer læses som ægte overvejelse eller som eftermonteret retfærdiggørelse. For et stort team er hule registre værre end ingen, fordi de lærer folk, at loggen ikke kan stoles på. I virksomheds- og offentlig revision er forskellen skarp: tilsynsorganer og efterfølgende konsulenter er afhængige af en begrundelse, der afspejler, hvad der reelt blev overvejet, og et register, der læses som teater, underminerer den sikkerhed, loggen findes for at give.

6. **Hvilke af jeres højrisiko-beslutninger kan I sikre med en automatiseret fitness function frem for at stole på, at periodisk manuel gennemgang fanger en overtrædelse?** Et beslutningsregister dokumenterer et valg, men kun en automatiseret kontrol kørt i continuous integration holder det valg fra stille at eroderes, mens dusinvis af udviklere rører koden gennem årene. Afvejningen er investering, for at skrive og vedligeholde fitness functions (med værktøjer som ArchUnit) koster ingeniørtid, og mange beslutninger, især proces- eller leverandørvalg, er slet ikke mekanisk testbare. Tag dokumentation med: hvilke grænsebeslutninger (modulafhængigheder, hændelsesudsendelse, dataadgangsregler) er stille blevet overtrådt og først fanget sent i gennemgang eller i produktion. For en virksomhed med mange teams gør fitness functions styring fra en central flaskehals til kontinuerlig håndhævelse, der skalerer uden at bremse alle. I regulerede og offentlige sammenhænge er en automatiseret, altid tændt kontrol langt stærkere revisionsbevis end en underskrift på en gennemgang, fordi den beviser, at beslutningen stadig holder i dag, frem for at nogen engang godkendte den.

## Sektorperspektiv

**Startup.** Hold det til vanen og intet andet: en `decisions/`-mappe i dit hovedrepo og en note med to afsnit (kontekst og valg), hver gang du træffer et valg, din fremtidige selv vil stille spørgsmål ved. Spring livscyklus, roller og godkendere helt over, for proces, du ikke kan opretholde, er proces, du vil opgive. Det ene register, der sparer din første ansatte for at spørge, hvorfor systemet er bygget sådan, betaler allerede for hele praksissen.

**Lille virksomhed.** Uden dedikeret arkitekt og med lidt tid så læg registre, hvor dit team allerede arbejder, hvad enten det er en wiki, et fælles dokument eller repoet, frem for at købe et dedikeret værktøj. Vanen betyder langt mere end værktøjet, så sænk tærsklen: kald mappen `decisions` frem for `adr`, og fang leverandør- og køb-versus-byg-valg i samme åndedrag som tekniske. Når du læner dig op ad eksterne konsulenter, er et kort dateret register over, hvorfor du valgte en leverandør eller platform, billig forsikring mod at være låst til et valg, ingen senere kan forklare.

**Stor virksomhed.** Arbejdet er koordinering på tværs af mange teams: standardisér på én skabelon, udgiv et søgbart indeks på tværs af teams, og understøt centrale grænsebeslutninger med fitness functions, så overtrædelser fejler buildet i stedet for at vente på gennemgang. Tildel en ansvarlig vedligeholder til hvert register med en gennemgangskadence, så loggen forbliver et levende aktiv frem for at forfalde til folklore. Gjort godt bliver ét teams begrundelse for et svært valg et aktiv, det næste team adopterer på en eftermiddag i stedet for at forhandle det forfra.

**Offentlig sektor.** Indkøbsregler, åbenhed og offentlig ansvarlighed gør beslutningsregistre tæt på obligatoriske. Kræv et uforanderligt, erstattet register for hvert arkitektonisk væsentligt krav, hvert med kobling mellem valget og det mandat eller den compliance-kontrol, det opfylder, så tilsynsorganer finder en sporbar begrundelse frem for en rekonstruktion. Fordi offentlige systemer spænder over flerårige, multi-leverandør-levetider, er en velført log ofte det, der lader en efterfølgende konsulent forstå, hvorfor systemet har den form, det har, og fortsætte arbejdet uden at forhandle afgjort grund forfra.

## Eksempler

**Startup.** Et startup med fem medarbejdere tilføjer en almindelig `decisions/`-mappe til sit hovedrepo, med en note i to afsnit (kontekst og valg), hver gang nogen træffer et valg, deres fremtidige selv vil stille spørgsmål ved. Der er ingen livscyklus, ingen roller og ingen godkendere: blot vanen at skrive *hvorfor* ved siden af koden. Da deres første ansatte kommer til seks måneder senere, læser hun hele mappen på en time og holder op med at spørge "hvorfor er det bygget sådan?" Den lette log koster minutter pr. indførsel og sparer dem for den genopdagelsesafgift, der bider længe før et team vokser sig stort.

**Stor virksomhed.** En detailhandler med 30 ingeniørteams standardiserer på registre i MADR-format i hvert repo plus et søgbart centralt indeks. Da et nyt team står over for "[monorepo](https://en.wikipedia.org/wiki/Monorepo) versus multirepo", finder de tre tidligere registre med kontekst og konsekvenser og adopterer begrundelsen på en eftermiddag i stedet for en måned med debat. Centrale grænsebeslutninger (serviceejerskab, dataadgangsregler) understøttes af ArchUnit fitness functions, så overtrædelser fejler buildet i stedet for at blive fanget i gennemgang. Det er styring, der skalerer uden en central flaskehals.

**Offentlig sektor.** En myndighed, der moderniserer et ydelsessystem, kræver et ADR for hvert arkitektonisk væsentligt krav, hvert med kobling af beslutningen til det mandat eller den compliance-kontrol, det opfylder (tilgængelighed, dataopbevaringssted, reviderbarhed). Registre er uforanderlige og erstattede, hvilket producerer en sporbar log, der opfylder tilsynsgennemgang. Afgørende er det også, at den lader en efterfølgende konsulent forstå, *hvorfor* systemet har den form, det har, og bevarer kontinuitet over de flerårige, multi-leverandør-levetider, der er typiske for offentlige programmer (kapitel 4.6, 10.4).

## Business case: motivation, ROI og TCO

Et beslutningsregister koster minutter at skrive og nogle få flere at gennemgå. Afkastet er undgået *gen-beslutnings*omkostning og undgået *forkert-omstødelses*omkostning, begge store og tilbagevendende på langlivede systemer. Hver gang et team forhandler et afgjort spørgsmål forfra, eller omstøder et sundt valg, fordi ingen huskede begrænsningen bag det, betaler de i seniorers tid og ofte i en hændelse. En beslutningslog omsætter den tilbagevendende afgift til en engangsskrivning.

På **totale ejeromkostninger** er beslutningsregistre blandt den dokumentation med størst løftestang, du kan føre, fordi de rammer det enkeltstående mest udskiftningsfølsomme aktiv: begrundelse. Onboarding er hurtigere (nyansatte læser *hvorfor*, ikke kun koden). Modernisering er sikrere (kapitel 3.6: du kan skelne væsentlige beslutninger fra tilfældige). Revisioner er billigere (beviset findes allerede). Omkostningen ved *ikke* at føre dem er usynlig på ethvert dashboard, og den akkumuleres stille ved hver afgang. For at argumentere over for ledelsen, peg på en nylig dyr genopdagelse eller en omstødt beslutning, der forårsagede en hændelse, og bemærk, at rettelsen koster næsten intet at indføre.

## Anti-mønstre og faldgruber

- **At registrere *hvad* uden *hvorfor*:** udelade kontekst og afviste alternativer, selve pointen.
- **Papirarbejde bagefter:** registre skrevet for at opfylde et mandat, ikke for at tænke; de læses som hule, og ingen stoler på dem.
- **Mega-dokumenter med flere beslutninger:** én kæmpeside, ingen kan navigere eller erstatte rent.
- **Udaterede påstande:** omkostninger og begrænsninger, der engang var sande, præsenteret som tidløse.
- **Stille redigeringer:** at ændre en beslutnings historik uden en dateret note, hvilket ødelægger revisionssporet.
- **Skrive-kun-logs:** registre skabt og aldrig bragt frem i det øjeblik, de er relevante, så de ikke påvirker adfærd.
- **Forkortelsesportvagt:** at insistere på "ADR" og "arkitektur" og dermed afskrække bidrag.
- **Ingen livscyklus:** registre, der aldrig gennemgås, erstattes eller udfases, og forfalder til misinformation.

## Modenhedsmodel

- **Niveau 1 (Opstart):** Beslutninger lever i folks hoveder, chattråde og commit-beskeder; registrering er reaktiv og ad hoc, og begrundelse går rutinemæssigt tabt med personaleudskiftning.
- **Niveau 2 (Udvikling):** Nogle teams fører registre, i varierende formater og skabeloner, når en enkelt person husker det; praksis er uens på tværs af teams, uden fælles log, navngivning eller proces.
- **Niveau 3 (Standardisering):** Én enkelt skabelon, lagring i repo og en defineret livscyklus og styring (kriterier for at rejse/springe over, roller, gennemgangskadence) er dokumenteret og anvendt ensartet i hele organisationen; registre gennemgås og erstattes frem for at blive redigeret stille.
- **Niveau 4 (Styring):** Beslutningsloggen måles mod baselines: dækning (andelen af arkitektonisk væsentlige beslutninger, der bærer et register), friskhed (andelen af registre gennemgået inden for deres kadence, plus antallet af udaterede eller forældede påstande) og synlighed (hvor ofte et relevant register faktisk nåede den udvikler, der ændrede den styrede kode). Ansvarlige vedligeholdere handler på disse mål, erstatter forældede registre og lukker dækningshuller på grundlag af dokumentation frem for anekdote.
- **Niveau 5 (Orkestrering):** En søgbar beslutningslog på tværs af teams er integreret i det daglige arbejde: relevante registre dukker automatisk op ved de ændringer, de styrer, centrale beslutninger sikres af fitness functions i continuous integration, og loggen fodrer onboarding, modernisering og revision som et levende aktiv. Organisationen forbedrer løbende selve praksissen, udfaser, erstatter og omdefinerer registre, efterhånden som systemet og dets begrænsninger skifter, og omfordeler, hvor den investerer stringens, efterhånden som porteføljen af beslutninger vokser.

## Idéer til drøftelse

1. Hvad var den sidste beslutning, dit team omstødte eller genforhandlede, fordi ingen huskede den oprindelige begrundelse?
2. Ville en omdøbning af jeres `adr/`-bibliotek til `decisions/` ændre, hvem der bidrager, og hvad der bliver registreret?
3. Hvilke af jeres kritiske beslutninger kunne i dag sikres af en automatiseret fitness function?
4. Uforanderlig-og-erstat eller levende dokument: hvilket passer til jeres revisionsforpligtelser og jeres kultur, og hvorfor?
5. Hvordan ville en ny ansat (eller en efterfølgende konsulent) i dag opdage, *hvorfor* jeres system har den form, det har?
6. Hvad retfærdiggør at rejse et beslutningsregister på dit team, og hvad retfærdiggør *ikke* at rejse et?

## Vigtigste pointer

- Et beslutningsregister fastholder én vigtig beslutning med dens **kontekst og konsekvenser**: *hvorfor*, ikke kun *hvad*.
- Hold registre **specifikke, tidsstemplede og lette**; standardisér på én skabelon (Nygard, MADR eller lignende).
- Opbevar dem **i versionsstyring ved siden af koden**; overvej at kalde dem "decisions" for at udvide bidrag.
- Definér en **livscyklus og styring** (kriterier for at rejse/springe over, roller, gennemgangskadence); forbehold tung proces til envejsdør-beslutninger.
- Gør beslutninger **synlige** i ændringens øjeblik og, hvor muligt, **testbare** via fitness functions.
- ROI er undgået genopdagelses- og forkert-omstødelsesomkostning; TCO-argumentet er stærkest, hvor udskiftning, modernisering og revision betyder mest. Se kapitel 1.5 (beslutningstagning og styring) og kapitel 3.1 (arkitekturgrundlag).

## Referencer og videre læsning

- Michael Nygard, "Documenting Architecture Decisions" (2011): the foundational lightweight ADR.
- MADR: Markdown Any Decision Records project (adr.github.io/madr).
- Jeff Tyree and Art Akerman, "Architecture Decisions: Demystifying Architecture" (*IEEE Software*, 2005).
- Olaf Zimmermann, "Y-Statements" and "Architectural Decision Making" (ozimmer.ch).
- Joel Parker Henderson, *Architecture Decision Record (ADR)*: templates, examples, and teamwork guidance (github.com/joelparkerhenderson/architecture-decision-record).
- ThoughtWorks Technology Radar: "Lightweight Architecture Decision Records."
- Neal Ford, Rebecca Parsons, Patrick Kua, Pramod Sadalage, *Building Evolutionary Architectures* (fitness functions).
- AWS Prescriptive Guidance, "ADR process"; Red Hat, "Why you should use ADRs."
- Wikipedia, "Architectural decision" and "Architecturally significant requirements."
