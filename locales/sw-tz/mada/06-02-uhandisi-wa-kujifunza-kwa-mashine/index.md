# 6.2 Uhandisi wa kujifunza kwa mashine (MLOps)

## Muhtasari na msukumo

Uhandisi wa kujifunza kwa mashine, kwa kawaida huitwa [MLOps](https://en.wikipedia.org/wiki/MLOps), ni nidhamu ya kutoa [kujifunza kwa mashine](https://en.wikipedia.org/wiki/Machine_learning) kwenye daftari na majaribio na kuiweka kwenye mifumo ya uzalishaji ya kutegemewa, inayoonekana, inayodumishika. Programu ya kawaida hutenda kama msimbo wake unavyosema. Mfumo wa ML hutenda kama msimbo wake, data yake, na vigezo vyake vya mfano vilivyojifunzwa vinavyosema kwa pamoja. Hilo hufanya mifumo ya ML kuwa ngumu zaidi kujaribu, ngumu zaidi kuzalisha upya, na yenye mwelekeo wa kushindwa kimyakimya dunia inapoteleza mbali na data iliyofunzwa. MLOps huleta ukali wa uhandisi wa programu (udhibiti wa matoleo, majaribio, utoaji endelevu, na ufuatiliaji) kwenye uhalisia huu wa sehemu tatu wa msimbo pamoja na data pamoja na mifano.

Kwa timu kubwa, MLOps ndiyo inayotenganisha mfano wa mara moja unaovutia kwenye onyesho na meli ya mifano ambayo timu nyingi zinaweza kujenga, kusambaza, na kuendesha kwa usalama. Bila majukwaa na mazoea ya pamoja, kila timu inabuni upya mabomba ya data, mizunguko ya mafunzo, na usambazaji, na unaishia na mifumo dhaifu ambayo hakuna anayeweza kuizalisha upya miezi sita baadaye. Mashirika yanategemea MLOps kupanuka kuvuka mifano kadhaa, kutimiza malengo ya kiwango cha huduma, na kuwaridhisha wakaguzi wanaouliza jinsi utabiri fulani ulivyozalishwa.

Katika serikali na tasnia zinazodhibitiwa, MLOps mara nyingi ni sharti la uzingatiaji lililojificha. Uwezo wa kuzalisha upya, asili, na matoleo ndivyo vinavyoruhusu wakala kujibu swali lenye uzito wa kisheria: hasa mfano upi, uliofunzwa kwa data ipi, kwa msimbo upi, ulizalisha uamuzi uliomwathiri raia? Mazoea yaliyokomaa ya MLOps huweka swali hilo likijibika miaka baadaye, ambayo ni uhandisi mzuri na ulinzi wa kisheria.

*Angalia pia:* sura ya 8.1 (CI/CD na utoaji), sura ya 9.2 (uonekanaji na ufuatiliaji), na sura ya 6.6 (miundombinu na operesheni za AI).

## Kanuni kuu

- Chukulia data, msimbo, na mifano kama mabaki yenye matoleo ya pamoja; kubadilisha moja hubadilisha tabia ya mfumo.
- Otomatisha njia kutoka data hadi mfano uliofunzwa hadi usambazaji ili iweze kujirudia na kukaguliwa.
- Fanya kila mfano ufuatilike hadi data, msimbo, na usanidi halisi uliouzalisha.
- Tathmini mifano dhidi ya data ya uwakilishi, iliyowekwa kando kabla ya usambazaji, na uendelee kutathmini baadaye.
- Dhania mifano hudhoofika; fuatilia kuteleza (tofauti ya taratibu ya data hai au mahusiano ya ingizo-matokeo na yale mfano ulifunzwa nayo), matatizo ya ubora wa data, na kuoza kwa utendaji tangu siku ya kwanza.
- Pendelea mabomba ya kuchosha, yanayozalishika upya kuliko majaribio ya ujanja, yasiyozalishika upya.
- Tenganisha wasiwasi wa kasi ya majaribio na ustahimilivu wa uzalishaji, na uuunganishe kwa makusudi.

## Mapendekezo

### Simamia mzunguko mzima wa ML waziwazi

Fafanua na uweke vifaa vya kupima kwenye kila hatua: kuingiza na kuthibitisha data, [uhandisi wa vipengele](https://en.wikipedia.org/wiki/Feature_engineering), mafunzo, tathmini, usambazaji, na ufuatiliaji. Fanya mipaka kati ya hatua iwe wazi ili kila moja ijaribiwe, irudiwe, na ikaguliwe. Epuka kushindwa kwa kawaida ambapo mfano unafunzwa kwenye daftari la papo hapo na kutupwa juu ya ukuta kwa operesheni. Badala yake, funika mzunguko kwenye bomba lililoratibiwa ambalo mhandisi yeyote aliyeidhinishwa anaweza kuliendesha kutoka checkout safi.

### Tumia maduka ya vipengele, ufuatiliaji wa majaribio, na rejista za mifano

**Duka la vipengele** huweka fasili za vipengele kati ili mabadiliko yaleyale yaendeshe kwenye mafunzo na kuhudumia. Hii huondoa mkengeuko wa mafunzo-na-kuhudumia (kutokuwa na uthabiti kati ya jinsi vipengele vinavyokokotolewa kwa mafunzo dhidi ya utabiri hai) na kuziruhusu timu kutumia tena vipengele badala ya kuvikokotoa upya. **Ufuatiliaji wa majaribio** hurekodi vigezo vya kila mbio ya mafunzo, toleo la msimbo, toleo la data, na vipimo, ili matokeo yalinganishwe na kuzalishika upya. **Rejista ya mifano** ni mfumo rasmi wa mifano iliyofunzwa, ukishikilia matoleo, asili, matokeo ya tathmini, hali ya idhini, na hatua ya usambazaji. Pamoja, haya yanakuruhusu kujibu "nini kilibadilika?" tabia inapohama, na kupandisha au kurudisha mifano kupitia hatua zinazotawaliwa.

### Fanya data na mifano ziweze kuzalishwa upya, ziwe na matoleo na asili

Weka matoleo kwenye seti zako za data, si msimbo tu. Tumia hifadhi inayotambulika kwa maudhui au zana za matoleo ya data ili mbio ya mafunzo irejelee picha isiyobadilika. Bandika msimbo kwa commit za git, na bandika mazingira kwa utegemezi uliofungwa na picha za kontena. Nasa asili mwanzo hadi mwisho: data ghafi ipi ililisha vipengele vipi, vipengele na msimbo upi vilizalisha mfano upi, na mfano huo umesambazwa wapi. Tukio au ukaguzi unapofika, asili hugeuza ndoto mbaya ya kiuchunguzi kuwa swali rahisi. Rekodi nasibu (mbegu) na maunzi popote matokeo yanapozitegemea.

### Chagua mifumo ya usambazaji kulingana na mzigo wa kazi

- **Kundi** hukimbiza alama kwa ratiba juu ya seti kubwa za data; rahisi zaidi kuendesha, huvumilia ucheleweshaji, bora kwa ripoti na maamuzi ya mara kwa mara.
- **Mtandaoni (wakati halisi)** huhudumia maombi ya mtu mmoja mmoja ndani ya bajeti finyu za ucheleweshaji; inahitaji urejeshaji wa vipengele wa ucheleweshaji mdogo na upangaji makini wa uwezo.
- **Kutiririka** huweka alama matukio mfululizo yanapofika; inafaa kugundua ulaghai na ufuatiliaji ambapo usafi ni muhimu.
- **Pembeni** huendesha mifano kwenye vifaa au maunzi ya ndani ya majengo kwa sababu ya ucheleweshaji, faragha, muunganisho, au enzi ya data, ya kawaida katika serikali na mazingira ya uwandani.

Chagua mfumo rahisi zaidi unaotimiza sharti, na ubuni usambazaji wako kwa usambazaji wa kivuli, canary, na kurudisha papo hapo.

### Fuatilia kuteleza, kuzorota, na ubora wa data

Weka vifaa vya kupima kwenye ingizo na matokeo kwenye uzalishaji. Tazama **kuteleza kwa data** (usambazaji wa ingizo ukihama), **[kuteleza kwa dhana](https://en.wikipedia.org/wiki/Concept_drift)** (uhusiano kati ya ingizo na lengo ukibadilika), kushindwa kwa **ubora wa data** (nulls, mabadiliko ya skima, vyanzo vya juu vilivyovunjika), na **kuzorota kwa utendaji** kunakopimwa dhidi ya ukweli uliochelewa pale ulipo. Weka vizingiti vya tahadhari, andika vitabu vya mwongozo, na uunganishe ufuatiliaji na vichocheo vyako vya kufunza upya. Kuzorota kimya ndiko kushindwa kwa kawaida kwa ML, na ufuatiliaji ndio ulinzi wako pekee dhidi yake.

## Mabadilishano: faida na hasara

| Uamuzi | Chaguo A | Chaguo B | Mabadilishano |
|---|---|---|---|
| Mfumo wa kuhudumia | Kundi | Mtandaoni | Urahisi na gharama dhidi ya usafi na ucheleweshaji |
| Ukokotoaji wa vipengele | Duka la vipengele | Mabomba kwa kila mfano | Uthabiti na kutumia tena dhidi ya mzigo wa kuweka |
| Jukwaa | Nunua jukwaa la MLOps linalosimamiwa | Kusanya zana za chanzo huria | Kasi na msaada dhidi ya unyumbulifu na kufungwa |
| Kufunza upya | Kwa ratiba | Kunakochochewa na kuteleza | Kutabirika dhidi ya uitikiaji na ugumu |
| Ukali wa kuzalishika upya | Matoleo kamili ya data | Ufuatiliaji mwepesi | Nguvu ya ukaguzi dhidi ya hifadhi na juhudi |

Mabadilishano ya jumla ni uwekezaji sasa dhidi ya udhaifu baadaye. Miundombinu mizito ya kuzalishika upya na ufuatiliaji inagharimu juhudi mwanzoni, lakini inazuia gharama kubwa zaidi sana ya kushindwa kusikoelezeka, mifano isiyozalishika upya, na uaminifu uliomomonyoka. Majukwaa yanayosimamiwa huharakisha timu lakini yanaweza kuunda kufungwa; mirundiko ya chanzo huria hutoa udhibiti kwa bei ya kazi ya muunganisho. Mashirika makubwa kwa kawaida hunufaika na timu ya jukwaa la pamoja inayoficha ugumu huu nyuma ya chaguo-msingi za barabara iliyojengwa.

## Maswali ya kujadili na timu yako

1. **Tungejuaje mfano uliosambazwa umezorota kimyakimya kabla mteja au raia hajadhurika, na nani anamiliki tahadhari hiyo?** Kuoza kimya ndiko kushindwa kwa kawaida kwa ML: msimbo bado unaendesha, mfano bado unarudisha alama za imani, na ubora unateleza dunia inapohama kutoka data ya mafunzo. Kwa timu kubwa inayoendesha mifano mingi, mnahitaji hili lijibiwe kwa kila mfano, si mara moja kwa meli, kwa sababu kila moja ina wasifu wake wa kuteleza na ucheleweshaji wake wa ukweli. Leta ufuatiliaji wenu wa sasa wa kuteleza kwa data, kuteleza kwa dhana, na kuvunjika kwa ubora wa data, vizingiti vya tahadhari, na kitabu cha mwongozo kinachosema nani anajibu. Katika mazingira yanayodhibitiwa ambapo lebo zinafika wiki baadaye, jadili ishara mbadala mnazoweza kuzitazama kwa wakati huo, kwa sababu kusubiri ukweli uliochelewa kunamaanisha kusubiri kugundua madhara. Kama hakuna mmiliki mmoja aliyetajwa kwa tahadhari ya kuteleza ya mfano, mfano huo kwa vitendo haufuatiliwi.

2. **Mkaguzi akituomba kuzalisha upya utabiri mahususi wa miezi kumi na minane iliyopita, tungeweza kweli kufanya hivyo mwanzo hadi mwisho?** Uwezo wa kuzalisha upya ni sharti la uzingatiaji lililojificha ndani ya uhandisi mzuri: unaruhusu wakala kujibu hasa mfano upi, uliofunzwa kwa data ipi, kwa msimbo upi, ulizalisha uamuzi ulioathiri mtu. Leta mfano halisi na ujaribu kuufuatilia: picha isiyobadilika ya data, commit ya git, utegemezi uliofungwa na picha ya kontena, mbegu zilizorekodiwa, na asili kutoka data ghafi kupitia vipengele hadi mfano uliosambazwa. Ishara ni kama kiungo chochote katika mnyororo huo kinakosekana au ni cha mkono. Kwa serikali na tasnia zinazodhibitiwa, amua kipindi cha uhifadhi ambacho sheria inahitaji kweli na uthibitishe hifadhi yenu inaweka asili ikijibika kwa dirisha hilo lote, kwa kuwa pengo hugeuza swali la kawaida kuwa dharura ya kiuchunguzi.

3. **Kanuni yetu ni ipi ya kupandisha mfano hadi uzalishaji na kuurudisha nyuma, na je, inatekelezwa na rejista au kwa uaminifu tu?** Kupandisha bila utawala ndivyo majaribio ya daftari yanavyovuja kwenye uzalishaji na jinsi mfano mbaya unavyodumu kwa sababu hakuna anayeweza kuurudisha kwa usafi. Kwa timu nyingi, tofauti kati ya iliyokomaa na dhaifu ni kama rejista ya mifano inaweka lango la kupandisha kwa idhini ya lazima na tathmini, au mhandisi anaweza kusukuma uzito kwa mkono. Leta njia yenu ya sasa ya kupandisha, utaratibu wenu wa kurudisha nyuma, na ushahidi kwamba usambazaji wa kivuli au canary unaendeshwa kweli kabla ya trafiki kamili. Jadili kama kufunza upya kunafanyika kwa ratiba au kunachochewa na kuteleza, na kama mifano iliyofunzwa upya inapita malango ya uthibitishaji kabla ya usambazaji, kwa sababu kufunza upya kwa data hai bila uthibitishaji huongeza kuteleza au sumu. Jibu linapaswa kutekelezwa kwenye jukwaa, si kwenye ukurasa wa wiki ambao watu wanaaminiwa kuufuata.

4. **Tunajenga jukwaa letu la MLOps kwa zana za chanzo huria, tunanunua linalosimamiwa, au tunachanganya, na nani amepima kufungwa?** Uchaguzi huu huweka dari ya kasi ya kila mfano wa baadaye kusafirishwa na udhibiti mnaobaki nao juu ya data na mabomba yenu. Jukwaa linalosimamiwa huipeleka timu uzalishaji haraka na hubeba msaada, lakini linaweza kunasa fasili za vipengele vyenu, rekodi za asili, na mabaki ya mifano kwenye umbo la umiliki msiloweza kuliacha kwa urahisi; mrundiko wa chanzo huria uliokusanywa hukuweka ukihamishika kwa bei ya kazi halisi ya muunganisho na matengenezo. Leta jumla ya gharama ya umiliki kwa kila njia (leseni au kujenga, hifadhi, kokotoo kwa kufunza upya, na wafanyakazi wa jukwaa wa kuendesha), usomaji wa uaminifu wa uwezo wa timu yenu kuendesha miundombinu, na jaribio madhubuti la kutoka: mngeweza kusafirisha nje rejista, duka la vipengele, na asili na kujenga upya kwingine? Katika mazingira ya mashirika makubwa na serikali, ongeza mapungufu ya ununuzi na kanuni za enzi ya data, kwa kuwa jukwaa linalohifadhi data ya mafunzo katika kanda au umbo ambalo mdhibiti wenu analikataza linaondolewa bila kujali urahisi wake.

5. **Duka letu la vipengele na rejista ya mifano vinapaswa kuwa jukwaa moja la kati au vilivyoshirikishwa kwa kila timu, na mkengeuko wa mafunzo-na-kuhudumia unatugharimu nini leo?** Kuweka fasili za vipengele kati huondoa mkengeuko ambapo kipengele kinakokotolewa kwa njia moja kwenye mafunzo na nyingine kwenye kuhudumia, chanzo kimya na ghali cha upotevu wa usahihi, lakini jukwaa moja linaweza kuwa kizuizi kinachopunguza kasi ya kila timu. Kushirikisha kunazipa timu uhuru huku kukizidisha mabomba na nafasi za timu mbili kufasili kipengele kilekile kwa kutokuwa na uthabiti. Leta ushahidi wa mahali mkengeuko umeshawauma, timu ngapi zinatumia tena vipengele dhidi ya kuvijenga upya, na chaguo-msingi za barabara iliyojengwa ambazo timu ya jukwaa la pamoja ingeweza kutoa. Kwa shirika kubwa, pima faida ya utawala ya mfumo mmoja rasmi unaokaguliwa dhidi ya gharama ya utoaji ya foleni ya kati, na katika mazingira yanayodhibitiwa pendelea asili ya kati inayomruhusu mkaguzi kufuatilia utabiri wowote hadi msimbo halisi wa kipengele uliouzalisha.

6. **Tumelinganisha mfumo wa usambazaji wa kila mfano na mahitaji yake halisi ya ucheleweshaji, usafi, na enzi, au tumeweka kila kitu kwenye umbo moja?** Kundi, mtandaoni, kutiririka, na pembeni kila moja hubeba gharama na ugumu tofauti sana wa uendeshaji, na kuchagua usio sahihi ama kunazidisha matumizi kwenye miundombinu ya wakati halisi ambayo ripoti ya usiku haikuihitaji kamwe au kunaporwa kikokotoo cha ulaghai usafi unaoutegemea. Amua kwa kila mzigo wa kazi mfumo gani sharti linahalalisha kweli, na upinge kusawazisha kwenye chaguo ngumu zaidi kwa sababu inahisi ya kisasa. Leta bajeti ya ucheleweshaji, kiasi, gharama ya jibu lililochakaa, na ucheleweshaji wa ukweli kwa kila mfano. Katika serikali na mazingira ya uwandani, pima usambazaji wa pembeni na wa ndani ya majengo kwa makusudi, kwa kuwa kanuni za enzi ya data au muunganisho wa mara kwa mara vinaweza kulazimisha mifano kwenye maunzi ya ndani, na chaguo hilo linaumba upya jinsi mnavyoweka matoleo, kufuatilia, na kurudisha kila mfano mnaousukuma huko.

## Mtazamo wa sekta

**Kampuni changa.** Rasilimali yako adimu zaidi ni umakini wa kihandisi, kwa hiyo weka MLOps nyepesi na uinunue. Fuatilia majaribio kwenye zana rahisi inayopangishwa, bandika kila mfano uliosambazwa kwa picha ya data ya mafunzo na commit ya msimbo kwenye git, na uongeze ukaguzi mmoja wa bei nafuu wa kuteleza badala ya jukwaa. Ruka duka la vipengele na mabomba maalumu hadi mfano wa pili au wa tatu ufanye kutumia tena kustahili; mrundiko dhaifu usioweza kuudumisha utakuzamisha haraka kuliko uwezo uliokosekana.

**Biashara ndogo.** Huenda huna mtaalamu wa jukwaa la ML na bajeti ni finyu, kwa hiyo chukulia MLOps kama kitu kilichopachikwa kwenye zana unazoendesha tayari badala ya mfumo unaouajiria. Pendelea huduma inayosimamiwa inayoshughulikia matoleo, usambazaji, na ufuatiliaji kwa ajili yako, na uweke nidhamu kama swali la usafi wa data na uwezo wa kuzalisha upya: jua mfano na data gani zilizalisha matokeo fulani, na uhifadhi uwezo wa kurudisha nyuma. Pendelea wauzaji wanaokuruhusu kusafirisha nje data na mifano yako ili kubadili baadaye kubaki kunawezekana.

**Biashara kubwa.** Tatizo ni ukubwa kuvuka mifano kadhaa na timu nyingi: duka la vipengele la pamoja, ufuatiliaji wa majaribio, na rejista ya mifano yenye kupandisha kunakotawaliwa ili vikundi viache kubuni upya mabomba. Weka bajeti ya timu ya jukwaa inayotoa chaguo-msingi za barabara iliyojengwa, sawazisha asili na ufuatiliaji ili kila mfano ukaguliwe na kila tukio lielezeke, na simamia kujenga-dhidi-ya-kununua na kufungwa kwa makusudi nyuma ya kiolesura kinachoweka zana za chini zikibadilishika. Tekeleza malango ya uthibitishaji na kurudisha nyuma kwenye jukwaa, si kwa mkataba.

**Serikali.** Uwezo wa kuzalisha upya, asili, na matoleo ni mahitaji ya uzingatiaji yaliyojificha, kwa hiyo yachukulie kama ya daraja la kwanza tangu siku ya kwanza. Weka toleo la seti ya data na msimbo halisi nyuma ya kila mfano uliosambazwa, uhifadhi asili hiyo kwa kipindi kinachohitajika kisheria, na uweze kuzalisha upya utabiri wowote wa kihistoria uliomwathiri raia. Weka binadamu akipitia maamuzi yenye matokeo, pima usambazaji wa pembeni na wa ndani ya majengo pale kanuni za enzi ya data zinapodai, na udai jukwaa lolote la muuzaji litoe uhamishaji kamili wa data, vipengele, na asili yenu.

## Mifano

**Kampuni changa.** Kampuni changa ndogo ya uchanganuzi ilisafirisha mfano wake wa kwanza wa kutabiri kuondoka kwa wateja na mwanasayansi mmoja wa data na usanidi mwepesi. Ilifuatilia majaribio kwenye zana rahisi inayopangishwa, ikabandika kila mfano uliosambazwa kwa picha ya data yake ya mafunzo na commit ya msimbo kwenye git, na kuongeza kazi ya msingi ya kila wiki iliyolinganisha ingizo za hivi karibuni dhidi ya usambazaji wa mafunzo. Chanzo cha data kilipobadilisha umbo lake la tarehe na utabiri kuanza kuteleza, ukaguzi huo rahisi uliinasa ndani ya siku badala ya baada ya simu ya mteja mwenye hasira, na timu iliweza kuzalisha upya mfano mzuri wa mwisho na kurudisha nyuma.

**Biashara kubwa.** Benki ya rejareja inaendesha mifano kadhaa ya mikopo na ulaghai. Ilisawazisha kwenye duka la vipengele linaloshirikiwa kuvuka timu, huduma ya kufuatilia majaribio, na rejista ya mifano yenye malango ya idhini ya lazima. Kila mfano kwenye uzalishaji unafuatilika hadi picha ya data yake ya mafunzo na commit ya msimbo. Mifano ya ulaghai inasambazwa kama vikokotoo vya kutiririka; mifano ya mikopo inaendeshwa kwa kundi. Safu ya ufuatiliaji inatazama kuteleza kwa ingizo na kutoa tahadhari skima ya chanzo cha data inapobadilika, jambo lililowahi kunasa mlisho wa juu uliovunjika kabla haujaharibu maamuzi.

**Serikali.** Wakala wa manufaa ya umma unatumia mfano wa ML kupa kipaumbele mapitio ya kesi. Kwa kuwa maamuzi hayo yanaathiri ufikiaji wa raia kwa huduma, wakala unaweka toleo la seti halisi ya data na msimbo nyuma ya kila mfano uliosambazwa, unaweka asili hii kwa kipindi kinachohitajika kisheria, na unaweza kuzalisha upya utabiri wowote wa kihistoria unapohitajika. Mifano inasambazwa kwa kundi na binadamu anapitia kesi zilizowekewa alama, na kifuatiliaji cha kuteleza kinalazimisha tathmini upya ya lazima idadi ya watu inayoingia inapohama, ili mfano usitumike kamwe kimyakimya nje ya masharti ambayo ulithibitishwa.

## Kesi ya biashara: sababu, ROI, na TCO

MLOps hujilipia kwa kugeuza majaribio dhaifu kuwa mali za kutegemewa. ROI inatokana na muda wa haraka zaidi hadi uzalishaji kwa mifano mipya, matukio ghali machache, miundombinu iliyorudiwa kidogo, na uwezo wa kuendesha mifano mingi na timu ndogo ya jukwaa. Duka la vipengele la pamoja na rejista vinaweza kupunguza muda wa utoaji kwa kila mfano kwa kiasi kikubwa, kwa sababu timu zinaacha kujenga upya mabomba yaleyale.

TCO inajumuisha kujenga au leseni ya jukwaa, hifadhi ya data na mifano yenye matoleo, kokotoo la kufunza upya, na wafanyakazi wa kuendesha yote. Ipime dhidi ya gharama ya kutopokea: mifano msioweza kuizalisha upya au kuikagua, kushindwa kimya kunakodhuru wateja au raia, na matokeo ya kidhibiti. Katika mazingira yanayodhibitiwa, gharama ya mfano usioweza kuelezeka kwenye ukaguzi inaweza kuzidi uwekezaji wote wa MLOps. Weka kesi kwa uongozi kwa kuweka MLOps kama kupunguza hatari na kuharakisha utoaji, si mzigo: barabara iliyojengwa ambayo kila mfano wa baadaye utasafiri.

## Mifumo mibaya na mitego

- **Kuruka kutoka daftari hadi uzalishaji.** Kusambaza mifano iliyofunzwa kwenye madaftari yasiyotawaliwa bila uwezo wa kuzalisha upya.
- **Mkengeuko wa mafunzo-na-kuhudumia.** Msimbo tofauti wa vipengele kwenye mafunzo na kuhudumia, ukisababisha upotevu wa kimya wa usahihi.
- **Hakuna matoleo ya data.** Kuweka matoleo kwenye msimbo lakini si data, kwa hiyo mbio haziwezi kuzalishwa upya.
- **Sambaza na usahau.** Kusafirisha mfano bila ufuatiliaji, kugundua kuzorota watumiaji wanapolalamika tu.
- **Kufunza upya kwa kuendeshwa kiotomatiki.** Kufunza upya kiotomatiki kwa data hai bila uthibitishaji, kukuza kuteleza au sumu.
- **Miundombinu ya mara moja.** Kila timu ikijenga bomba lake, ikizidisha gharama na udhaifu.
- **Kupuuza lebo zilizochelewa.** Kudhania unaweza kupima usahihi papo hapo wakati ukweli unafika wiki baadaye.

## Kielelezo cha ukomavu

1. **Kuanzisha.** Mifano inajengwa papo hapo kwenye madaftari; usambazaji wa mkono; hakuna matoleo ya data wala mifano; hakuna ufuatiliaji; kuzalisha upya utabiri wa zamani ni kubahatisha.
2. **Kuendeleza.** Baadhi ya ufuatiliaji wa majaribio na rejista ya mifano zinaonekana, lakini mazoea yanatofautiana kwa timu; usambazaji umeotomatishwa kwa sehemu; ufuatiliaji wa msingi unafunika mifano michache; matoleo ya data ni pungufu na asili ina mapengo.
3. **Kusawazisha.** Jukwaa la pamoja lenye duka la vipengele, rejista, mabomba yanayozalishika upya, na asili ya mwanzo hadi mwisho limeandikwa na linatekelezwa shirika zima; ufuatiliaji wa kuteleza na ubora wa data unaendeshwa kuvuka mifano; kupandisha na kurudisha nyuma kunafuata njia inayotawaliwa ambayo kila timu inaitumia.
4. **Kusimamia.** Meli inapimwa dhidi ya vipimo vya msingi: viwango vya kuteleza, kuvunjika kwa ubora wa data, usahihi wa mfano dhidi ya ukweli uliochelewa, mkengeuko wa mafunzo-na-kuhudumia, muda hadi uzalishaji, na gharama ya uendeshaji kwa kila mfano vinafuatiliwa kama vipimo; vizingiti vya tahadhari na malango ya uthibitishaji yanatekelezwa kwa ushahidi, na afya ya kila mfano inapitiwa kwa mzunguko uliowekwa na mmiliki aliyetajwa.
5. **Kuratibu.** Mzunguko wa maisha umeotomatishwa kikamilifu, unakaguliwa, na unajirekebisha; kufunza upya kunakochochewa na kuteleza kunaendeshwa nyuma ya malango ya uthibitishaji; barabara zilizojengwa za kujihudumia zinaziruhusu timu kusafirisha kwa usalama; tathmini endelevu inafunga utendaji wa mfano na vipimo vya biashara, na jukwaa limeunganishwa na utoaji, hatari, na uzingatiaji ili mifano mara kwa mara istaafishwe, ibadilishwe, na ipanuliwe upya data na hali zinavyohama.

## Mawazo ya kujadili

- Mnasawazishaje uhuru wa majaribio na uwezo wa kuzalisha upya wa uzalishaji?
- Kichocheo sahihi cha kufunza upya ni kipi (ratiba, kuteleza, au kuoza kwa utendaji) kwa matumizi yenu?
- Mnapaswa kuhifadhi asili ya data na mifano kwa muda gani, na nini kinaendesha sharti hilo?
- Maduka ya vipengele na rejista yanapaswa kuwa majukwaa ya kati au yaliyoshirikishwa kwa kila timu?
- Mnafuatiliaje usahihi lebo za ukweli zinapofika kwa ucheleweshaji mrefu?
- Usambazaji wa pembeni unastahili ugumu wake ulioongezwa wa uendeshaji lini?

## Mambo muhimu ya kukumbuka

- Tabia ya ML inatokana na msimbo pamoja na data pamoja na mifano; weka matoleo na utawale vyote vitatu pamoja.
- Maduka ya vipengele, ufuatiliaji wa majaribio, na rejista ni uti wa mgongo wa ML inayozalishika upya.
- Asili hufanya mifano ikaguliwe na matukio yaeleweke: muhimu katika mazingira yanayodhibitiwa.
- Chagua kundi, mtandaoni, kutiririka, au pembeni kulingana na mahitaji ya ucheleweshaji, usafi, na enzi.
- Mifano hudhoofika; ufuatiliaji wa kuteleza, ubora wa data, na kuoza si wa hiari.

## Marejeo na usomaji zaidi

- Chip Huyen, *Designing Machine Learning Systems*.
- Andriy Burkov, *Machine Learning Engineering*.
- D. Sculley et al., *Hidden Technical Debt in Machine Learning Systems*.
- Mark Treveil et al., *Introducing MLOps*.
- Valliappa Lakshmanan, Sara Robinson, and Michael Munn, *Machine Learning Design Patterns*.
- Emmanuel Ameisen, *Building Machine Learning Powered Applications*.
