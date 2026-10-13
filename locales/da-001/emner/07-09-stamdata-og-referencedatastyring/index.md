# 7.9 Stamdata- og referencedatastyring

## Overblik og motivation

Spørg fem systemer, hvor mange kunder organisationen har, og I får fem forskellige tal. Ét tæller e-mailadresser, ét tæller kontrakter, ét tæller logins, og to er uenige om, hvorvidt "Acme Corp" og "ACME Corporation" er samme virksomhed. [Stamdatastyring](https://en.wikipedia.org/wiki/Master_data_management) (MDM, master data management) er disciplinen at afstemme de kerneentiteter, jeres forretning deler, kunde, produkt, leverandør, medarbejder, lokation, til én autoritativ version, hvert system kan stole på.

Begynd med at sortere jeres data i tre slags, fordi de kræver forskellig behandling. Stamdata beskriver forretningens navneord: de personer, steder og ting, som mange processer henviser til. Referencedata er det kontrollerede ordforråd, de processer bruger: valutakoder, landekoder, lister over måleenheder, produktkategorier. Transaktionsdata registrerer udsagnsordene: en ordre afgivet, en betaling foretaget, en forsendelse sendt. Stamdata og referencedata har lavere volumen end transaktioner, men refereres overalt, så en fejl i dem forurener alt nedstrøms.

Omkostningen ved at gøre det forkert er konkret. Når den samme kunde findes som fire let forskellige poster, sender I fire kataloger, I kan ikke se en eneste relation værd at bevare, og jeres omsætning pr. kunde er stille forkert. En [golden record](https://en.wikipedia.org/wiki/Single_source_of_truth), den enkelte betroede version af en entitet samlet fra mange kilder, er det, der erstatter de modstridende kopier, så hver integration holder op med at genløse det samme matchingproblem.

For virksomheder, der afstemmer systemer ophobet gennem årtiers vækst og opkøb, er MDM forskellen mellem et sammenhængende kundebillede og en permanent afstemningsskat. For det offentlige stiger indsatsen: en borger, der optræder som tre forskellige personer i tre agenturer, kan blive nægtet en ydelse, beskattet to gange eller tabt mellem afdelinger. Dette kapitel supplerer datastrategi og datastyring (kapitel 7.1), som sætter ejerskab og politik; datamodellering og det semantiske lag (kapitel 7.7), som definerer, hvad entiteter betyder; og datakvalitet og observerbarhed (kapitel 7.8), som holder poster rene over tid.

## Grundprincipper

- Sortér jeres data i stam-, reference- og transaktionsdata; hver kræver forskellig håndtering.
- Én golden record pr. entitet i den virkelige verden, samlet bevidst, ikke opdaget ved et tilfælde.
- Vælg en MDM-arkitekturstil, der passer til jeres behov for kontrol og latens, ikke til mode.
- Matching og survivorship er forretningsregler, så skriv dem ned, og lad stewards justere dem.
- Referencedata er fælles ordforråd; versionér det, og offentliggør det som en API.
- Styring og stewardship er MDM's motor; softwaren er blot værktøjet.
- Udbred golden records som hændelser, så nedstrøms systemer holdes synkroniserede, ikke forældede.
- Mål MDM på forbedrede beslutninger og fjernede dubletter, ikke på indlæste poster.

## Anbefalinger

### Klassificér først stam-, reference- og transaktionsdata

I kan ikke styre det, I ikke har sorteret, så begynd med at klassificere jeres datadomæner. En nyttig test for stamdata er, om en forkert værdi forplanter sig: hvis én dårlig adresse bølger ind i fakturering, forsendelse og juridiske meddelelser, ser I på stamdata. Det styrer jeres investering: I bygger en matchingmotor til kundeentiteten, ikke til ordrelinjer. Navngiv domænerne eksplicit, rangér dem efter, hvor meget smerte deres duplikering forårsager, og begynd med det ene eller de to, der gør mest ondt, som regel kunde og produkt, fordi de berører omsætning direkte.

### Vælg en MDM-arkitekturstil bevidst

Der er fire almindelige arkitekturstile, og den rette afhænger af, hvor meget autoritet I kan centralisere, og hvor hurtigt ændringer skal udbredes. Registerstilen lader data blive i kildesystemerne og bygger kun et indeks over matchede identifikatorer, så den kan svare "disse fem poster er samme kunde" uden at flytte nogen data; den er billig og lavrisiko, men skrivebeskyttet, så den kan ikke rette kilderne. Konsolideringsstilen trækker kopier ind i en central hub og fletter dem til golden records til rapportering, men skubber ikke rettelser tilbage, så kilderne forbliver rodede. Sameksistensstilen går videre: den synkroniserer rensede værdier tilbage til kildesystemerne, så kilderne forbedres over tid, mens de stadig fungerer uafhængigt. Den centraliserede eller transaktionelle hub-stil gør MDM-hubben til selve kildesystemet, hvor entiteter oprettes og redigeres direkte, og hvert andet system forbruger fra den; det giver den stærkeste konsistens og kontrol, og det er det sværeste at adoptere, fordi det ændrer, hvor arbejdet foregår. Mange organisationer udvikler sig fra et register, der beviser værdi, mod sameksistens, efterhånden som tilliden vokser, og kører mere end én stil på tværs af forskellige domæner.

### Match, flet og sæt survivorship-regler eksplicit

MDM's hjerte er at afgøre, hvornår to poster beskriver den samme ting i den virkelige verden. Det er [recordlinkage](https://en.wikipedia.org/wiki/Record_linkage), sjældent så enkelt som et eksakt nøglematch, fordi virkelige data er fulde af tastefejl, forkortelser og manglende felter. Deterministisk matching bruger eksakte regler på valgte felter (samme CVR-nummer eller samme e-mail plus postnummer). Probabilistisk matching scorer ligheden på tværs af mange felter med [tilnærmet strengmatching](https://en.wikipedia.org/wiki/Approximate_string_matching) og vægte, så "Bob Smith, 12 Main St" og "Robert Smith, 12 Main Street" kan vurderes som et sandsynligt match over en tærskel. At afgøre, hvilke poster der henviser til samme entitet, kaldes identitetsopløsning, og den driver alt fra kundebilleder til svindeldetektion.

Når poster matcher, skal I afgøre, hvilke værdier der overlever ind i golden recorden. Disse survivorship-regler er forretningslogik, så gør dem eksplicitte: foretræk den nyeste værdi for et telefonnummer, den mest fuldstændige værdi for en adresse, den mest betroede kilde for et juridisk navn. Sæt et tærskelbånd, hvor match flettes automatisk, et lavere bånd, hvor de afvises automatisk, og et midterbånd, hvor et menneske afgør, hvilket er, hvor stewardship bor. Hold hver fletning reversibel og logget, fordi en forkert fletning, der smelter to rigtige kunder sammen, er værre end et overset match.

### Behandl referencedata som versioneret fælles ordforråd

Referencedata er det fælles ordforråd, jeres systemer taler, og ordforråd, der driver, forårsager tavs misalignment: når ét system bruger ISO-landekoden "GB" og et andet "UK", fejler joins, og tal divergerer. Vedligehold hver referenceliste ét styret sted, offentliggør den til hver forbruger, og, afgørende, versionér den. Koder tilføjes, udgår, deles og flettes over tid, og hvis I overskriver listen på stedet, bryder I historiske rapporter, der var korrekte under de gamle koder.

Behandl et referencedatasæt som en API med en kontrakt. Offentliggør det med ikrafttrædelsesdatoer, så en forbruger kan spørge "hvad var de gyldige regionskoder på denne dato", behold udgåede koder frem for at slette dem, og registrér mappingen, når en kode skifter betydning. Foretræk anerkendte eksterne standarder, hvor de findes, såsom ISO-lande- og valutakoder, fordi standarder giver jer interoperabilitet gratis og hænger sammen med åbne-standarder-disciplinen i kapitel 3.8.

### Modellér hierarkier og relationer, ikke blot flade poster

Stamdata er ikke en bunke uafhængige rækker; det er et net af relationer. En kunde tilhører en husstand og en koncernmoder. Et produkt ruller op i en kategori og et brand. Disse hierarkier bærer reel forretningsbetydning: rul salg op efter koncernmoder, og billedet ændrer sig fuldstændigt fra at rulle op efter den enkelte konto. Modellér disse relationer eksplicit, så forbrugere traverserer dem ensartet i stedet for, at hvert team opfinder sin egen opsummering.

Hold øje med tilfældet, hvor én entitet har brug for flere hierarkier på én gang. Et produkt kan rulle op på én måde for økonomi og en anden for varesortiment, og begge er legitime, så understøt flere navngivne hierarkier frem for at tvinge ét sandt træ. Relationer mellem domæner betyder også noget, såsom hvilken leverandør der leverer hvilket produkt.

### Forbind golden records med det semantiske lag og datakvalitet

De golden records, MDM producerer, er de troværdige entiteter, som det semantiske lag fra kapitel 7.7 henviser til, når det definerer målinger: "aktive kunder" betyder kun noget, når "kunde" er entydig. Fodr jeres golden records ind i det semantiske lag, så hver måling tæller de samme deduplikerede, opløste entiteter.

MDM og datakvalitet (kapitel 7.8) er to sider af samme mønt: kvalitetstjek opdager de dubletter, nulls og formatovertrædelser, som MDM så løser, og MDM's matching bringer kvalitetsproblemer frem, tjekkene overså. Kør kontinuerlig kvalitetsovervågning specifikt på jeres stamdata: dubletrater, fordelinger af matchkonfidens, fuldstændighed af nøglefelter og størrelsen af gennemgangskøen, så drift kommer til syne, før forbrugere ser det.

### Udbred golden records gennem hændelser

En golden record, intet nedstrøms system ser, hjælper ingen. Det stærkeste mønster er hændelsesdrevet udbredelse: når en entitet oprettes, flettes eller rettes, udgiver MDM-hubben en ændringshændelse, og abonnerende systemer opdaterer deres lokale kopi. Det bygger på [hændelsesdrevet arkitektur](https://en.wikipedia.org/wiki/Event-driven_architecture) og streamingmønstrene fra kapitel 7.2 og holder dusinvis af systemer konsistente uden skrøbelige natlige batchsynkroniseringer, der efterlader alle en dag forældede.

Udgiv hændelserne med nok kontekst til at være nyttige: entitetsidentifikatoren, hvad der ændrede sig, de nye overlevende værdier og en version, så forbrugere kan ordne opdateringer og opdage dem, de missede. Gør forbrugere idempotente, så genafspilning af en hændelse ikke gør skade, og tilbyd en API til systemer, der ikke kan abonnere. Princippet fra dataarkitektur og lagring (kapitel 3.4) gælder: design til, at golden recorden skal flyde, for en, ingen forbruger, er blot et dyrt regneark.

### Tildel stewardship og styring før værktøj

MDM fejler som et teknologiprojekt og lykkes som et styringsprojekt. Den kritiske rolle er [datasteward](https://en.wikipedia.org/wiki/Data_steward), en person ansvarlig for kvaliteten og reglerne i et bestemt domæne, som løser tvetydige match, justerer survivorship-regler og træffer afgørelse, når to afdelinger er uenige om, hvad "leverandør" betyder. Stewards er som regel forretningsfolk med dyb domæneviden, ikke ingeniører, og de har brug for reel autoritet og afsat tid, fordi deltidsstewardship uden mandat producerer præcis den drift, MDM skulle stoppe.

Pak stewards ind i styringsstrukturerne fra kapitel 7.1: en dataejer ansvarlig for hvert domæne, et råd til at afgøre tværgående tvister og klare politikker for, hvem der må oprette eller flette stamposter. Dokumentér beslutningerne, fordi reglerne for at matche en kunde er institutionel viden, der skal overleve medarbejderudskiftning. Værktøjet tjener styringen; at købe en MDM-platform, før I navngiver jeres stewards, er at købe en motor uden chauffør.

## Afvejninger: fordele og ulemper

| MDM-stil | Fordele | Ulemper |
|---|---|---|
| Register (kun indeks) | Billigt, lavrisiko, kilder urørte | Skrivebeskyttet; kan ikke rette kildedata |
| Konsolidering (centrale kopier) | Rene poster til analyse hurtigt | Kilder forbliver rodede; ingen tilbageskrivning |
| Sameksistens (synkronisér tilbage til kilder) | Kilder forbedres; afbalanceret kontrol | Mere integration; synkroniseringskonflikter at håndtere |
| Centraliseret / transaktionel hub | Stærkeste konsistens og kontrol | Højeste omkostning; ændrer, hvor arbejdet foregår |
| Deterministisk matching | Forudsigelig, forklarlig, revisionsbar | Overser tastefejl, varianter og rodede data |
| Probabilistisk matching | Fanger virkelig variation | Kræver justering; falske fletninger hvis skødesløs |

Den centrale spænding i MDM er kontrol versus forstyrrelse. De stile, der giver jer de reneste, mest konsistente data (sameksistens og centraliserede hubs), er præcis dem, der trænger mest ind på, hvordan kildesystemer og deres ejere arbejder, og den indtrængen er, hvor MDM-programmer går i stå. Den pragmatiske vej er at optjene tillid med en lavrisikostil og først bevæge sig mod stærkere kontrol, hvor business casen er klar. Matchingafvejningen løber parallelt: deterministiske regler er revisionsbare, men skrøbelige, probabilistisk scoring er kraftfuld, men kræver stewardship og tolerance over for den lejlighedsvise forkerte fletning. De fleste modne programmer blander begge.

## Spørgsmål til drøftelse med dit team

1. **Hvilke stamdatadomæner forårsager os faktisk smerte, og har vi rangeret dem efter omkostning i stedet for at tage dem alle på én gang?** Mange MDM-programmer falder sammen under deres egen ambition, når de forsøger at mestre hver entitet i virksomheden på én gang og leverer intet i to år. Det produktive træk er at finde det ene eller de to domæner, hvor duplikering og konflikt koster jer reelle penge eller tillid, som regel kunde eller produkt, og at kvantificere den omkostning: de spildte udsendelser, afstemningstimerne, de forkerte omsætningstal, revisionsfundene. Tag konkrete eksempler på den samme entitet, der optræder på flere måder på tværs af jeres systemer, med, og lad den rangering fortælle jer, hvor I skal begynde, for en snæver, målbar sejr bygger den troværdighed, I har brug for til at udvide.

2. **Hvem ejer hvert stamdatadomæne, og har vores stewards autoriteten og tiden til faktisk at gøre jobbet?** MDM-værktøj uden bemyndiget stewardship er en bil uden chauffør, og den almindeligste fejlform er at navngive en steward på et slide, mens man ikke giver vedkommende noget reelt mandat og ingen afsatte timer. De mennesker, der løser tvetydige match og afgør tvister om "hvad tæller som en kunde", har brug for domæneekspertise, beslutningsautoritet og beskyttet tid. Tag jeres organisationsdiagram med, og spørg for jeres topdomæne præcis, hvem der afgør, hvornår to poster er samme person, og hvem der træffer afgørelse, når salg og økonomi er uenige. Hvis I ikke kan navngive den person og pege på deres afsatte tid, har I fundet det hul, der vil sænke programmet.

3. **Når vi fletter to poster til en golden record, kan vi så forklare og omgøre beslutningen, og hvor kommer de overlevende værdier fra?** Survivorship-regler er forretningslogik, de fleste teams aldrig har skrevet ned, hvilket betyder, at fletninger sker ved et tilfælde af indlæsningsrækkefølge eller værktøjsstandarder, og en forkert fletning, der smelter to rigtige kunder sammen, er smertefuld at rulle tilbage. Tag en reel flettet post med, og spor hvert overlevende felt tilbage til dets kilde og regel: hvorfor denne adresse, hvorfor dette navn, hvorfor dette telefonnummer. Bekræft, at hver fletning er logget og reversibel, og at et midterbånd af usikre match går til et menneske frem for at blive flettet automatisk. Hvis I ikke kan forklare en specifik golden record, kan jeres stewards ikke forsvare den over for en revisor eller en forurettet kunde.

4. **Hvilken MDM-arkitekturstil passer til hvert domæne, vi planlægger at mestre, og kan vi forsvare det valg over for den forstyrrelse, det påfører kildesystemernes ejere?** Den stil, I vælger, afgør, hvor meget I kan rense dataene, og hvor meget I trænger ind på de teams, der ejer kilderne, og at vælge efter mode eller leverandørpitch frem for efter kontrol-versus-forstyrrelse-virkeligheden er, hvordan programmer går i stå halvvejs. Et register beviser værdi billigt, men retter aldrig en kilde; en centraliseret hub giver den stærkeste konsistens, men flytter, hvor poster oprettes, hvilket er en organisatorisk ændring forklædt som en teknisk. Tag for hvert kandidatdomæne en ærlig vurdering af, hvor meget autoritet I faktisk har over kildeejerne, hvor friske nedstrøms kopier skal være, og hvad en tilbageskrivning ville bryde i eksisterende arbejdsgange, med. I virksomheds- og offentlige sammenhænge så tilføj migrerings- og forandringsledelsesomkostningen ved at flytte kildesystemet, fordi de teams, hvis daglige arbejde flytter, vil modsætte sig en hub, de ikke blev hørt om, og en gået i stå sameksistensudrulning er dyrere end et beskedent register, der leverer.

5. **Hvordan justerer vi matchingtærsklerne, og har vi aftalt, hvilken rate af falske fletninger og oversete match vi kan leve med i hvert domæne?** Hver probabilistisk matchingmotor afvejer falske fletninger (at smelte to rigtige entiteter sammen) mod oversete match (at lade én entitet være splittet), og balancen er en forretningsbeslutning, ikke en standard, nogen lod stå i værktøjet. Sæt auto-flet- og auto-afvis-båndene for brede, og I korrumperer golden records tavst; sæt dem for smalle, og den menneskelige gennemgangskø vokser hurtigere, end stewards kan rydde den. Tag den nuværende konfidensfordeling, størrelsen og alderen på gennemgangskøen og eksempelfejl af begge slags med, så rummet kan se den reelle omkostning ved hver retning. I et offentligt identitetsdomæne så hæld hårdt mod oversete match og menneskelig gennemgang, fordi en forkert fletning kan nægte en ydelse eller blotlægge én borgers data for en anden, og anke- og revisionsomkostningen ved den fejl overstiger langt omkostningen ved en dublet, en steward løser i næste uge.

6. **Hvordan får nedstrøms systemer at vide, at en golden record ændrede sig, og hvor forældet kan hvert enkelt være, før en beslutning går galt?** En perfekt opløst golden record, intet system forbruger, er et dyrt regneark, og udbredelsesmekanismen, hvad enten det er ændringshændelser, en abonnements-API eller et natligt batch, sætter stille, hvor aktuel hver afhængig beslutning er. Hændelsesdrevet udbredelse holder dusinvis af forbrugere næsten i realtid, men kræver idempotente forbrugere og versionerede hændelser; en natlig synkronisering er enklere, men efterlader alle en dag forældede, hvilket kan være fint for en marketingliste og farligt for et svindeltjek. Tag listen over forbrugende systemer, den friskhed hvert faktisk har brug for, og hvordan en forbruger, der misser en opdatering i dag, kommer sig, med. For en stor eller offentlig organisation så navngiv, hvem der ejer kontrakten for disse hændelser, og hvordan en abonnent opdager en tabt besked, for en entitetsændring, der tavst ikke når ét agentur, genskaber netop den fragmentering, MDM blev finansieret til at fjerne.

## Sektorperspektiv

**Startup.** Med en håndfuld ingeniører og ingen runway at give af så køb ikke en MDM-platform. Mestr den ene entitet, der korrumperer jeres tal, som regel kunden duplikeret på tværs af selvbetjening og salg, med et matchingjob i det varehus, I allerede kører, og én person, der gennemgår usikre match ugentligt. Hold hver fletning logget og reversibel, så en dårlig regel koster en eftermiddag, ikke en kunderelation, og vend først tilbage til tungere værktøj, når den manuelle gennemgangskø vokser fra en enkelt gennemgåer.

**Lille virksomhed.** I har ingen datasteward og et stramt budget, så behandl det som en køb-ikke-byg-beslutning, og støt jer til standarder, I får gratis. Foretræk værktøjer, der allerede deduplikerer kontakter og taler ISO-lande- og valutakoder, frem for en skræddersyet hub, I ikke kan vedligeholde, og vælg det ene domæne, typisk kunder eller produkter, hvor dubletter koster jer rigtige penge. Tildel ansvaret til en navngiven ejer, selv hvis det er en brøkdel af én persons uge, fordi ordforråd, der driver uden at nogen holder øje, er det, der stille ødelægger jeres rapporter.

**Stor virksomhed.** På tværs af et dusin ERP- og CRM-systemer ophobet gennem opkøb er arbejdet porteføljestyring: rangér domæner efter omkostningen ved deres duplikering, rejs bemyndigede stewards i forretningen, og standardisér survivorship-regler og referencedataversionering, så grupper holder op med at genløse det samme matchingproblem. Budgettér integrations- og permanent stewardshipomkostning eksplicit, udbred golden records som versionerede hændelser, så kilder forbedres over tid, og styr MDM som et målt program med dubletrater og gennemgangskømålinger frem for en engangsoprydning.

**Offentlig sektor.** Indkøbsregler, streng datadelingslovgivning og offentlig ansvarlighed former hvert valg. Nøgl personentiteten på en styret national identifikator, versionér referencedata efter ikrafttrædelsesdato, så historiske poster forbliver korrekte, og gør identitetsopløsning bevidst konservativ: usikre match går til uddannede stewards, aldrig automatiserede fletninger, fordi en forkert fletning kan nægte en ydelse eller lække én borgers data til en anden. Log hvert match til revision og anke, kræv dataportabilitet og oplyst matchinglogik fra leverandører, og hold hele kapabiliteten inden for de interoperabilitetsstandarder, den offentlige sektor allerede har forpligtet sig til.

## Eksempler

**Startup.** Et hurtigt voksende softwarefirma sælger gennem både selvbetjent tilmelding og et salgsteam, og de to kanaler opretter den samme kunde to gange under let forskellige firmanavne. Omsætning pr. konto ser forkert ud, og salgsteamet bliver ved med at koldringe til eksisterende brugere. I stedet for at købe en tung platform begynder de med et let register: et matchingjob i deres datavarehus, der linker poster efter e-maildomæne og normaliseret firmanavn, med én deltidssteward, der gennemgår de usikre match ugentligt. Det koster lidt, retter rapporteringsfejlen og beviser den værdi, der retfærdiggør mere investering, efterhånden som de vokser.

**Stor virksomhed.** En global producent er vokset gennem opkøb og kører et dusin ERP- og CRM-systemer, hver med sine egne leverandørposter, så den samme leverandør optræder femten måder, og virksomheden ikke kan forhandle som én køber eller se sit sande forbrug. Den rejser en MDM-hub i sameksistensstil til leverandør- og produktdomænerne med deterministisk matching på skatte- og registreringsidentifikatorer plus probabilistisk scoring på navne og adresser. Navngivne stewards i indkøb justerer survivorship-reglerne og arbejder gennemgangskøen, og golden records udgives som ændringshændelser, der flyder tilbage i hvert ERP, så rensede data forbedrer kilderne. Konsolideret forbrugssynlighed låser op for bedre kontraktvilkår, og den afstemningsskat, der åd økonomi hvert kvartal, falder kraftigt.

**Offentlig sektor.** En national regering vil have agenturer til at behandle en borger som én person frem for en fremmed ved hver skranke, mens den respekterer strenge juridiske grænser for datadeling. Den bygger en centraliseret stamdatahub til personentiteten, nøglet på en styret national identifikator, med referencedata versioneret efter ikrafttrædelsesdato, så historiske poster forbliver korrekte. Identitetsopløsning er bevidst konservativ: usikre match går til uddannede stewards frem for automatiserede fletninger, fordi en forkert fletning kunne nægte nogen en ydelse eller blotlægge deres data, og hvert match logges til revision og anke. Udbyttet er færre duplikerede poster, mindre svindel fra splittede identiteter og en borger, der ikke skal bevise, hvem vedkommende er ved hver dør, inden for interoperabilitetsstandarderne i kapitel 3.8.

## Business case: motivation, ROI og TCO

Afkastet af MDM kommer af at fjerne en skat, de fleste organisationer betaler uden at navngive den. Duplikerede og modstridende poster koster penge på åbenlyse måder (spildt marketing til den samme person fem gange, forsendelsesfejl fra forældede adresser, mistede mængderabatter) og på mindre åbenlyse måder (analytikere der afstemmer tal, ledere der beslutter på tal, der stille er forkerte, revisorer der fakturerer timer for at nøste ud, hvilken post der er den rigtige). Et konsolideret leverandørbillede betaler ofte for hele programmet alene gennem bedre kontraktvilkår.

Den samlede ejeromkostning har tre dele: platformen eller byggeriet, integrationen til kilder og forbrugere og, størst over tid, det løbende stewardship. Integrationsomkostningen er let at undervurdere, fordi det at forbinde et dusin aldrende kildesystemer er, hvor MDM-programmer bløder tidsplan og budget, og stewardshipomkostningen er let at glemme, fordi den er en permanent driftsudgift, ikke et engangsbyggeri. For at fremlægge sagen for ledelsen så bind MDM til tal, de allerede følger: omsætningsnøjagtighed, marketingeffektivitet, indkøbsbesparelser, revisionsomkostning og regulatorisk risiko, og begynd så snævert og lad en målt sejr på ét højsmerte-domæne finansiere udvidelsen.

## Anti-mønstre og faldgruber

- **Koge-havet-omfang:** at mestre hvert domæne på én gang, levere intet i årevis og miste sponsorat før den første sejr.
- **Værktøj før styring:** at købe en MDM-platform, før stewards og ejere er navngivet, så motoren ingen chauffør har.
- **Deltidsstewards uden autoritet:** at tildele stewardship på et slide uden at give noget reelt mandat eller beskyttet tid.
- **Tavs survivorship:** at flette poster efter værktøjsstandard eller indlæsningsrækkefølge, uden skrevne regler og uden mulighed for at forklare en golden record.
- **Irreversible fletninger:** at flette usikre match automatisk uden fortryd, så en forkert sammensmeltning af to rigtige entiteter bliver permanent skade.
- **Referencedata overskrevet på stedet:** at redigere kodelister uden versionering og bryde hver historisk rapport, der var korrekt under de gamle koder.
- **Golden records ingen forbruger:** at bygge en pletfri hub, intet nedstrøms system abonnerer på, så de rene data aldrig når beslutninger.
- **Genopfindelse af standardkoder:** at præge jeres egne lande- eller valutalister, når ISO-standarder findes, og miste interoperabilitet uden grund.

## Modenhedsmodel

- **Niveau 1, Opstart:** Stam- og referencedata er ustyrede. Den samme entitet findes mange gange uden autoritativ version, kodelister divergerer, matching er manuel og reaktiv, og ingen ejer problemet, så tal for kerneentiteter er uenige, og ingen kan sige, hvilket der er rigtigt.
- **Niveau 2, Udvikling:** Nøgledomæner er anerkendt, og nogen deduplikerer dem, ofte i varehuset til rapportering. Basal deterministisk matching findes, referencelister samles, og nogle få personer fungerer som uformelle stewards, men praksis varierer fra team til team, kilderne forbliver rodede, og regler bor i folks hoveder frem for på papir.
- **Niveau 3, Standardisering:** MDM er et styret program anvendt ensartet på tværs af organisationen. Stamdomæner har navngivne ejere og bemyndigede stewards, matching- og survivorship-regler er dokumenteret og håndhævet, golden records produceres og udbredes til forbrugere, og referencedata versioneres og offentliggøres med ikrafttrædelsesdatoer som en API.
- **Niveau 4, Styring:** Programmet måles og styres mod baselines. Dubletrater, matchkonfidensfordelinger, rater for falske fletninger og oversete match, nøglefeltfuldstændighed samt gennemgangskøens størrelse og alder følges som målinger; tærskler justeres mod de tal frem for på fornemmelse; og MDM-værdi (omsætningsnøjagtighed, indkøbsbesparelser, gennemgangsomkostning) kvantificeres og rapporteres til ejere efter en fast kadence.
- **Niveau 5, Orkestrering:** Golden records flyder som versionerede hændelser næsten i realtid, fodrer det semantiske lag og er betroede på tværs af organisationen. Matching forbedres løbende mod målte udfald, mestring udvides til nye domæner som en gentagelig kapabilitet, og MDM er integreret med styring og risikoplanlægning, så programmet tilpasser sig, efterhånden som kilder, standarder og entitetslandskabet skifter.

## Idéer til drøftelse

1. Hvis to af jeres systemer er uenige om, hvor mange kunder I har, hvilket er så rigtigt, og hvordan ville I bevise det?
2. Hvilket stamdatadomæne ville levere den største målbare sejr, hvis I mestrede det først, og hvad er den sejr værd?
3. Hvor ville probabilistisk matching hjælpe jer i dag, og er I trygge ved den lejlighedsvise forkerte fletning, den indebærer?
4. Hvordan versionerer I jeres referencedata, og hvad går i stykker i jeres historiske rapporter, når en kode skifter betydning?
5. Hvem er den navngivne steward for jeres vigtigste entitet, og har vedkommende autoriteten og tiden til faktisk at gøre jobbet?
6. Når en golden record ændres, hvordan finder jeres nedstrøms systemer ud af det, og hvor forældede kan de være, før det gør ondt?

## Vigtigste pointer

- Sortér jeres data i stam-, reference- og transaktionsdata; invester matching og styring, hvor duplikering koster mest.
- Producér én golden record pr. entitet i den virkelige verden, samlet af eksplicitte, reversible, loggede survivorship-regler.
- Vælg en MDM-arkitekturstil (register, konsolidering, sameksistens eller centraliseret hub), der passer til jeres appetit for kontrol og forstyrrelse.
- Behandl referencedata som versioneret fælles ordforråd, foretræk anerkendte standarder, og overskriv aldrig kodelister på stedet.
- MDM lykkes på styring og stewardship, ikke værktøj; udbred golden records som hændelser, og mål programmet på forbedrede beslutninger.

## Referencer og videre læsning

- David Loshin, *Master Data Management*
- Alex Berson and Larry Dubov, *Master Data Management and Data Governance*
- Dan Power, *The Definitive Guide to Master Data Management*
- John Talburt, *Entity Resolution and Information Quality*
- Peter Christen, *Data Matching: Concepts and Techniques for Record Linkage, Entity Resolution, and Duplicate Detection*
- Ivan P. Fellegi and Alan B. Sunter, "A Theory for Record Linkage," *Journal of the American Statistical Association*
- DAMA International, *DAMA-DMBOK: Data Management Body of Knowledge*
- Ralph Kimball and Margy Ross, *The Data Warehouse Toolkit*
