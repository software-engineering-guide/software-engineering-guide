# 2.16 Uhandisi wa utendaji

## Muhtasari na msukumo

Uhandisi wa utendaji ni ufundi wa kufanya msimbo uwe wa haraka vya kutosha, kwa makusudi, ukitumia upimaji badala ya hisia. Sura hii inafanya kazi katika ngazi ya msimbo na vipengele: kazi, vitanzi, miundo ya data, hoja, ugawaji wa kumbukumbu, na jinsi huduma moja inavyotumia muda wake. Ni mwenza wa sura ya 3.5, inayoshughulikia utendaji katika ngazi ya mfumo (kupanua kwa upana, kusawazisha mzigo, uwezo, na ustahimilivu). Mfumo unapokuwa polepole, sura ya 3.5 inauliza unahitaji mashine ngapi; sura hii inauliza kwa nini mashine moja inafanya kazi nyingi hivyo tangu mwanzo. Kwa kawaida utahitaji zote mbili, na mtazamo wa ngazi ya msimbo ndipo gharama na ucheleweshaji mwingi wa kushangaza hujificha kweli.

Kwa timu kubwa, nidhamu hii ni muhimu kwa sababu utendaji huoza kimyakimya. Hakuna commit moja inayofanya huduma iwe polepole, lakini elfu ndogo, kila moja ikiongeza wito wa hifadhidata au kitanzi kisicho na kikomo, zitafanya hivyo. Bila mbinu ya pamoja ya kupima, kupanga bajeti, na kudhibiti utendaji, unagundua uozo tu mteja analalamika au uzinduzi unapoyeyuka. Mbinu hugeuza utendaji kutoka kuzima moto kishujaa kuwa sifa ya kawaida unayoilinda.

Kwa mashirika makubwa, utendaji ni fedha: msimbo wa haraka zaidi unamaanisha mashine chache, bili ndogo za wingu, na uwezo wa kutimiza [makubaliano ya kiwango cha huduma](https://en.wikipedia.org/wiki/Service-level_agreement) (SLA) kuhusu ucheleweshaji bila kutoa rasilimali nyingi kupita kiasi. Kwa serikali, utendaji ni ufikiaji: ukurasa unaopakia kwenye simu ya zamani kupitia muunganisho dhaifu wa simu ndio tofauti kati ya raia kukamilisha dai la manufaa na kukata tamaa. Mifumo ya umma pia inahitaji ushahidi wa vipimo vya utendaji unaoweza kuzalishwa upya, kwa sababu vyombo vya ununuzi na usimamizi vitakuomba uthibitishe namba, si kuzitamka tu.

## Kanuni kuu

- **Pima kabla ya kuboresha.** Kizuizi karibu kamwe hakipo unapokisia. Chunguza utendaji, kisha utende.
- **Epuka uboreshaji wa mapema.** Onyo la Donald Knuth linashikilia: kuboresha msimbo usiojalisha kunagharimu uwazi na hakununui kitu.
- **Fafanua "haraka vya kutosha" kama namba.** Bajeti ya utendaji yenye lengo na asilimia hugeuza maoni kuwa kufaulu au kufeli.
- **Wastani husema uongo; asilimia husema ukweli.** Mkia (p99) ndio watumiaji wanaohisi, si wastani.
- **Ushindi wa algoriti hushinda urekebishaji mdogo.** Daraja bora la ugumu hushinda ujanja wowote wa kigezo kisichobadilika.
- **Ucheleweshaji na uwezo wa kupitisha ni malengo tofauti.** Kuboresha kimoja kunaweza kuzorotesha kingine; jua ni kipi unanunua.
- **Pima kwa uaminifu au usipime kabisa.** Kupasha moto, tofauti, na mzigo wa kazi unaowakilisha hutenganisha namba halisi na hadithi.
- **Dhibiti utendaji kwenye CI, uuangalie kwenye uzalishaji.** Kurudi nyuma kunakonaswa kabla ya kuunganisha ni nafuu; kunakonaswa na watumiaji, ghali.

## Mapendekezo

### Pima kwanza, na uchunguze utendaji kabla ya kugusa mstari

Kanuni ya zamani zaidi katika uwanja huu ndiyo inayopuuzwa zaidi: tafuta kizuizi kabla ya kuboresha. Fikia [kichunguzi cha utendaji](https://en.wikipedia.org/wiki/Profiling_(computer_programming)), zana inayochukua sampuli au kufunga vifaa vya kupima kwenye programu inayoendesha ili kuonyesha inatumia wapi muda na kumbukumbu. Chunguza CPU (kazi zipi zinachoma mizunguko), kumbukumbu na ugawaji (kinachogawiwa na mara ngapi, kwa kuwa msukosuko wa ugawaji huendesha vituo vya ukusanyaji wa taka), na I/O (muda unaotumika kusubiri diski, mtandao, au hifadhidata). [Grafu ya mwali](https://en.wikipedia.org/wiki/Flame_graph), taswira iliyorundikwa ambapo kila kisanduku ni kazi na upana wake ni muda uliotumika, hufanya gharama kuu ionekane kwa mtazamo: tafuta visanduku vipana zaidi, si safu zenye kina zaidi. Boresha gharama kubwa zaidi kwanza, pima tena, na usimame ukifikia bajeti. Hili linaunganishwa na mazoea ya uonekanaji ya sura ya 9.2, kwa sababu uchunguzi wa uzalishaji unashinda kila makisio yaliyofanywa kutoka kompyuta mpakato.

Jilinde dhidi ya kosa kinyume pia. Mstari kamili wa Knuth ni kwamba uboreshaji wa mapema ndio mzizi wa uovu mwingi, na alimaanisha kuhusu uzembe mdogo unaokushawishi kutoa dhabihu msimbo unaosomeka kwa kasi ya kufikirika. Andika toleo wazi kwanza, pima, na uboreshe tu msimbo ambao kichunguzi kinaushtaki.

### Fafanua "haraka vya kutosha" kwa bajeti za utendaji

Kasi si fadhila kwa jumla; ni lengo unalotimiza au unalokosa. Weka **bajeti ya utendaji**: kikomo madhubuti kama "ucheleweshaji wa p99 wa malipo chini ya ms 300" au "mwisho huu unagawa chini ya MB 1 kwa kila ombi." Kifunge na kitu ambacho watumiaji au biashara wanahisi, na kieleze kama **asilimia**, si wastani, kwa sababu wastani huficha mkia wa polepole ambapo watumiaji halisi wanaishi. Ikiwa 1% ya maombi huchukua sekunde 5, wastani wako unaweza kuonekana sawa huku sehemu muhimu ya wateja ikiteseka. Bajeti hutoa timu ufafanuzi wa pamoja usioweza kubishaniwa wa kukamilika na mstari ambao kurudi nyuma kunauvuka waziwazi.

### Fikia ufanisi wa algoriti kabla ya uboreshaji mdogo

Ushindi mkubwa zaidi, wa bei nafuu zaidi hutoka kwenye [ufanisi wa algoriti](https://en.wikipedia.org/wiki/Algorithmic_efficiency), jinsi kazi inavyokua ingizo linapokua, inayoelezwa kwa [nukuu ya Big O](https://en.wikipedia.org/wiki/Big_O_notation) (njia ya kuainisha kasi ya ukuaji, kwa hiyo upangaji wa O(n log n) hupanuka vizuri zaidi sana kuliko wa O(n kwa mraba)). Kitanzi cha ndani-ndani kisichoonekana kwa vipengele kumi kinakuwa maafa kwa elfu kumi. Kabla hujarekebisha kwa mkono kazi moto, uliza kama inafanya kazi nyingi kupita kiasi kwa msingi: hoja ya N+1 ya bahati mbaya, uchanganuzi wa mstari unaopaswa kuwa utafutaji wa hashi, au kazi inayojirudia inayoweza kukumbukwa. Hili linaunganishwa na misingi ya algoriti katika sura ya 2.13. Hakuna kiasi cha urekebishaji wa kigezo kisichobadilika kinachookoa daraja la ugumu lisilo sahihi.

### Tofautisha ucheleweshaji na uwezo wa kupitisha, na uheshimu mkia

**Ucheleweshaji** ni muda ambao operesheni moja inachukua; **uwezo wa kupitisha** ni operesheni ngapi zinakamilika kwa kila kipimo cha muda. Si lengo lilelile, na kuboresha kimoja kunaweza kuumiza kingine. Kuweka kwenye makundi huboresha uwezo wa kupitisha lakini huongeza ucheleweshaji kwa kipengele cha kwanza kwenye kundi; kuongeza wafanyakazi sambamba huinua uwezo wa kupitisha lakini kunaweza kuzorotesha ucheleweshaji wa mkia kupitia mgongano. Amua ni kipi watumiaji wako wanahitaji kweli. Na daima angalia mkia: ucheleweshaji wa p95 na p99, 5% na 1% ya polepole zaidi ya maombi, kwa sababu kwa ukubwa mtumiaji hufanya maombi mengi na hukumbana na mkia mara nyingi. Ripoti asilimia, toa tahadhari juu yake, na uzipangie bajeti.

### Jua mipaka ya ulinganifu wa utekelezaji

Unapofanya utekelezaji sambamba, kumbuka [sheria ya Amdahl](https://en.wikipedia.org/wiki/Amdahl%27s_law): kuongezeka kwa kasi kutokana na kuongeza vichakataji kunadhibitiwa na sehemu ya kazi inayopaswa kuendeshwa kwa mfuatano. Ikiwa 10% ya kazi ni ya mfuatano kwa asili, hakuna idadi ya viini itakayokufikisha zaidi ya kasi ya mara 10. Ulinganifu (kupanga kazi ili kazi ndogo ziendelee kwa kujitegemea) na utekelezaji sambamba (kuziendesha kweli kwa wakati mmoja) huongeza ugumu halisi, kutoka hali za mbio hadi mzigo wa uratibu. Pima sehemu ya mfuatano kabla hujadhani nyuzi zaidi zitakuokoa, na uwe mkweli kwamba toleo rahisi zaidi sahihi mara nyingi ni la haraka vya kutosha.

### Tumia kache na ukaribu wa data, na uheshimu gharama zake

[Kache](https://en.wikipedia.org/wiki/Cache_(computing)), hifadhi ya haraka ya matokeo yaliyokokotolewa hivi karibuni au kwa gharama kubwa, ndiyo zana yenye nguvu zaidi ya utendaji ulio nayo na hatari zaidi. Kauli ya Phil Karlton kwamba matatizo mawili magumu katika sayansi ya kompyuta ni kubatilisha kache na kutaja vitu ni onyo: kache iliyopitwa na wakati hutoa majibu yasiyo sahihi, na mantiki ya kubatilisha ndipo hitilafu fiche huzaliwa. Weka kache kwa makusudi, weka muda wa kuisha, na ujue hadithi yako ya usahihi kabla ya kuboresha kiwango cha mafanikio. Katika kiwango cha chini kabisa, [ukaribu wa marejeo](https://en.wikipedia.org/wiki/Locality_of_reference), kuweka data inayotumika pamoja karibu pamoja kwenye kumbukumbu, hutumia daraja la kache la CPU na unaweza kufanya msimbo uwe wa haraka mara kadhaa bila badiliko la algoriti, kwa kugeuza kukosa kache kuwa mafanikio. Safu zinazoendelea hushinda miundo ya kufukuza viashiria kwa sababu hii. Hili linakutana na uchaguzi wa mpangilio wa data katika sura ya 3.4.

### Pima kwa uaminifu na usiamini vipimo vidogo

Kipimo kinachosema uongo ni kibaya kuliko kutokuwa nacho, kwa sababu kinatoa kujiamini kwa uongo. Pasha moto kabla ya kupima, ili upime tabia ya hali thabiti badala ya kuanza mara moja na ukusanyaji wa wakati-wa-kuendesha. Endesha marudio mengi na uripoti tofauti, si namba moja ya bahati. Tumia mzigo wa kazi unaowakilisha wenye ukubwa na migawanyo halisi ya data, kwa sababu kipimo kidogo kwenye ingizo la kuchezea mara nyingi hupima uwezo wa mkusanyaji kufuta jaribio lako badala ya kasi halisi ya msimbo. Jihadhari na mitego ya kawaida: thamani ambayo kiboresha huthibitisha haitumiki na kuiondoa, kitanzi ambacho muda-wa-kuendesha unakiinua, au kache inayopashwa moto kwenye kipimo na baridi kwenye uzalishaji. Ukiwa na shaka, pima njia nzima, si kazi iliyotengwa.

### Dhibiti utendaji kwenye CI na uuangalie kwenye uzalishaji

Fanya utendaji kuwa sifa ambayo bomba inailinda. Ongeza majaribio ya utendaji kwenye mkakati wa sura ya 2.4, na malango ya kurudi nyuma yanayofeli ujenzi kipimo muhimu au bajeti inapozorota zaidi ya kizingiti. Hili hunasa kuteleza polepole kabla ya kuunganishwa. Kisha funga mzunguko kwenye uzalishaji kwa telemetri ya sura ya 9.2: fuatilia asilimia halisi za ucheleweshaji, viwango vya ugawaji, na hoja za polepole dhidi ya bajeti zako, kwa sababu trafiki ya uzalishaji hupata kesi ambazo vipimo vyako havikuwahi kufikiria.

## Mabadilishano: faida na hasara

| Mbinu | Faida | Hasara |
|---|---|---|
| Boresha sasa, kulingana na hisia | Inahisi yenye tija; ushindi wa bahati mara kwa mara | Kwa kawaida inarekebisha msimbo usio sahihi; inaongeza ugumu bila faida |
| Pima kwanza, kisha boresha | Inalenga kizuizi halisi; inategemea ushahidi | Inahitaji zana na nidhamu; polepole kuanza |
| Kache | Faida kubwa za ucheleweshaji na uwezo wa kupitisha | Hitilafu za kubatilisha; data iliyopitwa na wakati; gharama ya kumbukumbu |
| Ulinganifu zaidi | Uwezo wa juu wa kupitisha kwa kazi sambamba | Dari ya Amdahl; mgongano; hitilafu za ulinganifu |
| Uboreshaji mdogo | Hubana vigezo visivyobadilika | Dari ndogo; huumiza usomekaji; mara nyingi ni kelele |
| Uboreshaji wa algoriti | Ushindi hupanuka na ukubwa wa ingizo | Unahitaji uchambuzi; wakati mwingine uandishi upya mkubwa |
| Malango ya utendaji ya CI | Husimamisha kurudi nyuma mapema na kwa bei nafuu | Vipimo visivyotegemewa vinamomonyoa uaminifu; vinahitaji mazingira thabiti |

Mvutano wa msingi ni juhudi dhidi ya malipo, na suluhisho ni upimaji. Kazi ya utendaji ina faida zinazopungua kwa kasi: suluhisho la kwanza lililoongozwa na uchunguzi linaweza kupunguza ucheleweshaji kwa nusu, la kumi linaweza kupunguza asilimia moja huku likiongeza ugumu wa msimbo mara mbili. Unalitatua kwa kukataa kuboresha bila namba mkononi na bajeti ya kufikia. Pima ili kupata suluhisho linalostahili kufanywa, na usimame mara tu unapovuka bajeti badala ya kufukuza kasi kwa ajili yake yenyewe.

## Maswali ya kujadili na timu yako

1. **Je, una bajeti ya utendaji iliyoandikwa kwa njia zako muhimu, na je, imeelezwa kama asilimia?** Timu nyingi zina hisia isiyo wazi kwamba mambo yanapaswa kuwa "ya haraka" lakini hakuna namba ambayo mtu yeyote angeweza kuikosa, ikimaanisha utendaji si kazi ya mtu hadi uvunjike. Bajeti kama "p99 chini ya ms 300" hufanya lengo liwe madhubuti, inawapa wapitiaji kitu cha kutekeleza, na inageuza kurudi nyuma kuwa tukio linaloonekana badala ya kuteleza polepole. Ni muhimu zaidi kwa timu kubwa, ambapo ucheleweshaji hupenya kupitia mikono mingi na hakuna mwandishi mmoja anayeona gharama ya jumla. Leta data yako ya sasa ya ucheleweshaji na uulize kama mnaripoti wastani, unaowabembeleza, au asilimia, zinazosema ukweli. Usipoweza kusema "haraka vya kutosha" inamaanisha nini kama namba, hilo ndilo la kwanza la kurekebisha.

2. **Ulipoboresha kitu mara ya mwisho, kichunguzi cha utendaji kilikuambia pa kuangalia, au ulikisia?** Kizuizi kinajulikana kuwa mahali pengine kuliko wahandisi wenye uzoefu wanavyotarajia, na muda unaotumika kurekebisha msimbo usio sahihi ni muda unaopotea mara mbili, mara moja katika kazi na mara moja katika ugumu ulioongezwa. Utamaduni unaochunguza kwanza hutumia juhudi mahali panapolipa na kuacha msimbo wazi bila kuguswa. Waombe timu yako kukumbuka marekebisho matatu ya mwisho ya utendaji na kama kila moja lilianza kutoka kipimo au dhana. Fikiria kama unaweza kuchunguza kwenye uzalishaji, au mazingira ya majaribio yanayowakilisha, kwa sababu uchunguzi wa kompyuta mpakato unaweza kupotosha vibaya. Jibu hufichua kama kazi yenu ya utendaji ni uhandisi au hadithi za kale.

3. **Nini kinazuia kurudi nyuma kwa utendaji kufika kwenye uzalishaji leo?** Katika timu inayokua, jibu la uaminifu mara nyingi ni "malalamiko ya mteja," ikimaanisha watumiaji ndio jaribio lenu la kurudi nyuma. Lango la CI linalofeli ujenzi kipimo au bajeti inapozorota hunasa tatizo wakati ni nafuu kurekebisha na mwandishi bado anakumbuka badiliko. Jadilini kama vipimo vyenu ni thabiti vya kutosha kuvidhibiti, kwa sababu jaribio la utendaji lisilotegemewa linalolia mbwa-mwitu litapuuzwa au kuzimwa. Zungumza kuhusu unachotazama kwenye uzalishaji pia, kwa kuwa baadhi ya kurudi nyuma kunaonekana tu chini ya trafiki na data halisi. Lengo ni kufanya utendaji kuwa sifa ambayo mfumo unaitetea kiotomatiki, si ile mnayoigundua upya kwenye tukio.

4. **Je, mnaboresha ucheleweshaji au uwezo wa kupitisha kwa kila njia muhimu, na je, yeyote ameandika uchaguzi huo?** Haya ni malengo tofauti yanayovuta pande kinyume: kuweka kwenye makundi na wafanyakazi sambamba huinua uwezo wa kupitisha lakini kunaweza kuongeza ucheleweshaji kwa maombi ya mtu mmoja mmoja, kwa hiyo timu inayoboresha kwa hisia mara nyingi hununua mhimili usio sahihi na kuwafanya watumiaji wasubiri kuokoa muda wa mashine ambao hakuna aliyekuwa na uhaba nao. Katika timu kubwa hatari huzidishwa, kwa sababu kundi moja hurekebisha huduma ya pamoja kwa uwezo wa kupitisha wa wingi huku jingine likiitegemea kwa ucheleweshaji shirikishi, na hakuna anayejua lengo la mwingine. Leta mtindo halisi wa matumizi wa kila njia (ombi shirikishi dhidi ya kundi la nyuma), ucheleweshaji wa asilimia wa sasa, na uwezo endelevu wa kupitisha mnaouhitaji, kisha amueni mhimili waziwazi badala ya kuacha chaguo-msingi lijitokeze. Kwa mfumo wa shirika kubwa au serikali chini ya SLA, taja ni kipimo kipi makubaliano yameandikiwa, kwa sababu kuboresha mhimili usiopimwa kunaweza kuvunja mkataba huku dashibodi zenu zikionekana zenye afya.

5. **Mnajuaje vipimo vyenu vinapima kazi halisi badala ya kiboresha kufuta jaribio lenu?** Kipimo kinachosema uongo ni kibaya kuliko kutokuwa nacho, kwa sababu kinaipa timu kujiamini kwa uongo kisha kurudi nyuma kunasafirishwa hata hivyo. Timu mara kwa mara huripoti namba moja ya bahati kutoka mzunguko baridi kwenye ingizo la kuchezea, ambayo hupima kuanza, ukusanyaji wa wakati-wa-kuendesha, na uwezo wa mkusanyaji kuondoa msimbo usiotumika badala ya tabia ambayo watumiaji wanaikumbuka kweli. Leta kipimo cha mfano na ukihoji: je, kinapasha moto, kinaendesha marudio mengi, kinaripoti tofauti, kinatumia ukubwa na migawanyo ya data inayowakilisha, na kinashinda kuondolewa kwa msimbo uliokufa kwenye matokeo yake. Mvuto unaoshindana ni kwamba vipimo vya uaminifu ni polepole kuandika na kuendesha kuliko vipimo vidogo vya haraka, kwa hiyo kubaliana mahali ambapo makadirio ya bei nafuu yanakubalika na mahali unapodai ukali. Katika mazingira ya umma au yanayodhibitiwa ambapo vyombo vya ununuzi na usimamizi vitakuomba kuzalisha namba upya, nasa kifaa, mzigo wa kazi, na mazingira kando ya matokeo ili dai liweze kuthibitishwa badala ya kutamkwa tu.

6. **Kazi ya utendaji inaposhindana na vipengele kwa wahandisi walewale, mnaamuaje, na nani anashikilia mamlaka ya bajeti?** Utendaji una faida zinazopungua kwa kasi, kwa hiyo suluhisho la kwanza lililoongozwa na uchunguzi linaweza kupunguza ucheleweshaji kwa nusu huku la kumi likipunguza asilimia moja kwa ugumu wa msimbo mara mbili, na bila kanuni sauti kubwa zaidi au tarehe ya mwisho iliyo karibu zaidi hushinda. Mazingatio yanayoshindana ni halisi: deni la utendaji ambalo halijarekebishwa hujumlika kimyakimya na kuwa ghali zaidi kurekebisha baadaye, hata hivyo kufukuza kasi zaidi ya bajeti kunaiacha ramani ya barabara na njaa na kuongeza ugumu unaopunguza kasi ya kazi ya baadaye. Leta hali ya sasa ya bajeti kwa kila njia muhimu, gharama iliyokadiriwa ya hali ilivyo kwa mashine au ubadilishaji uliopotea, na malipo ya pembeni ya uboreshaji unaofuata, ili biashara hii ifanywe kwa ushahidi badala ya shinikizo. Kwa programu ya shirika kubwa au serikali, taja nani anamiliki bajeti ya utendaji na nani anaweza kuidhinisha matumizi ya muda wa kihandisi dhidi yake, kwa sababu lengo ambalo hakuna anayewajibika kulitetea ni lile linalomomonyoka kimyakimya.

## Mtazamo wa sekta

**Kampuni changa.** Kasi ya utoaji inashinda mchakato, kwa hiyo pinga uandishi upya na mifumo mikubwa ya utendaji. Tumia alasiri moja na kichunguzi cha utendaji kwenye njia ambayo watumiaji wanalalamikia kweli, rekebisha gharama kubwa zaidi (mara nyingi hoja ya N+1 au uchanganuzi wa mstari wa bahati mbaya), na uongeze bajeti moja nyepesi ya asilimia kwenye CI ili ushindi usirudi nyuma kimyakimya. Hifadhi uboreshaji wa kina kwa wakati namba halisi, si hisia, inaposema msimbo ni polepole mno.

**Biashara ndogo.** Bila mtaalamu wa utendaji na bajeti finyu, tegemea zana ambazo tayari unazilipia: kichunguzi katika wakati-wa-kuendesha wako, asilimia za ucheleweshaji katika dashibodi ya mwenyeji wako, na kichanganuzi cha hoja kilichojengwa ndani ya hifadhidata yako. Weka bajeti moja au mbili wazi zilizofungwa na kitu ambacho wateja wanahisi, kama muda wa kupakia ukurasa au wa malipo, na uchukulie ukiukaji kama ishara ya kununua ngazi ya haraka zaidi au kurekebisha hoja mbaya zaidi badala ya kuanzisha mradi wa urekebishaji usioweza kuuajiri.

**Biashara kubwa.** Kwa ukubwa wa meli, utendaji ni gharama ya moja kwa moja, kwa hiyo utawale kama nidhamu ya pamoja: zana za kawaida za uchunguzi, bajeti za asilimia zilizofungwa na vipimo vya biashara, na malango ya kurudi nyuma ya CI yanayotumika kwa uthabiti ili kuteleza polepole kwa timu yoyote kusiinue bili nzima ya wingu. Fuatilia ucheleweshaji, ugawaji, na uwezo wa kupitisha dhidi ya vipimo vya msingi kuvuka huduma, na uhifadhi ushahidi wa vipimo unaoweza kuzalishwa upya, kwa sababu upunguzaji wa CPU wa 30% kwenye meli kubwa ni akiba inayojirudia inayostahili kukaguliwa na kutetewa dhidi ya adhabu za SLA.

**Serikali.** Utendaji ni hakikisho la ufikiaji: ukurasa unaopakia kwenye simu ya zamani kupitia muunganisho dhaifu huamua kama raia anakamilisha dai la manufaa. Weka bajeti wazi dhidi ya vifaa vya kiwango cha chini vinavyowakilisha na mitandao iliyopunguzwa kasi, na uchapishe matokeo ya vipimo yanayoweza kuzalishwa upya yanayonasa kifaa, mtandao, na mzigo wa kazi, ili vyombo vya ununuzi na usimamizi viweze kuthibitisha namba badala ya kuziamini tu. Pendelea upimaji wa uwazi, unaokaguliwa kuliko madai ya muuzaji, na uwashikilie wagavi kwa ushahidi uleule unaoweza kuzalishwa upya.

## Mifano

**Kampuni changa.** Timu ndogo ya SaaS inagundua dashibodi yao inahisi ni polepole na inavutiwa kuiandika upya kwa mfumo wa kazi wa haraka zaidi. Badala yake wanatumia alasiri na kichunguzi cha utendaji na grafu ya mwali, inayoonyesha kwamba 70% ya muda wa ombi ni mwisho mmoja unaotoa hoja moja ya hifadhidata kwa kila safu, muundo wa kawaida wa N+1. Wanaibadilisha na hoja moja ya kundi, ucheleweshaji unashuka kutoka sekunde 1.2 hadi milisekunde 90, na wanaongeza bajeti ya p99 ya ms 200 kwenye kipimo chepesi cha CI ili marekebisho yasirudi nyuma kimyakimya. Hakuna uandishi upya, alasiri moja, ushindi wa mara kumi.

**Biashara kubwa.** Jukwaa la rejareja linaendesha maelfu ya matukio, na bili yake ya wingu inatawaliwa na huduma moja ya mapendekezo. Kampeni ya uchunguzi wa utendaji inapata msukosuko mzito wa ugawaji unaosababisha vituo vya mara kwa mara vya ukusanyaji wa taka, pamoja na kache yenye kiwango duni cha mafanikio. Kurekebisha miundo ya data kwa ukaribu na kurekebisha funguo za kache kunapunguza CPU kwa kila ombi kwa 40%, ikiiruhusu timu kuendesha trafiki ileile kwenye mashine chache kwa 40%. Akiba inalipa juhudi za kihandisi ndani ya wiki, na SLA ya ucheleweshaji wa p99 iliyovunjwa mara kwa mara sasa inashikilia kwa raha, ikiepuka adhabu za kimkataba.

**Serikali.** Mamlaka ya kitaifa ya kodi lazima iwahudumie raia kwenye vifaa vya zamani na miunganisho dhaifu ya vijijini. Timu inaweka bajeti wazi: ukurasa wa kuwasilisha lazima uwe shirikishi chini ya sekunde 3 kwenye simu ya kiwango cha chini kupitia wasifu wa 3G uliopunguzwa kasi. Wanachunguza ukurasa, wanapunguza kazi inayozuia ushirikiano, na kuchapisha matokeo ya vipimo yanayoweza kuzalishwa upya, wakinasa kifaa, mtandao, na mzigo wa kazi, ili vyombo vya usimamizi na wakaguzi wa ufikivu waweze kuthibitisha dai badala ya kuliamini tu. Utendaji hapa si kiegemeo cha gharama bali hakikisho la ufikiaji linaloweka huduma ikitumika kwa kila mtu.

## Kesi ya biashara: sababu, ROI, na TCO

Mapato ya uhandisi wa utendaji yanaonekana katika leja tatu. Ya kwanza ni gharama ya miundombinu: msimbo wa haraka zaidi hufanya kazi ileile kwenye mashine chache, na kwa meli kubwa upunguzaji wa CPU wa 30% ni akiba ya moja kwa moja, inayojirudia inayozidi sana juhudi ya mara moja ya kihandisi. Ya pili ni mapato na kuridhika: ucheleweshaji unahusiana na ubadilishaji, kuacha, na uaminifu wa mtumiaji, kwa hiyo kupunguza mkia ni kiegemeo cha ukuaji, si kazi ya usafi tu. Ya tatu ni hatari iliyoepukwa: ukiukaji wa SLA hubeba adhabu, na uzinduzi unaoyeyuka chini ya mzigo hubeba uharibifu wa sifa na gharama ya kuzima moto.

Jumla ya gharama ya umiliki ni ya wastani na ya mapema. Unawekeza katika zana za uchunguzi, mazingira thabiti ya kupima, na malango ya CI, pamoja na nidhamu ya kuandika bajeti na kusoma uchunguzi. Gharama kubwa zaidi, iliyofichika ni mbadala: deni la utendaji hujumlika kimyakimya, na kuongeza kasi kwenye mfumo wa polepole baada ya uzinduzi ni ghali zaidi sana kuliko kuulinda mfululizo. Jenga hoja kwa uongozi katika vipimo vyao wenyewe. Tafsiri ucheleweshaji kuwa viwango vya ubadilishaji au ukamilishaji wa raia, tafsiri CPU kuwa matumizi ya kila mwezi ya wingu, na tafsiri lango la kurudi nyuma kuwa matukio yaliyoepukwa. Hoja yenye nguvu zaidi ni kwamba utendaji ni wa bei nafuu kulinda commit kwa commit na wa maangamizi kurejesha baada ya kuoza.

## Mifumo mibaya na mitego

- **Kuboresha bila kuchunguza.** Kurekebisha msimbo usio kizuizi huku gharama halisi ikibaki bila kuguswa.
- **Uboreshaji wa mapema.** Kutoa dhabihu uwazi kwa kasi ya kufikirika ambayo kichunguzi kisingeitaja kamwe.
- **Kuripoti wastani.** Kuficha mkia wenye maumivu nyuma ya wastani wa kustarehesha; watumiaji wanahisi p99, si wastani.
- **Maigizo ya vipimo vidogo.** Namba kutoka mzigo wa kuchezea ambao kiboresha kilifuta nusu yake, bila kupasha moto wala tofauti iliyoripotiwa.
- **Kache bila hadithi ya kubatilisha.** Kufukuza kiwango cha mafanikio huku ukitoa data iliyopitwa na wakati au isiyo sahihi.
- **Kudhani nyuzi zaidi zinasaidia.** Kupuuza sheria ya Amdahl na sehemu ya mfuatano, kisha kuzama katika mgongano.
- **Hakuna lango la kurudi nyuma.** Kuwaacha watumiaji kuwa jaribio la utendaji kwa sababu hakuna kitu kwenye CI kinacholinda bajeti.
- **Kuboresha mhimili usio sahihi.** Kununua uwezo wa kupitisha kwa kuweka kwenye makundi wakati watumiaji walihitaji ucheleweshaji mdogo, au kinyume chake.

## Kielelezo cha ukomavu

- **Ngazi ya 1, Kuanzisha:** Utendaji unashughulikiwa tu kitu kinapovunjika. Hakuna bajeti, hakuna tabia ya kuchunguza, hakuna vipimo. Uboreshaji ni kubahatisha kunakoendeshwa na hisia, na wastani ndio kipimo pekee ambacho mtu yeyote anaripoti.
- **Ngazi ya 2, Kuendeleza:** Baadhi ya timu huchunguza wakati wa matukio na kuweka vipimo vichache, lakini mazoea hayana uthabiti na yanategemea shauku ya mtu binafsi. Bajeti zipo kwa njia isiyo rasmi kwa njia moja au mbili muhimu, na asilimia zinaonekana kwenye baadhi ya dashibodi, hata hivyo hakuna kinachozuia kurudi nyuma kabla hakijasafirishwa na kila timu inavumbua upya mbinu yake.
- **Ngazi ya 3, Kusawazisha:** Njia muhimu zina bajeti za asilimia zilizoandikwa, na uchunguzi ni hatua ya kwanza iliyoandikwa, inayotarajiwa kabla ya mtu yeyote kuboresha. CI inajumuisha majaribio ya utendaji yenye malango ya kurudi nyuma, kanuni za upimaji wa uaminifu (kupasha moto, tofauti, data inayowakilisha) zimeandikwa na kutekelezwa shirika zima, na kila timu inafuata mbinu ileile badala ya yake yenyewe.
- **Ngazi ya 4, Kusimamia:** Shirika hupima utendaji kama sifa inayodhibitiwa. Asilimia za ucheleweshaji, uwezo wa kupitisha, viwango vya ugawaji, na hesabu za hoja za polepole zinafuatiliwa dhidi ya vipimo vya msingi wazi kwenye uzalishaji na CI, kurudi nyuma kunapimwa dhidi ya vizingiti badala ya kubishaniwa, na bajeti zimefungwa na vipimo vya biashara kama ubadilishaji au matumizi ya wingu ili ukiukaji uchochee uamuzi unaotegemea data. Ushahidi wa vipimo unaweza kuzalishwa upya na kunaswa na kifaa, mzigo wa kazi, na mazingira yake kwa ukaguzi.
- **Ngazi ya 5, Kuratibu:** Utendaji unaboreshwa kila wakati na kuunganishwa kuvuka shirika. Bajeti, uchunguzi, upimaji wa uaminifu, na uchambuzi wa grafu ya mwali ni ujuzi wa kawaida, malango ya kurudi nyuma ni thabiti na yanaaminiwa, na data ya uzalishaji na CI hufunga mzunguko kiotomatiki. Shirika hurekebisha bajeti trafiki, vifaa, na vipaumbele vya biashara vinapohama, husawazisha upya juhudi kuelekea njia ambapo malipo ni ya juu zaidi, na kutetea utendaji kama sifa ya kudumu badala ya kampeni ya mara kwa mara.

## Mawazo ya kujadili

1. Ni njia zipi muhimu zenu zina bajeti iliyoandikwa, inayotegemea asilimia leo, na zipi zinalindwa kwa matumaini tu?
2. Kichunguzi cha utendaji kilikushangaza lini mara ya mwisho, na hilo lilikufundisha nini kuhusu mahali unapodhani muda unaenda?
3. Je, vipimo vyenu vinapasha moto, kuripoti tofauti, na kutumia data inayowakilisha, au vinapima kiboresha?
4. Mnatumia mashine wapi kuziba msimbo ambao kampeni ya uchunguzi ingeufanya kuwa wa bei nafuu zaidi?
5. Kwa kazi yenu iliyo na ulinganifu zaidi, sehemu ya mfuatano ni ipi, na je, sheria ya Amdahl inadhibiti kasi mnayoifukuzia?
6. Mwenzako akiunganisha badiliko lililoongeza ucheleweshaji wa p99 mara mbili, ingechukua muda gani kabla mtu yeyote kugundua, na wangegunduaje?

## Mambo muhimu ya kukumbuka

- Pima kabla ya kuboresha; kizuizi mara chache kipo unapokisia, na uboreshaji wa mapema unagharimu uwazi bila faida.
- Fafanua "haraka vya kutosha" kama bajeti ya asilimia, kwa sababu wastani huficha mkia ambapo watumiaji halisi wanaishi.
- Pendelea ushindi wa algoriti (daraja bora la Big O) kuliko urekebishaji mdogo, na ujue kama unahitaji ucheleweshaji au uwezo wa kupitisha.
- Heshimu mipaka ya ulinganifu wa utekelezaji (sheria ya Amdahl) na hatari za kache (kubatilisha na kupitwa na wakati).
- Pima kwa uaminifu kwa kupasha moto, tofauti, na mizigo ya kazi inayowakilisha, na usiamini vipimo vidogo.
- Dhibiti utendaji kwenye CI (sura ya 2.4) na uuangalie kwenye uzalishaji (sura ya 9.2); kamilisha mtazamo wa ngazi ya mfumo katika sura ya 3.5.
- Utendaji ni gharama kwa mashirika makubwa, ufikiaji kwa serikali, na ni wa bei nafuu kulinda mfululizo lakini ghali kurekebisha baadaye.

## Marejeo na usomaji zaidi

- Brendan Gregg, *Systems Performance: Enterprise and the Cloud* (profiling, flame graphs, and method).
- Brendan Gregg, *BPF Performance Tools* (practical observability and profiling on Linux).
- Donald E. Knuth, "Structured Programming with go to Statements" (*ACM Computing Surveys*, 1974): the source of the premature-optimization maxim.
- Donald E. Knuth, *The Art of Computer Programming* (algorithmic analysis and complexity).
- Thomas H. Cormen, Charles E. Leiserson, Ronald L. Rivest, and Clifford Stein, *Introduction to Algorithms* (Big O and algorithmic efficiency).
- Gene M. Amdahl, "Validity of the Single Processor Approach to Achieving Large-Scale Computing Capabilities" (1967): the origin of Amdahl's law.
- Ulrich Drepper, "What Every Programmer Should Know About Memory" (the memory hierarchy and data locality).
- Martin Kleppmann, *Designing Data-Intensive Applications* (latency, throughput, and tail behavior in systems).
- Aleksey Shipilev, "JMH and the pitfalls of microbenchmarking" (honest benchmarking practice on managed runtimes).
- Ilya Grigorik, *High Performance Browser Networking* (client-side and network performance for low-bandwidth users).
