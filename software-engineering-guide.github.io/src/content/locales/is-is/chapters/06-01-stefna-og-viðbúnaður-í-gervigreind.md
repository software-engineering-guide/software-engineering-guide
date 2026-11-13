# 6.1 Stefna og viðbúnaður í gervigreind

## Yfirlit og tilgangur

[Gervigreind](https://en.wikipedia.org/wiki/Artificial_intelligence) hefur þróast úr rannsóknarnýjung í kjarnagetu sem stórar skipulagsheildir eru nú ætlast til að taki í notkun á ábyrgan hátt og í stórum stíl. Fyrir fyrirtæki og opinberar stofnanir er raunverulega spurningin ekki lengur hvort gervigreind geti gert eitthvað áhrifamikið í sýnikennslu. Hún er hvort tiltekin fjárfesting leysi raunverulegt vandamál betur en valkostirnir, verði rekin örugglega árum saman og lifi af úttekt, innkaup og opinbera skoðun. Gervigreindarstefna er sú grein að ákveða hvar á að beita gervigreind, hvar á að forðast hana og hvaða undirstöður þú þarft áður en fyrsta líkanið nær framleiðslu.

Fyrir stór teymi hækka stærð og tregða húfið. Illa mótað verkefni getur brennt fjárveitingar, truflað hæfa verkfræðinga og rýrt traust eftirlitsaðila og borgara þegar það bregst opinberlega. Vel valið verkefni getur sjálfvirknivætt leiðindavinnu, dregið fram innsýn úr gögnum sem þú náðir aldrei til áður og leyst hæft fólk undan til verðmætari starfa. Munurinn er sjaldan líkanið sjálft. Hann snýst um hve vel þú mótar vandann, hve tilbúin gögn þín og mannauður eru og hve heiðarleg viðskiptarök þín eru.

Opinbert og regluverkað umhverfi bætir við fleiri skorðum. Opinberir aðilar verða að rökstyðja útgjöld, tryggja gagnsæi, forðast ólögmæta mismunun og vera ábyrgir gagnvart kjörnum fulltrúum og almenningi. Innkaupareglur geta bannað bindingu við einn seljanda, krafist skýranleika og skyldað seljendur til að sýna hegðun líkana. Hér skaltu líta á reglufylgni, úttektarhæfni og útgönguleiðir sem fyrsta flokks kröfur, ekki eftirþanka.

## Meginreglur

- Byrjaðu á vandamáli sem er þess virði að leysa, ekki tækni sem leitar að notkun.
- Kjóstu einföldustu nálgun sem mætir þörfinni. Gervigreind er einn valkostur af mörgum og oft ekki sá besti.
- Líttu á gagnaviðbúnað, mannauð og vettvangsþroska sem forsendur, ekki samhliða verkstrauma sem er hægt að greiða úr síðar.
- Taktu ákvarðanir um smíða eða kaupa skýrt og endurskoðaðu þær eftir því sem markaðurinn og geta þín breytast.
- Magnsettu heildareignarkostnað, þar með talinn rekstur, vöktun og endanlega endurnýjun, ekki bara leyfið eða tilraunaverkefnið.
- Hannaðu fyrir útgöngu frá fyrsta degi: forðastu arkitektúr sem gerir skipti á seljendum eða líkönum óheyrilega dýr.
- Í regluverkuðu og opinberu umhverfi skaltu líta á gagnsæi, innkaupasamræmi og ábyrgð sem hönnunarskorður.
- Mældu kostnaðinn við að *aðhafast ekki* til jafns við kostnaðinn við að aðhafast.

## Ráðleggingar

### Mótaðu vandann áður en þú velur tækni

Skrifaðu eins síðu vandalýsingu. Nefndu ákvörðunina eða verkið sem þú vilt bæta, núverandi grunnlínu, mælanlega útkomuna sem þú vilt og hvað gerist þegar kerfið hefur rangt fyrir sér. Spyrðu síðan hvort vandinn henti gervigreind yfirleitt. Eru nógu mikil viðeigandi gögn til? Er verkið mynsturbundið frekar en reglubundið? Þolirðu líkindasvör? Getur maður athugað úttakið? Mörg vandamál leysast betur með ákvörðunarbundnum hugbúnaði, betri ferlahönnun eða einfaldlega betri gagnahreinlæti. Skrifaðu skýrt niður hvar gervigreind á *ekki* við: til dæmis ákvarðanir sem lög krefjast að séu fullkomlega skýranlegar, eða þar sem kostnaðurinn við sjaldgæfa villu er skelfilegur og ómögulegt að grípa.

### Notaðu ákvörðunartré um smíða, kaupa, fínstilla eða gefa fyrirmæli

Færðu þig frá ódýrasta og fljótlegasta til dýrasta og best stýrða:

1. **Gefðu fyrirmæli til núverandi hýsts líkans.** Ef almennt líkan (eins og Claude frá Anthropic, eða sambærilegt frá öðrum veitendum) leysir vandann með vandlegum fyrirmælum og sókn, gerðu það fyrst. Lægsti kostnaður, hraðasta endurtekning, engir þjálfunarinnviðir.
2. **Auktu með sókn eða verkfærum.** Ef bilið er þekking eða aðgerðir skaltu bæta við [sóknaraukinni myndun](https://en.wikipedia.org/wiki/Retrieval-augmented_generation) (RAG), sem sækir viðeigandi skjöl við fyrirspurn og leggur þau til líkansins sem samhengi, og verkfærabeitingu áður en þú snertir vigtir líkansins.
3. **Fínstilltu eða aðlagaðu.** Ef fyrirmæli ná ekki nauðsynlegri nákvæmni, tóni eða sniði með samkvæmni skaltu [fínstilla](https://en.wikipedia.org/wiki/Fine-tuning_(deep_learning)) minna líkan á þínum gögnum: það er, þjálfa forþjálfað líkan frekar á dæmum þínum til að sérhæfa það. Þetta kaupir stjórn á kostnað [MLOps](https://en.wikipedia.org/wiki/MLOps) (rekstur vélnáms) leiðslu.
4. **Keyptu sérhæfða vöru.** Fyrir vel skilgreind svið (skjalavinnsla, svikaeinkunn) getur þroskuð söluaðilavara slegið allt sem þú smíðar.
5. **Smíðaðu frá grunni.** Taktu frá þjálfun [grunnlíkana](https://en.wikipedia.org/wiki/Foundation_model) (stór líkön forþjálfuð á breiðum gögnum og aðlögunarhæf að mörgum verkum) fyrir skipulagsheildir með einstök gögn, djúpan mannauð og stefnumótandi ástæður. Fyrir nær öll fyrirtæki og stofnanir er þetta rangt val.

### Komdu á gagna-, mannauðs- og vettvangsforsendum

Úttektu gögnin þín með tilliti til aðgengis, gæða, merkingar, uppruna og lagagrundvallar fyrir notkun. Staðfestu að þú hafir í raun rétt til að nota þau fyrir gervigreind, þar með talin persónugögn og gögn þriðja aðila. Metdu mannauð heiðarlega: þú þarft gagnafræðinga og líka vélnámsverkfræðinga, gagnaverkfræðinga, vörustjóra sem skilja líkindakerfi og rýna sem geta metið úttak. Áður en þú stigvaxar skaltu setja upp vettvangsgrunnlínu: tilraunarakningu, líkanaskrá (aðalgagnageymslu fyrir þjálfaðar líkanaútgáfur og samþykktarstöðu þeirra), vöktun og örugga þjónustu, svo hvert nýtt notkunartilvik þurfi ekki að finna upp reksturinn aftur.

### Meðhöndlaðu regluverkað og opinbert umhverfi af ásetningi

Fáðu innkaupa-, lögfræði- og áhættuteymi að borðinu snemma. Krefstu þess að seljendur upplýsi um uppruna líkana, vinnubrögð við þjálfunargögn, matsniðurstöður og þekktar takmarkanir. Kjóstu samninga sem veita flytjanleika gagna þinna og fyrirmæla og forðastu séreignarsnið sem fanga þig. Þar sem við á skaltu birta tilgang og öryggisráðstafanir gervigreindarkerfa sem snúa að almenningi og gefa fólki leið til að andmæla sjálfvirkum ákvörðunum. Samræmdu við viðurkennda ramma (sjá kafla 6.5) svo úttektir finni skjalfest, verjanlegt ferli.

### Reiknaðu heildareignarkostnað og varastu bindingu

Líkanaðu allan lífsferilskostnaðinn: ályktun eða leyfi, gagnaleiðslur, mannlega rýni, vöktun, endurþjálfun, atvikaviðbrögð og afvirkjun. Berðu hann saman við kostnað óbreytts ástands og valkostanna. Dragðu úr bindingu með því að setja líkanið á bak við innra viðmót, halda fyrirmælum og matsgagnasöfnum flytjanlegum og prófa annan veitanda öðru hverju.

## Málamiðlanir: kostir og gallar

| Nálgun | Kostir | Gallar | Best þegar |
|---|---|---|---|
| Fyrirmæli til hýsts líkans | Hröð, ódýr, engir innviðir, auðvelt að skipta | Minni stjórn, kostnaður á kall, gagnamiðlunarspurningar | Frumgerðir, breið verk, óviss krafa |
| Sóknaraukning | Jarðtengir svör í þínum gögnum, uppfæranleg | Sóknargæði erfið, bætir við innviðum | Þekkingarþung verk |
| Fínstilla minna líkan | Stjórn, lægri kostnaður á kall í stærð, möguleiki á eigin rekstri | Krefst MLOps, gagna og viðhalds | Stöðug, umfangsmikil, sérhæfð verk |
| Kaupa vöru | Reynd, studd, hröð til verðmætis | Leyfiskostnaður, binding, takmörkuð passun | Vel skilgreind staðlavandamál |
| Smíða grunnlíkan | Hámarksstjórn og aðgreining | Gífurlegur kostnaður, sjaldgæfur mannauður, mikil áhætta | Nánast aldrei, utan fremstu rannsóknarstofa |

Ríkjandi málamiðlunin er stjórn gegn kostnaði og hraða. Fyrirmæli gefa mestan hraða og sveigjanleika en minnsta stjórn. Smíði gefur mesta stjórn en krefst fjármuna sem fáar skipulagsheildir ættu að eyða. Flest stór teymi ættu að búa í miðjunni: gefa fyrirmæli og sækja fyrst, fínstilla af vali og kaupa fyrir staðlaðar þarfir. Binding skiptir skammtímaþægindum fyrir langtímaáhættu, og það skiptir sérstaklega máli hjá hinu opinbera, þar sem margra ára útgönguskyldur eru algengar.

## Spurningar til að ræða með teyminu

1. **Hvar situr hvert af þremur efstu væntanlegu notkunartilvikum okkar á stiganum fyrirmæli, sókn, fínstilling, kaup, smíði og hvaða sönnunargögn myndu færa það um eitt þrep?** Þetta skiptir máli því mest sóuð gervigreindarútgjöld koma af því að byrja þrepi of hátt: að þjálfa líkan þegar vandleg fyrirmæli hefðu dugað. Fyrir stórt teymi stöðvar það að samþykkja stigann sem sameiginlegt sjálfgefið að hver hópur finni upp dýra leiðslu aftur. Komdu með eins síðu vandalýsinguna fyrir hvern frambjóðanda, núverandi grunnlínu og heiðarlegt mat á því hvort bilið sé þekking (sókn), samkvæmni (fínstilling) eða leyst staðlavara (kaup). Í fyrirtækja- og opinberu umhverfi skaltu bæta við innkaupa- og úttektarkostnaði hvers þreps, því fínstillt líkan dregur með sér MLOps-byrði sem hýst kall gerir ekki. Svarið ætti að láta þig drepa eða lækka að minnsta kosti eitt of víðfeðmt verkefni í herberginu.

2. **Hver er áþreifanleg útgönguáætlun okkar fyrir seljandann eða líkanið sem við treystum mest á og höfum við í raun prófað hana?** Binding er ódýr að samþykkja og dýr að leysa, og hjá hinu opinbera gætirðu borið margra ára útgönguskyldur sem þú getur ekki mætt ef þú æfðir aldrei. Komdu með listann yfir séreignareiginleika sem þú reiðir þig á, hvort fyrirmæli og matsgagnasöfn eru flytjanleg og hvernig líkanið situr á bak við innra viðmót (eða gerir það ekki). Merkið til að fylgjast með er hvort nokkur hafi nokkru sinni keyrt matssafnið þitt gegn öðrum veitanda. Ef ekki er útgönguáætlun þín von, ekki áætlun. Ef heiðarlega svarið er að skipti tækju mánuði og krefðust endurskriftar kjarnakóða skaltu líta á það sem hönnunargalla til að laga núna, ekki brú til að fara yfir síðar.

3. **Hvað segir heiðarlegt viðbúnaðarmatsblað um gagnaréttindi okkar og hvaða notkunartilvik útilokar það í dag?** Að sleppa gagnaviðbúnaði er bilunin sem sekkur tilraunaverkefnum hljóðlega: líkanið virkar, en þú hafðir aldrei lagagrundvöllinn til að nota gögnin, eða þau eru ómerkt og án uppruna. Fyrir stóra skipulagsheild reisa persónugögn og gögn þriðja aðila samþykkis- og samningsmörk sem eru ólík eftir lögsagnarumdæmi og gagnasafni. Komdu með úttekt á aðgengi, gæðum, merkingu, uppruna og lagagrundvelli fyrir hvern frambjóðanda og vertu viljugur að merkja sum notkunartilvik lokuð þar til gagnaundirstöður eru til. Í regluverkuðu og opinberu umhverfi er ónothæfur lagagrundvöllur ekki töf heldur hörð stöðvun, og að fjármagna viðbúnaðarvinnuna ætti að vera skýr liður í áætluninni en ekki eftirþanki.

4. **Hvernig vitum við að lifandi gervigreindarnotkunartilvik virkar í raun og hvaða sönnunargögn myndu fá okkur til að drepa það?** Flest gervigreindareignasöfn safna uppvakningum: tilraunaverkefnum sem fóru í loftið, heilluðu einhvern og keyra nú endalaust án þess að nokkur athugi hvort þau vinni enn fyrir kostnaði sínum. Komdu þér saman um grunnlínuna og árangursmælikvarðann fyrir opnun, settu síðan skýran drápsþröskuld, svo ákvörðunin um að hætta sé tekin fyrirfram en ekki varin í augnablikinu. Komdu með núverandi mælikvarða, kostnað mannlegs eftirlits á útkomu og rekið sem þú hefur séð frá opnun. Fyrir fyrirtækja- og opinber eignasöfn skaltu nefna hver rýnir hvert kerfi á föstum takti og hver hefur vald til að leggja það niður. Notkunartilvik sem enginn ber ábyrgð á að rýna er eitt sem enginn mun nokkurn tímann slökkva á.

5. **Hvar er maður áfram í lykkjunni, hvað kostar það eftirlit og höfum við í raun fjárhagsáætlað það?** Ódýrustu útlítandi gervigreindarnotkunartilvikin eru þau sem hljóðlega gera ráð fyrir fullri sjálfvirkni og leka síðan kostnaði gegnum rýni, leiðréttingu og stigmögnun sem veruleikinn þvingar aftur inn. Ákveddu af ásetningi hvaða ákvarðanir maður verður að staðfesta, hverjar líkanið má taka eitt og hverjar það má aldrei taka, verðleggðu síðan mannlega tímann sem það felur í sér. Komdu með magn lágtraustsmála, kostnað rangs svars og núverandi stigmögnunarleið. Í regluverkuðu og opinberu umhverfi skaltu tengja hverja sjálfvirka ákvörðun við ábyrgan embættismann og áfrýjunarleið, því eftirlit sem þú getur ekki lýst er eftirlit sem þú hefur ekki.

6. **Höfum við mannauðinn og vettvanginn til að reka það sem við leggjum til, eða gerum við hljóðlega ráð fyrir getu sem við höfum ekki?** Metnaðarfullar gervigreindaráætlanir bregðast minna á líkaninu en á óglæsilegum undirstöðum: enginn til að viðhalda leiðslunni, enginn sem getur metið úttak, enginn vettvangur til að setja upp á. Paraðu hvert væntanlegt notkunartilvik við færnina og innviðina sem það þarf í raun og vertu heiðarlegur þar sem bilið er ráðning, samstarfsaðili eða ástæða til að smíða ekki. Komdu með skrá yfir hver getur átt hvert kerfi í framleiðslu, á hvaða vettvangi það mun keyra og hvaða getu þú þyrftir að kaupa. Fyrir stóra eða opinbera skipulagsheild skaltu bæta við innkaupa- og ráðningarfyrirvara, því áætlun sem hvílir á mannauði sem þú getur ekki ráðið innan tilskilins tíma er áætlun um að skila of litlu.

## Sjónarhorn eftir geirum

**Sprotafyrirtæki.** Hraði og lífsafkoma ráða. Veldu eitt þröngt notkunartilvik sem snertir kjarnagildi þitt, afhentu það á hýstu líkani á bak við þunnt viðmót og settu hart þak á útgjöld. Forðastu að smíða innviði eða þjálfa líkön: knappasta auðlind þín er athygli verkfræðinga og fínstillt leiðsla sem þú getur ekki viðhaldið er skuld, ekki skurður. Haltu skiptum ódýrum svo þú getir fylgt hraðfara markaði.

**Lítið fyrirtæki.** Þú hefur líklega enga gagnafræðinga og þröngt fjárhagsáætlun, svo líttu á gervigreind sem eitthvað sem þú kaupir innbyggt í verkfæri sem þú notar nú þegar, ekki áætlun sem þú mannar. Rammaðu viðbúnað sem gagnahreinlætis- og persónuverndarspurningu frekar en vélnámsverkefni: vittu hvaða viðskiptavinagögn þú átt, hvað þú mátt gera við þau og hvar rangt sjálfvirkt svar myndi kosta þig viðskiptavin. Kjóstu seljendur sem gera gervigreindina valkvæða, gagnsæja og auðvelda að slökkva á.

**Stórfyrirtæki.** Vandinn er eignasafnsstjórnarhættir yfir mörg teymi: sameiginlegur smíða-eða-kaupa stigi, samræmt viðbúnaðarmat og bindingar- og heildarkostnaðargreining svo hópar hætti að finna upp dýrar leiðslur aftur. Fjárhagsáætlaðu MLOps- og mannlegt eftirlit skýrt, staðlaðu viðmótslagið svo veitendur haldist skiptanlegir og stýrðu gervigreindarnotkunartilvikum sem eignasafni með skýrum mælikvörðum og drápsviðmiðum en ekki dreifingu tilraunaverkefna.

**Hið opinbera.** Gagnsæi, innkaupareglur og ábyrgð móta hvert val. Kjóstu kerfi sem vísa í opinberar heimildir í stað þess að búa til stefnu, hafðu mann ábyrgan fyrir afleiddum ákvörðunum og krefstu gagnaflytjanleika og upplýsingagjafar um takmarkanir líkana í samningum. Birtu lýsingu á einföldu máli og áfrýjunarleið, virtu allar margra ára útgönguskyldur sem þú skrifar undir og haltu gervigreind frá lokamatsákvörðunum sem verða að hvíla hjá ábyrgum embættismanni.

## Dæmi

**Sprotafyrirtæki.** Fimm manna tímaskipulagsfyrirtæki vildi bæta við „bókaðu fund fyrir mig“ eiginleika á náttúrulegu máli án þess að taka verkfræðingana tvo af kjarnavörunni. Það valdi minnsta vandamálið sem skipti máli, að þátta beiðni í tillögu að tíma, og afhenti það með hýstu líkani á bak við þunnt innra API svo það gæti skipt um veitanda síðar. Teymið setti hart mánaðarlegt útgjaldaþak, rakti hvort notendur samþykktu tillögðu tímana og ákvað að endurskoða fínstillt líkan aðeins ef umfang réttlætti einhvern tímann aukavinnuna.

**Stórfyrirtæki.** Fjölþjóðlegt tryggingafélag vildi flýta flokkun tjóna. Í stað þess að þjálfa sérsmíðað líkan mótaði það vandann þröngt (beina og draga saman innkomin tjón), gerði frumgerð með hýstu líkani auk sóknar yfir skilmálaskjölin sín og mældi gegn mannlegum afgreiðslutíma og nákvæmni. Aðeins eftir að hafa sannað gildi fínstillti það minna líkan fyrir umfangsmestu tjónategundina til að skera kostnað á kall. Það hélt líkaninu á bak við innra API svo það gæti skipt um veitanda og líkanaði þriggja ára heildareignarkostnað sem innihélt mannlega rýni lágtraustsmála.

**Hið opinbera.** Landsbundið skattyfirvald íhugaði gervigreindaraðstoðarmann til að hjálpa starfsfólki að svara fyrirspurnum borgara. Þar sem þau svör snertu lagaskyldur krafðist stofnunin gagnsæis: kerfið gat aðeins sýnt opinbera leiðsögn með tilvísunum, aldrei fundið upp stefnu, og maður rýndi hverja sjálfvirka tillögu áður en hún fór út. Innkaup kröfðust þess að seljandinn upplýsti um takmarkanir líkansins og veitti gagnaflytjanleika og stofnunin birti lýsingu á einföldu máli á kerfinu og áfrýjunarleið. Hún hélt gervigreind alfarið frá lokamatsákvörðunum og tók þær frá fyrir ábyrga embættismenn.

## Viðskiptarök: hvatar, ávöxtun fjárfestingar og heildarkostnaður

Gervigreindarstefna er til að hjálpa þér að forðast tvær speglaðar bilanir: að offjárfesta í gervigreind sem borgar sig aldrei, og að vanfjárfesta á meðan keppinautar eða systurstofnanir stinga af. Ávöxtun kemur af sparaðri vinnu, styttri hringrásartíma, lækkuðum villuhlutföllum og nýrri getu. Mældu þetta gegn raunverulegri grunnlínu og afslátt fyrir raunverulegan kostnað mannlegs eftirlits, sem sjaldan hverfur.

Heildareignarkostnaður verður að innihalda óglæsilegu liðina: gagnaleiðslur, vöktun, endurþjálfun þegar heimurinn rekur, öryggisrýni og endanlega afvirkjun. Tilraunaverkefni sem lítur ódýrt út getur orðið dýrt þegar það keyrir í stærð árum saman. Settu fram kostnað þess að taka *ekki* upp líka: hægari þjónustu, hærri handvirkan kostnað og stefnumótandi rek. Færðu rök við forystu með eignasafnssýn: fáein veðmál með mikilli vissu, skýra árangursmælikvarða, drápsviðmið fyrir bilanir og viðbúnaðarmat sem sýnir að gagna- og mannauðsundirstöður séu til. Biddu leiðtoga að fjármagna viðbúnað skýrt. Slepptu honum og þú tryggir dýra endurvinnslu.

## Andmynstur og gildrur

- **Lausn í leit að vandamáli.** Að kaupa gervigreind því jafningjar gerðu það og leita svo að notkunartilviki.
- **Að sleppa gagnaviðbúnaði.** Að opna líkön á gögnum sem eru ekki til, ómerkt eða lagalega ónothæf.
- **Sýnikennsludrifnar ákvarðanir.** Að skuldbinda sig út frá fágaðri sýnikennslu án mats í framleiðslugæðum.
- **Að hunsa mannlegu lykkjuna.** Að gera ráð fyrir fullri sjálfvirkni og vanfjárhagsáætla rýni, sem er þar sem mestur kostnaður felst.
- **Þögul binding.** Að byggja djúpt á séreignareiginleikum eins seljanda án útgönguáætlunar.
- **Að vanmeta rekstur.** Að líta á útsetningu sem endamarkið frekar en upphaf viðhaldsskyldu.
- **Reglufylgni sem eftirþanki.** Að bæta gagnsæi og úttektarhæfni við eftir hönnun, á margföldum kostnaði.

## Þroskalíkan

1. **Upphaf.** Ad hoc tilraunir, engin sameiginleg stefna, ákvarðanir knúnar af tískubylgjum og áhuga einstaklinga.
2. **Þróun.** Vandamótun er til fyrir sum verkefni, fyrsta vettvangsgrunnlína birtist, smíða-eða-kaupa er rætt en ósamræmt.
3. **Stöðlun.** Eignasafn gervigreindarnotkunartilvika með skýrum mælikvörðum, skjalfest ákvörðunartré, viðbúnaðarmat og bindingar- og heildarkostnaðargreining, beitt samræmt yfir teymi.
4. **Stjórnun.** Eignasafnið er mælt: viðbúnaður, ávöxtun, heildarkostnaður og kostnaður mannlegs eftirlits eru rakin gegn grunnlínum. Drápsviðmiðum er framfylgt á sönnunargögnum og áhrif á afhendingu og gæði knýja hverja ákvörðun um fara eða ekki fara.
5. **Samhæfing.** Gervigreindarstefna er samþætt viðskipta- og áhættuskipulagningu, viðbúnaði er stöðugt viðhaldið og skipulagsheildin leggur reglulega niður, endurnýjar og endurmótar gervigreindarkerfi á sönnunargögnum og endurjafnar eignasafnið þegar markaðs- og áhættumyndin breytist.

## Hugmyndir til umræðu

- Hvernig ákveðurðu hvenær vandamál hentar í raun ekki gervigreind og hver hefur vald til að segja nei?
- Hvaða viðbúnaðarþröskuldur ætti að hliða verkefni frá tilraun til framleiðslu?
- Hve mikil binding er ásættanleg í skiptum fyrir hraðari tíma til verðmætis?
- Hvernig ættu gagnsæisskyldur að móta ákvörðun um smíða eða kaupa hjá hinu opinbera?
- Hvernig heldurðu heildarkostnaðarmati heiðarlegu þegar seljendur og áhugamenn hafa hvata til að vanmeta hann?
- Hver á gervigreindareignasafnið og hvernig eru drápsákvarðanir teknar?

## Helstu atriði

- Stefna byrjar á raunverulegu vandamáli og heiðarlegri grunnlínu, ekki á tækni.
- Kjóstu einföldustu leiðina: fyrirmæli, síðan sókn, síðan fínstilling, síðan kaup, og sjaldan smíði frá grunni.
- Gagna-, mannauðs- og vettvangsviðbúnaður eru forsendur. Að fjármagna þær er hluti áætlunarinnar.
- Regluverkað og opinbert umhverfi krefst gagnsæis, innkaupasamræmis og útgönguleiða í hönnun.
- Líkanaðu allan heildareignarkostnað og kostnað aðgerðaleysis og varastu bindingu við seljanda frá fyrstu arkitektúrákvörðun.

## Heimildir og frekari lestur

- Ajay Agrawal, Joshua Gans, and Avi Goldfarb, *Prediction Machines: The Simple Economics of Artificial Intelligence*.
- Eric Siegel, *The AI Playbook: Mastering the Rare Art of Machine Learning Deployment*.
- Andriy Burkov, *The Hundred-Page Machine Learning Book*.
- National Institute of Standards and Technology, *AI Risk Management Framework (AI RMF 1.0)*.
- Organisation for Economic Co-operation and Development, *OECD AI Principles*.
- Thomas H. Davenport, *The AI Advantage: How to Put the Artificial Intelligence Revolution to Work*.
