# 8.2 Infrastructure as code en configuratie

## Overzicht en motivatie

[Infrastructure as code](https://en.wikipedia.org/wiki/Infrastructure_as_code) (IaC) betekent infrastructuur (netwerken, servers, databases, load balancers, rechten) definiëren en inrichten via machineleesbare definitiebestanden in plaats van handmatige consoleklikken of ad hoc scripts. [Configuratiebeheer](https://en.wikipedia.org/wiki/Configuration_management) breidt hetzelfde idee uit naar de instellingen en toestand van systemen zodra ze bestaan. Samen veranderen ze infrastructuur van een met de hand gemaakt, kwetsbaar artefact in een geversioneerd, beoordeelbaar, reproduceerbaar product van dezelfde engineeringdiscipline die je voor applicatiecode gebruikt.

Voor grote teams is IaC geen gemak maar een noodzaak. Wanneer honderden engineers omgevingen nodig hebben en duizenden bronnen consistent moeten blijven over regio's en accounts, kan handmatige provisioning niet bijbenen en niet correct blijven. Met de hand geconfigureerde infrastructuur drijft vroeg of laat af naar unieke "sneeuwvlok"-servers die niemand volledig begrijpt en die na een falen niet betrouwbaar kunnen worden herbouwd. Infrastructuur coderen maakt haar consistent, controleerbaar en wegwerpbaar. Elke omgeving kan uit haar definitie worden herschapen, en elke wijziging is een beoordeelbare diff.

Organisaties van onderneming en overheid krijgen nog een beslissend voordeel: afdwingbare governance. Beveiligings- en complianceeisen, zoals versleuteling in rust, netwerksegmentatie, goedgekeurde regio's en tagging voor kostentoewijzing, kunnen direct in de code worden ingebed en automatisch worden gecontroleerd voordat er iets wordt ingericht. In plaats van infrastructuur achteraf auditen en overtredingen najagen, voorkom je dat niet-conforme infrastructuur ooit bestaat. Deze verschuiving van detectie naar preventie is de kernreden dat IaC fundamenteel is geworden voor moderne platformpraktijk.

## Kernprincipes

- Geef de voorkeur aan declaratieve definities die de gewenste toestand beschrijven boven imperatieve scripts die stappen beschrijven.
- Bewaar alle infrastructuurdefinities in versiebeheer, beoordeeld als elke andere code.
- Behandel infrastructuur als onveranderlijk: vervang in plaats van ter plekke te wijzigen.
- Maak provisioning idempotent zodat dezelfde definitie herhaaldelijk toepassen hetzelfde resultaat geeft.
- Detecteer en verzoen drift, de live omgeving die afwijkt van haar gedeclareerde definitie, continu. De code, niet het live systeem, is de bron van waarheid.
- Stel infrastructuur samen uit herbruikbare, geversioneerde modules in plaats van kopiëren en plakken.
- Codeer beleid als code, organisatieregels uitgedrukt als machinecontroleerbare code, zodat vangrails automatisch zijn, niet adviserend.
- Houd geheimen buiten definities. Verwijs ernaar vanuit een speciale geheimenbeheerder.

## Aanbevelingen

### Kies declaratieve tooling en structureer haar rond modules

Neem een declaratieve IaC-tool aan, zoals [Terraform](https://en.wikipedia.org/wiki/Terraform_(software)), Pulumi of een cloud-native optie als CloudFormation, en standaardiseer er organisatiebreed op zodat je een gefragmenteerd toolinglandschap vermijdt. De sleutelarchitectuurpraktijk is modulariteit: bouw kleine, goed gedocumenteerde, geversioneerde modules die gangbare patronen vastleggen (een conform netwerk, een geharde database, een standaardservice). Teams stellen omgevingen dan samen uit deze modules in plaats van ruwe bronnen te schrijven. Dit verspreidt goede standaarden en beveiligingsinstellingen automatisch en vermindert duplicatie dramatisch.

### Beheer toestand bewust

Declaratieve tools volgen de koppeling tussen code en echte bronnen in een toestandsbestand. Sla toestand extern op in een gedeelde, versleutelde, toegangsgecontroleerde backend en gebruik vergrendeling zodat gelijktijdige wijzigingen haar niet kunnen corrumperen. Houd toestand nooit op een laptop en bewerk haar nooit met de hand behalve als laatstmiddelherstelactie. Toestand is gevoelig, omdat ze bronmetadata en geheimen kan bevatten, dus bescherm haar dienovereenkomstig.

### Bouw onveranderlijke infrastructuur met gouden images

In plaats van draaiende servers te patchen, bak je een geversioneerd "gouden image" (een vooraf geconfigureerd, gehard machine- of containerimage) en deploy je verse instanties ervan. Wanneer je een wijziging of patch nodig hebt, bouw je een nieuw image en rol je het uit, de oude instanties buiten dienst stellend. Dit elimineert configuratiedrift, maakt rollback triviaal en houdt elke instantie identiek en herleidbaar tot een bekend-goede build. Geautomatiseerde imagepijplijnen moeten beveiligingsverharding en scanning bevatten, zodat compliance op imageniveau is ingebouwd.

### Detecteer en verzoen configuratiedrift

Drift gebeurt wanneer de live omgeving afwijkt van haar definitie, meestal omdat iemand een handmatige noodwijziging maakte. Draai regelmatig driftdetectie die de werkelijke toestand met de gedeclareerde toestand vergelijkt en de verschillen markeert. Behandel drift als defect: verzoen door de code bij te werken en opnieuw toe te passen, niet door de handmatige wijziging te laten staan. Gebruik voor systemen die doorlopende configuratieafdwinging nodig hebben een configuratiebeheertool die hosts continu naar hun gedeclareerde toestand laat convergeren.

### Neem GitOps en pull-based deployment aan

In het GitOps-model bevat een Git-repository de gedeclareerde gewenste toestand van het systeem, en een geautomatiseerde agent die binnen de doelomgeving draait trekt die toestand continu binnen en verzoent het live systeem om ermee overeen te komen. Dit keert het traditionele pushmodel om. Geen extern systeem heeft permanente inloggegevens nodig om de omgeving te wijzigen, omdat de omgeving haar eigen configuratie binnenhaalt. GitOps geeft je een compleet auditspoor (elke wijziging is een commit), eenvoudige rollback (draai de commit terug) en sterke driftcorrectie (de agent herbevestigt continu de gewenste toestand). Het is vooral krachtig voor [Kubernetes](https://en.wikipedia.org/wiki/Kubernetes) en voor organisaties die één enkele, beoordeelbare bron van waarheid willen.

### Dwing vangrails af met policy as code

Druk organisatieregels, zoals toegestane regio's, verplichte versleuteling, vereiste tags en verboden publieke blootstelling, uit als machinecontroleerbare beleidsregels met een tool als Open Policy Agent (OPA) of een platformeigen beleidsengine als Sentinel. Draai deze controles in de pijplijn vóór provisioning, zodat schendingen automatisch worden geblokkeerd. Policy as code verandert de intentie van een beveiligingsteam in een uitvoerbare, uniform toegepaste maatregel, en schaalt naar duizenden wijzigingen op een manier die handmatige review nooit kon.

## Afwegingen: voor- en nadelen

| Keuze | Voordelen | Nadelen | Past het best bij |
|---|---|---|---|
| Declaratieve IaC (Terraform/Pulumi) | Reproduceerbaar, beoordeelbaar, drift-detecteerbaar | Leercurve. Complexiteit van toestandsbeheer | Bijna alle teams op schaal |
| Imperatieve scripts | Vertrouwd. Flexibel voor eenmalig | Niet idempotent. Moeilijk te auditen en te herhalen | Smalle, transitionele gevallen |
| Onveranderlijk + gouden images | Geen drift. Triviale rollback | Overhead van imagebuildpijplijn | Vloten die consistentie nodig hebben |
| Veranderlijk configuratiebeheer | Fijnmazige doorlopende controle | Driftrisico. Tragere convergentie | Legacy of langlevende hosts |
| GitOps (pull-based) | Sterk auditspoor. Zelfherstellend | Vraagt in-clusteragent en Git-discipline | Kubernetes en cloud-native |
| Policy as code | Automatische, uniforme vangrails | Beleidsschrijfinspanning vooraf | Gereguleerde omgevingen |

De hoofdspanning is tussen flexibiliteit en controle. Handmatige en imperatieve aanpakken voelen sneller voor één wijziging, maar ze stapelen verborgen inconsistentie op die op schaal verlammend wordt. Declaratieve, onveranderlijke, door beleid bestuurde infrastructuur vraagt meer investering vooraf en een echte cultuurverschuiving, aangezien engineers moeten ophouden snelle consolewijzigingen te maken, maar ze betaalt die investering vele malen terug in betrouwbaarheid, controleerbaarheid en het vermogen alles op aanvraag te herbouwen.

## Vragen om met je team te bespreken

1. **Wie bezit de gedeelde modulebibliotheek, en hoe bereikt een verbetering in een module elk team dat haar gebruikt?** Modules betalen zich alleen terug als reparaties en geharde standaarden zich voortplanten, en dat vraagt helder eigenaarschap en echt versiebeheer, geen map waar iedereen uit kopieert. Besluit wie de modules voor conform netwerk en geharde database onderhoudt, hoe je ze versioneert (semantisch versiebeheer met een changelog) en hoe teams upgrades binnenhalen zonder brandoefening. Op schaal is dit het verschil tussen een misconfiguratie eenmaal repareren en haar over duizend met de hand bewerkte bronnen najagen. Neem bewijs mee: hoeveel aparte kopieën van hetzelfde patroon vandaag bestaan, hoe lang een beveiligingsreparatie nodig heeft om elke omgeving te bereiken en of teams modulversies pinnen of laten zweven. Als een kritieke patch niet in dagen het hele landschap kan bereiken, is je modulariteit cosmetisch.

2. **Wat is je cadans voor driftdetectie, en wat gebeurt er werkelijk wanneer drift wordt gevonden?** Drift is de live omgeving die stilletjes afwijkt van haar gedeclareerde toestand, meestal door een consolewijziging in nood, en haar tolereren verandert je code in fictie. Besluit hoe vaak je de werkelijke toestand met de gedeclareerde toestand vergelijkt (nachtelijk is een redelijke standaard) en, belangrijker, besluit de respons: verzoen door de code bij te werken en opnieuw toe te passen, nooit door de handmatige wijziging te laten staan. In gereguleerde omgevingen is dit een beheerseis, omdat auditors nodig hebben dat de gedeclareerde toestand continu met de werkelijkheid overeenkomt. Neem je huidige getallen mee: hoeveel bronnen driften elke week, hoe lang blijven ze afgedreven en is iemand verantwoordelijk voor het sluiten ervan. Behandel elke drift als defect met een eigenaar, anders erodeert de garantie van de bron van waarheid tot niemand de code nog vertrouwt.

3. **Ben je naar GitOps en pull-based verzoening gegaan, of houdt een extern systeem nog permanente inloggegevens om productie te wijzigen?** In het pullmodel verzoent een agent binnen de doelomgeving het live systeem continu met Git, wat de noodzaak wegneemt dat enig extern systeem schrijftoegang houdt, en ze herbevestigt de gewenste toestand zodat drift zichzelf corrigeert. Dat is een sterke beveiligings- en auditpositie, aangezien elke wijziging een commit is en geen operator permanente productie-inloggegevens nodig heeft. De kosten zijn echt: een in-clusteragent om te draaien en strikte Git-discipline, dus weeg het af tegen je huidige push-gebaseerde automatisering. Neem de lijst mee van wie en wat productie nu direct kan wijzigen, en welk auditspoor die wijzigingen achterlaten. Voor Kubernetes en enclaves met hoge zekerheid is deze verschuiving meestal de moeite waard. Voor een handvol statische bronnen kan het overdreven zijn.

4. **Hoe wordt je infrastructuurtoestand opgeslagen, vergrendeld en toegangsgecontroleerd, en wat gebeurt er de dag dat ze corrupt raakt of verloren gaat?** Toestand is de kaart tussen je code en de echte bronnen, dus een verloren of beschadigd toestandsbestand kan een tool blind laten voor bronnen die ze maakte en iemand verleiden tot een destructieve herhaling. Voor een groot team vermenigvuldigt het risico zich, omdat veel engineers die tegen gedeelde toestand toepassen een externe, versleutelde, vergrendelde backend nodig hebben zodat gelijktijdige runs elkaar niet kunnen verpletteren. Weeg het gemak van één grote toestand af tegen de schadezone die ze creëert, en overweeg toestand per omgeving of per domein te splitsen zodat één fout niet alles kan neerhalen. Neem de feiten mee: waar toestand vandaag leeft, of vergrendeling wordt afgedwongen, wie haar kan lezen (ze kan geheimen bevatten) en of je ooit een herstel hebt gerepeteerd. Behandel in omgevingen van onderneming en overheid de toestandsbackend als gevoelige, toegangsgecontroleerde bezitting met eigen back-up, auditlog en herstelrunbook, want haar verliezen is je register van wat bestaat verliezen.

5. **Wanneer een echt noodgeval een handmatige wijziging eist, wat is het goedgekeurde break-glasspad, en hoe wordt die wijziging terug in code gevouwen?** Elke volwassen IaC-praktijk ontmoet uiteindelijk het incident van 3 uur 's nachts waar wachten op een pijplijn onaanvaardbaar is, en de eerlijke vraag is niet of handmatige wijzigingen ooit gebeuren maar hoe je ze inperkt. Besluit vooraf wie de pijplijn mag omzeilen, wat ze mogen aanraken, hoe de actie wordt gelogd en de deadline waarbinnen de wijziging in code moet worden verzoend of teruggedraaid. Zonder die afspraak wordt de noodzakelijke uitzondering stilletjes de alledaagse gewoonte en keert ClickOps door de achterdeur terug. Neem bewijs mee: hoeveel wijzigingen buiten de pijplijn er vorig kwartaal gebeurden, hoe lang elke onverzoend bleef en of driftdetectie ze werkelijk ving. Voor gereguleerde en publieke organen is een gedocumenteerde break-glassprocedure met automatische logging vaak een beheerseis, omdat auditors verwachten dat zowel noodgevallen mogelijk zijn als dat elk een spoor achterlaat en het systeem terugbrengt naar zijn gedeclareerde toestand.

6. **Hoeveel van je beveiligings- en compliancebasis is uitgedrukt als beleid dat een slechte wijziging automatisch blokkeert, tegenover regels die in een document leven en erop leunen dat iemand ze onthoudt?** Vangrails geschreven als proza in een wiki worden routinematig geschonden, omdat ze ervan afhangen dat elke engineer ze onder deadlinedruk leest en toepast, terwijl dezelfde regels uitgedrukt als policy as code een niet-conforme wijziging afwijzen voordat ze ooit wordt ingericht. Voor een grote organisatie is dit de enige manier waarop de intentie van een beveiligingsteam naar duizenden wijzigingen schaalt zonder een reviewknelpunt te worden. Weeg de kosten vooraf van beleid schrijven en onderhouden af tegen de terugkerende kosten van handmatige review en herstel achteraf, en besluit welke maatregelen (versleuteling, goedgekeurde regio's, verplichte tags, geen publieke blootstelling) onderhandelbaar genoeg zijn om als harde poorten af te dwingen. Neem de lijst van je huidige basisregels mee en markeer welke geautomatiseerd tegenover adviserend zijn, plus hoe vaak elk in de praktijk wordt geschonden. In contexten van onderneming en overheid verandert geautomatiseerd beleid een audit van weken handmatig bewijs verzamelen in een query tegen afgedwongen maatregelen, en verandert het compliance van detectie in preventie.

## Sectorperspectief

**Startup.** Snelheid wint, dus zet je hele stack in één declaratieve repository (Terraform is een gangbare standaard), houd toestand in een beheerde versleutelde backend en leid elke wijziging door een pull request, zelfs met een team van drie. Sla de zware platformapparatuur over: geen centraal modulenteam, nog geen beleidsengine, alleen versiebeheer en de discipline nooit in de console te klikken. Dat alleen geeft je reproduceerbare omgevingen die je kunt afbreken om geld te besparen en herbouwen voor de volgende demo.

**Kleinbedrijf.** Zonder aparte platformspecialist leun je op beheerde diensten en de IaC die je cloudprovider of leverancier al ondersteunt in plaats van maatwerktooling op te zetten die je niet kunt onderhouden. Geef de voorkeur aan een gehost platform waarvan de verstandige standaarden (versleuteling, back-ups, patchen) voor je worden afgehandeld boven een goudenimagepijplijn bouwen die je niemand hebt om te draaien. Formuleer het doel smal: krijg je handvol kritieke bronnen in code zodat je ze kunt herbouwen na een falen of een vertrekkende aannemer.

**Grote onderneming.** Het kernprobleem is consistentie over veel teams, accounts en regio's, dus investeer in een geversioneerde gedeelde modulebibliotheek, externe vergrendelde toestand en policy as code afgedwongen in de pijplijn. Een centraal platformteam publiceert geharde modules en vangrails terwijl productteams zichzelf bedienen daarbinnen, en driftdetectie draait continu zodat duizenden bronnen in een bekende toestand blijven. Begroot de doorlopende kosten van modules en beleid onderhouden, want hun waarde komt uit een reparatie of geharde standaard die zich overal tegelijk voortplant.

**Overheid.** Aanbestedingsregels, accreditatie en publieke verantwoording duwen je naar onveranderlijke infrastructuur, ondertekende commits en GitOps-verzoening binnen een geaccrediteerde enclave, zodat geen operator permanente inloggegevens heeft om productie te wijzigen. Codeer de vereiste beveiligingsbasis in gouden images en policy as code, en laat de commitgeschiedenis dienen als sabotagebestendig, continu beschikbaar auditbewijs. Geef de voorkeur aan open, overdraagbare tooling boven bedrijfseigen formaten die je vastzetten, en maak de break-glassprocedure en haar logging expliciet zodat noodwijzigingen nog aan configuratiebeheereisen voldoen.

## Voorbeelden

**Startup.** Een startup van vijf personen definieert haar hele AWS-opzet, de VPC, database en containerservice, in één Terraform-repository met toestand bewaard in een versleutelde S3-backend en vergrendeling via DynamoDB. Elke wijziging gaat door een pull request, dus zelfs een solo bereikbare engineer kan precies zien wat er verandert voordat hij apply draait. Wanneer ze een verse stagingomgeving nodig hebben voor een grote demo, kopiëren ze een kleine module en zetten haar in minuten op, en breken haar net zo snel weer af om de cloudrekening laag te houden.

**Grote onderneming.** Een multinationale retailer beheert infrastructuur over meerdere cloudaccounts en regio's. Een centraal platformteam publiceert geversioneerde Terraform-modules voor conforme netwerken, databases en servicestellingen, en dwingt OPA-beleid af dat elke bron zonder versleuteling of kostentoewijzingstags afwijst. Productteams richten hun eigen omgevingen self-service in, maar elke wijziging stroomt door de pijplijn, waar beleid automatisch wordt gecontroleerd. Driftdetectie draait nachtelijk en opent tickets voor elke handmatige wijziging, wat duizenden bronnen continu in een bekende, conforme toestand houdt.

**Overheid.** Een defensieagentschap dat opereert in een omgeving met hoge zekerheid bouwt geharde gouden images die de vereiste beveiligingsbasis insluiten en deployt alleen onveranderlijke instanties ervan. Alle infrastructuur wordt gedeclareerd in Git en verzoend door een GitOps-agent binnen de geaccrediteerde enclave, zodat geen operator permanente inloggegevens heeft om productie direct te wijzigen. Elke wijziging is een ondertekende commit. Dit geeft auditors een compleet, sabotagebestendig overzicht en voldoet aan eisen voor continue bewaking en configuratiebeheer zonder handmatig bewijs verzamelen.

## Zakelijke onderbouwing: motivatie, ROI en TCO

Het ROI van IaC komt uit snelheid, betrouwbaarheid en risicovermindering. Omgevingen die ooit weken van door tickets gedreven handmatige provisioning vergden kunnen in minuten worden gemaakt, wat engineers vrijmaakt en projecten versnelt. Reproduceerbaarheid verkort de hersteltijd na falen drastisch, omdat elke omgeving uit code kan worden herbouwd. Geautomatiseerde beleidsafdwinging vermindert de frequentie en kosten van beveiligingsincidenten en auditbevindingen, wat voor gereguleerde organisaties aanzienlijk kan zijn.

In de TCO-boekhouding omvatten adoptiekosten tooling, training, een modulen- en beleidsbibliotheek bouwen en de discipline om op te houden handmatige wijzigingen te maken. De kosten van niet adopteren zijn steiler en stapelen zich in de tijd op: sneeuwvlokinfrastructuur die niemand kan herbouwen, trage en foutgevoelige provisioning, beveiligingsmisconfiguraties die tot inbreuken leiden en audits die weken handmatige inspanning verbruiken. Formuleer IaC voor leiderschap als infrastructuur omzetten van een onbeheerde verplichting in een bestuurde, reproduceerbare bezitting, en als het mechanisme dat beveiliging en compliance automatisch maakt in plaats van aspiratief.

## Antipatronen en valkuilen

- **ClickOps in productie.** Wijzigingen met de hand in de console maken garandeert drift en vernietigt reproduceerbaarheid.
- **Geheimen in code.** Inloggegevens hard coderen in definitiebestanden lekt ze in versiegeschiedenis en toestand.
- **Monolithische, ongemodulariseerde definities.** Eén enorme configuratie die niemand durft te wijzigen wordt even broos als de handmatige opzet die ze verving.
- **Onbeheerde toestand.** Lokale of niet-vergrendelde toestandsbestanden leiden tot corruptie en verloren infrastructuur.
- **Getolereerde drift.** Handmatige wijzigingen laten staan erodeert de garantie van de bron van waarheid tot de code fictie is.
- **Beleid als documentatie.** Regels die in een wiki leven in plaats van een geautomatiseerde controle worden routinematig geschonden.
- **Kopieer-plakwildgroei.** Configuratie over teams dupliceren betekent dat reparaties en verbeteringen zich nooit verspreiden.

## Volwassenheidsmodel

**Niveau 1: Initiëren.** Infrastructuur wordt handmatig ingericht via de console en ad hoc scripts. Omgevingen zijn inconsistent, ongedocumenteerd en kunnen niet betrouwbaar worden gereproduceerd, en herstel van een falen is traag en onzeker.

**Niveau 2: Ontwikkelen.** Sommige infrastructuur is gecodeerd, maar praktijken variëren per team. Toestandsbeheer is inconsistent, drift is gangbaar, geheimen lekken soms in definities en beleid wordt, zo al, via handmatige review afgedwongen.

**Niveau 3: Standaardiseren.** Declaratieve IaC is de gedocumenteerde standaard over de organisatie, gebouwd uit gedeelde geversioneerde modules met beheerde, externe, vergrendelde toestand. Policy as code dwingt vangrails af in de pijplijn, geheimen worden uit een speciale beheerder gerefereerd en driftdetectie draait op een regelmatig ritme.

**Niveau 4: Beheersen.** De praktijk wordt gemeten aan de hand van uitgangswaarden. Je volgt driftpercentage en gemiddelde tijd tot verzoening, adoptie van modulversies over teams, geblokkeerde tegenover ontsnapte beleidsschendingen, provisioning-doorlooptijd en het aandeel bronnen dat werkelijk onder code staat. Deze statistieken poorten wijzigingen en sturen waar je investeert, zodat beslissingen op bewijs rusten in plaats van anekdote.

**Niveau 5: Orkestreren.** Infrastructuur is onveranderlijk en GitOps-gedreven, zelfherstellend tegen drift, met complianceonderbouwing automatisch geproduceerd. De module- en beleidsbibliotheek verbetert continu uit echt gebruik en incidenten, en infrastructuurpraktijk is geïntegreerd met beveiligings-, kosten- en leveringsplanning zodat het hele landschap zich aanpast naarmate eisen verschuiven.

## Ideeën voor discussie

- Waar moet de lijn liggen tussen centraal bestuurde modules en teamautonomie om aangepaste infrastructuur te definiëren?
- Hoe handel je de echte noodwijziging af die de pijplijn moet omzeilen, zonder ClickOps te normaliseren?
- Wat is de juiste strategie om toestand over veel accounts en teams te beheren en te beveiligen?
- Wanneer is veranderlijk configuratiebeheer nog gerechtvaardigd tegenover volledig onveranderlijke infrastructuur?
- Hoe houd je de bibliotheek met policy as code afgestemd op evoluerende beveiligings- en regelgevende eisen?
- Hoe ziet een realistisch migratiepad eruit voor legacy-infrastructuur die voor IaC dateert?

## Belangrijkste inzichten

- Definieer infrastructuur declaratief, versioneer haar en behandel haar als beoordeelbare, reproduceerbare code.
- Bouw uit kleine, geversioneerde modules om goede standaarden te verspreiden en duplicatie te elimineren.
- Geef de voorkeur aan onveranderlijke infrastructuur en gouden images om drift af te schaffen en rollback te vereenvoudigen.
- Beheer toestand bewust en houd geheimen buiten definities.
- Neem GitOps aan voor een sterk auditspoor en zelfherstellende verzoening.
- Dwing vangrails af met policy as code zodat compliance in bestaan wordt voorkomen, niet achteraf geaudit.

## Referenties en verder lezen

- Kief Morris, *Infrastructure as Code: Dynamic Systems for the Cloud Age*.
- Yevgeniy Brikman, *Terraform: Up & Running*.
- Betsy Beyer, Chris Jones, Jennifer Petoff, and Niall Richard Murphy (eds.), *Site Reliability Engineering*.
- Gene Kim, Jez Humble, Patrick Debois, and John Willis, *The DevOps Handbook*.
- Weaveworks, "GitOps" foundational writings (Alexis Richardson et al.).
- Open Policy Agent documentation and the Rego policy language.
- NIST Special Publication 800-53, security and privacy controls (configuration management family).
