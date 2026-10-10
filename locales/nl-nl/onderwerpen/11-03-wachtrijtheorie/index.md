# 11.3 Wachtrijtheorie

## Overzicht en motivatie

[Wachtrijtheorie](https://en.wikipedia.org/wiki/Queueing_theory) is de wiskundige studie van wachtrijen. In software-engineering is het de stille theorie achter een enorme hoeveelheid praktijk. Reactiesnelheid van klantenservice, [kanban](https://en.wikipedia.org/wiki/Kanban_%28development%29)planning (een pull-gebaseerde methode die [werk in uitvoering](https://en.wikipedia.org/wiki/Work_in_process) begrenst om flow te verbeteren), berichtenwachtrijen tussen processen, continuous-deploymentpijplijnen: dit zijn allemaal wachtrijen, en ze gehoorzamen allemaal dezelfde wetten. Die wetten begrijpen laat een team redeneren over [doorlooptijden](https://en.wikipedia.org/wiki/Lead_time), [doorvoer](https://en.wikipedia.org/wiki/Throughput), capaciteit en de ware kosten van systemen dicht bij hun grenzen draaien, in plaats van er in productie door verrast te worden. Dit hoofdstuk staat in het deel over Flow omdat wachtrijtheorie het formele fundament van flow is: ze verklaart *waarom* werk wacht, en wat het wachten werkelijk vermindert.

Hier is de motivatie: intuïtie over wachtrijen is betrouwbaar fout, en op dure manieren fout. Mensen nemen aan dat een server op 90% benutting "10% van problemen verwijderd" is, terwijl wachttijden niet-lineair exploderen naarmate benutting 100% nadert. Ze nemen aan dat meer werk in uitvoering (WIP) toevoegen oplevering versnelt, terwijl het doorlooptijden verlengt. Ze plannen capaciteit rond gemiddelden en worden dan vernietigd door variabiliteit. Een beetje wachtrijtheorie vervangt deze kostbare intuïties door een klein aantal robuuste verbanden, het belangrijkst **[de wet van Little](https://en.wikipedia.org/wiki/Little%27s_law)**, die gelden over klantwachtrijen, taakborden en CI/CD-pijplijnen eveneens.

Voor grote teams, onderneming en overheid is wachtrijtheorie een gedeelde taal voor capaciteit en flow, een die rollen verbindt die anders langs elkaar heen praten. Productmanagers geven om doorlooptijd van idee tot klant. SRE's geven om serverbenutting en latentie. DevOps-teams geven om deploymentfrequentie. Supportleiders geven om reactietijden. Dit zijn allemaal wachtrijstatistieken, en ze in één kader uitdrukken (aankomstsnelheid, servicesnelheid, benutting, wachttijd) laat een organisatie capaciteit plannen, realistische SLO's (service level objectives) stellen en investering rechtvaardigen met wiskunde in plaats van anekdote.

## Kernprincipes

- **Alles met een wachttijd is een wachtrij:** tickets, taken, berichten en deploys inbegrepen.
- **De wet van Little is het anker:** items in het systeem = aankomstsnelheid × tijd in het systeem (κ = λτ).
- **Benutting en wachttijd zijn niet-lineair:** de laatste 15% capaciteit is de duurste.
- **Variabiliteit is de vijand van flow:** gemiddelden verbergen de pijn. Variantie creëert wachtrijen.
- **Werk in uitvoering verminderen vermindert doorlooptijd:** flow, niet drukte, is het doel.
- **Meet de hele flow:** aankomsten, service, successen, falen, overslagen en wachttijden.
- **Een proces is een wachtrij van wachtrijen:** modelleer fasen en optimaliseer dan de beperkende.

## Aanbevelingen

### Leer de kernnotatie en gebruik haar consistent

Een handvol grootheden beschrijft elke wachtrij. Erop standaardiseren (Griekse letters zijn conventie) verwijdert dubbelzinnigheid over teams:

- **λ (lambda), aankomstsnelheid:** hoe snel nieuwe items binnenkomen.
- **μ (mu), servicesnelheid:** hoe snel items worden afgehandeld. Omdat "servicesnelheid" dubbelzinnig wordt gebruikt, is het vaak de moeite waard doorvoer expliciet te splitsen in **totaalsnelheid (χ)**, **succesnelheid (α)**, **faalsnelheid (β)** en **overslagsnelheid (σ)**, waar χ = α + β + σ.
- **ρ (rho), benutting / verkeersintensiteit = λ / μ:** de enkele belangrijkste samenvatting. ρ < 1 betekent dat de wachtrij leegloopt. ρ ≥ 1 betekent dat ze onbegrensd groeit.
- **Tijden:** doorlooptijd (τ, begin tot einde), werktijd (φ, werkelijke verwerking), wachttijd (ω, in afwachting) en staptijd (θ, tussen afrondingen).
- **ε (epsilon), foutverhouding:** falen ÷ totaal.

Falen en *overslagen* expliciet benoemen telt in software: een item dat wordt verlaten (een klant die opgeeft, een winkelwagen die achterblijft, een afgewezen werkticket) verlaat de wachtrij zonder bediend te zijn, en doen alsof het "bediend" werd corrumpeert je statistieken. Volg **balking** (besluiten niet aan te sluiten), **reneging** (opgeven na wachten) en **jockeying** (van wachtrij wisselen) als eersterangs uitkomsten.

### Veranker planning op de wet van Little

De wet van Little stelt dat het langetermijngemiddelde aantal items in een stabiel systeem gelijk is aan de gemiddelde aankomstsnelheid maal de gemiddelde tijd die elk item in het systeem doorbrengt: **κ = λ τ** (klassiek L = λW). Ze is verbazingwekkend algemeen (ze vraagt geen aanname over de aankomstverdeling of de servicevolgorde), wat haar het werkpaard van flowplanning maakt. Herschikt vertelt ze je dat **doorlooptijd = werk in uitvoering ÷ doorvoer**. Dat is de wiskundige basis van kanban en lean: als je kortere doorlooptijden wilt en je doorvoer niet kunt verhogen, moet je WIP verlagen. Ze geeft ook snelle gezondheidscontroles. Als 40 tickets open staan en je sluit er 8 per dag, duurt het gemiddelde ticket ongeveer 5 dagen, hoe druk iemand zich ook voelt. Haar enige eis is *stabiliteit*: aankomsten mogen niet aanhoudend vertrekken overtreffen (ρ < 1), anders breken de wachtrij en de aannames van de wet af.

### Respecteer de niet-lineariteit van benutting

De belangrijkste operationele les van wachtrijtheorie is dat responstijd scherp stijgt, niet geleidelijk, naarmate benutting 100% nadert. Bob Wescotts *Seven insights into queueing theory* vatten de praktische gevolgen levendig samen:

1. Hoe trager het servicecentrum, hoe lager de piekbenutting waarvoor je moet plannen.
2. Het is heel moeilijk de laatste 15% van wat dan ook te gebruiken.
3. Hoe dichter je bij de rand draait, hoe hoger de prijs van het ongelijk hebben.
4. Groei van responstijd wordt begrensd door hoeveel items kunnen wachten.
5. Dit zijn gemiddelden, geen maxima: plan voor de staart.
6. Pas op voor het menselijke ontkenningseffect over meerdere servicecentra.
7. Toon kleine verbeteringen in hun beste licht.

De ontwerpimplicatie: **voorzie bewust ruimte.** Mikken op 70–80% benutting voor latentiegevoelige systemen is geen verspilling. Het is voorspelbare responstijd kopen. Dit informeert direct capaciteitsplanning en SLO's (hoofdstuk 3.5 en 9.1).

### Modelleer processen als een wachtrij van wachtrijen

Echt werk stroomt door fasen, en een meertrapsproces is eenvoudig een wachtrij waarvan de items zelf bij elke stap in de wachtrij staan. Modelleer het zo: de aankomstsnelheid van het proces is de aankomstsnelheid van fase 1. De succesnelheid van het proces is de succesnelheid van de laatste fase. De fout- en overslagaantallen van het proces zijn de sommen over fasen. Twee gangbare vormen keren terug:

- **Trechters**, waar het aantal items per fase krimpt (werving: outreach → interview → aanbod. Inkoop: browsen → winkelwagen → betalen. Oplevering: integreren → UAT → productie). Optimaliseer de fase die het meest telt: maximaliseer aankomsten aan de bovenkant van de trechter, minimaliseer overslagen midden in de trechter (verlaten winkelwagens) of minimaliseer fouten in de laatste fase (slechte productie-uitrol).
- **Double-diamond**-discovery-en-opleveringsflows (ontdekken → definiëren → ontwikkelen → opleveren), die het deel Flow van dit boek direct behandelt (hoofdstuk 11.1).

De **beperkende fase** (het knelpunt) vinden en verlichten is waar flowverbetering loont. Niet-beperkingen optimaliseren verplaatst de wachtrij slechts.

### Verbind wachtrijstatistieken met de KPI's die teams al gebruiken

Wachtrijgrootheden sluiten schoon aan op de leverings- en betrouwbaarheidsstatistieken elders in dit boek, wat de theorie praktisch maakt in plaats van academisch:

- **Opleveringsdoorlooptijd (Dτ)**, "concept tot klant," is een doorlooptijdmaat (τ) en een DORA-statistiek ([DevOps Research and Assessment](https://en.wikipedia.org/wiki/DevOps_Research_and_Assessment)) (hoofdstuk 11.2).
- **Deploymentfrequentie (Dμ)** is een servicesnelheidsmaat.
- **Wijzigingsfaalpercentage (Dε)** is een foutverhouding.
- **Tijd tot herstel (Rτ)** is een herstel-doorlooptijd, d.w.z. MTTR (hoofdstuk 9.3).

Onderscheid de verschillende **MTTR's** (gemiddelde tijd om te *reageren*, *repareren*, *herstellen* en *op te lossen*) omdat ze verschillende segmenten van de incidentwachtrij meten en routinematig worden verward. SLI's/SLO's/SLA's (hoofdstuk 9.1) in wachtrijtermen gronden houdt doelen eerlijk en vergelijkbaar.

## Afwegingen: voor- en nadelen

| Beslissing | Voordelen | Nadelen |
|---|---|---|
| **Systemen op hoge benutting draaien** | Lagere hardware-/kosten per eenheid | Niet-lineaire latentie-explosies. Fragiel bij pieken |
| **Ruime marge voorzien** | Voorspelbare latentie. Veerkrachtig tegen variantie | Hogere vaste kosten. Lijkt "ondergebruikt" |
| **WIP beperken (kanban)** | Kortere doorlooptijden. Minder contextwisselen | Voelt langzamer. Vraagt discipline om de limiet te houden |
| **Formele wachtrijmodellering** | Gekwantificeerde capaciteitsbeslissingen. Minder verrassingen | Leercurve. Modellen vereenvoudigen rommelige werkelijkheid |
| **Alleen vuistregels** | Snel, geen wiskunde | Fout juist waar het het duurst is (nabij capaciteit) |

De terugkerende afweging is **efficiëntie tegenover voorspelbaarheid**: benutting opvoeren bespaart geld tot het plotseling niet meer doet, waarna de kosten van latentie, falen en brandjes blussen de besparingen overtreffen. De bijdrage van wachtrijtheorie is je te vertellen *waar* die afgrond ligt zodat de afweging een keuze is, geen ongeluk.

## Vragen om met je team te bespreken

1. **Wat is je expliciete benuttingsdoel voor elk latentiegevoelig systeem, en wie heeft het goedgekeurd?** Ruimte is een bewuste aankoop van voorspelbare latentie, dus het moet een vermeld beleid zijn, geen toeval van welke belasting toevallig arriveerde. Omdat responstijd niet-lineair stijgt, kan draaien op 85% al verhoogde staartlatentie betekenen, maar financiën ziet ruimte als verspilling en duwt benutting omhoog. Neem de getallen mee: huidige benutting, de gemeten latentiecurve en de kosten van je laatste latentie-incident, en toon dan waar de afgrond voor elke service ligt. Stel voor systemen van onderneming en overheid met seizoenspieken (aangifteseizoen, inschrijfvensters) het doel buiten de afgrond voor de piek, niet het gemiddelde. Als niemand het benuttingsdoel bezit, blijven latentie-incidenten "uit het niets" verschijnen.

2. **Waar in je systemen is een wachtrij onbegrensd, zonder tegendruk om belasting af te werpen wanneer overweldigd?** Een onbegrensde wachtrij faalt niet soepel. Ze degradeert tot instorting, omdat aankomsten die aanhoudend vertrekken overtreffen (rho >= 1) betekent dat de wachtrij zonder limiet groeit. Inventariseer je berichtenwachtrijen, threadpools en verzoekbuffers en vraag wat er bij elk gebeurt wanneer de aankomstsnelheid de servicesnelheid overtreft: werpt het belasting af, past het tegendruk toe of valt het om? Dit telt acuut op ondernemingsschaal, waar één verzadigde downstream over services kan cascaderen. Neem een belastingtestresultaat of een eerder incident mee waar een wachtrij ophoopte en controleer of het systeem overtollig werk afwees of het allemaal probeerde vast te houden. De oplossing zijn begrensde wachtrijen met expliciete tegendruk en timeouts afgeleid van de wet van Little, zodat een overbelasting afwerpt in plaats van omvalt.

3. **Modelleer je je flow van idee naar productie als wachtrij van wachtrijen, en zijn je verbeteringen op de echte beperking gericht?** Een meertrapsproces is een wachtrij waarvan de items bij elke fase in de wachtrij staan, en alles behalve de beperkende fase optimaliseren verplaatst de wachtrij slechts. Breng je opleveringstrechter in kaart (integreren naar UAT naar productie, of ontdekken naar definiëren naar ontwikkelen naar opleveren) en meet aankomst-, service-, wacht- en overslagsnelheden bij elke fase om te vinden waar werk werkelijk ophoopt. Teams optimaliseren routinematig de fase die ze het best begrijpen in plaats van het knelpunt, wat inspanning besteedt en niets beweegt. Neem wachttijddata per fase mee, geen onderbuikgevoel, want het knelpunt is vaak een wachttoestand (review, goedkeuring, omgevingsbeschikbaarheid) in plaats van een werktoestand. Zodra je de beperking kent, richt je daarop en laat je de niet-beperkingen met rust.

4. **Gebruik je de wet van Little om WIP-limieten te stellen, of voeg je capaciteit toe om doorlooptijden te genezen die alleen meer discipline zou oplossen?** De wet van Little zegt dat doorlooptijd gelijk is aan werk in uitvoering gedeeld door doorvoer, dus als je de doorvoer niet kunt verhogen is de enige hefboom die overblijft voor kortere doorlooptijden WIP verlagen, wat niets kost dan terughoudendheid. De concurrerende trek is echt: werk in uitvoering begrenzen voelt langzamer en stilstaand, en managers onder druk zouden liever aannemen of hardware kopen dan teams zeggen minder te beginnen en meer af te maken. Neem de harde getallen mee, open items en afrondingssnelheid per fase, en bereken de geïmpliceerde gemiddelde doorlooptijd, vergelijk die dan met wat mensen geloven dat het is. Het gat is meestal groot en beschamend. In een grote onderneming of agentschap moet een aanname- of inkoopverzoek gerechtvaardigd als doorlooptijdoplossing eerst tegen deze rekenkunde worden getoetst, want een personeelsuitbreiding die WIP verhoogt kan juist de doorlooptijden verlengen die ze moest verkorten.

5. **Plan je capaciteit rond gemiddelden, of heb je de variabiliteit gekwantificeerd die je wachtrijen werkelijk creëert?** Wachtrijen ontstaan uit variantie, niet uit het gemiddelde, dus twee systemen met identieke gemiddelde belasting kunnen zich totaal anders gedragen als het ene stootsgewijze aankomsten of lange-staartservicetijden heeft. De spanning is dat gemiddelden makkelijk te verzamelen en geruststellend om te rapporteren zijn, terwijl de variantie en de staart moeilijker te meten en onwelkom in een statusupdate zijn. Neem de verdeling mee, niet het gemiddelde: stootachtigheid van aankomsten, de 95e en 99e percentiel service- en wachttijden en de batchgroottes die werk in pieken concentreren. Plan voor systemen van onderneming en overheid met voorspelbare golven (aangifteseizoen, salarisrondes, inschrijfvensters, belasting aan het kwartaaleinde) de buffer en het benuttingsdoel uit de variantie van de piekperiode, want een ontwerp gedimensioneerd op het jaargemiddelde zal falen precies wanneer het publiek kijkt.

6. **Welke van je wachtrijen tellen stilletjes verlatingen en afwijzingen alsof het werk werd bediend, en welke onvervulde vraag verbergt dat?** Een item dat balkt, rent of wordt afgewezen verlaat de wachtrij zonder te worden afgehandeld, en het als "bediend" vastleggen corrumpeert tegelijk je doorvoer, je foutverhouding en je capaciteitsplan. De concurrerende overweging is dat "gesprekken beantwoord" of "tickets gesloten" er op een dashboard beter uitziet dan "bellers die opgaven", dus het eerlijke getal is degene die niemand vrijwillig boven water brengt. Neem de overslagsnelheid (σ) mee, balking- en renegingtellingen en het verschil tussen aangeboden belasting en bediende belasting, zodat de ware vraag zichtbaar wordt. Dit telt scherp bij overheidsdienstverlening, waar burgers die een telefoonwachtrij of een uitkeringsaanvraag verlaten onvervulde verplichtingen zijn in plaats van opgeloste zaken, en ze als afgehandeld rapporteren zowel prestaties verkeerd weergeeft als de capaciteit onderschat die het publiek verschuldigd is.

## Sectorperspectief

**Startup.** Je hebt geen tijd voor formele wachtrijmodellering en geen behoefte eraan. Grijp eerst naar de twee goedkoopste winsten: pas de wet van Little toe op je achterstand om de echte doorlooptijd te zien die je WIP impliceert, en bekijk je kanbanbord voor de fase waar werk ophoopt voordat je aanneemt tegen een knelpunt dat misschien niet bestaat. Houd benutting weg van de afgrond op elk latentiegevoelig pad door ruimte te laten in plaats van af te stemmen, want een uitval tijdens een groeipiek kost veel meer dan wat ongebruikte capaciteit.

**Kleinbedrijf.** Zonder wachtrijspecialist in dienst koop je de statistieken in plaats van de modellen te bouwen. Kies een helpdesk, berichtenbroker of hostingplatform dat al aankomstsnelheid, wachttijd en verlating rapporteert en lees die getallen in plaats van ze af te leiden. Kader de beslissing als letten op twee symptomen: wachttijden die niet-lineair stijgen naarmate je drukker wordt, en klanten die opgeven voordat ze worden bediend, aangezien een verloren klant de wachtrijkost is die een klein bedrijf het meest raakt.

**Grote onderneming.** Het werk is wachtrijdenken een gedeelde discipline maken over veel teams: één afgesproken notatie (λ, μ, ρ, doorlooptijd), consistent WIP- en benuttingsruimtebeleid en tegendrukstandaarden zodat een verzadigde downstream niet over services kan cascaderen. Stel SLO's en capaciteit uit wachtrijanalyse in plaats van gissen, en beheer je wachtrijen als portfolio met uitgangswaarden en reviews zodat geen enkel team geïsoleerd heet draait. Bak de analyse in capaciteitsgovernance en audit, zodat een ruimtedoel een gedocumenteerde beslissing is die iemand bezit.

**Overheid.** Aanbesteding, transparantie en publieke verantwoording geven elke capaciteitskeuze vorm. Dimensioneer contactcentra en burgergerichte systemen uit variantie van de piekperiode (aangifteseizoen, inschrijfvensters), niet het jaargemiddelde, en bemand om benutting weg van de afgrond te houden wanneer vraag piekt. Volg balking en reneging als onvervulde publieke vraag in plaats van ze te verbergen in "gesprekken beantwoord", en rechtvaardig capaciteitsuitgaven met schattingen van wachttijd via de wet van Little, wat auditors en gekozen functionarissen een verdedigbare, door wiskunde gesteunde zaak geeft in plaats van een anekdote.

## Voorbeelden

**Startup.** Een SaaS-team van vijf personen dat verdrinkt in een supportachterstand neemt aan dat ze nog een medewerker moeten aannemen. Voordat ze het geld uitgeven passen ze de wet van Little toe: 60 open tickets en 12 gesloten per dag betekent dat een gemiddeld ticket ongeveer 5 dagen wacht, wat overeenkomt met de boze e-mails. Hun kanbanbord bekijkend merken ze dat tickets ophopen bij het wachten op engineering, niet op support, dus begrenzen ze werk in uitvoering en sturen bugmeldingen direct de sprint in in plaats van ze te laten wachten. De doorlooptijd daalt naar onder twee dagen zonder nieuwe medewerker, en ze gebruiken het vrijgekomen budget voor het echte knelpunt.

**Grote onderneming.** Een betalingsplatform dat zijn autorisatieservice dimensioneert meet λ ≈ 850 verzoeken/seconde en per node μ ≈ 200/seconde. Naïef is dat ~5 nodes (ρ = 0,85), maar wetend dat ρ = 0,85 al sterk verhoogde staartlatentie betekent, richt het team in op ρ ≈ 0,65 en gebruikt de wet van Little om aantallen verzoeken onderweg te voorspellen en wachtrijdieptes en timeouts in te stellen. Incidenten in het hoogseizoen die vroeger "uit het niets" verschenen verdwijnen, omdat het team niet langer op het steile deel van de curve opereerde.

**Overheid.** Het contactcentrum van een belastingdienst modelleert ondersteuning in het aangifteseizoen als wachtrij: aankomstpieken (λ), agentcapaciteit (μ) en, cruciaal, de **overslagsnelheid (σ)** van burgers die opgeven na lange wachttijden. Door balking en reneging te volgen in plaats van alleen "gesprekken beantwoord" ziet leiderschap de ware onvervulde vraag, bemant ze om benutting tijdens pieken weg van de afgrond te houden en rechtvaardigt ze de extra capaciteit met schattingen van wachttijd via de wet van Little, een verdedigbare, door wiskunde gesteunde zaak voor publieke uitgaven in plaats van een anekdotische.

## Zakelijke onderbouwing: motivatie, ROI en TCO

Wachtrijtheorie loont door twee dure fouten te voorkomen: **overprovisioning** (betalen voor ongebruikte capaciteit die je niet nodig had) en, veel schadelijker, **onderprovisioning nabij de afgrond** (waar kleine belastingstijgingen grote latentie, geschonden SLA's, verlaten klanten en noodbestedingen veroorzaken). Omdat de kosten van draaien nabij 100% benutting niet-lineair zijn, zijn de besparingen van "gewoon wat meer belasting" klein en het neerwaarts risico catastrofaal, precies de asymmetrie die een beetje wiskunde omzet in een bewuste beslissing. Het rendement wordt gemeten in vermeden uitval, gehaalde SLA's, behouden klanten die anders zouden balken en rustigere bereikbaarheidsroosters.

Op **total cost of ownership** is het kader goedkoop om over te nemen (het is kennis, geen tooling) en verbetert het bijna elke capaciteits-, latentie- en flowbeslissing die een grote organisatie over de levensduur van een systeem neemt. De wet van Little en WIP-limieten verkorten doorlooptijden zonder iets te kopen (een puur procesvoordeel), terwijl benuttingsdiscipline een bescheiden, voorspelbare vaste kost ruilt tegen het elimineren van dure, onvoorspelbare falen. Vertaal om de zaak voor leiderschap te maken een recent latentie-incident naar de benuttingscurve en toon hoe een ruimtedoel het had voorkomen, en gebruik de wet van Little om WIP-vermindering direct aan snellere oplevering te koppelen.

## Antipatronen en valkuilen

- **Capaciteit plannen rond gemiddelden:** variantie negeren, wat werkelijk wachtrijen creëert.
- **Heet draaien:** mikken op 90%+ benutting op latentiegevoelige systemen en geschokt zijn door staartlatentie.
- **Overslagen als service tellen:** verlaten klanten of afgewezen tickets als afgehandeld behandelen, wat statistieken corrumpeert.
- **WIP opstapelen:** drukte verwarren met doorvoer en doorlooptijden verlengen.
- **Een niet-knelpunt optimaliseren:** fasen verbeteren die niet de beperking zijn en de wachtrij elders heen verplaatsen.
- **De MTTR's verwarren:** "herstel" rapporteren terwijl je "reparatie" meet, of omgekeerd.
- **Onbegrensde wachtrijen:** geen tegendruk, zodat een overbelast systeem tot instorting degradeert in plaats van belasting af te werpen.
- **Gemiddelden als maxima:** ontwerpen op het gemiddelde en door de staart worden opgeroepen.

## Volwassenheidsmodel

- **Niveau 1, Initiëren:** Wachtrijen (tickets, taken, berichten, deploys) zijn onbeheerd en reactief. Capaciteit wordt gegokt. Benutting draait waar de belasting landt. Latentieproblemen verrassen het team en worden achteraf geblust.
- **Niveau 2, Ontwikkelen:** Een paar teams verzamelen basisstatistieken (doorvoer, gemiddelde wachttijd) maar lezen ze als gemiddelden en passen ze inconsistent toe. Sommige groepen begrenzen WIP of laten ruimte terwijl andere heet draaien. Er is geen gedeelde notatie, dus de praktijken reizen niet over teams.
- **Niveau 3, Standaardiseren:** Een gemeenschappelijke notatie (λ, μ, ρ, doorlooptijd) is gedocumenteerd en organisatiebreed afgedwongen. WIP-limieten en benuttingsruimtedoelen zijn bewust gesteld voor elk latentiegevoelig systeem. De verschillende MTTR's worden onderscheiden. Begrensde wachtrijen met tegendruk zijn de standaard over services.
- **Niveau 4, Beheersen:** De wachtrijen worden gemeten en beheerst tegen uitgangswaarden: aankomstsnelheid, servicesnelheid, benutting, staartlatentie (p95/p99) en doorlooptijd worden gevolgd tegen gedefinieerde doelen en SLO's. Wachtrijdieptes, timeouts en ruimte worden afgeleid uit de wet van Little in plaats van gegokt. Balking, reneging en overslagsnelheid worden geteld zodat aangeboden belasting van bediende belasting wordt onderscheiden. Capaciteitsbeslissingen worden op dit bewijs beoordeeld, niet op gevoel.
- **Niveau 5, Orkestreren:** Flow wordt continu gemodelleerd als wachtrij van wachtrijen. Knelpunten worden geïdentificeerd en verlicht als doorlopende praktijk. Capaciteit, SLO's en tegendruk passen zich aan verschuivende vraag en variantie aan. Wachtrijstatistieken sluiten direct aan op DORA en bedrijfs-KPI's, en de organisatie herbalanceert capaciteit over de hele flow naarmate belasting en risicobeeld veranderen.

## Ideeën voor discussie

1. Op welke benutting draaien je latentiegevoelige systemen werkelijk, en waar ligt hun afgrond?
2. Pas de wet van Little toe op je huidige achterstand: welke doorlooptijd impliceert je WIP ÷ doorvoer, en komt dat overeen met de werkelijkheid?
3. Welke van je wachtrijen tellen stilletjes "overslagen" (verlatingen, afwijzingen) alsof ze bediend waren?
4. Waar zou WIP verlagen de doorlooptijd goedkoper verkorten dan capaciteit toevoegen?
5. Welke fase in je flow van idee naar productie is het echte knelpunt, en zijn je verbeteringen daar op gericht?
6. Tonen je dashboards gemiddelden waar de staart is wat je werkelijk pijn doet?

## Belangrijkste inzichten

- Klantwachtrijen, kanbanborden, berichtenwachtrijen en deploypijplijnen zijn allemaal wachtrijen bestuurd door dezelfde wetten.
- **De wet van Little (κ = λτ)** verankert flowplanning: doorlooptijd = WIP ÷ doorvoer.
- Benutting en wachttijd zijn **niet-lineair**: voorzie ruimte. De laatste 15% is de duurste.
- Volg het volledige beeld: aankomsten, service, successen, **falen en overslagen** en wachttijden. Laat verlating zich niet verbergen.
- Modelleer processen als **wachtrij van wachtrijen** en repareer het **knelpunt**, niet het drukwerk.
- Wachtrijstatistieken sluiten direct aan op **DORA-/flow-** en **SLI-/SLO**-maten (hoofdstuk 11.1, 11.2, 9.1), wat de hele organisatie één taal geeft voor capaciteit en flow.

## Referenties en verder lezen

- Bob Wescott, *Seven Insights into Queueing Theory* (and *The Every Computer Performance Book*).
- John D. C. Little, "A Proof for the Queuing Formula L = λW" (1961): Little's Law.
- Nicole Forsgren, Jez Humble, Gene Kim, *Accelerate*: flow-based DORA metrics that align with queue KPIs.
- Donald Reinertsen, *The Principles of Product Development Flow*: queues, batch size, and WIP economics.
- Daniel Vacanti, *Actionable Agile Metrics for Predictability*: Little's Law applied to kanban.
- Joel Parker Henderson, *Queueing Theory*: notation, KPIs, and queue-of-queues (github.com/joelparkerhenderson/queueing-theory).
- Dan Slimmon, "The most important thing to understand about queues" (2016).
- Wikipedia: "Queueing theory," "M/M/1 queue," "Little's law," "Markov chain."
