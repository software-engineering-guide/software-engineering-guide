# 5.1 UX-grundlag

## Overblik og motivation

[Brugeroplevelse](https://en.wikipedia.org/wiki/User_experience) (UX) handler om at forstå mennesker (deres mål, deres sammenhænge, deres begrænsninger) og derefter forme software, så den hjælper dem med at lykkes med mindst mulig gnidning. Det er ikke pynt, du påfører til sidst. Det er en arbejdsmåde, der begynder før den første kodelinje og fortsætter længe efter udgivelsen. Dette kapitel dækker de research-, modellerings- og [design thinking](https://en.wikipedia.org/wiki/Design_thinking)-praksisser, der lader en stor organisation træffe produktbeslutninger ud fra dokumentation frem for gæt.

For store teams er UX lige så meget et koordineringsproblem som et håndværk. Når dusinvis af squads leverer ind i ét fælles produkt, hober uens mentale modeller, duplikerede flows og selvmodsigende terminologi sig op til en forvirrende helhed, intet enkelt team ejer. Et fælles UX-grundlag, bygget af fælles personas, aftalte kundeoplevelsesrejser og en dokumenteret [informationsarkitektur](https://en.wikipedia.org/wiki/Information_architecture), giver hvert team det samme kort over brugeren, så deres separate beslutninger tilsammen giver en sammenhængende oplevelse. Uden det optimerer hvert team lokalt, og produktet som helhed giver ingen mening.

Virksomheder og det offentlige hæver indsatsen. Virksomhedssoftware har ofte fastlåste brugere, der ikke kan gå, så dårlig UX betales i træning, supporttickets, fejl og tabt produktivitet frem for ved at folk forlader den. Offentlige tjenester når ofte hele befolkningen, herunder mennesker i krise, på gamle enheder, med lav digital tryghed eller uden nogen alternativ udbyder. Her er UX-kvalitet et spørgsmål om lighed og borgerlig tillid: en dårligt designet ydelsesansøgning kan nægte nogen mad eller bolig, ikke fordi de ikke er berettigede, men fordi de ikke kunne færdiggøre formularen.

## Grundprincipper

- Design for rigtige mennesker, der udfører rigtige opgaver under rigtige forhold, ikke for en idealiseret bruger på en hurtig forbindelse med fuld opmærksomhed.
- Research reducerer risiko. Det billigste tidspunkt at opdage en forkert antagelse er, før du har bygget oven på den.
- Brugere kan ikke pålideligt fortælle dig, hvad de vil gøre; observér adfærd, ikke blot angivne præferencer.
- Fokusér på det job, brugeren forsøger at få gjort, ikke den funktion, du vil levere.
- Ensartethed er en funktion: en sammenhængende mental model på tværs af produktet sænker den kognitive belastning.
- [Tilgængelighed](https://en.wikipedia.org/wiki/Accessibility) og inklusion er en del af god UX fra start, ikke en senere compliance-gennemgang.
- Kvalitative og kvantitative metoder besvarer forskellige spørgsmål; brug begge.
- Lille, hyppig research slår sjælden, tung research.

## Anbefalinger

### Etablér kontinuerlig research med blandede metoder

Sigt efter en let, men kontinuerlig researchpraksis frem for lejlighedsvise store undersøgelser. Interviews afslører motivationer og mentale modeller. [Brugbarhedstest](https://en.wikipedia.org/wiki/Usability_testing) afslører, hvor designs bryder sammen; fem til otte deltagere pr. runde afdækker de fleste af de alvorlige problemer. Spørgeskemaer måler holdninger i skala, men kan ikke forklare "hvorfor." Analyse og instrumentering viser, hvad folk faktisk gør på tværs af hele populationen. Par en kvalitativ metode (hvorfor) med en kvantitativ (hvor mange), så fund både forklares og størrelsesbestemmes. Og hold et researcharkiv, så indsigter forbliver søgbare og genbrugelige på tværs af teams i stedet for at gå tabt i én squads slides.

### Modellér brugere med personas, kundeoplevelsesrejser og jobs-to-be-done

Byg et lille sæt evidensbaserede personas, der indfanger mål, sammenhænge og begrænsninger, ikke demografiske karikaturer. Ram behov ind som jobs-to-be-done, det underliggende udfald en bruger forsøger at opnå frem for en funktion ("når jeg mister mit job, vil jeg hurtigt forstå, hvilken støtte jeg er berettiget til, så jeg kan blive ved med at betale husleje"). Det holder fokus på udfald frem for funktioner. Kundeoplevelsesrejser kortlægger hele oplevelsen på tværs af kanaler og over tid og afslører huller og overdragelser, ingen enkelt skærm viser. For tjenester med tung backstage-drift (callcentre, sagsbehandlere, ordreudførelse) brug [servicetegninger](https://en.wikipedia.org/wiki/Service_blueprint) til at forbinde frontstage-oplevelsen med de systemer og medarbejdere, der står bag.

### Design informationsarkitekturen bevidst

Informationsarkitektur (IA) er, hvordan indhold, funktioner og navigation struktureres og benævnes. Brug [kortsortering](https://en.wikipedia.org/wiki/Card_sorting) og trætest til at udlede den struktur fra brugernes mentale modeller frem for fra jeres organisationsdiagram. En almindelig fejl i store organisationer er at eksponere interne afdelingsgrænser som navigation på øverste niveau. Etablér et kontrolleret ordforråd, så det samme begreb har det samme navn overalt. [Interaktionsdesign](https://en.wikipedia.org/wiki/Interaction_design) definerer så adfærden fra øjeblik til øjeblik: tilstande, feedback, fejlretning og flowet mellem trin.

### Anvend design thinking pragmatisk

Dobbeltdiamantmodellen (divergér og konvergér så for at definere det rette problem, og divergér og konvergér derefter for at designe den rette løsning) er en nyttig ramme. Behandl den dog som en tankegang, ikke en stiv proces med porte. I praksis kør stramme løkker: formulér en hypotese, skitsér, test med en håndfuld brugere, og lær inden for dage. Gem den tungere afdækning til reelt nye eller højrisikoproblemer. Og pas på "innovationsteater," hvor workshops producerer post-its, men ingen leveret ændring.

### Integrér UX i leveringen

Indlejr designere og researchere i leveringsteams frem for at køre en separat "UX-afdeling", der overdrager specifikationer hen over en mur. Gør researchfund til et fast input til prioritering. Læg UX-kvalitetsporte, såsom brugbarhedsbenchmarks og tilgængelighedstjek, ind i definitionen af færdig. Og følg udfaldsmålinger (opgavesucces, tid på opgave, fejlrate, tilfredshed) lige ved siden af jeres leveringsmålinger.

## Afvejninger: fordele og ulemper

| Tilgang | Fordele | Ulemper |
|---|---|---|
| Kontinuerlig afdækningsresearch | Fanger problemer tidligt, bygger fælles forståelse | Løbende omkostning, kræver rekrutteringspipeline og dygtigt personale |
| Tung research på forhånd | Dyb indsigt før større investering | Langsom, kan forsinke læring, som kun levering afslører |
| Beslutninger kun på analyse | Skalerer, objektiv, billig når først instrumenteret | Forklarer hvad, men ikke hvorfor; blind over for ikke-brugere og grænsetilfælde |
| Personas og kundeoplevelsesrejser | Bringer mange teams på linje om én model af brugeren | Bliver forældede, kan blive fiktion, hvis ikke genopfrisket med data |
| Indlejrede designere | Hurtig feedback, delt ejerskab | Sværere at holde håndværket ensartet på tværs af mange teams |

Hver organisation afvejer researchinvestering mod leveringshastighed. Fejlen er at behandle det som enten-eller. Den produktive holdning er proportional: brug mere afdækning på beslutninger, der er dyre at omgøre (kerne-IA, primære flows, platformsvalg), og mindre på detaljer, I let kan ændre senere. Omkostningen ved research er næsten altid lille ved siden af omkostningen ved at bygge det forkerte godt.

## Spørgsmål til drøftelse med dit team

1. **Hvem ejer den fælles informationsarkitektur og det kontrollerede ordforråd, og hvad sker der, når et team vil afvige?** I skala er den mest almindelige fejl at lade hver squad eksponere sin egen organisationsdiagramstruktur og sine egne navne for det samme begreb, så produktet ender med tre ord for én ting og navigation, der spejler afdelinger i stedet for brugeropgaver. Beslut nu, om IA og ordforråd ejes centralt, udledes af kortsortering og trætest frem for intern politik, og hvordan et team anmoder om en ændring. Det betyder mere i virksomheder og det offentlige, fordi fastlåste brugere ikke kan gå, så inkoherens betales i træning, supporttickets og fejl frem for frafald. Tag den nuværende liste over duplikerede termer og modstridende flows med som dokumentation. Hvis I ikke kan nævne en ejer, er det jeres første handlingspunkt.

2. **Hvad er vores rekrutteringspipeline for researchdeltagere, og når den assisterede digitale, lavtillids- og ikke-digitale brugere?** Kontinuerlig afdækning virker kun, hvis I kan komme foran rigtige brugere hver uge, og de sværeste at rekruttere er ofte dem, der mest har brug for tjenesten: mennesker i krise, på gamle enheder eller som normalt er afhængige af hjælp. At teste kun selvsikre, forbundne frivillige giver jer en smigrende, men falsk læsning, især for offentlige tjenester, hvor lige adgang er hele pointen. Aftal, hvem der driver rekruttering, hvilke incitamenter I tilbyder, og hvordan I observerer assisterede digitale sessioner uden at øge et sårbart menneskes byrde. Tag deltagerdemografien fra jeres tre seneste undersøgelser med og tjek den mod jeres faktiske brugerbase. Hvis den hælder mod let tilgængelige brugere, så ret pipelinen, før I stoler på fundene.

3. **Hvilke UX-kvalitetsporte hører hjemme i vores definition af færdig, og hvordan forhindrer vi, at de bliver teater?** At indlejre designere og researchere betaler sig kun, hvis research er et fast input til prioritering, og hvis brugbarheds- og tilgængelighedstjek faktisk blokerer en historie fra at blive leveret, ikke et slidedæk alle nikker til og ignorerer. Vælg konkrete udfaldsmålinger, I vil følge ved siden af leveringsmålinger: opgavesucces, tid på opgave, fejlrate og tilfredshed. Risikoen er research kørt for at retfærdiggøre allerede trufne beslutninger, så aftal, hvem der kan nedlægge veto mod en lancering på en UX-port, og hvilken dokumentation der overtrumfer en direktørs mening. Tag én nylig funktion med og spørg, om dens research ændrede beslutningen eller blot dekorerede den. Hvis fund aldrig flytter en køreplan, er jeres porte kosmetiske.

4. **Hvordan forhindrer vi, at vores personas, kundeoplevelsesrejser og IA forfalder til fiktion, når den research, der producerede dem, er et år gammel?** Fælles modeller er det, der lader dusinvis af teams designe mod én sammenhængende oplevelse, men de virker kun, så længe de stadig beskriver rigtige brugere, og i det øjeblik en persona bliver et artefakt, folk citerer for at vinde diskussioner frem for et resumé af dokumentation, gør den aktiv skade. Beslut, hvem der ejer opfriskningen af hver model, på hvilken kadence og mod hvilke data (friske interviews, analyse, supporttemaer), og aftal en synlig "sidst valideret"-dato, så forældede modeller er åbenlyse. Det modstridende hensyn er omkostning: at opfriske alt kontinuerligt er spild, så bind opfriskningsfrekvens til, hvor hurtigt den del af brugerbasen eller rejsen faktisk ændrer sig. Tag proveniensen af jeres nuværende øverste personas med og spørg, hvornår hver sidst blev tjekket mod en rigtig bruger. I virksomheder og det offentlige, hvor en fastlåst eller offentlig brugerbase skifter langsomt, men væsentligt (en aldrende befolkning, en ny ydelse, et enhedsskifte), kan en model, der stille driver ud af dato, styre års investering mod brugere, der ikke længere findes.

5. **Hvor bor tilgængelighed i vores proces, og kan vi bevise, at en udgivelse opfylder den, før den leveres, frem for efter en klage?** At behandle tilgængelighed som en sen compliance-gennemgang er både den mest almindelige og den dyreste fejl, fordi det koster langt mere at eftermontere semantik, fokusrækkefølge og kontrast i en bygget grænseflade end at designe dem ind. Beslut, hvilken standard I holder jer til (for eksempel WCAG, Web Content Accessibility Guidelines), om overensstemmelse er en blokerende port i definitionen af færdig, og hvem der er ansvarlig, når en utilgængelig funktion når produktion. Spændingen er hastighed versus inklusion, og teams under deadlinepres dropper stille de tjek, der ikke håndhæves. Tag jeres seneste revision, den automatiserede og manuelle dækning bag den og antallet af tilgængelighedsproblemer fundet efter udgivelse frem for før med. For det offentlige især er dette ikke valgfri høflighed: det er ofte en juridisk pligt og et spørgsmål om lighed, da en offentlig tjeneste, der udelukker handicappede eller assisteret-digitale brugere, har fejlet i sit kerneformål, ikke et sekundært.

6. **Når vores analyse og vores kvalitative research er uenige, hvordan afgør vi, hvilken vi tror på, og hvem er voldgiftsmand?** Store organisationer akkumulerer både dashboards, der viser, hvad tusinder af brugere gør, og interviews, der forklarer, hvorfor en håndfuld opfører sig, som de gør, og de to vil rutinemæssigt pege i modsatte retninger: et flow med høj gennemførelse, der stille ydmyger folk, eller en funktion, brugere roser i sessioner, men aldrig rører i skala. Aftal på forhånd, hvordan I triangulerer, hvilket spørgsmål hver metode stoles på til at besvare (analyse til omfang og rækkevidde, research til årsag og mening), og hvem der har autoritet til at træffe beslutningen, når de er i konflikt. Risikoen er at plukke den kilde, der smigrer den allerede valgte plan. Tag en konkret nylig uenighed med og gå igennem, hvordan den faktisk blev løst. I virksomheds- og offentlige sammenhænge skærpes indsatsen, fordi analyse systematisk undertæller netop de mennesker, der betyder mest: ikke-brugere, dem der forlader og dem på hjælpeteknologi dukker sjældent op i tragten, så at stole på tal alene kan gøre de udelukkede usynlige.

## Sektorperspektiv

**Startup.** I har ingen researcher og ingen tid til et arkiv, så gør research til en grundlægger-vane: sid ved siden af fem rigtige brugere en eftermiddag, før I bygger det næste. Spring formelle personas og kundeoplevelsesrejser over; en fælles forståelse af det ene job, I løser, genopfrisket ved at se på folk ugentligt, slår dokumentation, ingen vedligeholder. Jeres fordel er, at hele teamet kan optage en indsigt samme dag, den opstår, så beskyt den hastighed og modstå ceremoni.

**Lille virksomhed.** Uden en UX-specialist og med et stramt budget så støt jer til de konventioner, jeres brugere allerede kender, frem for at opfinde jeres egne, og køb værktøj med fornuftige standarder i stedet for at designe flows fra bunden. Gør den billige research med høj værdi selv: en håndfuld brugbarhedssessioner over et videoopkald og en gennemlæsning af jeres supporttickets afdækker de fleste af de alvorlige problemer. Behandl tilgængelighedsgrundprincipper (kontrast, labels, tastaturadgang) som minimum, I får fra et godt komponentbibliotek, frem for et projekt, I bemander.

**Stor virksomhed.** Kerneproblemet er sammenhæng på tværs af mange teams, så invester i de fælles grundlag: ejede personas, vedligeholdte kundeoplevelsesrejser, et kontrolleret ordforråd og en dokumenteret informationsarkitektur, som squads designer mod frem for uden om. Indlejr designere og researchere i leveringsteams, men styr håndværket centralt, så produktet ikke splintres i inkonsistente dialekter. Finansiér et researcharkiv og kvalitetsporte i definitionen af færdig, og følg UX-udfaldsmålinger som en portefølje, så intet enkelt teams lokale optimering forringer helheden.

**Offentlig sektor.** Tilgængelighed og lige adgang er pligter, ikke præferencer, så hold udgivelser til en offentliggjort standard og research med hele spektret af offentligheden, herunder assisterede digitale, lavtillids- og ikke-digitale brugere. Indkøb og åbenhed former leveringen: offentliggør jeres designprincipper og researchmetoder, strukturér tjenester omkring borgernes livsbegivenheder frem for interne afdelinger, og hold dokumentation for test til revision. Fordi brugere ofte ikke har nogen alternativ udbyder, nægter et flow, de ikke kan færdiggøre, en tjeneste, så behandl gennemførelse for den sværeste at nå bruger som det reelle mål for succes.

## Eksempler

**Startup.** Et startup på fire personer, der byggede et planlægningsværktøj til små klinikker, havde stærke meninger om, hvad receptionister havde brug for, men ingen dokumentation. Før de skrev flere funktioner, sad grundlæggerne ved siden af fem receptionister en eftermiddag hver og så dem arbejde. De lærte, at den reelle smerte ikke var bookinghastighed, men dobbeltbookinger forårsaget af en forvirrende kalendervisning, noget ingen havde tænkt på at nævne i tidligere salgssamtaler. At omformulere produktet omkring det ene job og skitsere og teste rettelser med de samme fem mennesker over en uge forvandlede en gået-i-stå prøveperiode til deres første betalende kunder.

**Stor virksomhed.** En multinational bank konsoliderede syv regionale interne låneoprettelsesværktøjer til én platform. I stedet for at flette funktionssæt kørte teamet kortlægning af kundeoplevelsesrejser og servicetegninger med risikovurderere på tværs af regioner. De fandt, at de "regionale forskelle", alle antog, mest var inkonsistent terminologi og skærmrækkefølge, ikke ægte procesforskelle. En samlet IA og et fælles ordforråd skar risikovurderernes træningstid væsentligt og reducerede behandlingsfejl, fordi medarbejderne nu delte én mental model.

**Offentlig sektor.** En national skattemyndighed, der redesignede sin onlineindberetningstjeneste, kørte modereret brugbarhedstest med skatteydere på tværs af aldre, enheder og niveauer af digital tryghed, plus assisteret digital observation af folk, der normalt er afhængige af hjælp. Testen afslørede, at jargontunge sektionsoverskrifter fik folk til at opgive eller indberette forkert. At omformulere indholdet omkring skatteydernes jobs-to-be-done og omstrukturere IA'en omkring livsbegivenheder frem for interne skattekoder øgede vellykket selvbetjeningsgennemførelse og reducerede callcentervolumen, hvilket direkte sænkede omkostningen ved at betjene og samtidig forbedrede lige adgang.

## Business case: motivation, ROI og TCO

Afkastet af UX kommer fra tre løftestænger: mere succes (flere brugere gennemfører værdifulde opgaver), lavere omkostning ved at betjene (færre supportkontakter, mindre træning, færre fejl) og mindre omarbejde (at fange forkerte retninger, før de bygges). I virksomhedssammenhænge, hvor brugere er fastlåste, viser gevinsten sig som produktivitet og færre fejl frem for konvertering; nogle få sekunder sparet pr. transaktion, på tværs af tusinder af medarbejdere, akkumulerer til store årlige besparelser.

De totale ejeromkostninger må veje omkostningen ved at adoptere mod omkostningen ved ikke at adoptere. Adoptionsomkostningerne er lette at se: researchere og designere, rekruttering og incitamenter til deltagere, værktøj og tid i planen. Omkostningen ved ikke at adoptere er større, men sværere at få øje på: opgivne transaktioner, support- og træningsoverhead, dyre sene redesigns, fejlslagne lanceringer og omdømmemæssig eller juridisk eksponering, når offentlige tjenester udelukker folk. Fordi disse omkostninger er spredt over support-, trænings- og driftsbudgetter frem for produktlinjen, undervurderer ledelsen dem ofte.

For at føre sagen over for ledelsen så bind UX til målinger, ledere allerede følger: gennemførelses- og konverteringsrater, omkostning pr. transaktion, supportticketvolumen, træningsdage og fejl- og omarbejdsrater. Kør en lille, instrumenteret pilot, der viser en målbar før-og-efter, og ekstrapolér så på tværs af porteføljen. At ramme research ind som risikoreduktion på ikke-omgørlige beslutninger plejer at falde i god jord hos økonomi- og styringsinteressenter.

## Anti-mønstre og faldgruber

- **HiPPO-drevet design**: beslutninger truffet efter den bedst lønnede persons mening i stedet for dokumentation.
- **Researchteater**: undersøgelser kørt for at retfærdiggøre allerede trufne beslutninger, fund ignoreret.
- **Personas som fiktion**: opfundne profiler aldrig valideret mod rigtige brugere, brugt til at vinde diskussioner.
- **Organisationsdiagram som IA**: navigation, der spejler interne afdelinger frem for brugeropgaver.
- **Big bang-research**: sjældne, dyre undersøgelser, der kommer for sent til at ændre noget.
- **Kun test af den lykkelige sti**: at ignorere fejltilstande, grænsetilfælde og brugere under stress.
- **Design som et sidste lag maling**: at hente UX ind kun for at få en færdig build til at "se pæn ud."
- **At ignorere assisterede og ikke-digitale brugere**: at designe kun for selvsikre, forbundne brugere.

## Modenhedsmodel

**Niveau 1: Opstart.** Ingen dedikeret UX-praksis. Beslutninger træffes efter mening og den bedst lønnedes instinkt. Research, hvis den overhovedet sker, er ad hoc og reaktiv, udløst af en lancering, der gik dårligt. Flows og terminologi er inkonsistente på tværs af teams, og ingen ejer den samlede oplevelse.

**Niveau 2: Udvikling.** Nogle teams har designere og kører lejlighedsvise brugbarhedstests, og nogle få personas eller kundeoplevelsesrejser findes, men praksis varierer vidt mellem squads og vedligeholdes ikke. UX behandles som en fase frem for en kontinuerlig disciplin og omgås ofte under tidspres. Godt arbejde sker i lommer, men giver ikke tilsammen en helhed på tværs af produktet.

**Niveau 3: Standardisering.** Kontinuerlig research med blandede metoder fodrer prioritering, og fælles personas, kundeoplevelsesrejser og en IA med kontrolleret ordforråd er dokumenteret og brugt på tværs af teams. UX-kvalitetsporte, herunder brugbarhedsbenchmarks og tilgængelighedstjek, sidder i definitionen af færdig og håndhæves i hele organisationen. Et søgbart researcharkiv holder indsigter genbrugelige frem for fanget i én squads slides.

**Niveau 4: Styring.** Praksissen måles mod baselines frem for blot at blive udført. I følger opgavesucces, tid på opgave, fejlrate, tilfredshed og tilgængelighedsoverensstemmelse som aftalte målinger, sætter mål og holder øje med dem over udgivelser. Researchdeltagerstikprøver tjekkes mod den reelle brugerbase, så fund er repræsentative, kvalitetsporte rapporterer beståelsesrater frem for meninger, og omkostningen ved research vejes mod målte reduktioner i supportkontakter, træning og omarbejde. Beslutninger om at levere eller holde hviler på dokumentation mod disse baselines.

**Niveau 5: Orkestrering.** Research er kontinuerlig, udfaldsknyttet og integreret med produkt-, forretnings- og risikoplanlægning på tværs af organisationen. Teams kører kontrollerede eksperimenter, lukker løkken fra indsigt til leveret ændring til målt effekt og pensionerer eller omafgrænser modeller af brugere, efterhånden som populationen og dens rejser skifter. UX-grundlaget tilpasser sig løbende: personas, rejser, IA og standarder opfriskes på dokumentation, og organisationen genbalancerer, hvor den investerer i afdækning, efterhånden som omgørlighed og risiko ændrer sig.

## Idéer til drøftelse

- Hvor meget afdækning er "nok", før man forpligter sig til en retning, og hvem afgør det?
- Hvordan holder I personas og kundeoplevelsesrejser i live, i stedet for at lade dem blive forældede artefakter?
- Når kvantitativ analyse og kvalitativ research er uenige, hvilken stoler I på, og hvorfor?
- Hvordan bør en stor organisation afveje en central UX-standard mod hvert teams autonomi?
- Hvad er den rette måde at researche tjenester brugt af mennesker i krise uden at øge deres byrde?
- Hvordan måler I ROI af research, der forebygger en fejl, I derfor aldrig begik?

## Vigtigste pointer

- UX er en arbejdsmåde fra begyndelsen, ikke pynt til sidst.
- Kombinér kvalitative metoder (hvorfor) med kvantitative metoder (hvor mange).
- Modellér brugere med evidensbaserede personas, kundeoplevelsesrejser, jobs-to-be-done og servicetegninger.
- Strukturér information omkring brugernes mentale modeller, ikke organisationsdiagrammet.
- Behandl design thinking som en pragmatisk tankegang med stramme læringsløkker, ikke en stiv proces.
- Omkostningen ved research er lille sammenlignet med omkostningen ved at bygge det forkerte.
- I virksomheder og det offentlige omsættes UX-kvalitet direkte til produktivitet, omkostning ved at betjene og lige adgang.

## Referencer og videre læsning

- Don Norman, *The Design of Everyday Things*
- Steve Krug, *Don't Make Me Think*
- Erika Hall, *Just Enough Research*
- Kim Goodwin, *Designing for the Digital Age*
- Louis Rosenfeld, Peter Morville, and Jorge Arango, *Information Architecture: For the Web and Beyond*
- Clayton Christensen et al., *Competing Against Luck* (jobs-to-be-done)
- Alan Cooper, *The Inmates Are Running the Asylum*
- Jakob Nielsen, *Usability Engineering*
- UK Government Digital Service, *Service Manual* and *Design Principles*
- U.S. General Services Administration, *18F Methods* and the *U.S. Web Design System* research guidance
- Nielsen Norman Group, research method articles and reports
