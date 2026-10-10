# 3.3 Dreifð kerfi

## Yfirlit og tilgangur

[Dreift kerfi](https://en.wikipedia.org/wiki/Distributed_computing) er hvert kerfi þar sem íhlutir keyra á fleiri en einni vél og samhæfast yfir net. Um leið og þú ferð yfir ferlamörk yfir net erfirðu nokkur hörð sannindi sem eru einfaldlega ekki til innan eins ferlis. Netið er óáreiðanlegt og töf þess sveiflast. Skilaboð geta týnst, tvítekist, seinkað eða víxlast. Fjarlægir íhlutir bila á eigin vegum. Engin sameiginleg klukka er til. Klassísku „[mýtur dreifðrar tölvunar](https://en.wikipedia.org/wiki/Fallacies_of_distributed_computing)“ (netið er áreiðanlegt, töf er núll, bandvídd er óendanleg, netskipan breytist aldrei) nefna einmitt forsendurnar sem valda rekstrarrofum. Verkefni þitt er að hanna fyrir þennan veruleika frá byrjun, frekar en að enduruppgötva hann í atviki.

Fyrir stóra skipulagsheild er dreifing ekki valkvæð. Hvert kerfi sem þjónar landsstærð eða heimsstærð, tengir saman margar deildir eða þarf mikið aðgengi mun spanna margar vélar, gagnaver og oft svæði. Fyrirtæki reka dreifð færslukerfi, atburðaleiðslur og fjölsvæða uppsetningar. Ríkisstjórnir reka samþættingar milli stofnana þar sem hver stofnun á sín kerfi og enginn stýrir heildinni. Hér birtist bilið milli traustrar og brothættrar hönnunar sem rekstrarrof í fréttum, vangreiddar bætur og eftirlitsafleiðingar. Aðferðir þessa kafla (samræmisrökhugsun, [eins-áhrif](https://en.wikipedia.org/wiki/Idempotence), endurtekningar með undanhaldi, [rofar](https://en.wikipedia.org/wiki/Circuit_breaker_design_pattern), [sögur](https://en.wikipedia.org/wiki/Long-running_transaction) og dreifður sýnileiki) eru staðlaðar varnir þínar.

Erfiðasti hluti dreifðra kerfa er að bilanir eru að hluta og slitróttar. Forrit á einni vél virkar annaðhvort eða hrynur. Dreift kerfi getur verið hálfvirkt: sumar beiðnir heppnast, sumar renna út á tíma og sumar týnast hljóðlega, allt í einu. Þessi kafli beinist að rökhugsuninni og mynstrunum sem leyfa stóru teymi að smíða kerfi sem skerðast mjúklega og haldast skiljanleg undir hlutabilun.

## Meginreglur

- **Netið er ekki áreiðanlegt.** Hannaðu hvert fjarsamskipti með þeirri forsendu að þau geti verið hæg, bilað, tvítekist eða víxlast.
- **Þú getur ekki haft fullkomið samræmi og fullkomið aðgengi meðan á skiptingu stendur.** Veldu af ásetningi fyrir hver samskipti (CAP/PACELC) og mundu að töf er kostnaður jafnvel þegar engin skipting er.
- **Gerðu aðgerðir eins-áhrifa.** Ef hægt er að endurtaka aðgerð örugglega verður mestöll dreifð bilanameðhöndlun viðráðanleg.
- **Hvert fjarkall þarfnast tímamarka.** Ótakmörkuð bið breytir einu hægu ósjálfstæði í kerfisvítt rekstrarrof.
- **Kjóstu endanlegt samræmi þar sem reksturinn leyfir, en gerðu það skýrt.** Notendur og endurskoðendur verða að skilja hvenær þeir gætu séð úrelt gögn.
- **Einangraðu bilanir.** Skilrúm og rofar stöðva eitt bilandi íhlut frá því að flæða yfir í alla.
- **Þú getur ekki fundið villur í því sem þú sérð ekki.** Dreift flæði krefst samhæfðrar rekjunar, mælikvarða og skráa á hverju hoppi.
- **„Nákvæmlega-einu sinni afhending“ er goðsögn. Nákvæmlega-einu sinni *vinnsla* er verkfræðiafrek.** Hannaðu fyrir að-minnsta-kosti-einu sinni með afritunarhreinsun.

## Ráðleggingar

### Rökræddu um samræmi með CAP og PACELC

[CAP-setningin](https://en.wikipedia.org/wiki/CAP_theorem) segir að meðan á netskiptingu stendur verði kerfi að velja milli samræmis (hver lestur sér síðasta skrif) og aðgengis (hver beiðni fær svar). [PACELC](https://en.wikipedia.org/wiki/PACELC_design_principle) bætir við öðru skipti: **E**lse (þegar engin skipting er) skiptirðu enn **L**atency gegn **C**onsistency. Stimplaðu þetta ekki sem merkimiða á heilt kerfi. Ákveddu það fyrir hverja aðgerð. Millifærsla á bankainnstæðu þarfnast sterks samræmis og neitar frekar en að eiga á hættu tvíeyðslu. Samfélagsmiðlaflæði eða teljari fyrir vöruskoðanir getur sætt sig við úreldingu í skiptum fyrir aðgengi og hraða. Skrifaðu niður hvaða samræmislíkan hvert gagnaflæði notar (sterkt, orsakasamband, lestu-þín-eigin-skrif eða endanlegt) svo enginn geri ráð fyrir ábyrgð sem kerfið veitir í raun ekki.

### Smíðaðu eins-áhrif, tímamörk, endurtekningar og undanhald saman

Líttu á þessar fjórar aðferðir sem einn pakka. Gefðu hverri fjaraðgerð **tímamörk** svo hangandi ósjálfstæði geti ekki hindrað þráð að eilífu. Við bilun skaltu **reyna aftur**, en aðeins fyrir aðgerðir sem eru öruggar til endurtekningar. Öruggar til endurtekningar þýðir **eins-áhrifa**: úthlutaðu hverri beiðni einkvæmum lykli og láttu móttakandann afritunarhreinsa, svo endurtekin „gjaldfæra kort“ gjaldfæri ekki tvisvar. Dreifðu endurtekningum með **[veldisundanhaldi](https://en.wikipedia.org/wiki/Exponential_backoff) og skjálfta**, svo þú forðist samstilltan endurtekningarstorm sem breytir stuttu blikki í sjálfskaðandi [álagsárás](https://en.wikipedia.org/wiki/Denial-of-service_attack). Settu þak á fjölda endurtekninga og heildartímafjárhagsáætlun, því að reyna að eilífu flytur aðeins bilunina. Án eins-áhrifa eru endurtekningar hættulegar. Án undanhalds eru endurtekningar eyðileggjandi.

### Bættu við rofum og skilrúmum til að stöðva keðjuverkun

**Rofi** (circuit breaker) fylgist með köllum á ósjálfstæði og „opnast“ eftir þröskuld bilana: hann bilar hratt í kælitíma í stað þess að hrúga fleiri beiðnum á þjónustu sem á í erfiðleikum, og „hálfopnast“ síðan til að prófa endurheimt. Þetta stöðvar keðjuverkunina þar sem hæg niðurstraumsþjónusta tæmir þræði allra kallenda þar til allt kerfið stöðvast. **Skilrúm** (bulkheads) skipta tilföngum (þráðasjóðum, tengingasjóðum) svo mettun í einu ósjálfstæði geti ekki étið getuna sem önnur þurfa. Parið hvort tveggja við mjúka skerðingu: þegar ónauðsynlegt ósjálfstæði er óaðgengilegt skaltu skila svörum úr skyndiminni eða sjálfgefnum frekar en að láta alla beiðnina bila.

### Stýrðu dreifðum færslum með sögum, ekki tveggja þrepa framkvæmd

Þú getur yfirleitt ekki haldið einni [ACID](https://en.wikipedia.org/wiki/ACID)-færslu (Atomicity, Consistency, Isolation, Durability) yfir margar þjónustur eða gagnagrunna. Dreifð [tveggja þrepa framkvæmd](https://en.wikipedia.org/wiki/Two-phase_commit_protocol) er hæg, læsir tilföngum og skerðir aðgengi. Notaðu **söguna** (saga pattern) í staðinn. Mótaðu viðskiptafærslu sem röð staðbundinna færslna, hver gefur út atburð sem kveikir á þeirri næstu, með **bótaaðgerð** fyrir hvert skref til að afturkalla það ef síðara skref bilar. Sögur koma í tveimur bragðtegundum. **Kóreógrafía** lætur þjónustur bregðast við atburðum hver annarrar, án miðlægs stjórnanda. **Hljómsveitarstjórn** lætur miðlægan samhæfingaraðila stýra skrefunum, sem er auðveldara að rökræða um og fylgjast með. Sögur taka endanlegu samræmi opnum örmum: kerfið fer gegnum millistöður og samleitist síðan. Hannaðu því notendaupplifunina og úttektarslóðina til að gera grein fyrir „í vinnslu“ og „bættum“ ástöndum.

### Líttu á nákvæmlega-einu sinni sem að-minnsta-kosti-einu sinni plús afritunarhreinsun

[Skilaboðamiðlarar](https://en.wikipedia.org/wiki/Message_broker) geta ekki raunverulega tryggt nákvæmlega-einu sinni afhendingu yfir bilanir. Það sem þeir og þú *getið* náð er **að-minnsta-kosti-einu sinni afhending með eins-áhrifa vinnslu**, sem skilar nákvæmlega-einu sinni *áhrifum*. Hannaðu neytendur til að meðhöndla tvítekin skilaboð örugglega, með eins-áhrifalyklum eða skrá yfir unnin skilaboð. Þekktu röðunar- og afhendingarábyrgðir miðlarans nákvæmlega. Fyrir straumvinnslu skaltu nota neytendahópa, skiptingar og stöðustjórnun af ásetningi og gera endurvinnslu örugga, svo þú getir spilað straum aftur eftir galla lagfæringu án þess að spilla niðurstraumsástandi.

### Mældu dreifð flæði frá enda til enda

Taktu upp þrjár stoðir sýnileika, samhæfðar yfir þjónustumörk. Berðu **rekjunar-/fylgniauðkenni** gegnum hvert hopp, svo þú getir fylgt einni notandabeiðni yfir allar þjónusturnar sem hún snertir (dreifð rekjun). Gefðu út skipulagða **mælikvarða** (töfarhundraðshluta, villuhlutföll, mettun, afköst) á hverja þjónustu og hvert ósjálfstæði. Gefðu út skipulagðar **skrár** sem bera fylgniauðkennið. Notaðu allt þetta til að setja þjónustustigsmarkmið og til að gefa viðvörun um einkenni sem notendur finna í raun, eins og villuhlutfall og töf, frekar en aðeins um heilsu einstakra véla. Í dreifðu kerfi er sýnileiki ekki valkvæð verkfæri. Hann er eina leiðin til að skilja hegðun undir hlutabilun.

## Málamiðlanir: kostir og gallar

| Aðferð | Kostir | Gallar / kostnaður |
|---|---|---|
| Sterkt samræmi | Einfalt hugarlíkan, engir úreltir lestrar | Minna aðgengi við skiptingar, meiri töf, samhæfingarkostnaður |
| Endanlegt samræmi | Hátt aðgengi, lág töf, stigvaxandi | Úreltir lestrar, flókin rökhugsun, þarfnast lausnar árekstra |
| Endurtekningar með undanhaldi | Rífur sig sjálfvirkt gegnum tímabundnar bilanir | Magnar álag ef rangt notað, þarfnast eins-áhrifa og þaka |
| Rofar / skilrúm | Koma í veg fyrir keðjubilun, bila hratt | Aukin flækja, stilling þröskulda, hætta á ótímabærri opnun |
| Saga (á móti 2PC) | Stigvaxandi, aðgengileg, engar dreifðar læsingar | Endanlegt samræmi, bótarökfræði, erfiðari rökhugsun |

Meginmálamiðlunin er milli samhæfingar og sjálfstæðis. Sérhver ábyrgð sem þú vilt yfir vélar (samræmi, röðun, nákvæmlega-einu sinni) kostar töf, aðgengi eða flækju. Hún krefst þess að vélar séu sammála, og samkomulag yfir óáreiðanlegu neti er dýrt. Færnin er að kaupa aðeins ábyrgðirnar sem reksturinn þarfnast í raun, aðgerð fyrir aðgerð, og hanna allt annað fyrir mjúka skerðingu. Ofkaupt samræmi gerir kerfin þín hæg og brothætt. Vankaupt færðu hljóða gagnaspillingu sem birtist sem úttektarbilun mánuðum síðar.

## Spurningar til að ræða með teyminu

1. **Eru seigluminstur ykkar afhent sem sameiginleg sjálfgefin gildi vettvangsins, eða finnur hvert teymi upp tímamörk og endurtekningar að nýju?** Kaflinn lítur á eins-áhrif, tímamörk, afmarkaðar endurtekningar, rofa og rekjun sem ódýrust og áreiðanlegust þegar þau eru smíðuð einu sinni inn í sameiginleg bókasöfn og sjálfgefin gildi vettvangs. Í stórri skipulagsheild tryggir að láta hvert teymi handsmíða þau ósamræmi: sumar leiðir endurtaka ekki-eins-áhrifa aðgerðir, sumar hafa engin tímamörk, sumar gefa út ekkert fylgniauðkenni. Komdu með sönnunargögn með því að úttekta úrtak þjónusta og telja hve margar setja skýr tímamörk á hvert fjarkall og bera rekjunarauðkenni frá enda til enda. Ef sú tala er lág er lagfæringin vettvangsfjárfesting, ekki þjálfunarminnisblað. Stöðluð sjálfgefin gildi gera seiglu líka prófanlega og úttektarhæfa, sem eftirlitsaðilar í fjármálum og hjá hinu opinbera ætlast sífellt meira til að þú sýnir fram á.

2. **Samsetjast tímamörk og endurtekningarfjárhagsáætlanir yfir alla kallkeðjuna, eða endurtekur djúp beiðni sig inn í rekstrarrof?** Ein beiðni fer oft yfir mörg hopp, og ef hvert lag endurtekur sjálfstætt þrisvar með eigin tímamörkum margfaldast innsta bilunin og ytri kallandi bíður langt umfram hvaða mannlegt þolmark sem er. Settu heildartímafjárhagsáætlun fyrir notandasnúnu beiðnina og deildu henni niður keðjuna, svo innri þjónusta viti hve lítinn tíma hún á eftir og bili hratt í stað þess að endurtaka inn í storm. Komdu með ósjálfstæðisrit þitt og raunverulega rekjun, leggðu síðan saman versta tilvik tímamarka og endurtekninga og berðu saman við það sem notandinn mun í raun bíða. Veldisundanhald með skjálfta og þak á heildartilraunir heldur stuttu blikki frá því að verða sjálfskaðandi álagsárás. Djúpar, málglaðar samstilltar keðjur eru óvinurinn hér, svo svarið gæti ýtt þér í átt að ósamstilltu flæði eða færri hoppum.

3. **Hvenær sprautuðuð þið síðast inn bilunum sem hönnun ykkar fullyrðir að lifa af og hvað brást sem þið bjuggust ekki við?** Seigluminstur eru tilgátur þar til þú lætur kerfið bila af ásetningi: drepa tilvik, bæta töf á ósjálfstæði, sleppa hluta skilaboða, endurafhenda lotu tvisvar. Í dreifðu kerfi eru áhugaverðu bilanirnar að hluta og slitróttar, svo rofi eða sögubót sem lítur rétt út í kóða getur samt hegðað sér illa undir raunverulegum tímamörkum-sem-kannski-kláruðust. Komdu með niðurstöður raunverulegs leikdags eða bilanainnsprautunar, ekki hönnunarskjals, og taktu eftir hvaða viðvaranir kviknuðu, hve lengi rekjun var að staðsetja bilunina og hvort endurtekningarstormur myndaðist. Í eftirlitsskyldum geirum eru sönnunargögn um að þú hafir prófað bilun hluti af því að sýna endurskoðendum rekstrarseiglu. Hafir þú aldrei keyrt slíkt á fyrsta tilraunin heima í prófunarumhverfi með þröngt sprengjusvæði og rofa til að hætta við.

4. **Getur eigandi hvers helsta gagnaflæðis nefnt samræmislíkanið sem það veitir og passar valið við það sem reksturinn þarfnast í raun?** CAP og PACELC neyða fram yfirvegað val fyrir hverja aðgerð, samt er sjálfgefið í stórri skipulagsheild rek: flæði sem byrjaði endanlega samræmt fyrir lághagsmuna teljara er endurnýtt fyrir eitthvað sem nú samþykkir greiðslur eða veitir aðgang, og enginn endurskoðar ábyrgðina. Sjónarmiðin sem togast á eru raunveruleg, því sterkt samræmi kostar aðgengi við skiptingu og töf jafnvel þegar hún er engin, en endanlegt samræmi kaupir hraða á kostnað úreltra lestra og árekstralausnar sem þú verður að hanna fyrir. Komdu með skrá yfir helstu gagnaflæði þín, hvert merkt með núverandi líkani (sterkt, orsakasamband, lestu-þín-eigin-skrif eða endanlegt) og viðskiptaafleiðingu úrelts eða týnds lesturs, leitaðu síðan að misræmi þar sem ábyrgðin er sterkari eða veikari en hagsmunirnir réttlæta. Í fjármálum fyrirtækja og í bóta- eða auðkenniskerfum hins opinbera er endanlega samræmdur lestur á bak við valdbæra ákvörðun sú tegund hljóður galli sem birtist sem úttektarniðurstaða eða ranglát synjun mánuðum síðar, svo rýnin sjálf eru sönnunargögn sem endurskoðendur munu biðja um að sjá.

5. **Hvernig hegða fjölþjónustuviðskiptafærslur ykkar sér hálfnaðar og hver ber ábyrgð á bótunum sem afturkalla þær?** Að skipta tveggja þrepa framkvæmd út fyrir sögur þýðir að kerfið fer gegnum sýnileg millistig, og skref getur heppnast á meðan síðara skref bilar og kveikir á bótaaðgerð sem afturkallar það. Fyrir stórt teymi vekur þetta erfiðar eignarhaldsspurningar: heimila-skuldfæra-leggja inn-höfuðbók keðjan fer oft yfir nokkur teymi, og bót sem eitt teymi gleymir að útfæra skilur peninga eða skrár eftir varanlega ósamræmd. Vegðu kóreógrafíu, þar sem þjónustur bregðast við atburðum hver annarrar án miðlægs stjórnanda og flæðið er erfitt að sjá, gegn hljómsveitarstjórn, þar sem samhæfingaraðili stýrir og fylgist með skrefunum á kostnað íhlutar til að reka. Komdu með ástandsritið fyrir mikilvægustu söguna þína, lista yfir bótaaðgerðir og eigendur þeirra og sönnunargögn um að „í vinnslu“ og „bætt“ ástönd séu meðhöndluð bæði í notendaupplifun og úttektarslóð. Í bankastarfsemi og málastjórnun hins opinbera ætlast eftirlitsaðilar til að þú getir endurbyggt nákvæmlega hvað varð um færslu sem brást miðja vegu, svo ómótað millistig er regluvörslubil, ekki bara galli.

6. **Lifa skilaboðaneytendur ykkar tvítekna og víxlaða afhendingu og getið þið sannað það áður en miðlarinn neyðir spurninguna fram?** Nákvæmlega-einu sinni afhending er goðsögn, svo raunveruleg ábyrgð ykkar er að-minnsta-kosti-einu sinni, og neytandi sem gerir ráð fyrir að hvert skeyti komi einu sinni og í röð mun tvívinna daginn sem miðlarinn endurafhendir lotu eftir yfirtöku. Yfir mörg teymi safnast áhættan upp, því einn ekki-eins-áhrifa neytandi á sameiginlegum straumi getur spillt niðurstraumsástandi sem önnur teymi reiða sig á, og bilunin er ósýnileg þar til endurspilun eða skipting víxlar atburðum. Málamiðlunin er verkfræðikostnaður eins-áhrifalykla, skráar yfir unnin skilaboð og skýrrar stöðu- og skiptingarmeðhöndlunar, sett gegn kostnaði hljóðrar spillingar. Komdu með lista yfir neytendur á mikilvægum straumum þínum, taktu eftir hverjir afritunarhreinsa og hverjir aðeins vona og komdu með niðurstöðu raunverulegs endurafhendingar- eða endurspilunarprófs frekar en fullvissu um að þetta ætti að vera í lagi. Fyrir gagnaskipti milli stofnana hins opinbera og atburðaleiðslur fyrirtækja er hæfnin til að spila straum aftur örugglega eftir galla lagfæringu, án þess að búa til tvítekin mál eða gjöld, bæði rekstrarnauðsyn og eitthvað sem endurskoðendur munu vilja sjá sýnt.

## Sjónarhorn eftir geirum

**Sprotafyrirtæki.** Með tvo eða þrjá hreyfanlega hluta og ekkert vettvangsteymi stattu gegn því að smíða dreifðan vélbúnað sem þú getur ekki mannað. Keyptu seiglu þar sem hún býr í SDK sem greiðslu- eða skilaboðaveitan þín gefur þér þegar og eyddu takmarkaðri athygli þinni í mynstrin tvö sem koma í veg fyrir óafturkræfan skaða: eins-áhrifalykil á hverju peningahreyfandi eða reikningsbreytandi kalli og tímamörk með afmarkaðri endurtekningu svo flöktandi tenging geri aldrei tvöfalt. Haltu fjölda netstökka litlum, því hvert samstillt ósjálfstæði sem þú bætir við er enn eitt sem getur brugðist áður en þú hefur nokkurn á bakvakt til að taka eftir.

**Lítið fyrirtæki.** Þú hefur líklega engan dreifðra kerfa sérfræðing og þröngt fjárhagsáætlun, svo líttu á þetta sem kaupa-ekki-smíða spurningu: kjóstu stýrðar biðraðir, stýrða gagnagrunna og vettvanga sem sjá um endurtekningar, röðun og afritunarhreinsun fyrir þig frekar en innviði sem þú verður að reka. Rammaðu áhættu þína í einföldum orðum, vitandi hvaða aðgerðir myndu skaða viðskiptavin ef þær keyrðu tvisvar eða skiluðu úreltum gögnum, og kveiktu á eins-áhrifa- og að-minnsta-kosti-einu sinni eiginleikum sem söluaðilar þínir bjóða þegar. Forðastu að sauma þjónustur saman gegnum sameiginlegan gagnagrunn til að þykjast hafa færslu, því það endurskapar hljóðlega erfiðasta dreifða vandamálið án nokkurra verkfæra til að stýra því.

**Stórfyrirtæki.** Kjarnavandinn er samræmi yfir mörg teymi, svo afhentu eins-áhrif, tímamörk, afmarkaðar endurtekningar, rofa og samhæfða rekjun sem sameiginleg sjálfgefin gildi vettvangs frekar en að láta hvern hóp handsmíða þau. Staðlaðu hvernig samræmislíkön og afhendingarábyrgðir eru lýst fyrir hvert flæði, keyrðu bilanainnsprautun og leikdaga reglulega og láttu heildartímafjárhagsáætlanir samsetjast yfir djúpar kallkeðjur svo ein þjónusta geti ekki endurtekið vettvanginn inn í rekstrarrof. Stýrðu seiglu sem mældri getu með þjónustustigsmarkmiðum á notandasýnileg einkenni, því í þínum stærðum getur ein vantandi tímamörk flætt yfir í rekstrarrof í fréttum.

**Hið opinbera.** Kerfi milli stofnana þýða að enginn á heildina, svo hannaðu fyrir mörk sem þú stýrir ekki: varanlegar biðraðir með að-minnsta-kosti-einu sinni afhendingu, afritunarhreinsun á stöðugu skilaboðaauðkenni og fylgniauðkenni sem flæða yfir stofnanamörk til að gefa endurskoðendum rakningu frá enda til enda. Innkaupa- og gagnsæisreglur ýta þér til að skjalfesta samræmislíkan og afhendingarábyrgð hverrar samþættingar og til að halda valdbærum ákvörðunum (auðkenni, hæfi, bótum) á sterkt samræmdum lestrum frekar en skyndiminnisendapunktum. Líttu á sönnunargögn um prófaða bilun og endurbyggjanlega færslusögu sem afurðir, þar sem rekstrarseigla og ábyrgð gagnvart almenningi eru samnings- og lögbundnar skyldur, ekki innri þægindi.

## Dæmi

**Sprotafyrirtæki.** Lítið fjártæknisprotafyrirtæki hefur aðeins tvo hreyfanlega hluta sem tala saman yfir net: forritið sitt og greiðsluveitu þriðja aðila. Jafnvel í þessari stærð lætur það hverja gjaldbeiðni bera eins-áhrifalykil og vefur kallið í endurtekningu með undanhaldi, svo týnt svar á flöktandi tengingu gjaldfærir aldrei viðskiptavin tvisvar. Að sleppa þessu virðist ódýrt á degi eitt, en fyrsta tvöfalda gjaldfærslan sem lendir á raunverulegum notanda kostar stuðningsbruna, endurgreiðslu og beyglu á trausti sem unga fyrirtækið hefur ekki efni á.

**Stórfyrirtæki.** Alþjóðlegur samnýtingarvettvangur ferða vinnur ferðagreiðslur gegnum sögu: heimila kort, skuldfæra farþega, leggja inn hjá ökumanni, skrá höfuðbókarfærslu, hver staðbundin færsla með bótaafturköllun. Sérhvert skref ber eins-áhrifalykil, svo endurtekningar eftir nettímamörk gjaldfæra aldrei tvisvar. Köll á svikamatsþjónustuna sitja á bak við rofa. Þegar hún skerðist á álagstíma opnast rofinn og ferðir falla til baka á varfærið mat í stað þess að hindra hverja ferð. Þegar viðskiptavinur véfengir ferð leyfir dreifð rekjun verkfræðingum að fylgja henni yfir tylft þjónusta á sekúndum.

**Hið opinbera.** Landsbundin auðkennaþjónusta er notuð af mörgum stofnunum til staðfestingar. Hún býður sterkt samræmdan lestur fyrir valdbærar stöðuathuganir (þú mátt ekki samþykkja bætur gegn úreltum auðkennisgögnum), auk endanlega samræmds, skyndiminnisendapunkts fyrir fjölmargar, ónauðsynlegar uppflettingar. Gagnaskipti milli stofnana keyra yfir varanlega skilaboðaröð með að-minnsta-kosti-einu sinni afhendingu og neytandi hverrar stofnunar afritunarhreinsar á skilaboðaauðkenni, svo endurafhent færsla búi ekki til tvítekið mál. Fylgniauðkenni flæða yfir stofnanamörk og gefa endurskoðendum rakningu frá enda til enda á því hvernig gögn borgara færðust milli deilda.

## Viðskiptarök: hvatar, ávöxtun fjárfestingar og heildarkostnaður

Agi dreifðra kerfa er keyptur ódýrt og fjarvera hans er greidd hörmulega. Upptökukostnaðurinn er verkfræðitími til að smíða eins-áhrif, tímamörk, endurtekningar, rofa og rekjun inn í sameiginleg bókasöfn og sjálfgefin gildi vettvangs. Það er hófleg, að mestu einskiptis fjárfesting sem gagnast síðan hverju teymi. Kostnaðurinn við að taka það *ekki* upp er mældur í stórum rekstrarrofum: ein vantandi tímamörk sem flæða yfir í fullt vettvangsrof, ekki-eins-áhrifa greiðsluleið sem tvígjaldfærir þúsundir viðskiptavina eða sögulaus dreifð færsla sem skilur gögn eftir varanlega ósamræmd. Hvert þessara er atvik í fréttum með beinum tekju-, úrbóta- og mannorðskostnaði og, í eftirlitsskyldum geirum, sektum.

Rammaðu rökin við forystu um aðgengi og sprengjusvæði. Seiglumynstur draga beint úr bæði tíðni og lengd alvarlegra atvika, mælikvörðunum sem stjórnendur fylgjast þegar með sem uppitími og meðaltími til endurheimtar. Dreifður sýnileiki er stærsta einstaka vogarstöngin á MTTR: teymi með samhæfða rekjun leysa þvert-þjónustuatvik á broti af tímanum. Því þessa getu er best að afhenda sem sameiginleg sjálfgefin gildi vettvangs er jaðarkostnaður á hvert teymi lágur og ávinningur um alla skipulagsheildina safnast upp. Heildareignarkostnaðarrökin eru einföld: að smíða seiglu inn frá byrjun er brot af kostnaði við að bæta henni við eftir rekstrarrofið sem neyðir málið fram.

## Andmynstur og gildrur

- **Engin tímamörk.** Eitt hangandi ósjálfstæði tæmir hvern þráð og fellir allt kerfið.
- **Endurtekning ekki-eins-áhrifa aðgerða.** Tvítekin hliðaráhrif: tvöfaldar gjaldfærslur, tvítekin skrár, tvöfaldur tölvupóstur.
- **Endurtekningarstormar.** Samstilltar endurtekningar án undanhalds og skjálfta sem magna lítið blik í rekstrarrof.
- **Gert ráð fyrir nákvæmlega-einu sinni afhendingu.** Að smíða neytendur sem brotna á tvíteknum skilaboðum sem miðlarinn mun á endanum afhenda.
- **Dreifðar færslur gegnum sameiginlegan gagnagrunn.** Að tengja þjónustur gegnum einn gagnagrunn til að þykjast hafa ACID, sem endurskapar dreift einlitt kerfi.
- **Hunsun hlutabilunar.** Kóði sem gerir ráð fyrir að fjarkall heppnist fullkomlega eða bregðist fullkomlega, án meðhöndlunar fyrir „rann út á tíma en kláraðist kannski“.
- **Engin fylgniauðkenni.** Að finna villur í þvert-þjónustuatviki með því að grep-a ótengdar skrár á tíu vélum.
- **Málglaðar samstilltar kallkeðjur.** Djúp samstillt ósjálfstæðisrit þar sem eitt hægt hopp stöðvar alla beiðnina.

## Þroskalíkan

- **Stig 1: Upphaf.** Fjarköll eru meðhöndluð eins og staðbundin köll. Tímamörk vantar eða eru barnaleg, endurtekningar eru fjarverandi eða kæruleysislegar og bilanir flæða yfir kerfið. Engin sameiginleg sýn er á samræmi eða afhendingu, og að finna villur í þvert-þjónustuatviki þýðir skráagrúsk á hverri vél eftir á.
- **Stig 2: Þróun.** Sum teymi bæta við tímamörkum og grunnendurtekningum og örlitlu eins-áhrifum, en vinnubrögðin eru ósamræmd frá þjónustu til þjónustu. Skrár eru miðlægar en ekki fylgnatengdar, svo að rekja beiðni yfir hopp er handvirkt. Dreifðum færslum er vonað að virki frekar en að þær séu mótaðar, og samræmisábyrgðir búa í höfðum einstakra verkfræðinga.
- **Stig 3: Stöðlun.** Eins-áhrif, afmarkaðar endurtekningar, undanhald með skjálfta, rofar og skilrúm eru staðlað um alla skipulagsheildina gegnum sameiginleg bókasöfn. Sögur með bótaaðgerðum meðhöndla fjölþjónustufærslur, dreifð rekjun með fylgniauðkennum er til staðar og hvert helsta gagnaflæði skjalfestir samræmislíkan sitt og afhendingarábyrgð. Reglurnar eru skrifaðar niður og framfylgt um alla skipulagsheildina frekar en látnar eftir hverju teymi.
- **Stig 4: Stjórnun.** Seigla er mæld gegn grunnlínum, ekki bara til staðar. Þú rekur villuhlutfall, töfarhundraðshluta, mettun og afköst á hverja þjónustu og ósjálfstæði, fylgist með endurtekningarhlutföllum og opnunarhlutföllum rofa og setur þjónustustigsmarkmið á notandasýnileg einkenni. Staðfest er að heildartímafjárhagsáætlanir samsetjast yfir kallkeðjur, meðaltími til endurheimtar fyrir þvert-þjónustuatvik er vaktaður mælikvarði og bilanainnsprautunar- og leikdaganiðurstöður næra tölurnar sem hliða hverja breytingu.
- **Stig 5: Samhæfing.** Seigla er stöðugt bætt sjálfgefið gildi vettvangs, samþætt um alla skipulagsheildina og aðlögunarhæf að aðstæðum. Bilanainnsprautun keyrir reglulega í framleiðslu með þröngum sprengjusvæðum, kerfi skerðast mjúklega með hönnun og samræmis- og afhendingarval eru endurskoðuð eftir því sem álag og viðskiptahagsmunir breytast. Mælikvarðar Stigs 4 knýja sjálfvirk viðbrögð og stöðuga arkitektúrþróun, svo dreifða búið verður traustara með hverju atviki frekar en að lifa það bara af.

## Hugmyndir til umræðu

1. Hverjar af mikilvægum aðgerðum þínum eru í raun eins-áhrifa í dag og hverjar eru það hljóðlega ekki?
2. Getur teymið þitt, fyrir hvert helsta gagnaflæði, sagt samræmislíkanið og afhendingarábyrgðina eftir minni?
3. Hvar hefði rofi komið í veg fyrir síðasta keðjurekstrarrof þitt?
4. Hve lengi tekur það núna að rekja eina bilandi beiðni yfir allar þjónusturnar sem hún snertir?
5. Hverjar af „dreifðu færslunum“ þínum treysta í raun á heppni og hverjar eru sannar sögur með bótum?
6. Ef skilaboðamiðlarinn þinn endurafhenti öll skilaboð tvisvar í eina klukkustund, hvað myndi brotna?

## Helstu atriði

- Gerðu ráð fyrir að netið sé óáreiðanlegt og bilanir séu að hluta. Hannaðu hvert fjarsamskipti fyrir hægagang, tap, tvítekningu og víxlun.
- Ákveddu samræmi gegn aðgengi fyrir hverja aðgerð með CAP/PACELC. Skjalfestu líkanið sem hvert flæði veitir.
- Eins-áhrif, tímamörk, afmarkaðar endurtekningar og undanhald-með-skjálfta eru einn pakki. Taktu aldrei upp endurtekningar án hinna þriggja.
- Rofar og skilrúm halda bilunum í skefjum. Sögur með bótum koma í stað óframkvæmanlegra dreifðra færslna.
- Líttu á afhendingu sem að-minnsta-kosti-einu sinni og gerðu vinnslu eins-áhrifa til að ná nákvæmlega-einu sinni áhrifum.
- Samhæfð rekjun, mælikvarðar og skrár eru eina leiðin til að skilja og reka dreifð flæði.

## Heimildir og frekari lestur

- Martin Kleppmann, *Designing Data-Intensive Applications*
- Andrew Tanenbaum and Maarten van Steen, *Distributed Systems: Principles and Paradigms*
- Michael Nygard, *Release It!: Design and Deploy Production-Ready Software*
- Sam Newman, *Building Microservices*
- Chris Richardson, *Microservices Patterns* (sagas, transactional messaging)
- Eric Brewer, "CAP Twelve Years Later" and Daniel Abadi on PACELC
- Leslie Lamport, "Time, Clocks, and the Ordering of Events in a Distributed System"
- Cindy Sridharan, *Distributed Systems Observability*
- Nassim Nicholas Taleb's notion of antifragility (as applied by resilience-engineering literature)
