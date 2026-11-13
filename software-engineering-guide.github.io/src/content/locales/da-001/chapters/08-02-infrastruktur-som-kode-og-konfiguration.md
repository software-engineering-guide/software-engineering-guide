# 8.2 Infrastruktur som kode og konfiguration

## Overblik og motivation

[Infrastruktur som kode](https://en.wikipedia.org/wiki/Infrastructure_as_code) (IaC) betyder at definere og provisionere infrastruktur (netværk, servere, databaser, load balancere, tilladelser) gennem maskinlæsbare definitionsfiler frem for manuelle konsolklik eller ad hoc scripts. [Konfigurationsstyring](https://en.wikipedia.org/wiki/Configuration_management) udvider den samme idé til systemers indstillinger og tilstand, når de først eksisterer. Sammen forvandler de infrastruktur fra et håndlavet, skrøbeligt artefakt til et versioneret, gennemgåeligt, reproducerbart produkt af den samme ingeniørdisciplin, I bruger til applikationskode.

For store teams er IaC ikke en bekvemmelighed, men en nødvendighed. Når hundredvis af ingeniører har brug for miljøer, og tusinder af ressourcer skal forblive ensartede på tværs af regioner og konti, kan manuel provisionering ikke følge med og kan ikke forblive korrekt. Menneskekonfigureret infrastruktur driver før eller siden ind i unikke "snefnug"-servere, ingen fuldt ud forstår, og som ikke pålideligt kan genopbygges efter en fejl. At kodificere infrastruktur gør den ensartet, revisionsbar og bortskaffelig. Ethvert miljø kan genskabes fra sin definition, og enhver ændring er en gennemgåelig diff.

Virksomheds- og offentlige organisationer får en yderligere, afgørende fordel: håndhævbar styring. Sikkerheds- og compliancekrav, såsom kryptering i hvile, netværkssegmentering, godkendte regioner og tagging til omkostningsallokering, kan indlejres direkte i koden og tjekkes automatisk, før noget provisioneres. I stedet for at revidere infrastruktur bagefter og jagte overtrædelser forhindrer I, at ikke-kompatibel infrastruktur overhovedet kommer til at eksistere. Dette skifte fra detektion til forebyggelse er hovedårsagen til, at IaC er blevet grundlæggende for moderne platformspraksis.

## Grundprincipper

- Foretræk deklarative definitioner, der beskriver ønsket tilstand, frem for imperative scripts, der beskriver trin.
- Gem alle infrastrukturdefinitioner i versionsstyring, gennemgået som enhver anden kode.
- Behandl infrastruktur som uforanderlig: erstat frem for at ændre på stedet.
- Gør provisionering idempotent, så anvendelse af den samme definition gentagne gange giver samme resultat.
- Opdag og afstem drift, når det levende miljø afviger fra sin deklarerede definition, kontinuerligt; koden, ikke det levende system, er sandhedskilden.
- Sammensæt infrastruktur af genbrugelige, versionerede moduler frem for at kopiere og indsætte.
- Kod politik som kode, organisatoriske regler udtrykt som maskintjekbar kode, så rækværk er automatisk, ikke vejledende.
- Hold hemmeligheder ude af definitioner; henvis til dem fra en dedikeret hemmelighedsstyring.

## Anbefalinger

### Vælg deklarativt værktøj, og strukturér det omkring moduler

Adoptér et deklarativt IaC-værktøj, såsom [Terraform](https://en.wikipedia.org/wiki/Terraform_(software)), Pulumi eller en cloud-nativ mulighed som CloudFormation, og standardisér på det i hele organisationen, så I undgår et fragmenteret værktøjslandskab. Den centrale arkitekturpraksis er modularitet: byg små, veldokumenterede, versionerede moduler, der indfanger almindelige mønstre (et kompatibelt netværk, en hærdet database, en standardtjeneste). Teams sammensætter så miljøer af disse moduler frem for at forfatte rå ressourcer. Det spreder gode standarder og sikkerhedsindstillinger automatisk og reducerer dramatisk duplikering.

### Styr tilstand bevidst

Deklarative værktøjer sporer mappingen mellem kode og reelle ressourcer i en tilstandsfil. Gem tilstand eksternt i en delt, krypteret, adgangskontrolleret backend, og brug låsning, så samtidige ændringer ikke kan korrumpere den. Hold aldrig tilstand på en bærbar, og redigér den aldrig i hånden, undtagen som en sidste udvej til genopretning. Tilstand er følsom, fordi den kan indeholde ressourcemetadata og hemmeligheder, så beskyt den derefter.

### Byg uforanderlig infrastruktur med golden images

I stedet for at patche kørende servere så bag et versioneret "golden image" (et forkonfigureret, hærdet maskine- eller containerimage), og udrul friske instanser fra det. Når I har brug for en ændring eller patch, så byg et nyt image og rul det ud, mens de gamle instanser pensioneres. Det eliminerer konfigurationsdrift, gør tilbagerulning triviel og holder hver instans identisk og sporbar til et kendt godt build. Automatiserede imagepipelines bør inkludere sikkerhedshærdning og scanning, så compliance er indbygget på imageniveau.

### Opdag og afstem konfigurationsdrift

Drift opstår, når det levende miljø afviger fra sin definition, som regel fordi nogen foretog en manuel nødændring. Kør regelmæssig driftsdetektion, der sammenligner faktisk tilstand med deklareret tilstand og flagger forskellene. Behandl drift som en fejl: afstem ved at opdatere koden og anvende den igen, ikke ved at lade den manuelle ændring stå. For systemer, der har brug for løbende konfigurationshåndhævelse, brug et konfigurationsstyringsværktøj, der kontinuerligt konvergerer værter mod deres deklarerede tilstand.

### Adoptér GitOps og pull-baseret udrulning

I GitOps-modellen rummer et Git-repository systemets deklarerede ønskede tilstand, og en automatiseret agent, der kører inde i målmiljøet, trækker kontinuerligt den tilstand og afstemmer det levende system, så det matcher. Det vender den traditionelle push-model på hovedet. Intet eksternt system behøver stående legitimationsoplysninger for at ændre miljøet, fordi miljøet trækker sin egen konfiguration. GitOps giver et komplet revisionsspor (hver ændring er en commit), nem tilbagerulning (fortryd commitet) og stærk driftskorrektion (agenten genhævder kontinuerligt den ønskede tilstand). Det er især kraftfuldt til [Kubernetes](https://en.wikipedia.org/wiki/Kubernetes) og for organisationer, der vil have en enkelt, gennemgåelig sandhedskilde.

### Håndhæv rækværk med politik som kode

Udtryk organisatoriske regler, såsom tilladte regioner, obligatorisk kryptering, påkrævede tags og forbudt offentlig eksponering, som maskintjekbare politikker med et værktøj som Open Policy Agent (OPA) eller en platformsnativ politikmotor som Sentinel. Kør disse tjek i pipelinen før provisionering, så overtrædelser blokeres automatisk. Politik som kode forvandler et sikkerhedsteams hensigt til en eksekverbar, ensartet anvendt kontrol, og den skalerer til tusinder af ændringer på en måde, manuel gennemgang aldrig kunne.

## Afvejninger: fordele og ulemper

| Valg | Fordele | Ulemper | Bedst egnet |
|---|---|---|---|
| Deklarativ IaC (Terraform/Pulumi) | Reproducerbar, gennemgåelig, drift kan opdages | Indlæringskurve; kompleks tilstandsstyring | Næsten alle teams i skala |
| Imperative scripts | Velkendte; fleksible til engangsopgaver | Ikke idempotente; svære at revidere og gentage | Snævre, overgangsmæssige tilfælde |
| Uforanderlig + golden images | Ingen drift; triviel tilbagerulning | Overhead i imagebuildpipeline | Flåder, der har brug for ensartethed |
| Foranderlig konfigurationsstyring | Finkornet løbende kontrol | Driftsrisiko; langsommere konvergens | Ældre eller langlivede værter |
| GitOps (pull-baseret) | Stærkt revisionsspor; selvhelende | Kræver agent i klyngen og Git-disciplin | Kubernetes og cloud-native |
| Politik som kode | Automatisk, ensartet rækværk | Indsats med at forfatte politik på forhånd | Regulerede miljøer |

Hovedspændingen er mellem fleksibilitet og kontrol. Manuelle og imperative tilgange føles hurtigere for en enkelt ændring, men de ophober skjult inkonsistens, der bliver lammende i skala. Deklarativ, uforanderlig, politikstyret infrastruktur kræver mere investering på forhånd og et reelt kulturelt skifte, da ingeniører skal holde op med at foretage hurtige konsolændringer, men den tjener den investering ind mange gange i pålidelighed, revisionsbarhed og evnen til at genopbygge hvad som helst efter behov.

## Spørgsmål til drøftelse med dit team

1. **Hvem ejer det fælles modulbibliotek, og hvordan når en forbedring af et modul hvert team, der bruger det?** Moduler betaler sig kun, hvis rettelser og hærdede standarder udbredes, og det kræver klart ejerskab og reel versionering, ikke en mappe, alle kopierer fra. Afgør, hvem der vedligeholder modulerne for kompatibelt netværk og hærdet database, hvordan I versionerer dem (semantisk versionering med en changelog), og hvordan teams trækker opgraderinger uden en brandøvelse. I skala er det forskellen mellem at rette en fejlkonfiguration én gang og at jagte den på tværs af tusind håndredigerede ressourcer. Tag dokumentation med: hvor mange forskellige kopier af det samme mønster findes i dag, hvor lang tid en sikkerhedsrettelse tager at nå hvert miljø, og om teams fastlåser modulversioner eller lader dem flyde. Hvis en kritisk patch ikke kan nå hele ejendommen på få dage, er jeres modularitet kosmetisk.

2. **Hvad er jeres kadence for driftsdetektion, og hvad sker der egentlig, når drift findes?** Drift er det levende miljø, der stille afviger fra sin deklarerede tilstand, som regel fra en nødændring i konsollen, og at tolerere den forvandler jeres kode til fiktion. Afgør, hvor ofte I sammenligner faktisk tilstand med deklareret tilstand (natligt er en rimelig standard) og, vigtigere, afgør responsen: afstem ved at opdatere koden og anvende den igen, aldrig ved at lade den manuelle ændring stå. I regulerede sammenhænge er det et kontrolkrav, fordi revisorer har brug for, at den deklarerede tilstand kontinuerligt matcher virkeligheden. Tag jeres nuværende tal med: hvor mange ressourcer driver hver uge, hvor længe de forbliver drevet, og om nogen er ansvarlig for at lukke dem. Behandl hver drift som en fejl med en ejer, ellers eroderer sandhedskildegarantien, til ingen længere stoler på koden.

3. **Er I gået over til GitOps og pull-baseret afstemning, eller har et eksternt system stadig stående legitimationsoplysninger til at ændre produktion?** I pull-modellen afstemmer en agent inde i målmiljøet kontinuerligt det levende system til Git, hvilket fjerner behovet for, at noget udefrakommende system har skriveadgang, og den genhævder ønsket tilstand, så drift selvkorrigerer. Det er en stærk sikkerheds- og revisionsholdning, da hver ændring er en commit, og ingen operatør behøver stående produktionslegitimationsoplysninger. Omkostningen er reel: en agent i klyngen at drive og streng Git-disciplin, så vej det mod jeres nuværende push-baserede automatisering. Tag listen over, hvem og hvad der i dag direkte kan mutere produktion, og hvilket revisionsspor de ændringer efterlader, med. For Kubernetes og højsikkerhedsenklaver er dette skifte som regel det værd; for en håndfuld statiske ressourcer kan det være overkill.

4. **Hvordan er jeres infrastrukturtilstand gemt, låst og adgangskontrolleret, og hvad sker der den dag, den korrumperes eller går tabt?** Tilstand er kortet mellem jeres kode og de reelle ressourcer, så en tabt eller beskadiget tilstandsfil kan efterlade et værktøj blindt over for ressourcer, det oprettede, og friste nogen til en destruktiv gen-anvendelse. For et stort team multipliceres risikoen, fordi mange ingeniører, der anvender mod delt tilstand, har brug for en ekstern, krypteret, låst backend, så samtidige kørsler ikke kan overskrive hinanden. Vej bekvemmeligheden ved én stor tilstand mod den sprængradius, den skaber, og overvej at dele tilstand pr. miljø eller pr. domæne, så en enkelt fejl ikke kan tage alt ned. Tag fakta med: hvor tilstand bor i dag, om låsning håndhæves, hvem der kan læse den (den kan indeholde hemmeligheder), og om I nogensinde har øvet en genopretning. I virksomheds- og offentlige sammenhænge så behandl tilstandsbackenden som et følsomt, adgangskontrolleret aktiv med sin egen backup, revisionslog og genopretnings-runbook, fordi at miste den er at miste jeres fortegnelse over, hvad der eksisterer.

5. **Når en reel nødsituation kræver en manuel ændring, hvad er den sanktionerede break-glass-vej, og hvordan bliver den ændring foldet tilbage i koden?** Hver moden IaC-praksis møder før eller siden hændelsen klokken tre om natten, hvor det ikke er acceptabelt at vente på en pipeline, og det ærlige spørgsmål er ikke, om manuelle ændringer nogensinde sker, men hvordan I afgrænser dem. Afgør på forhånd, hvem der må omgå pipelinen, hvad de må røre, hvordan handlingen logges, og fristen for, hvornår ændringen skal afstemmes ind i koden eller fortrydes. Uden den aftale bliver nødundtagelsen stille til dagligdags vane, og ClickOps vender tilbage gennem bagdøren. Tag dokumentation med: hvor mange ændringer uden for båndet skete sidste kvartal, hvor længe hver forblev uafstemt, og om driftsdetektion faktisk fangede dem. For regulerede og offentlige organer er en dokumenteret break-glass-procedure med automatisk logning ofte et kontrolkrav, fordi revisorer forventer både, at nødsituationer er mulige, og at hver efterlader et spor og returnerer systemet til dets deklarerede tilstand.

6. **Hvor meget af jeres sikkerheds- og compliancebaseline er udtrykt som politik, der automatisk blokerer en dårlig ændring, versus regler, der bor i et dokument og afhænger af, at nogen husker dem?** Rækværk skrevet som prosa i en wiki overtrædes rutinemæssigt, fordi de afhænger af, at hver ingeniør læser og anvender dem under deadlinepres, mens de samme regler udtrykt som politik som kode afviser en ikke-kompatibel ændring, før den nogensinde provisioneres. For en stor organisation er det den eneste måde, et sikkerhedsteams hensigt skalerer til tusinder af ændringer uden at blive en gennemgangsflaskehals. Vej omkostningen ved at forfatte og vedligeholde politikker på forhånd mod den tilbagevendende omkostning ved manuel gennemgang og afhjælpning bagefter, og afgør, hvilke kontroller (kryptering, godkendte regioner, obligatoriske tags, ingen offentlig eksponering) der er så ufravigelige, at de håndhæves som hårde porte. Tag listen over jeres nuværende baselineregler med, og markér hvilke der er automatiserede versus vejledende, plus hvor ofte hver overtrædes i praksis. I virksomheds- og offentlige sammenhænge forvandler automatiseret politik en revision fra ugers manuel dokumentationsindsamling til en forespørgsel mod håndhævede kontroller, og den gør compliance til forebyggelse frem for detektion.

## Sektorperspektiv

**Startup.** Hastighed vinder, så læg hele jeres stak i ét deklarativt repository (Terraform er en almindelig standard), hold tilstand i en administreret krypteret backend, og rut hver ændring gennem en pull request, selv med et team på tre. Spring det tunge platformsapparat over: intet centralt modulteam, ingen politikmotor endnu, blot versionsstyring og disciplinen aldrig at klikke i konsollen. Det alene giver jer reproducerbare miljøer, I kan rive ned for at spare penge og genopbygge til næste demo.

**Lille virksomhed.** Uden en dedikeret platformsspecialist så støt jer til administrerede tjenester og den IaC, jeres cloududbyder eller leverandør allerede understøtter, frem for at rejse skræddersyet værktøj, I ikke kan vedligeholde. Foretræk at købe en hostet platform, hvis fornuftige standarder (kryptering, backups, patching) håndteres for jer, frem for at bygge en golden-image-pipeline, I ikke har nogen til at køre. Ram målet snævert ind: få jeres håndfuld kritiske ressourcer ind i kode, så I kan genopbygge dem efter en fejl eller en afgående konsulent.

**Stor virksomhed.** Kerneproblemet er ensartethed på tværs af mange teams, konti og regioner, så invester i et versioneret fælles modulbibliotek, ekstern låst tilstand og politik som kode håndhævet i pipelinen. Et centralt platformsteam udgiver hærdede moduler og rækværk, mens produktteams selvbetjener sig inden for dem, og driftsdetektion kører kontinuerligt, så tusinder af ressourcer forbliver i en kendt tilstand. Budgettér den løbende omkostning ved at vedligeholde moduler og politikker, fordi deres værdi kommer af, at en rettelse eller en hærdet standard udbredes overalt på én gang.

**Offentlig sektor.** Indkøbsregler, akkreditering og offentlig ansvarlighed skubber jer mod uforanderlig infrastruktur, signerede commits og GitOps-afstemning inde i en akkrediteret enklave, så ingen operatør har stående legitimationsoplysninger til at ændre produktion. Kod den påkrævede sikkerhedsbaseline ind i golden images og politik som kode, og lad commit-historikken tjene som manipulationssikker, kontinuerligt tilgængelig revisionsdokumentation. Foretræk åbent, portabelt værktøj frem for proprietære formater, der fælder jer, og gør break-glass-proceduren og dens logning eksplicit, så nødændringer stadig opfylder krav om konfigurationskontrol.

## Eksempler

**Startup.** Et startup på fem personer definerer hele sit AWS-setup, altså VPC, database og containertjeneste, i ét enkelt Terraform-repository med tilstand holdt i en krypteret S3-backend og låsning gennem DynamoDB. Hver ændring går gennem en pull request, så selv en solo vagthavende ingeniør kan se præcis, hvad der vil ændre sig, før apply køres. Når de har brug for et frisk stagingmiljø til en stor demo, kopierer de et lille modul og rejser det på minutter, og river det ned lige så hurtigt for at holde cloudregningen lav.

**Stor virksomhed.** En multinational detailhandler styrer infrastruktur på tværs af flere cloudkonti og regioner. Et centralt platformsteam udgiver versionerede Terraform-moduler til kompatible netværk, databaser og tjenestestilladser og håndhæver OPA-politikker, der afviser enhver ressource uden kryptering eller omkostningsallokeringstags. Produktteams provisionerer deres egne miljøer selvbetjent, men hver ændring flyder gennem pipelinen, hvor politik tjekkes automatisk. Driftsdetektion kører natligt og åbner tickets for enhver manuel ændring og holder tusinder af ressourcer kontinuerligt i en kendt, kompatibel tilstand.

**Offentlig sektor.** Et forsvarsagentur, der opererer i et højsikkerhedsmiljø, bygger hærdede golden images, der indlejrer den påkrævede sikkerhedsbaseline, og udruller kun uforanderlige instanser fra de images. Al infrastruktur er deklareret i Git og afstemt af en GitOps-agent inde i den akkrediterede enklave, så ingen operatør har stående legitimationsoplysninger til direkte at ændre produktion. Hver ændring er en signeret commit. Det giver revisorer en komplet, manipulationssikker historik og opfylder krav om kontinuerlig overvågning og konfigurationskontrol uden manuel dokumentationsindsamling.

## Business case: motivation, ROI og TCO

ROI af IaC kommer af hastighed, pålidelighed og risikoreduktion. Miljøer, der engang tog uger af ticketdrevet manuel provisionering, kan oprettes på minutter, hvilket frigør ingeniører og fremskynder projekter. Reproducerbarhed skærer genoprettelsestiden efter fejl drastisk, fordi ethvert miljø kan genopbygges fra kode. Automatiseret politikhåndhævelse reducerer hyppigheden og omkostningen af sikkerhedshændelser og revisionsfund, hvilket for regulerede organisationer kan være betydeligt.

På TCO-regnskabet omfatter adoptionsomkostninger værktøj, træning, opbygning af et modul- og politikbibliotek og disciplinen til at holde op med at foretage manuelle ændringer. Omkostningen ved ikke at adoptere er stejlere og akkumulerer over tid: snefnugsinfrastruktur, ingen kan genopbygge, langsom og fejlbehæftet provisionering, sikkerhedsfejlkonfigurationer, der fører til brud, og revisioner, der æder ugers manuel indsats. Over for ledelsen så ram IaC ind som at konvertere infrastruktur fra et uforvaltet ansvar til et styret, reproducerbart aktiv og som mekanismen, der gør sikkerhed og compliance automatisk frem for ambitiøs.

## Anti-mønstre og faldgruber

- **ClickOps i produktion.** At foretage ændringer i hånden i konsollen garanterer drift og ødelægger reproducerbarhed.
- **Hemmeligheder i kode.** At hardkode legitimationsoplysninger i definitionsfiler lækker dem ind i versionshistorik og tilstand.
- **Monolitiske, ikke-modulariserede definitioner.** Én enorm konfiguration, ingen tør ændre, bliver lige så skrøbelig som den manuelle opsætning, den erstattede.
- **Uforvaltet tilstand.** Lokale eller ulåste tilstandsfiler fører til korruption og tabt infrastruktur.
- **Tolereret drift.** At lade manuelle ændringer stå eroderer sandhedskildegarantien, til koden er fiktion.
- **Politik som dokumentation.** Regler, der bor i en wiki i stedet for et automatiseret tjek, overtrædes rutinemæssigt.
- **Kopier-og-indsæt-udbredelse.** At duplikere konfiguration på tværs af teams betyder, at rettelser og forbedringer aldrig spreder sig.

## Modenhedsmodel

**Niveau 1: Opstart.** Infrastruktur provisioneres manuelt gennem konsollen og ad hoc scripts. Miljøer er inkonsistente, udokumenterede og kan ikke pålideligt reproduceres, og genopretning efter en fejl er langsom og usikker.

**Niveau 2: Udvikling.** Noget infrastruktur er kodificeret, men praksis varierer fra team til team. Tilstandsstyring er inkonsistent, drift er almindelig, hemmeligheder lækker nogle gange ind i definitioner, og politik håndhæves, hvis overhovedet, gennem manuel gennemgang.

**Niveau 3: Standardisering.** Deklarativ IaC er den dokumenterede standard i hele organisationen, bygget af fælles versionerede moduler med styret, ekstern, låst tilstand. Politik som kode håndhæver rækværk i pipelinen, hemmeligheder refereres fra en dedikeret styring, og driftsdetektion kører efter en regelmæssig kadence.

**Niveau 4: Styring.** Praksissen måles mod baselines. I følger driftsrate og gennemsnitlig tid til at afstemme, adoption af modulversioner på tværs af teams, politikovertrædelser blokeret versus undsluppet, provisioneringsledetid og andelen af ressourcer, der faktisk er under kode. Disse målinger lukker ændringer og styrer, hvor I investerer, så beslutninger hviler på dokumentation frem for anekdote.

**Niveau 5: Orkestrering.** Infrastruktur er uforanderlig og GitOps-drevet, selvhelende mod drift, med complianceevidens produceret automatisk. Modul- og politikbiblioteket forbedres løbende ud fra reel brug og hændelser, og infrastrukturpraksis er integreret med sikkerheds-, omkostnings- og leveringsplanlægning, så hele ejendommen tilpasser sig, når krav skifter.

## Idéer til drøftelse

- Hvor bør linjen ligge mellem centralt styrede moduler og teamautonomi til at definere tilpasset infrastruktur?
- Hvordan håndterer I den reelle nødændring, der skal omgå pipelinen, uden at normalisere ClickOps?
- Hvad er den rette strategi til at styre og sikre tilstand på tværs af mange konti og teams?
- Hvornår er foranderlig konfigurationsstyring stadig berettiget versus fuldt uforanderlig infrastruktur?
- Hvordan holder I politik-som-kode-biblioteket på linje med udviklende sikkerheds- og regulatoriske krav?
- Hvordan ser en realistisk migreringsvej ud for ældre infrastruktur, der er ældre end IaC?

## Vigtigste pointer

- Definér infrastruktur deklarativt, versionér den, og behandl den som gennemgåelig, reproducerbar kode.
- Byg af små, versionerede moduler for at sprede gode standarder og eliminere duplikering.
- Foretræk uforanderlig infrastruktur og golden images for at afskaffe drift og forenkle tilbagerulning.
- Styr tilstand bevidst, og hold hemmeligheder ude af definitioner.
- Adoptér GitOps for et stærkt revisionsspor og selvhelende afstemning.
- Håndhæv rækværk med politik som kode, så compliance forebygges ind i eksistens, ikke revideres bagefter.

## Referencer og videre læsning

- Kief Morris, *Infrastructure as Code: Dynamic Systems for the Cloud Age*.
- Yevgeniy Brikman, *Terraform: Up & Running*.
- Betsy Beyer, Chris Jones, Jennifer Petoff, and Niall Richard Murphy (eds.), *Site Reliability Engineering*.
- Gene Kim, Jez Humble, Patrick Debois, and John Willis, *The DevOps Handbook*.
- Weaveworks, "GitOps" foundational writings (Alexis Richardson et al.).
- Open Policy Agent documentation and the Rego policy language.
- NIST Special Publication 800-53, security and privacy controls (configuration management family).
