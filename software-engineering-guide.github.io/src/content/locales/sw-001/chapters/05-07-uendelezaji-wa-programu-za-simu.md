# 5.7 Uendelezaji wa programu za simu

## Muhtasari na msukumo

[Uendelezaji wa programu za simu](https://en.wikipedia.org/wiki/Mobile_app_development) ni nidhamu ya kujenga programu kwa simu na kompyuta mbao. Kwa watu wengi, simu sasa ndiyo kompyuta yao kuu au pekee. Hilo hufanya programu ya simu kuwa mlango wa mbele wa huduma yako, na mara nyingi uso ambao watumiaji hutumia kulihukumu shirika lako lote.

Simu ni mazingira tofauti ya kihandisi, si toleo dogo la wavuti au kompyuta ya mezani. Kifaa kinaendesha mfukoni, kwenye betri, kupitia miunganisho inayokuja na kuondoka. Skrini ni ndogo. Mfumo wa uendeshaji unadhibiti programu yako inaweza kufanya nini. Majukwaa mawili makuu yapo ([iOS](https://en.wikipedia.org/wiki/IOS) kutoka Apple na [Android](https://en.wikipedia.org/wiki/Android_%28operating_system%29) kutoka Google), kila moja ikiwa na lugha, kanuni za usanifu, na duka lake. Huwezi tu kusafirisha sasisho wakati wowote upendao, kwa sababu duka hulipitia kwanza, na watumiaji huchagua lini kulisakinisha. Sura hii inajengwa juu ya uhandisi wa frontend (sura ya 5.6), misingi ya UX (sura ya 5.1), na ufikivu (sura ya 5.3), na inategemea usalama wa programu (sura ya 4.2) na CI/CD na utoaji (sura ya 8.1).

Umuhimu kwa mashirika makubwa na serikali ni mkubwa. Mashirika husafirisha programu za wateja na programu za ndani kwa wafanyakazi wao, mara nyingi zikisimamiwa kupitia [usimamizi wa vifaa vya simu](https://en.wikipedia.org/wiki/Mobile_device_management) (MDM: programu ya kati inayosanidi na kulinda vifaa vya kampuni). Serikali hujenga programu zinazomkabili raia kwa manufaa, afya, utambulisho, na malipo, na lazima zihudumie kila mtu, ikijumuisha watu wenye vifaa vya zamani na miunganisho ya polepole, chini ya sheria za ufikivu. Katika mazingira yote mawili, simu ni kujitolea kwa uzito, kwa muda mrefu, kwa hiyo ichukulie kwa ukali ule ule unaoupa mfumo mwingine wowote wa uzalishaji.

## Kanuni kuu

- Sanifu kwa kifaa: skrini ndogo, betri, na mtandao unaokuja na kuondoka.
- Dhania muunganisho wa mara kwa mara; fanya kazi nje ya mtandao kwanza na usawazishe unapoweza.
- Heshimu mikataba ya usanifu na mwingiliano ya kila jukwaa.
- Huwezi kudhibiti muda wa toleo; duka na mtumiaji ndio wanaodhibiti.
- Mgawanyiko ni wa kawaida; unga mkono wigo halisi wa vifaa na matoleo ya OS.
- Hifadhi data kwa usalama kwenye kifaa, kwa sababu vifaa hupotea na kuibiwa.
- Ufikivu ni sharti, si ung'arishaji wa mwisho.
- Chagua mbinu yako ya ujenzi kwa maisha yote ya programu, si siku ya uzinduzi tu.

## Mapendekezo

### Chagua mbinu ya ujenzi kwa makusudi

Kuna mbinu tatu pana, na kila moja inafaa mahitaji tofauti.

[Uendelezaji asilia](https://en.wikipedia.org/wiki/Mobile_app_development) unamaanisha kuandika kando kwa kila jukwaa kwa kutumia zana zake: Swift kwa iOS, Kotlin kwa Android. Unapata utendaji bora, ufikiaji kamili wa vipengele vya kifaa, na hisia mwaminifu zaidi ya jukwaa, kwa gharama ya kujenga na kudumisha misingi miwili ya msimbo.

[Mifumo ya majukwaa mtambuka](https://en.wikipedia.org/wiki/Cross-platform_software) huruhusu msingi mmoja wa msimbo kulenga majukwaa yote mawili. [React Native](https://en.wikipedia.org/wiki/React_Native) hutumia JavaScript na huonyesha vijenzi halisi vya asili. [Flutter](https://en.wikipedia.org/wiki/Flutter_%28software%29) hutumia lugha ya Dart na huchora wijeti zake yenyewe. Hizi hupunguza juhudi iliyorudiwa na zinaweza kuharakisha utoaji, lakini huongeza utegemezi kwa afya ya mfumo na zinaweza kubaki nyuma ya vipengele vipya zaidi vya jukwaa.

[Programu ya wavuti inayoendelea](https://en.wikipedia.org/wiki/Progressive_web_app) (PWA: tovuti inayoweza kusakinishwa na inayoweza kufanya kazi nje ya mtandao) haihitaji duka na husasishwa papo hapo, lakini ina ufikiaji mdogo wa baadhi ya vipengele vya kifaa na uwepo dhaifu zaidi kwenye skrini ya nyumbani.

Chagua kulingana na vipengele vya kifaa vinavyohitajika, wasifu wa utendaji, upeo wa matengenezo, ujuzi unaoweza kuajiri, na ufikiaji unaohitaji. Programu ya watumiaji ya utendaji wa juu inaweza kuhalalisha asilia. Programu ya maudhui-na-fomu yenye timu ndogo inaweza kufaa vizuri majukwaa mtambuka au PWA.

### Fuata miongozo ya usanifu ya jukwaa

Kila jukwaa lina mikataba ya kina iliyochapishwa. Apple inatoa [Human Interface Guidelines](https://en.wikipedia.org/wiki/Human_interface_guidelines), na Google inatoa [Material Design](https://en.wikipedia.org/wiki/Material_Design). Hizi zinashughulikia urambazaji, ishara, uchapaji, nafasi, na tabia za mfumo. Kuzifuata kunafanya programu yako ihisi inayojulikana, jambo linalopunguza juhudi ambayo watumiaji hutumia kuijifunza. Kuzipinga kunafanya programu ihisi ya kigeni na ya kutatiza. Msingi wa msimbo wa majukwaa mtambuka bado unahitaji kuheshimu mikataba ya kila jukwaa pale inapotofautiana, badala ya kulazimisha mwonekano wa jukwaa moja kwa jingine.

### Sanifu kwa vikwazo vya simu

Jenga nje-ya-mtandao-kwanza: acha kazi za msingi zifanye kazi bila muunganisho, hifadhi mabadiliko ndani ya kifaa, na usawazishe mtandao unaporudi. Shughulikia migongano kwa makini data ileile inapobadilika mahali pawili. Kuwa mwangalifu na betri na data: kusanya miito ya mtandao, epuka eneo la mara kwa mara au kazi ya nyuma, bana mizigo, na uheshimu mipangilio ya mtumiaji ya kuokoa data. Panga kwa mgawanyiko, mtawanyiko mpana wa ukubwa wa skrini, nguvu ya kifaa, na matoleo ya OS. Chagua wigo wa usaidizi kulingana na data halisi ya matumizi, na ujaribu kwenye vifaa vya wastani, si bora tu. Sanifu kwa skrini ndogo zenye daraja wazi, shabaha kubwa za kugusa, na maudhui yanayojirekebisha kwa ukubwa na mwelekeo tofauti.

### Panga usambazaji, matoleo, na masasisho

Kuchapisha kunapita kwenye [Apple App Store](https://en.wikipedia.org/wiki/App_Store_%28Apple%29) na [Google Play](https://en.wikipedia.org/wiki/Google_Play), kila moja ikiwa na michakato ya mapitio na sera zinazoweza kuchelewesha au kukataa toleo. Jenga muda wa mapitio ndani ya ratiba yako, na usome sera mapema. Kwa kuwa watumiaji huchagua lini kusasisha, daima utakuwa na matoleo mengi uwandani kwa wakati mmoja. Weka programu yako ikiendana nyuma na wateja wa zamani, na weka matoleo kwenye API zako (sura ya 2.3) ili programu ya zamani iendelee kufanya kazi. Toa njia ya kuhitaji sasisho unapolazimika, kwa mfano ombi la sasisho la lazima toleo linapokuwa si salama au halisaidiwi, na uitumie kwa uchache. Mashirika pia yanaweza kusambaza programu za ndani kupitia MDM au njia za faragha badala ya maduka ya umma.

### Tumia arifa za kusukuma na viungo vya kina kwa uangalifu

[Arifa za kusukuma](https://en.wikipedia.org/wiki/Push_technology) hukuruhusu kuwafikia watumiaji programu ikiwa imefungwa. Zitumie kwa thamani halisi, heshimu ridhaa ya mtumiaji na ruhusa za jukwaa, na epuka kelele, kwa sababu watu huzima arifa kutoka programu zinazopita mipaka. [Viungo vya kina](https://en.wikipedia.org/wiki/Deep_linking) humpeleka mtumiaji moja kwa moja kwenye skrini mahususi kutoka kiungo au arifa. Visanidi ili kiungo kifungue mahali sahihi kwenye programu, na kirudi kwa wavuti kwa neema programu isiposakinishwa.

### Linda programu na data yake

Chukulia kifaa kama kisichoaminika na kinachoweza kupotea. Hifadhi data nyeti kwenye hifadhi salama ya jukwaa ([iOS Keychain](https://en.wikipedia.org/wiki/Keychain_%28software%29) au Android Keystore), kamwe si kwenye faili wazi. Toa [uthibitishaji wa kibiometriki](https://en.wikipedia.org/wiki/Biometrics) (alama ya kidole au uso) kufungua vitendo nyeti, ukiungwa mkono na nenosiri la kufungua. Fikiria [kubandika vyeti](https://en.wikipedia.org/wiki/Public_key_pinning) (kukagua kwamba seva inawasilisha cheti kinachotarajiwa) kwa miunganisho ya thamani ya juu, na upange kuzungusha vyeti hivyo. Punguza unachohifadhi kwenye kifaa, linda siri, na ufuate mwongozo mpana katika usalama wa programu (sura ya 4.2).

### Jenga bomba halisi la majaribio na utoaji

Jaribu kwenye vifaa halisi, si [emulators](https://en.wikipedia.org/wiki/Emulator) na viigaji tu, kwa sababu maunzi, vihisi, na utendaji hutofautiana. Tumia maabara ya vifaa au shamba la vifaa vya wingu kufunika mtawanyiko wa uwakilishi wa mifano na matoleo ya OS. Otomatisha ujenzi, majaribio, kusaini, na uwasilishaji wa duka kupitia [ujumuishaji na utoaji endelevu](https://en.wikipedia.org/wiki/CI/CD) (sura ya 8.1), ikijumuisha usambazaji wa beta kwa wajaribu kabla ya toleo la umma. Kusimamia funguo za kusaini na vitambulisho vya duka kwa usalama ni sehemu ya bomba hili.

### Fanya ufikivu kuwa sharti

Unga mkono vipengele vya ufikivu vya kila jukwaa: visomaji skrini ([VoiceOver](https://en.wikipedia.org/wiki/VoiceOver) kwenye iOS, [TalkBack](https://en.wikipedia.org/wiki/Google_TalkBack) kwenye Android), ukubwa wa maandishi wa kidinamiki, utofautishaji wa rangi wa kutosha, na shabaha kubwa za kugusa. Weka lebo kwenye vidhibiti ili teknolojia saidizi iweze kuvielezea. Jaribu na zana halisi za usaidizi, si ukaguzi wa kiotomatiki tu. Kwa serikali hasa, ufikivu ni agizo la kisheria, na maelezo yako katika ufikivu (sura ya 5.3).

## Mabadilishano: faida na hasara

| Mbinu | Faida | Hasara |
|---|---|---|
| Asilia (Swift, Kotlin) | Utendaji bora, ufikiaji kamili wa kifaa, hisia ya kweli ya jukwaa | Misingi miwili ya msimbo, gharama ya juu, wafanyakazi zaidi |
| React Native | Msingi mmoja wa JavaScript, vijenzi halisi vya asili, marudio ya haraka | Utegemezi wa mfumo, ugumu wa daraja, kubaki nyuma kwa vipengele |
| Flutter | Msingi mmoja, UI thabiti, utendaji imara | Ujuzi wa Dart si wa kawaida, ukubwa mkubwa wa programu, mfano wake wa wijeti |
| Programu ya wavuti inayoendelea | Hakuna duka, masasisho ya papo hapo, msingi mmoja wa wavuti | Vipengele vichache vya kifaa, uwepo dhaifu, mipaka ya jukwaa |
| Masasisho ya lazima | Huondoa matoleo ya zamani yasiyo salama haraka | Huchosha watumiaji yakitumiwa kupita kiasi; yanaweza kuzuia ufikiaji |
| Kubandika vyeti | Ulinzi imara dhidi ya kunasa | Huvunjika vyeti vikizunguka bila masasisho ya programu |

Mabadilishano yanayojirudia ni ufikiaji na kasi ya utoaji dhidi ya kina na uaminifu. Asilia hutoa uzoefu tajiri na mwaminifu zaidi lakini unagharimu zaidi kujenga na kudumisha. Mbinu za majukwaa mtambuka na PWA huokoa juhudi na kupanua ufikiaji, kwa gharama fulani katika hisia ya jukwaa au ufikiaji wa kifaa. Kwa timu ndogo inayosafirisha fomu na maudhui, kushiriki msingi wa msimbo mara nyingi ni busara. Kwa programu ya watumiaji inayodai, kina cha asilia kinaweza kustahili bei. Amua ukiwa na maisha kamili ya programu mbele yako, si uzinduzi tu.

## Maswali ya kujadili na timu yako

1. **Tunaunga mkono wateja wa zamani uwandani kwa muda gani, na je, API yetu ina matoleo ili kuwaweka wakifanya kazi?** Kwa kuwa watumiaji huchagua lini kusasisha, daima una matoleo mengi ya programu yaliyosakinishwa kwa wakati mmoja, na badiliko la backend linalodhania kila mtu yuko wa sasa litavunja mkia mrefu wa wateja wa zamani. Amua dirisha lenu la upatanifu wa nyuma, weka matoleo kwenye API zenu ili programu ya zamani iendelee kufanya kazi, na uweke njia ya sasisho la lazima isiyotumika mara nyingi kwa matoleo ambayo si salama kweli. Hili ni muhimu kwa programu za raia za serikali na za wafanyakazi wa mashirika kwa pamoja, ambapo watu wenye vifaa vya zamani hawawezi au hawataki kusasisha kwa ratiba yenu. Leta data yenu ya sasa ya usambazaji wa matoleo na uliza nini kinavunjika kwa mteja wa zamani zaidi bado anayetumika kweli. Kama hamjui usambazaji huo, upime kabla hamjasafirisha badiliko lenu linalofuata la kuvunja.

2. **Kiwango chetu cha kutuma arifa ya kusukuma ni kipi, na nani anaamua nini kinastahili kumkatiza mtumiaji?** Arifa za kusukuma huwafikia watu programu ikiwa imefungwa, jambo linalozifanya zenye nguvu na rahisi kutumia vibaya, na watumiaji huzima arifa (au kufuta programu) kutoka bidhaa zinazopita mipaka. Kubaliana nini kinahesabika kama thamani halisi, jinsi watumiaji wanavyodhibiti mzunguko na njia, na jinsi mnavyoheshimu ridhaa ya jukwaa badala ya kusumbua kuomba ruhusa. Bila kiwango cha pamoja, kila timu yenye kipimo cha kutimiza itachukua arifa ya kusukuma, na njia nzima inashuka kuwa kelele. Leta arifa za mwezi uliopita mlizotuma na uliza ni zipi mtumiaji angekushukuru. Kama nyingi zilikuwa za kutangaza, kaza sera kabla kiwango cha kujiondoa hakijafanya hivyo.

3. **Bomba letu la utoaji wa simu ni halisi, likijumuisha kusaini, shamba la vifaa, na usambazaji wa beta, au toleo ni mbio za mkono zenye mkazo?** Simu inaongeza hatari ambazo wavuti haina: mapitio ya duka yanaweza kuchelewesha au kukataa toleo, funguo za kusaini na vitambulisho vya duka lazima vishughulikiwe kwa usalama, na maunzi na vihisi hutofautiana vya kutosha kwa emulators kuficha matatizo halisi. Kuotomatisha ujenzi, majaribio, kusaini, na uwasilishaji wa duka kupitia CI/CD, kwa usambazaji wa beta kwa wajaribu na shamba la vifaa vya wingu linalofunika mifano watumiaji wenu wanayobeba kweli, ndiko kunakogeuza matoleo kutoka ushujaa kuwa utaratibu. Amua nani anamiliki bomba na funguo za kusaini, na jinsi muda wa mapitio ya duka unavyojengwa ndani ya kila mpango wa toleo. Leta hadithi ya toleo lenu la mwisho na uhesabu hatua za mkono. Kila moja ni mahali toleo lenye mkazo linaweza kwenda vibaya chini ya tarehe ya mwisho.

4. **Tumechagua asilia, majukwaa mtambuka, au programu ya wavuti inayoendelea kwa maisha yote ya bidhaa hii, au kwa siku ya uzinduzi tu?** Mbinu ya ujenzi ndio kiegemeo kikubwa zaidi cha gharama na uwezo wa programu ya simu kwa miaka, na uchaguzi uliofanywa kusafirisha haraka unaweza kukunasa: asilia hununua ufikiaji tajiri zaidi wa kifaa na hisia ya jukwaa kwa bei ya misingi miwili ya msimbo na seti mbili za ujuzi, wakati majukwaa mtambuka na PWA hushiriki msimbo lakini huongeza utegemezi wa mfumo au kupoteza ufikiaji wa baadhi ya vipengele vya kifaa. Kwa timu kubwa, uamuzi huu unaendesha uajiri, bajeti ya matengenezo, na kasi unayoweza kupokea kila toleo la mwaka la OS, kwa hiyo unastahili mmiliki wazi badala ya chaguo-msingi lililowekwa na yeyote aliyeandika mfano wa kwanza. Leta vipengele vya kifaa vinavyohitajika, wasifu wa utendaji, upeo wa matengenezo, na ujuzi mnaoweza kuajiri kweli, na muwe waaminifu kuhusu vipengele vipi vya jukwaa mngepoteza chini ya kila chaguo. Katika mazingira ya mashirika makubwa na serikali, pima kama programu ni kujitolea kwa muda mrefu kunakopaswa kuokoka mabadiliko ya wafanyakazi na muongo wa mabadiliko ya jukwaa, na rekodi uamuzi na sababu zake ili timu ya baadaye isibaki ikibahatisha kwa nini msingi wa msimbo unaonekana ulivyo.

5. **Wigo gani wa usaidizi wa vifaa na toleo la OS watumiaji wetu halisi wanahitaji, na je, tunajaribu kwenye maunzi wanayobeba kweli badala ya simu zilizo kwenye meza zetu?** Mgawanyiko ni hali ya kawaida ya simu: watumiaji wanaenea kuvuka mtawanyiko mpana wa ukubwa wa skrini, nguvu ya kifaa, na matoleo ya OS, na programu iliyorekebishwa kwenye simu bora za timu itasafirishwa polepole au iliyovunjika kwenye maunzi ya wastani ambayo sehemu kubwa ya hadhira yenu inamiliki. Kuweka wigo wa usaidizi ni mabadilishano kati ya ufikiaji na juhudi, kwa sababu kila mfano wa zamani na toleo la OS unaloahidi kuunga mkono linapanua matriki ya majaribio na mzigo wa matengenezo, kwa hiyo wigo lazima utoke kwenye data halisi ya matumizi badala ya dhana. Leta usambazaji wenu wa vifaa na matoleo ya OS, mifano ambayo shamba la vifaa vya wingu au maabara inafunika sasa, na utendaji mliopima kwenye maunzi ya kiwango cha chini, si viigaji tu. Kwa programu za raia za serikali hili ni karibu lisilojadilika, kwa sababu lazima uhudumie kila mtu ikijumuisha watu wenye vifaa vya zamani na miunganisho ya polepole chini ya wajibu wa ufikivu, na kwa meli za mashirika mnapaswa kujaribu simu hasa za kustahimili ambazo wafanyakazi wanabeba badala ya sampuli ya jumla.

6. **Data nyeti gani inaishi kwenye kifaa, na je, kila kipande kimelindwa dhidi ya simu iliyopotea, kuibiwa, au mikononi mwa mtu mwingine?** Kifaa cha simu husafiri mfukoni na hupotea au kuibiwa, kwa hiyo data au siri yoyote iliyohifadhiwa kwenye faili wazi iko simu moja iliyopotea mbali na kufichuka, na eneo la mlipuko hukua kwa kila mtumiaji. Mazingatio yanavutana: kuweka data kwenye kache ya kifaa ndiko kunakofanya nje-ya-mtandao-kwanza kufanya kazi na kuweka programu haraka, hata hivyo kila kipengele kilichowekwa kwenye kache ni dhima inayopaswa kukaa kwenye hifadhi salama ya jukwaa (iOS Keychain au Android Keystore), kupunguzwa, na ikiwezekana kufungwa nyuma ya kibiometriki au nenosiri. Leta orodha ya hasa kile programu inahifadhi ndani, mahali kila kipengele kimehifadhiwa, nini kinakifungua, na kama miunganisho ya thamani ya juu inatumia kubandika vyeti kwa mpango wa kuzungusha unaowezekana. Katika mazingira ya mashirika, funga hili na sera ya usimamizi wa vifaa vya simu na kufuta kwa mbali, na katika serikali chukulia data binafsi ya kwenye kifaa kama mfiduo wa faragha na wa kisheria unaopaswa kuhalalishwa, kuandikwa, na kutetewa chini ya ukaguzi.

## Mtazamo wa sekta

**Kampuni changa.** Ukiwa na timu ndogo na muda mfupi wa fedha, mara chache unaweza kumudu misingi miwili ya asili au seti mbili za ujuzi, kwa hiyo mfumo wa majukwaa mtambuka au hata PWA inayofikia maduka yote mawili kutoka msingi mmoja kwa kawaida hushinda. Safirisha nje-ya-mtandao-kwanza kwa kazi moja ya msingi inayojalisha, weka tokeni yoyote kwenye hifadhi salama badala ya faili wazi, na ujenge muda wa mapitio ya duka ndani ya kila toleo ili kukataliwa kusivunje tarehe ya uzinduzi. Ruka masasisho ya lazima, kubandika vyeti, na shamba la vifaa hadi matumizi halisi yahalalishe.

**Biashara ndogo.** Bila mtaalamu maalumu wa simu na bajeti finyu, egemea sana kununua kuliko kujenga: kijenzi cha programu kisicho na msimbo, programu ya chapa-nyeupe kutoka kwa muuzaji wako wa mauzo au miadi, au PWA iliyotengenezwa vizuri kutoka tovuti yako iliyopo mara nyingi hushinda programu ya kipekee usiyoweza kuidumisha. Ukiagiza programu, miliki funguo za kusaini na akaunti za duka mwenyewe ili mkandarasi asishikilie uwepo wako mateka, na dai ufikivu na hifadhi salama ya kwenye kifaa kwenye mkataba. Weka wigo kwenye kazi moja au mbili ambazo wateja wanazifanya kweli kwenye simu.

**Biashara kubwa.** Kwa ukubwa, programu ni kujitolea kwa muda mrefu kuvuka timu nyingi, kwa hiyo sawazisha mbinu ya ujenzi, mfumo wa hifadhi salama, bomba la CI/CD, na sera ya matoleo ya API badala ya kuacha kila bidhaa ibuni upya. Programu za wafanyakazi wa ndani kwa kawaida hupita kwenye usimamizi wa vifaa vya simu kwa usakinishaji, usanidi, kufuta kwa mbali, na sera, wakati programu za wateja zinahitaji shamba la vifaa linalofunika matumizi halisi na ufikivu na usalama unaokaguliwa. Tawala funguo za kusaini, vitambulisho vya duka, na muda wa toleo kati ili badiliko la backend linalovunja lisiwaache wateja wa zamani mkia mrefu.

**Serikali.** Kanuni za ununuzi, uwazi, na uwajibikaji wa umma huumba kila uchaguzi. Lazima uhudumie kila mtu, ikijumuisha watu wenye vifaa vya zamani na miunganisho ya polepole, kwa hiyo ufikivu ni agizo la kisheria linalothibitishwa na zana halisi za usaidizi, na wigo mpana wa usaidizi wa vifaa ni karibu usiojadilika. Pendelea mbinu na mikataba inayoepuka kufungwa kwa muuzaji, weka data ikihamishika, na uruhusu umma kukagua programu inafanya nini na data yao, na chukulia data binafsi ya kwenye kifaa kama mfiduo unaopaswa kuhalalisha na kuandika chini ya ukaguzi.

## Mifano

**Kampuni changa.** Kampuni changa ya watu watatu inayojenga programu ya kufuatilia tabia ilihitaji kufikia iOS na Android lakini haikuweza kumudu misingi miwili ya asilia au seti mbili za ujuzi. Walichagua mfumo wa majukwaa mtambuka ili timu moja ndogo isafirishe kwenye maduka yote mawili, na kusanifu nje-ya-mtandao-kwanza tangu mwanzo ili mtumiaji aweze kurekodi tabia kwenye treni ya chini ya ardhi bila mawimbi na kusawazisha baadaye. Waliweka tokeni ya kuingia kwenye hifadhi salama ya jukwaa badala ya faili wazi, walijenga muda wa mapitio ya duka ndani ya kila mpango wa toleo, na kujaribu kwenye simu chache za bei nafuu za zamani kando ya zao, jambo lililonasa utendaji wa polepole ambao vinginevyo wangeusafirisha.

**Biashara kubwa.** Kampuni ya usafirishaji ilijenga programu ya ndani kwa madereva wake na wafanyakazi wa ghala. Kwa kuwa maghala na njia za uwasilishaji zina mawimbi yenye hitilafu, timu ilichagua usanifu wa nje-ya-mtandao-kwanza: skani na masasisho ya hali huhifadhiwa ndani na kusawazishwa muunganisho unaporudi. Walitumia mfumo wa majukwaa mtambuka kuhudumia msingi mmoja wa msimbo kwa majukwaa yote mawili na timu ndogo. Programu inasambazwa kupitia usimamizi wa vifaa vya simu badala ya maduka ya umma, ili IT idhibiti usakinishaji, usanidi, na sera ya usalama kwenye vifaa vya kampuni. Vitambulisho nyeti vinaishi kwenye hifadhi salama ya jukwaa, na kibiometriki hufungua programu. Shamba la vifaa vya wingu hujaribu mtawanyiko wa uwakilishi wa simu za kustahimili ambazo wafanyakazi wanabeba kweli.

**Serikali.** Wakala wa kitaifa ulisafirisha programu inayomkabili raia kwa utambulisho na manufaa. Ufikivu ulikuwa sharti gumu tangu siku ya kwanza: usaidizi kamili wa kisomaji skrini, ukubwa wa maandishi wa kidinamiki, na utofautishaji imara, ukijaribiwa na zana halisi za usaidizi kutimiza sheria. Kwa kuwa raia hutumia wigo mkubwa wa vifaa, timu iliunga mkono bendi pana ya mifano ya zamani na miunganisho ya polepole, na kuweka kazi za msingi zikifanya kazi nje ya mtandao. Data nyeti inabaki kwenye hifadhi salama ya kifaa, kibiometriki hulinda ufikiaji, na miunganisho ya thamani ya juu inatumia kubandika vyeti kwa mchakato uliopangwa wa kuzungusha. Matoleo ya API huweka programu za zamani zilizosakinishwa zikifanya kazi, na njia ya sasisho la lazima isiyotumika mara nyingi ipo kwa marekebisho ya usalama. Ratiba za mapitio ya duka zimejengwa ndani ya kila mpango wa toleo.

## Kesi ya biashara: sababu, ROI, na TCO

Simu ndipo watumiaji wengi wanapokutana na huduma yako, kwa hiyo programu huathiri upokeaji, kuridhika, na ukamilishaji wa kazi zinazojalisha kwa shirika lako. Programu ya haraka, ya kutegemewa, iliyosanifiwa vizuri huongeza matumizi na kupunguza mzigo wa msaada. Kwa mashirika, programu ya ndani ya simu inaweza kufanya wafanyakazi wanaotembea kuwa na tija zaidi kwa kupimika na kupunguza makaratasi. Kwa serikali, programu ya raia inayotumika hupanua ufikiaji na kupunguza mahitaji ya kituo cha simu na ya ana kwa ana.

Kwenye jumla ya gharama ya umiliki (TCO), uchaguzi wa mbinu ndio kiegemeo kikubwa zaidi. Asilia inamaanisha kulipia misingi miwili ya msimbo na seti mbili za ujuzi kwa maisha yote ya programu. Majukwaa mtambuka hubadilisha sehemu ya hilo kwa utegemezi lazima uuweke wa sasa. Zaidi ya msimbo, weka bajeti ya ada za duka na mizunguko ya mapitio, maabara ya majaribio ya vifaa au shamba la wingu, usaidizi endelevu wa toleo la OS majukwaa yanapotoa kila mwaka, na kazi ya usalama ambayo simu inadai. Gharama ya kuwekeza kidogo huonekana kama kuanguka kwenye vifaa visivyoungwa mkono, matukio ya usalama kutoka data isiyolindwa ya kwenye kifaa, matoleo yaliyokataliwa au kuchelewa, na watumiaji wanaoacha programu ya polepole au ya kutatiza.

Kuweka kesi kwa uongozi, unganisha programu na matokeo madhubuti: ukamilishaji wa kazi, ubakizaji, tija ya wafanyakazi, au gharama ya msaada iliyopungua. Pima uamuzi wa mbinu kamili kuvuka maisha ya programu, si toleo la kwanza tu, na taja hatari (usalama, sheria ya ufikivu, kukataliwa na duka) ambazo mazoea mazito ya simu hupunguza.

## Mifumo mibaya na mitego

- **Kuchukulia simu kama tovuti iliyopunguzwa**: kupuuza kugusa, ishara, na mikataba ya jukwaa.
- **Kudhania mtandao kamili**: hakuna ushughulikiaji wa nje ya mtandao, kwa hiyo programu inavunjika mawimbi yanaposhuka.
- **Kujaribu kwenye simu bora ya hivi karibuni tu**: kuficha utendaji duni kwenye vifaa ambavyo watumiaji halisi wanabeba.
- **Kuhifadhi siri kwenye faili wazi**: data nyeti inafichuka kifaa kinapopotea au kuibiwa.
- **Kufurika kwa arifa**: arifa nyingi mno, kwa hiyo watumiaji wanazinyamazisha au kufuta programu.
- **Kupuuza muda wa mapitio ya duka**: mipango ya toleo inayodhania uchapishaji wa papo hapo kisha inateleza.
- **Hakuna njia ya sasisho la lazima**: matoleo ya zamani yasiyo salama yanaendelea kuishi bila njia ya kuyastaafisha.
- **Kumaliza betri na data**: kazi ya nyuma ya mara kwa mara na mtandao wenye mazungumzo mengi ambayo watumiaji wanaona.
- **Ufikivu kama wazo la baadaye**: kuwatenga watumiaji na, kwa serikali, kuvunja sheria.
- **Msingi mmoja wa msimbo ukilazimishwa kuonekana sawa kila mahali**: programu inayohisi ya kigeni kwenye majukwaa yote mawili.

## Kielelezo cha ukomavu

**Ngazi ya 1: Kuanzisha.** Simu ni ya papo hapo na ya kuitikia. Programu inajengwa kama tovuti, inajaribiwa kwenye simu za timu yenyewe, na mara nyingi inavunjika nje ya mtandao. Fikra kidogo hutolewa kwa hifadhi salama, ufikivu, au ratiba za mapitio ya duka. Matoleo ni mbio za mkono zenye mkazo, na hakuna anayemiliki mbinu ya ujenzi wala funguo za kusaini.

**Ngazi ya 2: Kuendeleza.** Mazoea ya msingi yanaonekana, lakini hayana uthabiti kuvuka timu na bidhaa. Mbinu ya ujenzi imechaguliwa kwa programu fulani, inafuata misingi ya jukwaa na inajaribiwa kwenye vifaa vichache halisi, na ushughulikiaji fulani wa nje ya mtandao na hifadhi salama upo. Ujenzi umeotomatishwa kwa sehemu na mtu anamiliki uwasilishaji wa duka, hata hivyo programu ya timu nyingine inaweza bado kufanya yote haya tofauti au kutofanya kabisa.

**Ngazi ya 3: Kusawazisha.** Mazoea mazuri yameandikwa na kutekelezwa shirika zima. Nje-ya-mtandao-kwanza ndiyo chaguo-msingi, wigo ulioandikwa wa usaidizi wa vifaa unajaribiwa kwenye maabara ya vifaa au shamba la wingu, na miongozo ya usanifu ya jukwaa na ufikivu inafuatwa na kuthibitishwa kwa zana halisi za usaidizi. Hifadhi salama, kibiometriki, na matoleo ya API ni kiwango, CI/CD huotomatisha ujenzi, majaribio, kusaini, na usambazaji wa beta, na muda wa mapitio ya duka umepangwa ndani ya kila toleo.

**Ngazi ya 4: Kusimamia.** Ubora wa simu unapimwa na kudhibitiwa dhidi ya vipimo vya msingi. Kuanguka, utendaji wa kuanza baridi na uonyeshaji wa skrini, matumizi ya betri na data, na viwango vya ukamilishaji wa kazi vinanaswa mfululizo kutoka vifaa halisi na kufuatiliwa dhidi ya malengo, vikiwa na mgawanyo kwa mfano na toleo la OS ili regression kwenye maunzi ya kiwango cha chini inaswe, isisafirishwe. Ufikivu na usalama vinakaguliwa badala ya kudhaniwa, viwango vya kujiondoa kwenye arifa na upokeaji wa masasisho vinafuatiliwa, na wigo wa usaidizi na mbinu ya ujenzi vinapitiwa kwa ushahidi huu. Maamuzi ya kuua au kurekebisha toleo yanategemea vipimo, si jinsi programu ilivyohisi kwenye simu ya kiongozi.

**Ngazi ya 5: Kuratibu.** Simu inaboreshwa mfululizo na kuunganishwa kuvuka shirika, na inajirekebisha mandhari ya vifaa inapohama. Kuzungusha vyeti, njia za sasisho la lazima, na kurudisha nyuma ni utaratibu, wigo wa usaidizi na mbinu ya ujenzi vinapanuliwa upya kwa ushahidi majukwaa yanapotoa kila mwaka, na mtawanyiko mzima wa watumiaji na vifaa unachukuliwa kama wa daraja la kwanza. Upangaji wa simu umeunganishwa na usalama, ufikivu, API, na mazoea ya utoaji, kwa hiyo badiliko la OS, daraja jipya la kifaa, au mabadiliko ya sera hufyonzwa kama kazi ya kawaida badala ya dharura.

## Mawazo ya kujadili

- Mnaamuaje kati ya asilia, majukwaa mtambuka, na programu ya wavuti inayoendelea kwa bidhaa fulani?
- Wigo gani wa usaidizi wa vifaa na toleo la OS unafaa data yenu halisi ya watumiaji, na mnaiweka ya sasa vipi?
- Nje-ya-mtandao-kwanza ni muhimu wapi katika programu yenu, na mtashughulikiaje migongano ya usawazishaji?
- Sasisho la lazima linahalalishwa lini, na mnaepukaje kuwazuia watumiaji isivyo haki?
- Mtajaribuje kwenye vifaa halisi kwa ukubwa unaoakisi watumiaji wenu?
- Data nyeti gani inaishi kwenye kifaa, na kila kipande kinalindwa vipi?
- Mnaheshimuje mikataba ya kila jukwaa kutoka msingi wa msimbo wa pamoja?

## Mambo muhimu ya kukumbuka

- Chagua mbinu ya ujenzi (asilia, majukwaa mtambuka, au PWA) kwa maisha yote ya programu.
- Fuata miongozo ya usanifu ya jukwaa ili programu ihisi inayojulikana na kupunguza juhudi ya mtumiaji.
- Sanifu kwa vikwazo vya simu: nje-ya-mtandao-kwanza, betri na data kwa uangalifu, mgawanyiko, skrini ndogo.
- Huwezi kudhibiti muda wa toleo; panga kwa mapitio ya duka, matoleo, na masasisho ya lazima.
- Tumia arifa za kusukuma na viungo vya kina kwa uangalifu na ridhaa.
- Linda data ya kwenye kifaa kwa hifadhi salama, kibiometriki, na, pale panapostahili, kubandika vyeti.
- Jaribu kwenye vifaa halisi na uotomatishe bomba la simu kupitia CI/CD.
- Fanya ufikivu kuwa sharti, ambalo kwa serikali ni agizo la kisheria.

## Marejeo na usomaji zaidi

- Apple, *Human Interface Guidelines*
- Google, *Material Design* guidelines
- Apple, *App Store Review Guidelines*
- Google, *Google Play developer policies and Android developer documentation*
- OWASP, *Mobile Application Security Verification Standard (MASVS)* and *Mobile Security Testing Guide*
- React Native project documentation
- Flutter project documentation
- Google, *web.dev* guidance on progressive web apps
- U.S. Section 508 and WCAG (Web Content Accessibility Guidelines) references for mobile accessibility
- NIST, *Guidelines on mobile device security and management*
