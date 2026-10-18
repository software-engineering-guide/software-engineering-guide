# 6.3 AI ya kuzalisha na programu za LLM

## Muhtasari na msukumo

[AI ya kuzalisha](https://en.wikipedia.org/wiki/Generative_artificial_intelligence), na hasa [mifano mikubwa ya lugha](https://en.wikipedia.org/wiki/Large_language_model) (LLM), inaweza kuzalisha maandishi fasaha, msimbo, muhtasari, na data yenye muundo kutoka maagizo ya lugha asilia. Hilo huifanya kuwa vipengele vyenye nguvu vya wasaidizi, utafutaji, uchakataji wa nyaraka, na uotomatishaji. Lakini nguvu hizo huja na wasifu wa kipekee wa hatari. LLM ni za uwezekano. Zinaweza kuzalisha uongo wenye imani ([hallucinations](https://en.wikipedia.org/wiki/Hallucination_(artificial_intelligence))). Ni nyeti kwa jinsi unavyozielekeza. Na zinafungua nyuso mpya za shambulio kama [sindano ya maagizo](https://en.wikipedia.org/wiki/Prompt_injection) (maagizo hasidi yanayoingizwa kwenye ingizo ili kuteka tabia ya mfano). Kwa hiyo kujenga programu za LLM zinazotegemewa kunahusu kidogo mfano na zaidi uhandisi unaouzunguka: jinsi unavyotoa muktadha, kuweka majibu kwenye maarifa yanayoaminika, kubana matokeo, na kutathmini ubora.

Kwa timu kubwa, programu za LLM zinadai mifumo mipya inayotofautiana na programu ya kawaida na kujifunza kwa mashine ya kawaida. Mara nyingi hakuna hatua ya mafunzo. Badala yake, tabia huumbwa na maagizo, muktadha uliorejeshwa, fasili za zana, na vizuizi (ukaguzi wa wakati wa kuendesha unaobana ingizo na matokeo ya mfano). Hilo huhamisha juhudi ya kihandisi kuelekea usimamizi wa muktadha, ubora wa urejeshaji, uratibu, na tathmini. Mashirika yanayopokea LLM kwa ukubwa yanahitaji mifumo ya pamoja ili kila timu isigundue upya njia zilezile za kushindwa kwa njia ngumu.

Mashirika ya serikali na yanayodhibitiwa yanakabiliwa na madai ya ziada. LLM inayobuni nukuu ya sera au kuvujisha data nyeti si hitilafu tu; inaweza kuwa tukio la kisheria au la usalama. Mazingira haya yanahitaji msingi kwenye vyanzo vyenye mamlaka, uthibitishaji mkali wa matokeo, usimamizi wa binadamu kwa matokeo yenye athari, na rekodi wazi za kile mfumo uliulizwa na kile ulichozalisha. Mbinu katika sura hii (uzalishaji unaoongezwa kwa urejeshaji, vizuizi, na tathmini kali) ndizo zinazofanya LLM kuwa salama vya kutosha kusambazwa katika mazingira ya dau kubwa. Mifano ya Claude ya Anthropic ni chaguo moja linaloongoza kati ya watoa huduma kadhaa wenye uwezo; mazoea hapa yanatumika bila kujali mfano unaochagua.

## Kanuni kuu

- Weka mfano kwenye maarifa yanayoaminika badala ya kutegemea ulichokariri.
- Chukulia maagizo na muktadha kama mabaki yaliyohandisiwa, yenye matoleo, si mifuatano ya kutupwa.
- Dhania mfano unaweza kuwa si sahihi au kudanganywa; thibitisha matokeo na ubane vitendo.
- Mpe mfano muktadha na zana anazohitaji tu, si zaidi, ili kupunguza makosa na uso wa shambulio.
- Tathmini mfululizo kwa seti za majaribio zisizo mtandaoni, vipimo vya mtandaoni, na busara ya binadamu.
- Weka binadamu kwenye mzunguko kwa matokeo yenye athari.
- Sanifu kwa mfano kama kijenzi kisichoaminika ndani ya mfumo unaoaminika.

## Mapendekezo

### Handisi maagizo na simamia muktadha kwa makusudi

Chukulia maagizo kama msimbo: yahifadhi kwenye udhibiti wa matoleo, pitia mabadiliko, na uyajaribu dhidi ya seti ya mifano. Panga kila agizo kwa uwazi: jukumu na kazi, vikwazo, mahitaji ya umbo, na mifano pale inaposaidia. Chukulia dirisha la muktadha (kipande kilichowekwa cha maandishi ambacho mfano unaweza kuzingatia kwa wakati mmoja) kama rasilimali adimu. Jumuisha taarifa husika zaidi, ipange kwa busara, na uondoe kelele, kwa sababu muktadha usiohusika au mwingi kupita kiasi hudhoofisha ubora na kuongeza gharama. Kwa programu za mizunguko mingi, simamia hali ya mazungumzo waziwazi, ukifupisha au kukata historia kubaki ndani ya mipaka huku ukihifadhi kinachojalisha. Pendelea maagizo wazi na mifano-michache (maonyesho machache yaliyofanyiwa kazi yaliyojumuishwa kwenye agizo) kuliko hila za kina zinazovunjika mara mfano unapobadilika.

### Weka majibu kwenye msingi kwa uzalishaji unaoongezwa kwa urejeshaji (RAG)

Kwa kazi nzito za maarifa, rejesha nyaraka husika kutoka mkusanyiko unaoaminika na uziwasilishe kwa mfano kama muktadha, ukiuambia ujibu kutoka nyenzo hiyo tu na kunukuu vyanzo vyake. RAG huweka maarifa ya sasa bila kufunza upya, hubana majibu kwenye maudhui yaliyoidhinishwa, na huwezesha kunukuu na kuthibitisha. Wekeza kwenye ubora wa urejeshaji: gawanya nyaraka kwa busara, chagua [embeddings](https://en.wikipedia.org/wiki/Word_embedding) (uwakilishi wa vekta za namba unaoweka maana zinazofanana karibu) zinazofaa eneo lako, na kagua kama vifungu vilivyorejeshwa vina jibu kweli, kwa sababu jibu fasaha lililojengwa juu ya kifungu kisicho sahihi ni mbaya kuliko hakuna jibu. Na pale hakuna chochote husika kinapopatikana, fanya mfumo useme hivyo badala ya kubuni maudhui.

### Jenga mawakala na matumizi ya zana kwa uangalifu

LLM zinaweza kuita zana (utafutaji, hifadhidata, vikokotoo, API za ndani) na zinaweza kuunganishwa kuwa mawakala wanaopanga na kutenda kwa hatua kadhaa. Hii huongeza uwezo halisi, lakini pia huzidisha hatari: kila zana ni njia nyingine ya mfano usio sahihi au uliodanganywa kusababisha madhara. Fafanua zana kwa skima sahihi, thibitisha kila hoja, tumia upendeleo mdogo, na uhitaji uthibitisho au idhini ya binadamu kwa vitendo vyenye athari kama kutuma mawasiliano au kuhamisha fedha. Weka mizunguko ya wakala ikiwa na mipaka, inayoonekana, na inayoweza kukatizwa. Anza na zana zenye wigo mkali, za madhumuni moja kabla hujafikia uhuru usio na mipaka.

### Ongeza vizuizi na thibitisha matokeo

Funika mfano kwa tabaka za ulinzi. Njiani ndani, chuja na gundua sindano ya maagizo, hasa maudhui yasiyoaminika (kurasa za wavuti, nyaraka za mtumiaji) yanapoingia kwenye muktadha. Njiani nje, thibitisha muundo dhidi ya skima, kagua madai dhidi ya vyanzo, chuja maudhui yasiyo salama au yasiyozingatia, na kataa au jaribu tena uthibitishaji unaposhindwa. Kwa matokeo yenye muundo, chambua na thibitisha badala ya kuamini umbizo la mfano. Usiruhusu kamwe matokeo ghafi ya mfano kuchochea vitendo visivyoweza kurekebishwa bila uthibitishaji. Chukulia kupunguza hallucination kama sifa ya mfumo unayoipata kupitia msingi, kunukuu, uthibitishaji, na mapitio ya binadamu, si kitu ambacho mfano unakisimamia peke yake.

### Tathmini nje ya mtandao, mtandaoni, na kwa binadamu

Jenga mfululizo wa tathmini wa ingizo za uwakilishi zenye matokeo yanayojulikana mazuri au yaliyopimwa kwa kigezo, na uuendeshe kwa kila badiliko la agizo au mfano (tathmini ya nje ya mtandao). Pima tabia halisi kwenye uzalishaji kwa vipimo kama mafanikio ya kazi, kiwango cha kupandisha ngazi, na maoni ya mtumiaji (tathmini ya mtandaoni). Kwa ubora wa kiubinafsi, tumia wapitiaji wa binadamu na, kwa uangalifu, upimaji unaotegemea mfano. Tathmini ndiyo wavu wa usalama unaokuruhusu kubadilisha maagizo na mifano kwa imani. Bila hiyo, unaruka kipofu.

## Mabadilishano: faida na hasara

| Chaguo | Faida | Hasara | Bora wakati |
|---|---|---|---|
| Maagizo tupu | Rahisi, haraka, nafuu kubadilisha | Msingi mdogo, inaweza kuota | Kazi pana, dau dogo |
| RAG | Ya sasa, yenye msingi, inayonukuliwa | Urejeshaji ni mgumu kupata sawa | Kazi nzito za maarifa, za kweli |
| Mawakala wenye zana | Wenye nguvu, wanaweza kutenda | Uso mkubwa wa shambulio, ngumu kudhibiti | Uotomatishaji wenye wigo mzuri na vizuizi |
| Mfano mkubwa, imara zaidi | Ubora na hoja bora | Gharama na ucheleweshaji wa juu | Kazi ngumu au za dau kubwa |
| Mfano mdogo, nafuu zaidi | Haraka na wa bei nafuu | Dhaifu kwenye kazi ngumu | Kiasi kikubwa, kazi rahisi |

Mvutano wa msingi ni uwezo dhidi ya udhibiti na gharama. Uhuru zaidi na mifano mikubwa hutoa thamani zaidi, lakini zinadai vizuizi zaidi, tathmini zaidi, na fedha zaidi. Msingi kupitia RAG unaboresha uaminifu kwa gharama ya uhandisi wa urejeshaji. Mizani sahihi inategemea dau: programu za dau kubwa zinaelekea msingi, uthibitishaji, na usimamizi wa binadamu, hata unapogharimu zaidi.

## Maswali ya kujadili na timu yako

1. **Kiwango gani cha usahihi na msingi kipengele cha LLM lazima kifikie kabla ya kukabili umma, na nani anaidhinisha?** Jibu fasaha linalonukuu chanzo kisicho sahihi au kubuni sera ni baya kuliko hakuna jibu, na katika serikali nukuu iliyobuniwa ni tukio la kisheria, si hitilafu. Kwa timu kubwa, kiwango wazi kinazuia kila kikundi kuweka kizingiti chake cha faragha kwa hisia. Leta ufafanuzi wenu wa "msingi wa kutosha": kama kila dai lazima lifuatilike hadi chanzo kilichorejeshwa, kilichothibitishwa, kama mfumo lazima ukatae urejeshaji unapokosa matokeo, na seti yenu ya tathmini ya uadui inafunika nini kweli. Ishara ya kutazama ni kama yeyote anaweza kusafirisha badiliko la agizo moja kwa moja kwa watumiaji bila mbio ya regression. Kama dau ni la kisheria au la usalama, jibu linapaswa kuelekeza matokeo ya hatari kubwa zaidi kupitia mpitiaji wa binadamu mwenye mamlaka halisi kabla ya kutolewa.

2. **Vipengele vyetu vipi vya LLM ni mawakala kwa siri, na je, kila zana imepewa upendeleo mdogo na lango la binadamu kwa vitendo visivyoweza kurekebishwa?** Kipengele chochote kinachoruhusu mfano kuita zana au kutenda kwa hatua kadhaa kimevuka kuingia eneo la wakala, na kila zana ni njia nyingine ya mfano usio sahihi au uliodanganywa kusababisha madhara. Kwa mashirika yanayounganisha LLM na API za ndani, swali hili hufichua hatari ambayo lebo ya "msaidizi rahisi" huificha. Leta orodha ya kila zana ambayo mfano unaweza kuita, uthibitishaji wa hoja zake, wigo wa upendeleo wake, na vitendo vipi (kutuma mawasiliano, kuhamisha fedha, kubadilisha rekodi) vinahitaji uthibitisho. Jadili kama mizunguko ya wakala ina mipaka, inaonekana, na inakatizika. Jibu linapaswa kubana wigo na kuongeza malango ya idhini ya binadamu popote kitendo chenye athari au kisichoweza kurekebishwa kinafikika sasa bila moja.

3. **Tungejuaje ndani ya siku moja kwamba ubora wa urejeshaji wetu umeshuka, kwa kuwa jibu lenye imani lililojengwa juu ya kifungu kisicho sahihi linaonekana sawa?** RAG hufanya majibu kuaminika tu urejeshaji unapoleta kifungu chenye jibu kweli, na urejeshaji huoza kimyakimya nyaraka zinapobadilika, vipande vinapochakaa, au embeddings zinapoteleza kutoka eneo lenu. Kwa kuwa mfano bado unaandika kwa ufasaha juu ya muktadha mbaya, watumiaji huenda hawalalamiki hadi uaminifu tayari umepotea. Leta vipimo vyenu vya sasa vya ucheleweshaji na ukumbukaji wa urejeshaji, jinsi mnavyokagua kama vifungu vilivyorejeshwa vina jibu kweli, na jinsi usafi wa faharasa unavyoenda sambamba na mabadiliko ya nyaraka. Kwa usambazaji wa dau kubwa au wa umma, jadili kuandika vyanzo vilivyorejeshwa kwa ukaguzi ili uweze kufuatilia jibu baya hadi kifungu chake kibaya. Kama hamna tathmini yoyote ya urejeshaji, mnaweka msingi kwa imani.

4. **Tunachukulia maagizo, muktadha, na seti za tathmini kama mabaki yenye matoleo, yaliyopitiwa, au kama mifuatano iliyotawanyika kwenye madaftari na kumbukumbu za gumzo?** Maagizo yanapoenea kuvuka timu bila matoleo na yakirudiwa, marekebisho mahali pamoja hayafiki kwingine, na hakuna anayeweza kuzalisha upya mfumo uliambiwa kufanya nini robo iliyopita. Kwa timu kubwa, rejista ya pamoja ya maagizo na mfululizo wa regression unaoendeshwa kwa kila badiliko ndivyo vinavyoruhusu kubadilisha mfano au kuhariri agizo bila kuvunja kimyakimya kipengele cha timu mbili mbali. Mvuto unaoshindana ni kasi: wahandisi hurudia haraka zaidi wanapobandika agizo na kusafirisha, kwa hiyo kubaliana mstari uko wapi kati ya majaribio ya haraka na chochote kinachogusa watumiaji. Leta mahali maagizo yenu yanaishi leo kweli, kama seti ya tathmini inaweka lango la mabadiliko, na jinsi mnavyoweka matoleo kwenye mkusanyiko wa urejeshaji kando ya agizo. Katika mazingira ya mashirika makubwa na serikali, ongeza sharti la ukaguzi: huenda ukalazimika kuonyesha hasa agizo gani na vyanzo vipi vilizalisha matokeo fulani miezi baadaye, na agizo usiloweza kulijenga upya ni rekodi usiyoweza kuitetea.

5. **Kiasi kinapokua, tutadhibiti vipi gharama ya uelekezaji bila kudhoofisha ubora kimyakimya, na nani anamiliki uamuzi wa kuchagua mfano?** TCO kwa vipengele vya LLM inatawaliwa na uelekezaji wa kila mwito, na gharama zinazoonekana ndogo kwenye jaribio hujilimbikiza haraka kwa ukubwa wa uzalishaji, zikishawishi timu kushuka kimyakimya hadi mfano dhaifu na kutumaini hakuna anayeona ubora ukiteleza. Kwa shirika kubwa, kuziacha timu zichague mifano na mipaka ya gharama kwa hisia huzalisha ankara za mshangao na ubora usio thabiti. Mabadilishano halisi ni uwezo dhidi ya gharama na ucheleweshaji: mfano mkubwa hufikiria vizuri zaidi kazi ngumu, mdogo ni nafuu na wa haraka kwa rahisi, na kache, uelekezaji, na wigo wa urejeshaji vyote vinasogeza namba. Leta gharama kwa kila kazi iliyotatuliwa, ubora kwa ngazi ya mfano kwenye seti yenu ya tathmini, na mahali uvimbe wa agizo au muktadha unaongeza matumizi ya tokeni. Katika bajeti za mashirika makubwa na serikali, taja nani anaidhinisha uchaguzi wa mfano na dari ya matumizi, kwa sababu mstari wa gharama ambao hakuna anayeumiliki ni ule ambao hakuna anayeudhibiti trafiki inapokuwa mara tatu.

6. **Data nyeti gani inaweza kufikia mfano, data hiyo inaenda wapi, na tunaweza kuthibitisha ilibaki ndani ya mipaka?** Kila agizo, nyaraka iliyorejeshwa, na matokeo ya zana yanaweza kubeba data binafsi au ya siri kuingia kwenye mfano na, na mtoa huduma anayepangisha, kutoka nje ya mzunguko wenu, na uvujaji hapa ni tukio la kisheria au la usalama, si tiketi ya kasoro. Kwa timu kubwa inayounganisha LLM na mifumo ya ndani, hatari inajificha kwenye mabomba: mkusanyiko wa urejeshaji unaojumuisha rekodi ambazo mtumiaji fulani hapaswi kamwe kuziona, au kumbukumbu zinazonasa ingizo ghafi. Mvutano ni uwezo dhidi ya mfiduo, kwa kuwa kuficha na kuweka wigo mkali kunaweza kupunguza makali ya kipengele mnachojaribu kujenga. Leta ramani ya mtiririko wa data ya kinachoingia kwenye muktadha, masharti ya uhifadhi na mafunzo ya mtoa huduma, na jinsi mnavyoficha, kuweka wigo, na kuandika nyanja nyeti. Katika mazingira yanayodhibitiwa na ya umma, funga hili na kanuni za makazi ya data, wajibu wa uhifadhi wa kumbukumbu, na mipaka ya kimkataba juu ya jinsi muuzaji anavyoweza kutumia data yenu, kwa sababu usimamizi usioweza kuuthibitisha ni usimamizi usio nao.

## Mtazamo wa sekta

**Kampuni changa.** Safirisha kipengele kimoja finyu cha LLM kinachogusa thamani yako ya msingi, kilichojengwa kwa mfano unaopangishwa na urejeshaji juu ya maudhui yako mwenyewe, na uweke maagizo kwenye git nyuma ya kiolesura chembamba ili uweze kubadilisha watoa huduma. Endesha faili ndogo ya tathmini ya maswali halisi kabla ya kila badiliko, chuja maandishi yaliyobandikwa na mtumiaji kupunguza sindano ya maagizo, na uweke kikomo kikali cha matumizi ya kila mwezi. Pinga mawakala na kujipangisha: mzunguko usio na mipaka wa kuita zana usioweza kuusimamia ni dhima, si onyesho.

**Biashara ndogo.** Huenda huna mtaalamu wa ML, kwa hiyo nunua vipengele vya LLM vilivyopachikwa kwenye zana unazotumia tayari badala ya kuajiri kujenga. Weka hatari kama swali rahisi: jibu lenye imani lisilo sahihi lingekugharimu mteja wapi, na nani anakagua matokeo kabla hayajatoka. Pendelea wauzaji wanaoonyesha vyanzo vyao, wanakuruhusu kuweka binadamu kwenye mzunguko, na wanafanya AI iwe rahisi kuzima inapokosea.

**Biashara kubwa.** Tatizo ni ukubwa kuvuka timu nyingi: chapisha mifumo ya pamoja ya RAG, vizuizi, na skima za zana, pamoja na zana ya pamoja ya tathmini na rejista ya maagizo ili kila kikundi kiache kugundua upya njia zilezile za kushindwa. Weka bajeti ya gharama ya uelekezaji na mapitio ya binadamu waziwazi, sawazisha tabaka la kiolesura ili mifano ibaki ikibadilishika, na utawala mawakala kati kwa upendeleo mdogo, mizunguko yenye mipaka, na uandishi wa kumbukumbu za ukaguzi. Simamia vipengele vya LLM kama jalada lenye vipimo na vigezo vya kuua, si mtawanyiko wa majaribio.

**Serikali.** Uwazi, kanuni za ununuzi, na uwajibikaji huumba kila uchaguzi. Weka msingi kwa ukali kwenye vyanzo vilivyoidhinishwa vyenye nukuu, kataa urejeshaji unapokosa matokeo, na ukataze mfano kutaja sheria usiyoweza kuinukuu. Weka afisa anayewajibika akipitia matokeo yenye athari, andika ingizo na vyanzo vilivyorejeshwa kwa ukaguzi, endesha seti ya tathmini ya uadui kabla ya kila toleo, na udai ufichuzi wa mipaka ya mfano na masharti ya ushughulikiaji wa data kwenye mkataba.

## Mifano

**Kampuni changa.** Kampuni changa ya zana za wasanidi ya watu watatu iliongeza msaidizi wa gumzo juu ya nyaraka zake ili watumiaji waache kutuma barua pepe za maswali ya msingi. Ilitumia RAG ili kila jibu linukuu ukurasa mahususi wa nyaraka, iliagiza mfano useme "Sina uhakika, hapa ni nani wa kuuliza" urejeshaji unapokosa matokeo, na iliweka maagizo yake kwenye git. Kabla ya kila badiliko ilikimbiza maagizo dhidi ya faili ndogo ya maswali halisi ya watumiaji kunasa regression, na ilichuja maandishi yaliyobandikwa na watumiaji kupunguza sindano ya maagizo. Msaidizi alishughulikia maswali ya kawaida na kupitisha mengine kimyakimya kwenye kikasha cha pamoja cha waanzilishi.

**Biashara kubwa.** Kampuni ya programu ilijenga msaidizi wa msaada wa ndani juu ya nyaraka za bidhaa yake. Ilitumia [RAG](https://en.wikipedia.org/wiki/Retrieval-augmented_generation) ili majibu yanukuu kurasa mahususi za nyaraka, iliagiza mfano useme "Sijui" urejeshaji unaposhindwa, na ilithibitisha kwamba kila chanzo kilichonukuliwa kilikuwepo kweli. Maagizo yalikuwa kwenye udhibiti wa matoleo na yalijaribiwa dhidi ya mfululizo wa maswali halisi ya msaada kwa kila badiliko. Msaidizi alipunguza tiketi za kawaida na kupandisha ngazi chochote cha imani ya chini kwa mawakala wa binadamu, huku vipimo vya mtandaoni vikifuatilia viwango vya utatuzi na marekebisho.

**Serikali.** Wakala wa umma ulisambaza msaidizi wa LLM kuwasaidia wafanyakazi kuandaa majibu kwa maswali ya raia. Msingi ulikuwa mkali: mfano ungeweza kutunga majibu kutoka mwongozo ulioidhinishwa tu pamoja na nukuu, na ulikatazwa kutaja sera ambayo haikuwa kwenye vyanzo vilivyorejeshwa. Afisa anayewajibika alipitia kila rasimu kabla haijatoka. Uchujaji wa ingizo ulilinda dhidi ya sindano ya maagizo kutoka nyaraka zilizowasilishwa na raia, matokeo yaliandikwa kwa ukaguzi, na seti ya tathmini ya maswali ya uadui na ya pembeni iliendeshwa kabla ya kila toleo kuthibitisha mfumo ulikataa kubahatisha mambo ya sheria.

## Kesi ya biashara: sababu, ROI, na TCO

Programu za LLM hutoa ROI kwa kuotomatisha kazi nzito za lugha: kujibu maswali, kufupisha nyaraka, kuandaa maudhui, na kutoa muundo kutoka maandishi yasiyo na muundo. Thamani inaonekana kama tiketi zilizoepukwa, uandishi wa haraka zaidi, mapitio kidogo ya mkono, na uwezo mpya wa kujihudumia. Kwa kuwa mara nyingi hakuna hatua ya mafunzo, muda hadi thamani ya kwanza ni mfupi, kivutio kikubwa.

TCO, hata hivyo, inatawaliwa na gharama endelevu ya uelekezaji, miundombinu ya urejeshaji, mabomba ya tathmini, mifumo ya vizuizi, na mapitio ya binadamu. Gharama za kila mwito hujumlishwa haraka kwa ukubwa, na programu isiyofuatiliwa inaweza kuteleza kuwa tabia isiyo salama au ghali. Gharama ya kutopokea ni kubaki nyuma katika ubora wa huduma na tija ya wafanyakazi. Gharama ya kupokea bila uangalifu ni tukio la hallucination la umma au uvujaji wa data. Weka kesi kwa uongozi kwa kuoanisha lengo madhubuti la tija na mpango madhubuti wa usalama na tathmini, na kwa kupanga bajeti ya vizuizi na usimamizi wa binadamu vinavyoweka thamani ya kudumu.

## Mifumo mibaya na mitego

- **Kuamini matokeo fasaha.** Kuchanganya maandishi yenye imani, yaliyoandikwa vizuri na maandishi sahihi.
- **RAG bila tathmini ya urejeshaji.** Kudhania urejeshaji unafanya kazi na kutokagua kamwe kama unaleta vifungu sahihi.
- **Upofu wa sindano ya maagizo.** Kulisha maudhui yasiyoaminika kwenye maagizo bila ulinzi.
- **Mawakala wasio na mipaka.** Kuruhusu mawakala kuchukua vitendo vyenye athari bila mipaka au idhini ya binadamu.
- **Hakuna zana ya tathmini.** Kubadilisha maagizo na mifano kwa hisia, bila majaribio ya regression.
- **Kuenea kwa maagizo.** Maagizo yaliyotawanyika, yasiyo na matoleo, na yaliyorudiwa kuvuka timu.
- **Uotomatishaji wa kupita kiasi.** Kuwaondoa binadamu kwenye maamuzi yanayobeba uzito wa kisheria au wa usalama.

## Kielelezo cha ukomavu

1. **Kuanzisha.** Kutoa maagizo kwa papo hapo katika miradi iliyotengwa; hakuna msingi, vizuizi, wala tathmini; maagizo yanaishi popote mtu alipoyabandika, na hallucinations zinagunduliwa kwenye uzalishaji.
2. **Kuendeleza.** Baadhi ya timu huongeza RAG na matoleo ya maagizo, uthibitishaji wa msingi wa matokeo, na seti ndogo ya tathmini ya mkono, lakini mazoea yanatofautiana kwa timu na yanategemea mabingwa wa mtu mmoja mmoja badala ya matarajio ya pamoja.
3. **Kusawazisha.** Mifumo iliyoandikwa ya RAG, vizuizi, skima za zana, na matoleo ya maagizo inatekelezwa shirika zima; tathmini ya kiotomatiki ya nje ya mtandao inaendeshwa kwa kila badiliko la agizo au mfano; mtiririko wa dau kubwa hubeba vipimo vya mtandaoni na mapitio ya binadamu.
4. **Kusimamia.** Jalada linapimwa dhidi ya vipimo vya msingi: ukumbukaji wa urejeshaji, viwango vya hallucination na kukataa, ufikiaji wa ulinzi wa sindano, gharama na ucheleweshaji wa kila mwito, na viwango vya kupandisha ngazi na marekebisho vinafuatiliwa kwenye dashibodi; malango ya toleo na vigezo vya kuua vinawaka kwa ushahidi badala ya maoni, na mbio ya regression inazuia badiliko lolote linalosogeza kipimo upande mbaya.
5. **Kuratibu.** Tathmini endelevu ya nje na ya mtandaoni imefungwa na matokeo ya biashara; ulinzi wa sindano, mawakala, na msingi vinatawaliwa na vinaonekana; shirika mara kwa mara linastaafisha, kurekebisha, na kupanua upya vipengele vya LLM, na kubadilisha mifano ubora, gharama, na hatari vinapohama.

## Mawazo ya kujadili

- Mnaamuaje matokeo yapi yanahitaji mapitio ya binadamu kabla ya matumizi?
- Kiwango chenu cha "msingi wa kutosha" ni kipi kabla ya jibu kuonyeshwa kwa watumiaji?
- Mnajilindaje dhidi ya sindano ya maagizo maudhui yasiyoaminika yanapolazimika kuingia kwenye muktadha?
- Wakala anastahili hatari yake ya ziada lini dhidi ya muundo rahisi wa mwito mmoja?
- Mnatathminije ubora wa kiubinafsi kwa ukubwa bila kutegemea kupita kiasi upimaji unaotegemea mfano?
- Mnaweka vipi maagizo yakidumishika na thabiti kuvuka timu nyingi?

## Mambo muhimu ya kukumbuka

- Uaminifu unatokana na uhandisi unaozunguka mfano: muktadha, msingi, vizuizi, na tathmini.
- RAG huweka majibu kwenye vyanzo vinavyoaminika na huwezesha kunukuu na kuthibitisha.
- Chukulia mfano kama kijenzi kisichoaminika; thibitisha matokeo na ubane matumizi ya zana.
- Wape mawakala upendeleo mdogo, mizunguko yenye mipaka, na idhini ya binadamu kwa vitendo vyenye athari.
- Tathmini nje ya mtandao, mtandaoni, na kwa binadamu mfululizo; ndicho kinachofanya mabadiliko kuwa salama.

## Marejeo na usomaji zaidi

- Patrick Lewis et al., *Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks*.
- Jason Wei et al., *Chain-of-Thought Prompting Elicits Reasoning in Large Language Models*.
- OWASP Foundation, *OWASP Top 10 for Large Language Model Applications*.
- Chip Huyen, *AI Engineering: Building Applications with Foundation Models*.
- Anthropic, *Building Effective Agents* (engineering guidance).
- Louis-François Bouchard and Louie Peters, *Building LLMs for Production*.
