# 10.10 Uchumi wa uhandisi wa programu

## Muhtasari na msukumo

Uchumi wa uhandisi wa programu ni nidhamu ya kufanya maamuzi ya kihandisi kwa maneno ya thamani na gharama, chini ya kutokuwa na uhakika, kwa muda. Ni hoja inayojibu maswali ambayo uongozi unauliza kweli. Hii inastahili kujengwa? Chaguo lipi kati ya haya matatu linatoa faida bora? Itatugharimu nini kumiliki mfumo huu kwa muongo ujao, si kuusafirisha robo hii tu? Tulipe [deni hili la kiufundi](https://en.wikipedia.org/wiki/Technical_debt) sasa, au tuliahirishe na kulipa riba? Kila ramani ya njia, ununuzi, uwekezaji wa jukwaa, na programu ya usasishaji ni, chini yake, hoja ya kiuchumi. Sura hii inataja nidhamu inayofanya hoja hizo ziwe wazi, zinazolinganishwa, na zinazoweza kutetewa.

Kwa timu moja, hoja ya kiuchumi inaweza kubaki isiyo rasmi, kwa sababu gharama ya uamuzi mbaya ni ndogo na inarekebishwa haraka. Kwa biashara kubwa au shirika la serikali, dau ni kubwa, fedha ni za watu wengine, na maamuzi yanachunguzwa na fedha, wakaguzi, na umma. Programu inayoonekana nafuu kwa sababu mtu alihesabu gharama ya ujenzi tu, na kupuuza miaka ya uendeshaji, leseni, msaada, na ubadilishaji wa mwisho, itazidi bajeti yake kwa uhakika wa kuogofya. Pendekezo linaloahidi faida lakini halitaji kamwe dhana zake haliwezi kupingwa, kulinganishwa, wala kuwajibishwa. Uchumi wa uhandisi wa programu unakupa lugha ya pamoja, ya kiidadi, ili mtaji adimu uelekee kazi inayounda thamani zaidi.

Sura hii ni uti wa mgongo wa uchambuzi wa hoja ya [faida ya uwekezaji](https://en.wikipedia.org/wiki/Return_on_investment) (ROI) na [jumla ya gharama ya umiliki](https://en.wikipedia.org/wiki/Total_cost_of_ownership) (TCO) inayotumika kote katika mwongozo huu. Usimamizi wa jalada na programu (sura ya 10.1) unaamua *nini* cha kufadhili; sura hii inatoa mbinu ya kiuchumi ya *jinsi* ya kuamua. Inaunganishwa na ununuzi (sura ya 10.3), ambapo hesabu hizi zinahalalisha uchaguzi wa kununua-dhidi-ya-kujenga na wa mikataba; na gharama, FinOps (operesheni za kifedha, yaani usimamizi wenye nidhamu wa matumizi ya wingu na ya wakati wa kuendesha), na programu ya kijani (sura ya 9.4), inayogeuza uchumi wa gharama ya kuendesha kuwa mazoea ya uendeshaji; na bomba la ugunduzi na matokeo (sura ya 11.1), ambapo dhana za thamani huundwa na kujaribiwa; na deni la kiufundi katika kufanya maamuzi na utawala (sura ya 1.5); na matengenezo ya programu (sura ya 3.7), ambapo mkia mrefu wa gharama ya umiliki hutua kweli.

## Kanuni kuu

- **Thamani na gharama zote ni makadirio.** Chukulia kila namba kama safu yenye dhana, si ukweli. Kutokuwa na uhakika kwa uaminifu kunashinda usahihi wa uongo.
- **Fedha ina thamani ya wakati.** Dola ya leo ina thamani kuliko dola ya mwaka ujao; punguza thamani ya mtiririko wa fedha wa baadaye kabla ya kulinganisha chaguo.
- **Amua kwa jumla ya gharama ya umiliki, si bei ya ununuzi.** Ujenzi ni malipo ya awali; uendeshaji, msaada, na uangalizi ni rehani.
- **Gharama na faida za baadaye tu ndizo zinazojali kwa uamuzi.** [Gharama zilizozama](https://en.wikipedia.org/wiki/Sunk_cost) zimeisha; ziache unapochagua cha kufanya baadaye.
- **Kila uchaguzi una [gharama ya fursa](https://en.wikipedia.org/wiki/Opportunity_cost).** Ulinganisho unaofaa ni daima matumizi bora mbadala ya fedha, watu, na muda uleule.
- **Kuchelewa kuna bei.** [Gharama ya kuchelewa](https://en.wikipedia.org/wiki/Cost_of_delay), thamani inayopotea uamuzi au utoaji unaposubiri, mara nyingi ndiyo namba kubwa na inayopuuzwa zaidi kwenye kielelezo.
- **Fanya kesi ya biashara iweze kukanushwa.** Taja dhana kwa wazi hivi kwamba uhalisia unaweza baadaye kuthibitisha kuwa sahihi au si sahihi.

## Mapendekezo

### Weka maamuzi kwenye misingi ya uchumi

Jenga msamiati wa pamoja kabla ya kujenga lahajedwali. Tofautisha *thamani* (faida ambayo mdau anapata) na *gharama* (kinachotumika kuizalisha), na uzieleze zote kama *mtiririko wa fedha*, fedha zinazoingia au kutoka kwa nyakati maalumu. Kwa sababu malipo ya mwaka ujao yana thamani ndogo kuliko ya leo, tumia *[thamani ya fedha kwa wakati](https://en.wikipedia.org/wiki/Time_value_of_money)*: punguza mtiririko wa fedha wa baadaye hadi thamani ya sasa kwa kutumia kiwango cha punguzo kinachoakisi [gharama yenu ya mtaji](https://en.wikipedia.org/wiki/Cost_of_capital) au kiwango rasmi. *Pendekezo* kisha ni ulinganisho uliopangwa wa mitiririko ya fedha ya chaguo pinzani kwa upeo uliofafanuliwa. Sisitiza kwamba kila pendekezo kubwa litaje upeo, kiwango cha punguzo, na dhana zake kwenye ukurasa mmoja, ili wapitiaji wabishane kuhusu kiini badala ya kujenga upya hesabu.

### Amua waziwazi chini ya kutokuwa na uhakika na hatari

Maamuzi ya programu hufanywa kwa taarifa pungufu. Kujifanya vinginevyo ndilo kosa. Unda kielelezo cha kutokuwa na uhakika badala ya kukificha. Tumia makadirio ya pointi tatu (ya matumaini, ya uwezekano, ya kukata tamaa) badala ya namba moja, na uhesabu *[thamani inayotarajiwa](https://en.wikipedia.org/wiki/Expected_value)* kwa kupima matokeo kwa uwezekano wake. Kwa uchaguzi wenye matokeo, endesha [uchambuzi wa unyeti](https://en.wikipedia.org/wiki/Sensitivity_analysis): badilisha pembejeo mbili au tatu zinazojali zaidi na uone kama pendekezo linabadilika. Tofautisha *hatari* (uwezekano unaoweza kupimwa) na *kutokuwa na uhakika* kwa kina (uwezekano usiojulikana), na upendelee chaguo zinazohifadhi unyumbulifu kutokuwa na uhakika kunapokuwa juu. Ahadi ya hatua inayokuruhusu kusimama, kugeuka, au kuongeza baada ya kujifunza mara nyingi ina thamani kuliko dau la bei nafuu la yote-au-hakuna.

### Linganisha mbinu ya uamuzi na muktadha wa faida na wa umma

Mashirika ya kutafuta faida kwa kawaida huboresha faida ya kifedha, kwa kutumia [thamani halisi ya sasa](https://en.wikipedia.org/wiki/Net_present_value), ROI, na kurudisha, dhidi ya gharama ya mtaji. Vyombo visivyo vya faida na vya sekta ya umma huboresha thamani ya dhamira, matokeo ya huduma, usawa, na uangalizi wa fedha za umma, na haviwezi kupunguza kila faida kuwa mapato. Tumia vifaa vya uchambuzi vilevile katika mazingira yote mawili, lakini chagua kazi ya lengo kwa uaminifu. Katika serikali, uchambuzi wa [gharama-na-faida](https://en.wikipedia.org/wiki/Cost%E2%80%93benefit_analysis) na wa ufanisi wa gharama, viwango rasmi vya punguzo, na kuhesabu gharama ya maisha yote mara nyingi vinaamriwa. Weka thamani ya fedha kwa kinachoweza kuwekewa, na kwa kilichobaki tumia vigezo wazi, vilivyoandikwa visivyo vya kifedha badala ya kuviingiza kama vigezo vya kudanganya. Katika ulimwengu wote mbili, nidhamu ni ileile: fanya lengo na mabadilishano yaonekane.

### Kadiria gharama kwa zaidi ya mbinu moja

Hakuna mbinu moja ya ukadiriaji inayoaminika peke yake, kwa hiyo linganisha kwa pembetatu. Unganisha *ulinganisho* (linganisha na kazi iliyopita inayofanana), *hukumu ya mtaalamu* (maoni yaliyopangwa kutoka wahandisi wenye uzoefu, mfano wideband Delphi au planning poker), *kugawanya* (gawa kazi na kukunja makadirio kutoka chini-juu), na *vielelezo vya vigezo* (vinavyoendeshwa na fomula, kama [COCOMO II](https://en.wikipedia.org/wiki/COCOMO), vilivyorekebishwa kwa data yenu). Pale mnapokuwa na upitishaji wa kimajaribio, pendelea data ya kihistoria ya mtiririko kuliko ukubwa wa makisio. Daima eleza makadirio kama safu zenye imani, kadiria upya unapojifunza, na utenganishe kadirio la *juhudi* na ahadi ya *tarehe*. Kuchanganya hivyo viwili ndivyo makadirio yanavyogeuka ahadi zilizovunjika.

### Hesabu TCO, ROI, NPV, na kurudisha kwa uthabiti

Pokea seti ndogo, ya kawaida ya zana na uitumie kwa usawa, ili chaguo zilinganishwe kuvuka jalada. *Jumla ya gharama ya umiliki* hujumlisha gharama zote kuvuka maisha kamili: kujenga, kusambaza, leseni, kuendesha, kusaidia, kulinda, na kustaafisha. *ROI* huonyesha faida halisi kama asilimia ya gharama. *Thamani halisi ya sasa (NPV)* hupunguza kila mtiririko wa fedha wa baadaye hadi leo na kuujumlisha; NPV chanya inamaanisha chaguo linaunda thamani kwa kiwango chenu cha punguzo. *[Kipindi cha kurudisha](https://en.wikipedia.org/wiki/Payback_period)* ni muda wa kurejesha matumizi ya awali. Ni rahisi na angavu, lakini kipofu kwa kila kitu baada ya kufidia na kwa thamani ya fedha kwa wakati, kwa hiyo kitumie tu kando ya NPV. Sawazisha upeo na kiwango cha punguzo kuvuka chaguo zinazolinganishwa, la sivyo ulinganisho hauna maana.

### Weka bei kwenye deni la kiufundi na gharama ya kuchelewa

Fanya gharama mbili ambazo kwa kawaida hazionekani ziwe wazi. *Deni la kiufundi* hufanya kama deni la kifedha: njia za mkato hukopa kasi sasa na kutoza riba baadaye, kama utoaji wa polepole, kasoro zaidi, na gharama ya juu ya uendeshaji. Kadiria riba, deni linatoza kiasi gani kila toleo la baadaye, ili uchaguzi wa kulipata au kulilipa uwe uamuzi wa kiuchumi badala ya wa kimaadili (tazama sura za 1.5 na 3.7). *Gharama ya kuchelewa* ni thamani inayopotea kwa kila kitengo cha muda ambacho kitu chenye thamani kinachelewa. Kukipima kunabadilisha silika hafifu za "tunapaswa kuharakisha" kuwa kupa kipaumbele halisi, moja kwa moja zaidi kupitia upangaji wa Weighted-Shortest-Job-First. Timu zinazopima bei ya kuchelewa huacha kuboresha matumizi ya wafanyakazi na kuanza kuboresha thamani.

### Thamini vitu visivyoshikika na ujenge kesi ya biashara

Faida nyingi kubwa zaidi hupinga namba safi ya dola: hatari iliyopungua, msimamo bora wa usalama, tija ya wasanidi, uaminifu wa chapa, matokeo ya dhamira, chaguo. Kujifanya ni sifuri kunapendelea kila uamuzi kuelekea kinachoshikika. Vithamini hata hivyo. Weka thamani ya fedha kupitia mbadala pale panapoaminika (gharama ya uvunjaji uliopitwa, saa zilizookolewa mara kiwango kilichopakiwa). Pale usipoweza, vipe alama waziwazi dhidi ya vigezo vilivyotajwa na uvibebe kando ya kielelezo cha kifedha. Kusanya yote kuwa *kesi ya biashara*: tatizo, chaguo zilizozingatiwa (ikijumuisha kutofanya chochote), gharama na faida kuvuka upeo, dhana na hatari muhimu, pendekezo, na vipimo ambavyo mtahukumu baadaye kama ilifanya kazi. Iweke hai, na uipitie dhidi ya halisi ili shirika lenu lijifunze kukadiria vizuri zaidi.

## Mabadilishano: faida na hasara

| Mbinu | Faida | Hasara |
|---|---|---|
| Uundaji wa kina wa kiidadi (NPV, TCO) | Kamili, unalinganishwa, unakaguliwa; unalazimisha dhana kutoka wazi | Unachukua muda; usahihi wa uongo ikiwa pembejeo ni dhaifu; unaweza kuacha kisichopimwa |
| Mbinu nyepesi za kidole gumba (kurudisha, gharama ya kuchelewa) | Za haraka, angavu, rahisi kuwasilisha | Hupuuza thamani ya wakati au gharama za mkia mrefu; butu kwa ahadi kubwa |
| Makadirio ya namba moja | Rahisi, ya kuamua, rahisi kupanga kuzunguka | Huficha kutokuwa na uhakika; huwa ahadi za uongo; huadhibu uaminifu |
| Safu na thamani inayotarajiwa | Ya uaminifu kuhusu hatari; inaunga mkono maamuzi ya hatua | Ngumu kuwasilisha; inaweza kuhisi ya kukwepa kwa wadau wanaotaka namba moja |
| Kuweka thamani ya fedha kwa vitu visivyoshikika kupitia mbadala | Inaweka faida kubwa kwenye kielelezo; inawezesha mabadilishano | Mbadala zinaweza kupingwa; hatari ya kutengeneza namba rahisi |
| Uchambuzi kamili wa TCO wa maisha yote | Huzuia mshangao wa jenga-nafuu-endesha-ghali | Inahitaji data ya gharama ya kuendesha ambayo timu nyingi hazina mapema |

Mvutano unaojirudia ni kati ya ukali na kasi. Uundaji mzito wa kifedha unaboresha maamuzi makubwa, yasiyoweza kutenduliwa, ghali, lakini ni upotevu, hata madhara, kwa madogo, yanayoweza kutenduliwa, ambapo unatakasa tu jibu lililoamuliwa mapema kwa mamlaka ya lahajedwali. Mashirika yaliyokomaa hurekebisha uchambuzi kulingana na dau: hoja ya ukurasa mmoja ya gharama ya kuchelewa kwa kipengele cha kawaida, kesi kamili ya NPV-na-TCO kwa jukwaa au ununuzi wa miaka mingi. Mvutano wa pili ni kati ya usahihi na uaminifu. Namba moja ya kujiamini ni rahisi kutendea kazi lakini mara nyingi si sahihi. Safu ni ya kweli lakini ngumu zaidi kuahidi. Suluhisho ni kuamua kwa safu na thamani inayotarajiwa, kisha kuahidi nyongeza za hatua, ili mbaki na chaguo la kusahihisha mwelekeo ushahidi unapofika.

## Maswali ya kujadili na timu yako

1. **Tunatenganisha kadirio la juhudi na ahadi ya tarehe, na je, tunalinganisha makadirio kwa pembetatu badala ya kuamini namba moja?** Namba moja ya kujiamini ni rahisi kupanga kuzunguka na mara nyingi si sahihi, na kadirio la juhudi la safu linapogandishwa kuwa tarehe thabiti, uaminifu unaadhibiwa na kadirio linakuwa ahadi iliyovunjika. Linganisha kwa pembetatu: unganisha ulinganisho, hukumu ya mtaalamu, kugawanya, na upitishaji wa kihistoria, na upendelee data halisi ya mtiririko kuliko ukubwa wa makisio. Eleza makadirio kama safu zenye imani, na ukadirie upya unapojifunza. Kwa programu kubwa chini ya uchunguzi wa fedha na ukaguzi, hii ndiyo tofauti kati ya utabiri unaoweza kutetewa na namba ambayo hakuna anayeweza kuipinga. Leta kadirio la hivi karibuni lililoteleza na uulize kama lilikuwa kadirio la juhudi lililosimamiwa kuelekea kalenda.

2. **Tunapima gharama ya kuchelewa na kuitumia kupanga mfuatano wa kazi, au bado tunaboresha matumizi ya wafanyakazi?** Gharama ya kuchelewa, thamani inayopotea kwa kila kitengo cha muda kitu chenye thamani kinapochelewa, mara nyingi ndiyo namba kubwa na inayopuuzwa zaidi kwenye kielelezo. Timu ambazo hazijawahi kuipima huboresha kuweka kila mtu na shughuli, jambo linalonyima kimyakimya kazi yenye thamani ya juu zaidi. Ipime na upange mfuatano kwa Weighted-Shortest-Job-First ili kazi inayopoteza thamani zaidi kwa kusubiri iende kwanza. Hii inapanga upya ramani za njia na kubadilisha "tunapaswa kuharakisha" kuwa kupa kipaumbele halisi. Leta mipango miwili au mitatu inayoendelea na ukadirie kila mmoja unagharimu kiasi gani kwa wiki ya kuchelewa; usipoweza, hilo ndilo pengo la kufunga.

3. **Kesi zetu za biashara zinaamua kwa TCO ya maisha yote dhidi ya msingi wa kutofanya chochote, na je, ukali umerekebishwa kulingana na dau?** Ujenzi ni malipo ya awali; uendeshaji, leseni, msaada, na ubadilishaji wa mwisho ni rehani, na programu inayohesabu gharama ya ujenzi tu itazidi bajeti yake kwa uhakika wa kuogofya. Kila pendekezo kubwa linapaswa kulinganisha chaguo (ikijumuisha kutofanya chochote) kwa upeo wa kawaida kwa kiwango cha punguzo cha pamoja, na kutaja dhana zake kwenye ukurasa mmoja ili wapitiaji wabishane kuhusu kiini badala ya hesabu. Rekebisha juhudi: hoja ya ukurasa mmoja ya gharama ya kuchelewa kwa kipengele cha kawaida, kesi kamili ya NPV-na-TCO kwa jukwaa au ununuzi wa miaka mingi. Uundaji mzito wa uamuzi mdogo, unaoweza kutenduliwa unatakasa tu jibu lililoamuliwa mapema kwa mamlaka ya lahajedwali. Leta uamuzi wa hivi karibuni na uulize kama gharama ya kuendesha, si bei ya orodha, ndiyo iliyoendesha.

4. **Tunatumia kiwango gani cha punguzo kulinganisha chaguo kwa muda, na je, tumejaribu kama pendekezo linanusurika kiwango tofauti?** Thamani ya fedha kwa wakati inamaanisha dola ya mwaka wa tano si dola ya leo, hata hivyo mapendekezo mengi ama huruka kupunguza thamani kabisa au huzika kiwango ambacho hakuna aliyekubali. Sawazisha kiwango kimoja na upeo mmoja kuvuka chaguo zinazolinganishwa, la sivyo ulinganisho ni hesabu iliyovaa ufahamu. Mazingatio yanayoshindana ni kwamba kiwango chenyewe kinaweza kupingwa: cha chini mno na unavimbisha miradi mikubwa ya muda mrefu, cha juu mno na unanyima uwekezaji unaorudisha polepole. Leta kiwango ulichotumia, kilikotoka (gharama yenu ya mtaji, au kiwango rasmi kilichochapishwa), na uchambuzi wa unyeti unaoonyesha pendekezo linabadilika kwa kiwango gani. Kwa fedha za biashara kubwa na hasa serikali, kiwango mara nyingi kimeamriwa, kwa mfano kiwango rasmi cha tathmini, na kiwango kisichoandikwa au kisicho thabiti ndicho hasa mkaguzi atakachokipinga kwanza.

5. **Mpango unapofanya vibaya, tunaamua kwa thamani inayotarajiwa ya baadaye na kupuuza tulichotumia tayari, na je, tumepanga ufadhili ili tuweze kusimamisha kweli?** Gharama zilizozama zimeisha, lakini zinavuta kwa nguvu: timu hutetea juhudi zinazoshindwa kwa fedha zilizomwagwa tayari badala ya thamani iliyobaki mbele. Shinikizo linaloshindana ni halisi, kwa sababu kusimamisha kunaonekana kama kukiri upotevu na kunabeba gharama ya kisiasa, kwa hiyo nidhamu lazima ijengwe kwenye jinsi mnavyofadhili badala ya kuachiwa jinsi mtu anavyohisi wakati huo. Pendelea ahadi za hatua zenye thamani huru zinazokuruhusu kusimama, kugeuka, au kuongeza baada ya kila nyongeza, badala ya dau moja lisiloweza kutenduliwa. Leta juhudi inayoendelea iliyo nyuma, gharama iliyobaki ya kumaliza ikiwekwa dhidi ya faida iliyobaki inayotarajiwa, na hatua ambapo lango linalofuata la ufadhili linaangukia. Katika jalada la biashara kubwa au la serikali, taja nani ana mamlaka ya kusimamisha programu na kama muundo wa ufadhili unampa hatua halisi ya uamuzi, kwa sababu ahadi isiyo na lango ni ahadi ambayo hakuna anayeweza kuisimamisha.

6. **Tuko wazi kuhusu kazi yetu ya lengo, na tunathamini vitu visivyoshikika waziwazi badala ya kuvichukulia kama sifuri?** Faida nyingi kubwa zaidi, hatari iliyopungua, msimamo wa usalama, tija ya wasanidi, matokeo ya dhamira, na chaguo, hupinga namba safi ya dola, na kujifanya ni sifuri kunapendelea kila uamuzi kuelekea kinachoshikika na cha karibu. Hatari inayoshindana ni kosa kinyume: kutengeneza namba rahisi na kuvisha makisio usahihi wa uongo. Amua kwa makusudi faida zipi mtaweka thamani ya fedha kupitia mbadala zinazoaminika (uvunjaji uliopitwa, saa zilizookolewa mara kiwango kilichopakiwa) na zipi mtazipa alama dhidi ya vigezo vilivyotajwa visivyo vya kifedha vilivyobebwa kando ya kielelezo. Leta uamuzi wa hivi karibuni ambapo kitu kisichoshikika kilijali na uulize kama kilipimwa, kilipewa alama, au kilitupwa kimya. Kwa chombo cha sekta ya umma hili ni kali zaidi: thamani ya dhamira, usawa, na uangalizi wa fedha za umma haviwezi vyote kupunguzwa kuwa mapato, kwa hiyo chagua kazi ya lengo wazi na uandike vigezo visivyo vya kifedha badala ya kuviingiza kama vigezo vya kudanganya.

## Mtazamo wa sekta

**Kampuni changa.** Ukiwa na miezi ya njia ya kukimbia, namba kuu ya kiuchumi ni gharama ya kuchelewa: kila wiki wahandisi wako wachache wanayotumia nje ya bidhaa kuu ni mapato na kujifunza vilivyoahirishwa. Weka uchambuzi kwenye ukurasa mmoja na upendelee kununua uwezo wa kawaida kuliko kuujenga, ili umakini adimu wa kihandisi ubaki kwenye kinachotofautisha. Ruka vielelezo vya kina vya NPV; ulinganisho wa takriban wa maisha yote na kikomo kigumu cha matumizi vinatosha kukamata mtego wa jenga-nafuu-endesha-ghali kabla haujauma.

**Biashara ndogo.** Huna mchambuzi wa kifedha, kwa hiyo weka mbinu rahisi na ya uaminifu: linganisha gharama kamili ya kumiliki kila chaguo, usajili pamoja na masaa ya wafanyakazi unayotumia, dhidi ya kutofanya chochote. Uamuzi wa kununua-dhidi-ya-kujenga karibu daima unapendelea kununua, kwa sababu mfumo usioweza kuudumisha unakuwa gharama ya kuendesha isiyo kwenye bajeti inayokua kimyakimya. Hukumu uwekezaji kwa kurudisha kwa muda mfupi, angavu badala ya vielelezo vilivyopunguzwa, na uangalie bei ya kila kiti inayoonekana nafuu hadi unapopanuka.

**Biashara kubwa.** Changamoto ni uwezo wa kulinganisha kuvuka timu nyingi na jalada refu: sawazisha kiwango kimoja cha punguzo, upeo mmoja, na seti moja ya zana (NPV, TCO, gharama ya kuchelewa) ili mapendekezo pinzani yapangwe kwa msingi uleule. Pima waziwazi riba ya deni la kiufundi na gharama ya kuchelewa, kwa sababu kwa ukubwa vinazidi gharama za ujenzi za kichwa cha habari. Fanya kesi za biashara kuwa nyaraka hai zinazopitiwa dhidi ya halisi, ili usahihi wa ukadiriaji uboreke na fedha na ukaguzi viweze kuona kwa nini mtaji ulienda mahali ulipoenda.

**Serikali.** Uchambuzi wa gharama-na-faida, kiwango rasmi cha punguzo, na kuhesabu gharama ya maisha yote mara nyingi vimeamriwa, na lengo ni thamani ya umma badala ya mapato, kwa hiyo weka thamani ya fedha kwa unachoweza kwa uaminifu na upe alama kilichobaki dhidi ya vigezo vilivyo wazi, vilivyochapishwa. Taja kila dhana waziwazi dhidi ya msingi wa kutofanya chochote, kwa sababu wakaguzi na umma watazijaribu. Panga ufadhili kuwa nyongeza zenye thamani huru ili faida za kila hatua zitimizwe na kupimwa kabla ya inayofuata kuahidiwa, na ili programu iweze kusimamishwa bila kuacha fedha za umma zilizozama zikiwa zimekwama.

## Mifano

**Kampuni changa.** Kampuni changa ya watu sita yenye njia ya kukimbia ya miezi tisa inajadili kujenga mfumo wake wa utozaji au kulipia uliopangishwa. Kwenye ukurasa mmoja, waanzilishi wanalinganisha chaguo mbili kwa upeo wa miezi kumi na minane: ujenzi unaonekana nafuu kwenye karatasi lakini unagharimu miezi mitatu ya mhandisi mapema, na gharama ya kuchelewa (mapato yaliyoahirishwa wahandisi hao wasiposafirisha bidhaa kuu) inazidi sana ada ya usajili. Wananunua utozaji uliopangishwa, wanalinda muda adimu wa kihandisi kwa kinachotofautisha, na kuupitia uamuzi tu bei au kiasi kinapobadilisha hesabu.

**Biashara kubwa.** Muuzaji wa rejareja anapima kubadilisha jukwaa la biashara mtandaoni dhidi ya kuendelea kupachika la zamani. Timu ya uhandisi-na-fedha inajenga kielelezo cha miaka mitano kwa kiwango cha punguzo cha shirika, ikilinganisha chaguo tatu (kutofanya chochote, kurekebisha kwa nyongeza, na kubadilisha jukwaa kamili) kwa TCO kuvuka ujenzi, gharama ya kuendesha wingu, leseni, na msaada. Wanapima riba ya deni la kiufundi ya hali ya sasa (viwango vya matukio vinavyopanda na mdundo wa matoleo unaopungua) na gharama ya kuchelewa ya vipengele ambavyo jukwaa la zamani haliwezi kuunga mkono. Kubadilisha jukwaa kunaonyesha gharama ya juu ya awali lakini NPV chanya kufikia mwaka wa tatu na gharama ya chini ya kuendesha baada ya hapo. Uchambuzi wa unyeti unathibitisha pendekezo linashikilia isipokuwa bei za wingu zipande sana. Wanalifadhili kwa hatua zilizofungwa na hatua muhimu badala ya ahadi moja isiyoweza kutenduliwa.

**Serikali.** Wakala unaosasisha mfumo wa mafao unahitajika kuwasilisha uchambuzi wa gharama-na-faida kwa kutumia kiwango rasmi cha punguzo na kuhesabu gharama ya maisha yote. Kwa sababu faida kuu ni matokeo ya dhamira (huduma ya haraka zaidi, sahihi zaidi, ya usawa zaidi), timu inaweka thamani ya fedha kwa inachoweza kwa uaminifu (mzigo mdogo wa kituo cha simu, malipo yenye makosa machache, ulaghai ulioepukwa) na kupa alama kilichobaki dhidi ya vigezo wazi vya thamani ya umma badala ya kubuni namba za dola. Kesi ya biashara inawasilisha msingi wa kutofanya chochote, inataja dhana zake wazi kwa ukaguzi, na kupanga ufadhili kuwa nyongeza zenye thamani huru, ili faida za kila hatua zitimizwe na kupimwa kabla ya inayofuata kuahidiwa.

## Kesi ya biashara: sababu, ROI, na TCO

Faida ya kutumia uchumi wa uhandisi wa programu ni ugawaji bora wa mtaji: fedha, watu, na muda vinaelekea kazi inayounda thamani zaidi. Utaratibu ni wa sehemu tatu. Kwanza, upotevu ulioepukwa: mapendekezo yanayoshindwa mtihani wa uaminifu wa NPV au TCO yanakataliwa kabla hayajatumia miaka ya matumizi. Pili, mfuatano bora: kupima gharama ya kuchelewa kunasogeza mbele kazi yenye thamani ya juu zaidi, kujilimbikiza faida kuvuka jalada. Tatu, mshangao ghali chache: kuhesabu gharama ya maisha yote huzuia kushindwa kwa kawaida kwa kufadhili ujenzi wa bei nafuu na kushambuliwa na uendeshaji ghali.

Gharama ya mazoea ni ndogo: muda wa mchambuzi wa kujenga vielelezo, nidhamu ya kutaja dhana, na kazi ya kitamaduni ya kuwafanya viongozi waamue kwa namba zilizopunguzwa za maisha yote badala ya bei za kichwa cha habari. Gharama ya *kutoyafanya* ni kubwa zaidi lakini imesambaa. Mnathamini kupita kiasi kinachoshikika na cha karibu kimfumo, mnapima chini deni na kuchelewa, na mnagundua gharama za kuendesha tu baada ya kuwa zisizoepukika. Wasilisha nidhamu kwa uongozi kama udhibiti wa ubora wa kila uamuzi mwingine wa uwekezaji. Haiongezi mstari mpya wa matumizi bali inafanya kila mstari uliopo uwajibike. Mpango mmoja wa thamani ndogo ulioepukwa, au utabiri mmoja sahihi wa TCO unaozuia kulipuka kwa gharama ya kuendesha, unalipia mazoea yote mara nyingi.

## Mifumo mibaya na mitego

- **Bei ya ununuzi kama jumla ya gharama.** Kuamua kwa ada ya ujenzi au leseni huku ukipuuza miaka ya uendeshaji, msaada, na ubadilishaji wa mwisho.
- **Ahadi ya gharama iliyozama.** Kuendelea na juhudi inayoshindwa kwa sababu ya fedha zilizotumika tayari badala ya thamani inayotarajiwa ya baadaye.
- **Maigizo ya usahihi.** Lahajedwali za desimali kumi zilizojengwa juu ya pembejeo zilizokisiwa, zikitoa mamlaka ya uongo kwa hitimisho lililoamuliwa mapema.
- **Kupuuza thamani ya fedha kwa wakati.** Kulinganisha mtiririko wa fedha wa karibu na wa mbali kana kwamba dola ya mwaka wa tano ni sawa na dola ya leo.
- **Visivyoshikika kama sifuri.** Kuacha hatari, usalama, tija, na thamani ya dhamira kwa sababu ni ngumu kuweka bei, kupendelea kila uamuzi kuelekea kinachopimika.
- **Kadirio kama ahadi.** Kuchukulia kadirio la juhudi la safu kama ahadi ya tarehe thabiti, kisha kusimamia kalenda.
- **Deni la kiufundi lisilopimwa.** Kuchukua njia za mkato bila hesabu ya riba, hadi kodi inayojilimbikiza kwenye utoaji inakuwa mgogoro.
- **Upofu wa gharama ya kuchelewa.** Kuboresha matumizi ya timu na gharama ya kitengo huku ukipuuza thamani kubwa zaidi inayopotea kwa kuchelewa.

## Kielelezo cha ukomavu

**Ngazi ya 1 (Kuanzisha).** Maamuzi yanahalalishwa kwa bei ya kichwa cha habari na hisia, kwa kuitikia na kesi kwa kesi. Hakuna kupunguza, hakuna TCO, hakuna dhana zilizotajwa. Makadirio ni namba moja zinazochukuliwa kama ahadi. Deni la kiufundi na gharama ya kuchelewa haviko kwenye kielelezo chochote.

**Ngazi ya 2 (Kuendeleza).** Uwekezaji mkubwa unabeba kesi ya biashara ya takriban yenye baadhi ya gharama na faida, na baadhi ya gharama za kuendesha zinazingatiwa. Kurudisha rahisi au ROI inaonekana, lakini thamani ya fedha kwa wakati na kuhesabu gharama ya maisha yote vinatumika bila usawa na vinatofautiana timu kwa timu. Makadirio wakati mwingine hubeba safu, ingawa mazoea hayana uthabiti.

**Ngazi ya 3 (Kusawazisha).** Seti ya kawaida ya zana za kiuchumi (NPV, TCO, ROI, gharama ya kuchelewa) yenye kiwango cha pamoja cha punguzo na upeo imeandikwa na kutumika kwa uthabiti kuvuka jalada. Kutokuwa na uhakika kunaundwa kwa safu na thamani inayotarajiwa. Deni la kiufundi linakadiriwa na kupewa kipaumbele. Kesi za biashara zinalinganisha msingi wa kutofanya chochote, zinataja dhana zake, na zinakaguliwa.

**Ngazi ya 4 (Kusimamia).** Utabiri unapimwa dhidi ya halisi na kudhibitiwa kwa data. Usahihi wa ukadiriaji, ROI iliyotimizwa, gharama ya kuendesha dhidi ya makadirio, na matokeo ya gharama ya kuchelewa vinafuatiliwa dhidi ya vipimo vya msingi, na tofauti kubwa inachochea mapitio. Kesi za biashara zinabeba vipimo vilivyofafanuliwa vya mafanikio na vigezo vya kusimamisha vinavyotekelezwa kwa ushahidi badala ya hisia, na dhana za kiwango cha punguzo na unyeti zinathibitishwa dhidi ya matokeo ya kihistoria, kwa hiyo namba zinadhibitiwa badala ya kuzalishwa tu.

**Ngazi ya 5 (Kuratibu).** Hoja ya kiuchumi ni endelevu, iliyorekebishwa, na imeunganishwa na upangaji wa jalada, ununuzi, na hatari. Kesi za biashara ni nyaraka hai zinazopitiwa ushahidi unapofika, na usahihi wa ukadiriaji unaboreka kwa muda kwa sababu matokeo yanarudi. Gharama ya kuchelewa inaendesha mfuatano, vitu visivyoshikika vinathaminiwa waziwazi, na ufadhili wa hatua unahifadhi chaguo, kwa hiyo shirika linasawazisha upya mtaji kwa kujirekebisha kuelekea kazi inayounda thamani zaidi hali zinapohama.

## Mawazo ya kujadili

- Ukali wa kifedha wa kiasi gani unastahili kutumika kwa uamuzi unaoweza kutenduliwa, wa gharama ndogo kabla uchambuzi haujagharimu zaidi ya uamuzi?
- Shirika lenu linapaswa kutumia kiwango gani cha punguzo, na pendekezo linabadilika kiasi gani mnapokibadilisha?
- Kuweka thamani ya fedha kwa kitu kisichoshikika ni ufahamu wa kweli lini, na ni kutengeneza namba rahisi lini?
- Mnapimaje riba ya deni la kiufundi kwa ushawishi wa kutosha ili uongozi ufadhili kulilipa?
- Katika mazingira ya sekta ya umma, mnapimaje usawa na matokeo ya dhamira yanayopinga kuwekewa thamani ya fedha dhidi ya chaguo zenye faida safi zaidi ya kifedha?
- Kesi za biashara zinapaswa kupitiwa dhidi ya halisi, na nani anawajibika thamani iliyotimizwa inapotofautiana na utabiri?

## Mambo muhimu ya kukumbuka

- Uchumi wa uhandisi wa programu hufanya mabadilishano ya thamani-na-gharama yawe wazi, yanayolinganishwa, na yanayoweza kutetewa: ni uti wa mgongo wa uchambuzi wa hoja ya ROI na TCO inayotumika kote katika mwongozo huu.
- Amua kwa jumla ya gharama ya umiliki kuvuka maisha kamili, si bei ya ununuzi, na upunguze thamani ya mtiririko wa fedha wa baadaye ili thamani ya fedha kwa wakati iheshimiwe.
- Chukulia makadirio kama safu chini ya kutokuwa na uhakika, linganisha gharama kwa pembetatu kwa mbinu nyingi, na usiruhusu kadirio la juhudi kuwa ahadi ya tarehe thabiti.
- Pima gharama zisizoonekana kwa kawaida, deni la kiufundi kama riba na gharama ya kuchelewa kama thamani iliyopotea, kwa sababu mara nyingi ndizo namba kubwa zaidi kwenye kielelezo.
- Thamini vitu visivyoshikika waziwazi badala ya kuvichukulia kama sifuri, na uchague kazi ya lengo ya faida au ya umma kwa uaminifu.
- Jenga kesi hai za biashara zinazotaja dhana na chaguo ikijumuisha kutofanya chochote, rekebisha ukali kulingana na dau, na upitie utabiri dhidi ya halisi ili shirika lijifunze kukadiria vizuri zaidi.

## Marejeo na usomaji zaidi

- Barry W. Boehm, *Software Engineering Economics*
- Barry W. Boehm et al., *Software Cost Estimation with COCOMO II*
- IEEE Computer Society, *SWEBOK Guide* (Software Engineering Economics knowledge area)
- Donald G. Reinertsen, *The Principles of Product Development Flow* (cost of delay, WSJF)
- Steve McConnell, *Software Estimation: Demystifying the Black Art*
- Douglas W. Hubbard, *How to Measure Anything: Finding the Value of Intangibles in Business*
- Ward Cunningham, "The WyCash Portfolio Management System" (the technical-debt metaphor)
- Philippe Kruchten, Robert Nord, and Ipek Ozkaya, *Managing Technical Debt*
- Mark Schwartz, *The Art of Business Value* and *A Seat at the Table*
- U.S. Office of Management and Budget, Circular A-94 (guidelines and discount rates for benefit-cost analysis)
- HM Treasury, *The Green Book: Central Government Guidance on Appraisal and Evaluation*
