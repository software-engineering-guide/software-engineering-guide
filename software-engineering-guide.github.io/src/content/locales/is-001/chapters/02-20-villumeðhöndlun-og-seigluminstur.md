# 2.20 Villumeðhöndlun og seigluminstur

## Yfirlit og tilgangur

Sérhvert forrit sem þú skrifar mun bila. Diskur fyllist, net rofnar, þjónusta rennur út á tíma, kallandi sendir drasl, ósjálfstæði skilar einhverju sem skjölin nefndu aldrei. Spurningin er aldrei hvort bilun gerist. Hún er hvort kóðinn þinn mætir bilun með áætlun eða með óvæntri uppákomu. Villumeðhöndlun er handverkið að ákveða, línu fyrir línu og aðgerð fyrir aðgerð, hvað kóðinn gerir þegar heimurinn vinnur ekki með. Þetta er minnst glæsilegi hluti smíðar og sá sem ræður, meira en nokkur eiginleiki, hvort fólk treystir kerfinu þínu.

Þessi kafli fjallar um seiglu á kóða- og íhlutastigi: valin innan aðgerðar, einingar eða API. Hann bætir við kafla 3.5, sem fjallar um seiglu á kerfisstigi (álagsdreifingu, afritun, yfirtöku milli þjónusta). Kafli 3.5 heldur öllum vettvanginum uppi þegar heilt svæði fer dimmt. Þessi kafli heldur einni beiðni frá því að spilla gögnum þínum eða hverfa án ummerkja. Þetta tvennt styrkir hvort annað. Rofi í arkitektúrnum þínum þýðir lítið ef kóðinn á bak við hann gleypir undantekningar, og varnarfull aðgerð getur ekki bjargað þér ef umlykjandi kerfið hefur enga offramleiðslu. Þessi kafli byggir líka á kafla 2.9 (hugbúnaðarsmíði), þar sem villumeðhöndlun var einn agi meðal margra. Hér verður hún allt efnið.

Fyrir stór teymi er samræmi verðlaunin. Þegar hundruð verkfræðinga meðhöndla villur á hundrað ólíka vegu verður sérhver þjónusta gáta og sérhvert atvik uppgröftur. Í fyrirtækjaumhverfi hækkar það ósamræmi kostnað hverrar úttektar og hverrar samþættingar. Í opinberum og öðrum hávirðiskerfum eru hagsmunirnir skarpari: réttleiki, örugg bilun og skýr úttektarslóð eru ekki eiginleikar sem þú bætir við síðar heldur eiginleikar sem kerfið verður að hafa frá fyrsta commit. Bótakerfi sem reiknar hljóðlega rangt, eða skrárkerfi sem missir bilun án þess að skrá hana, er ekki bara gallað. Það er óáreiðanlegt á hátt sem tærir stofnunina að baki því.

## Meginreglur

- Greindu milli galla, villna og bilana og meðhöndlaðu hvert á réttu lagi.
- Veldu hraðbilun eða öruggbilun af ásetningi, eftir samhengi, aldrei fyrir slysni.
- Gerðu villumeðhöndlunarsamning hverrar aðgerðar og API skýran og heiðarlegan.
- Staðfestu á mörkum, treystu innan þeirra, verðu án óhóflega varúðs.
- Gleyptu aldrei villu hljóðlega. Dragðu hana fram, vefðu hana eða meðhöndlaðu hana af ásetningi.
- Gerðu endurtekningar öruggar með eins-áhrifum, tímamörkum, undanhaldi og skjálfta.
- Gefðu villuleiðinni sömu hönnunarathygli og gleðileiðinni.

## Ráðleggingar

### Greindu milli galla, villna og bilana

Ónákvæmur orðaforði framleiðir ónákvæma meðhöndlun, svo byrjaðu á skýrum hugtökum. **Galli** (fault) er brestur í kerfinu: villa, röng stilling, ósjálfstæði sem er niðri. **Villa** (error) er rangt innra ástand sem gallinn framleiðir: núll þar sem gildi ætti að vera, staða sem afstemmist ekki lengur. **Bilun** (failure) er það sem utanaðkomandi áhorfandi sér: beiðnin skilar röngu svari, eða engu svari. Einn galli getur valdið mörgum villum og margar villur geta verið gripnar áður en nokkur verður að sýnilegri bilun. Allur tilgangur villumeðhöndlunar er að brjóta þá keðju, að grípa villuna áður en hún verður bilun sem notandinn eða endurskoðandinn upplifir.

Þessi orðaforði segir þér líka hvar á að bregðast við. Gallar eru teknir fyrir í rýni, prófunum og stillingu. Villur eru teknar fyrir í keyrslu með mynstrunum í þessum kafla. Bilanir eru teknar fyrir með sýnileika (kafli 9.2) og kerfisstigsseiglu kafla 3.5. Þegar teymið þitt deilir þessum orðum verða atvikarýni skarpari: þú getur sagt nákvæmlega hvar keðjan átti að vera rofin og var það ekki, frekar en að rökræða um hvað „gallinn“ var.

### Veldu hraðbilun eða öruggbilun eftir samhengi

[Hraðbilun](https://en.wikipedia.org/wiki/Fail-fast_system) þýðir að stoppa um leið og eitthvað er rangt, neita að halda áfram á slæmu ástandi svo vandinn birtist hátt og nálægt orsök sinni. Öruggbilun þýðir að skerðast í þekkt, skaðlaust ástand og halda áfram að þjóna því sem þú getur örugglega. Hvorugt er altækt rétt, og færnin er að velja eftir samhengi. Við þróun og á innri mörkum er hraðbilun vinur þinn: forrit sem stöðvast á brotinni fastayrðingu réttir þér stuttan kallstafla í stað langrar dulúðar. Í framleiðslu, á jöðrum notendasnúins kerfis, vinnur öruggbilun oft: meðmælaspjald sem skilar engu er betra en afgreiðslusíða sem hleðst ekki.

Ákveddu þetta af ásetningi fyrir hver mörk og skrifaðu ákvörðunina niður. Flugstýringar- eða lækningatækjaíhlutur bilar öruggt í skilgreint ástand því að halda áfram á spilltum gögnum gæti skaðað einhvern. Höfuðbókarfærsla bilar hratt því að bóka ranga færslu er verra en að bóka enga. Röng paring er hættuleg í báðar áttir: öruggbilun þar sem þú þurftir hraðbilun felur spillingu, og hraðbilun þar sem þú þurftir öruggbilun breytir snyrtilegri hiksta í rekstrarrof.

### Veldu villumerkjabúnað og notaðu hann samræmt

Tungumál gefa þér tvær víðar leiðir til að gefa til kynna að eitthvað hafi farið úrskeiðis. [Undantekningarmeðhöndlun](https://en.wikipedia.org/wiki/Exception_handling) kastar hlut upp kallstaflann þar til einhver meðhöndlari grípur hann, sem aðskilur villuleiðina frá aðalrökfræðinni. Valkosturinn eru skýr villugildi: aðgerðin skilar bæði niðurstöðu og villu, og kallandi verður að skoða hvort tveggja. Mörg nútímatungumál formgera hið síðara með [Result-gerð](https://en.wikipedia.org/wiki/Result_type), oft kölluð Result eða Either, sem neyðir kallandann til að taka upp annaðhvort árangur eða bilun áður en hann notar gildið. Hvor nálgun hefur kostnað. Undantekningar halda gleðileiðinni hreinni en geta falið stýriflæði og freistað hönnuða í catch-all blokkir sem þurrka út upplýsingar. Skýrar niðurstöður gera hverja bilun sýnilega í tagaundirskriftinni en bæta við helgisið og er hægt að hunsa ef tungumálið neyðir ekki athugunina.

Rétta svarið snýst minna um hvaða búnað en um samræmi og heiðarleika. Veldu málvenjuna sem tungumál þitt og vistkerfi kjósa og beittu henni einsleitt yfir þjónusturnar þínar svo lesandi viti alltaf hvernig bilun ferðast. Taktu frá undantekningar fyrir raunverulega undantekningarkennd skilyrði, ekki venjulegt stýriflæði eins og „notandi fannst ekki“, sem er betur mótað sem venjuleg niðurstaða. Hvað sem þú velur skaltu aldrei láta bilun verða ósýnilega: óathugað villugildi er jafn hættulegt og tóm catch-blokk. Í stórum kóðagrunni slær skrifleg venja auk lint-tóls sem merkir hunsaðar villur hvaða einstaklingskjör sem er.

### Gerðu villumeðhöndlunarsamninginn skýran

Sérhver aðgerð og sérhvert API hefur villumeðhöndlunarsamning, hvort sem nokkur skrifaði hann niður eða ekki. Hann svarar: hvað getur farið úrskeiðis hér, hvernig munt þú frétta af því og hvað er tryggt um ástand þegar það gerist? Gerðu þann samning skýran. Skjalfestu hvaða villur aðgerð getur skilað eða kastað, greindu endurheimtanlegar villur (kallandi getur skynsamlega reynt aftur eða fallið til baka) frá óendurheimtanlegum (kallandi getur ekki lagað þetta og ætti að bera áfram eða hætta) og segðu hvort aðgerðin skilur ástand eftir óbreytt við bilun. Þessi síðasti eiginleiki, stundum kallaður sterka undantekningarábyrgðin, þýðir að bilað kall er eins og það hafi aldrei gerst, sem er einmitt það sem lætur kallanda reyna aftur örugglega.

Fyrir opinbert API eða API milli teyma er þessi samningur hluti viðmótsins, jafn raunverulegur og stikugerðirnar. Hannaðu lítið, stöðugt villuflokkunarkerfi: afmarkað safn flokka eins og staðfestingarvilla, fannst ekki, árekstur, óheimilað, ósjálfstæði-óaðgengilegt og innri villa. Kallendur geta þá greinst eftir flokki án þess að þátta strengi. Skýrt flokkunarkerfi gerir villumeðhöndlun samsetjanlega yfir margar þjónustur og gerir bilanir úttektarhæfar, því sérhver bilun kortleggst á þekkta, nefnda tegund.

### Staðfestu á mörkum og verðu án óhóflega varúðs

Líttu á gögn sem fara yfir traustmörk (netbeiðni, skrá, notendainntak, skilaboð frá annarri þjónustu) sem fjandsamleg þar til þau eru staðfest, og staðfestu þau á mörkunum, einu sinni, vandlega. Þetta er [varnarforritun](https://en.wikipedia.org/wiki/Defensive_programming) beitt með dómgreind. Innan einingar þar sem þú hefur þegar staðfest inntök fela óþarfar athuganir á hverri línu rökfræðina og bæla niður einmitt bilanirnar sem þú vildir sjá. Agi er: verðu fast á jöðrunum, treystu innan þeirra. Staðfestu uppbyggingu, svið og fastayrðingar þar sem gögn koma inn, breyttu þeim í gerðir sem gera ólögleg ástönd óframsetjanleg og láttu innri kóða gera ráð fyrir að hann vinni með hrein gögn.

Óhófleg varúð hefur raunverulegan kostnað. Kóði kæfður í núll-athugunum og varnargreinum er erfiðari að lesa, og verra, hann breytir oft skýrri bilun í hljóðan axlayppting, skilar sjálfgefnu gildi þar sem hann hefði átt að gefa viðvörun. Vörn sem hylur galla er ekki öryggi. Hún er frestun.

### Gerðu endurtekningar öruggar, afmarkaðar og kurteisar

Margir gallar eru tímabundnir: augnabliks netblik, þjónusta að endurræsa, stutt lásasamkeppni. Í hverju dreifðu kerfi (kafli 3.3) eru þessar hlutabilanir venjulega tilvikið frekar en undantekningin. Að reyna aftur er eðlilega viðbragðið, en barnaleg endurtekningarlykkja er hlaðin byssa. Fyrst skaltu gera aðgerðina sem þú reynir aftur [eins-áhrifa](https://en.wikipedia.org/wiki/Idempotence), sem þýðir að að framkvæma hana tvisvar hefur sömu áhrif og að framkvæma hana einu sinni. Án eins-áhrifa getur endurtekning eftir tímamörk gjaldfært kort tvisvar eða búið til tvær færslur, því þú getur ekki sagt hvort fyrsta tilraunin mistókst eða aðeins kvittun hennar tapaðist. Notaðu eins-áhrifalykla fyrir skrif svo móttakandi geti þekkt og afritunarhreinsað endurtekningu.

Í öðru lagi skaltu setja tímamörk á hvert fjarkall svo hangandi ósjálfstæði geti ekki hengt þig. Í þriðja lagi skaltu dreifa endurtekningum með [veldisundanhaldi](https://en.wikipedia.org/wiki/Exponential_backoff), tvöfalda biðina eftir hverja tilraun, og bæta við skjálfta (lítilli slembitöf) svo þúsund biðlarar sem jafna sig í einu samstillist ekki í hjörðarhlaup sem slær batnandi þjónustuna aftur niður. Í fjórða lagi skaltu setja þak á fjölda endurtekninga og heildartímann og gefast síðan upp mjúklega. Endurtekningar án marka, undanhalds, skjálfta og eins-áhrifa eru ein algengasta leiðin sem lítill hiksti verður að sjálfskaðandi rekstrarrofi.

### Bættu við rofum, skilrúmum og mjúkri skerðingu í kóða

Þegar ósjálfstæði er raunverulega niðri sóar að reyna það aftur fyrirhöfn og dýpkar holuna. [Rofi](https://en.wikipedia.org/wiki/Circuit_breaker_design_pattern) (circuit breaker) fylgist með bilanahlutfalli kalla á ósjálfstæði og „opnast“, þegar bilanir fara yfir þröskuld, til að bila strax í kælitíma frekar en að bíða eftir dæmdum köllum. Eftir kælitímann hleypir hann prufukalli í gegn og lokast aftur ef ósjálfstæðið hefur jafnað sig. Þetta ver bæði kallendur þína (hraðar, fyrirsjáanlegar bilanir í stað hrúgaðra tímamarka) og ósjálfstæðið sem á í erfiðleikum (andrými til að jafna sig). Skilrúmsmynstrið (bulkhead), nefnt eftir vatnsheldum hólfum skips, einangrar tilföng svo eitt mettað ósjálfstæði geti ekki étið hvern þráð eða tengingu og sökkt öllu ferlinu. Þú gefur hverju ósjálfstæði sinn eigin takmarkaða sjóð.

Þessi mynstur para sig við mjúka skerðingu á kóðastigi: þegar ónauðsynlegt ósjálfstæði er óaðgengilegt skaltu skila skertri en gagnlegri niðurstöðu í stað villu. Sýndu skyndiminnisgögn með úreldingarathugasemd, feldu sérsniðna spjaldið, settu skrifið í biðröð til síðari tíma. Þetta er staðbundna viðbótin við kerfisstigsseiglu kafla 3.5: arkitektúrinn veitir offramleiðslu yfir vélar og kóðinn þinn veitir skynsama hegðun þegar hluta vantar.

### Vefðu villur með samhengi og gleyptu þær aldrei

Villa sem les „tenging hafnað“ tíu lögum fyrir ofan þar sem hún gerðist er næstum gagnslaus. Þegar villa berst áfram skaltu vefja hana með samhengi: hvað þú varst að reyna að gera, hvaða eining eða beiðni, hvaða ósjálfstæði, á meðan þú varðveitir upprunalegu orsökina svo rótin tapist ekki. Góð tungumál og bókasöfn styðja þessa villukeðjun beint. Markmiðið er að ein skráarlína segi bakvaktarverkfræðingnum hvað brást, við hvaða aðgerð, fyrir hvaða inntak. Þetta er hráefnið í sýnileika kafla 9.2 og villuleit kafla 2.15.

Höfuðsyndin er að gleypa villu: tóm catch-blokk, hunsað skilagildi, `catch` sem skráir á villuleitarstigi og heldur áfram eins og ekkert hafi gerst. Gleypt villa hverfur ekki. Hún kemur aftur síðar sem spillt gögn eða óútskýranlegur galli, nú aðskilin frá orsök sinni. Sérhver villa verður að mæta einu af þremur örlögum: meðhöndla hana (jafna sig eða skerðast), vefja og bera hana áfram eða, efst í staflanum, skrá hana með fullu samhengi og bila. Ef þú grípur villu og gerir ekkert af þessu hefurðu valið að fela framtíðaratvik fyrir framtíðarsjálfinu þínu.

## Málamiðlanir: kostir og gallar

| Nálgun | Kostir | Gallar |
|---|---|---|
| Undantekningar | Hrein gleðileið, erfitt að hunsa ef óathugað | Falið stýriflæði, freistar catch-all útþurrkunar |
| Skýr villugildi / Result-gerðir | Bilun sýnileg í undirskrift, neyðir meðhöndlun | Meiri helgisiður, hægt að hunsa án framfylgdar |
| Hraðbilun | Dregur fram galla hátt, nálægt orsök | Léleg notendaupplifun ef notað á jaðrinum |
| Öruggbilun | Heldur áfram að þjóna, ver notendur og gögn | Getur hulið spillingu ef notað þar sem þurfti hraðbilun |
| Endurtekningar með undanhaldi | Rífur sig sjálfvirkt gegnum tímabundna galla | Magnar álag og tvöfalt skrif án eins-áhrifa |
| Rofi | Hraðar bilanir, leyfir ósjálfstæðum að jafna sig | Aukaástand og stilling, getur hulið viðvarandi vanda |
| Varnarstaðfesting á mörkum | Grípur slæm gögn snemma, einu sinni, hátt | Ofgert ringlar það rökfræði og felur raunverulegar bilanir |

Meginspennan er sýnileiki gegn hávaða. Meðhöndlaðu villur of hljóðlega og þú felur vandamál þar til þau eru dýr. Meðhöndlaðu þær of hátt og alls staðar og þú drekkir merkinu í helgisið og hylur bilanirnar sem skipta máli. Leystu það eftir staðsetningu og ásetningi. Vertu hávær og strangur á mörkum, þar sem slæm gögn og ósjálfstæðisbilanir koma inn. Vertu hljóður og traustur í innri, þar sem inntök eru þegar hrein. Ákveddu hraðbilun á móti öruggbilun fyrir hver mörk og skrifaðu það niður. Markmiðið er kóði þar sem sérhver bilun hefur nákvæmlega einn skýran eiganda og eitt skýrt örlag og ekkert fellur hljóðlega milli rifa.

## Spurningar til að ræða með teyminu

1. **Höfum við eitt sameiginlegt villuflokkunarkerfi og villumeðhöndlunarvenju yfir þjónusturnar okkar, eða spinnur hvert teymi?** Í stóru teymi er þetta munurinn á bilunum sem samsetjast og bilunum sem rugla. Þegar ein þjónusta skilar HTTP 500 fyrir staðfestingarvandamál, önnur kastar tagaðri undantekningu og þriðja skilar null, verður sérhver samþætting samningaviðræður og sérhvert atvik þýðingaræfing. Komdu með dæmi um sömu rökrænu bilun, segjum „færsla fannst ekki“, eins og hún birtist yfir þrjár af þjónustum þínum og sjáðu hve ólíkt þær gefa hana til kynna. Svarið ætti að verða skrifaður staðall: afmarkað safn villuflokka, samræmd leið til að gefa þá til kynna og lint-tól eða rýnigátlisti sem framfylgir því. Samræmi hér borgar sig í hverri framtíðarsamþættingu, úttekt og bakvakt.

2. **Fyrir hver mikilvæg mörk, höfum við valið hraðbilun eða öruggbilun af ásetningi og passar kóðinn við það val?** Flest teymi hafa aldrei tekið þessa ákvörðun skýrt, sem þýðir að hún var tekin fyrir þau af þeim sem skrifaði kóðann fyrst og ósamræmt. Sjónarmiðin sem togast á eru raunveruleg: að bila örugglega heldur notendum þjónustuðum en getur látið spillingu breiðast út, á meðan að bila hratt ver gögn en getur breytt minniháttar ósjálfstæðisrofi í sýnilega bilun. Komdu með atvikasögu þína og spurðu, fyrir þau verstu, hvort kóðinn hafi brugðist eins og þú hefðir valið ef spurður fyrirfram. Sönnunargögnin sem þú vilt eru kort af mörkum þínum með yfirvegaðan merkimiða á hverju, sérstaklega hvar sem peningar, öryggi eða borgaraskrár koma við sögu. Þar sem merkimiðinn og kóðinn eru ósammála hefurðu fundið næstu lagfæringu.

3. **Hvenær æfðum við villuleið af ásetningi síðast og hegðaði hún sér eins og hönnuð?** Villuleiðin er venjulega minnst prófaði kóðinn sem þú átt, en samt er hún þar sem traust vinnst eða tapast, og „við bilum örugglega“ er fullyrðing sem þú getur ekki staðið við ef þú hefur aldrei horft á það gerast. Endurtekningarlykkja án eins-áhrifa, rofi með röngum þröskuldi, gleypt undantekning í sjaldan heimsóttri grein: þetta felur sig þar til raunverulegt atvik finnur þau fyrir þig. Komdu með niðurstöður af því að sprauta bilun vísvitandi (drepið ósjálfstæði, framkölluð tímamörk, ranghannað hleðsla) inn í raunhæft umhverfi. Aðgerðin sem fylgir er að gera bilanainnsprautun að rútínu, svo endurheimt, skerðing og öruggbilunarhegðun sé sannreynd stöðugt en ekki vonast til. Sérhver villuleið sem þú hefur aldrei kallað fram er loforð sem þú hefur ekki prófað.

4. **Hver af skrifaðgerðum okkar eru eins-áhrifa og hvar myndi endurtekning eftir týnda kvittun tvítaka raunveruleg áhrif eins og greiðslu eða færslu?** Endurtekning er algengasta seigluviðbragðið og, gert kæruleysislega, algengasta leiðin sem tímabundið blik breytist í tvöfalda peninga eða gögn. Í stóru teymi býr endurtekningarrökfræði oft í sameiginlegum biðlurum, millihugbúnaði og einstökum þjónustum öllum í einu, svo ein skrif geta verið reynd aftur á nokkrum lögum án þess að nokkur eigi heildarhegðunina. Togið á móti er að eins-áhrifalyklar, afritunarhreinsun og geymdar beiðniniðurstöður bæta við geymslu og kóða, og teymi undir afhendingarþrýstingi sleppa þeim fyrir skrif sem þau gera ranglega ráð fyrir að séu örugg. Komdu með skrá yfir utanaðkomandi sýnileg skrif þín, hvert merkt fyrir hvort það beri eins-áhrifalykil og hvernig móttakandi þekkir og afritunarhreinsar endurtekningu. Í fyrirtækja- og opinberu umhverfi skaltu merkja þau sem færa peninga eða breyta skrá borgara fyrst, því tvöföld greiðsla eða tvítekin bót er úttektarniðurstaða og stundum lagaleg útsetning, ekki bara galli.

5. **Koma tímamörk okkar, rofar og skilrúm úr einu sameiginlegu, prófuðu bókasafni, eða handsmíðar hvert teymi þau?** Þessi mynstur eru auðveld að lýsa og auðvelt að fá lúmskt röng: vantandi tímamörk, rofaþröskuldur sem aldrei sleppur, tengingasjóður í stærð sem lætur eitt hægt ósjálfstæði svelta allt ferlið. Þegar hvert teymi útfærir þau aftur safnarðu mörgum örlítið biluðum afritum og engum einum stað til að laga galla einu sinni þegar þú finnur hann. Sjónarmiðið á móti er að sameiginlegt bókasafn leggur á sameiginlegt viðmót og uppfærslutakt, og teymi með óvenjuleg keyrsluumhverfi eða tafarþarfir kunna að hnýta í það eða fara framhjá því. Komdu með könnun á því hve margar ólíkar endurtekninga-og-rofa útfærslur keyra í raun í framleiðslu og hvaða þjónustur hafa enn engin tímamörk á útleiðandi köllum sínum. Fyrir stórt fyrirtæki eða stofnun gefur vottað sameiginlegt bókasafn líka öryggisrýnum og endurskoðendum einn íhlut til að votta frekar en tugi, sem lækkar kostnað hverrar rýni.

6. **Ef atvik gerðist í nótt, gæti hver bakvaktarverkfræðingur sem er rakið það úr einni skráarlínu og gæti endurskoðandi síðar séð hverja bilun sem kerfið skráði?** Vafin, flokkuð, vel skráð villa er munurinn á tíu mínútna greiningu og miðnæturuppgreftri, og gleypt villa er framtíðaratvik sem þú hefur falið fyrir sjálfum þér. Í stóru teymi fara bilanir yfir mörg þjónustuhopp, svo gildið kemur af samræmdu samhengi og fylgnaauðkennum sem lifa þau hopp, ekki af kostgæfni neins eins teymis. Spennan á móti er kostnaður og hávaði: skráðu allt og þú drekkir merkinu og borgar fyrir að geyma það. Skráðu of lítið og þú getur ekki endurgert hvað gerðist. Komdu með raunverulega nýlega bilun og gakktu slóð hennar frá enda til enda, taktu eftir hverju hoppi þar sem samhengi tapaðist eða villa var gripin og fleygt. Í eftirlitsskyldum og opinberum kerfum skaltu líta á þetta sem regluvörslueiginleika, því óúttektarhæf bilun, eða ákvörðun sem þú getur ekki útskýrt árum síðar, er lagaleg útsetning en ekki bara rekstrarbil.

## Sjónarhorn eftir geirum

**Sprotafyrirtæki.** Með handfylli verkfræðinga og ekkert svigrúm skaltu eyða villumeðhöndlunarfjárhagsáætlun þinni þar sem bilun kostar þig viðskiptavin eða gögn þín: settu tímamörk á hvert útleiðandi kall, gerðu peningaflutningsskrif eins-áhrifa og bættu við lint-reglu gegn hunsuðum villum. Slepptu íburðarmiklum ramma. Result-gerð fyrir kjarnaaðgerðir og mjúk skerðing á ónauðsynlegum ósjálfstæðum kaupa mestallt öryggið fyrir fáa daga vinnu. Bilaðu hratt við þróun svo gallar birtist hátt og standastu freistinguna að handsmíða rofa áður en þú hefur í raun ósjálfstæði sem réttlætir einn.

**Lítið fyrirtæki.** Án seigluúrskurðarsérfræðings á launaskrá og með þröngt fjárhagsáætlun skaltu hallast að því sem tungumál þitt, rammi og skýjaveitandi gefa þér þegar frekar en að smíða mynstur frá grunni: stýrðar biðraðir, endurtekningar veitanda megin og bókasafnstímamörk ná yfir meira en flest teymi búast við. Rammaðu ákvörðunina sem kaupa á móti smíða og keyptu hvar sem þroskað ósjálfstæði meðhöndlar endurtekningar, undanhald og eins-áhrif fyrir þig. Einbeittu af skornum skammti athygli þinni að einum eða tveimur mörkum þar sem röng eða týnd færsla myndi raunverulega skaða og tryggðu að þau bili örugglega og skilji eftir spor.

**Stórfyrirtæki.** Yfir mörg teymi eru verðlaunin samræmi: eitt sameiginlegt villuflokkunarkerfi, sameiginlegt bókasafn fyrir tímamörk, endurtekningar, rofa og skilrúm og lint-tól og rýnigátlisti sem framfylgja þeim í leiðslunni. Færðu hverja villu í sameinaðan sýnileikavettvang með fylgnaauðkennum svo bilun sé rekjanleg yfir þjónustuhopp og staðlaðu hraðbilunar-á-móti-öruggbilunar ákvarðanir fyrir hver mörk svo úttektir finni skjalfest, rökstutt mynstur frekar en dreifingu staðbundinna venja. Stýrðu sameiginlega bókasafninu sem raunverulegri vöru, því galli lagaður þar einu sinni er galli lagaður alls staðar.

**Hið opinbera.** Réttleiki, örugg bilun og varanleg úttektarslóð eru skyldur, ekki kjör. Bilaðu hratt á hverri brotinni fastayrðingu sem snertir peninga eða hæfi, staðfestu hvert borgarasnúið inntak á mörkum og skrifaðu hverja bilun í óbreytanlega skrá með nægu samhengi til að hægt sé að útskýra og rýna ákvörðun árum síðar. Innkaup og langir kerfislíftímar þýða að villusamningar verða að vera skjalfestir svo ríkisstarfsmenn geti viðhaldið kóðanum löngu eftir að upphaflegir höfundar eru farnir, og allur íhlutur söluaðila verður að afhjúpa bilunarhegðun sína frekar en fela hana á bak við ógagnsætt viðmót.

## Dæmi

**Sprotafyrirtæki.** Fjögurra manna sprotafyrirtæki afhendir forrit sem kallar á þriðja aðila greiðsluveitanda og tölvupóstþjónustu. Snemma bæta þau við barnalegri endurtekningarlykkju og tvígjaldfæra viðskiptavin strax þegar tímamörk fela vel heppnaða gjaldfærslu. Lagfæringin kennir lexíuna: þau bæta eins-áhrifalyklum við hvert skrif, setja tímamörk á hvert útleiðandi kall og skipta yfir í veldisundanhald með skjálfta. Þau taka upp Result-gerð fyrir kjarnaþjónustuaðgerðir svo bilun birtist í undirskriftinni og lint-regla merkir hverja hunsaða villu. Þegar tölvupóstsending bilar skerðist afgreiðsla mjúklega með því að setja skilaboðin í biðröð í stað þess að hindra söluna. Agin kostar fáa daga og sparar þeim flokk atvika sem hefðu kostað miklu meira í endurgreiðslum og trausti.

**Stórfyrirtæki.** Alþjóðlegt flutningafyrirtæki rekur hundruð þjónusta og staðlar villumeðhöndlun yfir þær allar. Sérhver þjónusta kortleggur bilanir á sameiginlegt flokkunarkerfi (staðfesting, fannst ekki, árekstur, ósjálfstæði-óaðgengilegt, innri) svo kallendur greinist eftir flokki en ekki með því að þátta skilaboð. Sameiginlegt bókasafn veitir rofa, afmarkaðar endurtekningar með undanhaldi og skjálfta og skilrúmuð tengingasjóði, svo enginn handsmíðar þessi mynstur rangt. Sérhver villa er skráð með fylgnasamhengi sem nærir sýnileikavettvang kafla 9.2, svo bakvaktarverkfræðingur geti rakið bilun yfir þjónustuhopp úr einni línu. Því staðallinn er einsleitur og framfylgt í leiðslunni færast verkfræðingar af öryggi yfir ókunnar þjónustur og endurskoðendur geta séð að sérhver bilun er skráð, flokkuð og rekjanleg.

**Hið opinbera.** Landsbundin bótastofnun smíðar hæfis- og greiðslukerfi þar sem rangt svar getur neitað einhverjum um húsaleigu eða ofgreitt úr opinberum sjóði. Réttleiki og örugg bilun eru óumsemjanleg, svo kóðinn bilar hratt á hverri brotinni fjárhagsfastayrðingu: útreikningur sem getur ekki afstemmst neitar að bóka frekar en að bóka ranga tölu. Sérhvert borgarasnúið inntak er staðfest á mörkum og ólögleg ástönd eru gerð óframsetjanleg í lénsgerðunum. Sérhver bilun er skrifuð í óbreytanlega úttektarskrá með fullu samhengi, sem fullnægir lagakröfunni um að ákvarðanir séu útskýranlegar og rýnanlegar árum síðar. Þar sem ónauðsynlegt ósjálfstæði eins og skjalaforskoðun er niðri skerðist kerfið mjúklega svo sakamaður geti enn unnið úr kröfunni. Nýir ríkisstarfsmenn erfa kóða með skjalfestum villusamningum, svo þeir geti viðhaldið honum örugglega löngu eftir að upphaflegir höfundar hafa haldið áfram.

## Viðskiptarök: hvatar, ávöxtun fjárfestingar og heildarkostnaður

Ávöxtun agaðrar villumeðhöndlunar birtist sem færri atvik, styttri atvik og ódýrari atvik. Flest framleiðslurekstrarrof eru ekki framandi. Þau rekja sig til gleyptrar undantekningar, vantandi tímamarka, endurtekningarstorms eða marka sem treystu gögnum sem þau hefðu átt að staðfesta. Hvert er hægt að koma í veg fyrir með mynstrunum hér, og hvert forðað atvik sparar ekki aðeins beinan kostnað niðurtíma heldur samanlagðan kostnað neyðarviðbragða, viðskiptavinaflótta og rannsóknar. Því vafin, vel skráð villa má greina á mínútum frekar en klukkustundum lækkar meðaltími til endurheimtar, og bilanahlutfall breytinga lækkar með þegar verkfræðingar hætta að óttast villuleiðina.

Upptökukostnaðurinn er hóflegur og aðallega einskiptis. Þú skrifar niður villuflokkunarkerfi, útvegar sameiginlegt bókasafn fyrir endurtekningar og rofa svo teymi finni þá ekki upp illa, bætir við lint-reglum gegn hunsuðum villum og byggir upp venju bilanainnsprautunar. Kostnaður vanrækslu safnast hljóðlega upp: gleyptar villur safnast í spillt gögn sem eru dýr að rekja upp og ósamræmd meðhöndlun margfaldar kostnað hverrar samþættingar og hverrar úttektar. Í eftirlitsskyldu og opinberu umhverfi er óúttektarhæf bilun regluvörslu- og lagaleg útsetning, ekki bara verkfræðivandamál. Til að færa rök við forystu skaltu tengja villumeðhöndlunaraga við mælikvarðana sem hún fylgist þegar með: atvikatíðni, meðaltíma til endurheimtar, bilanahlutfall breytinga og úttektarniðurstöður.

## Andmynstur og gildrur

- **Hljóð gleyping:** tómar catch-blokkir og hunsuð skilagildi sem breyta bilun í seinkað, aðskilið dularmál.
- **Catch-all útþurrkun:** víð `catch` sem skráir almenn skilaboð og fleygir upprunalegu villunni og samhengi hennar.
- **Endurtekning án eins-áhrifa:** að keyra ekki-eins-áhrifa skrif aftur eftir tímamörk, tvígjaldfæra eða tvítaka færslur.
- **Endurtekningarstormar:** ekkert undanhald, enginn skjálfti og ekkert þak, svo biðlarar samstillast og berja batnandi ósjálfstæði aftur niður.
- **Engin tímamörk:** ótakmörkuð fjarköll sem láta eitt hangandi ósjálfstæði éta þræði og frysta allt ferlið.
- **Undantekningar sem stýriflæði:** að kasta og grípa fyrir venjulegar niðurstöður eins og „fannst ekki“, sem felur rökfræði og hægir á kóða.
- **Varnaróhóflega varúð:** athuganir á hverri línu sem grafa rökfræðina og breyta raunverulegum bilunum í hljóð sjálfgefin gildi.
- **Strengjagerðar villur:** kallendur þátta villuskilaboðatexta því það er ekkert stöðugt, flokkað flokkunarkerfi til að greinast á.
- **Öruggbilun þar sem þú þurftir hraðbilun:** að halda áfram á spilltu ástandi í kerfi þar sem rangt svar er verra en ekkert.

## Þroskalíkan

- **Stig 1, Upphaf:** Villumeðhöndlun er ad hoc og viðbragðsdrifin, ákveðin á hvern hönnuð. Tómar catch-blokkir og hunsuð skilagildi eru algeng, endurtekningar eru barnalegar, tímamörk vantar og bilanir birtast sem spillt gögn eða dularfullir gallar án samræmdrar skráningar.
- **Stig 2, Þróun:** Teymi taka upp grunnvinnubrögð, en ósamræmt. Villur eru skráðar með nokkru samhengi, augljós gleyping er letjuð í rýni og tímamörk og einfaldar endurtekningar eru til, en venjur eru ólíkar milli þjónusta, eins-áhrif eru götótt og villuleiðin er sjaldan prófuð.
- **Stig 3, Stöðlun:** Sameiginlegt villuflokkunarkerfi og villumeðhöndlunarvenja eru skjalfest og framfylgt um alla skipulagsheildina. Mörkastaðfesting, eins-áhrifa endurtekningar með undanhaldi og skjálfta, rofar, skilrúm og villuvefjun eru staðlað, veitt af sameiginlegum bókasöfnum og sérhver villa nærir sameinaða sýnileikaleiðslu.
- **Stig 4, Stjórnun:** Villumeðhöndlunarhegðun er mæld gegn grunnlínum og stýrð með gögnum. Endurtekningarhlutföll, rofasleppingar, tímamarkatalningar, gleyptar-villu niðurstöður úr kyrrstæðri greiningu, meðaltími til endurheimtar og bilanahlutfall breytinga eru rakin fyrir hverja þjónustu. Rofaþröskuldar og tímamörk eru stillt út frá mældri töf og bilanagögnum frekar en giskað. Bilanainnsprautun keyrir á áætlun, og teymi rýna þessa mælikvarða til að grípa afturfarir og halda hverju hraðbilunar- eða öruggbilunarvali við sönnunargögn.
- **Stig 5, Samhæfing:** Seigla er samþætt afhendingar- og áhættuáætlun og stöðugt bætt. Flokkunarkerfið, sameiginlegu bókasöfnin og staðlarnir þróast af hverju atviki, glundroða- og bilanainnsprautunartilraunir eru rútína og skipulagsheildin aðlagar tímamörk, rofaþröskulda, skerðingarstefnur og markaákvarðanir eftir því sem umferð, ósjálfstæði og áhættumynd breytast.

## Hugmyndir til umræðu

1. Hvar í kóðagrunninum þínum er villa gleypt núna og hvernig myndirðu vita ef þú hefðir rangt fyrir þér um að hún sé það ekki?
2. Hverjar af skrifaðgerðum þínum eru eins-áhrifa og hverjar myndu tvíkeyrast ef endurtekning kviknaði eftir týnda kvittun?
3. Ætti „notandi fannst ekki“ að vera undantekning, villugildi eða venjuleg niðurstaða og svarar teymið þitt því samræmt?
4. Hver er raunveruleg regla þín um hvar staðfesting gerist og geturðu bent á mörk sem treysta gögnum sem þau ættu ekki?
5. Hvernig ákveðurðu þröskuld og kælitíma rofa og hvernig myndirðu vita að núverandi stillingar eru rangar?
6. Ef endurskoðandi bæði um að sjá hverja bilun sem kerfið þitt upplifði síðasta mánuð, gætirðu framleitt hana, flokkaða og með samhengi?

## Helstu atriði

- Greindu galla, villur og bilanir og brjóttu keðjuna áður en innri villa verður að sýnilegri bilun.
- Veldu hraðbilun eða öruggbilun af ásetningi fyrir hver mörk og gerðu villumeðhöndlunarsamning hverrar aðgerðar skýran.
- Staðfestu fast á traustmörkum og treystu innan þeirra. Vörn sem hylur bilanir er frestun, ekki öryggi.
- Gerðu endurtekningar öruggar með eins-áhrifum, tímamörkum, veldisundanhaldi og skjálfta og bættu við rofum og mjúkri skerðingu í kóða.
- Vefðu villur með samhengi, færðu þær í sýnileika og gleyptu þær aldrei. Sérhver villa verður að vera meðhöndluð, borin áfram eða skráð og dregin fram.

## Heimildir og frekari lestur

- Michael T. Nygard, *Release It! Design and Deploy Production-Ready Software*
- Andrew Hunt and David Thomas, *The Pragmatic Programmer*
- Steve McConnell, *Code Complete: A Practical Handbook of Software Construction*
- Betsy Beyer, Chris Jones, Jennifer Petoff, and Niall Richard Murphy (eds.), *Site Reliability Engineering: How Google Runs Production Systems*
- Marc Brooker, "Timeouts, Retries, and Backoff with Jitter," Amazon Builders' Library
- Martin Fowler, "CircuitBreaker," martinfowler.com
- Nassim Nicholas Taleb, *Antifragile: Things That Gain from Disorder*
