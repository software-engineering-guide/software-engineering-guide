# 8.2 Innviðir sem kóði og stillingar

## Yfirlit og tilgangur

[Innviðir sem kóði](https://en.wikipedia.org/wiki/Infrastructure_as_code) (IaC) þýðir að skilgreina og útvega innviði (net, þjóna, gagnagrunna, álagsjafnara, heimildir) gegnum vélrænt læsilegar skilgreiningarskrár frekar en handvirka stjórnborðssmelli eða ad hoc skriftur. [Stillingastjórnun](https://en.wikipedia.org/wiki/Configuration_management) framlengir sömu hugmynd til stillinga og ástands kerfa eftir að þau eru til. Saman breyta þau innviðum úr handsmíðuðum, brothættum grip í útgáfustýrða, rýnanlega, endurtakanlega afurð sama verkfræðiaga og þú notar fyrir forritskóða.

Fyrir stór teymi er IaC ekki þægindi heldur nauðsyn. Þegar hundruð verkfræðinga þurfa umhverfi og þúsundir auðlinda verða að haldast samræmdar yfir svæði og reikninga getur handvirk útvegun ekki haldið í við og ekki haldist rétt. Handstilltir innviðir reka fyrr eða síðar í einstaka „snjókorna“-þjóna sem enginn skilur til fulls og ekki er hægt að endurbyggja áreiðanlega eftir bilun. Að kóða innviði gerir þá samræmda, úttektarhæfa og einnota. Hvert umhverfi má endurskapa úr skilgreiningu sinni og hver breyting er rýnanlegur mismunur.

Fyrirtæki og opinberar skipulagsheildir fá einn ávinning í viðbót, afgerandi: framfylgjanlega stjórnarhætti. Öryggis- og reglufylgnikröfur, eins og dulkóðun í hvíld, netskiptingu, samþykkt svæði og merkingu fyrir kostnaðarskiptingu, má fella beint inn í kóðann og athuga sjálfvirkt áður en nokkuð er útvegað. Í stað þess að úttekta innviði eftir á og elta brot kemurðu í veg fyrir að ólöglegir innviðir verði nokkru sinni til. Þessi færsla frá greiningu til forvarna er kjarnaástæða þess að IaC hefur orðið grundvallaratriði í nútíma vettvangsvinnubrögðum.

## Meginreglur

- Kjóstu yfirlýsandi skilgreiningar sem lýsa æskilegu ástandi fram yfir skipandi skriftur sem lýsa skrefum.
- Geymdu allar innviðaskilgreiningar í útgáfustýringu, rýndar eins og annan kóða.
- Líttu á innviði sem óbreytanlega: skiptu út frekar en að breyta á staðnum.
- Gerðu útvegun eins-áhrifa svo að beita sömu skilgreiningu aftur og aftur skili sömu niðurstöðu.
- Greindu og sættu rek, þegar lifandi umhverfi víkur frá yfirlýstri skilgreiningu, samfellt. Kóðinn, ekki lifandi kerfið, er uppspretta sannleikans.
- Settu innviði saman úr endurnýtanlegum, útgáfustýrðum einingum frekar en að afrita og líma.
- Kóðaðu stefnu, skipulagsreglur settar fram sem vélathugahæfur kóði, svo varnarrimlar séu sjálfvirkir, ekki ráðgefandi.
- Haltu leyndarmálum utan skilgreininga. Vísaðu í þau úr sérstökum leyndarmálastjóra.

## Ráðleggingar

### Veldu yfirlýsandi verkfæri og byggðu upp í kringum einingar

Taktu upp yfirlýsandi IaC-verkfæri, svo sem [Terraform](https://en.wikipedia.org/wiki/Terraform_(software)), Pulumi eða skýjabyggðan kost eins og CloudFormation, og staðlaðu á það um skipulagsheildina svo þú forðist sundurlaust verkfæralandslag. Lykilarkitektúrvenjan er einingabygging: smíðaðu litlar, vel skjalfestar, útgáfustýrðar einingar sem fanga algeng mynstur (löghlýðið net, hert gagnagrunn, staðlaða þjónustu). Teymi setja síðan saman umhverfi úr þessum einingum frekar en að skrifa hráar auðlindir. Þetta dreifir góðum sjálfgefnum gildum og öryggisstillingum sjálfvirkt og dregur stórlega úr tvítekningu.

### Stýrðu ástandi af ásetningi

Yfirlýsandi verkfæri rekja varpið milli kóða og raunverulegra auðlinda í ástandsskrá. Geymdu ástandið fjarlægt í sameiginlegu, dulkóðuðu, aðgangsstýrðu bakenda og notaðu læsingu svo samtímabreytingar geti ekki spillt því. Haltu aldrei ástandi á fartölvu og breyttu því aldrei í höndunum nema sem síðasta úrræði til endurheimtar. Ástand er viðkvæmt, því það getur innihaldið lýsigögn auðlinda og leyndarmál, svo verndaðu það í samræmi við það.

### Byggðu óbreytanlega innviði með gullmyndum

Frekar en að bæta keyrandi þjóna skaltu baka útgáfustýrða „gullmynd“ (forstillta, herta vél eða ílátsmynd) og setja upp ný tilvik úr henni. Þegar þú þarft breytingu eða bót skaltu smíða nýja mynd og rúlla henni út, leggja gömlu tilvikin niður. Þetta eyðir stillingareki, gerir afturköllun léttvæga og heldur hverju tilviki eins og rekjanlegu til þekktrar góðrar smíði. Sjálfvirkar myndaleiðslur ættu að innihalda öryggisherðingu og skönnun, svo reglufylgni sé innbyggð á myndastigi.

### Greindu og sættu stillingarek

Rek verður þegar lifandi umhverfi víkur frá skilgreiningu sinni, yfirleitt af því einhver gerði neyðarhandbreytingu. Keyrðu reglulega rekgreiningu sem ber raunverulegt ástand saman við yfirlýst ástand og merkir mismuninn. Líttu á rek sem galla: sættu með því að uppfæra kóðann og beita aftur, ekki með því að skilja handbreytinguna eftir. Fyrir kerfi sem þurfa viðvarandi stillingaframfylgd skaltu nota stillingastjórnunartól sem lætur hýsla samleita stöðugt að yfirlýstu ástandi sínu.

### Taktu upp GitOps og togbundna útsetningu

Í GitOps-líkaninu geymir Git-hirsla yfirlýst æskilegt ástand kerfisins og sjálfvirkur umboðsmaður sem keyrir inni í skotmarksumhverfinu togar það ástand samfellt og sættir lifandi kerfið við það. Þetta snýr hefðbundna ýtilíkaninu við. Ekkert ytra kerfi þarf varanleg auðkennisgögn til að breyta umhverfinu, því umhverfið togar eigin stillingar. GitOps gefur þér fullkomna úttektarslóð (hver breyting er innritun), auðvelda afturköllun (afturkallaðu innritunina) og sterka rekleiðréttingu (umboðsmaðurinn staðhæfir æskilegt ástand samfellt aftur). Það er sérstaklega öflugt fyrir [Kubernetes](https://en.wikipedia.org/wiki/Kubernetes) og fyrir skipulagsheildir sem vilja eina, rýnanlega uppsprettu sannleikans.

### Framfylgdu varnarrimlum með stefnu sem kóða

Settu skipulagsreglur, svo sem leyfð svæði, skyldubundna dulkóðun, nauðsynleg merki og bannaða opinbera útsetningu, fram sem vélathugahæfar stefnur með verkfæri eins og Open Policy Agent (OPA) eða stefnuvél innbyggðri í vettvang eins og Sentinel. Keyrðu þessar athuganir í leiðslunni fyrir útvegun, svo brot séu blokkuð sjálfvirkt. Stefna sem kóði breytir ásetningi öryggisteymis í keyranlega, jafnt beitta stýringu og hún skalast yfir þúsundir breytinga á hátt sem handvirk rýni gæti aldrei.

## Málamiðlanir: kostir og gallar

| Val | Kostir | Gallar | Best passun |
|---|---|---|---|
| Yfirlýsandi IaC (Terraform/Pulumi) | Endurtakanlegt, rýnanlegt, rekgreinanlegt | Lærdómsferill. Flækja ástandsstjórnunar | Næstum öll teymi í stærð |
| Skipandi skriftur | Kunnuglegar. Sveigjanlegar fyrir einstök verk | Ekki eins-áhrifa. Erfitt að úttekta og endurtaka | Þröng, bráðabirgðatilvik |
| Óbreytanlegt + gullmyndir | Ekkert rek. Léttvæg afturköllun | Yfirbygging myndasmíðaleiðslu | Flotar sem þurfa samræmi |
| Breytanleg stillingastjórnun | Fínkorna viðvarandi stjórn | Rekáhætta. Hægari samleitni | Arfleifðar- eða langlífir hýslar |
| GitOps (togbundið) | Sterk úttektarslóð. Sjálfsviðgerð | Krefst umboðsmanns í klasanum og Git-aga | Kubernetes og skýjabyggt |
| Stefna sem kóði | Sjálfvirkir, jafnir varnarrimlar | Stefnuritunarfyrirhöfn fyrirfram | Regluverkuð umhverfi |

Meginspennan er sveigjanleiki gegn stjórn. Handvirkar og skipandi nálganir finnast hraðari fyrir eina breytingu, en þær safna falinni ósamkvæmni sem verður lamandi í stærð. Yfirlýsandi, óbreytanlegir, stefnustýrðir innviðir biðja um meiri fjárfestingu fyrirfram og raunverulega menningarbreytingu, því verkfræðingar verða að hætta að gera fljótar stjórnborðsbreytingar, en þeir endurgreiða þá fjárfestingu margfalt í áreiðanleika, úttektarhæfni og getunni til að endurbyggja hvað sem er eftir þörfum.

## Spurningar til að ræða með teyminu

1. **Hver á sameiginlega einingasafnið og hvernig nær úrbót í einingu til hvers teymis sem notar hana?** Einingar borga sig aðeins ef lagfæringar og hert sjálfgefin gildi dreifast, og það krefst skýrs eignarhalds og raunverulegrar útgáfustýringar, ekki möppu sem allir afrita úr. Ákveddu hver viðheldur löghlýðna netinu og hertu gagnagrunnseiningunum, hvernig þú útgáfustýrir þeim (merkingarfræðileg útgáfustýring með breytingaskrá) og hvernig teymi toga uppfærslur án neyðaræfingar. Í stærð er þetta munurinn á því að laga ranga stillingu einu sinni og að elta hana yfir þúsund handbreyttar auðlindir. Komdu með sönnunargögn: hve mörg ólík afrit af sama mynstri eru til í dag, hve lengi öryggislagfæring er að ná til hvers umhverfis og hvort teymi festa einingaútgáfur eða láta þær fljóta. Ef mikilvæg bót nær ekki til allrar landareignarinnar á dögum er einingabygging ykkar snyrtifræðileg.

2. **Hver er rekgreiningartaktur ykkar og hvað gerist í raun þegar rek finnst?** Rek er lifandi umhverfið sem hljóðlega víkur frá yfirlýstu ástandi sínu, yfirleitt af neyðarstjórnborðsbreytingu, og að umbera það breytir kóðanum í skáldskap. Ákveddu hve oft þú berð raunverulegt ástand saman við yfirlýst ástand (næturlega er skynsamlegt sjálfgefið) og, mikilvægara, ákveddu viðbragðið: sættu með því að uppfæra kóðann og beita aftur, aldrei með því að skilja handbreytinguna eftir. Í regluverkuðu umhverfi er þetta stýringarkrafa, því úttektaraðilar þurfa að yfirlýst ástand passi við veruleikann samfellt. Komdu með núverandi tölur: hve margar auðlindir reka í viku, hve lengi þær haldast reknar og hvort einhver ber ábyrgð á að loka þeim. Líttu á hvert rek sem galla með eiganda, annars rýrnar sannleiksuppsprettutryggingin þar til enginn treystir kóðanum.

3. **Hafið þið fært ykkur yfir í GitOps og togbundna sátt, eða heldur ytra kerfi enn varanlegum auðkennisgögnum til að breyta framleiðslu?** Í togbundna líkaninu sættir umboðsmaður inni í skotmarksumhverfinu lifandi kerfið samfellt við Git, sem fjarlægir þörfina fyrir nokkurt ytra kerfi til að halda skrifaðgangi og hann staðhæfir æskilegt ástand aftur svo rek leiðréttist sjálft. Það er sterk öryggis- og úttektarstaða, þar sem hver breyting er innritun og enginn rekstraraðili þarf varanleg framleiðsluauðkennisgögn. Kostnaðurinn er raunverulegur: umboðsmaður í klasa til að reka og strangur Git-agi, svo vegðu hann gegn núverandi ýtibundinni sjálfvirkni. Komdu með lista yfir hver og hvað getur nú breytt framleiðslu beint og hvaða úttektarslóð þær breytingar skilja eftir. Fyrir Kubernetes og áhættuvarin umhverfi með mikla vissu er þessi breyting yfirleitt þess virði. Fyrir örfáar kyrrstæðar auðlindir getur hún verið of mikið.

4. **Hvernig er innviðaástand ykkar geymt, læst og aðgangsstýrt og hvað gerist daginn sem það spillist eða tapast?** Ástand er varpið milli kóðans og raunverulegra auðlinda, svo tapuð eða skemmd ástandsskrá getur skilið verkfæri eftir blint á auðlindir sem það bjó til og freistað einhvers til eyðileggjandi endurbeitingar. Fyrir stórt teymi margfaldast áhættan, því margir verkfræðingar sem beita gegn sameiginlegu ástandi þurfa fjarlægan, dulkóðaðan, læstan bakenda svo samtímakeyrslur geti ekki rústað hver annarri. Vegðu þægindi eins stórs ástands gegn sprengisvæðinu sem það skapar og íhugaðu að skipta ástandi á umhverfi eða lén svo ein mistök geti ekki fellt allt. Komdu með staðreyndirnar: hvar ástand býr í dag, hvort læsingu er framfylgt, hver getur lesið það (það getur innihaldið leyndarmál) og hvort þið hafið nokkru sinni æft endurheimt. Í fyrirtækja- og opinberu umhverfi skaltu líta á ástandsbakendann sem viðkvæma, aðgangsstýrða eign með eigin afritun, úttektarskrá og endurheimtarkeyrsluhandbók, því að tapa honum er að tapa skránni yfir það sem er til.

5. **Þegar raunveruleg neyð krefst handbreytingar, hver er heimilaða neyðarleiðin og hvernig er sú breyting felld aftur inn í kóðann?** Sérhver þroskuð IaC-venja hittir að lokum atvikið klukkan þrjú um nótt þar sem að bíða eftir leiðslu er ekki ásættanlegt og heiðarlega spurningin er ekki hvort handbreytingar gerast nokkurn tímann heldur hvernig þú heftir þær. Ákveddu fyrirfram hver má sniðganga leiðsluna, hverju þeir mega snerta, hvernig aðgerðin er skráð og frestinn til að sætta breytinguna í kóða eða afturkalla hana. Án þess samkomulags verður neyðarundantekningin hljóðlega daglegur vani og ClickOps snýr aftur bakdyramegin. Komdu með sönnunargögn: hve margar breytingar utan ferlisins gerðust síðasta ársfjórðung, hve lengi hver var ósáttuð og hvort rekgreining greip þær í raun. Fyrir regluverkaða og opinbera aðila er skjalfest neyðarleiðarferli með sjálfvirkri skráningu oft stýringarkrafa, því úttektaraðilar búast bæði við að neyðartilvik séu möguleg og að hvert skilji eftir slóð og skili kerfinu í yfirlýst ástand.

6. **Hve mikið af öryggis- og reglufylgnigrunnlínu ykkar er sett fram sem stefna sem blokkar sjálfvirkt slæma breytingu, á móti reglum sem búa í skjali og treysta á að einhver muni þær?** Varnarrimlar skrifaðir sem prósi á wiki eru brotnir reglulega, því þeir treysta á að hver verkfræðingur lesi og beiti þeim undir fresti, á meðan sömu reglur settar fram sem stefna sem kóði hafna ólöglegri breytingu áður en hún er nokkru sinni útveguð. Fyrir stóra skipulagsheild er þetta eina leiðin sem ásetningur öryggisteymis skalast yfir þúsundir breytinga án þess að verða rýniflöskuháls. Vegðu upphafskostnað við að skrifa og viðhalda stefnum gegn endurteknum kostnaði handvirkrar rýni og úrbóta eftir á og ákveddu hverjar stýringar (dulkóðun, samþykkt svæði, skyldubundin merki, engin opinber útsetning) eru nógu óumsemjanlegar til að framfylgja sem hörðum hliðum. Komdu með lista yfir núverandi grunnlínureglur þínar og merktu hverjar eru sjálfvirkar á móti ráðgefandi, auk þess hve oft hver er brotin í reynd. Í fyrirtækja- og opinberu samhengi breytir sjálfvirk stefna úttekt úr vikum af handvirkri sönnunargagnasöfnun í fyrirspurn gegn framfylgdum stýringum og hún breytir reglufylgni úr greiningu í forvörn.

## Sjónarhorn eftir geirum

**Sprotafyrirtæki.** Hraði vinnur, svo settu allan staflann í eina yfirlýsandi hirslu (Terraform er algengt sjálfgefið), geymdu ástand í stýrðum dulkóðuðum bakenda og beindu hverri breytingu gegnum sameiningarbeiðni jafnvel með þriggja manna teymi. Slepptu þungum vettvangsvélbúnaði: ekkert miðlægt einingateymi, engin stefnuvél enn, bara útgáfustýring og agi til að smella aldrei í stjórnborðinu. Það eitt gefur þér endurtakanleg umhverfi sem þú getur rifið niður til að spara peninga og endurbyggt fyrir næstu kynningu.

**Lítið fyrirtæki.** Án sérstaks vettvangssérfræðings skaltu halla þér að stýrðum þjónustum og hvaða IaC sem skýjaveitan eða seljandinn styður nú þegar frekar en að setja upp sérsmíðuð verkfæri sem þú getur ekki viðhaldið. Kjóstu að kaupa hýstan vettvang þar sem skynsamleg sjálfgefin gildi (dulkóðun, afritun, bótun) eru afgreidd fyrir þig fram yfir að smíða gullmyndaleiðslu sem þú hefur engan til að reka. Rammaðu markmiðið þröngt: komdu fáu mikilvægu auðlindunum þínum í kóða svo þú getir endurbyggt þær eftir bilun eða farandi verktaka.

**Stórfyrirtæki.** Kjarnavandinn er samræmi yfir mörg teymi, reikninga og svæði, svo fjárfestu í útgáfustýrðu sameiginlegu einingasafni, fjarlægu læstu ástandi og stefnu sem kóða framfylgt í leiðslunni. Miðlægt vettvangsteymi birtir hertar einingar og varnarrimla á meðan vöruteymi sjálfsafgreiða innan þeirra og rekgreining keyrir samfellt svo þúsundir auðlinda haldist í þekktu ástandi. Fjárhagsáætlaðu viðvarandi kostnað við að viðhalda einingum og stefnum, því gildi þeirra kemur af því að lagfæring eða hert sjálfgefið gildi dreifist alls staðar í einu.

**Hið opinbera.** Innkaupareglur, faggilding og opinber ábyrgð ýta þér í átt að óbreytanlegum innviðum, undirrituðum innritunum og GitOps-sátt inni í faggildu afgirtu svæði, svo enginn rekstraraðili hafi varanleg auðkennisgögn til að breyta framleiðslu. Kóðaðu nauðsynlega öryggisgrunnlínu inn í gullmyndir og stefnu sem kóða og láttu innritunarsöguna þjóna sem skemmdavarin, samfellt tiltæk úttektarsönnunargögn. Kjóstu opin, flytjanleg verkfæri fram yfir séreignarsnið sem fanga þig og gerðu neyðarleiðarferliina og skráningu hennar skýra svo neyðarbreytingar uppfylli enn stillingastjórnunarkröfur.

## Dæmi

**Sprotafyrirtæki.** Fimm manna sprotafyrirtæki skilgreinir allt AWS-uppsetningu sína, það er VPC, gagnagrunn og ílátaþjónustu, í einni Terraform-hirslu með ástandi geymt í dulkóðuðum S3-bakenda og læsingu gegnum DynamoDB. Hver breyting fer gegnum sameiningarbeiðni, svo jafnvel einn bakvaktarverkfræðingur sér nákvæmlega hvað mun breytast áður en hann keyrir apply. Þegar þau þurfa ferskt prófunarumhverfi fyrir stóra kynningu afrita þau litla einingu og setja það upp á mínútum og rífa það niður jafn hratt til að halda skýjareikningnum lágum.

**Stórfyrirtæki.** Alþjóðlegur smásali stýrir innviðum yfir nokkra skýjareikninga og svæði. Miðlægt vettvangsteymi birtir útgáfustýrðar Terraform-einingar fyrir löghlýðin net, gagnagrunna og þjónustuumgjörð og framfylgir OPA-stefnum sem hafna hverri auðlind sem skortir dulkóðun eða kostnaðarskiptingarmerki. Vöruteymi útvega eigin umhverfi sjálfsafgreiðslu, en hver breyting flæðir gegnum leiðsluna, þar sem stefna er athuguð sjálfvirkt. Rekgreining keyrir næturlega og opnar miða fyrir hverja handbreytingu, sem heldur þúsundum auðlinda samfellt í þekktu, löghlýðnu ástandi.

**Hið opinbera.** Varnarstofnun sem starfar í umhverfi með mikla vissu smíðar hertar gullmyndir sem fella inn nauðsynlega öryggisgrunnlínu og setur aðeins upp óbreytanleg tilvik úr þeim myndum. Allir innviðir eru yfirlýstir í Git og sáttir af GitOps-umboðsmanni inni í faggilda afgirta svæðinu, svo enginn rekstraraðili hefur varanleg auðkennisgögn til að breyta framleiðslu beint. Hver breyting er undirrituð innritun. Þetta gefur úttektaraðilum fullkomna, skemmdavarin sögu og uppfyllir samfellda vöktunar- og stillingastjórnunarkröfur án handvirkrar sönnunargagnasöfnunar.

## Viðskiptarök: hvatar, ávöxtun fjárfestingar og heildarkostnaður

Ávöxtun IaC kemur af hraða, áreiðanleika og áhættuminnkun. Umhverfi sem áður tóku vikur af miðadrifinni handvirkri útvegun má búa til á mínútum, sem losar verkfræðinga og flýtir verkefnum. Endurtakanleiki skerðir endurheimtartíma eftir bilanir stórlega, því hvert umhverfi má endurbyggja úr kóða. Sjálfvirk stefnuframfylgd dregur úr tíðni og kostnaði öryggisatvika og úttektarniðurstaðna, sem fyrir regluverkaðar skipulagsheildir getur verið umtalsvert.

Á heildareignarkostnaðarreikningnum fela upptökukostnaður í sér verkfæri, þjálfun, að smíða eininga- og stefnusafn og agann til að hætta handbreytingum. Kostnaður þess að taka ekki upp er brattari og safnast með tímanum: snjókornainnviðir sem enginn getur endurbyggt, hæg og villuhætt útvegun, öryggisrangstillingar sem leiða til brota og úttektir sem éta vikur af handvirkri vinnu. Fyrir forystu skaltu ramma IaC sem að breyta innviðum úr óstýrðri skuld í stýrða, endurtakanlega eign og sem búnaðinn sem gerir öryggi og reglufylgni sjálfvirk frekar en metnaðarfull.

## Andmynstur og gildrur

- **ClickOps í framleiðslu.** Að gera breytingar í höndunum í stjórnborðinu tryggir rek og eyðileggur endurtakanleika.
- **Leyndarmál í kóða.** Að harðkóða auðkennisgögn í skilgreiningarskrár lekur þeim inn í útgáfusögu og ástand.
- **Risavaxnar, óeiningabyggðar skilgreiningar.** Ein risastór stilling sem enginn þorir að breyta verður jafn brothætt og handvirka uppsetningin sem hún kom í staðinn fyrir.
- **Óstýrt ástand.** Staðbundnar eða ólæstar ástandsskrár leiða til spillingar og týndra innviða.
- **Rek umborið.** Að skilja handbreytingar eftir rýrir sannleiksuppsprettutrygginguna þar til kóðinn er skáldskapur.
- **Stefna sem skjölun.** Reglur sem búa á wiki í stað sjálfvirkrar athugunar eru reglulega brotnar.
- **Afrita-og-líma útbreiðsla.** Að tvítaka stillingar yfir teymi þýðir að lagfæringar og úrbætur dreifast aldrei.

## Þroskalíkan

**Stig 1: Upphaf.** Innviðir eru útvegaðir handvirkt gegnum stjórnborðið og ad hoc skriftur. Umhverfi eru ósamræmd, óskjalfest og ekki hægt að endurtaka áreiðanlega og endurheimt eftir bilun er hæg og óviss.

**Stig 2: Þróun.** Sumir innviðir eru kóðaðir, en vinnubrögð eru ólík eftir teymum. Ástandsstjórnun er ósamræmd, rek er algengt, leyndarmál leka stundum inn í skilgreiningar og stefnu er framfylgt, ef yfirleitt, gegnum handvirka rýni.

**Stig 3: Stöðlun.** Yfirlýsandi IaC er skjalfesti staðallinn um skipulagsheildina, smíðað úr sameiginlegum útgáfustýrðum einingum með stýrðu, fjarlægu, læstu ástandi. Stefna sem kóði framfylgir varnarrimlum í leiðslunni, leyndarmálum er vísað í úr sérstökum stjóra og rekgreining keyrir á reglulegum takti.

**Stig 4: Stjórnun.** Venjan er mæld gegn grunnlínum. Þú rekur rekhlutfall og meðaltíma til sáttar, upptöku einingaútgáfa yfir teymi, stefnubrot blokkuð á móti sloppin, útvegunarleiðtíma og hlutfall auðlinda sem eru í raun undir kóða. Þessir mælikvarðar hliða breytingar og stýra hvar þú fjárfestir, svo ákvarðanir hvíli á sönnunargögnum frekar en sögusögnum.

**Stig 5: Samhæfing.** Innviðir eru óbreytanlegir og GitOps-drifnir, sjálfsviðgerðir gegn reki, með reglufylgnisönnunargögn framleidd sjálfvirkt. Einingar- og stefnusafnið batnar stöðugt af raunverulegri notkun og atvikum og innviðavenjur eru samþættar öryggi, kostnaði og afhendingarskipulagningu svo öll landareignin aðlagist eftir því sem kröfur breytast.

## Hugmyndir til umræðu

- Hvar ætti línan að liggja milli miðlægt stýrðra eininga og sjálfræðis teyma til að skilgreina sérsniðna innviði?
- Hvernig meðhöndlið þið raunverulegu neyðarbreytinguna sem verður að sniðganga leiðsluna, án þess að gera ClickOps eðlilegt?
- Hver er rétta aðferðin til að stýra og tryggja ástand yfir marga reikninga og teymi?
- Hvenær er breytanleg stillingastjórnun enn réttlætanleg á móti fullkomlega óbreytanlegum innviðum?
- Hvernig haldið þið stefnu-sem-kóða safninu í takt við þróandi öryggis- og regluverkskröfur?
- Hvernig lítur raunhæf flutningsleið út fyrir arfleifðarinnviði sem eru eldri en IaC?

## Helstu atriði

- Skilgreindu innviði yfirlýsandi, útgáfustýrðu þá og líttu á þá sem rýnanlegan, endurtakanlegan kóða.
- Byggðu úr litlum, útgáfustýrðum einingum til að dreifa góðum sjálfgefnum gildum og eyða tvítekningu.
- Kjóstu óbreytanlega innviði og gullmyndir til að afnema rek og einfalda afturköllun.
- Stýrðu ástandi af ásetningi og haltu leyndarmálum utan skilgreininga.
- Taktu upp GitOps fyrir sterka úttektarslóð og sjálfsviðgerðarsátt.
- Framfylgdu varnarrimlum með stefnu sem kóða svo reglufylgni sé forðuð til tilveru, ekki úttektuð eftir á.

## Heimildir og frekari lestur

- Kief Morris, *Infrastructure as Code: Dynamic Systems for the Cloud Age*.
- Yevgeniy Brikman, *Terraform: Up & Running*.
- Betsy Beyer, Chris Jones, Jennifer Petoff, and Niall Richard Murphy (eds.), *Site Reliability Engineering*.
- Gene Kim, Jez Humble, Patrick Debois, and John Willis, *The DevOps Handbook*.
- Weaveworks, "GitOps" foundational writings (Alexis Richardson et al.).
- Open Policy Agent documentation and the Rego policy language.
- NIST Special Publication 800-53, security and privacy controls (configuration management family).
