# 5.5 Uandaaji wa kimataifa na ulokalishaji

## Muhtasari na msukumo

[Uandaaji wa kimataifa](https://en.wikipedia.org/wiki/Internationalization_and_localization) (i18n) ni kazi ya kihandisi ya kujenga programu ili iweze kurekebishwa kwa lugha, eneo, na utamaduni wowote bila kubadilisha msimbo. Ulokalishaji (l10n) ni kazi inayofuata: kurekebisha bidhaa kwa lokali mahususi kwa kutafsiri maandishi, kuumba tarehe na namba, kurekebisha mpangilio, na kuzingatia matarajio ya kiutamaduni. Hivi viwili ni tofauti. Uandaaji wa kimataifa hufanywa mara moja, kwenye usanifu. Ulokalishaji hufanywa mara nyingi, kwenye maudhui. Pata usanifu sawa mapema na kila ulokalishaji ni nafuu. Ukikosea na kila mmoja unakuwa kurudisha kwa maumivu, kunakokabiliwa na makosa.

Kwa timu kubwa, i18n ni uamuzi wa msingi wa usanifu. Unagusa kila safu: uhifadhi wa data, ushughulikiaji wa mifuatano ya herufi, mpangilio, na mabomba ya maudhui. Usipoanzisha mapema na kuutekeleza kupitia maktaba za pamoja na kanuni za lint, timu hupachika mifuatano ya Kiingereza, kuunganisha vipande vilivyotafsiriwa, na kudhania maandishi ya Kilatini. Deni hilo lazima lifunguliwe kabla bidhaa kuingia soko jipya lolote. Mfumo wa pamoja wa i18n na mtiririko wa ulokalishaji huruhusu timu kadhaa kusafirisha bidhaa katika lugha nyingi bila kila moja kubuni upya mabomba.

Umuhimu wa mashirika makubwa na serikali ni wa moja kwa moja. Mashirika ya kimataifa lazima yahudumie wateja na wafanyakazi kuvuka nchi, lugha, na tawala za udhibiti. Serikali lazima zihudumie idadi ya watu wenye lugha mbalimbali. Nchi nyingi ni za lugha nyingi rasmi, na nyingi zinahitajika kisheria kutoa huduma katika lugha kadhaa, ikijumuisha maandishi ya [kulia-kwenda-kushoto](https://en.wikipedia.org/wiki/Bidirectional_text) na lugha za asili au za walio wachache. Kwa huduma za umma, ufikiaji wa lugha ni suala la usawa na la kisheria: raia asiyeweza kusoma lugha pekee inayopatikana kwa kweli amenyimwa huduma.

## Kanuni kuu

- Andaa usanifu kimataifa mara moja; lokalisha maudhui mara nyingi.
- Usipachike kamwe maandishi yanayomkabili mtumiaji; peleka mifuatano yote kwenye rasilimali zinazosimamiwa.
- Tumia [Unicode](https://en.wikipedia.org/wiki/Unicode) (UTF-8) kila mahali; dhania maandishi yanaweza kuwa katika hati yoyote.
- Usiunganishe kamwe vipande vilivyotafsiriwa; sarufi na mpangilio wa maneno hutofautiana kwa lugha.
- Panga kwa upanuzi wa maandishi, hati za kulia-kwenda-kushoto, na kanuni changamano za wingi na jinsia.
- Umba tarehe, namba, sarafu, na majina kulingana na lokali, si msimbo.
- Tenganisha maudhui yanayotafsirika na msimbo ili watafsiri wasiguse chanzo kamwe.
- Ulokalishaji ni wa kiutamaduni, si wa kilugha tu: rangi, picha, na mifano vinajalisha.

## Mapendekezo

### Jenga usanifu imara wa uandaaji wa kimataifa

Hifadhi na uchakate maandishi yote kama Unicode (UTF-8) mwanzo hadi mwisho (hifadhidata, API, na UI) ili hati yoyote iweze kuwakilishwa. Peleka kila mfuatano unaomkabili mtumiaji kwenye faili za rasilimali au katalogi ya ujumbe iliyofungwa kwa kitambulisho, kamwe usiopachikwa kwenye msimbo au alama. Wakilisha lokali kama lugha pamoja na eneo (na hati inapohitajika) ili uweze kutofautisha, kwa mfano, lahaja za lugha moja kuvuka nchi. Weka mantiki ya uumbaji kwenye maktaba ya uandaaji wa kimataifa iliyojaribiwa vizuri badala ya kuandika kwa mkono uumbaji wa tarehe, namba, na sarafu. Hifadhi data katika maumbo yasiyoegemea upande wowote, yasiyo na utata (mihuri ya muda ya UTC, misimbo ya ISO ya nchi na sarafu, vipimo vya msingi) na uumbe tu kwenye safu ya uwasilishaji.

### Shughulikia ugumu wa lugha ipasavyo

Usidhanie urefu wa maandishi; ruhusu nafasi pana kwa sababu tafsiri mara nyingi ni ndefu zaidi kuliko Kiingereza, na sanifu mipangilio inayojipanga upya badala ya kukata au kuingiliana. Unga mkono hati za pande mbili (kulia-kwenda-kushoto) kwa kutumia sifa za mpangilio za kimantiki badala ya za kimwili na kuakisi kiolesura pale inapofaa. Tumia kanuni za wingi za lokali kupitia maktaba yako ya i18n (lugha zina kuanzia umbo moja hadi sita za wingi) badala ya mantiki ya kijinga ya umoja/wingi. Shughulikia jinsia na upatanisho wa kisarufi pale lugha inapohitaji. Usijenge kamwe sentensi kwa kuunganisha; tumia violezo kamili vya ujumbe vyenye vigezo ili watafsiri wadhibiti mpangilio wa maneno.

### Anzisha mtiririko wa ulokalishaji na usimamizi wa tafsiri

Chukulia ulokalishaji kama bomba endelevu, si kundi la kabla ya uzinduzi. Toa mifuatano kiotomatiki, uisukume kwenye [mfumo wa usimamizi wa tafsiri](https://en.wikipedia.org/wiki/Translation_management_system), na uvute tafsiri zilizokamilika, ikiwezekana ikiunganishwa na CI ili mifuatano mipya iwekewe alama na matoleo yaliyolokalishwa yabaki sawia. Wape watafsiri muktadha: picha za skrini, maelezo, mipaka ya herufi, na faharasa na mwongozo wa mtindo kwa kila lugha ili kuweka istilahi na toni thabiti. Tumia [kumbukumbu ya tafsiri](https://en.wikipedia.org/wiki/Translation_memory) kutumia tena kazi ya awali na kupunguza gharama. Amua kwa makusudi pale [tafsiri ya mashine](https://en.wikipedia.org/wiki/Machine_translation) inakubalika (maudhui ya hatari ndogo, kiasi kikubwa) na pale tafsiri ya binadamu na mapitio yanahitajika (kisheria, kimatibabu, usalama, muhimu kwa chapa). [Fanya pseudo-ulokalishaji](https://en.wikipedia.org/wiki/Pseudolocalization) mapema, ukibadilisha mifuatano na vishikilia nafasi vilivyorefushwa, vyenye alama za herufi, kunasa mifuatano iliyopachikwa, kukata, na hitilafu za usimbaji kabla tafsiri halisi haijaanza.

### Lokalisha miundo, utamaduni, na maudhui, si maneno tu

Umba tarehe, nyakati, namba, sarafu, anwani, namba za simu, na majina kwa kila lokali, ukiheshimu mikataba ya mahali (mpangilio wa tarehe, vitenganishi vya desimali na vikundi, nafasi ya sarafu, mpangilio wa majina). Rekebisha picha, ikoni, rangi, mifano, na sitiari kwa maana ya kiutamaduni ya mahali, kwa kuwa alama na rangi hubeba maana tofauti kuvuka tamaduni. Zingatia tofauti za maudhui ya kisheria na ya udhibiti ya mahali. Tofautisha uthabiti wa kimataifa (chapa, utendaji wa msingi) na marekebisho ya kikanda (maudhui, mifano, uzingatiaji) na uamue waziwazi vipengele vipi vimewekwa na vipi vinanyumbulika.

### Tawala i18n kama miundombinu ya pamoja

Toa maktaba ya pamoja ya i18n, kanuni za lint za kupeleka mifuatano nje, na utaratibu wa kawaida wa kutatua lokali ili timu zisiweze kupachika maandishi kwa bahati mbaya. Anzisha umiliki wa bomba la ulokalishaji na faharasa. Jaribu katika lokali kadhaa kwenye CI, ikijumuisha lokali ya kulia-kwenda-kushoto na pseudo-lokali ya maandishi marefu, ili regression zinaswe kiotomatiki.

## Mabadilishano: faida na hasara

| Uamuzi | Faida | Hasara |
|---|---|---|
| Andaa kimataifa tangu siku ya kwanza | Kuingia soko baadaye ni nafuu, hakuna kurudisha | Gharama ya awali hata kabla lokali ya pili inahitajika |
| Rudisha i18n baadaye | Huahirisha gharama kama hitaji la kimataifa halina uhakika | Ghali sana na hatari kufungua dhana zilizopachikwa |
| Tafsiri ya binadamu | Ubora wa juu, sahihi kiutamaduni | Polepole na ghali zaidi |
| Tafsiri ya mashine | Haraka, nafuu, inapanuka hadi kiasi kikubwa sana | Hatari ya ubora na usahihi; haifai maudhui ya dau kubwa |
| Bomba endelevu la ulokalishaji | Lokali zinabaki sawia, hakuna mbio za uzinduzi | Uwekezaji wa zana na mchakato |
| Marekebisho ya kina ya kiutamaduni kwa kila kanda | Ulinganifu bora wa mahali na uaminifu | Lahaja zaidi za maudhui za kujenga na kudumisha |

Mabadilishano muhimu ni lini kuwekeza kwenye uandaaji wa kimataifa. Kurudisha i18n kwenye bidhaa iliyojaa msimbo uliopachikwa, ulioungwa, unaodhania Kilatini ni mojawapo ya aina ghali zaidi za deni la kiufundi kulipa. Kwa shirika lolote lenye matamanio yanayowezekana ya kimataifa au ya lugha nyingi, ambayo inajumuisha karibu mashirika makubwa yote na serikali za lugha nyingi, kuandaa usanifu kimataifa mapema ni nafuu zaidi sana kuliko kurudisha, ingawa faida inaahirishwa.

## Maswali ya kujadili na timu yako

1. **Tunatekeleza kupeleka mifuatano nje kwa kanuni za lint, na je, pseudo-ulokalishaji unaendeshwa kwenye CI kabla ya tafsiri yoyote halisi?** Deni linalofanya uandaaji wa kimataifa kuwa ghali (mifuatano ya Kiingereza iliyopachikwa, vipande vya sentensi vilivyoungwa, dhana za hati ya Kilatini) hujilimbikiza kimyakimya isipokuwa zana zinaizuia wakati wa commit. Kanuni za lint zinazoweka alama maandishi ya mtumiaji yaliyopachikwa, pamoja na pseudo-lokali ya maandishi marefu yenye alama inayoendeshwa kwenye CI, hunasa kukata, kuingiliana, na hitilafu za usimbaji zikiwa nafuu kurekebisha. Hii ndiyo inayoruhusu timu kadhaa kusafirisha bidhaa moja katika lugha nyingi bila kila moja kubuni upya mabomba au kufungua dhana kwa tarehe ya mwisho baadaye. Leta utafutaji wa mifuatano iliyopachikwa na uliza kama timu yoyote ingeweza kusafirisha moja kwa bahati mbaya leo. Kama hakuna kitu kwenye bomba kingeinasa, hilo ndilo pengo la kufunga kwanza.

2. **Tunahifadhi wapi data ya msingi, na je, uumbaji umefungwa kwenye safu ya uwasilishaji?** Kuhifadhi mihuri ya muda kama UTC, nchi na sarafu kama misimbo ya ISO, na kiasi katika vipimo vya msingi kunamaanisha lokali yoyote inaweza kuviumba ipasavyo pembeni, wakati mantiki ya uumbaji iliyooka kwenye safu ya data huzalisha hitilafu zenye maumivu kufungua. Kubaliana kwamba tarehe, namba, sarafu, anwani, na majina huumbwa tu kwenye uwasilishaji, kupitia maktaba iliyojaribiwa vizuri badala ya msimbo wa mkono. Hili ni muhimu kwa mashirika ya kimataifa na serikali za lugha nyingi ambapo raia lazima aone mpangilio sahihi wa tarehe, vitenganishi vya desimali, na mpangilio wa majina kwa mkataba wake. Leta mfano wa thamani ambayo mfumo wenu unahifadhi ikiwa imeumbwa tayari na ufuatilie nini kinavunjika lokali mpya inapoihitaji tofauti. Data na uwasilishaji vikiwa vimeunganika, amua jinsi mnavyovifungua kabla ya kuongeza lokali.

3. **Tafsiri ya mashine inakubalika wapi hasa, na bomba letu la ulokalishaji linawekwa endelevu badala ya kundi vipi?** Tafsiri ya mashine ni ya haraka na nafuu kwa maudhui ya hatari ndogo, kiasi kikubwa lakini haifai maandishi ya kisheria, kimatibabu, usalama, au muhimu kwa chapa ambapo tafsiri mbaya husababisha madhara halisi, kwa hiyo mpaka unahitaji kuwa sera wazi, si kubahatisha kwa kila timu. Vilevile, kuchukulia ulokalishaji kama kundi la kabla ya uzinduzi huhakikisha mbio za tafsiri, wakati kutoa mifuatano kiotomatiki na kusawazisha kupitia mfumo wa usimamizi wa tafsiri huweka kila lokali ya sasa. Amua nani anamiliki bomba, faharasa, na lango la mapitio ya binadamu kwa mifuatano ya dau kubwa. Leta toleo la hivi karibuni na uliza mifuatano yake mipya ilichukua muda gani kuonekana katika kila lugha. Kama lokali zinatofautiana kati ya matoleo, bomba lenu ni kundi lililojificha.

4. **Tunajaribu lokali ya kulia-kwenda-kushoto na pseudo-lokali ya maandishi marefu kiotomatiki, au tunadhania kimyakimya hati za Kilatini na mipangilio ya urefu wa Kiingereza?** Usaidizi wa pande mbili (kulia-kwenda-kushoto) na upanuzi wa maandishi ni dhana zinazovunjika kwa wazi zaidi katika soko jipya: violesura vilivyopaswa kuakisiwa lakini havikuakisiwa kamwe, na vitufe vinavyokatwa Kijerumani au Kifini kinapokuwa kirefu kwa asilimia arobaini kuliko Kiingereza. Vuta linaloshindana ni kasi, kwa kuwa kujenga juu ya sifa za mpangilio za kimantiki badala ya za kimwili na kuunganisha pseudo-lokali yenye alama kwenye ujumuishaji endelevu (CI) kunagharimu juhudi kabla mteja yeyote halisi hajaihitaji. Leta picha ya skrini ya skrini zenu zenye shughuli nyingi zaidi zilizoonyeshwa katika lokali ya kulia-kwenda-kushoto na katika pseudo-lokali iliyorefushwa, na uhesabu kuingiliana, lebo zilizokatwa, na mishale iliyokwama. Kwa shirika la kimataifa au serikali inayohitajika kisheria kuhudumia lugha ya kulia-kwenda-kushoto au ya walio wachache, mpangilio usioweza kuakisi si kasoro ya urembo, ni soko au wajibu wa kisheria usioweza kutimiza bila kujenga upya.

5. **Sehemu zipi za bidhaa zimewekwa kimataifa na zipi zinanyumbulika kwa kanda, na nani ana mamlaka ya kuamua?** Ulokalishaji ni wa kiutamaduni, si wa kilugha tu, kwa hiyo rangi, picha, mifano, vyeo vya heshima, na hata vipengele vipi vinatolewa vinaweza kutofautiana kwa soko, hata hivyo kila lahaja ya kikanda mnayoruhusu ni mabaki mengine ya kujenga, kutafsiri, kupitia, na kudumisha milele. Mvutano ni kati ya ulinganifu wa mahali, unaojenga uaminifu na ubadilishaji, na uthabiti, unaoweka chapa katika mshikamano na mzigo wa matengenezo ukiwa na mipaka. Leta orodha madhubuti ya kile lokali mpya inayopendekezwa ingebadilisha zaidi ya mifuatano iliyotafsiriwa, na upime kwa bei utunzaji endelevu wa kila lahaja, si ujenzi wake wa kwanza tu. Katika shirika kubwa uamuzi huu unahitaji mmiliki aliyetajwa ili timu za kikanda zisifanye fork bidhaa papo hapo, na katika serikali lazima uheshimu kanuni za maudhui za kisheria na za ufikivu zinazotofautiana kwa mamlaka na si za hiari.

6. **Lokali zipi tunajitolea kweli, tunaweka vipi istilahi thabiti kuvuka hizo, na ushahidi gani unaendesha orodha hiyo?** Kuongeza lugha ni rahisi kuahidi na ghali kudumisha, kwa sababu kila moja inahitaji faharasa, mwongozo wa mtindo, mapitio ya binadamu kwa mifuatano ya dau kubwa, na ushughulikiaji sahihi wa wingi na jinsia ambao mantiki ya kijinga ya umoja-au-wingi inakosea katika lugha nyingi. Mazingatio yanayoshindana ni ufikiaji dhidi ya gharama: soko au idadi ya watu iliyohudumiwa vibaya inaweza kuwa mbaya kuliko ile isiyohudumiwa kabisa. Leta idadi ya watu au mapato nyuma ya kila lokali mgombea, ufikiaji wa kanuni za wingi na uumbaji ambao maktaba yenu inatoa kwayo, na nani anamiliki faharasa yake. Kwa shirika la kimataifa kichocheo ni soko linaloweza kufikiwa na gharama ya msaada kwa kila lugha, wakati kwa serikali ni wajibu wa kisheria wa ufikiaji wa lugha na usawa, unaopimwa kwa idadi ya wakazi wanaoweza kufanya miamala katika lugha hiyo tu.

## Mtazamo wa sekta

**Kampuni changa.** Fanya chaguo za bei nafuu za usanifu siku ya kwanza na uache hapo: UTF-8 mwanzo hadi mwisho, kila mfuatano unaomkabili mtumiaji katika katalogi ya ujumbe, na tarehe, namba, na sarafu zilizoumbwa kupitia maktaba inayofahamu lokali. Hivi vinagharimu karibu hakuna ukisafirisha kwa lugha moja na vinaokoa kuandika upya mteja wako wa kwanza mkubwa anapotaka ya pili. Usianzishe bomba la tafsiri wala kuunga mkono lokali ambazo hakuna anayelipia bado; weka mlango wazi, si nyumba nzima ikiwa imepambwa.

**Biashara ndogo.** Bila mtaalamu wa uandaaji wa kimataifa na bajeti finyu, egemea vipengele vya i18n vilivyo tayari kwenye mfumo wako na huduma ya usimamizi wa tafsiri inayopangishwa badala ya kujenga mabomba mwenyewe. Tumia tafsiri ya mashine kwa maudhui ya hatari ndogo, kiasi kikubwa na ulipie tafsiri ya binadamu pale tu kosa lingekugharimu mteja au kukiuka kanuni, kama maandishi ya kisheria, usalama, au bili. Jitolee kwa lokali pale tu soko mahususi linapohalalisha wazi gharama endelevu ya tafsiri na mapitio.

**Biashara kubwa.** Tatizo ni utawala kuvuka timu nyingi: maktaba ya pamoja ya i18n, kanuni za lint zinazokataa mifuatano iliyopachikwa, bomba endelevu la ulokalishaji lenye kumbukumbu ya tafsiri na faharasa za kila lugha, na CI ya lokali nyingi inayojumuisha pseudo-lokali ya kulia-kwenda-kushoto na ya maandishi marefu. Endesha ulokalishaji kama miundombinu ya pamoja yenye mmiliki wazi ili vikundi viache kubuni upya mabomba au kutofautiana. Pima ufikiaji wa lugha, ubora wa ulokalishaji, na muda wa kuzindua lokali mpya, na usimamie jalada la lokali dhidi ya namba hizo badala ya kuzindua masoko papo hapo.

**Serikali.** Ufikiaji wa lugha mara nyingi ni wajibu wa kisheria, ukifunika lugha rasmi, hati za kulia-kwenda-kushoto, na lugha za asili au za walio wachache, kwa hiyo uwazi na usawa huumba kila uchaguzi. Jenga mfumo wa pamoja wa i18n na mtiririko wa tafsiri kuvuka mawakala, hitaji mapitio ya binadamu kwa istilahi za kisheria na usalama, na uchapishe faharasa ili istilahi zibaki thabiti kati ya huduma. Ununuzi unapaswa kudai usaidizi wa lokali, kulia-kwenda-kushoto, na ufikivu kwenye mikataba, na idadi ya watu inayohudumiwa katika kila lugha ndicho kipimo kinachohalalisha matumizi kwa umma.

## Mifano

**Kampuni changa.** Kampuni changa ndogo inayosafirisha kwa Kiingereza tu bado ilifanya chaguo chache za bei nafuu za usanifu siku ya kwanza: UTF-8 kila mahali, kila mfuatano unaomkabili mtumiaji ukitolewa kwenye katalogi ya ujumbe badala ya kupachikwa, na tarehe na sarafu zilizoumbwa kupitia maktaba inayofahamu lokali. Iligharimu karibu hakuna walipokuwa na lugha moja. Mwaka mmoja baadaye, mtarajiwa wao mkubwa zaidi alipoomba toleo la Kifaransa na Kijerumani, kuongeza lokali hizo kulikuwa zaidi zoezi la tafsiri lililokabidhiwa kwa mkandarasi, si kuandika upya, na walifunga mkataba ndani ya wiki badala ya kuuahirisha kwa robo ya kazi ya kihandisi.

**Biashara kubwa.** Kampuni ya biashara ya mtandaoni ya kimataifa iliandaa jukwaa lake kimataifa mapema: UTF-8 kote, mifuatano iliyotolewa nje, maktaba ya uumbaji inayofahamu lokali, na bomba endelevu la ulokalishaji lenye kumbukumbu ya tafsiri na faharasa za kila lugha. Kuingia soko jipya ikawa kwa kiasi kikubwa zoezi la maudhui (tafsiri, kagua, rekebisha picha) badala ya mradi wa kihandisi, kuruhusu kampuni kuzindua katika lokali mpya ndani ya wiki. Usaidizi wa kulia-kwenda-kushoto uliojengwa juu ya sifa za mpangilio za kimantiki ulimaanisha masoko ya Kiarabu na Kiebrania yalihitaji kazi ndogo mpya ya UI.

**Serikali.** Serikali ya kitaifa inayohitajika kisheria kutoa huduma katika lugha kadhaa rasmi, ikijumuisha hati ya kulia-kwenda-kushoto na lugha za walio wachache, ilijenga mfumo wa pamoja wa i18n na mtiririko wa tafsiri unaotumika kuvuka mawakala. Pseudo-ulokalishaji kwenye CI ulinasa mifuatano iliyopachikwa na kukata kabla ya uzinduzi; faharasa ya pamoja iliweka istilahi za kisheria thabiti kuvuka huduma na lugha. Raia wanaweza kukamilisha miamala ya kodi, afya, na manufaa katika lugha yao wenyewe wakiwa na uumbaji sahihi wa tarehe, namba, na majina, wakitimiza sheria ya ufikiaji wa lugha na kuboresha usawa kwa wazungumzaji wa lugha zisizo za walio wengi.

## Kesi ya biashara: sababu, ROI, na TCO

ROI ya uandaaji wa kimataifa ni ufikiaji wa soko na kasi. Bidhaa iliyoandaliwa vizuri kimataifa inaweza kuingia nchi mpya na masoko ya lugha haraka na kwa bei nafuu, ikigeuza kila lokali mpya kuwa mapato ya nyongeza au ufikiaji wa raia badala ya mradi mkubwa. Ubora wa ulokalishaji huendesha ubadilishaji, uaminifu, na gharama ya msaada katika kila soko: watumiaji hufanya miamala zaidi na kuwasiliana na msaada kidogo bidhaa inapozungumza lugha yao kwa usahihi na kuheshimu mikataba yao.

Kwenye TCO, gharama ya kupokea ni uhandisi wa awali wa kuandaa kimataifa, pamoja na gharama endelevu za tafsiri na bomba. Gharama ya kutopokea ni kurudisha kwa gharama: kufungua mifuatano iliyopachikwa, kuunganisha, hitilafu za usimbaji, na dhana za mpangilio kuvuka msingi mzima wa msimbo, mara nyingi kwa tarehe ya mwisho inayoendeshwa na hitaji la soko au la kisheria. Ulokalishaji duni pia hubeba gharama zilizofichika: mauzo yaliyopotea katika masoko yaliyohudumiwa vibaya, mzigo wa msaada kutoka miundo inayochanganya, na madhara ya kisheria au ya sifa kutoka maudhui ya dau kubwa yaliyotafsiriwa vibaya. Ulokalishaji endelevu huepuka mbio za gharama za tafsiri za kabla ya uzinduzi.

Kuweka kesi kwa uongozi, weka uandaaji wa kimataifa kama chaguo juu ya masoko ya baadaye. Ni uwekezaji wa awali wa wastani unaopunguza kwa kiasi kikubwa gharama na muda wa kila kuingia soko kwa siku zijazo. Kwa serikali, kichocheo ni wajibu wa kisheria wa ufikiaji wa lugha na usawa, unaopimwa kwa idadi ya watu inayohudumiwa katika kila lugha.

## Mifumo mibaya na mitego

- **Mifuatano iliyopachikwa**: maandishi ya mtumiaji yaliyooka kwenye msimbo, yakilazimisha mabadiliko ya msimbo kwa kila lokali.
- **Kuunganisha mifuatano**: kujenga sentensi kutoka vipande, ambayo huvunja sarufi na mpangilio wa maneno.
- **Dhana zisizo za Unicode**: hitilafu za usimbaji, [mojibake](https://en.wikipedia.org/wiki/Mojibake) (maandishi yaliyoharibika kutoka usimbaji wa herufi usiolingana), na kushindwa kuwakilisha hati.
- **Kudhania urefu wa maandishi ya Kiingereza**: mipangilio inayokata au kuingiliana inapotafsiriwa.
- **Kupuuza kulia-kwenda-kushoto**: kutumia mpangilio wa kimwili wa kushoto/kulia usioweza kuakisi.
- **Wingi wa kijinga**: mantiki ya umoja/wingi isiyo sahihi katika lugha nyingi.
- **Uumbaji usiojali lokali**: miundo ya tarehe, namba, na sarafu iliyopachikwa.
- **Kutafsiri bila muktadha**: watafsiri wakibahatisha maana, wakizalisha makosa.
- **Ulokalishaji wa kundi, wa dakika ya mwisho**: mbio za kabla ya uzinduzi badala ya bomba endelevu.
- **Kutojali utamaduni**: picha, rangi, au mifano inayokera au kuchanganya mahali.

## Kielelezo cha ukomavu

**Ngazi ya 1: Kuanzisha.** Lugha moja, mifuatano iliyopachikwa, dhana zisizo za Unicode, na maandishi yaliyojengwa kwa kuunganisha. Uandaaji wa kimataifa ni wa kuitikia: lokali mpya yoyote inamaanisha kubadilisha msimbo, na hitilafu za usimbaji na mpangilio zinapatikana kwa bahati kwenye uzalishaji.

**Ngazi ya 2: Kuendeleza.** Baadhi ya mifuatano imetolewa nje na Unicode inatumika mahali fulani, lakini mazoea hayana uthabiti kuvuka timu. Ulokalishaji ni juhudi ya mkono, ya kundi, ya kabla ya uzinduzi, na uumbaji, ushughulikiaji wa wingi, na usaidizi wa kulia-kwenda-kushoto vinashughulikiwa tofauti (au kabisa havishughulikiwi) kutoka timu moja hadi nyingine.

**Ngazi ya 3: Kusawazisha.** Usanifu wa pamoja wa i18n na maktaba ya uumbaji inayofahamu lokali ndio kiwango kilichoandikwa, kinachotekelezwa shirika zima. Kutoa mifuatano nje kunakaguliwa kwa kanuni za lint, mfumo wa usimamizi wa tafsiri na bomba endelevu vipo vikiwa na faharasa na kumbukumbu ya tafsiri, na pseudo-ulokalishaji pamoja na majaribio ya lokali nyingi (ikijumuisha ya kulia-kwenda-kushoto na ya maandishi marefu) yanaendeshwa kwenye CI.

**Ngazi ya 4: Kusimamia.** Programu ya ulokalishaji inapimwa na kudhibitiwa dhidi ya vipimo vya msingi. Timu zinafuatilia ufikiaji wa lugha, ubora wa ulokalishaji na viwango vya kasoro, ucheleweshaji wa kusawazisha mifuatano kutoka commit hadi toleo lililotafsiriwa, kasoro za kukata na uonyeshaji wa kulia-kwenda-kushoto zinazonaswa kwa kila toleo, gharama ya tafsiri kwa kila lokali, na muda wa kuzindua lokali mpya, na vipimo hivi vinaweka lango la matoleo na kuendesha mahali pa kuwekeza mapitio ya binadamu dhidi ya tafsiri ya mashine.

**Ngazi ya 5: Kuratibu.** Uandaaji wa kimataifa na ulokalishaji vinaboreshwa mfululizo na kuunganishwa kuvuka shirika. Ulokalishaji ni endelevu, tafsiri ya mashine na ya binadamu huchaguliwa kwa makusudi kwa kila daraja la maudhui, na marekebisho ya kiutamaduni ni ya kimfumo. Shirika linaongeza, kustaafisha, na kupanua upya lokali kwa kujibu ushahidi wa soko na usawa, na lokali mpya zinazinduliwa haraka kwa ubora wa juu bila kurudisha.

## Mawazo ya kujadili

- Bidhaa inapaswa kuandaliwa kimataifa mapema kiasi gani ikiwa hitaji la kimataifa halina uhakika?
- Tafsiri ya mashine inakubalika wapi, na wapi binadamu lazima wapitie?
- Mnaweka vipi istilahi thabiti kuvuka lugha na timu nyingi?
- Marekebisho ya kiutamaduni ya kikanda kiasi gani yanastahili matengenezo ya lahaja zilizoongezwa?
- Usaidizi wa kulia-kwenda-kushoto na lugha za walio wachache unapaswa kupewa kipaumbele na kujaribiwa vipi?
- Mnawapaje watafsiri muktadha wa kutosha bila kupunguza kasi ya bomba?

## Mambo muhimu ya kukumbuka

- Andaa usanifu kimataifa mara moja; lokalisha maudhui mara nyingi.
- Tumia Unicode kila mahali, toa mifuatano yote nje, na usiunganishe kamwe tafsiri.
- Panga kwa upanuzi wa maandishi, hati za kulia-kwenda-kushoto, na kanuni za wingi na uumbaji mahususi za lokali.
- Endesha bomba endelevu la ulokalishaji lenye kumbukumbu ya tafsiri, faharasa, na muktadha.
- Fanya pseudo-ulokalishaji mapema kwenye CI kunasa hitilafu za i18n kabla ya tafsiri halisi.
- Ulokalishaji ni wa kiutamaduni, si wa kilugha tu.
- Uandaaji wa kimataifa wa mapema ni nafuu zaidi sana kuliko kurudisha; kwa serikali ni sharti la kisheria la usawa.

## Marejeo na usomaji zaidi

- The Unicode Consortium, *The Unicode Standard* and Common Locale Data Repository (CLDR)
- W3C Internationalization (i18n) Activity, techniques and best practices
- Richard Ishida, W3C internationalization articles and tutorials
- Bert Esselink, *A Practical Guide to Localization*
- John Yunker, *Beyond Borders: Web Globalization Strategies*
- Unicode Technical Standard #35 (locale data markup) and ICU library documentation
- IETF BCP 47 language tags
- Government multilingual service and language-access guidance
- Nielsen Norman Group and W3C articles on RTL, text expansion, and localization UX
