# 4.1 Öryggisgrunnur og menning

## Yfirlit og tilgangur

Öryggi er ekki eiginleiki sem þú festir á í lokin, og það er ekki verk eins sérhæfðs teymis sem situr aðskilið frá verkfræði. Í stórri skipulagsheild er öryggi eiginleiki þess hvernig allt kerfið er hannað, smíðað, rekið og stýrt. Þegar þúsundir verkfræðinga afhenda kóða yfir hundruð þjónusta ræður veikasti hlekkurinn hve miklum skaða atvik getur valdið. Ein rangstillt geymslufata, ein óplástruð ósjálfstæðiseining eða einn ofréttindaður þjónustureikningur getur afhjúpað milljónir skráa. Grunnur og menning er það sem kemur í veg fyrir að það gerist í stórum stíl.

Fyrir fyrirtæki eru hagsmunirnir fjárhagslegir og mannorðslegir: innbrotskostnaður, eftirlitssektir, týndir viðskiptavinir og lækkað verðmat. Fyrir hið opinbera ná þeir til þjóðaröryggis, almenningstrausts og samfellu nauðsynlegrar þjónustu. Bæði umhverfi deila hörðum sannleika: þú getur ekki framfylgt öryggi eingöngu með stýringum og hliðum. Það verður að vera tileinkað af fólkinu sem vinnur verkið. Menning þar sem verkfræðingar skilja ógnir, finna fyrir eignarhaldi og eru verðlaunaðir fyrir að vekja áhyggjur skilar langtum betri niðurstöðum en sú sem reiðir sig á ofhlaðið öryggisteymi sem spilar markvörð.

Þessi kafli leggur fram hugarlíkönin og menningarvenjurnar sem liggja til grundvallar hverjum öðrum öryggiskafla í þessari handbók. Hann nær yfir að gera öryggi að verki allra, [ógnarmótun](https://en.wikipedia.org/wiki/Threat_model), öruggan þróunarlífsferil, grunnarkitektúrreglur eins og [vörn í dýpt](https://en.wikipedia.org/wiki/Defense_in_depth_(computing)) og [núlltraust](https://en.wikipedia.org/wiki/Zero_trust_security_model), og hvernig á að forgangsraða öryggisvinnu eftir raunverulegri áhættu frekar en ótta eða tísku.

*Sjá einnig:* kafla 4.2 (forritaöryggi), kafla 4.3 (innviða- og skýjaöryggi), kafla 4.4 (öryggisrekstur) og kafla 4.6 (regluvörslu og stjórnarhætti) sem byggja á þessum grunni.

## Meginreglur

- **Öryggi er verk allra.** Sérhver verkfræðingur, vörustjóri og rekstraraðili á öryggi þess sem hann smíðar. Öryggisteymið gerir kleift, ráðleggur og úttekur. Það vinnur ekki og getur ekki unnið verkið eitt.
- **Gerðu ráð fyrir broti.** Hannaðu eins og árásaraðilar séu þegar inni. Lágmarkaðu hvað brotinn íhlutur nær til.
- **Vörn í dýpt.** Engin ein stýring nægir. Lagskiptu óháðar stýringar svo bilun einnar þýði ekki bilun allra.
- **[Lágmarksréttindi](https://en.wikipedia.org/wiki/Principle_of_least_privilege).** Veittu lágmarksaðgang sem þarf, í lágmarkstíma, og afturkallaðu hann sjálfvirkt þegar hans er ekki lengur þörf.
- **Færðu til vinstri.** Finndu og lagaðu vandamál eins snemma og hægt er, þegar ódýrast er að bæta úr.
- **Áhættubyggð forgangsröðun.** Eyddu fyrirhöfn þar sem samsetning líkinda og áhrifa er hæst, leidd af CIA-þríhyrningnum (trúnaði, heilleika og aðgengi), ekki því sem komst í fréttir þessa vikuna.
- **Nám án sakbendingar.** Líttu á öryggisatvik og næstum-slys sem námstækifæri, ekki tilefni til refsingar.

## Ráðleggingar

### Komdu á öryggismeistaraáætlun

Felldu tilnefndan öryggismeistara inn í hvert verkfræðiteymi. Meistarar eru ekki fullar öryggissérfræðingar. Þeir eru verkfræðingar með aukaþjálfun og beina línu til miðlæga öryggisteymisins. Þeir rýna hönnun, flokka niðurstöður, svara spurningum liðsfélaga og bera öryggissamhengi inn í áætlanagerð. Þetta stigvaxar öryggissérfræðiþekkingu yfir skipulagsheildina án þess að ráða sérfræðing í hvert teymi, og það byggir upp traust, því ráðgjöfin kemur frá jafningja sem þekkir kóðagrunninn í raun.

Gefðu meisturum raunverulegan stuðning: reglulegan vettvang til að deila því sem þeir læra, fjárhagsáætlun fyrir þjálfun og ráðstefnur, viðurkenningu í frammistöðumati og tíma skorinn úr afhendingarskuldbindingum þeirra. Meistaraáætlun sem er til aðeins á pappír framleiðir ekkert.

### Æfðu ógnarmótun reglulega

Ógnarmótun er agaður vani að spyrja „hvað gæti farið úrskeiðis?“ áður en þú smíðar. Gerðu hana fyrir nýjar þjónustur, stóra eiginleika og hverja breytingu á traustmörkum. Haltu henni nógu léttri til að hún gerist í raun oft.

- **[STRIDE](https://en.wikipedia.org/wiki/STRIDE_model)** er hagnýtur gátlisti varpaður á öryggiseiginleika: Spoofing (auðkenning), Tampering (heilleiki), Repudiation (óafneitanleiki), Information disclosure (trúnaður), Denial of service (aðgengi) og Elevation of privilege (heimild). Gakktu hvert gagnaflæði og spyrðu hvernig hver flokkur á við.
- **PASTA** (Process for Attack Simulation and Threat Analysis) er þyngri, áhættumiðuð sjö stiga aðferð sem tengir tæknilegar ógnir við viðskiptaáhrif. Notaðu hana fyrir kerfi af miklu verðmæti.
- **[Árásartré](https://en.wikipedia.org/wiki/Attack_tree)** sundurliða markmið („stela viðskiptavinagögnum“) í greinóttu skrefin sem árásaraðili myndi taka, sem hjálpar þér að finna og snyrta leiðir.

Haltu ógnarlíkönum sem lifandi skjölum við hlið kóðans og endurskoðaðu þau hvenær sem arkitektúrinn breytist.

### Byggðu öruggan hugbúnaðarlífsferil

Fléttaðu öryggi inn í hvert skeið frekar en að líta á það sem lokahlið:

- **Kröfur:** fangaðu öryggis- og persónuverndarkröfur við hlið virknikrafna.
- **Hönnun:** ógnarmótaðu og rýndu traustmörk.
- **Útfærsla:** framfylgdu öruggum kóðunarstöðlum, kóðarýni og leyndarmálaskönnun fyrir innritun.
- **Prófun:** keyrðu [SAST](https://en.wikipedia.org/wiki/Static_application_security_testing) (kyrrstæða forritaöryggisprófun), [DAST](https://en.wikipedia.org/wiki/Dynamic_application_security_testing) (kvika forritaöryggisprófun) og ósjálfstæðisskönnun í leiðslunni (sjá kafla 4.4).
- **Útgáfa:** staðfestu herkomu, undirritaðu gripi og athugaðu stillingu.
- **Rekstur:** vaktaðu, plástraðu og bregstu við.

Tilgangur þess að færa til vinstri er ekki að hrúga öllu verkinu fyrr og yfirbuga verkfræðinga. Hann er að grípa þær tegundir galla sem eru miklu ódýrari að laga snemma.

### Taktu upp núlltraustarkitektúrreglur

Hefðbundið jaðaröryggi gerir ráð fyrir að allt innan netsins sé áreiðanlegt. Sú forsenda bregst um leið og árásaraðili nær fótfestu. Núlltraust kemur í stað óbeins nettrausts með skýrri, samfelldri staðfestingu: auðkenndu og heimilaðu hverja beiðni út frá auðkenni, tækjastöðu og samhengi, sama hvaðan hún kemur á netinu. Sameinaðu sterkt auðkenni, lágmarksréttindaheimild, örskiptingu í hluta og [dulkóðun](https://en.wikipedia.org/wiki/Encryption) alls staðar. Núlltraust er ferðalag, ekki vara, svo nálgastu það eitt skref í einu.

### Forgangsraðaðu eftir áhættu með CIA-þríhyrningnum

Rammaðu hverja eign og stýringu um **trúnað**, **heilleika** og **aðgengi**. Ekki öll gögn þurfa sömu vernd: opinber markaðssíða og gagnagrunnur heilsufarsskráa hafa gríðarlega ólíkar trúnaðarþarfir. Flokkaðu eignir þínar, metaðu líkur og áhrif brots og beindu af skornum skammti öryggisfyrirhöfn að áhættumestu samsetningunum. Skrifaðu niður áhættuákvarðanir þínar svo aðrir geti rýnt og varið þær síðar.

## Málamiðlanir: kostir og gallar

| Nálgun | Kostir | Gallar |
|---|---|---|
| Miðlægt öryggisteymi á allt öryggi | Djúp sérfræðiþekking, samræmdir staðlar | Flöskuháls, verkfræðingar missa áhuga, stigvaxar ekki |
| Dreift öryggi (meistarar) | Stigvaxar, byggir eignarhald, hraðari endurgjöf | Krefst fjárfestingar, ójöfn færni, þarfnast samhæfingar |
| Þung fyrirframógnarmótun fyrir allt | Ítarleg, grípur hönnunargalla | Hægir afhendingu, getur orðið hakæfing |
| Létt, áhættumiðuð ógnarmótun | Hröð, einbeitt að því sem skiptir máli | Getur misst af ógnum í „áhættulitlum“ kerfum |
| Strang hlið sem hindra útgáfur | Framfylgir regluvörslu | Núningur, hvetur til sniðgöngu |

Meginspennan er hraði gegn tryggingu. Hallaðu þér of langt að hliðum og miðlægri stjórn og þú skapar núning sem verkfræðingar fara framhjá, sem elur skuggaupplýsingatækni og gremju. Hallaðu þér of langt að sjálfræði án stuðnings og þú færð ósamræmt, óúttektað öryggi. Sjálfbæra svarið er sterk menning með styðjandi handriðum: sjálfvirk þar sem þú getur, mannleg þar sem dómgreindar er þörf, og alltaf útskýrð frekar en einfaldlega lögð á.

## Spurningar til að ræða með teyminu

1. **Hvaða kerfi ykkar verðskulda þunga ógnarmótun og hver ákveður þrepið?** Í stóru búi geturðu ekki keyrt sjö stiga PASTA-greiningu á hverja þjónustu, svo þú þarft skýra reglu um hvenær 30 mínútna STRIDE-yfirferð nægir og hvenær kerfi af miklu verðmæti verðskuldar djúpa, viðskiptaáhrifadrifna líkanagerð. Festu ákvörðunina í CIA-flokkun þinni: kerfi sem halda eftirlitsskyldum skrám, greiðsluflæði eða auðkenningarrökfræði sitja efst, og opinber markaðssíða gerir það ekki. Fyrir fyrirtækja- og opinber verk mun endurskoðandi biðja þig að verja hvers vegna tiltekið kerfi var mótað eins og það var, svo skrifaðu þrepaviðmiðin niður og nefndu eigandann sem beitir þeim. Komdu með núverandi eignaflokkun þína og lista yfir þjónustur án ógnarlíkans á fundinn, því bilið milli þeirra er raunveruleg áhætta þín. Ef þið getið ekki komist að samkomulagi um viðmiðið munuð þið sjálfgefið móta allt létt eða ekkert djúpt, og hvort tveggja bregst ykkur.

2. **Þegar öryggismeistari og afhendingarfrestur rekast á, hver getur í raun stöðvað útgáfuna?** Meistaraáætlun breytir niðurstöðum aðeins ef meistarinn ber raunverulegt vald, ekki bara aukaþjálfun og góðan ásetning. Ákveddu fyrirfram hvort meistari geti hindrað afhendingu, hvort hann stigmagni til miðlæga AppSec-teymisins og hvaða alvarleiki niðurstöðu réttlætir að stöðva afhendingu á móti að rekja hana. Þetta skiptir mestu undir þrýstingi, þegar vörustjóri vill afsala sér hönnunargalla vikuna fyrir opnun, sem er einmitt þegar óleystir gallar eru dýrastir að laga. Komdu með nýlegt dæmi þar sem öryggisáhyggja mætti fresti og raktu hver ákvað og hvernig, því sú saga leiðir í ljós sanna stigmögnunarleið þína. Ef heiðarlega svarið er að afhending vinnur alltaf eru meistarar þínir skraut og þú ættir að laga hvatann áður en þú bætir við fleiri.

3. **Hvað breytir „gerðu ráð fyrir broti“ áþreifanlega í næstu hönnunarrýni ykkar?** Reglan er auðvelt að kinka kolli við og erfitt að framkvæma, svo festu hana við sértækar skuldbindingar: hvaða traustmörk þú munt herða, hvar þú munt bæta við örskiptingu og hvernig þú munt minnka það sem einn brotinn þjónustureikningur nær til. Fyrir stórt teymi er ávinningurinn sprengjusvæðisminnkun, svo árásaraðili sem lendir í einni þjónustu geti ekki snúið sér að gagnageymslunni á bak við. Í fyrirtækja- og opinberu umhverfi mótar þetta líka lágmarksréttinda- og skammlífra-auðkennisgagna ákvarðanir þínar, sem eru ódýrar að hanna inn og sársaukafullar að bæta við eftir á. Komdu með eitt raunverulegt þjónustuvirki og spyrðu hvað árásaraðili gerir eftir að hann á vefþrepið, skuldbittu þig síðan til tveggja afmörkunarbreytinga þennan ársfjórðung. Óljóst samkomulag um að brot gerist er einskis virði nema það hreyfi heimild, netreglu eða líftíma auðkennisgagna.

4. **Hvernig munið þið vita að öryggismenning ykkar er í raun að batna og hvaða mælikvarða myndir þú verja fyrir stjórninni?** Þjálfunarlokahlutföll og miðafjöldi eru auðveld að safna og nánast gagnslaus, því þau mæla virkni frekar en áhættuminnkun, og stór skipulagsheild drukknar í þeim. Veldu útkomumælikvarða sem þú myndir í raun veðja fjárhagsáætlun á: miðgildistíma til úrbóta á alvarlegum niðurstöðum, hlutfall þjónusta með núgildandi ógnarlíkan, hlutfall atvika gripinna fyrir framleiðslu og hlutfall sjálfskýrðra næstum-slysa, sem ætti að hækka eftir því sem traust vex frekar en að lækka. Sjónarmiðið á móti er að sérhver góður mælikvarði má leika, svo paraðu hvern við gagnmælikvarða og rýndu þróunina frekar en mynd augnabliksins. Komdu með núverandi mælaborð og spyrðu hvaða tölur myndu breytast ef öryggi versnaði raunverulega. Þær sem gerðu það ekki eru skraut. Í fyrirtækja- og opinberu umhverfi mun eftirlitsaðili eða úttektarnefnd biðja um sönnunargögn um að stýringar virki, svo veldu mælikvarða sem þú getur varið undir athugun frekar en þá sem líta bara grænir út.

5. **Hvað gerist í raun næst þegar verkfræðingur tilkynnir mistök og er ferli ykkar án sakbendingar í reynd eða aðeins á skyggnunni?** Nám án sakbendingar er reglan sem oftast er boðuð og sjaldnast lifað, því fyrsta alvarlega atvik reynir hvort forysta meini það í raun. Ákveddu fyrirfram hvernig þú aðgreinir ábyrgð á að laga vandamál frá refsingu fyrir að hafa valdið því, og hver stýrir atvikarýninni svo hún haldist um bilað kerfi frekar en nafngreinda einstaklinga. Spennan er raunveruleg: hagsmunaaðilar vilja að einhver sé dreginn til ábyrgðar, samt tryggir að refsa tilkynnandanum að næstu mistök haldist falin þar til þau verða innbrot. Komdu með síðustu tvær atvikarýnir þínar og athugaðu hvort þær kenndu manneskju eða stýringu um, og hvort verkfræðingnum sem vakti viðvörun var þakkað eða hljóðlega ýtt til hliðar. Fyrir opinbera aðila og eftirlitsskyld fyrirtæki hækka skyldubundnar innbrotsupplýsingareglur hagsmunina enn frekar, því menning sem felur mistök mun líka missa af tilkynningarfrestunum sem bera lagalegar sektir.

6. **Hver á núninginn af vinstri-færslu verkfærum ykkar og eruð þið að kaupa þau, smíða eða drukkna í þeim?** Sjálfvirk kyrrstæð og kvik greining, ósjálfstæðisskönnun og leyndarmálaskönnun eru burðarás öruggs þróunarlífsferils, en leiðsla sem flæðir verkfræðinga í röngum jákvæðum kennir þeim að hunsa öryggisúttak, sem er verra en engin skönnun. Ákveddu hver stillir verkfærin, hver flokkar niðurstöðurnar og hvort þú kaupir samþættan vettvang eða setur saman opna skanna sem þú þarft síðan sjálfur að viðhalda. Sjónarmiðin sem togast á eru þekja gegn hávaða og stjórn gegn kostnaði: ódýr skanni sem hrópar „úlfur“ brennir traustið sem meistaraáætlun eyddi árum í að byggja. Komdu með núverandi rangt-jákvæða hlutfall þitt, meðaltímann sem verkfræðingar bíða eftir hindrandi athugun og lista yfir teymi sem hafa hljóðlega afvirkjað hlið. Í stórum fyrirtækjum og hjá hinu opinbera skaltu bæta við innkaupa- og verkfæraútbreiðslusjónarhorninu, því tíu teymi sem kaupa hvert sinn skanna framleiða ósamræmda þekju sem enginn endurskoðandi getur sætt.

## Sjónarhorn eftir geirum

**Sprotafyrirtæki.** Án öryggisteymis og með lítið svigrúm er menning eina stýringin sem þú hefur efni á. Gerðu 30 mínútna ógnarmótunartöflufund að vana fyrir hvern eiginleika sem snertir auðkenningu eða greiðslur, kveiktu á lágmarksréttindum og MFA alls staðar því þau kosta ekkert og haltu rás án sakbendingar þar sem hver sem er getur vakið áhyggjur. Slepptu þungu ferli og verkfærum. Stofnverkfræðingarnir geta ekki viðhaldið því, og agin sem þú byggir núna er það sem leyfir fyrirtækjakaupendum að treysta þér síðar.

**Lítið fyrirtæki.** Þú hefur engan sérstakan öryggissérfræðing og þröngt fjárhagsáætlun, svo hallaðu þér að öruggum sjálfgefnum gildum í verkfærunum sem þú kaupir þegar frekar en að setja upp eigin leiðslu. Kjóstu stýrða vettvanga sem framfylgja MFA, plástrun og lágmarksréttindum fyrir þig og líttu á öryggi sem gagnahreinlætisspurningu: vittu hvaða viðkvæm gögn þú heldur og hver getur náð þeim. Þegar þú verður að velja milli smíða og kaupa skaltu kaupa, því stýrð stýring sem þú heldur núgildandi slær sérsmíðaða sem þú lætur rotna.

**Stórfyrirtæki.** Í stærð hundraða þjónusta og þúsunda verkfræðinga er áskorunin samræmi og stjórnarhættir yfir mörg teymi. Rektu öryggismeistaraáætlun, staðlaðu ógnarmótunarþrep tengd CIA-flokkun og útvegaðu sniðmát á troðnum slóðum og sjálfvirkar leiðsluathuganir svo hvert teymi erfi góð sjálfgefin gildi. Raktu úrbóta- og þekjumælikvarða gegn grunnlínum og haltu úttektarslóð sem sýnir hvers vegna hvert kerfi var mótað og stýrt eins og það var.

**Hið opinbera.** Innkaupareglur, gagnsæisskyldur og opinber ábyrgð móta hvert val. Núlltraustarreglur og skammlíf auðkennisgögn eru oft fyrirskipuð með framkvæmdastefnu, og þú verður að geta sýnt endurskoðanda skjalfestan, áhættubyggðan rökstuðning hvert hertunarfjárhagsáætlun fór. Forgangsraðaðu kerfunum sem halda viðkvæmustu borgaraskránum fyrst, birtu varnirnar þar sem almenningur á rétt á að vita og krefstu þess að söluaðilar upplýsi um takmarkanir frekar en að sætta þig við ógegnsæja svarta kassa.

## Dæmi

**Sprotafyrirtæki.** Tíu manna sprotafyrirtæki hefur ekkert öryggisteymi og enga fjárhagsáætlun fyrir eitt, svo stofnverkfræðingarnir tveir gera ógnarmótun að 30 mínútna töflufundi fyrir hvern eiginleika sem snertir auðkenningu eða greiðslur og spyrja hvað gæti farið úrskeiðis og hver myndi vilja það. Þeir taka upp nokkrar grunnvenjur sem kosta ekkert: lágmarksréttindi á hverju skýjahlutverki, MFA á hverjum reikningi og rás án sakbendingar þar sem hver sem er getur vakið áhyggjur án ótta við sök. Þegar þeir safna síðar fjármagni og fyrirtækjakaupendur spyrja hvernig þeir meðhöndli öryggi leyfir sú snemmbúna menning þeim að svara heiðarlega í stað þess að flýta sér að finna upp eina.

**Stórfyrirtæki.** Hnattrænn banki með 6.000 verkfræðinga rekur öryggismeistaraáætlun með einum þjálfuðum meistara á teymi. Meistarar sækja mánaðarlegt félag, ljúka ársfjórðungslegri þjálfun og leiða ógnarmótun fyrir hverja nýja þjónustu með STRIDE. Miðlæga AppSec-teymið viðheldur sniðmátum á troðnum slóðum og sjálfvirkum leiðsluathugunum. Á tveimur árum féll miðgildistími til úrbóta á alvarlegum niðurstöðum úr 45 dögum í 9, og ógnarmótun á hönnunarstigi greip heimildargalla í greiðslu-API áður en hann náði framleiðslu og kom í veg fyrir líklegt tilkynningarskylt atvik.

**Hið opinbera.** Landsbundið skattayfirvald sem nútímavæðir eldri kerfi tekur upp núlltraustarreglur fyrirskipaðar með framkvæmdastefnu. Hvert innra þjónustukall er auðkennt með skammlífum auðkennisgögnum og heimilað á hverja beiðni. Netskiptingar veita ekki lengur traust. Yfirvaldið ógnarmótar hverja borgarasnúna þjónustu gegn árásartrjám með rót í „stela skattskrám“ og „breyta framtali“. Áhættubyggð forgangsröðun, samræmd CIA-áhrifastigum, beinir hertunarfjárhagsáætlun að kerfunum sem halda viðkvæmustu skránum fyrst.

## Viðskiptarök: hvatar, ávöxtun fjárfestingar og heildarkostnaður

Kostnaður við að byggja öryggismenningu er raunverulegur: tími meistara, þjálfun, verkfæri og hóflegt álag þess að gera ógnarmótun og rýnir. En sá kostnaður er lítill miðað við kostnaðinn við að gera það ekki. Meðalstórt gagnainnbrot nemur milljónum þegar rannsókn, tilkynningar, úrbætur, eftirlitssektir, lagaleg útsetning og týnd viðskipti eru talin. Innbrot hjá hinu opinbera bæta við truflun verkefna og rýrnun almenningstrausts sem enginn reikningur nær fullkomlega.

Ávöxtun öryggisfjárfestingar kemur frá þremur stöðum: **forðuðum atvikum** (innbrotið sem gerist aldrei), **minni úrbótakostnaði** (gallar lagaðir við hönnun kosta brot af þeim sem lagaðir eru í framleiðslu) og **hraðari afhendingu** (troðnar slóðir og sjálfvirkar athuganir leyfa teymum að afhenda af öryggi frekar en að bíða eftir handvirkri rýni). Þegar þú færir rök við forystu skaltu ramma öryggi sem áhættustjórnun með verðmiða, ekki sem óhlutbundið gott. Sýndu væntanlegt tap (líkur sinnum áhrif) helstu áhættna, kostnaðinn við að draga úr þeim og áhættuna sem eftir stendur. Stjórnendur fjármagna áhættuminnkun sem þeir geta mælt.

## Andmynstur og gildrur

- **Öryggisleikhús.** Stýringar sem líta áhrifamiklar út en draga úr engri raunverulegri áhættu, teknar upp til að fullnægja úttekt frekar en að vernda nokkuð.
- **Öryggisteymið sem hlið í lokin.** Að uppgötva hönnunargalla vikuna fyrir opnun, þegar þeir eru dýrastir að laga og líklegastir til að vera afsalaðir.
- **Sakbendingarmenning.** Að refsa verkfræðingnum sem tilkynnir mistök tryggir að næstu mistök haldist falin.
- **Hakógnarmótun.** Að fylla út sniðmát sem enginn les og framleiða skjöl aðskilin frá raunverulegum arkitektúr.
- **Ein stýring fyrir alla.** Að beita sama þunga ferli á opinbera vefsíðu og greiðslukerfi, sem sóar fyrirhöfn og elur gremju.
- **Óttadrifin forgangsröðun.** Að elta hvaða veikleika sem er vinsæll í fréttum frekar en það sem í raun ógnar eignum þínum.
- **Meistarar að nafninu til.** Að nefna meistara án þess að gefa þeim tíma, þjálfun eða vald.

## Þroskalíkan

**Stig 1: Upphaf.** Öryggi er viðbragðsdrifið og miðlægt. Rýnir gerast seint ef yfirleitt og engin ógnarmótun er til. Atvik knýja ad hoc lagfæringar. Verkfræðingar líta á öryggi sem vanda einhvers annars og enginn sameiginlegur staðall er til.

**Stig 2: Þróun.** Öryggisteymi er til og skilgreinir staðla, en vinnubrögð eru ósamræmd milli teyma. Einhver ógnarmótun gerist á stórum verkefnum og engin á öðrum. Grunnþjálfun er í boði. Öryggi er enn talið hlið og vinstri-færsla er metnaður frekar en veruleiki.

**Stig 3: Stöðlun.** Öryggismeistarar eru felldir inn í hvert teymi. Ógnarmótun er rútína fyrir nýjar þjónustur, þrepuð gegn CIA-flokkun, og öruggur þróunarlífsferill er skjalfestur og framfylgt um alla skipulagsheildina. Áhættubyggð forgangsröðun leiðir verkið, öruggir kóðunarstaðlar og leiðsluathuganir eru sjálfgefna troðna slóðin og atvikarýnir án sakbendingar eru normið.

**Stig 4: Stjórnun.** Öryggisútkomur eru mældar og stýrðar gegn grunnlínum. Skipulagsheildin rekur miðgildistíma til úrbóta á alvarlegum niðurstöðum, ógnarlíkanaþekju, hlutfall atvika gripinna fyrir framleiðslu og næstum-slysa tilkynningarhlutföll, sundurliðað á teymi. Vald meistara til að stöðva útgáfu er skilgreint og beitt í raun. Áhættuákvarðanir eru magnsettar sem líkur sinnum áhrif, skráðar og rýndar á föstum takti, svo stýringarbil birtist sem gögn frekar en óvæntar uppákomur.

**Stig 5: Samhæfing.** Öryggi er í raun verk allra og samþætt afhendingu, áhættu og viðskiptaáætlun. Ógnarmótun og örugg hönnun eru vani og létt og núlltraustarreglur eru að mestu raungerðar. Mælikvarðar knýja stöðugar umbætur, skipulagsheildin lærir af næstum-slysum yfir teymi og stýringar aðlagast sjálfvirkt eftir því sem ógnamyndin og arkitektúrinn breytast.

## Hugmyndir til umræðu

1. Hvernig mælirðu hvort öryggismenning sé í raun að batna, umfram að telja lokna þjálfun?
2. Hvar er rétta línan milli þess sem öryggismeistarar meðhöndla og þess sem miðlæga teymið á?
3. Hvernig heldurðu ógnarmótun verðmætri án þess að láta hana verða skrifræðislegt hak?
4. Er fullur núlltraustarkitektúr raunhæfur fyrir eldra búið þitt og ef ekki, hver er hagnýta undirmengið?
5. Hvernig ætti að forgangsraða öryggisvinnu gegn afhendingu eiginleika þegar bæði keppa um sömu verkfræðinga?
6. Hvaða hvatar breyta í raun hegðun verkfræðinga í átt að öryggiseignarhaldi?

## Helstu atriði

- Öryggi er menningareiginleiki stórra skipulagsheilda, ekki verk falið einu teymi.
- Öryggismeistarar stigvaxa sérfræðiþekkingu og eignarhald yfir verkfræðina.
- Ógnarmótun (STRIDE, PASTA, árásartré) leiðir hönnunargalla í ljós snemma og ódýrt.
- Öruggur hugbúnaðarlífsferill og vinstri-færsluhugarfar grípa galla þegar þeir kosta minnst.
- Vörn í dýpt, lágmarksréttindi og núlltraust eru grunnarkitektúrreglurnar.
- CIA-þríhyrningurinn og áhættubyggð forgangsröðun beina af skornum skammti fyrirhöfn þangað sem hún skiptir mestu.
- Kostnaður við að byggja öryggismenningu er langtum minni en kostnaður innbrotanna sem hún kemur í veg fyrir.

## Heimildir og frekari lestur

- Adam Shostack, *Threat Modelling: Designing for Security*
- Ross Anderson, *Security Engineering: A Guide to Building Dependable Distributed Systems*
- Michael Howard and Steve Lipner, *The Security Development Lifecycle*
- Betsy Beyer et al. (Google), *Building Secure and Reliable Systems*
- National Institute of Standards and Technology, *SP 800-207: Zero Trust Architecture*
- National Institute of Standards and Technology, *Secure Software Development Framework (SSDF), SP 800-218*
- OWASP, *Threat Modelling* and *Security Champions* guidance
