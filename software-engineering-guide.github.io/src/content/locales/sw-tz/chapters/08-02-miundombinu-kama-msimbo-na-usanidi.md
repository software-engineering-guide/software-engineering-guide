# 8.2 Miundombinu-kama-msimbo na usanidi

## Muhtasari na msukumo

[Miundombinu-kama-msimbo](https://en.wikipedia.org/wiki/Infrastructure_as_code) (IaC) inamaanisha kufafanua na kutayarisha miundombinu (mitandao, seva, hifadhidata, visambazaji mzigo, ruhusa) kupitia faili za fasili zinazosomeka na mashine badala ya mibofyo ya kiweko cha mkono au hati za papo hapo. [Usimamizi wa usanidi](https://en.wikipedia.org/wiki/Configuration_management) hupanua wazo lilelile kwa mipangilio na hali ya mifumo mara inapokuwepo. Pamoja zinageuza miundombinu kutoka mabaki dhaifu yaliyotengenezwa kwa mkono kuwa zao lenye matoleo, linaloweza kupitiwa, linalozalishika upya la nidhamu ileile ya kihandisi unayotumia kwa msimbo wa programu.

Kwa timu kubwa, IaC si urahisi bali ni lazima. Mamia ya wahandisi wanapohitaji mazingira na maelfu ya rasilimali lazima zibaki thabiti kuvuka kanda na akaunti, utayarishaji wa mkono hauwezi kuendana na hauwezi kubaki sahihi. Miundombinu iliyosanidiwa na binadamu huteleza, mapema au baadaye, kuwa seva za "kipekee" ambazo hakuna anayezielewa kikamilifu na ambazo haziwezi kujengwa upya kwa kutegemewa baada ya kushindwa. Kusimba miundombinu kunaifanya iwe thabiti, inayokaguliwa, na inayoweza kutupwa. Mazingira yoyote yanaweza kuundwa upya kutoka fasili yake, na badiliko lolote ni diff inayoweza kupitiwa.

Mashirika makubwa na serikali hupata faida moja zaidi, ya kuamua: utawala unaotekelezeka. Mahitaji ya usalama na uzingatiaji, kama usimbaji fiche wa kuhifadhiwa, kugawanya mtandao, kanda zilizoidhinishwa, na lebo za mgao wa gharama, yanaweza kupachikwa moja kwa moja kwenye msimbo na kukaguliwa kiotomatiki kabla chochote hakijatayarishwa. Badala ya kukagua miundombinu baada ya tukio na kufukuzia ukiukaji, unazuia miundombinu isiyozingatia isiwepo kamwe. Mabadiliko haya kutoka ugunduzi hadi kinga ndiyo sababu kuu IaC imekuwa msingi wa mazoea ya kisasa ya jukwaa.

## Kanuni kuu

- Pendelea fasili za kutangaza zinazoelezea hali inayotakiwa kuliko hati za amri zinazoelezea hatua.
- Hifadhi fasili zote za miundombinu kwenye udhibiti wa matoleo, zikipitiwa kama msimbo mwingine wowote.
- Chukulia miundombinu kama isiyobadilika: badilisha badala ya kurekebisha mahali.
- Fanya utayarishaji uwe na kutobadilika thamani ili kutumia fasili ileile mara kwa mara kuzae matokeo yaleyale.
- Gundua na patanisha kuteleza, mazingira hai yakitofautiana na fasili yake iliyotangazwa, mfululizo; msimbo, si mfumo hai, ndio chanzo cha ukweli.
- Tunga miundombinu kutoka moduli zinazotumika tena, zenye matoleo badala ya kunakili na kubandika.
- Simba sera kama msimbo, kanuni za shirika zilizoelezwa kama msimbo unaokaguliwa na mashine, ili vizuizi viwe vya kiotomatiki, si ushauri.
- Weka siri nje ya fasili; zirejelee kutoka kidhibiti maalumu cha siri.

## Mapendekezo

### Chagua zana za kutangaza na uzipange kuzunguka moduli

Pokea zana ya IaC ya kutangaza, kama [Terraform](https://en.wikipedia.org/wiki/Terraform_(software)), Pulumi, au chaguo la asili ya wingu kama CloudFormation, na usawazishe juu yake kuvuka shirika ili uepuke mandhari ya zana iliyogawanyika. Mazoea muhimu ya usanifu ni moduli: jenga moduli ndogo, zilizoandikwa vizuri, zenye matoleo zinazonasa mifumo ya kawaida (mtandao unaozingatia, hifadhidata iliyoimarishwa, huduma ya kawaida). Timu kisha hutunga mazingira kutoka moduli hizi badala ya kuandika rasilimali ghafi. Hii inaeneza chaguo-msingi nzuri na mipangilio ya usalama kiotomatiki na kupunguza marudio kwa kiasi kikubwa.

### Simamia hali kwa makusudi

Zana za kutangaza hufuatilia ulinganishaji kati ya msimbo na rasilimali halisi kwenye faili ya hali. Hifadhi hali kwa mbali kwenye backend ya pamoja, iliyosimbwa, inayodhibitiwa ufikiaji, na utumie kufunga ili mabadiliko sambamba yasiiharibu. Usiweke hali kwenye kompyuta ndogo kamwe, na usiihariri kwa mkono kamwe isipokuwa kama hatua ya mwisho ya urejeshaji. Hali ni nyeti, kwa sababu inaweza kuwa na metadata ya rasilimali na siri, kwa hiyo ilinde ipasavyo.

### Jenga miundombinu isiyobadilika kwa picha za dhahabu

Badala ya kupachika seva zinazoendesha, oka "picha ya dhahabu" yenye toleo (picha ya mashine au kontena iliyosanidiwa mapema, iliyoimarishwa) na usambaze mifano mipya kutoka kwayo. Unapohitaji badiliko au kiraka, jenga picha mpya na uisambaze, ukistaafisha mifano ya zamani. Hii inaondoa kuteleza kwa usanidi, inafanya kurudisha nyuma kuwa rahisi, na inaweka kila mfano ukifanana na kufuatilika hadi ujenzi unaojulikana kuwa mzuri. Mabomba ya picha ya kiotomatiki yanapaswa kujumuisha kuimarisha usalama na kuchanganua, ili uzingatiaji ujengwe ndani katika kiwango cha picha.

### Gundua na patanisha kuteleza kwa usanidi

Kuteleza hutokea mazingira hai yanapotofautiana na fasili yake, kwa kawaida kwa sababu mtu alifanya badiliko la mkono la dharura. Endesha ugunduzi wa mara kwa mara wa kuteleza unaolinganisha hali halisi na hali iliyotangazwa na kuweka alama tofauti. Chukulia kuteleza kama kasoro: patanisha kwa kusasisha msimbo na kutumia upya, si kuacha badiliko la mkono mahali pake. Kwa mifumo inayohitaji utekelezaji endelevu wa usanidi, tumia zana ya usimamizi wa usanidi inayounganisha wenyeji kuelekea hali yao iliyotangazwa mfululizo.

### Pokea GitOps na usambazaji unaotegemea kuvuta

Katika mfano wa GitOps, hazina ya Git inashikilia hali inayotakiwa iliyotangazwa ya mfumo, na wakala wa kiotomatiki anayeendesha ndani ya mazingira lengwa huvuta hali hiyo mfululizo na kupatanisha mfumo hai ili ulingane. Hii inapindua mfano wa jadi wa kusukuma. Hakuna mfumo wa nje unaohitaji vitambulisho vya kudumu vya kubadilisha mazingira, kwa sababu mazingira yanavuta usanidi wake wenyewe. GitOps inakupa nyayo kamili za ukaguzi (kila badiliko ni commit), kurudisha nyuma rahisi (rudisha commit), na marekebisho imara ya kuteleza (wakala anathibitisha upya hali inayotakiwa mfululizo). Una nguvu hasa kwa [Kubernetes](https://en.wikipedia.org/wiki/Kubernetes) na kwa mashirika yanayotaka chanzo kimoja cha ukweli kinachoweza kupitiwa.

### Tekeleza vizuizi kwa sera-kama-msimbo

Eleza kanuni za shirika, kama kanda zinazoruhusiwa, usimbaji fiche wa lazima, lebo zinazohitajika, na kukataza mfiduo wa umma, kama sera zinazokaguliwa na mashine kwa kutumia zana kama Open Policy Agent (OPA) au injini ya sera ya asili ya jukwaa kama Sentinel. Endesha ukaguzi huu kwenye bomba kabla ya kutayarisha, ili ukiukaji uzuiwe kiotomatiki. Sera-kama-msimbo hugeuza nia ya timu ya usalama kuwa kidhibiti kinachotekelezeka, kinachotumika kwa usawa, na kinapanuka hadi maelfu ya mabadiliko kwa njia ambayo mapitio ya mkono hayangeweza.

## Mabadilishano: faida na hasara

| Chaguo | Faida | Hasara | Inafaa zaidi |
|---|---|---|---|
| IaC ya kutangaza (Terraform/Pulumi) | Inazalishika upya, inapitiwa, kuteleza kunagunduliwa | Mkondo wa kujifunza; ugumu wa usimamizi wa hali | Karibu timu zote kwa ukubwa |
| Hati za amri | Zinazojulikana; zinanyumbulika kwa mambo ya mara moja | Hazina kutobadilika thamani; ngumu kukagua na kurudia | Kesi finyu, za mpito |
| Isiyobadilika + picha za dhahabu | Hakuna kuteleza; kurudisha nyuma kwa urahisi | Mzigo wa bomba la ujenzi wa picha | Meli zinazohitaji uthabiti |
| Usimamizi wa usanidi unaobadilika | Udhibiti wa kina endelevu | Hatari ya kuteleza; kuungana polepole | Wenyeji wa urithi au wa muda mrefu |
| GitOps (unaotegemea kuvuta) | Nyayo imara za ukaguzi; hujiponya | Inahitaji wakala ndani ya kundi na nidhamu ya Git | Kubernetes na asili ya wingu |
| Sera-kama-msimbo | Vizuizi vya kiotomatiki, vya usawa | Juhudi ya awali ya kuandika sera | Mazingira yanayodhibitiwa |

Mvutano mkuu ni unyumbulifu dhidi ya udhibiti. Mbinu za mkono na za amri zinahisi haraka kwa badiliko moja, lakini hukusanya kutokuwa na uthabiti kufichika kunakolemaza kwa ukubwa. Miundombinu ya kutangaza, isiyobadilika, inayotawaliwa na sera inaomba uwekezaji wa awali zaidi na mabadiliko halisi ya kitamaduni, kwa kuwa wahandisi lazima waache mabadiliko ya haraka ya kiweko, lakini inalipa uwekezaji huo mara nyingi katika kutegemewa, uwezo wa kukaguliwa, na uwezo wa kujenga upya chochote unapohitajika.

## Maswali ya kujadili na timu yako

1. **Nani anamiliki maktaba ya moduli ya pamoja, na uboreshaji wa moduli unafikiaje kila timu inayoitumia?** Moduli hulipa tu ikiwa marekebisho na chaguo-msingi zilizoimarishwa zinasambaa, na hilo linahitaji umiliki wazi na matoleo halisi, si folda ambayo kila mtu anakopa kutoka. Amua nani anadumisha moduli za mtandao unaozingatia na hifadhidata iliyoimarishwa, mnaziwekaje matoleo (matoleo ya kisemantiki yenye kumbukumbu ya mabadiliko), na timu zinavuta masasisho vipi bila mbio za dharura. Kwa ukubwa hii ndiyo tofauti kati ya kurekebisha usanidi mbaya mara moja na kuufukuzia kuvuka maelfu ya rasilimali zilizohaririwa kwa mkono. Leta ushahidi: nakala ngapi tofauti za mfumo ule ule zipo leo, marekebisho ya usalama yanachukua muda gani kufika kila mazingira, na kama timu zinabandika matoleo ya moduli au kuyaacha yaelee. Kiraka muhimu kisipofika eneo lote ndani ya siku, uundaji wenu wa moduli ni wa mapambo.

2. **Mzunguko wenu wa ugunduzi wa kuteleza ni upi, na nini kinatokea kuteleza kunapopatikana?** Kuteleza ni mazingira hai kutofautiana kimyakimya na hali yake iliyotangazwa, kwa kawaida kutokana na badiliko la dharura la kiweko, na kuvumilia kunageuza msimbo wenu kuwa hadithi. Amua mara ngapi mnalinganisha hali halisi na hali iliyotangazwa (kila usiku ni chaguo-msingi la busara) na, muhimu zaidi, amua jibu: patanisha kwa kusasisha msimbo na kutumia upya, kamwe si kuacha badiliko la mkono mahali pake. Katika mazingira yanayodhibitiwa hili ni sharti la udhibiti, kwa sababu wakaguzi wanahitaji hali iliyotangazwa ilingane na uhalisia mfululizo. Leta namba zenu za sasa: rasilimali ngapi zinateleza kila wiki, zinabaki zimeteleza kwa muda gani, na kama yeyote anawajibika kuzifunga. Chukulia kila kuteleza kama kasoro yenye mmiliki, la sivyo dhamana ya chanzo cha ukweli inamomonyoka hadi hakuna anayeamini msimbo.

3. **Mmehamia GitOps na upatanisho unaotegemea kuvuta, au mfumo wa nje bado unashikilia vitambulisho vya kudumu vya kubadilisha uzalishaji?** Katika mfano wa kuvuta wakala ndani ya mazingira lengwa hupatanisha mfumo hai na Git mfululizo, jambo linaloondoa hitaji la mfumo wowote wa nje kushikilia ufikiaji wa kuandika, na linathibitisha upya hali inayotakiwa ili kuteleza kujirekebishe. Huo ni msimamo imara wa usalama na ukaguzi, kwa kuwa kila badiliko ni commit na hakuna mwendeshaji anayehitaji vitambulisho vya kudumu vya uzalishaji. Gharama ni halisi: wakala wa ndani ya kundi wa kuendesha na nidhamu kali ya Git, kwa hiyo ipime dhidi ya uotomatishaji wenu wa sasa wa kusukuma. Leta orodha ya nani na nini kinaweza kubadilisha uzalishaji moja kwa moja sasa, na nyayo za ukaguzi ambazo mabadiliko hayo yanaacha. Kwa Kubernetes na maeneo ya uhakikisho wa juu mabadiliko haya kwa kawaida yanastahili; kwa rasilimali chache tuli yanaweza kuwa ya kupita kiasi.

4. **Hali ya miundombinu yenu inahifadhiwa, kufungwa, na kudhibitiwa ufikiaji vipi, na nini kinatokea siku ikiharibika au kupotea?** Hali ni ramani kati ya msimbo wenu na rasilimali halisi, kwa hiyo faili ya hali iliyopotea au kuharibika inaweza kuiacha zana kipofu kwa rasilimali iliyoziunda na kumshawishi mtu kutumia upya kwa uharibifu. Kwa timu kubwa hatari inazidishwa, kwa sababu wahandisi wengi wanaotumia dhidi ya hali ya pamoja wanahitaji backend ya mbali, iliyosimbwa, iliyofungwa ili uendeshaji sambamba usiharibu wenzake. Pima urahisi wa hali moja kubwa dhidi ya eneo la mlipuko inaloweka, na fikiria kugawanya hali kwa mazingira au kwa eneo ili kosa moja lisiangushe kila kitu. Leta ukweli: hali inaishi wapi leo, kama kufunga kunatekelezwa, nani anaweza kuisoma (inaweza kuwa na siri), na kama mmewahi kufanyia mazoezi urejeshaji. Katika mazingira ya mashirika makubwa na serikali, chukulia backend ya hali kama mali nyeti, inayodhibitiwa ufikiaji yenye nakala rudufu yake, kumbukumbu ya ukaguzi, na kitabu cha mwongozo cha urejeshaji, kwa sababu kuipoteza ni kupoteza rekodi yenu ya kilichopo.

5. **Dharura halisi inapodai badiliko la mkono, njia iliyoidhinishwa ya kuvunja kioo ni ipi, na badiliko hilo linarudishwa vipi kwenye msimbo?** Kila mazoea ya IaC yaliyokomaa hukutana na tukio la saa tisa usiku ambapo kusubiri bomba haikubaliki, na swali la uaminifu si kama mabadiliko ya mkono hutokea kamwe bali jinsi mnavyoyadhibiti. Amua mapema nani anaweza kupita bomba, anaruhusiwa kugusa nini, kitendo kinaandikwa vipi, na tarehe ya mwisho ambayo badiliko lazima lipatanishwe kwenye msimbo au kurudishwa. Bila makubaliano hayo, ubaguzi wa dharura unakuwa tabia ya kila siku kimyakimya na ClickOps inarudi kwa mlango wa nyuma. Leta ushahidi: mabadiliko mangapi ya nje ya bomba yalitokea robo iliyopita, kila moja lilibaki bila kupatanishwa kwa muda gani, na kama ugunduzi wa kuteleza uliyanasa kweli. Kwa vyombo vya umma na vinavyodhibitiwa, utaratibu ulioandikwa wa kuvunja kioo wenye uandishi wa kiotomatiki mara nyingi ni sharti la udhibiti, kwa sababu wakaguzi wanatarajia dharura zinawezekana na kila moja inaacha nyayo na kurudisha mfumo kwenye hali yake iliyotangazwa.

6. **Sehemu gani ya msingi wenu wa usalama na uzingatiaji imeelezwa kama sera inayozuia badiliko baya kiotomatiki, dhidi ya kanuni zinazoishi kwenye waraka na kutegemea mtu kukumbuka?** Vizuizi vilivyoandikwa kama nathari kwenye wiki vinakiukwa mara kwa mara, kwa sababu vinategemea kila mhandisi kuvisoma na kuvitumia chini ya shinikizo la tarehe ya mwisho, wakati kanuni zilezile zilizoelezwa kama sera-kama-msimbo zinakataa badiliko lisilozingatia kabla halijatayarishwa kamwe. Kwa shirika kubwa hii ndiyo njia pekee ambayo nia ya timu ya usalama inapanuka hadi maelfu ya mabadiliko bila kuwa kizuizi cha mapitio. Pima gharama ya awali ya kuandika na kudumisha sera dhidi ya gharama inayojirudia ya mapitio ya mkono na kurekebisha baada ya tukio, na uamue vidhibiti vipi (usimbaji fiche, kanda zilizoidhinishwa, lebo za lazima, hakuna mfiduo wa umma) havijadiliki vya kutosha kutekelezwa kama malango magumu. Leta orodha ya kanuni zenu za msingi za sasa na uweke alama zipi zimeotomatishwa dhidi ya za ushauri, pamoja na mara ngapi kila moja inakiukwa kwa vitendo. Katika mazingira ya mashirika makubwa na serikali, sera ya kiotomatiki hugeuza ukaguzi kutoka wiki za ukusanyaji wa ushahidi wa mkono hadi swali dhidi ya vidhibiti vilivyotekelezwa, na inageuza uzingatiaji kutoka ugunduzi hadi kinga.

## Mtazamo wa sekta

**Kampuni changa.** Kasi inashinda, kwa hiyo weka mrundiko wako wote kwenye hazina moja ya kutangaza (Terraform ni chaguo-msingi la kawaida), weka hali kwenye backend inayosimamiwa iliyosimbwa, na upitishe kila badiliko kupitia ombi la kuvuta hata ukiwa na timu ya watu watatu. Ruka mitambo mizito ya jukwaa: hakuna timu ya kati ya moduli, hakuna injini ya sera bado, udhibiti wa matoleo na nidhamu ya kutobofya kiweko kamwe tu. Hilo peke yake linakupa mazingira yanayozalishika upya unayoweza kuyabomoa kuokoa fedha na kuyajenga upya kwa onyesho linalofuata.

**Biashara ndogo.** Bila mtaalamu maalumu wa jukwaa, egemea huduma zinazosimamiwa na IaC yoyote ambayo mtoa huduma wako wa wingu au muuzaji tayari anaunga mkono badala ya kusimamisha zana za kipekee usizoweza kudumisha. Pendelea kununua jukwaa linalopangishwa ambalo chaguo-msingi zake zenye busara (usimbaji fiche, nakala rudufu, kupachika) zinashughulikiwa kwa ajili yako kuliko kujenga bomba la picha ya dhahabu usilokuwa na wa kuliendesha. Weka lengo kwa finyu: pata rasilimali zako chache muhimu kwenye msimbo ili uweze kuzijenga upya baada ya kushindwa au mkandarasi anayeondoka.

**Biashara kubwa.** Tatizo la msingi ni uthabiti kuvuka timu nyingi, akaunti, na kanda, kwa hiyo wekeza kwenye maktaba ya moduli ya pamoja yenye matoleo, hali ya mbali iliyofungwa, na sera-kama-msimbo inayotekelezwa kwenye bomba. Timu ya kati ya jukwaa huchapisha moduli zilizoimarishwa na vizuizi huku timu za bidhaa zikijihudumia ndani yake, na ugunduzi wa kuteleza unaendeshwa mfululizo ili maelfu ya rasilimali zibaki katika hali inayojulikana. Weka bajeti ya gharama endelevu ya kudumisha moduli na sera, kwa sababu thamani yake inatokana na marekebisho au chaguo-msingi iliyoimarishwa kusambaa kila mahali kwa wakati mmoja.

**Serikali.** Kanuni za ununuzi, uidhinishaji, na uwajibikaji wa umma vinakusukuma kuelekea miundombinu isiyobadilika, commit zilizosainiwa, na upatanisho wa GitOps ndani ya eneo lililoidhinishwa, ili hakuna mwendeshaji anayeshikilia vitambulisho vya kudumu vya kubadilisha uzalishaji. Simba msingi unaohitajika wa usalama kwenye picha za dhahabu na sera-kama-msimbo, na uache historia ya commit iwe ushahidi wa ukaguzi usioweza kuchezewa, unaopatikana kila wakati. Pendelea zana wazi, zinazohamishika kuliko miundo ya umiliki inayokunasa, na ufanye utaratibu wa kuvunja kioo na uandishi wake uwe wazi ili mabadiliko ya dharura yatimize bado mahitaji ya udhibiti wa usanidi.

## Mifano

**Kampuni changa.** Kampuni changa ya watu watano inafafanua usanidi wake wote wa AWS, yaani VPC, hifadhidata, na huduma ya kontena, kwenye hazina moja ya Terraform yenye hali iliyohifadhiwa kwenye backend ya S3 iliyosimbwa na kufunga kupitia DynamoDB. Kila badiliko linapitia ombi la kuvuta, kwa hiyo hata mhandisi wa simu ya dharura peke yake anaweza kuona hasa kitakachobadilika kabla ya kuendesha apply. Wanapohitaji mazingira mapya ya maandalizi kwa onyesho kubwa, wananakili moduli ndogo na kuyasimamisha ndani ya dakika, na kuyabomoa kwa haraka vilevile kuweka ankara ya wingu chini.

**Biashara kubwa.** Muuzaji wa rejareja wa kimataifa anasimamia miundombinu kuvuka akaunti na kanda kadhaa za wingu. Timu ya kati ya jukwaa inachapisha moduli za Terraform zenye matoleo kwa mitandao inayozingatia, hifadhidata, na kiunzi cha huduma, na kutekeleza sera za OPA zinazokataa rasilimali yoyote isiyo na usimbaji fiche au lebo za mgao wa gharama. Timu za bidhaa hutayarisha mazingira yao kwa kujihudumia, lakini kila badiliko linapita kwenye bomba, ambapo sera inakaguliwa kiotomatiki. Ugunduzi wa kuteleza unaendeshwa kila usiku na kufungua tiketi kwa badiliko lolote la mkono, ukiweka maelfu ya rasilimali mfululizo katika hali inayojulikana, inayozingatia.

**Serikali.** Wakala wa ulinzi unaofanya kazi katika mazingira ya uhakikisho wa juu unajenga picha za dhahabu zilizoimarishwa zinazopachika msingi unaohitajika wa usalama, na kusambaza tu mifano isiyobadilika kutoka picha hizo. Miundombinu yote imetangazwa kwenye Git na kupatanishwa na wakala wa GitOps ndani ya eneo lililoidhinishwa, kwa hiyo hakuna mwendeshaji anayeshikilia vitambulisho vya kudumu vya kubadilisha uzalishaji moja kwa moja. Kila badiliko ni commit iliyosainiwa. Hii inawapa wakaguzi historia kamili isiyoweza kuchezewa na kutimiza mahitaji ya ufuatiliaji endelevu na udhibiti wa usanidi bila ukusanyaji wa ushahidi wa mkono.

## Kesi ya biashara: sababu, ROI, na TCO

ROI ya IaC inatokana na kasi, kutegemewa, na kupunguza hatari. Mazingira yaliyochukua wiki za utayarishaji wa mkono unaoendeshwa na tiketi sasa yanaweza kuundwa ndani ya dakika, jambo linaloachia wahandisi na kuharakisha miradi. Uwezo wa kuzalisha upya hupunguza kwa kiasi kikubwa muda wa kupona baada ya kushindwa, kwa sababu mazingira yoyote yanaweza kujengwa upya kutoka msimbo. Utekelezaji wa sera wa kiotomatiki hupunguza mara na gharama ya matukio ya usalama na matokeo ya ukaguzi, ambayo kwa mashirika yanayodhibitiwa yanaweza kuwa makubwa.

Kwenye leja ya TCO, gharama za kupokea zinajumuisha zana, mafunzo, kujenga maktaba ya moduli na sera, na nidhamu ya kuacha kufanya mabadiliko ya mkono. Gharama ya kutopokea ni kali zaidi na hujilimbikiza kwa muda: miundombinu ya kipekee ambayo hakuna anayeweza kuijenga upya, utayarishaji wa polepole, wenye makosa, usanidi mbaya wa usalama unaosababisha uvunjaji, na ukaguzi unaotumia wiki za juhudi ya mkono. Kwa uongozi, weka IaC kama kugeuza miundombinu kutoka dhima isiyosimamiwa hadi mali iliyotawaliwa, inayozalishika upya, na kama utaratibu unaofanya usalama na uzingatiaji kuwa wa kiotomatiki badala ya wa matamanio.

## Mifumo mibaya na mitego

- **ClickOps kwenye uzalishaji.** Kufanya mabadiliko kwa mkono kwenye kiweko kunahakikisha kuteleza na kuharibu uwezo wa kuzalisha upya.
- **Siri kwenye msimbo.** Kupachika vitambulisho kwenye faili za fasili kunavivujisha kwenye historia ya matoleo na hali.
- **Fasili kubwa moja zisizo na moduli.** Usanidi mmoja mkubwa ambao hakuna anayethubutu kuubadilisha unakuwa dhaifu kama usanidi wa mkono uliobadilisha.
- **Hali isiyosimamiwa.** Faili za hali za ndani au zisizofungwa husababisha uharibifu na miundombinu iliyopotea.
- **Kuteleza kuvumiliwa.** Kuacha mabadiliko ya mkono mahali pake kunamomonyoa dhamana ya chanzo cha ukweli hadi msimbo unakuwa hadithi.
- **Sera kama nyaraka.** Kanuni zinazoishi kwenye wiki badala ya ukaguzi wa kiotomatiki zinakiukwa mara kwa mara.
- **Kuenea kwa kunakili na kubandika.** Kunakili usanidi kuvuka timu kunamaanisha marekebisho na maboresho hayasambai kamwe.

## Kielelezo cha ukomavu

**Ngazi ya 1: Kuanzisha.** Miundombinu inatayarishwa kwa mkono kupitia kiweko na hati za papo hapo. Mazingira hayana uthabiti, hayajaandikwa, na hayawezi kuzalishwa upya kwa kutegemewa, na kupona kutoka kushindwa ni polepole na kusiko na uhakika.

**Ngazi ya 2: Kuendeleza.** Baadhi ya miundombinu imesimbwa, lakini mazoea yanatofautiana kwa timu. Usimamizi wa hali hauna uthabiti, kuteleza ni kwa kawaida, siri wakati mwingine zinavuja kwenye fasili, na sera inatekelezwa, kama kabisa, kupitia mapitio ya mkono.

**Ngazi ya 3: Kusawazisha.** IaC ya kutangaza ndio kiwango kilichoandikwa kuvuka shirika, iliyojengwa kutoka moduli za pamoja zenye matoleo na hali inayosimamiwa, ya mbali, iliyofungwa. Sera-kama-msimbo inatekeleza vizuizi kwenye bomba, siri zinarejelewa kutoka kidhibiti maalumu, na ugunduzi wa kuteleza unaendeshwa kwa mzunguko wa kawaida.

**Ngazi ya 4: Kusimamia.** Mazoea yanapimwa dhidi ya vipimo vya msingi. Mnafuatilia kiwango cha kuteleza na muda wa wastani wa kupatanisha, upokeaji wa toleo la moduli kuvuka timu, ukiukaji wa sera uliozuiwa dhidi ya uliotoroka, muda wa kuongoza wa utayarishaji, na sehemu ya rasilimali iliyo chini ya msimbo kweli. Vipimo hivi vinaweka lango la mabadiliko na kuelekeza mahali pa kuwekeza, kwa hiyo maamuzi yanasimama juu ya ushahidi badala ya hadithi.

**Ngazi ya 5: Kuratibu.** Miundombinu ni isiyobadilika na inayoendeshwa na GitOps, inajiponya dhidi ya kuteleza, na ushahidi wa uzingatiaji unazalishwa kiotomatiki. Maktaba ya moduli na sera inaboreshwa mfululizo kutokana na matumizi halisi na matukio, na mazoea ya miundombinu yameunganishwa na usalama, gharama, na upangaji wa utoaji ili eneo lote lijirekebishe mahitaji yanapohama.

## Mawazo ya kujadili

- Mstari unapaswa kukaa wapi kati ya moduli zinazotawaliwa kati na uhuru wa timu wa kufafanua miundombinu maalumu?
- Mnashughulikiaje badiliko halisi la dharura linalopaswa kupita bomba, bila kugeuza ClickOps kuwa kawaida?
- Mkakati sahihi wa kusimamia na kulinda hali kuvuka akaunti na timu nyingi ni upi?
- Usimamizi wa usanidi unaobadilika bado unahalalishwa lini dhidi ya miundombinu isiyobadilika kikamilifu?
- Mnaweka vipi maktaba ya sera-kama-msimbo ikiendana na mahitaji ya usalama na ya kisheria yanayobadilika?
- Njia halisi ya uhamishaji kwa miundombinu ya urithi iliyotangulia IaC inaonekanaje?

## Mambo muhimu ya kukumbuka

- Fafanua miundombinu kwa kutangaza, iwekee matoleo, na uichukulie kama msimbo unaopitiwa, unaozalishika upya.
- Jenga kutoka moduli ndogo, zenye matoleo kueneza chaguo-msingi nzuri na kuondoa marudio.
- Pendelea miundombinu isiyobadilika na picha za dhahabu kuondoa kuteleza na kurahisisha kurudisha nyuma.
- Simamia hali kwa makusudi na uweke siri nje ya fasili.
- Pokea GitOps kwa nyayo imara za ukaguzi na upatanisho unaojiponya.
- Tekeleza vizuizi kwa sera-kama-msimbo ili uzingatiaji uzuiliwe kuwepo, si kukaguliwa baada ya tukio.

## Marejeo na usomaji zaidi

- Kief Morris, *Infrastructure as Code: Dynamic Systems for the Cloud Age*.
- Yevgeniy Brikman, *Terraform: Up & Running*.
- Betsy Beyer, Chris Jones, Jennifer Petoff, and Niall Richard Murphy (eds.), *Site Reliability Engineering*.
- Gene Kim, Jez Humble, Patrick Debois, and John Willis, *The DevOps Handbook*.
- Weaveworks, "GitOps" foundational writings (Alexis Richardson et al.).
- Open Policy Agent documentation and the Rego policy language.
- NIST Special Publication 800-53, security and privacy controls (configuration management family).
