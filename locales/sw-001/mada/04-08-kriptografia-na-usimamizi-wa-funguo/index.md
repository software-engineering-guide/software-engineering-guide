# 4.8 Kriptografia na usimamizi wa funguo

## Muhtasari na msukumo

Karibu kila mfumo unaojenga tayari unategemea [kriptografia](https://en.wikipedia.org/wiki/Cryptography), mazoea ya kulinda taarifa kwa mbinu za kihisabati ili wahusika waliokusudiwa tu waweze kuzisoma au kuziamini. Trafiki yako ya wavuti hupita kwenye njia zilizosimbwa, manenosiri yako yanafanywa hash, masasisho yako ya programu yanasainiwa, na data ya wateja wako inakaa imesimbwa kwenye diski. Habari njema kwa wahandisi wengi ni kwamba hawaombwi kubuni lolote kati ya haya. Sehemu ngumu si hisabati. Ni kutumia vipengele vilivyothibitishwa ipasavyo na, zaidi ya yote, kusimamia funguo ambazo vipengele hivyo vinazitegemea.

Sura hii imeandikwa kwa wahandisi ambao si wataalamu wa kriptografia, ambao ni karibu sote. Unahitaji uelewa wa kutosha kufanya chaguo sahihi, kujua kila zana inahakikisha nini, na kuepuka makosa yanayogeuza algorithimu imara kuwa faraja ya uongo. Sura ya 4.3 (usalama wa miundombinu na wingu) inataja usimbaji fiche na usimamizi wa funguo kwa kupita; hapa tunaingia ndani zaidi katika nini cha kusimba, jinsi gani, na jinsi ya kuendesha mzunguko wa maisha wa funguo unaoufanya kuwa halisi.

Kwa mashirika makubwa, kriptografia huenea kuvuka maelfu ya huduma, vyeti, na funguo, na cheti kimoja kilichokwisha muda au ufunguo mmoja uliopotea unaweza kuangusha mfumo muhimu au kuvujisha hifadhi ya data. Kwa serikali, kriptografia mara nyingi huamriwa, kuthibitishwa, na kukaguliwa, na kanuni za uainishaji wa data zinazoamua hasa funguo zipi zinalinda siri zipi na nani anaweza kuzishikilia. Katika mazingira yote mawili, kushindwa kunakojirudia ni kuleule: algorithimu nzuri zinazoharibiwa na usimamizi mbovu wa funguo.

## Kanuni kuu

- **Usibuni kriptografia yako mwenyewe.** Tumia maktaba zilizothibitishwa, zilizopitiwa na wengi, na algorithimu za kawaida. Mipango mipya hushindwa kwa njia ambazo wataalamu tu ndio wanazinasa.
- **Algorithimu ndizo sehemu rahisi; funguo ndizo sehemu ngumu.** Mzunguko wa maisha wa ufunguo ndipo kushindwa kwingi kwa ulimwengu halisi kunakoishi.
- **Jua kila kipengele kinahakikisha nini.** Usiri, uadilifu, na uhalisi ni sifa tofauti zinazohitaji zana tofauti.
- **Simba wakati wa kusafiri na ikihifadhiwa kwa chaguo-msingi.** Fanya ulinzi kuwa kiwango, si chaguo la kujiunga.
- **Tenganisha utunzaji wa funguo na ufikiaji wa data.** Yeyote anayesimamia ufunguo asiweze moja kwa moja kusoma data inayolindwa nao.
- **Panga kwa mabadiliko.** Algorithimu hudhoofika, funguo huvuja, na viwango hubadilika. Jenga kwa kuzungusha na kuhamisha tangu siku ya kwanza.
- **Pendelea utekelezaji uliothibitishwa pale inapojalisha.** Kwa kazi inayodhibitiwa na ya serikali, chagua moduli zenye uthibitisho unaotambulika.

## Mapendekezo

### Usibuni kriptografia yako mwenyewe

Hii ndiyo kanuni ya dhahabu, na inafaa kutajwa kwanza. Usibuni kamwe algorithimu yako ya usimbaji fiche, usibuni itifaki yako, wala usitekeleze kipengele kutoka kwenye karatasi kwa mkono. Kriptografia inayofanya kazi inaonekana rahisi na huficha njia fiche za kushindwa (njia za pembeni za muda, oracle za padding, nasibu dhaifu) ambazo huishi tu baada ya miaka ya mapitio ya wataalamu. Tumia maktaba zilizoimarika kama moduli ya kawaida ya kriptografia ya jukwaa lako au maktaba inayoheshimika, na uzitumie katika kiwango cha juu zaidi cha uondoaji kinachopatikana. Tumia njia za usimbaji fiche zilizothibitishwa na violesura "rahisi" vinavyofanya chaguo salama kuwa chaguo-msingi, badala ya kukusanya vipande vya kiwango cha chini mwenyewe.

### Linganisha kipengele na uhakikisho unaohitaji

Zana tofauti hutoa uhakikisho tofauti, na kuzichanganya ni kosa la kawaida na hatari. Jifunze familia tatu kuu.

- **Kriptografia ya [ufunguo linganifu](https://en.wikipedia.org/wiki/Symmetric-key_algorithm)** hutumia ufunguo mmoja wa siri unaoshirikiwa kusimba na kusimbua. Ni ya haraka na hulinda **usiri**, lakini pande zote mbili lazima tayari ziwe zinashiriki ufunguo. AES ndiyo farasi wa kazi wa kawaida.
- **Kriptografia ya [ufunguo wa umma](https://en.wikipedia.org/wiki/Public-key_cryptography)** hutumia jozi ya funguo zilizounganishwa kihisabati: ufunguo wa umma ambao yeyote anaweza kuushikilia na ufunguo wa faragha unaoweka siri. Hutatua usambazaji wa funguo na kuwezesha **saini za kidijitali**, zinazothibitisha **uhalisi** (nani alituma) na **uadilifu** (kwamba haikubadilishwa).
- **[Kazi ya hash ya kriptografia](https://en.wikipedia.org/wiki/Cryptographic_hash_function)** huzalisha alama ya kidole ya ukubwa usiobadilika ya data na hutoa ukaguzi wa **uadilifu**. Hashing ni ya njia moja na si usimbaji fiche. Kuhifadhi manenosiri, tumia kazi ya hashing ya manenosiri ya polepole yenye chumvi, kamwe si hash ya kawaida ya haraka (angalia sura ya 4.2 kuhusu usalama wa programu).

Somo la kiutendaji: usimbaji fiche huficha data lakini haithibitishi nani alituma, na hash hugundua kuchezewa lakini haifichi chochote. Mifumo mingi halisi huchanganya vyote, ndiyo maana unapaswa kuegemea maktaba zinazovifunga kwa usahihi.

### Simba wakati wa kusafiri kwa TLS ya sasa

Linda kila hatua ya mtandao kwa [Transport Layer Security](https://en.wikipedia.org/wiki/Transport_Layer_Security) (TLS), itifaki inayolinda data inapohama kati ya mifumo. Hitaji matoleo ya kisasa ya TLS, zima yaliyopitwa, chagua seti imara za cipher, na uthibitishe vyeti ipasavyo badala ya kuzima ukaguzi ili "ifanye kazi." Simba pia trafiki ya ndani ya huduma-hadi-huduma, si ukingo wa umma tu, kwa sababu msimamo wa uaminifu-sifuri unadhani mtandao wa ndani ni wa uadui. Otomatisha utoaji na usasishaji wa vyeti ili TLS iwe chaguo-msingi lisilo na juhudi kila mahali.

### Simba ikihifadhiwa kwa usimbaji fiche wa bahasha

Simba data iliyohifadhiwa kwa chaguo-msingi: hifadhidata, uhifadhi wa vitu, nakala rudufu, na kumbukumbu. Mfumo wa kawaida ni **usimbaji fiche wa bahasha**, ambapo **ufunguo wa usimbaji wa data (DEK)** husimba data halisi, na **ufunguo wa usimbaji wa ufunguo (KEK)** unaoshikiliwa kwenye huduma ya usimamizi wa funguo husimba DEK. Hii inakuruhusu kuzungusha ufunguo mkuu bila kusimba upya terabaiti za data, na inaweka ufunguo wenye nguvu wa mzizi ndani ya mpaka ulioimarishwa. Hifadhi DEK iliyofungwa tu karibu na data, na uichukue na kuifungua wakati wa matumizi.

### Endesha mzunguko wa maisha wa funguo kwa makusudi

Mzunguko wa maisha wa ufunguo ndio sehemu ngumu kweli ya kriptografia, na ndipo uvunjaji na hitilafu nyingi zinapoanzia. Simamia kila hatua kwa makusudi:

- **Kuzalisha:** unda funguo kutoka chanzo imara cha nasibu, kwa nguvu inayofaa.
- **Kusambaza:** fikisha funguo kwenye mifumo inayozihitaji bila kuzifichua kwenye msimbo, faili za usanidi, au gumzo.
- **Kuzungusha:** badilisha funguo kwa ratiba, na uweze kuzungusha haraka kwa kuathiriwa kunakoshukiwa.
- **Kubatilisha:** batilisha ufunguo au cheti kilichoathirika haraka, na uhakikishe mifumo inaheshimu kubatilisha.
- **Kuharibu:** staafisha kwa usalama nyenzo za zamani za funguo ili zisiweze kurejeshwa.

Tumia **huduma ya usimamizi wa funguo (KMS)** kuweka haya kati, na utumie [moduli ya usalama wa vifaa](https://en.wikipedia.org/wiki/Hardware_security_module) (HSM), kifaa kinachostahimili kuchezewa kinachozalisha na kulinda funguo ili zisitoke kamwe wazi, kwa funguo zako za uhakikisho wa juu zaidi. Tenganisha nani anaweza kusimamia funguo na nani anaweza kusoma data inayolindwa, ili utunzaji wa funguo utekeleze kutenganisha majukumu. Hii inaunganika moja kwa moja na uainishaji wa data na kanuni za utunzaji katika sura ya 4.5 (faragha na ulinzi wa data).

### Tofautisha usimamizi wa siri na usimamizi wa funguo

Hivi vinaingiliana lakini si sawa. **Usimamizi wa funguo** unatawala funguo za kriptografia na mzunguko wao wa maisha, kwa kawaida ndani ya KMS au HSM inayofanya shughuli za kriptografia kwa niaba yako ili ufunguo ghafi usitoke kamwe. **Usimamizi wa siri** unatawala vitambulisho vya programu (manenosiri ya hifadhidata, tokeni za API, vyeti) ambavyo huduma zinahitaji kuvichukua na kuvitumia wazi, kwa kawaida kutoka hazina ya siri yenye ufikiaji wa muda mfupi, unaokaguliwa. Tumia KMS kwa funguo, kidhibiti cha siri kwa vitambulisho, na usibandike kamwe chochote kati ya hivyo kwenye msimbo wa chanzo au faili za mazingira zilizowekwa kwenye udhibiti wa matoleo.

### Otomatisha PKI na mizunguko ya maisha ya vyeti

**Miundombinu ya ufunguo wa umma (PKI)** ni mfumo wa mamlaka za vyeti, vyeti, na minyororo ya uaminifu inayofunga funguo za umma kwa utambulisho. Kwa ukubwa, hatari kuu ya PKI ni kuisha kwa cheti bila kutarajiwa kunakoangusha huduma. Dumisha orodha ya kila cheti, fuatilia kuisha, na uotomatishe utoaji na usasishaji ili hakuna binadamu anayepaswa kukumbuka. Vyeti vya muda mfupi vinavyosasishwa kiotomatiki ni salama zaidi kuliko vya muda mrefu vinavyoshughulikiwa kwa mkono, kwa sababu uotomatishaji huondoa nukta moja ya kushindwa ya binadamu. Itifaki za kawaida hapa zinaunga mkono uwezo wa kuingiliana kuvuka wauzaji (sura ya 3.8 kuhusu uwezo wa kuingiliana na viwango huria).

### Jenga kwa wepesi wa kriptografia na uhamishaji wa baada ya quantum

Algorithimu hudhoofika kadiri muda unavyopita, na viwango husonga. **Wepesi wa kriptografia** unamaanisha kubuni mifumo ili uweze kubadilisha algorithimu na ukubwa wa funguo bila kuandika upya kwa maumivu: ficha kriptografia nyuma ya kiolesura kidogo, weka matoleo kwenye data yako iliyosimbwa ili ujue algorithimu ipi iliiunda, na dumisha orodha ya kriptografia ya unachotumia wapi. Hili ni muhimu sasa kwa sababu ya [kriptografia ya baada ya quantum](https://en.wikipedia.org/wiki/Post-quantum_cryptography), familia mpya ya algorithimu zilizobuniwa kupinga kompyuta za quantum za baadaye. Wapinzani wanaweza kuvuna data iliyosimbwa leo ili kuisimbua baadaye, kwa hiyo siri za muda mrefu zinahitaji mpango wa uhamishaji. Huhitaji kuingiwa na hofu, lakini unapaswa kujua orodha yako na uwe tayari kupokea algorithimu zilizosawazishwa za baada ya quantum majukwaa yanapozisafirisha.

### Pendelea utekelezaji uliothibitishwa pale unapohitajika

Kwa mifumo inayodhibitiwa na ya serikali, kutumia algorithimu imara hakutoshi; utekelezaji lazima uthibitishwe. **FIPS 140** (Federal Information Processing Standard 140) ni kiwango cha Marekani cha kuthibitisha moduli za kriptografia, na mikataba mingi inahitaji kriptografia iliyothibitishwa na FIPS. Kazi ya serikali pia inaweza kufuata mwongozo wa kitaifa kama seti ya Commercial National Security Algorithm (CNSA) ya NSA kwa mifumo ya siri. Angalia utawala upi unatumika kabla ya kujenga, kwa sababu kurudisha moduli zilizothibitishwa kuchelewa ni ghali. Hili linaunganika na ushahidi wa uzingatiaji na utawala (sura ya 4.6).

## Mabadilishano: faida na hasara

| Uamuzi | Faida | Hasara |
|---|---|---|
| KMS inayosimamiwa na mtoa huduma | Rahisi, iliyounganishwa, mzigo mdogo wa uendeshaji | Mtoa huduma anashikilia utunzaji; udhibiti mdogo wa moja kwa moja |
| Funguo zinazosimamiwa na mteja / HSM | Utunzaji kamili, hutimiza maagizo makali | Mzigo wa uendeshaji, hatari ya kupoteza funguo |
| Vyeti vya muda mfupi vya kiotomatiki | Hakuna kuisha bila kutarajiwa, kubatilisha haraka | Inahitaji uwekezaji wa uotomatishaji mwanzoni |
| Vyeti vya muda mrefu | Rahisi, sehemu chache zinazosonga | Kuisha kunakosimamiwa na binadamu husababisha hitilafu |
| Usimbaji fiche wa bahasha | Kuzungusha funguo kwa bei nafuu, hulinda ufunguo mkuu | Sehemu zaidi zinazosonga za kuelewa |
| Wepesi wa kriptografia mapema | Uhamishaji wa baadaye wa bei nafuu | Uondoaji wa ziada na juhudi ya usanifu sasa |
| Kupokea baada ya quantum mapema | Hulinda siri za muda mrefu | Zana changa, funguo kubwa zaidi, hatari fulani |

Mvutano wa msingi ni udhibiti dhidi ya mzigo wa uendeshaji. Kushikilia funguo zako kwenye HSM kunatoa utunzaji wa juu kabisa na kutimiza maagizo makali zaidi, lakini kunadai utaalamu na kuunda hatari mpya ya maafa: ukipoteza ufunguo unapoteza data, bila kurejesha kamwe. Huduma zinazosimamiwa na mtoa huduma huondoa mzigo huo lakini huweka utunzaji kwa mtoa huduma. Tatua kwa kuweka tabaka: tumia huduma zinazosimamiwa zenye chaguo-msingi zenye busara kwa mifumo mingi, na uhifadhi funguo zinazosimamiwa na mteja na HSM kwa data ya uainishaji wa juu zaidi ambapo udhibiti wa ziada unastahili gharama na hatari.

## Maswali ya kujadili na timu yako

1. **Mna orodha kamili ya funguo, vyeti, na algorithimu mnazotegemea?** Huwezi kuzungusha, kuhamisha, wala kukagua usichoweza kuona, na mashirika mengi hugundua yana nyenzo nyingi zaidi za kriptografia zilizotawanyika kuvuka huduma kuliko mtu yeyote anavyofuatilia. Orodha ni sharti la kila uamuzi wa baadaye: ufuatiliaji wa kuisha kwa vyeti, kuzungusha funguo, kuweka wigo wa FIPS, na upangaji wa baada ya quantum vyote vinaitegemea. Leta orodha ya vyeti vyenu vya sasa na tarehe zake za kuisha, na uliza nani anamiliki kila kimoja na nini kinavunjika kinapopita. Kwa eneo kubwa, jibu la uaminifu kwa kawaida ni kwamba hakuna chanzo kimoja cha ukweli, na kukijenga ndio hatua ya kwanza yenye kiegemeo cha juu zaidi. Kama huwezi kuorodhesha kriptografia yenu leo, wepesi na kuzungusha ni matamanio, si uwezo.

2. **Mnaweza kuzungusha au kubatilisha ufunguo ulioathirika haraka, na je, mmewahi kulifanyia mazoezi?** Kuzungusha na kubatilisha ni sehemu za mzunguko wa maisha wa ufunguo ambazo zinajalisha chini ya shinikizo tu, na timu mara kwa mara hugundua wakati wa tukio kwamba ufunguo umepachikwa kwenye msimbo katika sehemu kumi na mbili au kwamba kubatilisha hakusambai kweli. Amua lengo lenu la muda wa kuzungusha ufunguo na kubatilisha cheti, kisha lifanyie mazoezi kabla hamjalihitaji. Leta hadithi ya mfiduo wenu wa mwisho wa vitambulisho na mpitie kile kuzungusha kulichohitaji kwa vitendo. Kwa mifumo ya mashirika makubwa na serikali, kuzungusha kusikofanyiwa mazoezi kunaweza kumaanisha kuchagua kati ya mfiduo wa muda mrefu na hitilafu ya kujisababishia. Kuzungusha kukiwa hakujawahi kujaribiwa, dhania hakufanyi kazi.

3. **Utunzaji wa funguo uko wapi, na je, unatekeleza kutenganisha majukumu?** Yeyote anayeweza kusimamia ufunguo na yeyote anayeweza kusoma data inayolindwa nao hapaswi kuwa mtu yuleyule, kwa sababu kuunganisha mamlaka hayo kunashinda kimyakimya madhumuni ya usimbaji fiche wa kuhifadhiwa. Chaguo hili pia linaendesha kama mtatumia funguo zinazosimamiwa na mtoa huduma, funguo zinazosimamiwa na mteja, au HSM, kila moja ikiwa na udhibiti tofauti na hatari tofauti ya uendeshaji. Leta sera zenu za sasa za funguo na uangalie kama utambulisho wowote mmoja unaweza kusimamia ufunguo na kufikia data wazi iliyo nyuma yake, ambalo ni pengo la kawaida la kimya. Kwa data inayodhibitiwa na ya siri, kanuni za utunzaji zinaweza kuamriwa na uainishaji wa data (sura ya 4.5) na agizo. Utunzaji na ufikiaji visipotenganishwa, usimbaji fiche wenu unawalinda kidogo kuliko dashibodi inavyodokeza.

4. **Mngerejeshaje hali ikiwa ufunguo mkuu unaolinda usimbaji fiche wenu wa bahasha ungepotea au kuharibiwa?** Funguo zinazosimamiwa na mteja na HSM zinawapa utunzaji, lakini zinawakabidhi hali mpya ya kushindwa ya maafa: mkipoteza ufunguo wa usimbaji wa ufunguo, kila ufunguo wa usimbaji wa data unaoufunga unakuwa hausomeki milele, pamoja na data iliyo nyuma yake. Pima hili dhidi ya hatari kinyume ya nakala rudufu pana kupita kiasi inayounda upya kimyakimya tatizo lile la utunzaji mliokuwa mkijaribu kulitatua. Leta mipango yenu ya sasa ya nakala rudufu na amana ya funguo, eneo la mlipuko la kila ufunguo mkuu, na ushahidi kwamba urejeshaji umefanywa kweli badala ya kuandikwa tu. Kwa maeneo ya mashirika makubwa na serikali, funga hili kwa kanuni zenu za uainishaji wa data: funguo nyeti zaidi mara nyingi hukataza nakala za kawaida, kwa hiyo urejeshaji lazima ubuniwe kwa makusudi, ujaribiwe kwa ratiba, na upatanishwe na sharti lolote la udhibiti la kuthibitisha kwamba nyenzo za funguo zilizostaafishwa ziliharibiwa.

5. **Mifumo yenu iko tayari kiasi gani kwa uhamishaji wa baada ya quantum, na siri zipi za muda mrefu mngezihamisha kwanza?** Wapinzani wanaweza kuvuna trafiki iliyosimbwa na kumbukumbu leo na kuzisimbua kompyuta za quantum zitakapokomaa, kwa hiyo siri yoyote inayopaswa kubaki ya siri kwa miaka tayari imefichuliwa kwa siku zijazo msizoweza kuziona. Shinikizo linaloshindana ni kwamba zana za baada ya quantum bado ni changa, funguo ni kubwa zaidi, na kuhama mapema mno kunahatarisha kuweka dau kwenye algorithimu inayobadilika kabla haijatulia. Leta orodha yenu ya kriptografia, orodha ya siri zilizopangwa kwa muda zinazopaswa kubaki za siri, na usomaji wa uaminifu wa kama usanifu wenu unaweza kubadilisha algorithimu bila kuandika upya. Kwa kazi ya serikali na inayodhibitiwa, rekodi zenye maagizo ya usiri ya miongo mingi hufanya hili kuwa madhubuti badala ya nadharia, na ununuzi unaweza hivi karibuni kuhitaji mpango ulioandikwa wa uhamishaji na usaidizi wa algorithimu zilizosawazishwa za baada ya quantum.

6. **Kanuni zinapohitaji kriptografia iliyothibitishwa, mnajua hasa moduli zipi ziko katika wigo na kama zinastahili?** Kutumia algorithimu imara si sawa na kutumia utekelezaji uliothibitishwa, na timu mara kwa mara hugundua kuchelewa kwamba maktaba, wakati wa kuendesha wa lugha, au huduma ya wingu haijafunikwa na mpaka wa FIPS 140 ambao mkataba unadai. Mvutano ni kwamba moduli zilizothibitishwa zinaweza kubaki nyuma ya maktaba za sasa kwa vipengele na kasi, kwa hiyo kuzichagua kunabana mrundiko wenu kwa njia zinazojalisha kihandisi. Leta orodha ya moduli za kriptografia ambazo kila mfumo unaodhibitiwa unaziita kweli, vyeti vya uthibitisho vinavyozifunika, na agizo mahususi (FIPS 140, CNSA, au kanuni ya sekta) linalotumika. Kwa programu za mashirika makubwa na serikali, amueni hili kabla ya kujenga, kwa sababu kurudisha moduli zilizothibitishwa na kuidhinisha upya mfumo baadaye ni ghali, polepole, na mara nyingi hulazimisha kubuni upya vipengele mlivyodhani vimekamilika.

## Mtazamo wa sekta

**Kampuni changa.** Egemea kabisa chaguo-msingi zilizothibitishwa za jukwaa lako na utumie muda sifuri wa kihandisi kwenye kriptografia maalumu. Washa usimbaji fiche unaosimamiwa wa kuhifadhiwa, simamisha TLS kwa vyeti vinavyosasishwa kiotomatiki, fanya hash manenosiri kwa kazi ya kawaida ya polepole, na uweke siri kwenye kidhibiti cha siri cha jukwaa badala ya hazina. Uamuzi wako mmoja wa usanifu ni kiolesura chembamba kuzunguka nyanja chache unazosimba kwenye programu, ili kuhama baadaye kutoka funguo zinazosimamiwa na mtoa huduma kusiwe kuandika upya.

**Biashara ndogo.** Huna mtaalamu wa kriptografia na hamu ndogo ya kuendesha HSM, kwa hiyo nunua utunzaji badala ya kuujenga: tumia KMS na kidhibiti cha siri vinavyosimamiwa na mtoa huduma vinavyokuja na wingu lako au zana zako za SaaS. Weka kazi kama usafi, yaani hakuna funguo kwenye msimbo, usimbaji fiche umewashwa kila mahali kwa chaguo-msingi, na kuisha kwa vyeti kunafuatiliwa ili hakuna kinachopita bila kutarajiwa. Hifadhi funguo zinazosimamiwa na mteja kwa data adimu ambayo mkataba au mdhibiti anaihitaji kweli.

**Biashara kubwa.** Tatizo ni ukubwa na uthabiti kuvuka maelfu ya huduma, vyeti, na funguo. Endesha KMS ya kati yenye usimbaji fiche wa bahasha, otomatisha mzunguko mzima wa maisha wa vyeti ili hakuna kuisha kunakoshughulikiwa kwa mkono, na udumishe orodha moja ya kriptografia inayolisha kuzungusha, wigo wa FIPS, na upangaji wa baada ya quantum. Tenganisha utunzaji wa funguo na ufikiaji wa data kama kidhibiti cha shirika zima, na ufanye usimbaji fiche kuwa uwezo wa jukwaa ambao kila timu inarithi badala ya kazi ambayo kila timu inaibuni upya.

**Serikali.** Ununuzi, uthibitisho, na ukaguzi huumba kila uchaguzi. Tumia moduli zilizothibitishwa na FIPS 140 na ufuate mwongozo wa kitaifa kama CNSA kwa mifumo ya siri, funga utunzaji wa funguo na uainishaji wa data ili funguo nyeti zaidi ziwe na wafanyakazi walioidhinishwa chini ya kutenganisha majukumu kwa ukali, na uzalishe ushahidi endelevu wa kriptografia iliyothibitishwa kwa idhini inayoendelea. Andika mpango wa uhamishaji wa baada ya quantum kwa rekodi zinazopaswa kubaki za siri kwa miongo, na udai wauzaji wafichue moduli zipi zimethibitishwa kabla hamjajitolea.

## Mifano

**Kampuni changa.** Timu ndogo inayojenga programu ya kufuatilia afya inategemea kabisa chaguo-msingi zilizothibitishwa. Wanasimamisha TLS kwa vyeti vinavyosasishwa kiotomatiki, kuwasha usimbaji fiche wa kuhifadhiwa kwenye hifadhidata yao inayosimamiwa na uhifadhi wa vitu kwa KMS ya mtoa huduma, na kufanya hash manenosiri kwa kazi ya polepole yenye chumvi kutoka maktaba ya kawaida. Badala ya kuandika kriptografia yoyote wenyewe, wanatumia mwito wa kiwango cha juu wa usimbaji fiche uliothibitishwa kwa uga mmoja wanaopaswa kuusimba kwenye programu. Siri zinaishi kwenye kidhibiti cha siri cha jukwaa, kamwe si kwenye hazina. Inagharimu alasiri chache na inaondoa kategoria nzima ya makosa ya maafa.

**Biashara kubwa.** Benki ya kimataifa inaendesha KMS ya kati na meli ya HSM, yenye orodha ya kriptografia inayofuatilia kila ufunguo na cheti kuvuka maelfu ya huduma. Usimbaji fiche wa bahasha unalinda data ya wateja, funguo za data zikifungwa na funguo kuu zinazozungushwa kwa ratiba huku data ikibaki mahali pake. Utoaji na usasishaji wa vyeti umeotomatishwa kikamilifu baada ya hitilafu ya umma kuwafundisha gharama ya cheti kimoja kilichoisha. Wasimamizi wa funguo ni timu tofauti na wahandisi wa programu, kwa hiyo utunzaji unatekeleza kutenganisha majukumu, na safu ya wepesi wa kriptografia inawaruhusu kuanza majaribio ya algorithimu za baada ya quantum kwa kumbukumbu za muda mrefu.

**Serikali.** Wakala wa kitaifa unaoshughulikia rekodi za siri unatumia moduli za kriptografia zilizothibitishwa na FIPS 140 tu na kufuata mwongozo wa NSA CNSA kwa mifumo yake ya uainishaji wa juu zaidi. Funguo zinazalishwa na kushikiliwa kwenye HSM ambazo hazitoi kamwe nyenzo za funguo wazi, na utunzaji umefungwa kwa uainishaji wa data ili funguo nyeti zaidi ziwe na wafanyakazi walioidhinishwa chini ya kutenganisha majukumu kwa ukali. Vyeti vinaendesha kwenye PKI ya ndani inayosimamiwa yenye mizunguko ya maisha ya kiotomatiki, na ushahidi endelevu wa kriptografia iliyothibitishwa unalisha idhini inayoendelea ya wakala. Mpango ulioandikwa wa uhamishaji wa baada ya quantum unalinda rekodi zinazopaswa kubaki za siri kwa miongo.

## Kesi ya biashara: sababu, ROI, na TCO

Kriptografia ni eneo jingine ambapo uwekezaji wa wastani huzuia hasara za maafa, za kiwango cha kichwa cha habari. Jumla ya gharama ya umiliki inajumuisha KMS au HSM, zana za usimamizi wa siri na vyeti, na muda wa kihandisi wa kubuni mizunguko ya maisha na kuweka orodha ya sasa. Gharama hizi ni halisi lakini zina mipaka. Gharama ya kuziruka ni uvunjaji wa data isiyosimbwa, hitilafu ya saa kadhaa kutoka cheti kilichoisha, au upotevu wa data usiorejesheka kutoka ufunguo ulioshughulikiwa vibaya, kila moja ikibeba faini za udhibiti, gharama za arifa, na madhara ya kudumu ya sifa.

ROI imara zaidi inatokana na uotomatishaji na utumiaji tena. Mizunguko ya maisha ya vyeti ya kiotomatiki huondoa hitilafu ya kujisababishia ya kawaida zaidi. Usimamizi wa kati wa funguo wenye chaguo-msingi zenye busara unamaanisha kila huduma mpya inarithi usimbaji fiche wakati wa kusafiri na ikihifadhiwa bila juhudi ya kila timu, ikigeuza kriptografia kutoka kodi inayojirudia kuwa uwezo wa jukwaa. Kwa kazi inayodhibitiwa na ya serikali, moduli zilizothibitishwa na ushahidi wa kiotomatiki pia hupunguza gharama ya ukaguzi na idhini. Unapoweka kesi kwa uongozi, iweke wazi: algorithimu ni bure na zimethibitishwa, hatari inaishi kwenye usimamizi wa funguo na shughuli za vyeti, na uwekezaji mdogo, wa kiotomatiki hapo unazuia kushindwa kwa gharama.

## Mifumo mibaya na mitego

- **Kubuni kriptografia yako mwenyewe.** Algorithimu maalumu au itifaki zilizojengwa kwa mkono zinazoshindwa kwa njia fiche, za wataalamu tu.
- **Funguo na siri zilizopachikwa.** Vitambulisho vilivyobandikwa kwenye msimbo wa chanzo, faili za usanidi, au gumzo, ambapo vinavuja na haviwezi kuzungushwa.
- **Usimbaji fiche bila nidhamu ya funguo.** Kuwasha usimbaji fiche lakini kuacha ufikiaji wa funguo wazi au kutozungusha kamwe.
- **Kuchanganya hashing na usimbaji fiche.** Kuchukulia hash kama inayorejeshwa, au kuhifadhi manenosiri kwa hash ya haraka badala ya ya polepole yenye chumvi.
- **Bahati nasibu ya vyeti.** Hakuna orodha, hakuna ufuatiliaji wa kuisha, na hitilafu za ghafla za mara kwa mara cheti kinapopita.
- **Utunzaji wa funguo na ufikiaji wa data uliounganishwa.** Utambulisho mmoja unaoweza kusimamia ufunguo na kusoma data inayolindwa nao.
- **Hakuna mpango wa kuzungusha.** Funguo ambazo hazijawahi kuzungushwa na haziwezi kuzungushwa haraka chini ya shinikizo.
- **Kriptografia isiyo na wepesi.** Algorithimu zilizounganishwa kwa kina kiasi kwamba kuzibadilisha kunahitaji kuandika upya, kuzuia uhamishaji wowote wa baadaye.
- **Kupuuza maagizo ya uthibitisho.** Kutumia algorithimu imara kwenye moduli zisizothibitishwa pale FIPS au uthibitisho sawa na huo unahitajika.

## Kielelezo cha ukomavu

- **Ngazi ya 1, Kuanzisha:** Usimbaji fiche hauna uthabiti na mara nyingi haupo, unatumika kwa kuitikia mtu anapogundua pengo. Funguo na siri zimepachikwa au zinashirikiwa kwa njia isiyo rasmi kupitia gumzo na faili za usanidi. Hakuna orodha, hakuna kuzungusha, na vyeti vinaisha bila kutarajiwa, na timu mara kwa mara huandika kriptografia yao wenyewe.
- **Ngazi ya 2, Kuendeleza:** TLS na usimbaji fiche wa kuhifadhiwa vimewashwa kwa mifumo mikuu, na KMS au kidhibiti cha siri kipo, lakini upokeaji hauna usawa na unatofautiana kwa timu. Baadhi ya vyeti vinafuatiliwa huku vingine havifuatiliwi, kuzungusha ni kwa mkono na nadra, na hakuna orodha kamili ya kriptografia inayounganisha yote.
- **Ngazi ya 3, Kusawazisha:** Usimbaji fiche wakati wa kusafiri na ikihifadhiwa ndio chaguo-msingi lililoandikwa na kutekelezwa shirika zima. Funguo zinaishi kwenye KMS yenye kuzungusha kwa ratiba na usimbaji fiche wa bahasha, utunzaji wa funguo umetenganishwa na ufikiaji wa data, mizunguko ya maisha ya vyeti imeotomatishwa, orodha ya kriptografia inadumishwa, na moduli zilizothibitishwa zinatumika popote kanuni zinapozihitaji.
- **Ngazi ya 4, Kusimamia:** Eneo la kriptografia linapimwa na kudhibitiwa dhidi ya vipimo vya msingi. Mnafuatilia muda wa tahadhari kabla ya cheti kuisha, asilimia ya funguo zilizozungushwa kwa ratiba, muda wa wastani wa kubatilisha ufunguo ulioathirika, ugunduzi wa siri-ndani-ya-msimbo kwa kipindi, na ufikiaji wa orodha, na mnapitia vipimo hivi dhidi ya malengo. Kuzungusha na kubatilisha kunafanyiwa mazoezi kwa mzunguko na muda uliorekodiwa, na mikengeuko huchochea hatua ya kurekebisha badala ya kupita bila kutambuliwa.
- **Ngazi ya 5, Kuratibu:** Kriptografia ni uwezo wa jukwaa ambao kila huduma inarithi kwa chaguo-msingi, ukiboreshwa mfululizo na kuunganishwa kuvuka shirika. Kuzungusha na kubatilisha ni kwa haraka na kunafanyiwa mazoezi mara kwa mara, HSM zinalinda funguo za uhakikisho wa juu zaidi, na wepesi wa kriptografia pamoja na mpango hai wa uhamishaji wa baada ya quantum huweka eneo likijirekebisha algorithimu na maagizo yanapohama. Ushahidi wa uzingatiaji unazalishwa kiotomatiki na kulisha idhini inayoendelea.

## Mawazo ya kujadili

1. Mifumo ipi katika eneo lenu inahalalisha funguo zinazosimamiwa na mteja au HSM kwa kuzingatia gharama yao ya uendeshaji na hatari ya upotevu wa maafa?
2. Mngejengaje na kudumisha chanzo kimoja cha ukweli kwa kila ufunguo na cheti mnachomiliki?
3. Muda wenu halisi wa kuzungusha ufunguo ulioathirika leo ni upi, na nini kinaufanya kuwa wa polepole?
4. Usanifu wenu unafanya wapi ubadilishaji wa algorithimu ya kriptografia kuwa mgumu, na mngelirekebishaje kabla ya uhamishaji wa lazima?
5. Siri zipi za muda mrefu kati ya zenu zingejalisha mpinzani akizivuna sasa na kuzisimbua miaka baadaye?
6. Siri na funguo huishia kwenye msimbo, usanidi, au kumbukumbu, na mngejuaje?

## Mambo muhimu ya kukumbuka

- **Usibuni kriptografia yako mwenyewe.** Tumia maktaba zilizothibitishwa na algorithimu za kawaida katika kiwango cha juu zaidi salama cha uondoaji.
- **Algorithimu ni rahisi; usimamizi wa funguo ni mgumu.** Mzunguko wa maisha wa ufunguo (kuzalisha, kusambaza, kuzungusha, kubatilisha, kuharibu) ndipo kushindwa halisi kunakoishi.
- **Jua uhakikisho wako:** usimbaji fiche wa linganifu na wa ufunguo wa umma hulinda usiri, saini huthibitisha uhalisi na uadilifu, na hashing hugundua kuchezewa lakini si usimbaji fiche.
- **Simba wakati wa kusafiri kwa TLS ya sasa na ikihifadhiwa kwa usimbaji fiche wa bahasha**, kama chaguo-msingi kwa kila mfumo.
- **Tenganisha utunzaji wa funguo na ufikiaji wa data**, tumia KMS kwa funguo na kidhibiti cha siri kwa vitambulisho, na usipachike kamwe chochote kati ya hivyo.
- **Otomatisha mizunguko ya maisha ya vyeti** kuua hitilafu ya kuisha bila kutarajiwa, na udumishe orodha ya kriptografia.
- **Jenga kwa wepesi wa kriptografia** na uanze mpango wa uhamishaji wa baada ya quantum kwa siri za muda mrefu.
- **Pendelea utekelezaji uliothibitishwa** (FIPS 140 na mwongozo wa kitaifa unaotumika) pale kanuni au uainishaji unapouhitaji.

## Marejeo na usomaji zaidi

- National Institute of Standards and Technology, *FIPS 140-3: Security Requirements for Cryptographic Modules*.
- National Institute of Standards and Technology, *SP 800-57: Recommendation for Key Management*.
- National Institute of Standards and Technology, *SP 800-131A: Transitioning the Use of Cryptographic Algorithms and Key Lengths*.
- National Institute of Standards and Technology, post-quantum cryptography standards (FIPS 203, 204, and 205).
- Niels Ferguson, Bruce Schneier, and Tadayoshi Kohno, *Cryptography Engineering*.
- Jean-Philippe Aumasson, *Serious Cryptography*.
- David Wong, *Real-World Cryptography*.
- Internet Engineering Task Force, *RFC 8446: The Transport Layer Security (TLS) Protocol Version 1.3*.
- Open Web Application Security Project, *Cryptographic Storage Cheat Sheet* and *Transport Layer Protection Cheat Sheet*.
- National Security Agency, *Commercial National Security Algorithm (CNSA) Suite* guidance.
