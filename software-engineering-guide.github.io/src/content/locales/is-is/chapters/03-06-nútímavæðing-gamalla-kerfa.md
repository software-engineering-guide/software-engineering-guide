# 3.6 Nútímavæðing eldri kerfa

## Yfirlit og tilgangur

[Eldri kerfi](https://en.wikipedia.org/wiki/Legacy_system) eru kerfin sem reka heiminn. Kjarnahöfuðbækur banka, skatta- og bótavélar, flugumferðar- og varnarkerfi, iðgjaldaumsýsla trygginga og opinberar skrár sem samfélög reiða sig á eru oft áratuga gömul. Mörg eru skrifuð í [COBOL](https://en.wikipedia.org/wiki/COBOL) (Common Business-Oriented Language) eða annarri eldri tækni og þau vinna enn meirihluta mikilvægra færslna. „Eldri“ er ekki móðgun. Það þýðir að kerfið er nógu verðmætt til að hafa lifað af, nógu mikilvægt til að bilun sé skelfileg og nógu gamalt til að erfitt sé að breyta því örugglega. Nútímavæðing eldri kerfa er sú grein að bæta, flytja eða skipta út þessum kerfum án þess að rjúfa nauðsynlega þjónustu sem þau veita.

Þetta er hlutfallslega mest vandi fyrirtækja og hins opinbera og þar verða stærstu, opinberustu upplýsingatæknibilanirnar. Gríðarlegur hluti mikilvægra færslna um allan heim snertir enn [stórtölvukerfi](https://en.wikipedia.org/wiki/Mainframe_computer). Stór hluti framleiðslukóða í stórum stofnunum er á eldri málum sem öldrandi og minnkandi hópur sérfræðinga viðheldur. Ríkisstjórnir bera þyngstu byrðina: lögbundnar skyldur kóðaðar yfir áratugi, innkaupa- og fjárhagsáætlunarlotur sem lifa lengur en ríkisstjórnir og borgaraþjónustu sem má ekki trufla. Ráðandi áhættan er ekki að kerfin séu gömul, því mörg ganga frábærlega. Hún er að þekkingin til að viðhalda þeim er að hverfa á eftirlaun, vettvangarnir verða sífellt dýrari og takmarkaðri og freistingin að „endurskrifa bara allt“ leiðir til sumra dýrustu bilana í sögu greinarinnar.

Þessi kafli fjallar um stigvaxandi nútímavæðingarmynstrin sem virka í raun (kyrkingarfíku og útibú-með-ágripun), hvernig á að meta og forgangsraða áhættu eldri kerfa, ráðsmennsku stórtölvu- og COBOL-búa, aga [gagnaflutnings](https://en.wikipedia.org/wiki/Data_migration) og tvíkeyrslu og umfram allt hvernig á að standa gegn freistingu stóru endurskriftarinnar. Meginsannfæringin er að árangursrík nútímavæðing er nánast alltaf stigvaxandi, sönnunargagnadrifin og skilar stöðugt verðmæti. Hún er aldrei margra ára stórhvellur.

## Meginreglur

- **Eldra þýðir verðmætt og grundvallandi, ekki bara gamalt.** Berðu virðingu fyrir því sem kerfið gerir áður en þú snertir það. Það kóðar áratuga erfiðlega áunnar viðskiptareglur.
- **Stigvaxandi slær stórhvell, nánast alltaf.** Skiptu út bita fyrir bita á bak við stöðugt viðmót, skilaðu verðmæti samfellt og hafðu áhættu litla.
- **Stóra endurskriftin er sjálfgefin bilunarháttur.** Fullar endurskriftir fara rútínulega fram úr, skila of litlu og er hætt við. Líttu á hvötina með djúpri tortryggni.
- **Þú getur ekki nútímavætt það sem þú skilur ekki.** [Greindu með öfugri verkfræði](https://en.wikipedia.org/wiki/Reverse_engineering) og skjalfestu hegðun (þar á meðal óskjalfestar reglur) áður en þú skiptir henni út.
- **Gagnaflutningur er þar sem verkefni deyja.** Gögnin eru eldri, skítugri og flæktari en nokkur býst við. Skipuleggðu þau sem fyrsta flokks átak.
- **Keyrðu gamalt og nýtt samsíða til að byggja upp traust.** Tvíkeyrsla og samanburður grípa misræmi fyrir yfirfærslu.
- **Forgangsraðaðu eftir áhættu og verðmæti, ekki aldri.** Nútímavæddu það sem er áhættusamast og verðmætast fyrst, ekki það sem er einfaldlega elst.
- **Haltu ljósunum kveiktum meðan þú skiptir um vélina.** Þjónustan verður að halda áfram að ganga allan tímann. Enginn niðurtími er ásættanlegur fyrir mikilvæg borgara- eða fjárhagskerfi.

## Ráðleggingar

### Nútímavæddu stigvaxandi með kyrkingarfíkumynstrinu

**Kyrkingarfíkjan** (nefnd eftir vínviðnum sem vex umhverfis tré og kemur smám saman í staðinn fyrir það) er vinnuhesturinn í öruggri nútímavæðingu. Settu leiðsagnarlag (API-gátt, framhlið eða milliþjón) fyrir framan eldra kerfið. Smíðaðu síðan, getu fyrir getu, afleysinguna í nútímakerfi og beindu þeirri sneið umferðar þangað og láttu afganginn vera á eldra kerfinu. Með tímanum vex nýja kerfið og það gamla minnkar, þar til hægt er að leggja það niður. Þetta skilar verðmæti samfellt, heldur hverri breytingu lítilli og afturkræfri, forðast áhættusama yfirfærslu og leyfir þér að stöðva eða endurforgangsraða hvenær sem er. Það er andstæða stórhvellsins. Eldra kerfið heldur áfram að ganga og vinna fyrir sér meðan þú skiptir því út í kringum það.

### Notaðu útibú-með-ágripun fyrir innri samskeyti

Þar sem þú þarft að skipta út íhlut sem margir hlutar kerfisins reiða sig á skaltu nota **útibú-með-ágripun** (branch-by-abstraction). Kynntu ágripunarlag (viðmót) yfir núverandi útfærslu, fluttu kallendur til að reiða sig á ágripunina, smíðaðu nýju útfærsluna á bak við sömu ágripun, skiptu yfir (oft á bak við [eiginleikarofa](https://en.wikipedia.org/wiki/Feature_toggle), smám saman) og fjarlægðu loks gömlu útfærsluna. Þetta leyfir að skipta út stórum íhlut stigvaxandi á aðalþróunarlínunni án langlífs útibús, sem heldur kerfinu útgáfuhæfu allan tímann. Það parast eðlilega við kyrkingarfíkuna: framhliðin sér um ytri samskeyti, útibú-með-ágripun um innri.

### Metðu og forgangsraðaðu áhættu eldri kerfa af ásetningi

Áður en þú nútímavæðir skaltu byggja skýra, hreinskilna skrá og áhættumat yfir búið. Gefðu hverju kerfi einkunn fyrir viðskiptamikilvægi, tæknilega áhættu (úreldingu, óstudda vettvanga, öryggisútsetningu), breytingatíðni og, afgerandi, **þekkingaráhættu** (hve margir geta enn viðhaldið því og hve nálægt eftirlaunum þeir eru). Teiknaðu kerfin á áhættu-á-móti-verðmæti rist. Forgangsraðaðu að nútímavæða það sem er bæði áhættusamt og verðmætt. Íhugaðu að láta stöðug, lítið breytt, vel skilin kerfi í friði jafnvel þótt þau séu gömul, því virkt kerfi sem enginn þarf að breyta er ekki neyðartilvik. Þetta mat breytir „allt er gamalt og ógnvekjandi“ í rökstuddan, raðaðan vegvísi.

### Sinntu ráðsmennsku stórtölvu- og COBOL-búsins, ekki bara endurnýjun

Ekki ætti, eða er hægt, að skipta út öllum stórtölvu- eða COBOL-kerfum fljótlega og örugglega. Forgangur til skamms tíma er oft **ráðsmennska**: fangaðu þekkinguna áður en hún fer á eftirlaun. Skjalfestu viðskiptareglurnar sem kóðinn kóðar (mikið af því er óskjalfest og óbætanlegt), fjárfestu í sjálfvirkum prófum sem festa núverandi hegðun svo framtíðarbreyting sé örugg, ráðu og þjálfaðu viðhaldsaðila þvert á svið og nútímavæddu umlykjandi afhendingarvinnubrögð (frumkóðastýringu, [samfellda samþættingu](https://en.wikipedia.org/wiki/Continuous_integration) (CI), sjálfvirkar prófanir) jafnvel meðan kjarninn helst á sínum stað. Þar sem þú nútímavæðir skaltu kjósa að afhjúpa eldri getu gegnum nútíma API (innhjúpun) sem fyrsta skref. Meðhöndlaðu sjálfvirka þýðingu COBOL yfir í nútímamál með varúð, því hún framleiðir kóða sem keyrir en endurskapar oft trúlega óskiljanlega rökfræði. Knappasta auðlindin er skilningur, ekki reikniafl.

### Líttu á gagnaflutning og tvíkeyrslu sem kjarna verkefnisins

Erfiðasti og áhættusamasti hluti flestra nútímavæðingarátaka eru **gögnin**. Þau eru mikil að umfangi, léleg og ósamræmd að gæðum og full af óskjalfestri merkingu sem hefur safnast upp yfir áratugi. Sniðgreindu og hreinsaðu þau, varpaðu gömlum skemum á ný skýrt og byggðu endurtakanlegan, sjálfvirkan flutning með fullri afstemmingu (talningar, prófsummur, viðskiptaheildir) svo þú getir sannað að ekkert tapaðist eða breyttist. Dragðu úr áhættu yfirfærslu með **tvíkeyrslu** (samsíða keyrslu): rektu gömlu og nýju kerfin hlið við hlið á sömu inntökum og berðu saman úttök þar til nýja kerfið samsvarar því gamla að öryggismörkum þínum. Færðu þig yfir fyrst þá, og haltu getunni til að afturkalla. Fyrir raunverulega mikilvæg kerfi skaltu flytja og færa yfir í sneiðum frekar en allt í einu.

### Stýrðu freistingu stóru endurskriftarinnar

Eðlishvötin til að henda draslkennda gamla kerfinu og smíða hreint nýtt frá grunni er sterk og hún er nánast alltaf röng fyrir stór, mikilvæg kerfi. Fullar endurskriftir vanmeta verðmætið sem felst í „ljóta“ kóðanum (jaðartilvik, regluverksreglur, villusamhæfð hegðun sem raunverulegir notendur reiða sig á), taka mun lengri tíma en spáð var, skila ekki verðmæti fyrr en í lokin og er oft hætt við eftir gríðarleg útgjöld. Hafðu stigvaxandi nútímavæðingu sem sjálfgefið. Taktu endurskriftir frá fyrir tilvik þar sem vettvangurinn er raunverulega ósjálfbær og stigvaxandi leiðir eru tæmdar. Jafnvel þá skaltu sundurliða endurskriftina í sjálfstætt afhendanlega bita með kyrkingarmynstrinu frekar en eina stórhvellsútgáfu. Þegar forysta þrýstir á algjöra endurskrift skaltu krefjast spurningarinnar: hvaða verðmæti kemur út á fyrstu þremur mánuðunum og hvað gerist ef áætluninni er hætt miðja vegu?

## Málamiðlanir: kostir og gallar

| Nálgun | Kostir | Gallar |
|---|---|---|
| Kyrkingarfíka (stigvaxandi) | Samfellt verðmæti, lítil áhætta, afturkræft, heldur þjónustu gangandi | Lengri heildartímalína, þarf að reka tvö kerfi samsíða, samþættingarkostnaður |
| Stórhvellsendurskrift | Hrein byrjun, engar eldri skorður í nýja kóðanum | Mjög hátt bilanahlutfall, ekkert verðmæti fyrr en í lokin, gríðarlegur kostnaður, viðskiptareglur tapast |
| Innhjúpun (vefja með API) | Hröð, lítil áhætta, nútímavæðir aðgang án þess að snerta kjarnann | Kjarninn helst eldri. Frestar undirliggjandi áhættu, leysir hana ekki |
| Láta vera eins og er (ráðsmennska) | Engin verkefnisáhætta, ódýrast til skamms tíma | Þekkingar- og vettvangsáhætta safnast áfram, að lokum þvinguð aðgerð |

Grundvallarmálamiðlunin er hraði umbreytingar gegn hættu á bilun, og nútímavæðing eldri kerfa er sviðið þar sem þessi skipti eru skekktust. „Hraða, hreina“ stórhvellsendurskriftin er tálsýn sem framleiðir ítrekað hægustu og dýrustu niðurstöðuna af öllum: aflýsta áætlun og enn ónútímavætt kerfi. Stigvaxandi nálganir virðast hægari og krefjast þess að reka tvö kerfi samsíða, en þær skila verðmæti allan tímann, halda áhættu lítilli og afturkræfri og eru reynslusannað áreiðanlega leiðin. Raunverulega dómgreindarákvörðunin er milli þess að sinna ráðsmennsku stöðugs eldra kerfis aðeins lengur og að hefja stigvaxandi afleysingu núna. Láttu áhættuferil ráða þeirri ákvörðun, sérstaklega þekkingaráhættu, frekar en óþægindi gagnvart gamalli tækni.

## Spurningar til að ræða með teyminu

1. **Hafið þið stað til að setja leiðsagnarlag fyrir framan eldra kerfið ykkar og ef ekki, hvað þyrfti til að búa til slíkan?** Kyrkingarfíkjan byggir á samskeyti: API-gátt, framhlið eða milliþjóni sem þú getur beint einni getu í einu á nýja útfærslu. Mörg gömul kerfi hafa ekkert slíkt samskeyti, svo fyrsti nútímavæðingaráfanginn er oft einfaldlega að smíða hlerunarpunktinn og sú vinna er auðvelt að vanmeta. Komdu með núverandi samþættingarkort og spyrðu hvar umferð mætti hlera fyrir hverja getu án stórhvellsyfirfærslu. Ef hvergi er hægt gæti útibú-með-ágripun á innra samskeyti verið upphafshreyfingin í staðinn. Án leiðsagnarlags hefurðu enga stigvaxandi leið, sem er nákvæmlega hvernig skipulagsheildir eru ýttar aftur í átt að endurskriftinni sem venjulega mistekst.

2. **Hafið þið í raun teiknað búið ykkar á áhættu-á-móti-verðmæti rist, eða er vegvísir ykkar knúinn af því hvaða kerfi virðist elst?** Kaflinn krefst þess að þú nútímavæðir það sem er áhættusamt og verðmætt fyrst, og lætur vísvitandi stöðug, lítið breytt, vel skilin kerfi í friði jafnvel þótt þau séu ævaforn. Án skýrrar ristar flæðir athygli að háværustu kvörtuninni eða minnst smart tækninni, og raunverulegar tímasprengjur (mikilvægt kerfi með tvo viðhaldsaðila nærri eftirlaunum) bíða. Gefðu hverju kerfi einkunn fyrir viðskiptamikilvægi, tæknilega áhættu, breytingatíðni og þekkingaráhættu, raðaðu síðan frá efra hægra horninu. Komdu með þá rist á fundinn sem sameiginlega kortið. Þekkingaráhætta verðskuldar þyngsta vægið, því hún er eina inntakið sem aðeins versnar og er ekki hægt að kaupa til baka þegar fólkið fer.

3. **Þegar þið færið yfir, hvernig sannið þið að ekki ein einasta skrá tapaðist eða breyttist og hver staðfestir þau sönnunargögn?** Gagnaflutningur er þar sem þessi verkefni deyja og traust kemur frá afstemmingu: línutalningum, prófsummum og viðskiptaeftirlitsheildum sem passa milli gamla og nýja, auk tvíkeyrslu sem ber saman úttök á sömu inntökum þar til þau eru sammála að háum þröskuldi. Fyrir bóta- eða höfuðbókarkerfi er misræmi borgari sem fær of lítið greitt eða króna sem tapast, svo sönnunargögnin verða að fullnægja endurskoðanda, ekki bara verkfræðingi. Ákveddu núna hvaða heildir þið afstemmið, hvaða öryggisþröskuldur kallar fram yfirfærslu og hve lengi þið keyrið gamalt og nýtt samsíða. Haltu afturköllun tiltækri allan tímann og færðu yfir í sneiðum frekar en allt í einu. Misræmið sem þið finnið við tvíkeyrslu eru yfirleitt óskjalfestar eldri reglur sem þið verðið að varðveita, svo líttu á hvert sem uppgötvun, ekki bara galla.

4. **Hvaða eldri kerfum sinnið þið með ráðsmennsku á móti að skipta virkt út og hver ákvað hvað er hvað?** Kaflinn dregur vísvitandi línu milli kerfa sem vert er að stöðuga á staðnum (skjalfesta reglur, bæta við einkennaprófum, þjálfa viðhaldsaðila þvert á svið) og kerfa sem vert er að skipta út stigvaxandi, og þetta tvennt krefst mjög ólíkrar fjármögnunar og mönnunar. Fyrir stóra skipulagsheild er hættan rek: kerfi merkt „ráðsmennska í bili“ verður hljóðlega „ráðsmennska að eilífu“ þar til síðasti viðhaldsaðilinn fer á eftirlaun og valið er tekið fyrir ykkur í kreppu. Sjónarmiðin sem togast á eru ráðsmennskukostnaður og vettvangsúreldi öðrum megin gegn áhættu og truflun afleysingar hinum megin, og þekkingaráhætta ætti að ráða úrslitum því hún versnar aðeins. Komdu með áhættu-á-móti-verðmæti ristina, fjölda viðhaldsaðila og eftirlaunasjóndeildarhring fyrir hvert kerfi og skýran eiganda ráðsmennsku-eða-afleysingarákvörðunarinnar. Í eignasöfnum fyrirtækja og hins opinbera skaltu nefna rýnitakt og ábyrgan embættismann fyrir hvert kerfi, því flokkun sem enginn endurskoðar er ákvörðun sem enginn tekur.

5. **Þegar forysta biður um fulla endurskrift, hvert er fasta svarið ykkar og getið þið sýnt hvað stigvaxandi leið skilar á fyrstu þremur mánuðunum?** Stórhvellsendurskriftin er sjálfgefinn bilunarháttur, samt fær hún stöðugt fjármögnun því hrein byrjun er auðveld í sölu en kyrkingarfíka ekki. Stórt teymi þarf æfð viðbrögð svo rökin vinnist á sönnunargögnum en ekki á því hver er æðstur í herberginu. Raunverulega spennan er að sumir vettvangar eru raunverulega ósjálfbærir og endurskrift er réttlætanleg, svo svarið getur ekki verið altæk neitun: það verður að vega hvort stigvaxandi samskeyti eru enn til gegn raunkostnaði þess að halda gamla vettvanginum á lífi. Komdu með verðmætin sem fyrsti stigvaxandi áfangi myndi skila, söguleg bilanahlutföll sambærilegra endurskrifta og sundurliðun hverrar fyrirhugaðrar endurskriftar í sjálfstætt afhendanlega bita. Hjá hinu opinbera, þar sem aflýst margra ára áætlun brennir almannafé í fullri sýn, skaltu krefjast þess að sérhver endurskrift skili verðmæti snemma og lifi af að vera stöðvuð miðja vegu án algjörs taps.

6. **Hvernig munuð þið fanga viðskiptareglurnar sem eru læstar í elsta kóðanum ykkar áður en fólkið sem skilur þær er farið?** Mikið af verðmæti eldra kerfis er óskjalfest hegðun sem áratuga jaðartilvik, reglugerðir og villusamhæfðar lagfæringar hafa safnað, og hún lifir í minnkandi hópi sérfræðinga á eftirlaunum frekar en í nokkurri skriflegri skrá. Fyrir stóra skipulagsheild er þetta eina áhættan sem ekki er hægt að kaupa til baka þegar fólkið fer, svo hún verðskuldar fjármögnun á undan sýnilegri vettvangsvinnu. Togið á móti er að þekkingarfanga (skjölun, einkennapróf, öfug verkfræði, þjálfun þvert á svið) finnst eins og kostnaður sem skilar engu, sem er einmitt ástæðan fyrir því að honum er frestað. Komdu með skrá yfir hverjir halda mikilvægri þekkingu, hve nærri þeir eru brottför og hvaða prófaþekja festir núverandi hegðun í dag. Í eftirlitsskyldu og opinberu umhverfi skaltu líta á lögbundnu reglurnar sem kóðaðar eru í gömlum kóða sem regluvörslueign: að missa þær hljóðlega er ekki tæknileg skuld, það er lagaleg útsetning.

## Sjónarhorn eftir geirum

**Sprotafyrirtæki.** Eldra kerfið þitt er þitt eigið hrattsmíðaða MVP, ekki stórtölva: frumgerð sem nú ber tekjur og allir óttast að snerta. Ekki endurskrifa hana. Vefðu ógnvænlegustu eininguna á bak við hreint viðmót, bættu við einkennaprófum til að festa hegðun hennar og dragðu virkni út stigvaxandi svo hver lítil útgáfa skili verðmæti og minnki áhættu. Þú hefur engan tíma til endurbyggingar frá grunni, svo valkostir skipta meira máli en glæsileiki.

**Lítið fyrirtæki.** Þú hefur ekkert nútímavæðingarteymi og þröngt fjárhagsáætlun, svo hagnýta hreyfingin er yfirleitt að halda virku kerfi virku: fangaðu það sem sá eini sem skilur það veit, komdu því í frumkóðastýringu með fáeinum sjálfvirkum prófum og hallaðu þér að söluaðila eða pakkaðri vöru frekar en sérsmíðaðri endurbyggingu. Rammaðu ákvörðunina sem kaupa á móti smíða og kjóstu að kaupa þegar getan er hrávara. Eyddu takmarkaðri fyrirhöfn í eina kerfið sem bilun í myndi stöðva reksturinn, ekki það sem einfaldlega lítur út fyrir að vera elst.

**Stórfyrirtæki.** Vandinn er eignasafnsstærð: tugir kerfa, mörg teymi og þekkingaráhætta yfir allt búið. Keyrðu sameiginlegt áhættu-á-móti-verðmæti mat, staðlaðu stigvaxandi mynstur (kyrkingarfíku og útibú-með-ágripun) og líttu á gagnaflutning og tvíkeyrslu sem fyrsta flokks greinar með afstemmingu sem allir treysta. Stýrðu nútímavæðingu sem samfelldu eignasafni gegn áhættuferli frekar en dreifingu hetjulegra verkefna og fjárhagsáætlaðu ráðsmennsku og þekkingarfanganingu skýrt svo ekkert mikilvægt kerfi reiði sig á einn viðhaldsaðila á leið á eftirlaun.

**Hið opinbera.** Lögbundnar skyldur kóðaðar yfir áratugi, innkaupareglur og borgaraþjónusta sem má ekki trufla gera stórhvellsafleysingu sérstaklega hættulega. Kjóstu stigvaxandi kyrkingarfíkuflutning með yfirfærslu sneið fyrir sneið, sannaðu með afstemmingu og langri samsíða keyrslu að ekki ein borgaraskrá tapaðist eða var rangt reiknuð og haltu afturköllun tiltækri allan tímann. Innkaup ættu að krefjast gagnaflytjanleika og upplýsingagjafar um viðskiptareglur frekar en ógagnsærrar þýðingar, og hver margra ára áætlun verður að skila úttektarhæfu verðmæti snemma og standast opinbera athugun ef henni er hætt miðja vegu.

## Dæmi

**Sprotafyrirtæki.** Upprunalega MVP þriggja ára sprotafyrirtækis er orðið sinnar tegundar eldra kerfi: flýtt frumgerð sem nú vinnur raunverulegar tekjur og allir eru hræddir við að snerta. Í stað endurskriftar vefur teymið versta eininguna á bak við hreint viðmót, bætir við einkennaprófum til að festa núverandi hegðun hennar og flytur virkni út úr henni bita fyrir bita á nokkrum mánuðum. Hver lítil útgáfa skilar verðmæti og minnkar ógnvænlega hlutann, svo sprotafyrirtækið fær viðhaldanlegt kerfi án þess að veðja fyrirtækinu á endurbyggingu frá grunni sem það hefur ekki efni á.

**Stórfyrirtæki.** Stórt tryggingafélag rekur iðgjaldaumsýslu á stórtölvu-COBOL-kerfi sem er áreiðanlegt en dýrt að breyta og er viðhaldið af handfylli verkfræðinga nærri eftirlaunum. Í stað endurskriftar vefur tryggingafélagið stórtölvuna með nútíma API og beitir kyrkingarfíkunni: ný tilboðs-og-kaupa- og sjálfsafgreiðslugeta er smíðuð á nútímavettvangi og leidd gegnum framhlið, á meðan kjarnaskrár vátrygginga haldast á stórtölvunni. Samhliða skjalfestir teymið viðskiptareglur og bætir [einkennaprófum](https://en.wikipedia.org/wiki/Characterization_test) við kringum COBOL-kóðann. Á nokkrum árum flyst getan eftir getu af stórtölvunni, hver útgáfa skilar verðmæti, þar til hægt er að leggja niður kjarnann sem eftir er á forsendum tryggingafélagsins en ekki í kreppu.

**Hið opinbera.** Almannatryggingastofnun verður að nútímavæða áratuga gamalt bótaútreikningskerfi sem greiðir milljónum borgara og má hvorki trufla né greiða rangt. Hún hafnar stórhvellsafleysingu eftir að hafa rannsakað sambærilegar misheppnaðar áætlanir. Þess í stað sniðgreinir hún og hreinsar gögnin, smíðar sjálfvirkan flutning með fullri afstemmingu gegn eftirlitsheildum og keyrir nýju bótavélina samsíða þeirri gömlu í marga mánuði, gefur báðum sömu umsóknir og ber saman hvern útreikning, rannsakar hvert misræmi (sem leiðir oft í ljós óskjalfestar eldri reglur sem verður að varðveita). Aðeins þegar nýja kerfið samsvarar því gamla með mjög háu öryggi færir hún yfir bótategund fyrir bótategund, með afturköllun tiltæka allan tímann. Kyrkingarframhliðin lætur borgara sjá eina samfellda þjónustu gegnum umskiptin.

## Viðskiptarök: hvatar, ávöxtun fjárfestingar og heildarkostnaður

Nútímavæðing eldri kerfa hefur óvenjuleg viðskiptarök, því stærsti kostnaðurinn er oft kostnaður *aðgerðaleysis* og stærsta áhættan er nútímavæðingarverkefnið sjálft. Vaxandi kostnaður við að nútímavæða ekki er áþreifanlegur: hækkandi viðhald og leyfisgjöld á úreltum vettvöngum, sífellt knappara og dýrara sérfræðingavinnuafl, geta ekki mætt nýjum regluverks- eða þjónustukröfum hratt og vaxandi útsetning fyrir skelfilegri bilun þegar enginn er eftir sem skilur kerfið. Á móti því er kostnaður nútímavæðingar hár og framkvæmd sem stórhvellur ber raunverulega mikla líkindi á bilun. Það er einmitt þess vegna sem stigvaxandi nálgun skiptir máli fyrir ávöxtun fjárfestingar: hún breytir einu stóru veðmáli í röð smárra sem hvert skilar verðmæti og er hægt að stöðva.

Færðu rökin til forystu með því að endurramma valið. Spurningin er ekki „nútímavæða eða ekki“. Hún er „nútímavæða stigvaxandi núna, eða borga vaxandi ráðsmennskukostnað og horfast í augu við þvingaða, áhættusamari nútímavæðingu síðar í kreppu“. Magnsettu heildareignarkostnað óbreytts ástands (vettvangs- og leyfiskostnað, álagið fyrir knappa færni, áhættuvegins kostnað óendurheimtanlegs rekstrarrofs) og berðu saman við þrepaða áætlun sem minnkar áhættu og kostnað með hverjum áfanga meðan þjónustan heldur áfram að ganga. Umfram allt skaltu krefjast þess að hver fyrirhuguð endurskrift sé uppbyggð til að skila verðmæti snemma og oft. Áætlun sem skilar engu í þrjú ár og er hægt að aflýsa með algjöru tapi er ekki fjárfesting. Hún er fjárhættuspil. Sterkustu ávöxtunarrökin fyrir kyrkingarnálguninni eru valkostir: verðmæti kemur samfellt og skipulagsheildin getur breytt um stefnu hvenær sem er.

## Andmynstur og gildrur

- **Stórhvellsendurskriftin.** Margra ára allt-eða-ekkert afleysing sem skilar engu verðmæti fyrr en í lokin og er oft aflýst með miklum kostnaði.
- **Endurskrift án skilnings.** Að skipta út kóða þar sem viðskiptareglur voru aldrei skjalfestar og sleppa hljóðlega jaðartilvikum sem raunverulegir notendur og lög reiða sig á.
- **Vanmat á gögnunum.** Að meðhöndla gagnaflutning sem eftirþanka þegar hann er erfiðasti og áhættusamasti hluti verkefnisins.
- **Að sleppa tvíkeyrslu.** Að færa yfir á nýja kerfið án samsíða samanburðar og uppgötva misræmi aðeins eftir að það hefur áhrif á raunverulegt fólk.
- **Sjálfvirk þýðing sem lausn.** Að vélþýða COBOL yfir í nútímamál og trúa að verkinu sé lokið, sem framleiðir óskiljanlegan kóða sem endurskapar gömlu rökfræðina orðrétt.
- **Nútímavæðing eftir aldri, ekki áhættu.** Að eyða fyrirhöfn í gömul en stöðug kerfi á meðan áhættusöm, mikið breytt kerfi bíða.
- **Að missa þekkinguna.** Að láta síðustu viðhaldsaðilana fara á eftirlaun án þess að fanga viðskiptareglurnar og bæta við einkennaprófum.
- **Engin afturköllun.** Að færa yfir án leiðar til baka þegar nýja kerfið hegðar sér illa undir raunverulegu álagi og raunverulegum gögnum.

## Þroskalíkan

- **Stig 1: Upphaf.** Eldri kerfi eru óttast og fryst. Breytingum er forðast. Engin skrá eða áhættumat er til. Nútímavæðing, þegar hún er reynd yfirleitt, er ad hoc allt-eða-ekkert endurskrift knúin af gremju. Þekking býr í fáum höfðum á eftirlaunum án nokkurs skriflegs.
- **Stig 2: Þróun.** Sum teymi hafa skrá og grófa tilfinningu fyrir áhættu og nokkur eldri kerfi eru vafin með API fyrir aðgang. Stigvaxandi mynstur eru þekkt en beitt ójafnt og hugsunin rekur enn í átt að stórhvellsendurskriftum. Gagnaflutningur er reyndur en vanmetinn og vinnubrögð eru mjög mismunandi frá teymi til teymis.
- **Stig 3: Stöðlun.** Kerfi eru forgangsraðað eftir áhættu og verðmæti samkvæmt skjalfestri aðferð fyrir alla skipulagsheildina. Stigvaxandi mynstur (kyrkingarfíka, útibú-með-ágripun) eru framfylgd sjálfgefin og hver nútímavæðing fylgir stöðluðum leikbók. Gagnaflutningur er skipulagt, afstemmt átak með tvíkeyrslu fyrir yfirfærslu, og þekkingarfanganing og einkennapróf eru krafist vinnubrögð frekar en valkvæð.
- **Stig 4: Stjórnun.** Nútímavæðing er mæld og stýrð með gögnum. Búið ber grunnlínur: fjölda viðhaldsaðila og eftirlaunasjóndeildarhring á hvert kerfi, þekju einkennaprófa, árangurshlutföll afstemmingar flutnings, misræmistalningar tvíkeyrslu og verðmæti skilað á hvern áfanga, allt rakið gegn markmiðum. Ákvarðanir um ráðsmennsku-eða-afleysingu og fara/ekki-fara kall um yfirfærslu eru teknar á þessum sönnunargögnum, og kerfi sem rekur yfir þekkingaráhættuþröskuld kallar fram aðgerð frekar en að bíða eftir kreppu.
- **Stig 5: Samhæfing.** Nútímavæðing er samfelld, samþætt viðskipta- og áhættuáætlun og aðlögunarhæf. Eignasafnið er endurjafnað gegn áhættuferli (sérstaklega þekkingaráhættu) eftir því sem hann breytist, stigvaxandi afleysing er rútína og tíðindalítil, hver áfangi skilar verðmæti og er afturkræfur og skipulagsheildin stýrir hraðanum af ásetningi. Lærdómur af hverjum flutningi nærir aftur í sameiginlegu leikbókina svo allt búið batnar með tímanum.

## Hugmyndir til umræðu

1. Fyrir mikilvægasta eldra kerfið þitt, hve margir geta enn viðhaldið því og hve nærri brottför eru þeir?
2. Hvar freistast þú af stórhvellsendurskrift og hvaða verðmæti gæti stigvaxandi nálgun skilað á fyrstu þremur mánuðunum í staðinn?
3. Hve vel eru viðskiptareglurnar í elstu kerfum þínum skjalfestar og hvað verður um þær ef kóðanum er skipt út?
4. Hefurðu sniðgreint gögnin sem þú þyrftir að flytja og veistu hve skítug og flækt þau eru í raun?
5. Hvaða gömlu en stöðugu kerfum ertu að eyða nútímavæðingarorku í sem þú gætir óhætt látið í friði?
6. Gætirðu keyrt nýja kerfið þitt samsíða því gamla og sannað að þau séu sammála áður en þú færir yfir?

## Helstu atriði

- Eldra þýðir verðmætt og grundvallandi. Berðu virðingu fyrir og skildu kerfi áður en þú breytir því.
- Nútímavæddu stigvaxandi með kyrkingarfíku og útibúi-með-ágripun, skilaðu verðmæti samfellt og haltu hverri breytingu lítilli og afturkræfri.
- Líttu á stórhvellsendurskriftina sem sjálfgefinn bilunarhátt. Taktu hana frá fyrir raunverulega ósjálfbæra vettvanga og sundurliðaðu hana jafnvel þá.
- Forgangsraðaðu eftir áhættu og verðmæti (sérstaklega þekkingaráhættu), ekki aldri. Sum gömul kerfi er best að sinna með ráðsmennsku, ekki skipta út.
- Gagnaflutningur og tvíkeyrsla eru hjarta átaksins. Sniðgreindu, afstemmdu, keyrðu samsíða og haltu afturköllun.
- Sterkustu viðskiptarökin eru valkostir: stigvaxandi nútímavæðing breytir einu stóru, áhættusömu veðmáli í mörg lítil sem skila verðmæti.

## Heimildir og frekari lestur

- Michael Feathers, *Working Effectively with Legacy Code*
- Martin Fowler, "StranglerFigApplication" and "BranchByAbstraction"
- Sam Newman, *Monolith to Microservices*
- Nicholas Carr / industry studies on mainframe and COBOL dependency (context on the scale of legacy estates)
- Robert Annett, *Working with Legacy Systems*
- Eric Evans, *Domain-Driven Design* (anti-corruption layer)
- Gregor Hohpe, *Enterprise Integration Patterns* and *The Software Architect Elevator*
- Standish Group *CHAOS Report* (evidence on large project and rewrite failure rates)
