# 9.1 Áreiðanleikaverkfræði

## Yfirlit og tilgangur

[Áreiðanleikaverkfræði](https://en.wikipedia.org/wiki/Site_reliability_engineering) (SRE) beitir hugbúnaðarverkfræðivenjum á rekstur framleiðslukerfa. Í stað þess að líta á rekstur sem handvirka, miðadrifna vinnu aðskilda frá þróun lítur SRE á áreiðanleika sem verkfræðivandamál sem þú leysir með kóða, mælingum og skýrum þjónustumarkmiðum. Kjarnahugmyndin, gerð vinsæl af Google en nú útbreidd, er einföld: fólkið sem heldur kerfum keyrandi ætti að eyða mestum tíma sínum í að smíða sjálfvirkni og bæta kerfi, ekki slökkva sömu bilanirnar í höndunum aftur og aftur.

Fyrir stór teymi skiptir þetta máli því stærð hækkar bæði verðmæti áreiðanleika og kostnað þess að gera hann rangt. Þegar ein þjónusta styður milljónir notenda eða þúsundir innri notenda þýðir klukkustund af niðurtíma glataðar tekjur, misst viðskipti og rýrt traust. Handvirkur rekstur sem virkar vel fyrir örfáa þjóna hrynur undir hundruðum þjónusta og [samfelldri útsetningu](https://en.wikipedia.org/wiki/Continuous_deployment). SRE gefur þér sameiginlegt tungumál um áreiðanleika, leið til að gera málamiðlunina milli þess að afhenda eiginleika og að halda hlutum stöðugum skýra og leið til að halda þeirri línu samræmt yfir mörg teymi.

Fyrirtækja- og opinbert umhverfi bætir við frekara vægi. Regluverkaðar atvinnugreinar eins og bankar, heilbrigðisþjónusta og opinber þjónusta bera oft lagalegar eða samningsbundnar aðgengisskuldbindingar, úttektarkröfur og lítið þol fyrir rofum sem hafa áhrif á borgara eða öryggi. Opinber stafræn þjónusta birtir í auknum mæli áreiðanleikamarkmið sín og afkastagögn opinberlega. SRE gefur þér strangan, sönnunarbyggðan hátt til að skilgreina hvað „nógu áreiðanlegt“ þýðir, mæla það heiðarlega og verja verkfræðiforgangsröðun fyrir forystu og eftirlitsaðilum með gögnum frekar en skoðun.

*Sjá einnig:* kafla 9.2 (vöktun og eftirlit), kafla 9.3 (atvikastjórnun) og kafla 3.5 (stigvöxtur, afköst og seigla).

## Meginreglur

- **Áreiðanleiki er mikilvægasti eiginleikinn.** Kerfi sem virkar ekki er einskis virði sama hve marga eiginleika það hefur, en fullkominn áreiðanleiki er hvorki framkvæmanlegur né kostnaðarins virði.
- **Skilgreindu áreiðanleika með mælanlegum markmiðum.** Þjónustustigsvísar (SLI), markmið (SLO) og samningar (SLA) breyta óljósum væntingum í tölur sem allir geta komið sér saman um.
- **100 prósent er rangt markmið.** Notendur sjá ekki mun á mjög áreiðanlegu kerfi og fullkomlega áreiðanlegu, svo stefndu á „nógu áreiðanlegt“ og eyddu afganginum af fjárhagsáætluninni í hraða.
- **Villufjárhagsáætlanir samstilla hvata.** Bilið milli SLO og 100 prósenta er áhættufjárhagsáætlun sem forritarar og rekstraraðilar deila og kemur í stað rökræðna með reikningi.
- **Leiðindavinna er óvinurinn.** Endurtekna, handvirka, sjálfvirknivæðanlega rekstrarvinnu ætti að mæla, setja þak á og útrýma kerfisbundið.
- **Sjálfvirknivæddu af ásetningi.** Sjálfvirkni er hvernig lítið teymi rekur stórt kerfi. Að fjárfesta í henni er fyrsta flokks verkfræðistarfsemi.
- **Nám án sakbendingar.** Bilanir eru meðhöndlaðar sem tækifæri til að bæta kerfi og ferli, ekki til að refsa einstaklingum.

## Ráðleggingar

### Skilgreindu SLI, SLO og SLA af ásetningi

Byrjaðu út frá sjónarhorni notandans. **[Þjónustustigsvísir](https://en.wikipedia.org/wiki/Service-level_indicator)** er megindlegur mælikvarði á hegðun þjónustu, svo sem hlutfall beiðna afgreiddra á innan við 300 millisekúndum eða brot vel heppnaðra svara. Veldu fáa SLI sem endurspegla sannarlega ánægju notenda: aðgengi, töf, réttleiki og ferskleiki eru algeng. **[Þjónustustigsmarkmið](https://en.wikipedia.org/wiki/Service-level_objective)** er markgildi eða svið fyrir SLI, til dæmis „99,9 prósent beiðna heppnast yfir rúllandi 28 daga glugga.“ **[Þjónustustigssamningur](https://en.wikipedia.org/wiki/Service-level_agreement)** er samningur með afleiðingum (endurgreiðslum, viðurlögum) festum við lofað stig. Haltu SLO þínum strangari en SLA þínum, svo þú fáir viðvörun áður en þú brýtur skuldbindingu. Birtu SLO þín, rýndu þau ársfjórðungslega og líttu á þau sem lifandi skjöl sem herðast eða slakna þegar þú lærir.

### Taktu upp villufjárhagsáætlanir og framfylgdu þeim

Villufjárhagsáætlunin er `100% mínus SLO`. Ef SLO þitt er 99,9 prósent er fjárhagsáætlun þín 0,1 prósent óáreiðanleika á glugga, nokkurn veginn 43 mínútur á mánuði. Eyddu henni í skipulagða áhættu: ágengar útgáfur, tilraunir og stýrð bilunarpróf. Þegar fjárhagsáætlunin er heilbrigð geta teymi afhent hratt. Þegar hún klárast ætti stefnan sjálfvirkt að færa forgangsröðun að áreiðanleikavinnu og gera hlé á áhættusömum breytingum þar til kerfið jafnar sig. Kraftur villufjárhagsáætlunarinnar er að þú kemur þér saman um hana fyrirfram, svo hún tekur tilfinningar og pólitík úr augnablikinu þegar rof verður.

### Mældu og minnkaðu leiðindavinnu

Leiðindavinna er rekstrarvinna sem er handvirk, endurtekin, sjálfvirknivæðanleg, taktísk og vex í takt við kerfið. Raktu hlutfall SRE-tíma sem fer í leiðindavinnu og settu þak, oft um 50 prósent, svo að minnsta kosti helmingur verkfræðitímans fari í varanlegar umbætur. Haltu forgangslista verkefna til að minnka leiðindavinnu, forgangsraðaðu eftir tíðni sinnum kostnað og fagnaðu því að drepa endurtekið verk jafnmikið og að afhenda nýjan eiginleika. **Sjálfvirknivæðingarumboð** gerir þetta skýrt: hvert handvirkt ferli sem þú framkvæmir oftar en tiltekinn fjölda sinnum verður frambjóðandi fyrir sjálfvirkni eða sjálfsafgreiðsluverkfæri.

### Skipuleggðu afkastagetu og spáðu eftirspurn

Líkanaðu væntanlegt álag úr sögulegri þróun, áætluðum opnunum og viðskiptaspám. Sameinaðu lífræna vaxtarspá við einstaka atburði eins og markaðsherferðir, skattafresti eða innritunartímabil bóta sem skipta miklu hjá hinu opinbera. Haltu svigrúmi yfir hámarki, álagsprófaðu til að athuga forsendur þínar og sjálfvirknivæddu skölun þar sem þú getur, á meðan þú heldur mannrýndri [afkastagetuáætlun](https://en.wikipedia.org/wiki/Capacity_planning) fyrir stórar skuldbindingar. Raktu leiðtíma útvegunar svo skortur komi þér aldrei á óvart.

### Líttu á áreiðanleika sem eiginleika með raunverulegan kostnað

Hver auka „nía“ aðgengis kostar yfirleitt langtum meira í tvítekningu, prófunum og rekstrarflækju en sú á undan. Gerðu kostnað níanna skýran, svo vörueigendur velji markmiðið með opin augu. Hannaðu fyrir mjúka skerðingu, svo hlutabilanir gefi skerta þjónustu frekar en algjört rof. Fjárfestu í tvítekningu og yfirfærslu í réttu hlutfalli við SLO, ekki jafnt yfir hvern íhlut.

### Veldu skipulagslíkan fyrir SRE

Ekkert eitt rétt skipulag er til. **Miðlægt** SRE-teymi gefur þér samræmi, djúpa sérþekkingu og sameiginleg verkfæri, en það getur orðið flöskuháls eða ruslakista fyrir vandamál annarra. **Innbyggt** líkan setur SRE-verkfræðinga inni í vöruteymi fyrir náið samstarf, en áhættan er ósamræmi og einangrun. Margar stórar skipulagsheildir nota blending: miðlægt vettvangs- og staðlateymi auk innbyggðra áreiðanleikaverkfræðinga, með skýru þátttökulíkani sem skilgreinir hvenær þjónusta uppfyllir skilyrði fyrir SRE-stuðning og hvaða framleiðsluviðbúnaðarviðmið hún verður að standast fyrst.

## Málamiðlanir: kostir og gallar

| Ákvörðun | Kostir | Gallar |
|---|---|---|
| Ströng SLO (fleiri níur) | Meira traust notenda, mætir samningum | Hækkandi kostnaður, hægari eiginleikaafhending |
| Slök SLO (færri níur) | Hraðari afhending, lægri kostnaður | Hætta á brottfalli notenda og SLA-viðurlögum |
| Miðlægt SRE | Samræmi, sameiginleg sérþekking | Flöskuhálsar, fjarlægð frá vöru |
| Innbyggt SRE | Náið samstarf, samhengi | Ósamræmi, erfitt að manna |
| Mikil sjálfvirknifjárfesting | Skalast, minnkar leiðindavinnu | Kostnaður fyrirfram, sjálfvirkni getur sjálf bilað |

Áreiðanleikaverkfræði snýst í raun um að eyða takmörkuðum auðlindum skynsamlega. Að elta auka níu sem notendur geta ekki einu sinni skynjað sóar peningum sem gætu fjármagnað eiginleika eða lækkað verð. Farðu hina leiðina og vanfjárfestu í kerfi þar sem bilanir valda raunverulegum skaða og það er vanræksla. Villufjárhagsáætlunarrammi er til einmitt til að gera þessa málamiðlun sýnilega og samningshæfa frekar en óbeina og ágreiningsfulla. Skipulagslíkans-málamiðlunin er jafn raunveruleg: rétta svarið veltur á stærð fyrirtækis, verkfræðiþroska og hve einsleit þjónusta þín er.

## Spurningar til að ræða með teyminu

1. **Hvaða nákvæmlega SLI endurspeglar það sem notendur ykkar finna í raun og getið þið sýnt að hann sé ekki hégómamælikvarði?** Veldu rangan vísi og hvert mælaborð lítur grænt út á meðan notendur þjást, sem er hégóma-SLI gildran sem þessi kafli varar við. Komdu með raunveruleg gögn í umræðuna: mældu sömu notendaferð af raunverulegri beiðnaslóð (innskráning að mælaborði, greiðsla að staðfestingu) frekar en örgjörvanotkun þjóns eða heilsuathugun á bakenda. Fyrir stórt teymi dreifist einn slæmur SLI: tugir þjónusta erfa hann, viðvaranir kvikna á röngu og villufjárhagsáætlunin hættir að merkja nokkuð. Í fyrirtækja- og opinberu umhverfi þar sem SLA ber endurgreiðslur eða borgaraáhrif er SLI ykkar sönnunargögnin sem þið verjið fyrir úttektaraðilum, svo hann verður að rekjast beint til notendasýnilegs árangurs. Ef þú getur ekki dregið línu frá tölunni til upplifunar notanda skaltu skipta tölunni út.

2. **Hvað verður þjónusta að sanna áður en SRE-teymi ykkar tekur hana á bakvakt og hver segir nei?** Án framleiðsluviðbúnaðarviðmiðs verður miðlægt SRE-teymi ruslakista fyrir hverja óstöðuga þjónustu og drukknar í tæknilegri skuld annarra. Skrifaðu niður inngönguviðmiðin: SLO í eigu, virkar keyrsluhandbækur, framkvæmanlegar viðvaranir, afkastagetusvigrúm og sýnda útsetningar-og-afturköllunarleið. Fyrir stóra skipulagsheild er þetta þátttökulíkan það sem heldur áreiðanleikateyminu frá því að verða flöskuháls sem hægir á öllum. Í regluverkuðu umhverfi tvöfaldast viðbúnaðarrýnin sem stýring sem þú getur sýnt eftirlitsaðilum. Ákveddu hver hefur vald til að neita innleiðingu, því viðmið sem enginn framfylgir er ekki viðmið og svarið breytir því hvort SRE skalast eða hrynur undir erfðum sársauka.

3. **Hve langt fram í tímann útvegið þið fyrir stærsta fyrirsjáanlega hámark ykkar og þekkið þið leiðtíma útvegunar?** Að gera ráð fyrir að skýjateygjanleiki sé samstundis og óendanlegur býður skorti einmitt á hámörkunum sem skipta mestu og þau hámörk (skattafrestir, innritunargluggar, söluviðburðir) eru augnablikin þegar bilun er sýnilegust og dýrust. Komdu með tölurnar: sögulegt hámarksálag, spáðan vöxt, margfeldið sem þú álagsprófar að og raunverulegan leiðtíma til að afla stórrar frátekinnar afkastagetu eða sérhæfðra tilvika. Fyrir árstíðabundna opinbera þjónustu getur hámarkið verið margfalt eðlilegt álag og er pólitískt óhjákvæmilegt, svo að útvega vikum fyrirfram slær að vona að sjálfskölun haldi í við. Svarið ætti að setja áþreifanlegt dagatal: hvenær þú álagsprófar, hvenær þú læsir afkastagetu og hver á ákvörðunina um að fara.

4. **Þegar villufjárhagsáætlun ykkar klárast, hvað gerist í raun og hver hefur umboð til að framfylgja henni?** Villufjárhagsáætlun sem aldrei er brugðist við þegar hún er uppurin er bara skraut og augnablik rofs er versti tíminn til að semja um stefnuna frá grunni. Togið á móti er raunverulegt: skuldbundin opnun, tekjufrestur eða opinber tilkynning mun þrýsta fast á frystingu áhættusamra breytinga. Komdu með brunahraðagögnin, fyrirfram samþykktan stefnutexta og skrá yfir síðustu skiptin sem fjárhagsáætlunin var brotin, svo þú sjáir hvort frystingin hélt í raun. Fyrir stórt teymi samstillir fjárhagsáætlunin hvata aðeins ef hver hópur erfir sömu framfylgd, svo ákveddu fyrirfram hver skrifar undir undanþágu og hvernig sú undantekning er skráð. Í fyrirtækja- og opinberu umhverfi þar sem SLA ber viðurlög eða borgaraáhrif verður undanþáguslóðin úttektargripur, svo nefndu ábyrga eigandann núna frekar en að spinna þegar fjárhagsáætlunin er þegar horfin.

5. **Hvaða hluti vinnuviku SRE-teymis ykkar er leiðindavinna og er það mæld tala eða tilfinning?** Leiðindavinna sem enginn telur þenst hljóðlega út þar til teymið eyðir öllum tíma sínum í slökkvivinnu og engum í að smíða varanlegar umbætur, sem er nákvæmlega gildran sem SRE er til að sleppa úr. Spennan er að mæling leiðindavinnu er sjálf vinna og verkfræðingar undir frestþrýstingi streitast við að skrá í hvað tími þeirra fer. Komdu með heiðarlegt úrtak: viku eða tvær af raktum tíma gegn sameiginlegri skilgreiningu á leiðindavinnu (handvirk, endurtekin, sjálfvirknivæðanleg, taktísk og skalast með kerfinu), auk forgangslista sjálfvirkniverkefna raðað eftir tíðni sinnum kostnað. Fyrir stóra skipulagsheild þýðir 50 prósenta þak aðeins eitthvað ef það er skýrt frá og varið teymi fyrir teymi, svo komdu þér saman um hver rýnir töluna og hvað gerist þegar teymi brýtur hana. Í regluverkuðu og opinberu samhengi losar það að setja þak á leiðindavinnu knappa sérfræðinga fyrir stýringar- og úttektarvinnuna sem handvirkur rekstur þrengir að, svo líttu á leiðindavinnutöluna sem afkastagetumerki sem forysta ætti að sjá.

6. **Hvaða SRE-skipulagslíkan rekið þið og hvaða sönnunargögn myndu segja ykkur að það passi ekki lengur?** Miðlægt teymi gefur samræmi og sameiginleg verkfæri en getur orðið flöskuháls. Innbyggt líkan gefur samhengi en rekur í ósamræmi. Blendingurinn sem flestar stórar skipulagsheildir setjast á þarf skýrt þátttökulíkan eða hann erfir veikleika beggja. Komdu með merkin sem afhjúpa álag: hve lengi þjónustur bíða eftir SRE-stuðningi, hve mikið áreiðanleikavenjur eru ólíkar milli teyma og hvort innbyggðum verkfræðingum finnist þeir skornir frá faglegu samfélagi. Rétta svarið veltur á stærð fyrirtækis, verkfræðiþroska og hve einsleit þjónusta þín er, svo endurskoðaðu það þegar þau breytast frekar en að líta á fyrsta valið sem varanlegt. Fyrir fyrirtæki eða opinberan aðila með mörg teymi og strangar einsleitnikröfur jafnvægir miðlægur staðla- og vettvangshópur auk innbyggðra áreiðanleikaverkfræðinga yfirleitt samræmi gegn staðbundnu samhengi, en aðeins ef þátttökulíkanið og framleiðsluviðbúnaðarviðmiðið eru skrifuð niður og einhver á þau.

## Sjónarhorn eftir geirum

**Sprotafyrirtæki.** Með örfáa verkfræðinga og ekkert svigrúm fyrir sérstakt áreiðanleikateymi skaltu velja eitt SLO á notendaferðina sem skiptir mestu og deila bakvakt yfir allt teymið. Hallaðu þér að stýrðum þjónustum skýjaveitunnar og innbyggðri vöktun frekar en að smíða vöktunarinnviði og skrifaðu stutta eftirmálsrýni í sameiginlegt skjal svo lagfæringar festist. Hraði skiptir meira máli en ferli hér: laust SLO sem þú framfylgir slær íburðarmikið sem enginn fylgist með.

**Lítið fyrirtæki.** Án sérfræðings til að reka áreiðanleika skaltu líta á hann sem aga sem þú kaupir inn gegnum vettvang þinn: hýst uppitímavöktun, stýrða gagnagrunna og stöðusíðuverkfæri í stað sérsmíðaðs staflans. Settu eitt eða tvö SLO bundin við færslurnar sem borga reikningana og ákveddu heiðarlega hvaða bilanir myndu kosta þig viðskiptavin. Keyptu seiglu þar sem hún er ódýrari en að smíða hana og haltu rekstrarbyrðinni nógu léttri til að núverandi verkfræðingar geti borið hana samhliða eiginleikavinnu.

**Stórfyrirtæki.** Áskorunin er samræmi yfir mörg teymi: sameiginlegt SLO-orðasafn, sameiginleg villufjárhagsáætlunarstefna og framleiðsluviðbúnaðarviðmið sem hver þjónusta stenst áður en SRE tekur hana á bakvakt. Miðlægur vettvangs- og staðlahópur auk innbyggðra áreiðanleikaverkfræðinga heldur vinnubrögðum samræmdum án þess að verða flöskuháls og stjórnarhættir þurfa villufjárhagsáætlanir skýrðar og framfylgdar eins alls staðar. Fjárhagsáætlaðu vöktunarinnviðina og sjálfvirknifjárfestinguna skýrt og stýrðu áreiðanleika sem eignasafni með mælikvörðum sem forysta sér.

**Hið opinbera.** Opinber þjónusta ber oft útgefin aðgengismarkmið, lögbundnar skuldbindingar og úttektarskyldur, svo SLO og villufjárhagsáætlunarákvarðanir verða skrár sem þú ver fyrir eftirlitsaðilum. Innkaupareglur kunna að takmarka hvaða vöktun og hýsingu þú getur notað og gagnsæisvæntingar ýta þér til að birta áreiðanleikagögn á opinberu stöðumælaborði. Skipuleggðu miklar árstíðabundnar toppa eins og skattafresti og innritunarglugga bóta vikum fyrirfram og haltu eftirmálsrýnimenningu án sakbendingar svo opinberar bilanir knýi kerfisbætur frekar en sök á einstaklinga.

## Dæmi

**Sprotafyrirtæki.** Tíu manna sprotafyrirtæki rekur eitt vefforrit og deilir bakvakt yfir þrjá verkfræðinga. Frekar en að byggja áreiðanleikateymi sem það hefur ekki efni á velur það eitt marktækt SLO: 99,5 prósent árangur á innskráningar-að-mælaborði flæðinu, mælt af raunverulegum notendabeiðnum. Þegar óstöðugt API þriðja aðila byrjar að éta þá fjárhagsáætlun eyðir teymið föstudegi í að bæta við endurtilraun og skyndiminni í stað þess að afhenda næsta eiginleika, skrifar síðan tveggja málsgreina eftirmálsrýni í sameiginlegt skjal svo lagfæringin festist.

**Stórfyrirtæki.** Alþjóðlegt greiðslufyrirtæki setur 99,99 prósent aðgengis-SLO fyrir færslu-API sitt, sem gefur villufjárhagsáætlun upp á um fjórar mínútur á mánuði. Miðlægt SRE-vettvangsteymi á sameiginlega [vöktun](https://en.wikipedia.org/wiki/Observability_(software)), atvikaverkfæri og villufjárhagsáætlunarstefnuna, á meðan innbyggðir áreiðanleikaverkfræðingar vinna inni í hverjum vöruhóp. Þegar nýr svikagreiningareiginleiki brennir hálfri mánaðarfjárhagsáætlun á viku frystir fyrirfram samþykkt stefna óbrýnar útgáfur þar til áreiðanleikavinna endurheimtir svigrúm. Stjórnendur sætta sig við þetta án deilu, því þeir staðfestu stefnuna fyrirfram.

**Hið opinbera.** Landsbundið skattyfirvald rekur netframtalsþjónustu með miklum árstíðabundnum toppum í kringum árlega frestinn. SRE-teymi þess spáir eftirspurn úr fyrri árum auk mannfjölda- og stefnubreytinga, álagsprófar upp í margfalt eðlilegt hámark og útvegar afkastagetu vikum fyrirfram. Opinber SLO fyrir aðgengi og síðutöf fara á stöðumælaborð. Menning eftirmálsrýni án sakbendingar (að rýna bilanir til að bæta kerfi frekar en að kenna einstaklingum) og sjálfvirknivæðingarumboð skera jafnt og þétt handvirk inngrip sem áður réðu framtalstímabilinu og losa starfsfólk til að bæta kerfið frekar en að hjúkra því gegnum hvern frest.

## Viðskiptarök: hvatar, ávöxtun fjárfestingar og heildarkostnaður

Ávöxtun SRE kemur frá þremur uppsprettum: forðuðum niðurtíma, minni rekstrarvinnu og hraðari öruggri afhendingu. Niðurtími stórrar þjónustu getur kostað þúsundir til milljóna á klukkustund í glötuðum tekjum, viðurlögum og úrbótum, svo jafnvel hóflegar áreiðanleikabætur borga fyrir teymi fljótt. Minnkun leiðindavinnu breytir endurteknum handvirkum kostnaði í einskiptis sjálfvirknifjárfestingu, svo heildareignarkostnaður fellur eftir því sem stærð vex frekar en að klifra í takt við hana. Villufjárhagsáætlanir leyfa viðskiptunum að afhenda hraðar þegar áreiðanleiki er heilbrigður og fanga eiginleikaverðmæti sem of varfærinn rekstur myndi skilja eftir á borðinu.

Upptökukostnaðurinn er raunverulegur. SRE þarf hæfa verkfræðinga, vöktunarinnviði og menningarbreytingu sem keppir við eiginleikafresti. En kostnaður þess að taka ekki upp er hærri í stærð: ótakmarkaður rekstrarmannafli, ófyrirsjáanleg rof, kulnun starfsfólks og starfsmannavelta og orðsporsskaði sem er erfiður að magnsetja en auðvelt að verða fyrir. Til að færa rök við forystu skaltu ramma SRE sem áhættustýringu með mælanlegri ávöxtun. Settu fram núverandi kostnað atvika og handvirks reksturs, SLO-markmiðin bundin viðskiptaskuldbindingum og áætlaða minnkun beggja. Festu málflutninginn á villufjárhagsáætluninni sem stjórnarháttatóli sem gefur forystu vogarstöng á málamiðlunina milli áreiðanleika og hraða.

## Andmynstur og gildrur

- **SRE sem endurmerktur rekstur.** Að endurnefna rekstrarteymi án verkfræðitímans, sjálfvirknivæðingarumboðsins og valdsins til að standa á móti breytir engu.
- **Að stefna á 100 prósent.** Að elta fullkominn áreiðanleika sóar peningum og blokkar afhendingu fyrir ávinning sem notendur skynja ekki.
- **Hégóma-SLI.** Að mæla örgjörvanotkun þjóns í stað notendasýnilegs árangurs gefur tölur sem líta vel út á meðan notendur þjást.
- **Villufjárhagsáætlanir án tanna.** Fjárhagsáætlun sem aldrei er framfylgt þegar hún er uppurin er bara skraut.
- **Leiðindavinna án mælinga.** Ef þú rekur ekki leiðindavinnu étur hún teymið hljóðlega þar til engin umbótavinna gerist.
- **SRE sem ruslakista.** Miðlæg teymi sem erfa hverja óstöðuga þjónustu án viðbúnaðarviðmiðs drukkna í tæknilegri skuld annarra.
- **Að hunsa leiðtíma afkastagetu.** Að gera ráð fyrir að skýjateygjanleiki sé samstundis og óendanlegur býður skorti einmitt á hámörkunum sem skipta mestu.

## Þroskalíkan

**Stig 1, Upphaf.** Rekstur er handvirkur og viðbragðsdrifinn. Engin formleg SLO eru til, áreiðanleiki er skoðanamál og sömu atvik endurtaka sig á meðan slökkvivinna ræður. Öll sjálfvirkni er tilviljanakennd og enginn á áreiðanleika sem verkfræðiáhyggjuefni.

**Stig 2, Þróun.** Sumar þjónustur hafa grunn-SLI og SLO og frumstæða vöktun og viðvaranir, en vinnubrögð eru mjög ólík milli teyma. Leiðindavinna er viðurkennd en ekki mæld, sjálfvirkni er ad hoc og eftirmálsrýni gerist ósamræmt. Áreiðanleiki batnar í vösunum þar sem einstaklingar ýta honum, ekki af því skipulagsheildin krefst þess.

**Stig 3, Stöðlun.** SLI, SLO og villufjárhagsáætlunarstefna eru skjalfest og beitt samræmt yfir teymi. Leiðindavinna er skilgreind og rakin, afkastagetuáætlun er venjubundin, SRE-þátttökulíkan með framleiðsluviðbúnaðarrýni er til og sjálfvirkni er fjármagnaður vinnustraumur frekar en aukaverkefni. Áreiðanleikavenjur eru skrifaðar niður og framfylgdar um skipulagsheildina.

**Stig 4, Stjórnun.** Áreiðanleikaáætlunin er mæld og stýrð með gögnum gegn grunnlínum. Villufjárhagsáætlunarbrunahraði, leiðindavinnuhlutfall, SLO-árangur, meðaltími til endurheimtar og leiðtímar útvegunar eru rakin sem mælikvarðar, rýnd á föstum takti og notuð til að halda teymum við markmið sín. Fjárhagsáætlunarbrot ræsa samþykkta frystingu, afkastagetu er spáð gegn eftirspurnarlíkönum og hver ákvörðun um að fara eða ekki hvílir á sönnunargögnum frekar en skoðun.

**Stig 5, Samhæfing.** Áreiðanleikaverkfræði er samþætt um skipulagsheildina og stöðugt bætt. Villufjárhagsáætlunarstefna er sjálfvirk og virt alls staðar, mestur rekstur er sjálfsafgreiðsla, afkastageta er útveguð fyrirbyggjandi og áreiðanleikagögn knýja aðlögunarhæfar málamiðlanir milli hraða og stöðugleika. Skipulagsheildin endurmarkar SLO reglulega, leggur niður leiðindavinnu og endurjafnar áreiðanleikafjárfestingu eftir því sem viðskipta- og áhættumyndin breytist.

## Hugmyndir til umræðu

- Hvernig ætti skipulagsheild að setja fyrstu SLO sín þegar hún hefur engin söguleg áreiðanleikagögn til að festa þau við?
- Þegar villufjárhagsáætlunin er uppurin en stór opnun er skuldbundin, hver hefur vald til að hnekkja frystingunni og hvernig er sú ákvörðun skráð?
- Er miðlægt, innbyggt eða blendings SRE-líkan rétt fyrir skipulagsheild ykkar og hvað myndi kalla fram breytingu?
- Hvernig metið þið auka níu af aðgengi á móti eiginleikunum sem sama fjárfesting gæti fjármagnað?
- Hvað telst leiðindavinna í ykkar samhengi og hvar er línan milli verðmætrar handvirkrar dómgreindar og útrýmanlegrar endurtekningar?
- Hvernig ættu áreiðanleikamarkmið að vera ólík milli borgarasnúinnar opinberrar þjónustu og innri fyrirtækjaverkfæra?

## Helstu atriði

- SRE beitir hugbúnaðarverkfræði á rekstur og lítur á áreiðanleika sem mælanlegan, fjármagnanlegan eiginleika.
- SLI, SLO og SLA breyta áreiðanleika úr skoðun í samþykktar tölur. Haltu SLO strangari en SLA.
- Villufjárhagsáætlunin samstillir forritara og rekstraraðila með því að gera málamiðlunina milli áreiðanleika og hraða skýra og fyrirfram samda.
- Mældu og settu þak á leiðindavinnu og líttu á sjálfvirkni sem fyrsta flokks verkfræði svo rekstur skalist hægar en kerfið vex.
- Skipuleggðu afkastagetu út frá eftirspurnarspám og virtu leiðtíma útvegunar, sérstaklega fyrir árstíðabundna toppa.
- Veldu SRE-skipulagslíkan af ásetningi og skilgreindu skýra þátttöku- og framleiðsluviðbúnaðarviðmið.

## Heimildir og frekari lestur

- Betsy Beyer, Chris Jones, Jennifer Petoff, Niall Richard Murphy, *Site Reliability Engineering: How Google Runs Production Systems*
- Betsy Beyer, Niall Richard Murphy, David K. Rensin, Kent Kawahara, Stephen Thorne, *The Site Reliability Workbook: Practical Ways to Implement SRE*
- David N. Blank-Edelman (editor), *Seeking SRE: Conversations About Running Production Systems at Scale*
- Thomas A. Limoncelli, Strata R. Chalup, Christina J. Hogan, *The Practice of Cloud System Administration*
- Nicole Forsgren, Jez Humble, Gene Kim, *Accelerate: The Science of Lean Software and DevOps*
