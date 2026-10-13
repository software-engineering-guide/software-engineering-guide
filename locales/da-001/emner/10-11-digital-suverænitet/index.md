# 10.11 Digital suverænitet

## Overblik og motivation

[Digital suverænitet](https://en.wikipedia.org/wiki/Digital_sovereignty) er den grad, hvori en organisation, nation eller blok bevarer meningsfuld kontrol over sine egne data, sin software og sin infrastruktur. Det betyder kontrol over, hvor data fysisk befinder sig, hvilke love og regeringer der kan tvinge adgang til dem, og om kritiske systemer kan fortsætte med at fungere uden at afhænge af en fremmed magt eller en enkelt leverandør. Den har flere dimensioner: **[datasuverænitet](https://en.wikipedia.org/wiki/Data_sovereignty)** (hvis jurisdiktion og love styrer dataene), **driftssuverænitet** (evnen til at drive og administrere systemer uden en tredjeparts tilladelse eller tilstedeværelse), **softwaresuverænitet** (adgang til og kontrol over kildekoden og dens udvikling) og **forsyningskædesuverænitet** (frihed fra flaskehalse i hardware, tjenester og afhængigheder). Dette kapitel sidder i ledelsesdelen, fordi suverænitet grundlæggende er en strategi-, indkøbs- og risikobeslutning (kapitel 10.1–10.3) med dybe tekniske konsekvenser.

Motivationen er rykket fra teoretisk til presserende. [Cloud computing](https://en.wikipedia.org/wiki/Cloud_computing) koncentrerede en stor del af verdens infrastruktur hos en håndfuld udbydere, for det meste under ét lands jurisdiktion. Ekstraterritoriale love som den amerikanske [CLOUD Act](https://en.wikipedia.org/wiki/CLOUD_Act) (som kan tvinge en udbyder til at udlevere data, uanset hvor de er lagret) støder sammen med regimer som EU's [GDPR](https://en.wikipedia.org/wiki/General_Data_Protection_Regulation), en spænding krystalliseret af *[Schrems II](https://en.wikipedia.org/wiki/Schrems_II)*-dommen, der ugyldiggjorde EU-USA Privacy Shield. Tilføj geopolitiske chok, sanktioner og risikoen for, at en udbyder bliver afskåret, og afhængighed bliver en strategisk sårbarhed, ikke blot en fodnote i leverandørstyring. Suverænitet er disciplinen at afgøre, bevidst, hvor meget af den afhængighed jeres mest kritiske systemer og data sikkert kan bære.

For virksomheder og især det offentlige er indsatsen direkte. Multinationale virksomheder skal forene modstridende databeskyttelsesregimer og undgå en indlåsning, som en tilsynsmyndighed eller en geopolitisk begivenhed kunne forvandle til en eksistentiel migrering. Regeringer holder data (sundhedsjournaler, skat, forsvar, borgeridentitet), hvis eksponering for en fremmed jurisdiktion er et nationalt sikkerheds- og offentlig tillidsspørgsmål. Det er grunden til, at "suveræn cloud"-tilbud, initiativer som EU's [Gaia-X](https://en.wikipedia.org/wiki/Gaia-X) og nationale certificeringer som Frankrigs SecNumCloud er opstået. Målet er ikke selvforsyning. Det er proportional kontrol afstemt med følsomheden af det, der er på spil.

## Grundprincipper

- **Suverænitet er et spektrum, ikke en kontakt.** Afstem graden af kontrol med data- og arbejdsbyrdens følsomhed.
- **Placering er ikke jurisdiktion.** Data lagret lokalt kan stadig være juridisk tilgængelige for en fremmed regering; opbevaringssted alene er ikke suverænitet.
- **Design til udtrædelse.** Evnen til at forlade en udbyder er det sandeste mål for suverænitet.
- **[Åbne standarder](https://en.wikipedia.org/wiki/Open_standard) og [open source](https://en.wikipedia.org/wiki/Open-source_software) reducerer afhængighed:** de er værktøjer til strategisk autonomi, ikke blot omkostningsbesparere.
- **Kontrollér nøglerne.** Hvem der holder og kontrollerer krypteringsnøgler betyder ofte mere end, hvor bytes sidder.
- **Undgå at bytte én indlåsning for en anden.** En enkelt "suveræn" leverandør kan være lige så fangende som en hyperscaler.
- **Vær proportional.** Suverænitet har reelle omkostninger; at overrotere overalt spilder penge og sinker levering.

## Anbefalinger

### Klassificér data og arbejdsbyrder efter suverænitetsfølsomhed

Ikke alt har brug for samme beskyttelse. Klassificér data og systemer efter konsekvensen af adgang fra en fremmed jurisdiktion eller tab af udbyder. Offentlige og lavrisiko-arbejdsbyrder kan ligge på global hyperscale-infrastruktur af hensyn til skala og omkostning. Stærkt følsomme data (national sikkerhed, sundhed, borgeridentitet, regulerede poster) berettiger stærkere suverænitetskontroller. Denne niveauinddeling, den samme risikobaserede logik som dataklassificering i kapitel 4.5, er, hvad holder suverænitet overkommelig og fokuserer dyre kontroller, hvor de er berettigede, frem for at lokalisere alt.

### Forstå jurisdiktion, ikke blot opbevaringssted

**Dataopbevaringssted** (den fysiske eller geografiske placering, hvor data lagres) er nødvendigt, men ikke tilstrækkeligt. Det, der betyder noget juridisk, er *jurisdiktion*: hvilke regeringer der kan tvinge udlevering og under hvilke love. Et datasæt holdt i et datacenter i landet, drevet af en udbyder med hovedsæde i udlandet, kan stadig være tilgængeligt under udbyderens hjemlands lov (CLOUD Act-problemet). Kortlæg hvert systems juridiske eksponering: udbyderens hovedsæde, gældende love og eventuelle tilstrækkelighedsafgørelser eller overførselsmekanismer (Standard Contractual Clauses, EU-USA Data Privacy Framework). Behandl så det juridiske kort som en førsteklasses del af arkitekturen (kapitel 4.5, 4.6).

### Design til portabilitet og reversibilitet

Den mest varige suverænitetskontrol er en troværdig udtrædelse. Foretræk åbne standarder og portable formater (kapitel 3.8). Containerisér arbejdsbyrder, så de kan flytte. Hold infrastruktur som kode (kapitel 8.2), så et miljø kan genopbygges andetsteds. Undgå dyb afhængighed af en enkelt udbyders proprietære tjenester for jeres mest kritiske systemer. Vedligehold og *test* periodisk en udtrædelsesplan, en depotordning for data og konfiguration plus en øvet sti til et alternativ, så "vi kunne forlade den, hvis vi måtte" er et påvist faktum, ikke et håb. Det er modgiften mod **[leverandørindlåsning](https://en.wikipedia.org/wiki/Vendor_lock-in)**, tilstanden at være ude af stand til at skifte udbyder uden uoverkommelig omkostning eller forstyrrelse.

### Brug suveræn infrastruktur og nøglekontrol, hvor det er berettiget

For det mest følsomme niveau findes stærkere tekniske kontroller: **suveræn cloud**-tilbud (cloudregioner drevet af eller i partnerskab med enheder inden for jurisdiktionen, nogle gange certificerede som SecNumCloud), **[confidential computing](https://en.wikipedia.org/wiki/Confidential_computing)** (hardwarebaseret betroet eksekvering, der holder data krypteret selv mens de behandles) og kundekontrollerede krypteringsnøgler: **bring your own key (BYOK)** og, stærkere, **hold your own key (HYOK)**, hvor udbyderen aldrig har adgang til de nøgler, der låser dataene op. At kontrollere nøglerne kan levere meget af den praktiske fordel ved suverænitet selv på delt infrastruktur. Data, en udbyder ikke kan dekryptere, er data, den ikke meningsfuldt kan udlevere.

### Foretræk open source og åbne økosystemer til strategisk autonomi

Open source-software og åbne standarder er blandt de stærkeste suverænitetsløftestænger, fordi de fjerner den enkelte leverandørs nødkontakt. Kildekoden kan køres, revideres, forkes og vedligeholdes uafhængigt af enhver enkelt leverandør (kapitel 10.3, 3.8). Offentlige "public money, public code"-politikker og initiativer som Gaia-X afspejler dette. Open source er ikke automatisk suveræn. Den kræver stadig dygtige folk til at køre og understøtte den, og dens forsyningskæde skal sikres (kapitel 4.2). Men den konverterer afhængighed af en leverandør til afhængighed af et fællesskab og jeres egen kapabilitet, hvilket er langt lettere at kontrollere.

### Styr suverænitet som en proportional risiko, ikke en absolut

Rejs et suverænitetsrisikorammeværk ved siden af jeres anden styring (kapitel 10.2, 1.5). Vurdér koncentrations- og jurisdiktionsrisikoen ved større platforme. Afgør målsuverænitetsniveauer pr. dataniveau, og vej dem mod omkostning, kapabilitet og leveringsfart. Målet er en forsvarlig, dokumenteret position ("disse arbejdsbyrder accepterer hyperscale-afhængighed; disse kræver kontrol inden for jurisdiktionen; her er vores udtrædelsesholdning"), gennemgået, efterhånden som geopolitik og regulering ændrer sig, ikke en engangsabsolut holdning.

## Afvejninger: fordele og ulemper

| Tilgang | Fordele | Ulemper |
|---|---|---|
| **Global hyperscale-cloud** | Skala, funktioner, lav omkostning, fart | Jurisdiktionseksponering; koncentrations- og indlåsningsrisiko |
| **Suveræn cloud / udbyder inden for jurisdiktionen** | Juridisk kontrol; national sikkerhedspasform; tillid | Højere omkostning; færre funktioner; ofte mindre skala; ny indlåsning |
| **Nøglekontrol (BYOK/HYOK) på delt infrastruktur** | Meget af fordelen til lavere omkostning; bevarer skala | Driftskompleksitet; nøgleforvaltningsrisiko; ikke absolut |
| **Open source / selvhostet** | Revisionsbarhed, forkbarhed, ingen leverandørs nødkontakt | Kræver intern kapabilitet; I ejer driften og sikkerheden |
| **Datalokaliseringsmandater** | Regulatorisk compliance; politisk sikkerhed | Dyrt; fragmenterer data; kan reducere robusthed og anvendelighed |

Den definerende spænding er **kontrol versus kapabilitet og omkostning**. Maksimal suverænitet (selvhostet, inden for jurisdiktionen, open source, fuldt portabel) ofrer skalaen, funktionerne og farten fra globale platforme. Maksimal kapabilitet accepterer afhængighed og jurisdiktionseksponering. Løsningen er niveauinddeling: betal for suverænitet, hvor konsekvensen berettiger det, og tag pragmatisk afhængighed, hvor den ikke gør.

## Spørgsmål til drøftelse med dit team

1. **Har vi inddelt vores data og arbejdsbyrder efter suverænitetsfølsomhed, så dyre kontroller kun lander, hvor de er berettigede?** Suverænitet er et spektrum, ikke en kontakt, og at lokalisere alt brænder penge, opgiver kapabilitet og kan endda reducere robusthed ved at skrumpe jeres muligheder. Klassificér hvert system efter konsekvensen af adgang fra en fremmed jurisdiktion eller tab af udbyder: offentlige og lavrisiko-arbejdsbyrder kan ligge på global hyperscale-infrastruktur, mens data om national sikkerhed, sundhed eller borgeridentitet berettiger stærkere kontroller. Det er den samme risikobaserede logik som dataklassificering, og det er, hvad holder suverænitet overkommelig. Tag jeres kronjuvel-systemer og deres nuværende hosting med, og spørg, om beskyttelsen matcher følsomheden. Hvis I beskytter alt ens, betaler I næsten sikkert for meget et sted og er eksponerede et andet.

2. **Er åbne standarder og open source en del af vores suverænitetsstrategi, eller behandler vi dem kun som omkostningsbesparere?** Kildekode, I kan køre, revidere, forke og vedligeholde, fjerner den enkelte leverandørs nødkontakt, hvilket er en af de stærkeste autonomiløftestænger, I har. Åbne standarder og portable formater er, hvad gør en troværdig udtrædelse mulig, og en troværdig udtrædelse er det sandeste mål for suverænitet. Den mere subtile fælde er at undslippe en hyperscaler blot for at blive helt fanget af én "suveræn" leverandør uden udtrædelse: I byttede én indlåsning for en anden. Tag jeres mest kritiske platforme med, og spørg, hvor tæt hver er bundet til én udbyders proprietære tjenester. Hvor svaret er "meget", er åbne standarder og containeriserede, genopbyggelige miljøer den billigste måde at løsne grebet på.

3. **Hvem ejer vores suverænitetsrisikorammeværk, og hvor ofte gensyne vi holdningen, efterhånden som lov og geopolitik skifter?** En suverænitetsposition sat én gang og aldrig gennemgået bliver fiktion i det øjeblik, en dom, sanktion eller ny lov lander, og de chok kommer nu regelmæssigt. Rejs et levende rammeværk ved siden af jeres anden styring: vurdér koncentrations- og jurisdiktionsrisikoen ved større platforme, sæt målsuverænitetsniveauer pr. dataniveau, og dokumentér en forsvarlig position, I kan vise en tilsynsmyndighed. Navngiv ejeren og gennemgangskadencen. Tag spørgsmålet med om, hvordan en sanktion eller ugunstig dom mod jeres hovedudbyder ville ramme jeres kritiske tjenester i næste uge; hvis ingen kan svare, findes rammeværket endnu ikke.

4. **Hvem holder krypteringsnøglerne til vores mest følsomme data, og kunne vores udbyder tvinges til at udlevere de data i læsbar form?** Opbevaringssted og selv en "suveræn" region betyder lidt, hvis operatøren beholder nøglerne, fordi en udleveringskendelse så rammer dekrypterede data, uanset hvor bytes sidder. At kontrollere nøglerne selv, gennem bring your own key eller den stærkere hold your own key, hvor udbyderen aldrig ser dem, leverer ofte det meste af den praktiske fordel ved suverænitet på delt infrastruktur til en brøkdel af omkostningen ved at flytte alt. Det modstridende hensyn er operationelt: nøgleforvaltning er skånselsløs, og en tabt eller fejlhåndteret nøgle kan låse jer ude af jeres egne data lige så sikkert som enhver sanktion. Tag en fortegnelse over, hvilke datasæt der er krypterede, hvem der faktisk holder hver nøgle, og hvad jeres genoprettelsessti er, hvis en nøgle går tabt, med, og kortlæg det så mod jeres suverænitetsniveauer. For virksomheder og det offentlige så behandl nøgleforvaring som den linje, der afgør, om en fremmed udleveringskendelse returnerer chiffertekst eller klartekst, og gør det til et indkøbskrav frem for en senere eftermontering.

5. **Kunne vi faktisk forlade vores primære udbyder inden for en tidsramme, der betyder noget, og hvornår øvede vi det sidst?** En troværdig udtrædelse er det sandeste mål for suverænitet, og alligevel lever de fleste udtrædelsesplaner på papir og er aldrig blevet kørt, så portabilitet forbliver et håb frem for et påvist faktum. Spændingen er omkostning og fokus: at øve en udtrædelse, holde arbejdsbyrder containeriserede og holde en depotordning for data og konfiguration forbruger alt sammen ingeniøropmærksomhed, som leveringspres hellere ville bruge andetsteds. Tag jeres mest kritiske system, et ærligt estimat af, hvor lang tid en tvungen migrering ville tage, listen over proprietære tjenester det afhænger af og datoen for jeres sidste faktiske øvelse (hvis nogen) med. For en stor eller offentlig organisation, der bærer flerårige udtrædelsesforpligtelser i kontrakt, er en uøvet udtrædelse en forpligtelse, I måske juridisk ikke kan opfylde, så behandl en øvelseskadence som en del af systemets løbende omkostning, ikke en valgfri øvelse.

6. **For hvert kronjuvel-system, ved vi hvilke regeringer der i dag lovligt kan tvinge adgang til det, uanset hvor dataene fysisk sidder?** Placering er ikke jurisdiktion: data i et datacenter i landet kan stadig være tilgængelige under hjemlandslovgivningen for en operatør med hovedsæde i udlandet, og teams forveksler rutinemæssigt opbevaringssted med juridisk beskyttelse. Det svære er, at svaret kræver juridisk og indkøbsmæssigt input, ikke blot et arkitekturdiagram, og kortet skifter, efterhånden som tilstrækkelighedsafgørelser, domme og overførselsmekanismer ændrer sig. Tag for hvert kritisk datasæt udbyderens hovedsæde, de love der rækker til det, og den overførselsmekanisme, I støtter jer til, med, og vær ærlige, hvor ingen faktisk ved det. I regulerede og offentlige sammenhænge er en ukortlagt juridisk eksponering på borger- eller national sikkerhedsdata et fund, der venter på at ske ved den næste revision, så finansiér den juridiske kortlægning lige så eksplicit, som I finansierer infrastrukturen.

## Sektorperspektiv

**Startup.** Fart og runway dominerer, så køb suverænitet som en tynd funktion frem for at bygge en suveræn stak, I ikke kan bemande. Hvis en kundes jurisdiktion er begrænsningen, så udrul til jeres eksisterende udbyders in-region-mulighed, hold jeres egne krypteringsnøgler, så operatøren ikke kan dekryptere følsomme poster, og hold arbejdsbyrden containeriseret, så den forbliver portabel. Det lukker aftalen til en seed-stadie-omkostning og undgår en re-arkitektur, I ikke har runway til.

**Lille virksomhed.** Uden en suverænitetsspecialist og med et stramt budget så behandl dette som et kontraktgennemgangs- og leverandørvalgsspørgsmål, ikke et ingeniørprogram. Foretræk leverandører, der tilbyder regioner inden for jurisdiktionen, åbne databehandlingsvilkår og kundeholdte nøgler som standardfunktioner, og læs underdatabehandler- og udleveringsklausulerne, før I underskriver. Selvhosting for suverænitet betaler sig sjældent her: I ville arve drifts- og sikkerhedsbyrden uden folkene til at bære den.

**Stor virksomhed.** Opgaven er porteføljestyring på tværs af mange teams: en fælles niveauinddeling af data efter suverænitetsfølsomhed, et koncentrationsrisikobillede af, hvor megen kritisk belastning der sidder hos én udbyder eller i én jurisdiktion, og standardiseret nøglekontrol, portabilitet og udtrædelsesøvelser, så hver gruppe holder op med at lave sit eget ukoordinerede væddemål. Budgettér den højere omkostning og driftsbyrde ved det følsomme niveau eksplicit, og hold en dokumenteret, revisionsbar holdning, I kan vise en tilsynsmyndighed. Styr suverænitet som en levende risiko med målinger og gennemgangskadence, ikke en engangsmigrering.

**Offentlig sektor.** Indkøbsregler, åbenhed og offentlig ansvarlighed former hvert valg. Foretræk certificeret suveræn infrastruktur (for eksempel SecNumCloud-lignende kvalificering) og åbne standarder og open source, så platformen kan vedligeholdes uafhængigt af enhver enkelt leverandør, og kræv portabilitet og oplysning om juridisk eksponering i selve kontrakten. Offentliggør en beskrivelse i almindeligt sprog af, hvor borgerdata sidder, og hvem der kan nå dem, forbehold dyre suveræne kontroller til det reelt følsomme niveau, og hold mindre følsomme offentlige tjenester på billigere global infrastruktur.

## Eksempler

**Startup.** Et lille sundhedsteknologisk startup lander sin første hospitalskunde i Tyskland, som kræver, at patientdata forbliver under EU-jurisdiktion. I stedet for at overbygge en suveræn stak, det ikke har råd til, udruller grundlæggerne til deres eksisterende cloududbyders EU-region, holder deres egne krypteringsnøgler, så udbyderen ikke kan dekryptere de følsomme poster, og holder arbejdsbyrden containeriseret, så den forbliver portabel. Det køber det meste af den suverænitetsfordel, kunden har brug for, til en omkostning et seed-stadie-team kan bære, og det lukker aftalen uden en total re-arkitektur.

**Stor virksomhed.** En multinational bank skal holde visse kundedata inden for EU og uden for rækkevidde af fremmed udleveringslovgivning. I stedet for at opgive sin globale cloududbyder niveauinddeler den sin ejendom. Generelle arbejdsbyrder forbliver på hyperscale-regioner af hensyn til skala. Regulerede kundedata kører i EU-regioner med **hold your own key**-kryptering (udbyderen kan ikke dekryptere dem) og en afprøvet udtrædelsesplan til en alternativ udbyder. Det tilfredsstiller tilsynsmyndigheder og bankens egen koncentrationsrisikoappetit (kapitel 10.2) uden en total, kapabilitetsdræbende migrering.

**Offentlig sektor.** En national sundhedstjeneste holder borgeres sundhedsjournaler og vurderer eksponering for en fremmed jurisdiktion som uacceptabel. Den indkøber en suveræn cloud, altså infrastruktur drevet af en enhed i landet under national certificering (f.eks. SecNumCloud-lignende), med confidential computing til den mest følsomme behandling, og påbyder åbne standarder (kapitel 3.8) og open source-komponenter, så platformen kan vedligeholdes uafhængigt af enhver enkelt leverandør. Den højere omkostning og det snævrere funktionssæt accepteres som prisen for national sikkerhedskontrol og offentlig tillid. I mellemtiden forbliver mindre følsomme tjenester (en offentlig informationsportal) på billigere global infrastruktur.

## Business case: motivation, ROI og TCO

Økonomien i digital suverænitet er asymmetrisk og bedst ramt ind som forsikring mod lavsandsynlige, højpåvirknings-begivenheder. Omkostningerne er synlige og tilbagevendende: suveræn infrastruktur og infrastruktur inden for jurisdiktionen er typisk dyrere, tilbyder færre administrerede tjenester og kræver mere intern driftskapabilitet, hvilket alt sammen hæver den samlede ejeromkostning og kan sinke levering. Fordelene er for det meste undgåede katastrofer: regulatoriske bøder og tvungen re-arkitektur efter en dom som *Schrems II*, et forretningsafsluttende tab af adgang, hvis en udbyder sanktioneres eller afskæres, eller den omdømmemæssige og nationale sikkerhedsskade ved fremmed udlevering af følsomme data. Fordi disse hale-begivenheder er alvorlige og i stigende grad plausible, er proportional investering i suverænitet, især billige-men-kraftfulde kontroller som nøgleejerskab, portabilitet og åbne standarder, ofte stærkt positiv forventningsværdi, selv om den ser ud som ren omkostning i et regneark for stabil tilstand.

Fælden på begge sider er uproportionalitet. *Under*-investering efterlader kritiske data og systemer eksponerede for en enkelt jurisdiktion eller leverandør uden udtrædelse og forvandler en håndterbar risiko til en eksistentiel. *Over*-investering, ved at lokalisere alt og afvise alle globale platforme, brænder penge, opgiver kapabilitet og kan *reducere* robusthed ved at skrumpe jeres muligheder. For at fremlægge sagen for ledelsen så bind suverænitetsforbrug til en data-og-arbejdsbyrde-risikoniveauinddeling. Kvantificér koncentrations- og jurisdiktionseksponeringen for kronjuvel-systemerne. Prissæt de billige kontroller (nøgler, portabilitet, udtrædelsesøvelser), der nedbringer risikoen ved dem. Forbehold dyr suveræn infrastruktur til det niveau, der reelt berettiger det.

## Anti-mønstre og faldgruber

- **Suverænitetsteater:** at reklamere med dataopbevaring i landet, mens en udbyder med hovedsæde i udlandet beholder juridisk adgang til dataene.
- **At forveksle kryptering med suverænitet:** at kryptere data, men lade udbyderen holde nøglerne, så den stadig kan tvinges til at dekryptere.
- **Overrotation:** at lokalisere og selvhoste alt til ruinøs omkostning og reduceret kapabilitet, uanset følsomhed.
- **Ny enkelt indlåsning:** at undslippe en hyperscaler ved at blive helt fanget af én "suveræn" leverandør uden udtrædelse.
- **Ingen afprøvet udtrædelse:** en udtrædelsesplan, der eksisterer på papir, men aldrig er øvet, så portabilitet er upåvist.
- **At ignorere den menneskelige forsyningskæde:** at antage, at open source eller selvhosting giver suverænitet uden de dygtige folk til at køre den.
- **Statisk holdning:** at sætte en suverænitetsposition én gang og aldrig gensyne den, efterhånden som lov og geopolitik skifter.

## Modenhedsmodel

- **Niveau 1 (Opstart):** Suverænitet er uovervejet og reaktiv; data og kritiske systemer sidder, hvor det er billigst, uden kort over jurisdiktions- eller koncentrationsrisiko og uden ejer.
- **Niveau 2 (Udvikling):** Dataopbevaringssted adresseres for de mest åbenlyse regulerede data på nogle projekter, men jurisdiktion, nøglekontrol og udtrædelse overvejes ikke systematisk; praksis varierer team for team, og afhængighed af enkelte udbydere er uundersøgt.
- **Niveau 3 (Standardisering):** Data og arbejdsbyrder er inddelt i niveauer efter suverænitetsfølsomhed under en dokumenteret politik anvendt i hele organisationen; jurisdiktion er kortlagt; nøglekontrol, portabilitet og åbne standarder er påkrævet på følsomme niveauer; udtrædelsesplaner findes og er påbudt frem for valgfrie.
- **Niveau 4 (Styring):** Holdningen måles og styres mod baselines: koncentrationsrisiko (andelen af kritiske arbejdsbyrder hos én udbyder eller i én jurisdiktion), nøgleejerskabsdækning på tværs af følsomme datasæt, jurisdiktionskortlægningens fuldstændighed og øvede udtrædelsestider følges som målinger, rapporteres til styring og håndhæves mod tærskler, så en drivende afhængighed udløser handling på dokumentation frem for efter et chok.
- **Niveau 5 (Orkestrering):** Suverænitet forbedres løbende og er integreret på tværs af organisationen: det levende risikorammeværk fodrer arkitektur-, indkøbs- og risikoplanlægning som standard, udtrædelser øves rutinemæssigt, og organisationen omafgrænser adaptivt niveauer, rebalancerer udbydere og reviderer sin holdning, efterhånden som domme, sanktioner og regulering skifter.

## Idéer til drøftelse

1. For jeres mest følsomme datasæt, hvilke regeringer kan lovligt tvinge adgang til det i dag, og ved I det?
2. Er jeres dataopbevaringssted reel suverænitet, eller holder en udbyder med hovedsæde i udlandet stadig nøglerne og den juridiske eksponering?
3. Kunne I faktisk forlade jeres primære cloududbyder, hvis I skulle, og har I nogensinde testet det?
4. Hvilke af jeres arbejdsbyrder har reelt brug for suveræn infrastruktur, og hvilke overbeskytter I til unødig omkostning?
5. Hvor ville kontrol over jeres egne krypteringsnøgler give jer det meste af suverænitetsfordelen til en brøkdel af omkostningen?
6. Hvordan ville en sanktion, et udfald eller en juridisk dom mod jeres hovedudbyder påvirke jeres kritiske tjenester i næste uge?

## Vigtigste pointer

- Digital suverænitet er proportional kontrol over jeres data, software og infrastruktur, på tværs af data-, drifts-, software- og forsyningskædedimensionerne.
- **Placering er ikke jurisdiktion:** opbevaringssted alene forhindrer ikke fremmed juridisk adgang; kortlæg, hvem der kan tvinge udlevering.
- **Design til udtrædelse** og **kontrollér jeres nøgler:** portabilitet og nøgleejerskab er de kontroller med højest løftestang og laveste omkostning.
- **Åbne standarder og open source** er værktøjer til strategisk autonomi; forbehold dyr **suveræn cloud** til det niveau, der berettiger det.
- Styr suverænitet som en **proportional, levende risiko** (kapitel 10.2, 10.3, 4.5, 4.6, 3.8) og undgå både underbeskyttelse og ruinøs overrotation.
- ROI er forsikring mod alvorlige hale-begivenheder (regulatoriske, geopolitiske og indlåsning) prissat mod reel, tilbagevendende omkostning.

## Referencer og videre læsning

- European Court of Justice, *Data Protection Commissioner v. Facebook Ireland and Maximillian Schrems* ("Schrems II", 2020).
- Regulation (EU) 2016/679, *General Data Protection Regulation (GDPR)*; Regulation (EU) 2023/2854, *Data Act*.
- U.S. *Clarifying Lawful Overseas Use of Data (CLOUD) Act* (2018).
- ANSSI, *SecNumCloud* qualification framework (France).
- Gaia-X European Association for Data and Cloud (Gaia-X initiative).
- ENISA, reports on cloud security and EU cybersecurity certification (EUCS).
- Julia Pohle and Thorsten Thiel, "Digital Sovereignty" (*Internet Policy Review*, 2020).
- Bert Hubert, writings on European digital autonomy and dependency on foreign providers.
- Kai Zenner and others, analyses of EU digital sovereignty policy (for context; verify current sources).
