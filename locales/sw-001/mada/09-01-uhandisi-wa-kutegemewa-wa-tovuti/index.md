# 9.1 Uhandisi wa kutegemewa wa tovuti

## Muhtasari na msukumo

[Uhandisi wa kutegemewa wa tovuti](https://en.wikipedia.org/wiki/Site_reliability_engineering) (SRE) hutumia mazoea ya uhandisi wa programu kuendesha mifumo ya uzalishaji. Badala ya kuchukulia operesheni kama kazi ya mkono inayoendeshwa na tiketi, iliyotengwa na uundaji, SRE huchukulia kutegemewa kama tatizo la kihandisi unalolitatua kwa msimbo, upimaji, na malengo wazi ya huduma. Wazo kuu, lililoenezwa na Google lakini sasa limeenea, ni rahisi: watu wanaoweka mifumo ikiendesha wanapaswa kutumia muda wao mwingi kujenga uotomatishaji na kuboresha mifumo, si kuzima moto wa kushindwa kuleule kwa mkono tena na tena.

Kwa timu kubwa, hili ni muhimu kwa sababu ukubwa huongeza thamani ya kutegemewa na gharama ya kukosea. Huduma moja inaposaidia mamilioni ya watumiaji au maelfu ya watumiaji wa ndani, saa moja ya kukatika inamaanisha mapato yaliyopotea, miamala iliyokosa, na uaminifu uliomomonyoka. Operesheni za mkono zinazofanya kazi vizuri kwa seva chache huanguka chini ya mamia ya huduma na [usambazaji endelevu](https://en.wikipedia.org/wiki/Continuous_deployment). SRE inakupa lugha ya pamoja kwa kutegemewa, njia ya kufanya mabadilishano kati ya kusafirisha vipengele na kuweka mambo thabiti yawe wazi, na njia ya kushikilia mstari huo kwa uthabiti kuvuka timu nyingi.

Mazingira ya mashirika makubwa na serikali huongeza uzito zaidi. Sekta zinazodhibitiwa kama benki, afya, na huduma za umma mara nyingi hubeba ahadi za kisheria au za kimkataba za upatikanaji, mahitaji ya ukaguzi, na uvumilivu mdogo kwa kukatika kunakoathiri raia au usalama. Huduma za kidijitali za serikali zinazidi kuchapisha malengo yao ya kutegemewa na data ya utendaji wazi. SRE inakupa njia makini, inayotegemea ushahidi ya kufafanua "inategemewa vya kutosha" inamaanisha nini, kuipima kwa uaminifu, na kutetea vipaumbele vya kihandisi kwa uongozi na vyombo vya usimamizi kwa data badala ya maoni.

*Tazama pia:* sura ya 9.2 (uonekanaji na ufuatiliaji), sura ya 9.3 (usimamizi wa matukio), na sura ya 3.5 (kupanuka, utendaji, na ustahimilivu).

## Kanuni kuu

- **Kutegemewa ndicho kipengele muhimu zaidi.** Mfumo usiofanya kazi hauna thamani bila kujali una vipengele vingapi, lakini kutegemewa kamili hakuwezekani wala hakustahili gharama yake.
- **Fafanua kutegemewa kwa malengo yanayopimika.** Viashiria vya kiwango cha huduma (SLI), malengo (SLO), na makubaliano (SLA) hugeuza matarajio hafifu kuwa namba ambazo kila mtu anaweza kukubaliana.
- **Asilimia 100 ni lengo lisilo sahihi.** Watumiaji hawawezi kutofautisha kati ya mfumo unaotegemewa sana na ule unaotegemewa kikamilifu, kwa hiyo lenga "kutegemewa vya kutosha" na utumie bajeti iliyobaki kwa kasi.
- **Bajeti za makosa huoanisha motisha.** Pengo kati ya SLO na asilimia 100 ni bajeti ya hatari ambayo wasanidi na waendeshaji hushiriki, ikibadilisha mabishano na hesabu.
- **Kazi ya kuchosha ndiyo adui.** Kazi ya uendeshaji inayojirudia, ya mkono, inayoweza kuotomatishwa inapaswa kupimwa, kuwekewa kikomo, na kuondolewa kimfumo.
- **Otomatisha kwa makusudi.** Uotomatishaji ndio jinsi timu ndogo inavyoendesha mfumo mkubwa; kuwekeza ndani yake ni shughuli ya kihandisi ya daraja la kwanza.
- **Kujifunza bila lawama.** Kushindwa kunachukuliwa kama fursa za kuboresha mifumo na michakato, si kuwaadhibu watu binafsi.

## Mapendekezo

### Fafanua SLI, SLO, na SLA kwa makusudi

Anza kutoka mtazamo wa mtumiaji. **[Kiashiria cha kiwango cha huduma](https://en.wikipedia.org/wiki/Service-level_indicator)** ni kipimo cha kiasi cha tabia ya huduma, kama sehemu ya maombi yaliyohudumiwa chini ya milisekunde 300 au sehemu ya majibu yenye mafanikio. Chagua idadi ndogo ya SLI zinazoakisi furaha ya mtumiaji kweli: upatikanaji, ucheleweshaji, usahihi, na uchangamfu ni za kawaida. **[Lengo la kiwango cha huduma](https://en.wikipedia.org/wiki/Service-level_objective)** ni thamani lengwa au safu ya SLI, kwa mfano "asilimia 99.9 ya maombi yanafanikiwa kwa dirisha linaloviringika la siku 28." **[Makubaliano ya kiwango cha huduma](https://en.wikipedia.org/wiki/Service-level_agreement)** ni mkataba wenye matokeo (marejesho, adhabu) yaliyoambatishwa na kiwango kilichoahidiwa. Weka SLO zako kuwa kali kuliko SLA zako, ili upate onyo kabla ya kuvunja ahadi. Chapisha SLO zako, zipitie kila robo mwaka, na uzichukulie kama nyaraka hai zinazobana au kulegea unavyojifunza.

### Pokea bajeti za makosa na uzitekeleze

Bajeti ya makosa ni `100% toa SLO`. Ikiwa SLO yako ni asilimia 99.9, bajeti yako ni asilimia 0.1 ya kutokutegemewa kwa kila dirisha, takriban dakika 43 kwa mwezi. Itumie kwa hatari iliyopangwa: matoleo makali, majaribio, na majaribio ya kushindwa yaliyodhibitiwa. Bajeti ikiwa na afya, timu zinaweza kusafirisha haraka. Ikiisha, sera inapaswa kuhamisha vipaumbele kiotomatiki kuelekea kazi ya kutegemewa na kusitisha mabadiliko hatari hadi mfumo upone. Nguvu ya bajeti ya makosa ni kwamba mnakubaliana nayo mapema, kwa hiyo inaondoa hisia na siasa kutoka wakati wa kukatika.

### Pima na punguza kazi ya kuchosha

Kazi ya kuchosha ni kazi ya uendeshaji iliyo ya mkono, inayojirudia, inayoweza kuotomatishwa, ya kimbinu, na inayokua sambamba na mfumo. Fuatilia asilimia ya muda wa SRE inayotumika kwa kazi ya kuchosha na uweke kikomo, kwa kawaida karibu asilimia 50, ili angalau nusu ya muda wako wa kihandisi uende kwenye maboresho ya kudumu. Weka mrundikano wa miradi ya kupunguza kazi ya kuchosha, ipe kipaumbele kwa mzunguko mara gharama, na usherehekee kuua kazi inayojirudia kama unavyosherehekea kusafirisha kipengele kipya. **Agizo la uotomatishaji** hufanya hili kuwa wazi: utaratibu wowote wa mkono unaoufanya zaidi ya idadi iliyowekwa ya mara unakuwa mgombea wa uotomatishaji au zana ya kujihudumia.

### Panga uwezo na tabiri mahitaji

Unda kielelezo cha mzigo unaotarajiwa kutoka mienendo ya kihistoria, uzinduzi uliopangwa, na makadirio ya biashara. Unganisha makadirio ya ukuaji wa asili na matukio ya mara moja kama kampeni za uuzaji, tarehe za mwisho za kodi, au vipindi vya usajili wa mafao vinavyojali sana serikalini. Weka nafasi ya ziada juu ya kilele, jaribu mzigo kuangalia dhana zako, na otomatisha kupanuka unapoweza huku ukiweka [mpango wa uwezo](https://en.wikipedia.org/wiki/Capacity_planning) uliopitiwa na binadamu kwa ahadi kubwa. Fuatilia muda wa kuongoza wa utayarishaji ili upungufu usikushtue kamwe.

### Chukulia kutegemewa kama kipengele chenye gharama halisi

Kila "tisa" ya ziada ya upatikanaji kwa kawaida hugharimu zaidi sana katika urudufu, majaribio, na ustadi wa uendeshaji kuliko ile iliyotangulia. Fanya gharama ya tisa iwe wazi, ili wamiliki wa bidhaa wachague lengo kwa macho wazi. Sanifu kwa kushuka kwa upole, ili kushindwa kwa sehemu kutoe huduma iliyopunguzwa badala ya kukatika kamili. Wekeza kwenye urudufu na kuhamisha kwa kushindwa sawia na SLO, si kwa usawa kuvuka kila kijenzi.

### Chagua mfano wa kimuundo wa SRE

Hakuna muundo mmoja sahihi. Timu ya SRE ya **kati** inakupa uthabiti, utaalamu wa kina, na zana za pamoja, lakini inaweza kuwa kizuizi au jalala la matatizo ya wengine. Mfano wa **kupachikwa** huweka SRE ndani ya timu za bidhaa kwa ushirikiano wa karibu, lakini unahatarisha kutokuwa na uthabiti na kutengwa. Mashirika mengi makubwa hutumia mseto: jukwaa la kati na kikundi cha viwango pamoja na wahandisi wa kutegemewa waliopachikwa, wenye mfano wazi wa ushirikishaji unaofafanua lini huduma inastahili msaada wa SRE na kiwango gani cha utayari wa uzalishaji lazima ivuke kwanza.

## Mabadilishano: faida na hasara

| Uamuzi | Faida | Hasara |
|---|---|---|
| SLO kali (tisa zaidi) | Uaminifu wa juu wa mtumiaji, inatimiza mikataba | Gharama inayopanda, utoaji wa vipengele wa polepole |
| SLO legevu (tisa chache) | Kusafirisha haraka, gharama ndogo | Hatari ya watumiaji kuondoka na adhabu za SLA |
| SRE ya kati | Uthabiti, utaalamu wa pamoja | Vizuizi, umbali kutoka bidhaa |
| SRE iliyopachikwa | Ushirikiano wa karibu, muktadha | Kutokuwa na uthabiti, ngumu kuajiri |
| Uwekezaji mzito wa uotomatishaji | Inapanuka, inapunguza kazi ya kuchosha | Gharama ya awali, uotomatishaji wenyewe unaweza kushindwa |

Uhandisi wa kutegemewa kwa kweli ni kutumia rasilimali finyu kwa busara. Kufukuzia tisa ya ziada ambayo watumiaji hawawezi hata kuiona kunapoteza fedha ambazo zingefadhili vipengele au kupunguza bei. Ukienda upande mwingine na kuwekeza kidogo mno kwenye mfumo ambao kushindwa kwake kunasababisha madhara halisi, huo ni uzembe. Mfumo wa bajeti ya makosa upo hasa kufanya mabadilishano haya yaonekane na yaweze kujadiliwa badala ya kuwa ya kimya na ya mzozo. Mabadilishano ya mfano wa kimuundo ni ya kweli vilevile: jibu sahihi linategemea ukubwa wa kampuni, ukomavu wa kihandisi, na jinsi huduma zenu zinavyofanana.

## Maswali ya kujadili na timu yako

1. **SLI ipi hasa inaakisi kile watumiaji wenu wanachohisi kweli, na mnaweza kuonyesha si kipimo cha mapambo?** Chagua kiashiria kisicho sahihi na kila dashibodi inaonekana ya kijani huku watumiaji wanateseka, ambao ni mtego wa SLI ya mapambo ambao sura hii inaonya. Leta data halisi kwenye mjadala: pima safari ileile ya mtumiaji kutoka njia halisi ya ombi (kuingia hadi dashibodi, malipo hadi uthibitisho) badala ya CPU ya seva au ukaguzi wa afya wa nyuma. Kwa timu kubwa, SLI moja mbaya inaenea: makumi ya huduma huirithi, tahadhari zinawaka kwa kitu kisicho sahihi, na bajeti ya makosa inaacha kuwa na maana. Katika mazingira ya mashirika makubwa na serikali ambapo SLA hubeba marejesho au athari kwa raia, SLI yenu ni ushahidi mnaoutetea kwa wakaguzi, kwa hiyo lazima ifuatilike moja kwa moja hadi mafanikio yanayoonekana kwa mtumiaji. Ikiwa huwezi kuchora mstari kutoka namba hadi uzoefu wa mtumiaji, badilisha namba.

2. **Huduma lazima ithibitishe nini kabla timu yenu ya SRE kuipokea kwenye simu ya dharura, na nani anasema hapana?** Bila kiwango cha utayari wa uzalishaji, timu ya kati ya SRE inakuwa jalala la kila huduma isiyo thabiti na kuzama kwenye deni la kiufundi la wengine. Andika vigezo vya kuingia: SLO inayomilikiwa, vitabu vya mwongozo vinavyofanya kazi, tahadhari zinazotekelezeka, nafasi ya uwezo, na njia iliyoonyeshwa ya kusambaza-na-kurudisha-nyuma. Kwa shirika kubwa mfano huu wa ushirikishaji ndio unaoizuia timu ya kutegemewa kuwa kizuizi kinachopunguza kasi ya kila mtu. Katika mazingira yanayodhibitiwa mapitio ya utayari yanafanya kazi pia kama kidhibiti mnachoweza kuvionyesha vyombo vya usimamizi. Amua nani ana mamlaka ya kukataa kupokea, kwa sababu kiwango ambacho hakuna anayekitekeleza si kiwango, na jibu hubadilisha kama SRE inapanuka au inaanguka chini ya maumivu ya kurithi.

3. **Mnatayarisha mapema kwa muda gani kabla ya kilele chenu kikubwa zaidi kinachotabirika, na mnajua muda wenu wa kuongoza wa utayarishaji?** Kudhania unyumbulifu wa wingu ni wa papo hapo na usio na kikomo kunaalika upungufu wakati wa vilele vinavyojali zaidi, na vilele hivyo (tarehe za mwisho za kodi, madirisha ya usajili, matukio ya mauzo) ndio nyakati ambapo kushindwa kunaonekana zaidi na kugharimu zaidi. Leta namba: mzigo wa kilele wa kihistoria, ukuaji uliotabiriwa, kizidisho mnachojaribu mzigo hadi, na muda halisi wa kuongoza wa kupata uwezo mkubwa uliohifadhiwa au mifano maalumu. Kwa huduma za msimu za serikali kilele kinaweza kuwa mara kadhaa ya mzigo wa kawaida na hakiwezi kukosekana kisiasa, kwa hiyo kutayarisha mapema wiki kadhaa kabla ni bora kuliko kutumaini kupanuka kiotomatiki kunaendana. Jibu linapaswa kuweka kalenda halisi: lini mnajaribu mzigo, lini mnafunga uwezo, na nani anamiliki uamuzi wa kwenda.

4. **Bajeti yenu ya makosa ikiisha, nini kinatokea kweli, na nani ana hadhi ya kuitekeleza?** Bajeti ya makosa ambayo haitendewi kazi inapoisha ni pambo tu, na wakati wa kukatika ndio wakati mbaya zaidi wa kujadili sera upya kuanzia mwanzo. Mvuto unaoshindana ni halisi: uzinduzi uliokubaliwa, tarehe ya mwisho ya mapato, au tangazo la umma vitasukuma kwa nguvu dhidi ya kufungia mabadiliko hatari. Leta data ya kasi ya kuteketeza, maandishi ya sera yaliyokubaliwa mapema, na rekodi ya mara chache zilizopita bajeti ilipovunjwa, ili muone kama kufungia kulishikilia kweli. Kwa timu kubwa bajeti huoanisha motisha tu ikiwa kila kikundi kinarithi utekelezaji ule ule, kwa hiyo amua mapema nani anaidhinisha kubatilisha na jinsi ubaguzi huo unavyoandikwa. Katika mazingira ya mashirika makubwa na serikali ambapo SLA hubeba adhabu au athari kwa raia, nyayo za kubatilisha zinakuwa mabaki ya ukaguzi, kwa hiyo taja mmiliki anayewajibika sasa badala ya kubuni bajeti ikishapotea.

5. **Ni sehemu gani ya wiki ya timu yenu ya SRE ni kazi ya kuchosha, na je, hiyo ni namba iliyopimwa au hisia?** Kazi ya kuchosha ambayo hakuna anayeihesabu hupanuka kimyakimya hadi timu inatumia muda wake wote kuzima moto na hakuna kujenga maboresho ya kudumu, hasa mtego ambao SRE ipo kuukwepa. Mvutano ni kwamba kupima kazi ya kuchosha ni kazi yenyewe, na wahandisi walio chini ya shinikizo la tarehe ya mwisho hupinga kuandika masaa yao yanaenda wapi. Leta sampuli ya uaminifu: wiki moja au mbili za muda uliofuatiliwa dhidi ya fasili ya pamoja ya kazi ya kuchosha (ya mkono, inayojirudia, inayoweza kuotomatishwa, ya kimbinu, na inayopanuka na mfumo), pamoja na mrundikano wa miradi ya uotomatishaji iliyopangwa kwa mzunguko mara gharama. Kwa shirika kubwa kikomo cha asilimia 50 kina maana tu ikiripotiwa na kutetewa timu kwa timu, kwa hiyo kubaliani nani anapitia namba na nini kinatokea timu inapoivunja. Katika mazingira ya serikali na yanayodhibitiwa, kuweka kikomo cha kazi ya kuchosha kunaachia wataalamu adimu kwa kazi ya vidhibiti na ukaguzi ambayo operesheni za mkono hubana, kwa hiyo chukulia kielelezo cha kazi ya kuchosha kama ishara ya uwezo ambayo uongozi unapaswa kuiona.

6. **Mnatumia mfano gani wa kimuundo wa SRE, na ni ushahidi gani ungewaambia umeacha kufaa?** Timu ya kati inatoa uthabiti na zana za pamoja lakini inaweza kuwa kizuizi; mfano uliopachikwa unatoa muktadha lakini unateleza kuelekea kutokuwa na uthabiti; mseto ambao mashirika mengi makubwa huishia nao unahitaji mfano wazi wa ushirikishaji la sivyo unarithi udhaifu wa yote mawili. Leta ishara zinazofichua mkazo: huduma zinasubiri kwa muda gani msaada wa SRE, mazoea ya kutegemewa yanatofautiana kiasi gani kati ya timu, na kama wahandisi waliopachikwa wanahisi wametengwa na jumuiya ya kitaaluma. Jibu sahihi linategemea ukubwa wa kampuni, ukomavu wa kihandisi, na jinsi huduma zenu zinavyofanana, kwa hiyo lipitie hayo yanapobadilika badala ya kuchukulia uchaguzi wa kwanza kama wa kudumu. Kwa taasisi ya shirika kubwa au serikali yenye timu nyingi na mahitaji makali ya usawa, kikundi cha kati cha viwango-na-jukwaa pamoja na wahandisi wa kutegemewa waliopachikwa kwa kawaida husawazisha uthabiti dhidi ya muktadha wa ndani, lakini tu ikiwa mfano wa ushirikishaji na kiwango cha utayari wa uzalishaji vimeandikwa na mtu anavimiliki.

## Mtazamo wa sekta

**Kampuni changa.** Ukiwa na wahandisi wachache na bila muda wa ziada kwa timu maalumu ya kutegemewa, chagua SLO moja kwenye safari ya mtumiaji inayojali zaidi na ushiriki simu ya dharura kuvuka timu nzima. Egemea huduma zinazosimamiwa za mtoa huduma wako wa wingu na ufuatiliaji uliojengwa ndani badala ya kujenga miundombinu ya uonekanaji, na uandike uchambuzi mfupi wa baada ya tukio kwenye waraka wa pamoja ili marekebisho yashikamane. Kasi ni muhimu zaidi ya mchakato hapa: SLO legevu unayoitekeleza kweli inashinda ile ya kina ambayo hakuna anayeitazama.

**Biashara ndogo.** Bila mtaalamu wa kuendesha kutegemewa, ichukulie kama nidhamu unayoinunua kupitia jukwaa lako: ufuatiliaji wa muda wa kufanya kazi uliopangishwa, hifadhidata zinazosimamiwa, na zana za ukurasa wa hali badala ya mrundikano wa kipekee. Weka SLO moja au mbili zilizofungwa kwa miamala inayolipa bili, na uamue kwa uaminifu kushindwa gani kungekugharimu mteja. Nunua ustahimilivu pale ambapo ni nafuu kuliko kujenga, na uweke mzigo wa uendeshaji mwepesi vya kutosha ili wahandisi wako waliopo waubebe kando ya kazi ya vipengele.

**Biashara kubwa.** Changamoto ni uthabiti kuvuka timu nyingi: msamiati wa pamoja wa SLO, sera ya pamoja ya bajeti ya makosa, na kiwango cha utayari wa uzalishaji ambacho kila huduma inavuka kabla SRE kuipokea kwenye simu ya dharura. Kikundi cha kati cha jukwaa-na-viwango pamoja na wahandisi wa kutegemewa waliopachikwa huweka mazoea sawa bila kuwa kizuizi, na utawala unahitaji bajeti za makosa ziripotiwe na kutekelezwa kwa njia ileile kila mahali. Weka bajeti wazi ya miundombinu ya uonekanaji na uwekezaji wa uotomatishaji, na usimamie kutegemewa kama jalada lenye vipimo ambavyo uongozi unaweza kuviona.

**Serikali.** Huduma za umma mara nyingi hubeba malengo ya upatikanaji yaliyochapishwa, ahadi za kisheria, na wajibu wa ukaguzi, kwa hiyo SLO na maamuzi ya bajeti ya makosa huwa rekodi unazotetea kwa vyombo vya usimamizi. Kanuni za ununuzi zinaweza kubana ufuatiliaji na upangishaji unaoweza kutumia, na matarajio ya uwazi yanakusukuma kuchapisha data ya kutegemewa kwenye dashibodi ya hali ya umma. Panga vilele vikali vya msimu kama tarehe za mwisho za kodi na madirisha ya usajili wa mafao wiki kadhaa mapema, na uweke utamaduni wa uchambuzi wa baada ya tukio usio na lawama ili kushindwa kwa umma kuendeshe uboreshaji wa mfumo badala ya lawama za mtu binafsi.

## Mifano

**Kampuni changa.** Kampuni changa ya watu kumi inaendesha programu moja ya wavuti na kushiriki simu ya dharura kuvuka wahandisi watatu. Badala ya kujenga timu ya kutegemewa isiyoimudu, inachagua SLO moja yenye maana: mafanikio ya asilimia 99.5 kwenye mtiririko wa kuingia-hadi-dashibodi, yaliyopimwa kutoka maombi halisi ya watumiaji. API ya mtu wa tatu isiyotegemewa inapoanza kula bajeti hiyo, timu inatumia Ijumaa kuongeza jaribio tena na kache badala ya kusafirisha kipengele kinachofuata, kisha inaandika uchambuzi wa baada ya tukio wa aya mbili kwenye waraka wa pamoja ili marekebisho yashikamane.

**Biashara kubwa.** Kampuni ya malipo ya kimataifa inaweka SLO ya upatikanaji ya asilimia 99.99 kwa API yake ya miamala, inayotoa bajeti ya makosa ya takriban dakika nne kwa mwezi. Timu ya kati ya jukwaa la SRE inamiliki [uonekanaji](https://en.wikipedia.org/wiki/Observability_(software)) wa pamoja, zana za matukio, na sera ya bajeti ya makosa, huku wahandisi wa kutegemewa waliopachikwa wakifanya kazi ndani ya kila kikundi cha bidhaa. Kipengele kipya cha kugundua ulaghai kinapoteketeza nusu ya bajeti ya mwezi ndani ya wiki, sera iliyokubaliwa mapema inafungia matoleo yasiyo muhimu hadi kazi ya kutegemewa irejeshe nafasi ya ziada. Watendaji wanakubali hili bila mjadala, kwa sababu waliidhinisha sera mapema.

**Serikali.** Mamlaka ya kitaifa ya kodi inaendesha huduma ya kuwasilisha marejesho mtandaoni yenye vilele vikali vya msimu karibu na tarehe ya mwisho ya kila mwaka. Timu yake ya SRE inatabiri mahitaji kutoka miaka ya awali pamoja na mabadiliko ya idadi ya watu na sera, inajaribu mzigo hadi mara kadhaa ya kilele cha kawaida, na kutayarisha uwezo wiki kadhaa mapema. SLO zinazowakabili umma kwa upatikanaji na ucheleweshaji wa kurasa zinawekwa kwenye dashibodi ya hali. Utamaduni wa [uchambuzi wa baada ya tukio](https://en.wikipedia.org/wiki/Postmortem_documentation) usio na lawama (kupitia kushindwa kuboresha mifumo badala ya kugawa lawama kwa mtu binafsi) na agizo la uotomatishaji hupunguza hatua kwa hatua uingiliaji wa mkono uliowahi kutawala msimu wa kuwasilisha, ukiwaachia wafanyakazi kuboresha mfumo badala ya kuulea kupitia kila tarehe ya mwisho.

## Kesi ya biashara: sababu, ROI, na TCO

Faida ya SRE inatoka vyanzo vitatu: kukatika kulikoepukwa, kazi ndogo ya uendeshaji, na utoaji salama wa haraka zaidi. Kukatika kwa huduma kubwa kunaweza kugharimu maelfu hadi mamilioni kwa saa katika mapato yaliyopotea, adhabu, na urekebishaji, kwa hiyo hata mafanikio madogo ya kutegemewa hulipia timu haraka. Kupunguza kazi ya kuchosha hubadilisha gharama ya mkono inayojirudia kuwa uwekezaji wa mara moja wa uotomatishaji, kwa hiyo jumla ya gharama ya umiliki inashuka ukubwa unavyokua badala ya kupanda sambamba nao. Bajeti za makosa huiruhusu biashara kusafirisha haraka kutegemewa kukiwa na afya, ikinasa thamani ya vipengele ambayo operesheni za tahadhari kupita kiasi zingeiacha mezani.

Gharama ya kupokea ni halisi. SRE inahitaji wahandisi wenye ujuzi, miundombinu ya uonekanaji, na mabadiliko ya kitamaduni yanayoshindana na tarehe za mwisho za vipengele. Lakini gharama ya kutopokea ni kubwa zaidi kwa ukubwa: idadi ya wafanyakazi wa uendeshaji isiyo na mipaka, kukatika kusikotabirika, wafanyakazi kuchoka na kuondoka, na uharibifu wa sifa ambao ni mgumu kupimwa lakini rahisi kuteseka nao. Kutoa hoja kwa uongozi, weka SRE kama usimamizi wa hatari wenye faida zinazopimika. Wasilisha gharama ya sasa ya matukio na operesheni za mkono, malengo ya SLO yaliyofungwa kwa ahadi za biashara, na upungufu uliokadiriwa wa yote mawili. Weka hoja kwenye bajeti ya makosa kama chombo cha utawala kinachowapa viongozi kiguzo juu ya mabadilishano ya kutegemewa-dhidi-ya-kasi.

## Mifumo mibaya na mitego

- **SRE kama operesheni zilizobadilishwa jina.** Kubadilisha jina la timu ya uendeshaji bila muda wa kihandisi, agizo la uotomatishaji, na mamlaka ya kupinga hakubadilishi chochote.
- **Kulenga asilimia 100.** Kufukuzia kutegemewa kamili kunapoteza fedha na kuzuia utoaji kwa faida ambazo watumiaji hawawezi kuziona.
- **SLI za mapambo.** Kupima CPU ya seva badala ya mafanikio yanayoonekana kwa mtumiaji kunatoa namba zinazoonekana nzuri huku watumiaji wanateseka.
- **Bajeti za makosa zisizo na meno.** Bajeti isiyotekelezwa inapoisha ni pambo tu.
- **Kazi ya kuchosha bila kupimwa.** Usipoifuatilia, kazi ya kuchosha inameza timu kimyakimya hadi hakuna kazi ya maboresho inayofanyika.
- **SRE kama jalala.** Timu za kati zinazorithi kila huduma isiyo thabiti bila kiwango cha utayari huzama kwenye deni la kiufundi la wengine.
- **Kupuuza muda wa kuongoza wa uwezo.** Kudhania unyumbulifu wa wingu ni wa papo hapo na usio na kikomo kunaalika upungufu wakati wa vilele vinavyojali zaidi.

## Kielelezo cha ukomavu

**Ngazi ya 1, Kuanzisha.** Operesheni ni za mkono na za kuitikia. Hakuna SLO rasmi, kutegemewa ni suala la maoni, na matukio yaleyale yanajirudia huku kuzima moto kunatawala. Uotomatishaji wowote ni wa bahati, na hakuna anayemiliki kutegemewa kama wasiwasi wa kihandisi.

**Ngazi ya 2, Kuendeleza.** Baadhi ya huduma zina SLI na SLO za msingi na ufuatiliaji na tahadhari za awali, lakini mazoea yanatofautiana sana kati ya timu. Kazi ya kuchosha inakubaliwa lakini haipimwi, uotomatishaji ni wa papo hapo, na uchambuzi wa baada ya tukio unafanyika bila uthabiti. Kutegemewa kunaboreka katika mifuko ambapo watu binafsi wanalisukuma, si kwa sababu shirika linalitaka.

**Ngazi ya 3, Kusawazisha.** SLI, SLO, na sera ya bajeti ya makosa zimeandikwa na kutumika kwa uthabiti kuvuka timu. Kazi ya kuchosha imefafanuliwa na kufuatiliwa, upangaji wa uwezo ni wa kawaida, mfano wa ushirikishaji wa SRE wenye mapitio ya utayari wa uzalishaji upo, na uotomatishaji ni mkondo wa kazi uliofadhiliwa badala ya mradi wa pembeni. Mazoea ya kutegemewa yameandikwa na kutekelezwa kote shirikani.

**Ngazi ya 4, Kusimamia.** Programu ya kutegemewa inapimwa na kudhibitiwa kwa data dhidi ya vipimo vya msingi. Kasi ya kuteketeza bajeti ya makosa, asilimia ya kazi ya kuchosha, mafanikio ya SLO, muda wa wastani wa kupona, na muda wa kuongoza wa utayarishaji vinafuatiliwa kama vipimo, vinapitiwa kwa mzunguko uliowekwa, na kutumika kushikilia timu kwenye malengo yao. Ukiukaji wa bajeti unachochea kufungia kulikokubaliwa, uwezo unatabiriwa dhidi ya mifano ya mahitaji, na kila uamuzi wa kwenda au kutokwenda unasimama juu ya ushahidi badala ya maoni.

**Ngazi ya 5, Kuratibu.** Uhandisi wa kutegemewa umeunganishwa kuvuka shirika na unaboreshwa mfululizo. Sera ya bajeti ya makosa imeotomatishwa na inaheshimiwa kila mahali, operesheni nyingi ni za kujihudumia, uwezo unatayarishwa kwa uchangamfu, na data ya kutegemewa inaendesha mabadilishano yanayojirekebisha kati ya kasi na uthabiti. Shirika kwa kawaida linarekebisha wigo wa SLO, linastaafisha kazi ya kuchosha, na kusawazisha upya uwekezaji wa kutegemewa picha ya biashara na hatari inapohama.

## Mawazo ya kujadili

- Shirika linapaswa kuweka SLO zake za kwanza vipi lisipokuwa na data ya kihistoria ya kutegemewa ya kuzitegemeza?
- Bajeti ya makosa ikiwa imeisha lakini uzinduzi mkubwa umekubaliwa, nani ana mamlaka ya kubatilisha kufungia, na uamuzi huo unarekodiwa vipi?
- Mfano wa SRE wa kati, uliopachikwa, au mseto ni sahihi kwa shirika lenu, na nini kingechochea mabadiliko?
- Mnathaminije tisa ya ziada ya upatikanaji dhidi ya vipengele ambavyo uwekezaji uleule ungefadhili?
- Nini kinahesabika kama kazi ya kuchosha katika muktadha wenu, na mstari uko wapi kati ya hukumu ya mkono yenye thamani na kujirudia kunakoweza kuondolewa?
- Malengo ya kutegemewa yanapaswa kutofautianaje kati ya huduma za serikali zinazowakabili raia na zana za ndani za biashara kubwa?

## Mambo muhimu ya kukumbuka

- SRE hutumia uhandisi wa programu kwenye operesheni, ikichukulia kutegemewa kama kipengele kinachopimika, kinachoweza kufadhiliwa.
- SLI, SLO, na SLA hugeuza kutegemewa kutoka maoni kuwa namba zilizokubaliwa; weka SLO kuwa kali kuliko SLA.
- Bajeti ya makosa huoanisha wasanidi na waendeshaji kwa kufanya mabadilishano ya kutegemewa-dhidi-ya-kasi yawe wazi na yaliyojadiliwa mapema.
- Pima na uweke kikomo kazi ya kuchosha, na uchukulie uotomatishaji kama uhandisi wa daraja la kwanza ili operesheni zipanuke kwa kasi ndogo kuliko mfumo.
- Panga uwezo kutoka makadirio ya mahitaji na uheshimu muda wa kuongoza wa utayarishaji, hasa kwa vilele vya msimu.
- Chagua mfano wa kimuundo wa SRE kwa makusudi na ufafanue mfano wazi wa ushirikishaji na kiwango cha utayari wa uzalishaji.

## Marejeo na usomaji zaidi

- Betsy Beyer, Chris Jones, Jennifer Petoff, Niall Richard Murphy, *Site Reliability Engineering: How Google Runs Production Systems*
- Betsy Beyer, Niall Richard Murphy, David K. Rensin, Kent Kawahara, Stephen Thorne, *The Site Reliability Workbook: Practical Ways to Implement SRE*
- David N. Blank-Edelman (editor), *Seeking SRE: Conversations About Running Production Systems at Scale*
- Thomas A. Limoncelli, Strata R. Chalup, Christina J. Hogan, *The Practice of Cloud System Administration*
- Nicole Forsgren, Jez Humble, Gene Kim, *Accelerate: The Science of Lean Software and DevOps*
