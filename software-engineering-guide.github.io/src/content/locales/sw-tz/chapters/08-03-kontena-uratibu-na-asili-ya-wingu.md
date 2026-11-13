# 8.3 Kontena, uratibu, na asili ya wingu

## Muhtasari na msukumo

[Kontena](https://en.wikipedia.org/wiki/OS-level_virtualization) hufunga programu pamoja na utegemezi wake kuwa kitengo kimoja, kinachohamishika, kilichotengwa. Linaendesha kwa njia ileile kwenye kompyuta ndogo, kwenye mazingira ya majaribio, na kwenye uzalishaji. Majukwaa ya uratibu, hasa [Kubernetes](https://en.wikipedia.org/wiki/Kubernetes), hupanga na kusimamia idadi kubwa ya kontena kuvuka meli za mashine. Yanashughulikia uwekaji, kupanuka, afya, mitandao, na kupona. [Asili ya wingu](https://en.wikipedia.org/wiki/Cloud-native_computing) ni mtindo mpana wa usanifu uliojengwa juu ya misingi hii: programu zilizosanifiwa kama huduma zilizounganishwa kwa ulegevu, zinazosambazwa kwa uhuru, zinazopanuka kwa mlalo zinazodhania miundombinu inayobadilika, inayojiponya.

Kwa timu kubwa, kontena na uratibu hutatua tatizo moja gumu. Unahitaji kuendesha huduma nyingi, zilizojengwa na timu nyingi, kwa kutegemewa na kwa ufanisi kwenye miundombinu ya pamoja. Kontena huipa kila timu mkataba thabiti wa kufunga na wa wakati wa kuendesha, unaostaafisha daraja la kushindwa la "inafanya kazi kwenye mashine yangu." Uratibu huficha mashine mmoja mmoja nyuma ya msingi wa pamoja, kwa hiyo timu zinasambaza kwenye jukwaa badala ya seva. Usanifu huu ndio unaokuruhusu kuendesha mamia au maelfu ya huduma bila kila timu kubuni upya usambazaji, kupanuka, na ustahimilivu.

Wapokeaji wa mashirika makubwa na serikali hupata uwezo wa kuhamishika, ustahimilivu, na njia ya kuondoka kwenye kufungwa. Kwa kurudisha, wanarithi ugumu halisi na wajibu mpya wa usalama. Jukwaa la kontena lina nguvu hasa kwa sababu linaweza kupangwa na linabadilika, jambo linalomaanisha lazima uliongoze kwa makini. Asili ya picha, kutenganisha wapangaji wengi, sera za mtandao, na gharama vyote vinakuwa wasiwasi wa kiwango cha jukwaa. Wapokeaji wa sekta ya umma wanazidi kuongeza mahitaji ya enzi: udhibiti wa mahali data inapoishi na nani anaweza kuifikia. Hilo hufanya uwezo wa kuendesha mizigo thabiti kuvuka mazingira yaliyochaguliwa kuwa uwezo wa kimkakati, si undani wa kiufundi tu.

## Kanuni kuu

- Pakiti programu kama picha ndogo za kontena za madhumuni moja, zisizobadilika.
- Fanya usafi wa picha: picha za msingi za kiwango cha chini, matoleo yaliyobandikwa, zilizochanganuliwa kwa udhaifu, na zilizosainiwa.
- Sanifu programu ziwe zisizo na hali na zinazopanuka kwa mlalo popote iwezekanavyo, ukitoa hali nje.
- Chukulia mfano wa hali inayotakiwa wa jukwaa la uratibu kama chanzo cha ukweli na uache ujiponye.
- Tekeleza kutengwa na upendeleo mdogo kati ya wapangaji, mizigo, na nafasi za majina.
- Fuata kanuni za [twelve-factor](https://en.wikipedia.org/wiki/Twelve-Factor_App_methodology), mbinu ya kujenga programu zinazoweza kutupwa, zenye usanidi nje, zinazopanuka kwa mlalo, na uzipanue kwa uhalisia wa mifumo iliyosambazwa.
- Fanya gharama iwe wasiwasi wa uhandisi wa daraja la kwanza unaoonekana, si wazo la baadaye.
- Pendelea uondoaji unaohamishika, unaotegemea viwango ili kuhifadhi unyumbulifu wa kimkakati.

## Mapendekezo

### Fanya usafi mkali wa picha

Picha ya kontena ni kitengo chenu cha msingi cha uaminifu na usambazaji, kwa hiyo ichukulie hivyo. Anza kutoka picha za msingi za kiwango cha chini, zinazoaminika kupunguza uso wa shambulio. Bandika matoleo ya utegemezi na picha ya msingi kwa uwezo wa kuzalisha upya. Changanua kila picha kwa udhaifu unaojulikana kwenye bomba la ujenzi, na uzuie zile zenye matokeo muhimu. Sainia picha na uthibitishe saini wakati wa kusambaza, ili picha zilizoidhinishwa, zisizobadilishwa tu ziendeshe. Weka sajili ya ndani iliyochaguliwa ya picha za msingi zilizoimarishwa ambazo timu hujenga kutoka kwazo. Hilo huenea chaguo-msingi nzuri za usalama kiotomatiki.

### Tumia mifumo ya Kubernetes badala ya kuibuni upya

Kubernetes huzawadia timu zinazopokea mifumo yake iliyoimarika, na huadhibu timu zinazopambana na mfano wake. Tumia maelezo ya kutangaza kwa hali inayotakiwa. Ongeza vipimo vya afya ili jukwaa liweze kugundua na kubadilisha mifano isiyo na afya. Weka maombi na mipaka ya rasilimali ili kipanga ratiba kiweze kupakia mizigo kwa usalama. Tumia kupanuka kwa mlalo kiotomatiki kwa mahitaji yanayobadilika. Kwa mantiki ya uendeshaji inayopaswa kuendesha mfululizo, kama kusimamia hifadhidata, kuzungusha vyeti, au kupatanisha rasilimali maalumu, tumia mfumo wa opereta, unaosimba maarifa ya uendeshaji ya binadamu kuwa programu inayotazama hali na kutenda. Pinga hamu ya kujenga uratibu wa kipekee juu ya jukwaa. Pendelea miundo asili.

### Sanifu wapangaji wengi kwa makusudi

Timu nyingi zinaposhiriki kundi, kutengwa ni sharti la usalama na kutegemewa, si pambo. Tumia nafasi za majina kama mipaka ya upangaji. Tekeleza kiasi cha rasilimali ili hakuna mpangaji anayeweza kuwanyima wengine. Tumia sera za mtandao kubana trafiki kwa kinachoruhusiwa waziwazi. Tumia [udhibiti wa ufikiaji unaotegemea jukumu](https://en.wikipedia.org/wiki/Role-based_access_control) (RBAC) kubana kila timu inachoweza kufanya. Kwa mizigo yenye mahitaji makali zaidi ya kutengwa, fikiria makundi tofauti au sandbox imara zaidi. Amua mapema kama mfano wenu ni wapangaji wengi laini (timu za ndani zinazoaminika) au wapangaji wengi wagumu (mizigo isiyoaminiana), kwa sababu hizo mbili zinadai vidhibiti tofauti sana.

### Jenga asili ya wingu, twelve-factor na zaidi

Mbinu ya twelve-factor, kwa utegemezi wake wazi, usanidi kwenye mazingira, michakato isiyo na hali, uwezo wa kutupwa, na kadhalika, inabaki msingi bora kwa huduma zinazostawi kwenye jukwaa linalobadilika. Ipanue kwa uhalisia ulioongezwa wa mifumo iliyosambazwa. Sanifu kwa kushindwa kwa sehemu. Fanya shughuli ziwe na kutobadilika thamani na zinazoweza kujaribiwa tena. Fichua afya na telemetry. Chukulia uonekanaji kama kipengele kilichojengwa ndani badala ya nyongeza. Toa hali yote nje kwa huduma za data zinazosimamiwa, ili mifano ya programu ibaki inayoweza kutupwa na inayopanuka kwa mlalo.

### Panga mikakati ya wingu-nyingi, mseto, na enzi kwa vitendo

Uwezo wa kuhamishika una thamani, lakini uufuate kwa macho wazi. Sawazisha kwenye uondoaji unaohamishika kama kontena, Kubernetes, na API wazi, ili mizigo iweze kuhama inapohitajika. Lakini epuka mtego wa kukataa kila huduma inayosimamiwa, unaobadilisha tija halisi kwa uwezo wa kuhamishika dhahania. Kwa mahitaji ya mseto na enzi, sanifu ili mizigo na mabomba yaleyale yaweze kuendesha kwenye kanda iliyochaguliwa, kituo cha data cha faragha, au wingu la enzi linalotimiza kanuni za mamlaka na makazi ya data. Fanya mipaka ya enzi na makazi iwe wazi kwenye usanifu na sera.

### Fanya gharama ionekane kwa FinOps

Katika mazingira ya wingu yanayonyumbulika, gharama ni matokeo ya moja kwa moja ya maamuzi ya kihandisi, kwa hiyo wape wahandisi mwonekano na uwajibikaji. Weka lebo rasilimali kwa mgao wa gharama. Gawa matumizi kwa timu na huduma. Onyesha data ya gharama kando ya vipimo vya utendaji. Rekebisha ukubwa wa mizigo, tumia kupanuka kiotomatiki kulinganisha mahitaji, na rejesha rasilimali zisizotumika. Anzisha mazoea ya FinOps yanayoleta uhandisi, fedha, na bidhaa pamoja, ili matumizi ya wingu yawe wajibu wa pamoja, endelevu badala ya mshangao wa kila robo.

## Mabadilishano: faida na hasara

| Chaguo | Faida | Hasara | Inafaa zaidi |
|---|---|---|---|
| Kubernetes | Yenye nguvu, inayohamishika, mfumo mkubwa wa ikolojia | Ugumu mkali; mzigo wa uendeshaji | Huduma nyingi kwa ukubwa |
| Huduma ya kontena inayosimamiwa | Mzigo mdogo wa uendeshaji; mwanzo wa haraka | Kufungwa fulani; udhibiti mdogo | Timu zinazotaka urahisi |
| Kundi moja la pamoja | Matumizi bora ya rasilimali | Kutengwa ni ngumu zaidi; eneo la mlipuko | Wapangaji wa ndani wanaoaminika |
| Kundi kwa kila mpangaji | Kutengwa imara | Gharama na mzigo wa juu zaidi | Mizigo isiyoaminiana au inayodhibitiwa |
| Uwezo wa kuhamishika wa wingu-nyingi | Unyumbulifu; huepuka kufungwa | Huduma za kiwango cha chini kabisa cha pamoja | Kupunguza hatari ya kimkakati |
| Huduma zinazosimamiwa za wingu moja kwa kina | Tija ya juu zaidi | Utegemezi wa muuzaji | Timu zinazolenga kasi |

Mabadilishano ya jumla ni uwezo dhidi ya ugumu. Kubernetes na usanifu wa asili ya wingu hutoa unyumbulifu, ustahimilivu, na kasi. Lakini huweka mzigo mkubwa wa uendeshaji na wa kiakili ambao timu ndogo mara kwa mara huudharau. Vilevile, kufukuzia uwezo kamili wa kuhamishika wa [wingu-nyingi](https://en.wikipedia.org/wiki/Multicloud) hubadilisha tija kwa chaguo. Jibu sahihi linategemea ukubwa na hatari. Mashirika makubwa yenye timu nyingi na mahitaji makali ya utawala kwa kawaida huhalalisha uwekezaji. Juhudi ndogo mara nyingi zinahudumiwa vizuri zaidi na huduma zinazosimamiwa zinazoficha ugumu.

## Maswali ya kujadili na timu yako

1. **Mnasaini picha na kuthibitisha saini wakati wa kusambaza, na je, udhaifu muhimu unazuia ujenzi kweli?** Picha ni kitengo chenu cha uaminifu, kwa hiyo mnyororo wa ugavi unaoizunguka unastahili malango magumu, si maonyo. Amua kama picha zilizosainiwa, zilizothibitishwa tu ndizo zinaweza kuendesha, kama uchanganuzi unazuia matokeo muhimu au unayaandika tu, na nani anadumisha sajili iliyochaguliwa ya picha za msingi zilizoimarishwa ambazo timu hujenga kutoka kwazo. Kwa mizigo ya mashirika makubwa na serikali hili mara nyingi ni sharti la uzingatiaji, na pia ni ulinzi wenu bora dhidi ya utegemezi wenye sumu unaofika kwenye uzalishaji. Leta hali ya sasa: sehemu gani ya picha zinazoendesha inatoka msingi wenu ulioimarishwa, ngapi zina CVE muhimu zisizopachikwa, na kama picha yoyote isiyosainiwa inaweza kupangiwa ratiba sasa. Matokeo muhimu yasipozuia usambazaji, kichanganuzi chenu ni pambo.

2. **Maombi ya rasilimali, mipaka, na kiasi vinazuiaje mzigo mmoja kuwanyima majirani zake, bila kuacha uwezo ghali ukiwa bila kazi?** Kwenye kundi la pamoja, mzigo usio na mipaka unaweza kuanguka au kupunguza kasi ya kila kitu kinachouzunguka, na kiasi kilichowekwa kwa ukarimu mno kinapoteza faida za matumizi zinazohalalisha jukwaa. Amua chaguo-msingi zenye busara, nani anazirekebisha, na jinsi mnavyonasa mizigo isiyo na maombi yaliyowekwa kabisa. Kwa ukubwa hili ni kidhibiti cha kutegemewa na cha gharama, kwa sababu kurekebisha ukubwa ndipo akiba kubwa ya FinOps inapoishi. Leta data: matumizi ya sasa ya kundi, mara ngapi mizigo inaondolewa au kupunguzwa kasi, na nafasi za majina zipi hazina kiasi. Lengo ni kupakia kwa msongamano, usalama, kwa hiyo chukulia mipaka iliyokosekana kama kasoro ambayo jukwaa linaikataa.

3. **Hali gani inaruhusiwa kuishi ndani ya kontena, na kila kitu kingine kinaenda wapi?** Ustahimilivu wa asili ya wingu unategemea mifano inayoweza kutupwa ambayo jukwaa linaweza kupanga upya kwa utashi, na hilo linashikilia tu ikiwa hali muhimu inaishi kwenye huduma za data zinazosimamiwa badala ya diski ya ndani ya kontena. Amua kanuni waziwazi, kwa sababu hali iliyohifadhiwa kwenye kontena kwa bahati mbaya inakuwa upotevu wa data wakati ujao wa kupanga upya. Kwa timu zinazohamisha programu za zamani hili mara nyingi ndilo sehemu ngumu zaidi, kwa kuwa huduma za urithi zinadhania mfumo wa faili wa ndani thabiti. Leta orodha: huduma zipi zinaandika hali ya ndani, zipi zinategemea vikao vya kunata au mshikamano wa nodi, na ingehitaji nini kutoa kila moja nje. Hadi hali iwe ya nje, mna kontena zinazoonekana kunyumbulika lakini haziwezi kuhamishwa kweli.

4. **Timu nyingi zinaposhiriki kundi, mfano wenu wa kutengwa umechaguliwa kwa makusudi kuwa wapangaji wengi laini au wagumu, na vidhibiti vinalingana na chaguo hilo?** Nafasi za majina hutenganisha timu za ndani zinazoaminika, lakini haziwezi kuzuia mzigo wa uadui kikamilifu au ulioathirika, na kuchukulia upangaji laini kama mgumu ni tukio la usalama linalosubiri kutokea. Amua kwa kila mzigo kama wapangaji wanahitaji kugawana kwa haki tu au lazima wadhaniwe kutoaminiana, kisha ulinganishe vidhibiti: nafasi za majina, kiasi, sera za mtandao, na RBAC kwa kesi laini, makundi tofauti au sandbox imara zaidi kwa kesi ngumu. Kwa shirika kubwa uamuzi huu unaendesha gharama moja kwa moja, kwa sababu kundi kwa kila mpangaji ni ghali zaidi sana kuliko nafasi za majina za pamoja, kwa hiyo unataka kutumia bajeti ya kutengwa pale tu kielelezo cha tishio kinapodai. Leta orodha ya wapangaji: mizigo ipi inashiriki kundi leo, ipi inashughulikia trafiki inayodhibitiwa au ya nje, na wapi sera ya mtandao bado ni kuruhusu-kwa-chaguo-msingi. Katika mazingira ya mashirika makubwa na serikali, kuchanganya mizigo isiyoaminiana chini ya upangaji laini ndiyo hasa matokeo ambayo mkaguzi ataweka alama, kwa hiyo taja mpaka kabla yao.

5. **Mnalipia kiasi gani kwa uwezo wa kuhamishika wa wingu-nyingi, na je, mtautumia kweli?** Kusawazisha kwenye kontena, Kubernetes, na API wazi kunaweka mizigo ikihamishika, lakini kukataa kila huduma inayosimamiwa kuhifadhi chaguo hilo kunabadilisha tija halisi ya kila siku kwa uwezo wa kuhamishika ambao shirika huenda halitautumia kamwe. Amua wapi uwezo wa kuhamishika ni sharti halisi, kama wajibu wa enzi au wa kutoka mliosaini, dhidi ya wapi ni blanketi la faraja linalopunguza kasi ya kila timu. Mazingatio yanayoshindana ni kasi: huduma zinazosimamiwa kwa kina hutoa vipengele haraka zaidi, na usanifu wa kiwango cha chini kabisa cha pamoja ni kodi ya kudumu kwa kila timu. Leta ushahidi: huduma zipi zinazosimamiwa mmeziepuka na hilo liligharimu muda gani wa kihandisi, kama mmewahi kuhamisha mzigo kati ya watoa huduma, na mikataba yenu inawalazimisha nini kweli. Kwa wapokeaji wa serikali na wanaodhibitiwa, kanuni za makazi ya data na wingu la enzi zinaweza kufanya uwezo wa kuhamishika usijadiliwe, kwa hiyo sanifu ili maelezo na mabomba yaleyale yaendeshe kwenye kanda ya enzi na eneo la faragha, lakini kuwa mwaminifu kwamba hii ni gharama ya uzingatiaji, si bima ya bure.

6. **Kila timu inaweza kuona inachotumia, na je, yeyote anamiliki ankara kabla haijawa mshangao?** Kwenye jukwaa linalonyumbulika, gharama ni matokeo ya moja kwa moja ya maamuzi ya kihandisi, hata hivyo bila lebo za mgao wa gharama na dashibodi zinazoonekana matumizi hujilimbikiza kwenye bwawa la pamoja ambalo hakuna anayehisi kuwajibika hadi fedha zipandishe ngazi. Amua jinsi mnavyogawa gharama kwa timu na huduma, nani anaipitia, na kama wahandisi wanaona gharama kando ya vipimo vya utendaji au wanasikia tu mara moja kwa robo. Mvutano ni kati ya uwajibikaji na msuguano: sukuma gharama kwa nguvu mno na kila uamuzi unakuwa mazungumzo ya bajeti, ipuuze na mizigo isiyotumika, iliyokuzwa kupita kiasi inajilimbikiza kimyakimya. Leta namba: matumizi ya sasa kwa timu, uwezo kiasi gani unakaa bila kazi au umekuzwa kupita kiasi, na mzigo unaokimbia ungeonekana kwa haraka kiasi gani. Kwa bajeti za mashirika makubwa na serikali, matumizi ya wingu yasiyogawanywa ni kushindwa kwa utawala na hatari halisi ya kifedha, kwa hiyo simamisha mazoea ya FinOps yanayoweka uhandisi, fedha, na bidhaa kwenye mazungumzo yaleyale badala ya kupatanisha baadaye.

## Mtazamo wa sekta

**Kampuni changa.** Fikia huduma ya kontena inayosimamiwa badala ya kundi la Kubernetes linalojipangishwa: ukiwa na huduma kadhaa na bila mhandisi wa jukwaa, ndege za udhibiti ni usumbufu usioweza kuumudu. Pakiti picha ndogo kutoka msingi mdogo, bandika matoleo, ongeza uchanganuzi mmoja wa udhaifu kwenye ujenzi, na usukume hali yote kwenye hifadhidata inayosimamiwa ili mifano ibaki inayoweza kutupwa. Ruka nafasi za majina, maopereta, na uwezo wa kuhamishika wa wingu-nyingi hadi uwe na huduma na watu wa kuhalalisha.

**Biashara ndogo.** Bila mtaalamu maalumu wa jukwaa na bajeti finyu, egemea sana huduma zinazosimamiwa na uache mtoa huduma aendeshe uratibu ambao vinginevyo ungeuajiria. Chukulia misingi ya kontena kama sakafu yako ya usalama: picha za kiwango cha chini, kubandika matoleo, na uchanganuzi kwenye bomba vinatoa ulinzi mwingi kwa juhudi ndogo. Pendelea kununua jukwaa linaloungwa mkono kuliko kujenga, na uhifadhi uwezo wa kuhamishika wa kutosha, kontena za kawaida na API wazi, ili usinaswe bei au masharti yakibadilika.

**Biashara kubwa.** Kazi ni utawala wa jukwaa kuvuka timu nyingi: timu ya kati ya jukwaa inayotoa picha za msingi zilizoimarishwa, malango ya kusaini na kuchanganua, upangaji wa nafasi za majina na kiasi, sera ya mtandao, na RBAC, pamoja na lebo za mgao wa gharama na dashibodi ya FinOps. Sawazisha mkataba wa usambazaji ili mamia ya huduma ziendeshe kwa njia ileile, na usimamie usalama, upangaji, na gharama kati huku timu zikijihudumia usambazaji. Fadhili timu ya jukwaa ipasavyo, kwa sababu jukwaa lisilo na rasilimali za kutosha linakuwa kizuizi ambacho shirika zima linakisubiri.

**Serikali.** Enzi, makazi ya data, na uwajibikaji wa umma huumba usanifu. Endesha mizigo kwenye kontena za kawaida na Kubernetes ili mabomba yaleyale yaendeshe kwenye kanda ya enzi na eneo lililoidhinishwa la ndani ya majengo, na usimbe mipaka ya makazi na ufikiaji kama sera badala ya mkataba. Chora picha kutoka sajili ya ndani iliyoimarishwa, tumia upangaji mgumu kwa data nyeti zaidi, na uhifadhi uwezo wa kuhamishika unaokupa ustahimilivu na nguvu ya kujadiliana, kwa kuwa kanuni za ununuzi mara nyingi zinakataza kufungwa na muuzaji mmoja.

## Mifano

**Kampuni changa.** Kampuni changa ya watu sita inapakia huduma zake mbili kama picha ndogo za kontena zilizojengwa kutoka msingi mdogo, na kuziendesha kwenye huduma ya kontena inayosimamiwa badala ya kundi la Kubernetes lililopangishwa, kwa hiyo hakuna anayelazimika kutunza ndege za udhibiti. Wanabandika matoleo ya picha ya msingi na kuongeza uchanganuzi wa udhaifu kwenye ujenzi wao, lakini wanaruka kwa makusudi vipengele vizito vya uratibu hadi wawe na huduma zaidi ya chache. Hali inaishi kwenye Postgres inayosimamiwa, ikiweka kontena zikiwa za kutupwa na kuliruhusu jukwaa kuzianzisha upya au kuzipanua bila upotevu wowote wa data.

**Biashara kubwa.** Kampuni ya mawasiliano ya simu inaendesha mamia ya [huduma ndogo](https://en.wikipedia.org/wiki/Microservices) kwenye makundi ya Kubernetes ya pamoja. Timu ya jukwaa inatoa picha za msingi zilizoimarishwa, inatekeleza kusaini picha na malango ya udhaifu, na kutenganisha vitengo vya biashara kwenye nafasi za majina zenye kiasi, sera za mtandao, na RBAC. Lebo za mgao wa gharama na dashibodi ya FinOps zinagawa matumizi kwa kila mstari wa bidhaa, na kupanuka kiotomatiki kunarekebisha ukubwa wa uwezo kwa mahitaji. Timu za bidhaa husambaza mara kadhaa kwa siku kwenye jukwaa thabiti bila kusimamia seva. Kampuni inabaki na udhibiti wa kati juu ya usalama na gharama.

**Serikali.** Huduma ya taifa ya afya lazima iweke data ya raia ndani ya mipaka ya taifa na chini ya udhibiti wa kisheria wa taifa. Inaendesha mizigo yake kwenye kanda ya wingu la enzi kwa kontena za kawaida na Kubernetes, kwa hiyo mabomba na maelezo yaleyale yanaendesha pia kwenye mazingira ya ndani ya majengo yaliyoidhinishwa kwa data nyeti zaidi. Mipaka ya makazi ya data na ufikiaji imesimbwa kama sera, picha zinachorwa kutoka sajili ya ndani iliyoimarishwa, na upangaji mgumu unatenga mizigo nyeti. Uwezo wa kuhamishika kuvuka kanda ya enzi na eneo la faragha unaipa huduma ustahimilivu na nguvu ya kujadiliana bila kutoa uzingatiaji.

## Kesi ya biashara: sababu, ROI, na TCO

ROI ya kontena na uratibu inatokana na matumizi ya juu ya rasilimali, usambazaji wa haraka na wa kutegemewa zaidi, kupanuka kunakolingana na matumizi kwa mahitaji, na ustahimilivu ulioboreshwa kupitia kujiponya. Kusawazisha kwenye jukwaa la pamoja kunapunguza juhudi iliyorudiwa kuvuka timu na kuharakisha kuanza, kwa sababu kila huduma inafuata mkataba ule ule wa usambazaji na uendeshaji.

Uchambuzi wa TCO lazima uwe mwaminifu kuhusu mzigo wa uendeshaji. Gharama za kupokea zinajumuisha wafanyakazi wa uhandisi wa jukwaa, mafunzo, zana za usalama kwa picha na makundi, na juhudi endelevu ya kuendesha jukwaa lenyewe. Gharama ya kutopokea inajumuisha usambazaji wa kipekee usio thabiti kuvuka timu, matumizi duni ya miundombinu ghali, kupanuka kwa mkono dhaifu, na ugumu wa kutimiza mahitaji ya ustahimilivu na enzi. Kwa uongozi, kesi inasimama juu ya ukubwa. Chini ya idadi fulani ya huduma ugumu unaweza kutolipa, na huduma inayosimamiwa ni busara zaidi. Lakini kwa ukubwa wa mashirika makubwa na serikali, jukwaa la asili ya wingu lililotawaliwa kwa kawaida ndilo msingi wa gharama nafuu zaidi na wenye ustahimilivu zaidi, mradi mnafadhili timu ya jukwaa kuliendesha ipasavyo.

## Mifumo mibaya na mitego

- **Picha nene, zisizochanganuliwa.** Picha zilizovimba zilizojengwa kutoka misingi isiyoaminika hubeba udhaifu usio wa lazima na kupunguza kasi ya kila kitu.
- **Kubernetes kwa kila kitu.** Kupokea kiratibu changamano kwa huduma chache rahisi kunanunua ugumu bila faida.
- **Kupuuza mipaka ya rasilimali.** Bila maombi na mipaka, mzigo mmoja unaweza kuwanyima au kuangusha majirani zake.
- **Upangaji laini kwa mizigo ya uadui.** Kutegemea nafasi za majina peke yake kutenganisha wapangaji wasioaminiana ni tukio la usalama linalosubiri kutokea.
- **Kontena zenye hali kwa bahati mbaya.** Kuhifadhi hali muhimu ndani ya kontena zinazoweza kutupwa husababisha upotevu wa data wakati wa kupanga upya.
- **Upofu wa gharama.** Kuchukulia matumizi ya wingu kama gharama isiyobadilika badala ya matokeo ya uhandisi husababisha ankara zinazokimbia.
- **Maigizo ya uwezo wa kuhamishika.** Kukataa huduma zote zinazosimamiwa kuhifadhi uwezo wa kuhamishika ambao shirika halitautumia kamwe.

## Kielelezo cha ukomavu

**Ngazi ya 1: Kuanzisha.** Kontena zinatumika papo hapo, kama kabisa. Picha zinajengwa kwa mkono na hazichanganuliwi, usambazaji ni wa mkono na wa kuitikia, na hakuna jukwaa la pamoja, mwonekano wa gharama, wala mfano wa kutengwa.

**Ngazi ya 2: Kuendeleza.** Timu zinapakia programu kwenye kontena na kupokea kiratibu, lakini mazoea yanatofautiana kati ya vikundi. Uchanganuzi wa picha, mipaka ya rasilimali, na kusaini hazina uthabiti, na gharama na upangaji wa wapangaji wengi haujatawaliwa kimfumo.

**Ngazi ya 3: Kusawazisha.** Jukwaa sanifu limeandikwa na kutekelezwa kuvuka shirika: picha za msingi zilizoimarishwa, malango ya kusaini na kuchanganua, upangaji wa nafasi za majina wenye kiasi na sera ya mtandao, RBAC, na mgao wa gharama. Mifumo ya asili ya wingu na twelve-factor ndiyo kawaida inayotarajiwa badala ya chaguo la ndani.

**Ngazi ya 4: Kusimamia.** Jukwaa linapimwa na kudhibitiwa dhidi ya vipimo vya msingi. Mnafuatilia matumizi ya kundi, sehemu ya picha zinazoendesha zilizojengwa kutoka msingi ulioimarishwa, udhaifu muhimu usiopachikwa, mzunguko wa usambazaji na kiwango cha kushindwa kwa mabadiliko, viwango vya kuondolewa na kupunguzwa kasi, na gharama kwa kila timu na huduma dhidi ya bajeti. Malango yanatekelezwa kwa ushahidi huu: mipaka ya rasilimali iliyokosekana na picha zisizosainiwa zinakataliwa kiotomatiki, na kuteleza kutoka kiwango kunachochea hatua badala ya onyo.

**Ngazi ya 5: Kuratibu.** Jukwaa ni la kujihudumia na kujiponya, limeunganishwa kuvuka shirika na linajirekebisha. FinOps hurekebisha ukubwa na kurejesha uwezo mfululizo, usanifu unaohamishika unaunga mkono mahitaji ya mseto na enzi, na jukwaa linaboreshwa mfululizo kutokana na matumizi yaliyopimwa, likistaafisha na kubadilisha vijenzi mizigo, gharama, na picha ya hatari inapohama.

## Mawazo ya kujadili

- Kwa ukubwa gani kupokea Kubernetes kunaacha kuwa ugumu kwa ajili yake na kuanza kulipa?
- Mpaka sahihi uko wapi kati ya upangaji laini na mgumu kwa mizigo yenu?
- Mnapaswa kuwekeza kiasi gani kwenye uwezo wa kuhamishika wa wingu-nyingi dhidi ya tija ya huduma zinazosimamiwa kwa kina?
- Mnawapaje wahandisi uwajibikaji halisi wa gharama bila kugeuza kila uamuzi kuwa mazungumzo ya bajeti?
- Mfano wenu wa utawala kwa picha za msingi ni upi, na nani anadumisha sajili iliyoimarishwa?
- Mahitaji ya enzi na makazi ya data yanaumbaje usanifu wa jukwaa lenu?

## Mambo muhimu ya kukumbuka

- Kontena husawazisha kufunga na wakati wa kuendesha; uratibu husawazisha uendeshaji kwa ukubwa.
- Usafi wa picha, yaani picha ndogo, zilizobandikwa, zilizochanganuliwa, zilizosainiwa, ni usalama wa msingi.
- Tumia mifumo asili ya Kubernetes na maopereta badala ya kujenga uratibu wa kipekee.
- Chagua mfano wa upangaji wa wapangaji wengi kwa makusudi kulingana na jinsi mizigo inavyoaminiana.
- Fuata twelve-factor na uipanue kwa uhalisia wa mifumo iliyosambazwa kama kushindwa kwa sehemu na uonekanaji.
- Chukulia gharama kama matokeo ya uhandisi na uisimamie mfululizo kupitia FinOps.

## Marejeo na usomaji zaidi

- Adam Wiggins, *The Twelve-Factor App* (methodology).
- Brendan Burns, Joe Beda, and Kelsey Hightower, *Kubernetes Up & Running*.
- Bilgin Ibryam and Roland Huß, *Kubernetes Patterns*.
- Cornelia Davis, *Cloud Native Patterns*.
- J.R. Storment and Mike Fuller, *Cloud FinOps*.
- Liz Rice, *Container Security*.
- Cloud Native Computing Foundation (CNCF), cloud-native definition and landscape.
