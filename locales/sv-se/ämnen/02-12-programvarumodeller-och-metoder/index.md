# 2.12 Programvarumodeller och metoder

## Översikt och motivation

En programvarumodell är en medveten förenkling av ett system, byggd för att besvara en specifik fråga. En metod är ett disciplinerat sätt att producera programvara, inklusive de modeller den använder längs vägen. Tillsammans bildar de ett kunskapsområde i Software Engineering Body of Knowledge (SWEBOK), eftersom de är de mentala verktyg du använder för att resonera om ett system före, under och efter att du bygger det. Ett UML-klassdiagram ([Unified Modelling Language](https://en.wikipedia.org/wiki/Unified_Modeling_Language)), ett [entitet-relationsdiagram](https://en.wikipedia.org/wiki/Entity%E2%80%93relationship_model) (ERD), en [tillståndsmaskin](https://en.wikipedia.org/wiki/Finite-state_machine), en [formell specifikation](https://en.wikipedia.org/wiki/Formal_specification) och en engångsprototyp är alla modeller. [Vattenfall](https://en.wikipedia.org/wiki/Waterfall_model), [prototyputveckling](https://en.wikipedia.org/wiki/Software_prototyping), formell utveckling och [agil](https://en.wikipedia.org/wiki/Agile_software_development) utveckling är alla metoder.

Varför bry sig om modeller över huvud taget? För att mänskligt arbetsminne är litet och programvarusystem är stora. Ingen kan hålla ett system på hundra tusen rader i huvudet, så vi ritar bilder och skriver abstraktioner som visar en sida i taget: data, kontrollflöde, tillstånd, interaktioner. En modell är aldrig tänkt att vara trogen koden. Den är tänkt att vara lämplig för ett beslut. En bra modell visar exakt det du behöver för att avgöra något, och döljer allt annat.

I stora team är de verkliga insatserna samordning och kommunikation. När hundratals ingenjörer, arkitekter, analytiker och revisorer arbetar på ett system är gemensamma modeller den gemensamma mark där de förhandlar design, krav och risk. Betrakta därför modellering som ett verktyg med ett jobb att göra. Det betalar sig när en modell är billigare än misstaget den förhindrar. Det blir slöseri när du ritar den för sin egen skull, behåller den långt efter att den blivit inaktuell eller utarbetar den bortom beslutet den var tänkt att tjäna. Modellering hänger tätt ihop med programvarukrav (kapitel 2.8), principer för programvarudesign (kapitel 2.2), arkitektur och dess notationer som C4 och arc42 (kapitel 3.1) och agila arbetssätt (kapitel 10.7).

## Nyckelprinciper

- Varje modell har ett syfte. Om du inte kan namnge beslutet en modell informerar, rita den inte.
- Abstraktion är modelleringens kärnhandling: ta med det som spelar roll för syftet, utelämna resten.
- Enhetlighet spelar roll inom och mellan modeller. Motstridiga modeller är värre än inga.
- Modeller är kommunikationsartefakter först. Deras målgrupp avgör deras notation och detaljnivå.
- Föredra den lättaste modell som besvarar frågan. Utarbetning har en bärkostnad.
- En modell är bara så bra som sin analys. En ogranskad modell är ett otestat antagande.
- Välj metod efter problemets osäkerhet, risk och felkonsekvens.

## Rekommendationer

### Modellera med abstraktion, syfte och enhetlighet

Börja varje modell med att namnge dess syfte och målgrupp. Abstrahera sedan skoningslöst mot det syftet: ett sekvensdiagram som är tänkt att reda ut ett kapplöpningstillstånd ska visa tidpunkter och meddelanden, inte varje fält. Håll dina modeller konsekventa med varandra, så att entiteterna i ett ERD, klasserna i ett klassdiagram och substantiven i kraven alla stämmer överens, och konsekventa med verkligheten, vilket betyder att du uppdaterar eller raderar en modell när systemet går vidare. En inaktuell modell som människor litar på är en fara. En inaktuell modell som alla ignorerar är slöseri som fortfarande kostar uppmärksamhet.

### Välj strukturella eller beteendemodeller efter frågan

Använd strukturella modeller för att visa vad ett system består av och hur delarna förhåller sig: klassdiagram, komponentdiagram och entitet-relationsdiagram för datastruktur. Använd beteendemodeller för att visa vad ett system gör över tid: tillståndsmaskiner för objekt med meningsfulla livscykler, sekvensdiagram för interaktioner mellan komponenter och aktivitetsdiagram för arbetsflöden och affärsprocesser. Välj den notation som blottlägger beslutet framför dig. De flesta system behöver bara en handfull diagramtyper, ritade selektivt, inte hela UML-katalogen tillämpad på allt.

### Analysera modeller, rita dem inte bara

En modell förtjänar sin plats genom analys, inte bara genom att ritas. Kontrollera en tillståndsmaskin för onåbara tillstånd, saknade övergångar och baklås. Kontrollera ett ERD för normaliseringsproblem och föräldralösa relationer. Gå igenom ett sekvensdiagram mot kraven för att hitta saknade felvägar. Granska dina modeller med de domänexperter som kan upptäcka vad som är fel. Och där kostnaden för fel är hög, sträck dig efter verktygsstödd analys (modellkontrollanter, konsistenskontrollanter, simulering) i stället för att ögna igenom det.

### Tillämpa heuristiska metoder som standard

De flesta programvaror byggs med heuristiska metoder: erfarenhetsbaserade, iterativa ansatser som använder modeller informellt och bedömer resultat mot förväntningar snarare än bevis. För de flesta affärs- och myndighetssystem är det precis rätt: krav utvecklas, och en defekt går vanligen att återhämta sig från. Heuristiska metoder passar naturligt ihop med agil (kapitel 10.7): modellera precis tillräckligt för att samstämma teamet, bygg och lär sedan.

### Reservera formella metoder för högkonsekvenskärnor

[Formella metoder](https://en.wikipedia.org/wiki/Formal_methods) uttrycker specifikationer i matematik och använder verifiering, vare sig bevis eller uttömmande [modellkontroll](https://en.wikipedia.org/wiki/Model_checking), för att fastställa egenskaper. De kostar verklig skicklighet och tid, och de betalar sig precis där fel är katastrofala eller oåterkalleliga: säkerhetskritisk styrning, kryptografiska protokoll, kärnor för finansiell avveckling och liknande. Tillämpa dem på den lilla kritiska kärnan, inte hela systemet. Och notera att enbart formell specifikation, även utan fullt bevis, ofta tillför värde helt enkelt genom att tvinga dig att vara precis.

### Använd prototyputveckling för att avveckla osäkerhet

När krav eller genomförbarhet är oklara, bygg en prototyp för att lära dig, och besluta sedan, med avsikt, om du ska utveckla den vidare eller kasta den. Engångsprototyper utforskar en fråga billigt och raderas sedan. Evolutionära prototyper blir produkten och måste byggas enligt produktionsstandard. Det klassiska felet är att låta en engångsprototyp glida in i produktion av misstag. Namnge därför prototypens typ innan du bygger den.

### Anpassa metoden efter risk, inte mode

Välj metoder efter problemets osäkerhet och felkonsekvensen. Hög osäkerhet gynnar prototyputveckling och agil iteration. Hög konsekvens gynnar formell analys och rigorös verifiering. Ett system med båda behöver en kritisk formell kärna inom ett i övrigt agilt hölje. Vad du än gör, anta inte en metod bara för att den är prestigefylld eller för att en leverantör säljer den.

## Avvägningar: för- och nackdelar

| Modell eller metod | Väl tillämpad | Felläge |
|---|---|---|
| Strukturella modeller (UML, ERD) | Gemensam bild av delar och data | Diagramspridning. Drift från koden |
| Beteendemodeller (tillstånd, sekvens, aktivitet) | Blottlägger tidpunkter, tillstånd och kantfall | Överdetaljerade diagram ingen läser |
| Heuristiska metoder | Snabba, flexibla, passar de flesta system | Odisciplinerade. Dolda antaganden |
| Formella metoder | Bevisbara egenskaper för kritiska kärnor | Hög kostnad. Felaktigt tillämpade på hela systemet |
| Prototyputveckling | Billigt lärande. Avvecklar risk tidigt | Engångskod befordrad till produktion |
| Agila metoder | Anpassas till föränderliga krav | Hoppar över modellering som behövs för svåra problem |

Den återkommande spänningen är mellan stringens och hastighet. För lite modellering skickar dolda antaganden in i produktion. För mycket modellering bränner insats på diagram som aldrig informerar ett beslut och ruttnar i samma stund som koden ändras. Det finns ingen fast dos som löser detta, bara en proportionsregel: investera i en modell eller metod i proportion till den osäkerhet den avvecklar och kostnaden för att få beslutet fel. En betalningsmotor och en marknadsföringssajt förtjänar olika behandling.

## Frågor att diskutera med ditt team

1. **Analyserar vi våra modeller, eller ritar vi dem bara och går vidare?** En modell förtjänar sin plats genom analys, inte genom att finnas: en tillståndsmaskin ni aldrig kontrollerar för onåbara tillstånd eller saknade övergångar är ett otestat antagande utklätt till ett diagram. I ett stort team är det här där verkliga defekter gömmer sig, eftersom en trovärdig bild litas på just när ingen har gått igenom den mot kraven för att hitta den saknade felvägen eller den föräldralösa relationen. Ta med er viktigaste beteendemodell till mötet och försök bryta den: vilken övergång är odefinierad, vilket tillstånd saknar utgång, vilken sekvens saknar tidsgräns? Där kostnaden för fel är hög bör svaret driva er mot verktygsstödd analys (modellkontrollanter, konsistenskontrollanter, simulering) snarare än att ögna igenom, eftersom hela skälet att modellera en kritisk kärna är att hitta felet på en whiteboard i stället för i produktion.

2. **När två av våra modeller är oeniga, vilken vinner, och vem märker motsägelsen?** Enhetlighet spelar roll inom och mellan modeller, och motstridiga modeller är värre än inga, eftersom människor agerar på båda. I ett stort system driver entiteterna i datamodellen, klasserna i designen och substantiven i kraven i det tysta isär när olika team uppdaterar olika artefakter, och det första tecknet är ofta en produktionsbugg där två komponenter var oeniga om vad en sak är. Ta med ett exempel: välj ett kärnbegrepp och kontrollera om ERD:et, koden och kraven faktiskt är överens om dess form och livscykel. Om de inte är det, besluta vilken artefakt som är auktoritativ och vem som ansvarar för att hålla de andra i takt, och var beredd att radera en modell snarare än låta en inaktuell fortsätta ljuga för teamet.

3. **Vilken kärna i vårt system förlorar, om den är fel, verkliga pengar eller skadar någon, och får den den stringens den förtjänar?** Kapitlets centrala drag är att anpassa metoden efter risk: heuristiska och agila metoder för den återhämtningsbara majoriteten, formell specifikation och verifiering för den lilla högkonsekvenskärnan och billig prototyputveckling för det genuint osäkra. Felmönstren är symmetriska och båda är dyra: att tillämpa formella metoder på en marknadsföringssajt bränner pengar, och att behandla en avvecklingsmotor eller en behörighetsregeluppsättning som vanligt agilt arbete inbjuder den katastrofala, oåterkalleliga defekten. Ta med en karta över ert system och markera var ett fel är katastrofalt mot återhämtningsbart, och var krav är säkra mot okända. Svaret bör koncentrera er modelleringsinvestering dit pengarna och oklarheten finns, och uttryckligen undanhålla den överallt annars, så att en kritisk formell kärna kan sitta inom ett i övrigt agilt hölje utan att någon metod läcker in i den andras territorium.

4. **Hur mycket modellerar vi innan vi skriver kod, och förändras den dosen med den osäkerhet som ligger framför oss?** Stor design i förväg och ingen design alls är båda felmönster, och rätt dos ligger däremellan, styrd av hur mycket osäkerhet en modell faktiskt avvecklar. I ett stort team går trycket åt båda håll: en styrningsprocess kan kräva en full uppsättning diagram innan någon kod, vilket låser beslut fattade med minst information, medan leveranstrycket kan driva ett team att hoppa över den enda tillståndsmaskin som skulle ha fångat ett kostsamt kantfall. Ta med era två senaste projekt och sortera modellerna ni producerade i dem som informerade ett verkligt beslut och dem som ritades bara för att en mall bad om dem. I företags- och myndighetsprogram, där en fasgrind eller godkännandenämnd ofta föreskriver dokument i förväg, kom förberedd att argumentera för modellering som följer risk snarare än en fast leveranslista, så att betalningskärnan får sin stringens och det interna rapporteringsverktyget inte drunknar i diagram ingen läser.

5. **Har vi kommit överens om en gemensam notation och ett enda hem för våra modeller, eller uppfinner varje team sin egen?** Modeller är kommunikationsartefakter först, och deras värde kollapsar när en tillståndsmaskin ritad i ett teams verktyg inte kan läsas, hittas eller litas på av teamet som ärver den. För hundratals ingenjörer är hänsynen verklig: en föreskriven notation och ett repositorie köper enhetlighet och sökbarhet, men de lägger också på en inlärningskostnad och kan driva människor mot tunga verktyg när en fotograferad whiteboard skulle duga. Ta med exempel på var en modell faktiskt bodde (en wiki, ett diagramverktyg, ett bildspel, någons laptop) och fråga vem som kunde hitta och förstå den sex månader senare. I företags- och reglerade miljöer skärper revisionsvinkeln detta: en revisor som inte kan hitta den aktuella datamodellen eller spåra ett beslut tillbaka till en dokumenterad tillståndsmaskin kommer att behandla systemet som odokumenterat, så kom överens om en liten gemensam notation och en varaktig plats, och acceptera lätt fångst framför ceremoni överallt där konsekvensen är låg.

6. **Innan vi bygger en prototyp, beslutar vi med avsikt om den är engångs eller evolutionär, och håller vi oss till det valet?** Det klassiska, dyra felet är en engångsprototyp som i det tysta glider in i produktion därför att den demonstrerade bra och ingen namngav dess typ i förväg. Spänningen är genuin: engångsprototyper köper det billigast möjliga lärandet och bör raderas, medan evolutionära prototyper blir produkten och måste byggas enligt produktionsstandard från första raden, och att förväxla de två antingen slösar omarbete eller levererar skör kod i en roll den aldrig konstruerades för. Ta med en nylig prototyp och fråga vad som beslutades innan den byggdes, vem som hade befogenhet att befordra eller kasta den och om det beslutet överlevde leveranstrycket. I myndigheter och andra ansvarsskyldiga miljöer, där ett medborgarvänt system bär transparens- och tillförlitlighetsskyldigheter, behandla oavsiktlig befordran som ett kontrollmisslyckande: fastställ prototypens öde i förväg och gör att kasta en lyckad engångsprototyp till ett firat utfall snarare än ett slöseri att undvika.

## Sektorsperspektiv

**Startup.** Modellera på en whiteboard, fotografera den och gå vidare. Din knappaste resurs är utvecklingsuppmärksamhet, så sträck dig efter en modell bara när den är billigare än misstaget den förhindrar: en prenumerationstillståndsmaskin innan du kodar faktureringskantfallen, inte en full UML-katalog för en produkt som kan byta kurs nästa månad. Stanna heuristisk och agil, håll formella metoder helt utanför bilden och behandla varje prototyp som engångs om du inte medvetet beslutar något annat.

**Småföretag.** Du har sannolikt ingen vars jobb är formell modellering, så lita på de modeller som redan finns inbyggda i verktygen och ramverken du köper snarare än att inrätta en egen modelleringspraktik. Rama in de få modeller du ritar kring konkreta beslut: en enkel datamodellskiss för att enas om vilka kunddata du håller, ett tillståndsdiagram för det enda arbetsflöde som kostar dig en kund när det går sönder. Föredra en köpt produkt med en beprövad datamodell framför att bygga och dokumentera din egen, och håll det du ritar tillräckligt lätt för att en person kan underhålla det.

**Storföretag.** Kärnproblemet är samordning över många team, så gemensamma modeller blir den gemensamma marken: en överenskommen datamodell, en konsekvent notation och ett hem där ERD:et, C4-diagrammen och tillståndsmaskinerna kan hittas och litas på. Standardisera en liten notation och upprätthåll enhetlighet så att entiteterna i kraven, designen och databasen inte driver isär mellan team. Reservera formell specifikation och modellkontroll för högkonsekvenskärnorna (avveckling, avstämning, åtkomstkontroll), finansiera den specialistkompetens det kräver och behåll ett revisionsspår från varje dokumenterad modell tillbaka till beslutet den motiverade.

**Offentlig sektor.** Regler fastställda i lag måste kunna spåras till lagtext, vilket är där formell specifikation förtjänar sin kostnad: specificera behörighets- eller bedömningslogik exakt, verifiera nyckelegenskaper och låt revisorer spåra varje utfall tillbaka till regeln som producerade det. Upphandling lägger till sin egen tyngd, eftersom dokument och modeller ofta är avtalade leverabler, så kom överens om vilka modeller som är genuint beslutsbärande snarare än producerade bara för att tillfredsställa en checklista. Publicera klartextbeskrivningar av hur konsekvensrika system fungerar, och använd engångsprototyputveckling för att testa medborgarvänd intagning med verkliga användare innan ni förbinder er till ett produktionsbygge.

## Exempel

**Startup.** En liten startup som bygger en produkt för prenumerationsfakturering skissar prenumerationens livscykel (prov, aktiv, förfallen, avslutad, återaktiverad) som en tillståndsmaskin på en whiteboard innan den skriver kod. När de går igenom diagrammet märker de att de aldrig definierade vad som händer när ett förfallet kontos betalning äntligen går igenom, ett kantfall som skulle ha strandsatt verkliga kunder i limbo. Den modellen på fem minuter besparar dem ett produktionshuvudbry, och de fotograferar den i stället för att underhålla ett tungt diagramverktyg. Överallt annars förblir de agila och modellerar precis tillräckligt för att samstämma, för i deras skala är en defekt återhämtningsbar och formella metoder skulle vara ren kostnad.

**Storföretag.** En global bank bygger en ny betalningsplattform. Teamet använder ett entitet-relationsdiagram för att enas om den gemensamma datamodellen över konto-, huvudbok- och meddelandeteamen, och C4-diagram (kapitel 3.1) för att visa hur tjänsterna passar ihop. De modellerar transaktionens livscykel (väntande, godkänd, avvecklad, återförd, bestridd) som en uttrycklig tillståndsmaskin, och analysen visar att den saknar en övergång för delåterföringar. Luckan åtgärdas på en whiteboard i stället för i produktion. Sekvensdiagram går igenom avvecklingsflödet mot kraven (kapitel 2.8) för att blottlägga saknade tidsgräns- och omförsöksvägar. Den dagliga leveransen är agil, men kärnalgoritmen för avstämning, där ett fel betyder verkliga förlorade pengar, får en formell specifikation och modellkontrolleras före implementation. Modellering koncentreras dit pengarna och oklarheten finns, och hålls lätt överallt annars.

**Offentlig sektor.** En nationell skattemyndighet moderniserar bidragsbedömning. Eftersom behörighetsreglerna är fastställda i lag och granskas skriver teamet en formell specifikation av reglerna som rena transformationer och verifierar nyckelegenskaper, som att ingen sökande är både behörig och obehörig och att varje ärende når ett beslut, så att revisorer kan spåra utfall tillbaka till lagtext. Vid sidan av den formella kärnan bygger teamet en engångsprototyp av det medborgarvända intagningsformuläret för att testa med verkliga användare. De lär sig att en flerstegsguide minskar fel, kastar sedan prototypen och bygger om intagningen enligt produktionsstandard. Aktivitetsdiagram dokumenterar handläggarens hela process för utbildning och revision. De högkonsekventa reglerna får formell stringens, den osäkra användarupplevelsen får billig prototyputveckling, och ingen metod tillämpas där den andra hör hemma.

## Affärsnytta: motiv, ROI och TCO

Avkastningen på modellering kommer från att hitta defekter tidigare, där de är långt billigare att åtgärda. En motsägelse funnen på en whiteboard kostar minuter. Samma motsägelse funnen i produktion kan kosta ett avbrott, ett omarbetsprogram eller, i reglerade domäner, ett rättsligt ansvar. Modeller sänker också den totala ägandekostnaden genom att tjäna som varaktig kommunikation. Ett system som överlever sina författare, det normala fallet i företag och myndigheter, är långt billigare att underhålla när dess datamodell, tillståndsmaskiner och nyckelflöden är dokumenterade korrekt.

Kostnaderna är verkliga, och du måste väga dem. Modeller tar tid att bygga, skicklighet för att bygga väl och löpande insats för att hålla aktuella. Formella metoder lägger till specialistarbete. Brytpunkten styrs av osäkerhet och konsekvens. Där båda är låga förstör tung modellering värde och agila heuristiker vinner. Där endera är hög betalar sig riktad modellering, och för den kritiska kärnan formell verifiering, många gånger om genom att förhindra den dyra klassen av fel. För att argumentera inför ledningen, knyt modelleringsinvestering till specifika risker som avvecklats och till underhållbarheten hos långlivade system. Och följ om modeller faktiskt konsulteras, för en oanvänd modell är ren kostnad.

## Antimönster och fallgropar

- **Modellering för sin egen skull:** att producera diagram därför att en process kräver dem, inte därför att de informerar ett beslut.
- **Inaktuella modeller som litas på som sanning:** diagram som inte längre matchar koden men ändå förlitas på.
- **Stor design i förväg:** uttömmande modeller producerade före någon kod, vilket låser beslut fattade med minst information.
- **Diagramspridning:** varje UML-typ tillämpad enhetligt, vilket dränker de få användbara vyerna i brus.
- **Formella metoder överallt:** att tillämpa dyr verifiering på kod där felkonsekvensen inte motiverar det.
- **Oavsiktlig prototypbefordran:** en engångsprototyp som i det tysta levereras som produkten.
- **Notation framför substans:** att gräla om UML-korrekthet i stället för om modellen besvarar frågan.

## Mognadsmodell

- **Nivå 1 (Initiera):** Modellering är ad hoc eller frånvarande och rent reaktiv. Ingen metod är namngiven. Modeller, när de alls ritas, är inkonsekventa, oanalyserade och överges så fort mötet tar slut.
- **Nivå 2 (Utveckla):** Vissa team ritar vanliga diagram och följer en namngiven metod, men praxis är ojämn över organisationen: modeller produceras ofta ceremoniellt, driver från koden och analyseras sällan för defekter.
- **Nivå 3 (Standardisera):** En gemensam notation, en dokumenterad guide för metodval och konsistensregler är definierade och upprätthålls i hela organisationen. Modeller väljs efter syfte, hålls i takt med systemet, granskas för defekter och metoden anpassas efter varje problems risk.
- **Nivå 4 (Hantera):** Modellering mäts och styrs mot utgångslägen. Team följer hur många defekter analys fångar före implementation, hur långt modeller driver från koden, om varje modell faktiskt konsulterades för ett verkligt beslut samt omarbete och cykeltid som sparats mot ett definierat utgångsläge. Metodval kalibreras efter uppmätt osäkerhet och konsekvens, och kritiska kärnor verifieras formellt mot överenskomna täckningsmål.
- **Nivå 5 (Orkestrera):** Modellering och metodval förbättras kontinuerligt och är integrerade med leverans- och riskplanering i hela organisationen. Investering anpassas när osäkerhet och konsekvens förskjuts, modeller hålls rutinmässigt aktuella, avvecklas eller fördjupas på grundval av belägg, och formella, heuristiska och prototypmetoder komponeras så att var och en sitter exakt där den betalar sig.

## Idéer för diskussion

- Vilka modeller informerade i ert senaste projekt ett verkligt beslut, och vilka ritades bara därför att en process krävde det?
- Var i era system skulle en formell specifikation betala sig själv, och var skulle den vara slöseri?
- Hur avgör ni om en prototyp är engångs eller evolutionär, och upprätthåller ni det beslutet?
- Hur håller ni modeller från att driva ur takt med koden, eller accepterar ni att vissa bör raderas i stället?
- Vad är rätt mängd modellering före kod i ert sammanhang, och hur förändras den med osäkerhet?
- Vilken beteendemodell (tillstånd, sekvens eller aktivitet) skulle ha fångat er senaste produktionsincident?

## Viktigaste punkter

- En modell är en målinriktad abstraktion. Om du inte kan namnge beslutet den informerar, rita den inte.
- Anpassa strukturella och beteendemodeller efter den specifika frågan och håll dem konsekventa och aktuella.
- Analysera modeller. En ogranskad modell är ett otestat antagande.
- Heuristiska och agila metoder passar de flesta system. Reservera formella metoder för högkonsekvenskärnor.
- Använd prototyper för att avveckla osäkerhet och besluta i förväg om de är engångs eller evolutionära.
- Investera i modellering i proportion till den osäkerhet den avvecklar och kostnaden för att få beslutet fel.

## Referenser och vidare läsning

- IEEE Computer Society, *SWEBOK Guide (Software Engineering Body of Knowledge), Version 4.0*, Software Engineering Models and Methods knowledge area
- Martin Fowler, *UML Distilled: A Brief Guide to the Standard Object Modelling Language*
- Grady Booch, James Rumbaugh, Ivar Jacobson, *The Unified Modelling Language User Guide*
- Frederick P. Brooks, *The Mythical Man-Month* and *No Silver Bullet: Essence and Accident in Software Engineering*
- Daniel Jackson, *Software Abstractions: Logic, Language, and Analysis* (the Alloy modelling language)
- Leslie Lamport, *Specifying Systems* (TLA+)
- Simon Brown, *Software Architecture for Developers* (the C4 model)
- David Harel, *Statecharts: A Visual Formalism for Complex Systems*
