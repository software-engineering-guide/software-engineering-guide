# 7.7 Gagnalíkön og merkingarlagið

## Yfirlit og tilgangur

[Gagnalíkan](https://en.wikipedia.org/wiki/Data_model) er ákvörðun um hvað gögn þín þýða, tekin áður en þú ákveður hvar gögnin búa. Það nefnir hlutina sem viðskipti þín láta sig varða, eiginleikana sem lýsa þeim og tengslin þar á milli. Geymsla, vísitölur, skráarsnið og fyrirspurnarvélar koma allt síðar. Þessi röðun skiptir máli því merking gagna þinna lifir lengur en hver tækni sem þú notar til að geyma þau. Vöruhús eru endurnýjuð, töflusnið breytast og fyrirspurnarvélar koma og fara, en „viðskiptavinur“, „pöntun“ og „virkur notandi“ verða að merkja það sama yfir þau öll, árum saman.

Fyrir lítið teymi er líkanagerð oft óbein. Einn verkfræðingur heldur öllu skemanu í höfðinu og sameiginlegur skilningur á „tekjum“ lifir því aðeins þrír eru til að vera ósammála. Í stærð stórra forritarastofnana, fyrirtækja og opinberra stofnana hrynur sú óformlegheit nákvæmlega á þann hátt sem lýst er í kafla 7.1 (gagnastefna og gagnastjórnun). Tugir teyma smíða hundruð taflna, hvert með sína hugmynd um hvað „lota“ er eða hvenær notandi telst „virkur“. Tvö mælaborð sýna tvær ólíkar tölur fyrir sömu vikuna og stjórnendafundur breytist í rifrildi um hvers fyrirspurn er rétt í stað þess hvað á að gera næst. Slæm líkanagerð tilkynnir sig ekki. Hún birtist mánuðum síðar sem sáttarvinna, misheppnaðar úttektir og ákvarðanir teknar á tölum sem enginn getur varið.

Þessi kafli fjallar um að vinna það verk af ásetningi. Hann nær yfir hugtaka-, rökræn og efnisleg líkön, einingar-tengslalíkanagerð, hvenær á að normalforma og hvenær að afstaðla, hvernig líkanagerð er ólík fyrir færslu- og greiningarvinnuálag, víddarlíkanagerð með staðreyndum og víddum og merkingarlagið sem geymir einu stýrðu skilgreiningu hvers viðskiptamælikvarða. Ávinningurinn er ekki glæsileiki sjálfs síns vegna. Hann er að „virkur notandi“ og „tekjur“ merki eitt alls staðar, svo teymi þín geti treyst tölunum og hreyft sig hraðar fyrir vikið.

*Sjá einnig:* kafla 3.4 (gagnaarkitektúr og geymsla), kafla 7.3 (greining og viðskiptagreind) og kafla 11.5 (lykilárangursmælikvarðar).

## Meginreglur

- Ákveddu hvað gögn þýða áður en þú ákveður hvar þau búa.
- Líkanaðu á þremur stigum: hugtaka (viðskipti), rökrænu (uppbygging), efnislegu (útfærsla).
- Normalformaðu til að vernda réttleika í færslukerfum. Afstaðlaðu af ásetningi fyrir greiningarhraða.
- Láttu líkanið passa vinnuálaginu: færslur og greining hafa andstæðar þarfir.
- Sérhver viðskiptamælikvarði hefur nákvæmlega eina stýrða skilgreiningu og hún býr í merkingarlaginu.
- Samræmdar víddir leyfa sjálfstæðum teymum að tengja og bera saman gögn örugglega.
- Kornastærð er hönnunarákvörðun sem þú tekur af ásetningi, ekki slys í fyrirspurn.
- Líkön eru lifandi eignir: nefndu þau vel, skjalfestu þau og haltu þeim þróanlegum.

## Ráðleggingar

### Líkanaðu á þremur stigum, í röð

Vinndu frá merkingu og út á við. Byrjaðu á hugtakalíkani: hlutunum sem viðskipti þín láta sig varða og hvernig þeir tengjast, skrifað á einföldu máli sem sérfræðingur á sviðinu getur athugað. „Viðskiptavinur leggur inn margar pantanir. Pöntun inniheldur margar pöntunarlínur. Hver pöntunarlína vísar í eina vöru.“ Engir lyklar, engar tegundir, engar töflur enn. Smíðaðu síðan rökrænt líkan sem bætir við uppbyggingu: eiginleikum, frum- og aðkomulyklum, fjöldatengslum og skorðum, enn óháð tilteknum gagnagrunni. [Einingar-tengslalíkanagerð](https://en.wikipedia.org/wiki/Entity%E2%80%93relationship_model) er staðlaða táknmálið hér og einingar-tengslarit er gripurinn sem þú rýnir með bæði verkfræðingum og viðskiptahagsmunaaðilum. Aðeins þá skaltu framleiða efnislega líkanið: raunverulegar töflur, dálka, gagnagerðir, vísitölur, skiptingar og geymsluskipulag fyrir valda vél. Að stökkva beint í efnislega hönnun eru algengustu líkanamistökin, því það bakar tæknival dagsins inn í ákvarðanir sem ættu að endast lengur.

### Normalform færslukerfi, afstaðlaðu greiningarkerfi af ásetningi

Fyrir kerfi sem skrá færslur skaltu kjósa [normalform gagnagrunns](https://en.wikipedia.org/wiki/Database_normalization). Normalform fjarlægja tvítekningu svo hver staðreynd sé geymd einu sinni, sem kemur í veg fyrir uppfærslufrávik og heldur skrifum réttum þegar margir notendur breyta gögnum samtímis. Þetta er rétta sjálfgefið fyrir [netfærsluvinnslu](https://en.wikipedia.org/wiki/Online_transaction_processing) (OLTP), þar sem réttleiki undir samtímaskrifum skiptir meira máli en hraði einnar greiningarfyrirspurnar. Greiningarkerfi hafa andstæðar áherslur. Þau eru lesþung, þau skanna og taka saman gríðarleg svið og að tengja tugi normalformaðra taflna við fyrirspurn er hægt og erfitt að rökræða um. Þar afstaðlarðu af ásetningi, fellir tengda eiginleika saman svo fyrirspurnir séu einfaldari og hraðari. Aginn er að afstaðla yfirvegað, með skjalfestri ástæðu, frekar en að láta tvítekningu læðast inn af slysni. Kafli 3.4 (gagnaarkitektúr og geymsla) fjallar um vélarnar sem láta hvort mynstur skila árangri.

### Notaðu víddarlíkanagerð fyrir greiningu

Fyrir greiningarvinnuálag skaltu taka upp [víddarlíkanagerð](https://en.wikipedia.org/wiki/Dimensional_modeling), nálgunina sem Ralph Kimball gerði vinsæla. Þú skiptir heiminum í staðreyndir og víddir. Staðreyndatafla geymir mælingar viðskiptaferlis: upphæð sölu, lengd símtals, magn sent. Víddartöflur geyma lýsandi samhengið sem þú síar og flokkar eftir: viðskiptavininn, vöruna, verslunina, dagsetninguna. Raðaðu einni staðreyndatöflu umkringdri víddum sínum og þú ert með [stjörnuskema](https://en.wikipedia.org/wiki/Star_schema), sem er auðvelt fyrir greinendur að skilja og hratt fyrir vélar að spyrjast fyrir um. Normalformaðu þær víddir í undirtöflur og þú færð snjókornaskema, sem sparar einhverja geymslu á kostnað fleiri tenginga og meiri flækju. Kjóstu stjörnuna nema þú hafir áþreifanlega ástæðu. Fyrir mjög stór, mjög regluverkuð umhverfi þar sem úttektarhæfni og uppsprettuupprakning ráða líkanar gagnahvelfingaraðferð miðstöðvar, tengla og gervihnetti til að fanga sögu og ætterni ákaft, á kostnað fleiri taflna og brattari lærdómsferils. Flest teymi ættu að byrja á Kimball-stjörnum og seilast í gagnahvelfingu aðeins þegar úttektarkröfur réttlæta það.

### Festu kornastærðina og meðhöndlaðu breytilegar víddir skýrt

Áður en þú bætir við einum dálki í staðreyndatöflu skaltu segja kornastærð hennar: nákvæmlega hvað ein lína stendur fyrir. „Ein lína á pöntunarlínu.“ „Ein lína á notanda á dag.“ Kornastærð er grunnur réttar líkans, því hver mælikvarði og hver vídd annaðhvort passar þeirri kornastærð eða á ekki heima í töflunni. Að blanda kornastærðum er hvernig þú færð tvítaldar tekjur. Ákveddu síðan hvernig víddir breytast með tímanum. Viðskiptavinur flytur í nýja borg. Skrifarðu yfir gamla gildið, heldurðu fullri sögu eða rekurðu aðeins núverandi og fyrra gildi? Þetta eru stöðluðu mynstrin fyrir [hægt breytilegar víddir](https://en.wikipedia.org/wiki/Slowly_changing_dimension) og að velja rangt þýðir að söguskýrslur þínar endurskrifa hljóðlega fortíðina. Ákveddu kornastærðina og breytingaaðferðina fyrirfram, skrifaðu þær í skjölun líkansins og haltu línunni í rýni.

### Smíðaðu eitt merkingarlag sem einu skilgreiningu hvers mælikvarða

Þetta er ráðleggingin sem borgar fyrir allan kaflann. [Merkingarlag](https://en.wikipedia.org/wiki/Semantic_layer) situr milli efnislegu taflnanna þinna og hvers verkfæris sem notar þær og geymir einu stýrðu skilgreiningu hvers viðskiptamælikvarða. „Virkur notandi“ er skilgreindur einu sinni, sem kóði, með nákvæmri rökfræði sinni: hvaða atburðir teljast, yfir hvaða glugga, með hvaða innri reikninga útilokaða. „Tekjur“ eru skilgreindar einu sinni, þar með talið hvernig endurgreiðslur, afslættir og gjaldmiðlaumbreyting eru meðhöndluð. Hvert mælaborð, minnisbók, skýrsla og öfug-ETL verk les þá skilgreiningu í stað þess að endurútfæra hana í sérsmíðaðri fyrirspurn. Þegar skilgreiningin breytist breytist hún á einum stað og hver notandi uppfærist saman. Þetta er búnaðurinn sem gerir stýrðar mælikvarðaskilgreiningar raunverulegar frekar en metnaðarfullar og það er bein útfærsla á því sem kafli 11.5 (lykilárangursmælikvarðar) biður um. Líttu á mælikvarðaskilgreiningar sem útgáfustýrðan kóða með eigendum, rýni og prófum, nákvæmlega eins og kafli 7.1 biður þig að líta á gögn sem vöru.

### Komdu á venjum, nafngiftum og skjölun

Samræmi er eiginleiki. Taktu upp nafngiftavenjur og framfylgdu þeim: venju fyrir töfluheiti, venju fyrir lykla, staðal fyrir dagsetningardálka, reglu um hvernig þú merkir staðreynd á móti vídd. Ákveddu einu sinni hvort þú notar eintölu- eða fleirtölunöfn eininga og blandaðu þeim aldrei. Skjalfestu hvert líkan þar sem fólkið sem notar það mun leita: merkingu hverrar töflu, kornastærð hverrar staðreyndar, skilgreiningu hvers mælikvarða og eiganda hvers. Góðar nafngiftir og skjölun er það sem leyfir nýjum greinanda að bjarga sér sjálfur í stað þess að trufla teymið og það er það sem leyfir úttektaraðila að rekja tölu úr stjórnarkynningu aftur til uppsprettu án leiðsagnar.

### Haltu líkönum þróanlegum

Líkan þitt mun breytast, svo hannaðu fyrir breytingar. Bættu við dálkum frekar en að endurnýta þá sem fyrir eru. Notaðu staðgenglalykla svo breyting á náttúrulegum lykli í frumkerfi gárist ekki um vöruhúsið þitt. Útgáfustýrðu mælikvarðaskilgreiningum og úreltu þær með tilkynningu í stað þess að breyta þeim hljóðlega undir keyrandi mælaborðum. Haltu umbreytingum í útgáfustýringu, prófuðum og rýndum, svo breyting á því hvað „virkur notandi“ merkir sé sameiningarbeiðni með mismun og samþykkjanda, ekki hljóðlát breyting í viðskiptagreindartóli. Líkan sem þú getur ekki þróað örugglega verður líkan sem fólk fer framhjá og skuggaskilgreiningar eru hvernig ein uppspretta sannleikans deyr.

## Málamiðlanir: kostir og gallar

| Nálgun | Kostir | Gallar | Best passun |
|---|---|---|---|
| Normalformað (3NF) | Rétt skrif, engin tvítekning, sveigjanlegt | Hægar greiningartengingar, flóknar fyrirspurnir | OLTP og rekstrarkerfi |
| Stjörnuskema (Kimball) | Hratt, innsæi, greinendavænt | Einhver tvítekning, ETL að viðhalda | Mest greining og viðskiptagreind |
| Snjókornaskema | Minni geymsla, hreinni víddir | Fleiri tengingar, meiri flækja | Stórar, þétt stýrðar víddir |
| Gagnahvelfing | Full saga, úttektarhæf, lipur hleðsla | Margar töflur, brattur lærdómsferill | Mjög regluverkuð, úttektarþung |
| Merkingarlag yfir líkönum | Ein skilgreining alls staðar, verkfærahlutlaust | Smíði fyrirfram, þarfnast eignarhalds | Fjölteymis-, fjölverkfæraskipulagsheildir |

Kjarnaspennan er hraði einnar fyrirspurnar gegn réttleika og sveigjanleika yfir alla landareignina. Normalform vernda réttleika og borga fyrir það í fyrirspurnarflækju. Víddarlíkön kaupa fyrirspurnarhraða og skýrleika og borga fyrir það með ETL og einhverri stýrðri tvítekningu. Enginn algildur sigurvegari er til, sem er ástæða þess að þú lætur líkanið passa vinnuálaginu frekar en að velja uppáhald. Merkingarlagið leysir seinni spennuna, milli margra teyma og margra verkfæra, með því að gera mælikvarðaskilgreininguna óháða hverju þeirra. Mistökin eru að meðhöndla þetta sem hugmyndafræðilegar fylkingar. Heilbrigð skipulagsheild rekur normalformuð OLTP-kerfi, víddarlíkön fyrir greiningu nærð úr þeim og eitt merkingarlag ofan á, hvert að gera verkið sem það er gott í.

## Spurningar til að ræða með teyminu

1. **Þegar tvö mælaborð sýna ólíkar tölur fyrir sama mælikvarða, hvers skilgreining vinnur og hvar býr sú skilgreining efnislega?** Þessi spurning afhjúpar hvort þið hafið í raun eina uppsprettu sannleikans eða trúið bara að þið hafið. Í flestum stórum teymum er heiðarlega svarið að „virkur notandi“ sé endurskilgreindur í tugi ólíkra fyrirspurna og sigurvegarinn sé sá sem rífst hæst á fundinum. Komdu með raunveruleg sönnunargögn: veldu einn mælikvarða, finndu hvern stað þar sem hann er reiknaður og berðu rökfræðina saman línu fyrir línu. Þú munt nær örugglega finna hljóðlátan ágreining um glugga, útilokanir og jaðartilvik. Svarið ætti að knýja ákvörðun um að smíða merkingarlag þar sem hver mælikvarði er skilgreindur einu sinni, sem rýndur kóði, svo spurningin hætti að snúast um fólk og fari að snúast um útgáfustýrðan grip. Þar til sú skilgreining hefur eitt efnislegt heimili er hver sátt tímabundin.

2. **Hver er kornastærð mikilvægustu staðreyndatöflu ykkar og geta allir í herberginu sagt hana á sama hátt?** Kornastærð er hljóðláti grunnurinn sem flest líkanamistök rekjast til. Ef helmingur teymisins segir „ein lína á pöntun“ og hinn helmingurinn „ein lína á pöntunarlínu“ hafið þið tvítalningargalla sem bíður þess að birtast í tekjuskýrslu. Komdu með raunverulegu töfluna og biddu hvern að lýsa einni línu í einni setningu. Ágreiningur hér er ekki samskiptavandamál til að slétta yfir. Hann er hönnunargalli til að laga áður en fleiri mælikvarðar hlaðast ofan á. Svarið ætti að vera skrifað í skjölun líkansins og framfylgt í rýni, því þegar greinendur byggja fyrirspurnir á tvíræðri kornastærð dreifist tvíræðnin hraðar en þú getur leiðrétt.

3. **Hvernig mun þetta líkan taka við breytingum og hvað verður um skýrslur síðasta árs þegar skilgreining breytist?** Sérhvert líkan stendur frammi fyrir breytilegum frumkerfum, breytilegum viðskiptareglum og breytilegum mælikvarðaskilgreiningum, svo raunverulega spurningin er hvort breyting sé stýrð sameiningarbeiðni eða hljóðlát breyting sem endurskrifar sögu. Komdu með nýlegt dæmi: mælikvarða sem skilgreining breyttist á eða frumkerfislykil sem var endurnefndur og raktu hvað varð um núverandi mælaborð. Ef hægt breytileg vídd var meðhöndluð með yfirskrift gætu söguskýrslur þínar hljóðlega hafa breytt fyrri gildum sínum, sem er alvarlegt vandamál fyrir alla sem gera þróunargreiningu eða regluverkaða skýrslugerð. Svarið ætti að ýta þér að staðgenglalyklum, útgáfustýrðum mælikvarðaskilgreiningum, skýrum breytingaaðferðum og umbreytingum í útgáfustýringu með rýni. Líkan sem enginn getur breytt örugglega verður líkan sem fólk yfirgefur.

4. **Hvaða víddir verða að merkja það sama yfir hvert teymi og hver ber ábyrgð á að eiga hverja?** Samræmdar víddir eru það sem leyfir markaðssetningu, fjármálum og rekstri að tengja gögn sín og fá sambærileg svör, en aðeins þegar „viðskiptavinur“, „vara“, „svæði“ og „dagsetning“ bera eina samþykkta skilgreiningu í stað einkaafrits á teymi. Togið á móti er sjálfræði: hvert teymi vill líkana eigin heim á eigin hraða og að þvinga sameiginlega vídd hægir á þeim til skamms tíma en borgar sig yfir landareignina. Komdu með tvær eða þrjár víddir sem birtast í flestum þverteymisskýrslum, skráðu hverja útgáfu af hverri sem er til í dag og sjáðu hve langt lyklar þeirra og eiginleikar víkja í raun. Nefndu eiganda fyrir hverja samræmda vídd, því sameiginleg vídd án eiganda rekur aftur í einkaafrit innan ársfjórðungs. Í fyrirtækja- og opinberu umhverfi, þar sem tala frá einni deild er borin saman við aðra opinberlega, er ósamræmd vídd munurinn á heiðarlegum samanburði og óviljandi ósannindum, svo ákveddu snemma hvaða víddir eru stýrðar miðlægt og hverjar haldast staðbundnar.

5. **Hvar liggja mörkin milli normalformaðra færslukerfa ykkar og afstaðlaðra greiningarlíkana og er hver afstöðlun yfirveguð ákvörðun?** Að láta líkanið passa vinnuálaginu er kjarnaagi, samt eru mörkin nákvæmlega þar sem allt óskýrist: greinandi afstaðlar vöruhústöflu fyrir hraða, verkfræðingur normalformar skýrslutöflu af vana og enginn skrifaði niður hvorum megin hvert val á heima. Spennan er hraði einnar fyrirspurnar gegn réttleika og sveigjanleika yfir allt, og sanngjarnt fólk lendir ólíkt eftir því hvort það á skrif eða lestur. Komdu með hægustu greiningarfyrirspurn þína og mest keppta færslutöflu og spyrðu fyrir hvern tvítekinn dálk hvort tvítekningin hafi verið valin með skjalfestri ástæðu eða læðst inn af slysni. Markmiðið er skrifleg regla um hvenær afstöðlun er leyfð og hver samþykkir, ekki hreinleikakeppni. Fyrir stórar eða regluverkaðar skipulagsheildir ákveða þessi mörk líka hvar persónugögn eru tvítekin, svo óskjalfest afstöðlun er bæði afkastaspurning og gagnastjórnunarútsetning sem einhver verður einhvern tímann að útskýra fyrir úttektaraðila.

6. **Ættuð þið að smíða eða kaupa merkingarlagið og hver ber ábyrgð á að halda hverri mælikvarðaskilgreiningu núgildandi þegar það er til?** Merkingarlag skilar einni uppsprettu sannleikans aðeins þegar það er í eigu og viðhaldið, svo val á verkfæri skiptir minna máli en svarið við því hver rýnir breytingu á því hvað „tekjur“ merkja og hver er ábyrgur þegar skilgreining úreldist. Sjónarmiðin sem togast á eru raunveruleg: smíði gefur þér stjórn og passar staflann þinn en bætir við verkfræðibyrði, á meðan að kaupa mælikvarðatól er hraðara en felur í sér hættu á bindingu og skilgreiningarmáli sem þú stýrir ekki til fulls. Komdu með fáu mikilvægustu mælikvarðana þína, verkfærin sem nota þá í dag og heiðarlegt mat á því hvort nokkur eigi þessar skilgreiningar eða þær bara séu til. Ákveddu fyrirfram hvort skilgreiningar búi sem útgáfustýrður kóði með nefndum eigendum og prófum, því merkingarlag sem enginn viðheldur rotnar í sömu dreifðu skilgreiningarnar og það átti að koma í staðinn fyrir. Í fyrirtækja- og opinberri skýrslugerð, þar sem mælikvarði á opinberu mælaborði verður að vera rekjanlegur til skjalfestrar, rýndrar skilgreiningar, er það eignarhald og getan til að sanna ætterni tölu sem breytir merkingarlaginu úr þægindum í úttektarhæfa stýringu.

## Sjónarhorn eftir geirum

**Sprotafyrirtæki.** Líkanagerð getur beðið, en skilgreiningar ekki. Með tvo verkfræðinga og ekkert svigrúm til að smíða vöruhús skaltu setja eitt lítið merkingarlag í umbreytingartólið þitt og skilgreina tvo eða þrjá mælikvarða sem stjórn þín horfir í raun á, „virkur notandi“ og „tekjur“, einu sinni sem prófaðan kóða. Slepptu gagnahvelfingu og íburðarmiklum víddarskemum. Þunn stjarna og fáeinar stýrðar skilgreiningar kaupa þér samræmdar tölur án þess að hægja á afhendingu. Ávinningurinn er að undirbúningur stjórnarfunda hættir að vera rifrildi um hvers fyrirspurn sé rétt.

**Lítið fyrirtæki.** Þú hefur engan gagnalíkanasmið og enga fjárveitingu fyrir mælikvarðavettvang, svo hallaðu þér að skilgreiningunum sem eru innbyggðar í verkfærin sem þú rekur nú þegar og skrifaðu fáu mikilvægu niður í eitt sameiginlegt skjal sem allir lesa. Kjóstu að kaupa greiningu innbyggða í núverandi hugbúnað fram yfir að setja upp vöruhús sem þú getur ekki mannað. Þar sem þú líkanar skaltu halda því einföldu og nefna hluti samræmt, því sá sem viðheldur því á næsta ári gæti verið sá sem man ekki hvers vegna „viðskiptavinur“ merkti tvennt. Samræmi er ódýrara en sátt.

**Stórfyrirtæki.** Vandinn er mörg teymi og mörg verkfæri sem reka í einkaskilgreiningar, svo fjárfestu í samræmdum víddum, einu stýrðu merkingarlagi og mælikvarðaskilgreiningum haldið sem útgáfustýrðum kóða með eigendum og rýni. Staðlaðu nafngiftir, kornastærðaryfirlýsingar og hægt-breytilegra-víddar aðferðir yfir landareignina svo tala í einu verkfæri passi við sömu tölu í öðru. Líttu á merkingarlagið sem vöru með vegvísi og eigandateymi og mældu hve mikinn sáttartíma það fjarlægir. Ávöxtunin eru traustar tölur yfir reksturinn og úttektir sem rekjast hreint úr stjórnarkynningu aftur til uppsprettu.

**Hið opinbera.** Gagnsæi og þverstofnunarsamanburðarhæfni móta verkið: kanónísk viðmiðunargögn fyrir landafræði og lýðfræði, stýrðar skilgreiningar kjarnavísitalna og birt aðferðafræði með útgáfustýrðum útgáfum svo almenningur geti rakið hverja tölu aftur til skjalfestrar skilgreiningar. Innkaupareglur geta krafist þess að líkön þín og skilgreiningar haldist flytjanleg og seljandahlutlaus, svo forðastu merkingarlag læst við eitt séreignarverkfæri. Haltu einstökum stofnunum frjálsum að líkana rekstrargögn sín á meðan þær samræmast sameiginlegum víddum fyrir allt sem skýrt er frá á landsvísu. Útgefin vísitala sem ekki er hægt að rekja til útgáfustýrðrar skilgreiningar er ábyrgðarbrestur jafnt og gagnabrestur.

## Dæmi

**Sprotafyrirtæki.** Fyrirtæki í A-lotu hafði þrjár skilgreiningar á „virkum notanda“ búandi á þremur stöðum: vörugreiningartólinu, fjármálatöflureikninum og fjárfestakynningunni. Tölurnar pössuðu aldrei og hver undirbúningur stjórnarfundar breyttist í óðagot. Tveir verkfræðingar kynntu lítið merkingarlag í umbreytingartólinu sínu, skilgreindu „virkur notandi“ og „mánaðarlegar endurteknar tekjur“ einu sinni sem prófaðan kóða, með nákvæmum gluggum og útilokunum skrifaðar niður. Hvert mælaborð les nú þær skilgreiningar. Rifrildið um undirbúning stjórnarfunda hvarf og innleiðing nýs greinanda fór úr viku af hópþekkingu í að lesa eitt skjalfest líkan. Þetta tengist beint aganum sem lýst er í kafla 7.4 (vörugreining og tilraunir), þar sem stöðug skilgreining á „virkum“ er það sem gerir tilraunaniðurstöður sambærilegar.

**Stórfyrirtæki.** Alþjóðlegur smásali rak fimm viðskiptagreindartól yfir markaðssetningu, fjármál, aðfangakeðju, vöruframboð og verslanir og hvert hafði endurfundið upp „brúttóframlegð“ örlítið ólíkt. Þau smíðuðu eitt merkingarlag ofan á Kimball-stíl vöruhús með samræmdum víddum, svo „vara“, „verslun“ og „dagsetning“ merktu það sama yfir hverja staðreyndatöflu og hvert verkfæri. Hver mælikvarði var skilgreindur einu sinni og notaður alls staðar. Sáttarfundir sem áður átu daga á ársfjórðung hurfu að mestu og þegar fjármál breyttu því hvernig skil höfðu áhrif á framlegð barst breytingin í öll fimm verkfærin í einu. Samræmdu víddirnar voru það sem leyfði sjálfstæðum teymum að tengja gögn sín af öryggi frekar en tortryggni.

**Hið opinbera.** Landsstjórn þurfti sambærilega skýrslugerð yfir heilbrigðis-, vinnumarkaðs- og menntastofnanir, hverja sem hafði sögulega skilgreint „heimili“, „svæði“ og „atvinnu“ á sinn hátt. Þverstofnunaraðili kom á sameiginlegum viðmiðunargögnum og stöðluðum skilgreiningum: kanónískum víddartöflum fyrir landafræði og lýðfræði og stýrðum skilgreiningum kjarnavísitalna, birtum með aðferðafræði og útgáfustýrðum útgáfum. Einstakar stofnanir líkana eigin rekstrargögn en samræmast sameiginlegum víddum og skilgreiningum fyrir allt sem skýrt er frá á landsvísu. Niðurstaðan er að tölu frá einni stofnun má bera heiðarlega saman við aðra og almenningur getur rakið hverja útgefna vísitölu til skjalfestrar skilgreiningar, sem styður gagnsæisskyldurnar sem fjallað er um í kafla 7.1.

## Viðskiptarök: hvatar, ávöxtun fjárfestingar og heildarkostnaður

Ávöxtun góðrar líkanagerðar og merkingarlags er mestmegnis endurheimtur tími og forðuð villa. Í mörgum skipulagsheildum eyða greinendur meirihluta tíma síns í að finna gögn, sætta andstæðar tölur og endurbyggja skilgreiningar sem aðrir hafa þegar skrifað. Ein stýrð skilgreining hvers mælikvarða breytir þeirri endurteknu vinnu í einskiptisfjárfestingu. Hún fjarlægir líka heilan flokk dýrra bilana: röngu töluna í stjórnarkynningu, ranglega skýrðu töluna sem ræsir úttektarniðurstöðu, ársfjórðungslangt sáttarverkefni sem er til aðeins því tvö teymi skilgreindu „tekjur“ ólíkt. Þegar skilgreiningin býr á einum rýndum stað hætta þessar bilanir að mestu að gerast.

Kostnaðurinn er raunverulegur og vert að nefna. Þú fjárfestir fyrirfram í hugtaka- og rökrænni líkanagerð, í að smíða og fylla merkingarlagið og í viðvarandi eignarhaldi sem heldur skilgreiningum núgildandi. Heildareignarkostnaður (TCO) felur í sér verkfærin, líkana- og greiningarverkfræðitímann og stjórnunina til að halda líkaninu frá því að reka. Vegðu það gegn kostnaði þess að gera það ekki, sem er stærri en falinn: hann birtist sem tvítekin leiðsla, greinendur sem mennskar sáttarvélar og stjórnendur sem taka örugga ákvarðanir á tölum sem enginn getur varið. Færðu rök við forystu á þeirra máli. Ein traust skilgreining hvers mælikvarða er það sem leyfir þeim að bera saman yfir reksturinn, treysta mælaborðunum og svara eftirlitsaðilum án neyðaræfingar. Byrjaðu þar sem sáttarsársaukinn er mestur, skilgreindu þá fáu mælikvarða einu sinni og láttu endurheimta tímann fjármagna restina.

## Andmynstur og gildrur

- Að stökkva beint í efnislegar töflur, sem bakar tækni dagsins inn í ákvarðanir sem ættu að endast lengur.
- Að skilgreina sama mælikvarða sjálfstætt í hverju mælaborði, svo engar tvær tölur passa.
- Að láta kornastærð ósagða og uppgötva síðan tvítalda mælikvarða í tekjuskýrslu.
- Að afstaðla greiningartöflur af slysni í stað skjalfestrar ákvörðunar.
- Að normalforma greiningarvöruhús þar til hver fyrirspurn er tólf-töflu tenging sem enginn skilur.
- Að meðhöndla hægt breytilegar víddir með yfirskrift, svo söguskýrslur endurskrifa hljóðlega fortíðina.
- Að nota náttúrulega lykla alls staðar, svo breyting á frumkerfislykli gárist gegnum allt vöruhúsið.
- Að smíða merkingarlag án eiganda, svo skilgreiningar reka og traust rofnar.
- Að líta á líkanið sem búið við opnun í stað lifandi eignar sem verður að haldast þróanleg.

## Þroskalíkan

- **Stig 1, Upphaf:** Líkanagerð er óbein og viðbragðsdrifin. Töflur eru hannaðar efnislegt-fyrst af hverjum sem þarf þær. Mælikvarðar eru endurskilgreindir í hverri skýrslu og tölur stangast reglulega á. Kornastærð er óskjalfest og enginn á skilgreiningarnar.
- **Stig 2, Þróun:** Sumar greiningartöflur fylgja víddarmynstri og fáeinir lykilmælikvarðar hafa skrifaðar skilgreiningar, en þær búa á wiki og er ekki framfylgt. Nafngiftavenjur eru til á pappír. Vinnubrögð eru ólík eftir teymum og sátt er enn tíð og handvirk.
- **Stig 3, Stöðlun:** Hugtaka-, rökræn og efnisleg líkön eru aðgreind og rýnd. Merkingarlag skilgreinir kjarnamælikvarða einu sinni, sem útgáfustýrðan kóða með eigendum. Samræmdar víddir leyfa teymum að tengja örugglega. Kornastærð og hægt-breytilegra-víddar aðferðir eru skjalfestar og framfylgdar í rýni um skipulagsheildina.
- **Stig 4, Stjórnun:** Líkanalandareignin er mæld gegn grunnlínum. Þú rekur þekju mælikvarðaskilgreininga (hlutfall skýrðra mælikvarða sem merkingarlagið þjónar), fjölda tvítekinna eða skuggaskilgreininga enn í notkun, sáttartíma á ársfjórðung og hlutfall kornastærðar- og ætternigalla sem finnast í rýni á móti í framleiðslu. Skilgreiningabreytingar flæða gegnum rýndar sameiningarbeiðnir með prófum og ferskleiki, prófaárangur og rek eru vöktuð á mælaborðum. Þegar mælikvarði víkur eða vídd hættir að samræmast kemur mælingin því upp á yfirborðið áður en stjórnarfundur gerir það.
- **Stig 5, Samhæfing:** Sérhver mikilvægur mælikvarði hefur eina stýrða skilgreiningu notaða af öllum verkfærum og teymum og merkingarlagið er samþætt greiningu, tilraunum og regluverkaðri skýrslugerð. Líkön eru þróanleg í hönnun og stöðugt fínpússuð. Skilgreiningar eru treystar um skipulagsheildina. Sáttarvinna hefur að mestu horfið. Skipulagsheildin úreldir, endurmarkar og samræmir nýjar víddir reglulega eftir því sem reksturinn breytist og endurjafnar líkanalandareignina sem aðlögunarhæfa eign.

## Hugmyndir til umræðu

1. Veldu þrjá mikilvægustu mælikvarðana þína. Hve margar ólíkar skilgreiningar á hverjum eru til yfir verkfærin þín í dag og hvað þyrfti til að fella þær saman í eina?
2. Hvar hefur ósögð kornastærð valdið raunverulegri skýrsluvillu og hve lengi tók að taka eftir?
3. Hverjar af víddum þínum ættu að vera samræmdar yfir teymi fyrst og hver á þær?
4. Eru mælikvarðaskilgreiningar þínar í útgáfustýringu með rýni, eða breytanlegar hljóðlega innan viðskiptagreindartóls?
5. Hvenær endurskrifaði hægt breytileg vídd síðast sögu þína án þess að nokkur tæki eftir og hvernig myndir þú grípa það næst?
6. Ef þú skiptir um vöruhúsvél á morgun, hve mikið af merkingu líkans þíns lifði af flutninginn?

## Helstu atriði

- Gagnalíkanagerð er að ákveða hvað gögn þýða og sú merking lifir lengur en hver geymslutækni sem þú velur.
- Líkanaðu á þremur stigum í röð: hugtaka, síðan rökrænu, síðan efnislegu.
- Normalformaðu færslukerfi fyrir réttleika. Afstaðlaðu greiningarkerfi yfirvegað fyrir hraða.
- Notaðu víddarlíkanagerð með staðreyndum, víddum og sagðri kornastærð fyrir greiningu.
- Smíðaðu eitt merkingarlag svo hver viðskiptamælikvarði hafi eina stýrða skilgreiningu alls staðar.
- Samræmdar víddir leyfa sjálfstæðum teymum að tengja og bera saman gögn sín af öryggi.
- Nefndu vel, skjalfestu, notaðu staðgenglalykla og útgáfustýrðu skilgreiningum svo líkanið haldist þróanlegt.

## Heimildir og frekari lestur

- Ralph Kimball and Margy Ross, *The Data Warehouse Toolkit: The Definitive Guide to Dimensional Modelling*.
- Bill Inmon, *Building the Data Warehouse*.
- Dan Linstedt and Michael Olschimke, *Building a Scalable Data Warehouse with Data Vault 2.0*.
- Peter Chen, "The Entity-Relationship Model: Toward a Unified View of Data," ACM Transactions on Database Systems.
- E. F. Codd, "A Relational Model of Data for Large Shared Data Banks," Communications of the ACM.
- C. J. Date, *An Introduction to Database Systems*.
- Lars Rönnbäck and colleagues, writings on anchor modelling.
- DAMA International, *DAMA-DMBOK: Data Management Body of Knowledge*.
