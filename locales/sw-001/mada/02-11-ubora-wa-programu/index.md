# 2.11 Ubora wa programu

## Muhtasari na msukumo

[Ubora wa programu](https://en.wikipedia.org/wiki/Software_quality) ni jinsi mfumo unavyotimiza mahitaji yaliyotajwa na matarajio yanayofaa. Hilo linamaanisha zaidi ya kama unafanya kazi: linamaanisha kama mfumo unategemewa, ni salama, unadumishika, unatumika kwa urahisi, una utendaji mzuri, na unafaa kwa madhumuni yake kwa muda. Ubora ni mpana kuliko majaribio. Majaribio (sura ya 2.4) ni shughuli moja inayofichua kasoro. Ubora ni nidhamu nzima ya kujenga kitu sahihi kwa ufasaha, na ya kujua, kwa ushahidi, kwamba umefanya hivyo. Mfumo unaweza kupita kila jaribio na bado ukawa wa ubora duni ikiwa hauwezi kudumishwa, haufikiki, au haufai vizuri kwa mahitaji halisi ya watumiaji.

Katika timu kubwa, ubora hauwezi kuishi kichwani mwa mtu mmoja wala katika tabia za timu moja. Mamia ya wahandisi, bidhaa nyingi, na mifumo ya muda mrefu vinahitaji ufafanuzi wa pamoja wa ubora, michakato wazi ya kuuhakikisha, na vipimo vinavyokuambia kama unaimarika au unazorota. Bila hayo, "ubora" unakuwa hamu isiyo wazi inayopoteza kila mjadala dhidi ya tarehe ya mwisho, na kasoro hurundikana hadi mabadiliko yanakuwa ya polepole na ya hatari.

Katika mazingira ya mashirika makubwa na ya serikali dau hupanda zaidi. Mifumo inayodhibitiwa, muhimu kwa usalama, na inayowakabili raia lazima ionyeshe ubora, si kuudai tu: michakato iliyoandikwa, ushahidi unaofuatilika, na uthibitisho huru mara nyingi ni lazima. Ubora duni hubeba gharama ya moja kwa moja ya kifedha, kisheria, na ya sifa, na katika baadhi ya nyanja huweka watu hatarini. Nidhamu ya makusudi ya ubora, iliyojengwa kwa miundo, michakato, upimaji, na utamaduni, ndiyo inayogeuza ubora kutoka ajali kuwa matokeo yanayosimamiwa.

## Kanuni kuu

- Ubora ni kufaa kwa madhumuni pamoja na kulingana na mahitaji; fafanua yote mawili waziwazi.
- Ubora hujengwa ndani, hautiwi kwa majaribio; uthibitisho hupata kasoro, lakini kinga huziepuka.
- Tofautisha [uhakikisho wa ubora](https://en.wikipedia.org/wiki/Quality_assurance) (je, michakato yetu ni imara?) na [udhibiti wa ubora](https://en.wikipedia.org/wiki/Quality_control) (je, bidhaa hii ni nzuri?).
- Uthibitisho unauliza "je, tulijenga kwa usahihi?"; uthibitishaji wa kufaa unauliza "je, tulijenga kitu sahihi?"
- Pima ubora kwa seti ndogo ya vipimo vyenye maana; chukulia vipimo kama ishara, si malengo.
- Gharama ya kasoro hupanda kadiri inavyopatikana baadaye, kwa hiyo sogeza shughuli za ubora mapema.
- Ubora ni sifa ya shirika zima na utamaduni wake, si lango mwishoni.

## Mapendekezo

### Pokea kielelezo cha pamoja cha ubora kama ISO/IEC 25010

Mpe shirika lako msamiati wa pamoja wa ubora kwa kupokea kielelezo kinachotambuliwa cha ubora wa bidhaa. [ISO/IEC 25010](https://en.wikipedia.org/wiki/ISO/IEC_25010) hufafanua sifa ikiwemo ufaafu wa kiutendaji, ufanisi wa utendaji, upatanifu, uwezo wa kutumika, kutegemewa, usalama, uwezo wa kudumishwa, na uhamishikaji. Kitumie kufanya ubora kuwa madhubuti: kwa kila mfumo, amua sifa zipi zinajalisha zaidi na "nzuri vya kutosha" inamaanisha nini kwa kila moja. Sifa hizi za ubora wa bidhaa ndizo **sifa za ubora** zinazoendesha usanifu (sura ya 3.1). Ubora na usanifu ni mitazamo miwili ya wasiwasi mmoja, kwa hiyo uziache zishiriki orodha moja ya vipaumbele badala ya mbili zinazoshindana.

### Tenganisha uhakikisho wa ubora na udhibiti wa ubora

Chukulia uhakikisho wa ubora (QA) na udhibiti wa ubora (QC) kama shughuli tofauti lakini zinazokamilishana. QA inalenga mchakato na ni ya kinga: huboresha jinsi kazi inavyofanyika, kupitia viwango, mapitio, ufafanuzi wa kukamilika, na mafunzo, ili kasoro ziwe na uwezekano mdogo wa kutokea kwanza. QC inalenga bidhaa na ni ya kugundua: hukagua vitu halisi vya kazi, kama majaribio, [mapitio ya msimbo](https://en.wikipedia.org/wiki/Code_review), na ukaguzi, kunasa kasoro zilizoingia. Shirika lililokomaa huwekeza katika vyote viwili, lakini huegemea QA, kwa sababu kuzuia kasoro ni nafuu kuliko kuzipata na kuzirekebisha.

### Endesha michakato wazi ya usimamizi wa ubora wa programu

Fanya ubora kuwa mchakato unaosimamiwa, si tumaini la kimya. Kwa kazi muhimu, andika mpango wa ubora unaotaja sifa za ubora zinazolengwa, shughuli za uhakikisho na udhibiti, vigezo vya kukubalika, na nani anawajibika. Uufumbe katika mazoea ulionayo tayari: mapitio ya msimbo (sura ya 2.5) kama udhibiti na njia ya kushiriki maarifa, mkakati wa majaribio (sura ya 2.4) kama wavu wa usalama wa kiotomatiki, na [uchambuzi tuli](https://en.wikipedia.org/wiki/Static_program_analysis) kama ukaguzi endelevu. Pitia data ya ubora mara kwa mara na utende kwa mielekeo, badala ya kuitikia matukio tu.

### Fanya uthibitisho na uthibitishaji wa kufaa kama nidhamu mbili tofauti

Uthibitisho hukubali kwamba vitu vya kazi vinatimiza ubainishaji wake, ili ingizo sahihi kwa kila hatua zitoe pato sahihi, kupitia mapitio, uchambuzi tuli, na majaribio dhidi ya mahitaji. Uthibitishaji wa kufaa hukubali kwamba mfumo uliokamilika unatimiza mahitaji ya watumiaji na matumizi yaliyokusudiwa, kupitia majaribio ya watumiaji, majaribio ya kukubalika, majaribio ya awali, na maoni ya uwandani. Unahitaji vyote viwili. Mfumo unaweza kuwa sahihi dhidi ya ubainishaji wenye kasoro (umethibitishwa lakini haufai), au unaweza kushughulikia haja halisi na bado ukawa na kasoro (unafaa lakini haujathibitishwa). Katika mazingira yanayodhibitiwa, [uthibitisho na uthibitishaji](https://en.wikipedia.org/wiki/Verification_and_validation) huru (IV&V) na upande tofauti na wasanidi unaweza kuhitajika.

### Pima ubora kwa vipimo vyenye maana

Chagua seti ndogo ya vipimo vinavyoakisi matokeo ya ubora na vichocheo vyake, na uvifuatilie kwa muda. Vipimo vya manufaa ni pamoja na msongamano wa kasoro, kiwango cha kasoro zinazotoroka (kasoro zilizopatikana kwenye uzalishaji dhidi ya kabla ya toleo), muda wa wastani wa kugundua na kurekebisha, kiwango cha kushindwa kwa mabadiliko, ishara za afya ya msimbo kama ugumu na urudiaji, na ishara za uthibitishaji kama masuala yaliyoripotiwa na watumiaji na ulinganifu wa ufikivu. Epuka vipimo vya majivuno na vinavyoweza kuchezewa: kipimo kinachogeuka lengo huacha kupima uhalisia. Oanisha namba na ishara za kiubora kutoka mapitio na maoni ya watumiaji.

### Tambulisha na simamia kasoro kwa utaratibu

Chukulia kasoro kama data, si moto wa kuzimwa tu. Zipange kwa ukali, aina, na chanzo cha msingi. Zifuatilie kutoka ugunduzi hadi suluhisho. Tafuta mifumo ili uzuie kujirudia. Tumia mbinu kama [uchambuzi wa chanzo cha msingi](https://en.wikipedia.org/wiki/Root_cause_analysis) na uainishaji wa kasoro kutofautisha makosa ya mara moja na udhaifu wa kimfumo. Rudisha ulichojifunza kwenye QA, kupitia viwango vilivyosasishwa, majaribio yaliyoongezwa, na mapitio yaliyoboreshwa, ili aina ileile ya kasoro isirudi. Kasoro iliyorekebishwa bila kuelewa chanzo chake ni kasoro uliyoikaribisha tena.

### Simamia gharama ya ubora kwa makusudi

Elewa uchumi wa ubora kupitia kategoria za kawaida: gharama za kinga (mafunzo, viwango, usanifu mzuri, zana), gharama za tathmini (mapitio, majaribio, ukaguzi), na gharama za kushindwa (kurudia kazi ndani kabla ya toleo, pamoja na kushindwa kwa nje kunakopatikana na watumiaji, kunakogharimu zaidi sana). Hamisha uwekezaji wako kuelekea kinga na tathmini ya mapema, kwa sababu kila dola huko huepusha dola nyingi za gharama ya kushindwa baadaye. Fanya gharama hizi zionekane, ili "hatuna muda wa ubora" ionekane kwa ilivyo: uchaguzi wa kutumia zaidi kwenye kushindwa badala yake.

### Jenga utamaduni wa ubora

Fanya ubora kuwa wajibu wa kila mtu, unaomilikiwa na timu zinazojenga programu, badala ya kukabidhiwa idara ya QA ya chini ya mkondo inayoukagua mwishoni. Viongozi wanapaswa kutuza matokeo ya ubora, kufanya iwe salama kuripoti kasoro na karibu-makosa, na kuchukulia data ya ubora kama zana ya kujifunza badala ya fimbo. Mtazamo usio wa lawama kwa kasoro huleta matatizo wazi mapema. Ule wa lawama huyaficha hadi yawe ghali.

## Mabadilishano: faida na hasara

| Mazoea / chaguo | Faida | Hasara |
|---|---|---|
| Kielelezo rasmi cha ubora (ISO 25010) | Msamiati wa pamoja; vipaumbele wazi | Mzigo ukitumika kwa ukaidi |
| Uhakikisho wa ubora mzito (kinga) | Kasoro chache; gharama ya jumla ndogo | Uwekezaji wa awali; malipo hujitokeza polepole |
| Udhibiti wa ubora mzito (ukaguzi) | Hunasa kasoro zinazopenya | Ghali; hupata kasoro kuchelewa |
| IV&V huru | Uhakikisho wa juu; wa kimalengo | Ghali; polepole; unaweza kuhisi wa kupingana |
| Vipimo vingi vya ubora | Mwonekano; onyo la mapema | Hatari ya kuchezewa; mzigo wa upimaji |
| Timu maalumu ya QA | Umakini na utaalamu | Inaweza kuwaondolea wasanidi wajibu |
| Ubora unaomilikiwa na timu | Umiliki; maoni ya haraka | Inahitaji nidhamu na ujuzi kila mahali |

Mabadilishano ya msingi ni uwekezaji dhidi ya uhakikisho, yakiumbwa na muda. Kinga hugharimu fedha sasa kuepuka gharama kubwa za kushindwa baadaye. Kwa hiyo kiwango sahihi cha kiuchumi cha ubora si cha juu kabisa; ni nukta ambapo gharama ya pembeni ya uhakikisho zaidi inalingana na gharama ya kushindwa inayoiepusha. Nukta hiyo iko juu kwa mifumo muhimu kwa usalama na chini kwa zana za ndani zenye dau la chini. Mvutano mwingine unaojirudia ni umiliki. Vikundi vya kati vya QA hujenga utaalamu lakini vinaweza kuwaacha wasanidi waondoe wajibu. Ubora unaomilikiwa na timu hujenga umiliki lakini unadai ujuzi na nidhamu kila mahali.

## Maswali ya kujadili na timu yako

1. **Aina ileile ya kasoro inapojitokeza mara mbili, tunafanya uchambuzi wa chanzo cha msingi, au tunairekebisha tena tu?** Kasoro iliyorekebishwa bila kuelewa chanzo chake ni kasoro uliyoikaribisha tena, na katika timu kubwa chanzo kilekile kinaweza kujitokeza kuvuka huduma nyingi kabla mtu yeyote hajaunganisha nukta. Kuchukulia kasoro kama data (iliyopangwa kwa ukali, aina, na chanzo, kisha kuchimbwa kwa mifumo) ndiko kunakotenganisha timu inayozidi kutegemewa na ile inayobaki na shughuli ya kurekebisha kosa lilelile. Leta kifuatiliaji chenu cha kasoro kwenye mkutano na utafute saini zinazojirudia: matukio mangapi ya hivi karibuni yanashiriki chanzo ambacho hamkukishughulikia kimfumo? Jibu linapaswa kulisha kinga, kwa hiyo chanzo kinachojirudia kinaendesha kiwango kilichosasishwa, msaidizi mpya wa pamoja, jaribio lililoongezwa, au orodha hakiki bora ya mapitio, kwa sababu hivyo ndivyo marekebisho sehemu moja yanavyozuia darasa zima lisirudi.

2. **Je, ni salama kwenye timu yetu kuripoti kasoro au karibu-kosa, na nini kinamtokea mtu anayelileta?** Ubora ni sifa ya utamaduni, na mtazamo usio wa lawama huleta matatizo wazi mapema huku wa lawama ukiyaficha hadi yawe ghali, ambayo katika mfumo unaodhibitiwa au unaowakabili raia yanaweza kumaanisha kushindwa hadharani au adhabu. Hili ni muhimu zaidi kwa ukubwa, ambapo mhandisi aliye karibu zaidi na hatari mara nyingi ni mdogo kwa cheo na kishawishi cha kunyamaza ni kikubwa. Leta ishara za uaminifu: je, karibu-makosa yanaandikwa na kujadiliwa, au yanatoweka? Je, uchambuzi wa baada ya tukio unataja sababu au unataja watu? Hatua ni kufanya data ya ubora iwe zana ya kujifunza badala ya fimbo, kutuza watu wanaofichua matatizo, na kuendesha uchambuzi wa baada ya tukio usio wa lawama, kwa sababu huwezi kuzuia kile timu yako inachoogopa kuripoti.

3. **Je, uthibitishaji wa kufaa unaweza kusimamisha toleo kweli, na nani anashikilia mamlaka hayo tarehe ya mwisho inapokaribia?** Uthibitisho (je, tulijenga kwa usahihi?) na uthibitishaji wa kufaa (je, tulijenga kitu sahihi?) ni nidhamu tofauti, na uthibitishaji wa kufaa una meno tu ikiwa ukaguzi wa ufikivu ulioshindwa, jaribio la kukubalika lililoshindwa, au utafiti wa watumiaji unaotisha vinaweza kuzuia kusafirisha kweli. Katika mazingira ya mashirika makubwa na ya serikali hili mara nyingi ni lazima, wakati mwingine kupitia uthibitisho na uthibitishaji huru na upande tofauti na wasanidi, na "tulisafirisha hata hivyo" si jibu ambalo chombo cha usimamizi kinakubali. Leta matoleo yenu machache ya mwisho: je, ishara yoyote ya ubora iliwahi kusimamisha moja, au lango daima hulegea mbele ya tarehe? Uthibitishaji wa kufaa ukiwa haujawahi kuzuia toleo, ni mapambo, na suluhisho ni kuandika vigezo vya kukubalika kwenye mpango wa ubora mapema, kutaja nani anamiliki uamuzi wa kwenda/kutokwenda, na kuupa uamuzi huo mamlaka halisi huru kutoka shinikizo la utoaji.

4. **Je, tunajua gharama yetu ya ubora duni kweli, na je, tunahamisha matumizi kwa makusudi kutoka kushindwa kuelekea kinga?** Gharama ya ubora duni (COPQ) ni fedha zinazopotea kwa kurudia kazi ndani, matukio ya uzalishaji, marekebisho ya dharura, mzigo wa msaada, watumiaji waliopotea, na adhabu, na karibu daima ni kubwa kuliko matumizi yanayoonekana kwenye mapitio na majaribio. Katika timu kubwa gharama za kushindwa zimetawanyika kuvuka njia za matukio, foleni za msaada, na kurudia kazi ambako hakuna anayeliandika kama kurudia kazi, kwa hiyo zinabaki zisizoonekana hadi mtu azijumlishe. Mvutano ni kwamba kinga hugharimu fedha sasa, katika mzunguko wa bajeti, kuepuka gharama za kushindwa zinazotua baadaye na kutua kwenye bajeti ya mtu mwingine, jambo linalofanya biashara hii iwe rahisi kuahirisha milele. Leta takwimu halisi: idadi na gharama ya matukio, saa za kurudia kazi, kiwango cha kasoro zilizotoroka, na mgawanyo wa sasa wa matumizi kuvuka kinga, tathmini, na kushindwa, kisha amua kama mchanganyiko unapaswa kuhamia mapema. Kwa mifumo ya mashirika makubwa na ya serikali, ambapo gharama nyingi za maisha hutua baada ya toleo la kwanza, weka COPQ mbele ya watu wanaoshikilia bajeti, kwa sababu namba ambayo chombo cha usimamizi kinaweza kuiona ni ngumu zaidi kubadilishwa kuliko ombi lisilo wazi la "ubora".

5. **Ni vipimo vipi vya ubora vyetu vimegeuka kimyakimya kuwa malengo, na vinaendesha tabia gani sasa?** Kipimo kinachogeuka lengo huacha kupima uhalisia: fukuza asilimia ya ufikiaji wa majaribio na unapata majaribio yaliyoandikwa kusogeza namba, si majaribio yanayonasa kasoro. Kwa ukubwa hili ni hatari, kwa sababu dashibodi ya kichwa cha habari inayoshirikiwa na timu kadhaa huweka vichocheo kwa zote, na kipimo kinachoweza kuchezewa huenea udanganyifu kila mahali kwa wakati mmoja. Jambo linaloshindana ni kwamba bado unahitaji upimaji, kwa hiyo jibu mara chache ni "acha kipimo" bali "kioanishe na ishara ya kukabili na kisome pamoja na ushahidi wa kiubora kutoka mapitio na watumiaji". Leta seti yenu ya vipimo ya sasa na, kwa kila kimoja, uliza mtu aliye chini ya shinikizo angefanya nini kukisogeza bila kuboresha ubora, na kama mmeona hilo likitokea. Katika mazingira yanayodhibitiwa na yanayowakabili raia, kuwa mwangalifu hasa na vipimo vya ulinganifu vinavyoonekana kijani huku uthibitishaji wa kufaa msingi (ufikivu, matokeo halisi ya watumiaji) haukujaribiwa kweli, kwa kuwa mkaguzi hatimaye atajaribu uhalisia nyuma ya namba.

6. **Nani anamiliki ubora hapa: timu zinazoandika msimbo, au kikundi tofauti mwishoni, na tunawekeza rasilimali kwa kipi kweli?** Umiliki unaumba kila kitu chini ya mkondo, kwa sababu kikundi cha QA cha chini ya mkondo huwaruhusu wasanidi kuondoa wajibu wa msimbo wanaouandika, huku ubora unaomilikiwa na timu ukijenga umiliki kwa gharama ya kudai ujuzi na nidhamu kila timu. Katika timu kubwa hili si lazima liwe moja au jingine: mfumo endelevu kwa kawaida ni timu zinazomiliki ubora kupitia mapitio ya msimbo na majaribio ya kiotomatiki, zikisaidiwa na kikundi kidogo cha kati kinachodumisha viwango, kuendesha uhakikisho wa ubora kama uboreshaji wa mchakato, na kufundisha, badala ya kukagua ubora mwishoni. Leta ramani ya uaminifu ya mahali kazi ya ubora inapofanyika sasa, nani anawajibika kasoro inapotoroka, na mahali bajeti na idadi ya wafanyakazi vilipo kweli dhidi ya mahali maneno yanasema ubora unaishi. Kwa mashirika makubwa na ya serikali, ongeza sharti la uthibitisho na uthibitishaji huru: mifumo mingine ya uhakikisho inaamuru upande tofauti, kwa hiyo amua kwa makusudi udhibiti upi ni wa timu za utoaji na upi lazima ubaki huru kutimiza ukaguzi.

## Mtazamo wa sekta

**Kampuni changa.** Kasi ni muhimu kuliko taratibu, kwa hiyo taja sifa mbili au tatu za ubora zinazolinda bidhaa yako kweli, kwa kawaida kutegemewa na uwezo wa kudumishwa, na uache ung'arishaji usubiri. Miliki ubora katika timu nzima kwa mapitio ya msimbo na safu ya wastani ya majaribio ya kiotomatiki badala ya kuanzisha kikundi tofauti cha QA usichoweza kukiajiri. Aina ileile ya hitilafu ikionekana mara mbili, tumia dakika ishirini kwa chanzo cha msingi na uongeze msaidizi mmoja wa pamoja pamoja na jaribio, ili kinga ibaki nafuu na kiwango chako cha kushindwa kwa mabadiliko kibaki chini unapoendelea haraka.

**Biashara ndogo.** Bila mtaalamu maalumu wa ubora na bajeti finyu, tegemea ubora uliojengwa ndani ya zana na majukwaa unayonunua badala ya mchakato unaopaswa kuuendesha. Unapochagua programu, chukulia ushahidi wa ubora wa muuzaji kama sehemu ya ununuzi: msimamo wa usalama, ufikivu, kuitikia kwa msaada, na mara ngapi matoleo yao yanavunja mambo. Fuatilia ishara chache za bei nafuu, za uaminifu (matukio ya uzalishaji, masuala yaliyoripotiwa na wateja, muda wa kurekebisha) badala ya programu ya vipimo ya kina usiyo na mtu wa kuidumisha.

**Biashara kubwa.** Kazi ni uthabiti kuvuka timu nyingi: pokea kielelezo cha pamoja cha ubora kama ISO/IEC 25010, tenganisha uhakikisho wa ubora (mchakato) na udhibiti wa ubora (bidhaa), na uendeshe mapitio ya gharama ya ubora yanayohamisha matumizi kuelekea kinga. Weka ubora ukimilikiwa na timu za utoaji, ukisaidiwa na kikundi kidogo cha kati kinachodumisha viwango na dashibodi za kiwango cha kasoro zinazotoroka, kiwango cha kushindwa kwa mabadiliko, na mielekeo ya afya ya msimbo. Sawazisha msamiati na malango ili vikundi viache kuvumbua upya mazoea ya ubora, huku ukiacha nafasi kwa timu kutimiza viwango hivyo kwa njia zao.

**Serikali.** Ununuzi, uwazi, na uwajibikaji wa umma huweka mfumo, kwa hiyo andika mahitaji ya ubora kwenye mikataba na uhitaji ushahidi wa ubora ulioandikwa, unaofuatilika badala ya madai. Tarajia uthibitisho na uthibitishaji huru na upande tofauti na wasanidi, ulinganifu wa lazima wa ufikivu, na rekodi za kasoro zenye ukali na chanzo cha msingi zikihifadhiwa kama sehemu ya njia ya ukaguzi. Ripoti takwimu za gharama ya ubora duni (kurudia kazi, rufaa, kushindwa kwa huduma) kwa vyombo vya usimamizi, na upe uthibitishaji wa kufaa mamlaka halisi ya kuzuia toleo ambalo lingewaangusha raia wanaolitegemea.

## Mifano

**Kampuni changa.** Kampuni changa ya watu watano inaamua kwamba kwa bidhaa yake ya awali, kutegemewa na uwezo wa kudumishwa ndizo sifa za ubora zinazojalisha, na inaacha ung'arishaji kamili wa pikseli usubiri. Ubora unamilikiwa na timu nzima: mapitio ya msimbo na safu ya wastani ya majaribio ya kiotomatiki ndio udhibiti, na hakuna kikundi tofauti cha QA cha kukabidhi kasoro. Aina ileile ya hitilafu inapojitokeza mara mbili, wanatumia dakika ishirini kwa kuangalia haraka chanzo cha msingi na kuongeza msaidizi mmoja wa pamoja pamoja na jaribio, kwa hiyo inaacha kujirudia badala ya kurekebishwa kwa mkono kila mara. Tabia hiyo ndogo ya kinga inaweka kiwango chao cha kushindwa kwa mabadiliko chini wanapoendelea haraka.

**Biashara kubwa.** Kampuni kubwa ya huduma za kifedha inapokea ISO/IEC 25010 kama msamiati wake wa ubora na, kwa kila bidhaa, inarekodi viwango lengwa vya kutegemewa, usalama, na uwezo wa kudumishwa. Timu zinamiliki ubora: mapitio ya msimbo na majaribio ya kiotomatiki ni udhibiti kwenye bomba, huku kikundi kidogo cha kati kinaendesha QA kwa kudumisha viwango na kufundisha. Dashibodi ya ubora inafuatilia kiwango cha kasoro zinazotoroka, kiwango cha kushindwa kwa mabadiliko, na mielekeo ya afya ya msimbo. Kasoro zinapangwa na kuchambuliwa kwa chanzo, na vyanzo vinavyojirudia vinaendesha masasisho ya maktaba za pamoja na orodha hakiki. Uongozi hupitia data ya gharama ya ubora kila robo mwaka na umehamisha matumizi kuelekea kinga, ukipunguza matukio ya uzalishaji na gharama ya kuyarekebisha.

**Serikali.** Wakala wa kitaifa unaotoa jukwaa la manufaa linalowakabili raia unafanya kazi chini ya mfumo wa uhakikisho unaohitaji ushahidi wa ubora ulioandikwa. Unaendesha mchakato rasmi wa usimamizi wa ubora wenye mpango wa ubora kwa kila toleo, pamoja na uthibitisho na uthibitishaji huru na timu tofauti na wasanidi. Uthibitisho unakagua kila kitu cha kazi dhidi ya mahitaji yanayofuatiliwa hadi sera. Uthibitishaji wa kufaa unajumuisha majaribio ya ulinganifu wa ufikivu na utafiti wa watumiaji na raia halisi, na yote mawili yanaweza kuzuia toleo. Kasoro zinafuatiliwa na ukali na chanzo cha msingi kama sehemu ya njia ya ukaguzi, na takwimu za gharama ya ubora duni (kurudia kazi, rufaa, na kushindwa kwa huduma) zinakwenda kwa vyombo vya usimamizi kuhalalisha uwekezaji endelevu katika kinga.

## Kesi ya biashara: sababu, ROI, na TCO

Mapato ya ubora ni jumla ya gharama ya umiliki ya chini na kasi thabiti ya utoaji. Gharama ya ubora ina pande mbili. Matumizi mazuri, kinga na tathmini, yanaonekana na yanadhibitika: usanifu, viwango, mapitio, majaribio, na zana. Gharama ya ubora duni (COPQ) ni kubwa zaidi lakini mara nyingi imefichika: kurudia kazi ndani, matukio ya uzalishaji, marekebisho ya dharura, msaada kwa wateja, watumiaji waliopotea, adhabu za udhibiti, na uharibifu wa sifa. Tafiti zilizoanza na "Quality Is Free" ya Crosby mara kwa mara zimegundua kwamba jumla ya gharama ya ubora duni inazidi sana gharama ya kuuzuia, na kwamba kasoro huwa ghali zaidi kadiri unavyozinasa baadaye: suala lililopatikana kwenye usanifu linagharimu sehemu ndogo ya suala lilelile lililopatikana kwenye uzalishaji.

Kwa uongozi, hoja si "tumia zaidi kwenye ubora." Ni "tumia mapema ili utumie kidogo kwa jumla." Pima COPQ kutoka data yako mwenyewe (idadi na gharama ya matukio, saa za kurudia kazi, kiwango cha kasoro zilizotoroka) na uonyeshe jinsi kinga na tathmini ya mapema inavyoishusha. Unganisha ubora na matokeo ya biashara: kutegemewa huhifadhi wateja, uwezo wa kudumishwa huweka mabadiliko ya baadaye kuwa nafuu, na usalama na ufikivu vinakuweka mbali na matatizo ya kisheria. Katika mifumo ya mashirika makubwa na ya serikali ya muda mrefu, ambapo gharama nyingi hutua baada ya toleo la kwanza, vipimo vya uwezo wa kudumishwa na kutegemewa vya ubora vinatawala gharama ya maisha. Hilo hufanya uwekezaji wa mapema wa ubora kuwa mojawapo ya maamuzi yenye kiegemeo cha juu zaidi unayoweza kufanya.

## Mifumo mibaya na mitego

- **Ubora kama lango la mwisho:** kukagua ubora mwishoni badala ya kuujenga ndani, kwa hiyo kasoro zinapatikana zikiwa ghali zaidi.
- **Kuchanganya majaribio na ubora:** kudhani kwamba majaribio yanayopita yanamaanisha ubora wa juu, ukipuuza uwezo wa kudumishwa, uwezo wa kutumika, na kufaa kwa madhumuni.
- **QA kama kisiwa tofauti:** timu ya chini ya mkondo "inayomiliki ubora," ikiwaruhusu wasanidi kuondoa wajibu wa msimbo wanaouandika.
- **Maigizo ya vipimo:** kufukuza asilimia za ufikiaji au hesabu za kasoro kama malengo, kunakoalika kuchezea na kuficha ubora halisi.
- **Uthibitisho bila uthibitishaji wa kufaa:** kujenga ubainishaji kwa usahihi bila kukagua kamwe kwamba ubainishaji unatimiza mahitaji halisi.
- **Hakuna uchambuzi wa chanzo cha msingi:** kurekebisha kasoro moja moja bila kushughulikia chanzo cha kimfumo, kwa hiyo darasa lilelile hujirudia.
- **Kupuuza gharama ya ubora duni:** kuchukulia ubora kama gharama tupu kwa sababu gharama za kushindwa zimefichika na hazipimwi.

## Kielelezo cha ukomavu

**Ngazi ya 1 (Kuanzisha).** Ubora haujafafanuliwa na ni wa papo hapo. Unategemea bidii ya mtu binafsi, unakaguliwa hasa kwa majaribio ya mkono mwishoni, na kasoro zinashughulikiwa kwa kuitikia zinapojitokeza. Hakuna kielelezo cha pamoja, hakuna vipimo, na hakuna mstari kati ya uhakikisho na udhibiti.

**Ngazi ya 2 (Kuendeleza).** Mazoea ya msingi yanatokea: mapitio ya msimbo, majaribio ya kiotomatiki, na kifuatiliaji cha kasoro. Baadhi ya data ya ubora inakusanywa, lakini kwa kutofautiana, na kila timu inafanya kwa njia yake. Ubora bado unaonekana hasa kama majaribio, kinga ni ndogo, uthibitisho unafanyika, na uthibitishaji wa kufaa si rasmi.

**Ngazi ya 3 (Kusawazisha).** Shirika linapokea kielelezo cha pamoja cha ubora (kama ISO/IEC 25010), linatenganisha QA na QC, na kuendesha michakato ya usimamizi wa ubora yenye mipango ya ubora na vigezo vya kukubalika, vilivyoandikwa na kutumika kwa uthabiti kuvuka timu. Uthibitisho na uthibitishaji wa kufaa ni tofauti na wa makusudi, na kasoro zinapangwa na kuchambuliwa kwa chanzo kwa mpango uliokubaliwa.

**Ngazi ya 4 (Kusimamia).** Ubora unapimwa na kudhibitiwa dhidi ya vipimo vya msingi. Seti ndogo ya vipimo vyenye maana inafuatiliwa kwa muda (msongamano wa kasoro, kiwango cha kasoro zinazotoroka, muda wa wastani wa kugundua na kurekebisha, kiwango cha kushindwa kwa mabadiliko, na ishara za afya ya msimbo kama ugumu na urudiaji), na gharama ya ubora inapimwa kuvuka kinga, tathmini, na kushindwa. Malango ya kukubalika na ubora yanatekelezwa kwa ushahidi badala ya maoni, mielekeo inapitiwa kwa ratiba thabiti, na uthibitishaji wa kufaa unaweza kuzuia toleo kweli.

**Ngazi ya 5 (Kuratibu).** Ubora ni nidhamu inayoboreshwa kila wakati, inayomilikiwa kiutamaduni, iliyounganishwa na upangaji wa biashara na hatari. Kinga ndiyo msisitizo, data ya gharama ya ubora inaongoza uwekezaji unakoenda, na matokeo ya chanzo cha msingi huzuia kujirudia kwa utaratibu. Timu zinamiliki ubora mwanzo hadi mwisho, vipimo vinalisha uboreshaji endelevu, na shirika hurekebisha mazoea yake ya ubora bidhaa, hatari, na kanuni zinapohama. Hili linaoana na ngazi za juu za vielelezo vya ukomavu katika sura ya 10.8.

## Mawazo ya kujadili

- Ni sifa zipi za ubora za ISO/IEC 25010 zinajalisha zaidi kwa mifumo yenu, na "nzuri vya kutosha" ni nini kwa kila moja?
- Shirika lenu liko wapi kwenye mchanganyiko wa matumizi ya kinga-tathmini-kushindwa, na je, linapaswa kuhama?
- Je, mnatofautisha uthibitisho na uthibitishaji wa kufaa kivitendo, au mnaunganisha vyote viwili kuwa "majaribio"?
- Je, ubora unamilikiwa na timu zinazojenga programu, au umekabidhiwa kikundi tofauti, na nini kingebadilika mkiuhamisha?
- Gharama yenu halisi ya ubora duni ni ipi, na je, mngeweza kuipima vizuri vya kutosha kujenga kesi ya biashara?
- Ni vipimo vipi vya ubora vyenu ni ishara halisi, na vipi vimegeuka malengo yanayoweza kuchezewa?

## Mambo muhimu ya kukumbuka

- Ubora ni mpana kuliko majaribio: ni kufaa kwa madhumuni pamoja na ulinganifu, kuvuka sifa kama kutegemewa, usalama, na uwezo wa kudumishwa.
- Tumia kielelezo cha pamoja cha ubora (ISO/IEC 25010) ili sifa za ubora ziwe wazi na zioane na usanifu (sura ya 3.1).
- Tenganisha uhakikisho wa ubora (zuia, mchakato) na udhibiti wa ubora (gundua, bidhaa), na uegemee kinga.
- Fanya uthibitisho (tulijenga kwa usahihi) na uthibitishaji wa kufaa (tulijenga kitu sahihi) kama nidhamu tofauti.
- Pima ubora kwa vipimo vichache vyenye maana, na ubainishe kasoro kwa ukali na chanzo cha msingi kuzuia kujirudia.
- Simamia gharama ya ubora: kinga na tathmini ya mapema ni nafuu zaidi sana kuliko kushindwa, hasa katika mifumo ya muda mrefu.
- Jenga utamaduni wa ubora usio wa lawama ambapo timu zinamiliki ubora, zikisaidiwa na mapitio ya msimbo (sura ya 2.5) na mkakati wa majaribio (sura ya 2.4).

## Marejeo na usomaji zaidi

- IEEE Computer Society, *SWEBOK Guide (Guide to the Software Engineering Body of Knowledge)*, Software Quality knowledge area.
- ISO/IEC 25010, *Systems and software engineering: Systems and software Quality Requirements and Evaluation (SQuaRE): System and software quality models*.
- ISO/IEC 25000 series (SQuaRE), *Software product quality requirements and evaluation*.
- Philip B. Crosby, *Quality Is Free: The Art of Making Quality Certain*.
- W. Edwards Deming, *Out of the Crisis*.
- Capers Jones and Olivier Bonsignour, *The Economics of Software Quality*.
- Gerald Weinberg, *Quality Software Management*.
- ISO/IEC/IEEE 12207, *Systems and software engineering: Software life cycle processes* (quality assurance and V&V process context).
