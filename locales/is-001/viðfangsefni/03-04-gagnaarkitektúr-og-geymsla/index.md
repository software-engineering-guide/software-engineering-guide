# 3.4 Gagnaarkitektúr og geymsla

## Yfirlit og tilgangur

Gögn lifa lengur en kóði. Forrit eru endurskrifuð á nokkurra ára fresti, en gögnin sem þau stýra (viðskiptavinaskrár, fjárhagshöfuðbækur, bótasaga, heilsufarsskrár) endast í áratugi. Þau eru oft verðmætasta og mest eftirlitsskylda eign skipulagsheildarinnar. Gagnaarkitektúr er sú grein að ákveða hvernig gögn eru líkönuð, hvar þau eru geymd, hvernig þau haldast samræmd, hvernig þau þróast og hvernig þau eru afgreidd nógu hratt í stórum stíl. Fyrir stóra skipulagsheild eru þessar ákvarðanir grundvallaratriði. Val þitt á geymsluvélum og gagnalíkönum takmarkar hvað reksturinn getur gert, hve hratt hann getur hreyfst og hve mikið það kostar, allan líftíma kerfisins.

Hagsmunirnir eru mestir í fyrirtækjum og hjá hinu opinbera vegna stærðar, langlífis og regluverks. Færslugeymsla banka má aldrei týna eða tvítelja eina krónu. Opinber skrá verður að varðveita færslur lögbundin tímabil og sanna heilleika þeirra fyrir endurskoðendum. Heilbrigðiskerfi verður að framfylgja fínkornaðri aðgangsstýringu og búsetureglum. Á sama tíma þjóna þessar skipulagsheildir gríðarlegu les- og skrifmagni og hafa ekki efni á því að hver fyrirspurn lendi á einum [venslagagnagrunni](https://en.wikipedia.org/wiki/Relational_database). Gagnaarkitektúr verður því að sætta réttleika og endingu við afköst og stigvöxt, og gera það á meðan skemað breytist sífellt til að mæta nýjum kröfum.

Þessi kafli fjallar um helstu geymslulíkönin og hvenær á að nota hvert, aga [fjölmálavarðveislu](https://en.wikipedia.org/wiki/Polyglot_persistence), gagnalíkönun og hið oft vanmetna vandamál þróunar og flutnings skema, [skyndiminni](https://en.wikipedia.org/wiki/Cache_(computing)) og [CDN](https://en.wikipedia.org/wiki/Content_delivery_network) (efnisdreifinet) með hinu alræmda erfiða vandamáli ógildingar, og hvernig færslur, læsingar og samtími hegða sér þegar þú ýtir þeim í stóran stíl. Rauði þráðurinn er einfaldur: það er enginn algildur gagnagrunnur. Það eru málamiðlanir, og góður gagnaarkitektúr þýðir að velja þær meðvitað, eitt vinnuálag í einu.

## Meginreglur

- **Mótaðu gögnin eftir aðgangsmynstrunum, ekki öfugt.** Hannaðu geymslu út frá því hvernig gögn verða lesin og skrifuð, ekki út frá óhlutbundnu „réttu“ líkani.
- **Enginn einn gagnagrunnur ræður öllum.** Ólíkt vinnuálag vill ólíkar vélar. Fjölmálavarðveisla er eðlileg í stórum stíl.
- **Réttleiki fyrst fyrir aðalgagnageymsla.** Fyrir valdbær gögn eru ending og samræmi óumsemjanleg. Fínstilltu afköst í kringum þau, ekki í gegnum þau.
- **Skemað mun breytast, svo skipuleggðu það.** Flutningar eru fyrsta flokks, samfelld verkfræðivinna, ekki einskiptis.
- **Eigðu gögnin þín á bak við þjónustumörk.** Hvert afmarkað samhengi (sjálfstætt lénslíkan með eigin skýr mörk) á sín gögn. Að deila gagnagrunni tengir teymi og eyðileggur sjálfræði.
- **Skyndiminni er réttleikavandi í dulargervi afkastaávinnings.** Sérhvert skyndiminni kynnir úreldingu og ógildingaráhættu. Meðhöndlaðu það af ásetningi.
- **Afnormun er málamiðlun, ekki synd.** Að tvítaka gögn fyrir lesafköst er lögmætt ef þú berð samræmisafleiðingarnar.
- **Samræmi og stigvöxtur skipta hvort öðru.** Því sterkari sem færsluábyrgðin er, því erfiðara er að dreifa henni. Kauptu aðeins það sem vinnuálagið þarfnast.

## Ráðleggingar

### Veldu geymslulíkan út frá vinnuálagi

Láttu hvert vinnuálag samsvara líkaninu sem hentar því. **Venslagagnagrunnar** gefa sterkt samræmi, samtengingar og þroskaðar færslur. Þeir eru sjálfgefni kosturinn fyrir aðalgagnageymsla og allt með flóknum heilleikareglum. **[Skjalageymslur](https://en.wikipedia.org/wiki/Document-oriented_database)** henta stigveldisgögnum með sveigjanlegu skema sem eru lesin sem heild (heil pöntun, heilt snið). **[Lykil-gildis](https://en.wikipedia.org/wiki/Key-value_database)** geymslur gefa gríðarlegan hraða fyrir einfaldar uppflettingar (setur, eiginleikarofar, skyndiminni). **[Netgagnagrunnar](https://en.wikipedia.org/wiki/Graph_database)** skara fram úr þar sem tengsl eru fyrirspurnin (svikahringir, skipurit, réttindi, aðfangakeðjur). **[Dálkageymslur](https://en.wikipedia.org/wiki/Column-oriented_DBMS)** knýja greiningarfyrirspurnir sem skanna fáa dálka yfir milljarða raða (gagnavöruhús, skýrslugerð). **[Tímaraðagagnagrunnar](https://en.wikipedia.org/wiki/Time_series_database)** fínstilla fyrir viðbótarþung, tímastimpluð gögn (mælikvarða, fjarmælingar, skynjara [Internets hlutanna](https://en.wikipedia.org/wiki/Internet_of_things) (IoT), markaðsgögn). Stattu gegn freistingunni að þvinga eina vél til að vinna öll verk. Að nota venslagagnagrunn sem biðröð, eða skjalageymslu sem höfuðbók, býður sársauka heim.

### Taktu upp fjölmálavarðveislu af ásetningi

Stór kerfi nota lögmætt nokkrar geymslur: venslaaðalgagnageymsla, leitarvísitölu, skyndiminni, greiningargagnavöruhús og kannski netgagnagrunn eða tímaraðavél. Þetta er **fjölmálavarðveisla**, og hún er rétta mynstrið þegar vinnuálag er raunverulega ólíkt. Kostnaðurinn er rekstrarlegur, því þú hefur nú fleiri vélar til að reka, tryggja, afrita og manna. Stýrðu þeim kostnaði með því að líta á hverja geymslu sem í eigu þjónustu, staðla rekstrarverkfæri og halda fjölda tækni við þær sem vinna sér inn sæti sitt. Vertu varkár við að taka upp nýjan gagnagrunn fyrir hverja minniháttar þörf. Hver og einn er varanleg rekstrarskuldbinding.

### Mótaðu gögn og líttu á þróun skema sem samfellda

Fjárfestu í gagnalíkönun fyrirfram fyrir aðalgagnageymsla. Normaðu til að vernda heilleika, afnormaðu síðan sértækt fyrir sannaða lestrarhitapunkta. Hvað sem líkaninu líður **þróast skemað að eilífu**, svo gerðu flutninga örugga og rútínu. Notaðu útgáfustýrð, sjálfvirk, einstefnuflutningsskriftur sem eru innrituð í frumkóðastýringu og beitt gegnum afhendingarleiðsluna. Fyrir breytingar án niðurtíma á stórum töflum skaltu nota **þenja-og-þjappa (samsíða breytingar)** mynstrið: bættu við nýja dálknum eða töflunni, fylltu aftur og tvískrifaðu, fluttu lesendur og fjarlægðu síðan gamla formið. Aldrei ein brjótandi breyting. Gerðu skemabreytingar afturábaksamhæfðar yfir útgáfur svo gamall og nýr kóði keyri samtímis. Í atburðauppsprettu- eða skilaboðakerfum skaltu útgáfumerkja atburða- og skilaboðaskema skýrt og styðja uppvörpun gamalla atburða (að umbreyta þeim í núverandi skema við lestur).

### Hannaðu skyndiminni og ógildingu með opin augu

Skyndiminni og CDN eru áhrifamestu afkastaverkfærin. CDN afgreiðir kyrrstætt og skyndiminnishæft efni frá jaðrinum nálægt notendum og forritaskyndiminni hlífa gagnagrunninum við endurteknum lestri. En erfiði hlutinn er ógilding: að vita hvenær skyndiminnisgögn eru úrelt. Veldu aðferð fyrir hvert tilvik. Notaðu tímabundið fyrningartímabil (TTL) þar sem lítil úrelding er ásættanleg og einfaldast. Notaðu skýra ógildingu eða gegnumskrif þar sem ferskleiki skiptir máli. Notaðu cache-aside þar sem forritið stýrir fyllingu. Stilltu TTL meðvitað, varðu gegn **skyndiminnisstormum** (margir biðlarar endurbyggja sömu útrunnu færslu í einu) með læsingu eða beiðnasamruna og komdu í veg fyrir **hjarðhlaup** á köldu skyndiminni. Skyndiminnisgeymdu aldrei gögn þar sem úrelding gæti valdið réttleika- eða regluvörslubresti (réttindi, stöður, samþykki) án skýrrar, prófaðrar ógildingarleiðar. Líttu á skyndiminnislykla, TTL og ógildingu sem hönnuð verk, ekki tilfallandi stillingu.

### Stýrðu færslum, læsingum og samtíma fyrir stigvöxt

Skildu einangrunarstig og veldu það veikasta sem er enn rétt fyrir hverja færslu, því hærri einangrun kostar samtíma. Kjóstu **[bjartsýnan samtíma](https://en.wikipedia.org/wiki/Optimistic_concurrency_control)** (útgáfuathuganir við skrif) fyrir lágan árekstur og lestrarþung vinnuálög, og náðu í **svartsýnar læsingar** aðeins undir raunverulegum heitum árekstri, með læsingum stuttum og í samræmdri röð til að forðast baktjaldslás. Þegar þú stigvaxar verður einn skrifanlegur gagnagrunnur flöskuháls. Kynntu lesafrit fyrir lesstigvöxt (með því að sætta þig við afritunartöf) og **[sneiddu](https://en.wikipedia.org/wiki/Shard_(database_architecture))/skiptu** eftir lykli sem dreifir álagi jafnt og heldur tengdum gögnum saman til að forðast færslur milli sneiða. Mundu að sneiðing skiptir burt auðveldum samtengingum milli sneiða og fjölsneiða [ACID](https://en.wikipedia.org/wiki/ACID)-færslum (Atomicity, Consistency, Isolation, Durability), sem er oft ástæðan fyrir því að sögur og afnormun birtast. Ýttu þessum aðferðum inn aðeins eftir því sem vinnuálagið krefst. Ótímabær sneiðing bætir við varanlegri flækju.

## Málamiðlanir: kostir og gallar

| Geymslugerð | Best fyrir | Styrkleikar | Veikleikar |
|---|---|---|---|
| Venslagagnagrunnur | Aðalgagnageymsla, flókinn heilleiki | ACID, samtengingar, þroskuð verkfæri | Erfiðara að stigvaxa skrif lárétt |
| Skjalageymsla | Samsafnslestur, sveigjanlegt skema | Hraður lestur/skrif heils hlutar, sveigjanlegt | Veikar samtengingar/færslur milli skjala |
| Lykil-gildi | Setur, skyndiminni, einfaldar uppflettingar | Gríðarlegur hraði og stigvöxtur | Engin fyrirspurn umfram lykilinn |
| Netgagnagrunnur | Tengslaþungar fyrirspurnir | Hröð yfirferð, svipmikil | Sérhæfð rekstrarkunnátta, stigvaxtartakmörk |
| Dálkageymsla | Greining, skýrslugerð | Hraðar samantektarskannanir, þjöppun | Léleg fyrir línuleg færsluskrif |
| Tímaraðir | Mælikvarðar, fjarmælingar, IoT | Skilvirk viðbót og tímafyrirspurnir | Þröngur tilgangur |

Ráðandi málamiðlunin er samræmi og rík fyrirspurn gegn láréttum stigvexti og hraða. Venslakerfi gefa sterkustu ábyrgðirnar og sveigjanlegustu fyrirspurnirnar, en þau eru erfiðust að stigvaxa skrif yfir margar vélar. [NoSQL](https://en.wikipedia.org/wiki/NoSQL)-fjölskyldur (ekki-venslaðar) slaka á samtengingum, færslum eða skema til að fá stigvöxt og hraða. Skyndiminni skiptir ferskleika fyrir töf. Sneiðing skiptir færslum milli skiptinga fyrir skrifafköst. Ekkert af þessu er algilt rétt. Listin er að setja hvert vinnuálag á þann punkt ferilsins sem réttleika- og afkastaþarfir þess krefjast í raun.

## Spurningar til að ræða með teyminu

1. **Getur hver og einn nefnt eitt aðalgagnageymsla fyrir hvert mikilvægt gagnasafn, eða eru skyndiminni og varpanir hljóðlega meðhöndluð sem sannleikur?** Gögn lifa lengur en kóði, og skaðlegustu gagnaatvikin koma af reki: skyndiminni, leitarvísitala eða lesvarpan er talin valdbær og vikur hljóðlega frá raunverulegu uppsprettunni. Í stóru teymi gerist þetta þegar eignarhald er óskýrt og nokkrar þjónustur skrifa skarast afrit, svo enginn getur sagt hvaða gildi er rétt í atviki. Komdu með kort af mikilvægum gögnum þínum og, fyrir hvern hlut, einu geymsluna sem er valdbær auk afleiddu afritanna sem verða að vera endurbyggjanleg úr henni. Í fjármálum og hjá hinu opinbera er að geta sannað hvaða skrá er lagalega uppsprettan og endurbyggt restina oft regluverkskrafa, ekki þægindi. Allt sem þú getur ekki endurbyggt úr aðalgagnageymslanu er sjálft aðalgagnageymsla, hvort sem þú ætlaðir það eða ekki.

2. **Hvað kostar hver gagnagrunnsvél í búinu ykkar í raun að reka, tryggja og afrita og vinnur hver og ein sér enn sæti sitt?** Fjölmálavarðveisla er rétt þegar vinnuálag er raunverulega ólíkt, en hver vél er varanleg rekstrarskuldbinding: plástrun, afritun, vöktun, öryggisrýni og starfsfólk sem þekkir hana klukkan 3 að nóttu. Stór skipulagsheild getur rekið inn í dýragarð geymslna sem hver var tekin upp fyrir einn eiginleika, og jaðargeymslan bætir við kostnaði að eilífu á meðan hún þjónar vinnuálagi sem geymsla sem þú rekur þegar gæti ráðið við. Listaðu hverja vél, vinnuálagið sem réttlætir hana og hver er á bakvakt fyrir hana, merktu síðan allar sem voru teknar upp fyrir þörf sem aðalgeymsla gæti nú mætt. Upptaka nýs gagnagrunns ætti að standast háa kröfu, því að fjarlægja einn síðar þýðir enn einn flutning. Að staðla rekstrarverkfæri yfir geymslurnar sem þú heldur er hvernig þú heldur kostnaði niðri án þess að þvinga eina vél til að vinna öll verk.

3. **Hvar getur notandi lesið úrelt gildi af afriti rétt eftir eigin skrif og brýtur það loforð sem þú gafst honum?** Lesafrit stigvaxa lestur en dragast aftur úr aðalgeymslunni, svo notandi sem uppfærir snið og endurhleður strax getur séð gamla gildið, sem les sem galli eða, fyrir stöðu eða samþykkisfána, regluvörslubrest. Ákveddu fyrir hvert flæði hvort lestu-þín-eigin-skrif skipti máli og leiddu þá lestra til aðalgeymslunnar eða notaðu setusamræmisbúnað. Komdu með lista yfir flæði sem afgreidd eru af afritum og merktu hver notandi bregst við strax eftir að hafa skrifað. Fyrir stöður, réttindi og samþykki skaltu líta á úrelta lestra sem réttleikabresti, ekki útlitslega. Málið er að kaupa samræmið sem hvert vinnuálag þarfnast í raun og gera úreldinguna sem þú sættir þig við skýra frekar en tilviljanakennda.

4. **Getur þú breytt skema stærstu, annasömustu töflunnar þinnar í dag án niðurtíma og hver hefur í raun æft þenja-og-þjappa skrefin?** Skemað þróast að eilífu og bilunin sem sárast er stórhvella breyting sem læsir risatöflu, frystir þjónustuna og er ekki hægt að afturkalla hreint. Í stóru teymi margfaldast áhættan því nokkrar þjónustur lesa sama formið, svo brjótandi breyting þarfnast gamals og nýs kóða sem keyrir hlið við hlið yfir áfangaskipta uppsetningu. Togið á móti er hraði: ein breyting er fljótleg að skrifa, á meðan þenja-og-þjappa (bæta við nýja forminu, fylla aftur, tvískrifa, flytja lesendur, fella gamla formið) er fleiri skref og meiri þolinmæði. Komdu með stærstu töfluna þína, heiðarlegt mat á því hve lengi barnaleg breyting myndi læsa henni og tiltekinn flutning sem einhver hefur keyrt frá enda til enda í æfingu en ekki í kenningu. Í fyrirtækja- og opinberum kerfum sem keyra samfellt og bera lögbundin aðgengismarkmið er niðurtími vegna flutnings brot, svo þenja-og-þjappa agi er verðið fyrir að mega yfirleitt breyta skemanu.

5. **Hver skyndiminnis- eða afrituð gildi, ef þau eru afgreidd úrelt, myndu valda regluvörslu- eða öryggisbresti frekar en útlitslegum og eru allar þessar ógildingarleiðir prófaðar?** Skyndiminni er réttleikavandi í afkastabúningi: hættan er ekki hægagangur heldur að afgreiða réttindi, stöðu, samþykkisfána eða aðgangsákvörðun eftir að hún breyttist. Fyrir stóra skipulagsheild er hættan dreifð, því skyndiminni og jaðarlög safnast upp yfir teymi og enginn einn getur talið upp hvað er geymt hvar eða hvenær það hreinsast. Spennan er raunveruleg: ágengt skyndiminni og langur TTL kaupa töf og vernda gagnagrunninn, á meðan strangur ferskleiki kostar hvort tveggja. Komdu með skrá yfir skyndiminnis- og CDN-afgreidd gögn, merkta fyrir hvaða færslur bera regluvörslu- eða öryggisafleiðingu, auk sönnunargagna um að ógildingarleið hverrar þeirra hafi verið æfð í reynd en ekki aðeins stillt. Í eftirlitsskyldu og opinberu umhverfi er úrelt samþykkis- eða hæfisgildi úttektarhæf bilun, svo þessi atriði þarfnast skýrrar, prófaðrar ógildingarleiðar eða ættu alls ekki að vera skyndiminnisgeymd.

6. **Hver er varðveislu-, skjalavistunar- og gagnabúsetustefna ykkar fyrir hverja valdbæra geymslu og getið þið sannað hana fyrir endurskoðanda?** Gögn lifa lengur en kóði og oft lengur en teymið sem skrifaði hann, svo ótakmarkaður vöxtur og óljósar búsetureglur verða hljóðlega vandi sem enginn á þar til tafla er óviðráðanleg eða skrá situr í röngu lögsagnarumdæmi. Stór skipulagsheild spannar margar geymslur og svæði, og sjónarmiðin sem togast á eru kostnaður (heit geymsla er dýr, svo skjalavistaðu og stigskiptu), afköst (uppþembdar töflur hægja á öllu) og lagaleg skylda (lögbundin varðveislulágmörk og búsetuþök sem geta rekist á). Komdu með, fyrir hvert valdbært gagnasafn, varðveislutímabilið, hvar gögnin búa líkamlega, skjalavistunar- og eyðingarbúnaðinn og nafn þess sem ber ábyrgð. Fyrir fyrirtæki og sérstaklega opinber kerfi eru varðveisla og búseta yfirleitt lagaskyldur með úttektar- og fullveldiskröfum, svo að geta sannað hvar hver skrá býr, hve lengi hún er geymd og hvenær henni er eytt er rekstrarleyfi, ekki sparisiðum.

## Sjónarhorn eftir geirum

**Sprotafyrirtæki.** Haltu þig við einn gagnagrunn og stattu gegn dýragarðinum. Ein stýrð venslageymsla gefur þér færslur, eitt til að afrita og einn stað til að rökræða um samræmi, sem er nákvæmlega það sem þriggja manna teymi getur haldið í höfðinu. Bættu við skyndiminni, lesafriti eða leitarvísitölu aðeins þegar tiltekin hæg fyrirspurn eða raunverulegt lesmagn knýr á, svo flækjan komi með borgandi ástæðu. Haltu flutningum útgáfustýrðum frá degi eitt, því að bæta flutningsaga við lifandi vöru eftir á er mun erfiðara en að byrja með hann.

**Lítið fyrirtæki.** Þú hefur engan gagnagrunnssérfræðing og engan tíma til að reka nokkrar vélar, svo kjóstu stýrða geymslu og láttu vettvangsveituna sjá um afritun, plástrun og afritun gagna. Líttu á geymsluval sem kaupákvörðun: veldu leiðinlegu, vel studdu vélina sem verkfærin þín samþættast þegar frekar en þá hröðustu á frammistöðuprófi. Settu einfalda varðveislu- og afritunarstefnu sem þú getur í raun staðfest og skyndiminnisgeymdu aldrei neitt sem tengist peningum eða heimildum án skýrrar leiðar til að hreinsa það, því úrelt verð eða réttindi kostar þig viðskiptavin.

**Stórfyrirtæki.** Kjarnaáskorunin er fjölmálavarðveisla yfir mörg teymi: venslaaðalgagnageymsla auk leitar, skyndiminnis, vöruhúss og kannski net- eða tímaraðavéla, hver í eigu þjónustu frekar en samnýtt. Staðlaðu rekstrarverkfæri, afritun og vöktun yfir geymslurnar sem þú heldur, haltu upptöku nýrra véla við háa kröfu og gerðu þenja-og-þjappa flutninga og skýra skyndiminnisógildingu að sjálfgefnu. Stýrðu búinu sem eignasafni með skýru gagnaeignarhaldi, svo engin vél lifi lengur en vinnuálagið sem réttlætti hana og ekkert teymi sé tengt gegnum sameiginlegan gagnagrunn.

**Hið opinbera.** Gagnabúseta, lögbundin varðveisla og sannanlegur heilleiki móta hvert val. Útvegaðu hverja geymslu á fullvalda svæðum, stilltu CDN til að skyndiminnisgeyma aðeins ópersónugögn og haltu óbreytanlegri úttektarsögu fyrir skrár sem verða að vera endurbyggjanlegar fyrir eftirlitsaðila. Flutningar sem ný löggjöf krefst þarf að beita afturábaksamhæft gegnum leiðsluna svo þjónustan haldist aðgengileg gegnum lagafresti og aðalgagnageymslað verður að vera auðkennanlegt svo þú getir sannað hvaða gildi er lagaleg uppspretta og endurbyggt hvert afleitt afrit úr því.

## Dæmi

**Sprotafyrirtæki.** Sprotafyrirtæki á frumstigi rekur allt á einu stýrðu PostgreSQL-tilviki og stendur gegn löngunni til að bæta við sérstakri leitarvél, skyndiminni og vöruhúsi áður en það þarf þau. Einn gagnagrunnur þýðir eitt til að afrita, einn stað til að rökræða um samræmi og færslur sem bara virka, sem skiptir máli þegar allt teymið er þrír verkfræðingar. Þau bæta við Redis-skyndiminni og lesafriti aðeins þegar tiltekin hæg fyrirspurn og raunverulegt lesmagn réttlætir það, svo flækjan kemur með borgandi ástæðu frekar en á undan henni.

**Stórfyrirtæki.** Smásölubanki geymir valdbæru höfuðbókina sína í sterkt samræmdum venslagagnagrunni: hver bókun er rétt ACID-færsla, sneidd eftir reikningasviði fyrir skrifstigvöxt. Umhverfis hana situr fjölmála bú: leitarvísitala fyrir viðskiptavinauppflettingu, Redis-skyndiminni (gegnumskrif, stutt TTL) fyrir reikningsyfirlit í farsímaforritinu, dálkavöruhús fyrir regluverks- og greiningarskýrslur og netgagnagrunnur fyrir svikagreiningu á færslunetum. Skemabreytingar á höfuðbókinni nota þenja-og-þjappa með tvískrifum svo sólarhringskerfið taki aldrei niðurtíma vegna flutnings.

**Hið opinbera.** Landsbundin ökutækjaskrá geymir valdbærar skrár í venslaaðalgagnageymsla með lögbundinni varðveislu og fullri úttektarsögu. Opinberar „athuga ökutæki“ uppflettingar eru afgreiddar af lesafriti og jaðarskyndiminni með stuttum TTL, því örlítið úrelt opinber gögn eru ásættanleg og lesmagnið dverga skrif. Gagnabúsetulög krefjast þess að allar skrár haldist innanlands, svo hver geymsla er útveguð á fullvalda svæðum og CDN er stillt til að skyndiminnisgeyma aðeins ópersónugögn. Flutningar til að bæta við nýjum reitum sem samgöngustefna krefst eru framkvæmdir afturábaksamhæft gegnum leiðsluna svo þjónustan haldist aðgengileg gegnum lagafresti.

## Viðskiptarök: hvatar, ávöxtun fjárfestingar og heildarkostnaður

Gagnaarkitektúrákvarðanir hafa meðal lengstu og stærstu kostnaðarhala í hugbúnaði, því gögn og skema þeirra eru erfiðustu hlutirnir að breyta þegar kerfi og samþættingar reiða sig á þau. Upptökukostnaður góðra vinnubragða (yfirveguð geymsluval, agaðir flutningar, hannað skyndiminni og viðeigandi sneiðing) er aðallega tími eldri verkfræðinga og nokkur viðbótar rekstrarverkfæri. Kostnaðurinn við að taka það *ekki* upp birtist sem einn ofhlaðinn gagnagrunnur sem kæfir allan reksturinn, neyðarendurvettvangsvæðing þegar röng geymsla uppgötvast of seint, langvarandi rekstrarrof vegna misheppnaðs flutnings og, skaðlegast, gagnaspilling eða regluvörslubrot vegna rangt ógilds skyndiminnis eða týndrar færslu.

Færðu rökin til forystu í orðum stigvaxtarrýmis, atvikaáhættu og regluverksáhættu. Réttu geymsluvalin eru það sem leyfir rekstrinum að auka les- og skrifmagn án endurskriftar. Agaðir flutningar eru það sem leyfir skemanu að halda í við nýjar kröfur án niðurtíma. Rétt skyndiminni er það sem skilar hraðri notendaupplifun án hljóðra úreldingargalla. Magnsettu heildareignarkostnað yfir líftíma kerfisins. Ein vel valin gagnaarkitektúr forðast endurtekinn kostnað við að vinna í kringum lélega, og eitt forðað gagnaspillingaratvik dvergar venjulega allan kostnað við að gera þetta vel. Í eftirlitsskyldum geirum er hæfnin til að sanna gagnaheilleika og búsetu ekki kostnaðarstaður heldur rekstrarleyfi.

## Andmynstur og gildrur

- **Sameiginlegur gagnagrunnur yfir þjónustur.** Margar þjónustur lesa og skrifa eitt skema, sem tengir teymi og gerir hverja breytingu að samhæfingarkreppu.
- **Einn gagnagrunnur fyrir allt.** Að þvinga greiningu, biðraðir, leit og færslur á eina venslavél þar til hún hrynur.
- **Stórhvellsflutningar.** Stakar brjótandi skemabreytingar sem krefjast niðurtíma og ekki er hægt að afturkalla örugglega.
- **Skyndiminni án ógildingaraðferðar.** Úrelt gögn afgreidd endalaust, eða réttleikagallar því enginn á hvenær skyndiminnið hreinsast.
- **Ótímabær sneiðing.** Að dreifa gögnum áður en álag krefst þess, og tapa samtengingum og færslum varanlega fyrir engan ávinning.
- **Hunsun afritunartafar.** Að lesa eigin skrif af afriti sem er á eftir og fá úrelt gögn, sem brýtur væntingar notenda.
- **Ótakmarkaður gagnavöxtur.** Engin skjalavistunar- eða varðveislustefna, svo töflur vaxa þar til afköst og kostnaður verða óþolandi.
- **Afleidd gögn geymd sem sannleikur.** Að líta á skyndiminni, vísitölu eða vörpun sem aðalgagnageymslað og uppgötva síðan að hún rak.

## Þroskalíkan

- **Stig 1: Upphaf.** Einn gagnagrunnur er notaður í öllum tilgangi. Skemabreytingar eru handvirkar og ad hoc, án flutningsaga. Skyndiminni er tilfallandi og ógilding eftirþanki. Afkastavandi er leystur viðbragðsdrifið með því að kaupa stærri vél og enginn getur áreiðanlega nefnt aðalgagnageymslað fyrir tiltekið gagnasafn.
- **Stig 2: Þróun.** Sum geymsluval eru yfirveguð og skyndiminni eða vöruhús hefur birst, en vinnubrögð eru mismunandi eftir teymum. Flutningar eru útgáfustýrðir en krefjast stundum niðurtíma og þenja-og-þjappa er notað af þeim sem tilviljun vill að kunni það. Nokkrar þjónustur deila enn gagnagrunni og skyndiminnisaðferðir eru ólíkar frá einu teymi til næsta.
- **Stig 3: Stöðlun.** Fjölmálavarðveisla er pöruð við vinnuálag, hver geymsla í eigu þjónustu og aldrei samnýtt. Sjálfvirkir, afturábaksamhæfðir þenja-og-þjappa flutningar án niðurtíma eru skjalfesti og framfylgdi staðallinn um alla skipulagsheildina. Skyndiminnisaðferðir, TTL og ógildingarleiðir eru skýr hönnunargögn og eina aðalgagnageymslað fyrir hvert gagnasafn er skjalfest, með afleiddum afritum endurbyggjanlegum úr því.
- **Stig 4: Stjórnun.** Gagnabúið er mælt og stýrt gegn grunnlínum. Þú rekur lengd flutninga og afturköllunarhlutfall, afritunartöf gegn lestu-þín-eigin-skrif kröfum, skyndiminnishitahlutfall og úreldingaratvik, rekstrarkostnað á hverja geymslu og fyrirspurnartöf við markhundraðshluta, og bregst við tölunum. Varðveisla og búseta eru úttekin gegn lögbundnum kröfum, réttleiki afleiddra gagna er staðfestur samfellt og hver vél verður að réttlæta kostnað sinn gegn vinnuálaginu sem hún þjónar.
- **Stig 5: Samhæfing.** Gagnaarkitektúr er stöðugt bættur og samþættur getu-, kostnaðar- og áhættuáætlun um alla skipulagsheildina. Sneiðing, skyndiminni og samræmisval eru endurjöfnuð fyrir hvert vinnuálag eftir því sem aðgangsmynstur og kostnaður breytast og geymslur sem vinna sér ekki lengur sæti sitt eru lagðar niður gegnum skipulagða flutninga. Skemaþróun, skjalavistun og búseta eru fullsjálfvirk og aðlögunarhæf, svo búið mótar sig að nýjum kröfum og álagi án neyðarendurvettvangsvæðingar.

## Hugmyndir til umræðu

1. Hverjar af núverandi geymslum þínum vinna verk sem þær voru ekki hannaðar fyrir og hver væri rétta vélin?
2. Getur þú framkvæmt skemabreytingu á stærstu töflunni þinni í dag án niðurtíma? Ef ekki, hvers vegna ekki?
3. Hvar skyndiminnisgeymir kerfið þitt gögn þar sem úrelding gæti valdið regluvörslu- eða réttleikabresti?
4. Hvaða þjónustur deila gagnagrunni og hvað þyrfti til að gefa hverri sinn eigin?
5. Hvar er einn skrifanlegur gagnagrunnur stigvaxtarþak þitt og er lesafritun eða sneiðing rétta næsta skrefið?
6. Hver er varðveislu- og skjalavistunarstefna þín og hver ber ábyrgð á henni?

## Helstu atriði

- Gögn lifa lengur en kóði. Geymslu- og líkönunarákvarðanir takmarka reksturinn allan líftíma kerfisins.
- Láttu hvert vinnuálag samsvara geymslulíkaninu sem hentar aðgangsmynstri þess og búist við fjölmálavarðveislu í stórum stíl.
- Gefðu hverri þjónustu eignarhald á gögnum sínum og tengdu aldrei teymi gegnum sameiginlegan gagnagrunn.
- Líttu á skemaþróun sem samfellda og notaðu afturábaksamhæfða, niðurtímalausa þenja-og-þjappa flutninga.
- Skyndiminni er réttleikavandi. Hannaðu TTL, ógildingu og stormvörn af ásetningi og skyndiminnisgeymdu aldrei regluvörslukritísk gögn án prófaðrar ógildingarleiðar.
- Kauptu aðeins samræmið og færsluábyrgðirnar sem hvert vinnuálag þarfnast. Sneiðing og afritun skipta færslum milli skiptinga fyrir stigvöxt.

## Heimildir og frekari lestur

- Martin Kleppmann, *Designing Data-Intensive Applications*
- Pramod Sadalage and Martin Fowler, *NoSQL Distilled*
- Pramod Sadalage and Scott Ambler, *Refactoring Databases: Evolutionary Database Design*
- C. J. Date, *An Introduction to Database Systems*
- Joe Celko, *SQL for Smarties*
- Vlad Mihalcea, *High-Performance Java Persistence* (transactions, isolation, concurrency)
- Eric Evans, *Domain-Driven Design* (bounded contexts and data ownership)
- Werner Vogels, "Eventually Consistent"
