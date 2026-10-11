# 2.19 Endurbygging og tæknileg skuld

## Yfirlit og tilgangur

[Endurbygging](https://en.wikipedia.org/wiki/Code_refactoring) (refactoring) er að breyta innri uppbyggingu kóða án þess að breyta því sem hann gerir utan frá séð. Þú endurnefnir breytu, klýfur langa aðgerð, dregur út flokk, fellir flækju af skilyrðum saman í eitthvað sem lesandi getur fylgt og forritið hegðar sér nákvæmlega eins og áður. Þessi síðasti hluti er allur agi hennar. Endurbygging varðveitir hegðun samkvæmt skilgreiningu, og um leið og þú breytir líka hegðun ertu ekki lengur að endurbyggja. Þú ert að gera tvennt áhættusamt í einu og fela hvort á bak við hitt. Þessi kafli lítur á þetta sem aðskildar athafnir af ásetningi, því rugl milli þeirra er þar sem mest endurbygging fer úrskeiðis.

Í stóru teymi skiptir þetta meira máli en fyrir einmana hönnuð, því kóðinn sem þú ert að hreinsa er kóði sem hundruð annarra lesa, byggja á og óttast að snerta. Endurbygging er hvernig sameiginlegur kóðagrunnur helst íbúðarhæfur yfir ár og starfsmannaveltu. Hún tengist beint hugbúnaðarsmíði (kafli 2.9), þar sem dagleg kóðagæði eru sett, og prófunarstefnu (kafli 2.4), sem er öryggisnetið sem gerir endurbyggingu örugga yfirleitt. Hún tengist líka erfiðari spurningunni um [tæknilega skuld](https://en.wikipedia.org/wiki/Technical_debt): uppsafnaðan kostnað flýtileiða, eldri hönnunar og frestaðrar hreinsunar sem gera hverja framtíðarbreytingu hægari. Endurbygging er aðalleiðin til að greiða þá skuld niður, svo viðfangsefnin tvö eiga heima í einum kafla.

Í fyrirtækja- og opinberu umhverfi hækka hagsmunirnir. Þessi kerfi eru langlíf, oft áratuga gömul og iðulega undir úttektar- og breytingastýringarkerfum sem líta á hverja kóðabreytingu sem stýrðan atburð. Þú getur ekki einfaldlega endurskrifað bótakerfi borgara yfir langa helgi. Þú nútímavæðir það í litlum, afturkræfum, sönnunarbyggðum skrefum, sem er nákvæmlega það sem agaða endurbyggingin gefur þér. Að samhæfa þá vinnu yfir mörg teymi og langlíf kerfi (kafli 10.4) er ein af skilgreinandi áskorunum verkfræði í stórum stíl, og að fá hana rangt er hvernig skipulagsheildir enda frosnar, ófærar um að breyta hugbúnaði sem þær skilja ekki lengur.

## Meginreglur

- Endurbygging varðveitir hegðun. Ef þú ert að breyta því sem kóðinn gerir er það sérstök breyting, gerð sérstaklega.
- Áreiðanlegt prófasafn er forsenda öruggrar endurbyggingar, ekki valkvæð aukabúnaður.
- Vinndu í litlum, nefndum, afturkræfum skrefum og haltu kóðanum virkum eftir hvert.
- Gerðu tæknilega skuld sýnilega og rakta, fjármagnaðu síðan niðurgreiðslu sem stöðuga afkastagetu frekar en hetjudáðir.
- Endurbyggðu kóðann sem þú ert þegar að breyta, þar sem hreinsunin vinnur fyrir sér.
- Ekki er öll skuld þess virði að greiða. Stöðugum, sjaldan snertum eða brátt útleiddum kóða má sleppa.
- Mældu innri gæði til að upplýsa dómgreind, aldrei sem markmið til að spila með.

## Ráðleggingar

### Haltu endurbyggingu og hegðunarbreytingu stranglega aðskildum

Ákveddu áður en þú byrjar hvort þú ert að gera: og aldrei óskýra þetta tvennt í einu commit. Þegar þú endurbyggir verða prófin sem stóðust fyrir að standast eftir, óbreytt, því sýnileg hegðun hefur ekki hreyfst. Þegar þú breytir hegðun skaltu gera það sem eigið commit með eigin prófum. Ástæðan er hagnýt: ef blönduð breyting brýtur eitthvað geturðu ekki sagt hvort endurskipulagning þín kynnti gallann eða hegðunarbreyting þín, og í kóðarýni (kafli 2.5) getur rýnir ekki rökrætt um hvorn helming hreint. Venjan sem virkar er tveggja-hatta reglan frá Martin Fowler: þú ert alltaf með annaðhvort endurbyggingarhattinn eða eiginleikahattinn á höfðinu, þú veist hvorn og þú skiptir af ásetningi. Aðskilin commit gera líka [útgáfustýringar](https://en.wikipedia.org/wiki/Version_control)söguna læsilega, svo verkfræðingur sem helmingaleitar bilun geti sleppt hreinum endurbyggingar-commit af öryggi.

### Komdu á áreiðanlegu öryggisneti áður en þú endurskipuleggur

Endurbygging án prófa er bara breytingar og von. Áður en þú endurskipuleggur nokkuð afdrifaríkt þarftu safn sem þú treystir til að grípa hegðunarbreytingu ef þú veldur einni, sem er kjarnarök prófunarstefnu (kafli 2.4). Fyrir kóða sem þegar hefur góða þekju skaltu keyra prófin, endurbyggja í litlum skrefum og keyra þau aftur eftir hvert skref. Fyrir eldri kóða án prófa er heiðarlega hreyfingin að skrifa fyrst [lýsingarpróf](https://en.wikipedia.org/wiki/Characterization_test) (characterisation tests). Lýsingarpróf fullyrðir ekki hvað kóðinn ætti að gera. Það fangar hvað kóðinn gerir í raun núna, með öllum sérkennum sínum, svo hver breyting á hegðun birtist sem bilað próf. Michael Feathers gerði þessa nálgun vinsæla fyrir einmitt þær aðstæður sem stórar skipulagsheildir lifa í: kóði sem virkar, skiptir máli og hefur engin próf. Þegar núverandi hegðun er negld niður geturðu endurbyggt undir henni örugglega og aðeins þá breytt hegðun ofan á.

### Lærðu að þekkja kóðalykt og beittu litlum nefndum endurbyggingum

[Kóðalykt](https://en.wikipedia.org/wiki/Code_smell) er yfirborðsmerki um að eitthvað undir kunni að þurfa athygli: aðgerð sem hefur vaxið of löng, flokkur sem veit of mikið, tvítekin rökfræði, löng stikulista, nöfn sem ljúga um hvað þau gera. Lykt er vísbending, ekki dómur, svo þú rannsakar frekar en hlýðir blindandi. Viðbragðið er lítil, nefnd endurbygging úr skrá Fowlers: Extract Function, Rename Variable, Move Method, Replace Conditional with Polymorphism og tugir í viðbót. Gildi nefndra hreyfinga er að hver er lítil, skilin, vélrænt örugg og oft studd beint af IDE-inu þínu. Þú setur saman stórar umbætur úr mörgum örsmáum áreiðanlegum skrefum, heldur kóðanum grænum allan tímann, frekar en einu stóru stökki sem þú getur ekki sannreynt.

### Kjóstu tækifærisbundna endurbyggingu og taktu frá átök fyrir raunverulega byggingarþörf

Mest endurbygging ætti að vera tækifærisbundin, felld inn í vinnuna sem þú ert þegar að vinna. Skátareglan fangar það: skildu kóðann eftir örlítið hreinni en þú fannst hann. Þegar þú snertir skrá til að bæta við eiginleika eða laga galla skilurðu þegar það horn, og litlar hreinsanir þar safnast upp yfir tíma án þess að þurfa leyfi nokkurs eða sérstaka fjárhagsáætlun. Skipulögð endurbyggingarátök, þar sem teymi stöðvar eiginleikavinnu til að endurskipuleggja stórt svæði, eru stundum nauðsynleg, en þau eru dýr, erfið að tímasetja gegn vöruþrýstingi og áhættusöm ef svæðið er illa prófað. Taktu frá átök fyrir byggingarvandamál sem tækifærishreinsun nær ekki til og færðu rök með sönnunargögnum um breytingakostnaðinn sem þú ert að borga. Kjóstu stöðugan dropann af litlum hreinsunum. Hann er varanlegri en stöku hetjuleg endurskrif.

### Notaðu kyrkingarfíkjumynstrið fyrir stórar byggingarbreytingar

Þegar heilt undirkerfi þarf að skipta út skaltu ekki reyna stórhvells-endurskrif sem keyrir í ár og sameinast í lokin. Þannig deyja nútímavæðingarverkefni. Notaðu [kyrkingarfíkjumynstrið](https://en.wikipedia.org/wiki/Strangler_fig_pattern) (strangler fig), nefnt af Martin Fowler eftir vínviðnum sem vex í kringum tré og leysir það smám saman af hólmi. Þú setur framhlið fyrir framan gamla kerfið, beinir einni sneið af virkni í einu að nýjum kóða á bak við þá framhlið, sannreynir hana í framleiðslu og endurtekur þar til gamla kerfið er alveg umkringt og hægt er að fjarlægja það. Hver sneið er lítil, afhendanleg og afturkræf, svo áhættu er haldið afmarkaðri og virði berst stöðugt. Náskylt mynstur, branch by abstraction, gerir það sama innan eins kóðagrunns: þú kynnir ágripunarlag yfir það sem þú vilt skipta út, byggir nýju útfærsluna á bak við það meðan báðar sambúa, flytur neytendur smám saman yfir og eyðir gömlu útfærslunni þegar ekkert byggir lengur á henni. Hvort tveggja leyfir [eldra kerfi](https://en.wikipedia.org/wiki/Legacy_system) að þróast meðan það er lifandi, sem er eina tegund nútímavæðingar sem flestar stórar skipulagsheildir hafa í raun efni á.

### Líttu á tæknilega skuld sem eignasafn og gerðu hana sýnilega

Skuldalíkingin, mynduð af Ward Cunningham, aðskilur tvennt: höfuðstólinn (sóðalega kóðann eða flýtileiðina sjálfa) og vextina (aukafyrirhöfnina sem hver framtíðarbreyting borgar vegna hans). Ekki öll skuld er jöfn. Fjórðungatafla Fowlers flokkar hana eftir tveimur ásum: yfirveguð á móti óviljandi og skynsamleg á móti kæruleysisleg. Skynsamleg-yfirveguð skuld („við afhendum núna og hreinsum næsta sprett og við vitum kostnaðinn“) er lögmæt viðskiptaákvörðun. Kæruleysisleg-óviljandi skuld („hvað er hönnunarmynstur?“) er bara skaði. Stjórnunarverkið, sem tengist ákvarðanatöku og stjórnarháttum (kafli 1.5) og meðferð hennar á skuld sem eignasafni, er að gera skuldina sýnilega svo hægt sé að rökræða um hana: rektu mikilvæg atriði þar sem vinnan býr, merktu kóðann og skráðu vextina sem þú borgar svo niðurgreiðsla keppi um afkastagetu á sönnunargögnum en ekki þeim sem kvartar hæst. Skuld sem þú sérð ekki geturðu ekki stýrt.

### Fjármagnaðu niðurgreiðslu sem stöðuga afkastagetu, ekki hetjudáðir

Bilunarhátturinn er að líta á hreinsun sem eitthvað sem þú gerir „þegar hlutirnir róast“, sem er aldrei. Varanlega mynstrið er föst, vernduð afkastageta til niðurgreiðslu: skýr sneið af hverri lotu, eða varanlegt samkomulag um að hreinsun fylgi eiginleikavinnu á sama svæði. Það sem virkar ekki er stöku hetjusprettur þar sem einhver brennir helgi til að laga allt, því hann er ósjálfbær, órýndur og afturkallar sig venjulega. Stöðug afkastageta heldur vaxtagreiðslum niðri og forðast uppsveiflu-niðursveiflu hringinn þar sem skuld safnast þar til kreppa neyðir fram dýrt endurskrif. Þetta er stjórnunarskuldbinding jafnt og verkfræðivenja, og hún á heima í því hvernig þú skipuleggur hugbúnaðarviðhald (kafli 3.7) yfir líftíma kerfis.

### Mældu innri gæði en láttu mælikvarðann ekki verða markmiðið

Þú getur mælt innri gæði með merkjum eins og [hringflækju](https://en.wikipedia.org/wiki/Cyclomatic_complexity) (talning sjálfstæðra leiða gegnum aðgerð), tvítekningu, prófaþekju, bilanahlutfalli breytinga og hve langan tíma breytingar taka á svæðunum sem þú grunar. Þessar tölur eru gagnlegar til að koma auga á hvar skuld þéttist og til að fylgjast með þróun yfir tíma. Hættan er lögmál Goodharts: þegar mælikvarði verður markmið hættir hann að mæla nokkuð raunverulegt. Skyldaðu þekjutölu og þú færð próf sem fullyrða ekkert. Verðlaunaðu lág flækjustig og þú færð rökfræði smurða yfir fleiri aðgerðir til að sniðganga mælikvarðann. Notaðu mælikvarða til að hefja samtöl og staðsetja heita bletti, og tengdu aldrei gæðamælikvarða við hlið sem fólk er hvatt til að spila með.

### Vittu hvenær á ekki að endurbyggja

Endurbygging er fjárfesting og sumur kóði mun aldrei borga hana til baka. Ef eining er stöðug, sjaldan snert og skilin nógu vel til að breyta í þau fáu skipti sem þú verður, er að hreinsa hana fyrirhöfn eytt fyrir vexti sem þú varst ekki að borga. Ef kóði er á leið í lok líftíma er að endurbyggja hann að fægja eitthvað sem þú ert um það bil að henda. Agi er að eyða hreinsunarfjárhagsáætlun þinni þar sem breyting er tíð og sársaukafull, sem er þar sem að lækka vextina safnast í raun upp, og að skilja rólegu hornin í friði.

## Málamiðlanir: kostir og gallar

| Nálgun | Kostir | Gallar |
| --- | --- | --- |
| Tækifærisbundin endurbygging (skátareglan) | Ódýr, samfelld, engin sérstök fjárhagsáætlun, safnast upp yfir tíma | Ójöfn þekja, heitar skrár batna á meðan kaldar rotna |
| Skipulögð endurbyggingarátök | Lagar byggingarvandamál sem hreinsun nær ekki til | Dýr, keppir við eiginleika, áhættusöm án góðra prófa |
| Kyrkingarfíkja / branch by abstraction | Stigvaxandi, afturkræft, heldur kerfinu lifandi, afmarkar áhættu | Hægara en endurskrif á pappír, þarf aga til að ljúka |
| Stórhvells-endurskrif | Hrein skífa, engar eldri skorður | Hátt bilanahlutfall, langur tími til virðis, hegðunarbil |
| Yfirveguð skynsamleg skuld | Afhendir virði núna, skýr, skipulögð endurgreiðsla | Verður kæruleysisleg ef endurgreiðslan er aldrei tímasett |
| Mælikvarðahliðuð gæði | Hlutlæg, sýnileg, grípur rek snemma | Býður spilun heim, refsar blæbrigðum, getur rýrt raunveruleg gæði |

Meginspennan er hraði núna gegn breytanleika síðar og hún er raunveruleg. Að afhenda flýtileið getur verið rétt ákvörðun þegar fresturinn er raunverulegur og skuldin skynsamleg og rakin. Mistökin eru að þykjast að skuldin sé ókeypis, eða að láta hana safnast ósýnilega þar til kerfið er of dýrt til að breyta. Leystu það með því að gera skiptin skýr í hvert skipti: nefndu skuldina, áætlaðu vextina, ákveddu af ásetningi og skráðu ákvörðunina svo niðurgreiðslu megi tímasetja frekar en gleyma. Teymi sem tekur lán vitandi og greiðir jafnt og þétt helst hratt í ár. Teymi sem tekur lán blindandi malar til stöðvunar.

## Spurningar til að ræða með teyminu

1. **Hvernig komum við í veg fyrir að endurbygging og hegðunarbreyting blæði saman í sama commit og framfylgir rýni okkar því í raun?** Þetta er grunnagi alls kaflans og sá sem oftast er brotinn undir frestþrýstingi, því það finnst skilvirkt að „hreinsa þetta á meðan ég er hér“ og afhenda allt saman. Kostnaðurinn lendir síðar: þegar blandað commit brýtur framleiðslu getur enginn sagt hvort endurskipulagningin eða eiginleikinn olli því, og helmingaleit gegnum söguna þína hættir að vera áreiðanleg. Komdu með handfylli nýlegra sameiningarbeiðna og athugaðu heiðarlega hve margar blönduðu hattana tvo. Sjónarmiðið á móti er núningur, þar sem að skipta vinnu í aðskilin commit er örlítið meiri fyrirhöfn fyrirfram. Svarið ætti að móta commit-venjur þínar og rýnigátlista.

2. **Hvar er tæknilega skuldin okkar, hve mikla vexti borgum við af henni og hver ákveður hvað er greitt niður?** Flest teymi geta ekki svarað þessu, sem er raunverulega vandamálið, því skuld sem þú sérð ekki er stýrð af þeim sem kvartar hæst frekar en þar sem kostnaðurinn er í raun. Að gera hana sýnilega þýðir að rekja mikilvæg atriði, merkja kóðann og safna sönnunargögnum um hvaða svæði gera breytingar hægar og bilanagjarnar. Togið á móti er að hver klukkustund í niðurgreiðslu er klukkustund ekki varið í eiginleika sem forystan sér, svo ákvörðunin verður að vera eignasafnsákvörðun tekin með forystu, tengd því hvernig þú stýrir verkfræðivinnu (kafli 1.5). Komdu með bilanahlutfallsgögn breytinga þinna og lista yfir skrárnar sem allir óttast að snerta. Svarið ætti að verða að verndaðri, stöðugri niðurgreiðsluafkastagetu, ekki óljósum ásetningi um að hreinsa þegar hlutirnir róast.

3. **Hvaða hluta kóðagrunnsins ættum við vísvitandi ekki að endurbyggja og hvernig myndum við vita það?** Að endurbyggja allt er jafn mikil bilun og að endurbyggja ekkert, því fyrirhöfn sem fer í að hreinsa stöðugan, sjaldan snertan eða brátt útleiddan kóða eru vextir greiddir af láni sem þú skuldaðir ekki. Dómgreindarákvörðunin er raunveruleg: eining getur litið ljót út og samt verið rangur staður til að fjárfesta ef enginn breytir henni nokkurn tíma. Komdu með breytingatíðnigögn þín við hlið flækjumerkja þinna, því skurðpunktur hárrar veltu og mikillar flækju er þar sem hreinsun safnast upp, á meðan lítið-velta kóði er venjulega best látinn í friði. Áhættan á móti er að „við látum það vera“ verði afsökun til að snerta aldrei neitt erfitt. Svarið ætti að gefa þér skýran stuttlista yfir heita bletti sem vert er að fjárfesta í og leyfi til að hunsa rólegu hornin.

4. **Treystum við prófasafninu okkar nógu vel til að endurbyggja kóðann sem við þurfum helst að breyta og hvar þyrftum við að skrifa lýsingarpróf fyrst?** Öryggisnet sem þú getur ekki treyst breytir endurbyggingu í breytingar og von, og í stóru teymi er óttalegasti kóðinn venjulega minnst prófaði kóðinn, sem er einmitt þar sem hreinsun myndi borga sig mest. Komdu með þekju- og bilanahlutfallsgögn fyrir heita blettina þína og vertu heiðarlegur um hvaða mikilvægu einingar myndu gefa þér enga viðvörun ef endurskipulagning breytti hegðun. Sjónarmiðið á móti er að skrifa lýsingarpróf fyrir eldri kóða er hæg, óglæsileg vinna sem afhendir engan eiginleika, svo það er auðvelt að fresta að eilífu. Í fyrirtækja- og opinberum kerfum undir úttekt og breytingastýringu eru þessi niðurnegldu próf líka sönnunin um að breyting hafi varðveitt hegðun, svo að fjármagna þau er öryggisráðstöfun og regluvörsluráðstöfun í senn. Svarið ætti að nefna hvaða svæði fá prófabúnað áður en nokkur snertir þau.

5. **Þegar undirkerfi þarf í raun að skipta út, hvernig ákveðum við milli stigvaxandi kyrkingarfíkjuleiðar og endurskrifs, og hver hefur vald til að segja nei við endurskrifinu?** Stórhvells-endurskrif er hrífandi og bilanagjarnasti valkosturinn á borðinu, því hrein skífa lítur alltaf ódýrari út á pappír en að lifa með gömlu skorðunum. Fyrir stóra skipulagsheild heldur stigvaxandi leiðin (framhlið, ein sneið í einu, sannreynd í framleiðslu) kerfinu lifandi og afmarkar áhættu, en hún er hægari, krefst aga til að ljúka og keppir við lystina fyrir nýju upphafi. Komdu með breytingatíðnikort undirkerfisins, heiðarlegt mat á því hve lengi endurskrif myndi keyra áður en það skilaði virði og hegðunarbilin sem samhliða endurskrif þyrfti að loka. Í opinberu og eftirlitsskyldu umhverfi er margra ára endurskrif sem sameinast í lokin sjaldan lifanlegt undir úttekt, svo svarið ætti að sjálfgefa kyrkingarfíku eða branch by abstraction og líta á hvert endurskrif sem undantekningu sem verður að rökstyðja með sönnunargögnum.

6. **Hvernig notum við innri gæðamælikvarða til að finna hvar skuld þéttist án þess að leyfa tölu að verða markmið sem fólk spilar með?** Mælikvarðar eins og flækja, tvítekning, þekja og bilanahlutfall breytinga eru eina leiðin sem stór skipulagsheild getur séð yfir kóða sem enginn einn les, en um leið og einn er tengdur við hlið eða frammistöðumat tekur lögmál Goodharts við og talan hættir að mæla nokkuð raunverulegt. Komdu með dæmi um hvar mælikvarði knýr þegar hegðun og spurðu hvort hann sé að hefja samtöl eða hljóðlega verðlauna próf sem fullyrða ekkert og rökfræði smurða yfir aðgerðir til að sniðganga þröskuld. Togið á móti er að forystan vill einfalda mælaborðstölu, og „notaðu dómgreind“ er erfiðara að selja en grænn stika. Í fyrirtækja- og opinberu samhengi þar sem mælikvarðar næra stjórnarháttaskýrslugerð skaltu vera skýr um að gæðamerki upplýsa fjárfestingu og staðsetja heita bletti en hliða aldrei einstaklinga. Svarið ætti að draga fasta línu milli þess að mæla til að læra og að mæla til að dæma.

## Sjónarhorn eftir geirum

**Sprotafyrirtæki.** Með handfylli verkfræðinga og ekkert svigrúm skaltu endurbyggja aðeins tækifærisbundið: berðu einn hatt á commit svo sagan haldist helmingaleitanleg og haltu stuttum, heiðarlegum lista yfir flýtileiðirnar sem þú tókst vísvitandi. Farðu ekki í hreinsunarátök eða fægðu stöðugar einingar. Eyddu af skornum skammti athygli í skrána sem allir óttast og skrifaðu lýsingarpróf aðeins þar sem breyting hræðir þig í raun. Yfirveguð, sýnileg skuld er fín á þessu stigi. Kæruleysisleg, ósýnileg skuld er það sem drepur þig.

**Lítið fyrirtæki.** Án sérstaks vettvangs- eða verkfærasérfræðings og með þröngt fjárhagsáætlun skaltu hallast að því sem IDE-ið þitt og tungumálavistkerfi gefa þér ókeypis: sjálfvirkar endurnefningar- og útdráttarhreyfingar, lint-tól og grunnþekjumerki. Líttu á mestalla skuld sem eitthvað sem þú stýrir í venjulegri vinnu frekar en eitthvað sem þú ræður ráðgjafa til að laga og kjóstu að kaupa vel viðhaldin bókasöfn frekar en að smíða og þurfa síðan að endurbyggja þín eigin. Taktu frá sjaldgæfu greiddu fyrirhöfnina fyrir eina kerfið þar sem seinlæti kostar þig beint viðskiptavini.

**Stórfyrirtæki.** Yfir mörg teymi er vandinn eignasafnsstjórnarhættir: sameiginleg skuldaskrá, samræmd merking heitra bletta eftir breytingatíðni og flækju og vernduð sneið af afkastagetu hvers teymis til niðurgreiðslu svo hreinsun hætti að tapa fyrir eiginleikum sjálfgefið. Staðlaðu tveggja-hatta aga og lýsingarprófavenju svo hver verkfræðingur sem flytur milli teyma finni sömu reglur, og notaðu kyrkingarfíku og branch by abstraction fyrir byggingarbreytingar samhæfðar yfir hópa. Haltu gæðamælikvörðum upplýsandi svo þeir staðsetji skuld án þess að vera spilað með þá í frammistöðumötum.

**Hið opinbera.** Langlíf kerfi undir ströngum úttektar- og breytingastýringarreglum gera agaða endurbyggingu að regluvörslueign, ekki bara verkfræðieign: að halda endurskipulagningu stranglega aðskildri frá hegðunarbreytingu leyfir endurskoðendum að sjá nákvæmlega hvaða commit breyttu hegðun og hver bara tóku til. Innkaupa- og gagnsæisreglur hygla litlum, afturkræfum, sönnunarbyggðum skrefum fram yfir stórhvells-endurskrif, svo sjálfgefðu kyrkingarfíku með lýsingarprófum sem skjalfesta að hegðun sé varðveitt. Gerðu skuldaskrána og niðurgreiðsluáætlun hennar hluta viðhaldsskrár kerfisins svo eftirlitsstofnanir fái rekjanleikann sem þær krefjast.

## Dæmi

**Sprotafyrirtæki.** Sex manna sprotafyrirtæki afhendir hratt og veit að það tekur á sig skuld, svo það gerir tvennt ódýrt vel. Sérhver sameiningarbeiðni ber einn hatt: endurbyggingar-commit eru aðskilin eiginleika-commit, sem heldur sögu þeirra helmingaleitanlegri jafnvel á miklum hraða. Og þau halda stuttum, heiðarlegum lista yfir flýtileiðirnar sem þau tóku vísvitandi, með eins línu athugasemd um vextina sem hver kostar. Þegar greiðslueining verður skráin sem allir óttast gera sá listi og bilanasaga þeirra rökin fyrir að eyða tveimur dögum í að draga út hreinni mörk. Þau skrifa lýsingarpróf til að negla niður núverandi hegðun, endurbyggja undir með endurnefningar- og útdráttarhreyfingum IDE-sins og snerta aldrei stöðugu einingarnar sem enginn breytir. Skuldin sem þau bera er yfirveguð og sýnileg, svo hún verður aldrei kæruleysislega tegundin.

**Stórfyrirtæki.** Alþjóðlegt flutningafyrirtæki rekur fimmtán ára gamalt pöntunarkerfi sem mörg teymi breyta í hverri viku. Í stað endurskrifs taka þau upp kyrkingarfíkjumynstrið: framhlið situr fyrir framan einsteininn og ein afmörkuð geta í einu er endurbeint að nýjum þjónustum á bak við hana, sannreynd í framleiðslu áður en næsta sneið hefst. Að samhæfa þetta yfir teymi og langlíft kerfi (kafli 10.4) er erfiði hlutinn, svo þau viðhalda sameiginlegri skuldaskrá, merkja heita bletti eftir breytingatíðni og flækju og taka frá fasta sneið af afkastagetu hvers teymis til niðurgreiðslu. Innri gæðamælikvarðar upplýsa hvar á að leita en hliða aldrei frammistöðumat neins, sem heldur tölunum heiðarlegum. Á tveimur árum skreppur einsteinninn stöðugt saman og engin ein breyting teflir öllu kerfinu í tvísýnu.

**Hið opinbera.** Landsbundin skattstofnun þarf að nútímavæða áratuga gamlan álagningarvettvang undir ströngum úttektar- og breytingastýringarreglum, þar sem hver kóðabreyting er stýrður, sönnunarbyggður atburður. Stórhvells-endurskrif er ómögulegt, svo þau nota branch by abstraction: ágripunarlag er kynnt yfir eldri útreikningsvélina, ný útfærsla er byggð á bak við það og neytendur eru fluttir einn skattareglu í einu, hver flutningur skjalfestur sem lítil, afturkræf breyting með lýsingarprófum sem sanna að hegðun sé óbreytt. Því endurbygging er haldið stranglega aðskilinni frá hverri löggjafarhegðunarbreytingu geta endurskoðendur séð nákvæmlega hvaða commit breyttu hegðun og hver bara endurskipulögðu. Skuldaskráin og niðurgreiðsluáætlun hennar verða hluti viðhaldsskrár kerfisins (kafli 3.7) og gefa eftirlitsstofnunum rekjanleikann sem þær krefjast.

## Viðskiptarök: hvatar, ávöxtun fjárfestingar og heildarkostnaður

Ávöxtun endurbyggingar og skuldaniðurgreiðslu er viðvarandi geta til að breyta hugbúnaði ódýrt, og fyrir flest kerfi er meirihluti líftímakostnaðar viðhald, svo hér er heildareignarkostnaður að stórum hluta ákveðinn. Vextir af tæknilegri skuld eru greiddir í gjaldmiðlinum sem forystan fylgist þegar með: hægari afhending, hærra bilanahlutfall breytinga, lengri tími til endurheimtar eftir atvik og verkfræðingar sem forðast óttalegasta kóðann. Þegar þú gerir skuld sýnilega og fjármagnar niðurgreiðslu jafnt og þétt lækkarðu kostnað hverrar framtíðarbreytingar á svæðunum sem skipta mestu og forðast uppsveiflu-niðursveiflu mynstrið þar sem vanrækt skuld neyðir fram dýrt neyðarendurskrif.

Upptökukostnaðurinn er hóflegur og aðallega menningarlegur: komdu á tveggja-hatta agann, byggðu öryggisnetið þar sem þú þarft að endurbyggja, haltu skuldaskrá og verndaðu stöðuga sneið af afkastagetu til niðurgreiðslu. Kostnaður vanrækslu safnast hljóðlega upp. Vextir safnast á hverja breytingu þar til hraði hrynur og skipulagsheildin finnur sig frosna, ófæra um að breyta kerfi sem hún skilur ekki lengur örugglega, sem er dýrasta niðurstaðan af öllum. Til að færa rök við forystu skaltu tengja skuld beint við afhendingarmælikvarða sem hún lætur sig þegar varða og ramma niðurgreiðslu sem eignasafnsákvörðun með mælanlegum ávinningi, ekki sem verkfræðinga sem biðja um tíma til að taka til.

## Andmynstur og gildrur

- **Að blanda endurbyggingu við hegðunarbreytingu:** eitt commit gerir hvort tveggja, svo brot verður ekki eignað og saga verður óáreiðanleg.
- **Endurbygging án öryggisnets:** að endurskipuleggja óprófaðan kóða og vona, sem eru breytingar í trú.
- **Stórhvells-endurskrifið:** að skipta út virku kerfi allt í einu, mynstur með háu bilanahlutfalli og löngum tíma til virðis.
- **Endurbygging sem hetjuleg helgi:** órýnd, ósjálfbær hreinsun sem afturkallar sig í stað stöðugrar afkastagetu.
- **Ósýnileg skuld:** flýtileiðir sem enginn rekur, svo niðurgreiðsla er knúin af kvörtunarmagni frekar en raunverulegum kostnaði.
- **Að spila með gæðamælikvarða:** að ná þekju- eða flækjumarki á meðan raunveruleg gæði falla, því mælikvarðinn varð markmiðið.
- **Að endurbyggja rangan kóða:** að fægja stöðugar eða brátt útleiddar einingar á meðan raunverulegu heitu blettirnir halda áfram að kosta þig.
- **Eilíf endurbygging:** endalaus endurskipulagning sem afhendir aldrei virði, spegilmynd þess að hreinsa aldrei.

## Þroskalíkan

- **Stig 1, Upphaf:** Endurbygging er ad hoc og viðbragðsdrifin, oft blönduð hegðunarbreytingu í sama commit. Ekkert áreiðanlegt öryggisnet er til, tæknileg skuld er ósýnileg og órakin og hreinsun gerist aðeins í stökum hetjusprettum eða alls ekki.
- **Stig 2, Þróun:** Sum teymi aðskilja endurbyggingu frá hegðunarbreytingu og styðjast við próf þar sem þau eru til, og nefndar endurbyggingar og lýsingarpróf birtast í vösum. Vinnubrögð eru ósamkvæm milli teyma, skuld er rædd og stundum skráð og niðurgreiðsla keppir ad hoc gegn eiginleikum og tapar venjulega.
- **Stig 3, Stöðlun:** Tveggja-hatta agi, lýsingarpróf fyrir eldri kóða og litlar nefndar endurbyggingar eru skjalfest og vænt um alla skipulagsheildina. Skuld er rakin í sameiginlegri skrá sem aðskilur höfuðstól frá vöxtum og vernduð afkastageta til niðurgreiðslu er skipulögð í hverri lotu og framfylgt í rýni.
- **Stig 4, Stjórnun:** Skuld og hreinsun eru mæld og stýrð með gögnum gegn grunnlínum. Þú rekur breytingatíðni og flækju til að staðsetja heita bletti, fylgist með bilanahlutfalli breytinga og breytingaafhendingartíma á endurbyggðum svæðum og skráir vextina sem hvert mikilvægt atriði kostar, svo niðurgreiðsluákvarðanir hvíli á sönnunargögnum og drepa-eða-fjárfesta ákvarðanir séu teknar á þróun frekar en kvörtunarmagni. Gæðamerki upplýsa fjárfestingu án þess að vera tengd við hlið sem fólk getur spilað með.
- **Stig 5, Samhæfing:** Skuld er stýrð sem stöðugt endurjafnað eignasafn samþætt vöru- og viðhaldsáætlun yfir alla skipulagsheildina. Byggingarbreyting notar venjulega kyrkingarfíku og branch by abstraction samhæfð yfir teymi, niðurgreiðsla er samfelld og samsvarar því hvar breyting er tíð og sársaukafull og vinnubrögðin aðlagast eftir því sem kerfið og áhættumynd þess breytast, svo langlífur kóði haldist breytanlegur áratugum saman.

## Hugmyndir til umræðu

1. Hver er raunveruleg, framfylgd regla teymisins þíns um að halda endurbyggingu aðskildri frá hegðunarbreytingu og hvar brotnar hún undir frestþrýstingi?
2. Hvernig ákveðurðu, með sönnunargögnum, hvaða kóði verðskuldar hreinsun og hver er best látinn í friði?
3. Hvar myndu lýsingarpróf leyfa þér að endurbyggja örugglega eldra svæði sem þú forðast í dag?
4. Fyrir næstu stóru nútímavæðingu þína, hvernig myndi kyrkingarfíkjuleið líta út og hvaða framhlið eða ágripun myndirðu kynna fyrst?
5. Hver á tæknilegu skuldaskrána og hvernig vinnur niðurgreiðsla í raun afkastagetu gegn eiginleikavinnu?

## Helstu atriði

- Endurbygging varðveitir hegðun. Haltu henni stranglega aðskildri frá hegðunarbreytingu, í aðskildum commit.
- Áreiðanlegt prófasafn er forsenda öruggrar endurbyggingar, og lýsingarpróf gefa eldri kóða eitt.
- Vinndu í litlum, nefndum, afturkræfum skrefum, kjóstu tækifærisbundna hreinsun og notaðu kyrkingarfíku eða branch by abstraction fyrir stórar byggingarbreytingar.
- Gerðu tæknilega skuld sýnilega, aðskildu höfuðstól frá vöxtum og fjármagnaðu niðurgreiðslu sem stöðuga afkastagetu frekar en hetjudáðir.
- Mældu innri gæði til að leiða dómgreind, aldrei sem markmið til að spila með, og endurbyggðu ekki kóða sem er stöðugur eða á leið í lok líftíma.

## Heimildir og frekari lestur

- Martin Fowler, *Refactoring: Improving the Design of Existing Code*, second edition
- Michael Feathers, *Working Effectively with Legacy Code*
- Ward Cunningham, *The WyCash Portfolio Management System* (OOPSLA 1992 experience report, origin of the debt metaphor)
- Martin Fowler, "TechnicalDebtQuadrant" and "StranglerFigApplication" (martinfowler.com)
- Kent Beck, *Tidy First? A Personal Exercise in Empirical Software Design*
- Steve McConnell, *Code Complete: A Practical Handbook of Software Construction*
- Robert C. Martin, *Clean Code: A Handbook of Agile Software Craftsmanship*
