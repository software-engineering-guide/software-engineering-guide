# 2.14 Muundo wa mradi na hazina

## Muhtasari na msukumo

Muundo wa mradi na hazina ni mpangilio halisi wa msimbo: folda, faili, na kanuni za majina zinazoamua kila kitu kinaishi wapi. *Hazina* (mara nyingi hufupishwa "repo") ni chombo kinachodhibitiwa kwa [udhibiti wa matoleo](https://en.wikipedia.org/wiki/Version_control) kinachoshikilia faili za mradi na historia yake. *Mradi*, wakati mwingine huitwa *solution* unapokusanya vipengele kadhaa vinavyohusiana, ni kitengo cha kimantiki cha programu unayoijenga. Muundo ni ramani unayotumia kupata, kuelewa, na kubadilisha programu hiyo.

Katika timu ndogo, mtu mmoja anaweza kushikilia mpangilio mzima kichwani. Katika timu kubwa, yenye mamia au maelfu ya wahandisi, kuhama mara kwa mara kati ya timu, na wakandarasi wanaojiunga na kuondoka, kila hazina inayopangwa tofauti hutoza kodi mpya ya kiakili. Unapofungua repo usiyoifahamu, unapaswa kuweza kukisia chanzo, majaribio, nyaraka, na usanidi wa usambazaji viko wapi, bila kusoma mwongozo. Kila repo inapojibu maswali hayo kwa njia ileile, uhamaji ni wa bei nafuu na utambulisho ni wa haraka. Kila repo ikiwa ya pekee, kila mabadiliko ya muktadha hugeuka mradi mdogo wa utafiti.

Katika mazingira ya mashirika makubwa na ya serikali, muundo thabiti pia ni suala la udhibiti na uhakikisho. Wakaguzi, wapitiaji wa usalama, na wadumishaji wa muda mrefu, mara nyingi wakifanya kazi miaka baada ya waandishi wa asili kuondoka, wanahitaji kupata kwa uhakika nyaraka za ubainishaji, faili za leseni, sera za usalama, na fasili za ujenzi. Mpangilio unaotabirika pia unaruhusu zana za kiotomatiki (vichanganuzi, wachambuzi wa utegemezi, ukaguzi wa uzingatiaji) kufanya kazi kwa njia ileile kuvuka jalada zima la mifumo. Kwa hiyo sura hii inachukulia muundo kama kanuni unayoamua mara moja na kuitumia kila mahali. Unahusiana kwa karibu na viwango vya uandishi wa msimbo na mtindo (sura ya 2.1), udhibiti wa matoleo na usimamizi wa chanzo (sura ya 2.6), na nyaraka (sura ya 2.7).

## Kanuni kuu

- Fuata *[kanuni ya mshangao mdogo kabisa](https://en.wikipedia.org/wiki/Principle_of_least_astonishment)*: mpangilio unapaswa kulingana na kile mhandisi mwenye uzoefu angetarajia, ili kusiwe na kitu cha kukariri.
- Uthabiti kuvuka hazina hushinda ubunifu wa mahali pamoja; muundo wa kutosha wa sare kila mahali una thamani kuliko muundo kamili mahali pamoja.
- [README](https://en.wikipedia.org/wiki/README) ni mlango wa mbele; mgeni anapaswa kujielekeza kutoka kwake peke yake.
- Fanya muundo ujieleze kupitia majina, ili folda na faili zitangaze madhumuni yake.
- Tekeleza muundo kwa jukwaa la ujenzi na violezo, si kwa nguvu ya nia na maoni ya mapitio.
- Tenganisha wasiwasi kimwili: chanzo, majaribio, nyaraka, ujenzi, na usambazaji vinastahili kuwa katika sehemu tofauti, zinazotabirika.
- Panga utegemezi utiririke upande mmoja, kutoka viini thabiti kuelekea kingo tete.

## Mapendekezo

### Pokea mpangilio thabiti wa ngazi ya juu

Fafanua seti ya kawaida ya folda za ngazi ya juu ambazo kila hazina inatumia inapofaa, na uandike kila moja ni ya nini. Kanuni ya kawaida isiyoegemea muuzaji ni pamoja na: folda ya chanzo (mara nyingi `src`) kwa msimbo wa uzalishaji; folda ya majaribio (mara nyingi `test` au `tests`) kwa majaribio ya kiotomatiki; folda ya `docs` kwa nyaraka; folda ya `build` kwa fasili za ujenzi na matokeo; folda ya `deploy` kwa usambazaji na *[miundombinu kama msimbo](https://en.wikipedia.org/wiki/Infrastructure_as_code)* (fasili zinazosomeka na mashine za seva, mitandao, na huduma, zilizoshughulikiwa katika sura ya 8.2); folda ya `scripts` kwa uotomatishaji na zana za wasanidi; folda ya `examples` kwa sampuli zinazoweza kuendeshwa; na folda ya `spec` au `specification` kwa mahitaji na ubainishaji wa usanifu. Si kila repo inahitaji kila folda, lakini pale wasiwasi upo, unapaswa kuishi mahali panapotarajiwa kwa jina linalotarajiwa.

### Fanya README kuwa sehemu ya kuingilia

Hitaji faili ya README kwenye mzizi wa hazina kama mahali pa kuanzia pekee, pa kikanuni. Inapaswa kusema mradi ni nini, jinsi ya kuujenga na kuuendesha, jinsi ya kuendesha majaribio, mahali pa kupata nyaraka za kina zaidi, nani anaumiliki, na jinsi ya kuchangia. README si seti nzima ya nyaraka; ni faharasa inayoelekeza kwa zingine (sura ya 2.7). Chukulia README iliyokosekana au iliyopitwa na wakati kama kasoro, kwa sababu ndicho kitu cha kwanza kila mhandisi mpya, mkaguzi, au mwunganishaji atakisoma.

### Sawazisha faili za kihariri na usanidi

Weka usanidi wa pamoja wa kihariri na zana kwenye hazina ili kila mchangiaji apate tabia thabiti kiotomatiki. Faili ya `.editorconfig` (faili rahisi isiyoegemea kihariri inayofafanua kanuni za nafasi, ujongezaji, na miisho ya mistari) huweka muundo wa msingi sare kuvuka vihariri na mifumo ya uendeshaji tofauti. Ongeza faili ya kupuuza kwa mfumo wa udhibiti wa matoleo (ili matokeo ya ujenzi na vitu vya ndani visiwekwe kamwe), pamoja na usanidi wa pamoja wa kipanga muundo na linter ulioelezwa katika sura ya 2.1. Faili hizi hufanya kanuni za hazina ziwe hai, si zilizoandikwa tu.

### Fafanua kanuni za majina na folda

Kubaliana kanuni za kutaja folda na faili (herufi kubwa/ndogo, vitenganishi, umoja dhidi ya wingi, na viambishi vinavyohitajika kama vile vinavyoashiria majaribio) na uzitumie kwa usawa. Majina yanapaswa kufichua nia na kulingana na msamiati wa kikoa unaotumika kwingineko katika shirika. Lengo ni rahisi: njia inapaswa kuwasilisha maana, ili kusoma jina la folda au faili kukuambie kilichomo bila kukifungua.

### Panga tabaka na utegemezi kwa makusudi

Panga msimbo ili tabaka zake za usanifu zionekane katika mpangilio wa folda, na ili utegemezi utiririke upande mmoja, wenye busara. Sera ya kiwango cha juu haipaswi kutegemea undani wa kiwango cha chini. Msimbo wa pamoja, thabiti unapaswa kukaa mahali moduli nyingi zinaweza kuufikia bila kuunda mizunguko. Unapofanya tabaka kuwa halisi, zilizoakisiwa kwenye mti wa saraka, wahandisi wana uwezekano mkubwa wa kuviheshimu, na ukiukaji ni rahisi kuuona kwenye mapitio na ukaguzi wa kiotomatiki wa utegemezi.

### Tekeleza muundo kwa jukwaa la ujenzi na violezo

Toa *[jukwaa la ujenzi](https://en.wikipedia.org/wiki/Scaffold_%28programming%29)*, uzalishaji wa kiotomatiki wa mradi wa kuanzia, ili hazina mpya zianze zikiwa sahihi tayari. *Kiolezo* au *cookiecutter* (mifupa ya mradi yenye vigezo inayozalisha hazina tayari kutoka majibu ya maswali machache) huweka mpangilio wa kawaida, README, faili za usanidi, na usanidi wa [CI](https://en.wikipedia.org/wiki/Continuous_integration) mahali pamoja. Wahandisi wanapounda huduma mpya kutoka kiolezo cha pamoja, uthabiti unakuwa chaguo-msingi badala ya matamanio, na maboresho ya kiolezo hutiririka hadi miradi ya baadaye.

### Weka muundo thabiti kuvuka hazina nyingi kwa ukubwa

Chukulia mpangilio wenyewe kama kiwango kinachotawaliwa: kinachodumishwa kati kama kiwango kingine chochote cha kihandisi (sura ya 1.7), na kinachowekwa katika matoleo kama msimbo (sura ya 2.6). Kichapishe, toa violezo vinavyokitekeleza, na ruhusu mikengeuko kupitia mchakato ulioandikwa wa vighairi tu, ili "kiwango" kihifadhi maana yake. Kwa ukubwa wa jalada, karibu thamani yote ya muundo inatokana na usawa wake kuvuka hazina, kwa hiyo kuteleza ndiyo hatari kuu ya kusimamia.

### Acha muundo ufahamishe uchaguzi wa monorepo dhidi ya hazina nyingi

Husisha muundo na uamuzi wa mpaka wa hazina ulioshughulikiwa katika sura ya 2.6. *[Monorepo](https://en.wikipedia.org/wiki/Monorepo)* (hazina moja inayoshikilia miradi mingi) inahitaji kanuni wazi ya ndani ya kutenganisha miradi na msimbo wake wa pamoja, ili mti mmoja ubaki unaoweza kupitika. Mbinu ya *hazina nyingi* (hazina nyingi ndogo, moja kwa kila mradi au huduma) inahitaji uthabiti imara kuvuka hazina, ili kila repo ihisi inayofahamika ingawa inasimama peke yake. Vyovyote, muundo ulioandikwa, wenye violezo ndio unaoweka urambazaji unaotabirika. Uchaguzi wa mpaka hubadilisha mahali unapotumia kanuni, si kama unaihitaji.

## Mabadilishano: faida na hasara

| Chaguo | Faida | Hasara |
|---|---|---|
| Mpangilio wa kawaida mkali wa shirika zima | Kufahamika papo hapo; wahandisi wanaohamishika; zana sare | Wakati mwingine haufai miradi isiyo ya kawaida; unahitaji utawala |
| Uhuru wa mpangilio kwa kila timu | Uboreshaji wa mahali; uhuru wa juu | Mgawanyiko; kubadilisha muktadha kwa gharama; zana zisizo thabiti |
| Jukwaa la ujenzi na violezo | Hazina sahihi kwa chaguo-msingi; mabadiliko yanaenea | Matengenezo ya kiolezo; hatari ya kuteleza kwa hazina zilizozalishwa |
| Daraja la folda lenye kina, la tabaka | Muundo wazi; mipaka wazi | Mzigo wa urambazaji; njia ndefu; hatari ya kuhandisi kupita kiasi |
| Mpangilio tambarare, usio na kina | Rahisi kuchanganua; taratibu chache | Kutenganisha duni; huvunjika mradi unapokua |

Mabadilishano makuu ni usawa dhidi ya uhuru. Mpangilio mmoja wa kawaida huondoa msuguano kwa wahandisi wengi wanaohama kati ya misimbo, kwa gharama ya mradi wa mara moja moja ambao mahitaji yake hayaingii vizuri kwenye ukungu. Katika shirika kubwa, faida ya pamoja ya kufahamika karibu daima inazidi hasara hiyo ya mahali. Ndiyo maana msimamo unaopendekezwa ni kiwango chaguo-msingi imara pamoja na njia iliyoandikwa ya vighairi (sura ya 1.7), badala ya usawa mgumu au uhuru usiosimamiwa. Mabadilishano ya pili ni kina dhidi ya urahisi: muundo wa kutosha kutenganisha wasiwasi halisi, lakini si mwingi kiasi cha urambazaji kugeuka matembezi kupitia folda tupu.

## Maswali ya kujadili na timu yako

1. **Mhandisi anapohamia repo yetu asiyoifahamu, inachukua muda gani hadi aweze kupata majaribio, usanidi wa usambazaji, na mmiliki?** Hii ndiyo kodi ya urambazaji ambayo muundo upo kuiondoa, na kwa ukubwa wa jalada inalipwa maelfu ya mara kwa mwaka kwa vipande vidogo vinavyojumlika kuwa upotevu mkubwa wa muda wa kihandisi. Hoja ya kanuni ya mshangao mdogo ni kwamba mhandisi mwenye uzoefu anapaswa kuweza kukisia chanzo, majaribio, nyaraka, na usambazaji viko wapi bila kusoma mwongozo, kwa hiyo jaribio la uaminifu ni kama kukisia huko kunafaulu kuvuka repo zenu. Leta namba halisi kwenye mkutano: jipime muda mkijielekeza katika repo mbili au tatu za ndani msizozifahamu, au vuta data ya utambulisho kuhusu wanachama wapya wanachukua muda gani kufanya badiliko la kwanza. Jibu likipimwa kwa siku za utafiti badala ya dakika za kutambua, mmepima gharama ya repo za pekee, na hilo linahalalisha uwekezaji wa mara moja katika mpangilio wa kawaida ambao kila repo inaushiriki.

2. **Tabaka zetu za usanifu zinaonekana kwenye mti wa folda, au mizunguko ya utegemezi inajificha ndani ya mpangilio tambarare?** Muundo ni zaidi ya kupatikana: unapofanya tabaka kuwa halisi, wahandisi wanaziheshimu na wapitiaji na ukaguzi wa kiotomatiki wa utegemezi wanaweza kuona ukiukaji, ilhali rundo tambarare huruhusu uunganishaji usiofaa na mizunguko kupenya bila kuonekana hadi mabadiliko yawe hatari. Katika mfumo mkubwa, wa muda mrefu hili ndilo linaloweka sera ya kiwango cha juu isitegemee kimyakimya undani wa kiwango cha chini, na ni aina hasa ya mmomonyoko ambao ni nafuu kuzuia na ghali kutengua. Leta grafu yenu ya utegemezi au endesha ukaguzi wa haraka: kuna mizunguko, na kuna kitu thabiti kinachotegemea kitu tete? Jibu linapaswa kukusukuma kuakisi tabaka katika saraka na kuongeza ukaguzi wa kiotomatiki wa mwelekeo wa utegemezi, ili mipaka ionekane kwenye mti na itekelezwe kwenye bomba badala ya kuishi kwenye mfano wa kiakili wa mtu tu.

3. **Hazina zetu mpya zinaanza sahihi kutoka kiolezo, au tunategemea ukurasa wa wiki na nia njema?** Muundo unaotekelezwa na jukwaa la ujenzi ndio chaguo-msingi; muundo ulioelezwa kwenye waraka huteleza, kwa sababu uhalisia hufuata kinachozalisha repo, si ukurasa unasema zinapaswa kuonekanaje. Kwa shirika kubwa au linalodhibitiwa hili pia ni suala la uhakikisho: kila repo inapozalishwa kutoka kiolezo cha pamoja, vichanganuzi vya usalama, wachambuzi wa utegemezi, na wakaguzi wanapata leseni, sera ya usalama, ubainishaji, na fasili ya ujenzi mahali pamoja kila mara, kuvuka wauzaji na kuvuka miaka. Leta ushahidi: repo zenu za hivi karibuni ngapi zilijengwa kwa jukwaa kutoka kiolezo cha kawaida dhidi ya kukusanywa kwa mkono, na zile za kiolezo zimeteleza kiasi gani tangu hapo? Hatua ni kufanya kiolezo kiwe njia pekee rahisi ya kuanzisha repo, kukitawala kama kiwango chenye matoleo na njia ya vighairi iliyoandikwa, na kugundua kuteleza kiotomatiki, kwa sababu usawa ndipo karibu thamani yote ya muundo inapoishi.

4. **Tumeamua kama kiwango chetu kinahusu monorepo au hazina nyingi tofauti, na je, kanuni ileile inashikilia pande zote mbili za mpaka huo?** Uchaguzi wa mpaka wa hazina hubadilisha mahali unapotumia kanuni, si kama unaihitaji, na kukosea kunamaanisha mti mmoja mkubwa ambao hakuna anayeweza kuupitia au mtawanyiko wa repo ambazo kila moja inahisi ngeni. Monorepo inahitaji kanuni wazi ya ndani ya kutenganisha miradi na msimbo wake wa pamoja ili mti mmoja ubaki unaoweza kupitika, ilhali mbinu ya hazina nyingi inahitaji uthabiti imara kuvuka hazina ili kila repo inayojitegemea ihisi inayofahamika. Leta orodha ya sasa: repo ngapi mnazo, msimbo wa pamoja unatenganishwa vipi ndani ya monorepo yoyote, na jaribio la muda la kama mhandisi anaweza kupata mradi ndani ya mti mkubwa haraka kama anavyoupata kwenye repo inayojitegemea. Kwa shirika kubwa au programu ya serikali ambapo wauzaji tofauti hutoa hazina tofauti, amua kwa makusudi sehemu zipi za kanuni ni za ulimwengu wote na zipi ni mahususi kwa mpaka, kwa sababu wakaguzi na zana za jukwaa lazima zifanye kazi kwa njia ileile iwe msimbo unafika kama mti mmoja au hamsini.

5. **Nani anamiliki kiwango chetu cha muundo, na hasa nini kinatokea mradi unaposhindwa kweli kuendana nacho?** Kwa ukubwa wa jalada, karibu thamani yote ya muundo inatokana na usawa, kwa hiyo hatari halisi ni kiwango kisicho na mmiliki kinachooza na njia ya vighairi isiyo wazi hadi kila timu inavumbua kimyakimya mpangilio wake. Mvutano ni kati ya usawa mgumu usiofaa mradi wowote usio wa kawaida na uhuru usiosimamiwa unaogawanya kila kitu, na jibu lenye afya ni chaguo-msingi imara pamoja na mchakato ulioandikwa, unaokaguliwa wa vighairi unaotawaliwa na mmiliki aliyetajwa na kuwekwa katika matoleo kama msimbo. Leta ushahidi: kuna mmiliki mmoja anayewajibika, waraka wa kiwango wenye matoleo na rekodi ya mabadiliko, kumbukumbu ya vighairi vilivyotolewa na kwa nini, na hesabu ya mikengeuko isiyoandikwa unayoweza kuipata porini. Katika mazingira ya mashirika makubwa na ya serikali kighairi ambacho hakuna aliyekirekodi ni pengo la udhibiti, kwa hiyo funga kila mkengeuko na sababu iliyoandikwa na tarehe ya mapitio, na uhakikishe mikataba ya ununuzi inayoamuru mpangilio pia inataja nani anaweza kuidhinisha kuondoka kwake.

6. **README na faili zetu za usanidi zilizowekwa kwenye hazina zinafanya kanuni zetu kuwa hai, au ni mapambo?** README ni mlango wa mbele, na `.editorconfig`, faili ya kupuuza, na usanidi wa linter ulioangaliwa ndani ndizo zinazofanya kanuni zijitekeleze, hata hivyo hivi ndivyo vitu vya kwanza kupitwa na wakati na vya mwisho kugunduliwa hadi mkaguzi au mwanachama mpya ashindwe kujenga mradi. Mvutano ni kati ya README fupi inayobaki ya sasa na ile ya kina inayoteleza, na kati ya kuwaamini watu kupanga msimbo kwa usahihi na kuruhusu usanidi wa pamoja uutekeleze kiotomatiki. Leta sampuli: vuta repo tano na uangalie README ngapi zinaeleza kweli mradi ni nini, jinsi ya kujenga, kujaribu, na kuuendesha, na nani anaumiliki, na ngapi zinabeba faili za usanidi wa pamoja badala ya kutegemea tabia za mtu binafsi. Kwa shirika kubwa au linalodhibitiwa, ambapo waunganishaji, wapitiaji wa usalama, na wadumishaji wa muda mrefu husoma README kabla ya chochote kingine, chukulia mlango wa mbele uliokosekana au uliopitwa na wakati kama kasoro yenye mmiliki, na ukague uwepo wa faili za usanidi kiotomatiki ili ulinganifu usitegemee nia njema.

## Mtazamo wa sekta

**Kampuni changa.** Kasi inashinda, kwa hiyo kubaliana mpangilio mmoja rahisi, tambarare wa kutosha kwa repo yako ya kwanza (src, test, docs, scripts, README iliyojazwa, `.editorconfig`, na faili za kupuuza) na uuhifadhi kama kiolezo chepesi alasiri hiyohiyo. Zalisha huduma ya pili kutoka kwake ili repo zote mbili zihisi zinazofahamika na mkandarasi mpya ajifunze kwa saa badala ya kuchambua repo ya pekee. Pinga madaraja yenye kina na utawala mzito usioyahitaji bado; mapato yote hapa ni kwamba waanzilishi wawili na mkandarasi wanashiriki ramani moja.

**Biashara ndogo.** Bila mtaalamu wa jukwaa na bajeti finyu, pokea mpangilio wa kawaida ambao lugha au mfumo wako wa kazi tayari unaudhania badala ya kuvumbua mwingine, ili zana zilizotengenezwa tayari na mwajiriwa yeyote mpya wafike wakiwa wamefunzwa juu yake. Nunua jukwaa la ujenzi (kizalishaji cha mfumo wa kazi au kiolezo cha cookiecutter) badala ya kujenga chako, na utumie juhudi yako adimu kuweka README iliyojazwa ikiwa ya sasa. README hiyo ndiyo bima ya bei nafuu zaidi uliyo nayo kwa siku mtu mmoja aliyejua mpangilio atakapohama.

**Biashara kubwa.** Kuvuka timu nyingi na mamia ya hazina lengo ni usawa: chapisha kiwango cha muundo chenye matoleo, zalisha kila huduma mpya kutoka violezo vya pamoja, gundua kuteleza kiotomatiki, na ruhusu mikengeuko kupitia mchakato ulioandikwa wa vighairi tu. Kwa sababu kila repo inaonekana sawa, mhandisi aliyehamishwa kwenda timu mpya anakuwa na tija ndani ya saa, na vichanganuzi vya usalama na utegemezi vya jalada zima vinapata leseni, sera ya usalama, na fasili ya ujenzi mahali pamoja kila mara. Weka bajeti ya matengenezo ya kiolezo na ugunduzi wa kuteleza waziwazi, kwa sababu utunzaji huo ndio unaoweka kiwango na maana kwa ukubwa.

**Serikali.** Ununuzi, uwazi, na uwajibikaji wa muda mrefu huumba mpangilio, kwa hiyo amuru muundo wa pamoja katika viwango vya utoaji vinavyomfunga kila muuzaji. Hitaji folda ya `specification` inayounganisha msimbo na mahitaji yaliyoidhinishwa, faili ya leseni na sera ya usalama kwenye mzizi, na folda ya `deploy` inayoshikilia fasili za miundombinu kama msimbo, ili wakaguzi wapate vitu vya uzingatiaji kwa njia ileile kwa kila mfumo. Kwa sababu wakandarasi kutoka wauzaji tofauti wote wanafuata ramani moja, matengenezo baada ya mkataba kuisha yanagharimu kidogo zaidi sana, na umma unapata njia inayoweza kutetewa, inayokaguliwa kutoka hitaji hadi msimbo unaoendesha.

## Mifano

**Kampuni changa.** Kampuni changa ya watu watatu inakubaliana mpangilio rahisi wa kawaida kwa repo yake ya kwanza (src, test, docs, scripts, README iliyojazwa, .editorconfig, na faili za kupuuza) na kuuhifadhi kama kiolezo chepesi. Wanapoanzisha huduma yao ya pili mwezi mmoja baadaye, wanaizalisha kutoka kiolezo hicho, kwa hiyo repo zote mbili tayari zinahisi zinazofahamika na mkandarasi mpya anajifunza ndani ya alasiri. Wanapinga madaraja ya folda yenye kina wasiyoyahitaji bado, wakiweka mti tambarare vya kutosha kuchanganua kwa mtazamo. Gharama ilikuwa alasiri moja ya usanidi, na inawaokoa kutoka kwa mtawanyiko wa repo za pekee ambao vinginevyo ungefanya kila repo ya baadaye kuwa mradi mdogo wa utafiti.

**Biashara kubwa.** Muuzaji wa rejareja wa kimataifa anaendesha mamia ya huduma kuvuka lugha kadhaa. Timu yake ya jukwaa inachapisha kiwango cha muundo wa hazina chenye matoleo na seti ya violezo vya miradi vinavyokitekeleza. Kila huduma mpya inazalishwa kutoka kiolezo, kwa hiyo inafika na folda za kawaida za `src`, `test`, `docs`, `deploy`, na `scripts`, README iliyojazwa, `.editorconfig`, faili za kupuuza, na bomba la CI linalofanya kazi. Kwa sababu kila hazina inaonekana sawa, mhandisi aliyehamishwa kwenda timu mpya anakuwa na tija ndani ya saa, na vichanganuzi vya usalama na utegemezi vya shirika zima vinaendeshwa kwa usawa kwa sababu daima vinapata faili mahali vinapotarajia.

**Serikali.** Wakala wa kitaifa unaoboresha mifumo ya zamani unaamuru mpangilio wa pamoja wa hazina kama sehemu ya viwango vyake vya utoaji kwa wauzaji wote. Kila hazina lazima iwe na folda ya `specification` inayounganisha msimbo na mahitaji yaliyoidhinishwa, README iliyoandikwa, faili ya leseni na sera ya usalama kwenye mzizi, na folda ya `deploy` inayoshikilia fasili za miundombinu kama msimbo (sura ya 8.2). Kwa sababu wakandarasi kutoka wauzaji tofauti wote wanafuata muundo uleule, wakaguzi wa wakala wanaweza kupata vitu vya uzingatiaji kwa njia ileile kwa kila mfumo, na matengenezo ya muda mrefu baada ya mkataba kuisha yanagharimu kidogo zaidi sana kwa sababu wadumishaji wanaoingia tayari wanajua ramani.

## Kesi ya biashara: sababu, ROI, na TCO

Gharama ya kupokea kiwango cha muundo hasa ni ya mara moja: kukubaliana mpangilio, kujenga violezo, na kuandika kanuni. Gharama ya mara kwa mara ni ndogo, imejikita katika kudumisha violezo na kutawala vighairi. Gharama ya *kutokuwa* na kiwango inajirudia na kujumlika: kila mhandisi anayefungua repo asiyoifahamu hulipa kodi ya urambazaji, kila utambulisho unaenda polepole zaidi, na zana za kiotomatiki lazima zisanidiwe kwa kila repo kwa sababu hakuna kitu kilicho mahali unapotarajia. Kuvuka shirika kubwa, misuguano hii midogo huzidishwa kuwa hasara kubwa za muda wa kihandisi.

Mapato yanaonekana kama utambulisho wa haraka, uhamaji wa bei nafuu kati ya timu, ishara ya juu zaidi kutoka zana za jalada zima, na, katika mazingira yanayodhibitiwa, gharama ya chini ya ukaguzi na matengenezo ya muda mrefu, kwa sababu vitu vinapatikana kila mara. *Jumla ya gharama ya umiliki* (TCO, yaani gharama kamili ya maisha ya kujenga, kuendesha, na kudumisha mfumo) hupungua zaidi katika mifumo ya muda mrefu, ambapo wadumishaji wanaonufaika na muundo unaotabirika kwa kawaida si waandishi walioiunda. Kujenga hoja kwa uongozi, weka muundo kama kiwango cha gharama ya chini, kiegemeo cha juu kinachoboresha tija ya wasanidi na utayari wa ukaguzi, na uweke namba kwenye gharama ya leo ya kutokuwa na uthabiti ukitumia data ya muda wa utambulisho na juhudi inayotumika kutafuta vitu katika hazina zisizofahamika.

## Mifumo mibaya na mitego

- **Hazina ya pekee:** kila repo ikipangwa tofauti, kwa hiyo kila moja lazima ijifunzwe upya kutoka mwanzo.
- **README iliyokosekana au iliyopitwa na wakati:** hakuna mlango wa mbele, ukiwalazimisha wageni kuchambua jinsi ya kujenga na kuendesha mradi.
- **Muundo kwa waraka, si kwa kiolezo:** ukurasa wa wiki unaelezea mpangilio wa kawaida, lakini hakuna kitu kinachoutengeneza au kuutekeleza, kwa hiyo uhalisia unauhama.
- **Kuteleza kwa kiolezo:** hazina zilizozalishwa kutoka kiolezo hutofautiana kwa muda na maboresho ya kiolezo hayazifikii kamwe.
- **Daraja lililohandisiwa kupita kiasi:** viota vya kina vya folda karibu tupu vinavyoongeza taratibu bila kusaidia urambazaji.
- **Wasiwasi uliochanganywa:** chanzo, majaribio, matokeo ya ujenzi, na siri zimechanganywa bila kutenganishwa wazi.
- **Matokeo ya ujenzi na vitu vya ndani vilivyowekwa:** faili zilizozalishwa kuwekwa kwa sababu kanuni za kupuuza hazikuwekwa kamwe, zikichafua historia na tofauti.
- **Ukiukaji wa tabaka uliofichwa na muundo tambarare:** hakuna mipaka halisi, kwa hiyo mizunguko ya utegemezi na uunganishaji usiofaa hupenya bila kuonekana.

## Kielelezo cha ukomavu

- **Ngazi ya 1 (Kuanzisha):** Kila hazina inapangwa kwa papo hapo na waandishi wake, ikiitikia chochote wakati unahitaji; mipangilio hutofautiana sana; README hazipo au hazitegemewi; wageni lazima waongozwe kupitia kila repo kwa mkono.
- **Ngazi ya 2 (Kuendeleza):** Kanuni za msingi zipo kwa njia isiyo rasmi na repo nyingi zinafanana; baadhi ya timu zinaweka mpangilio wa kuanzia wao wenyewe; lakini hakuna kiwango chenye mamlaka, hakuna jukwaa la ujenzi la pamoja, na muundo unateleza dhahiri kutoka timu moja hadi nyingine.
- **Ngazi ya 3 (Kusawazisha):** Kiwango kilichoandikwa, chenye matoleo cha muundo kinatekelezwa shirika zima; hazina mpya zinazalishwa kutoka violezo vya pamoja vinavyobeba mpangilio wa kawaida, README, faili za usanidi, na CI; mikengeuko hupitia mchakato ulioandikwa wa vighairi badala ya kutokea kimyakimya.
- **Ngazi ya 4 (Kusimamia):** Ulinganifu na kiwango unapimwa na kudhibitiwa kwa data: ukaguzi wa kiotomatiki unaripoti sehemu ya repo zinazolingana na mpangilio, hazina za kiolezo zimeteleza kiasi gani, ukamilifu wa README, na ukiukaji wa mwelekeo wa utegemezi, vyote vikifuatiliwa dhidi ya vipimo vya msingi; nyakati za utambulisho na urambazaji zinapimwa; vighairi vinarekodiwa na kupitiwa, na mabadiliko ya kiolezo yanaidhinishwa kwa ushahidi badala ya maoni.
- **Ngazi ya 5 (Kuratibu):** Muundo unaboreshwa kila wakati na unabadilika: maboresho ya kiolezo yanaenea kiotomatiki kwenye hazina zilizopo, utawala wa muundo umeunganishwa na zana za usalama, uzingatiaji, na jukwaa, na kiwango kinabadilika kwa makusudi lugha, usanifu, na jalada vinapohama, kikiweka usawa juu huku shirika likibadilika kuzunguka.

## Mawazo ya kujadili

- Folda zipi za ngazi ya juu zinapaswa kuwa za ulimwengu wote kweli kuvuka shirika lenu, na zipi ziwe za hiari?
- Mnazuiaje hazina zilizozalishwa kutoka kiolezo zisiteleze mbali nacho kwa muda?
- Mstari uko wapi kati ya daraja la tabaka lenye manufaa na taratibu za folda zilizohandisiwa kupita kiasi?
- Kiwango chenu cha muundo kinapaswa kutofautiana vipi, kama kinapaswa, kati ya monorepo na mbinu ya hazina nyingi?
- Mchakato sahihi wa vighairi ni upi kwa mradi ambao mahitaji yake halisi hayaingii kwenye mpangilio wa kawaida?
- Muundo wenu kiasi gani unaweza kukaguliwa kiotomatiki, na nini bado kinategemea mapitio ya binadamu?
- Nani anamiliki kiwango cha muundo na violezo vyake, na mabadiliko yanapendekezwa na kutolewa vipi?

## Mambo muhimu ya kukumbuka

- Panga kila hazina ili mhandisi yeyote aweze kupitia msimbo wowote kwa matarajio, akifuata kanuni ya mshangao mdogo kabisa.
- Pokea mpangilio thabiti wa ngazi ya juu (chanzo, majaribio, nyaraka, ujenzi, usambazaji, scripts, mifano, ubainishaji) na ufanye README iwe sehemu ya kuingilia.
- Weka usanidi wa kihariri na zana kwenye hazina (kama `.editorconfig`) ili kanuni ziwe hai, si zimeandikwa tu.
- Tekeleza muundo kwa jukwaa la ujenzi na violezo ili hazina mpya ziwe sahihi kwa chaguo-msingi.
- Kwa ukubwa, thamani iko katika usawa: tawala kiwango, simamia kuteleza, na ruhusu mikengeuko kwa kighairi kilichoandikwa tu.

## Marejeo na usomaji zaidi

- Robert C. Martin, *Clean Architecture: A Craftsman's Guide to Software Structure and Design*
- Steve McConnell, *Code Complete: A Practical Handbook of Software Construction*
- Andrew Hunt and David Thomas, *The Pragmatic Programmer*
- Titus Winters, Tom Manshreck, and Hyrum Wright (eds.), *Software Engineering at Google*
- Scott Chacon and Ben Straub, *Pro Git*
- EditorConfig project documentation (as a reference standard for editor configuration)
