# 10.12 Opinn hugbúnaður á móti lokuðum

## Yfirlit og tilgangur

Nær sérhvert nútímakerfi er blanda af hugbúnaði sem þú skrifaðir, hugbúnaði sem þú keyptir og hugbúnaði sem þú tókst ókeypis. Tveimur af þessum þremur fylgir grundvallarval: er hugbúnaðurinn **opinn** eða **lokaður**? **[Opinn hugbúnaður](https://en.wikipedia.org/wiki/Open-source_software) (OSS)** er dreift undir leyfi sem veitir öllum rétt til að nota, rannsaka, breyta og endurdreifa frumkóðanum, mannlæsilegu leiðbeiningunum sem skilgreina forritið. **Lokaður hugbúnaður**, einnig kallaður **[séreignarhugbúnaður](https://en.wikipedia.org/wiki/Proprietary_software)**, er dreift sem fullbúinni vöru þar sem seljandinn heldur frumkóðanum leyndum. Þú færð rétt til að keyra hann undir leyfi, en ekki til að skoða eða breyta því hvernig hann virkar. Millistig, **[frumkóðaaðgengilegur hugbúnaður](https://en.wikipedia.org/wiki/Source-available_software)**, birtir frumkóðann til lestrar en takmarkar notkun, breytingar eða endurdreifingu. Hann er *sýnilegur* en ekki *opinn* samkvæmt viðurkenndu skilgreiningunni.

Tvær skýringar skipta máli áður en þú berð þau saman. Í fyrsta lagi er „frjáls“ tvíræð. Samfélagið aðgreinir **frjálst-sem-í-frelsi** (frelsið til að breyta og deila, stundum skrifað „libre“) frá **frjálst-sem-í-verði** (kostar ekkert, „gratis“). Opinn hugbúnaður snýst um frelsi, ekki endilega verð. Í öðru lagi skiptast opin hugbúnaðarleyfi í tvær fjölskyldur. **[Frjálsleg leyfi](https://en.wikipedia.org/wiki/Permissive_software_license)** (svo sem [MIT](https://en.wikipedia.org/wiki/MIT_License), BSD og Apache 2.0) leyfa þér nánast hvað sem er, þar á meðal að fella kóðann inn í lokaða vöru. **[Copyleft](https://en.wikipedia.org/wiki/Copyleft) leyfi** (svo sem [GNU General Public Licence](https://en.wikipedia.org/wiki/GNU_General_Public_License), GPL) krefjast þess að afleidd verk sem þú dreifir séu einnig gefin út undir sömu opnu skilmálum, gagnkvæmnireglu sem gagnrýnendur kalla stundum „veirukennda“ og stuðningsmenn „deildu-eins“.

Þessi kafli skoðar valið frá tveimur hliðum. Sem **neytandi** ákveður þú hvort taka eigi upp opinn eða séreignaríhlut. Sem **framleiðandi** ákveður þú hvort gera eigi hugbúnað sem þú smíðaðir opinn. Fyrir stór fyrirtæki og sérstaklega hið opinbera bera báðar ákvarðanir þunga langt umfram leyfisskrána. Þær snerta innkaup (kafli 10.3), stafrænt fullveldi (kafli 10.11), öryggi aðfangakeðju (kafli 4.2), samvirkni (kafli 3.8) og útreikning smíða-eða-kaupa (kafli 6.1).

## Meginreglur

- **Leyfið, ekki verðið, skilgreinir „opið“.** Lestu leyfið. Ókeypis og opinn hugbúnaður eru ólíkar fullyrðingar.
- **Hvorugt líkanið er í eðli sínu öruggara.** Bæði geta verið framúrskarandi eða vanræksluleg. Venjurnar í kringum kóðann skipta meira máli en opnun hans.
- **Opnun er lyftistöng til að draga úr ósjálfstæði.** Aðgangur að frumkóða er endanleg vernd gegn [innilokun seljanda](https://en.wikipedia.org/wiki/Vendor_lock-in).
- **Þú berð alltaf rekstrarbyrðina.** Ókeypis að eignast er aldrei ókeypis að reka. [Heildareignarkostnaður](https://en.wikipedia.org/wiki/Total_cost_of_ownership) segir raunverulegu söguna.
- **Aðgreinendur haldast lokaðir. Hversdagsvara má opna.** Opnaðu það sem aðgreinir þig ekki. Gættu þess sem gerir það.
- **Copyleft hefur afleiðingar.** Skildu gagnkvæmniskyldur áður en þú fellir copyleft-kóða inn í vöru sem þú dreifir.
- **Lifandi samfélag er eign. Yfirgefin geymsla er skuld.** Dæmdu verkefnið, ekki bara leyfið.

## Ráðleggingar

### Metdu íhlut út frá verkefninu, ekki bara leyfinu

Áður en þú tekur upp nokkurt ósjálfstæði, opið eða séreign, skaltu meta heilsu þess: útgáfutakt, fjölda og fjölbreytni viðhaldsaðila, viðbragðsfýsi við öryggisskýrslum og breidd upptöku. Opið safn með einn viðhaldsaðila og lítill séreignarseljandi bera sömu **rútufaktoráhættu** (hættuna á að verkefni hrynji ef einn eða fáeinir lykilmenn fara). Kjóstu íhluti með breiðan framlagshóp eða fjárhagslega traustan seljanda og skráðu matið sem hluta af áreiðanleikakönnun (kaflar 10.2, 4.2).

### Lestu og raktu leyfi sem fyrsta flokks skyldu

Haltu skrá yfir hvern íhlut og leyfi hans og framfylgdu stefnu um hvaða leyfisfjölskyldur eru ásættanlegar fyrir hvaða notkun. Mikilvægi greinarmunurinn er copyleft. **Frjálslegur** kóði (MIT, Apache 2.0) má almennt fella frjálslega inn í lokaðar vörur. **Sterkt copyleft** (GPL) getur skyldað þig til að gefa út eigið dreift afleitt verk undir sömu skilmálum. Notaðu sjálfvirka **hugbúnaðarsamsetningargreiningu (SCA)**, verkfæri sem skanna ósjálfstæði þín til að bera kennsl á íhluti, leyfi og þekkta veikleika, og búðu til **hugbúnaðarefnisskrá (SBOM)**, formlega skrá yfir hvern íhlut í vöru (kaflar 10.3, 4.2).

### Dæmdu öryggi eftir venjum, ekki opnun

Gerðu ekki ráð fyrir að opinn hugbúnaður sé öruggur vegna **„mörg augu“ röksemdarinnar** ([lögmál Linusar](https://en.wikipedia.org/wiki/Linus%27s_law): „með nógu mörgum augum eru allir gallar grunnir“). Og gerðu ekki ráð fyrir að séreignarkóði sé öruggur gegnum **[öryggi með leynd](https://en.wikipedia.org/wiki/Security_through_obscurity)** (gallaða trúin að það feli galla að fela frumkóða). Mörg augu hjálpa aðeins ef hæft fólk horfir í raun og mörg mikið notuð verkefni eru þunnt viðhaldin. Bæði líkön bera **aðfangakeðjuáhættu**: opinn hugbúnaður gegnum brotin eða yfirgefin ósjálfstæði, séreign gegnum ógagnsæjan kóða og uppfærsluleiðir sem þú getur ekki skoðað. Festu útgáfur, staðfestu uppruna, skannaðu samfellt og vaktaðu ráðgjöf óháð líkani (kafli 4.2).

### Hannaðu fyrir útgöngu og samvirkni

Kjóstu íhluti sem tala opna staðla og flytjanleg gagnasnið, svo þú getir skipt þeim út síðar (kaflar 3.8, 10.11). Með opnum hugbúnaði færðu endanlegu útgönguna: ef verkefni stöðvast getur þú **[greint](https://en.wikipedia.org/wiki/Fork_(software_development))** það (búið til og viðhaldið eigin afriti). Með séreignarhugbúnaði skaltu semja um vernd fyrirfram: gagnaútflutning á opnum sniðum, skjalfest API og **[frumkóðatryggingu](https://en.wikipedia.org/wiki/Source_code_escrow)** (lagalegt fyrirkomulag þar sem seljandi leggur frumkóða inn hjá þriðja aðila, sem er afhentur þér ef seljandi bregst). Hannaðu svo enginn einn íhlutur, af hvorri gerð sem er, geti haldið kerfi þínu í gíslingu.

### Vegðu heildareignarkostnað, ekki yfirskriftarverð

Berðu kosti saman á **heildareignarkostnaði (TCO)**, fullum líftímakostnaði þar á meðal kaupum, samþættingu, rekstri, stuðningi, þjálfun, uppfærslum og endanlegri útskiptingu, frekar en leyfisgjöldum einum. Opinn hugbúnaður skiptir oft leyfiskostnaði út fyrir hærri rekstrar- og mönnunarkostnað. Séreignarhugbúnaður skiptir oft fyrirsjáanlegum áskriftargjöldum út fyrir innilokun og minni stjórn. Taktu með kostnað líkansins sjálfs: sjálfstyðjandi opinn hugbúnaður þarf færni innanhúss, en séreignarhugbúnaður þarf seljandastjórnunargetu.

### Sem framleiðandi, opnaðu það sem aðgreinir þig ekki

Flokkaðu eigin hugbúnað í það sem gefur þér samkeppnis- eða verkefnaforskot og það sem er óaðgreinandi lagnir. Haltu aðgreinendum séreign. Íhugaðu að opna hversdagsinnviðina, þar sem samfélag getur deilt viðhaldi og umbótum. Hjá hinu opinbera skaltu vega **„almannafé, almenningskóða“** (regluna að hugbúnaður fjármagnaður af skattgreiðendum ætti sjálfgefið að vera aðgengilegur almenningi) sem drifkraft gagnsæis, endurnýtingar og fullveldis (kaflar 10.5, 10.11). Veldu leyfið yfirvegað: frjálslegt til að hámarka upptöku, copyleft til að halda vistkerfinu opnu.

## Málamiðlanir: kostir og gallar

| Vídd | Opinn hugbúnaður | Lokaður / séreign |
|---|---|---|
| **Kaupkostnaður** | Venjulega enginn að eignast | Leyfis- eða áskriftargjald |
| **Heildareignarkostnaður** | Kostnaður færist í rekstur og mönnun | Fyrirsjáanlegri, en innilokunarálag |
| **Stjórn og sérsnið** | Full: þú getur lesið og breytt frumkóðanum | Takmörkuð við það sem seljandinn afhjúpar |
| **Stuðningur og ábyrgð** | Samfélag, eða greiddur þriðji aðili. Enginn einn að sækja til saka | Samningsbundinn stuðningur og skýr ábyrgur aðili |
| **Öryggisstaða** | Úttektarhæfur. „Mörg augu“ ef raunverulega viðhaldið | Seljandastýrður. Ógagnsær. Leynd er ekki vernd |
| **Langlífi / yfirgefning** | Má greina ef viðhaldið. Getur samt visnað | Veltur á lífvænleika og vegvísi seljanda |
| **Innilokun seljanda** | Lítil: frumkóði og opin snið gera útgöngu mögulega | Mikil nema dregið sé úr með stöðlum og tryggingu |
| **Vistkerfi** | Opið samfélag og samvirkni | Sérvalið, samþætt, stundum girt |

Endurtekna spennan er **stjórn á móti þægindum og ábyrgð**. Opinn hugbúnaður hámarkar stjórn, úttektarhæfni og frelsi frá innilokun, en hann biður þig að útvega getuna, samþættinguna og stuðninginn sjálf(ur). Séreignarhugbúnaður skilar studdri, samþættri, ábyrgri vöru með samning til að framfylgja, en hann gefur eftir stjórn og býður innilokun. Lausnin er sjaldan allt-eða-ekkert. Flestar þroskaðar eignir blanda opnum grunnum við séreignarkerfi þar sem stuðningur, ábyrgð eða sérhæfð geta réttlætir málamiðlunina.

## Spurningar til að ræða með teyminu

1. **Framfylgjum við leyfisstefnu með sjálfvirkri SCA og SBOM í leiðslunni, sérstaklega til að grípa sterkt copyleft áður en það er sent?** Að fella GPL-safn inn í dreifða séreignarvöru getur skyldað þig til að gefa út eigin frumkóða og það óvænta kemur yfirleitt seint í ljós, þegar dýrt er að vinda ofan af. Haltu skrá yfir hvern íhlut og leyfi hans, framfylgdu hvaða leyfisfjölskyldur eru ásættanlegar fyrir hvaða notkun og keyrðu hugbúnaðarsamsetningargreiningu sjálfvirkt svo leiðslan loki fyrir brot frekar en lögfræðingur grípi þau á sendingartíma. Búðu til SBOM sem sjálfsagðan hlut. Fyrir stóra eða opinbera eign er þetta líka aðfangakeðjuhreinlæti og oft innkaupakrafa. Komdu með núverandi leyfisskrá þína, eða þá staðreynd að þú hefur enga, og ákveddu hver á stefnuna.

2. **Þegar við tökum upp ósjálfstæði, metum við heilsu verkefnis og rútufaktor sem áreiðanleikakönnun?** Opið safn með einn viðhaldsaðila og lítill séreignarseljandi bera sömu áhættu: verkefnið hrynur ef einn eða fáeinir lykilmenn fara. Áður en þú tekur upp nokkuð skaltu meta útgáfutakt, fjölda og fjölbreytni viðhaldsaðila, viðbragðsfýsi við öryggisskýrslum og breidd upptöku og skrá matið. Hvorugt líkanið er öruggara sjálfgefið. „Mörg augu“ hjálpa aðeins ef hæft fólk horfir í raun og mörg mikið notuð verkefni eru þunnt viðhaldin. Komdu með þrjú eða fjögur ósjálfstæðin sem varan þín reiðir sig mest á og spyrðu, fyrir hvert, hve margir þyrftu að ganga burt áður en það yrði vandamál þitt. Ef þú getur ekki svarað er það matið sem þú skuldar sjálfum þér.

3. **Þegar við kaupum séreign, tryggjum við útgönguvernd fyrirfram?** Séreignarhugbúnaður býður ábyrgð og þægindi í skiptum fyrir stjórn og falinn kostnaður er innilokun: skiptikostnaður sem leyfir seljanda að hækka verð eða rýra þjónustu með litlu úrræði. Semdu um verndina áður en þú skrifar undir, þegar þú hefur enn áhrifavald: gagnaútflutning á opnum sniðum, skjalfest API og frumkóðatryggingu sem losar frumkóðann ef seljandi bregst. Með opnum hugbúnaði er útganga þín geta til að greina. Með séreign verður þú að skrifa útgönguna inn í samninginn. Komdu með mikilvægustu séreignarkerfi þín og spyrðu hvað gerist í raun ef seljandinn tvöfaldar verðið eða fer á hausinn. Ef svarið er „við erum föst“ skaltu laga samninginn við endurnýjun.

4. **Fyrir hugbúnaðinn sem við smíðum sjálf, hvernig ákveðum við hvað á að opna og hvað halda lokuðu og hver hefur vald til að taka þá ákvörðun?** Farðu rangt með í aðra áttina og þú gefur burt kóðann sem aðgreinir þig. Farðu rangt með í hina og þú hamstrar hversdagslagnir sem samfélag myndi glaðlega deila viðhaldinu á. Samkeppnisþrýstingurinn er raunverulegur: verkfræðingar vilja ráðninga- og orðsporsávinning opinberrar geymslu, á meðan vara og lögfræði óttast að afhenda keppinautum forskot eða afhjúpa öryggisviðkvæma þumalputtareglu. Komdu með heiðarlega flokkun kerfa þinna í verkefnaaðgreinandi á móti óaðgreinandi innviði og nefndu manneskjuna eða stjórnina sem samþykkir útgáfu, því ad hoc ákvörðun tekin af hverjum sem ýtti á geymsluna er hvernig krúnudjásn leka. Fyrir stórt fyrirtæki er spurningin eignasafnsstefna og hjá hinu opinbera rekst hún á „almannafé, almenningskóða“, regluna að skattfjármagnaður hugbúnaður ætti að vera opinber sjálfgefið, svo ákveddu fyrirfram hvaða undanþágur (þjóðaröryggi, svikagreining, persónuupplýsingar) réttlæta að halda kóða lokuðum.

5. **Ná smíða-eða-kaupa samanburðir okkar fullum heildareignarkostnaði, eða lítum við enn á núll leyfisgjald sem núll kostnað?** Algengustu fjárhagslegu mistökin með opinn hugbúnað eru að lesa „ókeypis að eignast“ sem „ókeypis að reka“ og uppgötva síðan að samþætting, rekstur, öryggisviðbrögð og greiddur stuðningur dverga hvaða leyfi sem þú forðaðist. Spennan er að séreignaráskrift lítur dýr út á reikningnum á meðan hún felur innilokunarálag og opinn íhlutur lítur ókeypis út á reikningnum á meðan hann færir kostnað á eigið starfsfólk. Komdu með eins-fyrir-eins TCO-líkan fyrir tvær eða þrjár raunverulegar ákvarðanir: kaup, samþættingu, rekstur, stuðning, þjálfun, uppfærslur, öryggisviðbrögð og endanlega útskiptingu, verðlagt yfir allan líftímann frekar en fyrsta árið. Í fyrirtækja- eða opinberri eign skaltu bæta við kostnaði rekstrarlíkansins sjálfs, þar sem sjálfstyðjandi opinn hugbúnaður krefst færni innanhúss sem þú verður að ráða og halda, og líttu á samanburð sem sleppir þessum línum sem sönnunargagn, ekki greiningu.

6. **Dæmum við öryggi íhlutar eftir venjum hans, eða treystum við á opnunarmerkið, hvort sem er „mörg augu“ eða leynd lokaðs kóða?** Bæði sjálfgildin eru gildrur: „mörg augu“ vernda þig aðeins þegar hæft fólk rýnir í raun kóðann og mörg mikið notuð opin verkefni keyra á einum örmagna viðhaldsaðila, á meðan lokaður hugbúnaður sem treystir á að árásaraðilar sjái hann ekki er öryggi með leynd, ekki stýring. Umræðan skiptir máli því hún breytir því hvar þú eyðir knöppu öryggisátaki og heiðarlega svarið er að bæði líkön bera aðfangakeðjuáhættu, opinn hugbúnaður gegnum brotin eða yfirgefin ósjálfstæði og séreign gegnum ógagnsæjar uppfærsluleiðir sem þú getur ekki skoðað. Komdu með sönnunargögn fyrir mikilvægustu íhluti þína: hver rýnir þá í raun, hve hratt ráðgjöf er plástruð, hvort útgáfur eru festar og uppruni staðfestur og hvort þú býrð til SBOM. Fyrir stóra eða opinbera eign skaltu tengja þetta við innkaup og samfelldar skönnunarskyldur, því eftirlitsaðili mun spyrja hvað þú skoðaðir, ekki hvort frumkóðinn var opinber.

## Sjónarhorn eftir geirum

**Sprotafyrirtæki.** Með litla fjárhagslega þrautseigju smíðar þú á opnum grunnum því þú hefur ekki efni á leyfisgjöldum og vilt frelsið til að greina ef verkefni stöðvast. Keyrðu samsetningargreiningarskönnun áður en þú sendir svo sterkt copyleft-safn skyldi þig ekki hljóðlega til að birta eigin frumkóða og haltu þínum eina raunverulega aðgreini strangt lokuðum. Opnaðu lítið, ómikilvægt verkfæri ef það hjálpar ráðningum, en mannaðu ekki viðhaldsbyrði sem þú getur ekki borið.

**Lítið fyrirtæki.** Án lögfræðings eða innri vettvangssérfræðings skaltu líta á leyfið sem áhættu sem þú mátt ekki misskilja frekar en viðfangsefni sem þú getur náð tökum á. Kjóstu studd séreignarverkfæri eða viðskiptaútgáfur opins hugbúnaðar þar sem seljandi á plástra og ábyrgð, því að styðja sjálf(ur) staflann sem þú getur ekki rekið er fölsk hagkvæmni. Þegar þú tekur upp ókeypis íhlut skaltu athuga að leyfi hans leyfi notkun þína og að verkefnið sé í raun viðhaldið, ekki yfirgefið.

**Stórfyrirtæki.** Í stærð er vandinn samræmi milli margra teyma: skrifleg leyfisstefna, sjálfvirk hugbúnaðarsamsetningargreining og SBOM-gerð í hverri leiðslu og smíða-eða-kaupa ákvarðanir byggðar á TCO frekar en vana hvers teymis. Stýrðu opnum og séreignarhugbúnaði sem einu safni, staðlaðu útgönguvernd eins og opin snið og frumkóðatryggingu í innkaupum og fylgstu með heilsu mikilvægra ósjálfstæða svo eitt yfirgefið verkefni verði ekki atvik. Stýrðu framleiðendahliðinni líka, með skýrri reglu um hvað skipulagsheildin opnar á móti því sem hún heldur lokuðu.

**Hið opinbera.** Innkaupareglur, gagnsæisskyldur og opinber ábyrgð móta hvert val. Vegðu „almannafé, almenningskóða“, regluna að skattfjármagnaður hugbúnaður ætti að vera opinber sjálfgefið, til að efla endurnýtingu milli stofnana og stafrænt fullveldi, á sama tíma og þú ristir þröngar undanþágur fyrir öryggisviðkvæman eða persónuupplýsingakóða. Krefstu þess að hver séreignarbirgir veiti gagnaútflutning á opnum sniðum og frumkóðatryggingu svo seljandabilun geti ekki strandað opinbera þjónustu og birtu ekki-viðkvæma frumkóðann svo borgarar geti úttekið reglurnar sem stýra þeim.

## Dæmi

**Sprotafyrirtæki.** Þriggja stofnenda sprotafyrirtæki smíðar alla vöru sína á opnum grunnum (Linux, opnum gagnagrunni, veframmaverki) því það hefur ekki efni á leyfisgjöldum og vill frelsið til að greina ef verkefni stöðvast. Fyrir sendingu keyrir einn stofnandi samsetningargreiningarskönnun og grípur sterkt copyleft-safn sem hefði þvingað þau til að birta séreignarsamsvörunarreikniritið sitt, svo þau skipta því út fyrir jafngildi með frjálslegu leyfi. Þau halda því reikniriti, sínum eina aðgreini, strangt lokuðu og opna aðeins lítið innra skráningarverkfæri til að byggja velvild og laða að verkfræðinga.

**Stórfyrirtæki.** Stórt tryggingafélag rekur kjarnavettvang sinn á opnum grunnum: Linux, víða notuðum opnum gagnagrunni og gámastýringu. En það kaupir séreignarlíkanasvítu fyrir tryggingastærðfræði, því sérfræðiþekking seljandans á sviðinu, regluverksvottanir og stuðningssamningur eru gjaldsins virði og ekkert sambærilegt opið val er til. Það borgar áskrift að **viðskiptaútgáfu opins hugbúnaðar** (seljandastuddum dreifingum opnu íhlutanna) til að fá ábyrgð og plástra á lögnunum, á meðan það heldur verðlagningarreikniritinu sem aðgreinir það strangt séreign og innanhúss. TCO-greining (kafli 10.10) knýr hvert val frekar en hugmyndafræði.

**Hið opinbera.** Landsbundið skattyfirvald, undir stefnunni „almannafé, almenningskóði“, smíðar nýja bótarétthæfisþjónustu á opnum íhlutum og opnum stöðlum (kafli 3.8), svo aðrar stofnanir geti endurnýtt hana og borgarar geti úttekið reglurnar. Það birtir ekki-viðkvæma kóðann í opinberri geymslu og heldur aðeins svikagreiningarþumalputtareglum lokuðum af öryggisástæðum. Þetta dregur úr innilokun seljanda og eflir stafrænt fullveldi (kafli 10.11). Innkaupareglur (kafli 10.3) krefjast þess að hver séreignaríhlutur veiti gagnaútflutning á opnum sniðum og frumkóðatryggingu, til að tryggja samfellu ef birgir bregst.

## Viðskiptarök: hvatar, ávöxtun fjárfestingar og heildarkostnaður

Fjárhagsleg aðdráttarafl opins hugbúnaðar, skortur á leyfisgjaldi, er óáreiðanlegasti hluti raka, því kaup eru lítið brot af TCO. Endingargóðu ávöxtunin er stefnumótandi: frelsi frá innilokun (getan til að skipta um eða sleppa birgi án þess að endurarkitektúrera), úttektarhæfni fyrir öryggi og reglufylgni, hraðari upptaka því verkfræðingar geta prófað áður en þeir skuldbinda sig og sameiginlegt viðhald hversdagskóða yfir heila atvinnugrein. Mótkostnaðurinn er raunverulegur. Þú verður að útvega samþættingu, rekstur, öryggisviðbrögð og oft greiddan stuðning og illa valið óviðhaldið verkefni getur kostað meira í atvikum en nokkurt leyfi hefði gert.

Viðskiptarök séreignarhugbúnaðar eru ábyrgð og þægindi: einn seljandi ábyrgur fyrir vörunni, stuðningssamningur sem þú getur framfylgt, samþættir eiginleikar og fyrirsjáanleg fjárhagsáætlunargerð. Falinn kostnaður hans er innilokun, skiptikostnaðurinn sem leyfir seljanda að hækka verð eða rýra þjónustu með litlu úrræði, auk ósjálfstæðis gagnvart gjaldþoli og vegvísi seljandans. Algeng **viðskiptalíkön** þoka línuna: **[opinn kjarni](https://en.wikipedia.org/wiki/Open-core_model)** (opinn grunnur með greiddum séreignarviðbótum), **tvöfalt leyfi** (sami kóði boðinn undir bæði copyleft-leyfi og greiddu viðskiptaleyfi), **[hugbúnaður sem þjónusta](https://en.wikipedia.org/wiki/Software_as_a_service) (SaaS)** (hugbúnaðurinn keyrir sem hýst þjónusta sem þú leigir, þar sem frumkóðinn getur verið óviðkomandi því þú átt aldrei tvíundarskrána) og **stuðnings-/áskriftar** líkön sem selja þjónustu í kringum annars frjálsan kóða.

Fyrir framleiðanda getur ávöxtun þess að **opna eigin óaðgreinandi hugbúnað** verið umtalsverð. Utanaðkomandi framlagsaðilar draga úr viðhaldsálagi þínu. Verkefnið verður ráðningar- og orðsporseign. Ytri upptaka gerir staðal þinn að þeim ríkjandi. Hjá hinu opinbera skilar það gagnsæi og endurnýtingu yfir opinbera geirann. Stefnumótandi reglan er einföld: opnaðu hversdagsvöruna til að deila kostnaði hennar og rækta vistkerfi og haltu aðgreininum lokuðum til að vernda forskotið sem fjármagnar allt annað.

## Andmynstur og gildrur

- **„Ókeypis þýðir ókeypis“:** að líta á núll kaupkostnað sem núll TCO og vanfjármagna síðan rekstur og stuðning.
- **Leyfisblinda:** að fella sterkt copyleft-kóða inn í dreifða séreignarvöru og ræsa skyldur sem þú skipulagðir aldrei.
- **Trú á „mörg augu“:** að gera ráð fyrir að opið verkefni sé úttekið þegar það hefur einn ofhlaðinn viðhaldsaðila og enga öryggisrýni.
- **Öryggi með leynd:** að trúa að lokaður frumkóði sé öruggur einfaldlega af því árásaraðilar geta ekki lesið hann.
- **Hugmyndafræðileg algildishyggja:** að skylda „allt opið“ eða „allt séreign“ í stað þess að velja á hvern íhlut eftir verðleikum og TCO.
- **Að hunsa uppruna:** að draga inn ósjálfstæði án SBOM, útgáfufestingar eða aðfangakeðjustaðfestingar (kafli 4.2).
- **Að opna krúnudjásnin:** að gefa út kóðann sem aðgreinir þig, sem gefur burt forskot þitt.
- **Greina-og-gleyma:** að greina yfirgefið verkefni án getu til að viðhalda greininni í raun.

## Þroskalíkan

**Stig 1 (Upphaf).** Opnir og séreignaríhlutir koma inn í eignina ad hoc. Leyfi eru ólesin, engin skrá eða SBOM er til og valið milli líkana er gert af vana eða verði einu. Yfirgefning og leyfisáhætta kemur aðeins í ljós þegar eitthvað bilar og hvert teymi bregst við á eigin spýtur.

**Stig 2 (Þróun).** Sum teymi byrja á grunnvenjum: íhlutaskrá og leyfisskrá, gróf sýn á ásættanleg leyfi og stöku hugbúnaðarsamsetningargreining. Smíða-eða-kaupa og opið-eða-lokað ákvarðanir eru skráðar, en agi er götóttur og ósamræmdur milli teyma, svo copyleft- eða rútufaktorsóvænt getur samt sloppið í gegn þar sem vaninn hefur ekki fest rætur.

**Stig 3 (Stöðlun).** Skjalfest rammaverk stýrir bæði notkun og framleiðslu um skipulagsheildina. Íhlutir eru valdir á TCO og verkefnaheilsu, leyfum er framfylgt sjálfvirkt í leiðslunni svo brot loki smíði, SBOM eru búin til sem sjálfsagður hlutur og skýr stefna segir hvað skipulagsheildin opnar á móti því sem hún heldur lokuðu. Útgönguvernd eins og opin snið og frumkóðatrygging er staðlað í innkaupum og öll teymi fylgja sömu reglum frekar en eigin.

**Stig 4 (Stjórnun).** Áætlunin er mæld og stýrð gegn grunnlínum. Skipulagsheildin rekur mælikvarða eins og SBOM-þekju yfir vörur, hlutfall ósjálfstæða sem brjóta stefnu, meðaltíma til að plástra birtan ósjálfstæðisveikleika, rútufaktors- og heilsueinkunnir mikilvægra verkefna og raungerðan TCO gegn áætluninni sem réttlætti hvert val. Þröskuldar ræsa aðgerð: íhlutur sem viðhald stöðvast á eða plástratöf rekur yfir markmið er merktur til útskiptingar á sönnunargögnum og opið-eða-lokað og smíða-eða-kaupa ákvarðanir eru rýndar gegn tölunum frekar en varðar af vana.

**Stig 5 (Samhæfing).** Opin hugbúnaðarstefna er yfirveguð viðskiptageta, samþætt um skipulagsheildina og stöðugt bætt. Skipulagsheildin leggur til og stýrir stundum verkefnunum sem hún er háð, opnar óaðgreinandi hugbúnað sinn sem sjálfsagðan hlut og nærir ósjálfstæðisheilsu- og TCO-gögnum aftur inn í innkaupa-, öryggis- og vöruáætlanagerð. Hún endurjafnar reglulega safn sitt af opnum og séreignarhugbúnaði, aðlagast breytingum í kostnaði, áhættu, fullveldi og stefnumótandi forskoti áður en þær þvinga fram kreppu.

## Hugmyndir til umræðu

- Hvar í eign ykkar myndi missir eins seljanda eða viðhaldsaðila vera tilvistarlegur og hver er útgönguáætlun ykkar?
- Hver eigin kerfa ykkar eru hversdagsvara sem þið gætuð opnað og hver eru raunverulegir aðgreinendur til að vernda?
- Lítur skipulagsheild ykkar á „mörg augu“ sem raunverulega öryggisstýringu eða órannsakaða forsendu?
- Fyrir lesendur í opinbera geiranum: hverju myndi „almannafé, almenningskóði“ sjálfgefið breyta í næstu innkaupum ykkar?
- Hve vel ná TCO-samanburðir ykkar rekstrar- og stuðningskostnaðinum sem opinn hugbúnaður færir á ykkur?

## Helstu atriði

- **Opið á móti lokuðu er skilgreint af leyfinu**, ekki verði. Þekktu muninn á frjálst-sem-í-frelsi og frjálst-sem-í-verði og milli frjálslegs og copyleft.
- **Hvorugt líkanið er í eðli sínu öruggara eða ódýrara.** Dæmdu venjur verkefnisins og fullan TCO, ekki opnunarmerkið.
- **Opnun er sterkasta mótefnið við innilokun**, sem skilar úttektarhæfni, flytjanleika og getu til að greina. Séreignarhugbúnaður býður ábyrgð og þægindi í skiptum fyrir stjórn.
- **Ákveddu á hvern íhlut eftir verðleikum** og blandaðu líkönum yfirvegað frekar en eftir hugmyndafræði.
- **Sem framleiðandi, opnaðu hversdagsvöruna og haltu aðgreininum lokuðum**, og hjá hinu opinbera, vegðu „almannafé, almenningskóða“ fyrir gagnsæi, endurnýtingu og fullveldi.

## Heimildir og frekari lestur

- Eric S. Raymond, *The Cathedral and the Bazaar*
- Nadia Eghbal, *Working in Public: The Making and Maintenance of Open Source Software*
- Karl Fogel, *Producing Open Source Software: How to Run a Successful Free Software Project*
- Adrian Cockcroft and others, various O'Reilly titles on open-source strategy and operations
- Free Software Foundation, *The Free Software Definition* (and the GNU General Public Licence texts)
- Open Source Initiative, *The Open Source Definition* and approved-licence list
- Free Software Foundation Europe, *Public Money, Public Code* campaign materials
- Yochai Benkler, *The Wealth of Networks*
