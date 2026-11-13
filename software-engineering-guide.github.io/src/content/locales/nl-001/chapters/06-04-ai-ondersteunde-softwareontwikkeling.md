# 6.4 AI-ondersteunde softwareontwikkeling

## Overzicht en motivatie

AI-codeerassistenten kunnen nu code genereren, functies aanvullen, tests schrijven, onbekende systemen uitleggen en je helpen bij het [refactoren](https://en.wikipedia.org/wiki/Code_refactoring). Goed gebruikt versnellen ze routinewerk. Ze verlagen de drempel tot onbekende talen en frameworks. Ze nemen het sleurwerk uit boilerplate.

Slecht gebruikt richten ze echte schade aan. Ze kunnen een codebasis overspoelen met plausibel ogende maar subtiel foute code. Ze kunnen beveiligingslekken introduceren, licentieblootstelling creëren en de vaardigheden eroderen van de engineers die erop leunen. AI-ondersteunde ontwikkeling is tegelijk een echt productiviteitsgereedschap en een echt risico. Het verschil zit bijna volledig in de engineeringdiscipline eromheen.

Voor grote teams is de uitdaging consistentie en veiligheid op schaal. Wanneer honderden ontwikkelaars AI-assistenten gebruiken, tellen kleine individuele gewoonten op tot organisatorische uitkomsten. Als iedereen suggesties kritiekloos accepteert, stijgen reviewlast en defectpercentages. Als je heldere normen, goede standaarden en sterke verificatie biedt, verhogen dezelfde tools de doorvoer zonder de kwaliteit te verlagen. Het productiviteitsverhaal is ook genuanceerder dan leveranciersclaims suggereren. Echte winst verschilt sterk per taak, en naïeve meting, zoals geaccepteerde suggesties tellen, zal je misleiden.

Omgevingen van onderneming en overheid voegen scherpere beperkingen toe. Code die gereguleerde systemen raakt, gevoelige data verwerkt of kritieke infrastructuur draait kan niet worden vertrouwd alleen omdat een AI haar produceerde. Licentieherkomst telt wanneer gegenereerde code trainingsdata onder restrictieve licenties kan echoën. Sommige organisaties moeten broncode on-premises houden en kunnen haar helemaal niet naar externe diensten sturen. Heldere, afdwingbare normen voor AI-ondersteuning vaststellen is nu onderdeel van verantwoord engineeringleiderschap. Onder de beschikbare assistenten zijn tools gebouwd op de Claude-modellen van Anthropic één toonaangevende optie naast andere. De praktijken hieronder gelden welke je ook kiest.

*Zie ook:* hoofdstuk 2.5 (codereview en samenwerking), hoofdstuk 2.4 (teststrategie) en hoofdstuk 6.5 (verantwoorde en betrouwbare AI).

## Kernprincipes

- De engineer, niet de assistent, is verantwoordelijk voor elke gecommitte regel.
- AI-gegenereerde code is een concept om te beoordelen en te verifiëren, nooit een afgewerkt product om te vertrouwen.
- Verificatie-inspanning moet schalen met het risico van de code, niet met hoe zelfverzekerd de uitvoer eruitziet.
- Meet productiviteit aan uitkomsten die tellen (geleverde waarde, kwaliteit, doorlooptijd), niet aan aantallen suggesties.
- Bescherm tegen beveiligings- en licentierisico's geïntroduceerd via gegenereerde code.
- Behoud en kweek menselijke engineeringvaardigheid. Laat assistenten haar niet uithollen.
- Wees transparant over waar en hoe AI-ondersteuning wordt gebruikt.

## Aanbevelingen

### Gebruik AI-pairprogramming als opstel- en verkenningstool

Richt assistenten op taken waar ze uitblinken en fouten goedkoop te vangen zijn: boilerplate, testskeletten, formaatconversies, onbekende code uitleggen en benaderingen verkennen. Behandel hun uitvoer als eerste concept. Blijf op de bestuurdersstoel zitten. Lees, begrijp en bewerk elke suggestie in plaats van op de automatische piloot te accepteren. Gebruik de assistent in onbekende domeinen om te leren, maar controleer zijn beweringen tegen gezaghebbende documentatie. Assistenten kunnen API's verzinnen en gedrag verkeerd weergeven met volledige zelfverzekerdheid.

### Beoordeel, test en verifieer AI-gegenereerde code als onbetrouwbare invoer

Geef AI-gegenereerde code dezelfde toetsing als code van een nieuw teamlid, of meer. Een menselijke reviewer moet haar goed genoeg begrijpen om haar uit te leggen en te onderhouden. "De AI schreef het" is nooit een acceptabel antwoord op "waarom werkt dit?" Sta op tests, en let op AI-gegenereerde tests die slechts huidig gedrag bevestigen in plaats van beoogd gedrag. Draai [statische analyse](https://en.wikipedia.org/wiki/Static_program_analysis), beveiligingsscanning en afhankelijkheidscontroles. Behandel voor code met hoog risico (authenticatie, [cryptografie](https://en.wikipedia.org/wiki/Cryptography), financiële logica, veiligheidssystemen) AI-uitvoer als startpunt dat deskundige menselijke verificatie eist, nooit als gezaghebbend.

### Meet productiviteit eerlijk en stel realistische verwachtingen

Sla ijdele statistieken als acceptatiepercentage of gegenereerde regels over. Kijk in plaats daarvan naar lever- en kwaliteitssignalen in de tijd: doorlooptijd, wijzigingsfaalpercentage, defectontsnappingspercentage en door ontwikkelaars gerapporteerde effectiviteit. Winst is echt maar ongelijk: groot voor sommige taken, verwaarloosbaar of negatief voor andere. Tijd bespaard bij het schrijven van code kan opnieuw verloren gaan bij het beoordelen en debuggen ervan. Stel verwachtingen dienovereenkomstig met leiderschap, zodat investering op bewijs rust in plaats van hype, en teams nooit onder druk worden gezet onveilige suggesties te accepteren om een statistiek te halen.

### Beheer beveiligings- en licentierisico's

Scan gegenereerde code op kwetsbaarheden en onveilige patronen. Assistenten kunnen onveilige idiomen uit hun trainingsdata reproduceren. Plak nooit geheimen, inloggegevens of gevoelige data in prompts die naar externe diensten gaan. Geef de voorkeur aan tools die aan je eisen voor gegevensverwerking voldoen, inclusief on-premises of private deployment waar broncode de omgeving niet mag verlaten. Pak ook licenties aan. Gegenereerde code kan op gelicentieerde trainingsdata lijken, dus gebruik tools en beleid die dit risico verkleinen, bewaar herkomst waar je kunt en leid alles wat twijfelachtig is door juridische review. Volg de herkomst van afhankelijkheden die de assistent voorstelt, want hij kan verlaten of kwaadaardige pakketten aanbevelen.

### Stel teamnormen, openbaarmaking en vaardigheidsonderhoud vast

Publiceer heldere richtlijnen over wanneer en hoe AI-ondersteuning mag worden gebruikt, welke data nooit gedeeld mag worden en welke verificatie elk risiconiveau vereist. Moedig transparantie aan over AI-ondersteunde bijdragen waar het ertoe doet voor review en verantwoording. Houd menselijke vaardigheden met opzet scherp. Zorg dat engineers, vooral junioren, de fundamenten nog leren in plaats van hun begrip uit te besteden. Roteer mensen door werk dat diepe expertise bouwt en behandel overmatige afhankelijkheid als echt langetermijnrisico voor het vermogen van het team.

## Afwegingen: voor- en nadelen

| Dimensie | Voordeel van AI-ondersteuning | Risico van AI-ondersteuning |
|---|---|---|
| Snelheid | Snellere boilerplate en concepten | Tijd verloren aan het beoordelen van foute code |
| Onboarding | Makkelijker instappen in nieuwe talen/frameworks | Oppervlakkig begrip, verzonnen API's |
| Kwaliteit | Meer tests, snellere refactors | Plausibele maar subtiel foute code |
| Beveiliging | Kan reparaties en scanning voorstellen | Kan kwetsbaarheden introduceren |
| Vaardigheden | Maakt tijd vrij voor werk met hogere waarde | Erodeert fundamenten bij overmatig gebruik |
| Licenties | Sneller hergebruik van gangbare patronen | Herkomst en licentieblootstelling |

De centrale afweging is snelheid tegenover verificatie. AI verschuift inspanning van schrijven naar beoordelen. De nettowinst hangt af van of je review- en verificatiepraktijken sterk genoeg zijn om te vangen wat de assistent fout doet. Zwakke review leidt tot kwaliteitsverval. Sterke review en heldere normen vangen het voordeel.

## Vragen om met je team te bespreken

1. **Welke delen van onze codebasis zijn helemaal verboden terrein voor AI-ondersteuning, en hoe dwingen we die grens af?** Uniform vertrouwen is een valstrik: dezelfde lichte toetsing toepassen op authenticatie, cryptografie, financiële logica en veiligheidssystemen als op boilerplate is hoe subtiele, zelfverzekerde fouten kritieke paden bereiken. Voor een groot team verandert een expliciete lijst van uitgesloten of alleen-door-experts-te-beoordelen modules individueel oordeel in een organisatorische waarborg. Neem je risicokaart van de codebasis mee, je huidige beleid (als je er een hebt) en hoe je gegenereerde code werkelijk zou tegenhouden in een beperkte module te landen: pijplijncontroles, eigenaarschapsregels of reviewpoorten. In defensie-, gereguleerde en veiligheidskritieke omgevingen moeten sommige modules AI-ondersteuning volledig uitsluiten. Het antwoord moet verificatie-inspanning schalen naar het risico van de code, nooit naar hoe zelfverzekerd de uitvoer eruitziet.

2. **Wat zijn onze echte trends in wijzigingsfalen en defectontsnapping sinds we assistenten adopteerden, en meten we ze of gokken we?** Productiviteitsclaims van leveranciers en tellingen van acceptatiepercentages zijn ijdele statistieken die misleiden, omdat tijd bespaard bij het schrijven van code opnieuw verloren kan gaan bij het beoordelen en debuggen. Om leiderschap op bewijs in plaats van hype te laten investeren heb je lever- en kwaliteitssignalen in de tijd nodig: doorlooptijd, wijzigingsfaalpercentage, defectontsnappingspercentage en door ontwikkelaars gerapporteerde effectiviteit. Neem alle echte getallen mee die je hebt, en wees eerlijk waar je er geen hebt. Het risico om op te letten is teams onder druk die onveilige suggesties accepteren om een statistiek te halen. Het antwoord moet suggestietellingen vervangen door uitkomstmaten, en verwachtingen stellen dat winst echt maar ongelijk is, groot voor sommige taken en negatief voor andere.

3. **Als gegenereerde code restrictief gelicentieerde trainingsdata echoot of een riskante afhankelijkheid binnenhaalt, wie vangt dat en wanneer?** Gegenereerde code kan op gelicentieerd materiaal lijken of verlaten of kwaadaardige pakketten aanbevelen, en die blootstelling landt in je product of iemand het opmerkte of niet. Voor ondernemingen en overheid dragen licentieherkomst en toeleveringsketenrisico juridisch gewicht dat een "de AI schreef het"-schouderophaal niet overleeft. Neem je huidige geheimenscanning, licentiecontroles en tracking van afhankelijkheidsherkomst mee en identificeer waar in de pijplijn elk draait. Bespreek wat twijfelachtige code naar juridische review leidt en wie die beslissing bezit. Als geheimen in externe tools geplakt kunnen worden of niet-gecontroleerde pakketten ongehinderd kunnen mergen, dicht die gaten dan voordat je assistentgebruik over het team opschaalt.

4. **Hoe houden we engineers, vooral junioren, de fundamenten laten leren in plaats van hun begrip aan de assistent uit te besteden?** Vaardigheidsverval is een langzaam risico dat nooit in de snelheid van dit kwartaal verschijnt, en jaren later verschijnt als een team dat zonder prompt niet kan debuggen, ontwerpen of beoordelen. Voor een grote organisatie is de concurrerende trek echt: assistenten laten junior engineers vandaag sneller opleveren, en de druk om leveringsdoelen te halen vecht tegen het tragere werk van diepe expertise bouwen. Neem bewijs mee van hoe je mensen werkelijk groeien: welk deel van de junioren kan uitleggen welke code ze mergden, hoeveel zelfstandig probleemoplossen je onboarding nog vereist en of reviews oppervlakkig begrip vangen of werkende uitvoer slechts afstempelen. Roteer mensen bewust door werk dat meesterschap bouwt en behandel overmatige afhankelijkheid als vermogensrisico, niet persoonlijk falen. Bij de overheid en langlevende kritieke systemen moet het personeel decennia lang systemen kunnen bouwen en verifiëren zonder leverancierstools, dus een opleidingspad dat directe fundamenten garandeert is een continuïteitseis, geen aardigheid.

5. **Welke assistenten mogen we werkelijk gebruiken gezien waar onze broncode en data moeten blijven, en hoe voorkomen we dat ooit een geheim een prompt bereikt?** Eisen voor gegevensverwerking bepalen de tool vóór productiviteit: een assistent die je bron naar een externe dienst streamt kan meteen gediskwalificeerd zijn, wat zijn vermogens ook zijn. Voor een groot team is de spanning tussen het gemak van de beste gehoste tool en de eis dat bedrijfseigen code, inloggegevens en gevoelige data je grens nooit verlaten. Neem je dataclassificatiekaart mee, de deploymentopties die elke kandidaattool biedt (gehost, privé, on-premises) en de concrete maatregelen die geheimen uit prompts houden: pre-commit-scanning, promptfiltering en engineerstraining. Besluit welke tools zijn toegestaan voor welke klassen code en maak de grens afdwingbaar in plaats van adviserend. In gereguleerde, defensie- en geclassificeerde omgevingen kan een on-premises of air-gapped deployment de enige wettelijke optie zijn, en broncode naar een externe dienst sturen moet worden verboden en technisch geblokkeerd, niet slechts ontmoedigd.

6. **Hoe maken we van verspreide individuele gewoonten consistente organisatiebrede normen, en wie bezit het beleid naarmate tools evolueren?** Wanneer honderden ontwikkelaars elk hun eigen aanpak improviseren, tellen kleine gewoonten op tot organisatorische uitkomsten, en inconsistente verificatie is waar defecten en blootstelling doorglippen. De concurrerende overweging is autonomie: teams ergeren zich aan zware centrale mandaten, maar een vrije-voor-allen levert ongelijke kwaliteit en geen gedeelde waarborg op. Neem je huidige richtlijnen mee (als je ze hebt), bewijs van hoe uniform ze worden gevolgd en een voorstel voor goede standaarden ingebakken in de pijplijn zodat het veilige pad het makkelijke pad is. Noem een eigenaar die het beleid actueel houdt naarmate assistenten om de paar maanden veranderen, en een openbaarmakingsnorm zodat reviewers weten wanneer AI-ondersteuning een bijdrage vormde. Koppel de normen voor een onderneming of publiek orgaan aan audit en verantwoording: een gedocumenteerde, afgedwongen standaard die een auditor kan inspecteren verslaat een volkspraktijk die per team varieert en verdwijnt wanneer een sleutelpersoon vertrekt.

## Sectorperspectief

**Startup.** Met een handvol engineers en geen runway om te verspillen leun je op gehoste assistenten voor boilerplate, tests en onbekende frameworks, en laat je ze routinewerk versnellen. Houd één niet-onderhandelbare regel: een mens die de wijziging begrijpt beoordeelt elke merge, want een subtiele foute regel in een codebasis van vijf mensen heeft nergens om zich te verbergen en niemand anders om haar te vangen. Voeg vroeg een geheimenscanner en een licentiecontrole toe. Ze zijn goedkoop en voorkomen dure fouten die je je later niet kunt veroorloven op te ruimen.

**Kleinbedrijf.** Je hebt waarschijnlijk geen beveiligingsspecialist en een krap budget, dus geef de voorkeur aan assistenten ingebed in tools die je al vertrouwt boven een maatwerkopzet die je moet onderhouden. Formuleer het risico in gewone termen: plak nooit klantdata of inloggegevens in een externe prompt en behandel gegenereerde code die facturering of authenticatie raakt als concept om te verifiëren, niet een afgewerkt antwoord. Kies leveranciers wier voorwaarden voor gegevensverwerking je werkelijk kunt lezen en wier AI-functies je kunt uitzetten als ze zich misdragen.

**Grote onderneming.** Het probleem is consistentie en veiligheid over veel teams: gedeelde normen per risiconiveau, verplichte review en scanning in de pijplijn en eerlijke lever- en kwaliteitsstatistieken in plaats van acceptatietellingen. Standaardiseer de toolkeuzes en het deploymentmodel zodat bedrijfseigen code binnen je grens blijft, begroot de review- en correctiekosten die assistenten op reviewers afwentelen en sluit risicovolle modules expliciet uit of poort ze. Beheer AI-ondersteuning als bestuurd vermogen met een eigenaar, niet een verstrooiing van individuele gewoonten.

**Overheid.** Aanbestedingsregels, transparantie en publieke verantwoording geven elke keuze vorm. Geef de voorkeur aan on-premises of private deployment waar broncode en gevoelige data de omgeving niet mogen verlaten, verbied code naar externe diensten te sturen en eis openbaarmaking van AI-ondersteunde bijdragen zodat beslissingen controleerbaar blijven. Schrijf beveiligings- en licentiescans voor op alle gegenereerde code, sluit AI-ondersteuning uit van veiligheidskritieke en geclassificeerde modules en houd een opleidingspad aan dat verzekert dat het publieke personeel systemen kan bouwen en verifiëren zonder leverancierstools over de lange levensduur van de systemen die het bezit.

## Voorbeelden

**Startup.** Een SaaS-startup van zes engineers adopteerde AI-codeerassistenten om sneller te gaan op routinewerk. Ze leunde erop voor boilerplate, tests en code voor onbekende frameworks, maar hield een vaste regel dat een mens die de wijziging begreep elke pull request moest beoordelen, en voegde een geheimenscanner en licentiecontrole toe aan de pijplijn. Voor de factureringscode en authenticatie behandelden engineers AI-uitvoer als ruw concept om regel voor regel te verifiëren in plaats van te vertrouwen. Ze volgden doorlooptijd en ontsnapte defecten in plaats van geaccepteerde suggesties te tellen en behielden de winst zonder dat de kwaliteit wegzakte.

**Grote onderneming.** Een groot e-commercebedrijf rolde AI-codeerassistenten uit met vangrails. Het verbood geheimen in prompts. Het eiste menselijke review, waarbij van de reviewer werd verwacht dat hij de code begreep. Het voegde beveiligingsscanning toe in de pijplijn en koos een private deployment zodat bedrijfseigen code zijn omgeving nooit verliet. Het mat impact via doorlooptijd en wijzigingsfaalpercentage in plaats van acceptatietellingen. Het vond solide winst op boilerplate en tests, maar stond op deskundige review voor betaalcode, waar het AI-uitvoer als onbetrouwbaar behandelde.

**Overheid.** Een defensiesoftwareorganisatie stond AI-ondersteuning alleen toe via een on-premises tool die geclassificeerde en gevoelige code binnen haar grens hield. Ze verbood bron naar enige externe dienst te sturen. Ze eiste openbaarmaking van AI-ondersteunde bijdragen bij codereview en schreef beveiligings- en licentiescans voor op alle gegenereerde code. Ze sloot AI-ondersteuning volledig uit van bepaalde veiligheidskritieke modules. Junior engineers volgden een opleidingspad dat verzekerde dat ze fundamenten direct leerden, zodat het personeel het vermogen niet zou verliezen systemen zonder ondersteuning te bouwen en te verifiëren.

## Zakelijke onderbouwing: motivatie, ROI en TCO

De motivatie is snellere oplevering en minder sleurwerk, zodat je schaarse engineeringtalent zich kan richten op ontwerp, oordeel en moeilijke problemen. ROI toont zich als verkorte doorlooptijd voor geschikte taken en verbeterde ontwikkelaarservaring, maar alleen waar verificatie de kwaliteit hoog houdt. Naïeve ROI-claims gebaseerd op suggestietellingen zijn misleidend, en je moet ze afwijzen.

De TCO omvat toollicenties, beveiligde of on-premises deployment, beveiligings- en licentiescanning en de vaak onderschatte kosten van AI-uitvoer beoordelen en corrigeren. De kosten van *niet* adopteren zijn competitief: peers kunnen sneller leveren en talent aantrekken dat moderne tools verwacht. De kosten van onzorgvuldig adopteren zijn kwaliteitsverval, beveiligingsincidenten en juridische blootstelling. Maak de zaak voor het bestuur met een pilot die echte lever- en kwaliteitsuitkomsten meet, gekoppeld aan een concreet plan voor normen, verificatie en gegevensbescherming.

## Antipatronen en valkuilen

- **Acceptatie op de automatische piloot.** Suggesties committen zonder ze te lezen of te begrijpen.
- **Ijdele statistieken.** Succes beoordelen aan acceptatiepercentage of gegenereerde regels.
- **Geheimen in prompts.** Inloggegevens of gevoelige data in externe tools plakken.
- **AI-tests vertrouwen.** Gegenereerde tests accepteren die huidig gedrag vastleggen, niet beoogd gedrag.
- **Herkomst negeren.** Licentie- en afhankelijkheidsrisico's in gegenereerde code over het hoofd zien.
- **Vaardigheidsverval.** Junioren hun begrip laten uitbesteden en nooit fundamenten laten leren.
- **Uniform vertrouwen.** Dezelfde lage toetsing toepassen op veiligheidskritieke code als op boilerplate.

## Volwassenheidsmodel

1. **Initiëren.** Individuen gebruiken assistenten ad hoc en reactief. Geen beleid, geen meting. Geheimen en intellectueel eigendom lopen risico, en gegenereerde code merged met welke toetsing elke persoon toevallig toepast.
2. **Ontwikkelen.** Basisgebruiksrichtlijnen en dataregels bestaan en enige beveiligingsscanning draait, maar de praktijk is inconsistent over teams: verificatiediepte varieert per persoon, productiviteitsclaims zijn anekdotisch en code met hoog risico wordt niet betrouwbaar gepoort.
3. **Standaardiseren.** Normen per risiconiveau zijn gedocumenteerd en organisatiebreed afgedwongen: verplichte menselijke review, beveiligings- en licentiescans in de pijplijn, beveiligde of on-premises deployment waar vereist, openbaarmakingspraktijken en een expliciete lijst van uitgesloten of alleen-door-experts-te-beoordelen modules.
4. **Beheersen.** De praktijk wordt gemeten en beheerst aan de hand van uitgangswaarden: doorlooptijd, wijzigingsfaalpercentage en defectontsnappingspercentage worden vóór en na adoptie gevolgd, review- en correctiekosten worden gekwantificeerd, incidenten van geheimenlekken en licentieblootstelling worden geteld en go/no-go-beslissingen over tools en uitbreiding rusten op dat bewijs in plaats van leveranciersclaims.
5. **Orkestreren.** AI-ondersteuning wordt continu verbeterd en over de organisatie geïntegreerd: verificatie is als standaardpad in de pijplijn ingebouwd, vaardigheidsontwikkeling is bewust en gevolgd, beleid past zich aan naarmate tools elke paar maanden veranderen en de organisatie herevalueert, vervangt en bakent assistenten routinematig opnieuw af naarmate het bewijs en het risicobeeld verschuiven.

## Ideeën voor discussie

- Hoe moeten verificatie-eisen verschillen tussen boilerplate en veiligheidskritieke code?
- Welke productiviteitsstatistieken weerspiegelen werkelijk waarde van AI-ondersteuning in jouw context?
- Wanneer, als ooit, moeten AI-ondersteunde bijdragen worden bekendgemaakt?
- Hoe voorkom je vaardigheidsverval, vooral bij junior engineers?
- Welke beperkingen op gegevensverwerking bepalen welke tools je mag gebruiken?
- Hoe beheer je licentie- en herkomstrisico van gegenereerde code?

## Belangrijkste inzichten

- De engineer blijft verantwoordelijk. AI-uitvoer is een onbetrouwbaar concept om te verifiëren.
- Schaal verificatie naar risico en vertrouw nooit veiligheidskritieke AI-code zonder deskundige review.
- Meet echte lever- en kwaliteitsuitkomsten, geen suggestietellingen.
- Bescherm tegen beveiligings-, datalek- en licentierisico's met beleid en tooling.
- Stel heldere normen vast en behoud bewust menselijke engineeringvaardigheid.

## Referenties en verder lezen

- Nicole Forsgren, Jez Humble, and Gene Kim, *Accelerate: The Science of Lean Software and DevOps*.
- Andrew Ng, *Machine Learning Yearning* (on realistic expectations and measurement).
- OWASP Foundation, *OWASP Top 10 for Large Language Model Applications*.
- Peter Naur, *Programming as Theory Building* (on understanding versus code artifacts).
- Titus Winters, Tom Manshreck, and Hyrum Wright, *Software Engineering at Google*.
- GitClear and related industry studies on AI-assisted code quality trends.
