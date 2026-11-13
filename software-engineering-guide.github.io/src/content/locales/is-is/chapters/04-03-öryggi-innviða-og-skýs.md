# 4.3 Öryggi innviða og skýs

## Yfirlit og tilgangur

Forrit keyra á innviðum, og þessa dagana eru þeir innviðir að mestu skýjabyggðir, hugbúnaðarskilgreindir og sífellt breytilegir. Einn verkfræðingur getur nú útvegað gagnagrunn, opnað netleið eða veitt heimild með einni skipun, í stærð og á hraða sem hefðbundin breytingastýring sá aldrei fyrir. Það vald er einmitt ástæða þess að rangstilling, ekki framandi árásir, er helsta orsök skýjainnbrota. Óvart opinber geymslufata eða of víð aðgangshlutverk getur afhjúpað gögn heillar skipulagsheildar á sekúndum.

Fyrir stór fyrirtæki spanna skýjainnviðir marga veitendur, þúsundir reikninga og blöndu stýrðra þjónusta, gáma og þjónustulausra falla. Árásaryfirborðið er ekki kyrrstæður jaðar. Það er lifandi, víðfeðmt safn tilfanga og auðkenna. Fyrir hið opinbera mætir sama flækja ströngum heimildakerfum, gagnabúsetuskyldum og flokkunarmörkum sem móta hvert arkitektúrval. Í báðum er auðkennalagið orðið nýi jaðarinn: hver getur gert hvað, við hvaða tilfang, undir hvaða skilyrðum.

Þessi kafli nær yfir hvernig á að tryggja þann grunn: [auðkenna- og aðgangsstjórnun](https://en.wikipedia.org/wiki/Identity_management) (IAM), [netskiptingu í hluta](https://en.wikipedia.org/wiki/Network_segmentation), [dulkóðun](https://en.wikipedia.org/wiki/Encryption) og [lyklastjórnun](https://en.wikipedia.org/wiki/Key_management), öryggi gáma og [þjónustulausra](https://en.wikipedia.org/wiki/Serverless_computing) vinnuálaga og samfellda stöðustjórnun sem heldur ört breytilegu skýjabúi frá því að reka út í hættu.

## Meginreglur

- **Auðkenni er jaðarinn.** Aðgangsákvarðanir byggja á sterku auðkenni og fínkorna heimild, ekki netstaðsetningu.
- **Lágmarksréttindi, alltaf.** Hvert auðkenni, mannlegt eða vélrænt, fær lágmarksheimildir sem þarf og ekkert umfram.
- **Skiptu til að afmarka.** Skiptu netum og vinnuálagi í hluta svo brot á einu svæði geti ekki breiðst frjálst út.
- **Dulkóðaðu alls staðar.** Verndaðu gögn á ferð og í hvíld sjálfgefið, með vel stýrðum lyklum.
- **Óbreytanlegt og yfirlýsandi.** Skilgreindu innviði sem kóða (IaC), settu upp óbreytanlega og líttu á rek sem galla.
- **Samfelld sannprófun.** Staða er ekki einskiptis úttekt. Skannaðu og framfylgdu samfellt.
- **Örugg sjálfgefin stilling.** Sjálfgefið ástand hvers tilfangs ætti að vera læst, ekki opið.

## Ráðleggingar

### Hannaðu auðkenna- og aðgangsstjórnun af ásetningi

IAM er mikilvægasti hluti skýjaöryggis og sá sem oftast er illa stýrt.

- Notaðu **[hlutverkabyggða aðgangsstýringu](https://en.wikipedia.org/wiki/Role-based_access_control) (RBAC)** til að veita heimildir eftir starfsvirkni, og **[eigindabyggða aðgangsstýringu](https://en.wikipedia.org/wiki/Attribute-based_access_control) (ABAC)** þar sem fínni, samhengismeðvitaðar ákvarðanir þarf (byggðar á merkjum, umhverfi, gagnaflokkun eða tíma).
- Útrýmdu langlífum kyrrstæðum auðkennisgögnum í þágu skammlífra, sjálfvirkt útgefinna tákna og vinnuálagsauðkennasambands.
- Framfylgdu [MFA](https://en.wikipedia.org/wiki/Multi-factor_authentication) (fjölþátta auðkenningu) fyrir allan mannlegan aðgang og krefstu sterkrar auðkenningar fyrir forréttindaaðgerðir.
- Beittu lágmarksréttindum af nákvæmni: byrjaðu á núlli og bættu við heimildum af ásetningi. Rýndu og snyrtu ónotaðar heimildir reglulega. Aðgangur hneigist til að safnast.
- Aðskildu skyldur svo ekkert eitt auðkenni geti bæði gert og samþykkt viðkvæmar breytingar.
- Notaðu sérstaka reikninga eða verkefni til að skapa harð mörk milli umhverfa (framleiðslu, prófunar, þróunar) og milli viðskiptaeininga.

### Skiptu netum og örskiptu vinnuálagi

Flöt net leyfa árásaraðilum að reika til hliðar þegar þeir eru komnir inn. Skiptu og afmarkaðu.

- Skiptu á netstigi í þrep og svæði og leyfðu aðeins umferðina sem hvert þrep þarfnast með réttu.
- Beittu **örskiptingu** svo einstök vinnuálög eigi aðeins samskipti við tilteknu jafningjana sem þau þurfa, framfylgd með auðkennismeðvitaðri stefnu frekar en víðum undirnetsreglum.
- Neitaðu austur-vestur umferð sjálfgefið. Krefstu skýrra leyfisreglna.
- Settu viðkvæmar gagnageymslur í einkaundirnet án beinnar internetútsetningar, sem aðeins næst um stýrðar leiðir.
- Notaðu einkatengingu við stýrðar þjónustur í stað þess að fara um opna internetið þar sem mögulegt er.

### Dulkóðaðu gögn og stýrðu lyklum rétt

Dulkóðun er aðeins jafn sterk og lyklastjórnunin að baki henni.

- Dulkóðaðu **á ferð** með núverandi [TLS](https://en.wikipedia.org/wiki/Transport_Layer_Security) (Transport Layer Security) alls staðar, þar á meðal innri þjónustu-í-þjónustu umferð.
- Dulkóðaðu **í hvíld** sjálfgefið fyrir alla geymslu, gagnagrunna og afrit.
- Stýrðu lyklum með **lyklastjórnunarþjónustu (KMS)** og notaðu **[vélbúnaðaröryggiseiningu](https://en.wikipedia.org/wiki/Hardware_security_module) (HSM)** fyrir lykla með hæstu tryggingu og fyrir regluverkskröfur.
- Snúðu lyklum á áætlun og styddu hraðan snúning við grun um brot.
- Stýrðu og úttektaðu hver getur notað og stýrt lyklum aðskilið frá því hver getur nálgast gögnin, svo lyklavarsla framfylgi aðskilnaði skyldna.
- Íhugaðu viðskiptavinastýrða lykla þar sem regluverk eða samningsbundið traust krefst þess að skipulagsheildin haldi lyklunum frekar en veitandinn.

### Tryggðu gáma, Kubernetes og þjónustulausan rekstur

Hvert reikniaflslíkan kemur með eigin áhættu.

- **Gámar:** smíðaðu úr lágmarks, traustum grunnmyndum. Skannaðu myndir fyrir veikleika fyrir uppsetningu. Keyrðu sem ekki-rót. Gerðu skráarkerfi skrifvarin þar sem hægt er. Bakaðu aldrei leyndarmál inn í myndir.
- **[Kubernetes](https://en.wikipedia.org/wiki/Kubernetes):** kveiktu á RBAC og afmarkaðu þjónustureikninga þröngt. Beittu netstefnum fyrir örskiptingu. Notaðu inntökustýringar og stefnuvélar til að framfylgja stöðlum. Takmarkaðu forréttindagáma. Einangraðu viðkvæm vinnuálög. Haltu stjórnlaginu og hnútum plástruðum.
- **Þjónustulaus:** beittu lágmarksréttindum á keyrsluhlutverk hvers falls (algeng uppspretta ofheimilda). Staðfestu öll atburðainntök. Stýrðu leyndarmálum gegnum leyndarmálageymslu vettvangsins. Vaktaðu fyrir óeðlileg kallamynstur.

Hvað sem líkaninu líður skaltu halda keyrsluumhverfinu plástruðu og myndunum ferskum. Gámur er aðeins jafn öruggur og hugbúnaðurinn inni í honum.

### Stýrðu skýjaöryggisstöðu samfellt

Skýið breytist alltof hratt til að reglubundnar handvirkar úttektir haldi í við.

- Taktu upp **Cloud Security Posture Management (CSPM)** verkfæri til að greina samfellt rangstillingar, opinbera útsetningu og stefnubrot yfir reikninga.
- Skilgreindu öryggisstefnu sem kóða og framfylgdu henni við uppsetningu svo slæmar stillingar séu hindraðar áður en þær lenda.
- Kjóstu forvörn (handrið sem stöðva rangstillingu) fram yfir greiningu (viðvaranir eftir á) og sameinaðu hvort tveggja.
- Haltu nákvæmri skrá yfir tilföng og auðkenni. Þú getur ekki tryggt það sem þú sérð ekki.
- Raktu og úrbættu rek milli yfirlýstra innviða-sem-kóða og raunverulegs keyrandi ástands.

## Málamiðlanir: kostir og gallar

| Ákvörðun | Kostir | Gallar |
|---|---|---|
| RBAC | Einfalt, skiljanlegt, auðvelt að úttekta | Gróft, hlutverkasprenging í stærð |
| ABAC | Fínkorna, samhengismeðvitað, stigvaxar með merkjum | Flókið að hanna og rökræða um |
| Veitendastýrðir lyklar (KMS) | Auðvelt, samþætt, lág rekstrarbyrði | Veitandinn heldur vörslu. Minni stjórn |
| Viðskiptavinastýrðir lyklar/HSM | Full stjórn, uppfyllir strangar kröfur | Rekstraraukakostnaður, hætta á að tapa lyklum |
| Forvarnarhandrið | Stöðvar rangstillingu áður en hún gerist | Getur hindrað lögmæta vinnu, þarfnast stillingar |
| Eingöngu greinandi CSPM | Sveigjanlegt, ekki hindrandi | Skaði getur orðið fyrir greiningu |
| Örskipting | Sterk afmörkun hliðarhreyfingar | Rekstrarflækja, stefnaútbreiðsla |

Ráðandi málamiðlunin er stjórn gegn rekstrarbyrði. Þéttari stýringar (viðskiptavinastýrðir lyklar, ströng örskipting, ABAC) draga úr áhættu, en þær krefjast sérfræðiþekkingar og viðhalds sem lítil teymi eiga erfitt með að halda uppi. Rétta stigið fer eftir því hve viðkvæm gögnin eru og hvaða reglugerðir gilda. Hagnýt nálgun lagskiptir sterk örugg sjálfgefin gildi fyrir alla, tekur síðan frá aukanákvæmni fyrir áhættumestu kerfin, og kýs sjálfvirk handrið sem gera örugga valið að sjálfgefnu frekar en handvirkum aga.

## Spurningar til að ræða með teyminu

1. **Hvar munuð þið draga hörð reikninga- eða verkefnamörk og hvað á heima innan hvers?** Sérstakir reikningar og verkefni skapa sterkustu afmörkun sem skýið býður, svo brot í þróun nái ekki framleiðslu og ein viðskiptaeining geti ekki snert gögn annarrar. Ákveddu mörkaskemað áður en búið vex í þúsundir reikninga, því að bæta einangrun við flata uppbyggingu eftir á er hægt og áhættusamt. Fyrir fyrirtækja- og opinber verk varpast þessi mörk líka hreint á umhverfisaðskilnað, gagnaflokkun og sprengjusvæðistakmörk sem endurskoðendur búast við að sjá. Komdu með núverandi teikningu af því hvaða vinnuálög deila reikningi í dag og merktu hvar eitt of víðfeðmt hlutverk spannar framleiðslu og utan-framleiðslu. Ef viðkvæm gögn sitja á sama reikningi og tilraunavinnuálög eru það mörkin til að laga fyrst.

2. **Hver er staðall ykkar um hver má stýra lyklum á móti hver má nálgast dulkóðuðu gögnin?** Dulkóðun er aðeins jafn sterk og lyklastjórnun, og að aðgreina lyklavörslu frá gagnaaðgangi gerir KMS-ið þitt að framfylgdarpunkti fyrir aðskilnað skyldna. Ákveddu hver má búa til, snúa og nota lykla og tryggðu að það mengi skarist ekki við fólkið sem getur lesið gögnin sem þessir lyklar vernda. Fyrir eftirlitsskyld og opinber kerfi knýr þetta oft valið milli veitendastýrðra lykla og viðskiptavinastýrðra lykla eða HSM, sem bera meiri stjórn og meiri rekstrarhættu á að tapa lyklum. Komdu með núverandi lyklastefnur þínar og athugaðu hvort eitthvert eitt auðkenni geti bæði stýrt lykli og lesið gögnin að baki honum, því það er algengt hljótt bil. Ef varsla og aðgangur eru ekki aðskilin verndar dulkóðun í hvíld þig minna en mælaborðið gefur til kynna.

3. **Hvernig munuð þið gera örugg sjálfgefin gildi óumflýjanleg í lendingarsvæðinu ykkar frekar en bara ráðlögð?** Rangstilling, ekki framandi árásir, er helsta orsök skýjainnbrota, og lagfæringin eru forvarnarhandrið sem hindra opinberan gagnagrunn eða ódulkóðaða geymslufötu áður en hún lendir, ekki viðvaranir eftir á. Ákveddu hvaða stefnur þú munt framfylgja við uppsetningu (engin opinber geymsla, dulkóðun sjálfgefið, skyldumerki) og hverjar þú munt aðeins greina og skýra frá. Fyrir stórt teymi þýðir að kóða þetta inn í lendingarsvæði og innviða-sem-kóða sniðmát að hver nýr reikningur erfir vernd án fyrirhafnar á teymi, sem breytir öryggi úr endurteknum skatti í einskiptis fjárfestingu. Komdu með rangstillingarniðurstöður síðasta mánaðar og spyrðu hverjar forvarnarhandrið hefði stöðvað alveg. Ef stöðustjórnun þín er eingöngu greinandi getur skaði orðið áður en nokkur sér viðvörunina, svo færðu áhrifamestu athuganirnar yfir í forvörn.

4. **Hvernig útrýmið þið langlífum kyrrstæðum auðkennisgögnum án þess að brjóta sjálfvirknina sem hljóðlega byggir á þeim?** Innbyggðir aðgangslyklar sem aldrei renna út eru meðal algengustu orsaka skýjainnbrota, því einn lekinn lykill í skriftu, skrá eða hugbúnaðarsafni réttir árásaraðila varanlegan aðgang. Togið á móti er rekstrarlegt: eldri CI-verk, cron-verkefni og þriðju-aðila samþættingar gera oft ráð fyrir að kyrrstæður lykill sé til, og að skipta þeim yfir í skammlíf tákn eða vinnuálagsauðkennasamband tekur verkfræðitíma sem enginn skipulagði. Fyrir stórt teymi kemur sameiginleg flutningsleið (gefa út tákn sjálfvirkt, setja fyrningarstaðal og gefa viðvörun um hvern nýjan langlífan lykil) í veg fyrir að hver hópur finni upp eigið veikara svar. Komdu með skrá yfir hvert kyrrstætt auðkennisgagn í notkun, aldur þess, sprengjusvæði og hvort kerfið sem það nærir getur tekið við sambandsauðkenni í dag. Í fyrirtækja- og opinberu umhverfi skaltu tengja frestinn við úttektar- og heimildalotur, því auðkennisgagn sem lifir lengur en manneskjan sem bjó það til er einmitt niðurstaðan sem stöðvar samfellda heimild.

5. **Þegar tilfang er rangstillt eða lykill brotinn, hve fljótt getið þið greint, afmarkað og úrbætt það og hafið þið mælt það?** Opinber fata eða of víð hlutverk er aðeins jafn hættuleg og glugginn sem það helst opið, svo meðaltími til greiningar og úrbóta er talan sem í raun afmarkar útsetningu þína. Spennan er milli forvarnarhandriða sem stöðva mistökin við uppsetningu og greinandi stöðustjórnunar sem grípur það sem sleppur í gegn, og þú þarft heiðarlegar tölur fyrir hvort tveggja frekar en huggandi forsendu um að handrið dekki allt. Komdu með rangstillingar- og reksniðurstöður síðasta ársfjórðungs með tímastimplum, miðgildistímann frá innleiðingu til úrbóta og æfingaskrána fyrir lykilbrotssnúning. Fyrir fyrirtækja- og opinber bú sem spanna þúsundir reikninga skaltu semja um hver ber ábyrgð á úrbótum fyrir niðurstöðu sem ekkert teymi á augljóslega, því viðvörun án ábyrgs viðbragðsaðila er viðvörun sem eldist í atvik.

6. **Hvernig munuð þið halda öryggisstöðu samræmdri yfir mörg ský, reikninga og teymi án þess að hægja á öllum í skríð?** Fjölský- og fjölreikningabú sundrast hratt: hver veitandi hefur eigið IAM-líkan, eigin sjálfgefin gildi og eigin stöðuverkfæri, svo stefna framfylgd á einum stað lekur hljóðlega á öðrum. Málamiðlunin er milli miðlægrar stjórnar sem tryggir samræmi og staðbundins sjálfræðis sem leyfir teymum að hreyfa sig hratt, og að hallast of langt hvora átt tefur annaðhvort afhendingu eða leyfir stöðlum að reka. Komdu með núverandi þekjukort þitt: hvaða reikningar erfa lendingarsvæðishandrið, hverjir eru óstýrðir og hvar sama stýring er tjáð á þrjá ólíka vegu yfir veitendur. Fyrir stóra eða opinbera skipulagsheild skaltu bæta við úttektarsjónarhorni, því endurskoðendur búast við einum verjanlegum staðli beittum alls staðar, og stýring sem er til í aðalskýinu þínu en ekki því afleidda er bil sem ákveðinn árásaraðili eða matsmaður finnur fyrst.

## Sjónarhorn eftir geirum

**Sprotafyrirtæki.** Hraði og lífsafkoma vinna, svo hallaðu þér alfarið að öruggum sjálfgefnum gildum sem fylgja ókeypis: dulkóðun í hvíld á, geymsla einkamál nema manneskja opni hana, MFA á rótarreikningnum og innbyggt vinnuálagsauðkenni veitandans í stað límdra aðgangslykla. Settu ekki upp CSPM-vettvang eða handsmíðaða örskiptingu sem þú getur ekki viðhaldið. Eitt handrið sem hindrar gagnagrunn opinn internetinu kaupir mestan hluta verndarinnar fyrir eftirmiðdag af vinnu. Haltu öllu í innviðum-sem-kóða frá byrjun svo herðing stigvaxi með þér frekar en að verða endurskrift síðar.

**Lítið fyrirtæki.** Án sérstaks öryggisverkfræðings og með þröngt fjárhagsáætlun skaltu kjósa stýrðar þjónustur þar sem sjálfgefin gildi eru þegar hert og lyklastjórnun er séð um fyrir þig, frekar en að byggja eigin KMS-aga. Líttu á skýjaöryggi sem stillingarhreinlætisspurningu: vittu hvaða fötur og gagnagrunnar eru til, haltu þeim einkamálum, krefstu MFA og kveiktu á innbyggðum stöðuathugunum veitandans sem kosta ekkert aukalega. Þegar þú kaupir verkfæri skaltu kjósa þau sem merkja opinbera útsetningu og ódulkóðaða geymslu úr kassanum, því þessi tvenn mistök valda flestum forðanlegum innbrotum.

**Stórfyrirtæki.** Raunverulegi vandinn er samræmi yfir þúsundir reikninga og mörg teymi, svo verkið er vettvangsvinna: lendingarsvæði sem útvega hvern reikning hertan, handrið framfylgd sem stefna-sem-kóði og CSPM sem skannar samfellt fyrir rek. Staðlaðu IAM-líkanið, lyklavörslureglurnar og skiptingargrunnlínuna svo hópar hætti að finna upp veikari útgáfur, og mældu stöðu yfir búið frekar en að treysta orði hvers teymis. Fjárhagsáætlaðu viðvarandi verkfræði til að halda stefnum núgildandi þegar veitendur bæta við þjónustum og búið vex.

**Hið opinbera.** Innkaupareglur, gagnabúsetuskyldur og heimildakerfi móta hvert val, svo öryggisstýringar tvöfaldast sem úttektargögn. Kjóstu FIPS-vottaða lyklastjórnun með vörslu aðgreinda frá gagnaaðgangi, einangruð svæði sem halda gögnum innan landamæra og undirritaðar, skannaðar gámamyndir með ströngri inntökustýringu. Birtu varnirnar sem þú getur, nærðu samfellda stöðustjórnun beint inn í áframhaldandi heimild og krefstu þess að söluaðilar upplýsi um sjálfgefnar stillingar sínar og styðji skiptingar- og lyklavörslustýringarnar sem flokkunarmörk þín krefjast.

## Dæmi

**Sprotafyrirtæki.** Lítið sprotafyrirtæki rekur allt á einum skýjareikningi og getur ekki mannað vettvangsteymi, svo það hallast að sjálfgefnum gildum sem fylgja örugg: dulkóðun í hvíld sjálfgefið, geymslufötur einkamál nema manneskja opni þær beinlínis og MFA krafist á rótarreikningnum. Í stað langlífra aðgangslykla límdra inn í CI notar það innbyggt vinnuálagsauðkenni veitandans svo leiðslan fái skammlíf auðkennisgögn sjálfvirkt. Eitt ókeypis handrið sem merkir hvern gagnagrunn opinn internetinu bjargar þeim frá algengustu og dýrustu skýjamistökunum, á kostnað eins eftirmiðdags í uppsetningu.

**Stórfyrirtæki.** Fjölmiðlafyrirtæki sem rekur þúsundir reikninga yfir tvo skýjaveitendur framfylgir lendingarsvæðismynstri: hver reikningur er útvegaður úr sniðmáti með dulkóðun í hvíld sjálfgefið, engum opinberum aðgangi að geymslu, skyldumerkjum og grunnlínu handriðsstefna. CSPM skannar samfellt fyrir rek og vinnuálagsauðkennasamband hefur útrýmt langlífum lyklum fyrir CI-kerfi. Þegar hönnuður reynir óvart að opna gagnagrunn internetinu hindrar forvarnarstefna breytinguna og stofnar miða sjálfvirkt.

**Hið opinbera.** Varnartengd stofnun starfar á einangruðu skýjasvæði þar sem gagnabúseta er framfylgd með stefnu svo engin gögn fari yfir landamæri. Viðkvæmustu lyklarnir búa í FIPS-vottuðum (Federal Information Processing Standards) HSM, með lyklavörslu aðgreinda frá gagnaaðgangi til að framfylgja aðskilnaði skyldna. Kubernetes-klasar nota strangar netstefnur og inntökustýringar. Sérhver gámamynd er skönnuð og undirrituð áður en hún má keyra. Samfelld stöðustjórnun nærir beint sönnunargögn stofnunarinnar fyrir áframhaldandi heimild.

## Viðskiptarök: hvatar, ávöxtun fjárfestingar og heildarkostnaður

Öryggi skýjainnviða er þar sem lítil fjárfesting afstýrir skelfilegu, fréttaverðu tapi. Heildareignarkostnaðurinn felur í sér CSPM-verkfæri, lyklastjórnunarþjónustur, verkfræðitímann til að hanna lágmarksréttinda-IAM og skiptingu og viðvarandi fyrirhöfn við að halda stefnum núgildandi. Þessi kostnaður er raunverulegur en hóflegur. Kostnaðurinn við að sleppa honum er ein rangstillt auðlind sem afhjúpar heilan viðskiptavinagagnagrunn, ásamt eftirlitssektum, tilkynningakostnaði og varanlegum vörumerkjaskaða sem fylgir. Skýjarangstillingarinnbrot eru meðal algengustu og mest forðanlegu atvika í greininni.

Sjálfvirkni og endurnýting magna ávöxtunina. Kóðaðu örugg sjálfgefin gildi inn í lendingarsvæði og innviða-sem-kóða sniðmát, og hver nýr reikningur og vinnuálag erfir vernd án fyrirhafnar á teymi, sem breytir öryggi úr endurteknum handvirkum skatti í einskiptis vettvangsfjárfestingu. Fyrir hið opinbera og eftirlitsskyld fyrirtæki lækkar sterk stöðustjórnun líka kostnað úttekta og samfelldrar heimildar með því að framleiða sönnunargögn sjálfvirkt. Þegar þú færir rök við forystu skaltu leggja áherslu á að auðkenna- og stillingarlagið er nú aðalinnbrotsleiðin, að rangstilling er forðanleg og að handrið skera bæði áhættu og núning handvirkrar rýni.

## Andmynstur og gildrur

- **Algildisheimildir.** Að veita víðan `*` aðgang „til að fá hlutina til að virka“ og herða aldrei.
- **Langlífir kyrrstæðir lyklar.** Aðgangslyklar innbyggðir í skriftur og CI sem aldrei renna út og leka að lokum.
- **Flöt net.** Engin skipting, svo einn brotinn gestgjafi nær öllu.
- **Opinbert fyrir slysni.** Geymsla og gagnagrunnar afhjúpuð internetinu með sjálfgefnum eða kæruleysislegum stillingum.
- **Dulkóðun án lyklaaga.** Að kveikja á dulkóðun en skilja lyklaaðgang eftir galopinn eða snúa aldrei.
- **Leyndarmál bökuð í myndir.** Auðkennisgögn innbyggð í gámamyndir sem dreifast alls staðar þar sem myndin keyrir.
- **Ofheimiluð þjónustulaus hlutverk.** Föll fá langtum meira en þau þurfa því afmörkun var sleppt.
- **Eingöngu úttektarstaða.** Að greina rangstillingar eftir á í stað þess að koma í veg fyrir þær við uppsetningu.
- **Að hunsa rek.** Að láta keyrandi umhverfið víkja frá innviðum-sem-kóða þar til enginn veit raunverulegt ástand.

## Þroskalíkan

**Stig 1: Upphaf.** Handvirk útvegun knúin af hverjum sem þarf tilfang. Víðar algildisheimildir og langlífir kyrrstæðir lyklar. Flöt net án skiptingar. Dulkóðun beitt ósamræmt, ef yfirleitt. Engin stöðustjórnun. Rangstillingar birtast aðeins eftir að atvik neyðir spurninguna fram.

**Stig 2: Þróun.** Sum IAM-hlutverk og MFA birtast og dulkóðun í hvíld er kveikt fyrir helstu geymslur, en vinnubrögð eru mismunandi eftir teymum. Grunnnetþrep eru til án sjálfgefinnar neitunar. Stillingarrýnir gerast reglulega og í höndunum. Innviðir eru að hluta skilgreindir sem kóði, svo herðing fer eftir því hvaða hópur útvegaði reikninginn.

**Stig 3: Stöðlun.** Lágmarksréttinda RBAC og ABAC með skammlífum auðkennisgögnum eru skjalfest og framfylgt um alla skipulagsheildina. Skipting notar sjálfgefna neitun austur-vestur. Dulkóðun á ferð og í hvíld er á sjálfgefið, með lyklum í KMS á snúningsáætlun og vörslu aðgreinda frá gagnaaðgangi. Gáma- og Kubernetes-herðing er staðall og CSPM keyrir gegn skilgreindum stefnum beittum samræmt yfir hvern reikning.

**Stig 4: Stjórnun.** Staðan er mæld, ekki gert ráð fyrir henni. Þú rekur nefnda mælikvarða gegn grunnlínum og markmiðum: hlutfall auðkenna innan lágmarksréttindagrunnlínu síns, meðaltíma til greiningar og úrbóta á rangstillingum og reki, handriða- og CSPM-þekju yfir reikninga, lyklasnúningssamræmi og fjölda eftirlifandi langlífra auðkennisgagna. Niðurstöður eru flokkaðar eftir sprengjusvæði, úrbætur hafa eiganda og þjónustustigsmarkmið, og þróunargögn um þessar tölur knýja hvert næsta herðingarátak á að fara.

**Stig 5: Samhæfing.** Örugg sjálfgefin gildi eru bökuð inn í lendingarsvæði og innviði-sem-kóða svo hvert tilfang fæðist hert, og stýringar aðlagast eftir því sem búið og ógnamyndin breytast. Örskipting notar auðkennismeðvitaða stefnu. Viðskiptavinastýrðir lyklar og HSM vernda kerfin með hæstu tryggingu með vörsluaðskilnaði. Forvarnarhandrið hindra rangstillingu við uppsetningu, rek er sjálfvirkt greint og úrbætt og stöðusönnunargögn næra samfellda heimild sjálfvirkt. Öryggi er samþætt afhendingu og áhættuáætlun og skipulagsheildin leggur reglulega niður og endurmarkar stýringar eftir því sem veitendur, þjónustur og reglugerðir breytast.

## Hugmyndir til umræðu

1. Hvar er ABAC virði flækju sinnar á móti því að halda sig við RBAC í umhverfi þínu?
2. Hvernig útrýmirðu langlífum auðkennisgögnum án þess að brjóta eldri sjálfvirkni?
3. Hver er rétta skiptingin milli forvarnarhandriða og greinandi stöðustjórnunar?
4. Hvaða kerfi réttlæta viðskiptavinastýrða lykla eða HSM miðað við rekstrarkostnað þeirra?
5. Hvernig heldurðu lágmarksréttindaheimildum frá því að safnast hljóðlega aftur upp í ofréttindi?
6. Hvernig ætti fjölskýjaflækja að breyta nálgun þinni að samræmdri stöðu og stefnu?

## Helstu atriði

- Auðkenni er nýi jaðarinn. Fjárfestu í lágmarksréttinda-IAM með skammlífum auðkennisgögnum.
- Skiptu netum og örskiptu vinnuálagi til að afmarka brot.
- Dulkóðaðu á ferð og í hvíld sjálfgefið og stýrðu lyklum með KMS/HSM og vörsluaðskilnaði.
- Herðu gáma, Kubernetes og þjónustulausan rekstur. Haltu keyrsluumhverfi og myndum plástruðum.
- Kjóstu forvarnarhandrið fram yfir greiningu eftir á og stýrðu stöðu samfellt.
- Bakaðu örugg sjálfgefin gildi inn í lendingarsvæði og innviði-sem-kóða svo vernd stigvaxi sjálfvirkt.
- Rangstilling, ekki framandi árásir, er helsta orsök skýjainnbrota og hún er forðanleg.

## Heimildir og frekari lestur

- National Institute of Standards and Technology, *SP 800-207: Zero Trust Architecture*
- Centre for Internet Security, *CIS Benchmarks* (cloud providers, Kubernetes, Docker)
- Cloud Security Alliance, *Cloud Controls Matrix* and *Security Guidance for Cloud Computing*
- NIST, *SP 800-190: Application Container Security Guide*
- Liz Rice, *Container Security*
- Marco Lancini and others, *Cloud security posture and detection* engineering literature
- Provider Well-Architected security pillars (as vendor-neutral architectural guidance)
