# 2.18 Stjórnun ósjálfstæðis og aðfangakeðju

## Yfirlit og tilgangur

Opnaðu lásskrá verkefnisins þíns og teldu pakkana. Ef þú ert eins og flest teymi er kóðinn sem þú skrifaðir þunnt lag ofan á hundruð eða þúsundir [ósjálfstæða](https://en.wikipedia.org/wiki/Coupling_(computer_programming)) sem þú skrifaðir ekki, skilur ekki til fulls og getur ekki auðveldlega úttektað. Nútíma vefþjónusta dregur inn ramma, gagnagrunnsrekil, skráningarbókasafn og raðgreiningarsnið, og hvert þeirra dregur inn fleiri. Niðurstaðan er að mestur hluti keyrandi hugbúnaðar þíns, oft yfirgnæfandi meirihlutinn, kom frá ókunnugum á netinu. Það er ekki bilun. Það er samningurinn sem leyfir litlu teymi að afhenda á vikum það sem áður tók ár. Atriðið er að taka samninginn með opin augu.

Að stýra þessum fengna kóða vel er verkfræðigrein út af fyrir sig, og þessi kafli fjallar um handverk hennar: hvernig þú velur ósjálfstæði, festir þau, uppfærir, endurgerir smíðar þínar og heldur öllu grafinu læsilegu eftir því sem það vex. Öryggisógnarhliðin, þar sem árásaraðili eitrar vísvitandi það graf, fær fulla umfjöllun í kafla 4.2 um forritaöryggi. Hér er áhyggjuefnið dagleg verkfræði: útgáfuskorður, lásskrár, yfirfærða árekstra, uppfærslutakt og að vita hvað er í hugbúnaðinum þínum. Fáðu þetta rétt og öryggi verður miklu auðveldara, því þú getur ekki varið aðfangakeðju sem þú sérð ekki.

Fyrir stór teymi, og sérstaklega fyrir fyrirtæki og hið opinbera, hækka hagsmunirnir með stærð. Þegar fimm hundruð hugbúnaðarsöfn velja hvert sín eigin bókasöfn færðu fimm hundruð örlítið ólíkar útgáfur af sama skráningarramma, leyfi sem enginn samþykkti og enga leið til að svara „erum við fyrir áhrifum?“ þegar alvarlegur veikleiki lendir. Fyrirtæki svara þessu með samþykktum bókasöfnum og sameiginlegum skráningum. Opinberir aðilar svara því æ oftar með skyldum: bandaríska framkvæmdafyrirskipunin 14028 ýtti [hugbúnaðarefnisskrá](https://en.wikipedia.org/wiki/Software_supply_chain) (SBOM) og smíðaherkomu inn í grunnlínuna fyrir hugbúnað sem þeir kaupa. Skipulagsheildirnar sem haldast rólegar í næstu ósjálfstæðiskreppu eru þær sem unnu þessa vinnu áður en þær þurftu á henni að halda.

## Meginreglur

- Mestur hluti hugbúnaðar þíns er kóði sem þú skrifaðir ekki. Berðu ábyrgðina þótt þú hafir ekki skrifað hann.
- Hvert ósjálfstæði er varanleg skuldbinding jafnt og eign. Bættu þeim við af ásetningi, ekki viðbragðsdrifið.
- Festu útgáfur með lásskrám svo smíðar séu endurgeranlegar og ákvörðunarhæfar, ekki „hvað sem var nýjast þann daginn“.
- Uppfærðu með stöðugum takti, í litlum sjálfvirkum skrefum, frekar en í sjaldgæfum ógnvekjandi stökkum.
- Vittu nákvæmlega hvað er í hugbúnaðinum þínum. Þú getur ekki tryggt eða leyfisbundið það sem þú getur ekki talið upp.
- Kjóstu færri, vel viðhaldin ósjálfstæði fram yfir mörg þægileg.
- Stýrðu hvaðan pakkar koma. Óstaðfest skrá er opnar dyr.

## Ráðleggingar

### Skildu útgáfustýringu og skorðaðu hana af ásetningi

Lærðu hvernig vistkerfið þitt tjáir útgáfur, því uppfærsluhegðun þín reiðir sig alfarið á það. Flestir pakkastjórar nota einhverja mynd af [merkingarbærri útgáfustýringu](https://en.wikipedia.org/wiki/Software_versioning) (SemVer), þar sem útgáfa les MAJOR.MINOR.PATCH: plástrahækkun lofar aðeins villuleiðréttingum, minniháttar hækkun bætir við afturábak samhæfum eiginleikum og meirihækkun gefur til kynna brjótandi breytingar. Ósjálfstæðisyfirlýsingar þínar setja þá skorðu, eins og „samhæft við 4.x“ eða „að minnsta kosti 2.3.0“, sem segir leysinum hve langt hann má reika þegar hann velur útgáfur.

Vertu yfirvegaður um hve laus eða þröng þessi skorður eru. Laus svið taka upp lagfæringar sjálfvirkt, á kostnað þess að leyfa minniháttar útgáfu sem þú rýndir aldrei að renna í framleiðslu. Þröngar festingar gefa stjórn á kostnað handvirkrar fyrirhafnar. Raunsæja svarið fyrir flest teymi er að lýsa yfir hæfilega frjálslegum sviðum í skránni þinni og frysta síðan nákvæmu leystu útgáfurnar í lásskrá svo sviðið sé aðeins endurmetið þegar þú uppfærir af ásetningi. Líttu á SemVer sem loforð sem viðhaldsmenn reyna að halda, ekki ábyrgð sem þeir halda alltaf. „Plástra“-útgáfa getur samt brotið þig, sem er einmitt hvers vegna þú prófar uppfærslur frekar en að treysta þeim.

### Innritaðu lásskrár og krefstu endurgeranlegra smíða

Lásskrá skráir nákvæma útgáfu og dulritunarsamantekt hvers pakka í ósjálfstæðisgrafinu þínu, bein og yfirfærð jafnt. Innritaðu hana í útgáfustýringu (kafli 2.6) og líttu á hana sem fyrsta flokks hluta frumkóða þíns. Verk hennar er að gera smíðina að falli: sömu inntök framleiða sama úttak í hvert skipti, á hverri vél, þetta ár og það næsta. Án hennar geta tveir verkfræðingar sem keyra „install“ með viku á milli fengið mismunandi kóða, og galli sem birtist í framleiðslu getur verið ómögulegt að endurskapa á fartölvunni sem smíðaði hann.

Stefndu að raunverulega [endurgeranlegum smíðum](https://en.wikipedia.org/wiki/Reproducible_builds), þar sem tiltekið commit gefur alltaf hegðunarlega eins afurð. Í samfelldri samþættingu (kafli 8.1) skaltu setja upp stranglega úr lásskránni og láta smíðina mistakast ef lásskráin og skráin eru ósammála, frekar en að leysa hljóðlega nýjar útgáfur. Samantektirnar í lásskránni gera tvöfalt gagn: þær festa hegðun og greina átroðning, því pakki þar sem innihald passar ekki lengur við skráða samantekt sinnar mun ekki setjast upp. Endurgeranleiki er grunnurinn sem allt annað í þessum kafla stendur á.

### Stýrðu yfirfærðum ósjálfstæðum og tígulárekstrum af ásetningi

Bein ósjálfstæði þín eru aðeins þau sem þú nefndir. Undir þeim situr miklu stærra graf yfirfærðra ósjálfstæða, pakkarnir sem pakkarnir þínir byggja á, og þar býr mest af áhættu þinni og óvæntum uppákomum. Klassísk bilun er tígulósjálfstæðið: bókasafn A þarf útgáfu 1 af sameiginlegu tóli, bókasafn B þarf útgáfu 2 og nú verður leysirinn að sætta ómögulega beiðni. Sum vistkerfi leyfa mörgum útgáfum að sambúa, skipta diski og minni fyrir frið. Önnur þvinga eina útgáfu og skilja þig eftir að miðla árekstrinum.

Gerðu þessa árekstra sýnilega í stað þess að láta þá grassera. Notaðu verkfærin þín til að prenta allt ósjálfstæðistréð og útskýra hvers vegna tiltekinn pakki er til staðar og hver dró hann inn. Þegar árekstur birtist skaltu leysa hann af ásetningi: uppfærðu eftirbátinn, festu yfirskrift eða fjarlægðu ósjálfstæði sem þú getur ekki mætt kröfum. Fylgstu með vexti grafsins yfir tíma, því óstýrð útbreiðsla yfirfærðra ósjálfstæða er hæg uppsöfnun [tæknilegrar skuldar](https://en.wikipedia.org/wiki/Technical_debt) sem að lokum birtist sem óleysanleg uppfærsla eða veikleiki sem þú getur ekki plástrað án endurskrifs.

### Uppfærðu með stöðugum takti með sjálfvirkum sameiningarbeiðnum

Áhættumesta uppfærslustefnan er sú sem flest teymi renna í fyrir slysni: uppfærðu aldrei, uppfærðu síðan allt í einu undir neyðarþrýstingi þegar mikilvægur veikleiki neyðir hönd þína. Þá ertu ár á eftir, breytingaskrárnar eru veggur og uppfærslan er margra vikna verkefni í stað venjulegs verks. Lagfæringin er taktur. Taktu upp sjálfvirkan ósjálfstæðisuppfærara (Dependabot og Renovate eru algeng dæmi) sem opnar sameiningarbeiðni þegar ósjálfstæði fær nýja útgáfu, með breytingaskránni og prófaniðurstöðum þínum fest við.

Stilltu síðan flæðið svo það hjálpi þér frekar en að drekkja þér. Flóð einstakra sameiningarbeiðna á hverjum morgni þjálfar fólk í að hunsa þær, sem er verra en engin sjálfvirkni. Lotaðu áhættulitlum uppfærslum eins og plástraútgáfum, láttu þær sameinast sjálfvirkt þegar próf standast og taktu frá mannlega athygli fyrir meirihækkanir og allt sem snertir viðkvæmt bókasafn. Settu takt sem teymið getur haldið uppi, kannski vikulega rýni, svo uppfærsla haldist lítill, stöðugur skattur frekar en sjaldgæfur sársaukafullur reikningur. Hér borgar sterk prófunarstefna (kafli 2.4) sig, því sjálfvirkar uppfærslur eru aðeins öruggar ef próf þín geta gripið það sem þær brjóta.

### Lágmarkaðu fótsporið og metðu áður en þú tekur upp

Sérhvert ósjálfstæði sem þú bætir við er viðvarandi skuldbinding: við galla þess, veikleika, leyfi, áframhaldandi áhuga viðhaldsmanns þess og eigið vaxandi graf undirósjálfstæða. Ódýrasta ósjálfstæðið að stýra er það sem þú bættir ekki við. Áður en þú nærð í pakka skaltu spyrja hvort nokkrir tugir lína af eigin kóða dygðu, sérstaklega fyrir léttvæga virkni. Saga pakkavistkerfa er full af varúðarsögum þar sem örlítill, víða treystur pakki var fjarlægður eða rændur og braut hálft internetið.

Þegar þú tekur upp skaltu meta frambjóðandann eins og langtímasambandið sem það er. Athugaðu viðhaldsheilsu: nýleg commit, svarandi viðhaldsmenn, raunverulega útgáfusögu og fleiri en eina manneskju með lyklana. Athugaðu leyfið og staðfestu að það sé á samþykkta listanum þínum (kafli 10.3). Athugaðu öryggissögu þess, stærð og eigið yfirfært fótspor, því lítill eiginleiki er ekki þess virði að draga inn hundrað pakka. Skrifaðu þessi viðmið niður svo „ættum við að bæta þessu við?“ sé gátlisti sem allt teymið þitt beitir samræmt, ekki skap.

### Framleiddu SBOM og fangaðu smíðaherkomu

Þú getur ekki svarað „erum við fyrir áhrifum af þessum veikleika?“ hratt nema þú vitir þegar hvað er í hugbúnaðinum þínum. SBOM er svarið: véllæsileg skrá yfir hvern íhlut í smíð, með útgáfum og leyfum, á stöðluðu sniði eins og SPDX eða CycloneDX. Myndaðu eina sjálfvirkt sem hluta smíðaleiðslu þinnar, geymdu hana við hlið afurðarinnar og haltu henni eins lengi og sú afurð keyrir einhvers staðar. Þegar næsti fyrirsagnarveikleiki lendir breytir fyrirspurn gegn SBOM-um þínum viku af örvæntingarfullu grep í fimm mínútna skýrslu.

Farðu skrefi lengra og fangaðu herkomu: undirritaða, átroðningsgreinandi skrá um hvernig afurð var smíðuð, úr hvaða frumkóðacommit, af hvaða leiðslu. [Opinn hugbúnaðar](https://en.wikipedia.org/wiki/Open-source_software)samfélagið hefur sameinast um SLSA-rammann (Supply-chain Levels for Software Artifacts) sem stigskipt líkan fyrir einmitt þetta, frá „við getum lýst smíði okkar“ upp í „við getum sannað það, og sönnunin stenst í hættu komið smíðakerfi“. Vottun leyfir neytanda að sannreyna að afurð hafi í raun komið úr leiðslunni þinni. Fyrir opinbera vinnu er þetta æ oftar ekki valkvætt. Herkoma og SBOM sitja innan innkaupaskylda, svo að byggja getuna snemma heldur þér hæfum til að bjóða.

### Stýrðu uppsprettum þínum með skrám, speglum og vendoring

Hvaðan pakkarnir þínir koma skiptir jafn miklu máli og hvaða pakka þú velur. Sæktu beint af opinbera internetinu við hverja smíði og þú erfir rekstrarrof þess, afturkallaðar útgáfur og árásaraðila. Settu upp innri pakkaskrá eða skyndiminnisspegil sem milligöngu fyrir opinbera vistkerfið, svo smíðar séu hraðar, endurtakanlegar og einangraðar frá því að upptök hverfi. Skráin verður líka eðlilegur staður til að framfylgja stefnu: lokaðu á þekktar slæmar útgáfur, settu nýjar útgáfur í stutta bið og hafnaðu pökkum sem falla á leyfis- eða öryggishlið þín.

Stilltu þá skrá vandlega til að forðast tvær sértækar gildrur. Ósjálfstæðisruglingur gerist þegar smíðaverkfæri, boðið bæði innri einkapakka og opinberan pakka með sama nafni, sækir opinbera pakka árásaraðilans. Þú ver þig gegn því með því að afmarka innri nöfn og festa innri pakka við innri uppsprettuna skýrt. [Ritvillunöfnun](https://en.wikipedia.org/wiki/Typosquatting) (typosquatting) gerist þegar illgjarn pakki notar nafn einu lyklaslagi frá vinsælu og bíður eftir feitum fingri. Samansett skrá með leyfislista hindrar það við dyrnar. Fyrir lítið safn mikilvægra eða hægbreytilegra ósjálfstæða skaltu íhuga vendoring, að innrita raunverulega ósjálfstæðisfrumkóðann í eigið hugbúnaðarsafn, svo smíðin þín hafi núll ytri ósjálfstæði. Það skiptir uppfærsluþægindum fyrir algjöra stjórn, sem er stundum einmitt rétt.

## Málamiðlanir: kostir og gallar

| Nálgun | Kostir | Gallar |
| --- | --- | --- |
| Laus útgáfusvið | Sjálfvirkar lagfæringar, lítil handvirk fyrirhöfn | Órýndur kóði nær framleiðslu, óákvörðunarhæft án lásskrár |
| Ströng festing auk lásskrár | Endurgeranlegar, úttektarhæfar smíðar | Krefst yfirvegaðrar uppfærsluvinnu, getur dregist aftur úr í lagfæringum |
| Ágengur uppfærslutaktur | Lítil, örugg skref, alltaf nálægt núverandi | Stöðugt rót, krefst stöðugrar rýniathygli |
| Sjaldgæfar, lotaðar stórar uppfærslur | Færri truflanir dag frá degi | Ógnvekjandi, áhættusamt, dýrt þegar þvingað |
| Mörg þægileg ósjálfstæði | Hratt að byggja eiginleika | Stórt árásaryfirborð, þungt viðhaldsálag |
| Lágmarksfótspor auk vendoring | Stjórn, lítið yfirborð, engin upptakaáhætta | Meiri kóði sem þú átt, þú berð uppfærslurnar sjálfur |
| Opinber skrá beint | Engin uppsetning | Rekstrarrof, afturkallanir, rugling- og ritvillunöfnunarútsetning |
| Innri skrá og spegill | Hraði, stefnuframfylgd, einangrun | Innviðir til að reka og viðhalda |

Meginspennan liggur milli hraða og stjórnar. Sérhvert val hér að ofan er sama skífan séð frá mismunandi sjónarhorni: hve mikið af fengna kóðanum þínum ætlarðu að stýra virkt og hve mikið ætlarðu að láta flæða inn á trausti? Hallaðu of langt í stjórn og þú drukknar í handvirkri rýni, dregst aftur úr í öryggislagfæringum og hægir á teyminu sem ósjálfstæði áttu að flýta. Hallaðu of langt í hraða og þú vaknar einn daginn með óúttektarhæft, óuppfærsluhæft graf og leyfisbrot sem þú getur ekki útskýrt fyrir lögfræðingi. Lausnin er afstaða, ekki fastur punktur: læstu og endurgerðu allt, uppfærðu stöðugt í litlum skrefum, lágmarkaðu það sem þú tekur á þig og framfylgdu stefnu við flöskuháls sem þú stjórnar. Sú samsetning kaupir bæði hraða og öryggi, sem er málamiðlunin sem er þess virði að gera í stórum stíl.

## Spurningar til að ræða með teyminu

1. **Hver er raunverulegur uppfærslutaktur þinn og myndi þvinguð neyðaruppfærsla taka klukkustundir eða vikur?** Flest teymi geta ekki svarað þessu heiðarlega fyrr en mikilvægur veikleiki neyðir málið. Kaflinn lítur á stöðuga, sjálfvirka, smáskrefa uppfærslu sem örugga leið og sjaldgæfa stórhvells-uppfærslu sem hættulega, því bilið sem þú lætur opnast er bilið sem þú verður að spretta yfir undir þrýstingi síðar. Komdu með sönnunargögnin: hve mörg ósjálfstæði þín eru meira en eina meirihækkun á eftir og hve langan tíma síðasta mikilvæga uppfærsla þín tók í raun. Ræddu hvort þú getir tekið upp sjálfvirkan uppfærara, hvernig þú lotar áhættulitlum breytingum svo fólk stilli sig ekki út og hvaða prófanir þú þarft til að sjálfvirk sameining sé örugg. Svarið ætti að breyta því hvernig þú fjárhagsáætlar verkfræðitíma og breyta sjaldgæfri kreppu í venjulegan vikulegan skatt. Ef heiðarlega svarið er „vikur“ er það áhætta til að nefna núna, ekki uppgötva í miðju atviki.

2. **Ef alvarlegur veikleiki yrði tilkynntur í algengu bókasafni núna, hve fljótt gætirðu skráð hverja áhrifaða afurð sem þú rekur?** Þetta er spurningin sem SBOM er til að svara, og hraði svars þíns er bein mæling á aðfangakeðjuþroska þínum. Án skrár ertu skertur við að grep'a hugbúnaðarsöfn og taka viðtöl við teymi, sem tekur daga sem þú hefur kannski ekki meðan klukkan tifar. Komdu með áþreifanlega merkið: býrðu til SBOM á smíð, hvar er hún geymd og geturðu í raun spurt yfir þær allar í dag? Ræddu hvort þú þekkir ekki aðeins bein ósjálfstæði heldur yfirfærða grafið, því veikleikapakkinn er venjulega einn sem þú nefndir aldrei. Svarið ákvarðar hvort næsta atvik þitt er fyrirspurn eða brunaæfing, og það er þess virði að byggja getuna áður en þú þarft hana. Opinberir aðilar skylda þetta nú einmitt af þeirri ástæðu.

3. **Hvernig ákveðurðu hvort nýtt ósjálfstæði sé þess virði að taka upp og beitir allir sama viðmiði?** Kaflinn heldur því fram að hvert ósjálfstæði sé varanleg skuldbinding jafnt og þægindi, og að ódýrasta að stýra sé það sem þú bættir aldrei við. Samt er ákvörðunin ósýnileg hjá flestum teymum: verkfræðingur þarf eiginleika, finnur pakka og hann er í lásskránni fyrir hádegi án rýni á viðhaldi hans, leyfi, öryggissögu eða fótspori. Komdu með dæmi úr eigin grafi um pakka sem enginn man eftir að hafa tekið upp og gæti ekki varið í dag. Ræddu hvort skriflegur matsgátlisti og samþykktur bókasafnalisti (kafli 10.3) myndu hjálpa eða bara bæta við núningi og hvar línan liggur milli léttvægra hjálparhluta sem þú ættir að skrifa sjálfur og raunverulegra innviða sem vert er að byggja á. Svarið mótar langtímaþyngdina sem teymið þitt ber, eina litla ákvörðun í einu.

4. **Stýrirðu í raun yfirfærðu ósjálfstæðum þínum, eða aðeins þeim sem þú nefndir?** Mest af áhættu þinni býr einu stigi neðar, í pökkunum sem pakkarnir þínir drógu inn, og tígulárekstur þar sem tvö bókasöfn krefjast ósamrýmanlegra útgáfa af sameiginlegu tóli getur hindrað uppfærslu á versta mögulega augnabliki. Þetta skiptir máli í stórum stíl því einn óplástranlegur yfirfærður pakki getur fryst öryggislagfæringu yfir hundruð hugbúnaðarsafna, og togið á móti er raunverulegt: að draga fram og festa allt grafið kostar viðvarandi fyrirhöfn, á meðan að hunsa það skiptir þeirri fyrirhöfn fyrir hæga uppsöfnun skuldar sem birtist sem óleysanleg uppfærsla. Komdu með sönnunargögnin: getur verkfærakeðjan þín prentað allt tréð og útskýrt hvers vegna tiltekinn pakki er til staðar og hver dró hann inn, og hve margar ólíkar útgáfur af algengustu bókasöfnum þínum sambúa í dag? Fyrir fyrirtæki og hið opinbera skaltu bæta við hvort skrá þín og stefna ná yfirleitt til yfirfærðra íhluta, því skylda til að vita hvað er í hugbúnaðinum þínum er merkingarlaus ef hálft grafið er ósýnilegt þér. Svarið segir þér hvort næsta þvingaða uppfærsla þín er venjuleg sameining eða fjölteymis uppgröftur.

5. **Hvaðan koma pakkarnir þínir í raun og hvað stöðvar árásaraðila frá því að renna einum inn?** Sérhver smíð sem sækir beint af opinbera internetinu erfir rekstrarrof þess, afturkallaðar útgáfur og tvær sértækar árásir: ósjálfstæðisruglingur, þar sem smíðaverkfæri sækir opinberan pakka sem skyggir á einkapakkann þinn, og ritvillunöfnun, þar sem illgjarn pakki situr einu lyklaslagi frá vinsælu nafni. Þetta skiptir máli fyrir stórt teymi því ein eitruð sókn getur breiðst um allt landslag þitt áður en nokkur tekur eftir, og málamiðlunin er ósvikin: innri skrá eða skyndiminnisspegill gefur þér stefnuflöskuháls og einangrun frá upptökum, en hún er innviðir sem einhver þarf að reka og halda núverandi. Komdu með áþreifanlega merkið: eru innri pakkanöfn afmörkuð og fest við innri uppsprettuna skýrt, er leyfislisti til staðar og fær nokkur ný útgáfa stutta sóttkví áður en hún má notast? Fyrir opinbera og eftirlitsskylda kaupendur skaltu tengja þetta við samþykkta-hugbúnaðarlistann og engin-bein-internet afstöðuna sem innkaup krefjast æ oftar og vera heiðarlegur um hvort núverandi uppsetning þín stæðist þá kröfu í dag.

6. **Geturðu í raun endurskapað og sannað hvernig afurðir þínar voru smíðaðar?** Innrituð lásskrá með dulritunarsamantektum ætti að gera smíðina þína að falli, sömu inntök gefa sama úttak á hverri vél þetta ár og það næsta, og herkoma ætti að leyfa hverjum sem er að sannreyna að afurð hafi í raun komið úr leiðslunni þinni og frumkóðacommit. Þetta skiptir máli því óendurgeranleg smíð breytir framleiðslugalla í óleysanlega dulúð og skilur þig án getu til að sanna að átroðningur hafi ekki átt sér stað, og sjónarmiðið á móti er fyrirhöfn gegn tryggingu: ströng lásskráruppsetning, undirrituð vottun og SLSA-samræmd herkoma kosta uppsetningu og aga sem „settu bara upp nýjast“ flæði forðast. Komdu með sönnunargögnin: bregst samfelld samþætting þegar lásskráin og skráin eru ósammála, býrðu til og geymir SBOM og undirritaða herkomuskrá á smíð og hefur nokkur sannreynt eina? Fyrir fyrirtæki og sérstaklega opinbera vinnu sitja herkoma og SBOM æ oftar innan innkaupaskylda, svo heiðarlega svarið hér ákvarðar hvort þú haldist hæfur til að bjóða eða sért útilokaður.

## Sjónarhorn eftir geirum

**Sprotafyrirtæki.** Með pínulítið teymi og engan vettvangshóp skaltu hallast að sjálfgefnum gildum og sjálfvirkni frekar en ferli. Innritaðu lásskrár frá fyrsta degi, kveiktu á sjálfvirkum uppfærara sem lotar plástraútgáfum og sameinar sjálfvirkt á grænum prófum og haltu einni léttri reglu um að bæta við pökkum: kjóstu leiðinleg, vel viðhaldin bókasöfn og hugsaðu þig tvisvar um um örlitla. Þú munt ekki byggja innri pakkaskrá enn, og það er í lagi, en innrituðu samantektirnar einar og sér verja þig nú þegar: eitruð útgáfa mun einfaldlega ekki setjast upp.

**Lítið fyrirtæki.** Þú hefur engan ósjálfstæðissérfræðing og þröngt fjárhagsáætlun, svo keyptu aginn frekar en að byggja hann. Reiddu þig á uppfærslusjálfvirknina sem hýsingar- og kóðavettvangur þinn veitir nú þegar, kjóstu lítið safn þroskaðra bókasafna svo uppfærslur haldist ódýrar og notaðu ókeypis SBOM-myndara í leiðslunni þinni svo þú getir svarað „erum við fyrir áhrifum?“ án þess að manna það. Eyddu af skornum skammti athygli í leyfisathuganir og í að taka ekki upp léttvæga pakka sem þú gætir skrifað á tugi lína sjálfur.

**Stórfyrirtæki.** Vandinn er samræmi milli margra teyma: sameiginleg innri skrá sem speglar opinbera vistkerfið og framfylgir leyfis-, uppsprettu- og útgáfustefnu við einn flöskuháls, auk samansetts safns gullbókasafna sem sjálfgefið og skjalfestrar undanþáguleiðar fyrir allt annað. Gefðu út SBOM á smíð í miðlæga geymslu svo ein fyrirspurn svari útsetningu þinni yfir allt landslagið, rúllaðu samhæfðum uppfærslum gegnum sjálfvirkar sameiningarbeiðnir og líttu á ósjálfstæðisheilsu sem mælt, stýrt eignasafn frekar en slys á hverju safni.

**Hið opinbera.** Innkaupareglur og almenn ábyrgð móta allt. Krefstu þess að söluaðilar afhendi véllæsilega SBOM og SLSA-samræmda smíðaherkomu með hverri útgáfu, settu aðeins upp innanhúss af samþykktum hugbúnaðarlista sem þjónað er af spegli án beinnar leiðar að opinbera internetinu og kjóstu ósjálfstæði með stöðugu viðhaldi og skýru leyfi því kerfi getur verið í rekstri í fimmtán ár og verður að vera plástranlegt öll þau ár. Skipuleggðu lífslokaflutninga af ásetningi frekar en sem neyðartilvik og haltu skránum sem leyfa endurskoðanda að rekja hverja afhenta afurð til frumkóða hennar.

## Dæmi

**Sprotafyrirtæki.** Sex manna sprotafyrirtæki afhendir vefforrit byggt á ramma, greiðslubókasafni og um níu hundruð yfirfærðum pökkum sem þeir hafa aldrei skoðað. Þeir hafa ekki efni á vettvangsteymi, svo þeir hallast að sjálfvirkni: lásskrár innritaðar frá fyrsta degi, sjálfvirkur uppfærari sem lotar plástraútgáfum og sameinar á grænum prófum og klukkustund í mánuði til að rýna meirihækkanirnar sem hrúguðust upp. Eins málsgreinar regla þeirra um að bæta við ósjálfstæðum er að mestu „kjóstu leiðinleg, vel viðhaldin bókasöfn og hugsaðu þig tvisvar um um örlitla“. Þegar vinsæll pakki var í hættu komin þýddu innrituðu lásskrársamantektirnar að eitraða útgáfan myndi einfaldlega ekki setjast upp og þeir lásu um atvikið frekar en að lifa það.

**Stórfyrirtæki.** Banki með fjögur hundruð hugbúnaðarsöfn rekur innri pakkaskrá sem speglar opinbera vistkerfið og framfylgir stefnu við þann flöskuháls. Samansett safn gullbókasafna, eitt samþykkt skráningarbókasafn, einn HTTP-biðlari, einn JSON-þáttari, er sjálfgefið og allt annað krefst skjalfestrar undanþágu. Innri-uppsprettu líkan leyfir hvaða teymi sem er að leggja til þessi sameiginlegu bókasöfn á meðan lítill vettvangshópur á heilsu þeirra. Samhæfðar uppfærslur rúlla öryggisplástri yfir öll fjögur hundruð hugbúnaðarsöfnin gegnum sjálfvirkar sameiningarbeiðnir á nokkrum dögum og hver smíð gefur út SBOM í miðlæga geymslu. Þegar mikilvægur veikleiki er tilkynntur keyra þeir eina fyrirspurn og vita útsetningu sína áður en fréttalotunni lýkur.

**Hið opinbera.** Alríkisstofnun kaupir hugbúnað undir herkomu- og SBOM-kröfum rekjanlegum til framkvæmdafyrirskipunar 14028. Söluaðilar verða að afhenda véllæsilega SBOM með hverri útgáfu og sýna smíðaherkomu samræmda SLSA-rammanum, svo stofnunin geti sannreynt að hver afurð hafi komið úr fullyrtri uppsprettu. Innanhúss mega hönnuðir aðeins setja upp af samþykktum hugbúnaðarlista sem þjónað er af innri spegli án beinnar leiðar að opinbera internetinu. Langtímastuðningur knýr valin: þeir kjósa ósjálfstæði með stöðugu viðhaldi og skýru leyfi, því kerfi getur verið í rekstri í fimmtán ár og verður að vera plástranlegt öll þau ár. Þegar íhlutur nær lífslokum kemur skipulagður flutningur í staðinn frekar en neyðartilvik.

## Viðskiptarök: hvatar, ávöxtun fjárfestingar og heildarkostnaður

Ávöxtun ósjálfstæðisaga er að mestu mæld í hamförum sem aldrei gerast. Innrituð lásskrá og endurgeranleg smíð kosta nánast ekkert að taka upp og útrýma heilum flokki „virkar á minni vél“ galla og óendurskapanlegra framleiðslugalla, hver þeirra getur brennt dögum af tíma eldri verkfræðinga. Sjálfvirkur uppfærslutaktur breytir stöku margra vikna neyðaruppfærslu, þeirri tegund sem stöðvar vegvísi og örmagna teymi, í stöðugt lágt suð lítilla sameinaðra breytinga. Yfir eignasafn margra hugbúnaðarsafna er sú breyting frá sjaldgæfu-og-risastóru í tíð-og-örsmátt ein áhrifamesta ferlisbreyting sem verkfræðiskipulagsheild á kost á.

Heildareignarkostnaðarrökin snúast um það sem þú berð yfir ár, ekki það sem þú eyðir þennan sprett. Óstýrð ósjálfstæði safnast hljóðlega: úreldar útgáfur sem ekki er lengur hægt að uppfæra án endurskrifs, leyfi sem skapa lagalega útsetningu sem enginn verðlagði og graf svo flækt að ein nauðsynleg plástur kveikir foss af brjótandi breytingum. Kostnaður þess að gera þetta ekki berst allur í einu og á versta tíma, í öryggisatviki eða úttekt eða þvinguðum flutningi, þegar reikningurinn fyrir ára frestað viðhald fellur á með vöxtum. Til að færa rök við forystu skaltu ramma það á hennar tungumáli: endurgeranlegar smíðar draga úr atvikskostnaði, SBOM skera viðbragðstíma við veikleikum úr dögum í mínútur og samþykkt bókasöfn auk herkomu halda þér hæfum til eftirlitsskyldra og opinberra samninga sem þú værir annars útilokaður frá.

## Andmynstur og gildrur

- **Engin lásskrá, eða óinnrituð:** smíðar leysa nýtt í hvert skipti, svo enginn getur áreiðanlega endurskapað það sem var afhent eða það sem brotnaði.
- **Fljótandi „latest“ í framleiðslu:** hvað sem skráin þjónaði þá mínútu verður útgáfa þín, órýnd og órekjanleg.
- **Aldrei uppfæra fyrr en þvingað:** ára rek hrynur í eina ógnvekjandi, áhættusama neyðaruppfærslu undir veikleikaþrýstingi.
- **Uppfærslubotaþreyta:** ólotað flóð sameiningarbeiðna þjálfar teymið í að hunsa þær allar, líka þær brýnu.
- **Ósjálfstæðisútbreiðsla:** að bæta við pökkum viðbragðsdrifið fyrir léttvæga eiginleika og rækta óviðhaldanlegt graf og breitt árásaryfirborð.
- **Engin skrá:** án SBOM þýðir að svara „erum við fyrir áhrifum?“ daga af handvirkri fornleifafræði yfir hugbúnaðarsöfn.
- **Að treysta opinberu skránni blindandi:** bein sókn útsetur þig fyrir rekstrarrofi, afturkölluðum útgáfum, ósjálfstæðisruglingi og ritvillunöfnun.
- **Að hunsa yfirfærð ósjálfstæði:** að stýra aðeins því sem þú nefndir á meðan mest af áhættu þinni felst einu stigi neðar.
- **Óskoðuð leyfi:** að draga inn kóða þar sem leyfi stangast á við hvernig þú afhendir, uppgötvað aðeins í úttekt eða yfirtöku.

## Þroskalíkan

- **Stig 1, Upphaf:** Ósjálfstæðum er bætt við frjálslega án mats. Engin innrituð lásskrá, smíðar eru ekki endurgeranlegar, uppfærslur gerast aðeins í þvinguðum neyðartilvikum og enginn getur talið upp hvað hugbúnaðurinn inniheldur.
- **Stig 2, Þróun:** Sum teymi innrita lásskrár og fá að mestu endurgeranlegar smíðar, og lítil sjálfvirkni opnar uppfærslusameiningarbeiðnir, en vinnubrögð eru ósamkvæm frá hugbúnaðarsafni til hugbúnaðarsafns. Vitund um leyfi og yfirfærða áhættu er óformleg, án sameiginlegrar stefnu, skrár eða stjórnar yfir hvaðan pakkar koma.
- **Stig 3, Stöðlun:** Vinnubrögð eru skjalfest og framfylgt um alla skipulagsheildina. Sjálfvirkur uppfærari keyrir með stöðugum takti og skynsamlegri lotun, smíðar setja stranglega upp úr lásskrám og bregðast þegar lásskráin og skráin eru ósammála, SBOM er búin til á smíð, innri skrá framfylgir uppsprettu- og leyfisstefnu og ný ósjálfstæði eru metin gegn skriflegum gátlista sem hvert teymi beitir.
- **Stig 4, Stjórnun:** Ósjálfstæðislandslagið er mælt og stýrt með gögnum gegn grunnlínum. Þú rekur útgáfubil (hve mörg ósjálfstæði sitja meira en eina meirihækkun á eftir), meðaltíma til að plástra mikilvægan veikleika yfir allar afurðir, sjálfvirk uppfærslusameiningarhlutföll, SBOM-þekju sem hlutfall afhentra smíða og fjölda óleystra tígulárekstra og stefnuundanþága. Þessir mælikvarðar hliða útgáfur og knýja hvert þú eyðir fyrirhöfn, svo uppfærslur og úrbætur séu stýrðar af sönnunargögnum en ekki þeim sem hrópar hæst.
- **Stig 5, Samhæfing:** Ósjálfstæðisstjórnun er stöðugt bætt og samþætt um skipulagsheildina. Smíðaherkoma og vottun eru fönguð og sannreynd, SBOM eru fyrirspurnarhæfar yfir allt eignasafnið fyrir tafarlaus veikleikaviðbrögð, samhæfðar uppfærslur rúlla yfir mörg hugbúnaðarsöfn sjálfvirkt, gullbókasöfn eru samansett og innri-uppsprettu og allt kerfið aðlagast eftir því sem vistkerfið, ógnir og innkaupaskyldur breytast.

## Hugmyndir til umræðu

1. Hvar er rétta línan fyrir teymið þitt milli þess að skrifa lítið tól sjálfur og að taka á sig ósjálfstæði fyrir það?
2. Hve laus eða þröng ættu útgáfuskorðurnar þínar að vera og er svarið ólíkt fyrir forrit á móti útgefnum bókasöfnum?
3. Ættu áhættulitlar plástraruppfærslur að sameinast sjálfvirkt á grænum prófum og hvað þyrfti prófasafn þitt til að gera það öruggt?
4. Er innri skrá eða spegill rekstrarkostnaðarins virði fyrir stærð og áhættusnið skipulagsheildar þinnar?
5. Hvernig myndirðu forgangsraða hvaða ósjálfstæði á að vendora fyrir hámarksstjórn og hver á að skilja eftir á opinberu skránni?
6. Hvað þyrfti til að búa til og í raun nota SBOM fyrir hverja afurð sem þú afhendir, frá og með þessum ársfjórðungi?

## Helstu atriði

- Mestur hluti hugbúnaðar þíns er fenginn kóði. Að stýra honum vel er kjarnaverkfræðigrein, ekki eftiráhugsun.
- Innritaðu lásskrár og krefstu endurgeranlegra, ákvörðunarhæfra smíða svo sömu inntök framleiði alltaf sama úttak.
- Uppfærðu stöðugt í litlum sjálfvirkum skrefum í stað sjaldgæfra, þvingaðra, ógnvekjandi stökka.
- Bættu við ósjálfstæðum af ásetningi gegn skriflegu viðmiði. Ódýrasta að stýra er það sem þú tókst aldrei á þig.
- Búðu til SBOM og fangaðu herkomu svo þú vitir alltaf hvað er í hugbúnaðinum þínum og hvaðan hann kom.
- Stýrðu uppsprettum þínum með innri skrá til að verja gegn rugling, ritvillunöfnun og upptakabilun.

## Heimildir og frekari lestur

- U.S. Executive Order 14028, *Improving the Nation's Cybersecurity* (2021)
- National Institute of Standards and Technology (NIST), *Secure Software Development Framework* (SP 800-218)
- SLSA (Supply-chain Levels for Software Artifacts) framework specification, Open Source Security Foundation
- OWASP CycloneDX specification and the SPDX specification, for SBOM formats
- Tom Preston-Werner, *Semantic Versioning Specification (SemVer)*
- The Reproducible Builds project documentation
- Nicole Forsgren, Jez Humble, Gene Kim, *Accelerate: The Science of Lean Software and DevOps*
