# 3.2 Arkitektúrstílar og mynstur

## Yfirlit og tilgangur

Arkitektúrstíll er víðtæk, endurnýtanleg lögun til að skipuleggja kerfi: hvernig því er skipt upp, hvernig hlutarnir eiga samskipti og hvar mörkin liggja. Að velja einn er meðal afdrifaríkustu (og mest misskildu) ákvarðana sem stór skipulagsheild tekur. Of oft fylgir valið tísku („allir eru að nota [örþjónustur](https://en.wikipedia.org/wiki/Microservices)“) frekar en raunverulegum skorðum teymisins, lénsins og rekstrarveruleikans. Þú endar með annað tveggja óreiðu: dreift kerfi sem skipulagsheildin getur ekki rekið, eða flæktan [einlitan hugbúnað](https://en.wikipedia.org/wiki/Monolithic_application) sem enginn getur breytt örugglega. Hvorugt er stílnum að kenna. Bæði stafa af því að stíllinn passar ekki við aðstæðurnar.

Fyrir stór þróunarteymi skipta stílar mestu máli vegna [lögmáls Conways](https://en.wikipedia.org/wiki/Conway%27s_law): uppbygging kerfis hneigist til að endurspegla samskiptabyggingu skipulagsheildarinnar sem smíðar það. Arkitektúrstíll er því líka ákvörðun um skipulagshönnun. Að skipta kerfi í þjónustur er í raun ákvörðun um að skipta teymum, eignarhaldi og bakvaktarábyrgð. Fyrirtæki með hundruð verkfræðinga hafa efni á (og þurfa oft) fínkornaðar þjónustur með sjálfstæðri útgáfu, því sú sjálfstæði er hvernig mörg teymi afhenda án þess að hindra hvert annað. Þvingaðu sama mynstur upp á eitt lítið teymi og það erfir allan rekstrarskattinn án nokkurs skipulagsávinnings.

Opinbert umhverfi og fyrirtækjaumhverfi bæta við fleiri skorðum: löngum kerfislíftímum, ströngri breytingastýringu, innkaupalotum, samþættingu við rótgróin kerfi og úttektarhæfni. Þetta hallast að stílum sem halda mörkum skýrum og ósjálfstæði auðskoðanlegu. Kaflinn fer yfir helstu stíla: einlitt kerfi gegnum örþjónustur, [atburðadrifinn arkitektúr](https://en.wikipedia.org/wiki/Event-driven_architecture) með [CQRS](https://en.wikipedia.org/wiki/Command_Query_Responsibility_Segregation) og atburðauppsprettu, [þjónustunet](https://en.wikipedia.org/wiki/Service_mesh) og gáttarmynstur, [þjónustulausan rekstur](https://en.wikipedia.org/wiki/Serverless_computing) og innri aga [sexhyrnds](https://en.wikipedia.org/wiki/Hexagonal_architecture_(software)) og hreins arkitektúrs. Mikilvægara er að kaflinn hjálpar þér að segja til um hvenær hver þeirra á við.

*Sjá einnig:* kafla 2.2 (hönnunarreglur hugbúnaðar, þar á meðal [lénsdrifin hönnun](https://en.wikipedia.org/wiki/Domain-driven_design)), kafla 3.1 (grunnatriði arkitektúrs) og kafla 3.3 (dreifð kerfi).

## Meginreglur

- **Stíll fylgir kröftum, ekki tísku.** Veldu út frá stærð teymis, flækju léns, álagi og rekstrarþroska, aldrei af því að tækni er vinsæl.
- **Tenging er raunverulegi óvinurinn, ekki fjöldi útgáfueininga.** Vel einingaskipt einlitt kerfi slær dreifða drullukúlu.
- **Dreifing er kostnaður sem þú borgar fyrir sjálfstæði.** Skiptu aðeins þegar gildi sjálfstæðrar útgáfu, stigvaxtar eða bilanaeinangrunar er meira en kostnaður netkalla, hlutabilunar og gagnasamræmis yfir þjónustur.
- **Mörk ættu að fylgja viðskiptalénum.** Samstilltu þjónustur og einingar við afmarkaða samhengi (hvert sjálfstætt lénslíkan með eigin skýr mörk), ekki tæknileg lög.
- **Hannaðu innra byrðið vel óháð því ytra.** Sexhyrnd/hrein lagskipting heldur viðskiptarökfræði óháðri römmum og innviðum í hverjum stíl.
- **Lögmál Conways er óumflýjanlegt, svo notaðu það.** Hannaðu teymismörk og arkitektúr saman.
- **Byrjaðu einfaldara en þú heldur að þú þurfir.** Þú getur dregið þjónustur út úr góðu einingaskiptu einlitu kerfi. Að afdreifa ótímabært örþjónustuöngþveiti er mun erfiðara.

## Ráðleggingar

### Hafðu einingaskipt einlitt kerfi sem sjálfgefið, skiptu með sönnunargögnum

Byrjaðu flest kerfi sem eina útgáfueiningu með sterkum innri einingamörkum: skýrum viðmótum, enga seilingu inn í gögn annarrar einingar og framfylgdum ósjálfstæðisreglum. Þú færð einfaldar færslur, auðvelda endurbyggingu og eitt til að gefa út og fylgjast með. Skiptu einingu í sína eigin þjónustu aðeins þegar þú hefur áþreifanlega ástæðu: hluta sem verður að stigvaxa sjálfstætt, teymi sem þarf að gefa út á eigin takti, bilanalén sem þú verður að einangra eða tæknikröfu sem er ólík restinni. Þegar þú skiptir skaltu skipta eftir mörkum afmarkaðs samhengis svo hver þjónusta eigi sín gögn og afhjúpi stöðugan samning.

### Veistu hvenær örþjónustur vinna fyrir sér

Örþjónustur gefa þér sjálfstæða útgáfuhæfni, sjálfstæðan stigvöxt, bilanaeinangrun og frelsi til að blanda tækni. Í staðinn krefjast þær þroskaðs CI/CD (samfelldrar samþættingar og samfelldrar afhendingar), sjálfvirkra innviða, dreifðrar rekjunar, þjónustuuppgötvunar og bakvaktarmenningar. Spurðu þig heiðarlega: getur skipulagsheildin þín rekið tugi sjálfstætt útgefinna þjónusta í framleiðslu áreiðanlega? Ef vettvangurinn og rekstrarþroskinn er ekki til staðar margfalda örþjónustur aðeins bilunarhætti þína án þess að skila ávinningi sínum. Margar skipulagsheildir ná bestum árangri með handfylli grófkorna þjónusta samstilltar við helstu lén frekar en aragrúa örsmárra.

### Notaðu atburðadrifinn arkitektúr þar sem aftenging og ósamstilling borga sig

Atburðadrifinn arkitektúr leyfir framleiðendum að gefa út staðreyndir án þess að vita hverjir neyta þeirra. Það kaupir þér lausa tengingu, biðminni fyrir álagstoppa og auðvelda leið til að bæta við nýjum neytendum. Notaðu hann þar sem vinnuflæði eru náttúrulega ósamstillt og viðbragðsdrifin. **CQRS** (Command Query Responsibility Segregation) aðskilur skrifmódelið frá einu eða fleiri lesmódelum, sem hjálpar þegar les- og skrifálag eða form eru mjög ólík. **Atburðauppspretta** (event sourcing) geymir ástand sem viðbótarskrá atburða frekar en sem núverandi ástand og gefur þér fullkomna úttektarslóð og tímaferðalög. Það er öflugt fyrir fjármál og hið opinbera, þar sem „hvernig komumst við að þessu gildi?“ er lagaleg spurning, en bætir við raunverulegri flækju í útgáfustýringu atburða, endurbyggingu varpana og rökhugsun um endanlegt samræmi. Náðu í þetta af ásetningi, ekki sjálfgefið.

### Beittu gátt, BFF og nets mynstrum til að stýra mörgum þjónustum

**API-gátt** gefur ytri biðlurum einn inngangspunkt og sér um auðkenningu, hraðatakmörkun, leiðsögn og lúkningu [TLS](https://en.wikipedia.org/wiki/Transport_Layer_Security) (Transport Layer Security). **Backend-for-Frontend (BFF)** gefur hverri biðlaragerð (vef, farsíma, samstarfs-API) eigið sniðið samsafnslag, svo þú forðist uppþembt API sem hentar öllum. **Þjónustunet** færir þverlæg atriði (gagnkvæmt TLS, endurtekningar, tímamörk, umferðarfærslu og fjarmælingar) í innviðalag á hliðarvagni, svo forritateymi þurfi ekki að endurútfæra þau. Bættu neti við aðeins þegar fjöldi þjónusta gerir meðhöndlun þessara atriða á hverja þjónustu óviðráðanlega. Fyrir fáar þjónustur er net meiri rekstrarþyngd en það er þess virði.

### Vegðu þjónustulausan rekstur heiðarlega

Fall-sem-þjónusta og stýrðir þjónustulausir vettvangar taka netþjónastjórnun af þér, stigvaxa niður í núll og innheimta fyrir notkun, sem er frábært fyrir sveiflukennt, atburðadrifið eða lágt-grunnálag og fyrir lítil teymi. Málamiðlanirnar eru raunverulegar: kaldræsingartöf, takmörk á keyrslutíma og tilföngum, erfiðari staðbundin prófun, möguleg binding við söluaðila og kostnaður sem getur farið fram úr útvegðum innviðum við viðvarandi mikið magn. Notaðu þjónustulausan rekstur þar sem hagfræði hans og rekstrareinfaldleiki vinnur greinilega. Þvingaðu ekki stöðug, háafkasta kjarnakerfi í hann af ákafa.

### Haltu viðskiptarökfræði hreinni innan hverrar þjónustu

Hvað sem ytri stílnum líður skaltu halda innra byrðinu hreinu með **sexhyrndum (ports and adapters)** eða **hreinum arkitektúr**: viðskiptareglur í miðjunni sem reiða sig aðeins á ágripanir. Rammar, gagnagrunnar og skilaboðamiðlun á jöðrunum sem útskiptanlegir millistykki. Þetta heldur verðmætu lénsrökfræði þinni prófanlegri án innviða og flytjanlegri yfir tæknibreytingar: afgerandi kostur fyrir langlíf opinber kerfi og fyrirtækjakerfi sem munu lifa nokkrar kynslóðir ramma.

## Málamiðlanir: kostir og gallar

| Stíll | Best þegar | Kostir | Gallar |
|---|---|---|---|
| Einingaskipt einlitt kerfi | Flest kerfi, sérstaklega snemma | Einfaldur rekstur, auðveldar færslur og endurbygging | Ein útgáfueining, stigvaxar sem ein, hætta á veðrun |
| Örþjónustur | Mörg teymi, mikill stigvöxtur, þroskaður vettvangur | Sjálfstæð útgáfa/stigvöxtur, bilanaeinangrun | Dreifð flækja, gagnasamræmi, hár rekstrarkostnaður |
| Atburðadrifið / CQRS / atburðauppspretta | Ósamstillt vinnuflæði, úttektarþarfir, ólíkt les/skrif | Laus tenging, úttektarhæfni, stigvaxandi lestur | Endanlegt samræmi, útgáfustýring atburða, erfiðari villuleit |
| Þjónustulaus rekstur | Sveiflukennd eða lágt grunnálag, atburðadrifin vinna | Engin netþjónastjórnun, stigvöxtur niður í núll, borgað fyrir notkun | Kaldræsingar, takmörk, binding, kostnaður við mikið stöðugt álag |

Endurtekna stefið: þú kaupir sveigjanleika og sjálfstæði með rekstrar- og vitrænni flækju. Dreifðir og atburðadrifnir stílar gefa upp einfaldleika eins kallstafla og einnar færslu í skiptum fyrir getuna til að stigvaxa, gefa út og bila sjálfstætt. Sú málamiðlun borgar sig í stórum stíl og með þroskuðum vettvangi. Án hans er hún stórskaðleg. Innri agarnir (sexhyrndur/hreinn) eru nánast alltaf þess virði, því þeir kosta lítið og halda valkostum þínum opnum til að skipta um stíl síðar.

## Spurningar til að ræða með teyminu

1. **Áður en þú skiptir næstu þjónustu, muntu skipta teyminu sem á hana og hver hefur heimild til þess?** Lögmál Conways þýðir að þjónustumörk eru í raun teymismörk, svo skipting sem skipurit styður ekki framleiðir dreift einlitt kerfi: tvær útgáfueiningar, ein útgáfulest, sameiginleg bakvakt. Í stóru fyrirtæki liggur heimildin til að umskipa teymi venjulega ofar verkfræði, hjá skýrslulínum, fjármálum og mannauði, og þess vegna verður að ákveða arkitektúr og skipulagshönnun saman. Komdu með sönnunargögn í umræðuna: hefur fyrirhuguð þjónusta teymi sem getur átt hana frá enda til enda, mannað eigin bakvakt og gefið út á eigin takti? Ef svarið er nei skaltu annaðhvort fjármagna teymið eða halda getunni sem einingu í einlita kerfinu. Að skipta kóða án þess að skipta eignarhaldi kaupir allan kostnað dreifingar og ekkert af sjálfstæðinu.

2. **Getur þú gefið út hverja þjónustu þína sjálfstætt í dag, eða fara þær í leyni út í takt?** Dreifða einlita kerfið er versta niðurstaðan í þessum kafla: þú borgar fyrir netköll, hlutabilun og gagnasamræmi yfir þjónustur en getur samt ekki gefið út eina án hinna. Merkin eru sameiginlegur gagnagrunnur, sameiginlegt bókasafn sem neyðir samhæfðar uppfærslur og samþættingarpróf sem verða að keyra allt búið saman. Fyrir stórt teymi takmarkar þetta hljóðlega afköst, því hvert teymi bíður í röð á eftir einni útgáfu þó skýringarmyndin sýni sjálfstæði. Taktu eina nýlega breytingu og teldu hve margar þjónustur þurftu að fara út saman til að gera hana örugga. Ef sú tala er meiri en einn fyrir breytingu sem snerti eina getu eru mörk þín röng. Lagfæringin er venjulega að gefa hverri þjónustu eigin gögn og stöðugan, útgáfumerktan samning, ekki að bæta við fleiri þjónustum.

3. **Hver af núverandi þjónustuskiptingum þínum hefur hætt að borga sig og myndirðu sameina þær aftur?** Háþróaðasti vani kaflans er að líta á stílákvarðanir sem afturkræfar: dragðu út þegar hvati birtist og sameinaðu aftur þegar hvatinn hverfur. Flestar skipulagsheildir skipta aðeins, svo örsmáar þjónustur og málglaðar einingaþjónustur safnast upp þar til hljómsveitarstjórn og netkostnaður dverga vinnuna sem hver þjónusta vinnur. Leitaðu að þjónustum sem fara alltaf út saman, sem eru til vegna gagnagrunnstöflu frekar en viðskiptagetu eða þar sem netstökk ráða nú töf beiðni. Í fyrirtækja- og opinberum rekstri, þar sem stöðugildi og fjárhagsáætlanir eru rýndar, er að brjóta tvær þunnar þjónustur aftur í eina grófkorna lögmæt, kostnaðarsparandi hreyfing, ekki viðurkenning á ósigri. Settu endursameiningu á borðið jafn opinskátt og útdrátt og ákveddu hvort tveggja með sömu sönnunargögnum.

4. **Styður vettvangur þinn og bakvaktarþroski í raun stílinn sem þú leggur til og geturðu nefnt sérstöku götin áður en þú skuldbindur þig?** Örþjónustur, net og atburðadrifnir hryggir skila ávinningi sínum aðeins ofan á þroskuðu CI/CD, dreifðri rekjun, þjónustuuppgötvun og bakvaktarmenningu sem getur rökrætt um hlutabilun. Stór skipulagsheild ákveður gjarnan markstílinn í arkitektúrvettvangi og uppgötvar vantandi vettvang síðar, þegar tugir þjónusta eru þegar í framleiðslu og hvert atvik tekur klukkustundir að greina. Vegðu aðdráttarafl sjálfstæðrar útgáfu og stigvaxtar gegn edrú spurningunni um hver rekur þetta klukkan 3 að nóttu: sama skipting og leysir teymi til að afhenda samsíða margfaldar líka bilunarháttu sem hvert teymi verður að skilja. Komdu með heiðarlega skrá í umræðuna: núverandi útgáfutíðni, meðaltíma til endurheimtar, hvort þú hafir rekjun yfir þjónustumörk og hve margar þjónustur eitt teymi getur raunhæft rekið. Í fyrirtækja- og opinberu umhverfi skaltu bæta við innkaupa- og ráðningarfyrirvara fyrir vettvangsgetuna sem þig vantar, því stíll sem gerir ráð fyrir neti og vettvangsteymi sem þú hefur ekki fjármagnað er áætlun um að reka óviðhaldanlegt bú.

5. **Fyrir hvaða hluta lénsins er full atburðauppsprettu-úttektarslóð lagaleg nauðsyn frekar en þægindi og hver hefur heimild til að ákveða?** Atburðauppspretta og CQRS kaupa þér fullkomna, endurbyggjanlega sögu og lesmódel sem stigvaxa sjálf, en þau kosta þig útgáfustýringu atburða, endurbyggingu varpana og rökhugsun um endanlegt samræmi allan líftíma kerfisins. Sé hún beitt á lén sem þurfti aldrei úttektarslóðina er sú flækja hreinn skattur. Sé hún tekin frá léni þar sem „hvernig komumst við að þessu gildi?“ er lagaleg spurning er fjarvera hennar regluvörslubrestur. Sjónarmiðin sem togast á eru úttektarhæfni og fyrirspurnarstigvöxtur öðrum megin og erfið villuleit og vitrænt álag hönnuða hinum megin, svo ákvörðunin á heima hjá fólki sem skilur bæði reglugerðarskylduna og rekstrarbyrðina, ekki hjá þeim sem er áhugasamastur um mynstrið. Komdu með sértæku lagalegu eða samningsbundnu varðveislu- og endurbyggingarkröfurnar, væntanlegt atburðamagn og heiðarlegt mat á útgáfustýringar- og vörpunarvinnunni. Í fjármálum, skattamálum og hjá hinu opinbera, þar sem að endurbyggja ákvörðun árum síðar getur verið lögbundin skylda, skaltu nefna ábyrgan eiganda sem staðfestir að tiltekið afmarkað samhengi krefjist, eða krefjist ekki, óbreytanlegrar atburðaskrár.

6. **Hvernig muntu stöðva veðrun einingaskipta einlita kerfisins svo síðari útdráttur haldist ódýr og hvað mun framfylgja mörkunum?** Öll rökin fyrir að byrja með einingaskipt einlitt kerfi hvíla á loforðinu um að hrein innri mörk geri síðari þjónustuútdrátt viðráðanlegan, samt rotna þessi mörk hljóðlega um leið og tímamörk freista einnar einingar til að seilast í gögn annarrar. Fyrir stórt teymi með marga þátttakendur munu góður ásetningur og kóðarýni ein og sér ekki halda línunni. Án framfylgdarbúnaðar verður einlita kerfið hljóðlega að drullukúlunni sem stíllinn átti að forðast. Vegðu núninginn af framfylgdum ósjálfstæðisreglum og einingaviðmótum gegn kostnaði við að uppgötva, árum síðar, að engin mörk eru raunveruleg og hver útdráttur þýðir að greiða úr sameiginlegu ástandi. Komdu með sönnunargögn: eru einingamörk framfylgd af smíðaverkfærum, kyrrstæðri greiningu eða pakkabyggingu, eða eru þau aðeins skjalfestar venjur sem síðustu sex sameiningar hunsuðu? Í langlífum fyrirtækja- og opinberum kerfum sem verða að lifa strangar breytingastýringar og nokkrar rammakynslóðir skaltu líta á mörkaframfylgd sem úttektarhæfa stýringu, svo valkosturinn til að dreifa síðar sé sá sem þú hefur í raun varðveitt en ekki sá sem þú gerir ráð fyrir að þú eigir enn.

## Sjónarhorn eftir geirum

**Sprotafyrirtæki.** Hafðu eitt einingaskipt einlitt kerfi sem sjálfgefið og standastu aðdráttarafl örþjónusta, því knappasta auðlind þín er verkfræðiathygli og kvik þjónusta er rekstrarskattur sem þú hefur ekki efni á fyrir aðlögun vöru að markaði. Haltu hreinum einingamörkum svo þú getir dregið út síðar og náðu í þjónustulausan rekstur þar sem niðurstigvöxtur í núll og borgun fyrir notkun hentar sveiflukenndu, lágu grunnálagi þínu. Skiptu nákvæmlega einu aðeins þegar áþreifanlegur hvati birtist, eins og springandi tilkynningasendi, og aldrei fyrr.

**Lítið fyrirtæki.** Án vettvangsteymis og með þröngt fjárhagsáætlun skaltu kjósa einlitt kerfi eða handfylli grófkorna þjónusta á stýrðum vettvangi og kaupa hýsta innviði frekar en að smíða net, rekjun og þjónustuuppgötvun sjálf. Vegðu þjónustulausan rekstur og stýrða gagnagrunna sem leið til að forðast að reka netþjóna yfirleitt og vertu varkár gagnvart dreifðri hönnun þar sem þú hefur engan til að bera rekstrarbyrðina. Rétti arkitektúrinn er sá sem einn eða tveir geta í raun gefið út, fylgst með og endurheimt.

**Stórfyrirtæki.** Raunverulegi vandinn er mörg teymi og lögmál Conways: samstilltu grófkorna þjónustur við afmörkuð samhengi og teymiseignarhald og fjárfestu af ásetningi í vettvanginum (CI/CD, rekjun, neti og þjónustuuppgötvun) sem gerir dreifingu örugga. Staðlaðu gátt, BFF og innri hrein-arkitektúr mynstur svo hópar hætti að finna þau upp aftur og stýrðu útdrætti og endursameiningu sem sönnunargagnadrifnum eignasafnsákvörðunum frekar en staðbundnu vali. Fjárhagsáætlaðu rekstrarkostnað hverrar skiptingar skýrt, því í þínum stærðum er dreifða einlita kerfið dýr bilun og hæg að greiða úr.

**Hið opinbera.** Langir kerfislíftímar, ströng breytingastýring, innkaupalotur og úttektarhæfni móta valið: kjóstu stíla með skýrum, skoðanlegum mörkum og varanlegum samningum sem lifa söluaðila og rammakynslóðir. Atburðauppspretta vinnur sér inn flækju sína þar sem að endurbyggja borgarasnúna ákvörðun er lögbundin skylda, svo notaðu hana af ásetningi fyrir kjarnahöfuðbækur og haltu hreinum arkitektúr innan hverrar þjónustu til að einangra reglur sem breytast með hverju fjárlagaári. Líttu á flytjanleika og útgöngu úr séreignarlegum þjónustulausum eða söluaðilavettvöngum sem innkaupakröfur, ekki eftirþanka.

## Dæmi

**Sprotafyrirtæki.** Fjögurra manna sprotafyrirtæki sem smíðar tímaáætlunarvöru finnur fyrir þrýstingi að byrja með örþjónustur því keppinautur bloggaði um þær, en stenst. Þau afhenda eitt einingaskipt einlitt kerfi með skýrum innri mörkum (tímaáætlun, reikningagerð, tilkynningar) sem aðskildar einingar í einni útgáfueiningu, svo einn verkfræðingur getur rekið allt staðbundið og útgáfa er eitt push. Þegar varan nær fótfestu er aðeins tilkynningasendirinn, sem dreifir út í tölvupóst og SMS undir springandi álagi, dreginn í eigin þjónustu. Þau erfa ekkert af rekstrarskatti tugs þjónusta meðan þau eru enn að leita að aðlögun vöru að markaði.

**Stórfyrirtæki.** Stórt netverslunarfyrirtæki byrjar sem einingaskipt einlitt kerfi. Eftir því sem umferð vex og teymum fjölgar dregur það út hæstu álags-, mest sjálfstætt þróandi lénin (vörulista, körfu, afgreiðslu og leit) í aðskildar þjónustur, hver á sín gögn. Afgreiðsla gefur út atburði sem birgðir, afgreiðsla pantana og greiningar neyta gegnum atburðahrygg, svo nýir neytendur (svikagreining, tryggð) geta tengst án þess að snerta afgreiðslu. API-gátt sér um auðkenningu og hraðatakmörkun og BFF sníður gagnahleðslur fyrir farsíma. Lénin með minni umferð haldast í einlita kerfinu, sem forðast óþarfa sundrun.

**Hið opinbera.** Skattayfirvald smíðar álagningarvettvang á atburðauppsprettu fyrir kjarnahöfuðbókina, því sérhver breyting á skattskyldu skattgreiðanda verður að vera endurbyggjanleg og lagalega úttektarhæf árum saman. Skipanir (skila framtali, beita greiðslu, gefa út leiðréttingu) framleiða óbreytanlega atburði og lesmódel varpa núverandi stöðu fyrir fulltrúa og borgara. CQRS leyfir almenningssnúinni fyrirspurnarhliðinni að stigvaxa sjálfstætt fyrir álagstíma framtalsskila án þess að stofna skrifhliðinni í hættu. Innan hverrar þjónustu er fylgt hreinum arkitektúr, svo álagningarreglurnar, sem breytast með hverjum fjárlögum, haldast einangraðar frá geymslu- og skilaboðatækninni.

## Viðskiptarök: hvatar, ávöxtun fjárfestingar og heildarkostnaður

Fjármunirnir í húfi í stílvali eru gríðarlegir, því ákvörðunin er dýr að snúa við. Taktu upp örþjónustur of snemma og þú blæs upp heildareignarkostnað með vettvangssmíði, tvíteknum innviðum, dreifðri villuleit og þyngri rekstrarbyrði: kostnaði sem fylgir þér allan líftíma kerfisins. Neitaðu að skipta raunverulega ofhlöðnu einlitu kerfi og þú þakar afhendingarafköst: teymi bíða í röð á eftir sameiginlegri útgáfu og hver breyting stofnar öllu kerfinu í hættu. ROI-samtalið snýst í raun um að láta rekstrarútgjöld samsvara skipulagsþörf.

Færðu rökin til forystu í orðum afkasta og áhættu, ekki tækni. Sjálfstæð útgáfuhæfni þýðir fleiri teymi sem afhenda samsíða og styttri afgreiðslutíma: mælanlegan viðskiptahraða. Bilanaeinangrun þýðir færri heildarrekstrarrof og minna sprengjusvæði: mælanlegt aðgengi og mannorðsvernd. En vertu jafn heiðarlegur um vettvangsfjárfestinguna sem hver stíll krefst: net, rekjun og CI/CD-þroski eru forsendur, ekki valkvæðar viðbætur, og kostnaður þeirra á heima í heildareignarkostnaði. Fyrir margar skipulagsheildir er ódýrasta leiðin vel einingaskipt einlitt kerfi núna, með hreinum innri mörkum sem gera síðari útdrátt ódýran. Það kaupir þér valkostinn til að dreifa án þess að borga fyrir hann áður en þú þarft hann.

## Andmynstur og gildrur

- **Dreift einlitt kerfi.** Þjónustur sem verður að gefa út saman og deila gagnagrunni: allur kostnaður dreifingar, ekkert af sjálfstæðinu.
- **Nanóþjónustur.** Þjónustur svo fínkornaðar að hljómsveitarstjórn og netkostnaður dverga vinnuna sem þær vinna.
- **Örþjónustur án vettvangs.** Að skipta áður en þú hefur CI/CD, rekjun og bakvaktarþroska. Bilunarhættir margfaldast.
- **Einingaþjónustur.** Að skipta eftir gagnagrunnstöflu („Notendaþjónusta“, „Pöntunarþjónusta“) í stað viðskiptagetu, sem neyðir fram málglöð þvert-þjónustukall fyrir hverja aðgerð.
- **Atburðauppspretta alls staðar.** Að beita henni á lén sem þurfa ekki úttektarslóð og borga flækjuskattinn fyrir engan ávinning.
- **Gátt sem einlitt kerfi.** Að setja viðskiptarökfræði í API-gáttina og endurskapa miðlægan flöskuháls.
- **Rammatengdur kjarni.** Viðskiptarökfræði flækt við vef- eða ORM-rammann (object-relational mapping), sem gerir bæði prófun og tæknibreytingu sársaukafulla.

## Þroskalíkan

- **Stig 1: Upphaf.** Stíll er valinn af tísku eða slysni. Þú hefur eitt flækt einlitt kerfi eða tilviljanakennda dreifða óreiðu, mörk fylgja tæknilögum eða sögu frekar en léninu og skipting gerist viðbragðsdrifið þegar eitthvað bilar.
- **Stig 2: Þróun.** Sum teymi draga yfirveguð einingamörk innan einlita kerfisins eða setja upp nokkrar grófkorna þjónustur og sum þverlæg atriði eru meðhöndluð samræmt. Vinnubrögð eru ójöfn: einn hópur samstillir þjónustur við afmörkuð samhengi á meðan annar skiptir enn eftir gagnagrunnstöflu og útdráttur er áfram ad hoc.
- **Stig 3: Stöðlun.** Skjalfest nálgun er framfylgt um alla skipulagsheildina: þjónustur samstillast afmörkuðum samhengjum og eiga sín gögn, gátt og BFF mynstur eru notuð þar sem við á, innri hrein eða sexhyrnd lagskipting er staðallinn og hver skipting krefst yfirlýsts hvata. Einingamörk eru framfylgd með verkfærum, ekki bara venju.
- **Stig 4: Stjórnun.** Stílákvarðanir eru mældar og stýrðar gegn grunnlínum. Þú rekur útgáfutíðni og afgreiðslutíma á hverja þjónustu, meðaltíma til endurheimtar, hve margar þjónustur verða að fara út saman fyrir dæmigerða breytingu og netstökkstöf, og þú berð kostnað hverrar skiptingar saman við sjálfstæðið sem henni var ætlað að kaupa. Sönnunargögn, ekki kjör, ráða hvort mörk lifa og rek í átt að dreifðu einlitu kerfi er gripið af mælikvörðum en ekki rekstrarrofi.
- **Stig 5: Samhæfing.** Arkitektúr er samþættur skipulagshönnun og stöðugt aðlagaður. Þroskaður vettvangur (CI/CD, rekjun og net þar sem réttlætanlegt) gerir bæði dreifingu og endursameiningu ódýra, teymi draga reglulega út þegar hvati birtist og brjóta þjónustur aftur saman þegar hann hverfur og stílval eru endurjöfnuð eftir því sem teymisbygging, álag og áhættumynd breytast yfir allt búið.

## Hugmyndir til umræðu

1. Hvar í kerfinu þínu er einlitt kerfi í raun styrkur og hvar er það raunverulegur flöskuháls?
2. Hvaða áþreifanlegi hvati myndi réttlæta að draga út næstu þjónustu þína og geturðu nefnt hann áður en þú smíðar hana?
3. Hefur skipulagsheildin þín rekstrarþroskann sem örþjónustur krefjast? Hvað vantar?
4. Fyrir hvaða hluta lénsins þíns er full atburðauppsprettu-úttektarslóð lagaleg eða viðskiptaleg nauðsyn á móti þægilegt að hafa?
5. Hve vel spegla núverandi þjónustumörk þín teymismörkin og hjálpar sú samstilling eða skaðar?
6. Ef þú þyrftir að skipta um veframma eða gagnagrunn á næsta ári, hve mikið af viðskiptarökfræði þinni þyrftirðu að endurskrifa?

## Helstu atriði

- Veldu arkitektúrstíl út frá raunverulegum kröftum (stærð teymis, léni, álagi, rekstrarþroska), ekki út frá tísku.
- Einingaskipt einlitt kerfi er rétta sjálfgefna valið fyrir flest kerfi. Dragðu aðeins út þjónustur með áþreifanlegum hvata og eftir mörkum afmarkaðs samhengis.
- Örþjónustur skipta rekstrar- og vitrænni flækju fyrir sjálfstæða útgáfu, stigvöxt og bilanaeinangrun. Þær krefjast þroskaðs vettvangs.
- Atburðadrifið, CQRS og atburðauppspretta bjóða aftengingu og úttektarhæfni á kostnað endanlegs samræmis og útgáfustýringarflækju. Taktu upp af ásetningi.
- Gáttir, BFF og net temja bú margra þjónusta en bæta við þyngd. Kynntu þau þegar umfang krefst, ekki fyrr.
- Beittu sexhyrndum/hreinum arkitektúr innan hverrar þjónustu til að halda verðmætri viðskiptarökfræði prófanlegri og varanlegri yfir tæknibreytingar.

## Heimildir og frekari lestur

- Sam Newman, *Building Microservices* and *Monolith to Microservices*
- Chris Richardson, *Microservices Patterns*
- Eric Evans, *Domain-Driven Design*
- Vaughn Vernon, *Implementing Domain-Driven Design*
- Robert C. Martin, *Clean Architecture*
- Alistair Cockburn, "Hexagonal Architecture (Ports and Adapters)"
- Gregor Hohpe and Bobby Woolf, *Enterprise Integration Patterns*
- Martin Fowler, *Patterns of Enterprise Application Architecture* (and articles on CQRS and Event Sourcing)
- Matthew Skelton and Manuel Pais, *Team Topologies*
