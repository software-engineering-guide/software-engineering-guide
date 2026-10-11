# 7.1 Gagnastefna og gagnastjórnun

## Yfirlit og tilgangur

Gagnastefna er yfirveguð áætlun þín um að líta á gögn sem eign: hvernig þau eru framleidd, lýst, í eigu einhvers, vernduð, deilt og notuð til að skapa verðmæti. [Gagnastjórnun](https://en.wikipedia.org/wiki/Data_governance) er stýrikerfið sem gerir stefnuna raunverulega: hlutverkin, stefnurnar, staðlarnir og stýringarnar sem halda gögnum traustverðum og löglegum yfir tíma. Í litlum teymum eru þessi áhyggjuefni oft óbein, borin í hausum fáeinna verkfræðinga. Í stærð stórra forritarastofnana, fyrirtækja og opinberra stofnana hrynur sú óformlegheit. Hundruð teyma framleiða þúsundir taflna. Tugir kerfa segjast geyma „raunverulegu“ viðskiptavinaskrána. Og enginn getur sagt með vissu hvaða tala er rétt í stjórnarkynningu eða opinberri skýrslu.

Fyrir stór teymi er kostnaður slakrar gagnastjórnunar ekki óhlutbundinn. Eftirlitsaðilar ætlast til sýnilegs uppruna og stjórnunar á persónulegum, fjárhagslegum og heilbrigðisgögnum undir reglum eins og [GDPR](https://en.wikipedia.org/wiki/General_Data_Protection_Regulation) (almenna persónuverndarreglugerð ESB), [HIPAA](https://en.wikipedia.org/wiki/Health_Insurance_Portability_and_Accountability_Act) (bandarísku lögin um flytjanleika og ábyrgð sjúkratrygginga) og geirasértækum reglum. Fyrirtæki standa frammi fyrir beinni fjárhagslegri útsetningu af rangt skýrðum mælikvörðum, misheppnuðum úttektum og tvíteknum gagnavettvöngum. Opinberar stofnanir bera auknar skyldur um varðveislu skjala, upplýsingaaðgang, opinbera ábyrgð og jafna meðferð borgara. Í hverju þessara umhverfa eru gögn sem þú getur ekki treyst verri en engin gögn, því þau knýja öruggar en rangar ákvarðanir.

Hugmyndin sem knýr framfarir í stærð er einföld: líttu á gögn sem vöru. Í stað þess að gögn séu útblástur forrita hefur hvert mikilvægt gagnasafn eiganda, skjalfest viðmót, gæðatryggingar og notendur sem eru meðhöndlaðir sem viðskiptavinir. Þessi kafli fjallar um það vöruviðhorf samhliða klassísku stjórnunaragunum: ráðsmennsku, skráningu, [stofngagnastjórnun](https://en.wikipedia.org/wiki/Master_data_management) og gæðum. Hann fjallar líka um skipulagsvalin sem ráða því hvaða líkan hentar teyminu þínu: [gagnavef](https://en.wikipedia.org/wiki/Data_mesh) (data mesh; dreifð gögn í eigu léna, birt sem vörur), gagnavatnshús (lakehouse; vöruhússtíl stjórnun og stýring lögð yfir sveigjanlegt [gagnavatn](https://en.wikipedia.org/wiki/Data_lake)) og [gagnavöruhús](https://en.wikipedia.org/wiki/Data_warehouse) (stýrða miðlæga geymslu líkanaðra, fyrirspurnarklárra gagna).

*Sjá einnig:* kafla 4.5 (persónuvernd og gagnavernd), kafla 7.2 (gagnaverkfræði) og kafla 4.6 (reglufylgni og stjórnarhættir).

## Meginreglur

- Gögn eru varanleg eign með eigendum, ekki einnota aukaafurð forrita.
- Hvert mikilvægt gagnasafn hefur nefndan ábyrgan eiganda og skjalfestan samning.
- Stjórnun gerir traustverða notkun mögulega. Hún er ekki skrifræðislegt hlið sem segir bara nei.
- Ein áreiðanleg uppspretta ætti að vera fyrir hvern mikilvægan viðskiptahlut.
- Gæði, persónuvernd og uppruni eru hönnuð inn, ekki skoðuð inn eftir á.
- Notendur gagna eru viðskiptavinir sem þarfir þeirra móta vöruna.
- Stefnur eru kóðaðar og framfylgt sjálfvirkt hvar sem hægt er, ekki látnar velvilja eftir.
- Sambandsskipt eignarhald skalast betur en eitt miðlægt teymi eftir því sem skipulagsheildin vex.

## Ráðleggingar

### Líttu á gögn sem vöru

Gefðu hverju mikilvægu gagnasafni vörueiganda sem ber ábyrgð á hæfni þess til notkunar. Gagnavara hefur nafn, skjalfest skema, lýsingu á merkingu sinni og uppruna, skilgreindan endurnýjunartakt og útgefnar gæðaviðmiðanir. Notendur þínir ættu að geta fundið hana, skilið og reitt sig á hana án þess að spyrja framleiðsluteymið einnar spurningar. Beittu sama aga og þú beitir á hugbúnaðar-API: útgáfustýringu, úreldingartilkynningum, breytingaskrám og afturábaksamhæfi.

### Komdu á gagnasamningum og þjónustusamningum

Gagnasamningur er skýrt, vélathugahæft samkomulag milli framleiðanda og notenda hans. Hann nær yfir skema, merkingu, ferskleika, magn og leyfðar breytingar. Framfylgdu samningum í leiðslunni svo brjótandi andstreymisbreyting bili snemma við upptökin, frekar en að spilla hljóðlega niðurstreymisskýrslum vikum síðar. Paraðu samninga við þjónustustigssamninga og markmið. Til dæmis, „viðskiptavinavídd endurnýjuð fyrir 06:00 daglega, 99,5% daga, með færri en 0,1% núll viðskiptalyklum“. Birtu þetta og varaðu við brotum.

### Byggðu ráðsmennsku og stjórnunarrekstrarlíkan

Haltu ábyrgð aðskilinni frá framkvæmd. Gagnaeigendur (oft viðskiptaleiðtogar) bera ábyrgð á léni. Gagnaráðsmenn (sérfræðingar á sviðinu) viðhalda skilgreiningum, leysa gæðavandamál og samþykkja aðgang. Létt gagnastjórnarráð setur þvert yfir staðla og sker úr deilum. Haltu líkaninu sambandsskiptu: miðlægt stuðningsteymi veitir verkfæri, staðla og þjálfun á meðan lénateymi eiga gögn sín. Þetta forðast bæði flöskuháls fullrar miðstýringar og glundroða engrar stjórnunar.

### Fjárfestu í gagnaskrá og uppruna

Leitarhæf skrá er framdyr gagnalandareignar þinnar. Hún ætti að geyma viðskiptaorðasöfn, tæknileg skema, eignarhald, viðkvæmniflokkanir, gæðaeinkunnir og ætterni gagna frá frumkerfi gegnum umbreytingar til mælaborða. Sjálfvirknivæddu söfnun lýsigagna frekar en að treysta á handvirka skjölun, sem rotnar fljótt. Ætterni er nauðsynlegt fyrir áhrifagreiningu, atvikaviðbrögð, úttekt og eftirlitsbeiðnir eins og aðgang og eyðingu hins skráða.

### Stofngagnastjórnun og ein uppspretta sannleikans

Fyrir kjarnahluti (viðskiptavin, borgara, vöru, birgi, starfsmann) skaltu nota stofngagnastjórnun til að sætta tvítök og andstæðar skrár í eina gullskrá. Veldu arkitektúr (skráningar-, samþjöppunar-, samlífs- eða miðlægan) út frá því hve áreiðanleg miðstöðin þarf að vera. Skilgreindu pörunar- og sigurreglur skýrt og gerðu þær úttektarhæfar. [Ein uppspretta sannleikans](https://en.wikipedia.org/wiki/Single_source_of_truth) kemur í veg fyrir klassísku bilunina þar sem fjármál, sala og rekstur skýra hvert um sig frá ólíkum tekjum.

### Mældu gagnagæði yfir víddir

Stýrðu gæðum eftir nefndum víddum: nákvæmni, fullkomleika, samkvæmni, tímanleika, gildi og einkvæmni. Mældu leiðslur með sjálfvirkum prófum og samfelldri gagnavöktun (ferskleika-, magn-, skemarek- og dreifingarathuganir), svo þú grípir frávik áður en notendur verða fyrir áhrifum. Líttu á gagnaatvik eins og framleiðslubilanir, með greiningu, flokkun, rótargreiningu og eftirmálsrýni.

### Flokkaðu, verndaðu og stýrðu aðgangi

Flokkaðu gögn eftir viðkvæmni og beittu stýringum í réttu hlutfalli: dulkóðun, grímun, táknun, raða- og dálkaöryggi og aðgang með lágmarksréttindum rýndum reglulega. Haltu varðveislu- og eyðingaráætlun sem fullnægir bæði lágmörkunarkröfum og skjalavörslulögum. Í opinberu samhengi skaltu sætta gagnsæisskyldur við persónuvernd af ásetningi, frekar en tilvik fyrir tilvik.

## Málamiðlanir: kostir og gallar

| Nálgun | Kostir | Gallar | Best passun |
|---|---|---|---|
| Miðlægt stjórnunarteymi | Samræmdir staðlar, skýr ábyrgð | Flöskuháls, aftengt lénum | Smáar eða mjög regluverkaðar skipulagsheildir |
| Sambandsskipt stjórnun | Skalast, lénssérþekking, eignarhald | Krefst sterkra verkfæra og menningar | Stór fjöllénafyrirtæki |
| Gagnavöruhús | Þroskað, stýrt, afkastamikið SQL | Stíft, kostnaðarsamt fyrir óuppbyggð gögn | Stöðug, viðskiptagreindarþung vinnuálög |
| Gagnavatnshús | Sveigjanlegt, sameinað, ræður við allar gagnategundir | Yngri verkfæri, stjórnunarfyrirhöfn | Blönduð greining og vélnám |
| Gagnavefur | Lénaeignarhald, skalast skipulagslega | Hátt þroskaviðmið, samræmingarkostnaður | Mjög stórar, dreifðar skipulagsheildir |

Stjórnun skiptir alltaf á hraða og trausti. Létt stjórnun lætur teymi hreyfa sig hratt, þar til úttekt, brot eða vandræðaleg röng skýrsla neyðir dýrt uppgjör. Þung stjórnun ver traust en getur kæft tilraunir og ýtt teymum í átt að skuggakerfum. Varanlega svarið er að kóða stjórnun sem sjálfvirka, sjálfsafgreiðsluvarnarrimla, svo löghlýðna leiðin sé líka auðvelda leiðin. Arkitektúrlega kjósa vöruhús stýrðan einfaldleika, vefur kýs skipulagslega stærð og vatnshús skipta muninum. Rétta valið fylgir uppbyggingu skipulagsheildarinnar langtum meira en nokkurt tæknilegt viðmið.

## Spurningar til að ræða með teyminu

1. **Hvaða gagnaarkitektúr (vöruhús, vatnshús eða vefur) passar í raun við uppbyggingu skipulagsheildar ykkar og eruð þið heiðarleg um þroskaviðmiðið sem hver krefst?** Málamiðlunartaflan sýnir að þetta val fylgir skipulagi, ekki viðmiðum: vöruhús umbunar stöðugum, viðskiptagreindarþungum vinnuálögum, vatnshús ræður við blandaða greiningu og vélnám og vefur skalast yfir mörg sjálfstæð lén en krefst mikils þroska og sterkra verkfæra. Fyrir stórt fyrirtæki eða opinbera stofnun með tugi léna framleiðir stökk í vef áður en þú hefur sjálfsafgreiðsluvettvanga og stjórnunarmenningu glundroða klæddan sem valddreifingu. Komdu með áþreifanleg merki: hve mörg lén framleiða gögn, hvort miðlæg teymi séu þegar flöskuháls og hvort lénateymi hafi færnina og hvatann til að eiga vörur. Ef þú skortir sambandsskipt verkfæri í dag gæti heiðarlega svarið verið stýrt vöruhús eða vatnshús núna og vefur síðar. Veldu líkanið sem fólkið ykkar getur í raun rekið, fjárfestu síðan í þroskanum sem næsta líkan þarf.

2. **Getið þið staðið við eyðingarbeiðni frá enda til enda í dag og sannar ætterni ykkar hvert hvert eintak af persónuskrá fór?** Undir GDPR og svipuðum reglum er eyðingar- eða aðgangsbeiðni hins skráða lagaleg skylda með hörðum frestum, og að afrita gögn víða án ætternis gerir ómögulegt að fullnægja henni. Stór teymi dreifa reglulega gögnum í markaðsgeymslur, útdrætti, skyndiminni og töflureikna, svo raunverulega spurningin er hvort þið getið rakið og náð til hvers eintaks, ekki hvort þið getið eytt frumritinu. Komdu með sönnunargögn: veldu einn raunverulegan viðskiptavin eða borgara og reyndu að telja upp hvern stað þar sem gögn hans búa. Ef þið getið það ekki er það bil bæði reglufylgniáhætta og sprengisvæðisvandamál við brot. Svarið ætti að knýja fjárfestingu í sjálfvirku ætterni og þéttari stýringum á óstýrðri afritun, því löghlýðna leiðin verður að vera smíðuð áður en beiðnin berst.

3. **Er stjórnun ykkar auðvelda leiðin eða hlið sem fólk fer framhjá og hvar eru skuggakerfin sem sanna það?** Varanlega svar kaflans er að kóða stjórnun sem sjálfvirka, sjálfsafgreiðsluvarnarrimla svo löghlýðna leiðin sé líka hraðasta leiðin, því þung handvirk stjórnun ýtir teymum að skuggatöflureiknum og óstýrðum afritum. Fyrir fyrirtæki og stofnanir eru skuggakerfi þar sem brot, rangar tölur og misheppnaðar úttektir fæðast, einmitt af því enginn fylgist með þeim. Komdu með áþreifanlega skrá: hvaða teymi halda eigin afritum, hvaða skýrslur sniðganga skrána og hvar fólk segir að opinbera ferlið sé of hægt. Hvert skuggakerfi er merki um að stýrða leiðin kosti meira en lausnin. Lagaðu núninginn frekar en að gefa út enn eina stefnu, svo að nota vottuð gögn og samninga sé raunverulega auðveldara en að fara framhjá þeim.

4. **Hvaða mikilvægi viðskiptahlutur þarf mest eina áreiðanlega uppsprettu og hver ber nafn sem ábyrgur fyrir gullskrá hans í dag?** Stofngagnastjórnun er til að koma í veg fyrir að fjármál, sala og rekstur skýri hvert frá ólíkum viðskiptavini eða ólíkum tekjum, og í stærð breytir fjarvera einnar áreiðanlegrar uppsprettu hverri þverlénatölu í rifrildi. Sjónarmiðin sem togast á eru hve áreiðanleg miðstöðin þarf að vera (skráning, samþjöppun, samlíf eða fullkomlega miðlæg) og hve mikla pörunar- og sigurrökfræði þið eruð tilbúin að smíða og úttekta, þar sem þyngri miðstöð kostar meira en leysir fleiri árekstra. Komdu með hlutina sem birtast í flestum skýrslum (viðskiptavin, borgara, vöru, birgi, starfsmann), talningu á því hve mörg kerfi segjast geyma raunverulegu skrána fyrir hvern og pörunarreglurnar sem þið notið í dag, ef einhverjar. Fyrir banka eða landsstofnun skaltu nefna ábyrga eigandann og sigurreglurnar skýrt, því eftirlitsaðili sem rekur tölu úr opinberri skýrslu aftur til uppsprettu mun spyrja hver ákvað hvert tvítak vann, og „enginn“ er ekki svar sem lifir af úttekt.

5. **Hvernig vitið þið að mikilvægt gagnasafn sé hæft til notkunar áður en notandi uppgötvar að það er bilað?** Í óþroskuðum landareignum finnst gæði af greinandanum sem mælaborð hans brotnar eða stjórnandanum sem stjórnartala er röng, sem er dýrasti mögulegi greiningarpunkturinn. Spennan er milli kostnaðar við að mæla gæði (próf, ferskleika- og magnathuganir, dreifingar- og skemarekvöktun yfir nefndar víddir eins og nákvæmni, fullkomleika og gildi) og kostnaðar atvikanna sem þið komið í veg fyrir, og teymi vanfjárfesta reglulega því bilanirnar eru ósýnilegar þar til þær verða skelfilegar. Komdu með síðustu þrjú gagnaatvikin, hvernig þau voru greind og hve lengi þau stóðu áður en nokkur tók eftir, auk gæðaþjónustusamninganna sem þið birtið og varið við í dag. Fyrir skýrslugerð fyrirtækja og hins opinbera skaltu tengja hverja mikilvæga gagnavöru við skýra gæðaþröskulda og líta á brot eins og framleiðslubilun með flokkun og eftirmálsrýni, því röng tala í eftirlitsskýrslu eða opinberri tölfræði ber lagalegan og orðsporskostnað sem dvergar vöktunarreikninginn.

6. **Er stjórnun ykkar raunverulega sambandsskipt með lénaeignarhaldi, eða miðlægt teymi gert ábyrgt fyrir gögnum sem það skilur ekki?** Kaflinn heldur því fram að sambandsskipt eignarhald með miðlægum stuðningi skalist þar sem hrein miðstýring myndar flöskuháls og hrein valddreifing endar í glundroða, samt segjast mörg skipulagsheildir vera sambandsskiptar á meðan lítið miðlægt teymi er nafnlega ábyrgt fyrir þúsundum taflna sem það hefur enga lénaþekkingu á. Togið á móti er raunverulegt: miðlæg teymi gefa samræmi og einn aðila til að sækja til saka, á meðan lénaeignarhald gefur sérþekkingu og ábyrgð en krefst þess að viðskiptaeigendur taki á sig ábyrgð sem þeir vilja kannski ekki. Komdu með heiðarlegt kort af því hver er ábyrgur á móti hver viðheldur skilgreiningum og leysir gæðavandamál í raun fyrir helstu lén þín og hvort ráðsmenn hafi valdið og tímann sem hlutverkið krefst. Í stóru fyrirtæki eða stofnun skaltu athuga að eignarhald sitji hjá fólki sem hefur bæði lénaþekkingu og umboðið til að segja nei, því stjórnun úthlutuð miðlægu teymi án valds framleiðir stefnur sem enginn fylgir og ráð sem sker ekki úr neinu.

## Sjónarhorn eftir geirum

**Sprotafyrirtæki.** Hraði og lífsafkoma slá ferli. Nefndu einn eiganda fyrir hvert kjarnagagnasafn og gerðu eina geymslu að einu áreiðanlegu uppsprettunni fyrir hluti eins og „virkur viðskiptavinur“ og slepptu skrám, ráðum og vef alveg. Eins síðu samningur fyrir fáu mikilvægu töflurnar (skema, endurnýjunartími, ein gæðaviðmiðun) lýkur rifrildinu „hver er talan rétt“ á einum eftirmiðdegi. Hallaðu þér að stjórnuninni sem er þegar innbyggð í vöruhúsið þitt frekar en að manna starfsemi sem þú hefur ekki efni á.

**Lítið fyrirtæki.** Án sérstaks gagnasérfræðings og með þröngt fjárhagsáætlun skaltu líta á stjórnun sem gagnahreinlæti frekar en vettvangsverkefni: vittu hvaða persónugögn þú átt, hvar þau búa og hver má snerta þau. Kjóstu stýrt vöruhús eða viðskiptagreindartól sem veitir ætterni, aðgangsstýringu og varðveislu úr kassanum, svo þú kaupir stjórnun innbyggða í verkfæri sem þú rekur þegar í stað þess að smíða hana. Taktu frá sérsmíðaða leiðslu fyrir eina gagnasafnið sem knýr rekstrinn í raun.

**Stórfyrirtæki.** Í stærð yfir mörg teymi er verkið sambandsskipt eignarhald með miðlægum stuðningi: sameiginleg skrá með sjálfvirku ætterni, framfylgdir gagnasamningar, stofngögn fyrir kjarnahluti og gæðaþjónustusamningar mældir gegn grunnlínum. Kóðaðu stjórnun sem sjálfsafgreiðsluvarnarrimla svo löghlýðna leiðin sé líka hraða leiðin og stýrðu gögnum sem eignasafni vara með nefndum eigendum. Þannig geta úttektaraðilar rakið hverja tölu úr skýrslu aftur til uppsprettu og hópar hætta að finna upp sömu leiðslur og skilgreiningar aftur.

**Hið opinbera.** Innkaupareglur, gagnsæi og opinber ábyrgð móta hvert val. Líttu á útgefnar vísitölur sem gagnavörur með skjalfestri aðferðafræði, útgáfustýrðum útgáfum og gæðahliðum og sættu upplýsingalaga- og opinna gagnaskyldur við persónuvernd og lágmörkun af ásetningi frekar en tilvik fyrir tilvik. Krefstu gagnaflytjanleika og upplýsingagjafar um ætterni í samningum við seljendur til að forðast bindingu, haltu verjanlegri varðveislu- og eyðingaráætlun og láttu ráðsmennskuráð halda sameiginlegum skilgreiningum svo „heimili“ eða „atvinnuleysi“ þýði það sama í hverri deild.

## Dæmi

**Sprotafyrirtæki.** SaaS-fyrirtæki á frumstigi komst að því að reikningatöflureiknir þess, sölutólið og vörugagnagrunnurinn skýrðu hvert frá ólíkum fjölda viðskiptavina og enginn gat sagt hver væri réttur fyrir fjárfestauppfærsluna. Fjögurra manna teymið nefndi einn eiganda fyrir hvert kjarnagagnasafn, gerði vöruhúsið að einu uppsprettunni fyrir „virkur viðskiptavinur“ og skrifaði eins síðu samning sem lýsti skemanu og daglegum endurnýjunartíma. Það tók einn eftirmiðdag og batt enda á vikulegt rifrildi um hvaða tölu ætti að treysta.

**Stórfyrirtæki.** Fjölþjóðlegur banki sameinaði tugi andstæðra viðskiptavinaskráa yfir smásölu-, útlána- og eignastýringardeildir sínar í stofngagnamiðstöð með sigurreglum og gullskrá. Hvert lén birti gagnavörur með samningum og ferskleikaþjónustusamningum, birtar í miðlægri skrá með ætterni. Tími við eftirlitsskýrslugerð féll verulega, því úttektaraðilar gátu nú rakið hverja tölu úr skýrslu til uppsprettu. Bankinn lagði líka niður nokkra óþarfa skýrslugerðarvettvanga.

**Hið opinbera.** Landsbundin hagstofa lítur á útgefnar vísitölur sínar sem gagnavörur, með skjalfestri aðferðafræði, útgáfustýrðum útgáfum og ströngum gæðahliðum. Ráðsmennskuráð sættir skilgreiningar yfir deildir, svo „atvinnuleysi“ eða „heimili“ þýði það sama alls staðar. Flokkun og stýrður aðgangur verndar trúnað svarenda, á meðan opinber skrá styður gagnsæi og upplýsingalagaskyldur.

## Viðskiptarök: hvatar, ávöxtun fjárfestingar og heildarkostnaður

Hvatinn fyrir gagnastjórnun er áhættuminnkun og verðmætasköpun í nokkurn veginn jöfnum hlutföllum. Hvað áhættu varðar eru forðaður kostnaður meðal annars eftirlitssektir, brotaábyrgð, misheppnaðar úttektir og orðsporsskaði af birtingu rangra talna. Hvað verðmæti varðar flýta traustverð, finnanleg gögn hverju niðurstreymis greiningar- og vélnámsstarfi, draga úr tvíteknum leiðslum og stytta tímann frá spurningu til svars.

Upptökukostnaðurinn er raunverulegur: skrár- og gæðaverkfæri, tími ráðsmanna og eigenda og skipulagsbreytingin til að láta eignarhald festast. Vegðu heildareignarkostnað gegn kostnaði þess að taka ekki upp, sem er yfirleitt stærri, bara falinn. Ómældur birtist sá kostnaður þannig að greinendur eyða mestum tíma sínum í að finna og hreinsa gögn, teymi sem endurbyggja sömu leiðslurnar og stjórnendur sem taka ákvarðanir á tölum sem enginn getur varið. Færðu rök við forystu á þeirra tungumáli: stjórnun breytir gögnum úr skuld með ótakmarkaða niðurhlið í eign með samsettum ávöxtun og hún er forsenda traustverðrar gervigreindar. Byrjaðu þar sem sársaukinn og eftirlitsútsetningin eru mest, svo þú getir sýnt verðmæti fljótt.

## Andmynstur og gildrur

- Stjórnun í nefnd án sjálfvirkni, sem framleiðir stefnur sem enginn fylgir.
- Að skrá allt í einu í stað gagnasafnanna sem raunverulega skipta máli.
- Stofngagnaverkefni sem sjóða hafið og afhenda aldrei gullskrá.
- Að líta á [gagnagæði](https://en.wikipedia.org/wiki/Data_quality) sem einskiptis hreinsun frekar en samfellda vöktun.
- Eignarhald úthlutað miðlægu teymi sem skortir lénaþekkingu eða vald.
- Samningar skjalfestir á wiki-síðum en ekki framfylgt í leiðslum.
- Að afrita gögn víða án ætternis, sem gerir eyðingarbeiðnir ómögulegar að uppfylla.
- Að kaupa verkfæri og kalla það stefnu. Verkfæri án rekstrarlíkans bregðast.

## Þroskalíkan

1. Upphaf: Gögn eru óskjalfest og eigendalaus, meðhöndluð ad hoc og viðbragðsdrifið. Skilgreiningar stangast á milli teyma. Gæði uppgötvast af notendum þegar skýrslur brotna. Engin skrá eða ætterni er til.
2. Þróun: Grunnvinnubrögð birtast en eru ósamræmd milli teyma. Sum gagnasöfn hafa eigendur og skjölun og hlutaskrá er til. Gæðaathuganir eru handvirkar og viðbragðsdrifnar. Stjórnunarstefna er skrifuð en veikt og ójafnt framfylgd.
3. Stöðlun: Eignarhald, samningar og þjónustusamningar eru skjalfestir og framfylgdir um skipulagsheildina. Mikilvægar gagnavörur hafa nefnda eigendur. Skrá með sjálfvirku ætterni nær yfir lykillén. Stofngögn eru til fyrir kjarnahluti. Stjórnun er sambandsskipt með miðlægum stuðningi og beitt samræmt frekar en teymi fyrir teymi.
4. Stjórnun: Landareignin er mæld og stýrð gegn grunnlínum. Gæðavíddir (nákvæmni, fullkomleiki, tímanleiki, gildi, einkvæmni) eru raktar gegn útgefnum þjónustumarkmiðum. Samningabrotahlutföll, þekja ætternis og skrár, ferskleiki og tími til að uppfylla eyðingarbeiðni eru skýrð á mælaborðum. Vöktun varar við skemareki og magnfrávikum. Atvik fá flokkun, rótargreiningu og eftirmálsrýni. Aðgangs- og fara/ekki fara ákvarðanir hvíla á mælikvörðum gegn grunnlínum, ekki skoðun.
5. Samhæfing: Stjórnun er stöðugt bætt og samþætt um skipulagsheildina. Gögn sem vara er normið yfir lén. Samningum er framfylgt sjálfvirkt og brjótandi breytingar bila snemma. Sjálfsafgreiðsluvarnarrimlar kóða stefnu. Gæði og ætterni nærir fyrirbyggjandi áhættustýringu. Skilgreiningar eru treystar um skipulagsheildina og styðja regluverkaða skýrslugerð og gervigreind. Skipulagsheildin endurjafnar eignarhald, leggur niður óþarfa vettvanga og aðlagar stjórnun þegar reksturinn og regluverk breytast.

## Hugmyndir til umræðu

- Hver af viðskiptahlutum þínum þarf brýnast eina uppsprettu sannleikans og hvers vegna er hann sundurlaus í dag?
- Hvar hefðu framfylgdir gagnasamningar komið í veg fyrir nýlegt atvik?
- Er skipulagsheild þín byggð fyrir sambandsskipt eignarhald, eða myndi miðstýring passa betur núna?
- Hvernig sættirðu gagnsæisskyldur hins opinbera við persónuvernd og lágmörkun?
- Hve hátt hlutfall af tíma greinenda þinna fer í að finna og hreinsa gögn og hvers virði væri að helminga það?
- Hver er ábyrgur, með nafni, fyrir mikilvægasta gagnasafni þínu og veit hann það?

## Helstu atriði

- Líttu á gögn sem vöru með eigendum, samningum og þjónustusamningum, ekki sem útblástur forrita.
- Sambandsskipt stjórnun með miðlægum stuðningi skalast betur en hrein miðstýring.
- Skrá með sjálfvirku ætterni er framdyr traustverðrar gagnalandareignar.
- Komdu á einni uppsprettu sannleikans fyrir kjarnahluti með stofngagnastjórnun.
- Stýrðu gæðum samfellt yfir nefndar víddir með vöktun og atvikaviðbrögðum.
- Kóðaðu stjórnun sem sjálfvirka varnarrimla svo löghlýðna leiðin sé auðvelda leiðin.
- Veldu vöruhús, vatnshús eða vef eftir skipulagsheild þinni, ekki tískubylgjum.

## Heimildir og frekari lestur

- DAMA International, "DAMA-DMBOK: Data Management Body of Knowledge."
- Zhamak Dehghani, "Data Mesh: Delivering Data-Driven Value at Scale."
- Ralph Kimball and Margy Ross, "The Data Warehouse Toolkit."
- Piethein Strengholt, "Data Management at Scale."
- David Loshin, "Master Data Management."
- Chad Sanderson and colleagues, writings on data contracts.
- ISO/IEC 38505, "Governance of data."
- ISO 8000, "Data quality" standard series.
