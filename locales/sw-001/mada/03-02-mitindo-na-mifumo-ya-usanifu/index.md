# 3.2 Mitindo na mifumo ya usanifu

## Muhtasari na msukumo

Mtindo wa usanifu ni umbo pana, linaloweza kutumika tena la kupanga mfumo: unavyogawanywa, sehemu zinavyowasiliana, na mipaka inapoangukia. Kuchagua mmoja ni miongoni mwa maamuzi yenye matokeo makubwa zaidi (na yanayoeleweka vibaya zaidi) ambayo shirika kubwa hufanya. Mara nyingi uchaguzi hufuata mtindo ("kila mtu anafanya [huduma ndogo](https://en.wikipedia.org/wiki/Microservices)") badala ya vikwazo halisi vya timu, kikoa, na uhalisia wa uendeshaji. Unaishia na mkanganyiko mmoja kati ya miwili: mfumo uliosambazwa ambao shirika haliwezi kuuendesha, au [monolith](https://en.wikipedia.org/wiki/Monolithic_application) iliyochanganyika ambayo hakuna anayeweza kuibadilisha kwa usalama. Hakuna kati ya hivyo ni kosa la mtindo. Vyote vinatokana na kulinganisha mtindo vibaya na hali.

Kwa timu kubwa za wasanidi, mitindo ni muhimu zaidi ya yote kwa sababu ya [Sheria ya Conway](https://en.wikipedia.org/wiki/Conway%27s_law): muundo wa mfumo huelekea kuakisi muundo wa mawasiliano wa shirika linaloujenga. Kwa hiyo mtindo wa usanifu pia ni uamuzi wa muundo wa shirika. Kugawanya mfumo kuwa huduma kwa kweli ni uamuzi wa kugawanya timu, umiliki, na wajibu wa zamu. Mashirika yenye mamia ya wahandisi yanaweza kumudu (na mara nyingi yanahitaji) huduma ndogo sana zenye usambazaji huru, kwa sababu uhuru huo ndio jinsi timu nyingi zinavyosafirisha bila kuzuiana. Lazimisha muundo ule ule kwa timu moja ndogo, na inarithi kodi yote ya uendeshaji bila faida yoyote ya kishirika.

Mazingira ya serikali na mashirika makubwa yanaongeza vikwazo zaidi: maisha marefu ya mifumo, udhibiti mkali wa mabadiliko, mizunguko ya ununuzi, uunganishaji na mifumo ya rekodi iliyoimarika, na uwezo wa kukaguliwa. Haya yanapendelea mitindo inayoweka mipaka wazi na utegemezi rahisi kukagua. Sura hii inachunguza mitindo mikuu: monolith hadi huduma ndogo, [usanifu unaoendeshwa na matukio](https://en.wikipedia.org/wiki/Event-driven_architecture) wenye [CQRS](https://en.wikipedia.org/wiki/Command_Query_Responsibility_Segregation) na event sourcing, mifumo ya [mesh ya huduma](https://en.wikipedia.org/wiki/Service_mesh) na lango, [serverless](https://en.wikipedia.org/wiki/Serverless_computing), na nidhamu za ndani za usanifu wa [hexagonal](https://en.wikipedia.org/wiki/Hexagonal_architecture_(software)) na safi. Muhimu zaidi, inakusaidia kujua lini kila mmoja unafaa.

*Angalia pia:* sura ya 2.2 (kanuni za usanifu wa programu, ikijumuisha [Domain-Driven Design](https://en.wikipedia.org/wiki/Domain-driven_design)), sura ya 3.1 (misingi ya usanifu), na sura ya 3.3 (mifumo iliyosambazwa).

## Kanuni kuu

- **Mtindo hufuata nguvu, si mitindo ya wakati.** Chagua kulingana na ukubwa wa timu, ugumu wa kikoa, mzigo, na ukomavu wa uendeshaji, kamwe si kwa sababu teknolojia ni maarufu.
- **Uunganishaji ndio adui halisi, si idadi ya vitu vinavyosambazwa.** Monolith iliyogawanywa vizuri kwa moduli hushinda donge kubwa la matope lililosambazwa.
- **Usambazaji ni gharama unayoilipa kwa uhuru.** Gawanya tu pale thamani ya usambazaji huru, ukubwa, au kutenga kushindwa inapozidi gharama ya miito ya mtandao, kushindwa kwa sehemu, na uthabiti wa data kuvuka huduma.
- **Mipaka inapaswa kufuata kikoa cha biashara.** Pangilia huduma na moduli na miktadha iliyofungwa (kila mmoja ni kielelezo cha kikoa kinachojitegemea chenye mpaka wake wazi), si tabaka za kiufundi.
- **Buni ndani vizuri bila kujali nje.** Tabaka za hexagonal/safi huweka mantiki ya biashara huru kutoka mifumo ya kazi na miundombinu katika kila mtindo.
- **Sheria ya Conway haikwepeki, kwa hiyo itumie.** Buni mipaka ya timu na usanifu pamoja.
- **Anza rahisi kuliko unavyodhani unahitaji.** Unaweza kutoa huduma kutoka monolith nzuri ya moduli; kuondoa usambazaji wa fujo ya huduma ndogo ya mapema ni vigumu zaidi sana.

## Mapendekezo

### Chaguo-msingi ni monolith ya moduli; gawanya kwa ushahidi

Anza mifumo mingi kama kitengo kimoja kinachosambazwa chenye mipaka imara ya ndani ya moduli: violesura wazi, hakuna kufikia data ya moduli nyingine, na kanuni za utegemezi zinazotekelezwa. Unapata miamala rahisi, urekebishaji wa muundo rahisi, na kitu kimoja cha kusambaza na kuona. Gawanya moduli kuwa huduma yake yenyewe tu ukiwa na sababu madhubuti: sehemu inayopaswa kupanuka peke yake, timu inayohitaji kusambaza kwa mzunguko wake, eneo la kushindwa unalopaswa kulitenga, au hitaji la teknolojia linalotofautiana na mengine. Ukigawanya, gawanya kwa mistari ya miktadha iliyofungwa ili kila huduma imiliki data yake na kufichua mkataba thabiti.

### Jua lini huduma ndogo zinastahili

Huduma ndogo zinakupa usambazaji huru, ukubwa huru, kutengwa kwa kushindwa, na uhuru wa kuchanganya teknolojia. Kwa kurudi zinadai CI/CD iliyokomaa (ujumuishaji na utoaji endelevu), miundombinu ya kiotomatiki, ufuatiliaji uliosambazwa, ugunduzi wa huduma, na utamaduni wa zamu. Jiulize kwa uaminifu: shirika lako linaweza kuendesha huduma kadhaa zinazosambazwa kwa kujitegemea kwenye uzalishaji kwa uhakika? Jukwaa na ukomavu wa uendeshaji usipokuwepo, huduma ndogo zinazidisha njia zako za kushindwa bila kutoa faida zake. Mashirika mengi hufanya vizuri zaidi na huduma chache kubwa zilizopangwa kulingana na vikoa vikuu badala ya kundi la ndogo ndogo.

### Tumia usanifu unaoendeshwa na matukio pale kutenganisha na kutokuwa papo hapo kunapolipa

Usanifu unaoendeshwa na matukio huruhusu wazalishaji kutoa ukweli bila kujua nani anatumia. Hilo linakununulia uunganishaji legevu, bafa kwa kilele cha mzigo, na njia rahisi ya kuongeza watumiaji wapya. Utumie pale mtiririko wa kazi kwa asili sio wa papo hapo na unaitikia. **CQRS** (Command Query Responsibility Segregation) hutenganisha kielelezo cha kuandika na kimoja au zaidi cha kusoma, jambo linalosaidia pale mizigo au maumbo ya kusoma na kuandika yanapotofautiana sana. **Event sourcing** huhifadhi hali kama kumbukumbu ya matukio ya kuongeza tu badala ya hali ya sasa, ikikupa njia kamilifu ya ukaguzi na kusafiri nyuma kwa wakati. Hilo lina nguvu kwa fedha na serikali, ambapo "tulifikaje kwenye thamani hii?" ni swali la kisheria, lakini linaongeza ugumu halisi katika kuweka matoleo ya matukio, kujenga upya makadirio, na kufikiri kuhusu uthabiti wa mwisho. Zifikie kwa makusudi, si kwa chaguo-msingi.

### Tumia mifumo ya lango, BFF, na mesh kusimamia huduma nyingi

**Lango la API** linawapa wateja wa nje mlango mmoja wa kuingia, likishughulikia uthibitishaji, kikomo cha kasi, uelekezaji, na kukomesha [TLS](https://en.wikipedia.org/wiki/Transport_Layer_Security) (Transport Layer Security). **Backend-for-Frontend (BFF)** humpa kila aina ya mteja (wavuti, simu, API ya mshirika) safu yake ya uunganishaji iliyoundwa mahususi, ili uepuke API iliyovimba ya ukubwa mmoja kwa wote. **Mesh ya huduma** huhamisha masuala ya kuvuka sehemu (TLS ya pande zote, kujaribu upya, muda wa kuisha, kuhamisha trafiki, na telemetri) kwenye safu ya miundombinu ya sidecar, ili timu za programu zisilazimike kuyatekeleza upya. Ongeza mesh pale tu idadi ya huduma inapofanya kushughulikia masuala haya kwa kila huduma kutosimamika. Kwa huduma chache, mesh ni mzigo wa uendeshaji zaidi ya inavyostahili.

### Pima serverless kwa uaminifu

Kazi-kama-huduma na majukwaa ya serverless yanayosimamiwa huondoa usimamizi wa seva mezani pako, hupanuka hadi sifuri, na hutozwa kwa matumizi, jambo zuri kwa mizigo yenye mawimbi, inayoendeshwa na matukio, au yenye msingi wa chini na kwa timu ndogo. Mabadilishano ni halisi: ucheleweshaji wa kuanza baridi, mipaka ya muda wa utekelezaji na rasilimali, majaribio ya ndani magumu zaidi, uwezekano wa kufungwa na muuzaji, na gharama inayoweza kuzidi miundombinu iliyopangwa kwa kiasi cha juu endelevu. Tumia serverless pale uchumi wake na urahisi wa uendeshaji vinashinda wazi. Usilazimishe mifumo ya msingi thabiti, ya uwezo wa juu wa kupitisha ndani yake kwa shauku.

### Weka mantiki ya biashara safi ndani ya kila huduma

Mtindo wowote wa nje, weka ndani safi kwa **hexagonal (bandari na adapta)** au **usanifu safi**: kanuni za biashara katikati, zikitegemea dhana tu; mifumo ya kazi, hifadhidata, na ujumbe kwenye kingo kama adapta zinazoweza kubadilishwa. Hii huweka mantiki yako muhimu ya kikoa ikijaribika bila miundombinu na ikihamishika kuvuka mabadiliko ya teknolojia: faida ya maamuzi kwa mifumo ya serikali na mashirika makubwa ya muda mrefu itakayodumu kuliko vizazi kadhaa vya mifumo ya kazi.

## Mabadilishano: faida na hasara

| Mtindo | Bora pale | Faida | Hasara |
|---|---|---|---|
| Monolith ya moduli | Mifumo mingi, hasa mapema | Uendeshaji rahisi, miamala na urekebishaji wa muundo rahisi | Kitengo kimoja cha usambazaji; hupanuka kama kimoja; hatari ya mmomonyoko |
| Huduma ndogo | Timu nyingi, ukubwa wa juu, jukwaa lililokomaa | Usambazaji/ukubwa huru, kutengwa kwa kushindwa | Ugumu uliosambazwa, uthabiti wa data, gharama kubwa ya uendeshaji |
| Inayoendeshwa na matukio / CQRS / event sourcing | Mtiririko usio wa papo hapo, mahitaji ya ukaguzi, kusoma/kuandika kunakotofautiana | Uunganishaji legevu, uwezo wa kukaguliwa, usomaji unaopanuka | Uthabiti wa mwisho, matoleo ya matukio, utatuzi mgumu zaidi |
| Serverless | Kazi yenye mawimbi au ya msingi wa chini, inayoendeshwa na matukio | Hakuna usimamizi wa seva, hupanuka hadi sifuri, kulipa kwa matumizi | Kuanza baridi, mipaka, kufungwa, gharama kwa mzigo thabiti wa juu |

Mada inayojirudia: unanunua unyumbufu na uhuru kwa ugumu wa uendeshaji na wa kiakili. Mitindo iliyosambazwa na inayoendeshwa na matukio huacha urahisi wa safu moja ya miito na muamala mmoja kwa kubadilishana na uwezo wa kupanuka, kusambaza, na kushindwa kwa kujitegemea. Biashara hiyo inalipa kwa ukubwa na kwa jukwaa lililokomaa. Bila hivyo, ni maangamizi. Nidhamu za ndani (hexagonal/safi) karibu daima zinastahili, kwa sababu zinagharimu kidogo na kuweka chaguo zako wazi za kubadilisha mitindo baadaye.

## Maswali ya kujadili na timu yako

1. **Kabla ya kugawanya huduma ijayo, mtagawanya pia timu inayoimiliki, na nani ana mamlaka ya kufanya hivyo?** Sheria ya Conway inamaanisha mpaka wa huduma ni mpaka wa timu kwa kweli, kwa hiyo mgawanyo ambao chati ya shirika hauuungi mkono huzalisha monolith iliyosambazwa: vitu viwili vinavyosambazwa, treni moja ya toleo, zamu ya pamoja. Katika shirika kubwa mamlaka ya kuumba upya timu kwa kawaida yako juu ya uhandisi, kwa mistari ya kuripoti, fedha, na rasilimali watu, ndiyo maana usanifu na muundo wa shirika lazima viamuliwe pamoja. Leta ushahidi kwenye mjadala: huduma inayopendekezwa ina timu inayoweza kuimiliki mwanzo hadi mwisho, kuajiri zamu yake, na kusambaza kwa mzunguko wake? Jibu likiwa hapana, ama fadhili timu au weka uwezo huo kama moduli kwenye monolith. Kugawanya msimbo bila kugawanya umiliki kunakununulia kila gharama ya usambazaji na hakuna uhuru.

2. **Mnaweza kusambaza kila huduma yenu kwa kujitegemea leo, au zinasafirishwa kwa siri kwa pamoja?** Monolith iliyosambazwa ndilo tokeo baya zaidi katika sura hii: unalipia miito ya mtandao, kushindwa kwa sehemu, na uthabiti wa data kuvuka huduma, lakini bado huwezi kutoa moja bila nyingine. Ishara dhahiri ni hifadhidata ya pamoja, maktaba ya pamoja inayolazimisha masasisho yaliyoratibiwa, na majaribio ya uunganishaji yanayopaswa kuendesha eneo zima pamoja. Kwa timu kubwa hili hudhibiti kimyakimya uwezo wa kupitisha, kwa sababu kila timu inasubiri kwenye toleo moja ingawa mchoro unaonyesha uhuru. Chukua badiliko moja la hivi karibuni na uhesabu huduma ngapi zililazimika kusambazwa pamoja ili liwe salama; namba ikiwa zaidi ya moja kwa badiliko lililogusa uwezo mmoja, mipaka yenu si sahihi. Suluhisho kwa kawaida ni kumpa kila huduma data yake na mkataba thabiti, wenye matoleo, si kuongeza huduma zaidi.

3. **Ni mgawanyo upi wa huduma zenu zilizopo umeacha kulipa, na je, mngeziunganisha tena?** Tabia ya juu zaidi ya sura hii ni kuchukulia maamuzi ya mtindo kama yanayotenguka: toa pale kichocheo kinapoibuka, na unganisha tena kichocheo kinapotoweka. Mashirika mengi hugawanya tu, kwa hiyo huduma ndogo sana na huduma za vyombo vinavyozungumza kupita kiasi hukusanyika hadi mzigo wa uratibu na mtandao unazidi kazi ambayo kila huduma inafanya. Tafuta huduma zinazosambazwa pamoja kila mara, zilizopo kwa sababu ya jedwali la hifadhidata badala ya uwezo wa biashara, au ambazo miruko ya mtandao sasa inatawala ucheleweshaji wa ombi. Katika mifumo ya mashirika makubwa na serikali, ambapo idadi ya wafanyakazi na bajeti zinachunguzwa, kukunja huduma mbili nyembamba kuwa huduma moja kubwa ni hatua halali, ya kuokoa gharama, si kukiri kushindwa. Weka kuunganisha tena mezani kwa uwazi kama kutoa, na uamue yote mawili kwa ushahidi ule ule.

4. **Je, jukwaa na ukomavu wenu wa zamu unaunga mkono kweli mtindo mnaoupendekeza, na mnaweza kutaja mapengo mahususi kabla ya kujitolea?** Huduma ndogo, mesh, na uti wa mgongo unaoendeshwa na matukio hutoa faida zake tu juu ya CI/CD iliyokomaa, ufuatiliaji uliosambazwa, ugunduzi wa huduma, na utamaduni wa zamu unaoweza kufikiri kuhusu kushindwa kwa sehemu. Shirika kubwa huelekea kuamua mtindo lengwa katika jukwaa la usanifu na kugundua jukwaa linalokosekana baadaye, huduma kadhaa zikiwa tayari kwenye uzalishaji na kila tukio likichukua saa kutambuliwa. Pima mvuto wa usambazaji na ukubwa huru dhidi ya swali la kiasi: nani anauendesha saa tisa usiku? Mgawanyo ule ule unaozipa timu uhuru wa kusafirisha sambamba pia unazidisha njia za kushindwa ambazo kila timu lazima ziziele. Leta orodha ya uaminifu kwenye mjadala: mzunguko wa sasa wa usambazaji, muda wa wastani wa kurejesha, kama mna ufuatiliaji kuvuka mipaka ya huduma, na huduma ngapi timu moja inaweza kuziendesha kwa uhalisia. Katika mazingira ya mashirika makubwa na serikali, ongeza muda wa ununuzi na kuajiri kwa uwezo wa jukwaa mnaokosa, kwa sababu mtindo unaodhania mesh na timu ya jukwaa msiyoifadhili ni mpango wa kuendesha eneo lisilodumishika.

5. **Ni sehemu zipi za kikoa ambazo njia kamili ya ukaguzi ya event sourcing ni ulazima wa kisheria badala ya urahisi, na nani ana mamlaka ya kuamua?** Event sourcing na CQRS vinakununulia historia kamili inayoweza kujengwa upya na vielelezo vya kusoma vinavyopanuka peke yake, lakini vinakugharimu matoleo ya matukio, kujenga upya makadirio, na kufikiri kuhusu uthabiti wa mwisho kwa maisha ya mfumo. Zikitumika kwa kikoa ambacho hakikuhitaji njia ya ukaguzi, ugumu huo ni kodi tupu; zikizuiwa kwa kikoa ambapo "tulifikaje kwenye thamani hii?" ni swali la kisheria, kutokuwepo kwake ni kushindwa kwa uzingatiaji. Mazingatio yanayoshindana ni uwezo wa kukaguliwa na ukubwa wa hoja upande mmoja, na ugumu wa utatuzi na mzigo wa kiakili wa wasanidi upande mwingine, kwa hiyo uamuzi ni wa watu wanaoelewa wajibu wa udhibiti na mzigo wa uendeshaji, si yeyote mwenye shauku zaidi kwa muundo huo. Leta mahitaji mahususi ya kisheria au ya kimkataba ya uhifadhi na kujenga upya, ujazo unaotarajiwa wa matukio, na makadirio ya uaminifu ya kazi ya matoleo na makadirio. Katika fedha, kodi, na serikali, ambapo kujenga upya uamuzi miaka baadaye kunaweza kuwa wajibu wa kisheria, taja mmiliki anayewajibika anayeidhinisha kwamba muktadha fulani uliofungwa unahitaji, au haukihitaji, kumbukumbu ya matukio isiyobadilika.

6. **Mtazuiaje monolith ya moduli isimomonyoke ili kutoa baadaye kubaki nafuu, na nini kitatekeleza mipaka?** Hoja nzima ya kuanza na monolith ya moduli inategemea ahadi kwamba mipaka safi ya ndani hufanya kutoa huduma baadaye kuwa nafuu, hata hivyo mipaka hiyo huoza kimyakimya mara tarehe ya mwisho inapoishawishi moduli moja kufikia data ya nyingine. Kwa timu kubwa yenye wachangiaji wengi, nia njema na mapitio ya msimbo peke yake hayatashikilia mstari; bila utaratibu wa kutekeleza, monolith inakuwa kimyakimya donge kubwa la matope ambalo mtindo ulikusudiwa kuliepuka. Pima msuguano wa kanuni za utegemezi na violesura vya moduli vinavyotekelezwa dhidi ya gharama ya kugundua, miaka baadaye, kwamba hakuna mpaka wowote ulio halisi na kila uondoaji unamaanisha kufumua hali ya pamoja. Leta ushahidi: mipaka ya moduli inatekelezwa kwa zana za ujenzi, uchambuzi tuli, au muundo wa vifurushi, au ni desturi zilizoandikwa tu ambazo uunganishaji sita wa mwisho uliziruka? Katika mifumo ya mashirika makubwa na serikali ya muda mrefu inayopaswa kunusurika udhibiti mkali wa mabadiliko na vizazi kadhaa vya mifumo ya kazi, chukulia utekelezaji wa mipaka kama udhibiti unaokaguliwa, ili chaguo la kusambaza baadaye liwe moja mlilolihifadhi kweli badala ya mnalodhani bado mnalo.

## Mtazamo wa sekta

**Kampuni changa.** Chaguo-msingi ni monolith moja ya moduli na upinge mvuto wa huduma ndogo, kwa sababu rasilimali yako adimu zaidi ni umakini wa kihandisi na kundi la huduma ni kodi ya uendeshaji usiyoweza kumudu kabla ya bidhaa kupata soko. Weka mipaka safi ya moduli ili uweze kutoa baadaye, na fikia serverless pale kupanuka hadi sifuri na kulipa kwa matumizi kunafaa mzigo wako wenye mawimbi, wa msingi wa chini. Gawanya kitu kimoja tu kichocheo madhubuti kinapoibuka, kama mtumaji wa arifa wa milipuko, na kamwe mapema zaidi.

**Biashara ndogo.** Bila timu ya jukwaa na bajeti finyu, pendelea monolith au huduma chache kubwa kwenye jukwaa linalosimamiwa, na ununue miundombinu inayohifadhiwa badala ya kujenga mesh, ufuatiliaji, na ugunduzi wa huduma mwenyewe. Pima serverless na hifadhidata zinazosimamiwa kama njia ya kuepuka kuendesha seva kabisa, na tahadhari kuhusu muundo uliosambazwa ambao mzigo wake wa uendeshaji huna mtu wa kuubeba. Usanifu sahihi ni ule ambao mtu mmoja au wawili wanaweza kuusambaza, kuuona, na kuurejesha kweli.

**Biashara kubwa.** Tatizo halisi ni timu nyingi na Sheria ya Conway: pangilia huduma kubwa na miktadha iliyofungwa na umiliki wa timu, na uwekeze kwa makusudi katika jukwaa (CI/CD, ufuatiliaji, mesh, na ugunduzi wa huduma) linalofanya usambazaji kuwa salama. Sawazisha mifumo ya lango, BFF, na usanifu safi wa ndani ili vikundi viache kuvumbua upya, na utawale utoaji na kuunganisha tena kama maamuzi ya jalada yanayotegemea ushahidi badala ya mapendeleo ya mahali. Weka bajeti ya gharama ya uendeshaji ya kila mgawanyo waziwazi, kwa sababu kwa ukubwa wako kushindwa kwa monolith iliyosambazwa ni ghali na polepole kutengua.

**Serikali.** Maisha marefu ya mifumo, udhibiti mkali wa mabadiliko, mizunguko ya ununuzi, na uwezo wa kukaguliwa huumba uchaguzi: pendelea mitindo yenye mipaka wazi, inayokaguliwa na mikataba ya kudumu inayodumu kuliko wauzaji na vizazi vya mifumo ya kazi. Event sourcing inastahili ugumu wake pale kujenga upya uamuzi unaomkabili raia ni wajibu wa kisheria, kwa hiyo itumie kwa makusudi kwa leja kuu na uweke usanifu safi ndani ya kila huduma kutenga kanuni zinazobadilika kwa kila bajeti. Chukulia uhamishikaji na kutoka kwenye serverless au majukwaa ya muuzaji wa umiliki kama mahitaji ya ununuzi, si mawazo ya baadaye.

## Mifano

**Kampuni changa.** Kampuni changa ya watu wanne inayojenga bidhaa ya ratiba inahisi shinikizo la kuanza na huduma ndogo kwa sababu mshindani aliandika kuhusu hizo, lakini inapinga. Wanasafirisha monolith moja ya moduli yenye mipaka safi ya ndani (ratiba, bili, arifa) kama moduli tofauti katika kitu kimoja kinachosambazwa, kwa hiyo mhandisi mmoja anaweza kuendesha kila kitu kwa ndani na toleo ni kusukuma mara moja. Bidhaa inapopata mvuto, mtumaji wa arifa tu, anayegawanya kwa barua pepe na SMS chini ya mzigo wa milipuko, ndiye anayetolewa kuwa huduma yake. Hawarithi kodi yoyote ya uendeshaji ya huduma kadhaa wakati bado wanawinda soko la bidhaa.

**Biashara kubwa.** Kampuni kubwa ya biashara ya mtandaoni inaanza kama monolith ya moduli. Trafiki inapokua na timu kuongezeka, inatoa vikoa vyenye mzigo mkubwa zaidi, vinavyobadilika kwa kujitegemea zaidi (katalogi, kikapu, malipo, na utafutaji) kuwa huduma tofauti, kila moja ikimiliki data yake. Malipo hutoa matukio ambayo hesabu ya bidhaa, utimizaji, na uchanganuzi huyatumia kupitia uti wa mgongo wa matukio, kwa hiyo watumiaji wapya (kugundua ulaghai, uaminifu) wanaweza kuambatanisha bila kugusa malipo. Lango la API linashughulikia uthibitishaji na kikomo cha kasi, na BFF inaunda mizigo ya simu. Vikoa vilivyobaki vya trafiki ndogo vinabaki kwenye monolith, jambo linaloepuka mgawanyiko usio wa lazima.

**Serikali.** Mamlaka ya kodi inajenga jukwaa la tathmini juu ya event sourcing kwa leja kuu, kwa sababu kila badiliko la dhima ya mlipa kodi lazima liweze kujengwa upya na kukaguliwa kisheria kwa miaka. Amri (wasilisha marejesho, tumia malipo, toa marekebisho) huzalisha matukio yasiyobadilika, na vielelezo vya kusoma hukadiria salio za sasa kwa maafisa na raia. CQRS inaruhusu upande wa hoja unaomkabili umma upanuke peke yake kwa msimu wa kilele wa kuwasilisha bila kuhatarisha upande wa kuandika. Ndani, kila huduma inafuata usanifu safi, kwa hiyo kanuni za tathmini, zinazobadilika kwa kila bajeti, zinabaki zimetengwa na teknolojia ya uhifadhi na ujumbe.

## Kesi ya biashara: sababu, ROI, na TCO

Fedha zilizo hatarini katika uchaguzi wa mtindo ni kubwa mno, kwa sababu uamuzi ni ghali kutengua. Pokea huduma ndogo mapema mno na unaongeza jumla ya gharama ya umiliki kupitia ujenzi wa jukwaa, miundombinu iliyorudiwa, utatuzi uliosambazwa, na mzigo mzito zaidi wa uendeshaji: gharama zinazobaki nawe kwa maisha ya mfumo. Kataa kugawanya monolith iliyozidiwa kweli na unadhibiti uwezo wa kupitisha wa utoaji: timu zinasubiri kwenye toleo la pamoja, na kila badiliko linahatarisha mfumo mzima. Mjadala wa ROI kwa kweli unahusu kulinganisha matumizi ya uendeshaji na hitaji la shirika.

Jenga hoja kwa uongozi kwa mtazamo wa uwezo wa kupitisha na hatari, si teknolojia. Usambazaji huru unamaanisha timu nyingi zinasafirisha sambamba na muda mfupi wa kuongoza: kasi ya biashara inayopimika. Kutengwa kwa kushindwa kunamaanisha kukatika kwa jumla kidogo na mlipuko mdogo: upatikanaji unaopimika na ulinzi wa sifa. Lakini kuwa mkweli vilevile kuhusu uwekezaji wa jukwaa ambao kila mtindo unadai: mesh, ufuatiliaji, na ukomavu wa CI/CD ni mahitaji ya awali, si nyongeza za hiari, na gharama yao ni ya TCO. Kwa mashirika mengi njia ya bei nafuu zaidi ni monolith ya moduli iliyogawanywa vizuri sasa, yenye mipaka safi ya ndani inayofanya kutoa baadaye kuwa nafuu. Hilo linakununulia chaguo la kusambaza bila kulilipia kabla ya kulihitaji.

## Mifumo mibaya na mitego

- **Monolith iliyosambazwa.** Huduma zinazopaswa kusambazwa pamoja na kushiriki hifadhidata: gharama zote za usambazaji, hakuna uhuru.
- **Huduma ndogo sana.** Huduma ndogo kiasi kwamba mzigo wa uratibu na mtandao unazidi kazi wanayofanya.
- **Huduma ndogo bila jukwaa.** Kugawanya kabla ya kuwa na CI/CD, ufuatiliaji, na ukomavu wa zamu; njia za kushindwa zinazidi.
- **Huduma za vyombo.** Kugawanya kwa jedwali la hifadhidata ("Huduma ya Mtumiaji," "Huduma ya Agizo") badala ya uwezo wa biashara, kulazimisha miito ya kuzungumza kupita kiasi kuvuka huduma kwa kila operesheni.
- **Event sourcing kila mahali.** Kuitumia kwenye vikoa visivyohitaji njia ya ukaguzi, kulipa kodi ya ugumu bila faida.
- **Lango kama monolith.** Kuweka mantiki ya biashara kwenye lango la API, kuunda upya kizuizi cha kati.
- **Kiini kilichounganishwa na mfumo wa kazi.** Mantiki ya biashara iliyochanganyika na mfumo wa wavuti au ORM (ramani ya kitu-kwa-uhusiano), ikifanya majaribio na mabadiliko ya teknolojia yote kuwa na maumivu.

## Kielelezo cha ukomavu

- **Ngazi ya 1: Kuanzisha.** Mtindo huchaguliwa kwa mitindo ya wakati au ajali. Una monolith moja iliyochanganyika au fujo ya bahati mbaya iliyosambazwa, mipaka inafuata tabaka za kiufundi au historia badala ya kikoa, na mgawanyo hutokea kwa kuitikia kitu kinapovunjika.
- **Ngazi ya 2: Kuendeleza.** Baadhi ya timu huchora mipaka ya moduli ya makusudi ndani ya monolith au kuanzisha huduma chache kubwa, na baadhi ya masuala ya kuvuka sehemu yanashughulikiwa kwa uthabiti. Mazoea hayalingani: kikundi kimoja kinapangilia huduma na miktadha iliyofungwa wakati kingine bado kinagawanya kwa jedwali la hifadhidata, na kutoa kunabaki kwa papo hapo.
- **Ngazi ya 3: Kusawazisha.** Mbinu iliyoandikwa inatekelezwa shirika zima: huduma zinalingana na miktadha iliyofungwa na kumiliki data yao, mifumo ya lango na BFF inatumika inapofaa, tabaka safi au hexagonal za ndani ndizo kiwango, na kila mgawanyo unahitaji kichocheo kilichotajwa. Mipaka ya moduli inatekelezwa kwa zana, si desturi tu.
- **Ngazi ya 4: Kusimamia.** Maamuzi ya mtindo yanapimwa na kudhibitiwa dhidi ya vipimo vya msingi. Unafuatilia mzunguko wa usambazaji na muda wa kuongoza kwa kila huduma, muda wa wastani wa kurejesha, huduma ngapi lazima zisambazwe pamoja kwa badiliko la kawaida, na ucheleweshaji wa miruko ya mtandao, na kulinganisha gharama ya kila mgawanyo dhidi ya uhuru uliokusudiwa kununua. Ushahidi, si mapendeleo, unaamua kama mpaka unabaki, na kuteleza kuelekea monolith iliyosambazwa kunanaswa na vipimo badala ya kukatika.
- **Ngazi ya 5: Kuratibu.** Usanifu umeunganishwa na muundo wa shirika na unabadilishwa mfululizo. Jukwaa lililokomaa (CI/CD, ufuatiliaji, na mesh inapostahili) hufanya usambazaji na kuunganisha tena kuwa nafuu, timu hutoa mara kwa mara kichocheo kinapoibuka na kukunja huduma nyuma kimoja kinapotoweka, na uchaguzi wa mtindo unasawazishwa upya muundo wa timu, mzigo, na picha ya hatari vinapohama kuvuka eneo zima.

## Mawazo ya kujadili

1. Wapi katika mfumo wenu monolith ni nguvu kweli, na wapi ni kizuizi halisi?
2. Kichocheo gani madhubuti kingehalalisha kutoa huduma yenu inayofuata, na mnaweza kukitaja kabla ya kujenga?
3. Shirika lenu lina ukomavu wa uendeshaji ambao huduma ndogo zinadai? Kinakosekana nini?
4. Kwa sehemu zipi za kikoa chenu njia kamili ya ukaguzi ya event sourcing ni ulazima wa kisheria au wa biashara dhidi ya urahisi?
5. Mipaka ya huduma zenu za sasa inaakisi vizuri kiasi gani mipaka ya timu zenu, na je, mpangilio huo unasaidia au unaumiza?
6. Kama mngelazimika kubadilisha mfumo wa kazi wa wavuti au hifadhidata mwaka ujao, mantiki yenu ya biashara kiasi gani mngelazimika kuiandika upya?

## Mambo muhimu ya kukumbuka

- Chagua mtindo wa usanifu kutoka nguvu halisi (ukubwa wa timu, kikoa, mzigo, ukomavu wa uendeshaji), si kutoka mitindo ya wakati.
- Monolith ya moduli ndiyo chaguo-msingi sahihi kwa mifumo mingi; toa huduma tu kwa kichocheo madhubuti na kwa mistari ya miktadha iliyofungwa.
- Huduma ndogo hubadilisha ugumu wa uendeshaji na wa kiakili kwa usambazaji huru, ukubwa, na kutengwa kwa kushindwa; zinahitaji jukwaa lililokomaa.
- Usanifu unaoendeshwa na matukio, CQRS, na event sourcing hutoa kutenganisha na uwezo wa kukaguliwa kwa gharama ya uthabiti wa mwisho na ugumu wa matoleo; upokee kwa makusudi.
- Malango, BFF, na mesh hudhibiti eneo la huduma nyingi lakini huongeza uzito; yaanzishe ukubwa unapodai, si kabla.
- Tumia usanifu wa hexagonal/safi ndani ya kila huduma kuweka mantiki muhimu ya biashara ikijaribika na ya kudumu kuvuka mabadiliko ya teknolojia.

## Marejeo na usomaji zaidi

- Sam Newman, *Building Microservices* and *Monolith to Microservices*
- Chris Richardson, *Microservices Patterns*
- Eric Evans, *Domain-Driven Design*
- Vaughn Vernon, *Implementing Domain-Driven Design*
- Robert C. Martin, *Clean Architecture*
- Alistair Cockburn, "Hexagonal Architecture (Ports and Adapters)"
- Gregor Hohpe and Bobby Woolf, *Enterprise Integration Patterns*
- Martin Fowler, *Patterns of Enterprise Application Architecture* (and articles on CQRS and Event Sourcing)
- Matthew Skelton and Manuel Pais, *Team Topologies*
