# 2.6 Udhibiti wa matoleo na usimamizi wa chanzo

## Muhtasari na msukumo

Fikiria [udhibiti wa matoleo](https://en.wikipedia.org/wiki/Version_control) kama mfumo wa rekodi wa msimbo wako. Unanasa kila badiliko, ikijumuisha nani alilifanya, lini, na kwa nini, na unaruhusu watu wengi kufanya kazi kwenye programu ileile bila kuandikiana juu. Kwa shirika kubwa, ni zaidi sana ya nakala rudufu. Ndio msingi ambao ushirikiano, [uunganishaji endelevu](https://en.wikipedia.org/wiki/Continuous_integration) (CI), ukaguzi, na usimamizi wa matoleo vyote vinasimama juu yake. Chaguo unazofanya kuhusu matawi, muundo wa hazina, na nidhamu ya commit huumba jinsi timu yako inavyoweza kusonga haraka, na kwa usalama kiasi gani.

Kwa timu kubwa, usimamizi wa chanzo ni kweli tatizo la uratibu kwa ukubwa. Mamia ya wahandisi wanapoingiza mabadiliko kwenye msimbo wa pamoja, wanahitaji mkakati unaoweka uunganishaji mdogo, mstari mkuu ukiwa tayari kutolewa, na historia ikisomeka. Timu inayounganisha mfululizo hutiririka kwa utulivu. Timu inayoacha matawi yatofautiane kwa wiki hubadilika kutoka mgogoro mmoja wa uunganishaji hadi mwingine. Muundo wa hazina yako, moja kubwa au nyingi, pia huumba jinsi timu zinavyoshiriki msimbo na kuratibu.

Mazingira ya mashirika makubwa na ya serikali huongeza madai machache zaidi: ufuatiliaji, udhibiti wa ufikiaji, na uhifadhi. Badiliko linaweza kuhitaji kuunganishwa na kipengee cha kazi kilichoidhinishwa kwa ukaguzi. Siri hazipaswi kamwe kuingia kwenye historia. Ufikiaji wa hazina lazima uheshimu mipaka ya usalama. Hapa, mazoea yako ya udhibiti wa matoleo huwa sehemu ya mfumo wa udhibiti wa shirika, na kosa kama siri iliyovuja au historia isiyoweza kukaguliwa linaweza kuwa na matokeo mazito.

## Kanuni kuu

- Unganisha mabadiliko madogo mara kwa mara; kutofautiana kwa muda mrefu ndiko chanzo cha maumivu ya uunganishaji.
- Weka mstari mkuu tayari kutolewa daima.
- Historia ni nyaraka; andika commit kwa msomaji wa baadaye anayepaswa kuelewa kwa nini.
- Kamwe usiweke siri kwenye commit; chukulia siri yoyote iliyofika kwenye historia kama iliyoathirika.
- Otomatisha utekelezaji wa usafi (ndoano, ukaguzi wa CI) badala ya kutegemea nidhamu peke yake.
- Chagua muundo wa hazina (moja au nyingi) kulingana na jinsi timu zinavyoshiriki msimbo na kuratibu kweli, si mtindo.
- Unganisha mabadiliko na sababu zake (vipengee vya kazi, tiketi, au maamuzi) kwa ufuatiliaji.

## Mapendekezo

### Pendelea uendelezaji unaotegemea shina na matawi ya muda mfupi

Elekea [uendelezaji unaotegemea shina](https://en.wikipedia.org/wiki/Trunk-based_development): unganisha kwenye mstari mkuu wa pamoja mara kwa mara, ukitumia matawi ya vipengele ya muda mfupi yanayopimwa kwa saa au siku, si wiki. Matawi mafupi huweka uunganishaji mdogo na ujumuishaji endelevu, na tabia hiyo inahusiana sana na utendaji wa juu wa utoaji. Kazi isipokamilika bado, usiiegeshe kwenye tawi la muda mrefu. Tumia [bendera za vipengele](https://en.wikipedia.org/wiki/Feature_toggle), swichi za wakati wa kuendesha zinazoficha kazi isiyokamilika, ili uweze kuiunganisha kwa usalama badala yake. Hifadhi matawi ya toleo ya muda mrefu kwa msaada wa kweli wa matoleo mengi, na uingie ukijua gharama ya matengenezo wanayobeba.

### Chagua mfano wa matawi unaofaa ratiba ya matoleo

Linganisha [mfano wako wa matawi](https://en.wikipedia.org/wiki/Branching_(version_control)) na jinsi unavyotoa kweli. Ukitoa mfululizo, uendelezaji unaotegemea shina wenye matawi machache sana unakutumikia vyema. Ukisafirisha matoleo yenye nambari kwa wateja, au kuunga mkono matoleo kadhaa hai kwa wakati mmoja, unaweza kuhitaji matawi ya toleo na kurudisha marekebisho. Epuka mifano mizito yenye matawi mengi ya muda mrefu isipokuwa mfano wako wa matoleo unaudai kweli, kwa sababu huzidisha mzigo wa uunganishaji na matengenezo.

### Amua monorepo dhidi ya polyrepo kwa makusudi

Chagua [monorepo](https://en.wikipedia.org/wiki/Monorepo), hazina moja inayoshikilia miradi mingi, pale timu zinashiriki msimbo kwa wingi, zinahitaji mabadiliko ya kuvuka miradi kwa mara moja, na kutaka zana na uonekano wa pamoja. Kwa malipo, unakubali haja ya zana za ujenzi zilizopanuliwa na udhibiti wa ufikiaji. Chagua polyrepo, hazina tofauti kwa kila mradi au huduma, pale timu na huduma ni huru kweli, zinataka ufikiaji uliotengwa na mizunguko ya matoleo, na hazihitaji mabadiliko ya kuvuka hazina kwa mara moja. Kwa malipo, unakubali gharama ya kuratibu mabadiliko yanayovuka hazina. Zote mbili zinafanya kazi kwa ukubwa. Ni chaguo lisilofaa kwa mfumo wako wa uunganishaji ndilo linaloleta msuguano wa daima.

### Tekeleza usafi wa commit na commit za kawaida

Omba ujumbe wa commit unaoeleza kwa nini badiliko lilifanywa, si nini tu. Pokea desturi kama commit za kawaida ili ujumbe uwe na muundo na unaosomeka na mashine, jambo linalokuruhusu kuotomatisha kumbukumbu za mabadiliko na matoleo. Weka commit zikiwa ndogo kabisa, badiliko moja la kimantiki kila moja, ili historia ibaki inayoweza kutafutwa kwa mgawanyo na rahisi kutengua. Acha ndoano na ukaguzi wa CI vitekeleze muundo wa ujumbe na usafi wa msingi, badala ya kutegemea kumbukumbu.

### Weka mafaili makubwa ya binary na msimbo uliozalishwa nje ya historia ya kawaida

Usiweke mali kubwa za binary moja kwa moja kwenye historia kuu, kwa sababu zinavimbisha kila nakala milele. Tumia utaratibu wa kuhifadhi mafaili makubwa au hazina ya vitu vilivyotengenezwa badala yake. Kama kanuni, epuka pia kuweka msimbo uliozalishwa; uzalishe kwenye ujenzi. Unapolazimika kweli kuweka kitu kilichozalishwa, kitenge na ukiweke alama wazi ili kisichafue mapitio na ulinganisho.

### Zuia siri zisiingie kwenye hazina kamwe

Weka uchanganuzi wa kiotomatiki wa siri kwenye ndoano zako za kabla ya commit na CI ili stakabadhi zizuiwe kabla hazijatua. Wape wahandisi mfumo sahihi wa usimamizi wa siri, ili wasihitaji kamwe kuweka stakabadhi ndani ya msimbo. Na chukulia siri yoyote inayofika kwenye historia kama iliyoathirika: ibadilishe mara moja. Siri ikishasukumwa na kunakiliwa, kuiondoa kwenye historia ni ngumu na isiyo ya kuaminika.

### Weka udhibiti wa ufikiaji na ufuatiliaji

Weka ufikiaji wa hazina kuheshimu mipaka ya usalama na [upendeleo mdogo kabisa](https://en.wikipedia.org/wiki/Principle_of_least_privilege). Unganisha commit au maombi ya kuvuta na vipengee vya kazi, ili kila badiliko lifuatiliwe hadi sababu yake, jambo linalosaidia muktadha wa kila siku wa uhandisi na ukaguzi. Linda matawi yako muhimu kwa ukaguzi na mapitio yanayohitajika, ili hakuna kinachoungana bila kupita malango mliyokubaliana.

## Mabadilishano: faida na hasara

| Chaguo | Faida | Hasara |
|---|---|---|
| Uendelezaji unaotegemea shina | Uunganishaji endelevu; uunganishaji mdogo; mtiririko wa juu | Inahitaji bendera za vipengele na nidhamu; utengaji mdogo |
| Matawi ya vipengele ya muda mrefu | Utengaji imara wa kazi inayoendelea | Uunganishaji wenye maumivu; kuchelewa kuunganisha; kuteleza |
| Monorepo | Mabadiliko ya kuvuka miradi kwa mara moja; zana za pamoja; uonekano | Inahitaji zana za ujenzi zilizopanuliwa; udhibiti wa ufikiaji wa jumla kwa chaguo-msingi |
| Polyrepo | Matoleo huru; ufikiaji uliotengwa; zana rahisi kwa kila hazina | Mabadiliko ya kuvuka hazina ni magumu; mzigo wa uratibu wa matoleo |
| Commit za kawaida | Kumbukumbu za mabadiliko na matoleo za kiotomatiki; historia thabiti | Desturi ya awali; utekelezaji unahitajika |

Mabadilishano makuu hapa ni mzunguko wa uunganishaji dhidi ya utengaji. Matawi ya muda mrefu huhisi salama zaidi kwa sababu kazi yako inakaa peke yake, lakini utengaji huo ndio unaosababisha uunganishaji ghali na mshangao wa uunganishaji baadaye. Uendelezaji unaotegemea shina unaacha hisia hiyo ya utengaji kwa kubadilishana na uunganishaji endelevu, wa nafuu, na unakuomba ulete bendera za vipengele na nidhamu. Uamuzi wa monorepo/polyrepo hubadilishana urahisi wa kuvuka miradi na uhuru wa timu. Chagua inayolingana na jinsi msimbo wako ulivyounganishwa kweli.

## Maswali ya kujadili na timu yako

1. **Ni ukaguzi gani lazima upite kabla ya chochote kuungana kwenye mstari wenu mkuu uliolindwa, na je, mstari huo uko tayari kutolewa daima kweli?** Sura hii inachukulia mstari mkuu unaoweza kutolewa kama kanuni ya msingi na inaita mstari mkuu usiolindwa, ambapo msimbo uliovunjika au usiopitiwa unafika kwenye tawi ambalo kila mtu analitegemea, mfumo mbaya. Katika timu kubwa mstari mkuu mwekundu huzuia kila mtu kwa wakati mmoja, kwa hiyo lango unalohitaji ni sifa ya usalama ya pamoja, si ya kibinafsi. Leta ushahidi: ulinzi wa tawi unatekeleza nini leo kweli, na mara ngapi mstari mkuu umevunjika kwa sasa. Amua seti inayohitajika, majaribio yanayopita, uchanganuzi wa usalama, na mapitio, na ufanye mstari mkuu uweze kutolewa kwa sera badala ya matumaini. Lango hilo ndilo linaloruhusu watu wengi kuunganisha mfululizo bila hofu.

2. **Je, kupokea commit za kawaida kunastahili mzigo wa desturi kwa timu yenu, ukizingatia kinachootomatishwa?** Sura inapendekeza ujumbe wa commit wenye muundo, unaosomeka na mashine hasa kwa sababu unakuruhusu kuotomatisha kumbukumbu za mabadiliko na matoleo, na inaomba commit ndogo kabisa ili historia ibaki inayoweza kutafutwa kwa mgawanyo na kutenguliwa. Mabadilishano ni halisi: unalipa desturi ya awali na unahitaji utekelezaji, kwa kubadilishana na maelezo ya toleo yaliyozalishwa na historia ya kuaminika. Leta ishara ya unachofanya kwa mkono leo, kama kuandika kumbukumbu za mabadiliko kwa mkono au kuwinda commit ipi ilileta kurudi nyuma. Ukitoa mara nyingi au kudumisha matoleo mengi, uendeshaji wa kiotomatiki kwa kawaida hujilipia; ukikata toleo mara chache, desturi nyepesi inaweza kutosha. Acha ndoano na CI vitekeleze muundo ili usitegemee kumbukumbu.

3. **Je, mmekubali gharama ya kiuendeshaji ambayo muundo wa hazina yenu unadai, iwe zana za monorepo au uratibu wa kuvuka hazina?** Sura hii inasema monorepo na polyrepo zote zinafanya kazi kwa ukubwa, na kwamba chaguo lisilofaa kwa mfumo wenu wa uunganishaji ndilo linaleta msuguano wa daima. Monorepo inahitaji zana za ujenzi zilizopanuliwa na udhibiti wa ufikiaji wa ngazi nzuri zaidi, huku polyrepo zikifanya badiliko lolote linalovuka hazina kuwa mradi wa uratibu wenye hatari ya kutofautiana kwa matoleo. Leta ishara madhubuti: mara ngapi mabadiliko yenu yanavuka mipaka ya miradi, na kama zana zenu za ujenzi na ufikiaji zinaweza kubeba muundo mlio nao. Mabadiliko ya kuvuka miradi kwa mara moja yakiwa ya kawaida, wekeza katika zana za monorepo; timu na huduma zikiwa huru kweli, kubali gharama ya uratibu wa kuvuka hazina kwa makusudi. Hoja ni kulinganisha muundo na jinsi msimbo wako ulivyounganishwa kweli, kisha kufadhili zana ambazo muundo huo unahitaji.

4. **Stakabadhi hai ikiwekwa kwenye hazina yenye shughuli sasa hivi, ungeigundua kwa haraka kiasi gani, na je, kubadilisha ni kiotomatiki badala ya matumaini?** Sura hii inachukulia siri yoyote inayofika kwenye historia kama iliyoathirika na inaonya kwamba kuiondoa baadaye ni ngumu na isiyo ya kuaminika, kwa hiyo kinga na kubadilisha kwa haraka ndizo ulinzi pekee wa kweli. Kwa timu kubwa mfiduo hujumlika: siri iliyosukumwa kwenye hazina ya pamoja inanakiliwa kwenye mashine kadhaa na kuakisiwa kwenye kashe za CI ndani ya dakika, kwa hiyo mwitikio wa polepole wa binadamu unahakikisha uvunjaji. Jambo linaloshindana ni msuguano: uchanganuzi mkali wa kabla ya commit na kubadilisha kwa kulazimishwa hupunguza kasi ya watu na kuzalisha chanya za uongo, kwa hiyo lazima urekebishe udhibiti badala ya kuuzima. Leta ushahidi: kama uchanganuzi wa siri unaendeshwa kwenye ndoano za kabla ya commit na CI, muda wenu wa wastani wa kugundua na kubadilisha uvujaji unaojulikana, na kama wahandisi hata wana mfumo wa usimamizi wa siri unaoondoa kishawishi cha kuweka ndani ya msimbo. Katika mazingira ya mashirika makubwa na ya serikali, funga hili na mchakato wenu wa matukio na kanuni za uhifadhi, kwa sababu stakabadhi iliyovuja katika historia inayokaguliwa ni tukio la usalama na la uzingatiaji, na mdhibiti atauliza nani alijua na alitenda kwa haraka kiasi gani.

5. **Je, matawi yenu ni ya muda mfupi kweli, na pale sio, kwa nini kazi isiyokamilika inaegeshwa kwenye tawi badala ya kufichwa nyuma ya bendera ya kipengele?** Sura inaelekea kwa nguvu uendelezaji unaotegemea shina kwa sababu kutofautiana kwa muda mrefu ndiko chanzo cha maumivu ya uunganishaji, na inatoa bendera za vipengele kama utaratibu unaokuruhusu kuunganisha kazi pungufu kwa usalama badala ya kuitenga kwa wiki. Katika timu kubwa hii ni sifa ya uratibu, si upendeleo wa kibinafsi: kila tawi linaloishi kwa wiki linakuwa uma wa faragha wa uhalisia ambao mtu lazima hatimaye aupatanishe, na gharama ya upatanisho huo inakua na idadi ya wafanyakazi. Jambo linaloshindana ni kwamba bendera za vipengele hubeba gharama zake, ikijumuisha ugumu wa wakati wa kuendesha, kujaribu mchanganyiko, na bendera zilizochakaa zinazopaswa kustaafishwa. Leta data: mgawanyo wenu halisi wa maisha ya matawi, mara ngapi uunganishaji huzalisha migongano au mshangao, na matawi mangapi ya muda mrefu yapo sasa na kwa nini. Kwa shirika kubwa au linalodhibitiwa, ongeza picha ya matoleo, kwa kuwa msaada wa kweli wa matoleo mengi unaweza kuhalalisha matawi ya toleo ya muda mrefu yenye kurudisha marekebisho kwa nidhamu, na hilo ni uamuzi tofauti na kuegesha kazi ya kila siku ya vipengele nje ya mstari mkuu.

6. **Je, kila badiliko katika historia yenu linaweza kufuatiliwa hadi mwandishi wake na sababu yake ndani ya mipaka sahihi ya usalama, na je, hilo lingesimama kwenye ukaguzi?** Sura hii inachukulia udhibiti wa ufikiaji, upendeleo mdogo kabisa, na kuunganisha mabadiliko na vipengee vya kazi kama sehemu ya mfumo wa udhibiti wa shirika, si mng'ao wa hiari. Kwa timu kubwa, ufuatiliaji ndio unaogeuza mtiririko usioeleweka wa commit kuwa kitu unachoweza kufikiria wakati wa tukio au mapitio ya uzingatiaji, na mipaka ya ufikiaji ndiyo inayozuia akaunti moja iliyoathirika isifikie msimbo ambao haipaswi kuufikia kamwe. Jambo linaloshindana ni kasi ya msanidi: viungo vya lazima vya vipengee vya kazi, ruhusa za ngazi nzuri, na mapitio yanayohitajika huongeza taratibu ambazo timu ndogo yenye mwendo wa haraka inaweza kuruka kwa busara. Leta ushahidi: kama matawi yaliyolindwa yanahitaji ukaguzi na mapitio mnayodai, kama commit zinarejelea vipengee vya kazi vilivyoidhinishwa kweli, na ufikiaji unalingana vipi na mipaka yenu halisi ya usalama leo. Katika mazingira ya mashirika makubwa na ya serikali, funga hili na uainishaji, uhifadhi, na wajibu wa ukaguzi, kwa sababu historia isiyoweza kukaguliwa au ruhusa pana mno ya ufikiaji inakuwa matokeo yanayoweza kusimamisha programu au kushindwa kwa idhini.

## Mtazamo wa sekta

**Kampuni changa.** Kasi na kuishi hushinda. Tumia hazina moja, fanya kazi kwa shina, unganisha matawi ya muda mfupi mara kadhaa kwa siku, na ufiche kazi isiyokamilika nyuma ya bendera rahisi za vipengele badala ya matawi marefu. Washa uchanganuzi wa siri tangu commit ya kwanza kabisa, kwa sababu ufunguo uliovuja kwenye hazina ya umma unaweza kuzamisha kampuni isiyo na timu ya usalama ya kudhibiti. Ruka mifano tata ya matawi na mchakato mzito; tawi kuu lililolindwa na ujumbe wa commit wenye maana ni nidhamu ya kutosha kusonga haraka.

**Biashara ndogo.** Bila mtaalamu maalumu wa jukwaa au DevOps na bajeti finyu, nunua chaguo-msingi zinazosimamiwa badala ya kuzijenga. Mtoa huduma wa Git anayehifadhi hukupa ulinzi wa tawi, mapitio yanayohitajika, na uchanganuzi wa siri tayari, kwa hiyo yategemee badala ya kuhifadhi seva mwenyewe usiyoweza kuidumisha. Weka uamuzi kama usafi wa data: jua hazina zipi zinashikilia usanidi nyeti, weka stakabadhi katika msimamizi wa siri wa mtoa huduma, na uache jukwaa litekeleze kanuni chache unazozihitaji kweli.

**Biashara kubwa.** Tatizo gumu ni uthabiti kuvuka timu nyingi. Sawazisha ulinzi wa tawi, desturi za commit, na uchanganuzi wa siri kama sera ya shirika zima ili vikundi viache kuvivumbua upya, na ufanye uchaguzi wa monorepo dhidi ya polyrepo kwa makusudi kwa kila mfumo wa uunganishaji, ukifadhili zana za ujenzi zilizopanuliwa au uratibu wa kuvuka hazina unaodai. Elekeza mabadiliko kwa wahakiki sahihi kwa kanuni za umiliki wa msimbo, unganisha commit na vipengee vya kazi kwa ufuatiliaji, na uchukulie usafi wa udhibiti wa matoleo kama udhibiti unaotawaliwa wenye wamiliki na vipimo badala ya suala la tabia ya mtu binafsi.

**Serikali.** Kanuni za ununuzi, uwazi, na uwajibikaji wa umma huunda usanidi mzima. Hitaji kila commit irejelee kipengee cha kazi kilichoidhinishwa, dhibiti ufikiaji kwa kila mpaka wa uainishaji, na ufanye uchanganuzi wa siri na kubadilisha mara moja kuwe vya lazima chini ya mchakato ulioandikwa wa matukio. Unga mkono matoleo mengi yaliyosambazwa kwa matawi ya toleo ya muda mrefu na kurudisha marekebisho kwa nidhamu pale maeneo hayawezi kuboresha yote kwa wakati mmoja, na uweke historia ikikaguliwa na kuhifadhiwa ili maombi ya idhini, uhuru wa habari, na usimamizi yaweze kujibiwa bila mhangaiko.

## Mifano

**Kampuni changa.** Kampuni changa ya watu watatu inafanya kazi kwa shina kwa tabia na lazima, ikiunganisha matawi ya muda mfupi kwenye main mara kadhaa kwa siku na kuficha vipengele visivyokamilika nyuma ya bendera rahisi. Wanawasha uchanganuzi wa siri kwenye CI tangu commit ya kwanza, kwa sababu ufunguo wa API uliovuja kwenye hazina ya umma ungezamisha kampuni isiyo na timu ya usalama ya kudhibiti athari. Hazina moja, tawi kuu lililolindwa, na ujumbe wa commit wenye maana huwapa nidhamu ya kutosha kusonga haraka bila kujikwaa kwenye historia yao wenyewe.

**Biashara kubwa.** Kampuni kubwa ya teknolojia inaendesha monorepo yenye mamia ya huduma na maktaba za pamoja. Zana za ujenzi zilizopanuliwa na kanuni za umiliki wa msimbo zinaelekeza kila badiliko kwa wahakiki sahihi. Commit moja inaweza kusasisha kwa mara moja maktaba ya pamoja na kila mtumiaji wake, ikikwepa matatizo ya kutofautiana kwa matoleo yanayosumbua hazina zilizosambazwa. Uendelezaji unaotegemea shina wenye bendera za vipengele unaweka mstari mkuu tayari kutolewa, na uchanganuzi wa siri unazuia stakabadhi wakati wa commit kuvuka hazina nzima.

**Serikali.** Mkandarasi wa taifa wa ulinzi anashikilia ufuatiliaji mkali. Kila commit lazima irejelee kipengee cha kazi kilichoidhinishwa. Ulinzi wa tawi unahitaji uchanganuzi wa usalama unaopita na mapitio huru, na ufikiaji unadhibitiwa kwa makini kwa kila mpaka wa uainishaji. Uchanganuzi wa siri ni wa lazima, na stakabadhi yoyote iliyofichuliwa huchochea kubadilishwa mara moja chini ya mchakato wa matukio. Matawi ya toleo ya muda mrefu yanaunga mkono matoleo mengi yaliyosambazwa kuvuka maeneo ambayo hayawezi kuboresha yote kwa wakati mmoja, kwa kurudisha marekebisho ya usalama kwa nidhamu.

## Kesi ya biashara: sababu, ROI, na TCO

Usimamizi mzuri wa chanzo ni karibu bure kupokea na ghali kuukosa. Uendelezaji unaotegemea shina na uunganishaji endelevu ni miongoni mwa mazoea yanayohusiana sana na utendaji wa juu wa utoaji wa programu, ambao nao unahusiana na matokeo bora ya shirika. Historia safi, inayofuatilika hupunguza muda wa kutambua matukio na kutimiza ukaguzi, na matawi yenye nidhamu hukuokoa gharama inayojirudia, isiyopangiwa bajeti ya migogoro ya uunganishaji na marathoni za kuunganisha.

Hatari kubwa isiyo na usawa ni siri katika udhibiti wa matoleo. Stakabadhi moja iliyovuja inaweza kusababisha uvunjaji ambao gharama yake inapita uwekezaji wowote wa zana, na historia hufanya uvujaji kama huo udumu. Kuzuia ni nafuu; kusafisha baadaye si hivyo. Chaguo duni za muundo huonekana kama msuguano wa kudumu: kila badiliko la kuvuka hazina linakuwa mradi wa uratibu, au kila ujenzi wa monorepo unakuwa kikwazo. Kujenga hoja kwa uongozi, funga mkakati wako wa matawi na vipimo vya utoaji na muda wa kutambua matukio, na uweke uchanganuzi wa siri na udhibiti wa ufikiaji kama udhibiti wa gharama ndogo dhidi ya hatari ya gharama kubwa ya uvunjaji na ukaguzi.

## Mifumo mibaya na mitego

- **Matawi yanayotofautiana ya muda mrefu:** wiki za kazi iliyotengwa zinazoungana kuwa matukio ya uunganishaji yenye maumivu, hatari.
- **Siri kwenye historia:** stakabadhi zilizowekwa ndani ya msimbo zinazodumu kwenye nakala milele na zinahitaji kubadilishwa zikifichuliwa.
- **Kuweka binary kubwa kwenye historia kuu:** kuvimbisha kila nakala kwa kudumu na kupunguza kasi ya shughuli zote.
- **Ujumbe wa commit usio na maana:** "fix", "wip", "changes" unaoharibu thamani ya historia kama nyaraka.
- **Kuweka msimbo uliozalishwa kana kwamba uliandikwa kwa mkono:** ulinganisho wenye kelele, migongano ya uunganishaji, na mkanganyiko kuhusu chanzo cha ukweli.
- **Muundo mbaya wa hazina kwa uunganishaji:** polyrepo kwa msimbo uliounganishwa kwa ukali, au monorepo bila zana zilizopanuliwa.
- **Mstari mkuu usiolindwa:** hakuna ukaguzi unaohitajika, kwa hiyo msimbo uliovunjika au usiopitiwa unafika kwenye tawi ambalo kila mtu analitegemea.

## Kielelezo cha ukomavu

- **Ngazi ya 1, Kuanzisha:** Wa papo hapo na wa kuitikia. Matawi yanaboreshwa papo hapo, yanaishi kwa wiki, ujumbe wa commit unasema "fix" au "wip", hakuna uchanganuzi wa siri, na uunganishaji unaruka kutoka mgogoro mmoja wa kuunganisha hadi mwingine.
- **Ngazi ya 2, Kuendeleza:** Mazoea ya msingi yanaonekana lakini yanatofautiana kwa timu. Mfano wa matawi na desturi za ujumbe zipo mahali fulani, hata hivyo matawi bado yanaishi kwa muda mrefu mno, utekelezaji ni wa sehemu, uchanganuzi wa siri hauna uthabiti, na muundo wa hazina ulirithiwa badala ya kuchaguliwa.
- **Ngazi ya 3, Kusawazisha:** Mazoea yameandikwa na kutekelezwa shirika zima: uendelezaji unaotegemea shina wenye matawi mafupi, mstari mkuu uliolindwa na unaoweza kutolewa daima, desturi za commit zinazotekelezwa, uchanganuzi wa siri kwenye ndoano na CI, ufikiaji wa upendeleo mdogo kabisa, na uchaguzi wa makusudi wa monorepo au polyrepo.
- **Ngazi ya 4, Kusimamia:** Mazoea ya chanzo yanapimwa na kudhibitiwa kwa data. Unafuatilia maisha ya matawi, mzunguko wa uunganishaji, kiwango cha kuvunjika kwa mstari mkuu, muda wa wastani wa kugundua na kubadilisha siri iliyovuja, na ufuatiliaji wa badiliko-hadi-kipengee-cha-kazi dhidi ya vipimo vya msingi vilivyokubaliwa, na unatenda nambari zinapoteleza badala ya kusubiri tukio linalofuata.
- **Ngazi ya 5, Kuratibu:** Mazoea yanaboreshwa kila wakati na kuunganishwa kuvuka shirika. Matawi, muundo wa hazina, na zana hubadilika timu na uunganishaji wa msimbo zinapobadilika, uendeshaji wa kiotomatiki unatekeleza usafi mwanzo hadi mwisho, na data ya udhibiti wa matoleo inalisha maamuzi ya utoaji, usalama, na hatari shirika zima.

## Mawazo ya kujadili

- Je, maisha ya matawi ya timu yenu ni mafupi kweli, na kama sivyo, nini kinazuia uunganishaji endelevu?
- Je, uchaguzi wenu wa monorepo au polyrepo unalingana na jinsi msimbo wenu ulivyounganishwa kweli?
- Mnashughulikiaje binary kubwa na vitu vilivyozalishwa leo, na inawagharimu nini?
- Nini kingetokea stakabadhi hai ikiwekwa sasa hivi, na mngeigundua na kuibadilisha kwa haraka kiasi gani?
- Nidhamu ya ujumbe wa commit na ufuatiliaji ni kiasi gani inastahili kutekelezwa kwa muktadha wenu?
- Bendera za vipengele zinabadilishaje mkakati wenu wa matawi, na zinaleta hatari gani mpya?

## Mambo muhimu ya kukumbuka

- Unganisha mara kwa mara kwa matawi ya muda mfupi; kutofautiana kwa muda mrefu husababisha maumivu ambayo kinaonekana kuepuka.
- Weka mstari mkuu ukitolewa na kulindwa na ukaguzi unaohitajika.
- Usiruhusu siri ziingie kwenye historia kamwe; changanua kiotomatiki na ubadilishe mara moja zikiingia.
- Chagua monorepo au polyrepo kwa mahitaji yako halisi ya uunganishaji na uratibu.
- Chukulia historia ya commit kama nyaraka, kwa commit zenye maana, za kawaida, ndogo kabisa.

## Marejeo na usomaji zaidi

- Nicole Forsgren, Jez Humble, Gene Kim, *Accelerate: The Science of Lean Software and DevOps*
- Jez Humble and David Farley, *Continuous Delivery*
- Scott Chacon and Ben Straub, *Pro Git*
- Paul Hammant and others, writings on trunk-based development
- Conventional Commits specification (as a reference standard)
- Martin Fowler, articles on branching patterns and continuous integration
