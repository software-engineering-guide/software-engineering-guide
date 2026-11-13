# 2.3 API na usanifu wa violesura

## Muhtasari na msukumo

[API](https://en.wikipedia.org/wiki/API) (kiolesura cha kuandika programu) ni mkataba ambao kipande kimoja cha programu hutoa uwezo kwa kingine. Ndipo timu, mifumo, na mashirika yanapokutana, na ndicho kitu cha kudumu na ghali zaidi kukosea. Unaweza kurekebisha saini ya kazi ya ndani kwa uhuru. API iliyochapishwa ni tofauti: ni ahadi kwa watumiaji ambao huenda hutawahi kukutana nao, na kuivunja kunawavunja. Mashirika yanapogawanya [monolith](https://en.wikipedia.org/wiki/Monolithic_application) kuwa huduma na kufungua uwezo kwa washirika na umma, API inakuwa uso mkuu wa bidhaa na hatari kuu ya uunganishaji.

Kwa timu kubwa, API ndizo zinazowaruhusu watu kufanya kazi kwa kujitegemea. Kiolesura kilichobuniwa vizuri kinakuruhusu kubadilisha ndani yako bila kuratibu na kila mtumiaji, ambayo ndiyo hoja nzima ya mpaka wa huduma. Kibaya huvuja undani wa ndani, hulazimisha utoaji wa pamoja, na kugeuza seti ya huduma kuwa monolith iliyosambazwa: huduma zilizogawanyika lakini zimeunganishwa kwa ukali kiasi kwamba lazima zijengwe na kutolewa pamoja. Usanifu wa API yako huamua moja kwa moja jinsi timu zako zinavyoweza kusonga kwa kujitegemea.

Katika mazingira ya mashirika makubwa na ya serikali, API pia hubeba wajibu wa uzingatiaji, usalama, na uimara. API ya sekta ya umma inaweza kuhitajika kufuata [viwango huria](https://en.wikipedia.org/wiki/Open_standard), kubaki thabiti kwa miaka, na kuhudumia wasanidi wa nje usioweza kuratibu nao. API za mashirika makubwa huunga mkono uunganishaji wa washirika wenye viwango vya huduma vya kimkataba. Yote haya yanainua kiwango cha nidhamu ya matoleo, [utangamano wa nyuma](https://en.wikipedia.org/wiki/Backward_compatibility), utawala, na uzoefu wa msanidi.

## Kanuni kuu

- Buni mkataba kwanza. Kiolesura ni uamuzi wa makusudi wa bidhaa, si zao la pembeni la utekelezaji.
- Boresha kwa uzoefu wa mtumiaji, si urahisi wako mwenyewe.
- Chukulia utangamano wa nyuma kama ahadi. Mabadiliko yanayovunja yanahitaji toleo jipya na njia ya uhamiaji.
- Fanya kitu rahisi kiwe sahihi: chaguo-msingi zenye busara, makosa yanayotabirika, desturi thabiti.
- Buni kwa kushindwa. [Kutobadilisha matokeo (idempotency)](https://en.wikipedia.org/wiki/Idempotence) (ombi linalorudiwa lina athari ileile kama moja), kujaribu upya, ugawaji wa kurasa, na [kupunguza kasi ya maombi](https://en.wikipedia.org/wiki/Rate_limiting) ni wasiwasi wa daraja la kwanza, si mawazo ya baadaye.
- Chagua mtindo wa itifaki kufaa mwingiliano, si mtindo wa mitindo.
- Tawala API kama bidhaa, zikiwa na wamiliki, mizunguko ya maisha, na nyaraka.

## Mapendekezo

### Fanya kazi API-kwanza na kwa kuendeshwa na mkataba

Fafanua na upitie mkataba wa API, ikijumuisha rasilimali zake, shughuli, miundo, na maana ya makosa, kabla ya kuandika utekelezaji. Tumia ubainishaji unaosomeka na mashine, ili mkataba uweze kuzalisha nyaraka, vijiti vya mteja na seva, seva za mfano, na uthibitishaji. Sasa watumiaji wanaweza kuanza kuunganisha dhidi ya mfano wakati unajenga, na mkataba unakuwa chanzo kimoja cha ukweli ambacho pande zote mbili hujaribu dhidi yake.

### Chagua mtindo wa mwingiliano kwa makusudi

Chagua kati ya [REST](https://en.wikipedia.org/wiki/REST) (uhamishaji wa hali ya uwakilishi), [GraphQL](https://en.wikipedia.org/wiki/GraphQL), [gRPC](https://en.wikipedia.org/wiki/GRPC), na [ujumbe unaoendeshwa na matukio](https://en.wikipedia.org/wiki/Event-driven_architecture) kulingana na mwingiliano, si upendeleo binafsi. Tumia REST kwa violesura vinavyoelekezwa kwa rasilimali, vinavyooana kwa upana, vinavyoweza kuhifadhiwa kwenye kashe. Tumia GraphQL pale wateja mbalimbali wanahitaji usomaji unaonyumbulika, uliokusanywa juu ya grafu tajiri. Tumia gRPC kwa miito ya utendaji wa juu, iliyoandikwa kwa aina kali kati ya huduma za ndani. Tumia ujumbe unaoendeshwa na matukio kwa mtiririko wa kazi usio wa wakati mmoja, usiounganishwa na kwa kusambaza mabadiliko ya hali. Mifumo mikubwa mingi hutumia mitindo kadhaa kwa wakati mmoja, kila mmoja pale unapofaa.

### Weka matoleo na ustaafishe kwa nidhamu

Pokea mkakati wazi wa matoleo na sera iliyochapishwa ya kustaafisha: jinsi unavyoainisha mabadiliko, muda gani unaunga mkono matoleo ya zamani, na jinsi unavyowaarifu watumiaji. Chora mstari wazi kati ya mabadiliko yanayooana nyuma (kuongeza sehemu za hiari, kiungo kipya) na yanayovunja (kuondoa au kubadilisha jina la sehemu, kubadilisha aina au maana). Kamwe usitumie upya maana ya sehemu iliyopo. Wape watumiaji vipindi vya kuingiliana vya kuhama, na uwasilishe ratiba mapema.

### Fanya maana ya makosa iwe thabiti na inayosomeka na mashine

Rudisha makosa yenye muundo, yanayotabirika: misimbo thabiti inayosomeka na mashine, ujumbe unaosomeka na binadamu, na muktadha wa kutosha wa kutenda, bila kuvuja undani nyeti wa ndani. Tumia maana ileile ya hali kuvuka kila kiungo, ili wateja washughulikie makosa kwa usawa. Andika kila kosa ambalo mtumiaji anaweza kukutana nalo.

### Jenga ndani kutobadilisha matokeo, ugawaji wa kurasa, na kupunguza kasi ya maombi

Fanya shughuli za uandishi ziwe salama kujaribu upya kwa kuunga mkono funguo za kutobadilisha matokeo, ili mteja anayejaribu upya baada ya muda kuisha asitoze mara mbili wala kuunda mara mbili. Gawa kurasa kila kiungo cha orodha tangu siku ya kwanza, na upendelee ugawaji wa kurasa unaotegemea kielekezi kwa seti kubwa au zinazobadilika. Tumia na uandike mipaka ya kasi, na urudishe hali ya sasa ya kikomo kwa wateja ili waweze kupunguza mwendo kwa neema.

### Tawala API na uwekeze katika uzoefu wa msanidi

Chukulia kila API kama bidhaa, yenye mmiliki, mzunguko wa maisha, na kiingilio cha orodha. Weka mapitio ya usanifu au bodi ya viwango vya API ili violesura vibaki thabiti kuvuka timu. Wekeza katika uzoefu wa msanidi: nyaraka sahihi za marejeo, miongozo ya kuanza, mifano, eneo la majaribio, na kumbukumbu ya mabadiliko. Katika mfumo mkubwa wa ikolojia, tovuti au orodha inayofanya API zipatikane ni muhimu.

## Mabadilishano: faida na hasara

| Mtindo | Bora kwa | Faida | Hasara |
|---|---|---|---|
| REST / HTTP | API za umma, zinazoelekezwa kwa rasilimali | Inapatikana kila mahali, inaweza kuhifadhiwa kwenye kashe, rahisi, inaoana | Kuchukua kupita/pungufu; safari nyingi za kwenda-na-kurudi; mikataba legevu isipobainishwa |
| GraphQL | Usomaji unaonyumbulika kwa wateja mbalimbali | Hoja zinazobainishwa na mteja; kiungo kimoja; muundo imara | Ugumu wa kashe na kupunguza kasi; hatari za gharama ya hoja; ugumu wa seva |
| gRPC | Miito ya ndani ya utendaji wa juu | Haraka, mnene, aina kali, utiririshaji | Msaada duni wa kivinjari; haisomeki sana na binadamu; zana nzito zaidi |
| Inayoendeshwa na matukio | Mtiririko wa kazi usio wa wakati mmoja, usiounganishwa | Uunganishaji legevu; inapanuka; inastahimili | Ngumu zaidi kufikiria; uthabiti wa mwisho; ugumu wa kiuendeshaji |

Mikakati ya matoleo hubadilishana uthabiti na matengenezo. Kuunga mkono matoleo mengi ya zamani hulinda watumiaji, lakini huzidisha msimbo unaopaswa kuudumisha na kuujaribu. Utangamano wa nyuma hubadilishana uhuru wako mwenyewe na uthabiti wa mtumiaji, kwa kawaida biashara sahihi kwa API inayotumika sana. Picha kuu: gharama ya uamuzi mbaya wa API inalipwa na kila mtumiaji kwa maisha yote ya kiolesura. Kwa hiyo inastahili juhudi zaidi za usanifu kwenye mpaka kuliko karibu popote pengine.

## Maswali ya kujadili na timu yako

1. **Unaainishaje badiliko kama linaloendana nyuma dhidi ya linalovunja, na ni ukaguzi gani wa kiotomatiki unanasa mavunjiko ya kimya kabla hayajatolewa?** Sura hii inachora mstari mgumu: kuongeza sehemu za hiari na viungo vipya ni salama, ilhali kuondoa au kubadilisha jina la sehemu, kubadilisha aina, au kutumia upya maana ya sehemu kunavunja watumiaji. Katika timu kubwa mtu anayefanya badiliko mara nyingi hawezi kuona kila mtumiaji, kwa hiyo mabadiliko "madogo" yanaweza kuvunja kimyakimya washirika ambao hujawahi kuzungumza nao. Leta ishara madhubuti kwenye mkutano: je, mnaendesha ukaguzi wa kiotomatiki wa utangamano wa mkataba kwenye CI dhidi ya ubainishaji uliochapishwa, au mnategemea mtu kukumbuka kanuni. Katika mazingira ya mashirika makubwa na ya serikali, ambapo badiliko linalovunja hulazimisha uhamiaji ulioratibiwa kuvuka kila mshirika na linaweza kuvuka mabadiliko ya wasambazaji na tawala, gharama inapanuka na idadi ya watumiaji. Amua kanuni za uainishaji na uunganishe lango la utangamano, ili badiliko lisiloendana lishindwe ujenzi badala ya uunganishaji.

2. **Ni vitu vipi vya kuaminika, funguo za kutobadilisha matokeo, ugawaji wa kurasa, na kupunguza kasi ya maombi, vilivyo vya lazima kwenye kila kiungo kipya tangu siku ya kwanza?** Sura inasisitiza hivi ni wasiwasi wa daraja la kwanza, kwa sababu kuweka ufunguo wa kutobadilisha matokeo kwenye kiungo cha tozo kilicho hai au kuongeza ugawaji wa kurasa kwenye orodha inayosafirishwa tayari ni badiliko linalovunja lenyewe. Mfumo mkubwa wa ikolojia hukuza hili: kiungo kinachofanya kazi kwenye majaribio kinaporomoka chini ya ujazo halisi wa data, na uandishi usio na kutobadilisha matokeo hugeuza hitilafu moja ya mtandao kuwa tozo mbili. Leta ushahidi wa viungo vipi vya sasa vinakosa haya na dhoruba ya kujaribu upya ingefanya nini. Fanya chaguo-msingi zisijadiliwe kwa viungo vipya: ugawaji wa kurasa wa kielekezi kwa kila orodha, funguo za kutobadilisha matokeo kwa kila uandishi, mipaka ya kasi iliyoandikwa inayorudisha hali yake ya sasa. Hiyo inageuza uhamiaji wa baadaye wa kulazimishwa kuwa tabia ya usanifu ya mara moja.

3. **Je, mnabuni na kupitia mkataba kweli kabla ya kuandika utekelezaji, au kiolesura kinavuja kutoka msimbo?** Pendekezo la API-kwanza linaomba ubainishaji unaosomeka na mashine, uliopitiwa mapema, unaozalisha nyaraka, vijiti, na mifano na kuwaruhusu watumiaji kuunganisha dhidi ya mfano wakati unajenga. Mkataba unapofuata utekelezaji, kiolesura hufichua muundo wa ndani wa hifadhidata na kuhama kila utekelezaji unapohama, ambayo ndiyo mfumo mbaya mkuu katika sura hii. Ishara ya kuchunguza: je, mtumiaji anaweza kuanza kuunganisha dhidi ya mfano wenu leo, au lazima asubiri seva inayoendesha. Kwa API za umma na za washirika, ambapo kiolesura ndicho uso wa bidhaa na kitu ghali zaidi kukosea, kutumia siku moja kwenye mkataba huokoa wiki za mizunguko ya msaada. Fanya mapitio ya mkataba kuwa hatua ya lazima kabla utekelezaji haujaanza.

4. **Timu mbili zinapohitaji kuonyesha uwezo uleule, mtindo upi wa mwingiliano unashinda, na nani ana mamlaka ya kusema hapana kwa itifaki ya nne?** Sura hii inakuambia uchague REST, GraphQL, gRPC, au ujumbe unaoendeshwa na matukio kwa kufaa mwingiliano, lakini kwa ukubwa hatari halisi ni kwamba kila timu huchagua pendwa yake na watumiaji wanakabiliwa na desturi tofauti kwenye kila kiungo. Shirika kubwa hulipia mgawanyiko huo katika maktaba za mteja, milango, ufuatiliaji, na mzigo wa kiakili kwa kila mwunganishaji anayejifunza milio minne badala ya mmoja. Leta orodha ya itifaki zilizopo tayari kwenye uzalishaji, mwingiliano ambao kila moja ilichaguliwa kuuhudumia, na watumiaji wanaovuka zaidi ya mmoja. Jambo linaloshindana ni halisi: chaguo-msingi la pamoja hupunguza kuenea, hata hivyo agizo gumu hulazimisha matatizo yenye umbo la gRPC kwenye shimo lenye umbo la REST. Taja chombo cha viwango au mapitio ya usanifu yanayomiliki mchakato wa vighairi, kwa sababu katika mashamba ya mashirika makubwa na ya serikali kuenea kwa mitindo kunakuwa ushuru wa kudumu kwenye uunganishaji na tatizo gumu kutengua washirika wanapotegemea kila moja.

5. **Sera yetu iliyochapishwa ya kustaafisha ni ipi, na je, tunaweza kuthibitisha tunaheshimu kweli dirisha la msaada tunalolitangaza?** Sura inachukulia matoleo na kustaafisha kama nidhamu: sera iliyoandikwa ya muda gani matoleo ya zamani yanaishi, jinsi watumiaji wanavyoarifiwa, na muingiliano gani wanapata kuhama. Ahadi usiyoweza kuitekeleza ni mbaya kuliko kutokuwa nayo, kwa sababu mfumo mkubwa wa ikolojia unajumuisha watumiaji ambao huzungumzi nao ambao wataendelea kuita toleo lililostaafishwa hadi lishindwe kwenye uzalishaji. Leta ushahidi kwenye mjadala: matoleo mangapi hai mnayabeba leo, matumizi halisi kwa kila moja, kama mnaweza kuona watumiaji wapi bado wanaita kiungo kilichostaafishwa, na jinsi mapema mlitangaza kustaafishwa kwenu kwa mwisho. Shinikizo linaloshindana ni gharama ya matengenezo dhidi ya uthabiti wa mtumiaji, na zote ni halisi. Kwa washirika wa mashirika makubwa chini ya viwango vya huduma vya kimkataba na API za sekta ya umma zinazopaswa kuokoka kuvuka tawala na mabadiliko ya wasambazaji, dirisha la msaada ni ahadi inayoweza kudumu kuliko timu iliyoifanya, kwa hiyo amua nani anaimiliki na jinsi kustaafishwa kunavyothibitishwa salama kabla hakijatokea.

6. **Tunajuaje uzoefu wetu wa msanidi ni mzuri, au tunaudhania kwa sababu API inafanya kazi kwetu?** Sura hii inaweka kila API kama bidhaa ambayo kupokelewa kwake kunategemea nyaraka sahihi za marejeo, miongozo ya kuanza, mifano, eneo la majaribio, kumbukumbu ya mabadiliko, na orodha inayopatikana. Timu mara kwa mara huchanganya "API inafanya kazi" na "API inatumika", na pengo linaonekana kama tiketi za msaada, uunganishaji ulioshindwa, na watumiaji wanaokata tamaa kimyakimya. Leta ishara zinazopimika badala ya maoni: muda hadi wito wa kwanza wenye mafanikio kwa mwunganishaji mpya, kiasi cha tiketi za msaada kwa kila kiungo, jinsi nyaraka zilizochapishwa zilivyochakaa dhidi ya mkataba hai, na kama mgeni anaweza kujihudumia kutoka kwenye tovuti bila kutuma barua pepe kwa timu yako. Mvutano ni kwamba nyaraka na tovuti zinagharimu juhudi halisi zinazoshindana na kutoa vipengele, hata hivyo katika mfumo mkubwa wa ikolojia uzoefu duni wa msanidi husukuma gharama ya uunganishaji kwa mamia ya watumiaji kwa wakati mmoja. Katika serikali, ambapo API huria inahudumia wasanidi wa nje usioweza kuratibu nao na uwazi mara nyingi umeamriwa, kiolesura kinachotumika, kilichoandikwa vizuri, kinachopatikana ni sehemu ya wajibu wa uwajibikaji kwa umma, si fadhila.

## Mtazamo wa sekta

**Kampuni changa.** Ukiwa na wahandisi wawili au watatu na bila muda wa taratibu, weka mkataba mwepesi lakini halisi: ubainishaji mmoja unaosomeka na mashine ambao wateja wako wa kwanza wa washirika wa usanifu wanaweza kuunganisha dhidi yake wakati unajenga. Usianzishe lango la API, orodha, wala bodi ya utawala bado, lakini funga tabia mbili ambazo ni chungu kuongeza baadaye, funguo za kutobadilisha matokeo kwenye uandishi na ugawaji wa kurasa wa kielekezi kwenye orodha, kwa sababu kuziongeza kwenye kiungo hai ni badiliko linalovunja usiloweza kulimudu. Pendelea mtindo mmoja wa mwingiliano, karibu daima REST, ili usibebe kuenea kwa itifaki hadi mwaka wako wa kwanza.

**Biashara ndogo.** Bila mtaalamu maalumu wa API na bajeti finyu, tegemea zana zinazozalisha nyaraka, mifano, na vijiti vya mteja kutoka ubainishaji ili mtu wa jumla aweze kudumisha kiolesura bila utaalamu wa kina wa itifaki. Pima kununua dhidi ya kujenga kwa nguvu: lango lililotengenezwa tayari au jukwaa la usimamizi wa API linakupa kupunguza kasi ya maombi, funguo, na tovuti ya wasanidi ambayo vinginevyo ungeunda kwa mkono. Weka uso mdogo na desturi thabiti, kwa kuwa kila kiungo cha ziada na kila muundo wa kosa wa mara moja ni kitu ambacho timu nyembamba lazima iuunge mkono milele.

**Biashara kubwa.** Kuvuka timu nyingi huru, tatizo kuu ni uthabiti bila kuwa kikwazo: mwongozo wa mtindo wa pamoja, mapitio ya viwango vya API, orodha inayofanya violesura vipatikane, na ukaguzi wa kiotomatiki wa utangamano wa nyuma kwenye CI ili mavunjiko ya kimya yashinde ujenzi badala ya uunganishaji. Tawala kila API kama bidhaa yenye mmiliki aliyetajwa, mzunguko wa maisha, na sera iliyochapishwa ya kustaafisha, na upime kupokelewa, mzigo wa msaada, na mzunguko wa mabadiliko yanayovunja ili jalada libaki na afya. Sawazisha mitindo ya mwingiliano na kanuni za matoleo shirika zima, kwa sababu kwa ukubwa huu mgawanyiko ndio chaguo-msingi ghali.

**Serikali.** Kanuni za ununuzi, maagizo ya viwango huria, na uwajibikaji wa umma huunda kila chaguo. Chapisha mkataba hadharani, fuata viwango huria vilivyoamriwa, na utoe eneo la majaribio na nyaraka za marejeo ili wasanidi wa nje usioweza kuratibu nao waweze kujihudumia. Chukulia utangamano wa nyuma wa muda mrefu kama sharti la sera, kwa kuwa uunganishaji lazima uokoke kuvuka tawala na mabadiliko ya wasambazaji, na ufanye mabadiliko yanayovunja yawe nadra, yanayotawaliwa kwa nguvu, na yanayotangazwa mapema sana. Weka API na nyaraka zake za uwazi vya kutosha kuhimili uchunguzi wa umma na ukaguzi, na uepuke miundo ya umiliki ambayo ingenasa tawala ya baadaye.

## Mifano

**Kampuni changa.** Kampuni changa ya hatua ya mbegu inayosafirisha API yake ya kwanza ya umma inaandika mkataba kama ubainishaji unaosomeka na mashine kabla ya kuandika msimbo, kwa hiyo wateja wake wawili wa washirika wa usanifu wanaweza kuunganisha dhidi ya mfano wakati seva bado inajengwa. Hata ikiwa na watumiaji wachache tu, inaongeza funguo za kutobadilisha matokeo kwenye kiungo cha tozo na ugawaji wa kurasa wa kielekezi kwenye kila orodha, kwa sababu kuvirekebisha washirika wanapotegemea API kungemaanisha badiliko linalovunja ambalo haiwezi kulimudu. Mkataba wa awali unagharimu siku moja na kuokoa wiki za kurudi-na-kurudi kwa msaada.

**Biashara kubwa.** Kampuni kubwa ya malipo inaonyesha API ya umma ya REST kwa maelfu ya wafanyabiashara. Kila kiungo cha uandishi kinakubali ufunguo wa kutobadilisha matokeo, kwa hiyo kujaribu upya kwa mtandao hakuundi tozo mbili kamwe. Kila kiungo cha orodha kinatumia ugawaji wa kurasa wa kielekezi. Makosa yanabeba misimbo thabiti iliyoandikwa katika marejeo ya umma. Sera rasmi ya kustaafisha inahakikisha dirisha refu la msaada kwa toleo lolote, pamoja na taarifa ya mapema na miongozo ya uhamiaji. Nidhamu hii ni faida ya ushindani: waunganishaji wanaamini kwamba API haitavunjika chini yao.

**Serikali.** Huduma ya kidijitali ya taifa inachapisha API huria kwa data ya raia, ikifuata viwango huria vilivyoamriwa na mchakato wa usanifu wa API-kwanza. Mkataba unabainishwa na kupitiwa kabla ya ujenzi, unachapishwa katika orodha ya kati ya API za serikali, na kutolewa pamoja na eneo la majaribio, kwa hiyo wasanidi wa wengine, ambao hawawezi kuratibiwa mmoja mmoja, wanaweza kuunganisha wenyewe. Utangamano wa nyuma wa muda mrefu ni sharti la sera, kwa sababu uunganishaji lazima uokoke kuvuka tawala na mabadiliko ya wasambazaji. Kwa hiyo mabadiliko yanayovunja ni nadra na yanatawaliwa kwa nguvu.

## Kesi ya biashara: sababu, ROI, na TCO

Usanifu mzuri wa API hupunguza gharama ya uunganishaji, ambayo mara nyingi ndiyo gharama kubwa zaidi ya kuunganisha mifumo na kutambulisha washirika. Kwa API iliyo wazi, thabiti, iliyoandikwa vizuri, watumiaji huunganisha ndani ya siku bila tiketi hata moja ya msaada. Mbaya huzalisha mzigo usioisha wa msaada, uunganishaji ulioshindwa, na uharibifu wa sifa. API yenyewe inapokuwa bidhaa, uzoefu wa msanidi huendesha moja kwa moja kupokelewa na mapato.

Gharama kubwa zaidi iliyofichika ni mabadiliko yanayovunja. Kila badiliko linalovunja hulazimisha uhamiaji ulioratibiwa kuvuka watumiaji wote, timu za ndani na washirika wa nje vilevile, na gharama ya jumla inapanuka na idadi ya watumiaji na ugumu wao wa kuhama kwa pamoja. Kuwekeza mapema katika usanifu wa mkataba-kwanza, utangamano wa nyuma, na nidhamu ya matoleo huepuka matukio haya ya ghali ya uhamiaji wa shirika zima. Unapozungumza na uongozi, weka ubora wa API kama kiegemeo cha uhuru wa timu, ukuaji wa mfumo wa ikolojia wa washirika, na kuepuka uhamiaji wa kulazimishwa wa gharama. Fuatilia muda wa uunganishaji, kiasi cha tiketi za msaada, na mzunguko wa mabadiliko yanayovunja kama ushahidi wako.

## Mifumo mibaya na mitego

- **API za utekelezaji-kwanza:** kiolesura kinavuja muundo wa ndani wa hifadhidata na kinabadilika kila utekelezaji unapobadilika.
- **Mabadiliko yanayovunja kimya:** kutumia upya sehemu au kukaza uthibitishaji bila kupandisha toleo huvunja watumiaji bila kutabirika.
- **Violesura vya mazungumzo mengi:** miundo inayohitaji safari nyingi za kwenda-na-kurudi kwa shughuli moja ya kimantiki, ikidhuru utendaji na uwezo wa kutumika.
- **Desturi zisizo thabiti:** kila kiungo kinavumbua majina yake, muundo wa kosa, na ugawaji wa kurasa, kwa hiyo wateja hawawezi kujumlisha.
- **Hakuna ugawaji wa kurasa wala kupunguza kasi:** viungo vinavyofanya kazi kwenye majaribio na kuporomoka chini ya ujazo halisi wa data au mzigo.
- **Uandishi usiobadilisha matokeo:** kujaribu upya husababisha nakala; hitilafu moja ya mtandao huharibu data.
- **Kuenea kwa matoleo:** matoleo mengi mno hai bila kustaafisha, yakizidisha matengenezo hadi yasiweze kudhibitiwa.
- **Nyaraka kama wazo la baadaye:** marejeo yasiyoandikwa au yaliyochakaa yanayosukuma gharama yote ya uunganishaji kwa watumiaji.

## Kielelezo cha ukomavu

- **Ngazi ya 1, Kuanzisha:** API huibuka kutoka utekelezaji kama zao la pembeni; hakuna desturi za pamoja; kiolesura kinavuja muundo wa ndani wa hifadhidata; mabadiliko yanayovunja ni ya kawaida, hayatangazwi, na yanagunduliwa uunganishaji wa mtumiaji unaposhindwa.
- **Ngazi ya 2, Kuendeleza:** Baadhi ya timu hufuata desturi za msingi za REST, huweka matoleo bila rasmi, na kuandika nyaraka kwa mkono, lakini mazoea hayana uthabiti kuvuka timu; kutobadilisha matokeo, ugawaji wa kurasa, na kupunguza kasi huonekana kwenye viungo vingine na si vingine; watumiaji bado wanajifunza hulka za kila API kesi kwa kesi.
- **Ngazi ya 3, Kusawazisha:** Usanifu wa mkataba-kwanza wenye ubainishaji unaosomeka na mashine umeandikwa na kutekelezwa shirika zima; sera iliyochapishwa ya kustaafisha, maana thabiti ya makosa, na kutobadilisha matokeo, ugawaji wa kurasa wa kielekezi, na kupunguza kasi vya lazima vinatumika kwa kila kiungo kipya; mwongozo wa mtindo wa pamoja na mapitio ya viwango vya API huweka violesura thabiti kuvuka timu.
- **Ngazi ya 4, Kusimamia:** Jalada la API linapimwa na kudhibitiwa dhidi ya vipimo vya msingi: ukaguzi wa kiotomatiki wa utangamano wa nyuma unazuia kila badiliko kwenye CI, na unafuatilia muda hadi wito wa kwanza wenye mafanikio, kiasi cha tiketi za msaada kwa kila kiungo, mzunguko wa mabadiliko yanayovunja, idadi ya matoleo hai, na matumizi kwa kila kiungo ili maamuzi ya kustaafisha na usanifu yasimame kwenye ushahidi badala ya maoni. Kila API ni bidhaa inayotawaliwa katika orodha yenye mmiliki aliyetajwa, na vipimo huchochea hatua huduma inapoteleza kutoka malengo yake.
- **Ngazi ya 5, Kuratibu:** Mkakati wa API unaboreshwa kila wakati na kuunganishwa kuvuka shirika; orodha, lango, kanuni za matoleo, na malango ya utangamano hufanya kazi kama mfumo mmoja; shirika mara kwa mara hustaafisha, kuunganisha, na kupanga upya wigo wa violesura kulingana na kupokelewa na gharama zilizopimwa; viwango vya mtindo wa mwingiliano na matoleo hubadilika mfumo wa ikolojia, washirika, na teknolojia vinapohama, na mabadiliko yanayovunja ni nadra na yanasimamiwa vyema.

## Mawazo ya kujadili

- Unaamuaje lini API ya ndani ni thabiti vya kutosha kuchapishwa nje?
- Dirisha sahihi la msaada kwa matoleo yaliyostaafishwa katika muktadha wenu ni lipi, na nani analilipia?
- GraphQL au gRPC zinapaswa kuchukua nafasi ya REST ndani wapi, na wapi zingeongeza ugumu zaidi ya thamani?
- Unatekelezaje uthabiti wa API kuvuka timu nyingi huru bila kuwa kikwazo?
- API zinazotumiwa na AI na violesura vya zana za wakala vinapaswa kubadilishaje desturi zako za usanifu?
- Ni ukaguzi gani wa kiotomatiki unaweza kunasa mabadiliko yasiyooana nyuma kabla hayajatolewa?

## Mambo muhimu ya kukumbuka

- Buni mkataba kwanza; API ni bidhaa na ahadi ya muda mrefu.
- Utangamano wa nyuma hulinda watumiaji; mabadiliko yanayovunja yanahitaji matoleo mapya na njia za uhamiaji.
- Chagua REST, GraphQL, gRPC, au matukio kwa kufaa mwingiliano, si mtindo wa mitindo.
- Jenga kutobadilisha matokeo, ugawaji wa kurasa, kupunguza kasi, na makosa thabiti tangu siku ya kwanza.
- Tawala API kama bidhaa zenye wamiliki, orodha, na uzoefu imara wa msanidi.

## Marejeo na usomaji zaidi

- Roy Fielding, *Architectural Styles and the Design of Network-based Software Architectures* (dissertation)
- Arnaud Lauret, *The Design of Web APIs*
- Mike Amundsen, *RESTful Web APIs* and *Design and Build Great Web APIs*
- Sam Newman, *Building Microservices*
- OpenAPI Specification; JSON Schema (as reference standards)
- Martin Kleppmann, *Designing Data-Intensive Applications*
