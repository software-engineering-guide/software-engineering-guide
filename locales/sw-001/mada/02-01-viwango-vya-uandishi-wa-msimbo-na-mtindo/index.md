# 2.1 Viwango vya uandishi wa msimbo na mtindo

## Muhtasari na msukumo

Viwango vya uandishi wa msimbo ni desturi za pamoja zinazoruhusu watu wengi kuandika msimbo kana kwamba mwandishi mmoja makini aliuandika. Vinashughulikia majina, muundo, mpangilio wa mafaili, milio ya lugha, ushughulikiaji wa makosa, na mifumo ya uandishi ambayo timu inapendelea. Katika timu ndogo, ladha ya mtu binafsi inaweza kushinda siku. Katika timu kubwa (mamia au maelfu ya wahandisi, wakandarasi wengi, mauzo ya juu ya wafanyakazi), kutokuwa na uthabiti kunakuwa ushuru unaolipa kwa kila usomaji, kila mapitio, na kila utambulisho. Viwango hubadilisha mabishano mengi madogo ya mtindo kuwa uamuzi wa mara moja ambao mashine kisha inakutekelezea.

Kwa mashirika makubwa dau ni madhubuti. Msimbo husomwa mara nyingi zaidi sana kuliko unavyoandikwa. Katika mazingira ya mashirika makubwa na ya serikali, mstari wa msimbo unaweza kusomwa na wakaguzi, wapitiaji wa usalama, na wadumishaji miaka baada ya mwandishi wake kuondoka. Mtindo thabiti hupunguza gharama ya kiakili ya usomaji huo, hupunguza eneo la kasoro, na hufanya uchambuzi wa kiotomatiki uwe wa kuaminika kuvuka [linters](https://en.wikipedia.org/wiki/Lint_(software)) (zana zinazoashiria kiotomatiki kasoro zinazowezekana na ukiukaji wa mtindo), vichanganuzi vya usalama, na zana za [urekebishaji wa muundo](https://en.wikipedia.org/wiki/Code_refactoring). Pale udhibiti unapotumika, kama katika huduma za kifedha, huduma za afya, ulinzi, na mifumo ya sekta ya umma, viwango pia ni sehemu ya ushahidi kwamba msimbo unadumishika na unadhibitiwa.

Njia ya kisasa ni kuchukulia mtindo kama jambo lililotatuliwa, la kiotomatiki badala ya suala la busara ya binadamu inayoendelea. Vipanga muundo na linters huendeshwa kwenye kihariri, kwenye ndoano za kabla ya commit, na kwenye [uunganishaji endelevu](https://en.wikipedia.org/wiki/Continuous_integration) (CI), mchakato wa kiotomatiki wa kujenga-na-kujaribu unaoendeshwa kwa kila badiliko. Mashine hutekeleza mtindo, ili uweze kutumia umakini wako wa mapitio kwa usanifu na usahihi. Lengo si usawa kwa ajili yake. Ni kuondoa msuguano: unapaswa kuweza kuhama kati ya huduma na timu bila kujifunza upya misingi.

## Kanuni kuu

- Uthabiti unashinda upendeleo wa mtu binafsi; mtindo mmoja uliokubaliwa, unaotumika kila mahali, una thamani zaidi ya mtindo "bora" unaotumika bila usawa.
- Otomatisha utekelezaji. Vipanga muundo na linters ndio chanzo cha ukweli, si maoni ya mapitio ya msimbo kuhusu nafasi.
- Boresha kwa msomaji na mdumishaji, si mwandishi wa awali.
- Pendelea desturi ambazo jamii pana ya lugha tayari inazitumia kuliko kanuni maalumu za nyumbani.
- Fanya kiwango kiwe rahisi kupokea: toa usanidi wa pamoja, violezo, na zana badala ya PDF ambayo hakuna anayeisoma.
- Kanuni za mtindo zinapaswa kuwa chache, zinazoweza kutetewa, na zisizo na utata; kila kanuni ina utaratibu wa utekelezaji au ni pendekezo tu.
- Kutaja majina ndio uamuzi wa kusomeka wenye kiegemeo cha juu zaidi na unastahili mwongozo wazi.

## Mapendekezo

### Pokea mwongozo wa mtindo wa msingi kwa kila lugha

Kwa kila lugha unayotumia, pokea mwongozo wa mtindo unaotambulika sana kama msingi (kwa mfano, mwongozo wa jamii au muuzaji kwa lugha hiyo) na uandike tofauti tu ambazo shirika lako linahitaji. Usivumbue mtindo wa nyumbani kutoka mwanzo. Chapisha uchaguzi wako mahali pa kati, panapopatikana, na uuweke katika matoleo kama msimbo.

### Fanya vipanga muundo kuwa chaguo-msingi lisilojadiliwa

Tumia kipanga muundo cha kiotomatiki chenye msimamo kwa kila lugha inayokuwa nacho, kikiwa na usanidi mmoja wa pamoja ulioingizwa kwenye hazina. Muundo haupaswi kuibuka kamwe kwenye mapitio, kwa sababu unatumika kiotomatiki wakati wa kuhifadhi na kuthibitishwa kwenye CI. Pale lugha inapokosa kipanga muundo imara, chagua usanidi mmoja wa linter na ushughulikie kwa namna hiyo hiyo.

### Endesha linters kama malango yanayotekelezwa, si ushauri

Sanidi linters kwa seti ya kanuni iliyokubaliwa, shindwa ujenzi kwa ukiukaji, na uweke seti ya kanuni katika [udhibiti wa matoleo](https://en.wikipedia.org/wiki/Version_control) ili mabadiliko yapitie mapitio. Tenganisha kanuni zinazoweza kurekebishwa kiotomatiki (zitumie kiotomatiki) na kanuni zinazohitaji busara ya binadamu (ziweke bendera na uzuie). Anzisha kanuni mpya katika hali ya "onyo," futa mrundikano, kisha uzipandishe hadi "kosa."

### Tekeleza katika tabaka nyingi

Toa muunganisho wa kihariri kwa maoni ya papo hapo, ndoano za kabla ya commit kwa utekelezaji wa mahali, na ukaguzi wa CI kama lango lenye mamlaka. Kadiri unavyonasa ukiukaji mapema, ndivyo unavyokuwa nafuu zaidi. CI lazima iwe kinga ya mwisho, kwa sababu ndoano za mahali zinaweza kuepukwa.

### Toa kanuni wazi kwa majina

Sawazisha desturi za herufi kwa kila lugha, hitaji majina yanayofichua nia, piga marufuku vifupisho vinavyopotosha, na ufafanue desturi za booleani, mikusanyiko, vipimo, na shughuli zisizo za wakati mmoja. Andika msamiati wako wa eneo katika faharasa ya pamoja ili dhana ileile iwe na jina lilelile kila mahali.

### Simamia uthabiti wa lugha nyingi kwa makusudi

Katika msimbo unaovuka lugha kadhaa, lenga dhana thabiti (mifumo ya ushughulikiaji wa makosa, muundo wa kumbukumbu, mpangilio wa mradi) hata pale sintaksia inapotofautiana. Toa usanidi wa kila lugha kutoka hazina ya kati ili huduma mpya irithi viwango kiotomatiki kupitia violezo au uanzishaji.

### Weka milio ya lugha na mifumo katika kanuni

Nenda zaidi ya muundo. Andika milio ya lugha unayopendelea, kama jinsi ya kushughulikia makosa, jinsi ya kupanga moduli, na lini kutumia vighairi dhidi ya aina za matokeo, pamoja na mifumo ya uandishi ambayo timu zako zinapendelea. Hapa ndipo usomekaji halisi na uwezo wa kudumishwa unapoishi.

## Mabadilishano: faida na hasara

| Mbinu | Faida | Hasara |
|---|---|---|
| Kipanga muundo kikali cha kiotomatiki, hakuna usanidi | Humaliza mabishano yote ya muundo; uthabiti wa papo hapo; utambulisho rahisi sana | Baadhi ya chaguo zisizopendwa haziwezi kujadiliwa; tofauti kubwa ya awali inapotumika kwa mara ya kwanza |
| Linter inayosanidika yenye kanuni za nyumbani | Inalingana na mahitaji ya shirika; inaweza kuweka kanuni halisi za kuzuia kasoro | Kuteleza kwa usanidi; mabishano ya kanuni ndogo; mzigo wa matengenezo |
| Kiwango cha jamii kilichopokelewa kwa jumla | Kinajulikana kwa waajiriwa wapya; mfumo imara wa zana; matengenezo ya chini | Huenda kisifae vikwazo maalumu vya shirika; kanuni zisizofaa mara kwa mara |
| Kiwango maalumu cha ndani | Kinafaa shirika hasa | Ghali kuandika na kudumisha; hakijulikani kwa waajiriwa; zana dhaifu |
| Uhuru wa kila timu | Ari ya juu ya mahali; mahususi kwa muktadha | Mgawanyiko; uhamaji wa kuvuka timu wenye maumivu; zana zisizo thabiti |

Chaguo-msingi zinazotekelezwa hubadilishana uhuru kidogo wa mtu binafsi kwa faida kubwa za pamoja: msuguano mdogo wa mapitio, utambulisho wa haraka, na uendeshaji wa kiotomatiki wa kuaminika. Hatari kuu ni kuhandisi kiwango kupita kiasi hadi mamia ya kanuni zinazopunguza kasi ya kila mtu bila kuzuia kasoro halisi. Weka seti ya kanuni ndogo na yenye msingi wa ushahidi, na uelekee kupokea kiwango kilichopo ili matengenezo yabaki nafuu.

## Maswali ya kujadili na timu yako

1. **Ni kanuni zipi za linter zinapaswa kushindwa ujenzi, na unazipandishaje kutoka onyo hadi kosa bila kusimamisha kila mtu?** Sura hii inabishana kwamba kila kanuni inahitaji utaratibu wa utekelezaji, na kwamba kanuni mpya zinapaswa kutua katika hali ya onyo, kufutwa mrundikano wao, kisha kugeuka kuwa kosa. Katika timu kubwa, kugeuza kanuni kuwa kosa dhidi ya msimbo mchafu huzuia mamia ya mabadiliko yasiyohusiana usiku mmoja. Leta ushahidi mgumu kwenye mkutano: idadi ya sasa ya ukiukaji kwa kila kanuni mgombea, na kama inaweza kurekebishwa kiotomatiki au inahitaji busara ya binadamu. Katika mazingira ya mashirika makubwa na ya serikali mstari wa kupita/kushindwa pia unalisha malango ya ukaguzi, kwa hiyo seti ya kanuni isiyo wazi inadhoofisha hadithi yako ya uzingatiaji. Amua usambazaji wa hatua: rekebisha kiotomatiki unachoweza, wekea bajeti usafishaji, kisha funga lango.

2. **Unapotumia kipanga muundo kwa mara ya kwanza kwenye msimbo wako wa zamani, utazuiaje urekebishaji huo usiharibu git blame na kuzamisha mapitio?** Jedwali la mabadilishano linaonya kuhusu tofauti kubwa ya awali, na sehemu ya mifumo mibaya inataja kuchanganya commit za kupanga muundo na mabadiliko ya mantiki. Kupanga upya kwa kufagia kunaandika upya maelfu ya mistari na kufanya blame ielekeze kwenye urekebishaji badala ya mwandishi halisi, jambo linaloumiza yeyote anayetatua miaka baadaye. Fanya urekebishaji kama commit moja iliyotengwa, iliyowekewa lebo wazi, na uisajili katika faili la kupuuza blame ili historia ibaki yenye manufaa. Kwa wakaguzi wanaofuatilia nani alibadilisha nini, kutengwa huko ndiko tofauti kati ya ushahidi safi na kelele. Kubaliana mfuatano kabla ya kugusa msimbo, si baada.

3. **Nani anamiliki faharasa yenu ya majina na msamiati wa eneo, na neno jipya linaongezwaje?** Sura inaita kutaja majina uamuzi wa usomekaji wenye kiegemeo cha juu zaidi na inakuomba uandike msamiati wa eneo katika faharasa ya pamoja. Bila mmiliki aliyetajwa, dhana ileile hupata majina matatu tofauti kuvuka timu, na zana za uchambuzi tuli na utafutaji hupoteza kuaminika. Leta mifano ya dhana ambazo tayari zina majina yanayopingana katika msimbo wako kama ishara madhubuti. Kabidhi mmiliki mmoja na njia nyepesi ya mapendekezo, ili kuongeza au kubadilisha jina la neno kiwe badiliko dogo, lililopitiwa badala ya mabishano katika kila ombi la kuvuta. Jibu linabadilisha utambulisho: mwajiriwa mpya anasoma faharasa moja badala ya kuchambua nia kutoka msimbo usio thabiti.

4. **Kwa kila lugha, je, mnapokea mwongozo wa mtindo wa jamii au muuzaji unaotambulika kwa jumla, na tofauti za nyumbani zinahalalishwa wapi kweli?** Sura hii inabishana kwamba unapaswa kuchukua kiwango kilichopo kama msingi na kuandika tofauti tu ambazo shirika lako linahitaji, kwa sababu kiwango maalumu ni ghali kuandika na hakijulikani kwa waajiriwa. Mvuto unaoshindana ni halisi: kikwazo cha ndani (kanuni ya usalama, mfumo wa zamani, agizo la ufikivu) wakati mwingine kinagongana kweli na chaguo-msingi la jamii, na kila tofauti unayoibakiza ni kanuni ambayo sasa unaimiliki na kuidumisha milele. Leta orodha ya tofauti zilizopendekezwa kwenye mkutano, kila moja ikiwa na kikwazo madhubuti kinachoichochea, na uwe tayari kukata tofauti yoyote ambayo ni ladha tu. Katika mazingira ya mashirika makubwa na ya serikali, msingi unaolingana na jamii pana ya lugha pia unamaanisha wakandarasi na wasambazaji wapya wanafika wakiwa tayari wanaifahamu, jambo linalofupisha utambulisho na kuimarisha ushahidi wa uwezo wa kudumishwa ambao wakaguzi wanautafuta.

5. **Katika msimbo wa lugha nyingi, ni desturi zipi ni za wote kweli na zipi zinabaki za lugha ya mahali, na unazuiaje usanidi wa kila hazina kuteleza?** Sura inaomba dhana thabiti (ushughulikiaji wa makosa, muundo wa kumbukumbu, mpangilio wa mradi) kuvuka lugha hata pale sintaksia inapotofautiana, na usanidi wa kila lugha unaotolewa kutoka hazina ya kati ili huduma mpya zirithi viwango kiotomatiki. Mvutano ni kwamba kulazimisha milio ya lugha moja kwenye nyingine huzalisha msimbo wa ajabu, usio wa asili, huku kuiacha kila timu kugawanya usanidi wake kunaishia "kiwango" kutokumaanisha chochote. Leta orodha ya usanidi wenu wa sasa wa linter na kipanga muundo kwa kila hazina na ulinganisho unaoonyesha jinsi ulivyoshatofautiana, kama ishara madhubuti. Kwa shirika kubwa linaloendesha makumi ya huduma, amua utaratibu wa usambazaji (violezo, uanzishaji, kifurushi cha usanidi cha pamoja) ili mabadiliko ya kanuni yaenee mara moja badala ya kunakiliwa kwa mkono kwenye kila hazina.

6. **Lini kuzima kanuni ni halali, nani anapitia ukandamizaji, na unazuiaje kuzima kwa jumla kusiondoe kiini cha kiwango?** Sehemu ya mifumo mibaya inaashiria ukandamizaji ulioenea ndani ya mstari kama ishara kwamba kanuni ni mbaya au timu imekata tamaa, hata hivyo sera ngumu ya hakuna-vighairi huwasukuma watu kuandika msimbo mbaya zaidi ili kutimiza linter tu. Kubaliana njia nyepesi: ukandamizaji lazima ubebe sababu, ukae katika wigo mdogo iwezekanavyo, na uonekane kwenye mapitio badala ya kuzikwa kwenye faili la kupuuza la jumla. Leta idadi ya sasa ya ukandamizaji kwa kila kanuni na kwa kila hazina, kwa sababu kanuni inayokandamizwa mamia ya mara inakuambia kitu kuhusu kanuni, si msimbo. Katika kazi inayodhibitiwa na ya sekta ya umma, ukandamizaji wa jumla usioelezwa unadhoofisha moja kwa moja hadithi ya ukaguzi, kwa kuwa bomba haliwezi tena kuonyesha kwamba msimbo uliounganishwa ulipita malango yaliyokubaliwa kweli.

## Mtazamo wa sekta

**Kampuni changa.** Kasi inashinda, kwa hiyo pokea chaguo-msingi za kipanga muundo na linter cha jamii kwa lugha yako moja siku ya kwanza na uviunganishe kwenye ndoano ya kabla ya commit na CI kabla mhandisi wa pili hajafika. Usiandike mtindo wa nyumbani usio na muda wa kuudumisha: usanidi unaosafirishwa kwenye hazina ndio kiwango chote. Unapoongeza lugha ya pili, fikia mwongozo wa kisheria wa lugha hiyo badala ya kuvumbua desturi kutoka mwanzo.

**Biashara ndogo.** Bila mtaalamu maalumu wa zana na bajeti finyu, tegemea kabisa kipanga muundo cha bure chenye msimamo kinachokuja na au kando ya lugha yako, na ukubali chaguo-msingi zake badala ya kuzirekebisha. Hii ni kesi wazi ya kununua-badala-ya-kujenga: kudumisha seti maalumu ya kanuni kunagharimu muda usio nao, huku kipanga muundo kilichotengenezwa tayari hakigharimu chochote na kinamaliza mabishano ya mtindo mara moja. Weka usanidi kwenye hazina ili mkandarasi mmoja utakayemwajiri mwaka ujao airithi bila mazungumzo.

**Biashara kubwa.** Kwa ukubwa kazi ni utawala kuvuka timu nyingi: hazina ya kati ya viwango vya uhandisi inayoshikilia usanidi wa pamoja wa kipanga muundo na linter kwa kila lugha, huduma mpya zinazozalishwa kutoka violezo vinavyovuta usanidi huo, na malango ya CI yanayozuia uunganishaji usiozingatia. Weka seti ya kanuni katika matoleo kama msimbo na upitishe mabadiliko kupitia mapitio ya mara kwa mara ili viwango vibadilike kwa makusudi badala ya kuteleza. Faida ni wahandisi kuhama kati ya timu kwenda kwenye msimbo unaojulikana, na zana za kiotomatiki zinazozalisha ishara ya kuaminika kwa sababu kila hazina ni thabiti.

**Serikali.** Ununuzi na uwajibikaji huunda uchaguzi: amuru mtindo mahususi na seti ya kanuni za usalama kama sehemu ya mahitaji ya mamlaka ya kuendesha, na ufanye bomba litoe ripoti inayoonyesha kila badiliko lililounganishwa lilipita malango yaliyokubaliwa kama ushahidi wa ukaguzi. Kwa sababu kipanga muundo kinatumika kiotomatiki, msimbo kutoka kwa wasambazaji na wakandarasi wengi unaonekana thabiti, jambo linalolinda kazi ya matengenezo ya umma muda mrefu baada ya mikataba kuisha. Pendelea misingi ya jamii inayotambulika kuliko kanuni maalumu ili kiwango kiwe cha uwazi na msambazaji yeyote wa baadaye aweze kukipokea bila kufungwa kwa umiliki.

## Mifano

**Kampuni changa.** Kampuni changa ya watu wanne inapokea chaguo-msingi za kipanga muundo na linter cha jamii kwa lugha yake moja siku ya kwanza, ikiviunganisha kwenye ndoano ya kabla ya commit na CI ili hakuna anayebishana kuhusu nafasi kwenye mapitio. Kwa sababu usanidi unasafirishwa ndani ya hazina, waajiriwa wa tano na wa sita wanairithi kiotomatiki na hawaoni maoni ya muundo kamwe. Timu inapoongeza lugha ya pili baadaye, inafikia mwongozo wa kawaida wa lugha hiyo badala ya kuvumbua mtindo wa nyumbani usio na muda wa kuudumisha.

**Biashara kubwa.** Benki kubwa inaendesha huduma katika Java, Python, na TypeScript kuvuka makumi ya timu. Inachapisha hazina ya kati ya "viwango vya uhandisi" inayoshikilia usanidi wa pamoja wa kipanga muundo na linter kwa kila lugha. Huduma mpya zinazalishwa kutoka kiolezo kinachovuta usanidi huo, kwa hiyo kila hazina inaanza ikizingatia. CI inazuia uunganishaji kwa ukiukaji wowote, na mapitio ya kila robo yanatawala mabadiliko ya kanuni. Muda wa utambulisho kwa wahandisi wanaohama kati ya timu unapungua kwa wazi, kwa sababu kila hazina inaonekana inayojulikana.

**Serikali.** Wakala wa sekta ya umma unaoboresha mfumo wa zamani unaamuru seti ya kanuni za linting za ufikivu na usalama kama sehemu ya mahitaji yake ya mamlaka ya kuendesha (ATO), idhini rasmi inayohitajika kuendesha mfumo katika uzalishaji. Uzingatiaji wa mtindo unakuwa sehemu ya ushahidi wa ukaguzi: bomba linazalisha ripoti inayoonyesha msimbo wote uliounganishwa ulipita malango ya [uchambuzi tuli](https://en.wikipedia.org/wiki/Static_program_analysis) yaliyokubaliwa. Kwa sababu kipanga muundo kinatumika kiotomatiki, wakandarasi kutoka wasambazaji wengi wanazalisha msimbo unaoonekana thabiti, jambo linalofanya kazi ya matengenezo ya muda mrefu ya serikali iwe rahisi mikataba inapoisha.

## Kesi ya biashara: sababu, ROI, na TCO

Gharama ya kupokea viwango hasa ni ya mara moja: kuchagua miongozo, kuunganisha zana, na kutumia commit moja kubwa ya awali ya kupanga muundo. Gharama inayojirudia ni ndogo, kwa sababu utekelezaji ni wa kiotomatiki. Gharama ya *kutopokea* viwango inajirudia na kujumlika: kila mapitio hutumia dakika kwa mtindo, kila utambulisho ni wa polepole, zana za uchambuzi tuli huzalisha kelele, na msimbo usio thabiti huficha kasoro. Kuvuka shirika kubwa, dakika hizo hujumlika kuwa hasara za sawa-na-wafanyakazi-wa-muda-kamili.

Mapato yanaonekana kama kupungua kwa ucheleweshaji wa mapitio, maoni machache ya mapitio yanayohusiana na mtindo, utambulisho wa haraka, na ishara ya juu zaidi kutoka zana za kiotomatiki. Katika mazingira yanayodhibitiwa kuna mapato zaidi katika utayari wa ukaguzi: udhibiti unaoweza kuonyeshwa, unaotekelezwa hupunguza juhudi na hatari ya mapitio ya uzingatiaji. Kujenga hoja kwa uongozi, weka viwango kama kiegemeo cha gharama ya chini, cha kiwango cha juu juu ya tija ya wasanidi na msimamo wa ukaguzi, na uweke nambari kwenye gharama ya sasa ya kutokuwa na uthabiti ukitumia uchambuzi wa maoni ya mapitio na data ya utafiti wa utambulisho.

## Mifumo mibaya na mitego

- **Mtindo unabishaniwa kwenye mapitio ya msimbo:** ishara kwamba utekelezaji si wa kiotomatiki; hamisha kanuni kwenye zana.
- **Waraka wa viwango usiosomwa:** ukurasa wa wiki bila utekelezaji ni mapambo; kila kanuni inahitaji utaratibu.
- **Kuenea kwa kanuni:** mamia ya kanuni ndogo zinazopunguza kasi ya kazi bila kuzuia kasoro.
- **Kuteleza kwa usanidi:** kila hazina inagawanya usanidi wake wa linter hadi "kiwango" kinakuwa hakina maana.
- **Kupanga muundo hazina nzima katikati ya kazi ya vipengele:** kuchanganya commit za muundo na mabadiliko ya mantiki huharibu mapitio na blame; fanya urekebishaji mkubwa katika commit zilizotengwa, zenye lebo wazi.
- **Kupuuza linter kwa ukandamizaji wa jumla:** kuzima kulikoenea ndani ya mstari huashiria kanuni isiyo sahihi au timu iliyokata tamaa.
- **Viwango bila umiliki:** bila mmiliki wazi, kanuni hazibadiliki kamwe na huoza.

## Kielelezo cha ukomavu

- **Ngazi ya 1, Kuanzisha:** Mtindo ni wa kila mwandishi na wa kuitikia; hakuna usanidi wa pamoja; muundo unabishaniwa kwenye mapitio na kuamuliwa na yeyote anayejali zaidi siku hiyo.
- **Ngazi ya 2, Kuendeleza:** Timu binafsi hupokea kipanga muundo na linter, lakini usanidi na seti za kanuni hutofautiana timu hadi timu na hazina hadi hazina, kwa hiyo uthabiti unaishia mpaka wa kila timu.
- **Ngazi ya 3, Kusawazisha:** Usanidi wa kati wa pamoja kwa kila lugha umeandikwa na kutekelezwa shirika zima; CI inazuia uunganishaji usiozingatia; hazina mpya zinarithi viwango kiotomatiki kupitia violezo au uanzishaji.
- **Ngazi ya 4, Kusimamia:** Kiwango kinapimwa na kudhibitiwa kwa data: viwango vya ukiukaji, idadi ya ukandamizaji, maoni ya mapitio yanayohusiana na mtindo, na muda wa utambulisho vinafuatiliwa dhidi ya vipimo vya msingi, na mabadiliko ya kanuni hupandishwa au kustaafishwa kwa ushahidi huo badala ya maoni.
- **Ngazi ya 5, Kuratibu:** Viwango vinaboreshwa kila wakati na kuunganishwa kuvuka shirika; milio ya lugha nyingi na msamiati wa eneo vimeandikwa na kutekelezwa, utekelezaji hauna msuguano karibu kabisa, na seti ya kanuni hubadilika lugha, zana, na mahitaji ya shirika yanapohama.

## Mawazo ya kujadili

- Mstari uko wapi kati ya kanuni inayotekelezwa na mwongozo ulioandikwa unaoamini busara ya mhandisi?
- Shirika linapaswa kushughulikiaje kanuni ya jamii inayopendwa inayogongana na kikwazo halisi cha ndani?
- Nani anamiliki viwango, na mabadiliko ya kanuni yanapendekezwaje, kujadiliwa, na kutolewa bila usumbufu?
- Katika msimbo wa lugha nyingi, ni desturi zipi zinapaswa kuwa za wote kweli na zipi zibaki za lugha ya mahali?
- Unarekebishaje viwango kwenye msimbo mkubwa wa zamani bila urekebishaji mkubwa wa mara moja unaosumbua?
- Zana zinazosaidiwa na AI zinapaswa kuwa na jukumu gani katika kupendekeza au kutekeleza milio ya lugha zaidi ya muundo wa kimitambo?

## Mambo muhimu ya kukumbuka

- Chukulia mtindo kama tatizo la kiotomatiki, lililotatuliwa ili binadamu wapitie usanifu na usahihi.
- Pokea viwango vya jamii vilivyopo na uandike tofauti tu.
- Tekeleza kwenye kihariri, kabla ya commit, na tabaka za CI, ukiwa na CI kama lango lenye mamlaka.
- Weka seti ya kanuni ndogo, inayoweza kutetewa, na inayotawaliwa kwa kati.
- Majina na milio ya lugha, si nafasi, ndipo usomekaji unaposhindwa kweli.

## Marejeo na usomaji zaidi

- Robert C. Martin, *Clean Code: A Handbook of Agile Software Craftsmanship*
- Andrew Hunt and David Thomas, *The Pragmatic Programmer*
- Steve McConnell, *Code Complete*
- Dustin Boswell and Trevor Foucher, *The Art of Readable Code*
- Kevlin Henney (ed.), *97 Things Every Programmer Should Know*
- Google, *Google Engineering Practices* and language style guides (as reference exemplars)
