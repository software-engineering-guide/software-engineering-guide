# 5.6 Frontend-engineering

## Overzicht en motivatie

Frontend-engineering is de discipline van de klantgerichte laag van software bouwen: de code die in de browser of op het apparaat draait en ontwerpen, content en data omzet in een werkende interface. Ze omvat keuzes voor framework en architectuur, renderstrategie, statusbeheer, prestaties en veerkracht over de enorme diversiteit aan browsers, apparaten en netwerkomstandigheden in de echte wereld. De frontend is waar al het werk stroomopwaarts (UX, ontwerp, content, toegankelijkheid, internationalisering) de gebruiker succesvol bereikt of uiteenvalt.

Voor grote teams is de frontend bijzonder uitdagend, omdat ze is blootgesteld aan een omgeving die de organisatie niet beheert. De browsers, apparaten, verbindingen en instellingen van gebruikers verschillen enorm, en het platform (het web) evolueert continu. Op schaal stapelen architectuurkeuzes zich op. Een framework dat vandaag wordt gekozen beperkt jarenlang het aannemen van personeel, de prestaties en de onderhoudbaarheid, en duizenden kleine beslissingen over bundelgrootte en rendering tellen op tot de ervaring die gebruikers werkelijk krijgen. Gedeelde standaarden, componentbibliotheken, prestatiebudgetten en architectuurpatronen houden veel onafhankelijke teams ervan af een trage, inconsistente, kwetsbare eenheid te produceren.

De relevantie voor onderneming en overheid is acuut. Ondernemingen onderhouden langlevende applicaties waar levensduur van frameworks en onderhoudbaarheid zwaarder wegen dan nieuwigheid, en waar veel teams moeten samenwerken. Overheden bedienen het hele publiek, inclusief mensen op oude apparaten, trage of gemeten verbindingen en hulptechnologieën. Dat maakt prestaties, [progressive enhancement](https://en.wikipedia.org/wiki/Progressive_enhancement) en veerkracht geen optionele afwerking maar het verschil tussen een dienst die voor iedereen werkt en een die de minst bevoorrechten uitsluit. Een overheidsdienst die alleen werkt op de nieuwste telefoon met een snelle verbinding faalt in haar mandaat.

## Kernprincipes

- De frontend draait in een omgeving die je niet beheert. Ontwerp voor variabiliteit en falen.
- Kies saaie, duurzame technologie voor langlevende systemen. Optimaliseer voor onderhoudbaarheid en personeel aannemen.
- Prestaties zijn een functie en, voor veel gebruikers, een voorwaarde voor toegang.
- Progressive enhancement: lever eerst een werkende kernervaring en leg er dan verbeteringen overheen.
- Stuur minder code. De snelste en betrouwbaarste code is de code die je niet uitlevert.
- Stem de renderstrategie af op contenttype en gebruikersbehoefte, niet op de mode.
- Veerkracht: de interface moet soepel degraderen, niet breken, wanneer dingen misgaan.
- Standaarden en platformfuncties overleven frameworks. Leun op het platform.

## Aanbevelingen

### Kies frameworks voor levensduur en pasvorm, niet voor hype

Selecteer frontendtechnologie op basis van het probleem, het team, de onderhoudshorizon en de arbeidsmarkt, niet op wat trendt. Geef voor langlevende systemen van onderneming en overheid de voorkeur aan volwassen, goed ondersteunde technologieën met grote talentpools, stabiele releasepraktijken en heldere upgradepaden. Weeg de totale kosten van frameworkonrust: herschrijvingen zijn duur en riskant. Geef de voorkeur aan aanpakken die leunen op [webstandaarden](https://en.wikipedia.org/wiki/Web_standards) zodat je investering frameworkomloop overleeft, en isoleer frameworkspecifieke code achter grenzen zodat de applicatie niet gegijzeld wordt door de levenscyclus van één bibliotheek.

### Stem renderstrategie af op de behoefte

De belangrijkste renderstrategieën passen elk bij andere content. Server-side rendering (SSR) produceert snelle eerste weergave en goede SEO ([zoekmachineoptimalisatie](https://en.wikipedia.org/wiki/Search_engine_optimization)) en werkt zonder client-JavaScript, geschikt voor contentrijke en publieke pagina's. [Static site generation](https://en.wikipedia.org/wiki/Static_site_generator) (SSG) rendert vooraf bij build voor maximale snelheid en cachebaarheid, ideaal voor content die zelden verandert. Client-side rendering (CSR) past bij sterk interactieve app-achtige ervaringen achter authenticatie. Streaming en progressieve hydratatie sturen en activeren de pagina stapsgewijs zodat gebruikers content sneller zien en gebruiken. Veel grote systemen mengen deze per route in plaats van er globaal één te kiezen. Beheer status bewust: houd serverstatus, URL-status en lokale UI-status gescheiden en voorkom alles te centraliseren in één zware globale store.

### Behandel prestaties als begrote, gemeten discipline

Neem prestatiebudgetten aan (expliciete limieten op bundelgrootte, aantal verzoeken en sleutelstatistieken) en dwing ze af in CI zodat regressies de build laten falen. Volg de Core Web Vitals (laden, interactiviteit en visuele stabiliteit) met real-user monitoring van echte apparaten en netwerken, niet alleen labtests op snelle machines. Verminder JavaScript agressief: splits code en [laad lui](https://en.wikipedia.org/wiki/Lazy_loading) zodat gebruikers alleen downloaden wat een gegeven weergave nodig heeft, stel niet-kritisch werk uit en geef de voorkeur aan platformmogelijkheden boven zware bibliotheken. Optimaliseer afbeeldingen en lettertypen, cache effectief en meet op representatieve apparaten van lage kwaliteit en trage verbindingen.

### Bouw met progressive enhancement en veerkracht

Begin vanuit een basis die werkt met semantische HTML en minimaal of geen JavaScript, en verbeter dan voor capabele clients. Dit zorgt dat de kerntaak mogelijk blijft wanneer scripts niet laden, een apparaat oud is of een netwerk wankel, een gangbare realiteit in plaats van een randgeval. Handel fouten soepel af: toon nuttige toestanden voor laden, leeg, fout en offline in plaats van lege schermen of oneindige spinners. Overweeg voor diensten waar mensen van afhangen offline-first-technieken zodat de app bruikbaar blijft door onderbroken connectiviteit en synchroniseert wanneer de verbinding terugkeert.

### Zorg voor compatibiliteit over browsers, apparaten en hulptechnologie

Test over de browsers, apparaten en hulptechnologieën die je gebruikers werkelijk hebben, geïnformeerd door echte analytics in plaats van de eigen machines van het team. Gebruik progressive enhancement en featuredetectie in plaats van aan te nemen dat de nieuwste platformfuncties overal beschikbaar zijn. Bouw [responsief](https://en.wikipedia.org/wiki/Responsive_web_design) (zie het hoofdstuk over designsystemen) zodat één codebasis telefoons tot desktops bedient. Integreer toegankelijkheid en internationalisering vanaf het begin in de frontendarchitectuur, niet als latere rondes.

### Bestuur de frontend als gedeelde infrastructuur

Lever gedeelde componentbibliotheken, linting, formattering en buildtooling zodat teams consistent en productief zijn. Stel architectuurrichtlijnen vast (hoe applicaties te structureren, status te beheren en bundels te splitsen) en prestatiebudgetten afgedwongen in CI. Overweeg voor zeer grote frontends modulaire of micro-frontendarchitecturen die teams onafhankelijk laten deployen, maar weeg de toegevoegde complexiteit en prestatiekosten zorgvuldig af, want ze zijn niet gratis.

## Afwegingen: voor- en nadelen

| Beslissing | Voordelen | Nadelen |
|---|---|---|
| Populair, volwassen framework | Grote talentpool, stabiel, ondersteund | Kan legacyballast dragen. Langzamer in het overnemen van de nieuwste functies |
| Nieuwste framework | Moderne functies, prestatiewinst | Onrustrisico, kleine talentpool, onzekere levensduur |
| SSR / SSG | Snelle eerste weergave, SEO, werkt zonder JS | Server- of buildcomplexiteit, cache-uitdagingen |
| CSR (SPA) | Rijke interactiviteit, app-gevoel | Trage eerste load, JS-afhankelijk, kosten voor SEO en veerkracht |
| Zware client-JavaScript | Rijke functies | Slechte prestaties op apparaten van lage kwaliteit, fragiel |
| Progressive enhancement | Veerkrachtig, inclusief, werkt overal | Meer ontwerpinspanning om een werkende basis te definiëren |
| Micro-frontends | Onafhankelijke teamdeploys, schaal | Complexiteit, gedupliceerde afhankelijkheden, prestatie-overhead |

De terugkerende afweging is rijkdom en gemak voor ontwikkelaars tegenover bereik, prestaties en veerkracht. Zware client-side aanpakken zijn prettig om te bouwen en te demonstreren op snelle machines, maar sluiten gebruikers op zwakke apparaten en netwerken uit. Laat de balans voor doelgroepen van onderneming en vooral overheid overhellen naar prestaties, progressive enhancement en duurzaamheid, omdat de kosten van gebruikers uitsluiten hoog en vaak niet onderhandelbaar zijn.

## Vragen om met je team te bespreken

1. **Hoe isoleren we frameworkspecifieke code zodat de applicatie niet gegijzeld wordt door de levenscyclus van één bibliotheek?** Voor langlevende systemen van onderneming en overheid is frameworkonrust de grootste vermijdbare uitgave: een herschrijving is duur en riskant, en de trending bibliotheek van vandaag beperkt jarenlang aannemen en onderhoud. Leunen op webstandaarden en frameworkspecifieke code achter heldere grenzen zetten betekent dat je bedrijfslogica en content de volgende frameworkomloop overleven. Besluit waar die naden liggen en of een nieuwe engineer platformcode van frameworkcode kan onderscheiden. Neem een schatting mee van wat je laatste frameworkmigratie kostte, of wat de dreigende zal kosten. Als je kernlogica vastgelast zit aan de API's van één bibliotheek, prijs die koppeling dan voordat je de frameworkkeuze verdedigt.

2. **Stemmen we renderstrategie per route af, of dwingen we één strategie op het hele product?** Server-side rendering geeft snelle eerste weergave en werkt zonder client-JavaScript voor publieke content, statische generatie maximaliseert snelheid voor pagina's die zelden veranderen en client-rendering past bij interactieve app-achtige oppervlakken achter login. Eén globaal afdwingen vertraagt óf publieke pagina's met zware JavaScript óf over-engineert een eenvoudige contentpagina. Dit is een bereiksvraag voor de overheid, waar een dienst die pas werkt nadat een grote bundel is geladen gebruikers op oude apparaten en trage verbindingen uitsluit. Neem je sleutelroutes mee en label elke met de strategie die ze vandaag werkelijk gebruikt. Als een publiek toegankelijke pagina JavaScript nodig heeft om haar content te tonen, besluit dan of dat een bewuste keuze is of een ongeluk.

3. **Hoe gedisciplineerd is ons statusbeheer, en centraliseren we alles te veel in één zware globale store?** Serverstatus, URL-status en lokale UI-status gescheiden houden voorkomt de koppeling en re-renderstormen die grote frontends traag en fragiel maken, maar de verleidelijke standaard is alles in één globale store te dumpen. Dit stapelt zich op op schaal, waar veel teams die aan één gedeelde store zitten verborgen afhankelijkheden en onvoorspelbare prestaties creëren. Spreek af waar elk soort status thuishoort en wat niet in de globale store hoort. Neem een component mee die vaker rendert dan zou moeten en traceer waarom. Als het antwoord een opgeblazen centrale store is, besluit dan de grenzen voordat de koppeling uithardt.

4. **Wat zijn onze prestatiebudgetten, laten ze de build falen in CI en worden ze gemeten op de apparaten die onze gebruikers werkelijk hebben?** Een budget dat niemand afdwingt is een wens, en een budget alleen gemeten op de snelle laptops van het team beschrijft een gebruiker die niet bestaat. Voor een grote organisatie zijn budgetten het ene mechanisme dat bundelgrootte en Core Web Vitals in toom houdt terwijl tientallen teams functies aan een gedeeld oppervlak toevoegen, omdat geen enkele reviewer elke regressie met het oog kan vangen. De concurrerende druk is leveringssnelheid: een harde buildfout over een paar kilobyte voelt hinderlijk tot je de afhaakkosten prijst die het voorkomt. Neem je huidige budgetten mee, de real-user monitoringdata van apparaten van lage kwaliteit en trage verbindingen en de lijst releases waar een regressie doorglipte. Koppel het budget bij de overheid, waar het mandaat is het hele publiek te bedienen inclusief mensen op oude telefoons en gemeten data, aan het langzaamste tiende van je gebruikers in plaats van de mediaan, en maak de CI-poort niet onderhandelbaar.

5. **Welke van onze diensten moeten blijven werken zonder client-JavaScript, en hebben we dat pad werkelijk getest?** Progressive enhancement is makkelijk te claimen en makkelijk stilletjes te breken, omdat het verbeterde pad degene is die ontwikkelaars dagelijks gebruiken terwijl de basis ongetest wegrot. Dit bewust beslissen telt op schaal, aangezien veel teams die naar één platform opleveren elk zullen aannemen dat scripts altijd laden tenzij een gedeelde standaard anders zegt, en één harde afhankelijkheid de kerntaak kan breken voor iedereen wiens bundel faalt. De afweging is echt: een werkende no-JavaScript-basis kost ontwerpinspanning en beperkt hoe je interactiviteit bouwt. Neem je kritieke gebruikersreizen mee, een test die elk laadt met scripts uitgeschakeld of gefaald en bewijs van hoe vaak scripts in het veld werkelijk niet laden. Voor een publieke dienst is een uitkerings- of belastingformulier dat instort wanneer één script time-out gaat geen gedegradeerde ervaring, het is een burger die een wettelijke verplichting niet kan voltooien, dus behandel de basis als complianceeis, niet als aardigheid.

6. **Wanneer betalen micro-frontends werkelijk voor hun complexiteit, en wie beslist voordat een team er een pakt?** Onafhankelijke teamdeploys zijn aantrekkelijk, maar micro-frontends dragen complexiteit van gedistribueerde systemen, gedupliceerde afhankelijkheden en een prestatiebelasting die gebruikers betalen in tragere loads. Zonder gedeeld beslispunt nemen ambitieuze teams ze aan voor organisatorisch gemak lang voordat de schaal de kosten rechtvaardigt, en het hele product erft de overhead. De concurrerende overweging is autonomie: teams die op één gedeelde codebasis opleveren kunnen elkaar blokkeren, en op echte schaal is die koppeling zelf een dure kwestie. Neem het aantal teams mee dat aan het oppervlak zit, de deploycontentie die je vandaag werkelijk ervaart en een gemeten schatting van de payloadduplicatie die een splitsing zou introduceren. Eis voor platforms van onderneming en overheid, waar architectuurbeslissingen veel teams jarenlang binden en een audit en overdracht moeten overleven, een expliciete, gedocumenteerde drempel en een eigenaar die de stap goedkeurt, in plaats van elk team in isolatie te laten beslissen.

## Sectorperspectief

**Startup.** Snelheid en bereik tellen allebei wanneer elke aanmelding telt, dus weersta de zware single-page-app voor publieke pagina's. Render je marketing en aanmeldstroom server-side zodat ze snel laden op de middenklassetelefoons en wankele data die je vroege klanten gebruiken, en reserveer client-side interactiviteit voor de app achter login. Stel één eenvoudig bundelgroottebudget in CI in zodat een onzorgvuldige afhankelijkheid de pagina niet stilletjes kan opblazen, en leun op webstandaarden om een kleine codebasis onderhoudbaar te houden terwijl je mensen aanneemt.

**Kleinbedrijf.** Zonder aparte frontendspecialist en met een krap budget geef je de voorkeur aan een goed ondersteund mainstreamframework of een gehoste sitebouwer boven iets op maat, zodat je uit een grote talentpool aanneemt en onderhoud koopt in plaats van het te bemannen. Formuleer de keuze als duurzaamheid: de goedkoopste optie is degene die je over twee jaar niet hoeft te herschrijven. Sta erop dat pagina's snel en mobielvriendelijk zijn en toegankelijke opmaak standaard meekomt, want een trage of kapotte checkout kost je klanten die je je niet kunt veroorloven te verliezen.

**Grote onderneming.** Het probleem is consistentie over veel teams: een gedeelde componentbibliotheek, afgesproken architectuurpatronen, linting en buildtooling en prestatiebudgetten afgedwongen in CI zodat geen team het geheel stilletjes kan laten achteruitgaan. Kies frameworks voor levensduur en personeel aannemen in plaats van nieuwigheid, isoleer frameworkspecifieke code achter grenzen om de volgende migratie te overleven en stem renderstrategie per oppervlak af. Beheer de frontend als gedeelde infrastructuur met real-user monitoring, governance en een controleerbaar overzicht van waarom elke architectuurkeuze is gemaakt.

**Overheid.** Je bedient het hele publiek, inclusief mensen op oude apparaten, trage of gemeten verbindingen en hulptechnologieën, dus progressive enhancement en prestaties zijn verplichtingen, geen afwerking. Maak een werkende no-JavaScript-basis een harde regel voor burgergerichte diensten, begroot pagina's voor de langzaamste gebruikers in plaats van de mediaan en houd de kerntaak voltooibaar wanneer een script faalt. Aanbesteding en transparantie gelden: geef de voorkeur aan duurzame, op standaarden leunende technologie die lock-in bij één leverancier vermijdt, documenteer de toegankelijkheids- en prestatie-eisen in contracten en kun aantonen dat de dienst werkt voor de minst bevoorrechte gebruiker, niet alleen het demonstratieapparaat.

## Voorbeelden

**Startup.** Een startup in de seedfase werd verleid haar marketingsite en aanmeldstroom als zware single-page-app te bouwen, maar haar doelklanten waren shoppers vaak op middenklassetelefoons over wankele mobiele data. De twee oprichters renderden in plaats daarvan de publieke pagina's server-side zodat ze snel laadden en werkten voordat enige JavaScript draaide, en reserveerden client-side interactiviteit voor de app achter login. Ze stelden een eenvoudig bundelgroottebudget in CI in zodat een onzorgvuldige afhankelijkheid de pagina niet stilletjes kon opblazen. De slanke, snelle eerste load verbeterde de aanmeldingen meetbaar, en leunen op webstandaarden hield hun kleine codebasis makkelijk te onderhouden terwijl ze mensen aannamen.

**Grote onderneming.** Een financiëledienstenbedrijf moderniseerde een uitgestrekte set interne en klantapplicaties door te standaardiseren op een volwassen framework, een gedeelde componentbibliotheek en afgedwongen prestatiebudgetten in CI. Renderstrategie werd per oppervlak gekozen: server-side gerenderde, cachebare pagina's voor publieke marketing en content, en een client-side gerenderde applicatie achter login voor interactieve dashboards. Bundelbudgetten en real-user monitoring vingen regressies vóór release, hielden laadtijden snel over de vele teams van het bedrijf en verminderden het risico van frameworkonrust dat eerder dure herschrijvingen had afgedwongen.

**Overheid.** Een nationaal digitaal dienstteam bouwde burgergerichte diensten met progressive enhancement als harde regel: elke dienst werkt eerst met semantische HTML en server-rendering, en JavaScript verbetert alleen. Dit garandeert dat de dienst functioneert op oude telefoons, trage landelijke verbindingen en hulptechnologieën, populaties die een overheid niet kan uitsluiten. Prestatiebudgetten houden pagina's licht en snel op apparaten van lage kwaliteit, en soepele degradatie betekent dat een mislukt script nooit iemand belet een uitkeringsaanvraag af te ronden. Het resultaat is een dienst die snel, veerkrachtig, toegankelijk en bruikbaar is voor het hele publiek.

## Zakelijke onderbouwing: motivatie, ROI en TCO

Frontend-engineeringkeuzes drijven omzet, bereik en kosten. Prestaties zijn direct gekoppeld aan conversie, betrokkenheid en taakvoltooiing. Snellere ervaringen presteren meetbaar beter dan tragere, en voor gebruikers op zwakke apparaten is prestatie de lijn tussen de dienst gebruiken en afhaken. Progressive enhancement en ondersteuning over apparaten vergroten het adresseerbare publiek, wat voor de overheid een mandaat is en voor onderneming marktaandeel. Degelijke framework- en architectuurkeuzes verminderen de frequentie en kosten van herschrijvingen, de grootste vermijdbare uitgave in frontend-engineering.

Qua TCO zijn de adoptiekosten de discipline van prestatiebudgetten en testen, de inspanning van progressive enhancement en de investering in gedeelde tooling en componentbibliotheken. De kosten van niet adopteren worden betaald in trage ervaringen die gebruikers en omzet verliezen, uitsluiting van gebruikers met apparaten van lage kwaliteit en hulptechnologie (met juridische blootstelling bij de overheid), fragiele applicaties die in het veld breken en dure frameworkonrust en herschrijvingen gedreven door trends najagen. Frontendproblemen verschijnen als diffuus afhaken en supportlast in plaats van een enkele kostenpost, en zijn dus makkelijk te onderbelichten.

Verbind Core Web Vitals en laadtijden voor het bestuur aan conversie- en voltooiingstrechters, kwantificeer de gebruikers die door zware client-side aanpakken worden uitgesloten en prijs de kosten van eerdere of dreigende herschrijvingen tegen de stabiliteit van een duurzame, op standaarden leunende architectuur. Formuleer prestatiebudgetten en progressive enhancement als risicovermindering en bereiksuitbreiding.

## Antipatronen en valkuilen

- **Frameworks najagen**: herschrijven op de nieuwste bibliotheek, onrust zonder voordeel voor gebruikers.
- **Alleen-JavaScript-ervaringen**: niets werkt tot een grote bundel laadt en draait, wat veel gebruikers uitsluit.
- **Alleen op snelle apparaten testen**: de vlaggenschiplaptops van het team verbergen de echte gebruikerservaring.
- **Bundelgrootte negeren**: onbegrensde afhankelijkheidsgroei tot pagina's overal traag zijn.
- **Geen prestatiebudget**: regressies hopen zich stilletjes op, release na release.
- **Faalscenario's met leeg scherm**: geen laad-, lege, fout- of offlinetoestanden. Een mislukt verzoek breekt de pagina.
- **Over-gecentraliseerde globale status**: alles in één store, wat koppeling en re-renderstormen creëert.
- **Voortijdige micro-frontends**: complexiteit van gedistribueerde systemen en gedupliceerde payloads zonder de schaal om ze te rechtvaardigen.
- **Toegankelijkheid en i18n in de architectuur verwaarlozen**: ze later vastschroeven tegen hoge kosten.

## Volwassenheidsmodel

**Niveau 1: Initiëren.** Ad hoc frontend gebouwd per team zonder gedeelde standaarden. Zware client-side code, geen prestatiebudgetten, alleen getest op de eigen apparaten van het team. Frameworkkeuzes gemaakt op voorkeur of hype, en een mislukt script kan gebruikers naar een leeg scherm laten staren.

**Niveau 2: Ontwikkelen.** Sommige teams nemen gedeelde tooling en een componentbibliotheek over, maar de praktijk is inconsistent over de organisatie. Prestaties worden af en toe gemeten in plaats van begroot of afgedwongen. Renderstrategie is vaak uniform ongeacht contenttype, en testen over apparaten is beperkt en handmatig.

**Niveau 3: Standaardiseren.** Framework en architectuur worden bewust gekozen voor levensduur, en de keuzes zijn gedocumenteerd en organisatiebreed afgedwongen. Renderstrategie wordt per oppervlak afgestemd, progressive enhancement en soepele degradatie zijn de standaard, en gedeelde componentbibliotheken, linting en buildtooling gelden voor elk team. Cross-browser, toegankelijkheid en internationalisering zijn ingebouwd in plaats van vastgeschroefd.

**Niveau 4: Beheersen.** De frontend wordt gemeten en beheerst met data. Prestatiebudgetten worden afgedwongen in CI zodat regressies de build laten falen, en Core Web Vitals worden gevolgd met real-user monitoring van echte apparaten van lage kwaliteit en trage verbindingen tegen expliciete uitgangswaarden. Bundelgrootte, dekking van fout- en offlinetoestanden en het aandeel gebruikers bediend op de langzaamste verbindingen worden gerapporteerd en beoordeeld, zodat beslissingen op bewijs rusten in plaats van mening.

**Niveau 5: Orkestreren.** Prestaties, veerkracht en bereik worden continu verbeterd en gekoppeld aan zakelijke uitkomsten over de hele organisatie. De frontend leunt op webstandaarden voor duurzaamheid, isoleert frameworkafhankelijkheden zodat migraties goedkoop zijn en evolueert architectuur adaptief naarmate apparaten, het platform en real-user data verschuiven. Het hele publiek en alle apparaten zijn eersterangs, en frontendpraktijk is geïntegreerd met ontwerp, toegankelijkheid en productplanning in plaats van behandeld als aparte zorg.

## Ideeën voor discussie

- Hoe beslis je wanneer een frameworkmigratie haar kosten en risico waard is?
- Welke Core Web Vitals en bundelbudgetten moeten harde buildfalende drempels zijn?
- Waar is progressive enhancement essentieel, en waar is een client-side app acceptabel?
- Hoe houd je frontendarchitectuur consistent over veel autonome teams?
- Wanneer betalen micro-frontends werkelijk voor hun complexiteit?
- Hoe moeten tests op echte apparaten en trage netwerken in de pijplijn worden gebouwd?

## Belangrijkste inzichten

- De frontend draait in een omgeving die je niet beheert: ontwerp voor variabiliteit en falen.
- Kies duurzame, goed ondersteunde technologie voor langlevende systemen. Leun op webstandaarden.
- Stem renderstrategie (SSR, SSG, CSR, streaming) af op content en behoefte, vaak gemengd per route.
- Behandel prestaties als begrote, gemeten discipline afgedwongen in CI met real-user data.
- Bouw met progressive enhancement zodat de kernervaring overal werkt.
- Lever minder JavaScript: splits code, laad lui en geef de voorkeur aan platformmogelijkheden.
- Vooral voor de overheid zijn prestaties en veerkracht voorwaarden voor gelijke toegang.

## Referenties en verder lezen

- Jeremy Keith, *Resilient Web Design*
- Aaron Gustafson, *Adaptive Web Design* (progressive enhancement)
- Steve Souders, *High Performance Web Sites*
- Ilya Grigorik, *High Performance Browser Networking*
- Addy Osmani, writings on performance, code-splitting, and the cost of JavaScript
- Google, *Web Vitals* and web.dev performance guidance
- MDN Web Docs, web platform and progressive enhancement references
- Alex Russell, essays on the cost of JavaScript and device diversity
- UK Government Digital Service, progressive enhancement and frontend guidance
- WHATWG HTML Living Standard and W3C web platform specifications
