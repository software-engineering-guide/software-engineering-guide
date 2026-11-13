# 5.6 Uhandisi wa frontend

## Muhtasari na msukumo

Uhandisi wa frontend ni nidhamu ya kujenga safu ya programu inayomkabili mteja: msimbo unaoendesha kwenye kivinjari au kifaa na kugeuza usanifu, maudhui, na data kuwa kiolesura kinachofanya kazi. Unaenea kuvuka chaguo za mfumo na usanifu, mkakati wa uonyeshaji, usimamizi wa hali, utendaji, na ustahimilivu kuvuka utofauti mkubwa wa vivinjari, vifaa, na hali za mtandao katika ulimwengu halisi. Frontend ndipo kazi yote ya juu ya mkondo (UX, usanifu, maudhui, ufikivu, uandaaji wa kimataifa) inapomfikia mtumiaji kwa mafanikio au kuporomoka.

Kwa timu kubwa, frontend ni changamoto ya kipekee, kwa sababu inakabiliwa na mazingira ambayo shirika halidhibiti. Vivinjari vya watumiaji, vifaa, miunganisho, na mipangilio hutofautiana kwa kiasi kikubwa, na jukwaa (wavuti) hubadilika mfululizo. Kwa ukubwa, chaguo za usanifu hujilimbikiza. Mfumo uliochaguliwa leo unabana uajiri, utendaji, na utunzikaji kwa miaka, na maelfu ya maamuzi madogo kuhusu ukubwa wa kifurushi na uonyeshaji hujumlishwa kuwa uzoefu ambao watumiaji wanaupata kweli. Viwango vya pamoja, maktaba za vijenzi, bajeti za utendaji, na mifumo ya usanifu ndivyo vinavyozuia timu nyingi huru zisizalishe kizima chenye polepole, kisicho thabiti, dhaifu.

Umuhimu wa mashirika makubwa na serikali ni mkali. Mashirika hudumisha programu za muda mrefu ambapo maisha marefu ya mfumo na utunzikaji vinajalisha zaidi ya uvumbuzi, na ambapo timu nyingi lazima ziingiliane. Serikali zinahudumia umma mzima, ikijumuisha watu wenye vifaa vya zamani, miunganisho ya polepole au yenye kikomo cha data, na teknolojia saidizi. Hilo hufanya utendaji, [uboreshaji wa hatua kwa hatua](https://en.wikipedia.org/wiki/Progressive_enhancement), na ustahimilivu kuwa si ung'arishaji wa hiari bali tofauti kati ya huduma inayofanya kazi kwa kila mtu na ile inayowatenga wasiojiweza zaidi. Huduma ya serikali inayofanya kazi tu kwenye simu ya hivi karibuni na muunganisho wa haraka inashindwa agizo lake.

## Kanuni kuu

- Frontend inaendesha katika mazingira usiyoyadhibiti; sanifu kwa utofauti na kushindwa.
- Chagua teknolojia ya kuchosha, ya kudumu kwa mifumo ya muda mrefu; boresha kwa utunzikaji na uajiri.
- Utendaji ni kipengele na, kwa watumiaji wengi, sharti la ufikiaji.
- Uboreshaji wa hatua kwa hatua: toa uzoefu wa msingi unaofanya kazi kwanza, kisha ongeza maboresho kwa tabaka.
- Tuma msimbo mdogo; msimbo wa haraka na wa kutegemewa zaidi ni ule usiousafirisha.
- Linganisha mkakati wa uonyeshaji na aina ya maudhui na hitaji la mtumiaji, si mitindo.
- Ustahimilivu: kiolesura kinapaswa kushuka taratibu, si kuvunjika, mambo yanapoenda vibaya.
- Viwango na vipengele vya jukwaa hudumu kuliko mifumo; egemea jukwaa.

## Mapendekezo

### Chagua mifumo kwa maisha marefu na ufaao, si ushabiki

Chagua teknolojia ya frontend kulingana na tatizo, timu, upeo wa matengenezo, na soko la uajiri, si kinachovuma. Kwa mifumo ya mashirika makubwa na serikali ya muda mrefu, pendelea teknolojia iliyokomaa, yenye msaada mzuri, yenye vikundi vikubwa vya vipaji, mazoea thabiti ya matoleo, na njia wazi za kuboresha. Pima jumla ya gharama ya mabadiliko ya mifumo: kuandika upya ni ghali na hatari. Pendelea mbinu zinazoegemea [viwango vya wavuti](https://en.wikipedia.org/wiki/Web_standards) ili uwekezaji wako uokoke mauzo ya mifumo, na utenge msimbo mahususi wa mfumo nyuma ya mipaka ili programu isiwe mateka wa mzunguko wa maisha wa maktaba moja.

### Linganisha mkakati wa uonyeshaji na hitaji

Mikakati mikuu ya uonyeshaji kila mmoja unafaa maudhui tofauti. Uonyeshaji wa upande wa seva (SSR) huzalisha uchoraji wa kwanza wa haraka na SEO nzuri ([uboreshaji wa injini za utafutaji](https://en.wikipedia.org/wiki/Search_engine_optimization)) na hufanya kazi bila JavaScript ya mteja, ukifaa kurasa nzito za maudhui na zinazomkabili umma. [Uzalishaji wa tovuti tuli](https://en.wikipedia.org/wiki/Static_site_generator) (SSG) huonyesha mapema wakati wa ujenzi kwa kasi ya juu zaidi na uwezo wa kuhifadhi kwenye kache, unaofaa maudhui yanayobadilika mara chache. Uonyeshaji wa upande wa mteja (CSR) unafaa uzoefu mwingiliano sana wa mtindo wa programu nyuma ya uthibitishaji. Utiririshaji na unyunyizaji wa hatua kwa hatua hutuma na kuamsha ukurasa kidogo kidogo ili watumiaji waone na kutumia maudhui mapema. Mifumo mingi mikubwa huchanganya hizi kwa kila njia badala ya kuchagua moja kimataifa. Simamia hali kwa makusudi: weka hali ya seva, hali ya URL, na hali ya UI ya ndani tofauti, na uepuke kuweka kila kitu katikati kwenye hifadhi moja nzito ya kimataifa.

### Chukulia utendaji kama nidhamu iliyopangiwa bajeti, inayopimwa

Pokea bajeti za utendaji (mipaka wazi ya ukubwa wa kifurushi, idadi ya maombi, na vipimo muhimu) na uzitekeleze kwenye CI ili regression zishindwe ujenzi. Fuatilia Core Web Vitals (upakiaji, mwingiliano, na utulivu wa kuona) kwa ufuatiliaji wa watumiaji halisi kutoka vifaa na mitandao halisi, si majaribio ya maabara kwenye mashine za haraka tu. Punguza JavaScript kwa ukali: gawanya msimbo na [pakia kwa uvivu](https://en.wikipedia.org/wiki/Lazy_loading) ili watumiaji wapakue tu kile mwonekano fulani unachohitaji, ahirisha kazi isiyo muhimu, na upendelee uwezo wa jukwaa kuliko maktaba nzito. Boresha picha na fonti, tumia kache ipasavyo, na upime kwenye vifaa vya kiwango cha chini vya uwakilishi na miunganisho ya polepole.

### Jenga kwa uboreshaji wa hatua kwa hatua na ustahimilivu

Anza kutoka msingi unaofanya kazi na HTML ya kisemantiki na JavaScript kidogo au bila kabisa, kisha boresha kwa wateja wenye uwezo. Hii inahakikisha kazi ya msingi inabaki inawezekana hati zinaposhindwa kupakia, kifaa kinapokuwa cha zamani, au mtandao unapokuwa na hitilafu, uhalisia wa kawaida badala ya hali ya pembeni. Shughulikia makosa kwa neema: onyesha hali zenye manufaa kwa upakiaji, tupu, kosa, na nje ya mtandao badala ya skrini tupu au vizungushio visivyo na mwisho. Kwa huduma ambazo watu wanazitegemea, fikiria mbinu za nje-ya-mtandao-kwanza ili programu ibaki ikitumika kupitia muunganisho wa mara kwa mara, ikisawazisha muunganisho unaporudi.

### Hakikisha upatanifu wa vivinjari, vifaa, na teknolojia saidizi

Jaribu kuvuka vivinjari, vifaa, na teknolojia saidizi ambazo watumiaji wako wanazo kweli, ukiongozwa na uchanganuzi halisi badala ya mashine za timu yenyewe. Tumia uboreshaji wa hatua kwa hatua na ugunduzi wa vipengele badala ya kudhania vipengele vipya zaidi vya jukwaa vinapatikana kila mahali. Jenga kwa [uitikiaji](https://en.wikipedia.org/wiki/Responsive_web_design) (angalia sura ya mfumo wa usanifu) ili msingi mmoja wa msimbo uhudumie simu hadi kompyuta za mezani. Unganisha ufikivu na uandaaji wa kimataifa kwenye usanifu wa frontend tangu mwanzo, si kama duru za baadaye.

### Tawala frontend kama miundombinu ya pamoja

Toa maktaba za vijenzi za pamoja, lint, uumbaji, na zana za ujenzi ili timu ziwe thabiti na zenye tija. Anzisha miongozo ya usanifu (jinsi ya kupanga programu, kusimamia hali, na kugawanya vifurushi) na bajeti za utendaji zinazotekelezwa kwenye CI. Kwa frontend kubwa sana, fikiria usanifu wa moduli au micro-frontend unaoruhusu timu kusambaza kwa uhuru, lakini pima ugumu ulioongezwa na gharama ya utendaji kwa uangalifu, kwa kuwa si bure.

## Mabadilishano: faida na hasara

| Uamuzi | Faida | Hasara |
|---|---|---|
| Mfumo maarufu uliokomaa | Kundi kubwa la vipaji, thabiti, unaoungwa mkono | Unaweza kubeba uzito wa urithi; polepole kupokea vipengele vipya |
| Mfumo mpya zaidi | Vipengele vya kisasa, faida za utendaji | Hatari ya mabadiliko, kundi dogo la vipaji, maisha marefu yasiyo na uhakika |
| SSR / SSG | Uchoraji wa kwanza wa haraka, SEO, hufanya kazi bila JS | Ugumu wa seva au ujenzi, changamoto za kache |
| CSR (SPA) | Mwingiliano tajiri, hisia ya programu | Upakiaji wa kwanza polepole, unategemea JS, gharama ya SEO na ustahimilivu |
| JavaScript nzito ya mteja | Vipengele tajiri | Utendaji duni kwenye vifaa vya kiwango cha chini, dhaifu |
| Uboreshaji wa hatua kwa hatua | Ustahimilivu, ujumuishaji, hufanya kazi kila mahali | Juhudi zaidi ya usanifu kufafanua msingi unaofanya kazi |
| Micro-frontends | Usambazaji huru wa timu, ukubwa | Ugumu, utegemezi uliorudiwa, mzigo wa utendaji |

Mabadilishano yanayojirudia ni utajiri na urahisi wa msanidi dhidi ya ufikiaji, utendaji, na ustahimilivu. Mbinu nzito za upande wa mteja ni za kupendeza kujenga na kuonyesha kwenye mashine za haraka, lakini zinawatenga watumiaji wenye vifaa na mitandao dhaifu. Kwa hadhira za mashirika makubwa na hasa za serikali, elekeza mizani kuelekea utendaji, uboreshaji wa hatua kwa hatua, na uimara, kwa sababu gharama ya kuwatenga watumiaji ni kubwa na mara nyingi haijadiliki.

## Maswali ya kujadili na timu yako

1. **Tunatengaje msimbo mahususi wa mfumo ili programu isiwe mateka wa mzunguko wa maisha wa maktaba moja?** Kwa mifumo ya mashirika makubwa na serikali ya muda mrefu, mabadiliko ya mifumo ndiyo gharama kubwa zaidi inayoweza kuepukika: kuandika upya ni ghali na hatari, na maktaba inayovuma leo inabana uajiri na matengenezo kwa miaka. Kuegemea viwango vya wavuti na kuweka msimbo mahususi wa mfumo nyuma ya mipaka wazi kunamaanisha mantiki yenu ya biashara na maudhui yenu yanaokoka mauzo ya mfumo yanayofuata. Amua mishono hiyo iko wapi na kama mhandisi mpya angeweza kutofautisha msimbo wa jukwaa na wa mfumo. Leta makadirio ya uhamishaji wenu wa mwisho wa mfumo uligharimu kiasi gani, au unaokaribia utagharimu. Mantiki yenu ya msingi ikiwa imeunganishwa kwa API za maktaba moja, pima kuunganishwa huko kabla ya kutetea chaguo la mfumo.

2. **Tunalinganisha mkakati wa uonyeshaji kwa kila njia, au tunalazimisha mkakati mmoja kwa bidhaa nzima?** Uonyeshaji wa upande wa seva hutoa uchoraji wa kwanza wa haraka na hufanya kazi bila JavaScript ya mteja kwa maudhui ya umma, uzalishaji tuli huongeza kasi kwa kurasa zinazobadilika mara chache, na uonyeshaji wa mteja unafaa nyuso mwingiliano za mtindo wa programu nyuma ya kuingia. Kulazimisha mmoja kimataifa ama kunapunguza kasi ya kurasa za umma na JavaScript nzito au kunazidisha ugumu wa ukurasa rahisi wa maudhui. Hili ni swali la ufikiaji kwa serikali, ambapo huduma inayofanya kazi tu baada ya kifurushi kikubwa kupakia inawatenga watumiaji wenye vifaa vya zamani na miunganisho ya polepole. Leta njia zenu kuu na uweke lebo kwa kila moja mkakati inaoutumia leo. Ukurasa unaomkabili umma ukihitaji JavaScript kuonyesha maudhui yake, amua kama huo ni uchaguzi wa makusudi au ajali.

3. **Usimamizi wetu wa hali una nidhamu kiasi gani, na je, tunaweka kila kitu katikati kwenye hifadhi moja nzito ya kimataifa?** Kuweka hali ya seva, hali ya URL, na hali ya UI ya ndani tofauti kunazuia kuunganishwa na dhoruba za kuonyesha upya zinazofanya frontend kubwa kuwa polepole na dhaifu, hata hivyo chaguo-msingi linalovutia ni kutupa kila kitu kwenye hifadhi moja ya kimataifa. Hili linajilimbikiza kwa ukubwa, ambapo timu nyingi zinazogusa hifadhi moja ya pamoja huunda utegemezi uliofichika na utendaji usioweza kutabirika. Kubaliana mahali kila aina ya hali inapostahili na kisichostahili kuwa kwenye hifadhi ya kimataifa. Leta kijenzi kinachoonyeshwa upya zaidi ya kinavyostahili na ufuatilie kwa nini. Jibu likiwa hifadhi ya kati iliyovimba, amua mipaka kabla kuunganishwa hakujaimarika.

4. **Bajeti zetu za utendaji ni zipi, je, zinashindwa ujenzi kwenye CI, na zinapimwa kwenye vifaa ambavyo watumiaji wetu wanavyo kweli?** Bajeti ambayo hakuna anayeitekeleza ni tamanio, na bajeti inayopimwa kwenye kompyuta za haraka za timu tu inaelezea mtumiaji asiyekuwepo. Kwa shirika kubwa, bajeti ndio utaratibu pekee unaoshikilia ukubwa wa kifurushi na Core Web Vitals chini ya udhibiti timu kadhaa zinapoongeza vipengele kwenye uso wa pamoja, kwa sababu hakuna mpitiaji mmoja anayeweza kunasa kila regression kwa macho. Shinikizo linaloshindana ni kasi ya utoaji: kushindwa kwa ujenzi kwa sababu ya kilobaiti chache kunaonekana kuzuia hadi upime kuachwa kunakozuia. Leta bajeti zenu za sasa, data ya ufuatiliaji wa watumiaji halisi kutoka vifaa vya kiwango cha chini na miunganisho ya polepole, na orodha ya matoleo ambapo regression ilipenya. Katika serikali, ambapo agizo ni kuhudumia umma mzima ikijumuisha watu wenye simu za zamani na data yenye kikomo, funga bajeti na sehemu ya kumi ya polepole zaidi ya watumiaji wenu badala ya wastani, na ufanye lango la CI lisilojadilika.

5. **Huduma zetu zipi lazima ziendelee kufanya kazi bila JavaScript ya mteja, na je, tumejaribu njia hiyo kweli?** Uboreshaji wa hatua kwa hatua ni rahisi kudai na rahisi kuuvunja kimyakimya, kwa sababu njia iliyoboreshwa ndiyo wasanidi wanaitumia kila siku huku msingi ukioza bila kujaribiwa. Kuamua hili kwa makusudi ni muhimu kwa ukubwa, kwa kuwa timu nyingi zinazosafirisha kwenye jukwaa moja kila moja itadhania hati daima hupakia isipokuwa kiwango cha pamoja kinasema vinginevyo, na utegemezi mgumu mmoja unaweza kuvunja kazi ya msingi kwa yeyote ambaye kifurushi chake kinashindwa. Mabadilishano ni halisi: msingi unaofanya kazi bila JavaScript unagharimu juhudi ya usanifu na unabana jinsi unavyojenga mwingiliano. Leta safari zenu muhimu za mtumiaji, jaribio linalopakia kila moja na hati zimezimwa au zimeshindwa, na ushahidi wa mara ngapi hati zinashindwa kupakia kweli uwandani. Kwa huduma ya umma, fomu ya manufaa au ya kodi inayoporomoka hati moja inapoisha muda si uzoefu uliopungua, ni raia asiyeweza kukamilisha wajibu wa kisheria, kwa hiyo chukulia msingi kama sharti la uzingatiaji, si pambo.

6. **Micro-frontends zinalipia ugumu wao kweli lini, na nani anaamua kabla timu haijazifikia?** Usambazaji huru wa timu unavutia, lakini micro-frontends hubeba ugumu wa mfumo uliosambazwa, utegemezi uliorudiwa, na kodi ya utendaji ambayo watumiaji huilipa katika upakiaji polepole zaidi. Bila kituo cha pamoja cha uamuzi, timu zenye tamaa huzipokea kwa urahisi wa kishirika muda mrefu kabla ukubwa haujahalalisha gharama, na bidhaa nzima inarithi mzigo. Mazingatio yanayoshindana ni uhuru: timu zinazosafirisha kwenye msingi mmoja wa pamoja wa msimbo zinaweza kuzuiana, na kwa ukubwa halisi kuunganishwa huko ni tatizo ghali lenyewe. Leta idadi ya timu zinazogusa uso, mgongano wa usambazaji mnaoupata kweli leo, na makadirio yaliyopimwa ya marudio ya mzigo ambayo mgawanyo ungeleta. Kwa majukwaa ya mashirika makubwa na serikali, ambapo maamuzi ya usanifu yanafunga timu nyingi kwa miaka na lazima yaokoke ukaguzi na makabidhiano, hitaji kizingiti kilichoandikwa wazi na mmiliki anayeidhinisha hatua, badala ya kuacha kila timu iamue peke yake.

## Mtazamo wa sekta

**Kampuni changa.** Kasi na ufikiaji vyote vinajalisha kila usajili ukihesabiwa, kwa hiyo pinga programu nzito ya ukurasa mmoja kwa kurasa za umma. Onyesha upande wa seva ukurasa wako wa uuzaji na mtiririko wa kujisajili ili zipakie haraka kwenye simu za kiwango cha kati na data yenye hitilafu ambayo wateja wako wa mapema wanatumia, na uhifadhi mwingiliano wa upande wa mteja kwa programu nyuma ya kuingia. Weka bajeti moja rahisi ya ukubwa wa kifurushi kwenye CI ili utegemezi wa uzembe usivimbe ukurasa kimyakimya, na uegemee viwango vya wavuti kuweka msingi mdogo wa msimbo ukidumishika unapoajiri.

**Biashara ndogo.** Bila mtaalamu maalumu wa frontend na bajeti finyu, pendelea mfumo wa kawaida unaoungwa mkono vizuri au kijenzi cha tovuti kinachopangishwa kuliko kitu chochote cha kipekee, ili uajiri kutoka kundi kubwa la vipaji na kununua matengenezo badala ya kuajiri. Weka uchaguzi kama uimara: chaguo la bei nafuu zaidi ni lile usilolazimishwa kuliandika upya ndani ya miaka miwili. Dai kurasa za haraka, zinazofaa simu, na alama zinazofikika kutoka mwanzo, kwa kuwa malipo ya polepole au yaliyovunjika yanakugharimu wateja ambao huwezi kumudu kuwapoteza.

**Biashara kubwa.** Tatizo ni uthabiti kuvuka timu nyingi: maktaba ya pamoja ya vijenzi, mifumo ya usanifu iliyokubaliwa, lint na zana za ujenzi, na bajeti za utendaji zinazotekelezwa kwenye CI ili hakuna timu inayoweza kurudisha kizima nyuma kimyakimya. Chagua mifumo kwa maisha marefu na uajiri badala ya uvumbuzi, tenga msimbo mahususi wa mfumo nyuma ya mipaka ili kuokoka uhamishaji unaofuata, na ulinganishe mkakati wa uonyeshaji kwa kila uso. Simamia frontend kama miundombinu ya pamoja yenye ufuatiliaji wa watumiaji halisi, utawala, na rekodi inayokaguliwa ya kwa nini kila chaguo la usanifu lilifanywa.

**Serikali.** Unahudumia umma mzima, ikijumuisha watu wenye vifaa vya zamani, miunganisho ya polepole au yenye kikomo cha data, na teknolojia saidizi, kwa hiyo uboreshaji wa hatua kwa hatua na utendaji ni wajibu, si ung'arishaji. Fanya msingi unaofanya kazi bila JavaScript kuwa kanuni ngumu kwa huduma zinazomkabili raia, panga bajeti za kurasa kwa watumiaji wa polepole zaidi badala ya wastani, na uweke kazi ya msingi ikikamilika hati inaposhindwa. Ununuzi na uwazi vinatumika: pendelea teknolojia ya kudumu, inayoegemea viwango inayoepuka kufungwa kwa muuzaji mmoja, andika mahitaji ya ufikivu na utendaji kwenye mikataba, na uweze kuonyesha kwamba huduma inafanya kazi kwa mtumiaji asiyejiweza zaidi, si kifaa cha onyesho tu.

## Mifano

**Kampuni changa.** Kampuni changa ya hatua ya mbegu ilishawishika kujenga tovuti yake ya uuzaji na mtiririko wa kujisajili kama programu nzito ya ukurasa mmoja, lakini wateja wao walengwa walikuwa wanunuzi mara nyingi kwenye simu za kiwango cha kati kupitia data ya simu yenye hitilafu. Waanzilishi wawili badala yake walionyesha upande wa seva kurasa za umma ili zipakie haraka na kufanya kazi kabla JavaScript yoyote haijaendesha, na kuhifadhi mwingiliano wa upande wa mteja kwa programu nyuma ya kuingia. Waliweka bajeti rahisi ya ukubwa wa kifurushi kwenye CI ili utegemezi wa uzembe usivimbe ukurasa kimyakimya. Upakiaji wa kwanza wa haraka, mwembamba uliboresha usajili kwa kupimika, na kuegemea viwango vya wavuti kuliweka msingi wao mdogo wa msimbo ukidumishika waliposhiriki kuajiri.

**Biashara kubwa.** Kampuni ya huduma za kifedha iliboresha seti pana ya programu za ndani na za wateja kwa kusawazisha kwenye mfumo ulio komaa, maktaba ya pamoja ya vijenzi, na bajeti za utendaji zinazotekelezwa kwenye CI. Mkakati wa uonyeshaji ulichaguliwa kwa kila uso: kurasa zilizoonyeshwa upande wa seva, zinazoweza kuhifadhiwa kwenye kache kwa uuzaji wa umma na maudhui, na programu iliyoonyeshwa upande wa mteja nyuma ya kuingia kwa dashibodi mwingiliano. Bajeti za vifurushi na ufuatiliaji wa watumiaji halisi zilinasa regression kabla ya toleo, zikiweka nyakati za upakiaji kuwa za haraka kuvuka timu nyingi za kampuni na kupunguza hatari ya mabadiliko ya mfumo ambayo hapo awali ililazimisha kuandika upya kwa gharama.

**Serikali.** Timu ya huduma ya kidijitali ya taifa ilijenga huduma zinazomkabili raia kwa uboreshaji wa hatua kwa hatua kama kanuni ngumu: kila huduma inafanya kazi na HTML ya kisemantiki na uonyeshaji wa seva kwanza, na JavaScript inaboresha tu. Hii inahakikisha huduma inafanya kazi kwenye simu za zamani, miunganisho ya polepole ya vijijini, na teknolojia saidizi, makundi ambayo serikali haiwezi kuyatenga. Bajeti za utendaji huweka kurasa nyepesi na za haraka kwenye vifaa vya kiwango cha chini, na kushuka kwa neema kunamaanisha hati iliyoshindwa haizuii kamwe mtu kukamilisha ombi la manufaa. Matokeo ni huduma ya haraka, thabiti, inayofikika, na inayoweza kutumiwa na umma mzima.

## Kesi ya biashara: sababu, ROI, na TCO

Chaguo za uhandisi wa frontend huendesha mapato, ufikiaji, na gharama. Utendaji umefungwa moja kwa moja na ubadilishaji, ushirikishi, na ukamilishaji wa kazi. Uzoefu wa haraka unashinda wa polepole kwa kupimika, na kwa watumiaji wenye vifaa dhaifu, utendaji ni mstari kati ya kutumia huduma na kuiacha. Uboreshaji wa hatua kwa hatua na usaidizi wa vifaa vingi hupanua hadhira inayoweza kufikiwa, ambayo kwa serikali ni agizo na kwa mashirika ni sehemu ya soko. Chaguo sahihi za mfumo na usanifu hupunguza mara na gharama za kuandika upya, gharama kubwa zaidi inayoweza kuepukika katika uhandisi wa frontend.

Kwenye TCO, gharama za kupokea ni nidhamu ya bajeti za utendaji na majaribio, juhudi ya uboreshaji wa hatua kwa hatua, na uwekezaji katika zana za pamoja na maktaba za vijenzi. Gharama ya kutopokea inalipwa katika uzoefu wa polepole unaopoteza watumiaji na mapato, kuwatenga watumiaji wa kiwango cha chini na wa teknolojia saidizi (kwa mfiduo wa kisheria katika serikali), programu dhaifu zinazovunjika uwandani, na mabadiliko ya mifumo ya gharama na kuandika upya kunakoendeshwa na kufuata mitindo. Matatizo ya frontend hujitokeza kama kuacha kulikosambaa na mzigo wa msaada badala ya kipengele kimoja cha mstari, kwa hiyo ni rahisi kuwekeza kidogo.

Kuweka kesi kwa uongozi, unganisha Core Web Vitals na nyakati za upakiaji na funeli za ubadilishaji na ukamilishaji, pima kwa namba watumiaji wanaotengwa na mbinu nzito za upande wa mteja, na upime gharama ya kuandika upya zilizopita au zinazokaribia dhidi ya uthabiti wa usanifu wa kudumu unaoegemea viwango. Weka bajeti za utendaji na uboreshaji wa hatua kwa hatua kama kupunguza hatari na kupanua ufikiaji.

## Mifumo mibaya na mitego

- **Kufukuzia mifumo**: kuandika upya kwenye maktaba mpya zaidi, kuingia mabadiliko bila faida kwa mtumiaji.
- **Uzoefu wa JavaScript tu**: hakuna kinachofanya kazi hadi kifurushi kikubwa kipakie na kiendeshe, kikiwatenga watumiaji wengi.
- **Kujaribu kwenye vifaa vya haraka tu**: kompyuta bora za timu huficha uzoefu halisi wa mtumiaji.
- **Kupuuza ukubwa wa kifurushi**: ukuaji usio na mipaka wa utegemezi hadi kurasa ni polepole kila mahali.
- **Hakuna bajeti ya utendaji**: regression hujilimbikiza kimyakimya toleo kwa toleo.
- **Kushindwa kwa skrini tupu**: hakuna hali za upakiaji, tupu, kosa, au nje ya mtandao; ombi lililoshindwa linavunja ukurasa.
- **Hali ya kimataifa iliyowekwa katikati kupita kiasi**: kila kitu kwenye hifadhi moja, kuunda kuunganishwa na dhoruba za kuonyesha upya.
- **Micro-frontends za mapema**: ugumu wa mfumo uliosambazwa na mizigo iliyorudiwa bila ukubwa wa kuhalalisha.
- **Kupuuza ufikivu na i18n kwenye usanifu**: kuzibana baadaye kwa gharama kubwa.

## Kielelezo cha ukomavu

**Ngazi ya 1: Kuanzisha.** Frontend ya papo hapo iliyojengwa kwa kila timu bila viwango vya pamoja. Msimbo mzito wa upande wa mteja, hakuna bajeti za utendaji, unajaribiwa tu kwenye vifaa vya timu yenyewe. Chaguo za mfumo hufanywa kwa upendeleo au ushabiki, na hati iliyoshindwa inaweza kuwaacha watumiaji wakitazama skrini tupu.

**Ngazi ya 2: Kuendeleza.** Baadhi ya timu hupokea zana za pamoja na maktaba ya vijenzi, lakini mazoea hayana uthabiti kuvuka shirika. Utendaji unapimwa mara kwa mara badala ya kupangiwa bajeti au kutekelezwa. Mkakati wa uonyeshaji mara nyingi ni sare bila kujali aina ya maudhui, na majaribio ya vifaa vingi ni machache na ya mkono.

**Ngazi ya 3: Kusawazisha.** Mfumo na usanifu huchaguliwa kwa makusudi kwa maisha marefu, na chaguo hizo zimeandikwa na kutekelezwa shirika zima. Mkakati wa uonyeshaji unalinganishwa kwa kila uso, uboreshaji wa hatua kwa hatua na kushuka kwa neema ndivyo kiwango, na maktaba za pamoja za vijenzi, lint, na zana za ujenzi zinatumika kwa kila timu. Vivinjari vingi, ufikivu, na uandaaji wa kimataifa vimejengwa ndani badala ya kubanwa.

**Ngazi ya 4: Kusimamia.** Frontend inapimwa na kudhibitiwa kwa data. Bajeti za utendaji zinatekelezwa kwenye CI ili regression zishindwe ujenzi, na Core Web Vitals zinafuatiliwa kwa ufuatiliaji wa watumiaji halisi kutoka vifaa halisi vya kiwango cha chini na miunganisho ya polepole dhidi ya vipimo vya msingi vilivyo wazi. Ukubwa wa kifurushi, ufikiaji wa hali za kosa na nje ya mtandao, na sehemu ya watumiaji wanaohudumiwa kwenye miunganisho ya polepole zaidi vinaripotiwa na kupitiwa, kwa hiyo maamuzi yanategemea ushahidi badala ya maoni.

**Ngazi ya 5: Kuratibu.** Utendaji, ustahimilivu, na ufikiaji vinaboreshwa mfululizo na kufungwa na matokeo ya biashara kuvuka shirika zima. Frontend inaegemea viwango vya wavuti kwa uimara, inatenga utegemezi wa mfumo ili uhamishaji uwe wa bei nafuu, na inabadilisha usanifu kwa kujirekebisha vifaa, jukwaa, na data ya watumiaji halisi vinapohama. Umma mzima na vifaa vyote ni raia wa daraja la kwanza, na mazoea ya frontend yameunganishwa na usanifu, ufikivu, na upangaji wa bidhaa badala ya kuchukuliwa kama suala tofauti.

## Mawazo ya kujadili

- Mnaamuaje wakati uhamishaji wa mfumo unastahili gharama na hatari yake?
- Core Web Vitals na bajeti za vifurushi zipi zinapaswa kuwa vizingiti vigumu vinavyoshindwa ujenzi?
- Uboreshaji wa hatua kwa hatua ni muhimu wapi, na programu ya upande wa mteja inakubalika wapi?
- Mnaweka vipi usanifu wa frontend thabiti kuvuka timu nyingi huru?
- Micro-frontends zinalipia ugumu wao kweli lini?
- Majaribio ya vifaa halisi na mtandao wa polepole yanapaswa kujengwa vipi kwenye bomba?

## Mambo muhimu ya kukumbuka

- Frontend inaendesha katika mazingira usiyoyadhibiti: sanifu kwa utofauti na kushindwa.
- Chagua teknolojia ya kudumu, inayoungwa mkono vizuri kwa mifumo ya muda mrefu; egemea viwango vya wavuti.
- Linganisha mkakati wa uonyeshaji (SSR, SSG, CSR, utiririshaji) na maudhui na hitaji, mara nyingi ukichanganywa kwa kila njia.
- Chukulia utendaji kama nidhamu iliyopangiwa bajeti, inayopimwa, inayotekelezwa kwenye CI kwa data ya watumiaji halisi.
- Jenga kwa uboreshaji wa hatua kwa hatua ili uzoefu wa msingi ufanye kazi kila mahali.
- Safirisha JavaScript kidogo; gawanya msimbo, pakia kwa uvivu, na upendelee uwezo wa jukwaa.
- Kwa serikali hasa, utendaji na ustahimilivu ni masharti ya ufikiaji wa usawa.

## Marejeo na usomaji zaidi

- Jeremy Keith, *Resilient Web Design*
- Aaron Gustafson, *Adaptive Web Design* (progressive enhancement)
- Steve Souders, *High Performance Web Sites*
- Ilya Grigorik, *High Performance Browser Networking*
- Addy Osmani, writings on performance, code-splitting, and the cost of JavaScript
- Google, *Web Vitals* and web.dev performance guidance
- MDN Web Docs, web platform and progressive enhancement references
- Alex Russell, essays on the cost of JavaScript and device diversity
- UK Government Digital Service, progressive enhancement and frontend guidance
- WHATWG HTML Living Standard and W3C web platform specifications
