# 6.6 Miundombinu na operesheni za AI

## Muhtasari na msukumo

Miundombinu na operesheni za AI ni nidhamu ya kutayarisha, kupanga ratiba, na kuendesha mifumo maalumu ya kokotoo, hifadhi, na kuhudumia ambayo mizigo ya AI inadai, kwa gharama nafuu, kwa kutegemewa, na kwa kuonekana. AI ya kisasa ni ghali kuendesha. Kufunza na kuhudumia mifano mikubwa kunahitaji viongeza kasi adimu ([GPU](https://en.wikipedia.org/wiki/Graphics_processing_unit) na [TPU](https://en.wikipedia.org/wiki/Tensor_Processing_Unit)), mitandao ya kasi ya juu, hifadhi ya vekta ya kiwango kikubwa kwa urejeshaji (kuorodhesha data kama vekta za namba ili vitu vinavyofanana vipatikane haraka), na tabaka za kuhudumia zilizorekebishwa kwa ucheleweshaji na matokeo. Kupata miundombinu hii sawa ndiyo tofauti kati ya AI inayopanuka kwa uendelevu na AI inayotumia bajeti kimyakimya huku ikitoa pungufu.

Kwa timu kubwa, matatizo ya msingi ni ukubwa, uhaba, na gharama. Viongeza kasi ni vichache na ghali, kwa hiyo kupanga ratiba na matumizi ni muhimu sana. GPU zisizotumika ni fedha iliyochomwa, na uelekezaji usiokusanywa vizuri huzidisha gharama kwa kila ombi. Programu nzito za urejeshaji zinahitaji [hifadhidata za vekta](https://en.wikipedia.org/wiki/Vector_database) zinazobaki za haraka zinapokua. Programu za AI ya kuzalisha zinahitaji matoleo ya maagizo, mabomba ya tathmini, na uonekanaji (wakati mwingine huitwa LLMOps) kuendesha kwa usalama na kuboreka kwa muda. Bila miundombinu ya pamoja na nidhamu ya uendeshaji, kila timu inapigana vita vilevile na gharama zinaruka.

Mashirika ya serikali na yanayodhibitiwa huongeza mahitaji kuhusu enzi ya data, usalama, na matumizi yanayotabirika. Yanaweza kuhitaji usambazaji wa ndani ya majengo au wa wingu la enzi ili data nyeti na mifano visiondoke kamwe kwenye mipaka inayodhibitiwa. Lazima yatabiri na kuhalalisha matumizi ya miundombinu, na kutimiza viwango vya usalama na upatikanaji. Maamuzi ya miundombinu ya AI katika mazingira haya yana matokeo ya miaka mingi, kwa hiyo yafanye kwa kuzingatia ununuzi, usalama, na kutoka.

## Kanuni kuu

- Chukulia kokotoo la kiongeza kasi kama rasilimali adimu, ghali ya kupangiwa ratiba na kutumiwa, si kuhodhiwa.
- Boresha gharama kwa kila kipande cha kazi chenye manufaa, si uwezo ghafi.
- Rekebisha ukubwa wa mifano na maunzi kwa kazi; chaguo kubwa zaidi mara chache ni la gharama nafuu zaidi.
- Sanifu kuhudumia kwa ucheleweshaji na matokeo kwa kukusanya na kuhifadhi kwenye kache kama mbinu za daraja la kwanza.
- Fanya mifumo ya AI ionekane: fuatilia gharama, ucheleweshaji, ubora, na makosa mfululizo.
- Weka matoleo na utathmini maagizo na mifano kwa ukali ule ule kama msimbo.
- Panga kwa uwezo wa kuhamisha na epuka kufungwa katika uchaguzi wa miundombinu na kuhudumia.

## Mapendekezo

### Panga na dhibiti kokotoo la kiongeza kasi

Tabiri mahitaji ya mafunzo na uelekezaji tofauti, kwa sababu yana maumbo tofauti. Mafunzo ni ya milipuko na yanaweza kupangiwa ratiba; uelekezaji ni endelevu na nyeti kwa ucheleweshaji. Tumia vipanga ratiba na kiasi kugawana GPU na TPU adimu kuvuka timu, kuweka kipaumbele mizigo, na kuongeza matumizi. Pima matumizi na uchukulie kutotumika kwa muda mrefu kama tatizo la kurekebisha. Changanya uwezo ulioshikiliwa kwa mzigo wa msingi na uwezo wa mahitaji au wa doa kwa milipuko ili kudhibiti gharama. Fikiria kama viongeza kasi vya bei nafuu au vidogo, au uelekezaji wa CPU kwa mifano myepesi, vingetosha. Chagua kati ya wingu, ndani ya majengo, na mseto kulingana na gharama kwa ukubwa wako, mahitaji ya enzi ya data, na mifumo ya milipuko, na uhifadhi njia ya kutoka.

### Jenga miundombinu ya urejeshaji: embeddings na hifadhidata za vekta

Kwa programu za uzalishaji unaoongezwa kwa urejeshaji, simamisha miundombinu ya kuzalisha [embeddings](https://en.wikipedia.org/wiki/Word_embedding) (uwakilishi wa vekta za namba unaoweka vitu vinavyofanana karibu) na kuziweka kwenye hifadhidata ya vekta inayounga mkono [utafutaji wa jirani wa karibu wa takriban](https://en.wikipedia.org/wiki/Nearest_neighbor_search) (kupata vekta zinazofanana zaidi bila kulinganisha kila moja kikamilifu) kwa ukubwa wako. Panga kwa mambo matatu: gharama na ucheleweshaji wa kuzalisha embeddings, usafi wa faharasa nyaraka zinapobadilika, na mzigo wa uendeshaji wa kuweka faharasa zikiwa thabiti. Tathmini kama hifadhidata maalumu ya vekta, kiendelezi chenye uwezo wa vekta cha hifadhidata iliyopo, au huduma inayosimamiwa inafaa vizuri zaidi ukubwa wako na uvumilivu wa kufungwa. Fuatilia ucheleweshaji na ukumbukaji wa urejeshaji, kwa sababu ubora wa urejeshaji huamua moja kwa moja ubora wa programu.

### Boresha kuhudumia mifano: kukusanya, kache, na ucheleweshaji

Kuhudumia ndipo gharama ya uelekezaji na uzoefu wa mtumiaji huamuliwa. Tumia **kukusanya** kuchakata maombi kadhaa pamoja na kuongeza matokeo ya kiongeza kasi, ukisawazisha ukubwa wa kundi dhidi ya ucheleweshaji. Tumia **kache** kwa ukali: hifadhi maombi yanayofanana au yanayofanana kisemantiki, hifadhi embeddings, na tumia kache ya maagizo au awali pale jukwaa linapoiunga mkono ili kuepuka kukokotoa upya muktadha wa pamoja. Weka malengo wazi ya ucheleweshaji, na upime ucheleweshaji wa mkia, si wastani tu. Elekeza maombi kwa mifano ya ukubwa unaofaa: mfano mdogo kwa kesi rahisi, mkubwa tu inapohitajika. Panua kuhudumia kiotomatiki kwa mahitaji, na ujaribu mzigo kabla ya uzinduzi ili ujue uwezo wako na mkunjo wa gharama.

### Fanya LLMOps: matoleo ya maagizo, mabomba ya tathmini, na uonekanaji

Chukulia maagizo kama mabaki yenye matoleo kwenye udhibiti wa chanzo, yenye mapitio na uwezo wa kurudisha nyuma. Jenga mabomba ya tathmini yanayoendesha seti za majaribio za nje ya mtandao kiotomatiki kila maagizo au mifano inapobadilika, ili unase regression kabla ya toleo. Weka vifaa vya kupima kwa kina kwenye uzalishaji: andika ingizo, matokeo, ucheleweshaji, matumizi ya tokeni, gharama, na makosa, kwa sampuli na ulinzi wa faragha. Fuatilia ishara za ubora na maoni ya mtumiaji mtandaoni. Uonekanaji huu hukuruhusu kunasa kuzorota, kudhibiti gharama, kutatua kushindwa, na kuboresha mifumo kwa usalama: uti wa mgongo wa uendeshaji wa AI ya kuzalisha kwenye uzalishaji.

### Simamia gharama bila kuchoka na kwa kuonekana

Gawanya matumizi ya AI kwa timu na matumizi ili gharama ionekane na kumilikiwa. Weka bajeti na tahadhari, fuatilia gharama kwa kila ombi na kwa kila matokeo, na upitie vichochezi vikuu vya gharama mara kwa mara. Vuta viegemeo ulivyo navyo: kurekebisha ukubwa wa mfano, kache, kukusanya, kupunguza maagizo na muktadha, na kuchagua usambazaji wa bei nafuu zaidi unaotimiza mahitaji. Gharama za AI zinaweza kupanuka na matumizi kwa njia za kushangaza, kwa hiyo uonekanaji endelevu wa gharama ni muhimu kuepuka mshangao usiopendeza.

## Mabadilishano: faida na hasara

| Uamuzi | Chaguo A | Chaguo B | Mabadilishano |
|---|---|---|---|
| Mahali pa kokotoo | Wingu | Ndani ya majengo | Unyumbulifu na gharama ndogo ya awali dhidi ya udhibiti, enzi, na uchumi wa hali thabiti |
| Uwezo | Ulioshikiliwa | Wa mahitaji/doa | Gharama inayotabirika dhidi ya unyumbulifu na hatari ya kukatizwa |
| Ukubwa wa kundi | Makundi makubwa | Makundi madogo | Matokeo na gharama dhidi ya ucheleweshaji |
| Ukubwa wa mfano | Mfano mkubwa | Mfano mdogo | Ubora dhidi ya gharama na kasi |
| Hifadhi ya vekta | Hifadhidata maalumu | Kiendelezi cha hifadhidata iliyopo | Utendaji kwa ukubwa dhidi ya urahisi na mifumo michache |
| Kache | Kali | Kidogo | Gharama na ucheleweshaji mdogo dhidi ya usafi na ugumu |

Mabadilishano yanayotawala ni gharama dhidi ya ucheleweshaji na ubora. Kukusanya, kache, na mifano midogo hupunguza gharama lakini vinaweza kuongeza ucheleweshaji au kupunguza ubora. Mizani sahihi inategemea uvumilivu wa programu yako. Ndani ya majengo dhidi ya wingu hubadilisha udhibiti na uchumi wa hali thabiti dhidi ya unyumbulifu na kujitolea kidogo, uamuzi unaoumbwa sana na mahitaji ya enzi ya data na ukubwa.

## Maswali ya kujadili na timu yako

1. **Gharama yetu kwa kila matokeo yenye manufaa leo ni kiasi gani, na kiegemeo kipi kingeisogeza zaidi?** Uwezo ghafi na wastani wa kila ombi huficha namba inayojalisha: inagharimu kiasi gani kutoa kipande kimoja halisi cha thamani, na jinsi inavyopanuka na matumizi. Kwa timu kubwa, pengo kati ya usambazaji ulioboreshwa na ambao haujaboreshwa mara nyingi ni mara kadhaa katika matumizi, kwa hiyo swali hili hugeuza wasiwasi usio wazi kuhusu ankara kuwa orodha iliyopangwa ya marekebisho. Leta ugawaji wa sasa wa gharama kwa timu na matumizi, mielekeo ya kila ombi na kila matokeo, na vichochezi vikuu vya gharama. Jadili viegemeo kwa mpangilio wa faida: kurekebisha ukubwa wa mfano, kache (ikijumuisha kache ya awali na ya kisemantiki), kukusanya, na kupunguza maagizo au muktadha. Katika serikali, ongeza shinikizo la kutabiri na kuhalalisha matumizi ya miaka mingi. Jibu linapaswa kumpa kila kichochezi kikuu cha gharama mmiliki na kiegemeo, si kukunja mabega.

2. **Mtoa huduma wetu wa sasa wa uelekezaji akiongeza bei maradufu au akikatika kesho, tungebadili kwa kasi kiasi gani?** Kufungwa kimya ni rahisi kujenga na ya maumivu kuepuka, na mirundiko ya kuhudumia ndipo inapojificha kwa kina zaidi. Kwa mashirika na hasa serikali, uwezo wa kuhamisha ni sharti la ununuzi na mwendelezo, si pambo. Leta usanifu wenu: kama mifano inakaa nyuma ya kiolesura cha ndani, kama maagizo na mfululizo wa tathmini vinahamishika, na tabia ngapi mahususi ya mtoa huduma ya kuhudumia mnayoitegemea. Ishara ya kutazama ni kama yeyote amewahi kuendesha mfululizo wenu wa tathmini dhidi ya mtoa huduma wa pili au lengo la pili la usambazaji. Kubadili kungechukua miezi na kuandika upya njia za msingi, chukulia hilo kama kasoro ya usanifu ya kushughulikia sasa, kwa kuwa chaguo za enzi na za ndani ya majengo zinaweza kuwa za lazima kwa taarifa ndogo.

3. **Matumizi yetu ya kiongeza kasi sasa hivi ni kiasi gani, na GPU zisizotumika na uelekezaji usiokusanywa vinachoma kiasi gani?** Viongeza kasi ni adimu na ghali, kwa hiyo kutotumika kwa muda mrefu na kuhudumia kwa kila ombi huchota kimyakimya bajeti ambazo zingefadhili uwezo zaidi. Kwa shirika kubwa linalogawana GPU kuvuka timu, swali hili hufichua kama kupanga ratiba, kiasi, na vipaumbele vinaweka matumizi juu kweli au maunzi yaliyohodhiwa, yasiyotumika vizuri ndiyo kawaida. Leta namba halisi za matumizi, msimamo wenu wa kukusanya na kache, na vipimo vya ucheleweshaji wa mkia, si wastani tu, kwa kuwa watumiaji wanahisi mkia wa polepole. Jadili kama mahitaji ya mafunzo na uelekezaji yanatabiriwa tofauti, kwa kuzingatia maumbo yao tofauti, na kama mfano mdogo au uelekezaji wa CPU ungetosha kwa kesi nyepesi. Jibu linapaswa kuelekeza kwenye uwezo mahususi usiotumika wa kurejesha na maombi mahususi ya kukusanya au kuelekeza kwa mfano wa ukubwa unaofaa.

4. **Badiliko la agizo au mfano linaposafirishwa, nini kinazuia regression ya kimya ya ubora au gharama isiwafikie watumiaji?** Mrundiko wa kuhudumia unaweza kuonekana na afya kwenye ucheleweshaji na upatikanaji huku majibu inayorudisha yakizidi kuwa mabaya kimyakimya au agizo jipya likizidisha matumizi ya tokeni kwa kila ombi maradufu. Kwa timu kubwa ambapo vikundi vingi vinahariri maagizo na kubadilisha mifano kwa uhuru, badiliko lisilo na lango ni tukio la uzalishaji linalosubiri kutokea, na eneo la mlipuko hukua na kila timu kwenye jukwaa la pamoja. Leta ufikiaji wenu wa tathmini: maagizo na mifano ipi ina seti za majaribio za nje ya mtandao, kama seti hizo zinaendeshwa kiotomatiki kwa kila badiliko, vizingiti gani vya ubora na gharama vinaweka lango la toleo, na jinsi mnavyoweza kurudisha nyuma kwa haraka. Jadili kama maagizo yanaishi kwenye udhibiti wa chanzo wenye mapitio, au kama mtu bado anaweza kuhariri agizo la mfumo hai kwa mkono. Katika mazingira ya mashirika makubwa na serikali, funga kila badiliko na nyayo za ukaguzi na mwidhinishaji aliyetajwa, kwa sababu mdhibiti anayeuliza "nani alibadilisha hili na mlijaribu nini" anahitaji jibu lililorekodiwa, si lililokumbukwa.

5. **Tunaamuaje kati ya wingu, ndani ya majengo, na usambazaji wa enzi, na je, tumepima uchumi halisi wa hali thabiti badala ya jaribio?** Uchaguzi wa mahali pa kokotoo huweka mkunjo wenu wa gharama, msimamo wa enzi ya data, na chaguo za kutoka kwa miaka, hata hivyo mara nyingi hufanywa kwa ankara ya wingu ya jaribio isiyofanana kabisa na uzalishaji kwa ukubwa. Kwa shirika kubwa, uwezo unaobadilika wa wingu ni nafuu kuanza na unaweza kuwa mstari mkubwa zaidi mmoja uelekezaji unapoendeshwa mfululizo, wakati ndani ya majengo hubadilisha kujitolea kidogo kwa udhibiti na uchumi wa hali thabiti. Leta ujazo uliotabiriwa wa mafunzo na uelekezaji, kiwango cha kusawazisha ambapo maunzi yaliyoshikiliwa au yanayomilikiwa yanashinda ya mahitaji, vikwazo vyenu vya makazi ya data na usalama, na mifumo ya milipuko inayopendekeza mseto. Katika mazingira ya serikali na yanayodhibitiwa, pima mahitaji ya wingu la enzi au ndani ya majengo yanayoweza kuwa ya lazima kwa taarifa ndogo, na uthibitishe usanifu unaweka mifano nyuma ya kiolesura cha ndani ili hatua ya kulazimishwa isiandike upya njia za msingi.

6. **Tunamiliki matumizi yetu ya AI kweli, na kila timu inaweza kuona na kujibu gharama inayoendesha?** Gharama ya AI inapanuka na matumizi kwa njia zinazowashangaza watu, na bila ugawaji ankara inatua kama namba moja isiyo wazi ambayo hakuna timu inayohisi kuwajibika kuipunguza. Katika shirika kubwa, gharama ambayo hakuna anayeimiliki ni gharama ambayo hakuna anayeiboresha, kwa hiyo swali ni kama matumizi yamewekewa lebo kwa timu na matumizi yenye bajeti, tahadhari, na mielekeo ya kila matokeo, au yanagunduliwa tu fedha zinapopandisha ngazi. Leta mfano wenu wa ugawaji wa gharama, vichochezi vikuu kwa timu, na viegemeo ambavyo kila mmiliki anadhibiti: kurekebisha ukubwa, kache, kukusanya, na kupunguza muktadha. Kwa bajeti za mashirika makubwa na serikali, ongeza nidhamu ya kutabiri na kuhalalisha matumizi ya miundombinu ya miaka mingi, kwa kuwa chombo cha umma kisichoweza kuelezea ankara yake ya kokotoo mstari kwa mstari kitapata shida kuitetea kwenye mapitio.

## Mtazamo wa sekta

**Kampuni changa.** Usimiliki miundombinu yoyote unayoweza kuepuka. Ita API ya uelekezaji inayopangishwa, elekeza maombi rahisi kwa mfano mdogo wa bei nafuu na uhifadhi mkubwa kwa kesi ngumu, na uhifadhi kwa kache kwa ukali ili maagizo yanayojirudia yasigharimu chochote. Tumia hifadhidata ya vekta inayosimamiwa badala ya kuendesha yako, weka maagizo kwenye git na hati fupi ya tathmini kabla ya kila badiliko, na uandike gharama kwa kila ombi ili ankara inayokimbia ionekane kabla haijaumiza. Rasilimali yako adimu zaidi ni umakini wa kihandisi, kwa hiyo nunua uendeshekaji na uweke kubadili kwa bei nafuu.

**Biashara ndogo.** Bila timu ya jukwaa, chukulia kuhudumia, urejeshaji, na uonekanaji kama vitu unavyonunua ndani ya zana unazotumia tayari, si mifumo unayoiajiria. Pendelea uelekezaji unaosimamiwa na utafutaji wa vekta unaosimamiwa wenye bei ya uwazi, inayotabirika, na uweke kikomo kigumu cha matumizi na tahadhari ya bili tangu siku ya kwanza. Weka uamuzi kama kununua dhidi ya kujenga kwa uaminifu: kuendesha GPU au faharasa ya vekta mara chache kunalipa kwa kiasi chako, na mfano mdogo nyuma ya API inayopangishwa kwa kawaida hutimiza hitaji kwa sehemu ndogo ya juhudi.

**Biashara kubwa.** Tatizo ni jukwaa la pamoja, la barabara iliyojengwa kuvuka timu nyingi: viongeza kasi vilivyokusanywa vyenye vipanga ratiba, kiasi, na vipaumbele kuongeza matumizi, kukusanya na kache za kawaida, vipanga njia vya kurekebisha ukubwa, na gharama inayogawanywa kwa kila timu na matumizi. Weka lango la mabadiliko ya maagizo na mifano kwa mfululizo wa tathmini wa kiotomatiki, sawazisha tabaka la kiolesura ili watoa huduma na malengo ya usambazaji yabaki yakibadilishika, na simamia gharama kwa kila matokeo kama kipimo cha daraja la kwanza badala ya kila kikundi kubuni upya miundombinu ghali, isiyotumika vizuri.

**Serikali.** Enzi ya data, usalama, na matumizi yanayotabirika huumba kila uchaguzi. Pendelea usambazaji wa ndani ya majengo au wa wingu la enzi ili data nyeti na mifano ibaki ndani ya mipaka inayodhibitiwa, panga ratiba ya GPU adimu kuvuka idara kwa kiasi unachoweza kuhalalisha kwenye ununuzi, na tabiri uwezo kutetea matumizi ya miaka mingi mstari kwa mstari. Weka matoleo na utathmini maagizo na mifano kwa nyayo za ukaguzi zilizorekodiwa, weka uonekanaji kamili juu ya gharama na ubora, na uweke mifano nyuma ya kiolesura cha ndani ili hatua ya kulazimishwa kwa mtoa huduma mpya au jukwaa la enzi isikuache ukiwa umekwama.

## Mifano

**Kampuni changa.** Kampuni changa ndogo inayoendesha kipengele cha uandishi cha AI iliweka ankara yake yenye akili bila kumiliki GPU yoyote. Iliita API ya uelekezaji inayopangishwa, ikaelekeza maombi rahisi kwa mfano mdogo wa bei nafuu na kuhifadhi mkubwa kwa kesi ngumu, na kuhifadhi majibu ya maagizo yanayojirudia kwenye kache. Iliweka maagizo yake kwenye git yenye hati fupi ya tathmini iliyoendeshwa kabla ya kila badiliko, ilitumia hifadhidata ya vekta inayosimamiwa kwa urejeshaji ili isiiendeshe, na iliandika gharama kwa kila ombi ili waanzilishi waone matumizi yakipanda kabla hayajawa mshangao.

**Biashara kubwa.** Kampuni ya vyombo vya habari inayoendesha kipengele cha LLM chenye trafiki ya juu ilipunguza gharama za uelekezaji kwa kiasi kikubwa. Ilielekeza maombi rahisi kwa mfano mdogo na kuhifadhi mkubwa kwa magumu. Ilihifadhi majibu ya maswali yanayojirudia kwenye kache na kuwasha kache ya awali kwa agizo lake la mfumo la pamoja. Iliendesha GPU kupitia kipanga ratiba cha pamoja kuweka matumizi juu, iliweka matoleo ya maagizo yote kwenye git na mfululizo wa tathmini wa kiotomatiki ukiweka lango la mabadiliko, na iliweka vifaa vya kupima gharama kwa kila ombi ili kila timu ya bidhaa imiliki matumizi yake.

**Serikali.** Wakala wa kitaifa wenye kanuni kali za enzi ya data ulisambaza mifumo yake ya AI ndani ya majengo ili data nyeti na mifano visiache mazingira yake yanayodhibitiwa. Ulipanga ratiba ya GPU adimu kuvuka idara kwa kiasi na vipaumbele, ulitabiri uwezo kuhalalisha ununuzi wa miaka mingi, na kujenga jukwaa la utafutaji wa vekta kwa urejeshaji juu ya nyaraka rasmi. Maagizo na mifano viliwekewa matoleo na kutathminiwa kabla ya toleo. Uonekanaji kamili ulifuatilia gharama na ubora, na usanifu uliweka mifano nyuma ya kiolesura cha ndani kuhifadhi njia ya kutoka na kuepuka kufungwa.

## Kesi ya biashara: sababu, ROI, na TCO

Motisha ya miundombinu ya AI yenye nidhamu ni rahisi. AI kwa ukubwa ni ghali, na pengo kati ya usambazaji ulioboreshwa na usioboreshwa mara nyingi ni mara kadhaa katika matumizi. ROI inatokana na matumizi ya juu ya kiongeza kasi, gharama ndogo kwa kila ombi kupitia kukusanya na kache, mifano ya ukubwa unaofaa, na kuepuka kutayarisha kupita kiasi. Uonekanaji na mabomba ya tathmini hulipa kwa kuzuia matukio ya gharama na kuwezesha marudio salama.

TCO inaenea kuvuka kokotoo la kiongeza kasi (mstari mkubwa zaidi kwa mizigo mingi), hifadhi ya vekta, miundombinu ya kuhudumia, mitandao, na wafanyakazi wa jukwaa na operesheni wa kuendesha. Ipime dhidi ya gharama ya kutowekeza: ankara za uelekezaji zinazokimbia, ucheleweshaji duni unaodhoofisha upokeaji, na kushindwa kupanuka. Kwa serikali, ongeza gharama ya kushindwa mahitaji ya enzi au usalama. Weka kesi kwa uongozi kwa kuonyesha mielekeo ya gharama kwa kila matokeo na jukwaa la barabara iliyojengwa linaloruhusu timu nyingi kusambaza AI kwa ufanisi, badala ya kila moja kujenga miundombinu ghali, isiyotumika vizuri.

## Mifumo mibaya na mitego

- **Viongeza kasi visivyotumika.** Kutenga GPU adimu kwa timu zinazoziacha zikitumika kidogo.
- **Hakuna kukusanya wala kache.** Kuhudumia kila ombi moja moja na kukokotoa upya muktadha wa pamoja.
- **Mfano mkubwa zaidi kwa chaguo-msingi.** Kutumia mfano wa gharama pale mdogo ungetosha.
- **Upofu wa gharama.** Hakuna ugawaji, bajeti, au mwonekano wa gharama kwa kila ombi hadi ankara ifike.
- **Maagizo bila matoleo.** Kubadilisha maagizo kwenye uzalishaji bila matoleo au lango la tathmini.
- **Kupuuza ucheleweshaji wa mkia.** Kuboresha ucheleweshaji wa wastani huku watumiaji wakiteseka na mikia ya polepole.
- **Kufungwa kimya.** Kujenga kwa kina juu ya mrundiko wa kuhudumia wa mtoa huduma mmoja bila uwezo wa kuhamisha.

## Kielelezo cha ukomavu

1. **Kuanzisha.** Ugawaji wa GPU wa papo hapo ukimjibu anayepaza sauti zaidi, hakuna kukusanya wala kache, hakuna mwonekano wa gharama hadi ankara ifike, maagizo yanahaririwa hai na bila matoleo, ufuatiliaji mdogo.
2. **Kuendeleza.** Baadhi ya timu hupokea upangaji wa ratiba wa pamoja, kache, na maagizo yenye udhibiti wa matoleo, lakini mazoea hayana uthabiti kuvuka shirika: kundi moja linakusanya na kutathmini huku jingine bado linahudumia kila ombi moja moja na kubadilisha maagizo kwa mkono.
3. **Kusawazisha.** Jukwaa lililoandikwa, la barabara iliyojengwa linatekelezwa shirika zima: upangaji wa ratiba wa pamoja wenye kiasi na vipaumbele, kukusanya, kache, na kurekebisha ukubwa vya kawaida, miundombinu ya vekta kwa urejeshaji, mabomba ya tathmini ya kiotomatiki yanayoweka lango la kila badiliko la agizo au mfano, na ugawaji wa gharama kwa timu na matumizi.
4. **Kusimamia.** Jukwaa linapimwa na kudhibitiwa dhidi ya vipimo vya msingi: matumizi ya kiongeza kasi, gharama kwa kila matokeo yenye manufaa, ucheleweshaji wa mkia, ukumbukaji wa urejeshaji, na regression za ubora kwa kila badiliko vinafuatiliwa kwa tahadhari na vizingiti, gharama inamilikiwa na kila timu, na kwenda au kutokwenda kwenye badiliko kunaamuliwa kwa ushahidi badala ya hisia.
5. **Kuratibu.** Miundombinu inaboreshwa mfululizo na kujirekebisha: uelekezaji, kukusanya, na kupanua hujirekebisha kwa ishara hai za gharama na ubora, uwezo unasawazishwa upya kuvuka timu na kati ya wingu, ndani ya majengo, na malengo ya enzi mahitaji na vikwazo vinapohama, uwezo wa kuhamisha unafanyiwa mazoezi, na upangaji wa miundombinu umeunganishwa na bidhaa, usalama, na ununuzi.

## Mawazo ya kujadili

- Mnaongezaje matumizi ya kiongeza kasi bila kunyima mizigo ya kipaumbele?
- Usawa sahihi wa kukusanya na kache uko wapi kwa mahitaji yenu ya ucheleweshaji?
- Usambazaji wa ndani ya majengo au wa enzi unahalalisha gharama yake juu ya wingu lini?
- Mnagawa na kudhibiti vipi matumizi ya AI kuvuka timu nyingi?
- Nini kinapaswa kuweka lango la badiliko la agizo au mfano kufikia uzalishaji?
- Mnaweka vipi miundombinu ya kuhudumia ikihamishika vya kutosha kubadili watoa huduma?

## Mambo muhimu ya kukumbuka

- Viongeza kasi ni adimu na ghali; vipangie ratiba, vigawane, na vitumie kwa makusudi.
- Kukusanya, kache, na kurekebisha ukubwa wa mfano ndio viegemeo vikuu vya gharama na ucheleweshaji.
- Programu za urejeshaji zinahitaji miundombinu ya embedding na utafutaji wa vekta inayoendeshwa vizuri.
- LLMOps (matoleo ya maagizo, mabomba ya tathmini, na uonekanaji) ni uti wa mgongo wa uendeshaji wa AI ya kuzalisha.
- Simamia gharama kwa kuonekana na uhifadhi uwezo wa kuhamisha ili kuepuka kufungwa.

## Marejeo na usomaji zaidi

- Chip Huyen, *Designing Machine Learning Systems*.
- Google, *Site Reliability Engineering* (Beyer, Jones, Petoff, Murphy, editors).
- Jared Kaplan et al., *Scaling Laws for Neural Language Models*.
- Reza Yazdani Aminabadi et al., *DeepSpeed Inference: Enabling Efficient Inference of Transformer Models at Unprecedented Scale*.
- Woosuk Kwon et al., *Efficient Memory Management for Large Language Model Serving with PagedAttention* (vLLM).
- Andriy Burkov, *Machine Learning Engineering*.
