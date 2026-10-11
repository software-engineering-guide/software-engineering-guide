# 2.4 Prófunarstefna

## Yfirlit og tilgangur

[Prófunarstefna](https://en.wikipedia.org/wiki/Software_testing) er hið yfirvegaða safn vala um hvað á að prófa, á hvaða stigi, hversu sjálfvirkt og með hvaða öryggi, svo teymið þitt geti breytt kóða hratt án þess að brjóta hann. Próf eru það sem lætur stóra skipulagsheild setja upp oft og örugglega. Þau kóða væntanlega hegðun, grípa afturfarir og gefa verkfræðingum sjálfstraust til að [endurbyggja](https://en.wikipedia.org/wiki/Code_refactoring). Án samhangandi stefnu hneigjast prófanir til tveggja slæmra átta: fjarverandi (óttadrifin, hæg þróun) eða uppblásnar (þúsundir hægra, óáreiðanlegra prófa sem enginn treystir).

Fyrir stórt teymi skiptir stefnan meira máli en nokkurt eitt próf. Hundruð verkfræðinga sem vinna í sameiginlegum kóðagrunni þurfa hratt, áreiðanlegt öryggisnet. Án þess er sérhver breyting áhættusöm og sérhver útgáfa verður handvirk þolraun. Próf virka líka sem keyranleg skjölun fyrirhugaðrar hegðunar, sem er ómetanlegt þegar upphaflegir höfundar hafa haldið áfram. Stefnan ræður hvort prófasafnið þitt er eign sem hraðar afhendingu eða skuldbinding sem dregur úr henni.

Í fyrirtækja- og opinberu samhengi hefur prófun aukið vægi. Reglugerðir kunna að krefjast skjalfestrar prófaþekju og sönnunargagna. Öryggiskritísk kerfi og kerfi sem snúa að borgurum krefjast mikillar tryggingar. Aðgengis- og öryggisprófanir kunna að vera lagalega skyldaðar. Stefnan verður því að jafna hraða, öryggi, kostnað og regluvörslu og verður að líta á þekju sem merki, ekki markmið til að spila með.

## Meginreglur

- Prófaðu til að öðlast sjálfstraust til breytinga, ekki til að ná tölu.
- Kjóstu hröð, áreiðanleg, einangruð próf. Hæg eða óáreiðanleg próf tæra traustið sem gerir safn gagnlegt.
- Ýttu prófum á lægsta stig sem gefur raunverulegt sjálfstraust og taktu frá hæg, breið próf fyrir raunverulega samþættingaráhættu.
- Óáreiðanlegt próf er bilað próf. Líttu á óáreiðanleika sem fyrsta flokks galla.
- Þekja er merki, ekki markmið. Há þekja léttvægs kóða sannar lítið.
- Prófaðu hegðun og samninga, ekki útfærsluatriði, svo prófin lifi endurbyggingu.
- Gerðu ófallbundnar prófanir (aðgengi, afköst, öryggi) hluta af stefnunni, ekki eftiráhugsun.

## Ráðleggingar

### Notaðu prófapýramídann sem sjálfgefið og þekktu gagnrýni á hann

Hafðu sem sjálfgefið mörg hröð [einingapróf](https://en.wikipedia.org/wiki/Unit_testing), færri [samþættingarpróf](https://en.wikipedia.org/wiki/Integration_testing) og fá heildstæð (end-to-end) próf, því kostnaður og brothættni aukast eftir því sem umfang vex. Þekktu líka gagnrýnina: lögunin ætti að fylgja arkitektúrnum þínum, ekki kreddu. Þjónustuþungt kerfi gæti þurft stærra samþættingarlag („prófabikarinn“), og raunverulega markmiðið er sjálfstraust á hverja kostnaðar- og hraðaeiningu, ekki tiltekin skuggamynd. Hvað sem þú gerir skaltu forðast öfugan pýramída af aðallega hægum heildstæðum prófum.

### Taktu upp TDD, BDD og tilgreiningardrifna þróun þar sem þau hjálpa

Notaðu [prófdrifna þróun](https://en.wikipedia.org/wiki/Test-driven_development) (TDD) til að knýja hönnun og tryggja prófanleika, sérstaklega fyrir flókna rökfræði. Hún er hönnunaragi jafnt og prófunaragi. Notaðu [hegðunardrifna þróun](https://en.wikipedia.org/wiki/Behavior-driven_development) (BDD) til að tjá próf á sviðstungumáli sem þú deilir með hagsmunaaðilum, sem er verðmætt fyrir samþykkisviðmið í eftirlitsskyldu eða kröfuþungu umhverfi. Tilgreiningardrifin þróun gengur skrefi lengra: hún lítur á keyranlega tilgreiningu (samþykkta hegðun, tjáða sem dæmi) sem einu uppsprettu sannleikans sem bæði leiðir útfærsluna og staðfestir hana. Þetta blómstrar þar sem kröfur þurfa að vera rekjanlegar til samþykkissönnunar, eins og í opinberum og eftirlitsskyldum áætlunum. Tengt öllum þremur er **[vinstri-færsla prófana](https://en.wikipedia.org/wiki/Shift-left_testing)** (shift-left testing): að færa sannprófun eins snemma og mögulegt er í lífsferlinum, skrifa próf samhliða eða á undan kóðanum og keyra þau stöðugt, svo þú grípir galla þegar þeir eru ódýrastir að laga, frekar en í seinum prófunarfösum eða í framleiðslu. Ekkert af þessu er skylda alls staðar. Beittu þeim þar sem þau bæta við skýrleika.

### Beittu háþróuðum aðferðum á verðmætan kóða

Notaðu eiginleikabyggðar prófanir til að athuga fastayrðingar yfir mörg mynduð inntök, sem grípur jaðartilvik sem dæmabyggð próf missa af. Notaðu [fuzz-prófanir](https://en.wikipedia.org/wiki/Fuzzing) á þáttara og mörk óhæfs inntaks til að finna hrun og öryggisgalla. Notaðu [stökkbreytingarprófanir](https://en.wikipedia.org/wiki/Mutation_testing) til að mæla hvort prófin þín greina í raun innsprautaða galla, miklu betra gæðamerki en hrá þekja. Notaðu skyndimyndaprófanir af varúð fyrir raðgreint úttak og gættu þín á gildrunni að endursamþykkja skyndimyndir blindandi.

### Stýrðu prófagögnum og notaðu tilbúin gögn

Gerðu próf ákvarðandi með stýrðum, einangruðum prófagögnum og forðastu sameiginlega breytilega festu sem tengja próf saman. Búðu til [tilbúin gögn](https://en.wikipedia.org/wiki/Synthetic_data) sem endurspegla einkenni framleiðslu án þess að afhjúpa raunverulegar persónuupplýsingar, sem er nauðsynlegt þar sem persónuverndarreglur banna notkun framleiðslugagna í prófaumhverfi. Veittu verksmiðjur eða smiði svo hvert próf geti smíðað nákvæmlega þau gögn sem það þarf.

### Líttu á óáreiðanleg próf sem galla

Greindu óáreiðanleika sjálfvirkt, færðu óáreiðanleg próf út úr hindrandi leiðinni og lagaðu eða eyddu þeim innan frests. Safn sem bilar af handahófi þjálfar verkfræðinga í að hunsa bilanir, sem eyðileggur allt gildi þess. Rektu óáreiðanleikahlutföll og gerðu áreiðanleika að skýrum gæðamælikvarða á prófasafnið sjálft.

### Notaðu þekju sem merki og bættu við ófallbundnum prófunum

Mældu þekju til að finna óprófuð svæði, en breyttu henni ekki í hart markmið sem býður upp á spilun með staðhæfingalausum prófum. Bættu hana upp með stökkbreytingarprófunum til dýptar. Byggðu aðgengisprófanir (sjálfvirkar athuganir auk handvirkra úttekta), afkastaprófanir (álags- og töfgrunnlínur með afturfaragreiningu) og öryggisprófanir (ósjálfstæðisskönnun, [kyrrstæð greining](https://en.wikipedia.org/wiki/Static_program_analysis) og kvik prófun) inn í leiðsluna.

## Málamiðlanir: kostir og gallar

| Prófagerð / vinnubrögð | Kostir | Gallar |
|---|---|---|
| Einingapróf | Hröð, nákvæm, ódýr, stöðug | Missa samþættingar- og kerfisstigsgalla |
| Samþættingarpróf | Grípa viðmóts- og tengingagalla | Hægari, meiri uppsetning, brothættari |
| Heildstæð próf | Mesta sjálfstraust í raunverulegri hegðun | Hæg, óáreiðanleg, dýr í viðhaldi |
| TDD | Betri hönnun, tryggður prófanleiki | Námsferill, finnst hægt í fyrstu |
| Eiginleikabyggðar prófanir | Finnur jaðartilvik, kóðar fastayrðingar | Krefst hugsunar í eiginleikum, erfiðara að skrifa |
| Stökkbreytingarprófanir | Sönn mæling á skilvirkni prófa | Reikniaflsfrekt, hægt að keyra |
| Hátt þekjumarkmið | Dregur fram óprófaðan kóða | Hægt að spila með, getur hvatt til lítilla gilda prófa |

Meginmálamiðlunin er sjálfstraust gegn hraða og kostnaði. Breiðari próf gefa meira sjálfstraust en keyra hægar og brotna oftar. Þrengri próf eru hröð og stöðug en missa kerfisstigsgalla. Rétta blandan hámarkar sjálfstraust á hverja sekúndu endurgjafar og hverja klukkustund viðhalds. Og ofprófun er raunverulegur bilunarháttur: uppblásið safn óþarfra, hægra, brothættra prófa getur kostað meira en gallarnir sem það kemur í veg fyrir.

## Spurningar til að ræða með teyminu

1. **Hvaða ófallbundnu próf, aðgengi, afköst og öryggi, ættu að hindra útgáfu og hver ættu aðeins að skýra frá?** Þessi kafli heldur því fram að ófallbundnar prófanir eigi heima í stefnunni frekar en sem eftiráhugsun, og tekur fram að aðgengi geti verið lagalega skyldað og öryggisprófanir geti verið hluti af authority-to-operate sönnunum. Fyrir stórt eða borgarasnúið kerfi hægir hindrandi hlið á afhendingu, en aðgengis- eða öryggisgalli fundinn í framleiðslu ber úrbóta-, orðspors- og lagalegan kostnað sem dvergar prófið. Komdu með merkin sem ráða: reglugerðaráhættu þína, hvort kerfið snýr að borgurum og hve oft þessir gallar sleppa nú út í framleiðslu. Gerðu lagalega skyldaðar athuganir hindrandi og láttu lægri áhættuathuganir skýra frá með þróun, svo hliðið endurspegli raunverulega áhættu en ekki kreddu. Svarið setur beint hvað má og má ekki sameinast.

2. **Setur þú hart þekjuhlutfall sem hlið, og ef svo er, hvað kemur í veg fyrir að verkfræðingar spili með það með staðhæfingalausum prófum?** Kaflinn er staðfastur um að þekja sé merki, ekki markmið, að há þekja léttvægs kóða sanni lítið og að hart markmið bjóði upp á spilun. Ein tala lögð á yfir stóra skipulagsheild framleiðir áreiðanlega próf sem keyra kóða án þess að fullyrða nokkuð, sem hækkar mælikvarðann og lækkar raunverulegt sjálfstraust. Komdu með betra merki í umræðuna: stökkbreytingaprófunareinkunn á verðmætustu einingum þínum, sem mælir hvort prófin greina í raun innsprautaða galla. Notaðu þekju til að finna óprófuð svæði og stökkbreytingarprófanir til dýptar og standa gegn því að breyta hvoru tveggja í markmið sem forystan rekur í einangrun. Ákveddu hvar talan hjálpar raunverulega og hvar hún býður aðeins upp á leikhús.

3. **Hver er stefna þín þegar prófasafnið verður of hægt til að verkfræðingar bíði eftir því?** Meginmálamiðlun þessa kafla er sjálfstraust gegn hraða og kostnaði, og hann nefnir ofprófun sem raunverulegan bilunarhátt þar sem uppblásið, óþarft, hægt safn kostar meira en gallarnir sem það kemur í veg fyrir. Í stóru teymi er keyrslutími safns sameiginlegur skattur greiddur á hverja breytingu og safn sem fólk lærir að sniðganga missir allt gildi sitt. Komdu með sönnunargögnin: CI-veggklukkutíma, hægustu prófin og hve mikil óþörf heildstæð þekja tvítekur ódýrari einingapróf. Ýttu prófum á lægsta stig sem gefur raunverulegt sjálfstraust, samhliðaðu og eyddu óþörfum hægum prófum innan frests. Að fínstilla sjálfstraust á hverja sekúndu endurgjafar, ekki hráan fjölda prófa, er markmiðið.

4. **Þegar próf verður óáreiðanlegt, hver á það, hve hratt verður að laga það eða eyða og hvað framfylgir þeim frest?** Þessi kafli lítur á óáreiðanlegt próf sem bilað próf, fyrsta flokks galla, því safn sem bilar af handahófi þjálfar stórt teymi í að hunsa rauðar smíðar og eyðileggur hljóðlega öryggisnetið sem allir reiða sig á. Þrýstingurinn á móti er raunverulegur: að setja óáreiðanlegt próf í sóttkví opnar fyrir afhendingu í dag en hætta er á að hylja raunverulegan hlé-galla, á meðan að hindra á því stöðvar hundruð verkfræðinga vegna bilunar sem getur verið hreint suð. Komdu með sönnunargögnin sem útkljá það: núverandi óáreiðanleikahlutfall þitt, hve lengi próf sitja í sóttkví áður en nokkur snertir þau og hve mörg próf í sóttkví reyndust fela raunverulegan galla. Úthlutaðu eiganda á hvert próf í sóttkví, settu harðan frest til að laga eða eyða og rektu áreiðanleika sem skýran mælikvarða fyrir safnið sjálft. Í fyrirtækja- og opinberu umhverfi þar sem græn smíði er hluti útgáfusönnunar er óstýrður haugur prófa í sóttkví einnig úttektarskuldbinding, því þú ert að afhenda á merki sem þú hefur einkum samþykkt að vantreysta.

5. **Máttu nota framleiðslugögn í prófaumhverfi, og ef ekki, hvernig býrðu til tilbúin gögn trú nóg til að grípa raunverulega galla?** Kaflinn er beinn um að persónuverndarreglur banni oft raunveruleg persónugögn í prófun, og að tilbúin gögn þurfi að endurspegla framleiðslueinkenni eða prófin gefi falskt sjálfstraust. Fyrir stóra skipulagsheild er spennan milli trúfesti og regluvörslu: framleiðslugögn grípa sóðalegu jaðartilvikin sem tilbúin gögn missa af, en hvert afrit af þeim margfaldar útsetningu þína og skyldur. Komdu með sérkennin: hvaða gagnasöfn bera persónu- eða eftirlitsskyld gögn, hvað persónuverndar- og gagnabúsetureglur þínar krefjast í raun og hve vel núverandi festur þínar endurskapa dreifingarnar og jaðartilvikin sem sjást í framleiðslu. Staðlaðu verksmiðjur eða smiði svo hvert próf smíði nákvæmlega þau gögn sem það þarf og fjárfestu í tilbúinni gagnagerð sem passar við raunverulega lýðfræði- og magndreifingu. Í opinberum og eftirlitsskyldum áætlunum er að nota borgaragögn í prófaumhverfi ekki flýtileið, það er tilkynningarskyldur brestur, svo gagnastefnan verður að vera útkljáð áður en fyrsta umhverfið er sett upp.

6. **Hvar ættu TDD, BDD eða tilgreiningardrifin þróun að vera væntanleg frekar en valkvæð og hver ákveður?** Þessi kafli kynnir þetta sem aga til að beita þar sem þeir bæta við skýrleika, ekki skyldur fyrir hverja kóðalínu, en stórt teymi hagnast samt á sameiginlegu sjálfgefnu gildi svo vinnubrögð sundrist ekki teymi fyrir teymi. Málamiðlunin er milli hönnunar- og rekjanleikaávinnings (keyranlegar tilgreiningar sem stefnusérfræðingar geta rýnt, próf sem lifa endurbyggingu) og raunverulegs námsferils og fyrirframhægfara sem gera altæka skyldu að slá aftur. Komdu með sönnunargögn til að afmarka það: hvaða einingar bera flókna rökfræði eða hátt bilanahlutfall breytinga, hvar samþykkisviðmið þurfa að vera rekjanleg til krafna og hvernig teymi sem þegar iðka þetta skýra frá hraða og gallahlutfalli. Taktu frá væntinguna fyrir flókna rökfræði og kröfuþung svæði og láttu einfaldari kóða velja sjálfan. Í eftirlitsskyldum og opinberum áætlunum þar sem hugbúnaður verður að vera rekjanlegur til laganna sem hann útfærir er tilgreiningardrifin þróun með keyranlegum samþykkissönnunum minna val en leið að authority-to-operate, svo nefndu berum orðum hvar hennar er krafist.

## Sjónarhorn eftir geirum

**Sprotafyrirtæki.** Pínulítið teymi getur ekki mannað gæðaprófanir, svo láttu safnið vinna fyrir sér: hröð einingapróf á hverju commit auk fárra heildstæðra prófa yfir eina leiðina sem borgar reikningana, og ekkert sem þú munt ekki viðhalda. Slepptu þekjumarkmiðum og prófaðu rökfræðina sem þú óttast mest að brjóta, svo þú getir afhent nokkrum sinnum á dag án handvirkrar afturfaraathugunar. Lagaðu óáreiðanlegt próf sama dag, því á þessu stigi er safn sem teymið lærir að hunsa verra en ekkert safn.

**Lítið fyrirtæki.** Án sérstaks prófunarverkfræðings og með þröngt fjárhagsáætlun skaltu hallast að prófunum sem eru innbyggðar í rammana og verkfærin sem þú keyrir þegar frekar en sérsmíðað prófunarkerfi sem þú getur ekki stutt. Forgangsraðaðu fáum athugunum sem vernda tekjur og traust viðskiptavina og notaðu hýst CI svo þú sért ekki að viðhalda smíðainnviðum sjálfur. Kjóstu að kaupa aðgengis- og öryggisskönnun sem þjónustu frekar en að smíða hana, því einn missir galli getur kostað meira en ár af verkfærinu.

**Stórfyrirtæki.** Yfir mörg teymi er stefnuvandinn samræmi: sameiginlegt pýramídasjálfgefið, sjálfvirk sóttkví óáreiðanlegra prófa og ófallbundin hlið sem þýða það sama alls staðar, svo græn smíði sé áreiðanleg sama hver framleiddi hana. Fjárhagsáætlaðu keyrslutíma safns sem sameiginlegan skatt og samhliðaðu af krafti, því CI-veggklukkutími er greiddur á hverja breytingu af hverjum verkfræðingi. Stýrðu þekju og stökkbreytingareinkunnum sem eignasafnsmerkjum með skýru eignarhaldi, ekki tölum sem forystan rekur í einangrun.

**Hið opinbera.** Innkaup og eftirlit gera prófun að sönnunargögnum, ekki bara verkfræðihreinlæti. Settu fram hæfis- og stefnureglur sem keyranlegar tilgreiningar rýndar af sviðssérfræðingum, svo þú getir rakið hugbúnaðinn til laganna sem hann útfærir, og gerðu aðgengis- og öryggisprófanir hindrandi því þær eru lagalega skyldaðar og hluti authority-to-operate sönnunar. Notaðu tilbúin gögn mynduð til að passa við raunverulegar dreifingar, því borgaragögn í prófaumhverfi eru tilkynningarskyldur brestur, og haltu prófaafurðum úttektarhæfum svo ytri rýnir geti staðfest nákvæmlega hvað var sannreynt.

## Dæmi

**Sprotafyrirtæki.** Fimm manna sprotafyrirtæki hefur ekki efni á gæðateymi, svo það hallast að hröðu einingaprófasafni sem keyrir á hverju commit auk fárra heildstæðra prófa sem ná yfir skráningar-til-greiðslu leiðina sem borgar reikningana. Stofnendurnir sleppa tæmandi þekju og prófa í staðinn rökfræðina sem þeir óttast mest að brjóta, sem lætur þá afhenda nokkrum sinnum á dag án handvirkrar afturfaraathugunar. Þegar óáreiðanlegt próf byrjar að bila af handahófi laga þeir það sama dag, því safn sem teymið lærir að hunsa er verra en ekkert safn á því stigi þar sem traust er allt.

**Stórfyrirtæki.** Stór vefverslunarvettvangur heldur úti þúsundum hraðra einingaprófa sem keyra á hverju commit á mínútum, markvissu safni samþættingarprófa í kringum greiðslu- og birgðamörk og litlu safni heildstæðra prófa fyrir mikilvægu afgreiðsluferðirnar. Óáreiðanleg heildstæð próf eru sjálfvirkt sett í sóttkví og úthlutað til viðgerðar. Því verkfræðingar treysta safninu setja þeir upp mörgum sinnum á dag, öruggir um að rauð smíði þýði raunverulegt vandamál.

**Hið opinbera.** Landsbundið bótakerfi sem starfar undir eftirliti notar BDD til að tjá hæfisreglur sem keyranlegar tilgreiningar rýndar af stefnusérfræðingum, sem gefur rekjanlega sönnun þess að hugbúnaðurinn útfæri lögin. Það notar tilbúin gögn mynduð til að passa við raunverulegar lýðfræðidreifingar, því persónuverndarreglur banna borgaragögn í prófaumhverfi. Aðgengisprófanir eru skyldar og hindra útgáfu, þar sem þjónustan verður að vera nothæf öllum borgurum. Og öryggisprófanir eru hluti authority-to-operate (ATO) sönnunar, formlega samþykkisins til að reka kerfið í framleiðslu.

## Viðskiptarök: hvatar, ávöxtun fjárfestingar og heildarkostnaður

Ávöxtun prófana er hæfileikinn til að breyta hugbúnaði hratt og örugglega, sem er grunnur viðvarandi afhendingarhraða. Áreiðanlegt sjálfvirkt safn kemur í stað hægra, dýrra handvirkra [afturfaraprófana](https://en.wikipedia.org/wiki/Regression_testing) og grípur galla þegar þeir eru ódýrastir að laga, fyrir útgáfu frekar en í framleiðslu. Í eftirlitsskyldu eða borgarasnúnu kerfi dvergar kostnaður framleiðslugalla (úrbætur, orðspor og hugsanleg lagaleg áhætta) kostnað prófanna sem hefðu gripið hann.

Upptökukostnaðurinn er raunverulegur: þú skrifar og viðheldur prófum og smíðar [samfellda samþættingar](https://en.wikipedia.org/wiki/Continuous_integration) (CI) innviði. En kostnaðurinn við að prófa ekki er hærri og safnast upp: óttadrifin þróun sem hægir niður í skrið, tíðar afturfarir og handvirk útgáfuferli sem skala ekki. Það er líka kostnaður við ofprófun, svo rökin eru fyrir vel hannaðri stefnu, ekki hámarksfjölda prófa. Til að færa rök við forystu skaltu tengja safnið við uppsetningartíðni, bilanahlutfall breytinga og meðaltíma til endurheimtar og magngreina handvirku prófunarvinnuna sem það kemur í stað og framleiðsluatvikin sem það kemur í veg fyrir.

## Andmynstur og gildrur

- **Ísjakaprófanir (ice-cream-cone):** aðallega hæg heildstæð próf yfir þunnum einingagrunni. Hægt, óáreiðanlegt, dýrt.
- **Þekja sem markmið:** að elta prósentu með staðhæfingalausum eða léttvægum prófum sem sanna ekkert.
- **Að prófa útfærsluatriði:** próf tengd innviðum sem brotna við hverja endurbyggingu og letja breytingar.
- **Umborinn óáreiðanleiki:** handahófskenndar bilanir sem þjálfa teymið í að hunsa rauðar smíðar.
- **Sameiginleg breytileg prófagögn:** próf sem trufla hvert annað og bila ófyrirsjáanlega.
- **Notkun framleiðslugagna í prófun:** persónuverndar- og regluvarslubrestur sem bíður þess að gerast.
- **Ófallbundnar prófanir sleppt:** aðgengi, afköst og öryggi uppgötvuð aðeins í framleiðslu.
- **Vantreysta safnið:** svo óáreiðanlegt að verkfræðingar endurkeyra eða sniðganga það reglulega og gera tilgang þess að engu.

## Þroskalíkan

- **Stig 1, Upphaf:** Prófun er handvirk og viðbragðsdrifin. Sjálfvirk þekja er í lágmarki. Afturfarir eru tíðar og gripnar seint, oft af notendum frekar en safninu.
- **Stig 2, Þróun:** Sjálfvirk einingapróf og nokkur samþættingarpróf eru til, en safnið er hægt eða óáreiðanlegt, traust er lítið og vinnubrögð eru mjög ólík milli teyma.
- **Stig 3, Stöðlun:** Jafnvægt, hratt, áreiðanlegt safn hliðar hverja breytingu. Skjalfest pýramídasjálfgefið, stefna um óáreiðanleg próf og ófallbundnar prófanir (aðgengi, afköst, öryggi) eru framfylgt samræmt milli teyma.
- **Stig 4, Stjórnun:** Heilsa safnsins er mæld og stýrð gegn grunnlínum. Óáreiðanleikahlutfall, CI-veggklukkutími, stökkbreytingareinkunn á verðmætum einingum og hlutfall galla sem sleppa eru rakin og rýnd. Þekja er eitt merki meðal nokkurra og hlið kalla fram á grundvelli gagna frekar en skoðana.
- **Stig 5, Samhæfing:** Háþróaðar aðferðir (eiginleikabyggðar, stökkbreytingar, fuzz) beinast að verðmætum kóða. Prófun er samþætt afhendingarmælikvörðum eins og uppsetningartíðni, bilanahlutfalli breytinga og meðaltíma til endurheimtar. Skipulagsheildin endurmótar safnið stöðugt að arkitektúr og áhættu, leggur niður óþörf próf og fjárfestir þar sem gögn sýna að gallar sleppa enn.

## Hugmyndir til umræðu

- Hvaða lögun hefur prófadreifing þín í raun og samsvarar hún arkitektúr og áhættu þinni?
- Hvernig ákveðurðu hvenær kóði verðskuldar eiginleikabyggðar eða stökkbreytingarprófanir á móti dæmaprófum?
- Hver er stefna þín um óáreiðanleg próf og er henni í raun framfylgt?
- Hvernig býrðu til raunhæf tilbúin gögn án þess að leka viðkvæmum upplýsingum?
- Hvar hjálpar þekja þér raunverulega og hvar hefur verið spilað með hana?
- Hvernig ætti að rýna gervigreindarmynduð próf svo þau bæti við sjálfstrausti frekar en suði?

## Helstu atriði

- Prófaðu til að öðlast sjálfstraust til breytinga. Fínstilltu sjálfstraust á hverja hraða- og kostnaðareiningu.
- Notaðu pýramídann sem sjálfgefið en mótaðu prófanir að arkitektúrnum þínum.
- Líttu á óáreiðanleg próf sem galla og þekju sem merki, ekki markmið.
- Beittu háþróuðum aðferðum þar sem verðmætið réttlætir kostnaðinn.
- Hafðu aðgengis-, afkasta- og öryggisprófanir með í stefnunni og notaðu tilbúin gögn til að vernda persónuvernd.

## Heimildir og frekari lestur

- Kent Beck, *Test-Driven Development: By Example*
- Lisa Crispin and Janet Gregory, *Agile Testing: A Practical Guide for Testers and Agile Teams*
- Gerard Meszaros, *xUnit Test Patterns: Refactoring Test Code*
- Michael Feathers, *Working Effectively with Legacy Code*
- Nicole Forsgren, Jez Humble, Gene Kim, *Accelerate: The Science of Lean Software and DevOps*
- Martin Fowler, articles on the Test Pyramid and test-related patterns
