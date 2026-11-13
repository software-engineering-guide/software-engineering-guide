# 2.5 Codereview en samenwerking

## Overzicht en motivatie

[Codereview](https://en.wikipedia.org/wiki/Code_review) is de praktijk waarbij iemand anders dan de auteur een wijziging onderzoekt voordat die wordt samengevoegd. Het is een van de activiteiten met de hoogste hefboom voor kwaliteit en kennisdeling die een softwareorganisatie heeft, en voor grote teams is het ook een primair coördinatiemechanisme en cultuurdrager. Review vangt defecten op, verspreidt kennis van de codebase, handhaaft standaarden en begeleidt engineers, maar alleen wanneer je haar goed doet. Slecht gedaan wordt ze een knelpunt, een bron van wrijving of een stempel zonder inhoud die valse zekerheid geeft.

Voor grote teams is review waar individueel werk collectief eigenaarschap ontmoet. Het is vaak het belangrijkste contactpunt tussen engineers die anders voor zichzelf werken, dus haar normen bepalen hoe de hele organisatie samenwerkt. Review verspreidt kennis zodat geen enkel deel van het systeem door slechts één persoon wordt begrepen, wat het [busfactor](https://en.wikipedia.org/wiki/Bus_factor)-risico vermindert, het gevaar dat kennis bij te weinig mensen zit, dat grote, langlevende systemen plaagt. Het creëert ook een auditspoor van wie wat wijzigde en wie het goedkeurde.

In omgevingen van onderneming en overheid draagt review vaak een compliancedimensie. [Functiescheiding](https://en.wikipedia.org/wiki/Separation_of_duties) (niemand controleert alleen een volledige gevoelige wijziging), verplichte goedkeuringen en traceerbaarheid zijn vaak vereiste beheersmaatregelen. Een wijziging die gevoelige systemen raakt, kan review door specifieke rollen vereisen, en het reviewverslag wordt auditbewijs. Je uitdaging is aan deze controles te voldoen terwijl je review snel en opbouwend houdt, in plaats van haar tot ceremonie te maken.

## Kernprincipes

- Beoordeel om de wijziging te verbeteren en kennis te delen, niet om te pronken.
- Kleine wijzigingen krijgen betere reviews, dus houd pull requests (PR's) gefocust en redelijk van omvang.
- Reviewlatentie is een kost voor het hele team. Snelle doorlooptijd houdt iedereen in beweging.
- Automatiseer het mechanische (stijl, tests, beveiligingsscans) zodat mensen ontwerp en juistheid beoordelen.
- Scheid blokkerende problemen van suggesties en voorkeuren, en wees expliciet over welke welke is.
- Bekritiseer de code, niet de persoon. Feedbacknormen bepalen of review vertrouwen bouwt of corrodeert.
- De auteur is verantwoordelijk voor het makkelijk te beoordelen maken van een wijziging.

## Aanbevelingen

### Maak pull requests klein en goed beschreven

Houd elke wijziging gericht op één logische zorg en klein genoeg om zorgvuldig te beoordelen. Grote PR's krijgen oppervlakkige reviews. Geef een heldere beschrijving van wat er veranderde, waarom en hoe je het verifieerde, zodat de reviewer context heeft. Splits mechanische refactorings en gedragswijzigingen in aparte PR's, zodat elk makkelijk te doorgronden is. Een goede beschrijving is de belangrijkste bijdrage van de auteur aan de reviewkwaliteit.

### Stel reviewstandaarden en checklists vast

Maak duidelijk waar reviewers op moeten letten: juistheid, ontwerppasvorm, voldoende tests, beveiligingsimplicaties, leesbaarheid en naleving van standaarden. Een lichte checklist houdt reviews consistent en voorkomt dat belangrijke dimensies er doorheen glippen, zonder review tot afvinken te maken. Definieer wat review vereist, wie mag goedkeuren en welke rolgebonden goedkeuringen nodig zijn voor gevoelige gebieden.

### Stel normen voor reviewlatentie vast en bewaak ze

Spreek een doeldoorlooptijd af, bijvoorbeeld reageren binnen een werkdag, en maak review een volwaardig onderdeel van de dag in plaats van iets wat er als laatste tussen wordt geperst. Lange reviewwachtrijen leggen de oplevering stil en verleiden engineers tot te grote, gebundelde wijzigingen. Volg tijd tot eerste review en tijd tot samenvoegen, en behandel aanhoudende latentie als een procesprobleem om op te lossen, niet als een persoonlijke tekortkoming.

### Automatiseer alles wat mechanisch is

Draai opmaak, [linting](https://en.wikipedia.org/wiki/Lint_(software)), tests en beveiligings- en afhankelijkheidsscans in [continuous integration](https://en.wikipedia.org/wiki/Continuous_integration) (CI), zodat reviewers er nooit aandacht aan besteden. Bewaar menselijke review voor wat machines niet kunnen beoordelen: of het ontwerp klopt, of de aanpak bij het systeem past, of de tests betekenisvol zijn en of de code later nog steeds logisch zal zijn.

### Gebruik pair- en mobprogrammeren waar ze passen

Gebruik [pairprogrammeren](https://en.wikipedia.org/wiki/Pair_programming), waarbij twee engineers samen code schrijven aan één werkplek, voor complex of risicovol werk, onboarding en kennisoverdracht. Het is continue review en neemt vaak de behoefte aan een aparte reviewstap weg. Gebruik [mobprogrammeren](https://en.wikipedia.org/wiki/Mob_programming), waarbij het hele team tegelijk aan één taak werkt, voor kritieke ontwerpbeslissingen of om kennis van een lastig gebied over het team te verspreiden. Zie deze als aanvullingen op asynchrone review, gekozen naar context, niet als vervangingen die je overal oplegt.

### Neem geautomatiseerde en door AI ondersteunde review zorgvuldig aan

Gebruik geautomatiseerde reviewtools en AI-assistenten om veelvoorkomende problemen te vangen, verbeteringen voor te stellen en de last van de reviewer te verlichten, maar behandel hun uitvoer als input, niet als autoriteit. AI-review is goed in oppervlakkige problemen en consistentie, en slecht in diep ontwerpoordeel en systeemcontext. Houd een mens verantwoordelijk voor elke goedkeuring, vooral voor beveiligingsgevoelige en compliancerelevante wijzigingen.

### Stel constructieve feedbacknormen vast

Stel normen vast die feedback specifiek, vriendelijk en op de code gericht houden. Moedig reviewers aan vragen te stellen in plaats van bevelen te geven, de redenering achter een verzoek uit te leggen en goed werk te prijzen. Markeer blokkerende zorgen en optionele suggesties duidelijk (bijvoorbeeld door niet-blokkerende notities van een voorvoegsel te voorzien). Deze normen bepalen of review het team versterkt of wrok kweekt.

## Afwegingen: voor- en nadelen

| Aanpak | Voordelen | Nadelen |
|---|---|---|
| Asynchrone PR-review | Flexibel. Gedocumenteerd. Schaalt over tijdzones | Latentie. Verliest nuance. Kan vijandig aanvoelen |
| Pairprogrammeren | Continue review. Snelle kennisoverdracht. Hoge kwaliteit | Twee mensen aan één taak. Vermoeiend. Moeilijker te plannen |
| Mobprogrammeren | Afstemming van het hele team. Verspreidt diepe kennis | Duur in totaal. Niet voor routinewerk |
| Verplichte meerdere reviewers | Sterke zekerheid. Compliancevriendelijk | Trager. Verdunt verantwoordelijkheid. Wachtrijdruk |
| AI-ondersteunde review | Snel, onvermoeibaar bij veelvoorkomende problemen. Vermindert last | Mist systeemcontext. Vals vertrouwen bij overmatig vertrouwen |

De kernspanning is grondigheid tegenover snelheid. Diepere review vangt meer, maar vertraagt de oplevering en kan auteurs frustreren. Snellere review houdt de flow, maar riskeert oppervlakkig te zijn. De weg erdoorheen is reviewdiepte af te stemmen op wijzigingsrisico, zodat triviale wijzigingen een lichte review krijgen en riskante een diepe, en het mechanische werk weg te automatiseren zodat menselijke inspanning zich concentreert waar het ertoe doet.

## Vragen om met je team te bespreken

1. **Wat telt als te groot voor één pull request, en splits je mechanische refactorings van gedragswijzigingen?** Dit hoofdstuk stelt duidelijk dat grote PR's oppervlakkige reviews krijgen en dat de auteur de beoordeelbaarheid bezit, en het vraagt je refactorings van gedragswijzigingen te scheiden zodat elk makkelijk te doorgronden is. In een groot team garandeert een gigantische PR een afstempeling, wat valse zekerheid geeft terwijl echte defecten doorglippen. Neem het bewijs mee: je verdeling van PR-groottes en hoe de reviewdiepte daalt naarmate diffs groeien. Spreek een praktische groottenorm af en een gewoonte om zuivere refactorings apart van logicawijzigingen te laten landen, zodat een reviewer elke wijziging werkelijk in zijn hoofd kan houden. Die ene discipline tilt de kwaliteit van elke volgende review op.

2. **Hoe onderscheid je een blokkerend bezwaar van een optionele suggestie, en wordt die conventie daadwerkelijk gebruikt?** Het hoofdstuk vraagt je blokkerende problemen van voorkeuren te scheiden en expliciet te zijn over welke welke is, en markeert blokkeren op voorkeur als corrosief antipatroon. Zonder gedeelde conventie leest de stijlmening van een reviewer als een verplichte wijziging, wat wrok kweekt en de oplevering over het hele team vertraagt. Neem voorbeelden uit recente reviews mee waarin een voorkeur een samenvoeging stillegde als concreet signaal. Neem een lichte markering aan, bijvoorbeeld een voorvoegsel dat niet-blokkerende notities markeert, zodat auteurs onmiddellijk weten wat moet veranderen tegenover wat een suggestie is. Dat houdt review gericht op juistheid en ontwerp in plaats van smaak.

3. **Wie moet wijzigingen aan beveiligingsgevoelige of compliancerelevante code goedkeuren, en hoe wordt die routering afgedwongen?** Dit hoofdstuk beschrijft rolgebonden goedkeuringen, regels voor code-eigenaarschap en functiescheiding waarbij niemand alleen een volledige gevoelige wijziging controleert, met de goedkeuring vastgelegd als auditbewijs. In omgevingen van onderneming en overheid zijn dit vereiste beheersmaatregelen, en het risico is dat ze ofwel worden overgeslagen ofwel veranderen in een knelpunt dat de oplevering bevriest. Neem het signaal mee: welke modules gevoelig zijn en of eigenaarschapsregels die wijzigingen nu automatisch naar de juiste goedkeurders routeren. Codeer de routering in configuratie van code-eigenaarschap en koppel haar aan geautomatiseerde controles en kleine wijzigingen, zodat aan de beheersmaatregel wordt voldaan zonder een menselijke poortwachterwachtrij. Beslis dit bewust in plaats van de kloof tijdens een audit te ontdekken.

4. **Welk doel voor reviewlatentie heb je daadwerkelijk afgesproken, en meet en handhaaf je het, of is het slechts een aspiratie?** Het hoofdstuk behandelt reviewlatentie als een kost voor het hele team en vraagt je tijd tot eerste review en tijd tot samenvoegen te volgen, waarbij aanhoudende vertraging als procesprobleem wordt behandeld in plaats van een persoonlijke tekortkoming. In een groot team belast een eigenaarloze reviewwachtrij iedereen stilletjes: auteurs bundelen grotere wijzigingen om de wachttijd te vermijden, die wijzigingen krijgen dan oppervlakkiger reviews en de doorlooptijd van oplevering drijft omhoog zonder één enkele schuldige. De concurrerende overweging is dat een hard latentiedoel reviewers kan duwen tot vluchtig lezen, dus snelheid en diepgang moeten worden gebalanceerd in plaats van blind verhandeld. Neem het bewijs mee: je huidige verdeling van tijd tot eerste review, hoe die varieert per team en per wijzigingsgrootte en waar reviews het langst blijven liggen. Koppel in omgevingen van onderneming en overheid het doel aan de flowstatistieken die het bestuur al volgt, want een verplichte beheersmaatregel met meerdere reviewers zonder latentienorm wordt het knelpunt dat de oplevering bevriest en mensen verleidt de beheersmaatregel helemaal te omzeilen.

5. **Voor welke soorten wijziging vertrouw je op geautomatiseerde en door AI ondersteunde review, en waar moet een mens verantwoordelijk blijven?** Het hoofdstuk zegt de uitvoer van AI-review als input te behandelen, niet als autoriteit: sterk bij oppervlakkige problemen en consistentie, zwak bij diep ontwerpoordeel en systeemcontext, met een mens verantwoordelijk voor elke goedkeuring. Zonder expliciete grens drijft een groot team af naar overmatig vertrouwen, waarbij een groene botopmerking leest als een geslaagde review en echte ontwerp- en beveiligingsrisico's onder valse zekerheid doorglippen. De concurrerende trek is dat AI-review de last werkelijk verlicht en veelvoorkomende defecten onvermoeibaar vangt, dus haar verbieden verspilt hefboom. Neem het bewijs mee: waar geautomatiseerde suggesties echte problemen hebben gevangen, waar ze ruis hebben opgeleverd en welke wijzigingstypen (beveiligingsgevoelig, compliancerelevant, architectonisch) je nooit een machine alleen zou laten goedkeuren. Noem voor werk in onderneming en overheid wie de verantwoordelijkheid voor een goedkeuring draagt wanneer een AI-assistent in de lus zat, want een audit zal vragen wie een wijziging beoordeelde, en "de tool deed het" is geen antwoord dat een toezichthouder accepteert.

6. **Waar moeten pairing of mobbing asynchrone review vervangen, en hoe gebruik je review om het busfactorrisico bewust te verminderen?** Het hoofdstuk kadert pair- en mobprogrammeren als continue review gekozen naar context, en noemt review het mechanisme dat kennis verspreidt zodat geen deel van het systeem door slechts één persoon wordt begrepen. Impliciet gelaten concentreert kennis zich: dezelfde expert beoordeelt elke wijziging aan een subsysteem, review wordt een afstempeling omdat niemand anders hem kan uitdagen en het busfactorrisico groeit precies waar het systeem het meest kritiek is. De concurrerende overweging is kosten, want mobbing besteedt de tijd van het hele team en pairing bindt twee engineers, dus je kunt het niet overal verplichten. Neem het bewijs mee: welke modules slechts één geloofwaardige reviewer hebben, waar onboarding stokt en waar een lastig gebied baat zou hebben bij een live sessie boven opmerkingenthreads. Behandel in een grote of publieke organisatie bewuste kennisverspreiding als risicobeheer, omdat een langlevend systeem waarvan kritieke delen van één persoon afhangen een operationele en continuïteitsverplichting is, niet louter een personeelsongemak.

## Sectorperspectief

**Startup.** Met drie of vier engineers houd je review licht: de goedkeuring van één teamgenoot op een kleine pull request, mechanische controles in CI en geen verplichte tweede reviewer die een samenvoeging zou stilleggen. Het echte doel is minder compliance dan ervoor zorgen dat meer dan één persoon elk deel van het systeem begrijpt, dus pair op de riskante stukken en behandel dat als onboarding. Bouw geen zware routering van code-eigenaarschap waar je snel aan ontgroeit. Een gedeelde norm van kleine, goed beschreven wijzigingen koopt het grootste deel van het voordeel tegen vrijwel geen kosten.

**Kleinbedrijf.** Je hebt waarschijnlijk geen specialist voor reviewtooling, dus leun op wat je hostingplatform (bijvoorbeeld een beheerde Git-dienst) kant-en-klaar biedt in plaats van aangepaste automatisering te bouwen. Koop de integraties voor linting, tests en beveiligingsscans in plaats van ze te onderhouden, zodat je weinige engineers hun schaarse reviewminuten aan ontwerp en juistheid besteden. Houd één eenvoudige regel aan, elke wijziging krijgt één ander paar ogen, en weersta het toevoegen van proces dat je niemand hebt om te onderhouden.

**Grote onderneming.** De uitdaging is consistentie over veel teams: gedeelde standaarden, regels voor code-eigenaarschap die gevoelige wijzigingen naar de juiste goedkeurders routeren en rolgebonden goedkeuringen vastgelegd als auditbewijs. Automatiseer de mechanische controles organisatiebreed zodat menselijke review zich op ontwerp concentreert, en volg reviewlatentie als flowstatistiek zodat verplichte beheersmaatregelen met meerdere reviewers niet stilletjes knelpunten worden. Stem reviewdiepte af op wijzigingsrisico met een gedocumenteerd beleid, zodat triviale wijzigingen snel blijven terwijl riskante functiescheiding en diepere controle krijgen.

**Overheid.** Wijzigingsbeheer is vaak verplicht: elke productiewijziging beoordeeld en goedgekeurd door iemand anders dan de auteur, met het verslag bewaard als auditbewijs om aan eisen van functiescheiding te voldoen. Geef de voorkeur aan een transparant, traceerbaar spoor van wie schreef, wie goedkeurde en welke controles slaagden, en investeer in automatisering en kleine, frequente wijzigingen zodat de beheersmaatregel de oplevering niet bevriest. Eis waar reviewtooling wordt ingekocht exporteerbare auditlogs en vermijd lock-in, omdat het bewijs elke afzonderlijke leverancier moet overleven en publieke scrutinie moet doorstaan.

## Voorbeelden

**Startup.** Een startup van vier engineers houdt elke pull request klein en vraagt de goedkeuring van één teamgenoot vóór het samenvoegen, minder voor compliance dan om zeker te zijn dat niemand de enige is die een deel van het systeem begrijpt. CI draait de formatter en de tests, zodat de mensen hun weinige reviewminuten aan ontwerp en juistheid besteden in plaats van aan spaties. Wanneer het team een lastig stuk van de betalingsstroom raakt, pairen twee van hen eraan in plaats van asynchrone opmerkingen te wisselen, wat dient als onboarding voor de nieuwste aanwerving.

**Grote onderneming.** Een groot softwarebedrijf eist minstens één goedkeurende review op elke wijziging, plus een tweede goedkeuring voor wijzigingen aan beveiligingsgevoelige modules die zijn geïdentificeerd via regels voor code-eigenaarschap. CI handelt alle stijl- en testcontroles af, zodat reviewers zich op ontwerp en juistheid richten. Het team volgt tijd tot eerste review en behandelt een stijgende mediaan als signaal om de werklast te herbalanceren. Nieuwe engineers worden ingewerkt via pairing, wat hun pad naar zelfstandig bijdragen verkort.

**Overheid.** Een nationale dienst die onder strikte eisen voor wijzigingsbeheer opereert, verplicht dat elke productiewijziging wordt beoordeeld en goedgekeurd door iemand anders dan de auteur, met de goedkeuring vastgelegd voor audit. Om te voorkomen dat deze beheersmaatregel een knelpunt wordt, investeert de dienst in geautomatiseerde controles en kleine, frequente wijzigingen en stelt ze een norm in voor reageren op dezelfde dag. Het reviewspoor, met wie schreef, wie goedkeurde en welke controles slaagden, wordt onderdeel van het compliancebewijs voor elke release en voldoet aan de eisen van functiescheiding zonder de oplevering te bevriezen.

## Zakelijke onderbouwing: motivatie, ROI en TCO

Codereview betaalt zich terug in drie valuta's: defecten opgevangen vóór productie, kennis verspreid over het team en standaarden die in de loop van de tijd automatisch worden gehandhaafd. Een defect in review vangen is veel goedkoper dan het in productie vangen, en het kennisdelingsvoordeel vermindert sleutelpersoonrisico dat een organisatie anders duur kan komen te staan wanneer iemand vertrekt. Review is ook het culturele overdrachtsmechanisme dat een groeiend team samenhangend houdt.

De kosten van review zijn engineertijd en wat latentie, beide beheersbaar met goede praktijken. De kosten van *niet* beoordelen, of slecht beoordelen, omvatten productiedefecten, gesiloede kennis, inconsistente code en, in gereguleerde omgevingen, mislukte audits en compliancebevindingen. Te zware review heeft ook echte kosten: lange wachtrijen, te grote bundels, gedemotiveerde engineers. Verbind reviewpraktijken om het bestuur te overtuigen aan het faalpercentage van wijzigingen, de doorlooptijd van oplevering en de onboardingsnelheid, en volg reviewlatentie als expliciete flowstatistiek.

## Antipatronen en valkuilen

- **De afstempeling:** goedkeuringen zonder echt onderzoek, die valse zekerheid geven en alleen aan de letter van een beheersmaatregel voldoen.
- **De gigantische PR:** duizenden regels die alleen vluchtig kunnen worden gelezen, wat een oppervlakkige review garandeert.
- **Alleen muggenzifterij:** zich richten op trivia terwijl ontwerp en juistheid worden gemist, vaak omdat mechanische controles niet zijn geautomatiseerd.
- **Review als poortwachterschap:** review gebruiken om dominantie te laten gelden of anderen te blokkeren, wat samenwerking vergiftigt.
- **De trage wachtrij:** reviews die dagen blijven liggen, wat de oplevering stillegt en bundelen aanmoedigt.
- **Overmatig vertrouwen in AI-review:** geautomatiseerde suggesties als autoriteit behandelen en menselijk oordeel laten vallen bij riskante wijzigingen.
- **Blokkeren op voorkeur:** persoonlijke stijlmeningen presenteren als vereiste wijzigingen zonder ze te onderscheiden van echte defecten.

## Volwassenheidsmodel

- **Niveau 1, Initiëren:** Review is ad hoc en reactief. Ze wordt vaak overgeslagen of inconsistent gedaan, mechanische problemen domineren de opmerkingen, feedbacknormen zijn niet vastgesteld en elk goedkeuringsspoor is toevallig in plaats van bewust.
- **Niveau 2, Ontwikkelen:** Basisreviewpraktijken bestaan maar verschillen van team tot team. Review is op sommige plaatsen vereist en op andere traag of optioneel, automatisering is gedeeltelijk en de grootte en kwaliteit van pull requests schommelen sterk zonder gedeelde verwachting.
- **Niveau 3, Standaardiseren:** Standaarden zijn gedocumenteerd en organisatiebreed gehandhaafd. Kleine gerichte PR's, geautomatiseerde opmaak, linting, tests en beveiligingsscans in CI, heldere checklists, een expliciete conventie voor blokkerend tegenover suggestie en regels voor code-eigenaarschap die gevoelige wijzigingen naar de juiste goedkeurders routeren.
- **Niveau 4, Beheersen:** Review wordt gemeten en gestuurd aan de hand van uitgangswaarden. Tijd tot eerste review, tijd tot samenvoegen, reviewdiepte tegenover wijzigingsrisico, percentage ontsnapte defecten en faalpercentage van wijzigingen worden gevolgd. Aanhoudende latentie wordt behandeld als procesprobleem, en de data stuurt waar de reviewerlast moet worden herbalanceerd en waar beheersmaatregelen de oplevering vertragen zonder zekerheid toe te voegen.
- **Niveau 5, Orkestreren:** Review wordt continu verbeterd en is over de organisatie geïntegreerd. Diepte past zich aan het wijzigingsrisico aan, pairing, mobbing en AI-ondersteuning worden bewust gebruikt met een verantwoordelijke mens, kennisverspreiding en busfactorrisico worden doelbewust beheerd, en review verbetert meetbaar kwaliteit, leveringsflow en onboarding.

## Ideeën voor discussie

- Wat is het juiste doel voor reviewlatentie voor jouw team, en wat weerhoudt je ervan het te halen?
- Hoe stem je reviewdiepte af op wijzigingsrisico zonder bureaucratie toe te voegen?
- Waar overtreffen pairing of mobbing asynchrone review in jouw context?
- Hoeveel moet AI-ondersteunde review worden vertrouwd, en voor welke soorten wijzigingen?
- Hoe houd je reviewfeedback opbouwend naarmate het team groeit en diverser wordt?
- Hoe voldoe je aan compliance-eisen voor goedkeuring zonder knelpunten te creëren?

## Belangrijkste inzichten

- Houd pull requests klein en goed beschreven. De auteur bezit de beoordeelbaarheid.
- Automatiseer het mechanische zodat mensen ontwerp, juistheid en tests beoordelen.
- Volg en beheer reviewlatentie als een flowkost voor het hele team.
- Stem reviewdiepte af op wijzigingsrisico en onderscheid blokkerende problemen van voorkeuren.
- Gebruik pairing, mobbing en AI-ondersteuning als aanvullingen die bij de context passen, met een verantwoordelijke mens.

## Referenties en verder lezen

- Karl Wiegers, *Peer Reviews in Software: A Practical Guide*
- Google, *Engineering Practices: How to Do a Code Review* (as a reference exemplar)
- Nicole Forsgren, Jez Humble, Gene Kim, *Accelerate: The Science of Lean Software and DevOps*
- Kent Beck, *Extreme Programming Explained* (on pair programming)
- Woody Zuill, writings on mob programming
- Michael Lopp, *Managing Humans* (on engineering collaboration)
