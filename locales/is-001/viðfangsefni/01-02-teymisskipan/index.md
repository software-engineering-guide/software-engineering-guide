# 1.2 Teymisskipan og skipulagshönnun

## Yfirlit og tilgangur

Hvernig þú skiptir fólki í teymi ákvarðar hvaða hugbúnað þú getur smíðað og hversu hratt. Þetta er ekki líking. Þetta er næstum vélræn afleiðing sem þekkist sem [lögmál Conways](https://en.wikipedia.org/wiki/Conway%27s_law): skipulagsheildir hanna kerfi sem endurspegla samskiptaform þeirra sjálfra. Ef þrjú teymi smíða [þýðanda](https://en.wikipedia.org/wiki/Compiler) færðu þriggja umferða þýðanda. Ef greiðslurökfræðin þín er skipt milli framendateymis, bakendateymis og gagnagrunnsteymis þarf hver greiðslubreyting þríhliða samhæfingu. Fyrir litla skipulagsheild er það viðráðanlegt. Fyrir stóra verður lögun skipuritsins ráðandi skorða á verkfræðina, arkitektúrinn, afhendingarhraðann og gæðin. Að hanna teymisskipan er því fyrsta flokks verkfræðistarf, ekki eftiráhugsun starfsmannasviðs.

Teymisskipan (team topologies) gefur þér ásetningsbundinn orðaforða fyrir þessa hönnun. Í stað þess að láta uppbyggingu safnast upp fyrir tilviljun með skipulagsbreytingum og fjölgun starfsmanna velja þroskuð skipulagsheildir teymisgerðir og samskiptaform af ásetningi og endurskoða þessi val eftir því sem kerfið og reksturinn þróast. Markmiðið er að halda [vitrænni byrði](https://en.wikipedia.org/wiki/Cognitive_load) hvers teymis lágri, heildarmagninu sem teymi þarf að halda í höfðinu til að vera skilvirkt, svo teymi geti átt sitt svið frá enda til enda og afhent stöðugt flæði virðis án þess að bíða stöðugt eftir öðrum.

Fyrir fyrirtæki og hið opinbera er þessi agi úrslitaatriði. Stórar skipulagsheildir teygja sig eðlilega í djúp stigveldi, sameiginlega þjónustu með löngum biðröðum og yfirfærslukeðjur sem breyta tveggja daga breytingu í tveggja mánaða verkefni. Hið opinbera bætir við innkaupamörkum, verktakateymum og lögboðnum [aðskilnaði starfa](https://en.wikipedia.org/wiki/Separation_of_duties) sem sundra eignarhaldi enn frekar. Útfærð teymisskipan er hvernig þessar skipulagsheildir endurheimta flæði: samræma teymi við virðisstrauma, smíða vettvang sem dregur úr vitrænni byrði og velja samskiptamynstur sem gera ósjálfstæði sýnilegt og ásetningsbundið í stað falins og stöðugs.

## Meginreglur

- Lögmál Conways er óumflýjanlegt. Hannaðu teymi til að passa við hugbúnaðarverkfræðina sem þú vilt („öfuga hreyfingin“).
- Fínstilltu fyrir vitræna byrði teymisins, ekki hámarksnýtingu einstaklinga.
- Kjóstu straumtengd teymi sem eiga sneið af virði frá enda til enda.
- Vettvangar eru til að draga úr vitrænni byrði straumtengdra teyma, ekki til að vera hliðverðir.
- Hafðu samskipti teyma skýr og fá: samvinnu, X-sem-þjónustu eða stuðning.
- Lágmarkaðu ósjálfstæði. Sérhver yfirfærsla milli teyma er biðröð og áhætta.
- Teymisskipan er lifandi hönnun sem verður að þróast eftir því sem kerfið og reksturinn breytast.

## Ráðleggingar

### Notaðu fjórar grunnteymisgerðir

Teymisskipan skilgreinir fjórar teymisgerðir sem ná yfir flestar þarfir. Straumtengd teymi eru sjálfgefin: hvert á samfellt flæði vinnu fyrir tiltekna vöru, þjónustu eða notendaferð, frá enda til enda. Vettvangsteymi bjóða innri vörur (reikniafl, uppsetningu, gagnaleiðslur, auðkenni) sem straumtengd teymi nota í sjálfsafgreiðslu, sem lækkar vitræna byrði þeirra. Stuðningsteymi eru sérfræðingar (prófanir, öryggi, sýnileiki) sem þjálfa straumtengd teymi í að byggja upp getu og stíga svo til baka. Teymi flókinna undirkerfa eiga íhluti sem krefjast djúprar sérfræðiþekkingar (verðlagningarvél, [myndkóðari](https://en.wikipedia.org/wiki/Video_codec), dulritunareining), þar sem ekki er skynsamlegt að hvert teymi búi yfir þeirri þekkingu. Flest teymin þín ættu að vera straumtengd. Hinar þrjár gerðirnar eru til að styðja þau.

### Beittu öfugri Conway-hreyfingu

Þar sem hugbúnaður endurspeglar uppbyggingu skipulagsheildarinnar skaltu móta teymin þannig að þau framleiði hugbúnaðinn sem þú vilt. Viltu lauslega tengdar þjónustur með skýrum mörkum? Búðu til lauslega tengd teymi með skýrum eignarmörkum. Viltu greiðslugetu sem er afhent á eigin áætlun? Myndaðu greiðsluteymi sem á hana frá fremri enda til aftari. Berðust ekki við lögmál Conways með hetjulegri samhæfingu. Teiknaðu teymismörkin upp á nýtt svo að arkitektúrinn sem þú vilt verði leið minnstu mótstöðu.

### Stýrðu vitrænni byrði með skýrum hætti

Teymi getur aðeins náð tökum á svo miklu. Vitræn byrði nær yfir flækjustig sviðsins, tæknina, rekstrarbyrðina og breidd hagsmunaaðila. Þegar teymi á of margar ótengdar þjónustur hrynja bæði gæði og hraði. Afmarkaðu því ábyrgð hvers teymis við svið sem það getur raunverulega náð tökum á og notaðu vettvanga og stuðningsteymi til að taka ódýra flækju af borðinu. Haltu teymum í um fimm til níu manns: nógu litlum til að eiga auðvelt með samskipti og, ef svo má segja, til að nægja nokkrar pítsur.

### Veldu samskiptaform af ásetningi

Takmarkaðu samskipti teyma við þrjú form. Samvinna er náin, hánæm vinna milli tveggja teyma í ákveðinn tíma. Hún er öflug til uppgötvunar en dýr, svo hafðu hana tímabundna. X-sem-þjónusta er hrein veitenda-/notendatengsl með vel skilgreindu viðmóti, tilvalin fyrir vettvangsnotkun í stórum stíl. Stuðningur er þegar eitt teymi hjálpar öðru að læra, sem er það sem stuðningsteymi gera. Nefndu formið fyrir hvert mikilvægt tengsl milli teyma og lestu langvarandi samvinnu milli sömu tveggja teyma sem merki um að mörk þeirra séu á röngum stað.

### Veldu rekstrarlíkan fyrir þverlægar aðgerðir

Öryggi, gögn, hönnun og sambærilegar greinar má skipuleggja á þrjá vegu: miðlægt (eitt teymi á það fyrir alla), sambandsskipað (sérfræðingar í hlutastarfi innan teyma, samhæfðir í gegnum gildi) eða innfellt (sérstakur sérfræðingur innan hvers straumtengds teymis). Miðlægt gefur þér samræmi og dýpt en verður flöskuháls. Innfellt gefur þér hraða og samhengi en hættu á ósamræmi og tvíverknaði. Sambandsskipað (oft hub-and-spoke eða [starfsvettvangslíkan](https://en.wikipedia.org/wiki/Community_of_practice)) liggur milli þessara tveggja. Veldu fyrir hverja aðgerð og hvert umfang. Flestar stórar skipulagsheildir lenda á sambandsskipuðu fyrir þessar greinar, með lítinn miðlægan kjarna sem setur staðla.

### Fjárfestu í innri opnum hugbúnaði (inner-source)

[Inner-source](https://en.wikipedia.org/wiki/Inner_source) flytur samvinnumynstur [opins hugbúnaðar](https://en.wikipedia.org/wiki/Open-source_software) inn í skipulagsheildina: sameiginleg innri hugbúnaðarsöfn, birtar framlagsreglur, [kóðarýni](https://en.wikipedia.org/wiki/Code_review) yfir teymismörk og skýra umsjónarmenn. Þegar teymi þarf breytingu á íhlut annars teymis getur það lagt breytinguna sjálft til í stað þess að skrá miða og bíða í biðröð. Þetta léttir á ósjálfstæði milli teyma án þess að leysa upp eignarhald og dreifir þekkingu og stöðlum eðlilega yfir stóran hóp verkfræðinga.

## Málamiðlanir: kostir og gallar

| Líkan fyrir þverlægar aðgerðir | Kostir | Gallar |
| --- | --- | --- |
| Miðlægt (eitt teymi fyrir alla) | Samræmi, djúp sérfræðiþekking, skýrir staðlar | Flöskuháls, biðraðir, tap á vörusamhengi |
| Sambandsskipað (hub-and-spoke, gildi) | Jafnar samræmi og hraða, deilir þekkingu | Krefst samhæfingaragna, ábyrgð getur orðið óskýr |
| Innfellt (sérfræðingur í hverju teymi) | Hratt, ríkt af samhengi, mikið eignarhald | Tvíverknaður, ósamræmi, erfitt að manna í stórum stíl |

| Teymisgerð | Best fyrir | Áhætta ef ofnotað |
| --- | --- | --- |
| Straumtengt | Mesta vöru- og þjónustuafhendingu | Engin, þetta ætti að vera ráðandi |
| Vettvangur | Að draga úr sameiginlegri vitrænni byrði | Verður fílabeinsturns-hliðvörður |
| Stuðnings | Að dreifa getu tímabundið | Breytist í varanlegt ósjálfstæði |
| Flókið undirkerfi | Raunverulega djúp sérfræðisvið | Notað sem afsökun til að hamstra venjulega vinnu |

Endurtekna málamiðlunin er sjálfstæði gegn samræmi. Fullkomlega sjálfstæð teymi hreyfast hratt en reka sundur í stöðlum, verkfærum og öryggisstöðu. Fullkomlega miðlæg stjórn heldur hlutum samræmdum en kæfir flæði. Góð teymisskipan finnur samskeytin: sjálfstæði fyrir straumtengda afhendingu ásamt þunnum miðlægum stöðlum og troðnum slóðum (vel studd sjálfgefin verkfæri sem gera samræmda valið auðvelt) fyrir það sem raunverulega þarf að vera samræmt.

## Spurningar til að ræða með teyminu

1. **Hvaða áþreifanleg merki segja þér að vitræn byrði teymis sé of há, áður en gæði hrynja?** „Afmarkaðu hvert teymi við svið sem það getur náð tökum á“ er auðvelt að segja og erfitt að framkvæma án gagna, því vitræn byrði er ósýnileg þar til afhending og áreiðanleiki versna. Fylgstu með mælanlegum einkennum: fjölda ótengdra þjónusta eða hugbúnaðarsafna sem teymi á, hve langan tíma móttaka tekur, yfir hve mörg svið einn verkfræðingur þarf að skipta samhengi á viku og vaxandi atvikatíðni í hornum ábyrgðarsviðs teymisins. Fyrir stóra skipulagsheild skiptir þetta máli því ofhlaðin teymi verða hljóðlega að flöskuhálsum sem ekkert skipurit spáir fyrir um. Komdu með þessar tölur í umræðuna, ásamt tilfinningu teymisins sjálfs fyrir því hvað það getur og getur ekki haldið í höfðinu. Ef merkin benda til ofhleðslu er lausnin að losa ódýra vinnu yfir á vettvang eða stuðningsteymi, ekki að krefjast meiri hetjudáða.

2. **Er skipulagsbreyting raunverulega þess virði að raska hér, eða ertu að fóðra skipulagsbreytingafíkn?** Að teikna mörk upp á nýtt til að beita öfugu Conway-hreyfingunni er öflugt, og hver skipulagsbreyting eyðir líka þeim stöðugleika sem teymi þurfa til að samlagast og endurstillir hart áunna sviðsþekkingu. Sjónarmiðin sem togast á eru viðvarandi samhæfingarskattur núverandi uppbyggingar gegn einskiptiskostnaði og móralsáfalli þess að breyta henni. Í fyrirtækja- og opinberu samhengi gera innkaupamörk, verktakateymi og lögboðinn aðskilnaður starfa skipulagsbreytingar hægari og dýrari, svo þröskuldurinn ætti að vera hærri. Komdu með gögn um tafir sem ósjálfstæði veldur: hve mörg verkefni bíða eftir öðru teymi og hve lengi. Skipuleggðu upp á nýtt þegar sú bið er byggingarleg og mikil, og stattu gegn því að stokka upp þegar sársaukinn er tímabundinn eða ódýrara væri að leysa hann með innri opnum framlögum og skýrari viðmótum.

3. **Fyrir öryggi, gögn og hönnun, hvaða atburður kallar fram að þú færir þig milli innfellds, sambandsskipaðs og miðlægs líkans?** Ráðlegging kaflans er að velja fyrir hverja aðgerð og hvert umfang, og erfiðari agi er að ákveða fyrirfram hvaða vöxtur eða áhætta fær þig til að endurskoða það val. Líkan sem hentar fimmtíu verkfræðingum getur orðið flöskuháls eða samræmisstórslys við fimm hundruð, og fyrirtæki og opinberar stofnanir þurfa sérstaklega að nefna þá staðla sem lítill miðlægur kjarni mun alltaf halda. Komdu með núverandi biðtíma og samræmisbil fyrir hverja aðgerð: miðlægt öryggisteymi með margra vikna rýnibiðraðir er merki um að sambandsskipa, en innfelldir sérfræðingar sem framleiða ósamrýmanleg gagnalíkön eru merki um að bæta við miðlægum staðlakjarna. Ákveddu kveikjuna núna, svo sem þröskuld biðraðarlengdar eða úttektarniðurstöðu, svo breytingin verði skipulögð þróun frekar en neyðarviðbragð. Svarið ákvarðar hvar þú fjárfestir í troðnum slóðum og talsmönnum á móti miðlægum kjarna.

4. **Hvernig veistu hvort vettvangsteymið þitt dregur raunverulega úr vitrænni byrði eða er hljóðlega orðið hliðvörður?** Vettvangur er til að gera samræmda, áreiðanlega valið auðvelt með sjálfsafgreiðslu, og sama teymið getur rekið út í að skylda tól, handrýna hverja beiðni og bæta við þeim núningi sem það átti að fjarlægja. Fyrir stóra skipulagsheild ræður þessi greinarmunur því hvort vettvangsfjárfestingin borgar sig til baka eða verður að miðlægum flöskuhálsi sem öll straumtengd teymi bíða í röð á bak við. Sjónarmiðin sem togast á eru samræmi og stjórn á annarri hliðinni gegn sjálfstæði notenda og flæði á hinni. Komdu með gögn sem notandi myndi þekkja: hve langan tíma tekur straumtengt teymi að sjálfsafgreiða nýtt umhverfi eða leiðslu án þess að skrá miða, hlutfall sjálfsafgreiðsluaðgerða á móti mannlega milligengnum, og vettvangsupptöku mælda í teymum sem velja hann frekar en teymum sem eru þvinguð á hann. Í fyrirtækja- og opinberu samhengi skaltu krefjast þess að vettvangurinn framleiði úttektar- og regluvörslugögn sjálfvirkt frekar en gegnum handvirk hlið, því vettvangur sem uppfyllir aðskilnað starfa með því að setja inn mannlegan rýni hefur endurskapað flöskuhálsinn sem hann var fjármagnaður til að leysa upp.

5. **Hvaða samskipti milli teyma hafa fest sig í varanlegri samvinnu, og hvað myndi breyta hverju þeirra í hreint þjónustuviðmót eða endurteiknuð mörk?** Samvinnuform á að vera ákaft og tímabundið, og pörun sem lýkur aldrei er venjulega merki um að eignarhald sé á röngum stað eða að viðmótið milli tveggja teyma hafi aldrei verið gert skýrt. Þetta skiptir máli í stórum stíl því ónefnd, viðvarandi samvinna er þar sem samhæfingarkostnaður felur sig: hún birtist á engu skipuriti en leggur skatt á hverja breytingu sem teymin tvö snerta. Sjónarmiðin sem togast á eru uppgötvunargildið af því að vera nálægt gegn því flæði sem þú færð með því að breyta samskiptunum í X-sem-þjónustu samning með skilgreindu viðmóti, eða með því að sameina ábyrgðina í eitt teymi. Komdu með lista yfir teymispör sem hafa átt samvinnu samfellt lengur en ársfjórðung, breytingarnar sem kröfðust beggja teyma síðustu mánuði og hvort stöðugt viðmót milli þeirra mætti skrifa niður. Í fyrirtækja- og opinberu samhengi, þar sem verktakamörk og innkaupalotur geta fryst yfirfærslu árum saman, skaltu nefna hvaða tengsl þú getur breytt með viðmóti og innri opnum framlögum og hver eru samningsbundin föst og verður að stýra sem skýrum ósjálfstæði.

6. **Þegar stuðningsteymi hjálpar öðru teymi að byggja upp getu, hvernig veistu að það hafi tekist og geti stigið til baka í stað þess að verða varanlegt ósjálfstæði?** Stuðningsteymi eiga að þjálfa straumtengt teymi í að ná tökum á prófunum, öryggi eða sýnileika og halda svo áfram, og án skýrs útgönguskilyrðis harðnar þjálfunarsambandið í varanlega þjónustu sem straumtengda teymið tileinkar sér aldrei. Fyrir stóra skipulagsheild er þetta munurinn á því að dreifa getu yfir tugi teyma og því að búa til nýjan sameiginlegan flöskuháls sem skalar verr með hverju ári. Sjónarmiðin sem togast á eru dýpt og samræmi sem sérfræðiteymi veitir gegn sjálfstæði og eignarhaldi frá enda til enda sem þú ert að byggja inn í straumtengd teymi. Komdu með gögn um færslu getu: hvort móttökuteymið sinnir nú vinnunni án þess að stuðningsteymið sé viðstatt, hve mörgum teymum fastur stuðningshópur er skuldbundinn á sama tíma og hve lengi hvert verkefni hefur staðið fram yfir fyrirhugaða yfirfærslu. Í fyrirtækja- og opinberu samhengi, þar sem af skornum skammti sérfræðikunnátta getur legið á bak við eitt miðlægt teymi eða einn samning, skaltu ákveða fyrirfram hvernig þú fjármagnar færslu getu og talsmenn, svo að sérfræðiþekking dreifist inn í afhendingarteymi í stað þess að vera læst á bak við biðröð sem hver úttekt og útgáfa þarf að bíða á.

## Sjónarhorn eftir geirum

**Sprotafyrirtæki.** Með fáa verkfræðinga og lítið fjármagn er rétt teymisskipan eitt straumtengt teymi sem á alla vöruna, og agaþörfin er að neita að búa til sílóa áður en þú þarft á þeim að halda. Standastu freistinguna að ráða einn „DevOps“-mann eða „QA“-mann sem verður hlið. Felldu þá hæfni inn í eina teymið sem innfellda getu. Láttu lögmál Conways vinna með þér með því að halda skipulaginu flötu, svo arkitektúrinn haldist jafn einfaldur og breytanlegur og teymið.

**Lítið fyrirtæki.** Þú munt ekki manna sérstakt vettvangs- eða stuðningsteymi, svo keyptu vettvanginn: notaðu stýrða skýjaþjónustu, hýstar leiðslur og tilbúin öryggisverkfæri til að taka ódýra vitræna byrði af þínu eina eða tveimur teymum. Settu þverlæg málefni eins og öryggi og gögn fram sem hluti sem þú stillir og notar frekar en aðgerð sem þú smíðar. Taktu frá sérsniðið eignarhald fyrir það eina flókna undirkerfi sem raunverulega aðgreinir þig og láttu söluaðila bera rest.

**Stórfyrirtæki.** Í stórum stíl er vandinn samhæfingarkostnaður yfir mörg teymi, svo gerðu teymisskipan að skýrri, stýrðri hönnun: sameiginlegt flokkunarkerfi fjögurra teymisgerða, nefnd samskiptaform, vettvangur á troðinni slóð og inner-source til að létta biðraðir milli teyma. Fylgstu með töfum vegna ósjálfstæðis og vitrænni byrði teyma sem eignasafnsmælikvörðum og stýrðu skipulagsbreytingum sem ásetningsbundinni þróun með háum þröskuldi frekar en árlegu viðbragði. Þunnur miðlægur kjarni heldur stöðlunum sem þurfa að vera samræmdir, á meðan straumtengd teymi halda sjálfstæði yfir afhendingu.

**Hið opinbera.** Innkaupareglur, verktakamörk og lögboðinn aðskilnaður starfa sundra eignarhaldi, svo hannaðu teymisskipan til að uppfylla þessar skorður með verkfærum og skýrum viðmótum frekar en mannlegum yfirfærslum. Kjóstu sambandsskipuð líkön með lítinn staðlakjarna og vettvang sem framleiðir úttektar- og regluvörslugögn sjálfvirkt, svo aðskilnaður starfa sé framfylgt af leiðslum frekar en rýnibiðröðum. Skjalfestu teymismörk, samskiptaform og rekstrarlíkan opinskátt, svo uppbygging sé gagnsæ endurskoðendum, eftirlitsaðilum og almenningi sem fjármagnar hana.

## Dæmi

**Sprotafyrirtæki.** Tíu manna sprotafyrirtæki hefur eitt straumtengt teymi sem á alla vöruna frá enda til enda, sem er einmitt rétt í þessari stærð: engar yfirfærslur, enginn samhæfingarskattur og allir deila sama samhengi. Vandinn byrjar þegar þeir ráða sérstakan „DevOps-mann“ og sérstakan „QA-mann“ og endurskapa fyrir slysni starfsgreinasíló, svo hver útgáfa bíður nú á tveimur einstaklingum. Þeir leiðrétta stefnuna með því að líta á þessar ráðningar sem innfellda vettvangs- og prófunargetu innan eina teymisins, frekar en hlið sem vinna þarf að fara í gegnum. Í þessari stærð er ódýrasta teymisskipanin sú sem heldur öllum í einu flæði.

**Stórfyrirtæki.** Greiðsluferli stórrar verslunarkeðju var hægt að breyta því framendi, bakendi og afgreiðslurökfræði voru skipt milli þriggja starfsgreinaskipaðra teyma, sem þvingaði hverja breytingu í gegnum þrjá verkefnalista. Með því að beita öfugu Conway-hreyfingunni endurskipulögðu þeir sig í straumtengd teymi í kringum notendaferðir („vafra“, „karfa og greiðsla“, „eftir kaup“), hvert með sína sneið frá enda til enda, studd af vettvangsteymi sem bauð uppsetningu og sýnileika sem þjónustu. Greiðslubreytingar sem áður tóku ársfjórðung fóru að koma út á dögum, því samhæfingin sem áður spannaði teymi gerðist nú innan eins.

**Hið opinbera.** Skattstofnun hins opinbera rak miðlægt öryggisteymi sem rýndi hverja útgáfu og skapaði margra vikna biðröð sem seinkaði mikilvægum lagfæringum. Hún færði sig yfir í sambandsskipað líkan: lítil miðlæg öryggisdeild setti staðla og veitti „troðna slóð“ af fyrirfram samþykktum, sjálfvirkt skönnuðum leiðslum, á meðan öryggistalsmenn í hlutastarfi innan hvers afhendingarteymis tóku daglegar ákvarðanir. Vettvangurinn framleiddi regluvörslugögn sjálfvirkt. Lögbundnar kröfur um aðskilnað starfa voru enn uppfylltar, en með verkfærum og skýrum viðmótum frekar en mannlegum flöskuhálsi, sem stytti útgáfutíma verulega og bætti úttektarviðbúnað.

## Viðskiptarök: hvatar, ávöxtun fjárfestingar og heildarkostnaður

Þú borgar fyrir slæma teymishönnun í samhæfingarkostnaði, og sá kostnaður vex hraðar en línulega með fjölda teyma sem þurfa að samstilla sig fyrir dæmigerða breytingu. Sérhver yfirfærsla er biðröð með biðtíma, samhengisflutningur sem tapar upplýsingum og ný tækifæri til misskilnings. Þegar venjuleg breyting krefst þess að þrjú teymi samstilli vegvísa sína er raunverulegur kostnaður ekki summa vinnu þeirra. Hann er margfalt stærri kostnaður við tímasetningu, bið og endurvinnslu. Teiknaðu mörkin upp á nýtt þannig að flestar breytingar rúmist innan eignarhalds eins teymis og kostnaðurinn hverfur einfaldlega.

Upptökukostnaðurinn er raunverulegur. Skipulagsbreytingar eru truflandi og að byggja vettvanga og inner-source vinnubrögð krefst fjárfestingar fyrirfram áður en ávinningurinn kemur. En kostnaðurinn við að gera það ekki safnast upp. Skipulagsheildir sem láta uppbyggingu safnast upp fyrir tilviljun hrúga upp yfirfærslukeðjum, sameiginlegum flöskuhálsteymum með ársfjórðungslangar biðraðir og arkitektúr sem skipuritið hefur steingert. Til að færa rök fyrir þessu við forystu skaltu mæla tafir vegna ósjálfstæðis: hve mörg virk verkefni bíða eftir öðru teymi og hve lengi. Vettvangs- og teymisskipanafjárfestingar borga sig venjulega til baka með því að breyta þeirri bið í flæði, sem birtist sem styttri afhendingartímar og meiri afköst án þess að bæta við mannafla.

## Andmynstur og gildrur

- Að hunsa lögmál Conways: að hanna arkitektúr sem skipulagið getur ekki afhent.
- Starfsgreinasíló: aðskilin framenda-, bakenda-, QA- og rekstrarteymi sem þurfa að samhæfa sig fyrir hverja breytingu.
- Flöskuháls sameiginlegrar þjónustu: miðlægt teymi sem hvert verkefni þarf að bíða á bak við.
- Vettvangur sem hliðvörður: vettvangsteymi sem skyldar frekar en þjónar og bætir við núningi í stað þess að fjarlægja hann.
- Vitræn ofhleðsla: teymi sem eiga víðfeðm, ótengd kerfi sem þau ná ekki tökum á.
- Varanleg „samvinna“: tvö teymi sem eru stöðugt flækt saman, sem bendir til rangstaðsetts marks.
- Skipulagsbreytingafíkn: að stokka stöðugt upp og eyðileggja þann stöðugleika sem teymi þurfa til að samlagast.

## Þroskalíkan

- **Stig 1, Upphaf.** Teymi myndast fyrir tilviljun, út frá mannafla eða eldra stigveldi. Enginn nefnir teymisgerðir eða samskiptaform. Starfsgreinasíló og flöskuhálsar sameiginlegrar þjónustu eru alls staðar og ósjálfstæði er falið þar til það hindrar útgáfu.
- **Stig 2, Þróun.** Nokkur straumtengd teymi eru til og fyrsta vettvangs- eða inner-source átak birtist, en mynstrið er beitt ójafnt: fá teymi eiga sneið sína frá enda til enda á meðan önnur bíða enn í röð á bak við miðlægar aðgerðir, og vitræn byrði er rædd með sögum frekar en stýrt.
- **Stig 3, Stöðlun.** Teymisgerðirnar fjórar og samskiptaformin þrjú eru skjalfest og notuð af ásetningi um alla skipulagsheildina. Vettvangar og inner-source létta ósjálfstæði milli teyma. Rekstrarlíkan fyrir öryggi, gögn og hönnun er valið og skrifað niður, og ný teymi eru mynduð eftir þessum stöðlum frekar en með spuna.
- **Stig 4, Stjórnun.** Teymisskipan er mæld og stýrð gegn grunnlínum: teymi fylgjast með vitrænni byrði, töfum vegna ósjálfstæðis (verkefni sem bíða eftir öðru teymi og hve lengi), sjálfsafgreiðsluhlutfalli og upptöku vettvangs, lengd samskiptaforma og flæðimælikvörðum afhendingar svo sem afhendingartíma og breytingatíðni. Þröskuldar kalla fram aðgerðir, til dæmis biðraðarlengd sem neyðir aðgerð til að sambandsskipa eða viðvarandi samvinna sem bendir á rangstætt mark, svo ákvarðanir byggi á gögnum frekar en skoðunum.
- **Stig 5, Samhæfing.** Teymishönnun er stöðugt bætt og samþætt arkitektúr, vörum og áhættuáætlun. Skipulagsheildin mótar mörk upp á nýtt eftir því sem kerfið og reksturinn þróast, lýkur stuðningsverkefnum þegar geta hefur færst yfir og endurjafnar vettvangsfjárfestingu eftir því sem vitræn byrði breytist, og heldur hröðu flæði sem aðlögunarhæfum, varanlegum eiginleika frekar en einskiptis skipulagsbreytingu.

## Hugmyndir til umræðu

- Fyrir dæmigerða breytingu, hve mörg teymi þurfa að samhæfa sig, og hvers vegna?
- Hver teyma okkar bera of mikla vitræna byrði, og hvað gæti vettvangur tekið af þeim?
- Hvar erum við að berjast við lögmál Conways í stað þess að teikna mörk upp á nýtt?
- Þjóna vettvangsteymin okkar straumtengdum teymum eða eru þau hliðverðir?
- Ættu öryggi, gögn og hönnun að vera miðlæg, sambandsskipuð eða innfelld hjá okkur núna?
- Hvaða „tímabundna“ samvinna hefur hljóðlega orðið að varanlegu ósjálfstæði?

## Helstu atriði

- Skipulagsuppbygging ákvarðar arkitektúr og afhendingarhraða. Hannaðu hana af ásetningi.
- Notaðu teymisgerðirnar fjórar, með straumtengt sem sjálfgefið og hinar til stuðnings.
- Beittu öfugu Conway-hreyfingunni til að gera æskilegan arkitektúr að auðveldu leiðinni.
- Stýrðu vitrænni byrði. Afmarkaðu hvert teymi við svið sem það getur náð tökum á.
- Takmarkaðu og nefndu samskiptaform milli teyma. Líttu á viðvarandi ósjálfstæði sem mörkagalla.
- Veldu miðlæg, sambandsskipuð eða innfelld líkön fyrir þverlægar aðgerðir eftir umfangi og notaðu InnerSource til að létta biðraðir.

## Heimildir og frekari lestur

- Matthew Skelton and Manuel Pais, "Team Topologies: Organising Business and Technology Teams for Fast Flow"
- Melvin Conway, "How Do Committees Invent?" (the origin of Conway's Law)
- Nicole Forsgren, Jez Humble, Gene Kim, "Accelerate"
- Will Larson, "An Elegant Puzzle: Systems of Engineering Management"
- Sam Newman, "Building Microservices" (on aligning services to teams)
- Danese Cooper and Klaas-Jan Stol, "Adopting InnerSource," and the InnerSource Commons patterns
- Frederick Brooks, "The Mythical Man-Month" (communication overhead)
