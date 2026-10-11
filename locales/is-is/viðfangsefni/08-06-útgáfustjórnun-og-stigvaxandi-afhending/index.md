# 8.6 Útgáfustjórnun og stigvaxandi afhending

## Yfirlit og tilgangur

Gagnlegasta hugmyndin í nútíma útgáfustjórnun er líka sú einfaldasta: að afhenda kóða og að afhjúpa eiginleika eru tveir ólíkir atburðir og þú ættir að geta gert annan án hins. Kafli 8.1 (CI/CD og afhending) kemur breytingu þinni í smíði einu sinni, prófaða og eflda sem óbreytanlegan grip. Þessi kafli fjallar um það sem gerist næst: hvernig þú breytir útsettum kóða í lifandi upplifun fyrir raunverulega notendur, smám saman, örugglega og með skjótri leið til baka. **Útsetning** þýðir að setja kóða upp á þjóna. **Útgáfa** þýðir að leyfa notendum að ná til getu. Þegar þú aðgreinir þetta tvennt verður útsetning venjuleg og leiðinleg og útgáfa verður stýrð, afturkræf ákvörðun.

Fyrir stór teymi breytir þessi aðgreining tilfinningalegum hita afhendingar. Þegar tugir þjónusta og hundruð verkfræðinga breyta framleiðslu á hverjum degi þýðir tengt „útsetning jafngildir útgáfu“ líkan að hver notendasnúin breyting er áhættusamur, allt-í-einu atburður. Aðgreining leyfir þér að sameina ókláraða vinnu á bak við rofa, rúlla eiginleika til eins prósents umferðar, fylgjast með tölunum og víkka eða hörfa án þess að snerta smíðina. **Stigvaxandi afhending** er yfirheitið yfir þetta: að gefa út breytingu til sífellt breiðari áheyrenda á meðan sjálfvirkar athuganir ákveða hvort halda skuli áfram.

Fyrirtækja- og opinbert umhverfi bætir við samræmingu og sönnun. Greiðsluvettvangur gefur út yfir margar þjónustur sem verða að koma sér saman um skema. Opinber stofnun starfar undir rekstrarheimild og formlegri breytingastjórn og úttektaraðilar vilja sönnunargögn um nákvæmlega hver var afhjúpaður fyrir hverju og hvenær. Vel gerð stigvaxandi afhending fullnægir bæði löngun til að hreyfa sig hratt og skyldunni til að sanna stjórn, því sami búnaðurinn sem takmarkar sprengisvæði framleiðir líka úttektarhæfa skrá yfir útsetninguna.

## Meginreglur

- **Útsetning er ekki útgáfa.** Afhentu kóða dimman, kveiktu síðan á honum af ásetningi.
- **Lítið sprengisvæði fyrst.** Afhjúpaðu breytingu fyrir fáum áður en þú afhjúpar hana fyrir öllum.
- **Sérhver útgáfa hefur bakkgír.** Ef þú getur ekki afturkallað á sekúndum hefurðu ekki lokið við að hanna útgáfuna.
- **Láttu merki knýja eflingu.** Heilsumælikvarðar og villufjárhagsáætlanir, ekki dagatöl eða bjartsýni, ákveða hvort útsetning heldur áfram.
- **Rofi er skuld þar til hann er fjarlægður.** Sérhver rofi er kóði sem þú verður að viðhalda og að lokum eyða.
- **Láttu gagnagrunnsbreytingu lifa af báðar áttir.** Útsetningar og afturköllun verða báðar að vera öruggar gegn sama skema.
- **Samþykki ættu að skrá, ekki hindra.** Úttektarsönnunargögn eru aukaafurð leiðslunnar, ekki vikulegur fundur.

## Ráðleggingar

### Aðgreindu útsetningu frá útgáfu með eiginleikarofum

[Eiginleikarofi](https://en.wikipedia.org/wiki/Feature_toggle), eða eiginleikafáni, er keyrslurofi sem ákveður hvort kóðaleið er virk, án endurútsetningar. Líttu á rofa sem tegundað orðasafn, því líftími þeirra er ólíkur. **Útgáfurofi** felur vinnu í gangi og lifir í daga til vikur. **Rekstrarrofi** (drápsrofi) leyfir þér að afvirkja undirkerfi undir álagi og getur lifað endalaust. **Tilraunarofi** skiptir umferð fyrir stýrt próf og lifir meðan á tilrauninni stendur. **Heimildarrofi** hliðar getu eftir áskrift eða hlutverki og er í reynd varanlegur. Gefðu hverjum rofa eiganda, tegund, sjálfgefið gildi og væntanlegan fjarlægingardag. Sjálfgefna gildið ætti að vera það örugga, svo bilun rofaþjónustu lokist yfir í þekkta góða hegðun frekar en opnist að óprófuðum leiðum.

### Veldu stigvaxandi afhendingarmynstur á þjónustuþrep

Láttu útgáfubúnaðinn samsvara sprengisvæðinu, eins og kafli 8.1 heldur fram um útsetningarstefnur. [Kanarí-útgáfa](https://en.wikipedia.org/wiki/Feature_toggle#Canary_release) beinir lítilli sneið umferðar að nýju útgáfunni og víkkar aðeins ef heilsan heldur. [Blá-græn útsetning](https://en.wikipedia.org/wiki/Blue-green_deployment) heldur tveimur framleiðsluumhverfum og færir umferð á milli fyrir samstundis skipti og samstundis afturköllun. **Rúllandi útsetning** skiptir út tilvikum í lotum. **Hringbundin útsetning** víkkar gegnum nefnda áheyrendur: innri notendur fyrst, síðan beta-hóp, síðan lítið svæði, síðan alla. Hringir eru gagnlegasta rammunin fyrir stórar skipulagsheildir því þeir nefna hver er afhjúpaður á hverju skrefi, sem er einmitt það sem bæði úttektaraðili og atvikasvarandi vilja vita. Gámavettvangur og stýring (kafli 8.3) veita umferðarmótunarfrumstæðurnar sem gera þessi mynstur ódýr í rekstri.

### Hliðaðu útsetningar á heilsuathugunum og sjálfvirkri afturköllun

Skilgreindu hlutlæg heilsuviðmið fyrir útgáfuna, ekki í atvikinu. Sjálfvirk greining ber kanaríið saman við grunnlínuna á villuhlutfalli, töf og mettun og annaðhvort eflir eða afturkallar án þess að bíða eftir að maður taki eftir. Tengdu eflingu við [þjónustustigsmarkmið](https://en.wikipedia.org/wiki/Service-level_objective) þitt og villufjárhagsáætlun úr áreiðanleikaverkfræði (kafli 9.1): þegar fjárhagsáætlunin er heilbrigð gefurðu út frjálslega og þegar hún er eydd neitar leiðslan að halda áfram þar til þjónustan stöðugast. Sjálfvirk afturköllun skiptir mestu máli því hún fjarlægir hikið sem breytir lítilli afturför í stórt rof. Skjót afturköllun er líka ódýrasta atvikastýring þín: afturköllun sem tekur sekúndur minnkar sprengisvæðið áður en atvikaferlið þitt (kafli 9.3) er jafnvel komið alveg í gang. Bilunarhlutfall breytinga og endurheimtartími sem þú bætir þannig eru sömu flæðis- og stöðugleikamerkin sem afhendingarleiðslan þín rekur (kafli 11.2).

### Notaðu dimmar opnanir og skuggaumferð til að draga úr áhættu

Sumar breytingar eru of afleiddar til að mæta fyrst raunverulegum notendum við fulla útsetningu. **Dimm opnun** afhendir eiginleika slökktan, æfir hann síðan innanhúss eða gegn broti af framleiðslu áður en nokkur sér hann. **Skuggaumferð** afritar lifandi beiðnir á nýju kóðaleiðina og fleygir svörunum, svo þú mælir raunverulegt álag og réttleika án nokkurra áhrifa á notendur. Þessi tækni leyfir þér að staðfesta endurskrift eða nýtt ósjálfstæði undir ósvikinni umferð, sem ekkert prófunarumhverfi endurskapar trúlega. Paraðu þau við sömu heilsugreiningu og þú notar fyrir kanarí.

### Keyrðu stýrðar tilraunir gegnum sama rofakerfi

Tilraunarofinn er þar sem útgáfuverkfræði mætir vörunámi. [A/B-prófunar](https://en.wikipedia.org/wiki/A/B_testing) skipting þjónar afbrigðum til sambærilegra hópa og mælir valda niðurstöðu, sem nærir vörugreiningarvenjuna í kafla 7.4. Endurnýttu eitt rofa- og miðunarkerfi bæði fyrir öryggisútsetningar og tilraunir, svo þú hafir eina úttektarslóð og einn drápsrofa frekar en tvo samhliða rofastafla sem eru ósammála um hver er í hvaða hólfi.

### Haltu gagnagrunninum afturábaksamhæfum með víkka-og-dragðu-saman

Útsetningar og afturkallanir haldast aðeins öruggar ef skemað þolir bæði gamlan og nýjan kóða samtímis, sem er óhjákvæmilegt í hverri stigvaxandi útsetningu. Notaðu **víkka-og-dragðu-saman** (samhliða breytingar) mynstrið: fyrst *víkkaðu* með því að bæta við nýjum dálkum eða töflum í afturábaksamhæfri flutningi, settu síðan upp kóða sem skrifar í bæði gamla og nýja lögun, endurfylltu síðan, færðu lestur yfir og aðeins mun síðar *dragðu saman* með því að fjarlægja gömlu lögunina þegar enginn keyrandi kóði er háður henni. Sameinaðu aldrei eyðileggjandi flutning við útsetninguna sem þarfnast hans. Þessi agi er það sem leyfir þér að afturkalla kóða án gagnagrunns sem þegar hefur færst áfram og hann tengist beint prófunarstefnu þinni (kafli 2.4), sem verður að ná yfir blandaða útgáfugluggann.

### Láttu breytingastjórn skrá frekar en hindra

Sættu úttekt við flæði með því að fyrirfram samþykkja flokka breytinga. Skilgreindu staðlaðar, áhættulitlar breytingategundir sem flæða gegnum leiðsluna sjálfvirkt og fanga hver samþykkti, hvaða próf keyrðu, hvaða gripur var settur upp og hvaða áheyrendur voru afhjúpaðir á hverjum hring. Taktu frá mannlega breytingaráðgjafarrýni fyrir sannarlega áhættumiklar breytingar. Hefðbundin [breytingastjórnar](https://en.wikipedia.org/wiki/Change_control) nefnd sem skoðar hverja venjulega útsetningu verður flöskuháls sem ýtir teymum í átt að stærri, áhættusamari lotum, öfugt við það sem hún ætlar. Hjá hinu opinbera geta rekstrarheimild og formleg breytingastjórn lifað saman með stigvaxandi afhendingu þegar útsetningarverkfærin gefa út sönnunargögnin sem stýringarramminn krefst, svo hringbundna skráin er úttektargripurinn.

## Málamiðlanir: kostir og gallar

| Mynstur | Kostir | Gallar | Best passun |
|---|---|---|---|
| Kanarí | Gagnadrifið, lítið sprengisvæði | Þarfnast góðra mælikvarða og umferðarmagns | Stórar notendasnúnar þjónustur |
| Blár-grænn | Samstundis skipti og afturköllun | Tvöfaldar umhverfiskostnað við skiptin | Mikilvægar þjónustur sem þurfa skjóta afturköllun |
| Rúllandi | Ódýrt, einfalt, ekkert aukaumhverfi | Hæg afturköllun, blandaðar útgáfur lifandi | Ástandslausar innri þjónustur |
| Hringbundið | Nefndir áheyrendur, skýr úttektarslóð | Hægari full útsetning. Meiri samræming | Regluverkaðar og fjölþjónustu landareignir |
| Eiginleikarofar | Aðgreina útsetningu frá útgáfu. Samstundis drápsrofi | Rofaskuld. Prófafylki vex | Teymi sem afhenda ókláraða vinnu örugglega |
| Útgáfulestir | Fyrirsjáanlegur taktur, auðveld samræming | Tengir margar breytingar. Bíður eftir lestinni | Mörg teymi sem deila útgáfu |
| Útgáfa eftir þörfum | Litlar lotur, hröð endurgjöf | Erfiðari þverteymissamræming | Hátraust samfelldrar afhendingar teymi |

Kjarnaspennan er milli samræmingar og sjálfstæðis. **Útgáfulestir** bunka breytingum margra teyma á fastan tímaáætlun, sem er auðvelt að rökræða um en neyðir fullgerða breytingu til að bíða og tengir óskylda vinnu í einn atburð. **Útgáfa eftir þörfum** leyfir hverju teymi að afhenda þegar það er tilbúið, sem er hraðara en krefst þess að þjónustur haldist sjálfstætt útsetjanlegar og afturábaksamhæfar. Lausnin er yfirleitt að aðgreina á gripa- og skemastigi svo teymi *geti* gefið út eftir þörfum, nota síðan rofa og hringi til að samræma *notendasýnilega* augnablikið þegar þverþjónustueiginleiki kveikir í raun á sér. Þannig eru tæknilega útgáfan og vörukynningin aðskildar ákvarðanir og hvorug blokkar hina.

## Spurningar til að ræða með teyminu

1. **Þegar útgáfa fer úrskeiðis klukkan tvö um nótt, hve margar sekúndur tekur að afturkalla og hver eða hvað togar í gikkinn?** Heiðarlega svarið afhjúpar hvort þið hafið í raun aðgreint útsetningu frá útgáfu eða bara bætt rofum ofan á tengt ferli. Afturköllun sem krefst endursmíði, gagnagrunnsflutnings til að afturkalla eða útkallaðs manns til að ákveða er ekki afturköllun, hún er annað atvik. Komdu með raunverulegan búnað fyrir þrjár efstu þjónustur þínar: rofann eða umferðarfærsluna sem afturkallar útsetningu, heilsumerkið sem ræsir hana sjálfvirkt og skemaábyrgðina sem gerir afturköllun örugga. Fyrir stóra landareign ræður þetta raunverulegu sprengisvæði ykkar, því skjót sjálfvirk afturköllun er það sem heldur afturför frá því að verða rof. Ef svarið er mælt í fundum frekar en sekúndum er það fyrsta sem á að laga.

2. **Hver er stefna ykkar um að leggja niður rofa og hve mikla rofaskuld berið þið núna?** Sérhver eiginleikarofi er gaffall í kóða þínum sem margfaldar fjölda ástanda sem þú verður að rökræða um og prófa og rofi sem lifir tilgang sinn er hrein skuld. Ákveddu regluna núna: sérhver útgáfurofi fær eiganda og fyrningardag, úreltir rofar birtast á mælaborði og að fjarlægja þá er skipulögð vinna frekar en einhvern tímann-hreinsun. Komdu með talningu lifandi rofa, aldur þeirra og hve margir eru yfir áætluðum fjarlægingardegi. Í stórum kóðagrunni verða óstýrðir rofar varanleg skilyrðisflækja sem enginn þorir að eyða og öryggisbúnaðurinn verður uppspretta galla. Umburðarlyndi teymisins fyrir þeirri tölu er í raun yfirlýsing um hve alvarlega það lítur á rekstrarhreinlæti.

3. **Gerir breytingasamþykktarferli ykkar útgáfur öruggari eða bara hægari?** Margar skipulagsheildir reka breytingaráðgjafarnefnd sem rýnir hverja útsetningu og óþægilega spurningin er hvort hún hafi nokkru sinni í raun stöðvað slæma breytingu eða aðeins bætt við töf. Komdu með gögn: miðgildi samþykktartafar, bilunarhlutfall breytinga fyrir nefndarrýndar á móti fyrirfram samþykktum breytingum og hve oft rýni bunkar litlar breytingar í stærri, áhættusamari. Markmiðið er að taka frá mannlega rýni fyrir sannarlega áhættumiklar breytingar á meðan staðlaðar breytingar flæða gegnum leiðsluna með sjálfvirkri sönnunargagnasöfnun. Fyrir regluverkað og opinbert samhengi skaltu staðfesta að útsetningarverkfærin framleiði úttektarskrána sem stýringarramminn þarf, svo stjórn verði aukaafurð afhendingar frekar en hlið fyrir framan hana. Ef rýni bætir við töf án þess að fækka bilunum er hún leikhús í reglufylgnibúningi.

4. **Hvaða hlutlægu heilsumerkjum eruð þið tilbúin að leyfa vél að bregðast við og hefur hver efstu þrepa þjónusta í raun mælikvarða nógu góða til að hliða á?** Sjálfvirk kanarígreining og villufjárhagsáætlunarhliðun virka aðeins ef villuhlutfall, töf og mettun eru mæld nógu hreint til að treysta eflingu eða afturköllun án manns í lykkjunni og mörg teymi uppgötva í atviki að merki þeirra eru of hávaðasöm eða of strjál til að ákveða. Fyrir stóra landareign ræður þetta hve mikið af útgáfumagni ykkar getur flætt örugglega án handvirkrar barnagæslu, sem er munurinn á vettvangi sem skalast og einum sem þarf mann til að fylgjast með hverri útsetningu. Komdu með raunveruleg mælaborð fyrir þrjár mikilvægustu þjónusturnar þínar: mælikvarðana sem þú hliðar á, umferðarmagnið sem gerir kanarí tölfræðilega marktækt og falsk-jákvæða hlutfall sjálfvirku greiningarinnar. Í regluverkuðu og opinberu umhverfi nærir sömu merki úttektarskrána, svo léleg vöktun er bæði áreiðanleikabil og reglufylgnibil og að fjármagna mælikvarðagæði ætti að vera nefndur liður í áætluninni frekar en gert ráð fyrir getu.

5. **Lifa skemabreytingar ykkar í raun af afturköllun og hvernig sannið þið að blandaði útgáfugluggi sé öruggur áður en þið afhendið?** Stigvaxandi afhending lofar skjótum bakkgír, en eyðileggjandi flutningur tengdur eiginleika ógildir það loforð hljóðlega, því að afturkalla kóðann skilur hann eftir að benda á gagnagrunn sem hefur þegar færst áfram. Fyrir stóra skipulagsheild þar sem margar þjónustur deila skema magnast áhættan: samdráttarskref eins teymis getur strandað afturköllun annars, svo víkka-og-dragðu-saman agi þarf að vera sameiginlegur staðall frekar en staðbundinn vani. Komdu með flutningshandbók þína og sönnunargögnin um að henni sé fylgt: hvernig þú aðgreinir víkkun frá samdrætti, hvort tvískrif og endurfylling séu prófuð undir álagi og hvernig prófasafn þitt æfir gamlan kóða gegn nýja skemanu og nýjan kóða gegn gamla. Fyrir fyrirtækja- og opinberar landareignir sem bera langlíf gögn og formlega breytingastjórn er óafturkræfur flutningur ekki bara rofáhætta, hann er gagnaheilindi- og úttektarútsetning sem áætlaður viðhaldsgluggi bjargar ekki.

6. **Þegar þverþjónustueiginleiki spannar teymi sem afhenda á ólíkum hraða, hver á augnablikið sem kveikt er á honum og hvernig samræmið þið án þess að tengja útsetningar þeirra?** Allur tilgangurinn með því að aðgreina útsetningu frá útgáfu er að hvert teymi geti afhent grip sinn sjálfstætt á meðan einn rofi stýrir notendasýnilegu opnuninni, en það heldur aðeins ef einhver á opnunarákvörðunina og rofamiðunina yfir þjónustumörk. Fyrir stórt teymi er bilunarhátturinn í raun útgáfulest sem enginn valdi: ein hæg þjónusta neyðir öll hin teymin til að bíða, eða ósamræmd rofabreyting afhjúpar hálftengdan eiginleika. Komdu með ósjálfstæðakortið fyrir næstu fjölþjónustuopnun þína, eiganda opnunarrofans og afturábaksamhæfistryggingarnar sem leyfa hverri þjónustu að setja upp á eigin klukku. Í fyrirtækja- og opinberum áætlunum með formlegar opnunarsamþykktir skaltu nefna hver skrifar undir þverþjónustukveikinguna og hvaða sönnunargögn hann sér, svo samræmda opnunin sé yfirveguð, skráð ákvörðun frekar en tilviljun þess sem sameinaði síðast.

## Sjónarhorn eftir geirum

**Sprotafyrirtæki.** Að aðgreina útsetningu frá útgáfu er þess virði að gera jafnvel með þrjá verkfræðinga, en haltu því ódýru. Vefðu nýrri vinnu í útgáfurofa sem er sjálfgefið af, afhentu í stofn og kveiktu á eiginleikum fyrir sjálfan þig áður en viðskiptavini svo ókláruð breyting blokki aldrei útsetningu. Slepptu þungum kanarígreiningarvettvöngum sem þú getur ekki mannað: hýst rofaþjónusta og harður drápsrofi kaupa mestallt öryggið og einn maður sem á vikulegan rofahreinsunarsið heldur skuld frá því að gleypa hraða þinn.

**Lítið fyrirtæki.** Án útgáfuverkfræðings og með þröngt fjárhagsáætlun skaltu halla þér að hvaða stigvaxandi afhendingu sem núverandi vettvangur þinn gefur þér nú þegar, frekar en að smíða útsetningarkerfi. Stýrð hýsing, eiginleikarofa-SaaS eða innbyggð stigskipt útsetning rammans þíns nær yfirleitt yfir litla sprengisvæðið sem þú þarft. Líttu á bakkgírinn sem það sem þú verður að fá rétt: breyting sem þú getur slökkt á á sekúndum skiptir langtum meira máli en háþróuð sjálfvirk greining sem þú hefur engan tíma til að stilla.

**Stórfyrirtæki.** Vandinn er samræmi yfir mörg teymi og þjónustur: sameiginlegt rofaorðasafn með eigendum, tegundum og fyrningu, stöðluð hringbundin útsetning og villufjárhagsáætlunarhliðun beitt eins alls staðar svo hópar hætti að finna upp keppinauta rofastafla. Stýrðu rofaskuld sem mælikvarða yfir alla landareignina, staðlaðu víkka-og-dragðu-saman flutninga svo skemabreyting eins teymis strandi aldrei afturköllun annars og gerðu úttektarhæfu útsetningarskrána að aukaafurð sem hver þjónusta gefur út í sömu lögun. Fyrirfram samþykktu staðlaðar breytingar og taktu frá mannlega rýni fyrir sannarlega áhættumiklar, svo stjórn skalist án nefndar á mikilvægu slóðinni.

**Hið opinbera.** Innkaupareglur, gagnsæi og opinber ábyrgð móta hverja útgáfu. Gerðu útsetningarverkfærin að uppsprettu úttektarsönnunargagna, svo hver hringvíkkun skrái samþykkjandi yfirvaldið, prófin sem keyrðu, kjötkássu gripsins og nákvæmlega þýðið sem var afhjúpað, og rekstrarheimild lifi saman við stigvaxandi afhendingu í stað þess að berjast við hana. Kjóstu blá-græn eða hringbundin mynstur með nefndum áheyrendum sem bæði úttektaraðili og atvikasvarandi geta lesið, staðfestu afleiddar breytingar með skuggaumferð gegn lifandi tilvikum áður en nokkur borgari verður fyrir áhrifum og haltu úttektarhæfu skránni sem gripnum sem stýringarramminn tekur við í stað áætlaðs allt-í-einu glugga.

## Dæmi

**Sprotafyrirtæki.** Tíu manna SaaS-fyrirtæki afhendir í stofn mörgum sinnum á dag og vefur hverri nýrri getu í útgáfurofa sem er sjálfgefið af. Áhættusöm ný reikningagerðarsamþætting opnast dimm: þau keyra skuggaumferð gegn henni í viku og horfa á hana meðhöndla raunverulegar beiðnalögun án áhrifa á viðskiptavini, rúlla henni síðan út hring fyrir hring, byrja á eigin reikningum og örfáum vinveittum beta-viðskiptavinum. Þegar villuhlutfall rýkur upp á fimm prósenta hringnum slekkur sjálfvirk athugun á rofanum á sekúndum og þau aflúsa rólega á mánudegi. Einn verkfræðingur á vikulegan rofahreinsunarsið svo rofarnir hrannist aldrei upp.

**Stórfyrirtæki.** Alþjóðlegt greiðslufyrirtæki samræmir breytingu sem spannar sex þjónustur og sameiginlegt skema. Hvert teymi setur upp grip sinn sjálfstætt og afturábaksamhæft með víkka-og-dragðu-saman, svo nýju dálkarnir eru til og tvískrifaðir löngu áður en nokkur notandi sér eiginleikann. Notendasýnilega opnunin er einn tilraunarofi, rúllaður gegnum hringi bundna við villufjárhagsáætlunarheilsu: innra, síðan eitt lítið land, síðan vaxandi prósentu, með sjálfvirkri kanarígreiningu sem eflir eða afturkallar á hverju skrefi. Rofastjórnarþjónusta framfylgir eigendum, tegundum og fyrningu yfir landareignina og fyrirfram samþykktar staðlaðar breytingar flæða án nefndar á meðan aðeins skemasamdráttarskrefið fær mannlega rýni. Hver hringfærsla er skráð, svo úttektarslóðin skrifar sig sjálf.

**Hið opinbera.** Landsbundin bótastofnun starfar undir rekstrarheimild og formlegri breytingastjórn. Frekar en að líta á stigvaxandi afhendingu sem reglufylgniáhættu gerir hún útsetningarverkfærin að uppsprettu úttektarsönnunargagna: hver hringvíkkun skráir samþykkjandi yfirvaldið, prófin sem keyrðu, kjötkássu gripsins og nákvæmlega þýðið sem var afhjúpað. Nýr hæfisútreikningur opnast dimmur og er staðfestur með skuggaumferð gegn lifandi tilvikum, rúllar síðan út svæði fyrir svæði á bak við rofa með blá-grænum skiptum fyrir samstundis afturköllun. Staðlaðar breytingar eru fyrirfram flokkaðar svo venjuleg vinna bíði ekki í röð fyrir aftan nefnd, á meðan áhættumiklar stefnubreytingar fá enn formlega rýni. Úttektarhæfa útsetningarskráin fullnægir stýringarrammanum ítarlegar en gamla ársfjórðungslega allt-í-einu útgáfan gerði nokkru sinni.

## Viðskiptarök: hvatar, ávöxtun fjárfestingar og heildarkostnaður

Ávöxtun stigvaxandi afhendingar ræðst af forðuðum atvikum og minnkaðri alvarleika þeirra. Breyting sem nær til eins prósents notenda og afturkallast sjálfvirkt kostar námundunarvillu, þar sem sami galli við fulla útsetningu getur þýtt klukkustundir af rofi, neyðarviðbrögð og orðsporsskaða. Að aðgreina útsetningu frá útgáfu breytir líka sjálfri útgáfunni úr áætluðum, streituvaldandi atburði í hversdagslegan, sem lækkar samræmingarskattinn sem vex ólínulega með teymisstærð. Að aðgreina opnunarákvörðunina frá útsetningu leyfir vöru og verkfræði að hreyfast á eigin klukkum, svo markaðsdagsetning neyði aldrei áhættusaman kóðafrystingu.

Heildareignarkostnaðurinn er raunverulegur en hóflegur miðað við þann ávinning. Þú fjárfestir í rofavettvangi, kanarígreiningarverkfærum, heilsumælikvörðum nógu góðum til að hliða á og agann að afturábaksamhæfum skemabreytingum. Viðvarandi kostnaðurinn er rofahreinlæti og stærra prófafylkið sem rofar búa til, sem er ástæða þess að óstýrð rofalandareign er helsta leiðin sem þessi venja verður dýr. Kostnaður þess að taka hana ekki upp er greiddur í sprengisvæði: hver útgáfa er allt-eða-ekkert, afturköllun er hæg og ein slæm útsetning getur fellt alla í einu. Fyrir regluverkaðar skipulagsheildir er reglufylgniarðurinn afgerandi, því sami búnaðurinn sem takmarkar útsetningu býr líka til úttektarsönnunargögnin sem annars yrðu sett saman í höndunum.

## Andmynstur og gildrur

- **Útsetning jafngildir útgáfu.** Að tengja þetta tvennt gerir hverja notendasnúna breytingu að áhættusömum, allt-í-einu atburði án bakkgírs.
- **Rofaskuld.** Rofar sem lifa tilgang sinn verða varanleg skilyrðisflækja sem enginn þorir að eyða.
- **Rofar sem opnast við bilun.** Rofaþjónustubilun sem sjálfgefið fer á nýju, óprófuðu leiðina breytir smávægilegu blikki í rof.
- **Afturköllun sem þarf skemaafturköllun.** Eyðileggjandi flutningur afhentur með eiginleika sínum gerir ómögulegt að afturkalla kóða örugglega.
- **Handvirk efling eftir tilfinningu.** Að láta útsetningu halda áfram því hún „lítur vel út“ í stað skilgreindra heilsuviðmiða og villufjárhagsáætlana.
- **Útsetning án afturköllunaráætlunar.** Að hanna hvernig kveikt er á eiginleika án þess að hanna hvernig slökkt er á honum.
- **Stimpilgúmmí breytinganefndar.** Rýni sem hafnar aldrei neinu bætir við töf án þess að bæta við öryggi og ýtir teymum í átt að stórum lotum.
- **Tilrauna- og öryggisrofar í aðskildum kerfum.** Tveir rofastaflar sem eru ósammála um hver er í hvaða hólfi tvöfalda úttektarflötinn.

## Þroskalíkan

- **Stig 1, Upphaf:** Útsetning og útgáfa eru sami atburðurinn. Breytingar fara út allar í einu, afturköllun þýðir að endurútsetja gamla smíði í höndunum og skemaflutningar eru eyðileggjandi og tengdir eiginleikum. Hvers kyns stigvaxandi útsetning er ad hoc, viðbragðsdrifin og óskjalfest.
- **Stig 2, Þróun:** Eiginleikarofar eru til hjá sumum teymum og fela ókláraða vinnu, en þá skortir eigendur, tegundir og fyrningu og skuld safnast. Kanarí eða blár-grænn er notað fyrir fáeinar mikilvægar þjónustur, beitt ósamræmt teymi fyrir teymi. Afturköllun er skriftuð en maður ræsir hana og skemabreytingar eru aðeins stundum afturábaksamhæfar.
- **Stig 3, Stöðlun:** Útsetning og útgáfa eru aðgreind sjálfgefið um skipulagsheildina. Rofar eru tegundaðir, í eigu og fyrnast, með örugg sjálfgefin gildi, eftir skjalfestum og framfylgdum staðli. Stigvaxandi afhending með hringbundinni útsetningu og sjálfvirkri kanarígreiningu er normið, víkka-og-dragðu-saman flutningar eru skyldaðir og staðlaðar breytingar flæða gegnum leiðsluna með sjálfvirkri sönnunargagnasöfnun.
- **Stig 4, Stjórnun:** Útgáfuferlið er mælt og stýrt með gögnum. Bilunarhlutfall breytinga, meðaltími til endurheimtar, afturköllunartöf, aldur og fjöldi rofa og falsk-jákvæð hlutfall kanarígreiningar eru rakin gegn grunnlínum og villufjárhagsáætlunum og útsetningar eru hliðaðar á þeim SLO (kafli 9.1) svo efling og afturköllun virki sjálfvirkt á skilgreindum heilsumerkjum. Rofaskuld er skýrð sem mælikvarði yfir landareignina og lögð niður á áætlun og frávik frá útsetningarstaðlinum koma upp á mælaborði frekar en í eftirmálsrýni.
- **Stig 5, Samhæfing:** Stigvaxandi afhending er stöðugt bætt og samþætt um skipulagsheildina. Dimmar opnanir og skuggaumferð draga reglulega úr áhættu stórra breytinga, tilraunir og öryggisútsetningar deila einu rofakerfi og úttektarslóð og útgáfustefna aðlagast stöðu villufjárhagsáætlunar í rauntíma. Úttektarhæfa útsetningarskráin fullnægir breytingastjórn (kafli 9.3) sem aukaafurð og skipulagsheildin stillir hringi sína, hlið og þröskulda af sönnunargögnum eftir því sem landareignin og áhættumyndin breytast.

## Hugmyndir til umræðu

1. Fyrir mikilvægustu þjónustu ykkar, hvar eru réttu mörkin milli sjálfvirkrar heilsuhliðaðrar afturköllunar og mannlegrar ákvörðunar og hvaða merki myndið þið treysta nógu vel til að láta vélina bregðast ein við?
2. Ættu tilraunarofar og útgáfurofar að deila einum vettvangi og einum drápsrofa, eða skapar sameining þeirra meiri áhættu en hún fjarlægir?
3. Hvernig ákveðið þið milli útgáfulestar og útgáfu eftir þörfum þegar eiginleiki spannar nokkur teymi sem afhenda á ólíkum hraða?
4. Hver er heiðarlegur helmingunartími útgáfurofa í kóðagrunni ykkar og hvað myndi gera fjarlægingu jafn hversdagslega og sköpun?
5. Hvernig ætti staða villufjárhagsáætlunar að breyta því hver má gefa út og hver á ákvörðunina um að frysta útgáfur þegar fjárhagsáætlunin er eydd?
6. Í regluverkuðu samhengi ykkar, hvaða sérstöku sönnunargögn verður útsetning að gefa út til að stýringarramminn taki stigvaxandi afhendingu í stað áætlaðs útgáfuglugga?

## Helstu atriði

- **Aðgreindu útsetningu frá útgáfu.** Að afhenda kóða og að afhjúpa eiginleika eru ólíkar ákvarðanir og rofar eru það sem aðgreinir þær.
- **Rúllaðu út stigvaxandi.** Kanarí, blár-grænn, rúllandi og hringbundin mynstur takmarka sprengisvæði. Veldu á þjónustuþrep eftir áhættu.
- **Hliðaðu á heilsu og villufjárhagsáætlunum.** Láttu skilgreind merki og SLO (kafli 9.1) knýja sjálfvirka eflingu og afturköllun, ekki dagatöl eða bjartsýni.
- **Hannaðu bakkgírinn fyrst.** Skjót, örugg afturköllun minnkar sprengisvæðið áður en atvikaferlið þitt (kafli 9.3) er alveg komið í gang.
- **Tegundaðu, eigðu og fyrndu hvern rofa.** Útgáfu-, rekstrar-, tilrauna- og heimildarrofar hafa ólíkan líftíma. Óstýrðir rofar verða skuld.
- **Gerðu skemabreytingar afturábaksamhæfar.** Notaðu víkka-og-dragðu-saman svo bæði útsetning og afturköllun haldist örugg yfir blandaða útgáfugluggann (kafli 2.4).
- **Láttu samþykki skrá, ekki hindra.** Fyrirfram samþykktu staðlaðar breytingar og taktu frá mannlega rýni fyrir mikla áhættu, svo útsetningarskráin sé úttektarsönnunargögnin.

## Heimildir og frekari lestur

- Jez Humble and David Farley, *Continuous Delivery: Reliable Software Releases through Build, Test, and Deployment Automation*.
- Nicole Forsgren, Jez Humble, and Gene Kim, *Accelerate: The Science of Lean Software and DevOps*.
- Gene Kim, Jez Humble, Patrick Debois, and John Willis, *The DevOps Handbook*.
- Betsy Beyer, Chris Jones, Jennifer Petoff, and Niall Richard Murphy (eds.), *Site Reliability Engineering*.
- Pete Hodgson, "Feature Toggles (Feature Flags)" (essay on martinfowler.com).
- Danilo Sato, "Canary Release" and Martin Fowler, "BlueGreenDeployment" (essays on martinfowler.com).
- Sam Newman, *Building Microservices: Designing Fine-Grained Systems* (expand-and-contract and independent deployability).
- Pramod Sadalage and Scott Ambler, *Refactoring Databases: Evolutionary Database Design* (parallel-change schema migrations).
- Ron Kohavi, Diane Tang, and Ya Xu, *Trustworthy Online Controlled Experiments: A Practical Guide to A/B Testing*.
- James Governor, "Progressive Delivery" (RedMonk, the coining of the term).
