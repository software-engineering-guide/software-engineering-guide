# 5.6 Framendaverkfræði

## Yfirlit og tilgangur

Framendaverkfræði er sú grein að smíða notendasnúna lag hugbúnaðar: kóðann sem keyrir í vafranum eða á tækinu og breytir hönnun, efni og gögnum í virkt viðmót. Hún nær yfir ramma- og arkitektúrval, birtingarstefnu, ástandsstjórnun, afköst og seiglu yfir gríðarlega fjölbreytni vafra, tækja og netskilyrða í raunheimi. Framendinn er þar sem öll andstreymisvinnan (notendaupplifun, hönnun, efni, aðgengi, alþjóðavæðing) annaðhvort nær til notandans með árangri eða fellur í sundur.

Fyrir stór teymi er framendinn einstaklega krefjandi, því hann er útsettur fyrir umhverfi sem skipulagsheildin stýrir ekki. Vafrar, tæki, tengingar og stillingar notenda eru stórkostlega ólík og vettvangurinn (vefurinn) þróast stöðugt. Í stærð safnast arkitektúrval upp. Rammi valinn í dag takmarkar ráðningar, afköst og viðhaldshæfni árum saman, og þúsundir lítilla ákvarðana um búntstærð og birtingu leggjast saman í upplifunina sem notendur fá í raun. Sameiginlegir staðlar, íhlutasöfn, afkastafjárhagsáætlanir og arkitektúrmynstur eru það sem heldur mörgum sjálfstæðum teymum frá því að framleiða hæga, ósamræmda, brothætta heild.

Mikilvægi fyrir fyrirtæki og hið opinbera er brýnt. Fyrirtæki viðhalda langlífum forritum þar sem rammalanglífi og viðhaldshæfni skipta meira máli en nýjungar og þar sem mörg teymi verða að vera samvirk. Ríkisstjórnir þjóna öllum almenningi, þar á meðal fólki á gömlum tækjum, hægum eða mældum tengingum og hjálpartækni. Það gerir afköst, [stigvaxandi aukningu](https://en.wikipedia.org/wiki/Progressive_enhancement) og seiglu ekki valkvæðan fágun heldur muninn á þjónustu sem virkar fyrir alla og einni sem útilokar hina verst settu. Opinber þjónusta sem virkar aðeins á nýjasta símanum með hraðri tengingu bregst umboði sínu.

## Meginreglur

- Framendinn keyrir í umhverfi sem þú stýrir ekki. Hannaðu fyrir breytileika og bilun.
- Veldu leiðinlega, varanlega tækni fyrir langlíf kerfi. Fínstilltu fyrir viðhaldshæfni og ráðningar.
- Afköst eru eiginleiki og, fyrir marga notendur, forsenda aðgangs.
- Stigvaxandi aukning: afhentu virkan kjarna fyrst, lagðu síðan aukningar ofan á.
- Sendu minni kóða. Hraðasti og áreiðanlegasti kóðinn er kóðinn sem þú afhendir ekki.
- Láttu birtingarstefnu samsvara efnistegund og notendaþörf, ekki tísku.
- Seigla: viðmótið ætti að skerðast mjúklega, ekki brotna, þegar eitthvað fer úrskeiðis.
- Staðlar og vettvangseiginleikar lifa lengur en rammar. Hallaðu þér að vettvanginum.

## Ráðleggingar

### Veldu ramma fyrir langlífi og passun, ekki æði

Veldu framendatækni út frá vandanum, teyminu, viðhaldssjóndeildarhringnum og ráðningarmarkaðnum, ekki því sem er vinsælt. Fyrir langlíf fyrirtækja- og opinber kerfi skaltu kjósa þroskaða, vel studda tækni með stóra hæfileikahópa, stöðug útgáfuvinnubrögð og skýrar uppfærsluleiðir. Vegðu heildarkostnað rammaskipta: endurskriftir eru dýrar og áhættusamar. Kjóstu nálganir sem hallast að [vefstöðlum](https://en.wikipedia.org/wiki/Web_standards) svo fjárfesting þín lifi af rammaskipti og einangraðu rammasértækan kóða á bak við mörk svo forritið sé ekki gísl lífsferils eins bókasafns.

### Láttu birtingarstefnu samsvara þörfinni

Helstu birtingarstefnurnar passa hver ólíku efni. Þjónahlið birting (SSR) framleiðir fyrstu málningu fljótt og gott SEO ([leitarvélabestun](https://en.wikipedia.org/wiki/Search_engine_optimization)) og virkar án biðlara-JavaScript, sem hentar efnisþungum og opinberum síðum. [Kyrrstæð síðugerð](https://en.wikipedia.org/wiki/Static_site_generator) (SSG) forbirtir við smíði fyrir hámarkshraða og skyndiminnishæfni, tilvalin fyrir efni sem breytist sjaldan. Biðlarahlið birting (CSR) hentar mjög gagnvirkum, forritslíkum upplifunum á bak við auðkenningu. Streymi og stigvaxandi vökvun senda og virkja síðuna stigvaxandi svo notendur sjái og noti efni fyrr. Mörg stór kerfi blanda þessu eftir leið frekar en að velja eina hnattrænt. Stýrðu ástandi af ásetningi: haltu þjónaástandi, URL-ástandi og staðbundnu viðmótsástandi aðgreindu og forðastu að miðlægja allt í einni þungri hnattrænni geymslu.

### Líttu á afköst sem fjárhagsáætlaðan, mældan aga

Taktu upp afkastafjárhagsáætlanir (skýr takmörk á búntstærð, fjölda beiðna og lykilmælikvarða) og framfylgdu þeim í CI svo afturfarir felli smíðina. Raktu Core Web Vitals (hleðslu, gagnvirkni og sjónrænan stöðugleika) með raunnotendavöktun frá raunverulegum tækjum og netum, ekki bara rannsóknarstofuprófum á hröðum vélum. Minnkaðu JavaScript ágengt: kóðaskiptu og [letihlaða](https://en.wikipedia.org/wiki/Lazy_loading) svo notendur sæki aðeins það sem tiltekin sýn þarf, frestaðu ónauðsynlegri vinnu og kjóstu vettvangsgetu fram yfir þung bókasöfn. Fínstilltu myndir og leturgerðir, geymdu í skyndiminni á áhrifaríkan hátt og mældu á dæmigerðum lágbúnaðartækjum og hægum tengingum.

### Byggðu með stigvaxandi aukningu og seiglu

Byrjaðu á grunnlínu sem virkar með merkingarfræðilegu HTML og lágmarks eða engu JavaScript og auktu síðan fyrir hæf biðlaratæki. Þetta tryggir að kjarnaverkið haldist mögulegt þegar skriftur hlaðast ekki, tæki er gamalt eða net er flöktandi, algengur veruleiki frekar en jaðartilvik. Meðhöndlaðu villur mjúklega: sýndu gagnleg ástönd fyrir hleðslu, tóm, villu og ótengd skilyrði frekar en auða skjái eða endalausa snúðhringi. Fyrir þjónustur sem fólk reiðir sig á skaltu íhuga ótengt-fyrst aðferðir svo forritið haldist nothæft gegnum slitrótta tengingu og samstillist þegar tengingin kemur aftur.

### Tryggðu samhæfni milli vafra, tækja og hjálpartækni

Prófaðu yfir vafrana, tækin og hjálpartæknina sem notendur þínir hafa í raun, upplýst af raunverulegri greiningu frekar en vélum teymisins sjálfs. Notaðu stigvaxandi aukningu og eiginleikagreiningu frekar en að gera ráð fyrir að nýjustu vettvangseiginleikar séu í boði alls staðar. Byggðu [svarandi](https://en.wikipedia.org/wiki/Responsive_web_design) (sjá hönnunarkerfiskaflann) svo einn kóðagrunnur þjóni símum til borðtölva. Samþættu aðgengi og alþjóðavæðingu í framendaarkitektúr frá byrjun, ekki sem síðari ferðir.

### Stýrðu framendanum sem sameiginlegum innviðum

Útvegaðu sameiginleg íhlutasöfn, lint, sniðun og smíðaverkfæri svo teymi séu samræmd og afkastamikil. Settu arkitektúrleiðbeiningar (hvernig á að byggja upp forrit, stýra ástandi og skipta búntum) og afkastafjárhagsáætlanir framfylgdar í CI. Fyrir mjög stóra framenda skaltu íhuga einingar- eða örframendaarkitektúr sem leyfir teymum að setja upp sjálfstætt, en vegðu viðbótarflækjuna og afkastakostnaðinn vandlega, því þeir eru ekki ókeypis.

## Málamiðlanir: kostir og gallar

| Ákvörðun | Kostir | Gallar |
|---|---|---|
| Vinsæll, þroskaður rammi | Stór hæfileikahópur, stöðugur, studdur | Getur borið arfleifðarþunga. Hægari að taka upp nýjustu eiginleika |
| Nýjasti rammi | Nútímaeiginleikar, afkastabætur | Ræringarhætta, lítill hæfileikahópur, óviss líftími |
| SSR / SSG | Hröð fyrsta málning, SEO, virkar án JS | Þjóna- eða smíðaflækja, skyndiminnisáskoranir |
| CSR (SPA) | Rík gagnvirkni, forritslíkt yfirbragð | Hæg fyrsta hleðsla, háð JS, SEO- og seigluverð |
| Þungt biðlara-JavaScript | Ríkir eiginleikar | Léleg afköst á lágbúnaðartækjum, brothætt |
| Stigvaxandi aukning | Seig, þátttökuvæn, virkar alls staðar | Meiri hönnunarfyrirhöfn til að skilgreina virka grunnlínu |
| Örframendar | Sjálfstæðar teymisuppsetningar, stigvöxtur | Flækja, tvítekin ósjálfstæði, afkastaaukakostnaður |

Endurtekna málamiðlunin er auðlegð og þægindi forritara gegn útbreiðslu, afköstum og seiglu. Þungar biðlarahliðar nálganir eru þægilegar að smíða og sýna á hröðum vélum, en þær útiloka notendur á veikum tækjum og netum. Fyrir fyrirtækja- og sérstaklega opinbera áheyrendur skaltu hallast að afköstum, stigvaxandi aukningu og endingu, því kostnaður þess að útiloka notendur er hár og oft óumsemjanlegur.

## Spurningar til að ræða með teyminu

1. **Hvernig einangrum við rammasértækan kóða svo forritið sé ekki gísl lífsferils eins bókasafns?** Fyrir langlíf fyrirtækja- og opinber kerfi er rammaskipti stærsti forðanlegi kostnaðurinn: endurskrift er dýr og áhættusöm, og vinsælt bókasafn dagsins takmarkar ráðningar og viðhald árum saman. Að hallast að vefstöðlum og setja rammasértækan kóða á bak við skýr mörk þýðir að viðskiptarökfræði þín og efni lifi af næsta rammaskipti. Ákveddu hvar þessi samskeyti eru og hvort nýr verkfræðingur gæti greint vettvangskóða frá rammakóða. Komdu með mat á því hvað síðasti rammaflutningur þinn kostaði, eða hvað sá sem vofir mun kosta. Ef kjarnarökfræði þín er soðin við API eins bókasafns skaltu verðleggja þá tengingu áður en þú ver rammavalið.

2. **Samsvörum við birtingarstefnu eftir leið, eða þvingum eina stefnu á alla vöruna?** Þjónahlið birting gefur hraða fyrstu málningu og virkar án biðlara-JavaScript fyrir opinbert efni, kyrrstæð gerð hámarkar hraða fyrir síður sem breytast sjaldan og biðlarabirting hentar gagnvirkum forritslíkum flötum á bak við innskráningu. Að þvinga eina hnattrænt annaðhvort hægir á opinberum síðum með þungu JavaScript eða yfirhannar einfalda efnissíðu. Þetta er útbreiðsluspurning fyrir hið opinbera, þar sem þjónusta sem virkar aðeins eftir að stór búnti hleðst útilokar notendur á gömlum tækjum og hægum tengingum. Komdu með lykilleiðir þínar og merktu hverja með stefnunni sem hún notar í raun í dag. Ef opinber síða þarf JavaScript til að sýna efni sitt skaltu ákveða hvort það sé yfirveguð ákvörðun eða slys.

3. **Hve agaður er ástandsstjórn okkar og erum við að miðlægja allt í eina þunga hnattræna geymslu?** Að halda þjónaástandi, URL-ástandi og staðbundnu viðmótsástandi aðgreindu kemur í veg fyrir tenginguna og endurbirtingarstorma sem gera stóra framenda hæga og brothætta, samt er freistandi sjálfgefið að demba öllu í eina hnattræna geymslu. Þetta safnast í stærð, þar sem mörg teymi sem snerta eina sameiginlega geymslu skapa falin ósjálfstæði og ófyrirsjáanleg afköst. Komdu þér saman um hvar hver tegund ástands á heima og hvað á ekki heima í hnattrænu geymslunni. Komdu með íhlut sem endurbirtist oftar en hann ætti og raktu hvers vegna. Ef svarið er uppblásin miðlæg geymsla skaltu ákveða mörkin áður en tengingin harðnar.

4. **Hverjar eru afkastafjárhagsáætlanir okkar, fella þær smíðina í CI og eru þær mældar á tækjunum sem notendur okkar hafa í raun?** Fjárhagsáætlun sem enginn framfylgir er ósk, og fjárhagsáætlun mæld aðeins á hröðum fartölvum teymisins lýsir notanda sem er ekki til. Fyrir stóra skipulagsheild eru fjárhagsáætlanir eini búnaðurinn sem heldur búntstærð og Core Web Vitals í skefjum þegar tugir teyma bæta eiginleikum við sameiginlegt yfirborð, því enginn einn rýnir getur gripið hverja afturför með berum augum. Þrýstingurinn á móti er afhendingarhraði: hörð smíðabilun yfir fáein kílóbæti finnst hindrandi þar til þú verðleggur brottfallið sem hún kemur í veg fyrir. Komdu með núverandi fjárhagsáætlanir þínar, raunnotendavöktunargögn frá lágbúnaðartækjum og hægum tengingum og lista yfir útgáfur þar sem afturför slapp í gegn. Hjá hinu opinbera, þar sem umboðið er að þjóna öllum almenningi þar á meðal fólki á gömlum símum og mældum gögnum, skaltu binda fjárhagsáætlunina við hægasta tíunda hluta notenda þinna frekar en miðgildið og gera CI-hliðið óumsemjanlegt.

5. **Hvaða þjónustur okkar verða að halda áfram að virka án nokkurs biðlara-JavaScript og höfum við í raun prófað þá leið?** Stigvaxandi aukning er auðvelt að fullyrða og auðvelt að brjóta hljóðlega, því auknu leiðin er sú sem forritarar nota daglega á meðan grunnlínan rotnar óprófuð. Að ákveða þetta af ásetningi skiptir máli í stærð, þar sem mörg teymi sem afhenda á einn vettvang munu hvert gera ráð fyrir að skriftur hlaðist alltaf nema sameiginlegur staðall segi annað, og eitt hart ósjálfstæði getur brotið kjarnaverkið fyrir hvern þann sem búnti bilar. Málamiðlunin er raunveruleg: virk án JavaScript grunnlína kostar hönnunarfyrirhöfn og þrengir hvernig þú smíðar gagnvirkni. Komdu með mikilvægar notendaferðir þínar, próf sem hleður hverja með skriftur afvirkjaðar eða bilaðar og sönnunargögn um hve oft skriftur hlaðast í raun ekki á vettvangi. Fyrir opinbera þjónustu er bóta- eða skatteyðublað sem hrynur þegar ein skrifta rennur út á tíma ekki skert upplifun, það er borgari sem getur ekki lokið lagalegri skyldu, svo líttu á grunnlínuna sem regluvörslukröfu, ekki kurteisi.

6. **Hvenær borga örframendar í raun fyrir flækju sína og hver ákveður áður en teymi nær í einn?** Sjálfstæðar teymisuppsetningar eru aðlaðandi, en örframendar bera dreifðs kerfis flækju, tvítekin ósjálfstæði og afkastaskatt sem notendur borga í hægari hleðslum. Án sameiginlegs ákvörðunarpunkts taka metnaðarfull teymi þá upp af skipulagslegum þægindum löngu áður en stærð réttlætir kostnaðinn, og öll varan erfir aukakostnaðinn. Sjónarmiðið á móti er sjálfræði: teymi sem afhenda á einum sameiginlegum kóðagrunni geta hindrað hvert annað, og í raunverulegri stærð er sú tenging eigið dýrt vandamál. Komdu með fjölda teyma sem snerta yfirborðið, uppsetningarárekstur sem þú upplifir í raun í dag og mælt mat á hleðsluafritun sem skipting myndi kynna. Fyrir fyrirtækja- og opinbera vettvang, þar sem arkitektúrákvarðanir binda mörg teymi árum saman og verða að lifa af úttekt og afhendingu, skaltu krefjast skýrs, skjalfests þröskulds og eiganda sem samþykkir hreyfinguna, frekar en að láta hvert teymi ákveða í einangrun.

## Sjónarhorn eftir geirum

**Sprotafyrirtæki.** Hraði og útbreiðsla skipta bæði máli þegar hver nýskráning telur, svo stattu gegn þungu einnar-síðu forriti fyrir opinberar síður. Þjónahlið birtu markaðs- og nýskráningarflæði þitt svo það hlaðist hratt á meðalsíma og stopula farsímagagnatengingu fyrstu viðskiptavina þinna og taktu frá biðlarahliðar gagnvirkni fyrir forritið á bak við innskráningu. Settu eina einfalda búntstærðarfjárhagsáætlun í CI svo kærulaust ósjálfstæði geti ekki hljóðlega blásið upp síðuna og hallaðu þér að vefstöðlum til að halda litlum kóðagrunni viðhaldanlegum þegar þú ræður.

**Lítið fyrirtæki.** Án sérstaks framendasérfræðings og með þröngt fjárhagsáætlun skaltu kjósa vel studdan almennan ramma eða hýstan síðusmið fram yfir allt sérsmíðað, svo þú ráðir úr stórum hæfileikahópi og kaupir viðhald frekar en að manna það. Rammaðu valið sem endingu: ódýrasti kosturinn er sá sem þú neyðist ekki til að endurskrifa eftir tvö ár. Krefstu hraðra, farsímavænna síðna og aðgengilegs álags úr kassanum, því hæg eða brotin greiðsla kostar þig viðskiptavini sem þú hefur ekki efni á að missa.

**Stórfyrirtæki.** Vandinn er samræmi yfir mörg teymi: sameiginlegt íhlutasafn, samþykkt arkitektúrmynstur, lint og smíðaverkfæri og afkastafjárhagsáætlanir framfylgdar í CI svo ekkert teymi geti hljóðlega rýrt heildina. Veldu ramma fyrir langlífi og ráðningar frekar en nýjungar, einangraðu rammasértækan kóða á bak við mörk til að lifa af næsta flutning og samsvaraðu birtingarstefnu eftir fleti. Stýrðu framendanum sem sameiginlegum innviðum með raunnotendavöktun, stjórnarháttum og úttektarhæfri skrá yfir hvers vegna hvert arkitektúrval var gert.

**Hið opinbera.** Þú þjónar öllum almenningi, þar á meðal fólki á gömlum tækjum, hægum eða mældum tengingum og hjálpartækni, svo stigvaxandi aukning og afköst eru skyldur, ekki fágun. Gerðu virka án JavaScript grunnlínu að harðri reglu fyrir borgarasnúnar þjónustur, fjárhagsáætlaðu síður fyrir hægustu notendur frekar en miðgildið og haltu kjarnaverkinu kláranlegu þegar skrifta bilar. Innkaup og gagnsæi gilda: kjóstu varanlega tækni sem hallast að stöðlum sem forðast bindingu við einn söluaðila, skjalfestu aðgengis- og afkastakröfur í samningum og vertu fær um að sýna að þjónustan virki fyrir verst setta notandann, ekki bara kynningartækið.

## Dæmi

**Sprotafyrirtæki.** Sprotafyrirtæki á frumstigi freistaðist til að smíða markaðssíðu sína og nýskráningarflæði sem þunga einnar-síðu forrit, en markviðskiptavinir þeirra voru kaupendur oft á meðalsímum yfir stopula farsímagögn. Stofnendurnir tveir þjónahlið-birtu í staðinn opinberu síðurnar svo þær hlóðust hratt og virkuðu áður en nokkurt JavaScript keyrði, og tóku frá biðlarahliðar gagnvirkni fyrir forritið á bak við innskráningu. Þeir settu einfalda búntstærðarfjárhagsáætlun í CI svo kærulaust ósjálfstæði gæti ekki hljóðlega blásið upp síðuna. Granna, hraða fyrsta hleðslan bætti nýskráningar mælanlega og að hallast að vefstöðlum hélt litla kóðagrunninum þeirra auðveldum í viðhaldi þegar þeir réðu.

**Stórfyrirtæki.** Fjármálaþjónustufyrirtæki nútímavæddi víðfeðmt safn innri forrita og viðskiptavinaforrita með því að staðla á þroskaðan ramma, sameiginlegt íhlutasafn og framfylgdar afkastafjárhagsáætlanir í CI. Birtingarstefna var valin eftir fleti: þjónahlið-birtar, skyndiminnishæfar síður fyrir opinbera markaðssetningu og efni, og biðlarahliðar forrit á bak við innskráningu fyrir gagnvirk mælaborð. Búntfjárhagsáætlanir og raunnotendavöktun gripu afturfarir fyrir útgáfu, sem hélt hleðslutímum hröðum yfir mörg teymi fyrirtækisins og dró úr rammaskiptaáhættunni sem áður hafði þvingað fram kostnaðarsamar endurskriftir.

**Hið opinbera.** Landsbundið stafrænt þjónustuteymi smíðaði borgarasnúnar þjónustur með stigvaxandi aukningu sem harða reglu: hver þjónusta virkar með merkingarfræðilegu HTML og þjónahlið birtingu fyrst, og JavaScript eykur aðeins. Þetta tryggir að þjónustan virki á gömlum símum, hægum dreifbýlistengingum og hjálpartækni, þýðum sem ríkisstjórn getur ekki útilokað. Afkastafjárhagsáætlanir halda síðum léttum og hröðum á lágbúnaðartækjum og mjúk skerðing þýðir að biluð skrifta hindrar aldrei neinn í að klára bótaumsókn. Niðurstaðan er þjónusta sem er hröð, seig, aðgengileg og nothæf öllum almenningi.

## Viðskiptarök: hvatar, ávöxtun fjárfestingar og heildarkostnaður

Framendaverkfræðival knýja tekjur, útbreiðslu og kostnað. Afköst eru beint tengd umbreytingu, þátttöku og verkklárun. Hraðari upplifanir slá hægari mælanlega og fyrir notendur á veikum tækjum eru afköst línan milli þess að nota þjónustuna og að gefast upp. Stigvaxandi aukning og stuðningur yfir tæki víkka aðgengilega áheyrendahópinn, sem fyrir hið opinbera er umboð og fyrir fyrirtæki er markaðshlutdeild. Traust ramma- og arkitektúrval draga úr tíðni og kostnaði endurskrifta, stærsta forðanlega kostnaðarins í framendaverkfræði.

Hvað heildareignarkostnað varðar er upptökukostnaðurinn agi afkastafjárhagsáætlana og prófunar, fyrirhöfn stigvaxandi aukningar og fjárfesting í sameiginlegum verkfærum og íhlutasöfnum. Kostnaðurinn við að taka ekki upp er greiddur í hægum upplifunum sem tapa notendum og tekjum, útilokun lágbúnaðar- og hjálpartækninotenda (með lagalegri útsetningu hjá hinu opinbera), brothættum forritum sem brotna á vettvangi og kostnaðarsamri rammaskiptiu og endurskriftum knúnum af að elta strauma. Framendavandamál birtast sem dreift brottfall og stuðningsálag frekar en ein kostnaðarlína, svo auðvelt er að vanfjárfesta í þeim.

Til að færa rök við forystu skaltu tengja Core Web Vitals og hleðslutíma við umbreytingar- og klárunartrektir, magnsetja notendurna sem þungar biðlarahliðar nálganir útiloka og verðleggja kostnað fyrri eða yfirvofandi endurskrifta gegn stöðugleika varanlegs, staðlamiðaðs arkitektúrs. Rammaðu afkastafjárhagsáætlanir og stigvaxandi aukningu sem áhættuminnkun og útbreiðsluaukningu.

## Andmynstur og gildrur

- **Rammaeltingar**: að endurskrifa á nýjasta bókasafninu, sem skapar ræringu án notendaávinnings.
- **Eingöngu JavaScript upplifanir**: ekkert virkar fyrr en stór búnti hleðst og keyrir, sem útilokar marga notendur.
- **Að prófa aðeins á hröðum tækjum**: flaggskipsfartölvur teymisins fela raunverulega notendaupplifun.
- **Að hunsa búntstærð**: ótakmarkaður ósjálfstæðisvöxtur þar til síður eru hægar alls staðar.
- **Engin afkastafjárhagsáætlun**: afturfarir safnast hljóðlega útgáfu eftir útgáfu.
- **Auðir skjáir við bilun**: engin hleðslu-, tóm-, villu- eða ótengd ástönd. Misheppnuð beiðni brýtur síðuna.
- **Ofmiðlægt hnattrænt ástand**: allt í einni geymslu, sem skapar tengingu og endurbirtingarstorma.
- **Ótímabærir örframendar**: dreifðs kerfis flækja og tvítekin hleðsla án stærðar til að réttlæta þá.
- **Að vanrækja aðgengi og i18n í arkitektúr**: að bæta þeim við síðar á háum kostnaði.

## Þroskalíkan

**Stig 1: Upphaf.** Ad hoc framendi smíðaður á hvert teymi án sameiginlegra staðla. Þungur biðlarakóði, engar afkastafjárhagsáætlanir, prófað aðeins á eigin tækjum teymisins. Rammaval gert af kjörum eða æði og biluð skrifta getur skilið notendur eftir starandi á auðan skjá.

**Stig 2: Þróun.** Sum teymi taka upp sameiginleg verkfæri og íhlutasafn, en vinnubrögð eru ósamræmd yfir skipulagsheildina. Afköst eru mæld stundum frekar en fjárhagsáætluð eða framfylgd. Birtingarstefna er oft einsleit óháð efnistegund og þvert-tækja prófun er takmörkuð og handvirk.

**Stig 3: Stöðlun.** Rammi og arkitektúr eru valin af ásetningi fyrir langlífi og valin skjalfest og framfylgd um alla skipulagsheildina. Birtingarstefna er samsvöruð eftir fleti, stigvaxandi aukning og mjúk skerðing eru staðallinn og sameiginleg íhlutasöfn, lint og smíðaverkfæri gilda um hvert teymi. Þvert-vafra, aðgengi og alþjóðavæðing eru byggð inn frekar en fest á.

**Stig 4: Stjórnun.** Framendinn er mældur og stýrður með gögnum. Afkastafjárhagsáætlunum er framfylgt í CI svo afturfarir felli smíðina og Core Web Vitals eru raktir með raunnotendavöktun frá raunverulegum lágbúnaðartækjum og hægum tengingum gegn skýrum grunnlínum. Búntstærð, villu- og ótengd-ástands þekja og hlutfall notenda þjónað á hægustu tengingunum er skýrt frá og rýnt, svo ákvarðanir hvíli á sönnunargögnum frekar en skoðun.

**Stig 5: Samhæfing.** Afköst, seigla og útbreiðsla eru stöðugt bætt og tengd viðskiptaútkomum um alla skipulagsheildina. Framendinn hallast að vefstöðlum fyrir endingu, einangrar rammaósjálfstæði svo flutningar séu ódýrir og þróar arkitektúr aðlögunarhæft eftir því sem tæki, vettvangur og raunnotendagögn breytast. Allur almenningur og öll tæki eru fyrsta flokks og framendavinnubrögð eru samþætt hönnun, aðgengi og vöruáætlun frekar en meðhöndluð sem aðskilið áhyggjuefni.

## Hugmyndir til umræðu

- Hvernig ákveðurðu hvenær rammaflutningur er kostnaðar síns og áhættu virði?
- Hvaða Core Web Vitals og búntfjárhagsáætlanir ættu að vera harðir smíðafellandi þröskuldar?
- Hvar er stigvaxandi aukning nauðsynleg og hvar er biðlarahliðar forrit ásættanlegt?
- Hvernig heldurðu framendaarkitektúr samræmdum yfir mörg sjálfstæð teymi?
- Hvenær borga örframendar í raun fyrir flækju sína?
- Hvernig ætti raunverulegt-tæki og hæg-nets prófun að vera byggð inn í leiðsluna?

## Helstu atriði

- Framendinn keyrir í umhverfi sem þú stýrir ekki: hannaðu fyrir breytileika og bilun.
- Veldu varanlega, vel studda tækni fyrir langlíf kerfi. Hallaðu þér að vefstöðlum.
- Láttu birtingarstefnu (SSR, SSG, CSR, streymi) samsvara efni og þörf, oft blandað eftir leið.
- Líttu á afköst sem fjárhagsáætlaðan, mældan aga framfylgdan í CI með raunnotendagögnum.
- Byggðu með stigvaxandi aukningu svo kjarnaupplifunin virki alls staðar.
- Sendu minna JavaScript. Kóðaskiptu, letihlaðið og kjóstu vettvangsgetu.
- Sérstaklega fyrir hið opinbera eru afköst og seigla forsendur fyrir jöfnum aðgangi.

## Heimildir og frekari lestur

- Jeremy Keith, *Resilient Web Design*
- Aaron Gustafson, *Adaptive Web Design* (progressive enhancement)
- Steve Souders, *High Performance Web Sites*
- Ilya Grigorik, *High Performance Browser Networking*
- Addy Osmani, writings on performance, code-splitting, and the cost of JavaScript
- Google, *Web Vitals* and web.dev performance guidance
- MDN Web Docs, web platform and progressive enhancement references
- Alex Russell, essays on the cost of JavaScript and device diversity
- UK Government Digital Service, progressive enhancement and frontend guidance
- WHATWG HTML Living Standard and W3C web platform specifications
