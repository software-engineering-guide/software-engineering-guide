# 2.12 Líkön og aðferðir hugbúnaðar

## Yfirlit og tilgangur

Hugbúnaðarlíkan er yfirveguð einföldun kerfis, smíðuð til að svara tiltekinni spurningu. Aðferð er agaður háttur við að framleiða hugbúnað, þar með talin líkönin sem hún notar á leiðinni. Saman mynda þau Software Engineering Body of Knowledge (SWEBOK) þekkingarsvið, því þau eru hugarverkfærin sem þú notar til að rökræða um kerfi áður en þú smíðar það, meðan á smíðinni stendur og eftir hana. UML-flokkarit ([Unified Modelling Language](https://en.wikipedia.org/wiki/Unified_Modeling_Language)), [eininga-tengslarit](https://en.wikipedia.org/wiki/Entity%E2%80%93relationship_model) (ERD), [ástandsvél](https://en.wikipedia.org/wiki/Finite-state_machine), [formleg tilgreining](https://en.wikipedia.org/wiki/Formal_specification) og einnota frumgerð eru öll líkön. [Fossamódel](https://en.wikipedia.org/wiki/Waterfall_model), [frumgerðasmíði](https://en.wikipedia.org/wiki/Software_prototyping), formleg þróun og [lipur aðferðafræði](https://en.wikipedia.org/wiki/Agile_software_development) eru öll aðferðir.

Hvers vegna nenna að búa til líkön? Vegna þess að vinnuminni manna er lítið og hugbúnaðarkerfi eru stór. Enginn getur haldið hundrað þúsund lína kerfi í höfðinu, svo við teiknum myndir og skrifum ágripanir sem sýna eina hlið í einu: gögnin, stýriflæðið, ástöndin, samskiptin. Líkan er aldrei ætlað að vera trútt kóðanum. Það er ætlað að henta ákvörðun. Gott líkan sýnir nákvæmlega það sem þú þarft til að ákveða eitthvað og felur allt annað.

Í stórum teymum eru raunverulegir hagsmunir samhæfing og samskipti. Þegar hundruð verkfræðinga, arkitekta, greinenda og endurskoðenda vinna að einu kerfi eru sameiginleg líkön sameiginlegi grundvöllurinn þar sem þeir semja um hönnun, kröfur og áhættu. Líttu því á mótun sem verkfæri með verk að vinna. Hún borgar sig þegar líkan er ódýrara en mistökin sem það kemur í veg fyrir. Hún verður sóun þegar þú teiknar hana í sjálfri sér, heldur henni löngu eftir að hún er úrelt eða útfærir hana lengra en ákvörðunin sem henni var ætlað að þjóna. Mótun tengist þétt hugbúnaðarkröfum (kafli 2.8), hönnunarreglum hugbúnaðar (kafli 2.2), arkitektúr og táknmálum hans eins og C4 og arc42 (kafli 3.1) og lipru vinnulagi (kafli 10.7).

## Meginreglur

- Sérhvert líkan hefur tilgang. Ef þú getur ekki nefnt ákvörðunina sem líkan upplýsir, teiknaðu það ekki.
- Ágripun er kjarnaathöfn mótunar: taktu með það sem skiptir máli fyrir tilganginn, slepptu hinu.
- Samræmi skiptir máli innan og milli líkana. Misvísandi líkön eru verri en engin.
- Líkön eru fyrst og fremst samskiptaafurðir. Áhorfendur þeirra ákvarða táknmál og smáatriði.
- Kjóstu léttasta líkanið sem svarar spurningunni. Útfærsla hefur burðarkostnað.
- Líkan er aðeins jafn gott og greining þess. Óathugað líkan er óprófuð forsenda.
- Veldu aðferð sem passar óvissu, áhættu og afleiðingum bilunar vandans.

## Ráðleggingar

### Mótaðu með ágripun, tilgangi og samræmi

Byrjaðu hvert líkan á að nefna tilgang þess og áhorfendur. Ágripaðu síðan miskunnarlaust að þeim tilgangi: runurit sem ætlað er að leysa kappakstursástand ætti að sýna tímasetningu og skilaboð, ekki hvern reit. Haltu líkönum þínum samræmdum hvert öðru, svo einingarnar í ERD, flokkarnir í flokkariti og nafnorðin í kröfunum séu öll sammála, og samræmdum raunveruleikanum, sem þýðir að þú uppfærir eða eyðir líkani þegar kerfið heldur áfram. Úrelt líkan sem fólk treystir er hætta. Úrelt líkan sem allir hunsa er sóun sem kostar samt athygli.

### Veldu byggingarleg eða hegðunarleg líkön eftir spurningunni

Notaðu byggingarleg líkön til að sýna úr hverju kerfi er gert og hvernig hlutarnir tengjast: flokkarit, íhlutarit og eininga-tengslarit fyrir gagnauppbyggingu. Notaðu hegðunarleg líkön til að sýna hvað kerfi gerir yfir tíma: ástandsvélar fyrir hluti með marktækan lífsferil, runurit fyrir samskipti yfir íhluti og athafnarit fyrir vinnuflæði og viðskiptaferla. Veldu það eina táknmál sem afhjúpar ákvörðunina fyrir framan þig. Flest kerfi þurfa aðeins handfylli ritgerða, teiknaðar sértækt, ekki alla UML-skrána beitta á allt.

### Greindu líkön, teiknaðu þau ekki bara

Líkan vinnur sér inn pláss sitt með greiningu, ekki bara teikningu. Athugaðu ástandsvél fyrir óaðgengileg ástönd, vantandi umskipti og pattstöðu. Athugaðu ERD fyrir normalíseringarvandamál og munaðarlaus tengsl. Gakktu í gegnum runurit gegn kröfunum til að finna vantandi villuleiðir. Rýndu líkön þín með sviðssérfræðingum sem geta komið auga á hvað er rangt. Og þar sem kostnaður bilunar er mikill skaltu ná í verkfærastudda greiningu (líkanaprófara, samræmisprófara, hermun) frekar en að líta á það með augunum.

### Beittu aðferðum byggðum á þumalfingursreglum sem sjálfgefnu

Mestur hugbúnaður er smíðaður með aðferðum byggðum á þumalfingursreglum: reynslubyggðum, endurteknum nálgunum sem nota líkön óformlega og dæma niðurstöður gegn væntingum frekar en sönnunum. Fyrir flest viðskipta- og opinber kerfi er það einmitt rétt: kröfur þróast og galli er venjulega afturkræfur. Þumalfingursaðferðir para sig eðlilega við lipra aðferðafræði (kafli 10.7): mótaðu rétt nóg til að samræma teymið, smíðaðu síðan og lærðu.

### Taktu frá formlegar aðferðir fyrir áhrifamikla kjarna

[Formlegar aðferðir](https://en.wikipedia.org/wiki/Formal_methods) tjá tilgreiningar í stærðfræði og nota sannprófun, hvort sem er sönnun eða tæmandi [líkanaprófun](https://en.wikipedia.org/wiki/Model_checking), til að staðfesta eiginleika. Þær kosta raunverulega færni og tíma og borga sig einmitt þar sem bilun er skelfileg eða óafturkræf: öryggiskritísk stjórnun, dulritunarsamskiptareglur, kjarnar fjármálauppgjörs og þess háttar. Beittu þeim á lítinn mikilvægan kjarna, ekki allt kerfið. Og athugaðu að formleg tilgreining ein og sér, jafnvel án fullrar sönnunar, bætir oft við virði einfaldlega með því að þvinga þig til nákvæmni.

### Notaðu frumgerðir til að losna við óvissu

Þegar kröfur eða framkvæmanleiki eru óljós skaltu smíða frumgerð til að læra, ákveða síðan, af ásetningi, hvort á að þróa hana áfram eða farga henni. Einnota frumgerðir kanna spurningu ódýrt og er síðan eytt. Þróunarfrumgerðir verða varan og verða að vera smíðaðar eftir framleiðslustöðlum. Klassíska bilunin er að láta einnota frumgerð renna í framleiðslu fyrir slysni. Svo nefndu gerð frumgerðarinnar áður en þú smíðar hana.

### Láttu aðferð passa áhættu, ekki tísku

Veldu aðferðir eftir óvissu vandans og afleiðingum bilunar. Mikil óvissa hallast að frumgerðasmíði og lipri endurtekningu. Miklar afleiðingar hallast að formlegri greiningu og nákvæmri sannprófun. Kerfi með hvoru tveggja þarf mikilvægan formlegan kjarna inni í annars lipru umslagi. Hvað sem þú gerir skaltu ekki taka upp aðferð bara af því hún er virðuleg eða af því söluaðili er að selja hana.

## Málamiðlanir: kostir og gallar

| Líkan eða aðferð | Beitt vel | Bilunarháttur |
|---|---|---|
| Byggingarleg líkön (UML, ERD) | Sameiginleg mynd af hlutum og gögnum | Ritasprenging, rek frá kóða |
| Hegðunarleg líkön (ástand, runa, athöfn) | Afhjúpa tímasetningu, ástönd og jaðartilvik | Of ítarleg rit sem enginn les |
| Þumalfingursaðferðir | Hraðar, sveigjanlegar, passa flestum kerfum | Agalausar, faldar forsendur |
| Formlegar aðferðir | Sannanlegir eiginleikar fyrir mikilvæga kjarna | Hár kostnaður, beitt ranglega á allt kerfið |
| Frumgerðasmíði | Ódýrt nám, losar við áhættu snemma | Einnota kóði upphafinn í framleiðslu |
| Lipur aðferðafræði | Aðlagast breytilegum kröfum | Sleppir mótun sem þarf fyrir erfið vandamál |

Endurtekna spennan er milli nákvæmni og hraða. Of lítil mótun sendir faldar forsendur í framleiðslu. Of mikil mótun brennir fyrirhöfn á rit sem aldrei upplýsa ákvörðun og rotna um leið og kóðinn breytist. Enginn fastur skammtur lagar þetta, aðeins hlutfallsregla: fjárfestu í líkani eða aðferð í hlutfalli við óvissuna sem það leysir og kostnað þess að fá ákvörðunina ranga. Greiðsluvél og markaðsvefsíða verðskulda ólíka meðhöndlun.

## Spurningar til að ræða með teyminu

1. **Greinum við líkön okkar, eða teiknum við þau bara og höldum áfram?** Líkan vinnur sér inn pláss sitt með greiningu, ekki með því að vera til: ástandsvél sem þú athugar aldrei fyrir óaðgengileg ástönd eða vantandi umskipti er óprófuð forsenda klædd sem rit. Í stóru teymi er þetta þar sem raunverulegir gallar felast, því sennilega útlítandi mynd er treyst einmitt þegar enginn hefur gengið hana gegn kröfunum til að finna vantandi villuleiðina eða munaðarlausa tengslin. Komdu með mikilvægasta hegðunarlíkanið þitt á fundinn og reyndu að brjóta það: hvaða umskipti eru óskilgreind, hvaða ástand hefur enga útgönguleið, hvaða runa hefur engin tímamörk? Þar sem kostnaður bilunar er mikill ætti svarið að ýta þér í átt að verkfærastuddri greiningu (líkanaprófurum, samræmisprófurum, hermun) frekar en að líta á það með augunum, því allur tilgangur þess að móta mikilvægan kjarna er að finna gallann á töflu en ekki í framleiðslu.

2. **Þegar tvö líkana okkar eru ósammála, hvort vinnur og hver tekur eftir mótsögninni?** Samræmi skiptir máli innan og milli líkana, og misvísandi líkön eru verri en engin, því fólk bregst við báðum. Í stóru kerfi reka einingarnar í gagnalíkaninu, flokkarnir í hönnuninni og nafnorðin í kröfunum hljóðlega í sundur þegar ólík teymi uppfæra ólíkar afurðir, og fyrsta merkið er oft framleiðslugalli þar sem tveir íhlutir voru ósammála um hvað hlutur er. Komdu með dæmi: veldu kjarnahugtak og athugaðu hvort ERD, kóðinn og kröfurnar séu í raun sammála um lögun þess og lífsferil. Ef ekki, ákveddu hvaða afurð er valdbær og hver er ábyrgur fyrir að halda hinum í takt, og vertu tilbúinn að eyða líkani frekar en að leyfa úreltu að halda áfram að ljúga að teyminu.

3. **Hvaða kjarni í kerfinu okkar, ef hann er rangur, tapar raunverulegum peningum eða skaðar einhvern, og fær hann nákvæmnina sem hann verðskuldar?** Aðalhreyfing þessa kafla er að láta aðferð passa áhættu: þumalfingurs- og lipra aðferðir fyrir afturkræfa meirihlutann, formlega tilgreiningu og sannprófun fyrir litla áhrifamikla kjarnann og ódýra frumgerðasmíði fyrir raunverulega óvissuna. Bilunarhættirnir eru samhverfir og báðir dýrir: að beita formlegum aðferðum á markaðsvefsíðu brennir peninga, og að meðhöndla uppgjörsvél eða hæfisreglusett sem venjulega lipra vinnu býður skelfilegum, óafturkræfum galla heim. Komdu með kort af kerfinu þínu og merktu hvar villa er skelfileg á móti afturkræf og hvar kröfur eru vissar á móti óþekktar. Svarið ætti að einbeita mótunarfjárfestingu þinni þar sem peningarnir og tvíræðnin eru og halda henni berum orðum frá öllu öðru, svo mikilvægur formlegur kjarni geti setið inni í annars lipru umslagi án þess að nokkur aðferð leki inn á svæði hinnar.

4. **Hve mikla mótun gerum við áður en við skrifum kóða og breytist sá skammtur með óvissunni fyrir framan okkur?** Stór hönnun fyrirfram og engin hönnun eru báðir bilunarhættir, og rétti skammturinn situr þar á milli, stýrður af því hve mikla óvissu líkan leysir í raun. Í stóru teymi liggur þrýstingurinn í báðar áttir: stjórnarháttaferli kann að krefjast fulls safns rita áður en nokkur kóði er skrifaður, sem læsir ákvarðanir teknar með minnstu upplýsingarnar, á meðan afhendingarþrýstingur kann að ýta teymi til að sleppa einu ástandsvélinni sem hefði gripið dýrt jaðartilvik. Komdu með síðustu tvö verkefni þín og flokkaðu líkönin sem þú framleiddir í þau sem upplýstu raunverulega ákvörðun og þau teiknuð aðeins af því sniðmát bað um þau. Í fyrirtækja- og opinberum áætlunum, þar sem áfangahlið eða samþykkisstjórn krefst oft skjala fyrirfram, vertu tilbúinn að mæla fyrir mótun sem fylgir áhættu frekar en föstum afurðalista, svo greiðslukjarninn fái nákvæmni sína og innra skýrsluverkfærið drukkni ekki í ritum sem enginn les.

5. **Höfum við samþykkt sameiginlegt táknmál og eitt heimili fyrir líkön okkar, eða finnur hvert teymi upp sitt eigið?** Líkön eru fyrst og fremst samskiptaafurðir, og gildi þeirra hrynur þegar ástandsvél teiknuð í verkfæri eins teymis er ekki hægt að lesa, finna eða treysta af teyminu sem erfir hana. Fyrir hundruð verkfræðinga eru sjónarmiðin sem togast á raunveruleg: skyldað táknmál og geymsla kaupa samræmi og finnanleika, en leggja líka á námskostnað og geta ýtt fólki í átt að þungum verkfærum þegar ljósmynduð tafla myndi duga. Komdu með dæmi um hvar líkan bjó í raun (wiki, ritaverkfæri, glærusett, fartölva einhvers) og spurðu hver gæti fundið og skilið það sex mánuðum síðar. Í fyrirtækja- og eftirlitsskyldu umhverfi skerpir úttektarhornið þetta: endurskoðandi sem getur ekki fundið núverandi gagnalíkan eða rakið ákvörðun til skjalfestrar ástandsvélar mun líta á kerfið sem óskjalfest, svo komdu þér saman um lítið sameiginlegt táknmál og varanlegan stað, og samþykktu létta fönguð frekar en helgisið hvar sem afleiðingin er lítil.

6. **Áður en við smíðum frumgerð ákveðum við af ásetningi hvort hún sé einnota eða þróunarkennd og höldum við okkur við það val?** Klassíska, dýra bilunin er einnota frumgerð sem rennur hljóðlega í framleiðslu því hún sýndist vel í kynningu og enginn nefndi gerð hennar fyrirfram. Spennan er raunveruleg: einnota frumgerðir kaupa ódýrasta mögulega nám og ætti að eyða, á meðan þróunarfrumgerðir verða varan og verða að vera smíðaðar eftir framleiðslustöðlum frá fyrstu línu, og að rugla þessu tvennu annaðhvort sóar endurvinnslu eða afhendir brothættan kóða í hlutverk sem hann var aldrei hannaður fyrir. Komdu með nýlega frumgerð og spurðu hvað var ákveðið áður en hún var smíðuð, hver hafði vald til að upphefja eða farga henni og hvort sú ákvörðun lifði afhendingarþrýsting. Í opinberu og öðru ábyrgu umhverfi, þar sem borgarasnúið kerfi ber gagnsæis- og áreiðanleikaskyldur, skaltu líta á óviljandi upphafningu sem stýringarbrest: festu örlög frumgerðarinnar fyrirfram og gerðu að farga árangursríkri einnota frumgerð að fögnuðum árangri en ekki sóun til að forðast.

## Sjónarhorn eftir geirum

**Sprotafyrirtæki.** Mótaðu á töflu, ljósmyndaðu hana og haltu áfram. Af skornum skammti auðlind þín er verkfræðiathygli, svo náðu í líkan aðeins þegar það er ódýrara en mistökin sem það kemur í veg fyrir: áskriftarástandsvél áður en þú kóðar jaðartilvik reikningagerðar, ekki fulla UML-skrá fyrir vöru sem getur snúið við í næsta mánuði. Vertu þumalfingurs- og lipur, hafðu formlegar aðferðir alveg af borðinu og líttu á hverja frumgerð sem einnota nema þú ákveðir annað meðvitað.

**Lítið fyrirtæki.** Þú hefur líklega engan sem starfar við formlega mótun, svo hallaðu þér að líkönunum sem þegar eru innbyggð í verkfærin og rammana sem þú kaupir frekar en að koma upp eigin mótunarvenju. Rammaðu fáu líkönin sem þú teiknar í kringum áþreifanlegar ákvarðanir: einföld gagnalíkansskissa til að koma sér saman um hvaða viðskiptavinagögn þú heldur, ástandsrit fyrir eitt vinnuflæðið sem tapar þér viðskiptavini þegar það bilar. Kjóstu keypta vöru með sannreynt gagnalíkan fram yfir að smíða og skjalfesta þitt eigið og haltu því sem þú teiknar nógu léttu til að ein manneskja geti viðhaldið því.

**Stórfyrirtæki.** Meginvandinn er samhæfing yfir mörg teymi, svo sameiginleg líkön verða sameiginlegi grundvöllurinn: samþykkt gagnalíkan, samræmt táknmál og heimili þar sem ERD, C4-ritin og ástandsvélarnar finnast og er treyst. Staðlaðu lítið táknmál og framfylgdu samræmi svo einingarnar í kröfunum, hönnuninni og gagnagrunninum reki ekki í sundur milli teyma. Taktu frá formlega tilgreiningu og líkanaprófun fyrir áhrifamikla kjarna (uppgjör, afstemmingu, aðgangsstýringu), fjármagnaðu sérfræðiþekkinguna sem það krefst og haltu úttektarslóð frá hverju skjalfestu líkani aftur til ákvörðunarinnar sem það réttlætti.

**Hið opinbera.** Reglur settar í lög verða að vera rekjanlegar til laga, sem er þar sem formleg tilgreining vinnur sér inn kostnað sinn: tilgreindu hæfis- eða álagningarrökfræði nákvæmlega, sannprófaðu lykileiginleika og leyfðu endurskoðendum að rekja hverja niðurstöðu aftur til reglunnar sem framleiddi hana. Innkaup bæta við eigin þunga, þar sem skjöl og líkön eru oft samningsbundnar afurðir, svo komdu þér saman um hvaða líkön eru raunverulega ákvörðunarberandi frekar en framleidd aðeins til að fullnægja gátlista. Birtu látlausar lýsingar á því hvernig afdrifarík kerfi virka og notaðu einnota frumgerðasmíði til að prófa borgarasnúna móttöku með raunverulegum notendum áður en þú skuldbindur þig til framleiðslusmíði.

## Dæmi

**Sprotafyrirtæki.** Lítið sprotafyrirtæki sem smíðar áskriftarreikningavöru teiknar áskriftarlífsferilinn (prufa, virk, í vanskilum, afturkölluð, endurvirkjuð) sem ástandsvél á töflu áður en það skrifar kóða. Þegar þeir ganga í gegnum ritið taka þeir eftir að þeir skilgreindu aldrei hvað gerist þegar greiðsla reiknings í vanskilum loksins gengur í gegn, jaðartilvik sem hefði skilið raunverulega viðskiptavini eftir í lausu lofti. Það fimm mínútna líkan sparar framleiðsluhöfuðverk og þeir ljósmynda það frekar en að viðhalda þungu ritaverkfæri. Alls staðar annars staðar halda þeir sig lipra og móta rétt nóg til að samræma, því í þeirra stærð er galli afturkræfur og formlegar aðferðir væru hreinn kostnaður.

**Stórfyrirtæki.** Alþjóðlegur banki smíðar nýjan greiðsluvettvang. Teymið notar eininga-tengslarit til að koma sér saman um sameiginlega gagnalíkanið yfir reikninga-, höfuðbókar- og skilaboðateymin og C4-rit (kafli 3.1) til að sýna hvernig þjónusturnar passa saman. Þeir móta færslulífsferilinn (í bið, hreinsuð, gerð upp, snúið við, umdeild) sem skýra ástandsvél, og greining sýnir að hana vantar umskipti fyrir hlutaviðsnúninga. Bilið er lagað á töflu en ekki í framleiðslu. Runurit ganga í gegnum uppgjörsflæðið gegn kröfunum (kafli 2.8) til að draga fram vantandi tímamarka- og endurtekningarleiðir. Dagleg afhending er lipur, en kjarnaafstemmingarreikniritið, þar sem villa þýðir raunverulega tapaða peninga, fær formlega tilgreiningu og er líkanaprófað fyrir innleiðingu. Mótun er einbeitt þar sem peningarnir og tvíræðnin eru og haldið léttri alls staðar annars staðar.

**Hið opinbera.** Landsbundin skattstofnun nútímavæðir bótaálagningu. Því hæfisreglur eru settar í lög og úttektaðar skrifar teymið formlega tilgreiningu reglnanna sem hreinar umbreytingar og sannprófar lykileiginleika, svo sem að enginn umsækjandi sé bæði hæfur og óhæfur og að hvert mál nái ákvörðun, svo endurskoðendur geti rakið niðurstöður aftur til laga. Samhliða formlega kjarnanum smíðar teymið einnota frumgerð af borgarasnúnu móttökueyðublaði til að prófa með raunverulegum notendum. Þeir læra að fjölþrepa leiðarvísir fækkar villum, farga síðan frumgerðinni og endurbyggja móttökuna eftir framleiðslustöðlum. Athafnarit skjalfesta ferli sakamanns frá enda til enda fyrir þjálfun og úttekt. Áhrifamiklu reglurnar fá formlega nákvæmni, óvissa notendaupplifunin fær ódýra frumgerðasmíði og hvorug aðferðin er beitt þar sem hin á heima.

## Viðskiptarök: hvatar, ávöxtun fjárfestingar og heildarkostnaður

Ávöxtun mótunar kemur frá því að finna galla fyrr, þar sem þeir eru miklu ódýrari að laga. Mótsögn fundin á töflu kostar mínútur. Sama mótsögn fundin í framleiðslu getur kostað rekstrarrof, endurvinnsluáætlun eða, í eftirlitsskyldum sviðum, lagalega skuldbindingu. Líkön lækka líka heildareignarkostnað með því að þjóna sem varanleg samskipti. Kerfi sem lifir höfunda sína, eðlilega tilvikið í fyrirtækja- og opinberu umhverfi, er miklu ódýrara að viðhalda þegar gagnalíkan þess, ástandsvélar og lykilflæði eru skjalfest nákvæmlega.

Kostnaðurinn er raunverulegur og þú verður að vega hann. Líkön taka tíma að byggja, færni til að byggja vel og viðvarandi fyrirhöfn til að halda núverandi. Formlegar aðferðir bæta við sérfræðivinnu. Jafnvægispunkturinn ræðst af óvissu og afleiðingum. Þar sem hvort tveggja er lágt eyðileggur þung mótun virði og lipur þumalfingursregla vinnur. Þar sem annað hvort er hátt borgar markviss mótun, og, fyrir mikilvæga kjarnann, formleg sannprófun, sig margfalt til baka með því að koma í veg fyrir dýra flokk bilunar. Til að færa rök við forystu skaltu tengja mótunarfjárfestingu við tiltekna áhættu sem leyst er og við viðhaldanleika langlífra kerfa. Og rektu hvort líkön séu í raun notuð, því ónotað líkan er hreinn kostnaður.

## Andmynstur og gildrur

- **Mótun í sjálfri sér:** að framleiða rit því ferli krefst þeirra, ekki því þau upplýsa ákvörðun.
- **Úrelt líkön treyst sem sannleikur:** rit sem passa ekki lengur við kóðann en er enn treyst.
- **Stór hönnun fyrirfram:** tæmandi líkön framleidd fyrir allan kóða og læsa ákvarðanir teknar með minnstu upplýsingarnar.
- **Ritasprenging:** hver UML-gerð beitt einsleitt og drekkir fáu gagnlegu sýnunum í hávaða.
- **Formlegar aðferðir alls staðar:** að beita dýrri sannprófun á kóða þar sem afleiðing bilunar réttlætir það ekki.
- **Óviljandi upphafning frumgerðar:** einnota frumgerð hljóðlega afhent sem varan.
- **Táknmál fram yfir innihald:** að deila um UML-réttleika í stað þess hvort líkanið svarar spurningunni.

## Þroskalíkan

- **Stig 1 (Upphaf):** Mótun er ad hoc eða fjarverandi og hrein viðbrögð. Engin aðferð er nefnd. Líkön, þegar þau eru teiknuð yfirleitt, eru ósamræmd, ógreind og yfirgefin um leið og fundinum lýkur.
- **Stig 2 (Þróun):** Sum teymi teikna algeng rit og fylgja nefndri aðferð, en vinnubrögð eru ójöfn yfir skipulagsheildina. Líkön eru oft framleidd helgisiðalega, reka frá kóðanum og eru sjaldan greind fyrir galla.
- **Stig 3 (Stöðlun):** Sameiginlegt táknmál, skjalfestur aðferðavalsleiðarvísir og samræmisreglur eru skilgreindar og framfylgt um alla skipulagsheildina. Líkön eru valin eftir tilgangi, haldið í takt við kerfið, rýnd fyrir galla og aðferðin er látin passa áhættu hvers vanda.
- **Stig 4 (Stjórnun):** Mótun er mæld og stýrð gegn grunnlínum. Teymi rekja hve marga galla greining grípur fyrir innleiðingu, hve langt líkön reka frá kóðanum, hvort hvert líkan var í raun leitað til fyrir raunverulega ákvörðun og endurvinnsluna og hringrásartímann sem sparaðist miðað við skilgreinda grunnlínu. Aðferðaval er kvarðað eftir mældri óvissu og afleiðingum og mikilvægir kjarnar eru formlega sannprófaðir gegn samþykktum þekjumarkmiðum.
- **Stig 5 (Samhæfing):** Mótun og aðferðaval eru stöðugt bætt og samþætt afhendingar- og áhættuáætlun um skipulagsheildina. Fjárfesting aðlagast eftir því sem óvissa og afleiðingar breytast, líkön eru reglulega haldin núverandi, lögð niður eða dýpkuð á grundvelli sönnunargagna og formlegar, þumalfingurs- og frumgerðaaðferðir eru samsettar svo hver sitji nákvæmlega þar sem hún borgar sig.

## Hugmyndir til umræðu

- Fyrir síðasta verkefni þitt, hvaða líkön upplýstu raunverulega ákvörðun og hver voru teiknuð aðeins því ferli krafðist þeirra?
- Hvar í kerfum þínum myndi formleg tilgreining borga sig og hvar væri hún sóun?
- Hvernig ákveðurðu hvort frumgerð sé einnota eða þróunarkennd og framfylgirðu þeirri ákvörðun?
- Hvernig heldurðu líkönum frá því að reka úr takti við kóðann, eða samþykkirðu að sumum ætti frekar að eyða?
- Hvert er rétt magn mótunar fyrir kóða í þínu samhengi og hvernig breytist það með óvissu?
- Hvert hegðunarlíkana (ástands, runu eða athafnar) hefði gripið nýjasta framleiðsluatvik þitt?

## Helstu atriði

- Líkan er tilgangsbundin ágripun. Ef þú getur ekki nefnt ákvörðunina sem það upplýsir, teiknaðu það ekki.
- Láttu byggingarleg og hegðunarleg líkön passa tiltekinni spurningu og haltu þeim samræmdum og núverandi.
- Greindu líkön. Óathugað líkan er óprófuð forsenda.
- Þumalfingurs- og lipur aðferð passar flestum kerfum. Taktu frá formlegar aðferðir fyrir áhrifamikla kjarna.
- Notaðu frumgerðir til að losna við óvissu og ákveddu fyrirfram hvort þær séu einnota eða þróunarkenndar.
- Fjárfestu í mótun í hlutfalli við óvissuna sem hún leysir og kostnað þess að fá ákvörðunina ranga.

## Heimildir og frekari lestur

- IEEE Computer Society, *SWEBOK Guide (Software Engineering Body of Knowledge), Version 4.0*, Software Engineering Models and Methods knowledge area
- Martin Fowler, *UML Distilled: A Brief Guide to the Standard Object Modelling Language*
- Grady Booch, James Rumbaugh, Ivar Jacobson, *The Unified Modelling Language User Guide*
- Frederick P. Brooks, *The Mythical Man-Month* and *No Silver Bullet: Essence and Accident in Software Engineering*
- Daniel Jackson, *Software Abstractions: Logic, Language, and Analysis* (the Alloy modelling language)
- Leslie Lamport, *Specifying Systems* (TLA+)
- Simon Brown, *Software Architecture for Developers* (the C4 model)
- David Harel, *Statecharts: A Visual Formalism for Complex Systems*
