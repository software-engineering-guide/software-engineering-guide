# 2.6 Útgáfustýring og frumkóðastjórnun

## Yfirlit og tilgangur

Líttu á [útgáfustýringu](https://en.wikipedia.org/wiki/Version_control) sem skráningarkerfi kóðagrunnsins þíns. Hún fangar sérhverja breytingu, þar á meðal hver gerði hana, hvenær og hvers vegna, og lætur marga vinna að sama hugbúnaði án þess að skrifa yfir hver annan. Fyrir stóra skipulagsheild er hún miklu meira en öryggisafrit. Hún er grunnurinn sem samvinna, [samfelld samþætting](https://en.wikipedia.org/wiki/Continuous_integration) (CI), úttekt og útgáfustjórnun hvíla á. Valin sem þú tekur um greinar, hugbúnaðarsafnsuppbyggingu og commit-aga móta hve hratt teymið þitt getur hreyft sig og hve örugglega.

Fyrir stór teymi er frumkóðastjórnun í raun samhæfingarvandi í stórum stíl. Þegar hundruð verkfræðinga ýta breytingum inn í sameiginlegan kóða þurfa þeir stefnu sem heldur sameiningum litlum, heldur aðallínunni útgáfuhæfri og heldur sögunni læsilegri. Teymi sem samþættir stöðugt flæðir mjúklega. Teymi sem lætur greinar reka sundur vikum saman hrasar frá einni samþættingarkreppu til annarrar. Uppbygging hugbúnaðarsafna þinna, eitt stórt eða mörg, mótar líka hvernig teymi deila kóða og samhæfa sig.

Fyrirtækja- og opinbert umhverfi bæta við nokkrum kröfum til viðbótar: rekjanleika, aðgangsstýringu og varðveislu. Breyting kann að þurfa að tengjast samþykktu vinnuatriði fyrir úttekt. Leyndarmál mega aldrei komast í sögu. Aðgangur að hugbúnaðarsöfnum verður að virða öryggismörk. Hér verða útgáfustýringarvenjur þínar hluti af stýriramma skipulagsheildarinnar og mistök eins og lekið leyndarmál eða óúttektarhæf saga geta haft alvarlegar afleiðingar.

## Meginreglur

- Samþættu litlar breytingar oft. Löng frávik eru rót samrunasársauka.
- Haltu aðallínunni alltaf útgáfuhæfri.
- Saga er skjölun. Skrifaðu commit fyrir framtíðarlesandann sem þarf að skilja hvers vegna.
- Skuldbindu aldrei leyndarmál. Líttu á hvert leyndarmál sem kemst í sögu sem í hættu.
- Sjálfvirknivæddu framfylgd hreinlætis (hooks, CI-athuganir) frekar en að treysta á aga einan.
- Veldu hugbúnaðarsafnsuppbyggingu (eitt á móti mörgum) eftir því hvernig teymi deila kóða og samhæfa sig í raun, ekki tísku.
- Tengdu breytingar við rök þeirra (vinnuatriði, miða eða ákvarðanir) fyrir rekjanleika.

## Ráðleggingar

### Kjóstu stofnþróun (trunk-based) með skammlífum greinum

Hallaðu þér að [stofnþróun](https://en.wikipedia.org/wiki/Trunk-based_development): samþættu oft í sameiginlega aðallínu, með skammlífum eiginleikagreinum mældum í klukkustundum eða dögum, ekki vikum. Stuttar greinar halda sameiningum litlum og samþættingu samfelldri, og sú venja er sterklega tengd mikilli afhendingarframmistöðu. Þegar vinna er ekki fullkláruð skaltu ekki leggja hana á langlífa grein. Notaðu [eiginleikarofa](https://en.wikipedia.org/wiki/Feature_toggle), keyrslurofa sem fela ókláraða vinnu, svo þú getir sameinað hana örugglega í staðinn. Taktu frá langlífar útgáfugreinar fyrir raunverulegan fjölútgáfustuðning og farðu inn í það vitandi viðhaldskostnaðinn sem þær bera.

### Veldu greinalíkan sem passar útgáfutakti

Láttu [greinalíkan](https://en.wikipedia.org/wiki/Branching_(version_control)) þitt samsvara því hvernig þú gefur út í raun. Ef þú setur upp stöðugt þjónar stofnþróun með lágmarks greinum þér vel. Ef þú afhendir útgefnar útgáfur til viðskiptavina, eða styður nokkrar lifandi útgáfur í einu, gætirðu þurft útgáfugreinar og afturábak-yfirfærslu. Forðastu þung líkön með mörgum langlífum greinum nema útgáfulíkanið þitt krefjist þeirra í alvöru, því þau margfalda sameiningar- og viðhaldsyfirbyggingu.

### Ákveddu einsafn á móti fjölsafni af ásetningi

Náðu í [einsafn](https://en.wikipedia.org/wiki/Monorepo), eitt hugbúnaðarsafn sem heldur mörgum verkefnum, þegar teymi deila kóða mikið, þurfa frumeindabreytingar yfir verkefni og vilja sameinuð verkfæri og sýnileika. Í staðinn tekurðu á þig þörfina fyrir stækkuð smíðaverkfæri og aðgangsstýringar. Náðu í fjölsöfn, aðskilin hugbúnaðarsöfn fyrir hvert verkefni eða þjónustu, þegar teymi og þjónustur eru raunverulega sjálfstæð, vilja einangraðan aðgang og útgáfulotur og þurfa ekki frumeindabreytingar yfir söfn. Í staðinn tekurðu á þig kostnað við að samhæfa breytingar sem spanna söfn. Hvort tveggja virkar í stórum stíl. Það er rangt val fyrir tengslamynstrið þitt sem skapar stöðugan núning.

### Framfylgdu commit-hreinlæti og hefðbundnum commit

Biddu um commit-skilaboð sem útskýra hvers vegna breyting var gerð, ekki bara hvað. Taktu upp venju eins og hefðbundin commit (conventional commits) svo skilaboð séu skipulögð og vélþáttanleg, sem leyfir þér að sjálfvirknivæða breytingaskrár og útgáfustýringu. Haltu commit frumeindalegum, ein rökræn breyting hvert, svo sagan haldist tvískiptanleg og auðveld að afturkalla. Láttu hooks og CI-athuganir framfylgja skilaboðasniði og grunnhreinlæti í stað þess að treysta á minni.

### Haltu stórum tvíundarskrám og mynduðum kóða utan venjulegrar sögu

Skuldbindu ekki stórar tvíundareignir beint í aðalsöguna, því þær blása upp hvert afrit að eilífu. Notaðu stórskráageymslu eða afurðasafn í staðinn. Sem regla skaltu forðast að skuldbinda myndaðan kóða líka. Myndaðu hann í smíðinni. Þegar þú verður raunverulega að skuldbinda mynduð afurð skaltu einangra hana og merkja hana skýrt svo hún mengi ekki rýni og mismun.

### Komdu í veg fyrir að leyndarmál komist nokkurn tíma í hugbúnaðarsafnið

Settu sjálfvirka leyndarmálaskönnun í pre-commit hooks og CI svo skilríki séu hindruð áður en þau lenda. Gefðu verkfræðingum almennilegt leyndarmálastjórnunarkerfi, svo þeir þurfi aldrei að harðkóða skilríki í fyrsta lagi. Og líttu á hvert leyndarmál sem kemst í sögu sem í hættu: snúðu því strax. Þegar leyndarmáli hefur verið ýtt og það afritað er erfitt og óáreiðanlegt að fjarlægja það úr sögu.

### Komdu á aðgangsstýringu og rekjanleika

Settu upp aðgang að hugbúnaðarsöfnum til að virða öryggismörk og [minnstu réttindi](https://en.wikipedia.org/wiki/Principle_of_least_privilege). Tengdu commit eða sameiningarbeiðnir við vinnuatriði, svo hver breyting rekjist aftur til raka sinna, sem hjálpar bæði daglegu verkfræðisamhengi og úttekt. Verndaðu lykilgreinar þínar með skyldum athugunum og rýni, svo ekkert sameinist án þess að standast hliðin sem þú samþykktir.

## Málamiðlanir: kostir og gallar

| Val | Kostir | Gallar |
|---|---|---|
| Stofnþróun | Samfelld samþætting, litlar sameiningar, mikið flæði | Krefst eiginleikarofa og aga, minni einangrun |
| Langlífar eiginleikagreinar | Sterk einangrun vinnu í vinnslu | Sársaukafullar sameiningar, seinkuð samþætting, rek |
| Einsafn | Frumeindabreytingar yfir verkefni, sameiginleg verkfæri, sýnileiki | Þarfnast stækkaðra smíðaverkfæra, gróf aðgangsstýring sjálfgefið |
| Fjölsafn | Sjálfstæðar útgáfur, einangraður aðgangur, einföld verkfæri á safn | Erfiðar breytingar yfir söfn, útgáfusamhæfingaryfirbygging |
| Hefðbundin commit | Sjálfvirkar breytingaskrár og útgáfustýring, samræmd saga | Venja fyrirfram, framfylgd nauðsynleg |

Stóra málamiðlunin hér er samþættingartíðni gegn einangrun. Langlífar greinar finnast öruggari því vinna þín situr á eigin spýtur, en sú einangrun er einmitt það sem veldur dýrum sameiningum og samþættingaróvæntingum síðar. Stofnþróun gefur upp þá einangrunartilfinningu í skiptum fyrir samfellda, ódýra samþættingu og biður þig að koma með eiginleikarofa og aga. Einsafns/fjölsafns ákvörðunin skiptir auðveldleika yfir verkefni fyrir sjálfstæði teyma. Veldu það sem passar því hve þétt kóðinn þinn er raunverulega tengdur.

## Spurningar til að ræða með teyminu

1. **Hvaða athuganir verða að standast áður en nokkuð sameinast í varða aðallínu þína og er sú aðallína sannarlega alltaf útgáfuhæf?** Þessi kafli lítur á útgáfuhæfa aðallínu sem kjarnareglu og kallar óvarða aðallínu, þar sem brotinn eða órýndur kóði nær til greinarinnar sem allir reiða sig á, andmynstur. Í stóru teymi hindrar rauð aðallína alla í einu, svo hliðið sem þú krefst er sameiginlegur öryggiseiginleiki, ekki persónulegur. Komdu með sönnunargögnin: hvað greinavörn þín framfylgir í raun í dag og hve oft aðallínan er nú biluð. Ákveddu skyldu settið, standast próf, öryggisskannanir og rýni, og gerðu aðallínuna útgáfuhæfa með stefnu en ekki von. Það hlið er það sem lætur marga samþætta stöðugt án ótta.

2. **Er það þess virði að taka upp hefðbundin commit fyrir venjuyfirbygginguna, miðað við hvað þau sjálfvirknivæða?** Kaflinn mælir með skipulögðum, vélþáttanlegum commit-skilaboðum einmitt því þau leyfa þér að sjálfvirknivæða breytingaskrár og útgáfustýringu, og hann biður um frumeindaleg commit svo saga haldist tvískiptanleg og afturkræf. Málamiðlunin er raunveruleg: þú borgar venju fyrirfram og þarft framfylgd í skiptum fyrir mynduð útgáfuskýrsla og áreiðanlega sögu. Komdu með merkið um hvað þú gerir í höndunum í dag, svo sem að skrifa breytingaskrár handvirkt eða leita að því hvaða commit kynnti afturför. Ef þú gefur oft út eða viðheldur mörgum útgáfum borgar sjálfvirknin sig venjulega sjálf. Ef þú klippir sjaldan útgáfur gæti léttari venja nægt. Láttu hooks og CI framfylgja sniðinu svo það reiði sig ekki á minni.

3. **Hefurðu samþykkt rekstrarkostnaðinn sem hugbúnaðarsafnsuppbygging þín krefst, hvort sem það eru einsafnsverkfæri eða samhæfing milli safna?** Þessi kafli segir að bæði einsafn og fjölsafn virki í stórum stíl og að rangt val fyrir tengslamynstrið þitt sé það sem skapar stöðugan núning. Einsafn þarf stækkuð smíðaverkfæri og fíngerðari aðgangsstýringu, á meðan fjölsöfn gera hverja breytingu sem spannar söfn að samhæfingarverkefni með útgáfuskekkjuáhættu. Komdu með áþreifanlega merkið: hve oft breytingar þínar fara yfir verkefnamörk og hvort smíða- og aðgangsverkfæri þín geti borið uppbygginguna sem þú hefur. Ef frumeindabreytingar yfir verkefni eru algengar skaltu fjárfesta í einsafnsverkfærum. Ef teymi og þjónustur eru raunverulega sjálfstæð skaltu samþykkja samhæfingarkostnað milli safna af ásetningi. Atriðið er að láta uppbyggingu samsvara því hve þétt kóðinn þinn er raunverulega tengdur og fjármagna svo verkfærin sem sú uppbygging krefst.

4. **Ef lifandi skilríki yrðu skuldbundin í upptekið hugbúnaðarsafn núna, hve fljótt myndir þú greina það og er snúningur í raun sjálfvirkur frekar en von?** Þessi kafli lítur á hvert leyndarmál sem kemst í sögu sem í hættu og varar við að það sé erfitt og óáreiðanlegt að fjarlægja það síðar, svo forvarnir og hraður snúningur eru einu raunverulegu varnirnar. Fyrir stórt teymi safnast útsetningin upp: leyndarmáli ýtt í sameiginlegt safn er afritað á tugi véla og speglað í CI-skyndiminni innan mínútna, svo hægt mannlegt viðbragð tryggir innbrot. Sjónarmiðið á móti er núningur: ágeng pre-commit skönnun og þvingaður snúningur hægir á fólki og framleiðir rangar jákvæðar niðurstöður, svo þú verður að stilla stýringarnar frekar en slökkva á þeim. Komdu með sönnunargögnin: hvort leyndarmálaskönnun keyrir bæði í pre-commit hooks og CI, meðaltíma þinn til að greina og snúa þekktum leka og hvort verkfræðingar hafi yfirleitt leyndarmálastjórnunarkerfi sem fjarlægir freistinguna til að harðkóða. Í fyrirtækja- og opinberu umhverfi skaltu tengja þetta við atvikaferli þitt og varðveislureglur, því lekið skilríki í úttektarhæfri sögu er bæði öryggisatvik og regluvörsluatvik, og eftirlitsaðilinn mun spyrja hver vissi og hve fljótt þeir brugðust við.

5. **Eru greinar þínar sannarlega skammlífar og þar sem þær eru það ekki, hvers vegna er ókláruð vinna lögð á grein í stað þess að vera falin á bak við eiginleikarofa?** Kaflinn hallast sterkt að stofnþróun því löng frávik eru rót samrunasársauka, og hann býður eiginleikarofa sem búnaðinn sem leyfir þér að sameina ófullkomna vinnu örugglega í stað þess að einangra hana vikum saman. Í stóru teymi er þetta samhæfingareiginleiki, ekki persónulegt kjör: sérhver grein sem lifir vikum saman verður einkaklofningur raunveruleikans sem einhver verður að sætta að lokum, og kostnaður þeirrar sáttar vex með mannfjölda. Sjónarmiðið á móti er að eiginleikarofar bera eigin kostnað, þar á meðal keyrsluflækju, prófun samsetninga og úrelta rofa sem verður að leggja niður. Komdu með gögnin: raunverulega dreifingu greinalífs, hve oft samþætting framleiðir árekstra eða óvæntar uppákomur og hve margar langlífar greinar eru til núna og hvers vegna. Fyrir stóra eða eftirlitsskylda skipulagsheild skaltu bæta útgáfumyndinni við, því raunverulegur fjölútgáfustuðningur kann að réttlæta langlífar útgáfugreinar með agaðri afturábak-yfirfærslu, og það er önnur ákvörðun en að leggja daglega eiginleikavinnu utan aðallínunnar.

6. **Er hægt að rekja sérhverja breytingu í sögu þinni til höfundar og raka innan réttra öryggismarka og myndi það standast úttekt?** Þessi kafli lítur á aðgangsstýringu, minnstu réttindi og að tengja breytingar við vinnuatriði sem hluta af stýriramma skipulagsheildarinnar, ekki valkvæða fágun. Fyrir stórt teymi er rekjanleiki það sem breytir ógagnsærri straumi commit í eitthvað sem þú getur rökrætt um í atviki eða regluvörslurýni, og aðgangsmörk eru það sem stöðva einn í hættu kominn reikning frá því að ná til kóða sem hann ætti aldrei að snerta. Sjónarmiðið á móti er hraði þróunaraðila: skyldubundnir vinnuatriðatenglar, fíngerð réttindi og skyldar rýnir bæta við helgisiði sem lítið, hraðfara teymi gæti skynsamlega sleppt. Komdu með sönnunargögnin: hvort varðar greinar krefjast athugana og rýni sem þú fullyrðir, hvort commit vísa í raun til samþykktra vinnuatriða og hvernig aðgangur samsvarar raunverulegum öryggismörkum þínum í dag. Í fyrirtækja- og opinberu samhengi skaltu tengja þetta við flokkun, varðveislu og úttektarskyldur, því óúttektarhæf saga eða of víð aðgangsveiting verður að niðurstöðu sem getur stöðvað áætlun eða fellt vottun.

## Sjónarhorn eftir geirum

**Sprotafyrirtæki.** Hraði og lífsafkoma vinna. Notaðu eitt hugbúnaðarsafn, vinndu með stofnþróun, sameinaðu skammlífar greinar nokkrum sinnum á dag og feldu ókláraða vinnu á bak við einfalda eiginleikarofa frekar en langar greinar. Kveiktu á leyndarmálaskönnun frá fyrsta commit, því lekinn lykill í opinberu safni getur sökkt fyrirtæki án öryggisteymis til að ná tökum á því. Slepptu íburðarmiklum greinalíkönum og þungu ferli. Varin aðalgrein og merkingarbær commit-skilaboð eru nægur agi til að hreyfa sig hratt.

**Lítið fyrirtæki.** Án sérstaks vettvangs- eða DevOps-sérfræðings og með þröngt fjárhagsáætlun skaltu kaupa stýrð sjálfgefin gildi frekar en að smíða þau. Hýstur Git-veitandi gefur þér greinavörn, skyldar rýnir og leyndarmálaskönnun úr kassanum, svo hallaðu þér að þeim í stað þess að hýsa sjálfur netþjón sem þú getur ekki viðhaldið. Rammaðu ákvörðunina sem gagnahreinlæti: veistu hvaða hugbúnaðarsöfn halda viðkvæmri stillingu, geymdu skilríki í leyndarmálastjóra veitandans og láttu vettvanginn framfylgja fáu reglunum sem þú þarft í raun.

**Stórfyrirtæki.** Erfiða vandamálið er samræmi milli margra teyma. Staðlaðu greinavörn, commit-venjur og leyndarmálaskönnun sem stefnu um alla skipulagsheildina svo hópar hætti að finna þau upp aftur, og taktu einsafns-á-móti-fjölsafns valið af ásetningi fyrir hvert tengslamynstur, fjármagnaðu stækkuð smíðaverkfæri eða samhæfingu milli safna sem það krefst. Beindu breytingum til réttra rýna með kóðaeignarreglum, tengdu commit við vinnuatriði fyrir rekjanleika og líttu á útgáfustýringarhreinlæti sem stýrða stýringu með eigendum og mælikvörðum frekar en einstaklingsvenju.

**Hið opinbera.** Innkaupareglur, gagnsæi og almenn ábyrgð móta alla uppsetninguna. Krefstu þess að sérhvert commit vísi til samþykkts vinnuatriðis, stýrðu aðgangi eftir flokkunarmörkum og gerðu leyndarmálaskönnun og tafarlausan snúning skyldu undir skjalfestu atvikaferli. Styddu margar uppsettar útgáfur með langlífum útgáfugreinum og agaðri afturábak-yfirfærslu þar sem staðir geta ekki allir uppfært í einu og haltu sögunni úttektarhæfri og varðveittri svo vottunar-, upplýsingalaga- og eftirlitsbeiðnum megi svara án þess að hlaupa um.

## Dæmi

**Sprotafyrirtæki.** Þriggja manna sprotafyrirtæki vinnur með stofnþróun bæði af vana og nauðsyn, sameinar skammlífar greinar í main nokkrum sinnum á dag og felur hálfkláraða eiginleika á bak við einfalda rofa. Þeir kveikja á leyndarmálaskönnun í CI frá fyrsta commit, því lekinn API-lykill í opinberu safni gæti sökkt fyrirtæki sem hefur ekkert öryggisteymi til að ná tökum á afleiðingunum. Eitt hugbúnaðarsafn, varin aðalgrein og merkingarbær commit-skilaboð gefa þeim nægan aga til að hreyfa sig hratt án þess að hrasa um eigin sögu.

**Stórfyrirtæki.** Stórt tæknifyrirtæki rekur einsafn með hundruðum þjónusta og sameiginlegra bókasafna. Stækkuð smíðaverkfæri og kóðaeignarreglur beina hverri breytingu til réttra rýna. Eitt commit getur frumeindalega uppfært sameiginlegt bókasafn og alla neytendur í einu og sniðgengið útgáfuskekkjuvandamálin sem hrjá dreifð hugbúnaðarsöfn. Stofnþróun með eiginleikarofum heldur aðallínunni útgáfuhæfri og leyndarmálaskönnun hindrar skilríki við commit-tíma yfir allt hugbúnaðarsafnið.

**Hið opinbera.** Landsbundinn varnarverktaki heldur fast við strangan rekjanleika. Sérhvert commit verður að vísa til samþykkts vinnuatriðis. Greinavörn krefst staðinna öryggisskannana og sjálfstæðrar rýni og aðgangur er stýrður náið eftir flokkunarmörkum. Leyndarmálaskönnun er skylda og sérhvert afhjúpað skilríki kallar fram tafarlausan snúning undir atvikaferli. Langlífar útgáfugreinar styðja margar uppsettar útgáfur yfir staði sem geta ekki allir uppfært í einu, með agaðri afturábak-yfirfærslu öryggisleiðréttinga.

## Viðskiptarök: hvatar, ávöxtun fjárfestingar og heildarkostnaður

Traust frumkóðastjórnun er nánast ókeypis í upptöku og dýr að vera án. Stofnþróun og samfelld samþætting eru meðal vinnubragðanna sem eru sterklegast tengd mikilli hugbúnaðarafhendingarframmistöðu, sem aftur fylgir betri skipulagsárangri. Hrein, rekjanleg saga styttir tímann sem það tekur að greina atvik og fullnægja úttektum, og agaðar greinar spara þér endurtekinn, ófjárhagsáætlaðan kostnað samþættingarkreppna og sameiningamaraþona.

Stærsta ójafna áhættan eru leyndarmál í útgáfustýringu. Eitt lekið skilríki getur valdið innbroti sem kostar langt umfram nokkra verkfærafjárfestingu, og saga lætur slíka leka loða við. Að koma í veg fyrir þá er ódýrt. Að hreinsa upp eftir þá er það ekki. Léleg uppbyggingarval birtast sem langvarandi núningur: sérhver breyting milli safna verður samhæfingarverkefni, eða sérhver einsafnssmíði verður flöskuháls. Til að færa rök við forystu skaltu tengja greinastefnu þína við afhendingarmælikvarða og atvikagreiningartíma og ramma leyndarmálaskönnun og aðgangsstýringu sem ódýrar stýringar gegn dýrri innbrots- og úttektaráhættu.

## Andmynstur og gildrur

- **Langlífar sundurleitar greinar:** vikur af einangraðri vinnu sem sameinast í sársaukafullum, áhættusömum samþættingarviðburðum.
- **Leyndarmál í sögu:** harðkóðuð skilríki sem lifa í afritum að eilífu og krefjast snúnings þegar þau eru afhjúpuð.
- **Stórar tvíundarskrár skuldbundnar í aðalsögu:** blása varanlega upp hvert afrit og hægja á öllum aðgerðum.
- **Merkingarlaus commit-skilaboð:** „fix“, „wip“, „changes“ sem eyðileggja gildi sögu sem skjölunar.
- **Myndaður kóði skuldbundinn eins og handskrifaður:** hávaðasamur mismunur, sameiningarárekstrar og ruglingur um uppsprettu sannleikans.
- **Röng hugbúnaðarsafnsuppbygging fyrir tengslin:** fjölsöfn fyrir þétt tengdan kóða, eða einsöfn án stækkaðra verkfæra.
- **Óvarin aðallína:** engar skyldar athuganir, svo brotinn eða órýndur kóði nær til greinarinnar sem allir reiða sig á.

## Þroskalíkan

- **Stig 1, Upphaf:** Ad hoc og viðbragðsdrifið. Greining er spunnin, greinar lifa vikum saman, commit-skilaboð segja „fix“ eða „wip“, engin leyndarmálaskönnun er til staðar og samþætting hrasar frá einni sameiningarkreppu til annarrar.
- **Stig 2, Þróun:** Grunnvinnubrögð birtast en eru ólík eftir teymum. Greinalíkan og skilaboðavenjur eru til sums staðar, en greinar lifa enn of lengi, framfylgd er að hluta, leyndarmálaskönnun er götótt og safnauppbygging var erfð en ekki valin.
- **Stig 3, Stöðlun:** Vinnubrögð eru skjalfest og framfylgt um alla skipulagsheildina: stofnþróun með stuttum greinum, varin og alltaf útgáfuhæf aðallína, framfylgdar commit-venjur, leyndarmálaskönnun bæði í hooks og CI, minnstu réttindi og yfirveguð einsafns- eða fjölsafnsval.
- **Stig 4, Stjórnun:** Frumkóðavenjur eru mældar og stýrðar með gögnum. Þú rekur greinalíftíma, samþættingartíðni, bilanahlutfall aðallínu, meðaltíma til að greina og snúa lekið leyndarmál og breyting-til-vinnuatriðis rekjanleika gegn samþykktum grunnlínum og bregst við þegar tölurnar reka í stað þess að bíða næsta atviks.
- **Stig 5, Samhæfing:** Vinnubrögð eru stöðugt bætt og samþætt um skipulagsheildina. Greinar, safnauppbygging og verkfæri aðlagast eftir því sem teymi og kóðatengsl breytast, sjálfvirkni framfylgir hreinlæti frá enda til enda og útgáfustýringargögn næra afhendingar-, öryggis- og áhættuákvarðanir um skipulagsheildina.

## Hugmyndir til umræðu

- Er greinalífstími teymisins þíns í raun stuttur og ef ekki, hvað kemur í veg fyrir samfellda samþættingu?
- Passar einsafns- eða fjölsafnsval þitt við hve tengdur kóðinn þinn er í raun?
- Hvernig meðhöndlarðu stórar tvíundarskrár og mynduð afurð í dag og hvað kostar það þig?
- Hvað myndi gerast ef lifandi skilríki væru skuldbundin núna og hve fljótt myndirðu greina og snúa þeim?
- Hve mikill commit-skilaboða- og rekjanleikaagi er þess virði að framfylgja í þínu samhengi?
- Hvernig breyta eiginleikarofar greinastefnu þinni og hvaða nýju áhættu kynna þeir?

## Helstu atriði

- Samþættu oft með skammlífum greinum. Löng frávik valda sársaukanum sem þau virðast forðast.
- Haltu aðallínunni útgáfuhæfri og varinni með skyldum athugunum.
- Láttu leyndarmál aldrei komast í sögu. Skannaðu sjálfvirkt og snúðu strax ef þau gera það.
- Veldu einsafn eða fjölsafn eftir raunverulegum tengslum og samhæfingarþörfum.
- Líttu á commit-sögu sem skjölun, með merkingarbærum, hefðbundnum, frumeindalegum commit.

## Heimildir og frekari lestur

- Nicole Forsgren, Jez Humble, Gene Kim, *Accelerate: The Science of Lean Software and DevOps*
- Jez Humble and David Farley, *Continuous Delivery*
- Scott Chacon and Ben Straub, *Pro Git*
- Paul Hammant and others, writings on trunk-based development
- Conventional Commits specification (as a reference standard)
- Martin Fowler, articles on branching patterns and continuous integration
