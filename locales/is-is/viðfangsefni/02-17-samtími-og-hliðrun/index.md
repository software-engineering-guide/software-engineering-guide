# 2.17 Samtími og hliðrun

## Yfirlit og tilgangur

[Samtími](https://en.wikipedia.org/wiki/Concurrency_(computer_science)) (concurrency) er list þess að skipuleggja forrit sem sjálfstæð verkefni sem geta þokast áfram án þess að bíða hvert eftir öðru. [Hliðrun](https://en.wikipedia.org/wiki/Parallel_computing) (parallelism) er að keyra þessi verkefni í raun á sama augnabliki á mörgum örgjörvum. Munurinn er ekki smásmygli. Samtími er leið til að skipuleggja kóða svo hægt netkall frysti ekki allt forritið. Hliðrun er leið til að ljúka stórum útreikningi hraðar með því að dreifa honum yfir kjarna. Að rugla þessu tvennu saman leiðir teymi til að bæta við þráðum í von um hraða og fá aðeins galla.

Fyrir stór teymi skiptir þetta efni máli því samtími er þar sem réttleiki deyr hljóðlega. Einn höfundur sem skrifar einþráða kóða getur rökrætt um hann línu fyrir línu, en um leið og margir höfundar deila minni yfir þráða springur fjöldi mögulegra víxlana, og forrit sem stenst hvert próf getur samt brugðist einu sinni af milljón undir framleiðsluálagi, ekki með háværu hruni heldur með spilltum gögnum, föstum beiðnum og atvikum sem enginn getur endurskapað. Þessi kafli byggir á kóðastigsáherslu kafla 2.16 (afkastaverkfræði) og tölvunarfræðiundirstöðum kafla 2.13 og nærir samhæfingarvandamál kafla 3.3 (dreifð kerfi), sem er samtími yfir vélar með viðbættri grimmd óáreiðanlegs nets.

Fyrir fyrirtæki eru samtímagallar afkastagallar. Þjónustur með mikla umferð lifa eða deyja eftir getu sinni til að meðhöndla þúsundir samtímabeiðna án þess að keppa um sameiginlegt ástand, og einn ósamstilltur teljari getur spillt höfuðbók undir álagi. Fyrir hið opinbera eru hagsmunirnir réttleiki og úttektarhæfi í kerfum sem eru í rekstri í áratugi og snerta öryggi, bætur eða opinberar skrár. Kappakstursástand í skatta- eða heilbrigðiskerfi er ekki óþægindi. Það er rangt svar sem einhver verður síðar að útskýra fyrir eftirlitsaðila. Í báðum tilfellum er markmiðið það sama: gerðu örugga leiðina að sjálfgefinni, svo að fólkið mörgu sem snertir kóðann þurfi ekki hvert að vera samtímasérfræðingur.

## Meginreglur

- **Samtími er uppbygging, hliðrun er framkvæmd.** Ákveddu hvort þú þarft í raun áður en þú nærð í þræði.
- **Sameiginlegt breytilegt ástand er óvinurinn.** Næstum sérhver samtímagalli rekst til tveggja verkefna sem snerta sömu breytanlegu gögn.
- **Kjóstu óbreytileika og skilaboðasendingar.** Gögn sem geta ekki breyst er ekki hægt að keppa um og skilaboð slá sameiginlegt minni fyrir öryggi.
- **Óákvörðunarhæfi er kjarnaerfiðleikinn.** Gallinn sem birtist í einni keyrslu af þúsund er allt vandamálið, ekki jaðartilvik.
- **Settu mörk á allt.** Ótakmarkaðar biðraðir, þráðafjöldi og vinna í flugi breyta toppi í rekstrarrof.
- **Hærra stigs líkön slá hráa lása.** Leikarar, rásir og skipulagður samtími gefa mörgum höfundum örugga sjálfgefna gildið og hver lás hefur kostnað.
- **Prófaðu víxlanirnar, ekki bara gleðileiðina.** Ákvörðunarhæf próf geta ekki gripið galla sem aðeins sjaldgæf röðun afhjúpar.

## Ráðleggingar

### Ákveddu hvort þú þarft samtíma eða hliðrun

Byrjaðu á að nefna vandann. Ef þjónusta þín eyðir mestum tíma sínum í bið (eftir gagnagrunnum, netköllum eða diski) hefurðu I/O-bundið vinnuálag, og samtími er svarið: byggðu kóðann svo á meðan ein beiðni bíður þokist aðrar áfram. Einn þráður með async/await, eða lítill sjóður, getur þjónað þúsundum biðandi beiðna. Ef forritið þitt er í staðinn örgjörvabundið, malar í gegnum útreikning með lítilli bið, þá er hliðrun yfir kjarna það sem kaupir hraða, og hér er loftið sett af lögmáli Amdahls (sjá kafla 2.16): raðbundna brotið takmarkar hröðun þína sama hve mörgum kjörnum þú bætir við. Mældu í hvaða ham þú ert áður en þú hannar.

### Líttu á sameiginlegt breytilegt ástand sem óvininn

Nánast sérhver samtímagalli minnkar í sama lögun: tvö verkefni lesa og skrifa sömu breytanlegu gögn án þess að koma sér saman um röð. Þetta er [kappakstursástand](https://en.wikipedia.org/wiki/Race_condition), og það framleiðir týndar uppfærslur, hálfskrifaða hluti og gildi sem brjóta fastayrðingar sem kóðinn gerði ráð fyrir að væru öruggar. Áreiðanlegasta vörnin er að hafa minna sameiginlegt breytilegt ástand. Gefðu hverju verkefni eigin gögn, sendu afrit frekar en tilvísanir og afmarkaðu breytilegt ástand við einn eiganda sem aðrir ná til gegnum skilaboð. Þegar þú verður raunverulega að deila skaltu gera deilinguna skýra og litla, svo rýnir geti séð hvern stað þar sem ástandið er snert.

### Kjóstu óbreytileika og skilaboðasendingar sem sjálfgefin gildi

Öruggustu sameiginlegu gögnin eru gögn sem geta ekki breyst. [Óbreytanlegur hlutur](https://en.wikipedia.org/wiki/Immutable_object), þegar hann hefur verið smíðaður, má lesa af hvaða fjölda þráða sem er án nokkurrar samstillingar, því það er ekkert til að keppa um. Gerðu óbreytileika að sjálfgefnu og breytileika að yfirveguðu undantekningunni. Þegar verkefni verða að samhæfast skaltu kjósa skilaboðasendingar fram yfir sameiginlegt minni: frekar en að deila sameiginlegri breytu lætur eitt verkefni hitt fá gildið, sem er heimspekin að baki Go-málshættinum „ekki eiga samskipti með því að deila minni, deildu minni með því að eiga samskipti“. Skilaboðasending breytir ósýnilegum, röðháðum göllum í skýrt, skoðanlegt gagnaflæði, og sá skýrleiki er næstum alltaf kostnaðar á skilaboð virði í kóða sem margir viðhalda.

### Náðu í hærra stigs líkön áður en þú nærð í hráa lása

Handskrifuð læsing er rétt í kenningu og stórslys í reynd, því menn eru slæmir í að rökræða um hverja víxlun. Kjóstu líkön sem gera örugg samtíma að sjálfgefnu. [Leikaralíkanið](https://en.wikipedia.org/wiki/Actor_model) gefur hverjum leikara einkaástand og pósthólf: leikarar deila aldrei minni og senda aðeins skilaboð, svo heilir flokkar kappaksturs hverfa. [Samskiptandi raðferli](https://en.wikipedia.org/wiki/Communicating_sequential_processes) (CSP), líkanið að baki rásum í tungumálum eins og Go, lætur sjálfstæð ferli senda gildi yfir tagaðar rásir. Skipulagður samtími bindur líftíma samtímaverkefna við lesmálsgildissvið, svo verkefni geta ekki lifað blokkina sem skapaði þau og villur berast í stað þess að hverfa. Async/await leyfir þér að skrifa samtíma, I/O-bundinn kóða í raðbundnum stíl. Hvert þessara hækkar gólfið fyrir meðalhöfundinn, sem er það sem stórt teymi þarf.

### Skildu minnislíkanið þitt, ódeilanleika og sýnileika

Þegar þú deilir minni bíta tveir eiginleikar. **Ódeilanleiki** (atomicity) þýðir að aðgerð gerist öll í einu eða alls ekki. Venjuleg hækkun (`x = x + 1`) er ekki ódeilanleg, því hún les, leggur við og skrifar sem þrjú skref sem annar þráður getur truflað, sem er hvernig teljarar tapa uppfærslum. **Sýnileiki** þýðir að skrif eins þráðar verða sjáanleg öðrum. Án réttrar samstillingar getur gildi skrifað á einum kjarna setið í skyndiminni ósýnilegt öðrum, svo þráður getur lykkjað að eilífu á flaggi sem þegar var sett. Minnislíkan tungumáls þíns skilgreinir hvenær skrif verða sýnileg og hvaða raðanir þýðandinn og örgjörvinn mega endurraða, svo þú getur ekki gert ráð fyrir að kóði keyri í þeirri röð sem þú skrifaðir hann. Notaðu ódeilanlegu gerðir tungumálsins og samstillingarfrumstæður frekar en að finna upp eigið lásalaust kerfi.

### Notaðu samstillingarfrumstæður af ásetningi og hannaðu gegn pattstöðu

Þegar deiling er óumflýjanleg skaltu ná í réttu frumstæðuna og virða verð hennar. Lás eða mutex (gagnkvæm útilokun) leyfir einum þræði í einu að fara inn í mikilvægan kafla, en raðar aðgangi, svo heitur lás verður flöskuháls sem þurrkar út ávinning margra kjarna. Semafór takmarkar hve mörg verkefni mega halda áfram í einu, sem er hvernig þú setur mörk á sjóð. Ódeilanlegar aðgerðir bjóða lásalausar uppfærslur fyrir einföld gildi eins og teljara, ódýrari en lás en auðvelt að misnota fyrir allt samsett. Lásar bera þrjá klassíska bilunarhætti. [Pattstaða](https://en.wikipedia.org/wiki/Deadlock) (deadlock) er þegar verkefni bíða hvert eftir öðru í hring og ekkert getur haldið áfram, kennslubókardæmið er tveir þræðir sem hvor heldur einum lás og vill hinn. **Lifandi pattstaða** (livelock) er þegar verkefni halda áfram að bregðast hvert við öðru en þokast ekkert. **Hungur** (starvation) er þegar verkefni fær aldrei tilfang því önnur halda áfram að troðast framfyrir. Agarnir sem koma í veg fyrir þetta eru áþreifanlegir: settu altæka lásaröðun, haltu lásum stutt, bættu við tímamörkum svo fast verkefni bili hátt, kallaðu aldrei á óþekktan kóða meðan þú heldur lás og notaðu sanngjarna tímaröðun þar sem hungur er áhætta. Skrifaðu þessar reglur niður, því nýr höfundur getur ekki enduruppgötvað þær úr kóðanum einum.

### Settu mörk á biðraðir, sjóði og vinnu í flugi með bakþrýstingi

Ótakmörkuð biðröð er tímasprengja. Undir umferðartoppi berst vinna hraðar en hún tæmist, biðröðin vex án marka, minnið fyllist og þjónustan deyr á hátt sem lítur út eins og dularfullt minnisþurrðarhrun en ekki yfirálagið sem það er. Settu mörk á hverja biðröð, þak á hvern þráðasjóð og beittu [bakþrýstingi](https://en.wikipedia.org/wiki/Back_pressure): þegar kerfið er fullt skaltu gefa upp á við merki um að hægja á eða hafna vinnu hratt frekar en að taka við endalausri vinnu sem þú getur ekki lokið. Stærðarsettu sjóði að vinnuálaginu (nokkurn veginn kjarnafjöldi fyrir örgjörvabundna vinnu, hærra fyrir I/O-bundna þar sem þræðir bíða mest) og líttu á markið sem yfirvegaða afkastagetuákvörðun. Þetta tengist seigluminstrum kafla 3.3.

### Notaðu gagnahliðrun þar sem vinnan er vandræðalaust hliðrunarhæf

Sum vandamál skiptast hreint: beittu sömu aðgerð á hvert stak stórs gagnasafns, án þess að nokkurt stak byggi á öðru. Þessi gagnahliðrun er vinalegasta tegundin, því það er lítið sameiginlegt ástand til að keppa um og hröðunin getur nálgast kjarnafjöldann, eins og map-reduce leiðslur, hliðruð fylkisaðgerðir og vigurvæddur talnakóði sýna allt. Jafnvel hér skaltu virða lögmál Amdahls: sameiningar- eða fækkunarskrefið er oft raðbundið og takmarkar ávinning þinn, og yfirbygging skiptingarinnar getur ráðið fyrir lítil inntök. Náðu í það þegar vinnan á stak er veruleg og stökin eru sannarlega sjálfstæð. Annars er einfaldasta raðbundna útgáfan oft bæði nógu hröð og miklu auðveldari að halda réttri, atriði sem smíðavenjur kafla 2.9 styrkja.

### Prófaðu og villuleitaðu óákvörðunarhæfan kóða af ásetningi

Samtímagallar eru óákvörðunarhæfir, svo venjuleg próf, sem keyra eina víxlun, missa þá að mestu. Taktu á vandamálinu af ásetningi með álags- og fuzz-prófum sem keyra mörg verkefni undir slembitímasetningu til að hrista fram sjaldgæfar raðanir. Náðu í kappakstursgreina og þráðahreinsa, verkfæri sem mæla minnisaðgang til að grípa gagnakappakstur jafnvel þegar gallaða víxlunin gerðist ekki í þessari keyrslu. Þar sem vettvangur þinn býður það skaltu nota ákvörðunarhæfa hermun eða stýrða tímaraðara sem endurspila tiltekna víxlun og breyta heisenbug í endurskapanlegan galla, og hanna svo að framleiðsluhengi leyfi þér að fanga þráðaástand og lásaeign, sem tengist villuleitaraga kafla 2.15. Umfram allt skaltu kjósa hönnun (óbreytileika, skilaboðasendingar, einn eigandi) sem gerir heila flokka þessara galla ómögulega, því galli sem þú getur ekki búið til er einn sem þú þarft aldrei að villuleita.

## Málamiðlanir: kostir og gallar

| Nálgun | Kostir | Gallar |
|---|---|---|
| Sameiginlegt minni með lásum | Hratt á aðgerð, kunnuglegt | Kappaksturs-, pattstöðu- og sýnileikagallar, erfitt fyrir marga höfunda að halda réttu |
| Óbreytileiki | Engin samstilling nauðsynleg, léttvægt þráðaörugg lesning | Afritunarkostnaður, óþægilegt fyrir stórar breytilegar byggingar |
| Skilaboðasending (leikarar, rásir) | Skýrt gagnaflæði, heilir gallaflokkar hverfa | Yfirbygging á skilaboð, getur falið bakþrýsting ef biðraðir eru ótakmarkaðar |
| Async/await | Ódýr samtími fyrir I/O-bundna vinnu, raðbundið útlítandi kóði | Engin hliðrun fyrir örgjörvavinnu, að blokkera verkefni stöðvar önnur |
| Skipulagður samtími | Skýr líftími verkefna, villur berast, engin lekin verkefni | Nýrra, minna tiltækt í sumum vistkerfum |
| Gagnahliðrun | Nær línuleg hröðun á sjálfstæðri vinnu | Amdahl-loft, yfirbygging ræður fyrir lítil inntök |
| Ódeilanlegt / lásalaust | Engin lásasamkeppni fyrir einföld gildi | Ótrúlega auðvelt að fá lúmskt rangt, erfitt að rýna |

Meginspennan er öryggi gegn hráum hraða og lausnin er að kaupa réttleika fyrst og eyða afköstum aðeins þar sem mæling sannar að þú verðir. Hrá sameiginleg-minnis læsing er hraðasta á aðgerð og hættulegust á kóðalínu. Hærra stigs líkön kosta lítið af afköstum og skila miklu öryggi og skýrleika, og fyrir kóða sem margar hendur viðhalda er sú málamiðlun afdráttarlaust þess virði. Taktu frá handstillta lásalausa samtímavinnu fyrir litlu heitu blettina þar sem greinir (kafli 2.16) sannar að samhæfingaryfirbyggingin skiptir máli, og haltu jafnvel þeim á bak við vel prófuð mörk.

## Spurningar til að ræða með teyminu

1. **Fyrir upptekustu þjónustuna þína, er vinnuálagið I/O-bundið eða örgjörvabundið og passar samtímahönnun þín við það?** Teymi bæta reglulega þráðasjóðum við þjónustur sem eyða 95% tímans í bið eftir gagnagrunni og fá samkeppni en engin afköst, eða þau reyna að hliðra útreikning þar sem raðbundna brotið takmarkar hverja hröðun. Rétta hönnunin fylgir hamnum: async eða lítill sjóður fyrir biðþunga vinnu, raunveruleg hliðrun yfir kjarna fyrir útreikningsþunga vinnu. Komdu með greiningu sem sýnir hvar tíminn fer í raun, ekki forsendu, og ef mestur tími fer í útreikning skaltu mæla raðbundna brotið og láta lögmál Amdahls segja þér loftið. Svarið mótar hvort þú nærð í async, takmarkaðan sjóð eða gagnahliðrun.

2. **Hvert er sjálfgefið teymisins þíns fyrir að deila ástandi milli verkefna og er það öruggt með smíði?** Í stóru teymi skiptir sjálfgefið meira máli en undantekningarnar, því mestur kóði er skrifaður af fólki sem eru ekki samtímasérfræðingar og afrita hvaða mynstur sem þegar er til staðar. Ef sjálfgefið eru sameiginlegir breytilegir hlutir varðir af ad hoc lásum ertu einum gleymdum lás frá kappakstri sem birtist mánuðum síðar í framleiðslu. Ef sjálfgefið er óbreytileiki og skilaboðasending gerast heilir flokkar galla aldrei, og sjaldgæfi staðurinn sem raunverulega þarf sameiginlegt minni sker sig úr fyrir vandlega rýni. Ræddu hvað nýr verkfræðingur myndi ná í í dag, hvort rýni þín myndi grípa ósamstillt skrif og hvernig á að gera örugga leiðina að auðveldu leiðinni.

3. **Hvernig myndirðu finna, endurskapa og laga samtímagalla sem birtist einu sinni af milljón beiðnum í framleiðslu?** Heiðarlega svarið hjá mörgum teymum er að þau gætu það ekki, því gallinn hverfur þegar þau líta og prófin þeirra keyra aðeins eina góðkynja víxlun. Það ætti að valda þér áhyggjum, því þessir gallar spilla gögnum hljóðlega og tæra traust. Ræddu hvort þú keyrir kappakstursgreina og þráðahreinsa í samfelldri samþættingu, hvort þú álagsprófar með slembitímasetningu og hvort framleiðslusýnileiki þinn fangar þráða- og lásaástand á augnabliki hengis. Bestu teymin svara með því að gera flesta slíka galla ómögulega með vali sínu á líkani, svo fáu leifarnar séu sjaldgæfar og afmarkaðar.

4. **Hvar í kerfinu þínu er enn ótakmörkuð biðröð eða ótakmarkaður þráðasjóður og hvað gerist við hana undir skyndilegum tíföldum toppi?** Þetta skiptir máli því ótakmörkuð vinna í flugi er bilunin sem dulbýr sig sem dularfullt minnisþurrðarhrun: vinna berst hraðar en hún tæmist, minnið fyllist og þjónustan deyr og lítur út eins og vélbúnaðarbilun frekar en yfirálagið sem það er. Sjónarmiðin sem togast á eru raunveruleg, því mark sett of lágt hafnar lögmætri umferð og mark of hátt frestar hruninu í stað þess að koma í veg fyrir það, svo talan er afkastagetuákvörðun, ekki ágiskun. Komdu með skrá yfir hverja biðröð og sjóð, núverandi mörk hennar (eða viðurkenningu á að hún hafi engin), bakþrýstingshegðunina þegar hún fyllist og álagsprófasönnun um hvernig kerfið versnar við jaðarinn. Fyrir fyrirtækjaflota getur ein ótakmörkuð biðröð fossað í rekstrarrof yfir allan flotann, og fyrir opinberan vettvang sem verður að haldast tiltækur borgurum er mjúk höfnun með skýrri villu þjónustuskylda, svo markið og höfnunarleið þess tilheyra afkastagetuáætluninni og keyrsluhandbókinni, ekki minni eins verkfræðings.

5. **Hver er stefna teymisins þíns um að nota hærra stigs samtímalíkön á móti handskrifuðum lásum og hvar hefurðu leyft undantekningar?** Sjálfgefna líkanið ákvarðar hve örugg meðalbreyting er, því flestir höfundar eru ekki samtímasérfræðingar og afrita hvaða mynstur sem þegar er til: leikarar, rásir og skipulagður samtími hækka gólfið fyrir alla, á meðan hrá læsing er rétt í kenningu og uppspretta pattstaða í reynd. Spennan er sú að hærra stigs líkön kosta litla yfirbyggingu á skilaboð eða verkefni, og greinir mun stöku sinnum sanna að heit leið þarfnist handstillts lásalauss kóða, svo altækt bann er jafn rangt og frjáls-fyrir-alla. Komdu með listann yfir staði þar sem þú hefur farið fyrir neðan örugga sjálfgefna gildið, greiningarsönnunina sem réttlætti hvern og hvernig hver undantekning er girt á bak við prófuð mörk og skjalfesta lásaröðun. Í stóru fyrirtæki er þessi stefna það sem heldur þúsundum þátttakenda frá því að hver finni upp óöruggt kerfi, og í langlífu opinberu kerfi er hún það sem leyfir rýni árum síðar að skilja hvers vegna hættulegt mynstur var leyft og staðfesta að það sé enn réttlætanlegt.

6. **Þegar þú ákveður að hliðra útreikning, hvernig mælirðu raðbundna brotið og hver er ábyrgur fyrir að staðfesta að hröðunin sé raunveruleg?** Teymi dreifa reglulega útreikningi yfir kjarna og fagna tölu sem greinir myndi aldrei staðfesta, því lögmál Amdahls takmarkar ávinninginn við andhverfu raðbundna brotsins sama hve mörgum kjörnum þú bætir við, og skiptingar- og sameiningaryfirbyggingin getur þurrkað ávinninginn alveg út fyrir lítil inntök. Togið á móti er að hliðrun bætir við raunverulegri flækju og nýju kappakstursyfirborði, svo spurningin er hvort mælda hröðunin réttlætir réttleikaáhættuna sem þú tekur á þig. Komdu með greiningu sem einangrar raðbundna hlutann, inntaksstærðirnar þar sem hliðrun vinnur í raun og viðmið fyrir og eftir á dæmigerðum vélbúnaði frekar en vongóðu mati. Fyrir fyrirtæki sem borgar fyrir stóran útreikningaflota breytist heiðarleg raðbundin-brots greining í sparaðan eða sóaðan vélbúnaðarkostnað, og fyrir opinbera stofnun sem ber ábyrgð á kostnaði opinbers kerfis ætti sá sem samþykkti hliðruðu hönnunina að geta sýnt mælinguna sem réttlætti hana undir úttekt.

## Sjónarhorn eftir geirum

**Sprotafyrirtæki.** Með pínulítið teymi og ekkert svigrúm skaltu kaupa réttleika með uppbyggingu, ekki með samtímasérfræðingi sem þú getur ekki ráðið. Náðu í einu öruggu sjálfgefnu gildi sem tungumál þitt gefur þér, async/await fyrir I/O-bundna vinnu, eitt eigandi verkefni eða leikara fyrir allt sameiginlegt ástand, og slepptu handstilltri læsingu alveg. Týnd uppfærslu kappakstur á greiðsluleið getur sökkt þér hraðar en týndur eiginleiki, svo eyddu litlu aukamagni af kóða til að gera þann gallaflokk ómögulegan og haltu áfram.

**Lítið fyrirtæki.** Þú hefur engan sem starfar við samtíma, svo kjóstu vettvanga og stýrðar þjónustur sem meðhöndla hann fyrir þig: gagnagrunnsfærsla, hýst biðröð eða beiðnilíkan ramma slær þráðum sem þú viðheldur í höndunum. Þegar þú metur verkfæri skaltu líta á „gerir þetta samtíma öruggan sjálfgefið“ sem kaupa-gegn-smíða spurningu og kjósa valkostinn þar sem röng víxlun getur ekki hljóðlega spillt færslu viðskiptavinar. Haltu sameiginlegu breytilegu ástandi utan eigin kóða hvar sem takmörkuð, stýrð þjónusta getur haldið því í staðinn.

**Stórfyrirtæki.** Yfir mörg teymi er markmiðið húsa­sjálfgefið sem heldur þúsundum þátttakenda öruggum: óbreytileiki og skilaboðasending sem normið, hærra stigs líkön fram yfir hráa lása, takmarkaðar biðraðir og sjóðir með bakþrýstingi og skjalfest altæk lásaröðun. Kóðaðu þetta í verkfræðistaðla, framfylgdu með kappakstursgreinum og álagsprófum í CI og stýrðu undantekningunum þar sem greinir réttlætti lásalausan kóða svo hver haldist á bak við prófuð, rýnd mörk. Stýrðu samtímaafkastagetu sem flotamálefni með biðraðamörkum og sjóðastærðum tengdum mældu álagi.

**Hið opinbera.** Réttleiki og úttektarhæfi í kerfum sem eru í rekstri í áratugi slær hráan afköst. Krefstu þess að hver ástandsbreyting sé skráð og endurspilanleg, svo grunaður kappakstur megi endurskapa og lagfæringin sönnuð fyrir eftirlitsaðila, og haltu gervigreindarlausum ákvörðunarhæfum leiðum fyrir ákvarðanir sem snerta bætur, öryggi eða opinberar skrár. Innkaup ættu að krefjast þess að söluaðilar upplýsi samtímalíkan sitt og sönnun fyrir þekju kappakstursgreina og álagsprófa, því rangt svar undir álagi í opinberu kerfi er ekki óþægindi, það er eitthvað sem ábyrgur embættismaður verður síðar að útskýra.

## Dæmi

**Sprotafyrirtæki.** Lítið teymi afhendir greiðslueiginleika og tekur eftir að reikningsstöður reka stundum um nokkur sent undir álagi. Orsökin er venjuleg les-breyta-skrifa á stöðureit frá samtíma beiðnameðhöndlurum, týnd-uppfærsla kappakstur. Frekar en að strá lásum flytja þeir stöðu hvers reiknings á bak við eitt eigandi verkefni sem vinnur úr skuldfærslum og innfærslum sem skilaboðum, einu í einu. Reikið hverfur, kóðinn verður auðveldur að rökræða um og þeir bæta við álagsprófi sem skýtur þúsundum samtímaflutninga til að verja lagfæringuna. Ein byggingarbreyting, heill gallaflokkur lagður niður.

**Stórfyrirtæki.** Pöntunarþjónusta með mikil afköst, sem meðhöndlar tugþúsundir beiðna á sekúndu, þjáist af reglubundnum töfartoppum og stöku minnisþurrðarhrunum í umferðarbylgjum. Rannsókn finnur ótakmarkaða vinnubiðröð á bak við þráðasjóð sem vex án marka þegar eftirspurn fer yfir afkastagetu. Teymið setur mörk á biðröðina, setur þak á sjóðinn í stærð tengdri kjarnafjölda og bætir við bakþrýstingi sem hafnar umframálagi hratt með skýrri villu. Afköst verða fyrirsjáanleg, hrunin stöðvast og heitur lás á sameiginlegu skyndiminni er skipt út fyrir lásalausa byggingu aðeins eftir að greinir sannar að samkeppnin er raunveruleg. Örugg sjálfgefin gildi fyrir mörgu höfundana, stillt samtími aðeins þar sem mælt.

**Hið opinbera.** Landsbundinn bótavettvangur er í rekstri í áratugi og verður að framleiða úttektarhæfar, réttar niðurstöður jafnvel undir samtímamálauppfærslum. Teymið velur óbreytileika og skilaboðasendingar sem húsa­sjálfgefið, afmarkar hvert breytilegt ástand við einn eiganda og setur altæka lásaröðun þar sem lásar eru eftir, allt skrifað inn í verkfræðistaðlana. Þeir keyra þráðahreinsa og slembiálagspróf í leiðslunni og hanna svo að hver ástandsbreyting sé skráð og endurspilanleg fyrir eftirlit, sem leyfir þeim að endurskapa og sanna lagfæringuna þegar sjaldgæf víxlun er grunuð. Réttleiki og úttektarhæfi eru meðhöndluð sem fyrsta flokks kröfur, ekki afkastaeftiráhugsanir.

## Viðskiptarök: hvatar, ávöxtun fjárfestingar og heildarkostnaður

Ávöxtun agaðs samtíma birtist sem atvik sem aldrei gerast. Eitt framleiðslukappakstursástand getur spillt gögnum yfir þúsundir færslna, og kostnaðurinn felur bæði í sér verkfræðistundirnar til að finna galla sem felur sig þegar fylgst er með honum og miklu stærri kostnaðinn við að afstemma slæm gögn, tilkynna notendum og endurbyggja traust. Þetta eru meðal dýrustu galla að greina einmitt því þeir eru óákvörðunarhæfir, svo að elta einn heisenbug getur dvergað fyrirhöfnina við að velja öruggt líkan fyrirfram.

Ávinningurinn birtist líka í afköstum og kostnaði. Rétt stærðarsettur samtími leyfir þjónustu að meðhöndla miklu meira álag á sama vélbúnaði, endurtekinn sparnaður fyrir stóran flota, á meðan bakþrýstingur og takmarkaðar biðraðir koma í veg fyrir fossandi rekstrarrof sem breyta umferðartoppi í opinbert atvik. Heildareignarkostnaður er hóflegur og aðallega menningarlegur: þú fjárfestir í húsastíl (óbreytileika, skilaboðasendingum, skipulögðum samtíma), í verkfærum (kappakstursgreinum, þráðahreinsum, álagsbúnaði í CI) og í stöðlum sem kóða lásaröðun og takmörkun. Valkosturinn er kóðagrunnur þar sem réttleiki veltur á því að hver höfundur sé sérfræðingur að eilífu, sem ekkert vaxandi teymi getur staðið undir. Færðu rök við forystu í hennar einingum: þýddu forðaðan kappakstur í gagnaspillingaratvik forðuð, bakþrýsting í rekstrarrof komið í veg fyrir og öruggt sjálfgefið í móttökutíma sparaðan.

## Andmynstur og gildrur

- **Að bæta við þráðum fyrir hraða á I/O-bundinni vinnu.** Fleiri þræðir á biðþunga þjónustu kaupa samkeppni, ekki afköst.
- **Sameiginlegt breytilegt ástand alls staðar.** Hvaða þráður sem er sem breytir hvaða hlut sem er gerir réttleika að heppni sem enginn rýnir getur sannreynt.
- **Ótakmarkaðar biðraðir og sjóðir.** Toppur vex biðröðina þar til minnið deyr. Hrunið lítur dularfullt út en er einfalt yfirálag.
- **Ad hoc læsing án altækrar raðar.** Lásar teknir í ólíkri röð yfir kóðagrunninn pattstaða undir álagi.
- **Að gera ráð fyrir að kóði keyri í skrifaðri röð.** Að hunsa minnislíkanið, svo sýnileikagalli skilur þráð eftir snúast á úreltu gildi.
- **Handsmíðuð lásalaus snilld.** Sérsniðin lásalaus kerfi eru næstum alltaf lúmskt röng og nánast ómöguleg að rýna.
- **Að prófa aðeins gleðivíxlunina.** Ákvörðunarhæf próf standast á meðan ein-af-milljón röðunin spillir framleiðslu.
- **Að kalla á óþekktan kóða meðan lás er haldinn.** Kallbakk sem blokkar eða fer aftur inn breytir mikilvægum kafla í pattstöðu.

## Þroskalíkan

- **Stig 1, Upphaf:** Samtími er ad hoc og viðbragðsdrifinn. Þráðum og lásum er bætt við af innsæi, sameiginlegt breytilegt ástand er alls staðar og biðraðir eru ótakmarkaðar. Kappakstursástand birtist sem óendurskapanleg framleiðsluatvik sem enginn getur greint og engin verkfæri eru til að grípa þau.
- **Stig 2, Þróun:** Sum teymi hafa lært grunnvinnubrögð: þau nota lása af meiri gát og setja mörk á augljósustu biðraðir sínar. Óformleg vitund um kappakstur og pattstöður er til og nokkrar mikilvægar leiðir fá aukna skoðun. Vinnubrögð eru ósamkvæm milli teyma, prófun er enn að mestu ein-víxlun og örugg mynstur lifa í einstaklingum frekar en skriflega.
- **Stig 3, Stöðlun:** Skipulagsheildin hefur skjalfestan húsastíl framfylgt um alla skipulagsheildina: óbreytileiki og skilaboðasending sem sjálfgefin gildi, hærra stigs líkön fram yfir hráa lása, takmarkaðar biðraðir og sjóðir með bakþrýstingi og skjalfest altæk lásaröðun. Kappakstursgreinar og álagspróf keyra í CI og samtímaval fylgja því hvort vinna er I/O-bundin eða örgjörvabundin.
- **Stig 4, Stjórnun:** Skipulagsheildin mælir og stýrir samtímastöðu sinni gegn grunnlínum. Hún rekur þekju kappakstursgreina og þráðahreinsa yfir þjónustur, skráir biðraðardýpt, lásabeið, sjóðamettun og höfnunarhlutfall sem vöktuð mælikvarða og álagsprófar niðurbrotsferilinn svo sérhvert mark sé gagnabyggð afkastagetuákvörðun. Samtímaatvik eru talin og þróuð, raðbundin brot hliðraðs vinnuálags eru mæld gegn hröðuninni sem náðist í raun og ákvarðanir um áfram eða stopp á nýjum hönnunum byggja á þeim sönnunargögnum frekar en innsæi.
- **Stig 5, Samhæfing:** Öruggur samtími er leið minnstu mótstöðu fyrir hvern höfund, og vinnubrögðin eru stöðugt bætt og samþætt um skipulagsheildina. Heilir gallaflokkar eru ómögulegir með smíði, heitir blettir eru stilltir aðeins þar sem greining sannar það og ákvörðunarhæf endurspilun gerir sjaldgæfa leifargallann endurskapanlegan. Réttleiki og úttektarhæfi eru stöðugt varðir eiginleikar, afkastagetumörk aðlagast mældu álagi og staðlarnir þróast eftir því sem vettvangurinn og vinnuálagið breytast.

## Hugmyndir til umræðu

1. Ef þú úttektaðir upptekustu þjónustuna þína í dag, hve mikið af ástandi hennar er sameiginlegt og breytilegt og hve mikið af þeirri deilingu er sannarlega nauðsynlegt?
2. Hvert er sjálfgefið svar teymisins þíns þegar einhver þarf að láta tvö verkefni samhæfast og vildirðu frekar að það væri óbreytileiki eða skilaboðasending?
3. Hvar leynast ótakmarkaðar biðraðir eða ótakmarkaðir sjóðir enn í kerfinu þínu og hvað myndi gerast við þær undir skyndilegum tíföldum umferðartoppi?
4. Innihalda samfelldar samþættingarkeyrslur þínar kappakstursgreini eða þráðahreinsa og hvenær greip einn síðast eitthvað fyrir framleiðslu?
5. Fyrir mest hliðraða vinnuálagið þitt, hvert er raðbundna brotið og takmarkar lögmál Amdahls hröðunina sem þú ert í raun að elta?
6. Gæti teymið þitt endurskapað ein-af-milljón víxlunargalla eftir pöntun og hvað þyrfti til að komast þangað?

## Helstu atriði

- Samtími skipuleggur forrit sem sjálfstæð verkefni. Hliðrun keyrir þau í einu. Ákveddu hvað þú þarft áður en þú bætir við þráðum.
- Sameiginlegt breytilegt ástand er rót nánast sérhvers samtímagalla. Kjóstu óbreytileika og skilaboðasendingar sem örugg sjálfgefin gildi fyrir marga höfunda.
- Náðu í hærra stigs líkön (leikara, rásir, skipulagðan samtíma, async/await) áður en handskrifaða lása, sem eru réttir í kenningu og hættulegir í reynd.
- Skildu ódeilanleika, sýnileika og minnislíkanið þitt. Notaðu réttu frumstæðuna, haltu lásum stutt og settu altæka lásaröðun til að forðast pattstöðu, lifandi pattstöðu og hungur.
- Settu mörk á hverja biðröð og sjóð og beittu bakþrýstingi, svo toppur versni mjúklega frekar en að hrynja (kafli 3.3).
- Prófaðu víxlanirnar af ásetningi með kappakstursgreinum, álagsprófum og endurspilun (kafli 2.15) og virtu lögmál Amdahls þegar þú hliðrar (kafli 2.16).
- Fyrir fyrirtæki eru þetta afköst og forðuð atvik. Fyrir hið opinbera er það réttleiki og úttektarhæfi í langlífum kerfum.

## Heimildir og frekari lestur

- Brian Goetz et al., *Java Concurrency in Practice* (atomicity, visibility, the memory model, and safe publication).
- Herb Sutter, "The Free Lunch Is Over" (why software must embrace concurrency as clock speeds plateau).
- Leslie Lamport, "Time, Clocks, and the Ordering of Events in a Distributed System" (ordering and the foundations of concurrent reasoning).
- C. A. R. Hoare, "Communicating Sequential Processes" (*Communications of the ACM*, 1978): the CSP model behind channels.
- Carl Hewitt, Peter Bishop, and Richard Steiger, "A Universal Modular Actor Formalism for Artificial Intelligence" (the origin of the actor model).
- Edsger W. Dijkstra, "Cooperating Sequential Processes" (semaphores, mutual exclusion, and the deadlock problem).
- Maurice Herlihy and Nir Shavit, *The Art of Multiprocessor Programming* (locks, atomics, and lock-free data structures).
- Nathaniel J. Smith, "Notes on Structured Concurrency, or: Go Statement Considered Harmful" (the case for structured concurrency).
- Martin Kleppmann, *Designing Data-Intensive Applications* (concurrency and consistency where memory meets distributed systems).
- Gene M. Amdahl, "Validity of the Single Processor Approach to Achieving Large-Scale Computing Capabilities" (1967): the origin of Amdahl's law.
