# 5.5 Internationalisering en lokalisering

## Overzicht en motivatie

[Internationalisering](https://en.wikipedia.org/wiki/Internationalization_and_localization) (i18n) is het engineeringwerk om software zo te bouwen dat ze aan elke taal, regio en cultuur kan worden aangepast zonder de code te wijzigen. Lokalisering (l10n) is het werk dat volgt: een product werkelijk aanpassen voor een specifieke locale door tekst te vertalen, datums en getallen op te maken, de layout aan te passen en rekening te houden met culturele verwachtingen. De twee zijn verschillend. Internationalisering wordt eenmaal gedaan, in de architectuur. Lokalisering wordt vele malen gedaan, in de content. Krijg je de architectuur vooraf goed, dan is elke lokalisering goedkoop. Krijg je haar fout, dan wordt elke lokalisering een pijnlijke, foutgevoelige aanpassing achteraf.

Voor grote teams is i18n een fundamentele architectuurbeslissing. Ze raakt elke laag: dataopslag, stringverwerking, layout en contentpijplijnen. Als je haar niet vroeg vaststelt en afdwingt met gedeelde bibliotheken en lintregels, coderen teams Engelse teksten hard, plakken ze vertaalde fragmenten aan elkaar en nemen ze Latijnse schriften aan. Die schuld moet worden afgelost voordat het product een nieuwe markt kan betreden. Een gedeeld i18n-raamwerk en lokaliseringsworkflow laten tientallen teams een product in veel talen opleveren zonder dat elk de leidingen opnieuw uitvindt.

De relevantie voor onderneming en overheid is direct. Multinationale ondernemingen moeten klanten en medewerkers bedienen over landen, talen en regelgevingsregimes. Overheden moeten taalkundig diverse bevolkingen bedienen. Veel landen zijn officieel meertalig, en veel zijn wettelijk verplicht diensten in meerdere talen te leveren, inclusief [rechts-naar-links](https://en.wikipedia.org/wiki/Bidirectional_text)schriften en inheemse of minderheidstalen. Voor publieke diensten is taaltoegang een kwestie van gelijkheid en recht: een burger die de enige beschikbare taal niet kan lezen wordt in feite de dienst ontzegd.

## Kernprincipes

- Internationaliseer de architectuur eenmaal. Lokaliseer de content vele malen.
- Codeer gebruikersgerichte tekst nooit hard. Externaliseer alle strings in beheerde resources.
- Gebruik overal [Unicode](https://en.wikipedia.org/wiki/Unicode) (UTF-8). Neem aan dat tekst in elk schrift kan zijn.
- Plak vertaalde fragmenten nooit aan elkaar. Grammatica en woordvolgorde verschillen per taal.
- Plan voor tekstuitbreiding, rechts-naar-linksschriften en complexe meervouds- en geslachtsregels.
- Maak datums, getallen, valuta en namen op naar locale, niet naar code.
- Scheid vertaalbare content van code zodat vertalers nooit aan de bron komen.
- Lokalisering is cultureel, niet alleen taalkundig: kleuren, beeld en voorbeelden doen ertoe.

## Aanbevelingen

### Bouw een degelijke internationaliseringsarchitectuur

Sla alle tekst van begin tot eind op en verwerk haar als Unicode (UTF-8) (database, API's en UI) zodat elk schrift kan worden weergegeven. Externaliseer elke gebruikersgerichte string in resourcebestanden of een berichtencatalogus met een identifier als sleutel, nooit ingebed in code of opmaak. Stel een locale voor als taal plus regio (en schrift waar nodig) zodat je bijvoorbeeld de varianten van één taal over landen kunt onderscheiden. Houd opmaaklogica in een goed geteste internationaliseringsbibliotheek in plaats van datum-, getal- en valutaopmaak met de hand te rollen. Sla data op in neutrale, ondubbelzinnige vormen (UTC-tijdstempels, ISO-land- en valutacodes, basiseenheden) en maak ze alleen op in de presentatielaag.

### Handel taalcomplexiteit correct af

Neem geen tekstlengte aan. Laat ruim de ruimte, omdat vertalingen vaak veel langer uitvallen dan Engels, en ontwerp layouts die herstromen in plaats van afkappen of overlappen. Ondersteun bidirectionele (rechts-naar-links)schriften door logische in plaats van fysieke layouteigenschappen te gebruiken en de interface waar gepast te spiegelen. Gebruik de meervoudsregels van de locale via je i18n-bibliotheek (talen hebben van één tot zes meervoudsvormen) in plaats van naïeve enkelvoud/meervoud-logica. Handel geslacht en grammaticale overeenkomst af waar de taal dat vereist. Bouw zinnen nooit door fragmenten aan elkaar te plakken. Gebruik volledige, geparametriseerde berichtsjablonen zodat vertalers de woordvolgorde bepalen.

### Stel een lokaliseringsworkflow en vertaalbeheer vast

Behandel lokalisering als continue pijplijn, niet als batch voor lancering. Extraheer strings automatisch, duw ze naar een [vertaalbeheersysteem](https://en.wikipedia.org/wiki/Translation_management_system) en haal voltooide vertalingen terug, bij voorkeur geïntegreerd met CI zodat nieuwe strings worden gemarkeerd en gelokaliseerde versies synchroon blijven. Geef vertalers context: screenshots, beschrijvingen, tekenlimieten en per taal een woordenlijst en stijlgids om terminologie en toon consistent te houden. Gebruik [vertaalgeheugen](https://en.wikipedia.org/wiki/Translation_memory) om eerder werk te hergebruiken en kosten te besparen. Besluit bewust waar [machinevertaling](https://en.wikipedia.org/wiki/Machine_translation) acceptabel is (content met laag risico en hoog volume) en waar menselijke vertaling en review vereist zijn (juridisch, medisch, veiligheid, merkkritisch). [Pseudo-lokaliseer](https://en.wikipedia.org/wiki/Pseudolocalization) vroeg, door strings te vervangen door verlengde, geaccentueerde plaatshouders, om hard gecodeerde strings, afkapping en encodingbugs te vangen voordat de echte vertaling begint.

### Lokaliseer formaten, cultuur en content, niet alleen woorden

Maak datums, tijden, getallen, valuta, adressen, telefoonnummers en namen per locale op, met respect voor lokale conventies (datumvolgorde, decimale en groeperingsscheidingstekens, plaatsing van valuta, naamvolgorde). Pas beeld, pictogrammen, kleuren, voorbeelden en metaforen aan op lokale culturele betekenis, aangezien symbolen en kleuren per cultuur verschillende connotaties dragen. Houd rekening met lokale juridische en regelgevende contentverschillen. Onderscheid wereldwijde consistentie (merk, kernfunctionaliteit) van regionale aanpassing (content, voorbeelden, compliance) en besluit expliciet welke elementen vast zijn en welke meebuigen.

### Bestuur i18n als gedeelde infrastructuur

Lever een gedeelde i18n-bibliotheek, lintregels voor stringexternalisatie en een standaard mechanisme voor locale-bepaling zodat teams niet per ongeluk tekst hard kunnen coderen. Stel eigenaarschap van de lokaliseringspijplijn en woordenlijsten vast. Test in CI in meerdere locales, inclusief een rechts-naar-linkslocale en een pseudo-locale met lange tekst, zodat regressies automatisch worden gevangen.

## Afwegingen: voor- en nadelen

| Beslissing | Voordelen | Nadelen |
|---|---|---|
| Vanaf dag één internationaliseren | Goedkope latere markttoegang, geen aanpassing achteraf | Kosten vooraf, ook voordat een tweede locale nodig is |
| i18n later achteraf aanpassen | Stelt kosten uit als de wereldwijde behoefte onzeker is | Zeer duur en riskant om hard gecodeerde aannames terug te draaien |
| Menselijke vertaling | Hoge kwaliteit, cultureel nauwkeurig | Langzamer en duurder |
| Machinevertaling | Snel, goedkoop, schaalt naar enorm volume | Kwaliteits- en nauwkeurigheidsrisico. Ongeschikt voor content met hoge inzet |
| Continue lokaliseringspijplijn | Locales blijven synchroon, geen lanceringsdruk | Investering in tooling en proces |
| Diepe culturele aanpassing per regio | Betere lokale pasvorm en vertrouwen | Meer contentvarianten om te bouwen en te onderhouden |

De cruciale afweging is wanneer je in internationalisering investeert. i18n achteraf aanbrengen in een product vol hard gecodeerde, aaneengeplakte, Latijn-aannemende code is een van de duurdere vormen van technische schuld om af te lossen. Voor elke organisatie met aannemelijke internationale of meertalige ambities, wat in wezen alle grote ondernemingen en meertalige overheden omvat, is de architectuur vroeg internationaliseren veel goedkoper dan achteraf aanpassen, ook al wordt de opbrengst uitgesteld.

## Vragen om met je team te bespreken

1. **Dwingen we stringexternalisatie af met lintregels, en draait pseudo-lokalisering in CI vóór enige echte vertaling?** De schuld die internationalisering duur maakt (hard gecodeerde Engelse strings, aaneengeplakte zinsfragmenten, aannames over Latijnse schriften) hoopt zich stilletjes op tenzij tooling haar bij commit stopt. Lintregels die hard gecodeerde gebruikerstekst markeren, plus een geaccentueerde pseudo-locale met lange tekst in CI, vangen afkapping, overlap en encodingbugs terwijl ze goedkoop te repareren zijn. Dit laat tientallen teams één product in veel talen opleveren zonder dat elk de leidingen opnieuw uitvindt of onder deadline aannames terugdraait. Neem een zoekopdracht naar hard gecodeerde strings mee en vraag of enig team er vandaag per ongeluk een zou kunnen opleveren. Als niets in de pijplijn het zou vangen, is dat het eerste gat om te dichten.

2. **Waar slaan we canonieke data op, en is opmaak beperkt tot de presentatielaag?** Tijdstempels als UTC opslaan, landen en valuta als ISO-codes en bedragen in basiseenheden betekent dat elke locale ze aan de rand correct kan opmaken, terwijl opmaaklogica gebakken in de datalaag bugs produceert die pijnlijk zijn terug te draaien. Spreek af dat datums, getallen, valuta, adressen en namen alleen bij presentatie worden opgemaakt, via een goed geteste bibliotheek in plaats van met de hand gerolde code. Dit telt voor multinationale ondernemingen en meertalige overheden waar een burger de juiste datumvolgorde, decimale scheidingstekens en naamvolgorde in zijn eigen conventie moet zien. Neem een voorbeeld mee van een waarde die je systeem al opgemaakt opslaat en traceer wat breekt wanneer een nieuwe locale haar anders nodig heeft. Als data en presentatie verward zijn, besluit dan hoe je ze ontwart voordat je locales toevoegt.

3. **Waar precies is machinevertaling acceptabel, en hoe houden we onze lokaliseringspijplijn continu in plaats van batch?** Machinevertaling is snel en goedkoop voor content met laag risico en hoog volume maar ongeschikt voor juridische, medische, veiligheids- of merkkritische tekst waar een vertaalfout echte schade veroorzaakt, dus de grens moet een expliciet beleid zijn, geen gok per team. Evenzo garandeert lokalisering als batch voor lancering een vertaalcrunch, terwijl strings automatisch extraheren en synchroniseren via een vertaalbeheersysteem elke locale actueel houdt. Besluit wie de pijplijn bezit, de woordenlijsten en de menselijke reviewpoort voor strings met hoge inzet. Neem een recente release mee en vraag hoe lang haar nieuwe strings erover deden om in elke taal te verschijnen. Als locales tussen releases uit de pas lopen, is je pijplijn een verkapte batch.

4. **Testen we een rechts-naar-linkslocale en een pseudo-locale met lange tekst automatisch, of nemen we stilletjes Latijnse schriften en layouts met Engelse lengte aan?** Bidirectionele (rechts-naar-links) ondersteuning en tekstuitbreiding zijn de aannames die het zichtbaarst breken in een nieuwe markt: gespiegelde interfaces die nooit zijn gespiegeld, en knoppen die afkappen zodra Duits of Fins veertig procent langer uitvalt dan Engels. De concurrerende trek is snelheid, aangezien bouwen op logische in plaats van fysieke layouteigenschappen en een geaccentueerde pseudo-locale in continuous integration (CI) bedraden moeite kost voordat een echte klant het nodig heeft. Neem een screenshot mee van je drukste schermen gerenderd in een rechts-naar-linkslocale en in een verlengde pseudo-locale, en tel de overlappen, afgekapte labels en vastzittende pijlen. Voor een multinationale onderneming of een overheid die wettelijk een rechts-naar-links- of minderheidstaal moet bedienen is een layout die niet kan spiegelen geen cosmetisch defect, maar een markt of wettelijke verplichting die je zonder herbouw niet kunt nakomen.

5. **Welke delen van het product zijn wereldwijd vast en welke buigen mee per regio, en wie heeft de bevoegdheid dat te beslissen?** Lokalisering is cultureel, niet alleen taalkundig, dus kleuren, beeld, voorbeelden, aanspreekvormen en zelfs welke functies worden aangeboden kunnen per markt verschillen, maar elke regionale variant die je toestaat is nog een artefact om voor altijd te bouwen, te vertalen, te beoordelen en te onderhouden. De spanning is tussen lokale pasvorm, die vertrouwen en conversie bouwt, en consistentie, die het merk samenhangend en de onderhoudslast begrensd houdt. Neem een concrete lijst mee van wat een voorgestelde nieuwe locale zou wijzigen naast vertaalde strings, en prijs het doorlopende onderhoud van elke variant, niet alleen de eerste bouw. In een grote onderneming heeft deze beslissing een benoemde eigenaar nodig zodat regionale teams het product niet ad hoc kunnen forken, en bij de overheid moet ze juridische en toegankelijkheidscontentregels respecteren die per jurisdictie verschillen en niet optioneel zijn.

6. **Aan welke locales verbinden we ons werkelijk, hoe houden we terminologie over ze consistent en welk bewijs drijft die lijst?** Een taal toevoegen is makkelijk te beloven en duur vol te houden, omdat elke taal een woordenlijst nodig heeft, een stijlgids, menselijke review voor strings met hoge inzet en correcte afhandeling van meervoud en geslacht die naïeve enkelvoud-of-meervoudlogica in de meeste talen fout doet. De concurrerende overwegingen zijn bereik tegenover kosten: een markt of populatie slecht bedienen kan erger zijn dan haar helemaal niet bedienen. Neem de populatie of omzet achter elke kandidaatlocale mee, de dekking van meervoudsregels en opmaak die je bibliotheek ervoor biedt en wie haar woordenlijst bezit. Voor een multinationale onderneming is de drijfveer adresseerbare markt en supportkosten per taal, terwijl het voor de overheid de wettelijke verplichting tot taaltoegang en gelijkheid is, gekwantificeerd door het aantal inwoners dat alleen in die taal kan handelen.

## Sectorperspectief

**Startup.** Maak de goedkope architectuurkeuzes op dag één en stop daar: UTF-8 van begin tot eind, elke gebruikersgerichte string in een berichtencatalogus en datums, getallen en valuta opgemaakt via een locale-bewuste bibliotheek. Dit kost bijna niets terwijl je in één taal oplevert en bespaart een herschrijving wanneer je eerste grote klant een tweede wil. Zet geen vertaalpijplijn op en ondersteun geen locales waar nog niemand voor betaalt. Houd de deur open, niet het hele huis gemeubileerd.

**Kleinbedrijf.** Zonder internationaliseringsspecialist en met een krap budget leun je op de i18n-functies die al in je framework zitten en een gehoste vertaalbeheerdienst in plaats van zelf pijplijnen te bouwen. Gebruik machinevertaling voor content met laag risico en hoog volume en betaal alleen voor menselijke vertaling waar een fout je een klant zou kosten of een regel zou schenden, zoals juridische, veiligheids- of factuurtekst. Verbind je alleen aan een locale wanneer een specifieke markt de doorlopende vertaal- en reviewkosten duidelijk rechtvaardigt.

**Grote onderneming.** Het probleem is governance over veel teams: een gedeelde i18n-bibliotheek, lintregels die hard gecodeerde strings afwijzen, een continue lokaliseringspijplijn met vertaalgeheugen en woordenlijsten per taal en multilocale CI met een rechts-naar-links- en een lange-tekst-pseudo-locale. Draai lokalisering als gedeelde infrastructuur met een duidelijke eigenaar zodat groepen ophouden de leidingen opnieuw uit te vinden of uit de pas te lopen. Meet taaldekking, lokaliseringskwaliteit en tijd om een nieuwe locale te lanceren, en beheer het localeportfolio aan de hand van die getallen in plaats van markten ad hoc te lanceren.

**Overheid.** Taaltoegang is vaak een wettelijke verplichting, die officiële talen, rechts-naar-linksschriften en inheemse of minderheidstalen omvat, dus transparantie en gelijkheid geven elke keuze vorm. Bouw een gedeeld i18n-raamwerk en vertaalworkflow over instanties, eis menselijke review voor juridische en veiligheidsterminologie en publiceer woordenlijsten zodat termen consistent blijven tussen diensten. Aanbesteding moet ondersteuning voor locale, rechts-naar-links en toegankelijkheid in contracten eisen, en de populatie die in elke taal wordt bediend is de statistiek die de uitgaven tegenover het publiek rechtvaardigt.

## Voorbeelden

**Startup.** Een kleine startup die alleen in het Engels uitlevert maakte op dag één toch een paar goedkope architectuurkeuzes: overal UTF-8, elke gebruikersgerichte string in een berichtencatalogus getrokken in plaats van hard gecodeerd en datums en valuta opgemaakt via een locale-bewuste bibliotheek. Het kostte hen bijna niets terwijl ze één taal hadden. Een jaar later, toen hun grootste prospect om een Franse en Duitse versie vroeg, was die locales toevoegen vooral een vertaaloefening overgedragen aan een freelancer, geen herschrijving, en sloten ze de deal in weken in plaats van haar een kwartaal engineeringwerk uit te stellen.

**Grote onderneming.** Een wereldwijd e-commercebedrijf internationaliseerde zijn platform vroeg: UTF-8 overal, geëxternaliseerde strings, een locale-bewuste opmaakbibliotheek en een continue lokaliseringspijplijn met vertaalgeheugen en woordenlijsten per taal. Een nieuwe markt betreden werd grotendeels een contentoefening (vertalen, beoordelen, beeld aanpassen) in plaats van een engineeringproject, waardoor het bedrijf in weken in nieuwe locales kon lanceren. Rechts-naar-linksondersteuning gebouwd op logische layouteigenschappen betekende dat Arabische en Hebreeuwse markten weinig nieuw UI-werk vroegen.

**Overheid.** Een nationale overheid, wettelijk verplicht diensten in verschillende officiële talen te leveren, inclusief een rechts-naar-linksschrift en minderheidstalen, bouwde een gedeeld i18n-raamwerk en vertaalworkflow gebruikt over instanties. Pseudo-lokalisering in CI ving hard gecodeerde strings en afkapping vóór lancering. Een gedeelde woordenlijst hield juridische terminologie consistent over diensten en talen. Burgers kunnen belasting-, gezondheids- en uitkeringstransacties in hun eigen taal afronden met correcte datum-, getal- en naamopmaak, wat voldoet aan de wetgeving voor taaltoegang en de gelijkheid voor sprekers van niet-meerderheidstalen verbetert.

## Zakelijke onderbouwing: motivatie, ROI en TCO

Het ROI van internationalisering is markttoegang en snelheid. Een goed geïnternationaliseerd product kan snel en goedkoop nieuwe landen en taalmarkten betreden, waardoor elke nieuwe locale incrementele omzet of burgerbereik wordt in plaats van een groot project. Lokaliseringskwaliteit drijft conversie, vertrouwen en supportkosten in elke markt: gebruikers handelen meer en nemen minder contact op met support wanneer het product hun taal correct spreekt en hun conventies respecteert.

Qua TCO zijn de adoptiekosten de engineering vooraf om te internationaliseren, plus doorlopende vertaal- en pijplijnkosten. De kosten van niet adopteren zijn de dure aanpassing achteraf: hard gecodeerde strings, aaneenplakken, encodingbugs en layoutaannames ontrafelen over een hele codebasis, vaak onder een deadline gedreven door een markt of wettelijke eis. Slechte lokalisering draagt ook verborgen kosten: gemiste verkopen in slecht bediende markten, supportlast door verwarrende formaten en juridische of reputatieschade door verkeerd vertaalde content met hoge inzet. Continue lokalisering voorkomt dure vertaalcrunches voor lancering.

Formuleer internationalisering voor het bestuur als optie op toekomstige markten. Het is een bescheiden investering vooraf die de kosten en tijd van elke toekomstige markttoetreding dramatisch verlaagt. Voor de overheid is de drijfveer de wettelijke verplichting tot taaltoegang en gelijkheid, gekwantificeerd door de in elke taal bediende populatie.

## Antipatronen en valkuilen

- **Hard gecodeerde strings**: gebruikerstekst gebakken in code, wat codewijzigingen per locale afdwingt.
- **Stringconcatenatie**: zinnen bouwen uit fragmenten, wat grammatica en woordvolgorde breekt.
- **Niet-Unicode-aannames**: encodingbugs, [mojibake](https://en.wikipedia.org/wiki/Mojibake) (onleesbare tekst door niet-passende tekencoderingen) en onvermogen schriften weer te geven.
- **Engelse tekstlengte aannemen**: layouts die afkappen of overlappen bij vertaling.
- **Rechts-naar-links negeren**: fysieke links/rechts-layout gebruiken die niet kan spiegelen.
- **Naïeve meervoudsvorming**: enkelvoud/meervoud-logica die in de meeste talen fout is.
- **Locale-blinde opmaak**: hard gecodeerde datum-, getal- en valutaformaten.
- **Vertalen zonder context**: vertalers die de betekenis raden en fouten produceren.
- **Batch, last-minute lokalisering**: een crunch voor lancering in plaats van een continue pijplijn.
- **Culturele doofheid**: beeld, kleuren of voorbeelden die lokaal beledigen of verwarren.

## Volwassenheidsmodel

**Niveau 1: Initiëren.** Eén taal, hard gecodeerde strings, niet-Unicode-aannames en tekst gebouwd door aaneenplakken. Internationalisering is reactief: elke nieuwe locale betekent code wijzigen, en encoding- en layoutbugs worden bij toeval in productie gevonden.

**Niveau 2: Ontwikkelen.** Sommige strings zijn geëxternaliseerd en Unicode wordt op plekken gebruikt, maar de praktijk is inconsistent over teams. Lokalisering is een handmatige batchinspanning voor lancering, en opmaak, meervoudsafhandeling en rechts-naar-linksondersteuning worden van team tot team anders (of helemaal niet) aangepakt.

**Niveau 3: Standaardiseren.** Een gedeelde i18n-architectuur en locale-bewuste opmaakbibliotheek zijn de gedocumenteerde, organisatiebreed afgedwongen standaard. Stringexternalisatie wordt gecontroleerd met lintregels, een vertaalbeheersysteem en continue pijplijn zijn aanwezig met woordenlijsten en vertaalgeheugen, en pseudo-lokalisering plus multilocale tests (inclusief een rechts-naar-links- en een lange-tekstlocale) draaien in CI.

**Niveau 4: Beheersen.** Het lokaliseringsprogramma wordt gemeten en beheerst aan de hand van uitgangswaarden. Teams volgen taaldekking, lokaliseringskwaliteit en defectpercentages, synchronisatielatentie van strings van commit tot vertaalde release, afkappings- en rechts-naar-linksrenderdefecten gevangen per release, vertaalkosten per locale en tijd om een nieuwe locale te lanceren, en deze statistieken poorten releases en sturen waar je in menselijke review tegenover machinevertaling investeert.

**Niveau 5: Orkestreren.** Internationalisering en lokalisering worden continu verbeterd en over de organisatie geïntegreerd. Lokalisering is continu, machine- en menselijke vertaling worden bewust per contentklasse gekozen en culturele aanpassing is systematisch. De organisatie voegt locales toe, schaft ze af en bakent ze opnieuw af in reactie op markt- en gelijkheidsbewijs, en nieuwe locales lanceren snel op hoge kwaliteit zonder aanpassing achteraf.

## Ideeën voor discussie

- Hoe vroeg moet een product internationaliseren als de internationale vraag onzeker is?
- Waar is machinevertaling acceptabel, en waar moeten mensen beoordelen?
- Hoe houd je terminologie consistent over veel talen en teams?
- Hoeveel regionale culturele aanpassing is de extra onderhoudslast van varianten waard?
- Hoe moeten ondersteuning en testen van rechts-naar-links en minderheidstalen worden geprioriteerd?
- Hoe geef je vertalers genoeg context zonder de pijplijn te vertragen?

## Belangrijkste inzichten

- Internationaliseer de architectuur eenmaal. Lokaliseer content vele malen.
- Gebruik overal Unicode, externaliseer alle strings en plak vertalingen nooit aan elkaar.
- Plan voor tekstuitbreiding, rechts-naar-linksschriften en locale-specifieke meervouds- en opmaakregels.
- Draai een continue lokaliseringspijplijn met vertaalgeheugen, woordenlijsten en context.
- Pseudo-lokaliseer vroeg in CI om i18n-bugs te vangen vóór echte vertaling.
- Lokalisering is cultureel, niet alleen taalkundig.
- Vroeg internationaliseren is veel goedkoper dan achteraf aanpassen. Voor de overheid is het een wettelijke gelijkheidseis.

## Referenties en verder lezen

- The Unicode Consortium, *The Unicode Standard* and Common Locale Data Repository (CLDR)
- W3C Internationalisation (i18n) Activity, techniques and best practices
- Richard Ishida, W3C internationalisation articles and tutorials
- Bert Esselink, *A Practical Guide to Localisation*
- John Yunker, *Beyond Borders: Web Globalisation Strategies*
- Unicode Technical Standard #35 (locale data markup) and ICU library documentation
- IETF BCP 47 language tags
- Government multilingual service and language-access guidance
- Nielsen Norman Group and W3C articles on RTL, text expansion, and localisation UX
