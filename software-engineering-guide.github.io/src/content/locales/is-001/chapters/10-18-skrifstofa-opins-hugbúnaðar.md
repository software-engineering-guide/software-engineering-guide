# 10.18 Skrifstofa opins hugbúnaðar (OSPO) og framlög til upprunaverkefna

## Yfirlit og tilgangur

Skipulagsheild þín keyrir þegar á [opnum hugbúnaði](https://en.wikipedia.org/wiki/Open-source_software): stýrikerfin, tungumálin, gagnagrunnarnir og söfnin sem bera vöru þína eru að mestu skrifuð af fólki sem vinnur ekki fyrir þig. Kafli 10.3 fjallar um innkaup og leyfisfylgni og kafli 10.12 um valið milli opins og lokaðs. Þessi kafli fjallar um hlutverkið sem gerir allt það samfellt: [skrifstofu opins hugbúnaðar](https://en.wikipedia.org/wiki/Open_Source_Program_Office) (OSPO), teymið sem á hvernig fyrirtækið notar, leggur til og gefur út opinn hugbúnað. OSPO er þungamiðja sambands sem annars dreifist yfir hvern verkfræðing sem skrifar `import`.

Flestar skipulagsheildir rata inn í opinn hugbúnað eitt ósjálfstæði í einu og uppgötva síðan uppsafnaða útsetningu í einu: leyfisspurningu í áreiðanleikakönnun vegna yfirtöku, mikilvægt safn með einum örmagna viðhaldsaðila, öryggisráðgjöf í kóða sem enginn vissi að þeir sendu frá sér. OSPO breytir því æði í stýrða getu. Hún setur notkunarstefnu sem gerir kleift frekar en að hindra, ákveður hvenær framlag til upprunaverkefnis þjónar rekstrinum, hefur ráðsmennsku yfir verkefnunum sem þú gefur út og beitir opnu samstarfi innan fyrirtækisins gegnum [InnerSource](https://en.wikipedia.org/wiki/Inner_source). Þetta er stefnumótandi hlutverk, tengt verkfræðigildum þínum (kafli 1.1), ekki gátreitur fyrir reglufylgni.

Fyrir fyrirtæki er drifkrafturinn stærð: þúsundir ósjálfstæða, útflutnings- og leyfisskyldur yfir lögsagnarumdæmi og hundruð verkfræðinga sem hver tekur smáar ákvarðanir um opinn hugbúnað daglega. Ein skrifstofa gefur þeirri útbreiðslu hrygg. Fyrir hið opinbera er drifkrafturinn stefna og almannatraust. „Opið sjálfgefið“ og „almannafé, almenningskóði“ eru í auknum mæli lög, svo opinberir aðilar þurfa einhvern sem getur birt kóða á öruggan hátt, endurnýtt yfir stofnanir og haldið seljendum við opna staðla. Í báðum aðstæðum borgar OSPO sig með því að breyta ósýnilegri, óverðlagðri áhættu í yfirvegaða, fjárhagsáætlaða vinnu.

## Meginreglur

- **Opinn hugbúnaður er tvíhliða samband, ekki ókeypis vöruhús.** Þú notar, þú leggur til og þú gefur út og OSPO á allt þrennt.
- **Framlag er stefna, ekki góðgerðir.** Að senda upp til upprunaverkefnis dregur úr kostnaði við að bera einkaplástra og kaupir þér áhrif.
- **Gerðu hraðleiðina mögulega, ekki gæta hliðsins.** Stefna sem er hægari en að afrita kóða verður hunsuð, svo gerðu samræmisleiðina þá fljótustu.
- **Fjármagnaðu viðhaldsaðilana sem þú ert háð(ur).** Sameiginlegt er ekki sjálfbært af sjálfu sér og mikilvægasta safn þitt gæti haft einn ólaunaðan höfund.
- **Hafðu ráðsmennsku yfir því sem þú gefur út, eða gefðu það ekki út.** Yfirgefið verkefni skaðar orðspor þitt meira en ekkert verkefni myndi nokkru sinni gera.
- **Mældu þátttöku svo þú getir bætt hana.** Teldu framlög, ósjálfstæðisheilsu og tíma til samþykktar, ekki fréttatilkynningar.
- **Hjá hinu opinbera, hafðu opið sjálfgefið og birtu sjálfgefið.** Opnun er normið. Lokun er skjalfest undantekning.

## Ráðleggingar

### Komdu upp OSPO í stærð sem passar veruleika þínum

Þú þarft ekki stórt teymi til að byrja. Í sprotafyrirtæki getur OSPO verið einn verkfræðingur með skriflegt umboð og nokkrar klukkustundir á viku. Í fyrirtæki er hún lítill miðlægur hópur auk valddreifðs nets málsvara innbyggðra í vöruteymi. Hver sem stærðin er, gefðu henni skýra stofnskrá sem nær yfir fjórar skyldur: notkunarstefnu og reglufylgni, framlag til upprunaverkefna, útgáfu og ráðsmennsku eigin verkefna og samfélags- og fjármögnunartengsl. Settu hana þar sem hún sér bæði verkfræði og lögfræði, oft með skýrslugjöf til tæknistjóra eða varaforseta verkfræði með punktalínu til lögfræði og öryggis. Bilunarhátturinn er OSPO sem býr alfarið innan lögfræðinnar og verður hemill. Lagfæringin er að manna hana verkfræðingum sem senda, svo leiðsögn hennar beri trúverðugleika hjá teymunum sem hún þjónar.

### Notaðu á ábyrgan hátt og gerðu örugga leið að auðveldri leið

Notkun er þar sem mest áhætta kemur inn, svo gerðu góða hegðun áreynslulausa. Veittu sérvalda innri skrá yfir fyrirfram yfirfarna íhluti, sjálfvirka leyfis- og veikleikaskönnun í leiðslunni og skýr sjálfgildi sem forritari getur fylgt án þess að skrá miða. Styddu þig við leyfisagann í kafla 10.3 og aðfangakeðju- og ósjálfstæðisheilsuvenjurnar í kafla 2.18: festu útgáfur, búðu til hugbúnaðarefnisskrá, fylgstu með [hugbúnaðaraðfangakeðjunni](https://en.wikipedia.org/wiki/Software_supply_chain) fyrir brotin eða yfirgefin pakka og raktu endalok líftíma áður en hann þvingar fram flutning. Starf OSPO er ekki að samþykkja hvert ósjálfstæði handvirkt. Það er að byggja varnarteinana svo níutíu og fimm prósent vala séu sjálfkrafa örugg og aðeins raunverulega óvenjuleg tilfelli nái til manneskju.

### Leggðu til upprunaverkefna því það borgar sig, ekki því það er fallegt

Líttu á framlag til upprunaverkefna sem hagfræðilega ákvörðun. Sérhver einkaplástur sem þú berð gegn ósjálfstæði er skattur sem þú borgar á hverri uppfærslu, að eilífu, þar til breytingin lendir í upprunaverkefninu eða greinin víkur svo langt að þú átt hana alfarið. Að leggja lagfæringuna til baka eyðir þeim skatti. Að senda upp kaupir líka áhrif á stefnu, svo vegvísir íhlutar sem þú reiðir þig á beygist að þörfum þínum, og það gefur til kynna hæfni til verkfræðinganna sem þú vilt ráða. Gefðu forriturum þínum hraða, skjalfesta leið: fyrirfram samþykktan framlagsleyfissamning eða Developer Certificate of Origin, létt samþykki sem staðfestir að breytingin sé örugg að deila og stjórnendatíma fjárhagsáætlaðan fyrir vinnuna. Þegar valkosturinn er að viðhalda varanlegri [grein](https://en.wikipedia.org/wiki/Fork_(software_development)) af verkefni sem þú stýrir ekki er framlag til baka nánast alltaf ódýrara.

### Gefðu út eigin verkefni með raunverulegum stjórnarháttum

Þegar þú opnar hugbúnað sem þú smíðaðir skaltu gera það yfirvegað eða alls ekki. Ákveddu fyrst hvort kóðinn sé hversdagsvara sem er vert að deila eða aðgreinir sem er vert að halda lokuðum, með rökunum úr kafla 10.12. Ef þú gefur út skaltu velja leyfi sem passar ásetningi þínum (frjálslegt til að hámarka upptöku, copyleft til að halda vistkerfinu gagnkvæmu), skjalfesta hver ákveður hvað gegnum skriflegt stjórnarháttalíkan og skrá [vörumerkið](https://en.wikipedia.org/wiki/Trademark) á nafn verkefnisins svo þú getir varið það gegn misnotkun á meðan kóðinn er frjáls. Skuldbindu þig til raunverulegrar ráðsmennsku: opinberan villuskráningarlista, framlagsleiðbeiningar, siðareglur og öryggisstefnu með samræmdri birtingu svo tilkynnendur viti hvernig þeir ná til þín (kafli 4.2). Nefndu viðhaldsaðila og fjárhagsáætlaðu tíma hans. Verkefni sem þú opnar með látum og yfirgefur ári síðar gerir meira tjón á orðspori þínu en verkefni sem þú sendir aldrei.

### Beittu InnerSource til að eiga samstarf innan fyrirtækisins

Venjurnar sem láta opinn hugbúnað virka (opinberar geymslur, skýrar framlagsleiðbeiningar, rýni eftir verðleikum, lágur þröskuldur fyrir fyrsta plástur) virka alveg eins vel á bak við eldvegginn. InnerSource þýðir að hver verkfræðingur getur fundið, notað og bætt hvert innra verkefni, og sent beiðni um sameiningu yfir teymismörk í stað þess að skrá miða og bíða. Þetta brýtur niður einangrun, dreifir endurnotkun kóða og þjálfar fólk þitt í nákvæmlega vinnuflæðinu sem það mun nota þegar það leggur til út á við. OSPO er eðlilegt heimili InnerSource því hún á þegar verkfærin og menningarhandbókina. Byrjaðu með fáeinum verðmætum sameiginlegum söfnum, birtu framlagsleiðbeiningar þeirra innanhúss og umbunaðu teymum sem taka við utanaðkomandi plástrum af þokka.

### Fjármagnaðu og viðhaldið viðhaldsaðilunum sem þú ert háð(ur)

Framleiðslukerfi þitt gæti hvílt á safni viðhaldið af einni manneskju í frítíma sínum. Það er aðfangakeðjuáhætta og heiðarlega viðbragðið er að hjálpa til við að bera byrðina. Greindu mikilvægustu ósjálfstæði þín úr efnisskránni, finndu þau með þunnan viðhaldsgrunn og veldu viðbragð fyrir hvert: styrktu viðhaldsaðilann beint, leggðu til verkfræðitíma, gakktu í stofnun sem fjármagnar verkefnið eða, sem síðasta úrræði, búðu þig undir að greina eða skipta út. Að fjármagna sameiginlegt er ódýrara en neyðarástandið sem fylgir hruni þess og það heldur íhlutunum sem þú reiðir þig á heilbrigðum og á hreyfingu í átt sem þú getur haft áhrif á.

### Settu framlagsstefnu sem samþykkir hratt

Framlagsstefna er til að segja já hratt, ekki nei hægt. Skilgreindu hvað verkfræðingur má leggja til án þess að spyrja (villulagfæringar, skjöl, litla eiginleika í verkefni sem þú notar nú þegar), hvað þarf létta athugun (allt sem snertir aðgreini eða einkaleyfi) og hvernig hugverk og framlagssamningar eru meðhöndlaðir einu sinni, miðlægt, frekar en á hvert framlag. Sjálfvirknivæddu leiðinlegu hlutana: leyfisathuganir, fyrirfram undirritaðan fyrirtækjaframlagssamning og vélmenni sem flaggar sjaldgæfu innsendinguna sem þarfnast mannsaugna. Mældu tíma til samþykktar og líttu á hæga biðröð sem galla í stefnunni.

## Málamiðlanir: kostir og gallar

| Nálgun | Kostir | Gallar |
| --- | --- | --- |
| Miðlæg OSPO | Samræmd stefna, djúp sérfræðiþekking, skýrt eignarhald | Getur orðið flöskuháls ef hún aðeins hliðar og gerir aldrei kleift |
| Valddreifð OSPO (málsvarar í teymum) | Skalast, heldur ákvörðunum nærri verkfræðingum | Þarfnast sterkrar samhæfingar annars rekur stefna í sundur |
| Leggja til upprunaverkefna | Eyðir einkaplástraskatti, kaupir áhrif, hjálpar ráðningum | Viðvarandi fyrirhöfn, IP-rýni, vinna á tímaáætlun annars |
| Bera einkagreinar | Full stjórn, senda á eigin tímaáætlun | Varanlegur viðhaldsskattur, rekur frá öryggislagfæringum upprunaverkefnis |
| Gefa út eigið verkefni | Vistkerfi, orðspor, sameiginlegt viðhald | Raunverulegur ráðsmennskukostnaður. Yfirgefning skaðar orðspor |
| Fjármagna viðhaldsaðila | Ver mikilvæg ósjálfstæði, kaupir velvild | Beinn kostnaður og að velja hverja á að fjármagna er pólitískt |
| Engin OSPO (ad hoc) | Enginn uppsetningarkostnaður | Ósýnileg lagaleg, öryggis- og sjálfbærniskuld |

Meginspennan er milli stjórnar og þess að gera kleift. OSPO sem rýnir hvert ósjálfstæði og hvert framlag handvirkt finnst örugg, en hún verður það sem verkfræðingar fara fram hjá, sem framleiðir ósýnilegu skuggaósjálfstæðin sem þú varst að reyna að koma í veg fyrir. OSPO sem aðeins birtir glaðlega leiðsögn án nokkurrar sjálfvirkrar framfylgdar er hunsuð um leið og frestur nálgast. Lausnin er sú sama og rennur í gegnum kafla 10.3: sjálfvirknivæddu algenga tilfellið svo samræmisleiðin sé fljótasta leiðin og taktu frá mannlega dómgreind fyrir hið sannarlega nýja. Fáðu þetta jafnvægi rétt og skrifstofan er margfaldari krafts. Fáðu það rangt í hvora átt sem er og hún er annaðhvort hemill eða skraut.

## Spurningar til að ræða með teyminu

1. **Hver á samband ykkar við opinn hugbúnað í dag og gæti hann svarað erfiðri spurningu á morgun?** Ef lögfræðingar mögulegs kaupanda bæðu um leyfisskrá ykkar, eða blaðamaður spyrði hvaða óviðhaldið safn situr í greiðsluslóð ykkar, er nafn fest við svarið? Fyrir flestar skipulagsheildir er heiðarlega svarið „enginn,“ sem þýðir að hver verkfræðingur er hljóðlega að móta stefnu og enginn ber ábyrgð á summunni. Komdu með sönnunargögnin á fundinn: reyndu að framleiða samþykkta leyfislistann, hugbúnaðarefnisskrána og manneskjuna sem myndi svara copyleft-spurningu í áreiðanleikakönnun. Ef þessi gögn eru ekki til eða vísa á engan hefur þú fundið fyrsta OSPO-verkefni þitt. Ákvörðunin sem þarf að taka er ekki hvort eigi að hafa hlutverkið heldur hver á það og hvaða umboð hann ber, jafnvel þótt skrifstofan sé ein manneskja einn dag í viku.

2. **Berið þið einkaplástra sem þið gætuð sent upp og hvað kostar það ykkur?** Mörg teymi viðhalda hljóðlátum haug staðbundinna breytinga gegn ósjálfstæðum sínum, beita þeim aftur handvirkt á hverri uppfærslu og taka á sig sameiningarsársaukann eins og hann væri náttúrulögmál. Hver þessara plástra er endurtekinn skattur og hver er kandídat til að leggja til baka svo skatturinn hverfi. Komdu með sérstöðuna: listaðu greinarnar og staðbundnu plástrana sem smíði ykkar ber í raun, metdu verkfræðiklukkustundirnar sem hver kostar á ári og skráðu hvaða upprunaverkefni myndu líklega taka við breytingunni. Samkeppnissjónarmiðið er raunverulegt, því að senda upp tekur fyrirhöfn núna og gengur á tímaáætlun viðhaldsaðilans, en samanburðurinn er við að borga plástraskattinn að eilífu. Svarið ætti að breyta „við beitum honum alltaf aftur“ í yfirvegað val, með framlagsleið nógu hraða til að verkfræðingar noti hana.

3. **Hvaða ósjálfstæði myndi skaða mest ef viðhaldsaðilinn gengi burt og hvað ætlið þið að gera í því?** Einhvers staðar í staflanum ykkar er íhlutur sem myndi stöðva tekju- eða verkefnismikilvæga þjónustu ef hann brotnaði, viðhaldinn af manneskju eða handfylli sem þið hafið aldrei fjármagnað eða þakkað. Sameiginlegt finnst ókeypis allt þar til augnablikið sem það er það ekki og dýra útgáfan af þeim lærdómi er æði eftir yfirgefningu eða óplástraðan veikleika. Komdu með efnisskrána þína og raðaðu ósjálfstæðum eftir sprengisvæði, skráðu síðan fjölda viðhaldsaðila og fjármögnunarstöðu efstu fáu. Fyrir hvert mikilvægt, þunnt mannað ákveddu fyrirfram hvort þið styrkið, leggið til tíma, gangið í stofnun eða búið ykkur undir að skipta út. Það breytir dulinni stakri bilunarpunkt í stýrt samband, haldið við sama staðal og hver önnur rekstraráhætta (kafli 2.18).

4. **Áður en þið opnið næsta innra verkfæri, eruð þið tilbúin að hafa ráðsmennsku yfir því árum saman, eða eruð þið að senda opnun og óhjákvæmilega afsökunarbeiðni?** Opinber útgáfa er viðvarandi skuldbinding: villuskráningarlisti sem einhver verður að flokka, öryggispósthólf sem einhver verður að vakta og nafn sem einhver verður að verja. Teymi seilast í að opna til að hjálpa ráðningum eða velvilja og uppgötva síðan að yfirgefið verkefni með gömlum villum skaðar orðsporið sem þau vonuðust til að byggja, meira en að senda ekkert hefði gert. Komdu með sönnunargögnin: listaðu verkefnin sem þið hafið þegar gefið út og sýndu fyrir hvert aldur opinna villna, hvort nefndur viðhaldsaðili hafi fjárhagsáætlaðar klukkustundir, hvort það hafi stjórnarháttalíkan, skráð vörumerki og samræmda birtingarstefnu og hvort kóðinn sé hversdagsvara sem er vert að deila eða aðgreinir sem þú ættir að halda lokuðum (kafli 10.12). Samkeppnissjónarmiðið er að raunveruleg ráðsmennska kostar verkfræðitíma sem þú gætir eytt í vöruna, svo heiðarlega valið er oft að gefa út færri hluti og hafa ráðsmennsku yfir þeim almennilega. Fyrir fyrirtæki þýðir þetta lögfræði- og vörumerkjarýni fyrir opnun. Fyrir hið opinbera þýðir það að vörumerkið, birtingarleiðin og undanþáguferli birta-sjálfgefið séu útkljáð áður en geymslan verður opinber.

5. **Hve langan tíma tekur það verkfræðing í raun að fá ósjálfstæði samþykkt eða framlag hreinsað og er það hægara en að fara fram hjá ykkur?** Opið hugbúnaðarstefna keppir beint við hraðasta lausnaleið sem verkfræðingur getur fundið og hvert ferli hægara en að afrita kóðann verður sniðgengið, sem framleiðir ósýnileg skuggaósjálfstæði sem skrifstofan átti að koma í veg fyrir. Spennan er stjórn gegn því að gera kleift: hver handvirk rýni bætir við úttektarslóð og grípur sjaldgæft raunverulegt vandamál, en bætir líka við töf sem ýtir miðgildistilfellinu af samræmisleiðinni. Komdu með tölurnar á fundinn: mælda tímann til samþykktar fyrir staðlað ósjálfstæði og staðlað framlag, hlutfall ákvarðana sem eru meðhöndlaðar sjálfvirkt á móti af manneskju og fjölda undantekninga sem í raun þurftu dómgreind síðasta ársfjórðung. Í fyrirtæki með hundruð verkfræðinga sem hver tekur smáar ákvarðanir daglega verður tveggja daga biðröð hljóðlega að þúsundum sniðgenginna rýna. Hjá hinu opinbera rekst sama töfin á innkaupa- og úttektarskyldur sem krefjast pappírsslóðarinnar sem lausnaleiðin sleppir, svo lagfæringin er að sjálfvirknivæða algenga tilfellið frekar en að manna stærra hlið.

6. **Hver innri verkefna ykkar myndu hagnast mest á InnerSource og hvað kemur í veg fyrir að annað teymi sendi ykkur beiðni um sameiningu í dag?** Venjurnar sem láta opinn hugbúnað virka (opinberar geymslur, framlagsleiðbeiningar, rýni eftir verðleikum, lágur þröskuldur fyrir fyrsta plástur) borga sig á bak við eldvegginn með því að brjóta niður einangrun, dreifa endurnotkun og þjálfa fólk í nákvæmlega vinnuflæðinu sem það mun nota til að leggja til út á við. Samkeppnissjónarmiðið er að opnun innra verkefnis krefst framlagsleiðbeininga, afgangs rýnigetu og ákvörðunar um hvaða kóði verður að vera takmarkaður vegna öryggis eða regluverks. Komdu með sérstöðuna: nefndu verðmætu sameiginlegu söfnin, skráðu hver birta nú þegar innri framlagsleiðbeiningar og lýstu hvernig þvert teymi beiðni um sameiningu er meðhöndluð í dag, hvort hún er velkomin eða týnd í biðröð. Fyrir fyrirtæki er ávinningurinn mældur í tvítekinni innri smíði forðað yfir mörg teymi. Hjá hinu opinbera nær sama venja yfir stofnanamörk sem endurnotkun milli stofnana, svo að birta-sjálfgefið og sameiginlegir íhlutir dragi úr tvítekinni opinberri eyðslu frekar en að margfalda hana.

## Sjónarhorn eftir geirum

**Sprotafyrirtæki.** Gefðu skrifstofuna einum nefndum verkfræðingi í nokkrar klukkustundir á viku með einnar blaðsíðu stofnskrá, ekki nefnd. Hafðu frjálsleg leyfi sjálfgefin með skanna í leiðslunni, sendu upp aðeins fáu einkaplástrana sem í raun skaða á hverri uppfærslu og komdu upp litlum mánaðarlegum styrk fyrir safnið viðhaldið af einum sem þú getur sannarlega ekki lifað án. Hraði skiptir meira máli en þekja hér: samræmisleið hraðari en að afrita kóða slær ítarlega stefnu sem enginn fylgir.

**Lítið fyrirtæki.** Þú munt ekki manna sérstaka OSPO, svo keyptu getuna innbyggða í verkfærum sem þú rekur nú þegar: skanna sem flaggar leyfis- og veikleikavandamálum og sérvalda skrá yfir fyrirfram yfirfarna íhluti. Rammaðu vinnuna sem leyfisfylgni- og ósjálfstæðisheilsuhreinlæti frekar en áætlun: vittu hvað er í hugbúnaðarefnisskrá þinni, vittu hvað hvert leyfi skyldar þig til og vittu hvaða eins-viðhaldsaðila ósjálfstæði myndi skaða ef það hyrfi. Kjóstu að kaupa skönnun og skráningu fram yfir að smíða eigin.

**Stórfyrirtæki.** Keyrðu litla miðlæga skrifstofu auk valddreifðs nets málsvara innbyggðra í vöruteymi, svo stefna haldist samræmd á meðan ákvarðanir haldast nærri verkfræðingum. Sjálfvirknivæddu leyfis-, veikleika- og útflutningsskönnun, náðu yfir hvern verkfræðing með fyrirfram samþykktum framlagssamningi og raktu tíma til samþykktar sem skýrðan mælikvarða. Fjármagnaðu stofnanirnar á bak við mikilvæg ósjálfstæði þín, keyrðu InnerSource yfir margar geymslur og stýrðu allri eigninni sem safni með heilsu- og þátttökumælikvörðum frekar en dreifðum einstökum ákvörðunum.

**Hið opinbera.** Starfaðu undir opið-sjálfgefið og almannafé-almenningskóði: birtu nýjar þjónustur í opinberri geymslu nema skjalfest öryggis- eða persónuverndarundanþága eigi við. Keyrðu þverstofnanaskrá svo teymi endurnýti áður en þau smíða, skrifaðu kröfur um opinn hugbúnað og opna staðla inn í innkaup svo seljendur afhendi endurnýtanlegan kóða með réttindum varðveittum og sinntu samræmdri öryggisbirtingu fyrir það sem þú birtir. Fjármagnaðu viðhald sameiginlegra safna sem nokkrar stofnanir eru háðar, svo ekkert eitt teymi eigi hljóðlega innviði sem öll ríkisstjórnin treystir á.

## Dæmi

**Sprotafyrirtæki.** Tuttugu manna sprotafyrirtæki gerir aðalvettvangsverkfræðing sinn að hlutastarfs OSPO-eiganda með einnar blaðsíðu stofnskrá. Hún setur einfalda notkunarstefnu (frjálsleg leyfi fyrirfram samþykkt, copyleft rýnt, skanni í leiðslunni) og tekur eftir að teymið ber þrjá einkaplástra gegn opnu biðraðarsafni, beitt aftur sársaukafullt á hverri uppfærslu. Hún sendir alla þrjá upp. Tveir eru samþykktir innan mánaðar og eyða uppfærsluskattinum fyrir fullt og allt. Hún opnar eitt lítið innra verkfæri með raunverulegri README, leyfi og öryggistengilið, aðallega til að laða að verkfræðinga, og kemur upp mánaðarlegum styrk fyrir safnið sem viðhaldinn er af einum sem varan er háð. Ekkert af þessu þarf mannskap, aðeins nefndan eiganda og skýrt umboð.

**Stórfyrirtæki.** Alþjóðlegur banki rekur miðlæga OSPO sex manna auk valddreifðs nets málsvara opins hugbúnaðar innbyggðra í hvern vöruhóp. Miðlæga teymið á stefnuna, sjálfvirka leyfis- og útflutningsreglufylgniskönnun og framlagsleyfissamninginn sem hver verkfræðingur er undir frá fyrsta degi. Málsvararnir sinna staðbundinni rýni og þjálfa teymi sín í framlagi. Bankinn fjármagnar nokkrar stofnanir þar sem verkefni bera viðskiptakerfi hans, leggur lagfæringar upp til víða notaðs gagnarammaverks svo hann hætti að viðhalda grein og keyrir InnerSource yfir tvö hundruð innri geymslur svo hvaða teymi sem er geti sent beiðni um sameiningu til hvaða annars. Tími til samþykktar fyrir staðlað framlag er undir tveimur dögum, rakinn sem mælikvarði sem OSPO skýrir frá ársfjórðungslega.

**Hið opinbera.** Landsbundin stafræn stofnun starfar undir umboði „opinn hugbúnaður sjálfgefið“ og almannafé-almenningskóði. OSPO hennar birtir nýjar þjónustur í opinberri geymslu nema skjalfest undanþága eigi við vegna öryggis eða persónuverndar, rekur þverríkisstjórnarskrá svo stofnanir endurnýti kóða áður en þær smíða hann og skrifar kröfur um opinn hugbúnað og opna staðla inn í innkaup svo seljendur afhendi endurnýtanlegan, vel skjalfestan kóða með réttindi ríkisins varðveitt. Skrifstofan sinnir líka samræmdri öryggisbirtingu fyrir kóðann sem hún birtir og fjármagnar viðhald sameiginlegs auðkenningarsafns sem nokkrar stofnanir eru nú háðar, svo ekkert eitt teymi eigi hljóðlega íhlut sem öll ríkisstjórnin reiðir sig á.

## Viðskiptarök: hvatar, ávöxtun fjárfestingar og heildarkostnaður

Skýrasta ávöxtunin er útrýming forðanlegra, dýrra óvæntra atburða. Óstýrður opinn hugbúnaður framleiðir kreppur sem berast á eigin tímaáætlun: copyleft-brot sem kemur upp í áreiðanleikakönnun vegna yfirtöku, neyðarflutning af dauðum íhlut, brot rakið til ósjálfstæðis sem engin skrá taldi upp. OSPO breytir þessum lágu-líkinda, háa-kostnaðar atburðum í stöðuga, fjárhagsáætlaða vinnu. Bættu við endurteknum sparnaði af upprunasendingum: hver einkaplástur sem þú leggur niður hættir að skattleggja hverja framtíðaruppfærslu og yfir stóra eign samsetur það í raunverulega verkfræðigetu sem er skilað til vinnu við vöruna.

Á [heildareignarkostnaðar](https://en.wikipedia.org/wiki/Total_cost_of_ownership) bókhaldinu er skrifstofan ódýr miðað við það sem hún ver. Kostnaður hennar er lítið teymi, einhver skönnunar- og skráningarverkfæri og hóflegur viðhaldsaðilastyrkur. Berðu það saman við kostnaðinn af því að hafa hana ekki: lagalega ábyrgð, misheppnaða eða seinkaða áreiðanleikakönnun, öryggisatvik, tvítekna innri smíði á hlutum sem þegar eru til sem opinn hugbúnaður og hægt blæðandi greinar sem enginn valdi að halda. Það eru líka ávinningar sem erfiðara er að verðleggja en eru raunverulegir: áhrif á stefnu íhluta sem þú ert háð(ur), ráðninga- og orðsporsforskot af trúverðugri opinni viðveru og hraðari afhending því verkfræðingar endurnýta frekar en endursmíða. Þegar þú færir rök við forystu skaltu ramma OSPO sem aðfangakeðjustjórnun fyrir meirihluta kóðagrunns þíns, með stefnumótandi arð ofan á. Hjá hinu opinbera skaltu bæta við reglufylgnivíddinni, því opnun er oft krafist og að gera hana vel forðar bæði vanfylgni og tvítekinni opinberri eyðslu.

## Andmynstur og gildrur

- **OSPO sem hlið.** Skrifstofa sem aðeins rýnir og hindrar, gerir aldrei kleift, er sniðgengin og framleiðir skuggaósjálfstæðin sem hún átti að koma í veg fyrir.
- **Framlagsleikhús.** Að tilkynna opna hugbúnaðarstefnu á meðan samþykktarferlið er gert svo hægt að enginn leggur í raun til.
- **Yfirgefna útgáfan.** Að birta verkefni með opnunarbloggfærslu og flokka síðan aldrei villu, sem skaðar orðspor þitt meira en þögn myndi gera.
- **Greina-og-gleyma.** Að greina ósjálfstæði fyrir eina lagfæringu og bera hana síðan að eilífu, reka frá öryggisplástrum upprunaverkefnis.
- **Að nýta sér brothætta viðhaldsaðila.** Að vera háð mikilvægu eins-viðhaldsaðila safni og fjármagna, þakka eða hjálpa manneskjunni á bak við það aldrei.
- **Vörumerkjavanræksla.** Að gefa út verkefni án þess að vernda nafn þess og horfa síðan á grein eða seljanda versla með orðspor þitt.
- **Eignarhald aðeins lögfræðinnar.** Að hýsa OSPO alfarið í lögfræði svo leiðsögn hennar beri engan verkfræðitrúverðugleika og teymi slökkvi á sér.
- **Hégómamælikvarðar.** Að telja stjörnur og fjölmiðlaumfjöllun í stað ósjálfstæðisheilsu, tíma til samþykktar og lagðra niður einkaplástra.

## Þroskalíkan

- **Stig 1, Upphaf:** Verkfræðingar bæta við, plástra og stundum birta opinn hugbúnað án stefnu og án eiganda. Notkun, framlag og útgáfa er viðbragðsdrifin og ad hoc, knúin af frumkvæði einstaklinga. Einkagreinar safnast óséðar upp, enginn fjármagnar nokkurt upprunaverkefni og enginn gæti svarað leyfisspurningu í áreiðanleikakönnun.
- **Stig 2, Þróun:** Grunnvenjur birtast en eru ólíkar eftir teymum. Gróf notkunarstefna og samþykktur leyfislisti eru til og einhver er lauslega ábyrgur, en framlag er hægt og mál fyrir mál og sumir hópar gera langtum meira en aðrir. Fáein mikilvæg ósjálfstæði eru þekkt, en sjálfbærni, útgáfur og ráðsmennska eru ósamræmd.
- **Stig 3, Stöðlun:** Skipuð OSPO á notkun, framlag, útgáfu og samfélag og venjurnar eru skjalfestar og framfylgt um skipulagsheildina. Skönnun og hugbúnaðarefnisskrá eru sjálfvirk, fyrirfram samþykktur framlagssamningur og hröð samþykktarleið eru til, útgefin verkefni bera raunverulega stjórnarhætti, vörumerki og öryggisstefnur og InnerSource er að breiðast út. Teymi hins opinbera birta sjálfgefið.
- **Stig 4, Stjórnun:** Opna hugbúnaðarhlutverkið er mælt og stýrt gegn grunnlínum. Tími til samþykktar er rakinn gegn markmiði, framlagsmagn og samþykkishlutfall upprunaverkefna er skýrt, ósjálfstæðisheilsu- og viðhaldsaðilafjöldamælaborð flagga stökum bilunarpunktum, fjármögnuð viðhaldsaðilaþekja áhættumestu ósjálfstæðanna er vöktuð og skrá yfir einkaplástra og greinar fer niður ársfjórðung eftir ársfjórðung. Útgefin verkefni hafa mældan viðbragðstíma við villum, undantekningar eru rýndar á takti og hégómamælikvarðar eins og stjörnur eru lagðir til hliðar í þágu þessara.
- **Stig 5, Samhæfing:** Opinn hugbúnaður er stýrð stefnumótandi geta, samþætt verkfræði-, lögfræði-, öryggis- og innkaupaáætlanagerð og aðlöguð samfellt. Framlag er rútína, mikilvægir viðhaldsaðilar og stofnanir eru fjármagnaðar, skipulagsheildin hefur ráðsmennsku yfir vel reknum verkefnum og stýrir vistkerfunum sem hún er háð og InnerSource er normið. Þátttöku- og heilsumælikvarðar nærast inn í stöðugar umbætur og safnið er endurjafnað þegar ósjálfstæði, áhættur og umboð breytast.

## Hugmyndir til umræðu

1. Hvar er línan milli OSPO sem gerir kleift og einnar sem hliðar og hvernig mynduð þið vita utan frá hvora þið hafið byggt?
2. Hverja einkaplástra eða greina ykkar berið þið af vana frekar en nauðsyn og hvað þyrfti til að senda upp efstu þrjá?
3. Hvernig ættuð þið að ákveða hvaða viðhaldsaðila og stofnanir á að fjármagna þegar listi mikilvægra ósjálfstæða er lengri en fjárhagsáætlunin?
4. Hvað myndi í raun breytast í næstu útgáfu ykkar ef þið þyrftuð að birta hana með raunverulegum stjórnarháttum, vörumerki og samræmdri birtingarstefnu frá fyrsta degi?
5. Fyrir lesendur í opinbera geiranum, hvað er verjanlegt ferli til að undanskilja kóða birtingu-sjálfgefið án þess að grafa hljóðlega undan meginreglunni?
6. Hver innri safna ykkar myndu hagnast mest á InnerSource og hvað kemur í veg fyrir að annað teymi sendi ykkur beiðni um sameiningu í dag?

## Helstu atriði

- OSPO á allt samband við opinn hugbúnað: að nota á ábyrgan hátt, leggja til upprunaverkefna, gefa út eigin verkefni og viðhalda viðhaldsaðilunum sem þú ert háð(ur).
- Framlag til upprunaverkefna er stefna, ekki góðgerðir. Það eyðir endurteknum skatti einkaplástra, kaupir áhrif á stefnu og hjálpar þér að ráða.
- Gerðu samræmisleiðina að fljótustu leiðinni með sjálfvirkni og sérvali, svo skrifstofan geri verkfræðingum kleift frekar en að hliða þá.
- Gefðu út eigin verkefni aðeins með raunverulegum stjórnarháttum, völdu leyfi, vernduðu vörumerki og samræmdri öryggisbirtingu, eða gefðu þau alls ekki út.
- Fjármagnaðu og hjálpaðu mikilvægu viðhaldsaðilunum sem framleiðslukerfi þitt hvílir á, því sameiginlegt er ekki sjálfbært af sjálfu sér.
- Beittu InnerSource til að koma opnu hugbúnaðarsamstarfi inn í fyrirtækið og hjá hinu opinbera, hafðu opið sjálfgefið, birtu sjálfgefið og endurnýttu áður en þú smíðar.

## Heimildir og frekari lestur

- Nadia Eghbal, *Working in Public: The Making and Maintenance of Open Source Software*
- Nadia Eghbal, *Roads and Bridges: The Unseen Labour Behind Our Digital Infrastructure*
- Karl Fogel, *Producing Open Source Software: How to Run a Successful Free Software Project*
- Danese Cooper and Klaas-Jan Stol (editors), *Adopting InnerSource: Principles and Case Studies*
- The Linux Foundation and TODO Group, *OSPO guides and Open Source Program Office resources*
- The Linux Foundation and TODO Group, *State of OSPOs and Open Source Management* (annual survey series)
- Heather Meeker, *Open (Source) for Business*
- Open Source Initiative, *The Open Source Definition* and approved-licence list
- Free Software Foundation Europe, *Public Money, Public Code* campaign materials
- U.S. Federal Source Code Policy and Code.gov guidance
