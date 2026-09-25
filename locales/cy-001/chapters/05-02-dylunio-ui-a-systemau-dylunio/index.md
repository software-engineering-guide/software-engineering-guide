# 5.2 Dylunio UI a systemau dylunio

## Trosolwg a chymhelliant

Crefft siapio'r hyn y mae pobl yn ei weld ac yn ei gyffwrdd yw [dylunio rhyngwyneb defnyddiwr (UI)](https://en.wikipedia.org/wiki/User_interface_design): cynllun, [teipograffeg](https://en.wikipedia.org/wiki/Typography), lliw, bylchu, rheolaethau, a chyflyrau. Mae [system ddylunio](https://en.wikipedia.org/wiki/Design_system) yn cymryd y grefft honno ac yn ei throi'n ased a rennir, ailddefnyddiadwy, wedi'i lywodraethu: set ddogfennedig o egwyddorion, cydrannau, patrymau, a thocynnau y mae pob tîm yn tynnu ohoni, fel bod y cynnyrch cyfan yn edrych ac yn ymddwyn fel un. Mae dylunio UI yn penderfynu sut y dylai un sgrin edrych. Mae system ddylunio'n penderfynu sut mae deng mil o sgriniau ar draws llawer o dimau'n aros yn gydlynol.

I sefydliad mawr, y system ddylunio yw'r buddsoddiad ag effaith uchaf sengl mewn ansawdd UI a chyflymder danfon. Heb un, mae pob tîm yn ailddyfeisio botymau, ffurflenni, moddalau, a thrin gwallau, pob un ychydig yn wahanol, pob un yn cael ei gynnal ar wahân, pob un yn torri ar wahân. Mae defnyddwyr yn talu am hyn mewn dryswch ac anymddiriedaeth; mae'r busnes yn talu amdano mewn ymdrech ddyblyg ac ansawdd anwastad. Mae system ddylunio'n troi penderfyniadau dylunio un-tro yn gyfalaf ailddefnyddiadwy: datryswch [hygyrchedd](https://en.wikipedia.org/wiki/Accessibility), [ymatebolrwydd](https://en.wikipedia.org/wiki/Responsive_web_design), a brandio unwaith mewn cydran, ac mae pob tîm yn etifeddu'r canlyniad.

Mae menter a llywodraeth yn ychwanegu dwy bwysau benodol. Yn gyntaf, graddfa: mae angen i gannoedd o gymwysiadau, llawer wedi'u hadeiladu gan werthwyr neu eu caffael trwy uniadau, i gyd deimlo fel un sefydliad. Yn ail, hirhoedledd a newid: mae brandiau'n cael eu hadnewyddu, mae asiantaethau'n cael eu had-drefnu, a gall fod angen i un platfform wasanaethu sawl brand neu is-asiantaeth o un sylfaen god. Mae system ddylunio wedi'i phensaernïo'n dda, gyda themio a thocynneiddio priodol, yn gwneud y newidiadau ysgubol hyn yn drinadwy yn hytrach na trychinebus.

## Egwyddorion allweddol

- Mae cysondeb yn gostwng [llwyth gwybyddol](https://en.wikipedia.org/wiki/Cognitive_load); dylai botwm edrych ac ymddwyn yr un fath ym mhobman.
- Mae penderfyniadau dylunio'n asedau: daliwch nhw unwaith fel cydrannau a thocynnau ailddefnyddiadwy.
- Tocynnau yw'r ffynhonnell wirionedd ar gyfer penderfyniadau gweledol; mae cydrannau'n bwyta tocynnau, byth werthoedd wedi'u codio'n galed.
- Mae hygyrchedd ac ymatebolrwydd wedi'u hadeiladu i mewn i gydrannau, nid wedi'u bolltio ymlaen fesul sgrin.
- Mae system ddylunio'n gynnyrch â defnyddwyr (datblygwyr a dylunwyr), nid darn danfon un-tro.
- Mae hierarchaeth weledol yn arwain sylw: dylai teip, lliw, a lle wneud pwysigrwydd yn amlwg.
- Mae llywodraethu'n cadw system yn gydlynol; mae cyfraniad yn ei chadw'n fyw.

## Argymhellion

### Strwythurwch y system mewn haenau: tocynnau, cydrannau, patrymau

Mae tocynnau dylunio'n werthoedd wedi'u henwi, annibynnol-ar-blatfform ar gyfer lliw, bylchu, teipograffeg, radiws, dyrchafiad, a mudiant: y penderfyniadau atomig. Adeiladwch nhw mewn haenau: palet cyntefig (gwerthoedd crai), tocynnau semantig (`color-action-primary`, `space-inset-md`) sy'n cario ystyr, a thocynnau lefel-cydran lle mae eu hangen arnoch. Mae cydrannau'n bwyta'r tocynnau semantig, felly mae un newid yn lledaenu ym mhobman. Uwchben cydrannau mae patrymau: cyfansoddiadau profedig fel tabl data, ffurflen aml-gam, neu gyflwr gwag. Dogfennwch y tair haen i gyd mewn un lle, gydag enghreifftiau byw ac arweiniad defnydd.

### Ewch i'r afael â'r sylfeini gweledol yn iawn

Sefydlwch raddfa deipograffig gyda hierarchaeth glir a bylchu llinellau hael i alluogi darllenadwyedd, a chadwch at set gyfyngedig o feintiau a phwysau. Diffiniwch liw fel system, gyda digon o gyferbyniad ar gyfer hygyrchedd (gweler y bennod hygyrchedd) a rolau semantig, yn hytrach na lliwiau crai wedi'u gwasgaru trwy'r UI. Defnyddiwch raddfa bylchu a grid cynllun fel bod aliniad a rhythm yn aros yn gyson heb ddyfalu fesul sgrin. Dylai hierarchaeth weledol wneud y weithred gynradd a'r wybodaeth bwysicaf yn amlwg ar un olwg.

### Dyluniwch yn ymatebol ac yn symudol-yn-gyntaf

Dyluniwch ar gyfer y porthfan resymol lleiaf yn gyntaf, yna gwellwch ar gyfer sgriniau mwy. Mae hyn yn eich gorfodi i flaenoriaethu'r cynnwys a'r rheolaethau hanfodol. Defnyddiwch gynlluniau hylifol ac unedau cymharol fel bod rhyngwynebau'n addasu i unrhyw sgrin, yn hytrach na neidio rhwng ychydig o bwyntiau toriad sefydlog. Gwnewch dargedau cyffwrdd yn ddigon mawr, a sicrhewch fod rhyngweithiadau'n gweithio â chyffwrdd, llygoden, a bysellfwrdd. Mewn llywodraeth yn arbennig, tybiwch fod cyfran ystyrlon o'ch defnyddwyr ar ddyfeisiau bach, hŷn, neu gyllideb.

### Gwnewch drosglwyddiad dylunio-i-ddatblygu a phariti'n bryder dosbarth cyntaf

Nid yw system ddylunio'n talu ar ei ganfed ond pan fydd yr UI a ddanfonwyd yn cyfateb i'r dyluniad bwriadedig ac yn parhau i gyfateb. Anelwch at ffynhonnell wirionedd sengl: mae tocynnau wedi'u hallforio o'r offeryn dylunio'n bwydo'n uniongyrchol i mewn i god, fel bod dylunwyr a pheirianwyr yn cyfeirio at yr un gwerthoedd. Darparwch lyfrgell cydrannau wedi'u codio y bydd peirianwyr mewn gwirionedd yn eu defnyddio, gyda'r un enwau a phropiau â'r cydrannau dylunio. Defnyddiwch brofi atchweliad gweledol (cymhariaeth awtomataidd o UI wedi'i rendro yn erbyn delweddau llinell sylfaen a gymeradwywyd) a gwiriadau adolygiad-dylunio i ddal drifft. A mesurwch "bariti dylunio-cod" fel metrig iechyd eglur: y gyfran o UI wedi'i adeiladu o gydrannau system yn erbyn cod un-tro.

### Cefnogwch themio a labelu-gwyn ar raddfa menter

Pensaernïwch ar gyfer sawl brand o'r dechrau os oes unrhyw siawns y bydd eu hangen arnoch. Am fod cydrannau'n bwyta tocynnau semantig, mae thema'n ddim ond set wahanol o werthoedd tocyn, felly mae adnewyddiad brand neu is-frand newydd yn dod yn newid data, nid ailysgrifennu cod. Cefnogwch themâu golau a thywyll, moddau cyferbyniad uchel, a brandio fesul tenant trwy'r un mecanwaith. Cadwch resymeg benodol-i-frand allan o gydrannau, a'i wthio i mewn i setiau tocynnau a ffurfweddiad yn lle hynny.

### Llywodraethwch y system fel cynnyrch

Rhowch dîm pwrpasol, map ffordd, fersiynu, log newid, a sianel gymorth i'r system ddylunio. Nodwch sut mae timau'n cyfrannu cydrannau newydd, a sut mae'r rheini'n cael eu hadolygu a'u dyrchafu. Cydbwyswch reolaeth ganolog (i gadw cydlyniad a hygyrchedd) â model cyfrannu (fel bod y system yn esblygu gydag anghenion go iawn yn hytrach na dod yn dagfa). Cyfathrebwch ddiddymiadau a mudo'n glir, a rhowch ddigon o amser arwain i dimau sy'n defnyddio'r system.

## Cyfnewidfeydd: manteision ac anfanteision

| Penderfyniad | Manteision | Anfanteision |
|---|---|---|
| Adeiladu system ddylunio | Cysondeb, cyflymder, hygyrchedd unwaith, ailfrandio haws | Cost ymlaen llaw a pharhaus, angen tîm pwrpasol |
| Mabwysiadu system barod | Cychwyn cyflym, patrymau profedig | Golwg generig, anos ffitio brand ac anghenion unigryw |
| Llywodraethu canolog llym | Cydlyniad, ansawdd, hygyrchedd wedi'u gwarantu | Gall dagu timau, teimlo'n fiwrocrataidd |
| Model cyfraniad agored | Yn esblygu gydag anghenion go iawn, perchnogaeth a rennir | Risg o ddrifft ac anghysondeb heb adolygiad |
| Tocynneiddio a themio trwm | Ailfrandio rhad a chefnogaeth aml-frand | Mwy o haniaethiad, tro dysgu serthach |

Mae systemau dylunio'n cyfnewid cost ymlaen llaw a llywodraethu am gysondeb a chyflymder tymor hir. Ar gyfer cynnyrch bach gydag un tîm, efallai na fydd yr uwchben yn talu ar ei ganfed. Ar gyfer sefydliad mawr gyda llawer o dimau a chynhyrchion hirhoedlog, nid y cwestiwn yw a ddylid cael system ond faint i'w fuddsoddi a sut i'w llywodraethu. Y difaru mwyaf cyffredin yw tan-fuddsoddi mewn llywodraethu ac offer pariti: mae'r system yn bodoli ar bapur, ond mae timau'n drifftio i ffwrdd oddi wrthi'n dawel.

## Cwestiynau i'w trafod gyda'ch tîm

1. **Sut mae ein pensaernïaeth tocynnau wedi'i haenu, ac a yw cydrannau wedi'u gwahardd rhag defnyddio gwerthoedd wedi'u codio'n galed?** Mae cyfanswm taledigrwydd system ddylunio (ailfrandio rhad, themio aml-frand, hygyrchedd wedi'i ddatrys unwaith) yn dibynnu ar gydrannau'n bwyta tocynnau semantig fel `color-action-primary` yn hytrach na lliwiau crai a gwerthoedd picsel wedi'u gwasgaru trwy god. Penderfynwch ar yr haenau nawr: palet cyntefig, tocynnau semantig sy'n cario ystyr, a thocynnau lefel-cydran dim ond lle mae eu gwir angen arnoch. Mae gor-haniaethiad yn risg go iawn, felly cytunwch faint o haenau sy'n ormod a sut mae datblygwr yn dod o hyd i'r tocyn cywir yn gyflym. Dewch â grep o liwiau a bylchu wedi'u codio'n galed ar draws eich sylfaen god fel tystiolaeth o ddrifft. Os yw rhesymeg brand wedi'i bobi i mewn i gydrannau, mae ailfrandio'n dod yn ailysgrifennu cod yn lle newid ffurfweddiad, sef y drychineb union y mae tocynneiddio'n bodoli i'w hatal.

2. **Sut rydym yn mesur ac yn amddiffyn pariti dylunio-cod, a pha offer sy'n dal drifft yn awtomatig?** Mae system ddylunio sy'n bodoli dim ond fel ffeil ddylunio'n ddalen sticer: mae peirianwyr yn ailadeiladu popeth beth bynnag ac mae'r UI a ddanfonwyd yn araf yn gwyro oddi wrth y bwriad. Cytunwch ar fetrig pariti eglur (y gyfran o UI wedi'i adeiladu o gydrannau system yn erbyn cod un-tro) a gwifrwch brofi atchweliad gweledol i mewn i CI fel bod sgriniau wedi'u rendro'n cael eu cymharu yn erbyn llinellau sylfaen a gymeradwywyd. Mae hyn yn bwysig ar raddfa menter a llywodraeth oherwydd bod angen i gannoedd o gymwysiadau, llawer wedi'u hadeiladu gan werthwyr neu eu hetifeddu trwy uniadau, deimlo fel un sefydliad. Dewch â'r rhif pariti cyfredol a rhestr o'r prif gydrannau pwrpasol y mae timau'n parhau i'w hailadeiladu. Os nad oes neb yn berchen ar y metrig na'r gyfres atchweliad, mae drifft eisoes yn ennill yn dawel.

3. **Sut rydym yn llywodraethu cyfraniad, diddymiad, a mudo fel nad yw'r system yn tagu timau nac yn dryllio?** Mae rheolaeth ganolog lym yn gwarantu cydlyniad a hygyrchedd ond gall droi'r tîm system ddylunio'n dagfa y mae timau'n llwybro o'i chwmpas; mae cyfraniad agored yn cadw'r system yn fyw ond mae'n risgio amrywiadau gwahanol heb adolygiad. Penderfynwch ar y llwybr cyfraniad: sut mae tîm yn cynnig cydran newydd, pwy sy'n ei hadolygu, a sut mae'n cael ei dyrchafu. Yn gyfartal, cytunwch sut rydych yn cyfathrebu newidiadau torri, oherwydd bod diddymiadau heb gymorth mudo ac amser arwain yn achosi i dimau sy'n defnyddio'r system stolio neu fforchio. Dewch ag enghreifftiau o gydrannau y mae timau wedi'u hadeiladu y tu allan i'r system a gofynnwch pam na wnaethant gyfrannu'n ôl. Fel arfer mae'r ateb yn datgelu a yw eich llywodraethu'n wasanaeth neu'n rwystr.

4. **Sut rydym yn gwarantu bod hygyrchedd yn cael ei ddatrys unwaith y tu mewn i gydrannau, a beth sy'n stopio tîm rhag danfon un anhygyrch un-tro?** Y ddadl gryfaf dros system ddylunio yw bod cyferbyniad lliw, cyflyrau ffocws, gweithrediad bysellfwrdd, a semanteg darllenydd sgrin yn cael eu datrys unwaith a'u hetifeddu ym mhobman, ond mae'r addewid hwnnw'n cwympo'r eiliad y mae timau'n rholio'u rheolaethau eu hunain â llaw. I sefydliad mawr, dyma lle mae'r risg gyfreithiol a risg enw da fwyaf yn eistedd, oherwydd gall un ffurflen daliadau neu ddewisydd dyddiad anhygyrch rwystro defnyddwyr go iawn a sbarduno cwynion ar draws pob cynnyrch a'i copïodd. Pwyswch orfodaeth ganolog (cydrannau hygyrch ynghyd â leinsiwr neu giât adolygu sy'n gwrthod marcio crai) yn erbyn ymreolaeth tîm, a phenderfynwch lle mae'r llinell galed. Dewch â chanlyniadau archwiliad hygyrchedd, rhestr o gydrannau gyda'u statws cydymffurfio, a chyfrif o reolaethau pwrpasol y mae timau wedi'u hailadeiladu y tu allan i'r system. Mewn lleoliadau menter a llywodraeth nid manylder yw hyn: mae rhwymedigaethau fel WCAG, Adran 508, ac EN 301 549 yn gwneud cydymffurfiaeth yn ofyniad caffael ac archwilio, felly mae llyfrgell cydrannau â chydymffurfiaeth ddogfennedig yn ased cydymffurfiaeth ynddo'i hun.

5. **Faint o frandiau, tenantiaid, a themâu y mae'n rhaid i'r system hon eu gwasanaethu, ac a ydym wedi pensaernïo haen y tocynnau ar gyfer hynny nawr yn hytrach na'i hôl-osod yn ddiweddarach?** Mae themio'n rhad os gwnaethoch chi ddylunio ar ei gyfer ac yn greulon os na wnaethoch chi, oherwydd bod brand neu denant na ragwelwyd erioed yn gorfodi rhesymeg brand yn ôl i mewn i gydrannau ac yn dadwneud holl bwynt tocynneiddio. I dîm mawr mae'r penderfyniad hwn yn siapio blynyddoedd o waith: mae platfform y mae'n rhaid iddo wasanaethu sawl brand, thema olau a thywyll, modd cyferbyniad uchel, a brandio fesul tenant angen haen tocynnau semantig sy'n ddigon glân fel bod thema'n ddim ond set wahanol o werthoedd. Cydbwyswch yr hyblygrwydd hwnnw yn erbyn gor-haniaethiad, gan fod coeden tocynnau nad oes neb yn gallu ei llywio'n fethiant ynddi'i hun. Dewch â map ffordd y brandiau a'r tenantiaid y gallwch eu rhagweld, cyfrif y themâu ar waith heddiw, ac unrhyw gydrannau sydd eisoes yn gollwng rhesymeg benodol-i-frand. Mewn cyd-destunau menter a llywodraeth mae uniadau, caffaeliadau, ac ad-drefniadau asiantaeth yn rheolaidd yn ychwanegu brandiau na wnaethoch gynllunio ar eu cyfer, felly mae pensaernïo ar gyfer aml-frand o'r dechrau'n wahaniaeth rhwng newid data ac ailysgrifennu aml-flwyddyn.

6. **Sut byddwn yn mudo cymwysiadau etifeddiaeth a rhai wedi'u hadeiladu gan werthwyr i mewn i'r system, a sut mae'r tîm system ddylunio'n cael ei ariannu fel ei fod yn goroesi'r cylch cyllideb nesaf?** Nid yw system ddylunio ond yn danfon ei henillion pan fydd cynhyrchion go iawn yn ei mabwysiadu, ac eto'r cymwysiadau anoddaf i'w trosi yw'r rhai hen a'r rhai wedi'u hallanoli sydd fwyaf o'i hangen, ac mae'r tîm sy'n cynnal y system yn aml y toriad cyntaf pan fydd cyllidebau'n tynhau. I sefydliad mawr rhaid i chi ddewis rhwng mudo byddin-fawr ac un cynyddrannol, a sut i gael gwerthwyr i adeiladu ar eich cydrannau yn hytrach nag o'u cwmpas. Dewch ag inventori o gymwysiadau gyda'u sgôr pariti cyfredol, amcangyfrif o ymdrech mudo fesul cymhwysiad, a'r lifiau contractiol sydd gennych dros werthwyr. Mewn lleoliadau menter a llywodraeth, ysgrifennwch gydymffurfiaeth system ddylunio i mewn i delerau caffael fel bod gwaith gwerthwr newydd yn glanio ar y system yn ddiofyn, ac ariannwch y tîm cynnal fel seilwaith a rennir parhaol, oherwydd mae system sy'n colli ei stiwardiaid mewn ad-drefniad yn drifftio'n ôl i wasgariad o fewn blwyddyn.

## Lens sector

**Cwmni newydd.** Gyda dau neu dri pheiriannydd a dim rhedfa i'w sbario, peidiwch ag adeiladu system a lywodraethir. Treuliwch ddiwrnod neu ddau'n diffinio set fach o docynnau semantig ar gyfer lliw, bylchu, a theip, ynghyd â dwsin o gydrannau a rennir, i gyd mewn un ffeil y mae'r tîm cyfan yn cyfeirio ati. Dibynnwch ar lyfrgell gyntefig barod ar gyfer y rhannau anodd, a chadwch ddim byd wedi'i godio'n galed fel bod eich ailfrandio go iawn cyntaf yn newid tocyn yn hytrach nag ailysgrifennu.

**Busnes bach.** Heb ddylunydd pwrpasol a chyllideb dynn, prynwch yn hytrach nag adeiladu: mabwysiadwch lyfrgell gydrannau neu git UI profedig a'i themio'n ysgafn i'ch brand. Eich nod yw cynnyrch cyson, hygyrch heb staffio tîm system ddylunio, felly ffafriwch system sy'n danfon hygyrchedd ac ymatebolrwydd yn y bocs. Gwrthsefwch yr ysfa i'w fforchio, oherwydd bod copi wedi'i deilwra na allwch ei gynnal yn dod yn rwystr y funud y mae'r prosiect ffynhonnell yn symud ymlaen.

**Menter.** Y broblem yw cydlyniad ar draws llawer o dimau a chynhyrchion hirhoedlog, felly triniwch y system ddylunio fel seilwaith a rennir wedi'i lywodraethu gyda thîm pwrpasol, fersiynu, a map ffordd. Traciwch bariti dylunio-cod fel metrig go iawn, gwifrwch brofi atchweliad gweledol i mewn i CI, a phensaernïwch haen y tocynnau ar gyfer sawl brand a thema o'r dechrau. Cyllidebwch gost llywodraethu a mudo'n benodol, a rheolwch fabwysiadu fel portffolio yn hytrach na chymryd yn ganiataol y bydd timau'n drifftio i mewn i'r system ar eu pen eu hunain.

**Llywodraeth.** Mae rheolau caffael, tryloywder, ac atebolrwydd cyhoeddus yn siapio pob dewis. Mae cydymffurfiaeth hygyrchedd â safonau fel WCAG, Adran 508, ac EN 301 549 yn ofyniad cyfreithiol, nid dewis, felly mae llyfrgell cydrannau â chydymffurfiaeth ddogfennedig yn dod yn ased cydymffurfiaeth. Ffafriwch neu ehangwch system ddylunio gyhoeddus a rennir fel bod dinasyddion yn cwrdd â'r un patrymau ar draws gwasanaethau, ysgrifennwch ddefnydd system ddylunio i mewn i gontractau gwerthwyr, a chyhoeddwch eich cydrannau ac arweiniad yn agored fel y gall asiantaethau a'u cyflenwyr eu mabwysiadu a chael eu dwyn i gyfrif drostynt.

## Enghreifftiau

**Cwmni newydd.** Roedd cwmni newydd dau beiriannydd yn parhau i ailadeiladu botymau a meysydd ffurflen ychydig yn wahanol ar bob sgrin newydd, ac roedd y cynnyrch yn dechrau edrych fel pe bai wedi'i wnïo at ei gilydd. Yn lle system drwm, treuliasant ddau ddiwrnod yn diffinio set fach o docynnau dylunio semantig ar gyfer lliw, bylchu, a theip, ynghyd ag oddeutu dwsin o gydrannau a rennir, i gyd mewn un ffeil y mae'r tîm cyfan yn cyfeirio ati. Am nad oedd dim byd wedi'i godio'n galed, pan gynigiodd eu penodiad cyntaf â meddwl dylunio balet lanach, roedd yr adnewyddiad yn newid tocyn a laniodd ar draws y ap mewn prynhawn yn lle llafur sgrin-wrth-sgrin.

**Menter.** Adeiladodd cwmni meddalwedd byd-eang â dwsinau o dimau cynnyrch system ddylunio docynneiddiedig gyda llyfrgell cydrannau wedi'i chodio a rennir. Roedd tocynnau semantig yn gadael iddynt ddanfon adnewyddiad brand llawn ar draws pob cynnyrch mewn wythnosau, yn lle llafur aml-flwyddyn fesul tîm, oherwydd bod y newid yn set tocyn newydd yn hytrach na miloedd o olygiadau lliw wedi'u codio'n galed. Cododd pariti dylunio-cod, wedi'i dracio fel metrig dangosfwrdd, wrth i dimau ddisodli cydrannau pwrpasol, a dorrodd gynnal UI dyblyg.

**Llywodraeth.** Creodd llywodraeth genedlaethol system ddylunio gyffredin ar gyfer gwasanaethau cyhoeddus (cydrannau, patrymau, a hygyrchedd a rennir wedi'u hadeiladu i mewn) a orfodir ar draws asiantaethau. Mae dinesydd sy'n symud rhwng gwasanaeth treth, gwasanaeth iechyd, a gwasanaeth trwyddedu'n cwrdd â'r un pennyn, rheolaethau ffurflen, a phatrymau gwall, sy'n adeiladu ymddiriedaeth ac yn byrhau'r cromlin ddysgu. Mae asiantaethau a'u gwerthwyr yn danfon yn gyflymach ac yn fwy hygyrch oherwydd bod y problemau anodd wedi'u datrys yn ganolog, a gall y llywodraeth ddiweddaru arweiniad neu drwsio hygyrchedd unwaith a'u cael i ledaenu ym mhobman.

## Achos busnes: cymhellion, ROI, a TCO

Daw ROI system ddylunio o ddileu dyblygu a chyflymu danfon. Yn lle pob tîm yn dylunio ac yn adeiladu'r un cydrannau, maent yn cyfansoddi o lyfrgell a rennir, sy'n cyflymu danfon yn fesuradwy ac yn rhyddhau dylunwyr a pheirianwyr ar gyfer gwaith penodol-i-gynnyrch. Mae hygyrchedd ac ymatebolrwydd, wedi'u datrys unwaith mewn cydrannau, yn eich arbed y gost adfer fesul prosiect. Mae ailfrandio a themio a arferai gymryd blynyddoedd bellach yn cymryd wythnosau.

Ar TCO, mae cost mabwysiadu'n dîm pwrpasol, offer, a'r ymdrech i gynhyrchion presennol fudo i mewn i'r system. Mae cost peidio â mabwysiadu'n cael ei thalu'n barhaus: adeiladu a chynnal dyblyg ar draws timau, UIs anghyson ac anhygyrch sy'n creu risg cymorth a chyfreithiol, ac ailfrandio araf, drud. Am fod y dyblygu'n cael ei wasgaru ar draws cyllidebau llawer o dimau, mae'n hawdd ei anwybyddu: mae system ddylunio'n gwneud y gost gudd honno'n weladwy ac yn ei chapio mewn un lle.

I wneud yr achos i arweinyddiaeth, meintioli'r gwaith cydran dyblyg ar draws timau, yr enillion amser-i'r-farchnad o gyfansoddi, a chost a hyd eich ailfrandio diwethaf yn erbyn yr hyn y byddai system docynneiddiedig yn ei ganiatáu. Fframiwch y system fel seilwaith a rennir gyda metrig mabwysiadu mesuradwy (canran pariti), fel y gellir tracio ei gwerth dros amser yn hytrach na'i honni'n unig.

## Gwrth-batrymau a pheryglon

- **System ddylunio fel dalen sticer**: ffeil ddylunio statig heb gydrannau wedi'u codio, felly mae peirianwyr yn ailadeiladu popeth beth bynnag.
- **Gwerthoedd wedi'u codio'n galed ym mhobman**: lliwiau a bylchu wedi'u gwasgaru trwy god, gan wneud themio ac ailfrandio'n amhosibl.
- **Dim llywodraethu**: mae'r system yn dryllio wrth i dimau ychwanegu amrywiadau gwahanol; mae cysondeb yn erydu.
- **Llywodraethu heb gyfraniad**: mae'r tîm canolog yn dod yn dagfa ac mae timau'n llwybro o'i chwmpas.
- **Anwybyddu pariti**: mae'r UI wedi'i godio'n gwyro oddi wrth y bwriad dylunio ac nid oes neb yn mesur y bwlch.
- **Gor-haniaethiad**: cymaint o docynnau a haenau fel nad oes neb yn gallu dod o hyd i'r un cywir na'i defnyddio.
- **Rhesymeg brand wedi'i bobi i mewn i gydrannau**: yn gwneud aml-frand a themio'n ailysgrifennu cod yn lle newid ffurfweddiad.
- **Newidiadau torri heb gymorth mudo**: mae timau sy'n defnyddio'r system yn stolio neu'n fforchio'r system.

## Model aeddfedrwydd

**Lefel 1: Cychwyn.** Mae pob tîm yn adeiladu ei UI ei hun ad hoc ac yn adweithiol. Dim cydrannau a rennir, golwg ac ymddygiad anghyson, lliwiau a bylchu wedi'u codio'n galed fesul sgrin. Mae pob ailfrandio'n llafur sgrin-wrth-sgrin â llaw.

**Lefel 2: Datblygu.** Mae canllaw arddull neu lyfrgell cydrannau a rennir yn bodoli ond yn rhannol, yn ddewisol, ac yn aml allan o sync rhwng dylunio a chod. Mae rhai timau'n ei ddefnyddio, eraill ddim, ac mae arferion sylfaenol yn amrywio'n eang o dîm i dîm.

**Lefel 3: Safoni.** Mae system ddylunio docynneiddiedig gyda llyfrgell wedi'i chodio, dogfennaeth, a llywodraethu wedi'i chynnal yn cael ei dogfennu a'i gorfodi ar draws y sefydliad cyfan. Mae cydrannau'n bwyta tocynnau semantig, cefnogir themio, a mae hygyrchedd ac ymatebolrwydd wedi'u hadeiladu i mewn yn hytrach na'u bolltio ymlaen fesul sgrin.

**Lefel 4: Rheoli.** Mae'r system yn cael ei mesur a'i rheoli gyda data yn erbyn llinellau sylfaen. Mae pariti dylunio-cod yn cael ei dracio fel metrig eglur gyda thargedau fesul cynnyrch, mae profi atchweliad gweledol yn rhedeg mewn CI i ddal drifft, a mesurir cydymffurfiaeth hygyrchedd yn erbyn safonau yn hytrach na'i chymryd yn ganiataol. Mae dangosfyrddau mabwysiadu'n dangos cwmpas cydrannau fesul tîm, a chofnodir cost a hyd ailfrandio fel bod gwelliant yn weladwy dros amser.

**Lefel 5: Cerddorfa.** Mae'r system ddylunio'n gynnyrch sy'n gwella'n barhaus, wedi'i integreiddio ar draws y sefydliad ac yn addasol i newid. Mae ganddi fersiynu, map ffordd, a model cyfraniad gweithredol, felly mae'n esblygu gydag anghenion go iawn. Mae ailfrandio a themâu newydd yn newidiadau tocyn arferol, mae themio aml-frand ac aml-denant yn normal, ac mae'r tîm yn ymddeol, yn ail-gwmpasu, ac yn dyrchafu patrymau ar sail tystiolaeth o ddata defnydd, gan fwydo offer dylunio a phiblinellau danfon o ffynhonnell wirionedd sengl.

## Syniadau ar gyfer trafod

- Sut rydych yn cydbwyso llywodraethu canolog yn erbyn ymreolaeth tîm heb naill ai dryllio na thagu?
- Beth yw'r metrig cywir ar gyfer "pariti dylunio-cod," a sut rydych yn ei gadw'n onest?
- Pryd y dylid caniatáu i dîm adeiladu cydran un-tro yn lle defnyddio'r system?
- Sut rydych yn ariannu ac yn staffio system ddylunio fel ei bod yn goroesi cylchoedd cyllideb ac ad-drefniadau?
- Faint o hyblygrwydd themio sy'n werth y gost haniaethiad ychwanegol?
- Sut rydych yn mudo cymwysiadau etifeddiaeth a rhai wedi'u hadeiladu gan werthwyr i mewn i system a rennir?

## Casgliadau allweddol

- Mae system ddylunio'n troi penderfyniadau dylunio un-tro'n gyfalaf ailddefnyddiadwy, wedi'i lywodraethu.
- Strwythurwch hi mewn haenau (tocynnau, cydrannau, patrymau), gyda chydrannau'n bwyta tocynnau semantig.
- Adeiladwch hygyrchedd ac ymatebolrwydd i mewn i gydrannau fel bod pob tîm yn eu hetifeddu.
- Triniwch bariti dylunio-cod fel metrig iechyd mesuradwy, nid tybiaeth.
- Mae tocynneiddio'n gwneud ailfrandio a themio aml-frand yn newid data, nid ailysgrifennu.
- Llywodraethwch y system fel cynnyrch gyda map ffordd, fersiynu, a model cyfraniad.
- Ar raddfa menter a llywodraeth, system a rennir yw'r buddsoddiad UI ag effaith uchaf sydd ar gael.

## Cyfeiriadau a darllen pellach

- Brad Frost, *Atomic Design*
- Alla Kholmatova, *Design Systems: A Practical Guide to Creating Design Languages*
- Josef Müller-Brockmann, *Grid Systems in Graphic Design*
- Robert Bringhurst, *The Elements of Typographic Style*
- Ellen Lupton, *Thinking with Type*
- Luke Wroblewski, *Mobile First*
- Ethan Marcotte, *Responsive Web Design*
- Nathan Curtis, ysgrifau ar docynnau dylunio a llywodraethu systemau dylunio
- W3C Design Tokens Community Group, manyleb fformat
- Systemau dylunio llywodraeth (e.e., UK Government Design System, U.S. Web Design System) fel gweithrediadau cyfeirio
