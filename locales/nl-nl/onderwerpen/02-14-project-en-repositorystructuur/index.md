# 2.14 Project- en repositorystructuur

## Overzicht en motivatie

Project- en repositorystructuur is de fysieke organisatie van een codebase: de mappen, bestanden en naamconventies die bepalen waar een bepaald ding woont. Een *repository* (vaak ingekort tot "repo") is de [onder versiebeheer staande](https://en.wikipedia.org/wiki/Version_control) container die de bestanden van een project en hun geschiedenis bevat. Een *project*, soms een *solution* genoemd wanneer het meerdere verwante componenten groepeert, is de logische eenheid software die je bouwt. Structuur is de kaart waarmee je die software vindt, begrijpt en wijzigt.

In een klein team kan één persoon de hele indeling in zijn hoofd houden. In een groot team, met honderden of duizenden engineers, frequente verhuizingen tussen teams en externen die komen en gaan, levert elke repository die anders is georganiseerd een nieuwe cognitieve belasting op. Wanneer je een onbekende repo opent, moet je kunnen raden waar de broncode, de tests, de documentatie en de deploymentconfiguratie wonen, zonder een handleiding te lezen. Wanneer elke repo die vragen op dezelfde manier beantwoordt, is mobiliteit goedkoop en onboarding snel. Wanneer elke repo een uitzondering is, wordt elke contextwissel een klein onderzoeksproject.

In omgevingen van onderneming en overheid is consistente structuur ook een kwestie van beheersing en zekerheid. Auditors, beveiligingsreviewers en onderhouders op lange termijn, die vaak jaren nadat de oorspronkelijke auteurs weg zijn werken, moeten specificatiedocumenten, licentiebestanden, beveiligingsbeleid en builddefinities betrouwbaar kunnen vinden. Een voorspelbare indeling laat ook geautomatiseerde tooling (scanners, afhankelijkheidsanalysers, compliancecontroles) over een heel portfolio van systemen op dezelfde manier werken. Dit hoofdstuk behandelt structuur daarom als een conventie die je eenmaal vaststelt en overal toepast. Het is nauw verwant aan codeerstandaarden en stijl (hoofdstuk 2.1), versiebeheer en broncodebeheer (hoofdstuk 2.6) en documentatie (hoofdstuk 2.7).

## Kernprincipes

- Volg het *[principe van de minste verrassing](https://en.wikipedia.org/wiki/Principle_of_least_astonishment)*: de indeling moet overeenkomen met wat een ervaren engineer zou verwachten, zodat niets uit het hoofd geleerd hoeft te worden.
- Consistentie over repositories wint van lokale slimmigheid. Een voldoende uniforme structuur overal is meer waard dan de perfecte structuur op één plek.
- De [README](https://en.wikipedia.org/wiki/README) is de voordeur. Een nieuwkomer moet zich vanuit alleen die kunnen oriënteren.
- Maak structuur zelfbeschrijvend door naamgeving, zodat mappen en bestanden hun doel aankondigen.
- Dwing structuur af met scaffolding en sjablonen, niet met wilskracht en reviewopmerkingen.
- Scheid verantwoordelijkheden fysiek: broncode, tests, documentatie, build en deployment horen op aparte, voorspelbare plaatsen.
- Organiseer afhankelijkheden zodat ze in één richting stromen, van stabiele kernen naar volatiele randen.

## Aanbevelingen

### Neem een consistente indeling op het hoogste niveau aan

Definieer een standaardset mappen op het hoogste niveau die elke repository gebruikt waar van toepassing, en documenteer waar elke voor dient. Een gangbare, leverancieronafhankelijke conventie omvat: een bronmap (vaak `src`) voor productiecode, een testmap (vaak `test` of `tests`) voor geautomatiseerde tests, een `docs`-map voor documentatie, een `build`-map voor builddefinities en -uitvoer, een `deploy`-map voor deployment en *[infrastructure as code](https://en.wikipedia.org/wiki/Infrastructure_as_code)* (machineleesbare definities van servers, netwerken en diensten, behandeld in hoofdstuk 8.2), een `scripts`-map voor automatisering en ontwikkelaarstooling, een `examples`-map voor draaibare voorbeelden en een `spec`- of `specification`-map voor vereisten en ontwerpspecificaties. Niet elke repo heeft elke map nodig, maar waar een aspect bestaat, hoort het op de verwachte plaats met de verwachte naam te staan.

### Maak de README het startpunt

Eis een README-bestand in de root van de repository als enige, canonieke beginpunt. Het moet vermelden wat het project is, hoe je het bouwt en draait, hoe je de tests draait, waar diepere documentatie te vinden is, wie het bezit en hoe je bijdraagt. De README is niet de hele documentatieset. Ze is de index die naar de rest verwijst (hoofdstuk 2.7). Behandel een ontbrekende of verouderde README als defect, want het is het eerste wat elke nieuwe engineer, auditor of integrator leest.

### Standaardiseer editor- en configuratiebestanden

Check gedeelde editor- en toolingconfiguratie in de repository in, zodat elke bijdrager automatisch consistent gedrag krijgt. Een `.editorconfig`-bestand (een eenvoudig, editoronafhankelijk bestand dat regels voor witruimte, inspringing en regeleinden definieert) houdt de basisopmaak uniform over verschillende editors en besturingssystemen. Voeg een ignorebestand voor het versiebeheersysteem toe (zodat buildoutput en lokale artefacten nooit worden gecommit), samen met de gedeelde formatter- en linterconfiguraties uit hoofdstuk 2.1. Deze bestanden maken de conventies van de repository actief, niet alleen gedocumenteerd.

### Definieer naam- en mapconventies

Spreek conventies af voor het benoemen van mappen en bestanden (hoofdlettergebruik, scheidingstekens, enkelvoud tegenover meervoud en verplichte achtervoegsels zoals die welke tests markeren) en pas ze uniform toe. Namen moeten de bedoeling onthullen en aansluiten bij het domeinvocabulaire dat elders in de organisatie wordt gebruikt. Het doel is eenvoudig: een pad moet betekenis communiceren, zodat het lezen van een map- of bestandsnaam je vertelt wat erin zit zonder te openen.

### Organiseer lagen en afhankelijkheden bewust

Structureer de codebase zo dat haar architectuurlagen in de maplay-out zichtbaar zijn en afhankelijkheden in één verstandige richting stromen. Beleid op hoger niveau mag niet afhangen van detail op laag niveau. Gedeelde, stabiele code hoort waar veel modules erbij kunnen zonder cycli te creëren. Wanneer je de gelaagdheid fysiek maakt, weerspiegeld in de mappenboom, zullen engineers haar eerder respecteren en zijn schendingen makkelijker te zien in review en in geautomatiseerde afhankelijkheidscontroles.

### Dwing structuur af met scaffolding en sjablonen

Bied *[scaffolding](https://en.wikipedia.org/wiki/Scaffold_%28programming%29)*, de geautomatiseerde generatie van een startproject, zodat nieuwe repositories al correct beginnen. Een *sjabloon* of *cookiecutter* (een geparametriseerd projectskelet dat uit antwoorden op een paar vragen een kant-en-klare repository genereert) codeert de standaardindeling, de README, de configuratiebestanden en de [CI](https://en.wikipedia.org/wiki/Continuous_integration)-opzet op één plaats. Wanneer engineers nieuwe services uit een gedeeld sjabloon maken, wordt consistentie de standaard in plaats van een aspiratie, en verbeteringen aan het sjabloon stromen door naar toekomstige projecten.

### Houd structuur consistent over veel repositories op schaal

Behandel de indeling zelf als een bestuurde standaard: centraal onderhouden zoals elke andere engineeringstandaard (hoofdstuk 1.7) en geversioneerd als code (hoofdstuk 2.6). Publiceer haar, lever de sjablonen die haar implementeren en sta afwijkingen alleen toe via een gedocumenteerd uitzonderingsproces, zodat "de standaard" haar betekenis behoudt. Op portfolioschaal komt bijna alle waarde van structuur uit haar uniformiteit over repositories, dus afdrijving is het belangrijkste risico om te beheren.

### Laat structuur de keuze tussen monorepo en multi-repo informeren

Relateer structuur aan de beslissing over repositorygrenzen uit hoofdstuk 2.6. Een *[monorepo](https://en.wikipedia.org/wiki/Monorepo)* (één repository met veel projecten) heeft een heldere interne conventie nodig om projecten en hun gedeelde code te scheiden, zodat de ene boom navigeerbaar blijft. Een *multi-repo*-aanpak (veel kleine repositories, één per project of service) heeft sterke consistentie tussen repo's nodig, zodat elke repo vertrouwd aanvoelt ook al staat ze op zichzelf. Hoe dan ook houdt een gedocumenteerde, gesjabloneerde structuur navigatie voorspelbaar. De grenskeuze verandert waar je de conventie toepast, niet of je er een nodig hebt.

## Afwegingen: voor- en nadelen

| Keuze | Voordelen | Nadelen |
|---|---|---|
| Strikte standaardindeling voor de hele organisatie | Directe vertrouwdheid. Inwisselbare engineers. Uniforme tooling | Af en toe slechte pasvorm voor ongewone projecten. Vraagt governance |
| Vrijheid van indeling per team | Lokale optimalisatie. Hoge autonomie | Fragmentatie. Kostbare contextwissels. Inconsistente tooling |
| Scaffolding en sjablonen | Repo's zijn standaard correct. Wijzigingen planten zich voort | Onderhoud van sjablonen. Risico van afdrijving van gegenereerde repo's |
| Diepe, gelaagde maphiërarchie | Expliciete structuur. Heldere grenzen | Navigatie-overhead. Lange paden. Risico van over-engineering |
| Vlakke, ondiepe indeling | Makkelijk te scannen. Weinig ceremonie | Slechte scheiding. Valt uiteen naarmate het project groeit |

De dominante afweging is uniformiteit tegenover autonomie. Eén standaardindeling neemt wrijving weg voor de vele engineers die tussen codebases bewegen, ten koste van het af en toe voorkomende project waarvan de behoeften niet netjes in de mal passen. In een grote organisatie weegt de collectieve winst van vertrouwdheid bijna altijd op tegen dat lokale verlies. Daarom is de aanbevolen houding een sterke standaard plus een gedocumenteerd uitzonderingspad (hoofdstuk 1.7), in plaats van starre uniformiteit of onbeheerde vrijheid. Een tweede afweging is diepte tegenover eenvoud: genoeg structuur om echte verantwoordelijkheden te scheiden, maar niet zoveel dat navigatie een wandeling door lege mappen wordt.

## Vragen om met je team te bespreken

1. **Wanneer een engineer naar een onbekende repo van ons verhuist, hoe lang duurt het tot hij de tests, de deployconfiguratie en de eigenaar kan vinden?** Dit is de navigatiebelasting die structuur moet wegnemen, en op portfolioschaal wordt ze duizenden keren per jaar in kleine stukjes betaald die optellen tot serieus verloren engineeringtijd. Het punt van het principe van de minste verrassing is dat een ervaren engineer moet kunnen raden waar broncode, tests, documentatie en deployment wonen zonder een handleiding te lezen, dus de eerlijke toets is of dat raden slaagt over je repo's. Neem een echt getal mee naar de vergadering: tijd jezelf bij het oriënteren in twee of drie onbekende interne repositories, of haal onboardingdata op over hoe lang nieuwe medewerkers erover doen een eerste wijziging te maken. Als het antwoord in dagen onderzoek wordt gemeten in plaats van in minuten herkenning, heb je de kosten van uitzonderingsrepo's gekwantificeerd, en dat rechtvaardigt de eenmalige investering in een standaardindeling die elke repo deelt.

2. **Verschijnen onze architectuurlagen in de mappenboom, of verbergen afhankelijkheidscycli zich in een vlakke indeling?** Structuur gaat om meer dan vindbaarheid: wanneer je gelaagdheid fysiek maakt, respecteren engineers haar en kunnen reviewers en geautomatiseerde afhankelijkheidscontroles schendingen zien, terwijl een vlakke hoop ongepaste koppeling en cycli ongemerkt laat insluipen tot verandering gevaarlijk wordt. In een groot, langlevend systeem houdt dit beleid op hoger niveau ervan stilletjes van detail op laag niveau af te hangen, en het is precies het soort erosie dat goedkoop te voorkomen en duur om terug te draaien is. Neem je afhankelijkheidsgraaf mee of voer een snelle controle uit: zijn er cycli, en hangt iets stabiels af van iets volatiels? Het antwoord moet je ertoe brengen lagen in mappen te weerspiegelen en geautomatiseerde controles op afhankelijkheidsrichting toe te voegen, zodat de grenzen zichtbaar zijn in de boom en afgedwongen in de pipeline in plaats van alleen in iemands mentale model te leven.

3. **Beginnen onze nieuwe repositories correct vanuit een sjabloon, of vertrouwen we op een wikipagina en goede bedoelingen?** Structuur afgedwongen door scaffolding is de standaard. Structuur beschreven in een document drijft af, omdat de werkelijkheid volgt wat repo's genereert, niet wat een pagina zegt dat ze eruit moeten zien. Voor een grote of gereguleerde organisatie is dit ook een zekerheidskwestie: wanneer elke repo uit een gedeeld sjabloon wordt gegenereerd, vinden beveiligingsscanners, afhankelijkheidsanalysers en auditors de licentie, het beveiligingsbeleid, de specificatie en de builddefinitie elke keer op dezelfde plaats, over leveranciers en jaren heen. Neem het bewijs mee: hoeveel van je recente repo's zijn gescaffold uit het standaardsjabloon tegenover met de hand samengesteld, en hoever zijn de gesjabloneerde sindsdien afgedreven? De actie is het sjabloon de enige makkelijke manier te maken om een repo te starten, het te besturen als geversioneerde standaard met een gedocumenteerd uitzonderingspad en afdrijving automatisch te detecteren, want uniformiteit is waar bijna alle waarde van structuur zit.

4. **Hebben we besloten of onze standaard een monorepo of veel aparte repositories omspant, en geldt dezelfde conventie werkelijk aan beide kanten van die grens?** De keuze van repositorygrens verandert waar je de conventie toepast, niet of je er een nodig hebt, en het fout doen betekent één gigantische boom waar niemand in kan navigeren of een wildgroei van repo's die elk vreemd aanvoelen. Een monorepo heeft een heldere interne conventie nodig om projecten en hun gedeelde code te scheiden zodat de ene boom navigeerbaar blijft, terwijl een multi-repo-aanpak sterke consistentie tussen repo's nodig heeft zodat elke zelfstandige repo nog vertrouwd aanvoelt. Neem de huidige inventaris mee: hoeveel repo's je hebt, hoe gedeelde code binnen een monorepo wordt gescheiden en een getimede toets of een engineer een project in de grote boom even snel kan vinden als in een zelfstandige repo. Besluit voor een grote onderneming of een overheidsprogramma waar verschillende leveranciers aparte repositories opleveren bewust welke delen van de conventie universeel zijn en welke grensspecifiek, want auditors en platformtooling moeten op dezelfde manier werken of de code nu als één boom of als vijftig aankomt.

5. **Wie bezit onze structuurstandaard, en wat gebeurt er werkelijk wanneer een project er echt niet in past?** Op portfolioschaal komt bijna alle waarde van structuur uit uniformiteit, dus de echte risico's zijn een standaard zonder eigenaar die wegrot en een uitzonderingspad zo vaag dat elk team stilletjes zijn eigen indeling verzint. De spanning is die tussen starre uniformiteit die geen ongewoon project past en onbeheerde vrijheid die alles fragmenteert, en het gezonde antwoord is een sterke standaard plus een gedocumenteerd, controleerbaar uitzonderingsproces bestuurd door een benoemde eigenaar en geversioneerd als code. Neem het bewijs mee: is er één verantwoordelijke eigenaar, een geversioneerd standaarddocument met changelog, een logboek van verleende uitzonderingen en waarom en een telling van ongedocumenteerde afwijkingen die je in het wild kunt vinden. In omgevingen van onderneming en overheid is een niet vastgelegde uitzondering een gat in de beheersing, dus koppel elke afwijking aan een schriftelijke rechtvaardiging en een reviewdatum, en zorg dat aanbestedingscontracten die de indeling voorschrijven ook benoemen wie afwijkingen mag goedkeuren.

6. **Maken onze README en ingecheckte configuratiebestanden onze conventies actief, of zijn ze decoratief?** Een README is de voordeur en de ingecheckte `.editorconfig`, het ignorebestand en de linterconfiguratie maken conventies zelfhandhavend, maar toch zijn dit het eerste dat veroudert en het laatste dat iemand opmerkt tot een auditor of nieuwe medewerker het project niet gebouwd krijgt. De spanning is die tussen een slanke README die actueel blijft en een uitgebreide die afdrijft, en tussen mensen vertrouwen code correct op te maken en gedeelde configuratie het automatisch laten afdwingen. Neem een steekproef mee: haal vijf repo's op en controleer hoeveel README's werkelijk vermelden wat het project is, hoe je het bouwt, test en draait en wie het bezit, en hoeveel de gedeelde configuratiebestanden dragen in plaats van op individuele gewoonten te leunen. Behandel voor een grote of gereguleerde organisatie, waar integrators, beveiligingsreviewers en onderhouders op lange termijn de README voor al het andere lezen, een ontbrekende of verouderde voordeur als defect met een eigenaar, en controleer de aanwezigheid van configuratiebestanden automatisch zodat naleving niet van goede wil afhangt.

## Sectorperspectief

**Startup.** Snelheid wint, dus spreek één eenvoudige, vlak genoeg indeling af voor je eerste repo (src, test, docs, scripts, een ingevulde README, een `.editorconfig` en ignorebestanden) en bewaar haar dezelfde middag als licht sjabloon. Genereer de tweede service eruit, zodat beide repo's vertrouwd aanvoelen en een nieuwe externe in uren onboardt in plaats van een uitzondering te reverse-engineeren. Weersta diepe hiërarchieën en zware governance die je nog niet nodig hebt. Het hele rendement hier is dat twee oprichters en een externe één kaart delen.

**Kleinbedrijf.** Zonder platformspecialist en met een krap budget neem je de conventionele indeling aan die je taal of framework al veronderstelt in plaats van er een te verzinnen, zodat kant-en-klare tooling en elke nieuwe medewerker er al op getraind aankomt. Koop scaffolding (een frameworkgenerator of een cookiecuttersjabloon) in plaats van je eigen te bouwen, en besteed je schaarse inspanning aan het actueel houden van een ingevulde README. Die README is de goedkoopste verzekering die je hebt voor de dag dat de ene persoon die de indeling kende verder gaat.

**Grote onderneming.** Over veel teams en honderden repositories is het doel uniformiteit: publiceer een geversioneerde structuurstandaard, genereer elke nieuwe service uit gedeelde sjablonen, detecteer afdrijving automatisch en sta afwijkingen alleen toe via een gedocumenteerd uitzonderingsproces. Omdat elke repo er hetzelfde uitziet, is een engineer die naar een nieuw team wordt overgeplaatst binnen uren productief en vinden portfoliobrede beveiligings- en afhankelijkheidsscanners de licentie, het beveiligingsbeleid en de builddefinitie elke keer op dezelfde plaats. Begroot het onderhoud van sjablonen en afdrijvingsdetectie expliciet, want dat onderhoud houdt de standaard op schaal betekenisvol.

**Overheid.** Aanbesteding, transparantie en verantwoording op lange termijn geven de indeling vorm, dus schrijf een gemeenschappelijke structuur voor in de leveringsstandaarden die elke leverancier binden. Eis een `specification`-map die code koppelt aan goedgekeurde vereisten, een licentie- en beveiligingsbeleidsbestand in de root en een `deploy`-map met de infrastructure-as-code-definities, zodat auditors compliance-artefacten in elk systeem op dezelfde manier vinden. Omdat externen van verschillende leveranciers allemaal één kaart volgen, kost onderhoud nadat een contract eindigt veel minder, en wint het publiek een verdedigbaar, inspecteerbaar spoor van vereiste tot draaiende code.

## Voorbeelden

**Startup.** Een startup van drie personen spreekt een eenvoudige standaardindeling af voor zijn eerste repo (src, test, docs, scripts, een ingevulde README, een .editorconfig en ignorebestanden) en bewaart haar als licht sjabloon. Wanneer ze een maand later hun tweede service opstarten, genereren ze die uit dat sjabloon, zodat beide repo's al vertrouwd aanvoelen en de nieuwe externe in een middag onboardt. Ze weerstaan diepe maphiërarchieën die ze nog niet nodig hebben en houden de boom vlak genoeg om in één oogopslag te scannen. De kosten waren een middag opzet, en het bespaart hen de wildgroei aan uitzonderingen die anders van elke toekomstige repo een klein onderzoeksproject zou maken.

**Grote onderneming.** Een multinationale retailer draait honderden services in meerdere talen. Het platformteam publiceert een geversioneerde repositorystructuurstandaard en een set projectsjablonen die haar implementeren. Elke nieuwe service wordt uit een sjabloon gegenereerd, dus komt hij binnen met de standaardmappen `src`, `test`, `docs`, `deploy` en `scripts`, een ingevulde README, een `.editorconfig`, ignorebestanden en een werkende CI-pipeline. Omdat elke repository er hetzelfde uitziet, is een engineer die naar een nieuw team wordt overgeplaatst binnen uren productief, en draaien organisatiebrede beveiligings- en afhankelijkheidsscanners uniform omdat ze bestanden altijd vinden waar ze ze verwachten.

**Overheid.** Een nationale instantie die verouderde systemen moderniseert schrijft een gemeenschappelijke repositoryindeling voor als onderdeel van haar leveringsstandaarden voor alle leveranciers. Elke repository moet een `specification`-map bevatten die code koppelt aan goedgekeurde vereisten, een gedocumenteerde README, een licentie- en beveiligingsbeleidsbestand in de root en een `deploy`-map met de infrastructure-as-code-definities (hoofdstuk 8.2). Omdat externen van verschillende leveranciers dezelfde structuur volgen, kunnen de auditors van de instantie compliance-artefacten in elk systeem op dezelfde manier vinden, en kost onderhoud op lange termijn nadat een contract eindigt veel minder omdat nieuwe onderhouders de kaart al kennen.

## Zakelijke onderbouwing: motivatie, ROI en TCO

De kosten van het invoeren van een structuurstandaard zijn grotendeels eenmalig: de indeling afspreken, de sjablonen bouwen en de conventie documenteren. De terugkerende kosten zijn laag, geconcentreerd in het onderhouden van de sjablonen en het besturen van uitzonderingen. De kosten van *geen* standaard hebben zijn terugkerend en stapelend: elke engineer die een onbekende repo opent betaalt een navigatiebelasting, elke onboarding verloopt trager en geautomatiseerde tooling moet per repo worden geconfigureerd omdat niets staat waar je het verwacht. In een grote organisatie vermenigvuldigen deze kleine wrijvingen zich tot serieuze verliezen aan engineeringtijd.

Het rendement toont zich als snellere onboarding, goedkopere mobiliteit tussen teams, meer signaal uit portfoliobrede tooling en, in gereguleerde omgevingen, lagere kosten voor audit en onderhoud op lange termijn, omdat artefacten altijd vindbaar zijn. De *total cost of ownership* (TCO, de volledige levensduurkosten van het bouwen, beheren en onderhouden van een systeem) daalt het meest in langlevende systemen, waar de onderhouders die van voorspelbare structuur profiteren meestal niet de auteurs zijn die haar creëerden. Formuleer structuur om het bestuur te overtuigen als een goedkope standaard met hoge hefboom die ontwikkelaarsproductiviteit en auditgereedheid verbetert, en geef de kosten van inconsistentie vandaag een getal met onboardingtijddata en de inspanning besteed aan het zoeken naar dingen in onbekende repositories.

## Antipatronen en valkuilen

- **De uitzonderingsrepository:** elke repo anders georganiseerd, zodat elke vanaf nul opnieuw geleerd moet worden.
- **De ontbrekende of verouderde README:** geen voordeur, waardoor nieuwkomers moeten uitzoeken hoe het project te bouwen en te draaien.
- **Structuur per document, niet per sjabloon:** een wikipagina beschrijft de standaardindeling, maar niets genereert of dwingt haar af, dus de werkelijkheid drijft ervan af.
- **Sjabloonafdrijving:** uit een sjabloon gegenereerde repositories wijken in de loop der tijd af en verbeteringen aan het sjabloon bereiken ze nooit.
- **Overgeconstrueerde hiërarchie:** diepe nesten van bijna lege mappen die ceremonie toevoegen zonder navigatie te helpen.
- **Vermengde verantwoordelijkheden:** broncode, tests, buildoutput en geheimen door elkaar zonder duidelijke scheiding.
- **Gecommitte buildoutput en lokale artefacten:** gegenereerde bestanden ingecheckt omdat ignoreregels nooit zijn opgezet, wat geschiedenis en diffs vervuilt.
- **Laagschendingen verborgen door vlakke structuur:** geen fysieke grenzen, zodat afhankelijkheidscycli en ongepaste koppeling ongemerkt insluipen.

## Volwassenheidsmodel

- **Niveau 1 (Initiëren):** Elke repository is ad hoc georganiseerd door haar auteurs, reagerend op wat het moment nodig heeft. Indelingen verschillen sterk, README's ontbreken of zijn onbetrouwbaar en nieuwkomers moeten bij elke repo met de hand worden rondgeleid.
- **Niveau 2 (Ontwikkelen):** Basisconventies bestaan informeel en veel repo's lijken op elkaar. Sommige teams houden een eigen startindeling aan. Maar er is geen gezaghebbende standaard, geen gedeelde scaffolding en structuur drijft merkbaar af van team tot team.
- **Niveau 3 (Standaardiseren):** Een gedocumenteerde, geversioneerde structuurstandaard wordt organisatiebreed gehandhaafd. Nieuwe repositories worden gegenereerd uit gedeelde sjablonen met een standaardindeling, README, configuratiebestanden en CI. Afwijkingen lopen via een gedocumenteerd uitzonderingsproces in plaats van stilletjes te gebeuren.
- **Niveau 4 (Beheersen):** Naleving van de standaard wordt gemeten en gestuurd met data: geautomatiseerde controles rapporteren welk deel van de repo's overeenkomt met de indeling, hoe ver gesjabloneerde repo's zijn afgedreven, volledigheid van README's en schendingen van afhankelijkheidsrichting, allemaal gevolgd aan de hand van uitgangswaarden. Onboarding- en navigatietijden worden gemeten, uitzonderingen worden gelogd en beoordeeld, en sjabloonwijzigingen worden op bewijs goedgekeurd in plaats van op mening.
- **Niveau 5 (Orkestreren):** Structuur wordt continu verbeterd en is adaptief: sjabloonverbeteringen planten zich automatisch voort naar bestaande repositories, structuurgovernance is geïntegreerd met beveiligings-, compliance- en platformtooling en de standaard evolueert bewust naarmate talen, architecturen en het portfolio verschuiven, waarbij uniformiteit hoog blijft terwijl de organisatie eromheen verandert.

## Ideeën voor discussie

- Welke mappen op het hoogste niveau moeten werkelijk universeel zijn in je organisatie, en welke optioneel?
- Hoe voorkom je dat uit een sjabloon gegenereerde repositories na verloop van tijd ervan afdrijven?
- Waar ligt de grens tussen een behulpzame, gelaagde hiërarchie en overgeconstrueerde mapceremonie?
- Hoe moet je structuurstandaard verschillen, zo al, tussen een monorepo en een multi-repo-aanpak?
- Wat is het juiste uitzonderingsproces voor een project waarvan de echte behoeften niet in de standaardindeling passen?
- Hoeveel van je structuur kan automatisch worden gecontroleerd, en wat leunt nog op menselijke review?
- Wie bezit de structuurstandaard en haar sjablonen, en hoe worden wijzigingen voorgesteld en uitgerold?

## Belangrijkste inzichten

- Organiseer elke repository zo dat elke engineer elke codebase op verwachting kan navigeren, volgens het principe van de minste verrassing.
- Neem een consistente indeling op het hoogste niveau aan (source, test, docs, build, deploy, scripts, examples, specification) en maak de README het startpunt.
- Check editor- en toolingconfiguratie (zoals `.editorconfig`) in zodat conventies actief zijn en niet alleen opgeschreven.
- Dwing structuur af met scaffolding en sjablonen zodat nieuwe repositories standaard correct zijn.
- Op schaal zit de waarde in uniformiteit: bestuur de standaard, beheer afdrijving en sta afwijkingen alleen toe via gedocumenteerde uitzonderingen.

## Referenties en verder lezen

- Robert C. Martin, *Clean Architecture: A Craftsman's Guide to Software Structure and Design*
- Steve McConnell, *Code Complete: A Practical Handbook of Software Construction*
- Andrew Hunt and David Thomas, *The Pragmatic Programmer*
- Titus Winters, Tom Manshreck, and Hyrum Wright (eds.), *Software Engineering at Google*
- Scott Chacon and Ben Straub, *Pro Git*
- EditorConfig project documentation (as a reference standard for editor configuration)
