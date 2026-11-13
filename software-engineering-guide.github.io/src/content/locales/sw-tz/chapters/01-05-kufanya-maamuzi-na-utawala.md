# 1.5 Kufanya maamuzi na utawala

## Muhtasari na msukumo

Kila mfumo wa programu ni jumla ya maelfu ya maamuzi: [hifadhidata](https://en.wikipedia.org/wiki/Database) ipi, usanifu upi, maktaba ipi, kujenga au kununua, lini kuchukua deni na lini kulipa. Utawala ni jinsi unavyofanya maamuzi haya vizuri na kwa uthabiti, kuwashirikisha watu sahihi bila kuunda vikwazo, na kuhifadhi hoja ili timu za baadaye zisihukumiwe kujifunza upya. Katika timu ndogo, maamuzi hufanyika kwa mazungumzo na kuishi katika kumbukumbu ya pamoja. Kwa ukubwa, kumbukumbu hiyo hupotea. Watu huondoka, timu hupangwa upya, na "kwa nini" nyuma ya uchaguzi muhimu hupotea, ikiwaacha warithi ama kuuiga bila kuelewa au kuung'oa kwa upofu. Utawala mzuri ni mitambo inayofanya maamuzi yaonekane, ya makusudi, na ya kudumu kuvuka shirika kubwa linalobadilika.

Changamoto kuu kwa timu kubwa ni kusawazisha uhuru dhidi ya mpangilio. Sukuma maamuzi yote juu hadi bodi ya kati, na unapata uthabiti, lakini kwa gharama ya vikwazo vinavyolemaza na timu zisizowezeshwa. Sukuma maamuzi yote chini, na unapata kasi, lakini kwa gharama ya fujo: teknolojia zisizooana, juhudi zinazorudiwa, na makosa yanayorudiwa. Jibu lililokomaa si uwekaji kati wala machafuko. Ni mfano wenye tabaka. Timu huamua mengi kwa mahali ndani ya "barabara iliyotengenezwa" iliyowekwa alama vizuri, huku mchakato mwepesi, wa uwazi ukitawala chaguo zinazovuka maeneo kweli na ngumu kutenduliwa. Lengo ni kufanya maamuzi mazuri kuwa chaguo-msingi rahisi, na kutumia umakini adimu wa utawala pale tu unapojalisha kweli.

Mashirika makubwa na ya serikali hubeba dau la juu zaidi. Lazima yatimize wakaguzi, wadhibiti, na vyombo vya usimamizi vinavyodai maamuzi yaliyoandikwa na yanayoweza kutetewa. Hufanya kazi kwa upeo mrefu wa muda, ambapo uchaguzi mbaya wa usanifu au rundo lisilosimamiwa la [deni la kiufundi](https://en.wikipedia.org/wiki/Technical_debt) linaweza kuyabebesha mzigo kwa muongo. Na wajibu wao wa ununuzi na uzingatiaji hufanya maamuzi ya kujenga-dhidi-ya-kununua kuwa na matokeo makubwa hasa na magumu kutenduliwa. Kwa mashirika haya, kufanya maamuzi kwa nidhamu na kurekodiwa vizuri si urasimu kwa ajili yake. Ni usimamizi wa hatari, kumbukumbu ya kitaasisi, na msingi wa uwajibikaji.

## Kanuni kuu

- Rekodi maamuzi na hoja zake; uamuzi bila sababu ni dhima.
- Sukuma maamuzi hadi ngazi ya chini kabisa yenye muktadha, ndani ya mipaka wazi ya ulinzi.
- Linganisha uzito wa mchakato na uzito na uwezekano wa kutenduliwa wa uamuzi.
- Tofautisha yanayoweza kutenduliwa ("mlango wa pande mbili") na yasiyoweza kutenduliwa ("mlango wa upande mmoja") na uyatawale tofauti.
- Pendelea barabara zilizotengenezwa na chaguo-msingi kuliko idhini za kesi kwa kesi.
- Chukulia deni la kiufundi kama jalada linalosimamiwa, si kasoro ya maadili ya kuficha.
- Fanya utawala uwe wazi; kufanya maamuzi kwa siri huzaa kutoaminiana na kurudia kazi.

## Mapendekezo

### Pokea Rekodi za Maamuzi ya Usanifu na mchakato wa RFC wa ukubwa unaofaa

[Rekodi ya Uamuzi wa Usanifu](https://en.wikipedia.org/wiki/Architectural_decision) (ADR) ni waraka mfupi usiobadilika unaonasa uamuzi mmoja muhimu: muktadha wake, chaguo zilizozingatiwa, uchaguzi uliofanywa, na matokeo. Hifadhi ADR katika udhibiti wa matoleo kando ya msimbo, ili hoja isafiri na mfumo. Kwa maamuzi yanayohitaji mchango kabla ya kufanywa, tumia mchakato mwepesi wa [RFC](https://en.wikipedia.org/wiki/Request_for_Comments) (ombi la maoni): sambaza pendekezo, karibisha maoni kwa kipindi kilichowekwa, kisha amua na urekodi. Weka vyote viwili vyepesi. Thamani iko katika fikra na rekodi ya kudumu, si katika violezo tata. Pamoja, ADR na RFC hugeuza hoja isiyoandikwa, iliyosahaulika kuwa kumbukumbu ya kitaasisi inayotafutika.

### Tawala kupitia barabara zilizotengenezwa, si walinzi wa lango

Badala ya kupitia kila uamuzi mmoja mmoja, wekeza katika "barabara iliyotengenezwa": seti ya chaguo-msingi zilizobarikiwa, zinazosaidiwa vyema, lugha zilizoidhinishwa, mifumo, mabomba ya utoaji, na mifumo, ambazo timu zinaweza kupokea kwa msuguano mdogo na msaada mwingi. Timu zinazobaki kwenye barabara iliyotengenezwa zinahitaji utawala mdogo, kwa sababu uchaguzi salama, unaozingatia kanuni pia ni rahisi. Timu zenye sababu halisi ya kuiacha zinaweza, lakini zinabeba wajibu wa ziada na mapitio mepesi. Mfano huu wa "njia ya dhahabu" unapanuka vizuri zaidi kuliko bodi ya kati inayoidhinisha kila kitu, kwa sababu unahamisha utawala kutoka kulinda lango kwa kesi kwa kesi hadi chaguo-msingi zilizosanifiwa vyema.

### Tumia bodi za mapitio ya usanifu kwa uchache na kwa uwazi

Bodi ya mapitio ya usanifu, au mfano wake, ina jukumu halali kwa maamuzi makubwa zaidi, yanayovuka maeneo zaidi, au yasiyoweza kutenduliwa zaidi, na kwa kuweka viwango vinavyofafanua barabara iliyotengenezwa. Weka wigo wake finyu, vigezo vyake vichapishwe, na mchakato wake uwe wa haraka na wa ushauri, si kikwazo cha lazima kwa kazi ya kawaida. Kazi ya bodi ni kusimamia mshikamano na kushiriki maarifa, si kuidhinisha kila uchaguzi. Bodi inapogeuka kuwa foleni ambayo kila mradi lazima uisubiri, imeshindwa. Kasimu kwa nguvu, na uhifadhi mapitio ya kati kwa maamuzi machache yanayostahili kweli.

### Fanya kujenga-dhidi-ya-kununua-dhidi-ya-kupokea kuwe uchambuzi wa makusudi

Kwa uwezo wowote muhimu, pima njia tatu: kuujenga ndani, kununua bidhaa ya kibiashara, au kupokea suluhisho la [chanzo huria](https://en.wikipedia.org/wiki/Open-source_software). Jenga pale uwezo ni kitofautishi cha kweli na msingi wa dhamira yako. Nunua au pokea uwezo usio na upekee ambao wengine wanaufanya vizuri zaidi. Hesabu [jumla ya gharama ya umiliki](https://en.wikipedia.org/wiki/Total_cost_of_ownership) (TCO), si bei ya awali tu. Kununua kunaleta gharama za leseni, uunganishaji, na [kufungwa](https://en.wikipedia.org/wiki/Vendor_lock-in). Kujenga kunaleta matengenezo na wafanyakazi wa daima. Kupokea chanzo huria kunaleta wajibu wa msaada na ufuatiliaji wa usalama. Rekodi uamuzi na dhana zake kama ADR, ili uweze kuupitia upya hali zinapobadilika.

### Simamia deni la kiufundi kama jalada

Deni la kiufundi si baya kwa asili. Wakati mwingine kulichukua ili kutoa mapema ndiyo uamuzi sahihi. Kilicho kibaya ni deni lisilosimamiwa, lisiloonekana, lililosahaulika. Weka orodha wazi ya deni muhimu. Kwa kila kipengee, taja gharama linayoleta ("riba" inayoendelea) na gharama ya kulirekebisha. Kisha lisimamie kama jalada la kifedha. Lipa deni la riba ya juu linalopunguza kasi ya timu kila siku. Vumilia deni la riba ya chini katika pembe thabiti. Fanya maamuzi ya deni kwa makusudi badala ya kwa ajali. Tenga sehemu ya kudumu ya uwezo kulipa deni, ili lisijumlike kamwe kuwa mgogoro.

### Tofautisha maamuzi yanayoweza kutenduliwa na yasiyoweza kutenduliwa

Si maamuzi yote yanastahili mazingatio sawa. Maamuzi ya "mlango wa pande mbili" yanayoweza kutenduliwa hutenduliwa kwa urahisi, kwa hiyo yafanye haraka na kwa mahali, na timu, kwa mwelekeo wa kutenda. Kuyahangaikia hupoteza muda na kupunguza kasi ya kujifunza. Maamuzi ya "mlango wa upande mmoja" yasiyoweza kutenduliwa au ghali kutenduliwa, mkataba wa umma wa [API](https://en.wikipedia.org/wiki/API), mfano wa data kwa ukubwa, ahadi ya miaka mingi kwa msambazaji, yanastahili mazingatio ya polepole, makini, ya waandamizi na sababu iliyorekodiwa. Kuainisha maamuzi hivi ni mojawapo ya mazoea ya utawala yenye kiegemeo kikubwa zaidi uliyo nayo. Huelekeza uchunguzi adimu mahali panapolipa, na huachia kila kitu kingine kusonga.

## Mabadilishano: faida na hasara

| Mbinu ya utawala | Faida | Hasara |
| --- | --- | --- |
| Bodi ya kati ya mapitio kwa yote | Uthabiti na usimamizi wa juu zaidi | Kikwazo kikali; huzuia uwezeshaji wa timu; polepole |
| Barabara iliyotengenezwa yenye uhuru wa mahali | Inapanuka, haraka, chaguo-msingi salama, inawezesha timu | Inahitaji uwekezaji wa awali wa jukwaa; kuteleza nje ya barabara |
| Uhuru kamili wa timu, hakuna utawala | Haraka, umiliki wa juu | Mgawanyiko, kurudiwa, makosa yanayorudiwa |
| ADR / RFC | Kumbukumbu ya kudumu, maamuzi bora, uwazi | Mzigo wa kuandika; hupuuzwa zisipodumishwa |

| Chaguo la chanzo | Faida | Hasara |
| --- | --- | --- |
| Kujenga | Udhibiti kamili, inafaa hasa, inaweza kutofautisha | Gharama ya daima ya matengenezo na wafanyakazi |
| Kununua | Haraka, inasaidiwa, mwingine anaidumisha | Gharama ya leseni, kufungwa, inafaa kwa kutokamilika |
| Kupokea (chanzo huria) | Hakuna ada ya leseni, inaweza kukaguliwa, jamii | Mzigo wa msaada na usalama unakuangukia |

Mabadilishano ya kuunganisha ni udhibiti dhidi ya kasi, na uthabiti wa kati dhidi ya uhuru wa mahali. Kila chaguo la utawala liko kwenye wigo huu. Msimamo unaopendekezwa, barabara zilizotengenezwa pamoja na kukasimu kwa msingi wa uwezekano wa kutenduliwa, hununua kwa makusudi kasi nyingi ya uhuru huku ukihifadhi uthabiti unaojalisha. Hufanya hivyo kwa kufanya chaguo lililopangiliwa kuwa rahisi, na kuhifadhi mchakato mzito kwa uamuzi nadra usioweza kutenduliwa.

## Maswali ya kujadili na timu yako

1. **Nani anaamua kama uamuzi fulani ni mlango wa upande mmoja, na utanasaje makosa ya uainishaji katika pande zote mbili?** Kuainisha maamuzi kwa uwezekano wa kutenduliwa ni mojawapo ya mazoea ya utawala yenye kiegemeo kikubwa zaidi, na thamani yake huporomoka ukiweka lebo vibaya: ukichukulia uchaguzi unaoweza kutenduliwa kama usioweza, unauzamisha kwa mazingatio, ukichukulia usioweza kutenduliwa kama unaoweza, unatuma mfano wa data au mkataba wa API wa umma usioweza kutenduliwa kwa bei nafuu. Hatari inayoshindana ni kwamba mtu aliye karibu zaidi na kazi anaweza kuelemea kasi, huku bodi ya kati ikielemea tahadhari. Leta mifano madhubuti katika mjadala: itagharimu nini hasa, kwa muda na fedha, kutengua kila uamuzi, na nani anabeba gharama hiyo. Katika mazingira ya mashirika makubwa na ya serikali, ahadi za ununuzi na data kwa ukubwa hugeuza chaguo nyingi kuwa milango ya upande mmoja iliyoonekana inaweza kutenduliwa mwanzoni. Kubaliana nani anaainisha, na ujenge tabia ya maoni ya pili ya haraka juu ya chochote karibu na mpaka, ili uchunguzi adimu utue pale kutengua ni ghali kweli.

2. **Nani anamiliki, kufadhili, na kuajiri kwa barabara iliyotengenezwa, na nini kinazuia isioze kuwa mlinzi wa lango?** Barabara iliyotengenezwa hufanya kazi tu ikiwa chaguo-msingi zilizobarikiwa zinasaidiwa vyema kweli na ni rahisi kuliko mbadala, na hilo linahitaji uwekezaji endelevu ambao ni rahisi kuufadhili kidogo. Mabadilishano ni makali: barabara iliyotengenezwa yenye rasilimali pungufu inakuwa seti ya maagizo bila msaada, ambayo ndiyo hasa kulinda lango ambako mfano ulikusudiwa kuchukua nafasi yake, na timu kisha huizunguka. Leta ushahidi wa afya ya barabara: viwango vya kupokelewa, jinsi zana zilizoidhinishwa zilivyo za sasa, jinsi timu ya jukwaa inavyojibu haraka, na mara ngapi timu zinaomba kwenda nje ya barabara. Kwa mashirika makubwa na yanayodhibitiwa, barabara iliyotengenezwa pia ndivyo uchaguzi unaozingatia kanuni unavyokuwa rahisi, kwa hiyo ufadhili wake ni uwekezaji wa uzingatiaji, si urahisi tu. Amua mmiliki wazi na bajeti ya kudumu, na upime kama timu zinachagua barabara kwa sababu ni njia rahisi zaidi kweli.

3. **Timu zinaizunguka wapi utawala wenu, na IT ya kivuli hiyo inawaambia nini?** Timu huikwepa njia iliyoidhinishwa inapokuwa na maumivu zaidi kuliko njia ya kuzunguka, kwa hiyo IT ya kivuli iliyoenea ni hukumu ya usanifu juu ya utawala wenu kuliko tatizo la nidhamu. Mambo yanayoshindana ni halisi: baadhi ya kukwepa ni kutojali, na mengi ni kuepuka kwa busara bodi ya mapitio iliyogeuka foleni ya wiki kadhaa. Leta ushahidi: ni idhini zipi zinaruka, ni zana zipi zisizo rasmi zimeenea kimyakimya, na njia rasmi inachukua muda gani kweli. Katika mazingira ya mashirika makubwa na ya serikali dau ni la juu zaidi, kwa sababu zana zisizoidhinishwa zinaweza kukiuka wajibu wa ukaguzi, usalama, na ununuzi wenye uzito wa kisheria. Muundo ukionyesha watu wanazunguka kikwazo, suluhisho ni kuharakisha na kupanua barabara iliyotengenezwa na kupunguza wigo wa bodi hadi maamuzi machache yanayovuka maeneo na yasiyoweza kutenduliwa, si kuongeza idhini.

4. **Ni kiasi gani cha uwezo wetu wa utoaji kinaenda kulipa deni la kiufundi, na tunaweza kutaja vipengee vya riba ya juu zaidi ambavyo vinapaswa kulengwa kwanza?** Deni la kiufundi hufanya kazi kama riba inayojumlika, ushuru wa kimya kwa kila badiliko la baadaye, na shirika kubwa linaweza kulibeba kwa miaka kabla mtu hajagundua mfumo umekuwa polepole na dhaifu kubadilisha. Shinikizo linaloshindana ni butu: kila saa inayotumika kwenye deni ni saa isiyotumika kwenye vipengele ambavyo uongozi unaweza kuona, kwa hiyo kulipa ndiko kwanza kunakokatwa tarehe ya mwisho inapobana. Leta ushahidi halisi katika mjadala, orodha iliyoandikwa ya deni muhimu, makadirio ya uaminifu ya gharama endelevu ambayo kila kipengee kinaleta na gharama ya kukirekebisha, na sehemu halisi ya uwezo wa hivi karibuni iliyoenda kulipa dhidi ya kazi mpya. Kwa mashirika makubwa na ya serikali yenye upeo wa muongo, deni lisilosimamiwa hatimaye hulazimisha kuandika upya kwa gharama kubwa au matokeo ya ukaguzi, kwa hiyo chukulia mgao wa kudumu wa kulipa kama usimamizi wa hatari na uamue nani analinda ratiba zinapoteleza.

5. **Tunapohitaji hoja nyuma ya uamuzi uliofanywa miaka miwili iliyopita, tunaweza kuipata kweli, na je, kuna anayeweka rekodi hiyo hai?** Thamani yote ya Rekodi ya Uamuzi wa Usanifu ni kwamba hoja inadumu kuliko watu walioifanya, na thamani hiyo huporomoka ADR zikiandikwa mara moja, hazitafutwi kamwe, na kuteleza kimyakimya kuwa zimepitwa na wakati. Mvutano ni kati ya nidhamu ya kuandika inayochukua kunasa muktadha, chaguo, na matokeo wakati wa uamuzi, na shinikizo la kila siku la kutoa tu na kuendelea. Leta majaribio madhubuti katika mjadala: chagua maamuzi matatu muhimu ya hivi karibuni na uone kama yeyote anaweza kupata hoja iliyorekodiwa ndani ya dakika, na uangalie kama ADR zilizobatilishwa zimewekwa alama hivyo badala ya kupingana kimyakimya na mazoea ya sasa. Katika mazingira ya mashirika makubwa na ya serikali, rekodi hiyo inayotafutika ndiyo hasa ushahidi unaoweza kutetewa ambao wakaguzi na vyombo vya usimamizi vinadai, kwa hiyo amua ADR zinaishi wapi, nani anazipitia, na kinachofanya uamuzi uwe muhimu vya kutosha kurekodiwa.

6. **Lini mara ya mwisho tulifungua tena uamuzi mkubwa wa kujenga-dhidi-ya-kununua dhidi ya dhana zake za awali, na je, tungegundua dhana hizo zinapoisha muda?** Chaguo za chanzo ni miongoni mwa maamuzi ghali zaidi na magumu kutenduliwa unayofanya, na dhana zilizo nyuma yake (bei ya msambazaji, wafanyakazi wako mwenyewe, ukomavu wa chaguo la chanzo huria) huchakaa kimyakimya huku uamuzi ukibaki umeganda mahali pake. Mambo yanayoshindana yanapima gharama iliyozama na usumbufu wa kubadili dhidi ya gharama inayoongezeka ya kufungwa, kufaa kusikokamilika, au mzigo wa matengenezo usioutaka tena. Leta ADR ya awali na dhana zake zilizotajwa, makadirio ya sasa ya jumla ya gharama ya umiliki kwa kila njia ikijumuisha leseni, uunganishaji, wafanyakazi, na gharama ya kutoka, na ishara yoyote, mabadiliko ya bei au kupunguzwa kwa msaada, kwamba msingi umehama. Kwa wanunuzi wa serikali na wanaodhibitiwa, kanuni za ununuzi na mikataba ya miaka mingi hufanya milango hii ya upande mmoja kuwa ya kufunga hasa, kwa hiyo kubaliana mapema vichocheo na ratiba itakayolazimisha uamuzi upya wa makusudi badala ya kuhuisha kwa upofu.

## Mtazamo wa sekta

**Kampuni changa.** Tawala karibu hakuna na utegemee kasi kwa nguvu: kwa chaguo za mlango wa pande mbili zinazoweza kutenduliwa, amua mezani na uendelee. Hifadhi tabia yako moja ya utawala kwa milango michache ya upande mmoja, mfano wa msingi wa data au msambazaji wa msingi, na unase kila moja katika aya moja ili mwenzako wa baadaye asilazimike kuibishana upya kutoka mwanzo. Ruka bodi za mapitio na barabara zilizotengenezwa kabisa, kwa sababu kwa ukubwa wako ni mzigo usioumudu na timu nzima tayari inashiriki muktadha.

**Biashara ndogo.** Bila mbunifu kwenye wafanyakazi, fanya kujenga-dhidi-ya-kununua kuwa swali lako kuu la utawala na ulijibu kwa jumla ya gharama ya umiliki badala ya upendeleo. Chagua kununua au kupokea zana zinazosaidiwa vyema kwa chochote kisicho kitofautishi chako kikuu, kwa sababu matengenezo ya daima ndiyo gharama usiyoweza kuibeba zaidi. Weka kumbukumbu moja nyepesi ya maamuzi ili hoja nyuma ya chaguo zako chache zenye matokeo idumu mtu muhimu akiondoka.

**Biashara kubwa.** Tatizo lako ni kusawazisha uhuru dhidi ya mpangilio kuvuka timu nyingi, kwa hiyo wekeza katika barabara iliyotengenezwa iliyofadhiliwa na uhifadhi bodi finyu, ya haraka ya mapitio ya usanifu kwa maamuzi yanayovuka maeneo na yasiyoweza kutenduliwa kweli. Sawazisha ADR ili hoja iwe kumbukumbu ya kitaasisi inayotafutika, na usimamie deni la kiufundi na chaguo za chanzo kama majalada yenye bajeti za kudumu. Pima kama timu zinachagua barabara kwa sababu ni rahisi zaidi, na upunguze bodi yoyote iliyooza kuwa foleni.

**Serikali.** Maamuzi yaliyoandikwa, yanayoweza kutetewa si ya hiari hapa: wakaguzi na vyombo vya usimamizi vinatarajia kuona hoja, chaguo zilizopimwa, na dhana nyuma ya kila uchaguzi wenye matokeo. Endesha kujenga-dhidi-ya-kununua kama uchambuzi wa jumla ya gharama ya umiliki ulioandikwa, heshimu kanuni za ununuzi zinazozuia kufungwa kwa chanzo kimoja, na weka ADR kama njia ya ushahidi tayari kwa ukaguzi. Chukulia upeo mrefu wa muda kwa uzito, kwa sababu mfano wa data au ahadi ya msambazaji iliyofanywa leo inaweza kulifunga shirika kwa muongo, kwa hiyo iainishe kama mlango wa upande mmoja na uamue ipasavyo.

## Mifano

**Kampuni changa.** Kampuni changa ya watu wanne hufanya maamuzi mengi ndani ya dakika mezani pamoja, na kwa chaguo za mlango wa pande mbili zinazoweza kutenduliwa kasi hiyo ni faida halisi, kwa hiyo wanapinga mzigo wowote wa utawala. Lakini wanapochagua hifadhidata na mfano wa data ambao utakuwa na maumivu kubadilisha baadaye (mlango wa upande mmoja), wanasimama kuandika dokezo la aya moja: chaguo, uchaguzi, na dhana nyuma yake. Mwaka mmoja baadaye, wakigonga mipaka ya ukubwa, dokezo hilo moja linawaokoa kuibishana swali upya kutoka mwanzo. Wanatawala karibu hakuna, na kuhifadhi tabia yao moja nyepesi kwa maamuzi machache ghali kweli kutenduliwa.

**Biashara kubwa.** Timu za jukwaa za biashara kubwa zililemazwa na bodi ya mapitio ya usanifu iliyopaswa kuidhinisha kila uchaguzi wa teknolojia, ikiunda foleni za wiki kadhaa. Biashara ilipanga upya utawala kuzunguka barabara iliyotengenezwa: orodha iliyochaguliwa ya lugha, hifadhi za data, na mabomba yaliyoidhinishwa, yanayosaidiwa kikamilifu ambayo timu zingeweza kupokea mara moja. ADR zilirekodi uamuzi wowote wa kupotoka, na mapitio ya haraka, ya ushauri yalishughulikia chaguo za nje ya barabara pekee. Wigo wa bodi ulipungua hadi kuweka viwango na maamuzi machache ya kuvuka maeneo kweli. Utoaji ulikuwa wa kasi kubwa. Uthabiti kweli uliboreka, kwa sababu njia rahisi sasa ilikuwa ile inayozingatia kanuni. Na kumbukumbu ya ADR ilitoa shirika rekodi inayotafutika ya kwa nini vitu vilijengwa vilivyo.

**Serikali.** Idara ya serikali ilikabiliwa na uamuzi mkubwa wa kujenga-dhidi-ya-kununua kwa jukwaa la usimamizi wa kesi chini ya kanuni kali za ununuzi na ukaguzi. Badala ya kuamua kwa upendeleo, iliendesha uchambuzi ulioandikwa wa jumla ya gharama ya umiliki kuvuka chaguo tatu: kujenga maalumu, kununua bidhaa ya kibiashara, na kupokea msingi wa chanzo huria. Ilipima leseni, uunganishaji, matengenezo ya muda mrefu, wafanyakazi, na kufungwa, na kurekodi uamuzi na dhana zake kama ADR. Miaka baadaye, masharti ya msambazaji yalipobadilika, idara ilipitia upya ADR hiyo, ikagundua dhana zake za awali hazikuwa zikitumika tena, na kuamua upya ikijua hoja ya awali kikamilifu, ikiepuka uhamishaji wa upofu na wa gharama. Hoja iliyorekodiwa pia ilikuwa ushahidi unaoweza kutetewa ambao wakaguzi walihitaji hasa.

## Kesi ya biashara: sababu, ROI, na TCO

Maamuzi ni gharama yenye kiegemeo cha juu zaidi na uonekano wa chini zaidi katika programu. Uchaguzi mmoja mbaya, usioweza kutenduliwa wa usanifu au chanzo unaweza kuleta miaka ya mzigo au urekebishaji wa tarakimu tisa. Kuutawala vizuri, saa chache za mazingatio na rekodi iliyoandikwa, kunagharimu karibu hakuna kwa kulinganisha. Mapato ya ADR na kukasimu kwa msingi wa uwezekano wa kutenduliwa yanatoka vyanzo viwili: kuepuka makosa ghali kwenye maamuzi ya mlango wa upande mmoja, na kuepuka mazingatio yaliyopotea na kurudia kazi kwa kila kitu kingine. Sababu iliyorekodiwa pia hupunguza sana gharama inayojirudia ya kuibishana upya maswali yaliyotatuliwa na ya timu kuchambua nia nyuma ya mifumo iliyorithiwa.

Deni la kiufundi hufanya hoja ya TCO kuwa madhubuti. Deni lisilosimamiwa hufanya kazi hasa kama riba inayojumlika: ushuru unaokua kwa kila badiliko la baadaye, hadi mfumo unakuwa kwa vitendo hauwezi kudumishwa na kudai kuandikwa upya kwa gharama. Kusimamia deni kama jalada, kwa mgao wa kudumu wa uwezo wa kulipa vipengee vya riba ya juu, ni nafuu zaidi sana kuliko mgogoro wa mwisho. Utawala mzuri ni nafuu kupokea, hasa nidhamu ya kuandika maamuzi na uwekezaji wa awali katika barabara iliyotengenezwa. Kuuruka ni ghali: unalipa kwa kuandika upya kunakoweza kuepukika, mshangao wa kufungwa, kushindwa kwa ukaguzi, na kupoteza kumbukumbu ya kitaasisi. Kuwashawishi uongozi, weka utawala kwa lugha yao: kupunguza hatari, kuepuka kurudia kazi, utoaji wa haraka kupitia barabara iliyotengenezwa, na uwezo wa kutetewa tayari kwa ukaguzi. Onyesha kwamba lengo si mchakato zaidi bali mchakato unaolengwa vizuri zaidi, uchunguzi mzito pale tu kutengua ni ghali, na kasi isiyo na msuguano kila mahali pengine.

## Mifumo mibaya na mitego

- Maamuzi yasiyoandikwa: hoja inapotea mara watu walioifanya wanapoondoka.
- Kikwazo cha bodi ya idhini: chombo cha kati ambacho kila mradi lazima ukisubiri kwenye foleni.
- Mchakato wa saizi moja: kulazimisha maamuzi madogo yanayoweza kutenduliwa kupitia mapitio mazito.
- Kupooza kwa uchambuzi: kuhangaikia maamuzi ya mlango wa pande mbili yanayotenduliwa kwa urahisi.
- [IT ya kivuli](https://en.wikipedia.org/wiki/Shadow_IT): timu kukwepa utawala kabisa kwa sababu njia iliyoidhinishwa ina maumivu mengi.
- Deni la kiufundi lisiloonekana: deni lisilowahi kuorodheshwa, kulipwa, likijumlika kimyakimya.
- Silika za kujenga-kila-kitu au kununua-kila-kitu: kuchagua chanzo kwa mazoea badala ya uchambuzi wa TCO.
- Maigizo ya utawala: nyaraka na bodi zilizopo kwa mwonekano lakini hazishawishi maamuzi.

## Kielelezo cha ukomavu

- Ngazi ya 1 (Kuanzisha): Maamuzi ni ya papo hapo na hayarekodiwi; utawala ama haupo au ni kikwazo cha jumla; deni la kiufundi halionekani na hoja nyuma ya chaguo hupotea watu wanapoondoka.
- Ngazi ya 2 (Kuendeleza): Baadhi ya maamuzi huandikwa na baadhi ya mapitio yapo, lakini mazoea hayana uthabiti kuvuka timu na mchakato mara nyingi haulingani na uzito na uwezekano wa kutenduliwa wa uamuzi.
- Ngazi ya 3 (Kusawazisha): ADR, barabara iliyotengenezwa, kukasimu kwa msingi wa uwezekano wa kutenduliwa, na orodha ya deni vimeandikwa na kutekelezwa shirika zima, kwa hiyo uchaguzi unaozingatia kanuni ni chaguo-msingi rahisi na hoja inatafutika.
- Ngazi ya 4 (Kusimamia): Utawala unapimwa dhidi ya vipimo vya msingi: kupokelewa kwa barabara iliyotengenezwa, ufikiaji wa ADR, muda wa mzunguko wa maamuzi, deni kama sehemu ya uwezo, na viwango vya vighairi vya nje ya barabara vinafuatiliwa, na maamuzi ya kulipa deni au kupitia upya chanzo huchochewa na ushahidi huo badala ya mgogoro.
- Ngazi ya 5 (Kuratibu): Utawala unarekebishwa kila wakati na kuunganishwa na mipango ya utoaji na hatari; uchunguzi unalengwa hasa kwenye maamuzi yasiyoweza kutenduliwa; deni na chaguo za chanzo husawazishwa upya kikamilifu kama majalada na kuamuliwa upya kwa ushahidi hali zinapohama.

## Mawazo ya kujadili

- Kwa maamuzi yetu muhimu zaidi ya hivi karibuni, tunaweza kupata hoja iliyorekodiwa nyuma yake?
- Utawala wetu ni kikwazo wapi, na haupo wapi unapohitajika?
- Ni maamuzi gani yetu ya sasa ni milango ya upande mmoja, na je, tunayachukulia hivyo?
- Ni kiasi gani cha uwezo wetu kinaenda kulipa deni la kiufundi, na je, kinatosha?
- Je, timu zetu zinafuata barabara iliyotengenezwa kwa sababu ni njia rahisi zaidi kweli, au zinaizunguka?
- Lini mara ya mwisho tulipitia upya uamuzi mkubwa wa kujenga-dhidi-ya-kununua dhidi ya dhana zake za awali?

## Mambo muhimu ya kukumbuka

- Rekodi maamuzi muhimu na sababu zake kwa ADR; fanya hoja iwe ya kudumu.
- Tawala kupitia barabara zilizotengenezwa na chaguo-msingi, si kulinda lango kwa kesi kwa kesi.
- Linganisha uzito wa mchakato na uzito na uwezekano wa kutenduliwa wa uamuzi; kasimu milango ya pande mbili, fanya mazingatio kwa milango ya upande mmoja.
- Changanua kujenga-dhidi-ya-kununua-dhidi-ya-kupokea kwa jumla ya gharama ya umiliki, na urekodi dhana.
- Simamia deni la kiufundi kama jalada wazi lenye mgao wa kudumu wa kulipa.
- Weka utawala wazi na mwepesi; lenga uchunguzi adimu pale kutengua ni ghali.

## Marejeo na usomaji zaidi

- Michael Nygard, "Documenting Architecture Decisions" (the original ADR pattern)
- Gregor Hohpe, "The Software Architect Elevator" and "37 Things One Architect Knows"
- Amazon shareholder letters on Type 1 vs Type 2 (one-way vs two-way door) decisions
- Ward Cunningham, the original "technical debt" metaphor
- Martin Fowler, writings on technical debt and evolutionary architecture
- Neal Ford, Rebecca Parsons, Patrick Kua, "Building Evolutionary Architectures"
- Nicole Forsgren, Jez Humble, Gene Kim, "Accelerate" (loosely coupled architecture and autonomy)
- ISO/IEC/IEEE 42010 on architecture description
