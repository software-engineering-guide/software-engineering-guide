# 3.10 Innbyggð kerfi og rauntímakerfi

## Yfirlit og tilgangur

[Innbyggt kerfi](https://en.wikipedia.org/wiki/Embedded_system) er hugbúnaður sem keyrir á tæki frekar en á almennri tölvu. Það býr inni í bíl, gangráði, hitastilli, verksmiðjuvélmenni eða stýrieiningu. Hugbúnaðurinn er helgaður því tæki og tækið hefur yfirleitt þröng takmörk á minni, vinnslugetu og orku. Þú getur ekki alltaf bætt við tilföngum með því að smella á hnapp í skýjastjórnborði. Það sem þú afhendir er oft það sem keyrir árum saman.

[Rauntímakerfi](https://en.wikipedia.org/wiki/Real-time_computing) er kerfi þar sem réttleiki er háður tímasetningu, ekki bara því að skila réttu svari. Loftpúðastýring sem reiknar fullkomna útblásturskipun einni sekúndu of seint hefur brugðist algjörlega. Rauntímavinna bætir erfiðri spurningu við hvert verkefni: lýkur þetta fyrir frest sinn, í hvert skipti, í versta tilviki? Þetta er annar agi en afkastafyrsta hugsunin sem er algeng í vef- og skýjahugbúnaði.

Fyrir stóra skipulagsheild skiptir þetta meira máli en það virðist í fyrstu. Fyrirtæki smíða tengda bíla, lækningatæki, iðnaðarstýringar og milljarða [Internet hlutanna](https://en.wikipedia.org/wiki/Internet_of_things) (IoT) tækja. Ríkisstjórnir reka varnarvettvanga, flugtækni, raforkukerfisstýringar og lækningaeftirlit. Á þessum sviðum getur hugbúnaðargalli skaðað fólk, stöðvað framleiðslulínu eða teflt þjóðaröryggi í hættu. Reglurnar hér eru strangari, prófanir erfiðari og staðlarnir lagalega bindandi. Þessi kafli hjálpar þér að smíða hugbúnað sem er réttur, tímabær, öruggur og varinn undir raunverulegum skorðum. Hann tengist hugbúnaðarsmíði (kafli 2.9), dreifðum kerfum (kafli 3.3), stigvexti og afköstum (kafli 3.5), innviða- og skýjaöryggi (kafli 4.3) og hugbúnaðarviðhaldi (kafli 3.7).

## Meginreglur

- **Tímasetning er réttleikakrafa, ekki afkastasparisiðir.** Seint svar getur verið rangt svar.
- **Hannaðu fyrir versta tilvikið, ekki meðaltilvikið.** Rauntímaábyrgðir hvíla á hegðun í versta tilviki, ekki dæmigerðum hraða.
- **Ákveðni slær hráan hraða.** Fyrirsjáanlegt kerfi sem nær alltaf fresti sínum slær hraðara kerfi sem missir stundum af honum.
- **Tilföng eru takmörkuð og föst.** Fjárhagsáætlaðu minni, örgjörvalotur og orku af sömu ásetningi og peninga.
- **Öryggi og vernd eru verkfræðuð inn, ekki bætt við síðar.** Í eftirlitsskyldum geirum verður þú að sýna vinnu þína, ekki bara fullyrða gæði.
- **Vélbúnaðurinn er hluti kerfisins.** Þú getur ekki rökrætt um hugbúnaðinn án þess að rökræða um flöguna, skynjarana og eðlisfræðina.
- **Vettvangsuppfærslur eru lífsferilsgeta, ekki eftirþanki.** Tæki úti í heimi þurfa örugga leið til að fá lagfæringar.

## Ráðleggingar

### Flokkaðu hverja tímasetningarkröfu sem harða, fasta eða mjúka

Ekki eru allir frestir jafnir. Harður rauntímafrestur má aldrei bresta, því brestur veldur kerfisbilun eða skaða: hugsaðu um hreyflastýringu eða flugfleti. Fastur frestur þolir sjaldgæfa bresti, en seint niðurstaða er gagnslaus og er fleygt. Mjúkur rauntímafrestur rýrir verðmæti mjúklega: myndrammi sem berst örlítið seint lækkar gæði en veldur engum hamförum. Merktu hvert tímanæmt verkefni með flokki þess, því fyrirhöfnin, prófunarnákvæmnin og kostnaðurinn eru gríðarlega ólík. Tveir eiginleikar lýsa tímahegðun. [Töf](https://en.wikipedia.org/wiki/Latency_%28engineering%29) er seinkunin milli atburðar og svars. [Skjálfti](https://en.wikipedia.org/wiki/Jitter) (jitter) er breytileiki þeirrar tafar frá einu tilviki til þess næsta. Hörð rauntímakerfi láta sig jafn miklu varða að afmarka skjálfta og að lækka töf, því fyrirsjáanleiki er það sem leyfir þér að sanna að frestur sé alltaf uppfylltur.

### Veldu keyrslugrunn af ásetningi: RTOS eða bert járn

Þú hefur tvo meginundirstöður. Fastbúnaður á beru járni (bare-metal firmware) keyrir beint á vélbúnaðinum án stýrikerfis, með einfaldri lykkju og truflanameðhöndlurum. Það er smæsti og fyrirsjáanlegasti kosturinn og hentar örsmáum tækjum með eitt skýrt verkefni. [Rauntímastýrikerfi](https://en.wikipedia.org/wiki/Real-time_operating_system) (RTOS) er lítið stýrikerfi sem tímasetur verkefni eftir forgangi og tryggir tímamörk. Það gefur þér mörg verkefni, tímaáætlara og þjónustu eins og tímamæla og skilaboðaraðir, en heldur tímasetningu fyrirsjáanlegri. Veldu RTOS þegar þú hefur nokkur samtímis verkefni með ólíka fresti. Veldu bert járn þegar tækið er mjög þröngt eða tímasetning verður að vera sannanlega einföld. Fyrir hörð rauntímaverkefni skaltu kjósa forgangsrofinn, forgangsbyggðan tímaáætlara og greina hann með aðferð eins og tíðni-einhalla tímaáætlun (rate-monotonic scheduling), sem úthlutar forgangi eftir tíðni verkefnis og leyfir þér að sanna að verkefnasafnið sé tímasetjanlegt.

### Fjárhagsáætlaðu minni, örgjörva og orku sem fyrsta flokks tilföng

Líttu á hvert af skornum skammti tilfang sem fjárhagsáætlun með hörðu þaki. Fyrir minni skaltu kjósa kyrrstæða úthlutun fram yfir kvika úthlutun á hrúgunni, því kvikt minni getur sundrast og getur brugðist ófyrirsjáanlega á versta augnabliki. Margir öryggisstaðlar takmarka eða banna hrúgunotkun eftir ræsingu einmitt af þessari ástæðu. Fyrir örgjörva skaltu mæla [lengsta keyrslutíma](https://en.wikipedia.org/wiki/Worst-case_execution_time) (WCET), lengsta tímann sem verkefni getur tekið, og tímasetja gegn þeirri tölu, ekki meðaltalinu. Fyrir orku skaltu muna að mörg tæki ganga fyrir rafhlöðu eða uppskera orku, svo hannaðu vinnulotur, svefnástönd og vökuatburði til að ná orkufjárhagsáætlun sem verður að endast mánuði eða ár. Skrifaðu þessar fjárhagsáætlanir niður og rýndu þær eins og hverja aðra kröfu.

### Meðhöndlaðu truflanir og samtíma af ströngum aga

[Truflun](https://en.wikipedia.org/wiki/Interrupt) (interrupt) er vélbúnaðarmerki sem gerir hlé á núverandi vinnu til að keyra meðhöndlara strax. Truflanir eru hvernig tæki bregðast samstundis við heiminum og þær eru helsta uppspretta lúmskra galla. Haltu meðhöndlurum eins stuttum og hægt er: staðfestu atburðinn, geymdu lágmarksgögn og frestaðu raunverulegu vinnunni til venjulegs verkefnis. Því truflun getur kviknað milli hverra tveggja skipana verður þú að verja sameiginleg gögn fyrir [kapphlaupsskilyrðum](https://en.wikipedia.org/wiki/Race_condition) af varúð. Notaðu læsingalausar aðferðir, stutta krítíska hluta eða vel skilin frumstæð tól og varastu forgangsviðsnúning, þar sem lágforgangs verkefni sem heldur læsingu hindrar háforgangs verkefni. Þessi samtími deilir rökhugsun kafla 3.3, en með þrengri tímasetningu og engu svigrúmi fyrir endurtekningu.

### Skrifaðu tækjareklara sem einangra vélbúnaðaratriði

[Tækjareklari](https://en.wikipedia.org/wiki/Device_driver) er hugbúnaðarlagið sem talar við tiltekinn vélbúnaðarhluta: skynjara, útvarp, mótorstýringu. Haltu vélbúnaðarsértækum kóða á bak við hreint viðmót, svo restin af hugbúnaðinum þínum reiði sig á stöðuga ágripun frekar en á skráarföng. Þetta gerir kóðann prófanlegan utan skotmarksins, auðveldari að flytja þegar flaga klárast á lager og einfaldari að rökræða um. Skjalfestu hverja forsendu um tímasetningu, bætaröð og vélbúnaðarsérkenni, því þetta eru smáatriðin sem valda vettvangsbilunum. Þetta er smíðaagi kafla 2.9 beitt þar sem rangur biti getur stöðvað mótor.

### Taktu upp öryggisstaðalinn sem ræður þínu sviði

Ef tækið þitt getur skaðað fólk eða eignir gildir líklega [öryggisstaðall fyrir virkni](https://en.wikipedia.org/wiki/Functional_safety), og það er oft lög. IEC 61508 er almenni staðallinn fyrir öryggi rafeindakerfa og foreldri nokkurra annarra. [ISO 26262](https://en.wikipedia.org/wiki/ISO_26262) stýrir öryggi vegabifreiða. [DO-178C](https://en.wikipedia.org/wiki/DO-178C) stýrir loftbornum hugbúnaði í almennu flugi. IEC 62304 stýrir hugbúnaði lækningatækja. Fyrir kóðun er [MISRA C](https://en.wikipedia.org/wiki/MISRA_C) víða notað safn reglna sem takmarkar áhættusama eiginleika C-málsins til að gera kóða öruggari og greinanlegri. Þessir staðlar krefjast rekjanleika frá kröfu til kóða til prófs, skilgreindra ferla og sönnunargagna sem þú getur rétt endurskoðanda eða eftirlitsaðila. Taktu upp réttan snemma, því að bæta pappírsslóðinni við síðar er sársaukafullt og stundum ómögulegt.

### Prófaðu með hermun og vélbúnaði í lykkjunni

Þú getur ekki prófað innbyggðan hugbúnað eins og þú prófar vefforrit. Byggðu lagskipta stefnu. Keyrðu einingapróf á venjulegri tölvu gegn vélbúnaðarágripunarviðmótinu. Notaðu hermun til að móta tækið og umhverfi þess þegar raunverulegur vélbúnaður er af skornum skammti eða hættulegur í notkun. Notaðu síðan [vélbúnað-í-lykkjunni](https://en.wikipedia.org/wiki/Hardware-in-the-loop_simulation) (HIL) prófanir, þar sem raunverulega stýringin keyrir gegn hermdri útgáfu af eðlisfræðilega kerfinu sem hún stýrir, svo þú getir örugglega prófað bilunarástönd eins og fastan skynjara eða skyndilegt álag. Sjálfvirknivæddu þessi próf í leiðslunni þinni svo sérhver breyting sé athuguð undir raunhæfum aðstæðum áður en hún nær tæki.

### Hannaðu uppfærslur yfir loftið og tækjaöryggi frá fyrsta degi

Tæki á vettvangi munu þarfnast lagfæringa, svo skipuleggðu uppfærslur yfir loftið (OTA): leið til að afhenda nýjan fastbúnað örugglega yfir net. Örugg OTA-hönnun undirritar hverja uppfærslu með dulritun, staðfestir undirskriftina fyrir uppsetningu, uppfærir í einu lagi og getur afturkallað í þekkta góða mynd ef nýja myndin nær ekki að ræsa. Parið þetta við öryggisreglur kafla 4.3, aðlagaðar að þröngum vélbúnaði. Notaðu vélbúnaðartraustrót og öruggan ræsingarferil svo aðeins undirritaður fastbúnaður keyri. Dulkóðaðu gögn á ferð og í hvíld. Breyttu sjálfgefnum auðkennisupplýsingum og slökktu á ónotuðum viðmótum. IoT-floti er dreift kerfi með gríðarlegt árásaryfirborð, og eitt veikt sjálfgefið lykilorð getur teflt milljónum tækja í hættu í einu.

## Málamiðlanir: kostir og gallar

| Val | Kostir | Gallar / kostnaður |
|---|---|---|
| RTOS | Fjölverkavinnsla, forgangstímasetning, tímaþjónusta | Aukakostnaður, stærra fótspor, námsferill |
| Bert járn | Smæsta, fyrirsjáanlegasta, full stjórn | Erfitt að stigvaxa á mörg verkefni, meiri handavinna |
| Kyrrstæð úthlutun | Fyrirsjáanleg, engin sundrun, hentar öryggi | Minna sveigjanleg, verður að stærðarákvarða allt fyrirfram |
| Formleg öryggisvottun | Löglegur markaðsaðgangur, ströng sönnunargögn, meira traust | Mikill tíma- og peningakostnaður, hægari endurtekning |
| OTA-uppfærslur | Lagfæra og bæta tæki á vettvangi, lengja líf | Uppfærsluinnviðir, öryggisbyrði, afturköllunaráhætta |

Meginmálamiðlunin er milli fyrirsjáanleika og sveigjanleika. Allt sem gerir almennt kerfi þægilegt (kvikt minni, bakgrunnssorphirða, besta-viðleitni tímasetning, teygjanleg tilföng) vinnur gegn ábyrgðinni um að verkefni ljúki alltaf á tíma innan fasts fótspors. Innbyggð verkfræði og rauntímaverkfræði gefur vísvitandi upp sveigjanleika til að kaupa ákveðni og öryggi. Færnin er að eyða þeim skiptum aðeins þar sem frestur eða áhætta krefst þess í raun og að halda sveigjanlegu, hraðfara hlutunum (eins og skýjabakenda tækis) hinum megin við hreint mörk.

## Spurningar til að ræða með teyminu

1. **Mælið þið skjálfta, eða aðeins meðaltöf, á tímakritískum leiðum ykkar?** Réttleiki harðra rauntímakerfa hvílir á að afmarka breytileika í svartíma (skjálfta), ekki bara að lækka dæmigerða töf, því fyrirsjáanleiki er það sem leyfir þér að sanna að frestur sé alltaf uppfylltur. Stýrilykkja með lágu meðaltali en stöku stórum toppum getur samt misst af fresti sínum og valdið skaða, og meðaltalið felur það. Komdu með mælingar á dreifingunni, versta tilviki meðtöldu, fyrir hvert tímakritískt verkefni og merktu hvert sem hart, fast eða mjúkt svo prófunarnákvæmnin samsvari afleiðingu brests. Allt þægilegt í almennum kerfum (kvikt minni, sorphirða, besta-viðleitni tímasetning) ræðst á fyrirsjáanleika, svo það helst utan harðu leiðarinnar. Ef þú skýrir aðeins frá meðaltölum geturðu ekki með góðri samvisku fullyrt að harður frestur sé uppfylltur.

2. **Er RTOS-eða-bert-járn valið ykkar enn það rétta og getið þið sannað að verkefnasafnið sé tímasetjanlegt?** Keyrslugrunnurinn er ákvörðun til að endurskoða eftir því sem tækið vex: bert járn er smæstur og fyrirsjáanlegastur fyrir eitt skýrt verkefni, á meðan RTOS vinnur sér inn aukakostnað sinn þegar þú hefur nokkur samtímis verkefni með ólíka fresti. Fyrir hörð rauntímaverkefni bendir kaflinn á forgangsrofinn, forgangsbyggðan tímaáætlara greindan með aðferð eins og tíðni-einhalla tímaáætlun, sem leyfir þér að sanna að verkefnin passi frekar en að vona það. Komdu með núverandi verkefnasafn, tíðni þeirra og lengstu keyrslutíma og athugaðu hvort tímasetjanleikinn heldur í raun eða hvort verkefni hafa hljóðlega safnast umfram það sem grunnurinn getur tryggt. Varastu forgangsviðsnúning, þar sem lágforgangs verkefni sem heldur læsingu stöðvar háforgangs verkefni. Að velja grunninn af vana frekar en eftir verkefnasafninu er hvernig tímaábyrgðir rýrna hljóðlega.

3. **Hvar nákvæmlega eru mörkin milli ákveðna tækisins og sveigjanlega skýjabakendans og eru þau nógu hrein til að hreyfa sig hratt öðrum megin án þess að stofna hinu í hættu?** Meginmálamiðlun kaflans gefur upp sveigjanleika til að kaupa ákveðni og öryggi, og færnin er að eyða þeim skiptum aðeins þar sem frestur eða áhætta krefst þess í raun. Hrein mörk leyfa öryggiskritíska fastbúnaðinum að haldast íhaldssömum og vottuðum meðan skýjabakendinn endurtekur hratt, svo þau þróast hvort á sínum örugga hraða. Komdu með arkitektúr þinn og staðsettu það samskeyti: hvað verður að sanna ákveðið og uppfæra gegnum undirritaða, staðfesta leið, á móti því sem má breytast vikulega á þjóninum. Að þoka línuna dregur skýjavenjur (kvika úthlutun, besta-viðleitni tímasetningu) inn í stýriferilinn, eða hægir óþarflega á bakendanum niður í takt fastbúnaðarins. Að fá mörkin rétt er það sem heldur bæði öryggissönnunargögnunum og afhendingarhraðanum óskertum.

4. **Hvaða öryggisstaðall ræður hverri vöru og hve langt er núverandi sönnunargögn frá því sem endurskoðandi myndi samþykkja?** Staðallinn (IEC 61508, ISO 26262 fyrir vegabifreiðar, DO-178C fyrir loftborinn hugbúnað, IEC 62304 fyrir lækningatæki) er oft lög, og hann krefst rekjanleika frá kröfu til kóða til prófs sem þú getur ekki falsað í lokin. Fyrir stórt teymi er áhættan sú að hópar taki upp pappírsslóðina ójafnt, svo ein vörulína er tilbúin fyrir úttekt á meðan önnur uppgötvar miðja vegu í vottun að kröfur hennar voru aldrei raktar. Togið á móti er hraði: full rekjanleiki og MISRA C framfylgd hægja á daglegri endurtekningu, og teymi undir tímapressu freistast til að fresta sönnunargögnunum til „seinna“. Komdu með núverandi rekjanleikafylki, kyrrstæðu greiningarniðurstöðurnar sem enn eru opnar og heiðarlega bilagreiningu gegn markvissu tryggingarstigi. Í fyrirtækja- og opinberu samhengi skaltu bæta við vottunarfyrirvara og væntingum endurskoðandans, því að bæta sönnunargögnum við eftir hönnun er hægt, dýrt og stundum ómögulegt, og seinkuð vottun getur lokað markaðsaðgangi algjörlega.

5. **Ef alvarlegur galli fyndist í tæki á vettvangi á morgun, hve hratt gætuð þið lagað hann örugglega yfir allan flotann og hafið þið æft afturköllunina?** Tæki sem þú getur ekki plástrað verður varanleg öryggis- og verndarskuld, og líkamleg innköllun kostar stærðargráðum meira en undirrituð uppfærsla yfir loftið. Spennan er að kæruleysislegur uppfærslubúnaður er sjálfur árásaryfirborð og múrunarhætta: OTA-leið sem setur upp óundirritaðar myndir, eða getur ekki afturkallað slæma ræsingu, getur breytt einni slæmri útgáfu í milljónir dauðra eininga. Komdu með uppfærsluhönnun þína (dulritunarundirritun, undirskriftarstaðfestingu fyrir uppsetningu, uppsetningu í einu lagi, sjálfvirka afturköllun í þekkta góða mynd), stöðu örugga ræsingarferilsins og vélbúnaðartraustrótarinnar og síðasta skipti sem einhver æfði í raun afturköllun á raunverulegum vélbúnaði. Fyrir fyrirtækja- eða opinberan flota skaltu bæta við hver ber ábyrgð á undirritunarlyklunum og hvernig þú myndir afturkalla brotinn lykil, því lekinn lykill eða sameiginleg sjálfgefin auðkennisupplýsing getur teflt öllum flotanum í hættu í einu.

6. **Eru minnis-, örgjörva- og orkufjárhagsáætlanir ykkar skrifaðar niður með hörðum þökum og æfir prófunarstefna ykkar bæði hermun og raunverulegan vélbúnað?** Rauntímaábyrgðir hvíla á lengsta keyrslutíma og föstu tilfangafótspori, ekki meðalhegðun, svo ófjárhagsáætluð hrúguúthlutun eða óprófað versta álag er þar sem ákveðni rýrnar hljóðlega. Fyrir stórt teymi er hættan rek: verkefni safnast, minni skríður upp og enginn á fjárhagsáætlunina þar til tæki bilar á vettvangi eftir vikur af uppitíma. Málamiðlunin er þekja gegn kostnaði, því vélbúnaður-í-lykkjunni búnaður sem sprautar inn bilunum eins og föstum skynjara er dýr í smíði, á meðan hrein hermun felur tímagalla sem birtast aðeins á raunverulegri flögu. Komdu með skjalfestu fjárhagsáætlanirnar, mælda lengsta keyrslutíma gegn þeim og sönnunargögn um að leiðslan ykkar keyri einingapróf á ágripunarlaginu, hermun og vélbúnað-í-lykkjunni fyrir útgáfu. Í eftirlitsskyldu og opinberu umhverfi skaltu tengja þetta við byggingarlega prófunarþekju sem staðallinn krefst, því endurskoðandi mun vilja sönnun þess að bilunarástönd hafi verið æfð, ekki fullvissu um að meðaltilvikið hafi litið vel út.

## Sjónarhorn eftir geirum

**Sprotafyrirtæki.** Hraði og lífsafkoma ráða, svo veldu léttvægt RTOS eða einfalda lykkju á beru járni, bannaðu kvika úthlutun eftir ræsingu og mældu lengsta tíma einu mikilvægu lykkjunnar frekar en að elta vottunarfjárhagsáætlun sem þú hefur ekki. Slepptu formlegum öryggisferlum nema markaðurinn þvingi þá, en slepptu aldrei undirrituðum uppfærslum yfir loftið með sjálfvirkri afturköllun: ungt fyrirtæki lifir ekki af innköllun á vettvangi, og fjarlagfæring er munurinn á slæmri nótt og dauðri vöru. Haltu fastbúnaði tækisins litlum og íhaldssömum svo knappir verkfræðingar þínir viðhaldi ekki leiðslu sem þeir hafa ekki efni á.

**Lítið fyrirtæki.** Án innbyggðs kerfis sérfræðings á launaskrá skaltu hallast að sannreyndum einingum, viðmiðunarhönnun og söluaðila-RTOS dreifingum frekar en að rúlla þinn eigin tímaáætlara eða ræsiforrit. Rammaðu kaupa-eða-smíða valið um hver mun plástra tækið næsta áratug: keyptur öryggis- og uppfærslustakkur sem þú getur treyst á slær sérsmíðaðan sem enginn eftirlifandi getur viðhaldið. Líttu á sjálfgefin lykilorð, opin villuleitarviðmót og óundirritaðar uppfærslur sem bilanirnar sem líklegastar eru til að skaða þig, því þær eru ódýrar að koma í veg fyrir og stórskaðlegar að uppgötva á vettvangi.

**Stórfyrirtæki.** Vandinn er samræmi yfir margar vörulínur og teymi: sameiginleg keyrslugrunnsstefna, sameiginleg fjárhagsáætlunarsniðmát tilfanga, framfylgd MISRA C og kyrrstæð greining og einn vottaður uppfærslu-yfir-loftið og öruggs-ræsingarvettvangur svo hver hópur finni hann ekki upp aftur. Fjárhagsáætlaðu öryggis- og vélbúnað-í-lykkjunni byrðina skýrt, staðlaðu vélbúnaðarágripunarviðmótið svo flaga sem klárast á lager skilji ekki vöru eftir strandaða og stýrðu tímasönnunargögnum flotans, öryggisgripum og öryggisstöðu sem stýrðum eignum frekar en þjóðsögum hvers teymis. Ein veik sjálfgefin auðkennisupplýsing yfir flotann er skuldbinding á fyrirtækjastærð, svo miðlægðu stjórnun auðkenna og lykla.

**Hið opinbera.** Innkaupareglur, gagnsæi og opinber ábyrgð móta hvert val. Krefstu þess að birgjar þrói loftborinn, læknisfræðilegan eða varnarhugbúnað samkvæmt viðeigandi staðli (DO-178C, IEC 62304, IEC 61508) á tryggingarstigi sem passar við hættuna og afhendi rekjanleika- og byggingarþekjusönnunargögnin sem endurskoðendur munu rýna. Krefstu öruggrar ræsingar, vélbúnaðartraustrótar og stýrðs, undirritaðs vettvangsuppfærsluferlis, því óstaðfest uppfærsla á flug- eða raforkukerfi er óásættanleg. Kjóstu samninga sem veita réttindi til frumkóða, öryggisgripa og getu til að endurvotta með öðrum birgi, svo söluaðili sem fer á hausinn skilji ekki eftir strandað kerfi sem almenningur reiðir sig á í áratugi.

## Dæmi

**Sprotafyrirtæki.** Lítið vélbúnaðarsprotafyrirtæki sem smíðar rafhlöðuknúinn loftgæðamæli skrifar fastbúnað sinn gegn léttvægu RTOS með föstu safni verkefna og engri kvikri úthlutun eftir ræsingu, svo tækið sem fer út er tækið sem keyrir árum saman á hnapparafhlöðu. Jafnvel án vottunarfjárhagsáætlunar mælir teymið lengsta tíma skynjaralestrarlykkju sinnar og prófar eininguna gegn innsprautuðum bilunarástöndum á prófunarbekk fyrir hverja útgáfu. Undirritaðar uppfærslur yfir loftið með sjálfvirkri afturköllun leyfa þeim að laga galla yfir hverja sendu einingu, svo slæm lesning á vettvangi þýðir ekki innköllun sem unga fyrirtækið gæti ekki lifað af.

**Stórfyrirtæki.** Framleiðandi tengdra ökutækja smíðar rafræna hemlastýringu. Harða rauntímastýrilykkjan keyrir á RTOS með tíðni-einhalla tímaáætlun og kyrrstæðu minni og hvert verkefni ber mældan lengsta keyrslutíma. Teymið þróar samkvæmt ISO 26262 með fullum rekjanleika frá kröfu til kóða til prófs og framfylgir MISRA C með kyrrstæðri greiningu á hverri innritun. Vélbúnaður-í-lykkjunni búnaður spilar þúsundir vegaatburðarása, þar á meðal innsprautaðar skynjarabilanir, áður en nokkur fastbúnaður fer út. Undirritaðar OTA-uppfærslur leyfa fyrirtækinu að laga galla yfir allan flotann án kostnaðarsamrar innköllunar, með sjálfvirkri afturköllun ef bíll nær ekki að ræsa nýju myndina.

**Hið opinbera.** Landsbundið flugmálayfirvald vottar nýja flugstjórnartölvu. Birgirinn þróar loftborna hugbúnaðinn samkvæmt DO-178C á tryggingarstigi sem passar við hættuna og framleiðir sönnunargögn um kröfuþekju og byggingarlega prófunarþekju sem endurskoðendur rýna. Tímasetning er sönnuð ákveðin undir versta álagi, með afmarkaða truflanatöf og enga kvika úthlutun eftir ræsingu. Öruggur ræsingarferill og vélbúnaðartraustrót tryggja að aðeins undirritaður, vottaður fastbúnaður keyri. Vettvangsuppfærslur fylgja stýrðu, undirrituðu ferli, því óstaðfest uppfærsla á flugkerfi er óásættanleg.

## Viðskiptarök: hvatar, ávöxtun fjárfestingar og heildarkostnaður

Viðskiptarökin ráðast af kostnaði bilunar og kostnaði markaðsaðgangs. Í eftirlitsskyldum geirum geturðu alls ekki selt vöruna án öryggisvottunarinnar, svo ferlakostnaðurinn er einfaldlega aðgangsverðið. Umfram það eru gallar í tækjum á vettvangi óvenju dýrir: líkamleg innköllun kostar langt umfram skýjalagfæringu og öryggisatvik ber ábyrgð, eftirlitssektir og mannorðsskaða sem getur bundið enda á vörulínu. Að smíða öryggi, ákveðni og uppfæranleika inn frá byrjun er ódýrt miðað við að uppgötva fjarveru þeirra á vettvangi.

Rammaðu ávöxtun fjárfestingar um forðaðar innkallanir, hraðari vottun og lengra tækjalíf. Öflug OTA-geta breytir mörgum væntanlegum innköllunum í ódýrar fjarlagfæringar, og hver forðuð innköllun getur borgað fyrir alla uppfærsluáætlunina. Ströng WCET-greining og tilfangafjárhagsáætlun leyfir þér að afhenda á ódýrari vélbúnaði af öryggi, sem lækkar kostnað á einingu yfir stóran flota. Fyrir heildareignarkostnað skaltu muna að þessi tæki lifa í ár eða áratugi: viðhalds-, öryggisplástrunar- og stuðningsbyrðin (kafli 3.7) dvergar upphaflegu smíðina. Að hanna fyrir uppfæranleika, skýra vélbúnaðarágripun og skjalfestar fjárhagsáætlanir er það sem heldur þeim langa hala viðráðanlegum.

## Andmynstur og gildrur

- **Fínstilling fyrir meðaltilvikið.** Að ná frestinum „venjulega“ er að bregðast harðri rauntímakröfu.
- **Kvik úthlutun í stýriferlinum.** Hrúgusundrun veldur bilun sem birtist aðeins eftir vikur af uppitíma.
- **Feitir truflanameðhöndlarar.** Að setja þunga vinnslu inn í truflun sprengir tímafjárhagsáætlunina og skapar kapphlaupsskilyrði.
- **Að hunsa staðalinn fram að úttekt.** Að bæta við rekjanleika og sönnunargögnum seint er hægt, dýrt og stundum ómögulegt.
- **Afhending án uppfærsluleiðar.** Tæki sem þú getur ekki plástrað verður varanleg öryggis- og verndarskuld.
- **Sjálfgefin lykilorð og opin viðmót.** Eitt veikt lykilorð breytir IoT-flota í vélmennanet.
- **Prófun aðeins á hermi eða aðeins á vélbúnaði.** Hvort um sig felur galla sem hitt myndi grípa. Þú þarft bæði.
- **Að líta á vélbúnaðinn sem vandamál annars.** Tímasetning, bætaröð og skynjarasérkenni eru hugbúnaðaráhyggjuefni hér.

## Þroskalíkan

- **Stig 1: Upphaf.** Tímasetningu er vonað eftir, ekki greind. Minni er úthlutað kvikt að vild. Enginn öryggisstaðall er fylgt. Prófun er handvirk og aðeins á tæki. Ekki er hægt að uppfæra tæki eftir afhendingu, svo galli á vettvangi þýðir innköllun eða varanlega skuld.
- **Stig 2: Þróun.** Sum verkefni hafa mælda tímasetningu og grunn RTOS eða skipulögð lykkja er til staðar, en vinnubrögð eru mismunandi eftir teymum. Kóðunarleiðbeiningar eru til en ekki framfylgt. Prófun felur í sér einhverja hermun. Handvirk, áhættusöm uppfærsluleið er til á sumum vörum en ekki öðrum. Góðar venjur eru til staðar en ósamræmdar, og ekkert tryggir að næsta vörulína erfi þær.
- **Stig 3: Stöðlun.** Tímasetningarkröfur eru flokkaðar sem harðar, fastar eða mjúkar og greindar með lengsta keyrslutíma og tímasetjanleikaaðferð, skjalfestar og framfylgt um alla skipulagsheildina. Tilfangafjárhagsáætlanir fyrir minni, örgjörva og orku eru skrifaðar niður með hörðum þökum. Fylgt er viðeigandi öryggisstaðli með rekjanleika frá kröfu til kóða til prófs og MISRA C eða jafngildi er framfylgt með kyrrstæðri greiningu á hverri innritun. Vélbúnaður-í-lykkjunni prófun keyrir í leiðslunni. Undirritaðar, einlaga OTA-uppfærslur með afturköllun og öruggur ræsingarferill eru skylda grunnlínan alls staðar.
- **Stig 4: Stjórnun.** Skipulagsheildin mælir og stýrir innbyggða búinu gegn grunnlínum. Hún rekur jaðra lengsta keyrslutíma, skjálftadreifingar, frestbrestahlutföll, minnis- og orkurými, opnar kyrrstæðar greiningarniðurstöður, þekju vottunarsönnunargagna og árangurs- og afturköllunarhlutföll OTA-uppfærslna og ber þau saman við umsamin markmið. Rek gegn tilfanga- eða tímafjárhagsáætlun kallar fram aðgerð áður en tæki bilar á vettvangi og fara/ekki-fara útgáfuákvarðanir hvíla á þessum gögnum frekar en dómgreind augnabliksins. Stjórnendur sjá hvaða vörulínur eru tilbúnar fyrir úttekt og hverjar stefna í missta frest eða sprengda fjárhagsáætlun.
- **Stig 5: Samhæfing.** Ákveðni, öryggissönnunargögn og vernd eru stöðugt staðfest og sjálfvirk. Bilanainnsprautun og vélbúnaður-í-lykkjunni keyra á hverri breytingu og vottunargripir eru búnir til sem aukaafurð ferlisins. Flotinn er vaktaður, plástraður og uppfærður örugglega í stórum stíl allan langan þjónustulíftíma. Skipulagsheildin aðlagar keyrslugrunna sína, tilfangafjárhagsáætlanir og staðlaupptöku eftir því sem flögur klárast á lager, ógnir þróast og reglugerðir breytast, og endurjafnar allt tækjaeignasafnið á sönnunargögnum frekar en að bregðast við hverri kreppu einni og sér.

## Hugmyndir til umræðu

1. Hver af verkefnum tækisins þíns eru raunverulega hörð rauntímaverkefni og geturðu sannað að hvert þeirra nái alltaf fresti sínum?
2. Veistu lengsta keyrslutíma mikilvægu stýrilykkjunnar þinnar, eða aðeins meðaltalið?
3. Hvaða öryggisstaðall ræður vöru þinni og hve langt er núverandi sönnunargögn þín frá því sem hann krefst?
4. Ef alvarlegur galli fyndist í tæki á vettvangi á morgun, hvernig myndirðu laga hann og hve hratt?
5. Hvar er kvik minnisúthlutun enn til staðar í stýriferlinum þínum og hvað gerist ef hún bregst á klukkustund 1000?
6. Hvernig myndi IoT-floti þinn standast árásaraðila sem fann eina sameiginlega sjálfgefna auðkennisupplýsingu?

## Helstu atriði

- Innbyggður hugbúnaður keyrir á þröngum vélbúnaði og rauntímaréttleiki er háður tímasetningu, ekki bara réttu svari.
- Flokkaðu hvern frest sem harðan, fastan eða mjúkan og hannaðu fyrir tímasetningu í versta tilviki, afmarkaðan skjálfta og ákveðni fram yfir hráan hraða.
- Veldu RTOS eða bert járn af ásetningi og fjárhagsáætlaðu minni, örgjörva og orku sem föst, fyrsta flokks tilföng.
- Haltu truflanameðhöndlurum örsmáum, verðu sameiginleg gögn og einangraðu vélbúnað á bak við hrein, prófanleg reklaraviðmót.
- Taktu upp öryggisstaðalinn sem svið þitt krefst snemma (IEC 61508, ISO 26262, DO-178C, IEC 62304, MISRA C), með fullum rekjanleika.
- Prófaðu með hermun og vélbúnaði í lykkjunni og smíðaðu örugga, undirritaða OTA-uppfærslu með afturköllunargetu og tækjaöryggi frá fyrsta degi.

## Heimildir og frekari lestur

- IEC 61508, *Functional Safety of Electrical/Electronic/Programmable Electronic Safety-related Systems*
- ISO 26262, *Road Vehicles: Functional Safety*
- RTCA DO-178C, *Software Considerations in Airborne Systems and Equipment Certification*
- IEC 62304, *Medical Device Software: Software Life Cycle Processes*
- MISRA, *MISRA C: Guidelines for the Use of the C Language in Critical Systems*
- Michael Barr and Anthony Massa, *Programming Embedded Systems*
- Elecia White, *Making Embedded Systems*
- Jane W. S. Liu, *Real-Time Systems*
- Giorgio Buttazzo, *Hard Real-Time Computing Systems: Predictable Scheduling Algorithms and Applications*
- Colin Walls, *Embedded Software: The Works*
- Philip Koopman, *Better Embedded System Software*
- OWASP Internet of Things (IoT) security guidance
