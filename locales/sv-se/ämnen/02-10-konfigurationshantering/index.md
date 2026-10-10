# 2.10 Konfigurationshantering

## Översikt och motivation

[Konfigurationshantering](https://en.wikipedia.org/wiki/Software_configuration_management) (SCM, software configuration management) är disciplinen att identifiera komponenterna i ett programvarusystem, kontrollera hur de ändras, registrera tillståndet för varje ändring och verifiera att det du byggde och levererade stämmer med det du avsåg. Den besvarar en fråga som låter enkel men blir svår i stor skala: exakt vad finns i den här releasen, hur hamnade det där och vem godkände det? [SWEBOK](https://en.wikipedia.org/wiki/Software_Engineering_Body_of_Knowledge) behandlar SCM som ett grundläggande kunskapsområde av ett tydligt skäl: varje annan teknisk aktivitet behöver en stabil, känd konfiguration att arbeta mot.

I ett stort team är SCM bindväven som håller tusentals rörliga delar sammanhängande. Källkod, bibliotek, containerbilder, infrastrukturdefinitioner, konfigurationsdata, dokumentation och testartefakter ändras alla på sina egna klockor, och ett levererat system är en specifik kombination av specifika versioner av alla dem. Utan medveten konfigurationshantering är den kombinationen okänd och kan inte reproduceras. Du kan inte återskapa en tidigare release, spåra en defekt till ändringen som orsakade den eller med tillförsikt säga vad som körs i produktion.

Företags- och myndighetsmiljöer höjer insatserna. Reglerade och offentliga program måste visa att ändringar var auktoriserade, granskade och registrerade, att ett levererat bygge spåras tillbaka till godkända krav och källa och att inget kom in i systemet okontrollerat. Här är SCM lika mycket ett beläggssystem som ett tekniskt. [Versionshantering](https://en.wikipedia.org/wiki/Version_control) (kapitel 2.6) hanterar källkodens historik. SCM styr hela konfigurationen och den kontrollerade process genom vilken den ändras. Den hänger nära ihop med [infrastruktur som kod](https://en.wikipedia.org/wiki/Infrastructure_as_code) (kapitel 8.2), leveranspipelines (kapitel 8.1) samt revision och försäkran (kapitel 10.2).

## Nyckelprinciper

- Allt som avgör systemets beteende är ett [konfigurationsobjekt](https://en.wikipedia.org/wiki/Configuration_item) under kontroll, inte bara källkod.
- En [baslinje](https://en.wikipedia.org/wiki/Baseline_(configuration_management)) är en känd, överenskommen referenspunkt. Ändringar görs mot baslinjer medvetet, inte slarvigt.
- Förändring kontrolleras och registreras, den förhindras inte. Målet är auktoriserad, spårbar förändring.
- Statusredovisning betyder att du alltid kan svara på vad som finns i en konfiguration och vad dess ändringshistorik är.
- Revisioner verifierar att det byggda och levererade systemet stämmer med den registrerade konfigurationen och godkända krav.
- Reproducerbarhet är icke förhandlingsbar: varje släppt version måste kunna byggas om från kontrollerade indata.
- Automatisera identifiering, registrering och verifiering. Manuell bokföring skalar inte och överlever inte revision.

## Rekommendationer

### Definiera SCM-processen och tilldela ägarskap

Skriv ner en SCM-plan som anger vad som står under konfigurationskontroll, hur objekt identifieras, hur ändringar föreslås och godkänns och hur status registreras och revideras. Tilldela tydligt ägarskap, till exempel en konfigurationsansvarig eller ett ansvarigt team, så att SCM inte är allas jobb och därför ingens. Skala processen efter risken: ett litet internt verktyg behöver kontroll med lätt hand, medan ett säkerhetskritiskt eller reglerat system behöver formella nämnder och register. Förankra planen i en erkänd standard som IEEE 828 så att revisorer och partner kan följa den.

### Identifiera konfigurationsobjekt och upprätta baslinjer

Lista de konfigurationsobjekt som avgör hur systemet beter sig: källkod, beroenden, byggskript, containerbilder, infrastrukturdefinitioner, konfigurationsdata, scheman och nyckeldokument. Ge var och en en stabil identifierare och ett versionsschema. Sätt baslinjer vid meningsfulla punkter (en släppt version, en godkänd kravuppsättning, ett certifierat bygge) så att du har en överenskommen referens att ändra mot och återvända till. En baslinje är oföränderlig: när du väl förklarat den redigerar du den inte. Du ersätter den bara med en ny baslinje skapad genom ändringsprocessen.

### Kontrollera förändring genom en definierad process och lämpliga nämnder

Led ändringar av kontrollerade objekt genom en definierad väg: förslag, konsekvensanalys, godkännande, implementation och verifiering. För objekt med högre risk, använd en [ändringskontrollnämnd](https://en.wikipedia.org/wiki/Change_control_board) (CCB) som väger kostnad, risk och tidsplan innan den auktoriserar en ändring. Dimensionera nämnden rätt: en lätt automatiserad grind för rutinmässiga kodändringar och en formell tvärfunktionell CCB för ändringar som rör baslinjer, gränssnitt eller reglerat beteende. Dokumentera varje beslut och resonemanget bakom det, och koppla betydande konfigurationsbeslut till beslutsloggar (kapitel 1.6) så att resonemanget överlever.

### Upprätthåll konfigurationsstatusredovisning

För ett korrekt, sökbart register över varje konfigurationsobjekt: dess aktuella version, vilken baslinje det tillhör och vilka ändringsbegäranden som tillämpats på det. Denna statusredovisning är det som låter dig svara, när som helst, på vad en release innehåller och hur den kom dit. Generera registret automatiskt från dina register (versionshantering, pipeline, artefaktregister) i stället för att underhålla ett parallellt kalkylblad som driver från verkligheten. Registret är ryggraden i spårbarheten från krav till ändring till bygge till driftsättning.

### Genomför konfigurationsrevisioner

Verifiera två saker regelbundet. En funktionell konfigurationsrevision bekräftar att konfigurationen presterar så som dess krav specificerar. En fysisk konfigurationsrevision bekräftar att de levererade artefakterna stämmer med den registrerade konfigurationen: att bygget kom från den registrerade källan och de registrerade beroendena och inte innehåller något oredovisat. Automatisera så mycket av detta du kan: [reproducerbara byggen](https://en.wikipedia.org/wiki/Reproducible_builds), artefaktkontrollsummor, programvarumaterialförteckningar (SBOM:er) och ursprungsintyg förvandlar revision från en manuell inspektion till en kontinuerlig kontroll.

### Hantera releaser och leverans som kontrollerade händelser

Behandla en release som en specifik, identifierad baslinje levererad genom en upprepbar process. Versionera dina releaser uttryckligen, producera ett manifest eller en materialförteckning som beskriver exakt vad som ingår och registrera kopplingen från release till källrevision till driftsatt artefakt. Signera och kontrollsummera släppta artefakter så att vem som helst nedströms kan verifiera deras integritet. Knyt releasehantering till leveranspipelinen (kapitel 8.1) så att befordran genom miljöer i sig är kontrollerad, registrerad och reversibel.

### Välj och integrera SCM-verktyg

Lita på verktyg som automatiserar identifiering, kontroll, redovisning och revision snarare än att förlita dig enbart på disciplin: versionshantering för källkod, artefakt- och bildregister för binärer, en oföränderlig pipeline för byggen, infrastruktur som kod för miljöer och beroende- och SBOM-verktyg för ursprung. Koppla ihop dem så att en enda ändring flödar spårbart från commit till driftsatt release. Det du vill ha är en verktygskedja där konfigurationsregistret är en biprodukt av att göra arbetet, inte en separat kontorssyssla.

## Avvägningar: för- och nackdelar

| Val | Fördelar | Nackdelar |
|---|---|---|
| Formella ändringskontrollnämnder | Stark auktorisering och revisionsspår. Risk vägs före ändring | Lägre genomströmning. Overhead om det tillämpas på rutinändringar |
| Lätta automatiserade grindar | Snabbt flöde. Låg overhead. Skalar till många ändringar | Svagare för högriskbaslinjer. Mindre övervägande |
| Strikta oföränderliga baslinjer | Reproducerbara, granskningsbara referenspunkter | Disciplin och verktyg krävs. Friktion om det överanvänds |
| Automatiserad statusredovisning | Korrekt, alltid aktuellt register. Revisionsklart | Verktyg och integration i förväg |
| Manuella konfigurationsregister | Enkelt att börja. Inga verktyg behövs | Driver från verkligheten. Fallerar i stor skala och under revision |

Den centrala avvägningen är kontroll mot flöde. Tung ändringskontroll ger stark försäkran men bromsar leveransen. Lätt kontroll flödar snabbt men försvagar spårbarheten. Svaret är inte att välja ett globalt, utan att dela in kontrollen i nivåer efter risk: automatisera rutinändringar genom snabba grindar, och reservera formella nämnder och oföränderliga baslinjer för de objekt där auktorisering och granskningsbarhet verkligen spelar roll. Den andra avvägningen är verktygsinvestering i förväg mot löpande kontorskostnad och revisionsrisk. Automatiserad redovisning kostar mer att sätta upp och långt mindre att leva med.

## Frågor att diskutera med ditt team

1. **Vad hör exakt hemma på vår lista över konfigurationsobjekt, och vem äger beslutet när något nytt dyker upp?** SCM fungerar bara om listan över kontrollerade objekt matchar uppsättningen av det som faktiskt avgör beteende, och i ett stort system är den uppsättningen större än de flesta team tror: källkod, beroenden, byggskript, containerbilder, infrastrukturdefinitioner, scheman, funktionsflaggor och konfigurationsdata som i det tysta ändrar vad programvaran gör. Om ingen äger listan blir den inaktuell, och objektet som fällde er i produktion visar sig vara det enda ingen tänkte kontrollera. Ta med er nuvarande inventering till mötet och jaga beteendebestämmande objekt som saknas i den. Tilldela en ansvarig ägare (en konfigurationsansvarig eller ett namngivet team) så att att lägga till ett nytt objekt är ett medvetet beslut, inte en olycka, för SCM som är allas jobb är ingens jobb.

2. **Kan vi bevisa att en driftsatt artefakt kom från källan och pipelinen vi tror, och skulle beviset överleva manipulation?** Reproducerbarhet och spårbarhet är hela poängen med SCM, och den skarpa versionen av frågan är om ni kan länka den körande binären tillbaka till en specifik commit och ett byggkörning med belägg, inte påstående. I ett reglerat eller högvärdigt system är detta också ert försvar i leveranskedjan: signerade ursprungsintyg, artefaktkontrollsummor och en programvarumaterialförteckning förvandlar "vi är ganska säkra" till något en revisor eller en incidenthanterare kan verifiera. Ta med er senaste release och försök gå bakåt från den driftsatta artefakten till den godkända ändringen. Om något led är ett manuellt påstående snarare än en registrerad, verifierbar länk är det där en angripare eller ett ärligt misstag kan smyga in något obemärkt, och att stänga det betyder att koppla in signering och ursprung i pipelinen så att registret är en biprodukt av leveransen.

3. **Kan vem som helst redigera en release på plats i dag, och vad skulle det göra med vår förmåga att lita på den?** En baslinje är bara användbar om den är oföränderlig: i samma stund som "releasen" kan redigeras i efterhand kan du inte längre reproducera den eller förlita dig på den som referens, och varje efterföljande revision blir arkeologi. Det klassiska felet är konfiguration redigerad direkt i produktion eller en tagg som i det tysta flyttats, vilket är precis den genväg som känns harmlös och gör en release omöjlig att rekonstruera senare. Ta med det ärliga svaret till mötet: vem har åtkomst att ändra en driftsatt baslinje utan att gå genom ändringsprocessen, och har det hänt? Åtgärden är att göra baslinjer genuint oföränderliga och att leda varje ändring genom förslag, konsekvensanalys, godkännande och verifiering, med stringensen indelad i nivåer så att rutinändringar flödar genom snabba automatiserade grindar medan baslinje- och reglerade ändringar går till en nämnd.

4. **Genereras vår konfigurationsstatusredovisning automatiskt från våra register, eller underhålls den för hand, och hur långt har den drivit från det som faktiskt är driftsatt?** Statusredovisning är registret som låter dig svara, när som helst, på vad en release innehåller och hur den kom dit, och i ett stort system är det registret bara pålitligt om det faller ut ur arbetet snarare än att skrivas in i ett parallellt kalkylblad. Det motstridiga draget är att ett handhållet register känns billigt att börja med och flexibelt, medan att automatisera det betyder att integrera versionshantering, pipelinen och artefaktregistret så att registret blir en biprodukt av leveransen. Ta med registret ni förlitar er på i dag, välj tre nyliga releaser slumpmässigt och kontrollera om de registrerade versionerna, baslinjerna och tillämpade ändringsbegäranden matchar vad verktygen säger levererades. För ett företags- eller myndighetsprogram är ett statusregister som avviker från verkligheten inte en ordningsfråga, det är ett revisionsfynd som väntar på att hända, eftersom en revisor som fångar en lucka slutar lita på hela redogörelsen och ber er rekonstruera den för hand.

5. **Är vår ändringskontroll indelad i nivåer efter risk, eller styr samma nivå av ceremoni varje ändring oavsett vad den rör?** Kontroll och flöde drar åt olika håll: en formell ändringskontrollnämnd väger kostnad, risk och tidsplan innan den auktoriserar en ändring, men att tillämpa den ceremonin på en rutinmässig kodjustering lägger bara till fördröjning, medan att skicka en delad baslinje eller ett reglerat betalningsflöde genom en snabb automatiserad grind tar bort övervägande just där ni behöver det. Felmönstren är symmetriska, enhetlig tyngd som människor lär sig gå runt, eller enhetlig slapphet som låter en högriskändring glida igenom ogranskad. Ta med ett urval av förra kvartalets ändringar sorterade efter vad var och en rörde och kontrollera om den stringens den fick faktiskt matchade dess risk. I en reglerad eller offentlig miljö, namnge vilka objektklasser som måste nå en tvärfunktionell nämnd och vilka som får flöda genom automatiserade grindar, och dokumentera den indelningen uttryckligen, för "vi använder omdöme" är inte en kontroll en revisor eller ett tillsynsorgan kan verifiera.

6. **När körde vi senast en funktionell och en fysisk konfigurationsrevision, och hur mycket av beläggen skulle vara ett levande register snarare än en rekonstruktion?** En funktionell konfigurationsrevision bekräftar att systemet presterar så som dess krav specificerar, och en fysisk konfigurationsrevision bekräftar att de levererade artefakterna stämmer med den registrerade konfigurationen och inte innehåller något oredovisat. Hoppa över dem och ni litar på att era baslinjer och er statusredovisning är ärliga utan att någonsin kontrollera. Spänningen är kostnad: manuella revisioner är långsamma och smärtsamma, vilket är precis därför team skjuter upp dem, och vägen ut är att automatisera kontrollerna med reproducerbara byggen, artefaktkontrollsummor, programvarumaterialförteckningar och ursprungsintyg så att verifieringen blir kontinuerlig. Ta med er senaste release och försök producera, på stående fot, spåret från krav till ändring till bygge till driftsättning och beviset från artefakt till källa. För företags- och myndighetsprogram är detta beläggskedja vad certifiering och tillsyn kräver, så den ärliga frågan är om morgondagens revision skulle besvaras från register ni redan håller eller från en arkeologiövning ni inte har råd med.

## Sektorsperspektiv

**Startup.** Håll SCM lätt men verklig. Lägg källkod, infrastrukturdefinitioner och konfigurationsdata i versionshantering och gör varje release till ett taggat bygge producerat av en pipeline i stället för en handsammansatt artefakt. Hoppa över ändringskontrollnämnder och formella baslinjer, som är överkill i din storlek, men låt aldrig någon redigera konfiguration direkt i produktion, för just den genvägen är det som gör en release omöjlig att reproducera när en kund träffar på en bugg nästa tisdag.

**Småföretag.** Utan konfigurationsansvarig och med snäv budget, lita på verktyg som ger dig SCM nästan gratis: en hostad versionshanteringsplattform, dess inbyggda pipeline och ett artefaktregister, så att konfigurationsregistret är en biprodukt snarare än ett jobb du måste bemanna. Köp den här förmågan inbyggd i verktyg du redan betalar för i stället för att bygga en skräddarsydd process. Lägg din knappa uppmärksamhet på de två vanor som spelar störst roll, reproducerbara taggade releaser och att hålla beteendeförändrande konfiguration borta från manuella produktionsredigeringar.

**Storföretag.** Problemet är enhetlighet över många team: en gemensam SCM-plan, en gemensam taxonomi för konfigurationsobjekt, ändringskontroll indelad i nivåer och statusredovisning genererad automatiskt från versionshantering, artefaktregistret och pipelinen. Reservera formella ändringskontrollnämnder och oföränderliga baslinjer för delade plattforms- och reglerade flöden, låt rutinändringar flöda genom automatiserade grindar och standardisera signerat ursprung och SBOM:er så att varje teams release kan spåras och varje revisor kan fråga ett levande register i stället för att beställa en rekonstruktion.

**Offentlig sektor.** Upphandlingsregler, transparens och offentlig ansvarsskyldighet formar processen. Följ en formell SCM-plan i linje med en erkänd standard som IEEE 828, sätt baslinjer för konfigurationsobjekt vid avtalsmässiga milstolpar och led varje ändring av en kontrollerad baslinje genom en nämnd som dokumenterar konsekvens, beslut och motivering. Kräv att levererade artefakter är reproducerbara från kontrollerade indata, kontrollsummerade och spårbara från början till slut från godkänt krav till levererat bygge, eftersom det dokumenterade beläggsspåret är precis vad certifiering, revision och offentlig tillsyn kräver.

## Exempel

**Startup.** En startup med sex personer håller sin SCM lätt men verklig: källkod, infrastrukturdefinitioner och konfigurationsdata lever alla i versionshantering, och varje release är ett taggat, versionerat bygge producerat av samma pipeline i stället för sammansatt för hand. När en kund rapporterar en bugg som dök upp förra tisdagen spårar de den driftsatta artefakten tillbaka till den exakta committen på minuter i stället för att gissa. De hoppar över ändringskontrollnämnder och formella baslinjer, som skulle vara överkill i deras storlek, men de vägrar låta någon redigera konfiguration direkt i produktion, för just den genvägen är det som gör en release omöjlig att reproducera senare.

**Storföretag.** Ett stort finansiellt tjänsteföretag lägger alla driftsättningsbara artefakter, infrastrukturdefinitioner och konfigurationsdata under konfigurationskontroll. Varje release är en oföränderlig, versionerad baslinje med en genererad programvarumaterialförteckning, och varje driftsatt artefakt bär ett signerat ursprungsintyg som länkar den till en specifik källrevision och pipelinekörning. Rutinmässiga applikationsändringar flödar genom automatiserade pipelinegrindar, medan ändringar av delade plattformsbaslinjer eller reglerade betalningsflöden går till en ändringskontrollnämnd. Statusredovisning genereras automatiskt från versionshantering, artefaktregistret och pipelinen, så revisorer frågar ett levande register i stället för att be om en rekonstruktion.

**Offentlig sektor.** Ett försvarsprogram följer en formell SCM-plan i linje med IEEE 828. Konfigurationsobjekt listas och sätts som baslinjer vid avtalsmässiga milstolpar, och en ändringskontrollnämnd auktoriserar varje ändring av en kontrollerad baslinje och dokumenterar konsekvens, beslut och motivering. Funktionella konfigurationsrevisioner bekräftar att det levererade systemet uppfyller specificerade krav, och fysiska konfigurationsrevisioner bekräftar att levererade artefakter exakt stämmer med den registrerade konfigurationen. Releaser är reproducerbara från kontrollerade indata, kontrollsummerade och spårbara från början till slut, från godkänt krav via ändringsbegäran till levererat bygge, vilket är precis det beläggsspår som certifiering och tillsyn kräver.

## Affärsnytta: motiv, ROI och TCO

SCM finns för att kontrollera risk och kostnad under ett systems liv. Avkastningen kommer från reproducerbarhet och spårbarhet: du kan återskapa vilken release som helst, spåra defekter till de ändringar som orsakade dem och besvara revisionsfrågor från register i stället för arkeologi. Det krymper incidentdiagnostiden, minskar kostnaden och längden på revisioner och förhindrar den dyra klassen av fel där ingen kan säga vad som körs eller hur det ska byggas om.

Total ägandekostnad gynnar automatisering. Manuella konfigurationsregister är billiga att börja med och stadigt dyra att underhålla, och de fallerar precis när du behöver dem mest, under en incident eller en revision, eftersom de har drivit från verkligheten. Automatiserad identifiering, redovisning och revision kostar mer i förväg men förvandlar konfigurationsregistret till en nästan gratis biprodukt av leveranspipelinen. För att argumentera inför ledningen, rama in SCM som kontrollen som gör releaser reproducerbara och ändringar granskningsbara, och väg den mot kostnaden för oreproducerbara releaser, förlängda revisioner och regelefterlevnadsrisken med okontrollerad förändring.

## Antimönster och fallgropar

- **Konfiguration genom stamkunskap:** det verkliga innehållet i en release bor bara i en ingenjörs huvud, inte i något register.
- **Föränderliga baslinjer:** "releasen" redigeras på plats, så den kan inte längre reproduceras eller litas på som referens.
- **Okontrollerade konfigurationsdata:** koden är versionshanterad men konfigurationen som ändrar dess beteende redigeras ad hoc i produktion.
- **Ändringskontrollteater:** en nämnd som stämplar allt, vilket lägger till fördröjning utan att tillföra verklig granskning.
- **Manuell statusredovisning:** ett kalkylblad över versioner som i det tysta avviker från det som faktiskt är driftsatt.
- **Oreproducerbara byggen:** releaser som inte kan byggas om från kontrollerade indata, så revisioner och ombyggen blir gissningar.
- **Ospårbara releaser:** ingen koppling från driftsatt artefakt tillbaka till källrevision, ändringsbegäran och godkännande.

## Mognadsmodell

- **Nivå 1 (Initiera):** SCM är ad hoc och reaktivt. Bara källkod kontrolleras. Releaser sätts samman för hand. Det finns inga baslinjer, inget pålitligt register över vad som är driftsatt och inget sätt att reproducera ett tidigare bygge.
- **Nivå 2 (Utveckla):** Grundläggande praxis finns men varierar från team till team. Vissa system definierar konfigurationsobjekt och en ändringsprocess och versionerar sina releaser, baslinjer finns här och där, men register är delvis manuella och kontrollens stringens är inkonsekvent över organisationen.
- **Nivå 3 (Standardisera):** Praxis är dokumenterad och upprätthålls i hela organisationen. En gemensam taxonomi för konfigurationsobjekt, oföränderliga baslinjer, ändringskontroll indelad i nivåer och statusredovisning är etablerade och till stor del automatiserade. Releaser är reproducerbara och spårbara, och revisioner stöds av verktyg snarare än minne.
- **Nivå 4 (Hantera):** SCM mäts och styrs med data. Reproducerbarhetsfrekvens, spårbarhetstäckning från krav till driftsatt artefakt, ledtid för ändringar genom varje kontrollnivå, incidenter med konfigurationsdrift och revisionsfynd följs mot utgångslägen och mål. Avvikelser utlöser korrigering, och varje beslut att gå eller inte gå vidare vilar på dessa belägg snarare än på påstående.
- **Nivå 5 (Orkestrera):** SCM förbättras kontinuerligt och är integrerat i hela organisationen. Fullt automatiserat och kontinuerligt verifierat med reproducerbara byggen, SBOM:er, ursprungsintyg och levande statusredovisning är processen invävd i leverans, säkerhet och revision, och den anpassas när risk och leveransutfall förskjuts, och avvecklar och omdefinierar kontroller på grundval av belägg.

## Idéer för diskussion

- Kan ni reproducera er senaste release exakt från kontrollerade indata i dag, och hur lång tid skulle det ta?
- Vilka konfigurationsobjekt avgör beteende men är inte faktiskt under kontroll, särskilt konfigurationsdata och infrastruktur?
- Är er ändringskontroll indelad i nivåer efter risk, eller lägger den till enhetlig overhead eller enhetlig slapphet överallt?
- Var bor ert konfigurationsregister, och hur långt har det drivit från det som faktiskt är driftsatt?
- Vilka belägg kunde ni producera vid en revision i morgon, och hur mycket av det skulle vara rekonstruktion snarare än register?
- Hur förändrar reproducerbara byggen, SBOM:er och ursprung vad era revisioner kan verifiera automatiskt?

## Viktigaste punkter

- SCM kontrollerar hela konfigurationen (kod, beroenden, infrastruktur och konfigurationsdata), inte bara källkod.
- Baslinjer är oföränderliga referenspunkter. Förändring auktoriseras och registreras mot dem, den förhindras inte.
- Statusredovisning måste låta dig svara, när som helst, på vad en release innehåller och hur den kom dit.
- Revisioner verifierar att det som byggdes och levererades stämmer med den registrerade konfigurationen och godkända krav.
- Dela in kontrollen i nivåer efter risk och automatisera identifiering, redovisning och revision så att registret är en biprodukt av leveransen.

## Referenser och vidare läsning

- IEEE Computer Society, *SWEBOK Guide (Guide to the Software Engineering Body of Knowledge)*, Software Configuration Management knowledge area
- IEEE Std 828, *Standard for Configuration Management in Systems and Software Engineering*
- ISO/IEC/IEEE 12207, *Systems and software engineering: Software life cycle processes* (configuration management process)
- Jez Humble and David Farley, *Continuous Delivery*
- Bob Aiello and Leslie Sachs, *Configuration Management Best Practices: Practical Methods that Work in the Real World*
- NIST guidance on software supply chain security, software bills of materials (SBOM), and artifact provenance
- CNCF and open standards for build provenance and attestation (as reference frameworks)
