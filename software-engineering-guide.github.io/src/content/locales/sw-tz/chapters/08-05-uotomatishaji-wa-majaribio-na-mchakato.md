# 8.5 Uotomatishaji wa majaribio na mchakato

## Muhtasari na msukumo

Uotomatishaji wa majaribio na mchakato ni mazoea ya kubadilisha kazi ya kujirudia ya mkono ya kihandisi na ya uendeshaji kuwa mtiririko wa kazi unaotegemewa, unaotekelezwa na mashine. Upande wa majaribio, hii inamaanisha [uotomatishaji wa majaribio](https://en.wikipedia.org/wiki/Test_automation): seti za majaribio za kiotomatiki zinazoendesha mfululizo kuthibitisha usahihi, utendaji, na usalama. Upande wa mchakato, inapanuka hadi mitambo inayozunguka utoaji na uendeshaji wa programu: kukusanya ushahidi wa uzingatiaji, kutekeleza vitabu vya mwongozo vya uendeshaji, kurekebisha matatizo yanayojulikana, na kutekeleza vidhibiti vya utawala, usalama, na gharama. Wazo la kuunganisha ni rahisi. Chochote kinachofanywa mara kwa mara na kwa kutabirika kinapaswa kusimbwa, ili kiendeshe kwa uthabiti, haraka, na bila kazi ya kuchosha ya binadamu.

Kwa timu kubwa, uotomatishaji ndiyo njia pekee ya kuzuia ubora na udhibiti usiporomoke chini ya ukubwa. Majaribio ya mkono hayawezi kuendana na mamia ya wahandisi wanaofanya maelfu ya mabadiliko. Yanakuwa kizuizi, na ufunikaji wake unakosa uthabiti na kutegemewa. Taratibu za uendeshaji za mkono pia huteseka. Kuanzisha upya huduma, kuzungusha kitambulisho, na kukusanya ushahidi wa ukaguzi vyote vinakuwa vya polepole na vyenye makosa binadamu waliochoka wanapovifanya chini ya shinikizo kuvuka eneo kubwa. Kuotomatisha kazi hii hufanya matokeo yaweze kurudiwa. Pia kunawaachia wahandisi wenye ujuzi kulenga matatizo yanayohitaji hukumu ambayo yanahitaji kweli ufahamu wa binadamu.

Katika mazingira ya mashirika makubwa na serikali, uotomatishaji pia ni ufunguo wa kufanya uzingatiaji uwe endelevu. Mashirika yanayodhibitiwa lazima yaonyeshe mfululizo kwamba vidhibiti vipo na ushahidi unakusanywa. Kufanya hivi kwa mkono ni ghali, polepole, na kunakabiliwa na mapengo. Kuotomatisha ukusanyaji wa ushahidi na utekelezaji wa vidhibiti kunageuza uzingatiaji kutoka mazoezi ya dharura ya mara kwa mara kuwa sifa endelevu, inayothibitika ya mfumo. Mbinu hii ya "uzingatiaji-kama-msimbo" inapunguza gharama na kuimarisha uhakikisho ambao wakaguzi na wadhibiti wanahitaji.

## Kanuni kuu

- Otomatisha kazi inayojirudia, inayotabirika, na inayotegemea kanuni; hifadhi juhudi ya binadamu kwa hukumu.
- Fanya majaribio ya kiotomatiki yawe ya haraka, ya kutegemewa, na ya uamuzi, la sivyo yatapuuzwa.
- Endesha majaribio sambamba na uyahamishie mapema ili maoni yabaki ya haraka suti inapokua.
- Simba taratibu za uendeshaji kama [vitabu vya mwongozo](https://en.wikipedia.org/wiki/Runbook)-kama-msimbo ili ziwe na matoleo, zinazojaribika, na zinazotekelezeka.
- Pendelea uotomatishaji uliounganishwa vizuri kuliko hati dhaifu zinazobandikwa kwenye mifumo kutoka nje.
- Zalisha ushahidi wa uzingatiaji kiotomatiki kama zao la pembeni la mtiririko wa kawaida wa kazi.
- Weka binadamu kwenye mzunguko kwa vitendo vya hatari kubwa; otomatisha kilicho salama na cha kawaida kwanza.

## Mapendekezo

### Jenga miundombinu ya majaribio ya haraka, ya kutegemewa, na sambamba

Suti ya majaribio ina thamani tu ikiwa wahandisi wanaiamini na inarudisha maoni haraka. Wekeza kwenye miundombinu ya majaribio inayoendesha suti sambamba kuvuka wafanyakazi wengi, ili jumla ya muda wa saa ya ukutani ibaki chini hata idadi ya majaribio inapokua hadi maelfu. Panga suti kama piramidi: [majaribio ya kitengo](https://en.wikipedia.org/wiki/Unit_testing) mengi ya haraka, majaribio machache ya ujumuishaji, na idadi ndogo ya majaribio ya mwisho-hadi-mwisho. Kisha maoni mengi yanafika kwa sekunde. Ondoa majaribio yasiyotegemewa bila huruma. Jaribio linalofeli mara kwa mara ni baya kuliko kutokuwa na jaribio, kwa sababu linawafundisha wahandisi kupuuza kushindwa. Toa mazingira ya muda mfupi, ya kuombwa ili majaribio ya ujumuishaji na ya mwisho-hadi-mwisho yaendeshe dhidi ya miundombinu halisi, iliyotengwa.

### Otomatisha utoaji, uzingatiaji, na ukusanyaji wa ushahidi

Panua uotomatishaji zaidi ya majaribio hadi mtiririko wa kazi wa utoaji na uzingatiaji. Acha bomba lizalishe kiotomatiki mabaki ambayo wakaguzi wanahitaji: rekodi za nani aliidhinisha badiliko, majaribio gani yaliendesha na kupita, uchanganuzi wa usalama ulipata nini, na hasa mabaki gani yalisambazwa. Chukulia vidhibiti kama msimbo, ili ukaguzi unaohitajika utekelezwe kwa usawa na matokeo yake yaandikwe. "Uzingatiaji-kama-msimbo" huu hugeuza ukusanyaji wa ushahidi kutoka haraka ya mkono kabla ya ukaguzi kuwa rekodi endelevu, ya kisasa daima. Pia hufanya msimamo wa uzingatiaji wa mfumo uonekane wakati wowote.

### Pokea ChatOps na vitabu vya mwongozo-kama-msimbo

Simba taratibu za uendeshaji kama vitabu vya mwongozo vinavyotekelezeka vilivyohifadhiwa kwenye udhibiti wa matoleo, badala ya nyaraka za nathari zinazoteleza kupitwa na wakati. Mahali ambapo utaratibu ni salama na unaeleweka vizuri, uunganishe na uotomatishaji unaoweza kuuendesha kwa ombi. ChatOps huleta shughuli hizi kwenye kiolesura cha mazungumzo cha pamoja, ili waendeshaji wachochee na kuona vitendo vya kiotomatiki katika mazungumzo ya uwazi, ya ushirikiano, yaliyoandikwa. Hii inafanya shughuli zionekane kwa timu nzima na inaunda rekodi ya kiotomatiki ya kilichofanywa. Pia inapunguza kizuizi kwa wahandisi wasio na uzoefu mwingi kuendesha taratibu kwa usalama, kwa sababu uotomatishaji unasimba hatua sahihi.

### Tekeleza urekebishaji wa kiotomatiki kwa uangalifu

Kwa matatizo yanayoeleweka vizuri, yanayojirudia, jenga urekebishaji wa kiotomatiki unaogundua hali na kutumia suluhisho linalojulikana, kama kuanzisha upya mchakato ulioshindwa, kupanua chini ya mzigo, kusafisha diski iliyojaa, au kuhamisha kijenzi kwa kushindwa kwa mbadala. Anza na urekebishaji wa hatari ndogo, uhakika wa juu. Hitaji uthibitisho wa binadamu kwa chochote chenye eneo kubwa la mlipuko. Urekebishaji wa kiotomatiki hupunguza muda wa wastani wa kupona na kuondoa uchovu wa tahadhari unaojirudia. Lakini lazima ujengwe juu ya ugunduzi imara na ujumuishe kinga, kwa sababu uotomatishaji unaotenda kwa ishara ya uongo unaweza kukuza tukio. Andika kila kitendo cha kiotomatiki, ili waendeshaji wabaki na mwonekano kamili na waweze kuingilia.

### Weka uotomatishaji wa michakato ya roboti (RPA) mahali pake pazuri

[Uotomatishaji wa michakato ya roboti](https://en.wikipedia.org/wiki/Robotic_process_automation) huendesha violesura na programu zilizopo kuotomatisha kazi, ukiiga mibofyo na mibonyezo ya kibodi ambayo binadamu angefanya. RPA ina nafasi halali kama daraja kwa mifumo ya urithi au ya watu wengine isiyofichua API na isiyoweza kuunganishwa kwa njia nyingine yoyote. Itumie kwa vitendo kwa kesi hizo, lakini ujue mipaka yake. Uotomatishaji unaoendeshwa na kiolesura ni dhaifu kwa asili: unavunjika kiolesura kinapobadilika, na hautatui ukosefu wa msingi wa ujumuishaji. Mahali ambapo API halisi au ujumuishaji unapatikana, ipendelee. Chukulia RPA kama suluhisho la muda la kimbinu, si msingi wa kimkakati, na upange kuibadilisha mifumo inavyosasishwa.

### Otomatisha vidhibiti vya utawala, usalama, na gharama

Simba vidhibiti vya shirika kama ukaguzi wa kiotomatiki unaoendesha mfululizo: sera-kama-msimbo kwa vizuizi vya miundombinu, uchanganuzi wa kiotomatiki wa usalama kwenye mabomba, na ugunduzi wa kiotomatiki wa mikengeuko ya gharama na rasilimali zisizotumika. Kuotomatisha utawala hufanya vidhibiti viwe vya usawa na visivyoweza kukwepwa, na vinapanuka hadi kiasi cha mabadiliko ambacho mapitio ya mkono hayangeweza kufunika. Mbinu ileile inayotekeleza sera ya usalama inaweza kuweka alama ankara ya wingu inayokimbia au lebo inayohitajika iliyokosekana. Utawala unahama kutoka ukaguzi wa mkono wa mara kwa mara hadi kizuizi endelevu cha kiotomatiki.

## Mabadilishano: faida na hasara

| Chaguo | Faida | Hasara | Inafaa zaidi |
|---|---|---|---|
| Majaribio mapana ya kiotomatiki | Maoni ya haraka, thabiti; huwezesha mabadiliko | Gharama ya kujenga na kudumisha; hatari ya kutokutegemewa | Timu zote kwa ukubwa |
| Uzingatiaji-kama-msimbo | Ushahidi endelevu, tayari kwa ukaguzi | Uhandisi wa awali wa kusimba vidhibiti | Mashirika yanayodhibitiwa |
| Vitabu vya mwongozo-kama-msimbo + ChatOps | Shughuli zinazorudiwa, zinazoonekana, zilizoandikwa | Juhudi ya kusimba na kudumisha | Timu zenye mzigo halisi wa uendeshaji |
| Urekebishaji wa kiotomatiki | Kupona kwa kasi; kazi ndogo ya kuchosha | Hatari ikiwa ugunduzi si sahihi | Matatizo yanayojirudia yanayoeleweka vizuri |
| RPA (uotomatishaji wa kiolesura) | Huunganisha mifumo isiyo na API | Dhaifu; huficha mapengo ya ujumuishaji | Mifumo ya urithi kama suluhisho la muda |
| Utawala wa kiotomatiki | Vidhibiti vya usawa, visivyoweza kukwepwa | Juhudi ya kuandika na kurekebisha sera | Maeneo makubwa yanayotawaliwa |

Mabadilishano ya kati ni uwekezaji wa awali dhidi ya kazi ya kuchosha inayoendelea na hatari. Uotomatishaji daima hugharimu juhudi kujenga na kudumisha. Uotomatishaji uliojengwa vibaya, iwe majaribio yasiyotegemewa, RPA dhaifu, au urekebishaji unaochochewa na ishara mbaya, unaweza kuwa mbaya kuliko kutokuwepo, kwa sababu unamomonyoa uaminifu au unakuza kushindwa. Nidhamu ni ya sehemu tatu: otomatisha kinachoweza kurudiwa na kutegemewa kweli, wekeza kufanya uotomatishaji huo uaminike, na weka binadamu kwenye mzunguko pale hukumu au hatari kubwa inapodai. Ukifanywa vizuri, uotomatishaji hulipa mara nyingi. Ukifanywa kwa uzembe, unakuwa dhima yenyewe.

## Maswali ya kujadili na timu yako

1. **Majaribio yenu ya ujumuishaji na ya mwisho-hadi-mwisho yanaendesha dhidi ya mazingira halisi, ya muda mfupi, au dhidi ya sanduku la pamoja la maandalizi ambalo kila mtu anapigania?** Mazingira ya kuombwa yaliyotengwa kwa kila ombi la kuvuta huacha majaribio ya ujumuishaji na ya mwisho-hadi-mwisho kutumia miundombinu halisi bila timu kuzuiana au kuchafua hali ya pamoja. Mazingira moja ya pamoja ya maandalizi yanakuwa kizuizi na chanzo cha kushindwa kusiko thabiti, kunakotegemea mpangilio timu zaidi zinapojazana. Amua kama mnaweza kuanzisha mazingira ya muda mfupi, yanagharimu nini, na majaribio yapi yanayoyahitaji kweli dhidi ya mbadala wa haraka wa kumbukumbu. Leta data: maandalizi yanagombewa mara ngapi, kushindwa ngapi kunatokana na usumbufu wa mazingira ya pamoja, na muda wa sasa wa saa ya ukutani wa daraja la ujumuishaji. Jibu linaumba kutegemewa kwa majaribio yenu na jinsi tabaka za juu za piramidi zinavyorudisha maoni haraka.

2. **Taratibu za uendeshaji zimesimbwa kama vitabu vya mwongozo-kama-msimbo na kuonyeshwa kupitia ChatOps, au bado zinaishi kama nathari inayoteleza kupitwa na wakati?** Vitabu vya mwongozo vilivyosimbwa, vyenye udhibiti wa matoleo vinajaribika na kutekelezeka, na kuviendesha kupitia kiolesura cha mazungumzo cha pamoja hufanya kila kitendo kionekane na kuandikwa kiotomatiki. Hilo linapunguza kizuizi kwa mhandisi wa simu ya dharura asiye na uzoefu mwingi kutenda kwa usalama, kwa sababu uotomatishaji unasimba hatua sahihi badala ya kutegemea kumbukumbu ya kikabila. Amua taratibu zipi ni salama na zinaeleweka vya kutosha kuunganisha kwanza, na jinsi mnavyomwacha binadamu aweze kuingilia. Kwa eneo kubwa uwazi huu unafanya kazi pia kama rekodi ya ukaguzi ya nani alifanya nini na lini. Leta vitabu vyenu vya mwongozo vya sasa, taja vipi vimepitwa na wakati, na utambue taratibu mbili au tatu zinazoendeshwa mara nyingi zaidi za kusimba kwanza.

3. **Kwenye bomba lenu, ni uchanganuzi gani wa usalama na ukaguzi wa sera unaozuia muungano, na upi unaonya tu?** Utawala wa kiotomatiki unastahili kujengwa tu ikiwa vidhibiti haviwezi kukwepwa, kwa sababu ukaguzi unaoonya tu hupuuzwa chini ya shinikizo la tarehe ya mwisho kama sera ya wiki. Amua, kidhibiti kwa kidhibiti, kipi kinazuia na kipi kinaonya: udhaifu muhimu au lebo ya usimbaji fiche iliyokosekana pengine inazuia, wakati matokeo ya mtindo ya kiwango cha chini yanaweza kuonya. Kwa ukubwa hivi ndivyo mnavyotekeleza vizuizi vya usalama na gharama kwa usawa kuvuka kiasi cha mabadiliko ambacho mapitio ya mkono hayangeweza kufunika. Leta orodha yenu ya sasa ya ukaguzi na uweke alama kila moja kama inayozuia au ya ushauri, kisha mjadili kiwango cha chanya za uongo, kwa sababu ukaguzi wenye kelele unaozuia unawafundisha watu kudai ubaguzi. Mstari kati ya kuzuia na kuonya ndipo utawala wenu unapokuwa na meno au la.

4. **Ni urekebishaji gani wa kiotomatiki tuko tayari kuuacha utende bila binadamu kuthibitisha kwanza, na eneo la mlipuko ni nini ikiwa ugunduzi si sahihi?** Urekebishaji wa kiotomatiki hupunguza muda wa kupona na uchovu wa tahadhari, lakini suluhisho linalochochewa na ishara ya uongo linaweza kugeuza hitilafu ndogo kuwa kukatika kamili, kwa hiyo uamuzi wa nini kinaendesha bila usimamizi ni uamuzi wa hatari, si wa urahisi. Pima mivutano inayoshindana: kitendo bila usimamizi ni cha haraka zaidi lakini chenye hatari zaidi, wakati uthibitisho wa binadamu-kwenye-mzunguko ni salama zaidi lakini unarudisha ucheleweshaji na kazi ya kuchosha mliyotaka kuondoa. Leta urekebishaji wa wagombea ulioorodheshwa kwa mzunguko na kwa eneo baya zaidi la mlipuko, kiwango cha kihistoria cha chanya za uongo cha ugunduzi nyuma ya kila moja, na kama kila kitendo kimeandikwa na kinaweza kurudishwa. Kwa eneo kubwa la shirika au serikali, ongeza mamlaka rasmi ya mabadiliko na mpango wa kurudisha nyuma kwa chochote kinachogusa data ya uzalishaji au huduma zinazowakabili raia, kwa sababu urekebishaji wa kiotomatiki usioweza kukaguliwa au kutenduliwa ni ule ambao mdhibiti atawalazimisha kuuzima.

5. **Tunafadhili na kugawa umiliki vipi kwa kudumisha uotomatishaji wetu ili usioze kuwa dhima?** Majaribio, vitabu vya mwongozo, ukaguzi wa sera, na roboti za RPA vyote huoza mifumo inayovizunguka inapobadilika, na uotomatishaji uliopuuzwa ni mbaya kuliko kutokuwepo: kitabu cha mwongozo kilichopitwa na wakati kinatoa imani ya uongo wakati wa mgogoro na roboti ya RPA iliyoharibika inaacha kazi kimyakimya. Mvutano ni kwamba matengenezo yanashindana na kazi ya vipengele kwa wahandisi walewale, na hayaonekani hadi kitu kivunjike, kwa hiyo ndicho cha kwanza kupunguzwa chini ya shinikizo la tarehe ya mwisho. Leta orodha ya sasa ya mali za uotomatishaji, mrundikano wa majaribio yasiyotegemewa na roboti zilizoharibika, na makadirio ya uaminifu ya saa za wahandisi zinazoenda tayari kwenye matunzo dhidi ya kilichowekwa bajetini. Katika mazingira ya mashirika makubwa au serikali, taja mmiliki anayewajibika kwa kila uotomatishaji muhimu na ufadhili matengenezo yake kama kipengele wazi cha bajeti, kwa sababu wakaguzi na mapitio ya matukio yataulizia nani alikuwa na jukumu kidhibiti kisichotunzwa kiliposhindwa kimyakimya.

6. **Kwa kila mfumo wa urithi tunaouotomatisha kwa RPA, mpango halisi na kichocheo cha kustaafisha RPA hiyo kwa niaba ya ujumuishaji halisi ni nini?** RPA ni daraja halali kwa mifumo isiyofichua API, lakini daraja lisilo na mpango wa kutoka hugeuka kimyakimya kuwa miundombinu ya kudumu, dhaifu inayovunjika kwa kila badiliko la kiolesura na kuimarisha pengo la ujumuishaji lililopaswa kulivuka. Mabadilishano ni halisi: RPA hutoa thamani kwa haraka na kwa bei nafuu sasa, wakati ujumuishaji sahihi wa API unagharimu zaidi mapema lakini ni wa kudumu, kwa hiyo nidhamu ni kuchukulia RPA kama mkopo wenye tarehe, si ununuzi. Leta orodha ya roboti za RPA zilizo kwenye uzalishaji, mifumo ambayo kila moja inategemea, mara ngapi kila moja inavunjika, na kama juhudi ya usasishaji au ujumuishaji imefadhiliwa na kupangwa kweli kwa mfumo wa msingi. Kwa maeneo ya mashirika makubwa na serikali yanayobeba programu kuu za miongo kadhaa, funga kila roboti ya RPA na hatua iliyotajwa ya usasishaji, kwa sababu RPA iliyokuwa muhimu kimyakimya bila tarehe ya kustaafisha ni deni la kiufundi linalojilimbikiza kila mwaka kiolesura inachokwangua kinapoendelea kubadilika.

## Mtazamo wa sekta

**Kampuni changa.** Ukiwa na wahandisi wawili au watatu na bila muda wa kujenga miundombinu, weka piramidi ndogo, ya haraka ya majaribio inayoendesha ndani ya dakika chache kwa kila badiliko, na uchukulie jaribio lolote lisilotegemewa kama hitilafu halisi ya kurekebisha au kufuta wiki hiyo. Ruka zana nzito za uzingatiaji na sera-kama-msimbo ambazo huzihitaji bado, na usimbe tu marekebisho yako mawili au matatu ya uendeshaji yanayoendeshwa mara nyingi zaidi kama hati rahisi zinazochochewa kutoka kwenye mazungumzo. Otomatisha kinachoondoa kazi ya kuchosha ya kila siku, na pinga kujenga mitambo ya utawala kabla hujapata tatizo la utawala.

**Biashara ndogo.** Bila mtaalamu maalumu wa majaribio au jukwaa, egemea uotomatishaji uliojengwa kwenye zana ambazo tayari unalipia: waendeshaji wa majaribio waliojengwa ndani wa huduma ya CI, viongezi vyake vya uchanganuzi, na mazingira yanayosimamiwa badala ya kujenga miundombinu ya majaribio ya kipekee. Weka uamuzi wa kununua-dhidi-ya-kujenga kwenye matengenezo unayoweza kuyadumisha kwa uhalisia, kwa sababu bomba la kipekee la busara ambalo hakuna anayeweza kulidumisha ni matokeo mabaya kuliko la kawaida lililopangishwa. Tumia RPA kwa kiasi na tu pale zana ya muuzaji inapounganisha mfumo ambao huwezi kuuunganisha kwa njia nyingine yoyote.

**Biashara kubwa.** Kuvuka timu nyingi lengo ni vidhibiti vya usawa, visivyoweza kukwepwa kwa ukubwa ambao mapitio ya mkono hayawezi kufunika: miundombinu ya majaribio sambamba ya pamoja yenye mazingira ya muda mfupi, vizuizi vya sera-kama-msimbo, na ushahidi wa uzingatiaji unaozalishwa kiotomatiki kutoka kila uendeshaji wa bomba. Sawazisha violesura ili timu zitumie tena zana za urekebishaji na vitabu vya mwongozo badala ya kila moja kubuni upya hati dhaifu, na simamia uotomatishaji kama jalada linalomilikiwa, lililofadhiliwa lenye bajeti wazi za matengenezo. Angalia kwamba ukaguzi unaoonya tu kwa timu moja haukuchukuliwa kama unaozuia kwa nyingine, kwa sababu utekelezaji usio thabiti unadhoofisha uhakikisho mnaolipia.

**Serikali.** Kanuni za ununuzi, wajibu wa uwazi, na maagizo ya ufuatiliaji endelevu hufanya uzingatiaji-kama-msimbo kuwa karibu muhimu: kila uendeshaji wa bomba unapaswa kurekodi vidhibiti vilivyokaguliwa, uchanganuzi uliofanywa, na idhini zilizotolewa kama ushahidi usioweza kuchezewa, tayari kwa ukaguzi. Pendelea uotomatishaji wazi, unaohamishika kuliko kufungwa kwa umiliki ili mkataba wa baadaye uweze kuhamia kwa mtoaji mwingine, na umweke binadamu awajibike kwa urekebishaji wowote unaogusa huduma zinazowakabili raia. Mahali ambapo mfumo wa miongo kadhaa unalazimisha RPA, uandike kama daraja la makusudi, la muda lenye mpango wa umma wa usasishaji, na ushikilie ukaguzi wa utawala kwa msingi ulioagizwa wa usalama kwa kila badiliko.

## Mifano

**Kampuni changa.** Kampuni changa ya watu saba inaweka piramidi nyembamba ya majaribio ya kitengo ya haraka kwa kiasi kikubwa pamoja na majaribio machache ya ujumuishaji, yote yakiendesha sambamba ili suti kamili ikamilike chini ya dakika tatu kwa kila ombi la kuvuta. Jaribio linapoanza kukosa utegemezi, wanalichukulia kama hitilafu halisi na kulirekebisha au kulifuta wiki hiyo, kwa sababu kwa timu ndogo hivyo ujenzi mmoja mwekundu uliopuuzwa ungemomonyoa uaminifu kwa suti nzima. Pia wanasimba marekebisho yao mawili ya kawaida ya uendeshaji, kuanzisha upya mfanyakazi aliyekwama na kusafisha diski iliyojaa, kama hati ndogo zinazochochewa kutoka Slack, ili yeyote aliye kwenye simu ya dharura aweze kuziendesha kwa usalama bila kumwita mhandisi mmoja aliyeziandika.

**Biashara kubwa.** Kampuni kubwa ya biashara mtandaoni inaendesha suti ya majaribio ya makumi ya maelfu, iliyoendeshwa sambamba kuvuka meli ya wafanyakazi ili suti kamili ikamilike ndani ya dakika. Mazingira ya muda mfupi yanaanzishwa kwa kila ombi la kuvuta kwa majaribio halisi ya ujumuishaji. Shughuli zinaendeshwa kupitia ChatOps: wahandisi wa simu ya dharura wanachochea vitabu vya mwongozo vilivyosimbwa kutoka mazungumzoni, na kushindwa kwa kawaida kama huduma iliyozidiwa kunarekebishwa kiotomatiki, kitendo kikiandikwa kwa mapitio. Bomba linakusanya ushahidi wa uchanganuzi wa usalama na idhini kiotomatiki, kwa hiyo ukaguzi wa kila mwaka unatumia rekodi ya kisasa daima badala ya uwindaji wa ushahidi wa mkono.

**Serikali.** Wakala wa umma unaokabiliwa na mahitaji makali ya ufuatiliaji endelevu unatekeleza uzingatiaji-kama-msimbo. Kila uendeshaji wa bomba unarekodi vidhibiti vilivyokaguliwa, uchanganuzi uliofanywa, na idhini zilizotolewa, ukizalisha ushahidi usioweza kuchezewa unaowaridhisha wakaguzi inapohitajika. Kwa sababu moja ya mifumo yake kuu ni programu ya miongo kadhaa isiyo na API, wakala unatumia RPA kama daraja la makusudi kuotomatisha uingizaji wa data ndani yake huku juhudi ya usasishaji ikiendelea, ukiwa na mpango wazi wa kustaafisha RPA ujumuishaji sahihi utakapokuwepo. Ukaguzi wa kiotomatiki wa utawala unatekeleza msingi ulioagizwa wa usalama kwa kila badiliko la miundombinu.

## Kesi ya biashara: sababu, ROI, na TCO

ROI ya uotomatishaji wa majaribio na mchakato inaonekana kama muda wa wahandisi uliorejeshwa, utoaji wa haraka na salama zaidi, kupona kwa kasi kutoka matukio, na gharama ya uzingatiaji iliyopungua sana. Majaribio ya kiotomatiki huwezesha mabadiliko ya haraka, yenye kujiamini ambayo ndio msingi wa utendaji wa utoaji. Shughuli na urekebishaji wa kiotomatiki hupunguza kazi ya kuchosha na muda wa kukatika unaochosha timu na bajeti. Uzingatiaji-kama-msimbo unaweza kugeuza ukaguzi kutoka wiki za maandalizi ya mkono kuwa swali la kawaida, akiba ya kifedha na ya sifa.

Ulinganisho wa TCO unapima gharama halisi, endelevu ya kujenga na kudumisha uotomatishaji dhidi ya gharama ya kutoutomatisha. Majaribio na shughuli za mkono hazigharimu tu saa zinazotumika. Zinagharimu pia kasoro zinazotoroka, matukio yanayodumu kwa muda mrefu, ukaguzi unaotumia wafanyakazi maalumu, na uchovu wa wahandisi wanaofanya kazi ya kuchosha inayojirudia. Kwa uongozi, hoja ni ya moja kwa moja: uotomatishaji hubadilisha gharama ya uendeshaji inayojirudia na hatari kuwa uwekezaji wa mara moja pamoja na matengenezo unaopanuka, na hufanya ubora na uzingatiaji viwe endelevu badala ya vya vipindi. Tahadhari moja inastahili kutajwa wazi. Uotomatishaji lazima udumishwe na uaminiwe; uotomatishaji usiofadhiliwa, uliopuuzwa huoza kuwa dhima.

## Mifumo mibaya na mitego

- **Majaribio yasiyotegemewa yanavumiliwa.** Kushindwa kwa vipindi huharibu uaminifu na kuwafundisha wahandisi kupuuza matokeo mekundu.
- **Kuotomatisha mchakato uliovunjika.** Kuotomatisha mtiririko mbaya wa kazi kunafanya fujo itokee haraka zaidi tu; rekebisha mchakato kwanza.
- **RPA kama mkakati.** Kutegemea uotomatishaji dhaifu wa kiolesura kama suluhisho la kudumu kunaficha na kuimarisha mapengo ya ujumuishaji.
- **Urekebishaji bila ugunduzi imara.** Marekebisho ya kiotomatiki yanayochochewa na ishara mbaya yanaweza kukuza tukio.
- **Vitabu vya mwongozo kama nathari iliyopitwa na wakati.** Taratibu zinazoishi kwenye nyaraka zilizopitwa na wakati zinatoa imani ya uongo wakati wa mgogoro.
- **Ushahidi wa uzingatiaji unakusanywa kwa mkono.** Uwindaji wa mara kwa mara wa ushahidi wa mkono ni ghali na unaacha mapengo kati ya ukaguzi.
- **Hakuna binadamu kwenye mzunguko kwa vitendo vya hatari kubwa.** Uotomatishaji kamili wa shughuli hatari unaondoa hukumu inayozuia maafa.

## Kielelezo cha ukomavu

**Ngazi ya 1, Kuanzisha.** Majaribio na shughuli kwa kiasi kikubwa ni za mkono na za kuitikia. Ufunikaji ni wa papo hapo, taratibu zinaishi vichwani mwa watu au nyaraka zilizopitwa na wakati, urekebishaji unafanyika kwa mkono wakati wa matukio, na ushahidi wa uzingatiaji unakusanywa kwa haraka kabla ya kila ukaguzi.

**Ngazi ya 2, Kuendeleza.** Majaribio ya kiotomatiki yapo lakini ni ya polepole, hayategemeki, au yanaendesha bila uthabiti, na mazoea yanatofautiana sana kati ya timu. Baadhi ya hati za uendeshaji na vitabu vya mwongozo vipo katika mifuko, lakini urekebishaji bado ni wa mkono na utawala unatekelezwa kwa mapitio ya mara kwa mara badala ya ukaguzi endelevu.

**Ngazi ya 3, Kusawazisha.** Miundombinu ya majaribio ya haraka, sambamba, ya kutegemewa ndio kiwango kilichoandikwa kote shirikani. Vitabu vya mwongozo-kama-msimbo na ChatOps vinatumika kwa ujumla, ushahidi wa uzingatiaji unazalishwa kiotomatiki kutoka kwa uendeshaji wa bomba, na vidhibiti vya utawala vinaendesha kama ukaguzi wa kiotomatiki unaotekelezwa unaotumika kwa uthabiti kuvuka timu.

**Ngazi ya 4, Kusimamia.** Uotomatishaji wenyewe unapimwa na kudhibitiwa dhidi ya vipimo vya msingi. Mnafuatilia kiwango cha majaribio yasiyotegemewa, muda wa saa ya ukutani wa suti, muda wa wastani wa kupona kwa matukio yaliyorekebishwa kiotomatiki, sehemu ya vidhibiti vyenye ushahidi wa kiotomatiki, na viwango vya chanya za uongo kwenye ukaguzi unaozuia, na mnashikilia kila kipimo kwenye lengo lililokubaliwa. Maamuzi ya urekebishaji na ufunikaji yanaendeshwa na data hii, na kila kitendo cha kiotomatiki kimeandikwa ili mielekeo na kurudi nyuma vionekane badala ya kukisiwa.

**Ngazi ya 5, Kuratibu.** Uotomatishaji unaboreshwa mfululizo na kuunganishwa kuvuka shirika. Urekebishaji wa kiotomatiki unashughulikia matukio ya kawaida kwa kinga zilizothibitishwa, uzingatiaji ni endelevu na tayari kwa ukaguzi daima, na mnyororo wa zana za majaribio, uendeshaji, na utawala unajirekebisha mifumo inapobadilika, huku madaraja ya RPA yakistaafishwa kikamilifu ujumuishaji unapokomaa. Binadamu wanalenga hukumu huku mashine zikishughulikia yanayoweza kurudiwa, na mfumo mzima unajisawazisha upya kwa ushahidi.

## Mawazo ya kujadili

- Taratibu zipi za uendeshaji ni salama kuotomatisha kikamilifu, na zipi lazima zibaki na binadamu kwenye mzunguko?
- Mnaiwekaje suti kubwa ya majaribio ikiwa ya haraka na bila kutokutegemewa inapokua?
- RPA inahalalishwa wapi kama daraja kwa mifumo yenu ya urithi, na mpango wa kuistaafisha ni upi?
- Ni vidhibiti gani vingeweza kubadilishwa kutoka ukaguzi wa mkono hadi uzingatiaji-kama-msimbo endelevu kwanza?
- Mnajengaje uaminifu katika urekebishaji wa kiotomatiki bila kuhatarisha matukio yaliyokuzwa?
- Mnafadhili vipi matengenezo endelevu ambayo uotomatishaji unahitaji ili usioze kuwa dhima?

## Mambo muhimu ya kukumbuka

- Otomatisha kinachojirudia, kinachotabirika, na kinachotegemea kanuni; hifadhi juhudi ya binadamu kwa hukumu na maamuzi ya hatari kubwa.
- Fanya majaribio ya kiotomatiki yawe ya haraka, sambamba, na ya kutegemewa, na uondoe kutokutegemewa bila huruma.
- Simba shughuli kama vitabu vya mwongozo-kama-msimbo na uziwasilishe kupitia ChatOps kwa mwonekano na rekodi.
- Zalisha ushahidi wa uzingatiaji kiotomatiki ili ukaguzi utegemee rekodi endelevu, ya kisasa.
- Tumia RPA tu kama daraja la makusudi, la muda kwa mifumo isiyo na API, na upange kustaafishwa kwake.
- Tekeleza vidhibiti vya utawala, usalama, na gharama kama ukaguzi endelevu wa kiotomatiki, binadamu wakisimamia vitendo hatari.

## Marejeo na usomaji zaidi

- Lisa Crispin and Janet Gregory, *Agile Testing: A Practical Guide for Testers and Agile Teams*.
- Jez Humble and David Farley, *Continuous Delivery*.
- Betsy Beyer, Chris Jones, Jennifer Petoff, and Niall Richard Murphy (eds.), *Site Reliability Engineering* (see the chapter on eliminating toil).
- Gene Kim, Jez Humble, Patrick Debois, and John Willis, *The DevOps Handbook*.
- Nicole Forsgren, Jez Humble, and Gene Kim, *Accelerate*.
- NIST Special Publication 800-53 and 800-137 (continuous monitoring).
- Open Policy Agent documentation (policy as code).
