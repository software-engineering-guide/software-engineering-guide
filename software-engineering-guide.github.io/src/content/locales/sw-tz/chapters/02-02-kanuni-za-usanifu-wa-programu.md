# 2.2 Kanuni za usanifu wa programu

## Muhtasari na msukumo

Kanuni za usanifu wa programu ni kanuni za kidole gumba za kupanga msimbo ili uweze kuuelewa, kuubadilisha, na kuupanua kwa muda. Zinajumuisha vifupisho vilivyotajwa ([SOLID](https://en.wikipedia.org/wiki/SOLID) kwa kanuni tano za usanifu wa [kuelekezwa kwa vitu](https://en.wikipedia.org/wiki/Object-oriented_programming), [DRY](https://en.wikipedia.org/wiki/Don%27t_repeat_yourself) kwa usirudie-mwenyewe, [KISS](https://en.wikipedia.org/wiki/KISS_principle) kwa weka-rahisi, [YAGNI](https://en.wikipedia.org/wiki/You_aren%27t_gonna_need_it) kwa hutahitaji-hivyo), dhana za kimuundo ([uunganishaji](https://en.wikipedia.org/wiki/Coupling_(computer_programming)), [mshikamano](https://en.wikipedia.org/wiki/Cohesion_(computer_science)), [kutenganisha wasiwasi](https://en.wikipedia.org/wiki/Separation_of_concerns)), [mifumo ya usanifu](https://en.wikipedia.org/wiki/Software_design_pattern) iliyoorodheshwa, mbinu za ngazi ya juu za kuunda mifano kama [Domain-Driven Design](https://en.wikipedia.org/wiki/Domain-driven_design) (kuunda programu kwa lugha ya eneo la biashara), na uchaguzi kati ya mitindo ya kuelekezwa kwa vitu, [ya kiutendaji](https://en.wikipedia.org/wiki/Functional_programming), na [inayoelekezwa kwa data](https://en.wikipedia.org/wiki/Data-oriented_design). Hakuna kati ya hizi ni sheria. Ni uzoefu uliobanwa, na lazima uzitumie kwa busara.

Kwa timu kubwa, thamani ya kanuni za pamoja ni uratibu. Mamia ya wahandisi wanapofanya kazi kwenye mfumo mmoja, wanahitaji msamiati wa pamoja kwa mijadala ya usanifu na seti ya pamoja ya chaguo-msingi ili moduli zilizoandikwa kwa kujitegemea zilingane. Usanifu mzuri ndio unaowaruhusu watu wengi kubadilisha mfumo sambamba bila migongano ya mara kwa mara. Pia ndio unaoweka mfumo ubadilike muongo baadaye, maisha ya kawaida ya mifumo ya mashirika makubwa na ya serikali, muda mrefu baada ya kipindi cha waandishi wake wa awali.

Ujuzi muhimu si kukariri kanuni. Ni kujua lini kila moja inakupotosha. Kila kanuni ina njia ya kushindwa: DRY inaweza kuzalisha dhana isiyo sahihi, SOLID inaweza kuzalisha uelekezaji usio wa lazima, YAGNI inaweza kunyima upanuzi ambao unauhitaji kweli. Sura hii inachukulia kanuni kama zana zenye eneo la matumizi, na inasisitiza uunganishaji na mshikamano kama sifa za kina ambazo vifupisho vinajaribu kuzihudumia.

## Kanuni kuu

- Simamia uunganishaji na mshikamano kwanza; kanuni nyingi zilizotajwa ni njia zisizo za moja kwa moja za kuboresha sifa hizi mbili.
- Boresha kwa mabadiliko: usanifu mzuri hupunguza gharama ya mabadiliko utakayohitaji kufanya kweli.
- Pendelea usanifu rahisi zaidi unaofanya kazi sasa, lakini weka mipaka pale mabadiliko yanapowezekana.
- Kurudiwa ni nafuu kuliko dhana isiyo sahihi; subiri hadi mfumo uwe wazi.
- Fanya utegemezi uwe wazi na uuelekeze kwenye vitu thabiti.
- Unda mfano wa eneo kwa lugha ya eneo; panga mipaka ya programu na mipaka ya biashara.
- Chagua mifumo ya uandishi kufaa tatizo, si itikadi; mifumo mikubwa mingi imechanganywa kwa vitendo.

## Mapendekezo

### Tumia SOLID kama lenzi, si orodha hakiki

Tumia uwajibikaji-mmoja kuweka moduli zenye mshikamano, ugeuzaji-wa-utegemezi kuelekeza utegemezi kwenye dhana pale mpaka upo kweli, na wazi-na-kufungwa pale pointi za upanuzi ni halisi. Usitengeneze violesura, viwanda, na tabaka tu ili kutimiza kifupisho wakati kuna utekelezaji mmoja tu na hakuna wa pili unaoonekana. Uelekezaji una gharama, na unailipa kwa kila usomaji.

### Tumia DRY kwa maarifa, si kwa maandishi

DRY inahusu kutorudia kipande kimoja chenye mamlaka cha *maarifa*. Haihusu kuondoa mistari inayofanana tu kwa mwonekano. Vipande viwili vya msimbo vinavyoonekana sawa lakini vinabadilika kwa sababu tofauti vinapaswa kubaki tofauti. Pendelea kurudiwa kidogo kuliko dhana ya pamoja ya mapema inayounganisha vitu visivyohusiana. Toa dhana mara mfumo halisi unapoonekana mara mbili au tatu.

### Acha KISS na YAGNI zipinge kubahatisha

Jenga kwa mahitaji uliyo nayo, si yale unayoyafikiria. Epuka ujumla wa kubahatisha, kama mifumo inayosanidika, mifumo ya viongezeo, na pointi za upanuzi ambazo hakuna aliyeziomba. Kinyume chake ni kwamba unyumbufu fulani ni nafuu kweli kuujenga mapema, kama kiolesura thabiti au mshono safi. YAGNI inapinga *utekelezaji* wa kubahatisha, si mipaka iliyofikiriwa vizuri.

### Buni kwa uunganishaji mdogo na mshikamano wa juu waziwazi

Fanya kila moduli ifanye kitu kimoja kilichofafanuliwa vyema (mshikamano), na itegemee moduli chache iwezekanavyo, kupitia violesura nyembamba (uunganishaji mdogo). Unapopitia usanifu, uliza mabadiliko yapi yanavuka mipaka ya moduli. Mavuko hayo ndiyo kipimo halisi cha uunganishaji. Kutenganisha wasiwasi ni wazo lilelile linalotumika kwa tabaka na wasiwasi unaovuka maeneo.

### Tumia mifumo ya usanifu kama msamiati, tumia mifumo mibaya kama maonyo

Mifumo ni majina ya pamoja yenye manufaa kwa suluhisho zinazojirudia. Ifikie wakati tatizo linalingana nayo kweli. Usilazimishe mifumo ili uonekane mjuzi, kwa sababu msimbo uliojaa mifumo mara nyingi ni ishara ya kuhandisi kupita kiasi. Jifunze [mifumo mibaya](https://en.wikipedia.org/wiki/Anti-pattern) ya kawaida (vitu vya mungu, mifano isiyo na tabia pale isipofaa, mipira mikubwa ya matope, monolith zilizosambazwa) kama lebo za uchunguzi.

### Pokea Domain-Driven Design pale eneo ni tata

Kwa mifumo yenye kanuni nyingi za biashara, tumia zana za kimbinu na za kimkakati za DDD: lugha ya kila mahali inayoshirikiwa na wataalamu wa eneo, miktadha iliyopakana inayogawa mfumo katika vipande vilivyoundwa kwa kujitegemea, na ramani za miktadha zinazoeleza jinsi vipande hivyo vinavyohusiana. Miktadha iliyopakana ni yenye thamani hasa kwa ukubwa wa mashirika makubwa, kwa sababu inapanga umiliki wa timu na mipaka ya mfano. DDD ni ya kupindukia kwa mifumo rahisi ya [CRUD](https://en.wikipedia.org/wiki/Create,_read,_update_and_delete) (unda, soma, sasisha, futa).

### Chagua mifumo ya uandishi kwa kufaa

Tumia uelekezaji kwa vitu kufunika tabia yenye hali na kuunda mifano ya maeneo. Tumia mtindo wa kiutendaji kwa mabadiliko, ulinganifu, na utabirika kupitia [kutobadilika](https://en.wikipedia.org/wiki/Immutable_object). Tumia usanifu unaoelekezwa kwa data pale utendaji na tabia ya kashe vinapotawala. Mifumo mikubwa huchanganya vyote vitatu. Fanya uchaguzi kwa kila kipengele, na uweke mipaka kati ya mitindo safi.

## Mabadilishano: faida na hasara

| Kanuni / mbinu | Ikitumika vizuri | Njia ya kushindwa |
|---|---|---|
| SOLID | Mishono wazi ambapo mabadiliko hutokea; vitengo vinavyojaribika | Kuenea kwa violesura na tabaka; uelekezaji usio na malipo |
| DRY | Chanzo kimoja cha ukweli kwa maarifa halisi | Dhana isiyo sahihi inayounganisha msimbo usiohusiana |
| KISS / YAGNI | Mifumo myembamba, inayoeleweka | Mishono isiyobuniwa vya kutosha; urekebishaji ghali wa unyumbufu unaohitajika |
| Mifumo ya usanifu | Msamiati wa pamoja; miundo iliyothibitishwa | Ibada ya mizigo ya mifumo; ugumu wa bahati mbaya |
| Domain-Driven Design | Mifano na timu zilizopangwa; ugumu uliodhibitiwa | Taratibu nzito kwa maeneo rahisi; mipaka ya miktadha iliyowekwa vibaya |
| Kiutendaji / isiyobadilika | Utabirika; ulinganifu salama zaidi | Haifai vizuri kwa matatizo yenye hali kwa asili; mshangao wa utendaji |

Mvutano unaojirudia ni kati ya usanifu pungufu na usanifu uliopitiliza. Mifumo isiyobuniwa vya kutosha hukusanya uunganishaji na kuwa migumu. Mifumo iliyobuniwa kupita kiasi huzama katika dhana ambazo mtu lazima azielewe na kuzidumisha. Jibu si nukta isiyobadilika. Ni nidhamu: ahirisha maamuzi hadi uwe na taarifa za kutosha, huku ukihifadhi mishono inayokuruhusu kubadilisha mawazo.

## Maswali ya kujadili na timu yako

1. **Kizingiti chenu madhubuti cha kutoa dhana ya pamoja ni kipi, na unazuiaje DRY isizalishe isiyo sahihi?** Sura hii iko wazi kwamba kurudiwa ni nafuu kuliko dhana isiyo sahihi, na kwamba unapaswa kusubiri hadi mfumo uonekane mara mbili au tatu kabla ya kutoa. Katika timu kubwa hatari ni kwamba mtu anaunganisha vipande viwili vinavyofanana kuwa moduli ya pamoja kuvuka mipaka ya timu, kisha kila badiliko la baadaye kwa mwitaji mmoja linavuka kwa mwingine. Ishara ya kuleta ni kama vipande vilivyorudiwa vinabadilika kwa sababu ileile au vinafanana tu sasa hivi. Kubaliana kanuni ya tatu, na uhitaji kwamba dhana mgombea imebadilika pamoja kweli kabla ya kuunganisha waitaji. Makubaliano hayo moja huzuia aina ya uunganishaji ambayo ni ghali kuutengua timu nyingi zinapoutegemea.

2. **Unafanyaje uunganishaji na mshikamano uonekane kwenye mapitio ya usanifu badala ya kuuacha kwa hisia za tumbo?** Kanuni kuu zinaweka uunganishaji na mshikamano juu ya kila kifupisho, na kufafanua uunganishaji kama mabadiliko yanayovuka mipaka ya moduli. Silika haipanuki kuvuka mamia ya wahandisi ambao kila mmoja anaona kona yake tu ya mfumo. Leta ushahidi ambao mashine inaweza kuuzalisha: michoro ya utegemezi, na data ya mabadiliko-ya-pamoja inayoonyesha moduli zipi zinaendelea kuhaririwa pamoja katika commit zilezile. Ongeza swali wazi la mapitio linalouliza ni mipaka gani ya moduli badiliko linakulazimisha kuvuka. Moduli mbili zinapobadilika pamoja daima, hiyo ndiyo ishara yako ya kuziunganisha au kurekebisha mpaka kati yake.

3. **Mstari uko wapi katika mifumo yenu kati ya eneo lenye utajiri wa kutosha kuhalalisha Domain-Driven Design na programu rahisi ya CRUD ambapo ni ya kupindukia?** Sura inapendekeza miktadha iliyopakana ya DDD hasa kwa sababu inapanga umiliki wa timu na mipaka ya mfano, na inaonya kwamba DDD ni ya kupindukia kwa mifumo rahisi ya unda-soma-sasisha-futa na huharibika kuwa taratibu bila uundaji halisi wa mifano. Kukosea kwa mwelekeo wowote ni ghali: DDD nzito kwenye eneo jembamba huzika programu rahisi katika taratibu, ilhali mfano mkubwa wa pamoja kuvuka timu nyingi hulazimisha uratibu wa kuvuka timu daima. Leta ishara zinazoamua kweli: msongamano wa kanuni za biashara, na timu ngapi zinahitaji kumiliki vipande kwa kujitegemea. Hifadhi mitambo ya kimkakati kwa kiini tata, na uache pembe rahisi zikae rahisi. Hilo linakuweka mbali na maigizo ya DDD na mpira mkubwa wa matope.

4. **Dhana, kiolesura, au mfumo wa usanifu unastahili uelekezaji unaoongeza lini, na nani ana mamlaka ya kuita usanifu uliohandisiwa kupita kiasi?** Sura iko wazi kwamba uelekezaji una gharama unayolipa kwa kila usomaji, na kwamba kutengeneza violesura, viwanda, na tabaka kutimiza SOLID au kuonekana mjuzi ni njia ya kushindwa. Katika timu kubwa shinikizo huenda kinyume: wakaguzi huruhusu dhana ya ziada kupita kwa sababu inaonekana yenye nidhamu, na hakuna anayetaka kuwa mtu anayebishania muundo mdogo. Jambo linaloshindana ni halisi, kwa sababu baadhi ya mishono hulipa gharama yake kweli na kuiondoa baadaye ni ghali. Leta ushahidi madhubuti kwenye mjadala: kiolesura kina utekelezaji ngapi leo, pointi ya upanuzi imewahi kunyumbuka mara ngapi, na faili ngapi msomaji lazima afungue kufuata njia moja ya msimbo. Kubaliana kwamba utekelezaji mmoja usio na wa pili unaoonekana ni sababu chaguo-msingi ya kuiingiza ndani, na utaje nani anaweza kuita usanifu umehandisiwa kupita kiasi bila kusomeka kama tusi. Katika mifumo ya mashirika makubwa na ya serikali inayodumu kuliko waandishi wake kwa muongo, uelekezaji usio wa lazima ni ushuru ambao kila mdumishaji wa baadaye analipa, kwa hiyo chukulia "dhana hii inatununulia nini" kama swali la kudumu la mapitio, si changamoto binafsi.

5. **Unaamuaje mfumo wa uandishi kila kipengele kinatumia, wa kuelekezwa kwa vitu, wa kiutendaji, au unaoelekezwa kwa data, na unaweka mipaka kati yake safi vipi?** Sura inabishana kwamba mifumo mikubwa imechanganywa kwa vitendo na kwamba unapaswa kuchagua kwa kila kipengele kwa kufaa, ukitumia uelekezaji kwa vitu kwa maeneo yenye hali, mtindo wa kiutendaji kwa mabadiliko na ulinganifu, na usanifu unaoelekezwa kwa data pale utendaji na tabia ya kashe vinapotawala. Ikiachwa bila usimamizi, uchaguzi wa mfumo unakuwa suala la nani aliandika moduli kwanza, na hali inayobadilika inavuja kwenye mabadiliko yanayopaswa kuwa safi, au usafi wa kiutendaji unapambana na tatizo lenye hali kwa asili. Ushahidi unaostahili kuletwa ni mahali maumivu yenu halisi yalipo: vipengele vipi ni vigumu kujaribu kwa sababu ya hali iliyofichika, njia zipi za moto zimefungwa na kashe, na mtindo wa sasa unalazimisha njia za kuzunguka zisizo za asili wapi. Amua mfumo chaguo-msingi kwa kila tabaka kwa makusudi na uandike mishono kati ya mitindo inaangukia wapi, ili kiini cha kiutendaji na ukingo wa kiamri visichanganyike. Kwa mfumo unaodhibitiwa au wa serikali ambapo hesabu lazima ikaguliwe na kuzalishwa upya kwa kipindi fulani, kiini kisichobadilika, cha kiutendaji mara nyingi ni sharti la uzingatiaji badala ya ladha, na kikwazo hicho kinapaswa kuendesha mpaka badala ya kuufuata.

6. **Unazuiaje kanuni hizi zisiganduke kuwa itikadi, na unarekodi wapi hoja nyuma ya uamuzi wa usanifu ili timu ya baadaye iweze kuipitia upya?** Kila kanuni katika sura hii ina eneo la matumizi na njia ya kushindwa, na mfumo mzima unazichukulia kama zana za kutumia kwa busara badala ya sheria za kutekeleza. Katika timu kubwa kanuni kimyakimya inakuwa kanuni ngumu: DRY inakataza kurudiwa kwote, SOLID inaamuru kiolesura kwa kila darasa, na vighairi vya vitendo vinazuiwa kwenye mapitio na watu wanaotaja kifupisho badala ya matokeo. Mvutano ni kwamba uthabiti fulani husaidia mamia ya wahandisi kuratibu kweli, kwa hiyo huwezi kutangaza kila kanuni ni ya hiari tu. Leta mifano ambapo kufuata kanuni kwa herufi kulizalisha usanifu mbaya zaidi, na leta rekodi za maamuzi, ikiwa zipo, zinazoeleza kwa nini mpaka au dhana fulani ipo. Kubaliana kwamba kanuni ni chaguo-msingi ambazo mhandisi anaweza kupotoka nazo kwa sababu iliyorekodiwa, na unase chaguo za usanifu zenye matokeo katika rekodi fupi ya uamuzi wa usanifu ili timu inayofuata irithi hoja na si msimbo tu. Katika mifumo ya mashirika makubwa na ya sekta ya umma, ambapo waandishi wa awali wamekwenda zamani na ukaguzi huuliza kwa nini mfumo una umbo ulilo nalo, njia hiyo iliyoandikwa ndiyo tofauti kati ya usanifu ambao timu za baadaye zinaweza kuubadilisha kwa usalama na ule wanaoogopa kuugusa.

## Mtazamo wa sekta

**Kampuni changa.** Pendelea usanifu rahisi zaidi unaotoa na weka moduli moja iliyopangwa vizuri hadi kisa cha pili halisi kikulazimishe mshono. Rasilimali yako adimu ni umakini wa kihandisi, kwa hiyo violesura vya mapema, tabaka, na mifumo ya kubahatisha ni gharama safi. Fuata kanuni ya tatu kabla ya kutoa dhana yoyote ya pamoja, na uache YAGNI iue pointi za upanuzi ambazo hakuna aliyeziomba bado.

**Biashara ndogo.** Bila mbunifu maalumu na bajeti finyu, tegemea usanifu uliojengwa tayari katika mifumo na maktaba unazonunua badala ya kuvumbua mifumo yako mwenyewe. Hifadhi juhudi za usanifu maalumu kwa kanuni chache ambazo ni biashara yako kweli, na uweke kila kitu kingine cha kawaida ili mkandarasi au mwajiriwa mpya aweze kukisoma. Kurudiwa kidogo unakoelewa kunashinda dhana ya busara ambayo mwandishi wake tu anaweza kuidumisha.

**Biashara kubwa.** Malipo ya kanuni za pamoja ni uratibu kuvuka timu nyingi: msamiati wa pamoja wa mapitio ya usanifu, na miktadha iliyopakana inayopanga mipaka ya mfano na umiliki wa timu ili vikundi vibadilike kwa kujitegemea. Simamia uunganishaji na mshikamano waziwazi kwa data ya utegemezi na ya mabadiliko-ya-pamoja, na urekodi maamuzi ya usanifu yenye matokeo ili mifumo ibaki inayobadilika muda mrefu baada ya waandishi wake kuhama. Jilinde kwa usawa dhidi ya dhana isiyo sahihi inayounganisha timu na kuhandisi kupita kiasi kunakotoza kila msomaji.

**Serikali.** Uwezo wa kukaguliwa na kuzalishwa upya mara nyingi huamuru usanifu. Kiini kisichobadilika, cha kiutendaji hukuruhusu kuzalisha upya hesabu ya kihistoria hasa kwa kipindi fulani, jambo ambalo grafu iliyochanganyika ya vitu yenye hali iliyofichika inayobadilika haiwezi kuhakikisha. Pendelea mikataba wazi iliyochapishwa kuliko meza za pamoja kwenye mipaka ya miktadha, na weka usanifu na rekodi zake za maamuzi zikisomeka kwa wakaguzi na kwa timu yoyote itakayorithi mfumo muongo baadaye.

## Mifano

**Kampuni changa.** Kampuni changa ya wahandisi watatu inayojenga bidhaa yake ya kwanza inapinga hamu ya kugawanya kila kipengele katika tabaka za violesura na viwanda, ikiweka moduli moja iliyopangwa vizuri hadi kisa cha pili halisi kitokee. Mantiki ileile inapoonekana mara ya tatu kuvuka mtiririko wa usajili na bili, wanatoa kazi moja ndogo ya pamoja badala ya mfumo wa kubahatisha. Hii inaweka msimbo mdogo vya kutosha kwamba yeyote kati yao anaweza kuushikilia kichwani, na mishono michache wanayochora inaanguka mahali bidhaa inapowezekana kubadilika zaidi.

**Biashara kubwa.** Jukwaa kubwa la bima linaunda sera, madai, na bili kama miktadha iliyopakana tofauti, kila moja ikimilikiwa na timu maalumu yenye mfano wake wa data na mpaka wa huduma. Pale miktadha inapokutana, kama dai linaporejelea sera, inazungumza kupitia mikataba wazi iliyochapishwa badala ya meza za hifadhidata za pamoja. Hili linaziruhusu timu tatu kubadilika kwa kujitegemea, na lugha ya kila mahali inaweka mazungumzo na waandishi wa bima na wataalamu wa hesabu sahihi. Toleo la awali lilikuwa limeshiriki mfano mmoja mkubwa, na kila badiliko lilihitaji uratibu wa kuvuka timu.

**Serikali.** Mfumo wa kitaifa wa usindikaji wa kodi unapendelea kwa makusudi kiini cha kiutendaji, kinachoelekezwa kwa data kwa injini yake ya hesabu. Kanuni za kodi zinaelezwa kama mabadiliko safi juu ya rekodi za ingizo zisizobadilika, jambo linalozifanya zikaguliwe, zijaribike, na ziweze kuzalishwa upya kwa mwaka fulani wa kodi. Sehemu za kiamri, zenye hali (mtiririko wa kazi, arifa) zinawekwa pembeni. Wakaguzi wanaweza kuelekeza kwenye toleo mahususi la kanuni na kuzalisha upya hesabu yoyote ya kihistoria hasa, ambalo ni sharti la kisheria ambalo grafu iliyochanganyika ya vitu yenye hali iliyofichika inayobadilika isingeweza kuhakikisha.

## Kesi ya biashara: sababu, ROI, na TCO

Ubora wa usanifu ni uwekezaji katika *uwezo wa kubadilika* wa mfumo, na uwezo wa kubadilika hutawala jumla ya gharama ya umiliki. Gharama nyingi za mfumo hutua baada ya toleo lake la kwanza, katika marekebisho na upanuzi. Mifumo iliyobuniwa vizuri huweka gharama ya mabadiliko takriban sawa kwa muda. Iliyobuniwa vibaya huona gharama ya kila badiliko ikipanda hadi mfumo unakuwa kwa vitendo hauwezi kubadilishwa na unalazimika kuandikwa upya, matokeo ghali zaidi ya yote.

Gharama ya kupokea hasa ni ujuzi na nidhamu ya mapitio: kufundisha kanuni, na kutumia muda wa usanifu mapema. Gharama ya kutopokea ni mkusanyiko wa polepole wa [deni la kiufundi](https://en.wikipedia.org/wiki/Technical_debt), kasi ya utoaji inayoshuka, viwango vya kasoro vinavyopanda, na kuandika upya kwa gharama hatimaye. Kujenga hoja kwa uongozi, unganisha nidhamu ya usanifu na utabirika wa utoaji na kuepuka programu za kuandika upya, na ufuatilie viashiria vya mbele kama kiwango cha kushindwa kwa mabadiliko na muda wa kutekeleza vipengele vinavyolingana kwa muda. Jihadhari pia na kushindwa kinyume: kuwekeza kupita kiasi katika usanifu kwa siku zijazo zisizo na uhakika pia huharibu thamani. Kwa hiyo hoja ni ya usanifu *unaofaa*, uliolinganishwa na jinsi mabadiliko ya baadaye yanavyowezekana na ghali.

## Mifumo mibaya na mitego

- **Ujumla wa kubahatisha:** kujenga uwezo wa kupanuka kwa mahitaji ya kufikirika ambayo hayafiki kamwe.
- **Dhana isiyo sahihi:** kulazimisha msimbo usiohusiana pamoja kutimiza DRY, kuunda uunganishaji mbaya kuliko kurudiwa.
- **Ibada ya mizigo ya mifumo:** kutumia mifumo ya usanifu kwa ajili yake, kuongeza uelekezaji bila manufaa.
- **Vitu pungufu au vya mungu:** mifano isiyo na tabia, au vitu vinavyofanya kila kitu; vyote viwili vinaashiria majukumu yaliyowekwa mahali pasipofaa.
- **Monolith iliyosambazwa:** huduma zilizogawanywa kimwili lakini bado zimeunganishwa kwa ukali, zikichanganya gharama za mbinu zote mbili.
- **Mpira mkubwa wa matope:** hakuna muundo unaotambulika; kila badiliko linahatarisha kila kitu.
- **Maigizo ya DDD:** kupokea msamiati na muundo wa saraka bila uundaji wa mifano ya eneo unaoipa thamani.

## Kielelezo cha ukomavu

- **Ngazi ya 1, Kuanzisha:** Usanifu ni wa papo hapo na wa kuitikia; uunganishaji hujilimbikiza bila kudhibitiwa; kanuni hazijulikani au hutumika kama kauli mbiu, na dhana huonekana au kutoweka kwa mazoea ya mtu binafsi.
- **Ngazi ya 2, Kuendeleza:** Timu zinajua kanuni na kuzitumia, lakini bila uthabiti na mara nyingi kwa ukakamavu; baadhi ya vikundi husimamia uunganishaji na mshikamano kwa makusudi huku vingine havifanyi, na hakuna msamiati wa pamoja kuvuka shirika.
- **Ngazi ya 3, Kusawazisha:** Msamiati wa pamoja wa usanifu, kanuni ya tatu ya kutoa dhana, uchambuzi wa uunganishaji na mshikamano, na miktadha iliyopakana iliyopangwa kwa timu vimeandikwa na kutarajiwa shirika zima, vinatumika kwa uthabiti kwenye mapitio ya usanifu badala ya kuachwa kwa ladha ya mtu binafsi.
- **Ngazi ya 4, Kusimamia:** Afya ya usanifu inapimwa dhidi ya vipimo vya msingi: data ya uunganishaji na mabadiliko-ya-pamoja, kiwango cha kushindwa kwa mabadiliko, na muda wa kutekeleza vipengele vinavyolingana vinafuatiliwa kwa muda, ili dhana na mipaka ziongezwe, zibakizwe, au ziondolewe kwa ushahidi, na kuhandisi kupita kiasi na dhana isiyo sahihi vinanaswa kwa data badala ya maoni.
- **Ngazi ya 5, Kuratibu:** Nidhamu ya usanifu imeunganishwa na mipango ya utoaji na hatari kuvuka shirika; kanuni zinatumika kwa ufinyu wa maelezo na njia zinazojulikana za kushindwa; chaguo za mfumo na mipaka ni za makusudi na zinapitiwa upya kila wakati, na shirika mara kwa mara hurekebisha muundo, kupanga upya wigo, na kustaafisha dhana eneo na ushahidi vinapohama.

## Mawazo ya kujadili

- Unatofautishaje kati ya mshono unaohitajika na ujumla wa kubahatisha kabla ya kuwa na hitaji la baadaye?
- DRY imeifikisha timu yenu lini kwenye dhana isiyo sahihi, na mlitambuaje?
- Mipaka ya miktadha iliyopakana inapaswa kuanguka wapi, na inapaswa kuakisi chati ya shirika kwa karibu kiasi gani?
- Usanifu kiasi gani unapaswa kutangulia msimbo katika muktadha wenu, na mnarekodije maamuzi?
- Sehemu zipi za mfumo wenu zingenufaika na mtindo wa kiutendaji zaidi au unaoelekezwa kwa data?
- Unazuiaje kanuni za usanifu zisiganduke kuwa itikadi inayopinga vighairi vya vitendo?

## Mambo muhimu ya kukumbuka

- Uunganishaji na mshikamano ndizo sifa zinazojalisha; vifupisho ni njia za kufikia malengo hayo.
- Kila kanuni ina njia ya kushindwa; jua lini kila moja inakupotosha.
- Pendelea kurudiwa kidogo kuliko dhana ya mapema au isiyo sahihi.
- Tumia DDD na miktadha iliyopakana kupangilia maeneo tata na umiliki wa timu.
- Chagua mifumo ya uandishi kwa kufaa; mifumo mikubwa imechanganywa kwa vitendo.
- Buni kwa mabadiliko utakayohitaji kweli, ukiepuka usanifu pungufu na uliopitiliza.

## Marejeo na usomaji zaidi

- Robert C. Martin, *Clean Architecture* and *Agile Software Development, Principles, Patterns, and Practices*
- Eric Evans, *Domain-Driven Design: Tackling Complexity in the Heart of Software*
- Vaughn Vernon, *Implementing Domain-Driven Design*
- Erich Gamma, Richard Helm, Ralph Johnson, John Vlissides, *Design Patterns: Elements of Reusable Object-Oriented Software*
- Martin Fowler, *Refactoring: Improving the Design of Existing Code* and *Patterns of Enterprise Application Architecture*
- David L. Parnas, *On the Criteria to Be Used in Decomposing Systems into Modules*
- Sandi Metz, *Practical Object-Oriented Design*
