# 7.8 Gagnagæði og gagnavöktun

## Yfirlit og tilgangur

[Gagnagæði](https://en.wikipedia.org/wiki/Data_quality) eru hæfni til notkunar: að hve miklu leyti gögn þjóna ákvörðunum, vörum og skýrslum sem byggja á þeim. Gagnasafn er ekki gott eða slæmt í óhlutbundnu samhengi. Það er nógu gott fyrir tilgang, eða ekki. Viðskiptavinaheimilisfang sem er í lagi fyrir markaðstalningu getur verið óhæft fyrir lagalega tilkynningu. Sú rammun skiptir máli, því hún færir umræðuna frá „eru gögnin okkar fullkomin“ (aldrei) til „eru gögnin okkar hæf fyrir það sem við ætlum að gera við þau“ (svaranlegt og prófanlegt). Klassísku víddirnar eru nákvæmni, fullkomleiki, samkvæmni, tímanleiki, gildi og einkvæmni og flest raunveruleg vandamál leiða til einnar þeirra.

Hér er óþægilegi sannleikurinn fyrir stór teymi: slæm gögn eru verri en engin gögn. Þegar þú hefur engin gögn veistu það og heldur áfram með viðeigandi varkárni. Þegar þú hefur röng gögn sem líta rétt út bregstu við þeim með fölsku sjálfstrausti. Slæm gögn spillast hljóðlega. Þau flæða inn í mælaborð sem stjórnandi treystir, inn í [vélnámslíkan](https://en.wikipedia.org/wiki/Machine_learning) sem þjálfast á þeim og kóðar villur þeirra og inn í ákvarðanir sem enginn hugsar um að draga í efa því talan var þarna á skjánum. Skaðinn er dreifður og seinkaður, sem er einmitt ástæða þess að hann er dýr. Þegar einhver tekur eftir hefur rangi talan verið vitnað í stjórnarkynningu, eftirlitsskýrslu eða opinbera tölfræði.

Gagnavöktun er greinin sem grípur þetta áður en notendur þínir gera það. Hún er bein hliðstæða hugbúnaðarvöktunar og mælinga (kafli 9.2): sama eðlishvöt sem segir þér að fylgjast með beiðnatöf og villuhlutföllum segir þér að fylgjast með gagnaferskleika, magni, skema og dreifingu. Þessi kafli byggir á gagnastefnu og gagnastjórnun (kafli 7.1) og gagnaverkfræði (kafli 7.2) og nærir gagnalíkön og merkingarlag (kafli 7.7) og ábyrga og traustverða gervigreind (kafli 6.5). Fyrir fyrirtæki sem sætta mörg frumkerfi og ríkisstjórnir sem birta lögbundna tölfræði er það að líta á áreiðanleika gagna sem verkfræðivandamál með eigendum og þjónustustigum munurinn á trausti og mjög opinberri leiðréttingu.

## Meginreglur

- Gagnagæði eru hæfni til notkunar, ekki fullkomnun. Skilgreindu þau gegn tilganginum.
- Slæm gögn eru verri en engin gögn, því þau spilla ákvörðunum hljóðlega.
- Prófaðu gögn eins og þú prófar kóða: staðhæfingar, væntingar og skemaathuganir í leiðslunni.
- Samningar milli framleiðenda og notenda gera væntingar skýrar og framfylgjanlegar.
- Fylgstu með ferskleika, magni, skema og dreifingu, á sama hátt og þú fylgist með þjónustum.
- Ætterni breytir „eitthvað er rangt“ í „hér er það sem brotnaði og hverju það hefur áhrif á“.
- Líttu á gagnaatvik eins og framleiðsluatvik, með eignarhaldi, alvarleika og þjónustustigum.
- Greindu vandamál þar sem þau koma inn, ekki þremur lögum niðurstreymis í mælaborði.

## Ráðleggingar

### Skilgreindu gæði eftir víddum og mældu þau

Óljós gæðamarkmið framleiða óljósar niðurstöður. Brjóttu gæði í mælanlegar víddir og festu áþreifanlegar athuganir við hverja. Nákvæmni spyr hvort gildi endurspegli veruleikann (passar þessi skráðu tekjutala við höfuðbók uppsprettunnar). Fullkomleiki spyr hvort væntar færslur og reitir séu til staðar (vantar daga, eru nauðsynlegir dálkar núll). Samkvæmni spyr hvort sama staðreynd sé sammála yfir kerfi (passar viðskiptavinafjöldinn hjá fjármálum við fjöldann í vöruhúsinu). Tímanleiki spyr hvort gögn berist í tæka tíð til að nýtast (eru gögn gærdagsins tilbúin fyrir morgunskýrsluna). Gildi spyr hvort gildi fylgi reglum og sniðum (eru allir gjaldmiðlakóðar til, eru dagsetningar innan sviðs). Einkvæmni spyr hvort einingar birtist einu sinni (eru tvítekin pöntun að blása upp heildina). Veldu víddirnar sem skipta máli fyrir hvert gagnasafn, settu þröskulda og raktu þá með tímanum. Gæði sem þú mælir ekki eru gæði sem þú giskar á.

### Prófaðu leiðslur með staðhæfingum og væntingum

Gögn eiga skilið sömu prófunarnákvæmni og forritskóði. Notaðu [gagnastaðfestingu](https://en.wikipedia.org/wiki/Data_validation) á hverju stigi: staðhæfingabundin próf sem láta leiðsluna bila þegar fastaregla er brotin og væntingabundin próf sem lýsa hvernig „eðlilegt“ lítur út fyrir töflu og merkja frávik. Staðhæfðu að frumlyklar séu einkvæmir og ekki núll, að aðkomulyklar leysist, að flokkadálkar innihaldi aðeins viðurkennd gildi, að tölulegir dálkar falli innan trúverðugra sviða og að línufjöldi lendi í væntu bandi. Bættu við skemaathugunum sem bila hátt þegar dálki er bætt við, hann felldur niður, endurnefndur eða endurtegundur andstreymis. Keyrðu þessar athuganir í samfelldri samþættingu svo slæm umbreyting sé gripin fyrir sameiningu og keyrðu þær aftur í framleiðslu gegn lifandi gögnum svo slæm uppspretta sé gripin áður en hún nær til notenda. Markmiðið er að bila snemma og hátt, því biluð leiðsla er öruggari en hljóðlega röng.

### Komdu á gagnasamningum milli framleiðenda og notenda

Flest gagnagæðaatvik byrja andstreymis, þegar framleiðsluteymi breytir skema, merkingu eða gildavenju án þess að vita hver treystir á það. [Gagnasamningur](https://en.wikipedia.org/wiki/Data_contract) lagar þetta með því að gera viðmótið skýrt: skemað, merkingu hvers reits, leyfð gildi, ferskleikatryggingar og ferlið við að gera breytingu. Framleiðandinn skuldbindur sig til samningsins, notandinn smíðar gegn honum og brjótandi breyting krefst útgáfustýringar og tilkynningar frekar en hljóðlátrar óvæntrar uppákomu á mánudegi. Framfylgdu samningum vélrænt þar sem þú getur, með því að staðfesta innkomandi gögn gegn samningnum við mörkin og hafna eða einangra brot. Samningar breyta óbeinu, brothættu ósjálfstæði í skýrt, samið ósjálfstæði. Þeir gera líka eignarhald sýnilegt, sem er hálf orrustan í stærð.

### Vaktaðu fjögur merki gagnavöktunar

Gagnavöktun fylgist með fjórum merkjum, í beinni hliðstæðu við hvernig þú fylgist með keyrandi þjónustu (kafli 9.2). Ferskleiki: eru gögnin eins ný og þau ættu að vera, eða hefur leiðslan stöðvast. Magn: er línufjöldinn innan væntanlegs sviðs, eða barst tafla hálftóm eða tvíhlaðin. Skema: hefur uppbyggingin breyst óvænt. Dreifing: hafa gildin sjálf rekið, svo dálkur sem var 2 prósent núll er skyndilega 40 prósent núll, eða meðaltal hefur færst á vegu sem gefur til kynna andstreymisgalla. Mældu þessi merki á mikilvægu töflunum þínum, lærðu eðlileg mynstur þeirra og varaðu við brotum. Þannig skiptirðu „stjórnandi tók eftir að mælaborðið leit rangt út“ út fyrir „eigandateymið var kallað út á bilunarstaðnum“. Versti mögulegi greinir gagnavandamáls er niðurstreymis maður sem treystir tölunni.

### Bættu við fráviksgreiningu, en stilltu hana gegn viðvörunarþreytu

Föst þröskuldamörk grípa augljósar bilanir. Fyrir lúmskara rek skaltu leggja ofan á [fráviksgreiningu](https://en.wikipedia.org/wiki/Anomaly_detection) sem lærir árstíðarmynstur hvers mælikvarða og merkir tölfræðilega óvenjuleg frávik, svo þú grípir hægan leka áður en hann verður flóð. Vertu agaður í þessu. Hávaðasamar fráviksviðvaranir kenna fólki að hunsa viðvaranir, sem er verra en engar viðvaranir. Byrjaðu á verðmætustu töflunum, varaðu aðeins við því sem maður ætti að bregðast við, beindu hverri viðvörun til nefnds eiganda og stilltu miskunnarlaust. Viðvörun sem enginn bregst við er galli í vöktuninni þinni, ekki eiginleiki.

### Raktu ætterni fyrir áhrifagreiningu og rótarorsök

Þegar eitthvað brotnar skipta tvær spurningar strax máli: hvað olli því og hverju hefur það áhrif á. [Gagnaætterni](https://en.wikipedia.org/wiki/Data_lineage) svarar hvoru tveggja með því að kortleggja hvernig gögn flæða frá uppsprettu gegnum hverja umbreytingu til hverrar niðurstreymistöflu, mælaborðs og líkans. Fyrir rótarorsök rekurðu slæma tölu andstreymis til umbreytingarinnar eða uppsprettunnar sem kom henni inn. Fyrir áhrifagreiningu rekurðu fram á við til að sjá hvern notanda sem slæm hleðsla snerti, svo þú getir látið þá vita og einangrað skaðann áður en hann dreifist. Fangaðu ætterni sjálfvirkt úr umbreytingar- og samstillingarverkfærum þínum frekar en að viðhalda skýringarmynd í höndunum, því handteiknuð skýringarmynd er röng daginn eftir að þú teiknar hana. Í fyrirtækjum með margar uppsprettur skaltu birta ætterni í gagnaskrá svo hver notandi sjái hvaðan reitur kom og geti treyst honum í samræmi við það.

### Líttu á gagnaatvik eins og framleiðsluatvik

Vinnubrögðin sem halda þjónustum áreiðanlegum gilda beint um gögn. Gefðu hverju mikilvægu gagnasafni eiganda. Skilgreindu alvarleikastig fyrir „gagnarof“, tímabilin þegar gögn vantar, eru röng eða sein. Settu þjónustustig: ferskleikamarkmið, ásættanlega villufjárhagsáætlun og markmið um tíma til greiningar og úrlausnar. Settu gagnabakvaktalotur að baki mikilvægustu leiðslunum, skrifaðu keyrsluhandbækur og haltu eftirmálsrýni án sakbendingar eftir atvik svo sama bilun endurtaki sig ekki. Þegar greiðslutafla er sein eða opinber mælikvarði rangur er það atvik og á skilið sömu alvöru og rof. Þetta er menningarbreytingin sem lætur öll verkfærin borga sig.

### Greindu og sættu samfellt

Greining þýðir að skoða reglulega lögun gagna þinna: gildadreifingar, núllhlutföll, fjölda ólíkra gilda, lágmark og hámark og sniðmynstur. Hún dregur fram vandamál sem þú hugsaðir ekki um að staðhæfa og hún segir þér hvernig „eðlilegt“ lítur út svo þú getir sett góðar væntingar. Sátt þýðir að athuga að óháðar uppsprettur séu sammála: passar vöruhúsheildin við aðalgagnageymslukerfi uppsprettunnar, jafngildir summa hlutanna heildinni. Sjálfvirknivæddu sátt milli mikilvægra kerfa og varaðu við fráviki, því sáttarbrot er oft elsta og skýrasta merkið um að eitthvað andstreymis hafi farið úrskeiðis.

## Málamiðlanir: kostir og gallar

| Nálgun | Kostir | Gallar | Best passun |
|---|---|---|---|
| Staðhæfingapróf (hörð bilun) | Stöðvar slæm gögn kalt, skýrar fastareglur | Getur blokkað leiðslur á smávægilegum málum | Mikilvægir lyklar, tilvísunarheilindi |
| Væntingapróf (mjúk merking) | Grípur rek, minna brothætt | Þarfnast stillingar, hægt að hunsa | Dreifingar, magnbönd |
| Gagnasamningar | Kemur í veg fyrir andstreymisóvæntar uppákomur, skýrt eignarhald | Samræmingar- og stjórnunarkostnaður | Þverteymismörk framleiðanda eða notanda |
| Fráviksgreining | Grípur lúmskt, ófyrirséð rek | Viðvörunarþreyta, falskar jákvæðar | Verðmætar töflur, árstíðarmælikvarðar |
| Handvirkar stikkprufur | Ódýrt að byrja, engin verkfæri | Skalast ekki, missir af hljóðlátum villum | Aðeins mjög snemma stig |
| Fullur vöktunarvettvangur | Breið þekja, ætterni, viðvaranir | Kostnaður, uppsetning, enn eitt kerfi að reka | Margar uppsprettur, regluverkuð skýrslugerð |

Kjarnaspennan er þekja gegn hávaða. Mældu ekkert og vandamál ná til notenda þinna fyrst, sem eyðileggur traust. Mældu allt með hárvirkum viðvörunum og þú drekkir teyminu í fölskum jákvæðum þar til það þaggar niður í rásinni, sem líka lætur vandamál ná til notenda. Leystu þetta með því að raða gögnum þínum eftir sprengisvæði. Töflurnar sem fæða stjórnarmælikvarða, viðskiptavinasnúnar vörur, eftirlitsskýrslur og vélnámslíkön fá fulla meðferð: samninga, harðar staðhæfingar, vöktun og bakvaktareignarhald. Langi halinn af könnunartöflum fær létta greiningu. Eyddu áreiðanleikafjárhagsáætlun þinni þar sem röng gögn myndu skaða mest og vertu viljandi sparsamur alls staðar annars staðar.

## Spurningar til að ræða með teyminu

1. **Þegar slæm gögn ná til framleiðslu, hver kemst að því fyrst og hvernig?** Þetta er upplýsandi spurningin um áreiðanleika gagna ykkar, því heiðarlega svarið er yfirleitt „notandi, af tilviljun“. Ef greinandi, stjórnandi eða viðskiptavinur er greiningarkerfið ykkar er meðaltími ykkar til greiningar mældur í dögum og trúverðugleikinn tekur höggið í hvert sinn. Valkosturinn er mæling sem kallar eigandateymið út á bilunarstaðnum, áður en slæma talan dreifist. Komdu með raunverulegar tölur: hve mörg af síðustu tíu gagnaatvikum voru gripin af vöktun á móti tilkynnt af niðurstreymis manni og hve lengi sat hvert ógreint. Svarið segir þér hvort þið hafið vöktun eða bara von og það ætti beint að knýja hvar þið fjárfestið fyrst í ferskleika-, magn-, skema- og dreifingarathugunum.

2. **Hvaða gagnasöfn hafa eiganda, samning og þjónustustig og hver eru munaðarlaus?** Í stærð rekjast flest gagnagæðabrestir til óeigins viðmóts: framleiðsluteymi breytti einhverju án þess að hafa hugmynd um hver treysti á það, því enginn samningur sagði það. Eignarhald er grunnurinn sem gerir samninga, viðvörunarleiðir og atvikaviðbrögð möguleg og munaðarlaus gagnasöfn eru þar sem hljóðlát spilling býr. Gakktu gegnum mikilvægustu töflurnar og spyrðu fyrir hverja hver er ábyrgur, hverju framleiðandinn hefur skuldbundið sig til og hvaða ferskleika og nákvæmni notendum er lofað. Komdu með ætterni þitt: töflurnar með stærsta niðurstreymissprengisvæðið eru þær sem þurfa þetta mest og eru oft þær sem vantar það. Bilið milli „mikilvægt“ og „í eigu“ er forgangslisti ykkar fyrir næsta ársfjórðung.

3. **Hver er raunverulegur kostnaður gagnagæðaatviks fyrir okkur og meðhöndlum við það í samræmi við það?** Teymi vanfjárfesta í gagnagæðum því kostnaður slæmra gagna er dreifður og seinkaður, svo hann birtist aldrei sem línuliður, á meðan kostnaður við að smíða gæðaverkfæri er áþreifanlegur og strax. Endurrammaðu það með því að verðleggja raunverulegt atvik frá enda til enda: ranga ákvörðunin, endurvinnan, verkfræðingatímarnir sem fóru í að rekja rótarorsök án ætternis, rýrða traustið sem lætur fólk hljóðlega endurbyggja eigin skuggagagnasöfn og, í regluverkuðu eða opinberu umhverfi, leiðréttingartilkynningin og orðsporsskaði hennar. Komdu með tiltekið dæmi frá síðasta ári og leggðu það saman af heiðarleika. Ef ein hljóðlát bilun í greiðslu- eða opinberri tölfræðileiðslu gæti kostað meira en ár af vöktunarverkfærum, þá gerir málið rökin sjálft og samtalið færist frá hvort eigi að fjárfesta til hvar.

4. **Höfum við raðað gagnasöfnum okkar eftir sprengisvæði og fylgir vöktunarfjárfesting okkar í raun þeirri röðun?** Meginbilunarháttur í stærð er að eyða áreiðanleikafyrirhöfn jafnt, svo könnunartaflan sem enginn treystir fær sömu athygli og sú sem fæðir stjórnarmælikvarða, á meðan hárvirk viðvörun á lítils virði töflu kennir fólki að þagga niður í rásinni sem líka ber mikilvæga útkallið. Þú getur ekki mælt allt án þess að drukkna í hávaða og þú getur ekki mælt ekkert án þess að leyfa vandamálum að ná til notenda fyrst, svo raunverulega ákvörðunin er hvert fulla meðferðin (samningar, harðar staðhæfingar, vöktun og bakvaktareignarhald) fer og hvar létt greining dugar. Komdu með skrá yfir töflur þínar merktar eftir því hvað treystir á þær: stjórnarmælikvarðar, viðskiptavinasnúnar vörur, eftirlitsskýrslur og vélnámslíkön, berðu síðan þá röðun saman við hvar athuganir og viðvaranir sitja í raun í dag. Fyrir fyrirtæki sem sættir mörg frumkerfi eða ríkisstjórn sem birtir lögbundnar tölur tilheyra töflur með lagalega eða opinbera útsetningu efst á listanum og hvert bil milli „myndi skaða mest ef rangt“ og „er mest vaktað“ er forgangsröðunarvilla til að leiðrétta núna.

5. **Hvaða vélnámslíkön og greining taka ákvarðanir á gögnum sem við staðfestum aldrei og hvaða villur gætu þau hljóðlega kóðað?** Mælaborð sýnir einum manni ranga tölu sem gæti dregið hana í efa, en líkan þjálfast á röngum eiginleikum og kóðar þær villur inn í hverja spá sem það gerir, í stærð og ógagnsæi sem gerir skaðann langtum erfiðari að sjá eða afturkalla. Þrýstingurinn á móti er hraði: gagnavísindateymi vilja hreyfa sig hratt á nýjum eiginleikum og að bæta staðfestingu, samningum og ferskleikatryggingum við hverja veitu finnst eins og núningur þar til líkan rýrnar hljóðlega því andstreymisdálkur rak. Komdu með skrá yfir framleiðslulíkön þín og greiningu, gagnasöfnin sem hvert notar og heiðarlega merkingu á hverjar af þeim veitum hafa próf, samninga og vöktun á móti hverjar eru óvarðar. Í fyrirtækja- eða opinberu umhverfi þar sem líkan hefur áhrif á lána-, bóta- eða framfylgdarákvarðanir verða óstaðfest þjálfunargögn úttektar- og sanngirnisskuld ofan á gæðaáhættu, svo spurningin um hvaða veitur hliða líkanaútgáfu ætti að hafa eiganda og skjalfest svar (kafli 6.5).

6. **Þegar gagnagæðagalli kemur upp vikum eftir á, getum við í raun endurunnið og sætt, eða höfum við þegar fleygt því sem við þyrftum?** Margir gagnagæðabrestir eru ósýnilegir við hleðslu og verða aðeins skýrir síðar, þegar sáttarbrot eða grunsamleg þróun fær einhvern til að líta á, og þá veltur geta til að laga hreint á valum sem þú tókst miklu fyrr: hvort þú hélst óbreytanlegum hráskrám, hvort hægt er að sætta óháðar uppsprettur og hvort ætterni leyfir þér að rekja slæmu töluna til upprunans. Spennan er kostnaður og einfaldleiki gegn endurtakanleika, því að varðveita hrágögn og keyra samfellda sátt milli kerfa er ekki ókeypis og freistandi er að eyða hráum inntökum þegar umbreyttu töflurnar líta rétt út. Komdu með varðveislu- og óbreytanleikastefnu þína fyrir hrágögn, lista yfir mikilvæg kerfispör sem þið sættið sjálfvirkt og raunverulegt dæmi um galla sem þið gátuð eða gátuð ekki endurunnið ykkur út úr. Fyrir ríkisstofnun með lögbundna skyldu til að rekja hverja útgefna tölu til upprunaskráa, eða fyrirtæki sem stendur frammi fyrir eftirlitsendurútgáfu, eru óbreytanleg hrágögn og sjálfvirk sátt ekki valkvæð hreinlæti heldur búnaðurinn sem gerir leiðréttingu verjanlega.

## Sjónarhorn eftir geirum

**Sprotafyrirtæki.** Hraði og traust skipta meira máli en þekja. Settu fáein létt próf í umbreytingartólið þitt (einkvæmni og ekki-núll á lyklum, viðurkennd gildi á dálkunum sem bera merkingu, línufjöldabönd á hverja uppsprettu) og bættu ferskleika- og magnvöktun aðeins við fáu töflurnar sem fæða fyrirtækjamælikvarða þína. Beindu hverri viðvörun á eina rás sem einn verkfræðingur á og stattu gegn því að kaupa vöktunarvettvang áður en þú hefur töflurnar eða teymið til að réttlæta það. Markmiðið er að taka eftir rangmerktum reit áður en hann blæs upp tölu sem stofnendur vitna í, ekki að mæla allt.

**Lítið fyrirtæki.** Án gagnaverkfræðings og með þröngt fjárhagsáætlun skaltu halla þér að gæðaeiginleikunum sem eru þegar innbyggðir í vöruhúsið, viðskiptagreindartólið eða hugbúnaðarþjónustuna sem þú borgar fyrir frekar en að setja upp aðskilinn stafla. Beindu fyrirhöfn að fáum tölum sem raunverulega knýja ákvarðanir (tekjur, söluleiðslu, birgðir), sannreyndu þær gegn óháðri uppsprettu á reglulegum takti og líttu á ferskleika- og skemaviðvaranir seljanda sem nógu góðar þegar þær eru til. Að kaupa gæði innbyggð í verkfæri sem þú rekur nú þegar slær að smíða leiðslu sem þú hefur engan til að viðhalda.

**Stórfyrirtæki.** Vandinn er áreiðanleiki yfir mörg teymi og þúsundir taflna, svo staðlaðu viðmótið: gagnasamninga við hvert framleiðandamörk, vöktunarvettvang sem fylgist með ferskleika, magni, skema og dreifingu og ætterni birt í skrá fyrir áhrifagreiningu. Raðaðu gagnasöfnum eftir sprengisvæði, settu fráviksgreiningu og bakvaktareignarhald á þau verðmætu og keyrðu gagnaatvik gegnum sama alvarleika- og eftirmálsrýniferli og þjónusturof. Þjónustustig á leiðslunum sem fæða eftirlitsskýrslur og stjórnendamælaborð breyta áreiðanleika gagna úr væntingu í mælda, stýrða skuldbindingu.

**Hið opinbera.** Lögbundin nákvæmni og opinber ábyrgð setja viðmiðið: lentu óbreytanlegum hráum könnunar- og stjórnsýsluskrám, umbreyttu þeim í lagskiptum, prófuðum stigum og sættu gegn heildum uppsprettu á hverju skrefi. Haltu fullu ætterni svo hægt sé að rekja hverja útgefna tölu til upprunaskráa fyrir úttekt og hliðaðu hverja útgáfu á bak við staðfestingu fyrir gildi, fullkomleika og samkvæmni gegn fyrri tímabilum. Innkaup verkfæra ættu að krefjast gagnsæis og gagnaflytjanleika og röng opinber tölfræði verður að meðhöndlast sem alvarlegt atvik, með þeirri alvöru sem traust almennings á opinberum tölum krefst.

## Dæmi

**Sprotafyrirtæki.** Tuttugu manna fyrirtæki rekur markaðssetningu sína á vöruhúsi nærðu af vöruatburðum og greiðsluþjónustu. Snemma blés rangmerktur gjaldmiðilsreitur hljóðlega upp skýrðar tekjur í tvær vikur áður en nokkur tók eftir, sem hristi traust teymisins á hverju mælaborði. Þau brugðust við með léttu safni prófa í umbreytingartólinu: einkvæmni og ekki-núll á lyklum, athuganir á viðurkenndum gildum á gjaldmiðils- og stöðudálkum og línufjöldaband á hverja uppsprettu. Þau bættu við grunnferskleika- og magnvöktun á fáu töflunum sem fæða fyrirtækjamælikvarðana, beint á eina Slack-rás sem einn verkfræðingur á. Það er hógvært, en grípur bilanirnar sem skipta máli og stofnendurnir treysta tölunum aftur.

**Stórfyrirtæki.** Fjölþjóðlegur banki sættir viðskiptavina- og færslugögn úr tugum frumkerfa í stýrt vöruhús sem fæðir eftirlitsskýrslur, áhættulíkön og stjórnendamælaborð. Hann rekur gagnasamninga við hver framleiðandamörk, svo andstreymisskemabreyting er útgáfustýrð og samið um hana frekar en skellt á notendur. Vöktunarvettvangur fylgist með ferskleika, magni, skema og dreifingu yfir þúsundir taflna, með fráviksgreiningu á þeim verðmætu og ætterni birt í gagnaskrá fyrir áhrifagreiningu. Gagnaatvik fylgja sama alvarleika- og bakvaktarferli og þjónusturof, með þjónustustigum á leiðslunum sem fæða eftirlitsskil. Þegar frumkerfi rekur er eigandateymið kallað út og niðurstreymisskýrslurnar sem urðu fyrir áhrifum þekktar innan mínútna, ekki uppgötvaðar af eftirlitsaðila.

**Hið opinbera.** Landsbundin hagstofa birtir efnahagsvísitölur sem markaðir, stefnumótendur og almenningur líta á sem áreiðanlegar, svo nákvæmni er lögbundin skylda og hver útgefin tala verður að vera úttektarhæf. Leiðslur hennar lenda óbreytanlegum hráum könnunar- og stjórnsýsluskrám, umbreyta þeim síðan í lagskiptum, prófuðum stigum með sátt gegn heildum uppsprettu á hverju skrefi. Fullt ætterni leyfir greinendum að rekja hverja útgefna tölu til upprunaskráa, sem er bæði gæðatól og lagakrafa. Fyrir útgáfu standast tölur staðfestingarhlið fyrir gildi, fullkomleika og samkvæmni gegn fyrri tímabilum og öll frávik eru rannsökuð og skjalfest frekar en birt. Röng opinber tölfræði er alvarlegt atvik, svo stofnunin meðhöndlar gagnarof með þeirri alvöru sem traust almennings krefst.

## Viðskiptarök: hvatar, ávöxtun fjárfestingar og heildarkostnaður

Ávöxtun gagnagæða og gagnavöktunar kemur af varðveittu trausti, styttum atvikum og forðuðum slæmum ákvörðunum. Traustverð gögn eru grunnurinn sem lætur hverja niðurstreymisfjárfestingu í greiningu, viðskiptagreind og gervigreind borga sig í raun, því líkan eða mælaborð er aðeins jafn gott og gögnin undir því. Þegar gæðaathuganir grípa slæma hleðslu við mörkin forðastu langtum stærri kostnað þess að röng tala nái til ákvörðunar, viðskiptavinar eða skýrslu. Ætterni styttir rótarorsakarannsókn úr dögum af handvirkri rakningu í mínútur, sem er hrein endurheimt verkfræðitími. Vöktun skerðir meðaltíma til greiningar frá „þegar notandi kvartar“ til „þegar leiðslan bilar“, sem er þar sem mestur traustskaði er forðaður.

Heildareignarkostnaður felur í sér verkfæri fyrir prófanir, vöktun og skráningu, auk verkfræðitíma til að mæla leiðslur og skipulagsvinnu við að úthluta eigendum og skrifa samninga. Þetta er raunverulegt, en vegðu það gegn kostnaði þess að gera það ekki: hljóðlát spilling uppgötvuð af stjórnendum, vélnámslíkön þjálfuð á slæmum eiginleikum sem kóða villur í stærð, greinendur sem hljóðlega endurbyggja skuggagagnasöfn því þeir treysta ekki lengur opinberu og, í regluverkuðu eða opinberu umhverfi, leiðréttingartilkynningar sem skaða trúverðugleika árum saman. Til stjórnenda skaltu ramma gagnagæði sem tryggingu á hverja gagnadrifna ákvörðun sem skipulagsheildin tekur. Iðgjaldið er hóflegt og fyrirsjáanlegt. Ótryggða tapið, ein áberandi röng tala, er hvorugt.

## Andmynstur og gildrur

- Að líta á gagnagæði sem einskiptis hreinsunarverkefni í stað viðvarandi verkfræðivenju.
- Að uppgötva bilanir frá niðurstreymisnotendum frekar en frá vöktun á bilunarstaðnum.
- Ekkert gagnasafnseignarhald, svo enginn er ábyrgur þegar eitthvað brotnar og enginn er kallaður út.
- Framleiðendur sem breyta skemum eða merkingu án samnings, sem brýtur hljóðlega hvern notanda.
- Fráviksviðvaranir svo hávaðasamar að teymið þaggar niður í rásinni og missir af raunverulega atvikinu.
- Að fæða vélnámslíkön beint á óstaðfestum gögnum, sem kóðar villur í stærð (kafli 6.5).
- Að viðhalda ætterni sem handteiknaðri skýringarmynd sem er röng daginn eftir að þú teiknar hana.
- Að elta fullkomin gögn alls staðar í stað hæfra gæða á töflunum sem skipta máli.
- Að eyða hrágögnum, svo þú getur ekki endurunnið eða sætt þegar gæðagalli kemur upp síðar.

## Þroskalíkan

- **Stig 1, Upphaf:** Gæði eru starf einskis. Vandamál finnast af notendum, yfirleitt eftir að röng tala nær skýrslu. Engin próf, engin vöktun, ekkert eignarhald. Lagfæringar eru handvirk slökkvivinna og sömu bilanirnar endurtaka sig.
- **Stig 2, Þróun:** Sum teymi bæta við grunnprófum á mikilvægar töflur sínar (lyklar, núll, viðurkennd gildi) og örlítilli ferskleika- og magnvöktun á gagnasöfnunum sem þau láta sig mestu varða. Vinnubrögðin virka þar sem þau eru til, en þekja og nákvæmni eru ólík eftir teymum, ekkert er staðlað og atvik eru enn meðhöndluð viðbragðsdrifið.
- **Stig 3, Stöðlun:** Gæðavíddir eru skilgreindar með þröskuldum og sömu væntingar gilda yfir teymi frekar en að velta á því hver smíðaði leiðslu. Gagnasamningar stýra lykilmörkum framleiðenda, vöktun nær yfir ferskleika, magn, skema og dreifingu á mikilvægum töflum og ætterni styður áhrifagreiningu. Hvert mikilvægt gagnasafn hefur nefndan eiganda og gagnaatvik fylgja skjalfestu alvarleika- og viðbragðsferli um skipulagsheildina.
- **Stig 4, Stjórnun:** Gæði og áreiðanleiki eru mæld og stýrð gegn grunnlínum. Gagnarof er rakið með raunverulegum mælikvörðum: meðaltími til greiningar, meðaltími til úrlausnar, ferskleiki og nákvæmni gegn samþykktum þjónustustigum og villufjárhagsáætlanir sem gagnasafn getur eytt áður en það kallar fram aðgerð. Sáttarbrotahlutföll, árangurshlutföll prófa og falskar-jákvæðar-hlutföll fráviksgreiningar eru rakin yfir tíma, viðvaranir eru stilltar gegn þeim tölum frekar en eftir ágiskun og ákvarðanir um fara eða ekki fara á gagnaútgáfu eru teknar á mældum gæðum gegn grunnlínu frekar en von.
- **Stig 5, Samhæfing:** Gæði og vöktun eru allsráðandi, sjálfvirk og aðlögunarhæf. Fráviksgreining grípur lúmskt rek, samningum er framfylgt vélrænt og ætterni er fangað sjálfvirkt og birt í skrá. Gögn hafa þjónustustig og bakvaktareignarhald eins og framleiðsluþjónustur, sátt keyrir samfellt og eftirmálsrýni án sakbendingar nærir stöðuga minnkun gagnarofs. Gæði eru samþætt gagnastjórnun, vélnámi og viðskiptaskipulagningu og skipulagsheildin endurmarkar stöðugt þröskulda, þekju og eignarhald eftir því sem gagnalandslagið breytist.

## Hugmyndir til umræðu

1. Hverjar af töflum ykkar myndu valda mestum skaða ef þær væru hljóðlega rangar í viku og eru það þær sem þið vaktið mest?
2. Hvar hefði gagnasamningur komið í veg fyrir síðasta andstreymisvaldna atvik ykkar og hvers vegna var enginn til?
3. Hve mikinn verkfræðitíma tekur dæmigerð rótarorsakarannsókn í dag og hve miklu myndi sjálfvirkt ætterni spara?
4. Eru einhver vélnámslíkana ykkar að þjálfast á gögnum sem þið staðfestið ekki og hvaða villur gætu þau verið að kóða?
5. Er viðvörunarstilling ykkar nógu góð til að fólk bregðist við hverri viðvörun, eða hefur einhver þaggað niður í rásinni?
6. Hvaða ferskleika- og nákvæmnisþjónustustig myndu mikilvægustu notendur ykkar í raun skrifa undir og gætuð þið mætt þeim í dag?

## Helstu atriði

- Gagnagæði eru hæfni til notkunar yfir nákvæmni, fullkomleika, samkvæmni, tímanleika, gildi og einkvæmni.
- Slæm gögn eru verri en engin gögn, því þau spilla ákvörðunum og líkönum hljóðlega.
- Prófaðu gögn eins og kóða: staðhæfinga- og væntingapróf auk skemaathugana, í CI og í framleiðslu.
- Notaðu gagnasamninga til að gera væntingar framleiðenda og notenda skýrar og framfylgjanlegar.
- Fylgstu með ferskleika, magni, skema og dreifingu, í hliðstæðu við hugbúnaðarvöktun (kafli 9.2).
- Fangaðu ætterni fyrir hraða rótarorsaka- og áhrifagreiningu og birtu það fyrir notendur.
- Líttu á gagnaatvik eins og framleiðsluatvik, með eignarhaldi, alvarleika og þjónustustigum.
- Mældu þar sem röng gögn skaða mest. Stefndu að hæfum gæðum, ekki fullkomnun alls staðar.

## Heimildir og frekari lestur

- Barr Moses, Lior Gavish, and Molly Vorwerck, "Data Quality Fundamentals."
- Jacek Majchrzak, Sven Balnojan, and Marian Siwiak, "Data Contracts."
- Danette McGilvray, "Executing Data Quality Projects."
- Thomas C. Redman, "Data Driven: Profiting from Your Most Important Business Asset."
- Laura Sebastian-Coleman, "Measuring Data Quality for Ongoing Improvement."
- Joe Reis and Matt Housley, "Fundamentals of Data Engineering."
- DAMA International, "DAMA-DMBOK: Data Management Body of Knowledge."
- ISO/IEC 25012, "Data quality model."
