# 8.1 Samfelld samþætting og afhending

## Yfirlit og tilgangur

[Samfelld samþætting](https://en.wikipedia.org/wiki/Continuous_integration) og [samfelld afhending](https://en.wikipedia.org/wiki/Continuous_delivery) (CI/CD) eru bandvefurinn milli þess að skrifa kóða og að setja hann örugglega fyrir framan notendur. Samfelld samþætting þýðir að hver breyting er sameinuð oft í sameiginlega meginlínu og síðan smíðuð og prófuð sjálfvirkt, svo samþættingarvandamál komi upp innan mínútna í stað við lok langs útgáfuhrings. Samfelld afhending þýðir að hver breyting sem stenst leiðsluna er höfð í útsetjanlegu ástandi, svo útgáfa í framleiðslu verði viðskiptaákvörðun frekar en verkfræðióðagot. [Samfelld útsetning](https://en.wikipedia.org/wiki/Continuous_deployment) fer einu skrefi lengra og gefur út hverja breytingu sem stenst sjálfvirkt, án mannlegs hliðs.

Fyrir stór teymi skipta þessi greinarmunur gríðarlegu máli. Þegar hundruð verkfræðinga innrita í skarastandi kerfi vex kostnaður handvirkrar samþættingar og handvirkra prófana ólínulega. Sameiginleg, sjálfvirk leiðsla er eina hagnýta leiðin til að gefa mörgum framlagshöfum hraða, traustverða endurgjöf og að koma í veg fyrir að breyting eins teymis brjóti hljóðlega breytingu annars. Leiðslan verður eina uppspretta sannleikans um hvort hugbúnaðurinn er heilbrigður og hún framfylgir samræmi sem engin skjölun eða góður ásetningur getur tryggt í stærð.

Fyrirtækja- og opinbert umhverfi bætir við einni vídd í viðbót: úttektarhæfni og breytingastjórn. Eftirlitsaðilar, öryggisfulltrúar og úttektaraðilar þurfa sönnunargögn um að breytingar hafi verið rýndar, prófaðar og samþykktar og að gripurinn sem keyrir í framleiðslu sé nákvæmlega sá sem var smíðaður og staðfestur. Vel hönnuð CI/CD-leiðsla breytir þessum reglufylgniskyldum úr skjalavinnubyrði í sjálfvirka aukaafurð venjulegs verkfræðivinnuflæðis. Vel gert verður afhending hraðari og öruggari í senn, sem er útkoman sem skiptir forystu mestu.

*Sjá einnig:* kafla 8.4 (vettvangsverkfræði og þróunarupplifun), kafla 8.5 (prófana- og ferlasjálfvirkni) og kafla 7.4 (vörugreining og tilraunir) fyrir [eiginleikarofa](https://en.wikipedia.org/wiki/Feature_toggle) (keyrslurofa sem afhjúpa virkni fyrir notendum án endurútsetningar) og tilraunavinnubrögðin sem stigvaxandi afhending (að gefa breytingu út smám saman og vakta sjálfvirkt heilsumælikvarða hennar) gerir mögulega.

## Meginreglur

- Samþættu litlar breytingar oft. Langlífar greinar eru óvinur samfelldrar samþættingar.
- Smíðaðu gripinn einu sinni og efldu sama grip gegnum öll umhverfi.
- Gerðu leiðsluna að úrskurðarhliðinu: ef hún er græn er breytingin afhendanleg og ef hún er rauð stoppar vinna þar til það er lagað.
- Fínstilltu miskunnarlaust fyrir hraða endurgjöf svo forritarar haldist í flæði og gallar séu gripnir meðan samhengi er ferskt.
- Sjálfvirknivæddu allt sem er endurtekið, þar með talin próf, öryggisskönnun, útvegun og útsetningu.
- Líttu á leiðsluskilgreiningar sem útgáfustýrðan kóða undir rýni, ekki sem smellanlega stjórnborðsstillingu.
- Hannaðu fyrir örugga, afturkræfa útgáfu svo hægt sé að afturkalla hverja útsetningu fljótt.
- Aðgreindu útsetningu (að setja upp kóðann) frá útgáfu (að afhjúpa hann notendum) með eiginleikarofum.

## Ráðleggingar

### Hannaðu leiðsluna sem röð gæðahliða

Byggðu leiðsluna upp í stig sem þróast frá ódýru og hröðu til dýrs og ítarlegs: þýðing og einingapróf fyrst, síðan samþættingarpróf, öryggis- og leyfisskönnun og loks útsetning í prófunar- og framleiðsluumhverfi. Hvert stig er hlið sem breyting verður að standast. Raðaðu hliðunum svo hröðustu, líklegustu-til-að-bila athuganirnar keyri fyrst, sem gefur forriturum endurgjöf á skemmsta mögulega tíma. Haltu endurgjafarlykkju innritunarstigsins undir tíu mínútum hvar sem þú getur. Umfram það skipta forritarar um samhengi og framleiðni fellur.

### Smíðaðu einu sinni, efldu alls staðar

Framleiddu einn óbreytanlegan grip á smíðastiginu og efldu nákvæmlega þann grip gegnum prófun, millisvið og framleiðslu. Smíðaðu aldrei aftur fyrir hvert umhverfi, því endursmíði getur hljóðlega komið með mun. Stillingar sem eru ólíkar eftir umhverfi ætti að sprauta inn við útsetningu, ekki baka inn í aðskildar smíðar. Þetta vinnubragð er líka það sem leyfir þér að segja úttektaraðila, með vissu, að tvíundaskráin í framleiðslu sé sú sem stóðst hvert hlið.

### Gerðu leiðsluna að framfylgdarpunkti fyrir stefnu

Kóðaðu nauðsynlegar athuganir (samþykki kóðarýni, þröskulda prófaþekju, niðurstöður öryggisskönnunar, undirritaðar innritanir) beint inn í leiðsluna og greinarverndarreglur. Handvirk stefna sem býr á wiki er reglulega sniðgengin undir fresti. Stefna kóðuð í leiðslunni er beitt jafnt og sjálfvirkt á hverja breytingu.

### Haltu meginlínunni útsetjanlegri alltaf

Notaðu stofnlínuþróun (trunk-based development), sem samþættir alla vinnu í eina sameiginlega grein með fáum eða engum langlífum greinum, eða notaðu skammlífar eiginleikagreinar, og treystu á eiginleikarofa til að fela ókláraða vinnu frekar en langlífar greinar. Þetta heldur samrunaárekstrum litlum og heldur meginlínunni alltaf í útsetjanlegu ástandi, sem er forsenda raunverulegrar samfelldrar afhendingar.

### Veldu útsetningarstefnur af ásetningi

Láttu útsetningarstefnuna passa áhættu og sprengisvæði þjónustunnar:

- **Rúllandi** útsetningar skipta út tilvikum smám saman og eru skynsamlegt sjálfgefið fyrir ástandslausar þjónustur.
- **[Blár-grænn](https://en.wikipedia.org/wiki/Blue-green_deployment)** heldur tveimur eins umhverfum og skiptir umferð allri í einu, sem gefur samstundis afturköllunarleið.
- **Kanarí**-útgáfur beina litlu hlutfalli umferðar að nýju útgáfunni, fylgjast með heilsumælikvörðum og víkka aðeins ef merkin eru góð.
- **Eiginleikarofar** aðgreina útgáfu frá útsetningu og leyfa þér að virkja virkni fyrir tiltekna notendur eða hópa án endurútsetningar.

### Taktu upp stigvaxandi afhendingu með sjálfvirkri afturköllun

Stigvaxandi afhending sameinar kanarí-útgáfur við sjálfvirka greiningu mælikvarða eins og villuhlutfalls, töf og mettunar. Skilgreindu hlutlæg heilsuviðmið fyrirfram og láttu kerfið síðan efla eða afturkalla sjálfvirkt út frá þeim merkjum. Sjálfvirk afturköllun fjarlægir mannlega hik sem breytir litlu atviki í stórt.

### Útvegaðu útgáfustjórnun og breytingastjórn fyrir regluverkað umhverfi

Í regluverkuðu umhverfi skaltu halda léttri en raunverulegri breytingastjórnunarskrá. Fangaðu sjálfvirkt hver samþykkti hverja breytingu, hvaða próf keyrðu og hvaða grip var settur upp. Notaðu breytingaráðgjafarferli fyrir sannarlega áhættumiklar breytingar, en taktu þau frá fyrir þau tilvik. Að beina hverri venjulegri breytingu gegnum vikulega nefnd eyðileggur gildi sjálfvirkni. Stefndu frekar að stöðluðum, fyrirfram samþykktum breytingategundum sem flæða gegnum leiðsluna án hátíðleika.

## Málamiðlanir: kostir og gallar

| Nálgun | Kostir | Gallar | Best passun |
|---|---|---|---|
| Samfelld afhending (handvirkt útgáfuhlið) | Viðskiptin stýra tímasetningu. Sterkt fyrir regluverkaða útgáfuglugga | Krefst aga til að halda meginlínu afhendanlegri | Fyrirtæki með breytingaglugga |
| Samfelld útsetning (fullsjálfvirk) | Hröðust endurgjöf. Minnstu lotur | Krefst þroskaðra prófa og vöktunar | Hátraust, hátíðni teymi |
| Blár-grænn | Samstundis afturköllun. Einfalt hugmyndalíkan | Tvöfaldar umhverfiskostnað við skiptin | Mikilvægar þjónustur sem þurfa hraða afturköllun |
| Kanarí + stigvaxandi afhending | Takmarkar sprengisvæði. Gagnadrifið | Flókið að smíða. Þarfnast góðra mælikvarða | Stór notendasnúin kerfi |
| Eiginleikarofar | Aðgreinir útsetningu frá útgáfu | Rofaskuld ef ekki hreinsað | Teymi sem afhenda ókláraða vinnu örugglega |

Kjarnamálamiðlunin er hraði gegn stjórn, en það er oft fölsk tvískipting. Þroskuð sjálfvirkni skilar hvoru tveggja: útgáfur eru hraðari því þær eru minni og öruggari því hver er staðfest og afturkræf. Raunverulegi kostnaðurinn er fjárfestingin fyrirfram í prófaþekju, vöktun og leiðsluverkfræði, auk viðvarandi agans til að halda þeim heilbrigðum. Skipulagsheildir sem spara á þeirri fjárfestingu fá hraðann án öryggisins, sem er verra en hægt handvirkt ferli.

## Spurningar til að ræða með teyminu

1. **Hvert er markmið ykkar fyrir endurgjafartíma innritunarstigs og hvað er skorið þegar safnið vex fram úr tíu mínútum?** Hægt innritunarstig drepur hljóðlega samfellda samþættingu, því forritarar hætta að bíða eftir grænu og byrja að lota breytingar. Ákveddu töluna núna (þessi kafli mælir með undir tíu mínútum) og ákveddu búnaðinn til að halda henni: samhliða vinnuþjóna, stranga prófapýramída og að færa hæg samþættingarpróf á síðara stig. Í fyrirtækjastærð er þetta vettvangsákvörðun, því hundruð verkfræðinga deila sömu leiðslu og hver viðbótar mínúta margfaldast yfir hverja innritun. Komdu með raunveruleg gögn á fundinn: núverandi p50 og p95 leiðslulengd, tíu hægustu prófin og hve oft fólk endurkeyrir frekar en bíður. Ef þú getur ekki sagt markmiðið og varið það með tölum rekur leiðsla þín í átt að lotuvinnslu í CI-búningi.

2. **Hvaða útsetningarstefnu notar hver þjónusta og hver ber ábyrgð á því vali?** Rúllandi, blár-grænn og kanarí eru ekki skiptanleg: þau skipta kostnaði, afturköllunarhraða og flækju á ólíkan hátt og rétta valið veltur á sprengisvæði þjónustunnar. Blár-grænn kaupir samstundis afturköllun á verði tvöfalds umhverfis við skiptin, sem er þess virði fyrir greiðslukerfi og sóun fyrir innra mælaborð. Kanarí takmarkar útsetningu en krefst góðra heilsumælikvarða og meiri leiðsluverkfræði. Fyrir stóra eða regluverkaða landareign skilar það að láta hvert teymi velja eftir vana ósamræmi sem kemur upp í atviki, svo komið ykkur saman um sjálfgefin gildi á þjónustuþrep og skráið ákvörðunina. Komdu með þjónustuskrá þína og merktu hverja þjónustu með stefnu sinni, afturköllunarleið og þeim sem á það val.

3. **Hvernig sannið þið að gripurinn í framleiðslu sé nákvæmlega sá sem stóðst hvert hlið?** Að smíða einu sinni og efla sama grip er allur leikurinn fyrir úttektarhæfni og það brotnar um leið og einhver endursmíðar fyrir hvert umhverfi eða bætir keyrandi kassa. Í fyrirtækja- og opinberu umhverfi mun úttektaraðili biðja þig að rekja keyrandi tvíundaskrá til innritunar sinnar, rýni og samþykkta og þú vilt að það svar taki sekúndur, ekki viku. Ákveddu hvernig þú framfylgir því: óbreytanlegir gripir, undirritaðar myndir, undirskriftarstaðfesting við útsetningu og stillingar sprautað við útsetningu frekar en bakað inn í aðskildar smíðar. Komdu með núverandi göt á borðið, svo sem hvert stig sem endursmíðar, hverja handvirka bráðabótaleið og hvar stillingar kvíslast gripinn. Svarið ræður því hvort reglufylgnisönnunargögn ykkar eru aukaafurð leiðslunnar eða handvirkt óðagot fyrir hverja úttekt.

4. **Þegar meginlínan verður rauð, hvað stöðvar í raun og hvernig meðhöndlið þið óstöðug próf?** Leiðsla er aðeins úrskurðarhlið ef rauð smíði stöðvar raunverulega vinnu, samt umbera margar skipulagsheildir hljóðlega bilaða meginlínu og bakslag slitróttra bilana, sem kennir forriturum að endurkeyra þar til grænt og að afhenda ofan á bilanir. Fyrir stórt teymi safnast þetta rotnun, því óstöðugt próf eins teymis sem er hunsað verður afsökun allra til að sniðganga hliðið og traust á leiðslunni er langtum ódýrara að halda en að endurbyggja. Vegðu kraftana sem togast á: ströng stöðva-línuna regla ver gæði en getur blokkað hundruð verkfræðinga á einni slæmri innritun, á meðan væg stefna varðveitir afköst og rýrir hliðið. Komdu með sönnunargögn í umræðuna: núverandi rauðan tíma meginlínu, fjölda einangraðra eða óstöðugra prófa, endurkeyrsluhlutfall og hve oft breytingar sameinast yfir bilandi athugun. Í fyrirtækja- og opinberu umhverfi skaltu nefna hver á úrlausn óstöðugra prófa og hver hefur vald til að frysta sameiningar, því hlið sem enginn ber ábyrgð á að framfylgja er hlið sem úttektaraðilar munu finna að hefur verið reglulega hnekkt.

5. **Hver er lífsferill eiginleikarofa ykkar og hver er skyldugur til að leggja þá niður?** Rofar eru það sem leyfir þér að aðgreina útsetningu frá útgáfu og fela ókláraða vinnu, en hver rofi er grein í kóðanum þínum sem hreinsast aldrei af sjálfu sér og óstýrðir rofar safnast í skilyrðisflækju sem enginn þorir að snerta. Í stórri landareign er þessi skuld hættuleg, því úreltur rofi getur hljóðlega hliðað öryggislagfæringu eða snúið óprófuðum kóðaleiðum inn í framleiðslu og sá sem bjó hann til er oft farinn annað. Vegðu spennuna: rofar keyptu þér örugga, stigvaxandi afhendingu, svo markmiðið er ekki færri rofar heldur agaður lífsferill með eiganda, fyrningarvæntingu og verkfæri sem sýnir úrelta. Komdu með núverandi skrá á fundinn: hve margir rofar eru lifandi, hve gamall sá elsti er, hverjir hafa engan eiganda og hvort einhver langlífur rofi virkar nú sem varanleg stilling sem á heima annars staðar. Fyrir regluverkað umhverfi skaltu bæta við hver getur breytt rofa í framleiðslu og hvort sú breyting er skráð með sama aga og útsetning, því rofabreyting er útgáfa jafnvel þegar leiðslan keyrir aldrei.

6. **Hvar liggja mörkin milli samfelldrar afhendingar með mannlegu hliði og fullrar samfelldrar útsetningar og hver setur afturköllunarþröskulda?** Samfelld afhending heldur manni við stjórn á útgáfutímasetningu, sem hentar lögbundnum breytingagluggum og kerfum með stórt sprengisvæði, á meðan samfelld útsetning afhendir hverja breytingu sem stenst sjálfvirkt og krefst þroskaðra prófa, vöktunar og sjálfvirkrar afturköllunar til að vera örugg. Fyrir stóra eða regluverkaða skipulagsheild er svarið sjaldan einsleitt: markaðsvefurinn ykkar getur verið útsettur samfellt á meðan greiðslukjarninn heldur skjalfestu mannlegu hliði og að draga þá línu á þjónustuþrep kemur í veg fyrir bæði óþarfa núning og ógætilega sjálfvirkni. Sjónarmiðin sem togast á eru hraði og lotustærð gegn stjórn og úttektarhæfni, auk verkfræðikostnaðar heilsumælikvarðanna sem sjálfvirk afturköllun krefst. Komdu með sönnunargögnin: bilunarhlutfall breytinga á þjónustu, meðaltíma til endurheimtar, núverandi útgáfutakt og hlutlægu merkin (villuhlutfall, töf, mettun) sem þú myndir treysta til að efla eða afturkalla án manns. Í opinberu og fyrirtækjaumhverfi skaltu tengja hvert þrep við hver á afturköllunarþröskuldana og hver skrifar undir hverja færslu frá hliðaðri útgáfu til fullrar sjálfvirkni, svo ákvörðunin sé yfirveguð frekar en rekin.

## Sjónarhorn eftir geirum

**Sprotafyrirtæki.** Hallaðu þér að stýrðri CI/CD frá fyrsta degi: hýstur keyrari, ein leiðsla, ein óbreytanleg mynd og sjálfvirk útsetning í prófunarumhverfi við sameiningu. Smíðaðu ekki leiðsluinnviði sem þú þarft síðan að viðhalda. Eiginleikarofar leyfa tveimur eða þremur verkfræðingum að sameina hálfkláraða vinnu örugglega og afhenda nokkrum sinnum á dag og eins smells framleiðsluútsetning auk hraðs rofa-af er öll breytingastjórnin sem þú þarft þar til stærð krefst meira.

**Lítið fyrirtæki.** Án sérstaks vettvangs- eða útgáfuverkfræðings skaltu kjósa leiðsluna sem frumkóðahýsillinn gefur þér (innbyggðar aðgerðir eða sambærilegt) og sjálfgefna útsetningarstefnu hennar fram yfir allt sérsniðið. Rammaðu kaup-gegn-smíði valið af heiðarleika: stýrð leiðsla og hýsingarvettvangur með innbyggðri afturköllun kostar minna en verkfræðingatímarnir sem sérsmíðuð uppsetning eyðir. Haltu nauðsynjunum, sem eru smíða einu sinni, efla sama grip og auðveld afturköllun, og slepptu stigvaxandi afhendingarvélbúnaðinum þar til magn réttlætir hann.

**Stórfyrirtæki.** Kjarnavandinn er samræmi yfir mörg teymi: staðlaðu sameiginlegt leiðslusniðmát sem framfylgir rýni, skönnun, undirrituðum óbreytanlegum gripum og útsetningarstefnum á þjónustuþrep, svo gæði séu ekki ólík eftir teymum. Líttu á leiðsluskilgreiningar sem rýndan kóða, fangaðu breytingastjórnarsönnunargögn sjálfvirkt og stýrðu eiginleikarofum og afturköllunarþröskuldum sem stýrðum eignum frekar en einkavana hvers teymis. Ávinningurinn er hraðari afhending og úttektarsönnunargögn framleidd sem aukaafurð í stað ársfjórðungslegs óðagots.

**Hið opinbera.** Innkaupareglur, lögbundnir breytingagluggar og opinber ábyrgð móta leiðsluna. Kjóstu samfellda afhendingu með skjalfestu mannlegu útgáfuhliði fram yfir fulla sjálfvirkni fyrir afleidd kerfi, flokkaðu venjulega vinnu sem fyrirfram samþykktar staðlaðar breytingar og haltu samstundis afturköllunarleið (blár-grænn eða sjálfvirkt kanarí) fyrir þjónustur sem borgarar reiða sig á í þröngum árlegum gluggum. Tryggðu að leiðslan skrái hver samþykkti hverja breytingu, hvaða próf keyrðu og hvaða gripur var settur upp, svo gagnsæis- og úttektarskyldum sé mætt af venjulegu vinnuflæði frekar en handvirkri pappírsvinnu.

## Dæmi

**Sprotafyrirtæki.** Fjögurra manna SaaS-sprotafyrirtæki setur upp eina GitHub Actions leiðslu sem keyrir einingapróf, smíðar eina Docker-mynd og setur sömu mynd upp í prófunarumhverfi sjálfvirkt við hverja sameiningu í main. Framleiðsluútsetning er einn smellur og stofnendurnir styðjast við eiginleikarofa svo þeir geti sameinað hálfklárað verk á bak við rofa í stað þess að halda grein lifandi vikum saman. Þegar slæm útgáfa slæðist í gegn slökkva þeir á rofanum á sekúndum og laga rólega, sem heldur örlitla teyminu afhendandi nokkrum sinnum á dag án sérstaks rekstrarmanns.

**Stórfyrirtæki.** Alþjóðlegur banki sameinar tugi teymissértækra Jenkins-verka í staðlað leiðslusniðmát sem hvert vöruteymi erfir. Sniðmátið framfylgir stöðugri greiningu, ósjálfstæðaskönnun og undirrituðum, óbreytanlegum grip og setur upp með kanarí og sjálfvirkri afturköllun bundinni við villuhlutfalls- og töfarþröskulda. Því sami gripur er efldur frá prófun til framleiðslu og hvert hlið er skráð geta úttektaraðilar bankans rakið hverja framleiðslutvíundaskrá til innritunar, rýni og samþykktar á sekúndum, sem kemur í stað ársfjórðungslegrar handvirkrar sönnunargagnasöfnunar.

**Hið opinbera.** Landsbundið skattyfirvald sem nútímavæðir framtalskerfi tekur upp samfellda afhendingu með skýru mannlegu útgáfuhliði, svo það geti virt lögbundna breytingaglugga á framtalstímabilinu. Venjulegar breytingar eru flokkaðar sem staðlaðar fyrirfram samþykktar breytingar sem flæða sjálfvirkt í prófunarumhverfi. Framleiðsluútgáfa krefst eins skjalfests samþykkis sem leiðslan skráir. Blár-grænn útsetning gefur stofnuninni samstundis afturköllunarleið ef galli nær til framleiðslu, sem er mikilvægt þegar milljónir borgara reiða sig á þjónustuna í þröngum árlegum glugga.

## Viðskiptarök: hvatar, ávöxtun fjárfestingar og heildarkostnaður

Ávöxtun CI/CD-fjárfestingar birtist sem styttri leiðtími breytinga, lægra bilunarhlutfall breytinga og hraðari endurheimt þegar atvik verða: mælikvarðarnir sem rannsóknir tengja stöðugt bæði við afhendingarárangur og skipulagsárangur. Hraðari, minni útgáfur skera samræmingarkostnaðinn sem étur verkfræðigetu í stærð og sjálfvirk staðfesting skerðir dýra, móralsdrepandi slökkvivinnu við framleiðslugalla.

Heildareignarkostnaður vegur upptökukostnað gegn kostnaði þess að taka ekki upp. Upptökukostnaður felur í sér að smíða og viðhalda leiðslum, auka prófaþekju og fjárfesta í vöktun og vettvangsstarfsfólki. Kostnaður þess að taka ekki upp er stærri en minna sýnilegur: hægar handvirkar útgáfur, samþættingarsársauki, framleiðsluatvik sem skaða orðspor og, í regluverkuðu umhverfi, misheppnaðar úttektir og úrbætur. Fyrir forystu eru rökin best sett fram sem áhættuminnkun og afkastageta. Sjálfvirkni breytir knöppum tíma eldri verkfræðinga úr endurtekinni útgáfuleiðindavinnu í vinnu við vöru, á sama tíma og hún gerir rof sjaldgæfari og styttri.

## Andmynstur og gildrur

- **Einstakar leiðslur.** Hvert teymi handsmíðar einstaka leiðslu, svo úrbætur og lagfæringar er ekki hægt að deila og gæði eru mjög ólík.
- **Endursmíði á umhverfi.** Að endursmíða fyrir hvert stig brýtur „smíða einu sinni“ trygginguna og lætur lúmsk mun ná til framleiðslu.
- **Hunsaðar rauðar smíðar.** Að umbera ítrekað bilaða meginlínu eyðileggur traust á leiðslunni og gerir eðlilegt að afhenda ofan á bilanir.
- **Óstöðug próf látin óhreyfð.** Slitróttar bilanir kenna forriturum að endurkeyra þar til grænt, sem gerir hliðið marklaust.
- **Handvirk samþykktarleikhús.** Breytingaráðgjafarnefnd sem stimplar allt bætir við töf án þess að bæta við öryggi.
- **Rofaskuld.** Eiginleikarofar sem eru aldrei fjarlægðir safnast í óviðhaldanlega skilyrðisflækju.
- **Útsetning jafngildir útgáfu.** Að tengja þetta tvennt þýðir að hver notendasnúin breyting krefst áhættusamrar endurútsetningar.

## Þroskalíkan

**Stig 1: Upphaf.** Smíðar og útsetningar eru að mestu handvirkar, ad hoc og viðbragðsdrifnar. Samþætting gerist seint, útgáfur eru sjaldgæfar og streituvaldandi, afturköllun þýðir að endurútsetja gamla útgáfu í höndunum og engin sameiginleg hugmynd er til um leiðsluhlið.

**Stig 2: Þróun.** Sjálfvirkar smíðar og einingapróf keyra á hverri innritun, en vinnubrögð eru ólík eftir teymum. Útsetningar eru skriftaðar en samt ræstar og vaktaðar í höndunum, sum umhverfi eru samræmd og gripir kunna enn að vera endursmíðaðir á hverju stigi. Þar sem leiðsla er til er hún oft einstök sem ekki er hægt að deila.

**Stig 3: Stöðlun.** Skjalfest, stöðluð leiðslusniðmát er framfylgt yfir teymi. Það eflir einn óbreytanlegan grip gegnum öll umhverfi, beitir sjálfvirkum gæða- og öryggishliðum, kóðar nauðsynlegar athuganir eins og samþykki rýni og skönnunarniðurstöður og fangar breytingaskrár sjálfvirkt. Útsetningarstefnur eins og kanarí eða blár-grænn eru valdar af ásetningi á þjónustuþrep.

**Stig 4: Stjórnun.** Afhending er mæld og stýrð gegn grunnlínum. Skipulagsheildin rekur leiðtíma breytinga, útsetningartíðni, bilunarhlutfall breytinga og meðaltíma til endurheimtar, ásamt p50 og p95 leiðslulengd, hlutföllum óstöðugra prófa og endurkeyrslna og aldri eiginleikarofa. Afturköllunarþröskuldar eru settir út frá mældum villuhlutfalls-, töfar- og mettunargögnum, hlið eru framfylgd á sönnunargögnum frekar en vana og hver mælikvarði hefur eiganda sem bregst við þegar hann víkur frá markmiði.

**Stig 5: Samhæfing.** Afhending batnar stöðugt og er samþætt um skipulagsheildina. Stigvaxandi afhending með sjálfvirkri, mælikvarðadrifinni afturköllun er normið, útgáfa er aðgreind frá útsetningu með vel stýrðum rofum og reglufylgnisönnunargögn eru framleidd sjálfvirkt sem aukaafurð. Leiðslan aðlagast eftir því sem landareignin breytist og afhendingarmælikvarðar nærir viðskipta- og áhættuskipulagningu svo fjárfesting flæði til umbóta með mestan áhrifamátt.

## Hugmyndir til umræðu

- Hvar eru réttu mörkin milli samfelldrar afhendingar með mannlegu hliði og fullrar samfelldrar útsetningar fyrir mikilvægustu kerfin ykkar?
- Hvernig haldið þið skyldubundnu breytingastjórnunarferli marktæku án þess að breyta því í stimpilleikhús?
- Hvaða hlutlægu heilsumælikvarðar ættu að stýra sjálfvirkri afturköllun og hver á þröskulda þeirra?
- Hvernig ættu vettvangsteymi að jafnvægisstilla staðlað leiðslusniðmát gegn lögmætum þörfum teyma með óvenjulegar kröfur?
- Hver er stefna ykkar og verkfæri til að leggja niður eiginleikarofa áður en þeir verða skuld?
- Hvernig mælið þið hvort hraðari afhending bæti í raun viðskiptaárangur frekar en að afhenda bara meira?

## Helstu atriði

- CI, CD og samfelld útsetning eru aðgreind. Veldu sjálfvirknistigið sem passar áhættuþoli þínu og þroska.
- Smíðaðu gripinn einu sinni og efldu sama grip gegnum öll umhverfi.
- Hannaðu leiðsluna sem raðaða gæðahlið fínstillt fyrir hraða endurgjöf og líttu á hana sem úrskurðarvaldið um útsetningu.
- Veldu útsetningarstefnur af ásetningi og taktu upp stigvaxandi afhendingu með sjálfvirkri afturköllun til að takmarka sprengisvæði.
- Aðgreindu útgáfu frá útsetningu með eiginleikarofum og stýrðu rofaskuld.
- Í regluverkuðu umhverfi skaltu fanga breytingastjórnarsönnunargögn sjálfvirkt frekar en gegnum handvirka pappírsvinnu.

## Heimildir og frekari lestur

- Jez Humble and David Farley, *Continuous Delivery: Reliable Software Releases through Build, Test, and Deployment Automation*.
- Nicole Forsgren, Jez Humble, and Gene Kim, *Accelerate: The Science of Lean Software and DevOps*.
- Gene Kim, Jez Humble, Patrick Debois, and John Willis, *The DevOps Handbook*.
- Gene Kim, Kevin Behr, and George Spafford, *The Phoenix Project*.
- Betsy Beyer, Chris Jones, Jennifer Petoff, and Niall Richard Murphy (eds.), *Site Reliability Engineering*.
- Pete Hodgson, "Feature Toggles (Feature Flags)" (essay).
- ITIL (Information Technology Infrastructure Library), change management guidance.
