# 2.2 Hönnunarreglur hugbúnaðar

## Yfirlit og tilgangur

Hönnunarreglur hugbúnaðar eru þumalfingursreglur til að raða kóða þannig að þú getir skilið hann, breytt honum og útvíkkað með tímanum. Þær ná yfir nefnd skammstafanaheiti ([SOLID](https://en.wikipedia.org/wiki/SOLID) fyrir fimm [hlutbundnar](https://en.wikipedia.org/wiki/Object-oriented_programming) hönnunarreglur, [DRY](https://en.wikipedia.org/wiki/Don%27t_repeat_yourself) fyrir ekki-endurtaka-sjálfan-þig, [KISS](https://en.wikipedia.org/wiki/KISS_principle) fyrir hafðu-það-einfalt, [YAGNI](https://en.wikipedia.org/wiki/You_aren%27t_gonna_need_it) fyrir þú-munt-ekki-þurfa-á-því-að-halda), byggingarleg hugtök ([tengsl](https://en.wikipedia.org/wiki/Coupling_(computer_programming)), [samloðun](https://en.wikipedia.org/wiki/Cohesion_(computer_science)), [aðskilnaður áhyggjuefna](https://en.wikipedia.org/wiki/Separation_of_concerns)), skráð [hönnunarmynstur](https://en.wikipedia.org/wiki/Software_design_pattern), hærra stigs mótunaraðferðir eins og [Domain-Driven Design](https://en.wikipedia.org/wiki/Domain-driven_design) (að móta hugbúnað á tungumáli viðskiptasviðsins) og valið milli hlutbundins, [fallbundins](https://en.wikipedia.org/wiki/Functional_programming) og [gagnamiðaðs](https://en.wikipedia.org/wiki/Data-oriented_design) stíls. Ekkert af þessu eru lög. Þetta er þjöppuð reynsla og þú verður að beita henni með dómgreind.

Fyrir stór teymi er gildi sameiginlegra reglna samhæfing. Þegar hundruð verkfræðinga vinna að sama kerfi þurfa þeir sameiginlegan orðaforða fyrir hönnunarumræður og sameiginleg sjálfgefin gildi svo sjálfstætt skrifaðar einingar passi saman. Góð hönnun er það sem lætur marga breyta kerfi samhliða án stöðugra árekstra. Hún er líka það sem heldur kerfi breytanlegu áratug síðar, eðlilegum líftíma fyrirtækja- og opinberra kerfa, löngu eftir starfstíma upphaflegra höfunda þeirra.

Mikilvæga færnin er ekki að leggja reglur á minnið. Hún er að vita hvenær hver og ein villir þig. Sérhver regla hefur bilunarhátt: DRY getur framleitt ranga ágripun, SOLID getur framleitt óþarfa millilag og YAGNI getur svelt útvíkkanleika sem þú þarft raunverulega. Þessi kafli lítur á reglur sem verkfæri með gildissvið og leggur áherslu á tengsl og samloðun sem dýpri eiginleikana sem skammstafanirnar reyna að þjóna.

## Meginreglur

- Stýrðu tengslum og samloðun fyrst. Flestar nefndar reglur eru óbeinar leiðir til að bæta þessa tvo eiginleika.
- Fínstilltu fyrir breytingar: góð hönnun lágmarkar kostnað breytinganna sem þú munt í raun þurfa að gera.
- Kjóstu einföldustu hönnunina sem virkar núna, en haltu mörkum þar sem breytingar eru líklegar.
- Tvítekning er ódýrari en röng ágripun. Bíddu þar til mynstrið er skýrt.
- Gerðu ósjálfstæði skýrt og beindu því að stöðugum hlutum.
- Mótaðu sviðið á tungumáli sviðsins. Samræmdu hugbúnaðarmörk við viðskiptamörk.
- Veldu hugmyndafræði eftir vandanum, ekki hugmyndafræði. Flest stór kerfi eru raunsætt blönduð.

## Ráðleggingar

### Notaðu SOLID sem linsu, ekki gátlista

Beittu einnar-ábyrgðar til að halda einingum samloðandi, ósjálfstæðisumsnúningi til að beina ósjálfstæði að ágripunum þar sem mörk eru raunverulega til staðar og opið-lokað þar sem útvíkkunarpunktar eru raunverulegir. Framleiddu ekki viðmót, verksmiðjur og lög bara til að fullnægja skammstöfuninni þegar aðeins ein útfærsla er til og engin önnur í sjónmáli. Millilag hefur kostnað og þú borgar hann við hvern lestur.

### Beittu DRY á þekkingu, ekki á texta

DRY snýst um að tvítaka ekki eitt gagnvirkt stykki af *þekkingu*. Það snýst ekki um að útrýma línum sem líta bara svipað út. Tvö kóðastykki sem líta svipað út en breytast af ólíkum ástæðum ættu að haldast aðskilin. Kjóstu smá tvítekningu fram yfir ótímabæra sameiginlega ágripun sem tengir ótengda hluti. Dragðu út ágripunina þegar raunverulega mynstrið hefur birst tvisvar eða þrisvar.

### Láttu KISS og YAGNI standast ágiskanir

Smíðaðu fyrir kröfurnar sem þú hefur, ekki þær sem þú ímyndar þér. Forðastu ágiskunarlega almennt, svo sem stillanlega ramma, viðbótarkerfi og útvíkkunarpunkta sem enginn hefur beðið um. Mótvægið er að sveigjanleiki er raunverulega ódýrari að byggja inn snemma, eins og stöðugt viðmót eða hrein samskeyti. YAGNI mælir gegn ágiskunarlegri *útfærslu*, ekki gegn yfirveguðum mörkum.

### Hannaðu fyrir lág tengsl og háa samloðun af ásetningi

Láttu hverja einingu gera eitt vel skilgreint (samloðun) og reiða sig á sem fæstar aðrar einingar, gegnum þröng viðmót (lág tengsl). Þegar þú rýnir hönnun skaltu spyrja hvaða breytingar gára yfir einingamörk. Þær gárur eru hinn sanni mælikvarði tengsla. Aðskilnaður áhyggjuefna er sama hugmynd beitt á lög og þverlæg áhyggjuefni.

### Notaðu hönnunarmynstur sem orðaforða og andmynstur sem viðvaranir

Mynstur eru gagnleg sameiginleg nöfn á endurteknum lausnum. Náðu í eitt þegar vandinn samsvarar því í raun. Þvingaðu ekki mynstur upp á til að virðast háþróaður, því mynstraþungur kóði er oft merki um ofhönnun. Lærðu algeng [andmynstur](https://en.wikipedia.org/wiki/Anti-pattern) (guðshluti, blóðlausar líkön þar sem það á ekki við, stórar leirkúlur, dreifða einsteina) sem greiningarmerki.

### Taktu upp Domain-Driven Design þar sem sviðið er flókið

Fyrir kerfi með ríkar viðskiptareglur skaltu nota taktísk og stefnumótandi verkfæri DDD: alls staðar nálægt tungumál sem er deilt með sviðssérfræðingum, afmarkaðar samhengi sem skera kerfið í sjálfstætt mótuð stykki og samhengiskort sem lýsa hvernig þau stykki tengjast. Afmörkuð samhengi eru sérstaklega verðmæt í stærðargráðu fyrirtækja, því þau samræma teymiseignarhald við líkanamörk. DDD er ofgnótt fyrir einföld [CRUD](https://en.wikipedia.org/wiki/Create,_read,_update_and_delete)-kerfi (búa til, lesa, uppfæra, eyða).

### Veldu hugmyndafræði eftir passun

Notaðu hlutbundið fyrir að hylja ástandsbundna hegðun og móta svið. Notaðu fallbundinn stíl fyrir umbreytingar, samtíma og fyrirsjáanleika gegnum [óbreytileika](https://en.wikipedia.org/wiki/Immutable_object). Notaðu gagnamiðaða hönnun þar sem afköst og skyndiminnishegðun ráða. Stór kerfi blanda öllu þrennu. Taktu valið fyrir hvern íhlut og haltu mörkunum milli stíla hreinum.

## Málamiðlanir: kostir og gallar

| Regla / nálgun | Beitt vel | Bilunarháttur |
|---|---|---|
| SOLID | Skýr samskeyti þar sem breytingar gerast, prófanlegar einingar | Útbreiðsla viðmóta og laga, millilag án ávinnings |
| DRY | Ein uppspretta sannleikans fyrir raunverulega þekkingu | Röng ágripun tengir ótengdan kóða |
| KISS / YAGNI | Grönn, skiljanleg kerfi | Vanhönnuð samskeyti, dýrar eftirábætur á nauðsynlegum sveigjanleika |
| Hönnunarmynstur | Sameiginlegur orðaforði, sannreyndar byggingar | Farmdýrkun mynstra, tilviljanakennd flækja |
| Domain-Driven Design | Samræmd líkön og teymi, tamin flækja | Þungur helgisiður á einföldum sviðum, misstaðsett samhengismörk |
| Fallbundið / óbreytanlegt | Fyrirsjáanleiki, öruggari samtími | Óþægileg passun fyrir í eðli sínu ástandsbundin vandamál, afkastaóvæntingar |

Endurtekna spennan er milli vanhönnunar og ofhönnunar. Vanhönnuð kerfi safna tengslum og verða stíf. Ofhönnuð kerfi drukkna í ágripun sem einhver þarf að skilja og viðhalda. Svarið er ekki fastur punktur. Það er agi: fresta ákvörðunum þar til þú hefur nægar upplýsingar, á meðan þú heldur samskeytunum sem láta þig skipta um skoðun.

## Spurningar til að ræða með teyminu

1. **Hver er áþreifanlegur þröskuldur þinn til að draga út sameiginlega ágripun og hvernig kemurðu í veg fyrir að DRY framleiði ranga?** Þessi kafli er hreinskilinn um að tvítekning sé ódýrari en röng ágripun, og að þú ættir að bíða þar til mynstrið hefur birst tvisvar eða þrisvar áður en þú dregur út. Í stóru teymi er hættan sú að einhver þáttar tvö líkindabrot í sameiginlega einingu yfir teymismörk, og þá gárar hver framtíðarbreyting á einum kallanda yfir í hinn. Merkið til að koma með er hvort tvítekningarnar breytast af sömu ástæðu eða líta bara svipað út núna. Komdu þér saman um þriggja-reglu og krefstu þess að frambjóðandaágripun hafi í raun breyst saman áður en þú tengir kallendurna. Það eina samkomulag kemur í veg fyrir flokk af tengslum sem er dýr að rekja upp þegar mörg teymi reiða sig á það.

2. **Hvernig gerirðu tengsl og samloðun sýnileg í hönnunarrýni í stað þess að skilja þau eftir magatilfinningu?** Meginreglurnar setja tengsl og samloðun ofar hverri skammstöfun og skilgreina tengsl sem breytingarnar sem gára yfir einingamörk. Innsæi skalar ekki yfir hundruð verkfræðinga sem hver sér aðeins sitt horn kerfisins. Komdu með sannanir sem vél getur framleitt: ósjálfstæðisrit og samfylgnigögn sem sýna hvaða einingar eru stöðugt breyttar saman í sömu commit. Bættu við skýrri rýnispurningu sem spyr hvaða einingamörk breyting neyðir þig til að fara yfir. Þegar tvær einingar breytast alltaf saman er það merki þitt um að annaðhvort sameina þær eða laga mörkin á milli þeirra.

3. **Hvar er línan í kerfum þínum milli sviðs sem er nógu ríkt til að réttlæta Domain-Driven Design og venjulegs CRUD-forrits þar sem það er ofgnótt?** Kaflinn mælir með afmörkuðum samhengum DDD einmitt því þau samræma teymiseignarhald við líkanamörk, og varar við að DDD sé ofgnótt fyrir einföld búa-til-lesa-uppfæra-eyða kerfi og hnigni í helgisið án raunverulegrar mótunar. Að fá þetta rangt í hvora átt er kostnaðarsamt: þungt DDD á þunnu sviði grefur einfalt forrit í helgisið, á meðan útbreitt sameiginlegt líkan yfir mörg teymi þvingar stöðuga samhæfingu milli teyma. Komdu með merkin sem í raun ráða: þéttleika viðskiptareglna og hve mörg teymi þurfa að eiga hluta sjálfstætt. Taktu frá stefnumótandi vélbúnaðinn fyrir flókna kjarnann og láttu einföldu jaðrana haldast einfalda. Það heldur þér frá bæði DDD-leikhúsi og stóru leirkúlunni.

4. **Hvenær er ágripun, viðmót eða hönnunarmynstur virði millilagsins sem það bætir við og hver hefur vald til að kalla hönnun ofhannaða?** Þessi kafli er skýr um að millilag hefur kostnað sem þú borgar við hvern lestur, og að framleiða viðmót, verksmiðjur og lög til að fullnægja SOLID eða til að virðast háþróaður er bilunarháttur. Í stóru teymi liggur þrýstingurinn í hina áttina: rýnar veifa í gegn aukaágripun því hún lítur út fyrir að vera agað, og enginn vill vera sá sem mælir fyrir minni uppbyggingu. Sjónarmiðið á móti er raunverulegt, því sum samskeyti vinna sér raunverulega inn plássið sitt og að fjarlægja þau síðar er dýrt. Komdu með áþreifanlegar sannanir í umræðuna: hve margar útfærslur viðmót hefur í raun í dag, hve oft útvíkkunarpunkturinn hefur nokkurn tíma sveigst og hve margar skrár lesandi þarf að opna til að fylgja einni kóðaleið. Komdu þér saman um að ein útfærsla án annarrar í sjónmáli sé sjálfgefin ástæða til að fella inn og nefndu hver getur kallað hönnun ofhannaða án þess að það lesist sem móðgun. Í fyrirtækja- og opinberum kerfum sem lifa höfunda sína um áratug er gjörsamlega óþarfur millilag skattur sem hver framtíðarumsjónarmaður borgar, svo líttu á „hvað kaupir þessi ágripun okkur“ sem varanlega rýnispurningu, ekki persónulega áskorun.

5. **Hvernig ákveðurðu hvaða hugmyndafræði hver íhlutur notar, hlutbundna, fallbundna eða gagnamiðaða, og hvernig heldurðu mörkunum milli þeirra hreinum?** Kaflinn heldur því fram að stór kerfi séu raunsætt blönduð og að þú ættir að velja fyrir hvern íhlut eftir passun, með hlutbundið fyrir ástandsbundin svið, fallbundinn stíl fyrir umbreytingar og samtíma og gagnamiðaða hönnun þar sem afköst og skyndiminnishegðun ráða. Ef þetta er skilið eftir óstýrt verður val hugmyndafræði háð því hver skrifaði eininguna fyrst, og breytilegt ástand lekur inn í það sem ætti að vera hreinar umbreytingar, eða fallbundin hreinhyggja berst við í eðli sínu ástandsbundið vandamál. Sönnunin sem vert er að koma með er hvar raunverulegur sársauki þinn er: hvaða íhlutir eru erfiðir að prófa vegna falins ástands, hvaða heitu leiðir eru bundnar við skyndiminni og hvar núverandi stíll neyðir fram óþægilegar krókaleiðir. Ákveddu sjálfgefna hugmyndafræði fyrir hvert lag af ásetningi og skrifaðu niður hvar samskeytin milli stíla falla, svo fallbundinn kjarni og skipunarbundin jaðar blæði ekki hvort inn í annað. Fyrir eftirlitsskylt eða opinbert kerfi þar sem útreikningur verður að vera úttektarhæfur og endurgeranlegur fyrir tiltekið tímabil er óbreytanlegur, fallbundinn kjarni oft regluvörslukrafa frekar en smekkur, og sú skorða ætti að knýja mörkin frekar en fylgja þeim.

6. **Hvernig heldurðu þessum reglum frá því að harðna í kreddu og hvar skráirðu rökin að baki hönnunarákvörðun svo framtíðarteymi geti endurskoðað hana?** Sérhver regla í þessum kafla hefur gildissvið og bilunarhátt, og öll rammunin lítur á þær sem verkfæri til að beita með dómgreind frekar en lög til að framfylgja. Í stóru teymi verður regla hljóðlega að skyldu: DRY bannar alla tvítekningu, SOLID skyldar viðmót á hvern flokk og raunsæjar undantekningar eru hindraðar í rýni af fólki sem vitnar í skammstöfunina frekar en niðurstöðuna. Spennan er sú að samræmi hjálpar raunverulega hundruðum verkfræðinga að samhæfa sig, svo þú getur ekki einfaldlega lýst hverja reglu valkvæða. Komdu með dæmi þar sem að fylgja reglu bókstaflega framleiddi verri hönnun og komdu með ákvörðunarskrárnar, ef einhverjar eru, sem útskýra hvers vegna tiltekin mörk eða ágripun er til. Komdu þér saman um að reglur séu sjálfgefin gildi sem verkfræðingur má víkja frá með skráðri ástæðu og fangaðu afdrifaríkar hönnunarákvarðanir í stutta arkitektúrákvörðunarskrá svo næsta teymi erfi rökin og ekki bara kóðann. Í fyrirtækja- og opinberum kerfum, þar sem upphaflegir höfundar eru löngu farnir og úttektir spyrja hvers vegna kerfið sé mótað eins og það er, er sú skriflega slóð munurinn á hönnun sem framtíðarteymi getur breytt örugglega og einni sem þau óttast að snerta.

## Sjónarhorn eftir geirum

**Sprotafyrirtæki.** Kjóstu einföldustu hönnunina sem afhendist og haltu einni vel þáttaðri einingu þar til raunverulegt annað notkunartilvik neyðir samskeyti. Af skornum skammti auðlind þín er verkfræðiathygli, svo ótímabær viðmót, lög og ágiskunarrammar eru hreinn kostnaður. Fylgdu þriggja-reglunni áður en þú dregur út nokkra sameiginlega ágripun og láttu YAGNI drepa útvíkkunarpunktana sem enginn hefur beðið um enn.

**Lítið fyrirtæki.** Án arkitekts á launaskrá og með þröngt fjárhagsáætlun skaltu hallast að hönnuninni sem þegar er innbyggð í rammana og bókasöfnin sem þú kaupir frekar en að finna upp eigin mynstur. Taktu frá sérhönnunarátak fyrir handfylli reglna sem eru raunverulega viðskiptin þín og haltu öllu öðru hefðbundnu svo verktaki eða nýr starfsmaður geti lesið það. Smá tvítekning sem þú skilur slær snjalla ágripun sem aðeins höfundur hennar getur viðhaldið.

**Stórfyrirtæki.** Ávinningur sameiginlegra reglna er samhæfing yfir mörg teymi: sameiginlegur orðaforði fyrir hönnunarrýni og afmörkuð samhengi sem samræma líkanamörk við teymiseignarhald svo hópar þróist sjálfstætt. Stýrðu tengslum og samloðun af ásetningi með ósjálfstæðis- og samfylgnigögnum og skráðu afdrifaríkar hönnunarákvarðanir svo kerfi haldist breytanleg löngu eftir að höfundar þeirra halda áfram. Gættu jafnt gegn röngu ágripuninni sem tengir teymi og ofhönnuninni sem skattleggur hvern lesanda.

**Hið opinbera.** Úttektarhæfi og endurgeranleiki ráða oft hönnuninni. Óbreytanlegur, fallbundinn kjarni leyfir þér að endurskapa sögulegan útreikning nákvæmlega fyrir tiltekið tímabil, sem flókið hlutatré með földu breytilegu ástandi getur ekki tryggt. Kjóstu skýra birta samninga fram yfir sameiginlegar töflur á samhengismörkum og haltu hönnuninni og ákvörðunarskrám hennar læsilegum endurskoðendum og því teymi sem erfir kerfið áratug síðar.

## Dæmi

**Sprotafyrirtæki.** Þriggja verkfræðinga sprotafyrirtæki sem smíðar fyrstu vöru sína stenst freistinguna að skipta hverjum eiginleika í lög af viðmótum og verksmiðjum og heldur einni vel þáttaðri einingu þar til raunverulegt annað notkunartilvik birtist. Þegar sama rökfræðin birtist í þriðja sinn yfir skráningar- og greiðsluflæðin draga þeir út eina litla sameiginlega falli frekar en ágiskunarramma. Þetta heldur kóðagrunninum nógu litlum til að hver þeirra geti haldið honum í höfðinu og fáu samskeytin sem þeir draga falla þar sem varan er líklegust til að breytast.

**Stórfyrirtæki.** Stór tryggingavettvangur mótar vátryggingar, kröfur og reikningagerð sem aðskilin afmörkuð samhengi, hvert í eigu sérstaks teymis með eigið gagnalíkan og þjónustumörk. Þar sem samhengin mætast, eins og þegar krafa vísar til vátryggingar, tala þau gegnum skýra birta samninga frekar en sameiginlegar gagnagrunnstöflur. Þetta leyfir teymunum þremur að þróast sjálfstætt og alls staðar nálæga tungumálið heldur samtölum við vátryggingafræðinga nákvæmum. Fyrri útgáfa hafði deilt einu útbreiddu líkani og sérhver breyting krafðist samhæfingar milli teyma.

**Hið opinbera.** Landsbundið skattavinnslukerfi kýs vísvitandi gagnamiðaðan, fallbundinn kjarna fyrir útreikningsvél sína. Skattareglur eru settar fram sem hreinar umbreytingar yfir óbreytanlegar inntaksfærslur, sem gerir þær úttektarhæfar, prófanlegar og endurgeranlegar fyrir tiltekið skattár. Skipunarbundnu, ástandsbundnu hlutarnir (vinnuflæði, tilkynningar) eru geymdir á jöðrunum. Endurskoðendur geta bent á tiltekna reglu-útgáfu og endurskapað hvaða sögulega útreikning sem er nákvæmlega, sem er lagakrafa sem flókið hlutatré með földu breytilegu ástandi gat ekki tryggt.

## Viðskiptarök: hvatar, ávöxtun fjárfestingar og heildarkostnaður

Hönnunargæði eru fjárfesting í *breytanleika* kerfis, og breytanleiki ræður heildareignarkostnaði. Mestur kostnaður kerfis lendir eftir fyrstu útgáfu, í breytingum og útvíkkun. Vel hönnuð kerfi halda kostnaði breytinga nokkurn veginn flötum yfir tíma. Illa hönnuð sjá kostnað hverrar breytingar klifra þar til kerfið verður í reynd óbreytanlegt og þarf að endurskrifa það, dýrasta niðurstaðan af öllum.

Upptökukostnaðurinn er aðallega færni og rýniagi: að kenna reglurnar og eyða hönnunartíma fyrirfram. Kostnaðurinn við að taka þær ekki upp er hæg uppsöfnun [tæknilegrar skuldar](https://en.wikipedia.org/wiki/Technical_debt), fallandi afhendingarhraði, hækkandi gallahlutfall og endanleg kostnaðarsöm endurskrif. Til að færa rök við forystu skaltu tengja hönnunaragann við spáhæfni afhendingar og við að forðast endurskrifaáætlanir og rekja fyrirvara eins og bilanahlutfall breytinga og tíma til að útfæra sambærilega eiginleika yfir tíma. Gættu þín líka á andstæða bilinu: of mikil fjárfesting í hönnun fyrir óvissa framtíð eyðileggur líka virði. Svo rökin eru fyrir *viðeigandi* hönnun, kvarðaðri eftir því hve líkleg og hve dýr framtíðarbreyting er.

## Andmynstur og gildrur

- **Ágiskunarleg almennt:** að smíða útvíkkanleika fyrir ímyndaðar kröfur sem aldrei koma.
- **Röng ágripun:** að þvinga ótengdan kóða saman til að fullnægja DRY og skapa tengsl sem eru verri en tvítekning.
- **Farmdýrkun mynstra:** að beita hönnunarmynstrum í sjálfu sér og bæta við millilag án ávinnings.
- **Blóðlausir eða guðshlutir:** líkön án hegðunar, eða hlutir sem gera allt. Hvort tveggja gefur til kynna misstaðsetta ábyrgð.
- **Dreifður einsteinn:** þjónustur skiptar líkamlega en enn þétt tengdar og sameina kostnað beggja nálgana.
- **Stór leirkúla:** engin greinanleg uppbygging. Sérhver breyting teflir öllu í tvísýnu.
- **DDD-leikhús:** að taka upp orðaforðann og möppuuppbygginguna án sviðsmótunarinnar sem gefur henni virði.

## Þroskalíkan

- **Stig 1, Upphaf:** Hönnun er ad hoc og viðbragðsdrifin. Tengsl safnast óheft. Reglur eru óþekktar eða ákallaðar sem slagorð og ágripanir birtast eða hverfa eftir venjum einstaklinga.
- **Stig 2, Þróun:** Teymi þekkja reglurnar og beita þeim, en ósamræmt og oft kreddukennt. Sumir hópar stýra tengslum og samloðun af ásetningi á meðan aðrir gera það ekki, og enginn sameiginlegur orðaforði er til um skipulagsheildina.
- **Stig 3, Stöðlun:** Sameiginlegur hönnunarorðaforði, þriggja-regla fyrir að draga út ágripanir, tengsla- og samloðunargreining og afmörkuð samhengi samræmd teymum eru skjalfest og vænt um alla skipulagsheildina, beitt samræmt í hönnunarrýni frekar en látið ráðast af einstaklingssmekk.
- **Stig 4, Stjórnun:** Hönnunarheilsa er mæld gegn grunnlínum: tengsla- og samfylgnigögn, bilanahlutfall breytinga og tími til að útfæra sambærilega eiginleika eru rakin yfir tíma, svo ágripanir og mörk séu bætt við, haldið eða fjarlægð á grundvelli gagna, og ofhönnun og röng ágripun séu gripin af gögnum frekar en skoðun.
- **Stig 5, Samhæfing:** Hönnunaragi er samþættur afhendingar- og áhættuáætlun um skipulagsheildina. Reglum er beitt með blæbrigðum og þekktum bilunarháttum. Val á hugmyndafræði og mörkum er yfirvegað og stöðugt endurskoðað og skipulagsheildin endurbyggir, endurafmarkar og leggur niður ágripanir reglulega eftir því sem sviðið og gögnin breytast.

## Hugmyndir til umræðu

- Hvernig greinirðu á milli nauðsynlegs samskeytis og ágiskunarlegs almenns áður en þú hefur framtíðarkröfuna?
- Hvenær hefur DRY leitt teymið þitt að rangri ágripun og hvernig þekktirðu það?
- Hvar ættu mörk afmarkaðra samhengja að falla og hve náið ættu þau að speglast skipuritinu?
- Hve mikil hönnun ætti að koma á undan kóða í þínu samhengi og hvernig skráirðu ákvarðanirnar?
- Hvaða hlutar kerfisins þíns myndu njóta góðs af fallbundnari eða gagnamiðaðri stíl?
- Hvernig heldurðu hönnunarreglum frá því að harðna í kreddu sem stendur gegn raunsæjum undantekningum?

## Helstu atriði

- Tengsl og samloðun eru eiginleikarnir sem skipta máli. Skammstafanirnar eru leiðir að þeim markmiðum.
- Sérhver regla hefur bilunarhátt. Veistu hvenær hver og ein villir.
- Kjóstu smá tvítekningu fram yfir ótímabæra eða ranga ágripun.
- Notaðu DDD og afmörkuð samhengi til að samræma flókin svið við teymiseignarhald.
- Veldu hugmyndafræði eftir passun. Stór kerfi eru raunsætt blönduð.
- Hannaðu fyrir breytingarnar sem þú munt í raun þurfa og forðastu bæði vanhönnun og ofhönnun.

## Heimildir og frekari lestur

- Robert C. Martin, *Clean Architecture* and *Agile Software Development, Principles, Patterns, and Practices*
- Eric Evans, *Domain-Driven Design: Tackling Complexity in the Heart of Software*
- Vaughn Vernon, *Implementing Domain-Driven Design*
- Erich Gamma, Richard Helm, Ralph Johnson, John Vlissides, *Design Patterns: Elements of Reusable Object-Oriented Software*
- Martin Fowler, *Refactoring: Improving the Design of Existing Code* and *Patterns of Enterprise Application Architecture*
- David L. Parnas, *On the Criteria to Be Used in Decomposing Systems into Modules*
- Sandi Metz, *Practical Object-Oriented Design*
