# 1.10 Skilvirkni verkfræði og framleiðni þróunaraðila

## Yfirlit og tilgangur

Sérhver leiðtogi stórrar hugbúnaðarskipulagsheildar spyr fyrr eða síðar útgáfu af sömu spurningu: erum við að verða betri í að smíða hugbúnað og hvernig myndum við vita það? Þessi kafli fjallar um að svara því heiðarlega. **Skilvirkni verkfræði** er hversu vel skipulagsheildin þín breytir verkfræðiátaki í verðmætan, áreiðanlegan hugbúnað. **Framleiðni þróunaraðila** er einstaklings- og teymishlið þess: hve mikið gagnlegt framlag þróunaraðili getur skilað og hve mikið af tíma hans og athygli vinnuumhverfið gefur honum til baka í stað þess að taka frá honum.

Vandinn byrjar um leið og einhver reynir að þjappa þessu í eina tölu. Teldu kóðalínur og fólk skrifar meira af kóða. Teldu sögustig og áætlanir verðbólgna. Teldu commit, sameiningarbeiðnir eða klukkustundir við skrifborðið og þú verðlaunar hreyfingu í stað framvindu. Framleiðni þekkingarstarfsmanns er ekki talning á hlutum. Þróunaraðili sem eyðir tíu þúsund línum af dauðum kóða, eða ver degi í paraforritun svo liðsfélagi forðist rekstrarrof í framleiðslu, hefur unnið framúrskarandi starf sem engin einföld mælieining fangar. Heiðarlega svarið við „hve afkastamikil erum við?“ er fjölvítt, og það lítur á upplifun þróunaraðilans af vinnunni sem raunverulegt merki en ekki mjúkt.

Þetta skiptir meira máli, ekki minna, eftir því sem þú stækkar. Í fyrirtæki með tugi teyma margfaldast lítill núningur (hæg smíð, óáreiðanlegt prófasafn, tveggja daga bið eftir umhverfi) yfir hundruð verkfræðinga í gífurlega tapaða afkastagetu. Hjá hinu opinbera, þar sem ekkert markaðsverð er á afurð, er áhættan „afurðaleikhús“: að mæla skjöl sem framleidd eru eða miða sem lokað er á meðan opinbert virði er ómælt. Markmið þessa kafla er að hjálpa þér að mæla og bæta skilvirkni verkfræðiskipulagsheildarinnar og daglega upplifun þróunaraðila hennar, án þess að spila með, njósna eða raða fólki hvert gegn öðru.

## Meginreglur

- **Framleiðni er fjölvíð.** Engin ein tala fangar hana. Sérhver mælikvarði sem boðinn er fram sem *mælikvarðinn* er rangur.
- **Mældu til að fjarlægja núning, ekki til að raða fólki.** Viðfang mælingarinnar er kerfið, ekki einstaklingurinn.
- **Þríhyrningsmældu.** Sameinaðu hvernig þróunaraðilar segja að vinnan finnist og það sem kerfin skrá í raun.
- **Upplifun þróunaraðilans eru gögn.** Endurgjafarlykkjur, vitræn byrði og flæði eru mælanleg og þess virði að bæta.
- **Gerðu ráð fyrir að sérhver mælikvarði verði spilaður.** Hannaðu gegn lögmáli Goodharts með mörgum víddum og heiðarlegum ásetningi.
- **Tengdu við árangur, varlega.** Skilvirkni ætti að vísa upp til viðskiptavirðis án þess að verða markmið sem spillir.

## Ráðleggingar

### Hafnaðu gildru eins mælikvarða

Fyrsti agi er að neita að nefna eina tölu sem framleiðni. Kóðalínur, commit-talningar, [hraði](https://en.wikipedia.org/wiki/Velocity_(software_development)) sögustiga og skráðar klukkustundir deila öll banvænum galla: þau mæla virkni, ekki virði, og virkni er léttvægt að blása upp. Þetta er [lögmál Goodharts](https://en.wikipedia.org/wiki/Goodhart%27s_law) í verki, meginreglan um að þegar mælikvarði verður markmið hættir hann að vera góður mælikvarði. Hraði var fundinn upp sem eigin spáhjálp teymis. Um leið og stjórnandi ber stig eins teymis saman við annars endurskala teymin hljóðlega áætlanir sínar og talan verður merkingarlaus. Þegar einhver krefst eins framleiðni-KPI skaltu líta á það sem beiðni sem þú verður að móta aftur, ekki uppfylla. Bjóddu lítið jafnvægt safn í staðinn og útskýrðu hvers vegna ein tala myndi blekkja þá.

### Notaðu SPACE til að skipuleggja hvað þú mælir

**SPACE-ramminn** gefur þér víddirnar fimm sem vert er að halda saman: **S**atisfaction og vellíðan (ánægja), **P**erformance (frammistaða), **A**ctivity (virkni), **C**ommunication og samvinna og **E**fficiency og flæði. Tilgangur SPACE er að þú ættir að velja að minnsta kosti nokkrar víddir, aldrei bara eina og aldrei allar úr sama flokki. Virknimælikvarðar (commit, uppsetningar) eru tælandi því auðvelt er að safna þeim, en einir og sér skekkja þeir. Paraðu þá við ánægjumerki og frammistöðumerki svo engin ein vídd verði spiluð án þess að hinar afhjúpi það. Teymi sem afhendir fleiri uppsetningar á meðan ánægja hrynur og bilanahlutfall breytinga hækkar er ekki afkastameira, og jafnvægt safn sýnir þér það strax.

### Líttu á þróunarupplifun sem endurgjafarlykkjur, vitræna byrði og flæði

**Þróunarupplifun (DevEx)** er hvernig það er að vinna verkfræðivinnu hér, og hún er áþreifanlegri en hún hljómar. Hún hvílir á þremur hlutum sem þú getur mælt og bætt. **Endurgjafarlykkjur** eru hve lengi þróunaraðili bíður eftir að læra hvort eitthvað virkaði: staðbundinn smíðatími, lengd prófasafns, afgreiðslutími kóðarýni, uppsetningartími. Hægar lykkjur neyða til samhengisskipta og iðjulausrar biðar. **[Vitræn byrði](https://en.wikipedia.org/wiki/Cognitive_load)**, heildar andlega áreynslan sem verkefni krefst, vex þegar þróunaraðili þarf að halda á of mörgum verkfærum, óskjalfestum kerfum og flæktu ósjálfstæði til að gera einfalda breytingu. **[Flæði](https://en.wikipedia.org/wiki/Flow_(psychology))** er ástand einbeitts, afkastamikils niðursökkvunar sem sundruð dagatöl og stöðugar truflanir eyðileggja. Þegar þú styttir endurgjafarlykkju, fjarlægir hugtak sem þróunaraðili þurfti að halda í höfðinu eða verndar einbeitingartímablokk hefurðu bætt framleiðni á hátt sem engin virknitalning myndi skrá. Þetta er sama DevEx-áhyggjuefni og vettvangsverkfræði þjónar með troðnum slóðum og sjálfsafgreiðslu (kafli 8.4).

### Þríhyrningsmældu skynjun við kerfismælikvarða

Engin ein gagnaheimild er áreiðanleg ein og sér, svo sameinaðu tvær gerðir. **Skynjunargögn** koma frá þróunaraðilum sjálfum gegnum **þróunarupplifunarkönnun**: reglulegan, að mestu nafnlausan spurningalista sem spyr hve öruggir þeir finnast að afhenda, hvar þeir tapa tíma og hvað pirrar þá. **Kerfisgögn** koma frá verkfærunum þínum: tímasetningar leiðslna, rýnitöf, atvikatíðni. Hvort leiðréttir hitt. Kannanir grípa sársauka sem mælitæki missa af, svo sem niðurdrepandi bakvaktaskipulag eða óttaða eldri þjónustu. Kerfismælikvarðar grípa vandamál sem fólk hefur gert eðlileg og hætt að tilkynna. Þegar könnun segir að smíðar séu sársaukafullar og leiðslugögnin staðfesta fimmtán mínútna miðgildis smíði hefurðu forgangsraðaða, rökstudda fjárfestingu. Keyrðu könnunina á stöðugum takti, hafðu hana stutta og lokaðu alltaf lykkjunni með því að sýna hvað breyttist vegna hennar.

### Notaðu DORA sem afhendingarmerki, ekki stigatöflu

Fjórir **[DevOps Research and Assessment](https://en.wikipedia.org/wiki/DevOps_Research_and_Assessment) (DORA)** mælikvarðarnir (uppsetningartíðni, afhendingartími breytinga, bilanahlutfall breytinga og tími til að endurheimta þjónustu) eru sterkur, rannsóknastuddur lestur á afhendingargetu þinni og para hraða við stöðugleika svo hvorugu sé fórnað fyrir hitt. Kafli 11.5 á dýptina um þá og kafli 11.2 nær yfir afhendingarleiðsluna sem þeir mæla. Notaðu þá þar. Hér snýst leiðbeiningin um hvernig þú heldur á þeim. Líttu á DORA sem heilsumerki á teymisstigi sem sýnir hvort afhendingarkerfið þitt er að batna, ekki sem stigatöflu til að raða teymum eða einstaklingum. Um leið og DORA-tölur birtast í frammistöðumati einhvers byrja teymi að skipta upp uppsetningum til að bæta tíðni og fela atvik til að verja bilanahlutfall sitt, og merkið deyr.

### Mældu kerfið, njósnaðu aldrei um einstaklinginn

Þetta er línan sem þú mátt ekki fara yfir. Taktu saman mælikvarða á teymis- og skipulagsheildarstigi og notaðu þá til að finna og fjarlægja núning. Smíðaðu ekki mælaborð sem raða þróunaraðilum eftir commit, klukkustundum eða „framleiðnieinkunnum“ og láttu ekki fjarmælingar einstaklinga mata laun eða stöðuhækkun. Eftirlit eyðileggur sálfræðilega öryggið og traustið sem skilvirk verkfræði veltur á og kennir fólki að fínstilla mælikvarðann í stað vinnunnar. Vöxtur og mat einstaklinga tilheyrir aðskildum, mannlegum búnaði starfsstiga og stjórnandasamtala (kafli 1.3). Skilvirknimæling spyr „hvað hægir á teymum okkar?“ Hún spyr aldrei „hver er hægasti verkfræðingurinn okkar?“

### Ráðstu beint á leiðindavinnu og núning

Þegar þú getur séð hvar tími lekur skaltu eyða honum aftur. Mikið af því sem takmarkar skilvirkni er **leiðindavinna** (toil), handvirk, endurtekin, sjálfvirknivæðanleg vinna sem skalar með vexti og skilar engu varanlegu virði (kafli 9.1). Hægar rýnir eru líka núningur, svo að straumlínulaga kóðarýni (kafli 2.5) með minni breytingum og skýrum væntingum styttir kjarnaendurgjafarlykkju. Troðnar slóðir og sjálfsafgreiðsluvettvangar (kafli 8.4) fjarlægja heila flokka af bið og vitrænni byrði í einu. Taktu líka frá fjárhagsáætlun gegn [tæknilegri skuld](https://en.wikipedia.org/wiki/Technical_debt), uppsöfnuðum kostnaði fyrri flýtileiða sem skattleggur hverja framtíðarbreytingu, því kóðagrunnur sem enginn getur breytt á öruggan hátt er dýpsta framleiðnisökkvi sem til er.

## Málamiðlanir: kostir og gallar

| Nálgun | Kostir | Gallar |
| --- | --- | --- |
| Einn framleiðnimælikvarði (LOC, hraði, commit) | Ódýr, auðveldur, ein tala fyrir leiðtoga | Spilað strax, mælir virkni en ekki virði, tærir traust |
| Jafnvægt safn í SPACE-stíl | Stenst spilun, endurspeglar raunveruleikann | Meiri vinna að safna, erfiðara að draga saman í einni tölu |
| DevEx-könnun (skynjun) | Grípur fundinn sársauka sem mælitæki missa af | Huglæg, þarf traust og eftirfylgni til að haldast heiðarleg |
| Kerfismælikvarðar (DORA, leiðslutímasetningar) | Hlutlægir, samfelldir, erfitt að falsa samtals | Blindir á móral og samhengi, hættulegir ef beitt á einstaklinga |
| Þríhyrningsmæling beggja | Hvor heimild leiðréttir hina, traust | Krefst fjárfestingar í verkfærum og könnunaraga |

Meginspennan er nákvæmni gegn heiðarleika. Ein tala er auðveld að skýra frá og auðveld að spilla. Rík, fjölvíð mynd er heiðarleg en erfiðari að koma á framfæri við önnum kafinn stjórnanda. Leystu það með því að velja lítið jafnvægt safn (nokkrar SPACE-víddir auk könnunar auk DORA sem afhendingarlestur), tilkynna þróun frekar en augnablikstöður og vera skýr um að tölurnar eru til að bæta kerfið, ekki til að gefa fólki einkunn. Þegar forystan vill „eitt graf“ skaltu gefa henni þróun nokkurra viðbótarmerkja og stattu gegn freistingunni að þjappa þeim í falska samsetningu.

## Spurningar til að ræða með teyminu

1. **Ef leiðtogi krefðist einnar framleiðnitölu á morgun, hvað myndirðu gefa honum?** Þessi spurning afhjúpar hvort skipulagsheildin þín skilur gildruna. Heiðarlega svarið er að engin ein tala er örugg og hlutverk þitt er að móta beiðnina í lítið jafnvægt safn sem stenst spilun. Komdu með mælikvarðana sem þú tilkynnir nú þegar og spurðu fyrir hvern þeirra „hvernig gæti snjallt, kaldhæðið teymi blásið þetta upp án þess að vinna betra starf?“ Ef svarið er auðvelt er mælikvarðinn hættulegur um leið og hann verður markmið. Ræddu hvað þú myndir bjóða í staðinn og hvernig þú myndir útskýra fyrir forystunni hvers vegna ein tala myndi blekkja hana til að fínstilla rangan hlut. Gæði þess samtals spá fyrir um hvort mæling hjálpar þér eða spillir.

2. **Hver er hægasta endurgjafarlykkjan þín og hvað kostar hún þig á hverjum degi?** Endurgjafarlykkjur eru þar sem framleiðni lekur hljóðlega: fimmtán mínútna smíði, tveggja daga rýnibið, óáreiðanlegt prófasafn sem tærir traust á hverju grænu merki. Komdu með raunverulegar tölur úr þróunarupplifunarkönnun og úr leiðslumælitækjum þínum og sjáðu hvort skynjaður sársauki og mæld töf eru sammála. Áætlaðu daglegan kostnað með því að margfalda biðina með því hve margir þróunaraðilar lenda í henni og hve oft, og rökin fyrir fjárfestingu færa sig venjulega sjálf. Ákveddu hvaða lykkju á að stytta fyrst og hver á lagfæringuna. Teymi sem getur ekki nefnt hægustu lykkju sína hefur ekki enn byrjað að mæla það sem skiptir mestu máli.

3. **Hvar er mælingin þín í hættu á að finnast eins og eftirlit, og hvernig kemurðu í veg fyrir það?** Munurinn á því að mæla kerfið og að vakta fólk er munurinn á trausti og ótta, og auðvelt er að fara yfir hann án þess að taka eftir. Farðu í gegnum hvert mælaborð og skýrslu og spurðu hvort eitthvert þeirra gæti raðað einstaklingi eða mætt frammistöðumati. Ákveddu skýrt hvað helst samantekið, hvað helst nafnlaust og hvað er bannað, og segðu það síðan opinskátt við teymin sem eru mæld. Í fyrirtækja- og opinberu umhverfi, þar sem eftirlits- og úttektarþrýstingur er sterkur, er freistingin til að kafa niður að einstaklingum stöðug, svo varnarhandriðið verður að vera yfirlýst meginregla, ekki von. Ef þróunaraðilar trúa að tölurnar séu notaðar gegn þeim munu þeir fínstilla tölurnar og sannleikurinn hverfur.

4. **Þegar við spurðum þróunaraðila síðast hvernig vinnan finnst, hvað breyttist vegna þess og komust þeir að því?** Könnun sem skilar engum sýnilegum aðgerðum kennir þróunaraðilum að hætta að svara heiðarlega, svo önnur þögla könnunin dregur til sín færri og bragðdaufari svör en sú fyrsta, og mælitækið sem þú reiðir þig á hrörnar nákvæmlega þegar þú skalar það. Fyrir stóra skipulagsheild safnast sóunin upp: hundruð manna verja tíma í að tilkynna núning, skýrsla fer í umferð og ekkert er afhent. Komdu með þrjár helstu niðurstöður síðustu könnunar, áþreifanlegu vinnuna sem hver kallaði fram og hvernig þú komst niðurstöðunni aftur til fólksins sem vakti máls á henni. Vegðu togið milli þess að bregðast við háværustu kvörtuninni og þeirri útbreiddustu, því þær eru oft ólík vandamál. Í fyrirtækja- og opinberu umhverfi, þar sem könnunarþreyta og samráðsofhleðsla er þegar mikil, skaltu líta á að loka lykkjunni sem stjórnarháttaskuldbindingu: nefndu hver á svarið, birtu hvað breyttist og viðurkenndu að ósvöruð könnun er verri en engin.

5. **Hvernig myndum við bera saman teymi án þess að byggja stigatöflu sem refsar heiðarleika?** Leiðtogar stórra skipulagsheilda vilja eðlilega vita hvaða teymi blómstra og hver sitja föst, en að raða teymum eftir hráum hraða, uppsetningartíðni eða DORA-tölum hunsar að greiðsluteymi undir mikilli reglusetningu og frumgerðateymi á grænu grasi lifa í ólíkum heimum. Sjónarmiðið á móti er raunverulegt: þú þarft að koma auga á teymi í vanda og dreifa því sem virkar, en um leið og samanburður verður að stigatöflu endurskala teymi áætlanir, fela atvik og skipta upp uppsetningum til að verja stöðu sína. Komdu með sértæk dæmi um hvernig teymissamhengi er ólíkt í skipulagsheildinni þinni, ásamt tillögu um að bera hvert teymi saman við eigin þróun í tímans rás frekar en við nágranna sína. Í fyrirtækja- og opinberu umhverfi, þar sem úttektar- og eftirlitsþrýstingur ýtir fast í átt að röðun milli teyma, skaltu koma þér fyrirfram saman um hvað má bera saman, hvað verður aðeins lesið sem þróun á hvert teymi og hver hefur umboð til að hafna ósanngjörnum samanburði.

6. **Hvernig tengjum við skilvirkni við raunverulegan árangur án þess að breyta afhendingarmælikvarða í spillandi markmið?** Skilvirkni sem tengist aldrei upp til virðis lítur út eins og naflaskoðun í augum forystu, en um leið og afhendingarmerki eins og afhendingartími eða uppsetningartíðni verður markmiðið í frammistöðumati fínstilla teymi töluna og yfirgefa árangurinn sem henni var ætlað að vera staðgengill fyrir. Fyrir stóra skipulagsheild er spennan skörp, því stjórnendur vilja hreina línu frá verkfræðiátaki til viðskiptaárangurs á meðan heiðarlega línan er óhrein og seinkuð. Komdu með núverandi árangursmælikvarða þína, afhendingarmerkin sem þú myndir tengja þá við og skýra frásögn af því hvernig hvert gæti verið spilað ef það yrði markmið. Vegðu togið milli einfaldrar sögu sem forystan getur endursagt og sannkallaðrar myndar sem stenst skekkju. Hjá hinu opinbera eða á innri vettvangi án markaðar, þar sem engar tekjur festa virði, vertu tilbúinn að skilgreina árangur sem áreiðanleika þjónustu, hringrásartíma á lagfæringum og opinberan ávinning frekar en hráa virkni, og að verja það val gagnvart eftirlitsaðilum sem kunna að kjósa auðteljanlegri afurðir.

## Sjónarhorn eftir geirum

**Sprotafyrirtæki.** Með handfylli verkfræðinga og lítið fjármagn skaltu sleppa mælaborðum alveg og mæla þá tvo hluti sem hreyfast hraðast: tíu spurninga þróunarupplifunarkönnun og grunntímasetningar leiðslna. Mesta framleiðniáhætta þín er hægt eða óáreiðanlegt prófasafn og stöðug samhengisskipti, svo finndu verstu endurgjafarlykkjuna, styttu hana og haltu áfram. Settu ekki upp mælingaráætlun sem þú hefur engan til að reka, því eitt heiðarlegt samtal um hvar dagurinn lekur slær hvaða verkfæri sem þú þyrftir síðan að viðhalda.

**Lítið fyrirtæki.** Án mælingarsérfræðings og með þröngt fjárhagsáætlun skaltu hallast að því sem núverandi verkfæri þín skrá nú þegar: smíðatíma, rýnitöf og atvikatalningu úr kerfunum sem þú borgar nú þegar fyrir. Keyptu létt könnunartól frekar en að smíða eitt og standastu sölutilboð um einstaklingsframleiðnimælaborð, sem mun kosta þig traust sem þú hefur ekki efni á að missa. Rammaðu allt átakið inn sem að fjarlægja núning fyrir lítið teymi sem hefur ekki efni á að sóa degi nokkurs manns.

**Stórfyrirtæki.** Yfir tugi teyma er verðlaunin endurheimt afkastageta í stórum stíl og hættan er miðlægt mælaborð sem rennur hljóðlega í að raða fólki. Staðlaðu jafnvægt áætlun (ársfjórðungslega DevEx-könnun, nokkrar SPACE-víddir og DORA lesið sem afhendingarþróun á hvert teymi) og stýrðu henni svo að einstaklingsfjarmælingum sé aldrei safnað. Berðu hvert teymi saman við eigin þróun, réttlættu vettvangsfjárfestingu (kafli 8.4) gegn núningnum sem gögnin afhjúpa og gefðu einum ábyrgum eiganda umboð til að hafna hverjum mælikvarða sem yrði að stigatöflu.

**Hið opinbera.** Án markaðsverðs á afurð og með sterkum eftirlitsþrýstingi er togið í átt að afurðaleikhúsi (að telja skjöl og lokaða miða) stöðugt, og togið í átt að því að njósna um nafngreinda einstaklinga undir úttekt er enn sterkara. Mældu árangur og afhendingargetu í staðinn: hve hratt þjónusta afhendir lagfæringu, hve áreiðanleg hún er og hvernig starfsfólk og verktakar upplifa vinnuna gegnum nafnlausa könnun. Mældu opinbera starfsmenn og verktaka á sama kerfisstigi, birtu til hvers mælingin er og vertu tilbúinn að færa rök fyrir löggjafarvaldi að afhendingarþróun á hvert teymi sé heiðarlegri lestur á opinberu virði en nokkur einstaklingseinkunn.

## Dæmi

**Sprotafyrirtæki.** Tuttugu manna sprotafyrirtæki tekur eftir að afhending hefur hægst þótt allir séu uppteknir. Frekar en að setja upp framleiðnimælaborð keyrir verkfræðistjórinn tíu spurninga DevEx-könnun og sækir grunntímasetningar leiðslna. Könnunin og gögnin eru sammála: prófasafnið tekur tuttugu og tvær mínútur og bilar af handahófi, svo fólk lotar breytingum og skiptir um samhengi á meðan það bíður. Teymið ver tveimur vikum í að laga óáreiðanleg próf og samhliða keyra safnið og styttir það í fjórar mínútur. Uppsetningartíðni hækkar sjálfkrafa, ánægja stekkur í næstu könnun og enginn var nokkurn tíma raðaður eða gefin einkunn til að það gerðist.

**Stórfyrirtæki.** Banki með fjörutíu verkfræðiteymi vill réttlæta áframhaldandi fjárfestingu í innri vettvangi sínum. Vettvangshópurinn tekur upp jafnvægt mælingaráætlun: ársfjórðungslega DevEx-könnun yfir öll teymi, merki í SPACE-stíl og DORA-mælikvarða lesna á teymisstigi sem afhendingarheilsuþróun (kafli 11.5). Mikilvægt er að þau bera teymi sanngjarnt saman með því að bera hvert teymi saman við eigin þróun í tímans rás, ekki hvert við annað, því teymissamhengi er gríðarlega ólíkt. Gögnin sýna að teymi á troðnum slóðum (kafli 8.4) taka á móti nýjum verkfræðingum á dögum frekar en vikum og tilkynna mun lægri vitræna byrði. Sú sönnun, sett fram sem endurheimt afkastageta yfir hundruð þróunaraðila, fjármagnar vettvanginn í annað ár. Einstaklingsfjarmælingum er af ásetningi aldrei safnað.

**Hið opinbera.** Alríkisstofnun fyrir stafræna þjónustu verður að sýna löggjafarvaldi að verkfræðiútgjöld hennar skili virði, í umhverfi án markaðsverðs á afurð. Hún hafnar afurðaleikhúsi (að telja skjöl eða lokaða miða) og mælir í staðinn árangur og afhendingargetu: hve hratt þjónusta getur afhent lagfæringu, hve áreiðanleg hún er og hvernig vinnuaflið og verktakar þess upplifa vinnuna gegnum nafnlausa könnun. Afhendingarmerki í DORA-stíl sýna hvort nútímavæðing bætir í raun afköst og stöðugleika, tengd við opinberan árangur frekar en hráa virkni (kafli 11.5). Því mæling raðar aldrei einstaklingum, og því verktakar og opinberir starfsmenn eru mældir á sama kerfisstigi, forðast stofnunin eftirlits- og mórals-vandamálin sem sökkva slíkum átökum og gefur eftirlitsaðilum heiðarlegan lestur á virði.

## Viðskiptarök: hvatar, ávöxtun fjárfestingar og heildarkostnaður

Ávöxtun þess að mæla og bæta skilvirkni er endurheimt afkastageta, og í stórum stíl eru tölurnar miklar. Lítill núningur margfaldast yfir stóra skipulagsheild: tíu mínútna smíði sem hundrað verkfræðingar lenda í nokkrum sinnum á dag eru þúsundir verkfræðistunda á ári í bið. Styttu þá lykkju og þú hefur bætt við umtalsverðri afkastagetu án þess að ráða neinn. Ráðandi ávöxtunin hér er sú sama og í vettvangsverkfræði (kafli 8.4): dýr verkfræðitími færður frá bið og leiðindavinnu yfir í verðmæta vinnu.

Heildareignarkostnaðurinn er hóflegur en raunverulegur. Þú borgar fyrir könnunarverkfæri og aga til að reka þau, fyrir mælitækjabúnað leiðslna og fyrir stjórnunarathygli til að lesa þróun og bregðast við. Stærri áhættan fyrir ávöxtun er að gera mælingu illa. Einn spilaður mælikvarði eða eftirlitsáætlun getur skilað neikvæðri ávöxtun: mánuðir af átaki við að fínstilla tölu á meðan raunverulegur árangur staðnar, auk tæringar á trausti sem gerir hverja framtíðarbreytingu erfiðari. Kostnaðurinn við að mæla alls ekki er dreifður og gríðarlegur: núningur og leiðindavinna safnast ósýnilega upp, eldri verkfræðingar brenna út á forðanlegri sóun og forystan getur ekki sagt hvort fjárfestingar hjálpa. Færðu rök fyrir þessu við forystu sem vogarafl og heiðarleika: lítil, treyst, jafnvægt mælingaráætlun sem finnur hvar stórt vinnuafl tapar tíma og borgar sig mörgum sinnum um leið og þú bregst við fyrstu niðurstöðunni.

## Andmynstur og gildrur

- **Eini framleiðnimælikvarðinn.** Hver ein tala (LOC, hraði, commit, klukkustundir) er spiluð daginn sem hún verður markmið.
- **Að raða einstaklingum.** Stigatöflur og einstaklings„framleiðnieinkunnir“ eyðileggja traust og kenna fólki að fínstilla mælikvarðann.
- **Mæling sem eftirlit.** Nákvæmar einstaklingsfjarmælingar sem mata mat tæra sálfræðilega öryggið sem skilvirk vinna þarf.
- **Kannanir án eftirfylgni.** Að spyrja þróunaraðila hvernig vinnan finnst og breyta síðan engu kennir þeim að hætta að svara heiðarlega.
- **Samanburður á hráum tölum teyma.** Teymissamhengi er ólíkt. Samanburður á hraða eða DORA milli teyma refsar heiðarleika og verðlaunar spilun.
- **Afurðaleikhús.** Að telja framleiddar afurðir (skjöl, miða, afhenta eiginleika) á meðan raunverulegur árangur er ómældur, algengt þar sem ekkert markaðsverð er.
- **DORA í frammistöðumati.** Um leið og afhendingarmælikvarðar gefa fólki einkunn fela teymi atvik og skipta upp uppsetningum og merkið deyr.

## Þroskalíkan

- **Stig 1, Upphaf:** Framleiðni er metin eftir tilfinningu eða einum spilanlegum mælikvarða eins og kóðalínum, hraða eða klukkustundum. Mæling er ad hoc og viðbragðsdrifin, núningur er ósýnilegur, kvartanir eru sögulegar og enginn getur sagt hvort skipulagsheildin er að batna.
- **Stig 2, Þróun:** Sum teymi taka upp grunnvinnubrögð: nokkra mælikvarða, oft virknitalningar, og stöku þróunarupplifunarkönnun. Vinnubrögðin eru ósamkvæm milli teyma, gögnum er safnað en sjaldan brugðist við þeim, hrár samanburður milli teyma læðist inn og engin sameiginleg meginregla ver einstaklinga gegn röðun.
- **Stig 3, Stöðlun:** Jafnvægi mælingaráætlun er skjalfest og beitt um alla skipulagsheildina, með víddum í SPACE-stíl, reglulegri DevEx-könnun og DORA sem afhendingarmerki (kafli 11.5). Mælikvarðar eru samantektir á teymi samkvæmt stefnu, einstaklingar eru aldrei raðaðir og niðurstöður knýja áþreifanlega vinnu við að stytta endurgjafarlykkjur og skera leiðindavinnu (kafli 9.1).
- **Stig 4, Stjórnun:** Áætlunin er mæld og stýrð gegn grunnlínum. Tímar endurgjafarlykkja, könnunareinkunnir og DORA-þróun bera samþykkt markmið og eru rakin í tímans rás. Hvert teymi er borið saman við eigin þróun en ekki nágranna sína. Fjárfestingar í vettvangi og niðurskurði leiðindavinnu eru réttlætt með gögnum fyrir og eftir um endurheimta afkastagetu. Og afturför í hvaða merki sem er kallar fram rýni frekar en að fara óséð.
- **Stig 5, Samhæfing:** Mæling er treyst, rútína og aðlögunarhæf. Skynjunar- og kerfisgögn eru þríhyrningsmæld, þróun nærir stöðugar umbætur, núningur og vitræn byrði er virkt leitað og fjarlægð, mælingasafnið sjálft er endurskoðað eftir því sem skipulagsheildin breytist og skilvirkni er samþætt viðskipta- og opinberum árangri án þess að nokkrum mælikvarða sé leyft að verða spillandi markmið.

## Hugmyndir til umræðu

1. Hverjir af núverandi mælikvörðum þínum gæti kaldhæðið teymi blásið upp án þess að vinna betra starf, og hverju myndirðu skipta þeim út fyrir?
2. Ef þú gætir stytt nákvæmlega eina endurgjafarlykkju yfir alla skipulagsheildina, hver myndi skila mestri endurheimtri afkastagetu?
3. Hvernig myndirðu bera mörg teymi saman sanngjarnt þegar samhengi þeirra er ólíkt, án þess að búa til stigatöflu sem refsar heiðarleika?
4. Hvar er línan milli þess að mæla kerfið og að njósna um einstaklinginn, og hver í skipulagsheildinni þinni hefur umboð til að framfylgja henni?
5. Í umhverfi án markaðsverðs á afurð, svo sem hjá hinu opinbera eða á innri vettvangi, hvernig mælirðu raunverulegt virði frekar en virkni?
6. Hvað myndirðu sýna þróunaraðila til að sanna að könnun þessa ársfjórðungs breytti einhverju?

## Helstu atriði

- Framleiðni verkfræðinga er fjölvíð. Hafnaðu hverri einni tölu (kóðalínum, hraða, commit, klukkustundum) sem *mælikvarðanum*, því lögmál Goodharts tryggir að hún verði spiluð.
- Notaðu **SPACE-rammann** (ánægja og vellíðan, frammistaða, virkni, samskipti og samvinna, skilvirkni og flæði) til að halda saman nokkrum víddum svo engin ein vídd verði spiluð ein og sér.
- **Þróunarupplifun** snýst um endurgjafarlykkjur, vitræna byrði og flæði. Að stytta lykkjur og fjarlægja byrði er raunveruleg framleiðni sem virknitalningar sýna aldrei.
- **Þríhyrningsmældu** skynjunargögn úr DevEx-könnun við kerfisgögn úr verkfærunum þínum. Hvort leiðréttir hitt.
- Líttu á **DORA**-mælikvarða sem afhendingarmerki á teymisstigi, ekki stigatöflu. Dýpt þeirra býr í kafla 11.5 og leiðslan í kafla 11.2.
- Mældu **kerfið**, aldrei einstaklinginn. Taktu saman á teymi, haltu mati í aðskildum mannlegum farvegum kafla 1.3 og láttu mælingu aldrei verða eftirlit.
- Eyddu endurheimtum tíma í að skera leiðindavinnu (kafli 9.1), hraða kóðarýni (kafli 2.5) og troða slóðir (kafli 8.4). Tengdu skilvirkni við viðskiptaárangur án þess að leyfa nokkrum mælikvarða að verða spillandi markmið.

## Heimildir og frekari lestur

- Nicole Forsgren, Margaret-Anne Storey, Chandra Maddila, Thomas Zimmermann, Brian Houck, and Jenna Butler, "The SPACE of Developer Productivity" (*ACM Queue*, 2021): the multidimensional framework.
- Abi Noda, Margaret-Anne Storey, Nicole Forsgren, and Michaela Greiler, "DevEx: What Actually Drives Productivity" (*ACM Queue*, 2023): feedback loops, cognitive load, and flow.
- Nicole Forsgren, Jez Humble, and Gene Kim, *Accelerate: The Science of Lean Software and DevOps* (the DORA metrics and their research basis).
- DORA, *Accelerate State of DevOps Report* (annual): the ongoing research programme behind the four metrics.
- Betsy Beyer, Chris Jones, Jennifer Petoff, and Niall Richard Murphy, eds., *Site Reliability Engineering* (toil and its elimination).
- Matthew Skelton and Manuel Pais, *Team Topologies* (cognitive load as a first-class design concern).
- Mihaly Csikszentmihalyi, *Flow: The Psychology of Optimal Experience* (the origin of flow state).
- Tom DeMarco and Timothy Lister, *Peopleware: Productive Projects and Teams* (focus, interruption, and the human side of productivity).
- Goodhart, C. A. E., "Problems of Monetary Management: The UK Experience" (1975): the origin of Goodhart's law; see also Marilyn Strathern's widely quoted formulation.
- U.S. Government Accountability Office (GAO) guidance on performance measurement: measuring value in non-market public-sector settings.
