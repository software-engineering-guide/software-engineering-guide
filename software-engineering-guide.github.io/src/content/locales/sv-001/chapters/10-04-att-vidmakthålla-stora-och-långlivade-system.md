# 10.4 Att vidmakthålla stora och långlivade system

## Översikt och motivation

Det mesta som skrivs om programvaruteknik handlar om att bygga nya saker. Men det mesta av världens viktiga programvara är gammal, stor och fortfarande i drift: skattesystem, bidragsutbetalningar, flygledning, kärnbanksystem, industriell styrning och vardagslivets infrastruktur. Dessa system körs rutinmässigt i tio, tjugo eller trettio år. Det är långt längre än anställningstiden hos någon som byggde dem, och ofta längre än de företag och språk som producerade dem. Att vidmakthålla sådana system betyder att hålla dem tillförlitliga, säkra, förstådda och förmögna att förändras, över årtionden och över generationer av personal. Det är en av de svåraste och minst glamorösa disciplinerna på fältet, och en där stora företag och myndigheter bär den tyngsta bördan.

Varför spelar detta större roll för stora organisationer? Kontinuitet i skyldighet. Ett startup kan skriva om eller överge sin programvara. En nationell regering kan inte sluta betala pensioner medan den refaktoriserar. Företag och myndigheter äger system vars fel har konsekvenser mätta i försörjning, säkerhet eller offentligt förtroende. Och de äger många av dem samtidigt, bemannade av människor som kommer och går över årtionden. De centrala hoten är inte exotiska. De är den långsamma urholkningen av de människor som förstår systemet ([bussfaktor](https://en.wikipedia.org/wiki/Bus_factor), hur få personer som skulle behöva lämna innan kunskapen om ett system går förlorad), uppstaplingen av odokumenterad kunskap i några få huvuden, förfallet hos teknikstacken mot [livscykelslut](https://en.wikipedia.org/wiki/End-of-life_(product)) och den förlamning som sätter in när ett system blir för kritiskt att röra och för dåligt förstått för att ändra säkert.

Det här kapitlet handlar om förvaltarskap: det medvetna, oglamorösa arbetet att hjälpa ett system överleva sina upphovsmän med värdighet. Det behandlar kontinuitet i ägarskap och mildrande av bussfaktorn, planerad [avveckling](https://en.wikipedia.org/wiki/Deprecation) och nedläggning, kunskapsöverföring, de egendomliga utmaningarna med årtiondelånga system och den ständiga balansakten mellan att förnya och att bevara den stabilitet medborgare och kunder beror på.

## Nyckelprinciper

- **Varje kritiskt system behöver alltid en ägare.** Ägarskap är en kontinuerlig tilldelning, inte ett minne av vem som skrev det.
- **Kunskap som bor i ett huvud är en risk, inte en tillgång.** Institutionalisera förståelse innan personen lämnar.
- **Tråkigt är en funktion.** För långlivade kritiska system slår stabilitet och förutsägbarhet ofta nyhet.
- **Planera slutet i början.** Varje system kommer att avvecklas eller ersättas. Designa och dokumentera för den dagen.
- **Förändring är hur man förblir säker.** Ett system för skrämmande att röra fallerar redan. Förmågan att förändra är en överlevnadsegenskap.
- **Kontinuitet överlever individer.** Designa team, dokumentation och processer så att ingen enskild avgång är en kris.
- **Förtroende är den verkliga produkten.** För medborgar- och kundvända system är tillförlitlighet och rättvisa upprätthållna över tid uppdraget.

## Rekommendationer

### Etablera förvaltarskap och kontinuitet i ägarskap

Tilldela uttryckligt, aktuellt ägarskap för varje system som spelar roll. Äg på teamnivå, inte individnivå, så att ägarskapet överlever avgångar. Underhåll en [tjänstekatalog](https://en.wikipedia.org/wiki/Service_catalog) som för varje system registrerar vem som äger det, vad det gör, vad det beror på och hur kritiskt det är. Granska ägarskap regelbundet och låt aldrig ett system bli föräldralöst. Ett ägarlöst kritiskt system är en nödsituation som väntar på att hända. När team omorganiseras, överför ägarskap medvetet, med en överlämning, inte genom antagande. För de mest kritiska långlivade systemen, se till att ägarskapet inkluderar inte bara drift utan förmågan att förstå och förändra systemet, så att förvaltarskap inte förfaller till ren barnpassning.

### Mildra bussfaktor och nyckelpersonsrisk

Mät och minska aktivt koncentrationen av kunskap. Om bara en person kan driftsätta, felsöka eller ändra ett system är det en [enskild felpunkt](https://en.wikipedia.org/wiki/Single_point_of_failure) lika verklig som vilken hårdvara som helst. Minska den genom parprogrammering och rotation, obligatorisk kodgranskning, delad jour och en medveten regel att ingen kritisk uppgift har exakt en kapabel person. Korsutbilda så att minst två (helst tre) personer kan utföra varje väsentlig funktion. Behandla avgången av en nyckelperson som en förutsebar händelse ni förbereder er för kontinuerligt, inte en chock ni absorberar. Dokumentation hjälper. Men arbetskunskap spridd över ett team genom faktisk praxis är långt mer varaktig än dokument ingen har övat.

### Institutionalisera kunskapsöverföring

Fånga den kunskap som annars skulle lämna med människor. Fokusera först på den kunskap som är svår att rekonstruera: varför beslut fattades, vilka alternativ som förkastades och varför, var de vassa kanterna och de kritiska knepen som resten av systemet i tysthet beror på finns och hur systemet beter sig under stress. Använd arkitekturbeslutsloggar för att bevara resonemanget bakom valen, inte bara valen. Håll [körböcker](https://en.wikipedia.org/wiki/Runbook) och driftdokumentation nära systemet och öva dem regelbundet så att de förblir sanna. Bygg introduktionsvägar som får nya förvaltare till genuin kompetens. Behandla avgångar som kunskapsöverföringshändelser med verklig överlämningstid. Kom ihåg att [tyst kunskap](https://en.wikipedia.org/wiki/Tacit_knowledge), känslan för ett system, överförs främst genom att göra tillsammans med någon som har den, så överlappa avgående och anländande förvaltare där ni kan.

### Hantera avveckling, nedläggning och livscykelslut

Planera slut medvetet. När ni beslutar att avveckla eller ersätta ett system, behandla nedläggningen som ett projekt i sig: identifiera varje konsument och beroende, tillhandahåll en migreringsväg och en realistisk tidslinje, kommunicera tydligt och upprepade gånger och stöd konsumenter genom övergången. Undvik fällan att köra det gamla och nya systemet parallellt för evigt för att ingen vill göra det svåra arbetet att stänga av det gamla. Tilldela uttrycklig ansvarsskyldighet för att slutföra avvecklingen. Bevara data, register och förmågan att besvara frågor om det avvecklade systemet långt efter att det slutar köras, särskilt där rättsliga lagringsregler gäller. En nedläggning gjord dåligt lämnar zombiesystem som är ounderhållna men fortfarande förlitas på: det värsta av alla världar.

### Vidmakthåll system över årtionden

För system som måste köras i tjugo eller trettio år, planera för att överleva allt: det ursprungliga teamet, leverantörerna, språkekosystemet och hårdvaran. Föredra [öppna standarder](https://en.wikipedia.org/wiki/Open_standard) och dokumenterade gränssnitt framför proprietära svarta lådor, så att framtida underhållare har en chans. Modularisera, så att delar kan ersättas en i taget snarare än genom en allt-eller-inget-[omskrivning](https://en.wikipedia.org/wiki/Rewrite_(programming)) som är för riskfylld att någonsin försöka. Håll systemet kontinuerligt underhållet. Ett system hållet aktuellt i små steg förblir hållbart. Ett system fruset "för att det fungerar" blir i tysthet ounderhållbart när dess stack åldras ur stöd. Behåll också kompetensen att driva det: för genuint gammal teknik, utbilda efterträdare medvetet snarare än att hoppas att den sista experten aldrig går i pension.

### Balansera förnyelse med stabilitet och förtroende

Skilj de delar av er egendom där nyhet skapar värde från de delar där stabilitet är värdet. Kärnsystem som medborgare och kunder beror på dagligen belönar vanligen tillförlitlighet, bakåtkompatibilitet och försiktig förändring framför spännande omskrivningar. Investera innovation i kanterna (nya kanaler, nya funktioner, nya gränssnitt) medan ni håller den varaktiga kärnan stabil och väl förstådd. Förändra kärnan, ja, men i små, reversibla, väl testade steg snarare än heroiska språng. Målet är ett system som är både pålitligt och kapabelt att utvecklas: aldrig så fruset att det [ruttnar](https://en.wikipedia.org/wiki/Software_rot), aldrig så omrört att det blir opålitligt.

## Avvägningar: för- och nackdelar

| Tillvägagångssätt | Fördelar | Nackdelar |
|---|---|---|
| Behåll och underhåll det gamla systemet | Bevarar institutionell kunskap. Låg störning. Beprövad tillförlitlighet | Åldrande stack. Knapp kompetens. Växande risk om ounderhållet |
| Omskrivning med big bang | Färsk stack. Skakar av ackumulerat skräp | Mycket hög misslyckandefrekvens. Förlorar hårt förvärvad kunskap om gränsfall |
| Inkrementell modernisering | Kontinuerlig riskminskning. Håller igång | Långsamt. Kräver bibehållen finansiering och disciplin |
| Dokumentationstung överföring | Uttryckligt, sökbart register | Förfaller om ounderhållen. Missar tyst kunskap |
| Människobaserad överföring (parprogrammering/rotation) | Varaktig arbetskunskap. Motståndskraftiga team | Kostar nuvarande produktivitet. Behöver medveten schemaläggning |
| Frys den kritiska kärnan | Maximal stabilitet på kort sikt | Stacken åldras till ounderhållbarhet. Blir för skrämmande att röra |

Den definierande avvägningen är stabilitet mot utveckling, och de naiva lösningarna fallerar båda. Frys ett kritiskt system för att skydda det, och ni garanterar att det så småningom blir ounderhållbart och osäkert. Skriv om det helt för att modernisera, och ni inbjuder den höga misslyckandefrekvens big bang-ersättningar är ökända för och slänger årtionden av kodad kunskap om gränsfall som ingen minns finns där. Den varaktiga vägen är kontinuerlig, inkrementell förändring: håll systemet vid liv och i rörelse i små steg, så att det aldrig åldras ur stöd och aldrig behöver ett skrämmande språng. Kunskapsöverföring är en liknande avvägning, mellan dokumentens lätthet och levd erfarenhets varaktighet. Svaret är båda: levd, teamhållen kunskap som ryggraden och dokument som referens.

## Frågor att diskutera med ditt team

1. **Vilka av era kritiska system saknar just nu ett aktuellt, namngivet teamägarskap?** Ägarskap är en kontinuerlig tilldelning, inte ett minne av vem som skrev koden, och ett ägarlöst kritiskt system är en nödsituation som väntar på att hända, märkt först när det går sönder. Gå igenom er tjänstekatalog (eller bygg en) och kontrollera att varje system registrerar vem som äger det, vad det beror på och hur kritiskt det är. Ta med belägg: välj tre viktiga system och försök namnge det ansvariga teamet och senaste gången ägarskapet granskades. Där ett system är föräldralöst, eller där en omorganisation i tysthet tappade det, tilldela ägarskap medvetet med en verklig överlämning snarare än genom antagande. Se till att ägarskapet inkluderar förmågan att förstå och förändra systemet, så att förvaltarskap inte förfaller till ren barnpassning.

2. **När ni ersätter ett system, vem är ansvarig för att faktiskt stänga av det gamla?** Den eviga parallellkörningen är ett vanligt och kostsamt fel: gamla och nya system körs sida vid sida på obestämd tid eftersom ingen äger nedstängningen, vilket lämnar er med att underhålla två system och få säkerheten av inget av dem. Behandla varje nedläggning som ett hanterat projekt med namngiven ansvarsskyldighet för att slutföra avvecklingen, en kartlagd lista över konsumenter, en migreringsväg och en realistisk tidslinje. Ta med belägg: hur många "tillfälliga" parallellkörningar eller halvavvecklade system drar fortfarande underhåll i er egendom i dag? Bevara data och register för att uppfylla rättsliga lagringsregler långt efter att systemet slutar köras, men låt inte lagring bli en ursäkt att aldrig bli klar. En nedläggning gjord dåligt lämnar zombiesystem som är ounderhållna men fortfarande förlitas på, det värsta av alla världar.

3. **Vilken kompetens för era långlivade system kommer arbetsmarknaden att sluta tillhandahålla, och vad är er successionsplan?** System som körs i tjugo eller trettio år överlever sina språkekosystem, sina leverantörer och karriärerna hos de människor som förstår den gamla stacken, och marknaden kommer inte pålitligt att lämna er ersättare. Minska bussfaktorn medvetet så att ingen kritisk funktion har exakt en kapabel person och korsutbilda så att minst två, helst tre, personer kan utföra varje väsentlig uppgift. Ta med belägg: för varje åldrande kritiskt system, räkna hur många som säkert kan ändra det och hur nära pension de mest kunniga är. Svaret bör driva medveten utbildning av efterträdare och verklig överlappning mellan avgående och anländande förvaltare, eftersom tyst kunskap (känslan för ett system) överförs främst genom att göra tillsammans med någon som har den. Dokument är referensen. Levd, teamhållen kunskap är ryggraden.

4. **När ändrade ni senast ert mest kritiska långlivade system, och vågar någon fortfarande göra det?** Ett system ingen har rört på ett år är inte stabilt, det driftar mot fällan "för skrämmande att röra", där varje ändring fruktas och stacken därför i tysthet åldras ur stöd. För en stor organisation spelar detta roll eftersom förlamning ackumuleras: ju längre frysningen varar, desto mer bleknar kunskapen och desto riskablare blir den eventuella oundvikliga ändringen. Ta med belägg: för varje kritiskt system, datumet för den senaste medvetna ändringen, storleken på den minsta ändring någon skulle försöka i dag och om ett rutinmässigt beroende- eller säkerhetspatch kunde levereras denna vecka utan hjältemod. Den konkurrerande hänsynen är verklig, eftersom ändring också medför risk, så målet är inte omrörning utan en jämn takt av små, reversibla, väl testade steg. I företags- och myndighetsegendomar, där en frusen kärna kan sitta under en medborgartjänst i ett årtionde, behandla "vi ändrar den aldrig" som en röd flagga snarare än en försäkran och finansiera det kontinuerliga underhåll som håller möjligheten att ändra vid liv.

5. **Hur stor del av er egendom körs på en teknik som är vid eller nära livscykelslut, och vem följer den klockan?** Åldrande körtider, ostödda databaser och ounderhållna ramverk är det långsamma felmönster som förvandlas till en plötslig kris den dag en säkerhetspatch slutar anlända. För ett stort team är faran att ingen äger horisonten: enskilda team patchar det som går sönder, men ingen håller en portföljbild över vilka stackar som förlorar leverantörsstöd och när. Ta med belägg: en inventering av varje kritiskt systems kärnteknologier, deras publicerade datum för livscykelslut eller stödslut och det nuvarande gapet mellan vad ni kör och vad som fortfarande stöds. Spänningen är mellan kostnaden för kontinuerlig uppgradering och risken med uppskjutande, och uppskjutande vinner vanligen tills det katastrofalt förlorar. I företags- och myndighetssammanhang, där upphandlings- och ackrediteringscykler kan ta ett år eller mer, ligger ett datum för livscykelslut som ser avlägset ut ofta redan inom er ledtid, så arbetet med succession och uppgradering måste börja långt innan klockan går ut.

6. **Var i er egendom är stabilitet värdet och nyhet en skuld, och hur håller ni den gränsen ärlig?** Inte alla system belönar samma behandling: kärnsystem som medborgare och kunder beror på dagligen belönar vanligen tillförlitlighet och försiktig förändring, medan kanterna belönar experiment, och att blanda ihop de två slösar pengar eller inbjuder till avbrott. För en stor organisation är risken att ambition och karriärincitament driver spännande omskrivningar in i just den varaktiga kärna som borde förbli tråkig. Ta med belägg: en karta över er egendom som markerar var tillförlitlighet är uppdraget och var nyhet skapar värde, plus nyliga ändringar som korsade den linjen åt endera hållet och vad de kostade. Den konkurrerande hänsynen är att även en stabil kärna måste utvecklas, så "stabil" kan inte bli en ursäkt att frysa. I företags- och myndighetssammanhang, knyt gränsen till uttryckliga kritikalitetsnivåer och en namngiven befogenhet som kan lägga veto mot en riskfylld omskrivning av ett system allmänheten inte har råd att se fallera, så att bedömningen inte driftar med den som är högljuddast detta kvartal.

## Sektorsperspektiv

**Startup.** Med en handfull ingenjörer och lite livslängd koncentreras din vidmakthållanderisk i en eller två personer som skrev de system du inte har råd att förlora, som fakturering eller autentisering. Lägg nästan ingenting på process, men gör de billiga, högvärdiga sakerna nu: para en andra person genom varje kritiskt system, skriv en arkitekturbeslutslogg på en sida för de överraskande delarna och behåll en körbok du faktiskt använder. Stå emot lusten att skriva om något bara för att det är gammalt, eftersom en misslyckad omskrivning av ett kärnsystem i din storlek kan avsluta företaget.

**Småföretag.** Du har inget dedikerat underhållsteam och en snäv budget, så föredra att köpa och hosta framför att bygga något du skulle behöva vidmakthålla själv. Föredra leverantörer och öppna standarder som låter dig lämna och håll ett enkelt register över vilket externt system som kör vilken kritisk funktion och vem du ringer när det går sönder. Där du äger skräddarsydd kod, se till att minst två personer (eller en betrodd konsult plus en anställd) förstår den, så att en enda avgång eller ett löpt ut supportavtal inte strandsätter dig.

**Storföretag.** Din utmaning är portföljskala: många långlivade system, många team och personal som roterar över årtionden. Standardisera ägarskap på teamnivå i en tjänstekatalog, mät bussfaktor över egendomen och finansiera kontinuerlig inkrementell modernisering snarare än att satsa på big bang-omskrivningar. Styr horisonter för livscykelslut centralt så att ingen kritisk stack i tysthet åldras ur stöd och kör varje nedläggning som ett granskat projekt med namngiven ansvarsskyldighet för att slutföra avvecklingen.

**Offentlig sektor.** Kontinuitet i skyldighet är absolut: du kan inte sluta betala bidrag eller driva flygledning medan du refaktoriserar, och fel är offentliga och konsekvensfulla. Upphandlingsregler driver dig mot öppna standarder, dataportabilitet och dokumenterade gränssnitt så att framtida underhållare och framtida leverantörer har en chans. Finansiera medveten successionsutbildning för de äldre tekniker arbetsmarknaden inte längre tillhandahåller, bevara register över avvecklade system för att uppfylla lagstadgad lagring och behandla bibehållen tillförlitlighet hos medborgartjänster som det ansvariga uppdraget snarare än overhead.

## Exempel

**Startup.** Ett startup på fem personer har redan ett system det inte har råd att förlora: faktureringstjänsten en grundare skrev den första månaden och som nu kör varje kunddebitering. Bara den grundaren förstår den, så teamet behandlar bussfaktorn som en verklig risk snarare än en komplimang. De parar en andra ingenjör genom en hel faktureringscykel, skriver en kort arkitekturbeslutslogg som förklarar varför den märkliga omförsökslogiken finns och håller en körbok bredvid koden som de faktiskt övar under en incident. De står emot att skriva om den bara för att den är gammal och oglamorös och förbättrar den i stället i små reversibla steg, så att tjänsten som håller företaget vid liv förstås av mer än ett huvud.

**Storföretag.** Ett stort försäkringsbolag driver ett policyadministrationssystem först skrivet för årtionden sedan och fortfarande centralt för verksamheten. I stället för att försöka en riskfylld total omskrivning modulariserade det systemet bakom väldefinierade gränssnitt och ersätter nu en komponent i taget, varje ändring liten och reversibel. Varje kritisk funktion har minst tre personer som kan utföra den. Jouren är delad. Arkitekturbeslutsloggar fångar varför systemet fungerar som det gör. En kurerad intern kurs för nya ingenjörer till kompetens på den [äldre](https://en.wikipedia.org/wiki/Legacy_system) stacken, och avgående experter överlappar med efterträdare så att tyst kunskap överförs genom att göra.

**Offentlig sektor.** En nationell socialförsäkringsmyndighet driver bidragsutbetalningssystem som har körts i över trettio år och inte kan stanna. Den registrerar uttryckligt teamägarskap i en tjänstekatalog. Den finansierar kontinuerligt underhåll snarare än att frysa systemen. Den utbildar efterträdare i de äldre teknikerna medvetet, eftersom arbetsmarknaden inte kommer att tillhandahålla dem. När den avvecklar ett föråldrat delsystem kör den nedläggningen som ett hanterat projekt: kartlägger varje konsument, tillhandahåller migreringsstöd, bevarar register för att uppfylla rättsliga lagringsregler och tilldelar ansvarsskyldighet för att faktiskt slutföra avvecklingen, så att inget zombiesystem dröjer sig kvar.

## Affärsnytta: motiv, ROI och TCO

Avkastningen på att vidmakthålla långlivade system kommer av att undvika de två katastrofala felmönster som dominerar deras [totala ägandekostnad](https://en.wikipedia.org/wiki/Total_cost_of_ownership). Det första är den plötsliga krisen: en nyckelperson lämnar, en ostödd komponent bryts in i eller ett föräldralöst system fallerar utan någon som förstår det. Det andra är det misslyckade megaprojektet: en forcerad total omskrivning som överskrider, underlevererar eller kollapsar. Båda är enormt dyra, och båda är till stor del förebyggbara genom jämnt förvaltarskap. Kostnaden för ett enda undvikit omskrivningsmisslyckande, eller ett enda undvikit utdraget avbrott i en kritisk medborgartjänst, överstiger vanligen år av bibehållen underhållsinvestering.

Adoptionskostnaden är löpande och oglamorös: att finansiera underhåll som inte producerar nya funktioner, att betala för korsutbildning och dokumentationstid som minskar kortsiktig output och att investera i inkrementell modernisering som aldrig gör rubriker. Kostnaden för att *inte* anta är uppskjuten och större: stigande risk när stacken åldras, svällande nyckelpersonsexponering och så småningom en påtvingad, högriskig, högkostnads ersättning under nödförhållanden. När ni driver ärendet inför ledningen, ramma om underhåll från "kostnadsställe" till "riskhantering för system organisationen inte har råd att förlora". Presentera total ägandekostnad över hela det fleråriga livet (inklusive vidmakthållande och eventuell avveckling) snarare än bara bygget. Och betona detta: för medborgar- och kundvända system är bibehållen tillförlitlighet inte overhead. Det är det förtroende som är den faktiska produkten.

## Antimönster och fallgropar

- **Hjältebehållaren.** En oersättlig person som förstår systemet. Deras avgång är en existentiell händelse.
- **Frys och glöm.** Att förklara ett kritiskt system "klart", sluta underhålla det och se dess stack åldras till ounderhållbarhet.
- **Den dömda omskrivningen.** Att satsa organisationen på en total ersättning som slänger kodad kunskap och vanligen överskrider eller fallerar.
- **Föräldralösa system.** Kritisk programvara utan aktuell ägare, märkt först när den går sönder.
- **Dokumentationsteater.** Volymer av dokument som är föråldrade, oövade och betrodda av ingen.
- **Den eviga parallellkörningen.** Gamla och nya system som körs sida vid sida på obestämd tid eftersom ingen är ansvarig för nedstängningen.
- **Förlust av tyst kunskap.** Att låta experter lämna utan överlappning, så att känslan för systemet förångas.
- **För skrämmande att röra.** Ett system så dåligt förstått att varje ändring fruktas, vilket garanterar att det förfaller.

## Mognadsmodell

**Nivå 1: Initiera.** Vidmakthållande är ad hoc och reaktivt. System beror på enskilda hjältar, ägarskap är ihågkommet snarare än tilldelat och kunskap bor odokumenterad i några få huvuden. Gamla system fryses tills de går sönder, åldrande stackar driftar mot livscykelslut obemärkt och avvecklingar tillkännages men slutförs aldrig.

**Nivå 2: Utveckla.** Grundläggande praxis dyker upp men varierar team för team. Ägarskap är nedskrivet för de mest uppenbara stora systemen, viss körboks- och annan dokumentation finns och några kritiska funktioner har en andra kapabel person. Underhåll är finansierat men reaktivt, korsutbildning sker när någon kommer ihåg och det finns inget gemensamt sätt att göra något av det över organisationen.

**Nivå 3: Standardisera.** Förvaltarskapspraxis är dokumenterad och upprätthållen i hela organisationen. Ägarskap på teamnivå registreras i en tjänstekatalog och överlever omorganisationer. Mildrande av bussfaktor genom rotation och korsutbildning är en stående regel, arkitekturbeslutsloggar och övade körböcker förväntas, modernisering är inkrementell enligt policy och varje nedläggning körs som ett hanterat projekt med namngiven ansvarsskyldighet för att slutföra avvecklingen.

**Nivå 4: Hantera.** Vidmakthållande mäts och styrs med data mot utgångslägen. Ni följer bussfaktor per kritiskt system, antalet personer som säkert kan ändra vart och ett, åldern på varje kärnteknologi mot dess datum för livscykelslut, andelen av egendomen under kontinuerligt mot uppskjutet underhåll och antalet avstannade parallellkörningar och halvfärdiga avvecklingar. Dessa mått bär trösklar som utlöser åtgärd: ett system som faller under golvet för bussfaktor eller korsar en horisont för stödslut får finansierad avhjälpning, och förvaltarskapets hälsa rapporteras till ledningen vid sidan av leverans.

**Nivå 5: Orkestrera.** Förvaltarskap förbättras kontinuerligt och är integrerat i hela organisationen. Inget kritiskt system är en enskild mänsklig felpunkt, kunskapsöverföring inklusive tyst kunskap genom överlappning är rutin och system utvecklas i små reversibla steg så att inget åldras ur stöd. Ägarskap, spårning av livscykelslut, succession och nedläggningsplanering är invävda i portfölj- och riskplanering, egendomen balanseras om när teknik och skyldigheter skiftar och fleråriga system vidmakthålls medan förtroendet hos de människor som beror på dem bevaras.

## Idéer för diskussion

- Hur mäter ni bussfaktor meningsfullt, och vilket mål är rätt för olika kritikalitetsnivåer?
- När är inkrementell modernisering genuint omöjlig, vilket gör en omskrivning till den mindre risken?
- Hur finansierar och belönar ni underhållsarbete så att förvaltarskap är en respekterad karriärväg, inte en återvändsgränd?
- Vad är det rätta sättet att bevara tyst kunskap när den sista experten är på väg att gå i pension och ingen överlappning är möjlig?
- Hur länge bör ni behålla förmågan att besvara frågor om ett avvecklat system, och vem betalar för det?
- Var i er egendom är stabilitet värdet och nyhet en skuld, och hur håller ni den bedömningen ärlig över tid?

## Viktigaste punkter

- Det mesta av viktig programvara är gammal och långlivad. Att vidmakthålla den över årtionden och personalgenerationer är en förstklassig disciplin.
- Varje kritiskt system behöver aktuellt ägarskap på teamnivå. Föräldralösa kritiska system är latenta nödsituationer.
- Minska bussfaktor medvetet (ingen kritisk uppgift bör ha exakt en kapabel person) och överför tyst kunskap genom överlappning, inte bara dokument.
- Håll långlivade system kontinuerligt och inkrementellt underhållna. Att frysa dem och att satsa på totala omskrivningar är båda felmönster.
- Planera slut som hanterade projekt med ansvarigt slutförande och bevara data och register för att uppfylla skyldigheter.
- För medborgar- och kundvända system är bibehållen tillförlitlighet och rättvisa uppdraget, och underhåll är riskhantering för det ni inte har råd att förlora.

## Referenser och vidare läsning

- Michael Feathers, *Working Effectively with Legacy Code*
- Titus Winters, Tom Manshreck, and Hyrum Wright, *Software Engineering at Google*
- Frederick P. Brooks Jr., *The Mythical Man-Month*
- Nat Pryce and Steve Freeman, *Growing Object-Oriented Software, Guided by Tests*
- Sam Newman, *Monolith to Microservices*
- Martin Fowler, *Refactoring* and writings on the Strangler Fig pattern
- Betsy Beyer et al., *Site Reliability Engineering* and *The Site Reliability Workbook* (Google)
- Diomidis Spinellis, *Code Reading: The Open Source Perspective*
- U.S. Government Accountability Office, reports on federal legacy IT modernisation
