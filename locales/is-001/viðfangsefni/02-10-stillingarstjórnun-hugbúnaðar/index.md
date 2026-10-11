# 2.10 Stillingarstjórnun hugbúnaðar

## Yfirlit og tilgangur

[Stillingarstjórnun hugbúnaðar](https://en.wikipedia.org/wiki/Software_configuration_management) (SCM) er sú grein að auðkenna íhluti hugbúnaðarkerfis, stýra því hvernig þeir breytast, skrá ástand hverrar breytingar og sannreyna að það sem þú smíðaðir og afhentir samsvari því sem þú ætlaðir. Hún svarar spurningu sem hljómar einföld en verður erfið í stórum stíl: hvað er nákvæmlega í þessari útgáfu, hvernig komst það þangað og hver samþykkti? [SWEBOK](https://en.wikipedia.org/wiki/Software_Engineering_Body_of_Knowledge) lítur á SCM sem grundvallarþekkingarsvið af skýrri ástæðu: sérhver önnur verkfræðiaðgerð þarf stöðuga, þekkta stillingu til að vinna gegn.

Í stóru teymi er SCM bindivefurinn sem heldur þúsundum hreyfanlegra hluta samhangandi. Frumkóði, bókasöfn, ílátsmyndir, innviðaskilgreiningar, stillingargögn, skjölun og prófaafurðir breytast allt á eigin klukku, og afhent kerfi er ein tiltekin samsetning tiltekinna útgáfa af þeim öllum. Án yfirvegaðrar stillingarstjórnunar er sú samsetning óþekkt og ekki hægt að endurskapa hana. Þú getur ekki endurskapað liðna útgáfu, rakið galla til breytingarinnar sem olli honum né sagt með öryggi hvað er í gangi í framleiðslu.

Fyrirtækja- og opinbert umhverfi hækka hagsmunina. Eftirlitsskyldar og opinberar áætlanir þurfa að sýna að breytingar voru heimilaðar, rýndar og skráðar, að afhent smíði rekist til samþykktra krafna og frumkóða og að ekkert hafi komist inn í kerfið óstýrt. Hér er SCM jafn mikið sönnunarkerfi og verkfræðikerfi. [Útgáfustýring](https://en.wikipedia.org/wiki/Version_control) (kafli 2.6) stýrir frumkóðasögu. SCM stýrir allri stillingunni og stýrða ferlinu sem hún breytist með. Hún er nátengd [innviðum sem kóða](https://en.wikipedia.org/wiki/Infrastructure_as_code) (kafli 8.2), afhendingarleiðslum (kafli 8.1) og úttekt og tryggingu (kafli 10.2).

## Meginreglur

- Allt sem ákvarðar hegðun kerfis er [stillingaratriði](https://en.wikipedia.org/wiki/Configuration_item) undir stjórn, ekki bara frumkóði.
- [Grunnlína](https://en.wikipedia.org/wiki/Baseline_(configuration_management)) er þekktur, samþykktur viðmiðunarpunktur. Breytingar eru gerðar gegn grunnlínum af ásetningi, ekki af tilviljun.
- Breyting er stýrð og skráð, ekki komið í veg fyrir hana. Markmiðið er heimiluð, rekjanleg breyting.
- Stöðubókhald þýðir að þú getur alltaf svarað hvað er í stillingu og hver breytingasaga hennar er.
- Úttektir sannreyna að smíðað og afhent kerfi samsvari skráðri stillingu og samþykktum kröfum.
- Endurgeranleiki er óumsemjanlegur: hver útgefin útgáfa verður að vera endursmíðanleg úr stýrðum inntökum.
- Sjálfvirknivæddu auðkenningu, skráningu og sannprófun. Handvirkt bókhald skalar ekki og lifir ekki úttekt.

## Ráðleggingar

### Skilgreindu SCM-ferlið og úthlutaðu eignarhaldi

Skrifaðu niður SCM-áætlun sem segir hvað er undir stillingarstjórn, hvernig atriði eru auðkennd, hvernig breytingar eru lagðar til og samþykktar og hvernig staða er skráð og úttektuð. Úthlutaðu skýru eignarhaldi, svo sem stillingarstjóra eða ábyrgu teymi, svo SCM sé ekki verk allra og því ekki neins. Kvarðaðu ferlið að áhættu: lítið innra verkfæri þarf létta stjórn, á meðan öryggiskritískt eða eftirlitsskylt kerfi þarf formlegar stjórnir og skrár. Festu áætlunina við viðurkenndan staðal eins og IEEE 828 svo endurskoðendur og samstarfsaðilar geti fylgt henni.

### Auðkenndu stillingaratriði og settu grunnlínur

Skráðu stillingaratriðin sem ákvarða hvernig kerfið hegðar sér: frumkóða, ósjálfstæði, smíðaskriftur, ílátsmyndir, innviðaskilgreiningar, stillingargögn, skemu og lykilskjöl. Gefðu hverju stöðugt auðkenni og útgáfukerfi. Settu grunnlínur á marktækum punktum (útgefin útgáfa, samþykkt kröfusett, vottuð smíði) svo þú hafir samþykktan viðmiðunarpunkt til að breyta gegn og snúa aftur til. Grunnlína er óbreytanleg: þegar þú hefur lýst henni yfir breytirðu henni ekki. Þú leysir hana aðeins af hólmi með nýrri grunnlínu búinni til gegnum breytingaferlið.

### Stýrðu breytingum gegnum skilgreint ferli og viðeigandi stjórnir

Beindu breytingum á stýrðum atriðum gegnum skilgreinda leið: tillögu, áhrifamat, samþykki, innleiðingu og sannprófun. Fyrir áhættumeiri atriði skaltu nota [breytingastýringarstjórn](https://en.wikipedia.org/wiki/Change_control_board) (CCB) sem vegur kostnað, áhættu og tímaáætlun áður en hún heimilar breytingu. Stilltu stjórnina að stærð: létt sjálfvirkt hlið fyrir venjulegar kóðabreytingar og formlega þverfaglega CCB fyrir breytingar sem snerta grunnlínur, viðmót eða eftirlitsskylda hegðun. Skráðu hverja ákvörðun og rökin að baki henni og tengdu mikilvægar stillingarákvarðanir við ákvörðunarskrár (kafli 1.6) svo rökin lifi.

### Haltu stillingarstöðubókhaldi

Haltu nákvæmri, fyrirspurnarhæfri skrá yfir hvert stillingaratriði: núverandi útgáfu þess, hvaða grunnlínu það tilheyrir og breytingabeiðnirnar sem beitt var á það. Þetta stöðubókhald er það sem leyfir þér að svara, hvenær sem er, hvað útgáfa inniheldur og hvernig hún komst þangað. Myndaðu skrána sjálfvirkt úr skráningarverkfærum þínum (útgáfustýringu, leiðslu, afurðasafni) í stað þess að viðhalda samhliða töflureikni sem rekur frá raunveruleikanum. Þessi skrá er burðarás rekjanleika frá kröfu til breytingar til smíðar til uppsetningar.

### Framkvæmdu stillingarúttektir

Sannreyndu tvennt á reglulegri áætlun. Fallbundin stillingarúttekt staðfestir að stillingin framkvæmi eins og kröfur hennar tilgreina. Líkamleg stillingarúttekt staðfestir að afhentar afurðir samsvari skráðri stillingu: að smíðin hafi komið úr skráðum frumkóða og ósjálfstæðum og innihaldi ekkert óútskýrt. Sjálfvirknivæddu eins mikið af þessu og þú getur: [endurgeranlegar smíðar](https://en.wikipedia.org/wiki/Reproducible_builds), afurðaprófsummur, hugbúnaðarefnisskrár (SBOM) og herkomuvottanir breyta úttekt úr handvirkri skoðun í samfellda athugun.

### Stýrðu útgáfum og afhendingu sem stýrðum atburðum

Líttu á útgáfu sem tiltekna, auðkennda grunnlínu afhenta gegnum endurtakanlegt ferli. Útgáfustýrðu útgáfur þínar skýrt, framleiddu skrá eða efnisskrá sem lýsir nákvæmlega hvað er innifalið og skráðu kortlagninguna frá útgáfu til frumkóðaendurskoðunar til uppsettrar afurðar. Undirritaðu og prófsummaðu útgefnar afurðir svo hver sem er neðar geti sannreynt heilindi þeirra. Tengdu útgáfustjórnun inn í afhendingarleiðsluna (kafli 8.1) svo framvinda gegnum umhverfi sé sjálf stýrð, skráð og afturkræf.

### Veldu og samþættu SCM-verkfæri

Hallaðu þér að verkfærum sem sjálfvirknivæða auðkenningu, stjórn, bókhald og úttekt frekar en að treysta á aga einan: útgáfustýringu fyrir frumkóða, afurða- og myndasöfn fyrir tvíundir, óbreytanlega leiðslu fyrir smíðar, innviði sem kóða fyrir umhverfi og ósjálfstæðis- og SBOM-verkfæri fyrir herkomu. Tengdu þau svo ein breyting flæði rekjanlega frá commit til uppsettrar útgáfu. Það sem þú sækist eftir er verkfærakeðja þar sem stillingarskráin er aukaafurð þess að vinna verkið, ekki aðskilið skrifstofuverk.

## Málamiðlanir: kostir og gallar

| Val | Kostir | Gallar |
|---|---|---|
| Formlegar breytingastýringarstjórnir | Sterk heimild og úttektarslóð, áhætta vegin fyrir breytingu | Hægari afköst, yfirbygging ef beitt á venjulegar breytingar |
| Létt sjálfvirk hlið | Hratt flæði, lítil yfirbygging, skalar á margar breytingar | Veikari fyrir áhættumiklar grunnlínur, minni yfirvegun |
| Strangar óbreytanlegar grunnlínur | Endurgeranlegir, úttektarhæfir viðmiðunarpunktar | Agi og verkfæri krafist, núningur ef ofnotað |
| Sjálfvirkt stöðubókhald | Nákvæm, alltaf núverandi skrá, úttektarhæf | Verkfæri og samþættingarfjárfesting fyrirfram |
| Handvirkar stillingarskrár | Einfalt að byrja, engin verkfæri | Rekur frá raunveruleikanum, bregst í stórum stíl og undir úttekt |

Meginmálamiðlunin er stjórn gegn flæði. Þung breytingastjórn gefur sterka tryggingu en hægir á afhendingu. Létt stjórn flæðir hratt en veikir rekjanleika. Svarið er ekki að velja eitt altækt. Það er að stigskipta stjórn eftir áhættu: sjálfvirknivæða venjulegar breytingar gegnum hröð hlið og taka frá formlegar stjórnir og óbreytanlegar grunnlínur fyrir atriðin þar sem heimild og úttektarhæfi skipta raunverulega máli. Önnur málamiðlunin er verkfærafjárfesting fyrirfram gegn viðvarandi skrifstofukostnaði og úttektaráhættu. Sjálfvirkt bókhald kostar meira að koma upp og mun minna að lifa með.

## Spurningar til að ræða með teyminu

1. **Hvað á nákvæmlega heima á stillingaratriðalistanum okkar og hver á ákvörðunina þegar eitthvað nýtt birtist?** SCM virkar aðeins ef listi stýrðra atriða samsvarar mengi hlutanna sem raunverulega ákvarða hegðun, og í stóru kerfi er það mengi stærra en flest teymi halda: frumkóði, ósjálfstæði, smíðaskriftur, ílátsmyndir, innviðaskilgreiningar, skemu, eiginleikarofar og stillingargögnin sem breyta hljóðlega því sem hugbúnaðurinn gerir. Ef enginn á listann úreldist hann og atriðið sem felldi þig í framleiðslu reynist vera það eina sem enginn hugsaði um að stýra. Komdu með núverandi skrá þína á fundinn og leitaðu að hegðunarákvarðandi atriðum sem vantar í hana. Úthlutaðu ábyrgum eiganda (stillingarstjóra eða nefndu teymi) svo að bæta við nýju atriði sé yfirveguð ákvörðun, ekki slys, því SCM sem er verk allra er verk enginn.

2. **Getum við sannað að uppsett afurð hafi komið úr frumkóðanum og leiðslunni sem við höldum, og myndi sú sönnun lifa af átroðning?** Endurgeranleiki og rekjanleiki eru allur tilgangur SCM, og beitta útgáfa spurningarinnar er hvort þú getur tengt keyrandi tvíund aftur við tiltekið commit og smíðakeyrslu með sönnunargögnum, ekki fullyrðingu. Í eftirlitsskyldu eða hávirðiskerfi er þetta líka aðfangakeðjuvörn þín: undirritaðar herkomuvottanir, afurðaprófsummur og hugbúnaðarefnisskrá breyta „við erum nokkuð viss“ í eitthvað sem endurskoðandi eða atvikaviðbragðsaðili getur sannreynt. Komdu með síðustu útgáfu þína og reyndu að ganga hana afturábak frá uppsettu afurðinni til samþykktu breytingarinnar. Ef einhver hlekkur er handvirk fullyrðing frekar en skráður, sannprófanlegur tengill, þar getur árásaraðili eða heiðarleg mistök læðst inn einhverju ósýnilega, og að loka því þýðir að tengja undirritun og herkomu inn í leiðsluna svo skráin sé aukaafurð afhendingar.

3. **Getur einhver breytt útgáfu á staðnum í dag og hvað myndi það gera við getu okkar til að treysta henni?** Grunnlína er aðeins gagnleg ef hún er óbreytanleg: um leið og „útgáfunni“ er hægt að breyta eftirá geturðu ekki lengur endurskapað hana né reitt þig á hana sem viðmiðun, og hver úttekt niðurstreymis verður fornleifafræði. Klassíska bilunin er stilling breytt beint í framleiðslu eða merki hljóðlega fært, sem er einmitt flýtileiðin sem finnst skaðlaus og gerir útgáfu ómögulega að endurgera síðar. Komdu með heiðarlega svarið á fundinn: hver hefur aðgang til að breyta uppsettri grunnlínu án þess að fara gegnum breytingaferlið og hefur það gerst? Lagfæringin er að gera grunnlínur raunverulega óbreytanlegar og beina hverri breytingu gegnum tillögu, áhrifamat, samþykki og sannprófun, með því að stigskipta nákvæmni svo venjulegar breytingar flæði gegnum hröð sjálfvirk hlið á meðan grunnlínu- og eftirlitsskyldar breytingar fara til stjórnar.

4. **Er stillingarstöðubókhald okkar myndað sjálfvirkt úr skráningarverkfærum okkar eða viðhaldið í höndunum og hve langt hefur það rekið frá því sem er raunverulega uppsett?** Stöðubókhald er skráin sem leyfir þér að svara, hvenær sem er, hvað útgáfa inniheldur og hvernig hún komst þangað, og í stóru kerfi er sú skrá aðeins áreiðanleg ef hún fellur út úr vinnunni frekar en að vera slegin inn í samhliða töflureikni. Togið á móti er að handhaldin skrá finnst ódýr að byrja og sveigjanleg, á meðan að sjálfvirknivæða hana þýðir að samþætta útgáfustýringu, leiðsluna og afurðasafnið svo skráin verði aukaafurð afhendingar. Komdu með skrána sem þú reiðir þig á í dag, veldu þrjár nýlegar útgáfur af handahófi og athugaðu hvort skráðar útgáfur, grunnlínur og beittar breytingabeiðnir samsvari því sem verkfærin segja að hafi verið afhent. Fyrir fyrirtækja- eða opinbera áætlun er stöðuskrá sem víkur frá raunveruleikanum ekki snyrtimennskuvandi, hún er úttektarniðurstaða sem bíður þess að gerast, því endurskoðandi sem grípur eitt bil hættir að treysta allri frásögninni og biður þig að endurgera hana í höndunum.

5. **Er breytingastjórn okkar stigskipt eftir áhættu, eða stýrir sama stig helgisiða hverri breytingu óháð því hvað hún snertir?** Stjórn og flæði toga hvort gegn öðru: formleg breytingastýringarstjórn vegur kostnað, áhættu og tímaáætlun áður en hún heimilar breytingu, en að beita þeim helgisið á venjulega kóðalagfæringu bætir bara við töf, á meðan að ýta sameiginlegri grunnlínu eða eftirlitsskyldu greiðsluflæði gegnum hratt sjálfvirkt hlið fjarlægir yfirvegun einmitt þar sem þú þarft hana. Bilunarhættirnir eru samhverfir, einsleit þyngd sem fólk lærir að fara fram hjá, eða einsleit slökun sem lætur áhættumikla breytingu renna í gegn órannsakaða. Komdu með úrtak af breytingum síðasta ársfjórðungs flokkað eftir því hvað hver snerti og athugaðu hvort nákvæmnin sem hún fékk samsvaraði í raun áhættu hennar. Í eftirlitsskyldu eða opinberu umhverfi skaltu nefna hvaða atriðaflokkar verða að ná til þverfaglegrar stjórnar og hverjir mega flæða gegnum sjálfvirk hlið og skrá þá stigskiptingu skýrt, því „við notum dómgreind“ er ekki stýring sem endurskoðandi eða eftirlitsaðili getur sannreynt.

6. **Hvenær keyrðum við síðast fallbundna og líkamlega stillingarúttekt og hve mikið af sönnunargögnunum væri lifandi skrá frekar en endurgerð?** Fallbundin stillingarúttekt staðfestir að kerfið framkvæmi eins og kröfur þess tilgreina og líkamleg stillingarúttekt staðfestir að afhentar afurðir samsvari skráðri stillingu og innihaldi ekkert óútskýrt. Slepptu þeim og þú treystir því að grunnlínur þínar og stöðubókhald séu heiðarleg án þess nokkurn tíma að athuga. Spennan er kostnaður: handvirkar úttektir eru hægar og sársaukafullar, sem er einmitt ástæða þess að teymi fresta þeim, og leiðin út er að sjálfvirknivæða athuganirnar með endurgeranlegum smíðum, afurðaprófsummum, hugbúnaðarefnisskrám og herkomuvottunum svo sannprófun verði samfelld. Komdu með nýjustu útgáfu þína og reyndu að framleiða, á staðnum, rekjanleikaslóðina frá kröfu til breytingar til smíðar til uppsetningar og sönnunina frá afurð til frumkóða. Fyrir fyrirtækja- og opinberar áætlanir er þessi sönnunarslóð það sem vottun og eftirlit krefjast, svo heiðarlega spurningin er hvort úttekt morgundagsins yrði svarað úr skrám sem þú heldur nú þegar eða úr fornleifaæfingu sem þú hefur ekki efni á.

## Sjónarhorn eftir geirum

**Sprotafyrirtæki.** Haltu SCM léttu en raunverulegu. Settu frumkóða, innviðaskilgreiningar og stillingargögn í útgáfustýringu og gerðu hverja útgáfu að merktri smíði framleiddri af einni leiðslu frekar en handsamsettri afurð. Slepptu breytingastýringarstjórnum og formlegum grunnlínum, sem eru ofgnótt í þinni stærð, en leyfðu aldrei neinum að breyta stillingu beint í framleiðslu, því sú eina flýtileið er það sem gerir útgáfu ómögulega að endurskapa þegar viðskiptavinur rekst á galla næsta þriðjudag.

**Lítið fyrirtæki.** Án stillingarstjóra og með þröngt fjárhagsáætlun skaltu hallast að verkfærum sem gefa þér SCM nánast ókeypis: hýstum útgáfustýringarvettvangi, innbyggðri leiðslu hans og afurðasafni, svo stillingarskráin sé aukaafurð frekar en verk sem þú þarft að manna. Keyptu þessa getu innbyggða í verkfæri sem þú borgar nú þegar fyrir í stað þess að smíða sérsniðið ferli. Eyddu af skornum skammti athygli í tvær venjur sem skipta mestu, endurgeranlegar merktar útgáfur og að halda hegðunarbreytandi stillingu frá handvirkum framleiðslubreytingum.

**Stórfyrirtæki.** Vandinn er samræmi milli margra teyma: sameiginleg SCM-áætlun, sameiginlegt stillingaratriðaflokkunarkerfi, stigskipt breytingastýring og stöðubókhald myndað sjálfvirkt úr útgáfustýringu, afurðasafni og leiðslu. Taktu frá formlegar breytingastýringarstjórnir og óbreytanlegar grunnlínur fyrir sameiginlega vettvanga og eftirlitsskyld flæði, láttu venjulegar breytingar flæða gegnum sjálfvirk hlið og staðlaðu undirritaða herkomu og SBOM svo hægt sé að rekja útgáfu hvers teymis og hver endurskoðandi geti spurt lifandi skrá í stað þess að panta endurgerð.

**Hið opinbera.** Innkaupareglur, gagnsæi og almenn ábyrgð móta ferlið. Fylgdu formlegri SCM-áætlun í samræmi við viðurkenndan staðal eins og IEEE 828, settu grunnlínur á stillingaratriði við samningsbundna áfanga og beindu hverri breytingu á stýrða grunnlínu gegnum stjórn sem skráir áhrif, ákvörðun og rök. Krefstu þess að afhentar afurðir séu endurgeranlegar úr stýrðum inntökum, prófsummaðar og rekjanlegar frá enda til enda frá samþykktri kröfu til afhentrar smíði, því sú skjalfesta sönnunarslóð er einmitt það sem vottun, úttekt og almennt eftirlit krefjast.

## Dæmi

**Sprotafyrirtæki.** Sex manna sprotafyrirtæki heldur SCM léttu en raunverulegu: frumkóði, innviðaskilgreiningar og stillingargögn búa öll í útgáfustýringu, og hver útgáfa er merkt, útgáfustýrð smíði framleidd af sömu leiðslu frekar en handsamsett. Þegar viðskiptavinur tilkynnir galla sem birtist síðasta þriðjudag rekja þeir uppsetta afurð aftur til nákvæms commit á mínútum í stað þess að giska. Þeir sleppa breytingastýringarstjórnum og formlegum grunnlínum, sem væru ofgnótt í þeirra stærð, en þeir neita að leyfa neinum að breyta stillingu beint í framleiðslu, því sú eina flýtileið er það sem gerir útgáfu ómögulega að endurskapa síðar.

**Stórfyrirtæki.** Stórt fjármálaþjónustufyrirtæki setur allar uppsetningarhæfar afurðir, innviðaskilgreiningar og stillingargögn undir stillingarstjórn. Hver útgáfa er óbreytanleg, útgáfustýrð grunnlína með myndaðri hugbúnaðarefnisskrá, og hver uppsett afurð ber undirritaða herkomuvottun sem tengir hana við tiltekna frumkóðaendurskoðun og leiðslukeyrslu. Venjulegar forritabreytingar flæða gegnum sjálfvirk leiðsluhlið, á meðan breytingar á sameiginlegum vettvangsgrunnlínum eða eftirlitsskyldum greiðsluflæðum fara til breytingastýringarstjórnar. Stöðubókhald er myndað sjálfvirkt úr útgáfustýringu, afurðasafni og leiðslu, svo endurskoðendur spyrja lifandi skrá í stað þess að biðja um endurgerð.

**Hið opinbera.** Varnaráætlun fylgir formlegri SCM-áætlun í samræmi við IEEE 828. Stillingaratriði eru skráð og sett grunnlínur á við samningsbundna áfanga, og breytingastýringarstjórn heimilar hverja breytingu á stýrðri grunnlínu og skráir áhrif, ákvörðun og rök. Fallbundnar stillingarúttektir staðfesta að afhent kerfi uppfylli tilgreindar kröfur, og líkamlegar stillingarúttektir staðfesta að afhentar afurðir samsvari skráðri stillingu nákvæmlega. Útgáfur eru endurgeranlegar úr stýrðum inntökum, prófsummaðar og rekjanlegar frá enda til enda, frá samþykktri kröfu gegnum breytingabeiðni til afhentrar smíði, sem er einmitt sönnunarslóðin sem vottun og eftirlit krefjast.

## Viðskiptarök: hvatar, ávöxtun fjárfestingar og heildarkostnaður

SCM er til að stýra áhættu og kostnaði yfir líftíma kerfis. Ávöxtunin kemur frá endurgeranleika og rekjanleika: þú getur endurskapað hvaða útgáfu sem er, rakið galla til breytinganna sem ollu þeim og svarað úttektarspurningum úr skrám í stað fornleifafræði. Það styttir atvikagreiningartíma, dregur úr kostnaði og lengd úttekta og kemur í veg fyrir dýra flokk bilunar þar sem enginn getur sagt hvað er í gangi eða hvernig á að endursmíða það.

Heildareignarkostnaður hallast að sjálfvirkni. Handvirkar stillingarskrár eru ódýrar að byrja og stöðugt dýrar að viðhalda, og þær bregðast einmitt þegar þú þarft mest á þeim að halda, við atvik eða úttekt, því þær hafa rekið frá raunveruleikanum. Sjálfvirk auðkenning, bókhald og úttekt kostar meira fyrirfram en breytir stillingarskránni í nánast ókeypis aukaafurð afhendingarleiðslunnar. Til að færa rök við forystu skaltu ramma SCM sem stýringuna sem gerir útgáfur endurgeranlegar og breytingar úttektarhæfar og vegðu hana gegn kostnaði óendurgeranlegra útgáfa, langdreginna úttekta og regluvöruáhættu óstýrðrar breytingar.

## Andmynstur og gildrur

- **Stilling með ættbálkaþekkingu:** raunverulegt innihald útgáfu lifir aðeins í höfði verkfræðings, ekki í neinni skrá.
- **Breytanlegar grunnlínur:** „útgáfunni“ er breytt á staðnum, svo ekki er lengur hægt að endurskapa hana né treysta henni sem viðmiðun.
- **Óstýrð stillingargögn:** kóði er útgáfustýrður en stillingin sem breytir hegðun hans er breytt ad hoc í framleiðslu.
- **Breytingastýringarleikhús:** stjórn sem stimplar allt og bætir við töf án þess að bæta við raunverulegri skoðun.
- **Handvirkt stöðubókhald:** töflureiknir útgáfa sem hljóðlega víkur frá því sem er raunverulega uppsett.
- **Óendurgeranlegar smíðar:** útgáfur sem ekki er hægt að endursmíða úr stýrðum inntökum, svo úttektir og endursmíðar verða ágiskanir.
- **Órekjanlegar útgáfur:** engin kortlagning frá uppsettri afurð aftur til frumkóðaendurskoðunar, breytingabeiðni og samþykkis.

## Þroskalíkan

- **Stig 1 (Upphaf):** SCM er ad hoc og viðbragðsdrifið. Aðeins frumkóði er stýrður, útgáfur eru handsamsettar, engar grunnlínur eru til, engin áreiðanleg skrá yfir hvað er uppsett og engin leið til að endurskapa liðna smíði.
- **Stig 2 (Þróun):** Grunnvinnubrögð eru til en ólík milli teyma. Sum kerfi skilgreina stillingaratriði og breytingaferli og útgáfustýra útgáfur sínar, grunnlínur eru til hér og þar, en skrár eru að hluta handvirkar og nákvæmni stjórnar er ósamræmd yfir skipulagsheildina.
- **Stig 3 (Stöðlun):** Vinnubrögð eru skjalfest og framfylgt um alla skipulagsheildina. Sameiginlegt stillingaratriðaflokkunarkerfi, óbreytanlegar grunnlínur, stigskipt breytingastýring og stöðubókhald eru til staðar og að mestu sjálfvirk. Útgáfur eru endurgeranlegar og rekjanlegar og úttektir eru studdar af verkfærum en ekki minni.
- **Stig 4 (Stjórnun):** SCM er mælt og stýrt með gögnum. Endurgeranleikahlutfall, rekjanleikaþekja frá kröfu til uppsettrar afurðar, breytingatími gegnum hvert stjórnstig, stillingarrekstilvik og úttektarniðurstöður eru raktar gegn grunnlínum og markmiðum. Frávik kalla fram leiðréttingu og sérhver ákvörðun um áfram eða stopp byggir á þessum sönnunargögnum frekar en fullyrðingu.
- **Stig 5 (Samhæfing):** SCM er stöðugt bætt og samþætt um skipulagsheildina. Fullkomlega sjálfvirkt og stöðugt sannreynt með endurgeranlegum smíðum, SBOM, herkomuvottunum og lifandi stöðubókhaldi er ferlið ofið inn í afhendingu, öryggi og úttekt og það aðlagast eftir því sem áhætta og afhendingarniðurstöður breytast, leggur niður og endurafmarkar stýringar á grundvelli sönnunargagna.

## Hugmyndir til umræðu

- Geturðu endurskapað síðustu útgáfu þína nákvæmlega úr stýrðum inntökum í dag og hve langan tíma myndi það taka?
- Hvaða stillingaratriði ákvarða hegðun en eru ekki í raun undir stjórn, sérstaklega stillingargögn og innviðir?
- Er breytingastjórn þín stigskipt eftir áhættu, eða bætir hún við einsleitri yfirbyggingu eða einsleitri slökun alls staðar?
- Hvar býr stillingarskrá þín og hve langt hefur hún rekið frá því sem er raunverulega uppsett?
- Hvaða sönnunargögn gætirðu framleitt í úttekt á morgun og hve mikið af þeim væri endurgerð frekar en skrá?
- Hvernig breyta endurgeranlegar smíðar, SBOM og herkoma því sem úttektir þínar geta sannreynt sjálfvirkt?

## Helstu atriði

- SCM stýrir allri stillingunni (kóða, ósjálfstæði, innviðum og stillingargögnum), ekki bara frumkóða.
- Grunnlínur eru óbreytanlegir viðmiðunarpunktar. Breyting er heimiluð og skráð gegn þeim, ekki komið í veg fyrir hana.
- Stöðubókhald verður að leyfa þér að svara, hvenær sem er, hvað útgáfa inniheldur og hvernig hún komst þangað.
- Úttektir sannreyna að það sem var smíðað og afhent samsvari skráðri stillingu og samþykktum kröfum.
- Stigskiptu stjórn eftir áhættu og sjálfvirknivæddu auðkenningu, bókhald og úttekt svo skráin sé aukaafurð afhendingar.

## Heimildir og frekari lestur

- IEEE Computer Society, *SWEBOK Guide (Guide to the Software Engineering Body of Knowledge)*, Software Configuration Management knowledge area
- IEEE Std 828, *Standard for Configuration Management in Systems and Software Engineering*
- ISO/IEC/IEEE 12207, *Systems and software engineering: Software life cycle processes* (configuration management process)
- Jez Humble and David Farley, *Continuous Delivery*
- Bob Aiello and Leslie Sachs, *Configuration Management Best Practices: Practical Methods that Work in the Real World*
- NIST guidance on software supply chain security, software bills of materials (SBOM), and artifact provenance
- CNCF and open standards for build provenance and attestation (as reference frameworks)
