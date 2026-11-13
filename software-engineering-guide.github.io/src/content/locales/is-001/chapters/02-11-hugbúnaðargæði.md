# 2.11 Hugbúnaðargæði

## Yfirlit og tilgangur

[Hugbúnaðargæði](https://en.wikipedia.org/wiki/Software_quality) er hversu vel kerfi mætir yfirlýstum þörfum og sanngjörnum væntingum. Það þýðir meira en hvort það virkar: það þýðir hvort kerfið er áreiðanlegt, öruggt, viðhaldanlegt, nothæft, afkastamikið og hæft til tilgangs síns yfir tíma. Gæði eru víðtækari en prófanir. Prófanir (kafli 2.4) eru ein aðgerð sem afhjúpar galla. Gæði eru öll greinin að smíða rétta hlutinn vel og að vita, með sönnunargögnum, að þú hafir gert það. Kerfi getur staðist hvert próf og samt verið lítil gæði ef það er óviðhaldanlegt, óaðgengilegt eða illa lagað að því sem notendur þurfa í raun.

Í stóru teymi geta gæði ekki lifað í höfði einnar manneskju eða venjum eins teymis. Hundruð verkfræðinga, margar vörur og langlíf kerfi þurfa sameiginlega skilgreiningu á gæðum, skýr ferli til að tryggja þau og mælingar sem segja þér hvort þau eru að batna eða versna. Án þess verða „gæði“ óljós von sem tapar hverri deilu gegn fresti, og gallar hrannast upp þar til breyting verður hæg og áhættusöm.

Í fyrirtækja- og opinberu umhverfi hækka hagsmunirnir. Eftirlitsskyld, öryggiskritísk og borgarasnúin kerfi verða að sýna fram á gæði, ekki bara fullyrða þau: skjalfest ferli, rekjanleg sönnunargögn og sjálfstæð sannprófun eru oft skylda. Léleg gæði bera beinan fjárhags-, laga- og orðsporskostnað, og á sumum sviðum stofna þau fólki í hættu. Yfirveguð gæðagrein, byggð úr líkönum, ferlum, mælingum og menningu, er það sem breytir gæðum úr slysi í stýrða niðurstöðu.

## Meginreglur

- Gæði eru hæfni til tilgangs auk samræmis við kröfur. Skilgreindu hvort tveggja skýrt.
- Gæði eru byggð inn, ekki prófuð inn. Sannprófun finnur galla, en forvarnir forðast þá.
- Greindu á milli [gæðatryggingar](https://en.wikipedia.org/wiki/Quality_assurance) (eru ferlar okkar traustir?) og [gæðaeftirlits](https://en.wikipedia.org/wiki/Quality_control) (er þessi afurð góð?).
- Sannprófun (verification) spyr „smíðuðum við það rétt?“. Staðfesting (validation) spyr „smíðuðum við réttan hlut?“
- Mældu gæði með litlu safni marktækra mælikvarða. Líttu á mælikvarða sem merki, ekki markmið.
- Kostnaður galla vex því seinna sem hann finnst, svo færðu gæðaaðgerðir fyrr.
- Gæði eru eiginleiki allrar skipulagsheildarinnar og menningar hennar, ekki hlið í lokin.

## Ráðleggingar

### Taktu upp sameiginlegt gæðalíkan eins og ISO/IEC 25010

Gefðu skipulagsheildinni sameiginlegan orðaforða um gæði með því að taka upp viðurkennt afurðagæðalíkan. [ISO/IEC 25010](https://en.wikipedia.org/wiki/ISO/IEC_25010) skilgreinir eiginleika þar á meðal fallbundna hæfni, afkastanýtni, samhæfni, nothæfi, áreiðanleika, öryggi, viðhaldanleika og flytjanleika. Notaðu það til að gera gæði áþreifanleg: fyrir hvert kerfi skaltu ákveða hvaða eiginleikar skipta mestu og hvað „nógu gott“ þýðir fyrir hvern. Þessir afurðagæðaeiginleikar eru sömu **gæðaeiginleikar** og knýja arkitektúr (kafli 3.1). Gæði og arkitektúr eru tvær sýnir á einu áhyggjuefni, svo láttu þau deila einum forgangslista frekar en tveimur samkeppnisaðilum.

### Aðskildu gæðatryggingu frá gæðaeftirliti

Líttu á gæðatryggingu (QA) og gæðaeftirlit (QC) sem aðskildar en viðbótaraðgerðir. QA er ferlamiðuð og fyrirbyggjandi: hún bætir hvernig vinna er unnin, gegnum staðla, rýnir, skilgreiningar á „búið“ og þjálfun, svo gallar séu ólíklegri til að birtast í fyrsta lagi. QC er afurðamiðað og greinandi: það skoðar raunverulegar vinnuafurðir, svo sem prófanir, [kóðarýni](https://en.wikipedia.org/wiki/Code_review) og úttektir, til að grípa galla sem komust inn. Þroskuð skipulagsheild fjárfestir í hvoru tveggja, en hallast að QA, því að koma í veg fyrir galla er ódýrara en að finna og laga þá.

### Keyrðu skýr hugbúnaðargæðastjórnunarferli

Gerðu gæði að stýrðu ferli, ekki hljóðlátri von. Fyrir mikilvæga vinnu skaltu skrifa gæðaáætlun sem segir markgæðaeiginleikana, tryggingar- og eftirlitsaðgerðir, samþykkisviðmið og hver er ábyrgur. Vefðu hana inn í vinnubrögð sem þú hefur þegar: kóðarýni (kafli 2.5) sem bæði eftirlit og leið til að deila þekkingu, prófunarstefna (kafli 2.4) sem sjálfvirka öryggisnetið og [kyrrstæð greining](https://en.wikipedia.org/wiki/Static_program_analysis) sem samfelld skoðun. Rýndu gæðagögnin reglulega og bregstu við þróun, í stað þess að bregðast aðeins við atvikum.

### Iðkaðu sannprófun og staðfestingu sem aðskildar greinar

Sannprófun staðfestir að vinnuafurðir uppfylli tilgreiningar sínar, svo réttu inntökin í hvert stig gefi rétt úttök, gegnum rýnir, kyrrstæða greiningu og prófanir gegn kröfum. Staðfesting staðfestir að fullbúið kerfi mæti í raun þörfum notenda og fyrirhugaðri notkun, gegnum notendaprófanir, samþykkisprófanir, tilraunaverkefni og endurgjöf úr notkun. Þú þarft hvort tveggja. Kerfi getur verið rétt gagnvart gallaðri tilgreiningu (sannprófað en ekki gilt), eða það getur tekið á raunverulegri þörf en samt innihaldið galla (gilt en ekki sannprófað). Í eftirlitsskyldu umhverfi kann sjálfstæð [sannprófun og staðfesting](https://en.wikipedia.org/wiki/Verification_and_validation) (IV&V) aðila aðskilins frá hönnuðunum að vera skylda.

### Mældu gæði með marktækum mælikvörðum

Veldu lítið safn mælikvarða sem endurspegla gæðaniðurstöður og drifkrafta þeirra og fylgstu með þeim yfir tíma. Gagnlegir mælikvarðar eru gallaþéttleiki, hlutfall galla sem sleppa (gallar fundnir í framleiðslu á móti fyrir útgáfu), meðaltími til að greina og laga, bilanahlutfall breytinga, kóðaheilsumerki eins og flækja og tvítekning og staðfestingarmerki eins og notendatilkynnt vandamál og aðgengisfylgni. Forðastu hégóma- og spilanlega mælikvarða: mælikvarði sem verður markmið hættir að mæla raunveruleikann. Paraðu tölurnar við eigindleg merki úr rýnum og notendaendurgjöf.

### Einkenndu og stýrðu göllum kerfisbundið

Líttu á galla sem gögn, ekki bara elda til að slökkva. Flokkaðu þá eftir alvarleika, gerð og rótarorsök. Rektu þá frá uppgötvun til úrlausnar. Leitaðu að mynstrum svo þú getir komið í veg fyrir endurtekningu. Notaðu aðferðir eins og [rótarorsakagreiningu](https://en.wikipedia.org/wiki/Root_cause_analysis) og gallaflokkun til að greina einnota mistök frá kerfislægum veikleikum. Færðu það sem þú lærir aftur inn í QA, gegnum uppfærða staðla, viðbætt próf og bættar rýnir, svo sami flokkur galla komi ekki aftur. Galli lagaður án þess að skilja orsök hans er galli sem þú hefur boðið aftur.

### Stýrðu gæðakostnaði af ásetningi

Skildu gæðahagfræði gegnum klassísku flokkana: forvarnakostnað (þjálfun, staðla, góða hönnun, verkfæri), matskostnað (rýnir, prófanir, úttektir) og bilanakostnað (innri endurvinnsla fyrir útgáfu, auk ytri bilana sem notendur finna, sem kosta miklu meira). Færðu fjárfestingu þína í átt að forvörnum og snemmbúnu mati, því hver króna þar forðast margar krónur af bilanakostnaði síðar. Gerðu þennan kostnað sýnilegan, svo „við höfum engan tíma fyrir gæði“ sé séð fyrir það sem það er: val um að eyða meira í bilun í staðinn.

### Byggðu gæðamenningu

Gerðu gæði að ábyrgð allra, í eigu teymanna sem smíða hugbúnaðinn, frekar en að afhenda niðurstreymis QA-deild sem skoðar hann í lokin. Leiðtogar ættu að verðlauna gæðaniðurstöður, gera öruggt að tilkynna galla og næstum því slys og líta á gæðagögn sem námstæki frekar en vönd. Nálgun án sakbendingar á galla dregur vandamál í ljós snemma. Nálgun með sakbendingum felur þau þar til þau eru dýr.

## Málamiðlanir: kostir og gallar

| Vinnubrögð / val | Kostir | Gallar |
|---|---|---|
| Formlegt gæðalíkan (ISO 25010) | Sameiginlegur orðaforði, skýr forgangsröðun | Yfirbygging ef beitt kreddukennt |
| Þung gæðatrygging (forvarnir) | Færri gallar, lægri heildarkostnaður | Fjárfesting fyrirfram, hægara að sýna ávinning |
| Þungt gæðaeftirlit (skoðun) | Grípur galla sem sleppa í gegn | Dýrt, finnur galla seint |
| Sjálfstæð V&V | Há trygging, hlutlægt | Kostnaðarsamt, hægara, getur virst andstætt |
| Ríkir gæðamælikvarðar | Sýnileiki, snemmbúin viðvörun | Hætta á spilun, mælingayfirbygging |
| Sérstakt QA-teymi | Einbeiting og sérfræðiþekking | Getur velt ábyrgð af hönnuðum |
| Gæði í eigu teyma | Eignarhald, hröð endurgjöf | Krefst aga og færni alls staðar |

Meginmálamiðlunin er fjárfesting gegn tryggingu, mótuð af tímasetningu. Forvarnir kosta peninga núna til að forðast stærri bilanakostnað síðar. Svo hagfræðilega rétt gæðastig er ekki hámarkið. Það er punkturinn þar sem jaðarkostnaður meiri tryggingar jafnast á við bilanakostnaðinn sem hún forðast. Sá punktur situr hátt fyrir öryggiskritísk kerfi og lægra fyrir áhættulítil innri verkfæri. Hin endurtekna spennan er eignarhald. Miðlægir QA-hópar byggja sérfræðiþekkingu en geta leyft hönnuðum að velta ábyrgð af sér. Gæði í eigu teyma byggja eignarhald en krefjast færni og aga alls staðar.

## Spurningar til að ræða með teyminu

1. **Þegar sami flokkur galla birtist tvisvar, keyrum við rótarorsakagreiningu, eða lögum við hann bara aftur?** Galli lagaður án þess að skilja orsök hans er galli sem þú hefur boðið aftur, og í stóru teymi getur sama rótarorsök birst yfir margar þjónustur áður en nokkur tengir punktana. Að líta á galla sem gögn (flokkaða eftir alvarleika, gerð og orsök, síðan grafna eftir mynstrum) er það sem aðskilur teymi sem verður jafnt og þétt áreiðanlegra frá einu sem helst upptekið við að laga sömu mistökin. Komdu með gallaskrána þína á fundinn og leitaðu að endurteknum undirskriftum: hve mörg nýleg atvik deila orsök sem þú tókst aldrei á kerfislega? Svarið ætti að næra forvarnir, svo endurtekin orsök knýi uppfærðan staðal, nýjan sameiginlegan hjálparhlut, viðbætt próf eða betri rýnigátlista, því þannig hættir lagfæring á einum stað að leyfa öllum flokknum að koma aftur.

2. **Er öruggt í teyminu okkar að tilkynna galla eða næstum því slys og hvað verður um manneskjuna sem vekur máls á einu?** Gæði eru eiginleiki menningar, og nálgun án sakbendingar dregur vandamál í ljós snemma á meðan sakbendingarnálgun felur þau þar til þau eru dýr, sem í eftirlitsskyldu eða borgarasnúnu kerfi getur þýtt opinbera bilun eða refsingu. Þetta skiptir mestu í stórum stíl, þar sem verkfræðingurinn næst áhættunni er oft reynsluminni og hvatinn til að þegja er sterkur. Komdu með heiðarleg merki: eru næstum því slys skráð og rædd, eða hverfa þau? Nefna eftirrýni orsakir eða nefna þær fólk? Aðgerðin er að gera gæðagögn að námstæki frekar en vendi, verðlauna þá sem draga vandamál fram og halda eftirrýni án sakbendingar, því þú getur ekki komið í veg fyrir það sem teymið þitt óttast að tilkynna.

3. **Getur staðfesting í raun stöðvað útgáfu og hver hefur það vald þegar frestur nálgast?** Sannprófun (smíðuðum við það rétt?) og staðfesting (smíðuðum við réttan hlut?) eru aðskildar greinar, og staðfesting hefur aðeins tennur ef misheppnuð aðgengisathugun, misheppnað samþykkispróf eða skaðleg notendarannsókn getur raunverulega hindrað afhendingu. Í fyrirtækja- og opinberu umhverfi er þetta oft skylda, stundum gegnum sjálfstæða sannprófun og staðfestingu aðila aðskilins frá hönnuðunum, og „við afhentum það samt“ er ekki svar sem eftirlitsaðili tekur gilt. Komdu með síðustu útgáfur þínar: stöðvaði nokkurt gæðamerki nokkurn tíma eina, eða lætur hliðið alltaf undan dagsetningunni? Ef staðfesting hefur aldrei hindrað útgáfu er hún skraut, og lagfæringin er að skrifa samþykkisviðmið inn í gæðaáætlunina fyrirfram, nefna hver á ákvörðunina um áfram eða stopp og gefa þeirri ákvörðun raunverulegt vald óháð afhendingarþrýstingi.

4. **Vitum við í raun kostnað lélegra gæða okkar og erum við vísvitandi að færa útgjöld frá bilun í átt að forvörnum?** Kostnaður lélegra gæða (COPQ) er féð sem tapast í innri endurvinnslu, framleiðsluatvikum, neyðarlagfæringum, stuðningsálagi, týndum notendum og viðurlögum, og hann er næstum alltaf stærri en sýnileg útgjöld til rýna og prófana. Í stóru teymi eru bilanakostnaður dreifður yfir atvikarásir, stuðningsbiðraðir og endurvinnslu sem enginn skráir sem endurvinnslu, svo hann er ósýnilegur þar til einhver leggur hann saman. Spennan er sú að forvarnir kosta peninga núna, í fjárhagsáætlunarlotu, til að forðast bilanakostnað sem lendir síðar og á fjárhagsáætlun einhvers annars, sem gerir skiptin auðvelt að fresta að eilífu. Komdu með raunverulegar tölur: atvikafjölda og kostnað, endurvinnslutíma, hlutfall galla sem sleppa og núverandi skiptingu útgjalda yfir forvarnir, mat og bilun, og ákveddu síðan hvort blandan ætti að færast fyrr. Fyrir fyrirtækja- og opinber kerfi, þar sem mestur líftímakostnaður lendir eftir fyrstu útgáfu, skaltu leggja COPQ fyrir framan fólkið sem heldur fjárhagsáætluninni, því tala sem eftirlitsaðili getur séð er miklu erfiðari að skipta burt en óljós ákall til „gæða“.

5. **Hverjir af gæðamælikvörðum okkar hafa hljóðlega orðið markmið og hvaða hegðun knýja þeir nú?** Mælikvarði sem verður markmið hættir að mæla raunveruleikann: eltu þekjuhlutfall og þú færð próf skrifuð til að hreyfa töluna, ekki próf sem grípa galla. Í stórum stíl er þetta hættulegt, því hausmælaborð sem deilt er yfir tugi teyma setur hvata fyrir þau öll, og spilanlegur mælikvarði dreifir spiluninni alls staðar í einu. Sjónarmiðið á móti er að þú þarft enn mælingu, svo svarið er sjaldan „slepptu mælikvarðanum“ heldur „paraðu hann við mótmerki og lestu hann ásamt eigindlegum sönnunargögnum úr rýnum og frá notendum“. Komdu með núverandi mælikvarðasafn þitt og spurðu fyrir hvern þeirra hvað einhver undir þrýstingi gæti gert til að hreyfa hann án þess að bæta gæði og hvort þú hafir séð það gerast. Í eftirlitsskyldu og borgarasnúnu umhverfi skaltu vera sérstaklega varkár gagnvart samræmismælikvörðum sem líta grænir út á meðan undirliggjandi staðfesting (aðgengi, raunverulegar notendaniðurstöður) var aldrei raunverulega æfð, því endurskoðandi mun að lokum prófa raunveruleikann að baki tölunni.

6. **Hver á gæði hér: teymin sem skrifa kóðann, eða aðskilinn hópur í lokin, og hvort fjármögnum við í raun?** Eignarhald mótar allt niðurstreymis, því niðurstreymis QA-sílo leyfir hönnuðum að velta af sér ábyrgð á kóðanum sem þeir skrifa, á meðan gæði í eigu teyma byggja eignarhald á kostnað þess að krefjast færni og aga í hverju teymi. Í stóru teymi er þetta ekki annaðhvort eða: sjálfbæra mynstrið er venjulega teymi sem eiga gæði gegnum kóðarýni og sjálfvirk próf, studd af litlum miðlægum hópi sem viðheldur stöðlum, keyrir gæðatryggingu sem ferlabætur og þjálfar, frekar en að skoða gæði inn í lokin. Komdu með heiðarlegt kort af því hvar gæðavinna gerist nú, hver er ábyrgur þegar galli sleppur og hvar fjárhagsáætlun og mannafli sitja í raun á móti því hvar orðræðan segir að gæði búi. Fyrir fyrirtæki og opinberar skipulagsheildir skaltu bæta við kröfunni um sjálfstæða sannprófun og staðfestingu: sum tryggingakerfi skylda aðskilinn aðila, svo ákveddu af ásetningi hvaða stýringar tilheyra afhendingarteymunum og hverjar verða að vera sjálfstæðar til að fullnægja úttekt.

## Sjónarhorn eftir geirum

**Sprotafyrirtæki.** Hraði skiptir meira máli en helgisiðir, svo nefndu tvo eða þrjá gæðaeiginleika sem raunverulega vernda vöru þína, venjulega áreiðanleika og viðhaldanleika, og láttu fágun bíða. Eigðu gæði yfir allt teymið með kóðarýni og hóflegu sjálfvirku prófasafni frekar en að setja upp sérstakan QA-hóp sem þú getur ekki mannað. Þegar sami flokkur galla birtist tvisvar skaltu verja tuttugu mínútum í rótarorsök og bæta við einum sameiginlegum hjálparhlut auk prófs, svo forvarnir haldist ódýrar og bilanahlutfall breytinga þíns haldist lágt meðan þú hreyfir þig hratt.

**Lítið fyrirtæki.** Án sérstaks gæðasérfræðings og með þröngt fjárhagsáætlun skaltu hallast að gæðum sem eru innbyggð í verkfærin og vettvangana sem þú kaupir frekar en ferli sem þú þarft að keyra. Þegar þú velur hugbúnað skaltu líta á gæðasönnunargögn söluaðilans sem hluta af kaupunum: öryggisstöðu, aðgengi, svörun stuðnings og hve oft útgáfur þeirra brotna. Rektu handfylli af ódýrum, heiðarlegum merkjum (framleiðsluatvik, viðskiptavinatilkynnt vandamál, tími til lagfæringar) í stað íburðarmikillar mælikvarðaáætlunar sem þú hefur engan til að viðhalda.

**Stórfyrirtæki.** Verkið er samræmi yfir mörg teymi: taktu upp sameiginlegt gæðalíkan eins og ISO/IEC 25010, aðskildu gæðatryggingu (ferli) frá gæðaeftirliti (afurð) og keyrðu gæðakostnaðarrýnir sem færa útgjöld í átt að forvörnum. Haltu gæðum í eigu afhendingarteymanna, studdum af litlum miðlægum hópi sem viðheldur stöðlum og mælaborðum fyrir hlutfall galla sem sleppa, bilanahlutfall breytinga og kóðaheilsuþróun. Staðlaðu orðaforðann og hliðin svo hópar hætti að finna upp gæðavinnubrögð aftur, á meðan þú skilur eftir svigrúm fyrir teymi til að ná þeim viðmiðum á eigin hátt.

**Hið opinbera.** Innkaup, gagnsæi og almenn ábyrgð setja rammann, svo skrifaðu gæðakröfur inn í samninga og krefstu skjalfestra, rekjanlegra gæðasönnunargagna frekar en fullyrðinga. Búðu við sjálfstæðri sannprófun og staðfestingu aðila aðskilins frá hönnuðunum, skyldubundinni aðgengisfylgni og gallaskrám með alvarleika og rótarorsök sem hluta af úttektarslóðinni. Skýrðu frá kostnaðartölum lélegra gæða (endurvinnsla, kærur, þjónustubilanir) til eftirlitsaðila og gefðu staðfestingu raunverulegt vald til að hindra útgáfu sem myndi bregðast borgurunum sem treysta á hana.

## Dæmi

**Sprotafyrirtæki.** Fimm manna sprotafyrirtæki ákveður að fyrir frumvöru sína séu áreiðanleiki og viðhaldanleiki gæðaeiginleikarnir sem skipta máli og lætur pixlanákvæma fágun bíða. Gæði eru í eigu alls teymisins: kóðarýni og hóflegt sjálfvirkt prófasafn eru eftirlitin og enginn sérstakur QA-hópur er til að afhenda galla. Þegar sami flokkur villu birtist tvisvar verja þeir tuttugu mínútum í fljótlegt rótarorsakaútlit og bæta við einum sameiginlegum hjálparhlut auk prófs, svo hann hætti að endurtaka sig í stað þess að vera lagaður í höndunum í hvert skipti. Sú litla forvarnavenja heldur bilanahlutfalli breytinga þeirra lágu meðan þeir hreyfa sig enn hratt.

**Stórfyrirtæki.** Stórt fjármálaþjónustufyrirtæki tekur upp ISO/IEC 25010 sem gæðaorðaforða sinn og skráir fyrir hverja vöru markstig fyrir áreiðanleika, öryggi og viðhaldanleika. Teymi eiga gæði: kóðarýni og sjálfvirk próf eru eftirlit í leiðslunni, á meðan lítill miðlægur hópur rekur QA með því að viðhalda stöðlum og þjálfa. Gæðamælaborð rekur hlutfall galla sem sleppa, bilanahlutfall breytinga og kóðaheilsuþróun. Gallar eru flokkaðir og rótarorsakagreindir og endurteknar orsakir knýja uppfærslur á sameiginlegum bókasöfnum og gátlistum. Forystan rýnir gæðakostnaðargögn ársfjórðungslega og hefur fært útgjöld í átt að forvörnum, sem skerðir bæði framleiðsluatvik og kostnað við að laga þau.

**Hið opinbera.** Landsbundin stofnun sem afhendir borgarasnúinn bótavettvang vinnur undir tryggingakerfi sem krefst skjalfestrar gæðasönnunar. Hún rekur formlegt gæðastjórnunarferli með gæðaáætlun á hverja útgáfu, auk sjálfstæðrar sannprófunar og staðfestingar teymis aðskilins frá hönnuðunum. Sannprófun athugar hverja vinnuafurð gegn kröfum rekjanlegum til stefnu. Staðfesting felur í sér aðgengisfylgniprófanir og notendarannsóknir með raunverulegum borgurum, og hvor tveggja getur hindrað útgáfu. Gallar eru raktir með alvarleika og rótarorsök sem hluti úttektarslóðarinnar og kostnaðartölur lélegra gæða (endurvinnsla, kærur og þjónustubilanir) fara til eftirlitsaðila til að réttlæta áframhaldandi fjárfestingu í forvörnum.

## Viðskiptarök: hvatar, ávöxtun fjárfestingar og heildarkostnaður

Ávöxtun gæða er lægri heildareignarkostnaður og stöðugur afhendingarhraði. Gæðakostnaður hefur tvær hliðar. Góða útgjaldið, forvarnir og mat, er sýnilegt og stýranlegt: hönnun, staðlar, rýnir, prófanir og verkfæri. Kostnaður lélegra gæða (COPQ) er stærri en oft falinn: innri endurvinnsla, framleiðsluatvik, neyðarlagfæringar, viðskiptavinastuðningur, týndir notendur, eftirlitsviðurlög og orðsporsskaði. Rannsóknir allt frá „Quality Is Free“ eftir Crosby hafa stöðugt fundið að heildarkostnaður lélegra gæða dvergar kostnaðinn við að koma í veg fyrir þau, og að gallar verða margfalt dýrari því seinna sem þeir eru gripnir: vandamál fundið í hönnun kostar brot af sama vandamáli fundnu í framleiðslu.

Fyrir forystu eru rökin ekki „eyddu meira í gæði“. Þau eru „eyddu fyrr til að eyða minna í heild“. Magngreindu COPQ úr eigin gögnum (atvikafjölda og kostnaði, endurvinnslutíma, hlutfalli galla sem sleppa) og sýndu hvernig forvarnir og snemmbúið mat lækka hann. Tengdu gæði við viðskiptaniðurstöður: áreiðanleiki heldur viðskiptavinum, viðhaldanleiki heldur framtíðarbreytingum ódýrum og öryggi og aðgengi halda þér frá lagalegum vandræðum. Í langlífum fyrirtækja- og opinberum kerfum, þar sem mestur kostnaður lendir eftir fyrstu útgáfu, ráða viðhaldanleiki og áreiðanleiki gæða líftímakostnaði. Það gerir snemmbúna gæðafjárfestingu að einni af áhrifamestu ákvörðunum sem þú getur tekið.

## Andmynstur og gildrur

- **Gæði sem lokahlið:** að skoða gæði inn í lokin í stað þess að byggja þau inn, svo gallar finnast þegar þeir eru dýrastir.
- **Að rugla prófunum saman við gæði:** að gera ráð fyrir að staðin próf þýði mikil gæði og hunsa viðhaldanleika, nothæfi og hæfni til tilgangs.
- **QA sem aðskilið sílo:** niðurstreymis teymi sem „á gæði“ og leyfir hönnuðum að velta af sér ábyrgð á kóðanum sem þeir skrifa.
- **Mælikvarðaleikhús:** að elta þekjuhlutfall eða gallafjölda sem markmið, sem býður upp á spilun og felur raunveruleg gæði.
- **Sannprófun án staðfestingar:** að smíða tilgreininguna rétt án þess að athuga nokkurn tíma að tilgreiningin mæti raunverulegum þörfum.
- **Engin rótarorsakagreining:** að laga galla hvern fyrir sig án þess að taka á kerfislegu orsökinni, svo sami flokkur endurtekur sig.
- **Að hunsa kostnað lélegra gæða:** að líta á gæði sem hreinan kostnað því bilanakostnaður er falinn og ómældur.

## Þroskalíkan

**Stig 1 (Upphaf).** Gæði eru óskilgreind og ad hoc. Þau hvíla á samviskusemi einstaklinga, eru athuguð aðallega með handvirkum prófunum í lokin og gallar eru meðhöndlaðir viðbragðsdrifið þegar þeir birtast. Ekkert sameiginlegt líkan, engir mælikvarðar og engin lína milli tryggingar og eftirlits.

**Stig 2 (Þróun).** Grunnvinnubrögð birtast: kóðarýni, sjálfvirk próf og gallaskrá. Einhverjum gæðagögnum er safnað, en ójafnt, og hvert teymi gerir það á sinn hátt. Gæði eru enn aðallega séð sem prófanir, forvarnir eru í lágmarki, sannprófun á sér stað og staðfesting er óformleg.

**Stig 3 (Stöðlun).** Skipulagsheildin tekur upp sameiginlegt gæðalíkan (eins og ISO/IEC 25010), aðskilur QA frá QC og rekur gæðastjórnunarferli með gæðaáætlunum og samþykkisviðmiðum, skjalfest og beitt samræmt yfir teymi. Sannprófun og staðfesting eru aðskildar og yfirvegaðar og gallar eru flokkaðir og rótarorsakagreindir eftir samþykktu kerfi.

**Stig 4 (Stjórnun).** Gæði eru mæld og stýrð gegn grunnlínum. Lítið safn marktækra mælikvarða er rakið yfir tíma (gallaþéttleiki, hlutfall galla sem sleppa, meðaltími til að greina og laga, bilanahlutfall breytinga og kóðaheilsumerki eins og flækja og tvítekning) og gæðakostnaður er magngreindur yfir forvarnir, mat og bilun. Samþykkis- og gæðahlið eru framfylgd á grundvelli sönnunargagna frekar en skoðana, þróun er rýnd á föstum takti og staðfesting getur raunverulega hindrað útgáfu.

**Stig 5 (Samhæfing).** Gæði eru stöðugt bætt, menningarlega eigin grein samþætt viðskipta- og áhættuáætlun. Forvarnir eru áherslan, gæðakostnaðargögn leiða hvert fjárfesting fer og rótarorsakaniðurstöður koma kerfisbundið í veg fyrir endurtekningu. Teymi eiga gæði frá enda til enda, mælikvarðar næra stöðugar umbætur og skipulagsheildin aðlagar gæðavinnubrögð sín eftir því sem vörur, áhættur og reglugerðir breytast. Þetta samræmist hærri stigum þroskalíkana í kafla 10.8.

## Hugmyndir til umræðu

- Hvaða ISO/IEC 25010 gæðaeiginleikar skipta mestu fyrir kerfin þín og hvað er „nógu gott“ fyrir hvern?
- Hvar situr skipulagsheildin þín á forvarnir-mat-bilun útgjaldablöndunni og ætti hún að færast?
- Greinirðu sannprófun frá staðfestingu í reynd, eða þjappar þú hvoru tveggja saman í „prófanir“?
- Eiga teymin sem smíða hugbúnaðinn gæðin, eða eru þau falin aðskildum hópi, og hvað myndi breytast ef þú færðir það?
- Hver er sannur kostnaður lélegra gæða þíns og gætirðu mælt hann nógu vel til að færa viðskiptarök?
- Hverjir af gæðamælikvörðum þínum eru ósvikin merki og hverjir hafa orðið spilanleg markmið?

## Helstu atriði

- Gæði eru víðtækari en prófanir: þau eru hæfni til tilgangs auk samræmis, yfir eiginleika eins og áreiðanleika, öryggi og viðhaldanleika.
- Notaðu sameiginlegt gæðalíkan (ISO/IEC 25010) svo gæðaeiginleikar séu skýrir og samræmist arkitektúr (kafli 3.1).
- Aðskildu gæðatryggingu (fyrirbyggja, ferli) frá gæðaeftirliti (greina, afurð) og hallaðu þér að forvörnum.
- Iðkaðu sannprófun (smíðaði það rétt) og staðfestingu (smíðaði réttan hlut) sem aðskildar greinar.
- Mældu gæði með fáum marktækum mælikvörðum og einkenndu galla eftir alvarleika og rótarorsök til að koma í veg fyrir endurtekningu.
- Stýrðu gæðakostnaði: forvarnir og snemmbúið mat eru mun ódýrari en bilun, sérstaklega í langlífum kerfum.
- Byggðu gæðamenningu án sakbendingar þar sem teymi eiga gæði, studd af kóðarýni (kafli 2.5) og prófunarstefnu (kafli 2.4).

## Heimildir og frekari lestur

- IEEE Computer Society, *SWEBOK Guide (Guide to the Software Engineering Body of Knowledge)*, Software Quality knowledge area.
- ISO/IEC 25010, *Systems and software engineering: Systems and software Quality Requirements and Evaluation (SQuaRE): System and software quality models*.
- ISO/IEC 25000 series (SQuaRE), *Software product quality requirements and evaluation*.
- Philip B. Crosby, *Quality Is Free: The Art of Making Quality Certain*.
- W. Edwards Deming, *Out of the Crisis*.
- Capers Jones and Olivier Bonsignour, *The Economics of Software Quality*.
- Gerald Weinberg, *Quality Software Management*.
- ISO/IEC/IEEE 12207, *Systems and software engineering: Software life cycle processes* (quality assurance and V&V process context).
