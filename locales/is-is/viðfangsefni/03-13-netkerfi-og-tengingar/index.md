# 3.13 Netkerfi og tengingar

## Yfirlit og tilgangur

Sérhver beiðni sem forritið þitt sendir fer yfir net, og netið lætur sér fátt um frestina þína finnast. Milli kóðans þíns og gagnagrunnsins, greiðsluveitunnar eða vafrans situr stafli af hreyfanlegum hlutum: nafnaupplausn, leiðsögn, þrengslastýring, dulkóðunarhandsöl, álagsdreifar, milliþjónar og eldveggir. Flestir forritaverkfræðingar líta á allt þetta sem flata, áreiðanlega pípu, og sú forsenda er ríkasta uppspretta framleiðsluatvika. Klassísku [mýtur dreifðrar tölvunar](https://en.wikipedia.org/wiki/Fallacies_of_distributed_computing) (netið er áreiðanlegt, töf er núll, bandvídd er óendanleg, netskipan breytist aldrei, flutningskostnaður er núll) nefna einmitt trúna sem breytir litlum hiksta í rekstrarrof. Þessi kafli er ekki netvottunarnámskeið. Hann er vinnuþekkingin sem forritaverkfræðingur þarfnast í raun til að smíða kerfi sem haldast uppi þegar netið hegðar sér illa.

Fyrir stóra skipulagsheild er tenging þar sem arkitektúr mætir eðlisfræði og stjórnmálum í einu. Alþjóðlegt fyrirtæki saumar saman gagnaver, skýjasvæði, samstarfs-API og eldri kerfi, og hvert hopp bætir við töf, bilunarháttum og öryggismörkum sem einhver verður að eiga. Ríkisstjórnir bæta við ströngum reglum um hvernig umferð fer inn á og út af netum þeirra og hvert gögn borgara mega ferðast. Munurinn á teymi sem skilur netið og því sem hunsar það birtist í aðgengistölum, síðuhleðslutímum, innbrotsskýrslum og úttektarniðurstöðum. Efnið tengist dreifðum kerfum (kafli 3.3), stigvexti og seiglu (kafli 3.5), innviða- og skýjaöryggi (kafli 4.3) og dulritun og lyklastjórnun (kafli 4.8).

Góðu fréttirnar eru að þú þarft ekki að ná tökum á leiðsagnarsamskiptareglum til að smíða seig kerfi. Þú þarft að vita hvaða lög skipta máli fyrir ákvarðanir þínar, hvaðan töf kemur, hvernig nöfn leysast, hvernig tengingar eru tryggðar og álagsdreifðar og hvernig á að bila mjúklega á netmörkum. Fáðu þetta rétt og mestur hluti netsins verður áreiðanlegt undirlag.

## Meginreglur

- **Netið er ósjálfstæði, ekki gefið.** Líttu á hvert fjarkall sem eitthvað sem getur verið hægt, tapast eða logið til um hvort það kláraðist.
- **Töf ræðst af fjarlægð og umferðarlotum.** Þú getur ekki slegið ljóshraðann, svo fækkaðu umferðarlotum og færðu gögn nær notendum.
- **Nöfn bila oftar en vélar.** Nafnaupplausn og skírteini valda ótrúlegum hluta rekstrarrofa, svo líttu á þau sem fyrsta flokks rekstraráhyggjuefni.
- **Tryggðu og lúktu dulkóðun af ásetningi.** Vittu nákvæmlega hvar umferð er dulkóðuð, hvar hún er afkóðuð og hver heldur lyklunum.
- **Hver netmörk þurfa tímamörk og varaleið.** Ótakmörkuð bið og blindar endurtekningar breyta einu hægu ósjálfstæði í hnattrænt rekstrarrof.
- **Neitaðu sjálfgefið á jöðrum.** Skiptu netum í hluta, stýrðu því sem má fara út og gerðu ráð fyrir að jaðarinn sé þegar gegndræpur.
- **Fylgstu með tengingunni, ekki bara kóðanum.** Tengingavillur, endursendingar, handsalstímar og DNS-töf eru merki sem skrárnar þínar missa venjulega af.

## Ráðleggingar

### Skildu lögin sem í raun hafa áhrif á ákvarðanir þínar

Þú þarft ekki sjö laga líkanið utanbókar, en þú þarft hugarkort. Á flutningslaginu gefur [Transmission Control Protocol](https://en.wikipedia.org/wiki/Transmission_Control_Protocol) (TCP) þér raðaðan, áreiðanlegan bætastraum á kostnað handsals og röðunarhindrunar (head-of-line blocking), á meðan User Datagram Protocol (UDP) gefur þér ódýr, óröðuð gagnaskeyti án afhendingarábyrgðar. Áreiðanleg beiðni/svar umferð ferðast á TCP. Rauntímamiðlar, leikir og sum fjarmæling ferðast á UDP því seinn pakki er verri en týndur.

Þróun Hypertext Transfer Protocol ([HTTP](https://en.wikipedia.org/wiki/HTTP)) breytir afkastaþaki þínu. HTTP/1.1 meðhöndlar eina beiðni á tengingu í einu, svo vafrar opna margar tengingar og þú borgar endurtekin handsöl. HTTP/2 fjölfaldar marga strauma yfir eina TCP-tengingu, sem fjarlægir röðunarhindrun á forritastigi en ekki þá á TCP-stigi: einn týndur pakki stöðvar hvern straum á þeirri tengingu. HTTP/3 keyrir yfir QUIC, UDP-byggðan flutning sem gefur hverjum straumi óháða afhendingu, hraðari tengingaruppsetningu og tengingaflutning milli netbreytinga. Þú útfærir þetta sjaldan sjálfur, en þú velur það í álagsdreifum þínum, efnisdreifineti og biðlurum, og valið birtist í halatöf.

### Líttu á DNS og skírteini sem framleiðslukerfi

[Lénanafnakerfið](https://en.wikipedia.org/wiki/Domain_Name_System) (DNS) þýðir mannleg nöfn í vistföng og situr fyrir framan nánast hverja beiðni. Ótrúlega mörg stór rekstrarrof rekja sig til DNS: slæm skrárbreyting, útrunnið svæði, rangstilltur upplausnari, skyndiminnislag sem afgreiðir úrelt svör eða hægur valdbær þjónn sem bætir hundruðum millisekúndna við fyrsta bæti. Meðhöndlaðu DNS-breytingar af sömu nákvæmni og kóðauppsetningar. Notaðu skynsamleg lífstímagildi (TTL) svo þú getir fært umferð hratt í atviki án þess að bjóða úrelt skyndiminni í venjulegum rekstri, og vaktaðu upplausnartöf og bilanahlutföll sem raunverulega mælikvarða.

Skírteini verðskulda sömu alvöru. Þegar [Transport Layer Security](https://en.wikipedia.org/wiki/Transport_Layer_Security) (TLS) skírteini renna út ómerkt fara heilar þjónustur dimmar í einu, og bilunin lítur ekkert út eins og kóðagalli. Sjálfvirknivæddu útgáfu og endurnýjun, raktu fyrningardagsetningar miðlægt og gefðu viðvörun vel fyrir frestinn. Ákveddu af ásetningi hvar TLS lýkur: við jaðarálagsdreifi, við milliþjón eða alla leið að þjónustunni. Að ljúka á jaðrinum einfaldar innri umferð en skilur innra hoppið ódulkóðað nema þú dulkóðir aftur. Skírteinaveitur, lyklaskipti og dulmálsval eru fjallað um í kafla 4.8. Hér er rekstrarlega atriðið að DNS og skírteini bila hljóðlega og taka allt með sér, svo mældu og sjálfvirknivæddu hvort tveggja.

### Álagsdreifðu á réttu lagi og láttu milliþjóna vinna

[Álagsdreifing](https://en.wikipedia.org/wiki/Load_balancing_(computing)) dreifir umferð yfir marga bakenda og hvar þú gerir það skiptir máli. Lags 4 (L4) álagsdreifir leiðir eftir IP-vistfangi og gátt án þess að lesa hleðsluna, svo hann er hraður, óháður samskiptareglu og ódýr. Lags 7 (L7) álagsdreifir skilur HTTP, svo hann getur leitt eftir slóð eða haus, lokið TLS, endurtekið eins-áhrifa beiðnir og framfylgt hraðatakmörkunum, á kostnað meiri vinnu á beiðni. Mest forritaumferð vill L7 öfugan milliþjón eða API-gátt á jaðrinum, sem gefur þér einn stað til að meðhöndla TLS, auðkenningu, leiðsögn og sýnileika. Taktu L4 frá fyrir hrátt gegnumstreymi eða samskiptareglur sem eru ekki HTTP.

Heilsuathuganir eru það sem gerir álagsdreifingu örugga. Stilltu þær til að endurspegla raunverulega reiðubúð, ekki bara „ferlið er uppi“, svo bakendi sem nær ekki gagnagrunni sínum sé dreginn úr snúningi áður en hann afgreiðir villur, og tæmdu tengingar við uppsetningar svo beiðnir í flugi klárist. API-gátt miðlægir þverlæg atriði (auðkenningu, hraðatakmörkun, beiðnamótun, útgáfustýringu) en verður mikilvægt ósjálfstæði og hugsanlegur flöskuháls, svo gefðu henni sömu aðgengisfjárhagsáætlun og sýnileika og hverri kjarnaþjónustu.

### Færðu gögn nær notendum með CDN og jaðri

Töf ræðst af umferðarlotutíma, og umferðarlotutími ræðst af fjarlægð. [Efnisdreifinet](https://en.wikipedia.org/wiki/Content_delivery_network) (CDN) geymir efni í skyndiminni á viðverustöðum nálægt notendum svo kyrrstæðar eignir, og sífellt oftar kvik og sérsniðin svör, séu afgreidd frá nokkurra millisekúndna fjarlægð í stað handan hafs. Fyrir hverja notendasnúna vöru með landfræðilega dreifðan áheyrendahóp er CDN ein af afkastafjárfestingunum með hæstu ávöxtun sem þú getur gert, og hún tvöfaldast sem skjöldur sem gleypir umferðartoppa og magnárásir.

Ýttu vinnu út á jaðarinn þar sem það hjálpar. Að ljúka TLS á jaðrinum skerðir handsalstöf því dýru umferðarloturnar gerast nálægt notandanum, og að geyma API-svör í skyndiminni á jaðarstöðum styttir slóðina fyrir algengar beiðnir. Skiptin eru ógilding skyndiminnis: því nær og meira skyndiminnisgeymd sem gögn þín eru, því erfiðara er að tryggja ferskleika, svo vertu skýr um hvað má vera úrelt og hve lengi. Þetta tengist skyndiminnis- og afkastaumræðunni í kafla 3.5.

### Gerðu netmörkin seig sjálfgefið

Sérhvert fjarkall er staður þar sem netið getur skaðað þig, svo vefðu hvert þeirra í sama aga. Settu skýr tímamörk á hvert kall, því hangandi ósjálfstæði mun tæma tengingar- og þráðasjóði þína og stöðva allt á eftir. Endurtaktu aðeins aðgerðir sem eru öruggar til endurtekningar, notaðu veldisundanhald með skjálfta svo blik verði ekki að samstilltum endurtekningarstormi og settu þak á heildartilraunir og heildartíma. Bættu við rofa svo þú bilir hratt í kælitíma eftir þröskuld bilana í stað þess að hrúga beiðnum á þjónustu sem er þegar að drukkna. Þessi mynstur eru fjallað ítarlega í kafla 3.3. Atriðið hér er að þau eiga heima á netmörkunum sérstaklega, helst sem sameiginleg sjálfgefin gildi vettvangs frekar en eitthvað sem hvert teymi finnur upp aftur.

Fjárhagsáætlaðu tímamörk þín niður kallkeðjuna. Ef notendasnúin beiðni hefur tveggja sekúndna fjárhagsáætlun og fer yfir fjögur hopp verður hvert hopp að vita hversu lítill tími er eftir og bila hratt í stað þess að endurtaka út í tómið. Endurnýttu tengingar með sjóðum og keep-alive svo þú borgir ekki ferskt TCP- og TLS-handsal fyrir hverja beiðni, og fylgstu með halatöf, ekki bara meðaltölum, því hægasta eina prósentið er það sem notendur muna og það sem flæðir yfir undir álagi.

### Hannaðu og stýrðu netskipan þinni

Í skýinu er netið þitt hugbúnaður sem þú stillir, svo stilltu það af ásetningi. Settu vinnuálög í sýndareinkaský (VPC) og skiptu því í hluta: opinbert snúin þrep, forritaþrep og gagnaþrep í aðskildum undirnetum með reglum sem leyfa aðeins umferðina sem ætti að vera til. Stýrðu útleið jafn yfirvegað og inngangi. Óstýrður útgangsaðgangur er hvernig gögn fara út við innbrot og hvernig brotin vinnuálög ná stjórn-og-stýringarþjónum, svo leiddu útleiðandi umferð gegnum stýrðar gáttir og leyfilistaðu áfangastaðina sem raunverulega þarf að ná í. Skipuleggðu fyrir IPv6 frekar en að líta á það sem eftirþanka, því vistfangaþurrð og kröfur samstarfsaðila munu þvinga það fram á endanum og að bæta því við eftir á er sársaukafullt.

Taktu upp [núlltraustöryggislíkan](https://en.wikipedia.org/wiki/Zero_trust_security_model) (zero trust): hættu að líta á „inni í netinu“ sem treyst og auðkenndu og heimilaðu hverja beiðni út frá auðkenni frekar en netstaðsetningu. Í framkvæmd þýðir þetta gagnkvæmt TLS milli þjónusta, skammlíf auðkennisgögn og stefnu sem gerir ekki ráð fyrir að beiðni sé örugg bara því hún kom frá nágrannaundirneti. Þjónustunet getur skilað miklu af þessu einsleitt. Með því að keyra hliðarvagnsmilliþjón við hlið hverrar þjónustu gefur net þér gagnkvæmt TLS, samræmdar endurtekningar og tímamörk og fjarmælingar á hvert hopp án þess að breyta forritskóða. Það bætir við rekstrarflækju og nokkurri töf, svo taktu það upp þegar þjónustufjöldi þinn gerir einsleita, kóðalausa framfylgd aukakostnaðarins virði. Núlltraust og skipting í hluta eru þróuð frekar í köflum 4.3 og 8.3.

## Málamiðlanir: kostir og gallar

| Ákvörðun | Kostir | Gallar / kostnaður |
|---|---|---|
| L7 álagsdreifir / API-gátt | Snjöll leiðsögn, TLS-lúkning, auðkenning, hraðatakmörkun, sýnileiki | Meiri töf á beiðni, mikilvægt sameiginlegt ósjálfstæði |
| L4 álagsdreifir | Hraður, óháður samskiptareglu, ódýr | Sér ekki eða bregst við HTTP, engin efnismeðvituð leiðsögn |
| TLS-lúkning á jaðri | Hraðari handsöl, einfaldari bakendar | Innra hoppið ódulkóðað nema þú dulkóðir aftur |
| CDN og jaðarskyndiminni | Stór tafarsigur, gleypir toppa og árásir | Ógilding skyndiminnis og úrelding, aukakostnaður og stilling |
| Þjónustunet | Einsleitt gagnkvæmt TLS, endurtekningar, fjarmæling án forritsbreytinga | Rekstrarflækja, hliðarvagnstöf og tilfangakostnaður |
| HTTP/3 yfir QUIC | Engin röðunarhindrun á flutningi, hröð uppsetning, tengingaflutningur | Nýrri verkfæri, UDP stundum hamið, erfiðara að villuleita |

Meginspennan er milli stjórnar og einfaldleika. Sérhver öflugur íhlutur sem þú bætir við á netmörkunum (L7 gátt, net, CDN, útleiðarmilliþjónn) kaupir þér leiðsagnargreind, öryggisframfylgd og sýnileika, og hver bætir líka við hoppi, bilunarhætti og einhverju til að reka. Leystu það með því að ýta sameiginlegum áhyggjuefnum á sameiginlega innviði aðeins þegar nógu mörg teymi þurfa þau til að réttlæta rekstrarþyngdina, og með því að halda hröðu leiðinni stuttri. Tveggja manna sprotafyrirtæki sem lýkur TLS á stýrðum álagsdreifi og lætur þar við sitja gerir betri málamiðlun en sama teymi sem handsmíðar þjónustunet. Þúsund þjónusta fyrirtæki án einsleits gagnkvæms TLS og útleiðarstýringar gerir verri.

## Spurningar til að ræða með teyminu

1. **Hvar lýkur TLS í hverri beiðnaleið ykkar og geta allir teiknað það eins?** Þetta hljómar eins og smáatriði þar til atvik verður. Ef helmingur teymisins trúir að umferð sé dulkóðuð frá enda til enda og hinn helmingurinn veit að hún er afkóðuð á jaðrinum og send í skýrum texta til bakendans hefurðu bæði öryggisbil og villuleitargildru. Fyrir stóra skipulagsheild kortleggst þessi spurning beint á regluvörslu: eftirlitsaðilar og endurskoðendur munu spyrja hvar gögn borgara eða viðskiptavina ferðast í skýru og „við erum ekki viss“ er niðurstaða. Komdu með raunverulega teikningu af einni raunverulegri leið frá biðlara til gagnagrunns, sem merkir hvern punkt þar sem dulkóðun byrjar og endar og hver heldur hverju skírteini og lykli. Svarið ætti að segja þér hvort þú þarft innri endurdulkóðun, hvar gagnkvæmt TLS á heima og hvaða skírteini myndu taka þjónustu niður ef þau rynnu út. Ef enginn getur teiknað það af öryggi er það bil fyrsta verkefni þitt.

2. **Hvað verður um kerfið ykkar þegar DNS er hægt eða rangt og hafið þið í raun prófað það?** DNS er andstreymis nánast hverrar beiðni, samt hafa flest teymi aldrei séð kerfið sitt undir DNS-skerðingu. Hægur upplausnari bætir töf við hverja nýja tengingu, úrelt skyndiminni getur sent umferð til niðurlagðs gestgjafa og slæm skrárbreyting getur svelgt heila þjónustu á sekúndum. Í stóru fyrirtæki er sprengjusvæðið víðara því innri þjónustuuppgötvun, samstarfssamþættingar og skýjaendapunktar reiða sig allir á nafnaupplausn. Komdu með DNS-TTL stillingar þínar, upplausnartafarmælikvarða ef þú hefur þá og keyrsluhandbókina fyrir slæma skrárbreytingu, spyrðu síðan hve hratt þú gætir í raun fært umferð í atviki. Svarið ætti að ráða hvort þú vaktar upplausn sem fyrsta flokks mælikvarða, stillir TTL fyrir bæði lipurð og skyndiminnisnýtni og æfir DNS-yfirtöku. Ef þú hefur aldrei framkallað DNS-bilun í stýrðu prófi á sú tilraun heima í dagatalinu.

3. **Hvaða seigluminstur á netmörkum eru sjálfgefin gildi vettvangs og hvaða finnur hvert teymi upp aftur?** Tímamörk, afmarkaðar endurtekningar með skjálfta, rofar, tengingasjóðir og rekjun á hvert hopp eru ódýrust og áreiðanlegust þegar þau eru smíðuð einu sinni og erfð af öllum. Látin eftir einstökum teymum reka þau í sundur: sum köll hafa engin tímamörk, sum endurtaka ekki-eins-áhrifa aðgerðir, sum gefa út enga tengingastigsfjarmælingu og götin birtast aðeins undir álagi. Fyrir stórt teymi er þetta skipulagsval um hvar seigla býr, í sameiginlegu bókasafni eða vettvangslagi á móti dreifð yfir þjónustur. Komdu með úttekt á úrtaki þjónusta sem telur hve margar setja skýr tímamörk á hvert fjarkall og bera fylgniauðkenni frá enda til enda. Ef sú tala er lág er lagfæringin vettvangsfjárfesting, og að staðla hana gerir seiglu líka prófanlega og úttektarhæfa, sem skiptir sífellt meira máli í eftirlitsskyldum geirum. Svarið ætti að segja þér hvort þú fjármagnar netvettvangsgetu eða heldur áfram að borga fyrir ósamræmi í atvikum.

4. **Hvað getur hvert vinnuálag ykkar náð á opna internetinu núna og hver samþykkti hvern þessara útleiðandi áfangastaða?** Inngangur fær athyglina því þar knýja árásaraðilar á, en útleið er hvernig gögn fara í raun út við innbrot og hvernig brotið vinnuálag hringir heim í stjórn-og-stýringarþjón. Flest teymi geta talið upp hvað talar við þau mun auðveldar en við hvað þau tala, og sú ósamhverfa er einmitt bilið sem árásaraðili nýtir. Sjónarmiðið á móti er núningur: leyfilisti samþykktra áfangastaða hægir á hönnuðum sem vilja kalla á nýtt þriðja aðila API í dag, svo heiðarlega umræðan er hve mikil þægindi þú skiptir fyrir minna sprengjusvæði. Komdu með núverandi útleiðarreglur fyrir dæmigerða þjónustu, upptöku af hvert hún tengdist í raun síðustu viku og ferlið (ef nokkurt) til að samþykkja nýjan áfangastað. Fyrir fyrirtækja- og opinber kerfi er þetta ekki valkvæð hreinlætisgæsla heldur úttektarlína: mörkavernd og útleiðarskrár eru einmitt það sem eftirlitsaðilar og netmörkareglur krefjast að þú framleiðir, og „hvert vinnuálag getur náð hvert sem er“ er niðurstaða sem þér verður sagt að úrbæta.

5. **Samsetjast tímamörk og endurtekningar ykkar í eina samfellda fjárhagsáætlun niður hverja kallkeðju, eða giskar hvert hopp í einangrun?** Notendasnúin beiðni sem fer yfir fjórar þjónustur hefur einn frest sem notandinn finnur í raun, samt setur hvert hopp venjulega eigin tímamörk staðbundið, endurtekur inn í þjónustu sem hefur þegar gefist upp og sprengir heildarfjárhagsáætlunina meðan hún vinnur aukavinnu. Fyrir stórt teymi er hættan sprottin: einstaklega skynsamleg tímamörk á hverja þjónustu safnast í keðjustöðvun og samstilltan endurtekningarstorm sem ekkert eitt teymi sér af eigin mælaborði. Spennan er milli staðbundins sjálfræðis, þar sem hvert teymi stillir eigin mörk, og útbreidds tímafrests sem hvert hopp les og styttir eftir því sem tíma er varið. Komdu með raunverulega beiðnaleið með tímamarka- og endurtekningarstefnu á hverju hoppi, heildarfjárhagsáætlunina sem varan lofar og halatöfartölur þínar (p99, ekki meðaltal) undir álagi. Í eftirlitsskyldu og háaðgengissamhengi skaltu tengja þetta við endurheimtarmarkmið þín: keðja sem getur ekki bilað hratt innan fjárhagsáætlunar sinnar breytir einu hægu ósjálfstæði í brotið þjónustustigsmarkmið, og það brot er talan sem forysta og endurskoðendur munu biðja þig að útskýra.

6. **Við hvaða þjónustufjölda og umferðarsnið vinnur einsleit framfylgd (þjónustunet, L7 gátt, jaðarskyndiminni) sér inn rekstrarþyngd sína og hvar eruð þið á þeim ferli í dag?** Sérhver öflugur íhlutur sem þú bætir við á netmörkunum kaupir leiðsagnargreind, öryggi og sýnileika, og hver bætir líka við hoppi, bilunarhætti og einhverju til að reka allan sólarhringinn. Taktu upp þjónustunet of snemma og þú drekkir handfylli þjónusta í hliðarvagnsflækju. Taktu það upp of seint og þú hefur þúsund þjónustur án einsleits gagnkvæms TLS eða samræmdra endurtekninga. Sjónarmiðin sem togast á eru gildi kóðalausrar, samræmdrar framfylgdar yfir mörg teymi gegn raunverulegum kostnaði við að reka stjórnlagið, aukna töf og fáu fólkið sem getur villuleitað það. Komdu með núverandi þjónustufjölda þinn og vaxtarferil, hlutfall þjónusta sem eru þegar á sameiginlegum biðlurum sem veita sömu ábyrgðir og töfarrýmið sem þú hefur til að eyða. Fyrir stórt fyrirtæki eða stofnun er ákvörðunin líka stjórnarhátta: net eða miðlæg gátt leyfir vettvangsteymi að rúlla út stefnu alls staðar í einu, sem er öflugt fyrir regluvörslu og hættulegt ef sá einstaki flöskuháls er undirmannaður, svo fjárhagsáætlaðu það sem kjarnainnviði með eigin aðgengismarkmiði, ekki hliðarverkefni.

## Sjónarhorn eftir geirum

**Sprotafyrirtæki.** Hallaðu þér að stýrðum innviðum og eyddu knappri verkfræðiathygli í vöruna, ekki pakka. Stýrður L7 álagsdreifir sem lýkur TLS með sjálfendurnýjuðum skírteinum, auk CDN fyrir framan forritið þitt, kaupir þér dulkóðaða, álagsdreifða, hnattrænt hraða umferð án rekstrarteymis. Vefðu hvert utanaðkomandi kall í lítinn sameiginlegan biðlara með tímamörkum og afmarkaðri endurtekningu og stattu gegn þjónustuneti þar til þú hefur miklu fleiri þjónustur en fólk til að reka það.

**Lítið fyrirtæki.** Þú hefur engan netsérfræðing og þröngt fjárhagsáætlun, svo líttu á tengingu sem eitthvað sem þú kaupir stillt frekar en smíðar. Veldu skýjaveitu eða vettvang þar sem sjálfgefin gildi gefa þér þegar sjálfvirk skírteini, DNS-stjórnun og skynsaman eldvegg, og kveiktu á því sem þau bjóða frekar en að setja það saman sjálfur. Þar sem þú verður að ákveða skaltu kjósa stýrða valkostinn: að borga söluaðila fyrir að endurnýja skírteini og vakta DNS er miklu ódýrara en rekstrarrofið sem gleymd fyrning veldur.

**Stórfyrirtæki.** Vandinn þinn er samræmi yfir mörg teymi og svæði: einsleitt gagnkvæmt TLS, staðluð tímamörk og endurtekningar, stýrð útleið og skírteina- og DNS-vöktun sem ekkert eitt teymi getur valið að sleppa. Ýttu þessu inn í sameiginlega vettvangsinnviði (þjónustunet, innri gátt, sameiginlegt biðlarasafn) svo seigla sé erfð frekar en fundin upp aftur, og stýrðu netmörkunum með sömu aðgengisfjárhagsáætlun og sýnileika og hverri kjarnaþjónustu. Skiptu VPC í hluta, stýrðu útleið miðlægt og líttu á netskipan sem hugbúnað sem þú úttekur.

**Hið opinbera.** Innkaupareglur, gagnsæi og opinber ábyrgð móta hver mörk. Leiddu internetbundna umferð gegnum fáar hertar, vaktaðar gáttir, skráðu hvern ytri endapunkt og keyrðu núlltraustarkitektúr þar sem þjónustur auðkenna sig með auðkenni og skammlífum auðkennisgögnum frekar en netstaðsetningu. Líttu á DNS- og skírteinastjórnun sem mikilvæga innviði með sérstakri vöktun, því eitt útrunnið skírteini á borgarasnúinni þjónustu býður bæði opinberri og löggjafarlegri athugun heim, og haltu sönnunargögnum úttektarhæfum svo mörkaverndarrýni finni skjalfesta, rökstudda hönnun.

## Dæmi

**Sprotafyrirtæki.** Tíu manna hugbúnaður-sem-þjónusta fyrirtæki rekur allt á bak við einn stýrðan L7 álagsdreifi sem lýkur TLS með sjálfvirkt endurnýjuðum skírteinum og setur CDN fyrir framan vefforrit sitt og API. Sú samsetning gefur þeim hraðar hnattrænar síðuhleðslur, gleypir stöku umferðartopp frá vöruopnun og ver upptökin án sérstaks rekstrarteymis. Þau setja skýr tímamörk og afmarkaða endurtekningu á hvert kall á greiðsluveitu sína og tölvupóstþjónustu, vafið í lítinn sameiginlegan biðlara, svo hægur þriðji aðili hengi aldrei notendabeiðni. Þau standast að bæta við þjónustuneti: með tylft þjónusta myndi rekstrarkostnaðurinn dverga ávinninginn, og stýrðir innviðir gefa þeim þegar dulkóðaða, álagsdreifða umferð.

**Stórfyrirtæki.** Fjölþjóðleg smásala rekur yfir þrjú skýjasvæði og eldra gagnaver á staðnum, tengd með einkatengingum frekar en opna internetinu svo birgða- og greiðsluumferð fari aldrei yfir opin net. Hvert svæði situr í VPC skiptu í hluta með aðskildum opinberum, forrita- og gagnaundirnetum, og öll útleiðandi umferð flæðir gegnum útleiðargáttir sem leyfilista samþykkta áfangastaði, svo brotið vinnuálag geti ekki hljóðlega lekið gögnum. Hundruð þjónusta eiga samskipti gegnum þjónustunet sem framfylgir gagnkvæmu TLS alls staðar og beitir einsleitum endurtekningum, tímamörkum og rekjun, sem leyfir miðlægu vettvangsteymi að rúlla út nýrri endurtekningarstefnu án þess að snerta forritskóða. Miðlæg skírteinavöktun gefur viðvörun um fyrningar dögum fyrirfram og sjálfvirkni skiptir þeim út áður en nokkur viðskiptavinur tekur eftir.

**Hið opinbera.** Landsbundin stofnun starfar undir netmörkaverndarreglum sem leiða alla internetbundna umferð gegnum fáar hertar, vaktaðar gáttir, í samræmi við traust-internettengingar líkanið. Umferð milli stofnana keyrir yfir einkatengingar og hver ytri endapunktur er skráður, svo öryggisteymi vita nákvæmlega hvað getur komið inn og farið út. Stofnunin rekur núlltraustarkitektúr þar sem þjónustur auðkenna sig hver fyrir annarri með auðkenni og skammlífum auðkennisgögnum og engri beiðni er treyst aðeins fyrir að eiga uppruna innan jaðarsins. DNS- og skírteinastjórnun eru meðhöndluð sem mikilvægir innviðir með sérstakri vöktun, því eitt útrunnið skírteini eða slæm svæðisbreyting gæti tekið borgarasnúna bótagátt af netinu og kallað fram bæði opinbera og löggjafarlega athugun.

## Viðskiptarök: hvatar, ávöxtun fjárfestingar og heildarkostnaður

Netagi er keyptur ódýrt og fjarvera hans er greidd á versta hugsanlega augnabliki. Fjárfestingin er að mestu einskiptis og vettvangsmótuð: sameiginlegir biðlarar með tímamörkum og endurtekningum, sjálfvirk skírteinastjórnun, DNS-vöktun, skynsamlega skipt VPC og jaðarskyndiminni. Hvert gagnast hverju teymi sem erfir það, svo jaðarkostnaður á teymi er lágur á meðan ávinningurinn safnast. CDN borgar sig sérstaklega oft tvisvar, skerðir bandvíddarkostnað upptaka á meðan það bætir umbreytingar- og þátttökutölur sem fylgja hraðari síðuhleðslu.

Kostnaðurinn við að sleppa þessari vinnu er mældur í rekstrarrofum og innbrotum. Útrunnið skírteini eða slæm DNS-breyting getur tekið heila vöru af netinu á mínútum, með lagfæringu seinkaða meðan verkfræðingar elta ranga lagið. Vantandi tímamörk geta flætt eitt hægt ósjálfstæði yfir í fulla vettvangsstöðvun. Óstýrð útleið breytir einu brotnu vinnuálagi í gagnaleka. Rammaðu rökin við forystu í orðum sem hún fylgist þegar með: aðgengi, meðaltíma til endurheimtar, síðuhleðslutíma og innbrotsáhættu. Sjálfvirk skírteina- og DNS-stjórnun kemur í veg fyrir flokk sjálfskaðandi rekstrarrofa, jaðar- og CDN-fjárfesting hreyfir vöruafkastamælikvarða og skipting í hluta og útleiðarstýring minnka sprengjusvæði innbrota. Heildareignarkostnaðarrökin eru þau sem koma ítrekað fyrir í þessari handbók: að smíða getuna inn er brot af kostnaði við að bæta henni við eftir atvikið sem neyðir málið fram.

## Andmynstur og gildrur

- **Að gera ráð fyrir að netið sé áreiðanlegt og hratt.** Að kóða eins og fjarköll séu staðbundin, án tímamarka, án endurtekninga og án meðhöndlunar fyrir „rann út á tíma en kláraðist kannski“.
- **Handvirk skírteinastjórnun.** Að rekja fyrningu í töflureikni eða minni einhvers, sem tryggir endanlegt rekstrarrof þegar hún rennur ómerkt út.
- **Að hunsa DNS sem rekstrarkerfi.** Engin upplausnarvöktun, kæruleysisleg TTL og skrárbreytingar gerðar án nákvæmni uppsetningar.
- **Endurtekning án eins-áhrifa eða undanhalds.** Tvítekin hliðaráhrif og samstilltir endurtekningarstormar sem magna lítið blik í rekstrarrof.
- **Að treysta innra netinu.** Að líta á allt innan jaðarsins sem öruggt, með ódulkóðaðri innri umferð og engri auðkennisbyggðri heimild.
- **Óstýrð útleið.** Að leyfa vinnuálagi að ná hvaða útleiðandi áfangastað sem er og gefa árásaraðilum útleiðarslóð og rás til stjórnþjóna.
- **Málglaðar beiðnaleiðir.** Djúpar samstilltar kallkeðjur þar sem hvert hopp bætir við umferðarlotu, svo halatöf blæs upp undir álagi.
- **Að taka upp þjónustunet of snemma.** Að taka á sig hliðarvagnsflækju og töf fyrir handfylli þjónusta sem sameiginlegur biðlari myndi þjóna betur.

## Þroskalíkan

- **Stig 1, Upphaf:** Fjarköll eru meðhöndluð eins og staðbundin köll. Tímamörk og endurtekningar vantar eða eru barnaleg, og „rann út á tíma en kláraðist kannski“ er ómeðhöndlað. Skírteini og DNS eru stýrð í höndunum og valda óvæntum rekstrarrofum. Engin skipting í hluta er til og innri umferð er treyst sjálfgefið. Tengingavinna er viðbragðsdrifin og gerist aðeins eftir að atvik neyðir hana fram.
- **Stig 2, Þróun:** Sum teymi hafa tekið upp grunnvinnubrögð, en þau eru ósamræmd yfir þjónustur. Tímamörk og einfaldar endurtekningar eru til á stöðum, TLS er lokið við álagsdreifi og skírteini eru að mestu sjálfvirk. CDN fer fyrir framan kyrrstætt efni og grunnnetskipting er til, þó útleið sé að mestu opin og hvert teymi finni upp eigin biðlara. Það sem eitt teymi gerir vel hefur annað ekki byrjað á.
- **Stig 3, Stöðlun:** Seig netvinna er skjalfest og framfylgt um alla skipulagsheildina. Tímamörk, undanhald með skjálfta og rofar eru staðlað gegnum sameiginleg bókasöfn eða gátt sem hvert teymi erfir. DNS og skírteini eru vöktuð og sjálfvirk sem framleiðslukerfi, VPC eru skipt í hluta með stýrðum inngangi og útleið, tengingastigsfjarmæling er safnað alls staðar og núlltraustarreglur eru teknar upp sem stefna frekar en sem tilraun eins teymis.
- **Stig 4, Stjórnun:** Netmörkin eru mæld og stýrð gegn grunnlínum, ekki bara staðlað. Upplausnartöf, TLS-handsalstími, endursendinga- og tengingavilluhlutföll, halatöf (p99, ekki meðaltal), fyrirvari fyrir fyrningu skírteina og útleiðarstefnubrot eru rakin á mælaborðum með viðvörunarþröskuldum og villufjárhagsáætlunum. Fara/ekki-fara og getuákvarðanir eru knúnar af þeim gögnum, framkölluð DNS- og ósjálfstæðisbilunaræfingar eru keyrðar á áætlun og niðurstöður þeirra mældar, og afturför í einhverju merki er gripin og í eigu einhvers frekar en uppgötvuð í næsta rekstrarrofi.
- **Stig 5, Samhæfing:** Seig netvinna er stöðugt bætt sjálfgefið gildi vettvangs, samþætt um skipulagsheildina og aðlögunarhæf að breytingum. Gagnkvæmt TLS og auðkennisbyggð heimild eru einsleit, oft gegnum þjónustunet. Jaðar- og CDN-stefna er stillt gegn lifandi töfargögnum, útleið er fullstýrð og netskipan, veitu- og leiðsagnarval eru endurjöfnuð eftir því sem kostnaður, áhætta og umferð breytast. Netákvarðanir eru ofnar inn í getu-, öryggis- og viðskiptaáætlun og skipulagsheildin rökræðir skýrt um umferðarlotur, halatöf og mörkabilunarhætti sem sjálfsagðan hlut.

## Hugmyndir til umræðu

1. Ef aðal-DNS-veitandi þinn eða upplausnari skertist í klukkustund, hve mikið af kerfinu þínu myndi samt virka og hvernig myndirðu vita það?
2. Hverjar af þjónustum þínum senda enn umferð ódulkóðaða þegar hún er „inni í“ netinu og hvað þyrfti til að loka því bili?
3. Hvar eru dýpstu samstilltu kallkeðjurnar í arkitektúr þínum og hve margar netumferðarlotur verður dæmigerð notendabeiðni í raun fyrir?
4. Samsetjast tímamörk þín niður kallkeðjuna í samfellda fjárhagsáætlun, eða setur hvert lag sín eigin og vonar?
5. Hvað geta vinnuálög þín náð á opna internetinu núna og hver samþykkti hvern þessara útleiðandi áfangastaða?
6. Við hvaða fjölda þjónusta myndi einsleit framfylgd þjónustunets vega þyngra en rekstrarkostnaður þess fyrir skipulagsheildina þína og hve nærri ertu?

## Helstu atriði

- Netið er ósjálfstæði með eigin bilunarhætti. Hannaðu hvert fjarkall fyrir hægagang, tap og óljósa lokun, ekki bara árangur eða hreina bilun.
- Töf ræðst af umferðarlotum og fjarlægð, svo fækkaðu hoppum, endurnýttu tengingar og færðu gögn nær notendum með CDN og jaðri.
- DNS og TLS-skírteini bila hljóðlega og taka heilar þjónustur niður. Sjálfvirknivæddu og vaktaðu hvort tveggja sem framleiðslukerfi.
- Álagsdreifðu á laginu sem hentar umferðinni og settu sameiginleg áhyggjuefni á bak við L7 gátt aðeins þegar aðgengis- og sýnileikakostnaðurinn er réttlættur.
- Gerðu netmörkin seig sjálfgefið með tímamörkum, afmörkuðum endurtekningum með skjálfta og rofum, helst sem erfð sjálfgefin gildi vettvangs.
- Skiptu VPC í hluta, stýrðu útleið, skipuleggðu fyrir IPv6 og taktu upp núlltraust svo að vera „inni í“ netinu veiti engan sjálfvirkan trúnað.

## Heimildir og frekari lestur

- W. Richard Stevens, *TCP/IP Illustrated, Volume 1: The Protocols*
- Ilya Grigorik, *High Performance Browser Networking*
- Cricket Liu and Paul Albitz, *DNS and BIND*
- Andrew S. Tanenbaum and David J. Wetherall, *Computer Networks*
- Michael Nygard, *Release It!: Design and Deploy Production-Ready Software*
- Evan Gilman and Doug Barth, *Zero Trust Networks: Building Secure Systems in Untrusted Networks*
- Lee Calcote and Zack Butcher, *Istio: Up and Running* (service mesh concepts)
- Internet Engineering Task Force, RFC 9110 (HTTP Semantics) and RFC 9000 (QUIC)
- Peter Deutsch and James Gosling, "The Eight Fallacies of Distributed Computing"
- National Institute of Standards and Technology, *Special Publication 800-207: Zero Trust Architecture*
