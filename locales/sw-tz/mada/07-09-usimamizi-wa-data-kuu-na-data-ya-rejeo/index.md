# 7.9 Usimamizi wa data kuu na data ya rejeo

## Muhtasari na msukumo

Uliza mifumo mitano shirika lina wateja wangapi, na utapata namba tano tofauti. Mmoja unahesabu anwani za barua pepe, mwingine mikataba, mwingine kuingia, na miwili hayakubaliani kama "Acme Corp" na "ACME Corporation" ni kampuni ileile. [Usimamizi wa data kuu](https://en.wikipedia.org/wiki/Master_data_management) (MDM) ni nidhamu ya kupatanisha vyombo vya msingi ambavyo biashara yako inashiriki, mteja, bidhaa, msambazaji, mfanyakazi, eneo, kuwa toleo moja lenye mamlaka ambalo kila mfumo unaweza kuliamini.

Anza kwa kupanga data yako katika aina tatu, kwa sababu zinahitaji matibabu tofauti. Data kuu inaelezea nomino za biashara yako: watu, mahali, na vitu ambavyo michakato mingi inarejelea. Data ya rejeo ni msamiati unaodhibitiwa ambao michakato hiyo inatumia: misimbo ya sarafu, misimbo ya nchi, orodha za vipimo, kategoria za bidhaa. Data ya miamala hurekodi vitenzi: agizo lililowekwa, malipo yaliyofanywa, shehena iliyotumwa. Data kuu na ya rejeo ni ya kiasi kidogo kuliko miamala lakini inarejelewa kila mahali, kwa hiyo kosa ndani yake huchafua kila kitu cha chini ya mkondo.

Gharama ya kukosea ni madhubuti. Mteja yuleyule anapokuwepo kama rekodi nne tofauti kidogo, unatuma katalogi nne, huwezi kuona uhusiano mmoja unaostahili kuhifadhiwa, na namba yako ya mapato kwa kila mteja si sahihi kimyakimya. [Rekodi ya dhahabu](https://en.wikipedia.org/wiki/Single_source_of_truth), toleo moja linaloaminika la chombo lililokusanywa kutoka vyanzo vingi, ndiyo inayochukua nafasi ya nakala hizo zinazopingana, ili kila muunganisho uache kutatua tena tatizo lilelile la kulinganisha.

Kwa mashirika yanayopatanisha mifumo iliyokusanywa kwa miongo ya ukuaji na ununuzi, MDM ndiyo tofauti kati ya mtazamo thabiti wa mteja na kodi ya upatanisho ya kudumu. Kwa serikali, dau linapanda: raia anayeonekana kama watu watatu tofauti katika mawakala watatu anaweza kunyimwa manufaa, kutozwa kodi mara mbili, au kupotea kati ya idara. Sura hii inakamilisha mkakati wa data na utawala (sura ya 7.1), unaoweka umiliki na sera; uundaji wa data na safu ya kisemantiki (sura ya 7.7), inayofafanua vyombo vinamaanisha nini; na ubora wa data na uonekanaji (sura ya 7.8), unaoweka rekodi safi kwa muda.

## Kanuni kuu

- Panga data yako kuwa kuu, ya rejeo, na ya miamala; kila moja inahitaji ushughulikiaji tofauti.
- Rekodi moja ya dhahabu kwa kila chombo cha ulimwengu halisi, iliyokusanywa kwa makusudi, si kugunduliwa kwa bahati.
- Chagua mtindo wa usanifu wa MDM kufaa udhibiti na ucheleweshaji wako, si mitindo.
- Kulinganisha na kuokoka ni kanuni za biashara, kwa hiyo ziandike na uwaruhusu wasimamizi kuzirekebisha.
- Data ya rejeo ni msamiati wa pamoja; iwekee matoleo na uichapishe kama API.
- Utawala na usimamizi ndio injini ya MDM; programu ni zana tu.
- Sambaza rekodi za dhahabu kama matukio ili mifumo ya chini ya mkondo ibaki sawia, si iliyochakaa.
- Pima MDM kwa maamuzi yaliyoboreshwa na nakala zilizoondolewa, si rekodi zilizopakiwa.

## Mapendekezo

### Ainisha data kuu, ya rejeo, na ya miamala kwanza

Huwezi kusimamia usichopanga, kwa hiyo anza kwa kuainisha maeneo yako ya data. Jaribio muhimu la data kuu ni kama thamani isiyo sahihi inasambaa: ikiwa anwani moja mbaya inasambaa kwenye bili, usafirishaji, na notisi za kisheria, unatazama data kuu. Hii inaendesha uwekezaji wako: unajenga injini ya kulinganisha kwa chombo cha mteja, si mistari ya vitu vya maagizo. Taja maeneo waziwazi, yapange kwa maumivu ambayo marudio yake yanasababisha, na anza na moja au mawili yanayoumiza zaidi, kwa kawaida mteja na bidhaa kwa sababu zinagusa mapato moja kwa moja.

### Chagua mtindo wa usanifu wa MDM kwa makusudi

Kuna mitindo minne ya kawaida ya usanifu, na ule sahihi unategemea mamlaka kiasi gani unaweza kuweka kati na jinsi mabadiliko yanavyopaswa kusambaa haraka. Mtindo wa rejista huacha data kwenye mifumo chanzo na hujenga faharasa ya vitambulisho vilivyolinganishwa tu, kwa hiyo unaweza kujibu "rekodi hizi tano ni mteja yuleyule" bila kuhamisha data yoyote; ni nafuu na wa hatari ndogo, lakini wa kusoma tu, kwa hiyo hauwezi kurekebisha vyanzo. Mtindo wa kuunganisha huvuta nakala kwenye kitovu cha kati na kuziunganisha kuwa rekodi za dhahabu kwa kuripoti, lakini hausukumi marekebisho nyuma, kwa hiyo vyanzo vinabaki fujo. Mtindo wa kuishi pamoja unaenda mbali zaidi: unasawazisha thamani zilizosafishwa kurudi kwenye mifumo chanzo, kwa hiyo vyanzo vinaboreka kwa muda huku bado vikifanya kazi kwa uhuru. Mtindo wa kitovu cha kati au cha miamala hufanya kitovu cha MDM kuwa mfumo rasmi wenyewe, ambapo vyombo vinaundwa na kuhaririwa moja kwa moja na kila mfumo mwingine unatumia kutoka kwake; hii inatoa uthabiti na udhibiti imara zaidi, na ndio mgumu zaidi kuupokea kwa sababu unabadilisha mahali kazi inapofanyika. Mashirika mengi huendelea kutoka rejista inayothibitisha thamani kuelekea kuishi pamoja uaminifu unavyokua, na kuendesha zaidi ya mtindo mmoja kuvuka maeneo tofauti.

### Linganisha, unganisha, na weka kanuni za kuokoka waziwazi

Moyo wa MDM ni kuamua lini rekodi mbili zinaelezea kitu kilekile cha ulimwengu halisi. Hii ni [kuunganisha rekodi](https://en.wikipedia.org/wiki/Record_linkage), mara chache rahisi kama mlingano wa ufunguo kamili kwa sababu data halisi imejaa makosa ya kuandika, vifupisho, na nyanja zinazokosekana. Ulinganishaji wa kuamuliwa hutumia kanuni kamili kwenye nyanja zilizochaguliwa (kitambulisho cha kodi kilekile, au barua pepe pamoja na msimbo wa posta). Ulinganishaji wa uwezekano hupima ufanano kuvuka nyanja nyingi kwa [ulinganishaji wa takriban wa mifuatano](https://en.wikipedia.org/wiki/Approximate_string_matching) na uzito, ili "Bob Smith, 12 Main St" na "Robert Smith, 12 Main Street" vihukumiwe kuwa mlingano unaowezekana juu ya kizingiti. Kuamua rekodi zipi zinarejelea chombo kimoja kunaitwa utatuzi wa utambulisho, na unaendesha kila kitu kutoka mitazamo ya wateja hadi kugundua ulaghai.

Rekodi zinapolingana, lazima uamue thamani zipi zinaokoka kwenye rekodi ya dhahabu. Kanuni hizi za kuokoka ni mantiki ya biashara, kwa hiyo zifanye wazi: pendelea thamani ya hivi karibuni kwa namba ya simu, thamani kamili zaidi kwa anwani, chanzo kinachoaminika zaidi kwa jina la kisheria. Weka bendi ya kizingiti ambapo ulinganishaji unaunganishwa kiotomatiki, bendi ya chini ambapo unakataliwa kiotomatiki, na bendi ya kati ambapo binadamu anaamua, ambapo usimamizi unaishi. Weka kila muunganisho ukirekebishika na kuandikwa, kwa sababu muunganisho usio sahihi unaounganisha wateja wawili halisi ni mbaya kuliko ulinganishaji uliokosekana.

### Chukulia data ya rejeo kama msamiati wa pamoja wenye matoleo

Data ya rejeo ni msamiati wa pamoja ambao mifumo yako inazungumza, na msamiati unaoteleza husababisha kutolingana kimya: mfumo mmoja ukitumia msimbo wa nchi wa ISO "GB" na mwingine "UK," viungo vinashindwa na hesabu zinatofautiana. Dumisha kila orodha ya rejeo mahali pamoja palipotawaliwa, ichapishe kwa kila mtumiaji, na, muhimu, iwekee matoleo. Misimbo huongezwa, kustaafishwa, kugawanywa, na kuunganishwa kwa muda, na ukiandika orodha juu yake, unavunja ripoti za kihistoria zilizokuwa sahihi chini ya misimbo ya zamani.

Chukulia seti ya data ya rejeo kama API yenye mkataba. Ichapishe na tarehe zinazotumika ili mtumiaji aweze kuuliza "misimbo ya kanda halali ilikuwa ipi tarehe hii," weka misimbo iliyostaafishwa badala ya kuifuta, na urekodi ulinganishaji msimbo unapobadilisha maana. Pendelea viwango vya nje vinavyotambulika pale vilipo, kama misimbo ya nchi na sarafu ya ISO, kwa sababu viwango vinakupa uwezo wa kuingiliana bure na vinaunganika na nidhamu ya viwango huria katika sura ya 3.8.

### Unda madaraja ya uongozi na uhusiano, si rekodi tambarare tu

Data kuu si rundo la safu huru; ni utando wa uhusiano. Mteja ni wa kaya na wa kampuni mama. Bidhaa inakusanyika kwenye kategoria na chapa. Madaraja haya ya uongozi hubeba maana halisi ya biashara: kusanya mauzo kwa kampuni mama na picha inabadilika kabisa kutoka kukusanya kwa akaunti moja moja. Unda uhusiano huu waziwazi ili watumiaji wapitie kwa uthabiti badala ya kila timu kubuni ukusanyaji wake.

Tazama kesi ambapo chombo kimoja kinahitaji madaraja kadhaa kwa wakati mmoja. Bidhaa inaweza kukusanyika kwa njia moja kwa fedha na nyingine kwa uuzaji wa bidhaa, na zote mbili ni halali, kwa hiyo unga mkono madaraja kadhaa yaliyotajwa badala ya kulazimisha mti mmoja wa kweli. Uhusiano kati ya maeneo pia unajalisha, kama msambazaji gani anatoa bidhaa ipi.

### Unganisha rekodi za dhahabu na safu ya kisemantiki na ubora wa data

Rekodi za dhahabu ambazo MDM inazalisha ndizo vyombo vya kuaminika ambavyo safu ya kisemantiki ya sura ya 7.7 inavirejelea inapofafanua vipimo: "wateja hai" inamaanisha kitu tu wakati "mteja" ni wazi. Lisha rekodi zako za dhahabu kwenye safu ya kisemantiki ili kila kipimo kihesabu vyombo vilevile vilivyoondolewa nakala, vilivyotatuliwa.

MDM na ubora wa data (sura ya 7.8) ni pande mbili za sarafu moja: ukaguzi wa ubora hugundua nakala, thamani tupu, na ukiukaji wa umbo ambao MDM kisha huvitatua, na ulinganishaji wa MDM hufichua matatizo ya ubora ambayo ukaguzi ulikosa. Endesha ufuatiliaji endelevu wa ubora kwenye data yako kuu hasa: viwango vya nakala, usambazaji wa imani ya ulinganishaji, ukamilifu wa nyanja muhimu, na ukubwa wa foleni ya mapitio, ili kuteleza kujitokeze kabla watumiaji hawajaona.

### Sambaza rekodi za dhahabu kupitia matukio

Rekodi ya dhahabu ambayo hakuna mfumo wa chini ya mkondo unaiona haimsaidii yeyote. Mfumo imara zaidi ni uenezaji unaoendeshwa na matukio: chombo kinapoundwa, kuunganishwa, au kusahihishwa, kitovu cha MDM huchapisha tukio la badiliko, na mifumo inayojiandikisha husasisha nakala zao za ndani. Hii inajengwa juu ya [usanifu unaoendeshwa na matukio](https://en.wikipedia.org/wiki/Event-driven_architecture) na mifumo ya kutiririka ya sura ya 7.2, ikiweka mifumo kadhaa thabiti bila usawazishaji dhaifu wa kundi la usiku unaomwacha kila mtu amechakaa kwa siku.

Chapisha matukio kwa muktadha wa kutosha wa manufaa: kitambulisho cha chombo, kilichobadilika, thamani mpya zilizookoka, na toleo ili watumiaji waweze kupanga masasisho na kugundua yaliyokosekana. Fanya watumiaji wawe na kutobadilika thamani ili kucheza tukio upya kusidhuru, na utoe API kwa mifumo isiyoweza kujiandikisha. Kanuni kutoka usanifu wa data na uhifadhi (sura ya 3.4) inatumika: sanifu rekodi ya dhahabu itiririke, kwa sababu ile ambayo hakuna anayeitumia ni lahajedwali ghali tu.

### Gawa usimamizi na utawala kabla ya zana

MDM hushindwa kama mradi wa teknolojia na hufanikiwa kama wa utawala. Jukumu muhimu ni [msimamizi wa data](https://en.wikipedia.org/wiki/Data_steward), mtu anayewajibika kwa ubora na kanuni za eneo mahususi, anayetatua ulinganishaji wenye utata, kurekebisha kanuni za kuokoka, na kupatanisha idara mbili zinapotofautiana kuhusu "msambazaji" inamaanisha nini. Wasimamizi kwa kawaida ni watu wa biashara wenye maarifa ya kina ya eneo, si wahandisi, na wanahitaji mamlaka halisi na muda uliotengwa, kwa sababu usimamizi wa muda mfupi bila mamlaka huzalisha hasa kuteleza ambako MDM ilikusudiwa kukomesha.

Zungushia wasimamizi miundo ya utawala kutoka sura ya 7.1: mmiliki wa data anayewajibika kwa kila eneo, baraza la kutatua migogoro ya kuvuka maeneo, na sera wazi za nani anaweza kuunda au kuunganisha rekodi kuu. Andika maamuzi, kwa sababu kanuni za kulinganisha mteja ni maarifa ya kitaasisi yanayopaswa kuokoka mabadiliko ya wafanyakazi. Zana hutumikia utawala; kununua jukwaa la MDM kabla ya kutaja wasimamizi wako ni kununua injini bila dereva.

## Mabadilishano: faida na hasara

| Mtindo wa MDM | Faida | Hasara |
|---|---|---|
| Rejista (faharasa tu) | Nafuu, hatari ndogo, vyanzo havigusiwi | Kusoma tu; haiwezi kurekebisha data chanzo |
| Kuunganisha (nakala za kati) | Rekodi safi kwa uchanganuzi haraka | Vyanzo vinabaki fujo; hakuna uandishi wa kurudi |
| Kuishi pamoja (sawazisha kurudi kwa vyanzo) | Vyanzo vinaboreka; udhibiti uliosawazishwa | Muunganisho zaidi; migogoro ya usawazishaji ya kusimamia |
| Kitovu cha kati / cha miamala | Uthabiti na udhibiti imara zaidi | Gharama ya juu zaidi; hubadilisha kazi inapofanyika |
| Ulinganishaji wa kuamuliwa | Unaotabirika, unaoelezeka, unaokaguliwa | Hukosa makosa ya kuandika, tofauti, na data fujo |
| Ulinganishaji wa uwezekano | Hunasa tofauti za ulimwengu halisi | Inahitaji kurekebishwa; miunganisho ya uongo ukifanywa kizembe |

Mvutano wa msingi katika MDM ni udhibiti dhidi ya usumbufu. Mitindo inayokupa data safi na thabiti zaidi (kuishi pamoja na vitovu vya kati) ndiyo hasa inayovamia zaidi jinsi mifumo chanzo na wamiliki wake wanavyofanya kazi, na uvamizi huo ndipo programu za MDM zinapokwama. Njia ya kiutendaji ni kupata uaminifu kwa mtindo wa hatari ndogo na kusogea kuelekea udhibiti imara zaidi pale tu kesi ya biashara ni wazi. Mabadilishano ya ulinganishaji yanaendana: kanuni za kuamuliwa zinakaguliwa lakini dhaifu, alama ya uwezekano ina nguvu lakini inadai usimamizi na uvumilivu wa muunganisho usio sahihi wa mara kwa mara. Programu nyingi zilizokomaa huchanganya zote mbili.

## Maswali ya kujadili na timu yako

1. **Maeneo gani ya data kuu yanasababisha maumivu kweli kwetu, na je, tumeyapanga kwa gharama badala ya kuyashughulikia yote mara moja?** Programu nyingi za MDM huporomoka chini ya tamaa yake yenyewe, zikijaribu kusimamia kila chombo katika shirika mara moja na kutoa kitu hakuna kwa miaka miwili. Hatua yenye tija ni kupata eneo moja au mawili ambapo marudio na migogoro vinakugharimu fedha au uaminifu halisi, kwa kawaida mteja au bidhaa, na kupima gharama hiyo: barua zilizopotea, saa za upatanisho, namba zisizo sahihi za mapato, matokeo ya ukaguzi. Leta mifano madhubuti ya chombo kilekile kinachoonekana kwa njia nyingi kuvuka mifumo yenu, na uache mpangilio huo ukuambie wapi pa kuanzia, kwa sababu ushindi finyu, unaopimika hujenga sifa unayohitaji kupanuka.

2. **Nani anamiliki kila eneo la data kuu, na je, wasimamizi wetu wana mamlaka na muda wa kufanya kazi kweli?** Zana za MDM bila usimamizi uliowezeshwa ni gari bila dereva, na njia ya kawaida zaidi ya kushindwa ni kutaja msimamizi kwenye slaidi huku ukimpa hakuna mamlaka halisi wala saa zilizotengwa. Watu wanaotatua ulinganishaji wenye utata na kusuluhisha mabishano ya "nini kinahesabika kama mteja" wanahitaji utaalamu wa eneo, mamlaka ya uamuzi, na muda uliolindwa. Leta chati yenu ya shirika na uliza, kwa eneo lenu kuu, hasa nani anaamua rekodi mbili ni mtu yuleyule na nani anapatanisha mauzo na fedha zinapotofautiana. Kama huwezi kutaja mtu huyo na kuelekeza muda wake uliotengwa, mmepata pengo litakalozamisha programu.

3. **Tunapounganisha rekodi mbili kuwa rekodi ya dhahabu, tunaweza kueleza na kutendua uamuzi, na thamani zilizookoka zinatoka wapi?** Kanuni za kuokoka ni mantiki ya biashara ambayo timu nyingi hazijawahi kuiandika, jambo linalomaanisha miunganisho hutokea kwa bahati ya mpangilio wa upakiaji au chaguo-msingi za zana, na muunganisho usio sahihi unaounganisha wateja wawili halisi ni mgumu kufungua. Leta rekodi halisi iliyounganishwa na ufuatilie kila uga uliookoka hadi chanzo chake na kanuni: kwa nini anwani hii, kwa nini jina hili, kwa nini namba hii ya simu. Thibitisha kwamba kila muunganisho umeandikwa na unarekebishika, na kwamba bendi ya kati ya ulinganishaji wenye shaka inaenda kwa binadamu badala ya kuunganishwa kiotomatiki. Kama huwezi kueleza rekodi mahususi ya dhahabu, wasimamizi wenu hawawezi kuitetea kwa mkaguzi au mteja aliyedhulumiwa.

4. **Mtindo upi wa usanifu wa MDM unafaa kila eneo tunalopanga kusimamia, na tunaweza kutetea chaguo hilo dhidi ya usumbufu unaosababisha kwa wamiliki wa mifumo chanzo?** Mtindo mnaochagua unaamua mnaweza kusafisha data kiasi gani na mnavamia kiasi gani timu zinazomiliki vyanzo, na kuchagua kwa mitindo au ofa ya muuzaji badala ya uhalisia wa udhibiti-dhidi-ya-usumbufu ndivyo programu zinavyokwama nusu njia. Rejista inathibitisha thamani kwa bei nafuu lakini haisafishi chanzo kamwe; kitovu cha kati kinatoa uthabiti imara zaidi lakini kinahamisha mahali rekodi zinapoundwa, ambalo ni badiliko la kishirika lililovaa kama la kiufundi. Leta, kwa kila eneo mgombea, usomaji wa uaminifu wa mamlaka kiasi gani mnayoshikilia juu ya wamiliki wa vyanzo, nakala za chini ya mkondo lazima ziwe mpya kiasi gani, na uandishi wa kurudi ungevunja nini kwenye mtiririko wa kazi uliopo. Katika mazingira ya mashirika makubwa na serikali, ongeza gharama ya uhamishaji na usimamizi wa mabadiliko ya kuhamisha mfumo rasmi, kwa sababu timu ambazo kazi yao ya kila siku inahama zitapinga kitovu ambacho hazikushauriwa kuhusu, na utekelezaji wa kuishi pamoja uliokwama ni ghali zaidi kuliko rejista ya wastani inayosafirishwa.

5. **Tunarekebisha vipi vizingiti vya ulinganishaji, na je, tumekubaliana kiwango gani cha miunganisho ya uongo na ulinganishaji uliokosekana tunachoweza kuishi nacho katika kila eneo?** Kila injini ya ulinganishaji wa uwezekano hubadilishana miunganisho ya uongo (kuunganisha vyombo viwili halisi) dhidi ya ulinganishaji uliokosekana (kuacha chombo kimoja kimegawanyika), na usawa ni uamuzi wa biashara, si chaguo-msingi lililoachwa na mtu kwenye zana. Weka bendi za kuunganisha kiotomatiki na kukataa kiotomatiki pana mno na unaharibu rekodi za dhahabu kimyakimya; zifanye nyembamba mno na foleni ya mapitio ya binadamu inakua haraka kuliko wasimamizi wanavyoweza kuisafisha. Leta usambazaji wa sasa wa imani, ukubwa na umri wa foleni ya mapitio, na makosa ya sampuli ya aina zote mbili ili chumba kione gharama halisi ya kila mwelekeo. Katika eneo la utambulisho la serikali, egemea sana ulinganishaji uliokosekana na mapitio ya binadamu, kwa sababu muunganisho usio sahihi unaweza kumnyima mtu manufaa au kufichua data ya raia mmoja kwa mwingine, na gharama ya rufaa na ukaguzi ya kosa hilo inazidi gharama ya nakala ambayo msimamizi anaitatua wiki ijayo.

6. **Mifumo ya chini ya mkondo inajifunzaje rekodi ya dhahabu imebadilika, na kila moja inaweza kuchakaa kiasi gani kabla uamuzi haujaenda vibaya?** Rekodi ya dhahabu iliyotatuliwa kikamilifu ambayo hakuna mfumo unaoitumia ni lahajedwali ghali, na utaratibu wa kusambaza, iwe matukio ya mabadiliko, API ya kujiandikisha, au kundi la usiku, kimyakimya huweka jinsi kila uamuzi tegemezi ulivyo wa sasa. Uenezaji unaoendeshwa na matukio huweka watumiaji kadhaa karibu na wakati halisi lakini unadai watumiaji wenye kutobadilika thamani na matukio yenye matoleo; usawazishaji wa usiku ni rahisi lakini unamwacha kila mtu amechakaa kwa siku, ambayo inaweza kuwa sawa kwa orodha ya masoko na hatari kwa ukaguzi wa ulaghai. Leta orodha ya mifumo inayotumia, usafi ambao kila mmoja unahitaji kweli, na jinsi mtumiaji aliyekosa sasisho leo anavyopona. Kwa shirika kubwa au la umma, taja nani anamiliki mkataba wa matukio haya na jinsi mteja anavyogundua ujumbe uliodondoshwa, kwa sababu badiliko la chombo linaloshindwa kimya kufika kwa wakala mmoja linaunda upya mgawanyiko ambao MDM ilifadhiliwa kuuondoa.

## Mtazamo wa sekta

**Kampuni changa.** Ukiwa na wahandisi wachache na bila muda wa ziada, usinunue jukwaa la MDM. Simamia chombo kimoja kinachoharibu namba zako, kwa kawaida mteja aliyerudiwa kuvuka kujisajili na mauzo, kwa kazi ya kulinganisha kwenye ghala unaloendesha tayari na mtu mmoja anayepitia ulinganishaji wenye shaka kila wiki. Weka kila muunganisho ukiandikwa na kurekebishika ili kanuni mbaya igharimu alasiri, si uhusiano wa mteja, na urudi kwenye zana nzito zaidi tu foleni ya mapitio ya mkono inapozidi mpitiaji mmoja.

**Biashara ndogo.** Huna msimamizi wa data na bajeti finyu, kwa hiyo chukulia hili kama uamuzi wa kununua-si-kujenga na egemea viwango unavyopata bure. Pendelea zana zinazoondoa nakala za mawasiliano tayari na kuzungumza misimbo ya nchi na sarafu ya ISO kuliko kitovu maalumu usiloweza kudumisha, na uchague eneo moja, kwa kawaida wateja au bidhaa, ambapo nakala zinakugharimu fedha halisi. Gawa uwajibikaji kwa mmiliki aliyetajwa hata kama ni sehemu ya wiki ya mtu mmoja, kwa sababu msamiati unaoteleza bila mtu anayetazama ndio unaovunja ripoti zako kimyakimya.

**Biashara kubwa.** Kuvuka ERP na CRM kadhaa zilizokusanywa kwa ununuzi, kazi ni utawala wa jalada: panga maeneo kwa gharama ya marudio yao, simamisha wasimamizi waliowezeshwa kwenye biashara, na usawazishe kanuni za kuokoka na matoleo ya data ya rejeo ili vikundi viache kutatua tena tatizo lilelile la kulinganisha. Weka bajeti ya muunganisho na gharama ya kudumu ya usimamizi waziwazi, sambaza rekodi za dhahabu kama matukio yenye matoleo ili vyanzo viboreke kwa muda, na usimamie MDM kama programu iliyopimwa yenye viwango vya nakala na vipimo vya foleni ya mapitio badala ya usafishaji wa mara moja.

**Serikali.** Kanuni za ununuzi, sheria kali za kushiriki data, na uwajibikaji wa umma huumba kila uchaguzi. Funga chombo cha mtu kwa kitambulisho cha kitaifa kilichotawaliwa, weka matoleo kwenye data ya rejeo kwa tarehe zinazotumika ili rekodi za kihistoria zibaki sahihi, na ufanye utatuzi wa utambulisho uwe wa tahadhari kwa makusudi: ulinganishaji wenye shaka unaenda kwa wasimamizi waliofunzwa, kamwe miunganisho ya kiotomatiki, kwa sababu muunganisho usio sahihi unaweza kumnyima mtu manufaa au kuvujisha data ya raia mmoja kwa mwingine. Andika kila ulinganishaji kwa ukaguzi na rufaa, dai uhamishaji wa data na mantiki ya ulinganishaji iliyofichuliwa kutoka kwa wauzaji, na uweke uwezo mzima ndani ya viwango vya uwezo wa kuingiliana ambavyo sekta ya umma imejitolea tayari.

## Mifano

**Kampuni changa.** Kampuni ya programu inayokua haraka inauza kupitia kujisajili na timu ya mauzo, na njia hizo mbili huunda mteja yuleyule mara mbili kwa majina ya kampuni tofauti kidogo. Mapato kwa kila akaunti yanaonekana si sahihi na timu ya mauzo inaendelea kupigia watumiaji waliopo simu za baridi. Badala ya kununua jukwaa zito, wanaanza na rejista nyepesi: kazi ya kulinganisha kwenye ghala lao la data inayounganisha rekodi kwa kikoa cha barua pepe na jina la kampuni lililosanifiwa, na msimamizi mmoja wa muda mfupi anayepitia ulinganishaji wenye shaka kila wiki. Inagharimu kidogo, inarekebisha kosa la kuripoti, na inathibitisha thamani inayohalalisha uwekezaji zaidi wanapokua.

**Biashara kubwa.** Mtengenezaji wa kimataifa amekua kwa ununuzi na anaendesha ERP na CRM kumi na mbili, kila moja ikiwa na rekodi zake za wasambazaji, kwa hiyo msambazaji yuleyule anaonekana kwa njia kumi na tano na kampuni haiwezi kujadiliana kama mnunuzi mmoja wala kuona matumizi yake ya kweli. Inasimamisha kitovu cha MDM cha mtindo wa kuishi pamoja kwa maeneo ya msambazaji na bidhaa, ikitumia ulinganishaji wa kuamuliwa kwenye vitambulisho vya kodi na usajili pamoja na alama ya uwezekano kwenye majina na anwani. Wasimamizi waliotajwa kwenye ununuzi hurekebisha kanuni za kuokoka na kufanyia kazi foleni ya mapitio, na rekodi za dhahabu zinachapishwa kama matukio ya mabadiliko yanayotiririka kurudi kwenye kila ERP ili data iliyosafishwa iboreshe vyanzo. Mwonekano wa matumizi uliounganishwa unafungua masharti bora ya mkataba, na kodi ya upatanisho iliyotumia fedha kila robo inashuka kwa kiasi kikubwa.

**Serikali.** Serikali ya kitaifa inataka mawakala wamchukulie raia kama mtu mmoja badala ya mgeni kwenye kila kaunta, huku ikiheshimu mipaka mikali ya kisheria ya kushiriki data. Inajenga kitovu cha kati cha data kuu kwa chombo cha mtu, kilichofungwa kwa kitambulisho cha kitaifa kilichotawaliwa, na data ya rejeo yenye matoleo kwa tarehe zinazotumika ili rekodi za kihistoria zibaki sahihi. Utatuzi wa utambulisho ni wa tahadhari kwa makusudi: ulinganishaji wenye shaka unaenda kwa wasimamizi waliofunzwa badala ya miunganisho ya kiotomatiki, kwa sababu muunganisho usio sahihi ungeweza kumnyima mtu manufaa au kufichua data yake, na kila ulinganishaji unaandikwa kwa ukaguzi na rufaa. Faida ni rekodi chache zilizorudiwa, ulaghai mdogo kutoka utambulisho uliogawanyika, na raia asiyelazimika kuthibitisha yeye ni nani kwenye kila mlango, ndani ya viwango vya uwezo wa kuingiliana vya sura ya 3.8.

## Kesi ya biashara: sababu, ROI, na TCO

Faida ya MDM inatokana na kuondoa kodi ambayo mashirika mengi hulipa bila kuitaja. Rekodi zilizorudiwa na zinazopingana zinagharimu fedha kwa njia dhahiri (uuzaji uliopotea kwa mtu yuleyule mara tano, makosa ya usafirishaji kutoka anwani zilizochakaa, punguzo la kiasi lililokosekana) na kwa njia zisizo dhahiri (wachambuzi wakipatanisha hesabu, watendaji wakiamua kwa namba ambazo si sahihi kimyakimya, wakaguzi wakitoza saa kufumua rekodi ipi ni halisi). Mtazamo wa msambazaji uliounganishwa mara nyingi hulipia programu nzima kwa masharti bora ya mkataba pekee.

Jumla ya gharama ya umiliki ina sehemu tatu: jukwaa au ujenzi, muunganisho kwa vyanzo na watumiaji, na, kubwa zaidi baada ya muda, usimamizi endelevu. Gharama ya muunganisho ni rahisi kuidharau, kwa sababu kuunganisha mifumo kadhaa ya zamani chanzo ndipo programu za MDM zinapovuja ratiba na bajeti, na gharama ya usimamizi ni rahisi kuisahau, kwa sababu ni gharama ya kudumu ya uendeshaji, si ujenzi wa mara moja. Kuweka kesi kwa uongozi, funga MDM na namba wanazofuatilia tayari: usahihi wa mapato, ufanisi wa masoko, akiba ya ununuzi, gharama ya ukaguzi, na hatari ya udhibiti, kisha anza finyu na uache ushindi uliopimwa kwenye eneo moja lenye maumivu makubwa ufadhili upanuzi.

## Mifumo mibaya na mitego

- **Wigo wa kuchemsha bahari:** kusimamia kila eneo mara moja, kutoa kitu hakuna kwa miaka, na kupoteza ufadhili kabla ya ushindi wa kwanza.
- **Zana kabla ya utawala:** kununua jukwaa la MDM kabla ya kutaja wasimamizi na wamiliki, kwa hiyo injini haina dereva.
- **Wasimamizi wa muda mfupi bila mamlaka:** kugawa usimamizi kwenye slaidi bila kutoa mamlaka halisi wala muda uliolindwa.
- **Kuokoka kimya:** kuunganisha rekodi kwa chaguo-msingi la zana au mpangilio wa upakiaji, bila kanuni zilizoandikwa wala njia ya kueleza rekodi ya dhahabu.
- **Miunganisho isiyorekebishika:** kuunganisha kiotomatiki ulinganishaji wenye shaka bila kutendua, kwa hiyo muunganisho usio sahihi wa vyombo viwili halisi unakuwa madhara ya kudumu.
- **Data ya rejeo iliyoandikwa juu:** kuhariri orodha za misimbo bila matoleo, kuvunja kila ripoti ya kihistoria iliyokuwa sahihi chini ya misimbo ya zamani.
- **Rekodi za dhahabu ambazo hakuna anayetumia:** kujenga kitovu safi ambacho hakuna mfumo wa chini ya mkondo unajiandikisha kwake, kwa hiyo data safi haifiki kwenye maamuzi.
- **Kubuni upya misimbo ya kawaida:** kuunda orodha zako za nchi au sarafu viwango vya ISO vinapokuwepo, na kupoteza uwezo wa kuingiliana bila sababu.

## Kielelezo cha ukomavu

- **Ngazi ya 1, Kuanzisha:** Data kuu na ya rejeo haisimamiwi. Chombo kilekile kipo mara nyingi bila toleo lenye mamlaka, orodha za misimbo zinatofautiana, ulinganishaji ni wa mkono na wa kuitikia, na hakuna anayemiliki tatizo, kwa hiyo hesabu za vyombo vya msingi zinapingana na hakuna anayeweza kusema ipi ni sahihi.
- **Ngazi ya 2, Kuendeleza:** Maeneo muhimu yanatambuliwa na mtu anaondoa nakala, mara nyingi kwenye ghala kwa kuripoti. Ulinganishaji wa msingi wa kuamuliwa upo, orodha za rejeo zimekusanywa, na watu wachache hufanya kama wasimamizi wasio rasmi, lakini mazoea hutofautiana timu hadi timu, vyanzo vinabaki fujo, na kanuni zinaishi vichwani mwa watu badala ya karatasi.
- **Ngazi ya 3, Kusawazisha:** MDM ni programu iliyotawaliwa inayotumika kwa uthabiti kuvuka shirika. Maeneo kuu yana wamiliki waliotajwa na wasimamizi waliowezeshwa, kanuni za ulinganishaji na kuokoka zimeandikwa na kutekelezwa, rekodi za dhahabu zinazalishwa na kusambazwa kwa watumiaji, na data ya rejeo ina matoleo na inachapishwa na tarehe zinazotumika kama API.
- **Ngazi ya 4, Kusimamia:** Programu inapimwa na kudhibitiwa dhidi ya vipimo vya msingi. Viwango vya nakala, usambazaji wa imani ya ulinganishaji, viwango vya miunganisho ya uongo na ulinganishaji uliokosekana, ukamilifu wa nyanja muhimu, na ukubwa na umri wa foleni ya mapitio vinafuatiliwa kama vipimo; vizingiti vinarekebishwa dhidi ya namba hizo badala ya hisia; na thamani ya MDM (usahihi wa mapato, akiba ya ununuzi, gharama ya mapitio) inapimwa kwa namba na kuripotiwa kwa wamiliki kwa mzunguko uliowekwa.
- **Ngazi ya 5, Kuratibu:** Rekodi za dhahabu zinatiririka kama matukio yenye matoleo karibu na wakati halisi, zinalisha safu ya kisemantiki, na zinaaminiwa kuvuka shirika. Ulinganishaji unaboreshwa mfululizo dhidi ya matokeo yaliyopimwa, usimamizi unapanuka hadi maeneo mapya kama uwezo unaojirudia, na MDM imeunganishwa na utawala na upangaji wa hatari ili programu ijirekebishe vyanzo, viwango, na mandhari ya vyombo vinapohama.

## Mawazo ya kujadili

1. Mifumo yenu miwili ikitofautiana kuhusu mna wateja wangapi, ipi ni sahihi, na mngethibitishaje?
2. Eneo gani la data kuu lingetoa ushindi mkubwa zaidi unaopimika likisimamiwa kwanza, na ushindi huo una thamani gani?
3. Ulinganishaji wa uwezekano ungesaidia wapi leo, na je, mko raha na muunganisho usio sahihi wa mara kwa mara unaomaanisha?
4. Mnaweka vipi matoleo kwenye data yenu ya rejeo, na nini kinavunjika kwenye ripoti zenu za kihistoria msimbo unapobadilisha maana?
5. Nani ni msimamizi aliyetajwa wa chombo chenu muhimu zaidi, na je, ana mamlaka na muda wa kufanya kazi kweli?
6. Rekodi ya dhahabu inapobadilika, mifumo yenu ya chini ya mkondo inajuaje, na inaweza kuchakaa kiasi gani kabla haijaumiza?

## Mambo muhimu ya kukumbuka

- Panga data yako kuwa kuu, ya rejeo, na ya miamala; wekeza ulinganishaji na utawala pale marudio yanapogharimu zaidi.
- Zalisha rekodi moja ya dhahabu kwa kila chombo cha ulimwengu halisi, iliyokusanywa kwa kanuni za kuokoka wazi, zinazorekebishika, zilizoandikwa.
- Chagua mtindo wa usanifu wa MDM (rejista, kuunganisha, kuishi pamoja, au kitovu cha kati) kufaa hamu yako ya udhibiti na usumbufu.
- Chukulia data ya rejeo kama msamiati wa pamoja wenye matoleo, pendelea viwango vinavyotambulika, na usiandike kamwe juu ya orodha za misimbo.
- MDM hufanikiwa kwa utawala na usimamizi, si zana; sambaza rekodi za dhahabu kama matukio na upime programu kwa maamuzi yaliyoboreshwa.

## Marejeo na usomaji zaidi

- David Loshin, *Master Data Management*
- Alex Berson and Larry Dubov, *Master Data Management and Data Governance*
- Dan Power, *The Definitive Guide to Master Data Management*
- John Talburt, *Entity Resolution and Information Quality*
- Peter Christen, *Data Matching: Concepts and Techniques for Record Linkage, Entity Resolution, and Duplicate Detection*
- Ivan P. Fellegi and Alan B. Sunter, "A Theory for Record Linkage," *Journal of the American Statistical Association*
- DAMA International, *DAMA-DMBOK: Data Management Body of Knowledge*
- Ralph Kimball and Margy Ross, *The Data Warehouse Toolkit*
