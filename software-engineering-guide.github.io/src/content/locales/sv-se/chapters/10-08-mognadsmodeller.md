# 10.8 Mognadsmodeller

## Översikt och motivation

En [mognadsmodell](https://en.wikipedia.org/wiki/Maturity_model) är ett strukturerat sätt att bedöma hur kapabel och konsekvent din praxis är inom någon domän och att beskriva en väg för att förbättra den. Den definierar en liten stege av nivåer. Längst ned är arbetet ad hoc och reaktivt. Högst upp är det mätt, hanterat och kontinuerligt optimerande. Varje steg har observerbara egenskaper ni kan kontrollera mot.

Mognadsmodeller förvandlar en vag fråga ("är vi bra på det här?") till ett upprepbart svar ("vi är på nivå 2 här, nivå 4 där, och det här är vad nivå 3 skulle kräva"). Den här boken använder en femnivåmodell i varje kapitel och samlar dem i kapitel 12.4. Det här kapitlet handlar om själva disciplinen: hur modellerna fungerar, när de hjälper och hur de vilseleder.

Skälet till att de spelar roll är enkelt. Stora organisationer kan inte förbättra det de inte kan se. Över dussintals team varierar förmågan enormt och osynligt. Vissa team har utmärkt testning och svag säkerhet. Andra har det omvända. En mognadsmodell ger er ett gemensamt ordförråd och en gemensam måttstock, så att gap blir jämförbara, investering kan prioriteras och framsteg kan följas över tid i stället för att bara påstås. Välkända exempel inkluderar CMMI ([Capability Maturity Model Integration](https://en.wikipedia.org/wiki/Capability_Maturity_Model_Integration), för process), DORA-modellen ([DevOps Research and Assessment](https://en.wikipedia.org/wiki/DevOps_Research_and_Assessment), för programvaruleveransprestation), OWASP SAMM (Software Assurance Maturity Model) och BSIMM (Building Security In Maturity Model) för programvarusäkerhet, TMMi (Test Maturity Model integration, för testning), modellen Agile Fluency och mognadsmodeller för datahantering, plus otaliga interna poängkort.

För företag och särskilt myndigheter bär mognadsmodeller särskild tyngd. Statlig upphandling har länge använt CMMI-bedömningsnivåer som leverantörskvalificering, och ramverk som amerikanska CMMC ([Cybersecurity Maturity Model Certification](https://en.wikipedia.org/wiki/Cybersecurity_Maturity_Model_Certification)) knyter cybersäkerhetsmognad direkt till behörighet för försvarsarbete. Det ger mognadsmodeller verkliga tänder. Det skapar också den centrala risken i det här kapitlet: när en nivå blir en grind eller ett mål optimerar människor för bedömningen snarare än den underliggande förmågan. Väl använda är mognadsmodeller en spegel. Dåligt använda är de teater.

## Nyckelprinciper

- **Mognad är ett medel, inte ett mål.** Målet är förmåga och utfall, inte ett nivånummer.
- **Bedöm för att lära, inte för att poängsätta.** Ärlig självbedömning slår en smickrande bedömning.
- **Högre är inte alltid bättre.** Rätt mål beror på risk, sammanhang och kostnad.
- **Mät per domän, inte ett globalt betyg.** Förmåga är ojämn. Ett enda tal döljer det.
- **Prioritera luckorna med lägst mognad och högst risk först.**
- **Se upp för [Goodharts lag](https://en.wikipedia.org/wiki/Goodhart%27s_law).** När en nivå är ett mål slutar den mäta förmåga.
- **Bedöm om periodvis.** Mognad driftar när människor, system och hot förändras.

## Rekommendationer

### Välj rätt modell för domänen

Matcha modellen mot den förmåga ni vill förbättra och föredra etablerade, belägg-baserade modeller framför påhittade där de finns:

- **Process och leverans:** CMMI (bred processmognad), DORA-förmågemodellen (leveransprestation, förankrad i forskning, kapitel 11.2).
- **Säkerhet:** OWASP SAMM och BSIMM (programvarusäkerhetspraxis), CMMC (cybersäkerhet för försvar).
- **Testning och kvalitet:** TMMi.
- **Agil och arbetssätt:** modellen Agile Fluency (kapitel 10.7).
- **Data:** mognadsmodeller för datahantering (DMM, DCAM).

För internt bruk är en enkel fyra- eller femnivåskala tillämpad per förmåga (som den här boken gör) ofta mer åtgärdbar än ett tungt externt ramverk. Reservera formella, bedömda modeller för där de är avtalsmässigt krävda.

### Bedöm ärligt och per förmåga

Kör bedömningar som producerar sanning, inte tröst. Involvera de människor som gör arbetet. Samla belägg snarare än åsikter. Poängsätt varje förmåga separat, så att bilden speglar verkligheten: stark här, svag där. En självbedömning som används för att vägleda förbättring är värd mer än en extern bedömning som används för att förtjäna ett märke, eftersom den första belönar uppriktighet och den andra belönar presentation. Kapitel 12.4 ger en samlad självbedömning över varje domän i den här boken. Använd den som ett startinstrument.

### Använd mognad för att prioritera, inte för att straffa

Resultatet av en bedömning är en prioriterad förbättringsbacklogg, inte ett betyg för att fördela skuld. Kombinera mognad med risk. En nivå 1-förmåga inom ett lågriskområde kan vara bra. En nivå 2-förmåga inom ett säkerhets- eller regelefterlevnadskritiskt område är brådskande. Rikta investering mot de luckor där låg mognad möter hög risk och koppla arbetet till utfall (kapitel 11.1) så att förbättring mäts efter resultat, inte efter att klättra uppför stegen för sin egen skull.

### Sätt målnivåer medvetet: högre är inte gratis

Varje nivå upp kostar insats och lägger ofta till processtyngd. Det rätta målet är sällan "nivå 5 överallt." Det är den nivå där den extra förmågan fortfarande motiverar den extra kostnaden för den domänens risk. Reglerade och säkerhetskritiska förmågor kan genuint behöva de översta stegen, och revision kräver ofta minst en "definierad" nivå 3. Många andra betjänas väl på nivå 3 och skulle bara ackumulera byråkrati genom att pressa längre. Avgör mål per förmåga och sluta klättra när den riskjusterade avkastningen gör det.

### Skydda mot mognadsteater

Det enda felmönster som förstör värdet av mognadsmodeller är att optimera för poängen. Se upp för bedömningar som betygsätter generöst, belägg som sätts ihop bara för bedömningen eller "nivå 5"-påståenden som produktionsincidenter motsäger. Håll bedömningen knuten till observerbart beteende och verkliga utfall. Rotera era bedömare eller sanningskontrollera dem externt. Behandla en misstänkt hög självpoäng som en lukt. I samma ögonblick nivån blir målet slutar modellen tala sanning.

## Avvägningar: för- och nackdelar

| Tillvägagångssätt | Fördelar | Nackdelar |
|---|---|---|
| **Formella bedömda modeller (CMMI, CMMC)** | Jämförbara, avtalsmässigt erkända, rigorösa | Kostsamma. Inbjuder till manipulering. Kan förstena process |
| **Lättviktiga interna poängkort** | Snabba, åtgärdbara, låg overhead | Mindre jämförbara externt. Lätta att färga |
| **Belägg-baserade förmågemodeller (DORA)** | Knutna till verkliga utfall. Forskningsbaserade | Snävare omfattning. Behöver verkliga mått |
| **Ett enda övergripande mognadsbetyg** | Enkelt att kommunicera | Döljer ojämn förmåga. Vilseleder |
| **Bedömning per förmåga** | Korrekt, åtgärdbar prioritering | Mer insats. Inget enskilt rubriktal |

Den centrala spänningen är **bedömning som spegel mot bedömning som mål**. Samma modell som hjälper ett team se sig själv klart blir kontraproduktiv i samma ögonblick en nivå knyts till belöning, behörighet eller status. Ju mer en nivå betyder, desto mer energi flödar in i skenet av mognad snarare än substansen.

## Frågor att diskutera med ditt team

1. **Bör vi hålla en uppriktig intern självbedömning skild från varje avtalsmässigt bedömd nivå, och vem äger vardera?** När en CMMC- eller CMMI-nivå grindar intäkter glider bedömningen och sanningen isär, eftersom energi flödar mot att klara snarare än att förbättra. För ett stort företag eller en myndighetsleverantör är det gapet där risken gömmer sig: ni klarar revisionen och förblir exponerade. För två böcker medvetet. Behåll den formella bedömningen för behörighet och behåll ett rakt internt poängkort ingen belönas för att blåsa upp. Namnge en ägare för vartdera och behandla varje avstånd mellan dem som en signal att undersöka, inte att släta över. Ta med nyliga incidenter, nära misslyckanden och förfall efter bedömning till mötet som belägg för vilken bok som talar sanning.

2. **För varje domän, antar vi en etablerad belägg-baserad modell eller uppfinner vi vårt eget poängkort, och är det rätt val?** Etablerade modeller (DORA för leverans, SAMM eller BSIMM för säkerhet, TMMi för testning) bär forskning och extern jämförbarhet ett hemmabygge inte kan matcha. En lättviktig intern fyranivåskala är snabbare och mer åtgärdbar och ofta det bättre valet för intern styrning. Fällan är att uppfinna ett tungt skräddarsytt ramverk som har all ceremoni från en formell modell och ingen av beläggbasen. Avgör per domän: reservera formella bedömda modeller för där ett avtal kräver dem, använd belägg-baserade modeller där de finns och passar och behåll en enkel skala per förmåga för allt annat. Ta med listan över domäner, markera vilken modell var och en använder i dag och utmana varje påhittat poängkort.

3. **Vem kör våra bedömningar, hur skulle vi fånga generös betygssättning och hur ofta bedömer vi om?** En bedömning som betygsätter sig själv smickrar sig själv, och mognad driftar när människor, system och hot förändras, så en tvåårig bedömning är ofta fiktion. Rotera bedömare eller ta in en extern sanningskontroll och behandla en misstänkt hög självpoäng som en lukt att jaga, inte en vinst att fira. Sätt en omvärderingstakt knuten till hur fort varje domän förändras: säkerhet oftare än, säg, dokumentation. Samla belägg och involvera de människor som gör arbetet snarare än att samla åsikter från chefer. Om ert svar är att ett team poängsätter sig själv en gång om året utan korskontroll mäter ni komfort, inte förmåga.

4. **Vilken målmognadsnivå behöver varje förmåga egentligen, och var skulle att pressa högre bara köpa processtyngd?** Högre är inte gratis: varje nivå upp kostar insats och lägger vanligen till ceremoni, så ett generellt mål om nivå 5 överallt dränerar en ändlig förbättringsbudget in i byråkrati som vissa domäner aldrig kommer att betala tillbaka. För en stor organisation varierar rätt mål per förmåga, eftersom ett lågriskområde som ligger på nivå 2 kan vara helt säkert medan ett säkerhets- eller regelefterlevnadskritiskt område på samma nivå är en nödsituation. Ta med en riskklassificering per förmåga, en ärlig uppskattning av vad nästa steg kostar i insats och process och varje revisions- eller avtalsgolv, eftersom många revisioner kräver minst en definierad nivå 3. I företags- och myndighetssammanhang behöver vissa reglerade förmågor genuint de översta stegen medan de flesta betjänas väl på nivå 3, så avgör mål medvetet, förmåga för förmåga, och sluta klättra när den riskjusterade avkastningen gör det.

5. **Förbättrades det utfall en höjd mognadsnivå var avsedd att skydda faktiskt förra gången vi höjde en, eller flyttade bara poängen?** En nivå som klättrar medan incidenter, ledtid eller defektfrekvens förblir platta är Goodharts lag i praktiken: när talet blir målet slutar det mäta förmåga. För ett stort team slinker detta lätt förbi, eftersom en lyckad bedömning känns som framsteg även när produktion berättar en annan historia. Knyt varje förmågas nivå till ett verkligt utfallsmått innan ni investerar och ta sedan med belägget före och efter till diskussionen: incidenter per kvartal, felfrekvens för ändringar, tid till återhämtning, vad förmågan än finns för att förbättra. I företags- och myndighetsportföljer där en bedömd nivå grindar behörighet är gapet farligt, eftersom nivån kan stiga på ihopsatta belägg medan den underliggande praxisen i tysthet förfaller, och det första beviset på det är ett intrång, ett avbrott eller en misslyckad revision.

6. **Kommunicerar vi ett rubrikbetyg för mognad eller en bild per förmåga, och knyts nivåer någonsin till belöning, rangordning eller teamets ställning?** Ett enda övergripande tal är lätt att presentera för ledningen och döljer just den ojämnhet som spelar roll, eftersom stark leverans kan maskera en nivå 1-säkerhetsförmåga. En värmekarta per förmåga är mer arbete men visar var låg mognad möter hög risk. Den svårare frågan är hur poängen används, eftersom i samma ögonblick en nivå knyts till ett teams belöning eller rangordning dör ärlig rapportering och insats flödar in i skenet av mognad snarare än substansen. Ta med värmekartan och en uppriktig redogörelse för varje ställe där en nivå för närvarande matar en prestationsbedömning, ett budgetbeslut eller ett leverantörspoängkort. För företag och myndighetsleverantörer, där bedömda nivåer kan grinda intäkter och behörighet, var uttryckliga om vilka betyg som bär konsekvenser och vilka som finns bara för att styra, eftersom en mognadsbild människor belönas för att blåsa upp slutar beskriva verkligheten.

## Sektorsperspektiv

**Startup.** En tung bedömd modell är overhead du inte har råd med på en kort livslängd. Kör en självbedömning på en timme på en enkel skala över en handfull förmågor, rätta bara den lägsta mognadslucka som blockerar något konkret (säg säkerhetsformuläret från din första företagskund) och lämna resten. Bedömningen bör kosta en eftermiddag, inte en konsult, och dess resultat är en enda nästa åtgärd snarare än en enhetligt hög poäng du varken behöver eller kan finansiera.

**Småföretag.** Utan dedikerad bedömare och med snäv budget, låna en lättviktig publik modell i stället för att beställa ett skräddarsytt ramverk: en kort leverans- eller säkerhetschecklista du kan poängsätta själv. Behandla den som ett årligt samtal om var en svag punkt skulle kosta dig en kund, inte ett stående program. Håll den billig och rak, eftersom en smickrande poäng du betalade en leverantör för att producera är värd mindre än en uppriktig du gjorde själv på en eftermiddag.

**Storföretag.** Värdet är ett gemensamt poängkort per förmåga tillämpat konsekvent över många team, så att gap blir jämförbara och förbättringsbudget flödar till där låg mognad möter hög risk. Skydda hårt mot mognadsteater när nivåer matar budget eller status: rotera bedömare eller sanningskontrollera dem externt och hantera resultaten som en värmekarta som styr investering i upptrampade stigar (kapitel 4.2) snarare än en ligatabell som rangordnar team och dödar ärlig rapportering.

**Offentlig sektor.** En mognadsnivå är här ofta en bokstavlig grind: CMMC för försvarsarbete, en CMMI-bedömning som leverantörskvalificering. Uppfyll den krävda nivån med genuin förmåga och behåll en uppriktig intern självbedömning skild från den formella bedömningen så att revisionsgolvet aldrig i tysthet blir taket. Dokumentera belägg transparent för bedömare och behandla varje avstånd mellan den certifierade nivån och verklig praxis som ansvarig risk att stänga, inte pappersarbete att arkivera.

## Exempel

**Startup.** Ett SaaS-startup på tio personer kör en självbedömning på en timme mot en enkel fyranivåskala som täcker leverans, testning, säkerhet och jour. Det finner att leverans och testning ligger på nivå 3 men säkerhet fastnat på nivå 1, vilket spelar roll eftersom det är på väg att skriva under sin första företagskund med ett säkerhetsformulär. Så grundarna lägger nästa månad på att bara höja säkerhet till en försvarbar nivå 2 och lämnar resten, snarare än att jaga en enhetligt hög poäng de varken behöver eller har råd med ännu.

**Storföretag.** Ett finansiellt tjänsteföretag bedömer sina 40 team med ett lättviktigt poängkort per förmåga (leverans, testning, säkerhet, observerbarhet, jour). Värmekartan avslöjar att säkerhetsmognaden släpar mest där den regulatoriska exponeringen är högst, så plattformsteamet finansierar säkerhetsverktyg i upptrampade stigar (kapitel 4.2) för de teamen först. Eftersom bedömningen används för att prioritera investering snarare än att rangordna team rapporterar chefer ärligt. Omvärdering ett år senare visar verklig rörelse och, avgörande, färre säkerhetsincidenter, inte bara högre poäng.

**Offentlig sektor.** En försvarsentreprenör måste nå en krävd CMMC-nivå för att få bjuda på arbete, och en systemintegratör håller en CMMI-bedömning som avtalskvalificering. Här är mognadsnivån en bokstavlig grind till intäkter. Den välskötta versionen behandlar den krävda nivån som ett golv för genuin förmåga och håller en uppriktig intern självbedömning skild från den formella bedömningen. Den dåligt skötta versionen sätter ihop belägg för bedömningen och låter verklig praxis förfalla dagen efter, klarar revisionen medan den förblir exponerad.

## Affärsnytta: motiv, ROI och TCO

Avkastningen på mognadsbedömning kommer från **riktad investering**. Förbättringsbudgetar är ändliga. Spenderade blint finansierar de det som är högljuddast. En mognadsbedömning visar var förmågan är svagast mot risk, så att samma utgift köper mer riskminskning och mer utfallsförbättring. Själva bedömningen är billig, bara dagar av strukturerad, belägg-baserad granskning, jämfört med kostnaden för felfördelade förbättringsprogram eller, värre, ett oupptäckt förmågegap som dyker upp som ett intrång, ett avbrott eller en misslyckad revision.

Vad gäller **total ägandekostnad** är disciplinen billig när ni håller den lättviktig och dyr när den hårdnar till bedömningsbyråkrati. Den dominerande dolda kostnaden är *mognadsteater*: insats som läggs på att producera skenet av mognad ger ingenting tillbaka och kan maskera verklig risk, vilket är negativ ROI. Driv ärendet inför ledningen genom att presentera mognad som en risk- och investeringslins, en värmekarta som förvandlar "förbättra allt" till "förbättra dessa tre saker först", och budgetera uttryckligen mot frestelsen att jaga nivåer för deras egen skull. Där en nivå är avtalsmässigt krävd (CMMC, CMMI) är ROI direkt: den är priset för behörighet, och målet är att uppfylla den med verklig förmåga snarare än kostsam förställning.

## Antimönster och fallgropar

- **Nivå som mål:** att jaga ett tal i stället för den förmåga det är avsett att representera.
- **Mognadsteater:** att sätta ihop belägg för en bedömning medan verklig praxis förfaller.
- **Ett globalt betyg:** ett enda mognadstal som döljer farlig ojämnhet.
- **Högre-är-alltid-bättre:** att pressa varje förmåga till nivå 5 oavsett risk eller kostnad.
- **Bedöm en gång, aldrig igen:** en engångsbedömning behandlad som permanent sanning.
- **Att rangordna team för att skylla:** att använda mognad för straff, vilket dödar ärlig rapportering.
- **Modelldyrkan:** att följa ett tungt ramverks ceremoni förbi punkten av nytta.
- **Att ignorera utfall:** att klättra uppför stegen medan leverans, tillförlitlighet eller säkerhet inte förbättras.

## Mognadsmodell

- **Nivå 1, Initiera.** Ingen gemensam föreställning om mognad. Förmåga antas, är ojämn och omätt. Varje bedömning är reaktiv, utlöst av en incident eller ett revisionskrav snarare än planerad.
- **Nivå 2, Utveckla.** Ett fåtal team kör ad hoc-bedömningar mot någon skala, men modell, takt och stringens varierar från team till team. Resultat används inkonsekvent och belägg är tunna, så poängsättning för skenet är en ständigt närvarande risk.
- **Nivå 3, Standardisera.** En enda modell per förmåga och bedömningstakt är dokumenterade och tillämpade i hela organisationen. Bedömningar är belägg-baserade, involverar de människor som gör arbetet och matar en prioriterad förbättringsbacklogg snarare än ett betyg.
- **Nivå 4, Hantera.** Mognad mäts och styrs med data: varje förmågas nivå följs mot ett utgångsläge, knyts till ett utfallsmått (incidenter, ledtid, felfrekvens för ändringar) och bedöms om med en fast takt, så att drift och generös betygssättning visar sig som tal snarare än åsikter, och mål sätts medvetet per domän mot risk och kostnad.
- **Nivå 5, Orkestrera.** Bedömning är integrerad i hela organisationen och kontinuerligt förbättrad: mognad, risk och utfall informerar investering som en adaptiv bild, mål balanseras om när hot och sammanhang skiftar, bedömare roteras eller kontrolleras externt som en självklarhet och praxisen avvecklar aktivt ceremoni som inte längre förtjänar sin kostnad.

## Idéer för diskussion

1. Vilka av era förmågor antar ni är mogna utan belägg?
2. Var sammanfaller er lägsta mognad med er högsta risk, och är det dit er förbättringsbudget går?
3. Är någon mognadsnivå i er organisation ett mål eller en grind? Vilket beteende har det producerat?
4. Vad är rätt målnivå för varje förmåga, och var skulle att klättra längre bara lägga till byråkrati?
5. Skulle era team rapportera sin mognad ärligt, eller straffar sättet ni använder poäng uppriktighet?
6. När ni senast "förbättrade mognaden", ändrades utfallen faktiskt?

## Viktigaste punkter

- En mognadsmodell bedömer förmåga mot en stege av nivåer och beskriver en väg att förbättra: en spegel, inte en trofé.
- Välj etablerade, belägg-baserade modeller per domän (CMMI, DORA, SAMM/BSIMM, CMMC). En lättviktig skala per förmåga är ofta mest åtgärdbar.
- **Bedöm ärligt, per förmåga**, och använd resultaten för att **prioritera efter risk**, inte för att rangordna eller skylla.
- **Högre är inte alltid bättre:** sätt målnivåer medvetet mot risk och kostnad.
- Se upp för **mognadsteater** och **Goodharts lag**: en nivå som blir ett mål slutar mäta förmåga.
- Se kapitel 12.4 för den här bokens samlade självbedömning av mognad och varje kapitels egen mognadssektion.

## Referenser och vidare läsning

- CMMI Institute / ISACA, *Capability Maturity Model Integration (CMMI)*.
- Watts Humphrey, *Managing the Software Process* (origins of software process maturity).
- Nicole Forsgren, Jez Humble, Gene Kim, *Accelerate* (capability, not maturity-level, thinking for delivery).
- OWASP, *Software Assurance Maturity Model (SAMM)*; BSIMM (*Building Security In Maturity Model*).
- U.S. Department of Defence, *Cybersecurity Maturity Model Certification (CMMC)*.
- TMMi Foundation, *Test Maturity Model integration*.
- James Shore and Diana Larsen, *The Agile Fluency Model*.
- Martin Fowler, "Maturity Model" (bliki), on their uses and abuses.
