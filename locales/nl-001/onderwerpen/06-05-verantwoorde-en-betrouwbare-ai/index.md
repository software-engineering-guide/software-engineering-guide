# 6.5 Verantwoorde en betrouwbare AI

## Overzicht en motivatie

Verantwoorde en betrouwbare AI is de praktijk van AI-systemen bouwen en beheren die eerlijk, transparant, verantwoordelijk, veilig en respectvol voor privacy zijn. Het betekent ook dat je dit alles kunt aantonen aan de betrokken mensen en aan toezichthouders. Naarmate AI beslissingen overneemt die levens van mensen vormgeven (werving, leningen, uitkeringsrecht), is de vraag niet langer alleen "werkt het?" maar "is het juist, en kunnen we het rechtvaardigen?" Een systeem dat gemiddeld nauwkeurig is kan nog steeds oneerlijk zijn voor een subgroep, onverklaarbaar voor de persoon die het raakt of onveilig bij misbruik. Je verdient vertrouwen door deze dimensies bewust aan te pakken, niet door te hopen dat ze zichzelf regelen.

Voor grote teams kan verantwoorde AI niet het werk van één persoon of een vinkje aan het eind zijn. Weef haar in hoe je systemen ontwerpt, evalueert, deployt en bestuurt, met heldere eigenaar en escalatie. Op schaal raken kleine vooroordelen en gaten in toezicht veel mensen. Eén spraakmakend falen kan je reputatie schaden en regulering uitnodigen. Governanceraamwerken bestaan juist omdat ad hoc goede bedoelingen niet schalen.

Overheids- en gereguleerde organisaties staan voor bindende verplichtingen. Opkomende wetgeving, zoals de [AI-verordening van de EU](https://en.wikipedia.org/wiki/Artificial_Intelligence_Act), legt eisen op die naar risico zijn gegradeerd. Standaarden als het NIST AI Risk Management Framework en ISO/IEC 42001 geven je gestructureerde manieren om ze na te komen. Publieke organen moeten onwettige discriminatie vermijden, wegen bieden om geautomatiseerde beslissingen te betwisten en transparant zijn over hoe AI wordt gebruikt bij de uitoefening van publiek gezag. Verantwoorde AI is in deze omgevingen zowel een ethische plicht als een wettelijke noodzaak.

*Zie ook:* hoofdstuk 6.1 (AI-strategie en gereedheid), hoofdstuk 10.5 (ethiek, verantwoording en publiek belang) en hoofdstuk 4.5 (privacy en gegevensbescherming).

## Kernprincipes

- Eerlijkheid is een ontwerpdoel om te meten en te beheren, niet aan te nemen.
- Mensen die door AI-beslissingen worden geraakt verdienen uitleg en een route om ze te betwisten.
- Verantwoording rust bij mensen en de organisatie, nooit bij het model.
- Privacy en veiligheid moeten worden ingebouwd, inclusief bescherming tegen misbruik en kwaadwillig gebruik.
- Governance moet erkende raamwerken volgen zodat ze verdedigbaar en controleerbaar is.
- Menselijk toezicht moet betekenisvol zijn, met echt gezag om te overrulen en stop te zetten.
- Houd rekening met de bredere kosten van AI, inclusief haar milieuvoetafdruk.

## Aanbevelingen

### Detecteer en beperk vooroordeel en oneerlijkheid

Definieer wat eerlijkheid in jouw context betekent. Er zijn meerdere, soms conflicterende wiskundige definities, en de juiste hangt af van de beslissing en de wet. Test modellen op ongelijke prestaties over beschermde en kwetsbare groepen met representatieve data. Doe dit vóór deployment en blijf het erna doen, omdat [vooroordeel](https://en.wikipedia.org/wiki/Algorithmic_bias) kan ontstaan naarmate populaties verschuiven. Beperk het via betere data, herweging, beperkingen of het veranderen van hoe het systeem wordt gebruikt, en documenteer de afwegingen die je accepteerde. Een beschermd attribuut verwijderen verwijdert vooroordeel niet, aangezien proxy's blijven. Behandel eerlijkheid als doorlopende meet- en beheerdiscipline, niet als eenmalige vrijgave.

### Bied uitlegbaarheid, interpreteerbaarheid en transparantie

Stem het niveau van uitleg af op de inzet en het publiek. Geef voor ingrijpende beslissingen betrokken mensen een heldere reden in gewone taal die ze kunnen begrijpen en waar ze naar kunnen handelen. Houd voor interne governance genoeg technische [interpreteerbaarheid](https://en.wikipedia.org/wiki/Explainable_artificial_intelligence) om het systeem te debuggen en te verdedigen. Geef de voorkeur aan inherent interpreteerbare modellen waar de inzet hoog is en interpreteerbaarheid haalbaar. Gebruik waar complexe modellen nodig zijn uitlegtechnieken terwijl je eerlijk bent over hun grenzen. Wees transparant over wanneer AI wordt gebruikt, vooral bij interacties met het publiek.

### Bestuur met erkende raamwerken

Neem een gestructureerde governanceaanpak over in plaats van er een te verzinnen. Het **NIST AI Risk Management Framework** organiseert werk rond besturen, in kaart brengen, meten en beheren van AI-risico. De **AI-verordening van de EU** classificeert systemen naar risico en legt dienovereenkomstig verplichtingen op, met strikte eisen voor gebruik met hoog risico. **ISO/IEC 42001** definieert een AI-managementsysteem dat kan worden geaudit en gecertificeerd. Breng je systemen in kaart tegen deze raamwerken. Houd documentatie bij zoals model- en datakaarten (gestandaardiseerde samenvattingen van het doel, de prestaties en de beperkingen van een model of dataset). Draai risicobeoordelingen vóór deployment en houd een inventaris van AI-systemen bij met hun risiconiveaus en eigenaren. Goede governance wijst heldere rollen, beslisrechten en escalatiepaden toe.

### Zorg voor menselijk toezicht, verantwoording en beroep

Houd een mens betekenisvol aan het roer bij ingrijpende beslissingen, met echt gezag en de informatie die nodig is om het systeem te overrulen, geen rubberen stempel. Wijs heldere verantwoording toe: noem een eigenaar die aanspreekbaar is voor het gedrag van elk systeem. Geef mensen die door geautomatiseerde beslissingen worden geraakt een recht op uitleg en een werkbaar proces om in beroep te gaan bij een mens die de uitkomst kan wijzigen. Log beslissingen en de grondslag ervoor, zodat je beroepen en audits eerlijk en snel kunt afhandelen.

### Bescherm privacy, veiligheid en tegen misbruik

Minimaliseer de persoonsgegevens die je verzamelt en gebruikt, stel een rechtsgrond vast en pas privacytechnieken toe die bij de betrokken gevoeligheid passen. [Red-team](https://en.wikipedia.org/wiki/Red_team) systemen vóór en na deployment om manieren te vinden waarop ze kunnen worden gemanipuleerd, gejailbreakt of misbruikt om schade te veroorzaken, en repareer wat je vindt. Bouw waarborgen tegen het genereren van schadelijke content, het lekken van gevoelige data of het mogelijk maken van misbruik. Plan voor incidenten: bewaking, respons en openbaarmaking. Overweeg [dual use](https://en.wikipedia.org/wiki/Dual-use_technology) (hetzelfde vermogen dat zowel nuttige als schadelijke doelen dient) en misbruik stroomafwaarts, niet alleen beoogd gebruik.

### Houd rekening met milieukosten

Grote modellen trainen en serveren verbruikt aanzienlijk veel energie en water. Meet en rapporteer de voetafdruk van grote AI-werklasten. Geef de voorkeur aan efficiënte modellen en hardware waar ze aan de behoefte voldoen. Dimensioneer modellen op de taak in plaats van standaard het grootste te nemen, en betrek milieukosten bij architectuur- en aanbestedingsbeslissingen.

## Afwegingen: voor- en nadelen

| Spanning | Eén kant | Andere kant |
|---|---|---|
| Nauwkeurigheid tegenover eerlijkheid | Hoogste gemiddelde nauwkeurigheid | Billijke uitkomsten over groepen |
| Prestaties tegenover interpreteerbaarheid | Complexe, krachtige modellen | Uitlegbare, verdedigbare modellen |
| Automatisering tegenover toezicht | Efficiëntie en schaal | Menselijke controle en verantwoording |
| Datanut tegenover privacy | Rijkere modellen uit meer data | Dataminimalisatie en bescherming |
| Vermogen tegenover veiligheid | Brede, open functionaliteit | Beperkt, bewaakt gedrag |
| Snelheid tegenover governance | Snelle deployment | Grondige review en documentatie |

Er is zelden een gratis lunch. Eerlijkheid verbeteren kan wat nauwkeurigheid kosten. Interpreteerbaarheid kan wat prestaties kosten. Governance kost tijd. Het verantwoorde pad is deze afwegingen bewust te maken, ze te documenteren en te kiezen ten gunste van betrokken mensen en verdedigbaarheid wanneer de inzet hoog is. Governance formuleren als rem op innovatie is een valse tegenstelling. Onbeheerd AI-risico is zelf een bedreiging voor duurzame innovatie.

## Vragen om met je team te bespreken

1. **Welke van onze gedeployde AI-systemen zou de AI-verordening van de EU als hoog risico classificeren, en voldoen we vandaag aan die verplichtingen?** Op risico gegradeerde wetgeving is nu bindend, niet hypothetisch, en een systeem dat over werving, leningen of uitkeringsrecht beslist kan strikte eisen dragen die je mogelijk al schendt. Voor een grote organisatie dwingt deze vraag een eerlijke inventaris af in plaats van een comfortabele aanname dat governance "geregeld" is. Neem je lijst AI-systemen met hun risiconiveaus en eigenaren mee, afgebeeld tegen de AI-verordening van de EU, het NIST AI Risk Management Framework en ISO/IEC 42001 waar relevant. Het signaal om op te letten is elk ingrijpend systeem zonder risicoclassificatie, zonder impactbeoordeling en zonder model- of datakaart. Voor publieke organen die publiek gezag uitoefenen is ontbrekende naleving geen backlogitem maar juridische blootstelling, en het antwoord moet de beoordelingen en documentatie triggeren die die systemen vereisen.

2. **Wanneer een van onze modellen iemand afwijst, kan die persoon dan een reden in gewone taal krijgen en een mens bereiken die de uitkomst werkelijk kan terugdraaien?** Een recht op uitleg en een werkbaar beroep scheiden verantwoordelijke AI van een black box die mensen zonder verhaal schaadt. Gemiddeld gemeten eerlijkheid kan een individu nog steeds in de steek laten, en interpreteerbaarheid gekozen na deployment is meestal theater. Neem een specifieke gedeployde beslissing mee en traceer haar: de reden die de betrokkene ontvangt, het beroepskanaal en of de mens aan de andere kant echt gezag heeft en de gelogde grondslag om te overrulen. In overheids- en gereguleerde omgevingen is een beroepsroute vaak een wettelijke eis, geen beleefdheid. Als de reden onbegrijpelijk is of het beroep op een rubberen stempel uitloopt, is dat het gat om te repareren vóór de volgende release.

3. **Wie is de ene benoemde persoon die verantwoordelijk is wanneer een model schade veroorzaakt, en heeft die echt gezag om het stop te zetten?** Verantwoording rust bij mensen en de organisatie, nooit bij het model, maar dat principe is leeg tot een naam aan elk systeem is gehecht en die persoon werkelijk de stekker eruit kan trekken. Voor een groot team betekent diffuus eigenaarschap dat wanneer een eerlijkheidsfalen of een jailbreak opduikt, iedereen aanneemt dat iemand anders kijkt. Neem je eigenaarschapskaart mee, je escalatiepaden en bewijs dat toezicht betekenisvol is: krijgt de benoemde eigenaar de informatie en de macht om het systeem te overrulen of stop te zetten, of alleen om te knikken? Bespreek hoe je red-teamt op misbruik en kwaadwillig gebruik dat je je nog niet hebt voorgesteld, aangezien alleen beoogd gebruik testen de falen mist die de krantenkoppen halen. Het antwoord moet geen ingrijpend systeem achterlaten zonder verantwoordelijke eigenaar die het kan stoppen.

4. **Welke eerlijkheidsdefinitie kozen we voor elk ingrijpend model, wie tekende ervoor af en houden onze subgroepstatistieken stand in productie?** Eerlijkheid heeft meerdere wiskundige definities die met elkaar conflicteren, dus een model dat gelijke fout-positieven haalt kan gelijke uitkomsten schenden, en een definitie kiezen is een waardeoordeel dat niet moet worden overgelaten aan wie de trainingslus schreef. Voor een groot team verbergt een niet-onderzochte standaard de keuze in code en laat elke groep stroomafwaarts een beslissing erven die niemand besprak. Neem de eerlijkheidsstatistiek mee die je optimaliseerde, de beschermde en kwetsbare groepen waarover je testte, de representatieve data die je gebruikte en de afdrijving die je sinds de lancering hebt gezien, aangezien een beschermd attribuut verwijderen proxy's laat die vooroordeel in leven houden. Noem in omgevingen van onderneming en overheid de persoon met gezag om een eerlijkheidsafweging te accepteren en leg haar vast, want een toezichthouder of ombudsman zal vragen wie besloot dat deze definitie van eerlijk de juiste was voor mensen aan wie een lening, uitkering of baan werd geweigerd. Als na deployment geen subgroepstatistieken worden bewaakt, behandel het model dan als ongemeten in plaats van eerlijk.

5. **Op hoe weinig persoonsgegevens kan elk systeem draaien, en hebben we het ge-red-teamd op het misbruik en dual use waar we liever niet aan denken?** Privacy en veiligheid moeten worden ingebouwd, en de goedkoopste manier om zowel inbreukrisico als misbruikoppervlak te verkleinen is om in de eerste plaats minder data te verzamelen en te bewaren, toch hamsteren teams routinematig invoer "voor het geval het later helpt". Voor een grote organisatie is elk extra veld een vraag naar rechtsgrond, een bewaarverplichting en een grotere prijs voor een aanvaller of een jailbreak. Neem de datainventaris en rechtsgrond voor elk systeem mee, de resultaten van red teaming op manipulatie, lekken en schadelijke generatie en een eerlijke lijst van dual-use-vermogens waar dezelfde functie die een legitieme gebruiker helpt ook iemand helpt die te kwader trouw handelt. Koppel dit in gereguleerde en publieke contexten aan je incidentplan: bewaking, respons en openbaarmaking, want een publiek orgaan dat gevoelige data lekt of een te jailbreaken systeem oplevert staat voor wettelijke plichten, niet alleen schaamte. Als red teaming alleen ooit het beoogde pad oefende, heb je de demo getest, niet het systeem.

6. **Meten en bezitten we de milieuvoetafdruk van onze grote AI-werklasten, of is "gebruik het grootste model" een onbeprijsde standaard?** Grote modellen trainen en serveren verbruikt echte energie en water, en standaard het grootste model nemen voor taken die een kleiner aankan verandert een sluiproute in een terugkerende kost die de organisatie nooit op een dashboard ziet. Voor een groot team dat veel werklasten draait stapelen kleine inefficiënties per aanroep zich op tot een voetafdruk die een aanbestedings- en rapportageverplichting wordt naarmate verwachtingen over openbaarmaking aanscherpen. Neem de gemeten voetafdruk van je zwaarste werklasten mee, een vergelijking van modelgroottes tegen de nauwkeurigheid die de taak werkelijk nodig heeft en de hardware- en servingkeuzes die je kunt rechtzetten. Koppel dit in omgevingen van onderneming en overheid aan duurzaamheidstoezeggingen en aanbestedingscriteria, aangezien publieke organen steeds vaker milieueffect moeten rapporteren en uitgaven moeten rechtvaardigen, en een ongemeten voetafdruk een getal is dat je ooit gevraagd wordt te produceren en niet kunt. Besluit of milieukosten een formele input zijn voor modelkeuze, of geef toe dat ze dat vandaag niet zijn.

## Sectorperspectief

**Startup.** Je kunt geen governanceraad bemannen, dus doe de lichtgewicht versie die toch telt. Kies interpreteerbare modellen waar de beslissing ingrijpend is, schrijf een modelkaart van één pagina, test op ongelijke uitkomsten over de groepen die je kunt meten en log beslissingen zodat je eerlijkheid kunt herzien naarmate je groeit. Geef elke nadelige beslissing een duidelijke reden en een route naar een mens. Dit overslaan is geen snelheid, het is een verplichting die je je niet kunt veroorloven als één oneerlijke beslissing de pers of een toezichthouder bereikt.

**Kleinbedrijf.** Zonder aparte specialist behandel je verantwoorde AI als inkoopvraag: geef de voorkeur aan leveranciers die eerlijkheidstesten documenteren, model- en datakaarten tonen en je laten melden aan klanten wanneer AI wordt gebruikt. Weet welke persoonsgegevens je tools verzamelen en of je een rechtsgrond hebt ze te gebruiken. Houd waar een fout geautomatiseerd antwoord een klant kan schaden een persoon in de lus in plaats van een tool te vertrouwen die je niet kunt inspecteren of uitleggen.

**Grote onderneming.** De taak is governance op schaal over veel teams: breng elk systeem in kaart tegen het NIST AI Risk Management Framework, de AI-verordening van de EU en ISO/IEC 42001, houd een inventaris bij met risiconiveaus en benoemde eigenaren en eis eerlijkheids-, veiligheids- en privacytesten vóór en na lancering. Standaardiseer model- en datakaarten, red teaming en beroepsprocessen zodat groepen ophouden ze opnieuw uit te vinden. Begroot de kosten van governance, toezicht en interpreteerbaarheid expliciet en behandel onbeheerd AI-risico als bedreiging voor de toestemming om te opereren.

**Overheid.** Aanbestedingsregels, transparantie en publieke verantwoording geven elke keuze vorm. Publiceer een transparantieverklaring in gewone taal, draai een impactbeoordeling vóór deployment en houd betekenisvolle menselijke besluitvorming voor elke actie die een burger raakt, met een werkbare beroepsroute. Eis dat leveranciers modelbeperkingen bekendmaken en overdraagbaarheid van data verlenen, vermijd onwettige discriminatie, noem een verantwoordelijke functionaris voor elk systeem en rapporteer de milieuvoetafdruk van grote werklasten.

## Voorbeelden

**Startup.** Een kleine leningstartup die een vroege kredietscorefunctie bouwde kon geen governanceraad bemannen, dus deed ze de lichtgewicht versie die toch telde. Twee oprichters tekenden samen voor het model af, testten het op ongelijke uitkomsten over de groepen die ze konden meten en schreven een korte modelkaart van één pagina over data, grenzen en bekende risico's. Ze kozen een eenvoudiger, beter interpreteerbaar model zodat ze elke afgewezen aanvrager een duidelijke reden en een pad naar menselijke review konden geven, en ze logden beslissingen zodat ze eerlijkheid konden herzien naarmate ze groeiden.

**Grote onderneming.** Een bank die een kredietmodel deployde richtte een AI-governanceraad op, bracht het model in kaart in een categorie met hoog risico en eiste eerlijkheidstesten over demografische groepen vóór en na lancering. Ze documenteerde het model in een modelkaart. Ze gaf afgewezen aanvragers een reden in gewone taal en een beroep bij een menselijke acceptant, en red-teamde het systeem op manipulatie. Ze koos een iets minder nauwkeurig maar beter interpreteerbaar model, omdat ze elke beslissing aan toezichthouders moest uitleggen en verdedigen.

**Overheid.** Een publieke instantie die AI gebruikt om inspectiemiddelen toe te wijzen stemde haar programma af op het NIST AI RMF en de relevante bepalingen van toepasselijke AI-wetgeving. Ze publiceerde een transparantieverklaring die beschreef hoe het systeem werkte en zijn waarborgen. Ze voerde vóór deployment een impactbeoordeling uit, hield betekenisvolle menselijke besluitvorming voor elke actie die een burger raakt en bood een beroepsprocedure. Eerlijkheid werd continu bewaakt, de milieukosten van de werklast werden gerapporteerd en een verantwoordelijke functionaris werd aangewezen als aanspreekbaar voor het systeem.

## Zakelijke onderbouwing: motivatie, ROI en TCO

Verantwoorde AI beschermt waarde evenzeer als ze haar creëert. Het ROI is grotendeels vermeden kosten: minder discriminatieclaims, boetes van toezichthouders en reputatierampen. Soepelere audits. En groter vertrouwen van gebruikers en publiek, wat adoptie drijft. Betrouwbare systemen zijn ook robuuster, omdat de discipline die eerlijkheid en veiligheid produceert ook betere engineering produceert.

De TCO omvat governancepersoneel, eerlijkheids- en veiligheidstesten, documentatie, red teaming, toezichtprocessen en de prestaties die soms worden opgeofferd voor interpreteerbaarheid of eerlijkheid. Weeg dit af tegen de kosten van niet investeren: juridische aansprakelijkheid, gedwongen stillegging, verloren publiek vertrouwen en de veel hogere kosten van governance achteraf aanbrengen na een falen. In gereguleerde contexten is investering in verantwoorde AI steeds vaker niet onderhandelbaar. Maak de zaak voor het bestuur door haar te formuleren als risicobeheer en toestemming om te opereren: de voorwaarde om AI überhaupt op schaal te deployen.

## Antipatronen en valkuilen

- **Eerlijkheid door weglating.** Aannemen dat een model eerlijk is omdat het beschermde attributen negeert.
- **Uitlegbaarheidstheater.** Uitleg produceren die niet werkelijk weerspiegelt hoe beslissingen worden genomen.
- **Toezicht met rubberen stempel.** Nominale menselijke review zonder echt gezag of informatie om te overrulen.
- **Governance als bijgedachte.** Documentatie en review achteraf vastschroeven na ontwerp en deployment.
- **Geen beroepsroute.** Betrokken mensen geen manier laten om een geautomatiseerde beslissing te betwisten.
- **Misbruik negeren.** Alleen beoogd gebruik testen en jailbreaks en wangedrag missen.
- **Voetafdrukblindheid.** Standaard het grootste model nemen zonder acht voor milieukosten.

## Volwassenheidsmodel

1. **Initiëren.** Geen eerlijkheidstesten, uitleg of governance. Verantwoordelijkheid is niet gedefinieerd. Vooroordeel, misbruik en privacyproblemen duiken pas op na schade, en er is geen inventaris van AI-systemen of hun risico's.
2. **Ontwikkelen.** Enig vooroordeeltesten, modelkaarten en red teaming gebeuren op individuele systemen, maar de praktijk is inconsistent over teams. Toezicht is ad hoc. Raamwerken als het NIST AI Risk Management Framework en de AI-verordening van de EU zijn bekend maar slechts gedeeltelijk overgenomen.
3. **Standaardiseren.** Governance is gedocumenteerd en organisatiebreed afgedwongen: systemen zijn afgebeeld tegen erkende raamwerken en ISO/IEC 42001, elk heeft een risiconiveau en een benoemde eigenaar, en eerlijkheids-, veiligheids- en privacytesten, model- en datakaarten, beroepsroutes en red teaming voor systemen met hoog risico zijn vereist in plaats van optioneel.
4. **Beheersen.** Het programma wordt gemeten en beheerst met data: subgroepeerlijkheidsstatistieken, veiligheids- en jailbreakbevindingen, beroepsvolumes en terugdraaipercentages, overrulepercentages van toezicht en de voetafdruk van werklasten worden gevolgd tegen uitgangswaarden en drempels. Drift en ongelijke uitkomsten triggeren gedefinieerde actie. Go/no-go-beslissingen rusten op bewijs in plaats van geruststelling.
5. **Orkestreren.** Verantwoorde AI wordt continu verbeterd en over de organisatie geïntegreerd: bewaking van eerlijkheid, veiligheid en misbruik draait in productie, governance is in oplevering ingebouwd, milieukosten zijn een formele input voor modelkeuze en de organisatie past haar maatregelen aan naarmate wet, risico en vermogen verschuiven, met verantwoordelijkheid bezeten door iedereen in plaats van één team.

## Ideeën voor discussie

- Welke eerlijkheidsdefinitie geldt voor een gegeven beslissing, en wie beslist?
- Hoeveel nauwkeurigheid of prestaties is het acceptabel op te offeren voor eerlijkheid of interpreteerbaarheid?
- Wat maakt menselijk toezicht betekenisvol in plaats van een rubberen stempel?
- Hoe moeten beroepen tegen geautomatiseerde beslissingen worden ontworpen om eerlijk en tijdig te zijn?
- Hoe red-team je op misbruik dat je je nog niet hebt voorgesteld?
- Moeten milieukosten de modelkeuze beïnvloeden, en hoe zou je ze wegen?

## Belangrijkste inzichten

- Betrouwbare AI is door ontwerp eerlijk, uitlegbaar, verantwoordelijk, veilig en privacyrespecterend.
- Eerlijkheid en veiligheid zijn continue meet- en beheerdisciplines, geen eenmalige controles.
- Stem governance af op het NIST AI RMF, de AI-verordening van de EU en ISO/IEC 42001 om verdedigbaar en controleerbaar te zijn.
- Houd betekenisvol menselijk toezicht, heldere verantwoording en een echt recht op beroep.
- Engineer voor privacy en tegen misbruik, en houd rekening met milieukosten.

## Referenties en verder lezen

- National Institute of Standards and Technology, *AI Risk Management Framework (AI RMF 1.0)*.
- European Union, *Artificial Intelligence Act (Regulation on Artificial Intelligence)*.
- ISO/IEC 42001, *Information technology, Artificial intelligence, Management system*.
- Solon Barocas, Moritz Hardt, and Arvind Narayanan, *Fairness and Machine Learning: Limitations and Opportunities*.
- Christoph Molnar, *Interpretable Machine Learning*.
- Cathy O'Neil, *Weapons of Maths Destruction*.
- Emma Strubell, Ananya Ganesh, and Andrew McCallum, *Energy and Policy Considerations for Deep Learning in NLP*.
