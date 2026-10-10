# 1.5 Besluitvorming en governance

## Overzicht en motivatie

Elk softwaresysteem is de som van duizenden beslissingen: welke [database](https://en.wikipedia.org/wiki/Database), welke architectuur, welke bibliotheek, bouwen of kopen, wanneer je schuld aangaat en wanneer je die aflost. Governance is hoe je deze beslissingen goed en consistent neemt, de juiste mensen betrekt zonder knelpunten te creëren en de redenering bewaart zodat toekomstige teams niet gedoemd zijn haar opnieuw te leren. In een klein team gebeuren beslissingen in gesprek en leven ze in gedeeld geheugen. Op schaal verdampt dat geheugen. Mensen vertrekken, teams reorganiseren en het "waarom" achter een kritieke keuze gaat verloren, waardoor opvolgers haar ofwel blind kopiëren ofwel blind eruit slopen. Goede governance is de machinerie die beslissingen zichtbaar, weloverwogen en duurzaam maakt in een grote, veranderende organisatie.

De centrale uitdaging voor grote teams is autonomie afwegen tegen afstemming. Duw je alle beslissingen omhoog naar een centrale raad, dan krijg je consistentie, maar ten koste van verlammende knelpunten en machteloze teams. Duw je alle beslissingen omlaag, dan krijg je snelheid, maar ten koste van chaos: onverenigbare technologieën, dubbel werk en herhaalde fouten. Het volwassen antwoord is noch centralisatie noch anarchie. Het is een gelaagd model. Teams beslissen de meeste dingen lokaal binnen een goed gemarkeerde "gebaande weg", terwijl een licht, transparant proces de werkelijk overkoepelende en moeilijk omkeerbare keuzes bestuurt. Het doel is goede beslissingen de makkelijke standaard te maken en schaarse governance-aandacht alleen te besteden waar het echt telt.

Ondernemingen en overheden dragen verhoogde belangen. Ze moeten voldoen aan auditors, toezichthouders en controleorganen die gedocumenteerde, verdedigbare beslissingen eisen. Ze werken met lange tijdshorizonnen, waarbij een slechte architectuurkeuze of een onbeheerde stapel [technische schuld](https://en.wikipedia.org/wiki/Technical_debt) hen tien jaar kan belasten. En hun aanbestedings- en complianceverplichtingen maken beslissingen over bouwen of kopen bijzonder ingrijpend en moeilijk om te keren. Voor deze organisaties is gedisciplineerde, goed vastgelegde besluitvorming geen bureaucratie om de bureaucratie. Het is risicobeheer, institutioneel geheugen en het fundament van verantwoording.

## Kernprincipes

- Leg beslissingen en hun redenering vast. Een beslissing zonder motivering is een risico.
- Leg beslissingen op het laagste niveau dat de context heeft, binnen heldere kaders.
- Stem het gewicht van het proces af op het gewicht en de omkeerbaarheid van de beslissing.
- Onderscheid omkeerbare ("tweewegdeur") van onomkeerbare ("eenwegdeur") beslissingen en bestuur ze verschillend.
- Geef de voorkeur aan gebaande wegen en standaarden boven goedkeuringen per geval.
- Behandel technische schuld als een beheerd portfolio, niet als een morele tekortkoming om te verbergen.
- Maak governance transparant. Verborgen besluitvorming kweekt wantrouwen en herwerk.

## Aanbevelingen

### Hanteer Architecture Decision Records en een passend gedimensioneerd RFC-proces

Een [Architecture Decision Record](https://en.wikipedia.org/wiki/Architectural_decision) (ADR) is een kort, onveranderlijk document dat één belangrijke beslissing vastlegt: de context, de overwogen opties, de gemaakte keuze en de gevolgen. Sla ADR's op in versiebeheer naast de code, zodat de redenering met het systeem meereist. Gebruik voor beslissingen die input nodig hebben voordat ze worden genomen een licht [RFC](https://en.wikipedia.org/wiki/Request_for_Comments)-proces (request for comments): laat een voorstel rondgaan, nodig gedurende een afgebakende periode uit tot commentaar, beslis dan en leg vast. Houd beide licht. De waarde zit in het denken en het duurzame verslag, niet in uitgebreide sjablonen. Samen veranderen ADR's en RFC's impliciete, vergeten redeneringen in een doorzoekbaar institutioneel geheugen.

### Bestuur via gebaande wegen, niet via poortwachters

In plaats van elke beslissing een voor een te beoordelen, investeer je in een "gebaande weg": een set goedgekeurde, goed ondersteunde standaarden, toegestane talen, frameworks, deploymentpipelines en patronen, die teams met weinig wrijving en veel ondersteuning kunnen overnemen. Teams die op de gebaande weg blijven, hebben weinig governance nodig, omdat de veilige, compliante keuze ook de makkelijke is. Teams met een echte reden om hem te verlaten, mogen dat, maar nemen de extra verantwoordelijkheid en een lichte review op zich. Dit "golden path"-model schaalt veel beter dan een centrale raad die alles goedkeurt, omdat het governance verschuift van poortwachterschap per geval naar goed ontworpen standaarden.

### Gebruik architectuurreviewraden spaarzaam en transparant

Een architectuurreviewraad, of het equivalent daarvan, heeft een legitieme rol voor de grootste, meest overkoepelende of meest onomkeerbare beslissingen, en voor het vaststellen van de standaarden die de gebaande weg definiëren. Houd zijn reikwijdte smal, zijn criteria gepubliceerd en zijn proces snel en adviserend, niet een verplicht knelpunt voor routinewerk. De taak van de raad is samenhang bewaken en kennis delen, niet elke keuze goedkeuren. Wanneer een raad een wachtrij wordt waar elk project in moet wachten, is hij mislukt. Delegeer fel en bewaar centrale review voor de enkele beslissingen die het werkelijk verdienen.

### Maak bouwen-versus-kopen-versus-overnemen een weloverwogen analyse

Weeg voor elke belangrijke capaciteit drie wegen af: in eigen huis bouwen, een commercieel product kopen of een [open source](https://en.wikipedia.org/wiki/Open-source_software)-oplossing overnemen. Bouw wanneer de capaciteit een echt onderscheidend vermogen is en kern van je missie. Koop of neem over wat ongedifferentieerd is en wat anderen beter doen. Tel de [total cost of ownership](https://en.wikipedia.org/wiki/Total_cost_of_ownership) (TCO) mee, niet alleen de prijs vooraf. Kopen brengt licentie-, integratie- en [lock-in](https://en.wikipedia.org/wiki/Vendor_lock-in)-kosten met zich mee. Bouwen brengt eeuwigdurend onderhoud en bezetting met zich mee. Open source overnemen brengt verplichtingen rond ondersteuning en beveiligingsopvolging met zich mee. Leg de beslissing en haar aannames vast als ADR, zodat je haar kunt herzien wanneer omstandigheden veranderen.

### Beheer technische schuld als portfolio

Technische schuld is niet inherent slecht. Soms is het aangaan ervan om eerder op te leveren de juiste keuze. Wat slecht is, is onbeheerde, onzichtbare, vergeten schuld. Houd een expliciete inventaris bij van belangrijke schuld. Noteer voor elk item de kosten die het oplegt (de doorlopende "rente") en de kosten om het te herstellen. Beheer het dan als een financieel portfolio. Los schuld met hoge rente af die het team elke dag vertraagt. Tolereer schuld met lage rente in stabiele hoeken. Neem schuldbeslissingen bewust in plaats van per ongeluk. Reserveer een vast deel van de capaciteit om schuld af te lossen, zodat die nooit uitgroeit tot een crisis.

### Onderscheid omkeerbare van onomkeerbare beslissingen

Niet alle beslissingen verdienen evenveel overweging. Omkeerbare "tweewegdeur"-beslissingen zijn gemakkelijk ongedaan te maken, dus neem ze snel en lokaal, door het team, met een voorkeur voor handelen. Er te lang over piekeren verspilt tijd en vertraagt het leren. Onomkeerbare of kostbaar om te keren "eenwegdeur"-beslissingen, een publiek [API](https://en.wikipedia.org/wiki/API)-contract, een datamodel op schaal, een meerjarige leveranciersverplichting, verdienen trage, zorgvuldige, senior overweging en een vastgelegde motivering. Beslissingen zo indelen is een van de gewoonten met de hoogste hefboom in governance. Het richt schaarse aandacht waar die loont, en deblokkeert al het andere.

## Afwegingen: voor- en nadelen

| Governance-aanpak | Voordelen | Nadelen |
| --- | --- | --- |
| Centrale reviewraad voor alles | Maximale consistentie en toezicht | Ernstig knelpunt. Ontneemt teams hun bevoegdheid. Traag |
| Gebaande weg met lokale autonomie | Schaalt, snel, veilige standaard, versterkt teams | Vraagt platforminvestering vooraf. Enige afdrijving van de weg |
| Volledige teamautonomie, geen governance | Snel, sterk eigenaarschap | Fragmentatie, duplicatie, herhaalde fouten |
| ADR's / RFC's | Duurzaam geheugen, betere beslissingen, transparantie | Schrijfoverhead. Genegeerd als niet onderhouden |

| Sourcingkeuze | Voordelen | Nadelen |
| --- | --- | --- |
| Bouwen | Volledige controle, past precies, kan onderscheiden | Eeuwigdurende onderhouds- en bezettingskosten |
| Kopen | Snel, ondersteund, iemand anders onderhoudt het | Licentiekosten, lock-in, onvolmaakte pasvorm |
| Overnemen (open source) | Geen licentiekosten, controleerbaar, gemeenschap | Ondersteunings- en beveiligingslast komt bij jou te liggen |

De verbindende afweging is controle tegenover snelheid, en centrale consistentie tegenover lokale autonomie. Elke governancekeuze zit op dit spectrum. De aanbevolen houding, gebaande wegen plus delegeren op basis van omkeerbaarheid, koopt bewust het grootste deel van de snelheid van autonomie terwijl de consistentie die ertoe doet behouden blijft. Dat doet ze door de afgestemde keuze de makkelijke te maken en zwaar proces te bewaren voor de zeldzame onomkeerbare beslissing.

## Vragen om met je team te bespreken

1. **Wie bepaalt of een bepaalde beslissing een eenwegdeur is, en hoe vang je misclassificaties in beide richtingen op?** Beslissingen indelen op omkeerbaarheid is een van de gewoonten met de hoogste hefboom in governance, en haar waarde stort in als je dingen verkeerd labelt: behandel je een omkeerbare keuze als onomkeerbaar, dan verdrink je haar in overweging, behandel je een onomkeerbare als omkeerbaar, dan lever je een datamodel of publiek API-contract op dat je niet goedkoop ongedaan kunt maken. Het tegengestelde risico is dat de persoon het dichtst bij het werk bevooroordeeld kan zijn richting snelheid, terwijl een centrale raad bevooroordeeld kan zijn richting voorzichtigheid. Neem concrete voorbeelden mee naar de discussie: wat zou het daadwerkelijk kosten, in tijd en geld, om elke beslissing om te keren, en wie draagt die kosten. In onderneming en overheid maken aanbestedingsverplichtingen en data op schaal van veel keuzes eenwegdeuren die vooraf omkeerbaar leken. Kom overeen wie indeelt, en bouw de gewoonte van een snelle tweede mening bij alles in de buurt van de grens, zodat schaarse aandacht landt waar omkeren werkelijk duur is.

2. **Wie bezit, financiert en bemant de gebaande weg, en wat voorkomt dat hij vervalt tot een poortwachter?** Een gebaande weg werkt alleen als de goedgekeurde standaarden werkelijk goed ondersteund en makkelijker zijn dan de alternatieven, en dat vraagt aanhoudende investering die makkelijk onderfinancierd raakt. De afweging is scherp: een onderbezette gebaande weg wordt een reeks verplichtingen zonder ondersteuning, precies het poortwachterschap dat het model moest vervangen, en teams gaan er dan omheen. Neem bewijs van de gezondheid van de weg mee: adoptiepercentages, hoe actueel de goedgekeurde tools zijn, hoe snel het platformteam reageert en hoe vaak teams een verzoek indienen om van de weg af te gaan. Voor grote en gereguleerde organisaties is de gebaande weg ook hoe de compliante keuze de makkelijke wordt, dus haar financiering is een complianceinvestering, niet alleen een gemak. Bepaal een duidelijke eigenaar en een vast budget, en meet of teams de weg kiezen omdat hij werkelijk de makkelijkste route is.

3. **Waar sturen teams om je governance heen, en wat vertelt die shadow IT je?** Teams ontwijken het goedgekeurde pad wanneer het pijnlijker is dan de omweg, dus wijdverspreide shadow IT is minder een disciplineprobleem dan een ontwerpoordeel over je governance. De overwegingen zijn reëel: sommige ontwijking is roekeloos, en veel ervan is rationele ontwijking van een reviewraad die een wachtrij van weken is geworden. Neem het bewijs mee: welke goedkeuringen worden overgeslagen, welke onofficiële tools zich stilletjes hebben verspreid en hoe lang het officiële pad werkelijk duurt. In onderneming en overheid zijn de belangen hoger, omdat niet-goedgekeurde tools audit-, beveiligings- en aanbestedingsverplichtingen kunnen schenden die juridisch gewicht hebben. Als het patroon laat zien dat mensen om een knelpunt heen sturen, is de oplossing de gebaande weg sneller en breder te maken en de reikwijdte van de raad te beperken tot de enkele overkoepelende, onomkeerbare beslissingen, niet om meer goedkeuringen toe te voegen.

4. **Hoeveel van onze leveringscapaciteit gaat er daadwerkelijk naar het aflossen van technische schuld, en kunnen we de items met de hoogste rente noemen waar dat eerst op moet gericht zijn?** Technische schuld gedraagt zich als samengestelde rente, een stille belasting op elke toekomstige wijziging, en een grote organisatie kan haar jarenlang dragen voordat iemand merkt dat het systeem traag en broos is geworden om te wijzigen. De concurrerende druk is botweg: elk uur dat aan schuld wordt besteed, is een uur niet besteed aan functies die het bestuur kan zien, dus aflossing is het eerste wat wordt geschrapt als een deadline nadert. Neem echt bewijs mee naar de discussie: een schriftelijke inventaris van belangrijke schuld, een eerlijke inschatting van de doorlopende kosten die elk item oplegt en de kosten om het te herstellen, en het werkelijke deel van de recente capaciteit dat naar aflossing ging tegenover nieuw werk. Voor ondernemingen en overheidsorganen met horizonnen van tien jaar dwingt onbeheerde schuld uiteindelijk een dure herschrijving of een auditbevinding af, dus behandel een vaste aflossingsallocatie als risicobeheer en bepaal wie haar bewaakt als schema's schuiven.

5. **Als we de redenering achter een beslissing van twee jaar geleden nodig hebben, kunnen we haar dan echt vinden, en houdt iemand dat verslag levend?** De hele waarde van een Architecture Decision Record is dat de redenering de mensen overleeft die haar maakten, en die waarde stort in als ADR's eenmaal worden geschreven, nooit worden doorzocht en stilletjes verouderen. De spanning zit tussen de schrijfdiscipline die nodig is om context, opties en gevolgen op het moment van beslissen vast te leggen, en de dagelijkse druk om gewoon op te leveren en door te gaan. Neem concrete toetsen mee naar de discussie: kies drie belangrijke recente beslissingen en kijk of iemand de vastgelegde motivering binnen minuten kan vinden, en controleer of vervangen ADR's als zodanig zijn gemarkeerd in plaats van stilletjes de huidige praktijk tegen te spreken. In onderneming en overheid is dat doorzoekbare verslag precies het verdedigbare bewijs dat auditors en toezichthouders eisen, dus bepaal waar ADR's leven, wie ze beoordeelt en wat een beslissing belangrijk genoeg maakt om vast te leggen.

6. **Wanneer hebben we voor het laatst een belangrijke bouwen-versus-kopen-beslissing heropend tegen haar oorspronkelijke aannames, en zouden we zelfs merken wanneer die aannames verlopen?** Sourcingkeuzes behoren tot de duurste en moeilijkst om te keren beslissingen die je neemt, en de aannames erachter (de prijzen van een leverancier, je eigen bezetting, de volwassenheid van een open source-optie) raken stilletjes verouderd terwijl de beslissing op haar plek bevroren blijft. De overwegingen wegen de verzonken kosten en verstoring van overstappen tegen de oplopende kosten van lock-in, een onvolmaakte pasvorm of een onderhoudslast die je niet meer wilt. Neem de oorspronkelijke ADR en haar uitgesproken aannames mee, een actuele TCO-inschatting voor elke weg inclusief licenties, integratie, bezetting en uitstapkosten, en elk signaal, een prijswijziging of een verlaging van ondersteuning, dat een uitgangspunt is verschoven. Voor overheden en gereguleerde kopers maken aanbestedingsregels en meerjarige contracten deze eenwegdeuren extra bindend, dus spreek vooraf de triggers en de cadans af die een bewuste herbeslissing afdwingen in plaats van een blinde verlenging.

## Sectorperspectief

**Startup.** Bestuur bijna niets en leun zwaar op snelheid: beslis voor omkeerbare tweewegdeur-keuzes aan je bureau en ga verder. Bewaar je ene governance-gewoonte voor de handvol eenwegdeuren, een kerndatamodel of een fundamentele leverancier, en leg elk vast in één alinea zodat een toekomstige teamgenoot het niet van voor af aan opnieuw hoeft te bepleiten. Sla reviewraden en gebaande wegen helemaal over, want op jouw schaal zijn ze overhead die je je niet kunt veroorloven en deelt het hele team al de context.

**Kleinbedrijf.** Zonder architect in dienst maak je bouwen-versus-kopen je centrale governancevraag en beantwoord je die op total cost of ownership in plaats van op voorkeur. Kies standaard voor het kopen of overnemen van goed ondersteunde tools voor alles wat niet je kernonderscheid is, want eeuwigdurend onderhoud is de kost die je het minst kunt dragen. Houd één licht beslissingslogboek bij zodat de redenering achter je enkele ingrijpende keuzes het vertrek van een sleutelpersoon overleeft.

**Grote onderneming.** Je probleem is autonomie afwegen tegen afstemming over veel teams, dus investeer in een gefinancierde gebaande weg en bewaar een smalle, snelle architectuurreviewraad voor de werkelijk overkoepelende en onomkeerbare beslissingen. Standaardiseer ADR's zodat redenering doorzoekbaar institutioneel geheugen wordt, en beheer technische schuld en sourcingkeuzes als portfolio's met vaste budgetten. Meet of teams de weg kiezen omdat hij het makkelijkst is, en verklein elke raad die vervallen is tot een wachtrij.

**Overheid.** Gedocumenteerde, verdedigbare beslissingen zijn hier niet optioneel: auditors en toezichthouders verwachten de redenering, de afgewogen opties en de aannames achter elke ingrijpende keuze te zien. Voer bouwen-versus-kopen uit als vastgelegde TCO-analyse, eerbiedig aanbestedingsregels die enkelvoudige lock-in beperken en bewaar ADR's als auditklaar bewijsspoor. Neem lange tijdshorizonnen serieus, want een datamodel of leveranciersverplichting die je vandaag aangaat, kan de organisatie tien jaar binden, dus beschouw het als een eenwegdeur en overweeg dienovereenkomstig.

## Voorbeelden

**Startup.** Een startup van vier personen neemt de meeste beslissingen in minuten aan een gedeeld bureau, en voor omkeerbare tweewegdeur-keuzes is die snelheid een echt voordeel, dus ze weerstaan elke governance-overhead. Maar wanneer ze een database en een datamodel kiezen die later pijnlijk te wijzigen zijn (een eenwegdeur), pauzeren ze om een notitie van één alinea te schrijven: de opties, de keuze en de aannames erachter. Een jaar later, wanneer ze tegen schaallimieten aanlopen, behoedt die ene notitie hen ervoor de vraag van voor af aan opnieuw te bepleiten. Ze besturen bijna niets, en bewaren hun ene lichte gewoonte voor de enkele beslissingen die werkelijk kostbaar zijn om om te keren.

**Grote onderneming.** De platformteams van een grote onderneming werden verlamd door een architectuurreviewraad die elke technologiekeuze moest goedkeuren, wat wachtrijen van weken creëerde. De onderneming herstructureerde governance rond een gebaande weg: een samengestelde catalogus van goedgekeurde, volledig ondersteunde talen, datastores en pipelines die teams direct konden overnemen. ADR's legden elke beslissing vast om af te wijken, en een snelle, adviserende review handelde alleen keuzes buiten de weg af. De reikwijdte van de raad kromp tot het vaststellen van standaarden en de handvol werkelijk overkoepelende beslissingen. De oplevering versnelde sterk. De consistentie verbeterde zelfs, omdat het makkelijke pad nu het compliante was. En het ADR-archief gaf de organisatie een doorzoekbaar verslag van waarom dingen waren gebouwd zoals ze waren.

**Overheid.** Een overheidsdepartement stond voor een grote bouwen-of-kopen-beslissing over een casemanagementplatform onder strikte aanbestedings- en auditregels. In plaats van op voorkeur te beslissen, voerde het een gedocumenteerde TCO-analyse uit over drie opties: maatwerk bouwen, een commercieel product kopen en een open source-basis overnemen. Het woog licenties, integratie, onderhoud op lange termijn, bezetting en lock-in af, en legde de beslissing en haar aannames vast als ADR. Jaren later, toen de voorwaarden van een leverancier veranderden, heropende het departement die ADR, stelde vast dat de oorspronkelijke aannames niet meer golden en besloot opnieuw met volledige kennis van de eerdere redenering, waarmee een blinde en kostbare migratie werd vermeden. De vastgelegde motivering was ook precies het verdedigbare bewijs dat auditors vereisten.

## Zakelijke onderbouwing: motivatie, ROI en TCO

Beslissingen zijn de kostenpost met de hoogste hefboom en de laagste zichtbaarheid in software. Eén slechte, onomkeerbare architectuur- of sourcingkeuze kan jaren van belemmering opleveren of een herstel van negen cijfers. Goed besturen, een paar uur overweging en een schriftelijk verslag, kost daarbij vrijwel niets. Het rendement van ADR's en delegeren op basis van omkeerbaarheid komt uit twee bronnen: dure fouten vermijden bij de eenwegdeur-beslissingen, en verspilde overweging en herwerk vermijden bij al het andere. Vastgelegde motivering verlaagt ook sterk de terugkerende kosten van het opnieuw bepleiten van beslechte kwesties en van teams die de bedoeling achter geërfde systemen via reverse engineering reconstrueren.

Technische schuld maakt het TCO-argument concreet. Onbeheerde schuld gedraagt zich precies als samengestelde rente: een groeiende belasting op elke toekomstige wijziging, tot het systeem in feite onhoudbaar wordt en een dure herschrijving eist. Schuld als portfolio beheren, met een vaste capaciteitsallocatie om de items met hoge rente af te lossen, is veel goedkoper dan de uiteindelijke crisis. Goede governance is goedkoop om in te voeren, vooral de discipline om beslissingen op te schrijven en de investering vooraf in een gebaande weg. Haar overslaan is duur: je betaalt in vermijdbare herschrijvingen, lock-in-verrassingen, auditfalen en verloren institutioneel geheugen. Om het bestuur te overtuigen, formuleer je governance in hun taal: risicovermindering, vermeden herwerk, snellere oplevering via de gebaande weg en auditklare verdedigbaarheid. Laat zien dat het doel niet meer proces is maar beter gericht proces, zware aandacht alleen waar omkeren kostbaar is en wrijvingsloze snelheid overal elders.

## Antipatronen en valkuilen

- Ongedocumenteerde beslissingen: redenering gaat verloren op het moment dat de mensen die haar maakten vertrekken.
- Knelpunt van goedkeuringsraden: een centraal orgaan waar elk project achter moet aansluiten.
- Eén proces voor alles: triviale omkeerbare beslissingen door zware review forceren.
- Analyseverlamming: piekeren over gemakkelijk omkeerbare tweewegdeur-beslissingen.
- [Shadow IT](https://en.wikipedia.org/wiki/Shadow_IT): teams die governance volledig ontwijken omdat het goedgekeurde pad te pijnlijk is.
- Onzichtbare technische schuld: schuld die nooit wordt geïnventariseerd, nooit wordt afgelost, stilletjes oploopt.
- Bouw-alles- of koop-alles-reflexen: sourcing uit gewoonte in plaats van TCO-analyse.
- Governancetheater: documenten en raden die voor de schijn bestaan maar beslissingen niet vormgeven.

## Volwassenheidsmodel

- Niveau 1 (Initiëren): Beslissingen zijn ad hoc en niet vastgelegd. Governance is afwezig of een algemeen knelpunt. Technische schuld is onzichtbaar en de redenering achter keuzes verdampt wanneer mensen vertrekken.
- Niveau 2 (Ontwikkelen): Sommige beslissingen worden gedocumenteerd en enige review bestaat, maar de praktijk is inconsistent over teams en het proces past vaak niet bij het gewicht en de omkeerbaarheid van de beslissing.
- Niveau 3 (Standaardiseren): ADR's, een gebaande weg, delegeren op basis van omkeerbaarheid en een schuldinventaris zijn gedocumenteerd en organisatiebreed gehandhaafd, zodat de compliante keuze de makkelijke standaard is en redenering doorzoekbaar.
- Niveau 4 (Beheersen): Governance wordt afgemeten aan uitgangswaarden: adoptie van de gebaande weg, ADR-dekking, doorlooptijd van beslissingen, schuld als aandeel van de capaciteit en percentages uitzonderingen buiten de weg worden gevolgd, en beslissingen om schuld af te lossen of sourcing te herzien worden getriggerd door dat bewijs in plaats van door crisis.
- Niveau 5 (Orkestreren): Governance wordt continu bijgesteld en is geïntegreerd met levering en risicoplanning. Aandacht wordt precies gericht op onomkeerbare beslissingen. Schuld en sourcingkeuzes worden actief herbalanceerd als portfolio's en opnieuw beslist op bewijs naarmate omstandigheden verschuiven.

## Ideeën voor discussie

- Kunnen we voor onze belangrijkste recente beslissingen de vastgelegde redenering erachter vinden?
- Waar is onze governance een knelpunt, en waar is ze afwezig als ze nodig is?
- Welke van onze huidige beslissingen zijn eenwegdeuren, en behandelen we ze als zodanig?
- Hoeveel van onze capaciteit gaat naar het aflossen van technische schuld, en is dat genoeg?
- Volgen onze teams de gebaande weg omdat hij werkelijk het makkelijkste pad is, of sturen ze eromheen?
- Wanneer hebben we voor het laatst een belangrijke bouwen-versus-kopen-beslissing herzien tegen haar oorspronkelijke aannames?

## Belangrijkste inzichten

- Leg belangrijke beslissingen en hun motivering vast met ADR's. Maak redenering duurzaam.
- Bestuur via gebaande wegen en standaarden, niet via poortwachterschap per geval.
- Stem procesgewicht af op beslissingsgewicht en omkeerbaarheid. Delegeer tweewegdeuren, overweeg bij eenwegdeuren.
- Analyseer bouwen-versus-kopen-versus-overnemen op total cost of ownership en leg de aannames vast.
- Beheer technische schuld als expliciet portfolio met een vaste aflossingsallocatie.
- Houd governance transparant en licht. Richt schaarse aandacht waar omkeren kostbaar is.

## Referenties en verder lezen

- Michael Nygard, "Documenting Architecture Decisions" (the original ADR pattern)
- Gregor Hohpe, "The Software Architect Elevator" and "37 Things One Architect Knows"
- Amazon shareholder letters on Type 1 vs Type 2 (one-way vs two-way door) decisions
- Ward Cunningham, the original "technical debt" metaphor
- Martin Fowler, writings on technical debt and evolutionary architecture
- Neal Ford, Rebecca Parsons, Patrick Kua, "Building Evolutionary Architectures"
- Nicole Forsgren, Jez Humble, Gene Kim, "Accelerate" (loosely coupled architecture and autonomy)
- ISO/IEC/IEEE 42010 on architecture description
