# 10.8 Volwassenheidsmodellen

## Overzicht en motivatie

Een [volwassenheidsmodel](https://en.wikipedia.org/wiki/Maturity_model) is een gestructureerde manier om te beoordelen hoe bekwaam en consistent je praktijk is op een bepaald domein, en een pad te beschrijven om haar te verbeteren. Het definieert een kleine ladder van niveaus. Onderaan is werk ad hoc en reactief. Bovenaan wordt het gemeten, beheerst en continu geoptimaliseerd. Elke sport heeft waarneembare kenmerken waartegen je kunt toetsen.

Volwassenheidsmodellen zetten een vage vraag ("zijn we hier goed in?") om in een herhaalbaar antwoord ("we zitten hier op niveau 2, daar op niveau 4, en dit is wat niveau 3 zou vragen"). Dit boek gebruikt in elk hoofdstuk een model met vijf niveaus en consolideert ze in hoofdstuk 12.4. Dit hoofdstuk gaat over de discipline zelf: hoe de modellen werken, wanneer ze helpen en hoe ze misleiden.

De reden dat ze ertoe doen is eenvoudig. Grote organisaties kunnen niet verbeteren wat ze niet zien. Over tientallen teams varieert vermogen enorm en onzichtbaar. Sommige teams hebben uitstekend testen en zwakke beveiliging, andere het omgekeerde. Een volwassenheidsmodel geeft je een gedeeld vocabulaire en een gemeenschappelijke maatstaf, zodat gaten vergelijkbaar worden, investeringen kunnen worden geprioriteerd en voortgang in de tijd kan worden gevolgd in plaats van slechts beweerd. Bekende voorbeelden zijn CMMI ([Capability Maturity Model Integration](https://en.wikipedia.org/wiki/Capability_Maturity_Model_Integration), voor proces), het DORA-model ([DevOps Research and Assessment](https://en.wikipedia.org/wiki/DevOps_Research_and_Assessment)) (prestaties van softwarelevering), OWASP SAMM (Software Assurance Maturity Model) en BSIMM (Building Security In Maturity Model) voor softwarebeveiliging, TMMi (Test Maturity Model integration, voor testen), het Agile Fluency-model en volwassenheidsmodellen voor databeheer, plus talloze interne scorekaarten.

Voor onderneming en vooral overheid dragen volwassenheidsmodellen bijzonder gewicht. Overheidscontracten gebruiken al lang CMMI-beoordelingsniveaus als leverancierskwalificatie, en kaders als de Amerikaanse CMMC ([Cybersecurity Maturity Model Certification](https://en.wikipedia.org/wiki/Cybersecurity_Maturity_Model_Certification)) koppelen cyberbeveiligingsvolwassenheid direct aan geschiktheid voor defensiewerk. Dat geeft volwassenheidsmodellen echte tanden. Het creëert ook het centrale risico van dit hoofdstuk: wanneer een niveau een poort of doel wordt, optimaliseren mensen voor de beoordeling in plaats van het onderliggende vermogen. Goed gebruikt zijn volwassenheidsmodellen een spiegel. Slecht gebruikt zijn ze toneel.

## Kernprincipes

- **Volwassenheid is een middel, geen doel.** Het doel is vermogen en uitkomsten, geen niveaunummer.
- **Beoordeel om te leren, niet om te scoren.** Eerlijke zelfbeoordeling verslaat een vleiende beoordeling.
- **Hoger is niet altijd beter.** Het juiste doel hangt af van risico, context en kosten.
- **Meet per domein, niet één globaal cijfer.** Vermogen is ongelijk. Eén getal verbergt het.
- **Prioriteer eerst de gaten met de laagste volwassenheid en het hoogste risico.**
- **Pas op voor [de wet van Goodhart](https://en.wikipedia.org/wiki/Goodhart%27s_law).** Zodra een niveau een doel is, meet het geen vermogen meer.
- **Beoordeel periodiek opnieuw.** Volwassenheid drijft af naarmate mensen, systemen en dreigingen veranderen.

## Aanbevelingen

### Kies het juiste model voor het domein

Stem het model af op het vermogen dat je wilt verbeteren en geef de voorkeur aan gevestigde, op bewijs gebaseerde modellen boven verzonnen waar ze bestaan:

- **Proces en oplevering:** CMMI (brede procesvolwassenheid), het DORA-vermogensmodel (leveringsprestaties, gegrond in onderzoek, hoofdstuk 11.2).
- **Beveiliging:** OWASP SAMM en BSIMM (softwarebeveiligingspraktijken), CMMC (cyberbeveiliging in defensie).
- **Testen en kwaliteit:** TMMi.
- **Agile en werkwijzen:** het Agile Fluency-model (hoofdstuk 10.7).
- **Data:** volwassenheidsmodellen voor databeheer (DMM, DCAM).

Voor intern gebruik is een eenvoudige schaal van vier of vijf niveaus toegepast per vermogen (zoals dit boek doet) vaak uitvoerbaarder dan een zwaar extern kader. Reserveer formele, beoordeelde modellen voor waar ze contractueel vereist zijn.

### Beoordeel eerlijk en per vermogen

Draai beoordelingen die waarheid produceren, geen comfort. Betrek de mensen die het werk doen. Verzamel bewijs in plaats van meningen. Score elk vermogen apart, zodat het plaatje de werkelijkheid weerspiegelt: hier sterk, daar zwak. Een zelfbeoordeling gebruikt om verbetering te sturen is meer waard dan een externe beoordeling gebruikt om een badge te verdienen, omdat de eerste openhartigheid beloont en de tweede presentatie. Hoofdstuk 12.4 biedt een geconsolideerde zelfbeoordeling over elk domein in dit boek. Gebruik haar als beginpuntinstrument.

### Gebruik volwassenheid om te prioriteren, niet om te straffen

De uitkomst van een beoordeling is een geprioriteerde verbeterachterstand, geen rapportkaart om te beschuldigen. Combineer volwassenheid met risico. Een vermogen op niveau 1 in een gebied met laag risico kan prima zijn. Een vermogen op niveau 2 in een veiligheids- of compliancekritiek gebied is urgent. Richt investeringen op de gaten waar lage volwassenheid hoog risico ontmoet en verbind het werk aan uitkomsten (hoofdstuk 11.1) zodat verbetering wordt gemeten aan resultaten, niet aan de ladder beklimmen om haar zelf.

### Stel doelniveaus bewust: hoger is niet gratis

Elk niveau hoger kost inspanning en voegt vaak procesgewicht toe. Het juiste doel is zelden "niveau 5 overal." Het is het niveau waar het extra vermogen de extra kosten nog rechtvaardigt voor het risico van dat domein. Gereguleerde en veiligheidskritieke vermogens kunnen werkelijk de bovenste sporten nodig hebben, en audit vereist vaak minstens een "gedefinieerd" niveau 3. Veel andere zijn goed bediend op niveau 3 en zouden door verder te duwen slechts bureaucratie opstapelen. Besluit doelen per vermogen en stop met klimmen wanneer het risicogecorrigeerde rendement dat doet.

### Waak tegen volwassenheidstoneel

De ene faalwijze die de waarde van volwassenheidsmodellen vernietigt is optimaliseren voor de score. Let op beoordelingen die royaal scoren, bewijs dat alleen voor de beoordeling wordt samengesteld of claims van "niveau 5" die productie-incidenten tegenspreken. Houd de beoordeling gekoppeld aan waarneembaar gedrag en echte uitkomsten. Roteer je beoordelaars of laat ze extern controleren. Behandel een verdacht hoge zelfscore als geurtje. Op het moment dat het niveau het doel wordt, houdt het model op je de waarheid te vertellen.

## Afwegingen: voor- en nadelen

| Aanpak | Voordelen | Nadelen |
|---|---|---|
| **Formele beoordeelde modellen (CMMI, CMMC)** | Vergelijkbaar, contractueel erkend, rigoureus | Kostbaar. Nodigt uit tot bespelen. Kan proces laten verstenen |
| **Lichte interne scorekaarten** | Snel, uitvoerbaar, lage overhead | Minder extern vergelijkbaar. Makkelijk te vertekenen |
| **Op bewijs gebaseerde vermogensmodellen (DORA)** | Gekoppeld aan echte uitkomsten. Door onderzoek gesteund | Smallere reikwijdte. Vraagt echte statistieken |
| **Eén totaal volwassenheidscijfer** | Eenvoudig te communiceren | Verbergt ongelijk vermogen. Misleidt |
| **Beoordeling per vermogen** | Nauwkeurige, uitvoerbare prioritering | Meer inspanning. Geen enkel kopgetal |

De centrale spanning is **beoordeling als spiegel tegenover beoordeling als doel**. Hetzelfde model dat een team zichzelf helder laat zien wordt contraproductief op het moment dat een niveau aan beloning, geschiktheid of status wordt gekoppeld. Hoe meer een niveau uitmaakt, hoe meer energie naar de schijn van volwassenheid stroomt in plaats van de inhoud.

## Vragen om met je team te bespreken

1. **Moeten we een openhartige interne zelfbeoordeling gescheiden houden van elk contractueel beoordeeld niveau, en wie bezit elk?** Wanneer een CMMC- of CMMI-niveau omzet poort, drijven de beoordeling en de waarheid uit elkaar, omdat energie naar slagen stroomt in plaats van verbeteren. Voor een grote onderneming of een overheidsleverancier is dat gat waar risico zich verbergt: je slaagt voor de audit en blijft blootgesteld. Houd bewust twee boeken. Houd de formele beoordeling voor geschiktheid, en houd een botte interne scorekaart waarvoor niemand wordt beloond om op te blazen. Noem een eigenaar voor elk en behandel elke afstand tussen beide als signaal om te onderzoeken, niet om toe te dekken. Neem recente incidenten, bijna-ongelukken en verval na beoordeling mee naar de vergadering als bewijs welk boek de waarheid vertelt.

2. **Nemen we voor elk domein een gevestigd model op bewijs aan of verzinnen we ons eigen scorekaart, en is dat de juiste keuze?** Gevestigde modellen (DORA voor oplevering, SAMM of BSIMM voor beveiliging, TMMi voor testen) dragen onderzoek en externe vergelijkbaarheid die een zelfgemaakt raster niet kan evenaren. Een lichte interne schaal van vier niveaus is sneller en uitvoerbaarder, en is vaak de betere keuze voor interne sturing. De valkuil is een zwaar maatwerkkader te verzinnen dat alle ceremonie van een formeel model heeft en geen van de bewijsbasis. Besluit per domein: reserveer formele beoordeelde modellen voor waar een contract ze vereist, gebruik op bewijs gebaseerde modellen waar ze bestaan en passen, en houd een eenvoudige schaal per vermogen voor al het overige. Neem de lijst domeinen mee, markeer welk model elk vandaag gebruikt en daag elke verzonnen scorekaart uit.

3. **Wie draait onze beoordelingen, hoe zouden we royale scoring vangen en hoe vaak beoordelen we opnieuw?** Een beoordeling die zichzelf cijfert vleit zichzelf, en volwassenheid drijft af naarmate mensen, systemen en dreigingen veranderen, dus een beoordeling van twee jaar oud is vaak fictie. Roteer beoordelaars of haal een externe controle binnen en behandel een verdacht hoge zelfscore als geurtje om na te jagen, niet als overwinning om te vieren. Stel een ritme voor herbeoordeling in gekoppeld aan hoe snel elk domein verandert: beveiliging vaker dan bijvoorbeeld documentatie. Verzamel bewijs en betrek de mensen die het werk doen in plaats van meningen van managers te verzamelen. Als je antwoord is dat één team zichzelf eens per jaar scoort zonder kruiscontrole, meet je comfort, geen vermogen.

4. **Welk doelniveau van volwassenheid heeft elk vermogen werkelijk nodig, en waar zou hoger duwen ons slechts procesgewicht kopen?** Hoger is niet gratis: elk niveau hoger kost inspanning en voegt meestal ceremonie toe, dus een algemeen doel van niveau 5 overal laat een eindig verbeterbudget wegvloeien in bureaucratie die sommige domeinen nooit zullen terugbetalen. Voor een grote organisatie varieert het juiste doel per vermogen, omdat een gebied met laag risico op niveau 2 prima veilig kan zijn terwijl een veiligheids- of compliancekritiek gebied op hetzelfde niveau een noodgeval is. Neem een risicobeoordeling per vermogen mee, een eerlijke schatting van wat de volgende sport kost aan inspanning en proces en elke audit- of contractuele ondergrens, aangezien veel audits minstens een gedefinieerd niveau 3 vereisen. In omgevingen van onderneming en overheid hebben sommige gereguleerde vermogens werkelijk de bovenste sporten nodig terwijl de meeste goed bediend zijn op niveau 3, dus besluit doelen bewust, vermogen voor vermogen, en stop met klimmen zodra het risicogecorrigeerde rendement dat doet.

5. **Verbeterde de uitkomst die het beschermen moest werkelijk de laatste keer dat we een volwassenheidsniveau verhoogden, of bewoog alleen de score?** Een niveau dat klimt terwijl incidenten, doorlooptijd of defectpercentages vlak blijven is de wet van Goodhart in actie: zodra het getal het doel wordt, meet het geen vermogen meer. Voor een groot team glipt dit er makkelijk door, omdat een geslaagde beoordeling als vooruitgang voelt ook als productie een ander verhaal vertelt. Koppel het niveau van elk vermogen aan een echte uitkomststatistiek voordat je investeert en neem dan het voor-en-na-bewijs mee naar de discussie: incidenten per kwartaal, wijzigingsfaalpercentage, hersteltijd, wat het vermogen ook moet verbeteren. In portfolio's van onderneming en overheid waar een beoordeeld niveau geschiktheid poort is het gat gevaarlijk, omdat het niveau kan stijgen op samengesteld bewijs terwijl de onderliggende praktijk stilletjes vervalt, en het eerste bewijs daarvan is een inbreuk, uitval of mislukte audit.

6. **Communiceren we één kopcijfer van volwassenheid of een beeld per vermogen, en zijn niveaus ooit gekoppeld aan beloning, rangorde of teamstatus?** Een enkel totaalgetal is makkelijk aan leiderschap te presenteren en verbergt precies de ongelijkheid die ertoe doet, omdat sterke oplevering een vermogen op niveau 1 in beveiliging kan maskeren. Een heatmap per vermogen is meer werk maar toont waar lage volwassenheid hoog risico ontmoet. De moeilijkere vraag is hoe de scores worden gebruikt, want op het moment dat een niveau aan de beloning of rangorde van een team wordt gekoppeld, sterft eerlijke rapportage en stroomt inspanning naar de schijn van volwassenheid in plaats van de inhoud. Neem de heatmap mee, en een openhartig verslag van elke plek waar een niveau nu een functioneringsgesprek, een budgetbeslissing of een leveranciersscorekaart voedt. Wees voor ondernemingen en overheidsleveranciers, waar beoordeelde niveaus omzet en geschiktheid kunnen poorten, expliciet over welke cijfers gevolgen hebben en welke slechts bestaan om te sturen, want een volwassenheidsbeeld waarvoor mensen worden beloond om het op te blazen houdt op de werkelijkheid te beschrijven.

## Sectorperspectief

**Startup.** Een zwaar beoordeeld model is overhead die je op een korte runway niet kunt betalen. Draai een zelfbeoordeling van een uur op een eenvoudige schaal over een handvol vermogens, repareer alleen het gat met de laagste volwassenheid dat iets concreets blokkeert (zeg, de beveiligingsvragenlijst van je eerste ondernemingsklant) en laat de rest met rust. De beoordeling moet een middag kosten, geen adviseur, en haar uitkomst is één volgende actie in plaats van een uniforme hoge score die je niet nodig hebt en niet kunt financieren.

**Kleinbedrijf.** Zonder speciale beoordelaar en met een krap budget leen je een licht publiek model in plaats van een maatwerkkader in te kopen: een korte leverings- of beveiligingschecklist die je zelf kunt scoren. Behandel het als jaarlijks gesprek over waar een zwakke plek je een klant zou kosten, niet een permanent programma. Houd het goedkoop en bot, want een vleiende score die je een leverancier betaalde te produceren is minder waard dan een openhartige die je zelf in een middag deed.

**Grote onderneming.** De waarde is een gedeelde scorekaart per vermogen consistent toegepast over veel teams, zodat gaten vergelijkbaar worden en verbeterbudget stroomt naar waar lage volwassenheid hoog risico ontmoet. Waak hard tegen volwassenheidstoneel zodra niveaus budget of status voeden: roteer of controleer beoordelaars extern, en beheer de resultaten als heatmap die investering in gebaande wegen (hoofdstuk 4.2) stuurt in plaats van een ranglijst die teams rangschikt en eerlijke rapportage doodt.

**Overheid.** Een volwassenheidsniveau is hier vaak letterlijk een poort: CMMC voor defensiewerk, een CMMI-beoordeling als leverancierskwalificatie. Voldoe aan het vereiste niveau met echt vermogen en houd een openhartige interne zelfbeoordeling gescheiden van de formele beoordeling zodat de auditondergrens nooit stilletjes het plafond wordt. Documenteer bewijs transparant voor beoordelaars en behandel elke afstand tussen het gecertificeerde niveau en de echte praktijk als verantwoord risico om te sluiten, niet papierwerk om te archiveren.

## Voorbeelden

**Startup.** Een SaaS-startup van tien personen draait een zelfbeoordeling van een uur tegen een eenvoudige schaal van vier niveaus die oplevering, testen, beveiliging en bereikbaarheid dekt. Ze vindt oplevering en testen op niveau 3 maar beveiliging vast op niveau 1, wat ertoe doet omdat ze op het punt staat haar eerste ondernemingsklant te tekenen met een beveiligingsvragenlijst. Dus besteden de oprichters de volgende maand aan beveiliging alleen tot een verdedigbaar niveau 2 verhogen en laten de rest met rust, in plaats van een uniforme hoge score na te jagen die ze nog niet nodig hebben en zich niet kunnen veroorloven.

**Grote onderneming.** Een financiëledienstenbedrijf beoordeelt haar 40 teams met een lichte scorekaart per vermogen (oplevering, testen, beveiliging, observeerbaarheid, bereikbaarheid). De heatmap onthult dat beveiligingsvolwassenheid het meest achterblijft waar de wettelijke blootstelling het hoogst is, dus financiert het platformteam eerst beveiligingstooling op gebaande wegen (hoofdstuk 4.2) voor die teams. Omdat de beoordeling wordt gebruikt om investering te prioriteren in plaats van teams te rangschikken, rapporteren managers eerlijk. Herbeoordeling een jaar later toont echte beweging en, cruciaal, minder beveiligingsincidenten, niet slechts hogere scores.

**Overheid.** Een defensieaannemer moet een vereist CMMC-niveau halen om op werk te bieden, en een systeemintegrator heeft een CMMI-beoordeling als contractkwalificatie. Hier is het volwassenheidsniveau letterlijk een poort naar omzet. De goed gedraaide versie behandelt het vereiste niveau als ondergrens voor echt vermogen en houdt een openhartige interne zelfbeoordeling gescheiden van de formele beoordeling. De slecht gedraaide versie stelt bewijs samen voor de beoordeling en laat de echte praktijk de dag erna vervallen, slagend voor de audit terwijl ze blootgesteld blijft.

## Zakelijke onderbouwing: motivatie, ROI en TCO

Het rendement van volwassenheidsbeoordeling komt uit **gerichte investering**. Verbeterbudgetten zijn eindig. Blind besteed financieren ze wat het luidst is. Een volwassenheidsbeoordeling toont je waar vermogen het zwakst is tegen risico, zodat dezelfde uitgave meer risicovermindering en meer uitkomstverbetering koopt. De beoordeling zelf is goedkoop, slechts dagen gestructureerde, op bewijs gebaseerde review, afgezet tegen de kosten van verkeerd toegewezen verbeterprogramma's of, erger, een niet-gedetecteerd vermogensgat dat boven water komt als inbreuk, uitval of mislukte audit.

Op **total cost of ownership** is de discipline goedkoop wanneer je haar licht houdt en duur wanneer ze verhardt tot beoordelingsbureaucratie. De dominante verborgen kost is *volwassenheidstoneel*: inspanning besteed aan de schijn van volwassenheid produceren levert niets op en kan echt risico maskeren, wat negatieve ROI is. Maak de zaak voor leiderschap door volwassenheid te presenteren als risico-en-investeringslens, een heatmap die "verbeter alles" omzet in "verbeter eerst deze drie dingen," en begroot expliciet tegen de verleiding niveaus om hun eigen wil na te jagen. Waar een niveau contractueel vereist is (CMMC, CMMI), is de ROI direct: het is de prijs van geschiktheid, en het doel is eraan te voldoen met echt vermogen in plaats van dure schijn.

## Antipatronen en valkuilen

- **Niveau als doel:** een getal najagen in plaats van het vermogen dat het moet vertegenwoordigen.
- **Volwassenheidstoneel:** bewijs samenstellen voor een beoordeling terwijl de echte praktijk vervalt.
- **Eén globaal cijfer:** een enkele volwassenheidsscore die gevaarlijke ongelijkheid verbergt.
- **Hoger-is-altijd-beter:** elk vermogen naar niveau 5 duwen ongeacht risico of kosten.
- **Eenmaal beoordelen, nooit weer:** een eenmalige beoordeling behandeld als permanente waarheid.
- **Teams rangschikken om te beschuldigen:** volwassenheid gebruiken voor straf, wat eerlijke rapportage doodt.
- **Modelaanbidding:** de ceremonie van een zwaar kader volgen voorbij het punt van nut.
- **Uitkomsten negeren:** de ladder beklimmen terwijl oplevering, betrouwbaarheid of beveiliging niet verbeteren.

## Volwassenheidsmodel

- **Niveau 1, Initiëren.** Geen gedeeld begrip van volwassenheid. Vermogen wordt aangenomen, is ongelijk en ongemeten. Elke beoordeling is reactief, getriggerd door een incident of een auditeis in plaats van gepland.
- **Niveau 2, Ontwikkelen.** Een paar teams draaien ad-hocbeoordelingen tegen een of andere schaal, maar model, ritme en nauwkeurigheid variëren per team. Resultaten worden inconsistent gebruikt en bewijs is dun, dus scoren voor de schijn is een altijd aanwezig risico.
- **Niveau 3, Standaardiseren.** Eén model per vermogen en beoordelingsritme zijn gedocumenteerd en organisatiebreed toegepast. Beoordelingen zijn op bewijs gebaseerd, betrekken de mensen die het werk doen en voeden een geprioriteerde verbeterachterstand in plaats van een rapportkaart.
- **Niveau 4, Beheersen.** Volwassenheid wordt gemeten en beheerst met data: het niveau van elk vermogen wordt gevolgd tegen een uitgangswaarde, gekoppeld aan een uitkomststatistiek (incidenten, doorlooptijd, wijzigingsfaalpercentage) en volgens een vast ritme opnieuw beoordeeld, zodat afdrijving en royale scoring als getallen verschijnen in plaats van meningen, en doelen bewust per domein worden gesteld tegen risico en kosten.
- **Niveau 5, Orkestreren.** Beoordeling is over de organisatie geïntegreerd en wordt continu verbeterd: volwassenheid, risico en uitkomsten informeren investering als één adaptief beeld, doelen worden herbalanceerd naarmate dreigingen en context verschuiven, beoordelaars worden vanzelfsprekend geroteerd of extern gecontroleerd en de praktijk schaft actief ceremonie af die haar kosten niet meer verdient.

## Ideeën voor discussie

1. Welke van je vermogens neem je aan dat volwassen zijn zonder bewijs?
2. Waar valt je laagste volwassenheid samen met je hoogste risico, en gaat je verbeterbudget daarheen?
3. Is enig volwassenheidsniveau in je organisatie een doel of een poort? Welk gedrag heeft dat opgeleverd?
4. Wat is het juiste doelniveau voor elk vermogen, en waar zou verder klimmen slechts bureaucratie toevoegen?
5. Zouden je teams hun volwassenheid eerlijk rapporteren, of straft de manier waarop je scores gebruikt openhartigheid?
6. Toen je voor het laatst "volwassenheid verbeterde," veranderden de uitkomsten dan werkelijk?

## Belangrijkste inzichten

- Een volwassenheidsmodel beoordeelt vermogen tegen een ladder van niveaus en beschrijft een pad om te verbeteren: een spiegel, geen trofee.
- Kies per domein gevestigde, op bewijs gebaseerde modellen (CMMI, DORA, SAMM/BSIMM, CMMC). Een lichte schaal per vermogen is vaak het meest uitvoerbaar.
- **Beoordeel eerlijk, per vermogen**, en gebruik resultaten om **te prioriteren op risico**, niet om te rangschikken of te beschuldigen.
- **Hoger is niet altijd beter:** stel doelniveaus bewust tegen risico en kosten.
- Pas op voor **volwassenheidstoneel** en **de wet van Goodhart**: een niveau dat een doel wordt meet geen vermogen meer.
- Zie hoofdstuk 12.4 voor de geconsolideerde volwassenheidszelfbeoordeling van dit boek, en het eigen volwassenheidsgedeelte van elk hoofdstuk.

## Referenties en verder lezen

- CMMI Institute / ISACA, *Capability Maturity Model Integration (CMMI)*.
- Watts Humphrey, *Managing the Software Process* (origins of software process maturity).
- Nicole Forsgren, Jez Humble, Gene Kim, *Accelerate* (capability, not maturity-level, thinking for delivery).
- OWASP, *Software Assurance Maturity Model (SAMM)*; BSIMM (*Building Security In Maturity Model*).
- U.S. Department of Defence, *Cybersecurity Maturity Model Certification (CMMC)*.
- TMMi Foundation, *Test Maturity Model integration*.
- James Shore and Diana Larsen, *The Agile Fluency Model*.
- Martin Fowler, "Maturity Model" (bliki), on their uses and abuses.
