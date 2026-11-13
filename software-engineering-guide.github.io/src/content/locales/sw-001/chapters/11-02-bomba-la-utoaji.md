# 11.2 Bomba la utoaji

## Muhtasari na msukumo

Bomba la utoaji ni mtiririko wa kazi unaogeuza wazo lililothibitishwa kuwa programu inayoendesha mikononi mwa watumiaji (kwa kutegemewa, kwa kurudiwa, na kwa kupimika) kisha kulisha data ya matokeo yanayotokana kurudi kwenye ugunduzi (sura ya 11.1). Ni njia iliyoviwandani kutoka commit ya msimbo hadi badiliko la uzalishaji hadi athari iliyopimwa kwa watumiaji na biashara. Pale ugunduzi unapojibu *nini na kwa nini*, utoaji hujibu *tunalisafirishaje kwa usalama, kwa kasi gani, na kama liliifanya kazi kweli*.

Sura hii ni ya kuunganisha kwa makusudi. Mitambo inaishi kwa undani kwingine: mkakati wa majaribio (sura ya 2.4), uotomatishaji wa majaribio na mchakato (sura ya 8.5), [ujumuishaji endelevu](https://en.wikipedia.org/wiki/Continuous_integration) na [utoaji endelevu](https://en.wikipedia.org/wiki/Continuous_delivery) (CI/CD) na mikakati ya usambazaji (sura ya 8.1), miundombinu-kama-msimbo (sura ya 8.2), kutegemewa na SLO (malengo ya kiwango cha huduma, sura ya 9.1), na majaribio (sura ya 7.4). Hapa tunakusanya kuwa bomba moja la mwanzo-hadi-mwisho na, muhimu, tunaambatisha **vipimo vya matokeo** vinavyokuambia kama mashine nzima inazalisha thamani badala ya kuzalisha matoleo tu.

Kwa timu kubwa, bomba la utoaji ndilo uwekezaji wenye nguvu kubwa zaidi ya kunufaika katika ufanisi wa kihandisi. Muongo wa utafiti, hasa mpango wa DORA ([DevOps Research and Assessment](https://en.wikipedia.org/wiki/DevOps_Research_and_Assessment)) uliofupishwa katika *Accelerate*, unaonyesha kwamba timu zenye mabomba ya utoaji ya haraka, ya kiotomatiki, ya hatari ndogo zinafanya vizuri kwenye upitishaji *na* uthabiti *na* matokeo ya shirika. Imani ya zamani kwamba kasi na usalama vinabadilishana ni uongo kwa majaribio. Katika biashara kubwa, bomba imara ndilo linaloruhusu mamia ya wahandisi kuunganisha bila kuporomoka kwenye machafuko ya muungano na maigizo ya mkono ya matoleo. Serikalini, linabadilisha matoleo ya "mlipuko mmoja" ya kila robo, yenye sherehe nyingi, ya yote-au-hakuna (historia ikiwa sababu kuu ya programu zilizoshindwa) na mabadiliko madogo, yanayoweza kutenduliwa, yanayokaguliwa yanayotimiza wajibu wa udhibiti wa mabadiliko *kupitia* uotomatishaji badala ya licha yake.

## Kanuni kuu

- **Otomatisha kila kinachorudiwa.** Hatua za mkono ni polepole, zenye makosa, na zisizoweza kukaguliwa.
- **Makundi madogo, matoleo ya mara kwa mara.** Mabadiliko madogo ni rahisi kupitia, kujaribu, kusafirisha, na kutendua.
- **Jenga ubora ndani.** Majaribio na malango ya haraka ya kiotomatiki hukamata kasoro kabla ya uzalishaji, si baada.
- **Tenganisha usambazaji na toleo.** Safirisha msimbo gizani; washa vipengele kwa bendera ukiwa tayari.
- **Fanya kila kitu kiwe kinachoweza kutenduliwa.** Kurudisha nyuma haraka na mfiduo wa hatua kwa hatua hugeuza usambazaji kutoka dau hadi jaribio.
- **Bomba ndilo chanzo cha ukweli.** Kama haipo kwenye udhibiti wa matoleo na bomba, haikutokea.
- **Pima matokeo, si pato tu.** Idadi ya usambazaji ni pato; kipimo kilichosogea ni matokeo.

## Mapendekezo

### Otomatisha suti ya majaribio na uweke lango juu yake

Uotomatishaji wa majaribio ndio msingi unaofanya utoaji wa haraka kuwa salama. Tekeleza jalada la majaribio lenye usawa, la kiotomatiki zaidi (sura ya 2.4): majaribio mengi ya kitengo ya haraka, majaribio machache ya ujumuishaji na ya mkataba, idadi ndogo ya majaribio ya mwisho-hadi-mwisho, pamoja na ukaguzi wa kiotomatiki wa usalama (SAST/DAST/SCA: uchambuzi tuli, wa kuendesha, na wa muundo wa programu), ufikivu, na utendaji. Yaendeshe kama **malango ya ubora** kwenye bomba ili hakuna badiliko lifikie uzalishaji bila kupita. Weka suti ya haraka na ya kuaminika: suti ya polepole au isiyotegemewa hukwepwa, jambo linalopoteza madhumuni yake (sura ya 8.5). Lenga bomba limpe msanidi ishara wazi ya pita/shindwa ndani ya dakika za commit.

### Fanya ujumuishaji endelevu na utoaji endelevu

**Ujumuishaji endelevu (CI):** kila msanidi anaunganisha mabadiliko madogo kwenye mstari mkuu mara kwa mara (ikiwezekana kila siku), kila muungano ukichochea ujenzi na uendeshaji wa majaribio wa kiotomatiki. Hili linaungwa mkono vyema na uundaji wa msingi wa shina (sura ya 2.6), unaoweka matawi ya muda mfupi na ujumuishaji endelevu. **Utoaji endelevu (CD):** kila badiliko linalopita bomba *liko daima katika hali ya kutolewa* na linaweza kusambazwa kwa ombi. **Usambazaji endelevu** huenda hatua moja zaidi: kila badiliko linalopita husambazwa kwenye uzalishaji kiotomatiki. Chagua kiwango cha uotomatishaji kinachofaa wasifu wenu wa hatari; mazingira yanayodhibitiwa yanaweza kusimama kwenye utoaji endelevu wenye hatua ya upandishaji inayodhibitiwa (sura ya 8.1), lakini bado yanapaswa kuotomatisha kila kitu hadi lango hilo.

### Sambaza kwa usalama kwa mikakati ya hatua kwa hatua

Tenganisha **usambazaji** (msimbo unaoendesha kwenye uzalishaji) na **toleo** (watumiaji wanapopitia badiliko), na ufichue mabadiliko polepole:

- **[Bendera za vipengele](https://en.wikipedia.org/wiki/Feature_toggle)** zinakuruhusu kusambaza msimbo gizani na kutoa kwa makundi kwa ombi, na kurudisha nyuma papo hapo kwa kubadili.
- **Matoleo ya kanari** huelekeza asilimia ndogo ya trafiki kwenye toleo jipya, ukitazama vipimo vya afya kabla ya kupanua.
- **Usambazaji wa bluu-kijani** huweka mazingira mawili na kubadili trafiki kwa mara moja, na kurudisha nyuma papo hapo.
- **Usambazaji wa kuviringika** hubadilisha mifano hatua kwa hatua.
- **Utoaji wa hatua kwa hatua** huunganisha bendera, kanari, na uchambuzi wa kiotomatiki kupandisha au kurudisha nyuma kulingana na ishara hai.

Oanisha kila mkakati na kurudisha nyuma kiotomatiki kunakochochewa na ukiukaji wa SLO au kuteketeza bajeti ya makosa (kasi ambayo kushindwa kunatumia bajeti ya kutotegemewa inayoruhusiwa; sura ya 9.1). Tazama sura ya 8.1 kwa mitambo.

### Pima matokeo: pima bomba na athari

Bomba la utoaji linalosafirisha haraka lakini kusafirisha kitu kisicho sahihi ni upotevu wa haraka. Pima kwa ngazi tatu:

1. **Mtiririko wa utoaji, vipimo vinne vya DORA:**
   - *Mzunguko wa usambazaji:* mara ngapi unatoa kwenye uzalishaji.
   - *[Muda wa kuongoza](https://en.wikipedia.org/wiki/Lead_time) wa mabadiliko:* commit hadi uzalishaji.
   - *Kiwango cha kushindwa kwa mabadiliko:* asilimia ya matoleo yanayosababisha kuharibika.
   - *Muda wa kupona kutoka usambazaji ulioshindwa:* unarejesha huduma kwa kasi gani (hapo awali MTTR, muda wa wastani wa kupona).
   Timu zenye utendaji bora kabisa husambaza kwa ombi, kwa nyakati za kuongoza chini ya saa, viwango vya chini vya kushindwa, na kupona kwa dakika. Ongeza **vipimo vya mtiririko** kutoka fikra ya mtiririko wa thamani (muda wa mzunguko, [kazi inayoendelea](https://en.wikipedia.org/wiki/Work_in_process), ufanisi wa mtiririko) kuona mahali kazi inaposubiri.

2. **Kutegemewa na ubora, SLI na SLO** (viashiria na malengo ya kiwango cha huduma; sura ya 9.1): huduma inatimiza malengo yake ya kutegemewa na ahadi za sifa za ubora (sura ya 11.1) baada ya kila badiliko?

3. **Matokeo ya biashara na ya mtumiaji** (sura za 7.3–7.4): badiliko lilisogeza matokeo muhimu na KPI ambazo ugunduzi ulifafanua? Hapa ndipo toleo linapokutana na jaribio: safirisha nyuma ya bendera, pima dhidi ya kikundi cha udhibiti, na uweke tu kinachoshinda.

### Funga mzunguko kurudi kwenye ugunduzi

Kitendo cha mwisho cha bomba la utoaji si usambazaji; ni **ushahidi**. Vipimo vya matokeo (uanzishaji ulipanda, muda wa malipo ulishuka, tiketi za msaada zilipungua) vinatiririka kurudi kwenye bomba la ugunduzi (sura ya 11.1) kama msingi wa mzunguko unaofuata wa dau. Ugunduzi na utoaji vinapounganishwa na mzunguko huu wa maoni, shirika linakuwa mfumo wa kujifunza: dhana husafirishwa, kupimwa, na ama kupanuliwa au kutenduliwa, mfululizo.

### Fanya utoaji uweze kukaguliwa na kutawaliwa

Katika mazingira ya mashirika makubwa na serikali, chukulia bomba lenyewe kama kidhibiti cha uzingatiaji. Kwa sababu kila badiliko linapita kwenye udhibiti wa matoleo na bomba la kiotomatiki, unapata nyayo za ukaguzi zisizobadilika "bure": nani alibadilisha nini, majaribio na idhini zipi ziliweka lango, na lini lilisambazwa. Simba utenganisho wa majukumu, mapitio yanayohitajika, na ukaguzi wa sera kama **sera-kama-msimbo** (kanuni za utawala zilizoonyeshwa kwa umbo linalotekelezwa na mashine, lenye udhibiti wa matoleo; sura ya 8.2) ili udhibiti wa mabadiliko utekelezwe kiotomatiki na kuthibitishwa mfululizo (sura za 4.6 na 10.2), badala ya kujengwa upya kwa mkono kabla ya ukaguzi.

## Mabadilishano: faida na hasara

| Uamuzi | Faida | Hasara |
|---|---|---|
| **Usambazaji endelevu (kiotomatiki hadi uzalishaji)** | Maoni ya haraka zaidi; makundi madogo zaidi; kazi ndogo zaidi ya mkono | Inadai majaribio, ufuatiliaji, kurudisha nyuma vilivyokomaa; ngumu kwenye malango yanayodhibitiwa |
| **Utoaji endelevu wenye upandishaji wa mkono** | Kituo cha udhibiti wa binadamu/uzingatiaji; rafiki kwa ukaguzi | Polepole; hatari ya kukusanya mabadiliko kwenye lango |
| **Bendera za vipengele** | Utenganisho wa usambazaji/toleo; kurudisha nyuma papo hapo; kulenga | Deni la bendera na ugumu wa mchanganyiko zisipopogolewa |
| **Kanari / utoaji wa hatua kwa hatua** | Hupunguza eneo la mlipuko; upandishaji wa msingi wa data | Inahitaji uonekanaji imara na usimamizi wa trafiki |
| **Bluu-kijani** | Kubadili na kurudisha nyuma papo hapo | Inaongeza maradufu gharama ya mazingira; uhamishaji wa data na hali ni mgumu |
| **Mchakato mzito wa mkono wa matoleo** | Unahisi kudhibitiwa; unafahamika kwa wakaguzi | Polepole, wenye makosa, usioweza kuzalishwa upya, usiokaguliwa vizuri kwa vitendo |

Imani ya kihistoria ya mabadilishano, *nenda haraka na utavunja zaidi*, ndiyo muhimu ya kustaafisha. Ushahidi unaonyesha kwamba mazoea yanayoongeza kasi (uotomatishaji, makundi madogo, majaribio ya haraka, kutenduliwa) ni *yaleyale* yanayoongeza uthabiti. Mabadilishano halisi yanahusu **uwekezaji na undani wa udhibiti**, si kasi dhidi ya usalama.

## Maswali ya kujadili na timu yako

1. **Wasifu wenu halisi wa hatari ni upi, na je, unahalalisha kusimama kwenye utoaji endelevu badala ya kwenda kwenye usambazaji endelevu?** Kuchagua kiwango cha uotomatishaji ni uamuzi halisi, si chaguo-msingi. Usambazaji endelevu unatoa maoni ya haraka zaidi na makundi madogo zaidi, hata hivyo unadai majaribio yaliyokomaa, uonekanaji imara, na kurudisha nyuma papo hapo, kwa hiyo muktadha unaodhibitiwa unaweza kusimama kwa busara kwenye lango la upandishaji linalodhibitiwa. Leta ushahidi: kiwango chenu cha kushindwa kwa mabadiliko, muda wenu wa kupona, na uaminifu wa suti yenu ya majaribio, kwa sababu hivyo vinakuambia kama kiotomatiki-hadi-uzalishaji ni salama leo. Kwa biashara kubwa na serikali, otomatisha kila kitu hadi lango na ufanye lango lenyewe liwe sera-kama-msimbo, ili hatua ya binadamu iongeze udhibiti bila kuongeza kazi ya mkono. Mkishindwa kuamini bomba kukamata badiliko baya, wekeza kwenye malango na uonekanaji kabla ya kugeuza swichi.

2. **Bomba lenu linaweza kuzalisha ushahidi wa ukaguzi ambao mdhibiti angeuliza, bila mtu yeyote kuujenga upya kwa mkono?** Chukulia bomba lenyewe kama kidhibiti cha uzingatiaji. Kila badiliko linapaswa kubeba nyayo zisizobadilika za nani alibadilisha nini, majaribio na idhini zipi ziliweka lango, na lini lilisambazwa, zinazozalishwa kiotomatiki. Katika biashara kubwa na serikali, simba utenganisho wa majukumu na mapitio yanayohitajika kama sera-kama-msimbo ili udhibiti wa mabadiliko utekelezwe na kuthibitishwa mfululizo badala ya kukusanywa kwa haraka kabla ya ukaguzi. Ishara ya kuleta: chagua badiliko la hivi karibuni la uzalishaji na ujaribu kuzalisha nyayo zake kamili za idhini-na-majaribio ndani ya dakika tano. Msipoweza, mnalipia maandalizi ya ukaguzi wa mkono na kubeba hatari ambayo uotomatishaji ungeondoa.

3. **Toleo linapoanza kuharibika kwenye uzalishaji, nini kinachochea kurudisha nyuma, na je, ni kiotomatiki?** Kutenduliwa ndiko kunakofanya kasi kuwa na busara badala ya uzembe, kwa hiyo kichochezi cha kurudisha nyuma kinastahili usanifu wazi. Amua kama ukiukaji wa SLO au kuteketeza bajeti ya makosa kunarudisha nyuma kiotomatiki, au binadamu lazima atambue, aamue, na atende watumiaji wakiteseka. Leta matukio yenu machache ya mwisho na upime pengo kati ya "kipimo kilianza kuharibika" na "badiliko lilitenduliwa"; pengo hilo ndilo eneo lenu halisi la mlipuko. Kwa timu kubwa zinazosafirisha mara nyingi kwa siku, kurudisha nyuma kwa mkono hakupanuki, na bendera pamoja na uchambuzi wa kanari vinakuruhusu kupandisha au kutendua kwa ishara hai. Jibu likiwa "mtu anapigiwa simu na kutafuta suluhisho," mnachukulia kila usambazaji kama dau lisiloweza kutenduliwa.

4. **Mnaposafirisha kipengele, mnapima kama kilisogeza kipimo kilichokusudiwa kusogeza, au mnahesabu usambazaji na kusonga mbele?** Bomba linalosafirisha haraka lakini kamwe halikagui athari ni upotevu wa haraka, na pengo kati ya pato na matokeo ndipo uwekezaji mwingi wa utoaji unavuja kimyakimya. Kwa shirika kubwa, mamia ya matoleo kwa wiki huvutia kuchukulia mzunguko wa usambazaji kama ubao wa alama, hata hivyo mzunguko unapima mwendo, si thamani; mvuto unaoshindana ni kwamba kupima matokeo kunagharimu upimaji, kikundi cha udhibiti, na nidhamu ya kuacha kipengele kinachoshindwa kikiwa kimezimwa. Leta vipengele vichache vya mwisho vilivyosafirishwa na, kwa kila kimoja, kipimo lengwa ambacho ugunduzi ulifafanua, kipimo cha kabla-na-baada, na mlichofanya kilipoacha kusogea. Katika majalada ya biashara kubwa na serikali, taja nani anapitia matokeo kwa mdundo uliowekwa na nani ana mamlaka ya kustaafisha kipengele kilichosafirishwa lakini hakikulipa kamwe, kwa sababu badiliko ambalo hakuna anayewajibika kulipima ni lile ambalo hakuna atakayelizima kamwe. Mtihani wa uaminifu ni kama unaweza kuonyesha kipengele ulichokitendua *kwa sababu* ushahidi ulisema kilishindwa.

5. **Bomba lenu linachukua muda gani kumpa msanidi ishara ya pita/shindwa, na je, wanaamini majaribio vya kutosha kutoyazunguka?** Kasi ya maoni na uaminifu katika suti ndivyo vinavyofanya malango yazuie kweli badala ya kukwepwa, na vyote viwili humomonyoka kimyakimya msingi wa msimbo unapokua. Kwa timu kubwa, suti inayochukua dakika arobaini au kuyumba mara moja kati ya kumi huwafundisha mamia ya wahandisi kuunganisha ikiwa nyekundu, kuzima ukaguzi, au kuendesha tena hadi kijani, jambo linaloondoa kimyakimya usalama uliohalalisha kwenda haraka; mazingatio yanayoshindana ni ufunikaji na uhalisia wa majaribio dhidi ya kasi ya maoni na uthabiti, na kusukuma lolote kwa nguvu mno huharibu lingine. Leta muda wa sasa wa bomba, kiwango cha kurudiwa kwa majaribio yasiyotegemewa, na ushahidi wowote wa malango kurukwa au kuwekwa alama yasiyozuia. Kwa mazingira ya biashara kubwa na serikali ambapo malango hayo pia hubeba SAST, DAST, na ukaguzi wa sera unaotimiza uzingatiaji, lango lililokwepwa ni hatari ya ubora na pengo la ukaguzi, kwa hiyo pima kama lango ni la lazima kweli au la ushauri tu. Wasanidi wasipoweza kueleza kwa nini wanaamini ujenzi wa kijani, lango ni pambo.

6. **Nani anamiliki kuweka njia ya utoaji thabiti kuvuka timu na kupogoa deni la bendera za vipengele, au kila timu inabuni upya bomba lake?** Shirika linapokua, utoaji ama unakutana kwenye barabara ya lami ya pamoja au unavunjika kuwa makumi ya mabomba ya kipekee yenye malango yasiyolingana, nyayo za ukaguzi zisizo sawa, na bendera zinazodumu kuliko madhumuni yake. Mvutano ni halisi: barabara ya lami ya kati inakupa uthabiti, utawala, na faida ya ukubwa, lakini agizo linalopuuza vikwazo halisi vya timu huzaa mabomba ya kivuli na chuki, kwa hiyo barabara ya lami lazima iwe nzuri vya kutosha ili timu zijiunge kwa hiari. Leta orodha ya mabomba tofauti mangapi yapo leo, uundaji na uondoaji wa bendera unatawaliwa vipi, na muda wa kuongoza na ubora wa ukaguzi unatofautiana kiasi gani kati ya timu zenu bora na mbaya zaidi. Katika mazingira ya mashirika makubwa na serikali, ongeza pembe ya uzingatiaji: mabomba yasiyo thabiti yanamaanisha utenganisho wa majukumu na ushahidi wa udhibiti wa mabadiliko unathibitishwa kwa njia tofauti (au la kabisa) katika kila timu, na barabara moja ya lami iliyokaguliwa yenye sera-kama-msimbo inageuza hilo kutoka kamari ya kila timu kuwa dhamana ya shirika. Kama hakuna anayemiliki kuondoa bendera zilizopitwa, deni la mchanganyiko hatimaye litafanya mfumo usiojaribika.

## Mtazamo wa sekta

**Kampuni changa.** Kasi ni kuishi, kwa hiyo nunua bomba lako badala ya kulijenga: unganisha uundaji wa msingi wa shina na mwendeshaji wa CI aliyepangishwa, weka lango kwa kila muungano kwa majaribio ya kitengo ya haraka na uchanganuzi wa usalama, na usambaze moja kwa moja kwenye uzalishaji nyuma ya huduma ya bendera iliyopangishwa. Ruka timu ya jukwaa na zana za kipekee; rasilimali yako adimu zaidi ni umakini wa kihandisi, na bomba ambalo mhandisi mmoja wa jumla anaweza kulidumisha linashinda la kina ambalo hakuna mtu ana muda wa kulirekebisha. Fuatilia vipimo vinne vya DORA kwenye dashibodi rahisi tangu siku ya kwanza ili ujifunze mtiririko wako mapema na uweze kuonyesha wawekezaji kwamba mnasafirisha kila siku bila kuvunja.

**Biashara ndogo.** Bila mhandisi maalumu wa matoleo na bajeti finyu, chukulia utoaji kama kitu unachokikusanya kutoka huduma zinazosimamiwa badala ya mfumo unaoufanyia wafanyakazi: CI/CD inayosimamiwa, zana ya bendera iliyopangishwa, na jukwaa la wingu linaloshughulikia utoaji na kurudisha nyuma kwa niaba yako. Pinga kujenga miundombinu ya bomba ya kipekee usiyoweza kuidumisha, na uweke njia rahisi vya kutosha ili yeyote aliye kwenye simu ya dharura aielewe chini ya shinikizo. Pendelea zana zinazofanya utoaji wa hatua kwa hatua na kurudisha nyuma kwa mbofyo mmoja zipatikane tayari, kwa sababu uwezo huo ndio unaogeuza usambazaji wa kutisha wa Ijumaa kuwa wa kawaida.

**Biashara kubwa.** Tatizo kuu ni uthabiti kuvuka timu nyingi: bomba la barabara ya lami linaloungwa mkono lenye malango ya kiotomatiki ya majaribio, usalama, na sera-kama-msimbo ambayo timu hujiunga nayo badala ya kubuni upya. Sawazisha kiolesura ili vipimo vya DORA na SLO vilinganishwe kuvuka shirika, weka bajeti wazi ya uwezo wa jukwaa unaodumisha barabara ya lami, na usimamie bendera za vipengele na kushuka kwa muda wa kuongoza kama mali zinazotawaliwa badala ya hadithi za kila timu. Utawala na ukaguzi vinaenda pamoja kiotomatiki kila badiliko linapopita njia ileile iliyo na matoleo na malango.

**Serikali.** Kanuni za ununuzi, uwazi, na uwajibikaji wa umma huumba bomba, kwa hiyo pendelea utoaji endelevu unaosimama kwenye lango la upandishaji la kiotomatiki linalotekeleza utenganisho wa majukumu na idhini zinazohitajika kama sera-kama-msimbo. Fanya bomba lenyewe liwe kidhibiti cha uzingatiaji: kila badiliko linabeba nyayo zisizobadilika za ukaguzi zinazotimiza wajibu wa udhibiti wa mabadiliko na idhini ya kufanya kazi bila kujengwa upya kwa mkono. Badilisha matoleo ya "mlipuko mmoja" yenye sherehe nyingi na mabadiliko madogo, yanayoweza kutenduliwa, yaliyotenganishwa ili uweze kujaribu mtiririko wa umma katika kanda moja, kupima viwango vya makosa na ukamilishaji, na kurudisha nyuma ndani ya dakika ukiharibika.

## Mifano

**Kampuni changa.** Timu ya wahandisi watatu inayosafirisha zana ya uchanganuzi ya B2B inaanza kwa kusambaza kwa mkono alasiri za Ijumaa, jambo linalomaanisha toleo la kutisha mara moja kwa wiki na wikendi ya hofu. Ndani ya alasiri moja wanaunganisha uundaji wa msingi wa shina na bomba la GitHub Actions: majaribio ya kitengo ya haraka, kikaguzi cha msimbo, na uchanganuzi wa usalama vinaweka lango kwa kila muungano, na ujenzi unaopita unasambaza moja kwa moja kwenye uzalishaji nyuma ya bendera za LaunchDarkly. Mzunguko wa usambazaji unaruka kutoka kila wiki hadi mara kadhaa kwa siku, na kwa sababu kila kipengele kipya kinasafirishwa gizani na kuwashwa kwa mteja mmoja rafiki kwanza, usafirishaji wa CSV ulioharibika unakamatwa na kuzimwa ndani ya dakika badala ya kuwa tukio la Jumatatu. Wanafuatilia vipimo vinne vya DORA kwenye dashibodi rahisi ili waonyeshe wawekezaji timu inasafirisha kila siku bila kuvunja.

**Biashara kubwa.** Kampuni ya bima ya kimataifa inaunganisha timu 40 kwenye bomba la barabara ya lami la pamoja (mnyororo wa zana chaguo-msingi unaoungwa mkono, uliounganishwa mapema ambao timu hujiunga nao; sura ya 8.4): uundaji wa msingi wa shina, malango ya kiotomatiki ya majaribio na usalama, na usambazaji wa kanari wenye kurudisha nyuma kiotomatiki kwa ukiukaji wa SLO. Mzunguko wa usambazaji unapanda kutoka kila mwezi hadi mara nyingi kwa siku; muda wa kuongoza unashuka kutoka wiki sita hadi chini ya siku; kiwango cha kushindwa kwa mabadiliko kinashuka kwa sababu makundi ni madogo na malango ni ya kiotomatiki. Muhimu, vipengele vya bidhaa sasa vinasafirishwa nyuma ya bendera na kupimwa dhidi ya vikundi vya udhibiti, kwa hiyo bima inaweza kufunga kila toleo na athari yake kwa kiwango cha kukamilisha nukuu, ikiunganisha bomba la utoaji moja kwa moja na matokeo muhimu ya upande wa ugunduzi ya sura ya 11.1.

**Serikali.** Wakala wa umma unabadilisha matoleo ya "mlipuko mmoja" ya kila robo (kila moja wikendi ya hatua za mkono na chanzo cha mara kwa mara cha kukatika) na bomba la utoaji endelevu linalosimama kwenye lango la upandishaji la kiotomatiki linalotekeleza utenganisho wa majukumu na idhini zinazohitajika kama sera-kama-msimbo. Kila badiliko linabeba nyayo zisizobadilika za ukaguzi zinazotimiza wajibu wa wakala wa udhibiti wa mabadiliko na ATO (idhini ya kufanya kazi) (sura ya 4.6). Matoleo yanakuwa madogo, ya mara kwa mara, na yanayoweza kutenduliwa; muda wa kupona unashuka kutoka siku hadi dakika; na kwa sababu usambazaji umetenganishwa na toleo kupitia bendera, wakala unaweza kujaribu mtiririko mpya wa mafao katika kanda moja kabla ya utoaji wa kitaifa, ukipima viwango vya ukamilishaji na makosa kabla ya kuahidi.

## Kesi ya biashara: sababu, ROI, na TCO

Faida ya uwekezaji wa bomba la utoaji ni miongoni mwa zenye ushahidi bora zaidi katika programu. Muda wa kuongoza wa haraka zaidi na mzunguko wa usambazaji wa juu humaanisha mawazo yanafikia watumiaji (na kuanza kurudisha thamani, au kusahihishwa) mapema. Kiwango cha chini cha kushindwa kwa mabadiliko na kupona kwa kasi humaanisha kukatika kidogo, kuzima moto kidogo, na uharibifu mdogo wa sifa na wa kisheria. Utafiti wa DORA unaunganisha uwezo huu na utendaji bora wa kibiashara na wa shirika, si faraja ya kihandisi tu. Athari ya kujilimbikiza ni muhimu: timu inayosafirisha na kujifunza kila siku inarudia mara 20–30 zaidi kuliko inayosafirisha kila mwezi, na kasi hiyo ya kujifunza ndiyo ya kuamua kuvuka maisha ya bidhaa.

Kwenye **[jumla ya gharama ya umiliki](https://en.wikipedia.org/wiki/Total_cost_of_ownership)**, uotomatishaji huhamisha gharama kutoka kazi ya kuchosha ya mkono ya kudumu hadi uwekezaji wa mara moja-pamoja-na-matengenezo wa bomba. Toleo la mkono hutumia masaa ya wahandisi wakuu kila mara, halipanuki vizuri, na linazalisha ushahidi dhaifu wa ukaguzi. Bomba la kiotomatiki hugawanya gharama hiyo, kisha *inapunguza* kiasi kinapokua, huku ikizalisha ushahidi imara mfululizo. Kutenduliwa kunapunguza gharama ya kushindwa yenyewe: badiliko lolote likirudishwa nyuma ndani ya sekunde, gharama inayotarajiwa ya usambazaji mbaya inaporomoka, ndiyo inayofanya kwenda haraka kuwa na busara badala ya uzembe.

Kutoa hoja kwa uongozi, pima kipimo cha msingi cha sasa kwa vipimo vinne vya DORA na masaa ya mkono yanayotumika kwa kila toleo, kisha kadiria kazi ya kuchosha iliyoondolewa na kukatika kulikoepukwa. Gharama ya kupokea ni halisi, yaani uhandisi wa bomba, uwekezaji wa majaribio, na uwezo wa jukwaa/barabara ya lami (sura ya 8.4), lakini gharama ya *kutowekeza* inalipwa mfululizo katika maoni ya polepole, hatari ya siku ya toleo, uchovu wa wahandisi, na maumivu ya ukaguzi. Hoja ya kuamua ni kiungo cha ugunduzi: bomba la utoaji la haraka, lililopimwa ndilo linalofanya dau zilizothibitishwa za bomba la ugunduzi ziweze kujaribiwa kweli kwenye uzalishaji.

## Mifumo mibaya na mitego

- **Kupima pato, si matokeo:** kusherehekea idadi ya usambazaji huku vipimo lengwa vikibaki tambarare.
- **Suti za majaribio za polepole au zisizotegemewa:** malango ambayo wasanidi hujifunza kuyapuuza au kuyakwepa.
- **Matoleo ya mlipuko mmoja, yasiyo ya mara kwa mara:** makundi makubwa yenye hatari, magumu kutatua, na magumu kutendua.
- **Usambazaji na toleo vimechanganywa:** hakuna bendera za vipengele, kwa hiyo kila usambazaji ni dau lisiloweza kutenduliwa linalomkabili mtumiaji.
- **Maigizo ya matoleo ya mkono:** orodha za ukaguzi zinazoendeshwa kwa mkono ambazo ni za polepole, zisizo thabiti, na zisizokaguliwa vizuri.
- **Bomba la kiotomatiki, hakuna uonekanaji:** kusafirisha haraka bila uwezo wa kugundua au kutatua kurudi nyuma.
- **Deni la bendera za vipengele:** bendera zisizoondolewa kamwe, zinazojilimbikiza kuwa ugumu wa mchanganyiko usiojaribika.
- **Kuchezea vipimo vya DORA:** kugawanya usambazaji kuongeza mzunguko badala ya kuboresha mtiririko.
- **Hakuna mzunguko wa maoni:** matokeo hayapimwi kamwe, kwa hiyo utoaji hauarifu mzunguko unaofuata wa ugunduzi.

## Kielelezo cha ukomavu

- **Ngazi ya 1, Kuanzisha:** Matoleo ya mkono, adimu, yenye sherehe nyingi; majaribio kwa kiasi kikubwa ya mkono na kuendeshwa kwa mkono; mafanikio yanapimwa kama "imesafirishwa"; kurudisha nyuma ni kwa maumivu na kwa papo hapo; hakuna fikra ya pamoja ya jinsi utoaji unavyopaswa kufanya kazi.
- **Ngazi ya 2, Kuendeleza:** Baadhi ya timu zinasimamisha CI yenye ujenzi wa kiotomatiki na majaribio machache; matoleo yamepangwa; ufuatiliaji wa msingi upo; mazoea yanatofautiana timu kwa timu na vipimo vya DORA bado havifuatiliwi, kwa hiyo utoaji ni bora katika mifuko lakini hauna uthabiti kuvuka shirika.
- **Ngazi ya 3, Kusawazisha:** Bomba la barabara ya lami lililoandikwa linatekelezwa shirika zima: utoaji endelevu wenye malango ya kiotomatiki ya majaribio na usalama, usambazaji wa hatua kwa hatua wenye kurudisha nyuma, na utenganisho wa majukumu unaotekelezwa kama sera-kama-msimbo. Bomba linatoa nyayo zisizobadilika za ukaguzi, na kila timu inafuata njia ileile yenye matoleo badala ya ya kipekee.
- **Ngazi ya 4, Kusimamia:** Bomba linapimwa na kudhibitiwa dhidi ya vipimo vya msingi. Vipimo vinne vya DORA (mzunguko wa usambazaji, muda wa kuongoza, kiwango cha kushindwa kwa mabadiliko, muda wa kupona), mafanikio ya SLO, kuteketeza bajeti ya makosa, na vipimo vya mtiririko kama muda wa mzunguko na kazi inayoendelea vinafuatiliwa dhidi ya malengo, na malango na kurudisha nyuma vinawaka kwa vizingiti vilivyopimwa badala ya hukumu. Deni la bendera, viwango vya majaribio yasiyotegemewa, na kushuka kwa muda wa kuongoza vinafuatiliwa, na kila uamuzi wa kwenda au kutokwenda unafanywa kwa ushahidi.
- **Ngazi ya 5, Kuratibu:** Utoaji unaboreshwa mfululizo na kuunganishwa na ugunduzi na upangaji wa hatari. Usambazaji endelevu unaendesha pale panapofaa kwa utoaji wa hatua kwa hatua na kurudisha nyuma kiotomatiki; vipengele vinasafirishwa kama majaribio yaliyopimwa ambayo vipimo vya matokeo vinarudi kwa mzunguko unaofuata wa dau; utendaji bora wa DORA unadumishwa kuvuka timu kupitia barabara ya lami; na shirika linarekebisha malango, vizingiti, na uwezo kwa kujirekebisha mzigo, hatari, na mchanganyiko wa bidhaa unapohama.

## Mawazo ya kujadili

1. Vipimo vyenu vinne vya sasa vya DORA ni vipi, na kizuizi kikubwa zaidi kwenye mtiririko wenu wa commit-hadi-uzalishaji kiko wapi?
2. Mnaweza kutenganisha usambazaji na toleo leo? Kama sivyo, bendera za vipengele zingebadilisha nini kuhusu hatari yenu?
3. Suti yenu ya majaribio inachukua muda gani, na wasanidi wanaiamini vya kutosha kutoikwepa?
4. Mlipotuma kipengele chenu cha mwisho, mlipima kama kilisogeza kipimo kilichokusudiwa kusogeza?
5. Katika muktadha unaodhibitiwa, mchakato wenu wa udhibiti wa mabadiliko unapunguza kasi ya utoaji *au* unatekelezwa kiotomatiki kupitia bomba?
6. Bendera zipi za vipengele kwenye msingi wenu wa msimbo zingepaswa kuondolewa miezi iliyopita?

## Mambo muhimu ya kukumbuka

- Bomba la utoaji linageuza mawazo yaliyothibitishwa kuwa programu inayoendesha, iliyopimwa, na kulisha matokeo kurudi kwenye ugunduzi (sura ya 11.1).
- Otomatisha njia nzima: **malango ya majaribio** ya haraka, **CI/CD**, na **miundombinu-kama-msimbo**, bomba likiwa chanzo cha ukweli.
- **Tenganisha usambazaji na toleo** na utumie mikakati ya hatua kwa hatua (bendera, kanari, bluu-kijani) na kurudisha nyuma kiotomatiki.
- Pima kwa ngazi tatu: vipimo vya **DORA/mtiririko**, **kutegemewa/SLO**, na **matokeo ya biashara/mtumiaji**.
- Kasi na uthabiti ni **vinavyokamilishana**, si mabadilishano: mazoea yanayotoa kimoja yanatoa kingine.
- Bomba pia ni **kidhibiti cha uzingatiaji**: uotomatishaji hutoa nyayo zisizobadilika, endelevu za ukaguzi.
- ROI ni ya haraka, yenye ushahidi bora (DORA), na inayojilimbikiza; gharama kuu ya kutowekeza inalipwa mfululizo.

## Marejeo na usomaji zaidi

- *Accelerate: The Science of Lean Software and DevOps*, by Nicole Forsgren, Jez Humble, Gene Kim (the DORA metrics and evidence).
- *Continuous Delivery*, by Jez Humble and David Farley (the foundational text).
- *The DevOps Handbook*, by Kim, Humble, Debois, Willis.
- *The Phoenix Project*, by Gene Kim, Kevin Behr, George Spafford (narrative on flow).
- *Site Reliability Engineering*, by Beyer, Jones, Petoff, Murphy, eds. (SLIs/SLOs, error budgets).
- *Team Topologies*, by Matthew Skelton and Manuel Pais (paved roads and delivery-team design).
- *Feature Flags / progressive delivery*, writings by Pete Hodgson and the LaunchDarkly/Split communities.
- Google DORA, *Accelerate State of DevOps* reports (annual).
- Kim, Gene, *The Unicorn Project* (developer-experience view of flow).
- Reinertsen, Donald, *The Principles of Product Development Flow* (batch size, queues, flow economics).
