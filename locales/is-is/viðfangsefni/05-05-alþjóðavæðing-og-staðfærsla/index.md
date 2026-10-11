# 5.5 Alþjóðavæðing og staðfærsla

## Yfirlit og tilgangur

[Alþjóðavæðing](https://en.wikipedia.org/wiki/Internationalization_and_localization) (i18n) er verkfræðivinnan að smíða hugbúnað þannig að hægt sé að aðlaga hann að hverju tungumáli, svæði og menningu án þess að breyta kóðanum. Staðfærsla (l10n) er vinnan sem fylgir: að aðlaga vöru í raun að tilteknu málsvæði með því að þýða texta, sníða dagsetningar og tölur, laga uppsetningu og gera grein fyrir menningarlegum væntingum. Þetta tvennt er aðgreint. Alþjóðavæðing er gerð einu sinni, í arkitektúrnum. Staðfærsla er gerð oft, í efninu. Fáðu arkitektúrinn réttan fyrirfram og hver staðfærsla er ódýr. Fáðu hann rangan og hver verður sársaukafull, villuhætt endurbót.

Fyrir stór teymi er i18n grundvallararkitektúrákvörðun. Hún snertir hvert lag: gagnageymslu, strengjameðhöndlun, uppsetningu og efnisleiðslur. Ef þú kemur henni ekki á snemma og framfylgir henni gegnum sameiginleg bókasöfn og lint-reglur harðkóða teymi enskar strengi, tengja saman þýdd brot og gera ráð fyrir latnesku letri. Sú skuld þarf að leysast upp áður en varan getur farið á nokkurn nýjan markað. Sameiginlegur i18n rammi og staðfærsluvinnuflæði leyfa tugum teyma að afhenda vöru á mörgum tungumálum án þess að hvert finni upp lagnirnar.

Mikilvægi fyrir fyrirtæki og hið opinbera er beint. Fjölþjóðleg fyrirtæki verða að þjóna viðskiptavinum og starfsfólki yfir lönd, tungumál og regluverk. Ríkisstjórnir verða að þjóna málfarslega fjölbreyttum þýðum. Mörg lönd eru opinberlega fjöltyngd og mörg eru lagalega skylduð til að veita þjónustu á mörgum tungumálum, þar á meðal [hægri-til-vinstri](https://en.wikipedia.org/wiki/Bidirectional_text) letri og frumbyggja- eða minnihlutamálum. Fyrir opinbera þjónustu er tungumálaaðgengi jafnréttis- og lagamál: borgari sem getur ekki lesið eina tungumálið sem er í boði er í raun synjað um þjónustuna.

## Meginreglur

- Alþjóðavæddu arkitektúrinn einu sinni. Staðfærðu efnið oft.
- Harðkóðaðu aldrei texta sem snýr að notanda. Fluttu alla strengi út í stýrð tilföng.
- Notaðu [Unicode](https://en.wikipedia.org/wiki/Unicode) (UTF-8) alls staðar. Gerðu ráð fyrir að texti geti verið á hvaða letri sem er.
- Tengdu aldrei saman þýdd brot. Málfræði og orðaröð er ólík eftir tungumálum.
- Skipuleggðu fyrir textaþenslu, hægri-til-vinstri letur og flóknar fleirtölu- og kynjareglur.
- Sníddu dagsetningar, tölur, gjaldmiðla og nöfn eftir málsvæði, ekki kóða.
- Aðgreindu þýðanlegt efni frá kóða svo þýðendur snerti aldrei frumkóða.
- Staðfærsla er menningarleg, ekki bara málfarsleg: litir, myndmál og dæmi skipta máli.

## Ráðleggingar

### Byggðu trausta alþjóðavæðingararkitektúr

Geymdu og vinndu allan texta sem Unicode (UTF-8) frá enda til enda (gagnagrunn, API og viðmót) svo hvert letur sé framsetjanlegt. Fluttu hvern streng sem snýr að notanda út í tilfangaskrár eða skilaboðaskrá lyklaða eftir auðkenni, aldrei innbyggða í kóða eða álag. Skilgreindu málsvæði sem tungumál auk svæðis (og letri þar sem þarf) svo þú getir greint til dæmis afbrigði eins tungumáls yfir lönd. Haltu sníðarökfræði í vel prófuðu alþjóðavæðingarbókasafni frekar en að handrúlla dagsetninga-, tölu- og gjaldmiðilssníði. Geymdu gögn á hlutlausu, ótvíræðu formi (UTC-tímastimplar, ISO land- og gjaldmiðlakóðar, grunneiningar) og sníddu aðeins á framsetningarlaginu.

### Meðhöndlaðu tungumálaflækju rétt

Gerðu ekki ráð fyrir textalengd. Leyfðu rausnarlegt rými því þýðingar eru yfirleitt miklu lengri en enska og hannaðu uppsetningar sem flæða aftur frekar en að stytta eða skarast. Styddu tvíátta (hægri-til-vinstri) letur með því að nota rökrænar frekar en líkamlegar uppsetningareigindir og spegla viðmótið þar sem við á. Notaðu fleirtölureglur málsvæðisins gegnum i18n-bókasafnið þitt (tungumál hafa allt frá einu til sex fleirtöluform) í stað barnalegrar eintölu/fleirtölu rökfræði. Meðhöndlaðu kyn og málfræðilega samsvörun þar sem tungumálið krefst þess. Byggðu aldrei setningar með samtengingu. Notaðu fullar, stikaðar skilaboðasniðmát svo þýðendur stýri orðaröð.

### Komdu á staðfærsluvinnuflæði og þýðingastjórnun

Líttu á staðfærslu sem samfellda leiðslu, ekki lotu fyrir opnun. Dragðu út strengi sjálfvirkt, ýttu þeim í [þýðingastjórnunarkerfi](https://en.wikipedia.org/wiki/Translation_management_system) og dragðu fullbúnar þýðingar til baka, helst samþætt við CI svo nýir strengir séu merktir og staðfærðar útgáfur haldist samstilltar. Gefðu þýðendum samhengi: skjámyndir, lýsingar, stafatakmörk og hugtakaskrá og stílleiðbeiningu fyrir hvert tungumál til að halda hugtakanotkun og tóni samræmdri. Notaðu [þýðingaminni](https://en.wikipedia.org/wiki/Translation_memory) til að endurnýta fyrri vinnu og skera kostnað. Ákveddu af ásetningi hvar [vélþýðing](https://en.wikipedia.org/wiki/Machine_translation) er ásættanleg (áhættulítið, mikið magn efni) og hvar mannleg þýðing og rýni eru nauðsynleg (lögfræði, læknisfræði, öryggi, vörumerkiskritískt). [Gervistaðfærðu](https://en.wikipedia.org/wiki/Pseudolocalization) snemma, með því að skipta strengjum út fyrir lengda, áherslumerkta staðgengla, til að grípa harðkóðaða strengi, styttingu og kóðunargalla áður en raunveruleg þýðing hefst.

### Staðfærðu snið, menningu og efni, ekki bara orð

Sníddu dagsetningar, tíma, tölur, gjaldmiðla, heimilisföng, símanúmer og nöfn eftir málsvæði og virtu staðbundnar venjur (dagsetningaröð, aukastafa- og hópunaraðgreinara, gjaldmiðilsstaðsetningu, nafnaröð). Aðlagaðu myndmál, tákn, liti, dæmi og líkingar að staðbundinni menningarmerkingu, því tákn og litir bera ólíkar merkingar yfir menningar. Gerðu grein fyrir staðbundnum mun á lagalegu og reglugerðarefni. Greindu hnattrænt samræmi (vörumerki, kjarnavirkni) frá svæðisaðlögun (efni, dæmi, regluvarsla) og ákveddu skýrt hvaða þættir eru fastir og hverjir sveigjast.

### Stýrðu i18n sem sameiginlegum innviðum

Útvegaðu sameiginlegt i18n-bókasafn, lint-reglur um strengjaútflutning og staðlaðan málsvæðisgreiningarbúnað svo teymi geti ekki fyrir slysni harðkóðað texta. Settu eignarhald á staðfærsluleiðsluna og hugtakaskrárnar. Prófaðu í mörgum málsvæðum í CI, þar á meðal hægri-til-vinstri málsvæði og langtexta gervimálsvæði, svo afturfarir séu gripnar sjálfvirkt.

## Málamiðlanir: kostir og gallar

| Ákvörðun | Kostir | Gallar |
|---|---|---|
| Alþjóðavæða frá degi eitt | Ódýr markaðsinngangur síðar, engin endurbót | Kostnaður fyrirfram jafnvel áður en annað málsvæði er þörf |
| Bæta við i18n síðar | Fresta kostnaði ef hnattræn þörf er óviss | Mjög dýrt og áhættusamt að leysa upp harðkóðaðar forsendur |
| Mannleg þýðing | Há gæði, menningarlega nákvæm | Hægari og kostnaðarsamari |
| Vélþýðing | Hröð, ódýr, stigvaxar í gríðarlegt magn | Gæða- og nákvæmnisáhætta. Óhentug fyrir hágagnsemiefni |
| Samfelld staðfærsluleiðsla | Málsvæði haldast samstillt, engin opnunarkreppa | Verkfæra- og ferlafjárfesting |
| Djúp menningaraðlögun á svæði | Betri staðbundin passun og traust | Fleiri efnisafbrigði til að smíða og viðhalda |

Mikilvægasta málamiðlunin er hvenær á að fjárfesta í alþjóðavæðingu. Að bæta i18n við vöru fulla af harðkóðuðum, samtengdum, kóða sem gerir ráð fyrir latnesku letri er ein dýrasta tegund tæknilegrar skuldar að greiða. Fyrir hverja skipulagsheild með sennilega alþjóðlegan eða fjöltyngdan metnað, sem nær nánast til allra stórra fyrirtækja og fjöltyngdra ríkisstjórna, er að alþjóðavæða arkitektúrinn snemma langtum ódýrara en að bæta við síðar, jafnvel þótt ávinningurinn sé frestaður.

## Spurningar til að ræða með teyminu

1. **Framfylgjum við strengjaútflutningi með lint-reglum og keyrir gervistaðfærsla í CI áður en nokkur raunveruleg þýðing fer fram?** Skuldin sem gerir alþjóðavæðingu dýra (harðkóðaðir enskir strengir, samtengd setningabrot, latnesk-letur forsendur) safnast hljóðlega nema verkfæri stöðvi hana við innritun. Lint-reglur sem merkja harðkóðaðan notendatexta, auk langtexta áherslumerkts gervimálsvæðis keyrt í CI, grípa styttingu, skörun og kóðunargalla meðan ódýrt er að laga þá. Þetta er það sem leyfir tugum teyma að afhenda eina vöru á mörgum tungumálum án þess að hvert finni upp lagnirnar eða leysi upp forsendur á frest síðar. Komdu með leit að harðkóðuðum strengjum og spyrðu hvort nokkurt teymi gæti óvart afhent einn í dag. Ef ekkert í leiðslunni myndi grípa það er það bilið til að loka fyrst.

2. **Hvar geymum við kanónísk gögn og er sníðun afmörkuð við framsetningarlagið?** Að geyma tímastimpla sem UTC, lönd og gjaldmiðla sem ISO-kóða og upphæðir í grunneiningum þýðir að hvert málsvæði getur sniðið þau rétt á jaðrinum, á meðan sníðarökfræði bökuð inn í gagnalagið framleiðir galla sem er sársaukafullt að leysa upp. Komdu þér saman um að dagsetningar, tölur, gjaldmiðlar, heimilisföng og nöfn séu sniðin aðeins við framsetningu, gegnum vel prófað bókasafn frekar en handrúllaðan kóða. Þetta skiptir máli fyrir fjölþjóðleg fyrirtæki og fjöltyngdar ríkisstjórnir þar sem borgari verður að sjá rétta dagsetningaröð, aukastafaaðgreinara og nafnaröð í eigin venju. Komdu með dæmi um gildi sem kerfið þitt geymir þegar sniðið og raktu hvað brotnar þegar nýtt málsvæði þarf það ólíkt. Ef gögn og framsetning eru flækt skaltu ákveða hvernig þú greiðir úr því áður en þú bætir við málsvæðum.

3. **Hvar nákvæmlega er vélþýðing ásættanleg og hvernig er staðfærsluleiðsla okkar höfð samfelld frekar en í lotum?** Vélþýðing er hröð og ódýr fyrir áhættulítið, mikið magn efni en óhentug fyrir lögfræði-, læknisfræði-, öryggis- eða vörumerkiskritískan texta þar sem röng þýðing veldur raunverulegum skaða, svo mörkin þurfa að vera skýr stefna, ekki ágiskun á hvert teymi. Á sama hátt tryggir að líta á staðfærslu sem lotu fyrir opnun þýðingakreppu, á meðan að draga út strengi sjálfvirkt og samstilla gegnum þýðingastjórnunarkerfi heldur hverju málsvæði núgildandi. Ákveddu hver á leiðsluna, hugtakaskrárnar og mannlega rýnihliðið fyrir hágagnsemi strengi. Komdu með nýlega útgáfu og spyrðu hve lengi nýir strengir hennar voru að birtast á hverju tungumáli. Ef málsvæði reka úr takti milli útgáfa er leiðsla þín lota í dulargervi.

4. **Prófum við hægri-til-vinstri málsvæði og langtexta gervimálsvæði sjálfvirkt, eða gerum við hljóðlega ráð fyrir latnesku letri og enskri lengd uppsetningar?** Tvíátta (hægri-til-vinstri) stuðningur og textaþensla eru forsendurnar sem brotna sýnilegast á nýjum markaði: viðmót sem átti að spegla en var aldrei spegluð og hnappar sem styttast þegar þýska eða finnska er fjörutíu prósent lengri en enska. Þrýstingurinn á móti er hraði, því að smíða á rökrænum frekar en líkamlegum uppsetningareigindum og tengja áherslumerkt gervimálsvæði inn í samfellda samþættingu (CI) kostar fyrirhöfn áður en nokkur raunverulegur viðskiptavinur þarf það. Komdu með skjámynd af annasömustu skjám þínum birtum á hægri-til-vinstri málsvæði og á lengdu gervimálsvæði og teldu skörunina, klipptu merkin og fasta örvarnar. Fyrir fjölþjóðlegt fyrirtæki eða ríkisstjórn lagalega skylduð til að þjóna hægri-til-vinstri eða minnihlutamáli er uppsetning sem getur ekki speglast ekki snyrtigalli, það er markaður eða lögbundin skylda sem þú getur ekki mætt án endursmíði.

5. **Hvaða hlutar vörunnar eru hnattrænt fastir og hverjir sveigjast eftir svæði og hver hefur vald til að ákveða?** Staðfærsla er menningarleg, ekki bara málfarsleg, svo litir, myndmál, dæmi, ávörp og jafnvel hvaða eiginleikar eru í boði geta verið ólík eftir markaði, samt er hvert svæðisafbrigði sem þú leyfir enn einn gripur að smíða, þýða, rýna og viðhalda að eilífu. Spennan er milli staðbundinnar passunar, sem byggir traust og umbreytingu, og samræmis, sem heldur vörumerkinu samfelldu og viðhaldsbyrði afmarkaðri. Komdu með áþreifanlegan lista yfir hvað fyrirhugað nýtt málsvæði myndi breyta umfram þýdda strengi og verðleggðu viðvarandi viðhald hvers afbrigðis, ekki bara fyrstu smíði þess. Í stóru fyrirtæki þarf þessi ákvörðun nefndan eiganda svo svæðisteymi geti ekki kvíslað vöruna ad hoc, og hjá hinu opinbera verður hún að virða lagalegar og aðgengisreglur efnis sem eru ólíkar eftir lögsagnarumdæmi og eru ekki valkvæðar.

6. **Hvaða málsvæðum skuldbindum við okkur í raun, hvernig höldum við hugtakanotkun samræmdri yfir þau og hvaða sönnunargögn knýja þann lista?** Að bæta við tungumáli er auðvelt að lofa og dýrt að viðhalda, því hvert þarfnast hugtakaskrár, stílleiðbeiningar, mannlegrar rýni fyrir hágagnsemi strengi og réttrar fleirtölu- og kynjameðhöndlunar sem barnaleg eintölu-eða-fleirtölu rökfræði fær rangt í flestum tungumálum. Sjónarmiðin sem togast á eru ná gegn kostnaði: markaður eða þýði þjónað illa getur verið verra en það sem er ekki þjónað yfirleitt. Komdu með þýðið eða tekjurnar að baki hverju frambjóðendamálsvæði, fleirtölureglu- og sníðaþekjuna sem bókasafn þitt veitir því og hver á hugtakaskrá þess. Fyrir fjölþjóðlegt fyrirtæki er drifkrafturinn aðgengilegur markaður og stuðningskostnaður á tungumál, á meðan fyrir hið opinbera er það lagaleg tungumálaaðgangsskylda og jafnrétti, magnsett með fjölda íbúa sem geta aðeins átt viðskipti á því tungumáli.

## Sjónarhorn eftir geirum

**Sprotafyrirtæki.** Taktu ódýru arkitektúrákvarðanirnar á degi eitt og hættu þar: UTF-8 frá enda til enda, hver notendastrengur í skilaboðaskrá og dagsetningar, tölur og gjaldmiðlar sniðin gegnum málsvæðismeðvitað bókasafn. Þetta kostar nánast ekkert meðan þú afhendir á einu tungumáli og sparar endurskrift þegar stærsti fyrsti viðskiptavinur vill annað. Settu ekki upp þýðingaleiðslu eða styddu málsvæði sem enginn borgar fyrir enn. Haltu dyrunum opnum, ekki öllu húsinu innréttuðu.

**Lítið fyrirtæki.** Án alþjóðavæðingarsérfræðings og með þröngt fjárhagsáætlun skaltu hallast að i18n-eiginleikunum sem eru þegar í ramma þínum og hýstri þýðingastjórnunarþjónustu frekar en að smíða leiðslur sjálfur. Notaðu vélþýðingu fyrir áhættulítið, mikið magn efni og borgaðu fyrir mannlega þýðingu aðeins þar sem mistök myndu kosta þig viðskiptavin eða brjóta reglu, eins og lögfræði-, öryggis- eða reikningstexta. Skuldbindu þig til málsvæðis aðeins þegar tiltekinn markaður réttlætir greinilega viðvarandi þýðingar- og rýnikostnað.

**Stórfyrirtæki.** Vandinn er stjórnarhættir yfir mörg teymi: sameiginlegt i18n-bókasafn, lint-reglur sem hafna harðkóðuðum strengjum, samfelld staðfærsluleiðsla með þýðingaminni og hugtakaskrám á tungumál og fjölmálsvæða CI sem inniheldur hægri-til-vinstri og langtexta gervimálsvæði. Reku staðfærslu sem sameiginlega innviði með skýrum eiganda svo hópar hætti að finna upp lagnirnar eða reka úr takti. Mældu tungumálaþekju, staðfærslugæði og tíma til að opna nýtt málsvæði og stýrðu eignasafni málsvæða eftir þeim tölum frekar en að opna markaði ad hoc.

**Hið opinbera.** Tungumálaaðgengi er oft lagaskylda og nær yfir opinber tungumál, hægri-til-vinstri letur og frumbyggja- eða minnihlutamál, svo gagnsæi og jafnrétti móta hvert val. Byggðu sameiginlegan i18n-ramma og þýðingavinnuflæði yfir stofnanir, krefstu mannlegrar rýni fyrir lögfræði- og öryggishugtök og birtu hugtakaskrár svo hugtök haldist samræmd milli þjónusta. Innkaup ættu að krefjast málsvæða-, hægri-til-vinstri og aðgengisstuðnings í samningum, og þýðið sem þjónað er á hverju tungumáli er mælikvarðinn sem réttlætir útgjöldin fyrir almenningi.

## Dæmi

**Sprotafyrirtæki.** Lítið sprotafyrirtæki sem afhendir aðeins á ensku tók samt nokkrar ódýrar arkitektúrákvarðanir á degi eitt: UTF-8 alls staðar, hver notendastrengur dreginn í skilaboðaskrá í stað þess að vera harðkóðaður og dagsetningar og gjaldmiðlar sniðin gegnum málsvæðismeðvitað bókasafn. Það kostaði þau nánast ekkert meðan þau höfðu eitt tungumál. Ári síðar, þegar stærsta væntanlega viðskiptavini þeirra bað um franska og þýska útgáfu, var að bæta við þeim málsvæðum að mestu þýðingaræfing afhent verktaka, ekki endurskrift, og þau kláruðu samninginn á vikum í stað þess að fresta honum um ársfjórðung af verkfræðivinnu.

**Stórfyrirtæki.** Hnattrænt netverslunarfyrirtæki alþjóðavæddi vettvang sinn snemma: UTF-8 í gegn, útfluttir strengir, málsvæðismeðvitað sniðbókasafn og samfelld staðfærsluleiðsla með þýðingaminni og hugtakaskrám á tungumál. Að fara inn á nýjan markað varð að mestu efnisæfing (þýða, rýna, aðlaga myndmál) frekar en verkfræðiverkefni, sem leyfði fyrirtækinu að opna á nýjum málsvæðum á vikum. Hægri-til-vinstri stuðningur byggður á rökrænum uppsetningareigindum þýddi að arabískir og hebreskir markaðir kröfðust lítillar nýrrar viðmótsvinnu.

**Hið opinbera.** Landsstjórn lagalega skylduð til að afhenda þjónustu á nokkrum opinberum tungumálum, þar á meðal hægri-til-vinstri letri og minnihlutamálum, byggði sameiginlegan i18n-ramma og þýðingavinnuflæði notað yfir stofnanir. Gervistaðfærsla í CI greip harðkóðaða strengi og styttingu fyrir opnun. Sameiginleg hugtakaskrá hélt lagahugtökum samræmdum yfir þjónustur og tungumál. Borgarar geta klárað skatta-, heilbrigðis- og bótafærslur á eigin tungumáli með réttu dagsetninga-, tölu- og nafnasniði, sem fullnægir tungumálaaðgangslögum og bætir jafnrétti fyrir þá sem tala ekki meirihlutamál.

## Viðskiptarök: hvatar, ávöxtun fjárfestingar og heildarkostnaður

Ávöxtun alþjóðavæðingar er markaðsaðgangur og hraði. Vel alþjóðavædd vara getur farið inn í ný lönd og tungumálamarkaði hratt og ódýrt, sem breytir hverju nýju málsvæði í viðbótartekjur eða borgaraútbreiðslu frekar en stórt verkefni. Staðfærslugæði knýja umbreytingu, traust og stuðningskostnað á hverjum markaði: notendur eiga meiri viðskipti og hafa sjaldnar samband við stuðning þegar varan talar tungumál þeirra rétt og virðir venjur þeirra.

Hvað heildareignarkostnað varðar er upptökukostnaðurinn verkfræðin fyrirfram til að alþjóðavæða, auk viðvarandi þýðingar- og leiðslukostnaðar. Kostnaðurinn við að taka ekki upp er dýra endurbótin: að leysa upp harðkóðaða strengi, samtengingu, kóðunargalla og uppsetningarforsendur yfir allan kóðagrunn, oft á fresti knúnum af markaði eða lagakröfu. Léleg staðfærsla ber líka falinn kostnað: tapaða sölu á mörkuðum sem eru illa þjónaðir, stuðningsbyrði af ruglingslegum sniðum og lagalegan eða mannorðsskaða af rangþýddu hágagnsemiefni. Samfelld staðfærsla forðast kostnaðarsama þýðingakreppu fyrir opnun.

Til að færa rök við forystu skaltu ramma alþjóðavæðingu sem valkost á framtíðarmarkaði. Hún er hófleg fjárfesting fyrirfram sem lækkar stórlega kostnað og tíma hverrar framtíðarmarkaðsinngöngu. Fyrir hið opinbera er drifkrafturinn lagaleg tungumálaaðgangsskylda og jafnrétti, magnsett með þýðinu sem þjónað er á hverju tungumáli.

## Andmynstur og gildrur

- **Harðkóðaðir strengir**: notendatexti bakaður í kóða, sem neyðir kóðabreytingar á málsvæði.
- **Strengjasamtenging**: að byggja setningar úr brotum, sem brýtur málfræði og orðaröð.
- **Ekki-Unicode forsendur**: kóðunargallar, [mojibake](https://en.wikipedia.org/wiki/Mojibake) (brenglaður texti af ósamræmdum stafakóðunum) og vangeta til að tákna letur.
- **Að gera ráð fyrir enskri textalengd**: uppsetningar sem stytta eða skarast þegar þýtt.
- **Að hunsa hægri-til-vinstri**: líkamlega vinstri/hægri uppsetning sem getur ekki speglast.
- **Barnaleg fleirtala**: eintölu/fleirtölu rökfræði sem er röng í flestum tungumálum.
- **Málsvæðablind snið**: harðkóðuð dagsetninga-, tölu- og gjaldmiðilssnið.
- **Þýðing án samhengis**: þýðendur giska á merkingu og framleiða villur.
- **Staðfærsla í lotum á síðustu stundu**: kreppa fyrir opnun í stað samfelldrar leiðslu.
- **Menningarleg tillitsleysi**: myndmál, litir eða dæmi sem móðga eða rugla staðbundið.

## Þroskalíkan

**Stig 1: Upphaf.** Eitt tungumál, harðkóðaðir strengir, ekki-Unicode forsendur og texti byggður með samtengingu. Alþjóðavæðing er viðbragðsdrifin: hvert nýtt málsvæði þýðir kóðabreytingu og kóðunar- og uppsetningargallar finnast fyrir tilviljun í framleiðslu.

**Stig 2: Þróun.** Sumir strengir eru útfluttir og Unicode er notað á stöðum, en vinnubrögð eru ósamræmd milli teyma. Staðfærsla er handvirk, lotu-fyrir-opnun fyrirhöfn og sníðun, fleirtölumeðhöndlun og hægri-til-vinstri stuðningur er meðhöndlaður ólíkt (eða alls ekki) frá einu teymi til næsta.

**Stig 3: Stöðlun.** Sameiginleg i18n-arkitektúr og málsvæðismeðvitað sniðbókasafn eru skjalfesti, framfylgdi staðallinn um alla skipulagsheildina. Strengjaútflutningur er athugaður með lint-reglum, þýðingastjórnunarkerfi og samfelld leiðsla eru til með hugtakaskrám og þýðingaminni og gervistaðfærsla auk fjölmálsvæðaprófunar (þar á meðal hægri-til-vinstri og langtexta málsvæðis) keyrir í CI.

**Stig 4: Stjórnun.** Staðfærsluáætlunin er mæld og stýrð gegn grunnlínum. Teymi rekja tungumálaþekju, staðfærslugæði og gallahlutföll, strengjasamstillingartöf frá innritun til þýddrar útgáfu, styttingar- og hægri-til-vinstri birtingargalla gripna á útgáfu, þýðingarkostnað á málsvæði og tíma til að opna nýtt málsvæði, og þessir mælikvarðar hliða útgáfur og knýja hvar á að fjárfesta í mannlegri rýni á móti vélþýðingu.

**Stig 5: Samhæfing.** Alþjóðavæðing og staðfærsla eru stöðugt bættar og samþættar um skipulagsheildina. Staðfærsla er samfelld, vél- og mannleg þýðing er valin af ásetningi eftir efnisflokki og menningaraðlögun er kerfisbundin. Skipulagsheildin bætir við, leggur niður og endurmarkar málsvæði sem svar við markaðs- og jafnréttissönnunargögnum og ný málsvæði opnast hratt á háum gæðum án endurbótar.

## Hugmyndir til umræðu

- Hve snemma ætti vara að alþjóðavæðast ef alþjóðleg eftirspurn er óviss?
- Hvar er vélþýðing ásættanleg og hvar verður mannleg rýni að koma til?
- Hvernig heldurðu hugtakanotkun samræmdri yfir mörg tungumál og teymi?
- Hve mikil svæðisbundin menningaraðlögun er virði aukins afbrigðaviðhalds?
- Hvernig ætti að forgangsraða og prófa hægri-til-vinstri og minnihlutamálastuðning?
- Hvernig gefurðu þýðendum nægt samhengi án þess að hægja á leiðslunni?

## Helstu atriði

- Alþjóðavæddu arkitektúrinn einu sinni. Staðfærðu efni oft.
- Notaðu Unicode alls staðar, fluttu alla strengi út og tengdu aldrei saman þýðingar.
- Skipuleggðu fyrir textaþenslu, hægri-til-vinstri letur og málsvæðissértækar fleirtölu- og sníðareglur.
- Reku samfellda staðfærsluleiðslu með þýðingaminni, hugtakaskrám og samhengi.
- Gervistaðfærðu snemma í CI til að grípa i18n-galla fyrir raunverulega þýðingu.
- Staðfærsla er menningarleg, ekki bara málfarsleg.
- Snemmbúin alþjóðavæðing er langtum ódýrari en endurbót. Fyrir hið opinbera er hún lagaleg jafnréttiskrafa.

## Heimildir og frekari lestur

- The Unicode Consortium, *The Unicode Standard* and Common Locale Data Repository (CLDR)
- W3C Internationalisation (i18n) Activity, techniques and best practices
- Richard Ishida, W3C internationalisation articles and tutorials
- Bert Esselink, *A Practical Guide to Localisation*
- John Yunker, *Beyond Borders: Web Globalisation Strategies*
- Unicode Technical Standard #35 (locale data markup) and ICU library documentation
- IETF BCP 47 language tags
- Government multilingual service and language-access guidance
- Nielsen Norman Group and W3C articles on RTL, text expansion, and localisation UX
