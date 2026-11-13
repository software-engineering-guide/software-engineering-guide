# 1.6 Besluitenlogboeken

## Overzicht en motivatie

Een **besluitenlogboek** (decision record) is een document dat een belangrijke beslissing vastlegt samen met haar context en gevolgen. De bekendste vorm is het **[architecture decision record](https://en.wikipedia.org/wiki/Architectural_decision) (ADR)**, een korte notitie, bij voorkeur onveranderlijk, die één architectonisch belangrijke keuze vastlegt, waarom ze werd gemaakt en wat eruit volgt. De volledige verzameling records van een project is haar **decision log (ADL)**, en de discipline om ze bij te houden maakt deel uit van **architecture knowledge management (AKM)**. Dit hoofdstuk bouwt voort op de besluitvormings- en governancepraktijken van hoofdstuk 1.5 en richt zich op hoe je besluitenlogboeken op schaal schrijft, opslaat en volhoudt.

De motivatie is eenvoudig en pijnlijk op de harde manier te leren. Bij elk langlevend systeem is de duurste vraag "waarom is dit in vredesnaam zo gebouwd?", maanden of jaren later gesteld door mensen die er niet bij waren. Code laat zien *wat* het systeem doet. Tests laten zien dat het *werkt*. Maar geen van beide legt vast *waarom* je dit pad koos boven de alternatieven die je overwoog en verwierp. Zonder besluitenlogboeken verdampt die redenering met personeelswisselingen. Teams bepleiten beslechte kwesties opnieuw, draaien goede beslissingen om om slechte redenen terug of houden slechte beslissingen uit angst in stand. Een besluitenlogboek is een goedkope brief aan de toekomst die de redenering bewaart.

Voor grote teams is dit evenzeer een coördinatiemiddel als een geheugensteun. Ondernemingen draaien tientallen teams die overlappende keuzes maken. Een gedeeld besluitenlogboek verandert de zwaarbevochten redenering van één team in een herbruikbaar bezit en voorkomt uiteenlopende, onverenigbare beslissingen. In overheids- en gereguleerde omgevingen zijn besluitenlogboeken bijna verplicht. Auditors, toezichthouders en opvolgende leveranciers hebben allemaal een traceerbare motivering nodig die architectonisch belangrijke eisen verbindt met de keuzes die ertegen zijn gemaakt. Een goed bijgehouden besluitenlogboek is vaak het verschil tussen een systeem dat je kunt borgen en auditen en een systeem dat je niet kunt borgen.

## Kernprincipes

- **Leg het *waarom* vast, niet alleen het *wat*.** Context en verworpen alternatieven zijn het punt.
- **Eén beslissing per record.** Houd elk record specifiek en op zichzelf staand.
- **Klein en licht wint van uitputtend en ongebruikt.** Een record van één pagina dat bestaat, wint van een rapport dat nooit wordt geschreven.
- **Zet overal een tijdstempel op.** Kosten, beperkingen en leveranciers veranderen. Dateer elke bewering.
- **Geef pragmatisch de voorkeur aan een levend logboek.** Onveranderlijkheid is het ideaal. In de praktijk wijzig je met gedateerde notities.
- **Woorden boven afkortingen.** "Beslissingen" nodigt tot meer bijdragen uit dan "ADR's".
- **Maak beslissingen vindbaar en, waar mogelijk, toetsbaar.** Toon het juiste record op het juiste moment. Borg het met fitness functions.

## Aanbevelingen

### Leg de essentiële structuur vast

Een goed besluitenlogboek heeft een paar essentiële onderdelen. Pas een bekend sjabloon aan in plaats van er een te verzinnen:

- **Titel:** een korte gebiedende zin in de tegenwoordige tijd ("Gebruik [PostgreSQL](https://en.wikipedia.org/wiki/PostgreSQL) voor het grootboek").
- **Status:** voorgesteld, geaccepteerd, vervangen, afgeschaft.
- **Context:** de situatie, krachten, bedrijfsprioriteiten en beperkingen die deze beslissing noodzakelijk maken. Neem de architectonisch belangrijke eis op die ze adresseert.
- **Beslissing:** de gemaakte keuze, helder verwoord.
- **Gevolgen:** wat makkelijker wordt en wat moeilijker, vervolgbeslissingen die worden getriggerd en aanvaarde risico's.

Populaire sjablonen zijn die van Michael Nygard (eenvoudig en breed toegepast), van Tyree en Akerman (uitgebreider, met gewogen alternatieven), MADR (Markdown Any Decision Records, sterk in opties en hun voor- en nadelen) en Y-statements (een gestructureerde vorm van één zin). Standaardiseer op één per organisatie, zodat records vergelijkbaar zijn. Zie hoofdstuk 12.3 voor een kopieer-en-plak-sjabloon.

### Schrijf records die specifiek, gedateerd en vrijwel onveranderlijk zijn

Houd elk record over precies één beslissing. Zet een tijdstempel op afzonderlijke beweringen, vooral op alles wat afdrijft: prijzen, schaalcijfers, mogelijkheden van leveranciers, licentievoorwaarden. In theorie zou een record onveranderlijk moeten zijn. Als een beslissing verandert, schrijf je een *nieuw* record dat het oude vervangt en de geschiedenis behoudt. In de praktijk vinden veel teams een **levend-document**-aanpak beter werken: voeg nieuwe informatie in het bestaande record in met een datumstempel en een notitie dat die na de beslissing kwam. Beide zijn legitiem. De onveranderlijke stijl is sterker voor auditsporen. De levende stijl is beter voor dagelijkse teamkennis. Kies bewust en wees consistent.

### Bewaar records waar het werk is

Zet besluitenlogboeken in [versiebeheer](https://en.wikipedia.org/wiki/Version_control) naast de code: een map `decisions/` (of `adr/`) met [Markdown](https://en.wikipedia.org/wiki/Markdown)-bestanden, één per beslissing, genoemd met een kleine-letter, met streepjes gescheiden gebiedende werkwoordsgroep (`choose-database.md`, `format-timestamps.md`). Zo krijg je geschiedenis, review en diffs gratis, en blijft de motivering naast wat ze toelicht. Heeft je team een voorkeur voor [wiki's](https://en.wikipedia.org/wiki/Wiki), Google Docs of een tracker in Jira-stijl, gebruik die dan. De tool doet er veel minder toe dan de gewoonte. Een lichte opdrachtregeltool (zoals `adr-tools`) kan records opzetten en indexeren.

### Noem ze "beslissingen" en breid uit voorbij architectuur

Een praktisch inzicht van veel teams: het label doet ertoe. Sommige ontwikkelaars en managers krijgen de kriebels van het woord "architectuur", en "record" kan aanvoelen als papierwerk achteraf. De map eenvoudig "decisions" noemen zet vaak een knop om. Teams gaan leverancierskeuzes, planningsbeslissingen, roosterbeslissingen en data- en compliancebeslissingen vastleggen, allemaal met hetzelfde sjabloon. Mensen leren sneller van woorden dan van afkortingen, en ze dragen meer bij wanneer de framing is "help je toekomstige teamgenoten denken" in plaats van "vul het verplichte formulier in".

### Definieer de levenscyclus en governance

Om besluitenlogboeken te laten schalen spreek je het omringende proces af (hier ontmoet de governance van hoofdstuk 1.5 de praktijk):

- **Wie er een kan opstellen en wat het rechtvaardigt:** doorgaans elke geïnformeerde bijdrager. Stel een record op wanneer toekomstige ontwikkelaars het *waarom* nodig zullen hebben, en sla het over voor keuzes met laag risico, die op zichzelf staan of al gedocumenteerd zijn.
- **Levenscyclus:** een eenvoudige stroom zoals *Initiëren → Onderzoeken → Evalueren → Implementeren → Onderhouden → Afbouwen*, met acceptatiecriteria om tussen fasen te bewegen (probleem verwoord, alternatieven overwogen, afwegingen gedocumenteerd, stakeholders geraadpleegd).
- **Rollen:** voorsteller, onderzoeker, beoordelaar, goedkeurder en een verantwoordelijke beheerder die het record periodiek (minstens jaarlijks) beoordeelt en de uiteindelijke afbouw aanstuurt.
- **Governance:** hoe consensus, conflict, escalatie en veto werken, en eventuele compliancebeperkingen. Leun op principes als *bias for action* en *[disagree-and-commit](https://en.wikipedia.org/wiki/Disagree_and_commit)*, en bewaar zwaarder proces voor onomkeerbare "eenwegdeur"-beslissingen met een groot schadebereik.

### Maak beslissingen toetsbaar en vindbaar

Een besluitenlogboek *documenteert* een beslissing. Een **fitness function** *borgt* haar: een geautomatiseerde controle, uitgevoerd in [continuous integration](https://en.wikipedia.org/wiki/Continuous_integration) (CI), die verifieert dat de beslissing nog geldt ("alle toestandswijzigingen moeten gebeurtenissen uitzenden", "geen module mag over deze grenzen heen importeren", met tools als ArchUnit). Dit verandert governance van periodieke handmatige review in continue, schaalbare handhaving, wat vooral waardevol is voor regelgevings- en auditdoelen (hoofdstuk 3.1, 4.6, 8.5). Toon dan het *juiste* record op het *juiste* moment. Tooling die relevante beslissingen aan een pull request koppelt wanneer een ontwikkelaar de code raakt die ze besturen, wint van hopen dat mensen een documentatiemap lezen.

## Afwegingen: voor- en nadelen

| Keuze | Voordelen | Nadelen |
|---|---|---|
| **Lichte ADR's (Nygard/MADR)** | Snel te schrijven, worden echt geschreven. Weinig ceremonie | Minder stringentie voor beslissingen met hoge inzet en betwiste beslissingen |
| **Zware sjablonen (Tyree-Akerman)** | Gewogen alternatieven. Sterk voor grote, kostbare keuzes | Trager. Kan routinematig vastleggen afschrikken |
| **Onveranderlijk + vervangen** | Schoon auditspoor. Geschiedenis bewaard | Meer records. Lezers moeten ketens volgen |
| **Levend document (gedateerde wijzigingen)** | Eén actuele bron van waarheid. Makkelijk te onderhouden | Zwakker auditverhaal. Risico op stille bewerkingen |
| **Markdown in de repo** | Versiebeheerd, beoordeelbaar, naast de code | Minder vriendelijk voor niet-ontwikkelaars |
| **Wiki / documentatietool** | Toegankelijk voor alle rollen | Geschiedenis en review zwakker. Drijft weg van de code |

De kernspanning is **stringentie tegenover adoptie**. Het meest stringente systeem dat niemand gebruikt, legt niets vast. Het lichtste systeem dat iedereen gebruikt, groeit in waarde. Kies standaard voor licht en bewaar zwaarder proces voor de paar beslissingen die duur en moeilijk om te keren zijn.

## Vragen om met je team te bespreken

1. **Hoe bereikt het juiste besluitenlogboek een ontwikkelaar op het moment dat die de code raakt die ze bestuurt, in plaats van in een map te staan die niemand opent?** Een write-only logboek legt redenering vast die nooit gedrag verandert, wat de meest voorkomende manier is waarop besluitenlogboeken falen: ze bestaan, en niemand leest ze wanneer het ertoe doet. De tegenwicht-overweging is inspanning, omdat records automatisch tonen (ze aan een pull request koppelen wanneer iemand de bestuurde code bewerkt) investering in tooling vraagt die een wiki of documentatiemap niet vraagt. Neem bewijs mee naar de discussie: toen iemand onlangs een beslechte kwestie omdraaide of opnieuw bepleitte, was het relevante record toen vindbaar, of begraven? Voor een grote organisatie met tientallen teams is vindbaarheid wat de zwaarbevochten redenering van één team verandert in een herbruikbaar bezit in plaats van een privéarchief. Bepaal of je records in versiebeheer naast de code opslaat en ze in de pull-requeststroom inpast, zodat het record verschijnt waar het werk gebeurt.

2. **Wie is de verantwoordelijke beheerder van elk record, en wat voorkomt dat je logboek verwordt tot zelfverzekerde desinformatie?** De gevaarlijke faalwijze van een besluitenlogboek is geen lege map, maar een map vol records waarvan de kosten, leveranciersmogelijkheden en beperkingen jaren geleden stilletjes verouderd zijn. Elk record heeft een verantwoordelijke eigenaar nodig die het volgens een cadans (minstens jaarlijks) beoordeelt en het vervangen of afbouwen aanstuurt, anders rot het logboek tot folklore die mensen selectief citeren en weinig vertrouwen. Neem bewijs mee: hoeveel van je records ongedateerd zijn, hoeveel een leverancier of prijs beschrijven die intussen veranderd is en wanneer elk voor het laatst is beoordeeld. In overheids- en gereguleerde omgevingen is dit scherper, omdat een onveranderlijke, vervangen keten precies is waarop auditors en opvolgende leveranciers vertrouwen voor een traceerbare motivering. Bepaal je levenscyclus expliciet, zet tijdstempels op afzonderlijke beweringen die afdrijven en wijs beheerders aan, zodat het logboek een levend bezit blijft in plaats van een kerkhof.

3. **Moet je op één sjabloon over alle teams standaardiseren, en hoeveel stringentie hebben je beslissingen met de hoogste inzet werkelijk nodig?** Vergelijkbaarheid is een echt voordeel: wanneer elk team dezelfde vorm gebruikt (Nygard, MADR of vergelijkbaar), kan een nieuw team drie eerdere records vinden en de redenering in een middag overnemen in plaats van een maand debat. De kernspanning is stringentie tegenover adoptie, want het zwaarste sjabloon dat niemand gebruikt legt niets vast, terwijl het lichtste dat iedereen gebruikt in waarde groeit. Neem bewijs mee: worden records daadwerkelijk geschreven, en zijn, apart daarvan, grote, betwiste, dure beslissingen onderanalyseerd omdat de lichte vorm het afwegen van alternatieven oversloeg? Voor ondernemingen die overlappende keuzes over teams coördineren, voorkomt een gedeeld sjabloon plus een doorzoekbare index uiteenlopende, onverenigbare beslissingen. Kies standaard voor licht voor het gewone geval, en spreek vooraf af welke eenwegdeur-beslissingen een zwaardere vorm met gewogen alternatieven rechtvaardigen.

4. **Wat rechtvaardigt het eigenlijk om een besluitenlogboek op te stellen, en wie heeft de bevoegdheid om te zeggen dat een keuze er geen nodig heeft?** Leg de lat te hoog en de redenering achter ingrijpende keuzes verdampt. Leg haar te laag en het logboek vult zich met trivia die de records begraaft die mensen echt nodig hebben. Voor een grote organisatie betekent een onduidelijke drempel dat elk team een eigen drempel verzint, zodat de dekking ongelijk wordt en niemand kan vertrouwen dat een ontbrekend record duidt op een onbelangrijke beslissing. Neem bewijs mee naar de discussie: een handvol recente beslissingen die zijn vastgelegd maar dat niet hoefden, en pijnlijke die niet zijn vastgelegd en je later een herontdekking kostten. Spreek een eenvoudige toets af, zoals vastleggen wanneer een toekomstige ontwikkelaar het *waarom* nodig zal hebben en keuzes met laag risico, die op zichzelf staan of al gedocumenteerd zijn overslaan. In gereguleerde en overheidsomgevingen verschuift de afweging, omdat een auditmandaat kan eisen dat er een record is voor elke architectonisch belangrijke eis, ongeacht of het team het schrijven waard vindt, dus benoem vooraf welke beslissingen niet onderhandelbaar zijn.

5. **Zijn je records echte redenering, vastgelegd op het moment van beslissen, of papierwerk dat achteraf is geschreven om aan een mandaat te voldoen?** Een record dat achteraf is gemaakt om een ticket te sluiten, heeft de neiging de gekozen optie wit te wassen en stilletjes de alternatieven weg te laten die echt zijn afgewogen, wat precies de informatie is die een toekomstige lezer het meest nodig heeft. De concurrerende druk is reëel: het *waarom* opschrijven vóór of tijdens een beslissing voelt trager dan opleveren, en het schriftelijk toegeven van de verworpen paden vraagt psychologische veiligheid die sommige teams missen. Leg een steekproef van recente records op tafel en vraag eerlijk of de context en verworpen alternatieven lezen als echte overweging of als achteraf bijgepaste rechtvaardiging. Voor een groot team zijn holle records erger dan geen, omdat ze mensen leren dat het logboek niet te vertrouwen is. Bij audit in onderneming en overheid is dit onderscheid scherp: toezichthouders en opvolgende leveranciers zijn afhankelijk van een motivering die weerspiegelt wat werkelijk is overwogen, en een record dat als toneel leest ondermijnt de zekerheid die het logboek moet bieden.

6. **Welke van je beslissingen met de hoogste inzet kun je borgen met een geautomatiseerde fitness function, in plaats van erop te vertrouwen dat periodieke handmatige review een overtreding zal opmerken?** Een besluitenlogboek documenteert een keuze, maar alleen een geautomatiseerde controle in continuous integration voorkomt dat die keuze stilletjes erodeert als tientallen ontwikkelaars de code over jaren raken. De afweging is investering, omdat het schrijven en onderhouden van fitness functions (met tools als ArchUnit) engineeringtijd kost, en veel beslissingen, vooral proces- of leverancierskeuzes, helemaal niet mechanisch toetsbaar zijn. Neem bewijs mee: welke grensbeslissingen (moduleafhankelijkheden, uitzenden van gebeurtenissen, regels voor datatoegang) stilletjes zijn geschonden en pas laat in review of productie zijn betrapt. Voor een onderneming met veel teams veranderen fitness functions governance van een centraal knelpunt in continue handhaving die schaalt zonder iedereen te vertragen. In gereguleerde en overheidscontexten is een geautomatiseerde, altijd aanstaande controle veel sterker auditbewijs dan een handtekening onder een review, omdat ze bewijst dat de beslissing vandaag nog geldt in plaats van dat iemand haar ooit heeft goedgekeurd.

## Sectorperspectief

**Startup.** Houd het bij de gewoonte en niets anders: een map `decisions/` in je hoofdrepo, en een notitie met twee onderdelen (context en keuze) wanneer je een besluit neemt waar je toekomstige zelf vragen over zal hebben. Sla levenscyclus, rollen en goedkeurders volledig over, want proces dat je niet kunt volhouden is proces dat je zult laten vallen. Het ene record dat je eerste aanwerving het vragen "waarom is het systeem zo gebouwd?" bespaart, betaalt al voor de hele praktijk.

**Kleinbedrijf.** Zonder aparte architect en met weinig tijd zet je records waar je team al werkt, of dat nu een wiki, een gedeeld document of de repo is, in plaats van een speciale tool te kopen. De gewoonte doet er veel meer toe dan de tooling, dus verlaag de drempel: noem de map `decisions` in plaats van `adr`, en leg leveranciers- en bouwen-of-kopen-keuzes in één adem vast met technische. Als je steunt op externe medewerkers, is een kort, gedateerd record van waarom je een leverancier of platform koos goedkope verzekering tegen vastzitten aan een keuze die niemand later kan uitleggen.

**Grote onderneming.** Het werk is coördinatie over veel teams: standaardiseer op één sjabloon, publiceer een doorzoekbare index over teams heen en ondersteun belangrijke grensbeslissingen met fitness functions, zodat overtredingen de build laten falen in plaats van op review te wachten. Wijs aan elk record een verantwoordelijke beheerder toe met een beoordelingscadans, zodat het logboek een levend bezit blijft in plaats van te vervallen tot folklore. Goed uitgevoerd wordt de redenering van één team over een moeilijke keuze een bezit dat het volgende team in een middag overneemt in plaats van opnieuw te bepleiten.

**Overheid.** Aanbestedingsregels, transparantie en publieke verantwoording maken besluitenlogboeken bijna verplicht. Eis een onveranderlijk, vervangen record voor elke architectonisch belangrijke eis, elk met de keuze gekoppeld aan het mandaat of de compliancecontrole waaraan ze voldoet, zodat toezichthouders een traceerbare motivering vinden in plaats van een reconstructie. Omdat publieke systemen meerjarige levensduren met meerdere leveranciers beslaan, is een goed bijgehouden logboek vaak wat een opvolgende leverancier in staat stelt te begrijpen waarom het systeem is gevormd zoals het is en het werk voort te zetten zonder beslechte kwesties opnieuw te bepleiten.

## Voorbeelden

**Startup.** Een startup van vijf personen voegt een eenvoudige map `decisions/` toe aan zijn hoofdrepo, met een notitie van twee onderdelen (context en keuze) wanneer iemand een besluit neemt waar hun toekomstige zelf vragen over zal hebben. Er is geen levenscyclus, geen rollen en geen goedkeurders: alleen de gewoonte om het *waarom* naast de code op te schrijven. Wanneer hun eerste aanwerving zes maanden later binnenkomt, leest ze de hele map in een uur en stopt ze met vragen "waarom is het zo gebouwd?" Het lichte logboek kost minuten per invoer en bespaart hen de herontdekkingsbelasting die toeslaat lang voordat een team groot wordt.

**Grote onderneming.** Een retailer met 30 engineeringteams standaardiseert op records in MADR-formaat in elke repo, plus een doorzoekbare centrale index. Wanneer een nieuw team voor "[monorepo](https://en.wikipedia.org/wiki/Monorepo) versus multirepo" staat, vinden ze drie eerdere records met context en gevolgen, en nemen ze de redenering in een middag over in plaats van een maand debat. Belangrijke grensbeslissingen (eigenaarschap van services, regels voor datatoegang) worden ondersteund door ArchUnit-fitness functions, zodat overtredingen de build laten falen in plaats van in review te worden betrapt. Dat is governance die schaalt zonder centraal knelpunt.

**Overheid.** Een overheidsdienst die een uitkeringssysteem moderniseert eist een ADR voor elke architectonisch belangrijke eis, elk met de beslissing gekoppeld aan het mandaat of de compliancecontrole waaraan ze voldoet (toegankelijkheid, dataresidentie, controleerbaarheid). Records zijn onveranderlijk en worden vervangen, wat een traceerbaar logboek oplevert dat aan toezichtsreview voldoet. Cruciaal is dat het een opvolgende leverancier ook laat begrijpen *waarom* het systeem is gevormd zoals het is, waarmee de continuïteit over de meerjarige levensduren met meerdere leveranciers die typisch zijn voor publieke programma's behouden blijft (hoofdstuk 4.6, 10.4).

## Zakelijke onderbouwing: motivatie, ROI en TCO

Een besluitenlogboek kost minuten om te schrijven en nog een paar om te beoordelen. Het rendement is vermeden *herbeslissings*kosten en vermeden *verkeerde-omkering*skosten, die beide groot en terugkerend zijn bij langlevende systemen. Elke keer dat een team een beslechte kwestie opnieuw bepleit, of een gezonde keuze terugdraait omdat niemand de beperking erachter meer wist, betaalt het in tijd van senior engineers en vaak in een incident. Een besluitenlogboek zet die terugkerende belasting om in een eenmalig schrijfwerk.

Wat **total cost of ownership** betreft, behoren besluitenlogboeken tot de documentatie met de hoogste hefboom die je kunt bijhouden, omdat ze het meest personeelswisselingsgevoelige bezit raken: de motivering. Onboarding gaat sneller (nieuwe aanwervingen lezen het *waarom*, niet alleen de code). Modernisering is veiliger (hoofdstuk 3.6: je kunt essentiële van bijkomstige beslissingen onderscheiden). Audits zijn goedkoper (het bewijs bestaat al). De kosten van *niet* bijhouden zijn onzichtbaar op welk dashboard dan ook en stapelen zich stilletjes op bij elk vertrek. Wijs om het bestuur te overtuigen op een recente dure herontdekking, of een teruggedraaide beslissing die een incident veroorzaakte, en merk op dat het oplossen vrijwel niets kost.

## Antipatronen en valkuilen

- **Het *wat* vastleggen zonder *waarom*:** context en verworpen alternatieven weglaten, het hele punt.
- **Papierwerk achteraf:** records geschreven om aan een mandaat te voldoen, niet om te denken. Ze lezen hol en niemand vertrouwt ze.
- **Megadocumenten met meerdere beslissingen:** één gigantische pagina waar niemand doorheen komt of die niemand schoon kan vervangen.
- **Ongedateerde beweringen:** kosten en beperkingen die ooit waar waren, gepresenteerd als tijdloos.
- **Stille bewerkingen:** de geschiedenis van een beslissing wijzigen zonder gedateerde notitie, wat het auditspoor vernietigt.
- **Write-only logboeken:** records die worden gemaakt en nooit worden getoond op het moment dat ze relevant zijn, zodat ze gedrag niet beïnvloeden.
- **Poortwachterschap via afkortingen:** erop staan "ADR" en "architectuur" te gebruiken en daarmee bijdragen ontmoedigen.
- **Geen levenscyclus:** records die nooit worden beoordeeld, vervangen of afgebouwd en vervallen tot desinformatie.

## Volwassenheidsmodel

- **Niveau 1 (Initiëren):** Beslissingen leven in hoofden van mensen, chatthreads en commitberichten. Vastleggen is reactief en ad hoc, en motivering gaat routinematig verloren bij personeelswisselingen.
- **Niveau 2 (Ontwikkelen):** Sommige teams houden records bij, in uiteenlopende formaten en sjablonen, wanneer iemand eraan denkt. De praktijk is inconsistent over teams, zonder gedeeld logboek, naamgeving of proces.
- **Niveau 3 (Standaardiseren):** Eén sjabloon, opslag in de repo en een gedefinieerde levenscyclus en governance (criteria om op te stellen of over te slaan, rollen, beoordelingscadans) zijn gedocumenteerd en consistent organisatiebreed toegepast. Records worden beoordeeld en vervangen in plaats van stilletjes bewerkt.
- **Niveau 4 (Beheersen):** Het besluitenlogboek wordt afgemeten aan uitgangswaarden: dekking (het aandeel architectonisch belangrijke beslissingen met een record), versheid (het aandeel records dat binnen zijn cadans is beoordeeld, plus het aantal ongedateerde of verouderde beweringen) en vindbaarheid (hoe vaak een relevant record de ontwikkelaar bereikte die de bestuurde code wijzigde). Verantwoordelijke beheerders handelen op deze statistieken, vervangen verouderde records en dichten dekkingsgaten op bewijs in plaats van op anekdote.
- **Niveau 5 (Orkestreren):** Een doorzoekbaar besluitenlogboek over teams heen is geïntegreerd in het dagelijks werk: relevante records verschijnen automatisch bij de wijzigingen die ze besturen, belangrijke beslissingen worden geborgd door fitness functions in continuous integration en het logboek voedt onboarding, modernisering en audit als levend bezit. De organisatie verbetert de praktijk zelf continu, schaft records af, vervangt ze en herbegrenst ze naarmate het systeem en zijn beperkingen verschuiven, en herbalanceert waar ze stringentie investeert naarmate het portfolio van beslissingen groeit.

## Ideeën voor discussie

1. Wat was de laatste beslissing die je team terugdraaide of opnieuw bepleitte omdat niemand de oorspronkelijke redenering meer wist?
2. Zou het hernoemen van je map `adr/` naar `decisions/` veranderen wie bijdraagt en wat er wordt vastgelegd?
3. Welke van je kritieke beslissingen zou je vandaag kunnen borgen met een geautomatiseerde fitness function?
4. Onveranderlijk-en-vervangen of levend document: wat past bij je auditverplichtingen en je cultuur, en waarom?
5. Hoe zou een nieuwe aanwerving (of een opvolgende leverancier) nu ontdekken *waarom* je systeem gevormd is zoals het is?
6. Wat rechtvaardigt het opstellen van een besluitenlogboek in jouw team, en wat rechtvaardigt het *niet* opstellen ervan?

## Belangrijkste inzichten

- Een besluitenlogboek legt één belangrijke beslissing vast met haar **context en gevolgen**: het *waarom*, niet alleen het *wat*.
- Houd records **specifiek, van een tijdstempel voorzien en licht**. Standaardiseer op één sjabloon (Nygard, MADR of vergelijkbaar).
- Bewaar ze **in versiebeheer naast de code**. Overweeg ze "decisions" te noemen om bijdragen te verbreden.
- Definieer een **levenscyclus en governance** (criteria om op te stellen of over te slaan, rollen, beoordelingscadans). Bewaar zwaar proces voor eenwegdeur-beslissingen.
- Maak beslissingen **vindbaar** op het moment van wijziging en, waar mogelijk, **toetsbaar** via fitness functions.
- De ROI is vermeden herontdekkings- en verkeerde-omkeringskosten. Het TCO-argument is het sterkst waar personeelswisselingen, modernisering en audit het meest tellen. Zie hoofdstuk 1.5 (besluitvorming en governance) en hoofdstuk 3.1 (architectuurfundamenten).

## Referenties en verder lezen

- Michael Nygard, "Documenting Architecture Decisions" (2011): the foundational lightweight ADR.
- MADR: Markdown Any Decision Records project (adr.github.io/madr).
- Jeff Tyree and Art Akerman, "Architecture Decisions: Demystifying Architecture" (*IEEE Software*, 2005).
- Olaf Zimmermann, "Y-Statements" and "Architectural Decision Making" (ozimmer.ch).
- Joel Parker Henderson, *Architecture Decision Record (ADR)*: templates, examples, and teamwork guidance (github.com/joelparkerhenderson/architecture-decision-record).
- ThoughtWorks Technology Radar: "Lightweight Architecture Decision Records."
- Neal Ford, Rebecca Parsons, Patrick Kua, Pramod Sadalage, *Building Evolutionary Architectures* (fitness functions).
- AWS Prescriptive Guidance, "ADR process"; Red Hat, "Why you should use ADRs."
- Wikipedia, "Architectural decision" and "Architecturally significant requirements."
