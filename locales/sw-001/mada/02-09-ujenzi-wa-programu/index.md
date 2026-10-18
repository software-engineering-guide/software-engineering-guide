# 2.9 Ujenzi wa programu

## Muhtasari na msukumo

[Ujenzi wa programu](https://en.wikipedia.org/wiki/Software_construction) ndipo usanifu unapogeuka msimbo unaoendesha. Ni kazi ya kina ya kuandika msimbo, uthibitisho, [majaribio ya kitengo](https://en.wikipedia.org/wiki/Unit_testing), [majaribio ya uunganishaji](https://en.wikipedia.org/wiki/Integration_testing), na [utatuzi wa hitilafu](https://en.wikipedia.org/wiki/Debugging). Mwongozo wa [Software Engineering Body of Knowledge](https://en.wikipedia.org/wiki/Software_Engineering_Body_of_Knowledge) (SWEBOK) unachukulia ujenzi kama eneo lake la maarifa, kwa sababu nzuri: hapa ndipo kazi yako nyingi ya kila siku hufanyika. Chaguo unazofanya mstari kwa mstari (jinsi unavyodhibiti ugumu, jinsi unavyoshughulikia makosa, jinsi unavyoacha vitu vikisomeka) huamua kama mfumo unaweza kueleweka, kubadilishwa, na kuaminika kwa miaka ijayo.

Katika timu kubwa, ujenzi ni juhudi ya kikundi, si ya mtu mmoja. Mamia ya wahandisi huandika kwenye msimbo wa pamoja utakaodumu kuliko muda wa mtu yeyote kwenye timu. Kwa hiyo kigezo si "je, inafanya kazi kwenye mashine yangu leo." Ni "je, mgeni anaweza kuubadilisha kwa usalama baada ya miaka mitano." Ujenzi unaunganishwa juu na mahitaji (sura ya 2.8) na usanifu (sura ya 2.2), vinavyokuambia nini cha kujenga na umbo lake. Unaunganishwa pembeni na viwango vya uandishi wa msimbo (sura ya 2.1), majaribio (sura ya 2.4), na mapitio ya msimbo (sura ya 2.5), vinavyoumba jinsi kazi inavyoelezwa, kuthibitishwa, na kukaguliwa. Ujenzi mzuri hugeuza usanifu imara kuwa mali inayodumishika. Ujenzi duni hugeuza hata usanifu mzuri kuwa dhima.

Katika mazingira ya mashirika makubwa na ya serikali, ujenzi hubeba uzito wa ziada. Mifumo hii ni ya muda mrefu, inadhibitiwa kwa nguvu, na mara nyingi muhimu kwa usalama au raia. [Uandishi wa kujilinda](https://en.wikipedia.org/wiki/Defensive_programming), ushughulikiaji wa makosa wenye nidhamu, na msimbo ulio sahihi dhahiri si fadhila hapa; ni mahitaji ya uhakikisho, ukaguzi, na mwendelezo kuvuka miongo na mauzo ya wafanyakazi. Lengo ni msimbo unaowasilisha nia yake, unaostahimili kushindwa, na unaoweza kuthibitishwa. Msimbo unaoendesha tu haitoshi.

## Kanuni kuu

- Punguza ugumu kuliko yote; adui mkuu wa ujenzi wa ukubwa mkubwa ni msimbo ambao hakuna anayeweza kuuelewa kikamilifu.
- Tarajia mabadiliko; jenga ili marekebisho yanayowezekana ya baadaye yawe ya mahali na nafuu.
- Jenga kwa uthibitisho; andika msimbo ambao usahihi wake ni rahisi kukagua kwa majaribio, mapitio, na hoja.
- Tumia tena kwa makusudi; jenga juu ya vipengele vinavyoaminika vilivyopo badala ya kuvumbua upya, lakini epuka kuunganishwa na dhana zisizo sahihi.
- Fuata viwango; uthabiti kuvuka msimbo hupunguza gharama ya kiakili ya kila badiliko la baadaye.
- Shughulikia makosa na hali zisizo halali waziwazi; fanya njia za kushindwa zionekane badala ya kimya.
- Weka msimbo ukisomeka; ujenzi ni mawasiliano na wadumishaji wa baadaye kwanza na kikusanyaji pili.

## Mapendekezo

### Punguza ugumu kama nidhamu ya msingi

Fanya kupunguza ugumu, wa msingi na wa bahati mbaya, kuwa lengo lako kuu. Andika kazi na moduli ndogo, za madhumuni moja. Pendelea majina wazi kuliko hila za busara. Weka uwekaji wa viota ukiwa wa kina kifupi na mtiririko wa udhibiti ukiwa wa mstari. Weka maamuzi mahali pamoja ili kuelewa kipande kimoja cha msimbo kisikulazimishe kushikilia mfumo mzima kichwani. Ugumu ndio unaofanya misimbo mikubwa iwe polepole kubadilisha na hatari kuigusa, kwa hiyo pima kila chaguo kwa kama kinaongeza ugumu au kinauondoa. Tumia kanuni za usanifu za sura ya 2.2 kwa kiwango kidogo pia: mshikamano wa juu, uunganishaji mdogo, na [kutenganisha wasiwasi](https://en.wikipedia.org/wiki/Separation_of_concerns) wazi ni muhimu katika kazi moja kama katika usanifu.

### Jenga kwa mabadiliko na kwa uthibitisho

Fikiria mbele kwa mabadiliko yanayowezekana zaidi kuja (kanuni mpya za biashara, uunganishaji mpya, udhibiti mpya) na uyatenge nyuma ya violesura thabiti ili mabadiliko yabaki ya mahali. Wakati huohuo, andika msimbo ambao ni rahisi kuthibitisha: [kazi safi](https://en.wikipedia.org/wiki/Pure_function) (ingizo zilezile daima hutoa pato lilelile, bila athari za pembeni) pale unapoweza, hali iliyofichika ndogo, na utegemezi ulio wazi ili majaribio yaweze kuubadilisha. Msimbo mgumu kujaribu kwa kawaida ni msimbo mgumu kuuelewa na kubadilisha. Uwezo wa kujaribu (sura ya 2.4) ni ishara ya usanifu, si wasiwasi wa QA tu.

### Tumia tena kwa makusudi na usawazishe

Fikia maktaba zinazodumishwa vizuri, zinazoaminika na vipengele vya ndani kabla ya kuandika upya mantiki ya msingi, na uvitumie kupitia violesura vilivyo wazi (sura ya 2.3). Jenga vipengele vinavyoweza kutumika tena tu pale kisa cha pili halisi kipo, kwa sababu kujumlisha mapema ni aina yake ya ugumu. Tumia viwango na mtindo wa uandishi wa msimbo wa shirika lako (sura ya 2.1) kwa usawa, kwa hakika vikitekelezwa na vipanga muundo vya kiotomatiki na [linters](https://en.wikipedia.org/wiki/Lint_(software)), ili msimbo mzima usomeke kana kwamba mwandishi mmoja makini aliandika.

### Fanya uandishi wa kujilinda kwa busara

Thibitisha ingizo kwenye mipaka ya uaminifu (maombi ya nje, I/O ya faili na mtandao, ingizo la mtumiaji) na uchukulie data yoyote inayovuka mipaka hiyo kama ya uadui hadi ithibitishwe vinginevyo. Ndani ya moduli iliyojaribiwa vizuri, hata hivyo, usifunike kila mstari kwa ukaguzi usio wa lazima unaoficha mantiki na kukandamiza kushindwa halisi. Kanuni ni rahisi: jilinde kwenye mipaka, amini ndani yake. Tumia [madai](https://en.wikipedia.org/wiki/Assertion_(software_development)) kuandika na kutekeleza vigeu visivyobadilika ambavyo havipaswi kuwa uongo katika programu sahihi. Tumia [vighairi](https://en.wikipedia.org/wiki/Exception_handling) na ushughulikiaji wa makosa kwa hali zinazoweza kutokea halali wakati wa kuendesha. Viweke tofauti: madai hulinda dhana za mwandishi, ushughulikiaji wa makosa husimamia kushindwa kunakotarajiwa.

### Shughulikia makosa waziwazi na ushindwe kwa usalama

Kwa kila kosa, amua kwa makusudi la kufanya: kupona, kujaribu upya, kupitisha, au kushindwa haraka. Kamwe usimeze kighairi kimyakimya wala kupuuza kosa lililorudishwa; kushindwa kulikokandamizwa kunarudi kama kasoro ya fumbo baadaye. Weka muktadha katika ujumbe wako wa makosa na kumbukumbu ili kushindwa kuweze kutambuliwa. Katika mifumo muhimu kwa usalama na raia, shindwa kuelekea hali salama, inayojulikana badala ya kuendelea katika hali iliyoharibika. Fikiria njia ya kosa kwa kiasi kilekile kama njia ya furaha, kwa sababu kwenye uzalishaji njia ya kosa ndipo uaminifu unaposhindwa au kushinda.

### Jenga ubora ndani wakati wa ujenzi

Ubora hujengwa ndani, hauchunguzwi baadaye. Andika majaribio ya kitengo kando ya msimbo, endesha [uchambuzi tuli](https://en.wikipedia.org/wiki/Static_program_analysis) na linters mfululizo, na uweke kazi ndogo vya kutosha kuzifikiria. Tumia majina na muundo vinavyojieleza ili maoni yako yaeleze kwa nini, si nini. [Rekebisha muundo](https://en.wikipedia.org/wiki/Code_refactoring) unapoendelea kuweka msimbo ukikalika. Mapitio ya msimbo (sura ya 2.5) ni kinga ya binadamu, lakini ubora mwingi unapaswa kuwepo kabla mapitio hayajaanza.

### Chagua na usawazishe zana za ujenzi

Sawazisha mnyororo wa zana (vikusanyaji, mifumo ya ujenzi, vipanga muundo, linters, wachambuzi tuli, vitatuzi, wasimamizi wa utegemezi, na usanidi wa IDE) ili kila mhandisi afanye kazi katika mazingira thabiti, yanayoweza kuzalishwa upya. Unganisha zana hizi kwenye bomba ili ukaguzi wa ubora usiwe wa hiari. Karibisha zana za uandishi zinazosaidiwa na AI kwa makusudi, na uchukulie pato lao kama rasimu inayopaswa kupita viwango, mapitio, na majaribio yaleyale kama msimbo mwingine wowote.

## Mabadilishano: faida na hasara

| Mazoea | Faida | Hasara |
|---|---|---|
| Kupunguza ugumu kwa ukali | Kinasomeka, kinabadilika, kiwango cha chini cha kasoro | Kinaweza kuhisi polepole; hatari ya dhana nyingi kupita kiasi ikitumika vibaya |
| Ukaguzi mwingi wa kujilinda | Hunasa hali mbaya mapema, mipaka imara | Hujaza mantiki; unaweza kuficha hitilafu halisi ukizidi |
| Madai kwa vigeu visivyobadilika | Huandika na kutekeleza dhana | Huzimwa katika baadhi ya ujenzi wa uzalishaji; si ushughulikiaji wa makosa |
| Utumiaji mkubwa wa maktaba | Msimbo mdogo wa kumiliki; utoaji wa haraka | Hatari ya utegemezi, uunganishaji, mfiduo wa mnyororo wa ugavi |
| Viwango vikali na linting | Msimbo sare, wenye msuguano mdogo | Usanidi wa awali; unaweza kuhisi mgumu kwa watu binafsi |
| Kujenga kwa uwezo wa kujaribu | Msimbo unaoweza kuthibitishwa, kubadilishwa | Unaweza kuongeza uelekezaji ambao baadhi huuona kama taratibu |

Mabadilishano ya msingi katika ujenzi ni kasi ya muda mfupi dhidi ya uwezo wa kubadilika wa muda mrefu. Kukata njia (kuruka ushughulikiaji wa makosa, kuvumilia ugumu, kupuuza viwango) huhisi haraka papo hapo, na karibu daima ni ghali zaidi kwa maisha ya mfumo. Kushindwa kinyume ni kuhandisi kupita kiasi: kujilinda kupita kiasi, dhana za kubahatisha, na ujumla ambao hakuna anayeuhitaji. Ujenzi wenye ustadi uko katikati: rahisi iwezekanavyo, wa kujilinda kama mipaka inavyodai, na si zaidi.

## Maswali ya kujadili na timu yako

1. **Ufafanuzi wetu wa pamoja, madhubuti wa "ngumu mno" ni upi, na tunautekeleza wapi kabla ya kuunganisha?** "Punguza ugumu" ndiyo nidhamu kuu ya ujenzi, lakini kama kauli mbiu hupoteza kila mjadala dhidi ya tarehe ya mwisho. Katika timu kubwa ambapo mamia ya watu huandika kwenye msimbo mmoja, ugumu lazima upimike, kwa hiyo kubaliana ishara mtakazotendea kazi kweli: urefu wa kazi, kina cha uwekaji viota, ugumu wa mzunguko, na idadi ya vitu msomaji lazima ashikilie kichwani kuelewa badiliko moja. Leta mkosaji wako mbaya zaidi kwenye mkutano na uulize kama mapitio yenu ya sasa yangemnasa. Jibu linapaswa kugeuka kuwa lango la bomba au kipengee cha orodha hakiki ya mapitio, kwa sababu kizingiti kinachotekelezwa na zana kina thamani kuliko kanuni inayotekelezwa na nguvu ya nia, na kinamwokoa mwajiriwa wako anayefuata kutokana na mkusanyiko wa polepole wa msimbo ambao hakuna anayeweza kuugusa kwa usalama.

2. **Kwenye uzalishaji, njia zetu za makosa zinatenda kama tulivyobuni, na lini mara ya mwisho tuliendesha moja kwa makusudi?** Ushauri wa ujenzi unasema fikiria njia ya kosa kwa kiasi kilekile kama njia ya furaha, hata hivyo njia ya kosa kwa kawaida ni msimbo unaojaribiwa kidogo zaidi unaomiliki, na katika mfumo muhimu kwa raia au usalama ndipo uaminifu unaposhindwa au kushinda. Kighairi kilichokandamizwa au msimbo wa kurudi uliopuuzwa huwa kasoro ya fumbo wiki baadaye, na "shindwa kuelekea hali salama" ni ahadi usiyoweza kuitimiza kama hujawahi kuiona ikitokea. Leta historia yenu ya matukio: kukatika kwa awali kuligeukia kosa lililomezwa au njia ya kurejesha isiyojaribiwa mara ngapi? Hatua ni kujaribu kushindwa kwa makusudi (ingiza kadi iliyokataliwa, muda kuisha, ingizo lililoharibika) na kuhitaji kila kosa lishughulikiwe, liandikwe kwa muktadha, au lipitishwe, kamwe lisidondoshwe kimya.

3. **Sehemu zipi za msimbo wetu ni ngumu kujaribu, na ugumu huo unatuambia nini kuhusu usanifu?** Msimbo unaopinga majaribio karibu daima ni msimbo unaoficha hali, unaounganisha na utegemezi usio sahihi, au unaofanya mengi mno, kwa hiyo uwezo wa kujaribu ni ishara ya usanifu, si wazo la baadaye la QA. Katika mfumo wa mashirika makubwa wa muda mrefu hili ni muhimu kwa sababu moduli zenye maumivu kujaribu leo ndizo mgeni ataogopa kuzibadilisha baada ya miaka mitano. Leta darasa au huduma ambayo timu yako inaogopa kuandikia majaribio na uulize kwa nini: je, hali imefichika, je, utegemezi hauwezi kubadilishwa, je, kazi inafanya kazi tatu? Jibu linapaswa kuendesha urekebishaji kuelekea kazi safi, utegemezi ulio wazi, na vitengo vidogo vya madhumuni moja, kwa sababu kufanya msimbo uthibitishike ni kazi ileile ya kuufanya uwe unaoeleweka na wa nafuu kubadilisha.

4. **Tunatumia lini maktaba ya nje dhidi ya kujenga uwezo wenyewe, na nani anamiliki hatari ya mnyororo wa ugavi tunayoichukua?** Kufikia maktaba inayoaminika ni haraka kuliko kuvumbua upya mantiki ya msingi, hata hivyo kila utegemezi unaoongeza ni msimbo usioudhibiti, usioweza kuukagua kwa urahisi, na unaopaswa kuupachika siku utakapoathirika. Katika timu kubwa hatari ni kwamba wahandisi mia kila mmoja huvuta utegemezi wake wa kupitia hadi hakuna anayeweza kusema msimbo unaendesha nini kweli. Leta orodha yenu ya utegemezi na uulize mambo matatu madhubuti: maktaba ngapi hazidumishwi, ngapi zina udhaifu unaojulikana, na ngapi zinafunika mantiki rahisi vya kutosha kuimiliki kabisa. Jambo linaloshindana ni halisi, kwa sababu kuandika kriptografia yako au ushughulikiaji wa tarehe karibu daima ni mbaya kuliko maktaba iliyojaribiwa vita, kwa hiyo lengo ni sera ya makusudi ya kutumia tena badala ya kuepuka kwa jumla. Katika mazingira ya mashirika makubwa na ya serikali, ongeza pembe ya ununuzi na uzingatiaji wa leseni, kwa kuwa utegemezi usiokaguliwa unaweza kubeba leseni isiyooana na wajibu wako au asili ambayo hakuna mkaguzi anayeikubali.

5. **Tunashikiliaje msimbo uliozalishwa na AI kwa viwango vilevile vya ujenzi kama msimbo ulioandikwa na binadamu, na je, tunaweza kutofautisha hivi viwili inapojalisha?** Wasaidizi wa uandishi wa AI huzalisha rasimu zinazoonekana sahihi haraka, na kishawishi ni kuchukulia pato lao kama lililokamilika kwa sababu linakusanya na linaonekana la kawaida. Kanuni ya sura ni kwamba msimbo uliozalishwa unapita mapitio, majaribio, na viwango vilevile kama kitu kingine chochote, na timu kubwa lazima ifanye kanuni hiyo iwe ya kiutendaji badala ya ya matamanio. Leta mifano ya mabadiliko yaliyosaidiwa na AI yaliyosafirishwa hivi karibuni na uulize kama kila moja lilibeba majaribio, lilipita uchambuzi tuli, na liliyeleweka kweli na binadamu aliyeliwasilisha, au lilipitishwa kwa uaminifu. Shinikizo linaloshindana ni kasi, kwa sababu wasaidizi hawa wana tija kweli na kupunguza kila pendekezo hadi kutambaa kunatupa manufaa. Katika miktadha inayodhibitiwa na ya serikali, ongeza pembe ya asili na uwajibikaji, kwa sababu unaweza kulazimika kuthibitisha nani anawajibika kwa mstari wa msimbo na kama kipande kilichozalishwa kina swali la leseni au hakimiliki ambalo huwezi kulijibu.

6. **Je, mnyororo wetu wa zana za ujenzi umesawazishwa na kutekelezwa kwenye bomba kweli, au watu binafsi bado wanafanya kazi katika usanidi usiooana?** Mnyororo wa pamoja wa zana wa kipanga muundo, linter, mchambuzi tuli, mfumo wa ujenzi, na msimamizi wa utegemezi unamruhusu mhandisi kuvuka huduma zisizojulikana kwa kujiamini, kwa sababu msimbo unasomeka kwa sauti moja na ukaguzi ni uleule kila mahali. Unapoteleza, kila timu huvumbua upya usanidi wake, muda wa mapitio unatumika kubishana mtindo, na kasoro ambazo mchambuzi wa timu moja angezinasa zinateleza kwa nyingine. Leta orodha ya hazina ambazo haziendeshi ukaguzi wa kawaida kwa kila commit na uulize kwa nini kila moja ilijitoa. Mvutano ni kwamba usanidi mmoja ulioamriwa unaweza kuhisi mgumu kwa timu zenye mahitaji tofauti kweli, kwa hiyo amua mahali usawa unastahili msuguano na mahali kighairi kilichoandikwa kinafaa. Kwa shirika kubwa au chombo cha umma, funga hili na uwezo wa kuzalishwa upya na ukaguzi, kwa sababu ujenzi usioweza kuzalisha upya baiti kwa baiti kutoka mnyororo wa zana unaodhibitiwa ni ule usioweza kuutetea kwa mhakiki miaka baadaye.

## Mtazamo wa sekta

**Kampuni changa.** Kasi inashinda, kwa hiyo weka kipanga muundo na linter cha pamoja siku ya kwanza, thibitisha ingizo kwenye mpaka wako mmoja wa nje, na uweke msimbo wa ndani ukiwa safi badala ya wa kujilinda kila mstari. Ruka dhana za kubahatisha na mchakato mzito: kwa wahandisi wawili au watatu timu nzima inashikilia msimbo vichwani, na hatari halisi ni ugumu unaodumu kuliko kumbukumbu hiyo ya pamoja. Tegemea maktaba zinazoaminika kwa chochote cha msingi ili uandike msimbo mdogo iwezekanavyo unaoweza kuumiliki vizuri.

**Biashara ndogo.** Bila mhandisi maalumu wa ujenzi na bajeti finyu, pendelea desturi ambazo zana zako zilizopo zinazitekeleza bure: kipanga muundo na linter vinavyokuja na lugha, chaguo-msingi zenye busara, na seti ndogo ya kanuni ambazo kila mtu anaweza kuzikumbuka. Nunua au pokea maktaba zinazodumishwa vizuri badala ya kujenga miundombinu usiyoweza kuiajiria kudumisha. Tumia nidhamu yako ndogo kwa vitu viwili vinavyoumiza zaidi vikipuuzwa: kuthibitisha ingizo kwenye mpaka na kamwe kutomeza kosa kimya.

**Biashara kubwa.** Wahandisi mamia wakiandika kwenye msimbo wa pamoja, kipaumbele ni usawa na utekelezaji: mnyororo wa kawaida wa zana uliounganishwa kwenye bomba, malango ya uchambuzi tuli, na kanuni za uthibitisho wa mpaka zinazotumika kila mahali ili watu wahame kwa kujiamini kati ya huduma. Simamia hatari ya utegemezi na mnyororo wa ugavi kama mchakato unaotawaliwa badala ya ubunifu wa kila timu, na utumie madai kuweka vigeu visivyobadilika vya eneo vinavyopaswa kushikilia kuvuka kila timu. Chukulia viwango vya ujenzi kama msingi unaoweka msimbo ukikalika kuvuka miongo na mauzo ya wafanyakazi.

**Serikali.** Mifumo ya muda mrefu, muhimu kwa raia hufanya ujenzi wenye nidhamu kuwa suala la uhakikisho na uwajibikaji. Tenga kanuni tete kama sheria nyuma ya violesura thabiti ili mabadiliko yabaki ya mahali na yafuatiliwe hadi mahitaji, shindwa kuelekea hali salama zinazojulikana badala ya kuendelea katika zilizoharibika, na usafirishe kila moduli na majaribio yanayofanya kazi pia kama ushahidi wa ukaguzi. Wajibu wa ununuzi na uwazi unamaanisha mnyororo wenu wa zana, utegemezi, na ushughulikiaji wa makosa lazima viandikwe vizuri vya kutosha kwamba mtumishi wa umma anayefika miaka baadaye, au mkaguzi wa nje, anaweza kuthibitisha msimbo ni sahihi.

## Mifano

**Kampuni changa.** Kampuni changa ya wahandisi watatu inaweka kipanga muundo na linter cha pamoja siku ya kwanza na kuviendesha kwa kila commit, kwa hiyo msimbo unasomeka kwa sauti moja hata wanapoongeza wakandarasi. Wanathibitisha ingizo kwenye mpaka wao wa API na kuchukulia kila kitu cha nje kama cha uadui, lakini wanaweka mantiki ya ndani safi badala ya kuifunika kwa ukaguzi usio wa lazima. Ndoano ya malipo inapoanza kushindwa, suluhisho ni la haraka kwa sababu hakuna kighairi kilichomezwa kimya na ujumbe wa kosa unabeba muktadha wa kutosha kuelekeza moja kwa moja kwenye sababu. Usanidi mzima ulichukua alasiri na uliwaokoa mkusanyiko wa polepole wa ugumu ambao ungefanya wiki ya kwanza ya mwajiriwa wao anayefuata iwe ya taabu.

**Biashara kubwa.** Kampuni ya kimataifa ya malipo inatekeleza mnyororo wa pamoja wa zana kuvuka mamia ya wahandisi: muundo na linting ya kiotomatiki kwa kila commit, malango ya uchambuzi tuli kwenye bomba, na kanuni kwamba ingizo zote za nje zithibitishwe kwenye mipaka ya huduma. Mantiki ya eneo inatumia madai kutekeleza vigeu visivyobadilika kama "ingizo la leja daima lina usawa," huku hali za wakati wa kuendesha kama kadi iliyokataliwa zikishughulikiwa kama matokeo wazi, yaliyoandikwa. Kwa sababu viwango ni sare na makosa hayamezwi kimya kamwe, wahandisi wanahama kwa kujiamini kuvuka huduma zisizojulikana, na matukio ya uzalishaji yanaweza kutambuliwa moja kwa moja kutoka kwenye kumbukumbu.

**Serikali.** Wakala wa kitaifa wa kodi unajenga mfumo wa muda mrefu wa tathmini unaotarajiwa kuendeshwa kwa miongo chini ya sheria zinazobadilika. Ujenzi unatenga kila kanuni ya kodi nyuma ya kiolesura thabiti, kwa hiyo mabadiliko ya kila mwaka ya sheria yanabaki ya mahali na yanafuatilika hadi mahitaji (sura ya 2.8). Uthibitisho wa kujilinda unalinda kila ingizo linalomkabili raia. Njia za makosa zinashindwa kuelekea hali salama isiyotoa tathmini isiyo sahihi kimya. Kila moduli inasafirishwa na majaribio ya kitengo kama ushahidi wa ukaguzi. Kwa sababu ujenzi umesawazishwa na umeandikwa vizuri, watumishi wapya wa umma wanaweza kudumisha kwa usalama msimbo ulioandikwa na watangulizi walioondoka zamani.

## Kesi ya biashara: sababu, ROI, na TCO

Mapato ya ujenzi wenye nidhamu ni uwezo wa kudumu wa kubadilisha programu kwa bei nafuu na kwa usalama, na hapo ndipo sehemu kubwa ya jumla ya gharama ya umiliki ya mfumo huamuliwa. Tafiti za uchumi wa programu mara kwa mara zinaonyesha kwamba sehemu kubwa ya gharama ya maisha ya mfumo ni matengenezo, na gharama ya matengenezo inatawaliwa na jinsi msimbo unavyoeleweka na kubadilika. Kupunguza ugumu, kushughulikia makosa waziwazi, na kufuata viwango hupunguza moja kwa moja gharama ya kila badiliko la baadaye na kila tukio la uzalishaji.

Gharama ya kupokea ni ya wastani na hasa ya awali: weka viwango, unganisha linters na wachambuzi, na ujenge tabia ya kuandika msimbo unaothibitishika, wa kujilinda. Gharama ya kupuuza, kwa upande mwingine, inajumlika. Ugumu hujikusanya kuwa msimbo wa polepole kubadilisha na hatari kugusa. Makosa ya kimya hugeuka matukio ghali ya uzalishaji. Mtindo usio thabiti huzidisha juhudi za kila mapitio na kila utambulisho. Kujenga hoja kwa uongozi, unganisha ubora wa ujenzi na kiwango cha kushindwa kwa mabadiliko, muda wa wastani wa kurejesha, kiwango cha kasoro zinazotoroka, na muda wa utambulisho, vyote vinavyoboreshwa moja kwa moja na nidhamu ya ujenzi.

## Mifumo mibaya na mitego

- **Kuteleza kwa ugumu:** kukusanya msimbo wa busara, uliowekwa viota kwa kina, au uliotawanyika hadi hakuna anayeuelewa.
- **Kumeza makosa kimya:** vizuizi tupu vya catch na misimbo ya kurudi iliyopuuzwa inayogeuza kushindwa kuwa mafumbo ya baadaye.
- **Kupita kiasi kwa uandishi wa kujilinda:** ukaguzi usio wa lazima kila mahali unaozika mantiki na kuficha kasoro halisi.
- **Kuchanganya madai na ushughulikiaji wa makosa:** kutumia madai kwa hali za wakati wa kuendesha, au vighairi kwa vigeu visivyobadilika vya mwandishi.
- **Ujenzi wa kunakili-na-kubandika:** kurudia mantiki badala ya kuitumia tena, kwa hiyo marekebisho lazima yafanywe mahali pengi.
- **Ujumla wa kubahatisha:** kujenga dhana na uwezo wa kusanidi kwa mahitaji yasiyofika kamwe.
- **Kupuuza viwango:** kila mhandisi akiandika kwa njia yake, kuzidisha mzigo wa kiakili kuvuka msimbo.
- **Ujenzi usiojaribiwa:** kuandika msimbo bila majaribio yanayoambatana, kuahirisha uthibitisho hadi awamu isiyofika kamwe.

## Kielelezo cha ukomavu

- **Ngazi ya 1 (Kuanzisha):** Ujenzi ni wa papo hapo na wa kuitikia; ugumu na ushughulikiaji wa makosa hutofautiana kwa mtu; viwango vichache vipo, na kushindwa kimya ni kwa kawaida.
- **Ngazi ya 2 (Kuendeleza):** Viwango vya uandishi wa msimbo, vipanga muundo, na linters vipo, na ushughulikiaji wa msingi wa makosa na majaribio ya kitengo vinatarajiwa, lakini mazoea hayana uthabiti na kila timu inavitumia tofauti.
- **Ngazi ya 3 (Kusawazisha):** Kupunguza ugumu, uthibitisho wa mpaka, ushughulikiaji wazi wa makosa, na uwezo wa kujaribu vimeandikwa na kutekelezwa shirika zima, kwenye bomba na mapitio, kwa hiyo msimbo mzima unasomeka kana kwamba mwandishi mmoja makini aliandika.
- **Ngazi ya 4 (Kusimamia):** Ubora wa ujenzi unapimwa dhidi ya vipimo vya msingi; timu inafuatilia ugumu wa mzunguko, kiwango cha kasoro zinazotoroka, kiwango cha kushindwa kwa mabadiliko, ufikiaji wa majaribio ya njia za makosa, na matokeo ya mapitio ya msimbo, na inatenda juu ya mielekeo badala ya maoni.
- **Ngazi ya 5 (Kuratibu):** Ujenzi unaboreshwa kila wakati na kuunganishwa kuvuka shirika; mifumo ya kujilinda, viwango, na vipimo vinalisha urekebishaji na zana; zana zinazosaidiwa na AI zinaendeshwa chini ya malango ya ubora yaleyale, na mazoea hubadilika lugha, kanuni, na hatari zinapobadilika.

## Mawazo ya kujadili

- Ugumu wa bahati mbaya unakusanyika zaidi wapi kwenye msimbo wenu, na tabia gani za ujenzi zinauzalisha?
- Kanuni halisi ya timu yenu ni ipi kuhusu mahali pa kuthibitisha ingizo na mahali pa kuamini?
- Je, wahandisi wenu wanatofautisha madai na ushughulikiaji wa makosa, na je, tofauti hiyo ni thabiti?
- Ubora kiasi gani umejengwa ndani wakati wa ujenzi dhidi ya kunaswa baadaye kwenye mapitio au majaribio?
- Mnaamuaje lini kutumia maktaba dhidi ya kujenga, ikizingatiwa hatari ya mnyororo wa ugavi?
- Msimbo uliozalishwa na AI unapaswa kushikiliwaje kwa viwango vilevile vya ujenzi kama msimbo ulioandikwa na binadamu?

## Mambo muhimu ya kukumbuka

- Ujenzi ndipo usanifu unapogeuka msimbo unaodumishika; kupunguza ugumu ndiyo nidhamu yake kuu.
- Jenga kwa mabadiliko na uthibitisho: msimbo unaoweza kujaribiwa, kubadilishwa ni msimbo unaoeleweka.
- Jilinde kwenye mipaka ya uaminifu, amini ndani yake, na usimeze makosa kimya kamwe.
- Tumia madai kwa vigeu visivyobadilika na ushughulikiaji wa makosa kwa hali zinazotarajiwa za wakati wa kuendesha; usizichanganye.
- Sawazisha zana na mtindo, tumia tena kwa makusudi, na ujenge ubora ndani badala ya kuuchunguza baadaye.

## Marejeo na usomaji zaidi

- IEEE Computer Society, *SWEBOK Guide (Guide to the Software Engineering Body of Knowledge)*, Software Construction knowledge area
- Steve McConnell, *Code Complete: A Practical Handbook of Software Construction*
- Robert C. Martin, *Clean Code: A Handbook of Agile Software Craftsmanship*
- Andrew Hunt and David Thomas, *The Pragmatic Programmer*
- Martin Fowler, *Refactoring: Improving the Design of Existing Code*
- John Ousterhout, *A Philosophy of Software Design*
