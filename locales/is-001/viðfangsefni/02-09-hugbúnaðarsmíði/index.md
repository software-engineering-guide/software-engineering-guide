# 2.9 Hugbúnaðarsmíði

## Yfirlit og tilgangur

[Hugbúnaðarsmíði](https://en.wikipedia.org/wiki/Software_construction) er þar sem hönnun verður að keyrandi kóða. Þetta er nákvæma vinnan við kóðun, sannprófun, [einingaprófanir](https://en.wikipedia.org/wiki/Unit_testing), [samþættingarprófanir](https://en.wikipedia.org/wiki/Integration_testing) og [villuleit](https://en.wikipedia.org/wiki/Debugging). Leiðarvísir [Software Engineering Body of Knowledge](https://en.wikipedia.org/wiki/Software_Engineering_Body_of_Knowledge) (SWEBOK) lítur á smíði sem sérstakt þekkingarsvið, og með góðri ástæðu: hér gerist mest af daglegri vinnu þinni. Valin sem þú tekur lína fyrir línu (hvernig þú heldur flækju í skefjum, hvernig þú meðhöndlar villur, hve læsilegt þú skilur hlutina eftir) ákvarða hvort kerfi geti verið skilið, breytt og treyst um ókomin ár.

Í stóru teymi er smíði hópátak, ekki einleikur. Hundruð verkfræðinga skrifa inn í sameiginlegan kóðagrunn sem mun lifa starfstíma nokkurs eins í teyminu. Svo viðmiðið er ekki „virkar það á vélinni minni í dag“. Það er „getur ókunnugur breytt þessu örugglega eftir fimm ár“. Smíði tengist upp á við við kröfur (kafli 2.8) og hönnun (kafli 2.2), sem segja þér hvað á að smíða og lögun þess. Hún tengist til hliðar við kóðunarstaðla (kafli 2.1), prófanir (kafli 2.4) og kóðarýni (kafli 2.5), sem móta hvernig verkið er tjáð, sannreynt og skoðað. Góð smíði breytir traustri hönnun í viðhaldanlega eign. Léleg smíði breytir jafnvel góðri hönnun í skuldbindingu.

Í fyrirtækja- og opinberu umhverfi hefur smíði aukið vægi. Þessi kerfi eru langlíf, mjög eftirlitsskyld og oft öryggis- eða borgarakritísk. [Varnarkóðun](https://en.wikipedia.org/wiki/Defensive_programming), aguð villumeðhöndlun og kóði sem er augljóslega réttur eru ekki lúxus hér. Þau eru kröfur um tryggingu, úttekt og samfellu yfir áratugi og starfsmannaveltu. Markmiðið er kóði sem miðlar ásetningi sínum, stendur gegn bilun og er hægt að sannprófa. Kóði sem bara keyrir er ekki nóg.

## Meginreglur

- Lágmarkaðu flækju umfram allt. Helsti óvinur stórrar smíði er kóði sem enginn getur skilið til fulls.
- Sjáðu breytingar fyrir. Smíðaðu svo líklegar framtíðarbreytingar séu staðbundnar og ódýrar.
- Smíðaðu fyrir sannprófun. Skrifaðu kóða þar sem réttleiki er auðveldur að athuga með prófum, rýni og rökhugsun.
- Endurnýttu af ásetningi. Byggðu á traustum núverandi íhlutum frekar en að finna upp aftur, en forðastu tengsl við rangar ágripanir.
- Fylgdu stöðlum. Samræmi yfir kóðagrunn dregur úr vitrænum kostnaði hverrar framtíðarbreytingar.
- Meðhöndlaðu villur og ógild ástönd skýrt. Gerðu bilunarhætti sýnilega frekar en hljóða.
- Haltu kóða læsilegum. Smíði er samskipti við framtíðarumsjónarmenn fyrst og þýðandann í öðru lagi.

## Ráðleggingar

### Lágmarkaðu flækju sem aðalagann

Gerðu það að meginmarkmiði þínu að draga úr flækju, bæði nauðsynlegri og tilviljanakenndri. Skrifaðu litlar, einnar-tilgangs aðgerðir og einingar. Kjóstu skýr nöfn fram yfir snjöll brögð. Haltu hreiðrun grunnri og stýriflæði línulegu. Staðfærðu ákvarðanir svo að skilja eitt stykki af kóða neyði þig ekki til að halda öllu kerfinu í höfðinu. Flækja er það sem gerir stóra kóðagrunna hæga í breytingum og hættulega að snerta, svo vegðu hvert val eftir því hvort það bætir við flækju eða fjarlægir hana. Beittu hönnunarreglunum í kafla 2.2 líka í smáum mælikvarða: mikil samloðun, lág tengsl og skýr [aðskilnaður áhyggjuefna](https://en.wikipedia.org/wiki/Separation_of_concerns) skiptir jafn miklu máli í einni aðgerð og í arkitektúr.

### Smíðaðu fyrir breytingar og sannprófun

Hugsaðu fram í tímann um breytingarnar sem líklegast koma (nýjar viðskiptareglur, nýjar samþættingar, nýjar reglugerðir) og einangraðu þær á bak við stöðug viðmót svo breyting haldist staðbundin. Á sama tíma skaltu skrifa kóða sem er auðvelt að sannprófa: [hreinar aðgerðir](https://en.wikipedia.org/wiki/Pure_function) (sömu inntök gefa alltaf sama úttak, án hliðaráhrifa) þar sem þú getur, lágmarks falið ástand og ósjálfstæði gert skýrt svo próf geti skipt því út. Kóði sem er erfitt að prófa er venjulega kóði sem er erfitt að skilja og breyta. Prófanleiki (kafli 2.4) er hönnunarmerki, ekki bara gæðaprófunaráhyggjuefni.

### Endurnýttu af ásetningi og staðlaðu

Náðu í vel viðhaldin, traust bókasöfn og innri íhluti áður en þú endurskrifar grunnrökfræði og notaðu þau gegnum skýr viðmót (kafli 2.3). Smíðaðu endurnýtanlega íhluti aðeins þegar raunverulegt annað notkunartilvik er til, því að alhæfa of snemma er eigin tegund flækju. Beittu kóðunarstöðlum og stíl skipulagsheildarinnar (kafli 2.1) samræmt, helst framfylgt af sjálfvirkum sniðmótum og [lint-tólum](https://en.wikipedia.org/wiki/Lint_(software)), svo allur kóðagrunnurinn lesist eins og einn vandvirkur höfundur hefði skrifað hann.

### Iðkaðu varnarforritun með dómgreind

Staðfestu inntök á traustmörkum (ytri beiðnir, skráa- og netinntak/úttak, notendainntak) og líttu á öll gögn sem fara yfir þau mörk sem fjandsamleg þar til annað sannast. Innan vel prófaðrar einingar skaltu samt ekki kæfa hverja línu í óþörfum athugunum sem fela rökfræðina og bæla niður raunverulegar bilanir. Reglan er einföld: verðu á mörkunum, treystu innan þeirra. Notaðu [staðhæfingar](https://en.wikipedia.org/wiki/Assertion_(software_development)) til að skjalfesta og framfylgja fastayrðingum sem ættu aldrei að vera rangar í réttu forriti. Notaðu [undantekningar](https://en.wikipedia.org/wiki/Exception_handling) og villumeðhöndlun fyrir skilyrði sem geta löglega gerst í keyrslu. Haltu þessu tvennu aðskildu: staðhæfingar gæta forsendna forritara, villumeðhöndlun stýrir væntanlegri bilun.

### Meðhöndlaðu villur skýrt og bilaðu örugglega

Fyrir hverja villu skaltu ákveða af ásetningi hvað á að gera: jafna sig, reyna aftur, bera áfram eða bila hratt. Gleyptu aldrei undantekningu hljóðlega né hunsaðu skilað villugildi. Bæld bilun kemur til baka sem dularfullur galli síðar. Haltu samhengi í villuskilaboðum og skrám svo hægt sé að greina bilanir. Í öryggis- og borgarakritískum kerfum skaltu bila í öruggt, þekkt ástand frekar en halda áfram í spilltu. Gefðu villuleiðinni jafn mikla hugsun og gleðileiðinni, því í framleiðslu er villuleiðin þar sem traust vinnst eða tapast.

### Byggðu gæði inn við smíði

Gæði eru byggð inn, ekki skoðuð inn eftirá. Skrifaðu einingapróf samhliða kóðanum, keyrðu [kyrrstæða greiningu](https://en.wikipedia.org/wiki/Static_program_analysis) og lint-tól stöðugt og haltu aðgerðum nógu litlum til að rökræða um. Notaðu sjálfskýrandi nöfn og uppbyggingu svo athugasemdir þínar geti útskýrt hvers vegna, ekki hvað. [Endurbyggðu](https://en.wikipedia.org/wiki/Code_refactoring) jafnóðum til að halda kóðanum íbúðarhæfum. Kóðarýni (kafli 2.5) er mannlega bakstoðin, en mestöll gæðin þurfa að vera til staðar áður en rýni hefst.

### Veldu og staðlaðu smíðaverkfæri

Staðlaðu verkfærakeðjuna (þýðendur, smíðakerfi, sniðmótara, lint-tól, kyrrstæða greinendur, villuleitartól, ósjálfstæðisstjóra og IDE-stillingar) svo hver verkfræðingur vinni í samræmdu, endurgeranlegu umhverfi. Tengdu þessi verkfæri inn í leiðsluna svo gæðaathuganir séu ekki valkvæðar. Taktu upp gervigreindaraðstoðuð kóðunarverkfæri af ásetningi og líttu á úttak þeirra sem drög sem verða að standast sömu staðla, rýni og próf og hver annar kóði.

## Málamiðlanir: kostir og gallar

| Vinnubrögð | Kostir | Gallar |
|---|---|---|
| Ágeng flækjuminnkun | Læsilegt, breytanlegt, lágt gallahlutfall | Getur fundist hægt, hætta á ofágripun ef rangt beitt |
| Umfangsmiklar varnarathuganir | Grípur slæm ástönd snemma, traust mörk | Ringulreið í rökfræði, getur falið raunverulega galla ef ofgert |
| Staðhæfingar fyrir fastayrðingar | Skjalfestir og framfylgir forsendum | Slökkt á í sumum framleiðslusmíðum, ekki villumeðhöndlun |
| Mikil endurnýting bókasafna | Minni kóði til að eiga, hraðari afhending | Ósjálfstæðisáhætta, tengsl, aðfangakeðjuútsetning |
| Strangir staðlar og lint | Einsleitur, núningslítill kóðagrunnur | Uppsetning fyrirfram, getur fundist stíft einstaklingum |
| Smíði fyrir prófanleika | Sannprófanlegur, breytanlegur kóði | Getur bætt við millilagi sem sumir sjá sem helgisið |

Meginmálamiðlun smíðar er skammtímahraði gegn langtíma breytanleika. Að skera horn (sleppa villumeðhöndlun, umbera flækju, hunsa staðla) finnst hraðara á stundinni, og er næstum alltaf dýrara yfir líftíma kerfisins. Andstæða bilunin er ofhönnun: of mikil vörn, ágiskunarleg ágripun og almennni sem enginn þarf. Fær smíði lifir í miðjunni: eins einföld og mögulegt er, eins varnarmikil og mörkin krefjast, og ekki meira.

## Spurningar til að ræða með teyminu

1. **Hver er sameiginleg, áþreifanleg skilgreining okkar á „of flókið“ og hvar framfylgjum við henni fyrir sameiningu?** „Lágmarkaðu flækju“ er kjarnaagi smíðar, en sem slagorð tapar það hverri deilu gegn fresti. Í stóru teymi þar sem hundruð manna skrifa inn í einn kóðagrunn þarf flækja að vera mælanleg, svo komdu þér saman um merki sem þú munt í raun bregðast við: lengd aðgerða, hreiðrunardýpt, hringflækju og fjölda hluta sem lesandi þarf að halda í höfðinu til að skilja eina breytingu. Komdu með versta brotamanninn þinn á fundinn og spurðu hvort núverandi rýni þín hefði gripið hann. Svarið ætti að verða leiðsluhlið eða rýnigátlistaatriði, því þröskuldur framfylgt af verkfæri er meira virði en regla framfylgt af viljastyrk, og hann sparar næsta starfsmanni þínum hæga uppsöfnun kóða sem enginn getur snert örugglega.

2. **Haga villuleiðir okkar sér í framleiðslu eins og við hönnuðum þær, og hvenær æfðum við eina af ásetningi síðast?** Smíðaráðgjöfin segir gefðu villuleiðinni jafn mikla hugsun og gleðileiðinni, en villuleiðin er venjulega minnst prófaði kóðinn sem þú átt, og í borgarakritísku eða öryggiskritísku kerfi er hún þar sem traust vinnst eða tapast. Bæld undantekning eða hunsaður skilakóði verður dularfullur galli vikum síðar, og „bila í öruggt ástand“ er loforð sem þú getur ekki staðið við ef þú hefur aldrei horft á það gerast. Komdu með atvikasögu þína: hve mörg fyrri rekstrarrof rekja sig til gleypts villuskilaboðs eða óprófaðrar endurheimtarleiðar? Aðgerðin er að prófa bilun af ásetningi (sprauta inn hafnaða kortinu, tímamörkunum, ranghönnuðu inntakinu) og krefjast þess að hver villa sé meðhöndluð, skráð með samhengi eða borin áfram, aldrei hljóðlega felld.

3. **Hvaða hlutar kóðagrunnsins okkar eru erfiðir að prófa og hvað segir sá erfiðleiki okkur um hönnunina?** Kóði sem stendur gegn prófun felur næstum alltaf ástand, tengist röngum ósjálfstæðum eða gerir of mikið, svo prófanleiki er hönnunarmerki, ekki gæðaprófunareftiráhugsun. Á langlífu fyrirtækjakerfi skiptir þetta máli því einingarnar sem eru sársaukafullar að prófa í dag eru þær sem ókunnugur mun óttast að breyta eftir fimm ár. Komdu með flokkinn eða þjónustuna sem teymið þitt óttast að skrifa próf fyrir og spurðu hvers vegna: er ástandið falið, er ómögulegt að skipta út ósjálfstæðum, gerir aðgerðin þrjú verk? Svarið ætti að knýja endurbyggingu í átt að hreinum aðgerðum, skýrum ósjálfstæðum og litlum einnar-tilgangs einingum, því að gera kóðann sannprófanlegan er sama vinna og að gera hann skiljanlegan og ódýran í breytingum.

4. **Hvenær endurnýtum við ytra bókasafn á móti því að smíða getuna sjálf og hver á aðfangakeðjuáhættuna sem við tökum á okkur?** Að ná í traust bókasafn er hraðara en að finna upp grunnrökfræði aftur, en hvert ósjálfstæði sem þú bætir við er kóði sem þú stjórnar ekki, getur ekki auðveldlega úttektað og verður að plástra daginn sem hann er í hættu. Í stóru teymi er hættan sú að hundrað verkfræðingar dragi hver sín eigin yfirfærðu ósjálfstæði inn þar til enginn getur sagt hvað kóðagrunnurinn keyrir í raun. Komdu með ósjálfstæðisskrána þína og spurðu þriggja áþreifanlegra hluta: hve mörg bókasöfn eru óviðhaldin, hve mörg bera þekkta veikleika og hve mörg vefja rökfræði nógu einfalda til að eiga alveg. Sjónarmiðið á móti er raunverulegt, því að skrifa eigin dulritun eða dagsetningarmeðhöndlun er næstum alltaf verra en margreynt bókasafn, svo markmiðið er yfirveguð endurnýtingarstefna frekar en altæk forðun. Í fyrirtækja- og opinberu umhverfi skaltu bæta við innkaupa- og leyfisreglunarhorninu, því óskoðað ósjálfstæði getur borið leyfi ósamrýmanlegt skyldum þínum eða herkomu sem enginn endurskoðandi samþykkir.

5. **Hvernig höldum við gervigreindarmynduðum kóða við sömu smíðastaðla og handskrifuðum kóða og getum við greint þau í sundur þegar það skiptir máli?** Gervigreindar kóðunaraðstoðarmenn framleiða sennileg drög hratt og freistingin er að líta á úttak þeirra sem fullbúið því það þýðist og lítur málvenjulega út. Regla kaflans er að myndaður kóði standist sömu rýni, próf og staðla og allt annað, og stórt teymi verður að gera þá reglu framkvæmanlega en ekki aðeins væntingu. Komdu með dæmi um gervigreindaraðstoðaðar breytingar sem voru afhentar nýlega og spurðu hvort hver bar próf, stóðst kyrrstæða greiningu og var raunverulega skilin af manneskjunni sem lagði hana fram, eða var veifuð í gegn á trausti. Þrýstingurinn á móti er hraði, því þessir aðstoðarmenn eru raunverulega afkastamiklir og að hægja á hverri tillögu í skrið kastar ávinningnum burt. Í eftirlitsskyldu og opinberu samhengi skaltu bæta við herkomu- og ábyrgðarhorninu, því þú gætir þurft að votta hver ber ábyrgð á kóðalínu og hvort mynduð brot beri leyfis- eða höfundarréttarspurningu sem þú getur ekki svarað.

6. **Er smíðaverkfærakeðja okkar í raun staðluð og framfylgt í leiðslunni, eða vinna einstaklingar enn í ósamrýmanlegum uppsetningum?** Sameiginleg verkfærakeðja sniðmótara, lint-tóls, kyrrstæðs greinanda, smíðakerfis og ósjálfstæðisstjóra leyfir verkfræðingi að færast af öryggi yfir ókunnar þjónustur, því kóðinn lesist sem ein rödd og athuganirnar eru eins alls staðar. Þegar hún rekur finnur hvert teymi upp eigin stillingu, rýnitími fer í að deila um stíl og gallar sem greinandi eins teymis hefði gripið renna í gegn hjá öðru. Komdu með listann yfir hugbúnaðarsöfn sem keyra ekki stöðluðu athuganirnar á hverju commit og spurðu hvers vegna hvert valdi að víkja. Spennan er sú að ein skyldubundin uppsetning getur fundist stíf teymum með raunverulega ólíkar þarfir, svo ákveddu hvar einsleitni er núningsins virði og hvar skjalfest undanþága er í lagi. Fyrir stórt fyrirtæki eða opinbera aðila skaltu tengja þetta við endurgeranleika og úttekt, því smíði sem þú getur ekki endurskapað bæti fyrir bæti úr stýrðri verkfærakeðju er ein sem þú getur ekki varið fyrir matsaðila árum síðar.

## Sjónarhorn eftir geirum

**Sprotafyrirtæki.** Hraði vinnur, svo settu sameiginlegan sniðmótara og lint-tól upp fyrsta daginn, staðfestu inntök á einu ytra mörkunum þínum og haltu innri kóðanum hreinum frekar en varnarmiklum á hverri línu. Slepptu ágiskunarlegri ágripun og þungu ferli: með tvo eða þrjá verkfræðinga heldur allt teymið kóðagrunninum í höfðinu, og raunverulega áhættan er flækja sem lifir þetta sameiginlega minni. Hallaðu þér að traustum bókasöfnum fyrir allt grundvallarlegt svo þú skrifir sem minnst af kóða sem þú getur átt vel.

**Lítið fyrirtæki.** Án sérstaks smíðaverkfræðings og með þröngt fjárhagsáætlun skaltu kjósa venjur sem núverandi verkfærin þín framfylgja ókeypis: sniðmótari og lint-tól sem fylgja tungumálinu, skynsamleg sjálfgefin gildi og lítið safn reglna sem allir muna. Keyptu eða tak upp vel viðhaldin bókasöfn frekar en að smíða innviði sem þú getur ekki mannað til viðhalds. Eyddu takmörkuðum aga þínum í tvennt sem skaðar mest þegar vanrækt: að staðfesta inntak á mörkunum og gleypa aldrei villu hljóðlega.

**Stórfyrirtæki.** Með hundruð verkfræðinga sem skrifa inn í sameiginlegan kóða er forgangur einsleitni og framfylgd: staðlað verkfærakeðja tengd leiðslunni, hlið kyrrstæðrar greiningar og mörkastaðfestingarreglur beitt alls staðar svo fólk færist af öryggi milli þjónusta. Stýrðu ósjálfstæðis- og aðfangakeðjuáhættu sem stýrðu ferli frekar en spuna hvers teymis og notaðu staðhæfingar til að kóða lénsfastayrðingar sem verða að halda yfir hvert teymi. Líttu á smíðastaðla sem undirlagið sem heldur kóðagrunni íbúðarhæfum yfir áratugi og starfsmannaveltu.

**Hið opinbera.** Langlíf, borgarakritísk kerfi gera agaða smíði að spurningu um tryggingu og ábyrgð. Einangraðu sveiflukenndar reglur eins og löggjöf á bak við stöðug viðmót svo breyting haldist staðbundin og rekjanleg til krafna, bilaðu í örugg, þekkt ástönd frekar en að halda áfram í spilltu og afhentu hverja einingu með prófum sem tvöfaldast sem úttektarsönnun. Innkaupa- og gagnsæisskyldur þýða að verkfærakeðja þín, ósjálfstæði og villumeðhöndlun verða að vera skjalfest nógu vel til að ríkisstarfsmaður sem kemur árum síðar, eða ytri endurskoðandi, geti sannreynt að kóðinn sé réttur.

## Dæmi

**Sprotafyrirtæki.** Þriggja verkfræðinga sprotafyrirtæki setur upp sameiginlegan sniðmótara og lint-tól fyrsta daginn og keyrir þau á hverju commit, svo kóðagrunnurinn lesist sem ein rödd jafnvel þegar þeir bæta við verktökum. Þeir staðfesta inntök á API-mörkunum og líta á allt að utan sem fjandsamlegt, en halda innri rökfræðinni hreinni í stað þess að kæfa hana í óþörfum athugunum. Þegar greiðsluvefkrókur byrjar að bila er lagfæringin fljót því engin undantekning var nokkurn tíma gleypt hljóðlega og villuskilaboðin bera nægt samhengi til að benda beint á orsökina. Öll uppsetningin tók eftirmiðdag og sparaði þeim hæga uppsöfnun flækju sem hefði gert fyrstu viku næsta starfsmanns ömurlega.

**Stórfyrirtæki.** Alþjóðlegt greiðslufyrirtæki framfylgir sameiginlegri verkfærakeðju yfir hundruð verkfræðinga: sjálfvirkt snið og lint á hverju commit, hlið kyrrstæðrar greiningar í leiðslunni og reglu um að öll ytri inntök séu staðfest á þjónustumörkum. Lénsrökfræði notar staðhæfingar til að framfylgja fastayrðingum eins og „færsla í höfuðbók jafnast alltaf“, á meðan keyrsluskilyrði eins og hafnað kort eru meðhöndluð sem skýrar, skráðar niðurstöður. Því staðlar eru einsleitir og villur eru aldrei hljóðlega gleyptar færast verkfræðingar af öryggi yfir ókunnar þjónustur og framleiðsluatvik má greina beint úr skránum.

**Hið opinbera.** Landsbundin skattstofnun smíðar langlíft álagningarkerfi sem er ætlað að vera í rekstri í áratugi undir breytilegri löggjöf. Smíðin einangrar hverja skattareglu á bak við stöðugt viðmót, svo árlegar löggjafarbreytingar haldast staðbundnar og rekjanlegar til krafna (kafli 2.8). Varnarstaðfesting gætir hvers borgarasnúins inntaks. Villuleiðir bila í öruggt ástand sem gefur aldrei hljóðlega út ranga álagningu. Hver eining fylgir með einingaprófum sem úttektarsönnun. Því smíðin er stöðluð og vel skjalfest geta nýir ríkisstarfsmenn viðhaldið kóða skrifuðum af forverum sem fóru fyrir löngu.

## Viðskiptarök: hvatar, ávöxtun fjárfestingar og heildarkostnaður

Ávöxtun agaðrar smíðar er varanleg geta til að breyta hugbúnaði ódýrt og örugglega, og þar er mest af heildareignarkostnaði kerfis ákveðið. Rannsóknir á hugbúnaðarhagfræði sýna stöðugt að mestur líftímakostnaður kerfis er viðhald, og viðhaldskostnaði ræður hve skiljanlegur og breytanlegur kóðinn er. Að lágmarka flækju, meðhöndla villur skýrt og fylgja stöðlum lækkar beint kostnað hverrar framtíðarbreytingar og hvers framleiðsluatviks.

Upptökukostnaðurinn er hóflegur og aðallega fyrirfram: setja staðlana, tengja lint-tól og greinendur og byggja upp venjuna að skrifa sannprófanlegan, varnarmikinn kóða. Kostnaður vanrækslu safnast hins vegar upp. Flækja safnast í kóða sem er hægur að breyta og áhættusamur að snerta. Hljóðar villur breytast í dýr framleiðsluatvik. Ósamræmdur stíll margfaldar fyrirhöfn hverrar rýni og hverrar móttöku. Til að færa rök við forystu skaltu tengja smíðagæði við bilanahlutfall breytinga, meðaltíma til endurheimtar, hlutfall galla sem sleppa og móttökutíma, sem smíðaagi bætir allt beint.

## Andmynstur og gildrur

- **Flækjusiglingar:** að safna snjöllum, djúphreiðruðum eða útbreiddum kóða þar til enginn skilur hann.
- **Hljóð villugleyping:** tóm catch-blokk og hunsuð skilakóðar sem breyta bilunum í framtíðardulúð.
- **Varnarforritunarofgnótt:** óþarfar athuganir alls staðar sem grafa rökfræðina og fela raunverulega galla.
- **Að rugla staðhæfingum saman við villumeðhöndlun:** að nota staðhæfingar fyrir keyrsluskilyrði, eða undantekningar fyrir fastayrðingar forritara.
- **Afrita-og-líma smíði:** að tvítaka rökfræði í stað þess að endurnýta, svo lagfæringar þarf að gera á mörgum stöðum.
- **Ágiskunarleg almennni:** að smíða ágripanir og stillanleika fyrir þarfir sem aldrei koma.
- **Að hunsa staðla:** hver verkfræðingur kóðar á sinn hátt og margfaldar vitræna byrði yfir kóðagrunninn.
- **Óprófuð smíði:** að skrifa kóða án samfylgjandi prófa og fresta sannprófun til fasa sem aldrei kemur.

## Þroskalíkan

- **Stig 1 (Upphaf):** Smíði er ad hoc og viðbragðsdrifin. Flækja og villumeðhöndlun er ólík eftir einstaklingi, fáir staðlar eru til og hljóðar bilanir eru algengar.
- **Stig 2 (Þróun):** Kóðunarstaðlar, sniðmótarar og lint-tól eru til og grunnvillumeðhöndlun og einingaprófanir eru væntar, en vinnubrögð eru ósamkvæm og hvert teymi beitir þeim á sinn hátt.
- **Stig 3 (Stöðlun):** Flækjuminnkun, mörkastaðfesting, skýr villumeðhöndlun og prófanleiki eru skjalfest og framfylgt um alla skipulagsheildina, í leiðslunni og í rýni, svo allur kóðagrunnurinn lesist eins og einn vandvirkur höfundur hefði skrifað hann.
- **Stig 4 (Stjórnun):** Smíðagæði eru mæld gegn grunnlínum. Teymið rekur hringflækju, hlutfall galla sem sleppa, bilanahlutfall breytinga, villuleiðaprófaþekju og kóðarýnibreytingar og bregst við þróuninni frekar en skoðunum.
- **Stig 5 (Samhæfing):** Smíði er stöðugt bætt og samþætt um skipulagsheildina. Varnarmynstur, staðlar og mælikvarðar næra endurbyggingu og verkfæri, gervigreindaraðstoðuð verkfæri keyra undir sömu gæðahliðum og vinnubrögðin aðlagast eftir því sem tungumál, reglugerðir og áhættur breytast.

## Hugmyndir til umræðu

- Hvar safnast tilviljanakennd flækja mest í kóðagrunninum þínum og hvaða smíðavenjur skapa hana?
- Hver er raunveruleg regla teymisins þíns um hvar á að staðfesta inntök og hvar á að treysta?
- Greina verkfræðingar þínir staðhæfingar frá villumeðhöndlun og er sá greinarmunur samræmdur?
- Hve mikið af gæðum þínum er byggt inn við smíði á móti grípast síðar í rýni eða prófun?
- Hvernig ákveðurðu hvenær á að endurnýta bókasafn á móti því að smíða, með tilliti til aðfangakeðjuáhættu?
- Hvernig ætti að halda gervigreindarmynduðum kóða við sömu smíðastaðla og handskrifuðum kóða?

## Helstu atriði

- Smíði er þar sem hönnun verður að viðhaldanlegum kóða. Að lágmarka flækju er kjarnaagi hennar.
- Smíðaðu fyrir breytingar og sannprófun: prófanlegur, breytanlegur kóði er skiljanlegur kóði.
- Verðu á traustmörkum, treystu innan þeirra og gleyptu aldrei villur hljóðlega.
- Notaðu staðhæfingar fyrir fastayrðingar og villumeðhöndlun fyrir væntanleg keyrsluskilyrði. Ruglaðu þeim ekki saman.
- Staðlaðu verkfæri og stíl, endurnýttu af ásetningi og byggðu gæði inn frekar en að skoða þau inn eftirá.

## Heimildir og frekari lestur

- IEEE Computer Society, *SWEBOK Guide (Guide to the Software Engineering Body of Knowledge)*, Software Construction knowledge area
- Steve McConnell, *Code Complete: A Practical Handbook of Software Construction*
- Robert C. Martin, *Clean Code: A Handbook of Agile Software Craftsmanship*
- Andrew Hunt and David Thomas, *The Pragmatic Programmer*
- Martin Fowler, *Refactoring: Improving the Design of Existing Code*
- John Ousterhout, *A Philosophy of Software Design*
