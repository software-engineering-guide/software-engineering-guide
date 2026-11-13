# 3.5 Stigvöxtur, afköst og seigla

## Yfirlit og tilgangur

[Stigvöxtur](https://en.wikipedia.org/wiki/Scalability), afköst og seigla eru þrír aðgreindir eiginleikar, og fólk blandar þeim oft saman. **Afköst** eru hve hratt kerfið svarar og hve mikla vinnu það afkastar á hverja tilfangseiningu. **Stigvöxtur** er hve vel það heldur afköstum þegar álag vex. **Seigla** er hve vel það heldur áfram að virka, eða skerðist mjúklega, þegar eitthvað bilar. Kerfi getur verið hratt en ekki stigvaxandi (frábært við lágt álag, hrynur við hátt), stigvaxandi en brothætt (ræður við magn en fellur þegar einn íhlutur bilar) eða seigt en hægt. Stór skipulagsheild þarf alla þrjá, hannaða inn frá byrjun, því að bæta einhverjum þeirra við eftir opnun er dýrt og truflandi.

Fyrir kerfi fyrirtækja og hins opinbera eru afleiðingar mistaka opinberar og alvarlegar. Hugsaðu um bótagátt sem bognar á fyrsta degi nýs úrræðis, skilakerfi skatta sem rennur út á tíma á skilafresti eða greiðsluvettvang sem fellur á annatíma verslunar. Þetta eru bilanirnar sem rata í fréttir, kalla fram rannsóknir og tæra traust almennings. Þessi kerfi standa líka frammi fyrir mjög toppóttu, oft lögbundnu álagi (skilafrestir, innritunarglugga, útborgunardagar) og ströngum skyldum um aðgengi og endurheimt. Þú verður að skipuleggja getu fyrir fyrirsjáanlegar bylgjur, skerðast mjúklega undir ófyrirsjáanlegum og endurheimta innan skilgreindra tíma- og gagnatapsmarka eftir hamfarir. Þetta er verkfræði með ábyrgðarvídd gagnvart almenningi.

Þessi kafli fjallar um lárétta á móti lóðréttum stigvexti, ástandsleysi og [sneiðingu](https://en.wikipedia.org/wiki/Shard_(database_architecture)) sem hjálpartæki stigvaxtar, [álagsdreifingu](https://en.wikipedia.org/wiki/Load_balancing_(computing)), [sjálfvirka stigstillingu](https://en.wikipedia.org/wiki/Autoscaling) og getuáætlun, afkastaverkfræði með skýrum fjárhagsáætlunum, seigluminstur og [glundroðaverkfræði](https://en.wikipedia.org/wiki/Chaos_engineering) og fjölsvæða [hamfaraendurheimt](https://en.wikipedia.org/wiki/Disaster_recovery) römmuð af RTO, RPO og órofa rekstri. Sameinandi boðskapurinn er að þessir eiginleikar eru afurð yfirvegaðrar hönnunar og samfelldra prófana, ekki vonar.

*Sjá einnig:* kafla 3.3 (dreifð kerfi), kafla 9.1 (áreiðanleikaverkfræði) og kafla 9.2 (sýnileiki og vöktun).

## Meginreglur

- **Hannaðu fyrir útvíkkun, ekki uppstækkun.** Lóðrétt stigvöxtur hefur þak og er [einn bilunarpunktur](https://en.wikipedia.org/wiki/Single_point_of_failure). Lárétt stigvöxtur er leiðin til stórs, seigs umfangs.
- **Ástandsleysi er hjálpartæki láréttrar stigvaxtar.** Ef hver beiðni getur farið á hvaða tilvik sem er geturðu bætt við og fjarlægt getu frjálslega.
- **Þú getur ekki bætt það sem þú mælir ekki.** Afkastavinna er knúin af sniðgreiningu og álagsprófun gegn skýrum fjárhagsáætlunum, aldrei af ágiskunum.
- **Allt bilar. Hannaðu fyrir það.** Gerðu ráð fyrir að íhlutir muni bila og smíðaðu svo kerfið lifi bilun þeirra.
- **Mjúk skerðing slær harða bilun.** Hlutavirkt kerfi sem losar sig við ónauðsynlega eiginleika er betra en heildarrekstrarrof.
- **Getu er skipulagt, bylgjur eru gleyptar.** Spáðu fyrir um fyrirsjáanlegt álag. Notaðu sjálfvirka stigstillingu og rými fyrir restina.
- **Endurheimtarmarkmið eru viðskiptaákvarðanir.** RTO og RPO eru valin af rekstrinum gegn kostnaði og síðan verkfræðuð.
- **Prófaðu seiglu af ásetningi.** Þú veist ekki að kerfi er seigt fyrr en þú hefur látið það bila vísvitandi.

## Ráðleggingar

### Kjóstu lárétta stigvöxt og hannaðu ástandslausar þjónustur

Lóðréttur stigvöxtur (stærri vélar) er einfaldur og stundum rétta fyrsta skrefið, en hann rekst á hart þak, verður óhóflega dýr í efri endanum og skilur eftir einn bilunarpunkt. **Láréttur stigvöxtur** (fleiri vélar á bak við álagsdreifi) nær mun lengra og bætir aðgengi, því að missa eitt tilvik er lifanlegt. Forsendan er **ástandsleysi**. Haltu engu biðlaraseti eða beiðnaástandi á tilvikinu. Ýttu því í sameiginlega geymslu (gagnagrunn, skyndiminni, tóka). Ástandslausar þjónustur má bæta við, fjarlægja, skipta út og álagsdreifa frjálslega, sem er það sem gerir bæði sjálfvirka stigstillingu og rúllandi uppsetningu mögulega. Þar sem ástand verður að skipta skaltu **sneiða** eftir lykli sem dreifir álagi jafnt og heldur tengdum gögnum á sömu sneið.

### Álagsdreifðu, stigstilltu sjálfvirkt og skipuleggðu getu

Settu **álagsdreifi** fyrir framan hvert stigvaxið þrep til að dreifa umferð og leiða framhjá óheilbrigðum tilvikum með heilsuathugunum. Stilltu **sjálfvirka stigstillingu** til að bæta við getu þegar leiðandi vísir (örgjörvi, dýpt beiðnaraðar, töf) fer yfir þröskuld og fjarlægja hana þegar álag minnkar. Stilltu hraða stigstillingar og kælitíma svo þú hvorki dragist aftur úr toppi né sláist fram og til baka. Sjálfvirk stigstilling kemur ekki í staðinn fyrir **getuáætlun**. Fyrir fyrirsjáanlegar, rekstrarkritískar bylgjur (skattafresti, innritunartímabil, söluviðburði) skaltu spá fyrir um álagið, útvega eða forhita getu fyrirfram og álagsprófa að því marki með góðum fyrirvara. Sjálfvirk stigstilling ein og sér getur ekki brugðist samstundis við stökkbreytingu og kaldræsingar bæta við töf einmitt þegar þú hefur minnst efni á því. Hafðu alltaf rými. Að keyra á 100% skilur ekkert svigrúm til að gleypa toppa eða bilanir.

### Verkfræddu afköst gegn skýrum fjárhagsáætlunum

Settu **afkastafjárhagsáætlanir** (áþreifanleg markmið eins og p95 API-töf undir 200 ms, síðu gagnvirka á innan við 2 sekúndum eða kostnað á færslu undir þröskuldi) og framfylgdu þeim í prófunum og vöktun svo afturfarir felli leiðsluna frekar en að ná til notenda. Knúðu fínstillingu með **mælingum**. Sniðgreindu til að finna raunverulega flöskuhálsinn, sem er sjaldan þar sem þú giskar, og álagsprófaðu til að finna hvar kerfið brotnar og hvernig það hegðar sér nálægt því marki. Einbeittu þér að mikilvægu leiðinni og halanum (p95/p99), því í stórum stíl ráða halatafir notendaupplifun. Fínstilltu stærsta flöskuhálsinn fyrst, mældu aftur og hættu þegar þú uppfyllir fjárhagsáætlunina. Að ofhámarka kóða sem þegar er nægur er sóun.

### Smíðaðu inn seigluminstur og staðfestu með glundroðaverkfræði

Beittu seigluminstrunum úr dreifðum kerfum: tímamörkum, afmörkuðum endurtekningum með undanhaldi, [rofum](https://en.wikipedia.org/wiki/Circuit_breaker_design_pattern) (sem bila hratt þegar ósjálfstæði er óheilbrigt) og skilrúmum (sem einangra tilfangasjóði svo ein bilun geti ekki tæmt hina), auk **mjúkrar skerðingar** (að losa eða einfalda ónauðsynlega eiginleika undir álagi: slökkva á meðmælum, afgreiða skyndiminnisefni, setja ekki-brýna vinnu í biðröð) og **álagslosunar** (að hafna eða hemja umframbeiðnir til að vernda kjarnann frekar en að hrynja alveg). Útrýmdu einstökum bilunarpunktum með offramleiðslu á hverju þrepi. Staðfestu síðan seiglu með **glundroðaverkfræði**. Sprautaðu vísvitandi inn bilunum (drepið tilvik, bætið við töf, rofin ósjálfstæði, felldu svæði) í stýrðum tilraunum, byrjaðu í prófun og þroskaðu yfir í leikdaga í framleiðslu, til að sanna að kerfið hegði sér eins og hannað var. Seigla sem aldrei hefur verið prófuð er aðeins tilgáta.

### Skipuleggðu fjölsvæði, hamfaraendurheimt og órofa rekstur

Ákveddu endurheimtarmarkmiðin skýrt: **RTO** (Recovery Time Objective, hve lengi þú getur verið niðri) og **RPO** (Recovery Point Objective, hve miklu af gögnum þú hefur efni á að tapa). Þetta eru viðskiptaákvarðanir með bein kostnaðaráhrif og þær knýja arkitektúrinn. Valkostir spanna kostnað og hraða: afritun-og-endurheimt (ódýrust, hægust), tilraunaljós, heit biðstaða og virk-virk fjölsvæða uppsetning (dýrust, nánast engin RTO/RPO). Veldu þrepið sem mikilvægi hvers kerfis réttlætir. Ekki þarf allt virk-virk. Afritaðu gögn milli svæða í samræmi við valið RPO, sjálfvirknivæddu yfirtöku og umfram allt, **prófaðu yfirtökuna reglulega**. Óprófuð hamfaraendurheimt bregst áreiðanlega þegar hennar er loks þörf. Vefðu allt þetta inn í **áætlun um órofa rekstur** sem nær yfir fólk, samskipti og handvirkar varaleiðir, ekki bara tækni.

## Málamiðlanir: kostir og gallar

| Val | Kostir | Gallar |
|---|---|---|
| Lóðrétt stigvöxtur | Einföld, engin kóðabreyting, lítil fyrirhöfn í upphafi | Hart þak, dýr í efri endanum, einn bilunarpunktur |
| Lárétt stigvöxtur | Nánast ótakmarkaður stigvöxtur, bætir aðgengi | Krefst ástandsleysis, álagsdreifingar, meiri reksturs |
| Sjálfvirk stigstilling | Samræmir kostnað við eftirspurn, ræður við breytilegt álag | Bregst við með töf, kaldræsingar, getur slegist fram og til baka ef illa stillt |
| Virk-virk fjölsvæða | Nánast engin RTO/RPO, lifir svæðismissi | Hæsti kostnaður og flækja, erfitt gagnasamræmi |
| Afritun-og-endurheimt | Ódýrust, einföldust | Langt RTO, stærri gagnatapsgluggi |

Meginmálamiðlunin er kostnaður gegn tryggingu. Hver aukning stigvaxtarrýmis, afkasta og endurheimtargetu kostar peninga og flækju, og ávöxtunin er ólínuleg. Að fara úr 99,9% í 99,99% aðgengi, eða úr klukkustundar RTO í sekúndur, getur margfaldað kostnað. Agi er að stærðarákvarða hverja fjárfestingu eftir raunverulegu mikilvægi kerfisins og umburðarlyndi rekstrarins gagnvart niðurtíma og gagnatapi, frekar en að verkfræða allt viðbragðslaust fyrir hæsta þrep. Borgarasnúið greiðslukerfi vinnur sér inn virk-virk offramleiðslu. Innra skýrslutæki gerir það ekki.

## Spurningar til að ræða með teyminu

1. **Þegar síðasta alvarlega atvik ykkar gerðist, hvert af þremur (afköst, stigvöxtur, seigla) brást í raun og lagfærðuð þið rétta?** Kaflinn aðgreinir þau af ásetningi: kerfi getur verið hratt en hrunið undir álagi, stigvaxið en fallið þegar einn íhlutur deyr eða lifað bilanir á meðan það er hægt. Teymi greina oft rangt, bæta við getu við seiglu vanda eða herða kerfi sem var einfaldlega vanútvegað fyrir bylgju. Farðu í gegnum síðustu tvö alvarlegu atvik og nefndu hvaða eiginleiki brotnaði og hverju viðbragðið bætti í raun. Greinarmunurinn breytir lagfæringunni: ástandsleysi og sneiðing fyrir stigvöxt, offramleiðsla og rofar fyrir seiglu, sniðgreining og fjárhagsáætlanir fyrir afköst. Að fá flokkinn réttan er munurinn á að eyða í lækninguna og að eyða í einkenni.

2. **Fella afturfarir í afköstum leiðsluna ykkar, eða ná þær til notenda áður en nokkur tekur eftir?** Afkastafjárhagsáætlun (p95 töf, gagnvirknitími síðu, kostnaður á færslu) verndar aðeins notendur ef henni er framfylgt sjálfvirkt, svo breyting sem sprengir hana felli smíðina frekar en að fara út. Í stóru teymi með marga þátttakendur læðist töf inn gegnum þúsund litlar innritanir, og án hliðs rotnar halinn hægt þar til opnun afhjúpar hann. Komdu með núverandi fjárhagsáætlanir þínar og athugaðu hvort þær eru tengdar við CI og vöktun, og hvort þær miða á p95 og p99 frekar en meðaltöl, því halinn er það sem notendur finna í stórum stíl. Þar sem engin fjárhagsáætlun er til er að setja eina fyrsta skrefið. Framfylgd er það sem breytir góðum ásetningi í eiginleika sem lifir vöxt teymis.

3. **Undir álagi, hvað losnar fyrst og hönnuðuð þið þá röð eða uppgötvið þið hana í rekstrarrofinu?** Mjúk skerðing og álagslosun þýða að kerfið gefur upp ónauðsynlega vinnu til að vernda kjarnann, en aðeins ef þið hafið ákveðið fyrirfram hvað er nauðsynlegt. Fyrir borgarasnúna þjónustu er sú röðun oft stefnuákvörðun: skil á skattframtali verða að lifa jafnvel þó stöðumælaborð og söguleg uppfletting fari dimm. Ef enginn hefur valið losar kerfið það sem bilar fyrst, sem getur verið nákvæmlega það sem notendur þurfa mest. Listaðu eiginleika þína í forgangsröð og staðfestu að arkitektúrinn geti sleppt þeim lágforgangs (skyndiminnissvör, óvirk meðmæli, biðraðaða ekki-brýna vinnu) án þess að taka mikilvægu leiðina með sér. Prófaðu það síðan undir raunverulegu álagi, því óprófuð skerðing er aðeins von.

4. **Fyrir mikilvægasta kerfið ykkar, hver eru RTO og RPO, hver valdi þessar tölur í raun og hvenær sönnuðuð þið síðast að þið getið staðið við þær?** Recovery Time Objective (hve lengi þú getur verið niðri) og Recovery Point Objective (hve miklu af gögnum þú hefur efni á að tapa) eru viðskiptaákvarðanir með bein kostnaðaráhrif, samt eru þær í stóru teymi oft fundnar upp af þeim sem skrifaði keyrsluhandbókina frekar en í eigu þeirra sem bera ábyrgð á þjónustunni. Togið á móti er kostnaður gegn tryggingu: að minnka RTO úr klukkustund í sekúndur eða RPO úr mínútum í núll getur margfaldað innviðareikninginn, svo rétta talan er sú sem reksturinn mun í raun borga fyrir, ekki sú áhrifamesta. Komdu með skjalfestu markmiðin, dagsetningu síðasta raunverulega yfirtökuprófs og mældan tíma og gagnatap sem það próf skilaði, því óprófað markmið er ósk. Í fyrirtækja- og opinberu umhverfi geta þessar tölur verið settar með lögum, samningi eða SLA, svo nefndu hver staðfestir þær og hvort síðasta æfing uppfyllti skylduna eða brást hljóðlega.

5. **Fyrir stærstu fyrirsjáanlegu bylgju ykkar, treystið þið sjálfvirkri stigstillingu til að bregðast við á staðnum, eða hafið þið spáð fyrir um álagið, forútvegað og álagsprófað að því marki?** Sjálfvirk stigstilling bregst við með töf og kaldræsingar bæta við töf einmitt þegar þið hafið minnst efni á því, svo þekkt stökkbreyting (skilafrestur, innritunargluggi, söluviðburður) er einmitt tilvikið þar sem viðbragðsdrifin stigstilling brestur og yfirveguð getuáætlun vinnur. Spennan er kostnaður: að forhita getu fyrir topp þýðir að borga fyrir rými sem situr ónotað mestan hluta ársins, og freistingin er að vona að sjálfvirk stigstilling dekki það ókeypis. Komdu með topptölur síðasta árs, spá þessa árs með vexti og niðurstöður álagsprófs sem keyrt var á margfeldi þeirrar spár frekar en á meðalumferð dagsins í dag. Fyrir opinbera þjónustu eða fyrirtækjaþjónustu sem stendur frammi fyrir lögbundinni bylgju skaltu bæta við afleiðingu þess að fá það rangt, því bótagátt eða skattakerfi sem bognar á fyrsta degi verður opinber rannsókn, ekki bara hægur eftirmiðdagur.

6. **Hafið þið nokkurn tíma vísvitandi fellt íhlut í framleiðslu og samsvarar offramleiðsluþrep hvers kerfis í raun mikilvægi þess og kostnaði?** Seigla sem aldrei hefur verið prófuð er tilgáta, og þrepin sem þú getur keypt spanna frá ódýrri afritun-og-endurheimt gegnum heita biðstöðu til dýrrar virk-virk fjölsvæða uppsetningar, svo agi er að eyða tryggingu þar sem hún er réttlætt frekar en að gullhúða allt eða vernda ekkert. Sjónarmiðin sem togast á eru sprengjusvæði og fjárhagsáætlun: glundroðatilraunir verða að hafa handrið og rofa til að hætta við, og virk-virk fyrir innra skýrslutæki er sóun á meðan eingöngu afritun fyrir greiðsluvettvang er vanræksla. Komdu með skrá yfir einstaka bilunarpunkta þína, offramleiðsluþrep hvers mikilvægs kerfis og sönnunargögn um síðustu stýrðu bilanainnsprautun og hvað hún leiddi í ljós. Í eignasöfnum fyrirtækja og hins opinbera skaltu kortleggja hvert þrep á skjalfesta mikilvægiseinkunn svo endurskoðandi sjái að peningarnir fylgja áhættunni og svo enginn þurfi að verja útgjöldin í fyrsta sinn meðan á rekstrarrofi stendur.

## Sjónarhorn eftir geirum

**Sprotafyrirtæki.** Þú getur ekki spáð hvort opnun skilar fimmtíu nýskráningum eða fimmtíu þúsund, svo keyptu stigvöxt frekar en að smíða hann: keyrðu ástandslausar þjónustur á bak við stýrðan álagsdreifi og láttu vettvanginn stigstilla sjálfvirkt á beiðnahlutfalli. Settu eina hóflega afkastafjárhagsáætlun og veldu stýrðar gagnageymslur svo toppur þvingi ekki fram endurhönnun klukkan 2 að nóttu. Slepptu fjölsvæða hamfaraendurheimt og glundroðaáætlunum í bili. Haltu prófuðum afritum og eyddu takmarkaðri verkfræðiathygli í vöruna, ekki í offramleiðslu sem umferð þín réttlætir ekki enn.

**Lítið fyrirtæki.** Án áreiðanleikasérfræðings og með þröngt fjárhagsáætlun hallast kaupa-eða-smíða valið eindregið að kaupum: stýrður vettvangur eða þjónustulaus stakkur gerir stigvöxt og yfirtöku að verkefni veitandans, og eitt vel rekið svæði er venjulega nóg. Rammaðu seiglu sem fáein áþreifanleg loforð sem þú getur staðið við, eins og næturafrit sem þú hefur í raun endurheimt úr einu sinni og raunhæfan endurheimtarglugga sem þú hefur komið á framfæri við viðskiptavini. Forðastu að borga fyrir virk-virk eða samfellda álagsprófun sem þú hefur hvorki umferð né starfsfólk til að réttlæta.

**Stórfyrirtæki.** Vandinn er samræmi yfir mörg teymi: staðlaðu afkastafjárhagsáætlanir framfylgdar í CI, sameiginlegt bókasafn seigluminstra (tímamörk, rofar, skilrúm) og skjalfest offramleiðsluþrep fyrir hvert kerfi tengt mikilvægi þess. Taktu frá virk-virk fjölsvæða fyrir fyrsta flokks þjónustur, keyrðu glundroðaverkfræðiáætlun með handriðum og leikdögum í framleiðslu og líttu á getuáætlun fyrir þekktar bylgjur sem tímasettan aga frekar en eftirþanka. Stýrðu RTO og RPO miðlægt svo hvert mikilvægt kerfi hafi eigin, prófuð markmið sem endurskoðandi getur staðfest.

**Hið opinbera.** Álag er oft lögbundið í tíma og aðgengisskyldur eru lögbundnar, svo getuáætlun getur ekki treyst á sjálfvirka stigstillingu sem bregst við á staðnum: spáðu fyrir um frestabylgjuna, forútvegaðu og álagsprófaðu vel yfir spá. Innkaup ættu að tilgreina RTO, RPO og áætlun um æfðar yfirtökur sem samningskröfur, ekki loforð söluaðila, og ættu að forðast bindingu við eitt svæði fyrir mikilvægar þjónustur. Ákveddu fyrirfram hvaða leið er lagalega nauðsynleg (að skila framtali, að sækja um bætur) svo skerðing losi stöðumælaborð og uppflettingar fyrst, og vertu gagnsær gagnvart almenningi um rekstrarrof og endurheimt frekar en að vona að enginn taki eftir.

## Dæmi

**Sprotafyrirtæki.** Lítið sprotafyrirtæki sem opnar á Product Hunt getur ekki spáð hvort það fær fimmtíu nýskráningar eða fimmtíu þúsund, svo það heldur þjónustum sínum ástandslausum á bak við stýrðan álagsdreifi og lætur vettvanginn stigstilla sjálfvirkt á beiðnahlutfalli. Það setur eina hóflega afkastafjárhagsáætlun (síður svara á innan við 300ms við 95. hundraðshluta) og velur stýrðan gagnagrunn svo umferðartoppur þvingi ekki fram endurhönnun klukkan 2 að nóttu. Þegar opnunardagsbylgjan kemur hægist síðan lítillega á frekar en að falla og teymið eyðir deginum í að tala við nýja notendur í stað þess að berjast við rekstrarrof.

**Stórfyrirtæki.** Streymisfyrirtæki rekur ástandslausar þjónustur yfir mörg svæði á bak við hnattræna álagsdreifingu, með sjálfvirkri stigstillingu á beiðnahlutfalli til að fylgja daglegu háannatímabylgjunni. Afkastafjárhagsáætlanir hliða hverja útgáfu á p99 ræsitöf. Við svæðisbilun færist umferð sjálfkrafa til heilbrigðra svæða og ónauðsynlegir eiginleikar (sérsniðin forsíðumynd, endurnýjun meðmæla) skerðast fyrst til að vernda afspilun. Fyrirtækið keyrir samfelldar glundroðatilraunir í framleiðslu, drepur reglulega tilvik og sprautar inn töf, svo raunverulegar bilanir eru óaðgreinanlegar frá æfingum og valda engu rekstrarrofi sem viðskiptavinir sjá.

**Hið opinbera.** Skattayfirvald veit að skilakerfi þess stendur frammi fyrir gríðarlegri, lögbundið fastri frestabylgju á hverju ári. Í stað þess að treysta á að sjálfvirk stigstilling bregðist við á staðnum spáir það fyrir um toppálag út frá fyrri árum, forútvegar getu vikum fyrirfram og álagsprófar að 150% af spá. Arkitektúrinn er ástandslaus á bak við álagsdreifa með heita biðstöðu á öðru svæði. RTO og RPO eru sett með stefnu (ekki meira en 15 mínútna niðurtími og nánast ekkert gagnatap fyrir innsend framtöl) og yfirtaka er æfð ársfjórðungslega. Undir ofurálagi losna ónauðsynlegir eiginleikar (stöðumælaborð, söguleg uppfletting) fyrst svo að skil framtala, lagalega nauðsynlega leiðin, haldist aðgengileg.

## Viðskiptarök: hvatar, ávöxtun fjárfestingar og heildarkostnaður

Stigvöxtur, afköst og seigla eru klassísk dæmi þar sem kostnaður bilunar er langt umfram kostnað forvarna. En forvörnin er sýnileg í fjárhagsáætluninni og bilunin er aðeins möguleg, og þess vegna eru þau langvarandi vanfjármögnuð þar til fyrsta hamfarir verða. Upptökukostnaðurinn er raunverulegur: offramleiðsluinnviðir, fjölsvæða geta, álagsprófunar- og glundroðaverkfæri og verkfræðitími til að byggja ástandsleysi og seigluminstur. Kostnaðurinn við að fjárfesta *ekki* er áberandi rekstrarrof á annatíma: tapaðar tekjur á mínútu fyrir verslun, vanrækt lögbundnar skyldur og opinber rannsókn fyrir hið opinbera, sektir samkvæmt [þjónustustigssamningum](https://en.wikipedia.org/wiki/Service-level_agreement) (SLA) og varanlegur mannorðsskaði.

Rammaðu rökin við forystu með tölum sem reksturinn skilur þegar. Áætlaðu kostnað einnar klukkustundar niðurtíma á topp (tapaðar færslur, sektir, úrbætur, mannorð) og berðu saman við árlegan kostnað offramleiðslunnar og prófana sem koma í veg fyrir það. Fyrir mikilvæg kerfi er forvörnin nánast alltaf brot af einu stóru atviki. Tengdu RTO og RPO við skýra peninga: hve mikið af tekjum eða færslum á klukkustund niðurtíma og hve mikið gagnatap er lagalega eða viðskiptalega þolanlegt. Settu fram afköst sem tekju- og ánægjuvogarstöng, þar sem hraðari kerfi umbreyta betur og kosta minna á færslu, og settu fram seiglu sem tryggingu þar sem iðgjaldið er lítið miðað við tapið sem hún nær yfir. Sterkustu rökin eru að þessir eiginleikar eru ódýrir að hanna inn og stórskaðlegir að bæta við eftir rekstrarrofið sem neyðir málið fram.

## Andmynstur og gildrur

- **Klístraðar setur og ástand í tilviki.** Að geyma setuástand á netþjóninum, sem kemur í veg fyrir frjálsa lárétta stigvöxt og örugga skiptingu tilvika.
- **Sjálfvirk stigstilling sem getuáætlun.** Að gera ráð fyrir að sjálfvirk stigstilling gleypi þekkta stökkbylgju sem hún er of hæg til að bregðast við.
- **Keyrt heitt án rýmis.** Rekstur á nánast 100% nýtingu sem skilur ekkert eftir til að gleypa toppa eða bilanir.
- **Fínstilling án sniðgreiningar.** Að stilla kóða sem er ekki flöskuhálsinn á meðan sá raunverulegi er ósnertur.
- **Hunsun halans.** Að skýra frá meðaltöf á meðan p99-notendur þjást. Meðaltöl fela sársaukann í stórum stíl.
- **Óprófuð hamfaraendurheimt.** Hamfaraáætlun og afrit sem aldrei hafa verið æfð og munu bregðast þegar þeirra er þörf.
- **Einstakir bilunarpunktar.** Einn álagsdreifir, ein gagnagrunnsaðalnóða, eitt svæði: íhlutur án offramleiðslu sem tekur allt niður.
- **Glundroðaverkfræði án handriða.** Að sprauta inn bilunum án sprengjusvæðisstýringar eða rofa til að hætta við, sem veldur einmitt rekstrarrofinu sem átti að koma í veg fyrir.

## Þroskalíkan

- **Stig 1: Upphaf.** Ad hoc og viðbragðsdrifið. Eitt tilvik eða lóðrétt stigvaxið, með ástand haldið á netþjóninum. Engin álagsprófun, engar afkastafjárhagsáætlanir og engin hamfaraendurheimt umfram stöku afrit sem enginn hefur endurheimt úr. Hver íhlutabilun veldur fullu rekstrarrofi og stigvaxtarvandi uppgötvast í framleiðslu.
- **Stig 2: Þróun.** Grunnvinnubrögð birtast en eru mismunandi frá teymi til teymis. Sumar þjónustur eru lárétt stigvaxnar og ástandslausar á bak við álagsdreifi, með grunn sjálfvirkri stigstillingu á nokkrum þeirra. Álagsprófun gerist fyrir stórar opnanir en ekki reglulega, og afrit eru til á meðan hamfaraendurheimt er skjalfest en sjaldan æfð. Það sem eitt teymi gerir vel hefur annað ekki byrjað á.
- **Stig 3: Stöðlun.** Vinnubrögð eru skjalfest og framfylgt um alla skipulagsheildina. Getu er skipulögð fyrir þekktar bylgjur með rými, afkastafjárhagsáætlunum er framfylgt í CI svo afturfarir fella smíðina og seigluminstur (tímamörk, afmarkaðar endurtekningar, rofar, skilrúm) auk mjúkrar skerðingar eru sjálfgefin. RTO og RPO eru skilgreind fyrir hvert kerfi, offramleiðsluþrep eru úthlutuð eftir mikilvægi og hamfaraendurheimtaryfirtaka er prófuð reglulega yfir teymi.
- **Stig 4: Stjórnun.** Eiginleikarnir eru mældir og stýrðir gegn grunnlínum. Teymi rekja p95- og p99-töf, villufjárhagsáætlanir og nýtingu og rými gegn spá og gefa viðvörun um brot frekar en að uppgötva þau við opnun. Prófaðir yfirtökutímar eru bornir saman við markmiðs-RTO og RPO, mörk skerðingar og álagslosunar eru staðfest með mælikvörðum og ákvarðanir um útgáfur og getu eru knúnar af gögnum. Þar sem tölur reka frá grunnlínu er bilið sýnilegt og í eigu einhvers frekar en falið á bak við meðaltöl.
- **Stig 5: Samhæfing.** Stigvöxtur, afköst og seigla eru stöðugt bætt og samþætt um alla skipulagsheildina. Virk-virk fjölsvæða er notuð hvar sem mikilvægi réttlætir, glundroðaverkfræði keyrir samfellt þar á meðal leikdagar í framleiðslu og getuspá nærir beint í áætlanagerð og innkaup. Seigla er staðfest samfellt, endurheimtarmarkmið eru stöðugt uppfyllt og sönnuð og arkitektúrinn aðlagast eftir því sem álagsmynstur og áhættumynd breytast, tengd órofa rekstri og áhættuáætlun.

## Hugmyndir til umræðu

1. Hverjar af þjónustum þínum geyma enn ástand í tilvikinu og hvað kemur í veg fyrir að þú gerir þær ástandslausar?
2. Fyrir mikilvægasta kerfið þitt, hver eru RTO og RPO, hver setti þau og hvenær sannaðir þú síðast að þú getir staðið við þau?
3. Verndar sjálfvirk stigstilling þig í raun gegn stærstu þekktu bylgju þinni, eða treystirðu á hana til að gera eitthvað sem hún getur ekki?
4. Hvar er eftirstandandi einstakur bilunarpunktur þinn og hver er áætlunin um að fjarlægja hann?
5. Ertu að mæla og setja fjárhagsáætlun fyrir p99-töf, eða felurðu þig á bak við meðaltöl?
6. Hefurðu nokkurn tíma vísvitandi fellt íhlut í framleiðslu? Ef ekki, hvernig veistu að seigla þín virkar?

## Helstu atriði

- Greindu milli afkasta, stigvaxtar og seiglu. Stórt kerfi þarf alla þrjá, hannaða inn frá byrjun.
- Lárétt stigvöxtur og ástandslausar þjónustur eru grunnur stigvaxtar, aðgengis og öruggrar uppsetningar.
- Sameinaðu sjálfvirka stigstillingu við raunverulega getuáætlun og rými fyrir fyrirsjáanlegar, rekstrarkritískar bylgjur.
- Knúðu afköst með sniðgreiningu og álagsprófun gegn skýrum fjárhagsáætlunum og einbeittu þér að mikilvægu leiðinni og halanum.
- Smíðaðu seiglu með tímamörkum, rofum, skilrúmum, mjúkri skerðingu og offramleiðslu og staðfestu hana síðan með glundroðaverkfræði.
- Settu RTO og RPO sem viðskiptaákvarðanir, verkfræddu hamfaraendurheimt eftir mikilvægi hvers kerfis og prófaðu yfirtöku reglulega.

## Heimildir og frekari lestur

- Martin Kleppmann, *Designing Data-Intensive Applications*
- Michael Nygard, *Release It!: Design and Deploy Production-Ready Software*
- Betsy Beyer et al. (Google), *Site Reliability Engineering* and *The Site Reliability Workbook*
- Casey Rosenthal and Nora Jones, *Chaos Engineering*
- Brendan Gregg, *Systems Performance: Enterprise and the Cloud*
- John Allspaw, *The Art of Capacity Planning*
- Ilya Grigorik, *High Performance Browser Networking*
- Nassim Nicholas Taleb, *Antifragile*
