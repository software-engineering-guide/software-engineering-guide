# 2.2 Principer för programvarudesign

## Översikt och motivation

Principer för programvarudesign är tumregler för hur du ordnar kod så att du kan förstå, ändra och utöka den över tid. De omfattar namngivna akronymer ([SOLID](https://en.wikipedia.org/wiki/SOLID) för fem [objektorienterade](https://en.wikipedia.org/wiki/Object-oriented_programming) designprinciper, [DRY](https://en.wikipedia.org/wiki/Don%27t_repeat_yourself) för upprepa inte dig själv, [KISS](https://en.wikipedia.org/wiki/KISS_principle) för håll det enkelt, [YAGNI](https://en.wikipedia.org/wiki/You_aren%27t_gonna_need_it) för du kommer inte att behöva det), strukturella begrepp ([koppling](https://en.wikipedia.org/wiki/Coupling_(computer_programming)), [sammanhållning](https://en.wikipedia.org/wiki/Cohesion_(computer_science)), [åtskillnad av ansvarsområden](https://en.wikipedia.org/wiki/Separation_of_concerns)), katalogiserade [designmönster](https://en.wikipedia.org/wiki/Software_design_pattern), modelleringsansatser på högre nivå som [domändriven design](https://en.wikipedia.org/wiki/Domain-driven_design) (att modellera programvara på affärsdomänens språk) och valet mellan objektorienterade, [funktionella](https://en.wikipedia.org/wiki/Functional_programming) och [dataorienterade](https://en.wikipedia.org/wiki/Data-oriented_design) stilar. Inget av detta är lagar. Det är hoppressad erfarenhet, och du måste tillämpa det med omdöme.

För stora team ligger värdet i gemensamma principer i samordning. När hundratals ingenjörer arbetar på samma system behöver de ett gemensamt ordförråd för designdiskussioner och en gemensam uppsättning standardval så att oberoende skrivna moduler passar ihop. God design är det som låter många människor ändra ett system parallellt utan ständiga krockar. Det är också det som håller ett system förändringsbart ett decennium senare, den normala livslängden för företags- och myndighetssystem, långt efter att deras ursprungliga författare slutat.

Den avgörande färdigheten är inte att memorera principer. Det är att veta när var och en vilseleder dig. Varje princip har ett felläge: DRY kan ge fel abstraktion, SOLID kan ge onödig indirektion, YAGNI kan svälta utbyggbarhet du verkligen behöver. Det här kapitlet behandlar principer som verktyg med ett tillämpningsområde, och det betonar koppling och sammanhållning som de djupare egenskaper akronymerna försöker tjäna.

## Nyckelprinciper

- Hantera koppling och sammanhållning först. De flesta namngivna principer är indirekta sätt att förbättra dessa två egenskaper.
- Optimera för förändring: god design minimerar kostnaden för de ändringar du faktiskt kommer att behöva göra.
- Föredra den enklaste design som fungerar nu, men behåll gränser där förändring är sannolik.
- Duplicering är billigare än fel abstraktion. Vänta tills mönstret är tydligt.
- Gör beroenden uttryckliga och rikta dem mot stabila saker.
- Modellera domänen på domänens språk. Justera programvarans gränser efter affärsgränser.
- Välj paradigm efter problemet, inte efter ideologi. De flesta stora system är pragmatiskt blandade.

## Rekommendationer

### Använd SOLID som en lins, inte en checklista

Tillämpa enskilt ansvar för att hålla moduler sammanhållna, beroendeinversion för att rikta beroenden mot abstraktioner där en gräns verkligen finns och öppen-stängd där utökningspunkter är verkliga. Tillverka inte gränssnitt, fabriker och lager bara för att tillfredsställa akronymen när det bara finns en implementation och ingen andra i sikte. Indirektion har en kostnad, och du betalar den vid varje läsning.

### Tillämpa DRY på kunskap, inte på text

DRY handlar om att inte duplicera en enda auktoritativ bit *kunskap*. Det handlar inte om att eliminera rader som bara ser likadana ut. Två kodstycken som ser likadana ut men ändras av olika skäl bör förbli åtskilda. Föredra lite duplicering framför en förhastad gemensam abstraktion som kopplar ihop orelaterade saker. Extrahera abstraktionen när det verkliga mönstret har dykt upp två eller tre gånger.

### Låt KISS och YAGNI motstå spekulation

Bygg för de krav du har, inte de du föreställer dig. Undvik spekulativ generalitet, som konfigurerbara ramverk, insticksystem och utökningspunkter ingen har bett om. Motvikten är att viss flexibilitet verkligen är billigare att bygga in tidigt, som ett stabilt gränssnitt eller en ren söm. YAGNI argumenterar mot spekulativ *implementation*, inte mot genomtänkta gränser.

### Designa uttryckligen för låg koppling och hög sammanhållning

Låt varje modul göra en väldefinierad sak (sammanhållning) och bero på så få andra moduler som möjligt, genom smala gränssnitt (låg koppling). När du granskar en design, fråga vilka ändringar som ger krusningar över modulgränser. De krusningarna är det verkliga måttet på koppling. Åtskillnad av ansvarsområden är samma idé tillämpad på lager och tvärgående angelägenheter.

### Använd designmönster som ordförråd, tillämpa antimönster som varningar

Mönster är användbara gemensamma namn på återkommande lösningar. Sträck dig efter ett när problemet verkligen matchar det. Påtvinga inte mönster för att se sofistikerad ut, eftersom mönstertung kod ofta är ett tecken på överkonstruktion. Lär dig de vanliga [antimönstren](https://en.wikipedia.org/wiki/Anti-pattern) (gudobjekt, anemiska modeller där det är olämpligt, stora lerklumpar, distribuerade monoliter) som diagnostiska etiketter.

### Anta domändriven design där domänen är komplex

För system med rika affärsregler, använd DDD:s taktiska och strategiska verktyg: ett allestädes närvarande språk delat med domänexperter, avgränsade kontexter som skär systemet i oberoende modellerade delar och kontextkartor som beskriver hur delarna förhåller sig. Avgränsade kontexter är särskilt värdefulla i företagsskala, eftersom de justerar teamets ägarskap efter modellgränser. DDD är överkill för enkla [CRUD](https://en.wikipedia.org/wiki/Create,_read,_update_and_delete)-system (skapa, läsa, uppdatera, radera).

### Välj paradigm efter passform

Använd objektorientering för att kapsla in tillståndsbärande beteende och modellera domäner. Använd funktionell stil för transformationer, samtidighet och förutsägbarhet genom [oföränderlighet](https://en.wikipedia.org/wiki/Immutable_object). Använd dataorienterad design där prestanda och cachebeteende dominerar. Stora system blandar alla tre. Gör valet per komponent och håll gränserna mellan stilarna rena.

## Avvägningar: för- och nackdelar

| Princip / tillvägagångssätt | Väl tillämpad | Felläge |
|---|---|---|
| SOLID | Tydliga sömmar där förändring sker. Testbara enheter | Spridning av gränssnitt och lager. Indirektion utan utdelning |
| DRY | Enda sanningskälla för verklig kunskap | Fel abstraktion som kopplar orelaterad kod |
| KISS / YAGNI | Smala, begripliga system | Underdesignade sömmar. Kostsamma eftermonteringar av behövd flexibilitet |
| Designmönster | Gemensamt ordförråd. Beprövade strukturer | Mönsterkargokult. Oavsiktlig komplexitet |
| Domändriven design | Justerade modeller och team. Tämjd komplexitet | Tung ceremoni på enkla domäner. Felplacerade kontextgränser |
| Funktionell / oföränderlig | Förutsägbarhet. Säkrare samtidighet | Krångligt för i grunden tillståndsbärande problem. Prestandaöverraskningar |

Den återkommande spänningen är mellan underdesign och överdesign. Underdesignade system ackumulerar koppling och blir stela. Överdesignade system drunknar i abstraktion som någon måste förstå och underhålla. Svaret är inte en fast punkt. Det är en disciplin: skjut upp beslut tills du har tillräckligt med information, medan du behåller de sömmar som låter dig ändra dig.

## Frågor att diskutera med ditt team

1. **Vilken är er konkreta tröskel för att extrahera en gemensam abstraktion, och hur hindrar ni DRY från att ge fel en?** Det här kapitlet är rakt på sak med att duplicering är billigare än fel abstraktion, och att ni bör vänta tills mönstret har dykt upp två eller tre gånger innan ni extraherar. I ett stort team är faran att någon faktoriserar två likadana kodstycken till en gemensam modul över teamgränser, och sedan ger varje framtida ändring av en anropare krusningar i den andra. Signalen att ta med är om dupletterna ändras av samma skäl eller bara råkar se likadana ut just nu. Kom överens om en regel om tre, och kräv att en kandidatabstraktion faktiskt har ändrats tillsammans innan ni kopplar anroparna. Den enda överenskommelsen förhindrar en klass av koppling som är dyr att lösa upp när många team beror på den.

2. **Hur gör ni koppling och sammanhållning synliga i designgranskning i stället för att lämna dem åt magkänsla?** Nyckelprinciperna sätter koppling och sammanhållning över varje akronym och definierar koppling som de ändringar som ger krusningar över modulgränser. Intuition skalar inte över hundratals ingenjörer som var och en bara ser sitt hörn av systemet. Ta med belägg en maskin kan producera: beroendegrafer och samändringsdata som visar vilka moduler som hela tiden redigeras tillsammans i samma commits. Lägg till en uttrycklig granskningsfråga som frågar vilka modulgränser en ändring tvingar er att korsa. När två moduler alltid ändras tillsammans är det er signal att antingen slå ihop dem eller åtgärda gränsen mellan dem.

3. **Var går gränsen i era system mellan en domän rik nog att motivera domändriven design och en enkel CRUD-app där den är överkill?** Kapitlet rekommenderar DDD:s avgränsade kontexter just därför att de justerar teamets ägarskap efter modellgränser, och varnar för att DDD är överkill för enkla system för skapa-läsa-uppdatera-radera och förfaller till ceremoni utan verklig modellering. Att få detta fel i endera riktningen är kostsamt: tung DDD på en tunn domän begraver en enkel app i ceremoni, medan en vidsträckt gemensam modell över många team tvingar fram ständig samordning mellan team. Ta med de signaler som faktiskt avgör det: tätheten av affärsregler och hur många team som behöver äga delar oberoende. Reservera den strategiska maskineriet för den komplexa kärnan och låt de enkla kanterna förbli enkla. Det håller er borta från både DDD-teater och den stora lerklumpen.

4. **När är en abstraktion, ett gränssnitt eller ett designmönster värd den indirektion den lägger till, och vem har befogenhet att kalla en design överkonstruerad?** Det här kapitlet är uttryckligt med att indirektion har en kostnad du betalar vid varje läsning, och att tillverka gränssnitt, fabriker och lager för att tillfredsställa SOLID eller för att se sofistikerad ut är ett felläge. I ett stort team går trycket åt andra hållet: granskare vinkar igenom extra abstraktion eftersom det ser disciplinerat ut, och ingen vill vara den som argumenterar för mindre struktur. Den motstridiga hänsynen är verklig, eftersom vissa sömmar verkligen förtjänar sin plats och att ta bort dem senare är dyrt. Ta med konkreta belägg till diskussionen: hur många implementationer ett gränssnitt faktiskt har i dag, hur ofta utökningspunkten någonsin har flexats och hur många filer en läsare måste öppna för att följa en kodväg. Kom överens om att en enda implementation utan en andra i sikte är ett standardskäl att inlina, och namnge vem som kan kalla en design överkonstruerad utan att det läses som en förolämpning. I företags- och myndighetssystem som överlever sina författare med ett decennium är gratis indirektion en skatt varje framtida underhållare betalar, så behandla "vad köper den här abstraktionen oss" som en stående granskningsfråga, inte en personlig utmaning.

5. **Hur beslutar ni vilket paradigm varje komponent använder, objektorienterat, funktionellt eller dataorienterat, och hur håller ni gränserna mellan dem rena?** Kapitlet hävdar att stora system är pragmatiskt blandade och att ni bör välja per komponent efter passform, med objektorientering för tillståndsbärande domäner, funktionell stil för transformationer och samtidighet och dataorienterad design där prestanda och cachebeteende dominerar. Obehandlat blir paradigmvalet en fråga om vem som skrev modulen först, och föränderligt tillstånd läcker in i det som borde vara rena transformationer, eller en funktionell purism kämpar mot ett i grunden tillståndsbärande problem. Beläggen värda att ta med är var er faktiska smärta finns: vilka komponenter som är svåra att testa på grund av dolt tillstånd, vilka heta vägar som är cachebundna och var den nuvarande stilen tvingar fram krångliga lösningar. Bestäm standardparadigmet för varje lager medvetet och skriv ner var sömmarna mellan stilarna går, så att en funktionell kärna och en imperativ kant inte flyter in i varandra. För ett reglerat eller offentligt system där en beräkning måste vara granskningsbar och reproducerbar för en given period är en oföränderlig, funktionell kärna ofta ett regelefterlevnadskrav snarare än en smakfråga, och den begränsningen bör driva gränsen snarare än följa efter den.

6. **Hur hindrar ni de här principerna från att hårdna till dogm, och var dokumenterar ni resonemanget bakom ett designbeslut så att ett framtida team kan ompröva det?** Varje princip i det här kapitlet har ett tillämpningsområde och ett felläge, och hela inramningen behandlar dem som verktyg att tillämpa med omdöme snarare än lagar att upprätthålla. I ett stort team blir en princip i det tysta en regel: DRY förbjuder all duplicering, SOLID föreskriver ett gränssnitt per klass och pragmatiska undantag blockeras i granskning av människor som citerar akronymen snarare än utfallet. Spänningen är att viss enhetlighet verkligen hjälper hundratals ingenjörer att samordna sig, så ni kan inte bara förklara varje princip valfri. Ta med exempel där att följa en princip till punkt och pricka gav en sämre design, och ta med beslutsloggarna, om några, som förklarar varför en viss gräns eller abstraktion finns. Kom överens om att principer är standardval en ingenjör får avvika från med ett dokumenterat skäl, och fånga avgörande designval i en kort arkitekturbeslutslogg så att nästa team ärver resonemanget och inte bara koden. I företags- och offentliga system, där de ursprungliga författarna sedan länge är borta och revisioner frågar varför systemet har sin form, är det skrivna spåret skillnaden mellan en design framtida team säkert kan ändra och en de är rädda att röra.

## Sektorsperspektiv

**Startup.** Föredra den enklaste design som levererar och behåll en enda väl faktoriserad modul tills ett verkligt andra användningsfall tvingar fram en söm. Din knappaste resurs är utvecklingsuppmärksamhet, så förhastade gränssnitt, lager och spekulativa ramverk är ren kostnad. Följ regeln om tre innan du extraherar någon gemensam abstraktion, och låt YAGNI döda de utökningspunkter ingen har bett om ännu.

**Småföretag.** Utan särskild arkitekt och med snäv budget, lita på den design som redan är inbakad i de ramverk och bibliotek du köper i stället för att uppfinna egna mönster. Reservera eget designarbete för den handfull regler som verkligen är din verksamhet, och håll allt annat konventionellt så att en konsult eller nyanställd kan läsa det. Lite duplicering du förstår slår en klurig abstraktion bara dess författare kan underhålla.

**Storföretag.** Utdelningen av gemensamma principer är samordning över många team: ett gemensamt ordförråd för designgranskning och avgränsade kontexter som justerar modellgränser efter teamets ägarskap så att grupper kan utvecklas oberoende. Hantera koppling och sammanhållning uttryckligen med beroende- och samändringsdata, och dokumentera avgörande designbeslut så att system förblir förändringsbara långt efter att deras författare gått vidare. Vakta lika mycket mot den felaktiga abstraktion som kopplar team som mot den överkonstruktion som beskattar varje läsare.

**Offentlig sektor.** Granskningsbarhet och reproducerbarhet dikterar ofta designen. En oföränderlig, funktionell kärna låter dig reproducera en historisk beräkning exakt för en given period, vilket ett trassligt objektgraf med dolt föränderligt tillstånd inte kan garantera. Föredra uttryckliga publicerade kontrakt framför delade tabeller vid kontextgränser, och håll designen och dess beslutsloggar läsbara för revisorer och för det team som ärver systemet ett decennium senare.

## Exempel

**Startup.** En startup med tre ingenjörer som bygger sin första produkt motstår lusten att dela upp varje funktion i lager av gränssnitt och fabriker och behåller en enda väl faktoriserad modul tills ett verkligt andra användningsfall dyker upp. När samma logik dyker upp en tredje gång i registrerings- och faktureringsflödena extraherar de en liten gemensam funktion i stället för ett spekulativt ramverk. Det håller kodbasen tillräckligt liten för att var och en av dem kan hålla den i huvudet, och de få sömmar de drar hamnar där produkten med störst sannolikhet ändras.

**Storföretag.** En stor försäkringsplattform modellerar policy, skador och fakturering som separata avgränsade kontexter, var och en ägd av ett dedikerat team med egen datamodell och tjänstegräns. Där kontexterna möts, som när ett skadeärende refererar till en policy, talar de genom uttryckliga publicerade kontrakt snarare än delade databastabeller. Det låter de tre teamen utvecklas oberoende, och det allestädes närvarande språket håller samtalen med försäkringstagare och aktuarier precisa. En tidigare version hade delat en enda vidsträckt modell, och varje ändring krävde samordning mellan team.

**Offentlig sektor.** Ett nationellt system för skatteberäkning föredrar medvetet en dataorienterad, funktionell kärna för sin beräkningsmotor. Skatteregler uttrycks som rena transformationer över oföränderliga indataposter, vilket gör dem granskningsbara, testbara och reproducerbara för ett givet skatteår. De imperativa, tillståndsbärande delarna (arbetsflöde, aviseringar) hålls vid kanterna. Revisorer kan peka på en specifik regelversion och reproducera varje historisk beräkning exakt, vilket är ett rättsligt krav som ett trassligt objektgraf med dolt föränderligt tillstånd inte kunde garantera.

## Affärsnytta: motiv, ROI och TCO

Designkvalitet är en investering i ett systems *förändringsbarhet*, och förändringsbarhet dominerar den totala ägandekostnaden. Det mesta av ett systems kostnad landar efter dess första release, i modifiering och utökning. Väldesignade system håller kostnaden för förändring ungefär jämn över tid. Dåligt designade ser kostnaden för varje ändring stiga tills systemet blir i praktiken omodifierbart och måste skrivas om, det dyraste utfallet av alla.

Införandekostnaden är främst kompetens och granskningsdisciplin: att lära ut principerna och lägga designtid i förväg. Kostnaden för att inte införa dem är den långsamma uppbyggnaden av [teknisk skuld](https://en.wikipedia.org/wiki/Technical_debt), fallande leveranshastighet, stigande defektfrekvens och slutliga kostsamma omskrivningar. För att argumentera inför ledningen, koppla designdisciplin till leveransförutsägbarhet och till att undvika omskrivningsprogram, och följ ledande indikatorer som andel misslyckade ändringar och tiden att implementera jämförbara funktioner över tid. Se också upp för det motsatta felet: att överinvestera i design för osäkra framtider förstör också värde. Argumentet är alltså för *lämplig* design, kalibrerad efter hur sannolik och hur kostsam framtida förändring är.

## Antimönster och fallgropar

- **Spekulativ generalitet:** att bygga utbyggbarhet för tänkta krav som aldrig kommer.
- **Fel abstraktion:** att tvinga ihop orelaterad kod för att tillfredsställa DRY, vilket skapar koppling som är värre än duplicering.
- **Mönsterkargokult:** att tillämpa designmönster för deras egen skull och lägga till indirektion utan nytta.
- **Anemiska objekt eller gudobjekt:** modeller utan beteende, eller objekt som gör allt. Båda signalerar felplacerade ansvarsområden.
- **Distribuerad monolit:** tjänster uppdelade fysiskt men ändå tätt kopplade, som kombinerar kostnaderna för båda tillvägagångssätten.
- **Stor lerklump:** ingen urskiljbar struktur. Varje ändring riskerar allt.
- **DDD-teater:** att anta vokabulären och mappstrukturen utan den domänmodellering som ger den värde.

## Mognadsmodell

- **Nivå 1, Initiera:** Design är ad hoc och reaktiv. Koppling ackumuleras okontrollerat. Principer är okända eller åberopas som slagord, och abstraktioner dyker upp eller försvinner efter individuell vana.
- **Nivå 2, Utveckla:** Team känner till principerna och tillämpar dem, men inkonsekvent och ofta dogmatiskt. Vissa grupper hanterar koppling och sammanhållning medvetet medan andra inte gör det, och det finns inget gemensamt ordförråd över organisationen.
- **Nivå 3, Standardisera:** Ett gemensamt designordförråd, en regel om tre för att extrahera abstraktioner, analys av koppling och sammanhållning och avgränsade kontexter justerade efter team är dokumenterade och förväntade i hela organisationen, tillämpade konsekvent i designgranskning snarare än överlämnade åt individuell smak.
- **Nivå 4, Hantera:** Designens hälsa mäts mot utgångslägen: kopplings- och samändringsdata, andel misslyckade ändringar och tiden att implementera jämförbara funktioner följs över tid, så att abstraktioner och gränser läggs till, behålls eller tas bort på grundval av belägg, och överkonstruktion och fel abstraktion fångas av data snarare än åsikt.
- **Nivå 5, Orkestrera:** Designdisciplin är integrerad med leverans- och riskplanering i hela organisationen. Principer tillämpas med nyans och kända felmönster. Paradigm- och gränsval är medvetna och omprövas kontinuerligt, och organisationen omstrukturerar, omdefinierar och avvecklar rutinmässigt abstraktioner när domänen och beläggen förskjuts.

## Idéer för diskussion

- Hur skiljer ni en behövd söm från spekulativ generalitet innan ni har det framtida kravet?
- När har DRY lett ert team till fel abstraktion, och hur kände ni igen det?
- Var bör gränserna för avgränsade kontexter gå, och hur nära bör de spegla organisationsschemat?
- Hur mycket design bör föregå kod i ert sammanhang, och hur dokumenterar ni besluten?
- Vilka delar av ert system skulle ha nytta av en mer funktionell eller dataorienterad stil?
- Hur hindrar ni designprinciper från att hårdna till dogm som motstår pragmatiska undantag?

## Viktigaste punkter

- Koppling och sammanhållning är de egenskaper som spelar roll. Akronymerna är medel för de målen.
- Varje princip har ett felläge. Vet när var och en vilseleder.
- Föredra lite duplicering framför en förhastad eller fel abstraktion.
- Använd DDD och avgränsade kontexter för att justera komplexa domäner efter teamets ägarskap.
- Välj paradigm efter passform. Stora system är pragmatiskt blandade.
- Designa för de ändringar du faktiskt kommer att behöva och undvik både under- och överdesign.

## Referenser och vidare läsning

- Robert C. Martin, *Clean Architecture* and *Agile Software Development, Principles, Patterns, and Practices*
- Eric Evans, *Domain-Driven Design: Tackling Complexity in the Heart of Software*
- Vaughn Vernon, *Implementing Domain-Driven Design*
- Erich Gamma, Richard Helm, Ralph Johnson, John Vlissides, *Design Patterns: Elements of Reusable Object-Oriented Software*
- Martin Fowler, *Refactoring: Improving the Design of Existing Code* and *Patterns of Enterprise Application Architecture*
- David L. Parnas, *On the Criteria to Be Used in Decomposing Systems into Modules*
- Sandi Metz, *Practical Object-Oriented Design*
