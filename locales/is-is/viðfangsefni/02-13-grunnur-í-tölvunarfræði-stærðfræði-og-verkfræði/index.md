# 2.13 Grunnur í tölvunarfræði, stærðfræði og verkfræði

## Yfirlit og tilgangur

Undir hverjum ramma, tungumáli og skýjaþjónustu situr lag af varanlegri þekkingu sem breytist ekki: hvernig [reiknirit](https://en.wikipedia.org/wiki/Algorithm) hegða sér þegar gögn vaxa, hvernig [net](https://en.wikipedia.org/wiki/Computer_network) og [stýrikerfi](https://en.wikipedia.org/wiki/Operating_system) flytja í raun bæti, hvað sönnun eða líkindadreifing þýðir og hvernig þú mælir fullyrðingu í stað þess að bara fullyrða hana. *Software Engineering Body of Knowledge* (SWEBOK) nefnir þrjú þekkingarsvið fyrir þennan klöpp: tölvunarfræðigrunn, stærðfræðigrunn og verkfræðigrunn. Þessi kafli sameinar þau því í stóru teymi vinna þau saman. Tölvunarfræði segir þér hvernig vélar reikna. Stærðfræði segir þér hvernig á að rökræða nákvæmlega um réttleika og óvissu. Verkfræði segir þér hvernig á að breyta þeirri rökhugsun í áreiðanlega, mælanlega iðkun.

Hér er hvers vegna þetta skiptir máli: fjarvera þessara undirstöðuatriða er ósýnileg alveg þar til hún er skelfileg. Eiginleiki er afhentur og virkar á fartölvu, hrynur síðan í stórum stíl því enginn rökræddi um flækju. Endurtekningarlykkja fellir ósjálfstæði því enginn mótaði hana sem biðröð. „Handahófs“-tákngjafi reynist fyrirsjáanlegur því enginn skildi talnafræðina að baki. Teymi deilir í viku um hvaða hönnun er hraðari því enginn keyrði mælingu. Engin þessara bilana snýst um vantandi bókasafn. Þær snúast um vantandi undirstöður. Rammar ágripa vélina en afnema hana ekki, og ágripunin lekur einmitt undir álagi, töf og fjandsamlegum aðstæðum sem stór kerfi mæta.

Fyrir fyrirtækja- og opinber teymi eru undirstöður líka það sem gerir sérhæfingu örugga. Stórar skipulagsheildir skipta vinnu í framenda-, vettvangs-, gagna-, öryggis- og SRE-sérsvið (site reliability engineering) og reiða sig æ meira á gervigreindaraðstoðarmenn sem mynda sennilegan kóða eftir pöntun. Báðar þróanir auka sömu áhættu: að enginn í teyminu geti dæmt hvort aðferð sé traust. Mun myndað SQL skanna milljarð raða? Breytti „fínstillingin“ hljóðlega aukningarfræðilega kostnaðinum? Er tölfræðilega fullyrðingin í skýrslunni raunverulega marktæk? Sameiginlegar undirstöður eru sameiginlega tungumálið sem leyfir sérfræðingum að rýna vinnu hver annars, leyfir rýnum að grípa örugg-en-röng gervigreindarúttök og leyfir skipulagsheild að halda dómgreind sinni þegar verkfæri breytast. Þessi kafli tengist hugbúnaðarhönnun (kafli 2.2), dreifðum kerfum (kafli 3.3), biðraðafræði (kafli 11.3), gagnaarkitektúr (kafli 3.4) og gervigreind/vélnámi (kafli 6.2), sem öll beita þessum undirstöðum á tiltekin svið.

## Meginreglur

- **Ágripanir leka:** að þekkja lagið undir því sem þú notar er það sem bjargar þér þegar það lekur.
- **Aukningarfræði ræður stærð:** munurinn á O(n) og O(n²) er munurinn á því að virka og bila við tíu milljón raðir.
- **Réttleiki er rökhugsun, ekki heppni:** rökfræði, fastayrðingar og sönnunarhugtök liggja undir hverju áreiðanlegu kerfi.
- **Óvissa er magngreinanleg:** líkindi og tölfræði breyta „það virðist hægt“ í sönnunargögn.
- **Mældu áður en þú fullyrðir:** reynsluaðferðin aðskilur verkfræði frá skoðun.
- **Mótaðu áður en þú smíðar:** lítið formlegt líkan er ódýrara en stór framleiðslubilun.
- **Undirstöður lifa ramma:** fjárfestu í því sem verður enn satt eftir tuttugu ár.

## Ráðleggingar

### Tölvunarfræðigrunnur: þekktu vélina undir ágripuninni

Í stóru teymi viltu hafa vinnuhæf tök á tölvunarfræðiundirstöðunum sem ráða því hvort hugbúnaður hegðar sér rétt og skilvirkt í stórum stíl.

- **Reiknirit og [gagnagerðir](https://en.wikipedia.org/wiki/Data_structure).** Að velja rétta gerð (hakkatafla á móti tré, fylki á móti tengdum lista, rétta vísitalan) er áhrifamesta afkastaákvörðun sem flestir verkfræðingar taka, og þú tekur hana áður en nokkur greining fer fram. Gerðu þig reiprennandi í staðlaða efnisskránni og vittu hvaða aðgerðir hver gerð gerir ódýrar eða dýrar.
- **Reiknilega flækju.** [Big-O](https://en.wikipedia.org/wiki/Big_O_notation) rökhugsun, að lýsa því hvernig kostnaður reiknirits vex eftir því sem inntak þess vex, er daglega verkfærið þitt til að spá fyrir um hegðun í stórum stíl út frá hegðun á fartölvu. Venjan sem skiptir máli er að spyrja, um hverja lykkju og fyrirspurn, „hvað kostar þetta þegar gögnin vaxa?“ Hreiðruð lykkja yfir notendafærslur er fín í prófun og banvæn í framleiðslu.
- **Stýrikerfi og samtími.** Ferli, þræðir, minni, tímaröðun, skráakerfi og gildrur [samtíma](https://en.wikipedia.org/wiki/Concurrency_%28computer_science%29) (kappakstur, pattstöður, samkeppni) útskýra stóran hluta erfiðra framleiðslugalla. Að skilja hvað stýrikerfið gerir í raun afhjúpar töfarsveiflur og auðlindaþurrð.
- **Netkerfi.** Töf, bandvídd, pakkatap, TCP á móti UDP (áreiðanlegar á móti léttum flutningssamskiptareglum), DNS (Domain Name System sem leysir nöfn í heimilisföng), [TLS](https://en.wikipedia.org/wiki/Transport_Layer_Security) (Transport Layer Security sem dulkóðar tengingar) og raunveruleiki dreifðra samskipta liggja undir hverju þjónustukalli. Hinar klassísku [rangálykanir um dreifða tölvun](https://en.wikipedia.org/wiki/Fallacies_of_distributed_computing) (netið er ekki áreiðanlegt, töf er ekki núll, bandvídd er ekki óendanleg) eru netkerfislexíur sem endurtaka sig í kafla 3.3.
- **[Gagnagrunnar](https://en.wikipedia.org/wiki/Database).** Fyrirspurnaráætlun, vísitölur, færslur, einangrunarstig og normalísering ráða hvort gagnaaðgangur er hraður og réttur. Kafli 3.4 fjallar um gagnaarkitektúr. Grunnurinn er að vita hvers vegna vantandi vísitala breytir millisekúndu fyrirspurn í fulla töfluskönnun.
- **Tölvuarkitektúr.** Skyndiminni, minnisstigveldi, örgjörvaleiðslur og I/O-kostnaður útskýra afkastaóvæntingar sem greining ein getur ekki. Skyndiminnisvænt aðgangsmynstur getur slegið „snjöll“ reiknirit um stærðargráðu.
- **Grunnur gervigreindar/vélnáms og mannlegir þættir.** Nægur skilningur á gervigreind og vélnámi (AI/ML), nefnilega líkönum, þjálfun og ályktun, til að nota þau á ábyrgan hátt (kafli 6.2), auk nægs grunns í mannlegum þáttum (nothæfi, vitræn byrði, villuhætt viðmót) til að smíða hugbúnað sem fólk getur í raun rekið örugglega.

### Stærðfræðigrunnur: rökræddu nákvæmlega um réttleika og óvissu

Stærðfræði er tungumál nákvæmrar rökhugsunar. Þú þarft ekki að vera stærðfræðingur, en eftirfarandi hugtök eru nauðsynleg í daglegri verkfræði.

- **Rökfræði og sönnun.** Setningarökfræði og umsagnarökfræði liggja undir hverju skilyrði, hverri fastayrðingu og hverri prófastaðhæfingu. Að setja fram forskilyrði, eftirskilyrði og fastayrðingar, sem er að rökræða um hvað *verður* að vera satt, er hvernig þú skrifar réttan samhliða kóða og grípur jaðartilvik áður en atvik finnur þau.
- **[Mengjafræði](https://en.wikipedia.org/wiki/Set_theory) og vensl.** Mengi, vensl og föll eru stærðfræðilegi burðarásinn í venslalíkaninu, tagakerfum og skýrri hugsun um aðild, einkvæmni og vörpun.
- **Graf.** Ósjálfstæðisgröf, nettopologíur, smíðaraðir, leiðarval og félags-/skipulagsuppbygging eru öll [graf](https://en.wikipedia.org/wiki/Graph_theory). Að kunna yfirferðar-, stystu-leiðar- og hringagreiningarhugmyndir er víða beitanlegt.
- **[Endanlegar ástandsvélar](https://en.wikipedia.org/wiki/Finite-state_machine).** Samskiptareglur, vinnuflæði, viðmótsástönd og lífsferilsstjórnun eru hreint mótuð sem ástandsvélar, sem gera ólögleg ástönd óframsetjanleg og jaðartilvik talin upp.
- **[Líkindi](https://en.wikipedia.org/wiki/Probability) og [tölfræði](https://en.wikipedia.org/wiki/Statistics).** Afkastahundraðshlutar, afkastagetuáætlun, [A/B-prófanir](https://en.wikipedia.org/wiki/A/B_testing) (að bera saman tvö afbrigði á lifandi umferð til að sjá hvort stendur sig betur), áreiðanleikamat og vélnám hvíla allt á líkindum og tölfræði. Að þekkja muninn á meðaltali og p99 (99. hundraðshluta-, eða nánast verstatilviks-, gildinu), skilja dreifni og geta dæmt hvort niðurstaða sé marktæk er það sem aðskilur raunverulegar ályktanir frá suði. Það er líka stærðfræðin að baki biðraðafræði (kafli 11.3).
- **Talnafræði viðeigandi fyrir dulritun.** Mátreikningur, frumtölur og stakrænir logaritmar eru grunnur [opinberlykladulritunar](https://en.wikipedia.org/wiki/Public-key_cryptography) sem tryggir allt. Þú ættir ekki að útfæra eigin dulritun, en að skilja *hvers vegna* lyklastærð, handahóf og val reiknirits skipta máli er það sem heldur þér frá einföldu mistökunum sem brjóta öryggi.

### Verkfræðigrunnur: breyttu rökhugsun í áreiðanlega iðkun

Verkfræðiundirstöður eru það sem gerir hugbúnaðarverkfræði að *verkfræði*grein, og ekki handverk eitt.

- **Reynsluaðferðin.** Myndaðu tilgátu, hannaðu tilraun, mældu og láttu sönnunargögn, ekki starfsaldur eða innsæi, útkljá spurninguna. Hvort sem þú berð saman tvær hönnunir, greinir afturför eða metur fullyrðingu söluaðila, slær mæling rifrildi.
- **Mæling.** Skilgreindu hvað þú ert að mæla og hvernig, með einingum og skekkjumörkum. Slæm mæling (villandi meðaltöl, ófulltrúaleg viðmið, handvalin keyrsla) er verri en engin, því hún þvær skoðun í gögn.
- **Tölfræðigreining niðurstaðna.** Beittu líkindum og tölfræði hér að ofan á raunverulegar mælingar: skýrðu frá dreifingum og hundraðshlutum, taktu tillit til dreifni og forðastu að álykta af einni keyrslu eða of litlu úrtaki.
- **Ágripun og mótun.** Kjarnahreyfing verkfræðinnar er að byggja einfaldað líkan sem fangar það sem skiptir máli, felur það sem gerir það ekki og, jafn mikilvægt, þekkir eigin mörk. Afkastagetulíkan á baki umslags eða lítið ástandsvélarit afhjúpar hönnunargalla löngu áður en kóði gerir það.
- **Staðlar.** Verkfræði fleygir fram með því að standa á samþykktum stöðlum (samskiptareglum, sniðum, viðmótum og starfsreglum) frekar en að finna þá upp aftur. Í stórum og opinberum teymum eru staðlar líka hvernig sjálfstætt smíðaðir hlutar samvirka og hvernig vinna er úttektuð.
- **[Rótarorsakagreining](https://en.wikipedia.org/wiki/Root_cause_analysis).** Þegar eitthvað bilar finnur agað RCA („fimm hvers vegna“, bilanatré, eftirrýni án sakbendingar) undirliggjandi orsök frekar en næsta einkenni, svo lagfæringin haldi. Líttu á það sem reynsluaðferðina beitta á bilanir.

## Málamiðlanir: kostir og gallar

| Ákvörðun | Kostir | Gallar |
|---|---|---|
| **Fjárfestu í undirstöðum víða** | Varanleg dómgreind, öruggari sérhæfing og gervigreindarnotkun, færri stærðaróvæntingar | Hægari aðlögun, kostar tíma sem afhendingarþrýstingur stendur gegn |
| **Reiddu þig á ramma/ágripanir** | Hröð afhending, minna að vita fyrirfram | Bregst við lekann, enginn getur greint djúp vandamál |
| **Formleg mótun fyrir smíði** | Grípur hönnunargalla ódýrt, sameiginlegur skilningur | Fyrirhöfn fyrirfram, líkön geta ofeinfaldað raunveruleikann |
| **Mældu reynslulega** | Gagnabyggðar ákvarðanir, bindur enda á rifrildi | Krefst nákvæmni, slæm mæling villir |
| **Hallastu að gervigreindarmynduðum kóða** | Hraði, steypa meðhöndluð | Sennilegt-en-rangt úttak þarf undirstöður til að grípa |

Endurtekna málamiðlunin er **hraði núna á móti dómgreind síðar**. Undirstöður hjálpa sjaldan til að afhenda *þennan* eiginleika hraðar. Það sem þær gera er að hjálpa teyminu að taka réttar ákvarðanir yfir þúsundir eiginleika og forðast dýru, erfiðu-að-greina bilanirnar sem ágripanir fela. Hér er gildran: kostnaður við að vanrækja undirstöður er frestaður og dreifður, á meðan kostnaður við að læra þær er tafarlaus og sýnilegur. Svo undir afhendingarþrýstingi er stöðugt vanfjárfest í undirstöðum, þar til stærðar- eða öryggisatvik neyðir fram reikninginn.

## Spurningar til að ræða með teyminu

1. **Hver í teyminu okkar rýnir öryggisviðkvæma kóðann og skilja þeir hvers vegna lyklastærð og handahóf skipta í raun máli?** Þú ættir aldrei að rúlla eigin dulritun, en samt þarftu að velja bókasöfn, stærðarsetja lykla og afla handahófs, og hver þeirra er staður þar sem örugg röng ákvörðun (fyrirsjáanlegur tákngjafi, heimasmíðað kerfi sem söluaðili er að selja) brýtur hljóðlega öryggi þar til árásaraðili finnur það. Talnafræðin að baki opinberlykladulritun (mátreikningur, frumtölur, stakrænir logaritmar) er það sem leyfir rýni að hafna einföldu vali í stað þess að kinka því í gegn. Komdu með raunverulega afurð á fundinn: bentu á kóðann sem býr til táknin þín eða lotulykla og spurðu hver er hæfur til að segja að hann sé traustur. Ef heiðarlega svarið er enginn er bilið ekki vantandi bókasafn, og lagfæringin er að rækta eða ráða þá tilteknu undirstöðuhæfni og beina ákvörðunum um öryggisfrumstæður til einhvers sem hefur hana.

2. **Ráðum við og hækkum við fyrir undirstöðurökhugsun, eða verðlaunum við ramma­reiprennandi og borgum fyrir bilið síðar?** Kostnaður við að vanrækja undirstöður er frestaður og dreifður á meðan kostnaður við að læra þær er tafarlaus og sýnilegur, svo undir afhendingarþrýstingi er þessi þekking stöðugt vanfjárfest þar til stærðar- eða öryggisatvik neyðir fram reikninginn. Í stóru teymi sem skiptir vinnu í framenda-, vettvangs-, gagna- og SRE-sérsvið og reiðir sig æ meira á gervigreind sem myndar sennilegan kóða eru sameiginlegar undirstöður sameiginlega tungumálið sem leyfir sérfræðingum að rýna vinnu hver annars og grípa örugg-en-röng úttök. Komdu með viðtalsmatskvarða þinn og stöðuhækkunarviðmið: prófa þau hvort umsækjandi geti rökrætt um flækju, mælingu og réttleika, eða aðeins hvort hann kunni ramma þessa árs? Svarið ætti að endurmóta hvernig þú ræður, leiðbeinir og verndar námstíma, því á gervigreindaraðstoðartímanum er mannleg geta til að dæma traust að verða af skornum skammti, verðmæt færni.

3. **Þegar tveir verkfræðingar eru ósammála um afköst hönnunar, mælum við, eða víkjum við fyrir þeim sem er eldri?** Reynsluaðferðin er það sem gerir þetta að verkfræði en ekki skoðun: myndaðu tilgátu, keyrðu tilraun og láttu sönnunargögn útkljá spurninguna, hvort sem þú berð saman tvær hönnunir, greinir afturför eða athugar fullyrðingu söluaðila. Gildran í stóru teymi er að rifrildi vinnast með sjálfstrausti og tign, og vika hverfur í umræðu sem mæling hefði bundið enda á á klukkustund. Komdu með nýlega hönnunardeilu og spurðu hvernig hún var í raun útkljáð: með gögnum, eða af háværustu manneskjunni í herberginu? Aðgerðin er að gera mælingu að eðlilegum hluta hönnunarrýni, með skilgreindum einingum, skekkjumörkum og dreifingum frekar en einni handvalinni keyrslu, svo „það virðist hraðara“ sé skipt út fyrir p95- eða p99-tölu sem allt teymið getur treyst.

4. **Spyr hönnunar- og kóðarýni okkar í raun „hvað kostar þetta þegar gögnin vaxa?“, eða uppgötvum við svarið aðeins í stórum stíl?** Aukningarfræðileg rökhugsun er áhrifamesta daglega færnin á listanum, því O(n²) lykkja er ósýnileg með prófagögnum og banvæn í framleiðslu, og ódýrasti staðurinn til að grípa hana er rýnin, ekki atvikið. Í stóru teymi er þrýstingurinn á móti afköst: rýnar undir fresti athuga stíl og réttleika á úrtakinu fyrir framan sig og spyrja sjaldan hvernig kóðinn hegðar sér við tíu milljón raðir. Komdu með nýlega sameiningarbeiðni og lestu hana upphátt með þeirri einu spurningu beittri á hverja lykkju, fyrirspurn og samtengingu, spurðu síðan hvort rýnigátlisti þinn eða sniðmát minnir yfirleitt á hana. Í fyrirtækja- eða opinberu kerfi þar sem gagnamagn klífur árum saman og hæg fyrirspurn getur brotið þjónustustigssamning eða seinkað bótum borgara skaltu gera flækjuspurninguna að skyldubundnu, skriflegu hliði í rýni, svo venjan velti ekki á því hver rýndi þann daginn.

5. **Hvernig ákveðum við hvort gervigreindarmyndaður kóði sé réttur, skalanlegur og öruggur og hver er í raun hæfur til að taka þá ákvörðun?** Myndaður kóði er fljótur að framleiða og auðveldur að samþykkja án gagnrýni, og hann er örugglega rangur nógu oft til að að sameina hann án undirstaðna er hvernig lúmskir stærðar- og öryggisgallar komast í kóðagrunninn. Spennan fyrir stórt teymi er raunveruleg: verkfærið er til að flýta fólki og að krefjast djúprar rýni á hverja tillögu þurrkar út ávinninginn, svo þú verður að ákveða hvaða flokkar myndaðs kóða (öryggisfrumstæða, heit fyrirspurn, samtímabreyting) fá alltaf sérfræðiskoðun og hverjir mega standast léttari athuganir. Komdu með úrtak nýlega sameinaðra gervigreindaraðstoðaðra breytinga og spurðu, fyrir hverja, hver í teyminu gæti af öryggi sagt að hún sé traust og hvort nokkur gerði það í raun. Fyrir fyrirtæki eða opinbera skipulagsheild sem svarar endurskoðendum skaltu nefna ábyrgan rýni fyrir áhættumikla flokka og skrá að manneskja með viðeigandi undirstöðuhæfni hafi samþykkt, því „líkanið skrifaði það“ er ekki rökstutt svar þegar myndaður galli nær til framleiðslu.

6. **Hver af áhættumiklu hönnunum okkar verðskuldar lítið formlegt líkan áður en við skrifum kóða og veit nokkur hér hvernig á að byggja eitt?** Afkastagetuáætlun á baki umslags, endanleg ástandsvél sem gerir ólögleg ástönd óframsetjanleg eða mengjafræðileg gagnatilgreining er miklu ódýrari en framleiðslubilunin sem hún kemur í veg fyrir, en samt er mótun undirstaðan sem teymi sleppa fyrst undir afhendingarþrýstingi. Sjónarmiðið á móti er að líkan er fyrirhöfn fyrirfram án afhents eiginleika til að sýna, og of íburðarmikið líkan getur villt með því að fela eigin mörk, svo færnin er að velja minnsta líkanið sem afhjúpar raunverulegu áhættuna. Komdu með tvær eða þrjár hannanir með verstu sprengisvæðin (greiðsluflæði, hæfisvél, samtímaþung leiðsla) og spurðu hvort einnar blaðsíðu líkan hefði afhjúpað jaðartilvik sem þú lentir síðar í í framleiðslu. Í fyrirtækja- eða opinberu umhverfi þar sem galli ber lagalegar eða opinberar afleiðingar gefur lítið formlegt líkan líka eftirlitsaðilum rýnanlega afurð og rökstudda ástæðu til að treysta hönnuninni, svo líttu á mótunargetu sem hæfni til að byggja upp af ásetningi en ekki lúxus.

## Sjónarhorn eftir geirum

**Sprotafyrirtæki.** Með pínulítið teymi og lítið fjármagn hefurðu ekki efni á djúpri bilun sem tekur daga að greina, svo fáu undirstöðuvenjurnar sem borga sig strax eru þær til að halda: spyrðu hvað hver fyrirspurn kostar þegar gögn vaxa og mældu raunverulegan hundraðshluta áður en þú treystir afkastafullyrðingu. Byggðu ekki formlega-aðferða nákvæmni sem þú munt ekki nota, en tryggðu að að minnsta kosti einn stofnandi geti rökrætt um flækju og handahóf, því fyrirsjáanlegur tákngjafi eða tilviljanakennd full töfluskönnun getur sökkt þér áður en þú finnur vöru-markaðspassa. Hallaðu þér að vel greindum stöðluðum bókasöfnum fyrir allt öryggisviðkvæmt frekar en að finna það upp.

**Lítið fyrirtæki.** Án sérstaks sérfræðings og með þröngt fjárhagsáætlun skaltu líta á undirstöður sem kaupa-gegn-smíða síu: kjóstu stýrða gagnagrunna, hýsta auðkenningu og staðlaða dulritun svo erfiðu hlutarnir séu meðhöndlaðir af fólki sem skilur talnafræðina sem þú hefur engan tíma til að læra. Þar sem þú skrifar kóða er ódýrasta öryggisráðstöfunin einn rýnir sem spyr stærðarspurningarinnar og athugar að tilkynntar tölur séu hundraðshlutar, ekki smjaðrandi meðaltöl. Eyddu af skornum skammti undirstöðuathygli í handfylli ákvarðana (vísitölur, lyklastjórnun, afkastagetu) þar sem röng ákvörðun er dýr að afturkalla.

**Stórfyrirtæki.** Í stórum stíl og yfir mörg teymi eru undirstöður sameiginlega tungumálið sem heldur sérhæfingu og gervigreindaraðstoð öruggri, svo staðlaðu væntingar: flækjurökhugsun, mælingu með réttri tölfræði og rótarorsakagreiningu sem skrifleg hlið í hönnunar- og kóðarýni. Stjórnarhættir og úttekt njóta beint góðs, því skjalfest flækjuathugun, skráð hundraðshlutabyggð viðmið og eftirrýni án sakbendingar eru einmitt sönnunargögnin sem rýnar og eftirlitsaðilar biðja um. Fjárfestu í leiðsögn og innri menntun svo þekkingin lifi í skipulagsheildinni en ekki í fáum óbætanlegum einstaklingum.

**Hið opinbera.** Innkaupareglur, gagnsæi og almenn ábyrgð gera undirstöður að regluvörslueign jafnt og verkfræðieign. Krefstu staðlaðrar, vel greindrar dulritunar og hafnaðu heimasmíðuðu kerfi hvers söluaðila, mótaðu hæfis- og vinnuflæðisrökfræði sem endanlegar ástandsvélar svo eftirlitsaðilar geti skoðað reglurnar og skýrðu frá p95- og p99-töfum frekar en meðaltölum þegar þú réttlætir kerfi fyrir almenningi. Því samningar og úttektir krefjast rökstuddrar, gagnabyggðrar skrár skaltu líta á mælingu, mótun og rótarorsakagreiningu sem afurðir sem gera kerfið útskýranlegt fyrir borgurum og rýnum jafnt.

## Dæmi

**Sprotafyrirtæki.** Tveggja stofnenda greiningarsprotafyrirtæki afhendir mælaborð sem finnst samstundis með handfylli tilraunareikninga, grindast síðan til stöðvunar þegar fyrsti raunverulegi viðskiptavinurinn hleður heils árs gögnum. Annar stofnandinn rökræðir um flækju og kemur auga á fyrirspurn án vísitölu sem gerir fulla töfluskönnun á hverri síðuhleðslu og breytir millisekúndu uppflettingu í sekúndur. Að bæta við réttu vísitölunni lagar það og fljótleg mæling á p95 töf (ekki meðaltalinu, sem faldi hægu halann) staðfestir sigurinn með sönnunargögnum frekar en grun. Vantandi undirstaðan var ekki verkfæri heldur venjan að spyrja hvað fyrirspurn kostar þegar gögn vaxa, og þeir bættu þeirri spurningu við eigin gátlista fyrir sameiningu.

**Stórfyrirtæki.** Afgreiðsluþjónusta verslunarkeðju stóðst hvert próf og kynningu, lét síðan undan á tilboðsdegi. Rótarorsakagreining fann O(n²) lykkju sem bar saman hvern hlut í körfu við hvert vörulistatilboð: ósýnileg með prófakörfum með þremur hlutum, banvæn með raunverulegum körfum og stóru tilboðasetti við hámarksálag. Eldri verkfræðingur sem rökræddi um flækju skipti henni út fyrir hakkatöfluuppflettingu (O(n)) og lítið biðraðalíkan (kafli 11.3) setti örugg samtímamörk. Lagfæringin var eitt gagnagerðarval. Vantandi undirstaðan var venjan að spyrja „hvað kostar þetta þegar gögn vaxa?“ Skipulagsheildin bætti flækjurökhugsun við hönnunarrýnigátlista sinn, svo spurningin sé spurð fyrir atvikið, ekki eftir.

**Hið opinbera.** Bótastofnun sem nútímavæðir eldra kerfi notaði verkfræði- og stærðfræðiundirstöður af ásetningi. Greinendur mótuðu hæfisvinnuflæðið sem endanlega ástandsvél, sem gerði ólögleg ástandsumskipti óframsetjanleg og afhjúpaði jaðartilvik sem gamla kerfið hafði meðhöndlað ósamræmt árum saman. Þeir tilgreindu gögn með mengjafræðilegum venslum til að tryggja einkvæmni og tilvísunarheilindi og völdu staðlaða, vel greinda dulritun, skildu talnafræðina nógu vel til að stærðarsetja lykla rétt og hafna heimasmíðuðu kerfi söluaðila. Þegar afkastaspurningar komu upp mældu þeir með réttri tölfræði og skýrðu frá p95/p99 töfum frekar en meðaltölum og gáfu eftirlitsaðilum rökstudda, gagnabyggða ástæðu til að samþykkja kerfið.

## Viðskiptarök: hvatar, ávöxtun fjárfestingar og heildarkostnaður

Undirstöður borga sig með því að koma í veg fyrir dýrasta flokk bilana: þær sem birtast aðeins í stórum stíl, undir álagi eða undir árás, þegar kerfi er þegar í framleiðslu og lagfæring kostar mest. Eitt forðað rekstrarrof, eitt öryggisatvik sem aldrei gerðist því einhver skildi handahóf og lyklastærðir, eða ein stærðarendurhönnun sem þú þurftir ekki því rétta gagnagerðin var valin fyrirfram: hvert þeirra borgar til baka árs undirstöðufjárfestingu. Ávöxtunin er ekki línuliður. Hún er fjarvera endurtekinna, erfiðra-að-greina hamfara og nærvera teymis sem tekur stöðugt traustar ákvarðanir.

Hvað varðar **heildareignarkostnað** eru undirstöður óvenju ódýrar í viðhaldi, því þær eru þekking en ekki verkfæri eða leyfi, og þær afskrifast hægt. Big-O, líkindi og reynsluaðferðin eru jafn sönn í dag og fyrir áratugum, ólíkt römmum sem skipta út á nokkurra ára fresti. Fjárfestingin fer í ráðningar, leiðsögn og að vernda tíma til náms: að para byrjendur við eldri sem rökræða um flækju upphátt, halda eftirrýni án sakbendingar sem kennir rótarorsakagreiningu og gera mælingu og mótun að eðlilegum hluta hönnunarrýni. Á gervigreindaraðstoðartímanum hækkar ávöxtunin sennilega. Myndaður kóði er fljótur að framleiða og auðveldur að samþykkja án gagnrýni, svo mannleg geta til að dæma traust (er þetta rétt, mun það skala, er það öruggt?) verður af skornum skammti, verðmæt færni. Oft er ódýrasta leiðin til að hækka gæði að hækka undirstöðureiprennandi fólksins sem rýnir vinnuna.

## Andmynstur og gildrur

- **Eingöngu rammaþekking:** reiprennandi í verkfæri án skilnings á vélinni undir, sem skilur engan eftir fær um að greina djúpar bilanir.
- **Að hunsa aukningarfræði:** að afhenda kóða sem virkar á prófagögnum og hrynur á framleiðslugögnum því flækja var aldrei íhuguð.
- **Meðaltöl sem sannleikur:** að tilkynna meðaltöf eða eina viðmiðskeyrslu og missa af halanum sem raunverulega skaðar notendur.
- **Heimasmíðuð dulritun:** að finna upp öryggisfrumstæður án talnafræðilegs skilnings á hvers vegna þær eru brotnar.
- **Einkennalagfæringar:** að plástra næstu villu án rótarorsakagreiningar, svo bilunin endurtekur sig í nýju dulargervi.
- **Farmdýrkunarfínstilling:** að „fínstilla“ án mælingar, oft gera hluti hægari eða breyta aukningarkostnaði ómeðvitað.
- **Gagnrýnislaus gervigreindarsamþykkt:** að sameina sennilegan myndaðan kóða án undirstaðna til að dæma hvort hann sé réttur, skalanlegur eða öruggur.
- **Undirstöður sem „fræðilegar“:** að afgreiða undirstöður sem óviðkomandi „raunverulegri“ vinnu, borga síðan fyrir fjarveru þeirra í framleiðslu.

## Þroskalíkan

- **Stig 1 (Upphaf):** Þekking er aðeins rammadjúp. Stærðar- og öryggisbilanir koma teyminu á óvart, ákvarðanir hvíla á innsæi og tign, gervigreindarúttak er samþykkt gagnrýnislaust og undirstöðubil uppgötvast aðeins eftir atvik.
- **Stig 2 (Þróun):** Sumir eldri verkfræðingar rökræða um flækju, mælingu og réttleika, og fáar góðar venjur birtast í vösum, en þekkingin er sílóuð í einstaklingum, beitt ósamræmt yfir teymi og ekki krafist í rýni.
- **Stig 3 (Stöðlun):** Undirstöðurökhugsun er skjalfest og vænt um alla skipulagsheildina: flækju- og gagnagerðaathuganir, mæling með réttri tölfræði og rótarorsakagreining birtast venjulega í hönnunar- og kóðarýni, studd af skriflegum gátlistum, og eru hluti ráðninga- og vaxtarvæntinga fyrir hvert teymi.
- **Stig 4 (Stjórnun):** Skipulagsheildin mælir eigin undirstöðuheilsu gegn grunnlínum. Hún rekur rýniþekju flækjuspurningarinnar, hlutfall atvika rakin til missirar undirstöðu (óvísitölusett fyrirspurn, veikt handahóf, ótakmörkuð lykkja), hundraðshlutabyggð viðmið borin saman við fyrri útgáfur og gallahlutfall gervigreindaraðstoðaðs kóða sem sleppur, og byggir síðan ákvarðanir um áfram eða stopp á þeim sönnunargögnum frekar en skoðun.
- **Stig 5 (Samhæfing):** Undirstöður eru stöðugt bættar og samþættar um skipulagsheildina. Leiðsögn, innri menntun og mótun eru eðlileg. Mæling og rótarorsakagögn næra aftur í staðla og þjálfun. Undirstöðum er beitt af ásetningi til að meta gervigreindarmyndaða vinnu. Og teymið aðlagast, rökræðir frá frumreglum þegar rammar og ágripanir bregðast.

## Hugmyndir til umræðu

1. Hvenær lak ágripun síðast á teyminu þínu og hafði nokkur undirstöðuþekkinguna til að greina það fljótt?
2. Spyr hönnunar- eða kóðarýni þín í raun „hvað kostar þetta þegar gögnin vaxa?“
3. Hvernig metur þú hvort gervigreindarmyndaður kóði sé réttur, skalanlegur og öruggur og hver í teyminu getur það?
4. Hvar tilkynnir þú meðaltöl þegar hundraðshlutar og dreifni myndu segja raunverulegu söguna?
5. Hver undirstaðan er veikust yfir teymið þitt (flækja, líkindi/tölfræði, netkerfi eða reynsluaðferðin) og hvað myndi það kosta þig?
6. Hvernig viðheldurðu undirstöðuþekkingu þegar sérhæfing dýpkar og verkfæri breytast?

## Helstu atriði

- Undirstöður eru varanlega lagið undir römmum: tölvunarfræði (hvernig vélar reikna), stærðfræði (hvernig á að rökræða nákvæmlega) og verkfræði (hvernig á að mæla og móta).
- **Ágripanir leka**, og undirstöðuþekking er það sem leyfir teymi að greina bilunina þegar þær gera það, venjulega í stórum stíl, undir álagi eða undir árás.
- **Aukningarfræðileg rökhugsun** er áhrifamesta daglega færnin: spyrðu hvað hver lykkja og fyrirspurn kostar þegar gögn vaxa.
- **Líkindi, tölfræði og reynsluaðferðin** breyta skoðun í sönnunargögn: mældu og skýrðu frá dreifingum, ekki bara meðaltölum.
- **Mótaðu og rökræddu fyrir smíði:** endanlegar ástandsvélar, fastayrðingar og lítil afkastagetulíkön grípa galla ódýrt.
- Undirstöður gera **sérhæfingu og gervigreindaraðstoð örugga** með því að gefa teyminu sameiginlega dómgreind til að meta traust. Þær eru ódýrar í viðhaldi og afskrifast hægt.

## Heimildir og frekari lestur

- IEEE Computer Society, *SWEBOK Guide* (v4): Computing Foundations, Mathematical Foundations, and Engineering Foundations knowledge areas.
- Thomas H. Cormen, Charles E. Leiserson, Ronald L. Rivest, Clifford Stein, *Introduction to Algorithms* (CLRS): algorithms, data structures, and complexity.
- Martin Kleppmann, *Designing Data-Intensive Applications*: data structures, databases, distribution, and their trade-offs at scale.
- Andrew S. Tanenbaum, *Modern Operating Systems* and *Computer Networks*: operating-systems and networking foundations.
- Kenneth H. Rosen, *Discrete Mathematics and Its Applications*: logic, sets, graphs, and number theory for computing.
- Bruce Schneier, *Applied Cryptography* / Ferguson, Schneier, Kohno, *Cryptography Engineering*: the number theory and practice of cryptography.
- Andy Oram and Greg Wilson (eds.), *Making Software: What Really Works, and Why We Believe It*: the empirical method in software engineering.
- Peter Deutsch and James Gosling, "The Eight Fallacies of Distributed Computing": networking assumptions that recur in chapter 3.3.
- Wikipedia: "Big O notation," "Finite-state machine," "Five whys," "Public-key cryptography."
