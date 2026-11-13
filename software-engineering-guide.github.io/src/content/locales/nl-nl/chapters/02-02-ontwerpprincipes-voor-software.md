# 2.2 Ontwerpprincipes voor software

## Overzicht en motivatie

Ontwerpprincipes voor software zijn heuristieken om code zo in te richten dat je haar in de loop van de tijd kunt begrijpen, wijzigen en uitbreiden. Ze omvatten benoemde afkortingen ([SOLID](https://en.wikipedia.org/wiki/SOLID) voor vijf [objectgeoriënteerde](https://en.wikipedia.org/wiki/Object-oriented_programming) ontwerpprincipes, [DRY](https://en.wikipedia.org/wiki/Don%27t_repeat_yourself) voor don't-repeat-yourself, [KISS](https://en.wikipedia.org/wiki/KISS_principle) voor keep-it-simple, [YAGNI](https://en.wikipedia.org/wiki/You_aren%27t_gonna_need_it) voor you-aren't-gonna-need-it), structurele begrippen ([koppeling](https://en.wikipedia.org/wiki/Coupling_(computer_programming)), [samenhang](https://en.wikipedia.org/wiki/Cohesion_(computer_science)), [scheiding van verantwoordelijkheden](https://en.wikipedia.org/wiki/Separation_of_concerns)), gecatalogiseerde [ontwerppatronen](https://en.wikipedia.org/wiki/Software_design_pattern), modelleerbenaderingen op hoger niveau zoals [Domain-Driven Design](https://en.wikipedia.org/wiki/Domain-driven_design) (software modelleren in de taal van het bedrijfsdomein) en de keuze tussen objectgeoriënteerde, [functionele](https://en.wikipedia.org/wiki/Functional_programming) en [data-georiënteerde](https://en.wikipedia.org/wiki/Data-oriented_design) stijlen. Geen van deze is een wet. Het is gecomprimeerde ervaring, en je moet ze met oordeel toepassen.

Voor grote teams is de waarde van gedeelde principes coördinatie. Wanneer honderden engineers aan hetzelfde systeem werken, hebben ze een gemeenschappelijk vocabulaire nodig voor ontwerpgesprekken en een gemeenschappelijke set standaarden zodat onafhankelijk geschreven modules in elkaar passen. Goed ontwerp is wat veel mensen een systeem parallel laat wijzigen zonder voortdurende botsingen. Het is ook wat een systeem een decennium later nog veranderbaar houdt, de normale levensduur van systemen van ondernemingen en overheden, ver voorbij de diensttijd van hun oorspronkelijke auteurs.

De cruciale vaardigheid is niet principes uit het hoofd leren. Het is weten wanneer elk ervan je misleidt. Elk principe heeft een faalwijze: DRY kan de verkeerde abstractie opleveren, SOLID kan nodeloze indirectie opleveren, YAGNI kan uitbreidbaarheid verhongeren die je werkelijk nodig hebt. Dit hoofdstuk behandelt principes als gereedschap met een toepassingsgebied en benadrukt koppeling en samenhang als de diepere eigenschappen die de afkortingen proberen te dienen.

## Kernprincipes

- Beheer eerst koppeling en samenhang. De meeste benoemde principes zijn indirecte manieren om deze twee eigenschappen te verbeteren.
- Optimaliseer voor verandering: goed ontwerp minimaliseert de kosten van de wijzigingen die je daadwerkelijk zult moeten maken.
- Geef de voorkeur aan het eenvoudigste ontwerp dat nu werkt, maar houd grenzen waar verandering waarschijnlijk is.
- Duplicatie is goedkoper dan de verkeerde abstractie. Wacht tot het patroon duidelijk is.
- Maak afhankelijkheden expliciet en richt ze op stabiele dingen.
- Modelleer het domein in de taal van het domein. Stem softwaregrenzen af op bedrijfsgrenzen.
- Kies paradigma's naar het probleem, niet naar ideologie. De meeste grote systemen zijn pragmatisch gemengd.

## Aanbevelingen

### Gebruik SOLID als lens, niet als checklist

Pas de enkele-verantwoordelijkheid toe om modules samenhangend te houden, dependency inversion om afhankelijkheden op abstracties te richten waar een grens werkelijk bestaat, en open-closed waar uitbreidingspunten echt zijn. Fabriceer geen interfaces, factories en lagen alleen om aan de afkorting te voldoen wanneer er maar één implementatie is en geen tweede in zicht. Indirectie heeft een prijs, en je betaalt die bij elke leesbeurt.

### Pas DRY toe op kennis, niet op tekst

DRY gaat over het niet dupliceren van één gezaghebbend stuk *kennis*. Het gaat niet over het elimineren van regels die slechts op elkaar lijken. Twee stukken code die gelijk lijken maar om verschillende redenen veranderen, moeten gescheiden blijven. Geef de voorkeur aan wat duplicatie boven een voortijdige gedeelde abstractie die niet-verwante dingen koppelt. Haal de abstractie pas eruit zodra het echte patroon twee of drie keer is verschenen.

### Laat KISS en YAGNI speculatie weerstaan

Bouw voor de eisen die je hebt, niet voor de eisen die je je voorstelt. Vermijd speculatieve algemeenheid, zoals configureerbare frameworks, pluginsystemen en uitbreidingspunten waar niemand om gevraagd heeft. Het tegenwicht is dat sommige flexibiliteit werkelijk goedkoper vroeg wordt ingebouwd, zoals een stabiele interface of een schone naad. YAGNI pleit tegen speculatieve *implementatie*, niet tegen doordachte grenzen.

### Ontwerp expliciet voor lage koppeling en hoge samenhang

Laat elke module één goed gedefinieerd ding doen (samenhang) en van zo min mogelijk andere modules afhangen, via smalle interfaces (lage koppeling). Vraag bij het beoordelen van een ontwerp welke wijzigingen over modulegrenzen heen rimpelen. Die rimpelingen zijn de ware maat van koppeling. Scheiding van verantwoordelijkheden is hetzelfde idee toegepast op lagen en overkoepelende zaken.

### Gebruik ontwerppatronen als vocabulaire, pas antipatronen toe als waarschuwingen

Patronen zijn nuttige gedeelde namen voor terugkerende oplossingen. Pak er een wanneer het probleem er werkelijk mee overeenkomt. Leg geen patronen op om verfijnd te lijken, want patroonzware code is vaak een teken van over-engineering. Leer de gangbare [antipatronen](https://en.wikipedia.org/wiki/Anti-pattern) (god objects, bloedarme modellen waar ongepast, big balls of mud, gedistribueerde monolieten) als diagnostische labels.

### Neem Domain-Driven Design aan waar het domein complex is

Gebruik voor systemen met rijke bedrijfsregels de tactische en strategische gereedschappen van DDD: een alomtegenwoordige taal gedeeld met domeinexperts, afgebakende contexten die het systeem opdelen in onafhankelijk gemodelleerde stukken en contextkaarten die beschrijven hoe die stukken zich verhouden. Afgebakende contexten zijn vooral waardevol op ondernemingsschaal, omdat ze teameigenaarschap op modelgrenzen afstemmen. DDD is overkill voor eenvoudige [CRUD](https://en.wikipedia.org/wiki/Create,_read,_update_and_delete)-systemen (create, read, update, delete).

### Kies paradigma's naar geschiktheid

Gebruik objectoriëntatie voor het inkapselen van toestandsgebonden gedrag en het modelleren van domeinen. Gebruik functionele stijl voor transformaties, gelijktijdigheid en voorspelbaarheid via [onveranderlijkheid](https://en.wikipedia.org/wiki/Immutable_object). Gebruik data-georiënteerd ontwerp waar prestaties en cachegedrag domineren. Grote systemen mengen alle drie. Maak de keuze per component en houd de grenzen tussen stijlen schoon.

## Afwegingen: voor- en nadelen

| Principe / aanpak | Goed toegepast | Faalwijze |
|---|---|---|
| SOLID | Heldere naden waar verandering plaatsvindt. Testbare eenheden | Woekering van interfaces en lagen. Indirectie zonder opbrengst |
| DRY | Enkele bron van waarheid voor echte kennis | Verkeerde abstractie die niet-verwante code koppelt |
| KISS / YAGNI | Slanke, begrijpelijke systemen | Te weinig ontworpen naden. Kostbare achteraf-inbouw van benodigde flexibiliteit |
| Ontwerppatronen | Gedeeld vocabulaire. Beproefde structuren | Cargocult met patronen. Toevallige complexiteit |
| Domain-Driven Design | Afgestemde modellen en teams. Getemde complexiteit | Zware ceremonie op eenvoudige domeinen. Misplaatste contextgrenzen |
| Functioneel / onveranderlijk | Voorspelbaarheid. Veiligere gelijktijdigheid | Onhandige pasvorm voor inherent toestandsgebonden problemen. Prestatieverrassingen |

De terugkerende spanning is die tussen te weinig en te veel ontwerp. Te weinig ontworpen systemen stapelen koppeling op en worden star. Te veel ontworpen systemen verdrinken in abstractie die iemand moet begrijpen en onderhouden. Het antwoord is geen vast punt. Het is een discipline: stel beslissingen uit tot je genoeg informatie hebt, terwijl je de naden houdt die je laten bedenken.

## Vragen om met je team te bespreken

1. **Wat is je concrete drempel voor het afsplitsen van een gedeelde abstractie, en hoe voorkom je dat DRY de verkeerde oplevert?** Dit hoofdstuk is botweg dat duplicatie goedkoper is dan de verkeerde abstractie, en dat je moet wachten tot het patroon twee of drie keer is verschenen voordat je het afsplitst. In een groot team is het gevaar dat iemand twee op elkaar lijkende fragmenten samenvoegt in een gedeelde module over teamgrenzen heen, waarna elke toekomstige wijziging aan één aanroeper in de andere rimpelt. Het signaal om mee te nemen is of de duplicaten om dezelfde reden veranderen of nu slechts op elkaar lijken. Spreek een regel van drie af en eis dat een kandidaatabstractie daadwerkelijk samen is veranderd voordat je de aanroepers koppelt. Die ene afspraak voorkomt een klasse koppeling die duur is om te ontwarren zodra veel teams ervan afhangen.

2. **Hoe maak je koppeling en samenhang zichtbaar in ontwerpreview in plaats van ze aan onderbuikgevoel over te laten?** De kernprincipes zetten koppeling en samenhang boven elke afkorting en definiëren koppeling als de wijzigingen die over modulegrenzen rimpelen. Intuïtie schaalt niet over honderden engineers die elk alleen hun hoek van het systeem zien. Neem bewijs mee dat een machine kan produceren: afhankelijkheidsgrafen en co-change-data die laten zien welke modules steeds samen in dezelfde commits worden bewerkt. Voeg een expliciete reviewvraag toe die vraagt welke modulegrenzen een wijziging je dwingt over te steken. Wanneer twee modules altijd samen veranderen, is dat je teken om ze samen te voegen of de grens ertussen te repareren.

3. **Waar ligt in je systemen de lijn tussen een domein dat rijk genoeg is om Domain-Driven Design te rechtvaardigen en een gewone CRUD-app waar het overkill is?** Het hoofdstuk beveelt de afgebakende contexten van DDD aan juist omdat ze teameigenaarschap op modelgrenzen afstemmen, en waarschuwt dat DDD overkill is voor eenvoudige create-read-update-delete-systemen en zonder echt modelleren verwordt tot ceremonie. Dit in beide richtingen verkeerd doen is kostbaar: zware DDD op een dun domein begraaft een eenvoudige app onder ceremonie, terwijl een uitdijend gedeeld model over veel teams voortdurende coördinatie tussen teams afdwingt. Neem de signalen mee die het echt beslissen: de dichtheid van bedrijfsregels en hoeveel teams onafhankelijk stukken moeten bezitten. Bewaar de strategische machinerie voor de complexe kern en laat de eenvoudige randen eenvoudig. Dat houdt je uit de buurt van zowel DDD-theater als de big ball of mud.

4. **Wanneer is een abstractie, interface of ontwerppatroon de indirectie waard die het toevoegt, en wie heeft de bevoegdheid een ontwerp over-engineered te noemen?** Dit hoofdstuk is expliciet dat indirectie een prijs heeft die je bij elke leesbeurt betaalt, en dat het fabriceren van interfaces, factories en lagen om aan SOLID te voldoen of verfijnd te lijken een faalwijze is. In een groot team loopt de druk de andere kant op: reviewers laten extra abstractie door omdat het gedisciplineerd oogt, en niemand wil degene zijn die voor minder structuur pleit. De concurrerende overweging is echt, want sommige naden verdienen hun plek werkelijk en ze later weghalen is duur. Neem concreet bewijs mee naar de discussie: hoeveel implementaties een interface vandaag werkelijk heeft, hoe vaak het uitbreidingspunt ooit is gebruikt en hoeveel bestanden een lezer moet openen om één codepad te volgen. Spreek af dat een enkele implementatie zonder tweede in zicht een standaardreden is om te inlinen, en noem wie een ontwerp over-engineered kan noemen zonder dat het als belediging klinkt. In systemen van ondernemingen en overheden die hun auteurs met een decennium overleven, is gratuite indirectie een belasting die elke toekomstige onderhouder betaalt, dus behandel "wat levert deze abstractie ons op" als een vaste reviewvraag, niet als persoonlijke uitdaging.

5. **Hoe bepaal je welk paradigma elke component gebruikt, objectgeoriënteerd, functioneel of data-georiënteerd, en hoe houd je de grenzen ertussen schoon?** Het hoofdstuk betoogt dat grote systemen pragmatisch gemengd zijn en dat je per component moet kiezen naar geschiktheid, met objectoriëntatie voor toestandsgebonden domeinen, functionele stijl voor transformaties en gelijktijdigheid en data-georiënteerd ontwerp waar prestaties en cachegedrag domineren. Onbeheerd wordt paradigmakeuze een kwestie van wie de module als eerste schreef, en lekt muteerbare toestand in wat zuivere transformaties hoort te zijn, of vecht functioneel purisme tegen een inherent toestandsgebonden probleem. Het bewijs dat de moeite waard is om mee te nemen is waar je werkelijke pijn zit: welke componenten moeilijk te testen zijn door verborgen toestand, welke hot paths cachegebonden zijn en waar de huidige stijl onhandige omwegen afdwingt. Bepaal bewust het standaardparadigma voor elke laag en schrijf op waar de naden tussen stijlen vallen, zodat een functionele kern en een imperatieve rand niet in elkaar overlopen. Voor een gereguleerd of overheidssysteem waar een berekening controleerbaar en reproduceerbaar moet zijn voor een gegeven periode is een onveranderlijke, functionele kern vaak een compliance-eis in plaats van smaak, en die beperking moet de grens bepalen in plaats van erop te volgen.

6. **Hoe voorkom je dat deze principes verharden tot dogma, en waar leg je de redenering achter een ontwerpbeslissing vast zodat een toekomstig team haar kan herzien?** Elk principe in dit hoofdstuk heeft een toepassingsgebied en een faalwijze, en de hele kadering behandelt ze als gereedschap om met oordeel toe te passen in plaats van wetten om af te dwingen. In een groot team wordt een principe stilletjes een regel: DRY verbiedt elke duplicatie, SOLID verplicht een interface per klasse en pragmatische uitzonderingen worden in review geblokkeerd door mensen die de afkorting citeren in plaats van de uitkomst. De spanning is dat enige consistentie honderden engineers werkelijk helpt coördineren, dus je kunt niet simpelweg elk principe optioneel verklaren. Neem voorbeelden mee waar het naar de letter volgen van een principe een slechter ontwerp opleverde, en neem de besluitenlogboeken mee, indien aanwezig, die uitleggen waarom een bepaalde grens of abstractie bestaat. Spreek af dat principes standaarden zijn waarvan een engineer met een vastgelegde reden mag afwijken en leg ingrijpende ontwerpkeuzes vast in een kort architecture decision record, zodat het volgende team de redenering erft en niet alleen de code. In systemen van onderneming en publieke sector, waar de oorspronkelijke auteurs lang weg zijn en audits vragen waarom het systeem gevormd is zoals het is, is dat schriftelijke spoor het verschil tussen een ontwerp dat toekomstige teams veilig kunnen wijzigen en een ontwerp dat ze bang zijn aan te raken.

## Sectorperspectief

**Startup.** Geef de voorkeur aan het eenvoudigste ontwerp dat oplevert en houd één goed gefactoriseerde module tot een echte tweede use case een naad afdwingt. Je schaarse middel is engineeringaandacht, dus voortijdige interfaces, lagen en speculatieve frameworks zijn pure kosten. Volg de regel van drie voordat je enige gedeelde abstractie afsplitst, en laat YAGNI de uitbreidingspunten doden waar nog niemand om vroeg.

**Kleinbedrijf.** Zonder aparte architect en met een krap budget leun je op het ontwerp dat al is ingebakken in de frameworks en bibliotheken die je koopt in plaats van eigen patronen te verzinnen. Bewaar de aangepaste ontwerpinspanning voor de handvol regels die werkelijk jouw bedrijf zijn, en houd al het andere conventioneel zodat een externe medewerker of nieuwe aanwerving het kan lezen. Een beetje duplicatie die je begrijpt verslaat een slimme abstractie die alleen de auteur kan onderhouden.

**Grote onderneming.** De opbrengst van gedeelde principes is coördinatie over veel teams: een gemeenschappelijk vocabulaire voor ontwerpreview en afgebakende contexten die modelgrenzen op teameigenaarschap afstemmen zodat groepen onafhankelijk evolueren. Beheer koppeling en samenhang expliciet met afhankelijkheids- en co-change-data en leg ingrijpende ontwerpbeslissingen vast zodat systemen veranderbaar blijven lang nadat hun auteurs zijn doorgegaan. Bewaak evenzeer tegen de verkeerde abstractie die teams koppelt als tegen de over-engineering die elke lezer belast.

**Overheid.** Controleerbaarheid en reproduceerbaarheid dicteren vaak het ontwerp. Een onveranderlijke, functionele kern laat je een historische berekening exact reproduceren voor een gegeven periode, wat een verward objectgraaf met verborgen muteerbare toestand niet kan garanderen. Geef de voorkeur aan expliciete gepubliceerde contracten boven gedeelde tabellen op contextgrenzen en houd het ontwerp en de besluitenlogboeken leesbaar voor auditors en voor het team dat het systeem een decennium later erft.

## Voorbeelden

**Startup.** Een startup van drie engineers die zijn eerste product bouwt, weerstaat de neiging elke functie op te delen in lagen van interfaces en factories en houdt één goed gefactoriseerde module tot een echte tweede use case opduikt. Wanneer dezelfde logica een derde keer verschijnt in de aanmeldings- en factureringsstromen, halen ze één kleine gedeelde functie eruit in plaats van een speculatief framework. Zo blijft de codebase klein genoeg dat ieder van hen haar in het hoofd kan houden, en vallen de weinige naden die ze trekken waar het product het meest waarschijnlijk verandert.

**Grote onderneming.** Een groot verzekeringsplatform modelleert polis, schade en facturering als afzonderlijke afgebakende contexten, elk bezeten door een toegewijd team met een eigen datamodel en servicegrens. Waar de contexten elkaar ontmoeten, zoals wanneer een schadeclaim naar een polis verwijst, praten ze via expliciete gepubliceerde contracten in plaats van gedeelde databasetabellen. Zo kunnen de drie teams onafhankelijk evolueren, en houdt de alomtegenwoordige taal gesprekken met acceptanten en actuarissen precies. Een eerdere versie had één uitdijend model gedeeld, en elke wijziging vroeg coördinatie tussen teams.

**Overheid.** Een nationaal belastingverwerkingssysteem kiest bewust voor een data-georiënteerde, functionele kern voor zijn berekeningsmotor. Belastingregels worden uitgedrukt als zuivere transformaties over onveranderlijke invoerrecords, wat ze controleerbaar, testbaar en reproduceerbaar maakt voor een gegeven belastingjaar. De imperatieve, toestandsgebonden delen (workflow, notificaties) worden aan de randen gehouden. Auditors kunnen naar een specifieke regelversie wijzen en elke historische berekening exact reproduceren, wat een wettelijke eis is die een verward objectgraaf met verborgen muteerbare toestand niet kon garanderen.

## Zakelijke onderbouwing: motivatie, ROI en TCO

Ontwerpkwaliteit is een investering in de *veranderbaarheid* van een systeem, en veranderbaarheid domineert de total cost of ownership. Het grootste deel van de kosten van een systeem valt na de eerste release, in wijziging en uitbreiding. Goed ontworpen systemen houden de kosten van verandering in de tijd ruwweg vlak. Slecht ontworpen systemen zien de kosten van elke wijziging oplopen tot het systeem in feite niet meer te wijzigen is en moet worden herschreven, de duurste uitkomst van allemaal.

De invoeringskosten zijn vooral vaardigheid en reviewdiscipline: de principes onderwijzen en vooraf ontwerptijd besteden. De kosten van niet invoeren zijn de langzame opbouw van [technische schuld](https://en.wikipedia.org/wiki/Technical_debt), dalende leveringssnelheid, stijgende defectpercentages en uiteindelijke kostbare herschrijvingen. Verbind ontwerpdiscipline om het bestuur te overtuigen aan voorspelbaarheid van levering en het vermijden van herschrijvingsprogramma's, en volg voorlopende indicatoren zoals het faalpercentage van wijzigingen en de tijd om vergelijkbare functies te implementeren in de loop van de tijd. Let ook op het tegenovergestelde falen: te veel investeren in ontwerp voor onzekere toekomsten vernietigt ook waarde. Het argument is dus voor *passend* ontwerp, afgestemd op hoe waarschijnlijk en hoe kostbaar toekomstige verandering is.

## Antipatronen en valkuilen

- **Speculatieve algemeenheid:** uitbreidbaarheid bouwen voor ingebeelde eisen die nooit komen.
- **De verkeerde abstractie:** niet-verwante code samendwingen om DRY te behagen, waardoor koppeling ontstaat die erger is dan duplicatie.
- **Cargocult met patronen:** ontwerppatronen toepassen om hun eigen wil, wat indirectie zonder voordeel toevoegt.
- **Bloedarme of god objects:** modellen zonder gedrag, of objecten die alles doen. Beide signaleren misplaatste verantwoordelijkheden.
- **Gedistribueerde monoliet:** services die fysiek zijn gesplitst maar nog steeds strak gekoppeld zijn, wat de kosten van beide benaderingen combineert.
- **Big ball of mud:** geen herkenbare structuur. Elke wijziging riskeert alles.
- **DDD-theater:** het vocabulaire en de mapstructuur aannemen zonder het domeinmodelleren dat het waarde geeft.

## Volwassenheidsmodel

- **Niveau 1, Initiëren:** Ontwerp is ad hoc en reactief. Koppeling hoopt zich ongecontroleerd op. Principes zijn onbekend of worden als slogans aangehaald, en abstracties verschijnen of verdwijnen naar individuele gewoonte.
- **Niveau 2, Ontwikkelen:** Teams kennen de principes en passen ze toe, maar inconsistent en vaak dogmatisch. Sommige groepen beheren koppeling en samenhang bewust terwijl andere dat niet doen, en er is geen gedeeld vocabulaire in de organisatie.
- **Niveau 3, Standaardiseren:** Een gedeeld ontwerpvocabulaire, een regel van drie voor het afsplitsen van abstracties, analyse van koppeling en samenhang en afgebakende contexten afgestemd op teams zijn gedocumenteerd en organisatiebreed verwacht, consistent toegepast in ontwerpreview in plaats van overgelaten aan individuele smaak.
- **Niveau 4, Beheersen:** Ontwerpgezondheid wordt afgemeten aan uitgangswaarden: koppeling- en co-change-data, faalpercentage van wijzigingen en de tijd om vergelijkbare functies te implementeren worden in de loop van de tijd gevolgd, zodat abstracties en grenzen op bewijs worden toegevoegd, behouden of verwijderd, en over-engineering en de verkeerde abstractie worden opgevangen door data in plaats van mening.
- **Niveau 5, Orkestreren:** Ontwerpdiscipline is geïntegreerd met levering en risicoplanning in de organisatie. Principes worden met nuance en bekende faalwijzen toegepast. Keuzes van paradigma en grenzen zijn bewust en worden continu herzien, en de organisatie refactort, begrenst opnieuw en schaft abstracties routinematig af naarmate het domein en het bewijs verschuiven.

## Ideeën voor discussie

- Hoe onderscheid je een nodige naad van speculatieve algemeenheid voordat je de toekomstige eis hebt?
- Wanneer heeft DRY je team naar de verkeerde abstractie geleid, en hoe herkende je dat?
- Waar moeten de grenzen van afgebakende contexten vallen, en hoe nauw moeten ze het organigram spiegelen?
- Hoeveel ontwerp moet in jouw context aan code voorafgaan, en hoe leg je de beslissingen vast?
- Welke delen van je systeem zouden baat hebben bij een meer functionele of data-georiënteerde stijl?
- Hoe voorkom je dat ontwerpprincipes verharden tot dogma dat pragmatische uitzonderingen weerstaat?

## Belangrijkste inzichten

- Koppeling en samenhang zijn de eigenschappen die ertoe doen. De afkortingen zijn middelen tot die doelen.
- Elk principe heeft een faalwijze. Weet wanneer elk je misleidt.
- Geef de voorkeur aan wat duplicatie boven een voortijdige of verkeerde abstractie.
- Gebruik DDD en afgebakende contexten om complexe domeinen af te stemmen op teameigenaarschap.
- Kies paradigma's naar geschiktheid. Grote systemen zijn pragmatisch gemengd.
- Ontwerp voor de wijzigingen die je daadwerkelijk nodig zult hebben en vermijd zowel te weinig als te veel ontwerp.

## Referenties en verder lezen

- Robert C. Martin, *Clean Architecture* and *Agile Software Development, Principles, Patterns, and Practices*
- Eric Evans, *Domain-Driven Design: Tackling Complexity in the Heart of Software*
- Vaughn Vernon, *Implementing Domain-Driven Design*
- Erich Gamma, Richard Helm, Ralph Johnson, John Vlissides, *Design Patterns: Elements of Reusable Object-Oriented Software*
- Martin Fowler, *Refactoring: Improving the Design of Existing Code* and *Patterns of Enterprise Application Architecture*
- David L. Parnas, *On the Criteria to Be Used in Decomposing Systems into Modules*
- Sandi Metz, *Practical Object-Oriented Design*
