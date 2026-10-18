# 4.10 Majaribio ya kupenya na red teaming

## Muhtasari na msukumo

Unaweza kujenga kila kidhibiti ambacho kielelezo chako cha vitisho kinadai na bado usijue kama vinafanya kazi. Nyaraka zinasema ngome inazuia mlango huo, mapitio ya msimbo yanasema ingizo linathibitishwa, sera inasema upendeleo mdogo unatekelezwa. Usalama wa kushambulia ndio njia ya kujua kama lolote kati ya hayo ni kweli mshambulizi mwenye nia anapoyasukuma. Sura hii inahusu kushambulia kwa makusudi mifumo yako mwenyewe, kwa idhini, ili kupata udhaifu kabla mpinzani halisi hajaupata.

Nidhamu hii inaendeshwa kwenye wigo. Upande mwepesi kuna [uchanganuzi wa udhaifu](https://en.wikipedia.org/wiki/Vulnerability_scanner): zana za kiotomatiki zinazochunguza dosari zinazojulikana na usanidi mbaya. Katikati kuna [majaribio ya kupenya](https://en.wikipedia.org/wiki/Penetration_test): binadamu mwenye ujuzi anayeunganisha udhaifu kuthibitisha uwezekano wa kunyonywa dhidi ya shabaha iliyofafanuliwa. Upande wa mbali kuna [red teaming](https://en.wikipedia.org/wiki/Red_team): kampeni inayoendeshwa na lengo inayoiga mpinzani halisi kuvuka watu, mchakato, na teknolojia, na inayojaribu uwezo wako wa kugundua na kujibu, si uwezo wako wa kuzuia tu. Kila moja hujibu swali tofauti, na kuvichanganya ndiyo njia ya kawaida zaidi ambayo mashirika hupoteza fedha na kujifariji kwa uhakikisho wa uongo.

Sura hii imesimama kwa makusudi kando ya jirani zake. Sura ya 4.4 inashughulikia operesheni za usalama: upande wa ulinzi, wa ufuatiliaji unaotazama vitisho na kuvijibu. Sura hii ni mwenzake wa kushambulia anayejaribu kama ulinzi huo unafanya kazi kweli. Sura ya 4.9 inashughulikia mzunguko salama wa uendelezaji wa programu, ambapo usalama unajengwa ndani ya jinsi msimbo unavyobuniwa na kusafirishwa; majaribio ya kushambulia huthibitisha zao la mzunguko huo kutoka nje. Pia inajengwa juu ya misingi na utamaduni wa sura ya 4.1 na mazoea ya usalama wa programu ya sura ya 4.2.

Kwa mashirika makubwa, majaribio ya kushambulia ni zana ya kupunguza hatari na wajibu wa kisheria. Wasindikaji wa malipo, benki, na watoa huduma za afya wanakabiliwa na mahitaji wazi ya kupima. Kwa serikali, dau linafikia usalama wa taifa na uaminifu wa umma: wapinzani hapa ni dola zenye rasilimali nyingi, na mifumo wanayolenga inaendesha uchaguzi, manufaa, na miundombinu muhimu. Katika mazingira yote mawili, thamani haitokani na ripoti bali na unachorekebisha na jinsi unavyojifunza kwa kasi zaidi kugundua uvamizi unaofuata.

## Kanuni kuu

- Linganisha ushiriki na swali: uchanganuzi, majaribio ya kupenya, na red teaming hujibu mambo tofauti.
- Pata idhini iliyoandikwa na kanuni wazi za ushiriki kabla ya mtu yeyote kugusa mfumo.
- Matokeo hayana thamani hadi yarekebishwe na kujaribiwa tena; yafuatilie kama kazi nyingine yoyote.
- Red team ipo kuifanya timu ya buluu iwe bora, si kushinda.
- Iga wapinzani halisi na mbinu zao, si orodha hakiki za jumla.
- Pima ugunduzi na jibu, si idadi ya udhaifu uliopatikana tu.
- Jihadhari na maigizo: ushiriki uliowekewa wigo ili kupita unaonekana wa kuvutia na hauthibitishi chochote.

## Mapendekezo

### Elewa wigo wa usalama wa kushambulia

Anza kwa kutaja unachonunua. Uchanganuzi wa udhaifu ni mpana, wa kiotomatiki, na wa bei nafuu; uendeshe mfululizo dhidi ya eneo lako kunasa [Common Vulnerabilities and Exposures](https://en.wikipedia.org/wiki/Common_Vulnerabilities_and_Exposures) (CVE) zinazojulikana na usanidi mbaya. Huzalisha wingi na matokeo ya uongo, na hauwezi kukuambia kama dosari inanyonyeka kweli katika muktadha. Majaribio ya kupenya humweka mjaribu mwenye ujuzi dhidi ya shabaha iliyofafanuliwa kwa dirisha lililowekwa, akiunganisha udhaifu kuonyesha athari halisi: matokeo haya ya kichanganuzi, yakichanganywa na ruhusa dhaifu ile, yanazaa msimamizi wa kikoa. Hujibu "je, kitu hiki mahususi kinaweza kuvunjwa, na kwa kiasi gani."

Red teaming hujibu swali kubwa zaidi: "mpinzani aliyedhamiria akitulenga, je, tungegundua, na tungeweza kumzuia." Inaendeshwa na lengo (toa seti hii ya data, fikia mfumo huu wa udhibiti), inafunika uso mzima wa shambulio ikijumuisha watu na ufikiaji wa kimwili, na kwa kawaida huendeshwa bila kuwaonya watetezi. [Purple teaming](https://en.wikipedia.org/wiki/Red_team#Purple_team) huporomosha ukuta: nyekundu na buluu hufanya kazi pamoja katika chumba kimoja, mshambulizi anaendesha mbinu na mtetezi anatazama kama zana zake zinaikamata, akirekebisha ugunduzi kwa wakati halisi. Purple teaming mara nyingi hutoa uboreshaji wa ulinzi zaidi kwa kila dola kuliko red team ya siri, kwa sababu kila kitendo kinakuwa wakati wa kufundisha.

### Chagua sanduku jeusi, la kijivu, au jeupe kwa makusudi

Kiasi unachomwambia mjaribu kinaumba unachojifunza. Majaribio ya sanduku jeusi humpa hakuna ila shabaha, yakiiga mshambulizi wa nje asiye na ujuzi wa ndani; ni ya kweli lakini ya polepole, na wajaribu wanaweza kutumia bajeti nzima kwenye upelelezi ambao mpinzani halisi angeutumia miezi. Majaribio ya sanduku jeupe hukabidhi msimbo wa chanzo, michoro ya usanifu, na vitambulisho, yakimruhusu mjaribu kwenda kina na kufunika eneo zaidi katika muda unaopatikana. Sanduku la kijivu liko katikati: ujuzi fulani, vitambulisho fulani, likiiga mshambulizi aliyefanya kazi ya nyumbani au mtu wa ndani mwenye nia mbaya.

Kwa majaribio mengi ya programu, sanduku la kijivu au jeupe hutoa faida bora, kwa sababu unalipia kina cha uchambuzi, si mjaribu agundue upya mpangilio wa subnet yako. Hifadhi sanduku jeusi kwa wakati uhalisia wa awamu ya ugunduzi wenyewe ndio unaotaka kujaribu, kama kupima outsider anaweza kujifunza kiasi gani kutoka alama yako ya umma. Kuwa wazi unaagiza lipi, kwa kuwa ripoti ya sanduku jeusi inayopata kidogo inaweza kumaanisha uko salama au inaweza kumaanisha mjaribu aliishiwa muda kwenye mzunguko.

### Weka wigo kwa uangalifu na uandike kanuni za ushiriki

Wigo ndipo ushiriki hufanikiwa au kushindwa. Waraka wa [kanuni za ushiriki](https://en.wikipedia.org/wiki/Rules_of_engagement) hufafanua kilicho ndani ya mipaka na kisicho, mbinu zipi zinaruhusiwa, dirisha la majaribio, mifumo na mitandao inayofunikwa, mahitaji ya ushughulikiaji wa data, na mawasiliano ya dharura pande zote mbili. Unataja mifumo ya uzalishaji isiyoruhusiwa au inayohitaji uangalifu, unaweka kanuni ya kusimama mjaribu akipata kitu hatari kwa sasa, na unafafanua nini kitatokea wakipita kwa bahati kwenye shughuli halisi ya mshambulizi au data nyeti kweli.

Andika njia za kupandisha na barua ya "kutoka gerezani": idhini ambayo mjaribu anaweza kuitoa wafanyakazi wa usalama au vyombo vya sheria wakimhoji katikati ya ushiriki. Kubaliana mapema jinsi matokeo yanavyohifadhiwa na kusafirishwa, kwa kuwa ripoti ya jaribio la kupenya ni ramani ya jinsi ya kukuvunja na lazima ilindwe ipasavyo. Wigo mwembamba huzalisha matokeo ya kina kwenye uso mdogo; wigo mpana huzalisha ufikiaji wa juujuu wa uso mkubwa. Chagua kwa makusudi, na usiruhusu wigo upanuke kimyakimya katikati ya ushiriki bila idhini upya.

### Chukulia idhini kama mstari kati ya majaribio na uhalifu

Kitendo kimoja kinachomtenganisha mjaribu wa kupenya na mhalifu ni idhini. Kufikia mifumo ambayo huna idhini ya kuifikia ni uhalifu chini ya sheria kama [Computer Fraud and Abuse Act](https://en.wikipedia.org/wiki/Computer_Fraud_and_Abuse_Act) nchini Marekani na sawa nazo kwingine, na nia njema si utetezi. Idhini lazima ije kwa maandishi kutoka kwa mtu mwenye mamlaka halisi ya kuitoa, ifunike hasa mifumo na mbinu zilizo katika wigo, na isainiwe kabla kazi haijaanza.

Mifumo ya watu wa tatu inachanganya hili. Mtoa huduma wako wa wingu, wauzaji wako wa programu-kama-huduma, na miundombinu yoyote inayoshirikiwa inaweza kuwa na sera zake za majaribio, na huwezi kuidhinisha shambulio dhidi ya mali usizomiliki. Angalia kanuni za mtoa huduma, omba ruhusa pale inapohitajika, na ubaki ndani ya upangaji wako mwenyewe. Uhandisi wa kijamii unaolenga wafanyakazi huibua maswali ya kimaadili na kisheria kuhusu ridhaa na madhara ya kisaikolojia ambayo lazima uyafikirie mapema. Ukiwa na shaka, shirikisha wakili; gharama ya mazungumzo ni ndogo ikilinganishwa na gharama ya tukio la ufikiaji usioidhinishwa.

### Pima timu za ndani dhidi ya wajaribu wa watu wa tatu

Red team ya ndani inajua mazingira yako, hujenga mahusiano na watetezi, na inaweza kujaribu mfululizo badala ya milipuko ya kila mwaka. Ujuzi huo huo pia ni kikomo: wanashiriki upofu wenu na dhana za kishirika, na uhuru wao unaweza kuhojiwa wanaporipoti kwa uongozi uleule wa mifumo wanayojaribu. Kampuni za watu wa tatu huleta macho mapya, ujuzi maalumu, na uhuru ambao wakaguzi na wadhibiti mara nyingi hudai, lakini huanza polepole, hugharimu zaidi kwa kila ushiriki, na huondoka ripoti inapokabidhiwa.

Programu nyingi zilizokomaa hutumia zote mbili. Timu za ndani hushughulikia uigaji wa mpinzani endelevu, kurekebisha ugunduzi, na ujuzi wa kina wa mazingira unaofanya purple teaming kuwa na tija. Kampuni za nje hutoa uthibitisho huru wa mara kwa mara, hutimiza mahitaji ya uhuru ya viwango kama PCI DSS, na huchunguza maeneo ambayo watu wenu wameacha kuyaona. Utumie yupi, hakikisha wajaribu wana sifa: vyeti kama OSCP (Offensive Security Certified Professional) na uzoefu ulioonyeshwa vinajalisha zaidi ya wasilisho la mauzo lililong'arishwa.

### Endesha zawadi za hitilafu na ufichuzi ulioratibiwa

Programu ya [zawadi kwa hitilafu](https://en.wikipedia.org/wiki/Bug_bounty_program) huwaalika watafiti wa nje kupata na kuripoti udhaifu kwa kubadilishana na utambuzi na malipo. Inakupa majaribio endelevu, ya umati kuvuka ujuzi mbalimbali ambao usingeweza kuwaajiri wote mara moja, na unalipia matokeo halisi tu. Si mbadala wa majaribio ya kupenya yaliyopangwa, kwa kuwa watafiti hufuata kinacholipa na wanaweza kupuuza madaraja mazima, lakini ni nyongeza yenye nguvu inayofichua mashambulizi ya kibunifu.

Kabla hujaendesha zawadi inayolipwa, unahitaji sera ya [ufichuzi ulioratibiwa wa udhaifu](https://en.wikipedia.org/wiki/Coordinated_vulnerability_disclosure): njia iliyochapishwa, rahisi kupata kwa yeyote kuripoti tatizo la usalama kwa usalama, ahadi ya kutowashtaki kisheria watafiti wenye nia njema, ratiba za jibu zilizofafanuliwa, na mchakato wa ndani wa kupanga na kurekebisha kinachoingia. Faili ya security.txt na anwani wazi ya kuripoti ni kiwango cha chini. Mawakala wa serikali wanazidi kuamuru sera za ufichuzi wa udhaifu kwa mifumo inayomkabili umma, na kutokuwa na njia hakuwazuii watafiti kupata hitilafu; kunawazuia tu kukuambia kwa usalama.

### Tumia dhana-ya-uvunjaji na uigaji wa mpinzani

Majaribio ya mzunguko tu yanadhani mshambulizi anaanzia nje, lakini uvunjaji halisi mara nyingi huanza na kitambulisho kilichohadaiwa au kompyuta ndogo iliyoathirika tayari ndani. Zoezi la [dhana-ya-uvunjaji](https://en.wikipedia.org/wiki/Breach_and_attack_simulation) humwanzisha mjaribu na nafasi ya kuanzia, kama ufikiaji kama mfanyakazi wa kawaida, na kuuliza anaweza kwenda umbali gani kutoka hapo. Hii hujaribu moja kwa moja kugawanya kwa ndani, ugunduzi, na vidhibiti vya eneo la mlipuko, badala ya kuweka kila kitu kwenye mzunguko ambao hatimaye utavukwa. Kwa kawaida ni matumizi bora ya muda wa red team kuliko kuwatazama wakisaga dhidi ya ukingo ulioimarishwa.

Weka kampeni kwenye tabia halisi ya mpinzani kwa kutumia [MITRE ATT&CK](https://en.wikipedia.org/wiki/MITRE_ATT%26CK), hifadhi ya maarifa ya umma ya mbinu na taktiki ambazo washambulizi hutumia kweli, iliyopangwa kutoka ufikiaji wa awali hadi kutoa data. Uigaji wa mpinzani huchagua mhusika wa tishio anayejulikana kulenga sekta yako, huzalisha upya mbinu zake zilizoandikwa, na hujaribu kama unagundua na kuzuia kila hatua. Hii ni ya manufaa zaidi sana kuliko shambulio la jumla, kwa sababu inaoanisha ulinzi wako na wapinzani mahususi unaokabiliana nao na kuzalisha matokeo ambayo upelelezi wako wa vitisho unaweza kuyawekea kipaumbele.

### Lisha matokeo kwa timu ya buluu na uhandisi wa ugunduzi

Madhumuni ya kushambulia ni ulinzi bora. Kila kitendo cha red team ni nafasi ya kuuliza: je, zana zetu zilizalisha ishara, je, mtu yeyote aliiona, na je, walijibu ipasavyo. Endesha ushiriki ili kila mbinu ioane na ugunduzi ulio nao, unaohitaji kujenga, au unaohitaji kurekebisha. Huu ni uhandisi wa ugunduzi: kugeuza tabia ya mshambulizi kuwa tahadhari za kutegemewa, na ndipo thamani ya red team inapojilimbikiza. Matokeo kwamba "hatukugunduliwa wakati wa kusonga kando" yanapaswa kuwa kanuni mpya ya ugunduzi, inayojaribiwa kwa kuendesha upya mbinu.

Mazoezi ya mezani hupanua hili hadi kufanya maamuzi. Kusanya watu watakaojibu tukio halisi na mpitie hali halisi kwenye karatasi: nani anatangaza tukio, nani anazungumza na wanasheria, nani anaamua kuondoa mfumo mtandaoni. Mazoezi ya mezani ni nafuu, hufichua mapengo katika majukumu na mawasiliano ambayo majaribio ya kiufundi hukosa, na huandaa binadamu wanaojalisha zaidi usimamizi wa matukio wa sura ya 9.3 unapoanza kazi. Oanisha red teaming ya kiufundi na mazoezi ya mezani ya mara kwa mara ili zana zenu na watu wenu wote wafanyiwe mazoezi.

### Fuatilia urekebishaji na ujaribu tena

Ripoti ya udhaifu ambayo hakuna anayeitendea kazi ni dhima, kwa kuwa sasa mnajua mnaendesha dosari ambayo mkaguzi anaweza kuitaja. Lisha kila matokeo kwenye mfumo wenu wa kawaida wa kufuatilia kazi ukiwa na mmiliki, ukali, na tarehe ya mwisho iliyofungwa kwa hatari. Matokeo muhimu hupata matibabu ya dharura; ya chini hujiunga na backlog yenye kipaumbele cha uaminifu. Kipimo kinachojalisha ni muda wa kurekebisha, si muda wa kuripoti.

Kujaribu tena hufunga mzunguko. Baada ya suluhisho kusafirishwa, mjaribu (au ukaguzi wa kiotomatiki) huthibitisha udhaifu umeondoka kweli na kwamba suluhisho halikufungua tundu jipya. Bila kujaribu tena, "imerekebishwa" ni tumaini, si ukweli, na matokeo mengi hurudi kwa sababu suluhisho halikukamilika au regression ilizirudisha. Viwango kama PCI DSS vinahitaji mzunguko huu waziwazi. Jenga kujaribu tena ndani ya mkataba wa ushiriki ili lisiwe wazo la baadaye lililosahaulika.

## Mabadilishano: faida na hasara

| Mbinu | Bora kwa | Faida | Hasara |
|---|---|---|---|
| Uchanganuzi wa udhaifu | Ufikiaji endelevu wa dosari zinazojulikana | Nafuu, mpana, wa kiotomatiki, wa mara kwa mara | Una kelele; hauwezi kuthibitisha uwezekano wa kunyonywa |
| Majaribio ya kupenya | Kuthibitisha athari kwenye shabaha iliyofafanuliwa | Ufahamu wa kina, wa binadamu; minyororo halisi ya unyonyaji | Nukta moja ya wakati; wigo mwembamba; ghali |
| Red teaming | Kujaribu ugunduzi na jibu | Ya kweli; hujaribu watu na mchakato | Ghali; polepole; inahitaji timu ya buluu iliyokomaa |
| Purple teaming | Kuboresha ugunduzi haraka | Kujifunza kwingi kwa kila dola; ya ushirikiano | Si ya kweli kiasi; inahitaji timu zote mbili zipatikane |
| Zawadi kwa hitilafu | Ugunduzi endelevu wa umati | Lipa kwa kila matokeo; ujuzi mbalimbali | Ufikiaji usio sawa; mzigo wa kupanga; inahitaji mchakato |

Mvutano wa msingi ni kati ya uhalisia na kasi ya kujifunza. Red team ya siri ni jaribio la kweli zaidi unaloweza kuendesha, lakini masomo yake yanafika polepole na baada ya kampeni nzima tu, na timu ya buluu isiyokomaa hujifunza kidogo kwa kushindwa kimyakimya. Purple teaming hutoa muhanga mshangao ili kuongeza kasi ya watetezi kuboreka. Mvutano wa pili ni upana dhidi ya kina: uchanganuzi hufunika kila kitu kijuujuu, wakati jaribio la kupenya hufunika kipande kidogo kwa kina. Programu zilizokomaa huweka tabaka badala ya kuchagua moja, zikiendesha uchanganuzi endelevu chini ya majaribio ya kina ya mara kwa mara na kampeni za red team za wigo kamili za mara moja moja. Hatua mbaya ni kununua jaribio moja la kupenya la kila mwaka, kuweka ripoti kwenye faili, na kuita tatizo limetatuliwa.

## Maswali ya kujadili na timu yako

1. **Tunapoagiza majaribio ya kushambulia, tuko wazi ni swali gani tunauliza kweli, na je, ushiriki unalingana nalo?** Mashirika mengi hununua "jaribio la kupenya" na kupokea uchanganuzi wa udhaifu wenye muhtasari ulioandikwa na binadamu, kisha huamini wamejaribu ulinzi wao wakati wamekagua dosari zinazojulikana tu. Wengine huagiza red team wakati uwezo wao wa ugunduzi ni changa kiasi kwamba zoezi linathibitisha tu kile kila mtu alijua tayari. Leta wigo wenu wa ushiriki watatu wa mwisho na ripoti zilizotokana, na uliza kama kila moja ilijibu swali mlilohitaji kujibiwa: ufikiaji wa udhaifu unaojulikana, uwezekano wa kunyonywa wa shabaha mahususi, au uwezo wa kugundua na kujibu uvamizi. Jibu linapaswa kuunda mchanganyiko wa makusudi wa uchanganuzi, majaribio ya kupenya, na red au purple teaming unaolingana na ukomavu wenu.

2. **Nini kinatokea kwa matokeo baada ya ripoti kutua, na tungethibitishaje yalirekebishwa?** Thamani ya usalama wa kushambulia iko kabisa katika urekebishaji, hata hivyo programu nyingi hupima mafanikio kwa ukubwa wa ripoti badala ya kupungua kwa hatari. Fuatilia matokeo halisi kutoka ushiriki wenu wa mwisho: nani aliyamiliki, jinsi yalivyopewa kipaumbele dhidi ya kazi ya vipengele, lini yalirekebishwa, na kama yeyote alithibitisha suluhisho lilifanya kazi kweli. Kama huwezi kutoa njia hiyo, majaribio yenu yanazalisha maarifa ambayo hamyatendei kazi, ambayo ni mabaya kuliko kutojua, kwa sababu sasa mmefichuka kwa kujua. Matokeo ya mjadala huu yanapaswa kuwa mtiririko wa kazi unaofuatiliwa wa urekebishaji wenye wamiliki, tarehe za mwisho za hatari, na kujaribu tena kwa lazima kumejengwa ndani ya kila mkataba.

3. **Red team yetu inaifanya timu ya buluu kuwa bora, au inahifadhi alama tu?** Red team inayosherehekea ushindi usiogunduliwa na kuhodhi mbinu zake inafurahisha na haina maana. Uhusiano unapaswa kuwa wa ushirikiano chini ya uso wa uadui: kila mbinu isiyogunduliwa inapaswa kuwa kanuni mpya ya ugunduzi, kila njia iliyofanikiwa inapaswa kufahamisha kugawanya, na timu hizi mbili zinapaswa kuchambua pamoja. Waulize watetezi wenu walijifunza nini kutoka ushiriki wa mwisho wa red team na kama ugunduzi au kidhibiti chochote madhubuti kilibadilika kwa sababu hiyo. Jibu la uaminifu likiwa hakuna, mnalipia maigizo, na mnapaswa kuhamia purple teaming na uigaji wa mpinzani uliofungwa waziwazi kwa uhandisi wa ugunduzi.

4. **Kabla ya ushiriki wetu ujao, tuna idhini iliyoandikwa kwa kila mali iliyo katika wigo, ikijumuisha zile ambazo hatuzimiliki?** Idhini ndio mstari kati ya jaribio la kupenya na tukio la uhalifu wa kompyuta, na katika shirika kubwa mifumo ambayo mjaribu atagusa mara chache hukaa ndani ya mpaka mmoja wa umiliki: inavuka upangaji wa wingu, majukwaa ya programu-kama-huduma, mitandao inayosimamiwa, na miundombinu inayoshirikiwa ambayo mshirika au muuzaji anaidhibiti. Shinikizo linaloshindana ni kasi, kwa sababu kufukuzia ruhusa iliyosainiwa na sera za majaribio za mtoa huduma ni polepole na ya kushawishi kuruka tarehe ya mwisho inapokaribia. Leta rasimu ya kanuni za ushiriki, orodha ya mali yenye mmiliki aliyetajwa dhidi ya kila mfumo, sera husika za majaribio za wingu na wauzaji, na barua ya idhini iliyosainiwa ambayo mjaribu anaweza kuitoa akihojiwa katikati ya ushiriki. Kwa kazi ya mashirika makubwa na serikali mfiduo ni mkali: uchunguzi usioidhinishwa dhidi ya jukwaa linaloshirikiwa unaweza kukiuka mikataba, kuchochea kuripoti kwa udhibiti, au, kwa wakala wa umma, kuwa kichwa cha habari kuhusu serikali kushambulia mifumo ambayo haikuwa na haki ya kuigusa, kwa hiyo wakili anapaswa kuidhinisha kabla mtu yeyote hajaanza.

5. **Tunawekeza kwenye red team ya ndani, kampuni za nje, au zote mbili, na mgawanyo huo unalingana na tunachohitaji kweli?** Huu ni uamuzi wa kujenga-dhidi-ya-kununua wenye fedha halisi na matokeo ya miaka mingi: timu ya ndani inagharimu mishahara na zana na hutoa uigaji wa mpinzani endelevu na ujuzi wa kina wa mazingira, wakati kampuni za nje zinagharimu zaidi kwa kila ushiriki lakini huleta macho mapya, ujuzi maalumu, na uhuru ambao wakaguzi na wadhibiti wanadai. Mvutano ni kwamba kila moja inafunika upofu wa nyingine, kwa hiyo kuzichukulia kama mbadala badala ya nyongeza kwa kawaida huacha pengo. Leta matumizi yenu ya sasa kwa kila moja, vyeti na rekodi iliyoonyeshwa ya watu wanaofanya kazi, mzunguko wa ushiriki, na mahitaji ya uhuru ambayo viwango vyenu vinaweka. Katika shirika kubwa linalodhibitiwa, PCI DSS na tawala zinazofanana zinaweza kulazimisha majaribio ya nje huru bila kujali timu yenu ya ndani ni nzuri kiasi gani; katika serikali, kanuni za ununuzi na hitaji la kuonyesha tathmini ya mbali kabla ya idhini ya kufanya kazi mara nyingi hufanya mtu wa tatu aliyeidhinishwa kuwa wa lazima, si wa hiari.

6. **Tuna njia salama kwa watafiti wa nje kuripoti udhaifu, na tuko tayari kushughulikia kinachoingia?** Shirika kubwa linalomkabili umma tayari linachunguzwa na watafiti iwe linawaalika au la, na swali pekee ni kama wanaweza kukuambia kwa usalama au wanalazimika kuchapisha au kuuza wanachopata. Mazingatio yanayoshindana ni utayari: kufungua sera ya ufichuzi ulioratibiwa au zawadi inayolipwa huzalisha ripoti zinazoingia na mzigo wa kupanga, na programu inayolipia matokeo ambayo kamwe haiyarekebishi ni mbaya kuliko hakuna. Leta faili yenu ya sasa ya security.txt na anwani ya kuripoti kama ipo, mchakato wenu wa kupokea na kupanga, ratiba za jibu mnazoweza kujitolea kwa uaminifu, na uwezo wa backlog kurekebisha kinachofika. Kwa mawakala wa serikali sera ya ufichuzi wa udhaifu kwenye mifumo ya umma inazidi kuwa agizo badala ya heshima, na kwa mashirika zawadi inayoendeshwa vizuri ni chanzo cha matokeo ya kibunifu na ushahidi wa ukomavu wakati wa uchunguzi wa wateja, kwa hiyo uamuzi si kama kuwa na njia bali kama mna wafanyakazi wa kuiheshimu.

## Mtazamo wa sekta

**Kampuni changa.** Huwezi kumudu red team ya ndani, kwa hiyo weka tabaka za ufikiaji wa bei nafuu badala yake. Unganisha uchanganuzi wa udhaifu kwenye bomba lako la usambazaji kunasa dosari za utegemezi zinazojulikana kwa kila ujenzi, chapisha faili ya security.txt na sera rahisi ya ufichuzi ulioratibiwa ili watafiti waweze kukufikia, na uagize jaribio moja la kupenya la sanduku la kijivu kutoka kampuni inayoheshimika kabla ya mkataba wako wa kwanza wa shirika kubwa, ukifuatilia kila matokeo hadi suluhisho lililothibitishwa. Kasi inajalisha zaidi ya programu pana: chagua jaribio moja linalofungua mauzo au kufunga hatari yako kubwa na uruke mengine hadi ukue.

**Biashara ndogo.** Bila mtaalamu wa usalama kwa wafanyakazi na bajeti finyu, nunua badala ya kujenga. Tumia huduma ya uchanganuzi inayosimamiwa na uajiri kampuni ya nje ya majaribio ya kupenya kwa mzunguko wa wastani badala ya kuanzisha uwezo wowote wa ndani, na hakikisha mkataba wako unajumuisha kujaribu tena ili "imerekebishwa" ithibitishwe, si kudhaniwa. Hatua yako ya thamani ya juu, gharama ya chini zaidi ni njia iliyochapishwa kwa yeyote kuripoti dosari pamoja na nidhamu ya kupachika haraka, kwa kuwa uvunjaji mwingi wa ulimwengu halisi wa biashara ya ukubwa wako unakuja kupitia udhaifu unaojulikana, ambao haujapachikwa.

**Biashara kubwa.** Kwa ukubwa changamoto ni utawala kuvuka timu nyingi. Endesha uchanganuzi endelevu chini ya majaribio ya kupenya ya nje huru ya mara kwa mara yanayotimiza viwango kama PCI DSS, dumisha red team ya ndani kwa uigaji wa mpinzani endelevu na purple teaming, na usimamie urekebishaji kama jalada linalofuatiliwa lenye wamiliki, tarehe za mwisho za hatari, na kujaribu tena kwa lazima. Lisha kila mbinu isiyogunduliwa kwenye uhandisi wa ugunduzi, na uzalishe ushahidi wa ukaguzi, ufikiaji, ratiba, na viwango vya kufunga ambavyo uzingatiaji na bodi yenu inatarajia.

**Serikali.** Kanuni za ununuzi, uwazi, na uwajibikaji wa umma huumba programu nzima. Dumisha sera ya ufichuzi wa udhaifu kwenye mifumo inayomkabili umma kama maagizo yanavyozidi kuhitaji, tumia wakaguzi huru walioidhinishwa kwa majaribio ya kupenya yanayoweka lango la idhini ya mfumo ya kufanya kazi, na uige mpinzani kwa wahusika mahususi wa dola ambao washirika wako wa kijasusi wanaweka alama. Chukulia idhini, wigo, na ushughulikiaji wa data kwa ukali wa ziada kwa sababu mifumo inaendesha uchaguzi, manufaa, na miundombinu muhimu, na ufanye kujaribu tena kuwa sharti la kuweka mfumo wowote hai.

## Mifano

**Kampuni changa.** Kampuni changa ya fintech ya watu ishirini haiwezi kumudu red team ya ndani, kwa hiyo inaweka tabaka kwa kile inachoweza. Uchanganuzi wa kiotomatiki wa udhaifu unaendeshwa kwa kila usambazaji kupitia bomba lake, ukinasa dosari za utegemezi zinazojulikana mapema. Inachapisha faili ya security.txt na sera rahisi ya ufichuzi ulioratibiwa, kisha inafungua zawadi ya wastani ya hitilafu kwenye jukwaa la umma bidhaa inapotulia, ikilipa watafiti halisi kwa hitilafu halisi. Kabla ya kusaini mteja wake wa kwanza wa shirika kubwa, inaagiza jaribio la kupenya la sanduku la kijivu la programu kutoka kampuni inayoheshimika, inafuatilia kila matokeo hadi kufungwa kwenye kifuatiliaji chake cha kawaida cha masuala, na inalipia kujaribu tena kuthibitisha marekebisho. Mbinu hii ya tabaka inatoa ufikiaji wa kuaminika wa usalama kwa gharama ambayo kampuni changa inaweza kudumisha, na ripoti ya jaribio la kupenya inakuwa ushahidi inayoweza kushiriki wakati wa uchunguzi wa wateja.

**Biashara kubwa.** Muuzaji wa rejareja wa kimataifa anayechakata malipo ya kadi lazima atimize PCI DSS, inayohitaji majaribio ya kupenya ya ndani na ya nje angalau kila mwaka na baada ya mabadiliko makubwa, pamoja na majaribio ya kugawanya kuthibitisha mazingira ya mwenye kadi yametengwa. Inaendesha uchanganuzi endelevu kuvuka maelfu ya mali, inaagiza majaribio ya kupenya ya nje huru kutimiza kiwango, na kudumisha red team ya ndani inayoendesha mazoezi ya dhana-ya-uvunjaji yaliyowekwa kwenye MITRE ATT&CK dhidi ya wahusika wa tishio wanaojulikana kulenga rejareja. Red team inafanya kazi kwa ukaribu na kazi ya operesheni za usalama ya sura ya 4.4: kila mbinu isiyogunduliwa inakuwa tiketi ya uhandisi wa ugunduzi, na vikao vya purple team vya kila robo mwaka vinarekebisha tahadhari. Urekebishaji unafuatiliwa kwa tarehe za mwisho za hatari, na programu nzima inazalisha ushahidi wa ukaguzi ambao uzingatiaji wa sura ya 4.6 unahitaji.

**Serikali.** Wakala wa kitaifa unaoendesha mifumo ya manufaa ya raia unakabili wapinzani wa dola na agizo la umma la kulinda data nyeti binafsi. Unadumisha sera ya ufichuzi wa udhaifu kwenye mifumo yote inayomkabili umma, kama maagizo ya serikali yanavyozidi kuhitaji, ukiwapa watafiti njia salama ya kuripoti dosari. Wakaguzi huru wa watu wa tatu hufanya majaribio ya kupenya kama sehemu ya mchakato wa idhini kabla mfumo wowote kuwa hai, na ufuatiliaji endelevu unajumuisha uchanganuzi unaoendelea. Wakala unaendesha uigaji wa mpinzani uliofuata makundi mahususi ya tishio ambayo washirika wake wa kijasusi wanaweka alama, na mazoezi ya mezani ya mara kwa mara yanafanyia mazoezi jibu la tukio na uratibu wa kisheria ambao uvunjaji halisi ungedai. Matokeo yanalisha programu rasmi ya urekebishaji yenye ratiba za lazima, na kujaribu tena ni sharti la kuweka idhini ya mfumo ya kufanya kazi.

## Kesi ya biashara: sababu, ROI, na TCO

Faida ya usalama wa kushambulia ni uvunjaji ambao hukuuteseka. Uvunjaji mkubwa wa data unagharimu mamilioni katika jibu la moja kwa moja, faini za udhibiti, dhima ya kisheria, kuondoka kwa wateja, na uharibifu wa sifa, na kipengele ghali zaidi ni muda ambao uvamizi unabaki bila kugunduliwa. Red teaming na purple teaming hushambulia namba hiyo moja kwa moja kwa kupunguza pengo kati ya kuathirika na ugunduzi. Jaribio la kupenya linalopata njia inayonyonyeka kwenda hifadhidata yako ya wateja, na kurekebishwa kabla mshambulizi hajaipata, hulipia programu nzima mara nyingi kwa tukio moja lililoepukwa.

Pia kuna vichocheo vigumu. PCI DSS inaamuru majaribio ya kupenya kwa yeyote anayeshughulikia data ya kadi. Mifumo na tawala za idhini za serikali zinahitaji tathmini huru kabla na wakati wa operesheni. Wateja wa mashirika makubwa wanadai ripoti za hivi karibuni za majaribio ya kupenya kama sharti la mikataba. Katika hali hizi majaribio si ya hiari, na swali ni kama mnatoa thamani halisi ya usalama kutoka fedha ambazo lazima mzitumie hata hivyo.

Jumla ya gharama ya umiliki inajumuisha zaidi ya ada ya ushiriki. Weka bajeti ya zana na wafanyakazi wa timu ya ndani kama mnaijenga, mzigo wa kupanga wa zawadi ya hitilafu, na zaidi ya yote kazi ya urekebishaji ambayo matokeo huzalisha, ambapo matumizi halisi hutua. Programu inayoagiza majaribio lakini inakosesha fedha kurekebisha ni mbaya mara mbili: inalipia habari mbaya kisha inalipa tena matokeo yaliyopuuzwa yanapofyonzwa. Kuweka kesi kwa uongozi, unganisha majaribio na vipimo wanavyofuatilia: muda wa wastani wa kugundua, muda wa wastani wa kurekebisha, matokeo ya ukaguzi yaliyofungwa, na upunguzaji wa hatari kwenye mali zako muhimu zaidi.

## Mifumo mibaya na mitego

- **Changanua-na-ubadili-jina:** kuuza uchanganuzi wa udhaifu kama jaribio la kupenya, kukabidhi matokeo ya zana bila uthibitishaji wa binadamu wala kuunganisha unyonyaji.
- **Ripoti na usahau:** kuchukulia kikabidhiwa kama lengo, kuweka matokeo kwenye faili, na kutowahi kufuatilia urekebishaji wala kujaribu tena.
- **Wigo wa kupita:** kupunguza ushiriki ili mifumo inayoelekea kushindwa zaidi iwe nje ya mipaka kwa urahisi, ukizalisha ripoti safi isiyo na maana.
- **Red team kama ubao wa alama:** timu ya kiuadui inayohodhi mbinu na kusherehekea ushindi badala ya kuwafanya watetezi kuwa bora.
- **Kujaribu timu ya buluu changa kwa siri:** kuendesha red team ya siri kabla ya kuwa na uwezo wowote wa ugunduzi, kwa hiyo zoezi linathibitisha tu mliyokuwa mnayajua.
- **Hakuna idhini au wigo usio wazi:** kuanza kazi bila ruhusa iliyoandikwa, au kuacha wigo kuingia kwenye mifumo msiyoimiliki, kuita maafa ya kisheria.
- **Kupenda mzunguko kupita kiasi:** kujaribu ukingo wa nje tu huku ukipuuza uhalisia wa dhana-ya-uvunjaji kwamba washambulizi huanzia ndani.
- **Kupuuza njia ya ufichuzi:** kutokuwa na njia salama kwa watafiti wa nje kuripoti hitilafu, kwa hiyo wanachapisha hadharani au kuuza.
- **Vipimo vya maigizo:** kuhesabu udhaifu uliopatikana badala ya hatari iliyopunguzwa, ugunduzi ulioboreshwa, na muda wa kurekebisha uliofupishwa.

## Kielelezo cha ukomavu

- **Ngazi ya 1, Kuanzisha:** Majaribio ni ya mara kwa mara na ya kuitikia, mara nyingi jaribio moja la kupenya la kila mwaka lililofanywa kuweka alama kwenye kisanduku, au linalochochewa baada ya tukio tu. Ripoti zinawekwa kwenye faili bila ufuatiliaji mwingi, urekebishaji haufuatiliwi, hakuna njia ya ufichuzi, na ugunduzi wa uvamizi halisi haujajaribiwa na kuna uwezekano haupo.
- **Ngazi ya 2, Kuendeleza:** Uchanganuzi wa udhaifu na majaribio ya kupenya yapo lakini hayana uthabiti kuvuka timu, baadhi ya vikundi vikichanganua mfululizo na vingine hata kidogo. Matokeo yananaswa mahali fulani, ingawa wamiliki na tarehe za mwisho zina mashimo, kujaribu tena ni kwa papo hapo, na njia ya ufichuzi ulioratibiwa inaweza kuwepo kwa baadhi ya mifumo lakini si eneo zima.
- **Ngazi ya 3, Kusawazisha:** Majaribio ya kushambulia ni programu iliyoandikwa inayotekelezwa shirika zima, si tukio. Uchanganuzi unaendeshwa mfululizo chini ya majaribio ya kupenya yaliyopangwa yaliyoagizwa kwa mzunguko uliofafanuliwa na baada ya mabadiliko makubwa, kanuni za ushiriki na idhini ni mazoea ya kawaida, kila matokeo yanafuatiliwa hadi kufungwa yakiwa na mmiliki na tarehe ya mwisho ya hatari, kujaribu tena ni lazima, na sera ya ufichuzi ulioratibiwa inafunika mifumo yote inayomkabili umma.
- **Ngazi ya 4, Kusimamia:** Programu inapimwa na kudhibitiwa dhidi ya vipimo vya msingi. Mnafuatilia muda wa wastani wa kugundua na muda wa wastani wa kurekebisha, asilimia ya mbinu za red team zilizozalisha ishara, ufikiaji wa ugunduzi dhidi ya mbinu za MITRE ATT&CK zinazohusika na sekta yenu, viwango vya kurudi kwa matokeo, na muda wa jibu la ufichuzi, na mnashikilia kila kipimo dhidi ya lengo na kutenda kinapoteleza. Mazoezi ya dhana-ya-uvunjaji na uigaji wa mpinzani ni ya kawaida, red team inafanya kazi mfululizo, matokeo yanalisha uhandisi wa ugunduzi, na maamuzi ya kwenda au kutokwenda yanategemea ushahidi badala ya maoni.
- **Ngazi ya 5, Kuratibu:** Red na purple teaming zimeunganishwa kuvuka shirika na zinajirekebisha. Kila mbinu inaoana na ugunduzi uliojaribiwa, uigaji wa mpinzani unafuata wahusika mahususi wa tishio wanaolenga sekta yenu kwa sasa upelelezi unapohama, na programu inaboresha wigo wake, mbinu, na vipimo mfululizo inapojifunza. Majaribio ya kushambulia, operesheni za usalama, uhandisi wa ugunduzi, na jibu la tukio hufanya kazi kama mzunguko mmoja unaopunguza kwa kupimika pengo kati ya kuathirika na ugunduzi kadiri muda unavyopita.

## Mawazo ya kujadili

1. Mshambulizi halisi akipata nafasi ya kuanzia kama mfanyakazi wa kawaida leo, angefika umbali gani kabla mtu yeyote hajaona, na mnajuaje?
2. Ushiriki wenu upi wa mwisho ulikuwa wa kweli kweli, na upi uliwekewa wigo ili kushindwa kunakoelekea kuwe nje ya mipaka kwa urahisi?
3. Matokeo mangapi kutoka jaribio lenu la awali bado ni wazi, na hilo linasema nini kuhusu kama majaribio au urekebishaji ndio kizuizi chenu halisi?
4. Watafiti wa nje wana njia salama, dhahiri ya kuwaripotia udhaifu, na nini kinatokea ripoti inapofika?
5. Wajibuji wenu wa matukio walifanyia mazoezi uvunjaji kwenye karatasi mara ya mwisho lini, na zoezi la mezani lilifichua mapengo ambayo majaribio yenu ya kiufundi yalikosa?
6. Mnapima udhaifu uliopatikana, au mnapima ugunduzi ulioboreshwa na hatari iliyopunguzwa?

## Mambo muhimu ya kukumbuka

- Usalama wa kushambulia ni wigo: uchanganuzi hupata dosari zinazojulikana, majaribio ya kupenya huthibitisha uwezekano wa kunyonywa, na red teaming hujaribu ugunduzi na jibu. Linganisha ushiriki na swali.
- Idhini iliyoandikwa na kanuni wazi za ushiriki ndizo mstari kati ya majaribio ya usalama na uhalifu; usiziruke kamwe, hasa kwenye mifumo usiyoimiliki kikamilifu.
- Thamani iko katika urekebishaji na kujaribu tena, si ripoti. Fuatilia kila matokeo yakiwa na mmiliki, tarehe ya mwisho ya hatari, na suluhisho lililothibitishwa.
- Red team ipo kuifanya timu ya buluu iwe bora. Lisha matokeo kwenye uhandisi wa ugunduzi, pendelea purple teaming na mazoezi ya dhana-ya-uvunjaji, na weka kampeni kwenye mbinu halisi za wapinzani kupitia MITRE ATT&CK.
- Pima ugunduzi na jibu, si hesabu za udhaifu tu, na ujihadhari na ushiriki uliowekewa wigo ili kupita, unaozalisha faraja bila usalama.

## Marejeo na usomaji zaidi

- Georgia Weidman, *Penetration Testing: A Hands-On Introduction to Hacking*
- Peter Kim, *The Hacker Playbook 3: Practical Guide to Penetration Testing*
- Jim O'Gorman, Devon Kearns, and Mati Aharoni, *Metasploit: The Penetration Tester's Guide*
- Joe Vest and James Tubberville, *Red Team Development and Operations: A Practical Guide*
- MITRE, *MITRE ATT&CK* framework and knowledge base
- Payment Card Industry Security Standards Council, *PCI DSS Requirements and Testing Procedures* and *Penetration Testing Guidance*
- National Institute of Standards and Technology, *NIST SP 800-115: Technical Guide to Information Security Testing and Assessment*
- Dafydd Stuttard and Marcus Pinto, *The Web Application Hacker's Handbook*
