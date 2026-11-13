# 10.7 Lipur aðferðafræði

## Yfirlit og tilgangur

[Lipur aðferðafræði](https://en.wikipedia.org/wiki/Agile_software_development) (Agile) er hugarfar til að afhenda hugbúnað (og verðmæti) í endurtekningum, stigvaxandi og í nánu samstarfi við fólkið sem mun nota hann. Hún var fest í sessi í *Manifesto for Agile Software Development* árið 2001 og er best skilin ekki sem ferli heldur sem safn **gilda og meginreglna**: forgangsraða einstaklingum og samskiptum, virkum hugbúnaði, samstarfi við viðskiptavini og viðbrögðum við breytingum, fram yfir áætlanaþung, samningaþung og skjalaþung sjálfgildin sem komu á undan. Rammaverk eins og [Scrum](https://en.wikipedia.org/wiki/Scrum_(software_development)), [Kanban](https://en.wikipedia.org/wiki/Kanban_(development)) og [öfgaforritun](https://en.wikipedia.org/wiki/Extreme_programming) (XP) eru *útfærslur* á því hugarfari. Þau eru gagnlegir upphafspunktar en ekki hugarfarið sjálft. Þessi kafli er viðbót við kafla 1.4 (vinnulag, sem kannar aðferðir víðtækt) með því að fara djúpt í lipra aðferðafræði sérstaklega.

Lipur aðferðafræði er knúin af sama afli og lífgar uppgötvunar- og afhendingarleiðslurnar (kaflar 11.1–11.2): kröfur til hugbúnaðar eru *uppgötvaðar*, ekki fullþekktar fyrirfram, og heimurinn breytist hraðar en löng áætlun getur tekið við. Allt-í-einu afhending þar sem allt er skipulagt fyrst skilar ítrekað kerfum sem eru sein, yfir fjárhagsáætlun og, verst af öllu, röng, því allt námið berst í lokin, þegar dýrast er að bregðast við því. Kjarnaveðmál lipurrar aðferðafræði er einfalt: stuttar lotur við að smíða raunverulegan, virkan hugbúnað og fá raunverulega endurgjöf slá langar lotur ágiskana. Þegar vel er gert dregur hún úr áhættu samfellt frekar en að fresta henni.

Fyrir stór teymi, fyrirtæki og hið opinbera er lipur aðferðafræði bæði öflug og oft afbökuð. Fyrirtæki taka hana upp yfir hundruð teyma og skera hana oft niður í helgisið („við höldum stöðufundi núna“) án þess að breyta því hvernig ákvarðanir eru teknar eða hvernig verðmæti er mælt. Hið opinbera hefur tekið lipra aðferðafræði upp af ásetningi, því endurtekin, notendamiðuð afhending dregur sannanlega úr áhættu stórra opinberra áætlana: U.S. Digital Service og *Digital Services Playbook* þess, Government Digital Service og Service Standard í Bretlandi og lipar innkaupaumbætur spruttu allt að hluta til af áberandi [fossamistökum](https://en.wikipedia.org/wiki/Waterfall_model). Ávinningurinn er raunverulegur. Það er bilunarhátturinn „lipur aðeins að nafninu til“ líka.

## Meginreglur

- **Settu fjögur gildi stefnuskrárinnar** (fólk, virkan hugbúnað, samstarf og viðbragðsfýsi) fram yfir ferlaafurðir.
- **Afhentu virkan hugbúnað oft** í litlum áföngum. Virkur hugbúnaður er helsti mælikvarði framvindu.
- **Fagnaðu breytingum**, jafnvel seint. Aðlögunarhæfni er eiginleiki, ekki bilun.
- **Byggðu í kringum áhugasöm, valdefld, sjálfskipulögð teymi.**
- **Eigðu samstarf stöðugt við notendur og hagsmunaaðila.**
- **Hugleiddu og bættu** á reglulegum takti.
- **Haltu mannúðlegum hraða** og tæknilegri afburðagetu: hraði án handverks hrynur.

## Ráðleggingar

### Festu þig í gildum og meginreglum, ekki seremóníum

Mikilvægasta ráðleggingin í lipri aðferðafræði er að leiða með *hvers vegna*. Teymi sem heldur daglegan stöðufund, lotuyfirferð og afturlit, en skuldbindur sig enn til fasts umfangs á fastri dagsetningu, felur slæmar fréttir og breytir aldrei áætluninni, er ekki lipurt. Það er foss með fundum. Notaðu tólf meginreglurnar sem gátlista fyrir raunverulega lipurð. Afhendir þú virkan hugbúnað oft? Getur þú fagnað breytingu í næstu lotu? Ákveður teymið *hvernig* vinnan er unnin? Er viðskiptavinurinn í raun í lykkjunni? Ef seremóníurnar framleiða ekki þessar niðurstöður skaltu laga niðurstöðurnar, ekki seremóníurnar.

### Veldu rammaverk sem upphafspunkt, ekki trúarbrögð

Veldu rammaverk sem hentar vinnunni og aðlagaðu það:

- **Scrum:** tímaramma-sprettir, forgangsraðaður verkefnalisti og skilgreind hlutverk (vörueigandi, scrum-stjóri, forritarar). Gott fyrir eiginleikaafhendingu með skýrum vörueiganda. Veikt þegar vinnan er mjög truflanadrifin.
- **Kanban:** samfellt flæði með skýrum takmörkunum á vinnu í gangi og togkerfi. Gott fyrir þjónustu, rekstur og óútreiknanlega komu (og beint grundað í flæði og biðraðakenningu, sjá kafla 11.2, 11.3). Að takmarka vinnu í gangi styttir leiðtíma ([lögmál Littles](https://en.wikipedia.org/wiki/Little%27s_law)).
- **Öfgaforritun (XP):** verkfræðivenjur þar á meðal [prófdrifin þróun](https://en.wikipedia.org/wiki/Test-driven_development), [paraforritun](https://en.wikipedia.org/wiki/Pair_programming), [samfelld samþætting](https://en.wikipedia.org/wiki/Continuous_integration), endurbætur á kóða, litlar útgáfur. Tæknilegi burðarásinn sem gerir hvaða rammaverk sem er sjálfbært.
- **Scrumban** og blöndur: raunsæjar samsetningar sem mörg þroskuð teymi enda á.

Rammaverk eru vinnupallar. Haltu því sem hjálpar, slepptu því sem gerir það ekki og láttu „rammaverkið segir svo“ aldrei yfirskrifa „meginreglurnar segja hvers vegna.“

### Krefstu tæknilegrar afburðagetu

Lipur aðferðafræði án verkfræðiaga hrörnar fljótt í hraða framleiðslu óviðhaldanlegs kóða, „dökkan scrum“, þar sem teymi spretta sér í tjörugryfju galla og [tæknilegrar skuldar](https://en.wikipedia.org/wiki/Technical_debt). XP-venjurnar eru ekki valkvæðir aukahlutir. Samfelld samþætting (kafli 8.1), sjálfvirkar prófanir (kafli 2.4), endurbætur á kóða, stofnþróun (kafli 2.6) og hrein hönnun (kafli 2.2) eru það sem leyfir teymi að halda áfram að breyta hugbúnaði ódýrt, sem er öll forsenda lipurðar. Sjálfbær hraði skiptir máli af sömu ástæðu: útbrunnin teymi geta ekki viðhaldið gæðum eða viðbragðsfýsi.

### Skalaðu með varúð og kjóstu frekar að minnka

Skölunarrammaverk, svo sem SAFe (Scaled Agile Framework), LeSS, Nexus og Scrum@Scale, samhæfa mörg teymi að sameiginlegum markmiðum. Þau geta hjálpað, en þau bera viðvörun (í samhljómi við kafla 1.4): þung skölunarrammaverk innleiða oft aftur nákvæmlega boðvaldsstýringuna og áætlanaþungan aukakostnað sem lipur aðferðafræði átti að fjarlægja. Áður en þú tekur upp stórt rammaverk skaltu reyna *að minnka*. Skipuleggðu í kringum sjálfstæð, straumstillt teymi með skýru eignarhaldi og lágmarks þverteymisósjálfstæði (kafli 1.2), svo þú þurfir minna samhæfingarvélaverk í fyrsta lagi. Þar sem samhæfing er sannarlega nauðsynleg skaltu bæta við léttustu byggingu sem virkar og tengja hana við niðurstöður (OKR, markmið og lykilniðurstöður, kafli 11.1), ekki afurðir.

### Gerðu lipurð raunverulega í fyrirtækjum og hjá hinu opinbera

Aðlögunarhæf afhending og stofnanaskorður geta sambúið, en það krefst yfirvegaðrar hönnunar:

- **Blendingsstjórnarhættir:** aðlögunarhæfur afhendingarkjarni innan spádrifinnar fjármögnunar-/reglufylgniskeljar (kafli 10.6), svo endurtekning fullnægi eftirliti frekar en að berjast við það.
- **Lipur innkaup:** einingaskiptir, niðurstöðumiðaðir samningar og styttri áfangar í stað eins megasamnings með föstu umfangi. Þetta er þar sem lipur aðferðafræði hjá hinu opinbera tekst oftast eða mistekst.
- **Reglufylgni jafnóðum:** byggðu úttekt, aðgengi (kafli 5.3) og öryggi (kafli 4.1) inn í áfangann með sjálfvirkni og hæfnisföllum (sjálfvirkum athugunum sem sannreyna stöðugt arkitektúr- og gæðaeiginleika, kaflar 8.5, 1.6), ekki seinbúnu hliði.
- **Raunverulegur aðgangur að notendum:** erfiðast og mikilvægast. Teymi þurfa raunverulegt samband við borgara eða viðskiptavini, sem innkaupa- og öryggisreglur hindra oft.

### Bættu stöðugt og og meintu það

Afturlitið er vél umbóta í lipri aðferðafræði og er einskis virði ef það framleiðir enga breytingu. Haltu afturlit sem skapa fáar áþreifanlegar aðgerðir í eigu einhvers og kláraðu þær í raun fyrir það næsta. Mældu niðurstöður (færði breytingin lykilniðurstöðu? sjá kafla 11.1) og flæði (styttast leiðtímar? sjá kafla 11.2, 11.3). Mældu ekki hraða (velocity): hann er afkastagetumerki sem verður að lygi um leið og þú notar hann sem framleiðnimarkmið.

## Málamiðlanir: kostir og gallar

| Ákvörðun | Kostir | Gallar |
|---|---|---|
| **Lipur (aðlögunarhæf)** | Hröð endurgjöf. Tekur við breytingum. Snemmbúið, samfellt verðmæti | Erfiðara að festa umfang/kostnað fyrirfram. Krefst virks viðskiptavinar og aga |
| **Foss (spádrifinn)** | Fyrirsjáanlegt umfang. Hentar samningum/úttektum | Seinbúin endurgjöf. Allt-í-einu áhætta. Illa hæfur fyrir óvissar kröfur |
| **Scrum** | Taktur, hlutverk, einbeiting. Víða skilið | Seremóníukostnaður. Á erfitt með truflanadrifna vinnu |
| **Kanban** | Flæði, WIP-takmarkanir, sveigjanlegt. Frábært fyrir rekstur | Minni bygging. Krefst aga til að halda takmörkunum |
| **Þung skölun (SAFe)** | Samhæfir mörg teymi. Kunnuglegt stórum skipulagsheildum | Getur innleitt boðvaldsstýringu aftur. Seremóníuþungt |
| **Minnkun / sjálfræði teyma** | Minni samhæfingarkostnaður. Hraðari teymi | Krefst lítillar tengingar og sterks vettvangs/eignarhalds |

Skilgreinandi spennan er **aðlögunarhæfni á móti fyrirsjáanleika** og klassíski misskilningurinn er að lipur aðferðafræði þýði „engin áætlun.“ Það gerir hún ekki. Hún þýðir að skipuleggja stöðugt og skuldbinda sig til *niðurstaðna og takts* á meðan *umfang* sveigist. Hin endurtekna gildran er að líta á lipra aðferðafræði sem *aðeins* ferli (seremóníur) eða *aðeins* verkfræði (XP). Hún þarf hvort tveggja.

## Spurningar til að ræða með teyminu

1. **Eru samningar ykkar í fyrirtækja- eða opinberu samhengi einingaskiptir og niðurstöðumiðaðir, eða er afhending læst inni í einum megasamningi með föstu umfangi?** Lipur innkaup eru þar sem lipurð hjá hinu opinbera tekst oftast eða mistekst, því einn föstu verði, föstu umfangi samningur þvingar fram foss sama hvað afhendingarteymin kalla fundi sína. Einingaskiptir, niðurstöðumiðaðir samningar með styttri áföngum leyfa umfangi að sveigjast í verðmætan kjarna innan fastrar fjármögnunar, sem er nákvæmlega mynstrið á bak við nútíma opinbera sigra og mótefnið við fyrri allt-í-einu mistökum. Komdu með sönnunargögn: líttu á núverandi samninga ykkar og spyrðu hvort seljandi sé greiddur fyrir sýndan virkan hugbúnað eða fyrir fast umfang samþykkt fyrir árum. Svarið ætti að móta hvernig þið skipuleggið næstu innkaup langtum meira en hvaða rammaverk teymin ykkar taka upp innanhúss. Þú getur ekki verið aðlögunarhæf(ur) í afhendingu á meðan samningur þinn skyldar fjarlæga, allt-eða-ekkert opnun.

2. **Eru úttekt, aðgengi og öryggi innbyggð í hvern áfanga með sjálfvirkni, eða boltuð á sem seinbúið hlið?** Reglufylgni jafnóðum er það sem leyfir aðlögunarhæfri afhendingu að sambúa við stofnanaskorður: byggðu athuganirnar inn í áfangann með sjálfvirkni og hæfnisföllum frekar en að geyma þær fyrir æði fyrir útgáfu. Seinbúið reglufylgnihlið innleiðir aftur allt-í-einu áhættuna sem lipur aðferðafræði er til að fjarlægja, því dýru vandamálin koma í ljós í lokin þegar erfiðast er að laga þau. Komdu með sönnunargögn: fyrir síðasta áfanga ykkar, athugaðu hvort aðgengi, öryggi og úttektarsönnunargögn voru staðfest sjálfvirkt í leiðslunni eða frestað til handvirkrar rýni fyrir opnun. Svarið ætti að ýta þessum eiginleikum inn í samfelldar sjálfvirkar athuganir, svo eftirliti sé fullnægt með athöfninni að smíða frekar en aðskildum áfanga. Þetta er líka það sem heldur regluverkuðu áætlunarverki heiðarlegu milli úttekta frekar en aðeins vikurnar fyrir eina.

3. **Hvernig veistu hvort teymi ykkar spretta sér í tæknilega skuld og hvað ver sjálfbæran hraða undir opnunarþrýstingi?** Lipur aðferðafræði án verkfræðiaga hrörnar í dökkan scrum, þar sem teymi spretta hratt í tjörugryfju galla og óviðhaldanlegs kóða, og útbrunnin teymi geta ekki viðhaldið gæðum eða viðbragðsfýsi. XP-venjurnar (samfelld samþætting, sjálfvirkar prófanir, endurbætur á kóða, stofnþróun) eru það sem leyfir teymi að halda áfram að breyta hugbúnaði ódýrt, sem er öll forsenda lipurðar, svo þær eru ekki valkvæðir aukahlutir til að skipta burt þegar dagsetning nálgast. Komdu með sönnunargögn: fylgstu með hvort leiðtímar styttast eða lengjast, hvort gallahlutföll hækka og hvort teymið vinnur hljóðlega lengur til að ná hverjum spretti. Svarið ætti að gera tæknilega afburðagetu og mannúðlegan hraða óumsemjanleg, því hraði keyptur með fórn handverks hrynur innan fárra lota. Mældu flæði og niðurstöður, aldrei hraða sem markmið, því um leið og þú gerir afkastagetumerki að framleiðnimarkmiði verður það að lygi.

4. **Áður en þú seilist í þungt skölunarrammaverk, hefur þú reynt að draga úr þverteymisósjálfstæðum sem skapa þörfina til að samhæfa í fyrsta lagi?** Þetta skiptir mestu máli fyrir stóra skipulagsheild, því viðbragðið þegar mörg teymi verða að senda saman er að kaupa rammaverk eins og SAFe, LeSS eða Scrum@Scale og þung skölunarvélaverk smygla oft aftur inn boðvaldsstýringunni og áætlanaþunga aukakostnaðinum sem lipur aðferðafræði er til að fjarlægja. Samkeppnissjónarmiðið er raunverulegt: sumt samhæfing er sannarlega nauðsynleg og að minnka í sjálfstæð, straumstillt teymi krefst lítillar tengingar, skýrs eignarhalds og vettvangs nógu þroskaðs til að teymi geti afgreitt sig sjálf, sem þú hefur kannski ekki enn. Komdu með sönnunargögn í umræðuna: kortleggðu raunveruleg ósjálfstæði sem neyða teymi til að bíða hvert eftir öðru og spyrðu hve mörg myndu lifa yfirvegaða endurhönnun teymismarka og þjónustueignarhalds. Í fyrirtækja- og opinberum áætlunum, þar sem skipurit tuga teyma er algengt, er heiðarlega spurningin hvort þú sért að bæta við samhæfingarbyggingu til að bæta upp arkitektúr og teymishönnun sem þú gætir í staðinn einfaldað, svo þú þurfir alls minni samhæfingu.

5. **Hafa teymi ykkar raunverulegt, endurtekið samband við borgarana eða viðskiptavinina sem þau smíða fyrir, eða berst endurgjöf síuð gegnum staðgengla?** Samstarf við viðskiptavini er eitt fjögurra gilda stefnuskrárinnar og lotur án raunverulegs notendasambands fínstilla hljóðlega rangt, sem er dýrasta bilunin sem lipur aðferðafræði á að koma í veg fyrir. Spennan er að beinn aðgangur er erfiður að skipuleggja í stærð og er oft hindraður af nákvæmlega innkaupa-, persónuverndar- og öryggisreglunum sem stórar og opinberar skipulagsheildir verða að virða, svo auðvelda leiðin er að setja staðgengil í staðinn: viðskiptagreinanda, hagsmunaaðilanefnd eða rannsóknarkynningu síðasta ársfjórðungs. Komdu með sönnunargögn: fyrir síðustu áfanga ykkar, teldu hve margir voru staðfestir með raunverulegum notanda sem notar hugbúnaðinn og hve margir hvíldu á skoðun einhvers á því hvað notendur vilja. Fyrir opinbera þjónustu skaltu bæta við hvort nothæfisprófanir ykkar náðu til fólksins sem verst er sett, þar á meðal notenda hjálpartækni og þeirra með lítið stafrænt sjálfstraust, því opinber þjónusta sem virkar aðeins fyrir örugga meirihlutann hefur brugðist ábyrgðarskyldu sinni jafnvel þótt hver seremónía hafi gengið samkvæmt áætlun.

6. **Eru teymi ykkar fjármögnuð og stýrð í kringum niðurstöður og takt, eða í kringum fast umfang sem þvingar hljóðlega fram foss á bak við seremóníurnar?** Þetta er munurinn á raunverulegri lipurð og falskri lipurð og hann er ákveðinn fyrir ofan teymið, í því hvernig fé er losað og hvernig árangri er skýrt frá, ekki í því hvort stöðufundir gerast. Samkeppnistogið er að fjármála-, eignasafns- og eftirlitsdeildir eru smíðaðar til að samþykkja fast umfang gegn fastri fjárhagsáætlun árum fyrirfram og að biðja þær að fjármagna niðurstöðu með sveigjanlegu umfangi finnst eins og tap á stjórn sem þær munu standa gegn. Komdu með sönnunargögn: raktu hvernig núverandi verkefni var fjármagnað og hverju það skýrir frá og athugaðu hvort teymi eru mæld á afhentum niðurstöðum og flæði eða á sögupunktum og fylgni við umfang samþykkt fyrir löngu. Í fyrirtækja- og opinberu umhverfi skaltu tengja þetta beint við fjármögnunar- og reglufylgniskelina (kafli 10.6): ef féð er skuldbundið til fjarlægrar, allt-eða-ekkert opnunar geta teymin ekki verið aðlögunarhæf sama hve dyggilega þau framkvæma helgisiðina og lagfæringin tilheyrir stjórnarháttalíkaninu frekar en afhendingarteymunum.

## Sjónarhorn eftir geirum

**Sprotafyrirtæki.** Lifðu gildin og slepptu rammaverkadeilunni. Sendu virka sneið til raunverulegra notenda í hverri viku, sittu nógu nærri stofnendum og fyrstu viðskiptavinum til að endurgjöf berist daglega og fagnaðu stefnubreytingu um leið og sönnunargögn segja að núverandi veðmál sé rangt. Knappasta auðlind þín er athygli verkfræðinga, svo verndaðu tæknilega afburðagetu (samfellda samþættingu, sjálfvirkar prófanir, stofnþróun) jafnvel undir opnunarþrýstingi, því sá agi er það sem heldur þér færum um að snúa ódýrt í næstu viku.

**Lítið fyrirtæki.** Án lipurðarþjálfara og með þröngt fjárhagsáætlun skaltu líta á lipra aðferðafræði sem handfylli venja frekar en umbreytingaráætlun sem þú mannar: stutta vikulega lotu, sýnilegt borð með takmörkunum á vinnu í gangi og eina áþreifanlega umbót á viku sem þú klárar í raun. Hallaðu þér að Kanban, sem þarf litla seremóníu og passar truflanadrifinni vinnu, og taktu upp venjurnar sem eru innbyggðar í verkfærin sem þú kaupir nú þegar í stað þess að koma upp þungu ferli. Dæmdu fyrirhöfnina eftir því hvort þú sendir gagnlegan hugbúnað til viðskiptavina oftar, ekki eftir því hve náið þú hermir eftir Scrum.

**Stórfyrirtæki.** Vandinn er að samhæfa mörg teymi án þess að innleiða boðvaldsstýringu aftur. Kjóstu að minnka, það er að draga úr þverteymisósjálfstæðum gegnum straumstillta teymishönnun og traustan vettvang, áður en þú tekur upp þungt skölunarrammaverk. Fjármagnaðu og stýrðu í kringum niðurstöður (OKR) og takt frekar en fast árlegt umfang og sögupunkta, gerðu XP-stíl verkfræðivenjur óumsemjanlegar yfir teymi og stýrðu afhendingu sem safni með flæðismælikvörðum og niðurstöðumælingum svo hópar bæti sig á sönnunargögnum frekar en helgisið.

**Hið opinbera.** Innkaupareglur, gagnsæi og opinber ábyrgð móta hvert val. Byggðu einingaskipta, niðurstöðumiðaða samninga með styttri áföngum í stað eins megasamnings með föstu umfangi, því lipur innkaup eru þar sem lipurð hjá hinu opinbera tekst oftast eða mistekst. Byggðu úttekt, aðgengi og öryggi inn í hvern áfanga með sjálfvirkni svo eftirliti sé fullnægt með athöfninni að smíða, birtu framvindu og sönnunargögn um opinbert verðmæti til eftirlitsaðila og berstu fyrir raunverulegum aðgangi að borgurum (þar á meðal notendum hjálpartækni) í hverri lotu, því það er skorðan sem oftast er samið burt.

## Dæmi

**Sprotafyrirtæki.** Fimm manna sprotafyrirtæki sleppir seremóníudeilunni og lifir gildi lipurrar aðferðafræði beint. Það sendir virka sneið til raunverulegra notenda í hverri viku, situr nógu nærri stofnendum og fyrstu viðskiptavinum til að endurgjöf berist daglega og fagnar stefnubreytingu í næstu viku þegar sönnunargögn segja að núverandi veðmál sé rangt. Teymið neitar að fórna tæknilegri afburðagetu fyrir hraða, svo samfelld samþætting, sjálfvirkar prófanir og stofnþróun eru óumsemjanleg jafnvel undir opnunarþrýstingi og hvert föstudagsafturlit framleiðir eina áþreifanlega breytingu sem teymið klárar í raun fyrir það næsta. Það rekur aldrei hraða sem markmið, heldur mælir hvort send vinna færði virkjun og hvort leiðtímar styttast.

**Stórfyrirtæki.** 60 teyma umbreytingarátak fjarskiptafyrirtækis „gerir Scrum“ í fyrstu en sér enga framför. Teymi fá enn fast árlegt umfang og skýra frá hraða. Endurræsing einbeitir sér aftur að meginreglum: ársfjórðungsleg OKR koma í stað eiginleikaskipana, teymi eru endurskipulögð til að draga úr þverteymisósjálfstæðum (minnkun) og XP-venjur (samfelld samþætting, prófdrifin þróun, stofnþróun) eru gerðar óumsemjanlegar. Leiðtímar styttast, gallar fækka og, mikilvægast, reksturinn byrjar að mæla niðurstöður frekar en sögupunkta, sem tengir lipra afhendingu við uppgötvunarleiðsluna (kafli 11.1).

**Hið opinbera.** Stafrænt þjónustuteymi endurbyggir bótaumsókn fyrir borgara með lipurri aðferðafræði innan blendingsstjórnarskeljar: tveggja vikna áfanga sem afhenda virkan, notendaprófaðan hugbúnað, aðgengi og öryggi innbyggt í hvern áfanga og einingaskipt innkaup í stað eins föstu verðs samnings. Raunverulegar nothæfisprófanir með borgurum (þar á meðal notendum hjálpartækni) í hverri lotu grípa vandamál sem gamla fossferlið hefði sent frá sér. Áætlunin afhendir nothæfa þjónustu snemma og sýnir mælanlegt opinbert verðmæti fyrir eftirlitsaðilum. Þetta er mynstrið á bak við nútíma opinbera sigra og mótefnið við fyrri allt-í-einu mistökum.

## Viðskiptarök: hvatar, ávöxtun fjárfestingar og heildarkostnaður

Ávöxtun lipurrar aðferðafræði kemur af **áhættulækkun og hraðari verðmætanýtingu**. Með því að afhenda virkan hugbúnað snemma og oft breyta teymi óvissu í sönnunargögn samfellt og grípa röngu-hlutina og mun-ekki-virka bilanir á meðan þær eru ódýrar, í stað fjarlægrar, dýrrar opnunar. Rannsóknirnar á bak við nútíma afhendingu (DORA, [DevOps Research and Assessment](https://en.wikipedia.org/wiki/DevOps_Research_and_Assessment), niðurstöðurnar í kafla 11.2) sýna að venjurnar sem lipur aðferðafræði stuðlar að (litlar lotur, tíðar útgáfur, hröð endurgjöf, tæknileg afburðageta) fylgja betri afhendingu *og* stöðugleika *og* frammistöðu skipulagsheildar. Snemmbúnir áfangar byrja líka að skila verðmæti fyrr, sem bætir tímasetningu og heildarstærð ávöxtunar miðað við allt-í-einu útgáfu sem skilar engu fyrr en í lokin.

Hvað **[heildareignarkostnað](https://en.wikipedia.org/wiki/Total_cost_of_ownership)** varðar lækkar lipur aðferðafræði kostnað breytinga yfir líftíma kerfis, að því gefnu að verkfræðiaginn sé raunverulegur. Ríkjandi áhætta hennar er *fölsk lipurð*: seremónía án meginreglu eða handverks, sem bætir við fundakostnaði án þess að skila neinum ávinningi og getur verið verri en heiðarlegur foss. Viðskiptarökin eru því skilyrt. Ávöxtunin er há þegar þú tekur upp lipra aðferðafræði sem hugarfar-auk-verkfræði og nánast núll (eða neikvæð) þegar þú tekur hana upp sem helgisið. Færðu rök við forystu með því að ramma lipra aðferðafræði sem samfellda áhættulækkun og niðurstöðumælingu, ekki sem „að fara hraðar“, og með því að krefjast þess að fjárfestingin feli í sér tæknilegar venjur, ekki bara nýja fundi.

## Andmynstur og gildrur

- **Fölsk / farmdýrkunar-lipurð:** seremóníur framkvæmdar á meðan ákvarðanir, fjármögnun og hugarfar eru áfram foss.
- **Hraði sem framleiðni:** að breyta afkastagetuáætlun í markmið, sem spillir henni ([lögmál Goodharts](https://en.wikipedia.org/wiki/Goodhart%27s_law)).
- **Dökkur scrum:** að spretta án tæknilegrar afburðagetu í óviðhaldanlegan, gallaðan kóða.
- **Afturlit án breytinga:** íhugun sem framleiðir engar kláraðar aðgerðir.
- **Fast umfang *og* dagsetning *og* kostnaður:** að kalla það lipurt á meðan gæði taka hljóðlega á sig þrýstinginn.
- **Fjarverandi viðskiptavinur:** engin raunveruleg notendaendurgjöf, svo lotur fínstilla rangt.
- **Rammaverkadýrkun:** „SAFe/Scrum segir svo“ yfirskrifar meginreglurnar og dómgreind teymisins.
- **Skala fyrir minnkun:** að bæta við þungum samhæfingarrammaverkum í stað þess að draga úr ósjálfstæðum.

## Þroskalíkan

- **Stig 1, Upphaf.** Foss eða ad hoc afhending. Allt-í-einu útgáfur. Vinnan er viðbragðsdrifin og áætlanaþung, án endurtekinnar endurgjafar og án sameiginlegs skilnings á hvers vegna lipur aðferðafræði gæti hjálpað.
- **Stig 2, Þróun.** Fá teymi taka upp seremóníur lipurrar aðferðafræði (stöðufundi, spretti, afturlit), en vinnubrögð eru ósamræmd um skipulagsheildina: hugarfar og verkfræðiagi dragast aftur úr helgisiðunum, hraði er meðhöndlaður sem afurð og umfang er enn fast fyrirfram.
- **Stig 3, Stöðlun.** Gildi og meginreglur stýra vinnu í raun um skipulagsheildina, skjalfest og væntanlegt af hverju teymi: XP-stíl tæknileg afburðageta (samfelld samþætting, sjálfvirkar prófanir, endurbætur á kóða, stofnþróun) er staðalvenja, teymi skipuleggja sig sjálf, viðskiptavinir eru virkir í hverri lotu og afturlit framleiða áþreifanlega, klárða breytingu.
- **Stig 4, Stjórnun.** Afhending er mæld og stýrð gegn grunnlínum: teymi rekja leiðtíma, útsetningartíðni, bilunarhlutfall breytinga og flóttahlutfall galla (DORA-stíl flæðis- og stöðugleikamælikvarðana), samhliða niðurstöðumælingum tengdum lykilniðurstöðum, og bera hvern saman við þekkta grunnlínu. Afturlitsaðgerðir eru raktar til loka, sjálfbærs-hraða merki svo sem yfirvinna og kulnun eru vöktuð og hraði er aldrei notaður sem framleiðnimarkmið. Fara eða ekki-fara ákvarðanir hvíla á þessum sönnunargögnum frekar en skoðun.
- **Stig 5, Samhæfing.** Aðlögunarhæf afhending er samþætt við viðskipta- og áhættuáætlanagerð um skipulagsheildina: niðurstöður (OKR) knýja fjármögnun og takt, lítil-ósjálfstæðis teymishönnun (minnkun) lágmarkar samhæfingarkostnað og blendingsstjórnarhættir fullnægja eftirliti án þess að hægja á afhendingu. Stöðugar umbætur eru menningarlegar frekar en seremóníulegar og skipulagsheildin endurskilgreinir umfang, endurskipuleggur teymi og endurjafnar safn sitt reglulega þegar sönnunargögn og áhættumynd breytast.

## Hugmyndir til umræðu

1. Metðu teymi þitt gegn tólf meginreglum lipurrar aðferðafræði: hvar eruð þið lipur í seremóníu en ekki í innihaldi?
2. Er hraði notaður á teymi þínu sem spá eða sem markmið og hvað hefur það gert við hegðun?
3. Hvaða XP-tæknivenjur vantar og hvernig birtist skortur þeirra sem gallar eða hæg breyting?
4. Gætir þú dregið úr þverteymisósjálfstæðum í stað þess að taka upp skölunarrammaverk?
5. Hvað kemur sérstaklega í veg fyrir raunverulegan notendaaðgang í hverri lotu í þínu samhengi og hvernig gætir þú fjarlægt það?
6. Hver var síðasta áþreifanlega breytingin sem afturlit framleiddi í raun?

## Helstu atriði

- Lipur aðferðafræði er **hugarfar gilda og meginreglna**, ekki safn seremónía. Rammaverk eru upphafspunktar, ekki markmiðið.
- Afhentu **virkan hugbúnað oft**, fagnaðu breytingum og valdefldu **sjálfskipulögð teymi**.
- **Tæknileg afburðageta (XP-venjur) er óumsemjanleg.** Lipurð án hennar verður hröð hnignun.
- **Skalaðu með varúð. Kjóstu að minnka.** Dragðu úr ósjálfstæðum áður en þú bætir við samhæfingarrammaverkum.
- Í fyrirtækjum/hjá hinu opinbera skaltu sameina **aðlögunarhæfa afhendingu með blendingsstjórnarháttum og lipurum innkaupum** og berjast fyrir raunverulegum notendaaðgangi.
- Ávöxtunin er **samfelld áhættulækkun og fyrra verðmæti**, en aðeins þegar lipur aðferðafræði er raunveruleg, ekki helgisiður. Sjá kafla 1.4, 11.1, 11.2, 10.6 og 11.3.

## Heimildir og frekari lestur

- Kent Beck et al., *Manifesto for Agile Software Development* and its twelve principles (agilemanifesto.org, 2001).
- Ken Schwaber and Jeff Sutherland, *The Scrum Guide*.
- Kent Beck, *Extreme Programming Explained: Embrace Change*.
- David J. Anderson, *Kanban: Successful Evolutionary Change for Your Technology Business*.
- Mike Cohn, *User Stories Applied* and *Succeeding with Agile*.
- Jeff Patton, *User Story Mapping*.
- Stephen Denning, *The Age of Agile*.
- Matthew Skelton and Manuel Pais, *Team Topologies* (team design and descaling).
- Nicole Forsgren, Jez Humble, Gene Kim, *Accelerate* (evidence for agile/DevOps practices).
- U.S. Digital Service, *Digital Services Playbook*; UK Government, *Government Service Standard*.
