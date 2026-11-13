# 7.8 Ubora wa data na uonekanaji

## Muhtasari na msukumo

[Ubora wa data](https://en.wikipedia.org/wiki/Data_quality) ni ufaao kwa matumizi: kiwango ambacho data inahudumia maamuzi, bidhaa, na ripoti zinazoitegemea. Seti ya data si nzuri au mbaya kidhana. Ni nzuri vya kutosha kwa madhumuni, au sivyo. Anwani ya mteja inayofaa kwa hesabu ya masoko inaweza kuwa haifai kwa notisi ya kisheria. Fremu hiyo ni muhimu, kwa sababu inahamisha mazungumzo kutoka "je, data yetu ni kamilifu" (kamwe) hadi "je, data yetu inafaa kwa tunachotaka kufanya nayo" (inayojibika, na inayojaribika). Vipimo vya kawaida ni usahihi, ukamilifu, uthabiti, wakati, uhalali, na upekee, na matatizo mengi halisi hupungua hadi mojawapo.

Hii ndiyo ukweli usiopendeza kwa timu kubwa: data mbaya ni mbaya kuliko hakuna data. Huna data, unajua, na unaendelea kwa tahadhari ipasavyo. Una data isiyo sahihi inayoonekana sahihi, unatenda juu yake kwa imani ya uongo. Data mbaya huharibu kimyakimya. Inatiririka kwenye dashibodi ambayo mtendaji anaiamini, kwenye mfano wa [kujifunza kwa mashine](https://en.wikipedia.org/wiki/Machine_learning) unaofunzwa juu yake na kusimba makosa yake, na kwenye maamuzi ambayo hakuna anayefikiria kuyahoji kwa sababu namba ilikuwa hapo hapo kwenye skrini. Madhara yametawanyika na yamechelewa, ndiyo sababu hasa ni ghali. Mtu anapoona, namba isiyo sahihi tayari imenukuliwa kwenye mfuko wa bodi, faili ya udhibiti, au takwimu ya umma.

Uonekanaji wa data ni nidhamu inayonasa hili kabla ya watumiaji wenu. Ni sambamba ya moja kwa moja ya uonekanaji wa programu na telemetry (sura ya 9.2): silika ileile inayokuambia kufuatilia ucheleweshaji wa maombi na viwango vya makosa inakuambia kufuatilia usafi, kiasi, skima, na usambazaji wa data. Sura hii inajengwa juu ya mkakati wa data na utawala (sura ya 7.1) na uhandisi wa data (sura ya 7.2), na inalisha uundaji wa data na safu ya kisemantiki (sura ya 7.7) na AI ya kuwajibika na ya kuaminika (sura ya 6.5). Kwa mashirika yanayopatanisha mifumo mingi chanzo na serikali zinazochapisha takwimu za kisheria, kuchukulia kutegemewa kwa data kama tatizo la kihandisi lenye wamiliki na viwango vya huduma ndiyo tofauti kati ya uaminifu na marekebisho ya umma ya aibu.

## Kanuni kuu

- Ubora wa data ni ufaao kwa matumizi, si ukamilifu; ufafanue dhidi ya madhumuni.
- Data mbaya ni mbaya kuliko hakuna data, kwa sababu huharibu maamuzi kimyakimya.
- Jaribu data kama unavyojaribu msimbo: madai, matarajio, na ukaguzi wa skima kwenye bomba.
- Mikataba kati ya wazalishaji na watumiaji hufanya matarajio yawe wazi na yatekelezeke.
- Fuatilia usafi, kiasi, skima, na usambazaji, jinsi unavyofuatilia huduma.
- Asili hugeuza "kuna kitu kibaya" kuwa "hiki ndicho kilichovunjika na kinachoathiri."
- Chukulia matukio ya data kama matukio ya uzalishaji, yenye umiliki, ukali, na viwango vya huduma.
- Gundua matatizo yanapoingia, si tabaka tatu chini ya mkondo kwenye dashibodi.

## Mapendekezo

### Fafanua ubora kwa kipimo, na uupime

Malengo yasiyo wazi ya ubora huzalisha matokeo yasiyo wazi. Gawanya ubora katika vipimo vinavyopimika na uambatishe ukaguzi madhubuti kwa kila kimoja. Usahihi unauliza kama thamani zinaakisi uhalisia (je, mapato haya yaliyorekodiwa yanalingana na leja chanzo). Ukamilifu unauliza kama rekodi na nyanja zinazotarajiwa zipo (je, siku zozote zinakosekana, je, safu wima zinazohitajika ni tupu). Uthabiti unauliza kama ukweli ule ule unakubaliana kuvuka mifumo (je, hesabu ya wateja katika fedha inalingana na hesabu kwenye ghala). Wakati unauliza kama data inafika kwa wakati wa kuwa na manufaa (je, data ya jana iko tayari kabla ya ripoti ya asubuhi). Uhalali unauliza kama thamani zinafuata kanuni na umbo (je, misimbo yote ya sarafu ni halisi, je, tarehe ziko ndani ya safu). Upekee unauliza kama vyombo vinaonekana mara moja (je, kuna maagizo yaliyorudiwa yanayovimbisha jumla). Chagua vipimo vinavyojalisha kwa kila seti ya data, weka vizingiti, na uvifuatilie kwa muda. Ubora usioupima ni ubora unaoukisia.

### Jaribu mabomba kwa madai na matarajio

Data inastahili ukali ule ule wa majaribio kama msimbo wa programu. Tumia [uthibitishaji wa data](https://en.wikipedia.org/wiki/Data_validation) kwenye kila hatua: majaribio yanayotegemea madai yanayoshindwa bomba kanuni isiyobadilika inapokiukwa, na majaribio yanayotegemea matarajio yanayotangaza "kawaida" inaonekanaje kwa jedwali na kuweka alama mikengeuko. Dai kwamba funguo za msingi ni za kipekee na si tupu, kwamba funguo za kigeni zinatatuka, kwamba safu wima za kategoria zina thamani zinazokubalika tu, kwamba safu wima za namba ziko ndani ya safu zinazokubalika, na kwamba hesabu za safu zinatua katika bendi inayotarajiwa. Ongeza ukaguzi wa skima unaoshindwa kwa sauti safu wima inapoongezwa, kuondolewa, kubadilishwa jina, au kubadilishwa aina juu ya mkondo. Endesha ukaguzi huu kwenye ujumuishaji endelevu ili badiliko baya linaswe kabla ya kuunganishwa, na uuendeshe tena kwenye uzalishaji dhidi ya data hai ili chanzo kibaya kinaswe kabla hakijawafikia watumiaji. Lengo ni kushindwa mapema na kwa sauti, kwa sababu bomba lililovunjika ni salama kuliko lisilo sahihi kimyakimya.

### Anzisha mikataba ya data kati ya wazalishaji na watumiaji

Matukio mengi ya ubora wa data huanza juu ya mkondo, timu ya uzalishaji inapobadilisha skima, maana ya kisemantiki, au mkataba wa thamani bila kujua nani anaitegemea. [Mkataba wa data](https://en.wikipedia.org/wiki/Data_contract) hurekebisha hili kwa kufanya kiolesura kiwe wazi: skima, semantiki ya kila uga, thamani zinazoruhusiwa, hakikisho za usafi, na mchakato wa kufanya badiliko. Mzalishaji anajitolea kwa mkataba, mtumiaji anajenga dhidi yake, na badiliko linalovunja linahitaji matoleo na notisi badala ya mshangao wa kimyakimya Jumatatu. Tekeleza mikataba kimitambo pale unapoweza, kwa kuthibitisha data inayoingia dhidi ya mkataba mpakani na kukataa au kuweka karantini ukiukaji. Mikataba hugeuza utegemezi wa kimyakimya, dhaifu kuwa wa wazi, uliojadiliwa. Pia hufanya umiliki uonekane, ambayo ni nusu ya vita kwa ukubwa.

### Fuatilia ishara nne za uonekanaji wa data

Uonekanaji wa data hutazama ishara nne, sambamba ya moja kwa moja na jinsi unavyotazama huduma inayoendesha (sura ya 9.2). Usafi: je, data ni ya hivi karibuni kama inavyopaswa, au bomba limekwama. Kiasi: je, hesabu ya safu iko katika safu inayotarajiwa, au jedwali lilifika nusu tupu au lilipakiwa mara mbili. Skima: je, muundo umebadilika bila kutarajiwa. Usambazaji: je, thamani zenyewe zimeteleza, kiasi kwamba safu wima iliyokuwa na asilimia 2 tupu sasa ina asilimia 40 tupu, au wastani umehama kwa njia inayoashiria hitilafu ya juu ya mkondo. Weka vifaa vya kupima ishara hizi kwenye majedwali yenu muhimu, jifunze mifumo yao ya kawaida, na utoe tahadhari ukiukaji. Hivi ndivyo unavyobadilisha "mtendaji aliona dashibodi inaonekana vibaya" na "timu inayomiliki ilipigiwa simu pale kushindwa kulipotokea." Kigunduzi kibaya zaidi cha tatizo la data ni binadamu wa chini ya mkondo anayeamini namba.

### Ongeza ugunduzi wa hitilafu, lakini urekebishe dhidi ya uchovu wa tahadhari

Vizingiti tuli hunasa kushindwa kuliko dhahiri. Kwa kuteleza kwa hila zaidi, ongeza [ugunduzi wa hitilafu](https://en.wikipedia.org/wiki/Anomaly_detection) unaojifunza mfumo wa msimu wa kawaida wa kila kipimo na kuweka alama mikengeuko isiyo ya kawaida kitakwimu, ili unase uvujaji polepole kabla haujawa mafuriko. Kuwa na nidhamu kuhusu hili. Tahadhari zenye kelele za hitilafu huwazoeza watu kupuuza tahadhari, jambo baya kuliko hakuna tahadhari. Anza na majedwali yako ya thamani ya juu zaidi, toa tahadhari tu kwa mambo ambayo binadamu anapaswa kutenda, elekeza kila tahadhari kwa mmiliki aliyetajwa, na urekebishe bila huruma. Tahadhari ambayo hakuna anayeitendea kazi ni hitilafu katika ufuatiliaji wako, si kipengele.

### Fuatilia asili kwa uchambuzi wa athari na chanzo

Kitu kinapovunjika, maswali mawili yanajalisha mara moja: nini kilisababisha, na kinaathiri nini. [Asili ya data](https://en.wikipedia.org/wiki/Data_lineage) hujibu yote mawili kwa kuchora jinsi data inavyotiririka kutoka chanzo kupitia kila mabadiliko hadi kila jedwali la chini ya mkondo, dashibodi, na mfano. Kwa chanzo cha tatizo, unafuatilia takwimu mbaya juu ya mkondo hadi mabadiliko au chanzo kilichoileta. Kwa uchambuzi wa athari, unafuatilia mbele kuona kila mtumiaji aliyeguswa na upakiaji mbaya, ili uwaarifu na kuweka karantini madhara kabla hayajaenea. Nasa asili kiotomatiki kutoka zana zako za kubadilisha na kuratibu badala ya kudumisha mchoro kwa mkono, kwa sababu mchoro wa mkono si sahihi siku baada ya kuuchora. Katika mashirika yenye vyanzo vingi, chapisha asili kwenye orodha ya data ili mtumiaji yeyote aone uga ulitoka wapi na auamini ipasavyo.

### Chukulia matukio ya data kama matukio ya uzalishaji

Mazoea yanayoweka huduma za kutegemewa yanatumika moja kwa moja kwa data. Mpe kila seti muhimu ya data mmiliki. Fafanua viwango vya ukali kwa "muda wa kusimama kwa data," vipindi data inapokosekana, kuwa si sahihi, au kuchelewa. Weka viwango vya huduma: malengo ya usafi, bajeti ya makosa inayokubalika, na muda lengwa wa kugundua na kutatua. Weka mizunguko ya simu ya dharura ya data nyuma ya mabomba muhimu zaidi, andika vitabu vya mwongozo, na uendeshe tathmini zisizo na lawama baada ya matukio ili kushindwa kuleule kisirudie. Jedwali la malipo likichelewa au kipimo cha umma kikiwa si sahihi, hilo ni tukio, na linastahili uzito ule ule kama hitilafu. Hii ndiyo mabadiliko ya kitamaduni yanayofanya zana zote zilipe.

### Fanya uchambuzi wa wasifu na upatanisho mfululizo

Uchambuzi wa wasifu unamaanisha kuchunguza umbo la data yako mara kwa mara: usambazaji wa thamani, viwango vya thamani tupu, wingi wa kipekee, kiwango cha chini na cha juu, na mifumo ya umbo. Unafichua matatizo ambayo hukufikiria kudai, na unakuambia "kawaida" inaonekanaje ili uweze kuweka matarajio mazuri. Upatanisho unamaanisha kukagua kwamba vyanzo huru vinakubaliana: je, jumla ya ghala inalingana na mfumo chanzo rasmi, je, jumla ya sehemu ni sawa na kizima. Otomatisha upatanisho kati ya mifumo muhimu na utoe tahadhari kutofautiana, kwa sababu kuvunjika kwa upatanisho mara nyingi ni ishara ya mapema na wazi zaidi kwamba kitu cha juu ya mkondo kilienda vibaya.

## Mabadilishano: faida na hasara

| Mbinu | Faida | Hasara | Inafaa zaidi |
|---|---|---|---|
| Majaribio ya madai (kushindwa kigumu) | Husimamisha data mbaya papo hapo, kanuni zisizobadilika wazi | Inaweza kuzuia mabomba kwa masuala madogo | Funguo muhimu, uadilifu wa marejeo |
| Majaribio ya matarajio (alama laini) | Hunasa kuteleza, si dhaifu kupita kiasi | Inahitaji kurekebishwa, inaweza kupuuzwa | Usambazaji, bendi za kiasi |
| Mikataba ya data | Huzuia mshangao wa juu ya mkondo, umiliki wazi | Mzigo wa uratibu na utawala | Mipaka ya mzalishaji au mtumiaji kuvuka timu |
| Ugunduzi wa hitilafu | Hunasa kuteleza kwa hila, kusiotarajiwa | Uchovu wa tahadhari, chanya za uongo | Majedwali ya thamani ya juu, vipimo vya msimu |
| Ukaguzi wa doa wa mkono | Nafuu kuanza, hakuna zana | Haipanuki, hukosa makosa ya kimya | Hatua ya mwanzo kabisa tu |
| Jukwaa kamili la uonekanaji | Ufikiaji mpana, asili, tahadhari | Gharama, usanidi, mfumo mwingine wa kuendesha | Vyanzo vingi, kuripoti kunakodhibitiwa |

Mvutano wa msingi ni ufikiaji dhidi ya kelele. Usipoweka vifaa vya kupima chochote matatizo yanawafikia watumiaji wenu kwanza, jambo linaloharibu uaminifu. Ukiweka kila kitu kwa tahadhari za kuwaka haraka unazamisha timu yako kwa chanya za uongo hadi inanyamazisha kituo, jambo ambalo pia linaruhusu matatizo kuwafikia watumiaji. Tatua kwa kupanga data yako kwa eneo la mlipuko. Majedwali yanayolisha vipimo vya bodi, bidhaa zinazomkabili mteja, ripoti za udhibiti, na mifano ya kujifunza kwa mashine yanapata matibabu kamili: mikataba, madai magumu, uonekanaji, na umiliki wa simu ya dharura. Mkia mrefu wa majedwali ya uchunguzi unapata uchambuzi wa wasifu wa mwanga. Tumia bajeti yako ya kutegemewa pale data isiyo sahihi ingeumiza zaidi, na uwe mwangalifu kwa makusudi kila mahali pengine.

## Maswali ya kujadili na timu yako

1. **Data mbaya inapofika kwenye uzalishaji, nani anagundua kwanza, na kwa njia gani?** Hili ndilo swali linalofichua zaidi kuhusu kutegemewa kwa data yenu, kwa sababu jibu la uaminifu kwa kawaida ni "mtumiaji, kwa bahati mbaya." Kama mchambuzi, mtendaji, au mteja ndiye mfumo wenu wa ugunduzi, muda wenu wa wastani wa kugundua unapimwa kwa siku na sifa yenu inapata pigo kila mara. Mbadala ni vifaa vya kupima vinavyoipigia simu timu inayomiliki pale kushindwa kunapotokea, kabla namba mbaya haijaenea. Leta namba halisi: matukio mangapi kati ya kumi ya mwisho ya data yalinaswa na ufuatiliaji dhidi ya kuripotiwa na binadamu wa chini ya mkondo, na kila moja ilikaa bila kugunduliwa kwa muda gani. Jibu linakuambia kama mna uonekanaji au matumaini tu, na linapaswa kuendesha moja kwa moja mahali pa kuwekeza kwanza kwenye ukaguzi wa usafi, kiasi, skima, na usambazaji.

2. **Seti zipi za data zina mmiliki, mkataba, na kiwango cha huduma, na zipi ni yatima?** Kwa ukubwa, kushindwa kwingi kwa ubora wa data kunarejea kwenye kiolesura kisicho na mmiliki: timu ya uzalishaji ilibadilisha kitu bila kujua nani anakitegemea, kwa sababu hakuna mkataba uliosema hivyo. Umiliki ndio msingi unaofanya mikataba, njia za tahadhari, na jibu la tukio kuwezekana, na seti za data yatima ndipo uharibifu wa kimya unapoishi. Pitia majedwali yenu muhimu zaidi na uliza, kwa kila moja, nani anawajibika, mzalishaji amejitolea nini, na usafi na usahihi gani watumiaji wameahidiwa. Leta asili yenu: majedwali yenye eneo kubwa zaidi la mlipuko la chini ya mkondo ndiyo yanayohitaji hili zaidi na mara nyingi ndiyo yanayokosa. Pengo kati ya "muhimu" na "inamilikiwa" ndiyo orodha yenu ya kipaumbele kwa robo ijayo.

3. **Gharama halisi ya tukio la ubora wa data kwetu ni ipi, na je, tunalichukulia ipasavyo?** Timu huwekeza kidogo kwenye ubora wa data kwa sababu gharama ya data mbaya imetawanyika na imechelewa, kwa hiyo haionekani kamwe kama mstari wa bidhaa, wakati gharama ya kujenga zana za ubora ni madhubuti na ya papo hapo. Ibadilishe kwa kupima bei ya tukio halisi mwanzo hadi mwisho: uamuzi mbaya, kazi ya kurudia, saa za wahandisi zilizotumika kufuatilia chanzo bila asili, uaminifu uliomomonyoka unaowafanya watu kujenga upya kimyakimya seti zao za data za kivuli, na, katika mazingira yanayodhibitiwa au yanayomkabili umma, notisi ya marekebisho na uharibifu wake wa sifa. Leta mfano mahususi wa mwaka uliopita na uujumlishe kwa uaminifu. Kushindwa kimya kimoja kwenye bomba la malipo au takwimu za umma kungegharimu zaidi ya mwaka wa zana za uonekanaji, kesi ya biashara inajitengenezea yenyewe, na mazungumzo yanahama kutoka kama kuwekeza hadi wapi.

4. **Tumepanga seti zetu za data kwa eneo la mlipuko, na je, uwekezaji wetu wa ufuatiliaji unafuata mpangilio huo kweli?** Njia kuu ya kushindwa kwa ukubwa ni kutumia juhudi ya kutegemewa kwa usawa, kwa hiyo jedwali la uchunguzi ambalo hakuna anayeliamini linapata umakini ule ule kama lile linalolisha vipimo vya bodi, huku tahadhari ya kuwaka haraka kwenye jedwali la thamani ndogo ikiwazoeza watu kunyamazisha kituo kinachobeba pia simu muhimu. Huwezi kuweka vifaa vya kupima kila kitu bila kuzama kwenye kelele, na huwezi kuweka kitu chochote bila kuacha matatizo yawafikie watumiaji kwanza, kwa hiyo uamuzi halisi ni mahali matibabu kamili (mikataba, madai magumu, uonekanaji, na umiliki wa simu ya dharura) yanapoenda na mahali uchambuzi wa wasifu wa mwanga unatosha. Leta orodha ya majedwali yenu yaliyowekewa lebo kwa kinachoyategemea: vipimo vya bodi, bidhaa zinazomkabili mteja, ripoti za udhibiti, na mifano ya kujifunza kwa mashine, kisha ulinganishe mpangilio huo na mahali ukaguzi na tahadhari zenu zilipo leo. Kwa shirika linalopatanisha vyanzo vingi au serikali inayochapisha takwimu za kisheria, majedwali yenye mfiduo wa kisheria au wa umma yanastahili juu ya orodha, na pengo lolote kati ya "ingeumiza zaidi isipokuwa sahihi" na "inafuatiliwa zaidi" ni kosa la kuweka vipaumbele la kurekebisha sasa.

5. **Mifano gani ya kujifunza kwa mashine na uchanganuzi unaamua juu ya data tusiyothibitisha kamwe, na makosa gani yanaweza kuwa yanasimba kimyakimya?** Dashibodi inaonyesha namba isiyo sahihi kwa binadamu mmoja ambaye anaweza kuihoji, lakini mfano hufunzwa kwa vipengele visivyo sahihi na husimba makosa hayo kwenye kila utabiri unaofanya, kwa ukubwa na uficho unaofanya madhara kuwa magumu zaidi sana kuona au kutendua. Shinikizo linaloshindana ni kasi: timu za sayansi ya data zinataka kusonga haraka kwenye vipengele vipya, na kuongeza uthibitishaji, mikataba, na hakikisho za usafi kwa kila mlisho kunahisi kama msuguano hadi mfano uzorote kimyakimya kwa sababu safu wima ya juu ya mkondo iliteleza. Leta orodha ya mifano na uchanganuzi wenu wa uzalishaji, seti za data ambazo kila moja inatumia, na alama ya uaminifu ya mlisho upi una majaribio, mikataba, na uonekanaji dhidi ya upi haulindwi. Katika mazingira ya shirika au serikali ambapo mfano unaathiri mkopo, manufaa, au utekelezaji, data ya mafunzo isiyothibitishwa inakuwa dhima ya ukaguzi na haki juu ya hatari ya ubora, kwa hiyo swali la milisho ipi inaweka lango la toleo la mfano linapaswa kuwa na mmiliki na jibu lililoandikwa (sura ya 6.5).

6. **Hitilafu ya ubora inapojitokeza wiki baada ya tukio, tunaweza kuchakata upya na kupatanisha kweli, au tumeshatupa tunachohitaji?** Kushindwa kwingi kwa ubora hakuonekani wakati wa kupakia na kunakuwa wazi baadaye tu, kuvunjika kwa upatanisho au mwelekeo wa kutia shaka unapomsukuma mtu kutazama, na wakati huo uwezo wa kurekebisha kwa usafi unategemea chaguo ulizofanya mapema zaidi: kama ulihifadhi rekodi ghafi zisizobadilika, kama vyanzo huru vinaweza kupatanishwa, na kama asili inakuruhusu kufuatilia takwimu mbaya hadi asili yake. Mvutano ni gharama na urahisi dhidi ya uwezo wa kuzalisha upya, kwa sababu kuhifadhi data ghafi na kuendesha upatanisho endelevu kati ya mifumo si bure, na ni rahisi kufuta ingizo ghafi mara majedwali yaliyobadilishwa yanapoonekana sawa. Leta sera yenu ya uhifadhi na kutobadilika kwa data ghafi, orodha ya jozi muhimu za mifumo mnazopatanisha kiotomatiki, na mfano halisi wa hitilafu mliyoweza au msioweza kutoka kwayo kwa kuchakata upya. Kwa wakala wa serikali chini ya wajibu wa kisheria wa kufuatilia takwimu yoyote iliyochapishwa hadi rekodi chanzo, au shirika linalokabiliwa na usahihishaji wa udhibiti, data ghafi isiyobadilika na upatanisho wa kiotomatiki si usafi wa hiari bali utaratibu unaofanya marekebisho kuweza kutetewa.

## Mtazamo wa sekta

**Kampuni changa.** Kasi na uaminifu vinajalisha zaidi ya ufikiaji. Weka majaribio machache mepesi kwenye zana yako ya mabadiliko (upekee na isiyo tupu kwenye funguo, thamani zinazokubalika kwenye safu wima zinazobeba maana, bendi ya hesabu ya safu kwa kila chanzo), na uongeze ufuatiliaji wa usafi na kiasi kwenye majedwali machache yanayolisha vipimo vya kampuni tu. Elekeza kila tahadhari kwenye kituo kimoja anachomiliki mhandisi mmoja, na upinge kununua jukwaa la uonekanaji kabla ya kuwa na majedwali au timu ya kuhalalisha. Lengo ni kugundua uga uliowekewa lebo vibaya kabla haujavimbisha namba ambayo waanzilishi wananukuu, si kuweka vifaa vya kupima kila kitu.

**Biashara ndogo.** Bila mhandisi wa data na bajeti finyu, egemea vipengele vya ubora vilivyojengwa tayari kwenye ghala, zana ya BI, au majukwaa ya SaaS unayolipia badala ya kusimamisha mrundiko tofauti. Elekeza juhudi yako kwenye namba chache zinazoendesha maamuzi kweli (mapato, bomba la mauzo, hesabu ya bidhaa), zikague dhidi ya chanzo huru kwa mzunguko wa kawaida, na uchukulie tahadhari za muuzaji za usafi na skima kama za kutosha zinapokuwepo. Kununua ubora uliopachikwa kwenye zana unazoendesha tayari kunashinda kujenga bomba ambalo huna wa kulidumisha.

**Biashara kubwa.** Tatizo ni kutegemewa kuvuka timu nyingi na maelfu ya majedwali, kwa hiyo sawazisha kiolesura: mikataba ya data kwenye kila mpaka wa mzalishaji, jukwaa la uonekanaji linalotazama usafi, kiasi, skima, na usambazaji, na asili iliyochapishwa kwenye orodha kwa uchambuzi wa athari. Panga seti za data kwa eneo la mlipuko, weka ugunduzi wa hitilafu na umiliki wa simu ya dharura kwenye zile za thamani ya juu, na uendeshe matukio ya data kupitia mchakato ule ule wa ukali na tathmini ya baada ya tukio kama hitilafu za huduma. Viwango vya huduma kwenye mabomba yanayolisha ripoti za udhibiti na dashibodi za watendaji hugeuza kutegemewa kwa data kutoka matamanio hadi ahadi iliyopimwa, inayotawaliwa.

**Serikali.** Usahihi wa kisheria na uwajibikaji wa umma huweka kiwango: weka rekodi ghafi zisizobadilika za utafiti na utawala, zibadilishe kwa hatua za tabaka, zilizojaribiwa, na upatanishe dhidi ya jumla za chanzo kwa kila hatua. Hifadhi asili kamili ili takwimu yoyote iliyochapishwa ifuatiliwe hadi rekodi chanzo kwa ukaguzi, na uweke lango la kila toleo nyuma ya uthibitishaji wa uhalali, ukamilifu, na uthabiti dhidi ya vipindi vya awali. Ununuzi wa zana unapaswa kudai uwazi na uhamishaji wa data, na takwimu ya umma isiyo sahihi lazima ishughulikiwe kama tukio zito, kwa uzito ule ule ambao uaminifu wa umma kwa takwimu rasmi unadai.

## Mifano

**Kampuni changa.** Kampuni ya watu ishirini inaendesha mikakati yake ya kwenda sokoni kwenye ghala linalolishwa na matukio ya bidhaa na mtoa huduma wa malipo. Mapema, uga wa sarafu uliowekewa lebo vibaya ulivimbisha kimyakimya mapato yaliyoripotiwa kwa wiki mbili kabla ya mtu yeyote kuona, jambo lililotikisa uaminifu wa timu kwa kila dashibodi. Walijibu kwa seti nyepesi ya majaribio kwenye zana yao ya mabadiliko: upekee na isiyo tupu kwenye funguo, ukaguzi wa thamani zinazokubalika kwenye safu wima za sarafu na hali, na bendi ya hesabu ya safu kwa kila chanzo. Waliongeza ufuatiliaji wa msingi wa usafi na kiasi kwenye majedwali machache yanayolisha vipimo vya kampuni, ukielekezwa kwenye kituo kimoja cha Slack anachomiliki mhandisi mmoja. Ni wa wastani, lakini unanasa kushindwa kunakojalisha, na waanzilishi wanaamini namba tena.

**Biashara kubwa.** Benki ya kimataifa inapatanisha data ya wateja na miamala kuvuka mifumo kadhaa chanzo kuwa ghala lililotawaliwa linalolisha ripoti za udhibiti, mifano ya hatari, na dashibodi za watendaji. Inaendesha mikataba ya data kwenye kila mpaka wa mzalishaji, kwa hiyo badiliko la skima la juu ya mkondo linawekewa matoleo na kujadiliwa badala ya kurushiwa watumiaji. Jukwaa la uonekanaji linafuatilia usafi, kiasi, skima, na usambazaji kuvuka maelfu ya majedwali, likiwa na ugunduzi wa hitilafu kwenye zile za thamani ya juu na asili iliyochapishwa kwenye orodha ya data kwa uchambuzi wa athari. Matukio ya data yanafuata mchakato ule ule wa ukali na simu ya dharura kama hitilafu za huduma, yenye viwango vya huduma kwenye mabomba yanayolisha mawasilisho ya udhibiti. Mfumo chanzo unapoteleza, timu inayomiliki inapigiwa simu na ripoti za chini ya mkondo zilizoathirika zinajulikana ndani ya dakika, si kugunduliwa na mdhibiti.

**Serikali.** Wakala wa kitaifa wa takwimu unachapisha viashiria vya kiuchumi ambavyo masoko, watunga sera, na umma wanaviona kama vyenye mamlaka, kwa hiyo usahihi ni wajibu wa kisheria na kila takwimu iliyochapishwa lazima ikaguliwe. Mabomba yake yanatua rekodi ghafi zisizobadilika za utafiti na utawala, kisha kuzibadilisha kwa hatua za tabaka, zilizojaribiwa, zenye upatanisho dhidi ya jumla za chanzo kwa kila hatua. Asili kamili inawaruhusu wachambuzi kufuatilia namba yoyote iliyochapishwa hadi rekodi chanzo, ambayo ni zana ya ubora na sharti la kisheria. Kabla ya toleo, takwimu hupita malango ya uthibitishaji wa uhalali, ukamilifu, na uthabiti dhidi ya vipindi vya awali, na hitilafu yoyote huchunguzwa na kuandikwa badala ya kuchapishwa. Takwimu ya umma isiyo sahihi ni tukio zito, kwa hiyo wakala unachukulia muda wa kusimama kwa data kwa uzito ambao uaminifu wa umma unadai.

## Kesi ya biashara: sababu, ROI, na TCO

Faida ya ubora wa data na uonekanaji inatokana na uaminifu uliohifadhiwa, matukio yaliyofupishwa, na maamuzi mabaya yaliyoepukwa. Data ya kuaminika ndiyo msingi unaofanya kila uwekezaji wa chini ya mkondo katika uchanganuzi, akili ya biashara, na AI ulipe kweli, kwa sababu mfano au dashibodi ni nzuri kadiri data iliyo chini yake. Ukaguzi wa ubora unaponasa upakiaji mbaya mpakani, unaepuka gharama kubwa zaidi sana ya namba isiyo sahihi kufika kwenye uamuzi, mteja, au faili. Asili hupunguza uchunguzi wa chanzo kutoka siku za kufuatilia kwa mkono hadi dakika, ambayo ni muda wa kihandisi uliorejeshwa tupu. Uonekanaji hupunguza muda wa wastani wa kugundua kutoka "mtumiaji anapolalamika" hadi "bomba linaposhindwa," ambapo uharibifu mwingi wa uaminifu unaepukwa.

Jumla ya gharama ya umiliki inajumuisha zana za kujaribu, kuonekana, na kuorodhesha, pamoja na muda wa kihandisi wa kuweka vifaa vya kupima kwenye mabomba na kazi ya kishirika ya kugawa wamiliki na kuandika mikataba. Hii ni halisi, lakini ipime dhidi ya gharama ya kutofanya: uharibifu wa kimya unaogunduliwa na watendaji, mifano ya kujifunza kwa mashine iliyofunzwa kwa vipengele vibaya inayosimba makosa kwa ukubwa, wachambuzi wanaojenga upya kimyakimya seti za data za kivuli kwa sababu hawazamini tena rasmi, na, katika mazingira yanayodhibitiwa au ya umma, notisi za marekebisho zinazoharibu sifa kwa miaka. Kwa uongozi, weka ubora wa data kama bima kwenye kila uamuzi unaoendeshwa na data unaofanywa na shirika. Malipo ni ya wastani na yanatabirika. Hasara isiyo na bima, namba moja isiyo sahihi ya hadhi ya juu, si hivyo.

## Mifumo mibaya na mitego

- Kuchukulia ubora wa data kama mradi wa usafishaji wa mara moja badala ya mazoea endelevu ya kihandisi.
- Kugundua kushindwa kutoka kwa watumiaji wa chini ya mkondo badala ya ufuatiliaji pale kushindwa kunapotokea.
- Hakuna umiliki wa seti za data, kwa hiyo hakuna anayewajibika kitu kinapovunjika na hakuna anayepigiwa simu.
- Wazalishaji wakibadilisha skima au semantiki bila mkataba, kuvunja kimyakimya kila mtumiaji.
- Tahadhari za hitilafu zenye kelele sana hadi timu inanyamazisha kituo na kukosa tukio halisi.
- Kulisha data isiyothibitishwa moja kwa moja kwenye mifano ya kujifunza kwa mashine, kusimba makosa kwa ukubwa (sura ya 6.5).
- Kudumisha asili kama mchoro uliochorwa kwa mkono usio sahihi siku baada ya kuuchora.
- Kufukuzia data kamilifu kila mahali badala ya ubora unaofaa matumizi kwenye majedwali yanayojalisha.
- Kufuta data ghafi, kwa hiyo huwezi kuchakata upya au kupatanisha hitilafu ya ubora inapojitokeza baadaye.

## Kielelezo cha ukomavu

- **Ngazi ya 1, Kuanzisha:** Ubora si kazi ya mtu. Matatizo yanapatikana na watumiaji, kwa kawaida baada ya namba isiyo sahihi kufika kwenye ripoti. Hakuna majaribio, hakuna ufuatiliaji, hakuna umiliki. Marekebisho ni ya mkono ya kuzima moto, na kushindwa kuleule kunarudi.
- **Ngazi ya 2, Kuendeleza:** Baadhi ya timu huongeza majaribio ya msingi kwenye majedwali yao muhimu (funguo, thamani tupu, thamani zinazokubalika) na ufuatiliaji kidogo wa usafi na kiasi kwenye seti za data wanazojali zaidi. Mazoea yanafanya kazi pale yalipo, lakini ufikiaji na ukali hutofautiana kwa timu, hakuna kilichosawazishwa, na matukio bado yanashughulikiwa kwa kuitikia.
- **Ngazi ya 3, Kusawazisha:** Vipimo vya ubora vimefafanuliwa kwa vizingiti, na matarajio yaleyale yanatumika kuvuka timu badala ya kutegemea nani alijenga bomba. Mikataba ya data inatawala mipaka muhimu ya wazalishaji, uonekanaji unafunika usafi, kiasi, skima, na usambazaji kwenye majedwali muhimu, na asili inaunga mkono uchambuzi wa athari. Kila seti muhimu ya data ina mmiliki aliyetajwa, na matukio ya data yanafuata mchakato ulioandikwa wa ukali na jibu shirika zima.
- **Ngazi ya 4, Kusimamia:** Ubora na kutegemewa vinapimwa na kudhibitiwa dhidi ya vipimo vya msingi. Muda wa kusimama kwa data unafuatiliwa kwa vipimo halisi: muda wa wastani wa kugundua, muda wa wastani wa kutatua, usafi na usahihi dhidi ya viwango vya huduma vilivyokubaliwa, na bajeti za makosa ambazo seti ya data inaweza kutumia kabla ya kuchochea hatua. Viwango vya kuvunjika kwa upatanisho, viwango vya kupita vya majaribio, na viwango vya chanya za uongo za hitilafu vinafuatiliwa kwa muda, tahadhari zinarekebishwa dhidi ya namba hizo badala ya kubahatisha, na maamuzi ya kwenda au kutokwenda juu ya toleo la data yanafanywa kwa ubora uliopimwa dhidi ya kipimo cha msingi badala ya matumaini.
- **Ngazi ya 5, Kuratibu:** Ubora na uonekanaji vimeenea, vimeotomatishwa, na vinajirekebisha. Ugunduzi wa hitilafu hunasa kuteleza kwa hila, mikataba inatekelezwa kimitambo, na asili inanaswa kiotomatiki na kuchapishwa kwenye orodha. Data ina viwango vya huduma na umiliki wa simu ya dharura kama huduma za uzalishaji, upatanisho unaendeshwa mfululizo, na tathmini zisizo na lawama zinalisha kupunguza kwa kasi muda wa kusimama kwa data. Ubora umeunganishwa na utawala wa data, kujifunza kwa mashine, na upangaji wa biashara, na shirika mfululizo linapanua upya vizingiti, ufikiaji, na umiliki mandhari ya data inapohama.

## Mawazo ya kujadili

1. Majedwali yenu yapi yangesababisha madhara makubwa zaidi yakiwa si sahihi kimyakimya kwa wiki, na je, hayo ndiyo mnayoyafuatilia zaidi?
2. Mkataba wa data ungezuia wapi tukio lenu la mwisho lililosababishwa na juu ya mkondo, na kwa nini hakukuwa na mmoja?
3. Uchunguzi wa kawaida wa chanzo unachukua muda wa kihandisi kiasi gani leo, na asili ya kiotomatiki ingeokoa kiasi gani?
4. Mifano yenu yoyote ya kujifunza kwa mashine inafunzwa kwa data msiyoithibitisha, na makosa gani inaweza kuwa inasimba?
5. Tahadhari zenu zimerekebishwa vizuri vya kutosha ili watu watende kwa kila moja, au yeyote ameshanyamazisha kituo?
6. Viwango vipi vya huduma vya usafi na usahihi watumiaji wenu muhimu zaidi wangekubali kweli, na mngeweza kuvitimiza leo?

## Mambo muhimu ya kukumbuka

- Ubora wa data ni ufaao kwa matumizi kuvuka usahihi, ukamilifu, uthabiti, wakati, uhalali, na upekee.
- Data mbaya ni mbaya kuliko hakuna data, kwa sababu huharibu maamuzi na mifano kimyakimya.
- Jaribu data kama msimbo: majaribio ya madai na matarajio pamoja na ukaguzi wa skima, kwenye CI na kwenye uzalishaji.
- Tumia mikataba ya data kufanya matarajio ya mzalishaji na mtumiaji yawe wazi na yatekelezeke.
- Fuatilia usafi, kiasi, skima, na usambazaji, sambamba na uonekanaji wa programu (sura ya 9.2).
- Nasa asili kwa chanzo cha haraka na uchambuzi wa athari, na uichapishe kwa watumiaji.
- Chukulia matukio ya data kama matukio ya uzalishaji, yenye umiliki, ukali, na viwango vya huduma.
- Weka vifaa vya kupima pale data isiyo sahihi inapoumiza zaidi; lenga ubora unaofaa matumizi, si ukamilifu kila mahali.

## Marejeo na usomaji zaidi

- Barr Moses, Lior Gavish, and Molly Vorwerck, "Data Quality Fundamentals."
- Jacek Majchrzak, Sven Balnojan, and Marian Siwiak, "Data Contracts."
- Danette McGilvray, "Executing Data Quality Projects."
- Thomas C. Redman, "Data Driven: Profiting from Your Most Important Business Asset."
- Laura Sebastian-Coleman, "Measuring Data Quality for Ongoing Improvement."
- Joe Reis and Matt Housley, "Fundamentals of Data Engineering."
- DAMA International, "DAMA-DMBOK: Data Management Body of Knowledge."
- ISO/IEC 25012, "Data quality model."
