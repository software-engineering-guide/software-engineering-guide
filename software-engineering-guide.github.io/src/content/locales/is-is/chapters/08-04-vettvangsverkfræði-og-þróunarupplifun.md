# 8.4 Vettvangsverkfræði og þróunarupplifun

## Yfirlit og tilgangur

[Vettvangsverkfræði](https://en.wikipedia.org/wiki/Platform_engineering) er sú grein að smíða og reka innri vöru, innri þróunarvettvang (IDP), sem aðrir verkfræðingar nota til að smíða, afhenda og reka hugbúnað sinn. Í stað þess að hvert teymi setji saman eigin leiðslur, innviði og verkfæri frá grunni býður sérstakt vettvangsteymi valdar sjálfsafgreiðslugetur eftir vel studdum „gullnum slóðum“, sem eru skoðanaríkar, studdar leiðir með skynsamleg sjálfgefin gildi bökuð inn. [Þróunarupplifun](https://en.wikipedia.org/wiki/Developer_experience) (DevEx) er náskylda áhyggjuefnið um hvernig það er að vera verkfræðingur í skipulagsheildinni: hve auðveldlega og hratt forritari kemst frá hugmynd til keyrandi hugbúnaðar og hve mikill núningur stendur í vegi.

Fyrir stór teymi skiptir þetta máli því [hugræn byrði](https://en.wikipedia.org/wiki/Cognitive_load) og núningur skalast ekki mjúklega. Með mörgum teymum heldur fjöldi verkfæra, kerfa og ákvarðana sem hver verkfræðingur þarf að halda á lofti áfram að vaxa. Fyrr en varir fer stór hluti tíma þeirra í innviðalagnir og samræmingu frekar en að skila verðmæti. Án vettvangs leysir hvert teymi sömu vandamálin, svo sem útvegun, útsetningu, vöktun og reglufylgni, ósamræmt og aftur og aftur. Góður vettvangur tekur við þessari sameiginlegu flækju. Teymi geta þá einbeitt sér að léni sínu á meðan þau erfa samt staðla skipulagsheildarinnar fyrir öryggi, áreiðanleika og kostnað.

Mikilvægi fyrir fyrirtæki og hið opinbera er mikið, því þessar skipulagsheildir sameina stærð og strangar stjórnarhætti. Vettvangur er eðlilegi staðurinn til að kóða reglufylgni-, öryggis- og úttektarkröfur einu sinni, sem troðnar slóðir sem teymi fylgja sjálfgefið. Það slær því að ætlast til að hvert teymi túlki og útfæri stefnu rétt á eigin spýtur. Það breytir stjórnarháttum úr uppsprettu núnings í ósýnilegan eiginleika staðlaða vinnuflæðisins, nákvæmlega það sem stórar regluverkaðar skipulagsheildir þurfa til að hreyfa sig hratt án þess að missa stjórn.

## Meginreglur

- Líttu á vettvanginn sem vöru, með notendum, vegvísi og umboði til að vinna sér inn upptöku frekar en að þvinga hana.
- Útvegaðu gullnar slóðir: skoðanaríkar, vel studdar leiðir sem gera rétta háttinn að auðvelda hættinum.
- Gerðu getu sjálfsafgreiðslu svo teymi bíði ekki eftir miðum og mannlegum afhendingum.
- Leggðu troðnar slóðir frekar en að reisa hlið. Byggðu inn varnarrimla sem leiðbeina án þess að hindra lögmæta vinnu.
- Minnkaðu hugræna byrði forritara miskunnarlaust.
- Mældu þróunarupplifun og framleiðni með jafnvægum, fjölvíðum merkjum.
- Hafðu gullnar slóðir valkvæðar en svo góðar að teymi velji þær.

## Ráðleggingar

### Byggðu vettvanginn sem vöru

Mikilvægasta einstaka breytingin er að líta á vettvanginn sem vöru sem þjónar innri viðskiptavinum, ekki sem lögboðinn staðal sem lagður er ofan frá. Í reynd þýðir það að skilja þarfir forritara gegnum rannsóknir og endurgjöf, viðhalda vegvísi, mæla upptöku og ánægju og bera ábyrgð á upplifuninni. Vettvangur sem teymi eru neydd til að nota en hægir á þeim verður illa séður og sniðgenginn. Vettvangur sem gerir teymi raunverulega hraðari mun breiðast út á orðsporinu. Upptaka unnin með gæðum er sannasti mælikvarði árangurs vettvangs.

### Útvegaðu gullnar slóðir og troðnar slóðir

Skilgreindu gullnar slóðir fyrir algengu ferðirnar: að búa til nýja þjónustu, setja hana upp, bæta við gagnagrunni, tengja vöktun, mæta reglufylgnikröfum. Gullin slóð er studd, skoðanarík leið frá enda til enda með skynsamleg sjálfgefin gildi bökuð inn. Meðfram þessum slóðum skaltu fella inn varnarrimla, það er öryggisskönnun, stefnuathuganir og bestu venjur, svo teymi sem fylgir slóðinni sé sjálfvirkt löghlýðið og öruggt. Markmiðið er einfalt: auðveldasta leiðin til að gera eitthvað ætti líka að vera rétta, örugga og löghlýðna leiðin. Hafðu slóðirnar valkvæðar, svo teymi með sannarlega óvenjulegar þarfir geti vikið. En gerðu slóðirnar nógu sannfærandi til að flest teymi vilji það aldrei.

### Veittu raunverulega sjálfsafgreiðsluinnviði

Útrýmdu miða-og-bíða afhendingum með því að birta innviði og getur gegnum sjálfsafgreiðsluviðmót: gátt, skipanalínutól, API eða sniðmáta hirslur. Forritari ætti að geta útvegað löghlýðið umhverfi, sett upp nýja þjónustu úr sniðmáti eða beðið um gagnagrunn á mínútum, án þess að leggja inn beiðni og bíða daga eftir öðru teymi. Sjálfsafgreiðsla er það sem breytir vettvangi úr flöskuhálsi í hraðal. Og hún virkar aðeins því undirliggjandi varnarrimlar gera sjálfsafgreiðslu örugga.

### Bjóddu þróunargáttir, þjónustuskrár og stigakort

Þróunargátt gefur þér eina rúðu: skrá yfir allar þjónustur með eigendum þeirra, skjölun, ósjálfstæðum og heilsu. Þjónustuskrár gera eignarhald og arkitektúr finnanleg. Það er ómetanlegt í stærð, þar sem enginn getur haldið öllu kerfinu í höfðinu. Stigakort mæla hverja þjónustu gegn stöðlum eins og prófaþekju, öryggisstöðu, bakvaktarviðbúnaði og skjölun og gefa teymum skýra, hlutlæga mynd af hvar þau standa og hvað þarf að bæta. Saman stytta þessi verkfæri tímann sem verkfræðingar eyða í að leita upplýsinga og þau skýra ábyrgð.

### Mældu þróunarupplifun með jafnvægum rammaverkum

Stattu gegn einstökum framleiðnimælikvörðum. Þeir eru auðveldlega spilaðir og villandi. Notaðu fjölvíða ramma eins og SPACE (ánægja og vellíðan, frammistaða, virkni, samskipti og samvinna, skilvirkni og flæði) til að fanga raunverulega áferð þróunarupplifunar. Sameinaðu skynjunargögn úr könnunum við kerfisgögn úr verkfærum. Raktu afhendingarmælikvarða eins og leiðtíma og útsetningartíðni við hlið viðhorfs forritara. Markmiðið er að skilja og fjarlægja núning, ekki að raða einstaklingum. Mæling sem finnst eins og eftirlit mun éta traustið sem vettvangurinn byggir á.

### Minnkaðu hugræna byrði sem fyrsta flokks markmið

Hugræn byrði, heildar hugræna áreynslan sem forritari þarf að eyða í starfi sínu, er falinn skatturinn sem vettvangar eru til að minnka. Lágmarkaðu fjölda verkfæra, hugtaka og samhengisskipta sem forritari verður að ná tökum á. Útvegaðu skynsamleg sjálfgefin gildi, svo teymi taki færri ákvarðanir af litlu gildi. Byggðu upp eignarhald svo hvert teymi eigi afmarkaða, skiljanlega sneið kerfisins. Þegar þú metur hvaða vettvangseiginleika sem er skaltu spyrja einnar spurningar: minnkar eða eykur hann byrðina á teymunum sem munu nota hann?

## Málamiðlanir: kostir og gallar

| Val | Kostir | Gallar | Best passun |
|---|---|---|---|
| Vettvangur sem vara (valkvæður) | Vinnur sér upptöku. Heldur gagnsemi | Hægara að ná fullri þekju | Flestar skipulagsheildir |
| Lögboðinn vettvangur | Hröð stöðlun | Gremja. Sniðgöngur | Aðeins sterkar stjórnarháttaþarfir |
| Kaupa gátt/vettvang | Hraðara til verðmætis | Minna sniðið. Leyfiskostnaður | Teymi sem vilja forskot |
| Smíða innanhúss | Passar nákvæmum þörfum | Hár smíða- og viðhaldskostnaður | Stórar, sérstæðar skipulagsheildir |
| Aðeins stífar gullnar slóðir | Hámarkssamræmi | Hindrar lögmæt jaðartilvik | Mjög einsleit vinnuálög |
| Sveigjanlegar slóðir með neyðarútgöngum | Jafnvægi samræmis og sjálfræðis | Einhver frávik að stýra | Fjölbreyttar teymisþarfir |

Kjarnaspennan er stöðlun gegn sjálfræði. Of lítil stöðlun og hvert teymi finnur upp hjólið ósamræmt. Of mikil og þú kæfir teymin sem hafa sannarlega ólíkar þarfir. Heimspekin um vettvang sem vöru leysir þetta með því að gera stöðlun aðlaðandi frekar en skyldubundna. Önnur raunveruleg málamiðlun er smíða gegn kaupa. Að smíða innanhúsvettvang passar nákvæmum þörfum þínum en ber umtalsverðan viðvarandi kostnað. Að taka upp núverandi verkfæri flýtir verðmæti, á verði einhverrar sérsniðningar.

## Spurningar til að ræða með teyminu

1. **Hvernig munuð þið vita að vettvangurinn minnkar hugræna byrði frekar en að bæta við einu verkfæri enn til að læra?** Hugræn byrði er heildar hugræna áreynslan sem verkfræðingur eyðir í starfið og vettvangur sem bætir við hugtökum og samhengisskiptum getur gert hana verri jafnvel þótt hann líti áhrifamikill út. Taktu upp eitt próf fyrir hvern eiginleika: minnkar hann eða eykur byrðina á teymunum sem nota hann? Í stærð er þetta úrslitaatriði, því vettvangur situr fyrir framan hundruð verkfræðinga og ruglingslegur útdráttur skattleggur þá alla daglega. Komdu með sönnunargögn: hve mörg verkfæri og gáttir forritari snertir til að afhenda breytingu, tíma-að-fyrstu-útsetningu fyrir nýjan starfsmann og eigindlega endurgjöf um hvar fólk festist. Ef vettvangurinn lengir verkfærakeðjuna í stað þess að stytta hana hefurðu smíðað skatt, ekki troðna slóð.

2. **Hvaða staðla framfylgja stigakort ykkar og hvað gerist í raun við þjónustu sem fær lága einkunn?** Stigakort mæla hverja þjónustu gegn væntingum eins og prófaþekju, öryggisstöðu, bakvaktarviðbúnaði og skjölun og gildi þeirra hrynur ef rautt stig hefur engar afleiðingar. Ákveddu hvort stigakort séu eingöngu ráðgefandi, nærist inn í rýni eða hliði tilteknar getur og ákveddu hver á staðlana. Í regluverkuðum skipulagsheildum geta stigakort gefið eftirlitsaðilum samfellda sýn á reglufylgnistöðu, sem kemur í stað handvirkrar skýrslugerðar, svo viðmiðið sem þú setur skiptir máli. Komdu með drög að stöðlum og úrtak raunverulegra þjónusta stiguð gegn þeim og ræddu hvar teymi myndu lögmætt streitast á móti. Stigakort sem enginn bregst við er mælaborð. Stigakort tengt skýrum væntingum breytir hegðun.

3. **Rekið þið vettvanginn sem raunverulega vöru, með vegvísi, notendarannsóknum og upptökumælikvörðum, eða sem umboð?** Meginveðmál þessa kafla er að stöðlun ætti að vera aðlaðandi frekar en þvinguð og það heldur aðeins ef þú lítur á innri verkfræðinga sem viðskiptavini sem þú verður að vinna. Ákveddu hver leikur vörustjórann fyrir vettvanginn, hvernig þú safnar þörfum forritara og hvaða upptöku- og ánægjutölur skilgreina árangur. Fyrir stórar skipulagsheildir er umboð freistandi því það staðlar hratt, en það elur á sniðgöngum og gremju þegar verkfærin hægja á fólki. Komdu með núverandi valfrjálst upptökuhlutfall, ánægjumerki og helstu núningspunkta sem teymi tilkynna í dag. Ef teymi myndu yfirgefa vettvanginn um leið og umboðið félli hefurðu ekki smíðað vöru, þú hefur smíðað stefnu.

4. **Þegar teymi nær jaðri gullinnar slóðar, hver er neyðarútgangurinn og hver ákveður hvort víkka eigi slóðina eða halda línunni?** Gullin slóð er studd, skoðanarík leið með skynsamleg sjálfgefin gildi og gildi hennar kemur af því að flest teymi haldist á henni, samt breytist slóð án útgöngu í hlið sem ýtir sannarlega óvenjulegri vinnu alveg af vettvanginum. Komið ykkur saman fyrirfram um hvernig teymi biður um frávik, hver rýnir það og hvernig þú greinir einstaka undantekningu frá merki um að slóðin sjálf eigi að breytast. Fyrir stóra skipulagsheild er þetta munurinn á vettvangi sem tekur við fjölbreytileika og einum sem sundrast í skuggaverkfæri um leið og teymi finnst það hindrað. Komdu með núverandi fjölda teyma sem hafa farið af slóðinni, ástæðurnar sem þau gáfu og hve lengi undantekning er að fá samþykki. Í fyrirtækja- og opinberu umhverfi skaltu tengja hvern neyðarútgang við reglufylgnistýringarnar sem hann sniðgengur, svo frávik frá troðnu slóðinni verði aldrei hljóðlega frávik frá öryggis- eða faggildingargrunnlínunni.

5. **Smíðið þið vettvanginn innanhúss eða kaupið hann og hafið þið heiðarlega verðlagt viðvarandi kostnað hvorrar leiðar?** Vettvangurinn er sjálfur vara með lífsferil og smíða-eða-kaupa valið setur kostnaðarskipulag þitt árum saman: innanhúsgátt passar nákvæmum þörfum þínum en krefst fjármagnaðs teymis til að viðhalda henni, á meðan keyptur vettvangur nær verðmæti hraðar á verði leyfa og passunar sem er aldrei fullkomin. Ákveddu hverjar getur eru nógu aðgreinandi til að smíða og hverjar eru staðlavara sem þú ættir að kaupa og endurskoðaðu þá línu eftir því sem seljendur þroskast. Fyrir stórt teymi er í húfi áhrifamáttur: rangt smíðaval sekkur knöppum eldri verkfræðingum í lagnavinnu sem vara hefði séð um, á meðan rangt kaupval læsir hundruðum forritara inn í vegvísi annars. Komdu með raunhæft heildarkostnaðarmat fyrir hvern kost, þar með talið viðhald, uppfærslur og útgöngukostnað. Í fyrirtækja- og opinberum innkaupum skaltu bæta við faggildingar- og gagnaflytjanleikaskilmálum og kjósa samninga sem leyfa þér að fara án þess að yfirgefa þjónustuskrána og stigakortin sem þú hefur smíðað ofan á.

6. **Hvernig er vettvangsteymið fjármagnað og stærðarsett miðað við forritarana sem það þjónar og hvað verður um það þegar fjárhagsáætlanir þrengjast?** Vettvangur vinnur sér inn sess með áhrifamætti, þar sem lítið teymi margfaldar framleiðni mun stærri hóps forritara, en sama rammun gerir hann auðvelt skotmark þegar fjármál leita niðurskurðar og ávinningurinn er dreifður frekar en eignaður einni vörulínu. Ákveddu fjármögnunarlíkanið, hlutfall vettvangsverkfræðinga á móti forriturunum sem þeir styðja og hvernig þú munt verja þá fjárfestingu með sönnunargögnum frekar en trú. Fyrir stóra skipulagsheild er undirfjármagnaður vettvangur verri en enginn: teymi treysta á hann, hann rotnar og núningurinn snýr aftur með ósjálfstæði áfast. Komdu með mannafla vettvangsins, upptöku- og ánægjuþróun hans og mat á forritaratímum endurheimtum yfir skipulagsheildina. Í opinberum og regluverkuðum fyrirtækjum skaltu ramma vettvanginn sem staðinn þar sem reglufylgni er kóðuð einu sinni, svo að skera hann sparar ekki peninga, hann dreifir úttektar- og öryggisvinnu aftur yfir hvert teymi sem þarf nú að gera hana í höndunum.

## Sjónarhorn eftir geirum

**Sprotafyrirtæki.** Með örfáa verkfræðinga og ekkert svigrúm skaltu ekki setja upp vettvangsteymi. Smíðaðu eina sniðmátshirslu fyrir gullna slóð sem ný þjónusta getur afritað og keyrt á klukkustund. Forstilltu hana með CI, gámasmíði, lint og heilsuathugun og láttu hana breiðast út því hún sparar greinilega tíma, ekki því einhver skipar það. Keyptu hverja staðlagetu sem þú getur, haltu verkfærakeðjunni lítilli og líttu á hugræna byrði, ekki þekju, sem það sem á að vernda.

**Lítið fyrirtæki.** Þú hefur engan sérstakan vettvangssérfræðing og þröngt fjárhagsáætlun, svo hallaðu þér að stýrðum vettvangi eða skoðanaríku skýjaboði frekar en að smíða innri þróunarvettvang sjálfur. Rammaðu ákvörðunina sem kaupa gegn smíða og sjálfgefðu kaup: keypt gátt og sniðmát hennar gefa alhæfum verkfræðingum þínum gullnar slóðir án teymis til að viðhalda þeim. Veldu verkfæri sem eru sjálfsafgreiðslu og auðvelt að yfirgefa, svo seljandaskipti strandi ekki örfáu þjónusturnar sem þú rekur.

**Stórfyrirtæki.** Stærð og mörg teymi gera eignasafnssamræmi að verðlaununum: fjármagnað vettvangsteymi, gullnar slóðir með varnarrimlum, sjálfsafgreiðsluútvegun, þjónustuskrá og stigakort sem gera eignarhald og gæði sýnileg yfir hundruð þjónusta. Rektu vettvanginn sem vöru sem vinnur sér valfrjálsa upptöku frekar en umboð sem elur á sniðgöngum og kóðaðu öryggi og reglufylgni einu sinni sem troðnar slóðir svo stjórnarhættir fylgi með sjálfgefið. Mældu þróunarupplifun með jafnvægum rammaverkum og verðu fjármögnun vettvangsins með endurheimtum forritaratímum.

**Hið opinbera.** Innkaupareglur, gagnsæi og opinber ábyrgð móta vettvanginn. Kóðaðu skyldubundnar öryggisstýringar og faggildingarkröfur sem varnarrimla meðfram gullnu slóðunum, svo teymi sem útvegar innviði gegnum sjálfsafgreiðslugáttina erfi umhverfi sem þegar uppfyllir stýringargrunnlínuna, sem breytir mánaðalangri handvirkri faggildingu í að mestu sjálfvirkt skref. Notaðu stigakort til að gefa eftirlitsaðilum samfellda, úttektarhæfa sýn á reglufylgnistöðu og krefstu gagnaflytjanleika og opinna viðmóta í innkaupum svo skráin og troðnu slóðirnar sem þú smíðar séu ekki læst við einn birgi.

## Dæmi

**Sprotafyrirtæki.** Tólf manna sprotafyrirtæki hefur ekkert vettvangsteymi, svo einn eldri verkfræðingur eyðir nokkrum föstudögum í að smíða eina „ný þjónusta“ sniðmátshirslu sem kemur forstillt með CI, Dockerfile, lint og heilsuathugun. Hver verkfræðingur getur afritað hana og haft þjónustu keyrandi í prófunarumhverfi innan klukkustundar, í stað þess að afrita stillingar úr eldra verkefni og giska á eyðurnar. Sniðmátið er gullna slóðin og því það sparar öllum greinilega tíma tekur allt teymið það upp án þess að nokkrum sé sagt það.

**Stórfyrirtæki.** Stórt tryggingafélag stofnar vettvangsteymi sem afhendir innri þróunargátt. Hún skráir hverja þjónustu með eiganda hennar, skjölum og heilsustigakorti. Nýjar þjónustur eru búnar til úr sniðmátum gullinnar slóðar sem koma forstillt með CI/CD, öryggisskönnun, vöktun og reglufylgniathugunum. Gagnagrunnar og umhverfi eru útveguð sjálfsafgreiðslu gegnum gáttina. Innleiðingartími nýs verkfræðings fellur úr vikum í daga og úttektarsönnunargögn eru framleidd sjálfvirkt því hver þjónusta fylgir sömu troðnu slóð. Upptaka vettvangsins er valfrjáls og hún breiðist út því teymi sem nota hann afhenda merkjanlega hraðar.

**Hið opinbera.** Alríkisstofnun sem rekur tugi stafrænna þjónusta setur upp sameiginlegan vettvang. Hún kóðar skyldubundnar öryggisstýringar og faggildingarkröfur sem varnarrimla meðfram gullnu slóðum sínum. Teymi sem útvegar innviði gegnum sjálfsafgreiðslugáttina erfir umhverfi sem þegar uppfyllir stýringargrunnlínuna. Það breytir mánaðalangri handvirkri faggildingaræfingu í að mestu sjálfvirka. Stigakort rekja reglufylgnistöðu hverrar þjónustu og gefa eftirlitsaðilum samfellda sýn án handvirkrar skýrslugerðar og losa knappt sérfræðistarfsfólk undan endurtekinni rýni.

## Viðskiptarök: hvatar, ávöxtun fjárfestingar og heildarkostnaður

Ávöxtun vettvangsverkfræði kemur af endurheimtum forritaratíma og áunnum samræmi. Þegar verkfræðingar eyða minni tíma í að berjast við innviði og leita upplýsinga fer meira af dýrum tíma þeirra í að skila vöruverðmæti. Hraðari innleiðing, færri tvíteknar lausnir og sjálfvirk reglufylgni þýðir allt mælanleg afkastageta og minni áhætta. Því vettvangurinn þjónar mörgum teymum hefur hver úrbót á honum áhrifamátt yfir alla skipulagsheildina.

Hvað heildareignarkostnað varðar er upptökukostnaðurinn raunveruleg, viðvarandi fjárfesting: fjármagnað vettvangsteymi, verkfæri (smíðuð eða keypt) og agi til að reka vettvanginn sem vöru með stöðugum umbótum. Kostnaður þess að taka ekki upp er dreifður en mikill: hvert teymi borgar sama innviðaskattinn aftur og aftur, ósamræmt öryggi og reglufylgni, hæg innleiðing og eldri verkfræðingar sem brenna út á leiðindavinnu. Fyrir forystu er málið best sett fram sem áhrifamáttur. Hóflegt, vel rekið vettvangsteymi margfaldar framleiðni mun stærri hóps forritara og það kóðar stjórnarhætti einu sinni í stað þess að treysta á að hvert teymi geri það rétt.

## Andmynstur og gildrur

- **Vettvangur þvingaður, ekki boðinn.** Að skylda vettvang sem forritarar mislíkar elur á sniðgöngum og gremju.
- **Fílabeinsturns vettvangsteymi.** Að smíða án þess að skilja raunverulegar þarfir forritara framleiðir verkfæri sem enginn vill.
- **Hlið í stað troðinna slóða.** Varnarrimlar sem hindra lögmæta vinnu ýta teymum til að sniðganga vettvanginn alveg.
- **Einn framleiðnimælikvarði.** Að minnka framleiðni í eina spilanlega tölu bjagar hegðun og rýrir traust.
- **Mæling sem eftirlit.** DevEx-mælikvarðar notaðir til að raða einstaklingum eyðileggja sálfræðilega öryggið sem vettvangurinn þarf.
- **Gullin slóð án neyðarútgangs.** Stífar slóðir sem geta ekki sveigst fyrir sannarleg jaðartilvik verða hindranir.
- **Undirfjármagnaður vettvangur.** Að líta á vettvanginn sem aukaverkefni sveltir hann og tryggir lélega upplifun.

## Þroskalíkan

**Stig 1: Upphaf.** Enginn vettvangur er til. Hvert teymi setur saman eigin verkfæri og innviði viðbragðsdrifið, með miklum miðadrifnum afhendingum, tvíteknum lausnum og mikilli hugrænni byrði. Hvert teymi leysir útvegun, útsetningu og reglufylgni á eigin spýtur, ósamræmt.

**Stig 2: Þróun.** Nokkur sameiginleg verkfæri, sniðmát og ræsihirslur birtast, oft smíðuð af áhugasömum verkfræðingi, en þau eru brotakennd og að hluta handvirk. Fáein teymi taka upp gullna slóð á meðan önnur hunsa hana, sjálfsafgreiðsla er takmörkuð og þróunarupplifun er ekki mæld, svo gildi vettvangsins hvílir á sögusögnum.

**Stig 3: Stöðlun.** Vettvangsteymi rekur skjalfestar gullnar slóðir, sjálfsafgreiðsluútvegun, þróunargátt með þjónustuskrá og stigakort, beitt um skipulagsheildina. Varnarrimlar fyrir öryggi, stefnu og reglufylgni eru innbyggðir í troðnu slóðirnar, svo staðlaða vinnuflæðið sé það löghlýðna og sömu venjur gildi yfir teymi frekar en að vera ólíkar eftir hópum.

**Stig 4: Stjórnun.** Vettvangurinn er mældur og stýrður með gögnum gegn grunnlínum. Upptaka, ánægja, tími-að-fyrstu-útsetningu, leiðtími og útsetningartíðni eru rakin með jafnvægum rammaverkum eins og SPACE og samanlögðum könnunar- og kerfismerkjum. Stigakortaniðurstöður nærast inn í rýni og hugræn byrði, innleiðingartími og endurheimtir forritaratímar eru vöktuð gegn markmiðum. Ákvarðanir um að fjárfesta í eða leggja niður getu hvíla á sönnunargögnum, ekki málflutningi.

**Stig 5: Samhæfing.** Vettvangurinn er þroskuð vara með mikla valfrjálsa upptöku, stöðugt bætt af endurgjöf forritara og mælikvörðum og samþætt öryggi, reglufylgni og afhendingarskipulagningu um skipulagsheildina. Gullnar slóðir aðlagast eftir því sem þarfir breytast, stjórnarhættir eru ósýnilegur eiginleiki staðlaða vinnuflæðisins og vettvangsteymið leggur reglulega niður, skiptir út og endurmarkar getur eftir því sem tæknin og skipulagsheildin þróast.

## Hugmyndir til umræðu

- Hvernig vinnið þið upptöku fyrir vettvang án þess að skylda hann og hvenær, ef nokkurn tímann, er umboð réttlætanlegt?
- Hvaða gullnu slóðir myndu skila teymum ykkar mestu gildi fyrst?
- Hvernig mælið þið þróunarupplifun án þess að hún finnist eins og eftirlit?
- Hvar ættu neyðarútgangar að vera til svo óvenjuleg teymi séu ekki neydd alveg af vettvanginum?
- Hver er rétt stærð og fjármögnunarlíkan fyrir vettvangsteymi miðað við forritarana sem það þjónar?
- Hvernig ákveðið þið hvað á að smíða innanhúss á móti kaupa fyrir þróunargáttina og verkfærin?

## Helstu atriði

- Rektu vettvanginn sem vöru sem vinnur sér upptöku með því að gera teymi raunverulega hraðari.
- Útvegaðu gullnar slóðir og troðnar slóðir sem gera rétta, örugga, löghlýðna háttinn að auðvelda hættinum.
- Veittu raunverulega sjálfsafgreiðslu svo teymi hætti að bíða eftir miðum og afhendingum.
- Notaðu gáttir, skrár og stigakort til að gera eignarhald, arkitektúr og gæði sýnileg.
- Mældu þróunarupplifun með jafnvægum rammaverkum eins og SPACE, aldrei einni spilanlegri tölu.
- Líttu á að minnka hugræna byrði sem meginmarkmið vettvangsins.

## Heimildir og frekari lestur

- Matthew Skelton and Manuel Pais, *Team Topologies*.
- Nicole Forsgren, Margaret-Anne Storey, Chandra Maddila, et al., "The SPACE of Developer Productivity" (paper).
- Nicole Forsgren, Jez Humble, and Gene Kim, *Accelerate*.
- Gregor Hohpe, *The Software Architect Elevator*.
- Camille Fournier, *The Manager's Path*.
- Cloud Native Computing Foundation, platform engineering white paper.
