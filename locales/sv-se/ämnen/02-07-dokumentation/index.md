# 2.7 Dokumentation

## Översikt och motivation

[Dokumentation](https://en.wikipedia.org/wiki/Software_documentation) är den skrivna kunskap som låter människor använda, driva och ändra programvara utan att behöva pussla ihop förståelse enbart ur koden. Den finns i många genrer: hur man kommer igång, hur man utför en uppgift, hur ett system är uppbyggt, hur man svarar på en incident, vad ett [API](https://en.wikipedia.org/wiki/API) tar emot och returnerar. Var och en tjänar en annan läsare med ett annat behov. God dokumentation är inte valfri. Den är skillnaden mellan kunskap som skalar över en stor organisation och kunskap som bor i bara några få människors huvuden.

För stora team är dokumentation ditt bästa försvar mot nyckelpersonsrisk (faran när kritisk kunskap ligger hos bara en eller några få) och ditt snabbaste sätt att introducera nykomlingar. När hundratals ingenjörer är beroende av system de inte byggt, och människor kommer, flyttar och går hela tiden, kan organisationen bara fungera om kunskap skrivs ner och är lätt att hitta. Odokumenterade system blir sköra: bara deras författare kan ändra dem säkert, och när de författarna slutar förlorar organisationen förmågan att underhålla sin egen programvara. Det är ett av de vanligaste och dyraste misslyckandena i stor skala.

Företags- och myndighetssammanhang höjer insatserna ytterligare. System lever länge, så din dokumentation måste tjäna underhållare år, till och med decennier, efter att det ursprungliga teamet är borta. Regler och revisionsregimer föreskriver ofta särskilda dokument som belägg för kontroll: arkitekturposter, [körböcker](https://en.wikipedia.org/wiki/Runbook) (steg-för-steg-procedurer för drift och incidenthantering) och beslutsloggar. Offentliga system som lämnas över mellan leverantörer förlitar sig helt på dokumentation för att bära kunskap över avtalsgränser. Och ändå är dokumentation ökänt benägen att ruttna, så den verkliga utmaningen är att hålla den korrekt när programvaran förändras.

## Nyckelprinciper

- Skriv för en specifik läsare med ett specifikt behov. Olika dokumentationstyper tjänar olika syften.
- Håll dokumentationen nära koden och behandla den som kod (dokument som kod).
- Korrekthet slår fullständighet. En liten mängd pålitlig dokumentation slår en stor mängd som är fel.
- Generera det som kan genereras. Underhåll inte för hand det ett verktyg kan producera från sanningskällan.
- Bekämpa dokumentationsröta aktivt. Inaktuella dokument är värre än inga eftersom de vilseleder.
- Gör dokumentationen sökbar. Kunskap som inte går att hitta är i praktiken frånvarande.
- Dokumentera beslut och deras motivering, inte bara nuläget.

## Rekommendationer

### Anta dokument som kod

Håll dokumentationen i [versionshantering](https://en.wikipedia.org/wiki/Version_control) precis bredvid koden den beskriver, skriv den i rentextmarkup och granska den genom samma pull request-process. Det håller den versionshanterad, granskningsbar och nära koden, så att du kan uppdatera båda tillsammans. Publicera den genom en automatiserad pipeline så att den senaste versionen alltid är tillgänglig. Att behandla dokument som kod ger samma disciplin som håller kod pålitlig: granskning, historik och automatisering.

### Strukturera innehållet med ramverket Diátaxis

Organisera dokumentationen i fyra skilda typer, eftersom att blanda dem inte tjänar någon läsare väl: handledningar (inlärningsorienterade, för nykomlingar), instruktioner (uppgiftsorienterade, för ett specifikt mål), referens (informationsorienterad, exakt och fullständig) och förklaring (förståelseorienterad, varför och sammanhanget). Håll dessa åtskilda så blir allt lättare att skriva, navigera och underhålla, eftersom varje sida har ett tydligt jobb och en tydlig målgrupp.

### Underhåll de väsentliga driftdokumenten

Ge varje repositorie en tydlig [README](https://en.wikipedia.org/wiki/README) som sin ingång: vad det är, hur man bygger och kör det och vart man går härnäst. Skriv körböcker för driftuppgifter och incidenthantering, så att vem som helst som har jour kan agera, inte bara experterna. Håll arkitekturdokumentation som förklarar systemets struktur och nyckelkomponenter. Och tillhandahåll introduktionsdokumentation som får en ny ingenjör produktiv snabbt. Det är de dokument du saknar mest när de inte finns.

### Generera API-dokumentation och ändringsloggar från sanningskällan

Generera din API-referensdokumentation från det maskinläsbara kontraktet eller kodannoteringar, så att den inte kan driva ifrån det faktiska gränssnittet. För en [ändringslogg](https://en.wikipedia.org/wiki/Changelog), helst genererad från strukturerade commits eller releaseanteckningar, så att konsumenter kan se vad som ändrades mellan versioner. Att automatisera dessa tar den mest röttäta handunderhållna dokumentationen av ditt bord och håller den pålitlig.

### Dokumentera arkitekturbeslut

Fånga betydande arkitektur- och designbeslut som lätta, daterade poster som anger sammanhanget, beslutet och dess konsekvenser. Dessa beslutsposter bevarar den motivering som annars skulle gå förlorad, så att framtida underhållare kan se varför systemet är som det är i stället för att ifrågasätta det eller upprepa gamla misstag. De betalar sig särskilt över de långa livslängderna hos företags- och myndighetssystem.

### Bekämpa dokumentationsröta medvetet

Behandla inaktuell dokumentation som en defekt. Uppdatera dokumenten som en del av samma ändring som ändrar beteendet, och gör det till en granskningsförväntan. Tilldela ägarskap så att varje viktigt dokument har någon ansvarig. Granska högvärdig dokumentation för korrekthet då och då, rensa bort det som är föråldrat och ta bort eller flagga tydligt allt du inte längre litar på. Den dokumentation som ruttnar minst är levande dokumentation: genererad eller testad mot systemet självt.

### Investera i kunskapshantering och sökbarhet

Gör dokumentationen sökbar genom bra sökning, tydlig navigering och ett känt hem, så att människor kan hitta det de behöver utan att behöva fråga någon. Låt den inte fragmenteras över för många osammanhängande wikis och verktyg. Och fånga [tyst kunskap](https://en.wikipedia.org/wiki/Tacit_knowledge), den informella förståelse som bor i chattrådar och människors huvuden, i varaktig, sökbar form innan den glider iväg.

## Avvägningar: för- och nackdelar

| Tillvägagångssätt | Fördelar | Nackdelar |
|---|---|---|
| Dokument som kod | Versionshanterat, granskningsbart, nära koden. Låg röta | Kräver ingenjörsdisciplin. Mindre vänligt för icke-tekniska författare |
| Wiki / kunskapsbas | Lätt att redigera. Tillgänglig för alla | Driver från koden. Fragmenteras. Ruttnar tyst |
| Genererad dokumentation (API, ändringslogg) | Alltid korrekt. Lågt underhåll | Begränsad till vad källan uttrycker. Behöver verktyg |
| Handskriven förklaring | Rikt sammanhang och motivering som maskiner inte kan producera | Arbetskrävande. Benägen att bli inaktuell |
| Diátaxis-struktur | Tydligt syfte per sida. Lättare att navigera och underhålla | Strukturering i förväg. Kräver författardisciplin |

Den centrala avvägningen är insats mot korrekthet och beständighet. Den billigaste dokumentationen att skriva, en snabb wikisida, är också den mest benägna till röta och fragmentering. Den mest beständiga dokumentationen, genererad från källan eller granskad som kod, kostar mer disciplin i förväg men förblir pålitlig. En bra tumregel: generera det du kan, håll resten nära koden och granskad som kod och spara arbetskrävande handskriven förklaring för den motivering bara människor kan ge.

## Frågor att diskutera med ditt team

1. **Är era dokument åtskilda efter läsarens behov, eller trasslar handledningar, referens och förklaring ihop sig på en sida?** Det här kapitlet rekommenderar Diátaxis-uppdelningen i handledningar, instruktioner, referens och förklaring, och listar att blanda typer som ett antimönster som inte tjänar någon läsare väl. I stor skala behöver en nykomling som lär sig systemet och en ingenjör med jour som jagar ett exakt faktum olika sidor, och en enda blandad sida bromsar båda. Ta med signalen: välj era mest besökta dokument och kontrollera om var och en har ett tydligt jobb och en tydlig målgrupp. Strukturera om de värsta fallen till skilda typer, så att varje sida blir lättare att skriva, navigera och hålla aktuell. Den strukturen är det som gör dokumentation underhållbar när organisationen växer.

2. **Fångar ni betydande arkitekturbeslut med deras motivering, eller bara nuläget?** Kapitlet rekommenderar lätta, daterade beslutsposter som anger sammanhang, beslut och konsekvenser, och noterar att de betalar sig mest över de långa livslängderna hos företags- och myndighetssystem. Utan dem kan en underhållare år senare inte se varför systemet är som det är, så hen ifrågasätter sunda val eller upprepar gamla misstag. Ta med ett nyligt svårt beslut vars resonemang nu bara bor i en chattråd eller någons minne som den konkreta signalen. Anta ett kort beslutspostformat och gör skrivandet av en till en del av varje betydande designändring. Motiveringen är precis den kunskap bara människor kan ge och som ruttnar snabbast när den är oskriven.

3. **Kan vilken ingenjör som helst med jour svara på en incident enbart utifrån era körböcker, utan att behöva söka personen som byggde systemet?** Det här kapitlet namnger körböcker som ett väsentligt driftdokument så att vem som helst med jour kan agera, inte bara experterna, och beskriver ett myndighetsteam som bara kunde ärva ett system för att körböcker bar kunskapen över en avtalsgräns. Nyckelpersonsrisk är felet detta skyddar mot: när den enda experten är onåbar eller borta förvandlar en odokumenterad återställningsprocedur en rutinincident till ett avbrott. Ta med beläggen: ta en nylig incident och kontrollera om körboken ensam skulle ha löst den. Skriv och testa körböcker för de procedurer människor fruktar, och behandla en körbok som inte kan stå på egna ben som en defekt. Det är skillnaden mellan en återställning klockan två på natten och en eskalering klockan två på natten.

4. **Vilka av era API-referenser och ändringsloggar genereras från sanningskällan, och vilka underhålls fortfarande för hand och driver i det tysta?** Det här kapitlet säger åt dig att generera referensdokumentation från det maskinläsbara kontraktet eller kodannoteringar så att den inte kan avvika från det faktiska gränssnittet, och det listar handunderhåll av genererbart innehåll som ett antimönster. För ett stort team är en handskriven API-dokumentation som släpar efter det verkliga gränssnittet värre än ingen: varje konsument som litar på den skriver en trasig integration, och felet dyker upp långt från den inaktuella sidan som orsakade det. Ta med den konkreta signalen: ta stickprov av en handfull av era mest använda gränssnitt och jämför den publicerade referensen mot det verkliga kontraktet för att se hur långt var och en har drivit. Där ni hittar drift, koppla in referensen i bygget så att den regenereras vid varje ändring, och avveckla den handhållna kopian. I företags- och myndighetsmiljöer, där gränssnitt konsumeras över team, leverantörer och avtalsgränser ni aldrig ser, är en auktoritativ genererad referens ofta det enda som hindrar integratörer från att bygga mot fiktion.

5. **Vem äger varje högvärdigt dokument, och hur skulle ni märka i dag om ett hade blivit inaktuellt?** Kapitlet behandlar inaktuell dokumentation som en defekt och varnar för att ägarlösa dokument ruttnar eftersom att uppdatera dem är ingens jobb, medan inaktuella dokument presenterade som aktuella förstör förtroendet för all er dokumentation. I stor skala är faran inte en enda felaktig sida utan den långsamma urholkningen av tilltro: när läsare väl bränts av föråldrade instruktioner slutar de lita på hela korpusen och går tillbaka till att avbryta människor. Ta med en ägarkarta över era mest kritiska dokument och ett ärligt svar på hur röta upptäcks, genom granskningstakt, generering, tester mot systemet eller ren tur. Tilldela en namngiven ägare till varje dokument som spelar roll, och föredra levande dokumentation som är genererad eller testad så att inaktualitet visar sig mekaniskt snarare än genom en generad läsare. För företags- och myndighetssystem som överlever sina ursprungliga team är ägarlös dokumentation en skuld som en revisor eller en ärvande leverantör så småningom kommer att debitera er för.

6. **Hur sökbar är er dokumentation, och hur mycket kritisk kunskap bor fortfarande bara i chattrådar och människors huvuden?** Det här kapitlet säger att kunskap som inte går att hitta i praktiken är frånvarande, varnar för att fragmentera dokumentation över för många osammanhängande wikis och verktyg och uppmanar er att fånga tyst kunskap i varaktig, sökbar form innan den glider iväg. I en stor organisation återupptäcks, återfrågas och återbesvaras samma faktum ofta hundra gånger eftersom ingen kan hitta var det redan skrevs, och varje avgång tar oersättligt sammanhang med sig ut genom dörren. Ta med beläggen: räkna hur många separata dokumentationshem ni underhåller, försök hitta tre viktiga fakta enbart genom sökning och notera var de verkliga svaren visade sig bo i någons minne eller ett begravt meddelande. Konsolidera mot ett känt hem med verklig sökning och tydlig navigering, och gör att fånga tyst kunskap till en rutinmässig del av arbetet snarare än en heroisk räddning. I offentliga och starkt utlagda sammanhang, där system går mellan leverantörer och team genom avtal, är sökbar skriven kunskap det enda som överlever överlämningen.

## Sektorsperspektiv

**Startup.** Med en handfull ingenjörer och ingen löptid att undvara, dokumentera bara det ett avbrott klockan två på natten eller en nyanställd faktiskt skulle behöva: en riktig README per tjänst, en testad körbok för driftsättnings- och återställningsproceduren alla fruktar och några daterade anteckningar om de beslut du annars skulle glömma. Generera API-dokumentation från kontraktet så att du aldrig handunderhåller den. Stå emot att bygga en dokumentationsplattform. En versionshanterad mapp med markup bredvid koden räcker tills du känner verklig smärta.

**Småföretag.** Utan teknisk skribent och med snäv budget, lita på den dokumentation dina verktyg redan genererar och på lätta dokument som kod snarare än ett bemannat program. Rama in valet som köp mot bygg: föredra plattformar som producerar sin egen aktuella referens och sökbara kunskapsbas framför en wiki du måste sköta för hand. Lägg din knappa insats på de två eller tre dokument vars frånvaro skulle stoppa verksamheten, och låt en felaktig eller saknad sida vara utlösaren att åtgärda ägarskapet.

**Storföretag.** Över många team är problemet enhetlighet och sökbarhet: en gemensam pipeline för dokument som kod, en gemensam struktur som Diátaxis, genererade API-referenser och ändringsloggar och beslutsposter tillämpade på samma sätt överallt så att kunskap inte fragmenteras över dussintals wikis. Tilldela ägarskap för varje högvärdigt dokument och mät korrekthet, inte bara närvaro. Behandla arkitekturposter, körböcker och beslutsloggar som revisionsbelägg och standardisera hur de produceras så att en kontrollgranskning hittar ett dokumenterat, försvarbart spår snarare än en räddningsaktion.

**Offentlig sektor.** Upphandlingsregler och offentlig ansvarsskyldighet gör dokumentation till en leverabel, inte en artighet. Skriv in arkitekturdokumentation, körböcker och beslutsposter i avtal som föreskrivna artefakter, granskade för korrekthet så att kunskap överlever ett leverantörsbyte och ett system kan drivas av vem som än ärver det. Kräv att varje behörig operatör kan svara på en incident enbart utifrån körboken, och behåll beslutsloggar som ett transparent offentligt register över varför val gjordes. Tunn dokumentation här är inte en privat olägenhet. Den blir kostsam baklängeskonstruktion finansierad av skattebetalarna.

## Exempel

**Startup.** En startup med fem personer skriver en riktig README för varje tjänst och en kort körbok för den enda driftsättnings- och återställningsprocedur alla fruktar, så att ett avbrott klockan två på natten inte beror på att väcka den ende grundare som kan systemet. De genererar API-dokumentation från kontraktet i stället för att handskriva den, och noterar några daterade anteckningar som förklarar varför de valde sin databas och sitt autentiseringsupplägg. Det förblir lätt, men det betyder att den sjätte och sjunde anställda introduceras från dokument snarare än genom att avbryta alla.

**Storföretag.** Ett stort programvaruföretag håller all sin dokumentation i samma repositorier som sin kod, skriven i markup och granskad i pull requests precis bredvid ändringarna de beskriver. API-referenser genereras från tjänstekontrakt, så de driver aldrig. Ändringsloggar genereras från strukturerade commits, och arkitekturbeslutsposter bevarar resonemanget bakom stora val. En publicerad dokumentationssajt byggs automatiskt vid varje sammanslagning. Nya ingenjörer blir produktiva snabbt eftersom introduktionsguider och körböcker är aktuella och sökbara, och ingenjörer med jour lutar sig mot körböcker i stället för att söka de ursprungliga författarna.

**Offentlig sektor.** En nationell myndighet ärver ett system från en avgående konsult och är helt beroende av dokumentation för att bära kunskap över avtalsgränsen. Eftersom den tidigare leverantören underhöll arkitekturdokumentation, körböcker och beslutsposter som föreskrivna leverabler kan det nya teamet driva och ändra systemet utan de ursprungliga författarna. Där dokumentationen var tunn står myndigheten inför kostsam baklängeskonstruktion. Den erfarenheten driver en ny policy: dokumentation är en avtalad leverabel, granskad för korrekthet snarare än behandlad som en eftertanke, och körböcker måste låta varje behörig operatör svara på incidenter.

## Affärsnytta: motiv, ROI och TCO

Dokumentation betalar sig tillbaka i kortare introduktionstid, mindre nyckelpersonsrisk, snabbare incidentsvar och lägre kostnad för förändring under ett systems liv. Nya ingenjörer som blir produktiva på dagar snarare än veckor, jourpersonal som löser incidenter från en körbok i stället för att eskalera, underhållare som tryggt ändrar ett system år efter att det byggdes: det är stora, återkommande besparingar som växer över en stor organisation och en lång systemlivslängd.

Vad kostar dokumentation? Författande- och underhållsinsats. Vad kostar det att *inte* dokumentera? Du betalar kontinuerligt: i långsam introduktion, upprepade frågor, flaskhalsar kring nyckelpersoner, långsammare incidentåterhämtning och, i det yttersta fallet, system ingen säkert kan ändra, vilket tvingar fram dyra omskrivningar eller baklängeskonstruktion. I leverantörsövergångar och revisionsscenarier kan saknad dokumentation bära direkta avtals- och regelefterlevnadskostnader. För att argumentera inför ledningen, sätt tal på introduktionstid, incidentsvarstid och hur mycket kritisk kunskap som sitter i enskilda huvuden. Rama sedan in dokument som kod och generering som sätt att få varaktig dokumentation utan en motsvarande underhållsbörda. Och betona att felaktig dokumentation är en skuld, så investeringen måste inkludera att hålla den aktuell.

## Antimönster och fallgropar

- **Inaktuell dokumentation presenterad som aktuell:** vilseleder läsare och förstör förtroendet för all dokumentation.
- **Skriv-en-gång-wikin:** sidor som skapas och aldrig uppdateras och i det tysta driver från verkligheten.
- **Dokumentationsfragmentering:** kunskap utspridd över många verktyg och wikis så att inget går att hitta.
- **Att blanda dokumentationstyper:** handledningar, referens och förklaring trasslade på en sida, vilket inte tjänar någon läsare väl.
- **Handunderhåll av genererbart innehåll:** manuellt skriven API-dokumentation som oundvikligen avviker från det faktiska gränssnittet.
- **Tyst kunskap som tribal:** kritisk förståelse som bara finns i människors huvuden och chatthistorik och går förlorad när de slutar.
- **Dokumentation som eftertanke:** skriven i slutet, om alls, snarare än vid sidan av ändringen.
- **Inget ägarskap:** dokument utan ansvarig ägare ruttnar eftersom att uppdatera dem är ingens jobb.

## Mognadsmodell

- **Nivå 1, Initiera.** Dokumentationen är gles, utspridd och inaktuell, och kunskap bor i människors huvuden. Det som finns skrevs en gång och rördes aldrig mer, så ett avbrott eller en avgång betyder baklängeskonstruktion av systemet.
- **Nivå 2, Utveckla.** Nyckeldokument finns, som READMEs och några körböcker, men de underhålls inkonsekvent och är svåra att hitta. Vissa team dokumenterar väl och andra knappt alls, och det finns ingen gemensam förväntan på vad ett repositorie ska bära eller var det ska bo.
- **Nivå 3, Standardisera.** Dokument som kod är normen i hela organisationen: en gemensam struktur som Diátaxis, genererade API-referenser och ändringsloggar, beslutsposter och en förväntan i granskning att dokument ändras med den kod de beskriver. Varje högvärdigt dokument har en namngiven ägare, och det finns ett känt hem med verklig sökning.
- **Nivå 4, Hantera.** Dokumentation mäts, inte bara finns. Du följer täckning av de väsentliga dokumenten, dokumentändringsfrekvens mot kodändringsfrekvens, introduktionstid, incidentlösning enbart från körböcker och aktualitet mot en definierad inaktualitetströskel, och du granskar måtten mot utgångslägen. Röta fångas mekaniskt genom generering, tester mot systemet samt länk- och korrekthetskontroller, och inaktuella sidor flaggas eller rensas på grundval av belägg snarare än slump.
- **Nivå 5, Orkestrera.** Dokumentation förbättras kontinuerligt och är integrerad i hela organisationen: levande, till stor del genererad eller testad mot systemet, ägd, sökbar och adaptiv. Måtten matar tillbaka till var du investerar, tyst kunskap fångas som en rutinmässig del av arbetet och korpusen omfördelas och rensas aktivt när system, team och läsare förändras.

## Idéer för diskussion

- Vilken dokumentation skulle, om den försvann i morgon, skada er organisation mest, och finns den för närvarande och hålls aktuell?
- Hur gör ni det naturligt att uppdatera dokumentation som en del av att ändra kod snarare än en separat syssla?
- Var kan ni ersätta handskriven dokumentation med genererad dokumentation knuten till sanningskällan?
- Hur mäter ni om er dokumentation är korrekt och använd, inte bara finns?
- Hur bör AI-assistenter förändra hur ni skriver, underhåller och söker i dokumentation, och var kan de introducera trovärdigt men felaktigt innehåll?
- Hur fångar ni tyst kunskap innan de människor som bär den slutar?

## Viktigaste punkter

- Behandla dokumentation som kod: versionshanterad, granskad, nära källan och publicerad automatiskt.
- Strukturera innehållet efter läsarens behov med handledningar, instruktioner, referens och förklaring.
- Underhåll de högvärdiga väsentligheterna: READMEs, körböcker, arkitekturdokument, introduktion och beslutsposter.
- Generera API-dokumentation och ändringsloggar så att de inte kan driva från sanningskällan.
- Bekämpa röta med ägarskap, granskningsförväntningar och rensning. Felaktig dokumentation är värre än ingen.

## Referenser och vidare läsning

- Daniele Procida, *Diátaxis* documentation framework
- Andrew Etter, *Modern Technical Writing*
- Anne Gentle, *Docs Like Code*
- Google, *Developer Documentation Style Guide* and Season of Docs guidance (as reference exemplars)
- Michael Nygard, *Documenting Architecture Decisions* (architecture decision records)
- Andrew Hunt and David Thomas, *The Pragmatic Programmer* (on knowledge and documentation)
- *Keep a Changelog* (as a reference convention)
