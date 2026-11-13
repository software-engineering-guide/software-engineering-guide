# 8.4 Peirianneg platfform a phrofiad datblygwyr

## Trosolwg a chymhelliant

Mae [peirianneg platfform](https://en.wikipedia.org/wiki/Platform_engineering) yn ddisgyblaeth adeiladu a rhedeg cynnyrch mewnol, platfform datblygwyr mewnol (IDP), y mae peirianwyr eraill yn ei ddefnyddio i adeiladu, rhyddhau, a gweithredu eu meddalwedd. Yn hytrach na phob tîm yn cydosod ei biblinellau, ei seilwaith, a'i offer ei hun o'r cychwyn, mae tîm platfform penodedig yn darparu galluoedd hunanwasanaeth, curedig ar hyd "llwybrau euraidd" wedi'u cefnogi'n dda, sy'n llwybrau barn, wedi'u cefnogi gyda rhagosodiadau synhwyrol wedi'u pobi i mewn. [Profiad datblygwyr](https://en.wikipedia.org/wiki/Developer_experience) (DevEx) yw'r pryder cysylltiedig agos ynghylch sut mae'n teimlo i fod yn beiriannydd yn y sefydliad: pa mor hawdd ac yn gyflym y gall datblygwr fynd o syniad i feddalwedd sy'n rhedeg, a faint o ffrithiant sy'n sefyll yn y ffordd.

I dimau mawr, mae hyn yn bwysig oherwydd nad yw [llwyth gwybyddol](https://en.wikipedia.org/wiki/Cognitive_load) a ffrithiant yn graddio'n raslon. Pan fydd gennych lawer o dimau, mae nifer yr offer, y systemau, a'r penderfyniadau y mae'n rhaid i bob peiriannydd eu jyglo'n parhau i dyfu. Cyn hir, mae cyfran fawr o'u hamser yn mynd i blymio seilwaith a chydgysylltu yn hytrach na chyflenwi gwerth. Heb blatfform, mae pob tîm yn datrys yr un problemau, megis darparu, defnyddio, arsylladwyedd, a chydymffurfiaeth, yn anghyson ac yn ailadroddus. Mae platfform da'n amsugno'r cymhlethdod a rennir hwn. Yna gall timau ganolbwyntio ar eu maes tra'n dal i etifeddu safonau'r sefydliad ar gyfer diogelwch, dibynadwyedd, a chost.

Mae perthnasedd menter fawr a llywodraeth yn uchel, gan fod y sefydliadau hyn yn cyfuno graddfa â llywodraethu llym. Platfform yw'r lle naturiol i amgodio gofynion cydymffurfiaeth, diogelwch, ac archwilio unwaith, fel ffyrdd wedi'u palmantu y mae timau'n eu dilyn yn ddiofyn. Mae hynny'n well na disgwyl i bob tîm ddehongli a gweithredu polisi'n gywir ar ei ben ei hun. Mae'n troi llywodraethu o ffynhonnell ffrithiant yn briodwedd anweledig o'r llif gwaith safonol, yn union yr hyn sydd ei angen ar sefydliadau mawr, rheoledig i symud yn gyflym heb golli rheolaeth.

## Egwyddorion allweddol

- Triniwch y platfform fel cynnyrch, gyda defnyddwyr, map ffordd, a mandad i ennill mabwysiad yn hytrach na'i orfodi.
- Darparwch lwybrau euraidd: llwybrau barn, wedi'u cefnogi'n dda sy'n gwneud y ffordd gywir yn ffordd hawdd.
- Gwnewch alluoedd yn hunanwasanaeth fel nad yw timau'n aros am docynnau a throsglwyddiadau dynol.
- Palmantwch ffyrdd yn hytrach na chodi gatiau; adeiladwch reiliau diogelwch sy'n arwain heb rwystro gwaith cyfreithlon.
- Lleihewch lwyth gwybyddol ar ddatblygwyr cymwysiadau yn ddidostur.
- Mesurwch brofiad datblygwyr a chynhyrchedd â signalau cytbwys, aml-ddimensiynol.
- Cadwch lwybrau euraidd yn ddewisol ond mor dda fel bo timau'n eu dewis.

## Argymhellion

### Adeiladwch y platfform fel cynnyrch

Y symudiad pwysicaf sengl yw trin y platfform fel cynnyrch sy'n gwasanaethu cwsmeriaid mewnol, nid fel safon orfodol wedi'i gosod o'r brig. Yn ymarferol, mae hynny'n golygu deall anghenion datblygwyr drwy ymchwil ac adborth, cynnal map ffordd, mesur mabwysiad a boddhad, a bod yn atebol am y profiad. Bydd platfform y gorfodir timau i'w ddefnyddio ond sy'n eu harafu'n cael ei ddrwgdeimlo a'i lwybro o'i gwmpas. Bydd platfform sy'n gwneud timau'n gyflymach mewn gwirionedd yn lledaenu drwy enw da. Mabwysiad a enillwyd drwy ansawdd yw'r mesur gwirioneddol o lwyddiant platfform.

### Darparwch lwybrau euraidd a ffyrdd wedi'u palmantu

Diffiniwch lwybrau euraidd ar gyfer y teithiau cyffredin: creu gwasanaeth newydd, ei ddefnyddio, ychwanegu cronfa ddata, cysylltu arsylladwyedd, bodloni gofynion cydymffurfiaeth. Mae llwybr euraidd yn llwybr wedi'i gefnogi, barn, o ben i ben gyda rhagosodiadau synhwyrol wedi'u pobi i mewn. Ar hyd y llwybrau hyn, ymgorffolwch reiliau diogelwch, sef sganio diogelwch, gwiriadau polisi, ac arferion gorau, fel bo tîm sy'n dilyn y llwybr yn cydymffurfio ac yn ddiogel yn awtomatig. Mae'r nod yn syml: dylai'r ffordd hawsaf o wneud rhywbeth fod hefyd yn ffordd gywir, ddiogel, gydymffurfiol. Cadwch y llwybrau'n ddewisol, fel bo timau ag anghenion gwirioneddol anghyffredin yn gallu gwyro. Ond gwnewch y llwybrau'n ddigon deniadol fel na fydd y rhan fwyaf o dimau byth am wneud hynny.

### Cyflenwch seilwaith hunanwasanaeth gwirioneddol

Dilëwch drosglwyddiadau tocyn-ac-aros drwy amlygu seilwaith a galluoedd drwy ryngwynebau hunanwasanaeth: porth, offeryn llinell-orchymyn, API, neu ystorfeydd templed. Dylai datblygwr allu darparu amgylchedd cydymffurfiol, cychwyn gwasanaeth newydd o dempled, neu ofyn am gronfa ddata mewn munudau, heb gyflwyno cais ac aros ddyddiau am dîm arall. Hunanwasanaeth yw'r hyn sy'n troi platfform o dagfa yn gyflymydd. Ac mae ond yn gweithio oherwydd bod y reiliau diogelwch sylfaenol yn gwneud hunanwasanaeth yn ddiogel.

### Cynigiwch byrth datblygwyr, catalogau gwasanaeth, a chardiau sgorio

Mae porth datblygwr yn rhoi un cwarel gwydr ichi: catalog o'r holl wasanaethau â'u perchnogion, dogfennaeth, dibyniaethau, ac iechyd. Mae catalogau gwasanaeth yn gwneud perchnogaeth a phensaernïaeth yn ddarganfyddadwy. Mae hynny'n amhrisiadwy ar raddfa fawr, lle na all neb ddal y system gyfan yn eu pen. Mae cardiau sgorio'n mesur pob gwasanaeth yn erbyn safonau megis cwmpas profion, ystum diogelwch, parodrwydd galwad-ar-ddyletswydd, a dogfennaeth, ac yn rhoi darlun clir, gwrthrychol i dimau o ble maen nhw'n sefyll a beth i'w wella. Gyda'i gilydd, mae'r offer hyn yn torri'r amser y mae peirianwyr yn ei dreulio'n hela am wybodaeth, ac maen nhw'n egluro atebolrwydd.

### Mesurwch brofiad datblygwyr â fframweithiau cytbwys

Gwrthsafwch fetrigau cynhyrchedd un-rhif. Maen nhw'n hawdd eu chwarae ac yn gamarweiniol. Defnyddiwch fframweithiau aml-ddimensiynol megis SPACE (boddhad a llesiant, perfformiad, gweithgaredd, cyfathrebu a chydweithio, effeithlonrwydd a llif) i ddal gwir wead profiad datblygwyr. Cyfunwch ddata canfyddiadol o arolygon â data system o offer. Dilynwch fetrigau cyflenwi megis amser arwain a mynychder defnyddio ochr yn ochr â theimlad datblygwyr. Y nod yw deall a symud ffrithiant, nid rhestru unigolion. Bydd mesur sy'n teimlo fel gwyliadwriaeth yn erydu'r ymddiriedaeth y mae'r platfform yn dibynnu arni.

### Lleihewch lwyth gwybyddol fel nod dosbarth cyntaf

Llwyth gwybyddol, cyfanswm yr ymdrech feddyliol y mae'n rhaid i ddatblygwr ei gwario i wneud ei waith, yw'r dreth gudd y mae platfformau'n bodoli i'w lleihau. Lleihewch nifer yr offer, cysyniadau, a newidiadau cyd-destun y mae'n rhaid i ddatblygwr cymhwysiad eu meistroli. Darparwch ragosodiadau synhwyrol, fel bo timau'n gwneud llai o benderfyniadau gwerth isel. Strwythurwch berchnogaeth fel bo pob tîm yn berchen ar sleisen ffiniedig, ddealladwy o'r system. Pan fyddwch yn gwerthuso unrhyw nodwedd platfform, gofynnwch un cwestiwn: a yw'n lleihau neu'n cynyddu'r llwyth ar y timau a fydd yn ei ddefnyddio?

## Cyfaddawdau: manteision ac anfanteision

| Dewis | Manteision | Anfanteision | Ffit gorau |
|---|---|---|---|
| Platfform fel cynnyrch (optio i mewn) | Yn ennill mabwysiad; yn aros yn ddefnyddiol | Arafach i gyrraedd cwmpas llawn | Y rhan fwyaf o sefydliadau |
| Platfform gorfodol | Safoni cyflym | Drwgdeimlad; gweithdrefnau amgen | Anghenion llywodraethu cryf yn unig |
| Prynu porth/platfform | Cyflymach i werth | Llai wedi'i deilwra; cost trwyddedu | Timau am ben cychwyn |
| Adeiladu'n fewnol | Yn ffitio anghenion union | Cost adeiladu a chynnal a chadw uchel | Sefydliadau mawr, nodedig |
| Llwybrau euraidd anhyblyg yn unig | Cysondeb mwyaf | Yn rhwystro achosion ymyl cyfreithlon | Llwythi gwaith hynod unffurf |
| Llwybrau hyblyg ag allanfeydd dianc | Yn cydbwyso cysondeb ac ymreolaeth | Rhywfaint o wyriad i'w reoli | Anghenion tîm amrywiol |

Y tyndra craidd yw safoni yn erbyn ymreolaeth. Rhy ychydig o safoni, a bydd pob tîm yn ailddyfeisio'r olwyn yn anghyson. Gormod, a byddwch yn mygu'r timau y mae eu hanghenion mewn gwirionedd yn wahanol. Mae'r athroniaeth platfform-fel-cynnyrch yn datrys hyn drwy wneud safoni'n ddeniadol yn hytrach nag yn orfodol. Ail gyfaddawd gwirioneddol yw adeiladu yn erbyn prynu. Mae adeiladu platfform mewnol yn ffitio eich anghenion union ond mae'n cario cost barhaus sylweddol. Mae mabwysiadu offer sy'n bodoli'n cyflymu gwerth, ar bris rhywfaint o deilwra.

## Cwestiynau i'w trafod gyda'ch tîm

1. **Sut y byddwch yn gwybod bod y platfform yn lleihau llwyth gwybyddol yn hytrach nag ychwanegu un offeryn arall i'w ddysgu?** Llwyth gwybyddol yw cyfanswm yr ymdrech feddyliol y mae peiriannydd yn ei gwario i wneud y gwaith, a gall platfform sy'n ychwanegu cysyniadau a newidiadau cyd-destun ei wneud yn waeth hyd yn oed tra'n edrych yn drawiadol. Mabwysiadwch un prawf ar gyfer pob nodwedd: a yw'n lleihau neu'n cynyddu'r llwyth ar y timau sy'n ei ddefnyddio? Ar raddfa fawr mae hyn yn benderfynol, oherwydd mae platfform yn eistedd o flaen cannoedd o beirianwyr ac mae haniaeth ddryslyd yn trethu pob un ohonynt bob dydd. Dewch â thystiolaeth: faint o offer a phyrth y mae datblygwr yn eu cyffwrdd i ryddhau newid, amser-i-ryddhau-cyntaf ar gyfer aelod newydd, ac adborth ansoddol ar ble mae pobl yn mynd yn sownd. Os yw'r platfform yn tyfu'r gadwyn offer yn hytrach na'i chrebachu, rydych wedi adeiladu treth, nid ffordd wedi'i phalmantu.

2. **Pa safonau mae eich cardiau sgorio'n eu gorfodi, a beth mewn gwirionedd sy'n digwydd i wasanaeth sy'n sgorio'n wael?** Mae cardiau sgorio'n mesur pob gwasanaeth yn erbyn disgwyliadau megis cwmpas profion, ystum diogelwch, parodrwydd galwad-ar-ddyletswydd, a dogfennaeth, ac mae eu gwerth yn cwympo os nad oes canlyniad i sgôr goch. Penderfynwch a yw cardiau sgorio'n gynghorol yn unig, yn bwydo i mewn i adolygiad, neu'n gatio galluoedd penodol, a phenderfynwch pwy sy'n berchen ar y safonau. Mewn sefydliadau rheoledig gall cardiau sgorio roi gwelededd parhaus i gyrff goruchwylio i mewn i ystum cydymffurfiaeth, gan ddisodli adrodd â llaw, felly mae'r safon a osodwch yn bwysig. Dewch â'ch safonau drafft a sampl o wasanaethau gwirioneddol wedi'u sgorio yn eu herbyn, a thrafodwch lle byddai timau'n gwrthwynebu'n gyfreithlon. Mae cerdyn sgorio nad oes neb yn gweithredu arno'n ddangosfwrdd; mae cerdyn sgorio wedi'i glymu wrth ddisgwyliadau clir yn newid ymddygiad.

3. **A ydych chi'n rhedeg y platfform fel cynnyrch go iawn, gyda map ffordd, ymchwil defnyddwyr, a metrigau mabwysiad, neu fel mandad?** Bet ganolog y bennod hon yw y dylai safoni fod yn ddeniadol yn hytrach na'i orfodi, a dim ond os byddwch yn trin peirianwyr mewnol fel cwsmeriaid y mae'n rhaid ichi eu hennill y mae hynny'n dal. Penderfynwch pwy sy'n chwarae rheolwr cynnyrch ar gyfer y platfform, sut rydych yn casglu anghenion datblygwyr, a pha rifau mabwysiad a boddhad sy'n diffinio llwyddiant. I sefydliadau mawr mae mandad yn demtasiwn oherwydd ei fod yn safoni'n gyflym, ond mae'n bridio gweithdrefnau amgen a drwgdeimlad pan fydd yr offer yn arafu pobl. Dewch â chyfraddau mabwysiad gwirfoddol presennol, signalau boddhad, a phrif bwyntiau ffrithiant y mae timau'n eu hadrodd heddiw. Os byddai timau'n gadael y platfform y foment y codir y mandad, nid ydych wedi adeiladu cynnyrch, rydych wedi adeiladu polisi.

4. **Pan fydd tîm yn cyrraedd ymyl llwybr euraidd, beth yw'r allanfa ddianc, a phwy sy'n penderfynu a ddylid lledu'r llwybr neu ddal y llinell?** Mae llwybr euraidd yn llwybr wedi'i gefnogi, barn gyda rhagosodiadau synhwyrol, ac mae ei werth yn dod o'r rhan fwyaf o dimau'n aros arno, eto mae llwybr heb allanfa'n troi'n giât sy'n gwthio gwaith gwirioneddol anghyffredin oddi ar y platfform yn llwyr. Cytunwch ymlaen llaw sut mae tîm yn gofyn am wyriad, pwy sy'n ei adolygu, a sut rydych yn gwahaniaethu rhwng eithriad unigryw ac arwydd y dylai'r llwybr ei hun newid. I sefydliad mawr, dyma'r gwahaniaeth rhwng platfform sy'n amsugno amrywiaeth ac un sy'n chwalu'n offer cysgod y foment y bydd tîm yn teimlo eu bod wedi'u rhwystro. Dewch â'r cyfrif presennol o dimau sydd wedi mynd oddi ar y llwybr, y rhesymau a roddon nhw, a pha mor hir mae eithriad yn ei gymryd i'w gymeradwyo. Mewn lleoliadau menter fawr a llywodraeth, cysylltwch bob allanfa ddianc â'r rheolaethau cydymffurfiaeth y mae'n eu hosgoi, fel na fydd gwyriad o'r ffordd wedi'i phalmantu byth yn dawel yn dod yn wyriad o'r llinell sylfaen diogelwch neu achredu.

5. **A ydych chi'n adeiladu'r platfform yn fewnol neu'n ei brynu, ac a ydych chi wedi prisio'n onest gost barhaus y naill lwybr neu'r llall?** Mae'r platfform ei hun yn gynnyrch â chylch bywyd, ac mae'r dewis adeiladu-yn-erbyn-prynu'n gosod eich strwythur cost am flynyddoedd: mae porth mewnol yn ffitio eich anghenion union ond mae'n gofyn am dîm â chyllid i'w gynnal, tra bo platfform a brynwyd yn cyrraedd gwerth yn gyflymach am bris trwyddedu a ffit nad yw byth yn berffaith. Penderfynwch pa alluoedd sy'n ddigon gwahaniaethol i'w hadeiladu a pha rai sy'n nwydd y dylech ei brynu, ac ailymwelwch â'r llinell honno wrth i werthwyr aeddfedu. I dîm mawr, y risg yw trosoledd: mae penderfyniad adeiladu anghywir yn suddo peirianwyr uwch prin i mewn i blymio y byddai cynnyrch wedi'i drin, tra bo penderfyniad prynu anghywir yn cloi cannoedd o ddatblygwyr i mewn i fap ffordd rhywun arall. Dewch ag amcangyfrif cyfanswm cost realistig ar gyfer pob opsiwn, gan gynnwys cynnal a chadw, uwchraddiadau, a chost gadael. Mewn caffael menter fawr a llywodraeth, ychwanegwch delerau achredu a chludadwyedd data, a ffafriwch gontractau sy'n gadael ichi adael heb adael y catalog gwasanaeth a'r cardiau sgorio rydych wedi'u hadeiladu ar ei ben.

6. **Sut mae'r tîm platfform yn cael ei gyllido a'i faint o'i gymharu â'r datblygwyr y mae'n eu gwasanaethu, a beth sy'n digwydd iddo pan fydd cyllidebau'n tynhau?** Mae platfform yn ennill ei gadw drwy drosoledd, gan fod tîm bach yn lluosi cynhyrchedd poblogaeth lawer mwy o ddatblygwyr cymwysiadau, ond mae'r un fframio hwnnw'n ei wneud yn darged hawdd pan fydd cyllid yn chwilio am doriadau a'r budd yn wasgaredig yn hytrach na phriodoladwy i un llinell gynnyrch. Penderfynwch y model cyllido, cymhareb peirianwyr platfform i'r datblygwyr maen nhw'n eu cefnogi, a sut y byddwch yn amddiffyn y buddsoddiad hwnnw â thystiolaeth yn hytrach na ffydd. I sefydliad mawr, mae platfform â diffyg cyllid yn waeth na dim: mae timau'n dibynnu arno, mae'n dirywio, ac mae'r ffrithiant yn dychwelyd â dibyniaeth ynghlwm. Dewch â phen-cyfrif y platfform, ei duedd mabwysiad a boddhad, ac amcangyfrif o oriau datblygwyr a adferwyd ar draws y sefydliad. Mewn llywodraeth a mentrau rheoledig, fframiwch y platfform fel y lle y caiff cydymffurfiaeth ei amgodio unwaith, felly nid yw ei dorri'n arbed arian, mae'n ail-wasgaru gwaith archwilio a diogelwch ar draws pob tîm sydd bellach yn gorfod ei wneud â llaw.

## Trwy lens sector

**Cwmni newydd.** Gyda llond dwrn o beirianwyr a dim rhedfa i'w sbario, peidiwch â sefydlu tîm platfform; adeiladwch un ystorfa dempled "gwasanaeth newydd" y gall gwasanaeth newydd ei glonio a rhedeg o fewn awr. Rhag-gysylltwch ef â CI, adeiladwaith cynhwysydd, leintio, a gwiriad iechyd, a gadewch iddo ledaenu oherwydd ei fod yn amlwg yn arbed amser, nid oherwydd bod unrhyw un yn ei orfodi. Prynwch bob gallu nwyddau y gallwch, cadwch y gadwyn offer yn fach, a thriniwch lwyth gwybyddol, nid cwmpas, fel y peth i'w ddiogelu.

**Busnes bach.** Nid oes gennych arbenigwr platfform penodedig a chyllideb dynn, felly pwyswch ar blatfform a reolir neu gynnig cwmwl barn yn hytrach nag adeiladu platfform datblygwyr mewnol eich hun. Fframiwch y penderfyniad fel prynu-yn-erbyn-adeiladu a rhagosodwch brynu: mae porth a brynwyd a'i dempledi'n rhoi llwybrau euraidd i'ch peirianwyr cyffredinol heb dîm i'w cynnal. Dewiswch offer sy'n hunanwasanaeth ac yn hawdd eu gadael, fel na fydd newid gwerthwr yn gadael y llond dwrn o wasanaethau rydych yn eu rhedeg yn sownd.

**Menter fawr.** Mae graddfa a llawer o dimau'n gwneud cysondeb portffolio'n wobr: tîm platfform â chyllid, llwybrau euraidd â reiliau diogelwch, darpariaeth hunanwasanaeth, catalog gwasanaeth, a chardiau sgorio sy'n gwneud perchnogaeth ac ansawdd yn weladwy ar draws cannoedd o wasanaethau. Rhedwch y platfform fel cynnyrch sy'n ennill mabwysiad gwirfoddol yn hytrach na mandad sy'n bridio gweithdrefnau amgen, ac amgodiwch ddiogelwch a chydymffurfiaeth unwaith fel ffyrdd wedi'u palmantu fel bo llywodraethu'n reidio ymlaen yn ddiofyn. Mesurwch brofiad datblygwyr â fframweithiau cytbwys ac amddiffynwch gyllid y platfform ag oriau datblygwyr a adferwyd.

**Llywodraeth.** Mae rheolau caffael, tryloywder, ac atebolrwydd cyhoeddus yn llunio'r platfform. Amgodiwch reolaethau diogelwch gorfodol a gofynion achredu fel reiliau diogelwch ar hyd y llwybrau euraidd, fel bo tîm sy'n darparu drwy'r porth hunanwasanaeth yn etifeddu amgylchedd sydd eisoes yn bodloni'r llinell sylfaen rheolaeth, gan droi misoedd o achredu â llaw yn gam awtomataidd i raddau helaeth. Defnyddiwch gardiau sgorio i roi gwelededd parhaus, archwiliadwy i gyrff goruchwylio i mewn i ystum cydymffurfiaeth, ac mewn caffael mynnwch gludadwyedd data a rhyngwynebau agored fel nad yw'r catalog a'r ffyrdd palmantog rydych yn eu hadeiladu wedi'u clymu i un cyflenwr.

## Enghreifftiau

**Cwmni newydd.** Nid oes gan gwmni newydd deuddeg person dîm platfform, felly mae un peiriannydd uwch yn treulio ychydig ddyddiau Gwener yn adeiladu un ystorfa dempled "gwasanaeth newydd" sy'n dod wedi'i rag-gysylltu â CI, Dockerfile, leintio, a gwiriad iechyd. Gall unrhyw beiriannydd ei glonio a chael gwasanaeth yn rhedeg mewn llwyfannu o fewn awr, yn hytrach na chopïo ffurfweddiad o hen brosiect a dyfalu'r bylchau. Y templed yw'r llwybr euraidd, ac oherwydd ei fod yn amlwg yn arbed amser i bawb, mae'r tîm cyfan yn ei fabwysiadu heb i unrhyw un gael ei ddweud wrtho.

**Menter fawr.** Mae cwmni yswiriant mawr yn ffurfio tîm platfform sy'n rhyddhau porth datblygwr mewnol. Mae'n catalogio pob gwasanaeth â'i berchennog, dogfennau, a cherdyn sgorio iechyd. Caiff gwasanaethau newydd eu creu o dempledi llwybr-euraidd sy'n dod wedi'u rhag-gysylltu â CI/CD, sganio diogelwch, arsylladwyedd, a gwiriadau cydymffurfiaeth. Caiff cronfeydd data ac amgylcheddau eu darparu drwy hunanwasanaeth drwy'r porth. Mae amser sefydlu ar gyfer peiriannydd newydd yn gostwng o wythnosau i ddyddiau, a chynhyrchir tystiolaeth archwilio'n awtomatig oherwydd bod pob gwasanaeth yn dilyn yr un ffordd wedi'i phalmantu. Mae mabwysiad platfform yn wirfoddol, ac mae'n lledaenu oherwydd bod timau sy'n ei ddefnyddio'n rhyddhau'n amlwg gyflymach.

**Llywodraeth.** Mae asiantaeth ffederal sy'n rhedeg dwsinau o wasanaethau digidol yn sefydlu platfform a rennir. Mae'n amgodio'r rheolaethau diogelwch gorfodol a'r gofynion achredu fel reiliau diogelwch ar hyd ei lwybrau euraidd. Mae tîm sy'n darparu seilwaith drwy'r porth hunanwasanaeth yn etifeddu amgylchedd sydd eisoes yn bodloni'r llinell sylfaen rheolaeth. Mae hynny'n troi ymarfer achredu â llaw sy'n para misoedd yn un awtomataidd i raddau helaeth. Mae cardiau sgorio'n dilyn ystum cydymffurfiaeth pob gwasanaeth, gan roi gwelededd parhaus i gyrff goruchwylio heb adrodd â llaw, a rhyddhau staff arbenigol prin o adolygiad ailadroddus.

## Achos busnes: cymhellion, ROI, a TCO

Daw ROI peirianneg platfform o amser datblygwyr a adferwyd a chysondeb a enillwyd. Pan fydd peirianwyr yn treulio llai o amser yn ymladd seilwaith ac yn chwilio am wybodaeth, mae mwy o'u hamser drud yn mynd i gyflenwi gwerth cynnyrch. Mae sefydlu cyflymach, llai o atebion dyblyg, a chydymffurfiaeth awtomataidd i gyd yn trosi'n gapasiti mesuradwy a risg lai. Gan fod y platfform yn gwasanaethu llawer o dimau, caiff pob gwelliant iddo ei drosoli ar draws y sefydliad cyfan.

O ran TCO, mae cost mabwysiadu'n fuddsoddiad go iawn, parhaus: tîm platfform â chyllid, offer (wedi'i adeiladu neu ei brynu), a'r ddisgyblaeth i redeg y platfform fel cynnyrch â gwelliant parhaus. Mae cost peidio â mabwysiadu'n wasgaredig ond yn fawr: pob tîm yn talu'r un dreth seilwaith dro ar ôl tro, diogelwch a chydymffurfiaeth anghyson, sefydlu araf, a pheirianwyr uwch yn llosgi allan ar drafferth. I arweinyddiaeth, gwneir yr achos orau o ran trosoledd. Mae tîm platfform cymedrol, sy'n cael ei redeg yn dda, yn lluosi cynhyrchedd poblogaeth lawer mwy o ddatblygwyr cymwysiadau, ac mae'n amgodio llywodraethu unwaith yn lle dibynnu ar bob tîm i'w gael yn iawn.

## Gwrthbatrymau a pheryglon

- **Platfform wedi'i orfodi, nid ei gynnig.** Mae gorfodi platfform nad yw datblygwyr yn ei hoffi'n bridio gweithdrefnau amgen a drwgdeimlad.
- **Tîm platfform tŵr ifori.** Mae adeiladu heb ddeall anghenion datblygwyr go iawn yn cynhyrchu offer nad oes neb eu heisiau.
- **Gatiau yn lle ffyrdd palmantog.** Mae reiliau diogelwch sy'n rhwystro gwaith cyfreithlon yn gwthio timau i osgoi'r platfform yn llwyr.
- **Metrig cynhyrchedd sengl.** Mae lleihau cynhyrchedd i un rhif y gellir ei chwarae'n ystumio ymddygiad ac yn erydu ymddiriedaeth.
- **Mesur fel gwyliadwriaeth.** Mae metrigau DevEx a ddefnyddir i restru unigolion yn dinistrio'r diogelwch seicolegol y mae'r platfform ei angen.
- **Llwybr euraidd heb allanfa ddianc.** Mae llwybrau anhyblyg na allant hyblygu ar gyfer achosion ymyl gwirioneddol yn dod yn rhwystrau.
- **Platfform â diffyg cyllid.** Mae trin y platfform fel prosiect ochr yn ei lwgu ac yn gwarantu profiad gwael.

## Model aeddfedrwydd

**Lefel 1: Cychwyn.** Nid oes platfform yn bodoli. Mae pob tîm yn cydosod ei offer a'i seilwaith ei hun yn adweithiol, gyda throsglwyddiadau trwm a yrrir gan docynnau, atebion dyblyg, a llwyth gwybyddol uchel. Mae pob tîm yn datrys darparu, defnyddio, a chydymffurfiaeth ar ei ben ei hun, yn anghyson.

**Lefel 2: Datblygu.** Mae rhai offer a rennir, templedi, ac ystorfeydd cychwynnol yn ymddangos, yn aml wedi'u hadeiladu gan beiriannydd brwdfrydig, ond maen nhw'n dameidiog ac yn rhannol â llaw. Mae rhai timau'n mabwysiadu llwybr euraidd tra bo eraill yn ei anwybyddu, mae hunanwasanaeth yn gyfyngedig, ac ni chaiff profiad datblygwyr ei fesur, felly mae gwerth y platfform yn gorffwys ar chwedl.

**Lefel 3: Safoni.** Mae tîm platfform yn rhedeg llwybrau euraidd dogfennedig, darpariaeth hunanwasanaeth, porth datblygwr â chatalog gwasanaeth, a chardiau sgorio, wedi'u cymhwyso ar draws y sefydliad. Mae reiliau diogelwch ar gyfer diogelwch, polisi, a chydymffurfiaeth wedi'u hymgorffori yn y ffyrdd palmantog, felly'r llif gwaith safonol yw'r un cydymffurfiol, ac mae'r un confensiynau'n dal ar draws timau yn hytrach na newid fesul grŵp.

**Lefel 4: Rheoli.** Caiff y platfform ei fesur a'i reoli â data yn erbyn llinellau sylfaen. Caiff mabwysiad, boddhad, amser-i-ryddhau-cyntaf, amser arwain, a mynychder defnyddio eu dilyn â fframweithiau cytbwys megis SPACE a signalau arolwg a system wedi'u cyfuno; mae canlyniadau cardiau sgorio'n bwydo i mewn i adolygiad, a chaiff llwyth gwybyddol, amser sefydlu, ac oriau datblygwyr a adferwyd eu monitro yn erbyn targedau. Mae penderfyniadau i fuddsoddi mewn neu ddiddymu gallu yn gorffwys ar dystiolaeth, nid eiriolaeth.

**Lefel 5: Cydgysylltu.** Mae'r platfform yn gynnyrch aeddfed â mabwysiad gwirfoddol uchel, wedi'i wella'n barhaus o adborth a metrigau datblygwyr ac wedi'i integreiddio â diogelwch, cydymffurfiaeth, a chynllunio cyflenwi ar draws y sefydliad. Mae llwybrau euraidd yn addasu wrth i anghenion symud, mae llywodraethu'n briodwedd anweledig o'r llif gwaith safonol, ac mae'r tîm platfform yn rheolaidd yn diddymu, yn disodli, ac yn ailgwmpasu galluoedd wrth i'r dechnoleg a'r sefydliad esblygu.

## Syniadau i'w trafod

- Sut rydych yn ennill mabwysiad ar gyfer platfform heb ei orfodi, a phryd, os o gwbl, mae mandad yn gyfiawn?
- Pa lwybrau euraidd fyddai'n cyflenwi'r gwerth mwyaf i'ch timau yn gyntaf?
- Sut rydych yn mesur profiad datblygwyr heb iddo deimlo fel gwyliadwriaeth?
- Ble ddylai allanfeydd dianc fodoli fel nad yw timau anghyffredin yn cael eu gorfodi oddi ar y platfform yn llwyr?
- Beth yw'r maint a'r model cyllido cywir ar gyfer tîm platfform o'i gymharu â'r datblygwyr y mae'n eu gwasanaethu?
- Sut rydych yn penderfynu beth i'w adeiladu'n fewnol yn erbyn ei brynu ar gyfer eich porth a'ch offer datblygwyr?

## Prif negeseuon

- Rhedwch y platfform fel cynnyrch sy'n ennill mabwysiad drwy wneud timau'n wirioneddol gyflymach.
- Darparwch lwybrau euraidd a ffyrdd palmantog sy'n gwneud y ffordd gywir, ddiogel, gydymffurfiol yn ffordd hawdd.
- Cyflenwch hunanwasanaeth go iawn fel bo timau'n peidio ag aros am docynnau a throsglwyddiadau.
- Defnyddiwch byrth, catalogau, a chardiau sgorio i wneud perchnogaeth, pensaernïaeth, ac ansawdd yn weladwy.
- Mesurwch brofiad datblygwyr â fframweithiau cytbwys fel SPACE, byth un rhif y gellir ei chwarae.
- Triniwch leihau llwyth gwybyddol fel diben canolog y platfform.

## Cyfeiriadau a darllen pellach

- Matthew Skelton a Manuel Pais, *Team Topologies*.
- Nicole Forsgren, Margaret-Anne Storey, Chandra Maddila, et al., "The SPACE of Developer Productivity" (papur).
- Nicole Forsgren, Jez Humble, a Gene Kim, *Accelerate*.
- Gregor Hohpe, *The Software Architect Elevator*.
- Camille Fournier, *The Manager's Path*.
- Cloud Native Computing Foundation, papur gwyn peirianneg platfform.
