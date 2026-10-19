# 7.7 Uundaji wa data na safu ya kisemantiki

## Muhtasari na msukumo

[Mfano wa data](https://en.wikipedia.org/wiki/Data_model) ni uamuzi kuhusu data yako inamaanisha nini, unaofanywa kabla ya kuamua data inakaa wapi. Unataja vitu ambavyo biashara yako inajali, sifa zinazovielezea, na uhusiano kati yake. Hifadhi, faharasa, miundo ya faili, na injini za maswali vyote huja baadaye. Mpangilio huu ni muhimu kwa sababu maana ya data yako inadumu kuliko kila teknolojia unayoitumia kuishikilia. Maghala hubadilishwa, miundo ya jedwali hubadilika, na injini za maswali huja na kuondoka, lakini "mteja," "agizo," na "mtumiaji hai" lazima vimaanishe kitu kilekile kuvuka yote, kwa miaka.

Kwa timu ndogo, uundaji mara nyingi hautamkwi. Mhandisi mmoja anashikilia skima nzima kichwani mwake, na uelewa wa pamoja wa "mapato" unaokoka kwa sababu kuna watu watatu tu wa kutokubaliana. Kwa ukubwa wa mashirika makubwa ya wasanidi, mashirika, na mawakala wa serikali, kutokuwa rasmi huko kunaporomoka hasa kama ilivyoelezwa katika sura ya 7.1 (mkakati wa data na utawala). Timu kadhaa hujenga mamia ya majedwali, kila moja ikiwa na wazo lake la "kikao" ni nini au mtumiaji anapohesabiwa "hai." Dashibodi mbili zinaonyesha namba mbili tofauti kwa wiki ileile, na mkutano wa uongozi unageuka mabishano ya hoja ya nani ni sahihi badala ya cha kufanya baadaye. Uundaji mbaya hautangazi. Unajitokeza miezi baadaye kama kazi ya upatanisho, ukaguzi ulioshindwa, na maamuzi yaliyofanywa kwa takwimu ambazo hakuna anayeweza kuzitetea.

Sura hii inahusu kufanya kazi hiyo kwa makusudi. Inashughulikia mifano ya kidhana, ya kimantiki, na ya kimwili; uundaji wa uhusiano wa vyombo; lini kufanya kawaida na lini kutofanya; jinsi uundaji unavyotofautiana kwa mizigo ya miamala dhidi ya uchanganuzi; uundaji wa vipimo wenye ukweli na vipimo; na safu ya kisemantiki inayoshikilia fasili moja iliyotawaliwa ya kila kipimo cha biashara. Faida si uzuri kwa ajili yake yenyewe. Ni kwamba "mtumiaji hai" na "mapato" yanamaanisha kitu kimoja kila mahali, kwa hiyo timu zenu zinaweza kuamini namba na kusonga haraka kwa sababu hiyo.

*Angalia pia:* sura ya 3.4 (usanifu wa data na uhifadhi), sura ya 7.3 (uchanganuzi na akili ya biashara), na sura ya 11.5 (viashiria muhimu vya utendaji).

## Kanuni kuu

- Amua data inamaanisha nini kabla ya kuamua inakaa wapi.
- Unda katika ngazi tatu: kidhana (biashara), kimantiki (muundo), kimwili (utekelezaji).
- Fanya kawaida kulinda usahihi katika mifumo ya miamala; kataa kawaida kwa makusudi kwa kasi ya uchanganuzi.
- Linganisha mfano na mzigo wa kazi: miamala na uchanganuzi vina mahitaji kinyume.
- Kila kipimo cha biashara kina fasili moja tu iliyotawaliwa, na inaishi kwenye safu ya kisemantiki.
- Vipimo vinavyolingana huruhusu timu huru kuunganisha na kulinganisha data kwa usalama.
- Chembe ni uamuzi wa usanifu unaoufanya kwa makusudi, si ajali ya swali.
- Mifano ni mali hai: yataje vizuri, yaandike, na uyaweke yakibadilika.

## Mapendekezo

### Unda katika ngazi tatu, kwa mpangilio

Fanya kazi kutoka maana kuelekea nje. Anza na mfano wa kidhana: vyombo ambavyo biashara yako inajali na jinsi vinavyohusiana, vilivyoandikwa kwa lugha rahisi ambayo mtaalamu wa eneo anaweza kuikagua. "Mteja huweka maagizo mengi; agizo lina mistari mingi ya vitu; kila mstari wa kitu unarejelea bidhaa moja." Hakuna funguo, aina, wala majedwali bado. Kisha jenga mfano wa kimantiki unaoongeza muundo: sifa, funguo za msingi na za kigeni, wingi wa uhusiano, na vikwazo, bado bila kutegemea hifadhidata mahususi. [Uundaji wa uhusiano wa vyombo](https://en.wikipedia.org/wiki/Entity%E2%80%93relationship_model) ndio nukuu ya kawaida hapa, na mchoro wa uhusiano wa vyombo ndio mabaki unayopitia na wahandisi na wadau wa biashara. Ndipo tu uzalishe mfano wa kimwili: majedwali halisi, safu wima, aina za data, faharasa, ugawaji, na mpangilio wa hifadhi kwa injini uliyochagua. Kuruka hadi usanifu wa kimwili ndilo kosa la kawaida zaidi la uundaji, kwa sababu linaoka chaguo za teknolojia ya leo ndani ya maamuzi yanayopaswa kudumu kuliko hizo.

### Fanya mifumo ya miamala iwe ya kawaida, na ya uchanganuzi isiwe kwa makusudi

Kwa mifumo inayorekodi miamala, pendelea [kufanya hifadhidata ya kawaida](https://en.wikipedia.org/wiki/Database_normalization). Fomu za kawaida huondoa marudio ili kila ukweli uhifadhiwe mara moja, jambo linalozuia hitilafu za usasishaji na kuweka uandishi sahihi watumiaji wengi wanapobadilisha data kwa wakati mmoja. Hii ndiyo chaguo-msingi sahihi kwa [uchakataji wa miamala mtandaoni](https://en.wikipedia.org/wiki/Online_transaction_processing) (OLTP), ambapo usahihi chini ya uandishi sambamba unajalisha zaidi ya kasi ya swali lolote moja la uchanganuzi. Mifumo ya uchanganuzi ina vipaumbele kinyume. Inasoma kwa wingi, inachanganua na kujumlisha safu kubwa, na kuunganisha majedwali kadhaa ya kawaida wakati wa swali ni polepole na ngumu kufikiria. Hapo unakataa kawaida kwa makusudi, ukiunganisha sifa zinazohusiana pamoja ili maswali yawe rahisi na ya haraka zaidi. Nidhamu ni kukataa kawaida kwa makusudi, kwa sababu iliyoandikwa, badala ya kuacha marudio yaingie kwa bahati mbaya. Sura ya 3.4 (usanifu wa data na uhifadhi) inashughulikia injini zinazofanya kila mfumo ufanye vizuri.

### Tumia uundaji wa vipimo kwa uchanganuzi

Kwa mizigo ya uchanganuzi, pokea [uundaji wa vipimo](https://en.wikipedia.org/wiki/Dimensional_modeling), mbinu iliyoenezwa na Ralph Kimball. Unagawanya ulimwengu kuwa ukweli na vipimo. Jedwali la ukweli linashikilia vipimo vya mchakato wa biashara: kiasi cha mauzo, muda wa simu, wingi uliosafirishwa. Majedwali ya vipimo yanashikilia muktadha wa maelezo unaochuja na kukusanya kwa: mteja, bidhaa, duka, tarehe. Panga jedwali moja la ukweli likizungukwa na vipimo vyake na una [skima ya nyota](https://en.wikipedia.org/wiki/Star_schema), rahisi kwa wachambuzi kuelewa na ya haraka kwa injini kuuliza. Fanya vipimo hivyo viwe vya kawaida kuwa majedwali madogo na unapata skima ya theluji, inayookoa hifadhi kidogo kwa gharama ya viungo zaidi na ugumu zaidi; pendelea nyota isipokuwa una sababu madhubuti. Kwa mazingira makubwa sana, yanayodhibitiwa sana ambapo uwezo wa kukaguliwa na kufuatilia chanzo vinatawala, mbinu ya data vault huunda vitovu, viungo, na satelaiti kunasa historia na asili kwa nguvu, kwa gharama ya majedwali zaidi na mkondo mkali wa kujifunza. Timu nyingi zinapaswa kuanza na nyota za mtindo wa Kimball na kufikia data vault tu mahitaji ya ukaguzi yanapohalalisha.

### Weka chembe na ushughulikie vipimo vinavyobadilika waziwazi

Kabla ya kuongeza safu wima hata moja kwenye jedwali la ukweli, taja chembe yake: safu moja inawakilisha nini hasa. "Safu moja kwa kila mstari wa kitu cha agizo." "Safu moja kwa kila mtumiaji kwa siku." Chembe ndiyo msingi wa mfano sahihi, kwa sababu kila kipimo na kila kipimo cha uchambuzi ama kinafaa chembe hiyo au hakistahili kuwa kwenye jedwali. Kuchanganya chembe ndivyo unavyopata mapato yaliyohesabiwa mara mbili. Kisha amua jinsi vipimo vinavyobadilika kwa muda. Mteja anahamia jiji jipya; unaandika juu ya thamani ya zamani, kuweka historia kamili, au kufuatilia tu ya sasa na ya awali? Hizi ni mifumo ya kawaida ya [vipimo vinavyobadilika polepole](https://en.wikipedia.org/wiki/Slowly_changing_dimension), na kuchagua vibaya kunamaanisha ripoti zako za kihistoria zinaandika upya yaliyopita kimyakimya. Amua chembe na mkakati wa mabadiliko mapema, viandike kwenye nyaraka za mfano, na ushikilie msimamo kwenye mapitio.

### Jenga safu moja ya kisemantiki kama fasili moja ya kila kipimo

Hili ndilo pendekezo linalolipia sura nzima. [Safu ya kisemantiki](https://en.wikipedia.org/wiki/Semantic_layer) inakaa kati ya majedwali yako ya kimwili na kila zana inayoyatumia, na inashikilia fasili moja iliyotawaliwa ya kila kipimo cha biashara. "Mtumiaji hai" anafafanuliwa mara moja, kama msimbo, kwa mantiki yake kamili: matukio gani yanahesabika, kwa dirisha gani, bila kujumuisha akaunti zipi za ndani. "Mapato" yanafafanuliwa mara moja, ikijumuisha jinsi marejesho, punguzo, na ubadilishaji wa sarafu vinavyoshughulikiwa. Kila dashibodi, daftari, ripoti, na kazi ya reverse-ETL inasoma fasili hiyo badala ya kuitekeleza upya kwenye swali la kipekee. Fasili inapobadilika, inabadilika mahali pamoja na kila mtumiaji anasasishwa pamoja. Huu ndio utaratibu unaofanya fasili za vipimo zilizotawaliwa kuwa halisi badala ya za matamanio, na ni utekelezaji wa moja kwa moja wa kile sura ya 11.5 (viashiria muhimu vya utendaji) inachoomba. Chukulia fasili za vipimo kama msimbo wenye matoleo, wamiliki, mapitio, na majaribio, hasa kama sura ya 7.1 inavyokuomba uchukulie data kama bidhaa.

### Anzisha mikataba, majina, na nyaraka

Uthabiti ni kipengele. Pokea mikataba ya majina na uitekeleze: mkataba wa majina ya majedwali, mkataba wa funguo, kiwango cha safu wima za tarehe, kanuni ya jinsi unavyoweka alama ukweli dhidi ya kipimo. Amua mara moja kama unatumia majina ya vyombo ya umoja au wingi na usiyachanganye kamwe. Andika kila mfano mahali ambapo watu wanaoutumia watatazama: maana ya kila jedwali, chembe ya kila ukweli, fasili ya kila kipimo, na mmiliki wa kila kimoja. Majina mazuri na nyaraka ndivyo vinavyomruhusu mchambuzi mpya kujihudumia badala ya kuikatiza timu, na ndivyo vinavyomruhusu mkaguzi kufuatilia namba kutoka mfuko wa bodi hadi chanzo chake bila ziara ya kuongozwa.

### Weka mifano ikibadilika

Mfano wako utabadilika, kwa hiyo sanifu kwa mabadiliko. Ongeza safu wima badala ya kutumia upya zilizopo. Tumia funguo mbadala ili badiliko la ufunguo asilia wa mfumo chanzo lisisambae kwenye ghala lako. Weka matoleo kwenye fasili za vipimo na uziondoe kwa notisi badala ya kuzibadilisha kimyakimya chini ya dashibodi zinazoendesha. Weka mabadiliko kwenye udhibiti wa matoleo, yaliyojaribiwa na kupitiwa, ili badiliko la maana ya "mtumiaji hai" liwe ombi la kuvuta lenye diff na mwidhinishaji, si uhariri wa kimyakimya kwenye zana ya BI. Mfano usioweza kuubadilisha kwa usalama unakuwa mfano ambao watu wanauzunguka, na fasili za kivuli ndivyo chanzo kimoja cha ukweli kinavyokufa.

## Mabadilishano: faida na hasara

| Mbinu | Faida | Hasara | Inafaa zaidi |
|---|---|---|---|
| Ya kawaida (3NF) | Uandishi sahihi, hakuna marudio, unyumbulifu | Viungo vya uchanganuzi vya polepole, maswali changamano | OLTP na mifumo ya uendeshaji |
| Skima ya nyota (Kimball) | Ya haraka, ya kueleweka, rafiki wa mchambuzi | Marudio fulani, ETL ya kudumisha | Uchanganuzi na BI nyingi |
| Skima ya theluji | Hifadhi kidogo, vipimo safi zaidi | Viungo zaidi, ugumu zaidi | Vipimo vikubwa, vilivyotawaliwa kwa ukali |
| Data vault | Historia kamili, inakaguliwa, upakiaji wa wepesi | Majedwali mengi, mkondo mkali wa kujifunza | Yanayodhibitiwa sana, nzito kwa ukaguzi |
| Safu ya kisemantiki juu ya mifano | Fasili moja kila mahali, haitegemei zana | Ujenzi wa awali, inahitaji umiliki | Mashirika ya timu na zana nyingi |

Mvutano wa msingi ni kasi ya swali moja dhidi ya usahihi na unyumbulifu kuvuka eneo lote. Kufanya kawaida hulinda usahihi na kulipia katika ugumu wa maswali; mifano ya vipimo hununua kasi ya swali na uwazi na kulipia kwa ETL na marudio fulani yanayosimamiwa. Hakuna mshindi wa ulimwengu, ndiyo maana unalinganisha mfano na mzigo wa kazi badala ya kuchagua unaopenda. Safu ya kisemantiki hutatua mvutano wa pili, kati ya timu nyingi na zana nyingi, kwa kufanya fasili ya kipimo isitegemee yoyote kati yao. Kosa ni kuchukulia haya kama makambi ya kiitikadi. Shirika lenye afya linaendesha mifumo ya OLTP ya kawaida, mifano ya uchanganuzi ya vipimo inayolishwa kutoka kwayo, na safu moja ya kisemantiki juu, kila moja ikifanya kazi inayoifanya vizuri.

## Maswali ya kujadili na timu yako

1. **Dashibodi mbili zinapoonyesha namba tofauti kwa kipimo kilekile, fasili ya nani inashinda, na fasili hiyo inaishi wapi kimwili?** Swali hili linafichua kama kweli mna chanzo kimoja cha ukweli au mnaamini tu mnacho. Katika timu nyingi kubwa jibu la uaminifu ni kwamba "mtumiaji hai" amefafanuliwa upya katika maswali kumi na mawili, na mshindi ni yeyote anayebishana kwa sauti kubwa zaidi kwenye mkutano. Leta ushahidi halisi: chagua kipimo kimoja, pata kila mahali kinapokokotolewa, na ulinganishe mantiki mstari kwa mstari. Karibu hakika mtapata kutokubaliana kimya kuhusu madirisha, vitu vilivyotengwa, na kesi za pembeni. Jibu linapaswa kuendesha uamuzi wa kujenga safu ya kisemantiki ambapo kila kipimo kinafafanuliwa mara moja, kama msimbo uliopitiwa, ili swali liache kuwa kuhusu watu na kuanza kuwa kuhusu mabaki yenye matoleo. Hadi fasili hiyo iwe na makazi moja ya kimwili, kila upatanisho ni wa muda.

2. **Chembe ya jedwali lenu muhimu zaidi la ukweli ni ipi, na kila mtu chumbani anaweza kuitaja kwa njia ileile?** Chembe ndiyo msingi tulivu ambao kushindwa kwingi kwa uundaji kunarejea kwake. Kama nusu ya timu inasema "safu moja kwa kila agizo" na nusu nyingine "safu moja kwa kila mstari wa kitu," mna hitilafu ya kuhesabu mara mbili inayosubiri kujitokeza kwenye ripoti ya mapato. Leta jedwali halisi na umwombe kila mtu aeleze safu moja kwa sentensi moja. Kutokubaliana hapa si tatizo la mawasiliano la kulainisha; ni kasoro ya usanifu ya kurekebisha kabla vipimo zaidi havijarundikana juu yake. Jibu linapaswa kuandikwa kwenye nyaraka za mfano na kutekelezwa kwenye mapitio, kwa sababu wachambuzi wanapojenga maswali juu ya chembe isiyo wazi, utata unaenea haraka kuliko unavyoweza kurekebisha.

3. **Mfano huu utachukuaje mabadiliko, na nini kinatokea kwa ripoti za mwaka jana fasili inapohama?** Kila mfano unakabiliwa na mifumo chanzo inayobadilika, kanuni za biashara zinazobadilika, na fasili za vipimo zinazobadilika, kwa hiyo swali halisi ni kama mabadiliko ni ombi la kuvuta linalodhibitiwa au uhariri wa kimyakimya unaoandika upya historia. Leta mfano wa hivi karibuni: kipimo ambacho fasili yake ilibadilika, au ufunguo wa chanzo uliopewa jina jipya, na ufuatilie nini kilitokea kwa dashibodi zilizopo. Kama kipimo kinachobadilika polepole kilishughulikiwa kwa kuandika juu, ripoti zenu za kihistoria huenda zilibadilisha kimyakimya thamani zake za zamani, tatizo kubwa kwa yeyote anayefanya uchambuzi wa mielekeo au kuripoti kunakodhibitiwa. Jibu linapaswa kuwasukuma kuelekea funguo mbadala, fasili za vipimo zenye matoleo, mikakati wazi ya mabadiliko, na mabadiliko yaliyowekwa kwenye udhibiti wa matoleo kwa mapitio. Mfano ambao hakuna anayeweza kuubadilisha kwa usalama unakuwa mfano ambao watu wanauacha.

4. **Vipimo vipi lazima vimaanishe kitu kilekile kuvuka kila timu, na nani anawajibika kumiliki kila kimoja?** Vipimo vinavyolingana ndivyo vinavyoruhusu masoko, fedha, na operesheni kuunganisha data yao na kupata majibu yanayolinganishika, lakini tu wakati "mteja," "bidhaa," "eneo," na "tarehe" vinabeba fasili moja iliyokubaliwa badala ya nakala ya faragha kwa kila timu. Mvuto unaoshindana ni uhuru: kila timu inataka kuunda ulimwengu wake kwa kasi yake, na kulazimisha kipimo cha pamoja kunawapunguza kasi kwa muda mfupi huku kukilipa kuvuka eneo lote. Leta vipimo viwili au vitatu vinavyoonekana kwenye ripoti nyingi zaidi za kuvuka timu, orodhesha kila toleo la kila kimoja lililopo leo, na uone funguo na sifa zake zinatofautiana umbali gani kweli. Taja mmiliki kwa kila kipimo kinacholingana, kwa sababu kipimo cha pamoja kisicho na mmiliki kinarudi kuwa nakala za faragha ndani ya robo. Katika mazingira ya mashirika makubwa na serikali, ambapo takwimu kutoka idara moja inalinganishwa na nyingine hadharani, kipimo kisicholingana ndicho tofauti kati ya ulinganisho wa uaminifu na uongo wa bahati mbaya, kwa hiyo amua mapema vipimo vipi vinatawaliwa kati na vipi vinabaki vya ndani.

5. **Mpaka uko wapi kati ya mifumo yenu ya miamala ya kawaida na mifano yenu ya uchanganuzi isiyo ya kawaida, na je, kila kukataa kawaida ni uamuzi wa makusudi?** Kulinganisha mfano na mzigo wa kazi ni nidhamu ya msingi, hata hivyo mpaka ndipo inapofifia: mchambuzi anakataa kawaida ya jedwali la ghala kwa kasi, mhandisi anafanya jedwali la kuripoti kuwa la kawaida kwa mazoea, na hakuna aliyeandika upande upi kila chaguo linahusu. Mvutano ni kasi ya swali moja dhidi ya usahihi na unyumbulifu kuvuka kila kitu, na watu wenye busara hutua tofauti kulingana na kama wanamiliki uandishi au usomaji. Leta swali lenu la uchanganuzi lililo polepole zaidi na jedwali lenu la miamala lenye ushindani zaidi, na uliza kwa kila safu wima ya marudio kama marudio yake yalichaguliwa kwa sababu iliyoandikwa au yaliingia kwa bahati mbaya. Lengo ni kanuni iliyoandikwa ya lini kukataa kawaida kunaruhusiwa na nani anaidhinisha, si mashindano ya usafi. Kwa mashirika makubwa au yanayodhibitiwa, mpaka huu pia huamua mahali data binafsi inarudiwa, kwa hiyo kukataa kawaida bila nyaraka ni swali la utendaji na mfiduo wa utawala wa data ambao mtu atalazimika kuueleza kwa mkaguzi hatimaye.

6. **Mnapaswa kujenga au kununua safu ya kisemantiki, na nani anawajibika kuweka kila fasili ya kipimo ya sasa mara safu hiyo inapokuwepo?** Safu ya kisemantiki hutoa chanzo kimoja cha ukweli tu inapomilikiwa na kudumishwa, kwa hiyo uchaguzi wa zana unajalisha kidogo kuliko jibu la nani anapitia badiliko la maana ya "mapato" na nani anawajibika fasili inapochakaa. Mazingatio yanayoshindana ni halisi: kujenga kunakupa udhibiti na kunafaa mrundiko wako lakini kunaongeza mzigo wa uhandisi, wakati kununua zana ya vipimo ni haraka zaidi lakini kunahatarisha kufungwa na lugha ya fasili msiyoidhibiti kikamilifu. Leta vipimo vyenu vichache vya dau kubwa zaidi, zana zinazovitumia leo, na usomaji wa uaminifu wa kama yeyote anamiliki fasili hizo sasa au zipo tu. Amua mapema kama fasili zinaishi kama msimbo wenye matoleo wenye wamiliki waliotajwa na majaribio, kwa sababu safu ya kisemantiki ambayo hakuna anayeitunza huoza kuwa fasili zilezile zilizotawanyika ilizokusudiwa kuchukua nafasi yake. Katika kuripoti kwa mashirika makubwa na serikali, ambapo kipimo kwenye dashibodi ya umma lazima kifuatilike hadi fasili iliyoandikwa, iliyopitiwa, umiliki huo na uwezo wa kuthibitisha asili ya namba ndivyo vinavyogeuza safu ya kisemantiki kutoka urahisi hadi kidhibiti kinachokaguliwa.

## Mtazamo wa sekta

**Kampuni changa.** Uundaji unaweza kusubiri, lakini fasili haziwezi. Ukiwa na wahandisi wawili na bila muda wa kujenga ghala, weka safu moja ndogo ya kisemantiki kwenye zana yako ya mabadiliko na ufafanue vipimo viwili au vitatu ambavyo bodi yenu inatazama kweli, "mtumiaji hai" na "mapato," mara moja kama msimbo uliojaribiwa. Ruka data vault na skima changamano za vipimo; nyota nyembamba na fasili chache zilizotawaliwa zinakununulia namba thabiti bila kupunguza kasi ya utoaji. Faida ni kwamba maandalizi ya bodi yanaacha kuwa mabishano ya swali la nani ni sahihi.

**Biashara ndogo.** Huna mwundaji wa data wala bajeti ya jukwaa la vipimo, kwa hiyo egemea fasili zilizojengwa kwenye zana unazoendesha tayari na uandike zile chache zinazojalisha kwenye waraka mmoja wa pamoja ambao kila mtu anausoma. Pendelea kununua uchanganuzi uliopachikwa kwenye programu yako iliyopo kuliko kusimamisha ghala usiloweza kuhudumia. Pale unapounda, uweke rahisi na utaje vitu kwa uthabiti, kwa sababu mtu atakayedumisha mwaka ujao anaweza kuwa yule asiyeweza kukumbuka kwa nini "mteja" ilimaanisha vitu viwili. Uthabiti ni nafuu kuliko upatanisho.

**Biashara kubwa.** Tatizo ni timu nyingi na zana nyingi zinazoteleza kuwa fasili za faragha, kwa hiyo wekeza kwenye vipimo vinavyolingana, safu moja ya kisemantiki iliyotawaliwa, na fasili za vipimo zilizohifadhiwa kama msimbo wenye matoleo, wamiliki, na mapitio. Sawazisha majina, matamko ya chembe, na mikakati ya vipimo vinavyobadilika polepole kuvuka eneo ili namba katika zana moja ilingane na ileile katika nyingine. Chukulia safu ya kisemantiki kama bidhaa yenye mpango wa barabara na timu inayomiliki, na upime kiasi gani cha muda wa upatanisho inaondoa. Faida ni namba zinazoaminika kuvuka biashara na ukaguzi unaofuatilia kwa usafi kutoka mfuko wa bodi hadi chanzo.

**Serikali.** Uwazi na ulinganishi wa kuvuka mawakala huumba kazi: data ya rejeo ya kanuni kwa jiografia na demografia, fasili zilizotawaliwa za viashiria vya msingi, na mbinu iliyochapishwa yenye matoleo ya matoleo ili umma uweze kufuatilia takwimu yoyote hadi fasili iliyoandikwa. Kanuni za ununuzi zinaweza kuhitaji mifano na fasili zenu zibaki zinahamishika na zisizo na ubaguzi wa muuzaji, kwa hiyo epuka safu ya kisemantiki iliyofungwa kwa zana moja ya umiliki. Waache mawakala mmoja mmoja wawe huru kuunda data yao ya uendeshaji huku wakilingana na vipimo vya pamoja kwa chochote kinachoripotiwa kitaifa. Kiashiria kilichochapishwa ambacho hakiwezi kufuatiliwa hadi fasili yenye matoleo ni kushindwa kwa uwajibikaji kama ilivyo ya data.

## Mifano

**Kampuni changa.** Kampuni ya Series A ilikuwa na fasili tatu za "mtumiaji hai" zinazoishi mahali pa tatu: zana ya uchanganuzi wa bidhaa, lahajedwali ya fedha, na wasilisho la wawekezaji. Namba hazikuwahi kulingana, na kila maandalizi ya bodi yalikuwa mbio. Wahandisi wawili walianzisha safu ndogo ya kisemantiki kwenye zana yao ya mabadiliko, wakifafanua "mtumiaji hai" na "mapato ya kila mwezi yanayojirudia" mara moja kama msimbo uliojaribiwa, na madirisha na vitu vilivyotengwa vikiandikwa. Kila dashibodi sasa inasoma fasili hizo. Mabishano ya maandalizi ya bodi yalitoweka, na kumwanzisha mchambuzi mpya kulitoka wiki ya maarifa ya kinywa hadi kusoma mfano mmoja ulioandikwa. Hii inaunganika moja kwa moja na nidhamu iliyoelezwa katika sura ya 7.4 (uchanganuzi wa bidhaa na majaribio), ambapo fasili thabiti ya "hai" ndiyo inayofanya matokeo ya majaribio kulinganishwa.

**Biashara kubwa.** Muuzaji wa rejareja wa kimataifa aliendesha zana tano za akili ya biashara kuvuka masoko, fedha, ugavi, uuzaji wa bidhaa, na maduka, na kila moja ilikuwa imebuni upya "faida ghafi" tofauti kidogo. Walijenga safu moja ya kisemantiki juu ya ghala la mtindo wa Kimball lenye vipimo vinavyolingana, ili "bidhaa," "duka," na "tarehe" vimaanishe kitu kilekile kuvuka kila jedwali la ukweli na kila zana. Kila kipimo kilifafanuliwa mara moja na kutumiwa kila mahali. Mikutano ya upatanisho iliyokuwa ikila siku kwa kila robo ilitoweka kwa kiasi kikubwa, na fedha ilipobadilisha jinsi marejesho yanavyoathiri faida, badiliko lilisambaa kwenye zana zote tano kwa wakati mmoja. Vipimo vinavyolingana ndivyo vilivyoruhusu timu huru kuunganisha data yao kwa imani badala ya shaka.

**Serikali.** Serikali ya kitaifa ilihitaji kuripoti kinacholinganishwa kuvuka mawakala wa afya, kazi, na elimu, ambao kihistoria kila mmoja ulifafanua "kaya," "eneo," na "ajira" kwa njia yake. Chombo cha kuvuka mawakala kilianzisha data ya pamoja ya rejeo na fasili sanifu: majedwali ya vipimo ya kanuni ya jiografia na demografia, na fasili zilizotawaliwa za viashiria vya msingi, zilizochapishwa na mbinu na matoleo ya matoleo. Mawakala mmoja mmoja huunda data yao ya uendeshaji lakini hulingana na vipimo na fasili za pamoja kwa chochote kinachoripotiwa kitaifa. Matokeo ni kwamba takwimu kutoka wakala mmoja inaweza kulinganishwa na nyingine kwa uaminifu, na umma unaweza kufuatilia kiashiria chochote kilichochapishwa hadi fasili iliyoandikwa, ukiunga mkono wajibu wa uwazi ulioshughulikiwa katika sura ya 7.1.

## Kesi ya biashara: sababu, ROI, na TCO

Faida ya uundaji mzuri na safu ya kisemantiki kwa kiasi kikubwa ni muda uliorejeshwa na makosa yaliyoepukwa. Katika mashirika mengi, wachambuzi hutumia sehemu kubwa ya muda wao kutafuta data, kupatanisha namba zinazopingana, na kujenga upya fasili ambazo watu wengine tayari waliandika. Fasili moja iliyotawaliwa ya kila kipimo hugeuza kazi hiyo inayojirudia kuwa uwekezaji wa mara moja. Pia inaondoa kategoria nzima ya kushindwa kwa gharama: namba isiyo sahihi kwenye mfuko wa bodi, takwimu iliyoripotiwa vibaya inayochochea matokeo ya ukaguzi, mradi wa upatanisho wa robo nzima unaoishi kwa sababu timu mbili zilifafanua "mapato" tofauti. Fasili inapoishi mahali pamoja palipopitiwa, kushindwa huko kunakoma kwa kiasi kikubwa.

Gharama ni halisi na inastahili kutajwa. Unawekeza mwanzoni kwenye uundaji wa kidhana na wa kimantiki, kujenga na kujaza safu ya kisemantiki, na umiliki endelevu unaoweka fasili za sasa. Jumla ya gharama ya umiliki (TCO) inajumuisha zana, muda wa uundaji na uhandisi wa uchanganuzi, na utawala wa kuzuia mfano usiteleze. Ipime dhidi ya gharama ya kutofanya, ambayo ni kubwa zaidi lakini imejificha: inaonekana kama mabomba yaliyorudiwa, wachambuzi kama injini za binadamu za upatanisho, na watendaji wakifanya maamuzi yenye imani kwa takwimu ambazo hakuna anayeweza kuzitetea. Weka kesi kwa uongozi kwa maneno yao. Fasili moja ya kuaminika ya kila kipimo ndiyo inayowaruhusu kulinganisha kuvuka biashara, kuamini dashibodi, na kujibu wadhibiti bila mbio za dharura. Anza pale maumivu ya upatanisho ni mabaya zaidi, fafanua vipimo hivyo vichache mara moja, na uache muda uliorejeshwa ufadhili salio.

## Mifumo mibaya na mitego

- Kuruka moja kwa moja hadi majedwali ya kimwili, kuoka teknolojia ya leo kwenye maamuzi yanayopaswa kudumu kuliko hiyo.
- Kufafanua kipimo kilekile kwa kujitegemea kwenye kila dashibodi, kwa hiyo hakuna namba mbili zinazolingana.
- Kuacha chembe bila kutajwa, kisha kugundua vipimo vilivyohesabiwa mara mbili kwenye ripoti ya mapato.
- Kukataa kawaida kwa majedwali ya uchanganuzi kwa bahati mbaya badala ya kwa uamuzi ulioandikwa.
- Kufanya ghala la uchanganuzi kuwa la kawaida hadi kila swali ni kiungo cha majedwali kumi na mawili ambacho hakuna anayekielewa.
- Kushughulikia vipimo vinavyobadilika polepole kwa kuandika juu, kwa hiyo ripoti za kihistoria zinaandika upya yaliyopita kimyakimya.
- Kutumia funguo asilia kila mahali, kwa hiyo badiliko la ufunguo wa mfumo chanzo linasambaa kwenye ghala zima.
- Kujenga safu ya kisemantiki bila mmiliki, kwa hiyo fasili zinateleza na uaminifu unamomonyoka.
- Kuchukulia mfano kama umekamilika wakati wa uzinduzi badala ya mali hai inayopaswa kubaki ikibadilika.

## Kielelezo cha ukomavu

- **Ngazi ya 1, Kuanzisha:** Uundaji haujatamkwa na ni wa kuitikia. Majedwali yanasanifiwa kimwili-kwanza na yeyote anayeyahitaji. Vipimo vinafafanuliwa upya katika kila ripoti, na namba mara kwa mara zinapingana. Chembe haijaandikwa, na hakuna anayemiliki fasili.
- **Ngazi ya 2, Kuendeleza:** Baadhi ya majedwali ya uchanganuzi hufuata mfumo wa vipimo, na vipimo vichache muhimu vina fasili zilizoandikwa, lakini zinaishi kwenye wiki na hazitekelezwi. Mikataba ya majina ipo kwenye karatasi. Mazoea yanatofautiana timu hadi timu, na upatanisho bado ni wa mara kwa mara na wa mkono.
- **Ngazi ya 3, Kusawazisha:** Mifano ya kidhana, ya kimantiki, na ya kimwili ni tofauti na inapitiwa. Safu ya kisemantiki inafafanua vipimo vya msingi mara moja, kama msimbo wenye matoleo na wamiliki. Vipimo vinavyolingana huziruhusu timu kuunganisha kwa usalama. Chembe na mikakati ya vipimo vinavyobadilika polepole vimeandikwa na kutekelezwa kwenye mapitio kuvuka shirika.
- **Ngazi ya 4, Kusimamia:** Eneo la mifano linapimwa dhidi ya vipimo vya msingi. Mnafuatilia ufikiaji wa fasili za vipimo (sehemu ya vipimo vilivyoripotiwa vinavyohudumiwa na safu ya kisemantiki), idadi ya fasili zilizorudiwa au za kivuli bado zinatumika, saa za upatanisho zinazotumika kila robo, na kiwango cha kasoro za chembe na asili zinazonaswa kwenye mapitio dhidi ya uzalishaji. Mabadiliko ya fasili hupitia maombi ya kuvuta yaliyopitiwa yenye majaribio, na usafi, viwango vya kupita vya majaribio, na kuteleza vinatazamwa kwenye dashibodi. Kipimo kinapotofautiana au kipimo cha uchambuzi kinapoacha kulingana, upimaji unakifichua kabla ya mkutano wa bodi.
- **Ngazi ya 5, Kuratibu:** Kila kipimo muhimu kina fasili moja iliyotawaliwa inayotumiwa na zana na timu zote, na safu ya kisemantiki imeunganishwa na uchanganuzi, majaribio, na kuripoti kunakodhibitiwa. Mifano inabadilika kwa usanifu na kuboreshwa mfululizo; fasili zinaaminiwa shirika zima; kazi ya upatanisho imetoweka kwa kiasi kikubwa. Shirika mara kwa mara huondoa, hupanua upya, na kupatanisha vipimo vipya biashara inapobadilika, likisawazisha upya eneo la mifano kama mali inayojirekebisha.

## Mawazo ya kujadili

1. Chagua vipimo vyenu vitatu muhimu zaidi. Fasili ngapi tofauti za kila kimoja zipo kuvuka zana zenu leo, na ingehitaji nini kuziporomosha kuwa moja?
2. Chembe isiyotajwa imesababisha wapi kosa halisi la kuripoti, na ilichukua muda gani kugundua?
3. Vipimo vyenu vipi vya uchambuzi vinapaswa kulinganishwa kuvuka timu kwanza, na nani anavimiliki?
4. Fasili zenu za vipimo ziko kwenye udhibiti wa matoleo wenye mapitio, au zinaharirika kimyakimya ndani ya zana ya BI?
5. Kipimo kinachobadilika polepole kiliandika upya historia yenu mara ya mwisho lini bila yeyote kuona, na mngekinasa vipi wakati ujao?
6. Mngebadilisha injini yenu ya ghala kesho, maana ya mfano wenu ingeokoka kiasi gani katika uhamishaji?

## Mambo muhimu ya kukumbuka

- Uundaji wa data ni kuamua data inamaanisha nini, na maana hiyo inadumu kuliko kila teknolojia ya hifadhi mnayochagua.
- Unda katika ngazi tatu kwa mpangilio: kidhana, kisha kimantiki, kisha kimwili.
- Fanya mifumo ya miamala iwe ya kawaida kwa usahihi; kataa kawaida ya mifumo ya uchanganuzi kwa makusudi kwa kasi.
- Tumia uundaji wa vipimo wenye ukweli, vipimo, na chembe iliyotajwa kwa uchanganuzi.
- Jenga safu moja ya kisemantiki ili kila kipimo cha biashara kiwe na fasili moja iliyotawaliwa kila mahali.
- Vipimo vinavyolingana huziruhusu timu huru kuunganisha na kulinganisha data yao kwa imani.
- Taja vizuri, andika, tumia funguo mbadala, na uweke matoleo kwenye fasili ili mfano ubaki ukibadilika.

## Marejeo na usomaji zaidi

- Ralph Kimball and Margy Ross, *The Data Warehouse Toolkit: The Definitive Guide to Dimensional Modeling*.
- Bill Inmon, *Building the Data Warehouse*.
- Dan Linstedt and Michael Olschimke, *Building a Scalable Data Warehouse with Data Vault 2.0*.
- Peter Chen, "The Entity-Relationship Model: Toward a Unified View of Data," ACM Transactions on Database Systems.
- E. F. Codd, "A Relational Model of Data for Large Shared Data Banks," Communications of the ACM.
- C. J. Date, *An Introduction to Database Systems*.
- Lars Rönnbäck and colleagues, writings on anchor modeling.
- DAMA International, *DAMA-DMBOK: Data Management Body of Knowledge*.
