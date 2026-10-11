# 4.8 Dulritun og lyklastjórnun

## Yfirlit og tilgangur

Nánast hvert kerfi sem þú smíðar byggir þegar á [dulritun](https://en.wikipedia.org/wiki/Cryptography), þeirri venju að vernda upplýsingar með stærðfræðilegum aðferðum svo aðeins ætlaðir aðilar geti lesið þær eða treyst þeim. Vefumferð þín ferðast á dulkóðuðum rásum, lykilorð þín eru kjötkássuð, hugbúnaðaruppfærslur þínar eru undirritaðar og viðskiptavinagögn þín sitja dulkóðuð á diski. Góðu fréttirnar fyrir flesta verkfræðinga eru að ætlast er ekki til að þú finnir upp neitt af þessu. Erfiði hlutinn er ekki stærðfræðin. Hann er að nota sannreyndar byggingareiningar rétt og, umfram allt, að stýra lyklunum sem þær byggja á.

Þessi kafli er skrifaður fyrir verkfræðinga sem eru ekki dulritunarfræðingar, sem er nánast okkur öll. Þú þarft nægan skilning til að taka skynsamleg val, vita hvað hvert verkfæri tryggir og forðast mistökin sem breyta sterkum reikniritum í falska huggun. Kafli 4.3 (öryggi innviða og skýs) nefnir dulkóðun og lyklastjórnun í framhjáhlaupi. Hér förum við dýpra í hvað á að dulkóða, hvernig og hvernig á að reka lyklalífsferilinn sem gerir það raunverulegt.

Fyrir stór fyrirtæki dreifist dulritun yfir þúsundir þjónusta, skírteina og lykla, og eitt útrunnið skírteini eða týndur lykill getur tekið mikilvægt kerfi niður eða lekið gagnageymslu. Fyrir hið opinbera er dulritun oft fyrirskipuð, vottuð og úttekin, með gagnaflokkunarreglum sem ráða nákvæmlega hvaða lyklar vernda hvaða leyndarmál og hverjir mega halda þeim. Í báðum umhverfum er endurtekna bilunin sú sama: góð reiknirit grafin undan af ónákvæmri lyklastjórnun.

## Meginreglur

- **Finndu ekki upp eigin dulritun.** Notaðu sannreynd, víðrýnd bókasöfn og staðlaðar reiknirit. Nýsmíðuð dulritun bilar á vegu sem aðeins sérfræðingar grípa.
- **Reiknirit eru auðveldi hlutinn. Lyklar eru erfiði hlutinn.** Líftími lykils er þar sem flestar raunverulegar bilanir búa.
- **Vittu hvað hvert frumstætt tryggir.** Trúnaður, heilleiki og áreiðanleiki eru ólíkir eiginleikar sem krefjast ólíkra verkfæra.
- **Dulkóðaðu á ferð og í hvíld sjálfgefið.** Gerðu vernd að staðlinum, ekki valkvæðri.
- **Aðskildu lyklavörslu frá gagnaaðgangi.** Sá sem stýrir lykli ætti ekki sjálfkrafa að geta lesið gögnin sem hann ver.
- **Skipuleggðu fyrir breytingar.** Reiknirit veikjast, lyklar leka og staðlar þróast. Byggðu fyrir snúning og flutning frá degi eitt.
- **Kjóstu vottaðar útfærslur þar sem það skiptir máli.** Fyrir eftirlitsskylt og opinbert starf skaltu velja einingar með viðurkenndri vottun.

## Ráðleggingar

### Finndu ekki upp eigin dulritun

Þetta er gullna reglan og vert að nefna fyrst. Hannaðu aldrei eigið dulkóðunarreiknirit, finndu upp eigin samskiptareglu eða handútfærðu frumstætt úr grein. Virk dulritun lítur einföld út og felur lúmska bilunarhætti (tímahliðarrásir, fyllingarspádóma, veika slembni) sem aðeins lifa af ára sérfræðirýni. Notaðu rótgróin bókasöfn eins og staðlaða dulritunareiningu vettvangs þíns eða vel metið bókasafn og notaðu þau á hæsta ágripunarstigi sem í boði er. Náðu í auðkennda dulkóðunarhætti (authenticated encryption) og „auðveld“ viðmót sem gera örugga valið að sjálfgefnu, frekar en að setja saman lágstigsbita sjálfur.

### Láttu frumstætt samsvara tryggingunni sem þú þarft

Ólík verkfæri veita ólíkar tryggingar og að rugla þeim er algeng og hættuleg mistök. Lærðu þrjár meginfjölskyldurnar.

- **[Samhverf lykil](https://en.wikipedia.org/wiki/Symmetric-key_algorithm)dulritun** notar einn sameiginlegan leynilykil bæði til að dulkóða og afkóða. Hún er hröð og ver **trúnað**, en báðir aðilar verða þegar að deila lyklinum. AES er staðlaði vinnuhesturinn.
- **[Opinberlykla](https://en.wikipedia.org/wiki/Public-key_cryptography)dulritun** notar stærðfræðilega tengt lyklapar: opinberan lykil sem hver sem er getur haldið og einkalykil sem þú heldur leyndum. Hún leysir lyklaafhendingu og gerir **stafrænar undirskriftir** mögulegar, sem sanna **áreiðanleika** (hver sendi það) og **heilleika** (að því var ekki breytt).
- **[Dulritunarkjötkássufall](https://en.wikipedia.org/wiki/Cryptographic_hash_function)** framleiðir fastastærðar fingrafar gagna og veitir **heilleika**athugun. Kjötkássun er einstefna og er ekki dulkóðun. Til að geyma lykilorð skaltu nota hægt, saltað lykilorðskjötkássufall, aldrei venjulegt hraðkjötkássa (sjá kafla 4.2 um forritaöryggi).

Hagnýta lexían: dulkóðun felur gögn en sannar ekki hver sendi þau, og kjötkássa greinir fikt en felur ekkert. Flest raunveruleg kerfi sameina þetta, sem er einmitt ástæða þess að þú ættir að hallast að bókasöfnum sem búnta þetta rétt.

### Dulkóðaðu á ferð með núverandi TLS

Verndaðu hvert netstökk með [Transport Layer Security](https://en.wikipedia.org/wiki/Transport_Layer_Security) (TLS), samskiptareglunni sem tryggir gögn þegar þau færast milli kerfa. Krefstu nútíma TLS-útgáfa, afvirkjaðu úreltar, veldu sterkar dulmálssvítur og staðfestu skírteini rétt frekar en að slökkva á athugunum til að „fá það til að virka“. Dulkóðaðu innri þjónustu-í-þjónustu umferð líka, ekki bara opinbera jaðarinn, því núlltraustarstaða gerir ráð fyrir að innra netið sé fjandsamlegt. Sjálfvirknivæddu skírteinaútgáfu og endurnýjun svo TLS sé fyrirhafnarlaust sjálfgefið alls staðar.

### Dulkóðaðu í hvíld með umslagsdulkóðun

Dulkóðaðu geymd gögn sjálfgefið: gagnagrunna, hlutageymslu, afrit og skrár. Staðlaða mynstrið er **umslagsdulkóðun** (envelope encryption), þar sem **gagnadulkóðunarlykill (DEK)** dulkóðar raunveruleg gögn, og **lykladulkóðunarlykill (KEK)** haldinn í lyklastjórnunarþjónustu dulkóðar DEK. Þetta leyfir þér að snúa meistaralyklinum án þess að endurdulkóða terabæti af gögnum og heldur öfluga rótarlyklinum innan hertra marka. Geymdu aðeins umvafða DEK við hlið gagnanna og sæktu og afvafðu hann við notkun.

### Reku lyklalífsferilinn af ásetningi

Líftími lykils er raunverulega erfiði hluti dulritunar og þar sem flest innbrot og rekstrarrof eiga upptök. Stýrðu hverju skeiði af ásetningi:

- **Myndun:** búðu til lykla úr sterkri slembiuppsprettu, á viðeigandi styrk.
- **Dreifing:** komdu lyklum til kerfanna sem þurfa þá án þess að afhjúpa þá í kóða, stillingarskrám eða spjalli.
- **Snúningur:** skiptu lyklum út á áætlun og vertu fær um að snúa hratt við grun um brot.
- **Afturköllun:** ógildu brotinn lykil eða skírteini fljótt og tryggðu að kerfi virði afturköllunina.
- **Eyðing:** hættu notkun gamals lyklaefnis á öruggan hátt svo ekki sé hægt að endurheimta það.

Notaðu **lyklastjórnunarþjónustu (KMS)** til að miðlægja þetta og notaðu [vélbúnaðaröryggiseiningu](https://en.wikipedia.org/wiki/Hardware_security_module) (HSM), fikthelt tæki sem býr til og gætir lykla svo þeir yfirgefi aldrei í skýrum texta, fyrir lykla með hæstu tryggingu. Aðgreindu hver getur stýrt lyklum frá hver getur lesið vernduðu gögnin, svo lyklavarsla framfylgi aðskilnaði skyldna. Þetta tengist beint gagnaflokkunar- og vörslureglum í kafla 4.5 (persónuvernd og gagnavernd).

### Greindu milli leyndarmálastjórnunar og lyklastjórnunar

Þetta skarast en er ekki það sama. **Lyklastjórnun** stýrir dulritunarlyklum og lífsferli þeirra, yfirleitt innan KMS eða HSM sem framkvæmir dulritunaraðgerðir fyrir þig svo hrái lykillinn yfirgefi aldrei. **Leyndarmálastjórnun** stýrir forritaauðkennisgögnum (gagnagrunnslykilorðum, API-táknum, skírteinum) sem þjónustur þurfa að sækja og nota í skýrum texta, yfirleitt úr leyndarmálahvelfingu með skammlífum, úttektuðum aðgangi. Notaðu KMS fyrir lykla, leyndarmálastjóra fyrir auðkennisgögn og límdu hvorugt inn í frumkóða eða umhverfisskrár innritaðar í útgáfustýringu.

### Sjálfvirknivæddu PKI og skírteinalífsferla

**Opinberlyklainnviðir (PKI)** eru kerfi skírteinaveitna, skírteina og traustkeðja sem bindur opinbera lykla við auðkenni. Í stærð er ráðandi PKI-áhættan óvænt skírteinafyrning sem tekur þjónustu niður. Haltu skrá yfir hvert skírteini, vaktaðu fyrningar og sjálfvirknivæddu útgáfu og endurnýjun svo enginn maður þurfi að muna. Skammlíf skírteini endurnýjuð sjálfvirkt eru öruggari en langlíf sem eru handstýrð í höndunum, því sjálfvirkni fjarlægir mannlega einstaka bilunarpunktinn. Staðlaðar samskiptareglur hér styðja samvirkni yfir söluaðila (kafli 3.8 um samvirkni og opna staðla).

### Byggðu fyrir dulritunarlipurð og post-quantum flutning

Reiknirit veikjast með tímanum og staðlar hreyfast. **Dulritunarlipurð** (cryptographic agility) þýðir að hanna kerfi þannig að þú getir skipt um reiknirit og lyklastærðir án sársaukafullrar endurskriftar: ágripaðu dulritun á bak við lítið viðmót, útgáfumerktu dulkóðuð gögn þín svo þú vitir hvaða reiknirit framleiddi þau og haltu dulritunarskrá yfir hvað þú notar hvar. Þetta skiptir máli núna vegna [skammtafræðiþolinnar dulritunar](https://en.wikipedia.org/wiki/Post-quantum_cryptography), nýrrar fjölskyldu reiknirita hannaðra til að standast framtíðarskammtatölvur. Andstæðingar geta safnað dulkóðuðum gögnum í dag til að afkóða síðar, svo langlíf leyndarmál þarfnast flutningsáætlunar. Þú þarft ekki að fyllast skelfingu, en þú ættir að þekkja skrána þína og vera tilbúinn að taka upp stöðluðu skammtafræðiþolnu reikniritin þegar vettvangar afhenda þau.

### Kjóstu vottaðar útfærslur þar sem krafist er

Fyrir eftirlitsskyld og opinber kerfi er sterkt reiknirit ekki nóg. Útfærslan verður að vera vottuð. **FIPS 140** (Federal Information Processing Standard 140) er bandaríski staðallinn til að votta dulritunareiningar og margir samningar krefjast FIPS-vottaðrar dulritunar. Opinbert starf kann einnig að fylgja landsleiðbeiningum eins og Commercial National Security Algorithm (CNSA) svítu NSA fyrir leynileg kerfi. Athugaðu hvaða kerfi á við áður en þú smíðar, því að bæta við vottuðum einingum seint er dýrt. Þetta tengist regluvörslusönnunargögnum og stjórnarháttum (kafli 4.6).

## Málamiðlanir: kostir og gallar

| Ákvörðun | Kostir | Gallar |
|---|---|---|
| Veitendastýrt KMS | Auðvelt, samþætt, lág rekstrarbyrði | Veitandinn heldur vörslu. Minni bein stjórn |
| Viðskiptavinastýrðir lyklar / HSM | Full varsla, uppfyllir strangar kröfur | Rekstraraukakostnaður, hætta á að tapa lyklum |
| Sjálfvirk skammlíf skírteini | Engar óvæntar fyrningar, hröð afturköllun | Krefst sjálfvirknifjárfestingar fyrirfram |
| Langlíf skírteini | Einföld, færri hreyfanlegir hlutar | Mannstýrðar fyrningar valda rekstrarrofum |
| Umslagsdulkóðun | Ódýr lyklasnúningur, ver meistaralykilinn | Fleiri hreyfanlegir hlutar til að skilja |
| Dulritunarlipurð fyrirfram | Ódýrir framtíðarflutningar | Aukaágripun og hönnunarfyrirhöfn núna |
| Snemmbúin upptaka skammtafræðiþols | Ver langlíf leyndarmál | Óþroskuð verkfæri, stærri lyklar, nokkur áhætta |

Meginspennan er stjórn gegn rekstrarbyrði. Að halda eigin lyklum í HSM gefur hámarksvörslu og uppfyllir ströngustu kröfur, en krefst sérfræðiþekkingar og skapar nýja skelfilega áhættu: tapaðu lyklinum og þú tapar gögnunum, óafturkræft. Veitendastýrðar þjónustur fjarlægja þá byrði en setja vörslu hjá veitandanum. Leystu það með lagskiptingu: notaðu stýrðar þjónustur með skynsamlegum sjálfgefnum gildum fyrir flest kerfi og taktu viðskiptavinastýrða lykla og HSM frá fyrir gögn með hæstu flokkun þar sem aukastjórnin er kostnaðarins og áhættunnar virði.

## Spurningar til að ræða með teyminu

1. **Hafið þið fullkomna skrá yfir lykla ykkar, skírteini og reikniritin sem þið reiðið ykkur á?** Þú getur ekki snúið, flutt eða úttektað það sem þú sérð ekki, og flestar skipulagsheildir uppgötva að þær hafa langtum meira dulritunarefni dreift yfir þjónustur en nokkur rekur. Skrá er forsenda hverrar síðari ákvörðunar: skírteinafyrningarvöktun, lyklasnúningur, FIPS-umfang og skammtafræðiþolsáætlun byggja öll á henni. Komdu með lista yfir núverandi skírteini þín og fyrningardagsetningar og spyrðu hver á hvert og hvað brotnar þegar það rennur út. Fyrir stórt bú er heiðarlega svarið yfirleitt að engin einstök sannleiksuppspretta er til, og að byggja eina er áhrifamesta fyrsta skrefið. Ef þú getur ekki talið upp dulritun þína í dag eru lipurð og snúningur metnaður, ekki geta.

2. **Getið þið snúið eða afturkallað brotinn lykil hratt og hafið þið nokkurn tíma æft það?** Snúningur og afturköllun eru hlutar lyklalífsferilsins sem skipta aðeins máli undir þrýstingi, og teymi uppgötva rútínulega í atviki að lykill er harðkóðaður á tylft stöðum eða að afturköllun breiðist ekki raunverulega út. Ákveddu markmiðstíma þinn til að snúa lykli og afturkalla skírteini og æfðu það síðan áður en þú þarft það. Komdu með söguna af síðustu auðkennisgagnaafhjúpun þinni og gakktu í gegnum hvað snúningur krafðist í reynd. Fyrir fyrirtækja- og opinber kerfi getur óæfður snúningur þýtt val milli langvarandi afhjúpunar og sjálfskaðandi rekstrarrofs. Ef snúningur hefur aldrei verið prófaður skaltu gera ráð fyrir að hann virki ekki.

3. **Hvar situr lyklavarsla og framfylgir hún aðskilnaði skyldna?** Sá sem getur stýrt lykli og sá sem getur lesið gögnin sem hann ver ættu ekki að vera sami maðurinn, því að sameina þessi völd grefur hljóðlega undan tilgangi dulkóðunar í hvíld. Þetta val ræður líka hvort þú notar veitendastýrða lykla, viðskiptavinastýrða lykla eða HSM, hvert með ólíka stjórn og ólíka rekstraráhættu. Komdu með núverandi lyklastefnur þínar og athugaðu hvort eitthvert eitt auðkenni geti bæði stýrt lykli og nálgast skýra textann að baki honum, sem er algengt hljótt bil. Fyrir eftirlitsskyld og leynileg gögn geta vörslureglur verið fyrirskipaðar af gagnaflokkun (kafli 4.5) og af skyldu. Ef varsla og aðgangur eru ekki aðskilin verndar dulkóðun þín þig minna en mælaborðið gefur til kynna.

4. **Hvernig mynduð þið jafna ykkur ef meistaralykillinn sem ver umslagsdulkóðun ykkar týndist eða eyðilegðist?** Viðskiptavinastýrðir lyklar og HSM gefa þér vörslu, en þeir fá þér nýjan skelfilegan bilunarhátt: tapaðu lykladulkóðunarlyklinum og sérhver gagnadulkóðunarlykill sem hann umvefur verður varanlega ólæsilegur, ásamt gögnunum að baki þeim. Vegðu þetta gegn andstæðri áhættu of víðs afrits sem hljóðlega endurskapar einmitt vörsluvandann sem þú varst að reyna að leysa. Komdu með núverandi lyklaafrits- og vörslusamkomulög þín, sprengjusvæði hvers meistaralykils og sönnunargögn um að endurheimt hafi raunverulega verið framkvæmd frekar en aðeins skjalfest. Fyrir fyrirtækja- og opinber bú skaltu tengja þetta við gagnaflokkunarreglur þínar: viðkvæmustu lyklarnir banna oft kæruleysisleg afrit, svo endurheimt verður að vera hönnuð af ásetningi, prófuð á áætlun og samræmd hverri regluverkskröfu um að sanna að hætt lyklaefni hafi verið eytt.

5. **Hve tilbúin eru kerfi ykkar fyrir post-quantum flutning og hvaða langlífu leyndarmál mynduð þið flytja fyrst?** Andstæðingar geta safnað dulkóðaðri umferð og skjalasöfnum í dag og afkóðað þau þegar skammtatölvur þroskast, svo hvert leyndarmál sem verður að haldast leynt árum saman er þegar útsett fyrir framtíð sem þú sérð ekki. Þrýstingurinn á móti er að skammtafræðiþolin verkfæri eru enn ung, lyklarnir eru stærri og að flytja of snemma teflir í hættu veðmáli á reiknirit sem breytist áður en það sest. Komdu með dulritunarskrá þína, lista yfir leyndarmál raðaða eftir hve lengi þau verða að haldast leynileg og heiðarlegt mat á því hvort arkitektúr þinn geti skipt um reiknirit án endurskriftar. Fyrir opinbert og eftirlitsskylt starf gera skrár með áratuga trúnaðarskyldu þetta áþreifanlegt frekar en fræðilegt, og innkaup kunna fljótlega að krefjast skjalfestrar flutningsáætlunar og stuðnings við stöðluðu skammtafræðiþolnu reikniritin.

6. **Þegar regluverk krefst vottaðrar dulritunar, vitið þið nákvæmlega hvaða einingar eru í umfangi og hvort þær uppfylla skilyrði?** Að nota sterkt reiknirit er ekki það sama og að nota vottaða útfærslu, og teymi uppgötva rútínulega seint að bókasafn, tungumálakeyrsluumhverfi eða skýjaþjónusta er ekki dekkuð af FIPS 140 mörkunum sem samningur krefst. Spennan er að vottaðar einingar geta dregist aftur úr núverandi bókasöfnum í eiginleikum og hraða, svo að velja þær takmarkar stakk þinn á vegu sem skipta máli fyrir verkfræði. Komdu með lista yfir dulritunareiningarnar sem hvert eftirlitsskylt kerfi kallar í raun á, vottunarskírteinin sem dekka þær og sértæku skylduna (FIPS 140, CNSA eða geirareglu) sem gildir. Fyrir fyrirtækja- og opinber áætlun skaltu ákveða þetta áður en þú smíðar, því að bæta við vottuðum einingum og endurheimila kerfi eftir á er dýrt, hægt og þvingar oft endurhönnun íhlutanna sem þú hélst að væru búnir.

## Sjónarhorn eftir geirum

**Sprotafyrirtæki.** Hallaðu þér alfarið að sannreyndum sjálfgefnum gildum vettvangs þíns og eyddu engum verkfræðitíma í sérsmíðaða dulritun. Kveiktu á stýrðri dulkóðun í hvíld, lúktu TLS með sjálfvirkt endurnýjuðum skírteinum, kjötkássaðu lykilorð með staðlaðri hægri aðgerð og haltu leyndarmálum í leyndarmálastjóra vettvangsins frekar en hugbúnaðarsafninu. Eina hönnunarákvörðun þín er þunnt viðmót utan um fáa reiti sem þú dulkóðar í forritinu, svo framtíðarflutningur frá veitendastýrðum lyklum sé ekki endurskrift.

**Lítið fyrirtæki.** Þú hefur engan dulritunarfræðing og litla löngun til að reka HSM, svo keyptu vörslu frekar en að byggja hana: notaðu veitendastýrt KMS og leyndarmálastjóra sem fylgja skýinu þínu eða SaaS-verkfærum. Rammaðu verkið sem hreinlæti, það er, engir lyklar í kóða, dulkóðun kveikt alls staðar sjálfgefið og skírteinafyrningar vaktaðar svo ekkert renni út óvænt. Taktu viðskiptavinastýrða lykla frá fyrir fáu gögnin sem samningur eða eftirlitsaðili krefst þeirra raunverulega fyrir.

**Stórfyrirtæki.** Vandinn er stærð og samræmi yfir þúsundir þjónusta, skírteina og lykla. Reku miðlægt KMS með umslagsdulkóðun, sjálfvirknivæddu allan skírteinalífsferilinn svo engin fyrning sé handstýrð í höndunum og haltu einni dulritunarskrá sem nærir snúning, FIPS-umfang og skammtafræðiþolsáætlun. Aðgreindu lyklavörslu frá gagnaaðgangi sem skipulagsheildarvíða stýringu og gerðu dulkóðun að vettvangsgetu sem hvert teymi erfir frekar en verk sem hvert finnur upp aftur.

**Hið opinbera.** Innkaup, vottun og úttekt móta hvert val. Notaðu FIPS 140-vottaðar einingar og fylgdu landsleiðbeiningum eins og CNSA fyrir leynileg kerfi, bindu lyklavörslu við gagnaflokkun svo viðkvæmustu lyklarnir sitji hjá öryggisvottuðu starfsfólki undir ströngum aðskilnaði skyldna og framleiddu samfelld sönnunargögn um vottaða dulritun fyrir áframhaldandi heimild. Skjalfestu post-quantum flutningsáætlun fyrir skrár sem verða að haldast leynilegar í áratugi og krefstu þess að söluaðilar upplýsi hvaða einingar eru vottaðar áður en þú skuldbindur þig.

## Dæmi

**Sprotafyrirtæki.** Lítið teymi sem smíðar heilsurakningarforrit hallast alfarið að sannreyndum sjálfgefnum gildum. Þau loka TLS með sjálfvirkt endurnýjuðum skírteinum, kveikja á dulkóðun í hvíld á stýrða gagnagrunninum sínum og hlutageymslunni með KMS veitandans og kjötkássa lykilorð með hægri, saltaðri aðgerð úr stöðluðu bókasafni. Frekar en að skrifa nokkra dulritun sjálf nota þau háttsett auðkennt dulkóðunarkall fyrir eina reitinn sem þau verða að dulkóða í forritinu. Leyndarmál búa í leyndarmálastjóra vettvangsins, aldrei í hugbúnaðarsafninu. Það kostar fáa eftirmiðdaga og fjarlægir heilan flokk skelfilegra mistaka.

**Stórfyrirtæki.** Hnattrænn banki rekur miðlægt KMS og flota HSM, með dulritunarskrá sem rekur hvern lykil og skírteini yfir þúsundir þjónusta. Umslagsdulkóðun ver viðskiptavinagögn, með gagnalyklum umvöfðum meistaralyklum sem snúast á áætlun meðan gögnin haldast kyrr. Skírteinaútgáfa og endurnýjun eru fullsjálfvirk eftir að opinbert rekstrarrof kenndi þeim kostnað eins útrunnins skírteinis. Lyklastjórnendur eru sérstakt teymi frá forritaverkfræðingum, svo varsla framfylgir aðskilnaði skyldna, og dulritunarlipurðarlag leyfir þeim að byrja að tilraunakeyra skammtafræðiþolin reiknirit fyrir langlíf skjalasöfn.

**Hið opinbera.** Landsbundin stofnun sem meðhöndlar leynilegar skrár notar aðeins FIPS 140-vottaðar dulritunareiningar og fylgir CNSA-leiðbeiningum NSA fyrir kerfi með hæstu flokkun. Lyklar eru búnir til og haldnir í HSM sem sleppa aldrei skýrum lyklaefni, og varsla er bundin gagnaflokkun svo viðkvæmustu lyklarnir sitji hjá öryggisvottuðu starfsfólki undir ströngum aðskilnaði skyldna. Skírteini keyra á stýrðum innri PKI með sjálfvirkum lífsferlum og samfelld sönnunargögn um vottaða dulritun næra áframhaldandi heimild stofnunarinnar. Skjalfest post-quantum flutningsáætlun ver skrár sem verða að haldast leynilegar í áratugi.

## Viðskiptarök: hvatar, ávöxtun fjárfestingar og heildarkostnaður

Dulritun er enn eitt svið þar sem hófleg fjárfesting kemur í veg fyrir skelfilegt, fréttaverðugt tap. Heildareignarkostnaðurinn felur í sér KMS eða HSM, leyndarmála- og skírteinastjórnunarverkfæri og verkfræðitímann til að hanna lífsferla og halda skrá núgildandi. Þessi kostnaður er raunverulegur en afmarkaður. Kostnaðurinn við að sleppa honum er innbrot í ódulkóðuð gögn, margra klukkustunda rekstrarrof vegna útrunnins skírteinis eða óafturkræft gagnatap vegna misfarins lykils, hvert ber eftirlitssektir, tilkynningakostnað og varanlegan mannorðsskaða.

Sterkasta ávöxtunin kemur af sjálfvirkni og endurnýtingu. Sjálfvirkir skírteinalífsferlar útrýma algengasta sjálfskaðandi rekstrarrofinu. Miðlæg lyklastjórnun með skynsamlegum sjálfgefnum gildum þýðir að hver ný þjónusta erfir dulkóðun á ferð og í hvíld án fyrirhafnar á teymi, sem breytir dulritun úr endurteknum skatti í vettvangsgetu. Fyrir eftirlitsskylt og opinbert starf lækka vottaðar einingar og sjálfvirk sönnunargögn líka kostnað úttekta og heimildar. Þegar þú færir rök við forystu skaltu ramma það skýrt: reiknirit eru ókeypis og sönnuð, áhættan býr í lyklastjórnun og skírteinarekstri og lítil, sjálfvirk fjárfesting þar kemur í veg fyrir dýru bilanirnar.

## Andmynstur og gildrur

- **Að rúlla eigin dulritun.** Sérsmíðuð reiknirit eða handbyggðar samskiptareglur sem bila á lúmska, vegu sem aðeins sérfræðingar sjá.
- **Harðkóðaðir lyklar og leyndarmál.** Auðkennisgögn límd inn í frumkóða, stillingarskrár eða spjall, þar sem þau leka og ekki er hægt að snúa þeim.
- **Dulkóðun án lyklaaga.** Að kveikja á dulkóðun en skilja lyklaaðgang eftir galopinn eða snúa aldrei.
- **Að rugla kjötkássu saman við dulkóðun.** Að líta á kjötkássu sem afturkræfa, eða geyma lykilorð með hraðkjötkássa í stað hægs, saltaðs.
- **Skírteinahappdrætti.** Engin skrá, engin fyrningarvöktun og reglubundin óvænt rekstrarrof þegar skírteini rennur út.
- **Sameinuð lyklavarsla og gagnaaðgangur.** Eitt auðkenni sem getur bæði stýrt lykli og lesið gögnin sem hann ver.
- **Engin snúningsáætlun.** Lyklar sem hafa aldrei verið snúnir og ekki er hægt að snúa fljótt undir þrýstingi.
- **Dulritun án lipurðar.** Reiknirit tengd svo djúpt að skipti krefjast endurskriftar, sem hindrar hvern framtíðarflutning.
- **Að hunsa vottunarkröfur.** Að nota sterk reiknirit í óvottuðum einingum þar sem FIPS eða sambærileg vottun er krafist.

## Þroskalíkan

- **Stig 1, Upphaf:** Dulkóðun er ósamræmd og oft fjarverandi, beitt viðbragðsdrifið þegar einhver tekur eftir bili. Lyklar og leyndarmál eru harðkóðuð eða sameiginleg óformlega yfir spjall og stillingarskrár. Engin skrá, enginn snúningur og skírteini renna út óvænt, og teymi skrifa stundum eigin dulritun.
- **Stig 2, Þróun:** TLS og dulkóðun í hvíld eru kveikt fyrir helstu kerfi og KMS eða leyndarmálastjóri er til, en upptaka er ójöfn og mismunandi eftir teymum. Sum skírteini eru vöktuð á meðan önnur eru það ekki, snúningur er handvirkur og sjaldgæfur og engin fullkomin dulritunarskrá bindur það saman.
- **Stig 3, Stöðlun:** Dulkóðun á ferð og í hvíld er skjalfesta sjálfgefið framfylgt um alla skipulagsheildina. Lyklar búa í KMS með tímasettum snúningi og umslagsdulkóðun, lyklavarsla er aðgreind frá gagnaaðgangi, skírteinalífsferlar eru sjálfvirkir, dulritunarskrá er viðhaldið og vottaðar einingar eru notaðar hvar sem regluverk krefst þeirra.
- **Stig 4, Stjórnun:** Dulritunarbúið er mælt og stýrt gegn grunnlínum. Þú rekur fyrirvara skírteinafyrninga, hlutfall lykla snúinna á áætlun, meðaltíma til að afturkalla brotinn lykil, greiningar á leyndarmálum í kóða á tímabil og skráarþekju og rýnir þessa mælikvarða gegn markmiðum. Snúningur og afturköllun eru æfð á takti með skráðum tímasetningum og frávik kalla fram úrbætur frekar en að fara óséð.
- **Stig 5, Samhæfing:** Dulritun er vettvangsgeta sem hver þjónusta erfir sjálfgefið og hún er stöðugt bætt og samþætt um skipulagsheildina. Snúningur og afturköllun eru hröð og rútínulega æfð, HSM vernda lykla með hæstu tryggingu og dulritunarlipurð auk virkrar post-quantum flutningsáætlunar halda búinu aðlögunarhæfu eftir því sem reiknirit og skyldur breytast. Regluvörslusönnunargögn eru framleidd sjálfvirkt og næra áframhaldandi heimild.

## Hugmyndir til umræðu

1. Hvaða kerfi í búinu þínu réttlæta viðskiptavinastýrða lykla eða HSM miðað við rekstrarkostnað þeirra og skelfilega taps áhættu?
2. Hvernig myndirðu byggja og viðhalda einni sannleiksuppsprettu fyrir hvern lykil og skírteini sem þú átt?
3. Hver er raunhæfur tími þinn til að snúa brotnum lykli í dag og hvað gerir hann hægan?
4. Hvar gerir arkitektúr þinn erfitt að skipta um dulritunarreiknirit og hvernig myndirðu laga það fyrir þvingaðan flutning?
5. Hver af langlífum leyndarmálum þínum myndu skipta máli ef andstæðingur safnaði þeim núna og afkóðaði árum síðar?
6. Enda leyndarmál og lyklar nokkurn tíma í kóða, stillingu eða skrám og hvernig myndirðu vita það?

## Helstu atriði

- **Finndu ekki upp eigin dulritun.** Notaðu sannreynd bókasöfn og staðlað reiknirit á hæsta örugga ágripunarstigi.
- **Reiknirit eru auðveld. Lyklastjórnun er erfið.** Líftími lykils (myndun, dreifing, snúningur, afturköllun, eyðing) er þar sem raunverulegar bilanir búa.
- **Vittu tryggingar þínar:** samhverf og opinberlykla dulkóðun vernda trúnað, undirskriftir sanna áreiðanleika og heilleika og kjötkássa greinir fikt en er ekki dulkóðun.
- **Dulkóðaðu á ferð með núverandi TLS og í hvíld með umslagsdulkóðun**, sem sjálfgefið fyrir hvert kerfi.
- **Aðgreindu lyklavörslu frá gagnaaðgangi**, notaðu KMS fyrir lykla og leyndarmálastjóra fyrir auðkennisgögn og harðkóðaðu hvorugt.
- **Sjálfvirknivæddu skírteinalífsferla** til að drepa óvæntu fyrningarrekstrarrofið og haltu dulritunarskrá.
- **Byggðu fyrir dulritunarlipurð** og hafðu post-quantum flutningsáætlun fyrir langlíf leyndarmál.
- **Kjóstu vottaðar útfærslur** (FIPS 140 og viðeigandi landsleiðbeiningar) þar sem regluverk eða flokkun krefst þeirra.

## Heimildir og frekari lestur

- National Institute of Standards and Technology, *FIPS 140-3: Security Requirements for Cryptographic Modules*.
- National Institute of Standards and Technology, *SP 800-57: Recommendation for Key Management*.
- National Institute of Standards and Technology, *SP 800-131A: Transitioning the Use of Cryptographic Algorithms and Key Lengths*.
- National Institute of Standards and Technology, post-quantum cryptography standards (FIPS 203, 204, and 205).
- Niels Ferguson, Bruce Schneier, and Tadayoshi Kohno, *Cryptography Engineering*.
- Jean-Philippe Aumasson, *Serious Cryptography*.
- David Wong, *Real-World Cryptography*.
- Internet Engineering Task Force, *RFC 8446: The Transport Layer Security (TLS) Protocol Version 1.3*.
- Open Web Application Security Project, *Cryptographic Storage Cheat Sheet* and *Transport Layer Protection Cheat Sheet*.
- National Security Agency, *Commercial National Security Algorithm (CNSA) Suite* guidance.
