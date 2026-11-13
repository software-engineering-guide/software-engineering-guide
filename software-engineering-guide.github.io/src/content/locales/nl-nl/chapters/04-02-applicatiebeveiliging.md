# 4.2 Applicatiebeveiliging

## Overzicht en motivatie

Applicatiebeveiliging is waar abstracte dreigingen concrete code ontmoeten. De meeste inbreuken die de krantenkoppen halen herleiden naar een fout in de applicatielaag: een injectie, een kapotte authenticatiestroom, een blootgesteld geheim of een gecompromitteerde afhankelijkheid. Voor grote teams die veel services opleveren is het moeilijke deel niet weten dat deze fouten bestaan. Het is ze consistent voorkomen over een uitdijende codebase geschreven door duizenden handen over vele jaren.

Voor ondernemingen is applicatiebeveiliging een kwestie van klantvertrouwen en regelgevende verplichting. Een fout in een inlogstroom of een betaalpad kan fraude, boetes en verplichte inbreukmelding triggeren. Overheidssystemen kennen dezelfde technische risico's met data met hogere inzet: uitkeringsgeschiktheid, belastingrecords, strafrechtelijke data en nationale infrastructuur. In beide settings is de applicatie de voordeur, en aanvallers tasten haar constant en automatisch.

Dit hoofdstuk behandelt de praktijken die applicaties veerkrachtig houden: de veelvoorkomende kwetsbaarheidsklassen kennen en verdedigen, invoer valideren en uitvoer coderen, authenticatie en autorisatie goed krijgen, geheimen beheren en de softwaretoeleveringsketen beveiligen die steeds vaker je werkelijke aanvalsoppervlak bepaalt.

*Zie ook:* hoofdstuk 4.1 (beveiligingsfundamenten, dreigingsmodellering en de veilige ontwikkellevenscyclus), hoofdstuk 10.3 (open-sourcetoeleveringsketen en licenties) en hoofdstuk 10.2 (SBOM's, risico en zekerheid).

## Kernprincipes

- **Vertrouw invoer nooit.** Behandel alle data die een vertrouwensgrens overschrijdt als vijandig tot gevalideerd.
- **Veilige standaarden.** Het veilige pad moet het makkelijke pad zijn. Onveilig gedrag moet bewuste, zichtbare inspanning vragen.
- **Faal gesloten.** Wanneer een beveiligingscontrole niet kan worden voltooid, weiger toegang in plaats van haar te verlenen.
- **Verdediging in de diepte op appniveau.** Combineer validatie, codering, parametrisering en frameworkbescherming. Vertrouw niet op één.
- **Minste privilege voor identiteiten en tokens.** Beperk inloggegevens smal en laat ze snel verlopen.
- **Je afhankelijkheden zijn je code.** Je bent verantwoordelijk voor de beveiliging van alles wat je oplevert, inclusief componenten van derden en open source.
- **Standaarden boven improvisatie.** Gebruik gecontroleerde raamwerken zoals de ASVS van [OWASP](https://en.wikipedia.org/wiki/OWASP) (Open Worldwide Application Security Project) in plaats van je eigen beveiligingsmaatregelen te verzinnen.

## Aanbevelingen

### Ken en verdedig de OWASP Top 10, verifieer met ASVS

De OWASP Top 10 is de branchebasislijn van de meest kritieke risico's voor webapplicaties: kapotte toegangscontrole, cryptografische falen, injectie, onveilig ontwerp, beveiligingsmisconfiguratie, kwetsbare componenten, authenticatiefalen, dataintegriteitsfalen, loggingfalen en server-side request forgery. Behandel haar als vereiste kennis voor elke engineer, niet slechts een compliancereferentie om weg te leggen.

Neem voor een rigoureuze, testbare standaard de **OWASP Application Security Verification Standard (ASVS)** aan. ASVS definieert beveiligingsvereisten op drie niveaus van zekerheid, wat je concrete, controleerbare maatregelen geeft om tegen te ontwerpen en te testen. Kies het niveau dat bij het risico van elke applicatie past en verifieer ertegen.

### Valideer invoer en codeer uitvoer

Injectiefouten blijven onder de meest schadelijke juist omdat ze zo makkelijk te introduceren zijn. Verdedig je met gelaagde maatregelen:

- **Valideer invoer** tegen strikte toegestane lijsten (verwacht type, lengte, formaat, bereik). Weiger in plaats van op te schonen waar je kunt.
- **Gebruik geparametriseerde queries** en [prepared statements](https://en.wikipedia.org/wiki/Prepared_statement) voor alle databasetoegang. Bouw nooit SQL door stringconcatenatie. Gebruik veilige querybouwers en ORM's (object-relational mappers) correct.
- **Codeer uitvoer** contextueel. HTML, HTML-attributen, JavaScript, URL's en CSS vragen elk andere codering. Leun op automatisch ontsnappen van het framework en begrijp haar grenzen.
- **Voorkom [cross-site scripting](https://en.wikipedia.org/wiki/Cross-site_scripting) (XSS)** met uitvoercodering plus een sterk Content Security Policy als tweede laag.
- **Voorkom commando- en sjablooninjectie** door niet met onbetrouwbare data een shell aan te roepen en door logicavrije of gesandboxte sjablonen te gebruiken.

### Krijg authenticatie en autorisatie goed

Authenticatie bewijst wie een gebruiker is. Autorisatie bepaalt wat ze mogen doen. Beide falen vaak, dus krijg ze goed.

- Geef de voorkeur aan gevestigde protocollen: **[OAuth 2.0](https://en.wikipedia.org/wiki/OAuth)** voor gedelegeerde autorisatie en **[OpenID Connect](https://en.wikipedia.org/wiki/OpenID_Connect) (OIDC)** voor authenticatie. Bouw ze niet vanaf nul.
- Dwing **[multifactorauthenticatie](https://en.wikipedia.org/wiki/Multi-factor_authentication) (MFA)** af, vooral voor bevoorrechte en administratieve toegang.
- Sla wachtwoorden alleen op als gezouten hashes met een modern, traag, geheugenintensief algoritme (zoals [Argon2](https://en.wikipedia.org/wiki/Argon2) of [bcrypt](https://en.wikipedia.org/wiki/Bcrypt)). Sla nooit platte inloggegevens op of log ze.
- Beheer **sessies** zorgvuldig: genereer cryptografisch sterke tokens, stel secure en HttpOnly cookievlaggen in, roteer bij privilegewijziging en laat inactieve sessies verlopen.
- Dwing **autorisatie op de server af voor elk verzoek**, controleer dat de geauthenticeerde principal de specifieke resource bezit of mag benaderen. Kapotte autorisatie op objectniveau (het record van een andere gebruiker benaderen door een ID te wijzigen) is een van de meest voorkomende en ernstige API-fouten.
- Centraliseer autorisatielogica waar praktisch zodat beleid consistent en controleerbaar is.

### Beheer geheimen en roteer sleutels

Hardgecodeerde geheimen in broncode zijn een eeuwige oorzaak van inbreuken. Bouw een gedisciplineerde gewoonte rond geheimenbeheer:

- Bewaar geheimen in een toegewijde geheimenbeheerder of kluis, nooit in broncode, configuratiebestanden of omgevingsvariabelen ingecheckt in versiebeheer.
- Scan commits en repositories automatisch op gelekte geheimen en blokkeer samenvoegingen die ze introduceren.
- Roteer sleutels en inloggegevens regelmatig en onmiddellijk bij elk vermoeden van blootstelling. Geef de voorkeur aan kortlevende, automatisch uitgegeven inloggegevens boven langlevende statische.
- Pas minste privilege toe op elk geheim: beperk het tot precies wat het nodig heeft.
- Versleutel geheimen in rust en tijdens transport en audit de toegang ertoe.

### Beveilig de softwaretoeleveringsketen

Moderne applicaties worden grotendeels samengesteld uit componenten van derden, wat de toeleveringsketen tot een primair aanvalsoppervlak maakt.

- Houd een **[Software Bill of Materials](https://en.wikipedia.org/wiki/Software_bill_of_materials) (SBOM)** bij voor elke applicatie zodat je precies weet wat je oplevert en snel kunt reageren wanneer een nieuwe kwetsbaarheid opduikt.
- Scan afhankelijkheden continu (Software Composition Analysis, of SCA) en herstel bekend kwetsbare componenten snel.
- Pin en verifieer afhankelijkheidsversies. Gebruik lockbestanden en vertrouwde registers.
- Neem **SLSA** (Supply-chain Levels for Software Artifacts) aan om buildintegriteit te verhogen en genereer **herkomst**verklaringen die beschrijven hoe artefacten zijn gebouwd.
- **Onderteken artefacten** en verifieer handtekeningen voor deployment zodat je kunt vertrouwen dat wat draait is wat je bouwde.
- Beveilig het buildsysteem zelf. Een gecompromitteerde CI-pipeline kan kwaadaardige code injecteren in elke downstreamconsument.

## Afwegingen: voor- en nadelen

| Beslissing | Voordelen | Nadelen |
|---|---|---|
| Identiteitsprovider (OIDC) kopen/aannemen | Beproefd, MFA ingebouwd, minder code om te beveiligen | Leveranciersafhankelijkheid, integratie-inspanning, kosten |
| Eigen authenticatie bouwen | Volledige controle, geen externe afhankelijkheid | Buitengewoon makkelijk fout te doen, hoog onderhoud |
| Strikte validatie met toegestane lijst | Blokkeert hele kwetsbaarheidsklassen | Kan legitieme randgevallen breken, meer werk vooraf |
| Kortlevende inloggegevens | Klein inbreukvenster, automatische intrekking | Vraagt robuuste uitgifte-infrastructuur |
| Agressieve afhankelijkheidsupdates | Minder bekende kwetsbaarheden | Omloop, mogelijk brekende wijzigingen, testlast |
| SBOM + ondertekening + herkomst | Snelle incidentrespons, verifieerbaar vertrouwen | Investering in tooling en proces, cultuurverandering |

De terugkerende afweging is rigueur vooraf tegenover doorlopende blootstelling. Eigen authenticatie bouwen of afhankelijkheidshygiëne overslaan voelt vandaag sneller en kost je later enorm. Gecontroleerde standaarden en geautomatiseerde toeleveringsketenmaatregelen aannemen kost nu moeite, maar verandert een onbegrensd, onvoorspelbaar risico in een beheerd, begrensd risico. Voor grote teams telt de automatiseringsvermenigvuldiger het meest: een maatregel eenmaal toegepast in een gebaande-wegsjabloon beschermt elke service die haar gebruikt.

## Vragen om met je team te bespreken

1. **Welke ASVS-maatregelen ga je in je gebaande-wegframework bakken zodat engineers ze gratis krijgen?** De zet met de hoogste hefboom voor een groot team is het veilige pad de standaard te maken, zodat een maatregel eenmaal geschreven in een gedeeld framework elke service beschermt die haar aanneemt. Besluit welke ASVS-vereisten (geparametriseerde queries, uitvoercodering, veilige sessievlaggen, autorisatiecontroles op de server) in het sjabloon horen in plaats van in het geheugen van elke engineer. Besluit voor portfolio's van onderneming en overheid ook welke applicaties ASVS-niveau 2 versus niveau 3 nodig hebben, en koppel dat aan de gevoeligheid van de data die elke raakt. Neem een lijst van je services mee en markeer welke deze standaarden al erven en welke beveiliging met de hand herimplementeren, want de met de hand gerolde zijn waar injectie en kapotte toegangscontrole zich verbergen. Als veilige standaarden alleen op een wikipagina leven, worden ze onder leveringsdruk overgeslagen, dus zet ze in code.

2. **Hoe ga je kapotte autorisatie op objectniveau vinden en repareren over elke API, niet alleen de nieuwe?** Het record van een andere gebruiker benaderen door een ID te wijzigen is een van de meest voorkomende en ernstige API-fouten, en ze verbergt zich in oudere endpoints die dateren van voor je huidige standaarden. Autorisatie op de server bij elk verzoek en elk object is de regel, maar het moeilijke deel is verifiëren dat ze standhoudt over een uitdijende, jaren oude codebase geschreven door veel handen. Besluit of je autorisatielogica centraliseert, geautomatiseerde tests toevoegt die toegang over tenants heen proberen of gericht testen draait tegen je API's met het hoogste risico eerst. Neem je inventaris mee van endpoints die objectidentifiers blootleggen en rangschik ze naar de gevoeligheid van wat ze teruggeven. Zonder bewuste doorlichting blijf je deze fout opleveren en ontdek je haar pas wanneer een onderzoeker of een aanvaller dat doet.

3. **Wat is je plan voor de volgende wijdverbreide afhankelijkheidskwetsbaarheid: hoe snel kun je elke getroffen service vinden en patchen?** Wanneer een kritieke fout opduikt in een populaire bibliotheek, identificeren de bedrijven met een nauwkeurige SBOM getroffen services in uren terwijl anderen weken zoeken, en die snelheidskloof bepaalt hoeveel schade je oploopt. Besluit nu of je voor elk artefact een Software Bill of Materials produceert, of afhankelijkheidsscanning in elke pipeline draait en wie de noodpatchbeslissing bezit. Voor gereguleerde en overheidskopers zijn SBOM's en ondertekende herkomst steeds vaker een voorwaarde om zaken te doen, dus deze gereedheid beschermt ook omzet. Neem het eerlijke antwoord op een oefening mee: kies een bibliotheek die je breed gebruikt en tijd hoe lang het duurt om elke service te noemen die haar levert. Als het antwoord in dagen wordt gemeten, investeer dan in inventaris en ondertekening voordat het volgende incident je dwingt.

4. **Hoe ga je van langlevende statische geheimen naar kortlevende, automatisch uitgegeven inloggegevens, en welke systemen blokkeren dat vandaag?** Hardgecodeerde en langlevende geheimen zijn een eeuwige oorzaak van inbreuken, en de oplossing, kortlevende inloggegevens op aanvraag uitgegeven, hangt af van uitgifte-infrastructuur die oudere systemen vaak niet kunnen gebruiken. Voor een groot team is het gevaar ongelijke adoptie: een modern platform roteert sleutels elk uur terwijl een legacyservice nog een statisch databasewachtwoord in een configuratiebestand oplevert. Besluit welke werklasten nu een geheimenbeheerder of werklastidentiteitssysteem kunnen consumeren, welke eerst investering nodig hebben en wie het rotatierunbook bezit op het moment dat een sleutel als gelekt wordt vermoed. Neem een inventaris mee van elke inloggegeven in gebruik, haar levensduur, haar schadezone bij blootstelling en of commitscanning haar voor het samenvoegen zou vangen. Koppel dit in omgevingen van onderneming en overheid aan audit: examinatoren verwachten steeds vaker bewijs van rotatie, beperkte toegang en toegangslogging voor elk geheim, en een statische inloggegeven die je niet zonder downtime kunt roteren is een bevinding die wacht te worden opgeschreven.

5. **Waar draai je nog zelfgebouwde of inconsistente authenticatie, en wat is het plan om te consolideren op gecontroleerde protocollen?** Authenticatie bouwen is een van de makkelijkste manieren om subtiele, uitbuitbare fouten te introduceren, en toch draagt de meeste grote landschappen minstens één legacyinlogstroom die dateert van voor het besluit te standaardiseren op OAuth 2.0 en OIDC. De concurrerende druk is echt: een oude stroom migreren riskeert bestaande gebruikers en integraties te breken, terwijl haar laten staan een doelwit met hoge waarde onderbeschermd houdt. Besluit of je op één identiteitsprovider consolideert, MFA uniform afdwingt en een deadline stelt om elke maatwerkstroom uit te faseren, of gedocumenteerde uitzonderingen met compenserende maatregelen accepteert. Neem een kaart mee van elk authenticatiepad in de vloot, welke MFA afdwingen, welke wachtwoorden opslaan met een moderne geheugenintensieve hash en welke maatwerk zijn. Voeg voor portfolio's van onderneming en overheid de complianceinvalshoek toe: standaarden als NIST SP 800-63 stellen concrete verwachtingen aan identiteitszekerheid, en een zelfgebouwde stroom die ze niet kan aantonen zal een audit of een autorisatie-om-te-opereren-review niet overleven.

6. **Hoe verifieer je dat deze maatregelen in productie standhouden, en kun je het bewijzen met bewijs in plaats van bewering?** Een veilige standaard schrijven is niet hetzelfde als weten dat elke service haar nog naleeft, en maatregelen rotten stilletjes weg naarmate code verandert, uitzonderingen zich opstapelen en nieuwe endpoints worden opgeleverd. Voor een groot team is de vraag dekking: welke services draaien statische analyse, afhankelijkheidsscanning en dynamisch of penetratietesten, en hoe weet je dat degene die ze overslaan niet je applicaties met het hoogste risico zijn? Besluit welke verificatie verplicht is in de pipeline versus periodiek, wie de bevindingen trieert en welk bewijs je bewaart om te tonen dat een maatregel op een gegeven datum werd getest en slaagde. Neem je huidige dekkingskaart mee, je gemiddelde hersteltijd per ernst en de lijst applicaties zonder recente test. In gereguleerde en overheidscontexten is dit bewijs niet optioneel: auditors, autoriserende functionarissen en inbreukonderzoekers vragen allemaal om bewijs dat maatregelen zijn geverifieerd, en een beleid zonder testregisters stelt hen zelden tevreden.

## Sectorperspectief

**Startup.** Met twee of drie engineers en geen beveiligingsspecialist is je hefboom beveiliging te erven in plaats van te bouwen: neem een beheerde OIDC-identiteitsprovider aan, leun op een framework waarvan de ORM queries standaard parametriseert en bewaar geheimen in de geheimenbeheerder van je platform in plaats van `.env`-bestanden die een teamgenoot per ongeluk kan committen. Zet geautomatiseerde afhankelijkheidsscanning aan die patch-pull-requests opent, en behandel dat voorlopig als genoeg. Bouw geen eigen authenticatie of crypto, want één geïnjecteerde query of één gelekte sleutel kan het bedrijf beëindigen voordat het klanten heeft.

**Kleinbedrijf.** Je hebt waarschijnlijk geen applicatiebeveiligingsspecialist en een krap budget, dus koop maatregelen ingebed in de tools en platforms die je al betaalt in plaats van een aparte functie te bemannen. Kies een gehoste identiteitsprovider met MFA inbegrepen, een beheerde database die je naar geparametriseerde toegang stuurt en een repositoryhost die commits standaard scant op gelekte geheimen. Concentreer je schaarse aandacht op de basis van de OWASP Top 10 die de meeste echte inbreuken veroorzaakt, en geef de voorkeur aan leveranciers die veilige standaarden leveren die je niet zomaar kunt uitzetten.

**Grote onderneming.** Over veel teams is de uitdaging consistentie: bak ASVS-maatregelen in gebaande-wegframeworks zodat elke nieuwe service geparametriseerde queries, uitvoercodering, veilige sessies en autorisatie op de server gratis erft. Draai nauwkeurige SBOM's en afhankelijkheidsscanning over de vloot zodat de volgende wijdverbreide bibliotheekkwetsbaarheid een kwestie van uren is, niet weken, en centraliseer autorisatiebeleid zodat toegang tussen tenants testbaar wordt. Standaardiseer op één identiteitsprovider met afgedwongen MFA en beheer applicatiebeveiliging als bestuurd portfolio met ASVS-niveaus gelaagd naar risico en geauditeerd bewijs.

**Overheid.** Aanbestedingsregels, transparantie en publieke verantwoording geven vorm aan de maatregelen die je moet aantonen, niet slechts implementeren. Verifieer burgergerichte services tegen OWASP ASVS op een niveau afgestemd op datagevoeligheid, onderteken elk gedeployd artefact en attesteer zijn herkomst volgens SLSA om aan toeleveringsketenmandaten te voldoen en geef kortlevende inloggegevens uit vanuit een centrale kluis met volledige toegangslogging. Verwacht auditors en autoriserende functionarissen een gedocumenteerde bewakingsketen te tonen van bron tot productie, en stem identiteitszekerheid af op gepubliceerde standaarden als NIST SP 800-63.

## Voorbeelden

**Startup.** Een SaaS-team van drie engineers slaat het bouwen van een eigen login over en neemt vanaf dag één een beheerde OIDC-provider aan, wat MFA en veilige wachtwoordherstel oplevert zonder beveiligingskritieke code te schrijven die ze zich niet kunnen veroorloven fout te doen. Het leunt op de ORM van het framework zodat queries standaard geparametriseerd zijn, bewaart geheimen in de geheimenbeheerder van het platform in plaats van in `.env`-bestanden die een teamgenoot per ongeluk kan committen, en zet geautomatiseerde afhankelijkheidsscanning aan die een pull request opent wanneer een bibliotheek moet worden gepatcht. Niets hiervan vertraagt het team, en het betekent dat één gelekte sleutel of één geïnjecteerde query het bedrijf niet beëindigt voordat het klanten heeft.

**Grote onderneming.** Een retailplatform dat tientallen miljoenen shoppers bedient standaardiseert authenticatie op OIDC via één identiteitsprovider, MFA afdwingend voor personeel en step-upauthenticatie voor accountwijzigingen met hoge waarde. Alle databasetoegang loopt via een ORM geconfigureerd om queries te parametriseren, en een Content Security Policy ondersteunt uitvoercodering. Na een alom gepubliceerde kwetsbaarheid in een populaire logbibliotheek laat de SBOM van het bedrijf het elke getroffen service binnen uren identificeren en in twee dagen patchen, terwijl concurrenten zonder inventaris weken zochten.

**Overheid.** Een federale uitkeringsinstantie bouwt burgergerichte services geverifieerd tegen OWASP ASVS niveau 2, met niveau 3 voor de componenten die de gevoeligste records verwerken. Geheimen leven in een centrale kluis die kortlevende inloggegevens uitgeeft, en commitscanning blokkeert elke gelekte sleutel. Elk gedeployd artefact wordt ondertekend en zijn herkomst geattesteerd volgens SLSA, wat voldoet aan een federaal mandaat voor verifieerbare softwaretoeleveringsketens en auditors een heldere bewakingsketen geeft van bron tot productie.

## Zakelijke onderbouwing: motivatie, ROI en TCO

Uitgaven aan applicatiebeveiliging kopen de meest waarschijnlijke en duurste categorie inbreuk omlaag. De total cost of ownership omvat tooling (scanners, geheimenbeheerders, identiteitsproviders), engineertijd om bevindingen te herstellen en de milde wrijving van veilige standaarden. Weeg daartegenover de kosten van het overslaan: injectie- en kapotte-toegangscontrole-inbreuken leggen routinematig miljoenen records bloot, wat boetes van toezichthouders, verplichte melding, fraudeverliezen, herstelsprints en reputatieschade triggert die omzet jarenlang onderdrukt.

Het ROI is het sterkst wanneer maatregelen geautomatiseerd en hergebruikt zijn. Eén goed geconfigureerde identiteitsintegratie, één verharde querylaag in een gedeeld framework en één pipeline die kwetsbare afhankelijkheden blokkeert beschermen de hele vloot tegen marginale kosten per service. Toeleveringsketenmaatregelen in het bijzonder zijn van optioneel essentieel geworden: een gecompromitteerde afhankelijkheid kan elk van je klanten tot slachtoffer maken, en toezichthouders en ondernemingskopers eisen steeds vaker SBOM's en ondertekende herkomst als voorwaarde om zaken te doen. Koppel de investering om het bestuur te overtuigen aan specifieke, benoemde risico's en aan aanbestedings- en complianceeisen die omzet blokkeren als je ze niet haalt.

## Antipatronen en valkuilen

- **Je eigen crypto of authenticatie rollen.** Produceert bijna altijd subtiele, uitbuitbare fouten.
- **Validatie alleen aan de clientzijde.** Triviaal te omzeilen. De server moet alles opnieuw valideren.
- **Opschoning met zwarte lijst.** Proberen "slechte" tekens te strippen in plaats van goede toe te staan. Aanvallers vinden de gaten.
- **Geheimen in broncode of omgevingsbestanden.** De meest voorkomende oorzaak van lekken van inloggegevens.
- **Autorisatie op objecttoegang negeren.** Aannemen dat een geauthenticeerde gebruiker elk object mag benaderen waarvan hij het ID kan raden.
- **Afhankelijkheden zetten en vergeten.** Componenten van derden nooit bijwerken tot een inbreuk het afdwingt.
- **De Top 10 als finishlijn behandelen.** Het is een vloer, geen volledige standaard. Gebruik ASVS voor diepte.
- **Gevoelige data loggen.** Wachtwoorden, tokens en PII (persoonlijk identificeerbare informatie) in logs worden een inbreuk die wacht te gebeuren.

## Volwassenheidsmodel

**Niveau 1: Initiëren.** Applicatiebeveiliging hangt af van de kennis van individuele ontwikkelaars en reageert alleen na incidenten. Geen standaardmaatregelen. Geheimen staan in de broncode. Afhankelijkheden worden zelden bijgewerkt. Authenticatie is maatwerk en ad hoc, en injectie- of kapotte-toegangscontrolefouten worden gevonden door toeval in plaats van door proces.

**Niveau 2: Ontwikkelen.** Basispraktijken verschijnen maar verschillen per team. Bewustzijn van de OWASP Top 10 verspreidt zich, wat bescherming op frameworkniveau aanwezig is en een geheimenbeheerder bestaat maar wordt ongelijk gebruikt. Afhankelijkheidsscanning draait af en toe. Nieuwe systemen nemen een standaardidentiteitsprovider aan, terwijl oudere services hun zelfgebouwde inlogstromen onaangeroerd houden.

**Niveau 3: Standaardiseren.** Maatregelen zijn gedocumenteerd en organisatiebreed gehandhaafd. Op ASVS gebaseerde vereisten zijn per risicolaag vastgesteld, geparametriseerde queries en uitvoercodering zijn de norm en een centrale identiteitsprovider met MFA is vereist. Geheimen worden automatisch beheerd en gescand, SBOM's worden geproduceerd en afhankelijkheidsscanning draait in elke pipeline.

**Niveau 4: Beheersen.** De praktijk wordt gemeten en beheerst aan de hand van uitgangswaarden. Scan- en testdekking, gemiddelde hersteltijd per ernst, het aandeel services dat gebaande-wegstandaarden erft, ouderdom van rotatie van inloggegevens en geheimen en ASVS-conformiteit worden allemaal op dashboards gevolgd. Uitzonderingen worden gelogd met verloopdata, afdrijving van de uitgangswaarde triggert actie en releases worden gepoort op gedefinieerde beveiligingsdrempels in plaats van oordeelsbeslissingen.

**Niveau 5: Orkestreren.** Beveiliging wordt continu verbeterd en is over de organisatie geïntegreerd. Veilige standaarden zijn ingebouwd in gebaande-wegframeworks zodat het veilige pad automatisch is, kortlevende inloggegevens worden overal gebruikt en volledige toeleveringsketenzekerheid met ondertekening en herkomst (SLSA) is standaard. Verificatie is continu, de reactie op nieuwe kwetsbaarheden is snel en gemeten, en elk incident voedt terug in de gedeelde sjablonen zodat één oplossing de hele vloot verhardt.

## Ideeën voor discussie

1. Waar moet autorisatielogica leven om zowel consistent als onderhoudbaar te zijn over veel services?
2. Hoe agressief moet je afhankelijkheden bijwerken gezien de afweging tussen blootstelling en omloop?
3. Welk ASVS-niveau is passend voor elke klasse applicatie in je portfolio?
4. Hoe elimineer je langlevende geheimen zonder broze uitgifte-infrastructuur te creëren?
5. Wat zou er nodig zijn voor je organisatie om SBOM's en herkomst te produceren en te consumeren voor elk artefact?
6. Hoe voorkom je dat veilige standaarden onder leveringsdruk worden uitgeschakeld?

## Belangrijkste inzichten

- De OWASP Top 10 is essentiële kennis. ASVS biedt de testbare standaard.
- Laag invoervalidatie, parametrisering en uitvoercodering om injectie en XSS te verslaan.
- Gebruik gecontroleerde protocollen (OAuth 2.0, OIDC) en dwing MFA af. Bouw authenticatie nooit vanaf nul.
- Dwing autorisatie op de server af voor elk verzoek en elk object.
- Houd geheimen uit broncode, beheer ze centraal en roteer naar kortlevende inloggegevens.
- De toeleveringsketen is een primair aanvalsoppervlak. Gebruik SBOM's, SCA, ondertekening en herkomst (SLSA).
- Geautomatiseerde, herbruikbare maatregelen beschermen de hele vloot tegen marginale kosten per service.

## Referenties en verder lezen

- OWASP, *Top 10 Web Application Security Risks*
- OWASP, *Application Security Verification Standard (ASVS)*
- OWASP, *Cheat Sheet Series* (Input Validation, Authentication, Authorisation, Secrets Management)
- Dafydd Stuttard and Marcus Pinto, *The Web Application Hacker's Handbook*
- Aaron Parecki, *OAuth 2.0 Simplified*
- National Institute of Standards and Technology, *SP 800-63: Digital Identity Guidelines*
- Cloud Native Computing Foundation and OpenSSF, *SLSA framework* and *Supply-chain Security guidance*
