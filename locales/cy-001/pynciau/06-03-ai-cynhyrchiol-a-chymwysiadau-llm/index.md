# 6.3 Cymhwysiadau AI generadigol ac LLM

## Trosolwg a chymhelliant

Gall [AI generadigol](https://en.wikipedia.org/wiki/Generative_artificial_intelligence), a [modelau iaith mawr](https://en.wikipedia.org/wiki/Large_language_model) (LLMs) yn arbennig, gynhyrchu testun rhugl, cod, crynodebau, a data strwythuredig o gyfarwyddiadau iaith-naturiol. Mae hynny'n eu gwneud yn flociau adeiladu pwerus ar gyfer cynorthwywyr, chwilio, prosesu dogfennau, ac awtomeiddio. Ond mae'r cryfderau hynny'n dod â phroffil risg nodedig. Mae LLMs yn debygolegol. Gallant gynhyrchu anwireddau hyderus ([rhithweledigaethau](https://en.wikipedia.org/wiki/Hallucination_(artificial_intelligence))). Maent yn sensitif i sut yr ydych yn eu procio. Ac maent yn agor arwynebau ymosod newydd megis [chwistrelliad procio](https://en.wikipedia.org/wiki/Prompt_injection) (cyfarwyddiadau maleisus wedi'u smyglo i mewn i fewnbynnau i herwgipio ymddygiad y model). Felly mae adeiladu cymhwysiadau LLM dibynadwy yn llai am y model a mwy am y beirianneg o'i amgylch: sut yr ydych yn cyflenwi cyd-destun, gwreiddio atebion mewn gwybodaeth ymddiriedol, cyfyngu allbynnau, a gwerthuso ansawdd.

I dimau mawr, mae cymhwysiadau LLM yn galw am batrymau newydd sy'n wahanol i feddalwedd traddodiadol a dysgu peiriant clasurol fel ei gilydd. Yn aml does dim cam hyfforddi. Yn hytrach, siapir ymddygiad gan brociau, cyd-destun a adferwyd, diffiniadau teclyn, a chiatiau gwarchod (gwiriadau amser-rhedeg sy'n cyfyngu mewnbynnau ac allbynnau'r model). Mae hynny'n symud yr ymdrech beirianyddol tuag at reoli cyd-destun, ansawdd adfer, cyfundrefnu, a gwerthuso. Mae mentrau sy'n mabwysiadu LLMs ar raddfa angen patrymau a rennir fel nad yw pob tîm yn ailddarganfod yr un moddau methiant y ffordd galed.

Mae llywodraeth a sefydliadau rheoledig yn wynebu gofynion ychwanegol. Nid nam yn unig yw LLM sy'n ffugio dyfyniad polisi neu'n gollwng data sensitif; gall fod yn ddigwyddiad cyfreithiol neu ddiogelwch. Mae angen ar y lleoliadau hyn wreiddio mewn ffynonellau awdurdodol, dilysu allbwn llym, goruchwyliaeth ddynol ar gyfer allbynnau canlyniadol, a chofnodion clir o'r hyn y gofynnwyd i'r system ei wneud a'r hyn a gynhyrchodd. Y technegau yn y bennod hon (cynhyrchu wedi'i estyn gan adferiad, giatiau gwarchod, a gwerthusiad trylwyr) yw'r hyn sy'n gwneud LLMs yn ddigon diogel i'w defnyddio mewn cyd-destunau risg-uchel. Mae modelau Claude Anthropic yn un opsiwn blaenllaw ymysg sawl darparwr galluog; mae'r arferion yma'n gymwys ni waeth pa fodel a ddewiswch.

## Egwyddorion allweddol

- Gwreiddiwch y model mewn gwybodaeth ymddiriedol yn hytrach na dibynnu ar yr hyn a gofiodd.
- Triniwch brociau a chyd-destun fel arteffactau wedi'u peirianyddu, wedi'u fersiynu, nid llinynnau taflu-i-ffwrdd.
- Tybiwch y gall y model fod yn anghywir neu wedi'i drin; dilyswch allbynnau a chyfyngwch weithredoedd.
- Rhowch i'r model dim ond y cyd-destun a'r teclynnau sydd eu hangen arno, dim mwy, i leihau gwall ac arwyneb ymosod.
- Gwerthuswch yn barhaus gyda setiau prawf all-lein, metrigau ar-lein, a barn ddynol.
- Cadwch bobl yn y ddolen ar gyfer allbynnau canlyniadol.
- Dyluniwch ar gyfer y model fel cydran heb ei ymddiried o fewn system ymddiriedol.

## Argymhellion

### Peirianyddu prociau a rheoli cyd-destun yn fwriadol

Triniwch brociau fel cod: storiwch hwy mewn rheolaeth fersiynau, adolygwch newidiadau, a'u profi yn erbyn cyfres o enghreifftiau. Strwythurwch bob procio'n glir: rôl a thasg, cyfyngiadau, gofynion fformat, ac enghreifftiau lle maent yn helpu. Triniwch y ffenestr gyd-destun (y rhychwant sefydlog o destun y gall y model ei ystyried ar unwaith) fel adnodd prin. Cynhwyswch y wybodaeth fwyaf perthnasol, ei threfnu'n feddylgar, a strip allan sŵn, gan fod cyd-destun amherthnasol neu ormodol yn dirywio ansawdd ac yn codi cost. Ar gyfer cymhwysiadau amldro, rheolwch gyflwr sgwrs yn benodol, gan grynhoi neu dorri hanes i aros o fewn terfynau tra'n cadw'r hyn sy'n bwysig. Ffafriwch gyfarwyddiadau clir ac enghreifftiau ychydig-ergydion (llond llaw o arddangosiadau wedi'u gweithio wedi'u cynnwys yn y procio) dros driciau cywrain sy'n torri'r foment y mae model yn newid.

### Gwreiddio atebion â chynhyrchu wedi'i estyn gan adferiad (RAG)

Ar gyfer tasgau gwybodaeth-ddwys, adferwch ddogfennau perthnasol o gorpws ymddiriedol a'u cyflenwi i'r model fel cyd-destun, gan ddweud wrtho i ateb dim ond o'r deunydd hwnnw ac i ddyfynnu ei ffynonellau. Mae RAG yn cadw gwybodaeth yn gyfredol heb ailhyfforddi, yn cyfyngu atebion i gynnwys cymeradwy, ac yn galluogi dyfynnu a gwiriad. Buddsoddwch mewn ansawdd adfer: cwciwch ddogfennau'n synhwyrol, dewiswch [ymgladdiadau](https://en.wikipedia.org/wiki/Word_embedding) (cynrychioliadau fector rhifiadol sy'n gosod ystyron cyffelyb yn agos at ei gilydd) sy'n addas i'ch maes, a gwiriwch a yw'r darnau a adferwyd mewn gwirionedd yn cynnwys yr ateb, gan fod ateb rhugl wedi'i adeiladu ar y darn anghywir yn waeth na dim ateb. A phan na ddaw dim byd perthnasol i'r amlwg, gwnewch i'r system ddweud hynny yn hytrach na dyfeisio cynnwys.

### Adeiladu asiantau a defnydd teclyn gyda hunanataliad

Gall LLMs alw teclynnau (chwilio, cronfeydd data, cyfrifianellau, APIs mewnol) a gellir eu cyfansoddi'n asiantau sy'n cynllunio ac yn gweithredu dros gamau lluosog. Mae hyn yn ychwanegu gallu gwirioneddol, ond mae hefyd yn lluosi risg: mae pob teclyn yn ffordd arall i fodel anghywir neu wedi'i drin achosi niwed. Diffiniwch declynnau â sgemâu manwl gywir, dilyswch bob ymresymiad, cymhwyswch fraint leiaf, a mynnwch gadarnhad neu gymeradwyaeth ddynol ar gyfer gweithredoedd canlyniadol megis anfon cyfathrebiadau neu symud arian. Cadwch ddolenni asiant yn ffiniedig, arsylwadwy, a therfynadwy. Dechreuwch gyda theclynnau â chwmpas tynn, un-pwrpas cyn cyrraedd am ymreolaeth agored-ei-diwedd.

### Ychwanegu giatiau gwarchod a dilysu allbynnau

Lapiwch y model mewn haenau o amddiffyniad. Ar y ffordd i mewn, hidlwch a chanfyddwch chwistrelliad procio, yn enwedig pan fo cynnwys heb ei ymddiried (tudalennau gwe, dogfennau defnyddiwr) yn dod i mewn i'r cyd-destun. Ar y ffordd allan, dilyswch strwythur yn erbyn sgema, gwiriwch hawliadau yn erbyn ffynonellau, hidlwch gynnwys anniogel neu anghydymffurfiol, a gwrthodwch neu ailgeisiwch pan fo dilysu'n methu. Ar gyfer allbynnau strwythuredig, dosrannwch a gwiriwch yn hytrach nag ymddiried yn fformatio'r model. Peidiwch byth â gadael i allbwn crai'r model sbarduno gweithredoedd anwrthdroadwy heb ddilysu. Triniwch liniaru rhithweledigaethau fel priodwedd system a gyflawnwch trwy wreiddio, dyfynnu, dilysu, ac adolygiad dynol, nid rhywbeth y mae'r model yn ei reoli ar ei ben ei hun.

### Gwerthuso all-lein, ar-lein, a chyda phobl

Adeiladwch gyfres werthuso o fewnbynnau cynrychioliadol ag allbynnau hysbys-dda neu wedi'u sgorio-rwbrig, a'i rhedeg ar bob newid procio neu fodel (gwerthusiad all-lein). Mesurwch ymddygiad go iawn mewn cynhyrchu â metrigau megis llwyddiant tasg, cyfradd uwchgyfeirio, ac adborth defnyddiwr (gwerthusiad ar-lein). Ar gyfer ansawdd goddrychol, defnyddiwch adolygwyr dynol ac, yn ofalus, raddio seiliedig-ar-fodel. Gwerthusiad yw'r rhwyd ddiogelwch sy'n gadael i chi newid prociau a modelau'n hyderus. Hebddo, rydych yn hedfan yn ddall.

## Cyfaddawdau: manteision ac anfanteision

| Dewis | Manteision | Anfanteision | Gorau pan |
|---|---|---|---|
| Procio pur | Syml, cyflym, rhad i'w newid | Gwreiddio cyfyngedig, gall rithweledigo | Tasgau eang, risg isel |
| RAG | Cyfredol, wedi'i wreiddio, dyfynadwy | Mae adferiad yn anodd ei gael yn iawn | Tasgau gwybodaeth-drwm, ffeithiol |
| Asiantau â theclynnau | Pwerus, gall weithredu | Arwyneb ymosod mwy, anos ei reoli | Awtomeiddio â chwmpas da gyda giatiau gwarchod |
| Model mwy, cryfach | Ansawdd a rhesymu gwell | Cost ac oedi uwch | Tasgau cymhleth neu risg-uchel |
| Model llai, rhatach | Cyflym ac anghostus | Gwannach ar dasgau anodd | Cyfaint uchel, tasgau syml |

Y tyndra craidd yw gallu yn erbyn rheolaeth a chost. Mae mwy o ymreolaeth a modelau mwy'n cyflenwi mwy o werth, ond maent yn mynnu mwy o giatiau gwarchod, mwy o werthuso, a mwy o arian. Mae gwreiddio trwy RAG yn gwella ymddiriedolrwydd ar draul peirianneg adfer. Mae'r cydbwysedd cywir yn dibynnu ar y risg: mae cymhwysiadau risg-uchel yn gogwyddo tuag at wreiddio, dilysu, a goruchwyliaeth ddynol, hyd yn oed pan fo hynny'n costio mwy.

## Cwestiynau i'w trafod gyda'ch tîm

1. **Pa far cywirdeb a gwreiddio y mae'n rhaid i nodwedd LLM ei glirio cyn iddi wynebu'r cyhoedd, a phwy sy'n arwyddo i ffwrdd?** Mae ateb rhugl sy'n dyfynnu'r ffynhonnell anghywir neu'n dyfeisio polisi'n waeth na dim ateb, ac mewn llywodraeth mae dyfyniad wedi'i ffugio'n ddigwyddiad cyfreithiol, nid nam. I dîm mawr, mae bar penodol yn atal pob grŵp rhag gosod ei drothwy preifat ei hun yn ôl teimlad. Dewch â'ch diffiniad o "wedi'i wreiddio digon": a yw'n rhaid i bob hawliad olrhain i ffynhonnell a adferwyd, wedi'i gwirio, a yw'n rhaid i'r system wrthod pan fo adferiad yn dod yn wag, a beth y mae eich set werthuso wrthwynebus mewn gwirionedd yn ei chwmpasu. Y signal i'w wylio yw a all unrhyw un ar hyn o bryd gyflenwi newid procio'n syth i ddefnyddwyr heb redeg atchweliad. Os yw'r risg yn gyfreithiol neu'n ymwneud â diogelwch, dylai'r ateb gyfeirio'r allbynnau risg-uchaf trwy adolygydd dynol ag awdurdod go iawn cyn rhyddhau.

2. **Pa rai o'n nodweddion LLM sy'n asiantau yn gyfrinachol, ac a roddwyd i bob teclyn fraint leiaf a giât ddynol ar weithredoedd anwrthdroadwy?** Mae unrhyw nodwedd sy'n gadael i'r model alw teclynnau neu weithredu dros gamau lluosog wedi croesi i mewn i diriogaeth asiant, ac mae pob teclyn yn ffordd arall y mae model anghywir neu wedi'i drin yn achosi niwed. I fentrau sy'n gwifro LLMs i mewn i APIs mewnol, mae'r cwestiwn hwn yn dwyn i'r amlwg risg y mae label "cynorthwyydd syml" yn ei guddio. Dewch â rhestr eiddo o bob teclyn y gall y model ei alw, ei ddilysiad ymresymiad, ei gwmpas braint, a pha weithredoedd (anfon cyfathrebiadau, symud arian, newid cofnodion) sy'n mynnu cadarnhad. Trafodwch a yw dolenni asiant yn ffiniedig, yn arsylwadwy, ac yn derfynadwy. Dylai'r ateb dynhau cwmpasau ac ychwanegu giatiau cymeradwyaeth ddynol lle bynnag y mae gweithred ganlyniadol neu anwrthdroadwy'n hygyrch ar hyn o bryd heb un.

3. **Sut y byddem yn gwybod o fewn diwrnod bod ein hansawdd adferiad wedi gostwng, o ystyried bod ateb hyderus wedi'i adeiladu ar y darn anghywir yn edrych yn iawn?** Mae RAG yn gwneud atebion yn ymddiriedol dim ond pan fo adferiad mewn gwirionedd yn dwyn i'r amlwg y darn sy'n cynnwys yr ateb, ac mae adferiad yn pydru'n ddistaw wrth i ddogfennau newid, cwciau fynd yn hen, neu ymgladdiadau wyro oddi wrth eich maes. Gan fod y model yn dal i ysgrifennu'n rhugl dros gyd-destun gwael, efallai na fydd defnyddwyr yn cwyno nes bod ymddiriedaeth eisoes wedi'i cholli. Dewch â'ch mesurau presennol o oedi ac adalw adferiad, sut yr ydych yn gwirio a yw'r darnau a adferwyd mewn gwirionedd yn cynnwys yr ateb, a sut y mae ffresni mynegai'n cadw i fyny â newidiadau dogfen. Ar gyfer defnyddiadau risg-uchel neu gyhoeddus, trafodwch gofnodi ffynonellau a adferwyd ar gyfer archwilio fel y gallwch olrhain ateb gwael i'w ddarn gwael. Os nad oes gennych werthusiad adferiad o gwbl, rydych yn gwreiddio ar ffydd.

4. **A ydym yn trin prociau, cyd-destun, a setiau gwerthuso fel arteffactau wedi'u fersiynu, wedi'u hadolygu, neu fel llinynnau wedi'u gwasgaru ar draws llyfrau nodiadau a logiau sgwrsio?** Pan fo prociau'n gwasgaru ar draws timau heb eu fersiynu ac wedi'u dyblygu, ni fydd trwsiad mewn un lle byth yn cyrraedd y lleill, ac ni all neb atgynhyrchu'r hyn y gofynnwyd i'r system ei wneud y chwarter diwethaf. I dîm mawr, cofrestrfa procio a rennir a chyfres atchweliad sy'n rhedeg ar bob newid yw'r hyn sy'n gadael i chi gyfnewid model neu olygu cyfarwyddyd heb dorri nodwedd yn ddistaw dau dîm i ffwrdd. Y dynfa gystadleuol yw cyflymder: mae peirianwyr yn ailadrodd gyflymaf pan fyddant yn gludo procio a chyflenwi, felly cytunwch ble mae'r llinell rhwng arbrofion cyflym ac unrhyw beth sy'n cyffwrdd â defnyddwyr. Dewch â ble mae eich prociau'n byw mewn gwirionedd heddiw, a yw set werthuso'n giatio newidiadau, a sut yr ydych yn fersiynu'r corpws adferiad ochr yn ochr â'r procio. Mewn lleoliadau menter a llywodraeth, ychwanegwch y gofyniad archwilio: efallai y bydd yn rhaid i chi ddangos yn union pa brocio a pha ffynonellau a gynhyrchodd allbwn penodol fisoedd yn ddiweddarach, ac mae procio na allwch ei ailadeiladu'n gofnod na allwch ei amddiffyn.

5. **Wrth i gyfaint dyfu, sut y byddwn yn rheoli cost casgliad heb ddirywio ansawdd yn ddistaw, a phwy sy'n berchen ar y penderfyniad dewis-model?** Cost cyfanswm perchnogaeth ar gyfer nodweddion LLM sy'n cael ei dominyddu gan gasgliad fesul-galwad, ac mae costau sy'n edrych yn ddibwys mewn peilot yn cyfansymio'n gyflym ar raddfa cynhyrchu, gan demtio timau i ollwng yn ddistaw i fodel gwannach a gobeithio na fydd neb yn sylwi ar y llithriad ansawdd. I sefydliad mawr, mae gadael i bob tîm ddewis modelau a therfynau cost yn ôl teimlad yn cynhyrchu biliau annisgwyl ac ansawdd anghyson fel ei gilydd. Y cyfaddawd gwirioneddol yw gallu yn erbyn cost ac oedi: mae model mwy'n rhesymu'n well ar dasgau anodd, mae un lleiaf yn rhatach ac yn gyflymach ar rai syml, ac mae storfa dros dro, llwybro, a chwmpas adferiad i gyd yn symud y ffigur. Dewch â chost fesul tasg wedi'i datrys, ansawdd yn ôl haen model ar eich set werthuso, a lle mae chwyddiant procio neu gyd-destun yn chwyddo gwariant tocyn. Mewn cyllidebu menter a llywodraeth, enwch pwy sy'n cymeradwyo'r dewis model a'r nenfwd gwariant, gan fod llinell gost nad oes neb yn berchen arni'n un nad oes neb yn ei rheoli pan fo traffig yn treblu.

6. **Pa ddata sensitif all gyrraedd y model, i ble mae'r data hwnnw'n mynd, ac a allwn brofi iddo aros o fewn ffiniau?** Gall pob procio, dogfen a adferwyd, a chanlyniad teclyn gario data personol neu gyfrinachol i mewn i'r model ac, gyda darparwr a gynhelir, allan o'ch perimedr, ac mae gollyngiad yma'n ddigwyddiad cyfreithiol neu ddiogelwch, nid tocyn diffyg. I dîm mawr sy'n gwifro LLMs i mewn i systemau mewnol, mae'r risg yn cuddio yn y plymio: corpws adferiad sy'n cynnwys cofnodion na ddylai defnyddiwr penodol byth eu gweld, neu logiau sy'n dal mewnbynnau crai. Y tyndra yw gallu yn erbyn agoredrwydd, gan y gall dad-adnabod a chwmpasu tynn bylu'r nodwedd yr ydych yn ceisio ei hadeiladu. Dewch â map llif-data o'r hyn sy'n dod i mewn i'r cyd-destun, telerau cadw a hyfforddi'r darparwr, a sut yr ydych yn dad-adnabod, cwmpasu, a chofnodi meysydd sensitif. Mewn lleoliadau rheoledig a chyhoeddus, cydiwch hyn wrth reolau preswyliad-data, dyletswyddau cadw-cofnodion, a chyfyngiadau contractol ar sut y caiff gwerthwr ddefnyddio eich data, gan fod goruchwyliaeth na allwch ei dystiolaethu'n oruchwyliaeth nad oes gennych.

## Lens sector

**Cwmni newydd.** Cyflenwch un nodwedd LLM gul sy'n cyffwrdd â'ch gwerth craidd, wedi'i hadeiladu ar fodel a gynhelir gydag adferiad dros eich cynnwys eich hun, a chadwch brociau mewn git y tu ôl i ryngwyneb tenau fel y gallwch gyfnewid darparwyr. Rhedwch ffeil werthuso fach o gwestiynau go iawn cyn pob newid, hidlwch destun defnyddiwr wedi'i gludo i bylu chwistrelliad procio, a chapiwch wariant misol yn galed. Gwrthwynebwch asiantau a hunan-westeio: mae dolen alw-teclyn heb ffin na allwch ei goruchwylio'n atebolrwydd, nid demo.

**Busnes bach.** Mae'n debyg nad oes gennych arbenigwr ML, felly prynwch nodweddion LLM wedi'u mewnblannu mewn offer yr ydych eisoes yn eu defnyddio yn hytrach na staffio adeiladwaith. Fframiwch y risg fel cwestiwn plaen: lle byddai ateb anghywir hyderus yn costio cwsmer i chi, a phwy sy'n gwirio'r allbwn cyn iddo fynd allan. Ffafriwch werthwyr sy'n dangos eu ffynonellau, yn gadael i chi gadw person yn y ddolen, ac yn gwneud yr AI yn hawdd ei ddiffodd pan fo'n camymddwyn.

**Menter.** Y broblem yw graddfa ar draws llawer o dimau: cyhoeddwch batrymau a rennir ar gyfer RAG, giatiau gwarchod, a sgemâu teclyn, ynghyd â harnais gwerthuso cyffredin a chofrestrfa procio fel bod pob grŵp yn peidio ag ailddarganfod yr un moddau methiant. Cyllidebwch gost casgliad ac adolygiad dynol yn benodol, safonwch yr haen rhyngwyneb fel bod modelau'n aros yn gyfnewidiadwy, a llywodraethwch asiantau'n ganolog â braint leiaf, dolenni ffiniedig, a chofnodi archwilio. Rheolwch nodweddion LLM fel portffolio â metrigau a meini prawf lladd, nid gwasgariad o beilotiaid.

**Llywodraeth.** Mae tryloywder, rheolau caffael, ac atebolrwydd yn siapio pob dewis. Gwreiddiwch yn llym mewn ffynonellau cymeradwy â dyfyniadau, gwrthodwch pan fo adferiad yn dod yn wag, a gwaherddwch y model rhag datgan cyfraith na all ei ddyfynnu. Cadwch swyddog atebol yn adolygu allbynnau canlyniadol, cofnodwch fewnbynnau a ffynonellau a adferwyd ar gyfer archwilio, rhedwch set werthuso wrthwynebus cyn pob rhyddhad, a mynnwch ddatgeliad cyfyngiadau model a thelerau trin-data yn y contract.

## Enghreifftiau

**Cwmni newydd.** Ychwanegodd cwmni newydd offer-datblygu tri-pherson gynorthwyydd sgwrsio dros ei ddogfennau ei hun fel y gallai defnyddwyr stopio e-bostio cwestiynau sylfaenol. Defnyddiodd RAG fel bod pob ateb yn dyfynnu tudalen ddogfen benodol, gorchmynnodd i'r model ddweud "Nid wyf yn siŵr, dyma pwy i ofyn" pan ddôi adferiad yn wag, a chadwodd ei brociau mewn git. Cyn pob newid rhedodd y prociau yn erbyn ffeil fach o gwestiynau defnyddwyr go iawn i ddal atchweliadau, a hidlodd destun wedi'i gludo gan ddefnyddwyr i bylu chwistrelliad procio. Trafododd y cynorthwyydd y cwestiynau cyffredin a phasiodd y gweddill yn ddistaw i flwch derbyn a rennir y sylfaenwyr.

**Menter.** Adeiladodd cwmni meddalwedd gynorthwyydd cymorth mewnol dros ei ddogfennaeth cynnyrch. Defnyddiodd [RAG](https://en.wikipedia.org/wiki/Retrieval-augmented_generation) fel bod atebion yn dyfynnu tudalennau dogfen penodol, gorchmynnodd i'r model ddweud "Nid wyf yn gwybod" pan fethodd adferiad, a gwiriodd fod pob ffynhonnell a ddyfynnwyd mewn gwirionedd yn bodoli. Roedd prociau wedi'u rheoli-fersiwn ac wedi'u profi yn erbyn cyfres o gwestiynau cymorth go iawn ar bob newid. Gwyrodd y cynorthwyydd docynnau arferol ac uwchgyfeiriodd unrhyw beth hyder-isel i asiantau dynol, tra bo metrigau ar-lein yn olrhain cyfraddau datrys a chywiro.

**Llywodraeth.** Defnyddiodd asiantaeth gyhoeddus gynorthwyydd LLM i helpu staff ddrafftio ymatebion i ymholiadau dinasyddion. Roedd gwreiddio'n llym: ni allai'r model ond cyfansoddi atebion o ganllawiau cymeradwy â dyfyniadau, ac fe'i gwaharddwyd rhag datgan polisi nad oedd yn bresennol yn y ffynonellau a adferwyd. Adolygodd swyddog atebol bob drafft cyn iddo fynd allan. Gwarchododd hidlo mewnbwn yn erbyn chwistrelliad procio o ddogfennau a gyflwynwyd gan ddinasyddion, cofnodwyd allbynnau ar gyfer archwilio, a rhedodd set werthuso o ymholiadau gwrthwynebus ac achos-ymyl cyn pob rhyddhad i gadarnhau bod y system yn gwrthod dyfalu ar faterion cyfraith.

## Achos busnes: cymhellion, ROI, a TCO

Mae cymhwysiadau LLM yn cyflenwi ROI trwy awtomeiddio gwaith iaith-drwm: ateb cwestiynau, crynhoi dogfennau, drafftio cynnwys, a thynnu strwythur o destun anstrwythuredig. Mae gwerth yn ymddangos fel tocynnau a wyrwyd, drafftio cyflymach, llai o adolygiad llawlyfr, a galluoedd hunanwasanaeth newydd. Gan nad oes yn aml gam hyfforddi, mae amser i werth cyntaf yn fyr, atyniad mawr.

Fodd bynnag, mae TCO'n cael ei dominyddu gan gost casgliad parhaus, seilwaith adferiad, piblinellau gwerthuso, systemau giât gwarchod, ac adolygiad dynol. Mae costau fesul-galwad yn cronni'n gyflym ar raddfa, a gall cymhwysiad heb ei fonitro wyro i mewn i ymddygiad anniogel neu ddrud. Cost peidio â mabwysiadu yw syrthio ar ei hôl hi ar ansawdd gwasanaeth a chynhyrchedd staff. Cost mabwysiadu'n ddiofal yw digwyddiad rhithweledigaeth gyhoeddus neu ollyngiad data. Gwnewch yr achos i arweinyddiaeth trwy baru targed cynhyrchedd pendant â chynllun diogelwch a gwerthuso pendant, a thrwy gyllidebu ar gyfer y giatiau gwarchod a'r oruchwyliaeth ddynol sy'n cadw'r gwerth yn barhaol.

## Gwrth-batrymau a pheryglon

- **Ymddiried mewn allbwn rhugl.** Camgymryd testun hyderus, wedi'i ysgrifennu'n dda am destun cywir.
- **RAG heb werthusiad adferiad.** Tybio bod adferiad yn gweithio a byth yn gwirio a yw'n dwyn i'r amlwg y darnau cywir.
- **Dallineb chwistrelliad procio.** Bwydo cynnwys heb ei ymddiried i mewn i brociau heb amddiffynfeydd.
- **Asiantau di-ffin.** Gadael i asiantau gymryd gweithredoedd canlyniadol heb derfynau na chymeradwyaeth ddynol.
- **Dim harnais gwerthuso.** Newid prociau a modelau yn ôl teimlad, heb brofi atchweliad.
- **Gwasgariad procio.** Prociau wedi'u gwasgaru, heb eu fersiynu, ac wedi'u dyblygu ar draws timau.
- **Gor-awtomeiddio.** Tynnu pobl allan o benderfyniadau sy'n cario pwysau cyfreithiol neu ddiogelwch.

## Model aeddfedrwydd

1. **Cychwyn.** Procio digyswllt mewn prosiectau ynysig; dim gwreiddio, giatiau gwarchod, na gwerthuso; mae prociau'n byw lle bynnag y gludodd rhywun hwy, a chanfyddir rhithweledigaethau mewn cynhyrchu.
2. **Datblygu.** Mae rhai timau'n ychwanegu RAG a fersiynu procio, dilysiad allbwn sylfaenol, a set werthuso lawlyfr fach, ond mae arferion yn amrywio o dîm i dîm ac yn gorffwys ar hyrwyddwyr unigol yn hytrach na disgwyliad a rennir.
3. **Safoni.** Gorfodir patrymau wedi'u dogfennu ar gyfer RAG, giatiau gwarchod, sgemâu teclyn, a fersiynu procio ar draws y sefydliad; mae gwerthusiad all-lein awtomataidd yn rhedeg ar bob newid procio neu fodel; mae llifau risg-uchel yn cario metrigau ar-lein ac adolygiad dynol.
4. **Rheoli.** Mesurir y portffolio yn erbyn llinellau sylfaen: olrheinir adalw adferiad, cyfraddau rhithweledigaeth a gwrthodiad, cwmpasiad amddiffyn-chwistrelliad, cost ac oedi fesul-galwad, a chyfraddau uwchgyfeirio a chywiro ar ddangosfyrddau; mae giatiau rhyddhau a meini prawf lladd yn tanio ar dystiolaeth yn hytrach na barn, ac mae rhediad atchweliad yn blocio unrhyw newid sy'n symud metrig y ffordd anghywir.
5. **Cyfundrefnu.** Mae gwerthusiad all-lein ac ar-lein parhaus wedi'i gydio wrth ganlyniadau busnes; mae amddiffynfeydd chwistrelliad, asiantau, a gwreiddio wedi'u llywodraethu a'u harsylwi; mae'r sefydliad yn arferol yn ymddeol, yn ail-diwnio, ac yn ailgwmpasu nodweddion LLM, ac yn cyfnewid modelau wrth i ansawdd, cost, a risg newid.

## Syniadau ar gyfer trafodaeth

- Sut yr ydych yn penderfynu pa allbynnau sy'n mynnu adolygiad dynol cyn eu defnyddio?
- Beth yw eich safon ar gyfer "wedi'i wreiddio digon" cyn y gellir dangos ateb i ddefnyddwyr?
- Sut yr ydych yn amddiffyn yn erbyn chwistrelliad procio pan fo'n rhaid i gynnwys heb ei ymddiried ddod i mewn i'r cyd-destun?
- Pryd y mae asiant yn werth ei risg ychwanegol o'i gymharu â dyluniad symlach, un-galwad?
- Sut yr ydych yn gwerthuso ansawdd goddrychol ar raddfa heb ddibynnu gormod ar raddio seiliedig-ar-fodel?
- Sut yr ydych yn cadw prociau'n gynaliadwy ac yn gyson ar draws llawer o dimau?

## Casgliadau allweddol

- Daw dibynadwyedd o'r beirianneg o amgylch y model: cyd-destun, gwreiddio, giatiau gwarchod, a gwerthuso.
- Mae RAG yn gwreiddio atebion mewn ffynonellau ymddiriedol ac yn galluogi dyfynnu a gwiriad.
- Triniwch y model fel cydran heb ei ymddiried; dilyswch allbynnau a chyfyngwch ddefnydd teclyn.
- Rhowch i asiantau fraint leiaf, dolenni ffiniedig, a chymeradwyaeth ddynol ar gyfer gweithredoedd canlyniadol.
- Gwerthuswch all-lein, ar-lein, a chyda phobl yn barhaus; dyma'r hyn sy'n gwneud newid yn ddiogel.

## Cyfeiriadau a darllen pellach

- Patrick Lewis et al., *Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks*.
- Jason Wei et al., *Chain-of-Thought Prompting Elicits Reasoning in Large Language Models*.
- OWASP Foundation, *OWASP Top 10 for Large Language Model Applications*.
- Chip Huyen, *AI Engineering: Building Applications with Foundation Models*.
- Anthropic, *Building Effective Agents* (engineering guidance).
- Louis-François Bouchard and Louie Peters, *Building LLMs for Production*.
