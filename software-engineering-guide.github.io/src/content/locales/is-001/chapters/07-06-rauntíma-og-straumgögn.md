# 7.6 Rauntíma- og straumgögn

## Yfirlit og tilgangur

Flest sem þú veist um gagnaleiðslur gerir ráð fyrir að gögnin standi kyrr. Þú safnar degi af færslum, keyrir verk yfir nótt og lest niðurstöðurnar um morguninn. Rauntíma- og straumgögn snúa þeirri forsendu við. Í stað þess að vinna fullbúinn haug gagna vinnur þú endalaust flæði atburða þegar þeir berast og framleiðir svör samfellt. Þetta er munurinn á [lotuvinnslu](https://en.wikipedia.org/wiki/Batch_processing), sem vinnur á takmörkuðu, fullkláruðu gagnasafni, og [straumvinnslu](https://en.wikipedia.org/wiki/Stream_processing), sem vinnur á ótakmörkuðu flæði sem aldrei lýkur.

Fyrir stór teymi birtist straumur um leið og töf fer að skipta viðskiptin máli. Svikaákvörðun sem berst klukkustund of seint er einskis virði. Aðlögunarmerki sem lendir á morgun aðlagar ekkert. Rekstrarmælaborð sem dregst aftur úr raunveruleikanum um vakt villir um fyrir fólkinu sem horfir á það. Kafli 7.2 (gagnaverkfræði) heldur því fram að þú eigir að velja lotur sem sjálfgefið og seilast í straum aðeins þar sem töf borgar sig raunverulega, og þessi kafli tekur þig það sem eftir er: hvenær rauntími vinnur sér inn kostnað sinn og hvernig á að smíða hann án þess að kveikja í rekstrarfjárhagsáætluninni. Straumur situr nærri atburðadrifnu skilaboðamynstrunum í kafla 3.12 (atburðadrifinn arkitektúr og skilaboð), geymsluvalinu í kafla 3.4 (gagnaarkitektúr og geymsla) og mælingavinnubrögðum í kafla 9.2 (vöktun og mælingar).

Fyrirtækja- og opinbert umhverfi hækkar húfið. Banki skorar færslur fyrir svik á þeim tíma sem tekur kortalesara að blikka. Samgöngustofnun rekur ökutæki og spáir komutímum fyrir milljónir farþega. Bótastofnun fylgist með frávikum í kröfum á meðan hún heldur úttektarhæfri skrá yfir hverja ákvörðun. Í öllu þessu kemur verðmætið af því að bregðast við gögnum meðan þau eru fersk og áhættan af því að bregðast við gögnum sem eru röng, ófullkomin eða ómögulegt að endurbyggja síðar. Þessi kafli hefur skoðun á hvoru tveggja.

## Meginreglur

- Seilstu í straum aðeins þegar töf hefur skýrt viðskiptagildi. Lotur eru ódýrari og einfaldari.
- Aðgreindu takmörkuð (endanleg) gögn frá ótakmörkuðum (endalausum) gögnum og hannaðu í samræmi við það.
- Líttu á atburðatíma, ekki komutíma, sem uppsprettu sannleikans og skipuleggðu fyrir sein og óröð gögn.
- Gluggar og vatnsmerki eru hvernig þú færð endanleg svör úr óendanlegum straumum.
- Kjóstu í reynd-einu-sinni niðurstöður gegnum eins-áhrifa móttakendur fram yfir brothætt nákvæmlega-einu-sinni loforð.
- Ástandsrík vinnsla þarf eftirlitspunkta svo hún geti náð sér án þess að tapa eða tvítaka.
- Hannaðu fyrir bakþrýsting og endurvinnslu frá fyrsta degi, ekki sem eftirþanka.
- Haltu straumrökfræði vaktanlegri og úttektarhæfri. Hljóður straumur er verri en biluð lota.

## Ráðleggingar

### Réttlættu rauntíma áður en þú smíðar hann

Mikilvægasta straumákvörðunin er hvort eigi að streyma yfirleitt. Rauntími tvöfaldar nokkurn veginn rekstrarflækju þína og kostnað, því þú skiptir verki sem keyrir og stoppar fyrir kerfi sem verður að halda sér heilbrigðu á hverri sekúndu. Áður en þú skuldbindur þig skaltu nefna ákvörðunina sem fersk gögn gera mögulega og kostnaðinn við að sú ákvörðun berist of seint. Svikaskor, rekstrarviðvaranir og lifandi aðlögun standast yfirleitt kröfuna. Mælaborð sem maður skoðar tvisvar á dag gerir það nánast aldrei, sama hve fullnægjandi „rauntími“ hljómar á skipulagsfundi. Skrifaðu töfarkröfuna niður sem tölu, í sekúndum eða mínútum, og berðu hana saman við raunveruleikann. Mikið af því sem fólk kallar rauntíma er vel þjónað af örlotum sem keyra á nokkurra mínútna fresti á broti af kostnaðinum.

### Hannaðu í kringum atburðatíma, ekki vinnslutíma

Erfiðasta einstaka hugmynd í straumi er að atburðir gerast á einu augnabliki og eru unnir á öðru. Atburðatími er þegar hluturinn gerðist í raun, til dæmis þegar farþegi smellti korti. Vinnslutími er þegar kerfið þitt komst að því að meðhöndla hann. Þetta rekur stöðugt í sundur: sími missir merki í göngum og hleður upp þriggja mínútna smellum í einu, netsmáhik endurraðar skilaboðum, skipting dregst aftur úr. Ef þú reiknar á vinnslutíma sveiflast tölurnar þínar með innviðunum frekar en að endurspegla heiminn. Þetta sein-og-óröð vandamál er hjarta greinarinnar og það tengist beint atburðalíkönun í [atburðadrifnum arkitektúr](https://en.wikipedia.org/wiki/Event-driven_architecture). Stimplaðu hvern atburð með atburðatíma sínum við uppsprettuna, berðu þann tímastimpil gegnum alla leiðsluna og reiknaðu niðurstöður þínar gegn honum.

### Notaðu glugga og vatnsmerki til að fá endanleg svör

Ótakmarkaður straumur endar aldrei, svo „teldu atburðina“ hefur ekkert svar fyrr en þú afmarkar það. Gluggar gera þá afmörkun. Veltigluggar saxa tíma í föst, óskarast hólf, til dæmis hverja mínútu. Rennigluggar skarast, svo fimm mínútna gluggi sem færist fram á hverri mínútu gefur þér mjúka hreyfitölu. Lotugluggar flokka hviður virkni aðskildar með hléum aðgerðaleysis, sem hentar notendalotum vel. Þegar þú hefur glugga þarftu að ákveða hvenær gluggi er búinn, því sein gögn gætu enn borist. Vatnsmerki er mat kerfisins á að það hafi sennilega séð alla atburði upp að tilteknum atburðatíma. Þegar vatnsmerkið fer yfir enda glugga gefurðu út niðurstöðuna. Stilltu hve lengi þú bíður: haltu gluggum opnum lengur og þú þolir meiri seinkun á kostnað töf og minnis, lokaðu þeim hraðar og þú átt á hættu að missa eftirlegukindur. Ákveddu skýrt hvað verður um gögn sem berast eftir að gluggi lokar, hvort þú fleygir þeim, skráir eða gefur út leiðréttingu.

### Gerðu móttakendur eins-áhrifa og kjóstu í reynd-einu-sinni

Afhendingartryggingar hljóma einfaldar og eru það ekki. Minnst-einu-sinni afhending þýðir að hver atburður er unninn, en sumir gætu verið unnir oftar en einu sinni eftir endurtilraun, svo talningar geta blásið upp. Nákvæmlega-einu-sinni hljómar kjörið en er dýrt og, tekið bókstaflega yfir handahófskennd ytri kerfi, oft ómögulegt. Hagnýta markmiðið er í reynd-einu-sinni: sýnilega niðurstaðan er eins og hver atburður hafi verið unninn einu sinni, jafnvel þótt vélbúnaðurinn hafi endurreynt undir niðri. Þú kemst þangað með því að gera [eins-áhrifa](https://en.wikipedia.org/wiki/Idempotence) móttakendur örugga að skrifa í endurtekið, með ákvörðunarbundnum lyklum og uppfærslu-eða-innsetningum svo endurspilaður atburður skrifi yfir frekar en tvítaki. Sameinaðu minnst-einu-sinni afhendingu við eins-áhrifa skrif og þú færð réttar niðurstöður án þess að borga fyrir þunga færslusamræmingu alls staðar. Taktu frá raunverulegan nákvæmlega-einu-sinni vélbúnað fyrir þröngu staðina sem þurfa hann í raun.

### Settu eftirlitspunkta á ástandsríka vinnslu svo hún geti náð sér

Margir gagnlegir straumútreikningar eru ástandsríkir: keyrandi talningar, tengingar yfir strauma, tvítakahreinsun, svikalíkön sem muna nýlega hegðun. Það ástand býr í minni og myndi hverfa þegar ferli endurræsist. Eftirlitspunktar taka reglulega skyndimyndir af ástandinu og straumstöðunni saman, svo eftir hrun haldi kerfið áfram frá samkvæmum punkti frekar en að endurspila allt eða missa minni sitt. Stærðarsettu ástand þitt af ásetningi, því ótakmarkað ástand er algeng leið til að klára minni straumverks í framleiðslu. Notaðu fyrningu og líftíma á ástand sem þú þarft ekki lengur og vaktaðu ástandsstærð sem fyrsta flokks mælikvarða. Endurheimtartími eftir bilun er raunverulegt þjónustustigsáhyggjuefni, svo prófaðu hann áður en notendur þínir gera það.

### Streymdu úr rekstrargagnagrunnum með breytingagagnahöndun

Þú vilt oft bregðast við breytingum í gagnagrunni sem var aldrei hannaður til að gefa frá sér atburði. [Breytingagagnahöndun](https://en.wikipedia.org/wiki/Change_data_capture) (CDC) leysir þetta með því að lesa færsluskrá gagnagrunnsins og breyta hverri innsetningu, uppfærslu og eyðingu í straum breytingaatburða. Þetta er langtum betra en að spyrjast fyrir um töfluna á tímamæli, sem er hægt, missir millistig og hamrar á uppsprettuna. CDC leyfir þér að halda leitarvísitölu, skyndiminni, greiningargeymslu eða niðurstreymisþjónustu samfellt í takt við aðalgagnageymslukerfi, og gerir það án ágengra breytinga á forritinu. Líttu á breytingastrauminn sem fyrsta flokks gagnavöru: útgáfustýrðu skema hans, skjalfestu merkingu hans og fylgstu með töf hans, því allt niðurstreymis erfir þá töf.

### Kjóstu straum-fyrst arkitektúr fram yfir að viðhalda tveimur kóðagrunnum

Klassíski [Lambda-arkitektúrinn](https://en.wikipedia.org/wiki/Lambda_architecture) rekur lotulag fyrir nákvæma, fullkomna sögu samhliða hraðalagi fyrir ferskar, áætlaðar niðurstöður, og sameinar þær síðan. Hann virkar, en lætur þig skrifa og viðhalda sömu viðskiptarökfræði tvisvar, í tveimur kerfum, og sætta muninn að eilífu. Kappa-arkitektúrinn fellir þetta saman: haltu varanlegri, endurspilanlegri skrá yfir atburði og keyrðu alla vinnslu sem straumvinnslu, endurvinndu sögu með því að endurspila skrána þegar rökfræði breytist. Iðnaðurinn hefur rekið í átt að þessari straum-fyrst lögun því einn kóðagrunnur er stórkostlega ódýrari í viðhaldi og auðveldari að rökræða um. Ef þú getur tjáð lotuþarfir þínar sem endurspilun yfir varðveitta atburðaskrá forðastu tveggja kóðagrunna skattinn alveg. Notaðu skrárbundna miðlara sem varðveita sögu svo endurvinnsla sé spurning um að spóla til baka, ekki endurbyggja.

### Birtu strauma sem SQL, hlutgerð sjónarhorn og rauntíma-OLAP

Ekki allir sem þurfa straum ættu að þurfa að skrifa lágstigs straumvinnslukóða. Straum-SQL leyfir greinendum og verkfræðingum að tjá glugga, tengingar og samantektir á máli sem þeir kunna nú þegar og heldur niðurstöðum samfellt uppfærðum sem hlutgerðum sjónarhornum. Fyrir lágtafarsgreiningarfyrirspurnir yfir fersk gögn tekur rauntíma [netgreiningarvinnslu](https://en.wikipedia.org/wiki/Online_analytical_processing) (OLAP) geymsla við straumnum og svarar sneiða-og-teninga fyrirspurnum á millisekúndum, sem knýr raunverulega lifandi rekstrarmælaborð. Paraðu þetta við vörugreiningarvinnubrögðin í kafla 7.4 (vörugreining og tilraunir) þegar markmiðið er hröð endurgjöf á eiginleika og tilraunir. Veldu þessi hærra stigs verkfæri þar sem þau passa og taktu frá handskrifaða straumvinnsluaðila fyrir rökfræði sem þau geta ekki tjáð.

### Skipuleggðu bakþrýsting og endurvinnslu frá byrjun

Straumur getur borist hraðar en þú getur unnið hann. Bakþrýstingur er búnaðurinn sem leyfir hægum notanda að senda merki um að hægja á frekar en að detta um koll eða fleygja gögnum hljóðlega. Gakktu úr skugga um að hvert stig í leiðslunni virði hann og vaktaðu töf notenda sem aðalmælikvarða, því vaxandi töf er elsta viðvörunin um að þú sért að tapa kapphlaupinu. Endurvinnsla er hin getan sem fólk óskar sér að hafa byggt inn. Þegar þú finnur galla eða breytir reglu viltu endurspila sögu gegnum leiðrétta rökfræði. Það er aðeins mögulegt ef atburðaskráin þín varðveitir næga sögu og móttakendur þínir eru nógu eins-áhrifa til að taka við endurspiluninni. Hannaðu hvort tveggja inn frá fyrsta degi. Að bæta þeim við eftir á undir atvikaþrýstingi er ömurlegt.

## Málamiðlanir: kostir og gallar

| Val | Kostir | Gallar | Best passun |
| --- | --- | --- | --- |
| Lotur | Einfaldar, ódýrar, auðvelt að prófa og endurfylla | Mikil töf, úreltar milli keyrslna | Skýrslugerð, mest greining |
| Örlotur (mínútur) | Nærri rauntíma, langtum einfaldari en straumur | Ekki raunverulega samstundis | „Rauntíma“ mælaborð |
| Raunverulegur straumur (undir sekúndu) | Samstundis viðbrögð, samfelldar niðurstöður | Flókinn, kostnaðarsamur, erfitt að prófa | Svik, viðvaranir, lifandi aðlögun |
| Minnst-einu-sinni + eins-áhrifa móttakandi | Réttar niðurstöður, viðráðanlegt, seigt | Krefst agaðrar lyklahönnunar | Flestar straumleiðslur |
| Nákvæmlega-einu-sinni vélbúnaður | Sterk trygging frá enda til enda | Dýr, takmarkaður yfir kerfi | Þröng ferli með miklu í húfi |
| Lambda (lota + hraði) | Nákvæm saga auk fersks sjónarhorns | Tveir kóðagrunnar að viðhalda | Arfleifðarflutningar |
| Kappa (straum-fyrst) | Einn kóðagrunnur, endurspilanlegt | Krefst varðveittrar, varanlegrar skrár | Nýir straumvettvangar |

Kjarnaspennan er töf gegn flækju. Hvert skref í átt að rauntíma kostar þig í rekstrarbyrði, prófunarerfiðleikum og peningum, og ávöxtunin er ekki línuleg: að fara frá daglega til á nokkurra mínútna fresti er ódýrt og oft nóg, en að fara frá mínútum til undir sekúndu er þar sem kostnaðurinn safnast. Leystu spennuna með því að verðleggja ákvörðunina, ekki tæknina. Spyrðu hvaða aðgerð ferskleikinn gerir mögulega og hvað seinkun kostar, kauptu síðan aðeins jafn mikla töfarminnkun og sú aðgerð réttlætir. Þegar þú þarft straum skaltu halla þér að minnst-einu-sinni afhendingu með eins-áhrifa móttakendum og straum-fyrst skrá, því sú samsetning gefur þér réttleika og endurspilanleika án þyngstu trygginganna.

## Spurningar til að ræða með teyminu

1. **Hvaða ákvörðun gerir rauntímagögn í raun mögulega fyrir okkur og hvað kostar það þegar þau berast mínútu seint í stað samstundis?** Þetta er spurningin sem ætti að hliða hvert straumverkefni, því straumur tvöfaldar nokkurn veginn rekstrarkostnað þinn og flækju miðað við lotur. Stórt teymi getur brennt ársfjórðungum í að smíða rauntímavettvang sem þjónar mælaborðum sem maður athugar tvisvar á dag, sem eru peningar settir í eld. Komdu með áþreifanlegu aðgerðina sem gögnin knýja, hvort sem það er að loka á sviksamlega færslu, kalla út rekstraraðila eða breyta því sem notandi sér, og settu tölu á kostnað tafar fyrir hverja. Ef heiðarlega svarið er að fimm mínútna örlota myndi þjóna þörfinni er það niðurstaða sem vert er að fagna, ekki fela. Svarið ætti beint að breyta því hvort þið smíðið raunverulegan straum, sættið ykkur við örlotur eða haldið ykkur í lotum.

2. **Hvernig meðhöndlum við sein og óröð atburði og hvað verður um gögn sem berast eftir að gluggi lokar?** Sein og óröð gögn eru erfiði hluti straums og teymi sem sleppa þessari spurningu uppgötva hana í framleiðslu þegar tölur þeirra neita að stemma. Þrýstingarnir sem togast á eru töf og réttleiki: haltu gluggum opnum lengur til að ná eftirlegukindum og þú seinkar hverri niðurstöðu og eyðir meira minni, lokaðu þeim hraðar og þú fleygir hljóðlega raunverulegum gögnum. Komdu með sönnunargögn um hve seint gögn ykkar berast í raun, mælt sem bilið milli atburðatíma og vinnslutíma yfir uppsprettur ykkar, því farsímauppspretta í göngum hegðar sér allt öðruvísi en netþjónahliðaratburður. Ákveddu skýrt hvort sein gögn séu felld niður, skráð eða ræsi leiðréttingu og tryggðu að allir niðurstreymis viti hvað. Í opinberu samhengi þar sem tölur verða að vera verjanlegar getur að fleygja seinum atburðum hljóðlega verið reglufylgnivandamál, svo stefnan þarf að vera yfirveguð og skjalfest.

3. **Eru móttakendur okkar nógu eins-áhrifa til að við getum endurspilað sögu örugglega og varðveitir atburðaskráin nóg til að gera endurspilun mögulega?** Endurvinnsla er getan sem teymi óska sér oftast að þau hefðu byggt inn og byggðu oftast ekki, og hún veltur á tvennu sem vinnur saman: eins-áhrifa móttakendum sem taka við endurspiluðum atburðum án þess að tvítaka og varanlegri skrá sem varðveitir nóg sögu til að endurspila frá. Án beggja þýðir að laga rökfræðigalla að þið getið ekki hreint endurreiknað tímabilið sem varð fyrir áhrifum og eruð föst í að bæta tölur í höndunum undir þrýstingi. Komdu með núverandi varðveislugluggann þinn og áþreifanlegt próf: veldu raunverulegan galla frá síðasta ársfjórðungi og spyrðu hvort þú hefðir getað endurspilað leiðrétta rökfræði yfir gögnin sem urðu fyrir áhrifum. Togið á móti er kostnaður, þar sem að varðveita sögu og hanna eins-áhrifa skrif tekur geymslu og aga fyrirfram. En valkosturinn birtist á versta mögulega augnabliki, í atviki, svo svarið mótar hve mikið þú fjárfestir í endurspilanleika áður en þú þarft hans.

4. **Þegar straumverk hrynur, hve hratt verður það að ná sér, hve mikið ástand má það halda og höfum við í raun tímasett endurheimt undir framleiðsluálagi?** Lotuverk sem deyr má endurkeyra á morgun, en sívirk straumur sem deyr er rof í gangi, og ástandsrík verk sem halda keyrandi talningum, tengingum eða svikalíkönum geta tapað mínútum af minni eða tekið langan tíma að endurhlaða ástand eftir endurræsingu. Fyrir stórt teymi er þetta þar sem óglæsilegt smáatriði setur hljóðlega raunverulegt aðgengi þitt: ótakmarkað ástand vex þar til verk klárar minni og hæg eftirlitspunktsendurheimt breytir tíu sekúndna blikki í tíu mínútna. Þrýstingarnir sem togast á eru ferskleiki gegn öryggi, því tíðari eftirlitspunktar stytta endurheimt en bæta við kostnaði og rausnarleg ástandsvarðveisla bætir nákvæmni en á hættu á minnisþurrð. Komdu með áþreifanlegt endurheimtartímamarkmið, núverandi ástandsstærð og vaxtarferil hennar, eftirlitspunktabil þitt og niðurstöður raunverulegrar yfirfærsluæfingar frekar en vongott mat. Í fyrirtækja- og opinberu umhverfi þar sem straumurinn styður svikaskor eða almannaöryggisveitu er óprófuð endurheimtarleið rekstraráhætta sem þú hefur samþykkt án þess að mæla, svo líttu á æfinguna sem kröfu, ekki æskilegan eiginleika.

5. **Rekum við einn straum-fyrst kóðagrunn eða aðskilið lotulag og hraðalag og hvað kostar það okkur í raun að halda þeim sáttum?** Lambda-mynstrið með lotulagi fyrir nákvæma sögu auk hraðalags fyrir ferskar niðurstöður neyðir þig til að skrifa sömu viðskiptarökfræði tvisvar, í tveimur kerfum, og sætta svör þeirra að eilífu, á meðan straum-fyrst (Kappa) lögun heldur varanlegri, endurspilanlegri skrá og keyrir alla vinnslu sem straumvinnslu. Fyrir stóra skipulagsheild er tvítekna rökfræðin þar sem rek og deilutölur klekjast út, því regla breytist í einu lagi og ekki hinu og verkfræðingar eyða raunverulegum tíma í að útskýra hvers vegna þau eru ósammála. Togið í átt að því að halda báðum er tregða og þægindi sannreynds lotulags, svo vegðu það af heiðarleika gegn viðhaldsskattinum. Komdu með listann yfir útreikninga sem þið keyrið nú á báðum stöðum, atvikin sem tvö lög sem voru ósammála ollu og mat á hvort atburðaskráin ykkar varðveiti nóg sögu til að tjá lotuþarfir sem endurspilanir. Í opinberu og úttektuðu fyrirtækjasamhengi eru tvö lög sem geta skýrt frá ólíkum tölum fyrir sama tímabil sjálf reglufylgniskuld, þar sem þú verður að geta sagt hvaða tala er áreiðanleg og hvers vegna.

6. **Hver rekur þetta sívirka kerfi þegar það bilar klukkan þrjú um nótt og höfum við fjárhagsáætlað bakvaktarálagið og sérfræðifærnina sem það krefst, eða gerum við ráð fyrir lotulaga mönnun?** Straumur færir kostnað frá smíði til reksturs: kerfið verður að halda sér heilbrigðu á hverri sekúndu, sem þýðir raunverulega bakvaktarþekju, verkfræðinga sem eru fljótir í atburðatíma, vatnsmerkjum, ástandi og afhendingarmerkingu og prófanir sem eru erfiðari en fyrir verk sem keyrir og stoppar. Teymi samþykkja reglulega straumvettvang á grundvelli getu hans og fjármagna aldrei fólkið sem heldur honum á lífi, svo vettvangurinn hnignar og traust rýrnar. Málamiðlunin er umfang gegn sjálfbærni: hver viðbótar rauntímaleiðsla er enn eitt sem getur kallað einhvern út, svo spurningin er hvort töfin sem hún kaupir réttlæti varanlega rekstrarskuldbindingu. Komdu með heiðarlega skrá yfir hver á hvern straum í framleiðslu, núverandi bakvaktalotu þína og svigrúm hennar og hvar atburðatímasérþekkingin býr í raun, hvort sem það er ráðning, samstarfsaðili eða stýrð þjónusta. Fyrir opinberan aðila eða stórt fyrirtæki skaltu bæta við innkaupa- og ráðningarfyrirvara og stýrðum þjónustukostum, því rauntímavettvangur sem treystir á knappan mannauð sem þú getur ekki ráðið eða haldið er áætlun um að reka rofgjarnt kerfi undirmannað.

## Sjónarhorn eftir geirum

**Sprotafyrirtæki.** Straumur er sjaldan fyrsta hreyfing þín og að setja upp þungan vettvang getur sökkt örlitlu teymi. Veldu eitt merki sem snertir kjarnagildi þitt, settu atburði á einn varðveittan skrárbundinn miðlara og keyrðu léttan vinnsluaðila með lykluðum, eins-áhrifa móttakendum svo minnst-einu-sinni endurtilraun tvítaki aldrei. Geymdu nokkurra daga sögu svo þú getir endurspilað gegnum lagfærða rökfræði og kjóstu stýrða straumþjónustu fram yfir að reka eigin klasa, því knappasta auðlind þín er athygli verkfræðinga.

**Lítið fyrirtæki.** Þú hefur líklega engan straumsérfræðing og enga löngun til að reka sívirka innviði, svo líttu á rauntíma sem eitthvað sem þú kaupir innan verkfæra sem þú notar nú þegar frekar en kerfi sem þú mannar. Rammaðu þörfina sem töfarspurningu með tölu og í flestum tilvikum mun örlota sem endurnýjast á nokkurra mínútna fresti mæta henni á broti af kostnaði og áhættu. Veldu seljendur þar sem rauntímaeiginleikar eru gagnsæir um töf og auðvelt að falla frá og taktu frá sérsmíðaðan straum fyrir sjaldgæfa tilvikið þar sem fersk gögn knýja beint tekjur eða öryggi.

**Stórfyrirtæki.** Vandinn er samræmi og kostnaður yfir mörg teymi: sameiginlegur skrárbundinn vettvangur, staðlað atburðatíma- og seingagnastefna og eins-áhrifa móttakendur svo hópar hætti að finna upp brothættar leiðslur. Fjárhagsáætlaðu sívirka reksturinn og bakvaktarbyrðina skýrt, staðlaðu á straum-fyrst skrá svo þú forðist tvítekinn lotukóðagrunn og stýrðu straumum sem stýrðum gagnavörum með eigendum, skemaútgáfustýringu og vaktaðri töf frekar en dreifingu sérsmíðaðra verka. Raktu töf, endurheimtartíma og kostnað á straum sem eignasafnsmælikvarða.

**Hið opinbera.** Úttektarhæfni og opinber ábyrgð móta hvert val. Varðveittu hvern unninn atburð í varanlegri skrá svo tölur sem skilað er til eftirlitsaðila, farþegafjölda, bótafrávik, svikaákvarðanir, megi endurbyggja nákvæmlega og gerðu seingagnastefnuna skýra og skjalfesta frekar en að fleygja atburðum hljóðlega. Innkaup ættu að krefjast gagnaflytjanleika og upplýsingagjafar um afhendingar- og varðveislutryggingar stýrðrar þjónustu og hver endurútgáfa eftir reglubreytingu ætti að vera verjanleg endurspilun gegnum leiðrétta rökfræði, ekki handvirk bót sem enginn getur rakið.

## Dæmi

**Sprotafyrirtæki.** Neytendaforrit vill sýna notendum lifandi virknistraum og merkja grunsamlegar innskráningar um leið og þær gerast. Teymið stendur gegn því að setja upp þungan straumvettvang. Það setur atburði á einn varðveittan skrárbundinn miðlara, keyrir léttan straumvinnsluaðila fyrir innskráningaráhættu rökfræðina og nærir rauntíma OLAP-geymslu sem knýr virknistrauminn. Hver móttakandi er lyklaður og eins-áhrifa, svo minnst-einu-sinni endurtilraun tvítekur aldrei. Þegar þau finna síðar galla í áhættureglunni endurspila þau einfaldlega skrána gegnum lagfærða rökfræði yfir nótt, því þau geymdu viku af sögu og þurftu aldrei annan lotukóðagrunn.

**Stórfyrirtæki.** Smásölubanki skorar hverja kortafærslu fyrir svik innan heimildargluggans, tengir lifandi færslustrauminn við ástandsríkt líkan nýlegrar reikningshegðunar. Eftirlitspunktar leyfa skorunarþjónustunni að ná sér af hnútabilun á sekúndum án þess að tapa minni sínu um síðustu mínútur. Sérstaklega streymir breytingagagnahöndun uppfærslum úr kjarnabankagagnagrunninum í leitarvísitölu og aðlögunarþjónustu og heldur báðum ferskum án fyrirspurna á tímamæli. Rekstrarmælaborð lesa úr rauntíma OLAP-geymslu svo áhættu- og rekstrarteymi fylgist með rekstrinum þegar hann hreyfist og öll leiðslan gefur frá sér töf- og afkastamælingar sem lýst er í kafla 9.2.

**Hið opinbera.** Samgöngustofnun borgar tekur inn ökutækjastaðsetningar og fargjaldasmelli til að spá komutímum og fylgjast með þrengslum í rauntíma, nærir bæði opinber forrit og rekstrarmiðstöð. Því farþegar í göngum hlaða upp smellum í seinkuðum hviðum reiknar teymið farþegafjölda á atburðatíma með vatnsmerkjum stilltum eftir mældri seinkun og skráir hvern atburð sem berst eftir að gluggi hans lokar frekar en að fleygja honum hljóðlega. Hver unninn atburður er varðveittur í úttektarhæfri skrá svo farþegatölur sem skilað er til eftirlitsaðila megi endurbyggja nákvæmlega. Þegar fargjaldaregla breytist endurspila þau tímabilið sem varð fyrir áhrifum gegnum leiðrétta rökfræði og framleiða verjanlega endurútgáfu.

## Viðskiptarök: hvatar, ávöxtun fjárfestingar og heildarkostnaður

Ávöxtun rauntímagagna kemur af því að bregðast við meðan aðgerð skiptir enn máli. Svik gripin við heimild koma í veg fyrir tap sem næturlota myndi aðeins skýra frá. Aðlögun sem svarar innan lotu lyftir umbreytingu á vegu sem tillaga morgundagsins getur ekki. Rekstrarvöktun sem endurspeglar nútímann leyfir þér að grípa inn í áður en lítið vandamál verður rof eða opinbert atvik. Í hverju tilviki er verðmætið munurinn á að bregðast við núna og síðar, og sá munur er það sem þú ættir að magnsetja þegar þú færð rök fyrir málinu.

Heildareignarkostnaður er hærri en í lotum og heiðarleiki um það ver trúverðugleika þinn. Þú borgar fyrir sívirka innviði, fyrir verkfræðinga sem skilja atburðatíma, vatnsmerki, ástand og afhendingarmerkingu og fyrir erfiðari prófanir og bakvaktarbyrði kerfis sem verður að halda sér heilbrigðu samfellt frekar en að keyra og stoppa. Straum-fyrst arkitektúr á varðveittri skrá lækkar viðvarandi kostnað með því að spara þér tvítekinn lotukóðagrunn og að velja minnst-einu-sinni með eins-áhrifa móttakendum forðast kostnað nákvæmlega-einu-sinni vélbúnaðar frá enda til enda. Dýrustu mistökin eru að smíða rauntíma þar sem örlotur eða lotur myndu duga, svo sterkustu kostnaðarrökin eru oft ákvörðun um að streyma ekki. Rammaðu boðskapinn til forystu í kringum tilteknar töfarnæmar ákvarðanir og mælanlegan ávinning þeirra og vertu jafn skýr um hvar að halda sig í lotum sparar peninga án taps á verðmæti.

## Andmynstur og gildrur

- Að smíða straum vegna álits þegar örlota á nokkurra mínútna fresti myndi mæta þörfinni.
- Að reikna á vinnslutíma, svo tölurnar þínar sveiflast með innviðunum í stað heimsins.
- Að hunsa sein og óröð gögn þar til sátt bregst í framleiðslu.
- Að elta bókstaflegt nákvæmlega-einu-sinni alls staðar í stað minnst-einu-sinni með eins-áhrifa móttakendum.
- Ótakmarkað ástand án fyrningar, sem vex hljóðlega þar til verk klárar minni.
- Engir eftirlitspunktar, svo endurræsing tapar ástandi eða neyðir fullan endurspilun.
- Að spyrjast fyrir um rekstrargagnagrunna á tímamæli í stað breytingagagnahöndunar.
- Að viðhalda Lambda-lotulagi og hraðalagi með tvíteknum, reknandi rökfræði.
- Varðveislugluggi of stuttur til að endurspila sögu þegar þú finnur galla.
- Straumar án töfar-, afkasta- eða ferskleikamælinga, sem bila hljóðlega.

## Þroskalíkan

- **Stig 1, Upphaf:** Allt er lotur, eða fáein handsmíðuð straumverk keyra viðbragðsdrifið án vöktunar. Tölur eru reiknaðar á vinnslutíma, sein gögn eru hunsuð og endurræsing tapar ástandi. Enginn getur endurspilað sögu til að laga galla og vandamál uppgötvast þegar niðurstreymistölur neita að stemma.
- **Stig 2, Þróun:** Sum teymi reka kjarnastraumleiðslur á skrárbundnum miðlara með eftirlitspunktum og þau aðgreina atburðatíma frá vinnslutíma og nota grunnglugga. Vinnubrögð eru ósamræmd milli teyma: afhending er minnst-einu-sinni en ekki allir móttakendur eru eins-áhrifa, meðhöndlun seinna gagna er spunnin og töf er fylgst með óformlega frekar en varað við.
- **Stig 3, Stöðlun:** Atburðatími, vatnsmerki og skýr seingagnastefna eru skjalfest og beitt um skipulagsheildina. Móttakendur eru eins-áhrifa fyrir í reynd-einu-sinni niðurstöður, ástand hefur fyrningu og breytingagagnahöndun nærir niðurstreymiskerfi að venju. Varðveitt skrá styður endurspilun og töf, afköst og ferskleiki eru vöktuð með viðvörunum sem staðall um skipulagsheildina frekar en venja hvers teymis.
- **Stig 4, Stjórnun:** Straumlandareignin er mæld og stýrð gegn grunnlínum. Hver leiðsla ber þjónustustigsmarkmið fyrir töf frá enda til enda, töf notenda, endurheimtartíma, atburðatímaskekkju, hlutfall seinna atburða, ástandsstærð og kostnað á milljón atburði, allt rakið gegn samþykktum markmiðum og varað við afturför. Endurheimt er æfð og tímasett frekar en gert ráð fyrir, bakþrýstingssvigrúm og ástandsvöxtur eru vöktuð sem afkastagetumerki og nýr straumur verður að standast þessa mælikvarða áður en hann fer í framleiðslu.
- **Stig 5, Samhæfing:** Straum-fyrst arkitektúr þjónar bæði ferskum og sögulegum þörfum úr einni endurspilanlegri skrá og straum-SQL, hlutgerð sjónarhorn og rauntíma OLAP gera fersk gögn víða aðgengileg. Endurvinnsla er rútína og prófuð, vettvangurinn skalast sjálfvirkt og endurjafnar sig gegn mældu álagi og kostnaði og straumar eru lagðir niður, endurmarkaðir eða endurnýjaðir á sönnunargögnum. Straumur er samþættur viðskipta- og áhættuskipulagningu og hver straumur er vaktanlegur og úttektarhæfur frá enda til enda eftir því sem álags- og kostnaðarmyndin breytist.

## Hugmyndir til umræðu

1. Hvar í staflanum ykkar vinnur „rauntími“ sér raunverulega inn kostnað sinn og hvar er hann óskoðuð ósk?
2. Hve stórt er bilið milli atburðatíma og vinnslutíma yfir uppsprettur ykkar og mælið þið það?
3. Gætuð þið fellt Lambda lotu-og-hraða uppsetningu saman í einn straum-fyrst kóðagrunn og hvað myndi hindra það?
4. Hverjir móttakenda ykkar eru í raun eins-áhrifa og gætuð þið endurspilað gögn síðasta ársfjórðungs örugglega gegnum leiðrétta rökfræði í dag?
5. Hver er stefna ykkar fyrir gögn sem berast eftir að gluggi lokar og vita allir niðurstreymis af henni?
6. Hvernig myndi breytingagagnahöndun breyta því hvernig þið haldið leit, skyndiminnum og greiningu í takt?

## Helstu atriði

- Seilstu í straum aðeins þegar töfarnæm ákvörðun borgar fyrir hann. Lotur og örlotur eru ódýrari sjálfgefin.
- Reiknaðu á atburðatíma og líttu á sein og óröð gögn sem kjarnavandamálið, meðhöndlað með gluggum og vatnsmerkjum.
- Kjóstu minnst-einu-sinni afhendingu með eins-áhrifa móttakendum fyrir í reynd-einu-sinni niðurstöður frekar en bókstaflegt nákvæmlega-einu-sinni alls staðar.
- Settu eftirlitspunkta á ástandsríka vinnslu, afmarkaðu ástand þitt og vaktaðu töf notenda sem aðalmælikvarða.
- Notaðu breytingagagnahöndun til að streyma úr rekstrargagnagrunnum í stað þess að spyrjast fyrir.
- Kjóstu straum-fyrst arkitektúr á varðveittri, endurspilanlegri skrá fram yfir að viðhalda tveimur kóðagrunnum.
- Birtu strauma gegnum straum-SQL, hlutgerð sjónarhorn og rauntíma OLAP og haltu hverjum straumi vaktanlegum og úttektarhæfum.

## Heimildir og frekari lestur

- Tyler Akidau, Slava Chernyak, and Reuven Lax, "Streaming Systems."
- Martin Kleppmann, "Designing Data-Intensive Applications."
- Nathan Marz and James Warren, "Big Data" (Lambda architecture).
- Jay Kreps, "Questioning the Lambda Architecture" (O'Reilly Radar).
- Fabian Hueske and Vasiliki Kalavri, "Stream Processing with Apache Flink."
- Ben Stopford, "Designing Event-Driven Systems."
- Tyler Akidau and colleagues, "The Dataflow Model" (VLDB paper on windowing and watermarks).
