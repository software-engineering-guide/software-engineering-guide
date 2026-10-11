# 8.5 Prófana- og ferlasjálfvirkni

## Yfirlit og tilgangur

Prófana- og ferlasjálfvirkni er sú venja að skipta endurtekinni, handvirkri verkfræði- og rekstrarvinnu út fyrir áreiðanleg, vélkeyrð vinnuflæði. Á prófunarhliðinni þýðir það [prófasjálfvirkni](https://en.wikipedia.org/wiki/Test_automation): sjálfvirk prófasöfn sem keyra samfellt til að staðfesta réttleika, afköst og öryggi. Á ferlahliðinni nær hún yfir vélbúnaðinn í kringum hugbúnaðarafhendingu og rekstur: að safna reglufylgnisönnunargögnum, framkvæma rekstrarkeyrsluhandbækur, laga þekkt vandamál og framfylgja stjórnarhátta-, öryggis- og kostnaðarstýringum. Sameinandi hugmyndin er einföld. Allt sem er gert endurtekið og fyrirsjáanlega ætti að vera kóðað, svo það keyri samræmt, hratt og án mannlegrar leiðindavinnu.

Fyrir stór teymi er sjálfvirkni eina leiðin til að halda gæðum og stjórn frá því að hrynja í stærð. Handvirkar prófanir halda ekki í við hundruð verkfræðinga sem gera þúsundir breytinga. Þær verða flöskuháls og þekja þeirra verður ósamræmd og óáreiðanleg. Handvirk rekstrarferli líða líka fyrir það. Að endurræsa þjónustu, snúa auðkennisgögnum og safna úttektarsönnunargögnum verður allt hægt og villuhætt þegar þreytt fólk gerir það undir álagi yfir stóra landareign. Að sjálfvirknivæða þessa vinnu gerir niðurstöður endurtakanlegar. Það losar líka hæfa verkfræðinga til að einbeita sér að dómgreindarfreku vandamálunum sem sannarlega þurfa mannlega innsýn.

Í fyrirtækja- og opinberu samhengi er sjálfvirkni líka lykillinn að því að gera reglufylgni sjálfbæra. Regluverkaðar skipulagsheildir verða að sýna samfellt fram á að stýringar séu til staðar og sönnunargögnum safnað. Að gera þetta í höndunum er dýrt, hægt og hætt við götum. Að sjálfvirknivæða sönnunargagnasöfnun og stýringarframfylgd breytir reglufylgni úr reglubundinni neyðaræfingu í samfelldan, sannreynanlegan eiginleika kerfisins. Þessi „reglufylgni sem kóði“ nálgun bæði lækkar kostnað og styrkir fullvissuna sem úttektaraðilar og eftirlitsaðilar krefjast.

## Meginreglur

- Sjálfvirknivæddu vinnu sem er endurtekin, fyrirsjáanleg og reglubundin. Taktu frá mannlega fyrirhöfn fyrir dómgreind.
- Gerðu sjálfvirk próf hröð, áreiðanleg og ákvörðunarbundin, annars verða þau hunsuð.
- Keyrðu próf samhliða og færðu þau fyrr svo endurgjöf haldist hröð þegar safnið vex.
- Kóðaðu rekstrarferli sem [keyrsluhandbækur](https://en.wikipedia.org/wiki/Runbook) sem kóða svo þær séu útgáfustýrðar, prófanlegar og keyranlegar.
- Kjóstu vel samþætta sjálfvirkni fram yfir brothættar skriftur sem eru festar utan frá á kerfi.
- Framleiddu reglufylgnisönnunargögn sjálfvirkt sem aukaafurð venjulegra vinnuflæða.
- Haltu manni í lykkjunni fyrir áhættumiklar aðgerðir. Sjálfvirknivæddu öruggt og hversdagslegt fyrst.

## Ráðleggingar

### Byggðu hraða, áreiðanlega, samhliða prófainnviði

Prófasafn er aðeins verðmætt ef verkfræðingar treysta því og það skilar endurgjöf fljótt. Fjárfestu í prófainnviðum sem keyra söfn samhliða yfir marga vinnuþjóna, svo heildarveggklukkutími haldist lágur jafnvel þegar fjöldi prófa vex í þúsundir. Byggðu safnið upp sem pýramída: mörg hröð [einingapróf](https://en.wikipedia.org/wiki/Unit_testing), færri samþættingarpróf og lítinn fjölda enda-til-enda prófa. Þá berst mest af endurgjöf á sekúndum. Útrýmdu óstöðugum prófum miskunnarlaust. Próf sem bilar slitrótt er verra en ekkert próf, því það kennir verkfræðingum að hunsa bilanir. Útvegaðu skammlíf umhverfi eftir þörfum svo samþættingar- og enda-til-enda próf keyri gegn raunhæfum, einangruðum innviðum.

### Sjálfvirknivæddu útgáfu, reglufylgni og sönnunargagnasöfnun

Framlengdu sjálfvirkni út fyrir prófanir inn í útgáfu- og reglufylgnivinnuflæðið. Láttu leiðsluna framleiða sjálfvirkt gripina sem úttektaraðilar þurfa: skrár yfir hver samþykkti breytingu, hvaða próf keyrðu og stóðust, hvað öryggisskannanir fundu og nákvæmlega hvaða grip var settur upp. Líttu á stýringar sem kóða, svo nauðsynlegar athuganir séu framfylgdar jafnt og niðurstöður þeirra skráðar. Þessi „reglufylgni sem kóði“ breytir sönnunargagnasöfnun úr handvirku óðagoti fyrir úttekt í samfellda, alltaf núgildandi skrá. Hún gerir líka reglufylgnistöðu kerfisins vaktanlega hvenær sem er.

### Taktu upp ChatOps og keyrsluhandbækur sem kóða

Kóðaðu rekstrarferli sem keyranlegar keyrsluhandbækur geymdar í útgáfustýringu, frekar en sem prósaskjöl sem reka úr gildi. Þar sem ferli er öruggt og vel skilið skaltu tengja það við sjálfvirkni sem getur keyrt það eftir þörfum. ChatOps færir þennan rekstur inn í sameiginlegt spjallviðmót, svo rekstraraðilar ræsi og fylgist með sjálfvirkum aðgerðum í gagnsæju, samvinnuríku, skráðu samtali. Þetta gerir rekstur sýnilegan öllu teyminu og býr til sjálfvirka skrá yfir hvað var gert. Það lækkar líka þröskuldinn fyrir minna reynda verkfræðinga að keyra ferli örugglega, því sjálfvirknin kóðar réttu skrefin.

### Útfærðu sjálfvirka úrbót af varkárni

Fyrir vel skilin, endurtekin vandamál skaltu smíða sjálfvirka úrbót sem greinir ástand og beitir þekktri lagfæringu, svo sem að endurræsa bilað ferli, skala upp undir álagi, hreinsa fullan disk eða yfirfæra íhlut. Byrjaðu á áhættulitlum, háöruggum úrbótum. Krefstu mannlegrar staðfestingar fyrir allt með umtalsvert sprengisvæði. Sjálfvirk úrbót dregur úr meðaltíma til endurheimtar og útrýmir endurtekinni viðvörunarþreytu. En hún verður að byggja á traustri greiningu og innihalda varnir, því sjálfvirkni sem bregst við fölsku merki getur magnað atvik. Skráðu hverja sjálfvirka aðgerð, svo rekstraraðilar haldi fullum sýnileika og geti gripið inn í.

### Settu vélmennaferlasjálfvirkni (RPA) á réttan stað

[Vélmennaferlasjálfvirkni](https://en.wikipedia.org/wiki/Robotic_process_automation) stýrir núverandi notendaviðmótum og forritum til að sjálfvirknivæða verk, líkir eftir smellum og lyklaborðsinnsláttum sem maður myndi framkvæma. RPA á lögmætan sess sem brú fyrir arfleifðar- eða þriðja aðila kerfi sem bjóða ekkert API og er ekki hægt að samþætta öðruvísi. Notaðu hana hagnýtt fyrir slík tilvik, en þekktu takmörk hennar. Viðmótsdrifin sjálfvirkni er eðlislega brothætt: hún brotnar hvenær sem viðmótið breytist og hún tekur ekki á undirliggjandi skorti á samþættingu. Þar sem rétt API eða samþætting er tiltæk skaltu kjósa hana. Líttu á RPA sem taktískan bráðabirgðalausn, ekki stefnumótandi grunn, og skipuleggðu að skipta henni út eftir því sem kerfi nútímavæðast.

### Sjálfvirknivæddu stjórnarhátta-, öryggis- og kostnaðarstýringar

Kóðaðu skipulagsstýringar sem sjálfvirkar athuganir sem keyra samfellt: stefnu sem kóða fyrir innviðavarnarrimla, sjálfvirka öryggisskönnun í leiðslum og sjálfvirka greiningu kostnaðarfrávika og aðgerðalausra auðlinda. Sjálfvirknivæðing stjórnarhátta gerir stýringar samræmdar og ósniðgengilegar og hún skalast að magni breytinga sem handvirk rýni gæti aldrei þakið. Sama nálgun sem framfylgir öryggisstefnu getur merkt stjórnlausan skýjareikning eða vantandi nauðsynlegt merki. Stjórnarhættir færast frá reglubundinni handvirkri úttekt í samfelldan sjálfvirkan varnarrim.

## Málamiðlanir: kostir og gallar

| Val | Kostir | Gallar | Best passun |
|---|---|---|---|
| Víðtæk sjálfvirk prófun | Hröð, samræmd endurgjöf. Gerir breytingar mögulegar | Smíða- og viðhaldskostnaður. Óstöðugleikaáhætta | Öll teymi í stærð |
| Reglufylgni sem kóði | Samfelld, úttektarklár sönnunargögn | Verkfræði fyrirfram til að kóða stýringar | Regluverkaðar skipulagsheildir |
| Keyrsluhandbækur sem kóði + ChatOps | Endurtakanlegur, sýnilegur, skráður rekstur | Fyrirhöfn við að kóða og viðhalda | Teymi með raunverulegt rekstrarálag |
| Sjálfvirk úrbót | Hraðari endurheimt. Minni leiðindavinna | Áhætta ef greining er röng | Vel skilin endurtekin vandamál |
| RPA (viðmótssjálfvirkni) | Brúar kerfi án API | Brothætt. Felur samþættingargöt | Arfleifðarkerfi sem bráðabirgðalausn |
| Sjálfvirkir stjórnarhættir | Samræmdar, ósniðgengilegar stýringar | Stefnuritunar- og stillingarfyrirhöfn | Stórar, stýrðar landareignir |

Kjarnamálamiðlunin er fjárfesting fyrirfram gegn viðvarandi leiðindavinnu og áhættu. Sjálfvirkni kostar alltaf fyrirhöfn að smíða og viðhalda. Illa smíðuð sjálfvirkni, hvort sem það eru óstöðug próf, brothætt RPA eða úrbót ræst af slæmum merkjum, getur verið verri en engin, því hún rýrir traust eða magnar bilanir. Aginn er þríþættur: sjálfvirknivæddu það sem er sannarlega endurtakanlegt og áreiðanlegt, fjárfestu í að gera þá sjálfvirkni traustverða og haltu mönnum í lykkjunni þar sem dómgreind eða mikil áhætta krefst þess. Vel gert borgar sjálfvirkni sig margfalt. Gert af kæruleysi verður hún sjálf að skuld.

## Spurningar til að ræða með teyminu

1. **Keyra samþættingar- og enda-til-enda próf ykkar gegn raunhæfum, skammlífum umhverfum, eða gegn sameiginlegum prófunarkassa sem allir berjast um?** Einangruð umhverfi eftir þörfum fyrir hverja sameiningarbeiðni leyfa samþættingar- og enda-til-enda prófum að æfa raunhæfa innviði án þess að teymi blokki hvert annað eða mengi sameiginlegt ástand. Eitt sameiginlegt prófunarumhverfi verður flöskuháls og uppspretta óstöðugra, röðháðra bilana eftir því sem fleiri teymi hrúgast á. Ákveddu hvort þú getir sett upp skammlíf umhverfi, hvað þau kosta og hvaða próf þurfa þau í raun á móti hröðum staðgengli í minni. Komdu með gögn: hve oft prófunarumhverfið er keppt um, hve margar bilanir rekjast til truflunar sameiginlegs umhverfis og núverandi veggklukkutíma samþættingarþrepsins. Svarið mótar bæði áreiðanleika prófa ykkar og hve hratt efri lög pýramídans skila endurgjöf.

2. **Eru rekstrarferli kóðuð sem keyrsluhandbækur sem kóði og birt gegnum ChatOps, eða búa þau enn sem prósi sem rekur úr gildi?** Kóðaðar, útgáfustýrðar keyrsluhandbækur eru prófanlegar og keyranlegar og að keyra þær gegnum sameiginlegt spjallviðmót gerir hverja aðgerð sýnilega og sjálfvirkt skráða. Það lækkar þröskuldinn fyrir minna reyndan bakvaktarverkfræðing til að bregðast við örugglega, því sjálfvirknin kóðar réttu skrefin frekar en að treysta á hópminni. Ákveddu hvaða ferli eru örugg og nógu vel skilin til að tengja fyrst og hvernig þú heldur manninum fær um að grípa inn í. Fyrir stóra landareign tvöfaldast þetta gagnsæi sem úttektarskrá yfir hver gerði hvað og hvenær. Komdu með núverandi keyrsluhandbækur þínar, taktu eftir hverjar eru úreltar og finndu tvö eða þrjú mest keyrðu ferlin til að kóða fyrst.

3. **Í leiðslu ykkar, hvaða öryggisskannanir og stefnuathuganir blokka sameiningu og hverjar aðeins vara við?** Sjálfvirkir stjórnarhættir eru þess virði að smíða aðeins ef stýringarnar eru ósniðgengilegar, því athugun sem aðeins varar við er hunsuð undir fresti nákvæmlega eins og wiki-stefna. Ákveddu, stýringu fyrir stýringu, hvað blokkar og hvað varar við: mikilvægur veikleiki eða vantandi dulkóðunarmerki blokkar líklega, á meðan lægri-alvarleika stílniðurstaða gæti varað við. Í stærð er þetta hvernig þú framfylgir öryggis- og kostnaðarvarnarrimlum jafnt yfir magn breytinga sem engin handvirk rýni gæti þakið. Komdu með núverandi athugunarskrá þína og merktu hverja sem blokkandi eða ráðgefandi, ræddu síðan falskar-jákvæðar-hlutfallið, því hávaðasöm blokkandi athugun kennir fólki að krefjast undantekninga. Línan milli blokka og vara er þar sem stjórnarhættir ykkar annaðhvort hafa tennur eða ekki.

4. **Hvaða sjálfvirkar úrbætur erum við tilbúin að láta bregðast við án þess að maður staðfesti fyrst og hvert er sprengisvæðið ef greiningin er röng?** Sjálfvirk úrbót styttir endurheimtartíma og viðvörunarþreytu, en lagfæring ræst af fölsku merki getur breytt smávægilegu blikki í fullt rof, svo ákvörðunin um hvað keyrir án eftirlits er áhættuákvörðun, ekki þægindaákvörðun. Vegðu kraftana sem togast á: aðgerð án eftirlits er hraðust en áhættumest, á meðan mannleg staðfesting er öruggari en kemur aftur með töfina og leiðindavinnuna sem þú varst að reyna að fjarlægja. Komdu með frambjóðendaúrbæturnar raðaðar eftir tíðni og eftir verstu tilvik sprengisvæðis, söguleg falsk-jákvæð hlutföll greiningarinnar á bak við hverja og hvort hver aðgerð sé skráð og afturkræf. Fyrir stóra fyrirtækja- eða opinbera landareign skaltu bæta við formlegu breytingavaldi og afturköllunaráætlun fyrir allt sem snertir framleiðslugögn eða borgarasnúnar þjónustur, því sjálfvirk úrbót sem ekki er hægt að úttekta eða afturkalla er sú sem eftirlitsaðili mun neyða þig til að slökkva á.

5. **Hvernig fjármögnum við og úthlutum eignarhaldi á viðhaldi sjálfvirkninnar okkar svo hún rotni ekki í skuld?** Próf, keyrsluhandbækur, stefnuathuganir og RPA-vélmenni rotna öll eftir því sem kerfin í kring breytast og vanrækt sjálfvirkni er verri en engin: úrelt keyrsluhandbók gefur falska fullvissu í kreppu og bilað RPA-vélmenni sleppir hljóðlega vinnu. Spennan er að viðhald keppir við eiginleikavinnu um sömu verkfræðinga og það er ósýnilegt þar til eitthvað brotnar, svo það er fyrsta sem skorið er undir frestþrýstingi. Komdu með núverandi skrá yfir sjálfvirknieignir, bakslag óstöðugra prófa og bilaðra vélmenna og heiðarlegt mat á verkfræðingatímum sem þegar fara í viðhald á móti því sem er fjárhagsáætlað. Í fyrirtækja- eða opinberu umhverfi skaltu nefna ábyrgan eiganda fyrir hverja mikilvæga sjálfvirkni og fjármagna viðhald hennar sem skýran lið, því úttektaraðilar og atvikarýni munu spyrja hver bar ábyrgð þegar óviðhaldin stýring brást hljóðlega.

6. **Fyrir hvert arfleifðarkerfi sem við sjálfvirknivæðum með RPA, hver er áþreifanleg áætlun og kveikja til að leggja þá RPA niður í þágu raunverulegrar samþættingar?** RPA er lögmæt brú fyrir kerfi sem bjóða ekkert API, en brú án útgönguáætlunar harðnar hljóðlega í varanlega, brothætta innviði sem brotna við hverja viðmótsbreytingu og festa í sessi nákvæmlega samþættingarbilið sem hún átti að spanna. Málamiðlunin er raunveruleg: RPA skilar verðmæti hratt og ódýrt núna, á meðan rétt API-samþætting kostar meira fyrirfram en er endingargóð, svo aginn er að líta á RPA sem dagsett lán, ekki kaup. Komdu með lista RPA-vélmenna í framleiðslu, kerfin sem hvert reiðir sig á, hve oft hvert bilar og hvort nútímavæðingar- eða samþættingarviðleitni sé í raun fjármögnuð og tímasett fyrir undirliggjandi kerfi. Fyrir fyrirtækja- og opinberar landareignir sem bera áratuga gömul kjarnaforrit skaltu tengja hvert RPA-vélmenni við nefndan nútímavæðingaráfanga, því RPA sem hefur hljóðlega orðið mikilvægt án fyrningardagsetningar er tæknileg skuld sem safnar vöxtum hvert ár sem viðmótið sem það skrapar heldur áfram að breytast.

## Sjónarhorn eftir geirum

**Sprotafyrirtæki.** Með tvo eða þrjá verkfræðinga og engan tíma til að smíða innviði skaltu halda lítilli, hraðri prófapýramída sem keyrir á nokkrum mínútum á hverri breytingu og líta á hvert óstöðugt próf sem raunverulegan galla til að laga eða eyða þá vikuna. Slepptu þungum reglufylgniverkfærum og stefnu sem kóða sem þú þarft ekki enn og kóðaðu aðeins tvær eða þrjár mest keyrðu rekstrarlagfæringar þínar sem einfaldar skriftur ræstar úr spjalli. Sjálfvirknivæddu það sem fjarlægir daglega leiðindavinnu og stattu gegn því að smíða stjórnarháttavélbúnað áður en þú hefur stjórnarháttavandamál.

**Lítið fyrirtæki.** Án sérstaks prófana- eða vettvangssérfræðings skaltu halla þér að sjálfvirkni bakaðri í verkfærin sem þú borgar þegar fyrir: innbyggða prófakeyrara CI-þjónustunnar, skönnunarviðbætur hennar og stýrð umhverfi frekar en sérsmíðaða prófainnviðasmíð. Rammaðu kaup-gegn-smíða valið um viðhald sem þú getur raunhæft haldið uppi, því snjöll sérsmíðuð leiðsla sem enginn getur viðhaldið er verri útkoma en einfaldari hýst. Notaðu RPA sparlega og aðeins þar sem verkfæri seljanda brúar kerfi sem þú getur ekki samþætt öðruvísi.

**Stórfyrirtæki.** Yfir mörg teymi er markmiðið samræmdar, ósniðgengilegar stýringar í stærð sem handvirk rýni nær ekki yfir: sameiginlegir samhliða prófainnviðir með skammlífum umhverfum, stefnu-sem-kóða varnarrimlar og reglufylgnisönnunargögn framleidd sjálfvirkt úr hverri leiðslukeyrslu. Staðlaðu viðmótin svo teymi endurnýti úrbóta- og keyrsluhandbókaverkfæri í stað þess að hvert finni upp brothættar skriftur og stýrðu sjálfvirkni sem eigin, fjármögnuðu eignasafni með skýrum viðhaldsfjárhagsáætlunum. Gættu þess að athugun sem aðeins varar við hjá einu teymi sé ekki meðhöndluð sem blokkandi hjá öðru, því ósamræmd framfylgd grefur undan fullvissunni sem þú ert að borga fyrir.

**Hið opinbera.** Innkaupareglur, gagnsæisskyldur og samfelldar vöktunarkröfur gera reglufylgni sem kóða nánast nauðsynlega: hver leiðslukeyrsla ætti að skrá stýringarnar sem voru athugaðar, skannanirnar sem voru framkvæmdar og samþykktirnar sem voru veittar sem skemmdavarin, úttektarklár sönnunargögn. Kjóstu opna, flytjanlega sjálfvirkni fram yfir séreignarbindingu svo framtíðarsamningur geti flutt til annars birgis og haltu manni ábyrgum fyrir hverja úrbót sem snertir borgarasnúnar þjónustur. Þar sem áratuga gamalt kerfi neyðir RPA skaltu skjalfesta það sem yfirvegaða, tímabundna brú með opinberri nútímavæðingaráætlun og halda stjórnarháttaathugunum við lögbundna öryggisgrunnlínu á hverri breytingu.

## Dæmi

**Sprotafyrirtæki.** Sjö manna sprotafyrirtæki heldur grannri prófapýramída af aðallega hröðum einingaprófum auk fáeinna samþættingarprófa, öllum keyrandi samhliða svo heildarsafnið klárast á innan við þremur mínútum á hverri sameiningarbeiðni. Þegar próf byrjar að vera óstöðugt líta þau á það sem raunverulegan galla og laga eða eyða því þá vikuna, því með svo lítið teymi myndi ein hunsuð rauð smíði rýra traust á öllu safninu. Þau kóða líka tvær algengustu rekstrarlagfæringar sínar, að endurræsa fastan vinnuþjón og hreinsa fullan disk, sem litlar skriftur ræstar úr Slack, svo hver sem er á bakvakt geti keyrt þær örugglega án þess að kalla út eina verkfræðinginn sem skrifaði þær.

**Stórfyrirtæki.** Stórt netverslunarfyrirtæki rekur prófasafn tuga þúsunda prófa, samhliða keyrt yfir flota vinnuþjóna svo heildarsafnið klárast á mínútum. Skammlíf umhverfi setjast upp á hverja sameiningarbeiðni fyrir raunhæfar samþættingarprófanir. Rekstur gengur gegnum ChatOps: bakvaktarverkfræðingar ræsa kóðaðar keyrsluhandbækur úr spjalli og algengar bilanir eins og ofhlaðin þjónusta eru lagaðar sjálfvirkt, með aðgerðina skráða fyrir rýni. Leiðslan safnar öryggisskönnunar- og samþykktarsönnunargögnum sjálfvirkt, svo árleg úttekt styðst við alltaf núgildandi skrá frekar en handvirka sönnunargagnaleit.

**Hið opinbera.** Opinber stofnun sem lýtur ströngum samfelldum vöktunarkröfum útfærir reglufylgni sem kóða. Hver leiðslukeyrsla skráir stýringarnar sem voru athugaðar, skannanirnar sem voru framkvæmdar og samþykktirnar sem voru veittar og framleiðir skemmdavarin sönnunargögn sem fullnægja úttektaraðilum eftir þörfum. Því eitt kjarnakerfa hennar er áratuga gamalt forrit án API notar stofnunin RPA sem yfirvegaða brú til að sjálfvirknivæða gagnainnslátt í það á meðan nútímavæðingarviðleitni heldur áfram, með skýrri áætlun um að leggja RPA niður þegar rétt samþætting er til. Sjálfvirkar stjórnarháttaathuganir framfylgja lögboðnu öryggisgrunnlínunni á hverri innviðabreytingu.

## Viðskiptarök: hvatar, ávöxtun fjárfestingar og heildarkostnaður

Ávöxtun prófana- og ferlasjálfvirkni birtist sem endurheimtur verkfræðitími, hraðari og öruggari afhending, skjótari atvikaendurheimt og stórlega lægri reglufylgnikostnaður. Sjálfvirkar prófanir gera hraðar, öruggar breytingar mögulegar sem liggja til grundvallar afhendingarárangri. Sjálfvirkur rekstur og úrbætur skera leiðindavinnuna og niðurtímann sem tæma teymi og fjárhagsáætlanir. Reglufylgni sem kóði getur breytt úttekt úr vikum af handvirkum undirbúningi í venjulega fyrirspurn, sparnaður sem er bæði fjárhagslegur og orðsporslegur.

Samanburður heildareignarkostnaðar vegur raunverulegan, viðvarandi kostnað við að smíða og viðhalda sjálfvirkni gegn kostnaði þess að sjálfvirknivæða ekki. Handvirkar prófanir og rekstur kosta ekki bara klukkustundirnar sem fara í þær. Þær kosta líka gallana sem sleppa í gegn, atvikin sem standa lengi, úttektirnar sem éta sérfræðistarfsfólk og kulnun verkfræðinga sem vinna endurtekna leiðindavinnu. Fyrir forystu eru rökin einföld: sjálfvirkni breytir endurteknum rekstrarkostnaði og áhættu í einskiptis-auk-viðhalds fjárfestingu sem skalast og hún gerir gæði og reglufylgni samfelld frekar en stöku. Einn fyrirvari er vert að nefna skýrt. Sjálfvirkni verður að vera viðhaldið og treyst. Ófjármögnuð, vanrækt sjálfvirkni rotnar í skuld.

## Andmynstur og gildrur

- **Óstöðug próf umborin.** Slitróttar bilanir eyðileggja traust og kenna verkfræðingum að hunsa rauðar niðurstöður.
- **Að sjálfvirknivæða bilað ferli.** Að sjálfvirknivæða slæmt vinnuflæði lætur bara óreiðuna gerast hraðar. Lagaðu ferlið fyrst.
- **RPA sem stefna.** Að treysta á brothætta viðmótssjálfvirkni sem varanlega lausn felur og festir samþættingargöt í sessi.
- **Úrbót án traustrar greiningar.** Sjálfvirkar lagfæringar ræstar af slæmum merkjum geta magnað atvik.
- **Keyrsluhandbækur sem úreltur prósi.** Ferli sem búa í úreltum skjölum gefa falska fullvissu í kreppu.
- **Reglufylgnisönnunargögn söfnuð í höndunum.** Reglubundin handvirk sönnunargagnaleit er kostnaðarsöm og skilur eftir göt milli úttekta.
- **Enginn maður í lykkjunni fyrir áhættumiklar aðgerðir.** Full sjálfvirkni hættulegra aðgerða fjarlægir dómgreindina sem kemur í veg fyrir stórslys.

## Þroskalíkan

**Stig 1, Upphaf.** Prófanir og rekstur eru að mestu handvirk og viðbragðsdrifin. Þekja er ad hoc, ferli búa í hausum fólks eða úreltum skjölum, úrbót gerist í höndunum í atvikum og reglufylgnisönnunargögn eru sett saman í óðagoti fyrir hverja úttekt.

**Stig 2, Þróun.** Sjálfvirk próf eru til en eru hæg, óstöðug eða keyra ósamræmt og vinnubrögð eru mjög ólík milli teyma. Nokkrar rekstrarskriftur og keyrsluhandbækur eru til á stöku stað, en úrbót er enn handvirk og stjórnarháttum er framfylgt með reglubundinni rýni frekar en samfelldum athugunum.

**Stig 3, Stöðlun.** Hröð, samhliða og áreiðanleg prófainnviði eru skjalfesti staðallinn um skipulagsheildina. Keyrsluhandbækur sem kóði og ChatOps eru í almennri notkun, reglufylgnisönnunargögn eru framleidd sjálfvirkt úr leiðslukeyrslum og stjórnarhættastýringar keyra sem framfylgdar sjálfvirkar athuganir beittar samræmt yfir teymi.

**Stig 4, Stjórnun.** Sjálfvirknin sjálf er mæld og stýrð gegn grunnlínum. Þú rekur óstöðugleikahlutfall prófa, veggklukkutíma safns, meðaltíma til endurheimtar fyrir sjálfvirkt lagfærð atvik, hlutfall stýringa með sjálfvirk sönnunargögn og falsk-jákvæð hlutföll á blokkandi athugunum og heldur hverjum mælikvarða við samþykkt markmið. Úrbóta- og þekjuákvarðanir eru knúnar af þessum gögnum og hver sjálfvirk aðgerð er skráð svo þróun og afturfarir séu sýnilegar frekar en giskað á.

**Stig 5, Samhæfing.** Sjálfvirkni er stöðugt bætt og samþætt um skipulagsheildina. Sjálfvirk úrbót meðhöndlar venjuleg atvik með sönnuðum vörnum, reglufylgni er samfelld og alltaf úttektarklár og prófa-, rekstrar- og stjórnarhættaverkfærakeðjur aðlagast þegar kerfi breytast, með RPA-brýr virkt lagðar niður eftir því sem samþættingar þroskast. Menn einbeita sér að dómgreind á meðan vélar sjá um hið endurtakanlega og allt kerfið endurjafnar sig á sönnunargögnum.

## Hugmyndir til umræðu

- Hvaða rekstrarferli eru örugg til að sjálfvirknivæða fullkomlega og hver verða að halda manni í lykkjunni?
- Hvernig heldurðu stóru prófasafni hröðu og óstöðugleikalausu þegar það vex?
- Hvar er RPA réttlætanleg brú fyrir arfleifðarkerfi ykkar og hver er áætlunin um að leggja hana niður?
- Hvaða stýringar gætuð þið fært fyrst úr handvirkri úttekt yfir í samfellda reglufylgni sem kóða?
- Hvernig byggið þið traust á sjálfvirkri úrbót án þess að hætta á magnaðum atvikum?
- Hvernig fjármagnið þið viðvarandi viðhaldið sem sjálfvirkni krefst svo hún rotni ekki í skuld?

## Helstu atriði

- Sjálfvirknivæddu hið endurtekna, fyrirsjáanlega og reglubundna. Taktu frá mannlega fyrirhöfn fyrir dómgreind og áhættumiklar ákvarðanir.
- Gerðu sjálfvirk próf hröð, samhliða og áreiðanleg og útrýmdu óstöðugleika miskunnarlaust.
- Kóðaðu rekstur sem keyrsluhandbækur sem kóða og birtu þær gegnum ChatOps fyrir sýnileika og skrá.
- Framleiddu reglufylgnisönnunargögn sjálfvirkt svo úttektir styðjist við samfellda, núgildandi skrá.
- Notaðu RPA aðeins sem yfirvegaða, tímabundna brú fyrir kerfi án API og skipuleggðu niðurlagningu hennar.
- Framfylgdu stjórnarhátta-, öryggis- og kostnaðarstýringum sem samfelldum sjálfvirkum athugunum, með menn sem hafa eftirlit með áhættumiklum aðgerðum.

## Heimildir og frekari lestur

- Lisa Crispin and Janet Gregory, *Agile Testing: A Practical Guide for Testers and Agile Teams*.
- Jez Humble and David Farley, *Continuous Delivery*.
- Betsy Beyer, Chris Jones, Jennifer Petoff, and Niall Richard Murphy (eds.), *Site Reliability Engineering* (see the chapter on eliminating toil).
- Gene Kim, Jez Humble, Patrick Debois, and John Willis, *The DevOps Handbook*.
- Nicole Forsgren, Jez Humble, and Gene Kim, *Accelerate*.
- NIST Special Publication 800-53 and 800-137 (continuous monitoring).
- Open Policy Agent documentation (policy as code).
