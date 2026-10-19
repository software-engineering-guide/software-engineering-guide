# 4.1 Misingi ya usalama na utamaduni

## Muhtasari na msukumo

Usalama si kipengele unachokibana mwishoni, na si kazi ya timu moja maalumu iliyokaa mbali na uhandisi. Katika shirika kubwa, usalama ni sifa ya jinsi mfumo mzima unavyobuniwa, kujengwa, kuendeshwa, na kutawaliwa. Maelfu ya wahandisi wanaposafirisha msimbo kuvuka huduma mamia, kiungo dhaifu zaidi huamua tukio linaweza kusababisha madhara kiasi gani. Ndoo moja ya uhifadhi iliyosanidiwa vibaya, utegemezi ambao haujapachikwa, au akaunti ya huduma yenye upendeleo kupita kiasi inaweza kufichua mamilioni ya rekodi. Misingi na utamaduni ndivyo vinavyozuia hilo kwa ukubwa.

Kwa mashirika makubwa, dau ni la kifedha na la sifa: gharama za uvunjaji, faini za udhibiti, wateja waliopotea, na thamani zilizoshuka. Kwa serikali, zinaenea hadi usalama wa taifa, uaminifu wa umma, na mwendelezo wa huduma muhimu. Mazingira yote mawili yanashiriki ukweli mgumu: huwezi kutekeleza usalama kwa vidhibiti na malango peke yake. Lazima umezwe na watu wanaofanya kazi. Utamaduni ambapo wahandisi wanaelewa vitisho, wanahisi umiliki, na wanatuzwa kwa kuibua wasiwasi huzalisha matokeo bora zaidi sana kuliko ule unaotegemea timu ya usalama iliyochoka ikicheza golikipa.

Sura hii inaweka vielelezo vya kiakili na mazoea ya kiutamaduni yanayounga mkono kila sura nyingine ya usalama katika mwongozo huu. Inashughulikia kufanya usalama kuwa kazi ya kila mtu, [uundaji wa vitisho](https://en.wikipedia.org/wiki/Threat_model), mzunguko salama wa uendelezaji, kanuni za msingi za usanifu kama [ulinzi wa kina](https://en.wikipedia.org/wiki/Defense_in_depth_(computing)) na [uaminifu-sifuri](https://en.wikipedia.org/wiki/Zero_trust_security_model), na jinsi ya kuweka kipaumbele kazi ya usalama kwa hatari halisi badala ya hofu au mitindo.

*Angalia pia:* sura ya 4.2 (usalama wa programu), sura ya 4.3 (usalama wa miundombinu na wingu), sura ya 4.4 (operesheni za usalama), na sura ya 4.6 (uzingatiaji na utawala) zinajengwa juu ya misingi hii.

## Kanuni kuu

- **Usalama ni kazi ya kila mtu.** Kila mhandisi, meneja wa bidhaa, na mwendeshaji anamiliki usalama wa anachojenga. Timu ya usalama inawezesha, inashauri, na inakagua; haifanyi na haiwezi kufanya kazi peke yake.
- **Dhania uvunjaji.** Buni kana kwamba washambulizi tayari wako ndani. Punguza kile kijenzi kilichoathirika kinaweza kufikia.
- **Ulinzi wa kina.** Hakuna kidhibiti kimoja kinachotosha. Panga vidhibiti huru kwa tabaka ili kushindwa kwa kimoja kusimaanishe kushindwa kwa vyote.
- **[Upendeleo mdogo](https://en.wikipedia.org/wiki/Principle_of_least_privilege).** Toa ufikiaji wa kiwango cha chini kinachohitajika, kwa muda mfupi zaidi, na uufute kiotomatiki usipohitajika tena.
- **Sogeza kushoto.** Tafuta na urekebishe matatizo mapema iwezekanavyo, yanapokuwa nafuu zaidi kurekebisha.
- **Kuweka kipaumbele kwa hatari.** Tumia juhudi pale mchanganyiko wa uwezekano na athari ni wa juu zaidi, ukiongozwa na utatu wa CIA (usiri, uadilifu, na upatikanaji), si kwa chochote kilichofanya habari wiki hii.
- **Kujifunza bila lawama.** Chukulia matukio ya usalama na karibu-makosa kama fursa za kujifunza, si nafasi za adhabu.

## Mapendekezo

### Anzisha programu ya mabingwa wa usalama

Weka bingwa wa usalama aliyeteuliwa katika kila timu ya uhandisi. Mabingwa si wataalamu wa usalama wa muda wote. Ni wahandisi wenye mafunzo ya ziada na mstari wa moja kwa moja kwa timu kuu ya usalama. Wanapitia miundo, wanapanga matokeo, wanajibu maswali ya wenzao, na wanabeba muktadha wa usalama kwenye upangaji. Hii inapanua utaalamu wa usalama kuvuka shirika bila kuajiri mtaalamu kwa kila timu, na inajenga uaminifu, kwa sababu ushauri unatoka kwa mwenzao anayejua msimbo kweli.

Wape mabingwa msaada halisi: jukwaa la kawaida la kushiriki wanachojifunza, bajeti ya mafunzo na mikutano, kutambuliwa katika tathmini za utendaji, na muda uliotengwa kutoka ahadi zao za utoaji. Programu ya mabingwa iliyopo kwenye karatasi tu haizalishi chochote.

### Fanya uundaji wa vitisho kuwa wa kawaida

Uundaji wa vitisho ni tabia yenye nidhamu ya kuuliza "nini kinaweza kwenda vibaya?" kabla ya kujenga. Ifanye kwa huduma mpya, vipengele vikuu, na badiliko lolote la mipaka ya uaminifu. Iweke nyepesi vya kutosha ifanyike mara nyingi kweli.

- **[STRIDE](https://en.wikipedia.org/wiki/STRIDE_model)** ni orodha hakiki ya kiutendaji iliyooanishwa na sifa za usalama: Spoofing (uthibitishaji), Tampering (uadilifu), Repudiation (kutokanusha), Information disclosure (usiri), Denial of service (upatikanaji), na Elevation of privilege (uidhinishaji). Pitia kila mtiririko wa data na uulize jinsi kila kategoria inavyotumika.
- **PASTA** (Process for Attack Simulation and Threat Analysis) ni njia nzito zaidi ya hatua saba inayolenga hatari inayounganisha vitisho vya kiufundi na athari ya biashara; itumie kwa mifumo yenye thamani ya juu.
- **[Miti ya shambulio](https://en.wikipedia.org/wiki/Attack_tree)** huvunja lengo ("iba data ya wateja") kuwa hatua zenye matawi ambazo mshambulizi angechukua, ikikusaidia kupata na kukata njia.

Weka miundo ya vitisho kama nyaraka hai kando ya msimbo, na uipitie upya wakati wowote usanifu unapobadilika.

### Jenga mzunguko salama wa uendelezaji

Funga usalama katika kila awamu badala ya kuuchukulia kama lango la mwisho:

- **Mahitaji:** nasa mahitaji ya usalama na faragha kando ya ya kiutendaji.
- **Usanifu:** unda vitisho na upitie mipaka ya uaminifu.
- **Utekelezaji:** tekeleza viwango salama vya uandishi wa msimbo, mapitio ya msimbo, na uchanganuzi wa siri kabla ya commit.
- **Majaribio:** endesha [SAST](https://en.wikipedia.org/wiki/Static_application_security_testing) (upimaji tuli wa usalama wa programu), [DAST](https://en.wikipedia.org/wiki/Dynamic_application_security_testing) (upimaji wa kidinamiki wa usalama wa programu), na uchanganuzi wa utegemezi kwenye bomba (angalia sura ya 4.4).
- **Toleo:** thibitisha asili, saini vitu, na ukague usanidi.
- **Uendeshaji:** fuatilia, pachika, na ujibu.

Hoja ya kusogeza kushoto si kurundika kazi yote mapema na kuwalemea wahandisi. Ni kunasa aina za kasoro ambazo ni nafuu zaidi sana kurekebisha mapema.

### Pokea kanuni za usanifu wa uaminifu-sifuri

Usalama wa jadi wa mzunguko hudhani kila kitu ndani ya mtandao kinaaminika. Dhana hiyo inashindwa mara mshambulizi anapopata mguu. Uaminifu-sifuri hubadilisha uaminifu wa mtandao wa kimyakimya na uthibitisho wazi, endelevu: thibitisha na idhinisha kila ombi kulingana na utambulisho, msimamo wa kifaa, na muktadha, bila kujali linatoka wapi kwenye mtandao. Changanya utambulisho imara, uidhinishaji wa upendeleo mdogo, kugawanya kwa kina, na [usimbaji fiche](https://en.wikipedia.org/wiki/Encryption) kila mahali. Uaminifu-sifuri ni safari, si bidhaa, kwa hiyo uchukulie hatua kwa hatua.

### Weka vipaumbele kwa hatari ukitumia utatu wa CIA

Panga kila mali na kidhibiti kuzunguka **Usiri**, **Uadilifu**, na **Upatikanaji**. Si data yote inahitaji ulinzi sawa: ukurasa wa uuzaji wa umma na hifadhidata ya rekodi za afya zina mahitaji tofauti sana ya usiri. Ainisha mali zako, kadiria uwezekano na athari ya kuathiriwa, na uelekeze juhudi adimu ya usalama kwenye michanganyiko ya hatari ya juu zaidi. Andika maamuzi yako ya hatari ili wengine waweze kuyapitia na kuyatetea baadaye.

## Mabadilishano: faida na hasara

| Mbinu | Faida | Hasara |
|---|---|---|
| Timu kuu ya usalama inamiliki usalama wote | Utaalamu wa kina, viwango thabiti | Kizuizi, wahandisi hujitoa, haipanuki |
| Usalama uliosambazwa (mabingwa) | Hupanuka, hujenga umiliki, maoni ya haraka | Inahitaji uwekezaji, ujuzi usio sawa, inahitaji uratibu |
| Uundaji mzito wa vitisho wa awali kwa kila kitu | Wa kina, hunasa dosari za usanifu | Hupunguza kasi ya utoaji, unaweza kuwa kuweka alama tu |
| Uundaji mwepesi wa vitisho unaolenga hatari | Haraka, unalenga kinachojalisha | Unaweza kukosa vitisho katika mifumo ya "hatari ndogo" |
| Malango makali yanayozuia matoleo | Hutekeleza uzingatiaji | Msuguano, huchochea njia za kuzunguka |

Mvutano wa msingi ni kati ya kasi na uhakikisho. Egemea sana malango na udhibiti wa kati, na unaunda msuguano ambao wahandisi huuzunguka, ukizaa TEHAMA ya kivuli na uchungu. Egemea sana uhuru bila msaada, na unapata usalama usio thabiti, usiokaguliwa. Jibu endelevu ni utamaduni imara wenye vizuizi vinavyowezesha: vya kiotomatiki pale unaweza, vya binadamu pale busara inahitajika, na daima vilivyoelezwa badala ya kuwekwa tu.

## Maswali ya kujadili na timu yako

1. **Mifumo ipi yenu inastahili uundaji mzito wa vitisho, na nani anaamua ngazi?** Katika eneo kubwa huwezi kuendesha uchambuzi wa PASTA wa hatua saba kwa kila huduma, kwa hiyo unahitaji kanuni wazi ya lini pasi ya STRIDE ya dakika 30 inatosha na lini mfumo wenye thamani ya juu unastahili uundaji wa kina unaoendeshwa na athari ya biashara. Funga uamuzi kwenye uainishaji wako wa CIA: mifumo inayoshikilia rekodi zinazodhibitiwa, mtiririko wa malipo, au mantiki ya uthibitishaji iko juu, na ukurasa wa uuzaji wa umma hauko. Kwa kazi ya mashirika makubwa na serikali, mkaguzi atakuomba utetee kwa nini mfumo fulani uliundwa jinsi ulivyoundwa, kwa hiyo andika vigezo vya ngazi na taja mmiliki anayevitumia. Leta uainishaji wenu wa sasa wa mali na orodha ya huduma zisizo na kielelezo cha vitisho kwenye mkutano, kwa sababu pengo kati yake ndilo hatari yenu halisi. Mkishindwa kukubaliana kiwango, mtaelekea kuunda kila kitu kwa wepesi au hakuna kwa kina, na yote mawili yanawashinda.

2. **Bingwa wa usalama na tarehe ya mwisho ya utoaji zinapogongana, nani anaweza kusimamisha toleo kweli?** Programu ya mabingwa hubadilisha matokeo tu ikiwa bingwa ana mamlaka halisi, si mafunzo ya ziada na nia njema tu. Amua mapema kama bingwa anaweza kuzuia kusafirisha, kama anapandisha kwa timu kuu ya AppSec, na ukali wa matokeo gani unahalalisha kusimamisha utoaji dhidi ya kufuatilia tu. Hili ni muhimu zaidi chini ya shinikizo, meneja wa bidhaa anapotaka kusamehe dosari ya usanifu wiki moja kabla ya uzinduzi, ambayo ndiyo hasa wakati dosari zisizoshughulikiwa zinapokuwa ghali zaidi kurekebisha. Leta mfano wa hivi karibuni ambapo wasiwasi wa usalama ulikutana na tarehe ya mwisho na ufuatilie nani aliamua na jinsi, kwa sababu hadithi hiyo hufichua njia yenu halisi ya kupandisha. Jibu la uaminifu likiwa kwamba utoaji daima hushinda, mabingwa wenu ni mapambo na mnapaswa kurekebisha kichocheo kabla ya kuongeza wengine.

3. **"Dhania uvunjaji" inabadilisha nini madhubuti katika mapitio yenu ya usanifu yanayofuata?** Kanuni ni rahisi kukubali na ngumu kuitekeleza, kwa hiyo ifunge kwa ahadi mahususi: mipaka ipi ya uaminifu mtakaoibana, wapi mtaongeza kugawanya kwa kina, na jinsi mtakavyopunguza kile akaunti moja ya huduma iliyoathirika inaweza kufikia. Kwa timu kubwa, malipo ni kupunguza eneo la mlipuko, ili mshambulizi anayetua kwenye huduma moja asiweze kuhamia hifadhi ya data nyuma yake. Katika mazingira ya mashirika makubwa na serikali hii pia inaumba maamuzi yenu ya upendeleo mdogo na vitambulisho vya muda mfupi, ambavyo ni nafuu kubuni ndani na chungu kurudisha. Leta mchoro mmoja halisi wa huduma na uliza mshambulizi anafanya nini baada ya kumiliki ngazi ya wavuti, kisha jitoe kwa mabadiliko mawili ya kudhibiti robo hii. Makubaliano yasiyo wazi kwamba uvunjaji hutokea hayana thamani isipokuwa yanasogeza ruhusa, kanuni ya mtandao, au muda wa maisha wa kitambulisho.

4. **Mtajuaje utamaduni wenu wa usalama unaboreka kweli, na kipimo gani mngekitetea kwa bodi?** Viwango vya kukamilisha mafunzo na hesabu za tiketi ni rahisi kukusanya na karibu hazina manufaa, kwa sababu hupima shughuli badala ya kupunguza hatari, na shirika kubwa linazama ndani yake. Chagua vipimo vya matokeo ambavyo mngeweka bajeti juu yake: muda wa wastani wa kurekebisha matokeo makali, sehemu ya huduma zenye kielelezo cha sasa cha vitisho, sehemu ya matukio yanayonaswa kabla ya uzalishaji, na kiwango cha karibu-makosa yanayoripotiwa wenyewe, ambacho kinapaswa kupanda uaminifu unavyokua badala ya kushuka. Mazingatio yanayoshindana ni kwamba kila kipimo kizuri kinaweza kuchezewa, kwa hiyo oanisha kila kimoja na kipimo cha kukabili na upitie mwelekeo badala ya picha ya papo hapo. Leta dashibodi yenu ya sasa na uliza namba zipi zingebadilika usalama ukizidi kuwa mbaya kweli; zozote ambazo hazingebadilika ni mapambo. Katika mazingira ya mashirika makubwa na serikali mdhibiti au kamati ya ukaguzi itaomba ushahidi kwamba vidhibiti vinafanya kazi, kwa hiyo chagua vipimo mnavyoweza kutetea chini ya uchunguzi badala ya vile vinavyoonekana kijani tu.

5. **Nini kinatokea mhandisi atakaporipoti kosa wakati ujao, na je, mchakato wenu hauna lawama kivitendo au kwenye slaidi tu?** Kujifunza bila lawama ndiyo kanuni inayotangazwa mara nyingi na kuishi mara chache, kwa sababu tukio la kwanza kubwa hujaribu kama uongozi unamaanisha kweli. Amua mapema jinsi mnavyotenganisha uwajibikaji wa kurekebisha tatizo na adhabu kwa kulisababisha, na nani anaendesha mapitio ya baada ya tukio ili yabaki kuhusu mifumo iliyovunjika badala ya watu waliotajwa. Mvutano ni halisi: wadau wanataka mtu awajibishwe, hata hivyo kumwadhibu mripoti kunahakikisha kosa linalofuata linabaki limefichwa hadi kuwa uvunjaji. Leta mapitio yenu mawili ya mwisho ya matukio na uangalie kama yalimlaumu mtu au kidhibiti, na kama mhandisi aliyepiga kengele alishukuriwa au kuwekwa kando kimyakimya. Kwa serikali na mashirika makubwa yanayodhibitiwa, sheria za lazima za kufichua uvunjaji huinua dau zaidi, kwa sababu utamaduni unaoficha makosa pia utakosa tarehe za mwisho za kuripoti zinazobeba adhabu za kisheria.

6. **Nani anamiliki msuguano wa zana zenu za kusogeza-kushoto, na mnazinunua, kuzijenga, au kuzama ndani yake?** Uchambuzi wa kiotomatiki tuli na wa kidinamiki, uchanganuzi wa utegemezi, na uchanganuzi wa siri ndio uti wa mgongo wa mzunguko salama wa uendelezaji, lakini bomba linalofurika wahandisi na matokeo ya uongo huwafunza kupuuza matokeo ya usalama, jambo baya zaidi kuliko kutokuwa na uchanganuzi kabisa. Amua nani anarekebisha zana, nani anapanga matokeo, na kama mnanunua jukwaa lililounganishwa au mnakusanya vichanganuzi vya chanzo huria ambavyo kisha mnalazimika kuvidumisha wenyewe. Mazingatio yanayoshindana ni ufikiaji dhidi ya kelele na udhibiti dhidi ya gharama: kichanganuzi cha bei nafuu kinacholia mbwa-mwitu huchoma uaminifu ambao programu ya mabingwa ilitumia miaka kuujenga. Leta kiwango chenu cha sasa cha matokeo ya uongo, wastani wa muda ambao wahandisi wanasubiri ukaguzi unaozuia, na orodha ya timu zilizozima lango kimyakimya. Katika mashirika makubwa na serikali, ongeza pembe ya ununuzi na mtawanyiko wa zana, kwa sababu timu kumi zikinunua kichanganuzi chake kila moja huzalisha ufikiaji usio thabiti ambao hakuna mkaguzi anayeweza kupatanisha.

## Mtazamo wa sekta

**Kampuni changa.** Bila timu ya usalama na muda mfupi wa fedha, utamaduni ndio kidhibiti chako pekee cha kumudu. Fanya ubao mweupe wa uundaji wa vitisho wa dakika 30 kuwa tabia kabla ya kipengele chochote kinachogusa uthibitishaji au malipo, washa upendeleo mdogo na MFA kila mahali kwa sababu havigharimu chochote, na uweke njia isiyo na lawama ambapo yeyote anaweza kuibua wasiwasi. Ruka mchakato mzito na zana; wahandisi waanzilishi hawawezi kuvidumisha, na nidhamu unayoijenga sasa ndiyo itakayowaruhusu wanunuzi wa mashirika makubwa kukuamini baadaye.

**Biashara ndogo.** Huna mtaalamu maalumu wa usalama na bajeti ni finyu, kwa hiyo tegemea chaguo-msingi salama katika zana unazonunua tayari badala ya kuanzisha bomba lako mwenyewe. Pendelea majukwaa yanayosimamiwa yanayotekeleza MFA, kupachika, na upendeleo mdogo kwa ajili yako, na uchukulie usalama kama swali la usafi wa data: jua data nyeti gani unashikilia na nani anaweza kuifikia. Unapolazimika kuchagua kujenga dhidi ya kununua, nunua, kwa sababu kidhibiti kinachosimamiwa unachokiweka cha sasa kinashinda maalumu unachokiacha kioze.

**Biashara kubwa.** Kwa ukubwa wa huduma mamia na maelfu ya wahandisi, changamoto ni uthabiti na utawala kuvuka timu nyingi. Endesha programu ya mabingwa wa usalama, sawazisha ngazi za uundaji wa vitisho zilizofungwa na uainishaji wa CIA, na utoe violezo vya njia iliyopakwa lami na ukaguzi wa kiotomatiki wa bomba ili kila timu irithi chaguo-msingi nzuri. Fuatilia vipimo vya urekebishaji na ufikiaji dhidi ya vipimo vya msingi, na uweke njia ya ukaguzi inayoonyesha kwa nini kila mfumo uliundwa na kudhibitiwa jinsi ulivyodhibitiwa.

**Serikali.** Kanuni za ununuzi, wajibu wa uwazi, na uwajibikaji wa umma huumba kila uchaguzi. Kanuni za uaminifu-sifuri na vitambulisho vya muda mfupi mara nyingi huamriwa na sera ya utendaji, na lazima uweze kumwonyesha mkaguzi sababu iliyoandikwa, inayotegemea hatari ya mahali bajeti ya kuimarisha ilipoenda. Weka kipaumbele mifumo inayoshikilia rekodi nyeti zaidi za raia kwanza, chapisha vizuizi mahali umma una haki ya kujua, na udai wauzaji wafichue mapungufu badala ya kukubali masanduku meusi yasiyo wazi.

## Mifano

**Kampuni changa.** Kampuni changa ya watu kumi haina timu ya usalama wala bajeti ya moja, kwa hiyo wahandisi wawili waanzilishi wanafanya uundaji wa vitisho kuwa tabia ya ubao mweupe wa dakika 30 kabla ya kipengele chochote kinachogusa uthibitishaji au malipo, wakiuliza nini kinaweza kwenda vibaya na nani angetaka kitokee. Wanapokea tabia chache za msingi zisizogharimu chochote: upendeleo mdogo kwenye kila jukumu la wingu, MFA kwenye kila akaunti, na njia isiyo na lawama ambapo yeyote anaweza kuibua wasiwasi bila hofu ya lawama. Wanapokusanya mzunguko wa uwekezaji baadaye na wanunuzi wa mashirika makubwa wanauliza wanashughulikiaje usalama, utamaduni huo wa mapema unawaruhusu kujibu kwa uaminifu badala ya kuhangaika kuvumbua mmoja.

**Biashara kubwa.** Benki ya kimataifa yenye wahandisi 6,000 inaendesha programu ya mabingwa wa usalama yenye bingwa mmoja aliyefunzwa kwa kila kikosi. Mabingwa wanahudhuria chama cha kila mwezi, wanakamilisha mafunzo ya kila robo mwaka, na kuongoza uundaji wa vitisho kwa kila huduma mpya wakitumia STRIDE. Timu kuu ya AppSec inadumisha violezo vya njia iliyopakwa lami na ukaguzi wa kiotomatiki wa bomba. Kwa miaka miwili, muda wa wastani wa kurekebisha matokeo makali ulishuka kutoka siku 45 hadi 9, na uundaji wa vitisho wa hatua ya usanifu ulinasa dosari ya uidhinishaji katika API ya malipo kabla ya kufika uzalishaji, ukiepuka tukio linaloweza kuripotiwa.

**Serikali.** Wakala wa kitaifa wa kodi unaoboresha mifumo ya urithi unapokea kanuni za uaminifu-sifuri zinazoamriwa na sera ya utendaji. Kila wito wa huduma ya ndani unathibitishwa kwa vitambulisho vya muda mfupi na kuidhinishwa kwa kila ombi; sehemu za mtandao hazitoi uaminifu tena. Wakala unaunda vitisho vya kila huduma inayomkabili raia dhidi ya miti ya shambulio yenye mizizi katika "iba rekodi za walipa kodi" na "badilisha uwasilishaji." Kuweka kipaumbele kwa hatari, kulingana na viwango vya athari vya CIA, kunaelekeza bajeti ya kuimarisha kwa mifumo inayoshikilia rekodi nyeti zaidi kwanza.

## Kesi ya biashara: sababu, ROI, na TCO

Gharama ya kujenga utamaduni wa usalama ni halisi: muda wa mabingwa, mafunzo, zana, na mzigo wa wastani wa kufanya uundaji wa vitisho na mapitio. Lakini gharama hiyo ni ndogo ikilinganishwa na gharama ya kutoufanya. Wastani wa uvunjaji mkubwa wa data hufikia mamilioni ukihesabu uchunguzi, arifa, urekebishaji, faini za udhibiti, mfiduo wa kisheria, na biashara iliyopotea. Uvunjaji wa serikali huongeza usumbufu wa dhamira na mmomonyoko wa uaminifu wa umma ambao hakuna ankara inayoukamata kikamilifu.

Malipo ya uwekezaji wa usalama yanatokana na mahali pa tatu: **matukio yaliyoepukwa** (uvunjaji ambao haufanyiki kamwe), **gharama ya urekebishaji iliyopunguzwa** (kasoro zilizorekebishwa wakati wa usanifu zinagharimu sehemu ndogo ya zile zilizorekebishwa kwenye uzalishaji), na **utoaji wa haraka zaidi** (njia zilizopakwa lami na ukaguzi wa kiotomatiki huruhusu timu kusafirisha kwa kujiamini badala ya kusubiri mapitio ya mkono). Unapoweka kesi kwa uongozi, weka usalama kama usimamizi wa hatari wenye bei, si wema wa dhahania. Onyesha hasara inayotarajiwa (uwezekano mara athari) ya hatari kuu, gharama ya kuzipunguza, na hatari inayobaki. Watendaji hufadhili upunguzaji wa hatari wanaoweza kuupima.

## Mifumo mibaya na mitego

- **Maigizo ya usalama.** Vidhibiti vinavyoonekana vya kuvutia lakini havipunguzi hatari halisi, vilivyopokelewa kutimiza ukaguzi badala ya kulinda chochote.
- **Timu ya usalama kama lango mwishoni.** Kugundua dosari za usanifu wiki moja kabla ya uzinduzi, zinapokuwa ghali zaidi kurekebisha na zinaelekea zaidi kusamehewa.
- **Utamaduni wa lawama.** Kumwadhibu mhandisi anayeripoti kosa kunahakikisha kosa linalofuata linabaki limefichwa.
- **Uundaji wa vitisho wa kuweka alama.** Kujaza kiolezo ambacho hakuna anayekisoma, kuzalisha nyaraka zilizotengwa na usanifu halisi.
- **Vidhibiti vya ukubwa mmoja kwa wote.** Kutumia mchakato mzito uleule kwa tovuti ya umma na mfumo wa malipo, kupoteza juhudi na kuzaa chuki.
- **Kuweka kipaumbele kwa hofu.** Kufukuza udhaifu wowote unaovuma kwenye habari badala ya kinachotishia mali zako kweli.
- **Mabingwa kwa jina tu.** Kuwataja mabingwa bila kuwapa muda, mafunzo, wala mamlaka.

## Kielelezo cha ukomavu

**Ngazi ya 1: Kuanzisha.** Usalama ni wa kuitikia na wa kati. Mapitio hufanyika kuchelewa kama yapo, na hakuna uundaji wa vitisho. Matukio huendesha marekebisho ya papo hapo. Wahandisi wanaona usalama kama tatizo la mtu mwingine, na hakuna kiwango cha pamoja.

**Ngazi ya 2: Kuendeleza.** Timu ya usalama ipo na kufafanua viwango, lakini mazoea hayana uthabiti kuvuka timu. Uundaji wa vitisho fulani hufanyika kwenye miradi mikuu na hakuna kwenye mingine. Mafunzo ya msingi yanapatikana. Usalama bado unaonekana kama lango, na kusogeza kushoto ni matamanio badala ya halisi.

**Ngazi ya 3: Kusawazisha.** Mabingwa wa usalama wameingizwa katika kila timu. Uundaji wa vitisho ni wa kawaida kwa huduma mpya, umepangwa kwa ngazi dhidi ya uainishaji wa CIA, na mzunguko salama wa uendelezaji umeandikwa na kutekelezwa shirika zima. Kuweka kipaumbele kwa hatari kunaongoza kazi, viwango salama vya uandishi wa msimbo na ukaguzi wa bomba ndiyo njia iliyopakwa lami ya chaguo-msingi, na mapitio ya baada ya tukio yasiyo na lawama ni kawaida.

**Ngazi ya 4: Kusimamia.** Matokeo ya usalama yanapimwa na kudhibitiwa dhidi ya vipimo vya msingi. Shirika linafuatilia muda wa wastani wa kurekebisha matokeo makali, ufikiaji wa kielelezo cha vitisho, sehemu ya matukio yanayonaswa kabla ya uzalishaji, na viwango vya kuripoti karibu-makosa, vilivyogawanywa kwa kila timu. Mamlaka ya mabingwa kusimamisha toleo yamefafanuliwa na kutumiwa kweli. Maamuzi ya hatari yanapimwa kama uwezekano mara athari, kurekodiwa, na kupitiwa kwa mzunguko thabiti, kwa hiyo mapengo ya vidhibiti yanajitokeza kama data badala ya mshangao.

**Ngazi ya 5: Kuratibu.** Usalama ni kazi ya kila mtu kweli na umeunganishwa na utoaji, hatari, na upangaji wa biashara. Uundaji wa vitisho na usanifu salama ni wa kawaida na mwepesi, na kanuni za uaminifu-sifuri zimetimia kwa kiasi kikubwa. Vipimo vinaendesha uboreshaji endelevu, shirika linajifunza kutoka karibu-makosa kuvuka timu, na vidhibiti hujirekebisha kiotomatiki picha ya tishio na usanifu vinapobadilika.

## Mawazo ya kujadili

1. Mnapimaje kama utamaduni wa usalama unaboreka kweli, zaidi ya kuhesabu kukamilisha mafunzo?
2. Mpaka sahihi uko wapi kati ya kile mabingwa wa usalama wanashughulikia na kile timu kuu inamiliki?
3. Mnaweka vipi uundaji wa vitisho wenye manufaa bila kuuacha kuwa kuweka alama kwa urasimu?
4. Je, usanifu kamili wa uaminifu-sifuri unawezekana kwa eneo lenu la urithi, na kama sivyo, ni sehemu ndogo ipi ya kiutendaji?
5. Kazi ya usalama inapaswa kuwekewa kipaumbele vipi dhidi ya utoaji wa vipengele vyote vikishindania wahandisi walewale?
6. Vichocheo gani hubadilisha tabia ya mhandisi kuelekea umiliki wa usalama kweli?

## Mambo muhimu ya kukumbuka

- Usalama ni sifa ya kiutamaduni ya mashirika makubwa, si kazi iliyokabidhiwa timu moja.
- Mabingwa wa usalama hupanua utaalamu na umiliki kuvuka uhandisi.
- Uundaji wa vitisho (STRIDE, PASTA, miti ya shambulio) hufichua dosari za usanifu mapema na kwa bei nafuu.
- Mzunguko salama wa uendelezaji na mtazamo wa kusogeza kushoto hunasa kasoro zinapogharimu kidogo zaidi.
- Ulinzi wa kina, upendeleo mdogo, na uaminifu-sifuri ndio kanuni za msingi za usanifu.
- Utatu wa CIA na kuweka kipaumbele kwa hatari huelekeza juhudi adimu mahali panapojalisha zaidi.
- Gharama ya kujenga utamaduni wa usalama ni ndogo zaidi sana kuliko gharama ya uvunjaji unaozuia.

## Marejeo na usomaji zaidi

- Adam Shostack, *Threat Modeling: Designing for Security*
- Ross Anderson, *Security Engineering: A Guide to Building Dependable Distributed Systems*
- Michael Howard and Steve Lipner, *The Security Development Lifecycle*
- Betsy Beyer et al. (Google), *Building Secure and Reliable Systems*
- National Institute of Standards and Technology, *SP 800-207: Zero Trust Architecture*
- National Institute of Standards and Technology, *Secure Software Development Framework (SSDF), SP 800-218*
- OWASP, *Threat Modeling* and *Security Champions* guidance
