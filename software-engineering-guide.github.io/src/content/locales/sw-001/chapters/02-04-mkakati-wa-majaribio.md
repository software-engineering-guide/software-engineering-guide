# 2.4 Mkakati wa majaribio

## Muhtasari na msukumo

Mkakati wa [majaribio](https://en.wikipedia.org/wiki/Software_testing) ni seti ya chaguo za makusudi kuhusu nini cha kujaribu, katika ngazi gani, kwa kiotomatiki kiasi gani, na kwa kujiamini kiasi gani, ili timu yako ibadilishe msimbo haraka bila kuuvunja. Majaribio ndiyo yanayoruhusu shirika kubwa kutoa mara kwa mara na kwa usalama. Yanaweka tabia inayotarajiwa katika msimbo, hunasa kurudi nyuma, na kuwapa wahandisi kujiamini kwa [kurekebisha muundo](https://en.wikipedia.org/wiki/Code_refactoring). Bila mkakati thabiti, majaribio huelekea njia mbili mbaya: kutokuwepo (uendelezaji wa polepole unaoendeshwa na hofu) au kuvimba (maelfu ya majaribio ya polepole, yasiyo thabiti ambayo hakuna anayeyaamini).

Kwa timu kubwa, mkakati ni muhimu kuliko jaribio lolote moja. Mamia ya wahandisi wanaofanya kazi kwenye msimbo wa pamoja wanahitaji wavu wa usalama wa haraka, wa kuaminika. Bila huo, kila badiliko ni hatari na kila toleo linakuwa mateso ya mkono. Majaribio pia hufanya kazi kama nyaraka zinazotekelezeka za tabia iliyokusudiwa, jambo lisilo na bei waandishi wa awali wanapohama. Mkakati huamua kama seti yako ya majaribio ni mali inayoharakisha utoaji au dhima inayoupunguza.

Katika mazingira ya mashirika makubwa na ya serikali, majaribio hubeba uzito wa ziada. Kanuni zinaweza kuhitaji ufikiaji ulioandikwa wa majaribio na ushahidi. Mifumo muhimu kwa usalama na inayowakabili raia inadai uhakikisho wa juu. Majaribio ya ufikivu na usalama yanaweza kuhitajika kisheria. Kwa hiyo mkakati lazima usawazishe kasi, kujiamini, gharama, na uzingatiaji, na uchukulie ufikiaji kama ishara, si lengo la kudanganywa.

## Kanuni kuu

- Jaribu ili upate kujiamini kubadilisha, si kufikia nambari.
- Pendelea majaribio ya haraka, ya kuaminika, yaliyotengwa. Majaribio ya polepole au yasiyo thabiti humomonyoa uaminifu unaofanya seti iwe na manufaa.
- Sukuma majaribio hadi ngazi ya chini kabisa inayotoa kujiamini halisi, na uhifadhi majaribio ya polepole, mapana kwa hatari ya kweli ya uunganishaji.
- Jaribio lisilo thabiti ni jaribio lililovunjika. Chukulia kutokuwa thabiti kama kasoro ya daraja la kwanza.
- Ufikiaji ni ishara, si lengo. Ufikiaji wa juu wa msimbo mdogo hauthibitishi mengi.
- Jaribu tabia na mikataba, si undani wa utekelezaji, ili majaribio yako yaokoke urekebishaji.
- Fanya majaribio yasiyo ya kiutendaji (ufikivu, utendaji, usalama) kuwa sehemu ya mkakati, si wazo la baadaye.

## Mapendekezo

### Tumia piramidi ya majaribio kama chaguo-msingi, na ujue ukosoaji wake

Chagua majaribio mengi ya haraka ya [kitengo](https://en.wikipedia.org/wiki/Unit_testing), machache ya [uunganishaji](https://en.wikipedia.org/wiki/Integration_testing), na idadi ndogo ya majaribio ya mwanzo-hadi-mwisho, kwa sababu gharama na udhaifu hupanda wigo unapokua. Jua pia ukosoaji: umbo linapaswa kufuata usanifu wako, si itikadi. Mfumo wenye huduma nyingi unaweza kuhitaji safu kubwa ya uunganishaji ("testing trophy"), na lengo halisi ni kujiamini kwa kila kitengo cha gharama na kasi, si umbo fulani. Chochote ufanyacho, epuka piramidi iliyogeuzwa ya majaribio ya mwanzo-hadi-mwisho ya polepole kwa wingi.

### Pokea TDD, BDD, na uendelezaji unaoendeshwa na ubainishaji pale unaposaidia

Tumia [uendelezaji unaoendeshwa na majaribio](https://en.wikipedia.org/wiki/Test-driven_development) (TDD) kuendesha usanifu na kuhakikisha uwezo wa kujaribu, hasa kwa mantiki tata. Ni nidhamu ya usanifu kama ilivyo ya majaribio. Tumia [uendelezaji unaoendeshwa na tabia](https://en.wikipedia.org/wiki/Behavior-driven_development) (BDD) kueleza majaribio kwa lugha ya eneo unayoshirikiana na wadau, jambo lenye thamani kwa vigezo vya kukubalika katika mazingira yanayodhibitiwa au yenye mahitaji mengi. Uendelezaji unaoendeshwa na ubainishaji unaenda hatua moja zaidi: unachukulia ubainishaji unaotekelezeka (tabia iliyokubaliwa, iliyoelezwa kama mifano) kama chanzo kimoja cha ukweli kinachoongoza utekelezaji na kuuthibitisha. Hung'aa pale mahitaji lazima yafuatiliwe hadi ushahidi wa kukubalika, kama katika programu za serikali na zinazodhibitiwa. Linalohusiana na vyote vitatu ni **[majaribio ya kuhamia kushoto](https://en.wikipedia.org/wiki/Shift-left_testing)**: kuhamisha uthibitisho mapema iwezekanavyo katika mzunguko wa maisha, kuandika majaribio pamoja au kabla ya msimbo na kuyaendesha mfululizo, ili unase kasoro zikiwa nafuu zaidi kurekebisha, badala ya katika awamu za majaribio za marehemu au uzalishaji. Hakuna kati ya hivi cha lazima kila mahali. Vitumie pale vinapoongeza uwazi.

### Tumia mbinu za hali ya juu kwa msimbo wenye thamani ya juu

Tumia majaribio yanayotegemea sifa kuthibitisha vigeu visivyobadilika kuvuka ingizo nyingi zinazozalishwa, kunasa kesi za pembeni ambazo majaribio ya mifano hukosa. Tumia [majaribio ya fuzz](https://en.wikipedia.org/wiki/Fuzzing) kwenye vichanganuzi na mipaka ya ingizo lisiloaminika kupata kuporomoka na kasoro za usalama. Tumia [majaribio ya mabadiliko](https://en.wikipedia.org/wiki/Mutation_testing) kupima kama majaribio yako yanagundua kweli kasoro zilizoingizwa, ishara bora zaidi ya ubora kuliko ufikiaji ghafi. Tumia majaribio ya picha kwa busara kwa pato lililoratibiwa, na jihadhari na mtego wa kuidhinisha upya picha kwa upofu.

### Simamia data ya majaribio na utumie data bandia

Fanya majaribio yawe ya kuamuliwa kwa data ya majaribio iliyodhibitiwa, iliyotengwa, na uepuke vifaa vya pamoja vinavyobadilika vinavyounganisha majaribio. Zalisha [data bandia](https://en.wikipedia.org/wiki/Synthetic_data) inayoakisi sifa za uzalishaji bila kufichua taarifa halisi binafsi, muhimu pale kanuni za faragha zinapokataza kutumia data ya uzalishaji katika mazingira ya majaribio. Toa viwanda au wajenzi ili kila jaribio liunde hasa data linayohitaji.

### Chukulia majaribio yasiyo thabiti kama kasoro

Gundua kutokuwa thabiti kiotomatiki, hamisha majaribio yasiyo thabiti nje ya njia inayozuia, na uyarekebishe au uyafute kwa tarehe ya mwisho. Seti inayoshindwa bila mpangilio huwafunza wahandisi kupuuza kushindwa, jambo linaloharibu thamani yake yote. Fuatilia viwango vya kutokuwa thabiti na ufanye kuaminika kuwe kipimo wazi cha ubora wa seti yenyewe.

### Tumia ufikiaji kama ishara, na uongeze majaribio yasiyo ya kiutendaji

Pima ufikiaji kupata maeneo yasiyojaribiwa, lakini usiugeuze kuwa lengo gumu linalokaribisha udanganyifu kwa majaribio yasiyo na madai. Ukamilishe na majaribio ya mabadiliko kwa kina. Jenga majaribio ya ufikivu (ukaguzi wa kiotomatiki pamoja na ukaguzi wa mkono), majaribio ya utendaji (msingi wa mzigo na ucheleweshaji pamoja na utambuzi wa kurudi nyuma), na majaribio ya usalama (uchanganuzi wa utegemezi, [uchambuzi tuli](https://en.wikipedia.org/wiki/Static_program_analysis), na majaribio ya kidinamiki) ndani ya bomba.

## Mabadilishano: faida na hasara

| Aina ya jaribio / mazoea | Faida | Hasara |
|---|---|---|
| Majaribio ya kitengo | Haraka, sahihi, nafuu, thabiti | Hukosa kasoro za uunganishaji na ngazi ya mfumo |
| Majaribio ya uunganishaji | Hunasa kasoro za kiolesura na uunganishaji | Polepole; usanidi zaidi; dhaifu zaidi |
| Majaribio ya mwanzo-hadi-mwisho | Kujiamini kwa juu zaidi katika tabia halisi | Polepole, yasiyo thabiti, ghali kudumisha |
| TDD | Usanifu bora, uwezo wa kujaribu uliohakikishwa | Mkondo wa kujifunza; huhisi polepole mwanzoni |
| Majaribio yanayotegemea sifa | Hupata kesi za pembeni, huweka vigeu visivyobadilika | Yanahitaji kufikiri kwa sifa; magumu kuandika |
| Majaribio ya mabadiliko | Kipimo cha kweli cha ufanisi wa majaribio | Ghali kikokotozi; polepole kuendesha |
| Lengo la juu la ufikiaji | Hufichua msimbo usiojaribiwa | Linaweza kudanganywa; linaweza kuchochea majaribio yenye thamani ndogo |

Mabadilishano ya msingi ni kujiamini dhidi ya kasi na gharama. Majaribio mapana hutoa kujiamini zaidi lakini huendeshwa polepole na huvunjika mara nyingi zaidi. Majaribio membamba ni ya haraka na thabiti lakini hukosa kasoro za ngazi ya mfumo. Mchanganyiko sahihi huongeza kujiamini kwa kila sekunde ya maoni na kila saa ya matengenezo. Na kujaribu kupita kiasi ni njia halisi ya kushindwa: seti iliyovimba ya majaribio yanayorudiwa, ya polepole, dhaifu inaweza kugharimu zaidi ya kasoro inazozuia.

## Maswali ya kujadili na timu yako

1. **Ni majaribio yapi yasiyo ya kiutendaji, ufikivu, utendaji, na usalama, yanapaswa kuzuia toleo, na yapi yaripoti tu?** Sura hii inabishana kwamba majaribio yasiyo ya kiutendaji yanastahili kuwa katika mkakati badala ya wazo la baadaye, na inabainisha kwamba ufikivu unaweza kuhitajika kisheria na majaribio ya usalama yanaweza kuwa sehemu ya ushahidi wa mamlaka ya kuendesha. Kwa mfumo mkubwa au unaowakabili raia, lango linalozuia hupunguza kasi ya utoaji, lakini kasoro ya ufikivu au usalama inayopatikana kwenye uzalishaji hubeba gharama ya urekebishaji, sifa, na ya kisheria inayopita mbali gharama ya jaribio. Leta ishara zinazoamua: mfiduo wenu wa kidhibiti, kama mfumo unawakabili raia, na mara ngapi kasoro hizi hutoroka hadi uzalishaji kwa sasa. Fanya ukaguzi unaohitajika kisheria uzuie na uache ukaguzi wa hatari ndogo uripoti kwa mwelekeo, ili lango liakisi hatari halisi badala ya itikadi. Jibu huweka moja kwa moja kinachoweza na kisichoweza kuunganishwa.

2. **Je, mnaweka asilimia ngumu ya ufikiaji kama lango, na kama ndiyo, nini kinawazuia wahandisi kuidanganya kwa majaribio yasiyo na madai?** Sura iko imara kwamba ufikiaji ni ishara, si lengo, kwamba ufikiaji wa juu wa msimbo mdogo hauthibitishi mengi, na kwamba lengo gumu hualika udanganyifu. Nambari moja iliyowekwa kuvuka shirika kubwa kwa kuaminika huzalisha majaribio yanayotekeleza msimbo bila kudai chochote, jambo linaloinua kipimo na kupunguza kujiamini halisi. Leta ishara bora kwenye mjadala: alama ya majaribio ya mabadiliko kwenye moduli zenu zenye thamani ya juu zaidi, inayopima kama majaribio yanagundua kweli kasoro zilizoingizwa. Tumia ufikiaji kupata maeneo yasiyojaribiwa na majaribio ya mabadiliko kwa kina, na upinge kuyageuza kuwa lengo ambalo uongozi unalifuatilia peke yake. Amua mahali nambari inasaidia kweli na mahali inaalika maigizo tu.

3. **Sera yenu ni ipi seti ya majaribio inapokua polepole mno kwa wahandisi kuisubiri?** Mabadilishano ya msingi katika sura hii ni kujiamini dhidi ya kasi na gharama, na inataja kujaribu kupita kiasi kama njia halisi ya kushindwa ambapo seti iliyovimba, inayorudiwa, ya polepole inagharimu zaidi ya kasoro inazozuia. Katika timu kubwa, muda wa kuendesha seti ni ushuru wa pamoja unaolipwa kwa kila badiliko, na seti ambayo watu hujifunza kuikwepa hupoteza thamani yote. Leta ushahidi: muda wa saa wa CI, majaribio ya polepole zaidi, na kiasi gani cha ufikiaji wa mwanzo-hadi-mwisho unaorudiwa kinakopi majaribio ya kitengo ya nafuu zaidi. Sukuma majaribio hadi ngazi ya chini kabisa inayotoa kujiamini halisi, endesha sambamba, na ufute majaribio ya polepole yanayorudiwa kwa tarehe ya mwisho. Kuboresha kujiamini kwa kila sekunde ya maoni, si idadi ghafi ya majaribio, ndilo lengo.

4. **Jaribio linapokuwa lisilo thabiti, nani analimiliki, lazima lirekebishwe au kufutwa kwa haraka kiasi gani, na nini kinatekeleza tarehe hiyo ya mwisho?** Sura hii inachukulia jaribio lisilo thabiti kama jaribio lililovunjika, kasoro ya daraja la kwanza, kwa sababu seti inayoshindwa bila mpangilio huifunza timu kubwa kupuuza ujenzi mwekundu na kuharibu kimyakimya wavu wa usalama ambao kila mtu anautegemea. Shinikizo linaloshindana ni halisi: kuweka jaribio lisilo thabiti karantini kunafungua utoaji leo lakini kunahatarisha kuficha kasoro halisi ya mara kwa mara, huku kuzuia juu yake kunakwamisha mamia ya wahandisi kwa kushindwa ambako kunaweza kuwa kelele tupu. Leta ushahidi unaotatua: kiwango chenu cha sasa cha kutokuwa thabiti, majaribio hukaa karantini muda gani kabla mtu hajayagusa, na mangapi ya majaribio ya karantini yaligeuka kuficha kasoro halisi. Kabidhi mmiliki kwa kila jaribio la karantini, weka tarehe ngumu ya kurekebisha au kufuta, na ufuatilie kuaminika kama kipimo cha seti yenyewe. Katika mazingira ya mashirika makubwa na ya serikali ambapo ujenzi wa kijani ni sehemu ya ushahidi wa toleo, rundo lisilosimamiwa la karantini pia ni dhima ya ukaguzi, kwa sababu unatoa kwa ishara ambayo mmekubaliana kwa faragha kutoiamini.

5. **Je, mnaruhusiwa kutumia data ya uzalishaji katika mazingira ya majaribio, na kama sivyo, mtazalishaje data bandia yenye uaminifu wa kutosha kunasa kasoro halisi?** Sura iko wazi kwamba kanuni za faragha mara nyingi hukataza data halisi binafsi katika majaribio, na kwamba data bandia lazima iakisi sifa za uzalishaji la sivyo majaribio yako yanatoa kujiamini kwa uongo. Kwa shirika kubwa mvutano ni kati ya uaminifu na uzingatiaji: data ya uzalishaji hunasa kesi za pembeni zenye fujo ambazo data bandia hukosa, lakini kila nakala yake huzidisha mfiduo na wajibu wako. Leta mahususi: seti zipi za data zinabeba data binafsi au inayodhibitiwa, kanuni zenu za faragha na makazi ya data zinahitaji nini kweli, na vifaa vyenu vya sasa vinazalisha upya mgawanyo na kesi za pembeni zinazoonekana kwenye uzalishaji kwa uzuri kiasi gani. Sawazisha viwanda au wajenzi ili kila jaribio liunde hasa data linayohitaji, na wekeza katika uzalishaji bandia unaolingana na mgawanyo halisi wa idadi ya watu na ujazo. Katika programu za serikali na zinazodhibitiwa, kutumia data ya raia katika mazingira ya majaribio si njia ya mkato, ni uvunjaji unaoripotiwa, kwa hiyo mkakati wa data lazima utatuliwe kabla mazingira ya kwanza hayajasimamishwa.

6. **TDD, BDD, au uendelezaji unaoendeshwa na ubainishaji unapaswa kutarajiwa badala ya hiari wapi, na nani anaamua?** Sura hii inaviweka kama nidhamu za kutumia pale zinapoongeza uwazi, si maagizo kwa kila mstari wa msimbo, hata hivyo timu kubwa hunufaika na chaguo-msingi la pamoja ili mazoea yasigawanyike timu kwa timu. Mabadilishano ni kati ya faida za usanifu na ufuatiliaji (ubainishaji unaotekelezeka ambao wataalamu wa sera wanaweza kuupitia, majaribio yanayookoka urekebishaji) na mkondo halisi wa kujifunza na polepole ya awali inayofanya agizo la jumla lijirudi. Leta ushahidi kuweka wigo: moduli zipi zinabeba mantiki tata au viwango vya juu vya kushindwa kwa mabadiliko, mahali vigezo vya kukubalika lazima vifuatiliwe hadi mahitaji, na timu zinazotumia hivi tayari zinaripoti nini kuhusu kasi na viwango vya kasoro. Hifadhi matarajio kwa mantiki tata na maeneo yenye mahitaji mengi, na uache msimbo rahisi ujichagulie. Katika programu za serikali na zinazodhibitiwa ambapo programu lazima ifuatiliwe hadi sheria inayotekeleza, uendelezaji unaoendeshwa na ubainishaji wenye ushahidi unaotekelezeka wa kukubalika ni njia ya mamlaka yako ya kuendesha zaidi ya upendeleo, kwa hiyo taja waziwazi inapohitajika.

## Mtazamo wa sekta

**Kampuni changa.** Timu ndogo haiwezi kuajiri QA, kwa hiyo fanya seti ijilipie: majaribio ya kitengo ya haraka kwa kila commit pamoja na majaribio mawili ya mwanzo-hadi-mwisho kwenye njia moja inayolipa bili, na hakuna ambacho hutadumisha. Ruka malengo ya ufikiaji na ujaribu mantiki unayoogopa zaidi kuivunja, ili uweze kutoa mara kadhaa kwa siku bila kupitia kurudi nyuma kwa mkono. Rekebisha jaribio lisilo thabiti siku hiyo hiyo, kwa sababu katika hatua hii seti ambayo timu inajifunza kuipuuza ni mbaya kuliko kutokuwa na seti.

**Biashara ndogo.** Bila mhandisi maalumu wa majaribio na bajeti finyu, tegemea majaribio yaliyojengwa katika mifumo na zana unazoendesha tayari badala ya kifaa maalumu usichoweza kukiunga mkono. Pa kipaumbele ukaguzi machache unaolinda mapato na uaminifu wa wateja, na utumie CI inayohifadhiwa na wengine ili usidumishe miundombinu ya ujenzi mwenyewe. Pendelea kununua uchanganuzi wa ufikivu na usalama kama huduma badala ya kuujenga, kwa kuwa kasoro moja iliyokosekana inaweza kugharimu zaidi ya mwaka wa zana.

**Biashara kubwa.** Kuvuka timu nyingi tatizo la mkakati ni uthabiti: chaguo-msingi la piramidi la pamoja, karantini ya kiotomatiki ya majaribio yasiyo thabiti, na malango yasiyo ya kiutendaji yanayomaanisha kitu kilekile kila mahali, ili ujenzi wa kijani uaminike bila kujali nani aliyeuzalisha. Pangia bajeti muda wa kuendesha seti kama ushuru wa pamoja na uendeshe sambamba kwa nguvu, kwa sababu muda wa saa wa CI hulipwa kwa kila badiliko na kila mhandisi. Simamia alama za ufikiaji na mabadiliko kama ishara za jalada zenye umiliki wazi, si nambari ambazo uongozi unazifuatilia peke yake.

**Serikali.** Ununuzi na usimamizi hufanya majaribio kuwa ushahidi, si usafi wa kihandisi tu. Eleza kanuni za kustahiki na sera kama ubainishaji unaotekelezeka uliopitiwa na wataalamu wa eneo, ili uweze kufuatilia programu hadi sheria inayotekeleza, na ufanye majaribio ya ufikivu na usalama yazuie kwa sababu yanahitajika kisheria na ni sehemu ya ushahidi wa mamlaka ya kuendesha. Tumia data bandia iliyozalishwa kulingana na mgawanyo halisi, kwa kuwa data ya raia katika mazingira ya majaribio ni uvunjaji unaoripotiwa, na uweke vitu vya majaribio vinavyokaguliwa ili mhakiki wa nje athibitishe hasa kilichothibitishwa.

## Mifano

**Kampuni changa.** Kampuni changa ya watu watano haiwezi kumudu timu ya QA, kwa hiyo inategemea seti ya haraka ya majaribio ya kitengo inayoendeshwa kwa kila commit pamoja na majaribio mawili ya mwanzo-hadi-mwisho yanayofunika njia ya usajili-hadi-malipo inayolipa bili. Waanzilishi wanaruka ufikiaji kamili na badala yake wanajaribu mantiki wanayoogopa zaidi kuivunja, jambo linalowaruhusu kutoa mara kadhaa kwa siku bila kupitia kurudi nyuma kwa mkono. Jaribio lisilo thabiti linapoanza kushindwa bila mpangilio, wanalirekebisha siku hiyo hiyo, kwa sababu seti ambayo timu inajifunza kuipuuza ni mbaya kuliko kutokuwa na seti katika hatua ambapo uaminifu ndio kila kitu.

**Biashara kubwa.** Jukwaa kubwa la biashara ya mtandaoni linadumisha maelfu ya majaribio ya kitengo ya haraka yanayoendeshwa kwa kila commit ndani ya dakika, seti iliyolenga ya majaribio ya uunganishaji kuzunguka mipaka ya malipo na hesabu, na seti ndogo ya majaribio ya mwanzo-hadi-mwisho kwa safari muhimu za malipo. Majaribio yasiyo thabiti ya mwanzo-hadi-mwisho yanawekwa karantini kiotomatiki na kukabidhiwa kurekebishwa. Kwa sababu wahandisi wanaiamini seti, wanatoa mara nyingi kwa siku, wakiwa na uhakika kwamba ujenzi mwekundu unamaanisha tatizo halisi.

**Serikali.** Mfumo wa kitaifa wa manufaa unaofanya kazi chini ya usimamizi wa kidhibiti unatumia BDD kueleza kanuni za kustahiki kama ubainishaji unaotekelezeka uliopitiwa na wataalamu wa sera, jambo linalotoa ushahidi unaofuatilika kwamba programu inatekeleza sheria. Inatumia data bandia iliyozalishwa kulingana na mgawanyo halisi wa idadi ya watu, kwa sababu kanuni za faragha zinakataza data ya raia katika mazingira ya majaribio. Majaribio ya ufikivu ni ya lazima na yanazuia toleo, kwa kuwa huduma lazima itumike na raia wote. Na majaribio ya usalama ni sehemu ya ushahidi wa mamlaka ya kuendesha (ATO), idhini rasmi ya kuendesha mfumo katika uzalishaji.

## Kesi ya biashara: sababu, ROI, na TCO

Mapato ya majaribio ni uwezo wa kubadilisha programu haraka na kwa usalama, ambao ndio msingi wa kasi ya utoaji endelevu. Seti ya kiotomatiki inayoaminika inachukua nafasi ya [majaribio ya kurudi nyuma](https://en.wikipedia.org/wiki/Regression_testing) ya mkono ya polepole, ghali na kunasa kasoro zikiwa nafuu zaidi kurekebisha, kabla ya toleo badala ya katika uzalishaji. Katika mfumo unaodhibitiwa au unaowakabili raia, gharama ya kasoro ya uzalishaji (urekebishaji, sifa, na uwezekano wa mfiduo wa kisheria) inapita mbali gharama ya majaribio ambayo yangeinasa.

Gharama ya kupokea ni halisi: unaandika na kudumisha majaribio, na kujenga miundombinu ya [uunganishaji endelevu](https://en.wikipedia.org/wiki/Continuous_integration) (CI). Lakini gharama ya kutojaribu ni kubwa zaidi na inajumlika: uendelezaji unaoendeshwa na hofu unaoshuka hadi kutambaa, kurudi nyuma mara kwa mara, na michakato ya toleo la mkono isiyoweza kupanuka. Pia kuna gharama ya kujaribu kupita kiasi, kwa hiyo hoja ni ya mkakati ulioundwa vizuri, si idadi ya juu zaidi ya majaribio. Kujenga hoja kwa uongozi, unganisha seti na mzunguko wa utoaji, kiwango cha kushindwa kwa mabadiliko, na muda wa wastani wa kurejesha, na upime juhudi za majaribio ya mkono inazozibadilisha na matukio ya uzalishaji inayoyazuia.

## Mifumo mibaya na mitego

- **Majaribio ya koni ya aiskrimu:** kwa wingi majaribio ya mwanzo-hadi-mwisho ya polepole juu ya msingi mwembamba wa kitengo; polepole, yasiyo thabiti, ghali.
- **Ufikiaji kama lengo:** kufukuzia asilimia kwa majaribio yasiyo na madai au ya kipuuzi yasiyothibitisha chochote.
- **Kujaribu undani wa utekelezaji:** majaribio yaliyounganishwa na ndani yanayovunjika kwa kila urekebishaji, yakikatisha mabadiliko.
- **Kutokuwa thabiti kunakovumiliwa:** kushindwa bila mpangilio kunakoifundisha timu kupuuza ujenzi mwekundu.
- **Data ya majaribio ya pamoja inayobadilika:** majaribio yanayoingiliana na kushindwa bila kutabirika.
- **Kutumia data ya uzalishaji kwenye majaribio:** uvunjaji wa faragha na uzingatiaji unaosubiri kutokea.
- **Majaribio yasiyo ya kiutendaji yameruka:** ufikivu, utendaji, na usalama kugunduliwa kwenye uzalishaji tu.
- **Seti isiyoaminiwa:** isiyo ya kuaminika kiasi kwamba wahandisi huiendesha tena au kuikwepa mara kwa mara, ikibatilisha madhumuni yake.

## Kielelezo cha ukomavu

- **Ngazi ya 1, Kuanzisha:** Majaribio ni ya mkono na ya kuitikia; ufikiaji wa kiotomatiki ni mdogo; kurudi nyuma ni mara kwa mara na kunanaswa kuchelewa, mara nyingi na watumiaji badala ya seti.
- **Ngazi ya 2, Kuendeleza:** Majaribio ya kiotomatiki ya kitengo na baadhi ya uunganishaji yapo, lakini seti ni polepole au isiyo thabiti, uaminifu ni mdogo, na mazoea hutofautiana sana kutoka timu moja hadi nyingine.
- **Ngazi ya 3, Kusawazisha:** Seti yenye uwiano, ya haraka, ya kuaminika inazuia kila badiliko; chaguo-msingi la piramidi lililoandikwa, sera ya majaribio yasiyo thabiti, na majaribio yasiyo ya kiutendaji (ufikivu, utendaji, usalama) yanatekelezwa kwa uthabiti kuvuka timu.
- **Ngazi ya 4, Kusimamia:** Afya ya seti inapimwa na kudhibitiwa dhidi ya vipimo vya msingi; kiwango cha kutokuwa thabiti, muda wa saa wa CI, alama ya mabadiliko kwenye moduli zenye thamani ya juu, na kiwango cha kasoro zilizotoroka vinafuatiliwa na kupitiwa; ufikiaji ni ishara moja kati ya kadhaa, na malango huchochewa na ushahidi badala ya maoni.
- **Ngazi ya 5, Kuratibu:** Mbinu za hali ya juu (zinazotegemea sifa, mabadiliko, fuzz) zinalenga msimbo wenye thamani ya juu; majaribio yameunganishwa na vipimo vya utoaji kama mzunguko wa utoaji, kiwango cha kushindwa kwa mabadiliko, na muda wa wastani wa kurejesha; shirika huunda upya seti kila wakati kulingana na usanifu na hatari yake, likistaafisha majaribio yanayorudiwa na kuwekeza pale ushahidi unaonyesha kasoro bado zinatoroka.

## Mawazo ya kujadili

- Mgawanyo wa majaribio yenu una umbo gani kweli, na je, unalingana na usanifu na hatari yenu?
- Mnaamuaje lini kipande cha msimbo kinastahili majaribio yanayotegemea sifa au mabadiliko dhidi ya majaribio ya mifano?
- Sera yenu ya majaribio yasiyo thabiti ni ipi, na je, inatekelezwa kweli?
- Mnazalishaje data bandia halisi bila kuvuja taarifa nyeti?
- Ufikiaji unasaidia wapi kweli, na umedanganywa wapi?
- Majaribio yanayozalishwa na AI yanapaswa kupitiwaje ili yaongeze kujiamini badala ya kelele?

## Mambo muhimu ya kukumbuka

- Jaribu ili upate kujiamini kubadilisha; boresha kujiamini kwa kila kitengo cha kasi na gharama.
- Tumia piramidi kama chaguo-msingi lakini umba majaribio kulingana na usanifu wako.
- Chukulia majaribio yasiyo thabiti kama kasoro na ufikiaji kama ishara, si lengo.
- Tumia mbinu za hali ya juu pale thamani inapohalalisha gharama.
- Jumuisha majaribio ya ufikivu, utendaji, na usalama katika mkakati, na utumie data bandia kulinda faragha.

## Marejeo na usomaji zaidi

- Kent Beck, *Test-Driven Development: By Example*
- Lisa Crispin and Janet Gregory, *Agile Testing: A Practical Guide for Testers and Agile Teams*
- Gerard Meszaros, *xUnit Test Patterns: Refactoring Test Code*
- Michael Feathers, *Working Effectively with Legacy Code*
- Nicole Forsgren, Jez Humble, Gene Kim, *Accelerate: The Science of Lean Software and DevOps*
- Martin Fowler, articles on the Test Pyramid and test-related patterns
