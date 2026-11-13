# 7.1 Mkakati wa data na utawala

## Muhtasari na msukumo

Mkakati wa data ni mpango wenu wa makusudi wa kuchukulia data kama mali: jinsi inavyozalishwa, kuelezewa, kumilikiwa, kulindwa, kushirikiwa, na kutumiwa kuunda thamani. [Utawala wa data](https://en.wikipedia.org/wiki/Data_governance) ni mfumo wa uendeshaji unaofanya mkakati kuwa halisi: majukumu, sera, viwango, na vidhibiti vinavyoweka data ya kuaminika na inayozingatia kwa muda. Katika timu ndogo mambo haya mara nyingi hayatamkwi, yakibebwa vichwani mwa wahandisi wachache. Kwa ukubwa wa mashirika makubwa ya wasanidi, mashirika, na mawakala wa serikali, kutokuwa rasmi huko huporomoka. Mamia ya timu huzalisha maelfu ya majedwali. Mifumo kadhaa inadai kushikilia rekodi "halisi" ya mteja. Na hakuna anayeweza kusema kwa imani namba ipi ni sahihi kwenye wasilisho la bodi au ripoti ya umma.

Kwa timu kubwa, gharama ya utawala duni wa data si dhahania. Wadhibiti wanatarajia asili na udhibiti unaoweza kuonyeshwa juu ya data binafsi, ya kifedha, na ya afya chini ya tawala kama [GDPR](https://en.wikipedia.org/wiki/General_Data_Protection_Regulation) (Kanuni ya Jumla ya Ulinzi wa Data ya EU), [HIPAA](https://en.wikipedia.org/wiki/Health_Insurance_Portability_and_Accountability_Act) (Sheria ya Uhamishaji na Uwajibikaji wa Bima ya Afya ya Marekani), na kanuni mahususi za sekta. Mashirika yanakabiliwa na mfiduo wa moja kwa moja wa kifedha kutoka vipimo vilivyoripotiwa vibaya, ukaguzi ulioshindwa, na majukwaa ya data yaliyorudiwa. Mawakala wa serikali hubeba wajibu wa ziada kuhusu uhifadhi wa kumbukumbu, ufikiaji wa uhuru wa taarifa, uwajibikaji wa umma, na kuwatendea raia kwa usawa. Katika kila mazingira haya, data usiyoweza kuiamini ni mbaya kuliko hakuna data, kwa sababu inaendesha maamuzi yenye imani lakini yasiyo sahihi.

Wazo linaloendesha maendeleo kwa ukubwa ni rahisi: chukulia data kama bidhaa. Badala ya data kuwa moshi wa matokeo ya programu, kila seti muhimu ya data ina mmiliki, kiolesura kilichoandikwa, hakikisho za ubora, na watumiaji wanaochukuliwa kama wateja. Sura hii inashughulikia mtazamo huo wa bidhaa kando ya nidhamu za kawaida za utawala: usimamizi, kuorodhesha, [usimamizi wa data kuu](https://en.wikipedia.org/wiki/Master_data_management), na ubora. Pia inashughulikia chaguo za kishirika zinazoamua mfano upi unafaa timu yenu: [data mesh](https://en.wikipedia.org/wiki/Data_mesh) (data iliyogatuliwa, inayomilikiwa na maeneo, ikichapishwa kama bidhaa), data lakehouse (usimamizi na utawala wa mtindo wa ghala uliowekwa juu ya [ziwa la data](https://en.wikipedia.org/wiki/Data_lake) linalonyumbulika), na [ghala la data](https://en.wikipedia.org/wiki/Data_warehouse) (hifadhi ya kati iliyotawaliwa ya data iliyoumbwa, tayari kwa maswali).

*Angalia pia:* sura ya 4.5 (faragha na ulinzi wa data), sura ya 7.2 (uhandisi wa data), na sura ya 4.6 (uzingatiaji na utawala).

## Kanuni kuu

- Data ni mali ya kudumu yenye wamiliki, si zao la kutupwa la programu.
- Kila seti muhimu ya data ina mmiliki aliyetajwa anayewajibika na mkataba ulioandikwa.
- Utawala huwezesha matumizi ya kuaminika; si lango la kiukiritimba linalosema hapana tu.
- Kunapaswa kuwa na chanzo kimoja chenye mamlaka kwa kila chombo muhimu cha biashara.
- Ubora, faragha, na asili vimeundwa ndani, si kukaguliwa baadaye.
- Watumiaji wa data ni wateja ambao mahitaji yao yanaumba bidhaa.
- Sera zinasimbwa na kutekelezwa kiotomatiki popote iwezekanavyo, si kuachwa kwa nia njema.
- Umiliki ulioshirikishwa hupanuka vizuri kuliko timu moja ya kati shirika linapokua.

## Mapendekezo

### Chukulia data kama bidhaa

Mpe kila seti muhimu ya data mmiliki wa bidhaa anayewajibika kwa ufaao wake kwa matumizi. Bidhaa ya data ina jina, skima iliyoandikwa, maelezo ya maana na asili yake, mzunguko wa kusasisha ulioainishwa, na matarajio ya ubora yaliyochapishwa. Watumiaji wenu wanapaswa kuweza kuigundua, kuielewa, na kuitegemea bila kuuliza timu ya uzalishaji swali hata moja. Tumia nidhamu ileile unayotumia kwa API za programu: matoleo, notisi za kuondolewa, kumbukumbu za mabadiliko, na upatanifu wa nyuma.

### Anzisha mikataba ya data na SLA

Mkataba wa data ni makubaliano wazi, yanayoweza kukaguliwa na mashine kati ya mzalishaji na watumiaji wake. Unashughulikia skima, semantiki, usafi, kiasi, na mabadiliko yanayoruhusiwa. Tekeleza mikataba kwenye bomba ili badiliko la juu ya mkondo linalovunja lishindwe haraka chanzoni, badala ya kuharibu kimyakimya ripoti za chini ya mkondo wiki baadaye. Oanisha mikataba na makubaliano ya kiwango cha huduma na malengo. Kwa mfano, "jedwali la mteja linasasishwa kufikia 06:00 kila siku, kwa asilimia 99.5 ya siku, na funguo za biashara zisizo na thamani chini ya asilimia 0.1." Zichapishe hizi, na utoe tahadhari ukiukaji unapotokea.

### Jenga usimamizi na mfano wa uendeshaji wa utawala

Tenganisha uwajibikaji na utekelezaji. Wamiliki wa data (mara nyingi viongozi wa biashara) wanawajibika kwa eneo. Wasimamizi wa data (wataalamu wa masuala) wanadumisha fasili, kutatua masuala ya ubora, na kuidhinisha ufikiaji. Baraza jepesi la utawala wa data huweka viwango vinavyovuka maeneo na kutatua migogoro. Weka mfano ukiwa umeshirikishwa: timu ya kati ya kuwezesha inatoa zana, viwango, na kufundisha, wakati timu za maeneo zinamiliki data yao. Hii inaepuka kizuizi cha kuweka kila kitu kati na machafuko ya kutokuwa na utawala kabisa.

### Wekeza kwenye orodha ya data na asili

Orodha inayotafutika ndiyo mlango wa mbele wa eneo lenu la data. Inapaswa kushikilia faharasa za biashara, skima za kiufundi, umiliki, uainishaji wa unyeti, alama za ubora, na asili ya mwanzo hadi mwisho kutoka mfumo chanzo kupitia mabadiliko hadi dashibodi. Otomatisha uvunaji wa metadata badala ya kutegemea nyaraka za mkono, zinazooza haraka. Asili ni muhimu kwa uchambuzi wa athari, jibu la tukio, ukaguzi, na maombi ya udhibiti kama ufikiaji na kufuta kwa mhusika wa data.

### Usimamizi wa data kuu na chanzo kimoja cha ukweli

Kwa vyombo vya msingi (mteja, raia, bidhaa, msambazaji, mfanyakazi), tumia usimamizi wa data kuu kupatanisha nakala na rekodi zinazopingana kuwa rekodi moja ya dhahabu. Chagua usanifu (rejista, kuunganisha, kuishi pamoja, au wa kati) kulingana na jinsi kitovu kinavyohitaji kuwa na mamlaka. Fafanua kanuni za kulinganisha na kuokoka waziwazi, na uzifanye zikaguliwe. [Chanzo kimoja cha ukweli](https://en.wikipedia.org/wiki/Single_source_of_truth) huzuia kushindwa kwa kawaida ambapo fedha, mauzo, na operesheni kila moja huripoti mapato tofauti.

### Pima ubora wa data kuvuka vipimo

Simamia ubora kwa vipimo vilivyotajwa: usahihi, ukamilifu, uthabiti, wakati, uhalali, na upekee. Weka vifaa vya kupima kwenye mabomba kwa majaribio ya kiotomatiki na uonekanaji endelevu wa data (usafi, kiasi, kuteleza kwa skima, na ukaguzi wa usambazaji), ili unase hitilafu kabla watumiaji hawajaathirika. Chukulia matukio ya data kama hitilafu za uzalishaji, kwa ugunduzi, upangaji, uchambuzi wa chanzo, na tathmini za baada ya tukio.

### Ainisha, linda, na dhibiti ufikiaji

Ainisha data kwa unyeti, na utumie vidhibiti sawia: usimbaji fiche, kuficha, kutoa tokeni, usalama wa kiwango cha safu na safu wima, na ufikiaji wa upendeleo mdogo unaopitiwa mara kwa mara. Weka ratiba ya uhifadhi na kufuta inayotimiza mahitaji ya kupunguza na sheria ya uhifadhi wa kumbukumbu. Katika mazingira ya serikali, patanisha wajibu wa uwazi na ulinzi wa faragha kwa makusudi, badala ya kesi kwa kesi.

## Mabadilishano: faida na hasara

| Mbinu | Faida | Hasara | Inafaa zaidi |
|---|---|---|---|
| Timu ya kati ya utawala | Viwango thabiti, uwajibikaji wazi | Kizuizi, imetenganishwa na maeneo | Mashirika madogo au yanayodhibitiwa sana |
| Utawala ulioshirikishwa | Hupanuka, utaalamu wa eneo, umiliki | Inahitaji zana imara na utamaduni | Mashirika makubwa yenye maeneo mengi |
| Ghala la data | Lililokomaa, lililotawaliwa, SQL yenye utendaji | Gumu, ghali kwa data isiyo na muundo | Mizigo thabiti inayotegemea BI |
| Data lakehouse | Linalonyumbulika, lililounganishwa, linashughulikia aina zote za data | Zana changa, juhudi ya utawala | Uchanganuzi mchanganyiko na ML |
| Data mesh | Umiliki wa eneo, hupanuka kishirika | Kiwango cha juu cha ukomavu, gharama ya uratibu | Mashirika makubwa sana, yaliyogatuliwa |

Utawala daima hubadilisha kasi dhidi ya uaminifu. Utawala mwepesi unaziruhusu timu kusonga haraka, hadi ukaguzi, uvunjaji, au kuripoti vibaya kwa aibu kulazimishe hesabu ghali. Utawala mzito hulinda uaminifu lakini unaweza kusonga majaribio na kusukuma timu kuelekea mifumo ya kivuli. Jibu la kudumu ni kusimba utawala kama vizuizi vya kiotomatiki, vya kujihudumia, ili njia inayozingatia pia iwe njia rahisi. Kiusanifu, ghala hupendelea urahisi uliotawaliwa, mesh hupendelea ukubwa wa kishirika, na lakehouses hugawanya tofauti. Chaguo sahihi linafuata muundo wa shirika lenu kuliko kigezo chochote cha kiufundi.

## Maswali ya kujadili na timu yako

1. **Usanifu upi wa data (ghala, lakehouse, au mesh) unafaa muundo wa shirika lenu kweli, na je, mko waaminifu kuhusu kiwango cha ukomavu ambacho kila mmoja unadai?** Jedwali la mabadilishano linaonyesha chaguo hili linafuata muundo wa shirika, si vigezo: ghala hutuza mizigo thabiti inayotegemea BI, lakehouse hushughulikia uchanganuzi na ML mchanganyiko, na mesh hupanuka kuvuka maeneo mengi huru lakini inadai ukomavu wa juu na zana imara. Kwa shirika kubwa au wakala wa serikali wenye maeneo kadhaa, kuruka kwenda mesh kabla ya kuwa na majukwaa ya kujihudumia na utamaduni wa utawala huzalisha machafuko yaliyovaa ugatuzi. Leta ishara madhubuti: maeneo mangapi yanazalisha data, kama timu za kati tayari ni kizuizi, na kama timu za maeneo zina ujuzi na motisha ya kumiliki bidhaa. Kama hamna zana zilizoshirikishwa leo, jibu la uaminifu linaweza kuwa ghala au lakehouse iliyotawaliwa sasa na mesh baadaye. Chagua mfano ambao watu wenu wanaweza kuuendesha kweli, kisha wekeza kwenye ukomavu ambao mfano unaofuata unahitaji.

2. **Mnaweza kuheshimu ombi la kufuta mwanzo hadi mwisho leo, na je, asili yenu inathibitisha mahali nakala zote za rekodi binafsi zilipoenda?** Chini ya GDPR na tawala zinazofanana, ombi la mhusika wa data la kufuta au kufikia ni wajibu wa kisheria wenye tarehe za mwisho kali, na kunakili data kwa upana bila asili huufanya kutowezekana kutimiza. Timu kubwa mara kwa mara husambaza data kwenye maghala madogo, nakala za usafirishaji, kache, na lahajedwali, kwa hiyo swali halisi ni kama mnaweza kufuatilia na kufikia kila nakala, si kama mnaweza kufuta ya asili. Leta ushahidi: chagua mteja au raia mmoja halisi na ujaribu kuorodhesha kila mahali data yake inapoishi. Msipoweza, pengo hilo ni hatari ya uzingatiaji na tatizo la eneo la mlipuko la uvunjaji. Jibu linapaswa kuendesha uwekezaji kwenye asili ya kiotomatiki na vidhibiti vikali zaidi juu ya kunakili kusikodhibitiwa, kwa sababu njia inayozingatia lazima ijengwe kabla ombi halijafika.

3. **Utawala wenu ni njia rahisi au lango ambalo watu wanalizunguka, na mifumo ya kivuli inayothibitisha hilo iko wapi?** Jibu la kudumu la sura hii ni kusimba utawala kama vizuizi vya kiotomatiki, vya kujihudumia ili njia inayozingatia pia iwe ya haraka zaidi, kwa sababu utawala mzito wa mkono husukuma timu kuelekea lahajedwali za kivuli na nakala zisizotawaliwa. Kwa mashirika na mawakala, mifumo ya kivuli ndipo uvunjaji, namba mbaya, na ukaguzi ulioshindwa unapozaliwa, hasa kwa sababu hakuna anayeitazama. Leta orodha madhubuti: timu zipi zinaweka nakala zao, ripoti zipi zinapita orodha, na wapi watu wanasema mchakato rasmi ni wa polepole mno. Kila mfumo wa kivuli ni ishara kwamba njia iliyotawaliwa inagharimu zaidi ya njia mbadala. Rekebisha msuguano badala ya kutoa sera nyingine, ili kutumia data iliyothibitishwa na mikataba iwe rahisi kweli kuliko kuizunguka.

4. **Chombo kipi cha biashara kinahitaji zaidi chanzo kimoja chenye mamlaka, na nani kwa jina anawajibika kwa rekodi yake ya dhahabu leo?** Usimamizi wa data kuu upo kuzuia fedha, mauzo, na operesheni kila moja kuripoti mteja tofauti au takwimu tofauti ya mapato, na kwa ukubwa kutokuwepo kwa chanzo kimoja chenye mamlaka hugeuza kila namba ya kuvuka maeneo kuwa mabishano. Mazingatio yanayoshindana ni jinsi kitovu kinavyopaswa kuwa na mamlaka (rejista, kuunganisha, kuishi pamoja, au cha kati kabisa) na mantiki ya kulinganisha na kuokoka mko tayari kuijenga na kuikagua kiasi gani, kwa kuwa kitovu kizito kinagharimu zaidi lakini kinatatua migogoro zaidi. Leta vyombo vinavyoonekana kwenye ripoti nyingi zaidi (mteja, raia, bidhaa, msambazaji, mfanyakazi), hesabu ya mifumo mingapi inadai kushikilia rekodi halisi ya kila moja, na kanuni za kulinganisha mnazotumia leo, kama zipo. Kwa benki au wakala wa taifa, taja mmiliki anayewajibika na kanuni za kuokoka waziwazi, kwa sababu mdhibiti anayefuatilia takwimu kutoka ripoti ya umma hadi chanzo atauliza nani aliamua nakala ipi ishinde, na "hakuna" si jibu linaloweza kuokoka ukaguzi.

5. **Mnajuaje seti muhimu ya data inafaa kwa matumizi kabla mtumiaji hajagundua imevunjika?** Katika maeneo yasiyokomaa, ubora hupatikana na mchambuzi ambaye dashibodi yake inavunjika au mtendaji ambaye namba yake ya bodi si sahihi, ambayo ndiyo nukta ghali zaidi ya ugunduzi. Mvutano ni kati ya gharama ya kuweka vifaa vya kupima ubora (majaribio, ukaguzi wa usafi na kiasi, ufuatiliaji wa usambazaji na kuteleza kwa skima kuvuka vipimo vilivyotajwa kama usahihi, ukamilifu, na uhalali) na gharama ya matukio mnayozuia, na timu mara kwa mara huwekeza kidogo kwa sababu kushindwa kunabaki kusikoonekana hadi kugeuka maafa. Leta matukio matatu ya mwisho ya data, jinsi yalivyogunduliwa, na yalikimbia kwa muda gani kabla ya mtu kuona, pamoja na SLA za ubora mnazochapisha na kutoa tahadhari kweli leo. Kwa kuripoti kwa mashirika na serikali, funga kila bidhaa muhimu ya data na vizingiti wazi vya ubora na uchukulie ukiukaji kama hitilafu ya uzalishaji yenye upangaji na tathmini ya baada ya tukio, kwa sababu takwimu isiyo sahihi kwenye faili ya udhibiti au takwimu ya umma hubeba gharama ya kisheria na ya sifa inayozidi sana ankara ya ufuatiliaji.

6. **Utawala wenu umeshirikishwa kweli na umiliki wa maeneo, au ni timu ya kati inayowajibishwa kwa data isiyoielewa?** Sura inahoji kwamba umiliki ulioshirikishwa na uwezeshaji wa kati hupanuka pale mpangilio wa kati kabisa unapokuwa kizuizi na ugatuzi kamili unashuka kuwa machafuko, hata hivyo mashirika mengi hudai ushirikishaji huku timu ndogo ya kati ikibaki kwa jina inawajibika kwa maelfu ya majedwali isiyo na maarifa ya eneo juu yake. Mvuto unaoshindana ni halisi: timu za kati hutoa uthabiti na mtu mmoja wa kuuliza, wakati umiliki wa eneo hutoa utaalamu na uwajibikaji lakini unadai wamiliki wa biashara wakubali wajibu ambao huenda hawautaki. Leta ramani ya uaminifu ya nani anawajibika dhidi ya nani anadumisha fasili na kutatua masuala ya ubora kweli kwa maeneo yenu makuu, na kama wasimamizi wana mamlaka na muda ambao jukumu linahitaji. Katika shirika kubwa au wakala, hakikisha umiliki unakaa na watu wanaoshikilia maarifa ya eneo na mamlaka ya kusema hapana, kwa sababu utawala uliotolewa kwa timu ya kati bila mamlaka huzalisha sera ambazo hakuna anayezifuata na baraza lisilotatua chochote.

## Mtazamo wa sekta

**Kampuni changa.** Kasi na kunusurika vinashinda mchakato. Taja mmiliki mmoja kwa kila seti ya msingi ya data na ufanye hifadhi moja iwe chanzo kimoja cha ukweli kwa vyombo kama "mteja hai," na uruke orodha, mabaraza, na mesh kabisa. Mkataba wa ukurasa mmoja kwa majedwali yako machache muhimu (skima, wakati wa kusasisha, matarajio moja ya ubora) humaliza mabishano ya "namba ya nani ni sahihi" ndani ya alasiri. Egemea utawala uliojengwa tayari kwenye ghala lako badala ya kuajiri kazi usiyoweza kuimudu.

**Biashara ndogo.** Bila mtaalamu maalumu wa data na bajeti finyu, chukulia utawala kama usafi wa data badala ya mradi wa jukwaa: jua data binafsi gani unashikilia, inaishi wapi, na nani anaruhusiwa kuigusa. Pendelea ghala au zana ya BI inayosimamiwa inayotoa asili, udhibiti wa ufikiaji, na uhifadhi tayari, ili ununue utawala uliopachikwa kwenye zana unazoendesha tayari badala ya kuujenga. Hifadhi bomba lolote maalumu kwa seti moja ya data inayoendesha biashara kweli.

**Biashara kubwa.** Kwa ukubwa kuvuka timu nyingi, kazi ni umiliki ulioshirikishwa na uwezeshaji wa kati: orodha ya pamoja yenye asili ya kiotomatiki, mikataba ya data inayotekelezwa, data kuu kwa vyombo vya msingi, na SLA za ubora zinazopimwa dhidi ya vipimo vya msingi. Simba utawala kama vizuizi vya kujihudumia ili njia inayozingatia pia iwe ya haraka, na simamia data kama jalada la bidhaa lenye wamiliki waliotajwa. Hivyo wakaguzi wanaweza kufuatilia takwimu yoyote kutoka ripoti hadi chanzo, na vikundi vinaacha kubuni upya mabomba na fasili zilezile.

**Serikali.** Kanuni za ununuzi, uwazi, na uwajibikaji wa umma huumba kila uchaguzi. Chukulia viashiria vilivyochapishwa kama bidhaa za data zenye mbinu iliyoandikwa, matoleo yaliyowekewa matoleo, na malango ya ubora, na upatanishe wajibu wa uhuru wa taarifa na data wazi na faragha na kupunguza kwa makusudi badala ya kesi kwa kesi. Dai uhamishaji wa data na ufichuzi wa asili kwenye mikataba ya wauzaji kuepuka kufungwa, weka ratiba ya uhifadhi na kufuta inayoweza kutetewa, na uache baraza la usimamizi lishikilie fasili za pamoja ili "kaya" au "ukosefu wa ajira" vimaanishe kitu kilekile kuvuka kila idara.

## Mifano

**Kampuni changa.** Kampuni changa ya SaaS ya hatua ya mbegu iligundua kwamba lahajedwali yake ya bili, zana yake ya mauzo, na hifadhidata yake ya bidhaa kila moja iliripoti hesabu tofauti ya wateja, na hakuna aliyeweza kusema ipi ni sahihi kwa taarifa ya wawekezaji. Timu ya watu wanne ilitaja mmiliki mmoja kwa kila seti ya msingi ya data, ikafanya ghala kuwa chanzo kimoja cha "mteja hai," na kuandika mkataba wa ukurasa mmoja ukielezea skima na wakati wa kusasisha wa kila siku. Ilichukua alasiri moja, na ilimaliza mabishano ya kila wiki kuhusu namba ya kuamini.

**Biashara kubwa.** Benki ya kimataifa iliunganisha rekodi nyingi zinazopingana za wateja kuvuka vitengo vyake vya rejareja, mikopo, na utajiri kuwa kitovu cha usimamizi wa data kuu chenye kanuni za kuokoka na rekodi ya dhahabu. Kila eneo lilichapisha bidhaa za data zenye mikataba na SLA za usafi, zilizoonyeshwa kwenye orodha ya kati yenye asili. Muda wa kuripoti kwa udhibiti ulishuka sana, kwa sababu wakaguzi sasa walifuatilia takwimu yoyote kutoka ripoti hadi chanzo. Benki pia ilistaafisha majukwaa kadhaa yasiyohitajika ya kuripoti.

**Serikali.** Wakala wa kitaifa wa takwimu unachukulia viashiria vyake vilivyochapishwa kama bidhaa za data, vyenye mbinu iliyoandikwa, matoleo yaliyowekewa matoleo, na malango makali ya ubora. Baraza la usimamizi hupatanisha fasili kuvuka idara, ili "ukosefu wa ajira" au "kaya" vimaanishe kitu kilekile kila mahali. Uainishaji na ufikiaji unaodhibitiwa hulinda usiri wa waliojibu, wakati orodha ya umma inaunga mkono wajibu wa uwazi na uhuru wa taarifa.

## Kesi ya biashara: sababu, ROI, na TCO

Motisha ya utawala wa data ni kupunguza hatari na kuunda thamani kwa takriban uwiano sawa. Upande wa hatari, gharama zilizoepukwa zinajumuisha faini za udhibiti, dhima ya uvunjaji, ukaguzi ulioshindwa, na uharibifu wa sifa wa kuchapisha namba mbaya. Upande wa thamani, data ya kuaminika, inayogundulika huharakisha kila juhudi ya chini ya mkondo ya uchanganuzi na kujifunza kwa mashine, hupunguza mabomba yaliyorudiwa, na hufupisha muda kutoka swali hadi jibu.

Gharama ya kupokea ni halisi: zana za orodha na ubora, muda wa wamiliki na wasimamizi, na mabadiliko ya kishirika ili umiliki ushikamane. Pima TCO (jumla ya gharama ya umiliki) dhidi ya gharama ya kutopokea, ambayo kwa kawaida ni kubwa zaidi, imejificha tu. Isipopimwa, gharama hiyo inaonekana kama wachambuzi wakitumia muda wao mwingi kutafuta na kusafisha data, timu zikijenga upya mabomba yaleyale, na watendaji wakifanya maamuzi kwa takwimu ambazo hakuna anayeweza kuzitetea. Weka kesi kwa uongozi kwa lugha yao: utawala hugeuza data kutoka dhima yenye hasara isiyo na mipaka kuwa mali yenye faida zinazojilimbikiza, na ni sharti la AI ya kuaminika. Anza pale maumivu na mfiduo wa udhibiti ni mkubwa zaidi, ili uweze kuonyesha thamani haraka.

## Mifumo mibaya na mitego

- Utawala kwa kamati bila uotomatishaji, ukizalisha sera ambazo hakuna anayezifuata.
- Kuorodhesha kila kitu mara moja badala ya seti za data zinazojalisha kweli.
- Miradi ya data kuu inayochemsha bahari na kutosafirisha rekodi ya dhahabu kamwe.
- Kuchukulia [ubora wa data](https://en.wikipedia.org/wiki/Data_quality) kama usafishaji wa mara moja badala ya uonekanaji endelevu.
- Umiliki uliotolewa kwa timu ya kati isiyo na maarifa ya eneo wala mamlaka.
- Mikataba iliyoandikwa kwenye wiki lakini isiyotekelezwa kwenye mabomba.
- Kunakili data kwa upana bila asili, kufanya maombi ya kufuta kutowezekana kuheshimu.
- Kununua zana na kuiita mkakati; zana bila mfano wa uendeshaji hushindwa.

## Kielelezo cha ukomavu

1. Kuanzisha: Data haijaandikwa wala kumilikiwa, inashughulikiwa papo hapo na kwa kuitikia. Fasili zinapingana kuvuka timu. Ubora unagunduliwa na watumiaji ripoti zinapovunjika. Hakuna orodha wala asili.
2. Kuendeleza: Mazoea ya msingi yanaonekana lakini hayana uthabiti kuvuka timu. Baadhi ya seti za data zina wamiliki na nyaraka, na orodha pungufu ipo. Ukaguzi wa ubora ni wa mkono na wa kuitikia. Sera ya utawala imeandikwa lakini inatekelezwa kwa unyonge na bila usawa.
3. Kusawazisha: Umiliki, mikataba, na SLA vimeandikwa na kutekelezwa shirika zima. Bidhaa muhimu za data zina wamiliki waliotajwa; orodha yenye asili ya kiotomatiki inafunika maeneo muhimu; data kuu ipo kwa vyombo vya msingi; utawala umeshirikishwa na uwezeshaji wa kati na unatumika kwa uthabiti badala ya timu kwa timu.
4. Kusimamia: Eneo linapimwa na kudhibitiwa dhidi ya vipimo vya msingi. Vipimo vya ubora (usahihi, ukamilifu, wakati, uhalali, upekee) vinafuatiliwa dhidi ya malengo ya SLA yaliyochapishwa; viwango vya ukiukaji wa mikataba, ufikiaji wa asili na orodha, usafi, na muda wa kuheshimu ombi la kufuta vinaripotiwa kwenye dashibodi; uonekanaji unatoa tahadhari ya kuteleza kwa skima na hitilafu za kiasi; matukio hupata upangaji, uchambuzi wa chanzo, na tathmini za baada ya tukio; maamuzi ya ufikiaji na kwenda/kutokwenda yanategemea vipimo dhidi ya vipimo vya msingi, si maoni.
5. Kuratibu: Utawala unaboreshwa mfululizo na kuunganishwa kuvuka shirika. Data-kama-bidhaa ni kawaida kuvuka maeneo; mikataba inatekelezwa kiotomatiki na mabadiliko yanayovunja yanashindwa haraka; vizuizi vya kujihudumia vinasimba sera; ubora na asili vinalisha usimamizi wa hatari wa mbele; fasili zinaaminiwa shirika zima na zinaunga mkono kuripoti kunakodhibitiwa na AI. Shirika mara kwa mara husawazisha upya umiliki, kustaafisha majukwaa yasiyohitajika, na kurekebisha utawala biashara na kanuni zinapohama.

## Mawazo ya kujadili

- Chombo chenu cha biashara kipi kinahitaji haraka zaidi chanzo kimoja cha ukweli, na kwa nini kimegawanyika leo?
- Mikataba ya data iliyotekelezwa ingezuia wapi tukio la hivi karibuni?
- Shirika lenu limepangwa kwa umiliki ulioshirikishwa, au kuweka kati kungefaa zaidi sasa hivi?
- Mnapatanishaje wajibu wa uwazi wa serikali na faragha na kupunguza data?
- Asilimia gani ya muda wa wachambuzi wenu inatumika kutafuta na kusafisha data, na kuipunguza kwa nusu kungekuwa na thamani gani?
- Nani anawajibika, kwa jina, kwa seti yenu muhimu zaidi ya data, na je, anajua?

## Mambo muhimu ya kukumbuka

- Chukulia data kama bidhaa yenye wamiliki, mikataba, na SLA, si moshi wa programu.
- Utawala ulioshirikishwa wenye uwezeshaji wa kati hupanuka vizuri kuliko kuweka kati kabisa.
- Orodha yenye asili ya kiotomatiki ndio mlango wa mbele wa eneo la data linaloaminika.
- Anzisha chanzo kimoja cha ukweli kwa vyombo vya msingi kupitia usimamizi wa data kuu.
- Simamia ubora mfululizo kuvuka vipimo vilivyotajwa kwa uonekanaji na jibu la tukio.
- Simba utawala kama vizuizi vya kiotomatiki ili njia inayozingatia iwe njia rahisi.
- Chagua ghala, lakehouse, au mesh kufaa shirika lenu, si ushabiki.

## Marejeo na usomaji zaidi

- DAMA International, "DAMA-DMBOK: Data Management Body of Knowledge."
- Zhamak Dehghani, "Data Mesh: Delivering Data-Driven Value at Scale."
- Ralph Kimball and Margy Ross, "The Data Warehouse Toolkit."
- Piethein Strengholt, "Data Management at Scale."
- David Loshin, "Master Data Management."
- Chad Sanderson and colleagues, writings on data contracts.
- ISO/IEC 38505, "Governance of data."
- ISO 8000, "Data quality" standard series.
