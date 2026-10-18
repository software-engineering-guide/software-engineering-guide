# 7.2 Uhandisi wa data

## Muhtasari na msukumo

[Uhandisi wa data](https://en.wikipedia.org/wiki/Data_engineering) ni nidhamu ya kujenga na kuendesha mabomba na majukwaa yanayohamisha data kutoka inapozalishwa hadi inapounda thamani. Inashughulikia kuingiza kutoka mifumo chanzo, kubadilisha kuwa maumbo safi, yaliyoumbwa, kuhifadhi katika miundo ya gharama nafuu, kuratibu mtiririko mzima, na mazoea ya kutegemewa yanayoweka yote ya kuaminika. Kama mkakati wa data unavyoamua data gani inapaswa kuwepo na nani anaimiliki, uhandisi wa data ni mabomba na mitambo inayoifanya itiririke.

Kwa timu kubwa, nidhamu hii ni ya msingi. Uchanganuzi, [akili ya biashara](https://en.wikipedia.org/wiki/Business_intelligence), majaribio ya bidhaa, [kujifunza kwa mashine](https://en.wikipedia.org/wiki/Machine_learning), na kuripoti kwa udhibiti vyote viko chini ya mkondo wa mabomba ya data. Mabomba hayo yanapokuwa dhaifu, ya polepole, au yasiyo wazi, kila kazi tegemezi inateseka. Dashibodi zinaonyesha namba zilizochakaa. Mifano inafunzwa kwa vipengele vilivyoharibika. Wakaguzi hawawezi kujenga upya jinsi takwimu ilivyozalishwa. Kwa ukubwa wa mashirika na serikali, mabomba huchakata mabilioni ya rekodi kuvuka mifumo mingi chanzo, na kushindwa kimya kimoja kunaweza kusukuma data isiyo sahihi kwenye maamuzi, malipo, au takwimu za umma.

Uwanja umekua kutoka hati za mtu mmoja na zana kubwa za [ETL (toa, badilisha, pakia)](https://en.wikipedia.org/wiki/Extract,_transform,_load) hadi mrundiko wa kisasa wa data: vijenzi vya moduli, kwa kiasi kikubwa vinavyoendeshwa na SQL kwa kuingiza, kubadilisha, kuratibu, na kuhifadhi, vilivyounganishwa na miundo wazi. Moduli hii ni zawadi na mtego. Inakuruhusu kukusanya zana bora kabisa kila moja, lakini bila nidhamu ya kihandisi huzalisha mtawanyiko wa kazi zisizoandikwa, zisizojaribiwa. Sura hii inashughulikia mazoea yanayoweka mabomba yakiwa na kutobadilika thamani, yanayojaribika, yanayoonekana, na ya bei nafuu kwa ukubwa.

## Kanuni kuu

- Mabomba ni programu na yanastahili udhibiti wa matoleo, majaribio, mapitio, na CI/CD.
- Pendelea mabadiliko yenye kutobadilika thamani, yanayozalishika upya yanayoweza kuendeshwa tena kwa usalama.
- Fanya mtiririko wa data uonekane: usafi, kiasi, skima, na ubora vinafuatiliwa.
- Unda data kwa makusudi kwa watumiaji wake badala ya kutupa majedwali ghafi.
- Chagua kundi au kutiririka kulingana na mahitaji halisi ya ucheleweshaji, si ugeni.
- Boresha umbo la hifadhi, ugawaji, na gharama ya kokotoo kama mambo ya daraja la kwanza.
- Tenganisha kuingiza, kubadilisha, na kuhudumia ili kila moja ibadilike kwa uhuru.
- Shindwa kwa sauti na mapema; bomba lililovunjika ni salama kuliko data isiyo sahihi kimyakimya.

## Mapendekezo

### Chagua ETL au ELT kwa makusudi

ETL hubadilisha data kabla ya kuipakia kwenye lengo. [ELT (toa, pakia, badilisha)](https://en.wikipedia.org/wiki/Extract,_load,_transform) hupakia data ghafi kwanza na kuibadilisha ndani ya ghala au lakehouse yenye nguvu. Majukwaa ya kisasa ya wingu yamefanya ELT kuwa chaguo-msingi, kwa sababu hifadhi ni nafuu na kokotoo linanyumbulika, na kuweka data ghafi kunakuruhusu kuchakata upya mantiki inapobadilika au hitilafu zinapojitokeza. Pendelea ELT kwa mizigo ya uchanganuzi: weka data ghafi isiyobadilika, kisha jenga mabadiliko ya tabaka juu yake. Hifadhi kubadilisha kabla ya kupakia kwa kesi ambapo faragha, gharama, au vikwazo vya kimkataba vinahitaji kusafisha au kuchuja data kabla haijatua.

### Sanifu mabomba ya kundi na ya kutiririka kwa mahitaji yao ya ucheleweshaji

Mahitaji mengi ya uchanganuzi yanahudumiwa vizuri na mabomba ya kundi yaliyopangiwa ratiba, ambayo ni rahisi zaidi kufikiria, kujaribu, na kujaza nyuma. Fikia kutiririka tu biashara inapohitaji data ya ucheleweshaji mdogo kweli: kugundua ulaghai, tahadhari za uendeshaji, ubinafsishaji wa wakati halisi. Kutiririka huongeza ugumu halisi kuhusu mpangilio, semantiki ya mara-moja-tu, data inayofika kuchelewa, na usimamizi wa hali. Pale unapohitaji vyote viwili, fikiria usanifu unaounganisha mantiki ya kundi na kutiririka badala ya kudumisha misingi miwili ya msimbo inayotofautiana. Kuwa mwaminifu kuhusu mahitaji yako ya ucheleweshaji. "Wakati halisi" mara nyingi ni tamanio lisilochunguzwa linalozidisha gharama yako maradufu.

### Ratibu kwa utegemezi wazi

Tumia kiratibu kueleza mabomba kama [grafu zisizo na mzunguko zilizoelekezwa (DAG)](https://en.wikipedia.org/wiki/Directed_acyclic_graph) za kazi zenye utegemezi wazi, kujaribu tena, na ratiba. Hii inakupa mwonekano wa kile kilichoendeshwa, kilichoshindwa, na kilichozuiwa, pamoja na uwezo wa kujaza nyuma na kuendesha tena kwa kuamuliwa. Weka utegemezi kwa upatikanaji wa data, si saa tu, ili kazi za chini ya mkondo zisubiri data ya juu ya mkondo badala ya kuwaka kwa kubahatisha. Weka mantiki ya uratibu kwenye udhibiti wa matoleo, na uchukulie mabadiliko ya DAG kama mabadiliko ya msimbo.

### Unda data kwa matumizi

Majedwali ghafi mara chache yanafaa wachambuzi. Tumia [uundaji wa vipimo](https://en.wikipedia.org/wiki/Dimensional_modeling), unaopanga ukweli na vipimo vinavyolingana katika [skima za nyota](https://en.wikipedia.org/wiki/Star_schema), pale unapohitaji uchanganuzi uliotawaliwa, unaotumika tena, wa kujihudumia. Majedwali mapana yasiyo na muundo wa kawaida ("jedwali moja kubwa") yanaweza kufanya vizuri zaidi kwa mifumo mahususi ya maswali na ni rahisi kwa baadhi ya watumiaji, kwa gharama ya marudio na unyumbulifu. Panga mabadiliko yako kwa tabaka: tabaka ghafi la maandalizi, tabaka la msingi lililosafishwa na kupatanishwa, na maghala madogo yanayomkabili mtumiaji. Utengano huu unakuruhusu kurekebisha mantiki mahali pamoja, na unaruhusu watumiaji kutegemea violesura thabiti.

### Fanya mabomba yawe na kutobadilika thamani na yajaribike

Sanifu mabadiliko ili kuyaendesha tena kuzalishe matokeo yaleyale, badala ya kurudia au kuharibu data, kwa mfano kwa kutumia upserts za kuamuliwa zilizofungwa kwa vitambulisho vya biashara na mifumo ya kuandika juu ya ugawaji. Andika majaribio katika ngazi nyingi: majaribio ya kitengo kwa mantiki ya mabadiliko, majaribio ya skima, na majaribio ya data yanayothibitisha matarajio kama upekee, funguo zisizo tupu, uadilifu wa marejeo, na safu zinazokubalika za thamani. Yaendeshe haya kwenye CI, ili badiliko baya linaswe kabla halijafika kwenye data ya uzalishaji.

### Weka vifaa vya kupima uonekanaji na kutegemewa

Fuatilia ishara nne kuu za afya ya data: usafi (je, ni ya sasa), kiasi (je, idadi ya safu iko katika safu inayotarajiwa), skima (je, muundo umebadilika bila kutarajiwa), na usambazaji (je, thamani zimeteleza kwa njia isiyo ya kawaida). Toa tahadhari ukiukaji, na uzielekeze kwa timu inayomiliki. Weka vitabu vya mwongozo, mizunguko ya simu ya dharura, na tathmini zisizo na lawama za baada ya tukio kwa matukio ya data, kama ungefanya kwa huduma. Fuatilia asili, ili kitu kinapovunjika, uone athari ya chini ya mkondo mara moja.

### Boresha hifadhi na gharama

Tumia miundo wazi ya safu wima kama Parquet, au miundo wazi ya jedwali inayounga mkono mabadiliko ya skima, kusafiri kwa wakati, na masasisho yenye ufanisi. Gawanya data kwa safu wima unazochuja zaidi, kwa kawaida tarehe, na epuka kuenea kwa faili ndogo ndogo kwa kuziunganisha. Tenganisha data ya moto na baridi kwa hifadhi ya ngazi na sera za mzunguko wa maisha. Fuatilia matumizi ya kokotoo kwa kila bomba na kila swali. Gharama zinazokimbia kwa kawaida hutokana na uchanganuzi kamili, ugawaji uliokosekana, na kuchakata upya bila mipaka. Chukulia gharama kama kipimo chenye wamiliki, si mshangao kwenye ankara ya kila mwezi.

## Mabadilishano: faida na hasara

| Chaguo | Faida | Hasara | Inafaa zaidi |
|---|---|---|---|
| ELT (badilisha mahali) | Huweka data ghafi, hifadhi nafuu, inaweza kuchakatwa upya | Alama kubwa ya hifadhi, inahitaji utawala | Uchanganuzi wa wingu |
| ETL (badilisha kabla ya kupakia) | Hudhibiti gharama, huchuja data nyeti mapema | Hupoteza ghafi, ngumu kuchakata upya | Mizigo inayodhibitiwa au yenye vikwazo |
| Kundi | Rahisi, inajaribika, rahisi kujaza nyuma | Ucheleweshaji wa juu | Uchanganuzi mwingi |
| Kutiririka | Ucheleweshaji mdogo, mwitikio wa wakati halisi | Changamano, ghali, ngumu kujaribu | Ulaghai, tahadhari za uendeshaji |
| Skima ya nyota | Iliyotawaliwa, inatumika tena, rafiki kwa kujihudumia | Juhudi ya uundaji mwanzoni | BI ya pamoja |
| Jedwali pana | Haraka kwa maswali yanayojulikana, rahisi | Marudio, unyumbulifu mdogo | Matumizi finyu ya utendaji wa juu |

Mabadilishano yanayotawala ni urahisi dhidi ya ucheleweshaji na unyumbulifu. Kundi na ELT zenye skima za nyota za tabaka hukupa mfumo unaojaribika, unaoweza kujazwa nyuma, unaoeleweka vizuri unaohudumia mahitaji mengi kwa bei nafuu. Kutiririka, wakati halisi, na miundo isiyo na muundo wa kawaida sana hununua kasi na utendaji mahususi, lakini kwa gharama kali katika ugumu wa uendeshaji na ugumu wa kujaribu. Pokea ugumu tu pale hitaji madhubuti la biashara linapoulipia, na uweke njia rahisi kama chaguo-msingi lako.

## Maswali ya kujadili na timu yako

1. **Mmechagua ELT badala ya ETL kwa makusudi, na je, mnaweka data ghafi isiyobadilika ili muweze kuchakata upya mantiki inapobadilika au hitilafu zinapojitokeza?** Chaguo-msingi la sura ni ELT: weka data ghafi kwa bei nafuu, kisha jenga mabadiliko ya tabaka, kwa sababu kuweka ghafi kunakuruhusu kuendesha kila kitu tena kanuni inapobadilika au hitilafu inapoonekana wiki baadaye. Kufuta data ghafi kunafunga chaguo hilo na ni mtego wa kawaida wenye maumivu. Hoja ya ETL ni halisi katika mizigo inayodhibitiwa au yenye vikwazo, ambapo faragha, gharama, au masharti ya mkataba yanahitaji kuchuja au kuficha kabla data haijatua. Leta ushahidi: mmehitaji mara ngapi kuchakata upya historia, na iligharimu nini mliposhindwa? Kwa bomba la serikali au shirika linalopaswa kufuatilia takwimu yoyote hadi chanzo, rekodi ghafi zisizobadilika pia ni sharti la uwezo wa kukaguliwa, kwa hiyo jibu linaumba sera yenu ya hifadhi na uwezo wenu wa kutetewa kisheria.

2. **Ni ishara zipi kati ya nne za afya ya data mnazofuatilia kweli, na nani anapigiwa simu moja inapovunjika?** Sura inataja ishara nne zinazostahili kutazamwa: usafi, kiasi, skima, na usambazaji. Timu nyingi hazifuatilii hata moja na hujifunza kuhusu kushindwa kutoka kwa mtendaji anayetazama dashibodi iliyochakaa, ambacho ndicho kigunduzi kibaya zaidi kinachowezekana. Kwa ukubwa wa mashirika na serikali, kushindwa kimya kimoja kunaweza kusukuma data isiyo sahihi kwenye malipo, ripoti, au takwimu za umma, kwa hiyo gharama ya ugunduzi wa marehemu inapimwa kwa uaminifu na fedha, si kurekebisha tu. Leta muda wenu halisi wa wastani wa kugundua na jina la yeyote anayepata matukio kwanza sasa. Jibu likiwa "mtumiaji," mnahitaji tahadhari zinazoelekezwa kwa timu inayomiliki pamoja na vitabu vya mwongozo na tathmini zisizo na lawama za baada ya tukio, mkichukulia matukio ya data kama hitilafu za huduma.

3. **Wachambuzi wenu wanatumia maghala madogo yaliyoumbwa, yaliyojaribiwa, au mnawatupia majedwali ghafi na kuita kujihudumia?** Sura iko wazi: majedwali ghafi mara chache yanafaa wachambuzi, na kupanga mabadiliko kwa tabaka kuwa tabaka ghafi la maandalizi, msingi uliopatanishwa, na maghala madogo yanayomkabili mtumiaji kunakuruhusu kurekebisha mantiki mara moja na kuwapa watumiaji violesura thabiti. Mvuto unaoshindana ni kasi, kwa kuwa kuunda kwa skima za nyota au majedwali mapana ya makusudi kunagharimu juhudi mwanzoni na ni rahisi kuruka. Lakini kutupa data ghafi kunasukuma gharama ya uundaji kwa kila mchambuzi mara kwa mara, ikizalisha namba tofauti na saa zilizopotea. Leta ishara: sehemu gani ya muda wa wachambuzi inaenda kubadilisha umbo la data ghafi, na timu ngapi zimejenga upya viungo vilevile. Namba ikiwa ya juu, wekeza kwenye tabaka la msingi lililopatanishwa ili watumiaji wategemee violesura vilivyojaribiwa, vinavyotumika tena badala ya kuvibuni upya.

4. **"Wakati halisi" unastahili gharama yake wapi kweli, na wapi ni tamanio lisilochunguzwa linalozidisha mzigo wenu wa uendeshaji maradufu kimyakimya?** Chaguo-msingi la sura ni kundi lililopangiwa ratiba, ambalo ni rahisi zaidi kufikiria, kujaribu, na kujaza nyuma, huku kutiririka kukihifadhiwa kwa kesi ambapo biashara inahitaji ucheleweshaji mdogo kweli, kama kugundua ulaghai au tahadhari za uendeshaji. Mvuto unaoshindana ni heshima na maombi yasiyo wazi ya wadau ya data "hai," yanayosikika nafuu kwenye mkutano wa mipango na kuwa ghali kwenye uzalishaji, kwa sababu kutiririka kunaburuza mpangilio, semantiki ya mara-moja-tu, data inayofika kuchelewa, na usimamizi wa hali, pamoja na msingi wa pili wa msimbo wa kuweka sawia na mantiki ya kundi. Leta ushahidi kwenye mjadala: kwa kila bomba la kutiririka mnaloendesha au kupendekeza, taja uamuzi unaoulisha na ucheleweshaji ambao uamuzi huo unavumilia kweli, ukipimwa kwa dakika au saa badala ya vivumishi. Kwa jukwaa kubwa la shirika au serikali, ongeza gharama ya simu ya dharura na majaribio ya kila njia ya wakati halisi, kwa sababu bomba la kutiririka ambalo hakuna anayeweza kulijaribu wala kulihudumia saa nzima ni dhima ya kutegemewa iliyovaa kama kipengele, na jibu la uaminifu mara nyingi hurudisha hitaji la "wakati halisi" kuwa kundi la kila saa linalohudumia uamuzi uleule.

5. **Mabomba yenu yapi hayawezi kuendeshwa tena kwa usalama leo, na ingehitaji nini kufanya kila badiliko liwe na kutobadilika thamani?** Sura inasisitiza mabadiliko yenye kutobadilika thamani, yanayozalishika upya, kwa kutumia upserts za kuamuliwa zilizofungwa kwa vitambulisho vya biashara na mifumo ya kuandika juu ya ugawaji, ili kuendesha tena kuzalishe matokeo yaleyale badala ya kurudia au kuharibu data. Shinikizo linaloshindana ni kasi ya utoaji, kwa kuwa kazi ya kuongeza tu inasafirishwa haraka kuliko iliyobuniwa kuendeshwa tena, na gharama ya njia hiyo ya mkato inabaki imejificha hadi kushindwa kulazimishe kuendesha upya kwa sehemu saa nane usiku na mtu ahesabu mapato mara mbili. Leta orodha madhubuti: orodhesha kazi ambazo zingeharibu data kama zingeendeshwa tena kutoka nukta ya kushindwa, na ukadirie eneo la mlipuko la mbaya zaidi. Kwa ukubwa wa mashirika na serikali, ambapo kushindwa kimya kimoja kunaweza kusukuma data isiyo sahihi kwenye malipo, ripoti, au takwimu za umma, uchakataji usio na kutobadilika thamani si usumbufu tu, unadhoofisha uwezo wa kukaguliwa unaokuruhusu kuchakata upya kipindi baada ya kanuni kubadilika na bado kufuatilia kila takwimu hadi chanzo, kwa hiyo kufadhili kazi ya kufanya kuendesha upya kuwe salama ni swali la kidhibiti, si usafi tu.

6. **Mnajua kila bomba linagharimu kiasi gani kuendesha, nani anamiliki namba hiyo, na sehemu gani ya ankara yenu ya wingu inatokana na uchanganuzi kamili na ugawaji uliokosekana?** Sura inachukulia umbo la hifadhi, ugawaji, na matumizi ya kokotoo kama mambo ya daraja la kwanza yenye wamiliki, ikionya kwamba gharama zinazokimbia kwa kawaida hutokana na uchanganuzi kamili, ugawaji uliokosekana, na kuchakata upya bila mipaka. Mazingatio yanayoshindana ni kwamba kazi ya gharama inahisi isiyo ya dharura kuliko kusafirisha vipengele, kwa hiyo inaahirishwa hadi ankara ya kila mwezi iwe mshangao na fedha zianze kuuliza maswali ambayo uhandisi hauwezi kujibu. Leta ushahidi: matumizi kwa kila bomba na kila swali, sehemu ya gharama inayotokana na uchanganuzi usiogawanywa, na idadi ya faili ndogo ndogo zinazopaswa kuunganishwa. Kwa shirika kubwa linaloendesha mabilioni ya rekodi kuvuka mifumo mingi chanzo, ankara ya wingu isiyomilikiwa hukua bila timu yoyote kuhisi kuwajibika, na katika mazingira ya serikali matumizi ya umma lazima yahalalishwe mstari kwa mstari, kwa hiyo kugawa gharama ya kokotoo kwa mmiliki aliyetajwa mwenye kipimo kinachofuatiliwa hugeuza matumizi yasiyo wazi kuwa yanayosimamiwa na mara nyingi hufichua akiba kubwa vya kutosha kufadhili uwekezaji unaofuata wa jukwaa.

## Mtazamo wa sekta

**Kampuni changa.** Kasi inashinda usanifu. Unganisha kuingiza kwenye kiunganishi kinachosimamiwa, jenga mabadiliko machache yenye udhibiti wa matoleo, na uyaendeshe kwenye kiratibu chepesi kinachojaribu tena na kujaza nyuma chenyewe, badala ya kuandika kwa mkono kazi za cron zinazovunjika kimyakimya usiku. Weka kila modeli yenye kutobadilika thamani tangu commit ya kwanza na uongeze majaribio machache ya bei nafuu kwa funguo tupu na hesabu za safu, ili badiliko baya la chanzo lishindwe kwenye CI badala ya kujitokeza kwenye dashibodi ya mwanzilishi Jumatatu. Usisimamishe kutiririka wala jukwaa maalumu: rasilimali yako adimu zaidi ni umakini wa kihandisi.

**Biashara ndogo.** Bila mhandisi maalumu wa data, pendelea kununua mrundiko uliounganishwa kuliko kukusanya mmoja. Huduma ya ELT inayosimamiwa pamoja na ghala la wingu inakupa viunganishi, ratiba, na hifadhi bila timu ya jukwaa ya kuzidumisha. Weka chaguo kama usafi wa data badala ya mradi wa mabomba: jua mifumo chanzo ipi inalisha ripoti zako, weka data ghafi ili namba isiyo sahihi ifuatiliwe na kuchakatwa upya, na uchague zana ambazo gharama zake zinatabirika ili uchanganuzi kamili wa jedwali usilipue bajeti ya kila mwezi.

**Biashara kubwa.** Tatizo ni uthabiti kuvuka timu nyingi na mabilioni ya rekodi kutoka mifumo mingi chanzo. Sawazisha mfumo wa ELT, mfano wa tabaka za maandalizi-msingi-ghala dogo, na ishara nne za afya ya data ili vikundi viache kubuni upya mabomba dhaifu. Tekeleza majaribio ya data na CI kwenye kila modeli, gawa gharama ya kokotoo kwa timu zinazomiliki, na uendeshe matukio ya data kupitia nidhamu ileile ya simu ya dharura, kitabu cha mwongozo, na tathmini isiyo na lawama ya baada ya tukio unayotumia kwa huduma, ili kushindwa kimya kusifike kwenye dashibodi bila kutambuliwa.

**Serikali.** Kanuni za ununuzi, uwazi, na uwajibikaji wa umma huumba bomba. Weka rekodi ghafi zisizobadilika kwa uwezo wa kukaguliwa, ziubadilishe kwa hatua za tabaka zilizojaribiwa, na uhifadhi asili kamili ili mkaguzi aweze kufuatilia takwimu yoyote iliyochapishwa hadi nyaraka zake chanzo, mara nyingi ni sharti la kisheria. Uchakataji wenye kutobadilika thamani unakuruhusu kuchakata upya kipindi cha faili au kuripoti kwa usalama kanuni inapobadilika, na kupendelea miundo wazi na msimbo wa mabadiliko unaohamishika kunakuepusha na kufungwa kwa muuzaji mmoja kuvuka mkataba wa miaka mingi.

## Mifano

**Kampuni changa.** Kampuni changa ya uchanganuzi ya watu kumi ilikuwa imekua na mtandao wa kazi za cron zilizovunjika kimyakimya usiku na wakati mwingine kuhesabu safu mara mbili mhandisi alipoziendesha tena kwa mkono. Timu ilihamia kiunganishi kinachosimamiwa kwa kuingiza, mfumo wa mabadiliko kwa modeli zenye udhibiti wa matoleo, na kiratibu chepesi kinachojaribu tena na kujaza nyuma chenyewe. Walifanya kila modeli iwe na kutobadilika thamani na kuongeza majaribio machache kwa funguo tupu na hesabu za safu, kwa hiyo badiliko baya la chanzo sasa linashindwa kwenye CI badala ya kujitokeza kwenye dashibodi ya mwanzilishi Jumatatu.

**Biashara kubwa.** Muuzaji mkubwa wa rejareja alibadilisha mamia ya hati za uchimbaji za mkono na mrundiko wa ELT. Viunganishi vinavyosimamiwa hutua data chanzo ghafi, mfumo wa mabadiliko hujenga modeli zilizojaribiwa, zenye udhibiti wa matoleo kwenye lakehouse, na kiratibu husimamia utegemezi kwa kujaribu tena na kujaza nyuma. Majaribio ya data hunasa kuteleza kwa skima kutoka mifumo chanzo kabla halijafika kwenye dashibodi. Hifadhi ya safu wima iliyogawanywa ilipunguza gharama za maswali kwa kiasi kikubwa, huku ikiboresha usafi kutoka kila siku hadi kila saa.

**Serikali.** Mamlaka ya kodi inaingiza faili na data ya watu wa tatu kupitia bomba lililotawaliwa linalotua rekodi ghafi zisizobadilika kwa uwezo wa kukaguliwa, kisha kuzibadilisha kwa hatua za tabaka, zilizojaribiwa. Uchakataji wenye kutobadilika thamani unawaruhusu kuchakata upya kwa usalama kipindi cha faili kanuni inapobadilika. Asili kamili inawaruhusu wakaguzi kufuatilia takwimu yoyote iliyokokotolewa hadi nyaraka chanzo, sharti la kisheria kwa uwajibikaji wa umma.

## Kesi ya biashara: sababu, ROI, na TCO

ROI ya uhandisi wa data wenye nidhamu inatokana na kutegemewa, kasi, na udhibiti wa gharama. Mabomba ya kutegemewa yanamaanisha maamuzi na ripoti zinakaa juu ya data ya kuaminika, kwa hiyo unaepuka kazi ghali ya kurekebisha na uharibifu wa sifa wa namba zisizo sahihi. Mabomba ya moduli, yaliyojaribiwa huziruhusu timu kusafirisha bidhaa mpya za data haraka, ikijilimbikiza thamani ya kila uwekezaji wa uchanganuzi na ML wa chini ya mkondo. Kuboresha hifadhi na kokotoo hupunguza moja kwa moja ankara ya wingu, mara nyingi kwa viwango vikubwa ugawaji na mifumo ya maswali inaporekebishwa.

Gharama ya kupokea inajumuisha zana za jukwaa, muda wa kihandisi wa kujenga mabomba ya moduli yaliyojaribiwa, na nidhamu ya kuchukulia data kama programu. Ipime dhidi ya gharama ya kutopokea: kazi dhaifu za kipekee ambazo mwandishi wake tu anazielewa, uharibifu wa data wa kimya unaogunduliwa na watendaji, gharama za wingu zinazovimba kutokana na uchanganuzi kamili wa majedwali, na wachambuzi wanaokwama wakisubiri data. Kwa uongozi, weka uhandisi wa data kama msingi unaofanya uchanganuzi, BI, na AI kuwa wa kuaminika na wa bei nafuu. Ukiwekeza kidogo hapa, unaweka dari kwenye faida ya kila mpango wa data ulio juu yake.

## Mifumo mibaya na mitego

- Mabomba yaliyojengwa kama hati za mara moja bila udhibiti wa matoleo, majaribio, wala mapitio.
- Kazi zisizo na kutobadilika thamani zinazorudia au kuharibu data zinapoendeshwa tena baada ya kushindwa.
- Kupokea kutiririka kwa heshima wakati kundi lingetimiza sharti la ucheleweshaji.
- Kuwatupia wachambuzi majedwali ghafi na kuita kujihudumia.
- Hakuna uonekanaji, kwa hiyo kushindwa kunagunduliwa na watumiaji wa chini ya mkondo.
- Kupuuza ugawaji na ukubwa wa faili hadi ankara ya wingu ilipuke.
- Kuunganisha kuingiza, kubadilisha, na kuhudumia hadi hakuna kinachoweza kubadilika kwa usalama.
- Kufuta data ghafi, kufanya kutowezekana kuchakata upya mantiki inapobadilika.

## Kielelezo cha ukomavu

1. Kuanzisha: Hati za papo hapo na uendeshaji wa mkono, bila majaribio wala ufuatiliaji. Kushindwa kunagunduliwa na watumiaji wa chini ya mkondo, kazi haziwezi kuendeshwa tena kwa usalama, na gharama za wingu hazisimamiwi wala kugawanywa.
2. Kuendeleza: Baadhi ya timu zimepokea kiratibu na kuweka mabadiliko ya msingi kwenye udhibiti wa matoleo, lakini mazoea hayana uthabiti kuvuka shirika. Majaribio ya mara kwa mara yapo, kutobadilika thamani ni pungufu, na mabomba yaliyovunjika bado yanamaanisha kuzima moto kwa kuitikia.
3. Kusawazisha: ELT yenye mfano wa tabaka za maandalizi-msingi-ghala dogo, iliyojaribiwa na yenye udhibiti wa matoleo, ndio kiwango kilichoandikwa kinachotumika kuvuka timu. Utegemezi ulioratibiwa wenye kujaribu tena na kujaza nyuma, majaribio ya data yanayoendeshwa kwenye CI, na mikataba ya pamoja ya uundaji wa skima ya nyota na ugawaji vinatekelezwa shirika zima badala ya kuachwa kwa kila kikundi.
4. Kusimamia: Jukwaa linapimwa na kudhibitiwa. Usafi, kiasi, skima, na usambazaji vinafuatiliwa kwa tahadhari zinazoelekezwa kwa timu zinazomiliki, na SLA za mabomba, muda wa wastani wa kugundua, viwango vya kupita vya ubora wa data, na gharama ya kokotoo kwa kila bomba na kila swali vinafuatiliwa dhidi ya vipimo vya msingi. Vizingiti vya kurudisha nyuma na kuua vinatekelezwa kwa ushahidi, na gharama na kutegemewa vina wamiliki wanaoshikiliwa kwa malengo.
5. Kuratibu: Mabomba yanachukuliwa kikamilifu kama programu yenye CI/CD, mikataba ya data, na ugunduzi wa kiotomatiki wa hitilafu unaonasa kuteleza kabla watumiaji hawajafanya. Mantiki ya kundi na kutiririka inaunganishwa pale ucheleweshaji unalipa kweli, jukwaa linaboreshwa mfululizo na la kujihudumia, na uwezo, ngazi za hifadhi, na gharama vinasawazishwa upya kwa kujirekebisha mizigo inapohama ili bidhaa mpya za data zisafirishwe haraka kwenye msingi thabiti.

## Mawazo ya kujadili

- Katika mrundiko wenu "wakati halisi" unastahili gharama yake wapi kweli, na wapi ni tamanio tu?
- Mabomba yenu yapi hayawezi kuendeshwa tena kwa usalama leo, na ingehitaji nini kurekebisha hilo?
- Sehemu gani ya ankara yenu ya data ya wingu inatokana na uchanganuzi kamili na ugawaji uliokosekana?
- Wachambuzi wenu wanatumia maghala madogo yaliyoumbwa au majedwali ghafi, na hilo linawagharimu nini?
- Muda wenu wa wastani wa kugundua tukio la data ni upi, na nani anaupata kwanza?
- Kuunganisha mantiki ya kundi na kutiririka kungepunguza mzigo wenu wa matengenezo au kuongeza hatari?

## Mambo muhimu ya kukumbuka

- Chukulia mabomba kama programu: udhibiti wa matoleo, majaribio, mapitio, CI/CD, na uonekanaji.
- Pendelea ELT yenye modeli za tabaka, zilizojaribiwa; weka data ghafi kwa kuchakata upya.
- Chagua kundi kwa chaguo-msingi na kutiririka tu pale ucheleweshaji unalipa kweli.
- Fanya mabadiliko yawe na kutobadilika thamani ili kuendesha tena kuwe salama.
- Unda data kwa watumiaji kwa skima za nyota au majedwali mapana ya makusudi.
- Fuatilia usafi, kiasi, skima, na usambazaji, na uchukulie matukio ya data kama hitilafu.
- Boresha miundo ya hifadhi, ugawaji, na gharama ya kokotoo kama mambo ya daraja la kwanza.

## Marejeo na usomaji zaidi

- Joe Reis and Matt Housley, "Fundamentals of Data Engineering."
- Ralph Kimball and Margy Ross, "The Data Warehouse Toolkit."
- Martin Kleppmann, "Designing Data-Intensive Applications."
- Bill Inmon, "Building the Data Warehouse."
- James Densmore, "Data Pipelines Pocket Reference."
- Nathan Marz and James Warren, "Big Data" (Lambda architecture).
- Barr Moses and colleagues, "Data Quality Fundamentals" (data observability).
