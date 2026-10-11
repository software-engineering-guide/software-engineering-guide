# 10.3 Innkaup, opinn hugbúnaður og leyfi

## Yfirlit og tilgangur

Nær sérhvert nútímalegt hugbúnaðarkerfi er að mestu sett saman úr íhlutum sem einhver annar skrifaði. [Opinn hugbúnaður](https://en.wikipedia.org/wiki/Open-source_software) myndar grunn stýrikerfa, tungumála, rammaverka, gagnagrunna og skýjainnviða. Hann kemur inn í fyrirtækið á tvo vegu: gegnum yfirvegað [innkaup](https://en.wikipedia.org/wiki/Procurement) og gegnum óformlegar `import` setningar einstakra forritara. Þessi kafli fjallar um að sinna þeirri notkun (og, þar sem það á við, framlagi) af ásetningi. Það þýðir stefnu, leyfisfylgni, skilning á skyldum og copyleft-áhættu og áætlun fyrir óhjákvæmileg [endalok líftíma](https://en.wikipedia.org/wiki/End-of-life_(product)) íhlutanna sem þú ert háð(ur).

Fyrir stór teymi eru húfin í senn lagaleg, rekstrarleg og stefnumótandi. Lagalega eru [leyfi](https://en.wikipedia.org/wiki/Software_license) opins hugbúnaðar framfylgjanlegir samningar með raunverulegar skyldur. Að fara rangt með [copyleft](https://en.wikipedia.org/wiki/Copyleft) (leyfisveitingu sem getur krafist þess að afleidd verk séu deild undir sömu skilmálum) getur í versta falli neytt til birtingar séreignarkóða eða ræst málaferli. Leyfisbrot geta jafnvel hindrað yfirtöku eða almennt útboð í [áreiðanleikakönnun](https://en.wikipedia.org/wiki/Due_diligence). Rekstrarlega rotna óstýrð ósjálfstæði: íhlutir hætta að vera viðhaldnir, safna veikleikum og ná endalokum líftíma á meðan þeir eru enn grafnir djúpt í framleiðslu. Stefnumótandi er opinn hugbúnaður meira en kostnaðarsparandi inntak. Hann er leið til að forðast [innilokun](https://en.wikipedia.org/wiki/Vendor_lock-in), laða að hæfileikafólk og móta vistkerfin sem þú ert háð(ur), kostir sem þú nærð aðeins ef þú tekur þátt af ásetningi.

Hið opinbera hefur aukavídd. Mörg lögsagnarumdæmi hafa nú skýra stefnu sem styður opinn hugbúnað, opna staðla og kóðadeilingu milli stofnana. Þetta er oft orðað sem „almannafé, almenningskóði“: meginreglan að hugbúnaður fjármagnaður af skattgreiðendum ætti sjálfgefið að vera aðgengilegur almenningi. Verkfræðingar hjá hinu opinbera verða því að rata bæði um leyfisfylgni og virk umboð til að kjósa, birta og endurnýta opinn hugbúnað. Þessi kafli stefnir að því að gera allt þetta viðráðanlegt í stærð.

## Meginreglur

- **Opinn hugbúnaður er aðfangakeðja, ekki ókeypis dót.** Líttu á íhluti sem þú notar með sama aga og hvern mikilvægan seljanda.
- **Leyfi eru skyldur, ekki heimildir til að hunsa.** Sérhvert ósjálfstæði ber skilmála. Þekktu þá áður en þú sendir frá þér.
- **Copyleft er hönnunarskorða, ekki bannorð.** Copyleft-leyfi eru nothæf og verðmæt. Þau krefjast bara þess að þú skiljir hvernig þú sameinar og dreifir hugbúnaði.
- **Notaðu af ásetningi, leggðu til af stefnu.** Ákveddu hvað á að taka inn og, þar sem það þjónar þér, fjárfestu í að senda upp til upprunaverkefnis frekar en að greina.
- **Gerðu skrá yfir allt.** Þú getur ekki fylgt, tryggt eða uppfært það sem þú sérð ekki. SBOM (hugbúnaðarefnisskrá, heildarskrá yfir íhluti í hugbúnaði þínum) er lágmark.
- **Skipuleggðu endalok líftíma frá upphafi.** Sérhvert ósjálfstæði verður einn daginn óviðhaldið. Þekktu útgönguleið þína áður en þú neyðist í eina.
- **Hjá hinu opinbera, hafðu opið sjálfgefið.** Kjóstu [opna staðla](https://en.wikipedia.org/wiki/Open_standard) og opinn hugbúnað og birtu kóða fyrir almannafé nema sérstök ástæða sé til annars.

## Ráðleggingar

### Settu stefnu um opinn hugbúnað og notkunarreglur

Birtu skýra stefnu um hvernig forritarar mega koma með opinn hugbúnað inn í skipulagsheildina: hvaða leyfi eru fyrirfram samþykkt, hver krefjast rýni og hver eru bönnuð fyrir þín notkunartilvik. Veittu hraða, núningslitla samþykktarleið. Stefna sem er hægari en að afrita kóða verður einfaldlega hunsuð. Aðgreindu samhengi, því sama leyfi hegðar sér ólíkt þegar íhlutur er notaður innanhúss sem þjónusta, felldur inn í dreifða vöru eða tengdur inn í séreignarforrit. Gerðu auðveldu leiðina að leið samræmis: sérvalin innri geymsla yfirfarinna íhluta, sjálfvirk skönnun í leiðslunni og skýr leiðsögn sem forritarar geta fylgt án þess að hringja í lögfræðing í hefðbundnum tilvikum.

### Stýrðu leyfisfylgni, skyldum og copyleft-áhættu

Kynntu þér leyfisfjölskyldurnar og skyldur þeirra. [Frjálsleg leyfi](https://en.wikipedia.org/wiki/Permissive_software_license) (svo sem MIT, BSD og Apache 2.0) krefjast aðallega þakkar og varðveislu tilkynninga. Apache 2.0 bætir við skýru einkaleyfisveitingaákvæði. Veikt copyleft (svo sem [LGPL](https://en.wikipedia.org/wiki/GNU_Lesser_General_Public_License) og MPL) krefst þess að þú deilir breytingum á skránum sem leyfið nær yfir en leyfir almennt að þú sameinir við séreignarkóða. Sterkt copyleft (svo sem [GPL](https://en.wikipedia.org/wiki/GNU_General_Public_License)) getur krafist þess að allt dreifða verkið sé boðið undir sömu skilmálum. Netcopyleft ([AGPL](https://en.wikipedia.org/wiki/GNU_Affero_General_Public_License)) víkkar þá skyldu til hugbúnaðar sem boðinn er yfir net, ekki bara dreift sem tvíundarskrám. Skyldurnar sem skipta mestu ráðast af tvennu: hvort þú dreifir hugbúnaðinum og hve þétt þú sameinar íhluti. Sjálfvirknivæddu samræmi: skannaðu ósjálfstæði eftir leyfum, búðu til og sendu nauðsynlegar þakkar- og tilkynningaskrár og hliðaðu smíðina á stefnu svo bannað leyfi geti ekki læðst hljóðlega í framleiðslu.

### Komdu á skrifstofu opins hugbúnaðar (OSPO)

Ef þú notar opinn hugbúnað í stærð skaltu búa til miðpunkt, OSPO, sem á stefnu um opinn hugbúnað, stefnumörkun, tól fyrir samræmi, stjórn framlaga og samfélagstengsl. OSPO dregur úr glundroða þess að hvert teymi taki eigin ákvarðanir. Hún veitir sérfræðiþekkingu sem einstök teymi geta ekki viðhaldið. Og hún nær stefnumótandi verðmæti: að ákveða í hvaða verkefni á að fjárfesta, hvenær á að leggja upp til upprunaverkefnis og hvernig á að gefa út eigin opin verkefni vel. Jafnvel lítil OSPO (stundum ein manneskja auk þverfaglegs vinnuhóps) bætir samræmi verulega og dregur úr lagalegri áhættu miðað við frjálsa-fyrir-alla.

### Stýrðu framlögum og, þar sem við á, útgáfu

Ákveddu af ásetningi hvenær á að leggja til baka. Að senda lagfæringar og eiginleika upp til verkefna sem þú ert háð(ur) dregur úr viðhaldsbyrði þinni, því þú hættir að bera einkaplástra. Það byggir líka velvild og áhrif og styrkir íhluti sem eru þér mikilvægir. Gefðu forriturum skýrt, hratt ferli fyrir samþykkt framlög, þar á meðal hvernig hugverkaréttindi og framlagssamningar eru meðhöndluð. Þegar þú gefur út eigin opin verkefni skaltu gera það almennilega: veldu viðeigandi leyfi, skjalfestu stjórnarhætti og skuldbindu þig til ráðsmennsku. Yfirgefið verkefni skaðar orðspor þitt meira en ekkert verkefni.

### Mættu opinberum umboðum um opinn hugbúnað og „almannafé, almenningskóða“

Teymi hjá hinu opinbera ættu að líta á opnun sem sjálfgefið. Kjóstu opna staðla til að forðast innilokun og til að vinna þvert á stofnanir og seljendur. Birtu frumkóða þróaðan fyrir almannafé opinskátt nema sértæk, skjalfest undanþága eigi við: fyrir öryggisviðkvæma íhluti, réttindi þriðja aðila eða persónuverndarsjónarmið. Endurnýttu áður en þú smíðar: athugaðu hvort önnur stofnun hafi þegar gefið út hentugan kóða. Bakaðu þessar væntingar inn í innkaup, svo seljendur afhendi opinn, endurnýtanlegan, vel skjalfestan kóða með viðeigandi réttindum hjá hinu opinbera, frekar en séreignarsvarta kassa sem stofnunin getur hvorki viðhaldið né deilt.

### Stýrðu ósjálfstæði og hugbúnaði á endalokum líftíma

Haltu lifandi skrá (SBOM) yfir hvern íhlut og útgáfu hans, leyfi og viðhaldsstöðu. Haltu ósjálfstæði sæmilega nýlegum. Litlar, tíðar uppfærslur eru langtum ódýrari og öruggari en sjaldgæf, risastór stökk. Fylgstu með upprunaverkefnum fyrir tilkynningar um endalok líftíma og öryggisstuðningsglugga og skipuleggðu flutninga áður en stuðningi lýkur, ekki eftir að veikleiki þvingar fram æði. Fyrir mikilvæga íhluti í hættu á yfirgefningu skaltu ákveða fyrirfram hvort þú fjármagnar viðhaldsaðilann, leggur til viðhald sjálf(ur), greinir eða skiptir út. Fylgstu með endalokum líftíma bæði fyrir hugbúnað til sölu og opinn og haltu því að stuðningur sé á þrotum við sama staðal og hverja aðra rekstraráhættu.

## Málamiðlanir: kostir og gallar

| Val | Kostir | Gallar |
|---|---|---|
| Notaðu opinn hugbúnað frjálslega | Hröð afhending. Mikil áhrif. Engin leyfisgjöld | Leyfis-, öryggis- og viðhaldsskyldur sem þú átt nú |
| Ströng leyfisheimildaskrá | Lítil lagaleg áhætta. Fyrirsjáanlegt | Hægir á teymum. Getur útilokað sannarlega gagnlega íhluti |
| Aðeins frjálsleg leyfi | Lágmarksskyldur. Auðvelt að sameina | Fórnar verðmætum copyleft-verkefnum. Minna gagnkvæmni |
| Samþykktu copyleft þar sem hentar | Aðgangur að sterkum vistkerfum. Gagnkvæmniávinningur | Krefst aðgátar við sameiningu og dreifingu |
| Leggðu upp til upprunaverkefnis | Minni einkaplástrabyrði. Áhrif. Velvild | Viðvarandi fyrirhöfn. Hugverka- og ferlakostnaður |
| Smíðaðu séreign í staðinn | Full stjórn. Engar ytri skyldur | Hár kostnaður. Finnur upp hversdagsvöru. Þú heldur því við að eilífu |
| Opinber birting sjálfgefin | Gagnsæi. Endurnýting. Forðar innilokun | Birtingarfyrirhöfn. Öryggisrýni. Viðvarandi ráðsmennska |

Kjarnaspennan er milli hraða forritara og stjórnar. Læstu allt á bak við þunga rýni og forritarar fara fram hjá stefnunni. Það skapar óstýrð skuggaósjálfstæði, sem eru verri en frjálslynd-en-sýnileg nálgun. Skildu allt eftir óstýrt og þú safnar lagalegri og öryggisskuld ósýnilega. Lausnin er sjálfvirkni og sérval: gerðu samræmisleiðina að hröðustu leiðinni, gegnum fyrirfram yfirfarna íhluti, leiðsluskönnun og skýr sjálfgildi, svo þú fáir stjórn án núnings. Varðandi copyleft er málamiðlunin ekki „áhættusamt á móti öruggu“ heldur „skilið á móti óskilið.“ Copyleft er fullkomlega nothæft þegar þú veist hvernig þú sameinar og dreifir.

## Spurningar til að ræða með teyminu

1. **Hver er skýr regla ykkar um sterkt copyleft og netcopyleft í innri, dreifðum og netþjónuðum samhengjum?** Copyleft er hönnunarskorða, ekki bannorð, og skyldurnar ráðast af tvennu: hvort þú dreifir hugbúnaðinum og hve þétt þú sameinar íhluti. GPL í innra verkfæri hegðar sér mjög ólíkt GPL tengdu inn í vöru sem þú sendir frá þér og AGPL víkkar birtingarskyldur til hugbúnaðar sem þú býður bara yfir net, sem breytir smíða-eða-taka-upp útreikningnum fyrir allt sem þú rekur sem þjónustu. Skrifaðu regluna niður fyrir hvert samhengi, svo forritari viti án þess að hringja í lögfræðing að (til dæmis) frjálslegt er fyrirfram samþykkt alls staðar, sterkt copyleft er í lagi innanhúss en lokað frá afhentu vörunni og AGPL þarfnast rýni áður en það snertir netþjónustu. Komdu með sönnunargögn: skannaðu núverandi ósjálfstæðistré og finndu hvar copyleft-íhlutir sitja nú þegar miðað við dreifingarmörk ykkar. Hliðaðu síðan smíðina á þeirri stefnu, því regla sem enginn skanni framfylgir er regla sem forritarar brjóta óvart.

2. **Þurfið þið skrifstofu opins hugbúnaðar og hver á leyfisstefnu, skönnun og framlagsákvarðanir í dag?** Ef heiðarlega svarið er „enginn“ eða „hvert teymi ákveður“ rekið þið frjálsa-fyrir-alla sem safnar lagalegri og öryggisskuld ósýnilega. OSPO, jafnvel ein manneskja auk þverfaglegs vinnuhóps, dregur úr þeim glundroða og nær stefnumótandi verðmæti: í hvaða upprunaverkefni á að fjárfesta, hvenær á að leggja til og hvernig á að gefa út eigin verkefni vel. Komdu með sönnunargögn á fundinn: getur einhver framvísað núverandi samþykktum leyfislista, SBOM og nafni þess sem myndi svara copyleft-spurningu í áreiðanleikakönnun vegna yfirtöku? Svarið ætti að úthluta skýru eignarhaldi og gera samræmisleiðina að hröðustu leiðinni, gegnum fyrirfram yfirfarna íhluti og leiðsluskönnun, svo forritarar fái stjórn án núnings. Stefna sem er hægari en að afrita kóða verður einfaldlega hunsuð.

3. **Hvaða ósjálfstæði myndu skaða mest ef þau væru yfirgefin á morgun og hver er fyrirfram ákveðin viðbrögð ykkar fyrir hvert?** Sérhvert ósjálfstæði nær endalokum líftíma að lokum og dýra útgáfan af þeim atburði er að uppgötva að kjarnaíhlutur missti stuðning fyrir mánuðum, aðeins þegar veikleiki þvingar fram athygli. Fyrir mikilvæga íhluti ykkar í hættu á yfirgefningu skaltu ákveða fyrirfram hvort þið fjármagnið viðhaldsaðilann, leggið til viðhald sjálf, greinið eða skiptið út. Komdu með sönnunargögn: úr SBOM ykkar, listaðu íhlutina sem bilun myndi stöðva tekju- eða verkefnismikilvæga þjónustu og skráðu viðhaldsstöðu og öryggisstuðningsglugga hvers. Svarið ætti að breyta endalokum líftíma úr óvæntu í rakta rekstraráhættu með áætluðum flutningi, haldna við sama staðal og hver önnur áhætta. Að halda ósjálfstæði nýlegu í litlum, tíðum skrefum er langtum ódýrara en sjaldgæft, risastórt, þvingað stökk.

4. **Getið þið framleitt fullkomna, núverandi SBOM sem nær alla leið niður ósjálfstæðistréð ykkar, og hve hratt?** Þegar áberandi veikleiki lendir í víða notuðu safni er fyrsta spurning forystunnar „erum við útsett og hvar?“ Teymi sem getur ekki svarað innan klukkustunda er þegar á eftir, því raunverulega áhættan felst yfirleitt nokkrum lögum niðri í ósjálfstæðum sem enginn valdi viljandi. Samkeppnissjónarmiðið er kostnaður og hávaði: full óbein skrá yfir margar þjónustur býr til stóran, sífellt breytilegan lista og of margar viðvaranir kenna fólki að hunsa hann, svo þú þarft að ákveða hvaða dýpt og hvaða alvarleiki ræsir raunverulega aðgerð. Komdu með sönnunargögn í umræðuna: prófaðu að búa til ferska SBOM fyrir eina framleiðsluþjónustu núna, teldu hve margir íhlutir eru beinir á móti óbeinum og tímasettu hve langan tíma það tók. Fyrir fyrirtæki eða opinbera stofnun skaltu tengja þetta við áþreifanlegt atvikaviðbragðsmarkmið og við hvaða lagaskyldu sem er til að upplýsa um íhluti sem verða fyrir áhrifum, því umboð til að skýra frá útsetningu sem þú getur ekki talið upp er umboð sem þú munt brjóta.

5. **Hvenær er mikilvægt ósjálfstæði þess virði að fjármagna, leggja til eða hafa ráðsmennsku yfir, frekar en að líta á það sem ókeypis?** Flestar skipulagsheildir nota opinn hugbúnað eins og veitu og verða svo hissa þegar íhlutur sem ber tekjuþjónustu reynist vera einn ólaunaður sjálfboðaliði. Að ákveða af ásetningi að fjármagna viðhaldsaðila, senda lagfæringar upp eða gefa út og hafa ráðsmennsku yfir eigin verkefni breytir brothættu ókeypis inntaki í varanlegt, áhrifum beitt inntak og það hættir að láta verkfræðinga ykkar bera einkaplástra gegnum hverja uppfærslu. Spennan er að framlag og ráðsmennska kosta raunverulegan, viðvarandi verkfræðitíma og bera hugverka- og ferlakostnað, svo þú getur ekki gert það fyrir allt. Komdu með sönnunargögn: úr SBOM þinni, merktu handfylli íhluta sem bilun myndi stöðva verkefnismikilvæga þjónustu og skráðu fjölda viðhaldsaðila, fjármögnun og hve marga einkaplástra þú berð nú þegar gegn hverjum. Fyrir stóra eða opinbera skipulagsheild skaltu vega orðsporskostnað yfirgefinnar opinnar útgáfu sem þú birtir með látum og, hjá hinu opinbera, líta á viðvarandi ráðsmennsku yfir birtum kóða fyrir almannafé sem hluta af afhendingunni, ekki valkvæðan aukahlut.

6. **Skilar innkaup ykkar í raun opnum, endurnýtanlegum, vel skjalfestum kóða með réttindunum sem þið þurfið, eða séreignarsvörtum kössum sem þið getið hvorki viðhaldið né yfirgefið?** Samningar skrifaðir án sérfræðiþekkingar á opnum hugbúnaði afhenda seljanda reglulega stjórn sem þú munt sjá eftir: lokuð snið, engan rétt til að birta eða breyta og ósjálfstæði sem stofnunin getur ekki lagfært þegar seljandinn heldur áfram. Að koma þessu rétt fyrir snemma er langtum ódýrara en að uppgötva við endurnýjun að þú getur ekki farið. Samkeppnissjónarmiðin eru hraði og val á seljendum: að krefjast opinna afhendinga og flytjanleika getur þrengt hópinn og seinkað úthlutun og sumir sannarlega gagnlegir birgjar standa á móti. Komdu með sönnunargögn: dragðu fram tvo nýlega samninga og athugaðu hvort þeir tilgreini leyfisskilmála, afhendingu frumkóða, skjölunarstaðla, SBOM-afhendingu og réttindin sem skipulagsheildin heldur. Fyrir fyrirtækjainnkaup skaltu tengja þetta við innilokun og heildarkostnaðargreiningu. Fyrir hið opinbera skaltu tengja það við opið-sjálfgefið og „almannafé, almenningskóða“ umboð og við skjalfesta undanþáguferlið sem leyfir þér að loka aðeins öryggisviðkvæmu hlutunum frekar en öllu kerfinu.

## Sjónarhorn eftir geirum

**Sprotafyrirtæki.** Þú setur næstum allt saman úr opnum hugbúnaði og hefur engan lögfræðing, svo haltu reglunni á einni blaðsíðu: frjálsleg leyfi eins og MIT og Apache 2.0 eru fyrirfram samþykkt, sterkt copyleft er í lagi fyrir innri verkfæri en lokað frá afhentu vörunni og allt skrýtið fær skjóta rýni stofnanda. Bættu leyfis- og veikleikaskönnun við leiðsluna og haltu SBOM frá fyrsta degi, því ódýrasta augnablikið til að gera þetta rétt er áður en áreiðanleikakönnun kaupanda kembir ósjálfstæðistréð þitt. Bannaðu ekki copyleft af ótta. Skildu það og haltu áfram.

**Lítið fyrirtæki.** Án sérfræðings í opnum hugbúnaði og þröngt fjárhagsáætlun skaltu hallast að verkfærum frekar en mannskap: skanni í smíðinni og stuttur samþykktur leyfislisti vinna mest af því sem manneskja myndi gera. Rammaðu notkun sem kaupa-á-móti-smíða heiðarlega, því að finna upp vel viðhaldinn opinn íhlut að nýju er yfirleitt dýra valið, en það er líka að vera háð einum sem þú skráir aldrei. Haltu einfaldri skrá yfir hvað þú notar og undir hvaða leyfi, svo öryggisspurningalisti viðskiptavinar eða veikleikaviðvörun verði ekki að æði.

**Stórfyrirtæki.** Í stærð er vandinn samræmi milli margra teyma, svo komdu upp OSPO sem á stefnu, sjálfvirka skönnun, þakkarskrárgerð og stjórn framlaga og gerðu samræmisleiðina að hröðustu leiðinni gegnum sérvalda, fyrirfram yfirfarna íhluti. Framfylgdu copyleft-reglum eftir samhengi í leiðslunni, haltu SBOM yfir þjónustur og stýrðu nýleika ósjálfstæðis og endalokum líftíma sem rakinni rekstraráhættu. Líttu á opinn hugbúnað sem aðfangakeðjustjórnun fyrir meirihluta kóðagrunns þíns, með úttektarhæfum sönnunargögnum fyrir áreiðanleikakönnun vegna yfirtöku.

**Hið opinbera.** Opnun er oft skylduð, ekki valkvæð, svo hafðu opna staðla sjálfgefna og birtu kóða fyrir almannafé nema skjalfest undanþága eigi við vegna öryggis, réttinda þriðja aðila eða persónuverndar. Endurnýttu áður en þú smíðar með því að athuga þverstofnanaskrá og bakaðu opnar, endurnýtanlegar, vel skjalfestar afhendingar og varðveitt réttindi inn í innkaup svo þú fáir viðhaldanlegan kóða í stað séreignarsvartra kassa. Haltu birtum kóða við raunverulega ráðsmennsku og hafðu undanþáguferlið þröngt og gagnsætt svo það loki aðeins því sem það verður.

## Dæmi

**Sprotafyrirtæki.** Fjögurra manna sprotafyrirtæki sem smíðar farsímaforrit setur nær allt saman úr opnum hugbúnaði og hefur engan lögfræðing í starfsliði. Í stað þess að banna copyleft af ótta skrifa stofnendurnir einnar blaðsíðu stefnu: frjálsleg leyfi eins og MIT og Apache 2.0 eru fyrirfram samþykkt, sterkt copyleft eins og GPL er í lagi fyrir innri verkfæri en lokað frá afhenta forritinu til að forðast birtingarskyldur og allt óvenjulegt fær skjóta rýni stofnanda. Þeir bæta leyfis- og veikleikaskönnun við leiðsluna svo bannað leyfi læðist ekki inn í útgáfu, halda SBOM frá fyrsta degi og senda litla lagfæringu upp til mikilvægs safns svo þeir hætti að bera einkaplástur gegnum hverja uppfærslu. Að gera þetta rétt snemma sparar þeim líka sársaukafullt áfall þegar áreiðanleikakönnun kaupanda kembir að lokum ósjálfstæðistréð.

**Stórfyrirtæki.** Hugbúnaðarseljandi sem sendir frá sér dreifða vöru rekur OSPO. OSPO viðheldur samþykktum leyfislista, innri sérvalinni íhlutageymslu og sjálfvirkri leyfis- og veikleikaskönnun í hverri leiðslu. Þegar forritari dregur inn nýtt ósjálfstæði athugar leiðslan leyfi þess gegn stefnu, býr til þakkartilkynningarnar sem fylgja vörunni og merkir allt sem krefst rýni. Sterk copyleft-íhlutir eru leyfðir fyrir innri verkfæri en lokaðir frá dreifðu vörunni, til að forðast birtingarskyldur. Fyrirtækið sendir lagfæringar upp til nokkurra mikilvægra ósjálfstæða. Það útrýmdi bakstöðu einkaplástra sem verkfræðingar þess báru áður gegnum hverja uppfærslu.

**Hið opinbera.** Landsbundin stafræn þjónusta starfar undir stefnunni „almannafé, almenningskóði“. Nýjar þjónustur eru smíðaðar á opnum stöðlum, þróaðar opinskátt í opinberri kóðageymslu sjálfgefið og endurnýttar milli stofnana. Innkaupasniðmát hennar krefjast þess að seljendur afhendi opinn, vel skjalfestan, endurnýtanlegan kóða, með réttindum ríkisins til að birta og breyta. Áður en nýr íhlutur er hafinn leita teymi í þverstofnanaskrá að fyrirliggjandi endurnýtanlegum kóða. Öryggisviðkvæmar einingar eru undanskildar birtingu með skjalfestu ferli, frekar en með því að gera allt kerfið lokað.

## Viðskiptarök: hvatar, ávöxtun fjárfestingar og heildarkostnaður

Að stýra opnum hugbúnaði vel er munurinn á að ná gríðarlegum áhrifum hans og að greiða fyrir falinn kostnað hans. Opinn hugbúnaður leyfir stórri skipulagsheild að standa á grunni sem hún gæti aldrei haft efni á að smíða. En [heildareignarkostnaðurinn](https://en.wikipedia.org/wiki/Total_cost_of_ownership) felur í sér samræmi, öryggisplástrun og endanlegan flutning, kostnað sem berst hvort sem þú skipuleggur hann eða ekki. Yfirveguð stjórn breytir ófyrirsjáanlegum, dýrum kreppum í lítinn, jafnan, áætlaðan kostnað. Þessar kreppur fela í sér copyleft-brot sem uppgötvast í áreiðanleikakönnun vegna yfirtöku, neyðarflutning af yfirgefnum íhlut eða veikleika í ósjálfstæði sem enginn vissi að væri til.

Upptökukostnaðurinn er hóflegur miðað við útsetninguna: OSPO eða vinnuhópur, skönnunartól og agi þess að halda skrá. Kostnaðurinn við að taka það *ekki* upp birtist sem lagaleg ábyrgð, misheppnuð áreiðanleikakönnun, öryggisatvik rakin til óplástraðra ósjálfstæða og vaxandi kostnaður frestaðra uppfærslna sem þvinga að lokum fram sársaukafulla stórflutninga. Þegar þú færir rök við forystu skaltu ramma stjórn opins hugbúnaðar sem aðfangakeðjustjórnun fyrir meirihluta kóðagrunns þíns. Nefndu líka stefnumótandi ávinninginn: forðuð innilokun, hraðari afhending, hæfileikaaðdráttur og áhrif á vistkerfin sem þú ert háð(ur). Hjá hinu opinbera skaltu bæta við umboðsvíddinni. Opnun er oft krafist, ekki valkvæð, og að gera það vel forðar bæði vanfylgni og tvítekinni opinberri eyðslu.

## Andmynstur og gildrur

- **Afrita-og-líma leyfisveiting.** Forritarar draga inn íhluti án leyfisathugunar og uppgötva skyldur aðeins við úttekt eða yfirtöku.
- **Engin skrá.** Að geta ekki svarað „hvað erum við að nota og undir hvaða leyfi?“ þegar veikleiki eða leyfisspurning brýst út.
- **Copyleft-ofsahræðsla.** Að banna allt copyleft af ótta frekar en skilningi og fórna verðmætum vistkerfum.
- **Yfirgefna opna útgáfan.** Að birta verkefni með látum og viðhalda því svo aldrei, sem skaðar orðspor.
- **Að hunsa óbein ósjálfstæði.** Að yfirfara bein ósjálfstæði á meðan raunverulega áhættan felst nokkrum lögum niðri.
- **Endalokaáfall.** Að uppgötva að kjarnaíhlutur missti stuðning fyrir mánuðum, aðeins þegar veikleiki þvingar fram athygli.
- **Stefna hægari en afritun.** Samræmisferli svo þungt að forritarar fara fram hjá því og skapa ósýnileg skuggaósjálfstæði.
- **Svartir kassar hins opinbera.** Að kaupa séreignarkerfi sem stofnunin getur hvorki viðhaldið, deilt né yfirgefið, í bága við opið-sjálfgefið meginreglur.

## Þroskalíkan

**Stig 1: Upphaf.** Forritarar bæta við opnum hugbúnaði frjálslega án stefnu eða skrár. Leyfi eru órannsökuð og copyleft-skyldur óþekktar. Endalok líftíma uppgötvast fyrir slysni, yfirleitt þegar veikleiki þvingar fram athygli. Enginn á stefnu um opinn hugbúnað.

**Stig 2: Þróun.** Grunnstefna og samþykktur leyfislisti eru til og sum teymi fylgja þeim. Skönnun gerist, en oft handvirkt, seint eða aðeins á fáum verkefnum. Skrá er haldin fyrir stór kerfi á meðan óbein ósjálfstæði eru ókortlögð. Framlög og meðhöndlun endaloka líftíma er ad hoc og ósamræmd milli teyma.

**Stig 3: Stöðlun.** OSPO eða sambærilegt á stefnu, stefnumörkun og tól um skipulagsheildina. Leyfis- og veikleikaskönnun er sjálfvirk í hverri leiðslu, þakkar- og tilkynningaskrár eru búnar til sjálfvirkt og smíðin er hliðuð svo bannað leyfi komist ekki inn. SBOM eru viðhaldnar niður óbeina tréð, framlög fylgja skjalfestu ferli, endalok líftíma eru rakin með áætluðum flutningum og teymi hins opinbera birta sjálfgefið.

**Stig 4: Stjórnun.** Áætlunin er mæld og stýrð gegn grunnlínum. Þú rekur skönnunarþekju stefnu yfir þjónustur, meðaltíma til að plástra birtan ósjálfstæðisveikleika, hlutfall íhluta innan öryggisstuðningsglugga síns, flóttahlutfall leyfisbrota, nýleikabil ósjálfstæðis og fjölda einkaplástra sem sendir hafa verið upp. Staðsetning copyleft miðað við dreifingarmörk er vöktuð og mælikvarðar gegn markmiðum knýja hverja fara eða ekki-fara ákvörðun frekar en skoðun.

**Stig 5: Samhæfing.** Opinn hugbúnaður er stöðugt bætt stefnumótandi eign samþætt um skipulagsheildina. Samræmi er fullkomlega sjálfvirkt og íhlutir sem uppfylla það ekki komast ekki í framleiðslu. Þú fjárfestir af ásetningi í mikilvægum upprunaverkefnum, leggur reglulega til og hefur ráðsmennsku yfir eigin vel reknum verkefnum. Nýleiki ósjálfstæðis og endalok líftíma eru stýrð aðlögunarhæft eftir því sem áhætta og mælikvarðar breytast og opnun verður raunverulegur samkeppnis- og borgaralegur kostur.

## Hugmyndir til umræðu

- Hvar er rétta línan milli hraðs frjálslegs sjálfgildis og stjórnarinnar sem þarf til að forðast lagalega og öryggisskuld?
- Hvenær ætti skipulagsheild að fjármagna eða viðhalda mikilvægu upprunaósjálfstæði frekar en að líta á það sem ókeypis?
- Hvernig ákveður þú hverja eigin íhluta þinna er vert að gefa út og hafa ráðsmennsku yfir sem opinn hugbúnað?
- Fyrir hið opinbera, hvað er verjanlegt ferli til að undanskilja íhluti birtingu-sjálfgefið án þess að grafa undan meginreglunni?
- Hve djúpt inn í óbein ósjálfstæði verður leyfis- og öryggisrýni raunhæft að ná?
- Breytir netcopyleft (AGPL) smíða-eða-taka-upp útreikningi þínum fyrir hugbúnað sem þú býður sem þjónustu?

## Helstu atriði

- Opinn hugbúnaður er meirihluti flestra kóðagrunna og verður að stýra sem aðfangakeðju, ekki líta á hann sem ókeypis og afleiðingalausan.
- Leyfi bera raunverulegar skyldur. Skildu frjálsleg, veik-copyleft, sterk-copyleft og net-copyleft fjölskyldurnar og hvernig dreifing og sameining ræsa skyldur.
- Gerðu samræmisleiðina að hröðustu leiðinni gegnum sérval, sjálfvirka skönnun og skýr sjálfgildi, annars fara forritarar fram hjá stefnunni.
- Komdu upp OSPO til að eiga stefnumörkun, samræmi, framlög og ráðsmennsku í stærð.
- Haltu SBOM, haltu ósjálfstæði nýlegu í litlum skrefum og skipuleggðu endalok líftíma áður en hann þvingar fram kreppu.
- Hjá hinu opinbera, hafðu opna staðla sjálfgefna og birtu kóða fyrir almannafé, endurnýttu áður en þú smíðar.

## Heimildir og frekari lestur

- Heather Meeker, *Open (Source) for Business* and *Open Source for Business*
- Van Lindberg, *Intellectual Property and Open Source*
- The Linux Foundation and TODO Group, *OSPO guides* and *Open Source Program Office resources*
- OpenChain (ISO/IEC 5230), *Open Source Licence Compliance*
- Software Package Data Exchange (SPDX, ISO/IEC 5962) specification
- CycloneDX SBOM specification
- Free Software Foundation, *GNU General Public Licence* and *GPL FAQ*
- Open Source Initiative, *The Open Source Definition* and approved licence list
- Free Software Foundation Europe, *Public Money, Public Code*
- U.S. Federal Source Code Policy and Code.gov guidance
- UK Government, *Technology Code of Practice* and open-standards principles
