# 2.5 Mapitio ya msimbo na ushirikiano

## Muhtasari na msukumo

[Mapitio ya msimbo](https://en.wikipedia.org/wiki/Code_review) ni mazoea ya kumfanya mtu mwingine zaidi ya mwandishi achunguze badiliko kabla halijaunganishwa. Ni mojawapo ya shughuli zenye kiegemeo cha juu zaidi za ubora na kushiriki maarifa ambazo shirika la programu linazo, na kwa timu kubwa pia ni utaratibu mkuu wa uratibu na utamaduni. Mapitio hunasa kasoro, huenea maarifa ya msimbo, hutekeleza viwango, na hushauri wahandisi, lakini tu ukiyafanya vizuri. Yakifanywa vibaya, huwa kikwazo, chanzo cha msuguano, au muhuri wa mpira unaotoa uhakikisho wa uongo.

Kwa timu kubwa, mapitio ndipo kazi ya mtu binafsi inapokutana na umiliki wa pamoja. Mara nyingi ni mahali pa mguso mkuu kati ya wahandisi wanaofanya kazi peke yao vinginevyo, kwa hiyo kanuni zake huumba jinsi shirika zima linavyoshirikiana. Mapitio huenea maarifa ili hakuna sehemu ya mfumo inayoeleweka na mtu mmoja tu, jambo linalopunguza hatari ya [bus-factor](https://en.wikipedia.org/wiki/Bus_factor), hatari wakati maarifa yanakaa kwa watu wachache mno, inayosumbua mifumo mikubwa ya muda mrefu. Pia huunda njia ya ukaguzi ya nani alibadilisha nini na nani aliidhinisha.

Katika mazingira ya mashirika makubwa na ya serikali, mapitio mara nyingi hubeba kipimo cha uzingatiaji. [Mgawanyo wa majukumu](https://en.wikipedia.org/wiki/Separation_of_duties) (hakuna mtu mmoja anayedhibiti badiliko zima nyeti), idhini za lazima, na ufuatiliaji mara nyingi ni udhibiti unaohitajika. Badiliko linalogusa mifumo nyeti linaweza kuhitaji mapitio ya majukumu mahususi, na rekodi ya mapitio inakuwa ushahidi wa ukaguzi. Changamoto yako ni kutimiza udhibiti huu huku ukiweka mapitio ya haraka na ya kujenga, badala ya kuyageuza taratibu tupu.

## Kanuni kuu

- Pitia ili kuboresha badiliko na kushiriki maarifa, si kujionyesha.
- Mabadiliko madogo hupata mapitio bora, kwa hiyo weka maombi ya kuvuta (PR) yaliyolenga na ya ukubwa unaofaa.
- Ucheleweshaji wa mapitio ni gharama ya timu nzima. Majibu ya haraka huweka kila mtu akisonga.
- Otomatisha ya kimitambo (mtindo, majaribio, uchanganuzi wa usalama) ili binadamu wapitie usanifu na usahihi.
- Tenganisha masuala yanayozuia na mapendekezo na mapendeleo, na uwe wazi ni lipi ni lipi.
- Kosoa msimbo, si mtu. Kanuni za maoni huamua kama mapitio hujenga uaminifu au kuumomonyoa.
- Mwandishi anawajibika kufanya badiliko liwe rahisi kupitiwa.

## Mapendekezo

### Fanya maombi ya kuvuta yawe madogo na yaliyoelezwa vizuri

Weka kila badiliko likilenga wasiwasi mmoja wa kimantiki na dogo vya kutosha kupitiwa kwa makini. PR kubwa hupata mapitio ya juujuu. Toa maelezo wazi ya kilichobadilika, kwa nini, na jinsi ulivyothibitisha, ili mhakiki awe na muktadha. Tenganisha urekebishaji wa kimitambo na mabadiliko ya tabia katika PR tofauti, ili kila moja liwe rahisi kufikiria. Maelezo mazuri ni mchango muhimu zaidi wa mwandishi kwa ubora wa mapitio.

### Weka viwango vya mapitio na orodha hakiki

Eleza wahakiki wanapaswa kutafuta nini: usahihi, kufaa kwa usanifu, utoshelevu wa majaribio, athari za usalama, usomekaji, na kuzingatia viwango. Orodha hakiki nyepesi huweka mapitio thabiti na kuzuia vipimo muhimu visiteleze, bila kugeuza mapitio kuwa kutia alama visanduku. Fafanua nini kinahitaji mapitio, nani anaweza kuidhinisha, na idhini zozote za kijukumu zinazohitajika kwa maeneo nyeti.

### Weka na ufuatilie kanuni za ucheleweshaji wa mapitio

Kubaliana muda unaolengwa wa kujibu, kwa mfano kujibu ndani ya siku ya kazi, na ufanye mapitio kuwa sehemu ya daraja la kwanza ya siku badala ya kitu kinachobanwa mwisho. Foleni ndefu za mapitio hukwamisha utoaji na kuwashawishi wahandisi kuelekea mabadiliko makubwa, yaliyokusanywa. Fuatilia muda hadi mapitio ya kwanza na muda hadi kuunganishwa, na uchukulie ucheleweshaji endelevu kama tatizo la mchakato la kurekebisha, si kasoro ya mtu binafsi.

### Otomatisha kila kitu cha kimitambo

Endesha muundo, [linting](https://en.wikipedia.org/wiki/Lint_(software)), majaribio, na uchanganuzi wa usalama na utegemezi kwenye [uunganishaji endelevu](https://en.wikipedia.org/wiki/Continuous_integration) (CI), ili wahakiki wasitumie umakini kwayo kamwe. Hifadhi mapitio ya binadamu kwa vitu ambavyo mashine haziwezi kuhukumu: kama usanifu ni sahihi, kama mbinu inafaa mfumo, kama majaribio yana maana, na kama msimbo bado utaeleweka baadaye.

### Tumia kuoanishwa na kufanya kazi kama kundi pale yanapofaa

Tumia [kuandika msimbo kwa kuoanishwa](https://en.wikipedia.org/wiki/Pair_programming), ambapo wahandisi wawili wanaandika msimbo pamoja kwenye kituo kimoja, kwa kazi tata au zenye hatari kubwa, utambulisho, na uhamisho wa maarifa. Ni mapitio endelevu, na mara nyingi huondoa haja ya hatua tofauti ya mapitio. Tumia [kufanya kazi kama kundi](https://en.wikipedia.org/wiki/Mob_programming), ambapo timu nzima inafanya kazi kwenye kazi moja kwa wakati mmoja, kwa maamuzi muhimu ya usanifu au kueneza maarifa ya eneo gumu kuvuka timu. Yachukulie haya kama nyongeza kwa mapitio yasiyo ya wakati mmoja, yaliyochaguliwa kwa muktadha, si mbadala za kuamuru kila mahali.

### Pokea mapitio ya kiotomatiki na yanayosaidiwa na AI kwa uangalifu

Tumia zana za mapitio ya kiotomatiki na wasaidizi wa AI kunasa masuala ya kawaida, kupendekeza maboresho, na kupunguza mzigo wa mhakiki, lakini chukulia pato lao kama ingizo, si mamlaka. Mapitio ya AI ni mazuri kwa masuala ya juujuu na uthabiti, na hafifu kwa busara ya kina ya usanifu na muktadha wa mfumo. Weka binadamu anayewajibika kwa kila idhini, hasa kwa mabadiliko nyeti kwa usalama na yanayohusiana na uzingatiaji.

### Weka kanuni za maoni ya kujenga

Weka kanuni zinazoweka maoni mahususi, ya upole, na yaliyolenga msimbo. Wahimize wahakiki kuuliza maswali badala ya kutoa amri, kueleza hoja nyuma ya ombi, na kusifu kazi nzuri. Weka alama wazi kwa wasiwasi unaozuia na mapendekezo ya hiari (kwa mfano, kwa kuweka kiambishi awali kwa maelezo yasiyozuia). Kanuni hizi huamua kama mapitio huimarisha timu au huzaa chuki.

## Mabadilishano: faida na hasara

| Mbinu | Faida | Hasara |
|---|---|---|
| Mapitio ya PR yasiyo ya wakati mmoja | Yanayobadilika; yameandikwa; yanapanuka kuvuka maeneo ya saa | Ucheleweshaji; hupoteza maelezo ya kina; yanaweza kuhisi ya mvutano |
| Kuoanishwa | Mapitio endelevu; uhamisho wa haraka wa maarifa; ubora wa juu | Watu wawili kwa kazi moja; kuchosha; magumu kupanga |
| Kufanya kazi kama kundi | Mpangilio wa timu nzima; huenea maarifa ya kina | Ghali kwa jumla; si kwa kazi ya kawaida |
| Wahakiki wengi wa lazima | Uhakikisho imara; rafiki kwa uzingatiaji | Polepole; hutawanya uwajibikaji; shinikizo la foleni |
| Mapitio yanayosaidiwa na AI | Haraka, bila kuchoka kwa masuala ya kawaida; hupunguza mzigo | Hukosa muktadha wa mfumo; kujiamini kwa uongo likiaminiwa kupita kiasi |

Mvutano wa msingi ni ukamilifu dhidi ya kasi. Mapitio ya kina hunasa zaidi, lakini hupunguza kasi ya utoaji na yanaweza kuwakatisha tamaa waandishi. Mapitio ya haraka huweka mtiririko, lakini yana hatari ya kuwa ya juujuu. Njia ni kulinganisha kina cha mapitio na hatari ya badiliko, ili mabadiliko madogo yapate mapitio mepesi na hatarishi yapate ya kina, na kuotomatisha kazi ya kimitambo ili juhudi za binadamu zielekee pale zinapojalisha.

## Maswali ya kujadili na timu yako

1. **Nini kinahesabiwa kuwa kikubwa mno kwa ombi moja la kuvuta, na je, mnatenganisha urekebishaji wa kimitambo na mabadiliko ya tabia?** Sura hii inasema wazi kwamba PR kubwa hupata mapitio ya juujuu na kwamba mwandishi anamiliki uwezo wa kupitiwa, na inakuomba utenganishe urekebishaji na mabadiliko ya tabia ili kila moja liwe rahisi kufikiria. Katika timu kubwa PR kubwa kupindukia inahakikisha muhuri wa mpira, unaotoa uhakikisho wa uongo huku ukiruhusu kasoro halisi zipite. Leta ushahidi: mgawanyo wa ukubwa wa PR zenu na jinsi kina cha mapitio kinavyoshuka tofauti zinapokua. Kubaliana kanuni ya ukubwa wa vitendo na tabia ya kutua urekebishaji safi kando na mabadiliko ya mantiki, ili mhakiki aweze kushikilia kila badiliko kichwani. Nidhamu hiyo moja huinua ubora wa kila mapitio yanayofuata.

2. **Mnatofautishaje pingamizi linalozuia na pendekezo la hiari, na je, desturi hiyo inatumika kweli?** Sura inakuomba utenganishe masuala yanayozuia na mapendeleo na uwe wazi ni lipi ni lipi, na inaashiria kuzuia kwa mapendeleo kama mfumo mbaya unaomomonyoa. Bila desturi ya pamoja, maoni ya mtindo ya mhakiki husomwa kama badiliko linalohitajika, jambo linalozaa chuki na kupunguza kasi kuvuka timu nzima. Leta mifano kutoka mapitio ya hivi karibuni ambapo upendeleo ulikwamisha uunganishaji kama ishara madhubuti. Pokea alama nyepesi, kwa mfano kiambishi awali kinachoweka alama maelezo yasiyozuia, ili waandishi wajue mara moja nini lazima kibadilike dhidi ya nini ni pendekezo. Hilo huweka mapitio yakilenga usahihi na usanifu badala ya ladha.

3. **Nani lazima aidhinishe mabadiliko ya msimbo nyeti kwa usalama au unaohusiana na uzingatiaji, na uelekezaji huo unatekelezwaje?** Sura hii inaeleza idhini za kijukumu, kanuni za umiliki wa msimbo, na mgawanyo wa majukumu ambapo hakuna mtu mmoja anayedhibiti badiliko zima nyeti, huku idhini ikirekodiwa kama ushahidi wa ukaguzi. Katika mazingira ya mashirika makubwa na ya serikali hivi ni udhibiti unaohitajika, na hatari ni kwamba ama vinarukwa au vinageuka kikwazo kinachogandisha utoaji. Leta ishara: moduli zipi ni nyeti, na kama kanuni za umiliki zinaelekeza sasa mabadiliko hayo kwa waidhinishaji sahihi kiotomatiki. Weka uelekezaji katika usanidi wa umiliki wa msimbo na uuoanishe na ukaguzi wa kiotomatiki na mabadiliko madogo, ili udhibiti utimizwe bila foleni ya mlinzi wa lango wa binadamu. Amua hili kwa makusudi badala ya kugundua pengo wakati wa ukaguzi.

4. **Lengo la ucheleweshaji wa mapitio mliloliafikiana kweli ni lipi, na je, mnalipima na kulitekeleza, au ni matamanio tu?** Sura inachukulia ucheleweshaji wa mapitio kama gharama ya timu nzima na inakuomba ufuatilie muda hadi mapitio ya kwanza na muda hadi kuunganishwa, ukichukulia ucheleweshaji endelevu kama tatizo la mchakato badala ya kasoro ya mtu binafsi. Katika timu kubwa foleni ya mapitio isiyo na mmiliki hutoza kila mtu kimyakimya: waandishi hukusanya mabadiliko makubwa zaidi kuepuka kusubiri, mabadiliko hayo kisha hupata mapitio ya juujuu zaidi, na muda wa kuongoza wa utoaji unapanda bila mhusika mmoja. Jambo linaloshindana ni kwamba lengo gumu la ucheleweshaji linaweza kuwasukuma wahakiki kupitia haraka, kwa hiyo kasi na kina lazima visawazishwe badala ya kubadilishwa kwa upofu. Leta ushahidi: mgawanyo wenu wa sasa wa muda hadi mapitio ya kwanza, jinsi unavyotofautiana kwa timu na kwa ukubwa wa badiliko, na mahali mapitio yanakaa muda mrefu zaidi. Katika mazingira ya mashirika makubwa na ya serikali, funga lengo na vipimo vya mtiririko ambavyo uongozi unafuatilia tayari, kwa sababu udhibiti wa wahakiki wengi wa lazima bila kanuni ya ucheleweshaji unakuwa kikwazo kinachogandisha utoaji na kuwashawishi watu kuzunguka udhibiti kabisa.

5. **Kwa aina zipi za mabadiliko mnaamini mapitio ya kiotomatiki na yanayosaidiwa na AI, na binadamu lazima abaki anawajibika wapi?** Sura inasema chukulia pato la mapitio ya AI kama ingizo, si mamlaka: imara kwa masuala ya juujuu na uthabiti, hafifu kwa busara ya kina ya usanifu na muktadha wa mfumo, huku binadamu akiwajibika kwa kila idhini. Bila mpaka wazi, timu kubwa huteleza kuelekea kuamini kupita kiasi, ambapo maoni ya kijani ya roboti husomwa kama mapitio yaliyopita na hatari halisi za usanifu na usalama zinateleza chini ya kujiamini kwa uongo. Mvuto unaoshindana ni kwamba mapitio ya AI hupunguza mzigo kweli na hunasa kasoro za kawaida bila kuchoka, kwa hiyo kuyapiga marufuku kunapoteza kiegemeo. Leta ushahidi: mahali mapendekezo ya kiotomatiki yamenasa masuala halisi, mahali yamezalisha kelele, na aina zipi za mabadiliko (nyeti kwa usalama, zinazohusiana na uzingatiaji, za usanifu) ambazo kamwe hungeruhusu mashine kuidhinisha peke yake. Kwa kazi ya mashirika makubwa na ya serikali, taja nani anashikilia uwajibikaji kwa idhini wakati msaidizi wa AI alikuwa kwenye mzunguko, kwa sababu ukaguzi utauliza nani alipitia badiliko, na "zana ilifanya" si jibu ambalo mdhibiti anakubali.

6. **Kuoanishwa au kufanya kazi kama kundi kunapaswa kuchukua nafasi ya mapitio yasiyo ya wakati mmoja wapi, na unatumiaje mapitio kupunguza hatari ya bus-factor kwa makusudi?** Sura inaweka kuoanishwa na kufanya kazi kama kundi kama mapitio endelevu yaliyochaguliwa kwa muktadha, na inataja mapitio kama utaratibu unaoeneza maarifa ili hakuna sehemu ya mfumo inayoeleweka na mtu mmoja tu. Yakiachwa bila kutajwa, maarifa hukusanyika: mtaalamu yuleyule hupitia kila badiliko la mfumo mdogo, mapitio hugeuka muhuri wa mpira kwa sababu hakuna mwingine anayeweza kumpinga, na hatari ya bus-factor hukua hasa mfumo ulipo muhimu zaidi. Jambo linaloshindana ni gharama, kwa kuwa kufanya kazi kama kundi hutumia muda wa timu nzima na kuoanishwa hufunga wahandisi wawili, kwa hiyo huwezi kuamuru kila mahali. Leta ushahidi: moduli zipi zina mhakiki mmoja tu anayeaminika, utambulisho unakwama wapi, na eneo gumu lingenufaika wapi na kikao cha moja kwa moja badala ya nyuzi za maoni. Katika shirika kubwa au la umma, chukulia kuenea kwa maarifa kwa makusudi kama usimamizi wa hatari, kwa sababu mfumo wa muda mrefu ambao sehemu zake muhimu zinamtegemea mtu mmoja ni dhima ya kiuendeshaji na ya mwendelezo, si usumbufu wa wafanyakazi tu.

## Mtazamo wa sekta

**Kampuni changa.** Ukiwa na wahandisi watatu au wanne, weka mapitio mepesi: idhini ya mwenzako mmoja kwenye ombi dogo la kuvuta, ukaguzi wa kimitambo kwenye CI, na hakuna mhakiki wa pili wa lazima atakayekwamisha uunganishaji. Lengo halisi ni kidogo uzingatiaji na zaidi kuhakikisha zaidi ya mtu mmoja anaelewa kila sehemu ya mfumo, kwa hiyo oanisha kwenye vipande hatarishi na uchukulie hilo kama utambulisho. Usijenge uelekezaji mzito wa umiliki wa msimbo utakaoukuza hivi karibuni; kanuni ya pamoja ya mabadiliko madogo, yaliyoelezwa vizuri hununua faida nyingi kwa gharama karibu hakuna.

**Biashara ndogo.** Hakuna uwezekano una mtaalamu wa zana za mapitio, kwa hiyo tegemea kile jukwaa lako la kuhifadhi (kwa mfano huduma ya Git inayosimamiwa) linachotoa tayari badala ya kujenga uendeshaji wa kiotomatiki maalumu. Nunua miunganisho ya linting, majaribio, na uchanganuzi wa usalama badala ya kuidumisha, ili wahandisi wako wachache watumie dakika zao adimu za mapitio kwa usanifu na usahihi. Weka kanuni moja rahisi, kila badiliko linapata jozi nyingine ya macho, na upinge kuongeza mchakato ambao huna mtu wa kuudumisha.

**Biashara kubwa.** Changamoto ni uthabiti kuvuka timu nyingi: viwango vya pamoja, kanuni za umiliki wa msimbo zinazoelekeza mabadiliko nyeti kwa waidhinishaji sahihi, na idhini za kijukumu zilizorekodiwa kama ushahidi wa ukaguzi. Otomatisha ukaguzi wa kimitambo shirika zima ili mapitio ya binadamu yalenge usanifu, na ufuatilie ucheleweshaji wa mapitio kama kipimo cha mtiririko ili udhibiti wa wahakiki wengi wa lazima usiwe kikwazo kimyakimya. Linganisha kina cha mapitio na hatari ya badiliko kwa sera iliyoandikwa, ili mabadiliko madogo yabaki ya haraka huku hatarishi yakipata mgawanyo wa majukumu na uchunguzi wa kina.

**Serikali.** Udhibiti wa mabadiliko mara nyingi ni wa lazima: kila badiliko la uzalishaji limepitiwa na kuidhinishwa na mtu mwingine zaidi ya mwandishi, rekodi ikihifadhiwa kama ushahidi wa ukaguzi kutimiza mahitaji ya mgawanyo wa majukumu. Pendelea njia ya uwazi, inayofuatilika ya nani aliandika, nani aliidhinisha, na ukaguzi gani ulipita, na uwekeze katika uendeshaji wa kiotomatiki na mabadiliko madogo, ya mara kwa mara ili udhibiti usigandishe utoaji. Zana za mapitio zinaponunuliwa, dai kumbukumbu za ukaguzi zinazoweza kusafirishwa na uepuke kufungwa, kwa kuwa ushahidi lazima udumu kuliko muuzaji yeyote na kuhimili uchunguzi wa umma.

## Mifano

**Kampuni changa.** Kampuni changa ya wahandisi wanne inaweka kila ombi la kuvuta dogo na kuomba idhini ya mwenzake mmoja kabla ya kuunganisha, si kwa uzingatiaji sana bali kuhakikisha hakuna mtu mmoja ambaye ndiye pekee anayeelewa sehemu ya mfumo. CI inaendesha kipanga muundo na majaribio, kwa hiyo binadamu wanatumia dakika zao chache za mapitio kwa usanifu na usahihi badala ya nafasi. Timu inapogonga kipande kigumu cha mtiririko wa malipo, wawili wao wanaoanisha juu yake badala ya kubadilishana maoni yasiyo ya wakati mmoja, jambo linalofanya pia kazi ya utambulisho kwa mwajiriwa mpya.

**Biashara kubwa.** Kampuni kubwa ya programu inahitaji angalau mapitio moja ya kuidhinisha kwenye kila badiliko, pamoja na idhini ya pili kwa mabadiliko ya moduli nyeti kwa usalama zilizotambuliwa na kanuni za umiliki wa msimbo. CI inashughulikia ukaguzi wote wa mtindo na majaribio, kwa hiyo wahakiki wanazingatia usanifu na usahihi. Timu inafuatilia muda hadi mapitio ya kwanza na kuchukulia wastani unaopanda kama ishara ya kusawazisha upya mzigo wa kazi. Wahandisi wapya wanatambulishwa kupitia kuoanishwa, jambo linalofupisha njia yao ya kuchangia kwa kujitegemea.

**Serikali.** Wakala wa kitaifa unaofanya kazi chini ya mahitaji makali ya udhibiti wa mabadiliko unaamuru kila badiliko la uzalishaji lipitiwe na kuidhinishwa na mtu mwingine zaidi ya mwandishi, idhini ikirekodiwa kwa ukaguzi. Ili kuzuia udhibiti huu usigeuke kikwazo, wakala unawekeza katika ukaguzi wa kiotomatiki na mabadiliko madogo, ya mara kwa mara, na kuweka kanuni ya kujibu mapitio siku hiyo hiyo. Njia ya mapitio, inayofunika nani aliandika, nani aliidhinisha, na ukaguzi gani ulipita, inakuwa sehemu ya ushahidi wa uzingatiaji kwa kila toleo, ikitimiza mahitaji ya mgawanyo wa majukumu bila kugandisha utoaji.

## Kesi ya biashara: sababu, ROI, na TCO

Mapitio ya msimbo hukulipa kwa sarafu tatu: kasoro zilizonaswa kabla ya uzalishaji, maarifa yaliyoenea kuvuka timu, na viwango vinavyodumishwa kiotomatiki kwa muda. Kunasa kasoro kwenye mapitio ni nafuu zaidi sana kuliko kuinasa kwenye uzalishaji, na faida ya kushiriki maarifa hupunguza hatari ya mtu-muhimu ambayo vinginevyo inaweza kuligharimu shirika sana mtu anapoondoka. Mapitio pia ni utaratibu wa kupitisha utamaduni unaoweka timu inayokua ikiwa na mshikamano.

Gharama ya mapitio ni muda wa mhandisi na ucheleweshaji fulani, vyote vinavyoweza kudhibitiwa kwa mazoea mazuri. Gharama ya *kutopitia*, au kupitia vibaya, inajumuisha kasoro za uzalishaji, maarifa yaliyotengwa, msimbo usio thabiti, na, katika mazingira yanayodhibitiwa, ukaguzi ulioshindwa na matokeo ya uzingatiaji. Mapitio mazito kupita kiasi pia yana gharama halisi: foleni ndefu, makundi makubwa, wahandisi waliokata tamaa. Kujenga hoja kwa uongozi, unganisha mazoea ya mapitio na kiwango cha kushindwa kwa mabadiliko, muda wa kuongoza wa utoaji, na kasi ya utambulisho, na ufuatilie ucheleweshaji wa mapitio kama kipimo wazi cha mtiririko.

## Mifumo mibaya na mitego

- **Muhuri wa mpira:** idhini bila uchunguzi halisi, zinazotoa uhakikisho wa uongo na kutimiza herufi ya udhibiti tu.
- **PR kubwa:** maelfu ya mistari inayoweza kupitiwa juujuu tu, ikihakikisha mapitio ya juujuu.
- **Mapitio ya mambo madogo tu:** kuzingatia mambo ya kipuuzi huku usanifu na usahihi vikikosekana, mara nyingi kwa sababu ukaguzi wa kimitambo haujawekwa kiotomatiki.
- **Mapitio kama ulinzi wa lango:** kutumia mapitio kudai ukuu au kuwazuia wengine, kutia sumu ushirikiano.
- **Foleni ya polepole:** mapitio yanayokaa siku, kukwamisha utoaji na kuhimiza kukusanya.
- **Kuamini mapitio ya AI kupita kiasi:** kuchukulia mapendekezo ya kiotomatiki kama mamlaka na kuacha busara ya binadamu kwa mabadiliko hatarishi.
- **Kuzuia kwa upendeleo:** kuwasilisha maoni ya mtindo wa kibinafsi kama mabadiliko yanayohitajika bila kuyatofautisha na kasoro halisi.

## Kielelezo cha ukomavu

- **Ngazi ya 1, Kuanzisha:** Mapitio ni ya papo hapo na ya kuitikia. Mara nyingi yanarukwa au kufanywa bila uthabiti, masuala ya kimitambo yanatawala maoni, kanuni za maoni hazijawekwa, na njia yoyote ya idhini ni ya bahati badala ya makusudi.
- **Ngazi ya 2, Kuendeleza:** Mazoea ya msingi ya mapitio yapo lakini yanatofautiana timu hadi timu. Mapitio yanahitajika mahali fulani na ni ya polepole au ya hiari pengine, uendeshaji wa kiotomatiki ni wa sehemu, na ukubwa na ubora wa PR hubadilika sana bila matarajio ya pamoja.
- **Ngazi ya 3, Kusawazisha:** Viwango vimeandikwa na kutekelezwa shirika zima. PR ndogo zilizolenga, muundo wa kiotomatiki, linting, majaribio na uchanganuzi wa usalama kwenye CI, orodha hakiki wazi, desturi wazi ya kuzuia dhidi ya pendekezo, na kanuni za umiliki wa msimbo zinazoelekeza mabadiliko nyeti kwa waidhinishaji sahihi.
- **Ngazi ya 4, Kusimamia:** Mapitio yanapimwa na kudhibitiwa dhidi ya vipimo vya msingi. Muda hadi mapitio ya kwanza, muda hadi kuunganishwa, kina cha mapitio dhidi ya hatari ya badiliko, kiwango cha kasoro zinazotoroka, na kiwango cha kushindwa kwa mabadiliko vinafuatiliwa; ucheleweshaji endelevu unachukuliwa kama tatizo la mchakato; na data inaendesha mahali pa kusawazisha upya mzigo wa wahakiki na mahali udhibiti unapopunguza kasi ya utoaji bila kuongeza uhakikisho.
- **Ngazi ya 5, Kuratibu:** Mapitio yanaboreshwa kila wakati na kuunganishwa kuvuka shirika. Kina kinabadilika kulingana na hatari ya badiliko, kuoanishwa, kufanya kazi kama kundi na msaada wa AI vinatumika kwa makusudi na binadamu anayewajibika, kuenea kwa maarifa na hatari ya bus-factor vinasimamiwa kwa makusudi, na mapitio yanaboresha kwa kupimika ubora, mtiririko wa utoaji, na utambulisho.

## Mawazo ya kujadili

- Lengo sahihi la ucheleweshaji wa mapitio kwa timu yenu ni lipi, na nini kinazuia kulifikia?
- Mnalinganishaje kina cha mapitio na hatari ya badiliko bila kuongeza urasimu?
- Kuoanishwa au kufanya kazi kama kundi kunashinda mapitio yasiyo ya wakati mmoja wapi katika muktadha wenu?
- Mapitio yanayosaidiwa na AI yanapaswa kuaminiwa kiasi gani, na kwa mabadiliko ya aina zipi?
- Mnaweka vipi maoni ya mapitio kuwa ya kujenga timu inapokua na kuwa tofauti zaidi?
- Mnatimizaje mahitaji ya idhini ya uzingatiaji bila kuunda vikwazo?

## Mambo muhimu ya kukumbuka

- Weka maombi ya kuvuta madogo na yaliyoelezwa vizuri; mwandishi anamiliki uwezo wa kupitiwa.
- Otomatisha ya kimitambo ili binadamu wapitie usanifu, usahihi, na majaribio.
- Fuatilia na usimamie ucheleweshaji wa mapitio kama gharama ya mtiririko wa timu nzima.
- Linganisha kina cha mapitio na hatari ya badiliko, na utofautishe masuala yanayozuia na mapendeleo.
- Tumia kuoanishwa, kufanya kazi kama kundi, na msaada wa AI kama nyongeza zinazofaa muktadha, ukiweka binadamu anayewajibika.

## Marejeo na usomaji zaidi

- Karl Wiegers, *Peer Reviews in Software: A Practical Guide*
- Google, *Engineering Practices: How to Do a Code Review* (as a reference exemplar)
- Nicole Forsgren, Jez Humble, Gene Kim, *Accelerate: The Science of Lean Software and DevOps*
- Kent Beck, *Extreme Programming Explained* (on pair programming)
- Woody Zuill, writings on mob programming
- Michael Lopp, *Managing Humans* (on engineering collaboration)
