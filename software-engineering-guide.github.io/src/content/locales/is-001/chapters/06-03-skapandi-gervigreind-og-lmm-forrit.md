# 6.3 Skapandi gervigreind og forrit byggð á stórum mállíkönum

## Yfirlit og tilgangur

[Skapandi gervigreind](https://en.wikipedia.org/wiki/Generative_artificial_intelligence), og [stór mállíkön](https://en.wikipedia.org/wiki/Large_language_model) (LLM) sér í lagi, geta framleitt lipran texta, kóða, samantektir og uppbyggð gögn út frá fyrirmælum á náttúrulegu máli. Það gerir þau öfluga byggingarkubba fyrir aðstoðarmenn, leit, skjalavinnslu og sjálfvirkni. En þessir styrkleikar fylgja sérstakri áhættumynd. Mállíkön eru líkindabundin. Þau geta framleitt örugg ósannindi ([ofskynjanir](https://en.wikipedia.org/wiki/Hallucination_(artificial_intelligence))). Þau eru næm fyrir því hvernig þú gefur þeim fyrirmæli. Og þau opna nýja árásarfleti eins og [fyrirmælainnspýtingu](https://en.wikipedia.org/wiki/Prompt_injection) (illkvittin fyrirmæli smygluð inn í inntak til að ræna hegðun líkansins). Að smíða áreiðanleg mállíkanaforrit snýst því minna um líkanið og meira um verkfræðina í kringum það: hvernig þú útvegar samhengi, jarðtengir svör í traustri þekkingu, takmarkar úttak og metur gæði.

Fyrir stór teymi kalla mállíkanaforrit á ný mynstur sem eru ólík bæði hefðbundnum hugbúnaði og klassísku vélnámi. Oft er ekkert þjálfunarskref. Hegðun mótast í staðinn af fyrirmælum, sóttu samhengi, verkfæralýsingum og varnarrimlum (keyrslutímaathugunum sem takmarka inntak og úttak líkansins). Það færir verkfræðifyrirhöfnina að samhengisstjórnun, sóknargæðum, samstillingu og mati. Fyrirtæki sem taka upp mállíkön í stórum stíl þurfa sameiginleg mynstur svo hvert teymi uppgötvi ekki sömu bilunarhættina á erfiðan hátt.

Opinberar og regluverkaðar skipulagsheildir standa frammi fyrir viðbótarkröfum. Mállíkan sem býr til tilvitnun í stefnu eða lekur viðkvæmum gögnum er ekki bara galli. Það getur verið lagalegt atvik eða öryggisatvik. Þetta umhverfi krefst jarðtengingar í áreiðanlegum heimildum, strangrar úttaksstaðfestingar, mannlegs eftirlits með afleiddu úttaki og skýrra skráa um hvað kerfið var beðið um og hvað það framleiddi. Tæknin í þessum kafla (sóknarauking, varnarrimlar og ströng mæling) er það sem gerir mállíkön nógu örugg til útsetningar í umhverfi með miklu í húfi. Claude-líkön Anthropic eru einn leiðandi kostur af nokkrum hæfum veitendum. Vinnubrögðin hér gilda óháð því hvaða líkan þú velur.

## Meginreglur

- Jarðtengdu líkanið í traustri þekkingu frekar en að reiða þig á það sem það lagði á minnið.
- Líttu á fyrirmæli og samhengi sem hönnuð, útgáfustýrð gögn, ekki einnota strengi.
- Gerðu ráð fyrir að líkanið geti haft rangt fyrir sér eða verið blekkt. Staðfestu úttak og takmarkaðu aðgerðir.
- Gefðu líkaninu aðeins samhengið og verkfærin sem það þarf, ekkert umfram, til að draga úr villum og árásarfleti.
- Metdu samfellt með óbeintengdum prófasöfnum, beintengdum mælikvörðum og mannlegu mati.
- Hafðu menn í lykkjunni fyrir afleitt úttak.
- Hannaðu fyrir líkanið sem ótraustan íhlut innan trausts kerfis.

## Ráðleggingar

### Hannaðu fyrirmæli og stýrðu samhengi af ásetningi

Líttu á fyrirmæli sem kóða: geymdu þau í útgáfustýringu, rýndu breytingar og prófaðu þau gegn safni dæma. Byggðu hvert fyrirmæli skýrt upp: hlutverk og verk, skorður, sniðkröfur og dæmi þar sem þau hjálpa. Líttu á samhengisgluggann (fasta textalengd sem líkanið getur íhugað í einu) sem knappa auðlind. Taktu með mikilvægustu upplýsingarnar, raðaðu þeim vandlega og fjarlægðu hávaða, því óviðkomandi eða of mikið samhengi rýrir gæði og hækkar kostnað. Fyrir forrit með mörgum umferðum skaltu stýra samtalsástandi skýrt, draga saman eða stytta sögu til að halda þér innan marka en geyma það sem skiptir máli. Kjóstu skýr fyrirmæli og fáskotsdæmi (örfáar útfærðar sýnikennslur í fyrirmælunum) fram yfir íburðarmikil brögð sem brotna um leið og líkani er skipt.

### Jarðtengdu svör með sóknaraukinni myndun (RAG)

Fyrir þekkingarþung verk skaltu sækja viðeigandi skjöl úr traustu safni og leggja þau til líkansins sem samhengi, og segja því að svara aðeins út frá því efni og vitna í heimildir sínar. RAG heldur þekkingu núgildandi án endurþjálfunar, takmarkar svör við samþykkt efni og gerir tilvitnun og sannprófun mögulega. Fjárfestu í sóknargæðum: bútaðu skjöl skynsamlega, veldu [innfellingar](https://en.wikipedia.org/wiki/Word_embedding) (talnavektora sem setja svipaða merkingu nálægt hver annarri) sem henta þínu sviði og athugaðu hvort sóttar málsgreinar innihaldi í raun svarið, því lipurt svar byggt á rangri málsgrein er verra en ekkert svar. Og þegar ekkert viðeigandi finnst skaltu láta kerfið segja það í stað þess að finna upp efni.

### Smíðaðu fulltrúa og verkfærabeitingu af hófsemi

Mállíkön geta kallað á verkfæri (leit, gagnagrunna, reiknivélar, innri API) og verið samsett í fulltrúa sem skipuleggja og framkvæma yfir mörg skref. Þetta bætir við raunverulegri getu, en margfaldar líka áhættu: hvert verkfæri er enn ein leið fyrir rangt eða blekkt líkan til að valda skaða. Skilgreindu verkfæri með nákvæmum skemum, staðfestu hvert viðfang, beittu lágmarksréttindum og krefstu staðfestingar eða samþykkis manns fyrir afleiddar aðgerðir eins og að senda samskipti eða færa fé. Haltu fulltrúalykkjum afmörkuðum, vaktanlegum og stöðvanlegum. Byrjaðu á þröngt afmörkuðum verkfærum með einn tilgang áður en þú seilist í opið sjálfræði.

### Bættu við varnarrimlum og staðfestu úttak

Vefðu líkaninu í lög varna. Á leiðinni inn skaltu sía og greina fyrirmælainnspýtingu, sérstaklega þegar ótraust efni (vefsíður, skjöl notenda) fer inn í samhengið. Á leiðinni út skaltu staðfesta uppbyggingu gegn skema, athuga fullyrðingar gegn heimildum, sía óörugg eða ósamræmanleg efni og hafna eða endurreyna þegar staðfesting bregst. Fyrir uppbyggð úttök skaltu þátta og sannreyna frekar en að treysta sniði líkansins. Láttu aldrei hrátt líkanaúttak ræsa óafturkræfar aðgerðir án staðfestingar. Líttu á varnir gegn ofskynjunum sem kerfiseiginleika sem þú nærð með jarðtengingu, tilvitnun, staðfestingu og mannlegri rýni, ekki eitthvað sem líkanið stýrir sjálft.

### Metdu óbeintengt, beintengt og með mönnum

Smíðaðu matssafn dæmigerðra inntaka með þekkt-góðu eða einkunnarkvarðaskoruðu úttaki og keyrðu það á hverja breytingu á fyrirmælum eða líkani (óbeintengt mat). Mældu raunverulega hegðun í framleiðslu með mælikvörðum eins og verkárangri, stigmögnunarhlutfalli og endurgjöf notenda (beintengt mat). Fyrir huglæg gæði skaltu nota mannlega rýna og, af varúð, líkanabundna einkunnagjöf. Mat er öryggisnetið sem leyfir þér að breyta fyrirmælum og líkönum af öryggi. Án þess flýgurðu blindandi.

## Málamiðlanir: kostir og gallar

| Val | Kostir | Gallar | Best þegar |
|---|---|---|---|
| Hrein fyrirmæli | Einföld, hröð, ódýr í breytingum | Takmörkuð jarðtenging, geta valdið ofskynjunum | Breið verk, lítið í húfi |
| RAG | Núgildandi, jarðtengd, tilvitnanleg | Erfitt að fá sókn rétta | Þekkingarþung, staðreyndaverk |
| Fulltrúar með verkfæri | Öflugir, geta framkvæmt | Stærri árásarflötur, erfiðari í stjórn | Vel afmörkuð sjálfvirkni með varnarrimlum |
| Stærra, sterkara líkan | Betri gæði og rökhugsun | Hærri kostnaður og töf | Flókin verk eða mikið í húfi |
| Minna, ódýrara líkan | Hratt og ódýrt | Veikara á erfiðum verkum | Mikið magn, einföld verk |

Kjarnaspennan er geta gegn stjórn og kostnaði. Meira sjálfræði og stærri líkön skila meira gildi, en krefjast fleiri varnarrimla, meira mats og meiri peninga. Jarðtenging með RAG bætir traustverðleika á kostnað sóknarverkfræði. Rétta jafnvægið ræðst af því sem er í húfi: forrit með miklu í húfi hallast að jarðtengingu, staðfestingu og mannlegu eftirliti, jafnvel þótt það kosti meira.

## Spurningar til að ræða með teyminu

1. **Hvaða nákvæmni- og jarðtengingarviðmið þarf mállíkanseiginleiki að standast áður en hann mætir almenningi og hver skrifar undir?** Lipurt svar sem vitnar í ranga heimild eða finnur upp stefnu er verra en ekkert svar, og hjá hinu opinbera er uppspunnin tilvitnun lagalegt atvik, ekki galli. Fyrir stórt teymi stöðvar skýrt viðmið að hver hópur setji eigin einkaþröskuld eftir tilfinningu. Komdu með skilgreiningu þína á „nógu jarðtengt“: hvort sérhver fullyrðing verði að rekjast til sótts, staðfests heimildarefnis, hvort kerfið verði að neita þegar sókn kemur tómhent og hvað andstæðingamatssafnið þitt nær í raun yfir. Merkið til að fylgjast með er hvort nokkur geti nú sent fyrirmælabreytingu beint til notenda án afturfarakeyrslu. Ef það sem er í húfi er lagalegt eða öryggistengt ætti svarið að leiða áhættumesta úttakið gegnum mannlegan rýnanda með raunverulegt vald fyrir útgáfu.

2. **Hverjir af mállíkanseiginleikum okkar eru í leyni fulltrúar og hefur hvert verkfæri fengið lágmarksréttindi og mannlegt hlið á óafturkræfum aðgerðum?** Sérhver eiginleiki sem leyfir líkaninu að kalla á verkfæri eða framkvæma yfir mörg skref hefur farið inn á fulltrúasvæði og hvert verkfæri er enn ein leið fyrir rangt eða blekkt líkan til að valda skaða. Fyrir fyrirtæki sem tengja mállíkön við innri API afhjúpar þessi spurning áhættu sem merkið „einfaldur aðstoðarmaður“ felur. Komdu með skrá yfir hvert verkfæri sem líkanið getur kallað á, viðfangastaðfestingu þess, réttindaumfang og hvaða aðgerðir (að senda samskipti, færa fé, breyta skrám) krefjast staðfestingar. Ræddu hvort fulltrúalykkjur séu afmarkaðar, vaktanlegar og stöðvanlegar. Svarið ætti að herða umfang og bæta við samþykkishliðum manna alls staðar þar sem afleidd eða óafturkræf aðgerð er nú aðgengileg án þeirra.

3. **Hvernig myndum við vita innan dags að sóknargæði okkar hafi fallið, þar sem öruggt svar byggt á rangri málsgrein lítur vel út?** RAG gerir svör traustverð aðeins þegar sókn dregur í raun fram málsgreinina sem inniheldur svarið, og sókn rotnar hljóðlega þegar skjöl breytast, bútar úreldast eða innfellingar reka frá þínu sviði. Því líkanið skrifar enn lipurt yfir slæmt samhengi kvarta notendur kannski ekki fyrr en traust er þegar glatað. Komdu með núverandi mælingar á sóknartöf og endurheimt, hvernig þú athugar hvort sóttar málsgreinar innihaldi í raun svarið og hvernig ferskleiki vísitölunnar heldur í við skjalabreytingar. Fyrir útsetningar með miklu í húfi eða opinberar skaltu ræða að skrá sóttar heimildir fyrir úttekt svo þú getir rakið slæmt svar til slæmu málsgreinarinnar. Ef þú hefur alls ekkert sóknarmat ertu að jarðtengja á trú.

4. **Meðhöndlum við fyrirmæli, samhengi og matssöfn sem útgáfustýrð, rýnd gögn, eða sem strengi á víð og dreif í minnisbókum og spjallskrám?** Þegar fyrirmæli dreifast yfir teymi án útgáfustýringar og eru tvítekin berst lagfæring á einum stað aldrei til hinna og enginn getur endurtekið hvað kerfið var beðið um síðasta ársfjórðung. Fyrir stórt teymi eru sameiginleg fyrirmælaskrá og afturfarasafn sem keyrir á hverja breytingu það sem leyfir þér að skipta um líkan eða breyta fyrirmælum án þess að brjóta eiginleika tveimur teymum fjær hljóðlega. Togið á móti er hraði: verkfræðingar endurtaka hraðast þegar þeir líma fyrirmæli og afhenda, svo komdu þér saman um hvar línan liggur milli fljótra tilrauna og alls sem snertir notendur. Komdu með hvar fyrirmæli þín búa í raun í dag, hvort matssafn hliðar breytingar og hvernig þú útgáfustýrir sóknarsafninu við hlið fyrirmælanna. Í fyrirtækja- og opinberu umhverfi skaltu bæta við úttektarkröfunni: þú gætir þurft að sýna nákvæmlega hvaða fyrirmæli og hvaða heimildir framleiddu tiltekið úttak mánuðum síðar, og fyrirmæli sem þú getur ekki endurbyggt eru skrá sem þú getur ekki varið.

5. **Þegar magn vex, hvernig munum við stýra ályktunarkostnaði án þess að rýra gæði hljóðlega og hver á ákvörðunina um líkanaval?** Heildareignarkostnaður mállíkanseiginleika ræðst af ályktun á kall og kostnaður sem lítur léttvægur út í tilraunaverkefni safnast hratt í framleiðslustærð, sem freistar teyma til að falla hljóðlega niður í veikara líkan og vona að enginn taki eftir gæðafallinu. Fyrir stóra skipulagsheild skilar það bæði óvæntum reikningum og ósamkvæmum gæðum að láta hvert teymi velja líkön og kostnaðarmörk eftir tilfinningu. Raunverulega málamiðlunin er geta gegn kostnaði og töf: stærra líkan rökhugsar betur á erfiðum verkum, minna er ódýrara og hraðara á einföldum, og skyndiminni, leiðarval og sóknarumfang hreyfa öll töluna. Komdu með kostnað á leyst verk, gæði eftir líkanaþrepi á matssafni þínu og hvar fyrirmæla- eða samhengisþemba blæs út tókenaútgjöld. Í fjárhagsáætlunargerð fyrirtækja og hins opinbera skaltu nefna hver samþykkir líkanavalið og útgjaldaþakið, því kostnaðarliður sem enginn á er einn sem enginn stýrir þegar umferð þrefaldast.

6. **Hvaða viðkvæm gögn geta náð til líkansins, hvert fara þau og getum við sannað að þau hafi haldist innan marka?** Sérhver fyrirmæli, sótt skjal og verkfæraniðurstaða getur borið persónuleg eða trúnaðargögn inn í líkanið og, með hýstum veitanda, út fyrir jaðar þinn, og leki hér er lagalegt atvik eða öryggisatvik, ekki gallamiði. Fyrir stórt teymi sem tengir mállíkön við innri kerfi felst áhættan í lögnunum: sóknarsafn sem inniheldur skrár sem tiltekinn notandi ætti aldrei að sjá, eða skrár sem fanga hrá inntök. Spennan er geta gegn afhjúpun, þar sem útstrikun og þröngt umfang geta sljóvgað eiginleikann sem þú ert að smíða. Komdu með gagnaflæðikort af því sem fer inn í samhengið, varðveislu- og þjálfunarskilmála veitandans og hvernig þú strikar út, afmarkar og skráir viðkvæma reiti. Í regluverkuðu og opinberu umhverfi skaltu tengja þetta við gagnabúsetureglur, varðveisluskyldur skjala og samningsbundnar takmarkanir á því hvernig seljandi má nota gögn þín, því eftirlit sem þú getur ekki sýnt fram á er eftirlit sem þú hefur ekki.

## Sjónarhorn eftir geirum

**Sprotafyrirtæki.** Afhentu einn þröngan mállíkanseiginleika sem snertir kjarnagildi þitt, smíðaðan á hýstu líkani með sókn yfir þitt eigið efni, og haltu fyrirmælum í git á bak við þunnt viðmót svo þú getir skipt um veitanda. Keyrðu litla matsskrá með raunverulegum spurningum fyrir hverja breytingu, síaðu límdan notendatexta til að sljóvga fyrirmælainnspýtingu og settu hart þak á mánaðarleg útgjöld. Stattu gegn fulltrúum og eigin rekstri: ótakmörkuð verkfæralykkja sem þú getur ekki haft eftirlit með er skuld, ekki sýnikennsla.

**Lítið fyrirtæki.** Þú hefur líklega engan vélnámssérfræðing, svo keyptu mállíkanseiginleika innbyggða í verkfæri sem þú notar nú þegar frekar en að manna smíði. Rammaðu áhættuna sem einfalda spurningu: hvar myndi öruggt rangt svar kosta þig viðskiptavin og hver athugar úttakið áður en það fer út. Kjóstu seljendur sem sýna heimildir sínar, leyfa þér að hafa mann í lykkjunni og gera auðvelt að slökkva á gervigreindinni þegar hún hegðar sér illa.

**Stórfyrirtæki.** Vandinn er stærð yfir mörg teymi: birtu sameiginleg mynstur fyrir RAG, varnarrimla og verkfæraskemu, auk sameiginlegs matsramma og fyrirmælaskrár svo hver hópur hætti að uppgötva sömu bilunarhættina aftur. Fjárhagsáætlaðu ályktunarkostnað og mannlega rýni skýrt, staðlaðu viðmótslagið svo líkön haldist skiptanleg og stýrðu fulltrúum miðlægt með lágmarksréttindum, afmörkuðum lykkjum og úttektarskráningu. Stýrðu mállíkanseiginleikum sem eignasafni með mælikvörðum og drápsviðmiðum, ekki dreifingu tilraunaverkefna.

**Hið opinbera.** Gagnsæi, innkaupareglur og ábyrgð móta hvert val. Jarðtengdu strangt í samþykktum heimildum með tilvitnunum, neitaðu þegar sókn kemur tómhent og bannaðu líkaninu að fullyrða lög sem það getur ekki vitnað í. Haltu ábyrgum embættismanni sem rýnir afleitt úttak, skráðu inntök og sóttar heimildir fyrir úttekt, keyrðu andstæðingamatssafn fyrir hverja útgáfu og krefstu upplýsingagjafar um takmarkanir líkansins og gagnameðhöndlunarskilmála í samningnum.

## Dæmi

**Sprotafyrirtæki.** Þriggja manna sprotafyrirtæki í þróunarverkfærum bætti við spjallhjálp yfir eigin skjölum svo notendur hættu að senda tölvupósta með grunnspurningum. Það notaði RAG svo hvert svar vitnaði í tiltekna skjalasíðu, bauð líkaninu að segja „ég er ekki viss, hér er hver getur svarað“ þegar sókn kom tómhent og hélt fyrirmælum sínum í git. Fyrir hverja breytingu keyrði það fyrirmælin gegn lítilli skrá raunverulegra notendaspurninga til að grípa afturfarir og það síaði texta sem notendur límdu inn til að sljóvga fyrirmælainnspýtingu. Hjálpin afgreiddi algengu spurningarnar og sendi hljóðlega afganginn í sameiginlegt pósthólf stofnendanna.

**Stórfyrirtæki.** Hugbúnaðarfyrirtæki smíðaði innri stuðningsaðstoðarmann yfir vöruskjölun sína. Það notaði [RAG](https://en.wikipedia.org/wiki/Retrieval-augmented_generation) svo svör vitni í tilteknar skjalasíður, sagði líkaninu að segja „ég veit það ekki“ þegar sókn brást og staðfesti að sérhver tilvitnuð heimild væri til í raun. Fyrirmæli voru útgáfustýrð og prófuð gegn safni raunverulegra stuðningsspurninga á hverri breytingu. Aðstoðarmaðurinn beindi frá venjulegum beiðnum og stigmagnaði allt lágtraust til mannlegra fulltrúa, á meðan beintengdir mælikvarðar röktu úrlausnar- og leiðréttingarhlutföll.

**Hið opinbera.** Opinber stofnun setti upp mállíkansaðstoðarmann til að hjálpa starfsfólki að semja svör við fyrirspurnum borgara. Jarðtengingin var ströng: líkanið gat aðeins samið svör út frá samþykktri leiðsögn með tilvitnunum og var bannað að fullyrða stefnu sem var ekki í sóttum heimildum. Ábyrgur embættismaður rýndi hvert uppkast áður en það fór út. Inntakssíun varði gegn fyrirmælainnspýtingu úr skjölum sem borgarar lögðu fram, úttök voru skráð fyrir úttekt og matssafn andstæðinga- og jaðartilvika keyrði fyrir hverja útgáfu til að staðfesta að kerfið neitaði að giska á lögfræðileg málefni.

## Viðskiptarök: hvatar, ávöxtun fjárfestingar og heildarkostnaður

Mállíkanaforrit skila ávöxtun með því að sjálfvirknivæða tungumálaþunga vinnu: að svara spurningum, draga saman skjöl, semja efni og draga út uppbyggingu úr óuppbyggðum texta. Gildið birtist sem afstýrðir miðar, hraðari ritun, minni handvirk rýni og ný sjálfsafgreiðslugeta. Því oft er ekkert þjálfunarskref er tími til fyrsta gildis stuttur, sem er mikið aðdráttarafl.

Heildareignarkostnaður ræðst hins vegar af viðvarandi ályktunarkostnaði, sóknarinnviðum, matsleiðslum, varnarrimlakerfum og mannlegri rýni. Kostnaður á kall safnast hratt í stærð og óvaktað forrit getur rekið í óörugga eða dýra hegðun. Kostnaður þess að taka ekki upp er að dragast aftur úr í þjónustugæðum og framleiðni starfsfólks. Kostnaður þess að taka upp af kæruleysi er opinbert ofskynjunaratvik eða gagnaleki. Færðu rök við forystu með því að para áþreifanlegt framleiðnimarkmið við áþreifanlega öryggis- og matsáætlun og með því að fjárhagsáætla varnarrimlana og mannlega eftirlitið sem halda gildinu varanlegu.

## Andmynstur og gildrur

- **Að treysta lipru úttaki.** Að rugla öruggum, vel rituðum texta saman við réttan texta.
- **RAG án sóknarmats.** Að gera ráð fyrir að sókn virki og athuga aldrei hvort hún dragi fram réttar málsgreinar.
- **Blinda á fyrirmælainnspýtingu.** Að mata fyrirmæli með ótraustu efni án varna.
- **Ótakmarkaðir fulltrúar.** Að leyfa fulltrúum að grípa til afleiddra aðgerða án marka eða samþykkis manns.
- **Enginn matsrammi.** Að breyta fyrirmælum og líkönum eftir tilfinningu, án afturfaraprófana.
- **Fyrirmælaofvöxtur.** Fyrirmæli á víð og dreif, óútgáfustýrð og tvítekin yfir teymi.
- **Ofsjálfvirkni.** Að fjarlægja menn úr ákvörðunum sem bera lagalegt eða öryggislegt vægi.

## Þroskalíkan

1. **Upphaf.** Ad hoc fyrirmæli í einangruðum verkefnum. Engin jarðtenging, varnarrimlar eða mat. Fyrirmæli búa þar sem einhver límdi þau og ofskynjanir uppgötvast í framleiðslu.
2. **Þróun.** Sum teymi bæta við RAG og útgáfustýringu fyrirmæla, grunnúttaksstaðfestingu og litlu handvirku matssafni, en vinnubrögð eru ólík eftir teymum og hvíla á einstökum áhugamönnum frekar en sameiginlegum væntingum.
3. **Stöðlun.** Skjalfest mynstur fyrir RAG, varnarrimla, verkfæraskemu og útgáfustýringu fyrirmæla eru framfylgd um skipulagsheildina. Sjálfvirkt óbeintengt mat keyrir á hverja breytingu á fyrirmælum eða líkani og ferli með miklu í húfi bera beintengda mælikvarða og mannlega rýni.
4. **Stjórnun.** Eignasafnið er mælt gegn grunnlínum: sóknarendurheimt, ofskynjana- og neitunarhlutföll, þekja innspýtingarvarna, kostnaður og töf á kall og stigmögnunar- og leiðréttingarhlutföll eru rakin á mælaborðum. Útgáfuhlið og drápsviðmið virkjast á sönnunargögnum en ekki skoðun og afturfarakeyrsla stöðvar hverja breytingu sem hreyfir mælikvarða í ranga átt.
5. **Samhæfing.** Samfellt óbeintengt og beintengt mat er tengt viðskiptaniðurstöðum. Innspýtingarvarnir, fulltrúar og jarðtenging eru stýrð og vaktanleg og skipulagsheildin leggur reglulega niður, stillir upp á nýtt og endurmarkar mállíkanseiginleika og skiptir um líkön þegar gæði, kostnaður og áhætta breytast.

## Hugmyndir til umræðu

- Hvernig ákveðurðu hvaða úttök krefjast mannlegrar rýni fyrir notkun?
- Hver er staðall þinn fyrir „nógu jarðtengt“ áður en svar má sýna notendum?
- Hvernig ver þú kerfið gegn fyrirmælainnspýtingu þegar ótraust efni verður að fara inn í samhengið?
- Hvenær er fulltrúi aukinnar áhættu sinnar virði gagnvart einfaldari hönnun með einu kalli?
- Hvernig metur þú huglæg gæði í stærð án þess að reiða þig um of á líkanabundna einkunnagjöf?
- Hvernig heldurðu fyrirmælum viðhaldanlegum og samræmdum yfir mörg teymi?

## Helstu atriði

- Áreiðanleiki kemur af verkfræðinni í kringum líkanið: samhengi, jarðtengingu, varnarrimlum og mati.
- RAG jarðtengir svör í traustum heimildum og gerir tilvitnun og sannprófun mögulega.
- Líttu á líkanið sem ótraustan íhlut. Staðfestu úttök og takmarkaðu verkfærabeitingu.
- Gefðu fulltrúum lágmarksréttindi, afmarkaðar lykkjur og samþykki manna fyrir afleiddum aðgerðum.
- Metdu óbeintengt, beintengt og með mönnum samfellt. Það er það sem gerir breytingar öruggar.

## Heimildir og frekari lestur

- Patrick Lewis et al., *Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks*.
- Jason Wei et al., *Chain-of-Thought Prompting Elicits Reasoning in Large Language Models*.
- OWASP Foundation, *OWASP Top 10 for Large Language Model Applications*.
- Chip Huyen, *AI Engineering: Building Applications with Foundation Models*.
- Anthropic, *Building Effective Agents* (engineering guidance).
- Louis-François Bouchard and Louie Peters, *Building LLMs for Production*.
