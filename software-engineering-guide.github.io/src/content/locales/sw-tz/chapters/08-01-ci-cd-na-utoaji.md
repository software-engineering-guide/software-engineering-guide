# 8.1 CI/CD na utoaji

## Muhtasari na msukumo

[Ujumuishaji endelevu](https://en.wikipedia.org/wiki/Continuous_integration) na [utoaji endelevu](https://en.wikipedia.org/wiki/Continuous_delivery) (CI/CD) ni tishu ya kuunganisha kati ya kuandika msimbo na kuuweka mbele ya watumiaji kwa usalama. Ujumuishaji endelevu unamaanisha kila badiliko linaunganishwa mara kwa mara kwenye mstari mkuu wa pamoja, kisha kujengwa na kujaribiwa kiotomatiki, ili matatizo ya ujumuishaji yajitokeze ndani ya dakika badala ya mwishoni mwa mzunguko mrefu wa toleo. Utoaji endelevu unamaanisha kila badiliko linalopita bomba linawekwa katika hali inayoweza kusambazwa, ili kutoa kwenye uzalishaji kuwe uamuzi wa biashara badala ya mbio za kihandisi. [Usambazaji endelevu](https://en.wikipedia.org/wiki/Continuous_deployment) unaenda hatua moja zaidi na kutoa kila badiliko linalopita kiotomatiki, bila lango la binadamu.

Kwa timu kubwa, tofauti hizi ni muhimu sana. Mamia ya wahandisi wanapoweka commit kwenye mifumo inayoingiliana, gharama ya ujumuishaji wa mkono na majaribio ya mkono hukua bila mstari. Bomba la pamoja, la kiotomatiki ndiyo njia pekee ya kiutendaji ya kuwapa wachangiaji wengi maoni ya haraka, ya kuaminika na kuzuia badiliko la timu moja lisivunje kimyakimya la nyingine. Bomba linakuwa chanzo kimoja cha ukweli kuhusu kama programu ina afya, na linatekeleza uthabiti ambao hakuna kiasi cha nyaraka wala nia njema kinaweza kuuhakikishia kwa ukubwa.

Mazingira ya mashirika makubwa na serikali huongeza kipimo kimoja zaidi: uwezo wa kukaguliwa na udhibiti wa mabadiliko. Wadhibiti, maafisa wa usalama, na wakaguzi wanahitaji ushahidi kwamba mabadiliko yalipitiwa, kujaribiwa, na kuidhinishwa, na kwamba mabaki yanayoendesha kwenye uzalishaji ndiyo hasa yaliyojengwa na kuthibitishwa. Bomba la CI/CD lililosanifiwa vizuri hugeuza wajibu huu wa uzingatiaji kutoka mzigo wa makaratasi hadi zao la kiotomatiki la mtiririko wa kawaida wa kihandisi. Likifanywa vizuri, utoaji unakuwa wa haraka zaidi na salama zaidi kwa wakati mmoja, ambalo ndilo matokeo yanayojalisha zaidi kwa uongozi.

*Angalia pia:* sura ya 8.4 (uhandisi wa jukwaa na uzoefu wa msanidi), sura ya 8.5 (uotomatishaji wa majaribio na mchakato), na sura ya 7.4 (uchanganuzi wa bidhaa na majaribio) kwa mazoea ya [bendera za vipengele](https://en.wikipedia.org/wiki/Feature_toggle) (swichi za wakati wa kuendesha zinazofichua utendaji kwa watumiaji bila kusambaza upya) na majaribio ambayo utoaji wa hatua kwa hatua (kutoa badiliko polepole huku ukifuatilia kiotomatiki vipimo vyake vya afya) unawezesha.

## Kanuni kuu

- Unganisha mabadiliko madogo mara kwa mara; matawi ya muda mrefu ni adui wa ujumuishaji endelevu.
- Jenga mabaki mara moja na upandishe mabaki yaleyale kupitia kila mazingira.
- Fanya bomba kuwa lango lenye mamlaka: likiwa kijani, badiliko linaweza kusafirishwa; likiwa nyekundu, kazi inasimama hadi irekebishwe.
- Boresha bila kuchoka kwa maoni ya haraka ili wasanidi wabaki kwenye mtiririko na kasoro zinaswe muktadha ukiwa bado mpya.
- Otomatisha kila kitu kinachojirudia, ikijumuisha majaribio, uchanganuzi wa usalama, kutayarisha, na kusambaza.
- Chukulia fasili za bomba kama msimbo wenye udhibiti wa matoleo unaopitiwa, si usanidi wa kiweko cha kubofya.
- Sanifu kwa matoleo salama, yanayorekebishika ili usambazaji wowote utenduliwe haraka.
- Tenganisha kusambaza (kusakinisha msimbo) na kutoa (kuufichua kwa watumiaji) kwa kutumia bendera za vipengele.

## Mapendekezo

### Sanifu bomba kama mfululizo wa malango ya ubora

Panga bomba katika hatua zinazoendelea kutoka nafuu na za haraka hadi ghali na kamili: kukusanya na majaribio ya kitengo kwanza, kisha majaribio ya ujumuishaji, uchanganuzi wa usalama na leseni, na hatimaye usambazaji kwenye maandalizi na uzalishaji. Kila hatua ni lango ambalo badiliko lazima lipite. Panga malango ili ukaguzi wa haraka zaidi, unaoelekea kushindwa zaidi uendeshe kwanza, jambo linalowapa wasanidi maoni kwa muda mfupi iwezekanavyo. Weka mzunguko wa maoni wa hatua ya commit chini ya dakika kumi popote unapoweza. Zaidi ya hapo, wasanidi hubadilisha muktadha na tija inashuka.

### Jenga mara moja, pandisha kila mahali

Zalisha mabaki moja yasiyobadilika kwenye hatua ya ujenzi na upandishe mabaki hayohayo kupitia majaribio, maandalizi, na uzalishaji. Usijenge upya kwa kila mazingira, kwa sababu kujenga upya kunaweza kuleta tofauti kimyakimya. Usanidi unaotofautiana kwa mazingira unapaswa kuingizwa wakati wa kusambaza, si kuokwa ndani ya ujenzi tofauti. Mazoea haya pia ndiyo yanayokuruhusu kumwambia mkaguzi, kwa uhakika, kwamba binary iliyoko kwenye uzalishaji ndiyo ile iliyopita kila lango.

### Fanya bomba kuwa nukta ya kutekeleza sera

Simba ukaguzi unaohitajika (idhini ya mapitio ya msimbo, vizingiti vya ufikiaji wa majaribio, matokeo ya uchanganuzi wa usalama, commit zilizosainiwa) moja kwa moja kwenye bomba na kanuni za ulinzi wa matawi. Sera ya mkono inayoishi kwenye wiki mara kwa mara hupitwa chini ya shinikizo la tarehe ya mwisho. Sera iliyosimbwa kwenye bomba inatumika kwa usawa na kiotomatiki kwa kila badiliko.

### Weka mstari mkuu ukiwa tayari kutolewa wakati wote

Tumia uendelezaji unaotegemea shina, unaounganisha kazi yote kwenye tawi moja la pamoja lenye matawi ya muda mrefu machache au hakuna, au tumia matawi ya vipengele ya muda mfupi, na uegemee bendera za vipengele kuficha kazi isiyokamilika badala ya matawi ya muda mrefu. Hii inaweka migongano ya muunganisho midogo na inaweka mstari mkuu katika hali inayoweza kusambazwa kila wakati, ambalo ni sharti la utoaji endelevu wa kweli.

### Chagua mikakati ya usambazaji kwa makusudi

Linganisha mkakati wa usambazaji na hatari na eneo la mlipuko la huduma:

- Usambazaji wa **kuviringisha** hubadilisha mifano hatua kwa hatua na ni chaguo-msingi la busara kwa huduma zisizo na hali.
- **[Buluu-kijani](https://en.wikipedia.org/wiki/Blue-green_deployment)** hudumisha mazingira mawili yanayofanana na kubadilisha trafiki yote mara moja, ikitoa njia ya papo hapo ya kurudisha nyuma.
- Matoleo ya **canary** huelekeza asilimia ndogo ya trafiki kwa toleo jipya, hutazama vipimo vya afya, na hupanuka tu ishara zikiwa nzuri.
- **Bendera za vipengele** hutenganisha kutoa na kusambaza, zikikuruhusu kuwezesha utendaji kwa watumiaji au vikundi mahususi bila kusambaza upya.

### Pokea utoaji wa hatua kwa hatua na kurudisha nyuma kiotomatiki

Utoaji wa hatua kwa hatua unachanganya matoleo ya canary na uchambuzi wa kiotomatiki wa vipimo kama kiwango cha makosa, ucheleweshaji, na kujaa. Fafanua vigezo vya afya vya lengo mapema, kisha uache mfumo upandishe au urudishe nyuma kiotomatiki kulingana na ishara hizo. Kurudisha nyuma kiotomatiki huondoa kusita kwa binadamu kunakogeuza tukio dogo kuwa kubwa.

### Toa usimamizi wa matoleo na udhibiti wa mabadiliko kwa mazingira yanayodhibitiwa

Katika mazingira yanayodhibitiwa, weka rekodi nyepesi lakini halisi ya usimamizi wa mabadiliko. Nasa kiotomatiki nani aliidhinisha kila badiliko, majaribio gani yaliendeshwa, na mabaki gani yalisambazwa. Tumia michakato ya ushauri wa mabadiliko kwa mabadiliko ya hatari kubwa kweli, lakini yahifadhi kwa kesi hizo. Kupitisha kila badiliko la kawaida kwenye bodi ya kila wiki kunaharibu thamani ya uotomatishaji. Lenga badala yake aina za mabadiliko za kawaida, zilizoidhinishwa mapema zinazotiririka kupitia bomba bila sherehe.

## Mabadilishano: faida na hasara

| Mbinu | Faida | Hasara | Inafaa zaidi |
|---|---|---|---|
| Utoaji endelevu (lango la toleo la mkono) | Biashara inadhibiti wakati; imara kwa madirisha ya matoleo yanayodhibitiwa | Inahitaji nidhamu kuweka mstari mkuu ukiwa tayari kusafirishwa | Mashirika yenye madirisha ya mabadiliko |
| Usambazaji endelevu (kiotomatiki kabisa) | Maoni ya haraka zaidi; makundi madogo zaidi | Inadai majaribio na uonekanaji uliokomaa | Timu za uaminifu wa juu, mzunguko wa juu |
| Buluu-kijani | Kurudisha nyuma papo hapo; mfano rahisi wa kiakili | Inazidisha gharama ya mazingira mara mbili wakati wa kubadilisha | Huduma muhimu zinazohitaji kurudi nyuma haraka |
| Canary + utoaji wa hatua kwa hatua | Hupunguza eneo la mlipuko; inayoendeshwa na data | Changamano kujenga; inahitaji vipimo vizuri | Mifumo mikubwa inayomkabili mtumiaji |
| Bendera za vipengele | Hutenganisha kusambaza na kutoa | Deni la bendera zisiposafishwa | Timu zinazosafirisha kazi isiyokamilika kwa usalama |

Mabadilishano ya msingi ni kasi dhidi ya udhibiti, lakini hiyo mara nyingi ni chaguo la uongo. Uotomatishaji uliokomaa hutoa yote mawili: matoleo ni ya haraka zaidi kwa sababu ni madogo, na salama zaidi kwa sababu kila moja linathibitishwa na kurekebishika. Gharama halisi ni uwekezaji wa awali katika ufikiaji wa majaribio, uonekanaji, na uhandisi wa bomba, pamoja na nidhamu endelevu ya kuviweka vyema. Mashirika yanayobana uwekezaji huo hupata kasi bila usalama, ambalo ni baya kuliko mchakato wa mkono wa polepole.

## Maswali ya kujadili na timu yako

1. **Lengo lenu la muda wa maoni ya hatua ya commit ni lipi, na nini kinakatwa mfululizo unapozidi dakika kumi?** Hatua ya commit ya polepole huua ujumuishaji endelevu kimyakimya, kwa sababu wasanidi huacha kusubiri kijani na kuanza kukusanya mabadiliko. Amua namba sasa (sura hii inahoji chini ya dakika kumi) na amua utaratibu wa kuishikilia: wafanyakazi sambamba, piramidi kali ya majaribio, na kuhamisha ukaguzi wa ujumuishaji wa polepole kwenye hatua ya baadaye. Kwa ukubwa wa mashirika hili ni uamuzi wa jukwaa, kwa kuwa mamia ya wahandisi wanashiriki bomba lilelile na kila dakika ya ziada inazidishwa kuvuka kila commit. Leta data halisi kwenye mkutano: muda wa sasa wa p50 na p95 wa bomba, majaribio kumi ya polepole zaidi, na mara ngapi watu wanaendesha tena badala ya kusubiri. Kama huwezi kutaja lengo na kulitetea kwa namba, bomba lenu linateleza kuelekea mchakato wa kundi uliovaa vazi la CI.

2. **Huduma kila moja inatumia mkakati gani wa usambazaji, na nani anawajibika kwa chaguo hilo?** Kuviringisha, buluu-kijani, na canary havibadilishani: vinabadilishana gharama, kasi ya kurudisha nyuma, na ugumu tofauti, na chaguo sahihi linategemea eneo la mlipuko la huduma. Buluu-kijani inanunua kurudisha nyuma papo hapo kwa bei ya mazingira yaliyozidishwa mara mbili wakati wa kubadilisha, jambo linalostahili kwa mfumo wa malipo na upotevu kwa dashibodi ya ndani. Canary inapunguza mfiduo lakini inadai vipimo vizuri vya afya na uhandisi zaidi wa bomba. Kwa eneo kubwa au linalodhibitiwa, kuiachia kila timu kwa mazoea yake huzalisha kutokuwa na uthabiti kunakojitokeza wakati wa tukio, kwa hiyo kubaliana chaguo-msingi kwa ngazi ya huduma na urekodi uamuzi. Leta orodha yenu ya huduma na uweke lebo kila huduma na mkakati wake, njia yake ya kurudisha nyuma, na mtu anayemiliki uamuzi huo.

3. **Mnathibitishaje mabaki yaliyoko kwenye uzalishaji ndiyo hasa yaliyopita kila lango?** Jenga mara moja na upandishe mabaki yaleyale ni mchezo mzima kwa uwezo wa kukaguliwa, na unavunjika mara mtu anapojenga upya kwa kila mazingira au kuweka kiraka kwenye kisanduku kinachoendesha. Katika mazingira ya mashirika makubwa na serikali mkaguzi atawaomba kufuatilia binary inayoendesha hadi commit yake, mapitio yake, na idhini zake, na mnataka jibu hilo lichukue sekunde, si wiki. Amua jinsi mnavyotekeleza: mabaki yasiyobadilika, picha zilizosainiwa, uthibitishaji wa saini wakati wa kusambaza, na usanidi unaoingizwa wakati wa kusambaza badala ya kuokwa ndani ya ujenzi tofauti. Leta mapengo ya sasa mezani, kama hatua yoyote inayojenga upya, njia yoyote ya hotfix ya mkono, na mahali popote usanidi unapogawanya mabaki. Jibu linaamua kama ushahidi wenu wa uzingatiaji ni zao la bomba au mbio za mkono kabla ya kila ukaguzi.

4. **Mstari mkuu unapogeuka mwekundu, nini kinasimama kweli, na mnashughulikiaje majaribio yasiyo thabiti?** Bomba ni lango lenye mamlaka tu ikiwa ujenzi mwekundu unasimamisha kazi kweli, hata hivyo mashirika mengi huvumilia kimyakimya mstari mkuu uliovunjika na rundo la kushindwa kwa mara kwa mara, jambo linalowazoeza wasanidi kuendesha tena hadi kijani na kusafirisha juu ya kushindwa. Kwa timu kubwa kuoza huku kunajilimbikiza, kwa sababu jaribio lisilo thabiti lililopuuzwa la timu moja linakuwa kisingizio cha kila mtu kupita lango, na uaminifu kwenye bomba ni nafuu zaidi kuuweka kuliko kuujenga upya. Pima mivuto inayoshindana: kanuni kali ya kusimamisha mstari inalinda ubora lakini inaweza kuzuia mamia ya wahandisi kwa commit moja mbaya, wakati sera legevu inahifadhi matokeo na kumomonyoa lango. Leta ushahidi kwenye mjadala: muda wenu wa sasa wa mstari mkuu mwekundu, idadi ya majaribio yaliyowekwa karantini au yasiyo thabiti, kiwango cha kuendesha tena, na mara ngapi mabadiliko yanaunganishwa juu ya ukaguzi unaoshindwa. Katika mazingira ya mashirika makubwa na serikali, taja nani anamiliki upangaji wa majaribio yasiyo thabiti na nani ana mamlaka ya kuganda miunganisho, kwa sababu lango ambalo hakuna anayewajibika kulitekeleza ni moja ambalo wakaguzi watagundua limepitwa mara kwa mara.

5. **Mzunguko wenu wa maisha wa bendera za vipengele ni upi, na nani anawajibika kuzistaafisha?** Bendera ndizo zinazokuruhusu kutenganisha kusambaza na kutoa na kuficha kazi isiyokamilika, lakini kila bendera ni tawi kwenye msimbo wako ambalo halisafishwi lenyewe, na bendera zisizosimamiwa hujilimbikiza kuwa ugumu wa masharti ambao hakuna anayethubutu kuugusa. Katika eneo kubwa deni hili ni hatari, kwa sababu bendera iliyochakaa inaweza kuweka lango kimyakimya kwa marekebisho ya usalama au kupindua njia za msimbo ambazo hazijajaribiwa kuingia kwenye uzalishaji, na aliyeiunda mara nyingi ameshahama. Sawazisha mvutano: bendera zilikununulia utoaji salama, wa hatua kwa hatua, kwa hiyo lengo si bendera chache bali mzunguko wa maisha wenye nidhamu wenye mmiliki, matarajio ya kuisha, na zana inayofichua zilizochakaa. Leta orodha ya sasa kwenye mkutano: bendera ngapi ziko hai, kongwe zaidi ina umri gani, zipi hazina mmiliki, na kama bendera yoyote ya muda mrefu sasa inafanya kazi kama usanidi wa kudumu unaostahili kuwa kwingine. Kwa mazingira yanayodhibitiwa, ongeza nani anaweza kubadilisha bendera kwenye uzalishaji na kama badiliko hilo linaandikwa kwa ukali ule ule kama usambazaji, kwa sababu kugeuza bendera ni toleo hata bomba likiwa halijaendesha kamwe.

6. **Mpaka uko wapi kati ya utoaji endelevu wenye lango la binadamu na usambazaji endelevu kamili, na nani anaweka vizingiti vya kurudisha nyuma?** Utoaji endelevu unamweka mtu akidhibiti wakati wa toleo, jambo linalofaa madirisha ya kisheria ya mabadiliko na mifumo ya eneo kubwa la mlipuko, wakati usambazaji endelevu unasafirisha kila badiliko linalopita kiotomatiki na kudai majaribio yaliyokomaa, uonekanaji, na kurudisha nyuma kiotomatiki ili uwe salama. Kwa shirika kubwa au linalodhibitiwa jibu mara chache ni sare: tovuti yenu ya masoko inaweza kusambaza mfululizo wakati kiini chenu cha malipo kinabaki na lango la binadamu lililoandikwa, na kuchora mstari huo kwa ngazi ya huduma kunazuia msuguano usio wa lazima na uotomatishaji wa pupa. Mazingatio yanayoshindana ni kasi na ukubwa wa kundi dhidi ya udhibiti na uwezo wa kukaguliwa, pamoja na gharama ya uhandisi ya vipimo vya afya ambavyo kurudisha nyuma kiotomatiki kunahitaji. Leta ushahidi: kiwango cha kushindwa kwa mabadiliko kwa kila huduma, muda wa wastani wa kupona, mzunguko wa sasa wa matoleo, na ishara za lengo (kiwango cha makosa, ucheleweshaji, kujaa) ambazo mngeziamini kupandisha au kurudisha nyuma bila binadamu. Katika mazingira ya serikali na mashirika, funga kila ngazi na nani anamiliki vizingiti vya kurudisha nyuma na nani anaidhinisha hatua yoyote kutoka toleo lenye lango hadi uotomatishaji kamili, ili uamuzi uwe wa makusudi badala ya kuteleza.

## Mtazamo wa sekta

**Kampuni changa.** Egemea CI/CD inayosimamiwa tangu siku ya kwanza: mkimbiaji unaopangishwa, bomba moja, picha moja isiyobadilika, na usambazaji wa kiotomatiki kwenye maandalizi wakati wa muunganisho. Usijenge miundombinu ya bomba ambayo kisha unapaswa kuidumisha. Bendera za vipengele zinawaruhusu wahandisi wawili au watatu kuunganisha kazi ya nusu-kamili kwa usalama na kusafirisha mara kadhaa kwa siku, na usambazaji wa uzalishaji kwa mbofyo mmoja pamoja na kuzima bendera kwa haraka ndio udhibiti wote wa mabadiliko unaohitaji hadi ukubwa ulazimishe zaidi.

**Biashara ndogo.** Bila jukwaa maalumu au mhandisi wa matoleo, pendelea bomba ambalo mwenyeji wako wa chanzo anakupa (Actions zilizojengwa ndani au sawa) na mkakati wake wa usambazaji wa chaguo-msingi kuliko chochote cha kipekee. Weka uchaguzi wa kununua-dhidi-ya-kujenga kwa uaminifu: bomba linalosimamiwa na jukwaa la upangishaji lenye kurudisha nyuma lililojengwa ndani linagharimu kidogo kuliko saa za wahandisi ambazo usanidi wa kipekee unatumia. Hifadhi mambo muhimu, yaani jenga mara moja, pandisha mabaki yaleyale, na kurudisha rahisi, na uruke mitambo ya utoaji wa hatua kwa hatua hadi kiasi kihalalishe.

**Biashara kubwa.** Tatizo la msingi ni uthabiti kuvuka timu nyingi: sawazisha kiolezo cha pamoja cha bomba kinachotekeleza mapitio, uchanganuzi, mabaki yaliyosainiwa yasiyobadilika, na mikakati ya usambazaji kwa ngazi, ili ubora usitofautiane timu hadi timu. Chukulia fasili za bomba kama msimbo uliopitiwa, nasa ushahidi wa udhibiti wa mabadiliko kiotomatiki, na usimamie bendera za vipengele na vizingiti vya kurudisha nyuma kama mali zilizotawaliwa badala ya mazoea ya faragha ya kila timu. Faida ni utoaji wa haraka zaidi na ushahidi wa ukaguzi unaozalishwa kama zao la pembeni badala ya mbio za robo mwaka.

**Serikali.** Kanuni za ununuzi, madirisha ya kisheria ya mabadiliko, na uwajibikaji wa umma huumba bomba. Pendelea utoaji endelevu wenye lango la toleo la binadamu lililoandikwa kuliko uotomatishaji kamili kwa mifumo yenye matokeo, ainisha kazi ya kawaida kama mabadiliko ya kawaida yaliyoidhinishwa mapema, na uhifadhi njia ya kurudisha nyuma papo hapo (buluu-kijani au canary ya kiotomatiki) kwa huduma raia wanazozitegemea wakati wa madirisha finyu ya mwaka. Hakikisha bomba linarekodi nani aliidhinisha kila badiliko, majaribio gani yaliendeshwa, na mabaki gani yalisambazwa, ili wajibu wa uwazi na ukaguzi utimizwe na mtiririko wa kawaida badala ya makaratasi ya mkono.

## Mifano

**Kampuni changa.** Kampuni changa ya SaaS ya watu wanne inaweka bomba moja la GitHub Actions linaloendesha majaribio ya kitengo, kujenga picha moja ya Docker, na kusambaza picha hiyo hiyo kwenye maandalizi kiotomatiki kwa kila muunganisho kwenye main. Usambazaji wa uzalishaji ni mbofyo mmoja, na waanzilishi wanaegemea bendera za vipengele ili waunganishe kazi ya nusu-kamili nyuma ya bendera badala ya kuweka tawi hai kwa wiki. Toleo baya linapopenya, wanazima bendera ndani ya sekunde na kurekebisha kwa utulivu, jambo linalowaweka timu yao ndogo ikisafirisha mara kadhaa kwa siku bila mtu maalumu wa operesheni.

**Biashara kubwa.** Benki ya kimataifa inaunganisha kazi nyingi za Jenkins za timu mahususi kuwa kiolezo sanifu cha bomba ambacho kila timu ya bidhaa inarithi. Kiolezo kinatekeleza uchambuzi tuli, uchanganuzi wa utegemezi, na mabaki yaliyosainiwa, yasiyobadilika, na kinasambaza kupitia canary yenye kurudisha nyuma kiotomatiki kulingana na vizingiti vya kiwango cha makosa na ucheleweshaji. Kwa kuwa mabaki yaleyale yanapandishwa kutoka majaribio hadi uzalishaji na kila lango linaandikwa, wakaguzi wa benki wanaweza kufuatilia binary yoyote ya uzalishaji hadi commit, mapitio, na idhini yake ndani ya sekunde, wakichukua nafasi ya zoezi la mkono la ukusanyaji wa ushahidi la kila robo.

**Serikali.** Mamlaka ya taifa ya kodi inayoboresha mfumo wa kuwasilisha inapokea utoaji endelevu wenye lango la toleo la binadamu lililo wazi, ili iweze kuheshimu madirisha ya kisheria ya mabadiliko wakati wa msimu wa kuwasilisha. Mabadiliko ya kawaida yanaainishwa kama mabadiliko ya kawaida yaliyoidhinishwa mapema yanayotiririka kiotomatiki hadi maandalizi. Toleo la uzalishaji linahitaji idhini moja iliyoandikwa ambayo bomba linarekodi. Usambazaji wa buluu-kijani unaipa mamlaka njia ya papo hapo ya kurudisha nyuma kasoro ikifika kwenye uzalishaji, jambo muhimu mamilioni ya raia wanapotegemea huduma wakati wa dirisha finyu la mwaka.

## Kesi ya biashara: sababu, ROI, na TCO

Faida ya uwekezaji wa CI/CD inaonekana kama muda mfupi wa kuongoza wa mabadiliko, kiwango cha chini cha kushindwa kwa mabadiliko, na kupona haraka matukio yanapotokea: vipimo ambavyo utafiti mara kwa mara unavifunga na utendaji wa utoaji na matokeo ya kishirika. Matoleo ya haraka, madogo hupunguza mzigo wa uratibu unaotumia uwezo wa kihandisi kwa ukubwa, na uthibitishaji wa kiotomatiki hupunguza kazi ya gharama, inayopunguza ari ya kuzima moto kasoro za uzalishaji.

Jumla ya gharama ya umiliki hupima gharama ya kupokea dhidi ya gharama ya kutopokea. Gharama za kupokea zinajumuisha kujenga na kudumisha mabomba, kukuza ufikiaji wa majaribio, na kuwekeza kwenye uonekanaji na wafanyakazi wa jukwaa. Gharama ya kutopokea ni kubwa lakini isiyoonekana: matoleo ya mkono ya polepole, maumivu ya ujumuishaji, matukio ya uzalishaji yanayoharibu sifa, na, katika mazingira yanayodhibitiwa, ukaguzi ulioshindwa na kurekebisha. Kwa uongozi, hoja inawekwa vizuri zaidi kwa maneno ya kupunguza hatari na uwezo. Uotomatishaji hugeuza muda adimu wa wahandisi wakuu kutoka kazi ya matoleo inayojirudia hadi kazi ya bidhaa, huku ukifanya hitilafu kuwa adimu na fupi zaidi.

## Mifumo mibaya na mitego

- **Mabomba ya kipekee.** Kila timu hujenga bomba la kipekee kwa mkono, kwa hiyo maboresho na marekebisho hayawezi kushirikiwa na ubora unatofautiana sana.
- **Kujenga upya kwa kila mazingira.** Kujenga upya kwa kila hatua kunavunja hakikisho ya "jenga mara moja" na kuruhusu tofauti za hila kufika kwenye uzalishaji.
- **Ujenzi mwekundu uliopuuzwa.** Kuvumilia mstari mkuu uliovunjika kwa muda mrefu kunaharibu uaminifu kwenye bomba na kufanya kusafirisha juu ya kushindwa kuwa kawaida.
- **Majaribio yasiyo thabiti yaliyoachwa.** Kushindwa kwa mara kwa mara huwazoeza wasanidi kuendesha tena hadi kijani, kushinda madhumuni ya lango.
- **Maigizo ya idhini ya mkono.** Bodi ya ushauri wa mabadiliko inayoweka muhuri kila kitu inaongeza ucheleweshaji bila kuongeza usalama.
- **Deni la bendera.** Bendera za vipengele ambazo hazijaondolewa kamwe hujilimbikiza kuwa ugumu wa masharti usiodumishika.
- **Kusambaza ni kutoa.** Kuviunganisha kunamaanisha kila badiliko linalomkabili mtumiaji linahitaji kusambaza upya kwa hatari.

## Kielelezo cha ukomavu

**Ngazi ya 1: Kuanzisha.** Ujenzi na usambazaji kwa kiasi kikubwa ni wa mkono, wa papo hapo, na wa kuitikia. Ujumuishaji unatokea marehemu, matoleo ni nadra na yenye mkazo, kurudisha nyuma kunamaanisha kusambaza upya toleo la zamani kwa mkono, na hakuna dhana ya pamoja ya lango la bomba.

**Ngazi ya 2: Kuendeleza.** Ujenzi wa kiotomatiki na majaribio ya kitengo yanaendeshwa kwa kila commit, lakini mazoea yanatofautiana timu hadi timu. Usambazaji umeandikwa kwa hati lakini bado unachochewa na kusimamiwa kwa mkono, baadhi ya mazingira ni thabiti, na mabaki yanaweza bado kujengwa upya kwa kila hatua. Pale bomba lipo mara nyingi ni la kipekee lisilowezekana kushirikiwa.

**Ngazi ya 3: Kusawazisha.** Kiolezo kilichoandikwa, sanifu cha bomba kinatekelezwa kuvuka timu. Kinapandisha mabaki moja yasiyobadilika kupitia mazingira yote, kinatumia malango ya kiotomatiki ya ubora na usalama, kinasimba ukaguzi unaohitajika kama idhini ya mapitio na matokeo ya uchanganuzi, na kinanasa rekodi za mabadiliko kiotomatiki. Mikakati ya usambazaji kama canary au buluu-kijani huchaguliwa kwa makusudi kwa ngazi ya huduma.

**Ngazi ya 4: Kusimamia.** Utoaji unapimwa na kudhibitiwa dhidi ya vipimo vya msingi. Shirika linafuatilia muda wa kuongoza wa mabadiliko, mzunguko wa usambazaji, kiwango cha kushindwa kwa mabadiliko, na muda wa wastani wa kupona, pamoja na muda wa p50 na p95 wa bomba, viwango vya majaribio yasiyo thabiti na kuendesha tena, na umri wa bendera za vipengele. Vizingiti vya kurudisha nyuma vimewekwa kutoka data iliyoonekana ya kiwango cha makosa, ucheleweshaji, na kujaa, malango yanatekelezwa kwa ushahidi badala ya mazoea, na kila kipimo kina mmiliki anayetenda kinapoteleza kutoka lengo.

**Ngazi ya 5: Kuratibu.** Utoaji unaboreshwa mfululizo na kuunganishwa kuvuka shirika. Utoaji wa hatua kwa hatua wenye kurudisha nyuma kiotomatiki unaoendeshwa na vipimo ndio kawaida, kutoa kumetenganishwa na kusambaza kupitia bendera zilizotawaliwa vizuri, na ushahidi wa uzingatiaji unazalishwa kiotomatiki kama zao la pembeni. Bomba linajirekebisha eneo linapobadilika, na vipimo vya utoaji vinalisha upangaji wa biashara na hatari ili uwekezaji uelekee maboresho ya kiegemeo cha juu zaidi.

## Mawazo ya kujadili

- Mpaka sahihi uko wapi kati ya utoaji endelevu wenye lango la binadamu na usambazaji endelevu kamili kwa mifumo yenu muhimu zaidi?
- Mnaweka vipi mchakato wa lazima wa usimamizi wa mabadiliko wenye maana bila kuugeuza maigizo ya kuweka muhuri?
- Vipimo gani vya afya vya lengo vinapaswa kutawala kurudisha nyuma kiotomatiki, na nani anamiliki vizingiti vyake?
- Timu za jukwaa zinapaswa kusawazishaje violezo sanifu vya bomba dhidi ya mahitaji halali ya timu zenye mahitaji ya kawaida?
- Sera na zana yenu ya kustaafisha bendera za vipengele kabla hazijawa deni ni ipi?
- Mnapimaje kama utoaji wa haraka zaidi unaboresha matokeo ya biashara kweli badala ya kusafirisha zaidi tu?

## Mambo muhimu ya kukumbuka

- CI, CD, na usambazaji endelevu ni tofauti; chagua kiwango cha uotomatishaji kinacholingana na uvumilivu wako wa hatari na ukomavu.
- Jenga mabaki mara moja na upandishe mabaki yaleyale kupitia kila mazingira.
- Sanifu bomba kama malango ya ubora yaliyopangwa yaliyoboreshwa kwa maoni ya haraka, na ulichukulie kama uamuzi wenye mamlaka wa kusafirisha.
- Chagua mikakati ya usambazaji kwa makusudi, na upokee utoaji wa hatua kwa hatua wenye kurudisha nyuma kiotomatiki kupunguza eneo la mlipuko.
- Tenganisha kutoa na kusambaza kwa bendera za vipengele, na usimamie deni la bendera.
- Katika mazingira yanayodhibitiwa, nasa ushahidi wa udhibiti wa mabadiliko kiotomatiki badala ya makaratasi ya mkono.

## Marejeo na usomaji zaidi

- Jez Humble and David Farley, *Continuous Delivery: Reliable Software Releases through Build, Test, and Deployment Automation*.
- Nicole Forsgren, Jez Humble, and Gene Kim, *Accelerate: The Science of Lean Software and DevOps*.
- Gene Kim, Jez Humble, Patrick Debois, and John Willis, *The DevOps Handbook*.
- Gene Kim, Kevin Behr, and George Spafford, *The Phoenix Project*.
- Betsy Beyer, Chris Jones, Jennifer Petoff, and Niall Richard Murphy (eds.), *Site Reliability Engineering*.
- Pete Hodgson, "Feature Toggles (Feature Flags)" (essay).
- ITIL (Information Technology Infrastructure Library), change management guidance.
