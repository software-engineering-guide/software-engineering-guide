# 1.6 Rekodi za maamuzi

## Muhtasari na msukumo

**Rekodi ya uamuzi** ni waraka unaonasa uamuzi muhimu pamoja na muktadha wake na matokeo yake. Umbo linalojulikana zaidi ni **[rekodi ya uamuzi wa usanifu](https://en.wikipedia.org/wiki/Architectural_decision) (ADR)**, dokezo fupi, linalopendelewa lisibadilike, linalorekodi uchaguzi mmoja wenye umuhimu wa usanifu, kwa nini lilifanywa, na kinachofuata kutokana nalo. Seti kamili ya rekodi za mradi ni **kumbukumbu yake ya maamuzi (ADL)**, na nidhamu ya kuzitunza ni sehemu ya **usimamizi wa maarifa ya usanifu (AKM)**. Sura hii inajengwa juu ya mazoea ya kufanya maamuzi na utawala ya sura ya 1.5, ikilenga jinsi unavyoandika, kuhifadhi, na kudumisha rekodi za maamuzi kwa ukubwa.

Msukumo ni rahisi, na wenye maumivu kujifunza kwa njia ngumu. Katika mfumo wowote wa muda mrefu, swali ghali zaidi ni "kwa nini kwa dunia ulijengwa hivi?", linaloulizwa miezi au miaka baadaye na watu ambao hawakuwa chumbani. Msimbo unaonyesha *nini* mfumo unafanya. Majaribio yanaonyesha kwamba *unafanya kazi*. Lakini hakuna kati ya hivyo kinachonasa *kwa nini* ulichagua njia hii badala ya mbadala ulizozingatia na kukataa. Bila rekodi za maamuzi, hoja hiyo hupotea na mauzo ya wafanyakazi. Timu hubishana upya maswali yaliyotatuliwa, hutengua maamuzi mazuri kwa sababu mbaya, au hudumisha maamuzi mabaya kwa hofu. Rekodi ya uamuzi ni barua nafuu kwa wakati ujao inayohifadhi hoja.

Kwa timu kubwa, hii ni zana ya uratibu kama ilivyo msaada wa kumbukumbu. Mashirika makubwa huendesha makumi ya timu zinazofanya chaguo zinazoingiliana. Kumbukumbu ya maamuzi ya pamoja hugeuza hoja iliyopatikana kwa shida ya timu moja kuwa mali inayoweza kutumika tena, na huzuia maamuzi yanayotofautiana, yasiyooana. Katika mazingira ya serikali na yanayodhibitiwa, rekodi za maamuzi zinakaribia kuwa za lazima. Wakaguzi, vyombo vya usimamizi, na wakandarasi warithi wote wanahitaji sababu inayoweza kufuatiliwa inayounganisha mahitaji yenye umuhimu wa usanifu na chaguo zilizofanywa dhidi yake. Kumbukumbu ya maamuzi iliyotunzwa vizuri mara nyingi ndiyo tofauti kati ya mfumo unaoweza kuuhakikisha na kuukagua na ule usioweza.

## Kanuni kuu

- **Rekodi *kwa nini*, si *nini* tu.** Muktadha na mbadala zilizokataliwa ndizo hoja.
- **Uamuzi mmoja kwa kila rekodi.** Weka kila rekodi mahususi na inayojitegemea.
- **Ndogo na nyepesi inashinda kamili isiyotumika.** Rekodi ya ukurasa mmoja iliyopo inashinda ripoti isiyoandikwa kamwe.
- **Weka tarehe kwa kila kitu.** Gharama, vikwazo, na wasambazaji hubadilika; tia tarehe kila dai.
- **Pendelea kumbukumbu hai, kwa vitendo.** Kutobadilika ndiyo hali bora; kwa vitendo, rekebisha kwa maelezo yenye tarehe.
- **Maneno kuliko vifupisho.** "Maamuzi" huvutia michango zaidi kuliko "ADR."
- **Fanya maamuzi yapatikane na, inapowezekana, yajaribike.** Ibua rekodi sahihi wakati sahihi; ihakikishe kwa kazi za utimamu.

## Mapendekezo

### Nasa muundo muhimu

Rekodi nzuri ya uamuzi ina sehemu chache muhimu. Rekebisha kiolezo kinachojulikana badala ya kuvumbua kipya:

- **Kichwa:** kifungu kifupi cha amri cha wakati uliopo ("Tumia [PostgreSQL](https://en.wikipedia.org/wiki/PostgreSQL) kwa leja").
- **Hali:** imependekezwa, imekubaliwa, imebatilishwa, imeachwa.
- **Muktadha:** hali, nguvu, vipaumbele vya biashara, na vikwazo vinavyofanya uamuzi huu uwe wa lazima; jumuisha hitaji lenye umuhimu wa usanifu linalolishughulikia.
- **Uamuzi:** uchaguzi uliofanywa, ulioelezwa wazi.
- **Matokeo:** nini kinakuwa rahisi na nini kinakuwa kigumu, maamuzi ya kufuata yaliyochochewa, na hatari zilizokubaliwa.

Violezo maarufu ni pamoja na cha Michael Nygard (rahisi na kinachopokelewa kwa upana), cha Tyree na Akerman (cha kina zaidi, chenye mbadala zilizopimwa), MADR (Markdown Any Decision Records, imara kwenye chaguo na faida/hasara zake), na Y-statements (umbo lenye muundo la sentensi moja). Sawazisha kwenye kimoja kwa kila shirika, ili rekodi ziweze kulinganishwa. Tazama sura ya 12.3 kwa kiolezo cha kunakili na kubandika.

### Andika rekodi mahususi, zenye tarehe, na zisizobadilika kwa kiasi

Weka kila rekodi kuhusu uamuzi mmoja hasa. Tia tarehe madai binafsi, hasa chochote kinachoteleza: bei, nambari za ukubwa, uwezo wa wasambazaji, masharti ya leseni. Kwa nadharia, rekodi inapaswa kutobadilika. Uamuzi unapobadilika, unaandika rekodi *mpya* inayobatilisha ya zamani, ukihifadhi historia. Kwa vitendo, timu nyingi hupata kwamba mbinu ya **waraka hai** inafanya kazi vizuri zaidi: ingiza taarifa mpya katika rekodi iliyopo na muhuri wa tarehe na dokezo kwamba ilifika baada ya uamuzi. Zote mbili ni halali. Mtindo usiobadilika una nguvu zaidi kwa njia za ukaguzi; mtindo hai ni bora kwa maarifa ya kila siku ya timu. Chagua kwa makusudi, na uwe thabiti.

### Hifadhi rekodi mahali kazi ilipo

Weka rekodi za maamuzi katika [udhibiti wa matoleo](https://en.wikipedia.org/wiki/Version_control) kando ya msimbo: saraka ya `decisions/` (au `adr/`) ya mafaili ya [Markdown](https://en.wikipedia.org/wiki/Markdown), moja kwa kila uamuzi, yaliyotajwa kwa kifungu cha kitenzi cha amri cha herufi ndogo kilichotenganishwa kwa vistari (`choose-database.md`, `format-timestamps.md`). Hii inakupa historia, mapitio, na ulinganisho bila gharama, na inaweka sababu karibu na kile inachoeleza. Timu yako ikipendelea [wiki](https://en.wikipedia.org/wiki/Wiki), Google Docs, au kifuatiliaji cha mtindo wa Jira, tumia hivyo badala yake. Zana ni muhimu kidogo sana kuliko tabia. Zana nyepesi ya mstari wa amri (kama `adr-tools`) inaweza kuanzisha na kuorodhesha rekodi.

### Ziite "maamuzi," na upanue zaidi ya usanifu

Ufahamu wa vitendo kutoka timu nyingi: lebo ni muhimu. Baadhi ya wasanidi na mameneja hukereka na neno "usanifu," na "rekodi" inaweza kuhisiwa kama karatasi za baada ya tukio. Kubadilisha jina la saraka kuwa "decisions" tu mara nyingi hubadilisha kila kitu. Timu huanza kurekodi chaguo za wasambazaji, maamuzi ya kupanga, maamuzi ya ratiba, na maamuzi ya data na uzingatiaji, yote kwa kiolezo kilekile. Watu hujifunza haraka kutoka maneno kuliko vifupisho, na huchangia zaidi fremu inapokuwa "saidia wenzako wa baadaye kufikiri" badala ya "jaza fomu ya lazima."

### Fafanua mzunguko wa maisha na utawala

Ili rekodi za maamuzi zipanuke, kubaliana mchakato unaozizunguka (hapa ndipo utawala wa sura ya 1.5 unapokutana na mazoezi):

- **Nani anaweza kuiibua, na nini kinahalalisha:** kwa kawaida mchangiaji yeyote mwenye taarifa; ibua rekodi wakati wasanidi wa baadaye watahitaji *kwa nini*, na uruke kwa chaguo za hatari ndogo, zinazojitegemea, au zilizoandikwa tayari.
- **Mzunguko wa maisha:** mtiririko rahisi kama *Kuanzisha → Kutafiti → Kutathmini → Kutekeleza → Kudumisha → Kustaafisha*, na vigezo vya kukubalika vya kusonga kati ya hatua (tatizo limeelezwa, mbadala zimezingatiwa, mabadilishano yameandikwa, wadau wameshauriwa).
- **Majukumu:** mpendekezaji, mtafiti, mhakiki, mwidhinishaji, na mdumishaji anayewajibika anayepitia rekodi mara kwa mara (angalau kila mwaka) na kuendesha kustaafishwa hatimaye.
- **Utawala:** jinsi makubaliano, mgogoro, upandishaji, na kura ya turufu zinavyofanya kazi, na vikwazo vyovyote vya uzingatiaji. Tegemea kanuni kama *mwelekeo wa kutenda* na *[kutokubaliana-na-kujitolea](https://en.wikipedia.org/wiki/Disagree_and_commit)*, na uhifadhi mchakato mzito kwa maamuzi yasiyoweza kutenduliwa, yenye mlipuko mkubwa ("mlango wa upande mmoja").

### Fanya maamuzi yajaribike na yapatikane

Rekodi ya uamuzi *huandika* uamuzi; **kazi ya utimamu** *huhakikisha*: ukaguzi wa kiotomatiki, unaoendeshwa katika [uunganishaji endelevu](https://en.wikipedia.org/wiki/Continuous_integration) (CI), unaothibitisha uamuzi bado unashikilia ("mabadiliko yote ya hali lazima yatoe matukio," "hakuna moduli inayoweza kuagiza kuvuka mipaka hii," kwa kutumia zana kama ArchUnit). Hii inageuza utawala kutoka mapitio ya mara kwa mara ya mkono hadi utekelezaji endelevu unaopanuka, wenye thamani hasa kwa malengo ya udhibiti na ukaguzi (sura za 3.1, 4.6, 8.5). Kisha ibua rekodi *sahihi* wakati *sahihi*. Zana inayoambatisha maamuzi husika kwenye ombi la kuvuta msanidi anapogusa msimbo unaoutawala ni bora kuliko kutumaini watu wasome saraka ya nyaraka.

## Mabadilishano: faida na hasara

| Chaguo | Faida | Hasara |
|---|---|---|
| **ADR nyepesi (Nygard/MADR)** | Haraka kuandika, huandikwa kweli; taratibu ndogo | Ukali mdogo kwa maamuzi ya dau la juu, yanayobishaniwa |
| **Violezo vizito (Tyree-Akerman)** | Mbadala zilizopimwa; imara kwa chaguo kubwa, ghali | Polepole; vinaweza kukatisha kurekodi kwa kawaida |
| **Isiyobadilika + kubatilisha** | Njia safi ya ukaguzi; historia imehifadhiwa | Rekodi zaidi; wasomaji lazima wafuate minyororo |
| **Waraka hai (marekebisho yenye tarehe)** | Chanzo kimoja cha sasa cha ukweli; rahisi kudumisha | Hadithi dhaifu ya ukaguzi; hatari ya marekebisho ya kimya |
| **Markdown ndani ya hazina** | Ina matoleo, inapitiwa, kando ya msimbo | Si rafiki sana kwa wasio wasanidi |
| **Wiki / zana ya nyaraka** | Inafikika kwa majukumu yote | Historia na mapitio dhaifu; inateleza kutoka msimbo |

Mvutano wa msingi ni **ukali dhidi ya kupokelewa**. Mfumo mkali zaidi ambao hakuna anayeutumia hurekodi kitu. Mfumo mwepesi zaidi ambao kila mtu anautumia hujumlika kwa thamani. Chagua mwepesi kama chaguo-msingi, na uhifadhi mchakato mzito kwa maamuzi machache ghali na magumu kutenduliwa.

## Maswali ya kujadili na timu yako

1. **Rekodi sahihi ya uamuzi itamfikiaje msanidi wakati anagusa msimbo unaoutawala, badala ya kukaa kwenye saraka ambayo hakuna anayeifungua?** Kumbukumbu ya kuandikwa-tu hurekodi hoja ambayo kamwe haibadilishi tabia, ambayo ndiyo njia ya kawaida zaidi rekodi za maamuzi zinavyoshindwa: zipo, na hakuna anayezisoma inapojalisha. Jambo linaloshindana ni juhudi, kwa sababu kuibua rekodi kiotomatiki (kuziambatisha kwenye ombi la kuvuta mtu anapohariri msimbo unaotawaliwa) kunahitaji uwekezaji wa zana ambao wiki au saraka ya nyaraka haihitaji. Leta ushahidi katika mjadala: mtu alipotengua au kubishana upya swali lililotatuliwa hivi karibuni, je, rekodi husika ilipatikana wakati huo, au ilizikwa? Kwa shirika kubwa linaloendesha makumi ya timu, uwezo wa kupatikana ndio unaogeuza hoja iliyopatikana kwa shida ya timu moja kuwa mali inayoweza kutumika tena badala ya kumbukumbu ya faragha. Amua kama kuhifadhi rekodi katika udhibiti wa matoleo kando ya msimbo na kuziunganisha kwenye mtiririko wa ombi la kuvuta, ili rekodi ionekane kazi inapofanyika.

2. **Nani ni mdumishaji anayewajibika wa kila rekodi, na nini kinazuia kumbukumbu yenu kuoza kuwa taarifa potofu za kujiamini?** Njia hatari ya kushindwa ya kumbukumbu ya maamuzi si saraka tupu, ni saraka iliyojaa rekodi ambazo gharama, uwezo wa wasambazaji, na vikwazo vyake vilichakaa kimyakimya miaka iliyopita. Kila rekodi inahitaji mmiliki anayewajibika anayeipitia kwa ratiba (angalau kila mwaka) na kuendesha kubatilisha au kustaafisha, la sivyo kumbukumbu huoza kuwa hadithi za watu ambazo watu huzitaja kwa kuchagua na kuziamini kidogo. Leta ushahidi: rekodi ngapi zako hazina tarehe, ngapi zinaeleza msambazaji au bei iliyobadilika tangu hapo, na kila moja ilipitiwa lini mwisho. Katika mazingira ya serikali na yanayodhibitiwa hili ni kali zaidi, kwa sababu mnyororo usiobadilika, uliobatilishwa ndio hasa wakaguzi na wakandarasi warithi wanautegemea kwa sababu inayoweza kufuatiliwa. Amua mzunguko wenu wa maisha waziwazi, tia tarehe madai binafsi yanayoteleza, na kabidhi wadumishaji, ili kumbukumbu ibaki mali hai badala ya makaburi.

3. **Je, mnapaswa kusawazisha kwenye kiolezo kimoja kuvuka timu zote, na ukali kiasi gani maamuzi yenu ya dau la juu zaidi yanahitaji kweli?** Uwezo wa kulinganisha ni faida halisi: kila timu inapotumia umbo lilelile (Nygard, MADR, au sawa), timu mpya inaweza kupata rekodi tatu za awali na kupokea hoja alasiri moja badala ya mwezi wa mjadala. Mvutano wa msingi ni ukali dhidi ya kupokelewa, kwa sababu kiolezo kizito zaidi ambacho hakuna anayekitumia hakirekodi kitu, ilhali chepesi zaidi ambacho kila mtu anakitumia hujumlika kwa thamani. Leta ushahidi: je, rekodi zinaandikwa kweli, na tofauti, je, maamuzi makubwa, yanayobishaniwa, ghali yoyote yamechambuliwa kidogo kwa sababu umbo jepesi liliruka kupima mbadala? Kwa mashirika makubwa yanayoratibu chaguo zinazoingiliana kuvuka timu, kiolezo cha pamoja pamoja na faharisi inayotafutika huzuia maamuzi yanayotofautiana, yasiyooana. Chagua mwepesi kama chaguo-msingi kwa kesi ya kawaida, na kubaliana mapema ni maamuzi gani ya mlango wa upande mmoja yanastahili umbo zito lenye mbadala zilizopimwa.

4. **Nini hasa kinahalalisha kuibua rekodi ya uamuzi, na nani ana mamlaka ya kusema chaguo halihitaji?** Weka kizingiti juu mno na hoja nyuma ya chaguo zenye matokeo hupotea; kiweke chini mno na kumbukumbu hujaa mambo madogo yanayozika rekodi ambazo watu wanahitaji kweli. Kwa shirika kubwa, kizingiti kisicho wazi kinamaanisha kila timu hubuni chake, kwa hiyo ufikiaji unakuwa usio sawa na hakuna anayeweza kuamini kwamba rekodi iliyokosekana inaashiria uamuzi usio muhimu. Leta ushahidi katika mjadala: maamuzi machache ya hivi karibuni yaliyorekodiwa lakini hayakuhitaji, na yenye maumivu ambayo hayakurekodiwa na baadaye yalikugharimu kugundua upya. Kubaliana mtihani rahisi, kama kurekodi wakati wowote msanidi wa baadaye atahitaji *kwa nini* na kuruka chaguo za hatari ndogo, zinazojitegemea, au zilizoandikwa tayari. Katika mazingira ya serikali na yanayodhibitiwa hesabu hubadilika, kwa sababu agizo la ukaguzi linaweza kuhitaji rekodi kwa kila hitaji lenye umuhimu wa usanifu iwe timu inahukumu linastahili kuandikwa au la, kwa hiyo taja maamuzi ambayo hayajadiliwi mapema.

5. **Je, rekodi zenu ni hoja halisi iliyonaswa wakati wa uamuzi, au karatasi zilizoandikwa baadaye kutimiza agizo?** Rekodi iliyotolewa baada ya tukio kufunga tiketi huelekea kusafisha chaguo lililochaguliwa na kuacha kimyakimya mbadala zilizopimwa kweli, ambayo ndiyo hasa taarifa msomaji wa baadaye anayoihitaji zaidi. Shinikizo linaloshindana ni halisi: kuandika *kwa nini* kabla au wakati wa uamuzi kunahisi polepole kuliko kutoa, na kukiri njia zilizokataliwa kwa maandishi kunahitaji usalama wa kisaikolojia ambao baadhi ya timu hawana. Leta sampuli ya rekodi za hivi karibuni mezani na uulize kwa uaminifu kama muktadha na mbadala zilizokataliwa zinasomeka kama mazingatio halisi au kama uhalalishaji uliobuniwa baadaye. Kwa timu kubwa, rekodi tupu ni mbaya kuliko kutokuwepo, kwa sababu zinawafunza watu kwamba kumbukumbu haiwezi kuaminiwa. Katika ukaguzi wa mashirika makubwa na ya serikali tofauti hii ni kali: vyombo vya usimamizi na wakandarasi warithi hutegemea sababu inayoakisi kilichozingatiwa kweli, na rekodi inayosomeka kama maigizo inadhoofisha uhakikisho ambao kumbukumbu ipo kutoa.

6. **Ni maamuzi yenu gani ya dau la juu zaidi unaweza kuyahakikisha kwa kazi ya utimamu ya kiotomatiki, badala ya kuamini kwamba mapitio ya mara kwa mara ya mkono yatakamata ukiukaji?** Rekodi ya uamuzi huandika chaguo, lakini ni ukaguzi wa kiotomatiki unaoendeshwa katika uunganishaji endelevu tu unaozuia chaguo hilo kumomonyoka kimyakimya wasanidi makumi wanapogusa msimbo kwa miaka. Mabadilishano ni uwekezaji, kwa sababu kuandika na kudumisha kazi za utimamu (kwa zana kama ArchUnit) kunagharimu muda wa kihandisi, na maamuzi mengi, hasa chaguo za mchakato au msambazaji, hayawezi kujaribiwa kwa mitambo kabisa. Leta ushahidi: ni maamuzi gani ya mipaka (utegemezi wa moduli, utoaji wa matukio, kanuni za ufikiaji wa data) yamekiukwa kimyakimya na kunaswa kuchelewa tu katika mapitio au uzalishaji. Kwa shirika kubwa linaloendesha timu nyingi, kazi za utimamu hugeuza utawala kutoka kikwazo cha kati hadi utekelezaji endelevu unaopanuka bila kupunguza kasi ya wote. Katika mazingira ya serikali na yanayodhibitiwa, ukaguzi wa kiotomatiki, unaowashwa daima ni ushahidi wa ukaguzi wenye nguvu zaidi sana kuliko saini kwenye mapitio, kwa sababu unathibitisha uamuzi bado unashikilia leo badala ya kwamba mtu mara moja aliuidhinisha.

## Mtazamo wa sekta

**Kampuni changa.** Zingatia tabia na si kingine: saraka ya `decisions/` katika hazina yako kuu, na dokezo la sehemu mbili (muktadha na uchaguzi) wakati wowote unapofanya uamuzi ambao wewe wa baadaye atauhoji. Ruka mzunguko wa maisha, majukumu, na waidhinishaji kabisa, kwa sababu mchakato usioweza kuudumisha ni mchakato utakaouacha. Rekodi moja inayomwokoa mwajiriwa wako wa kwanza asiulize kwa nini mfumo umejengwa hivi tayari inalipia mazoea yote.

**Biashara ndogo.** Bila mbunifu maalumu na muda mdogo, weka rekodi mahali timu yako inapofanya kazi tayari, iwe wiki, waraka wa pamoja, au hazina, badala ya kununua zana maalumu. Tabia ni muhimu zaidi sana kuliko zana, kwa hiyo punguza kizuizi: taja saraka `decisions` badala ya `adr`, na unase chaguo za wasambazaji na kununua-dhidi-ya-kujenga kwa pumzi ileile kama za kiufundi. Unapotegemea wakandarasi wa nje, rekodi fupi yenye tarehe ya kwa nini ulichagua msambazaji au jukwaa ni bima nafuu dhidi ya kufungwa kwenye uchaguzi ambao hakuna anayeweza kuueleza baadaye.

**Biashara kubwa.** Kazi ni uratibu kuvuka timu nyingi: sawazisha kwenye kiolezo kimoja, chapisha faharisi ya kuvuka timu inayotafutika, na uunge mkono maamuzi muhimu ya mipaka kwa kazi za utimamu ili ukiukaji ushindwe wa ujenzi badala ya kusubiri mapitio. Kabidhi mdumishaji anayewajibika kwa kila rekodi mwenye ratiba ya mapitio, ili kumbukumbu ibaki mali hai badala ya kuoza kuwa hadithi za watu. Ikifanywa vizuri, hoja ya timu moja kuhusu uchaguzi mgumu inakuwa mali ambayo timu inayofuata inaipokea alasiri moja badala ya kuibishana upya.

**Serikali.** Kanuni za ununuzi, uwazi, na uwajibikaji wa umma hufanya rekodi za maamuzi kukaribia kuwa za lazima. Hitaji rekodi isiyobadilika, iliyobatilishwa kwa kila hitaji lenye umuhimu wa usanifu, kila moja ikiunganisha uchaguzi na agizo au udhibiti wa uzingatiaji unaotimiza, ili vyombo vya usimamizi vipate sababu inayoweza kufuatiliwa badala ya ujenzi upya. Kwa sababu mifumo ya umma inavuka maisha ya miaka mingi, wasambazaji wengi, kumbukumbu iliyotunzwa vizuri mara nyingi ndiyo inayomruhusu mkandarasi mrithi kuelewa kwa nini mfumo una umbo ulilo nalo na kuendelea na kazi bila kuibishana upya msingi uliotatuliwa.

## Mifano

**Kampuni changa.** Kampuni changa ya watu watano inaongeza saraka rahisi ya `decisions/` kwenye hazina yake kuu, ikiwa na dokezo la sehemu mbili (muktadha na uchaguzi) wakati wowote mtu anapofanya uamuzi ambao wao wa baadaye wataouhoji. Hakuna mzunguko wa maisha, hakuna majukumu, hakuna waidhinishaji: ni tabia ya kuandika *kwa nini* kando ya msimbo tu. Mwajiriwa wao wa kwanza anapojiunga miezi sita baadaye, anasoma saraka nzima kwa saa moja na kuacha kuuliza "kwa nini imejengwa hivi?" Kumbukumbu nyepesi inagharimu dakika kwa kila ingizo na inawaokoa ushuru wa kugundua upya unaouma muda mrefu kabla timu haijakua kubwa.

**Biashara kubwa.** Muuzaji wa rejareja mwenye timu 30 za uhandisi anasawazisha kwenye rekodi za muundo wa MADR katika kila hazina, pamoja na faharisi ya kati inayotafutika. Timu mpya inapokabiliwa na "[monorepo](https://en.wikipedia.org/wiki/Monorepo) dhidi ya multirepo," inapata rekodi tatu za awali zenye muktadha na matokeo, na kupokea hoja alasiri moja badala ya mwezi wa mjadala. Maamuzi muhimu ya mipaka (umiliki wa huduma, kanuni za ufikiaji wa data) yanaungwa mkono na kazi za utimamu za ArchUnit, kwa hiyo ukiukaji unashindwa wa ujenzi badala ya kunaswa kwenye mapitio. Huo ni utawala unaopanuka bila kikwazo cha kati.

**Serikali.** Wakala unaoboresha mfumo wa manufaa unahitaji ADR kwa kila hitaji lenye umuhimu wa usanifu, kila moja ikiunganisha uamuzi na agizo au udhibiti wa uzingatiaji unaotimiza (ufikivu, makazi ya data, uwezo wa kukaguliwa). Rekodi hazibadiliki na zinabatilishwa, zikizalisha kumbukumbu inayoweza kufuatiliwa inayotimiza mapitio ya usimamizi. Muhimu, pia inamruhusu mkandarasi mrithi kuelewa *kwa nini* mfumo una umbo ulilo nalo, ikihifadhi mwendelezo kuvuka maisha ya miaka mingi, wasambazaji wengi ya kawaida ya programu za umma (sura za 4.6, 10.4).

## Kesi ya biashara: sababu, ROI, na TCO

Rekodi ya uamuzi inagharimu dakika kuandika na chache zaidi kupitia. Mapato ni gharama iliyoepukwa ya *kuamua upya* na gharama iliyoepukwa ya *kutengua kimakosa*, zote kubwa na zinazojirudia kwenye mifumo ya muda mrefu. Kila wakati timu inapobishana upya swali lililotatuliwa, au kutengua uchaguzi mzuri kwa sababu hakuna aliyekumbuka kikwazo nyuma yake, hulipa kwa muda wa mhandisi mwandamizi na mara nyingi kwa tukio. Kumbukumbu ya maamuzi hubadilisha ushuru huo unaojirudia kuwa uandishi wa mara moja.

Kwa **jumla ya gharama ya umiliki**, rekodi za maamuzi ni miongoni mwa nyaraka zenye kiegemeo cha juu zaidi unazoweza kuzitunza, kwa sababu zinalenga mali moja nyeti zaidi kwa mauzo ya wafanyakazi: sababu. Utambulisho ni wa haraka zaidi (waajiriwa wapya husoma *kwa nini*, si msimbo tu). Uboreshaji ni salama zaidi (sura ya 3.6: unaweza kutofautisha maamuzi muhimu na yasiyo muhimu). Ukaguzi ni nafuu zaidi (ushahidi tayari upo). Gharama ya *kutozitunza* haionekani kwenye dashibodi yoyote, na hujumlika kimyakimya kwa kila kuondoka. Kujenga hoja kwa uongozi, elekeza kwenye kugundua upya kwa gharama ya hivi karibuni, au uamuzi uliotenguliwa uliosababisha tukio, na uonyeshe kwamba suluhisho linagharimu karibu hakuna kuanzisha.

## Mifumo mibaya na mitego

- **Kurekodi *nini* bila *kwa nini*:** kuacha muktadha na mbadala zilizokataliwa, ambazo ndizo hoja nzima.
- **Karatasi za baada ya tukio:** rekodi zilizoandikwa kutimiza agizo, si kufikiri; zinasomeka tupu na hakuna anayeziamini.
- **Nyaraka kubwa za maamuzi mengi:** ukurasa mmoja mkubwa ambao hakuna anayeweza kuabiri wala kubatilisha kwa usafi.
- **Madai bila tarehe:** gharama na vikwazo vilivyokuwa kweli mara moja, vikiwasilishwa kama visivyo na wakati.
- **Marekebisho ya kimya:** kubadilisha historia ya uamuzi bila dokezo lenye tarehe, kuharibu njia ya ukaguzi.
- **Kumbukumbu za kuandikwa tu:** rekodi zinazoundwa na kamwe hazionyeshwi wakati zinapohusika, kwa hiyo hazishawishi tabia.
- **Kulinda lango la vifupisho:** kusisitiza "ADR" na "usanifu" na kwa hiyo kukatisha michango.
- **Hakuna mzunguko wa maisha:** rekodi zisizopitiwa, kubatilishwa, wala kustaafishwa kamwe, zikioza kuwa taarifa potofu.

## Kielelezo cha ukomavu

- **Ngazi ya 1 (Kuanzisha):** Maamuzi yanaishi vichwani mwa watu, nyuzi za gumzo, na ujumbe wa commit; kunasa ni tendaji na wa papo hapo, na sababu hupotea mara kwa mara na mauzo ya wafanyakazi.
- **Ngazi ya 2 (Kuendeleza):** Baadhi ya timu hutunza rekodi, katika miundo na violezo mbalimbali, wakati wowote mtu mmoja anapokumbuka; mazoea hayana uthabiti kuvuka timu, bila kumbukumbu ya pamoja, majina, wala mchakato.
- **Ngazi ya 3 (Kusawazisha):** Kiolezo kimoja, uhifadhi ndani ya hazina, na mzunguko wa maisha na utawala ulioainishwa (vigezo vya kuibua/kuruka, majukumu, ratiba ya mapitio) vimeandikwa na kutumika kwa uthabiti shirika zima; rekodi hupitiwa na kubatilishwa badala ya kuhaririwa kimya.
- **Ngazi ya 4 (Kusimamia):** Kumbukumbu ya maamuzi inapimwa dhidi ya vipimo vya msingi: ufikiaji (sehemu ya maamuzi yenye umuhimu wa usanifu yenye rekodi), ujana (sehemu ya rekodi zilizopitiwa ndani ya ratiba yake, pamoja na idadi ya madai yasiyo na tarehe au yaliyochakaa), na uwezo wa kupatikana (mara ngapi rekodi husika ilimfikia msanidi aliyebadilisha msimbo unaotawaliwa). Wadumishaji wanaowajibika hutenda juu ya vipimo hivi, wakibatilisha rekodi zilizochakaa na kufunga mapengo ya ufikiaji kwa ushahidi badala ya hadithi.
- **Ngazi ya 5 (Kuratibu):** Kumbukumbu ya maamuzi ya kuvuka timu inayotafutika imeunganishwa katika kazi ya kila siku: rekodi husika huibuka kiotomatiki kwenye mabadiliko zinazoyatawala, maamuzi muhimu huhakikishwa na kazi za utimamu katika uunganishaji endelevu, na kumbukumbu inalisha utambulisho, uboreshaji, na ukaguzi kama mali hai. Shirika huboresha mazoea yenyewe kila wakati, likistaafisha, kubatilisha, na kupanga upya wigo wa rekodi mfumo na vikwazo vyake vinapohama, na kusawazisha upya mahali linapowekeza ukali jalada la maamuzi linapokua.

## Mawazo ya kujadili

1. Ni uamuzi gani wa mwisho timu yenu ilitengua au kubishana upya kwa sababu hakuna aliyekumbuka hoja ya awali?
2. Je, kubadilisha jina la saraka yenu ya `adr/` kuwa `decisions/` kungebadilisha nani anachangia na nini kinarekodiwa?
3. Ni maamuzi gani yenu muhimu yangeweza kuhakikishwa na kazi ya utimamu ya kiotomatiki leo?
4. Isiyobadilika-na-kubatilisha au waraka hai: ipi inafaa wajibu wenu wa ukaguzi na utamaduni wenu, na kwa nini?
5. Mwajiriwa mpya (au mkandarasi mrithi) angegunduaje sasa *kwa nini* mfumo wenu una umbo ulilo nalo?
6. Nini kinahalalisha kuibua rekodi ya uamuzi katika timu yenu, na nini kinahalalisha *kutoibua*?

## Mambo muhimu ya kukumbuka

- Rekodi ya uamuzi inanasa uamuzi mmoja muhimu pamoja na **muktadha na matokeo yake**: *kwa nini*, si *nini* tu.
- Weka rekodi **mahususi, zenye tarehe, na nyepesi**; sawazisha kwenye kiolezo kimoja (Nygard, MADR, au sawa).
- Zihifadhi **katika udhibiti wa matoleo kando ya msimbo**; fikiria kuziita "maamuzi" kupanua michango.
- Fafanua **mzunguko wa maisha na utawala** (vigezo vya kuibua/kuruka, majukumu, ratiba ya mapitio); hifadhi mchakato mzito kwa maamuzi ya mlango wa upande mmoja.
- Fanya maamuzi **yapatikane** wakati wa badiliko na, inapowezekana, **yajaribike** kupitia kazi za utimamu.
- ROI ni gharama iliyoepukwa ya kugundua upya na kutengua kimakosa; hoja ya TCO ina nguvu zaidi pale mauzo ya wafanyakazi, uboreshaji, na ukaguzi vinapojalisha zaidi. Tazama sura ya 1.5 (kufanya maamuzi na utawala) na sura ya 3.1 (misingi ya usanifu).

## Marejeo na usomaji zaidi

- Michael Nygard, "Documenting Architecture Decisions" (2011): the foundational lightweight ADR.
- MADR: Markdown Any Decision Records project (adr.github.io/madr).
- Jeff Tyree and Art Akerman, "Architecture Decisions: Demystifying Architecture" (*IEEE Software*, 2005).
- Olaf Zimmermann, "Y-Statements" and "Architectural Decision Making" (ozimmer.ch).
- Joel Parker Henderson, *Architecture Decision Record (ADR)*: templates, examples, and teamwork guidance (github.com/joelparkerhenderson/architecture-decision-record).
- ThoughtWorks Technology Radar: "Lightweight Architecture Decision Records."
- Neal Ford, Rebecca Parsons, Patrick Kua, Pramod Sadalage, *Building Evolutionary Architectures* (fitness functions).
- AWS Prescriptive Guidance, "ADR process"; Red Hat, "Why you should use ADRs."
- Wikipedia, "Architectural decision" and "Architecturally significant requirements."
