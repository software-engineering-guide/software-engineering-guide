# 2.12 Mifano na mbinu za programu

## Muhtasari na msukumo

Kielelezo cha programu ni urahisishaji wa makusudi wa mfumo, uliojengwa kujibu swali mahususi. Mbinu ni njia yenye nidhamu ya kuzalisha programu, ikijumuisha vielelezo inavyovitumia njiani. Kwa pamoja huunda eneo la maarifa la Software Engineering Body of Knowledge (SWEBOK), kwa sababu ni zana za kiakili unazotumia kufikiri kuhusu mfumo kabla, wakati, na baada ya kuujenga. Mchoro wa darasa wa UML ([Unified Modeling Language](https://en.wikipedia.org/wiki/Unified_Modeling_Language)), [mchoro wa uhusiano wa vyombo](https://en.wikipedia.org/wiki/Entity%E2%80%93relationship_model) (ERD), [mashine ya hali](https://en.wikipedia.org/wiki/Finite-state_machine), [ubainishaji rasmi](https://en.wikipedia.org/wiki/Formal_specification), na mfano wa majaribio wa kutupwa vyote ni vielelezo. [Waterfall](https://en.wikipedia.org/wiki/Waterfall_model), [kutengeneza mifano ya majaribio](https://en.wikipedia.org/wiki/Software_prototyping), uendelezaji rasmi, na [agile](https://en.wikipedia.org/wiki/Agile_software_development) vyote ni mbinu.

Kwa nini kujisumbua na vielelezo kabisa? Kwa sababu kumbukumbu ya kufanyia kazi ya binadamu ni ndogo na mifumo ya programu ni mikubwa. Hakuna anayeweza kushikilia mfumo wa mistari laki moja kichwani, kwa hiyo tunachora picha na kuandika dhana zinazoonyesha upande mmoja kwa wakati: data, mtiririko wa udhibiti, hali, mwingiliano. Kielelezo hakikusudiwi kamwe kuwa mwaminifu kwa msimbo; kinakusudiwa kufaa kwa uamuzi. Kielelezo kizuri kinaonyesha hasa unachohitaji kuamua jambo, na kinaficha kingine chote.

Katika timu kubwa, dau halisi ni uratibu na mawasiliano. Mamia ya wahandisi, wasanifu, wachambuzi, na wakaguzi wanapofanya kazi kwenye mfumo mmoja, vielelezo vya pamoja ni ardhi ya kawaida ambapo wanajadiliana usanifu, mahitaji, na hatari. Kwa hiyo chukulia uundaji wa vielelezo kama zana yenye kazi ya kufanya. Inalipa kielelezo kinapokuwa nafuu kuliko kosa kinalozuia. Inakuwa upotevu ukikichora kwa ajili yake yenyewe, ukikihifadhi muda mrefu baada ya kupitwa na wakati, au ukikifafanua zaidi ya uamuzi kilichokusudiwa kuutumikia. Uundaji wa vielelezo unaunganishwa kwa karibu na mahitaji ya programu (sura ya 2.8), kanuni za usanifu wa programu (sura ya 2.2), usanifu na nukuu zake kama C4 na arc42 (sura ya 3.1), na njia za kufanya kazi za agile (sura ya 10.7).

## Kanuni kuu

- Kila kielelezo kina madhumuni; ikiwa huwezi kutaja uamuzi ambao kielelezo kinaufahamisha, usikichore.
- Uondoaji wa maelezo ni kitendo cha msingi cha uundaji wa vielelezo: jumuisha kinachojalisha kwa madhumuni, acha kilichobaki.
- Uthabiti ni muhimu ndani na kuvuka vielelezo; vielelezo vinavyopingana ni vibaya kuliko kutokuwa navyo.
- Vielelezo ni vitu vya mawasiliano kwanza; hadhira yao huamua nukuu na kina chao.
- Pendelea kielelezo chepesi zaidi kinachojibu swali; ufafanuzi una gharama ya kubeba.
- Kielelezo ni kizuri tu kama uchambuzi wake; kielelezo kisichokaguliwa ni dhana isiyojaribiwa.
- Chagua mbinu kulingana na kutokuwa na uhakika kwa tatizo, hatari, na matokeo ya kushindwa.

## Mapendekezo

### Unda vielelezo kwa uondoaji wa maelezo, madhumuni, na uthabiti

Anza kila kielelezo kwa kutaja madhumuni na hadhira yake. Kisha ondoa maelezo bila huruma kuelekea madhumuni hayo: mchoro wa mfuatano unaokusudiwa kutatua hali ya mbio unapaswa kuonyesha muda na ujumbe, si kila uga. Weka vielelezo vyako vikiwa thabiti kati yake, ili vyombo katika ERD, madarasa katika mchoro wa darasa, na nomino katika mahitaji vyote vikubaliane, na thabiti na uhalisia, ambayo inamaanisha unasasisha au kufuta kielelezo mfumo unapoendelea. Kielelezo kilichopitwa na wakati ambacho watu wanakiamini ni hatari. Kielelezo kilichopitwa na wakati ambacho kila mtu anakipuuza ni upotevu unaoendelea kugharimu umakini.

### Chagua vielelezo vya kimuundo au vya kitabia kulingana na swali

Tumia vielelezo vya kimuundo kuonyesha mfumo umeundwa na nini na sehemu zinahusianaje: michoro ya darasa, michoro ya vipengele, na michoro ya uhusiano wa vyombo kwa muundo wa data. Tumia vielelezo vya kitabia kuonyesha mfumo unafanya nini kwa muda: mashine za hali kwa vitu vyenye mizunguko ya maisha yenye maana, michoro ya mfuatano kwa mwingiliano kuvuka vipengele, na michoro ya shughuli kwa mtiririko wa kazi na michakato ya biashara. Chagua nukuu moja inayofichua uamuzi ulio mbele yako. Mifumo mingi inahitaji aina chache tu za michoro, zilizochorwa kwa kuchagua, si orodha kamili ya UML iliyotumika kwa kila kitu.

### Changanua vielelezo, usivichore tu

Kielelezo hulipa kupitia uchambuzi, si kuchorwa tu. Kagua mashine ya hali kwa hali zisizofikika, mabadiliko yanayokosekana, na kukwama. Kagua ERD kwa matatizo ya kurekebisha na mahusiano yaliyoachwa. Pitia mchoro wa mfuatano dhidi ya mahitaji kupata njia za makosa zinazokosekana. Pitia vielelezo vyako na wataalamu wa eneo wanaoweza kuona kilicho kibaya. Na pale gharama ya kushindwa ni kubwa, fikia uchambuzi unaosaidiwa na zana (wakaguzi wa vielelezo, wakaguzi wa uthabiti, uigaji) badala ya kukagua kwa macho.

### Tumia mbinu za kiheuristiki kama chaguo-msingi

Programu nyingi hujengwa kwa mbinu za kiheuristiki: njia za kurudia zinazotegemea uzoefu zinazotumia vielelezo kwa njia isiyo rasmi na kuhukumu matokeo dhidi ya matarajio badala ya uthibitisho. Kwa mifumo mingi ya biashara na ya serikali, hilo ni sahihi kabisa: mahitaji hubadilika, na kasoro kwa kawaida inarekebishika. Mbinu za kiheuristiki huoana kwa asili na agile (sura ya 10.7): unda kielelezo cha kutosha tu kuoanisha timu, kisha jenga na ujifunze.

### Hifadhi mbinu rasmi kwa viini vyenye matokeo makubwa

[Mbinu rasmi](https://en.wikipedia.org/wiki/Formal_methods) huonyesha ubainishaji kwa hisabati na hutumia uthibitisho, iwe ni ushahidi au [ukaguzi kamili wa kielelezo](https://en.wikipedia.org/wiki/Model_checking), kuthibitisha sifa. Zinagharimu ujuzi na muda halisi, na zinalipa hasa pale kushindwa kunapokuwa kwa maafa au kusiko na kutenduka: udhibiti muhimu kwa usalama, itifaki za kriptografia, viini vya malipo ya kifedha, na mfano wake. Zitumie kwenye kiini kidogo muhimu, si mfumo mzima. Na kumbuka kuwa ubainishaji rasmi peke yake, hata bila uthibitisho kamili, mara nyingi huongeza thamani kwa kukulazimisha tu kuwa sahihi.

### Tumia mifano ya majaribio kuondoa kutokuwa na uhakika

Mahitaji au uwezekano usipokuwa wazi, jenga mfano wa majaribio kujifunza, kisha amua, kwa makusudi, kama utauendeleza au kuutupa. Mifano ya majaribio ya kutupwa huchunguza swali kwa bei nafuu kisha hufutwa. Mifano ya majaribio ya kuendelezwa huwa bidhaa na lazima ijengwe kwa viwango vya uzalishaji. Kushindwa kwa kawaida ni kuacha mfano wa kutupwa uteleze kwenye uzalishaji kwa bahati mbaya. Kwa hiyo taja aina ya mfano kabla ya kuujenga.

### Linganisha mbinu na hatari, si na mitindo

Chagua mbinu kwa kutokuwa na uhakika kwa tatizo na matokeo ya kushindwa. Kutokuwa na uhakika kwa juu kunapendelea mifano ya majaribio na kurudia kwa agile. Matokeo makubwa yanapendelea uchambuzi rasmi na uthibitisho mkali. Mfumo wenye yote mawili unahitaji kiini rasmi muhimu ndani ya bahasha ya agile kwa ujumla. Chochote ufanyacho, usipokee mbinu kwa sababu tu ina heshima au kwa sababu muuzaji anaiuza.

## Mabadilishano: faida na hasara

| Kielelezo au mbinu | Ikitumika vizuri | Hali ya kushindwa |
|---|---|---|
| Vielelezo vya kimuundo (UML, ERD) | Picha ya pamoja ya sehemu na data | Michoro kuenea; kuteleza kutoka msimbo |
| Vielelezo vya kitabia (hali, mfuatano, shughuli) | Hufichua muda, hali, na kesi za pembeni | Michoro yenye maelezo mengi kupita kiasi ambayo hakuna anayesoma |
| Mbinu za kiheuristiki | Za haraka, zinazonyumbulika, zinafaa mifumo mingi | Zisizo na nidhamu; dhana zilizofichika |
| Mbinu rasmi | Sifa zinazothibitishika kwa viini muhimu | Gharama kubwa; kutumika kwa mfumo mzima kimakosa |
| Mifano ya majaribio | Kujifunza kwa bei nafuu; huondoa hatari mapema | Msimbo wa kutupwa kupandishwa kwenye uzalishaji |
| Mbinu za agile | Hubadilika na mahitaji yanayobadilika | Huruka uundaji wa vielelezo unaohitajika kwa matatizo magumu |

Mvutano unaojirudia ni kati ya ukali na kasi. Uundaji mdogo mno wa vielelezo husafirisha dhana zilizofichika kwenye uzalishaji. Uundaji mwingi mno hutumia juhudi kwenye michoro isiyofahamisha uamuzi na inayooza msimbo unapobadilika. Hakuna kipimo kisichobadilika kinachotatua hili, ni kanuni ya uwiano tu: wekeza katika kielelezo au mbinu kulingana na kutokuwa na uhakika inachokiondoa na gharama ya kukosea uamuzi. Injini ya malipo na tovuti ndogo ya uuzaji vinastahili matibabu tofauti.

## Maswali ya kujadili na timu yako

1. **Je, tunachanganua vielelezo vyetu, au tunavichora tu na kuendelea?** Kielelezo hulipa kupitia uchambuzi, si kwa kuwepo: mashine ya hali ambayo hukaguli kwa hali zisizofikika au mabadiliko yanayokosekana ni dhana isiyojaribiwa iliyovikwa kama mchoro. Katika timu kubwa hapa ndipo kasoro halisi hujificha, kwa sababu picha inayoonekana kuwa inayokubalika huaminiwa hasa wakati hakuna aliyeipitia dhidi ya mahitaji kupata njia ya kosa inayokosekana au uhusiano ulioachwa. Leta kielelezo chenu muhimu zaidi cha kitabia kwenye mkutano na ujaribu kukivunja: mpito upi haujafafanuliwa, hali ipi haina kutokea, mfuatano upi hauna muda wa kuisha? Pale gharama ya kushindwa ni kubwa, jibu linapaswa kukuelekeza kwenye uchambuzi unaosaidiwa na zana (wakaguzi wa vielelezo, wakaguzi wa uthabiti, uigaji) badala ya kukagua kwa macho, kwa sababu sababu nzima ya kuunda kielelezo cha kiini muhimu ni kupata kasoro kwenye ubao mweupe badala ya kwenye uzalishaji.

2. **Vielelezo vyetu viwili vinapotofautiana, kipi kinashinda, na nani anagundua mgongano?** Uthabiti ni muhimu ndani na kuvuka vielelezo, na vielelezo vinavyopingana ni vibaya kuliko kutokuwa navyo, kwa sababu watu hutenda juu ya vyote viwili. Katika mfumo mkubwa vyombo katika kielelezo cha data, madarasa katika usanifu, na nomino katika mahitaji huteleza kimyakimya timu tofauti zinaposasisha vitu tofauti, na ishara ya kwanza mara nyingi ni hitilafu ya uzalishaji ambapo vipengele viwili vilitofautiana kuhusu kitu ni nini. Leta mfano: chagua dhana moja ya msingi na uangalie kama ERD, msimbo, na mahitaji vinakubaliana kweli kuhusu umbo na mzunguko wake wa maisha. Visipokubaliana, amua kipi ni chenye mamlaka na nani anawajibika kuweka vingine sawa, na uwe tayari kufuta kielelezo badala ya kuacha kilichopitwa na wakati kiendelee kuidanganya timu.

3. **Kiini kipi katika mfumo wetu, kikiwa kibaya, kinapoteza fedha halisi au kumdhuru mtu, na je, kinapata ukali kinaostahili?** Hatua kuu ya sura hii ni kulinganisha mbinu na hatari: mbinu za kiheuristiki na agile kwa wengi wanaorekebishika, ubainishaji rasmi na uthibitisho kwa kiini kidogo chenye matokeo makubwa, na mifano ya majaribio ya bei nafuu kwa kisichoeleweka kweli. Njia za kushindwa ni sawia na zote ni ghali: kutumia mbinu rasmi kwenye tovuti ndogo ya uuzaji huchoma fedha, na kuchukulia injini ya malipo au seti ya kanuni za kustahiki kama kazi ya kawaida ya agile hualika kasoro ya maafa isiyotenguka. Leta ramani ya mfumo wenu na uweke alama mahali kosa ni la maafa dhidi ya linalorekebishika, na mahali mahitaji yanajulikana dhidi ya yasiyojulikana. Jibu linapaswa kuelekeza uwekezaji wenu wa uundaji wa vielelezo mahali fedha na utata vilipo, na kuuzuia waziwazi kila mahali pengine, ili kiini rasmi muhimu kikae ndani ya bahasha ya agile bila mbinu yoyote kuvuja katika eneo la nyingine.

4. **Tunaunda vielelezo kiasi gani kabla ya kuandika msimbo, na je, kipimo hicho kinabadilika na kutokuwa na uhakika mbele yetu?** Usanifu mkubwa wa awali na kutokuwa na usanifu kabisa ni njia za kushindwa, na kipimo sahihi kiko kati yake, kikitawaliwa na kutokuwa na uhakika kiasi gani kielelezo kinaondoa kweli. Katika timu kubwa shinikizo huenda pande zote mbili: mchakato wa utawala unaweza kudai seti kamili ya michoro kabla ya msimbo wowote, ukifunga maamuzi yaliyofanywa kwa taarifa chache zaidi, huku shinikizo la utoaji likiweza kusukuma timu kuruka mashine ya hali moja ambayo ingenasa kesi ya pembeni ya gharama kubwa. Leta miradi yenu miwili ya mwisho na upange vielelezo mlivyozalisha kuwa vilivyofahamisha uamuzi halisi na vilivyochorwa kwa sababu kiolezo kiliviomba tu. Katika programu za mashirika makubwa na serikali, ambapo lango la awamu au bodi ya idhini mara nyingi huamuru nyaraka mapema, njoo tayari kutetea uundaji wa vielelezo unaofuata hatari badala ya orodha isiyobadilika ya vitu vya kutoa, ili kiini cha malipo kipate ukali wake na zana ya ndani ya ripoti isizame katika michoro ambayo hakuna anayesoma.

5. **Je, tumekubaliana nukuu ya pamoja na makao moja ya vielelezo vyetu, au kila timu inavumbua yake?** Vielelezo ni vitu vya mawasiliano kwanza, na thamani yao huporomoka mashine ya hali iliyochorwa kwenye zana ya timu moja isipoweza kusomwa, kupatikana, au kuaminiwa na timu inayoirithi. Kwa mamia ya wahandisi mazingatio yanayoshindana ni halisi: nukuu na hazina iliyoamriwa hununua uthabiti na uwezo wa kugundulika, lakini pia huweka gharama ya kujifunza na inaweza kusukuma watu kuelekea zana nzito wakati ubao mweupe uliopigwa picha ungetosha. Leta mifano ya mahali kielelezo kiliishi kweli (wiki, zana ya michoro, slaidi, kompyuta ya mtu) na uulize nani angeweza kukipata na kukielewa miezi sita baadaye. Katika mazingira ya mashirika makubwa na yanayodhibitiwa pembe ya ukaguzi inaongeza makali: mkaguzi asiyeweza kupata kielelezo cha sasa cha data au kufuatilia uamuzi hadi mashine ya hali iliyoandikwa atachukulia mfumo kuwa haujaandikwa, kwa hiyo kubaliana nukuu ndogo ya pamoja na mahali pa kudumu, na ukubali kunasa kwa wepesi badala ya taratibu popote matokeo ni madogo.

6. **Kabla ya kujenga mfano wa majaribio, tunaamua kwa makusudi kama ni wa kutupwa au wa kuendelezwa, na je, tunajishikilia kwa uchaguzi huo?** Kushindwa kwa kawaida, kwa gharama kubwa ni mfano wa kutupwa unaoteleza kimyakimya kwenye uzalishaji kwa sababu ulionyeshwa vizuri na hakuna aliyetaja aina yake mapema. Mvutano ni halisi: mifano ya kutupwa hununua kujifunza kwa bei nafuu kabisa na inapaswa kufutwa, huku mifano ya kuendelezwa ikiwa bidhaa na lazima ijengwe kwa viwango vya uzalishaji tangu mstari wa kwanza, na kuchanganya hivi viwili ama hupoteza kazi ya kurudia au husafirisha msimbo dhaifu kwenye jukumu usiloundiwa. Leta mfano wa majaribio wa hivi karibuni na uulize nini kiliamuliwa kabla ya kujengwa, nani alishikilia mamlaka ya kuupandisha au kuutupa, na kama uamuzi huo ulinusurika shinikizo la utoaji. Katika serikali na mazingira mengine yanayowajibika, ambapo mfumo unaowakabili raia hubeba wajibu wa uwazi na kutegemewa, chukulia kupandishwa kwa bahati mbaya kama kushindwa kwa udhibiti: weka hatima ya mfano mapema, na ufanye kutupa mfano wa kutupwa uliofanikiwa kuwa matokeo ya kusherehekewa badala ya upotevu wa kuepukwa.

## Mtazamo wa sekta

**Kampuni changa.** Unda kielelezo kwenye ubao mweupe, kipige picha, na uendelee. Rasilimali yako adimu zaidi ni umakini wa kihandisi, kwa hiyo fikia kielelezo tu kinapokuwa nafuu kuliko kosa kinalozuia: mashine ya hali ya usajili kabla ya kuandika kesi za pembeni za bili, si orodha kamili ya UML kwa bidhaa inayoweza kubadilisha mwelekeo mwezi ujao. Baki kiheuristiki na agile, weka mbinu rasmi nje kabisa ya mezani, na uchukulie kila mfano wa majaribio kama wa kutupwa isipokuwa uamue vinginevyo kwa makusudi.

**Biashara ndogo.** Huenda huna mtu ambaye kazi yake ni uundaji rasmi wa vielelezo, kwa hiyo tegemea vielelezo vilivyojengwa ndani ya zana na mifumo unayonunua badala ya kuanzisha mazoea yako ya uundaji. Panga vielelezo vichache unavyochora kuzunguka maamuzi madhubuti: mchoro rahisi wa kielelezo cha data kukubaliana ni data gani ya wateja unayoishikilia, mchoro wa hali kwa mtiririko mmoja unaokupotezea mteja ukivunjika. Pendelea bidhaa iliyonunuliwa yenye kielelezo cha data kilichothibitishwa kuliko kujenga na kuandika chako mwenyewe, na uweke chochote unachochora chepesi vya kutosha mtu mmoja aweze kukidumisha.

**Biashara kubwa.** Tatizo la msingi ni uratibu kuvuka timu nyingi, kwa hiyo vielelezo vya pamoja huwa ardhi ya kawaida: kielelezo cha data kilichokubaliwa, nukuu thabiti, na makao ambapo ERD, michoro ya C4, na mashine za hali zinaweza kupatikana na kuaminiwa. Sawazisha nukuu ndogo na utekeleze uthabiti ili vyombo katika mahitaji, usanifu, na hifadhidata visiteleze kati ya timu. Hifadhi ubainishaji rasmi na ukaguzi wa vielelezo kwa viini vyenye matokeo makubwa (malipo, upatanisho, udhibiti wa ufikiaji), fadhili ujuzi maalumu huo unaodai, na uweke njia ya ukaguzi kutoka kila kielelezo kilichoandikwa hadi uamuzi kilichoutetea.

**Serikali.** Kanuni zilizowekwa kwenye sheria lazima zifuatilike hadi sheria, na hapo ndipo ubainishaji rasmi unapostahili gharama yake: bainisha mantiki ya kustahiki au tathmini kwa usahihi, thibitisha sifa muhimu, na waache wakaguzi wafuatilie kila matokeo hadi kanuni iliyoyazalisha. Ununuzi unaongeza uzito wake, kwa kuwa nyaraka na vielelezo mara nyingi ni vitu vya kimkataba vya kutoa, kwa hiyo kubaliana vielelezo vipi vinabeba uamuzi kweli badala ya kuzalishwa tu kutimiza orodha hakiki. Chapisha maelezo ya lugha rahisi ya jinsi mifumo yenye matokeo makubwa inavyofanya kazi, na utumie mifano ya majaribio ya kutupwa kujaribu uingizaji wa data unaowakabili raia na watumiaji halisi kabla ya kujitolea kwenye ujenzi wa uzalishaji.

## Mifano

**Kampuni changa.** Kampuni changa ndogo inayojenga bidhaa ya bili ya usajili inachora mzunguko wa maisha wa usajili (jaribio, hai, umechelewa kulipwa, umeghairiwa, umewashwa upya) kama mashine ya hali kwenye ubao mweupe kabla ya kuandika msimbo. Wakipitia mchoro, wanagundua hawakuwahi kufafanua kinachotokea malipo ya akaunti iliyochelewa kulipwa yanapokamilika hatimaye, kesi ya pembeni ambayo ingewaacha wateja halisi katika hali ya kutokujulikana. Kielelezo hicho cha dakika tano kinaokoa maumivu ya kichwa ya uzalishaji, na wanakipiga picha badala ya kudumisha zana nzito ya michoro. Kwingineko wanabaki agile na wanaunda kielelezo cha kutosha tu kuoanisha, kwa sababu kwa ukubwa wao kasoro inarekebishika na mbinu rasmi zingekuwa gharama tupu.

**Biashara kubwa.** Benki ya kimataifa inajenga jukwaa jipya la malipo. Timu inatumia mchoro wa uhusiano wa vyombo kukubaliana kielelezo cha data cha pamoja kuvuka timu za akaunti, leja, na ujumbe, na michoro ya C4 (sura ya 3.1) kuonyesha jinsi huduma zinavyoungana. Wanaunda mzunguko wa maisha wa muamala (unasubiri, umeondolewa, umesuluhishwa, umebatilishwa, umepingwa) kama mashine ya hali iliyo wazi, na uchambuzi unafichua kuwa unakosa mpito wa ubatilishaji wa sehemu. Pengo linarekebishwa kwenye ubao mweupe badala ya kwenye uzalishaji. Michoro ya mfuatano inapitia mtiririko wa suluhisho dhidi ya mahitaji (sura ya 2.8) kufichua njia za muda kuisha na kujaribu upya zinazokosekana. Utoaji wa kila siku ni agile, lakini algoriti ya msingi ya upatanisho, ambapo kosa linamaanisha fedha halisi zilizopotea, inapata ubainishaji rasmi na inakaguliwa kielelezo kabla ya utekelezaji. Uundaji wa vielelezo umejikita mahali fedha na utata vilipo, na kuwekwa mwepesi kila mahali pengine.

**Serikali.** Wakala wa kitaifa wa kodi unaboresha tathmini ya manufaa. Kwa sababu kanuni za kustahiki zimewekwa kwenye sheria na kukaguliwa, timu inaandika ubainishaji rasmi wa kanuni kama mabadiliko safi na kuthibitisha sifa muhimu, kama hakuna mdai anayekuwa anastahili na hastahili kwa wakati mmoja na kila kesi kufikia uamuzi, ili wakaguzi wafuatilie matokeo hadi sheria. Kando ya kiini rasmi, timu inajenga mfano wa majaribio wa kutupwa wa fomu ya kuingiza data inayowakabili raia ili kujaribu na watumiaji halisi. Wanajifunza kuwa mchawi wa hatua nyingi hupunguza makosa, kisha wanatupa mfano na kujenga upya uingizaji kwa viwango vya uzalishaji. Michoro ya shughuli inaandika mchakato wa mfanyakazi wa kesi mwanzo hadi mwisho kwa mafunzo na ukaguzi. Kanuni zenye matokeo makubwa zinapata ukali rasmi; uzoefu wa mtumiaji usio na uhakika unapata mifano ya majaribio ya bei nafuu; hakuna mbinu inayotumika mahali pa nyingine.

## Kesi ya biashara: sababu, ROI, na TCO

Mapato ya uundaji wa vielelezo yanatokana na kupata kasoro mapema, ambapo ni nafuu zaidi kuzirekebisha. Mgongano uliopatikana kwenye ubao mweupe unagharimu dakika. Mgongano uleule uliopatikana kwenye uzalishaji unaweza kugharimu kukatika, programu ya kurudia kazi, au, katika nyanja zinazodhibitiwa, dhima ya kisheria. Vielelezo pia hupunguza jumla ya gharama ya umiliki kwa kutumika kama mawasiliano ya kudumu. Mfumo unaodumu kuliko waandishi wake, hali ya kawaida katika mashirika makubwa na serikali, ni nafuu zaidi sana kudumisha kielelezo chake cha data, mashine za hali, na mtiririko muhimu vinapoandikwa kwa usahihi.

Gharama ni halisi, na lazima uzipime. Vielelezo huchukua muda kujenga, ujuzi kujenga vizuri, na juhudi endelevu kuvihifadhi vya sasa; mbinu rasmi huongeza kazi ya wataalamu. Nukta ya kuvunja usawa inatawaliwa na kutokuwa na uhakika na matokeo. Pale yote mawili ni ya chini, uundaji mzito wa vielelezo huharibu thamani na heuristiki za agile hushinda. Pale lolote ni la juu, uundaji wa vielelezo unaolengwa, na, kwa kiini muhimu, uthibitisho rasmi, hulipa mara nyingi kwa kuzuia darasa ghali la kushindwa. Kujenga hoja kwa uongozi, funga uwekezaji wa uundaji wa vielelezo na hatari mahususi zilizoondolewa na uwezo wa kudumishwa wa mifumo ya muda mrefu. Na fuatilia kama vielelezo vinashauriwa kweli, kwa sababu kielelezo kisichotumika ni gharama tupu.

## Mifumo mibaya na mitego

- **Kuunda vielelezo kwa ajili yake yenyewe:** kuzalisha michoro kwa sababu mchakato unaidai, si kwa sababu inafahamisha uamuzi.
- **Vielelezo vilivyopitwa na wakati vinavyoaminiwa kama ukweli:** michoro isiyolingana tena na msimbo lakini bado inategemewa.
- **Usanifu mkubwa wa awali:** vielelezo kamili vinavyozalishwa kabla ya msimbo wowote, vikifunga maamuzi yaliyofanywa kwa taarifa chache zaidi.
- **Kuenea kwa michoro:** kila aina ya UML ikitumika kwa usawa, ikizamisha mitazamo michache ya manufaa kwenye kelele.
- **Mbinu rasmi kila mahali:** kutumia uthibitisho ghali kwenye msimbo ambapo matokeo ya kushindwa hayahalalishi.
- **Kupandishwa kwa bahati mbaya kwa mfano wa majaribio:** mfano wa kutupwa unaosafirishwa kimyakimya kama bidhaa.
- **Nukuu kuliko kiini:** kubishana usahihi wa UML badala ya kama kielelezo kinajibu swali.

## Kielelezo cha ukomavu

- **Ngazi ya 1 (Kuanzisha):** Uundaji wa vielelezo ni wa papo hapo au haupo na ni wa kuitikia tu; hakuna mbinu inayotajwa; vielelezo, vinapochorwa kabisa, havina uthabiti, havichanganuliwi, na huachwa mkutano unapoisha.
- **Ngazi ya 2 (Kuendeleza):** Baadhi ya timu huchora michoro ya kawaida na kufuata mbinu iliyotajwa, lakini mazoea hayalingani kuvuka shirika: vielelezo mara nyingi huzalishwa kwa taratibu, huteleza kutoka msimbo, na mara chache huchanganuliwa kwa kasoro.
- **Ngazi ya 3 (Kusawazisha):** Nukuu ya pamoja, mwongozo ulioandikwa wa kuchagua mbinu, na kanuni za uthabiti zimefafanuliwa na kutekelezwa shirika zima; vielelezo huchaguliwa kwa madhumuni, huwekwa sawa na mfumo, hupitiwa kwa kasoro, na mbinu inalinganishwa na hatari ya kila tatizo.
- **Ngazi ya 4 (Kusimamia):** Uundaji wa vielelezo unapimwa na kudhibitiwa dhidi ya vipimo vya msingi; timu hufuatilia kasoro ngapi uchambuzi unanasa kabla ya utekelezaji, vielelezo vimeteleza kiasi gani kutoka msimbo, kama kila kielelezo kilishauriwa kweli kwa uamuzi halisi, na kurudia kazi na muda wa mzunguko vilivyookolewa dhidi ya kipimo cha msingi kilichofafanuliwa; uchaguzi wa mbinu unarekebishwa kwa kutokuwa na uhakika na matokeo yaliyopimwa, na viini muhimu vinathibitishwa rasmi dhidi ya malengo ya ufikiaji yaliyokubaliwa.
- **Ngazi ya 5 (Kuratibu):** Uundaji wa vielelezo na uchaguzi wa mbinu unaboreshwa kila wakati na kuunganishwa na utoaji na upangaji wa hatari kuvuka shirika; uwekezaji hubadilika kutokuwa na uhakika na matokeo yanapohama, vielelezo huwekwa vya sasa, kustaafishwa, au kuongezewa kina kwa ushahidi, na mbinu rasmi, za kiheuristiki, na za mifano ya majaribio zinaunganishwa ili kila moja iwe hasa mahali inapolipa.

## Mawazo ya kujadili

- Kwa mradi wenu wa mwisho, vielelezo vipi vilifahamisha uamuzi halisi, na vipi vilichorwa kwa sababu mchakato uliviomba tu?
- Wapi katika mifumo yenu ubainishaji rasmi ungejilipa, na wapi ungekuwa upotevu?
- Mnaamuaje kama mfano wa majaribio ni wa kutupwa au wa kuendelezwa, na je, mnatekeleza uamuzi huo?
- Mnazuiaje vielelezo kuteleza nje ya usawazishaji na msimbo, au mnakubali kwamba vingine vinapaswa kufutwa badala yake?
- Kiasi sahihi cha uundaji wa vielelezo kabla ya msimbo katika muktadha wenu ni kipi, na kinabadilikaje na kutokuwa na uhakika?
- Kielelezo kipi cha kitabia (hali, mfuatano, au shughuli) kingenasa tukio lenu la hivi karibuni la uzalishaji?

## Mambo muhimu ya kukumbuka

- Kielelezo ni uondoaji wa maelezo wenye madhumuni; ikiwa huwezi kutaja uamuzi unaoufahamisha, usikichore.
- Linganisha vielelezo vya kimuundo na vya kitabia na swali mahususi, na uviweke thabiti na vya sasa.
- Changanua vielelezo; kielelezo kisichokaguliwa ni dhana isiyojaribiwa.
- Mbinu za kiheuristiki na agile zinafaa mifumo mingi; hifadhi mbinu rasmi kwa viini vyenye matokeo makubwa.
- Tumia mifano ya majaribio kuondoa kutokuwa na uhakika, na uamue mapema kama ni ya kutupwa au ya kuendelezwa.
- Wekeza katika uundaji wa vielelezo kulingana na kutokuwa na uhakika unaoondoa na gharama ya kukosea uamuzi.

## Marejeo na usomaji zaidi

- IEEE Computer Society, *SWEBOK Guide (Software Engineering Body of Knowledge), Version 4.0*, Software Engineering Models and Methods knowledge area
- Martin Fowler, *UML Distilled: A Brief Guide to the Standard Object Modeling Language*
- Grady Booch, James Rumbaugh, Ivar Jacobson, *The Unified Modeling Language User Guide*
- Frederick P. Brooks, *The Mythical Man-Month* and *No Silver Bullet: Essence and Accident in Software Engineering*
- Daniel Jackson, *Software Abstractions: Logic, Language, and Analysis* (the Alloy modeling language)
- Leslie Lamport, *Specifying Systems* (TLA+)
- Simon Brown, *Software Architecture for Developers* (the C4 model)
- David Harel, *Statecharts: A Visual Formalism for Complex Systems*
