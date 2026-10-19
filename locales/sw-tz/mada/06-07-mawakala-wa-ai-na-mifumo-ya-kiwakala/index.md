# 6.7 Mawakala wa AI na mifumo ya kiwakala

## Muhtasari na msukumo

**Wakala wa AI** ni [mfano mkubwa wa lugha](https://en.wikipedia.org/wiki/Large_language_model) (LLM) uliofungwa kwenye mzunguko: unapewa lengo, unaweza kuita zana, unadumisha kumbukumbu fulani ya ulichofanya, na unaamua hatua yake inayofuata mwenyewe hadi lengo litimie au ukate tamaa. Mzunguko huo ndio tofauti yote kati ya wakala na miito ya kawaida ya agizo-jibu ya sura ya 6.3. Mwito mmoja hujibu swali. Wakala husoma barua pepe yake, hutafuta hifadhidata, hufungua tiketi, hukagua matokeo, na hujaribu tena. Mfano hauzalishi maandishi tu tena; unachagua vitendo katika mifumo yako.

Mabadiliko hayo hubadilisha tatizo la kihandisi. Mfano unapoandika maneno tu, matokeo mabaya ni sentensi mbaya. Mfano unapoendesha zana, matokeo mabaya yanaweza kutuma ujumbe usio sahihi, kufuta rekodi, au kuhamisha fedha. Kwa hiyo [wakala mwerevu](https://en.wikipedia.org/wiki/Intelligent_agent) anaeleweka vizuri zaidi kama mpangaji asiyeaminika aliyekaa ndani ya mfumo unaoaminika, na kazi yako nyingi inaenda kwenye kubana kile mpangaji huyo anaruhusiwa kufanya. Sura hii inajengwa moja kwa moja juu ya misingi ya LLM ya sura ya 6.3, masuala ya uaminifu na uwajibikaji ya sura ya 6.5, na mazoea ya jukwaa ya sura ya 6.6.

Kwa timu kubwa dau ni la kishirika kama lilivyo la kiufundi. Mashirika yanataka mawakala waunganishwe kwenye mifumo halisi ya ndani (tiketi, fedha, rekodi za wateja), jambo linalomaanisha mawakala hurithi vidhibiti halisi vya ufikiaji na wajibu halisi wa usimamizi wa mabadiliko. Serikali huongeza uwajibikaji wa umma: kitendo cha kujiendesha kinachomwathiri raia lazima kielezeke, kisimamiwe, na kikaguliwe baadaye. Mfumo huu una nguvu. Ukisambazwa bila nidhamu, ni njia ya haraka ya kuotomatisha makosa.

## Kanuni kuu

- Wakala ni mfano pamoja na mzunguko, zana, kumbukumbu, na lengo. Hatari inaishi kwenye mzunguko, si nathari.
- Banisha uhuru kwa kazi. Toa uhuru mdogo zaidi unaokamilisha kazi.
- Pendelea mtiririko uliowekwa hatua zinapojulikana. Fikia uhuru usio na mipaka tu zisipojulikana.
- Chukulia kila zana kama uso wa shambulio na ipe upendeleo mdogo zaidi inayoweza kufanya nao kazi.
- Weka binadamu kwenye mzunguko kwa vitendo vyenye athari au visivyoweza kurekebishwa, na ufanye kubatilisha kuwe nafuu.
- Tathmini kwa mafanikio ya kazi, si jinsi nakala inavyosomeka.
- Fuatilia kila mbio. Kitendo usichoweza kukijenga upya ni kitendo usichoweza kukitawala.
- Muundo rahisi zaidi unaofanya kazi kwa kawaida ndio sahihi. Mara nyingi hiyo si wakala kabisa.

## Mapendekezo

### Anza na mtiririko, ongeza uhuru pale tu unapolazimika

Kosa la kawaida zaidi ni kuchukua wakala anayejiendesha wakati bomba lililowekwa lingetosha. Kama tayari unajua hatua (toa nyanja, zithibitishe, tafuta rekodi, andaa jibu), ziandike kama mtiririko ulioratibiwa ukiwa na mfano unaojaza nafasi mahususi. Uhuru hustahili nafasi yake pale njia kweli haiwezi kuamuliwa mapema, kwa mfano utafiti wa wazi au upangaji kuvuka zana nyingi zinazowezekana. Banisha uhuru kwa kazi: weka kikomo cha idadi ya hatua, banisha seti ya zana kwa kile lengo hili linahitaji, na uweke sharti wazi la kusimama. Kanuni nzuri ni kumpa mfano uhuru kama tatizo linavyodai hasa na si digrii moja zaidi.

### Fanya matumizi ya zana kuwa uwezo wa msingi, na uyafanye salama

Matumizi ya zana (pia huitwa kuita kazi) ndiyo yanayogeuza mfano kuwa wakala. Fafanua kila zana kwa skima sahihi, thibitisha kila hoja ambayo mfano unatoa, na utumie [kanuni ya upendeleo mdogo](https://en.wikipedia.org/wiki/Principle_of_least_privilege): wakala wa kuripoti wa kusoma tu anapata vitambulisho vya kusoma tu, kamwe si ufikiaji wa kuandika anaoweza kuutumia vibaya. Endesha zana ndani ya [sandbox](https://en.wikipedia.org/wiki/Sandbox_(computer_security)) ili mwito mbaya usifikie zaidi ya eneo lake la mlipuko. Pendelea zana nyingi nyembamba za madhumuni moja kuliko chache pana, kwa sababu zana nyembamba ni rahisi kufikiria, kutoa ruhusa, na kukagua. Huu ni uangalifu ule ule ambao sura ya 6.3 inahimiza kwa matumizi ya zana ya LLM, ukifanywa wa kati.

### Tumia mifumo ya wazi ya kufikiria na kupanga

Mawakala hufanya kazi vizuri zaidi mawazo yao yanapokuwa na muundo. Katika mfumo wa fikiria-na-tenda (ulioenezwa na utafiti wa ReAct), mfano hubadilishana kati ya kufikiria hali na kuchukua kitendo, kisha huchunguza matokeo kabla ya kufikiria tena. Kwa malengo magumu zaidi, mfanye mfano apange kwanza (agawanye katika kazi ndogo) kisha atekeleze, ili uweze kuchunguza na hata kuidhinisha mpango kabla zana yoyote haijaendesha. Weka mizunguko hii ikionekana na ikikatizika. Mpango unaoweza kuusoma ni mpango unaoweza kuusimamisha.

### Weka binadamu kwenye mzunguko kwa vitendo vyenye athari

Amua, kwa kila zana na kila kitendo, kama mfano unaweza kutenda peke yake au lazima aulize kwanza. Vitendo vinavyorekebishika, vya dau dogo (kutafuta, kuandaa rasimu) vinaweza kuendeshwa bila kusimamiwa. Vyenye athari au visivyorekebishika (kutuma mawasiliano ya nje, kuhamisha fedha, kubadilisha data ya uzalishaji, kuamua kesi ya raia) vinahitaji lango la [binadamu-kwenye-mzunguko](https://en.wikipedia.org/wiki/Human-in-the-loop) lenye mamlaka halisi ya kusema hapana. Sanifu kwa kurekebishika popote unapoweza: pendelea kuweka badiliko hatua kuliko kulithibitisha, na ufanye kutendua kuwe kipengele cha daraja la kwanza ili kitendo cha makosa kigharimu dakika, si tukio.

### Chukulia mfumo wa usalama kama wa uadui

Mawakala hupanua uso wa shambulio ulioelezwa katika sura ya 4.2. Tishio kuu ni [sindano ya maagizo](https://en.wikipedia.org/wiki/Prompt_injection): maagizo hasidi yaliyofichwa katika ukurasa wa wavuti, hati, au barua pepe ambayo wakala anasoma na kutii. Linalohusiana kwa karibu ni [tatizo la naibu aliyechanganyikiwa](https://en.wikipedia.org/wiki/Confused_deputy_problem), ambapo mshambulizi anamdanganya wakala mwenye upendeleo atumie vibaya ufikiaji wake halali mwenyewe, kwa mfano kutoa data kupitia zana ambayo wakala anaruhusiwa kuita. Dhania maudhui yoyote ambayo wakala anameza yanaweza kuwa ya uadui. Tenganisha maagizo yanayoaminika na data isiyoaminika, bana zana ili wakala aliyetekwa asiweze kufikia mifumo nyeti, na usiruhusu kamwe matokeo ghafi ya mfano kuchochea kitendo kisichorekebishika bila uthibitishaji.

### Tathmini kwa mafanikio ya kazi na jaribu regression ya kutoamuliwa

Hukumu mawakala kwa kama wanakamilisha kazi, si kama nakala inasikika ya akili. Jenga seti ya tathmini ya malengo ya uwakilishi yenye vigezo vya mafanikio vinavyokaguliwa (je, tiketi ilipata kipaumbele sahihi, je, urejeshaji fedha ulilingana na sera) na uiendeshe kwa kila badiliko la agizo, mfano, au zana. Kwa kuwa mawakala hawaamuliwi, mbio moja inathibitisha kidogo: endesha kila kesi mara kadhaa na ufuatilie kiwango cha mafanikio, si kupita au kushindwa. Hii inapanua nidhamu ya tathmini ya nje na ya mtandaoni ya sura ya 6.3 na 6.2 (uhandisi wa kujifunza kwa mashine na MLOps) kwa mifumo ambayo matokeo yake ni mfuatano wa vitendo.

### Weka vifaa vya kupima kwa uonekanaji, gharama, na ushughulikiaji wa kushindwa

Huwezi kutawala usichoweza kuona. Fuatilia kila mbio ya wakala mwanzo hadi mwisho (sura ya 6.6): lengo, kila hatua ya kufikiria, kila mwito wa zana na hoja zake na matokeo, tokeni zilizotumika, na matokeo ya mwisho. Ufuatiliaji huu ni kitatuzi chako, nyayo zako za ukaguzi, na kipimo chako cha gharama kwa wakati mmoja. Weka bajeti ngumu kwa hatua, muda, na matumizi, kwa sababu wakala anayezunguka anaweza kuchoma ucheleweshaji na fedha haraka. Shughulikia kushindwa waziwazi: jaribu tena makosa ya zana ya muda kwa kurudi nyuma, lakini gundua mizunguko ambapo mfano unarudia kitendo kinachoshindwa, na ushindwe kwa usalama badala ya kukorogana.

## Mabadilishano: faida na hasara

| Chaguo | Faida | Hasara | Bora wakati |
|---|---|---|---|
| Mtiririko uliowekwa (mfano unajaza nafasi) | Unaotabirika, nafuu, rahisi kujaribu na kukagua | Mgumu; unavunjika kwenye njia zisizotarajiwa | Hatua zinajulikana mapema |
| Wakala mmoja anayejiendesha | Unyumbulifu; unashughulikia malengo ya wazi | Ngumu zaidi kudhibiti, kutathmini, na kubana | Njia haiwezi kuamuliwa mapema |
| Uratibu wa mawakala wengi | Sambamba; majukumu maalumu | Gharama ya uratibu, makosa yanayojilimbikiza, matumizi ya juu | Kazi inagawanyika kweli kuwa sehemu huru |
| Kitendo bila kusimamiwa | Haraka, msuguano mdogo | Makosa yanatekelezwa bila ukaguzi | Vitendo vinarekebishika na vya dau dogo |
| Lango la binadamu-kwenye-mzunguko | Usalama, uwajibikaji, kurekebishika | Polepole; inahitaji uwezo wa wapitiaji | Vitendo vina athari au haviwezi kurekebishwa |

Mvutano wa msingi ni uhuru dhidi ya udhibiti. Uhuru zaidi unashughulikia hali nyingi zaidi lakini unadai vizuizi zaidi, tathmini zaidi, na fedha zaidi, na unashindwa kwa njia ngumu zaidi kutabiri. Miundo ya mawakala wengi huvutia timu kwa uzuri, hata hivyo kila wakala wa ziada anaongeza mzigo wa uratibu na mahali pengine kwa kosa dogo kujilimbikiza kuwa matokeo mabaya. Tatua mvutano kwa kuanza na uhuru mdogo zaidi unaotatua tatizo na kuongeza uhuru tu kazi madhubuti inapokulazimisha, daima ukioanisha na kizuizi kinacholingana.

## Maswali ya kujadili na timu yako

1. **Kipengele hiki kinahitaji wakala kweli, au mtiririko uliowekwa ungekuwa salama na nafuu zaidi?** Uhuru unashawishi, lakini kazi nyingi zina hatua zinazojulikana ambazo bomba lililoratibiwa huzishughulikia kwa hatari ndogo zaidi. Kwa timu kubwa, kuchagua mawakala kwa chaguo-msingi kunamaanisha kila kikundi kinachukua mzigo wa tathmini, ufuatiliaji, na usalama ambao muundo rahisi ungeepuka. Leta kazi mahususi na uliza kama hatua zake zinaweza kuamuliwa mapema; zikiweza, wakala huenda ni uhandisi wa kupita kiasi. Hifadhi uhuru usio na mipaka kwa malengo ambapo njia hutofautiana kweli kwa kila kesi. Jibu linapaswa kusukuma vipengele vingi kuelekea mtiririko na kuacha seti ndogo, ya makusudi kama mawakala wa kweli.

2. **Kwa kila zana ambayo wakala wetu anaweza kuita, jambo baya zaidi ambalo wakala aliyetekwa angeweza kufanya nayo ni lipi, na nini kinazuia hilo?** Sindano ya maagizo na mashambulizi ya naibu aliyechanganyikiwa hugeuza ufikiaji halali wa wakala mwenyewe dhidi yenu, kwa hiyo lenzi sahihi ni ya uadui (sura ya 4.2). Orodhesha kila zana, wigo wa upendeleo wake, na kama agizo hasidi lililoingizwa kupitia maudhui yaliyomezwa lingeweza kuifikia. Kwa mashirika yanayounganisha mawakala na mifumo ya ndani, hapa ndipo upendeleo mdogo, sandbox, na malango ya binadamu kwa vitendo visivyorekebishika vinapokuwa halisi. Leta orodha ya zana na vitambulisho ambavyo kila moja inashikilia. Kitendo chochote chenye athari kikifikika bila uthibitishaji au ukaguzi wa binadamu, hilo ndilo jambo la kwanza la kurekebisha.

3. **Tungejuaje kiwango cha mafanikio cha wakala kimeshuka, kwa kuwa kila mbio inaonekana ya kukubalika?** Mawakala hawaamuliwi, kwa hiyo nakala inayosomeka vizuri bado inaweza kuwa imechukua kitendo kisicho sahihi, na mbio moja ya kijani haithibitishi chochote. Uliza kama mna seti ya tathmini ya malengo yenye matokeo yanayokaguliwa, inayoendeshwa mara nyingi kwa kila kesi kuzalisha kiwango cha mafanikio badala ya kupita moja. Kwa usambazaji wa dau kubwa au wa umma, jadili jinsi ufuatiliaji wa mbio unavyokuruhusu kujenga upya hasa nini kilitokea kitu kinapoharibika (sura ya 6.5 na 6.6). Ishara yenu pekee ikiwa malalamiko ya watumiaji, tayari mmechelewa. Jibu linapaswa kufadhili zana ya tathmini kabla ya ukubwa, si baada ya tukio.

4. **Vitendo vipi vya wakala huyu haviwezi kurekebishwa kweli, nani ana mamlaka ya kuviidhinisha, na je, tuna uwezo wa wapitiaji wa kuajiri lango hilo?** Kishawishi ni kumruhusu mfano kutenda bila kusimamiwa kila mahali, lakini lango la binadamu ni halisi tu ikiwa mtu aliyetajwa mwenye mamlaka ya kusema hapana anapatikana wakala anapouliza. Kwa timu kubwa, foleni ya idhini ambayo hakuna anayeimiliki hugeuka kimyakimya kuwa muhuri wa mpira, na usalama mliobuni huyeyuka chini ya kiasi. Leta orodha kamili ya vitendo ambavyo wakala anaweza kuchukua, weka alama kila kimoja kinarekebishika au la, na ukadirie kiasi cha kila siku cha kesi za imani ya chini zitakazotua kwa mpitiaji. Pima msuguano na gharama ya uajiri ya lango dhidi ya eneo la mlipuko la kosa lisilosimamiwa, na upendelee kubuni upya kitendo kisichorekebishika kuwa cha hatua na kinachotendulika kuliko kuongeza mpitiaji mwingine. Katika mazingira ya mashirika makubwa na serikali, funga kila kitendo chenye athari na afisa anayewajibika na rekodi ya usimamizi wa mabadiliko, kwa sababu kitendo cha kujiendesha kinachomwathiri raia au mteja ambacho hakuna binadamu aliyekiidhinisha ndicho hasa kushindwa ambako ukaguzi utapata.

5. **Tunafikia muundo wa mawakala wengi kwa sababu kazi inagawanyika kweli, au kwa sababu inaonekana nzuri?** Kugawanya kazi kuvuka mawakala maalumu kunashawishi, hata hivyo kila wakala wa ziada anaongeza mzigo wa uratibu na mahali pengine ambapo kosa dogo hujilimbikiza kuwa matokeo mabaya. Kwa shirika kubwa gharama si matumizi na ucheleweshaji tu: mfumo wa mawakala wengi ni mgumu zaidi sana kufuatilia, kutathmini, na kufikiria unaposhindwa, kwa hiyo mzigo wa utawala huzidishwa na kila jukumu unaloongeza. Leta kazi na uonyeshe, kwa uhalisia, sehemu zipi zinaendeshwa kwa uhuru na sambamba, kisha linganisha kiwango cha mafanikio kilichopimwa na gharama ya toleo la mawakala wengi dhidi ya wakala mmoja kwenye seti ileile ya tathmini. Wakala mmoja akishinda au kulingana, muundo mzuri ni uhandisi wa kupita kiasi. Kwa usambazaji unaodhibitiwa au wa umma, kumbuka kila wakala katika mnyororo ni kijenzi kingine ambacho chombo cha usimamizi lazima kiweze kukikagua, kwa hiyo muundo wa ziada usioweza kuuhalalisha ni dhima ya ziada.

6. **Bajeti ngumu za hatua, muda, na matumizi ya wakala ni zipi, na wakala anayezunguka angenaswa vipi kabla hajapandisha gharama au ucheleweshaji?** Wakala anayerudia kitendo kinachoshindwa anaweza kuchoma fedha na muda bila onyo, kwa hiyo uhuru usio na mipaka ni hatari ya kifedha kama ilivyo ya usalama. Kwa timu kubwa inayoendesha mawakala wengi, mzunguko mmoja mbaya unaweza kupandisha ankara ya wingu au kumaliza kikomo cha kiwango kinachoinyima kila mzigo mwingine, jambo linalofanya vikomo vya kila mbio kuwa wasiwasi wa pamoja wa uendeshaji badala ya tatizo la timu moja. Leta bajeti za sasa za hatua, muda, na tokeni kwa kila wakala, tahadhari inayowaka mbio inapozizidi, na ugunduzi wa mzunguko unaoshindwa kwa usalama badala ya kukorogana. Pima bajeti finyu, zinazoweza kukata kazi ngumu halali, dhidi ya zile zilizolegea zinazoruhusu gharama kukimbia. Katika mazingira ya mashirika makubwa na serikali ambapo matumizi lazima yatabiriwe na kuhalalishwa, wakala ambaye gharama yake haina mipaka ni mstari wa gharama usioweza kuutetea kwenye mapitio ya bajeti wala ukaguzi.

## Mtazamo wa sekta

**Kampuni changa.** Safirisha wakala mmoja finyu anayegusa thamani yako ya msingi, kwenye mfano unaopangishwa, mwenye seti ndogo zaidi ya zana inayofanya kazi na kikomo kigumu cha hatua na matumizi. Pinga onyesho la mawakala wengi: umakini wako adimu wa kihandisi unatumika vizuri zaidi kubana uhuru wa wakala mmoja na kufuatilia mbio zake kuliko kuratibu majukumu usiloweza kuyadumisha. Weka kila kitendo chenye athari nyuma ya lango moja la "andaa, usitume kamwe" ili kosa ligharimu mbofyo wa kutendua, si tukio.

**Biashara ndogo.** Huna wa kuendesha zana ya tathmini wala sandbox, kwa hiyo pendelea mawakala waliopachikwa kwenye zana unazoziamini tayari, na uwashe tu uhuru unaoweza kuusimamia kwa macho. Chukulia wakala yeyote anayeweza kutuma, kulipa, au kufuta kwa niaba yako kama kitu cha kuweka mbali hadi mtu athibitishe kila kitendo, kwa sababu ujumbe wa kiotomatiki usio sahihi kwa mteja unakugharimu uhusiano. Pendelea wauzaji wanaokuonyesha wakala alifanya nini na wanakuruhusu kuzima uotomatishaji.

**Biashara kubwa.** Tatizo ni kutawala mawakala kuvuka timu nyingi: mifumo ya pamoja ya kubana uhuru, vitambulisho vya zana vya upendeleo mdogo, sandbox, malango ya binadamu-kwenye-mzunguko, na ufuatiliaji wa mwanzo hadi mwisho ili hakuna kikundi kinachobuni upya vizuizi. Unganisha mawakala na mifumo ya ndani chini ya vidhibiti vya ufikiaji ambavyo binadamu angeshikilia, weka lango la vitendo visivyorekebishika nyuma ya waidhinishaji waliotajwa na usimamizi wa mabadiliko, na simamia jalada kwa vipimo vya kiwango cha mafanikio, bajeti za kila mbio, na majaribio ya uadui ya sindano. Sawazisha tabaka la ufuatiliaji na tathmini ili tabia ya wakala yeyote ijengwe upya na kukaguliwa.

**Serikali.** Ununuzi, uwazi, na uwajibikaji wa umma hubana kila uchaguzi. Weka mawakala kwenye kukusanya ukweli na kuandaa rasimu, na uhifadhi kila uamuzi unaomwathiri raia kwa binadamu anayewajibika, kwa sababu wajibu wa uamuzi wa sekta ya umma hauwezi kukabidhiwa kwa mfano. Andika kila mbio ili chombo cha usimamizi kione vyanzo vipi vilitazamwa na nini kilifanywa, dai wauzaji wafichue zana na mipaka ya wakala, na uthibitishe kupitia seti ya tathmini ya uadui kwamba wakala anakataa kutenda zaidi ya wigo wake uliobanwa.

## Mifano

**Kampuni changa.** Kampuni changa ya uchanganuzi ya watu watano inajenga wakala wa kupanga msaada. Anasoma tiketi inayoingia, anatafuta nyaraka, na ama anaandaa jibu au kuelekeza tiketi kwa binadamu, na hiyo ndiyo seti nzima ya zana. Vitambulisho ni vya kusoma tu pamoja na kitendo kimoja cha "unda rasimu" ambacho hakitumi kamwe bila mtu kubofya tuma. Kila mbio inafuatiliwa ili waanzilishi waone kwa nini tiketi iliwekwa mahali ilipowekwa, na seti ya tathmini ya kila usiku ya tiketi halisi hamsini inaendesha wakala mara tano kila moja kufuatilia kiwango cha usahihi wa kuelekeza. Onyesho la ujanja la mawakala wengi la mshindani linapowashawishi, wanabaki na wakala mmoja kwa sababu kazi yao haigawanyiki.

**Biashara kubwa.** Benki inajenga wakala wa kuwasaidia wafanyakazi wa operesheni kupatanisha malipo yaliyoshindwa. Inaunganishwa na mifumo ya ndani chini ya vidhibiti vya ufikiaji ambavyo karani wa binadamu anavyo, kupitia vitambulisho vya huduma vya upendeleo mdogo vilivyowekewa wigo wa upatanisho tu. Wakala anaweza kuchunguza kwa uhuru (kusoma leja, kutafuta historia ya miamala) lakini kitendo chochote kinachohamisha fedha au kuhariri rekodi kinawekwa hatua na kinahitaji mwidhinishaji wa binadamu aliyetajwa, kutimiza usimamizi wa mabadiliko. Nyaraka zilizomezwa zinachukuliwa kama zisizoaminika kupunguza sindano ya maagizo, zana zinaendeshwa kwenye sandbox, na kila mbio inafuatiliwa mwanzo hadi mwisho kwa ukaguzi. Seti ya tathmini ya nje ya mtandao inaweka lango la kila badiliko la mfano au agizo, na bajeti za kila mbio zinabana hatua na matumizi ili wakala anayezunguka asiweze kupandisha gharama au ucheleweshaji.

**Serikali.** Wakala wa manufaa unafanya majaribio ya wakala wa kuwasaidia wahudumu wa kesi kukusanya ukweli wa dai: kuvuta rekodi, kukagua kanuni za ustahiki, na kuandaa muhtasari. Wakala unachora mstari mgumu: wakala anakusanya na kuandaa rasimu, lakini mhudumu wa kesi wa binadamu anafanya na kumiliki kila uamuzi unaomwathiri raia, kwa sababu uwajibikaji wa maamuzi ya sekta ya umma hauwezi kukabidhiwa kwa mfano (sura ya 6.5). Kila mbio inaandikwa kikamilifu, ikionyesha vyanzo vipi vilitazamwa na nini kiliandaliwa, ili chombo cha usimamizi kikague kesi yoyote. Uhuru umebanwa kwa makusudi kwenye soma-na-andaa, zana ni za upendeleo mdogo na zimewekwa kwenye sandbox, na seti ya tathmini ya uadui inathibitisha wakala anakataa kutenda zaidi ya kukusanya ukweli.

## Kesi ya biashara: sababu, ROI, na TCO

Mawakala hutoa faida kwa kuotomatisha kazi ya hatua nyingi ambayo zamani ilihitaji mtu kubofya kati ya mifumo: kupanga, kupatanisha, utafiti, na operesheni za kawaida. Thamani inaonekana kama kazi iliyokamilika bila binadamu kwenye kila hatua, mizunguko ya haraka, na wafanyakazi walioachiwa kazi nzito za busara. Kwa kuwa mawakala hujengwa juu ya LLM na zana zilizopo, muda hadi mfano wa kufanya kazi ni mfupi, na ndiyo sababu hasa timu zinajenga kupita kiasi.

Jumla ya gharama ya umiliki ndipo mawakala hutofautiana na vipengele vya kawaida vya LLM. Juu ya gharama ya uelekezaji unalipia miunganisho ya zana, mabomba ya sandbox na ruhusa, zana ya tathmini, mrundiko wa ufuatiliaji na uonekanaji (sura ya 6.6), na wapitiaji wa binadamu wanaoajiri malango ya idhini. Wakala anayezunguka au aliyebanwa vibaya anaongeza gharama ya kubadilika inayoweza kuruka bila onyo, kwa hiyo bajeti za hatua na matumizi ni sehemu ya usanifu, si wazo la baadaye. Gharama ya kutopokea ni operesheni za polepole na kazi ya mkono ambayo washindani wenu wanaiotomatisha. Gharama ya kupokea bila uangalifu ni kitendo cha kujiendesha kinachotuma ujumbe usio sahihi, kuvujisha data, au kufanya uamuzi usio na uwajibikaji. Weka kesi kwa uongozi kwa kuoanisha lengo moja madhubuti la uotomatishaji na mpango madhubuti wa vizuizi, tathmini, na usimamizi wa binadamu, na kwa kuwa waaminifu kwamba vizuizi ndio sehemu kubwa ya gharama.

## Mifumo mibaya na mitego

- **Wakala wakati mtiririko ungetosha.** Kuchukua hatari kamili ya uhuru kwa kazi ambayo hatua zake zilijulikana.
- **Zana na vitambulisho pana kupita kiasi.** Zana moja ya "fanya lolote" badala ya nyembamba, za upendeleo mdogo.
- **Upofu wa sindano ya maagizo.** Kulisha maudhui yasiyoaminika kwa wakala mwenye upendeleo halisi.
- **Hakuna lango la binadamu kwa vitendo visivyorekebishika.** Kumruhusu mfano atume, alipe, au afute bila ukaguzi.
- **Maigizo ya mawakala wengi.** Kugawanya kazi rahisi kuvuka mawakala, kulipia gharama ya uratibu bila faida.
- **Tathmini ya hisia.** Kuhukumu kwa jinsi nakala inavyosomeka badala ya kiwango cha mafanikio ya kazi.
- **Mizunguko isiyo na mipaka.** Hakuna kikomo cha hatua, muda, au matumizi, kwa hiyo wakala aliyekwama anachoma fedha na ucheleweshaji.
- **Mbio zisizofuatiliwa.** Hakuna rekodi ya wakala alichofanya, ikikuacha huwezi kutatua, kukagua, wala kuwajibika.

## Kielelezo cha ukomavu

- **Ngazi ya 1, Kuanzisha:** Mawakala wanaundwa mifano ya awali papo hapo wakiwa na ufikiaji mpana wa zana na bila mipaka. Mafanikio yanahukumiwa kwa maonyesho, kwa kuitikia, kitu kinapoharibika. Hakuna seti ya tathmini, hakuna ufuatiliaji, na hakuna lango la binadamu kwa vitendo vyenye athari.
- **Ngazi ya 2, Kuendeleza:** Baadhi ya mawakala wana mizunguko yenye mipaka na zana za upendeleo mdogo, na ufuatiliaji wa msingi upo, lakini mazoea yanatofautiana kwa timu. Seti ya tathmini ya mkono inanasa regression kubwa katika miradi michache huku mingine haina. Idhini ya binadamu inalinda vitendo dhahiri zaidi visivyorekebishika, hata hivyo ufikiaji hauna usawa na haujaandikwa.
- **Ngazi ya 3, Kusawazisha:** Mifumo ya pamoja inatawala uhuru, ruhusa za zana, sandbox, na malango ya binadamu-kwenye-mzunguko, iliyoandikwa na kutekelezwa kuvuka kila timu. Kila kitendo chenye athari kimewekewa lango au kuthibitishwa, mawakala wanafuatiliwa mwanzo hadi mwisho, na seti ya tathmini ya kiotomatiki yenye alama za kiwango cha mafanikio inaendeshwa kwa kila badiliko. Sindano ya maagizo inachukuliwa kama tishio la kudumu lenye jibu lililofafanuliwa.
- **Ngazi ya 4, Kusimamia:** Jalada la mawakala linapimwa na kudhibitiwa dhidi ya vipimo vya msingi. Kiwango cha mafanikio kwa kila kazi, kiwango cha kupita cha ulinzi wa sindano ya maagizo, gharama na idadi ya hatua kwa kila mbio, ucheleweshaji wa idhini ya binadamu, na matukio ya mzunguko au kushindwa vinafuatiliwa kama vipimo; vizingiti vya kurudisha nyuma na kuua vinatekelezwa kwa ushahidi huo badala ya malalamiko. Bajeti za kila mbio za hatua, muda, na matumizi zinafuatiliwa, na regression katika kipimo chochote huchochea hatua kabla ya ukubwa, si baada ya tukio.
- **Ngazi ya 5, Kuratibu:** Uhuru unalinganishwa na hatari ya kazi kwa sera na kurekebishwa mfululizo matokeo yanapoingia. Tathmini endelevu ya nje na ya mtandaoni inafunga tabia ya wakala na matokeo ya biashara, na shirika mara kwa mara linastaafisha, kupanua upya, au kupa upya ruhusa mawakala picha ya hatari inapohama. Ufuatiliaji, bajeti za gharama, na nyayo za ukaguzi ni sare kuvuka jalada; ulinzi wa sindano na naibu aliyechanganyikiwa unajaribiwa kwa uadui; uwajibikaji wa vitendo vya kujiendesha ni wazi na unakaguliwa.

## Mawazo ya kujadili

1. Vipengele vyenu vipi vya LLM vya sasa vimekuwa mawakala kimyakimya, na uhuru wa kila moja umebanwa kwa makusudi?
2. Kwa kila zana ya wakala, njia ya bei nafuu zaidi ya mshambulizi kuitumia vibaya kupitia maudhui yaliyoingizwa ni ipi, na nini kinazuia hilo?
3. Mmechagua miundo ya mawakala wengi wapi, na mnaweza kuonyesha gharama ya uratibu ililipa dhidi ya wakala mmoja?
4. Vitendo vipi vya wakala haviwezi kurekebishwa kweli, na je, kila kimoja kingeweza kubuniwa upya kuwa kinachorekebishika au cha hatua?
5. Wakala akichukua kitendo cha madhara kesho, mngeweza kujenga upya hasa alichofanya na nani alikuwa anawajibika?

## Mambo muhimu ya kukumbuka

- Wakala ni LLM kwenye mzunguko pamoja na zana, kumbukumbu, na lengo. Hatari inaishi kwenye mzunguko na zana, si maandishi.
- Pendelea mtiririko uliowekwa hatua zinapojulikana; hifadhi uhuru kwa malengo ya wazi kweli na uubane kwa ukali.
- Matumizi ya zana ndio uwezo wa msingi. Ipe kila zana upendeleo mdogo, skima iliyothibitishwa, na sandbox.
- Weka lango la vitendo vyenye athari na visivyorekebishika nyuma ya binadamu mwenye mamlaka halisi, na usanifu kwa kutendua kwa bei nafuu.
- Chukulia mawakala kama wa uadui: jilinde dhidi ya sindano ya maagizo na matumizi mabaya ya naibu aliyechanganyikiwa (sura ya 4.2).
- Tathmini kwa kiwango cha mafanikio ya kazi kuvuka mbio nyingi, na ufuatilie kila mbio kwa kutatua, kudhibiti gharama, na kukagua (sura ya 6.5 na 6.6).
- Mara nyingi jibu sahihi ni kutojenga wakala kabisa.

## Marejeo na usomaji zaidi

- Shunyu Yao et al., *ReAct: Synergizing Reasoning and Acting in Language Models*.
- Timo Schick et al., *Toolformer: Language Models Can Teach Themselves to Use Tools*.
- Anthropic, *Building Effective Agents* (engineering guidance on workflows versus agents).
- OWASP Foundation, *OWASP Top 10 for Large Language Model Applications* (including prompt injection and excessive agency).
- Simon Willison, writing on prompt injection and the "lethal trifecta" for AI agents.
- Norman Hardy, *The Confused Deputy* (the classic statement of the confused-deputy problem).
- Chip Huyen, *AI Engineering: Building Applications with Foundation Models*.
- Stuart Russell and Peter Norvig, *Artificial Intelligence: A Modern Approach* (intelligent agents and rational action).
