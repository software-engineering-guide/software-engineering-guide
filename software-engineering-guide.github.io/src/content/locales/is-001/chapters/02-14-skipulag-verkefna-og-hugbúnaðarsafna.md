# 2.14 Skipulag verkefna og hugbúnaðarsafna

## Yfirlit og tilgangur

Uppbygging verkefna og hugbúnaðarsafna er líkamleg skipulagning kóðagrunns: möppurnar, skrárnar og nafngiftavenjurnar sem ákvarða hvar hver hlutur býr. *Hugbúnaðarsafn* (oft stytt í „safn“, repo) er [útgáfustýrði](https://en.wikipedia.org/wiki/Version_control) geymirinn sem heldur skrám verkefnis og sögu þeirra. *Verkefni*, stundum kallað *lausn* þegar það flokkar saman nokkra skylda íhluti, er rökræna einingin af hugbúnaði sem þú ert að smíða. Uppbygging er kortið sem þú notar til að finna, skilja og breyta þeim hugbúnaði.

Í litlu teymi getur ein manneskja haldið öllu skipulaginu í höfðinu. Í stóru teymi, með hundruð eða þúsundir verkfræðinga, tíða flutninga milli teyma og verktaka sem koma og fara, leggur hvert safn sem er skipulagt öðruvísi á nýjan vitrænan skatt. Þegar þú opnar ókunnugt safn ættirðu að geta giskað hvar frumkóðinn, prófin, skjölunin og uppsetningarstillingin búa, án þess að lesa handbók. Þegar hvert safn svarar þessum spurningum eins er hreyfanleiki ódýr og móttaka hröð. Þegar hvert safn er snjókorn verður hvert samhengisskipti að litlu rannsóknarverkefni.

Í fyrirtækja- og opinberu umhverfi er samræmd uppbygging líka stýringar- og tryggingaráhyggjuefni. Endurskoðendur, öryggisrýnar og langtímaumsjónarmenn, sem oft vinna árum eftir að upphaflegir höfundar eru farnir, þurfa að finna áreiðanlega tilgreiningarskjöl, leyfisskrár, öryggisstefnur og smíðaskilgreiningar. Fyrirsjáanlegt skipulag leyfir líka sjálfvirkum verkfærum (skönnum, ósjálfstæðisgreinum, regluvörsluathugunum) að virka eins yfir heilt eignasafn kerfa. Þessi kafli lítur því á uppbyggingu sem venju sem þú ákveður einu sinni og beitir alls staðar. Hún tengist náið kóðunarstöðlum og stíl (kafli 2.1), útgáfustýringu og frumkóðastjórnun (kafli 2.6) og skjölun (kafli 2.7).

## Meginreglur

- Fylgdu *[meginreglunni um minnsta undrun](https://en.wikipedia.org/wiki/Principle_of_least_astonishment)*: skipulagið ætti að passa við það sem reyndur verkfræðingur býst við, svo ekkert þurfi að leggja á minnið.
- Samræmi milli safna slær staðbundna snilld. Nógu einsleit uppbygging alls staðar er meira virði en fullkomin uppbygging á einum stað.
- [README](https://en.wikipedia.org/wiki/README) er útidyrnar. Nýliði ætti að geta áttað sig af því einu.
- Gerðu uppbyggingu sjálflýsandi gegnum nafngiftir, svo möppur og skrár boði tilgang sinn.
- Framfylgdu uppbyggingu með grindarsmíði og sniðmátum, ekki viljastyrk og rýniathugasemdum.
- Aðskildu áhyggjuefni líkamlega: frumkóði, próf, skjölun, smíði og uppsetning tilheyra aðskildum, fyrirsjáanlegum stöðum.
- Skipuleggðu ósjálfstæði svo það flæði í eina átt, frá stöðugum kjörnum í átt að sveiflukenndum jöðrum.

## Ráðleggingar

### Taktu upp samræmt efsta-stigs skipulag

Skilgreindu staðlað safn efsta-stigs mappa sem hvert safn notar þar sem við á, og skjalfestu til hvers hver er. Algeng, söluaðilahlutlaus venja felur í sér: frumkóðamöppu (oft `src`) fyrir framleiðslukóða, prófamöppu (oft `test` eða `tests`) fyrir sjálfvirk próf, `docs` möppu fyrir skjölun, `build` möppu fyrir smíðaskilgreiningar og úttök, `deploy` möppu fyrir uppsetningu og *[innviði sem kóða](https://en.wikipedia.org/wiki/Infrastructure_as_code)* (véllæsilegar skilgreiningar á netþjónum, netum og þjónustum, fjallað um í kafla 8.2), `scripts` möppu fyrir sjálfvirkni og þróunarverkfæri, `examples` möppu fyrir keyranleg dæmi og `spec` eða `specification` möppu fyrir kröfur og hönnunartilgreiningar. Ekki þarf hvert safn hverja möppu, en þar sem áhyggjuefni er til ætti það að búa á væntum stað með væntu nafni.

### Gerðu README að inngangsstaðnum

Krefstu README-skrár í rót hugbúnaðarsafnsins sem eina, valdbæra upphafspunktinn. Hún ætti að segja hvað verkefnið er, hvernig á að smíða og keyra það, hvernig á að keyra prófin, hvar dýpri skjölun er að finna, hver á það og hvernig á að leggja til. README er ekki allt skjalasafnið. Hún er skráin sem vísar á restina (kafli 2.7). Líttu á vantandi eða úrelta README sem galla, því hún er það fyrsta sem sérhver nýr verkfræðingur, endurskoðandi eða samþættari les.

### Staðlaðu ritla- og stillingarskrár

Skuldbindu sameiginlega ritla- og verkfærastillingu í hugbúnaðarsafnið svo hver þátttakandi fái samræmda hegðun sjálfkrafa. `.editorconfig` skrá (einföld, ritlaóháð skrá sem skilgreinir bil-, inndráttar- og línuloka­reglur) heldur grunnsniði einsleitu milli ólíkra ritla og stýrikerfa. Bættu við hunsunarskrá fyrir útgáfustýringarkerfið (svo smíðaúttök og staðbundnar afurðir séu aldrei skuldbundnar), ásamt sameiginlegu sniðmótara- og lint-stillingunum sem lýst er í kafla 2.1. Þessar skrár gera venjur safnsins virkar, ekki bara skjalfestar.

### Skilgreindu nafngifta- og möppuvenjur

Komdu þér saman um venjur fyrir nafngiftir mappa og skráa (hástafa- og lágstafanotkun, aðgreinara, eintölu á móti fleirtölu og nauðsynleg viðskeyti eins og þau sem merkja próf) og beittu þeim einsleitt. Nöfn ættu að opinbera ásetning og passa við lénsorðaforðann sem notaður er annars staðar í skipulagsheildinni. Markmiðið er einfalt: slóð ætti að miðla merkingu, svo að lesa möppu- eða skráarnafn segi þér hvað er inni án þess að opna það.

### Skipuleggðu lög og ósjálfstæði af ásetningi

Byggðu kóðagrunninn svo arkitektúrlög hans birtist í möppuskipulaginu og svo ósjálfstæði flæði í eina, skynsama átt. Hærra-stigs stefna ætti ekki að byggja á lágstigs smáatriðum. Sameiginlegur, stöðugur kóði ætti að sitja þar sem margar einingar ná til hans án þess að skapa hringi. Þegar þú gerir lagskiptinguna líkamlega, endurspeglaða í möppuhierarkíunni, eru verkfræðingar líklegri til að virða hana og brot eru auðveldari að koma auga á í rýni og sjálfvirkum ósjálfstæðisathugunum.

### Framfylgdu uppbyggingu með grindarsmíði og sniðmátum

Útvegaðu *[grindarsmíði](https://en.wikipedia.org/wiki/Scaffold_%28programming%29)*, sjálfvirka myndun upphafsverkefnis, svo ný hugbúnaðarsöfn byrji þegar rétt. *Sniðmát* eða *cookiecutter* (stikuð verkefnisgrind sem myndar tilbúið hugbúnaðarsafn úr svörum við nokkrum spurningum) kóðar staðlaða skipulagið, README, stillingarskrárnar og [CI](https://en.wikipedia.org/wiki/Continuous_integration) uppsetninguna á einum stað. Þegar verkfræðingar búa til nýjar þjónustur úr sameiginlegu sniðmáti verður samræmi sjálfgefið í stað þess að vera von, og umbætur á sniðmátinu flæða til framtíðarverkefna.

### Haltu uppbyggingu samræmdri yfir mörg hugbúnaðarsöfn í stórum stíl

Líttu á skipulagið sjálft sem stýrðan staðal: viðhaldið miðlægt eins og hver annar verkfræðistaðall (kafli 1.7) og útgáfustýrt eins og kóði (kafli 2.6). Birtu það, útvegaðu sniðmátin sem útfæra það og leyfðu frávik aðeins gegnum skjalfest undanþáguferli, svo að „staðallinn“ haldi merkingu sinni. Í stærðargráðu eignasafns kemur nánast allt virði uppbyggingar frá einsleitni hennar yfir söfn, svo rek er aðaláhættan til að stýra.

### Láttu uppbyggingu upplýsa einsafns-á-móti-fjölsafns valið

Tengdu uppbyggingu við hugbúnaðarsafnsmarkaákvörðunina sem fjallað er um í kafla 2.6. *[Einsafn](https://en.wikipedia.org/wiki/Monorepo)* (eitt hugbúnaðarsafn sem heldur mörgum verkefnum) þarf skýra innri venju til að aðskilja verkefni og sameiginlegan kóða þeirra, svo eina tréð haldist rataðhæft. *Fjölsafns*-nálgun (mörg lítil hugbúnaðarsöfn, eitt fyrir hvert verkefni eða þjónustu) þarf sterkt samræmi milli safna, svo hvert safn finnist kunnuglegt þótt það standi eitt og sér. Hvort sem er er skjalfest, sniðmótuð uppbygging það sem heldur leiðsögn fyrirsjáanlegri. Markaválið breytir hvar þú beitir venjunni, ekki hvort þú þarft eina.

## Málamiðlanir: kostir og gallar

| Val | Kostir | Gallar |
|---|---|---|
| Ströng staðalskipulag fyrir alla skipulagsheildina | Tafarlaus kunnugleiki, færanlegir verkfræðingar, einsleit verkfæri | Stöku léleg passun fyrir óvenjuleg verkefni, þarf stjórnarhætti |
| Skipulagsfrelsi hvers teymis | Staðbundin fínstilling, mikið sjálfstæði | Sundrun, dýr samhengisskipti, ósamræmd verkfæri |
| Grindarsmíði og sniðmát | Rétt-sjálfgefin söfn, breytingar breiðast út | Sniðmátsviðhald, hætta á reki frá mynduðum söfnum |
| Djúp, lagskipt möppuhierarkía | Skýr uppbygging, skýr mörk | Leiðsagnaryfirbygging, langar slóðir, hætta á ofhönnun |
| Flatt, grunnt skipulag | Auðvelt að skanna, lítill helgisiður | Léleg aðskilnaður, brotnar þegar verkefnið vex |

Ráðandi málamiðlunin er einsleitni gegn sjálfstæði. Eitt staðalskipulag fjarlægir núning fyrir mörgu verkfræðingana sem flytja milli kóðagrunna, á kostnað stöku verkefnis sem þarfir passa ekki snyrtilega í mótið. Í stórri skipulagsheild vegur sameiginlegi ávinningurinn af kunnugleika nánast alltaf þyngra en það staðbundna tap. Þess vegna er ráðlagða afstaðan sterkt sjálfgefið staðall auk skjalfestrar undanþáguleiðar (kafli 1.7), frekar en stíf einsleitni eða óstýrt frelsi. Aukamálamiðlun er dýpt gegn einfaldleika: nóg uppbygging til að aðskilja raunveruleg áhyggjuefni, en ekki svo mikil að leiðsögn verði ganga um tómar möppur.

## Spurningar til að ræða með teyminu

1. **Þegar verkfræðingur flytur í ókunnugt safn okkar, hve lengi þar til hann finnur prófin, uppsetningarstillinguna og eigandann?** Þetta er leiðsagnarskatturinn sem uppbygging er til að útrýma, og í stærðargráðu eignasafns er hann greiddur þúsundum sinnum á ári í litlum skrefum sem leggjast saman í verulegan tapaðan verkfræðitíma. Tilgangur meginreglunnar um minnsta undrun er að reyndur verkfræðingur ætti að geta giskað hvar frumkóði, próf, skjölun og uppsetning búa án þess að lesa handbók, svo heiðarlega prófið er hvort sú ágiskun heppnast yfir söfnin þín. Komdu með raunverulega tölu á fundinn: tímasettu ykkur að átta ykkur á tveimur eða þremur ókunnugum innri hugbúnaðarsöfnum, eða sæktu móttökugögn um hve langan tíma nýir starfsmenn taka til að gera fyrstu breytingu. Ef svarið er mælt í dögum rannsóknar en ekki mínútum viðurkenningar hefurðu magngreint kostnað snjókornasafna, og það réttlætir einskiptis fjárfestingu í stöðluðu skipulagi sem hvert safn deilir.

2. **Birtast arkitektúrlög okkar í möppuhierarkíunni, eða fela ósjálfstæðishringir sig í flötu skipulagi?** Uppbygging snýst um meira en finnanleika: þegar þú gerir lagskiptingu líkamlega virða verkfræðingar hana og rýnar og sjálfvirkar ósjálfstæðisathuganir geta komið auga á brot, á meðan flatur haugur leyfir óviðeigandi tengslum og hringjum að læðast inn óséðum þar til breyting verður hættuleg. Í stóru, langlífu kerfi er þetta það sem heldur hærra-stigs stefnu frá því að hljóðlega byggja á lágstigs smáatriðum, og það er nákvæmlega sú tegund rýrnunar sem er ódýr að koma í veg fyrir og dýr að rekja upp. Komdu með ósjálfstæðisgrafið þitt eða keyrðu fljótlega athugun: eru hringir til, og byggir eitthvað stöðugt á einhverju sveiflukenndu? Svarið ætti að ýta þér til að endurspegla lög í möppum og bæta við sjálfvirkum ósjálfstæðisstefnuathugunum, svo mörkin séu sýnileg í trénu og framfylgd í leiðslunni frekar en að lifa aðeins í hugarlíkani einhvers.

3. **Byrja ný hugbúnaðarsöfn okkar rétt úr sniðmáti, eða reiðum við okkur á wiki-síðu og góðan ásetning?** Uppbygging framfylgd með grindarsmíði er sjálfgefið. Uppbygging lýst í skjali rekur, því raunveruleikinn fylgir því sem myndar söfn, ekki því sem síða segir að þau ættu að líta út. Fyrir stóra eða eftirlitsskylda skipulagsheild er þetta líka tryggingaráhyggjuefni: þegar hvert safn er myndað úr sameiginlegu sniðmáti finna öryggisskannar, ósjálfstæðisgreinar og endurskoðendur leyfið, öryggisstefnuna, tilgreininguna og smíðaskilgreininguna á sama stað í hvert skipti, yfir söluaðila og yfir ár. Komdu með sönnunargögnin: hve mörg nýleg söfn voru mynduð úr staðlaða sniðmátinu á móti handsamsett, og hve langt hafa sniðmótuðu hafa rekið síðan? Aðgerðin er að gera sniðmátið að eina auðvelda leiðin til að hefja safn, stýra því sem útgáfustýrðum staðli með skjalfestri undanþáguleið og greina rek sjálfvirkt, því einsleitni er þar sem næstum allt virði uppbyggingar býr.

4. **Höfum við ákveðið hvort staðall okkar spannar einsafn eða mörg aðskilin hugbúnaðarsöfn, og gildir sama venjan í raun beggja vegna þess marks?** Hugbúnaðarsafnsmarkavalið breytir hvar þú beitir venjunni, ekki hvort þú þarft eina, og að fá það rangt þýðir eitt risatré sem enginn getur ratað um eða sundrun safna sem hvert finnst framandi. Einsafn þarf skýra innri venju til að aðskilja verkefni og sameiginlegan kóða þeirra svo eina tréð haldist rataðhæft, á meðan fjölsafns-nálgun þarf sterkt samræmi milli safna svo hvert sjálfstætt safn finnist samt kunnuglegt. Komdu með núverandi skrá: hve mörg söfn þú hefur, hvernig sameiginlegur kóði er aðskilinn inni í einsafni og tímasett próf á hvort verkfræðingur geti fundið verkefni inni í stóra trénu jafn hratt og hann finnur eitt í sjálfstæðu safni. Fyrir stórt fyrirtæki eða opinbera áætlun þar sem ólíkir söluaðilar afhenda aðskilin söfn skaltu ákveða af ásetningi hvaða hlutar venjunnar eru altækir og hverjir eru markasértækir, því endurskoðendur og vettvangsverkfæri verða að virka eins hvort sem kóðinn kemur sem eitt tré eða fimmtíu.

5. **Hver á uppbyggingarstaðal okkar og hvað gerist í raun þegar verkefni passar ekki í hann?** Í stærðargráðu eignasafns kemur nánast allt virði uppbyggingar frá einsleitni, svo raunverulegu áhætturnar eru óeignaður staðall sem rotnar og undanþáguleið svo óljós að hvert teymi finnur hljóðlega upp sitt eigið skipulag. Spennan er milli stífrar einsleitni sem passar ekkert óvenjulegt verkefni og óstýrðs frelsis sem sundrar öllu, og heilbrigða svarið er sterkt sjálfgefið ásamt skjalfestu, úttektarhæfu undanþáguferli stýrðu af nefndum eiganda og útgáfustýrðu eins og kóða. Komdu með sönnunargögnin: er einn ábyrgur eigandi til, útgáfustýrt staðlaskjal með breytingaskrá, skrá yfir veittar undanþágur og hvers vegna og fjöldi óskjalfestra frávika sem þú getur fundið í náttúrunni. Í fyrirtækja- og opinberu umhverfi er undanþága sem enginn skráði stýringarbil, svo tengdu hvert frávik við skriflegan rökstuðning og rýnidagsetningu og tryggðu að innkaupasamningar sem skylda skipulagið nefni líka hver má samþykkja frávik frá því.

6. **Gera README okkar og innritaðar stillingarskrár venjur okkar virkar, eða eru þær skrautlegar?** README er útidyrnar og innrituð `.editorconfig`, hunsunarskrá og lint-stilling eru það sem gerir venjur sjálffylgjandi, en samt eru þetta fyrstu hlutirnir til að úreldast og þeir síðustu sem nokkur tekur eftir þar til endurskoðandi eða nýliði getur ekki fengið verkefnið til að smíðast. Spennan er milli grannrar README sem helst núverandi og ítarlegrar sem rekur, og milli þess að treysta fólki til að sníða kóða rétt og láta sameiginlega stillingu framfylgja því sjálfvirkt. Komdu með úrtak: taktu fimm söfn og athugaðu hve margar README segja í raun hvað verkefnið er, hvernig á að smíða, prófa og keyra það og hver á það, og hve mörg bera sameiginlegu stillingarskrárnar frekar en að reiða sig á einstaklingsvenjur. Fyrir stóra eða eftirlitsskylda skipulagsheild, þar sem samþættarar, öryggisrýnar og langtímaumsjónarmenn lesa README á undan öllu öðru, skaltu líta á vantandi eða úreltar útidyr sem galla með eiganda og athuga nærveru stillingarskráa sjálfvirkt svo samræmi velti ekki á velvild.

## Sjónarhorn eftir geirum

**Sprotafyrirtæki.** Hraði vinnur, svo komdu þér saman um eitt einfalt, nógu flatt skipulag fyrir fyrsta safnið þitt (src, test, docs, scripts, útfyllta README, `.editorconfig` og hunsunarskrár) og vistaðu það sem létt sniðmát sama eftirmiðdag. Myndaðu aðra þjónustuna úr því svo bæði söfn finnist kunnugleg og nýr verktaki komist af stað á klukkustundum frekar en að rekja snjókorn afturábak. Standastu djúpar hierarkíur og þunga stjórnarhætti sem þú þarft ekki enn. Öll ávöxtunin hér er að tveir stofnendur og verktaki deili einu korti.

**Lítið fyrirtæki.** Án vettvangssérfræðings og með þröngt fjárhagsáætlun skaltu taka upp hefðbundna skipulagið sem tungumálið þitt eða ramminn gerir þegar ráð fyrir í stað þess að finna upp eitt, svo tilbúin verkfæri og hver nýr starfsmaður komi þegar þjálfuð í því. Keyptu grindarsmíði (rammamyndara eða cookiecutter-sniðmát) í stað þess að smíða þína eigin og eyddu af skornum skammti fyrirhöfn í að halda útfylltri README núverandi. Sú README er ódýrasta trygging sem þú átt fyrir daginn sem eina manneskjan sem þekkti skipulagið heldur áfram.

**Stórfyrirtæki.** Yfir mörg teymi og hundruð hugbúnaðarsafna er markmiðið einsleitni: birtu útgáfustýrðan uppbyggingarstaðal, myndaðu hverja nýja þjónustu úr sameiginlegum sniðmátum, greindu rek sjálfvirkt og leyfðu frávik aðeins gegnum skjalfest undanþáguferli. Því hvert safn lítur eins út er verkfræðingur fluttur í nýtt teymi afkastamikill innan klukkustunda og öryggis- og ósjálfstæðisskannar yfir allt eignasafnið finna leyfið, öryggisstefnuna og smíðaskilgreininguna á sama stað í hvert skipti. Fjárhagsáætlaðu sniðmátsviðhald og rekgreiningu skýrt, því það viðhald er það sem heldur staðlinum marktækum í stórum stíl.

**Hið opinbera.** Innkaup, gagnsæi og langtímaábyrgð móta skipulagið, svo skyldaðu sameiginlega uppbyggingu í afhendingarstöðlunum sem binda hvern söluaðila. Krefstu `specification` möppu sem tengir kóða við samþykktar kröfur, leyfis- og öryggisstefnuskrár í rót og `deploy` möppu sem heldur innviðum-sem-kóða skilgreiningunum, svo endurskoðendur finni regluvöruafurðir á sama hátt í hverju kerfi. Því verktakar frá ólíkum söluaðilum fylgja einu korti kostar viðhald eftir að samningi lýkur miklu minna og almenningur fær rökstudda, skoðanlega slóð frá kröfu til keyrandi kóða.

## Dæmi

**Sprotafyrirtæki.** Þriggja manna sprotafyrirtæki kemur sér saman um einfalt staðalskipulag fyrir fyrsta safnið sitt (src, test, docs, scripts, útfyllta README, .editorconfig og hunsunarskrár) og vistar það sem létt sniðmát. Þegar þau setja upp aðra þjónustuna mánuði síðar mynda þau hana úr því sniðmáti, svo bæði söfn finnast þegar kunnugleg og nýi verktakinn kemst af stað á eftirmiðdegi. Þau standast djúpar möppuhierarkíur sem þau þurfa ekki enn og halda trénu nógu flötu til að skanna í fljótu bragði. Kostnaðurinn var einn eftirmiðdagur af uppsetningu, og hann sparar þeim snjókornasprengjuna sem annars myndi gera hvert framtíðarsafn að litlu rannsóknarverkefni.

**Stórfyrirtæki.** Fjölþjóðleg verslunarkeðja rekur hundruð þjónusta yfir nokkur tungumál. Vettvangsteymi hennar birtir útgáfustýrðan hugbúnaðarsafnsuppbyggingarstaðal og safn verkefnasniðmáta sem útfæra hann. Sérhver ný þjónusta er mynduð úr sniðmáti, svo hún kemur með stöðluðu `src`, `test`, `docs`, `deploy` og `scripts` möppunum, útfylltri README, `.editorconfig`, hunsunarskrám og virkri CI-leiðslu. Því hvert safn lítur eins út er verkfræðingur fluttur í nýtt teymi afkastamikill innan klukkustunda og öryggis- og ósjálfstæðisskannar yfir alla skipulagsheildina keyra einsleitt því þeir finna alltaf skrár þar sem þeir búast við.

**Hið opinbera.** Landsbundin stofnun sem nútímavæðir eldri kerfi skyldar sameiginlegt hugbúnaðarsafnsskipulag sem hluta af afhendingarstöðlum sínum fyrir alla söluaðila. Hvert hugbúnaðarsafn verður að innihalda `specification` möppu sem tengir kóða við samþykktar kröfur, skjalfesta README, leyfis- og öryggisstefnuskrá í rót og `deploy` möppu sem heldur innviðum-sem-kóða skilgreiningunum (kafli 8.2). Því verktakar frá ólíkum söluaðilum fylgja sömu uppbyggingu geta endurskoðendur stofnunarinnar fundið regluvöruafurðir á sama hátt í hverju kerfi og langtímaviðhald eftir að samningi lýkur kostar miklu minna því komandi umsjónarmenn þekkja þegar kortið.

## Viðskiptarök: hvatar, ávöxtun fjárfestingar og heildarkostnaður

Kostnaður við að taka upp uppbyggingarstaðal er aðallega einskiptis: að koma sér saman um skipulagið, smíða sniðmátin og skjalfesta venjuna. Endurtekni kostnaðurinn er lágur, einbeittur í að viðhalda sniðmátunum og stýra undanþágum. Kostnaðurinn við að hafa *ekki* staðal er endurtekinn og safnast upp: sérhver verkfræðingur sem opnar ókunnugt safn borgar leiðsagnarskatt, hver móttaka er hægari og sjálfvirk verkfæri þarf að stilla á hvert safn því ekkert er þar sem þú býst við. Yfir stóra skipulagsheild margfaldast þessi smáu núningur í veruleg töp á verkfræðitíma.

Ávöxtunin birtist sem hraðari móttaka, ódýrari hreyfanleiki milli teyma, hærra merki frá verkfærum yfir eignasafnið og, í eftirlitsskyldu umhverfi, lægri úttektar- og langtímaviðhaldskostnaður, því afurðir eru alltaf finnanlegar. *Heildareignarkostnaður* (TCO, sem þýðir fullur líftímakostnaður við að smíða, reka og viðhalda kerfi) lækkar mest í langlífum kerfum, þar sem umsjónarmennirnir sem njóta góðs af fyrirsjáanlegri uppbyggingu eru venjulega ekki höfundarnir sem bjuggu hana til. Til að færa rök við forystu skaltu ramma uppbyggingu sem ódýran, áhrifamikinn staðal sem bætir framleiðni þróunaraðila og úttektarviðbúnað og setja tölu á núverandi kostnað ósamræmis með móttökutímagögnum og fyrirhöfninni sem fer í að leita að hlutum í ókunnugum hugbúnaðarsöfnum.

## Andmynstur og gildrur

- **Snjókornasafnið:** hvert safn skipulagt öðruvísi, svo hvert og eitt verður að læra frá grunni.
- **Vantandi eða úrelt README:** engar útidyr, sem neyðir nýliða til að rekja afturábak hvernig á að smíða og keyra verkefnið.
- **Uppbygging eftir skjali, ekki sniðmáti:** wiki-síða lýsir staðalskipulaginu, en ekkert myndar eða framfylgir því, svo raunveruleikinn rekur frá því.
- **Sniðmátsrek:** hugbúnaðarsöfn mynduð úr sniðmáti víkja með tímanum og umbætur á sniðmátinu ná aldrei til þeirra.
- **Ofhönnuð hierarkía:** djúp hreiður nánast tómra mappa sem bæta við helgisið án þess að hjálpa leiðsögn.
- **Blönduð áhyggjuefni:** frumkóði, próf, smíðaúttök og leyndarmál hrúguð saman án skýrs aðskilnaðar.
- **Innritað smíðaúttök og staðbundnar afurðir:** mynduð skrá innrituð því hunsunarreglur voru aldrei settar upp, sem mengar sögu og mismun.
- **Lagabrot falin af flötu skipulagi:** engin líkamleg mörk, svo ósjálfstæðishringir og óviðeigandi tengsl læðast inn óséð.

## Þroskalíkan

- **Stig 1 (Upphaf):** Hvert hugbúnaðarsafn er skipulagt ad hoc af höfundum sínum, bregst við því sem augnablikið þarf. Skipulag er mjög ólíkt, README vantar eða er óáreiðanleg og nýliða þarf að leiða í gegnum hvert safn í höndunum.
- **Stig 2 (Þróun):** Grunnvenjur eru til óformlega og mörg söfn líkjast hvert öðru, sum teymi halda eigin upphafsskipulagi, en enginn valdbær staðall er til, engin sameiginleg grindarsmíði og uppbygging rekur áberandi frá einu teymi til annars.
- **Stig 3 (Stöðlun):** Skjalfestur, útgáfustýrður uppbyggingarstaðall er framfylgt um alla skipulagsheildina. Ný hugbúnaðarsöfn eru mynduð úr sameiginlegum sniðmátum sem bera staðlað skipulag, README, stillingarskrár og CI. Frávik fara gegnum skjalfest undanþáguferli en gerast ekki hljóðlega.
- **Stig 4 (Stjórnun):** Samræmi við staðalinn er mælt og stýrt með gögnum: sjálfvirkar athuganir skýra frá hlutfalli safna sem passa við skipulagið, hve langt sniðmótuð söfn hafa rekið, fullkomleika README og ósjálfstæðisstefnubrotum, allt rakið gegn grunnlínum. Móttöku- og leiðsagnartímar eru mældir. Undanþágur eru skráðar og rýndar og sniðmátsbreytingar eru samþykktar á sönnunargögnum frekar en skoðun.
- **Stig 5 (Samhæfing):** Uppbygging er stöðugt bætt og aðlögunarhæf: sniðmátsumbætur breiðast sjálfvirkt út til núverandi safna, uppbyggingarstjórnarhættir eru samþættir öryggis-, regluvörslu- og vettvangsverkfærum og staðallinn þróast af ásetningi eftir því sem tungumál, arkitektúr og eignasafn breytast, og heldur einsleitni hárri meðan skipulagsheildin breytist í kringum hann.

## Hugmyndir til umræðu

- Hvaða efsta-stigs möppur ættu að vera sannarlega altækar yfir skipulagsheildina þína og hverjar ættu að vera valkvæðar?
- Hvernig heldurðu hugbúnaðarsöfnum mynduðum úr sniðmáti frá því að víkja frá því með tímanum?
- Hvar er línan milli hjálplegrar, lagskiptrar hierarkíu og ofhannaðs möppuhelgisiðs?
- Hvernig ætti uppbyggingarstaðall þinn að vera ólíkur, ef yfirleitt, milli einsafns og fjölsafns-nálgunar?
- Hvert er rétt undanþáguferli fyrir verkefni þar sem raunverulegar þarfir passa ekki í staðalskipulagið?
- Hve mikið af uppbyggingu þinni er hægt að athuga sjálfvirkt og hvað treystir enn á mannlega rýni?
- Hver á uppbyggingarstaðalinn og sniðmát hans og hvernig eru breytingar lagðar til og útfærðar?

## Helstu atriði

- Skipuleggðu hvert hugbúnaðarsafn svo hver verkfræðingur geti ratað um hvaða kóðagrunn sem er eftir væntingum, eftir meginreglunni um minnsta undrun.
- Taktu upp samræmt efsta-stigs skipulag (frumkóði, próf, skjöl, smíði, uppsetning, skriftur, dæmi, tilgreining) og gerðu README að inngangsstaðnum.
- Innritaðu ritla- og verkfærastillingu (eins og `.editorconfig`) svo venjur séu virkar, ekki bara skrifaðar niður.
- Framfylgdu uppbyggingu með grindarsmíði og sniðmátum svo ný hugbúnaðarsöfn séu rétt sjálfgefið.
- Í stórum stíl er virðið í einsleitni: stýrðu staðlinum, stýrðu reki og leyfðu frávik aðeins með skjalfestri undanþágu.

## Heimildir og frekari lestur

- Robert C. Martin, *Clean Architecture: A Craftsman's Guide to Software Structure and Design*
- Steve McConnell, *Code Complete: A Practical Handbook of Software Construction*
- Andrew Hunt and David Thomas, *The Pragmatic Programmer*
- Titus Winters, Tom Manshreck, and Hyrum Wright (eds.), *Software Engineering at Google*
- Scott Chacon and Ben Straub, *Pro Git*
- EditorConfig project documentation (as a reference standard for editor configuration)
