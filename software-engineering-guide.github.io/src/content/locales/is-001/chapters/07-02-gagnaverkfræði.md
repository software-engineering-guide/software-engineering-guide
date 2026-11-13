# 7.2 Gagnaverkfræði

## Yfirlit og tilgangur

[Gagnaverkfræði](https://en.wikipedia.org/wiki/Data_engineering) er sú grein að smíða og reka leiðslurnar og vettvangana sem flytja gögn frá því þar sem þau verða til þangað sem þau skapa verðmæti. Hún nær yfir inntöku úr frumkerfum, umbreytingu í hrein og líkanuð form, geymslu á hagkvæmum sniðum, samstillingu alls flæðisins og áreiðanleikavinnubrögðin sem halda öllu traustverðu. Ef gagnastefna ákveður hvaða gögn ættu að vera til og hver á þau, þá er gagnaverkfræði lagnavinnan og vélbúnaðurinn sem lætur þau flæða.

Fyrir stór teymi er þessi grein grundvallaratriði. Greining, [viðskiptagreind](https://en.wikipedia.org/wiki/Business_intelligence), vörutilraunir, [vélnám](https://en.wikipedia.org/wiki/Machine_learning) og eftirlitsskýrslugerð sitja allt niðurstreymis gagnaleiðslna. Þegar þær leiðslur eru brothættar, hægar eða ógegnsæjar líður hver háð starfsemi. Mælaborð sýna úreltar tölur. Líkön þjálfast á spilltum eiginleikum. Úttektaraðilar geta ekki endurbyggt hvernig tala var framleidd. Í fyrirtækja- og opinberri stærð vinna leiðslur milljarða færslna úr mörgum frumkerfum og ein hljóð bilun getur ýtt röngum gögnum inn í ákvarðanir, greiðslur eða opinbera tölfræði.

Greinin hefur vaxið úr sérsmíðuðum skriftum og risavöxnum [ETL (draga út, umbreyta, hlaða)](https://en.wikipedia.org/wiki/Extract,_transform,_load) verkfærum í nútíma gagnastafla: einingabundna, mestmegnis SQL-drifna íhluti fyrir inntöku, umbreytingu, samstillingu og geymslu, tengda með opnum sniðum. Þessi einingabyggð er í senn gjöf og gildra. Hún leyfir þér að setja saman bestu verkfæri hverrar tegundar, en án verkfræðiaga framleiðir hún sundurleysi óskjalfestra, óprófaðra verka. Þessi kafli fjallar um vinnubrögðin sem halda leiðslum eins-áhrifa, prófanlegum, vaktanlegum og viðráðanlegum í kostnaði í stærð.

## Meginreglur

- Leiðslur eru hugbúnaður og eiga skilið útgáfustýringu, prófanir, rýni og CI/CD.
- Kjóstu eins-áhrifa, endurtakanlegar umbreytingar sem hægt er að keyra aftur örugglega.
- Gerðu gagnaflæði vaktanleg: ferskleiki, magn, skema og gæði eru vöktuð.
- Líkanaðu gögn af ásetningi fyrir notendur þeirra frekar en að demba hráum töflum.
- Veldu lotur eða straum út frá raunverulegum töfarþörfum, ekki nýjungagirni.
- Fínstilltu geymslusnið, skiptingu og reikniafl sem fyrsta flokks áhyggjuefni.
- Aðgreindu inntöku, umbreytingu og þjónustu svo hvert geti þróast sjálfstætt.
- Bilaðu hátt og snemma. Biluð leiðsla er öruggari en hljóðlega röng gögn.

## Ráðleggingar

### Veldu ETL eða ELT af ásetningi

ETL umbreytir gögnum áður en þau eru hlaðin í áfangastað. [ELT (draga út, hlaða, umbreyta)](https://en.wikipedia.org/wiki/Extract,_load,_transform) hleður hráum gögnum fyrst og umbreytir þeim inni í öflugu vöruhúsi eða vatnshúsi. Nútíma skýjavettvangar hafa gert ELT að sjálfgefnu vali, því geymsla er ódýr og reikniafl teygjanlegt, og að geyma hrágögn leyfir þér að endurvinna þegar rökfræði breytist eða villur koma upp. Kjóstu ELT fyrir greiningarvinnuálag: lentu hráum óbreytanlegum gögnum og byggðu síðan lagskiptar umbreytingar ofan á. Taktu frá umbreytingu fyrir hleðslu fyrir tilvik þar sem persónuvernd, kostnaður eða samningsskorður krefjast hreinsunar eða síunar áður en gögnin lenda.

### Hannaðu lotu- og straumleiðslur fyrir töfarþarfir þeirra

Flestar greiningarþarfir eru vel þjónað af tímasettum lotuleiðslum, sem eru einfaldari að rökræða um, prófa og endurfylla. Seilstu í streymi aðeins þegar viðskiptin þurfa raunverulega lágtafargögn: svikagreiningu, rekstrarviðvaranir, rauntímaaðlögun. Streymi bætir við raunverulegri flækju varðandi röð, nákvæmlega-einu-sinni merkingu, sein gögn og ástandsstjórnun. Þar sem þú þarft hvort tveggja skaltu íhuga arkitektúr sem sameinar lotu- og straumrökfræði frekar en að viðhalda tveimur ólíkum kóðagrunnum. Vertu heiðarlegur um töfarkröfur þínar. „Rauntími“ er oft óskoðuð ósk sem tvöfaldar kostnaðinn.

### Samstilltu með skýrum ósjálfstæðum

Notaðu samstilli til að tjá leiðslur sem [stefnd órásargröf (DAG)](https://en.wikipedia.org/wiki/Directed_acyclic_graph) verka með skýrum ósjálfstæðum, endurtilraunum og tímasetningu. Þetta gefur þér sýnileika á því sem keyrði, því sem bilaði og því sem er blokkað, auk getunnar til að endurfylla og endurkeyra ákvörðunarbundið. Byggðu ósjálfstæði á gagnaframboði, ekki bara klukkutíma, svo niðurstreymisverk bíði eftir andstreymisgögnum frekar en að ræsast á ágiskun. Haltu samstillingarrökfræði í útgáfustýringu og líttu á DAG-breytingar eins og kóðabreytingar.

### Líkanaðu gögn fyrir notkun

Hráar töflur eru sjaldan hæfar fyrir greinendur. Beittu [víddarlíkönun](https://en.wikipedia.org/wiki/Dimensional_modeling), sem raðar staðreyndum og samræmdum víddum í [stjörnuskemum](https://en.wikipedia.org/wiki/Star_schema), þar sem þú þarft stýrða, endurnýtanlega sjálfsafgreiðslugreiningu. Breiðar afstaðlaðar töflur („ein stór tafla“) geta staðið sig betur fyrir tiltekin fyrirspurnarmynstur og eru einfaldari fyrir suma notendur, á kostnað tvítekningar og sveigjanleika. Leggðu umbreytingar þínar í lög: hrátt millilag, hreinsað og samræmt kjarnalag og notendamiðaðar markaðsgeymslur. Þessi aðgreining leyfir þér að laga rökfræði á einum stað og leyfir notendum að reiða sig á stöðug viðmót.

### Gerðu leiðslur eins-áhrifa og prófanlegar

Hannaðu umbreytingar svo endurkeyrsla framleiði sömu niðurstöðu, frekar en að tvítaka eða spilla gögnum, til dæmis með ákvörðunarbundnum uppfærslu-eða-innsetningum lyklaðar á viðskiptaauðkenni og skiptingaryfirskriftarmynstrum. Skrifaðu próf á mörgum stigum: einingapróf fyrir umbreytingarrökfræði, skemapróf og gagnapróf sem staðhæfa væntingar eins og einkvæmni, lykla sem eru ekki núll, tilvísunarheilindi og viðurkennd gildasvið. Keyrðu þetta í CI, svo slæm breyting sé gripin áður en hún nær framleiðslugögnum.

### Komdu á vöktun og áreiðanleika

Vaktaðu fjögur kjarnamerki gagnaheilsu: ferskleika (er það uppfært), magn (er línufjöldinn innan væntanlegs sviðs), skema (hefur uppbyggingin breyst óvænt) og dreifingu (hafa gildi rekið óeðlilega). Varaðu við brotum og beindu þeim til eigandateymisins. Haltu keyrsluhandbókum, bakvaktarlotum og eftirmálsrýni án sakbendingar fyrir gagnaatvik, rétt eins og þú myndir gera fyrir þjónustur. Raktu ætterni, svo þegar eitthvað brotnar getir þú séð niðurstreymisáhrifin strax.

### Fínstilltu geymslu og kostnað

Notaðu súlnasnið með opnum stöðlum eins og Parquet, eða opin töflusnið sem styðja skemaþróun, tímaferðalög og skilvirkar uppfærslur. Skiptu gögnum eftir dálkunum sem þú síar mest á, venjulega dagsetningu, og forðastu ofgnótt smárra skráa með þjöppun. Aðgreindu heit og köld gögn með þrepaskiptri geymslu og lífsferilsstefnum. Vaktaðu reikniaflsútgjöld á leiðslu og á fyrirspurn. Stjórnlaus kostnaður kemur yfirleitt af fullum skönnunum, vantandi skiptingum og ótakmarkaðri endurvinnslu. Líttu á kostnað sem mælikvarða með eigendum, ekki óvænta tölu á mánaðarreikningnum.

## Málamiðlanir: kostir og gallar

| Val | Kostir | Gallar | Best passun |
|---|---|---|---|
| ELT (umbreyta á staðnum) | Geymir hrágögn, ódýr geymsla, endurvinnanlegt | Stórt geymslufótspor, krefst stjórnunar | Skýjagreining |
| ETL (umbreyta fyrir hleðslu) | Stýrir kostnaði, síar viðkvæm gögn snemma | Týnir hrágögnum, erfiðara að endurvinna | Regluverkuð eða skorðuð hleðsla |
| Lotur | Einfalt, prófanlegt, auðvelt að endurfylla | Meiri töf | Mest greining |
| Straumur | Lítil töf, rauntímaviðbrögð | Flókið, kostnaðarsamt, erfitt að prófa | Svik, rekstrarviðvaranir |
| Stjörnuskema | Stýrt, endurnýtanlegt, sjálfsafgreiðsluvænt | Líkanavinna fyrirfram | Sameiginleg viðskiptagreind |
| Breið tafla | Hröð fyrir þekktar fyrirspurnir, einföld | Tvítekning, minni sveigjanleiki | Þröng afkastamikil notkun |

Ríkjandi málamiðlunin er einfaldleiki gegn töf og sveigjanleika. Lotur og ELT með lagskiptum stjörnuskemum gefa þér prófanlegt, endurfyllanlegt, vel skilið kerfi sem þjónar flestum þörfum á viðráðanlegu verði. Straumur, rauntími og mjög afstöðluð hönnun kaupa hraða og tiltekin afköst, en á háu verði í rekstrarflækju og prófunarerfiðleikum. Taktu upp flækju aðeins þar sem áþreifanleg viðskiptakrafa borgar fyrir hana og haltu einföldu leiðinni sem sjálfgefinni.

## Spurningar til að ræða með teyminu

1. **Hafið þið valið ELT fram yfir ETL af ásetningi og haldið þið hráum óbreytanlegum gögnum svo þið getið endurunnið þegar rökfræði breytist eða villur koma upp?** Sjálfgefið í kaflanum er ELT: lentu hráum gögnum ódýrt, byggðu síðan lagskiptar umbreytingar, því að geyma hrágögn leyfir þér að keyra allt aftur þegar regla breytist eða villa birtist vikum síðar. Að eyða hrágögnum lokar þeim möguleika og er algeng, sársaukafull gildra. Rökin fyrir ETL eru raunveruleg í regluverkuðum eða skorðuðum hleðslum, þar sem persónuvernd, kostnaður eða samningsskilmálar krefjast síunar eða grímunar áður en gögn lenda. Komdu með sönnunargögn: hve oft hafið þið þurft að endurvinna sögu og hvað kostaði það þegar þið gátuð það ekki? Fyrir opinbera eða fyrirtækjaleiðslu sem verður að rekja hverja tölu til uppsprettu eru óbreytanlegar hráskrár líka úttektarkrafa, svo svarið mótar bæði geymslustefnu ykkar og lagalega verjanleika.

2. **Hver af fjórum gagnaheilsumerkjum vaktið þið í raun og hver er kallaður út þegar eitt brotnar?** Kaflinn nefnir fjögur merki sem vert er að horfa á: ferskleika, magn, skema og dreifingu. Mörg teymi vakta ekkert þeirra og læra um bilanir af stjórnanda sem starir á úrelt mælaborð, sem er versti mögulegi greinirinn. Í fyrirtækja- og opinberri stærð getur ein hljóð bilun ýtt röngum gögnum inn í greiðslur, skýrslur eða opinbera tölfræði, svo kostnaður seinnar greiningar er mældur í trausti og peningum, ekki bara endurvinnu. Komdu með raunverulegan meðaltíma til greiningar og nafn þess sem finnur atvik fyrst í dag. Ef svarið er „notandi“ þarftu viðvaranir beint til eigandateymisins auk keyrsluhandbóka og eftirmálsrýni án sakbendingar, og líta á gagnaatvik nákvæmlega eins og þjónusturof.

3. **Nota greinendur ykkar líkanaðar, prófaðar markaðsgeymslur, eða dembið þið hráum töflum á þá og kallið það sjálfsafgreiðslu?** Kaflinn er skýr: hráar töflur eru sjaldan hæfar fyrir greinendur og að leggja umbreytingar í hrátt millilag, samræmt kjarnalag og notendamiðaðar markaðsgeymslur leyfir þér að laga rökfræði einu sinni og gefa notendum stöðug viðmót. Togið á móti er hraði, þar sem líkanavinna með stjörnuskemum eða yfirveguðum breiðum töflum kostar fyrirhöfn fyrirfram og freistandi er að sleppa henni. En að demba hráum gögnum færir líkanakostnaðinn á hvern greinanda aftur og aftur, sem framleiðir ólíkar tölur og sóaða tíma. Komdu með merki: hve hátt hlutfall af tíma greinenda fer í að endurmóta hrá gögn og hve mörg teymi hafa endurbyggt sömu tengingar. Ef talan er há skaltu fjárfesta í samræmdu kjarnalagi svo notendur reiði sig á prófuð, endurnýtanleg viðmót í stað þess að finna þau upp aftur.

4. **Hvar vinnur „rauntími“ sér raunverulega inn kostnað sinn og hvar er hann óskoðuð ósk sem hljóðlega tvöfaldar rekstrarbyrði ykkar?** Sjálfgefið í kaflanum eru tímasettar lotur, sem eru einfaldari að rökræða um, prófa og endurfylla, og straumur tekinn frá fyrir tilvik þar sem viðskiptin þurfa raunverulega litla töf, svo sem svikagreiningu eða rekstrarviðvaranir. Togið á móti er álitið sem fylgir og óljósar beiðnir hagsmunaaðila um „lifandi“ gögn, sem hljóma ódýrar á skipulagsfundi og verða dýrar í framleiðslu, því straumur dregur með sér röð, nákvæmlega-einu-sinni merkingu, sein gögn og ástandsstjórnun, auk annars kóðagrunns til að halda í takt við lotu rökfræðina. Komdu með sönnunargögn í umræðuna: fyrir hverja straumleiðslu sem þið rekið eða leggið til skaltu nefna ákvörðunina sem hún nærir og töfina sem sú ákvörðun þolir í raun, mælda í mínútum eða klukkustundum frekar en lýsingarorðum. Fyrir stóran vettvang fyrirtækja eða hins opinbera skaltu bæta við bakvaktar- og prófunarkostnaði hverrar rauntímaleiðar, því straumleiðsla sem enginn getur prófað eða mannað allan sólarhringinn er áreiðanleikaskuld klædd sem eiginleiki, og heiðarlega svarið hrynur oft „rauntíma“ kröfu aftur í klukkutímalegar lotur sem þjóna sömu ákvörðun.

5. **Hverjar leiðslna ykkar er ekki hægt að endurkeyra örugglega í dag og hvað þyrfti til að gera hverja umbreytingu eins-áhrifa?** Kaflinn krefst eins-áhrifa, endurtakanlegra umbreytinga, með ákvörðunarbundnum uppfærslu-eða-innsetningum lyklaðar á viðskiptaauðkenni og skiptingaryfirskriftarmynstrum, svo endurkeyrsla framleiði sömu niðurstöðu frekar en að tvítaka eða spilla gögnum. Þrýstingurinn á móti er afhendingarhraði, þar sem barnalegt viðbótarverk afhendist hraðar en eitt hannað til endurkeyrslu og kostnaður þeirrar styttingar helst falinn þar til bilun neyðir hlutaendurkeyrslu klukkan tvö um nótt og einhver tvítalar tekjur. Komdu með áþreifanlega skrá: taktu saman verkin sem myndu spilla gögnum ef þau væru endurkeyrð frá bilunarpunkti og metdu sprengisvæði þess versta. Í fyrirtækja- og opinberri stærð, þar sem ein hljóð bilun getur ýtt röngum gögnum inn í greiðslur, skýrslur eða opinbera tölfræði, er vinnsla sem er ekki eins-áhrifa ekki bara óþægileg. Hún grefur undan úttektarhæfninni sem leyfir þér að endurvinna tímabil eftir reglubreytingu og samt rekja hverja tölu til uppsprettu, svo að fjármagna endurvinnuna til að gera endurkeyrslur öruggar er stýringaspurning, ekki bara snyrtimennska.

6. **Vitið þið hvað hver leiðsla kostar að keyra, hver á þá tölu og hve mikið af skýjareikningnum kemur af fullum skönnunum og vantandi skiptingum?** Kaflinn lítur á geymslusnið, skiptingu og reikniaflsútgjöld sem fyrsta flokks áhyggjuefni með eigendum og varar við því að stjórnlaus kostnaður megi yfirleitt rekja til fullra skannana, vantandi skiptinga og ótakmarkaðrar endurvinnslu. Sjónarmiðið á móti er að kostnaðarvinna finnst minna brýn en að afhenda eiginleika, svo henni er frestað þar til mánaðarreikningurinn kemur á óvart og fjármál spyrja spurninga sem verkfræði getur ekki svarað. Komdu með sönnunargögn: útgjöld á leiðslu og á fyrirspurn, hlutfall kostnaðar sem kemur af óskiptum skönnunum og fjölda smárra skráa sem ætti að þjappa. Fyrir stóra skipulagsheild sem keyrir milljarða færslna úr mörgum frumkerfum vex óeigandi skýjareikningur án þess að nokkurt eitt teymi finni ábyrgð, og í opinberu umhverfi þarf að rökstyðja opinber útgjöld línu fyrir línu, svo að eigna reikniaflskostnað nefndum eiganda með rakinn mælikvarða breytir ógegnsæjum kostnaði í stýrðan og afhjúpar oft sparnað sem er nógu stór til að fjármagna næstu vettvangsfjárfestingu.

## Sjónarhorn eftir geirum

**Sprotafyrirtæki.** Hraði slær arkitektúr. Tengdu inntöku við stýrðan tengil, byggðu fáeinar útgáfustýrðar umbreytingar og keyrðu þær á léttum samstilli sem endurreynir og endurfyllir sjálfur, frekar en að handsmíða cron-verk sem brotna hljóðlega yfir nótt. Haltu hverju líkani eins-áhrifa frá fyrsta framlagi og bættu við fáeinum ódýrum prófum fyrir núll lykla og línufjölda, svo slæm frumbreyting bili í CI í stað þess að birtast á mánudagsmælaborði stofnandans. Settu ekki upp straum eða sérsmíðaðan vettvang: knappasta auðlind þín er athygli verkfræðinga.

**Lítið fyrirtæki.** Án sérstaks gagnaverkfræðings skaltu kjósa að kaupa samþættan stafla frekar en að setja saman einn. Stýrð ELT þjónusta auk skýjavöruhúss gefur þér tengla, tímasetningu og geymslu án vettvangsteymis til að viðhalda þeim. Rammaðu valið sem gagnahreinlæti frekar en leiðsluverkefni: vittu hvaða frumkerfi fæða skýrslurnar þínar, geymdu hrágögn svo hægt sé að rekja og endurvinna ranga tölu og veldu verkfæri með fyrirsjáanlegan kostnað svo full töfluskönnun sprengi ekki mánaðarfjárhagsáætlunina.

**Stórfyrirtæki.** Vandinn er samræmi yfir mörg teymi og milljarða færslna úr mörgum frumkerfum. Staðlaðu ELT mynstrið, lagskipta hrátt-kjarna-markaðsgeymslu líkanið og fjögur gagnaheilsumerkin svo hópar hætti að finna upp brothættar leiðslur. Framfylgdu gagnaprófum og CI á hverju líkani, eignaðu reikniaflskostnað eigandateymum og keyrðu gagnaatvik gegnum sama bakvakta-, keyrsluhandbókar- og eftirmálsrýni án sakbendingar aga og þú notar fyrir þjónustur, svo hljóð bilun nái aldrei ótekin á mælaborð.

**Hið opinbera.** Innkaupareglur, gagnsæi og opinber ábyrgð móta leiðsluna. Lentu óbreytanlegum hráskrám fyrir úttektarhæfni, umbreyttu þeim í lagskiptum prófuðum stigum og haltu fullu ætterni svo úttektaraðili geti rakið hverja útgefna tölu aftur til upprunaskjala, oft lagakrafa. Eins-áhrifa vinnsla leyfir þér að endurvinna framtal eða skýrslutímabil örugglega þegar regla breytist og að kjósa opin snið og flytjanlegan umbreytingarkóða heldur þér frá bindingu við einn seljanda yfir margra ára samning.

## Dæmi

**Sprotafyrirtæki.** Tíu manna greiningarsprotafyrirtæki hafði safnað flækju cron-verka sem brotnuðu hljóðlega yfir nótt og tvítóku stundum línur þegar verkfræðingur endurkeyrði eitt í höndunum. Teymið fór yfir í stýrðan tengil fyrir inntöku, umbreytingarramma fyrir útgáfustýrð líkön og léttan samstilli sem endurreynir og endurfyllir sjálfur. Þau gerðu hvert líkan eins-áhrifa og bættu við fáeinum prófum fyrir núll lykla og línufjölda, svo slæm frumbreyting bilar nú í CI í stað þess að birtast á mánudagsmælaborði stofnandans.

**Stórfyrirtæki.** Alþjóðlegur smásali skipti hundruðum handskrifaðra útdráttarskripta út fyrir ELT stafla. Stýrðir tenglar lenda hráum frumgögnum, umbreytingarrammi byggir prófuð, útgáfustýrð líkön í vatnshúsi og samstillir stýrir ósjálfstæðum með endurtilraunum og endurfyllingum. Gagnapróf grípa skemarek úr frumkerfum áður en það nær mælaborðum. Skipt súlnageymsla skar fyrirspurnarkostnað verulega, á meðan ferskleiki batnaði úr daglegum í klukkutímalegan.

**Hið opinbera.** Skattayfirvald tekur inn framtöl og gögn þriðja aðila gegnum stýrða leiðslu sem lendir óbreytanlegum hráskrám fyrir úttektarhæfni, umbreytir þeim síðan í lagskiptum, prófuðum stigum. Eins-áhrifa vinnsla leyfir þeim að endurvinna framtalstímabil örugglega þegar regla breytist. Fullt ætterni leyfir úttektaraðilum að rekja hverja reiknaða tölu til upprunaskjala, lagakrafa vegna opinberrar ábyrgðar.

## Viðskiptarök: hvatar, ávöxtun fjárfestingar og heildarkostnaður

Ávöxtun agaðrar gagnaverkfræði kemur af áreiðanleika, hraða og kostnaðarstýringu. Áreiðanlegar leiðslur þýða að ákvarðanir og skýrslur hvíla á traustverðum gögnum, svo þú forðast dýra endurvinnu og orðsporsskaða rangra talna. Einingabundnar, prófaðar leiðslur leyfa teymum að afhenda nýjar gagnavörur hraðar, sem samnýtir verðmæti hverrar niðurstreymis greiningar- og vélnámsfjárfestingar. Að fínstilla geymslu og reikniafl lækkar beint skýjareikninginn, oft um mikið þegar skipting og fyrirspurnarmynstur eru löguð.

Upptökukostnaðurinn felur í sér vettvangsverkfæri, verkfræðitíma til að smíða prófaðar einingabundnar leiðslur og agann að líta á gögn sem hugbúnað. Vegðu það gegn kostnaði þess að taka ekki upp: brothætt sérsmíðuð verk sem aðeins höfundur þeirra skilur, hljóð gagnaspilling uppgötvuð af stjórnendum, þaninn skýjakostnaður af fullum töfluskönnunum og greinendur blokkaðir í bið eftir gögnum. Til stjórnenda skaltu ramma gagnaverkfræði sem grunninn sem gerir greiningu, viðskiptagreind og gervigreind traustverða og viðráðanlega í verði. Vanfjárfestu hér og þú setur þak á ávöxtun hvers gagnaverkefnis fyrir ofan.

## Andmynstur og gildrur

- Leiðslur smíðaðar sem einnota skriftur án útgáfustýringar, prófa eða rýni.
- Verk sem eru ekki eins-áhrifa og tvítaka eða spilla gögnum þegar þau eru endurkeyrð eftir bilun.
- Að taka upp straum vegna álits þegar lotur myndu mæta töfarkröfunni.
- Að demba hráum töflum á greinendur og kalla það sjálfsafgreiðslu.
- Engin vöktun, svo bilanir uppgötvast af niðurstreymisnotendum.
- Að hunsa skiptingu og skráastærð þar til skýjareikningurinn springur.
- Að tengja saman inntöku, umbreytingu og þjónustu svo ekkert geti breyst örugglega.
- Að eyða hrágögnum, sem gerir ómögulegt að endurvinna þegar rökfræði breytist.

## Þroskalíkan

1. Upphaf: Ad hoc skriftur og handvirkar keyrslur, án prófa eða vöktunar. Bilanir uppgötvast af niðurstreymisnotendum, verk er ekki hægt að endurkeyra örugglega og skýjakostnaður er óstýrður og óeignaður.
2. Þróun: Sum teymi hafa tekið upp samstilli og sett grunnumbreytingar í útgáfustýringu, en vinnubrögð eru ósamræmd um skipulagsheildina. Stöku próf eru til, eins-áhrifa eiginleiki er brotakenndur og bilaðar leiðslur þýða enn viðbragðsdrifna slökkvivinnu.
3. Stöðlun: ELT með lagskiptu hrátt-kjarna-markaðsgeymslu líkani, prófað og útgáfustýrt, er skjalfesti staðallinn sem beitt er yfir teymi. Samstilltar ósjálfstæði með endurtilraunum og endurfyllingum, gagnapróf í CI og sameiginlegar venjur um stjörnuskemalíkön og skiptingu eru framfylgd um skipulagsheildina frekar en látnar hverjum hópi eftir.
4. Stjórnun: Vettvangurinn er mældur og stýrður. Ferskleiki, magn, skema og dreifing eru vöktuð með viðvörunum beint til eigandateyma, og leiðsluþjónustusamningar, meðaltími til greiningar, gagnagæðaárangurshlutföll og reikniaflskostnaður á leiðslu og á fyrirspurn eru rakin gegn grunnlínum. Afturköllunar- og drápsþröskuldum er framfylgt á sönnunargögnum og kostnaður og áreiðanleiki hafa nefnda eigendur sem eru látnir svara fyrir markmið.
5. Samhæfing: Leiðslur eru meðhöndlaðar fullkomlega sem hugbúnaður með CI/CD, gagnasamningum og sjálfvirkri fráviksgreiningu sem grípur rek áður en notendur gera það. Lotu- og straumrökfræði er sameinuð þar sem töf borgar sig raunverulega, vettvangurinn er stöðugt bættur og sjálfsafgreiðsla og afkastageta, geymsluþrep og kostnaður eru endurjöfnuð aðlögunarhæft eftir því sem vinnuálag breytist svo nýjar gagnavörur afhendist hratt á stöðugum grunni.

## Hugmyndir til umræðu

- Hvar í staflanum ykkar vinnur „rauntími“ sér raunverulega inn kostnað sinn og hvar er hann óskhyggja?
- Hverjar leiðslur gætu ekki verið endurkeyrðar örugglega í dag og hvað þyrfti til að laga það?
- Hve mikið af skýjagagnareikningnum ykkar kemur af fullum skönnunum og vantandi skiptingum?
- Nota greinendur ykkar líkanaðar markaðsgeymslur eða hráar töflur og hvað kostar það þá?
- Hver er meðaltími ykkar til að greina gagnaatvik og hver finnur það fyrst?
- Myndi sameining lotu- og straumrökfræði draga úr viðhaldsbyrði ykkar eða bæta við áhættu?

## Helstu atriði

- Líttu á leiðslur sem hugbúnað: útgáfustýringu, próf, rýni, CI/CD og vöktun.
- Kjóstu ELT með lagskiptum, prófuðum líkönum. Geymdu hrágögn til endurvinnslu.
- Veldu lotur sem sjálfgefið og straum aðeins þar sem töf borgar sig raunverulega.
- Gerðu umbreytingar eins-áhrifa svo endurkeyrslur séu öruggar.
- Líkanaðu gögn fyrir notendur með stjörnuskemum eða yfirveguðum breiðum töflum.
- Vaktaðu ferskleika, magn, skema og dreifingu og líttu á gagnaatvik eins og rof.
- Fínstilltu geymslusnið, skiptingu og reikniaflskostnað sem fyrsta flokks áhyggjuefni.

## Heimildir og frekari lestur

- Joe Reis and Matt Housley, "Fundamentals of Data Engineering."
- Ralph Kimball and Margy Ross, "The Data Warehouse Toolkit."
- Martin Kleppmann, "Designing Data-Intensive Applications."
- Bill Inmon, "Building the Data Warehouse."
- James Densmore, "Data Pipelines Pocket Reference."
- Nathan Marz and James Warren, "Big Data" (Lambda architecture).
- Barr Moses and colleagues, "Data Quality Fundamentals" (data observability).
