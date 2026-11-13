# 2.6 Versiebeheer en broncodebeheer

## Overzicht en motivatie

Zie [versiebeheer](https://en.wikipedia.org/wiki/Version_control) als het register van je codebase. Het legt elke wijziging vast, inclusief wie haar maakte, wanneer en waarom, en laat veel mensen aan dezelfde software werken zonder elkaar te overschrijven. Voor een grote organisatie is het veel meer dan een back-up. Het is het fundament waarop samenwerking, [continuous integration](https://en.wikipedia.org/wiki/Continuous_integration) (CI), audit en releasebeheer rusten. De keuzes die je maakt over branching, repositorystructuur en commitdiscipline bepalen hoe snel je team kan bewegen, en hoe veilig.

Voor grote teams is broncodebeheer in feite een coördinatieprobleem op schaal. Wanneer honderden engineers wijzigingen in gedeelde code pushen, hebben ze een strategie nodig die samenvoegingen klein houdt, de hoofdlijn releasebaar houdt en de geschiedenis leesbaar houdt. Een team dat continu integreert stroomt soepel. Een team dat branches wekenlang laat afdrijven, schommelt van de ene integratiecrisis naar de volgende. Je repositorystructuur, één grote repo of vele, bepaalt ook hoe teams code delen en coördineren.

Omgevingen van onderneming en overheid voegen een paar eisen toe: traceerbaarheid, toegangsbeheer en bewaartermijnen. Een wijziging kan moeten verwijzen naar een goedgekeurd werkitem voor audit. Geheimen mogen nooit in de geschiedenis komen. Toegang tot repositories moet beveiligingsgrenzen respecteren. Hier worden je versiebeheerpraktijken deel van het beheersraamwerk van de organisatie, en een fout zoals een gelekt geheim of een niet-controleerbare geschiedenis kan ernstige gevolgen hebben.

## Kernprincipes

- Integreer vaak kleine wijzigingen. Lange divergentie is de wortel van samenvoegpijn.
- Houd de hoofdlijn altijd releasebaar.
- Geschiedenis is documentatie. Schrijf commits voor de toekomstige lezer die moet begrijpen waarom.
- Commit nooit geheimen. Behandel elk geheim dat de geschiedenis bereikt als gecompromitteerd.
- Automatiseer handhaving van hygiëne (hooks, CI-controles) in plaats van alleen op discipline te vertrouwen.
- Kies de repositorystructuur (mono tegenover poly) naar hoe teams werkelijk code delen en coördineren, niet naar mode.
- Koppel wijzigingen aan hun motivering (werkitems, tickets of beslissingen) voor traceerbaarheid.

## Aanbevelingen

### Geef de voorkeur aan trunk-based development met kortlevende branches

Neig naar [trunk-based development](https://en.wikipedia.org/wiki/Trunk-based_development): integreer vaak in een gedeelde hoofdlijn met kortlevende featurebranches gemeten in uren of dagen, niet weken. Korte branches houden samenvoegingen klein en integratie continu, en die gewoonte is sterk geassocieerd met hoge leveringsprestaties. Wanneer werk nog niet af is, parkeer het dan niet op een langlevende branch. Gebruik [functievlaggen](https://en.wikipedia.org/wiki/Feature_toggle), schakelaars op runtime die onafgemaakt werk verbergen, zodat je het in plaats daarvan veilig kunt samenvoegen. Bewaar langlevende releasebranches voor echte ondersteuning van meerdere versies, en ga erin met kennis van de onderhoudskosten die ze dragen.

### Kies een branchingmodel dat bij de releasecadans past

Stem je [branchingmodel](https://en.wikipedia.org/wiki/Branching_(version_control)) af op hoe je werkelijk uitrolt. Als je continu deployt, bedient trunk-based development met minimale branching je goed. Als je geversioneerde releases aan klanten levert, of meerdere live versies tegelijk ondersteunt, kun je releasebranches en backporting nodig hebben. Blijf weg van zware modellen met veel langlevende branches tenzij je releasemodel ze echt vereist, omdat ze de samenvoeg- en onderhoudsoverhead vermenigvuldigen.

### Besluit bewust tussen monorepo en polyrepo

Grijp naar een [monorepo](https://en.wikipedia.org/wiki/Monorepo), één repository met vele projecten, wanneer teams veel code delen, atomaire wijzigingen over projecten heen nodig hebben en uniforme tooling en zichtbaarheid willen. In ruil accepteer je de behoefte aan geschaalde buildtooling en toegangsbeheer. Grijp naar polyrepo's, aparte repositories per project of service, wanneer teams en services werkelijk onafhankelijk zijn, geïsoleerde toegang en releasecycli willen en geen atomaire wijzigingen over repo's heen nodig hebben. In ruil accepteer je de kosten van het coördineren van wijzigingen die repositories overspannen. Beide werken op schaal. Het is de verkeerde keuze voor jouw koppelingspatroon die constante wrijving veroorzaakt.

### Handhaaf commithygiëne en conventionele commits

Vraag om commitberichten die uitleggen waarom een wijziging is gemaakt, niet alleen wat. Neem een conventie aan zoals conventionele commits, zodat berichten gestructureerd en machineleesbaar zijn, wat je in staat stelt changelogs en versienummering te automatiseren. Houd commits atomair, één logische wijziging elk, zodat de geschiedenis bisecteerbaar en makkelijk terug te draaien blijft. Laat hooks en CI-controles berichtformaat en basale hygiëne afdwingen in plaats van op geheugen te leunen.

### Houd grote binaire bestanden en gegenereerde code uit de gewone geschiedenis

Commit geen grote binaire assets rechtstreeks in de hoofdgeschiedenis, omdat ze elke kloon voor altijd opblazen. Gebruik in plaats daarvan een mechanisme voor opslag van grote bestanden of een artefactrepository. Vermijd in de regel ook het committen van gegenereerde code. Genereer haar in de build. Wanneer je een gegenereerd artefact werkelijk moet committen, isoleer en markeer het duidelijk zodat het reviews en diffs niet vervuilt.

### Voorkom dat geheimen ooit de repository binnenkomen

Zet geautomatiseerde geheimenscans in je pre-commit hooks en CI, zodat inloggegevens worden geblokkeerd voordat ze ooit landen. Geef engineers een echt geheimenbeheersysteem, zodat ze nooit een inloggegeven hoeven te hardcoden. En behandel elk geheim dat de geschiedenis wel bereikt als gecompromitteerd: roteer het onmiddellijk. Zodra een geheim is gepusht en gekloond, is het uit de geschiedenis verwijderen moeilijk en onbetrouwbaar.

### Stel toegangsbeheer en traceerbaarheid in

Stel toegang tot repositories in zodat die beveiligingsgrenzen en [minste privilege](https://en.wikipedia.org/wiki/Principle_of_least_privilege) respecteert. Koppel commits of pull requests aan werkitems, zodat elke wijziging terug te voeren is op haar motivering, wat zowel de dagelijkse engineeringcontext als audit helpt. Bescherm je sleutelbranches met vereiste controles en reviews, zodat niets wordt samengevoegd zonder de poorten te passeren die je hebt afgesproken.

## Afwegingen: voor- en nadelen

| Keuze | Voordelen | Nadelen |
|---|---|---|
| Trunk-based development | Continue integratie. Kleine samenvoegingen. Hoge flow | Vraagt functievlaggen en discipline. Minder isolatie |
| Langlevende featurebranches | Sterke isolatie van werk in uitvoering | Pijnlijke samenvoegingen. Vertraagde integratie. Afdrijving |
| Monorepo | Atomaire wijzigingen over projecten. Gedeelde tooling. Zichtbaarheid | Vraagt geschaalde buildtooling. Standaard grof toegangsbeheer |
| Polyrepo | Onafhankelijke releases. Geïsoleerde toegang. Eenvoudige tooling per repo | Moeilijke wijzigingen over repo's. Overhead van versiecoördinatie |
| Conventionele commits | Geautomatiseerde changelogs en versienummering. Consistente geschiedenis | Conventie vooraf. Handhaving nodig |

De grote afweging hier is integratiefrequentie tegenover isolatie. Langlevende branches voelen veiliger omdat je werk apart staat, maar juist die isolatie veroorzaakt de dure samenvoegingen en integratieverrassingen later. Trunk-based development geeft dat gevoel van isolatie op in ruil voor continue, goedkope integratie, en vraagt je functievlaggen en discipline mee te brengen. De monorepo/polyrepo-beslissing ruilt gemak over projecten heen tegen teamonafhankelijkheid. Kies degene die past bij hoe sterk je code werkelijk gekoppeld is.

## Vragen om met je team te bespreken

1. **Welke controles moeten slagen voordat iets wordt samengevoegd met je beschermde hoofdlijn, en is die hoofdlijn werkelijk altijd releasebaar?** Dit hoofdstuk behandelt een releasebare hoofdlijn als kernprincipe en noemt een onbeschermde hoofdlijn, waar kapotte of onbeoordeelde code de branch bereikt waarvan iedereen afhangt, een antipatroon. In een groot team blokkeert een rode hoofdlijn iedereen tegelijk, dus de poort die je eist is een gedeelde veiligheidseigenschap, geen persoonlijke. Neem het bewijs mee: wat je branchebescherming vandaag daadwerkelijk afdwingt en hoe vaak de hoofdlijn nu kapot is. Bepaal de vereiste set, slagende tests, beveiligingsscans en review, en maak de hoofdlijn releasebaar door beleid in plaats van door hoop. Die poort is wat veel mensen continu laat integreren zonder angst.

2. **Is het aannemen van conventionele commits de conventie-overhead waard voor jouw team, gegeven wat ze automatiseert?** Het hoofdstuk beveelt gestructureerde, machineleesbare commitberichten aan juist omdat ze je changelogs en versienummering laten automatiseren, en vraagt om atomaire commits zodat de geschiedenis bisecteerbaar en terug te draaien blijft. De afweging is echt: je betaalt een conventie vooraf en hebt handhaving nodig, in ruil voor gegenereerde releasenotities en betrouwbare geschiedenis. Neem het signaal mee van wat je nu met de hand doet, zoals changelogs met de hand schrijven of zoeken welke commit een regressie introduceerde. Als je vaak released of meerdere versies onderhoudt, betaalt de automatisering zichzelf meestal terug. Als je zelden releases maakt, kan een lichtere conventie volstaan. Laat hooks en CI het formaat afdwingen, zodat het niet op geheugen leunt.

3. **Heb je de operationele kosten geaccepteerd die je repositorystructuur eist, of het nu gaat om monorepotooling of coördinatie over repo's heen?** Dit hoofdstuk zegt dat zowel monorepo als polyrepo op schaal werken, en dat de verkeerde keuze voor jouw koppelingspatroon constante wrijving veroorzaakt. Een monorepo vraagt geschaalde buildtooling en fijnmaziger toegangsbeheer, terwijl polyrepo's van elke wijziging die repositories overspant een coördinatieproject met risico op versiescheefheid maken. Neem het concrete signaal mee: hoe vaak je wijzigingen projectgrenzen overschrijden en of je build- en toegangstooling de structuur die je hebt kan dragen. Als atomaire wijzigingen over projecten heen gebruikelijk zijn, investeer dan in monorepotooling. Als teams en services werkelijk onafhankelijk zijn, accepteer de coördinatiekosten over repo's heen bewust. Het punt is de structuur af te stemmen op hoe sterk je code werkelijk gekoppeld is, en dan de tooling te financieren die die structuur vereist.

4. **Als nu een live inloggegeven in een drukke repository zou worden gecommit, hoe snel zou je het detecteren, en is rotatie daadwerkelijk automatisch in plaats van een hoop?** Dit hoofdstuk behandelt elk geheim dat de geschiedenis bereikt als gecompromitteerd en waarschuwt dat het later verwijderen moeilijk en onbetrouwbaar is, dus preventie en snelle rotatie zijn de enige echte verdedigingen. Voor een groot team stapelt de blootstelling zich op: een geheim gepusht naar een gedeelde repo wordt binnen minuten gekloond naar tientallen machines en gespiegeld in CI-caches, dus een trage menselijke reactie garandeert een inbreuk. De concurrerende overweging is wrijving: agressieve pre-commit-scans en geforceerde rotatie vertragen mensen en produceren valse positieven, dus je moet de controles tunen in plaats van ze uit te schakelen. Neem het bewijs mee: of geheimenscans zowel in pre-commit hooks als in CI draaien, je gemiddelde tijd om een bekend lek te detecteren en te roteren en of engineers zelfs een geheimenbeheersysteem hebben dat de verleiding om te hardcoden wegneemt. Koppel dit in omgevingen van onderneming en overheid aan je incidentproces en bewaarregels, omdat een gelekt inloggegeven in een controleerbare geschiedenis zowel een beveiligingsgebeurtenis als een compliancegebeurtenis is, en de toezichthouder zal vragen wie het wist en hoe snel ze handelden.

5. **Zijn je branches werkelijk kortlevend, en waar ze dat niet zijn, waarom wordt onafgemaakt werk op een branch geparkeerd in plaats van achter een functievlag verborgen?** Het hoofdstuk leunt sterk op trunk-based development omdat lange divergentie de wortel is van samenvoegpijn, en biedt functievlaggen als het mechanisme waarmee je onvolledig werk veilig kunt samenvoegen in plaats van het wekenlang te isoleren. In een groot team is dit een coördinatie-eigenschap, geen persoonlijke voorkeur: elke branch die weken leeft wordt een privévork van de werkelijkheid die iemand uiteindelijk moet verzoenen, en de kosten van die verzoening groeien met het aantal mensen. De concurrerende overweging is dat functievlaggen hun eigen kosten dragen, waaronder complexiteit op runtime, het testen van combinaties en verouderde vlaggen die moeten worden afgeschaft. Neem de data mee: je werkelijke verdeling van branchelevensduur, hoe vaak integratie conflicten of verrassingen oplevert en hoeveel langlevende branches er nu zijn en waarom. Voeg voor een grote of gereguleerde organisatie het releasebeeld toe, aangezien echte ondersteuning van meerdere versies langlevende releasebranches met gedisciplineerde backporting kan rechtvaardigen, en dat is een andere beslissing dan dagelijks functiewerk van de hoofdlijn af parkeren.

6. **Kan elke wijziging in je geschiedenis binnen de juiste beveiligingsgrenzen worden herleid naar haar auteur en haar motivering, en zou dat een audit doorstaan?** Dit hoofdstuk behandelt toegangsbeheer, minste privilege en het koppelen van wijzigingen aan werkitems als deel van het beheersraamwerk van de organisatie, niet als optionele afwerking. Voor een groot team is traceerbaarheid wat een ondoorzichtige stroom commits omzet in iets waarover je kunt redeneren tijdens een incident of compliancereview, en toegangsgrenzen zijn wat voorkomt dat één gecompromitteerd account code bereikt die het nooit mag raken. De concurrerende overweging is ontwikkelaarssnelheid: verplichte werkitemkoppelingen, fijnmazige rechten en vereiste reviews voegen ceremonie toe die een klein snel bewegend team redelijkerwijs zou kunnen overslaan. Neem het bewijs mee: of beschermde branches de controles en reviews vereisen die je beweert, of commits daadwerkelijk naar goedgekeurde werkitems verwijzen en hoe toegang vandaag aansluit op je echte beveiligingsgrenzen. Koppel dit in omgevingen van onderneming en overheid aan classificatie, bewaartermijnen en auditverplichtingen, omdat een niet-controleerbare geschiedenis of een te brede toegangstoekenning een bevinding wordt die een programma kan stilzetten of een accreditatie kan laten mislukken.

## Sectorperspectief

**Startup.** Snelheid en overleven winnen. Gebruik één repository, werk trunk-based, voeg kortlevende branches meerdere keren per dag samen en verberg onafgemaakt werk achter eenvoudige functievlaggen in plaats van langlevende branches. Zet geheimenscans aan vanaf de allereerste commit, omdat een gelekte sleutel in een publieke repo een bedrijf zonder beveiligingsteam om te beheersen kan laten zinken. Sla uitgebreide branchingmodellen en zwaar proces over. Een beschermde hoofdbranch en betekenisvolle commitberichten zijn genoeg discipline om snel te bewegen.

**Kleinbedrijf.** Zonder aparte platform- of DevOps-specialist en met een krap budget koop je de beheerde standaarden in plaats van ze te bouwen. Een gehoste Git-leverancier geeft je branchebescherming, vereiste reviews en geheimenscans kant-en-klaar, dus leun daarop in plaats van een server zelf te hosten die je niet kunt onderhouden. Formuleer de beslissing als datahygiëne: weet welke repositories gevoelige configuratie bevatten, bewaar inloggegevens in de geheimenbeheerder van de leverancier en laat het platform de paar regels afdwingen die je werkelijk nodig hebt.

**Grote onderneming.** Het moeilijke probleem is consistentie over veel teams. Standaardiseer branchebescherming, commitconventies en geheimenscans als organisatiebreed beleid zodat groepen ze niet opnieuw uitvinden, en maak de keuze tussen monorepo en polyrepo bewust per koppelingspatroon, waarbij je de geschaalde buildtooling of coördinatie over repo's heen financiert die het vraagt. Routeer wijzigingen naar de juiste reviewers met regels voor code-eigenaarschap, koppel commits aan werkitems voor traceerbaarheid en behandel versiebeheerhygiëne als een bestuurde beheersmaatregel met eigenaren en statistieken in plaats van een kwestie van individuele gewoonte.

**Overheid.** Aanbestedingsregels, transparantie en publieke verantwoording geven de hele opzet vorm. Eis dat elke commit naar een goedgekeurd werkitem verwijst, beheer toegang per classificatiegrens en maak geheimenscans en onmiddellijke rotatie verplicht onder een gedocumenteerd incidentproces. Ondersteun meerdere gedeployde versies met langlevende releasebranches en gedisciplineerde backporting waar locaties niet allemaal tegelijk kunnen upgraden, en houd de geschiedenis controleerbaar en bewaard zodat accreditatie-, openbaarheids- en toezichtsverzoeken kunnen worden beantwoord zonder haastwerk.

## Voorbeelden

**Startup.** Een startup van drie personen werkt trunk-based uit gewoonte en noodzaak, voegt kortlevende branches meerdere keren per dag samen in main en verbergt half afgemaakte functies achter eenvoudige vlaggen. Ze zetten geheimenscans in CI aan vanaf de eerste commit, omdat een gelekte API-sleutel in een publieke repo een bedrijf zonder beveiligingsteam om de gevolgen te beheersen kan laten zinken. Eén repository, een beschermde hoofdbranch en betekenisvolle commitberichten geven hen genoeg discipline om snel te bewegen zonder over hun eigen geschiedenis te struikelen.

**Grote onderneming.** Een groot technologiebedrijf draait een monorepo met honderden services en gedeelde bibliotheken. Geschaalde buildtooling en regels voor code-eigenaarschap routeren elke wijziging naar de juiste reviewers. Eén commit kan atomair een gedeelde bibliotheek en elke afnemer tegelijk bijwerken, wat de versiescheefheidsproblemen omzeilt die gedistribueerde repositories plagen. Trunk-based development met functievlaggen houdt de hoofdlijn releasebaar, en geheimenscans blokkeren inloggegevens bij commit over de hele repository.

**Overheid.** Een nationale defensieaannemer houdt zich aan strikte traceerbaarheid. Elke commit moet naar een goedgekeurd werkitem verwijzen. Branchebescherming vereist slagende beveiligingsscans en onafhankelijke review, en toegang wordt strak beheerd per classificatiegrens. Geheimenscans zijn verplicht, en elk blootgesteld inloggegeven triggert onmiddellijke rotatie onder een incidentproces. Langlevende releasebranches ondersteunen meerdere gedeployde versies over locaties die niet allemaal tegelijk kunnen upgraden, met gedisciplineerde backporting van beveiligingsfixes.

## Zakelijke onderbouwing: motivatie, ROI en TCO

Goed broncodebeheer is vrijwel gratis in te voeren en duur om zonder te zijn. Trunk-based development en continuous integration behoren tot de praktijken die het sterkst zijn geassocieerd met hoge softwareleveringsprestaties, die op hun beurt correleren met betere organisatieresultaten. Schone, traceerbare geschiedenis verkort de tijd om incidenten te diagnosticeren en aan audits te voldoen, en gedisciplineerde branching bespaart je de terugkerende, niet begrote kosten van integratiecrises en samenvoegmarathons.

Het grootste scheve risico zijn geheimen in versiebeheer. Eén gelekt inloggegeven kan een inbreuk veroorzaken waarvan de kosten elke toolinginvestering verbleken, en de geschiedenis laat zulke lekken blijven hangen. Ze voorkomen is goedkoop. Ze opruimen is dat niet. Slechte structuurkeuzes blijken uit chronische wrijving: elke wijziging over repo's heen wordt een coördinatieproject, of elke monorepobuild wordt een knelpunt. Verbind je branchingstrategie om het bestuur te overtuigen aan leveringsstatistieken en de tijd om incidenten te diagnosticeren, en formuleer geheimenscans en toegangsbeheer als goedkope beheersmaatregelen tegen kostbare inbreuk- en auditrisico's.

## Antipatronen en valkuilen

- **Langlevende afdrijvende branches:** weken geïsoleerd werk dat samenvoegt in pijnlijke, riskante integratiegebeurtenissen.
- **Geheimen in de geschiedenis:** hardgecodeerde inloggegevens die voor altijd in klonen blijven en rotatie vereisen zodra ze zijn blootgesteld.
- **Grote binaire bestanden in de hoofdgeschiedenis committen:** elke kloon blijvend opblazen en alle operaties vertragen.
- **Betekenisloze commitberichten:** "fix", "wip", "changes" die de waarde van de geschiedenis als documentatie vernietigen.
- **Gegenereerde code committen alsof ze met de hand is geschreven:** rumoerige diffs, samenvoegconflicten en verwarring over de bron van waarheid.
- **Verkeerde repostructuur voor de koppeling:** polyrepo's voor strak gekoppelde code, of monorepo's zonder geschaalde tooling.
- **Onbeschermde hoofdlijn:** geen vereiste controles, zodat kapotte of onbeoordeelde code de branch bereikt waarvan iedereen afhangt.

## Volwassenheidsmodel

- **Niveau 1, Initiëren:** Ad hoc en reactief. Branching wordt geïmproviseerd, branches leven weken, commitberichten zeggen "fix" of "wip", er is geen geheimenscan en integratie schommelt van de ene samenvoegcrisis naar de volgende.
- **Niveau 2, Ontwikkelen:** Basispraktijken verschijnen maar verschillen per team. Een branchingmodel en berichtconventies bestaan op plaatsen, maar branches leven nog te lang, handhaving is gedeeltelijk, geheimenscans zijn onvolledig en de repostructuur is geërfd in plaats van gekozen.
- **Niveau 3, Standaardiseren:** Praktijken zijn gedocumenteerd en organisatiebreed gehandhaafd: trunk-based development met korte branches, een beschermde en altijd releasebare hoofdlijn, afgedwongen commitconventies, geheimenscans in zowel hooks als CI, toegang met minste privilege en een bewuste keuze voor monorepo of polyrepo.
- **Niveau 4, Beheersen:** Broncodepraktijken worden gemeten en gestuurd met data. Je volgt levensduur van branches, integratiefrequentie, percentage verbroken hoofdlijn, gemiddelde tijd om een gelekt geheim te detecteren en te roteren en traceerbaarheid van wijziging naar werkitem tegen overeengekomen uitgangswaarden, en je handelt wanneer de cijfers afdrijven in plaats van op het volgende incident te wachten.
- **Niveau 5, Orkestreren:** Praktijken worden continu verbeterd en zijn over de organisatie geïntegreerd. Branching, repostructuur en tooling passen zich aan naarmate teams en codekoppeling veranderen, automatisering handhaaft hygiëne van begin tot eind en versiebeheerdata voedt levering-, beveiligings- en risicobeslissingen organisatiebreed.

## Ideeën voor discussie

- Is de branchelevensduur van je team werkelijk kort, en zo niet, wat verhindert continue integratie?
- Komt je keuze voor monorepo of polyrepo overeen met hoe gekoppeld je code werkelijk is?
- Hoe ga je vandaag om met grote binaire bestanden en gegenereerde artefacten, en wat kost het je?
- Wat zou er gebeuren als nu een live inloggegeven werd gecommit, en hoe snel zou je het detecteren en roteren?
- Hoeveel commitbericht- en traceerbaarheidsdiscipline is het waard af te dwingen voor jouw context?
- Hoe veranderen functievlaggen je branchingstrategie, en welke nieuwe risico's introduceren ze?

## Belangrijkste inzichten

- Integreer vaak met kortlevende branches. Lange divergentie veroorzaakt de pijn die ze lijkt te vermijden.
- Houd de hoofdlijn releasebaar en beschermd door vereiste controles.
- Laat nooit geheimen de geschiedenis binnenkomen. Scan automatisch en roteer onmiddellijk als ze dat toch doen.
- Kies monorepo of polyrepo naar je echte koppeling en coördinatiebehoeften.
- Behandel commitgeschiedenis als documentatie, met betekenisvolle, conventionele, atomaire commits.

## Referenties en verder lezen

- Nicole Forsgren, Jez Humble, Gene Kim, *Accelerate: The Science of Lean Software and DevOps*
- Jez Humble and David Farley, *Continuous Delivery*
- Scott Chacon and Ben Straub, *Pro Git*
- Paul Hammant and others, writings on trunk-based development
- Conventional Commits specification (as a reference standard)
- Martin Fowler, articles on branching patterns and continuous integration
