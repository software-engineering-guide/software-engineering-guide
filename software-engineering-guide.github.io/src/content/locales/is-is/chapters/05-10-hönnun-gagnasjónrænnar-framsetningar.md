# 5.10 Hönnun gagnasjónrænnar framsetningar

## Yfirlit og tilgangur

Graf er röksemd gerð úr bleki. Þegar þú teiknar gögn velurðu hvað lesandinn tekur fyrst eftir, hvað hann ber saman og hvaða niðurstöðu hann dregur á þeim tveimur sekúndum áður en hann heldur áfram. Gerðu það vel og erfið spurning svarar sér sjálf: þróunin er augljós, frávikið stekkur fram, hóparnir tveir eru greinilega ólíkir. Gerðu það illa og sömu gögnin villa um, rugla eða bara leiðast, og ákvörðunin sem þau áttu að upplýsa er tekin á tilfinningu. [Gagnasýn](https://en.wikipedia.org/wiki/Data_and_information_visualization) er hönnunarhandverkið að breyta tölum í myndir sem leyfa fólki að sjá hvað tölurnar þýða.

Þessi kafli fjallar um það handverk: að velja rétta grafið, kóða gögn heiðarlega, nota liti og uppsetningu svo augað lendi þar sem það á að lenda og halda öllu aðgengilegu. Hann á heima í 5. hluta því graf er viðmót og erfir allt frá restinni af hlutanum. Hann byggir á grunni [notendaupplifunar](https://en.wikipedia.org/wiki/User_experience) úr kafla 5.1, fær hönnunartákn og íhluti úr hönnunarkerfum kafla 5.2, verður að uppfylla aðgengisskyldurnar í kafla 5.3 og talar í skýrri, markvissri rödd efnishönnunar kafla 5.4. Hann heldur sér viljandi frá lagnavinnunni. Gagnaleiðslur, gagnavöruhús og skýrslutól greiningar og viðskiptagreindar (kafli 7.3) eru annað efni, eins og víðtækari ákvörðunarfræði og gagnamenning kafla 7.5. Hér lærirðu að gera myndina góða, sama hvaðan gögnin koma.

Fyrir stór teymi snýst það sem er í húfi um samræmingu og traust. Þegar hvert teymi stílar sín eigin graf endar fyrirtæki með fimmtíu mállýskur af „tekjur yfir tíma“, hver með ólíkum ásum, litum og námundun, og stjórnendur læra að vantreysta þeim öllum. Í fyrirtækjum knýr villandi mælaborð raunverulegt fjármagn í ranga átt. Hjá hinu opinbera er opinbert graf samskipti við borgara og snertir hagsmunaaðilasamskiptin í kafla 10.16: stytt ás á lýðheilsumynd getur skapað ofsahræðslu eða fölsk huggun fyrir milljónir, og aðgengi er lagaskylda, ekki val. Góð sjónræn gagnahönnun er leiðin til að gögn vinni sér rétt til að vera trúað.

## Meginreglur

- Byrjaðu á spurningu lesandans, veldu síðan grafið sem svarar henni.
- Láttu sjónkóðun samsvara gagnagerð: staða fyrir nákvæman samanburð, litblær fyrir flokka.
- Hámarkaðu hlutfall bleks sem ber gögn. Eyddu skreytingu sem ber engin.
- Notaðu forathyglieiginleika af ásetningi svo augað lendi fyrst á punktinum.
- Veldu litapallettur eftir hlutverki gagna (raðbundin, ósamstæð, flokkandi) og hafðu þær öruggar fyrir litblinda.
- Reiddu þig aldrei á lit einan. Útvegaðu texta, uppbyggingu og töfluvara.
- Segðu sannleikann um kvarða: engir styttir ásar, engin villandi svæði, enginn óþarfur tvöfaldur ás.
- Skýrðu innsýnina. Láttu lesandann ekki leita að henni.

## Ráðleggingar

### Byrjaðu á spurningunni, veldu síðan grafið

Hvert gott graf byrjar á spurningu, ekki gagnasafni. Áður en þú nærð í grafgerð skaltu nefna spurningu lesandans í einni setningu og para hana við verk. Samanburður („hvort er stærra?“) vill [súlurit](https://en.wikipedia.org/wiki/Bar_chart), þar sem lengdir sitja á sameiginlegri grunnlínu og augað raðar þeim fyrirhafnarlaust. Þróun yfir tíma („hvert stefnir þetta?“) vill [línurit](https://en.wikipedia.org/wiki/Line_chart), því samfelld lína les sem samfelld breyting. Dreifing („hvernig dreifist þetta?“) vill stöplarit eða kassarit, sem sýna lögun, miðju og frávik. Hluti af heild („hver er hlutur hvers hluta?“) er yfirleitt betur þjónað af staflaðri súlu en kökuriti, því fólk ber saman lengdir miklu nákvæmar en horn. Taktu frá [kökuritið](https://en.wikipedia.org/wiki/Pie_chart) fyrir tvær eða þrjár sneiðar þar sem skiptingin er öll sagan. Samband („hreyfast þessi tvö saman?“) vill [dreifirit](https://en.wikipedia.org/wiki/Scatter_plot), eina grafið sem afhjúpar fylgni og þyrpingar í fljótu bragði.

Agi felst í að láta spurninguna velja grafið, aldrei öfugt. Grafgerð valin því hún lítur áhrifamikil út (þrívítt sprengt kökurit, radarrit, kleinuhringur með tölu í gatinu) er ákvörðun tekin fyrir hönnuðinn, ekki lesandann. Þegar tafla myndi svara spurningunni hraðar (lesandi sem þarf nákvæmar tölur fyrir fjórar raðir þarf alls ekkert graf) skaltu nota töfluna. Graf er aðeins réttlætanlegt þegar mynd afhjúpar mynstur sem tölustafir í reit myndu fela.

### Láttu sjónkóðun samsvara gögnunum

Graf virkar með því að varpa gögnum á sjónræna eiginleika, og þeir eiginleikar eru ekki jafnir. Áratugir skynjunarrannsókna raða þeim. Staða eftir sameiginlegum kvarða er nákvæmasta rás sem menn hafa, og þess vegna slá súlur og punktar á sameiginlegum ás allt annað í samanburði. Lengd kemur næst, síðan horn og halli, síðan flatarmál, síðan litstyrkur og loks litblær, sem er nánast gagnslaus til að meta magn en frábær til að merkja flokka. Eyddu nákvæmustu rás þinni í mikilvægasta magnið.

Láttu rásina líka samsvara gagnagerðinni. Megindleg gögn (fjöldi, upphæðir, tímalengdir) eiga heima á stöðu, lengd eða raðbundnum litaferli. Raðgögn (lítið, miðlungs, stórt) geta notað raðaða stærð eða ljós-til-dökkt ferli. Flokkagögn (svæði, vörulína, flokkur) eiga heima á litblæ eða lögun, aldrei á stærð sem gefur til kynna að einn flokkur sé „meira“ en annar. Klassísku mistökin eru að kóða flokk sem regnboga svo auga lesandans finni upp röð sem gögnin hafa ekki. Kóðaðu magn þar sem augað les magn og auðkenni þar sem augað les auðkenni.

### Stefndu að grafískum ágæti: hámarkaðu gagnableksmagn

Edward Tufte gaf gagnasýn skýrustu hönnunarsiðfræðina og hana er vert að tileinka sér. Meginmælikvarði hans er [gagnablekshlutfallið](https://en.wikipedia.org/wiki/Data-ink_ratio): af öllu blekinu (eða mynddílunum) á síðunni, hvaða brot kóðar í raun gögn? Allt annað (þungar hjálparlínur, ramma, skuggar, bakgrunnsfyllingar, óþarfar skýringar, skrautleg þrívídd) er skattur á athygli lesandans. Tufte kallar þessa skreytingu grafrusl og fyrirmælin eru blátt áfram: eyddu því. Léttu hjálparlínur þar til þær hvísla, slepptu rammanum, merktu gögn beint í stað þess að þvinga ferð í skýringu og leyfðu gögnunum að standa nánast ein. Graf er fullbúið ekki þegar engu er eftir að bæta heldur þegar engu er eftir að fjarlægja án þess að missa merkingu.

Ein hugmynd Tufte á skilið sérstaka umfjöllun fyrir teymi: smáfjöldaritum. Í stað þess að troða átta röðum í eitt flækt línurit skaltu teikna átta lítil graf í ristu, hvert með sömu ásum og kvarða, eitt á hverja röð. Augað skannar ristina og sér þann skrýtna samstundis, því hver reitur er beint sambærilegur. Smáfjöldarit breytir „of margar línur til að lesa“ í „síðu sem þú getur flett“, og hún stigvaxar langtum betur en að hlaða fleiri litum og fleiri skýringarfærslum á eitt ofhlaðið línurit.

### Notaðu forathyglieiginleika og sjónræna stigskiptingu

Sumir sjónrænir munir skráast áður en meðvituð athygli kemur til, á broti úr sekúndu, án þess að lesandinn „leiti að þeim“. Þessir forathyglieiginleikar (einn rauður punktur meðal grárra, ein lengri súla, eitt atriði sett í sundur í rými) eru öflugasta tólið sem þú átt til að beina auganu. Notaðu þá af ásetningi. Ef punktur grafsins er að eitt svæði er að dragast aftur úr skaltu lita það svæði og gráa hin. Lesandinn sér skilaboðin áður en hann les titilinn. Ef allt er bjart og feitletrað er ekkert það, því birtuskil eru afstæð og síða af áherslu er síða af hávaða.

Þetta er sjónræn stigskipting beitt á gögn: ákveddu eitt atriðið sem lesandinn á að taka fyrst eftir og eyddu sterkasta merkinu þar. Titill og skýring segja niðurstöðuna í orðum. Litur og þyngd benda á sönnunargögnin. Allt stuðningsefni (ásar, hjálparlínur, aukaraðir) hörfar í grátt svo forgrunnurinn geti talað. Graf án stigskiptingar biður lesandann að vinna verk hönnuðarins við að finna út hvað skiptir máli.

### Veldu lit eftir hlutverki og hafðu hann öruggan fyrir litblinda

Litur er rásin sem oftast er misnotuð, svo meðhöndlaðu hann sem kerfi með þremur fjölskyldum. Raðbundin pallettan fer frá ljósu til dökks í einum litblæ og kóðar magn sem fer frá lágu til háu (þéttleiki íbúa, tekjur). Ósamstæð pallettan hefur tvo litbrigði sem mætast á hlutlausum miðpunkti og kóðar frávik frá miðju (hitafrávik, hagnaður og tap í kringum núll, samsinning í könnun í kringum hlutlaust). Flokkandi pallettan er mengi ólíkra litblæja til að merkja hópa án raðar. Haltu henni við um sjö liti, því umfram það getur lesandinn ekki greint þá í sundur. Að velja ranga fjölskyldu (flokkandi regnboga fyrir magn, raðbundið ferli fyrir óröðuð flokka) berst gegn skynjun lesandans.

Gerðu hann svo aðgengilegan, því um það bil einn af hverjum tólf körlum hefur einhverja mynd af [litblindu](https://en.wikipedia.org/wiki/Color_blindness). Rautt og grænt er klassíska gildran: graf með rauðu sem slæmu og grænu sem góðu er ósýnilegt algengustu skerðingunni. Veldu pallettur öruggar fyrir litblinda (bláar-í-appelsínugular ósamstæðar myndir og vel prófuð flokkandi mengi úr verkfærum eins og ColorBrewer eru öruggir upphafspunktar) og staðfestu með því að herma algengar skerðingar áður en þú afhendir. Athugaðu líka birtuskil, svo texti og merki uppfylli hlutföllin sem aðgengisstaðlarnir í kafla 5.3 krefjast. Litur ætti að styrkja skilaboð sem lifa af án hans.

### Reiddu þig ekki á lit einan. Útvegaðu valkosti

Aðgengi í gagnasýn nær lengra en val á pallettu. Kjarnareglan úr [Web Content Accessibility Guidelines](https://en.wikipedia.org/wiki/Web_Content_Accessibility_Guidelines) (WCAG) er að litur má aldrei vera eina leiðin til að miðla upplýsingum. Paraðu því lit við annað merki: bein merki, ólík form eða tákn á dreifiriti, ólíkir línustílar (heil, strikuð) á línuriti eða textamerki á mikilvægu súlunni. Lesandi sem getur ekki greint litblæi þína ætti samt að fá full skilaboð úr afritaðri kóðun.

Útvegaðu raunverulegan textavalkost og varaleið. Grafmynd þarf alt-texta sem segir niðurstöðuna, ekki „graf af sölu“, og lengri lýsingu eða myndatexta sem nefnir þróunina. Þar sem hagnýtt er skaltu bjóða undirliggjandi gögn sem aðgengilega töflu, svo skjálesaranotandi og töflureiknisþenkjandi greinandi fái báðir tölurnar beint. Þetta endurspeglar „leystu það einu sinni í íhlut“ agann úr kafla 5.2: byggðu aðgengilega grafíhluti með réttum hlutverkum, lyklaborðsfókus fyrir gagnvirka þætti og töfluskoðun innbyggða, svo hvert teymi erfi aðgengi frekar en að finna það upp á hverju mælaborði.

### Veistu hvort þú ert að kanna, útskýra eða vakta

Graf þjóna þremur ólíkum störfum og að rugla þeim framleiðir slæma vinnu. Könnunarsýn er fyrir þig, greinandann, að leita í gögnum að því áhugaverða. Hún má vera hröð, þétt og ljót, því áhorfandinn er einn sérfræðingur sem mun endurtaka. Útskýringarsýn er fyrir áheyrendur, að miðla tiltekinni niðurstöðu sem þú skilur þegar. Hún er yfirveguð, skýrð og afklædd að einum skilaboðum, og hún tilheyrir frásögn kafla 10.16. Mælaborð er þriðji hluturinn: viðvarandi, skimanlegur skjár til að vakta þekkta mælikvarða yfir tíma, fínstilltur fyrir „er eitthvað að núna?“ frekar en einstaka röksemd.

Láttu hönnunina passa við starfið. Útskýringargraf með fyrirsögn og einni auðkenndri röð er rangt fyrir vöktunarmælaborð, þar sem lesandinn þarf marga mælikvarða í fljótu bragði og samræmda staðsetningu svo augað læri uppsetninguna. Mælaborð troðið frásagnarskýringum er þreytandi að athuga á hverjum morgni. Og könnunarminnisbók full af hráum dreifiritum ætti aldrei að rétta stjórnanda eins og hún væri útskýring. Ákveddu starfið fyrst. Hönnunin fylgir.

### Villtu aldrei um fyrir lesandanum: heiðarlegir kvarðar, heiðarleg svæði

Fljótlegasta leiðin til að eyðileggja traust er graf sem lýgur á meðan það lítur sannleikssamlega út. Algengasta lygin er stytti ásinn: að byrja y-ás súlurits á 90 í stað 0 breytir 2% mun í hamar, því súlulengd varpast ekki lengur á gildi. Súlur verða að byrja á núlli, alltaf. Línurit, sem kóða breytingu frekar en stærð, mega nota grunnlínu sem er ekki núll ef þú merkir hana skýrt. Önnur gildra er tvöfaldi ásinn: tveir y-kvarðar á einu grafi leyfa þér að framleiða hvaða fylgni sem þú vilt með því að renna kvörðunum, og lesendur taka sjaldan eftir því. Kjóstu tvö samstillt graf eða vísitölusýn í staðinn. Þriðja er villandi flatarmál: þegar þú kvarðar tákn eða kúlu bæði eftir breidd og hæð til að tákna gildi vex flatarmálið sem ferningur og ofmetur muninn gífurlega. Kvarðaðu eftir flatarmáli, ekki hliðarlengd.

Meðhöndlaðu þetta sem heilindareglur, ekki stílval. Graf er fullyrðing sem þú biður lesandann að treysta og hver þessara bjaganna nýtir hvernig skynjun virkar til að láta lítinn hlut líta stóran út eða ótengdan hlut líta tengdan. Dæmin um hið opinbera og fyrirtæki hér á eftir sýna hve dýrt það svik verður þegar áheyrendur eru almenningur eða stjórn.

### Skýrðu innsýnina og bættu við gagnvirkni af hófsemi

Graf sem lætur lesandann finna punktinn er hálfklárað. Skýrðu það: titill sem segir niðurstöðuna („Nýskráningar tvöfölduðust eftir marsopnunina“) frekar en efnið („Nýskráningar yfir tíma“), útkall á lykilatburðinum, viðmiðunarlína fyrir markmiðið eða meðaltalið. Skýring er þar sem hönnunin í kafla 5.4 mætir myndinni. Orðin bera röksemdina og merkin veita sönnunina.

Gagnvirkni vinnur sér aðeins sæti þegar hún svarar raunverulegri eftirfylgnispurningu. Vísbendingar fyrir nákvæm gildi, síun á hluta og borun niður í smáatriði hjálpa allt þegar lesandinn á næstu spurningu sem kyrrstætt graf rúmar ekki. En gagnvirkni er kostnaður: hún felur upplýsingar á bak við sveim, bregst á snertingu og fyrir lyklaborðsnotendur og getur dregið afköst niður í skriðhraða. Á vefnum skaltu fylgjast með birtingarfjárhagsáætluninni úr kafla 5.6: tugþúsundir punkta vilja striga eða samantekna sýn, ekki tugþúsundir stakra skjalaþátta. Láttu sjálfgefnu, kyrrstæðu sýnina segja alla kjarnasöguna og láttu gagnvirkni afhjúpa dýptina undir.

## Málamiðlanir: kostir og gallar

| Ákvörðun | Kostir | Gallar |
|---|---|---|
| Smíða sýn í vörunni | Full stjórn á hönnun, aðgengi, gagnvirkni | Kostar verkfræðitíma. Þú átt afköst og viðhald |
| Nota graf viðskiptagreindartóls | Hröð, ódýr, tengd við vöruhúsið | Almennt útlit. Takmörkuð aðgengis- og skýringarstjórn |
| Gagnvirk graf | Svarar eftirfylgnispurningum. Kanna á staðnum | Hægari, erfiðari að gera aðgengileg, bregðast á prenti og snertingu |
| Kyrrstæð graf | Hröð, aðgengileg, prentklár, ótvíræð | Geta ekki svarað næstu spurningu lesandans |
| Mælaborð | Skimanleg vöktun margra þekktra mælikvarða | Slæmt fyrir einstaka röksemd. Freistar til mælikvarðaofvaxtar |
| Útskýringargraf | Skilar einum skilaboðum af krafti | Rangt fyrir vöktun eða opna könnun |
| Rík litanotkun og áhrif | Augnfangandi. Finnst fágað | Grafrusl. Skaðar gagnablekshlutfall og aðgengi |

Endurtekna spennan er tjáningarmáttur gegn heiðarleika og skýrleika. Sérhver eiginleiki sem gerir graf ríkara (annar ás, litstigull, þrívíddarsjónarhorn, hreyfimynd) bætir líka við leið til að villa um eða grafa punktinn. Leystu það með því að sjálfgefa minna: einfaldasta grafið sem svarar spurningunni, í fæstum litum, með kvarðanum sem segir sannleikann. Bættu aðeins við tjáningarmætti þegar tiltekin spurning lesanda krefst þess og borgaðu aðgengis- og afkastakostnaðinn meðvitað. Hin viðvarandi málamiðlunin er smíða gegn kaupa. Viðskiptagreindartól kemur grafi á skjá á mínútum og er rétt val fyrir innri vöktun. Sýn felld inn í viðskiptavinasnúna vöru þarf yfirleitt hönnunar-, aðgengis- og afkastastjórnunina sem aðeins sérsmíðaður íhlutur gefur.

## Spurningar til að ræða með teyminu

1. **Deila graf okkar einu sjónrænu máli eða finnur hvert teymi upp sitt eigið?** Þegar hvert teymi velur eigin liti, ásavenjur, námundun og grafgerðir safnar skipulagsheildin mállýskum sem grafa hljóðlega undan trausti: tvö mælaborð sem sýna „virka notendur“ með ólíkum kvörðum og ólíkum grænum kenna stjórnendum að ekki sé hægt að treysta gögnunum. Komdu með þrjú graf af sama mælikvarða frá þremur teymum og leggðu hlið við hlið. Bilin sem þú finnur (styttur ás hér, regnbogi flokka þar, tekjur í þúsundum á einu og milljónum á öðru) eru rökin fyrir sameiginlegu grafíhlutasafni með samþykktum pallettum, sjálfgefnum ásareglum og innbyggðu aðgengi, stýrt eins og hönnunarkerfið í kafla 5.2. Markmiðið er að hvert graf í fyrirtækinu lesist rétt við fyrstu sýn, því málfræðin er sameiginleg.

2. **Myndu mikilvægustu graf okkar lifa af litblindan lesanda og skjálesara?** Aðgengi í gagnasýn er auðvelt að sleppa því grafin líta enn vel út fyrir fólkið sem smíðaði þau, og það er nákvæmlega gildran. Taktu þrjú graf sem stjórnendur þínir sjá oftast og keyrðu þau gegnum litblindnihermi, reyndu síðan að skilja þau með slökkt á skjánum, aðeins með alt-textanum og töfluvaranum. Ef rauð-græn stöðumynd flatnar út, ef alt-textinn segir „graf“ og ekkert meira, eða ef engin leið er að ná undirliggjandi tölum án músar, hefurðu fundið hóp lesenda sem þú útilokar nú, sem í opinberri vinnu er lagaleg útsetning undir stöðlunum í kafla 5.3. Ákveddu hver á að laga það og hvort lagfæringin eigi heima í sameiginlegum íhlut svo hún sé leyst einu sinni.

3. **Getum við fyrir hvert graf sem knýr ákvörðun bent á spurninguna sem það svarar og staðfest að það villi ekki um?** Mörg graf eru til því einhver gerði þau einu sinni, ekki því þau svara lifandi spurningu, og sum mest vöktuðu bjaga kvarða án þess að nokkur taki eftir. Gakktu gegnum grafin á helstu mælaborðum þínum og nefndu fyrir hvert ákvörðunina sem það upplýsir og athugaðu heilindi þess: súlur frá núlli, enginn óþarfur tvöfaldur ás, svæði kvörðuð heiðarlega, titill sem segir niðurstöðu frekar en efni. Grafin sem svara engri núverandi spurningu eru frambjóðendur til eyðingar og þau sem villa um eru frambjóðendur til brýnnar viðgerðar, því graf sem hljóðlega ofmetur mun er verra en ekkert graf. Þetta tengist beint ákvörðunarmenningu kafla 7.5: teymi sem treystir grafum sínum tekur hraðari, betur rökstuddar ákvarðanir.

4. **Þegar teymi þarf graf, náum við fyrst í innbyggð graf viðskiptagreindartólsins eða í stýrt íhlutasafn og hver ákveður hvort?** Togið í átt að viðskiptagreindartólinu er raunverulegt: það er hratt, ódýrt og þegar tengt við vöruhúsið, svo flest vöktunarmælaborð eiga heima þar. En almennir sjálfgefnir valkostir þess eru þar sem mállýskur og grafrusl læðast inn og aðgengis- og skýringarstýringar þess eru yfirleitt veikar, sem skiptir mestu fyrir viðskiptavinasnúin og opinber graf sem bera orðspor þitt. Fyrir stóra skipulagsheild er hættan að sjálfgefna valið sé aldrei ákveðið, svo hvert teymi rekur til þess sem er auðveldast og landareignin sundrast. Komdu með skrá yfir hvar graf eru í raun smíðuð í dag, nokkur hlið-við-hlið dæmi úr viðskiptagreindartólinu á móti sérsmíðuðum íhlut og aðgengisbilin í hvoru. Í fyrirtækja- og opinberu umhverfi skaltu fella inn innkaupaveruleikann: þú ert oft læst á einn viðskiptagreindarvettvang árum saman, svo vittu nákvæmlega hvaða graf hann getur birt heiðarlega og aðgengilega og hver þurfa stýrðan íhlut, fyrir samninginn, ekki eftir.

5. **Hver má birta graf fyrir ytri eða stjórnendaáheyrendur og hvaða rýni fer það í gegnum fyrst?** Sjálfsafgreiðslugreining er raunverulegt gott, en hún þýðir að villandi graf getur náð til stjórnar eða almennings án annarra augna, og styttur ás eða ómerktur broddur á opinberri mynd er langtum erfiðara að afturkalla en að koma í veg fyrir. Spennan er hraði og sjálfræði gegn heilindum og trausti: lokaðu of fast og fólk fer framhjá þér, lokaðu of lítið og þú sendir grafið sem skapar skelfingu á markaði eða meðal kjósenda. Komdu með núverandi útgáfuleið mest sýnilegu grafa þinna, dæmi sem náðu til ytri áheyrenda án rýni og sönnunargögn um hvort aðferð og óvissa sé skýrð á grafinu sjálfu. Í opinberri og regluverkuðum vinnu er þetta brýnt: opinber tölfræði eru samskipti við borgara og snerta hagsmunaaðilatraustið í kafla 10.16, svo nefndu hver samþykkir, hvaða heilinda- og aðgengislista hann beitir og hvar ábyrgðin liggur þegar graf villir um.

6. **Hvar höfum við bætt við gagnvirkni og segir sjálfgefna kyrrstæða sýnin enn alla söguna án músar?** Gagnvirkni er tælandi og dýr: hún felur gildi á bak við sveim, bregst á snertingu og fyrir lyklaborðsnotendur og getur dregið birtingarfjárhagsáætlun niður í skriðhraða á stórum gagnasöfnum, eins og kafli 5.6 varar við. Sjónarmiðið á móti er að raunveruleg eftirfylgnispurning (nákvæmt gildi, borun niður, síaður hluti) er stundum kostnaðarins virði, svo markmiðið er hófsemi frekar en bann. Komdu með listann yfir gagnvirk graf sem þú afhendir, niðurstöður þess að prófa hvert með músina fjarri og á síma og afkastatölurnar þegar gögnin vaxa í tugþúsundir punkta. Fyrir fyrirtækja- og opinber áheyrendur er aðgengishliðin lagaskylda undir stöðlunum í kafla 5.3, og graf eru lesin á söluturnum, útprentunum og hjálpartækni, svo kyrrstæða, skýrða sjálfgefna sýnin þarf að bera kjarnaskilaboðin og gagnvirkni getur aðeins bætt dýpt undir.

## Sjónarhorn eftir geirum

**Sprotafyrirtæki.** Hraði vinnur, svo hallaðu þér að grafunum sem eru þegar í viðskiptagreindartólinu þínu eða léttu grafasafni frekar en að smíða íhlutalandareign sem þú getur ekki mannað. Eina ódýra ákvörðunin sem borgar sig síðar er að velja eina litblindaörugga pallettu og venjuna súlur-frá-núlli á degi eitt, svo þú safnir ekki tylft mállýskna af sama mælikvarða áður en þú átt tíu viðskiptavini. Kjóstu kyrrstætt, skýrt graf sem segir niðurstöðu sína fram yfir gagnvirkt sem þú munt ekki hafa tíma til að gera aðgengilegt.

**Lítið fyrirtæki.** Án gagnasérfræðings og með þröngt fjárhagsáætlun skaltu líta á sjónræna framsetningu sem eitthvað sem þú færð úr verkfærum sem þú borgar þegar fyrir: töflureikninn, greiningarþjónustuna, mælaborðið í viðskiptavinakerfinu. Lærðu fáu heilindareglurnar sem skipta máli (súlur byrja á núlli, enginn regnbogi fyrir magn, engin kaka með níu sneiðum) og beittu tilbúinni litblindaöruggri pallettu frekar en að panta sérsmíðaða. Keyptu grafið, smíðaðu það ekki, og taktu frá athyglina fyrir að lesa það rétt.

**Stórfyrirtæki.** Vandinn er samræmi yfir mörg teymi, svo stýrðu sjónrænni framsetningu eins og hönnunarkerfi: sameiginlegt grafíhlutasafn með samþykktum raðbundnum, ósamstæðum og flokkandi pallettum, heiðarlegum ásasjálfgefnum, stöðluðu tölusniði og innbyggðu aðgengi. Framfylgdu því með sjónrænum afturfaraprófunum og heilindaathugunum í afhendingarleiðslu kafla 8.1, svo graf sem styttir ás eða fellur á birtuskilum sé stöðvað áður en það fer í loftið. Ávinningurinn er að graf frá hvaða teymi sem er lesist rétt við fyrstu sýn og stjórnendur hætta að spyrja hvaða útgáfu af tölu eigi að trúa.

**Hið opinbera.** Hvert opinbert graf eru samskipti og háð opinberri ábyrgð, svo heiðarlegir kvarðar og WCAG-aðgengi eru skyldur, ekki val. Skyldaðu súlur frá núlli, flatarmál kóðað með flatarmáli, litblindaöruggar pallettur, einfalda titla sem segja niðurstöðuna og niðurhlaðanlega aðgengilega töflu við hlið hvers grafs. Skýrðu aðferð og óvissu á grafinu sjálfu svo umdeild tala verði ekki minnkuð í villandi fyrirsögn og tryggðu að hvaða viðskiptagreindartól sem þú kaupir geti uppfyllt þessa staðla, því skyldan er þín óháð söluaðila.

## Dæmi

**Sprotafyrirtæki.** Tíu manna greiningarsprotafyrirtæki afhendir notkunarmælaborð fyrir viðskiptavini. Fyrsta útgáfan notar sjálfgefið þema viðskiptagreindartóls: regnboga flokkaliti, hjálparlínur út um allt og kökurit með níu sneiðum sem enginn getur lesið. Notendur kvarta yfir að tölurnar finnist óáreiðanlegar. Teymið endursmíðar það sem innfellda íhluti með lítilli litblindaöruggri pallettu, skiptir kökuritinu út fyrir raðaða súlu, léttir hjálparlínurnar og bætir við beinum merkjum svo skýringin hverfur. Þau setja titla sem segja niðurstöður og bæta alt-texta og töfluskipti við hvert graf. Þátttaka í mælaborðinu eykst því viðskiptavinir geta loksins lesið það í fljótu bragði og hreinni hönnunin verður sölupunktur í kynningum.

**Stórfyrirtæki.** Fjölþjóðlegur banki á hundruð innri mælaborða smíðuð af tugum teyma, hvert með eigin liti og ásavenjur, og stjórnendur vantreysta þeim reglulega því sami mælikvarðinn lítur öðruvísi út í hverri kynningu. Fyrirtækið kynnir stýrt grafasafn ofan á viðskiptagreindarvettvang sinn: samþykktar raðbundnar, ósamstæðar og flokkandi pallettur, fastar reglur um að súluásar byrji á núlli, stöðlað tölusnið og aðgengi innbyggt í hvern íhlut. Sjónræn afturfarapróf í afhendingarleiðslu kafla 8.1 stöðvar graf sem brjóta staðlana. Innan árs lesist graf frá hvaða teymi sem er rétt við fyrstu sýn og stjórnendur hætta að spyrja „hvaða útgáfu af þessari tölu á ég að trúa?“

**Hið opinbera.** Landsbundin hagstofa birtir opinber gögn um efnahag, heilsu og mannfjölda og graf hennar eru lesin af blaðamönnum, stefnumótendum og borgurum sem geta ekki staðfest undirliggjandi tölur. Stofnunin meðhöndlar hvert graf sem samskipti við almenning og snerting við hagsmunaaðilatraustið í kafla 10.16. Hún skyldar heiðarlega kvarða (súlur frá núlli, enga villandi tvöfalda ása, flatarmál kóðað með flatarmáli), litblindaöruggar ósamstæðar pallettur fyrir svæðasamanburð, einfalda titla sem segja niðurstöðuna og niðurhlaðanlega aðgengilega töflu við hlið hvers grafs til að uppfylla WCAG. Þegar umdeild tala er birt útskýrir skýringin aðferðina og óvissuna á grafinu sjálfu, svo styttur ás eða ómerktur broddur geti aldrei orðið villandi fyrirsögn sem grefur undan trausti almennings.

## Viðskiptarök: hvatar, ávöxtun fjárfestingar og heildarkostnaður

Ávöxtun góðrar sjónrænnar hönnunar eru hraðari, betri ákvarðanir og færri dýr mistök. Mælaborð sem afhjúpar vandamál í fljótu bragði styttir tímann frá merki til aðgerðar og graf sem segir sannleikann kemur í veg fyrir að fjármagn elti blekkingu sem styttur ás bjó til. Þennan ávinning er erfitt að setja á reikning, en hann er raunverulegur: hver stjórnendafundur sem fer í að rífast um hvaða graf eigi að trúa, hver stefna byggð á misskilinni þróun og hver viðskiptavinur sem hættir því greining vörunnar var ólæsileg er kostnaður sem skýr hönnun fjarlægir. Þar sem graf knýja raunverulega peninga, eins og í bankadæminu, vegur verðmæti traustra talna margfalt þyngra en kostnaðurinn við að smíða þær vel.

Upptökukostnaðurinn er aðallega einskiptis og sameiginlegur. Þú skilgreinir samþykktar pallettur, ása- og sniðreglur og aðgengissjálfgefin gildi, kóðar þau síðan í grafíhlutasafn svo teymi erfi þau í stað þess að endurákveða á hverju mælaborði. Viðvarandi eignarkostnaður er raunverulegur en hóflegur: að viðhalda safninu, halda því aðgengilegu eftir því sem staðlar þróast og standa gegn ofvexti sérsmíðaðra grafa. Kostnaður vanrækslu safnast hljóðlega upp: ósamræmd, villandi, óaðgengileg graf rýra traust á öllum gögnum þínum, bjóða lagalegri áhættu í regluverkuðu og opinberu umhverfi og ýta fólki aftur í hrá töflureikni, sem sóar allri fjárfestingunni í greiningarstafla kafla 7.3. Til að færa rök við forystu skaltu tengja gæði sjónrænnar framsetningar við niðurstöður sem hún fylgist þegar með: ákvörðunarhraða, traust á skýrslugerð og, hjá hinu opinbera, aðgengisreglufylgni.

## Andmynstur og gildrur

- **Styttur súluás:** súlur sem byrja yfir núlli svo lítill munur líti út sem hyldýpi. Algengasta einstaka grafalygin.
- **Óþarfur tvöfaldur ás:** tveir y-kvarðar á einu grafi, runnir til að framleiða hvaða fylgni sem höfundurinn vill sýna.
- **Villandi flatarmál:** að kvarða tákn eða kúlu eftir hliðarlengd svo flatarmál þess, og skynjað gildi, vaxi sem ferningur.
- **Regnbogi fyrir magn:** að kóða raðað magn með óröðuðum flokkalitblæjum, svo augað getur ekki lesið stærð.
- **Kaka með mörgum sneiðum:** fleiri en þrjár sneiðar, sem þvinga lesendur til að bera saman horn sem þeir geta ekki metið. Notaðu raðaða súlu.
- **Grafrusl:** þungar hjálparlínur, rammar, þrívídd og skuggar sem lækka gagnablekshlutfallið og grafa merkið.
- **Litur sem eina vísbendingin:** rautt-grænt stöðumerki án merkis eða forms, ósýnilegt litblindum lesendum og skjálesurum.
- **Leit að skýringu:** að þvinga ferð til fjarlægrar skýringar þar sem bein merking á línu eða súlu dygði.
- **Allt áhersla:** hver röð feit og björt, svo birtuskil hrynja og ekkert sker sig úr.
- **Graf þar sem tafla vinnur:** mynd fyrir fjórar nákvæmar tölur sem lesandi þarf að lesa nákvæmlega.

## Þroskalíkan

- **Stig 1, Upphaf:** Graf eru gerð ad hoc í hvaða verkfæri sem er við höndina. Litir, ásar og snið eru ólík eftir höfundi, styttir ásar og flokkaregnbogar eru algeng, aðgengi er óíhugað og lesendur vantreysta niðurstöðunum.
- **Stig 2, Þróun:** Sum teymi taka upp grunnvinnubrögð, en þau eru ósamræmd um skipulagsheildina. Súlur byrja á núlli sums staðar, augljóst grafrusl er latt í rýni og húspalletta er til hjá fáeinum teymum, en annað teymi niður ganginn afhendir enn níu sneiða köku og rauð-græna stöðumynd.
- **Stig 3, Stöðlun:** Sameiginlegt grafíhlutasafn kóðar samþykktar raðbundnar, ósamstæðar og flokkandi pallettur, heiðarlegar ásareglur, staðlað snið og aðgengi (öruggt fyrir litblinda, alt-texti, töfluvari). Staðlarnir eru skjalfestir og framfylgdir um skipulagsheildina og útskýringar-, könnunar- og mælaborðsnotkun er aðgreind í hönnun.
- **Stig 4, Stjórnun:** Gæði sjónrænnar framsetningar eru mæld og stýrð gegn grunnlínum. Aðgengis- og grafheilindaathuganir keyra í afhendingarleiðslunni og skila árangurshlutföllum. Hlutfall grafa með súlur frá núlli, birtuskilasamræmdum lit og töfluvara er rakið sem mælikvarði. Skilningur er prófaður með raunverulegum lesendum gegn grunnlínu og fjöldi ósamstæðra mállýskna af hverjum lykilmælikvarða er vaktaður þegar hann leitar í átt að einni. Graf sem brjóta staðlana eru gripin fyrir útgáfu og tölurnar, ekki skoðun, ráða hvar safnið þarf vinnu.
- **Stig 5, Samhæfing:** Sjónræn framsetning er stöðugt bætt og samþætt um skipulagsheildina. Staðlar aðlagast þegar aðgengiskröfur og þarfir lesenda breytast, pallettur, íhlutir og venjur eru fínpússaðar af mældum sönnunargögnum, skýring og frásögn eru normið og venjan er ofin inn í greiningar- og ákvörðunarmenninguna svo graf frá hvaða teymi sem er lesist rétt við fyrstu sýn og sjónræna málið þróast eftir því sem skipulagsheildin lærir.

## Hugmyndir til umræðu

1. Hvaða graf á helsta mælaborði þínu myndi líta öðruvísi út ef ás þess byrjaði á núlli og breytir það sögunni?
2. Veldu mikilvægasta grafið þitt: lifa skilaboð þess af í gráskala, og ef ekki, hvaða afritaða vísbending myndi laga það?
3. Hvar notarðu gagnvirkt graf þegar kyrrstætt, skýrt graf myndi segja alla söguna hraðar?
4. Segja grafatitlar þínir niðurstöður eða efni, og hver myndi taka eftir því ef fyrirsagnartala snerist hljóðlega við?
5. Hvert grafa þinna svarar engri núverandi ákvörðun og hvað þyrfti til að eyða því án þess að nokkur sakni þess?
6. Hvenær ætti teymi að smíða sýn í vörunni á móti því að nota viðskiptagreindartólið, og áttu skriflega reglu til að velja?

## Helstu atriði

- Byrjaðu á spurningu lesandans, veldu síðan grafið: súlur fyrir samanburð, línur fyrir þróun, dreifirit fyrir samband, stöplarit fyrir dreifingu, raðaðar súlur fram yfir kökur fyrir hluta af heild.
- Láttu kóðunina samsvara gögnunum: eyddu stöðu og lengd í mikilvægasta magnið þitt og notaðu litblæ fyrir flokka, aldrei fyrir stærð.
- Stefndu að grafískum ágæti: hámarkaðu gagnablekshlutfallið, eyddu grafrusli, notaðu smáfjöldarit og beindu auganu með forathyglibirtuskilum og skýrri stigskiptingu.
- Meðhöndlaðu lit sem kerfi (raðbundinn, ósamstæður, flokkandi), hafðu hann öruggan fyrir litblinda og reiddu þig aldrei á lit einan. Útvegaðu merki, alt-texta og töfluvara.
- Segðu sannleikann um kvarða (súlur frá núlli, heiðarleg svæði, enginn óþarfur tvöfaldur ás), skýrðu innsýnina og bættu við gagnvirkni aðeins þegar raunveruleg eftirfylgnispurning krefst þess.

## Heimildir og frekari lestur

- Edward R. Tufte, *The Visual Display of Quantitative Information*
- Edward R. Tufte, *Envisioning Information*
- Stephen Few, *Show Me the Numbers: Designing Tables and Graphs to Enlighten*
- Stephen Few, *Information Dashboard Design: Displaying Data for At-a-Glance Monitoring*
- Cole Nussbaumer Knaflic, *Storytelling with Data: A Data Visualisation Guide for Business Professionals*
- Alberto Cairo, *The Truthful Art: Data, Charts, and Maps for Communication*
- Alberto Cairo, *How Charts Lie: Getting Smarter about Visual Information*
- William S. Cleveland, *The Elements of Graphing Data*
- Jacques Bertin, *Semiology of Graphics: Diagrams, Networks, Maps*
- Tamara Munzner, *Visualisation Analysis and Design*
- Cynthia A. Brewer, ColorBrewer: Colour Advice for Cartography (colorbrewer2.org)
- World Wide Web Consortium (W3C), *Web Content Accessibility Guidelines (WCAG) 2.2*
