# 8.3 Gámar, stýring og skýjabyggð tækni

## Yfirlit og tilgangur

[Gámur](https://en.wikipedia.org/wiki/OS-level_virtualization) pakkar forriti ásamt ósjálfstæðum þess í eina, flytjanlega, einangraða einingu. Hann keyrir eins á fartölvu, í prófunarumhverfi og í framleiðslu. Stýringarvettvangar, mest áberandi [Kubernetes](https://en.wikipedia.org/wiki/Kubernetes), tímasetja og stýra miklum fjölda gáma yfir flota véla. Þeir sjá um staðsetningu, skölun, heilsu, net og endurheimt. [Skýjabyggð](https://en.wikipedia.org/wiki/Cloud-native_computing) tækni er víðtækari arkitektúrstíll byggður á þessum grunni: forrit hönnuð sem laustengdar, sjálfstætt útsetjanlegar, láréttskalanlegar þjónustur sem gera ráð fyrir kviku, sjálfsviðgerðarinnviði.

Fyrir stór teymi leysa gámar og stýring eitt erfitt vandamál. Þú þarft að reka margar þjónustur, smíðaðar af mörgum teymum, áreiðanlega og skilvirkt á sameiginlegum innviðum. Gámar gefa hverju teymi samræmdan pökkunar- og keyrslusamning, sem leggur niður flokkinn „virkar á minni vél“ bilana. Stýring felur einstakar vélar á bak við sameiginlegan grunn, svo teymi setja upp á vettvang frekar en á þjóna. Þessi stöðlun er það sem leyfir þér að reka hundruð eða þúsundir þjónusta án þess að hvert teymi finni upp útsetningu, skölun og seiglu aftur.

Fyrirtæki og opinberir notendur fá flytjanleika, seiglu og leið burt frá bindingu. Á móti erfa þau raunverulega flækju og nýjar öryggisskyldur. Gámavettvangur er öflugur einmitt af því hann er forritanlegur og kvikur, sem þýðir að þú verður að stýra honum vandlega. Upprunar mynda, einangrun fjölleigu, netstefna og kostnaður verða öll áhyggjuefni á vettvangsstigi. Notendur í opinbera geiranum bæta í auknum mæli við fullveldiskröfum: stjórn á hvar gögn búa og hver hefur aðgang. Það gerir getuna til að keyra samræmd vinnuálög yfir valin umhverfi að stefnumótandi getu, ekki bara tæknilegu smáatriði.

## Meginreglur

- Pakkaðu forrit sem litlar, eins-tilgangs, óbreytanlegar gámamyndir.
- Stundaðu myndahreinlæti: lágmarksgrunnmyndir, festar útgáfur, skannaðar fyrir veikleikum og undirritaðar.
- Hannaðu forrit ástandslaus og láréttskalanleg þar sem hægt er, með ástand utan þeirra.
- Líttu á æskilegt-ástand líkan stýringarvettvangsins sem uppsprettu sannleikans og láttu hann gera við sig sjálfan.
- Framfylgdu einangrun og lágmarksréttindum milli leigjenda, vinnuálags og nafnarýma.
- Fylgdu [tólf-þátta](https://en.wikipedia.org/wiki/Twelve-Factor_App_methodology) reglunum, aðferðafræði til að smíða einnota, stillingar-utanvið, láréttskalanleg forrit, og framlengdu þær fyrir veruleika dreifðra kerfa.
- Gerðu kostnað að sýnilegu, fyrsta flokks verkfræðiáhyggjuefni, ekki eftirþanka.
- Kjóstu flytjanlegar, staðlabyggðar útdrætti til að varðveita stefnumótandi sveigjanleika.

## Ráðleggingar

### Stundaðu ítarlegt myndahreinlæti

Gámamyndin er grunneining trausts og útsetningar, svo meðhöndlaðu hana þannig. Byrjaðu á lágmarks, traustum grunnmyndum til að minnka árásarflötinn. Festu útgáfur ósjálfstæða og grunnmynda fyrir endurtakanleika. Skannaðu hverja mynd fyrir þekktum veikleikum í smíðaleiðslunni og blokkaðu þær með mikilvægum niðurstöðum. Undirritaðu myndir og staðfestu undirskriftir við útsetningu, svo aðeins samþykktar, óbreyttar myndir keyri. Haltu völdu innra myndasafni hertra grunnmynda sem teymi smíða úr. Það dreifir góðum öryggissjálfgefnum gildum sjálfvirkt.

### Notaðu Kubernetes-mynstur frekar en að finna þau upp aftur

Kubernetes umbunar teymum sem taka upp rótgróin mynstur þess og refsar teymum sem berjast gegn líkani þess. Notaðu yfirlýsandi skrár fyrir æskilegt ástand. Bættu við heilsukönnunum svo vettvangurinn geti greint og skipt út óheilbrigðum tilvikum. Settu auðlindabeiðnir og -takmörk svo tímasetjarinn geti pakkað vinnuálagi örugglega. Notaðu láréttskölun fyrir teygjanlega eftirspurn. Fyrir rekstrarrökfræði sem verður að keyra samfellt, svo sem að stýra gagnagrunni, snúa skírteinum eða sætta sérsniðnar auðlindir, notaðu rekstraraðilamynstrið, sem kóðar mannlega rekstrarþekkingu í hugbúnað sem fylgist með ástandi og bregst við. Stattu gegn freistingunni að smíða sérsmíðaða stýringu ofan á vettvanginn. Kjóstu innbyggðu hugtökin.

### Hannaðu fjölleigu af ásetningi

Þegar mörg teymi deila klasa er einangrun öryggis- og áreiðanleikakrafa, ekki munaður. Notaðu nafnarými sem leigumörk. Framfylgdu auðlindakvótum svo enginn leigjandi geti sveltt aðra. Beittu netstefnum til að takmarka umferð við það sem er leyft skýrt. Notaðu [hlutverkabundna aðgangsstýringu](https://en.wikipedia.org/wiki/Role-based_access_control) (RBAC) til að takmarka hvað hvert teymi getur gert. Fyrir vinnuálag með sterkari einangrunarþarfir skaltu íhuga aðskilda klasa eða sterkari sandkassa. Ákveddu snemma hvort líkan þitt sé mjúk fjölleiga (traust innri teymi) eða hörð fjölleiga (gagnkvæmt vantreystandi vinnuálag), því þessi tvö krefjast mjög ólíkra stýringa.

### Smíðaðu skýjabyggt: tólf-þátta og lengra

Tólf-þátta aðferðafræðin, með skýr ósjálfstæði, stillingar í umhverfinu, ástandslaus ferli, einnotagildi og svo framvegis, er áfram frábær grunnlína fyrir þjónustur sem dafna á kviku vettvangi. Framlengdu hana fyrir viðbótarveruleika dreifðra kerfa. Hannaðu fyrir hlutabilun. Gerðu aðgerðir eins-áhrifa og endurtakanlegar. Birtu heilsu og mælingar. Líttu á vöktun sem innbyggðan eiginleika frekar en viðbót. Færðu allt ástand út í stýrðar gagnaþjónustur, svo forritstilvik haldist einnota og láréttskalanleg.

### Skipuleggðu fjölskýja-, blendings- og fullveldisstefnur hagnýtt

Flytjanleiki er verðmætur, en sæktu hann með opin augu. Staðlaðu á flytjanlega útdrætti eins og gáma, Kubernetes og opin API, svo vinnuálag megi flytjast ef þarf. En forðastu gildruna að hafna hverri stýrðri þjónustu, sem skiptir raunverulegri framleiðni fyrir tilgátulegan flytjanleika. Fyrir blendings- og fullveldiskröfur skaltu hanna svo sömu vinnuálög og leiðslur geti keyrt á völdu svæði, í einkagagnaveri eða fullveldisskýi sem uppfyllir lögsögu- og gagnabúsetureglur. Gerðu fullveldis- og búsetumörk skýr í arkitektúr og stefnu.

### Gerðu kostnað sýnilegan með FinOps

Í teygjanlegu skýjaumhverfi er kostnaður bein afleiðing verkfræðiákvarðana, svo gefðu verkfræðingum sýnileika og ábyrgð. Merktu auðlindir fyrir kostnaðarskiptingu. Eignaðu útgjöld teymum og þjónustum. Sýndu kostnaðargögn við hlið afkastamælikvarða. Stilltu stærð vinnuálags, notaðu sjálfskölun til að mæta eftirspurn og endurheimtu ónotaðar auðlindir. Komdu á FinOps-venju sem leiðir saman verkfræði, fjármál og vöru, svo skýjaútgjöld verði sameiginleg, samfelld ábyrgð frekar en ársfjórðungsleg óvænt uppákoma.

## Málamiðlanir: kostir og gallar

| Val | Kostir | Gallar | Best passun |
|---|---|---|---|
| Kubernetes | Öflugt, flytjanlegt, gríðarlegt vistkerfi | Brött flækja. Rekstrarbyrði | Margar þjónustur í stærð |
| Stýrð gámaþjónusta | Minni rekstrarbyrði. Hraðari byrjun | Einhver binding. Minni stjórn | Teymi sem vilja einfaldleika |
| Einn sameiginlegur klasi | Skilvirk auðlindanotkun | Erfiðari einangrun. Sprengisvæði | Traustir innri leigjendur |
| Klasi á leigjanda | Sterk einangrun | Hærri kostnaður og yfirbygging | Vantreystandi eða regluverkað vinnuálag |
| Fjölskýjaflytjanleiki | Sveigjanleiki. Forðast bindingu | Lægsti-samnefnari þjónustur | Stefnumótandi áhættuminnkun |
| Djúpar stýrðar einsskýjaþjónustur | Hámarksframleiðni | Háð söluaðila | Hraðamiðuð teymi |

Yfirgripsmikla málamiðlunin er geta gegn flækju. Kubernetes og skýjabyggður arkitektúr skila teygjanleika, seiglu og hraða. En þau leggja verulega rekstrar- og hugræna byrði sem lítil teymi vanmeta reglulega. Á sama hátt skiptir það að elta fullan [fjölskýja](https://en.wikipedia.org/wiki/Multicloud) flytjanleika framleiðni fyrir valkosti. Rétta svarið veltur á stærð og áhættu. Stórar skipulagsheildir með mörg teymi og sterkar stjórnarháttaþarfir réttlæta yfirleitt fjárfestinguna. Smærri viðleitni er oft betur þjónað af stýrðum þjónustum sem fela flækjuna.

## Spurningar til að ræða með teyminu

1. **Undirritið þið myndir og staðfestið undirskriftir við útsetningu og blokkar mikilvægur veikleiki í raun smíðina?** Myndin er traustseining ykkar, svo aðfangakeðjan í kringum hana á skilið hörð hlið, ekki viðvaranir. Ákveddu hvort aðeins undirritaðar, staðfestar myndir geti keyrt, hvort skönnun blokki mikilvægar niðurstöður eða skrái bara og hver viðheldur valda myndasafninu af hertum grunnmyndum sem teymi smíða úr. Fyrir fyrirtækja- og opinbert vinnuálag er þetta oft reglufylgnikrafa og það er líka besta vörn þín gegn eitruðu ósjálfstæði sem nær framleiðslu. Komdu með núverandi stöðu: hvaða brot keyrandi mynda kemur úr hertu grunnmyndinni þinni, hve margar bera óbætta mikilvæga CVE og hvort óundirrituð mynd geti nú verið tímasett. Ef mikilvæg niðurstaða stöðvar ekki útsetningu er skanninn ykkar skraut.

2. **Hvernig koma auðlindabeiðnir, -takmörk og -kvótar í veg fyrir að eitt vinnuálag svelti nágranna sína, án þess að skilja dýra afkastagetu eftir aðgerðalausa?** Á sameiginlegum klasa getur vinnuálag án takmarka hrunið eða hægt á öllu í kringum sig og kvótar settir of rausnarlega sóa nýtingarávinningnum sem réttlætir vettvanginn. Ákveddu skynsamleg sjálfgefin gildi, hver stillir þau og hvernig þú grípur vinnuálag án nokkurra beiðna. Í stærð er þetta bæði áreiðanleika- og kostnaðarstýring, því stærðarstilling er þar sem mikið af FinOps-sparnaði býr. Komdu með gögn: núverandi klasanýtingu, hve oft vinnuálag er rekið út eða hægt á og hvaða nafnarými hafa enga kvóta. Markmiðið er þétt, örugg pökkun, svo líttu á vantandi takmörk sem galla sem vettvangurinn hafnar.

3. **Hvaða ástand má búa inni í gámi og hvert fer allt annað?** Skýjabyggð seigla veltur á einnota tilvikum sem vettvangurinn getur endurtímasett að vild og það heldur aðeins ef mikilvægt ástand býr í stýrðum gagnaþjónustum frekar en á staðbundnum diski gámsins. Ákveddu regluna skýrt, því ástand geymt í gámi fyrir slysni verður gagnatap við næstu endurtímasetningu. Fyrir teymi sem flytja eldri forrit er þetta oft erfiðasti hlutinn, þar sem arfleifðarþjónustur gera ráð fyrir stöðugu staðbundnu skráakerfi. Komdu með skrá: hvaða þjónustur skrifa staðbundið ástand, hverjar treysta á klístraðar lotur eða hnútasækni og hvað þyrfti til að færa hvert út. Þar til ástand er utanvið hefurðu gáma sem líta teygjanlega út en er í raun ekki hægt að flytja.

4. **Þegar mörg teymi deila klasa, er einangrunarlíkan ykkar vísvitandi valið sem mjúk eða hörð fjölleiga og passa stýringarnar því vali?** Nafnarými aðskilja traust innri teymi, en þau halda ekki vinnuálagi sem er virkt fjandsamlegt eða í hættu, og að meðhöndla mjúka leigu eins og hún væri hörð er öryggisatvik í bið. Ákveddu á vinnuálag hvort leigjendur þurfi bara sanngjarna skiptingu eða verði að vera gert ráð fyrir að þeir vantreysti hver öðrum, paraðu síðan stýringarnar: nafnarými, kvóta, netstefnur og RBAC fyrir mjúka tilvikið, aðskilda klasa eða sterkari sandkassa fyrir harða tilvikið. Fyrir stóra skipulagsheild knýr þessi ákvörðun kostnað beint, því klasi á leigjanda er langtum dýrari en sameiginleg nafnarými, svo þú vilt eyða einangrunarfjárhagsáætluninni aðeins þar sem ógnarlíkanið krefst. Komdu með leigjendaskrána: hvaða vinnuálög deila klasa í dag, hver meðhöndla regluverkaða eða ytri umferð og hvar netstefna er enn leyfa-allt sjálfgefið. Í fyrirtækja- og opinberu umhverfi er að blanda vantreystandi vinnuálagi undir mjúkri leigu nákvæmlega niðurstaðan sem úttektaraðili mun merkja, svo nefndu mörkin áður en þeir gera það.

5. **Hve mikið borgið þið fyrir fjölskýjaflytjanleika og munuð þið nokkurn tímann nota hann í raun?** Að staðla á gáma, Kubernetes og opin API heldur vinnuálagi flytjanlegu, en að hafna hverri stýrðri þjónustu til að varðveita þann kost skiptir raunverulegri, daglegri framleiðni fyrir flytjanleika sem skipulagsheildin kann aldrei að nýta. Ákveddu hvar flytjanleiki er ósvikin krafa, svo sem fullveldis- eða útgönguskylda sem þú hefur skrifað undir, á móti þar sem hann er hughreystingarteppi sem hægir á hverju teymi. Sjónarmiðið á móti er hraði: djúpar stýrðar þjónustur afhenda eiginleika hraðar og lægsti-samnefnari arkitektúr er viðvarandi skattur á hvert teymi. Komdu með sönnunargögnin: hvaða stýrðu þjónustum þið hafið forðast og hvað það kostaði í verkfræðitíma, hvort þið hafið nokkru sinni flutt vinnuálag milli veitenda og hverju samningar ykkar skylda ykkur í raun. Fyrir opinbera og regluverkaða notendur geta gagnabúsetu- og fullveldisskýjareglur gert flytjanleika óumsemjanlegan, svo hannaðu svo sömu skrár og leiðslur keyri á fullveldissvæði og í einkaafgirtu svæði, en vertu heiðarlegur um að þetta sé reglufylgnikostnaður frekar en ókeypis trygging.

6. **Getur hvert teymi séð hvað það eyðir og á einhver reikninginn áður en hann verður óvænt uppákoma?** Á teygjanlegum vettvangi er kostnaður bein afleiðing verkfræðiákvarðana, samt án kostnaðarskiptingarmerkja og sýnilegra mælaborða safnast útgjöld í sameiginlegan pott sem enginn finnur ábyrgð á fyrr en fjármál stigmagna. Ákveddu hvernig þú eignar kostnað teymum og þjónustum, hver rýnir hann og hvort verkfræðingar sjá kostnað við hlið afkastamælikvarða eða heyra bara um hann einu sinni á ársfjórðungi. Spennan er milli ábyrgðar og núnings: þrýstu kostnaði of fast og hver ákvörðun verður fjárhagsáætlunarsamningaviðræður, hunsaðu hann og aðgerðalaus, ofstór vinnuálög safnast hljóðlega. Komdu með tölurnar: núverandi útgjöld á teymi, hve mikil afkastageta er aðgerðalaus eða ofstór og hve fljótt stjórnlaust vinnuálag yrði tekið eftir. Fyrir fjárhagsáætlanir fyrirtækja og hins opinbera eru óeignuð skýjaútgjöld bæði stjórnarháttabrestur og raunveruleg fjárhagsáhætta, svo settu upp FinOps-venju sem setur verkfræði, fjármál og vöru í sama samtal frekar en að sætta eftir á.

## Sjónarhorn eftir geirum

**Sprotafyrirtæki.** Seilstu í stýrða gámaþjónustu frekar en sjálfhýstan Kubernetes-klasa: með tvær þjónustur og engan vettvangsverkfræðing eru stjórnlag truflun sem þú hefur ekki efni á. Pakkaðu litlar myndir úr lágmarksgrunni, festu útgáfur, bættu einni veikleikaskönnun við smíðina og ýttu öllu ástandi í stýrðan gagnagrunn svo tilvik haldist einnota. Slepptu nafnarýmum, rekstraraðilum og fjölskýjaflytjanleika þar til þú átt í raun þjónusturnar og fólkið til að réttlæta þau.

**Lítið fyrirtæki.** Án sérstaks vettvangssérfræðings og með þröngt fjárhagsáætlun skaltu halla þér fast að stýrðum þjónustum og láta veituna reka stýringuna sem þú þyrftir annars að manna. Líttu á gámagrunnatriði sem öryggisgólf þitt: lágmarksmyndir, útgáfufestingu og skönnun í leiðslunni gefa mestu verndina fyrir litla fyrirhöfn. Kjóstu að kaupa studdan vettvang fram yfir að smíða einn og haltu nægum flytjanleika, stöðluðum gámum og opnum API, svo þú sért ekki fastur ef verð eða skilmálar breytast.

**Stórfyrirtæki.** Verkefnið er vettvangsstjórnarhættir yfir mörg teymi: miðlægt vettvangsteymi sem útvegar hertar grunnmyndir, undirritunar- og skönnunarhlið, nafnarýmisleigu með kvótum, netstefnu og RBAC, auk kostnaðarskiptingarmerkja og FinOps-mælaborðs. Staðlaðu útsetningarsamninginn svo hundruð þjónusta starfi eins og stýrðu öryggi, fjölleigu og kostnaði miðlægt á meðan teymi sjálfsafgreiða útsetningu. Fjármagnaðu vettvangsteymið almennilega, því undirmannaður vettvangur verður flöskuhálsinn sem öll skipulagsheildin bíður eftir.

**Hið opinbera.** Fullveldi, gagnabúseta og opinber ábyrgð móta arkitektúrinn. Keyrðu vinnuálög á stöðluðum gámum og Kubernetes svo sömu leiðslur keyri á fullveldissvæði og í faggildu eigin afgirtu svæði og kóðaðu búsetu- og aðgangsmörk sem stefnu frekar en venju. Sæktu myndir í innra hert myndasafn, beittu harðri fjölleigu á viðkvæmustu gögnin og haltu flytjanleikanum sem gefur þér seiglu og samningsstöðu, því innkaupareglur banna oft bindingu við einn seljanda.

## Dæmi

**Sprotafyrirtæki.** Sex manna sprotafyrirtæki pakkar tveimur þjónustum sínum sem litlum gámamyndum smíðuðum úr lágmarksgrunni og keyrir þær á stýrðri gámaþjónustu frekar en sjálfhýstum Kubernetes-klasa, svo enginn þurfi að passa stjórnlag. Þau festa útgáfur grunnmynda og bæta veikleikaskönnun við smíðina, en sleppa viljandi þyngri stýringareiginleikum þar til þau eiga í raun fleiri en örfáar þjónustur. Ástand býr í stýrðum Postgres-gagnagrunni, sem heldur gámunum einnota og leyfir vettvangnum að endurræsa eða skala þá án gagnataps.

**Stórfyrirtæki.** Fjarskiptafyrirtæki rekur nokkur hundruð [örþjónustur](https://en.wikipedia.org/wiki/Microservices) á sameiginlegum Kubernetes-klösum. Vettvangsteymi útvegar hertar grunnmyndir, framfylgir myndaundirritun og veikleikahliðum og einangrar viðskiptaeiningar í nafnarými með kvótum, netstefnum og RBAC. Kostnaðarskiptingarmerki og FinOps-mælaborð eigna útgjöld hverri vörulínu og sjálfskölun stillir afkastagetu að eftirspurn. Vöruteymi setja upp tugi sinnum á dag á samræmdan vettvang án þess að stýra þjónum. Fyrirtækið heldur miðlægri stjórn á öryggi og kostnaði.

**Hið opinbera.** Landsbundin heilbrigðisþjónusta verður að halda borgaragögnum innan landamæra og undir landslegri lagastjórn. Hún rekur vinnuálög sín á fullveldisskýjasvæði með stöðluðum gámum og Kubernetes, svo sömu leiðslur og skrár keyra einnig í faggildu eigin umhverfi fyrir viðkvæmustu gögnin. Gagnabúsetu- og aðgangsmörk eru kóðuð sem stefna, myndir eru sóttar í innra hert myndasafn og hörð fjölleiga einangrar viðkvæm vinnuálög. Flytjanleiki milli fullveldissvæðisins og einkaafgirta svæðisins gefur þjónustunni seiglu og samningsstöðu án þess að fórna reglufylgni.

## Viðskiptarök: hvatar, ávöxtun fjárfestingar og heildarkostnaður

Ávöxtun gáma og stýringar kemur af hærri auðlindanýtingu, hraðari og áreiðanlegri útsetningum, teygjanlegri skölun sem mætir útgjöldum við eftirspurn og bættri seiglu gegnum sjálfsviðgerð. Að staðla á sameiginlegan vettvang dregur úr tvítekinni fyrirhöfn yfir teymi og flýtir innleiðingu, því hver þjónusta fylgir sama útsetningar- og rekstrarsamningi.

Heildareignarkostnaðargreiningin verður að vera heiðarleg um rekstrarbyrðina. Upptökukostnaður felur í sér vettvangsverkfræðinga, þjálfun, öryggisverkfæri fyrir myndir og klasa og viðvarandi fyrirhöfn við að reka vettvanginn sjálfan. Kostnaður þess að taka ekki upp felur í sér ósamræmda sérsmíðaða útsetningu yfir teymi, lélega nýtingu dýrra innviða, brothætta handvirka skölun og erfiðleika við að mæta seiglu- og fullveldiskröfum. Fyrir forystu hvílir málið á stærð. Undir tilteknum fjölda þjónusta borgar flækjan sig kannski ekki og stýrð þjónusta er viturlegri. En í fyrirtækja- og opinberri stærð er stýrður skýjabyggður vettvangur yfirleitt hagkvæmasti og seigasti grunnurinn, að því gefnu að þú fjármagnir vettvangsteymið til að reka hann almennilega.

## Andmynstur og gildrur

- **Feitar, óskannaðar myndir.** Uppþembdar myndir smíðaðar úr ótraustum grunnum bera óþarfa veikleika og hægja á öllu.
- **Kubernetes fyrir allt.** Að taka upp flókinn stýrivettvang fyrir örfáar einfaldar þjónustur kaupir flækju án ávinnings.
- **Að hunsa auðlindatakmörk.** Án beiðna og takmarka getur eitt vinnuálag sveltt eða hrunið nágranna sína.
- **Mjúk leiga fyrir fjandsamlegt vinnuálag.** Að treysta á nafnarými ein til að einangra vantreystandi leigjendur er öryggisatvik í bið.
- **Ástandsríkir gámar fyrir slysni.** Að geyma mikilvægt ástand inni í einnota gámum leiðir til gagnataps við endurtímasetningu.
- **Kostnaðarblinda.** Að líta á skýjaútgjöld sem fastan kostnað frekar en verkfræðiafurð leiðir til stjórnlausra reikninga.
- **Flytjanleikaleikhús.** Að hafna öllum stýrðum þjónustum til að varðveita flytjanleika sem skipulagsheildin mun aldrei nota í raun.

## Þroskalíkan

**Stig 1: Upphaf.** Gámar eru notaðir ad hoc, ef yfirleitt. Myndir eru handsmíðaðar og óskannaðar, útsetning er handvirk og viðbragðsdrifin og enginn sameiginlegur vettvangur, kostnaðarsýnileiki eða einangrunarlíkan er til.

**Stig 2: Þróun.** Teymi gámavæða forrit og taka upp stýri, en vinnubrögð eru ólík milli hópa. Myndaskönnun, auðlindatakmörk og undirritun eru ósamræmd og kostnaði og fjölleigu er ekki kerfisbundið stýrt.

**Stig 3: Stöðlun.** Staðlaður vettvangur er skjalfestur og framfylgdur um skipulagsheildina: hertar grunnmyndir, undirritunar- og skönnunarhlið, nafnarýmisbundin leiga með kvótum og netstefnu, RBAC og kostnaðarskipting. Skýjabyggð og tólf-þátta mynstur eru væntanlegt norm frekar en staðbundið val.

**Stig 4: Stjórnun.** Vettvangurinn er mældur og stýrður gegn grunnlínum. Þú rekur klasanýtingu, hlutfall keyrandi mynda smíðaðra úr hertu grunnmyndinni, óbætta mikilvæga veikleika, útsetningartíðni og bilunarhlutfall breytinga, brottrekstrar- og hægingarhlutföll og kostnað á teymi og þjónustu gegn fjárhagsáætlun. Hlið eru framfylgd á þeim sönnunargögnum: vantandi auðlindatakmörkum og óundirrituðum myndum er hafnað sjálfvirkt og frávik frá staðlinum kallar fram aðgerð frekar en viðvörun.

**Stig 5: Samhæfing.** Vettvangurinn er sjálfsafgreiðslu og sjálfsviðgerðar, samþættur um skipulagsheildina og aðlögunarhæfur. FinOps stillir stærð og endurheimtir afkastagetu samfellt, flytjanlegur arkitektúr styður blendings- og fullveldiskröfur og vettvangurinn batnar stöðugt af mældri notkun, leggur niður og skiptir út íhlutum þegar vinnuálög, kostnaður og áhættumynd breytast.

## Hugmyndir til umræðu

- Við hvaða stærð hættir upptaka Kubernetes að vera flækja sjálfs síns vegna og fer að borga sig?
- Hvar er rétta línan milli mjúkrar og harðrar fjölleigu fyrir vinnuálög ykkar?
- Hve mikið ættuð þið að fjárfesta í fjölskýjaflytjanleika á móti framleiðni djúpra stýrðra þjónusta?
- Hvernig gefið þið verkfræðingum raunverulega kostnaðarábyrgð án þess að breyta hverri ákvörðun í fjárhagsáætlunarsamningaviðræður?
- Hvert er stjórnarhættalíkan ykkar fyrir grunnmyndir og hver viðheldur hertu myndasafninu?
- Hvernig móta fullveldis- og gagnabúsetukröfur vettvangsarkitektúr ykkar?

## Helstu atriði

- Gámar staðla pökkun og keyrslu. Stýring staðlar rekstur í stærð.
- Myndahreinlæti, það er lágmarks, festar, skannaðar, undirritaðar myndir, er grundvallaröryggi.
- Notaðu innbyggð Kubernetes-mynstur og rekstraraðila frekar en að smíða sérsmíðaða stýringu.
- Veldu fjölleigulíkan af ásetningi út frá því hve mikið vinnuálögin treysta hvert öðru.
- Fylgdu tólf-þátta og framlengdu það fyrir dreifðra kerfa veruleika eins og hlutabilun og vöktun.
- Líttu á kostnað sem verkfræðiafurð og stýrðu honum samfellt gegnum FinOps.

## Heimildir og frekari lestur

- Adam Wiggins, *The Twelve-Factor App* (methodology).
- Brendan Burns, Joe Beda, and Kelsey Hightower, *Kubernetes Up & Running*.
- Bilgin Ibryam and Roland Huß, *Kubernetes Patterns*.
- Cornelia Davis, *Cloud Native Patterns*.
- J.R. Storment and Mike Fuller, *Cloud FinOps*.
- Liz Rice, *Container Security*.
- Cloud Native Computing Foundation (CNCF), cloud-native definition and landscape.
