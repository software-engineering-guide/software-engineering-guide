# 1.5 Ákvarðanataka og stjórnarhættir

## Yfirlit og tilgangur

Sérhvert hugbúnaðarkerfi er summa þúsunda ákvarðana: hvaða [gagnagrunnur](https://en.wikipedia.org/wiki/Database), hvaða arkitektúr, hvaða bókasafn, hvort smíða eða kaupa, hvenær taka á sig skuld og hvenær greiða hana niður. Stjórnarhættir eru hvernig þú tekur þessar ákvarðanir vel og samræmt, færð réttu aðilana að án þess að skapa flöskuhálsa og varðveitir rökin svo framtíðarteymi séu ekki dæmd til að læra þau upp á nýtt. Í litlu teymi gerast ákvarðanir í samtali og lifa í sameiginlegu minni. Í stórum stíl gufar það minni upp. Fólk hættir, teymi eru endurskipulögð og „hvers vegna“ að baki mikilvægu vali tapast, svo arftakar annaðhvort afrita það blint eða rífa það blint út. Góðir stjórnarhættir eru búnaðurinn sem gerir ákvarðanir sýnilegar, yfirvegaðar og varanlegar í stórri og síbreytilegri skipulagsheild.

Meginvandi stórra teyma er að jafna sjálfstæði og samræmi. Ýttu öllum ákvörðunum upp til miðlægrar stjórnar og þú færð samræmi, en á kostnað lamandi flöskuhálsa og valdalausra teyma. Ýttu öllum ákvörðunum niður og þú færð hraða, en á kostnað glundroða: ósamrýmanlegrar tækni, tvíverknaðar og endurtekinna mistaka. Þroskaða svarið er hvorki miðstýring né stjórnleysi. Það er lagskipt líkan. Teymi ákveða flest staðbundið innan vel merktrar „troðinnar slóðar“, á meðan létt og gagnsætt ferli stýrir því sem er raunverulega þverlægt og erfitt að afturkalla. Markmiðið er að gera góðar ákvarðanir að auðvelda sjálfgefna valinu og eyða af skornum skammti stjórnarháttaathygli aðeins þar sem hún skiptir raunverulega máli.

Fyrirtæki og hið opinbera bera hærri hagsmuni. Þau þurfa að fullnægja endurskoðendum, eftirlitsaðilum og stofnunum sem krefjast skjalfestra, rökstuddra ákvarðana. Þau starfa á löngum tímasjóndeildarhring, þar sem léleg arkitektúrákvörðun eða óstýrður haugur af [tæknilegri skuld](https://en.wikipedia.org/wiki/Technical_debt) getur íþyngt þeim í áratug. Og innkaupa- og regluvarsluskyldur þeirra gera ákvarðanir um að smíða eða kaupa sérstaklega afdrifaríkar og erfiðar að afturkalla. Fyrir þessar skipulagsheildir er agað, vel skráð ákvarðanataka ekki skriffinnska í sjálfri sér. Hún er áhættustýring, stofnanaminni og grunnur ábyrgðar.

## Meginreglur

- Skráðu ákvarðanir og rök þeirra. Ákvörðun án röksemdar er skuldbinding.
- Ýttu ákvörðunum á lægsta stig sem hefur samhengið, innan skýrra varnarhandriða.
- Láttu þunga ferlisins samsvara þunga og afturkræfni ákvörðunarinnar.
- Greindu á milli afturkræfra („tvíátta dyr“) og óafturkræfra („einátta dyr“) ákvarðana og stýrðu þeim á ólíkan hátt.
- Kjóstu troðnar slóðir og sjálfgefin gildi fram yfir samþykki í hverju tilviki.
- Líttu á tæknilega skuld sem stýrt eignasafn, ekki siðferðisbrest til að fela.
- Hafðu stjórnarhætti gagnsæja. Falin ákvarðanataka elur á vantrausti og endurvinnslu.

## Ráðleggingar

### Taktu upp arkitektúrákvörðunarskrár og hóflegt RFC-ferli

[Arkitektúrákvörðunarskrá](https://en.wikipedia.org/wiki/Architectural_decision) (Architecture Decision Record, ADR) er stutt, óbreytanlegt skjal sem fangar eina mikilvæga ákvörðun: samhengi hennar, valkostina sem voru skoðaðir, valið og afleiðingarnar. Geymdu ADR í útgáfustýringu ásamt kóðanum svo rökin ferðist með kerfinu. Fyrir ákvarðanir sem þurfa framlag áður en þær eru teknar skaltu nota létt [RFC](https://en.wikipedia.org/wiki/Request_for_Comments)-ferli (beiðni um umsögn): sendu tillögu, bjóddu umsagnir í afmarkaðan tíma, ákveddu síðan og skráðu. Hafðu hvort tveggja létt. Virðið er í hugsuninni og varanlegri skrá, ekki í íburðarmiklum sniðmátum. Saman breyta ADR og RFC þöglum, gleymdum rökum í leitanlegt stofnanaminni.

### Stýrðu með troðnum slóðum, ekki hliðvörðum

Frekar en að rýna hverja ákvörðun fyrir sig skaltu fjárfesta í „troðinni slóð“: safni blessaðra, vel studdra sjálfgefinna valkosta, samþykktra tungumála, ramma, uppsetningarleiðslna og mynstra, sem teymi geta tekið upp með litlum núningi og miklum stuðningi. Teymi sem halda sig á troðnu slóðinni þurfa lítið af stjórnarháttum, því öruggi, reglufylgni valkosturinn er líka sá auðveldi. Teymi með raunverulega ástæðu til að yfirgefa hana mega það, en taka á sig aukna ábyrgð og létta rýni. Þetta „gullna slóð“-líkan skalar mun betur en miðlæg stjórn sem samþykkir allt, því það færir stjórnarhætti frá hliðvörslu í hverju tilviki yfir í vel hönnuð sjálfgefin gildi.

### Notaðu arkitektúrrýnistjórnir sparlega og gagnsætt

Arkitektúrrýnistjórn, eða jafngildi hennar, hefur lögmætt hlutverk fyrir stærstu, mest þverlægu eða óafturkræfustu ákvarðanirnar og til að setja staðlana sem skilgreina troðnu slóðina. Hafðu umfang hennar þröngt, viðmið hennar birt og ferlið hratt og ráðgefandi, ekki skyldubundinn flöskuháls fyrir hversdagsvinnu. Hlutverk stjórnarinnar er að gæta samfellu og deila þekkingu, ekki að samþykkja hvert val. Þegar stjórn verður biðröð sem hvert verkefni þarf að bíða í hefur hún brugðist. Framseldu af krafti og taktu frá miðlæga rýni fyrir þær fáu ákvarðanir sem raunverulega krefjast hennar.

### Gerðu „smíða, kaupa eða taka upp“ að yfirveguðu mati

Fyrir hverja mikilvæga getu skaltu vega þrjár leiðir: smíða innanhúss, kaupa viðskiptavöru eða taka upp lausn með [opnum hugbúnaði](https://en.wikipedia.org/wiki/Open-source_software). Smíðaðu þegar getan er raunverulegt sérkenni og kjarni í hlutverki þínu. Keyptu eða taktu upp ósérgreinda getu sem aðrir gera betur. Teldu [heildareignarkostnað](https://en.wikipedia.org/wiki/Total_cost_of_ownership) (TCO), ekki aðeins verð fyrirfram. Kaup hafa í för með sér leyfis-, samþættingar- og [innilokunarkostnað](https://en.wikipedia.org/wiki/Vendor_lock-in). Smíði hefur í för með sér ævarandi viðhald og mönnun. Upptaka opins hugbúnaðar hefur í för með sér stuðnings- og öryggiseftirlitsskyldur. Skráðu ákvörðunina og forsendur hennar sem ADR, svo þú getir endurskoðað hana þegar aðstæður breytast.

### Stýrðu tæknilegri skuld sem eignasafni

Tæknileg skuld er ekki í eðli sínu slæm. Stundum er rétt ákvörðun að taka hana á sig til að afhenda fyrr. Það sem er slæmt er óstýrð, ósýnileg, gleymd skuld. Haltu skýrri skrá yfir mikilvæga skuld. Skráðu fyrir hvert atriði kostnaðinn sem það leggur á (viðvarandi „vexti“) og kostnaðinn við að laga það. Stýrðu því síðan eins og fjármálaeignasafni. Greiddu niður háa vexti sem hægja á teyminu á hverjum degi. Þoldu lága vexti í stöðugum hornum. Taktu skuldaákvarðanir meðvitað frekar en fyrir slysni. Taktu frá fastan hluta afkastagetu til að greiða niður skuld, svo hún safnist aldrei upp í kreppu.

### Greindu afturkræfar frá óafturkræfum ákvörðunum

Ekki allar ákvarðanir verðskulda jafna yfirvegun. Afturkræfar „tvíátta dyra“-ákvarðanir eru auðvelt að afturkalla, svo taktu þær hratt og staðbundið, af teyminu, með tilhneigingu til aðgerða. Að kvelja sig yfir þeim sóar tíma og hægir á námi. Óafturkræfar eða dýrar í afturköllun „einátta dyra“-ákvarðanir, opinber [API](https://en.wikipedia.org/wiki/API)-samningur, gagnalíkan í stórum stíl, margra ára skuldbinding við söluaðila, verðskulda hæga, vandaða, eldri yfirvegun og skráð rök. Að flokka ákvarðanir á þennan hátt er eitt þeirra stjórnarháttavenja sem skila mestu vægi. Það beinir af skornum skammti rýni þangað sem hún borgar sig og losar um allt annað.

## Málamiðlanir: kostir og gallar

| Stjórnarháttanálgun | Kostir | Gallar |
| --- | --- | --- |
| Miðlæg rýnistjórn fyrir allt | Hámarks samræmi og eftirlit | Alvarlegur flöskuháls, svipt teymi valdi, hægt |
| Troðin slóð með staðbundnu sjálfstæði | Skalar, hratt, öruggt sjálfgefið, valdeflir teymi | Krefst vettvangsfjárfestingar fyrirfram, nokkurt rek utan slóðar |
| Fullt sjálfstæði teyma, engir stjórnarhættir | Hratt, mikið eignarhald | Sundrun, tvíverknaður, endurtekin mistök |
| ADR / RFC | Varanlegt minni, betri ákvarðanir, gagnsæi | Skrifkostnaður, hunsað sé því ekki viðhaldið |

| Útvistunarval | Kostir | Gallar |
| --- | --- | --- |
| Smíða | Full stjórn, passar nákvæmlega, getur aðgreint | Ævarandi viðhalds- og mönnunarkostnaður |
| Kaupa | Hratt, stutt, einhver annar viðheldur því | Leyfiskostnaður, innilokun, ófullkomin passun |
| Taka upp (opinn hugbúnaður) | Ekkert leyfisgjald, skoðanlegt, samfélag | Stuðnings- og öryggisbyrði fellur á þig |

Sameinandi málamiðlunin er stjórn gegn hraða og miðlægt samræmi gegn staðbundnu sjálfstæði. Sérhvert stjórnarháttaval liggur á þessu bili. Ráðlagða afstaðan, troðnar slóðir ásamt framsali byggðu á afturkræfni, kaupir vísvitandi mestan hraða sjálfstæðis en heldur samræminu sem skiptir máli. Hún gerir þetta með því að gera samræmda valið auðvelt og taka frá þunga ferla fyrir sjaldgæfu óafturkræfu ákvörðunina.

## Spurningar til að ræða með teyminu

1. **Hver ákveður hvort tiltekin ákvörðun sé einátta dyr, og hvernig muntu grípa rangflokkun í báðar áttir?** Að flokka ákvarðanir eftir afturkræfni er eitt þeirra stjórnarháttavenja sem skila mestu vægi, og gildi hennar hrynur ef þú merkir hluti rangt: meðhöndlaðu afturkræft val sem óafturkræft og þú drekkir því í yfirvegun, meðhöndlaðu óafturkræft val sem afturkræft og þú afhendir gagnalíkan eða opinberan API-samning sem þú getur ekki afturkallað ódýrt. Samkeppnisáhættan er sú að sá sem er næst vinnunni kann að hallast að hraða, en miðlæg stjórn kann að hallast að varúð. Komdu með áþreifanleg dæmi í umræðuna: hvað myndi það raunverulega kosta, í tíma og peningum, að afturkalla hverja ákvörðun og hver ber þann kostnað. Í fyrirtækja- og opinberu samhengi gera innkaupaskuldbindingar og gögn í stórum stíl mörg val að einátta dyrum sem litu afturkræf út fyrirfram. Komdu þér saman um hver flokkar og byggðu upp venju að fá skjótt annað álit á öllu nálægt mörkunum, svo af skornum skammti rýni lendi þar sem afturköllun er raunverulega dýr.

2. **Hver á, fjármagnar og mannar troðnu slóðina, og hvað kemur í veg fyrir að hún hnigni í hliðvörð?** Troðin slóð virkar aðeins ef blessuðu sjálfgefnu valkostirnir eru raunverulega vel studdir og auðveldari en valkostirnir, og það krefst viðvarandi fjárfestingar sem er auðvelt að vanfjármagna. Málamiðlunin er skýr: vanfjármögnuð troðin slóð verður að safni skyldna án stuðnings, sem er einmitt sú hliðvarsla sem líkaninu var ætlað að koma í stað, og teymi fara þá fram hjá henni. Komdu með gögn um heilsu slóðarinnar: upptökuhlutfall, hve nýleg samþykkt verkfæri eru, hve hratt vettvangsteymið svarar og hve oft teymi sækja um að fara utan slóðar. Fyrir stórar og eftirlitsskyldar skipulagsheildir er troðin slóð líka hvernig samræmda valið verður auðvelt, svo fjármögnun hennar er regluvarslufjárfesting, ekki bara þægindi. Ákveddu skýran eiganda og fasta fjárveitingu og mældu hvort teymi velja slóðina því hún er raunverulega auðveldasta leiðin.

3. **Hvar fara teymi fram hjá stjórnarháttunum, og hvað segir þessi skuggaupplýsingatækni þér?** Teymi forðast samþykktu leiðina þegar hún er sársaukafyllri en leiðin í kringum hana, svo útbreidd skuggaupplýsingatækni er minna agavandamál en hönnunardómur um stjórnarhættina þína. Sjónarmiðin sem togast á eru raunveruleg: sum undanskot eru kærulaus og mörg eru skynsamleg forðun frá rýnistjórn sem hefur orðið að margra vikna biðröð. Komdu með gögnin: hvaða samþykktir eru sniðgengnar, hvaða óopinber verkfæri hafa hljóðlega breiðst út og hve langan tíma opinbera leiðin tekur í raun. Í fyrirtækja- og opinberu samhengi eru hagsmunir meiri, því óleyfileg verkfæri geta brotið úttektar-, öryggis- og innkaupaskyldur sem hafa lagalegt vægi. Ef mynstrið sýnir fólk fara fram hjá flöskuhálsi er lagfæringin að flýta og víkka troðnu slóðina og minnka umfang stjórnarinnar við fáar þverlægar, óafturkræfar ákvarðanir, ekki að bæta við fleiri samþykktum.

4. **Hve stór hluti afhendingargetu okkar fer í raun í að greiða niður tæknilega skuld, og getum við nefnt háu vaxta-atriðin sem hún ætti að beinast að fyrst?** Tæknileg skuld hegðar sér eins og samsettir vextir, hljóðlátur skattur á hverja framtíðarbreytingu, og stór skipulagsheild getur borið hana árum saman áður en nokkur tekur eftir því að kerfið er orðið hægt og brothætt að breyta. Þrýstingurinn á móti er hreinskilinn: hver klukkustund í skuld er klukkustund sem ekki fer í eiginleika sem forystan sér, svo niðurgreiðslan er það fyrsta sem skorið er þegar frestur þrengist. Komdu með raunveruleg gögn í umræðuna, skriflega skrá yfir mikilvæga skuld, heiðarlegt mat á viðvarandi kostnaði hvers atriðis og kostnaðinn við að laga það, og raunverulegt hlutfall nýlegrar afkastagetu sem fór í niðurgreiðslu á móti nýrri vinnu. Fyrir fyrirtæki og opinberar stofnanir á áratugalöngum tímasjóndeildarhring neyðir óstýrð skuld að lokum fram dýra endurskrif eða úttektarniðurstöðu, svo líttu á fasta niðurgreiðsluúthlutun sem áhættustýringu og ákveddu hver gætir hennar þegar tímaáætlun skríður til.

5. **Þegar við þurfum rökin að baki ákvörðun sem tekin var fyrir tveimur árum, getum við raunverulega fundið þau, og er einhver að halda þeirri skrá lifandi?** Allt gildi arkitektúrákvörðunarskrár er að rökin lifi þá sem tóku ákvörðunina, og það gildi hrynur ef ADR eru skrifaðar einu sinni, aldrei leitað í þeim og þær reka hljóðlega úr gildi. Spennan er milli skrifagans sem þarf til að fanga samhengi, valkosti og afleiðingar á ákvörðunarstundu og daglegs þrýstings til að afhenda bara og halda áfram. Komdu með áþreifanleg próf í umræðuna: veldu þrjár mikilvægar nýlegar ákvarðanir og sjáðu hvort einhver getur fundið skráð rök á mínútum, og athugaðu hvort úreltar ADR séu merktar sem slíkar en ekki hljóðlega mótsagnakenndar við núverandi vinnubrögð. Í fyrirtækja- og opinberu samhengi er sú leitanlega skrá einmitt rökstudda sönnunin sem endurskoðendur og eftirlitsaðilar krefjast, svo ákveddu hvar ADR búa, hver rýnir þær og hvað gerir ákvörðun nógu mikilvæga til að skrá.

6. **Hvenær endurskoðuðum við síðast stóra ákvörðun um að smíða eða kaupa gegn upprunalegum forsendum hennar, og myndum við yfirleitt taka eftir því þegar þær forsendur renna út?** Útvistunarval eru meðal dýrustu og erfiðustu ákvarðana til að afturkalla, og forsendurnar að baki þeim (verðlagning söluaðila, eigin mönnun, þroski opins valkosts) úreldast hljóðlega á meðan ákvörðunin helst fryst. Sjónarmiðin sem togast á vega sokkinn kostnað og röskun við að skipta á móti vaxandi kostnaði innilokunar, ófullkominnar passunar eða viðhaldsbyrði sem þú vilt ekki lengur. Komdu með upprunalegu ADR og yfirlýstar forsendur hennar, núverandi heildareignarkostnaðarmat fyrir hverja leið, með leyfum, samþættingu, mönnun og útgöngukostnaði, og hvert það merki, verðbreytingu eða stuðningslækkun, um að forsenda hafi breyst. Fyrir kaupendur hins opinbera og eftirlitsskylda gera innkaupareglur og margra ára samningar þessar einátta dyr sérstaklega bindandi, svo komdu þér saman fyrirfram um kveikjur og takt sem þvingar fram yfirvegaða endurákvörðun frekar en blinda endurnýjun.

## Sjónarhorn eftir geirum

**Sprotafyrirtæki.** Stýrðu nánast engu og hallaðu þér þungt á hraðann: fyrir afturkræf tvíátta dyra-val skaltu ákveða við skrifborðið og halda áfram. Taktu frá þína einu stjórnarháttavenju fyrir fáu einátta dyrnar, kjarna gagnalíkan eða grunnsöluaðila, og skráðu hverja í einni málsgrein svo framtíðar liðsfélagi sé ekki að deila um hana frá grunni. Slepptu rýnistjórnum og troðnum slóðum alveg, því í þinni stærð eru þær yfirbygging sem þú hefur ekki efni á og allt teymið deilir þegar samhenginu.

**Lítið fyrirtæki.** Án arkitekts á launaskrá skaltu gera smíða-eða-kaupa að miðlægri stjórnarháttaspurningu þinni og svara henni út frá heildareignarkostnaði frekar en smekk. Kjóstu sjálfgefið að kaupa eða taka upp vel studd verkfæri fyrir allt sem er ekki kjarnasérkenni þitt, því ævarandi viðhald er kostnaðurinn sem þú hefur síst efni á að bera. Haltu einni léttri ákvörðunarskrá svo rökin að baki fáu afdrifaríku valunum lifi þótt lykilmaður hætti.

**Stórfyrirtæki.** Vandinn þinn er að jafna sjálfstæði og samræmi yfir mörg teymi, svo fjárfestu í fjármagnaðri troðinni slóð og taktu frá þrönga, hraða arkitektúrrýnistjórn fyrir raunverulega þverlægar og óafturkræfar ákvarðanir. Staðlaðu ADR svo rök verði leitanlegt stofnanaminni og stýrðu tæknilegri skuld og útvistunarvali sem eignasöfnum með föstum fjárveitingum. Mældu hvort teymi velja slóðina því hún er auðveldust og minnkaðu hverja stjórn sem hefur hnignað í biðröð.

**Hið opinbera.** Skjalfestar, rökstuddar ákvarðanir eru ekki valkvæðar hér: endurskoðendur og eftirlitsaðilar ætlast til að sjá rökin, valkostina sem voru vegnir og forsendurnar að baki sérhverju afdrifaríku vali. Keyrðu smíða-eða-kaupa sem skráð heildareignarkostnaðarmat, virtu innkaupareglur sem takmarka innilokun eins aðila og haltu ADR sem úttektarhæfri sönnunarslóð. Taktu langan tímasjóndeildarhring alvarlega, því gagnalíkan eða skuldbinding við söluaðila sem gerð er í dag kann að binda skipulagsheildina í áratug, svo flokkaðu hana sem einátta dyr og yfirvegaðu í samræmi við það.

## Dæmi

**Sprotafyrirtæki.** Fjögurra manna sprotafyrirtæki tekur flestar ákvarðanir á mínútum yfir sameiginlegu skrifborði, og fyrir afturkræf tvíátta dyra-val er sá hraði raunverulegur kostur, svo þeir standa gegn allri stjórnarháttayfirbyggingu. En þegar þeir velja gagnagrunn og gagnalíkan sem verður sársaukafullt að breyta síðar (einátta dyr) staldra þeir við og skrifa eina málsgrein: valkostina, valið og forsendurnar að baki. Ári síðar, þegar þeir ná mörkum í stærðaraukningu, bjargar sú eina athugasemd þeim frá því að deila um spurninguna frá grunni. Þeir stýra nánast engu og taka frá einu léttu venjuna sína fyrir fáu ákvarðanirnar sem eru raunverulega dýrar að afturkalla.

**Stórfyrirtæki.** Vettvangsteymi stórs fyrirtækis voru lömuð af arkitektúrrýnistjórn sem þurfti að samþykkja hvert tæknival og skapaði margra vikna biðraðir. Fyrirtækið endurbyggði stjórnarhætti í kringum troðna slóð: samansett skrá yfir samþykkt, fullkomlega studd tungumál, gagnageymslur og leiðslur sem teymi gátu tekið upp samstundis. ADR skráðu hverja ákvörðun um að víkja frá, og hröð, ráðgefandi rýni sinnti aðeins valkostum utan slóðar. Umfang stjórnarinnar minnkaði í staðlasetningu og fáeinar raunverulega þverlægar ákvarðanir. Afhending hraðaðist verulega. Samræmi batnaði í raun, því auðvelda leiðin var nú sú reglufylgna. Og ADR-safnið gaf skipulagsheildinni leitanlega skrá yfir hvers vegna hlutir voru smíðaðir eins og þeir voru.

**Hið opinbera.** Ráðuneyti stóð frammi fyrir stórri smíða-eða-kaupa ákvörðun um málastjórnunarvettvang undir ströngum innkaupa- og úttektarreglum. Frekar en að ákveða eftir smekk framkvæmdi það skjalfest heildareignarkostnaðarmat á þremur valkostum: að smíða sérsniðið, kaupa viðskiptavöru og taka upp opinn grunn. Það vó leyfi, samþættingu, langtímaviðhald, mönnun og innilokun og skráði ákvörðunina og forsendur hennar sem ADR. Árum síðar, þegar skilmálar söluaðila breyttust, endurskoðaði ráðuneytið þá ADR, fann að upprunalegar forsendur þess héldu ekki lengur og tók nýja ákvörðun með fulla vitneskju um fyrri rök, og forðaðist blinda og kostnaðarsama flutninga. Skráð rök voru líka einmitt rökstudda sönnunin sem endurskoðendur kröfðust.

## Viðskiptarök: hvatar, ávöxtun fjárfestingar og heildarkostnaður

Ákvarðanir eru áhrifamesti og minnst sýnilegi kostnaðurinn í hugbúnaði. Ein léleg, óafturkræf arkitektúr- eða útvistunarákvörðun getur lagt árabil af hemli eða lagfæringarkostnað upp á níu tölustafi. Að stýra henni vel, nokkrar klukkustundir af yfirvegun og skrifleg skrá, kostar næstum ekkert í samanburði. Ávöxtun ADR og framsals byggðs á afturkræfni kemur frá tveimur upptökum: að forðast dýr mistök í einátta dyra-ákvörðunum og að forðast sóaða yfirvegun og endurvinnslu í öllu öðru. Skráð rök skera líka endurtekinn kostnað við að deila aftur um útkljáðar spurningar og við að teymi rekja ásetning erfðra kerfa afturábak.

Tæknileg skuld gerir TCO-rökin áþreifanleg. Óstýrð skuld hegðar sér nákvæmlega eins og samsettir vextir: vaxandi skattur á hverja framtíðarbreytingu, þar til kerfið verður í reynd óviðhaldanlegt og krefst dýrs endurskrifs. Að stýra skuld sem eignasafni, með fastri úthlutun afkastagetu til að greiða niður háu vaxtaatriðin, er mun ódýrara en kreppan sem annars kemur. Góðir stjórnarhættir eru ódýrir í upptöku, aðallega agi þess að skrifa ákvarðanir niður og fjárfesting fyrirfram í troðinni slóð. Að sleppa þeim er dýrt: þú borgar í forðanlegum endurskrifum, innilokunarvandamálum, úttektarbrestum og glötuðu stofnanaminni. Til að sannfæra forystu skaltu setja stjórnarhætti fram á hennar tungumáli: áhættulækkun, forðuð endurvinnsla, hraðari afhending gegnum troðnu slóðina og úttektarhæf rökstuðningur. Sýndu að markmiðið er ekki meira ferli heldur betur miðað ferli, þung rýni aðeins þar sem afturköllun er dýr og núningslaus hraði alls staðar annars staðar.

## Andmynstur og gildrur

- Óskjalfestar ákvarðanir: rök glatast um leið og fólkið sem tók þær hættir.
- Flöskuháls samþykktarstjórnar: miðlægur aðili sem hvert verkefni þarf að bíða í röð fyrir aftan.
- Eitt ferli fyrir allt: að þvinga léttvægar afturkræfar ákvarðanir í gegnum þunga rýni.
- Greiningarlömun: að kvelja sig yfir auðveldlega afturkræfum tvíátta dyra-ákvörðunum.
- [Skuggaupplýsingatækni](https://en.wikipedia.org/wiki/Shadow_IT): teymi sem sniðganga stjórnarhætti alveg því samþykkta leiðin er of sársaukafull.
- Ósýnileg tæknileg skuld: skuld sem aldrei er skráð, aldrei greidd niður, safnast hljóðlega upp.
- Smíða-allt eða kaupa-allt viðbrögð: útvistun eftir vana frekar en TCO-greiningu.
- Stjórnarháttaleikhús: skjöl og stjórnir sem eru til sýnis en móta ekki ákvarðanir.

## Þroskalíkan

- Stig 1 (Upphaf): Ákvarðanir eru ad hoc og óskráðar. Stjórnarhættir eru annaðhvort fjarverandi eða altækur flöskuháls. Tæknileg skuld er ósýnileg og rökin að baki vali gufa upp þegar fólk hættir.
- Stig 2 (Þróun): Sumar ákvarðanir eru skjalfestar og einhver rýni er til staðar, en vinnubrögðin eru ósamkvæm milli teyma og ferlið oft í ósamræmi við þunga og afturkræfni ákvörðunarinnar.
- Stig 3 (Stöðlun): ADR, troðin slóð, framsal byggt á afturkræfni og skuldaskrá eru skjalfest og framfylgt um alla skipulagsheildina, svo reglufylgna valið er auðvelt sjálfgefið og rök eru leitanleg.
- Stig 4 (Stjórnun): Stjórnarhættir eru mældir gegn grunnlínum: upptaka troðinnar slóðar, ADR-þekja, ákvörðunarhringrásartími, skuld sem hlutfall afkastagetu og undanþáguhlutfall utan slóðar eru raktar, og ákvarðanir um að greiða niður skuld eða endurskoða útvistun eru kallaðar fram af þeim gögnum frekar en kreppu.
- Stig 5 (Samhæfing): Stjórnarhættir eru stöðugt stilltir og samþættir afhendingu og áhættuáætlun. Rýni er nákvæmlega miðuð á óafturkræfar ákvarðanir. Skuld og útvistunarval eru virkt endurjöfnuð sem eignasöfn og endurákveðin á grundvelli gagna eftir því sem aðstæður breytast.

## Hugmyndir til umræðu

- Getum við fundið skráð rök að baki mikilvægustu nýlegu ákvörðunum okkar?
- Hvar eru stjórnarhættir okkar flöskuháls og hvar eru þeir fjarverandi þegar þörf er á þeim?
- Hverjar af núverandi ákvörðunum okkar eru einátta dyr og meðhöndlum við þær sem slíkar?
- Hve mikið af afkastagetu okkar fer í að greiða niður tæknilega skuld og er það nóg?
- Fylgja teymin okkar troðnu slóðinni því hún er raunverulega auðveldasta leiðin, eða fara þau fram hjá henni?
- Hvenær endurskoðuðum við síðast stóra smíða-eða-kaupa ákvörðun gegn upprunalegum forsendum hennar?

## Helstu atriði

- Skráðu mikilvægar ákvarðanir og rök þeirra með ADR. Gerðu rök varanleg.
- Stýrðu með troðnum slóðum og sjálfgefnum gildum, ekki hliðvörslu í hverju tilviki.
- Láttu ferlisþunga samsvara þunga og afturkræfni ákvörðunar. Framseldu tvíátta dyr, yfirvegaðu einátta dyr.
- Greindu smíða-kaupa-taka upp út frá heildareignarkostnaði og skráðu forsendurnar.
- Stýrðu tæknilegri skuld sem skýru eignasafni með fastri niðurgreiðsluúthlutun.
- Hafðu stjórnarhætti gagnsæja og létta. Beindu af skornum skammti rýni þangað sem afturköllun er dýr.

## Heimildir og frekari lestur

- Michael Nygard, "Documenting Architecture Decisions" (the original ADR pattern)
- Gregor Hohpe, "The Software Architect Elevator" and "37 Things One Architect Knows"
- Amazon shareholder letters on Type 1 vs Type 2 (one-way vs two-way door) decisions
- Ward Cunningham, the original "technical debt" metaphor
- Martin Fowler, writings on technical debt and evolutionary architecture
- Neal Ford, Rebecca Parsons, Patrick Kua, "Building Evolutionary Architectures"
- Nicole Forsgren, Jez Humble, Gene Kim, "Accelerate" (loosely coupled architecture and autonomy)
- ISO/IEC/IEEE 42010 on architecture description
