# 10.15 Áætlanagerð og spár

## Yfirlit og tilgangur

Sérhvert hugbúnaðarteymi fær sömu spurninguna: hvenær verður þetta búið? Á bak við þá spurningu situr [áætlun á hugbúnaðarfyrirhöfn](https://en.wikipedia.org/wiki/Software_development_effort_estimation), sú venja að spá fyrir um hve mikla vinnu eitthvað mun taka áður en þú hefur unnið hana. Það er eitt af því erfiðasta sem við gerum og eitt af því auðveldasta að gera illa. Vandinn er að hugbúnaður er uppgötvunarvinna. Þú ert að smíða eitthvað sem hefur aldrei verið til og mikið af því sem þú munt læra um vandamálið verður aðeins sýnilegt á meðan þú smíðar. Að spá fyrir um fyrirhöfn náms er sannarlega annað en að spá fyrir um fyrirhöfn þess að endurtaka þekkt verk.

Hvers vegna meðhöndla þetta sem sérstakan aga frekar en horn í verkefnastjórnun (kafli 10.6)? Því mistökin eru svo samkvæm og dýr. Teymi skuldbinda sig reglulega til stakra dagsetninga sem þau hafa engin sönnunargögn fyrir og verja þær síðan langt fram yfir það sem veruleikinn hefur mótmælt þeim. Leiðtogar rugla áætlun saman við loforð. Samningar festa tölu framleidda á síðdegi og halda fólki við hana í ár. Útkoman er seinkuð afhending, rýrnað traust og menning þar sem enginn segir það sem hann raunverulega trúir. Að gera þetta rétt snýst minna um betri stærðfræði og meira um heiðarleika: að aðgreina það sem þú veist frá því sem þú vonar og miðla óvissu sem óvissu.

Húfin hækka skarpt í fyrirtækja- og opinberu umhverfi. Fyrirtæki fjármagna söfn samtengdra verkefna gegn árlegum fjárhagsáætlunum og búast við föstum tölum til að úthluta fjármagni (kafli 10.1). Ríkisstjórnir gefa opinber loforð undir fjárveitingareglum, skrifa undir föstverðssamninga og svara löggjöfum þegar dagsetning rennur. Í báðum heimum er þrýstingurinn til að framleiða örugga staka tölu gríðarlegur og djúpa óvissan sem gerir þá tölu óáreiðanlega hverfur ekki þótt einhver mikilvægur vilji vissu. Þessi kafli færir rök fyrir annarri afstöðu: áætlaðu þegar það hjálpar þér að ákveða, spáðu með sönnunargögnum frekar en bjartsýni og segðu sannleikann um bilið.

## Meginreglur

- **Áætlun er spá, ekki loforð.** Haltu henni aðgreindri frá markmiðum og skuldbindingum.
- **Óvissa er raunveruleg, svo settu hana fram.** Bil með líkindum slær falska staka dagsetningu.
- **Fortíðin spáir betur fyrir um framtíðina en bjartsýni gerir.** Kjóstu mælda sögu fram yfir ferskar ágiskanir.
- **Sundurliðaðu til að skilja, spáðu til að skuldbinda.** Litlar sneiðar draga úr bæði áhættu og þörfinni á að áætla.
- **Taktu ytri sýnina.** Berðu saman við svipaðar fyrri tilraunir áður en þú treystir innri sögu þinni.
- **Endurspáðu samfellt.** Spá gerð einu sinni og aldrei uppfærð er skraut.
- **Áætlaðu aðeins þegar svarið mun breyta ákvörðun.** Annars er það sóun.

## Ráðleggingar

### Aðgreindu áætlunina, markmiðið og skuldbindinguna

Gagnlegasta hreyfingin í þessum kafla öllum kostar ekkert: haltu þremur hugmyndum aðgreindum. **Áætlun** er heiðarleg spá þín um hve lengi eitthvað mun taka, með óvissuna festa við. **Markmið** er viðskiptamarkmið sem þú vilt ná, svo sem opnun á sýningu eða regluverksfrestur. **Skuldbinding** er loforð sem þú gefur einhverjum öðrum og ætlar að halda. Þetta eru þrír ólíkir hlutir og að rugla þeim saman er hvernig verkefni byrja að ljúga að sjálfum sér. Þegar leiðtogi heyrir „um þrír til fimm mánuðir“ og skrifar niður „þrír mánuðir“ og söluteymið lofar viðskiptavini „tólf vikum“ hefur áætlun orðið að skuldbindingu hljóðlega án þess að nokkur ákvæði að taka áhættuna.

Segðu hvaða þú ert að gefa, í hvert sinn. Ef spurt er um dagsetningu skaltu svara með áætlun settri fram sem bil og láta síðan reksturinn setja markmið gegn henni og ákveða, yfirvegað, hverju á að skuldbinda sig til. Skuldbinding ætti að vera val tekið með opin augu, vegið óvissu áætlunarinnar gegn kostnaði við að missa af. Þessi agi tengist beint því hvernig skipulagsheild þín tekur og skráir ákvarðanir (kafli 1.5): skuldbinding er ákvörðun og verðskuldar strangleika ákvörðunar frekar en kinkandi samþykki á göngum.

### Skildu hvers vegna áætlanir eru rangar, og í hvaða átt

Hugbúnaðaráætlanir eru ekki tilviljanakennt rangar. Þær eru rangar á fyrirsjáanlegan, kerfisbundinn hátt og að þekkja mynstrið leyfir þér að leiðrétta fyrir því. Snemma í hverri tilraun situr þú inni í [óvissukeilunni](https://en.wikipedia.org/wiki/Cone_of_Uncertainty): í upphafi getur áætlun þín auðveldlega verið röng um stuðulinn fjóra í hvora átt og bilið þrengist aðeins eftir því sem þú smíðar og lærir. Að skuldbinda sig til nákvæmrar tölu við breiða munna keilunnar er að skuldbinda sig til tölu sem þú getur ekki enn stutt.

Ofan á þá byggingarlegu óvissu situr mannleg hlutdrægni. [Áætlunarvillan](https://en.wikipedia.org/wiki/Planning_fallacy) er áreiðanlega tilhneiging okkar til að vanmeta tíma, kostnað og áhættu eigin áætlana á meðan við ímyndum okkur besta tilfellið. Við sjáum hamingjuslóðina fyrir okkur, gleymum truflunum og samþættingaróvæntum og veikindadögum og framleiðum tölu sem gerir ráð fyrir að ekkert fari úrskeiðis. Álag er venjuleg varnarviðbrögð, en álag bætt við eftir tilfinningu er bara önnur ágiskun hlaðin ofan á þá fyrri og það er samið burt um leið og tímaáætlanir þrengjast. Lækningin er ekki meiri viljastyrkur. Hún er aðferð. Byggðu spár á því sem svipuð vinna tók í raun, ekki á því hvernig þessi vinna finnst að innan.

### Notaðu sundurliðun og sérfræðimat og þekktu takmörk þeirra

Vinnuhestatæknin er þess virði að þekkja og afmarka. **Sundurliðun** brýtur stóra afurð í minni hluta sem þú getur rökrætt um og rúllar þeim síðan upp. Hún hjálpar því fólk áætlar litla, kunnuglega hluti langtum betur en stóra, óljósa og því að leggja saman mörg óháð atriði leyfir sumum ofmötum að jafna sum vanmöt. Takmörk hennar eru að sundurliðun missir af vinnunni milli kassanna: samþættingu, samhæfingu og verkunum sem þú hugsaðir ekki um að telja upp. **Sérfræðimat** og áætlun með **samlíkingu** („þetta er eins og skýrslueininguna sem við smíðuðum í fyrra, sem tók tvo mánuði“) eru hröð og oft furðu góð, en þau erfa bjartsýni og blindu bletti áætlunargerðarmannsins.

Fyrir allt sem þú verður að setja tölu á skaltu kjósa [þriggja punkta áætlun](https://en.wikipedia.org/wiki/Three-point_estimation), sem biður um bjartsýna, líklegustu og svartsýna tölu og sameinar þær, oft sem PERT-vegið meðaltal (bjartsýn plús fjórum sinnum líklegust plús svartsýn, deilt með sex). Verðmætið er ekki nákvæma formúlan. Það er að þriggja punkta áætlun neyðir þig til að segja óvissu þína upphátt og framleiðir bil í stað falsks punkts. Afstæðar stærðaraðferðir eins og **sögupunktar** og **stuttermabolastærðir** (lítil, miðlungs, stór, extra stór) sneiða hjá gildrunni að spá fyrir um nákvæmar klukkustundir með því að bera atriði saman við hvert annað. Þær virka vel til röðunar og grófrar afkastagetu, en líttu á þær sem inntök í spá, ekki sem gjaldmiðil. Punktar eru ekki klukkustundir og að margfalda hraða með punktum til að framleiða dagsetningu innleiðir aftur öll vandamálin sem afstæð stærðarsetning átti að forðast.

### Spáðu líkindafræðilega út frá eigin flæðigögnum

Hér er breytingin sem breytir öllu: hættu að biðja fólk að giska á hve lengi vinna tekur og byrjaðu að mæla hve hratt teymi þitt klárar vinnu í raun. Afhendingarleiðsla þín (kafli 11.2) framleiðir nú þegar gögnin sem þú þarft. Ef þú rekur [afköst](https://en.wikipedia.org/wiki/Throughput), fjölda atriða sem teymi þitt lýkur á viku, getur þú spáð fyrir um framtíðina út frá fortíðinni í stað vonar. Teymi sem hefur lokað sex til ellefu atriðum á viku síðustu þrjá mánuði mun með miklum líkum taka um fjórar til sjö vikur að klára fjörutíu atriði sem eftir eru. Sú spá hvílir á sönnunargögnum og uppfærir sig sjálf í hverri viku þegar ný gögn berast.

Strangari útgáfan keyrir [Monte Carlo](https://en.wikipedia.org/wiki/Monte_Carlo_method) hermun: taktu úrtak úr sögulegum vikulegum afköstum þínum þúsundir sinnum til að byggja dreifingu mögulegra lokadagsetninga og lestu síðan svarið sem líkindi. „Við erum 85% líkleg til að klára fyrir 14. mars og 50% líkleg fyrir 28. febrúar“ er langtum gagnlegri og heiðarlegri fullyrðing en „þetta verður búið 1. mars.“ Þessi nálgun tengist beint biðraðakenningu (kafli 11.3): leiðtími jafngildir vinnu í gangi deilt með afköstum, svo sömu flæðismælikvarðar sem stýra hvernig vinna hreyfist stýra líka hvenær hún berst. Líkindaspá þarf sögu og nokkuð stöðugt ferli, sem er nákvæmlega ástæðan fyrir að hún umbunar teymum sem halda vinnu lítilli og flæði stöðugu. Hún fjarlægir líka hljóðlega mestan hluta áætlunarseremóníunnar, því þú þarft ekki lengur að stærðarsetja hvert atriði til að vita hvenær lotan lendir.

### Taktu ytri sýnina fyrir stór áætlunarverkefni

Fyrir stór, löng, dýr áætlunarverkefni geta einstakar áætlanir og jafnvel flæðisspár villt, því nýtt áætlunarverkefni hefur enga afkastasögu enn og innri saga þess er nákvæmlega þar sem áætlunarvillan bítur harðast. Mótefnið er [viðmiðunarflokksspá](https://en.wikipedia.org/wiki/Reference_class_forecasting): finndu viðmiðunarflokk svipaðra kláraðra tilrauna, skoðaðu hve lengi og hve mikið þær tóku í raun og staðsettu áætlunarverkefni þitt í þeirri dreifingu áður en þú treystir eigin neðan-frá áætlun. Ef sambærileg vettvangsskipti hjá fyrirtæki þínu hafa farið fram úr upphaflegum áætlunum um 60% að meðaltali er sú tala betri sönnunargögn um þitt en snyrtilega áætlunin sem teymi þitt var að setja saman. Ytri sýnin finnst letjandi og það er nákvæmlega gildi hennar: hún vinnur gegn bjartsýninni sem hver ný áætlun ber. Notaðu hana fyrir eignasafnsfjármögnun og fjárhagsáætlun risaáætlana (kafli 10.1), þar sem kostnaður kerfisbundinnar framúrkeyrslu er mældur í milljónum og trúverðugleika.

### Áætlaðu minna með því að skera smærra og raðaðu eftir kostnaði seinkunar

Stundum er rétt magn áætlanagerðar nánast ekkert. **#NoEstimates** röksemdin, í sanngjarna kjarna sínum, tekur eftir því að ef þú sneiðir vinnu í bita nógu litla til að hver taki dag eða tvo hættir áætlun nokkurs stakrar sneiðar að skipta máli. Þú telur einfaldlega afköst og spáir út frá talningunni. Þegar sneiðar eru einsleitar og litlar er flókin stærðarsetning sóun: hún eyðir fyrirhöfn í að framleiða nákvæmni sem spáin þarf ekki. Þetta er ekki röksemd gegn því að hugsa fram í tímann. Það er röksemd fyrir að gera einstakar spár ódýrar með því að gera einstaka bita smáa.

Það sem enn þarf ákvörðun er röð. Þegar þú getur ekki gert allt í einu skaltu raða eftir **kostnaði seinkunar**: verðmætinu sem þú tapar fyrir hverja tímaeiningu sem tiltekin vinna er seinn. Eiginleiki sem opnar stóran samning næsta ársfjórðung hefur háan kostnað seinkunar og ætti að stökkva fram fyrir fínheit með engan, jafnvel þótt fínheitið sé auðveldara. Að vega kostnað seinkunar gegn fyrirhöfn („vegið stystu-vinnu-fyrst“ þumalputtareglan úr straumlínustjórnun) segir þér hvað á að gera næst langtum áreiðanlegar en verkefnalisti raðaður eftir magatilfinningu. Taktu eftir að þetta endurrammar allt samtalið: í stað „hvenær verður allt búið,“ sem býður upp á falska nákvæmni, spyrð þú „hvað er verðmætasta sem hægt er að klára næst,“ sem þú getur í raun svarað.

## Málamiðlanir: kostir og gallar

| Nálgun | Kostir | Gallar |
|---|---|---|
| **Stök dagsetningaráætlun** | Einföld. Það sem hagsmunaaðilar biðja um | Nákvæmlega röng. Felur áhættu. Verður óvart skuldbinding |
| **Þriggja punkta / PERT áætlun** | Neyðir óvissu í dagsljósið. Ódýr | Enn ágiskun. Formúlan gefur í skyn falskan strangleika |
| **Sögupunktar / stuttermabolastærðir** | Hröð. Góð til röðunar og grófrar afkastagetu | Ekki klukkustundir. Hraðareikningur smyglar stökum dagsetningum aftur inn |
| **Líkindaflæðisspá** | Sönnunargagnabyggð. Sjálfuppfærandi. Heiðarleg bil | Þarf sögu og stöðugt flæði. Lítur síður „örugg“ út |
| **Viðmiðunarflokksspá** | Leiðréttir bjartsýni á stórum áætlunarverkefnum | Þarf sambærilegar fyrri tilraunir. Letjandi að heyra |
| **#NoEstimates (litlar sneiðar)** | Fjarlægir sóun. Spá með talningu | Krefst agaðrar sneiðingar. Truflandi fyrir fjármögnunaraðila sem vilja tölu |

Meginspennan er **vissan sem fólk vill á móti heiðarleikanum sem vinnan krefst**. Fjármögnunaraðilar, stjórnendur, samningar og löggjafar biðja um fasta staka dagsetningu því stök dagsetning er auðveld að fjárhagsáætla, lofa og verja. Hugbúnaður styður hana sjaldan. Leystu spennuna ekki með því að framleiða vissu og ekki með því að neita að svara, heldur með því að svara í gjaldmiðli líkinda: bil með vissustigum, endurspáð þegar sönnunargögn berast. Paraðu það við litlar sneiðar svo snemmbúnar, raunverulegar afhendingar komi í stað fjarlægra, ímyndaðra sem það sem fólk treystir. Sýndur áfangi er meira virði en nokkur áætlun.

## Spurningar til að ræða með teyminu

1. **Þegar einhver biður þig um dagsetningu, ertu að gefa áætlun, markmið eða skuldbindingu og veit allir í herberginu hvaða?** Þetta er spurningin sem kemur í veg fyrir mestan skaða fyrir minnstu fyrirhöfn. Í flestum skipulagsheildum hrynja þessi þrjú í eina tölu um leið og hún fer úr munni teymisins og enginn ákvað að taka áhættuna á að spá yrði að loforði. Komdu með raunverulegt dæmi: taktu síðasta skuldbundna frest þinn og raktu hann afturábak til samtalsins þar sem hann var fyrst mælt og spyrðu hvort hann var nokkru sinni annað en vongóð ágiskun í jakkafötum. Svarið ætti að breyta tungumáli þínu varanlega, svo áætlanir fari út sem bil, markmið séu nefnd viðskiptaóskir og skuldbindingar séu gerðar yfirvegað með óvissuna vegna og skráða sem ákvörðun (kafli 1.5). Ef teymi þitt getur ekki bent á hvar skuldbinding var meðvitað samþykkt ertu að gefa loforð fyrir slysni.

2. **Gætir þú spáð fyrir um næstu útgáfu þína út frá mældum afköstum í stað ferskra áætlana og hvað stöðvar þig?** Flest teymi hafa þegar gögnin til að svara „hvenær verður þetta búið“ reynslubundið, ónotuð í verkfærinu sem rekur vinnu þeirra. Ef þú veist hve mörgum atriðum teymi þitt hefur lokið á viku síðasta ársfjórðung getur þú hermt dreifingu lokadagsetninga og gefið líkindi frekar en ósk. Komdu með raunverulega afkastasögu þína og fjölda atriða sem eftir eru og berðu flæðibyggðu spána saman við hvaða dagsetningu sem teymið áætlaði eftir tilfinningu. Bilið er yfirleitt lærdómsríkt. Ef hindrunin er að atriði ykkar eru gjörólík að stærð eða flæði ykkar er óreglulegt er það sjálft niðurstaðan, því óstöðugt flæði er afhendingarvandamál sem vert er að laga óháð (kaflar 11.2, 11.3). Að færa sig frá áætlanagerð til mælingar er oft minna verkfærabreyting en ákvörðun um að treysta eigin sögu fram yfir bjartsýni.

3. **Fyrir stærsta núverandi áætlunarverkefni þitt, hefur þú tekið ytri sýnina, eða aðeins smíðað innri áætlun?** Stór áætlunarverkefni eru þar sem bjartsýni samsetur sig í dýra framúrkeyrslu og þar sem örugg neðan-frá áætlun er mest tælandi og minnst áreiðanleg. Agaginn er að nefna viðmiðunarflokk svipaðra kláraðra tilrauna innan eða utan skipulagsheildar þinnar, finna hvað þær kostuðu í raun og hve lengi þær tóku og staðsetja áætlunarverkefni þitt heiðarlega í þeirri dreifingu áður en þú ver eigin tölur. Komdu með gögnin: hvernig hafa sambærileg verkefni hér farið fram úr fyrstu áætlunum og gerir núverandi áætlun þín hljóðlega ráð fyrir að þú slærð hverja þeirra? Ef hún gerir það ertu að veðja á að vera einstök(n), veðmál sem grunnhlutföllin tapa áreiðanlega. Ytri sýnin mun gera spá þína minna smjaðrandi og langtum verjanlegri fyrir fjármögnunaraðilum og úttektaraðilum sem munu muna töluna sem þú gafst (kafli 10.1).

4. **Þegar fjármögnunaraðili, samningur eða löggjafi krefst einnar fastrar dagsetningar, hvernig svarar þú án þess að ljúga eða neita?** Hér er þrýstingurinn harðastur og hér lúta heiðarleg teymi oftast, því „70% líkur fyrir september“ hljómar undanskotsfullt við hlið öruggs „september“ keppinautar. Fyrir stóra skipulagsheild margfaldast húfin: ein föst dagsetning berst inn í fjárhagsáætlanir, háð áætlunarverkefni og opinber loforð, svo tala valin til þæginda verður kerfisbundin skuld um leið og hún rennur. Komdu með tungumálið sem þú ætlar í raun að nota, unnið dæmi um bil með vissustigum og lítinn snemmbúinn áfanga sem þú getur skuldbundið þig fast til á meðan seinna umfang er skilið eftir sem fjármagnað bil. Samkeppnissjónarmiðið er raunverulegt, því sumir frestir (regluverksskipti, sýningaropnun) eru sannarlega fastir og rétta hreyfingin þar er að festa dagsetninguna og sveigja umfang frekar en að þykjast að fyrirhöfnin sé örugg. Í fyrirtækja- og opinberu umhverfi skaltu tengja þetta við lögun samningsins: einingaskiptur, áfangafjármagnaður samningur leyfir þér að skuldbinda þig heiðarlega til verðmæts kjarna, á meðan einn föstu verði, föstu umfangi samningur festur við fjarlægan áfanga þvingar fram nákvæmlega fölsku vissuna sem framleiðir framúrkeyrsluna og fyrirsögnina.

5. **Hvernig ákveður teymi þitt hvað á að smíða næst og myndi röðun eftir kostnaði seinkunar skýrt breyta röðinni?** Flestir verkefnalistar eru raðaðir eftir blöndu af magatilfinningu, hver hrópaði hæst og grófri fyrirhöfn, sem hljóðlega fínstillir fyrir auðvelda sigra frekar en verðmæta. Kostnaður seinkunar, verðmætið sem þú tapar fyrir hverja tímaeiningu sem vinna er seinn, endurrammar spurninguna úr „hvenær verður allt búið“ í „hvað er verðmætasta sem hægt er að klára næst,“ sem þú getur í raun svarað með sönnunargögnum. Komdu með þrjú eða fjögur raunveruleg verkefnalistaatriði með heiðarlegu mati á verðmætinu sem hvert opnar og hvenær það verðmæti rennur út, raðaðu þeim síðan eftir verðmæti-tapað-á-viku gegn fyrirhöfn og berðu þá röð saman við núverandi áætlun. Endurröðunin er yfirleitt óvænt og erfitt að mótmæla. Samkeppnissjónarmiðið er að kostnaður seinkunar er sjálfur áætlun og getur verið leikinn af hverjum sem vill sitt atriði fyrst, svo nefndu hver á tölurnar og hvernig þær eru véfengdar. Fyrir fyrirtækjasafn eða opinbert áætlunarverkefni er þessi agi það sem leyfir þér að verja röðunarákvarðanir fyrir hagsmunaaðilum sem hver trúir að þeirra verkefni ætti að vera fyrst, því röðunin hvílir á yfirlýstu verðmæti frekar en pólitík.

6. **Hver endurspáir, hve oft og hver ber ábyrgð á að bregðast við þegar spáin hreyfist?** Spá gerð einu sinni við upphaf og aldrei endurskoðuð er skraut og dýrustu seinkanirnar eru þær sem lifandi spá hefði sýnt mánuðum áður en frestur gerði þær óumdeilanlegar. Fyrir stórt teymi er bilunin sjaldan fjarvera gagna og yfirleitt fjarvera fasts takts og nefnds eiganda: afköst reka, lokadagsetningardreifingin færist til hægri og enginn sem hefur það hlutverk að taka eftir er að horfa. Komdu með raunverulegan endurspátakt þinn (eða viðurkenndu að enginn er til), síðasta skipti sem spá breytti ákvörðun og rekið sem þú hefur séð síðan núverandi skuldbinding var sett. Samkeppnissjónarmiðið er spáþreyta, því að endurspá of hávaðasamt býður upp á ruðning og rýrir traust, svo komdu þér saman um skynsamlegt bil og þröskuld sem ræsir stigmögnun frekar en að bregðast við hverri sveiflu. Í fyrirtækja- og opinberu samhengi skaltu tengja þetta við eftirlit: upplýstu stjórnarháttaaðila með uppfærðu líkindabili á föstum tíma, svo seinkun birtist sem stýrð endurspá sem leiðtogar geta brugðist við frekar en óvænt sem afhjúpast á áfanganum.

## Sjónarhorn eftir geirum

**Sprotafyrirtæki.** Slepptu áætlunarseremóníunni nánast alveg. Sneiddu vinnu í eins-til-tveggja-daga bita, teldu hvað þú klárar á viku og gefðu stofnendum og fjárfestum þrengjandi bil í stað hetjulegrar stakrar dagsetningar. Saga þín er stutt og ferlið sveiflukennt, svo notaðu óvissukeiluna sem heiðarlega skýringu frekar en afsökun og endurspáðu hvern föstudag þegar myndin skýrist.

**Lítið fyrirtæki.** Þú hefur engan áætlunarsérfræðing og enga lyst á stærðarsetningarfundum, svo láttu verkfærin sem þú rekur nú þegar vinna verkið: flest verkefnakerfi afhjúpa afköst ókeypis og létt spá út frá því slær ágiskaðan frest. Stattu gegn freistingunni að kaupa þungan áætlunarhugbúnað sem þú getur ekki mannað. Einföld vikuleg talning kláraðra atriða og skýrt bil svarar „hvenær verður þetta búið“ nógu vel fyrir skuldbindingarnar sem þú gefur í raun viðskiptavinum.

**Stórfyrirtæki.** Vandinn er samræmi yfir mörg teymi sem fjármagna safn gegn árlegum fjármagnshring (kafli 10.1). Staðlaðu á bil með vissustigum frekar en stakar dagsetningar, krefstu viðmiðunarflokkssamanburðar fyrir stór áætlunarverkefni og komdu upp flæðismælikvörðum svo ágiskanir víki fyrir afkastabyggðum spám innan ársfjórðungs. Stýrðu áætlanagerð sem sameiginlegri venju með skýrum skilgreiningum á áætlun, markmiði og skuldbindingu, svo tala framleidd í einni deild merki það sama þegar hún nær stjórninni.

**Hið opinbera.** Innkaupareglur og opinber ábyrgð móta allt. Misst opinber dagsetning verður fyrirsögn og úttektarniðurstaða, svo kjóstu einingaskipta, áfangafjármagnaða samninga fram yfir eina skuldbindingu föstu verði, föstu umfangi festa við fjarlægan áfanga. Upplýstu eftirlitsaðila með líkindaspám og viðmiðunarflokkssönnunargögnum á einföldu máli, birtu vissustig heiðarlega og láttu sýnda virka áfanga verða sönnunargögnin sem almenningur og úttektaraðilar treysta frekar en undirskrift verktaka á bjartsýna áætlun.

## Dæmi

**Sprotafyrirtæki.** Níu manna sprotafyrirtæki sem undirbýr Series A kynningu þarf að vita hvort lykilsamþætting verði tilbúin. Frekar en að láta stofnendurna lofa fjárfestum dagsetningu gefur forystumaðurinn áætlun sem bil og útskýrir óvissukeiluna á bak við hana. Teymið hefur lokað fimm til níu verkefnalistaatriðum á viku, svo það keyrir fljóta Monte Carlo spá á vinnunni sem eftir er og skýrir frá „80% líkur fyrir þriðju viku ársfjórðungs, jöfn líkindi viku fyrr.“ Þau sneiða samþættinguna í tveggja daga bita svo engin stök áætlun skipti miklu máli, raða eftir kostnaði seinkunar til að smíða fjárfestasýnilegu slóðina fyrst og endurspá hvern föstudag. Fjárfestar fá heiðarlega, þrengjandi spá í stað öruggrar tölu sem hefði runnið.

**Stórfyrirtæki.** Smásali sem skiptir út pöntunarstjórnunarvettvangi sínum verður að fjármagna áætlunarverkefnið gegnum árlegan fjármagnshring sem krefst tölu. Áætlunarskrifstofan stenst freistinguna að verja snyrtilegu neðan-frá áætlunina og byggir í staðinn viðmiðunarflokk úr þremur sambærilegum vettvangsskiptum, tveimur innri og einu opinberlega skjalfestu, sem fóru fram úr upphaflegum áætlunum um 50% til 80%. Þau fjármagna gegn ytri sýnartölunni, setja tímaáætlunina fram sem líkindabil frekar en fasta opnun og koma upp flæðismælikvörðum frá fyrsta afhendingarteyminu svo innan ársfjórðungs komi afkastabyggð spá sem uppfærist mánaðarlega í stað ágiskunar. Þegar einn straumur fer heitur sýnir endurspáin það snemma og forystan endurjafnar frekar en að uppgötva seinkunina á frestinum.

**Hið opinbera.** Stofnun sem nútímavæðir bótakerfi starfar undir fjárveitingum og opinberri rýni, þar sem misst opinber dagsetning er fyrirsögn. Í stað eins föstu verði, föstu umfangi samnings bundnum við einn fjarlægan áfanga kaupir hún einingaskipta áfanga og skuldbindur sig opinberlega til verðmæts kjarna afhents snemma, með seinna umfang sett fram sem fjármagnað bil frekar en loforð. Áætlunarleiðtogar upplýsa eftirlitsaðila með líkindaspám og viðmiðunarflokkssamanburði, útskýra vissustig á einföldu máli, svo „70% fyrir september“ sé skilið sem nákvæmlega það. Sýndir virkir áfangar verða sönnunargögnin sem almenningur treystir, sem er sterkara en nokkur áætlun sem verktaki gæti skrifað undir.

## Viðskiptarök: hvatar, ávöxtun fjárfestingar og heildarkostnaður

Ávöxtun heiðarlegrar áætlanagerðar og spáa ræðst af forðuðu stórslysi. Stór hugbúnaðarátök fara fram úr eða mistakast langtum oftar en þau ná upphaflegri fastri áætlun og tapið samsetur sig: sokkinn kostnaður, glatað verðmæti vegna seinkaðrar afhendingar, neyðarútgjöld til að jafna sig og rýrnun trausts sem fylgir broti á opinberri skuldbindingu. Venjurnar hér (að aðgreina áætlun frá skuldbindingu, spá út frá raunverulegum afköstum, taka ytri sýnina á stórum áætlunarverkefnum) eru þær sem færa áætlunarverkefni af bilunarferlinum. Þú ert ekki að kaupa nákvæmari kristalskúlu. Þú ert að kaupa fyrri, sannari upplýsingar um hvar þú stendur, sem leyfir þér að leiðrétta á meðan leiðrétting er enn ódýr.

Hvað heildareignarkostnað varðar lækkar breytingin frá áætlunarseremóníu í mælda spá yfirleitt kostnað frekar en að hækka hann. Flókin áætlanagerð fyrirfram er dýr í framleiðslu og úreldist um leið og vinna hefst, á meðan afkastabyggð spá er nánast ókeypis þegar afhendingarleiðsla þín gefur frá sér gögnin. Báðar öfgar kosta peninga: ofáætlun (endalausir stærðarsetningarfundir sem framleiða nákvæmni sem enginn notar) og vanspá (að skuldbinda sig blint og borga fyrir framúrkeyrsluna síðar). Til að færa rök við forystu skaltu leggja fullhlaðinn kostnað síðustu stóru framúrkeyrslu þinnar við hlið nánast engu kostnaðar við að rekja afköst og gefa bil og sýna hvernig ytri sýnarspá hefði sett fjármögnunarhæfa væntingu frá upphafi.

## Andmynstur og gildrur

- **Stakar dagsetningarskuldbindingar:** bil hrunið í eina tölu, síðan varin yfir sönnunargögnin.
- **Áætlunarþvottur:** vongóð ágiskun send upp keðjuna þar til hún harðnar í samningsbundið loforð.
- **Hraði sem tímaáætlunarvél:** að margfalda sögupunkta með hraða til að framleiða nákvæma dagsetningu.
- **Álag eftir tilfinningu:** önnur ágiskun hlaðin ofan á þá fyrstu, samið burt undir þrýstingi.
- **Aðeins innri sýn:** að treysta ferskri neðan-frá áætlun á meðan hunsað er hvað svipuð áætlunarverkefni tóku í raun.
- **Að áætla allt:** stærðarsetning lítilla, einsleitra sneiða þar sem einstakar áætlanir breyta engri ákvörðun.
- **Frystar spár:** spá gerð einu sinni við upphaf og aldrei uppfærð þegar veruleikinn berst.
- **Nákvæmnisleikhús:** að gefa upp klukkustundir með tveimur aukastöfum við breiðan munna óvissukeilunnar.

## Þroskalíkan

- **Stig 1, Upphaf:** Áætlanir eru stakar dagsetningar framleiddar með magatilfinningu og meðhöndlaðar sem loforð. Enginn greinarmunur á áætlun, markmiði og skuldbindingu. Spár eru viðbragðsdrifnar og ad hoc. Framúrkeyrsla kemur öllum á óvart og er kennt um teyminu.
- **Stig 2, Þróun:** Einhver skipulögð áætlanagerð er til (sundurliðun, sögupunktar, þriggja punkta tölur), en venjan er ólík eftir teymum. Áætlanir eru enn mestmegnis stakar tölur. Hraði er notaður til að varpa dagsetningum. Spár eru gerðar einu sinni við upphaf og sjaldan endurskoðaðar.
- **Stig 3, Stöðlun:** Skjalfestur staðall er framfylgt um skipulagsheildina: áætlanir eru settar fram sem bil með yfirlýstri óvissu, áætlun, markmið og skuldbinding eru aðgreind með skilgreiningu, teymi rekja afköst og endurspá á föstum takti og stór áætlunarverkefni skulu nota viðmiðunarflokkssamanburð.
- **Stig 4, Stjórnun:** Venjan er mæld og stýrð með gögnum. Spánákvæmni er rakin gegn raunútkomu og kvörðun athuguð, svo þú getur sagt hvort „80% fyrir“ dagsetningar þínar lendi í raun átta sinnum af tíu. Afkasta- og hringrásartímagrunnlínur eru viðhaldnar. Kostnaður seinkunar er magngreindur. Spárek er vaktað gegn þröskuldum og ræsir stigmögnun. Skuldbindingar eru gerðar gegn sönnunargögnum frekar en bjartsýni.
- **Stig 5, Samhæfing:** Líkindaspá út frá flæðigögnum er samfelld og treyst því kvörðunarsaga hefur sannað hana heiðarlega. Skuldbindingar eru yfirvegaðar ákvarðanir sem vega vissu gegn kostnaði. Vinna er sneidd nógu smátt til að áætlanagerð er í lágmarki og kostnaður seinkunar knýr röð. Áætlanagerð er samþætt við eignasafnsfjármögnun og áhættuáætlanagerð og skipulagsheildin endurskilgreinir umfang og endurjafnar reglulega þegar spár hreyfast, aðlagar áætlunina að sönnunargögnum frekar en að verja upphaflegu töluna.

## Hugmyndir til umræðu

1. Hvað myndi breytast í skipulagsheild ykkar ef hver áætlun þyrfti að fara úr teyminu sem bil með vissustigi og stakar dagsetningar væru bannaðar?
2. Hvar eruð þið að eyða fyrirhöfn í að áætla vinnu sem er þegar nógu lítil og einsleit til að spá með talningu?
3. Ef þið mötuðuð síðustu tvo ársfjórðunga af afköstum inn í Monte Carlo hermun, myndi spáin vera sammála dagsetningunum sem þið skuldbunduð ykkur í raun til?
4. Fyrir stærsta áætlunarverkefni ykkar, hver er heiðarlegi viðmiðunarflokkurinn og hve illa mótmælir grunnhlutfallið núverandi áætlun ykkar?
5. Hvernig ákveður teymi ykkar röð í dag og myndi röðun skýrt eftir kostnaði seinkunar breyta því sem þið smíðið næst?
6. Þegar skuldbinding er samþykkt í skipulagsheild ykkar, er óvissan skráð sem hluti ákvörðunarinnar, eða hverfur hún um leið og dagsetningin er skrifuð niður?

## Helstu atriði

- Haltu **áætluninni, markmiðinu og skuldbindingunni** aðgreindum. Að rugla þeim saman er hvernig verkefni byrja að ljúga að sjálfum sér.
- Áætlanir eru kerfisbundið rangar í þekktum áttum: **óvissukeilan** víkkar snemmbúna vinnu og **áætlunarvillan** gerir bjartsýni að sjálfgildi.
- Kjóstu **líkindaspá út frá mældum afköstum** fram yfir ferskar ágiskanir. Gefðu bil og vissustig og endurspáðu samfellt.
- Taktu **ytri sýnina** með viðmiðunarflokksspá á stórum áætlunarverkefnum, þar sem bjartsýni er dýrust (kafli 10.1).
- **Sneiddu smátt** svo einstakar áætlanir hætti að skipta máli og **raðaðu eftir kostnaði seinkunar** frekar en magatilfinningu.
- Áætlaðu aðeins þegar það breytir ákvörðun. Annars er það sóun. Sjá kafla 10.6 (verkefnastjórnun), 11.2 (afhending), 11.3 (biðraðakenning) og 1.5 (ákvarðanataka og stjórnarhættir).

## Heimildir og frekari lestur

- Steve McConnell, *Software Estimation: Demystifying the Black Art*.
- Daniel Vacanti, *Actionable Agile Metrics for Predictability* and *When Will It Be Done?* (probabilistic forecasting from flow data).
- Troy Magennis, *Forecasting and Simulating Software Development Projects* (Monte Carlo methods).
- Bent Flyvbjerg and Dan Gardner, *How Big Things Get Done* (reference class forecasting and megaprojects).
- Daniel Kahneman, *Thinking, Fast and Slow* (the planning fallacy and the outside view).
- Donald Reinertsen, *The Principles of Product Development Flow* (cost of delay and queue economics).
- Vasco Duarte, *NoEstimates: How to Measure Project Progress Without Estimating*.
- Frederick Brooks, *The Mythical Man-Month* (why software schedules go wrong).
- Todd Little, "Schedule Estimation and Uncertainty Surrounding the Cone of Uncertainty" (*IEEE Software*, 2006).
