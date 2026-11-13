# 4.5 Persónuvernd og gagnavernd

## Yfirlit og tilgangur

Öryggi ver gögn gegn óheimilum aðgangi. Persónuvernd spyr annarrar spurningar: ættirðu yfirleitt að vera að safna, nota og geyma þessi gögn, og hafa þeir sem þau lýsa eitthvað um það að segja? Þetta tvennt skarast en er ekki það sama. Þú getur verið fullkomlega öruggur og samt brotið gegn persónuvernd. Þú gerir það með því að hamstra gögn sem þér kemur ekki við að halda, nota þau í tilgangi sem fólk samþykkti aldrei eða flytja þau yfir landamæri á vegu sem lög banna. Fyrir stór teymi er persónuvernd hönnunarskorða. Hún snertir hverja þjónustu sem meðhöndlar persónuupplýsingar, sem í dag þýðir nánast þær allar.

Hagsmunirnir eru miklir og vaxandi. Persónuverndarlöggjöf hefur breiðst út um heiminn. Hún ber sektir sem stigvaxa með tekjum og gefur einstaklingum aðfararhæf réttindi yfir gögnum sínum. Fyrir fyrirtæki býður misnotkun persónuupplýsinga heim eftirlitsaðgerðum, hópmálsóknum og missi viðskiptavinatrausts sem er dýrt að endurbyggja. Fyrir hið opinbera er skyldan enn þyngri. Borgarar geta ekki valið annan veitanda fyrir skatta-, heilbrigðis- eða bótagögn sín, svo ríkið skuldar þeim sérstaka umönnunarskyldu. Og persónuverndarbrestir tæra almenningstraustið sem hið opinbera byggir á.

Þessi kafli meðhöndlar persónuvernd sem verkfræðiaga. Við förum yfir að hanna fyrir persónuvernd frá byrjun, lágmarka og varðveita gögn á ábyrgan hátt, flokka og vernda viðkvæma flokka eins og [PII](https://en.wikipedia.org/wiki/Personally_identifiable_information) og [PHI](https://en.wikipedia.org/wiki/Protected_health_information), meðhöndla samþykki og lagagrunn og stýra flutningi yfir landamæri og búsetukröfum sem móta í auknum mæli arkitektúr.

*Sjá einnig:* kafla 4.6 (regluvörslu og stjórnarhætti), kafla 7.1 (gagnastefnu og stjórnarhætti) og kafla 4.1 (öryggisgrunn og menningu).

## Meginreglur

- **[Persónuvernd með hönnun](https://en.wikipedia.org/wiki/Privacy_by_design) og sjálfgefið.** Byggðu persónuvernd inn frá upphafi og gerðu persónuverndarvænstu stillinguna að sjálfgefinni.
- **[Gagnasparnaður](https://en.wikipedia.org/wiki/Data_minimization).** Safnaðu aðeins því sem þú þarft í raun, geymdu það aðeins eins lengi og þú þarft og deildu því aðeins eins og nauðsynlegt er.
- **Tilgangstakmörkun.** Notaðu gögn aðeins í þeim tilgangi sem upplýst var um þegar þeim var safnað.
- **Lagagrunnur.** Hafðu gilda lagalega réttlætingu fyrir hverja vinnslu.
- **Réttindi einstaklinga.** Virtu rétt fólks til að fá aðgang að gögnum sínum, leiðrétta, eyða og flytja þau.
- **Gagnsæi.** Segðu fólki skýrt hvað þú safnar, hvers vegna og með hverjum þú deilir því.
- **Ábyrgðarskylda.** Vertu fær um að sýna fram á regluvörslu, ekki bara fullyrða hana.

## Ráðleggingar

### Hannaðu fyrir persónuvernd frá byrjun

Persónuvernd fest á fullbúið kerfi er dýr og ófullkomin. Bakaðu hana inn frá byrjun.

- Framkvæmdu **[persónuverndarmat (DPIA)](https://en.wikipedia.org/wiki/Data_protection_impact_assessment)** fyrir ný kerfi og eiginleika sem vinna persónugögn í stórum stíl eða bera meiri áhættu, sem greinir og dregur úr persónuverndaráhættu áður en smíðað er.
- Gerðu sjálfgefin gildi persónuverndarvæn: samþykki fyrirfram frekar en afþökkun fyrir ónauðsynlega vinnslu, lágmarks gagnareiti og stystu skynsamlegu varðveislu.
- Fáðu persónuverndarsérþekkingu snemma að hönnun, við hlið öryggisógnarmótunar, svo bæði séu íhuguð á traustmarkastiginu.
- Haltu **gagnakorti eða skrá**: hvaða persónugögn þú heldur, hvar þau búa, hvers vegna og hvert þau flæða. Þú getur ekki verndað eða gert grein fyrir gögnum sem þú sérð ekki.

### Lágmarkaðu, varðveittu og eyddu á ábyrgan hátt

Hvert persónugagn sem þú heldur er skuld jafnt og eign.

- **Lágmarkaðu söfnun:** véfengdu hvern reit. Ef þú þarft hann ekki fyrir yfirlýstan tilgang skaltu ekki safna honum.
- **Settu varðveisluáætlanir** eftir gagnategund og tilgangi og framfylgdu þeim með sjálfvirkri eyðingu. Gögn geymd „til öryggis“ eru gögn sem bíða þess að vera brotin eða stefnt til.
- **Styddu rétt til eyðingar:** byggðu getuna til að finna og eyða gögnum einstaklings yfir öll kerfi, þar á meðal afrit og niðurstraumsafrit, innan lagafresta. Þetta er miklu auðveldara þegar það er hannað inn en fest á.
- **[Gerðu nafnlaus](https://en.wikipedia.org/wiki/Data_anonymization) eða safnaðu saman** gögn fyrir greiningu og prófun svo auðkennanleg gögn dreifist ekki í aukaumhverfi.

### Flokkaðu og verndaðu viðkvæm gögn

Ekki bera öll persónugögn sömu áhættu og sumir flokkar bera sérstakt lagalegt vægi.

- Flokkaðu gögn í þrep og greindu milli **PII** (persónugreinanlegra upplýsinga), **PHI** (verndaðra heilsufarsupplýsinga), fjárhagsgagna og sérflokka (eins og kynþáttar, trúar, heilsu, lífkenna eða kynhneigðar) sem bera aukna lagalega vernd.
- Beittu vernd í réttu hlutfalli við viðkvæmni: sterkari aðgangsstýringar, dulkóðun og vöktun fyrir viðkvæmustu þrepin.
- Notaðu **[táknun](https://en.wikipedia.org/wiki/Tokenization_(data_security))** til að skipta viðkvæmum gildum (eins og kortanúmerum eða landsbundnum auðkennum) út fyrir óviðkvæm tákn, sem minnkar kerfin sem nokkurn tíma snerta hrá gögn og minnkar þannig regluvörsluumfang.
- Notaðu **[dulnefningu](https://en.wikipedia.org/wiki/Pseudonymization)** til að aðskilja auðkenni frá restinni af færslu svo gögn séu síður beint rekjanleg til einstaklings, sem dregur úr áhættu en heldur notagildi.
- Hyldu viðkvæm gögn í skrám, villuskilaboðum, greiningu og umhverfum utan framleiðslu.

### Meðhöndlaðu samþykki og lagagrunn rétt

Vinnsla persónugagna krefst gilds lagalegs grunns og samþykki er aðeins einn af nokkrum.

- Auðkenndu og skjalfestu **lagagrunninn** fyrir hverja vinnslu: samþykki, samning, lagaskyldu, lífsnauðsynlega hagsmuni, opinbert verkefni eða lögmæta hagsmuni, eftir því hvaða kerfi gildir.
- Þar sem samþykki er grunnurinn skaltu gera það **frjálst gefið, sértækt, upplýst og ótvírætt**, með jafn auðveldri leið til að draga það til baka. Fyrirmerktir reitir og búntað samþykki eru ekki gild.
- Skráðu samþykki: hverju einstaklingurinn samþykkti, hvenær og á hvaða skilmálum, svo þú getir sýnt fram á það.
- Virtu **tilgangstakmörkun**: endurnýttu ekki gögn í eitthvað ósamrýmanlegt því hvers vegna þeim var safnað án nýs grunns.
- Virtu merki eins og [Do Not Track](https://en.wikipedia.org/wiki/Do_Not_Track) / [Global Privacy Control](https://en.wikipedia.org/wiki/Global_Privacy_Control) og afþökkunarbeiðnir þar sem lög krefjast.

### Stýrðu flutningi yfir landamæri og gagnabúsetu

Hvar gögn búa líkamlega og færast er nú fyrsta flokks arkitektúráhyggjuefni.

- Skildu **gagnabúsetu**kröfur: sum lögsagnarumdæmi krefjast þess að ákveðin gögn haldist innan landamæra og sum ríkisgögn verða að vera í tilteknum fullvalda eða viðurkenndum umhverfum.
- Fyrir **flutning yfir landamæri** skaltu tryggja að gildur lagalegur búnaður (fullnægjandi-ákvarðanir, venjulegir samningsskilmálar eða jafngildi) sé til staðar og skjalfestur.
- Hannaðu fyrir búsetu frá byrjun: svæðisfestu geymslu, gagnastaðsetningu og vandlega stjórn á hvert afrit, skrár og greiningargögn flæða, því þetta lekur oft gögnum yfir landamæri óséð.
- Raktu undirvinnsluaðila og þriðju aðila. Söluaðili sem flytur gögn úr landi getur brotið búsetuskyldur fyrir þína hönd.

## Málamiðlanir: kostir og gallar

| Ákvörðun | Kostir | Gallar |
|---|---|---|
| Ágengur gagnasparnaður | Minni áhætta, minni innbrotsáhrif, einfaldari regluvarsla | Getur takmarkað greiningu og framtíðarvörumöguleika |
| Löng varðveisla | Rík saga fyrir greiningu, vélnám, deilur | Stærri skuld, innbrotsútsetning, flækja eyðingar |
| Táknun | Minnkar regluvörsluumfang, ver hrá gögn | Aukin kerfisflækja, táknhvelfing til að tryggja |
| Samþykki fyrirfram (opt-in) sem sjálfgefið | Sterkara traust, skýr regluvarsla | Minna gagnamagn, erfiðari vaxtarmælikvarðar |
| Svæðisbundin gagnabúseta | Uppfyllir lagaskyldur, byggir fullveldistraust | Arkitektúrflækja, hærri kostnaður, tvítekin innviði |
| Miðlægt gagnavatn | Greiningarafl, ein uppspretta | Samþjöppuð áhætta, erfiðari tilgangstakmörkun |

Meginspennan er milli viðskiptalystar eftir gögnum og skuldarinnar sem þau eru. Vöru- og greiningarteymi vilja eðlilega safna meira og geyma lengur. Persónuverndaragi togar hina leiðina. Þroskaða lausnin endurramma gögn sem skuld til að réttlæta, ekki eign til að hamstra. Hver söfnunar- og varðveisluákvörðun verður að vinna sér inn sæti sitt gegn áhættunni sem hún skapar. Gagnabúseta bætir við kostnaðar-gegn-regluvörslu vídd. Að mæta fullveldiskröfum getur margfaldað innviði, samt er það einfaldlega óumsemjanlegt á sumum mörkuðum og í opinberu samhengi.

## Spurningar til að ræða með teyminu

1. **Hver er varðveisluáætlun ykkar fyrir hvern flokk persónugagna og hvað framfylgir eyðingu?** Gögn geymd „til öryggis“ eru gögn sem bíða þess að vera brotin eða stefnt til, svo hver reitur og hver færsla þarf skilgreindan líftíma bundinn tilgangi sínum. Ákveddu áætlunina eftir gagnategund og framfylgdu henni síðan með sjálfvirkri eyðingu frekar en að treysta á að nokkur muni. Fyrir fyrirtæki minnkar þetta innbrotsútsetningu og geymslukostnað í einu, og fyrir hið opinbera samræmist það lögbundnum skyldum til að halda borgaragögnum ekki lengur en lög leyfa. Komdu með úrtak af elstu geymdu skrám þínum og spyrðu hver þarf þær enn og á hvaða grunni, því heiðarlega svarið er oft enginn. Ef eyðing er handvirk eða engin safnast gögn upp að eilífu og skuld þín vex hljóðlega á efnahagsreikningnum.

2. **Hvaða viðkvæma reiti getið þið táknað eða dulnefnt til að minnka bæði áhættu og regluvörsluumfang?** Að skipta kortanúmerum eða landsbundnum auðkennum út fyrir tákn afmarkar hrágildin við litla, þétt stýrða hvelfingu, sem sker kerfin í umfangi fyrir úttektir eins og PCI-DSS skarpt. Dulnefning aðskilur auðkenni frá restinni af færslu, lækkar áhættu en heldur gögnum gagnlegum fyrir greiningu og prófun. Ákveddu hvaða mjög viðkvæm gildi réttlæta táknhvelfingu (aukin flækja, hvelfing til að tryggja) og hver þurfa aðeins hyljun í skrám og umhverfum utan framleiðslu. Komdu með kort af hvert hrá viðkvæm gildi flæða í dag, því sérhvert kerfi sem snertir þau er kerfi sem þú verður að vernda og úttekta. Fyrir eftirlitsskyld og opinber gögn er þessi umfangsminnkun ein af fáum hreyfingum sem lækkar kostnað og áhættu saman, svo beindu fyrst að viðkvæmustu reitunum.

3. **Áður en næsti eiginleiki ykkar fer út, hvað kallar fram persónuverndarmat og hver framkvæmir það?** Persónuvernd fest á fullbúið kerfi er dýr og ófullkomin, svo DPIA verður að keyra snemma, við hlið öryggisógnarmótunar, þegar þú getur enn breytt hönnuninni ódýrt. Ákveddu kveikjuna (ný vinnsla í stórum stíl, sérflokkagögn, nýr tilgangur) og nefndu hver á matið svo það falli ekki milli rifa undir afhendingarþrýstingi. Raunverulegt DPIA getur gripið ofsöfnun fyrir opnun, til dæmis með því að skipta nákvæmri staðsetningu út fyrir gróft svæði án vörutaps. Komdu með væntanlegan eiginleika og gakktu í gegnum hann: hvaða persónugögn hann safnar, hvers vegna og hvort minna uppáþrengjandi hönnun nái sama markmiði. Fyrir opinbera þjónustu sem borgarar geta ekki afþakkað er þessi snemmbúna athugun hluti umönnunarskyldunnar, svo gerðu hana að hliði, ekki eftirþanka.

4. **Þegar persónugögn fara yfir landamæri, þar á meðal gegnum afrit, skrár og undirvinnsluaðila, hvaða lagalegur búnaður dekkar hvert yfirferð og getið þið sannað það?** Búsetu- og flutningsreglur móta nú arkitektúr jafn mikið og allar afkastakröfur, og yfirferðirnar sem grípa teymi eru sjaldan þær augljósu: skrá send til erlends sýnileikaverkfæris, afrit afritað á ódýrara svæði eða undirvinnsluaðili sem hljóðlega færir gögn úr landi. Fyrir stóra skipulagsheild eru þrýstingarnir sem togast á raunverulegir, því svæðisfestir innviðir kosta meira og tvítaka rekstur, samt getur einn ólöglegur flutningur ógilt markaðsinngöngu eða kallað fram fullnustufyrirmæli. Komdu með núverandi gagnaflæðikort sem nefnir hvern stað þar sem persónugögn hvíla líkamlega eða ferðast, lagalega búnaðinn fyrir hver landamæri sem þau fara yfir (fullnægjandi-ákvörðun, venjulegir samningsskilmálar eða jafngildi) og lista undirvinnsluaðila með staðsetningum þeirra. Fyrir hið opinbera og fullvalda gagnasamhengi skaltu líta á búsetu sem harða arkitektúrskorðu frekar en samningsákvæði, því sumar skrár mega aldrei yfirgefa viðurkennd landsumhverfi og ábyrgi aðilinn getur ekki framselt þá skyldu til söluaðila.

5. **Hvaða lagagrunnur styður hverja vinnslu og gætuð þið varið það val fyrir eftirlitsaðila á morgun?** Samþykki er aðeins einn af nokkrum lagagrunnum og teymi velja það oft sjálfgefið þegar samningur, lagaskylda, opinbert verkefni eða lögmætir hagsmunir væru bæði heiðarlegri og varanlegri. Þetta skiptir máli í stærð því veikur eða rangt valinn grunnur getur ógilt heila leiðslu, og að greiða úr vinnslu sem þú áttir engan rétt á að framkvæma er miklu dýrara en að velja rétta grunninn fyrirfram. Vegðu sjónarmiðin sem togast á opinskátt: samþykki gefur einstaklingum stjórn en er hægt að draga til baka og verður að vera frjálst gefið, sértækt og óbúntað, á meðan grunnur eins og lögmætir hagsmunir forðast samþykkisþreytu en krefst skjalfests vægisprófs. Komdu með skrá sem varpar hverri vinnslu á fullyrtan grunn sinn, sönnunargögnin sem styðja hann og hvernig þú myndir draga til baka eða skipta ef véfengt. Hjá hinu opinbera hvílir mest kjarnavinnsla á opinberu verkefni frekar en samþykki, svo vertu nákvæmur um hvar valkvætt, afturkallanlegt samþykki byrjar, því að þoka þessu tvennu tærir traustið sem borgarar hafa ekkert val um en að veita.

6. **Ef einstaklingur nýtti rétt sinn til aðgangs, eyðingar eða flutnings í dag, gætuð þið uppfyllt það yfir hvert kerfi innan lagafrests?** Réttindi einstaklinga eru auðvelt að lofa í persónuverndarstefnu og erfitt að heiðra í arkitektúr sem dreifði afritum persónugagna í afrit, skyndiminni, greiningargeymslur og niðurstraumsþjónustur. Fyrir stórt teymi er þetta augnablikið þegar óhlutbundin regluvarsla verður áþreifanlegt verkfræðipróf, og misstur lögbundinn frestur er bæði tilkynningarskyld bilun og merki um að þú sjáir í raun ekki þín eigin gögn. Sjónarmiðið á móti er kostnaður og flækja, því að smíða raunverulega eyðingu og útflutning yfir kerfi er raunveruleg vinna, en valkosturinn er handvirk, hæg, villuhætt uppfylling sem stigvaxar ekki og brýtur hljóðlega lög. Komdu með heiðarlega gegnumgöngu á einni raunverulegri beiðni frá móttöku til lokunar, þar á meðal hvernig afrit og þriðju aðilar nást, og tímasettu hana gegn lagafrestinum. Fyrir opinbera þjónustu sem fólk getur ekki yfirgefið skaltu líta á sjálfsafgreiðslu, fullkomna og úttektarhæfa réttindauppfyllingu sem hluta umönnunarskyldunnar, ekki eiginleika til að tímasetja síðar.

## Sjónarhorn eftir geirum

**Sprotafyrirtæki.** Með örlítið teymi og lítið svigrúm skaltu líta á persónuvernd sem ódýra tryggingu frekar en áætlun sem þú getur ekki mannað. Safnaðu aðeins reitunum sem kjarnaeiginleikinn þarf, haltu léttu töflureiknisgagnakorti svo þú getir í raun svarað eyðingarbeiðni og haltu tölvupóstföngum og táknum úr skrám. Skýrt samþykkisflæði og raunveruleg eyðing kosta eftirmiðdag núna. Að bæta þeim við eftir að fyrsti fyrirtækjaviðskiptavinur eða eftirlitsaðili spyr kostar miklu meira, og ofsafnað gögn eru skuld sem þú græðir ekkert á að halda.

**Lítið fyrirtæki.** Án sérstaks persónuverndarsérfræðings og með þröngt fjárhagsáætlun skaltu hallast að persónuverndarstýringum sem eru þegar innbyggðar í verkfærin sem þú kaupir og kjósa söluaðila sem gera gagnameðhöndlun gagnsæja og búsetu skýra. Rammaðu ákvörðunina sem kaupa á móti smíða: þú smíðar nánast aldrei táknun eða réttindauppfyllingu sjálfur, svo veldu vettvanga sem bjóða varðveislureglur, útflutning og eyðingu úr kassanum. Vittu hvaða persónugögn þú heldur og hvar röng eða týnd skrá myndi kosta þig viðskiptavin, og skrifaðu niður lagagrunn fyrir hverja notkun jafnvel þótt skjalið sé stutt.

**Stórfyrirtæki.** Í stærð er vandinn samræmi yfir mörg teymi: sameiginlegt gagnakort, staðlað flokkunarþrep og framfylgd varðveisla svo ekkert eitt teymi verði veiki hlekkurinn. Fjárhagsáætlaðu verkfræðina fyrir eyðingu yfir kerfi, táknhvelfingar og búsetumeðvitaðan arkitektúr skýrt og stýrðu undirvinnsluaðilum miðlægt svo einn söluaðili geti ekki brotið flutningsskyldu fyrir þína hönd. Gerðu DPIA að hliði í afhendingarferlinu og mældu persónuverndarstöðu, því endurskoðendur og eftirlitsaðilar munu biðja þig að sýna fram á regluvörslu, ekki bara fullyrða hana.

**Hið opinbera.** Innkaupareglur, gagnsæisskyldur og opinber ábyrgð móta hvert val, og borgarar geta ekki tekið skatta-, heilbrigðis- eða bótagögn sín annað, svo umönnunarskyldan er aukin. Festu viðkvæmar skrár við viðurkennd landsumhverfi þar á meðal afrit og greiningu, bindu hvern söluaðila samningslega við sömu búsetu- og eyðingarskyldur og skjalfestu lagagrunn (oft opinbert verkefni) fyrir kjarnavinnslu meðan valkvæð notkun er höfð í sérstöku, afturkallanlegu samþykki. Birtu látlausar lýsingar á því hvað þú safnar og hvers vegna og gerðu réttindauppfyllingu áreiðanlega innan lögbundinna tímalína, því persónuverndarbrestur hér tærir almenningstraustið sem þjónustan byggir á.

## Dæmi

**Sprotafyrirtæki.** Neytendaforrit á frumstigi safnar aðeins gögnunum sem það raunverulega þarf, því hver aukareitur er skuld sem það vill síður verja síðar. Það heldur einföldu töflureiknisgagnakorti af hvar persónugögn búa svo það geti í raun svarað eyðingarbeiðni, heldur tölvupóstföngum og táknum úr skrám sínum og setur grunnvarðveislureglu til að hreinsa gögn úr löngu dauðum reikningum. Að byggja skýrt samþykkisflæði og raunverulega eyðingu núna kostar eftirmiðdag. Að bæta þeim við eftir að fyrsti fyrirtækjaviðskiptavinur eða eftirlitsaðili spyr kostar miklu meira.

**Stórfyrirtæki.** Hnattrænt neytendaforrit framkvæmir DPIA áður en það opnar nýjan meðmælaeiginleika og uppgötvar að hann myndi safna nákvæmri staðsetningu að óþörfu. Teymið skiptir yfir í gróf svæðisgögn og dregur úr áhættu án vörutaps. Kortanúmer eru táknuð svo aðeins lítil, þétt stýrð hvelfing heldur hrágildum, sem sker [PCI](https://en.wikipedia.org/wiki/Payment_Card_Industry_Data_Security_Standard)-umfang (greiðslukortaiðnaðarins) fyrirtækisins stórlega. Sjálfvirkar varðveislureglur hreinsa gögn óvirkra reikninga á áætlun og sjálfsafgreiðsluflæði leyfir notendum að flytja út og eyða gögnum sínum innan lagafrests yfir öll kerfi þar á meðal afrit.

**Hið opinbera.** Landsbundin heilbrigðisþjónusta flokkar allar sjúklingaskrár sem PHI og sérflokkagögn og framfylgir ströngum aðgangsstýringum, dulkóðun og úttektarskráningu. Gagnabúsetustefna heldur öllum skrám innan landamæra, þar á meðal afritum og greiningu, og hver söluaðili er samningsbundinn sama. Borgarar hafa skjalfestan lagagrunn (opinbert verkefni) fyrir kjarnavinnslu, á meðan valkvæð rannsóknarnotkun krefst sérstaks, afturkallanlegs samþykkis sem er skráð og heiðrað. Gagnakort liggur til grundvallar getunni til að svara aðgangs- og eyðingarbeiðnum innan lögbundinna tímalína.

## Viðskiptarök: hvatar, ávöxtun fjárfestingar og heildarkostnaður

Persónuverndarfjárfesting er oft römmuð sem hrein regluvörslukostnaður, en það vanmetur hana. Heildareignarkostnaðurinn felur í sér DPIA-ferli, gagnakorts- og skráartól, táknunar- og varðveisluinnviði og verkfræðina til að styðja réttindi einstaklinga og búsetu. Vegðu það gegn kostnaðinum við að fjárfesta ekki, sem er alvarlegur og sífellt líklegri. Persónuverndarsektir ná nú prósentum af heimstekjum, hópmálsóknir fylgja stórum innbrotum og eftirlitsaðilar hafa sýnt að þeir munu bregðast við. Umfram sektir eyðileggur misnotuð persónuvernd viðskiptavinatraustið sem tekjur byggja á. Og að úrbæta persónuverndarbrest eftir á (að bæta við eyðingu, greiða úr ólöglegum gagnaflæðum) kostar miklu meira en að byggja hana inn.

Ávöxtunin hefur líka raunverulegan ávinning. Sterk persónuvernd er samkeppnisaðgreining, og á eftirlitsskyldum og opinberum mörkuðum er hún forsenda þess að vinna viðskipti yfirleitt. Gagnasparnaður dregur beint úr innbrotsútsetningu og geymslukostnaði og táknun minnkar dýra umfang úttekta eins og PCI-DSS. Þegar þú færir rök við forystu skaltu setja persónuvernd fram á tvo vegu: sem áhættuleiðrétta skuldastjórnun með raunverulegri eftirlitsútsetningu og sem traustseign sem opnar markaði. Leggðu áherslu á að persónuvernd með hönnun er ódýr miðað við persónuvernd með málsókn, og að gögn hamstruð án tilgangs eru skuld sem situr á efnahagsreikningnum og bíður þess að raungerast.

## Andmynstur og gildrur

- **Safna öllu, ákveða síðar.** Að hamstra gögn án tilgangs og hámarka skuld fyrir engan ávinning.
- **Varðveisla af vanrækslu.** Að eyða aldrei neinu því engin áætlun er til, svo gögn safnast að eilífu.
- **Samþykkisleikhús.** Fyrirmerktir reitir, búntað samþykki eða blekkingarhönnun sem er lagalega ógild og tærir traust.
- **Eyðing sem missir afrit.** Að eyða úr aðalgeymslu en skilja afrit eftir í afritum, skrám og greiningu.
- **PII í skrám og prófunargögnum.** Að dreifa viðkvæmum gögnum í umhverfi með lítilli stýringu þar sem auðvelt er að afhjúpa þau.
- **Að hunsa gagnaflæði.** Að líta framhjá því að skrár, afrit, greining og undirvinnsluaðilar færa gögn yfir landamæri.
- **Persónuvernd sem eingöngu lagaleg áhyggjuefni.** Að líta á hana sem pappírsvinnu frekar en verkfræðihönnunarskorðu.
- **Ekkert gagnakort.** Að geta ekki svarað hvar persónugögn búa, sem gerir réttindabeiðnir og innbrotsviðbrögð ómöguleg.

## Þroskalíkan

**Stig 1: Upphaf.** Persónuvernd er meðhöndluð viðbragðsdrifið, ef yfirleitt. Persónugögnum er safnað frjálslega án skrár, sparnaðar eða varðveislutakmarka. Samþykki er eftirþanki, ekkert ferli er til fyrir aðgangs- eða eyðingarbeiðnir og hvar gögn búa líkamlega er óíhugað.

**Stig 2: Þróun.** Grunnvinnubrögð birtast en eru mismunandi eftir teymum. Persónuverndarstefna er til og grunnsamþykki er fangað, með einhverri vitund um varðveislu. Réttindabeiðnir eru meðhöndlaðar handvirkt og hægt, gagnaflokkun er óformleg og eitt teymi gæti kortlagt gögn sín meðan annað safnar frjálslega. Ekkert er framfylgt samræmt yfir skipulagsheildina.

**Stig 3: Stöðlun.** Persónuvernd með hönnun er skjalfest og framfylgt um alla skipulagsheildina. DPIA keyra fyrir áhættumeiri verkefni, gögn eru kortlögð og flokkuð í þrep og varðveisluáætlanir eru framfylgdar með sjálfvirkri eyðingu. Lagagrunnur er skjalfestur fyrir hverja vinnslu, gild samþykkisbúnaður er til staðar, réttindabeiðnir eru uppfylltar innan fresta og búseta er tekin fyrir hjá eftirlitsskyldum gögnum.

**Stig 4: Stjórnun.** Persónuverndaráætlunin er mæld og stýrð gegn grunnlínum. Þú rekur uppfyllingartíma réttindabeiðna gegn lögbundnum fresti, varðveislustefnuþekju og aldur elstu skráa, fjölda persónugagnareita í umfangi og hve margir eru táknaðir eða dulnefndir, DPIA-lokahlutfall fyrir eiginleika sem uppfylla skilyrði og fjölda óstýrðra landamæraflæða fundnum í úttektum. Mælikvarðar næra skilgreinda þröskulda, svo brot á markmiði (réttindabeiðni nálægt fresti, óvæntur flutningur, varðveislurek) kallar fram skjalfest viðbrögð í stað þess að fara óséð.

**Stig 5: Samhæfing.** Persónuvernd er sjálfgefin verkfræðiskorða sem batnar stöðugt og er samþætt um skipulagsheildina. Sparnaður, táknun og sjálfvirk varðveisla eru staðall, réttindabeiðnir eru sjálfsafgreiðsla og fullkomnar yfir öll kerfi þar á meðal afrit, og gagnaflæði og búseta eru rakin og framfylgd samfellt. Persónuverndarstaða aðlagast eftir því sem regluverk, markaðir og arkitektúr breytast og nærir lærdóm aftur í hönnun svo grunnlínan haldi áfram að hækka frekar en bara halda.

## Hugmyndir til umræðu

1. Hvernig leysirðu spennuna milli greiningarteyma sem vilja meiri gögn og persónuverndar sem vill minni?
2. Hver er raunhæfur arkitektúr til að heiðra eyðingu yfir aðalgeymslur, afrit og niðurstraumsafrit?
3. Hvaða lagagrunnur á við hverja af vinnslum þínum og geturðu varið valið?
4. Hvernig heldurðu persónugögnum úr skrám og umhverfum utan framleiðslu án þess að hindra villuleit?
5. Hvaða gagnabúsetukröfur gilda á mörkuðum þínum og hvernig flækja afrit og greining þær?
6. Hvernig ætti að sameina persónuverndar- og öryggisógnarmótun í eina hönnunarstarfsemi?

## Helstu atriði

- Persónuvernd ræður hvort og hvernig þú notar persónugögn. Hún er aðgreind frá og viðbót við öryggi.
- Hannaðu persónuvernd inn frá byrjun með DPIA og persónuverndarvænum sjálfgefnum gildum.
- Lágmarkaðu söfnun, framfylgdu varðveisluáætlunum og byggðu raunverulega eyðingargetu.
- Flokkaðu PII, PHI og sérflokka og verndaðu þá í réttu hlutfalli með táknun og hyljun.
- Settu og skjalfestu lagagrunn. Gerðu samþykki frjálst gefið, sértækt og afturkallanlegt.
- Líttu á gagnabúsetu og flutning yfir landamæri sem fyrsta flokks arkitektúrskorður.
- Gögn eru skuld jafnt og eign. Að hamstra þau án tilgangs er áhætta sem bíður þess að raungerast.

## Heimildir og frekari lestur

- Ann Cavoukian, *Privacy by Design: The 7 Foundational Principles*
- European Union, *General Data Protection Regulation (GDPR)* text and guidance
- National Institute of Standards and Technology, *Privacy Framework* and *SP 800-122* (Guide to Protecting PII)
- ISO/IEC 27701, *Privacy Information Management*
- Daniel Solove, *Understanding Privacy*
- OECD, *Privacy Guidelines* and *Fair Information Practice Principles (FIPPs)*
- California Consumer Privacy Act (CCPA/CPRA) statutory text and regulator guidance
