# 6.2 Vélnámsverkfræði (MLOps)

## Yfirlit og tilgangur

Vélnámsverkfræði, oftast kölluð [MLOps](https://en.wikipedia.org/wiki/MLOps), er sú grein að taka [vélnám](https://en.wikipedia.org/wiki/Machine_learning) úr minnisbókum og tilraunum og inn í áreiðanleg, vöktuð og viðhaldanleg framleiðslukerfi. Hefðbundinn hugbúnaður hegðar sér eins og kóði hans segir til um. Vélnámskerfi hegðar sér eins og kóði þess, gögn þess og lærðar líkanastikur þess segja saman til um. Það gerir vélnámskerfi erfiðari í prófun, erfiðari í endurtekningu og hætt við að bila hljóðlega þegar heimurinn rekur burt frá gögnunum sem þau voru þjálfuð á. MLOps færir nákvæmni hugbúnaðarverkfræðinnar (útgáfustýringu, prófanir, samfellda afhendingu og vöktun) að þessum þrískipta veruleika kóða, gagna og líkana.

Fyrir stór teymi er MLOps það sem aðgreinir einnota líkan sem heillar í sýnikennslu frá flota líkana sem mörg teymi geta smíðað, sett upp og rekið örugglega. Án sameiginlegra vettvanga og vinnubragða finnur hvert teymi upp gagnaleiðslur, þjálfunarlykkjur og útsetningu aftur, og þú endar með brothætt kerfi sem enginn getur endurtekið sex mánuðum síðar. Fyrirtæki reiða sig á MLOps til að stigvaxa yfir tugi líkana, ná þjónustustigsmarkmiðum og fullnægja úttektaraðilum sem spyrja hvernig tiltekin spá var framleidd.

Hjá hinu opinbera og í regluverkuðum greinum er MLOps oft reglufylgnikrafa í dulargervi. Endurtakanleiki, uppruni og útgáfustýring eru það sem leyfir stofnun að svara lagalega mikilvægri spurningu: nákvæmlega hvaða líkan, þjálfað á hvaða gögnum, með hvaða kóða, framleiddi ákvörðunina sem hafði áhrif á borgara? Þroskuð MLOps-venja heldur þeirri spurningu svaranlegri árum síðar, sem er bæði góð verkfræði og lagaleg vernd.

*Sjá einnig:* kafla 8.1 (CI/CD og afhending), kafla 9.2 (eftirlit og vöktun) og kafla 6.6 (innviðir og rekstur gervigreindar).

## Meginreglur

- Líttu á gögn, kóða og líkön sem sameiginlega útgáfustýrða gripi. Að breyta einu þeirra breytir hegðun kerfisins.
- Sjálfvirknivæddu leiðina frá gögnum til þjálfaðs líkans til útsetningar svo hún sé endurtakanleg og úttektarhæf.
- Gerðu hvert líkan rekjanlegt til nákvæmra gagna, kóða og stillinga sem framleiddu það.
- Metdu líkön gegn dæmigerðum, afskiptum gögnum fyrir útsetningu og haltu áfram að meta eftir hana.
- Gerðu ráð fyrir að líkön rýrni. Vaktaðu rek (smám saman fráhvarf lifandi gagna eða tengsla inntaks og úttaks frá því sem líkanið var þjálfað á), gagnagæðavandamál og afkastarýrnun frá fyrsta degi.
- Kjóstu leiðinlegar, endurtakanlegar leiðslur fram yfir sniðugar, óendurtakanlegar tilraunir.
- Aðgreindu áhyggjuefnin tilraunahraða og framleiðsluáreiðanleika og brúaðu þau af ásetningi.

## Ráðleggingar

### Stýrðu öllum vélnámslífsferlinum skýrt

Skilgreindu og mældu hvert stig: gagnainntöku og sannprófun, [eiginleikaverkfræði](https://en.wikipedia.org/wiki/Feature_engineering), þjálfun, mat, útsetningu og vöktun. Gerðu mörkin milli stiga skýr svo hægt sé að prófa, endurtaka og úttekta hvert þeirra. Forðastu algengu bilunina þar sem líkan er þjálfað í ad hoc minnisbók og kastað yfir vegg til reksturs. Vefðu í staðinn lífsferlinum í samstillta leiðslu sem hver heimiluð verkfræðingur getur keyrt úr hreinni útteknun.

### Notaðu eiginleikageymslur, tilraunarakningu og líkanaskrár

**Eiginleikageymsla** miðstýrir skilgreiningum eiginleika svo sömu umbreytingar keyri bæði í þjálfun og þjónustu. Þetta eyðir þjálfunar-þjónustuskekkju (ósamkvæmni í því hvernig eiginleikar eru reiknaðir fyrir þjálfun annars vegar og lifandi spár hins vegar) og leyfir teymum að endurnýta eiginleika frekar en að endurreikna þá. **Tilraunarakning** skráir stikur hverrar þjálfunarkeyrslu, kóðaútgáfu, gagnaútgáfu og mælikvarða, svo niðurstöður séu sambærilegar og endurtakanlegar. **Líkanaskrá** er aðalgagnageymsla þjálfaðra líkana og geymir útgáfur, uppruna, matsniðurstöður, samþykktarstöðu og útsetningarstig. Saman leyfa þessi þér að svara „hvað breyttist?“ þegar hegðun færist til, og að efla eða afturkalla líkön gegnum stýrð stig.

### Gerðu gögn og líkön endurtakanleg og útgáfustýrð með uppruna

Útgáfustýrðu gagnasöfnum þínum, ekki bara kóðanum. Notaðu innihaldsvistfangsgeymslu eða gagnaútgáfuverkfæri svo þjálfunarkeyrsla vísi í óbreytanlega skyndimynd. Festu kóða með git-framlögum og festu umhverfi með læstum ósjálfstæðum og ílátsmyndum. Fangaðu uppruna frá enda til enda: hvaða hrágögn fæddu hvaða eiginleika, hvaða eiginleikar og kóði framleiddu hvaða líkan og hvar það líkan er sett upp. Þegar atvik eða úttekt skellur á breytir uppruni réttarrannsóknarmartröð í einfalda fyrirspurn. Skráðu slembitölur (fræ) og vélbúnað þar sem niðurstöður ráðast af þeim.

### Veldu útsetningarmynstur sem passa vinnuálaginu

- **Lotuskor** keyrir á áætlun yfir stór gagnasöfn. Einfaldast í rekstri, þolir töf, tilvalið fyrir skýrslur og reglubundnar ákvarðanir.
- **Beintengd (rauntíma)** þjónusta svarar stökum beiðnum innan þröngrar töfarfjárhagsáætlunar. Krefst lágtafarsóknar eiginleika og vandaðrar afkastaáætlunar.
- **Straumspilun** skorar atburði samfellt þegar þeir berast. Hentar svikagreiningu og vöktun þar sem ferskleiki er mikilvægur.
- **Jaðar** keyrir líkön á tækjum eða eigin vélbúnaði af ástæðum sem varða töf, persónuvernd, tengingu eða gagnafullveldi, algengt hjá hinu opinbera og á vettvangi.

Veldu einfaldasta mynstrið sem mætir kröfunni og hannaðu útgáfu þína með skuggaútsetningum, kanarífuglum og tafarlausri afturköllun.

### Vaktaðu rek, rýrnun og gagnagæði

Mældu inntak og úttak í framleiðslu. Fylgstu með **gagnareki** (inntaksdreifingar færast), **[hugtakareki](https://en.wikipedia.org/wiki/Concept_drift)** (tengsl inntaks og markgildis breytast), **gagnagæða**bilunum (núll, skemabreytingar, bilaðar andstreymisheimildir) og **afkastarýrnun** mældri gegn seinkuðum sannleika þar sem þú hefur hann. Settu viðvörunarþröskulda, skrifaðu keyrsluhandbækur og tengdu vöktun við endurþjálfunartrigga. Hljóðlát rýrnun er klassíska vélnámsbilunin og vöktun er eina vörnin gegn henni.

## Málamiðlanir: kostir og gallar

| Ákvörðun | Valkostur A | Valkostur B | Málamiðlun |
|---|---|---|---|
| Þjónustumynstur | Lotur | Beintengt | Einfaldleiki og kostnaður gegn ferskleika og töf |
| Eiginleikareikningur | Eiginleikageymsla | Leiðslur á líkan | Samkvæmni og endurnýting gegn uppsetningarkostnaði |
| Vettvangur | Kaupa stýrðan MLOps-vettvang | Setja saman opinn hugbúnað | Hraði og stuðningur gegn sveigjanleika og bindingu |
| Endurþjálfun | Tímasett | Ræst af reki | Fyrirsjáanleiki gegn svörun og flækju |
| Endurtakanleikanákvæmni | Full gagnaútgáfustýring | Létt rakning | Úttektarstyrkur gegn geymslu og fyrirhöfn |

Yfirgnæfandi málamiðlunin er fjárfesting núna gegn brothættni síðar. Þung endurtakanleika- og vöktunarinnviði kosta fyrirhöfn fyrirfram, en þau koma í veg fyrir margfalt stærri kostnað óskýranlegra bilana, óendurtakanlegra líkana og rýrs trausts. Stýrðir vettvangar flýta fyrir teymum en geta skapað bindingu. Opnir hugbúnaðarstaflar bjóða stjórn á verði samþættingarvinnu. Stórar skipulagsheildir hagnast yfirleitt á sameiginlegu vettvangsteymi sem felur þessa flækju á bak við sjálfgefin gildi troðinnar slóðar.

## Spurningar til að ræða með teyminu

1. **Hvernig myndum við komast að því að útsett líkan hafi hljóðlega rýrnað áður en viðskiptavinur eða borgari skaðast og hver á þá viðvörun?** Hljóðlát rýrnun er klassíska vélnámsbilunin: kóðinn keyrir enn, líkanið skilar enn öruggum einkunnum og gæðin renna niður þegar heimurinn rekur frá þjálfunargögnunum. Fyrir stórt teymi sem rekur mörg líkön þarftu þessu svarað á hvert líkan, ekki einu sinni fyrir flotann, því hvert hefur sitt reksnið og sína seinkun sannleika. Komdu með núverandi vöktun þína á gagnareki, hugtakareki og gagnagæðarofum, viðvörunarþröskuldana og keyrsluhandbókina sem segir hver bregst við. Í regluverkuðu umhverfi þar sem merki berast vikum of seint skaltu ræða staðgöngumerki sem þú getur fylgst með á meðan, því að bíða eftir seinkuðum sannleika er að bíða eftir að uppgötva skaða. Ef enginn einn eigandi er nefndur fyrir rekviðvörun líkans er það líkan í raun óvaktað.

2. **Ef úttektaraðili biður okkur um að endurtaka tiltekna spá frá fyrir átján mánuðum, gætum við í raun gert það frá enda til enda?** Endurtakanleiki er reglufylgnikrafan sem felst í góðri verkfræði: hann leyfir stofnun að svara nákvæmlega hvaða líkan, þjálfað á hvaða gögnum, með hvaða kóða, framleiddi ákvörðun sem hafði áhrif á einhvern. Komdu með raunverulegt dæmi og reyndu að rekja það: óbreytanlega gagnaskyndimyndin, git-framlagið, læstu ósjálfstæðin og ílátsmyndin, skráðu fræin og upprunann frá hrágögnum gegnum eiginleika til útsetta líkansins. Merkið er hvort einhver hlekkur í þeirri keðju vantar eða er handvirkur. Fyrir hið opinbera og regluverkaðar greinar skaltu ákveða varðveislutímann sem lög krefjast í raun og staðfesta að geymslan haldi uppruna svaranlegum allan þann glugga, því gat breytir venjulegri fyrirspurn í réttarneyðartilfelli.

3. **Hver er regla okkar um að efla líkan í framleiðslu og afturkalla það og er henni framfylgt af líkanaskránni eða aðeins á trausti?** Óstýrð efling er hvernig minnisbókatilraunir leka í framleiðslu og hvernig slæmt líkan dvelur því enginn getur afturkallað það hreint. Fyrir mörg teymi er munurinn á þroskuðu og brothættu hvort líkanaskráin hliðar eflingu með skyldubundnu samþykki og mati, eða hvort verkfræðingur getur ýtt vigtum í höndunum. Komdu með núverandi eflingarleið þína, afturköllunarbúnað og sönnunargögn um að skuggaútsetningar eða kanarífuglar keyri í raun fyrir fulla umferð. Ræddu hvort endurþjálfun sé tímasett eða rekræst og hvort endurþjálfuð líkön standist sannprófunarhlið fyrir útsetningu, því endurþjálfun á lifandi gögnum án sannprófunar magnar rek eða eitrun. Svarið ætti að vera framfylgt í vettvanginum, ekki á wiki-síðu sem fólki er treyst til að fylgja.

4. **Smíðum við MLOps-vettvang okkar á opnum hugbúnaði, kaupum stýrðan eða blöndum hvoru tveggja og hver hefur vegið bindinguna?** Þetta val setur þakið á hve hratt hvert framtíðarlíkan fer í loftið og hve mikla stjórn þú heldur yfir gögnum þínum og leiðslum. Stýrður vettvangur kemur teymum í framleiðslu hratt og ber stuðning, en getur fangað eiginleikaskilgreiningar þínar, upprunaskrár og líkanagripi í séreignarsniði sem þú kemst ekki auðveldlega úr. Samsettur opinn hugbúnaðarstafli heldur þér flytjanlegum á verði raunverulegrar samþættingar- og viðhaldsvinnu. Komdu með heildareignarkostnað hvorrar leiðar (leyfi eða smíði, geymslu, reikniafl fyrir endurþjálfun og vettvangsstarfsfólkið til að reka það), heiðarlegt mat á getu teymisins til að reka innviði og áþreifanlegt útgöngupróf: gætirðu flutt út líkanaskrána, eiginleikageymsluna og upprunann og endurbyggt annars staðar? Í fyrirtækja- og opinberu umhverfi skaltu bæta við innkaupaskorðum og gagnafullveldisreglum, því vettvangur sem geymir þjálfunargögn á svæði eða sniði sem eftirlitsaðili þinn bannar er útilokaður sama hve þægilegur hann er.

5. **Ættu eiginleikageymsla okkar og líkanaskrá að vera einn miðlægur vettvangur eða sambandsskipt á teymi og hvað kostar þjálfunar-þjónustuskekkja okkur í dag?** Að miðstýra eiginleikaskilgreiningum eyðir skekkjunni þar sem eiginleiki er reiknaður á einn veg í þjálfun og annan í þjónustu, sem er hljóðlát og dýr uppspretta nákvæmnistaps, en einn vettvangur getur orðið flöskuháls sem hægir á hverju teymi. Sambandsskipting gefur teymum sjálfræði en margfaldar lagnirnar og líkurnar á að tvö teymi skilgreini sama eiginleika ósamkvæmt. Komdu með sönnunargögn um hvar skekkja hefur þegar bitið ykkur, hve mörg teymi endurnýta eiginleika á móti að endurbyggja þá og sjálfgefin gildi troðinnar slóðar sem sameiginlegt vettvangsteymi gæti boðið. Fyrir stóra skipulagsheild skaltu vega stjórnarháttaávinning eins úttektarhæfs aðalgagnageymslukerfis gegn afhendingarkostnaði miðlægrar biðraðar, og í regluverkuðu umhverfi skaltu kjósa miðlægan uppruna sem leyfir úttektaraðila að rekja hverja spá til nákvæms eiginleikakóða sem framleiddi hana.

6. **Höfum við parað útsetningarmynstur hvers líkans við raunverulegar kröfur þess um töf, ferskleika og fullveldi, eða sjálfgefið allt á eitt form?** Lotur, beintengd, straumspilun og jaðar bera mjög ólíkan rekstrarkostnað og flækju, og að velja rangt mynstur annaðhvort ofeyðir í rauntímainnviði sem næturskýrsla þurfti aldrei eða sveltir svikaskorara af ferskleikanum sem hann reiðir sig á. Ákveddu á hvert vinnuálag hvaða mynstur krafan réttlætir í raun og stattu gegn því að staðla á flóknasta valkostinn af því að hann finnst nútímalegur. Komdu með töfarfjárhagsáætlunina, magnið, kostnað gamals svars og seinkun sannleika fyrir hvert líkan. Hjá hinu opinbera og á vettvangi skaltu vega jaðar- og eigin-rekstrar útsetningu af ásetningi, því gagnafullveldisreglur eða slitrótt tenging geta þvingað líkön á staðbundinn vélbúnað, og það val mótar upp á nýtt hvernig þú útgáfustýrir, vaktar og afturkallar hvert líkan sem þú ýtir þangað.

## Sjónarhorn eftir geirum

**Sprotafyrirtæki.** Knappasta auðlind þín er athygli verkfræðinga, svo haltu MLOps léttu og keyptu það. Raktu tilraunir í einföldu hýstu verkfæri, festu hvert útsett líkan við þjálfunargagnaskyndimynd þess og kóðaframlag í git og bættu við einni ódýrri rekathugun frekar en vettvangi. Slepptu eiginleikageymslunni og sérsmíðuðum leiðslum þar til annað eða þriðja líkan gerir endurnýtinguna þess virði. Brothættur stafli sem þú getur ekki viðhaldið sekkur þér hraðar en vantandi geta.

**Lítið fyrirtæki.** Þú hefur líklega engan MLOps-sérfræðing og þröngt fjárhagsáætlun, svo líttu á MLOps sem eitthvað innbyggt í verkfærin sem þú rekur nú þegar frekar en kerfi sem þú mannar. Kjóstu stýrða þjónustu sem sér um útgáfustýringu, útsetningu og vöktun fyrir þig og rammaðu aginn sem gagnahreinlætis- og endurtakanleikaspurningu: vittu hvaða líkan og gögn framleiddu tiltekna niðurstöðu og haltu getunni til að afturkalla. Kjóstu seljendur sem leyfa þér að flytja út gögn og líkön svo síðari skipti séu enn möguleg.

**Stórfyrirtæki.** Vandinn er stærð yfir tugi líkana og mörg teymi: sameiginleg eiginleikageymsla, tilraunarakning og líkanaskrá með stýrðri eflingu svo hópar hætti að finna upp leiðslur aftur. Fjárhagsáætlaðu vettvangsteymi sem býður sjálfgefin gildi troðinnar slóðar, staðlaðu uppruna og vöktun svo hvert líkan sé úttektarhæft og hvert atvik skýranlegt og stýrðu smíða-eða-kaupa og bindingu af ásetningi á bak við viðmót sem heldur undirliggjandi verkfærum skiptanlegum. Framfylgdu sannprófunarhliðum og afturköllun í vettvanginum, ekki í venju.

**Hið opinbera.** Endurtakanleiki, uppruni og útgáfustýring eru reglufylgnikröfur í dulargervi, svo líttu á þau sem fyrsta flokks frá fyrsta degi. Útgáfustýrðu nákvæmu gagnasafni og kóða á bak við hvert útsett líkan, varðveittu þann uppruna í lögbundinn tíma og vertu fær um að endurtaka hverja sögulega spá sem hafði áhrif á borgara. Hafðu mann sem rýnir afleiddar ákvarðanir, vegðu jaðar- og eigin-rekstrar útsetningu þar sem gagnafullveldisreglur krefjast þess og krefstu þess að hver söluaðilavettvangur veiti fulla flytjanleika gagna, eiginleika og uppruna.

## Dæmi

**Sprotafyrirtæki.** Lítið greiningarsprotafyrirtæki afhenti fyrsta brottfallsspálíkan sitt með einum gagnafræðingi og léttri uppsetningu. Það rakti tilraunir í einföldu hýstu verkfæri, festi hvert útsett líkan við þjálfunargagnaskyndimynd þess og kóðaframlag í git og bætti við einföldu vikulegu verki sem bar nýleg inntök saman við þjálfunardreifinguna. Þegar gagnalind breytti dagsetningarsniði og spár fóru að reka greip þessi einfalda athugun það á dögum frekar en eftir reitt símtal viðskiptavinar, og teymið gat endurtekið síðasta góða líkanið og afturkallað.

**Stórfyrirtæki.** Smásölubanki rekur tugi lána- og svikalíkana. Hann staðlaði á eiginleikageymslu sameiginlega yfir teymi, tilraunarakningarþjónustu og líkanaskrá með skyldubundnum samþykktarhliðum. Hvert líkan í framleiðslu rekst til þjálfunargagnaskyndimyndar sinnar og kóðaframlags. Svikalíkön eru sett upp sem straumskorarar. Lánalíkön keyra í lotum. Vöktunarlag fylgist með inntaksreki og varar við þegar gagnalind breytir skema, sem einu sinni greip bilaða andstreymisveitu áður en hún spillti ákvörðunum.

**Hið opinbera.** Opinber bótastofnun notar vélnámslíkan til að forgangsraða málarýni. Þar sem þær ákvarðanir hafa áhrif á aðgang borgara að þjónustu útgáfustýrir stofnunin nákvæmu gagnasafni og kóða á bak við hvert útsett líkan, geymir þennan uppruna í lögbundinn tíma og getur endurtekið hverja sögulega spá á beiðni. Líkön eru sett upp í lotum með manni sem rýnir merkt mál og rekvöktun knýr fram skyldubundið endurmat hvenær sem innkomandi þýði færist, svo líkanið sé aldrei hljóðlega beitt utan skilyrðanna sem það var sannprófað fyrir.

## Viðskiptarök: hvatar, ávöxtun fjárfestingar og heildarkostnaður

MLOps borgar sig með því að breyta brothættum tilraunum í áreiðanlegar eignir. Ávöxtun kemur af hraðari tíma til framleiðslu fyrir ný líkön, færri kostnaðarsömum atvikum, minna af tvítekinni innviðavinnu og getunni til að reka mörg líkön með litlu vettvangsteymi. Sameiginleg eiginleikageymsla og líkanaskrá geta skorið afhendingartíma á líkan stórlega, því teymi hætta að endurbyggja sömu lagnirnar.

Heildareignarkostnaður nær yfir vettvangssmíði eða leyfi, geymslu fyrir útgáfustýrð gögn og líkön, reikniafl fyrir endurþjálfun og starfsfólkið til að reka allt saman. Vegðu það gegn kostnaði þess að taka ekki upp: líkön sem þú getur ekki endurtekið eða úttektað, hljóðlátar bilanir sem skaða viðskiptavini eða borgara og athugasemdir eftirlitsaðila. Í regluverkuðu umhverfi getur kostnaður óskýranlegs líkans í úttekt dvergað alla MLOps-fjárfestinguna. Færðu rök við forystu með því að ramma MLOps sem áhættuminnkun og afhendingarflýtingu, ekki aukakostnað: troðin slóð sem hvert framtíðarlíkan mun ferðast.

## Andmynstur og gildrur

- **Stökk frá minnisbók í framleiðslu.** Að setja upp líkön þjálfuð í óstýrðum minnisbókum án endurtakanleika.
- **Þjálfunar-þjónustuskekkja.** Mismunandi eiginleikakóði í þjálfun og þjónustu, sem veldur hljóðu nákvæmnistapi.
- **Engin gagnaútgáfustýring.** Að útgáfustýra kóða en ekki gögn, svo keyrslur verði ekki endurteknar.
- **Útsetja og gleyma.** Að afhenda líkan án vöktunar og uppgötva rýrnun aðeins þegar notendur kvarta.
- **Endurþjálfun á sjálfstýringu.** Að endurþjálfa sjálfvirkt á lifandi gögnum án sannprófunar, sem magnar rek eða eitrun.
- **Einnota innviðir.** Hvert teymi smíðar eigin leiðslu, sem margfaldar kostnað og brothættni.
- **Að hunsa seinkuð merki.** Að gera ráð fyrir að þú getir mælt nákvæmni samstundis þegar sannleikur berst vikum síðar.

## Þroskalíkan

1. **Upphaf.** Líkön smíðuð ad hoc í minnisbókum, handvirk útsetning, engin útgáfustýring gagna eða líkana, engin vöktun. Að endurtaka fyrri spá er ágiskun.
2. **Þróun.** Einhver tilraunarakning og líkanaskrá birtist, en vinnubrögð eru ólík eftir teymum. Útsetning er hálfsjálfvirk, grunnvöktun nær yfir fá líkön og gagnaútgáfustýring er að hluta með götum í uppruna.
3. **Stöðlun.** Sameiginlegur vettvangur með eiginleikageymslu, skrá, endurtakanlegum leiðslum og uppruna frá enda til enda er skjalfestur og framfylgdur um skipulagsheildina. Vöktun á reki og gagnagæðum keyrir yfir líkön og efling og afturköllun fylgja stýrðri leið sem hvert teymi notar.
4. **Stjórnun.** Flotinn er mældur gegn grunnlínum: rekhlutföll, gagnagæðarof, nákvæmni líkana gegn seinkuðum sannleika, þjálfunar-þjónustuskekkja, tími til framleiðslu og rekstrarkostnaður á líkan eru rakin sem mælikvarðar. Viðvörunarþröskuldum og sannprófunarhliðum er framfylgt á sönnunargögnum og heilsa hvers líkans er rýnd á föstum takti af nefndum eiganda.
5. **Samhæfing.** Lífsferillinn er fullsjálfvirkur, úttektarhæfur og aðlögunarhæfur. Rekræst endurþjálfun keyrir á bak við sannprófunarhlið, sjálfsafgreiðslu-troðnar slóðir leyfa teymum að afhenda örugglega, samfellt mat tengir frammistöðu líkana við viðskiptamælikvarða og vettvangurinn samþættist afhendingu, áhættu og reglufylgni svo líkön séu reglulega lögð niður, endurnýjuð og endurmörkuð þegar gögn og aðstæður breytast.

## Hugmyndir til umræðu

- Hvernig jafnvægirðu tilraunafrelsi við framleiðsluendurtakanleika?
- Hver er rétta endurþjálfunartrigginn (áætlun, rek eða afkastarýrnun) fyrir þín notkunartilvik?
- Hve lengi þarftu að varðveita gagna- og líkanaupprunann og hvað knýr þá kröfu?
- Ættu eiginleikageymslur og skrár að vera miðlægir vettvangar eða sambandsskiptir á teymi?
- Hvernig vaktarðu nákvæmni þegar sannleiksmerki berast með langri seinkun?
- Hvenær er jaðarútsetning aukinnar rekstrarflækju virði?

## Helstu atriði

- Vélnámshegðun kemur af kóða auk gagna auk líkana. Útgáfustýrðu og stýrðu öllum þremur saman.
- Eiginleikageymslur, tilraunarakning og skrár eru burðarás endurtakanlegs vélnáms.
- Uppruni gerir líkön úttektarhæf og atvik skýranleg: nauðsynlegt í regluverkuðu umhverfi.
- Veldu lotur, beintengt, straumspilun eða jaðar til að mæta kröfum um töf, ferskleika og fullveldi.
- Líkön rýrna. Vöktun á reki, gagnagæðum og rýrnun er ekki valkvæð.

## Heimildir og frekari lestur

- Chip Huyen, *Designing Machine Learning Systems*.
- Andriy Burkov, *Machine Learning Engineering*.
- D. Sculley et al., *Hidden Technical Debt in Machine Learning Systems*.
- Mark Treveil et al., *Introducing MLOps*.
- Valliappa Lakshmanan, Sara Robinson, and Michael Munn, *Machine Learning Design Patterns*.
- Emmanuel Ameisen, *Building Machine Learning Powered Applications*.
