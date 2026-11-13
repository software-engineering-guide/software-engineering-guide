# 2.3 Forritaskil og viðmótshönnun

## Yfirlit og tilgangur

[API](https://en.wikipedia.org/wiki/API) (forritaskil, application programming interface) er samningurinn sem einn hluti hugbúnaðar býður getu til annars. Þar mætast teymi, kerfi og skipulagsheildir, og það er varanlegasti og dýrasti hluturinn til að fá rangan. Þú getur endurbyggt innra fallaundirskrift að vild. Útgefin API eru öðruvísi: það er loforð til neytenda sem þú hittir kannski aldrei og að brjóta það brýtur þá. Þegar skipulagsheildir skipta [einsteinum](https://en.wikipedia.org/wiki/Monolithic_application) í þjónustur og opna getu fyrir samstarfsaðila og almenning verður API aðalvöruflöturinn og helsta samþættingaráhættan.

Fyrir stór teymi eru API það sem lætur fólk vinna sjálfstætt. Vel hannað viðmót leyfir þér að breyta innviðum þínum án þess að samhæfa við hvern neytanda, sem er allur tilgangur þjónustumarka. Illa hannað lekur innri smáatriðum, þvingar samstillta uppsetningu og breytir safni þjónusta í dreifðan einstein: þjónustur skiptar í sundur en samt svo tengdar að þær verða að vera smíðaðar og settar upp saman. API-hönnun þín ákvarðar beint hve sjálfstætt teymin þín geta hreyft sig.

Í fyrirtækja- og opinberu umhverfi bera API líka regluvörslu-, öryggis- og endinguskyldur. Opinbert API getur þurft að fylgja [opnum stöðlum](https://en.wikipedia.org/wiki/Open_standard), haldast stöðugt árum saman og þjóna ytri hönnuðum sem þú getur ekki samhæft við. API fyrirtækja liggja undir samstarfsaðilasamþættingum með samningsbundnu þjónustustigi. Allt þetta hækkar kröfuna um útgáfuaga, [afturábak samhæfni](https://en.wikipedia.org/wiki/Backward_compatibility), stjórnarhætti og upplifun hönnuða.

## Meginreglur

- Hannaðu samninginn fyrst. Viðmótið er yfirveguð vöruákvörðun, ekki aukaafurð útfærslu.
- Fínstilltu fyrir upplifun neytandans, ekki eigin þægindi.
- Líttu á afturábak samhæfni sem loforð. Brjótandi breytingar þurfa nýja útgáfu og flutningsleið.
- Gerðu auðvelda hlutinn réttan: skynsamleg sjálfgefin gildi, fyrirsjáanlegar villur, samræmdar venjur.
- Hannaðu fyrir bilun. [Eins-áhrif](https://en.wikipedia.org/wiki/Idempotence) (endurtekin beiðni hefur sömu áhrif og ein), endurtekningar, blaðsíðuskipting og [hraðatakmörkun](https://en.wikipedia.org/wiki/Rate_limiting) eru fyrsta flokks áhyggjuefni, ekki eftiráhugsanir.
- Veldu samskiptastíl eftir samspilinu, ekki tískunni.
- Stýrðu API sem vörum, með eigendum, lífsferlum og skjölun.

## Ráðleggingar

### Vinndu API-fyrst og samningsdrifið

Skilgreindu og rýndu API-samninginn, með tilföngum hans, aðgerðum, skemum og villumerkingum, áður en þú skrifar útfærsluna. Notaðu véllæsilega tilgreiningu, svo samningurinn geti framleitt skjölun, biðlara- og þjónsstubba, líkingaþjóna og staðfestingu. Þá geta neytendur byrjað að samþætta gegn líkingunni meðan þú smíðar, og samningurinn verður eina uppspretta sannleikans sem báðar hliðar prófa gegn.

### Veldu samspilsstíl af ásetningi

Veldu milli [REST](https://en.wikipedia.org/wiki/REST) (representational state transfer), [GraphQL](https://en.wikipedia.org/wiki/GraphQL), [gRPC](https://en.wikipedia.org/wiki/GRPC) og [atburðadrifinna skilaboða](https://en.wikipedia.org/wiki/Event-driven_architecture) eftir samspilinu, ekki persónulegri kjör. Notaðu REST fyrir tilfangamiðuð, víða samvirk, skyndiminnisgeymanleg viðmót. Notaðu GraphQL þegar fjölbreyttir biðlarar þurfa sveigjanlegar, samanteknar lesningar yfir ríkt graf. Notaðu gRPC fyrir hraðvirk, sterktegundagreind köll milli innri þjónusta. Notaðu atburðadrifin skilaboð fyrir ósamtíma, aftengd vinnuflæði og fyrir að dreifa ástandsbreytingum. Mörg stór kerfi nota nokkra stíla samtímis, hvern þar sem hann á við.

### Útgáfustýrðu og leggðu niður með aga

Taktu upp skýra útgáfustefnu og birta niðurlagningarstefnu: hvernig þú flokkar breytingar, hve lengi þú styður gamlar útgáfur og hvernig þú tilkynnir neytendum. Dragðu skýra línu milli afturábak samhæfra breytinga (að bæta við valkvæðum reitum, nýjum endapunktum) og brjótandi breytinga (að fjarlægja eða endurnefna reiti, breyta gerðum eða merkingu). Endurnýttu aldrei merkingu núverandi reits. Gefðu neytendum skörunarglugga til að flytja og tilkynntu tímalínur með góðum fyrirvara.

### Gerðu villumerkingar samræmdar og véllæsilegar

Skilaðu skipulögðum, fyrirsjáanlegum villum: stöðugum véllæsilegum kóðum, mannlæsilegum skilaboðum og nægu samhengi til að bregðast við, án þess að leka viðkvæmum innviðum. Notaðu sömu stöðumerkingar á hverjum endapunkti svo biðlarar geti meðhöndlað villur samræmt. Skjalfestu hverja villu sem neytandi gæti rekist á.

### Byggðu inn eins-áhrif, blaðsíðuskiptingu og hraðatakmörkun

Gerðu skrifaðgerðir öruggar til endurtekningar með því að styðja eins-áhrifalykla, svo biðlari sem reynir aftur eftir tímamörk gjaldfæri ekki tvisvar eða búi ekki til tvisvar. Blaðsíðuskiptu sérhvern listaendapunkt frá fyrsta degi og kjóstu bendilsbundna blaðsíðuskiptingu fyrir stór eða breytileg gagnasöfn. Beittu og skjalfestu hraðatakmörk og skilaðu núverandi takmarkaástandi til biðlara svo þeir geti dregið úr á mjúkan hátt.

### Stýrðu API og fjárfestu í upplifun hönnuða

Líttu á hvert API sem vöru, með eiganda, lífsferli og skráningu í skrá. Settu upp hönnunarrýni eða API-staðlastjórn svo viðmót haldist samræmd yfir teymi. Fjárfestu í upplifun hönnuða: nákvæmum tilvísunarskjölum, flýtileiðbeiningum, dæmum, sandkassa og breytingaskrá. Í stóru vistkerfi er gátt eða skrá sem gerir API finnanleg nauðsynleg.

## Málamiðlanir: kostir og gallar

| Stíll | Best fyrir | Kostir | Gallar |
|---|---|---|---|
| REST / HTTP | Opinber, tilfangamiðuð API | Alls staðar, skyndiminnisgeymanlegt, einfalt, samvirkt | Of- og vansókn gagna, margar ferðir, laus samningur nema tilgreindur |
| GraphQL | Sveigjanlegar lesningar fyrir ólíka biðlara | Fyrirspurnir tilgreindar af biðlara, einn endapunktur, sterkt skema | Flækja í skyndiminni og hraðatakmörkun, áhætta fyrirspurnarkostnaðar, flækja á þjóni |
| gRPC | Innri hraðvirk köll | Hratt, þétt, sterktegundagreint, straumun | Léleg vafrastuðningur, minna mannlæsilegt, þyngri verkfæri |
| Atburðadrifið | Ósamtíma, aftengd vinnuflæði | Laus tengsl, skalanlegt, seigt | Erfiðara að rökræða, endanlegt samræmi, rekstrarflækja |

Útgáfustefnur skipta stöðugleika fyrir viðhald. Að styðja margar gamlar útgáfur ver neytendur, en margfaldar kóðann sem þú þarft að viðhalda og prófa. Afturábak samhæfni skiptir eigin frelsi þínu fyrir stöðugleika neytenda, venjulega rétt skipti fyrir víða notað API. Stóra myndin: kostnaður slæmrar API-ákvörðunar er greiddur af hverjum neytanda yfir allan líftíma viðmótsins. Svo það er þess virði að eyða meiri hönnunarfyrirhöfn á mörkunum en nánast hvar sem er annars staðar.

## Spurningar til að ræða með teyminu

1. **Hvernig flokkarðu breytingu sem afturábak samhæfa eða brjótandi og hvaða sjálfvirka athugun grípur hljóðlátan brest áður en hann er afhentur?** Þessi kafli dregur harða línu: að bæta við valkvæðum reitum og nýjum endapunktum er öruggt, á meðan að fjarlægja eða endurnefna reiti, breyta gerðum eða endurnýta merkingu reits brýtur neytendur. Í stóru teymi sér sá sem gerir breytinguna oft ekki hvern neytanda, svo „lítil“ breyting getur hljóðlega brotið samstarfsaðila sem þú talar aldrei við. Komdu með áþreifanlega merkið á fundinn: keyrirðu sjálfvirkar samningssamhæfisathuganir í CI gegn útgefnu tilgreiningunni, eða treystirðu á að einhver muni regluna. Í fyrirtækja- og opinberu umhverfi, þar sem brjótandi breyting þvingar fram samhæfðan flutning yfir hvern samstarfsaðila og getur spannað breytingar á söluaðilum og ríkisstjórnum, skalar kostnaðurinn með fjölda neytenda. Ákveddu flokkunarreglurnar og tengdu samhæfishlið, svo ósamrýmanleg breyting láti smíðina mistakast frekar en samþættingu.

2. **Hvaða áreiðanleikaforsendur, eins-áhrifalyklar, blaðsíðuskipting og hraðatakmörkun, eru skylda á sérhverjum nýjum endapunkti frá fyrsta degi?** Kaflinn heldur því fram að þetta séu fyrsta flokks áhyggjuefni, því að bæta eins-áhrifalykli við lifandi gjaldfærsluendapunkt eða blaðsíðuskiptingu við lista sem þegar er afhentur er sjálft brjótandi breyting. Stórt vistkerfi magnar þetta: endapunktur sem virkar í prófun hrynur undir raunverulegu gagnamagni, og skrif án eins-áhrifa breytir einu netblikki í tvöfalda gjaldfærslu. Komdu með sönnunargögn um hvaða núverandi endapunktar skortir þetta og hvað endurtekningarstormur myndi gera. Gerðu sjálfgefnu gildin óumsemjanleg fyrir nýja endapunkta: bendilsblaðsíðuskipting á hverjum lista, eins-áhrifalyklar á hverju skrifi, skjalfest hraðatakmörk sem skila núverandi ástandi. Það breytir framtíðarþvinguðum flutningi í einskiptis hönnunarvenju.

3. **Hannarðu og rýnir þú samninginn í raun áður en þú skrifar útfærsluna, eða lekur viðmótið út úr kóðanum?** API-fyrst ráðleggingin biður um véllæsilega tilgreiningu, rýnda fyrirfram, sem framleiðir skjöl, stubba og líkingar og leyfir neytendum að samþætta gegn líkingu meðan þú smíðar. Þegar samningurinn eltir útfærsluna afhjúpar viðmótið innri gagnagrunnsuppbyggingu og færist í hvert sinn sem útfærslan gerir það, sem er helsta andmynstur þessa kafla. Merkið til að skoða: getur neytandi byrjað að samþætta gegn líkingu þinni í dag, eða þarf hann að bíða eftir keyrandi bakenda. Fyrir opinber API og samstarfsaðila-API, þar sem viðmótið er vöruflöturinn og dýrasti hluturinn til að fá rangan, sparar að eyða degi í samninginn vikur af stuðningsróti. Gerðu samningsrýni að skyldu skrefi áður en útfærsla hefst.

4. **Þegar tvö teymi þurfa að afhjúpa sömu getu, hvaða samspilsstíll vinnur og hver hefur vald til að segja nei við fjórða samskiptareglunni?** Þessi kafli segir þér að velja REST, GraphQL, gRPC eða atburðadrifin skilaboð eftir samspilsfit, en í stórum stíl er raunverulega áhættan að hvert teymi velur sinn uppáhalds og neytendur mæta ólíkri venju á hverjum endapunkti. Stór skipulagsheild borgar fyrir þá sundrun í biðlarasöfnum, gáttum, vöktun og vitrænni byrði á hvern samþættara sem lærir nú fjögur málvenjur í stað einnar. Komdu með skrá yfir samskiptareglur sem þegar eru í framleiðslu, samspilið sem hver var valin til að þjóna og neytendurna sem spanna fleiri en eina. Sjónarmiðið á móti er raunverulegt: sameiginlegt sjálfgefið dregur úr útbreiðslu, en stíf skylda þvingar gRPC-löguð vandamál í REST-laga gat. Nefndu staðlastjórnina eða arkitektúrrýnina sem á undanþáguferlið, því í fyrirtækja- og opinberum landslögum verður útbreiðsla stíla varanlegur skattur á samþættingu og erfitt vandamál að afturkalla þegar samstarfsaðilar reiða sig á hvern.

5. **Hver er birt niðurlagningarstefna okkar og getum við sannað að við heiðrum í raun stuðningsgluggann sem við auglýsum?** Kaflinn lítur á útgáfustýringu og niðurlagningu sem aga: skrifleg stefna um hve lengi gamlar útgáfur lifa, hvernig neytendum er tilkynnt og hvaða skörun þeir fá til að flytja. Loforð sem þú getur ekki framfylgt er verra en ekkert, því stórt vistkerfi inniheldur neytendur sem þú talar aldrei við og munu halda áfram að kalla á útrunna útgáfu þar til hún brotnar í framleiðslu. Komdu með sönnunargögnin í umræðuna: hve margar lifandi útgáfur þú ber í dag, raunverulega notkun á hverri, hvort þú sérð hvaða neytendur kalla enn á niðurlagðan endapunkt og hve langt fram í tímann síðasta niðurlagning var tilkynnt. Þrýstingurinn á móti er viðhaldskostnaður gegn stöðugleika neytenda og hvort tveggja er raunverulegt. Fyrir samstarfsaðila fyrirtækja undir samningsbundnu þjónustustigi og opinber API sem verða að lifa af ríkisstjórnir og söluaðilabreytingar er stuðningsglugginn skuldbinding sem getur lifað teymið sem gerði hana, svo ákveddu hver á hana og hvernig niðurlagning er sönnuð örugg áður en hún gerist.

6. **Hvernig vitum við að upplifun hönnuða okkar sé góð, eða erum við að gera ráð fyrir því því API virkar fyrir okkur?** Þessi kafli rammar hvert API sem vöru þar sem upptaka veltur á nákvæmum tilvísunarskjölum, flýtileiðbeiningum, dæmum, sandkassa, breytingaskrá og finnanlegri skrá. Teymi rugla reglulega saman „API virkar“ og „API er nothæft“, og bilið birtist sem stuðningsmiðar, misheppnaðar samþættingar og neytendur sem hljóðlega gefast upp. Komdu með mælanleg merki frekar en skoðanir: tíma að fyrsta árangursríka kalli fyrir nýjan samþættara, rúmmál stuðningsmiða á endapunkt, hve úrelt birt skjöl eru gegn lifandi samningnum og hvort nýliði getur sjálfsafgreitt úr gáttinni án þess að senda teyminu þínu póst. Spennan er sú að skjölun og gáttir kosta raunverulega fyrirhöfn sem keppir við að afhenda eiginleika, en í stóru vistkerfi ýtir léleg upplifun hönnuða samþættingarkostnaði yfir á hundruð neytenda í einu. Hjá hinu opinbera, þar sem opið API þjónar ytri hönnuðum sem þú getur ekki samhæft við og gagnsæi er oft skyldað, er nothæft, vel skjalfest, finnanlegt viðmót hluti af almennri ábyrgðarskyldu, ekki viðbót.

## Sjónarhorn eftir geirum

**Sprotafyrirtæki.** Með tvo eða þrjá verkfræðinga og engan tíma fyrir helgisiði skaltu hafa samninginn léttan en raunverulegan: ein véllæsileg tilgreining sem fyrstu hönnunarsamstarfsaðilar viðskiptavinir þínir geta samþætt gegn meðan þú smíðar. Settu ekki upp API-gátt, skrá eða stjórnarháttastjórn enn, en festu tvær venjur sem erfitt er að bæta við síðar, eins-áhrifalykla á skrifum og bendilsblaðsíðuskiptingu á listum, því að bæta þeim við lifandi endapunkt er brjótandi breyting sem þú hefur ekki efni á. Kjóstu einn samspilsstíl, næstum alltaf REST, svo þú berir enga samskiptaregluútbreiðslu inn í fyrsta árið.

**Lítið fyrirtæki.** Án sérstaks API-sérfræðings og með þröngt fjárhagsáætlun skaltu hallast að verkfærum sem framleiða skjöl, líkingar og biðlarastubba úr tilgreiningu svo alhliða starfsmaður geti viðhaldið viðmótinu án djúprar samskiptaregluþekkingar. Vegðu kaupa gegn smíða vandlega: tilbúin gátt eða API-stjórnunarvettvangur gefur þér hraðatakmörkun, lykla og hönnuðagátt sem þú myndir annars handsmíða. Haltu yfirborðinu litlu og venjunum samræmdum, því hver aukaendapunktur og hvert einstakt villusnið er eitthvað sem þunnt teymi þarf að styðja að eilífu.

**Stórfyrirtæki.** Yfir mörg sjálfstæð teymi er meginvandinn samræmi án þess að verða flöskuháls: sameiginlegur stílleiðarvísir, API-staðlarýni, skrá sem gerir viðmót finnanleg og sjálfvirkar afturábak-samhæfisathuganir í CI svo hljóðlátur brestur láti smíðina mistakast frekar en samþættingu. Stýrðu hverju API sem vöru með nefndum eiganda, lífsferli og birtri niðurlagningarstefnu og mældu upptöku, stuðningsálag og tíðni brjótandi breytinga svo eignasafnið haldist heilbrigt. Staðlaðu samspilsstíla og útgáfureglur um alla skipulagsheildina, því í þessari stærð er sundrun dýra sjálfgefna valið.

**Hið opinbera.** Innkaupareglur, opnar staðlaskyldur og almenn ábyrgð móta hvert val. Birtu samninginn opinskátt, fylgdu skyldum opnum stöðlum og útvegaðu sandkassa og tilvísunarskjöl svo ytri hönnuðir sem þú getur ekki samhæft við geti sjálfsafgreitt. Líttu á langtíma afturábak samhæfni sem stefnukröfu, því samþættingar verða að lifa af ríkisstjórnir og söluaðilabreytingar, og gerðu brjótandi breytingar sjaldgæfar, þungt stýrðar og tilkynntar langt fram í tímann. Haltu API-inu og skjölun þess nógu gagnsæju til að standast almenna og úttektarskoðun og forðastu séreignarsnið sem myndu fanga framtíðarstjórn.

## Dæmi

**Sprotafyrirtæki.** Sprotafyrirtæki á frumstigi sem afhendir fyrsta opinbera API sitt skrifar samninginn sem véllæsilega tilgreiningu áður en það kóðar, svo tveir hönnunarsamstarfsaðilar viðskiptavinir þess geti samþætt gegn líkingu meðan bakendinn er enn í smíðum. Jafnvel með aðeins handfylli neytenda bætir það eins-áhrifalyklum við gjaldfærsluendapunktinn og bendilsblaðsíðuskiptingu við hvern lista, því að bæta þeim við eftir að samstarfsaðilar reiða sig á API-ið þýddi brjótandi breytingu sem það hefur ekki efni á. Samningurinn fyrirfram kostar dag og sparar vikur af stuðningsfram-og-til-baka.

**Stórfyrirtæki.** Stórt greiðslufyrirtæki afhjúpar opinbert REST API fyrir þúsundir seljenda. Sérhver skrifendapunktur tekur við eins-áhrifalykli, svo netendurtekning býr aldrei til tvöfalda gjaldfærslu. Sérhver listaendapunktur notar bendilsblaðsíðuskiptingu. Villur bera stöðuga kóða skjalfesta í opinberri tilvísun. Formleg niðurlagningarstefna tryggir langan stuðningsglugga fyrir hverja útgáfu, með fyrirvara og flutningsleiðbeiningum. Þessi agi er samkeppnisforskot: samþættarar treysta að API-ið brotni ekki undir þeim.

**Hið opinbera.** Landsbundin stafræn þjónusta birtir opið API fyrir borgaragögn, sem fylgir skyldum opnum stöðlum og API-fyrst hönnunarferli. Samningurinn er tilgreindur og rýndur fyrir smíðina, birtur í miðlægri API-skrá ríkisins og þjónaður með sandkassa, svo þriðja aðila hönnuðir, sem ekki er hægt að samhæfa við hvern fyrir sig, geti samþætt á eigin spýtur. Langtíma afturábak samhæfni er stefnukrafa, því samþættingar verða að lifa af ríkisstjórnir og söluaðilabreytingar. Svo brjótandi breytingar eru sjaldgæfar og þungt stýrðar.

## Viðskiptarök: hvatar, ávöxtun fjárfestingar og heildarkostnaður

Góð API-hönnun lækkar samþættingarkostnað, sem er oft stærsti kostnaðurinn við að tengja kerfi og taka á móti samstarfsaðilum. Með skýru, stöðugu, vel skjalfestu API samþætta neytendur á dögum án eins stuðningsmiða. Lélegt framleiðir endalaust stuðningsálag, misheppnaðar samþættingar og orðsporsskaða. Þegar API er sjálft varan knýr upplifun hönnuða beint upptöku og tekjur.

Stærsti falinn kostnaður eru brjótandi breytingar. Sérhver brjótandi breyting þvingar fram samhæfðan flutning yfir alla neytendur, innri teymi og ytri samstarfsaðila jafnt, og heildarkostnaðurinn skalar með fjölda neytenda og því hve erfitt er fyrir þá að hreyfast samstillt. Fjárfesting fyrirfram í samningsfyrst hönnun, afturábak samhæfni og útgáfuaga forðast þessa dýru, skipulagsheildarbreiðu flutningsviðburði. Þegar þú talar við forystu skaltu setja API-gæði fram sem vogarafl fyrir sjálfstæði teyma, vöxt samstarfsaðilavistkerfis og að forðast kostnaðarsama þvingaða flutninga. Rektu samþættingartíma, rúmmál stuðningsmiða og tíðni brjótandi breytinga sem sönnun þína.

## Andmynstur og gildrur

- **Útfærslu-fyrst API:** viðmótið lekur innri gagnagrunnsuppbyggingu og breytist hvenær sem útfærslan gerir það.
- **Hljóðlátar brjótandi breytingar:** að endurnýta reit eða herða staðfestingu án útgáfuhækkunar brýtur neytendur ófyrirsjáanlega.
- **Málglöð viðmót:** hönnun sem krefst margra ferða fyrir eina rökræna aðgerð og skaðar afköst og nothæfi.
- **Ósamræmdar venjur:** hver endapunktur finnur upp eigin nafngiftir, villusnið og blaðsíðuskiptingu, svo biðlarar geta ekki alhæft.
- **Engin blaðsíðuskipting eða hraðatakmörkun:** endapunktar sem virka í prófun og hrynja undir raunverulegu gagnamagni eða álagi.
- **Skrif án eins-áhrifa:** endurtekningar valda tvíverknaði. Eitt netblik spillir gögnum.
- **Útgáfuútbreiðsla:** of margar lifandi útgáfur án niðurlagningar, sem margfaldar viðhald þar til það er óviðráðanlegt.
- **Skjöl sem eftiráhugsun:** óskjalfestar eða úreltar tilvísanir sem ýta öllum samþættingarkostnaði á neytendur.

## Þroskalíkan

- **Stig 1, Upphaf:** API verða til úr útfærslu sem aukaafurð. Engar sameiginlegar venjur. Viðmótið lekur innri gagnagrunnsuppbyggingu. Brjótandi breytingar eru algengar, óboðaðar og uppgötvast þegar samþætting neytanda mistekst.
- **Stig 2, Þróun:** Sum teymi fylgja grunn REST-venjum, útgáfustýra óformlega og skrifa skjöl í höndunum, en vinnubrögð eru ósamkvæm milli teyma. Eins-áhrif, blaðsíðuskipting og hraðatakmörkun birtast á sumum endapunktum og ekki öðrum. Neytendur læra enn sérkenni hvers API fyrir sig.
- **Stig 3, Stöðlun:** Samningsfyrst hönnun með véllæsilegum tilgreiningum er skjalfest og framfylgt um alla skipulagsheildina. Birt niðurlagningarstefna, samræmdar villumerkingar og skyldubundin eins-áhrif, bendilsblaðsíðuskipting og hraðatakmörkun gilda um hvern nýjan endapunkt. Sameiginlegur stílleiðarvísir og API-staðlarýni halda viðmótum samræmdum milli teyma.
- **Stig 4, Stjórnun:** API-eignasafnið er mælt og stýrt gegn grunnlínum: sjálfvirkar afturábak-samhæfisathuganir hliða hverja breytingu í CI og þú rekur tíma að fyrsta árangursríka kalli, rúmmál stuðningsmiða á endapunkt, tíðni brjótandi breytinga, fjölda lifandi útgáfa og notkun á endapunkt svo niðurlagning og hönnunarákvarðanir byggi á gögnum frekar en skoðun. Hvert API er stýrð vara í skrá með nefndum eiganda og mælikvarðar kalla fram aðgerðir þegar þjónusta rekur frá markmiðum sínum.
- **Stig 5, Samhæfing:** API-stefna er stöðugt bætt og samþætt um skipulagsheildina. Skráin, gáttin, útgáfureglur og samhæfishlið vinna sem eitt kerfi. Skipulagsheildin leggur reglulega niður, sameinar og endurafmarkar viðmót á grundvelli mældrar upptöku og kostnaðar. Samspilsstíla- og útgáfustaðlar aðlagast eftir því sem vistkerfið, samstarfsaðilar og tækni breytast og brjótandi breytingar eru sjaldgæfar og vel stýrðar.

## Hugmyndir til umræðu

- Hvernig ákveðurðu hvenær innra API er nógu stöðugt til að birta ytra?
- Hver er réttur stuðningsgluggi fyrir niðurlagðar útgáfur í þínu samhengi og hver borgar fyrir hann?
- Hvar ættu GraphQL eða gRPC að koma í stað REST innanhúss og hvar myndu þau bæta við meiri flækju en virði?
- Hvernig framfylgirðu API-samræmi yfir mörg sjálfstæð teymi án þess að verða flöskuháls?
- Hvernig ættu gervigreindarneytanleg API og verkfæraviðmót umboðsmanna að breyta hönnunarvenjum þínum?
- Hvaða sjálfvirkar athuganir geta gripið afturábak-ósamrýmanlegar breytingar áður en þær eru afhentar?

## Helstu atriði

- Hannaðu samninginn fyrst. API er vara og langlíft loforð.
- Afturábak samhæfni ver neytendur. Brjótandi breytingar þurfa nýjar útgáfur og flutningsleiðir.
- Veldu REST, GraphQL, gRPC eða atburði eftir samspilsfit, ekki tísku.
- Byggðu inn eins-áhrif, blaðsíðuskiptingu, hraðatakmörkun og samræmdar villur frá fyrsta degi.
- Stýrðu API sem vörum með eigendum, skrám og sterkri upplifun hönnuða.

## Heimildir og frekari lestur

- Roy Fielding, *Architectural Styles and the Design of Network-based Software Architectures* (dissertation)
- Arnaud Lauret, *The Design of Web APIs*
- Mike Amundsen, *RESTful Web APIs* and *Design and Build Great Web APIs*
- Sam Newman, *Building Microservices*
- OpenAPI Specification; JSON Schema (as reference standards)
- Martin Kleppmann, *Designing Data-Intensive Applications*
