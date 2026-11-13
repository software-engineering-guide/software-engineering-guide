# 7.9 Stofngagna- og tilvísunargagnastjórnun

## Yfirlit og tilgangur

Spurðu fimm kerfi hve marga viðskiptavini skipulagsheildin hefur og þú færð fimm ólíkar tölur. Eitt telur netföng, eitt telur samninga, eitt telur innskráningar og tvö eru ósammála um hvort „Acme Corp“ og „ACME Corporation“ séu sama fyrirtækið. [Stofngagnastjórnun](https://en.wikipedia.org/wiki/Master_data_management) (MDM) er sú grein að sætta kjarnahlutina sem viðskipti þín deila, viðskiptavin, vöru, birgi, starfsmann, staðsetningu, í eina áreiðanlega útgáfu sem hvert kerfi getur treyst.

Byrjaðu á að flokka gögn þín í þrjár tegundir, því þær þurfa ólíka meðferð. Stofngögn lýsa nafnorðum viðskiptanna: fólkinu, stöðunum og hlutunum sem mörg ferli vísa í. Tilvísunargögn eru stýrða orðasafnið sem þau ferli nota: gjaldmiðlakóðar, landakóðar, mælieiningalistar, vöruflokkar. Færslugögn skrá sagnorðin: pöntun lögð inn, greiðsla framkvæmd, sending send. Stofn- og tilvísunargögn eru minni að magni en færslur en vísað er í þau alls staðar, svo villa í þeim spillir öllu niðurstreymis.

Kostnaðurinn af því að gera þetta rangt er áþreifanlegur. Þegar sami viðskiptavinur er til sem fjórar örlítið ólíkar skrár sendirðu fjóra vörulista, þú getur ekki séð eitt samband sem vert er að halda og tekjur-á-viðskiptavin talan þín er hljóðlega röng. [Gullskrá](https://en.wikipedia.org/wiki/Single_source_of_truth), eina trausta útgáfa einingar sett saman úr mörgum uppsprettum, er það sem kemur í stað þessara andstæðu afrita, svo hver samþætting hætti að leysa sama pörunarvandamálið aftur.

Fyrir fyrirtæki sem sætta kerfi safnað gegnum áratuga vöxt og yfirtökur er MDM munurinn á samhangandi viðskiptavinasýn og varanlegum sáttarskatti. Hjá hinu opinbera hækkar húfið: borgari sem birtist sem þrír ólíkir einstaklingar hjá þremur stofnunum getur verið synjað um bætur, skattlagður tvisvar eða týndur milli deilda. Þessi kafli er viðbót við gagnastefnu og gagnastjórnun (kafli 7.1), sem setur eignarhald og stefnu, gagnalíkön og merkingarlag (kafli 7.7), sem skilgreinir hvað einingar þýða, og gagnagæði og gagnavöktun (kafli 7.8), sem heldur skrám hreinum með tímanum.

## Meginreglur

- Flokkaðu gögn þín í stofn-, tilvísunar- og færslugögn. Hver þarf ólíka meðhöndlun.
- Ein gullskrá á hverja raunveruleikaeiningu, sett saman af ásetningi, ekki uppgötvuð af slysni.
- Veldu MDM-arkitektúrstíl sem passar stjórnunar- og töfarþörfum þínum, ekki tískubylgjum.
- Pörun og sigurreglur eru viðskiptareglur, svo skrifaðu þær niður og leyfðu ráðsmönnum að stilla þær.
- Tilvísunargögn eru sameiginlegt orðasafn. Útgáfustýrðu þau og birtu eins og API.
- Stjórnun og ráðsmennska eru drifkraftur MDM. Hugbúnaðurinn er aðeins verkfærin.
- Dreifðu gullskrám sem atburðum svo niðurstreymiskerfi haldist í takt, ekki úrelt.
- Mældu MDM eftir bættum ákvörðunum og fjarlægðum tvíteknum, ekki hlöðnum skrám.

## Ráðleggingar

### Flokkaðu stofn-, tilvísunar- og færslugögn fyrst

Þú getur ekki stýrt því sem þú hefur ekki flokkað, svo byrjaðu á að flokka gagnalénin þín. Gagnlegt próf fyrir stofngögn er hvort röng gildi dreifist: ef ein röng heimilisfangsskrá berst inn í reikningagerð, sendingar og lagalegar tilkynningar ertu að líta á stofngögn. Þetta stýrir fjárfestingu þinni: þú smíðar pörunarvél fyrir viðskiptavinaeininguna, ekki pöntunarlínur. Nefndu lénin skýrt, raðaðu þeim eftir því hve miklum sársauka tvítekning þeirra veldur og byrjaðu á einu eða tveimur sem meiða mest, yfirleitt viðskiptavinur og vara því þau snerta tekjur beint.

### Veldu MDM-arkitektúrstíl af ásetningi

Fjórir algengir arkitektúrstílar eru til og sá rétti veltur á því hve mikið vald þú getur miðstýrt og hve hratt breytingar þurfa að dreifast. Skráningarstíllinn skilur gögn eftir í frumkerfunum og smíðar aðeins vísitölu pöruðra auðkenna, svo hann getur svarað „þessar fimm skrár eru sami viðskiptavinur“ án þess að færa nein gögn. Hann er ódýr og áhættulítill, en aðeins lesaðgangur, svo hann getur ekki lagað uppsprettur. Samþjöppunarstíllinn dregur afrit inn í miðlæga miðstöð og sameinar þau í gullskrár fyrir skýrslugerð, en ýtir ekki leiðréttingum til baka, svo uppsprettur haldast óhreinar. Samlífsstíllinn gengur lengra: hann samstillir hreinsuð gildi aftur til frumkerfa, svo uppsprettur batna með tímanum en starfa enn sjálfstætt. Miðlægi eða færslumiðstöðvarstíllinn gerir MDM-miðstöðina sjálfa að aðalgagnageymslukerfinu, þar sem einingar eru búnar til og breytt beint og hvert annað kerfi sækir úr henni. Þetta gefur sterkasta samkvæmni og stjórn og er erfiðast að taka upp því það breytir hvar vinnan fer fram. Margar skipulagsheildir þróast frá skráningu sem sannar verðmæti í átt að samlífi eftir því sem traust vex og reka fleiri en einn stíl yfir ólík lén.

### Paraðu, sameinaðu og settu sigurreglur skýrt

Kjarni MDM er að ákveða hvenær tvær skrár lýsa sama raunverulega hlutnum. Þetta er [skráartenging](https://en.wikipedia.org/wiki/Record_linkage), sjaldan jafn einfalt og nákvæm lyklasamsvörun því raunveruleg gögn eru full af innsláttarvillum, styttingum og vantandi reitum. Ákvörðunarbundin pörun notar nákvæmar reglur á valda reiti (sama kennitala, eða sama netfang auk póstnúmers). Líkindapörun skorar líkindi yfir marga reiti með [áætlaðri strengjasamsvörun](https://en.wikipedia.org/wiki/Approximate_string_matching) og vigtum, svo „Bob Smith, 12 Main St“ og „Robert Smith, 12 Main Street“ megi dæmast líkleg samsvörun yfir þröskuldi. Að ákveða hvaða skrár vísa í sömu einingu kallast auðkennaleysing og hún knýr allt frá viðskiptavinasýnum til svikagreiningar.

Þegar skrár passa saman verður þú að ákveða hvaða gildi lifa inn í gullskrána. Þessar sigurreglur eru viðskiptarökfræði, svo gerðu þær skýrar: kjóstu nýjasta gildi fyrir símanúmer, fullkomnasta gildi fyrir heimilisfang, áreiðanlegustu uppsprettu fyrir lagalegt nafn. Settu þröskuldaband þar sem samsvörun er sjálfkrafa sameinuð, lægra band þar sem hún er sjálfkrafa hafnað og miðband þar sem maður ákveður, sem er þar sem ráðsmennska býr. Haltu hverri sameiningu afturkræfri og skráðri, því röng sameining sem rennir saman tveimur raunverulegum viðskiptavinum er verri en missir.

### Líttu á tilvísunargögn sem útgáfustýrt sameiginlegt orðasafn

Tilvísunargögn eru sameiginlega orðasafnið sem kerfi þín tala og orðasafn sem rekur veldur hljóðlátu misræmi: þegar eitt kerfi notar ISO-landskóðann „GB“ og annað „UK“ bila tengingar og talningar víkja. Haltu hverjum tilvísunarlista á einum stýrðum stað, birtu hann fyrir hvern notanda og, mikilvægt, útgáfustýrðu hann. Kóðum er bætt við, þeir lagðir niður, klofnir og sameinaðir með tímanum og ef þú skrifar yfir listann á staðnum brýturðu söguskýrslur sem voru réttar undir gömlu kóðunum.

Líttu á tilvísunargagnasafn eins og API með samningi. Birtu það með gildisdagsetningum svo notandi geti spurt „hverjir voru gildu svæðiskóðarnir á þessum degi“, geymdu aflagða kóða frekar en að eyða þeim og skráðu varpið þegar kóði breytir merkingu. Kjóstu viðurkennda ytri staðla þar sem þeir eru til, svo sem ISO-lands- og gjaldmiðlakóða, því staðlar gefa þér samvirkni ókeypis og tengjast opna staðlaaganum í kafla 3.8.

### Líkanaðu stigveldi og tengsl, ekki bara flatar skrár

Stofngögn eru ekki haugur sjálfstæðra lína. Þau eru vefur tengsla. Viðskiptavinur tilheyrir heimili og fyrirtækjamóður. Vara rúllast upp í flokk og vörumerki. Þessi stigveldi bera raunverulega viðskiptamerkingu: veltu sölu upp eftir fyrirtækjamóður og myndin breytist algerlega frá því að velta upp eftir stökum reikningi. Líkanaðu þessi tengsl skýrt svo notendur ferðist um þau samræmt í stað þess að hvert teymi finni upp eigin upprúllun.

Gættu að tilvikinu þar sem ein eining þarf nokkur stigveldi samtímis. Vara getur rúllast upp á einn hátt fyrir fjármál og annan fyrir vöruframboð og hvort tveggja er lögmætt, svo styddu mörg nefnd stigveldi frekar en að þvinga eitt sanntré. Tengsl milli léna skipta líka máli, eins og hvaða birgir veitir hvaða vöru.

### Tengdu gullskrár við merkingarlagið og gagnagæði

Gullskrárnar sem MDM framleiðir eru traustu einingarnar sem merkingarlag kafla 7.7 vísar í þegar það skilgreinir mælikvarða: „virkir viðskiptavinir“ merkir eitthvað aðeins þegar „viðskiptavinur“ er ótvíræður. Fæddu gullskrárnar þínar inn í merkingarlagið svo hver mælikvarði telji sömu tvítakahreinsuðu, leystu einingar.

MDM og gagnagæði (kafli 7.8) eru tvær hliðar sama peningsins: gæðaathuganir greina tvítök, núll og sniðbrot sem MDM leysir síðan, og pörun MDM dregur fram gæðavandamál sem athuganirnar misstu af. Keyrðu samfellda gæðavöktun á stofngögnin sérstaklega: tvítakahlutföll, dreifingar pörunartrausts, fullkomleika lykilreita og stærð rýniraðarinnar, svo rek komi í ljós áður en notendur sjá það.

### Dreifðu gullskrám gegnum atburði

Gullskrá sem ekkert niðurstreymiskerfi sér hjálpar engum. Sterkasta mynstrið er atburðadrifin dreifing: þegar eining er búin til, sameinuð eða leiðrétt gefur MDM-miðstöðin út breytingaatburð og áskrifandi kerfi uppfæra staðbundið afrit sitt. Þetta byggir á [atburðadrifnum arkitektúr](https://en.wikipedia.org/wiki/Event-driven_architecture) og straummynstrunum í kafla 7.2 og heldur tugum kerfa samkvæmum án brothættra næturlotusamstillinga sem skilja alla eftir degi á eftir.

Birtu atburðina með nægu samhengi til að vera gagnlegir: einingarauðkenni, hvað breyttist, nýju sigurgildin og útgáfu svo notendur geti raðað uppfærslum og greint þær sem þeir misstu af. Gerðu notendur eins-áhrifa svo endurspilun atburðar skaði ekki og bjóddu API fyrir kerfi sem geta ekki gerst áskrifendur. Meginreglan úr gagnaarkitektúr og geymslu (kafli 3.4) gildir: hannaðu gullskrána til að flæða, því ein sem enginn notar er bara dýr töflureiknir.

### Úthlutaðu ráðsmennsku og stjórnun á undan verkfærum

MDM bregst sem tækniverkefni og tekst sem stjórnunarverkefni. Mikilvæga hlutverkið er [gagnaráðsmaður](https://en.wikipedia.org/wiki/Data_steward), maður ábyrgur fyrir gæðum og reglum tiltekins léns, sem leysir tvíræðar samsvaranir, stillir sigurreglur og sker úr þegar tvær deildir eru ósammála um hvað „birgir“ merkir. Ráðsmenn eru yfirleitt viðskiptafólk með djúpa lénaþekkingu, ekki verkfræðingar, og þeir þurfa raunverulegt vald og úthlutaðan tíma, því hlutastarfsráðsmennska án umboðs framleiðir nákvæmlega það rek sem MDM átti að stöðva.

Vefðu ráðsmönnunum inn í stjórnunarskipulag kafla 7.1: gagnaeiganda ábyrgan fyrir hvert lén, ráð til að útkljá þverlénadeilur og skýrar stefnur um hver má búa til eða sameina stofnskrár. Skjalfestu ákvarðanir, því reglurnar um að para viðskiptavin eru stofnanaþekking sem verður að lifa af starfsmannaveltu. Verkfæri þjóna stjórnuninni. Að kaupa MDM-vettvang áður en þú nefnir ráðsmenn þína er að kaupa vél án bílstjóra.

## Málamiðlanir: kostir og gallar

| MDM-stíll | Kostir | Gallar |
|---|---|---|
| Skráning (aðeins vísitala) | Ódýr, áhættulítil, uppsprettur óbreyttar | Aðeins lesaðgangur. Getur ekki lagað uppsprettugögn |
| Samþjöppun (miðlæg afrit) | Hreinar skrár fyrir greiningu fljótt | Uppsprettur haldast óhreinar. Engin ritun til baka |
| Samlíf (samstilla aftur í uppsprettur) | Uppsprettur batna. Jafnvægi stjórnar | Meiri samþætting. Samstillingarárekstrar að stýra |
| Miðlæg / færslumiðstöð | Sterkasta samkvæmni og stjórn | Hæsti kostnaður. Breytir hvar vinnan fer fram |
| Ákvörðunarbundin pörun | Fyrirsjáanleg, skýranleg, úttektarhæf | Missir innsláttarvillur, afbrigði og óhrein gögn |
| Líkindapörun | Grípur raunveruleg afbrigði | Þarfnast stillingar. Falskar sameiningar ef kæruleysi |

Kjarnaspenna í MDM er stjórn gegn truflun. Stílarnir sem gefa hreinustu, samkvæmustu gögnin (samlíf og miðlægar miðstöðvar) eru einmitt þeir sem trufla mest hvernig frumkerfi og eigendur þeirra vinna, og sú truflun er þar sem MDM-áætlanir stöðvast. Hagnýta leiðin er að vinna sér inn traust með áhættulitlum stíl og færa sig í átt að sterkari stjórn aðeins þar sem viðskiptarökin eru skýr. Pörunarmálamiðlunin er hliðstæð: ákvörðunarbundnar reglur eru úttektarhæfar en brothættar, líkindaskor er öflugt en krefst ráðsmennsku og umburðarlyndis fyrir stöku rangri sameiningu. Flestar þroskaðar áætlanir blanda hvoru tveggja.

## Spurningar til að ræða með teyminu

1. **Hvaða stofngagnalén valda okkur raunverulega sársauka og höfum við raðað þeim eftir kostnaði frekar en að meðhöndla þau öll í einu?** Margar MDM-áætlanir hrynja undan eigin metnaði, reyna að ná tökum á hverri einingu skipulagsheildarinnar í einu og skila engu í tvö ár. Árangursríka hreyfingin er að finna eitt eða tvö lén þar sem tvítekning og árekstrar kosta raunverulega peninga eða traust, yfirleitt viðskiptavin eða vöru, og magnsetja þann kostnað: sóuðu póstsendingarnar, sáttartímana, röngu tekjutölurnar, úttektarniðurstöðurnar. Komdu með áþreifanleg dæmi um að sama eining birtist á marga vegu yfir kerfin þín og láttu þá röðun segja þér hvar á að byrja, því þröngur, mælanlegur sigur byggir trúverðugleikann sem þú þarft til að stækka.

2. **Hver á hvert stofngagnalén og hafa ráðsmenn okkar vald og tíma til að gera starfið í raun?** MDM-verkfæri án valdeflds ráðsmennsku eru bíll án bílstjóra og algengasti bilunarhátturinn er að nefna ráðsmann á glæru en gefa honum ekkert raunverulegt umboð og enga úthlutaða tíma. Fólkið sem leysir tvíræðar samsvaranir og útkljár deilur um „hvað telst viðskiptavinur“ þarf lénaþekkingu, ákvörðunarvald og varinn tíma. Komdu með skipuritið þitt og spyrðu, fyrir helsta lén þitt, nákvæmlega hver ákveður hvenær tvær skrár eru sami einstaklingurinn og hver sker úr þegar sala og fjármál eru ósammála. Ef þú getur ekki nefnt þann mann og bent á úthlutaðan tíma hans hefurðu fundið bilið sem mun sökkva áætluninni.

3. **Þegar við sameinum tvær skrár í gullskrá, getum við útskýrt og afturkallað ákvörðunina og hvaðan koma lifandi gildin?** Sigurreglur eru viðskiptarökfræði sem flest teymi hafa aldrei skrifað niður, sem þýðir að sameiningar gerast fyrir tilviljun hleðsluraðar eða verkfærasjálfgilda og röng sameining sem rennir saman tveimur raunverulegum viðskiptavinum er sársaukafull að leysa upp. Komdu með raunverulega sameinaða skrá og raktu hvern lifandi reit til uppsprettu hans og reglu: hvers vegna þetta heimilisfang, hvers vegna þetta nafn, hvers vegna þetta símanúmer. Staðfestu að hver sameining sé skráð og afturkræf og að miðband óvissra samsvarana fari til manns frekar en að vera sjálfkrafa sameinað. Ef þú getur ekki útskýrt tiltekna gullskrá geta ráðsmenn þínir ekki varið hana fyrir úttektaraðila eða órétti beittum viðskiptavini.

4. **Hvaða MDM-arkitektúrstíll passar hverju léni sem við ætlum að ná tökum á og getum við varið það val gegn truflun sem hann leggur á eigendur frumkerfa?** Stíllinn sem þú velur ræður því hve mikið þú getur hreinsað gögnin og hve mikið þú truflar teymin sem eiga uppsprettur, og að velja eftir tísku eða söluræðu seljanda frekar en veruleika stjórnar-gegn-truflunar er hvernig áætlanir stöðvast hálfa leið. Skráning sannar verðmæti ódýrt en lagar aldrei uppsprettu. Miðlæg miðstöð gefur sterkasta samkvæmni en flytur hvar skrár eru búnar til, sem er skipulagsbreyting dulbúin sem tæknileg. Komdu með, fyrir hvert frambjóðandalén, heiðarlegt mat á því hve mikið vald þú hefur raunverulega yfir uppsprettueigendum, hve ferskar niðurstreymisafrit verða að vera og hvað ritun til baka myndi brjóta í núverandi vinnuflæði. Í fyrirtækja- og opinberu umhverfi skaltu bæta við flutnings- og breytingastjórnunarkostnaði þess að færa aðalgagnageymslukerfið, því teymin sem daglegt starf þeirra færist munu streitast gegn miðstöð sem ekki var leitað til þeirra um, og stöðvuð samlífsútgáfa er dýrari en hógvær skráning sem afhendist.

5. **Hvernig stillum við pörunarþröskulda og höfum við komið okkur saman um hvaða hlutfall falskra sameininga og missta samsvarana við getum lifað við í hverju léni?** Sérhver líkindapörunarvél skiptir fölskum sameiningum (að renna saman tveimur raunverulegum einingum) fyrir misstar samsvaranir (að skilja eina einingu eftir klofna) og jafnvægið er viðskiptaákvörðun, ekki sjálfgefið sem einhver skildi eftir í verkfærinu. Settu sjálfvirk sameiningar- og höfnunarbönd of breið og þú spillir gullskrám hljóðlega. Settu þau of þröng og mannlega rýniröðin vex hraðar en ráðsmenn geta hreinsað hana. Komdu með núverandi traustsdreifingu, stærð og aldur rýniraðarinnar og sýnishorn af villum beggja tegunda svo herbergið sjái raunverulegan kostnað hvorrar áttar. Í opinberu auðkennaléni skaltu hneigjast fast í átt að misstum samsvörunum og mannlegri rýni, því röng sameining getur synjað bótum eða afhjúpað gögn eins borgara fyrir öðrum og áfrýjunar- og úttektarkostnaður þeirrar villu dvergar kostnað tvítaks sem ráðsmaður leysir í næstu viku.

6. **Hvernig komast niðurstreymiskerfi að því að gullskrá breyttist og hve úrelt má hvert vera áður en ákvörðun fer úrskeiðis?** Fullkomlega leyst gullskrá sem ekkert kerfi notar er dýr töflureiknir og dreifingarbúnaðurinn, hvort sem það eru breytingaatburðir, áskriftar-API eða næturlota, setur hljóðlega hve núgildandi hver háð ákvörðun er. Atburðadrifin dreifing heldur tugum notenda nærri rauntíma en krefst eins-áhrifa notenda og útgáfustýrðra atburða. Nætursamstilling er einfaldari en skilur alla eftir degi á eftir, sem getur verið í lagi fyrir markpóstlista og hættulegt fyrir svikaathugun. Komdu með lista yfir notandakerfi, ferskleikann sem hvert þarf í raun og hvernig notandi sem missir af uppfærslu í dag nær sér. Fyrir stóra eða opinbera skipulagsheild skaltu nefna hver á samninginn um þessa atburði og hvernig áskrifandi greinir týnd skilaboð, því einingabreyting sem hljóðlega nær ekki til einnar stofnunar endurskapar nákvæmlega sundrunguna sem MDM var fjármagnað til að fjarlægja.

## Sjónarhorn eftir geirum

**Sprotafyrirtæki.** Með örfáa verkfræðinga og ekkert svigrúm til að sóa skaltu ekki kaupa MDM-vettvang. Náðu tökum á einu einingunni sem spillir tölum þínum, yfirleitt viðskiptavininum tvítekna yfir sjálfsafgreiðslu og sölu, með pörunarverki í vöruhúsinu sem þú rekur nú þegar og einum manni sem rýnir óvissar samsvaranir vikulega. Haltu hverri sameiningu skráðri og afturkræfri svo slæm regla kosti eftirmiðdag, ekki viðskiptasamband, og endurskoðaðu þyngri verkfæri aðeins þegar handvirka rýniröðin vex fram úr einum rýni.

**Lítið fyrirtæki.** Þú hefur engan gagnaráðsmann og þröngt fjárhagsáætlun, svo líttu á þetta sem kaup-ekki-smíða ákvörðun og hallaðu þér að stöðlum sem þú færð ókeypis. Kjóstu verkfæri sem tvítakahreinsa tengiliði nú þegar og tala ISO-lands- og gjaldmiðlakóða frekar en sérsmíðaða miðstöð sem þú getur ekki viðhaldið og veldu eitt lén, yfirleitt viðskiptavini eða vörur, þar sem tvítök kosta þig raunverulega peninga. Úthlutaðu ábyrgðinni á nefndan eiganda jafnvel þótt það sé brot af einnar manneskju viku, því orðasafn sem rekur án þess að nokkur horfi er það sem hljóðlega brýtur skýrslur þínar.

**Stórfyrirtæki.** Yfir tylft ERP- og CRM-kerfa safnaðra gegnum yfirtökur er verkið eignasafnsstjórnun: raðaðu lénum eftir kostnaði tvítekningar þeirra, settu upp valdefldan ráðsmenn í viðskiptunum og staðlaðu sigurreglur og útgáfustýringu tilvísunargagna svo hópar hætti að leysa sama pörunarvandamálið aftur. Fjárhagsáætlaðu samþættingu og varanlegan ráðsmennskukostnað skýrt, dreifðu gullskrám sem útgáfustýrðum atburðum svo uppsprettur batni með tímanum og stýrðu MDM sem mældri áætlun með tvítakahlutföllum og rýniraðarmælikvörðum frekar en einskiptis hreinsun.

**Hið opinbera.** Innkaupareglur, ströng gagnamiðlunarlög og opinber ábyrgð móta hvert val. Lyklaðu einstaklingseininguna á stýrt landsauðkenni, útgáfustýrðu tilvísunargögnum eftir gildisdagsetningu svo söguskrár haldist réttar og gerðu auðkennaleysingu viljandi varkára: óvissar samsvaranir fara til þjálfaðra ráðsmanna, aldrei sjálfvirkar sameiningar, því röng sameining getur synjað bótum eða lekið gögnum eins borgara til annars. Skráðu hverja pörun fyrir úttekt og áfrýjun, krefstu gagnaflytjanleika og upplýstrar pörunarrökfræði frá seljendum og haltu allri getunni innan samvirknistaðlanna sem hið opinbera hefur þegar skuldbundið sig til.

## Dæmi

**Sprotafyrirtæki.** Ört vaxandi hugbúnaðarfyrirtæki selur gegnum bæði sjálfsafgreiðsluskráningu og söluteymi og rásirnar tvær búa til sama viðskiptavin tvisvar undir örlítið ólíkum fyrirtækjanöfnum. Tekjur á reikning líta rangar út og söluteymið heldur áfram að hringja kalt í núverandi notendur. Frekar en að kaupa þungan vettvang byrja þau á léttri skráningu: pörunarverki í gagnavöruhúsinu sem tengir skrár eftir netfangaléni og stöðluðu fyrirtækjanafni, með einum hlutastarfsráðsmanni sem rýnir óvissar samsvaranir vikulega. Það kostar lítið, lagar skýrsluvilluna og sannar verðmætið sem réttlætir meiri fjárfestingu eftir því sem þau vaxa.

**Stórfyrirtæki.** Alþjóðlegur framleiðandi hefur vaxið gegnum yfirtökur og rekur tylft ERP- og CRM-kerfa, hvert með eigin birgjaskrár, svo sami birgirinn birtist á fimmtán vegu og fyrirtækið getur ekki samið sem einn kaupandi eða séð raunverulega eyðslu sína. Það setur upp samlífsstíls MDM-miðstöð fyrir birgja- og vörulén, notar ákvörðunarbundna pörun á skatta- og skráningarauðkenni auk líkindaskorunar á nöfn og heimilisföng. Nefndir ráðsmenn í innkaupum stilla sigurreglurnar og vinna rýniröðina og gullskrár eru birtar sem breytingaatburðir sem flæða aftur inn í hvert ERP svo hreinsuð gögn bæti uppsprettur. Sameinuð eyðslusýnileiki opnar betri samningsskilmála og sáttarskatturinn sem át fjármál á hverjum ársfjórðungi fellur verulega.

**Hið opinbera.** Landsstjórn vill að stofnanir líti á borgara sem einn einstakling en ekki ókunnugan við hvert afgreiðsluborð, á meðan hún virðir ströng lagaleg mörk gagnamiðlunar. Hún smíðar miðlæga stofngagnamiðstöð fyrir einstaklingseininguna, lyklaða á stýrt landsauðkenni, með tilvísunargögnum útgáfustýrðum eftir gildisdagsetningu svo söguskrár haldist réttar. Auðkennaleysing er viljandi varkár: óvissar samsvaranir fara til þjálfaðra ráðsmanna frekar en sjálfvirkra sameininga, því röng sameining gæti synjað einhverjum um bætur eða afhjúpað gögn hans og hver pörun er skráð fyrir úttekt og áfrýjun. Ávinningurinn er færri tvítekin skrá, minni svik af klofnum auðkennum og borgari sem þarf ekki að sanna hver hann er við hverjar dyr, innan samvirknistaðla kafla 3.8.

## Viðskiptarök: hvatar, ávöxtun fjárfestingar og heildarkostnaður

Ávöxtun MDM kemur af því að fjarlægja skatt sem flestar skipulagsheildir greiða án þess að nefna hann. Tvítekin og andstæð skrá kostar peninga á augljósa vegu (sóuð markaðssetning til sömu manneskju fimm sinnum, sendingarvillur af úreltum heimilisföngum, misstir magnafslættir) og á minna augljósa vegu (greinendur sem sætta talningar, stjórnendur sem ákveða á tölum sem eru hljóðlega rangar, úttektaraðilar sem rukka tíma til að greiða úr hvaða skrá er raunveruleg). Sameinuð birgjasýn borgar oft fyrir alla áætlunina með betri samningsskilmálum einum.

Heildareignarkostnaður hefur þrjá hluta: vettvanginn eða smíðina, samþættinguna við uppsprettur og notendur og, mestan með tímanum, viðvarandi ráðsmennskuna. Samþættingarkostnaðurinn er auðvelt að vanmeta, því að tengja tylft öldruð frumkerfi er þar sem MDM-áætlanir blæða tímaáætlun og fjárhagsáætlun, og ráðsmennskukostnaðinn er auðvelt að gleyma, því hann er varanlegur rekstrarkostnaður, ekki einskiptis smíði. Til að færa rök við forystu skaltu tengja MDM við tölur sem þeir fylgjast þegar með: tekjunákvæmni, markaðsskilvirkni, innkaupasparnað, úttektarkostnað og eftirlitsáhættu, byrja síðan þröngt og láta mældan sigur á einu lén með miklum sársauka fjármagna útvíkkunina.

## Andmynstur og gildrur

- **Umfang sem sýður hafið:** að ná tökum á hverju léni í einu, skila engu árum saman og missa stuðning áður en fyrsti sigurinn kemur.
- **Verkfæri á undan stjórnun:** að kaupa MDM-vettvang áður en ráðsmenn og eigendur eru nefndir, svo vélin hefur engan bílstjóra.
- **Hlutastarfsráðsmenn án valds:** að úthluta ráðsmennsku á glæru án raunverulegs umboðs eða varins tíma.
- **Hljóðlátar sigurreglur:** að sameina skrár eftir verkfærasjálfgildi eða hleðsluröð, án skrifaðra reglna og án leiðar til að útskýra gullskrá.
- **Óafturkræfar sameiningar:** að sjálfsameina óvissar samsvaranir án afturköllunar, svo röng samruni tveggja raunverulegra eininga verði varanlegur skaði.
- **Tilvísunargögn yfirskrifuð á staðnum:** að breyta kóðalistum án útgáfustýringar, sem brýtur hverja söguskýrslu sem var rétt undir gömlu kóðunum.
- **Gullskrár sem enginn notar:** að smíða tandurhreina miðstöð sem ekkert niðurstreymiskerfi gerist áskrifandi að, svo hreinu gögnin ná aldrei til ákvarðana.
- **Að finna upp staðalkóða aftur:** að mynta eigin lands- eða gjaldmiðlalista þegar ISO-staðlar eru til og tapa samvirkni að ástæðulausu.

## Þroskalíkan

- **Stig 1, Upphaf:** Stofn- og tilvísunargögn eru óstýrð. Sama eining er til oft án áreiðanlegrar útgáfu, kóðalistar víkja, pörun er handvirk og viðbragðsdrifin og enginn á vandamálið, svo talningar kjarnaeininga eru ósammála og enginn getur sagt hver er rétt.
- **Stig 2, Þróun:** Lykillén eru viðurkennd og einhver tvítakahreinsar þau, oft í vöruhúsinu fyrir skýrslugerð. Grunn ákvörðunarbundin pörun er til, tilvísunarlistar eru safnaðir og fáeinir menn starfa sem óformlegir ráðsmenn, en vinnubrögð eru ólík eftir teymum, uppsprettur haldast óhreinar og reglur búa í hausum fólks frekar en á pappír.
- **Stig 3, Stöðlun:** MDM er stýrð áætlun beitt samræmt um skipulagsheildina. Stofnlén hafa nefnda eigendur og valdefldan ráðsmenn, pörunar- og sigurreglur eru skjalfestar og framfylgdar, gullskrár eru framleiddar og dreift til notenda og tilvísunargögn eru útgáfustýrð og birt með gildisdagsetningum eins og API.
- **Stig 4, Stjórnun:** Áætlunin er mæld og stýrð gegn grunnlínum. Tvítakahlutföll, dreifingar pörunartrausts, hlutföll falskra sameininga og missta samsvarana, fullkomleiki lykilreita og stærð og aldur rýniraðar eru rakin sem mælikvarðar. Þröskuldar eru stilltir gegn þeim tölum frekar en eftir tilfinningu og MDM-verðmæti (tekjunákvæmni, innkaupasparnaður, rýnikostnaður) er magnsett og skýrt eigendum á föstum takti.
- **Stig 5, Samhæfing:** Gullskrár flæða sem útgáfustýrðir atburðir nærri rauntíma, nærir merkingarlagið og eru treystar um skipulagsheildina. Pörun er stöðugt bætt gegn mældum niðurstöðum, tökin ná til nýrra léna sem endurtakanleg geta og MDM er samþætt stjórnun og áhættuskipulagningu svo áætlunin aðlagist eftir því sem uppsprettur, staðlar og einingalandslagið breytast.

## Hugmyndir til umræðu

1. Ef tvö kerfi ykkar eru ósammála um hve marga viðskiptavini þið hafið, hvort er rétt og hvernig mynduð þið sanna það?
2. Hvaða stofngagnalén myndi skila stærsta mælanlega sigrinum ef þið næðuð tökum á því fyrst og hvers virði er sá sigur?
3. Hvar myndi líkindapörun hjálpa ykkur í dag og eruð þið sátt við stöku röngu sameininguna sem hún felur í sér?
4. Hvernig útgáfustýrið þið tilvísunargögn ykkar og hvað brotnar í söguskýrslum ykkar þegar kóði breytir merkingu?
5. Hver er nefndi ráðsmaðurinn fyrir mikilvægustu eininguna ykkar og hefur hann vald og tíma til að gera starfið í raun?
6. Þegar gullskrá breytist, hvernig komast niðurstreymiskerfi ykkar að því og hve úrelt mega þau vera áður en það meiðir?

## Helstu atriði

- Flokkaðu gögn þín í stofn-, tilvísunar- og færslugögn. Fjárfestu í pörun og stjórnun þar sem tvítekning kostar mest.
- Framleiddu eina gullskrá á hverja raunveruleikaeiningu, sett saman með skýrum, afturkræfum, skráðum sigurreglum.
- Veldu MDM-arkitektúrstíl (skráningu, samþjöppun, samlíf eða miðlæga miðstöð) sem passar lyst þinni á stjórn og truflun.
- Líttu á tilvísunargögn sem útgáfustýrt sameiginlegt orðasafn, kjóstu viðurkennda staðla og skrifaðu aldrei yfir kóðalista á staðnum.
- MDM tekst á stjórnun og ráðsmennsku, ekki verkfærum. Dreifðu gullskrám sem atburðum og mældu áætlunina eftir bættum ákvörðunum.

## Heimildir og frekari lestur

- David Loshin, *Master Data Management*
- Alex Berson and Larry Dubov, *Master Data Management and Data Governance*
- Dan Power, *The Definitive Guide to Master Data Management*
- John Talburt, *Entity Resolution and Information Quality*
- Peter Christen, *Data Matching: Concepts and Techniques for Record Linkage, Entity Resolution, and Duplicate Detection*
- Ivan P. Fellegi and Alan B. Sunter, "A Theory for Record Linkage," *Journal of the American Statistical Association*
- DAMA International, *DAMA-DMBOK: Data Management Body of Knowledge*
- Ralph Kimball and Margy Ross, *The Data Warehouse Toolkit*
