# 2.15 Villuleit og bilanagreining

## Yfirlit og tilgangur

Villuleit er agaða verkið að komast að því hvers vegna kerfi gerir eitthvað sem það ætti ekki að gera, og bilanagreining er sama færni beint að keyrandi framleiðslukerfi undir tímapressu. Hvort tveggja er [vísindaleg aðferð](https://en.wikipedia.org/wiki/Scientific_method) beitt á galla: þú tekur eftir óvæntri hegðun, myndar tilgátu um orsök hennar, hannar tilraun sem gæti staðfest eða hrakið hana og lætur sönnunargögnin, ekki grun þinn, segja þér hverju á að breyta. Gert á þennan hátt er villuleit lærð, kennanleg verkfræðifærni. Gert sem þjóðtrú verður hún hjátrú: að breyta handahófskenndum línum, endurræsa netþjóna og vona.

Fyrir stórt teymi er munurinn dýr. Einn erfiður galli getur dregið að verkfræðinga yfir nokkrar þjónustur, étið bakvaktartíma og stöðvað útgáfu. Þegar hver og einn villuleitar eftir innsæi safnast sú fyrirhöfn ekki upp, því enginn getur endurskapað eða útskýrt hvað aðrir reyndu. Þegar teymið deilir aðferð (endurskapa fyrst, einangra með leit, fanga gallann í mistakast-prófi, laga síðan) breytist sama fyrirhöfn í endurtakanlegt ferli og vaxandi afturfaraprófasafn. Villuleit tengist þétt prófunarstefnu (kafli 2.4), hugbúnaðargæðum (kafli 2.11) og smíðavenjunum (kafli 2.9) sem gera kóða greinanlegan í fyrsta lagi.

Í fyrirtækja- og opinberu umhverfi hækka hagsmunirnir. Fyrirtækjagallar fara yfir þjónustu- og teymismörk, svo sá sem sér einkennið er sjaldan sá sem á orsökina. Opinber kerfi bæta við skorðum sem flestir verkfræðingar mæta aldrei: loftbil eða takmörkuð umhverfi þar sem þú getur ekki tengt villuleitarforrit við framleiðslu, endurgeranlegar smíðar sem verður að greina úr afurðum og úttektarslóðir sem verða að skrá hvað þú breyttir og hvers vegna. Í öllum þremur er markmiðið það sama: að skipta ágiskunum út fyrir sönnunargögn.

## Meginreglur

- **Endurskapaðu áður en þú gerir tilgátur.** Galli sem þú getur ekki kallað fram eftir pöntun er orðrómur, ekki galli.
- **Villuleit er tilgátuprófun.** Segðu hvað þú trúir, hannaðu síðan ódýrustu tilraunina sem gæti sannað þig rangan.
- **Lestu villuna og kallstaflann fyrst.** Kerfið segir þér venjulega hvar það brotnaði áður en þú breytir línu.
- **Leitaðu í vandarýminu, skannaðu það ekki.** Helmingaðu grunaða svæðið í hverju skrefi í stað þess að lesa ofan frá og niður.
- **Minnkaðu í lágmark.** Strípaðu tilvikið þar til aðeins nauðsynlega kveikjan er eftir.
- **Ein breyting í einu.** Haglabyssubreytingar eyðileggja sönnunargögnin sem hefðu sagt þér hvaða breyting skipti máli.
- **Fangaðu gallann í mistakast-prófi áður en þú lagar.** Lagfæringin er aðeins sönnuð þegar það próf verður grænt og helst grænt.
- **Finndu rótarorsökina, ekki næsta einkenni.** Plástur sem felur einkennið skilur gallann eftir til að koma aftur.

## Ráðleggingar

### Endurskapaðu gallann áreiðanlega áður en þú breytir nokkru

Fyrsta verk þitt er áreiðanleg endurskapan: röð skrefa eða sjálfvirkt tilvik sem kallar fram gallann eftir pöntun. Án hennar geturðu ekki greint raunverulega lagfæringu frá tilviljun, því einkennið getur komið og farið af ástæðum sem þú stjórnaðir aldrei. Negldu niður inntökin, umhverfið, útgáfurnar og tímasetninguna. Ef gallinn er slitróttur skaltu leita að falda breytunni sem lætur hann birtast (tiltekin gagnafærsla, klukkumörk, samtímabeiðni) þar til endurskapanin er áreiðanleg. Áreiðanleg endurskapan er verðmætasta einstaka afurðin í villuleit, því allt eftir hana verður mælanlegt.

### Lestu villuna, skrárnar og kallstaflann áður en þú snertir kóða

Áður en þú myndar eina einustu tilgátu skaltu lesa það sem kerfið sagði þér þegar. [Kallstaflinn](https://en.wikipedia.org/wiki/Stack_trace) (skráin um kallakeðjuna á augnabliki bilunarinnar) nefnir venjulega skrána, línuna og röðina sem brást. Undantekningarskilaboðin, skráarlínurnar í kringum þau og gildin í gildissviði þrengja leitina áður en þú hefur breytt nokkru. Verkfræðingar sóa klukkustundum í að gera tilgátur um orsakir sem rakningin útilokaði á fyrstu línu. Líttu á villuúttakið sem fyrsta vitnið, lestu það vandlega og til fulls og ákveddu síðan hvað á að rannsaka.

### Einangraðu með tvíundarleit í vandarýminu

Skannaðu ekki kóðann ofan frá og niður. Leitaðu í honum. Notaðu [tvíundarleit](https://en.wikipedia.org/wiki/Binary_search_algorithm): finndu punkt þar sem ástandið er enn gott og punkt þar sem það er þegar slæmt, athugaðu síðan miðpunktinn og endurtaktu, helmingaðu grunaða svæðið í hvert skipti. Þetta breytir þúsund lína leit í tíu spurningar. Þegar afturförin birtist yfir svið commit skaltu beita sömu hugmynd á söguna með helmingaleit: `git bisect` gengur um commit-sviðið og þú merkir hverja endurskoðun góða eða slæma þar til hún nefnir nákvæmu breytinguna sem kynnti gallann. Sjálfvirknivæddu góða-eða-slæma prófið og helmingaleit keyrir sig sjálf.

### Minnkaðu í lágmarks endurskapanlegt dæmi

Þegar þú getur kallað fram gallann skaltu minnka hann. [Lágmarks endurskapanlegt dæmi](https://en.wikipedia.org/wiki/Minimal_reproducible_example) er minnsta inntak og kóðaleið sem enn bilar: fjarlægðu gögn, eiginleika og skref þar til frekari fjarlæging lætur gallann hverfa. Minnkun er ekki aukavinna. Hver þáttur sem þú útrýmir er orsök sem þú hefur útilokað, svo lágmarkstilvikið bendir oft beint á gallann. Þegar inntak er stórt eða skipulagt skaltu sjálfvirknivæða minnkunina með [delta-villuleit](https://en.wikipedia.org/wiki/Delta_debugging), reikniriti sem fjarlægir kerfisbundið bita úr biluðu inntaki til að finna lágmarks bilaða hlutmengið. Lítil, sjálfstæð endurskapan er líka besta mögulega villutilkynning til að afhenda öðru teymi.

### Mældu með skrám, notaðu síðan gagnvirkt villuleitarforrit

Láttu verkfærið passa gallann. Skráning og markviss mæling eru best þegar þú þarft að sjá hegðun yfir tíma, yfir ferli eða í umhverfi sem þú getur ekki gert hlé á. Gagnvirkt villuleitarforrit, sem leyfir þér að setja stöðvunarpunkta, stíga línu fyrir línu og skoða lifandi ástand, er best þegar þú getur keyrt kóðann staðbundið og þarft að horfa náið á eina keyrslu. Bættu við mælingu sem yfirvegaðri tilraun tengdri tilgátu, ekki sem dreifðum prent-yfirlýsingum, og fjarlægðu hana eða upphefðu í varanlega skipulagða skráningu þegar gallinn er leystur. Í framleiðslu skaltu hallast að sýnileikadrifinni villuleit: hánæmir atburðir og dreifð rakning (kafli 9.2) leyfa þér að fylgja einni beiðni yfir margar þjónustur, sem er oft eina leiðin til að villuleita dreift kerfi sem þú getur ekki tengt villuleitarforrit við.

### Skrifaðu mistakast-próf sem fangar gallann áður en þú lagar hann

Áður en þú skrifar lagfæringuna skaltu skrifa próf sem bilar vegna gallans. Þetta gerir þrennt í einu: það sannar að þú skiljir orsökina í raun, skilgreinir nákvæmlega hvað „lagað“ þýðir og verður varanlegur varðmaður. Gerðu síðan lagfæringuna og horfðu á prófið verða grænt. Það próf gengur nú í safnið þitt sem [afturfaraprófunar](https://en.wikipedia.org/wiki/Regression_testing)varðmaður, svo sami galli geti ekki snúið aftur óséður. Þessi venja tengir villuleit beint við prófunarstefnu þína (kafli 2.4): hver erfiður galli sem þú leysir skilur safnið eftir sterkara en hann fann það, og óáreiðanlegt próf fær sömu meðferð (endurskapaðu óákvörðunarhæfið, varðu síðan gegn því) frekar en endurtekningarskýringu.

### Finndu rótarorsökina og haltu greiningunni án sakbendingar

Að laga einkennið er ekki að laga gallann. Raktu bilunina aftur til sannrar upptaka hennar, spurðu hvers vegna á hverju lagi þar til þú nærð orsök sem þú getur fjarlægt frekar en hulið. Fyrir galla sem náðu framleiðslu skaltu keyra rótarorsakagreiningu án sakbendingar sem hluta af atvikastjórnun (kafli 9.3): einbeittu þér að kerfis- og ferlisaðstæðunum sem leyfðu gallanum að afhendast og lifa, aldrei að einstaklingnum sem skrifaði línuna. Sakbending rekur upplýsingar í felur og villuleit gengur á upplýsingum. Afraksturinn er bæði lagfæring og breyting á því hvernig flokkur galla er gripinn fyrr næst.

## Málamiðlanir: kostir og gallar

| Nálgun | Kostir | Gallar |
|---|---|---|
| Skráning og mæling | Virkar í framleiðslu og dreifðum kerfum, fangar hegðun yfir tíma | Hávaði, kostnaður og skráasprenging, getur truflað tímasetningargalla |
| Gagnvirkt villuleitarforrit | Nákvæm, lifandi ástandsskoðun, hratt fyrir staðbundna galla | Gagnslaust í takmarkaðri eða loftbilsframleiðslu, getur falið samtímagalla |
| Endurskapa-fyrst agi | Breytir ágiskun í mælingu, gerir mistakast-próf mögulegt | Hægt fyrirfram, sumir gallar eru raunverulega erfiðir að kalla fram |
| Tvíundarleit og helmingaleit | Hröð einangrun, jafnvel í ókunnugum kóða | Þarf áreiðanlegt góða-eða-slæma próf, erfitt þegar gallar víxlverka |
| Delta-villuleitarminnkun | Minnkar risastór inntök sjálfvirkt að kveikjunni | Uppsetningarkostnaður, gerir ráð fyrir að bilunin sé ákvörðunarhæf |
| Lagaðu einkennið núna | Endurheimtir þjónustu hratt undir þrýstingi | Skilur rótarorsök eftir til að snúa aftur, safnar skuld |

Meginspennan er hraði gegn vissu. Undir framleiðsluatviki gætirðu þurft að stöðva blæðinguna fyrst (afturköllun eða einkennisplástur) til að endurheimta þjónustu, og það er lögmætt. Mistökin eru að stoppa þar. Leystu spennuna með því að aðskilja verkin tvö: dragðu úr hratt til að vernda notendur, endurskapaðu síðan, finndu rótarorsökina og bættu við afturfaravarðmanninum áður en þú telur gallann lokaðan. Einkennislagfæring án eftirfylgni er galli sem þú hefur samþykkt að hitta aftur.

## Spurningar til að ræða með teyminu

1. **Þegar einhver lendir á erfiðum galla, hvað er það fyrsta sem hann gerir og er það að endurskapa eða giska?** Heiðarlega svarið afhjúpar hvort teymið þitt hefur sameiginlega aðferð eða herbergi fullt af einkaþjóðtrú. Biddu fólk að segja frá síðasta erfiða galla sínum upphátt: fékk það áreiðanlega endurskapan fyrst, eða byrjaði það að breyta kóða og endurræsa hluti? Teymi sem endurskapar fyrst getur afhent galla milli manna, því endurskapanin ferðast. Teymi sem giskar getur það ekki, því hver tilraun er óendurtakanleg. Þetta skiptir meira máli eftir því sem teymið stækkar, því sá sem sér einkenni er sífellt oftar ekki sá sem getur lagað það. Ef sjálfgefið er að giska skaltu koma þér saman um endurskapa-fyrst sem viðmið og gera hreina endurskapan að aðgangseyri að galla-miða.

2. **Koma gallarnir sem við lögum aftur og myndum við vita það ef þeir gerðu það?** Galli sem snýr aftur er galli þar sem rótarorsökin var aldrei fjarlægð og lagfæringin aldrei varin með prófi. Dragðu síðasta ársfjórðung atvika og enduropnaðra miða og teldu hve mörg voru endurtekningar eða náskyldir fyrri göllum. Hver endurtekning er sönnun þess að teymið plástraði einkenni, sleppti mistakast-prófinu eða stöðvaði rótarorsakagreiningu of snemma. Lagfæringin er regla: enginn galli er lokaður fyrr en próf sem bilar á gömlu hegðuninni stenst á nýju og gengur í safnið. Komdu með einn nýlegan endurtekinn galla og spurðu hvaða varðmaður hefði gripið hann, því sá varðmaður er það sem þig vantaði.

3. **Getum við yfirleitt villuleitað framleiðslukerfi okkar, miðað við hvernig við megum snerta þau?** Í fyrirtækja- og sérstaklega opinberu umhverfi geturðu oft ekki tengt villuleitarforrit, ekki endurskapað með raunverulegum gögnum og ekki breytt keyrandi kerfi án úttektarslóðar. Ef eina villuleitaraðferð þín er staðbundið gagnvirkt villuleitarforrit ertu blindur einmitt þar sem erfiðustu gallarnir búa. Spurðu hvaða sönnunargögn framleiðslubilun skilur í raun eftir: skipulagðar skrár, dreifðar rakningar (kafli 9.2), minnisafrit eða endurgeranlegar smíðaafurðir. Ákveddu núna hvað þú verður að fanga sjálfgefið svo framtíðaratvik sé greinanlegt, því þú getur ekki bætt mælingu við bilun sem þegar gerðist. Í eftirlitsskyldu umhverfi skaltu staðfesta að sama slóð fullnægi líka úttektarskyldum þínum.

4. **Þegar framleiðsluatvik neyðir okkur til að stöðva blæðinguna hratt, hvernig tryggjum við að rótarorsökin finnist samt eftir á?** Undir atviki er afturköllun eða einkennisplástur rétta fyrsta hreyfingin til að vernda notendur, en hættan er að miðinn lokist um leið og þjónusta kemur aftur og undirliggjandi gallinn sé aldrei greindur. Fyrir stórt teymi er þetta þar sem skuld safnast ósýnilega, því sami flokkur bilunar kemur upp á annarri þjónustu og hjá öðrum bakvaktarverkfræðingi mánuðum síðar. Komdu með síðustu alvarleikastig-eitt atvik þín og athugaðu hvert: fylgdi endurskapan, rótarorsakagreining og afturfaravarðmaður mildun, eða endaði sagan á „þjónusta endurheimt“? Komdu þér saman um skýra reglu að mildað atvik haldist opið þar til rótarorsökin er skilin og varin og nefndu hver á eftirfylgnina. Í fyrirtækja- og opinberu umhverfi skaltu tengja þetta við atvikastjórnunarferli þitt (kafli 9.3) svo eftiratvikarýni sé skyldubundið, úttektarhæft skref frekar en kurteisi sem rennur burt þegar næsti eldur byrjar.

5. **Hve mikið af bilun getum við í raun endurgert eftir á og hver ákvað hvað við fangum sjálfgefið?** Þú getur ekki bætt mælingu við bilun sem þegar hefur gerst, svo greinanleiki hvers atviks er ákveðinn fyrirfram af skránum, rakningunum, mælikvörðunum og minnisafritunum sem þú valdir að senda. Sjónarmiðið á móti er kostnaður og hávaði: hánæmir atburðir og full rakning eru ekki ókeypis, og ofskráning grefur merkið á meðan hún blæs út geymslu og, í eftirlitsskyldu samhengi, gagnavarðveisluáhættu þína. Komdu með raunverulegt nýlegt atvik og spurðu hvaða sönnunargögn það skildi eftir, unnið síðan afturábak að því hvað þú vildir að þú hefðir fangað og hvað það myndi kosta að halda. Ákveddu af ásetningi hvaða merki eru sjálfgefin á móti úrtaks- eða valkvæð og skráðu þá ákvörðun svo hún sé stefna en ekki slys. Fyrir fyrirtækja- eða opinbert kerfi skaltu bæta við hver er ábyrgur fyrir þeirri sýnileikafjárhagsáætlun og hvort fönguð slóð fullnægi líka úttektar-, persónuverndar- og gagnabúsetuskyldum.

6. **Lítum við á villuleit sem kennda, mælanlega færni, eða drekka nýir verkfræðingar hana í sig af sjálfu sér?** Villuleit er lærð, en flest teymi kenna hana aldrei skýrt, svo byrjendur erfa hvaða þjóðtrú sem er næst þeim og endurskapa-fyrst aðferðin dreifist ójafnt eða alls ekki. Spennan er sú að yfirveguð kennsla (pörun á erfiðum göllum, að skrifa upp eftiratvikaniðurstöður, að rekja mælikvarða) kostar tíma eldri manna sem alltaf finnst þörf annars staðar. Komdu með tvær tölur í umræðuna: endurtekna gallahlutfallið þitt og tímann til greiningar, því ef þú getur ekki mælt þær geturðu ekki sagt hvort aðferðin þín er að batna eða hnigna. Íhugaðu hvort móttaka felur í sér raunverulega villuleitaræfingu og hvort rótarorsakaniðurstöður næra í raun fyrri greiningu. Í stórri eða opinberri skipulagsheild verður skjalfest, mæld villuleitarvenja líka sönnun um verkfræðinákvæmni sem endurskoðendur, eftirlitsaðilar og eftirlitsstofnanir búast æ oftar við að sjá.

## Sjónarhorn eftir geirum

**Sprotafyrirtæki.** Með handfylli verkfræðinga og ekkert svigrúm er markmið þitt að gera galla ódýra að endurskapa og ómögulega að gleyma, ekki að smíða þungt ferli. Hallaðu þér að `git bisect`, hraðri staðbundinni endurskapan og einu mistakast-prófi fyrir hvern lagaðan galla, því sú venja kostar mínútur og stöðvar þig frá því að borga aftur fyrir sama galla meðan þú reynir að afhenda. Slepptu formlegum eftirrýnum, en slepptu aldrei afturfaraprófinu: það er eina afurðin sem er nógu lítil til að hafa alltaf efni á og nógu verðmæt til að halda alltaf.

**Lítið fyrirtæki.** Þú hefur líklega engan sérstakan áreiðanleika- eða sýnileikasérfræðing og þröngt verkfærafjárhagsáætlun, svo kjóstu það sem stakkurinn þinn gefur þér þegar: læsilega kallstafla, skipulagðar skrár og rakninguna sem er innbyggð í rammana og hýstu þjónusturnar sem þú hefur keypt. Þegar þú metur nýjan vettvang skaltu vega hve greinanlegar bilanir hann gerir, því ódýrt verkfæri sem felur hvað fór úrskeiðis kostar þig miklu meira í ágiskunartíma en leyfið sparaði. Endurskapa-fyrst og ein-breyting-í-einu eru ókeypis agar sem borga sig hraðast þegar enginn hefur stundir aflögu.

**Stórfyrirtæki.** Erfiðu gallarnir þínir fara yfir þjónustu- og teymismörk, svo sá sem sér einkennið á sjaldan orsökina og sameiginleg aðferð skiptir meira máli en færni nokkurs einstaklings. Staðlaðu endurskapa-fyrst, tvíundarleitareinangrun, mistakast-próf fyrir lagfæringu og eftirrýni án sakbendingar yfir teymi og fjárfestu í dreifðri rakningu (kafli 9.2) svo hægt sé að fylgja einni beiðni yfir þjónustur. Stýrðu villuleit sem mældri getu: rektu endurtekið gallahlutfall og tíma til greiningar og færðu rótarorsakaniðurstöður aftur inn í fyrri greiningu svo sami flokkur bilunar fari ekki hring um þjónustukortið þitt.

**Hið opinbera.** Innkaupareglur, takmörkuð umhverfi og almenn ábyrgð móta hvort og hvernig þú mátt villuleita yfirleitt. Þú getur oft ekki tengt villuleitarforrit við framleiðslu né afritað borgaragögn á fartölvu, svo hannaðu fyrir greiningu úr því sem er leyft: endurgeranlegar smíðar, tilbúnar færslur í einangruðu afgirtu svæði og skipulagðar skrár og rakningar fangaðar sjálfgefið. Skráðu hvert greiningarskref og hverja breytingu í úttektarslóðina og krefstu þess að söluaðilar afhjúpi nægilega fjarmælingu og smíðaendurgeranleika til að þú getir rannsakað bilanir sjálfstætt frekar en að reiða þig á orð birgis.

## Dæmi

**Sprotafyrirtæki.** Fjögurra verkfræðinga teymi sér afgreiðslu mistakast hjá broti notenda, en aldrei í prófun. Í stað þess að giska fangar einn verkfræðingur áreiðanlega endurskapan með því að endurspila nákvæma bilaða beiðnihleðsluna, les síðan kallstaflann sem þeir höfðu verið að hunsa, sem bendir á dagsetningarþáttunarkall. Fljótleg `git bisect` yfir commit vikunnar nefnir breytinguna sem skipti um dagsetningarbókasafn. Þeir skrifa mistakast-próf með villutímastimplinum, laga þáttarann, horfa á prófið verða grænt og halda því í safninu. Öll rannsóknin tekur eftirmiðdag því þeir endurskópu áður en þeir gerðu tilgátur, og gallinn snýr aldrei aftur.

**Stórfyrirtæki.** Greiðsluvettvangur sér slitrótt tímamörk sem ekkert eitt teymi getur útskýrt, því einkennið birtist í afgreiðslu en orsökin býr þrjár þjónustur í burtu. Bakvaktarverkfræðingar nota dreifða rakningu (kafli 9.2) til að fylgja einni bilaðri beiðni yfir þjónustumörk og finna niðurstreymis kall sem stundum læsist undir samtímaálagi, klassískt [kappakstursástand](https://en.wikipedia.org/wiki/Race_condition) þar sem niðurstaðan veltur á óheppilegri tímasetningu milli þráða. Þeir endurskapa það með álagsprófi, fanga það í mistakast-samþættingarprófi, laga læsinguna og halda eftirrýni án sakbendingar (kafli 9.3) sem bætir við rakningarspönn og viðvörun svo næsta tilvik sé gripið á mínútum, ekki dögum.

**Hið opinbera.** Bótastofnun rekur málakerfi sitt í loftbilsumhverfi þar sem verkfræðingar geta ekki tengt villuleitarforrit við framleiðslu og ekki afritað borgaragögn á fartölvur sínar. Útreikningsgalli birtist í afstemmingu. Teymið villuleitar úr því sem umhverfið leyfir: skipulögðum skrám, endurgeranlegri smíði sem þeir geta sett upp í einangruðu prófasvæði og tilbúnum færslum sem endurskapa bilaða tilvikið. Hvert greiningarskref er skráð í úttektarslóðina, lagfæringin fylgir með mistakast-svo-stenst prófi sem sönnunargagn og rótarorsakagreiningin nærir nýja athugun fyrir útgáfu. Því endurskapanin notaði tilbúin gögn yfirgaf engin borgarafærsla mörkin.

## Viðskiptarök: hvatar, ávöxtun fjárfestingar og heildarkostnaður

Ávöxtun agaðrar villuleitar er mæld í verkfræðistundum sem ekki fara í að giska og göllum sem koma ekki aftur. Ógreindur slitróttur galli getur étið daga af tíma eldri manna og endurteknar bakvaktarstigmagnanir. Endurskapa-fyrst aðferð breytir því í afmarkað, framseljanlegt verkefni, og mistakast-próf venjan stöðvar sama galla frá því að rukka þig aftur næsta ársfjórðung. Yfir stóra skipulagsheild er samanlögð áhrif þess að borga aldrei aftur fyrir sama galla umtalsverð, og hún bætir beint bilanahlutfall breytinga og meðaltíma til endurheimtar sem forystan fylgist þegar með.

Heildareignarkostnaðurinn er aðallega þjálfun og verkfæri og er hóflegur. Þú þarft sameiginlegar venjur (endurskapa fyrst, ein breyting í einu, mistakast-próf fyrir lagfæringu), villuleitarforrit og rakningu sem þegar eru algeng í verkfærakeðjunni og sýnileikafjárfestinguna sem lýst er í kafla 9.2. Stærri, falinn kostnaðurinn er valkosturinn: menning hjátrúar þar sem verkfræðingar beita haglabyssubreytingum, einkenni eru plástruð og snúa aftur og bakvaktarálag vex án takmarka. Að minnka bakvaktar-leiðindavinnu eina og sér réttlætir oft fjárfestinguna, og rökin fyrir forystu eru einfaldast sett fram sem færri endurtekin atvik og hraðari endurheimt fyrir einskiptis kostnað í venjum og mælingu.

## Andmynstur og gildrur

- **Haglabyssuvillaleit:** að breyta mörgu í einu, svo jafnvel lagfæring kennir þér ekkert um orsökina.
- **Að laga án þess að endurskapa:** að lýsa yfir sigri á galla sem þú gast aldrei kallað fram eftir pöntun.
- **Að hunsa villuúttakið:** að gera tilgátur um orsakir sem kallstaflinn hefur þegar útilokað.
- **Einkennaplástrar:** að þagga niður einkennið á meðan rótarorsökin lifir til að snúa aftur.
- **Prentyfirlýsingasprengja:** dreift villuleitarúttak skilið eftir í kóðanum og bætir við hávaða í stað tilraunar tengdrar tilgátu.
- **Afturfaraprófi sleppt:** að laga gallann en skilja engan varðmann eftir, svo hann geti hljóðlega komið aftur.
- **Að endurtaka óáreiðanleg próf:** að fela óákvörðunarhæfi með endurtekningum í stað þess að villuleita undirliggjandi kappakstursástand eða [heisenbug](https://en.wikipedia.org/wiki/Heisenbug), galla sem breytist eða hverfur um leið og þú reynir að fylgjast með honum.
- **Eftirrýni með sakbendingum:** að refsa höfundinum, sem rekur upplýsingarnar sem villuleit byggir á í felur.

## Þroskalíkan

- **Stig 1, Upphaf:** Villuleit er einstaklingsþjóðtrú og viðbrögð. Verkfræðingar giska, beita haglabyssubreytingum og endurræsa hluti. Gallar eru lagaðir við einkennið, endurskapanir eru sjaldgæfar og sömu gallar endurtaka sig. Framleiðsla er varla greinanleg og enginn getur afhent galla til neins því engin tilraun er endurtakanleg.
- **Stig 2, Þróun:** Sumir verkfræðingar endurskapa áreiðanlega, lesa kallstafla og nota villuleitarforrit, en vinnubrögðin eru ósamkvæm og breytileg frá manni til manns og teymi til teymis. Skráning er til en hávaðasöm og óskipulögð. Lagfæringar fylgja stundum mistakast-prófi, oft ekki, og rótarorsakagreining gerist aðeins þegar einhver krefst hennar.
- **Stig 3, Stöðlun:** Endurskapa-fyrst, tvíundarleitareinangrun, ein breyting í einu og mistakast-próf fyrir lagfæringu eru skjalfest teymisviðmið framfylgd um skipulagsheildina. Helmingaleit og delta-villuleitarminnkun eru algeng venja. Framleiðsla hefur skipulagða skráningu og rakningu (kafli 9.2) og eftirrýni án sakbendingar (kafli 9.3) eru staðlað viðbragð við hverjum galla sem slapp.
- **Stig 4, Stjórnun:** Villuleitarvenjan er mæld og stýrð gegn grunnlínum. Endurtekið gallahlutfall, tími til greiningar, fjöldi enduropnaðra miða og hlutfall lagfæringa sem fylgdu afturfaraprófi eru rakin fyrir hvert teymi og rýnd á takti. Endurskapan og rótarorsakalok eru meðhöndluð sem hlið en ekki góður ásetningur, og þróun gegn grunnlínunni knýr hvar þú fjárfestir í verkfærum, þjálfun og sýnileika.
- **Stig 5, Samhæfing:** Villuleit er kennd færni samþætt gæðum (kafli 2.11) og atvikastjórnun (kafli 9.3), og öll lykkjan aðlagast stöðugt. Sýnileiki er hannaður inn svo flestir framleiðslugallar séu greinanlegir án villuleitarforrits, hver leystur galli styrkir afturfaraprófasafnið og rótarorsakaniðurstöður næra fyrri greiningu svo flokkum galla sé komið í veg fyrir frekar en endurgreindum. Skipulagsheildin endurjafnar viðleitni eftir því sem kerfi hennar og bilunarhættir þróast og endurtekna gallahlutfallið heldur áfram að falla.

## Hugmyndir til umræðu

1. Hve stór hluti nýlegra galla var endurskapaður áreiðanlega áður en nokkur breytti kóða og hvað segir það hlutfall um aðferðina þína?
2. Þegar afturför birtist, grípur teymið þitt til helmingaleitar, eða les það kóða í höndunum þar til einhver kemur auga á hana?
3. Hve greinanlegt er framleiðslukerfið þitt í dag og hvað myndirðu gefa fyrir að hafa fangað um bilun sem þegar hefur gerst?
4. Fylgja lagfæringar þínar stöðugt mistakast-svo-stenst prófi og ef ekki, hvar brotnar sá agi?
5. Hvernig meðhöndlarðu óáreiðanleg próf: villuleitarðu óákvörðunarhæfið, eða breiðirðu yfir það með endurtekningum?
6. Er villuleit kennd nýjum verkfræðingum af ásetningi, eða eru þeir látnir drekka í sig þjóðtrú af sjálfu sér?

## Helstu atriði

- Villuleit er tilgátuprófun: endurskapaðu áreiðanlega, lestu villuna og kallstaflann, einangraðu síðan með tvíundarleit og helmingaleit frekar en að skanna.
- Minnkaðu bilunina í lágmarks endurskapanlegt dæmi, með delta-villuleit fyrir stór inntök, því hver þáttur sem fjarlægður er er orsök útilokuð.
- Láttu verkfærið passa gallann: mælingu og rakningu fyrir framleiðslu og dreifð kerfi (kafli 9.2), gagnvirk villuleitarforrit fyrir staðbundna rannsókn.
- Skrifaðu mistakast-próf sem fangar gallann áður en þú lagar hann, svo lagfæringin sé sönnuð og gallinn varinn gegn til frambúðar (kafli 2.4).
- Finndu og fjarlægðu rótarorsökina, haltu eftirrýni án sakbendingar (kafli 9.3) og líttu á villuleit sem lærða færni, ekki þjóðtrú.
- Breyttu einu í einu. Haglabyssubreytingar og einkennaplástrar eyðileggja sönnunargögn og bjóða gallanum aftur heim.

## Heimildir og frekari lestur

- David J. Agans, *Debugging: The 9 Indispensable Rules for Finding Even the Most Elusive Software and Hardware Problems*
- Andreas Zeller, *Why Programs Fail: A Guide to Systematic Debugging*
- Andreas Zeller and Ralf Hildebrandt, "Simplifying and Isolating Failure-Inducing Input" (the delta debugging algorithm)
- Brian W. Kernighan and Rob Pike, *The Practice of Programming* (chapter on debugging)
- Andrew Hunt and David Thomas, *The Pragmatic Programmer* (the chapters on debugging and assertions)
- Steve McConnell, *Code Complete: A Practical Handbook of Software Construction* (the debugging chapter)
- John Regehr, "Reducers Are Fuzzers" and related writing on test-case reduction
- Charity Majors, Liz Fong-Jones, and George Miranda, *Observability Engineering* (debugging production with high-cardinality telemetry and tracing)
- Betsy Beyer, Chris Jones, Jennifer Petoff, and Niall Richard Murphy, eds., *Site Reliability Engineering* (blameless postmortems and production debugging)
