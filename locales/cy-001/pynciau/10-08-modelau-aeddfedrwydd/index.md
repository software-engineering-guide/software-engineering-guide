# 10.8 Modelau aeddfedrwydd

## Trosolwg a chymhelliant

Mae [model aeddfedrwydd](https://en.wikipedia.org/wiki/Maturity_model) yn ffordd strwythuredig o asesu pa mor alluog a chyson yw eich arfer mewn rhyw barth, ac o ddisgrifio llwybr ar gyfer ei wella. Mae'n diffinio ysgol fach o lefelau. Ar y gwaelod, mae'r gwaith yn ad hoc ac yn adweithiol. Ar y brig, mae'n cael ei fesur, ei reoli, ac yn optimeiddio'n barhaus. Mae gan bob gris nodweddion arsylwadwy y gallwch eu gwirio yn eu herbyn.

Mae modelau aeddfedrwydd yn troi cwestiwn annelwig ("ydyn ni'n dda am hyn?") yn ateb ailadroddadwy ("rydym ar lefel 2 yma, lefel 4 yno, a dyma beth fyddai ei angen ar gyfer lefel 3"). Mae'r llyfr hwn yn defnyddio model pum-lefel ym mhob pennod ac yn eu cyfuno ym mhennod 12.4. Mae'r bennod hon yn ymwneud â'r ddisgyblaeth ei hun: sut mae'r modelau'n gweithio, pryd maen nhw'n helpu, a sut maen nhw'n camarwain.

Mae'r rheswm eu bod yn bwysig yn syml. Ni all sefydliadau mawr wella'r hyn na allant ei weld. Ar draws dwsinau o dimau, mae gallu'n amrywio'n enfawr ac yn anweledig. Mae gan rai timau brofi ardderchog a diogelwch gwan; mae gan eraill y gwrthwyneb. Mae model aeddfedrwydd yn rhoi geirfa a rennir a llathen gyffredin i chi, fel bod bylchau'n dod yn gymharadwy, y gellir blaenoriaethu buddsoddiad, ac y gellir olrhain cynnydd dros amser yn hytrach na dim ond ei honni. Mae enghreifftiau adnabyddus yn cynnwys CMMI ([Capability Maturity Model Integration](https://en.wikipedia.org/wiki/Capability_Maturity_Model_Integration), ar gyfer proses), model DORA ([DevOps Research and Assessment](https://en.wikipedia.org/wiki/DevOps_Research_and_Assessment)) (perfformiad cyflenwi meddalwedd), OWASP SAMM (Software Assurance Maturity Model) a BSIMM (Building Security In Maturity Model) ar gyfer diogelwch meddalwedd, TMMi (Test Maturity Model integration, ar gyfer profi), model Agile Fluency, a modelau aeddfedrwydd rheoli data, ynghyd â chardiau sgorio mewnol di-rif.

I fentrau ac yn arbennig i lywodraeth, mae modelau aeddfedrwydd yn cario pwysau arbennig. Mae contractio llywodraethol wedi defnyddio lefelau arfarniad CMMI ers amser maith fel cymhwyster cyflenwr, ac mae fframweithiau fel CMMC UDA ([Cybersecurity Maturity Model Certification](https://en.wikipedia.org/wiki/Cybersecurity_Maturity_Model_Certification)) yn clymu aeddfedrwydd seiberddiogelwch yn uniongyrchol at gymhwysedd ar gyfer gwaith amddiffyn. Mae hynny'n rhoi dannedd gwirioneddol i fodelau aeddfedrwydd. Mae hefyd yn creu prif risg y bennod hon: pan fydd lefel yn dod yn giât neu'n darged, mae pobl yn optimeiddio ar gyfer yr arfarniad yn hytrach na'r gallu sylfaenol. Wedi'i ddefnyddio'n dda, mae modelau aeddfedrwydd yn ddrych. Wedi'i ddefnyddio'n wael, maent yn theatr.

## Egwyddorion allweddol

- **Modd yw aeddfedrwydd, nid diben.** Y nod yw gallu a chanlyniadau, nid rhif lefel.
- **Aseswch i ddysgu, nid i sgorio.** Mae hunanasesiad gonest yn curo arfarniad gwenieithus.
- **Nid yw uwch bob amser yn well.** Mae'r targed cywir yn dibynnu ar risg, cyd-destun, a chost.
- **Mesurwch fesul parth, nid un radd fyd-eang.** Mae gallu'n anwastad; mae un rhif yn ei guddio.
- **Blaenoriaethwch y bylchau aeddfedrwydd-isaf, risg-uchaf yn gyntaf.**
- **Gwyliwch am [Gyfraith Goodhart](https://en.wikipedia.org/wiki/Goodhart%27s_law).** Unwaith y bydd lefel yn darged, mae'n peidio â mesur gallu.
- **Ailasesiwch yn gyfnodol.** Mae aeddfedrwydd yn drifftio wrth i bobl, systemau, a bygythiadau newid.

## Argymhellion

### Dewiswch y model cywir ar gyfer y parth

Cyfatebwch y model â'r gallu rydych am ei wella, a ffafriwch fodelau sefydledig, seiliedig-ar-dystiolaeth dros rai a ddyfeisiwyd lle maent yn bodoli:

- **Proses a chyflenwi:** CMMI (aeddfedrwydd proses eang), model gallu DORA (perfformiad cyflenwi, wedi'i seilio ar ymchwil, pennod 11.2).
- **Diogelwch:** OWASP SAMM a BSIMM (arferion diogelwch meddalwedd), CMMC (seiberddiogelwch amddiffyn).
- **Profi ac ansawdd:** TMMi.
- **Ystwyth a ffyrdd o weithio:** model Agile Fluency (pennod 10.7).
- **Data:** modelau aeddfedrwydd rheoli data (DMM, DCAM).

Ar gyfer defnydd mewnol, mae graddfa syml pedwar neu bum lefel a gymhwysir fesul gallu (fel y mae'r llyfr hwn yn ei wneud) yn aml yn fwy gweithredadwy na fframwaith allanol trwm. Cadwch fodelau ffurfiol, wedi'u harfarnu ar gyfer lle maent yn ofynnol yn gontractiol.

### Aseswch yn onest ac fesul gallu

Rhedwch asesiadau sy'n cynhyrchu gwirionedd, nid cysur. Cynhwyswch y bobl sy'n gwneud y gwaith. Casglwch dystiolaeth yn hytrach na barn. Sgoriwch bob gallu ar wahân, fel bod y darlun yn adlewyrchu realiti: cryf yma, gwan yno. Mae hunanasesiad a ddefnyddir i lywio gwelliant yn werth mwy nag arfarniad allanol a ddefnyddir i ennill bathodyn, oherwydd mae'r cyntaf yn gwobrwyo didwylledd a'r ail yn gwobrwyo cyflwyniad. Mae pennod 12.4 yn darparu hunanasesiad cyfun ar draws pob parth yn y llyfr hwn; defnyddiwch ef fel offeryn cychwynnol.

### Defnyddiwch aeddfedrwydd i flaenoriaethu, nid i gosbi

Allbwn asesiad yw ôl-groniad gwelliant wedi'i flaenoriaethu, nid cerdyn adroddiad ar gyfer bai. Cyfunwch aeddfedrwydd â risg. Gall gallu lefel-1 mewn ardal risg-isel fod yn iawn. Mae gallu lefel-2 mewn ardal ddiogelwch- neu gydymffurfiaeth-dyngedfennol yn frys. Cyfeiriwch fuddsoddiad at y bylchau lle mae aeddfedrwydd isel yn cwrdd â risg uchel, a chysylltwch y gwaith â chanlyniadau (pennod 11.1) fel bod gwelliant yn cael ei fesur gan ganlyniadau, nid drwy ddringo'r ysgol er ei mwyn ei hun.

### Gosodwch lefelau targed yn fwriadol: nid yw uwch yn rhad

Mae pob lefel i fyny'n costio ymdrech ac yn aml yn ychwanegu pwysau proses. Anaml y mae'r targed cywir yn "lefel 5 ym mhobman." Y lefel lle mae'r gallu ychwanegol yn dal i gyfiawnhau'r gost ychwanegol ar gyfer risg y parth hwnnw ydyw. Efallai bod angen y gwreiddiau uchaf yn wirioneddol ar allu rheoleiddiedig a diogelwch-dyngedfennol, ac mae archwiliad yn aml yn mynnu o leiaf lefel 3 "wedi'i ddiffinio." Mae llawer o rai eraill wedi'u gwasanaethu'n dda ar lefel 3 a dim ond yn cronni biwrocratiaeth drwy wthio ymhellach. Penderfynwch dargedau fesul gallu, a stopiwch ddringo pan fydd y dychweliad wedi'i addasu-risg yn stopio.

### Gwarchodwch yn erbyn theatr aeddfedrwydd

Y modd methiant sengl sy'n dinistrio gwerth modelau aeddfedrwydd yw optimeiddio ar gyfer y sgôr. Gwyliwch am asesiadau sy'n graddio'n hael, tystiolaeth wedi'i chydosod dim ond ar gyfer yr arfarniad, neu honiadau "lefel 5" y mae digwyddiadau cynhyrchu'n eu gwrth-ddweud. Cadwch yr asesiad wedi'i glymu wrth ymddygiad arsylwadwy a chanlyniadau gwirioneddol. Cylchdrowch neu wiriwch synnwyr cyffredin eich aseswyr yn allanol. Triniwch hunansgôr amheus o uchel fel arogl. Yr eiliad y daw'r lefel yn nod, mae'r model yn peidio â dweud y gwir wrthych.

## Cyfaddawdau: manteision ac anfanteision

| Dull | Manteision | Anfanteision |
|---|---|---|
| **Modelau ffurfiol wedi'u harfarnu (CMMI, CMMC)** | Cymharadwy, wedi'u cydnabod yn gontractiol, trylwyr | Costus; yn gwahodd chwarae'r system; gall galedu proses |
| **Cardiau sgorio mewnol ysgafn** | Cyflym, gweithredadwy, baich isel | Llai cymharadwy'n allanol; hawdd ei feio |
| **Modelau gallu seiliedig-ar-dystiolaeth (DORA)** | Wedi'u clymu wrth ganlyniadau gwirioneddol; wedi'u cefnogi gan ymchwil | Cwmpas culach; angen metrigau gwirioneddol |
| **Un radd aeddfedrwydd gyffredinol** | Syml i'w gyfleu | Yn cuddio gallu anwastad; yn camarwain |
| **Asesiad fesul gallu** | Blaenoriaethu cywir, gweithredadwy | Mwy o ymdrech; dim un pennawd rhif |

Y tyndra canolog yw **asesu fel drych yn erbyn asesu fel targed**. Mae'r un model sy'n helpu tîm i weld ei hun yn glir yn troi'n wrth-gynhyrchiol yr eiliad y caiff lefel ei chlymu wrth wobr, cymhwysedd, neu statws. Po fwyaf pwysig yw lefel, y mwyaf o egni sy'n llifo i mewn i ymddangosiad aeddfedrwydd yn hytrach na'r sylwedd.

## Cwestiynau i'w trafod gyda'ch tîm

1. **A ddylem gadw hunanasesiad mewnol gonest ar wahân i unrhyw lefel a arfarnwyd yn gontractiol, a phwy sy'n berchen ar bob un?** Pan fydd lefel CMMC neu CMMI yn giatio refeniw, mae'r arfarniad a'r gwirionedd yn drifftio ar wahân, oherwydd mae egni'n llifo tuag at basio yn hytrach na gwella. I fenter fawr neu gyflenwr llywodraethol, dyna lle mae risg yn cuddio: rydych yn pasio'r archwiliad ac yn aros yn agored. Rhedwch ddau lyfr yn fwriadol. Cadwch yr arfarniad ffurfiol ar gyfer cymhwysedd, a chadwch gerdyn sgorio mewnol plaen nad oes neb yn cael ei wobrwyo am ei chwyddo. Enwch berchennog ar gyfer pob un, a thriniwch unrhyw bellter rhyngddynt fel signal i'w ymchwilio, nid i'w guddio. Dewch â digwyddiadau diweddar, chwithdodau agos, a dirywiad wedi'r arfarniad i'r cyfarfod fel tystiolaeth o ba lyfr sy'n dweud y gwirionedd.

2. **Ar gyfer pob parth, a ydym yn mabwysiadu model sefydledig seiliedig-ar-dystiolaeth neu'n dyfeisio ein cerdyn sgorio ein hunain, ac ai dyna'r penderfyniad cywir?** Mae modelau sefydledig (DORA ar gyfer cyflenwi, SAMM neu BSIMM ar gyfer diogelwch, TMMi ar gyfer profi) yn cario ymchwil a chymharoldeb allanol na all grid cartref eu cyfateb. Mae graddfa fewnol ysgafn pedwar-lefel yn gyflymach ac yn fwy gweithredadwy, ac mae'n aml yn ddewis gwell ar gyfer llywio mewnol. Y trap yw dyfeisio fframwaith pwrpasol trwm sydd â holl seremoni model ffurfiol a dim o'r sylfaen dystiolaeth. Penderfynwch fesul parth: cadwch fodelau ffurfiol wedi'u harfarnu ar gyfer lle mae contract yn eu mynnu, defnyddiwch fodelau seiliedig-ar-dystiolaeth lle maent yn bodoli ac yn ffitio, a chadwch raddfa syml fesul gallu ar gyfer popeth arall. Dewch â'r rhestr o barthau, nodwch pa fodel y mae pob un yn ei ddefnyddio heddiw, a herwch bob cerdyn sgorio a ddyfeisiwyd.

3. **Pwy sy'n rhedeg ein hasesiadau, sut fyddem yn dal graddio hael, a pha mor aml ydym yn ailasesu?** Mae asesiad sy'n graddio ei hun yn ei wenieithu ei hun, ac mae aeddfedrwydd yn drifftio wrth i bobl, systemau, a bygythiadau newid, felly mae arfarniad dwy flwydd oed yn aml yn ffuglen. Cylchdrowch aseswyr neu ddewch â gwiriad synnwyr cyffredin allanol i mewn, a thriniwch hunansgôr amheus o uchel fel arogl i'w ymlid, nid buddugoliaeth i'w dathlu. Gosodwch gadenc ailasesu wedi'i glymu wrth ba mor gyflym mae pob parth yn newid: diogelwch yn amlach nag, dyweder, dogfennaeth. Casglwch dystiolaeth a chynhwyswch y bobl sy'n gwneud y gwaith yn hytrach na chasglu barn gan reolwyr. Os yw eich ateb yn dweud bod un tîm yn sgorio ei hun unwaith y flwyddyn heb wiriad croes, rydych yn mesur cysur, nid gallu.

4. **Pa lefel aeddfedrwydd targed sydd wir angen ei chyrraedd ar bob gallu, a lle byddai gwthio'n uwch ond yn prynu pwysau proses i ni?** Nid yw uwch yn rhad: mae pob lefel i fyny'n costio ymdrech ac fel arfer yn ychwanegu seremoni, felly mae nod cyffredinol o lefel 5 ym mhobman yn draenio cyllideb wella gyfyngedig i mewn i fiwrocratiaeth na fydd rhai parthau byth yn ei had-dalu. I sefydliad mawr mae'r targed cywir yn amrywio yn ôl gallu, oherwydd gall ardal risg-isel sy'n eistedd ar lefel 2 fod yn berffaith ddiogel tra bod ardal ddiogelwch- neu gydymffurfiaeth-dyngedfennol ar yr un lefel yn argyfwng. Dewch â graddfa risg fesul gallu, amcangyfrif gonest o beth mae'r gris nesaf yn ei gostio mewn ymdrech a phroses, ac unrhyw lawr archwiliad neu gontractiol, gan fod llawer o archwiliadau'n mynnu o leiaf lefel 3 "wedi'i ddiffinio." Mewn lleoliadau mentrau a llywodraethol, mae angen y gwreiddiau uchaf yn wirioneddol ar rai galluoedd rheoleiddiedig tra bod y rhan fwyaf wedi'u gwasanaethu'n dda ar lefel 3, felly penderfynwch dargedau'n fwriadol, gallu wrth allu, a stopiwch ddringo pan fydd y dychweliad wedi'i addasu-risg yn stopio.

5. **Y tro diwethaf i ni godi lefel aeddfedrwydd, a wnaeth y canlyniad yr oedd i fod i'w warchod wella mewn gwirionedd, neu ai dim ond y sgôr a symudodd?** Mae lefel sy'n dringo tra bod digwyddiadau, amser arwain, neu gyfraddau diffygion yn aros yn wastad yn Gyfraith Goodhart ar waith: unwaith y daw'r rhif yn darged, mae'n peidio â mesur gallu. I dîm mawr mae hyn yn llithro heibio'n hawdd, oherwydd mae arfarniad llwyddiannus yn teimlo fel cynnydd hyd yn oed pan fo cynhyrchu'n adrodd stori wahanol. Clymwch lefel pob gallu wrth fetrig canlyniad gwirioneddol cyn i chi fuddsoddi, yna dewch â'r dystiolaeth cyn-ac-ar-ôl i'r drafodaeth: digwyddiadau fesul chwarter, cyfradd methiant newid, amser i adfer, beth bynnag y mae'r gallu'n bodoli i'w wella. Mewn portffolios mentrau a llywodraethol lle mae lefel wedi'i harfarnu'n giatio cymhwysedd, mae'r bwlch yn beryglus, oherwydd gall y lefel godi ar dystiolaeth wedi'i chydosod tra bod yr arfer sylfaenol yn dirywio'n dawel, a'r prawf cyntaf o hynny yw toriad, toriad gwasanaeth, neu archwiliad wedi methu.

6. **A ydym yn cyfleu un radd aeddfedrwydd pennawd neu ddarlun fesul gallu, ac a yw lefelau byth wedi'u clymu wrth wobr, safle, neu statws tîm?** Mae un rhif cyffredinol yn hawdd i'w gyflwyno i arweinyddiaeth ac mae'n cuddio union yr anwastadrwydd sy'n bwysig, oherwydd gall cyflenwi cryf guddio gallu diogelwch lefel-1; mae map gwres fesul gallu yn fwy o waith eto'n dangos lle mae aeddfedrwydd isel yn cwrdd â risg uchel. Y cwestiwn anoddach yw sut mae'r sgoriau'n cael eu defnyddio, oherwydd yr eiliad y caiff lefel ei chlymu wrth wobr neu safle tîm, mae adrodd gonest yn marw ac mae ymdrech yn llifo i mewn i ymddangosiad aeddfedrwydd yn hytrach na'r sylwedd. Dewch â'r map gwres, a chyfrif didwyll o bob lle mae lefel yn bwydo adolygiad perfformiad, penderfyniad cyllideb, neu gerdyn sgorio gwerthwr ar hyn o bryd. I fentrau a chyflenwyr llywodraethol, lle gall lefelau wedi'u harfarnu giatio refeniw a chymhwysedd, byddwch yn benodol am ba raddau sy'n cario canlyniadau a pha rai sy'n bodoli dim ond i lywio, oherwydd mae darlun aeddfedrwydd y mae pobl yn cael eu gwobrwyo am ei chwyddo yn peidio â disgrifio realiti.

## Trwy lens sector

**Cwmni newydd.** Mae model ffurfiol trwm yn faich na allwch ei fforddio ar draffordd fer. Rhedwch hunanasesiad awr ar raddfa syml ar draws llond dwrn o alluoedd, trwsiwch dim ond y bwlch aeddfedrwydd-isaf sy'n rhwystro rhywbeth pendant (dyweder, holiadur diogelwch eich cwsmer menter cyntaf), a gadewch y gweddill yn llonydd. Dylai'r asesiad gostio prynhawn, nid ymgynghorydd, a'i allbwn yw un weithred nesaf yn hytrach na sgôr uchel unffurf nad oes ei angen arnoch nac y gallwch ei ariannu.

**Busnes bach.** Heb aseswr penodedig a chyllideb dynn, benthycwch fodel cyhoeddus ysgafn yn hytrach na chomisiynu fframwaith pwrpasol: rhestr wirio gyflenwi neu ddiogelwch fer y gallwch ei hunansgorio. Triniwch hi fel sgwrs flynyddol am le byddai man gwan yn costio cwsmer i chi, nid rhaglen sefydlog. Cadwch hi'n rad ac yn blaen, oherwydd mae sgôr wenieithus y talwch werthwr i'w chynhyrchu'n werth llai na un ddidwyll a wnaethoch eich hun mewn prynhawn.

**Menter.** Y gwerth yw cerdyn sgorio a rennir fesul gallu a gymhwysir yn gyson ar draws llawer o dimau, fel bod bylchau'n dod yn gymharadwy a chyllideb gwella'n llifo i lle mae aeddfedrwydd isel yn cwrdd â risg uchel. Gwarchodwch yn galed yn erbyn theatr aeddfedrwydd unwaith y bydd lefelau'n bwydo cyllideb neu statws: cylchdrowch neu wiriwch synnwyr cyffredin aseswyr yn allanol, a rheolwch y canlyniadau fel map gwres sy'n cyfeirio buddsoddiad ffordd-balmantog (pennod 4.2) yn hytrach na thabl cynghrair sy'n graddio timau ac yn lladd adrodd gonest.

**Llywodraeth.** Mae lefel aeddfedrwydd yn aml yn giât lythrennol yma: CMMC ar gyfer gwaith amddiffyn, arfarniad CMMI fel cymhwyster cyflenwr. Cyrhaeddwch y lefel ofynnol gyda gallu gwirioneddol, a chadwch hunanasesiad mewnol didwyll ar wahân i'r arfarniad ffurfiol fel na fydd llawr yr archwiliad byth yn dawel yn dod yn nenfwd. Dogfennwch dystiolaeth yn dryloyw ar gyfer arfarnwyr, a thriniwch unrhyw bellter rhwng y lefel ardystiedig a'r arfer gwirioneddol fel risg atebol i'w gau, nid papurwaith i'w ffeilio.

## Enghreifftiau

**Cwmni newydd.** Mae cwmni newydd SaaS deg person yn rhedeg hunanasesiad awr yn erbyn graddfa syml pedwar-lefel sy'n cwmpasu cyflenwi, profi, diogelwch, ac ar-alwad. Mae'n canfod cyflenwi a phrofi ar lefel 3 ond diogelwch yn sownd ar lefel 1, sy'n bwysig oherwydd ei fod ar fin llofnodi ei gwsmer menter cyntaf gyda holiadur diogelwch. Felly mae'r sylfaenwyr yn treulio'r mis nesaf yn codi diogelwch yn unig i lefel 2 amddiffynadwy ac yn gadael y gweddill yn llonydd, yn hytrach nag ymlid sgôr uchel unffurf nad oes ei angen arnynt nac y gallant ei fforddio eto.

**Menter.** Mae cwmni gwasanaethau ariannol yn asesu ei 40 tîm gyda cherdyn sgorio ysgafn fesul gallu (cyflenwi, profi, diogelwch, arsylladwyedd, ar-alwad). Mae'r map gwres yn datgelu bod aeddfedrwydd diogelwch yn ôl fwyaf lle mae amlygiad rheoleiddiol uchaf, felly mae'r tîm platfform yn ariannu offer diogelwch ffordd-balmantog (pennod 4.2) ar gyfer y timau hynny yn gyntaf. Am fod yr asesiad yn cael ei ddefnyddio i flaenoriaethu buddsoddiad yn hytrach na graddio timau, mae rheolwyr yn adrodd yn onest. Mae ailasesiad flwyddyn yn ddiweddarach yn dangos symudiad gwirioneddol, ac, yn hollbwysig, llai o ddigwyddiadau diogelwch, nid dim ond sgoriau uwch.

**Llywodraeth.** Rhaid i gontractwr amddiffyn gyrraedd lefel CMMC ofynnol i gynnig am waith, ac mae integreiddiwr systemau'n dal arfarniad CMMI fel cymhwyster contract. Yma mae'r lefel aeddfedrwydd yn giât lythrennol at refeniw. Mae'r fersiwn a redir yn dda yn trin y lefel ofynnol fel llawr ar gyfer gallu gwirioneddol ac yn cadw hunanasesiad mewnol didwyll ar wahân i'r arfarniad ffurfiol. Mae'r fersiwn a redir yn wael yn cydosod tystiolaeth ar gyfer yr arfarniad ac yn gadael i'r arfer gwirioneddol ddirywio'r diwrnod wedyn, gan basio'r archwiliad tra'n aros yn agored.

## Achos busnes: cymhellion, ROI, a TCO

Daw'r dychweliad ar asesiad aeddfedrwydd o **fuddsoddiad wedi'i gyfeirio**. Mae cyllidebau gwella'n gyfyngedig. Wedi'u gwario'n ddall, maent yn ariannu beth bynnag sydd fwyaf swnllyd. Mae asesiad aeddfedrwydd yn dangos i chi lle mae gallu wannaf yn erbyn risg, fel bod yr un gwariant yn prynu mwy o leihad risg a mwy o welliant canlyniad. Mae'r asesiad ei hun yn rhad, dim ond dyddiau o adolygiad strwythuredig, seiliedig-ar-dystiolaeth, wedi'i osod yn erbyn cost rhaglenni gwella wedi'u camddyrannu neu, yn waeth, bwlch gallu heb ei ganfod sy'n ymddangos fel toriad, toriad gwasanaeth, neu archwiliad wedi methu.

O ran **cyfanswm cost perchnogaeth**, mae'r ddisgyblaeth yn gost-isel pan fyddwch yn ei chadw'n ysgafn ac yn gost-uchel pan fydd yn caledu i mewn i fiwrocratiaeth arfarniad. Y gost gudd amlycaf yw *theatr aeddfedrwydd*: mae ymdrech a dreulir yn cynhyrchu ymddangosiad aeddfedrwydd yn dychwelyd dim ac yn gallu cuddio risg gwirioneddol, sy'n ROI negyddol. I wneud yr achos i arweinyddiaeth, cyflwynwch aeddfedrwydd fel lens risg-a-buddsoddiad, map gwres sy'n troi "gwella popeth" yn "gwella'r tri pheth hyn yn gyntaf," a chyllidebwch yn benodol yn erbyn y demtasiwn o ymlid lefelau er eu mwyn eu hunain. Lle mae lefel yn ofynnol yn gontractiol (CMMC, CMMI), mae'r ROI yn uniongyrchol: pris cymhwysedd ydyw, a'r nod yw ei chyrraedd gyda gallu gwirioneddol yn hytrach na esgus drud.

## Gwrthbatrymau a pheryglon

- **Lefel fel y nod:** ymlid rhif yn hytrach na'r gallu y mae i fod i'w gynrychioli.
- **Theatr aeddfedrwydd:** cydosod tystiolaeth ar gyfer arfarniad tra bod arfer gwirioneddol yn dirywio.
- **Un radd fyd-eang:** un sgôr aeddfedrwydd sy'n cuddio anwastadrwydd peryglus.
- **Uwch-yn-well-bob-amser:** gwthio pob gallu i lefel 5 waeth beth am risg neu gost.
- **Aseswch unwaith, byth eto:** arfarniad un-tro wedi'i drin fel gwirionedd parhaol.
- **Graddio timau i feio:** defnyddio aeddfedrwydd ar gyfer cosb, sy'n lladd adrodd gonest.
- **Addoli model:** dilyn seremoni fframwaith trwm heibio'r pwynt o ddefnyddioldeb.
- **Anwybyddu canlyniadau:** dringo'r ysgol tra nad yw cyflenwi, dibynadwyedd, na diogelwch yn gwella.

## Model aeddfedrwydd

- **Lefel 1, Cychwyn.** Dim syniad a rennir o aeddfedrwydd; caiff gallu ei dybio, yn anwastad, ac heb ei fesur; mae unrhyw asesiad yn adweithiol, wedi'i ysgogi gan ddigwyddiad neu fynnu archwiliad yn hytrach na'i gynllunio.
- **Lefel 2, Datblygu.** Mae ychydig o dimau'n rhedeg asesiadau ad hoc yn erbyn rhyw raddfa, ond mae'r model, y gadenc, a'r trylwyredd yn amrywio o dîm i dîm; defnyddir canlyniadau'n anghyson ac mae tystiolaeth yn denau, felly mae sgorio er ymddangosiad yn risg bythbresennol.
- **Lefel 3, Safoni.** Mae un model fesul gallu a chadenc asesu wedi'u dogfennu a'u cymhwyso ar draws y sefydliad; mae asesiadau'n seiliedig-ar-dystiolaeth, yn cynnwys y bobl sy'n gwneud y gwaith, ac yn bwydo ôl-groniad gwelliant wedi'i flaenoriaethu yn hytrach na cherdyn adroddiad.
- **Lefel 4, Rheoli.** Mesurir a rheolir aeddfedrwydd â data: olrheinir lefel pob gallu yn erbyn llinell sylfaen, wedi'i chlymu wrth fetrig canlyniad (digwyddiadau, amser arwain, cyfradd methiant newid), ac fe'i hailasesir ar gadenc osodedig, fel bod drifft a graddio hael yn ymddangos fel rhifau yn hytrach na barn, a gosodir targedau'n fwriadol fesul parth yn erbyn risg a chost.
- **Lefel 5, Cerddorfa.** Mae asesu wedi'i integreiddio ar draws y sefydliad a'i wella'n barhaus: mae aeddfedrwydd, risg, a chanlyniadau'n llywio buddsoddiad fel un darlun addasol, ailgydbwysir targedau wrth i fygythiadau a chyd-destun newid, cylchdroir aseswyr neu eu gwirio'n allanol fel mater o drefn, ac mae'r arfer yn ymddeol seremoni sydd bellach ddim yn ennill ei gost yn weithredol.

## Syniadau ar gyfer trafodaeth

1. Pa rai o'ch galluoedd rydych yn tybio eu bod yn aeddfed heb dystiolaeth?
2. Ble mae eich aeddfedrwydd isaf yn cyd-daro â'ch risg uchaf, ac a yw hynny lle mae eich cyllideb gwella'n mynd?
3. A yw unrhyw lefel aeddfedrwydd yn eich sefydliad yn darged neu'n giât? Pa ymddygiad y mae hynny wedi'i gynhyrchu?
4. Beth yw'r lefel darged gywir ar gyfer pob gallu, a lle byddai dringo ymhellach ond yn ychwanegu biwrocratiaeth?
5. A fyddai eich timau'n adrodd eu haeddfedrwydd yn onest, neu a yw'r ffordd rydych yn defnyddio sgoriau'n cosbi didwylledd?
6. Y tro diwethaf i chi "wella aeddfedrwydd," a wnaeth canlyniadau newid mewn gwirionedd?

## Prif negeseuon

- Mae model aeddfedrwydd yn asesu gallu yn erbyn ysgol o lefelau ac yn disgrifio llwybr i wella: drych, nid tlws.
- Dewiswch fodelau sefydledig, seiliedig-ar-dystiolaeth fesul parth (CMMI, DORA, SAMM/BSIMM, CMMC); mae graddfa ysgafn fesul gallu yn aml y mwyaf gweithredadwy.
- **Aseswch yn onest, fesul gallu**, a defnyddiwch ganlyniadau i **flaenoriaethu yn ôl risg**, nid i raddio na beio.
- **Nid yw uwch bob amser yn well:** gosodwch lefelau targed yn fwriadol yn erbyn risg a chost.
- Gwyliwch am **theatr aeddfedrwydd** a **Chyfraith Goodhart**: mae lefel sy'n dod yn darged yn peidio â mesur gallu.
- Gweler pennod 12.4 am hunanasesiad aeddfedrwydd cyfun y llyfr hwn, ac adran aeddfedrwydd ei hun ym mhob pennod.

## Cyfeiriadau a darllen pellach

- CMMI Institute / ISACA, *Capability Maturity Model Integration (CMMI)*.
- Watts Humphrey, *Managing the Software Process* (tarddiad aeddfedrwydd proses meddalwedd).
- Nicole Forsgren, Jez Humble, Gene Kim, *Accelerate* (meddwl gallu, nid lefel-aeddfedrwydd, ar gyfer cyflenwi).
- OWASP, *Software Assurance Maturity Model (SAMM)*; BSIMM (*Building Security In Maturity Model*).
- Adran Amddiffyn UDA, *Cybersecurity Maturity Model Certification (CMMC)*.
- TMMi Foundation, *Test Maturity Model integration*.
- James Shore a Diana Larsen, *The Agile Fluency Model*.
- Martin Fowler, "Maturity Model" (bliki), ar eu defnyddiau a'u camddefnyddiau.
