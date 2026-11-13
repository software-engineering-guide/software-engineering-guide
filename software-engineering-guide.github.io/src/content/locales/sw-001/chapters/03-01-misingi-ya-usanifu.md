# 3.1 Misingi ya usanifu

## Muhtasari na msukumo

[Usanifu wa programu](https://en.wikipedia.org/wiki/Software_architecture) ni seti ya maamuzi muhimu ya usanifu ambayo ni ghali kubadilisha: muundo wa vipengele vikuu, mahusiano kati yake, na sifa ambazo mfumo mzima lazima uonyeshe. Fikiria kama kielelezo cha kiakili cha pamoja kinachowaruhusu watu wengi kujenga bidhaa moja thabiti. Katika timu ndogo, usanifu unaweza kuishi vichwani mwa watu wachache na kubadilika unapoendelea. Katika shirika kubwa (mamia ya wahandisi, timu kadhaa, bidhaa nyingi, miaka ya ramani ya barabara), usanifu unakuwa kitu kinachoweka kila mtu akiwa ameratibiwa. Ukiwa wazi, timu husonga mbele kwa kujitegemea bila kugongana. Ukiwa na ukungu, kila utegemezi wa kuvuka timu hugeuka mazungumzo ya kujadiliana, na kila tukio hugeuka mradi wa kiakiolojia.

Kwa mashirika makubwa na serikali, misingi ni muhimu zaidi, kwa sababu mifumo ni ya muda mrefu, inadhibitiwa sana, na inashirikiwa kuvuka idara. Mfumo wa kodi, jukwaa la manufaa, rekodi ya kitaifa ya afya, au leja kuu ya benki itadumu kuliko kazi za watu walioijenga. Maamuzi unayofanya leo kuhusu uunganishaji, umiliki wa data, na [sifa za ubora](https://en.wikipedia.org/wiki/List_of_system_quality_attributes) yatadhibiti kinachowezekana kwa muongo au zaidi. Wadhibiti na wakaguzi wanazidi kutarajia usanifu ulioandikwa, unaoweza kutetewa: ushahidi kwamba kutegemewa, usalama, faragha, na ufikivu vilibuniwa ndani, si kuongezwa baadaye. Kuweka misingi sawa si suala la kitaaluma. Ni tofauti kati ya jukwaa linalojirekebisha kwa maagizo mapya na lile linalopaswa kujengwa upya kutoka mwanzo.

Sura hii inashughulikia misingi ya kudumu inayodumu kuliko mitindo ya teknolojia: sifa za ubora ("-ilities"), mahitaji muhimu ya kiusanifu, kazi za ufaafu na usanifu wa kubadilika, nyaraka nyepesi kwa [C4](https://en.wikipedia.org/wiki/C4_model) na arc42, na uchambuzi wenye muundo wa mabadilishano. Hizi ndizo zana zinazoruhusu timu kubwa kufikiri kuhusu usanifu kwa makusudi badala ya kwa bahati.

## Kanuni kuu

- **Usanifu ni kuhusu mabadilishano, si majibu sahihi.** Kila uamuzi muhimu hubadilisha ubora mmoja kwa mwingine; kazi ni kufanya mabadilishano hayo kwa makusudi na kwa uwazi.
- **Sifa za ubora ni mahitaji.** Utendaji, upatikanaji, usalama, na uwezo wa kudumishwa lazima zibainishwe kwa ukali ule ule kama vipengele, vinginevyo zitatolewa dhabihu chini ya shinikizo la tarehe ya mwisho.
- **Si kila hitaji ni muhimu kiusanifu.** Elekeza umakini adimu wa usanifu kwenye mahitaji yanayoumba muundo, magumu kubadilisha, au yenye hatari kubwa.
- **Usanifu lazima uweze kubadilika.** Usanifu mkubwa wa awali hushindwa kwa sababu maarifa ni machache zaidi mwanzoni; buni kwa kuongezeka na ulinde sifa muhimu kwa ukaguzi wa kiotomatiki.
- **Andika maamuzi, si michoro tu.** Hoja nyuma ya uchaguzi (na chaguo zilizokataliwa) ina thamani zaidi kuliko picha ya matokeo.
- **Fanya usanifu uweze kusomeka kwa wasioiunda.** Wanachama wapya, wakaguzi, na wadumishaji wa baadaye lazima waweze kujenga upya nia.
- **Ahirisha maamuzi unayoweza, amua yale lazima.** Weka chaguo wazi pale mabadiliko ni nafuu; jitolee mapema tu pale kujitolea kwa kuchelewa ni ghali.

## Mapendekezo

### Bainisha sifa za ubora kama hali zinazopimika

Malengo yasiyo wazi kama "mfumo unapaswa kuwa wa haraka" au "unaopatikana sana" hayawezi kujaribiwa wala kutekelezwa. Badala yake, andika kila sifa ya ubora kama hali madhubuti yenye kichocheo, muktadha, na jibu linalopimika: "Watumiaji wa wakati mmoja wa kilele wanapofikia 50,000, 95% ya maombi ya utafutaji hukamilika ndani ya ms 300." Funika sifa zinazojalisha kwa kikoa chako: upatikanaji, utendaji, ukubwa, usalama, uwezo wa kudumishwa, uonekanaji, ufikivu, uhamishikaji, na ufanisi wa gharama. Zipange kwa sauti, kwa sababu huwezi kuongeza zote kwa wakati mmoja. Mfumo uliorekebishwa kwa uthabiti wa juu kabisa hautakuwa pia na upatikanaji wa juu kabisa.

### Tambua mahitaji muhimu kiusanifu (ASRs)

Tenga muda kutenganisha ASR na mahitaji ya kawaida. Hitaji ni muhimu kiusanifu ikiwa linagusa vipengele vingi, ni ghali kutimiza, linaweka kikwazo kikali, au lina hatari ya kiufundi. Maagizo ya udhibiti (makazi ya data, uhifadhi, uwezo wa kukaguliwa), hali za mzigo wa juu, uunganishaji na mifumo ya rekodi ya urithi, na mipaka migumu ya usalama kwa kawaida ni ASR. Weka orodha fupi, hai yao, na ufuatilie maamuzi makubwa ya usanifu hadi orodha hiyo, ili wapitiaji waone kwa nini usanifu unaonekana ulivyo.

### Pokea usanifu wa kubadilika na kazi za ufaafu

Chukulia usanifu kama kitu kinachobadilika hatua kwa hatua kuelekea pande zinazoongozwa, si mchoro uliowekwa. **Kazi ya ufaafu** ni jaribio la kiotomatiki, la kimalengo kwamba sifa mahususi ya usanifu inashikilia: ukaguzi wa wakati wa ujenzi kwamba hakuna moduli inayoagiza kutoka safu iliyokatazwa, jaribio la utendaji linalofeli bomba ucheleweshaji wa p99 ukirudi nyuma, uchunguzi wa usalama unaozuia utegemezi wenye udhaifu unaojulikana, jaribio linalothibitisha hakuna huduma inayoshikilia muunganisho wa moja kwa moja kwenye hifadhidata ya huduma nyingine. Kazi za ufaafu hugeuza nia ya usanifu kuwa vizuizi vinavyotekelezwa mfululizo: njia pekee ya kuweka nia hiyo hai kuvuka timu kubwa, inayobadilika.

### Andika kwa C4 na arc42

Tumia **kielelezo cha C4** kuelezea muundo katika ngazi nne za ukaribu (Muktadha wa Mfumo, Vyombo, Vipengele, na Msimbo) ili kila hadhira isome ngazi inayoifaa na hakuna mchoro mmoja unaopaswa kusema kila kitu. Tumia **arc42** kama kiolezo cha simulizi linalozunguka: malengo, vikwazo, muktadha, mkakati wa suluhisho, vizuizi vya ujenzi, hali za wakati wa kuendesha, usambazaji, masuala ya kuvuka sehemu, maamuzi, na hatari. Rekodi maamuzi mahususi kama **[Rekodi fupi za Maamuzi ya Usanifu (ADR)](https://en.wikipedia.org/wiki/Architectural_decision)**: muktadha, uamuzi, hali, na matokeo, faili moja kwa kila uamuzi, zikiwekwa katika matoleo kando ya msimbo. Ukipokea tabia moja tu ya uandishi, ifanye iwe ADR: zinalipa zaidi kuliko kitu kingine chochote kwa timu kubwa.

### Endesha uchambuzi wenye muundo wa mabadilishano na uendeshe usanifu kwa hatari

Kwa mifumo yenye dau kubwa, tumia mbinu kama **[Architecture Tradeoff Analysis Method (ATAM)](https://en.wikipedia.org/wiki/Architecture_tradeoff_analysis_method)** kupima usanifu wagombea dhidi ya hali zilizopewa kipaumbele za sifa za ubora. Hufichua nukta za unyeti (ambapo uamuzi unaathiri sana sifa moja) na nukta za mabadilishano (ambapo unaathiri kadhaa). Kwa mguso mwepesi zaidi, pokea **usanifu unaoendeshwa na hatari**: tumia juhudi ya usanifu kulingana na hatari. Sehemu za hatari ndogo, zinazoeleweka vizuri zinahitaji taratibu chache. Maamuzi mapya, ya athari kubwa, au yasiyotenguka yanastahili mifano ya majaribio, uchunguzi mfupi, na mapitio rasmi.

## Mabadilishano: faida na hasara

| Mbinu | Faida | Hasara |
|---|---|---|
| Usanifu mkubwa wa awali | Uwazi wa uratibu; mshangao mdogo wa kuchelewa katika programu za wigo uliowekwa | Maamuzi yanafanywa maarifa yakiwa machache zaidi; polepole; dhaifu kwa mabadiliko |
| Usanifu unaojitokeza / wa kubadilika | Hubadilika na kujifunza; upotevu mdogo; unaunga mkono utoaji wa haraka | Hatari ya kuteleza bila kazi za ufaafu; inahitaji nidhamu imara ya kihandisi |
| Tathmini rasmi ya mtindo wa ATAM | Ya ukali, inayokaguliwa, hufichua migongano iliyofichika | Inahitaji muda na utaalamu mwingi; ya kupindukia kwa mabadiliko madogo |
| ADR nyepesi + C4 | Nafuu, zinasomeka, za kuongezeka, zinapanuka kwa timu nyingi | Ni nzuri tu kama nidhamu ya kuziweka za sasa |

Mvutano wa msingi ni kati ya uhakika na uwezo wa kubadilika. Programu za serikali za bei iliyowekwa na mifumo muhimu kwa usalama huegemea ukali zaidi wa awali na tathmini rasmi, kwa sababu gharama ya badiliko la kuchelewa au kushindwa ni kubwa mno. Mashirika ya bidhaa yanayosonga haraka huegemea njia za kubadilika zinazolindwa na uotomatishaji. Mashirika makubwa mengi yanahitaji yote mawili: utawala mzito zaidi kwa maamuzi yasiyotenguka, yenye athari kubwa na masuala ya kuvuka sehemu, na usanifu mwepesi, unaojitokeza kila mahali pengine. Ncha zote mbili hushindwa kwa njia zake: kuhandisi usanifu kupita kiasi hupoteza miaka na hakuletei kitu, wakati kuhandisi kidogo mno huzalisha mkanganyiko usioweza kupanuka wala kukaguliwa.

## Maswali ya kujadili na timu yako

1. **Sifa mbili za ubora zenu zinapogongana chini ya mzigo, ipi inashinda, na je, mmeandika mpangilio huo wa kipaumbele?** Kila usanifu hulazimisha mabadilishano: uthabiti wa juu kabisa hudhoofisha upatikanaji, usalama mkali huongeza ucheleweshaji, kache kali hupigana na uwezo wa kukaguliwa. Katika timu kubwa hatari ni kwamba vikundi tofauti hudhania kimyakimya vipaumbele tofauti, kwa hiyo kimoja huboresha uwezo wa kupitisha huku kingine kikilinda uthabiti mkali, na mgongano unajitokeza tu wakati wa tukio. Katika mazingira ya mashirika makubwa na serikali mdhibiti ataulizia sifa ipi mlilinda na kwa nini, kwa hiyo mpangilio lazima uwe wazi na unaoweza kutetewa badala ya hadithi za kale. Leta hali zenu za sifa za ubora na uzipange kwa sauti dhidi ya nyingine, jozi kwa jozi, hadi mpangilio uwe wazi bila utata. Kisha weka mshindi kwenye kazi ya ufaafu ili kipaumbele kishikilie chini ya shinikizo la tarehe ya mwisho badala ya kumomonyoka.

2. **Ni maamuzi gani ya hivi karibuni yalikuwa milango ya njia moja, na je, yalipata uchunguzi zaidi kuliko milango ya njia mbili?** Usanifu unaoendeshwa na hatari husema tumia juhudi ya usanifu kulingana na ugumu wa kutengua uamuzi, hata hivyo timu nyingi hupitia kila badiliko kwa taratibu zinazofanana kwa takriban. Hilo hupoteza umakini kwenye uchaguzi wa nafuu, unaotenguka huku usiotenguka (kielelezo cha data kilichowekwa katika rekodi ya kisheria, mkataba wa API ya umma, hifadhidata ya msingi) ukiteleza na changamoto kidogo mno. Vuta maamuzi muhimu ya robo iliyopita na uyapange kwa uwezo wa kutenguka, kisha uliza kama yale yasiyotenguka yalipata mifano ya majaribio, uchunguzi mfupi, au mapitio rasmi. Katika mifumo ya mashirika makubwa na serikali ya muda mrefu gharama ya mlango mbaya wa njia moja hujumlika kwa muongo, kwa hiyo ukali wa ziada unalipa mara nyingi. Linganisha uzito wa mchakato wenu na uwezo wa kutenguka wa uamuzi, si ukubwa wa tofauti ya msimbo.

3. **Kwa uamuzi wenu unaofuata wenye dau kubwa, mgumu kutengua, nani anahitaji kuwa chumbani, na mtapima chaguo dhidi ya hali zipi?** Mapitio ya mabadilishano yenye muundo kwa mtindo wa ATAM yanastahili gharama yake uamuzi unapokuwa usiotenguka na kugusa sifa kadhaa za ubora kwa wakati mmoja, na nguvu yake inatokana na watu waliopo: utoaji, usalama, uendeshaji, na wamiliki wa sera au biashara wanaohisi matokeo. Ruka sauti moja kati ya hizo na unagundua mgongano baada ya ujenzi, kama vile uchaguzi wa kache unavyoweza kuvunja kimyakimya hitaji la uwezo wa kukaguliwa. Leta hali za sifa za ubora zilizopewa kipaumbele kama kigezo cha kupima, na utafute nukta za unyeti ambapo chaguo moja husukuma sifa moja kwa nguvu na nukta za mabadilishano ambapo linahamisha kadhaa. Matokeo unayoyataka ni ADR fupi inayorekodi chaguo mlizokataa na kwa nini, ili hoja inusurike watu waliofanya. Hakuna uamuzi unaokuja unaoonekana kuhalalisha hili, hilo lenyewe linastahili kukaguliwa, kwa sababu programu kubwa isiyo na maamuzi yasiyotenguka upeo wa macho kwa kawaida haitazami mbali vya kutosha.

4. **Mwanachama mpya au mkaguzi wa nje akiwa na usanifu wenu ulioandikwa tu, wangeweza kujenga upya kwa nini mfumo una umbo ulilo nalo, na lini mara ya mwisho mlilijaribu hilo?** Usanifu unaoishi katika vichwa vya wakuu wachache ni nukta moja ya kushindwa: watu hao wanapohama, hoja nyuma ya kila uamuzi mgumu kutengua inahama nao, na timu inayofuata inaijifunza upya kupitia matukio. Kwa shirika kubwa usomekaji wa usanifu (michoro ya C4 inayolingana na uhalisia, simulizi la arc42, ADR zinazorekodi chaguo zilizokataliwa) ndio unaoruhusu timu kadhaa kufikiri kuhusu mfumo ule ule bila mkutano. Leta ADR ya hivi karibuni na mchoro wa sasa, mkabidhi mtu ambaye hakujenga kijenzi, na utazame anafika umbali gani kabla ya kulazimika kumuuliza mtu. Katika mazingira ya mashirika makubwa na serikali mkaguzi atafanya zoezi hilohilo hasa, na nyaraka zinazoelezea mfumo wa mwaka jana ni mbaya kuliko kutokuwa nazo kwa sababu zinawapotosha watu hasa wanaopaswa kuthibitisha. Chukulia ubichi wa rekodi iliyoandikwa kama sifa inayopimika, na uweke kazi ya ufaafu au mzunguko wa mapitio nyuma ya kuiweka kweli.

5. **Ni sifa zipi za usanifu wenu zinalindwa na kazi ya ufaafu ya kiotomatiki leo, na zipi bado zinategemea kila mtu kukumbuka kanuni?** Nia inayoishi kwenye ukurasa wa wiki au kumbukumbu ya mpitiaji tu humomonyoka tarehe ya mwisho inapofika, kwa sababu kanuni ya tabaka, mpaka wa kutokuwa na hifadhidata ya pamoja, na bajeti ya ucheleweshaji ndizo hasa timu hukata zikiwa chini ya shinikizo. Katika msimbo mkubwa unaobadilika haraka, nia pekee inayonusurika ni ile ambayo ujenzi unaitekeleza, kwa hiyo pengo kati ya sifa mnazodai na zile mnazokagua kweli ndilo hatari yenu halisi ya usanifu. Orodhesha sifa zenu muhimu, weka alama kila moja kuwa inatekelezwa, inapitiwa kwa mkono, au haina ulinzi, na uleta mara tatu za mwisho ambazo mapitio yalinasa kuteleza ambako kazi ya ufaafu ingeweza kunasa mapema. Katika mifumo inayodhibitiwa na ya umma hili ni muhimu mara mbili, kwa sababu mdhibiti ataulizia si kama mlikusudia makazi ya data au uwezo wa kukaguliwa bali jinsi mnavyothibitisha ulishikilia mfululizo, na bomba la kijani ni jibu lenye nguvu zaidi sana kuliko waraka wa sera. Pa kipaumbele uotomatishaji wa sifa ambazo kushindwa kwake kuna uwezekano mkubwa na ni ghali, na ukubali kwamba baadhi zitabaki za mkono.

6. **Mnapoamua kama hitaji ni muhimu kiusanifu, nani anafanya uamuzi huo, na mnawezaje kuzuia orodha ya ASR isiwe kila kitu au hakuna?** Thamani ya kutaja mahitaji muhimu kiusanifu inatokana na uteuzi: chukulia kila hitaji kuwa muhimu na usanifu unakwama, chukulia hakuna kuwa muhimu na yale ya kimuundo, ya hatari, magumu kubadilisha yanateleza bila ulinzi. Katika timu kubwa kishawishi ni kuruhusu kila kikundi kiamue kwa ndani, jambo linalozalisha viwango visivyo thabiti na mshangao wa kuvuka timu uchaguzi "mdogo" wa kundi moja unapodhibiti muundo wa jingine. Leta orodha yenu ya sasa ya ASR, vigezo mlivyotumia (inagusa vipengele vingi, ghali kutimiza, kikwazo kikali, hatari ya kiufundi), na mahitaji machache ya mpakani kujaribu mpaka kwa sauti. Kwa mashirika makubwa na serikali, maagizo ya udhibiti kama makazi ya data, uhifadhi, na uwezo wa kukaguliwa karibu daima ni muhimu na hayajadiliwi, kwa hiyo taja nani anamiliki orodha, inapitiwaje, na uamuzi wa kuongeza au kuacha ASR unarekodiwaje, kwa sababu ASR ambayo hakuna anayeitawala ni hitaji ambalo hakuna atakayelitetea chini ya uchunguzi.

## Mtazamo wa sekta

**Kampuni changa.** Weka taratibu karibu na sifuri na rekodi karibu kamili. Ruka warsha rasmi za ATAM na violezo vizito, lakini bado andika ADR fupi kadhaa kwa uchaguzi ambao ungekuwa na maumivu kutengua (hifadhidata, monolith dhidi ya huduma, mtoa uthibitishaji) na uweke hali mbili au tatu za sifa za ubora ambazo wateja wako wa mapema wanazihisi kweli. Rasilimali yako adimu ni umakini wa kihandisi, kwa hiyo linda tu sifa ambazo kushindwa kwake kungekuzamisha, kama kutengwa kwa wapangaji, na uache kila kitu kingine kijitokeze na kubaki nafuu kubadilisha.

**Biashara ndogo.** Bila mbunifu maalumu na bajeti finyu, tegemea misingi isiyogharimu karibu chochote: taja sifa zako chache za ubora kama namba madhubuti, andika ADR kwa chochote ambacho ungehangaika kutengua, na uache jukwaa au muuzaji uliyemchagua abebe maamuzi mazito ya kimuundo. Pendelea kununua mfumo unaosaidiwa vizuri kuliko kujenga miundombinu maalumu, na uchukulie usanifu ulioandikwa wa muuzaji kama kikwazo unachorithi badala ya kile unachopaswa kukiandika kutoka mwanzo.

**Biashara kubwa.** Changamoto ni mshikamano kuvuka timu nyingi na miaka ya ramani ya barabara, kwa hiyo wekeza katika mashine ya pamoja: chama cha usanifu, seti ya pamoja ya hali za sifa za ubora, ADR zilizohifadhiwa kando ya msimbo, na kazi za ufaafu kwenye CI zinazotekeleza mipaka ambayo mpitiaji mmoja hawezi kuilinda kwa ukubwa. Tumia uchambuzi wenye muundo wa mabadilishano kwa maamuzi yasiyotenguka, ya kuvuka sehemu, weka michoro ya C4 kama ramani ya pamoja katika mapitio ya usanifu, na utawale orodha ya ASR kati ili vikundi viache kufanya uchaguzi unaofaa kimahali unaogongana kimataifa.

**Serikali.** Mifumo ya muda mrefu, inayodhibitiwa hufanya usanifu ulioandikwa, unaoweza kutetewa kuwa sharti la ununuzi na uwajibikaji, si fadhila. Chukulia makazi ya data, uhifadhi, uwezo wa kukaguliwa, na ufikivu kama mahitaji muhimu kiusanifu yaliyoandikwa kwenye maelezo ya arc42 ambayo wakaguzi wanaweza kuyasoma moja kwa moja, na uendeshe warsha nyepesi za mabadilishano zinazojumuisha maafisa wa sera na usalama ili migongano (kama kache dhidi ya uwezo wa kukaguliwa) ijitokeze kwenye karatasi kabla ya msimbo. Weka njia ya hoja kamili vya kutosha kwamba afisa anayewajibika anaweza kuonyesha bidii, na upendelee usanifu wenye njia wazi za kutoka kuliko ule unaofunga chombo cha umma kwa muuzaji mmoja kwa muongo.

## Mifano

**Kampuni changa.** Timu ya SaaS ya hatua ya mbegu ya watu sita inaweka usanifu wake kwenye waraka wa pamoja badala ya mchakato rasmi, lakini bado inaandika maamuzi yangekuwa na maumivu kutengua. Wanarekodi takriban ADR kumi na mbili (kwa nini Postgres badala ya hifadhi ya nyaraka, kwa nini monolith ya moduli badala ya huduma, kwa nini walichagua mtoa uthibitishaji wao) na kuweka hali mbili za sifa za ubora zinazojalisha kweli kwa wateja wa mapema: "usajili unakamilika chini ya sekunde mbili" na "hakuna mteja anayeweza kusoma data ya mpangaji mwingine kamwe." Wanapoajiri wahandisi wao wa saba na wa nane, maelezo hayo huwaruhusu wageni kusafirisha wiki yao ya kwanza badala ya kumkatiza kila mtu kuuliza kwa nini mambo ni yalivyo.

**Biashara kubwa.** Benki ya kimataifa inaunganisha mifumo kumi na miwili ya malipo ya kikanda, kwa hiyo inaanzisha chama kidogo cha usanifu. Chama kinafafanua hali nane za sifa za ubora (ikiwemo "chakata miamala 10,000 kwa sekunde bila muamala uliopotea" na "rejesha kanda ndani ya dakika 15"), kinanasa takriban ADR arobaini, na kutekeleza kazi za ufaafu kwenye CI ([ujumuishaji endelevu](https://en.wikipedia.org/wiki/Continuous_integration)): hakuna huduma inayoweza kuandika kwenye hifadhidata ya kikoa kingine, miito yote ya huduma-hadi-huduma lazima ifuatiliwe, na utegemezi wowote wenye [CVE](https://en.wikipedia.org/wiki/Common_Vulnerabilities_and_Exposures) (Common Vulnerabilities and Exposures) muhimu unafeli ujenzi. Michoro ya muktadha na vyombo ya C4 inakuwa ramani ya pamoja katika kila mapitio ya usanifu, na migogoro ya uunganishaji kuvuka timu inapungua kwa kasi.

**Serikali.** Wakala wa kitaifa unaboresha jukwaa la manufaa, na sheria inauhitaji kuhakikisha makazi ya data, uwezo wa kukaguliwa wa miaka saba, na ulinganifu wa ufikivu. Wasanifu wake wanachukulia haya kama ASR na kuyaandika kwenye maelezo ya arc42 ambayo wakaguzi wanayapitia moja kwa moja. Wanaendesha warsha nyepesi ya ATAM na timu za utoaji, usalama, na maafisa wa sera kulinganisha usanifu mbili wagombea, na kugundua kwamba mkakati wa kache wa muundo unaopendelewa unagongana na hitaji la uwezo wa kukaguliwa. Kunasa mabadilishano hayo kwenye karatasi, kabla ya mstari mmoja wa msimbo, kunaokoa miezi ya kurudia kazi na kumpa waziri anayewajibika ushahidi ulioandikwa wa bidii.

## Kesi ya biashara: sababu, ROI, na TCO

Mapato ya misingi ya usanifu hasa ni gharama iliyoepukwa, ambayo huifanya iwe rahisi kuipa fedha kidogo na ghali kuiruka. Gharama ya kupokea ni ya wastani: muda wa wasanifu wachache wenye uzoefu, warsha chache, kiolezo cha nyaraka, na uwekezaji wa CI katika kazi za ufaafu, kwa kawaida asilimia ndogo ya tarakimu moja ya bajeti ya programu. Gharama ya *kutopokea* inafika baadaye, na kwa bei ya juu: kurudia kazi wakati sifa ya ubora isiyobainishwa inashindwa kwenye uzalishaji, kuhamisha jukwaa kwa dharura wakati uunganishaji usioandikwa unazuia badiliko lililoamriwa, matukio marefu kwa sababu hakuna anayeelewa mfumo, na ukaguzi ulioshindwa unaosimamisha utoaji au kuchochea faini.

Kwa uongozi, weka hoja katika uchaguzi na hatari. Misingi mizuri ya usanifu hupunguza gharama ya mabadiliko ya baadaye (kiegemeo cha moja kwa moja kwenye kasi ya utoaji na jumla ya gharama ya umiliki kwa maisha ya mfumo ya muongo), hupunguza mara ngapi na kwa muda gani matukio makali hudumu, na hutoa njia ya nyaraka ambayo wadhibiti na wakaguzi sasa wanadai. Tabia ya ADR peke yake inajilipa mara ya kwanza timu mpya ya uongozi inapouliza "kwa nini tulijenga hivi?" na kupata jibu ndani ya dakika badala ya uchunguzi wa kina. Weka namba pale unapoweza: pima gharama ya usanifu upya mkubwa mmoja ulioepukwa, au ukaguzi mmoja ulioshindwa ulioepukwa, dhidi ya gharama ndogo inayoendelea ya mazoea.

## Mifumo mibaya na mitego

- **Usanifu wa mnara wa pembe.** Wasanifu wanaozalisha michoro lakini hawagusi msimbo wala kuzungumza na timu za utoaji; miundo yao inapuuzwa au haiwezi kujengwa.
- **Sifa za ubora kama vivumishi.** "Inayopanuka, salama, ya kutegemewa" bila namba, bila hali, na kwa hiyo hakuna njia ya kuthibitisha au kubadilishana.
- **Usanifu mkubwa wa awali.** Kujitolea kwa kila undani kabla ya mstari wa kwanza wa msimbo, kufunga maamuzi wakati uelewa ni dhaifu zaidi.
- **Nyaraka zinazosema uongo.** Michoro inayoelezea mfumo wa mwaka jana; mbaya kuliko kutokuwa nayo kwa sababu inapotosha.
- **Usanifu wa wasifu.** Kuchagua teknolojia kujenga kazi badala ya kutimiza ASR.
- **Kupamba kupita kiasi.** Kuhandisi kwa ukubwa, unyumbufu, au ujumla ambao mahitaji hayakuuomba, kuongeza gharama na ugumu wa kudumu.
- **Hakuna vizuizi vya usanifu.** Kutegemea nia njema badala ya kazi za ufaafu kuhifadhi muundo kuvuka timu kubwa.

## Kielelezo cha ukomavu

- **Ngazi ya 1: Kuanzisha.** Usanifu ni wa dhahiri na unaishi vichwani mwa watu binafsi. Hakuna sifa za ubora zilizoandikwa, hakuna ADR, hakuna michoro ya pamoja. Muundo unagunduliwa wakati wa matukio, na kila utegemezi wa kuvuka timu unajadiliwa upya kutoka mwanzo.
- **Ngazi ya 2: Kuendeleza.** Baadhi ya timu zinaandika maamuzi ambayo yangeumiza kutengua na kuchora michoro muhimu, lakini mazoea hayana uthabiti: kikundi kimoja kinaweka ADR huku kingine hakiweki, sifa za ubora zinatajwa kama vivumishi badala ya hali zinazopimika, na nyaraka zinateleza kutoka mradi hadi mradi.
- **Ngazi ya 3: Kusawazisha.** Hali za sifa za ubora na mahitaji muhimu kiusanifu yanabainishwa na kupewa kipaumbele kwa kiwango kilichoandikwa cha shirika zima. ADR ni za kawaida na zimehifadhiwa kando ya msimbo, nyaraka za C4 na arc42 zinadumishwa kwa kiolezo cha pamoja, na mapitio yenye muundo ya mabadilishano yanahitajika kwa maamuzi muhimu kuvuka kila timu.
- **Ngazi ya 4: Kusimamia.** Usanifu unapimwa dhidi ya vipimo vya msingi badala ya kudaiwa. Kazi za ufaafu kwenye CI zinaripoti sifa kama ucheleweshaji wa p99, ukiukaji wa tabaka, miito isiyofuatiliwa, na utegemezi wenye udhaifu; ufikiaji wa ADR na ubichi wa nyaraka unafuatiliwa kama vipimo; mapitio ya mabadilishano yanapima chaguo dhidi ya hali zilizopewa kipaumbele; na kuteleza dhidi ya vipimo vya msingi vilivyokubaliwa huchochea jibu lililofafanuliwa badala ya mshangao. Wakaguzi wanaweza kutegemea ushahidi uliopimwa badala ya simulizi peke yake.
- **Ngazi ya 5: Kuratibu.** Usanifu hubadilika mfululizo na kwa kujirekebisha kuvuka shirika zima. Data ya kazi za ufaafu na matukio hulisha sifa zipi zinajalisha na juhudi ya usanifu inakoenda; orodha za ASR, vipaumbele vya sifa za ubora, na vizuizi vinawekwa upya wigo maagizo na hatari zinapohama; na mazoea yameunganishwa na utoaji, usalama, na upangaji wa hatari ili jukwaa lijirekebishe kwa mahitaji mapya badala ya kujengwa upya kutoka mwanzo.

## Mawazo ya kujadili

1. Ni sifa gani tatu za ubora zisizojadiliwa kweli kwa mfumo wenu muhimu zaidi, na je, mnaweza kuzitaja kila moja kama hali inayopimika leo?
2. Mnaamuaje wakati uamuzi ni "muhimu kiusanifu" vya kutosha kustahili ADR dhidi ya kuufanya tu?
3. Wapi kazi za ufaafu zingenasa kuteleza ambako mapitio yenu ya sasa ya msimbo yanakosa?
4. Je, shirika lenu linahandisi usanifu kupita kiasi au kidogo mno, na ushahidi gani unawaambia ipi?
5. Nani anawajibika kwa usanifu katika muundo wa timu-za-timu, na mnaepukaje minara ya pembe na machafuko kamili?
6. Mkaguzi wa nje angejengaje upya nia ya usanifu wenu kutoka kinachoandikwa leo?

## Mambo muhimu ya kukumbuka

- Usanifu ni seti ya maamuzi ambayo ni ghali kutengua; fanya mabadilishano hayo kwa makusudi na uyarekodi.
- Bainisha sifa za ubora kama hali zinazopimika na utambue mahitaji muhimu kiusanifu yanayoumba muundo.
- Buni kwa kuongezeka na ulinde sifa muhimu za usanifu kwa kazi za ufaafu za kiotomatiki.
- Andika kwa wepesi lakini kwa ukweli ukitumia michoro ya C4, simulizi la arc42, na ADR kwa kila uamuzi zilizohifadhiwa kando ya msimbo.
- Linganisha ukali na hatari: uchambuzi mzito kwa maamuzi yasiyotenguka, ya athari kubwa; taratibu nyepesi kila mahali pengine.
- Kesi ya biashara ni kurudia kazi kulikoepukwa, matukio mafupi, mabadiliko ya baadaye ya haraka, na ushahidi tayari kwa ukaguzi.

## Marejeo na usomaji zaidi

- Len Bass, Paul Clements, and Rick Kazman, *Software Architecture in Practice*
- Neal Ford, Rebecca Parsons, and Patrick Kua, *Building Evolutionary Architectures*
- Simon Brown, *Software Architecture for Developers* (and the C4 model)
- Mark Richards and Neal Ford, *Fundamentals of Software Architecture*
- George Fairbanks, *Just Enough Software Architecture: A Risk-Driven Approach*
- Michael Nygard, "Documenting Architecture Decisions" (the ADR pattern)
- Gernot Starke and Peter Hruschka, *arc42* documentation template
- Paul Clements et al., *Evaluating Software Architectures: Methods and Case Studies* (ATAM)
- ISO/IEC 25010, *Systems and software quality models*
