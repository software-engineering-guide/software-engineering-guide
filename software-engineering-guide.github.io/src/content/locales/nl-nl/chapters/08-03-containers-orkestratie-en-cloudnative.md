# 8.3 Containers, orkestratie en cloud-native

## Overzicht en motivatie

Een [container](https://en.wikipedia.org/wiki/OS-level_virtualization) verpakt een applicatie samen met haar afhankelijkheden in één enkele, draagbare, geïsoleerde eenheid. Ze draait op dezelfde manier op een laptop, in een testomgeving en in productie. Orkestratieplatformen, het meest prominent [Kubernetes](https://en.wikipedia.org/wiki/Kubernetes), plannen en beheren grote aantallen containers over vloten machines. Ze handelen plaatsing, schaling, gezondheid, netwerken en herstel af. [Cloud-native](https://en.wikipedia.org/wiki/Cloud-native_computing) is de bredere architectuurstijl gebouwd op deze fundamenten: applicaties ontworpen als losjes gekoppelde, onafhankelijk deploybare, horizontaal schaalbare services die een dynamische, zelfherstellende infrastructuur aannemen.

Voor grote teams lossen containers en orkestratie één moeilijk probleem op. Je moet veel services, gebouwd door veel teams, betrouwbaar en efficiënt op gedeelde infrastructuur draaien. Containers geven elk team een consistent verpakkings- en runtimecontract, wat de klasse falen van "het werkt op mijn machine" afschaft. Orkestratie verbergt afzonderlijke machines achter een gemeenschappelijke ondergrond, zodat teams naar een platform deployen in plaats van naar servers. Deze standaardisatie is wat je honderden of duizenden services laat beheren zonder dat elk team deployment, schaling en veerkracht opnieuw uitvindt.

Overnemers uit onderneming en overheid winnen overdraagbaarheid, veerkracht en een pad weg van lock-in. In ruil erven ze echte complexiteit en nieuwe beveiligingsverantwoordelijkheden. Een containerplatform is krachtig juist omdat het programmeerbaar en dynamisch is, wat betekent dat je het zorgvuldig moet besturen. Imageherkomst, isolatie bij multitenancy, netwerkbeleid en kosten worden allemaal zorgen op platformniveau. Overnemers in de publieke sector voegen steeds vaker soevereiniteitseisen toe: controle over waar data zich bevindt en wie er toegang toe heeft. Dat maakt het vermogen consistente werklasten over gekozen omgevingen te draaien een strategisch vermogen, niet slechts een technisch detail.

## Kernprincipes

- Verpak applicaties als kleine, enkelvoudige, onveranderlijke containerimages.
- Oefen imagehygiëne: minimale basisimages, gepinde versies, gescand op kwetsbaarheden en ondertekend.
- Ontwerp applicaties waar mogelijk stateless en horizontaal schaalbaar, met toestand extern.
- Behandel het gewenste-toestandsmodel van het orkestratieplatform als bron van waarheid en laat het zichzelf herstellen.
- Dwing isolatie en minste privilege af tussen tenants, werklasten en namespaces.
- Volg de [twaalf-factor](https://en.wikipedia.org/wiki/Twelve-Factor_App_methodology)principes, een methodologie voor het bouwen van wegwerpbare, configuratie-externaliserende, horizontaal schaalbare apps, en breid ze uit voor de realiteit van gedistribueerde systemen.
- Maak kosten een eersterangs, zichtbare engineeringzorg, geen bijgedachte.
- Geef de voorkeur aan draagbare, op standaarden gebaseerde abstracties om strategische flexibiliteit te behouden.

## Aanbevelingen

### Oefen rigoureuze imagehygiëne

Het containerimage is je fundamentele eenheid van vertrouwen en deployment, dus behandel het zo. Begin vanuit minimale, vertrouwde basisimages om het aanvalsoppervlak te verkleinen. Pin versies van afhankelijkheden en basisimages voor reproduceerbaarheid. Scan elk image op bekende kwetsbaarheden in de buildpijplijn en blokkeer die met kritieke bevindingen. Onderteken images en verifieer handtekeningen bij deployment, zodat alleen goedgekeurde, ongewijzigde images draaien. Houd een gecureerd intern register van geharde basisimages aan waarvan teams bouwen. Dat verspreidt goede beveiligingsstandaarden automatisch.

### Gebruik Kubernetes-patronen in plaats van ze opnieuw uit te vinden

Kubernetes beloont teams die zijn gevestigde patronen overnemen en straft teams die tegen zijn model vechten. Gebruik declaratieve manifesten voor gewenste toestand. Voeg gezondheidsprobes toe zodat het platform ongezonde instanties kan detecteren en vervangen. Stel resource requests en limits in zodat de planner werklasten veilig kan inpakken. Gebruik horizontale autoscaling voor elastische vraag. Gebruik voor operationele logica die continu moet draaien, zoals een database beheren, certificaten roteren of eigen resources verzoenen, het operatorpatroon, dat menselijke operationele kennis codeert in software die toestand bewaakt en handelt. Weersta de drang maatwerkorkestratie bovenop het platform te bouwen. Geef de voorkeur aan de native constructies.

### Ontwerp multitenancy bewust

Wanneer veel teams een cluster delen, is isolatie een beveiligings- en betrouwbaarheidseis, geen aardigheid. Gebruik namespaces als tenancygrenzen. Dwing resourcequota af zodat geen tenant anderen kan uithongeren. Pas netwerkbeleid toe om verkeer te beperken tot wat expliciet is toegestaan. Gebruik [rolgebaseerde toegangscontrole](https://en.wikipedia.org/wiki/Role-based_access_control) (RBAC) om te beperken wat elk team kan doen. Overweeg voor werklasten met sterkere isolatiebehoeften aparte clusters of sterkere sandboxing. Besluit vroeg of je model zachte multitenancy (vertrouwde interne teams) of harde multitenancy (elkaar wantrouwende werklasten) is, want de twee vragen zeer verschillende maatregelen.

### Bouw cloud-native, twaalf-factor en verder

De twaalf-factormethodologie, met haar expliciete afhankelijkheden, configuratie in de omgeving, stateless processen, wegwerpbaarheid enzovoort, blijft een uitstekende basis voor services die gedijen op een dynamisch platform. Breid haar uit voor de toegevoegde realiteit van gedistribueerde systemen. Ontwerp voor gedeeltelijk falen. Maak operaties idempotent en herhaalbaar. Stel gezondheid en telemetrie beschikbaar. Behandel observeerbaarheid als ingebouwde functie in plaats van aanvulling. Externaliseer alle toestand naar beheerde dataservices, zodat applicatie-instanties wegwerpbaar en horizontaal schaalbaar blijven.

### Plan multicloud-, hybride en soevereine strategieën pragmatisch

Overdraagbaarheid is waardevol, maar streef haar met heldere ogen na. Standaardiseer op draagbare abstracties als containers, Kubernetes en open API's, zodat werklasten kunnen verhuizen indien nodig. Maar vermijd de valstrik elke beheerde dienst te weigeren, wat echte productiviteit ruilt tegen hypothetische overdraagbaarheid. Ontwerp voor hybride en soevereine eisen zodat dezelfde werklasten en pijplijnen kunnen draaien in een gekozen regio, een privédatacenter of een soevereine cloud die aan jurisdictionele en dataresidentieregels voldoet. Maak de grenzen van soevereiniteit en residentie expliciet in architectuur en beleid.

### Maak kosten zichtbaar met FinOps

In elastische cloudomgevingen zijn kosten een direct gevolg van engineeringbeslissingen, dus geef engineers zicht en verantwoording. Tag bronnen voor kostentoewijzing. Wijs uitgaven toe aan teams en services. Toon kostendata naast prestatiestatistieken. Dimensioneer werklasten op maat, gebruik autoscaling om vraag te volgen en win ongebruikte bronnen terug. Zet een FinOps-praktijk op die engineering, financiën en product samenbrengt, zodat cloudkosten een gedeelde, continue verantwoordelijkheid worden in plaats van een kwartaalverrassing.

## Afwegingen: voor- en nadelen

| Keuze | Voordelen | Nadelen | Past het best bij |
|---|---|---|---|
| Kubernetes | Krachtig, draagbaar, enorm ecosysteem | Steile complexiteit. Operationele last | Veel services op schaal |
| Beheerde containerdienst | Minder ops-last. Snellere start | Enige lock-in. Minder controle | Teams die eenvoud willen |
| Eén gedeeld cluster | Efficiënt resourcegebruik | Moeilijker isolatie. Schadezone | Vertrouwde interne tenants |
| Cluster per tenant | Sterke isolatie | Hogere kosten en overhead | Wantrouwende of gereguleerde werklasten |
| Multicloud-overdraagbaarheid | Flexibiliteit. Vermijdt lock-in | Services op laagste gemene deler | Strategische risicobeperking |
| Diepe beheerde services bij één cloud | Maximale productiviteit | Leveranciersafhankelijkheid | Snelheidsgerichte teams |

De overkoepelende afweging is vermogen tegenover complexiteit. Kubernetes en cloud-native architecturen leveren elasticiteit, veerkracht en snelheid. Maar ze leggen een aanzienlijke operationele en cognitieve last op die kleine teams routinematig onderschatten. Evenzo ruilt volledige [multicloud](https://en.wikipedia.org/wiki/Multicloud)-overdraagbaarheid najagen productiviteit tegen optionaliteit. Het juiste antwoord hangt af van schaal en risico. Grote organisaties met veel teams en sterke governancebehoeften rechtvaardigen de investering meestal. Kleinere inspanningen worden vaak beter bediend door beheerde services die de complexiteit verbergen.

## Vragen om met je team te bespreken

1. **Onderteken je images en verifieer je handtekeningen bij deployment, en blokkeert een kritieke kwetsbaarheid werkelijk de build?** Het image is je eenheid van vertrouwen, dus de toeleveringsketen eromheen verdient harde poorten, geen waarschuwingen. Besluit of alleen ondertekende, geverifieerde images mogen draaien, of scannen kritieke bevindingen blokkeert of slechts logt en wie het gecureerde register van geharde basisimages onderhoudt waarvan teams bouwen. Voor werklasten van onderneming en overheid is dit vaak een complianceeis, en het is ook je beste verdediging tegen een vergiftigde afhankelijkheid die productie bereikt. Neem de huidige stand mee: welk deel van de draaiende images komt van je geharde basis, hoeveel dragen ongepatchte kritieke CVE's en of enig niet-ondertekend image nu kan worden ingepland. Als een kritieke bevinding een deploy niet stopt, is je scanner decoratie.

2. **Hoe voorkomen resource requests, limits en quota dat de ene werklast zijn buren uithongert, zonder dure capaciteit ongebruikt te laten?** Op een gedeeld cluster kan een werklast zonder limieten alles om zich heen laten crashen of throttlen, en te royaal ingestelde quota verspillen de benuttingswinst die het platform rechtvaardigt. Besluit verstandige standaarden, wie ze afstemt en hoe je werklasten vangt waar helemaal geen requests zijn ingesteld. Op schaal is dit zowel een betrouwbaarheids- als een kostenmaatregel, omdat op maat dimensioneren is waar veel van de FinOps-besparing leeft. Neem data mee: huidige clusterbenutting, hoe vaak werklasten worden verwijderd of gethrottled en welke namespaces geen quota hebben. Het doel is dicht, veilig inpakken, dus behandel ontbrekende limieten als defect dat het platform afwijst.

3. **Welke toestand mag in een container leven, en waar gaat al het andere heen?** Cloud-native veerkracht hangt af van wegwerpbare instanties die het platform naar believen kan herplannen, en dat geldt alleen als belangrijke toestand in beheerde dataservices leeft in plaats van op de lokale schijf van de container. Besluit de regel expliciet, want toestand per ongeluk in een container opgeslagen wordt dataverlies bij de volgende herplanning. Voor teams die oudere applicaties migreren is dit vaak het moeilijkste deel, aangezien legacyservices een stabiel lokaal bestandssysteem aannemen. Neem een inventaris mee: welke services lokale toestand schrijven, welke leunen op sticky sessions of knooppuntaffiniteit en wat het zou kosten om elk te externaliseren. Zolang toestand niet extern is, heb je containers die elastisch lijken maar niet echt verplaatst kunnen worden.

4. **Wanneer veel teams een cluster delen, is je isolatiemodel dan bewust gekozen als zachte of harde multitenancy, en passen de maatregelen bij die keuze?** Namespaces scheiden vertrouwde interne teams, maar ze bevatten geen werklast die actief vijandig of gecompromitteerd is, en zachte tenancy behandelen alsof ze hard was is een beveiligingsincident dat wacht te gebeuren. Besluit per werklast of tenants slechts eerlijk delen nodig hebben of aangenomen moeten worden elkaar te wantrouwen, en stem dan de maatregelen af: namespaces, quota, netwerkbeleid en RBAC voor het zachte geval, aparte clusters of sterkere sandboxing voor het harde geval. Voor een grote organisatie drijft deze beslissing de kosten direct, omdat een cluster per tenant veel duurder is dan gedeelde namespaces, dus je wilt het isolatiebudget alleen besteden waar het dreigingsmodel het eist. Neem de tenantinventaris mee: welke werklasten vandaag een cluster delen, welke gereguleerd of extern gericht verkeer afhandelen en waar netwerkbeleid nog default-allow is. In omgevingen van onderneming en overheid is wantrouwende werklasten mengen onder zachte tenancy precies de bevinding die een auditor zal markeren, dus noem de grens voordat zij dat doen.

5. **Hoeveel betaal je voor multicloud-overdraagbaarheid, en ga je haar ooit werkelijk gebruiken?** Standaardiseren op containers, Kubernetes en open API's houdt werklasten verplaatsbaar, maar elke beheerde dienst weigeren om die optie te bewaren ruilt echte, dagelijkse productiviteit tegen overdraagbaarheid die de organisatie misschien nooit uitoefent. Besluit waar overdraagbaarheid een echte eis is, zoals een soevereiniteits- of exitverplichting die je hebt ondertekend, tegenover waar het een geruststellend gebaar is dat elk team vertraagt. De concurrerende overweging is snelheid: diepe beheerde services leveren functies sneller op, en een architectuur van de laagste gemene deler is een blijvende belasting op elk team. Neem het bewijs mee: welke beheerde services je hebt vermeden en wat dat aan engineeringtijd kostte, of je ooit een werklast tussen aanbieders hebt verplaatst en wat je contracten werkelijk verplichten. Voor overheids- en gereguleerde overnemers kunnen dataresidentie en soevereine-cloudregels overdraagbaarheid niet onderhandelbaar maken, dus ontwerp zodat dezelfde manifesten en pijplijnen in een soevereine regio en een private enclave draaien, maar wees eerlijk dat dit een compliancekost is in plaats van gratis verzekering.

6. **Kan elk team zien wat het uitgeeft, en bezit iemand de rekening voordat het een verrassing wordt?** In een elastisch platform zijn kosten een direct resultaat van engineeringbeslissingen, toch loopt zonder kostentoewijzingstags en zichtbare dashboards uitgaven op in een gedeelde pool waar niemand zich verantwoordelijk voor voelt tot financiën escaleert. Besluit hoe je kosten aan teams en services toewijst, wie ze beoordeelt en of engineers kosten naast prestatiestatistieken zien of er maar eens per kwartaal van horen. De spanning is tussen verantwoording en wrijving: duw kosten te hard en elke beslissing wordt een budgetonderhandeling, negeer ze en ongebruikte, te grote werklasten stapelen stilletjes op. Neem de getallen mee: huidige uitgaven per team, hoeveel capaciteit ongebruikt of te groot is en hoe snel een op hol geslagen werklast zou worden opgemerkt. Voor budgetten van onderneming en overheid zijn niet-toegewezen cloudkosten zowel een governancefalen als een echt financieel risico, dus zet een FinOps-praktijk op die engineering, financiën en product in hetzelfde gesprek zet in plaats van achteraf af te stemmen.

## Sectorperspectief

**Startup.** Grijp naar een beheerde containerdienst in plaats van een zelf gehost Kubernetes-cluster: met een paar services en geen platformengineer zijn controlevlakken een afleiding die je niet kunt betalen. Verpak kleine images vanaf een minimale basis, pin versies, voeg één kwetsbaarheidsscan toe aan de build en duw alle toestand naar een beheerde database zodat instanties wegwerpbaar blijven. Sla namespaces, operators en multicloud-overdraagbaarheid over tot je werkelijk de services en de mensen hebt om ze te rechtvaardigen.

**Kleinbedrijf.** Zonder aparte platformspecialist en met een krap budget leun je sterk op beheerde services en laat je de aanbieder de orkestratie draaien die je anders zou moeten bemannen. Behandel containerbasis als je beveiligingsvloer: minimale images, versies pinnen en een scan in de pijplijn geven het meeste van de bescherming voor weinig inspanning. Geef de voorkeur aan een ondersteund platform kopen boven er een bouwen, en houd genoeg overdraagbaarheid, standaardcontainers en open API's, dat je niet vastzit als prijzen of voorwaarden veranderen.

**Grote onderneming.** De taak is platformgovernance over veel teams: een centraal platformteam dat geharde basisimages levert, ondertekenings- en scanpoorten, namespace-tenancy met quota, netwerkbeleid en RBAC, plus kostentoewijzingstags en een FinOps-dashboard. Standaardiseer het deploymentcontract zodat honderden services op dezelfde manier werken, en beheer beveiliging, multitenancy en kosten centraal terwijl teams deployment zelf bedienen. Financier het platformteam goed, want een ondergefinancierd platform wordt het knelpunt waar de hele organisatie op wacht.

**Overheid.** Soevereiniteit, dataresidentie en publieke verantwoording geven de architectuur vorm. Draai werklasten op standaardcontainers en Kubernetes zodat dezelfde pijplijnen in een soevereine regio en een geaccrediteerde on-premisesenclave draaien, en codeer residentie- en toegangsgrenzen als beleid in plaats van conventie. Haal images uit een intern geharde register, pas harde multitenancy toe op de gevoeligste data en behoud de overdraagbaarheid die je veerkracht en onderhandelingshefboom geeft, aangezien aanbestedingsregels vaak lock-in bij één leverancier verbieden.

## Voorbeelden

**Startup.** Een startup van zes personen verpakt haar twee services als kleine containerimages gebouwd vanaf een minimale basis, en draait ze op een beheerde containerdienst in plaats van een zelf gehost Kubernetes-cluster, zodat niemand controlevlakken hoeft te babysitten. Ze pinnen versies van basisimages en voegen een kwetsbaarheidsscan toe aan hun build, maar slaan bewust de zwaardere orkestratiefuncties over tot ze werkelijk meer dan een handvol services hebben. Toestand leeft in een beheerde Postgres-database, wat de containers wegwerpbaar houdt en het platform ze laat herstarten of schalen zonder enig dataverlies.

**Grote onderneming.** Een telecombedrijf draait enkele honderden [microservices](https://en.wikipedia.org/wiki/Microservices) op gedeelde Kubernetes-clusters. Een platformteam levert geharde basisimages, dwingt imageondertekening en kwetsbaarheidspoorten af en isoleert bedrijfsonderdelen in namespaces met quota, netwerkbeleid en RBAC. Kostentoewijzingstags en een FinOps-dashboard wijzen uitgaven toe aan elke productlijn, en autoscaling dimensioneert capaciteit op vraag. Productteams deployen tientallen keren per dag naar een consistent platform zonder servers te beheren. Het bedrijf houdt centrale controle over beveiliging en kosten.

**Overheid.** Een nationale gezondheidsdienst moet burgerdata binnen nationale grenzen en onder nationale wettelijke controle houden. Ze draait haar werklasten op een soevereine cloudregio met standaardcontainers en Kubernetes, zodat dezelfde pijplijnen en manifesten ook in een geaccrediteerde on-premisesomgeving draaien voor de gevoeligste data. Grenzen voor dataresidentie en toegang zijn als beleid gecodeerd, images komen uit een intern geharde register en harde multitenancy isoleert gevoelige werklasten. Overdraagbaarheid over de soevereine regio en de private enclave geeft de dienst veerkracht en onderhandelingshefboom zonder compliance op te offeren.

## Zakelijke onderbouwing: motivatie, ROI en TCO

Het ROI van containers en orkestratie komt uit hogere resourcebenutting, snellere en betrouwbaardere deployments, elastische schaling die uitgaven aan vraag koppelt en verbeterde veerkracht door zelfherstel. Standaardiseren op een gemeenschappelijk platform vermindert dubbele inspanning over teams en versnelt onboarding, omdat elke service hetzelfde deployment- en operationele contract volgt.

De TCO-analyse moet eerlijk zijn over de operationele last. Adoptiekosten omvatten platform-engineeringpersoneel, training, beveiligingstooling voor images en clusters en de doorlopende inspanning om het platform zelf te draaien. De kosten van niet adopteren omvatten inconsistente maatwerkdeployment over teams, slechte benutting van dure infrastructuur, brosse handmatige schaling en moeite met het halen van veerkracht- en soevereiniteitseisen. Voor leiderschap rust de zaak op schaal. Onder een bepaald aantal services loont de complexiteit mogelijk niet en is een beheerde dienst verstandiger. Maar op schaal van onderneming en overheid is een bestuurd cloud-native platform meestal het meest kosteneffectieve en veerkrachtige fundament, mits je het platformteam financiert om het goed te draaien.

## Antipatronen en valkuilen

- **Dikke, ongescande images.** Opgeblazen images gebouwd van onbetrouwbare basissen dragen onnodige kwetsbaarheden en vertragen alles.
- **Kubernetes voor alles.** Een complexe orkestrator overnemen voor een handvol eenvoudige services koopt complexiteit zonder opbrengst.
- **Resourcelimieten negeren.** Zonder requests en limits kan de ene werklast zijn buren uithongeren of laten crashen.
- **Zachte tenancy voor vijandige werklasten.** Alleen op namespaces leunen om wantrouwende tenants te isoleren is een beveiligingsincident dat wacht te gebeuren.
- **Per ongeluk toestandsvolle containers.** Belangrijke toestand opslaan in wegwerpbare containers leidt tot dataverlies bij herplannen.
- **Kostenblindheid.** Cloudkosten behandelen als vaste overhead in plaats van engineeringuitkomst leidt tot op hol geslagen rekeningen.
- **Overdraagbaarheidstheater.** Alle beheerde services weigeren om overdraagbaarheid te bewaren die de organisatie nooit zal gebruiken.

## Volwassenheidsmodel

**Niveau 1: Initiëren.** Containers worden ad hoc gebruikt, zo al. Images worden met de hand gebouwd en niet gescand, deployment is handmatig en reactief en er is geen gedeeld platform, kostenzicht of isolatiemodel.

**Niveau 2: Ontwikkelen.** Teams containeriseren applicaties en nemen een orkestrator over, maar praktijken variëren tussen groepen. Imagescanning, resourcelimieten en ondertekening zijn inconsistent, en kosten en multitenancy worden niet systematisch bestuurd.

**Niveau 3: Standaardiseren.** Een gestandaardiseerd platform is gedocumenteerd en over de organisatie afgedwongen: geharde basisimages, ondertekenings- en scanpoorten, namespace-tenancy met quota en netwerkbeleid, RBAC en kostentoewijzing. Cloud-native en twaalf-factorpatronen zijn de verwachte norm in plaats van een lokale keuze.

**Niveau 4: Beheersen.** Het platform wordt gemeten en beheerst aan de hand van uitgangswaarden. Je volgt clusterbenutting, het aandeel draaiende images gebouwd op de geharde basis, ongepatchte kritieke kwetsbaarheden, deploymentfrequentie en wijzigingsfaalpercentage, verwijderings- en throttlingpercentages en kosten per team en service tegen budget. Poorten worden afgedwongen op dit bewijs: ontbrekende resourcelimieten en niet-ondertekende images worden automatisch afgewezen, en afdrijving van de standaard triggert actie in plaats van een waarschuwing.

**Niveau 5: Orkestreren.** Het platform is self-service en zelfherstellend, over de organisatie geïntegreerd en adaptief. FinOps dimensioneert capaciteit continu op maat en wint haar terug, draagbare architectuur ondersteunt hybride en soevereine eisen, en het platform verbetert continu uit gemeten gebruik, componenten afschaffend en vervangend naarmate werklasten, kosten en het risicobeeld verschuiven.

## Ideeën voor discussie

- Bij welke schaal houdt Kubernetes overnemen op complexiteit om haarzelf te zijn en begint het te lonen?
- Waar ligt de juiste grens tussen zachte en harde multitenancy voor je werklasten?
- Hoeveel moet je investeren in multicloud-overdraagbaarheid tegenover de productiviteit van diepe beheerde services?
- Hoe geef je engineers echte kostenverantwoording zonder elke beslissing in een budgetonderhandeling te veranderen?
- Wat is je governancemodel voor basisimages, en wie onderhoudt het geharde register?
- Hoe geven soevereiniteits- en dataresidentie-eisen je platformarchitectuur vorm?

## Belangrijkste inzichten

- Containers standaardiseren verpakking en runtime. Orkestratie standaardiseert beheer op schaal.
- Imagehygiëne, dat wil zeggen minimale, gepinde, gescande, ondertekende images, is fundamentele beveiliging.
- Gebruik native Kubernetes-patronen en operators in plaats van maatwerkorkestratie te bouwen.
- Kies een multitenancymodel bewust op basis van hoeveel de werklasten elkaar vertrouwen.
- Volg twaalf-factor en breid uit voor realiteiten van gedistribueerde systemen als gedeeltelijk falen en observeerbaarheid.
- Behandel kosten als engineeringuitkomst en beheer ze continu via FinOps.

## Referenties en verder lezen

- Adam Wiggins, *The Twelve-Factor App* (methodology).
- Brendan Burns, Joe Beda, and Kelsey Hightower, *Kubernetes Up & Running*.
- Bilgin Ibryam and Roland Huß, *Kubernetes Patterns*.
- Cornelia Davis, *Cloud Native Patterns*.
- J.R. Storment and Mike Fuller, *Cloud FinOps*.
- Liz Rice, *Container Security*.
- Cloud Native Computing Foundation (CNCF), cloud-native definition and landscape.
