# 10.7 Agile

## Overzicht en motivatie

[Agile](https://en.wikipedia.org/wiki/Agile_software_development) is een mindset om software (en waarde) iteratief, incrementeel en in nauwe samenwerking te leveren met de mensen die haar zullen gebruiken. Gecodificeerd in het *Manifesto for Agile Software Development* van 2001 wordt ze het best begrepen niet als proces maar als een set **waarden en principes**: stel individuen en interacties, werkende software, samenwerking met de klant en reageren op verandering boven de plan-zware, contract-zware, documentatie-zware standaarden die eraan voorafgingen. Kaders als [Scrum](https://en.wikipedia.org/wiki/Scrum_(software_development)), [Kanban](https://en.wikipedia.org/wiki/Kanban_(development)) en [Extreme Programming](https://en.wikipedia.org/wiki/Extreme_programming) (XP) zijn *implementaties* van die mindset. Het zijn nuttige beginpunten, maar niet de mindset zelf. Dit hoofdstuk vult hoofdstuk 1.4 aan (werkwijzen, dat methoden breed overziet) door diep op Agile in het bijzonder in te gaan.

Agile wordt gedreven door dezelfde kracht die de discovery- en leveringspijplijnen bezielt (hoofdstuk 11.1–11.2): eisen voor software worden *ontdekt*, niet vooraf volledig gekend, en de wereld verandert sneller dan een lang plan kan absorberen. Big-bang, eerst-alles-plannen-oplevering produceert herhaaldelijk systemen die te laat zijn, boven budget en, het ergste, fout, omdat al het leren aan het eind arriveert, wanneer het het duurst is erop te handelen. De kernweddenschap van Agile is eenvoudig: korte cycli van echte, werkende software bouwen en echte feedback krijgen verslaat lange cycli van speculatie. Goed gedaan vermindert ze risico continu in plaats van het uit te stellen.

Voor grote teams, onderneming en overheid is Agile zowel krachtig als vaak verminkt. Ondernemingen nemen haar over honderden teams over en reduceren haar vaak tot ritueel ("we doen nu stand-ups") zonder te veranderen hoe beslissingen worden genomen of hoe waarde wordt gemeten. De overheid heeft Agile bewust omarmd, omdat iteratieve, gebruikersgerichte oplevering aantoonbaar het risico van grote publieke programma's vermindert: de U.S. Digital Service en haar *Digital Services Playbook*, de Britse Government Digital Service en Service Standard en agile aanbestedingshervormingen ontstonden deels als reactie op opzienbarende [waterval](https://en.wikipedia.org/wiki/Waterfall_model)mislukkingen. De prijs is echt. Dat is ook de faalwijze van "agile in naam alleen."

## Kernprincipes

- **Waardeer de vier waarden van het Manifesto** (mensen, werkende software, samenwerking en responsiviteit) boven procesartefacten.
- **Lever vaak werkende software** in kleine increments. Werkende software is de primaire maat van voortgang.
- **Verwelkom verandering**, zelfs laat. Aanpasbaarheid is een functie, geen falen.
- **Bouw rond gemotiveerde, bekrachtigde, zelforganiserende teams.**
- **Werk continu samen met gebruikers en belanghebbenden.**
- **Reflecteer en verbeter** volgens een regulier ritme.
- **Houd een humaan tempo vol** en technische uitmuntendheid: snelheid zonder vakmanschap stort in.

## Aanbevelingen

### Veranker op waarden en principes, niet ceremonies

De allerbelangrijkste Agile-aanbeveling is te leiden met het *waarom*. Een team dat een dagelijkse stand-up, een sprintreview en een retrospective houdt, maar zich nog steeds op vaste reikwijdte op een vaste datum committeert, slecht nieuws verbergt en het plan nooit verandert, is niet agile. Het is waterval met vergaderingen. Gebruik de twaalf principes als checklist voor echte wendbaarheid. Lever je vaak werkende software? Kun je een verandering volgende iteratie verwelkomen? Beslist het team *hoe* het werk wordt gedaan? Zit de klant werkelijk in de lus? Als de ceremonies die uitkomsten niet produceren, repareer dan de uitkomsten, niet de ceremonies.

### Kies een kader als beginpunt, niet als religie

Kies een kader dat bij het werk past en pas het aan:

- **Scrum:** sprints met vaste tijdsduur, een geprioriteerde achterstand en gedefinieerde rollen (productowner, scrummaster, ontwikkelaars). Goed voor functielevering met een heldere productowner. Zwak wanneer werk sterk door onderbrekingen wordt gedreven.
- **Kanban:** continue flow met expliciete limieten op werk in uitvoering en een pull-systeem. Goed voor ondersteuning, beheer en onvoorspelbare aanvoer (en direct gegrond in flow- en wachtrijtheorie, zie hoofdstuk 11.2, 11.3). WIP beperken verkort de doorlooptijd ([de wet van Little](https://en.wikipedia.org/wiki/Little%27s_law)).
- **Extreme Programming (XP):** engineeringpraktijken waaronder [testgedreven ontwikkeling](https://en.wikipedia.org/wiki/Test-driven_development), [pairprogrammeren](https://en.wikipedia.org/wiki/Pair_programming), [continuous integration](https://en.wikipedia.org/wiki/Continuous_integration), refactoring en kleine releases. De technische ruggengraat die elk kader houdbaar maakt.
- **Scrumban** en mengvormen: pragmatische combinaties waar veel volwassen teams op uitkomen.

Kaders zijn steigerwerk. Houd wat helpt, laat vallen wat niet helpt en laat "het kader zegt het" nooit "de principes zeggen waarom" overrulen.

### Sta op technische uitmuntendheid

Agile zonder engineeringdiscipline degradeert snel tot snelle productie van ononderhoudbare code, "dark scrum," waar teams zichzelf in een teerput van defecten en [technische schuld](https://en.wikipedia.org/wiki/Technical_debt) sprinten. De XP-praktijken zijn geen optionele extra's. Continuous integration (hoofdstuk 8.1), geautomatiseerd testen (hoofdstuk 2.4), refactoring, trunk-based development (hoofdstuk 2.6) en schoon ontwerp (hoofdstuk 2.2) zijn wat een team software goedkoop kan laten blijven veranderen, wat het hele uitgangspunt van wendbaarheid is. Houdbaar tempo telt om dezelfde reden: opgebrande teams kunnen kwaliteit of responsiviteit niet volhouden.

### Schaal met zorg, en geef de voorkeur aan afschalen

Opschalingskaders, zoals SAFe (het Scaled Agile Framework), LeSS, Nexus en Scrum@Scale, coördineren veel teams richting gedeelde doelen. Ze kunnen helpen, maar ze dragen een waarschuwing (in navolging van hoofdstuk 1.4): zware opschalingskaders voeren vaak juist de commando-en-controle, plan-zware overhead opnieuw in die Agile moest verwijderen. Probeer *afschalen* voordat je een groot kader overneemt. Organiseer rond onafhankelijke, stroomgerichte teams met helder eigenaarschap en minimale afhankelijkheden tussen teams (hoofdstuk 1.2), zodat je om te beginnen minder coördinatiemachinerie nodig hebt. Voeg waar coördinatie werkelijk nodig is de lichtste structuur toe die werkt, en verbind haar aan uitkomsten (OKR's, objectives and key results, hoofdstuk 11.1), niet output.

### Maak wendbaarheid echt in onderneming en overheid

Adaptieve oplevering en institutionele beperkingen kunnen samen bestaan, maar het vraagt bewust ontwerp:

- **Hybride governance:** een adaptieve leveringskern binnen een voorspellende financierings-/complianceschil (hoofdstuk 10.6), zodat iteratie toezicht bevredigt in plaats van ermee te vechten.
- **Agile aanbesteding:** modulaire, op uitkomsten gebaseerde contracten en kortere increments in plaats van één megacontract met vaste reikwijdte. Dit is waar Agile in de publieke sector het vaakst slaagt of faalt.
- **Compliance onderweg:** bouw audit, toegankelijkheid (hoofdstuk 5.3) en beveiliging (hoofdstuk 4.1) in de increment via automatisering en fitnessfuncties (geautomatiseerde controles die architecturale en kwaliteitseigenschappen continu verifiëren; hoofdstuk 8.5, 1.6), niet een late poort.
- **Echte gebruikerstoegang:** het moeilijkste en belangrijkste. Teams hebben echt contact met burgers of klanten nodig, wat aanbestedings- en beveiligingsregels vaak belemmeren.

### Verbeter continu, en meen het

De retrospective is de motor van verbetering van Agile, en ze is waardeloos als ze geen verandering oplevert. Draai retrospectives die een klein aantal concrete, bezeten acties genereren, en voltooi ze werkelijk vóór de volgende. Meet uitkomsten (verschoof de verandering een key result? zie hoofdstuk 11.1) en flow (krimpen doorlooptijden? zie hoofdstuk 11.2, 11.3). Meet geen velocity: het is een capaciteitssignaal dat een leugen wordt op het moment dat je het als productiviteitsdoel gebruikt.

## Afwegingen: voor- en nadelen

| Beslissing | Voordelen | Nadelen |
|---|---|---|
| **Agile (adaptief)** | Snelle feedback. Absorbeert verandering. Vroege, continue waarde | Moeilijker reikwijdte/kosten vooraf vast te leggen. Vraagt betrokken klant en discipline |
| **Waterval (voorspellend)** | Voorspelbare reikwijdte. Vriendelijk voor contract/audit | Late feedback. Big-bangrisico. Slechte pasvorm bij onzekere eisen |
| **Scrum** | Ritme, rollen, focus. Breed begrepen | Ceremonie-overhead. Worstelt met door onderbrekingen gedreven werk |
| **Kanban** | Flow, WIP-limieten, flexibel. Geweldig voor beheer | Minder structuur. Vraagt discipline om limieten te houden |
| **Zware opschaling (SAFe)** | Coördineert veel teams. Vertrouwd voor grote organisaties | Kan commando-en-controle opnieuw invoeren. Ceremoniezwaar |
| **Afschalen / teamautonomie** | Minder coördinatie-overhead. Snellere teams | Vraagt lage koppeling en sterk platform/eigenaarschap |

De bepalende spanning is **aanpasbaarheid tegenover voorspelbaarheid**, en de klassieke misvatting is dat Agile "geen plan" betekent. Dat doet ze niet. Ze betekent continu plannen en je committeren aan *uitkomsten en ritme* terwijl je *reikwijdte* laat meebuigen. De andere terugkerende valkuil is Agile behandelen als *alleen* proces (ceremonies) of *alleen* engineering (XP). Ze vraagt beide.

## Vragen om met je team te bespreken

1. **Zijn je contracten in jouw onderneming of overheidscontext modulair en op uitkomsten gebaseerd, of zit oplevering opgesloten in één megacontract met vaste reikwijdte?** Agile aanbesteding is waar publieke-sectorwendbaarheid het vaakst slaagt of faalt, omdat één contract met vaste prijs en vaste reikwijdte waterval afdwingt hoe de leveringsteams hun vergaderingen ook noemen. Modulaire, op uitkomsten gebaseerde contracten met kortere increments laten reikwijdte meebuigen tot een waardevolle kern binnen vaste financiering, precies het patroon achter moderne publieke successen en het tegengif voor eerdere big-bangmislukkingen. Neem bewijs mee: kijk naar je huidige contracten en vraag of een leverancier wordt betaald voor aangetoonde werkende software of voor een vaste reikwijdte die jaren geleden is goedgekeurd. Het antwoord moet veel meer bepalen hoe je de volgende aanbesteding structureert dan welk kader je teams intern aannemen. Je kunt niet adaptief zijn in oplevering terwijl je contract een verre, alles-of-niets go-live voorschrijft.

2. **Zijn audit, toegankelijkheid en beveiliging via automatisering in elke increment ingebouwd, of achteraf vastgeschroefd als late poort?** Compliance onderweg is wat adaptieve oplevering naast institutionele beperkingen laat bestaan: bouw de controles in de increment via automatisering en fitnessfuncties in plaats van ze te bewaren voor een wedloop vóór de release. Een late compliancepoort voert het big-bangrisico opnieuw in dat Agile moet verwijderen, omdat de dure problemen aan het eind boven water komen wanneer ze het moeilijkst te repareren zijn. Neem bewijs mee: controleer voor je laatste increment of toegankelijkheid, beveiliging en auditbewijs automatisch in de pijplijn werden geverifieerd of werden uitgesteld naar een handmatige review vóór de lancering. Het antwoord moet deze eigenschappen naar continue geautomatiseerde controles duwen, zodat toezicht wordt bevredigd door het bouwen zelf in plaats van door een aparte fase. Dit houdt een gereguleerd programma ook eerlijk tussen audits in plaats van alleen in de weken ervoor.

3. **Hoe zou je weten of je teams in technische schuld sprinten, en wat beschermt een houdbaar tempo onder lanceringsdruk?** Agile zonder engineeringdiscipline degradeert tot dark scrum, waar teams snel in een teerput van defecten en ononderhoudbare code sprinten, en opgebrande teams kwaliteit of responsiviteit niet kunnen volhouden. De XP-praktijken (continuous integration, geautomatiseerd testen, refactoring, trunk-based development) zijn wat een team software goedkoop kan laten blijven veranderen, het hele uitgangspunt van wendbaarheid, dus ze zijn geen optionele extra's om weg te ruilen wanneer een datum dreigt. Neem bewijs mee: volg of doorlooptijden krimpen of groeien, of defectpercentages stijgen en of het team stilletjes langere uren werkt om elke sprint te halen. Het antwoord moet technische uitmuntendheid en humaan tempo onbetwistbaar maken, omdat snelheid gekocht door vakmanschap op te offeren binnen een paar iteraties instort. Meet flow en uitkomsten, nooit velocity als doel, want op het moment dat je van een capaciteitssignaal een productiviteitsdoel maakt wordt het een leugen.

4. **Heb je, voordat je naar een zwaar opschalingskader grijpt, geprobeerd de afhankelijkheden tussen teams te verminderen die de behoefte aan coördinatie om te beginnen creëren?** Dit telt het meest voor een grote organisatie, omdat de reflex wanneer veel teams samen moeten uitleveren is een kader als SAFe, LeSS of Scrum@Scale te kopen, en zware opschalingsmachinerie smokkelt vaak de commando-en-controle, plan-zware overhead terug die Agile moet verwijderen. De concurrerende overweging is echt: sommige coördinatie is werkelijk vereist, en afschalen naar onafhankelijke, stroomgerichte teams vraagt lage koppeling, helder eigenaarschap en een platform dat volwassen genoeg is om teams self-service te laten doen, wat je mogelijk nog niet hebt. Neem bewijs mee naar de discussie: breng de werkelijke afhankelijkheden in kaart die teams op elkaar laten wachten en vraag hoeveel er een bewuste herontwerp van teamgrenzen en service-eigenaarschap zouden overleven. In programma's van onderneming en overheid, waar een organigram van tientallen teams gangbaar is, is de eerlijke vraag of je coördinatiestructuur toevoegt om te compenseren voor een architectuur en teamontwerp dat je in plaats daarvan kon vereenvoudigen, zodat je helemaal minder coördinatie nodig hebt.

5. **Hebben je teams echt, herhaald contact met de burgers of klanten voor wie ze bouwen, of arriveert feedback gefilterd via proxy's?** Samenwerking met de klant is een van de vier waarden van het Manifesto, en iteraties zonder echt gebruikerscontact optimaliseren stilletjes het verkeerde, de duurste faling die Agile moet voorkomen. De spanning is dat directe toegang op schaal moeilijk te regelen is en vaak wordt belemmerd door juist de aanbestedings-, privacy- en beveiligingsregels waaraan grote en publieke organisaties moeten voldoen, dus het makkelijke pad is een proxy te substitueren: een businessanalist, een belanghebbendencomité of de onderzoeksdeck van vorig kwartaal. Neem bewijs mee: tel voor je laatste paar increments hoeveel werden gevalideerd met een echte gebruiker die de software werkelijk gebruikte, en hoeveel rustten op iemands mening over wat gebruikers willen. Voeg voor een overheidsdienst toe of je usabilitytesten de meest geraakte mensen bereikten, inclusief gebruikers van hulptechnologie en mensen met weinig digitaal vertrouwen, want een publieke dienst die alleen werkt voor de zelfverzekerde meerderheid heeft haar verantwoordingsplicht gefaald ook als elke ceremonie volgens schema liep.

6. **Worden je teams gefinancierd en bestuurd rond uitkomsten en ritme, of rond een vaste reikwijdte die stilletjes waterval achter de ceremonies afdwingt?** Dit is het verschil tussen echte wendbaarheid en nep-agile, en het wordt boven het team beslist, in hoe geld wordt vrijgegeven en hoe succes wordt gerapporteerd, niet in of stand-ups plaatsvinden. De concurrerende trek is dat financiën-, portfolio- en toezichtsfuncties zijn gebouwd om een vaste reikwijdte tegen een vast budget jaren vooruit goed te keuren, en hen vragen een uitkomst met flexibele reikwijdte te financieren voelt als een verlies van controle waartegen ze zich zullen verzetten. Neem bewijs mee: volg hoe een huidig initiatief werd gefinancierd en waarop het rapporteert, en controleer of teams worden gemeten op opgeleverde uitkomsten en flow of op storypoints en naleving van een lang geleden goedgekeurde reikwijdte. Koppel dit in omgevingen van onderneming en overheid direct aan de financierings- en complianceschil (hoofdstuk 10.6): als het geld is gecommitteerd aan een verre, alles-of-niets go-live, kunnen de teams niet adaptief zijn hoe trouw ze de rituelen ook uitvoeren, en de oplossing hoort bij het governancemodel in plaats van bij de leveringsteams.

## Sectorperspectief

**Startup.** Leef de waarden en sla het kaderdebat over. Lever elke week een werkende plak aan echte gebruikers, zit dicht genoeg bij oprichters en vroege klanten dat feedback dagelijks arriveert en verwelkom een koerswijziging op het moment dat bewijs zegt dat de huidige weddenschap fout is. Je schaarste middel is engineeringaandacht, dus bescherm technische uitmuntendheid (continuous integration, geautomatiseerde tests, trunk-based development) zelfs onder lanceringsdruk, want die discipline is wat je volgende week goedkoop laat pivoteren.

**Kleinbedrijf.** Zonder agile coach en met een krap budget behandel je Agile als een handvol gewoonten in plaats van een transformatieprogramma dat je bemant: een korte wekelijkse cyclus, een zichtbaar bord met limieten op werk in uitvoering en elke week één concrete verbetering die je werkelijk afmaakt. Leun op Kanban, dat weinig ceremonie nodig heeft en past bij door onderbrekingen gedreven werk, en neem de praktijken over die zijn ingebed in de tools die je al koopt in plaats van een zwaar proces op te zetten. Beoordeel de inspanning op of je vaker nuttige software aan klanten uitlevert, niet op hoe nauw je Scrum nabootst.

**Grote onderneming.** Het probleem is veel teams coördineren zonder commando-en-controle opnieuw in te voeren. Geef de voorkeur aan afschalen, dat wil zeggen afhankelijkheden tussen teams verminderen door stroomgericht teamontwerp en een solide platform, voordat je een zwaar opschalingskader overneemt. Financier en bestuur rond uitkomsten (OKR's) en ritme in plaats van vaste jaarlijkse reikwijdte en storypoints, maak engineeringpraktijken in XP-stijl onbetwistbaar over teams en beheer oplevering als portfolio met flowstatistieken en uitkomstmaten zodat groepen verbeteren op bewijs in plaats van ritueel.

**Overheid.** Aanbestedingsregels, transparantie en publieke verantwoording geven elke keuze vorm. Structureer modulaire, op uitkomsten gebaseerde contracten met kortere increments in plaats van één megacontract met vaste reikwijdte, aangezien agile aanbesteding is waar Agile in de publieke sector het vaakst slaagt of faalt. Bouw audit, toegankelijkheid en beveiliging via automatisering in elke increment zodat toezicht wordt bevredigd door het bouwen zelf, publiceer voortgang en bewijs van publieke waarde aan toezichtsorganen en vecht voor echte toegang tot burgers (inclusief gebruikers van hulptechnologie) elke iteratie, omdat het de beperking is die het vaakst wordt weggeonderhandeld.

## Voorbeelden

**Startup.** Een startup van vijf personen slaat het ceremoniedebat over en leeft de Agile-waarden direct. Ze levert elke week een werkende plak aan echte gebruikers, zit dicht genoeg bij oprichters en vroege klanten dat feedback dagelijks arriveert en verwelkomt volgende week een koerswijziging wanneer het bewijs zegt dat de huidige weddenschap fout is. Het team weigert technische uitmuntendheid voor snelheid weg te ruilen, dus continuous integration, geautomatiseerde tests en trunk-based development zijn onbetwistbaar zelfs onder lanceringsdruk, en elke vrijdagretrospective produceert één concrete verandering die het team werkelijk afmaakt vóór de volgende. Ze volgt velocity nooit als doel en meet in plaats daarvan of opgeleverd werk de activatie bewoog en of doorlooptijden krimpen.

**Grote onderneming.** De transformatie van 60 teams van een telecombedrijf "doet Scrum" aanvankelijk maar ziet geen verbetering. Teams ontvangen nog steeds vaste jaarlijkse reikwijdte en rapporteren op velocity. Een reset richt zich opnieuw op principes: kwartaal-OKR's vervangen functiemandaten, teams worden herorganiseerd om afhankelijkheden tussen teams te verminderen (afschalen) en XP-praktijken (CI, TDD, trunk-based development) worden onbetwistbaar gemaakt. Doorlooptijden dalen, defecten nemen af en, cruciaal, het bedrijf begint uitkomsten te meten in plaats van storypoints, wat Agile-oplevering verbindt met de discoverypijplijn (hoofdstuk 11.1).

**Overheid.** Een digitaledienstteam herbouwt een burgergerichte uitkeringsapplicatie met Agile binnen een hybride governanceschil: increments van twee weken die werkende, door gebruikers geteste software opleveren, toegankelijkheid en beveiliging ingebouwd in elke increment en modulaire aanbesteding die een enkel contract met vaste prijs vervangt. Echt usabilitytesten met burgers (inclusief gebruikers van hulptechnologie) elke iteratie vangt problemen die het oude watervalproces zou hebben uitgeleverd. Het programma levert vroeg een bruikbare dienst en toont meetbare publieke waarde aan toezichtsorganen. Dit is het patroon achter moderne publieke successen, en het tegengif voor eerdere big-bangmislukkingen.

## Zakelijke onderbouwing: motivatie, ROI en TCO

Het rendement van Agile komt uit **risicovermindering en snellere waardeverwezenlijking**. Door vroeg en vaak werkende software te leveren zetten teams onzekerheid continu om in bewijs en vangen ze verkeerd-ding- en werkt-niet-falen terwijl ze goedkoop zijn, in plaats van bij een verre, dure go-live. Het onderzoek achter moderne oplevering (de bevindingen van DORA, [DevOps Research and Assessment](https://en.wikipedia.org/wiki/DevOps_Research_and_Assessment), in hoofdstuk 11.2) toont dat de praktijken die Agile bevordert (kleine batches, frequente releases, snelle feedback, technische uitmuntendheid) correleren met betere oplevering *en* stabiliteit *en* organisatieprestaties. Vroege increments beginnen ook eerder waarde terug te geven, wat de timing en totale omvang van ROI verbetert tegenover een big-bangrelease die tot het eind niets terugbrengt.

Op **[total cost of ownership](https://en.wikipedia.org/wiki/Total_cost_of_ownership)** verlaagt Agile de kosten van verandering over de levensduur van een systeem, mits de engineeringdiscipline echt is. Haar dominante risico is *nep-agile*: ceremonie zonder principe of vakmanschap, die vergaderoverhead toevoegt terwijl ze geen van de voordelen levert, en erger kan zijn dan een eerlijke waterval. Dus de businesscase is voorwaardelijk. Het rendement is hoog wanneer je Agile aanneemt als mindset-plus-engineering, en ruwweg nul (of negatief) wanneer je haar aanneemt als ritueel. Maak de zaak voor leiderschap door Agile te formuleren als continue risicovermindering en uitkomstmeting, niet als "sneller gaan," en erop te staan dat de investering technische praktijken omvat, niet alleen nieuwe vergaderingen.

## Antipatronen en valkuilen

- **Nep-/cargocult-agile:** ceremonies uitgevoerd terwijl beslissingen, financiering en mindset waterval blijven.
- **Velocity als productiviteit:** een capaciteitsschatting omzetten in een doel, wat haar corrumpeert ([de wet van Goodhart](https://en.wikipedia.org/wiki/Goodhart%27s_law)).
- **Dark scrum:** sprinten zonder technische uitmuntendheid naar ononderhoudbare, defectrijke code.
- **Retrospectives zonder verandering:** reflectie die geen voltooide acties oplevert.
- **Vaste reikwijdte *en* datum *en* kosten:** het agile noemen terwijl kwaliteit stilletjes de druk absorbeert.
- **Afwezige klant:** geen echte gebruikersfeedback, dus iteraties optimaliseren het verkeerde.
- **Kaderaanbidding:** "SAFe/Scrum zegt het" dat de principes en het oordeel van het team overrulet.
- **Opschalen vóór afschalen:** zware coördinatiekaders toevoegen in plaats van afhankelijkheden te verminderen.

## Volwassenheidsmodel

- **Niveau 1, Initiëren.** Waterval of ad hoc oplevering. Big-bangreleases. Werk is reactief en plan-zwaar, zonder iteratieve feedback en zonder gedeeld gevoel waarom Agile zou kunnen helpen.
- **Niveau 2, Ontwikkelen.** Een paar teams nemen Agile-ceremonies over (stand-ups, sprints, retrospectives), maar de praktijk is inconsistent over de organisatie: mindset en engineeringdiscipline lopen achter op de rituelen, velocity wordt als output behandeld en reikwijdte ligt nog vooraf vast.
- **Niveau 3, Standaardiseren.** Waarden en principes sturen werk werkelijk organisatiebreed, gedocumenteerd en van elk team verwacht: technische uitmuntendheid in XP-stijl (CI, geautomatiseerd testen, refactoring, trunk-based development) is standaardpraktijk, teams organiseren zichzelf, klanten zijn elke iteratie betrokken en retrospectives produceren concrete, voltooide verandering.
- **Niveau 4, Beheersen.** Oplevering wordt gemeten en beheerst tegen uitgangswaarden: teams volgen doorlooptijd, deploymentfrequentie, wijzigingsfaalpercentage en defectontsnappingspercentage (de flow- en stabiliteitsstatistieken in DORA-stijl), naast uitkomstmaten gekoppeld aan key results, en vergelijken elk met een bekende uitgangswaarde. Retrospectiveacties worden tot voltooiing gevolgd, signalen van houdbaar tempo zoals overwerk en burn-out worden bewaakt en velocity wordt nooit als productiviteitsdoel gebruikt. Go/no-go-beslissingen rusten op dit bewijs in plaats van op mening.
- **Niveau 5, Orkestreren.** Adaptieve oplevering is geïntegreerd met bedrijfs- en risicoplanning over de organisatie: uitkomsten (OKR's) drijven financiering en ritme, teamontwerp met lage afhankelijkheid (afschalen) minimaliseert coördinatie-overhead en hybride governance bevredigt toezicht zonder oplevering te vertragen. Continue verbetering is cultureel in plaats van ceremonieel, en de organisatie bakent haar portfolio routinematig opnieuw af, herteamt en herbalanceert naarmate bewijs en het risicobeeld verschuiven.

## Ideeën voor discussie

1. Beoordeel je team tegen de twaalf Agile-principes: waar ben je agile in ceremonie maar niet in inhoud?
2. Wordt velocity in je team gebruikt als voorspelling of als doel, en wat heeft dat met gedrag gedaan?
3. Welke technische XP-praktijken ontbreken, en hoe verschijnt hun afwezigheid als defecten of trage verandering?
4. Zou je, voordat je een opschalingskader overneemt, afhankelijkheden tussen teams kunnen verminderen?
5. Wat blokkeert in jouw context specifiek echte gebruikerstoegang elke iteratie, en hoe kon je dat verwijderen?
6. Wat was de laatste concrete verandering die een retrospective werkelijk opleverde?

## Belangrijkste inzichten

- Agile is een **mindset van waarden en principes**, geen set ceremonies. Kaders zijn beginpunten, niet het doel.
- Lever **vaak werkende software**, verwelkom verandering en bekrachtig **zelforganiserende teams**.
- **Technische uitmuntendheid (XP-praktijken) is onbetwistbaar.** Wendbaarheid zonder haar wordt snel verval.
- **Schaal met zorg. Geef de voorkeur aan afschalen.** Verminder afhankelijkheden voordat je coördinatiekaders toevoegt.
- Combineer in onderneming/overheid **adaptieve oplevering met hybride governance en agile aanbesteding**, en vecht voor echte gebruikerstoegang.
- Het rendement is **continue risicovermindering en eerdere waarde**, maar alleen wanneer Agile echt is, niet ritueel. Zie hoofdstuk 1.4, 11.1, 11.2, 10.6 en 11.3.

## Referenties en verder lezen

- Kent Beck et al., *Manifesto for Agile Software Development* and its twelve principles (agilemanifesto.org, 2001).
- Ken Schwaber and Jeff Sutherland, *The Scrum Guide*.
- Kent Beck, *Extreme Programming Explained: Embrace Change*.
- David J. Anderson, *Kanban: Successful Evolutionary Change for Your Technology Business*.
- Mike Cohn, *User Stories Applied* and *Succeeding with Agile*.
- Jeff Patton, *User Story Mapping*.
- Stephen Denning, *The Age of Agile*.
- Matthew Skelton and Manuel Pais, *Team Topologies* (team design and descaling).
- Nicole Forsgren, Jez Humble, Gene Kim, *Accelerate* (evidence for agile/DevOps practices).
- U.S. Digital Service, *Digital Services Playbook*; UK Government, *Government Service Standard*.
