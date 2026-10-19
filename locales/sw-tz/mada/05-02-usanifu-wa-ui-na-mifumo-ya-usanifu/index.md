# 5.2 Usanifu wa UI na mifumo ya usanifu

## Muhtasari na msukumo

[Usanifu wa kiolesura cha mtumiaji (UI)](https://en.wikipedia.org/wiki/User_interface_design) ni ufundi wa kuumba watu wanachokiona na kukigusa: mpangilio, [uchapaji](https://en.wikipedia.org/wiki/Typography), rangi, nafasi, vidhibiti, na hali. [Mfumo wa usanifu](https://en.wikipedia.org/wiki/Design_system) huchukua ufundi huo na kuugeuza kuwa mali ya pamoja, inayotumika tena, inayotawaliwa: seti iliyoandikwa ya kanuni, vijenzi, mifumo, na tokeni ambazo kila timu huchota kutoka kwazo, ili bidhaa nzima ionekane na kutenda kama moja. Usanifu wa UI huamua skrini moja inapaswa kuonekanaje. Mfumo wa usanifu huamua jinsi skrini elfu kumi kuvuka timu nyingi zinavyobaki thabiti.

Kwa shirika kubwa, mfumo wa usanifu ndio uwekezaji wenye kiegemeo cha juu zaidi katika ubora wa UI na kasi ya utoaji. Bila mmoja, kila timu inabuni upya vitufe, fomu, madirisha ibukizi, na ushughulikiaji wa makosa, kila kimoja tofauti kidogo, kila kimoja kikidumishwa kando, kila kimoja kikivunjika kando. Watumiaji wanalipia hili kwa mkanganyiko na kutoamini; biashara inalipia kwa juhudi iliyorudiwa na ubora usio sawa. Mfumo wa usanifu hugeuza maamuzi ya usanifu ya mara moja kuwa mtaji unaotumika tena: tatua [ufikivu](https://en.wikipedia.org/wiki/Accessibility), [uitikiaji](https://en.wikipedia.org/wiki/Responsive_web_design), na chapa mara moja ndani ya kijenzi, na kila timu inarithi matokeo.

Mashirika makubwa na serikali huongeza shinikizo mbili mahususi. Kwanza, ukubwa: mamia ya programu, nyingi zilizojengwa na wauzaji au kupatikana kupitia muunganiko, zote zinahitaji kuhisi kama shirika moja. Pili, maisha marefu na mabadiliko: chapa husasishwa, mawakala hupangwa upya, na jukwaa moja linaweza kuhitaji kuhudumia chapa kadhaa au mawakala wadogo kutoka msingi mmoja wa msimbo. Mfumo wa usanifu ulioundwa vizuri, wenye mada na tokeni ipasavyo, hufanya mabadiliko haya makubwa yawezekane badala ya kuwa maafa.

## Kanuni kuu

- Uthabiti hupunguza [mzigo wa kiakili](https://en.wikipedia.org/wiki/Cognitive_load); kitufe kinapaswa kuonekana na kutenda sawa kila mahali.
- Maamuzi ya usanifu ni mali: yanase mara moja kama vijenzi na tokeni zinazotumika tena.
- Tokeni ndizo chanzo cha ukweli cha maamuzi ya kuona; vijenzi hutumia tokeni, kamwe si thamani zilizopachikwa.
- Ufikivu na uitikiaji vimejengwa ndani ya vijenzi, si kubanwa kwa kila skrini.
- Mfumo wa usanifu ni bidhaa yenye watumiaji (wasanidi na wasanifu), si kikabidhiwa cha mara moja.
- Daraja la kuona huongoza umakini: chapa, rangi, na nafasi vinapaswa kufanya umuhimu uwe dhahiri.
- Utawala huweka mfumo katika mshikamano; mchango huuweka hai.

## Mapendekezo

### Panga mfumo katika tabaka: tokeni, vijenzi, mifumo

Tokeni za usanifu ni thamani zenye majina, zisizotegemea jukwaa za rangi, nafasi, uchapaji, kingo, mwinuko, na mwendo: maamuzi ya atomiki. Zijenge kwa ngazi: paleti ya msingi (thamani ghafi), tokeni za kisemantiki (`color-action-primary`, `space-inset-md`) zinazobeba maana, na tokeni za kiwango cha kijenzi pale unapozihitaji. Vijenzi hutumia tokeni za kisemantiki, kwa hiyo badiliko moja linasambaa kila mahali. Juu ya vijenzi kuna mifumo: mpangilio uliothibitishwa kama jedwali la data, fomu ya hatua nyingi, au hali tupu. Andika tabaka zote tatu mahali pamoja, zenye mifano hai na mwongozo wa matumizi.

### Pata misingi ya kuona sawa

Weka kipimo cha uchapaji chenye daraja wazi na nafasi pana ya mistari kwa usomaji, na ubaki kwenye seti ndogo ya ukubwa na unene. Fafanua rangi kama mfumo, yenye utofautishaji wa kutosha kwa ufikivu (angalia sura ya ufikivu) na majukumu ya kisemantiki, badala ya rangi ghafi zilizotawanyika kwenye UI. Tumia kipimo cha nafasi na gridi ya mpangilio ili mpangilio na mdundo vibaki thabiti bila kubahatisha kwa kila skrini. Daraja la kuona linapaswa kufanya kitendo kikuu na taarifa muhimu zaidi ziwe dhahiri kwa mtazamo mmoja.

### Sanifu kwa uitikiaji na simu kwanza

Sanifu kwa kidirisha kidogo cha busara kwanza, kisha boresha kwa skrini kubwa. Hii inakulazimisha kuweka kipaumbele maudhui na vidhibiti muhimu. Tumia mipangilio inayotiririka na vipimo vya kulinganisha ili violesura vijirekebishe kwa skrini yoyote, badala ya kuruka kati ya mipaka michache isiyobadilika. Fanya shabaha za kugusa ziwe kubwa vya kutosha, na uhakikishe mwingiliano unafanya kazi kwa kugusa, kipanya, na kibodi. Katika serikali hasa, dhania sehemu kubwa ya watumiaji wako wako kwenye vifaa vidogo, vya zamani, au vya bajeti.

### Fanya makabidhiano ya usanifu-hadi-maendeleo na usawa kuwa jambo la daraja la kwanza

Mfumo wa usanifu hulipa tu UI iliyosafirishwa inapolingana na usanifu uliokusudiwa na kuendelea kulingana. Lenga chanzo kimoja cha ukweli: tokeni zinazosafirishwa kutoka zana ya usanifu zinalisha msimbo moja kwa moja, ili wasanifu na wahandisi wanarejelea thamani zilezile. Toa maktaba ya vijenzi vilivyoandikwa kwa msimbo ambayo wahandisi watatumia kweli, yenye majina na props zilezile kama vijenzi vya usanifu. Tumia majaribio ya regression ya kuona (ulinganisho wa kiotomatiki wa UI iliyoonyeshwa dhidi ya picha za msingi zilizoidhinishwa) na ukaguzi wa mapitio ya usanifu kunasa kuteleza. Na upime "usawa wa usanifu-na-msimbo" kama kipimo wazi cha afya: sehemu ya UI iliyojengwa kutoka vijenzi vya mfumo dhidi ya msimbo wa mara moja.

### Unga mkono mada na chapa-nyeupe kwa ukubwa wa shirika

Sanifu kwa chapa nyingi tangu mwanzo ikiwa kuna uwezekano wowote utazihitaji. Kwa kuwa vijenzi hutumia tokeni za kisemantiki, mada ni seti tofauti tu ya thamani za tokeni, kwa hiyo usasishaji wa chapa au chapa ndogo mpya inakuwa badiliko la data, si kuandika upya msimbo. Unga mkono mada za mwanga na giza, hali za utofautishaji wa juu, na chapa ya kila mpangaji kupitia utaratibu huohuo. Weka mantiki mahususi ya chapa nje ya vijenzi, na uisukume kwenye seti za tokeni na usanidi badala yake.

### Tawala mfumo kama bidhaa

Mpe mfumo wa usanifu timu maalumu, mpango wa barabara, matoleo, kumbukumbu ya mabadiliko, na njia ya msaada. Eleza jinsi timu zinavyochangia vijenzi vipya, na jinsi hivyo vinapitiwa na kupandishwa. Sawazisha udhibiti wa kati (kuhifadhi mshikamano na ufikivu) na mfano wa mchango (ili mfumo ubadilike na mahitaji halisi badala ya kuwa kizuizi). Wasiliana wazi kuhusu kuondolewa na uhamishaji, na uzipe timu zinazotumia muda wa kutosha wa maandalizi.

## Mabadilishano: faida na hasara

| Uamuzi | Faida | Hasara |
|---|---|---|
| Jenga mfumo wa usanifu | Uthabiti, kasi, ufikivu mara moja, usasishaji rahisi wa chapa | Gharama ya awali na endelevu, unahitaji timu maalumu |
| Pokea mfumo uliotengenezwa tayari | Mwanzo wa haraka, mifumo iliyothibitishwa | Mwonekano wa jumla, ngumu kulingana na chapa na mahitaji ya kipekee |
| Utawala mkali wa kati | Mshikamano, ubora, ufikivu umehakikishwa | Unaweza kuzuia timu, kuhisi kiukiritimba |
| Mfano wa mchango wazi | Hubadilika na mahitaji halisi, umiliki wa pamoja | Hatari ya kuteleza na kutokuwa na uthabiti bila mapitio |
| Tokeni nzito na mada | Usasishaji wa chapa wa bei nafuu na usaidizi wa chapa nyingi | Uondoaji zaidi, mkondo mkali zaidi wa kujifunza |

Mifumo ya usanifu hubadilisha gharama ya awali na ya utawala kwa uthabiti na kasi ya muda mrefu. Kwa bidhaa ndogo yenye timu moja, mzigo huenda usilipe. Kwa shirika kubwa lenye timu nyingi na bidhaa za muda mrefu, swali si kama uwe na mfumo bali kiasi gani cha kuwekeza na jinsi ya kuutawala. Majuto ya kawaida zaidi ni kuwekeza kidogo mno kwenye utawala na zana za usawa: mfumo upo kwenye karatasi, lakini timu zinaondoka kimyakimya.

## Maswali ya kujadili na timu yako

1. **Usanifu wetu wa tokeni umepangwa kwa ngazi vipi, na je, vijenzi vimekatazwa kutumia thamani zilizopachikwa?** Faida yote ya mfumo wa usanifu (usasishaji wa bei nafuu wa chapa, mada za chapa nyingi, ufikivu uliotatuliwa mara moja) inategemea vijenzi kutumia tokeni za kisemantiki kama `color-action-primary` badala ya rangi ghafi na thamani za pikseli zilizotawanyika kwenye msimbo. Amua ngazi sasa: paleti ya msingi, tokeni za kisemantiki zinazobeba maana, na tokeni za kiwango cha kijenzi pale tu mnapozihitaji kweli. Uondoaji kupita kiasi ni hatari halisi, kwa hiyo kubaliana tabaka ngapi ni nyingi mno na jinsi msanidi anavyopata tokeni sahihi haraka. Leta grep ya rangi na nafasi zilizopachikwa kuvuka msingi wenu wa msimbo kama ushahidi wa kuteleza. Mantiki ya chapa ikipachikwa ndani ya vijenzi, usasishaji wa chapa unakuwa kuandika upya msimbo badala ya badiliko la usanidi, ambalo ndilo hasa janga ambalo tokeni zipo kuzuia.

2. **Tunapimaje na kutetea usawa wa usanifu-na-msimbo, na zana gani hunasa kuteleza kiotomatiki?** Mfumo wa usanifu unaokuwepo kama faili ya usanifu tu ni karatasi ya vibandiko: wahandisi hujenga upya kila kitu hata hivyo na UI iliyosafirishwa hutofautiana polepole na nia. Kubaliana kipimo wazi cha usawa (sehemu ya UI iliyojengwa kutoka vijenzi vya mfumo dhidi ya msimbo wa mara moja) na uunganishe majaribio ya regression ya kuona kwenye CI ili skrini zilizoonyeshwa zilinganishwe na picha za msingi zilizoidhinishwa. Hili ni muhimu kwa ukubwa wa mashirika makubwa na serikali kwa sababu mamia ya programu, nyingi zilizojengwa na wauzaji au kurithiwa kupitia muunganiko, zote zinahitaji kuhisi kama shirika moja. Leta namba ya sasa ya usawa na orodha ya vijenzi maalumu vikuu ambavyo timu zinaendelea kuvijenga upya. Kama hakuna anayemiliki kipimo wala mfululizo wa regression, kuteleza tayari kunashinda kimyakimya.

3. **Tunatawalaje mchango, kuondolewa, na uhamishaji ili mfumo usizuie timu wala usigawanyike?** Udhibiti mkali wa kati unahakikisha mshikamano na ufikivu lakini unaweza kuigeuza timu ya mfumo wa usanifu kuwa kizuizi ambacho timu hukipita pembeni; mchango wazi huweka mfumo hai lakini unahatarisha lahaja zinazotofautiana bila mapitio. Amua njia ya mchango: jinsi timu inavyopendekeza kijenzi kipya, nani anakipitia, na jinsi kinavyopandishwa. Vilevile, kubaliana jinsi mnavyowasiliana mabadiliko yanayovunja, kwa sababu kuondoa bila msaada wa uhamishaji na muda wa maandalizi husababisha timu zinazotumia kukwama au kufanya fork. Leta mifano ya vijenzi ambavyo timu zilijenga nje ya mfumo na uliza kwa nini hazikuchangia nyuma. Jibu kwa kawaida hufichua kama utawala wenu ni huduma au kizuizi.

4. **Tunahakikishaje ufikivu unatatuliwa mara moja ndani ya vijenzi, na nini kinazuia timu isisafirishe kijenzi cha mara moja kisichofikika?** Hoja kali zaidi ya mfumo wa usanifu ni kwamba utofautishaji wa rangi, hali za umakini, uendeshaji wa kibodi, na kisemantiki cha visomaji skrini hutatuliwa mara moja na kurithiwa kila mahali, lakini ahadi hiyo huporomoka timu zinapojenga vidhibiti vyao wenyewe kwa mkono. Kwa shirika kubwa hapa ndipo hatari kubwa zaidi ya kisheria na ya sifa ilipo, kwa sababu fomu moja isiyofikika ya malipo au kichagua tarehe kinaweza kuzuia watumiaji halisi na kuchochea malalamiko kuvuka kila bidhaa iliyokinakili. Pima utekelezaji wa kati (vijenzi vinavyofikika pamoja na linter au lango la mapitio linalokataa alama ghafi) dhidi ya uhuru wa timu, na uamue mstari mgumu uko wapi. Leta matokeo ya ukaguzi wa ufikivu, orodha ya vijenzi na hali ya uzingatiaji wake, na hesabu ya vidhibiti maalumu ambavyo timu zilivijenga upya nje ya mfumo. Katika mazingira ya mashirika makubwa na serikali hili si pambo: wajibu kama WCAG, Section 508, na EN 301 549 hufanya uzingatiaji kuwa sharti la ununuzi na ukaguzi, kwa hiyo maktaba ya vijenzi yenye uzingatiaji ulioandikwa ni mali ya uzingatiaji yenyewe.

5. **Mfumo huu lazima uhudumie chapa, wapangaji, na mada ngapi, na je, tumeunda safu ya tokeni kwa hilo sasa badala ya kuirudisha baadaye?** Kutumia mada ni nafuu ukibuni kwa ajili yake na ya kikatili usipofanya hivyo, kwa sababu chapa au mpangaji ambaye hakutarajiwa hulazimisha mantiki ya chapa kurudi ndani ya vijenzi na kubatilisha madhumuni yote ya tokeni. Kwa timu kubwa uamuzi huu unaumba miaka ya kazi: jukwaa linalopaswa kuhudumia chapa kadhaa, mada ya mwanga na giza, hali ya utofautishaji wa juu, na chapa ya kila mpangaji linahitaji safu ya tokeni za kisemantiki safi vya kutosha ili mada iwe seti tofauti tu ya thamani. Sawazisha unyumbulifu huo dhidi ya uondoaji kupita kiasi, kwa kuwa mti wa tokeni ambao hakuna anayeweza kuupitia ni kushindwa kwake. Leta mpango wa barabara wa chapa na wapangaji mnaoweza kuwaona mbele, idadi ya mada zinazotumika leo, na vijenzi vyovyote ambavyo tayari vinavujisha mantiki mahususi ya chapa. Katika mazingira ya mashirika makubwa na serikali, muunganiko, ununuzi, na kupangwa upya kwa mawakala mara kwa mara huongeza chapa ambazo hamkupanga, kwa hiyo kubuni kwa chapa nyingi tangu mwanzo ndio tofauti kati ya badiliko la data na uandishi upya wa miaka mingi.

6. **Tutahamishaje programu za urithi na zilizojengwa na wauzaji kwenye mfumo, na timu ya mfumo wa usanifu inafadhiliwaje ili iokoke mzunguko wa bajeti unaofuata?** Mfumo wa usanifu unatoa faida yake tu bidhaa halisi zinapoupokea, hata hivyo programu ngumu zaidi kubadilisha ni za zamani na zilizotolewa nje zinazouhitaji zaidi, na timu inayodumisha mfumo mara nyingi ndiyo ya kwanza kukatwa bajeti zinapobana. Kwa shirika kubwa lazima uamue kati ya uhamishaji wa mlipuko mmoja na wa hatua kwa hatua, na jinsi ya kuwafanya wauzaji wajenge juu ya vijenzi vyenu badala ya kuvizunguka. Leta orodha ya programu zenye alama zao za sasa za usawa, makadirio ya juhudi ya uhamishaji kwa kila programu, na viegemeo vya kimkataba mnavyoshikilia dhidi ya wauzaji. Katika mazingira ya mashirika makubwa na serikali, andika uzingatiaji wa mfumo wa usanifu kwenye masharti ya ununuzi ili kazi mpya ya wauzaji itue kwenye mfumo kwa chaguo-msingi, na ufadhili timu inayodumisha kama miundombinu ya pamoja ya kudumu, kwa sababu mfumo unaopoteza wasimamizi wake katika upangaji upya unateleza kurudi kwenye mgawanyiko ndani ya mwaka.

## Mtazamo wa sekta

**Kampuni changa.** Ukiwa na wahandisi wawili au watatu na bila muda wa ziada, usijenge mfumo unaotawaliwa. Tumia siku moja au mbili kufafanua seti ndogo ya tokeni za kisemantiki za rangi, nafasi, na chapa, pamoja na vijenzi kumi na viwili vya pamoja, vyote kwenye faili moja ambayo timu nzima inairejelea. Egemea maktaba ya vipengele vya msingi iliyotengenezwa tayari kwa sehemu ngumu, na usipachike chochote ili usasishaji wako wa kwanza halisi wa chapa uwe badiliko la tokeni badala ya kuandika upya.

**Biashara ndogo.** Bila mbunifu maalumu na bajeti finyu, nunua badala ya kujenga: pokea maktaba ya vijenzi iliyothibitishwa au kifurushi cha UI na uipe mada nyepesi kwa chapa yako. Lengo lako ni bidhaa thabiti, inayofikika bila kuajiri timu ya mfumo wa usanifu, kwa hiyo pendelea mfumo unaokuja na ufikivu na uitikiaji ndani yake. Pinga hamu ya kufanya fork, kwa sababu nakala iliyobinafsishwa ambayo huwezi kuidumisha inakuwa dhima mradi wa chanzo unaposonga mbele.

**Biashara kubwa.** Tatizo ni mshikamano kuvuka timu nyingi na bidhaa za muda mrefu, kwa hiyo chukulia mfumo wa usanifu kama miundombinu ya pamoja inayotawaliwa yenye timu maalumu, matoleo, na mpango wa barabara. Fuatilia usawa wa usanifu-na-msimbo kama kipimo halisi, unganisha majaribio ya regression ya kuona kwenye CI, na sanifu safu ya tokeni kwa chapa na mada nyingi tangu mwanzo. Weka bajeti ya gharama ya utawala na uhamishaji waziwazi, na simamia upokeaji kama jalada badala ya kudhani timu zitaelekea mfumoni zenyewe.

**Serikali.** Kanuni za ununuzi, uwazi, na uwajibikaji wa umma huumba kila uchaguzi. Uzingatiaji wa ufikivu kwa viwango kama WCAG, Section 508, na EN 301 549 ni sharti la kisheria, si upendeleo, kwa hiyo maktaba ya vijenzi yenye uzingatiaji ulioandikwa inakuwa mali ya uzingatiaji. Pendelea au panua mfumo wa usanifu wa umma wa pamoja ili raia wakutane na mifumo ileile kuvuka huduma, andika matumizi ya mfumo wa usanifu kwenye mikataba ya wauzaji, na uchapishe vijenzi na mwongozo wako wazi ili mawakala na wasambazaji wao waweze kuvipokea na kuwajibika kwavyo.

## Mifano

**Kampuni changa.** Kampuni changa ya wahandisi wawili iliendelea kujenga upya vitufe na nyanja za fomu kwa tofauti ndogo kwenye kila skrini mpya, na bidhaa ilianza kuonekana imeshonwa pamoja. Badala ya mfumo mzito, walitumia siku mbili kufafanua seti ndogo ya tokeni za usanifu za kisemantiki za rangi, nafasi, na chapa, pamoja na vijenzi kumi na viwili vya pamoja, vyote kwenye faili moja ambayo timu nzima iliirejelea. Kwa kuwa hakuna kilichopachikwa, mwajiriwa wao wa kwanza mwenye mtazamo wa usanifu alipopendekeza paleti safi zaidi, usasishaji ulikuwa badiliko la tokeni lililotua kuvuka programu kwa alasiri moja badala ya kusaga skrini kwa skrini.

**Biashara kubwa.** Kampuni ya programu ya kimataifa yenye timu kadhaa za bidhaa ilijenga mfumo wa usanifu wenye tokeni na maktaba ya pamoja ya vijenzi vilivyoandikwa kwa msimbo. Tokeni za kisemantiki ziliwaruhusu kusafirisha usasishaji kamili wa chapa kuvuka bidhaa zote kwa wiki, badala ya kusaga kwa miaka mingi kwa kila timu, kwa sababu badiliko lilikuwa seti mpya ya tokeni badala ya maelfu ya marekebisho ya rangi zilizopachikwa. Usawa wa usanifu-na-msimbo, uliofuatiliwa kama kipimo cha dashibodi, ulipanda timu zilipobadilisha vijenzi maalumu, jambo lililopunguza matengenezo ya UI iliyorudiwa.

**Serikali.** Serikali ya kitaifa iliunda mfumo wa pamoja wa usanifu kwa huduma za umma (vijenzi vya pamoja, mifumo, na ufikivu uliojengwa ndani) uliamriwa kuvuka mawakala. Raia anayehama kati ya huduma ya kodi, ya afya, na ya leseni anakutana na kichwa kilekile, vidhibiti vya fomu, na mifumo ya makosa, jambo linalojenga uaminifu na kufupisha mkondo wa kujifunza. Mawakala na wauzaji wao wanasafirisha kwa kasi zaidi na kwa ufikivu zaidi kwa sababu matatizo magumu yanatatuliwa kati, na serikali inaweza kusasisha mwongozo au marekebisho ya ufikivu mara moja na kuyasambaza kila mahali.

## Kesi ya biashara: sababu, ROI, na TCO

ROI ya mfumo wa usanifu inatokana na kuondoa marudio na kuharakisha utoaji. Badala ya kila timu kubuni na kujenga vijenzi vilevile, wanatunga kutoka maktaba ya pamoja, jambo linaloharakisha utoaji kwa kupimika na kuwaweka huru wasanifu na wahandisi kwa kazi mahususi ya bidhaa. Ufikivu na uitikiaji, vilivyotatuliwa mara moja ndani ya vijenzi, vinakuokoa gharama ya kurekebisha kwa kila mradi. Usasishaji wa chapa na mada ambao zamani ulichukua miaka sasa unachukua wiki.

Kwenye TCO, gharama ya kupokea ni timu maalumu, zana, na juhudi kwa bidhaa zilizopo kuhamia kwenye mfumo. Gharama ya kutopokea inalipwa kila wakati: ujenzi na matengenezo yaliyorudiwa kuvuka timu, UI zisizo thabiti na zisizofikika zinazozalisha hatari ya msaada na ya kisheria, na usasishaji wa chapa wa polepole, wa gharama. Kwa kuwa marudio yameenea kuvuka bajeti za timu nyingi, ni rahisi kuyapuuza: mfumo wa usanifu hufanya gharama hiyo iliyofichika ionekane na kuinasa mahali pamoja.

Kuweka kesi kwa uongozi, pima kwa namba kazi ya vijenzi iliyorudiwa kuvuka timu, faida ya muda-hadi-soko kutoka kutunga, na gharama na muda wa usasishaji wenu wa mwisho wa chapa dhidi ya kile mfumo wenye tokeni ungeruhusu. Weka mfumo kama miundombinu ya pamoja yenye kipimo cha upokeaji kinachopimika (asilimia ya usawa), ili thamani yake ifuatiliwe kwa muda badala ya kudaiwa tu.

## Mifumo mibaya na mitego

- **Mfumo wa usanifu kama karatasi ya vibandiko**: faili tuli ya usanifu isiyo na vijenzi vilivyoandikwa kwa msimbo, kwa hiyo wahandisi hujenga upya kila kitu hata hivyo.
- **Thamani zilizopachikwa kila mahali**: rangi na nafasi zilizotawanyika kwenye msimbo, zikifanya mada na usasishaji wa chapa kutowezekana.
- **Hakuna utawala**: mfumo unagawanyika timu zinapoongeza lahaja zinazotofautiana; uthabiti unamomonyoka.
- **Utawala bila mchango**: timu ya kati inakuwa kizuizi na timu zinaipita pembeni.
- **Kupuuza usawa**: UI iliyoandikwa kwa msimbo inateleza kutoka nia ya usanifu na hakuna anayepima pengo.
- **Uondoaji kupita kiasi**: tokeni na tabaka nyingi mno hadi hakuna anayeweza kupata au kutumia sahihi.
- **Mantiki ya chapa iliyopachikwa kwenye vijenzi**: hufanya chapa nyingi na mada kuwa kuandika upya msimbo badala ya badiliko la usanidi.
- **Mabadiliko yanayovunja bila msaada wa uhamishaji**: timu zinazotumia zinakwama au kufanya fork mfumo.

## Kielelezo cha ukomavu

**Ngazi ya 1: Kuanzisha.** Kila timu inajenga UI yake papo hapo na kwa kuitikia. Hakuna vijenzi vya pamoja, mwonekano na tabia zisizo thabiti, rangi na nafasi zilizopachikwa kwa kila skrini. Kila usasishaji wa chapa ni kusaga kwa mkono skrini kwa skrini.

**Ngazi ya 2: Kuendeleza.** Mwongozo wa mtindo au maktaba ya vijenzi ya pamoja ipo lakini ni pungufu, ya hiari, na mara nyingi haiendani kati ya usanifu na msimbo. Baadhi ya timu zinaitumia, nyingine hazitumii, na mazoea ya msingi yanatofautiana sana timu hadi timu.

**Ngazi ya 3: Kusawazisha.** Mfumo wa usanifu wenye tokeni, maktaba ya msimbo inayodumishwa, nyaraka, na utawala umeandikwa na kutekelezwa shirika zima. Vijenzi hutumia tokeni za kisemantiki, mada zinaungwa mkono, na ufikivu na uitikiaji vimejengwa ndani badala ya kubanwa kwa kila skrini.

**Ngazi ya 4: Kusimamia.** Mfumo unapimwa na kudhibitiwa kwa data dhidi ya vipimo vya msingi. Usawa wa usanifu-na-msimbo unafuatiliwa kama kipimo wazi chenye malengo kwa kila bidhaa, majaribio ya regression ya kuona yanaendeshwa kwenye CI kunasa kuteleza, na uzingatiaji wa ufikivu unapimwa dhidi ya viwango badala ya kudhaniwa. Dashibodi za upokeaji zinaonyesha ufikiaji wa vijenzi kwa timu, na gharama na muda wa usasishaji wa chapa vinarekodiwa ili uboreshaji uonekane kwa muda.

**Ngazi ya 5: Kuratibu.** Mfumo wa usanifu ni bidhaa inayoboreshwa mfululizo, iliyounganishwa kuvuka shirika na inayojirekebisha kwa mabadiliko. Una matoleo, mpango wa barabara, na mfano wa mchango unaofanya kazi, kwa hiyo unabadilika na mahitaji halisi. Usasishaji wa chapa na mada mpya ni mabadiliko ya kawaida ya tokeni, mada za chapa nyingi na wapangaji wengi ni kawaida, na timu inastaafisha, kupanua upya, na kupandisha mifumo kwa ushahidi kutoka data ya matumizi, ikilisha zana za usanifu na mabomba ya utoaji kutoka chanzo kimoja cha ukweli.

## Mawazo ya kujadili

- Mnasawazishaje utawala wa kati dhidi ya uhuru wa timu bila kugawanyika wala kuzuia?
- Kipimo sahihi cha "usawa wa usanifu-na-msimbo" ni kipi, na mnakiweka cha uaminifu vipi?
- Timu inapaswa kuruhusiwa lini kujenga kijenzi cha mara moja badala ya kutumia mfumo?
- Mnafadhili na kuajiri vipi mfumo wa usanifu ili uokoke mizunguko ya bajeti na upangaji upya?
- Unyumbulifu wa mada kiasi gani unastahili gharama ya uondoaji iliyoongezwa?
- Mnahamishaje programu za urithi na zilizojengwa na wauzaji kwenye mfumo wa pamoja?

## Mambo muhimu ya kukumbuka

- Mfumo wa usanifu hugeuza maamuzi ya usanifu ya mara moja kuwa mtaji unaotumika tena, unaotawaliwa.
- Upange katika tabaka (tokeni, vijenzi, mifumo), na vijenzi vitumie tokeni za kisemantiki.
- Jenga ufikivu na uitikiaji ndani ya vijenzi ili kila timu virithi.
- Chukulia usawa wa usanifu-na-msimbo kama kipimo cha afya kinachopimika, si dhana.
- Tokeni hufanya usasishaji wa chapa na mada za chapa nyingi kuwa badiliko la data, si kuandika upya.
- Tawala mfumo kama bidhaa yenye mpango wa barabara, matoleo, na mfano wa mchango.
- Katika ukubwa wa mashirika makubwa na serikali, mfumo wa pamoja ndio uwekezaji wenye kiegemeo cha juu zaidi wa UI unaopatikana.

## Marejeo na usomaji zaidi

- Brad Frost, *Atomic Design*
- Alla Kholmatova, *Design Systems: A Practical Guide to Creating Design Languages*
- Josef Müller-Brockmann, *Grid Systems in Graphic Design*
- Robert Bringhurst, *The Elements of Typographic Style*
- Ellen Lupton, *Thinking with Type*
- Luke Wroblewski, *Mobile First*
- Ethan Marcotte, *Responsive Web Design*
- Nathan Curtis, writings on design tokens and design system governance
- W3C Design Tokens Community Group, format specification
- Government design systems (e.g., UK Government Design System, U.S. Web Design System) as reference implementations
