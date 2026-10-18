# 6.8 Tathmini na majaribio ya AI

## Muhtasari na msukumo

Kujaribu programu ya kawaida kunategemea dhana ya kufariji: ukipewa ingizo lilelile, programu inarudisha matokeo yaleyale, na unaweza kuthibitisha hasa matokeo yanapaswa kuwa nini. Akili bandia huvunja dhana hiyo. Mfano unaweza kujibu swali lilelile kwa njia mbili tofauti, zote zikikubalika. Unaweza kupimwa kwenye wigo kutoka makosa hadi ustadi badala ya kupita au kushindwa. Na mara nyingi hakuna jibu moja sahihi la kuthibitisha. Kwa hiyo nidhamu ya tathmini, kupima mfano unavyotenda kuvuka kesi nyingi za uwakilishi badala ya kukagua matokeo moja dhidi ya thamani moja inayotarajiwa, inakuwa uti wa mgongo wa mfumo wowote wa AI unaoaminika. Timu zinaposafirisha vipengele vya AI vinavyowaaibisha, chanzo karibu daima ni kwamba hawakuwa na njia makini ya kupima ubora kabla ya toleo.

Kwa timu kubwa, tathmini ndiyo inayofanya mabadiliko kuwa salama. Mtabadilisha mifano, kuandika upya maagizo, kurekebisha urejeshaji, na kuongeza zana, na kila badiliko linaweza kudhoofisha kimyakimya tabia mliyodhani ni imara. Bila njia inayojirudia ya kupima ubora, kila badiliko ni kamari na kila regression inagunduliwa na mtumiaji. Sura hii ni mwenzi wa kupima wa sura za kujenga: AI ya kuzalisha na programu za LLM (sura ya 6.3), mawakala wa AI na mifumo ya kiwakala (sura ya 6.7), na uhandisi wa kujifunza kwa mashine na MLOps (sura ya 6.2). Inapanua mkakati wenu wa jumla wa majaribio (sura ya 2.4) hadi ulimwengu wa uwezekano.

Mashirika makubwa na serikali huongeza dau. Shirika linaloendesha vipengele kadhaa vya AI linahitaji jukwaa la pamoja la tathmini ili kila timu isibuni upya upimaji kuanzia sifuri. Wakala wa serikali unahitaji tathmini iliyoandikwa na inayokaguliwa, kwa sababu "tulijaribu" lazima iwe "hapa ni ushahidi, seti ya data, kipimo, na idhini." Tathmini ndipo AI ya kuwajibika na ya kuaminika (sura ya 6.5) inapoacha kuwa kauli ya thamani na kuwa kitu unachoweza kumwonyesha mdhibiti.

## Kanuni kuu

- Chukulia tathmini kama bidhaa ya daraja la kwanza, si wazo la baadaye linalobanwa kabla ya uzinduzi.
- Pima kwa data ya uwakilishi inayoakisi matumizi halisi, si mifano ya kuchezea inayobembeleza mfano.
- Changanya tathmini ya nje ya mtandao kwa marudio ya haraka na ya mtandaoni kwa ukweli wa msingi.
- Tumia busara ya binadamu kama nanga yako, na urekebishe kila mpimaji wa kiotomatiki dhidi yake.
- Linda seti zako za tathmini dhidi ya uchafuzi, la sivyo namba zako zitakudanganya.
- Unganisha tathmini kwenye ujumuishaji endelevu kama malango, ili ubora usiporomoke kimyakimya.
- Endelea kupima kwenye uzalishaji, kwa sababu ubora huteleza hata msimbo wako usipobadilika.

## Mapendekezo

### Pokea uendelezaji unaoendeshwa na tathmini

Kabla hujarekebisha agizo au kuchagua mfano, andika tathmini. Hii inaakisi uendelezaji unaoendeshwa na majaribio: unafafanua "nzuri" inamaanisha nini kwa maneno yanayopimika, kisha unajenga kuelekea hapo. Tathmini hapa inamaanisha seti ya data ya ingizo zilizooanishwa na njia ya kupima inayorudisha namba au daraja kwa kila matokeo. Anza kidogo. Kesi ishirini zilizochaguliwa kwa makini zinazoakisi nia halisi ya mtumiaji zinashinda elfu moja za nasibu. Kuza seti unavyojifunza mahali mfumo unaposhindwa, ukirudisha kila kushindwa kwa uzalishaji kama kesi ya kudumu ili kosa lilelile lisirudi bila kuonekana.

Uendelezaji unaoendeshwa na tathmini hubadilisha tabia ya timu. Ufafanuzi wa nzuri unapoandikwa na kuweza kuendeshwa, mabishano kuhusu kama badiliko lilisaidia yanakuwa yanayokaguliwa badala ya suala la ladha. Fanya seti ya tathmini kuwa mabaki yaliyopitiwa kwenye udhibiti wa matoleo, kando ya maagizo na msimbo inavyopima.

### Tenganisha tathmini ya nje ya mtandao na ya mtandaoni, na utumie zote

Tathmini ya nje ya mtandao hupitisha seti ya data iliyowekwa kupitia mfumo wako katika mazingira yanayodhibitiwa, ya haraka, nafuu, na yanayojirudia, ili ulinganishe matoleo kabla ya kitu chochote kusafirishwa. Tathmini ya mtandaoni hupima mfumo hai na watumiaji halisi kupitia vipimo kama ukamilishaji wa kazi, kiwango cha kupandisha ngazi, maoni ya kidole-juu na kidole-chini, na matokeo ya biashara ya chini ya mkondo. Ya nje ya mtandao inakuambia kama badiliko linaelekea kuwa salama; ya mtandaoni inakuambia kama lilifanya kazi kweli. Unahitaji zote mbili, kwa sababu seti za nje ya mtandao hazinasi uhalisia kikamilifu na ishara za mtandaoni zinafika kuchelewa kuwa ulinzi wako pekee.

Unganisha hizi mbili kuwa mzunguko. Vipimo vya mtandaoni vinaposhuka au watumiaji wanapoweka alama jibu baya, nasa kesi hiyo, iwekee lebo, na uiingize kwenye seti ya nje ya mtandao. Pitisha majaribio kupitia ulinganisho ule ule uliodhibitiwa unaotumia kwa badiliko lolote la bidhaa, ambalo ni eneo la uchanganuzi wa bidhaa na majaribio (sura ya 7.4). Jaribio la A/B linaloonyesha mfano mpya unaongeza mafanikio ya kazi lina thamani zaidi ya alama yoyote ya nje ya mtandao, hata hivyo alama ya nje ya mtandao ndiyo iliyokuwezesha kuthubutu kuendesha jaribio.

### Jenga seti za tathmini za uwakilishi na ulinde dhidi ya uchafuzi

Tathmini yako ni ya uaminifu kadiri data yake ilivyo. Jenga seti za dhahabu, makusanyo yaliyochaguliwa ya ingizo zenye matokeo yanayotarajiwa yaliyothibitishwa au vigezo vya alama, zinazoakisi usambazaji halisi wa kile watumiaji wanauliza: kesi za kawaida, kesi adimu-lakini-muhimu, kesi za uadui, na zile ambazo mfumo wako unazikosea sasa. Zipange kwa tabaka ili uweze kusoma ubora kwa kila sehemu badala ya kuficha kategoria inayoshindwa ndani ya wastani mzuri. Waache wataalamu wa eneo wathibitishe majibu yanayotarajiwa, kwa sababu seti ya dhahabu iliyojengwa juu ya majibu mabaya ni mbaya kuliko hakuna.

Kisha linda data hiyo dhidi ya uchafuzi. Uchafuzi wa seti ya majaribio hutokea mifano yako ya tathmini inapovuja kwenye data ya mafunzo ya mfano au kwenye agizo lenyewe, kwa hiyo mfano unaonekana kufanya vizuri kwa sababu kwa kweli umeshaona majibu. Ndiyo maana mfano unaweza kupata alama za kuvutia kwenye kigezo cha umma na kujikwaa kwenye trafiki yenu halisi. Weka sehemu ya data yako ya tathmini ya faragha na usiitume kwa mtu wa tatu usiyemwamini. Isasishe kwa muda. Angalia uvujaji wa hila zaidi ambapo wasanidi hurekebisha maagizo kwa mkono dhidi ya seti ya tathmini hadi alama haina maana, aina ya kufaa kupita kiasi kwenye jaribio badala ya uboreshaji halisi. Weka kando seti mpya unayoitazama mara chache tu.

### Chagua vipimo vinavyofaa kazi

Linganisha kipimo chako na umbo la matokeo. Kwa uainishaji na uchimbaji, ambapo kuna lebo sahihi, vipimo vya kawaida vinatumika: [usahihi na ukumbukaji](https://en.wikipedia.org/wiki/Precision_and_recall) (kati ya vitu ulivyoweka alama, vingapi vilikuwa sahihi, na kati ya vitu sahihi, vingapi ulivipata), [alama ya F](https://en.wikipedia.org/wiki/F-score) inayovisawazisha, na usahihi wa mlingano kamili. Kwa chochote ambapo uwezekano wenye imani unajalisha, pima [urekebishaji](https://en.wikipedia.org/wiki/Calibration_(statistics)), kama imani iliyotajwa ya asilimia 80 ni sahihi takriban asilimia 80 ya wakati, kwa sababu mfano uliorekebishwa vizuri unaojua unapokuwa na shaka ni salama zaidi sana kuliko wenye kujiamini kupita kiasi.

Matokeo ya kuzalisha ni magumu zaidi. Vipimo vinavyotegemea rejeo kama [BLEU](https://en.wikipedia.org/wiki/BLEU) na ROUGE, vilivyojengwa awali kwa tafsiri ya mashine na kufupisha, hulinganisha maandishi yaliyozalishwa na maandishi ya rejeo kwa kuhesabu maneno na vifungu vinavyoingiliana. Ni nafuu na vinajirudia, na ni vibadala dhaifu vya ubora: vinatuza mwingiliano wa juujuu na kuadhibu jibu sahihi lililoandikwa tofauti na rejeo. Vitumie kama ishara ghafi za regression, si ufafanuzi wako wa nzuri. Kwa kazi za wazi, alama za kigezo hufanya kazi vizuri zaidi: fafanua vigezo wazi (je, ina msingi, kamili, salama, na imeumbwa ipasavyo) na upime kila kimoja. Vigezo hufanya ubora wa kiubinafsi usomeke na uweze kupitiwa.

### Tumia LLM-kama-hakimu, lakini urekebishe dhidi ya binadamu

Kupima matokeo ya kuzalisha kwa mkono hakupanuki, kwa hiyo timu zinazidi kutumia [mfano mkubwa wa lugha](https://en.wikipedia.org/wiki/Large_language_model) imara kama hakimu wa kiotomatiki, ukiuelekeza kwa ingizo, matokeo, na kigezo, na kuuomba upime. Mbinu hii ya LLM-kama-hakimu ni ya haraka na yenye uwezo wa kushangaza, na inabeba upendeleo halisi ambao lazima uusimamie. Mahakimu huelekea kupendelea majibu marefu zaidi, kupendelea chaguo la kwanza linaloonyeshwa katika ulinganisho wa jozi (upendeleo wa nafasi), kutuza mtindo wao wa uandishi, na wanaweza kuyumbishwa na hoja fasaha lakini isiyo sahihi. Bila kudhibitiwa, hakimu mwenye upendeleo anakupa namba zenye imani, sahihi, zisizo sahihi.

Rekebisha hakimu dhidi ya lebo za binadamu. Waache watu wapime sampuli, kisha angalia hakimu wa mfano anakubaliana nao kiasi gani, na uendelee kurekebisha agizo la hakimu hadi mkubaliano uwe wa juu vya kutosha kuaminika. Punguza upendeleo unaojulikana kwa makusudi: nasibisha mpangilio wa chaguo, dhibiti urefu, na uombe alama iliyofungwa kwa kigezo yenye sababu badala ya namba tupu. Chukulia hakimu kama chombo cha kupimia kinachohitaji kurekebishwa mara kwa mara, si nabii asiyebadilika. Unapojenga hakimu, chagua mfano wenye uwezo zaidi unaopatikana kwa chaguo-msingi, kwa kuwa hakimu dhaifu ni rula dhaifu.

### Weka binadamu kwenye mzunguko kwa ukweli wa msingi

Tathmini ya binadamu inabaki nanga ambayo kila kipimo cha kiotomatiki kinapimwa dhidi yake, kwa hiyo wekeza kuifanya vizuri. Andika miongozo wazi ya uwekaji alama, funza wawekaji alama wako, na upime mkubaliano kati ya wawekaji alama, kiwango ambacho wapitiaji huru wanapa kesi ileile daraja lilelile. Mkubaliano mdogo kwa kawaida unamaanisha kigezo chako kina utata, si kwamba wapitiaji wako wazembe, kwa hiyo rekebisha kigezo. Kwa maeneo ya dau kubwa, tumia wataalamu waliohitimu, si wafanyakazi wa umati wasio na muktadha wa kuhukumu jibu la kisheria au kimatibabu.

### Fanya red-team kwa usalama na uimara wa uadui

Seti za kawaida za tathmini hupima kama mfumo unafanya jambo sahihi kwenye ingizo za busara. [Red teaming](https://en.wikipedia.org/wiki/Red_team), kushambulia mfumo wako mwenyewe kwa makusudi kupata mahali unapotenda vibaya, hupima kinachotokea chini ya shinikizo. Chunguza sindano ya maagizo, kuvunjwa kizuizi, maudhui yasiyo salama, uvujaji wa faragha, na matokeo yenye upendeleo. Ifanye mfululizo unaojirudia, si zoezi la mara moja: geuza kila shambulio lililofanikiwa kuwa kesi ya kudumu ya regression ili udhaifu uliorekebishwa ubaki umerekebishwa. Kazi hii inaunganika moja kwa moja na AI ya kuwajibika na ya kuaminika (sura ya 6.5), na katika mazingira yanayodhibitiwa mara nyingi ni ushahidi unaotimiza mapitio ya usalama.

### Tathmini mawakala kwa mafanikio ya kazi ya mwanzo hadi mwisho

Mawakala wanaopanga na kutenda kwa hatua nyingi hawawezi kuhukumiwa matokeo moja kwa moja. Kinachojalisha ni kama kazi nzima ilifanikiwa: je, wakala aliweka mkutano, alitatua tiketi, au alikamilisha mtiririko ipasavyo na kwa usalama. Jenga tathmini za kiwango cha kazi kwenye mazingira ya sandbox ambapo wakala anaweza kutenda dhidi ya vifaa vya uhalisia lakini salama, na upime matokeo ya mwisho pamoja na njia, yaani mfuatano wa hatua na miito ya zana alizochukua kufika huko. Jibu sahihi lililofikiwa kwa njia hatari au ya upotevu bado ni tatizo. Hili ni muhimu kwa mawakala wa AI na mifumo ya kiwakala (sura ya 6.7), ambapo kitendo kimoja kisicho sahihi kinaweza kuwa na matokeo halisi.

### Unganisha tathmini kwenye CI na ufuatilie uzalishaji

Fanya tathmini iwe ya kiotomatiki. Endesha mfululizo wako wa nje ya mtandao kwenye [ujumuishaji endelevu](https://en.wikipedia.org/wiki/Continuous_integration) (CI) kwa kila badiliko la agizo, mfano, au urejeshaji, na uweke lango la muunganisho juu yake kama unavyoweka lango la majaribio ya kitengo, mazoea yenye mizizi katika mkakati wenu mpana wa majaribio (sura ya 2.4). Kwa kuwa alama zina kelele, weka lango kwa vizingiti na mielekeo badala ya kudai mbio kamilifu, na ushindwe ujenzi kipimo muhimu kinaposhuka chini ya sakafu yake au kurudi nyuma kupita ukingo uliowekwa. Kisha endelea kutazama kwenye uzalishaji: fuatilia ishara za ubora, usambazaji wa matokeo, na kuteleza kwa ingizo ili unase kuzorota polepole ambako majaribio ya nje ya mtandao hukosa, jambo linalounganika na mazoea ya uonekanaji ya uhandisi wa kujifunza kwa mashine na MLOps (sura ya 6.2). Mfano uliokuwa sahihi wakati wa uzinduzi unaweza kuoza dunia inayoielezea inapobadilika chini yake.

## Mabadilishano: faida na hasara

| Mbinu ya tathmini | Faida | Hasara | Bora wakati |
|---|---|---|---|
| Tathmini ya binadamu | Uaminifu wa juu zaidi, inanasa nuances | Polepole, ghali, ngumu kupanua | Ukweli wa msingi, dau kubwa, kurekebisha mahakimu |
| LLM-kama-hakimu | Haraka, nafuu, inapanuka hadi seti kubwa | Ina upendeleo, inahitaji kurekebishwa | Mbio za mara kwa mara za nje ya mtandao kwa matokeo ya kuzalisha |
| Vipimo vya rejeo (BLEU, ROUGE) | Nafuu, vya kuamuliwa, vinajirudia | Kibadala dhaifu cha ubora halisi | Ishara ghafi za regression, si hukumu za mwisho |
| Vipimo vya kawaida (usahihi, ukumbukaji, alama ya F) | Vya lengo, vinaeleweka vizuri | Vinafaa kazi zenye lebo sahihi tu | Uainishaji, uchimbaji, urejeshaji |
| Vigezo vya umma | Vinalinganishika kuvuka mifano, hakuna usanidi | Uchafuzi, ufaao hafifu kwa kazi yako | Kuchagua mifano ya awali, si malango ya toleo |
| Tathmini ya mtandaoni (A/B, maoni) | Inaakisi watumiaji na matokeo halisi | Polepole, inafika baada ya mfiduo | Kuthibitisha badiliko lilisaidia kweli |

Mvutano wa msingi ni kasi dhidi ya uaminifu. Tathmini ya binadamu ndiyo inayoaminika zaidi na isiyopanuka kidogo zaidi; upimaji wa kiotomatiki ni kinyume. Suluhisho ni kuweka tabaka: tumia njia za haraka, nafuu kwa marudio ya mara kwa mara, zifunge kwenye busara ya binadamu kupitia urekebishaji wa mara kwa mara, na uhifadhi mapitio kamili ya binadamu kwa maamuzi ya dau kubwa zaidi na kuangalia kwamba vipimo vyenu vya bei nafuu bado vinafuata uhalisia. Mvutano wa pili ni urahisi wa nje ya mtandao dhidi ya ukweli wa mtandaoni. Seti za nje ya mtandao hukuruhusu kusonga haraka lakini hazifanani kikamilifu na uzalishaji, kwa hiyo chukulia alama imara ya nje ya mtandao kama ruhusa ya kuendesha jaribio makini la mtandaoni, si uthibitisho kwamba umekamilika.

## Maswali ya kujadili na timu yako

1. **Kiwango chetu cha "kizuri vya kutosha" ni kipi, na nani anamiliki seti ya tathmini inayokifafanua?** Kila kipengele cha AI kina kizingiti cha ubora kisichotamkwa, na kinapobaki kisichotamkwa, kila mhandisi anaweka chake kwa hisia na mabishano yanatatuliwa na yeyote mwenye cheo cha juu chumbani. Kuandika kiwango kama seti ya tathmini inayoendeshwa yenye alama lengwa kwa kila sehemu hugeuza mabishano hayo kuwa maswali yanayopimika. Leta ufafanuzi wenu wa sasa wa mafanikio, data nyuma yake, na maelezo ya uaminifu ya nani anaidumisha kweli, kwa sababu seti ya tathmini isiyo na mmiliki huoza haraka kama msimbo wowote usiotunzwa. Amua kama kiwango kinatofautiana kwa ngazi ya hatari, kwa kuwa jibu la kisheria linalomkabili umma linapaswa kufikia kiwango cha juu zaidi kuliko msaada wa mawazo wa ndani. Jibu linapaswa kukuambia kama yeyote anaweza kusafirisha badiliko la AI sasa bila kipimo chochote kati yake na watumiaji.

2. **Tunajuaje namba zetu za tathmini ni za uaminifu na si zilizochafuliwa au kufaa kupita kiasi?** Alama ni ya manufaa tu ikitabiri ubora wa ulimwengu halisi, na kuna njia nyingi kwa hiyo kuacha kufanya hivyo: data ya kigezo ikivuja kwenye mafunzo, wasanidi wakirekebisha maagizo dhidi ya seti ya majaribio hadi namba haina maana, au seti ya dhahabu iliyojengwa kwa majibu ambayo hayakuthibitishwa kamwe. Leta ushahidi wa data yenu ya tathmini ilitoka wapi, kiasi gani kinawekwa faragha, na inasasishwa mara ngapi. Jadili kama mnaweka seti mpya ya kando mnayoitazama mara chache, ili mwe na angalau namba moja ambayo hakuna aliyeiboresha dhidi yake. Kama huwezi kueleza kwa nini alama zako zingeshikilia kwenye data ambayo mfano haujaathiriwa nayo kamwe, unapima kioo chako mwenyewe.

3. **Binadamu wanabaki kwenye mzunguko wapi, na tunaweka vipi mahakimu wetu wa kiotomatiki wakiwa wamerekebishwa kwao?** LLM-kama-hakimu na vipimo vya rejeo vinakuruhusu kupima kwa ukubwa, na vinaachana na busara ya binadamu kwa njia zisizoonekana usipokagua. Leta kiwango chenu cha sasa cha mkubaliano kati ya upimaji wa kiotomatiki na mapitio ya binadamu, mlipimwa lini mara ya mwisho, na upendeleo gani (urefu, nafasi, mtindo) mmeujaribu. Amua maamuzi yapi yanahitaji mpimaji wa binadamu bila kujali gharama, kwa kawaida ya dau kubwa zaidi na yale yanayotumika kurekebisha hakimu wa kiotomatiki. Zungumza kuhusu ubora wa uwekaji alama pia, kwa sababu hakimu aliyerekebishwa dhidi ya lebo za binadamu zisizo thabiti hurithi kutokuwa na uthabiti huo. Jibu linapaswa kuzalisha ratiba ya kurekebisha, si baraka ya mara moja.

4. **Mabadiliko yapi ya AI yamewekewa lango la tathmini leo, na yapi bado yanawafikia watumiaji kwa imani ya mtu tu?** Lango linaloendesha kwenye mabadiliko mengine lakini si mengine hukupa udanganyifu wa usalama huku likiacha regression halisi zipenye kwenye njia isiyo na lango: marekebisho ya kimyakimya ya agizo, kurekebisha urejeshaji, kuinua toleo la mfano ambalo hakuna aliyedhani ni badiliko. Kwa timu kubwa, hatari hukua na idadi ya watu wanaoweza kugusa agizo, kwa sababu kila njia isiyo na lango ni njia ya kusafirisha regression ambayo hakuna seti ya data iliyowahi kuiona. Leta orodha ya aina za mabadiliko zinazochochea mfululizo wa nje ya mtandao kwenye ujumuishaji endelevu, zile zisizochochea, na matukio ya hivi karibuni yaliyofuatiliwa hadi badiliko lisilo na lango. Amua kizingiti na mwelekeo ambao lango linatekeleza, kwa kuwa alama yenye kelele inadai sakafu na ukingo wa regression badala ya mbio kamilifu. Katika mazingira ya mashirika makubwa na serikali, funga lango na rekodi ya toleo yenyewe, ili ushahidi kwamba badiliko lilipimwa uwe sehemu ya nyayo za ukaguzi na si picha ya skrini ambayo mtu aliipiga mara moja.

5. **Tunatumia kiasi gani kwenye tathmini, na je, matumizi hayo yanalingana na hatari ya kila kipengele?** Tathmini si bure: kazi ya uwekaji alama, kokotoo ambalo mahakimu wa kiotomatiki wanachoma kwa kila mbio, na kazi ya kudumu ya kuweka seti za dhahabu zikiwa za uwakilishi vyote vinagharimu fedha halisi, na timu isiyotaja gharama hizi kwa kawaida ama inawekeza kidogo kwa kipengele cha dau kubwa au inapaka dhahabu kitu cha kutupwa. Mvuto unaoshindana ni kati ya uaminifu na bajeti, kwa sababu njia inayoaminika zaidi, mapitio ya mtaalamu wa binadamu, pia ndiyo isiyopanuka kidogo zaidi, kwa hiyo huwezi kuimudu kila mahali na lazima uamue inapostahili bei yake. Leta gharama ya sasa kwa kila mbio ya tathmini, saa za uwekaji alama kwa kila kipengele, na ngazi ya hatari ya uaminifu kwa kila mfumo ili chumba kione fedha zinaenda wapi dhidi ya hatari inapoishi. Kwa shirika, hii ndiyo hoja imara zaidi ya jukwaa la pamoja la tathmini linalogawanya uwekaji alama na kokotoo kuvuka timu nyingi; kwa wakala wa serikali, ngazi ya hatari inapaswa kuoanisha moja kwa moja na kina cha ushahidi ambacho chombo cha usimamizi kitadai baadaye.

6. **Mfano bora unapofika, tunaweza kuthibitisha kwa kasi gani kama unasaidia, na nani anaruhusiwa kufanya kubadili?** Thamani ya mfululizo wa tathmini inatambuliwa kwa makali zaidi siku mfano imara zaidi unapotoka, kwa sababu timu inayoweza kuendesha seti zake za dhahabu na mfululizo wa red-team dhidi ya mfano mpya ndani ya alasiri inaweza kupokea maboresho ambayo timu inayopima kwa mkono itayakosa kwa miezi. Mvutano ni kati ya kasi na tahadhari: mnataka kusonga siku mfano bora unapoonekana, na hamwezi kuruhusu kubadili kudhoofishe kimyakimya kategoria ya majibu ambayo alama yenu ya wastani inaificha. Leta muda unaochukua sasa kuendesha ulinganisho kamili wa nje ya mtandao dhidi ya mtoa huduma mpya, kama seti zenu za tathmini zinahamishika kuvuka mifano, na sehemu ambapo regression ingejalisha zaidi. Katika mazingira yanayodhibitiwa na ya umma, taja nani ana mamlaka ya kuidhinisha badiliko la mfano na ushahidi ulioandikwa gani wanaohitaji, kwa sababu kubadilisha mfano nyuma ya uamuzi unaomkabili raia bila nyaraka ni badiliko hasa ambalo mkaguzi atakuomba kulihalalisha.

## Mtazamo wa sekta

**Kampuni changa.** Jenga tathmini ndogo zaidi ya uaminifu unayoweza na uiache ikue na bidhaa. Lahajedwali ya kesi ishirini hadi arobaini halisi, kila moja ikiwa na jibu linalotarajiwa lililothibitishwa, inayoendeshwa na hati kabla ya kila muunganisho, inashinda kigezo chochote cha umma kwa eneo lako na inagharimu karibu hakuna. Ruka jukwaa la pamoja na LLM-kama-hakimu hadi kupima kwa mkono kuumize kweli, lakini rudisha kila kushindwa kulikoripotiwa na mtumiaji kwenye seti tangu siku ya kwanza, kwa sababu tabia hiyo ndiyo inayozuia aibu ileile mara mbili.

**Biashara ndogo.** Huenda huna mtaalamu wa tathmini na unanunua AI yako ikiwa imepachikwa kwenye zana, kwa hiyo kazi yako ni kudai ushahidi badala ya kuujenga. Muulize kila muuzaji alipimaje ubora, kama wanajaribu kwenye data inayofanana na yako, na ungegunduaje regression baada ya sasisho usilolichagua. Weka seti ndogo ya faragha ya kesi zako halisi kukagua zana mwenyewe, kwa kuwa jibu la kiotomatiki lisilo sahihi linalomfikia mteja linakugharimu zaidi sana kuliko dakika ambazo ukaguzi huo unachukua.

**Biashara kubwa.** Zawadi ni jukwaa la pamoja la tathmini ili timu kumi na mbili zisibuni upya upimaji kila moja: hifadhi ya pamoja ya seti za dhahabu, mfululizo wa nje ya mtandao ulioweka lango kwenye ujumuishaji endelevu, maagizo ya mahakimu wa LLM yaliyosajiliwa na alama zao za urekebishaji, na vipimo vya mtandaoni kwa kila kipengele. Weka utawala juu yake na ngazi za hatari zinazoweka kiwango kinachohitajika na idhini kabla ya toleo, ili kipengele cha dau kubwa kipite lango la juu kuliko msaada wa ndani. Jukwaa hugawanya uwekaji alama na kokotoo kuvuka timu, ndiyo sababu kuu ya kulijenga badala ya kuacha kila kikundi kiboreshe papo hapo.

**Serikali.** Tathmini lazima ikaguliwe, si kufanywa tu, kwa hiyo hifadhi toleo la seti ya data, vipimo, jina la mpitiaji, na idhini kama ushahidi wa uwajibikaji kwa kila toleo. Mfululizo wa red-team unapaswa kuthibitisha mfumo unakataa kubuni sera au kutaja sheria isiyo kwenye vyanzo vyake, na ununuzi unapaswa kuwataka wauzaji kufichua jinsi walivyotathmini mfano na kutoa uhamishaji wa data yenu ya tathmini. Chombo cha usimamizi kinapouliza mnajuaje zana ni salama, jibu lazima liwe rekodi yenye tarehe, si uhakikisho.

## Mifano

**Kampuni changa.** Kampuni ya watu wanne inayojenga msaidizi wa kupitia mikataba ilianza na lahajedwali ya vifungu arobaini halisi, kila kimoja kikiwekewa lebo na wakili wao wa ndani na hatari kinachopaswa kuweka alama. Kila badiliko la agizo liliendeshwa dhidi ya seti hiyo kwa hati kabla ya kuunganisha, na alama ilichapishwa kwenye ombi la kuvuta. Mtumiaji alipoweka alama kifungu kilichokosekana, kiliingia moja kwa moja kwenye lahajedwali, kwa hiyo seti ilikua na bidhaa. Kiasi kilipopanda waliongeza LLM-kama-hakimu kupima ubora wa maelezo, lakini baada ya kuangalia inakubaliana na wakili kwenye sampuli tu. Nafuu, ya faragha, na ya uaminifu ilishinda kigezo chochote cha umma kwa eneo lao.

**Biashara kubwa.** Benki kubwa iliendesha vipengele kumi na viwili vya AI kuvuka msaada, utafutaji, na zana za ndani, na kila timu ilikuwa ikipima tofauti. Walijenga jukwaa la pamoja la tathmini: mahali pa pamoja pa kuhifadhi seti za dhahabu, kuendesha mfululizo wa nje ya mtandao kwenye CI, kusajili maagizo ya mahakimu wa LLM na alama zao za urekebishaji, na kufuatilia vipimo vya mtandaoni kwa kila kipengele. Utawala uliwekwa juu, na ngazi za hatari zilizoweka kiwango kinachohitajika na idhini kabla ya toleo. Kipengele kipya cha kueleza ulaghai hakingeweza kusafirishwa hadi seti yake ya tathmini ipitiwe, mfululizo wake wa red-team upite, na mmiliki wake anayewajibika asaini matokeo. Kutumia tena jukwaa kulimaanisha timu zilibishana kuhusu eneo lao, si jinsi ya kupima.

**Serikali.** Wakala wa afya ya umma ulisambaza msaidizi wa kuwasaidia wafanyakazi kujibu maswali ya manufaa kutoka mwongozo ulioidhinishwa. Kwa kuwa jibu lisilo sahihi lingeweza kuathiri ustahiki wa mtu, tathmini ililazimika kukaguliwa. Kila toleo liliendesha seti ya tathmini iliyoandikwa ikifunika maswali ya kawaida, kesi za pembeni, na maagizo ya uadui, na matokeo, toleo la seti ya data, vipimo, na jina la mpitiaji vilihifadhiwa kama ushahidi wa uwajibikaji. Mfululizo wa red-team ulikagua mfumo unakataa kubuni sera au kutaja sheria isiyo kwenye vyanzo vyake. Chombo cha usimamizi kilipouliza wakala ulijuaje zana ni salama, jibu lilikuwa rekodi yenye tarehe, si uhakikisho.

## Kesi ya biashara: sababu, ROI, na TCO

Tathmini hujilipia kwa kufanya kila uwekezaji mwingine wa AI kuwa salama na wa haraka zaidi. Faida ya uwekezaji (ROI) inaonekana kama matukio machache ya uzalishaji, marudio ya haraka kwa sababu timu zinaweza kubadilisha maagizo na mifano kwa imani, na uwezo wa kupokea mifano bora siku inapofika kwa sababu unaweza kuthibitisha kama inasaidia. Njia iliyo wazi zaidi ya kuithamini ni gharama ya kutokuwepo kwake: hallucination moja ya umma, matokeo yenye upendeleo, au uvujaji wa data unaweza kugharimu zaidi sana kwa kurekebisha, uaminifu uliopotea, na mfiduo wa udhibiti kuliko miaka ya miundombinu ya tathmini. Ndiyo tofauti kati ya kupata regression kwenye CI bure na kuipata kwenye gazeti.

Jumla ya gharama ya umiliki (TCO) ni halisi na inastahili kutajwa. Unalipia kazi ya uwekaji alama, kokotoo ambalo mahakimu wa kiotomatiki wanatumia, na kazi endelevu ya kuweka seti za tathmini za uwakilishi matumizi yanapohama. Kwa ukubwa wa shirika, jukwaa la pamoja hugawanya sehemu kubwa ya hili kuvuka timu nyingi, hoja imara zaidi ya kulijenga badala ya kuacha kila kikundi kiboreshe. Weka kesi kwa uongozi kwa kuoanisha hatari madhubuti (gharama ya jibu moja baya la umma katika eneo lenu) na uwezo madhubuti (kasi ya kupokea kila mfano mpya kwa usalama), na kwa kuweka tathmini kama kidhibiti kinachoruhusu shirika kusonga haraka bila kusonga kizembe.

## Mifumo mibaya na mitego

- **Kusafirisha kwa hisia.** Kuhukumu mabadiliko ya AI kwa kujaribu maagizo machache kwa mkono, bila seti ya data wala alama inayojirudia.
- **Maigizo ya vigezo.** Kuamini alama imara ya kigezo cha umma kama uthibitisho mfumo unafaa kazi yako, ukipuuza uchafuzi na kutolingana kwa usambazaji.
- **Kufaa kupita kiasi kwa seti ya tathmini.** Kurekebisha maagizo dhidi ya seti ileile iliyowekwa hadi namba ni ya juu na haina maana, bila seti mpya ya kando.
- **Mahakimu wasiorekebishwa.** Kusambaza LLM-kama-hakimu na kuamini alama zake bila kuangalia mkubaliano na wapimaji wa binadamu.
- **Kuabudu vipimo.** Kuboresha BLEU au ROUGE kana kwamba ni ubora, na kusafirisha majibu mabaya zaidi yanayoingiliana na maandishi ya rejeo tu.
- **Red teaming ya mara moja.** Kushambulia mfumo mara moja kabla ya uzinduzi na kutogeuza matokeo kuwa majaribio ya kudumu ya regression.
- **Imani ya nje ya mtandao tu.** Kuamini alama nzuri ya nje ya mtandao inamaanisha kipengele kinafanya kazi, bila kipimo cha mtandaoni cha matokeo halisi.
- **Seti za tathmini yatima.** Seti za data ambazo hakuna anayezimiliki, ambazo hazipokei kamwe kushindwa kwa uzalishaji na polepole zinaacha kuakisi uhalisia.

## Kielelezo cha ukomavu

- **Ngazi ya 1, Kuanzisha:** Mabadiliko ya AI yanahukumiwa kwa mkono kwenye mifano michache, kwa kuitikia, mtu anapohangaika tu. Hakuna seti ya data, hakuna alama inayojirudia, na hakuna lango. Regression zinapatikana na watumiaji, na hakuna anayeweza kusema kama mfumo ni bora au mbaya kuliko mwezi uliopita.
- **Ngazi ya 2, Kuendeleza:** Baadhi ya timu huweka seti ndogo za dhahabu na kuziendesha kwa mkono kabla ya mabadiliko makubwa, na alama chache za kawaida au za rejeo zipo. Mapitio ya binadamu hufanyika kwa vipengele muhimu, lakini upimaji hauna uthabiti kuvuka timu, tathmini haijaotomatishwa wala kuwekewa lango, na kila kikundi kinafanya tofauti.
- **Ngazi ya 3, Kusawazisha:** Mfululizo wa nje ya mtandao unaendeshwa kwenye ujumuishaji endelevu kwa kila badiliko la agizo, mfano, au urejeshaji na unaweka lango la muunganisho, kwa mazoea moja yaliyoandikwa kuvuka shirika. LLM-kama-hakimu imerekebishwa dhidi ya lebo za binadamu, red teaming ni mfululizo unaojirudia, na seti za data zinamilikiwa, zina matoleo, na zinalishwa na kushindwa kwa uzalishaji, uchafuzi ukilindwa kikamilifu.
- **Ngazi ya 4, Kusimamia:** Tathmini inapimwa na kudhibitiwa kwa data dhidi ya vipimo vya msingi. Viwango vya mkubaliano kati ya hakimu na binadamu, viwango vya kupita vya red-team, alama kwa kila sehemu, mafanikio ya kazi ya mtandaoni, na kuteleza vinafuatiliwa kwa muda, na miunganisho inawekewa lango kwa vizingiti na ukingo wa regression badala ya mbio moja kamilifu. Gharama ya uwekaji alama na kokotoo kwa kila mbio inapangiwa bajeti kwa kila kipengele, urekebishaji unafanyika kwa ratiba, na kila matokeo yanabeba mmiliki anayewajibika na idhini.
- **Ngazi ya 5, Kuratibu:** Jukwaa la pamoja la tathmini linahudumia shirika zima, na tathmini ya nje na ya mtandaoni zinaunda mzunguko endelevu uliofungwa na matokeo ya biashara. Mifano mipya inathibitishwa dhidi ya seti za tathmini zinazohamishika siku inapofika, jalada linajirekebisha matumizi na hatari vinapohama, ushahidi wa tathmini unakaguliwa kwa wadhibiti na usimamizi, na mafunzo kutoka kushindwa kwa timu moja yanatiririka kwenye seti za data za kila timu.

## Mawazo ya kujadili

1. Mnaamuaje wakati alama ya nje ya mtandao ina nguvu ya kutosha kuhalalisha jaribio la mtandaoni, na lini haina?
2. Uwiano sahihi wa tathmini ya binadamu na upimaji wa kiotomatiki kwa wasifu wenu wa hatari ni upi, na mnapaswa kuupitia mara ngapi?
3. Kigezo cha umma na seti yenu ya faragha ya tathmini zinapotofautiana kuhusu mfano upi ni bora, mnamwamini yupi na kwa nini?
4. Mnaiwekaje seti ya tathmini ikiwa ya uwakilishi tabia ya watumiaji inapohama, bila kuiacha ivimbe hadi iwe polepole mno kuendesha kwenye CI?
5. Nini kinastahili kuwa kwenye mfululizo wa red-team kwa eneo lenu, na nani ana sifa za kubuni mashambulizi?
6. Mnatathminije njia ya wakala, si jibu lake la mwisho tu, bila kuzama katika gharama ya kupima kila hatua?

## Mambo muhimu ya kukumbuka

- Tathmini ya AI inatofautiana na majaribio ya programu kwa sababu matokeo hayaamuliwi na mara chache kuna jibu moja sahihi, kwa hiyo unapima ubora kuvuka kesi za uwakilishi badala ya kuthibitisha thamani kamili.
- Fanya uendelezaji unaoendeshwa na tathmini: fafanua ubora unaopimika kwanza, kisha ujenge kuelekea hapo, na urudishe kila kushindwa kwa uzalishaji kwenye seti.
- Weka njia kwa tabaka kwa kasi na uaminifu: upimaji wa kiotomatiki wa bei nafuu kwa marudio ya mara kwa mara, busara ya binadamu kama nanga, na urekebishaji kuviweka sawa.
- Jilinde dhidi ya uchafuzi na kufaa kupita kiasi, la sivyo namba zako zitakubembeleza huku mfumo halisi unawakatisha tamaa watumiaji.
- Unganisha tathmini ya nje ya mtandao kwenye CI kama lango na uendelee kupima ubora na kuteleza kwenye uzalishaji, kwa sababu mfano uliokuwa mzuri wakati wa uzinduzi unaweza kuoza.

## Marejeo na usomaji zaidi

- Chip Huyen, *AI Engineering: Building Applications with Foundation Models*.
- Lianmin Zheng et al., *Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena*.
- Kishore Papineni et al., *BLEU: A Method for Automatic Evaluation of Machine Translation*.
- Chin-Yew Lin, *ROUGE: A Package for Automatic Evaluation of Summaries*.
- Percy Liang et al., *Holistic Evaluation of Language Models (HELM)*.
- Deep Ganguli et al., *Red Teaming Language Models to Reduce Harms: Methods, Scaling Behaviors, and Lessons Learned*.
- OWASP Foundation, *OWASP Top 10 for Large Language Model Applications*.
- National Institute of Standards and Technology, *AI Risk Management Framework*.
