# 6.6 Innviðir og rekstur gervigreindar

## Yfirlit og tilgangur

Innviðir og rekstur gervigreindar er sú grein að útvega, tímasetja og reka sérhæfða reikni-, geymslu- og þjónustukerfið sem gervigreindarvinnuálag krefst, á hagkvæman, áreiðanlegan og vaktanlegan hátt. Nútímagervigreind er dýr í rekstri. Þjálfun og þjónusta stórra líkana krefst knappra hraðla ([GPU](https://en.wikipedia.org/wiki/Graphics_processing_unit) og [TPU](https://en.wikipedia.org/wiki/Tensor_Processing_Unit)), hárrar bandbreiddar í netkerfum, stórrar vektorgeymslu fyrir sókn (að skrá gögn sem talnavektora svo hægt sé að finna svipuð atriði hratt) og þjónustulaga stilltra fyrir töf og afköst. Að fá þessa innviði rétta er munurinn á gervigreind sem stigvaxar á sjálfbæran hátt og gervigreind sem hljóðlega étur fjárhagsáætlun á meðan hún skilar of litlu.

Fyrir stór teymi eru kjarnavandamálin stærð, skortur og kostnaður. Hraðlar eru takmarkaðir og dýrir, svo tímasetning og nýting skipta gríðarlega miklu máli. Aðgerðalausir GPU eru brenndir peningar og illa lotuð ályktun margfaldar kostnað á beiðni. Sóknarþung forrit þurfa [vektorgagnagrunna](https://en.wikipedia.org/wiki/Vector_database) sem haldast hraðir þegar þeir vaxa. Forrit skapandi gervigreindar þurfa útgáfustýringu fyrirmæla, matsleiðslur og vöktun (stundum kallað LLMOps) til að starfa örugglega og batna með tímanum. Án sameiginlegra innviða og rekstrarsiðferðis berst hvert teymi sömu bardaga og kostnaður rýkur upp.

Opinberar og regluverkaðar skipulagsheildir bæta við kröfum um gagnafullveldi, öryggi og fyrirsjáanleg útgjöld. Þær gætu þurft útsetningu á eigin vélbúnaði eða í fullveldisskýi svo viðkvæm gögn og líkön yfirgefi aldrei stýrð mörk. Þær verða að spá fyrir um og rökstyðja innviðaútgjöld og uppfylla öryggis- og aðgengisstaðla. Innviðaákvarðanir um gervigreind í þessu umhverfi hafa margra ára afleiðingar, svo taktu þær með innkaup, öryggi og útgöngu í huga.

## Meginreglur

- Líttu á hraðlareikniafl sem knappa, dýra auðlind sem á að tímasetja og nýta, ekki hamstra.
- Fínstilltu kostnað á nytsama vinnueiningu, ekki hráa afkastagetu.
- Stilltu stærð líkana og vélbúnaðar að verkinu. Stærsti kosturinn er sjaldan sá hagkvæmasti.
- Hannaðu þjónustu fyrir töf og afköst með lotun og skyndiminni sem fyrsta flokks tækni.
- Gerðu gervigreindarkerfi vaktanleg: raktu kostnað, töf, gæði og villur samfellt.
- Útgáfustýrðu og metdu fyrirmæli og líkön af sömu nákvæmni og kóða.
- Skipuleggðu flytjanleika og forðastu bindingu í innviða- og þjónustuvali.

## Ráðleggingar

### Skipuleggðu og stýrðu hraðlareikniafli

Spáðu fyrir um eftirspurn eftir þjálfun og ályktun sérstaklega, þar sem þær hafa ólíka lögun. Þjálfun er hviðukennd og tímasetjanleg. Ályktun er samfelld og næm fyrir töf. Notaðu tímasetjara og kvóta til að skipta knöppum GPU og TPU milli teyma, forgangsraða vinnuálagi og knýja nýtingu upp. Mældu nýtingu og líttu á króníska iðjuleysi sem vandamál til að laga. Blandaðu frátekinni afkastagetu fyrir grunnálag við afkastagetu eftir þörfum eða afgangsgetu fyrir hviður til að stýra kostnaði. Íhugaðu hvort ódýrari eða smærri hraðlar, eða CPU-ályktun fyrir létt líkön, myndu duga. Veldu milli skýs, eigin vélbúnaðar og blendings út frá kostnaði í þinni stærð, gagnafullveldisþörfum og hviðumynstrum, og haltu útgönguleið.

### Smíðaðu sóknarinnviði: innfellingar og vektorgagnagrunna

Fyrir sóknarauknar forrit skaltu setja upp innviði til að búa til [innfellingar](https://en.wikipedia.org/wiki/Word_embedding) (talnavektora sem setja svipuð atriði nálægt hvert öðru) og geyma þær í vektorgagnagrunni sem styður hraða [leit að nálægustu nágrönnum með nálgun](https://en.wikipedia.org/wiki/Nearest_neighbor_search) (að finna líkustu vektorana án þess að bera hvern og einn tæmandi saman) í þinni stærð. Skipuleggðu þrennt: kostnað og töf innfellingarmyndunar, ferskleika vísitölu þegar skjöl breytast og rekstrarbyrðina af því að halda vísitölum samkvæmum. Metdu hvort sérstakur vektorgagnagrunnur, vektorfær viðbót við núverandi gagnagrunn eða stýrð þjónusta passar best við stærð þína og bindingarþol. Vaktaðu sóknartöf og endurheimt, því sóknargæði ráða beint gæðum forritsins.

### Fínstilltu líkanaþjónustu: lotun, skyndiminni og töf

Þjónustan er þar sem ályktunarkostnaður og notendaupplifun ráðast. Notaðu **lotun** til að vinna margar beiðnir saman og auka hraðlaafköst, og jafnvægisstilltu lotustærð gegn töf. Notaðu **skyndiminni** ótæpilega: geymdu eins eða merkingarlega líkar beiðnir, geymdu innfellingar og nýttu fyrirmæla- eða forskeytisskyndiminni þar sem vettvangurinn styður það til að forðast endurútreikning sameiginlegs samhengis. Settu skýr tafarmarkmið og mældu halatöf, ekki bara meðaltöl. Beindu beiðnum til líkana í réttri stærð: lítið líkan fyrir auðveld tilvik, stærra aðeins þegar þarf. Sjálfskalaðu þjónustu að eftirspurn og álagsprófaðu fyrir opnun svo þú þekkir afkastagetu þína og kostnaðarferil.

### Stundaðu LLMOps: útgáfustýringu fyrirmæla, matsleiðslur og vöktun

Líttu á fyrirmæli sem útgáfustýrða gripi í frumkóðastýringu, með rýni og getu til að afturkalla. Smíðaðu matsleiðslur sem keyra óbeintengd prófasöfn sjálfvirkt hvenær sem fyrirmæli eða líkön breytast, svo þú grípir afturfarir fyrir útgáfu. Mældu framleiðslu ítarlega: skráðu inntök, úttök, töf, tókennotkun, kostnað og villur, með úrtaki og persónuverndarvörnum. Raktu gæðamerki og endurgjöf notenda beintengt. Þessi vöktun leyfir þér að grípa rýrnun, stýra kostnaði, aflúsa bilanir og bæta kerfi örugglega: rekstrarlegur burðarás skapandi gervigreindar í framleiðslu.

### Stýrðu kostnaði vægðarlaust og vaktanlega

Eignaðu gervigreindarútgjöld til teyma og notkunartilvika svo kostnaður sé sýnilegur og eigandi hans þekktur. Settu fjárhagsáætlanir og viðvaranir, vaktaðu kostnað á beiðni og á niðurstöðu og rýndu stærstu kostnaðardrifkrafta reglulega. Notaðu vogarstengurnar sem þú hefur: líkanastærðarstillingu, skyndiminni, lotun, fyrirmæla- og samhengisklippingu og val á ódýrustu útsetningu sem mætir kröfum. Gervigreindarkostnaður getur skalast með notkun á óvæntan hátt, svo samfelld kostnaðarvöktun er nauðsynleg til að forðast óþægilegar óvæntar uppákomur.

## Málamiðlanir: kostir og gallar

| Ákvörðun | Valkostur A | Valkostur B | Málamiðlun |
|---|---|---|---|
| Staðsetning reikniafls | Ský | Eigin vélbúnaður | Teygjanleiki og lágur upphafskostnaður gegn stjórn, fullveldi og hagfræði stöðugs ástands |
| Afkastageta | Frátekin | Eftir þörfum/afgangsgeta | Fyrirsjáanlegur kostnaður gegn sveigjanleika og rofáhættu |
| Lotustærð | Stórar lotur | Litlar lotur | Afköst og kostnaður gegn töf |
| Líkanastærð | Stórt líkan | Lítið líkan | Gæði gegn kostnaði og hraða |
| Vektorgeymsla | Sérstakur gagnagrunnur | Viðbót við núverandi gagnagrunn | Afköst í stærð gegn einfaldleika og færri kerfum |
| Skyndiminni | Ótæpilegt | Lágmarks | Lægri kostnaður og töf gegn ferskleika og flækju |

Ríkjandi málamiðlunin er kostnaður gegn töf og gæðum. Lotun, skyndiminni og smærri líkön skera kostnað en geta bætt við töf eða dregið úr gæðum. Rétta jafnvægið ræðst af umburðarlyndi forritsins. Eigin vélbúnaður gegn skýi skiptir stjórn og hagfræði stöðugs ástands fyrir teygjanleika og litla skuldbindingu, ákvörðun sem er mjög mótuð af gagnafullveldisþörfum og stærð.

## Spurningar til að ræða með teyminu

1. **Hver er kostnaður okkar á nytsama niðurstöðu í dag og hvaða vogarstöng myndi hreyfa hann mest?** Hrá afkastageta og meðaltöl á beiðni fela töluna sem skiptir máli: hvað það kostar að skila einni raunverulegri verðmætaeiningu og hvernig það skalast með notkun. Fyrir stórt teymi er munurinn á fínstilltri og ófínstilltri útsetningu oft margfaldur í útgjöldum, svo þessi spurning breytir óljósum áhyggjum af reikningnum í raðaðan lista lagfæringa. Komdu með núverandi kostnaðarskiptingu eftir teymi og notkunartilviki, þróun á beiðni og á niðurstöðu og stærstu kostnaðardrifkrafta. Ræddu vogarstengurnar í röð eftir ávinningi: líkanastærðarstillingu, skyndiminni (þar með talið forskeytis- og merkingarskyndiminni), lotun og fyrirmæla- eða samhengisklippingu. Hjá hinu opinbera bætist við þrýstingur að spá fyrir um og rökstyðja margra ára útgjöld. Svarið ætti að gefa hverjum helsta kostnaðardrifkrafti eiganda og vogarstöng, ekki hálfkák.

2. **Ef núverandi ályktunarveitandi okkar tvöfaldaði verð sitt eða lægi niðri á morgun, hve hratt gætum við skipt?** Hljóðlát binding er auðveld að byggja og sársaukafullt að sleppa úr, og þjónustustaflar eru þar sem hún felst dýpst. Fyrir fyrirtæki og sérstaklega hið opinbera er flytjanleiki innkaupa- og samfellukrafa, ekki kurteisi. Komdu með arkitektúr þinn: hvort líkön sitji á bak við innra viðmót, hvort fyrirmæli og matssöfn séu flytjanleg og hve mikið af veitandasértækri þjónustuhegðun þú reiðir þig á. Merkið til að fylgjast með er hvort nokkur hafi nokkru sinni keyrt matssafnið þitt gegn öðrum veitanda eða öðru útsetningarmarki. Ef skipti tækju mánuði og krefðust endurskriftar kjarnaleiða skaltu líta á það sem hönnunargalla til að bregðast við núna, því fullveldis- og eigin-rekstrar kostir kunna að verða skylda með litlum fyrirvara.

3. **Hver er hraðlanýting okkar núna og hve mikið brenna aðgerðalausir GPU og ólotuð ályktun?** Hraðlar eru knappir og dýrir, svo króníkt iðjuleysi og þjónusta á beiðni tæmir hljóðlega fjárhagsáætlanir sem gætu fjármagnað meiri getu. Fyrir stóra skipulagsheild sem deilir GPU milli teyma afhjúpar þessi spurning hvort tímasetning, kvótar og forgangur haldi nýtingu raunverulega hárri eða hvort hamstraður, vannýttur vélbúnaður sé normið. Komdu með raunverulegar nýtingartölur, lotunar- og skyndiminnisstöðu þína og halatafarmælingar þínar, ekki bara meðaltöl, því notendur finna hæga halann. Ræddu hvort eftirspurn eftir þjálfun og ályktun sé spáð sérstaklega, miðað við ólíka lögun þeirra, og hvort smærra líkan eða CPU-ályktun myndi duga fyrir létt tilvik. Svarið ætti að benda á tiltekna aðgerðalausa getu til að endurheimta og tilteknar beiðnir til að lota eða beina til líkans í réttri stærð.

4. **Þegar fyrirmæla- eða líkanabreyting fer í loftið, hvað stöðvar hljóðláta gæða- eða kostnaðarafturför frá því að ná til notenda?** Þjónustustafli getur litið heilbrigður út á töf og uppitíma á meðan svörin sem hann skilar versna hljóðlega eða ný fyrirmæli tvöfalda tókennotkun á beiðni. Fyrir stórt teymi þar sem mörg teymi breyta fyrirmælum og skipta um líkön sjálfstætt er óhliðuð breyting framleiðsluatvik í bið, og sprengisvæðið vex með hverju teymi á sameiginlega vettvanginum. Komdu með matsþekju þína: hvaða fyrirmæli og líkön hafa óbeintengd prófasöfn, hvort þau söfn keyri sjálfvirkt á hverja breytingu, hvaða gæða- og kostnaðarþröskuldar hliða útgáfu og hve hratt þú getur afturkallað. Ræddu hvort fyrirmæli búi í frumkóðastýringu með rýni, eða hvort einhver geti enn breytt lifandi kerfisfyrirmælum í höndunum. Í fyrirtækja- og opinberu umhverfi skaltu tengja hverja breytingu við úttektarslóð og nefndan samþykkjara, því eftirlitsaðili sem spyr „hver breytti þessu og hvað prófuðuð þið“ þarf svar sem er skráð, ekki munað.

5. **Hvernig veljum við milli skýs, eigin vélbúnaðar og fullveldisútsetningar og höfum við verðlagt raunverulega hagfræði stöðugs ástands frekar en tilraunaverkefnið?** Val á staðsetningu reikniafls setur kostnaðarferil þinn, gagnafullveldisstöðu og útgönguleiðir árum saman, samt er það oft gert á skýjareikningi tilraunaverkefnis sem lítur ekkert út eins og framleiðsla í stærð. Fyrir stóra skipulagsheild er teygjanlegt skýjaafl ódýrt að byrja á og getur orðið stærsti einstaki liðurinn þegar ályktun keyrir samfellt, á meðan eigin vélbúnaður skiptir lítilli skuldbindingu fyrir stjórn og hagfræði stöðugs ástands. Komdu með spáð þjálfunar- og ályktunarmagn, jafnvægispunktinn þar sem frátekinn eða eigin vélbúnaður slær eftir-þörfum, gagnabúsetu- og öryggisskorður þínar og hviðumynstrin sem mæla með blendingi. Í opinberu og regluverkuðu umhverfi skaltu vega fullveldisský eða kröfur um eigin vélbúnað sem kunna að verða skylda með litlum fyrirvara og staðfesta að arkitektúrinn haldi líkönum á bak við innra viðmót svo þvinguð flutningur endurskrifi ekki kjarnaleiðir.

6. **Eigum við í raun gervigreindarútgjöld okkar og getur hvert teymi séð og svarað fyrir kostnaðinn sem það knýr?** Gervigreindarkostnaður skalast með notkun á vegu sem koma fólki á óvart, og án skiptingar lendir reikningurinn sem ein ógegnsæ tala sem ekkert teymi finnur ábyrgð á að minnka. Í stórri skipulagsheild er kostnaður sem enginn á kostnaður sem enginn fínstillir, svo spurningin er hvort útgjöld séu merkt til teyma og notkunartilvika með fjárhagsáætlunum, viðvörunum og þróun á niðurstöðu, eða hvort þau uppgötvist aðeins þegar fjármálasvið stigmagnar. Komdu með kostnaðarskiptingarlíkan þitt, stærstu drifkrafta eftir teymi og vogarstengurnar sem hver eigandi stýrir: stærðarstillingu, skyndiminni, lotun og samhengisklippingu. Fyrir fjárhagsáætlanir fyrirtækja og hins opinbera bætist við agi þess að spá fyrir um og rökstyðja margra ára innviðaútgjöld, því opinber aðili sem getur ekki útskýrt reikniaflsreikning sinn línu fyrir línu mun eiga erfitt með að verja hann í rýni.

## Sjónarhorn eftir geirum

**Sprotafyrirtæki.** Eigðu enga innviði sem þú getur forðast. Kallaðu á hýst ályktunar-API, beindu auðveldum beiðnum til lítils ódýrs líkans og taktu frá stærra fyrir erfið tilvik og geymdu í skyndiminni ótæpilega svo endurtekin fyrirmæli kosti ekkert. Notaðu stýrðan vektorgagnagrunn frekar en að reka þinn eigin, haltu fyrirmælum í git með stuttri matsskriftu fyrir hverja breytingu og skráðu kostnað á beiðni svo ofurreikningur sjáist áður en hann sker. Knappasta auðlind þín er athygli verkfræðinga, svo keyptu rekstrarhæfni og haltu skiptum ódýrum.

**Lítið fyrirtæki.** Án vettvangsteymis skaltu líta á þjónustu, sókn og vöktun sem eitthvað sem þú kaupir innan verkfæra sem þú notar nú þegar, ekki kerfi sem þú mannar. Kjóstu stýrða ályktun og stýrða vektorleit með gagnsæju, fyrirsjáanlegu verði og settu hart útgjaldaþak og reikningsviðvörun frá fyrsta degi. Rammaðu ákvörðunina sem kaup gegn smíði af heiðarleika: að reka GPU eða vektorvísitölu borgar sig sjaldan í þínu magni og lítið líkan á bak við hýst API mætir yfirleitt þörfinni með broti af fyrirhöfninni.

**Stórfyrirtæki.** Vandinn er sameiginlegur vettvangur troðinnar slóðar yfir mörg teymi: sameiginlegir hraðlar með tímasetjurum, kvótum og forgangi til að knýja nýtingu upp, stöðluð lotun og skyndiminni, leiðarar sem stilla stærð og kostnaður eignaður hverju teymi og notkunartilviki. Hliðaðu breytingar á fyrirmælum og líkönum með sjálfvirkum matssöfnum, staðlaðu viðmótslagið svo veitendur og útsetningarmörk haldist skiptanleg og stýrðu kostnaði á niðurstöðu sem fyrsta flokks mælikvarða frekar en að láta hvern hóp finna upp kostnaðarsama, vannýtta innviði.

**Hið opinbera.** Gagnafullveldi, öryggi og fyrirsjáanleg útgjöld móta hvert val. Kjóstu eigin vélbúnað eða fullveldisský svo viðkvæm gögn og líkön haldist innan stýrðra marka, tímasettu knappa GPU milli deilda með kvótum sem þú getur rökstutt í innkaupum og spáðu fyrir um afkastagetu til að verja margra ára útgjöld línu fyrir línu. Útgáfustýrðu og metdu fyrirmæli og líkön með skráðri úttektarslóð, haltu ítarlegri vöktun á kostnaði og gæðum og hafðu líkön á bak við innra viðmót svo þvinguð flutningur til nýs veitanda eða fullveldisvettvangs strandi þig ekki.

## Dæmi

**Sprotafyrirtæki.** Lítið sprotafyrirtæki sem rekur gervigreindarritunareiginleika hélt reikningnum skynsamlegum án þess að eiga neina GPU. Það kallaði á hýst ályktunar-API, beindi auðveldum beiðnum til ódýrara lítils líkans og geymdi það stærra fyrir erfið tilvik og geymdi svör við endurteknum fyrirmælum í skyndiminni. Það geymdi fyrirmæli sín í git með stuttri matsskriftu sem keyrði fyrir hverja breytingu, notaði stýrðan vektorgagnagrunn fyrir sókn svo það þyrfti ekki að reka einn og skráði kostnað á beiðni svo stofnendurnir gætu séð útgjöld stíga áður en þau urðu óvænt.

**Stórfyrirtæki.** Fjölmiðlafyrirtæki sem rekur mikla umferðar mállíkanseiginleika skar ályktunarkostnað verulega. Það beindi auðveldum beiðnum til lítils líkans og tók frá stærra líkan fyrir erfið. Það geymdi svör við endurteknum fyrirspurnum í skyndiminni og virkjaði forskeytisskyndiminni fyrir sameiginleg kerfisfyrirmæli sín. Það rak GPU gegnum sameiginlegan tímasetjara til að halda nýtingu hárri, útgáfustýrði öllum fyrirmælum í git með sjálfvirku matssafni sem hliðaði breytingar og mældi kostnað á beiðni svo hvert vöruteymi ætti sín útgjöld.

**Hið opinbera.** Landsbundin stofnun með ströng gagnafullveldisákvæði setti gervigreindarkerfi sín upp á eigin vélbúnaði svo viðkvæm gögn og líkön yfirgæfu aldrei stýrt umhverfi hennar. Hún tímasetti knappa GPU milli deilda með kvótum og forgangi, spáði fyrir um afkastagetu til að rökstyðja margra ára innkaup og smíðaði vektorleitarvettvang fyrir sókn yfir opinber skjöl. Fyrirmæli og líkön voru útgáfustýrð og metin fyrir útgáfu. Ítarleg vöktun rakti kostnað og gæði og arkitektúrinn hélt líkönum á bak við innra viðmót til að varðveita útgönguleið og forðast bindingu.

## Viðskiptarök: hvatar, ávöxtun fjárfestingar og heildarkostnaður

Hvatinn fyrir agaða gervigreindarinnviði er einfaldur. Gervigreind í stærð er kostnaðarsöm og munurinn á fínstilltri og ófínstilltri útsetningu er oft margfaldur í útgjöldum. Ávöxtun kemur af hærri hraðlanýtingu, lægri kostnaði á beiðni gegnum lotun og skyndiminni, líkönum í réttri stærð og að forðast ofúthlutun. Vöktun og matsleiðslur borga sig með því að koma í veg fyrir kostnaðarsöm atvik og leyfa örugga endurtekningu.

Heildareignarkostnaður spannar hraðlareikniafl (stærsta línan fyrir mörg vinnuálög), vektorgeymslu, þjónustuinnviði, netkerfi og vettvangs- og rekstrarstarfsfólkið til að reka það. Vegðu það gegn kostnaði þess að fjárfesta ekki: stjórnlausum ályktunarreikningum, lélegri töf sem grefur undan upptöku og vangetu til að stigvaxa. Fyrir hið opinbera bætist við kostnaður þess að mæta ekki fullveldis- eða öryggiskröfum. Færðu rök við forystu með því að sýna þróun kostnaðar á niðurstöðu og vettvang troðinnar slóðar sem leyfir mörgum teymum að setja upp gervigreind á skilvirkan hátt, frekar en að hvert smíði kostnaðarsama, vannýtta innviði.

## Andmynstur og gildrur

- **Aðgerðalausir hraðlar.** Að úthluta knöppum GPU til teyma sem vannýta þá.
- **Engin lotun eða skyndiminni.** Að þjóna hverri beiðni fyrir sig og endurreikna sameiginlegt samhengi.
- **Stærsta líkan sjálfgefið.** Að nota dýrt líkan þar sem lítið myndi duga.
- **Kostnaðarblinda.** Engin skipting, fjárhagsáætlanir eða sýnileiki kostnaðar á beiðni þar til reikningurinn berst.
- **Óútgáfustýrð fyrirmæli.** Að breyta fyrirmælum í framleiðslu án útgáfustýringar eða matshliðs.
- **Vanræksla halatafar.** Að fínstilla meðaltöf á meðan notendur þjást af hægum hala.
- **Hljóðlát binding.** Að byggja djúpt á þjónustustafla eins veitanda án flytjanleika.

## Þroskalíkan

1. **Upphaf.** Ad hoc GPU-úthlutun sem bregst við þeim sem hrópar hæst, engin lotun eða skyndiminni, enginn kostnaðarsýnileiki fyrr en reikningurinn berst, fyrirmæli breytt lifandi og óútgáfustýrð, lágmarksvöktun.
2. **Þróun.** Sum teymi taka upp sameiginlega tímasetningu, skyndiminni og útgáfustýrð fyrirmæli, en vinnubrögð eru ósamræmd um skipulagsheildina: einn hópur lotar og metur á meðan annar þjónar enn hverri beiðni fyrir sig og breytir fyrirmælum í höndunum.
3. **Stöðlun.** Skjalfestur vettvangur troðinnar slóðar er framfylgdur um skipulagsheildina: sameiginleg tímasetning með kvótum og forgangi, stöðluð lotun, skyndiminni og stærðarstilling, vektorinnviðir fyrir sókn, sjálfvirkar matsleiðslur sem hliða hverja breytingu á fyrirmælum eða líkani og kostnaðarskiptingu til teyma og notkunartilvika.
4. **Stjórnun.** Vettvangurinn er mældur og stýrður gegn grunnlínum: hraðlanýting, kostnaður á nytsama niðurstöðu, halatöf, sóknarendurheimt og gæðaafturfarir á breytingu eru rakin með viðvörunum og þröskuldum, hvert teymi á sinn kostnað og ákvörðun um fara eða ekki fara á breytingu er tekin á sönnunargögnum frekar en innsæi.
5. **Samhæfing.** Innviðir batna og aðlagast stöðugt: leiðarval, lotun og skölun stilla sig sjálf að lifandi kostnaðar- og gæðamerkjum, afkastageta er endurjöfnuð milli teyma og milli skýs, eigin vélbúnaðar og fullveldismarka eftir því sem eftirspurn og skorður breytast, flytjanleiki er æfður og innviðaskipulag er samþætt vöru, öryggi og innkaupum.

## Hugmyndir til umræðu

- Hvernig knýrðu hraðlanýtingu upp án þess að svelta forgangsvinnuálag?
- Hvar er rétta jafnvægið milli lotunar og skyndiminnis fyrir tafarkröfur þínar?
- Hvenær réttlætir eigin vélbúnaður eða fullveldisútsetning kostnað sinn umfram ský?
- Hvernig eignarðu og stýrir gervigreindarútgjöldum yfir mörg teymi?
- Hvað ætti að hliða fyrirmæla- eða líkanabreytingu frá því að ná til framleiðslu?
- Hvernig heldurðu þjónustuinnviðum nógu flytjanlegum til að skipta um veitanda?

## Helstu atriði

- Hraðlar eru knappir og dýrir. Tímasettu, deildu og nýttu þá af ásetningi.
- Lotun, skyndiminni og líkanastærðarstilling eru helstu vogarstengurnar fyrir kostnað og töf.
- Sóknarforrit þurfa vel rekna innfellingar- og vektorleitarinnviði.
- LLMOps (útgáfustýring fyrirmæla, matsleiðslur og vöktun) er rekstrarlegur burðarás skapandi gervigreindar.
- Stýrðu kostnaði vaktanlega og varðveittu flytjanleika til að forðast bindingu.

## Heimildir og frekari lestur

- Chip Huyen, *Designing Machine Learning Systems*.
- Google, *Site Reliability Engineering* (Beyer, Jones, Petoff, Murphy, editors).
- Jared Kaplan et al., *Scaling Laws for Neural Language Models*.
- Reza Yazdani Aminabadi et al., *DeepSpeed Inference: Enabling Efficient Inference of Transformer Models at Unprecedented Scale*.
- Woosuk Kwon et al., *Efficient Memory Management for Large Language Model Serving with PagedAttention* (vLLM).
- Andriy Burkov, *Machine Learning Engineering*.
