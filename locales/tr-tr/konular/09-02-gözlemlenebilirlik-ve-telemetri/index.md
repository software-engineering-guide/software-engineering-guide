# 9.2 Gözlemlenebilirlik ve telemetri

## Genel bakış ve motivasyon

[Telemetri](https://en.wikipedia.org/wiki/Telemetry), bir sistemin kendi davranışı hakkında yaydığı veridir: çalışan yazılımdan toplanan metrikler, günlükler, izler ve olaylar. İzleme, bu telemetriden zaten sormayı bildiğiniz soruları yanıtlar. Disk doldu mu? Hata oranı eşiğin üstünde mi? Hizmet ayakta mı? [Gözlemlenebilirlik](https://en.wikipedia.org/wiki/Observability_(software)) daha geniştir. Bir sistemin iç durumu hakkında dışarıdan, yeni kod sevk etmeden yeni sorular sorabilme yeteneğidir; böylece hiç öngörmediğiniz davranışları anlayabilirsiniz. Sistemler dağıtık, [mikro hizmet](https://en.wikipedia.org/wiki/Microservices) ve [olay güdümlü mimarilere](https://en.wikipedia.org/wiki/Event-driven_architecture) büyüdükçe, en çok acıtan arızalar kimsenin görmediği arızalardır ve onları ayıklamanızı sağlayan şey gözlemlenebilirliktir. İzleme size bir şeylerin yanlış olduğunu söyler. Gözlemlenebilirlik nedenini bulmanıza yardım eder.

Büyük takımlar için bu ayrım belirleyicidir. Bir monoliti tek makinedeki günlükleri okuyarak anlayabilirdiniz. Modern bir platform yüzlerce hizmeti, birçok takımı, birden çok bölgeyi ve üçüncü taraf bağımlılıkları kapsar; tek bir kullanıcı isteği düzinelerce bileşene dokunabilir. Hiç kimse sistemin bütününü kafasında taşıyamaz. Ortak, yüksek kaliteli telemetri, herhangi bir mühendisin bir isteği sınırlar boyunca izlemesini, belirtileri hizmetler arasında hizalamasını ve kimsenin tamamen sahip olmadığı bir sistem hakkında akıl yürütmesini sağlayan bağ dokusu olur. Onsuz olaylar uzar, suçlama takımlar arasında uçuşur ve kök nedenler gizli kalır.

Kurumsal ve kamu sistemleri, uyum, denetlenebilirlik ve kamusal hesap verebilirlikle bahsi yükseltir. Düzenleyiciler kimin neye ne zaman eriştiğine dair kanıt isteyebilir. Güvenlik takımları izinsiz girişleri saptamak için telemetriye ihtiyaç duyar. Vatandaşa dönük hizmetler yayımlanmış performans taahhütlerini karşıladıklarını göstermek zorundadır. İyi gözlemlenebilirlik bunların hepsine aynı anda hizmet eder: tek başına bir mühendislik aracı, bir güvenlik kontrolü ve bir hesap verebilirlik mekanizmasıdır. Açık enstrümantasyonda standartlaşmak, tek bir satıcının tescilli ajanlarına bağımlı kalmaktan kaçınmanızı sağlar; bu, sistemlerin onlarca yıl dayanması ve satın alma döngülerinden sağ çıkması gerektiğinde büyük önem taşır.

*Ayrıca bakınız:* bölüm 9.1 (site güvenilirliği mühendisliği ve SLO'lar), bölüm 9.3 (olay yönetimi) ve bölüm 3.3 (dağıtık sistemler).

## Temel ilkeler

- **Bilinmeyen sorular için enstrümante edin.** Telemetriyi, öngördüklerinizin ötesinde yeni arızaları da araştırabileceğiniz biçimde tasarlayın.
- **Üç sütun, tek hikâye.** Metrikler, günlükler ve izler birbirini tamamlayan görünümlerdir; değerleri, silolara ayrılmadan ilişkilendirildiğinde katlanır.
- **Her şeyi yapılandırın.** Tutarlı alanlara sahip, yapılandırılmış, makinece ayrıştırılabilir telemetri, yalnızca insanın okuyabildiği serbest metinden iyidir.
- **Ortak tanımlayıcılarla ilişkilendirin.** Her yere yayılan iz ve istek kimlikleri, tek bir olayı hizmetler boyunca birbirine dikmenizi sağlar.
- **Nedenlere değil, belirtilere göre uyarın.** İnsanları kullanıcıya görünen sorunlar için çağırın; altta yatan nedeni panolar ve soruşturma ortaya çıkarsın.
- **Her çağrı eyleme dönüştürülebilir olmalı.** İnsan eylemi gerektirmeyen bir uyarı, güveni aşındıran ve yorgunluğa yol açan gürültüdür.
- **Yüksek kardinalite bir özelliktir.** Kullanıcıya, isteğe, bölgeye ve sürüme göre dilimleyebilmek, üretimde hata ayıklamayı mümkün kılan şeydir.
- **Enstrümantasyonunuzun sahibi olun.** Verinizi kontrol etmek ve arka uçları değiştirebilmek için açık, üreticiden bağımsız telemetride standartlaşın.

## Öneriler

### Üç sütun ve ötesi üzerine kurun

**Metrikler**, depolaması ucuz, panolar, eğilimler ve uyarı eşikleri için ideal sayısal zaman serileridir. **Günlükler**, ayrıntıca zengin ve adli soruşturma için vazgeçilmez, zaman damgalı ayrık olay kayıtlarıdır. **[İzler](https://en.wikipedia.org/wiki/Tracing_(software))**, tek bir isteği hizmetler arasında hareket ederken izler ve dağıtık çağrı grafiği boyunca gecikmeyi ve bağımlılıkları gösterir. Bunların ötesinde **olayları** (dağıtımlar gibi anlamlı durum değişiklikleri), **profilleri** (kodun CPU'yu ve belleği nerede harcadığı) ve gerçek istemci deneyiminin **[gerçek kullanıcı izlemesini](https://en.wikipedia.org/wiki/Real_user_monitoring)** düşünün. Hiçbir sütun tek başına yetmez. Amaç, bir soruşturma sırasında aralarında akıcı biçimde gezinmektir.

### OpenTelemetry ve yapılandırılmış günlüklemede standartlaşın

Metrikleri, günlükleri ve izleri üretmek ve toplamak için üreticiden bağımsız standart olarak [OpenTelemetry](https://en.wikipedia.org/wiki/OpenTelemetry)'yi benimseyin. Enstrümantasyonu analiz arka ucundan ayırır; böylece yüzlerce hizmeti yeniden enstrümante etmeden satıcı değiştirebilirsiniz. Bu özellik uzun ömürlü kurumsal ve kamu sistemleri için kritiktir. Günlükleri zaman damgası, ciddiyet, hizmet ve tanımlayıcılar için tutarlı alan adlarıyla yapılandırılmış kayıtlar (örneğin JSON) olarak yayın. Bir iz ya da ilişkilendirme kimliğini uçtan her alt akış çağrısına yayın ve her günlük satırına ve metrik örneğine (exemplar) ekleyin; böylece üç sütun otomatik olarak birbirine bağlanır.

### Uyarıları eyleme dönüştürülebilirlik ve düşük gürültü için tasarlayın

Uyarı felsefeniz, nöbetin sürdürülebilir olup olmadığını belirler. Esas olarak kullanıcıların hissettiği belirtilere göre, SLO ([hizmet düzeyi hedefi](https://en.wikipedia.org/wiki/Service-level_objective)) yanma hızları olarak ifade edilerek uyarın. Hata bütçenizi (o hedeften izin verilen sapma) onu ihlal edecek kadar hızlı yakıyorsanız çağrı yapın; hızlı algılama ile yanlış alarmları dengelemek için çok pencereli yanma hızı uyarıları kullanın. Çağrıyı acil insan eylemi gerektiren sorunlara saklayın ve geri kalan her şeyi biletlere ya da panolara yönlendirin. Eylem gerektirmeden tetiklenen uyarıları acımasızca budayın; çünkü uyarı yorgunluğu, kaçırılan gerçek olayların ve nöbet tükenmişliğinin başlıca nedenidir. Her uyarı bir işletim kılavuzuna bağlanmalıdır.

### Sağlığı panolar ve SLO izlemeyle modelleyin

Panoları, sahip olduğunuz her metriğin duvarı yerine net bir sağlık modeli etrafında kurun. İyi bir başlangıç çerçevesi "dört altın sinyal"dir: gecikme, trafik, hatalar ve doygunluk. SLO durumunu ve kalan hata bütçesini bir bakışta gösteren hizmet düzeyinde panolar ve genel sistem ile kullanıcı yolculuğu sağlığını modelleyen daha üst düzey panolar oluşturun. Onları bilinçle küratörlüğünden geçirin, çünkü her şeyi gösteren panolar hiçbir şey anlatmaz. Müdahale edenlerin sinyalden bağlama, bağlamdan eyleme hızla geçebilmesi için panoları uyarılara ve işletim kılavuzlarına yakın tutun.

### Yüksek kardinaliteyle üretimde hata ayıklamayı etkinleştirin

En zor üretim sorunları dar bir dilime isabet eder: bir müşteri, bir bölge, bir API sürümü, bir cihaz türü. Bunları araştırmak için **yüksek kardinaliteli** telemetriye, yani kullanıcı kimliği ya da istek kimliği gibi çok sayıda farklı değeri olan alanlara göre gruplayıp süzebilme yeteneğine ihtiyacınız vardır. Kayıt başına birçok boyut taşıyan geniş, zengin nitelikli olaylar, sonradan keyfi sorular sormanızı sağlar. Aykırı değerleri yalıtmak için yeterli kardinaliteyi ve örnekleme doğruluğunu koruyun ve bir metrikteki sıçramanın sizi doğrudan temsilci yavaş isteklere götürmesi için örnek (exemplar) bağlantılı izleri tercih edin.

### Maliyeti, saklamayı ve örneklemeyi yönetin

Telemetri hacmi sistemle birlikte büyür ve büyük bir gidere dönüşebilir. Saklama politikalarını veri sınıfına göre belirleyin: yüksek çözünürlüklü veriyi kısa, toplulaştırılmış veriyi daha uzun tutun. İzlere, hataları ve yavaş istekleri tutmaya yanlı akıllı örnekleme uygulayın; böylece her rutin başarı için ödeme yapmadan ilginç kuyruğu elinizde tutarsınız. Telemetri harcamanızı düzenli olarak gözden geçirin, çünkü yönetilmeyen gözlemlenebilirlik maliyetleri, gözlemledikleri altyapıyla yarışabilir.

## Ödünleşimler: artılar ve eksiler

| Karar | Artılar | Eksiler |
|---|---|---|
| Yüksek kardinaliteli olaylar | Güçlü hata ayıklama, her şeyi sorabilme | Daha yüksek depolama ve sorgu maliyeti |
| Agresif örnekleme | Daha düşük maliyet, daha az gürültü | Nadir olayları kaçırabilir |
| Belirti tabanlı uyarı | Daha az, eyleme dönüştürülebilir çağrı | İyi çalışmak için iyi SLO'lar gerekir |
| OpenTelemetry standardı | Üreticiden bağımsız, taşınabilir | Geçiş çabası, olgunlaşan araçlar |
| Uzun günlük saklama | Daha iyi adli analiz ve denetim | Depolama maliyeti, gizlilik riski |

Gözlemlenebilirlik kararları, doğruluk ile maliyet arasındaki bir gerilime iner. Her şeyi tam çözünürlükle yakalamak size kusursuz bir geriye dönük bakış verir, ama ölçekte yasaklayıcı derecede pahalıdır. Agresif keserseniz para biriktirirsiniz, ama bir kesintiyi açıklayacak tek kaydı atmış olabilirsiniz. Örnekleme ve saklama katmanları, olgun takımların bu çizgide yürüme biçimidir: hataları ve aykırı değerleri tutarken rutin veriyi seyreltirler. Uyarı ödünleşimi ise duyarlılık ile gürültü arasındadır: çok fazla uyarı yorgunluğa ve kaçırılan olaylara yol açar, çok az uyarı sorunların çürümesine izin verir. Belirti tabanlı, SLO güdümlü uyarı bunun büyük kısmını çözer, ama yalnızca anlamlı SLO'larınız varsa.

## Takımınızla tartışılacak sorular

1. **Eski hizmetleri OpenTelemetry'ye taşıma planınız nedir ve geçiş sırasında iki enstrümantasyon yığınına para ödemekten nasıl kaçınırsınız?** Üreticiden bağımsız enstrümantasyon, yüzlerce hizmeti yeniden enstrümante etmeden arka uç değiştirmenizi sağlayan özelliktir ve herhangi bir tek satıcı sözleşmesinden uzun yaşayan kurumsal ve kamu sistemleri için en önemlisidir. İyi niyetlerin takıldığı yer geçiştir: yarı enstrümante edilmiş yapılar, bir istek yeni bir hizmetten eskisine geçtiği tam yerde boşluklar bırakır ve uçtan uca izi kırar. Tartışmaya bir envanter getirin: hangi hizmetler tescilli ajan verisi yayıyor, hangileri OpenTelemetry yayıyor ve iz bağlamı sınırda nerede düşüyor. Organizasyon şemalarını değil, gerçek istek yollarını izleyen bir sıralamaya karar verin ve iki toplayıcıyı birlikte çalıştırdığınız pencere için bütçe ayırın. Yanıt, telemetrinizin gerçekten sahibi olup olmadığınızı ya da tek bir satıcının ajanlarına kilitli kalıp kalmadığınızı belirler.

2. **Her uyarıyı eyleme dönüştürülebilirlik açısından en son ne zaman denetlediniz ve geçen ay kaç çağrı hiçbir insan eylemi gerektirmedi?** Uyarı yorgunluğu, kaçırılan gerçek olayların ve nöbet tükenmişliğinin başlıca nedenidir; bu yüzden eylem gerektirmeyen bir çağrı zararsız gürültü değildir, bağlı olduğunuz müdahaleyi aktif olarak aşındırır. Kanıtları getirin: geçen ayın çağrılarını çekin, her birini eyleme geçilmiş ya da görmezden gelinmiş diye işaretleyin ve kaçının bir işletim kılavuzuna eşlendiğini sayın. Çok sayıda hizmete yayılan büyük bir takımda, bir takımın gürültülü uyarıları ortak nöbeti herkes için duyarsızlaştırır. Her çağrının bir işletim kılavuzuna bağlandığı ve bir SLO yanma hızına bağlı olduğu bir standart koyun, geri kalanını acımasızca silin. Bu denetimin sonucu çağrı hacminizi doğrudan düşürmeli ve hangi hizmetlerin uyarılarının arkasında anlamlı bir SLO bulunmadığını söylemelidir.

3. **İz örnekleme stratejiniz nedir ve hataları ve yavaş kuyruğu koruduğundan ne kadar eminsiniz?** Telemetri hacmi sistemle birlikte büyür ve yönetilmeyen gözlemlenebilirlik maliyeti gözlemlediği altyapıyla yarışabilir; bu yüzden örnekleme yapacaksınız ve soru akıllıca örnekleyip örneklemediğinizdir. Kardinaliteyi sıyırmak ya da körü körüne örneklemek, tek bir müşteriye, bir bölgeye ya da bir API sürümüne isabet eden dar sorunları ayıklamak için gereken kayıtları tam olarak ortadan kaldırır. Mevcut saklama katmanlarınızı ve örnekleme kurallarınızı getirin: hataları ve yavaş istekleri tutmaya yanlı mısınız, bir metrik sıçramasının sizi temsilci bir yavaş isteğe götürmesi için örnek bağlantılı izler kullanıyor musunuz? Denetlenen ve gizlilikle bağlı sistemlerde, hata ayıklamak için kişisel veri istiflemeyesiniz diye saklamayı veri en azlaştırma kurallarıyla uzlaştırın. Yanıt, telemetri bütçenizi nereye harcadığınızı ve bir sonraki zor kesintinizin açıklanabilir mi yoksa bir bilmece mi olacağını belirler.

4. **SLO'larınızdan hangileri gerçek kullanıcı yolculuğu taahhütleri ve hangileri sahip takımın dışında kimsenin inanmadığı vekil metrikler?** Belirti tabanlı uyarı yalnızca belirtiler kullanıcıların gerçekten hissettiği şeylerle eşleştiğinde işe yarar; bu yüzden bir CPU eşiğine ya da uydurma bir erişilebilirlik hedefine bağlı uyarı, önemli olmayabilecek sorunlar için insanları çağırırken önemli olanlar karşısında sessiz kalır. Büyük bir kurumda SLO'lar, bağımsız takımların her olay sırasında ciddiyeti yeniden tartışmadan ortak bir nöbet rotasyonu paylaşmasını sağlayan sözleşmedir de. Mevcut SLO kataloğunu, her hedefin korumaya çalıştığı kullanıcı yolculuğunu ve son çeyreğin ihlallerini, müşterilerin gerçekten şikâyet edip etmediğiyle birlikte getirin. Kurumsal ve kamu ortamlarında en görünür SLO'ları hizmetin sorumlu tutulduğu yayımlanmış performans taahhütlerine bağlayın; böylece bir mühendisi çağıran aynı yanma hızı sinyali, bir düzenleyiciye ya da gözetim kurumuna gösterdiğiniz kanıt da olur. Tartışma, vekil metrikleri emekliye ayırmalı ve size mühendis olmayan birinin kullanıcılara verilmiş sözler olarak tanıyacağı kısa bir hedef listesi bırakmalıdır.

5. **Telemetri veri yönetişiminin sahibi kim ve kişisel verinin gözlemlenebilirlik arka ucunuza düşmeden önce gizlendiğini kanıtlayabilir misiniz?** Yüksek kardinaliteli olaylar ve uzun günlük saklama, hata ayıklamayı mümkün kılan özelliklerin tam kendisidir ve bir gözlemlenebilirlik deposunu kullanıcılarınızın kişisel verisinin yönetilmeyen bir kopyasına çeviren özelliklerin de tam kendisidir. Karşıt çekim gerçektir: mühendisler daha zengin nitelikler ve daha uzun saklama ister, gizlilik ve hukuk ise veri en azlaştırma ve kısa ömürler. Hangi alanların kişisel ya da hassas veri taşıdığını, gizlemenin ya da jetonlaştırmanın işlem hattında nerede olduğunu ve veri sınıfı başına saklama katmanlarınızı gösteren bir veri akışı haritası getirin. Düzenlenen ve kamusal sistemlerde hesap verecek sahibi adlandırın, saklamayı hukuki dayanağa ve uyduğunuz veri en azlaştırma kurallarına eşleyin ve telemetriye erişimin kendisinin de kaydedildiğini ve kontrol edildiğini bir denetçiye gösterebilecek durumda olun. Yanıt, gözlemlenebilirlik platformunuzun bir varlık mı yoksa keşfedilmeyi bekleyen kalıcı bir ihlal mi olduğunu belirler.

6. **Bir olay birkaç takımın hizmetini aştığında, telemetriniz tek bir müdahale edenin isteği uçtan uca izlemesine izin veriyor mu, yoksa iz her sahiplik sınırında kopuyor mu?** İlişkilendirilmiş, kimlik yayan telemetrinin tüm vaadi, tek bir mühendisin kimsenin tamamen sahip olmadığı bir sistem hakkında akıl yürütebilmesidir; bu vaat tam da iz bağlamının düştüğü ya da iki takımın uyumsuz tanımlayıcılar ve araçlar kullandığı sınırda çöker. Gözlemlenebilirlik araçlarını seçerken takım başına özerklik çekimini, bir kesinti sırasında her devrin çıkmaz sokak olduğu parçalanmış bir yapının ortak maliyetine karşı tartın. Yakın zamandaki bir takımlar arası olay zaman çizelgesini getirin ve müdahale edenin ipi nerede kaybettiğini işaretleyin; ayrıca hangi hizmetlerin ortak bir ilişkilendirme kimliği yaydığının ve hangilerinin yaymadığının envanterini çıkarın. Birçok satıcıdan ve uzun ömürlü sistemden derlenmiş büyük bir kurum ya da kamu platformu için, ne kadarını merkezi olarak dayatacağınıza (ortak bir iz bağlamı standardı ve ortak bir kimlik şeması) ve ne kadarını takımlara bırakacağınıza karar verin; çünkü onlarca yıl boyunca yeniden satın aldığınız bileşenlerin yine de aynı istek üzerinde birlikte çalışması gerekir. Yanıt, bir sonraki çok takımlı olayınızın koordineli bir soruşturma mı yoksa bir parmak gösterme turu mu olacağını söyler.

## Sektör merceği

**Girişim.** Bir avuç hizmetiniz ve boş elinizin olmadığı bir durumda, ilk günden OpenTelemetry ile enstrümante edin ve uçtan uca tek bir istek kimliği taşıyan yapılandırılmış JSON günlükleri sevk edin. Bu küçük yatırım "uygulama yavaş" şikâyetini okuyabileceğiniz bir ize çevirir ve sizi sonradan yeniden enstrümante etmeden ücretsiz bir katmandan ücretli bir arka uca geçmekte özgür bırakır. Deneyimini gerçekten ölçebileceğiniz kullanıcılarınız olana kadar ayrıntılı panoları ve SLO düzeneğini atlayın.

**Küçük işletme.** Gözlemlenebilirlik uzmanınız yok ve bütçeniz kısıtlı; bu yüzden kendi yığınınızı kurmak yerine enstrümantasyonun, depolamanın ve panoların paket halinde geldiği yönetilen bir arka uca yaslanın. Burada satın alma ile inşa etme kararı hemen her zaman satın almadan yanadır; kıt dikkatiniz, bir telemetri işlem hattı işletmekten çok hizmetin kapalı olduğunu söyleyen iki üç altın sinyal uyarısına harcanmalıdır. Telemetri maliyeti izlediği altyapıyı sessizce geçmesin diye sert bir saklama sınırı koyun.

**Kurumsal.** İş, birçok takım boyunca yönetişimdir: ortak bir OpenTelemetry standardı, ortak bir ilişkilendirme kimliği şeması ve küratörlüğü yapılmış SLO panoları; böylece tek bir müdahale eden, bir isteği düzinelerce hizmet boyunca izleyebilir. Telemetriyi saklama katmanları ve örnekleme politikasıyla bir maliyet merkezi olarak yönetin, ortak bir nöbeti sürdürülebilir tutmak için uyarıyı SLO yanma hızlarında standartlaştırın ve bir takımın yorgunluğu herkesi duyarsızlaştırmasın diye gürültülü uyarıları merkezi olarak budayın. Enstrümantasyon katmanını, herhangi bir arka uç sözleşmesinden uzun yaşayan, üreticiden bağımsız bir altyapı olarak ele alın.

**Kamu.** Satın alma kuralları, şeffaflık ve kamusal hesap verebilirlik tasarımı şekillendirir. Onlarca yıl çalışması beklenen bir sistemin, farklı satıcılar tarafından yeniden satın alınmaya, tescilli ajanlara rehin kalmadan dayanabilmesi için açık enstrümantasyonda standartlaşın ve bu taşınabilirliği sözleşmede şart koşun. Kimin hangi kayda ne zaman eriştiğini göstermek için yapılandırılmış denetim günlükleri kullanın, kişisel veriyi telemetri deposuna ulaşmadan önce gizleyin ya da jetonlaştırın ve saklamayı veri en azlaştırma hukukuyla uzlaştırın. Vatandaşa dönük hizmetler için SLO panolarını yayımlayın; böylece mühendislerinizin izlediği sinyaller, sorumlu tutulduğunuz taahhütlerin görünür kanıtı olur.

## Örnekler

**Girişim.** Dört kişilik bir girişim bir mobil arka uç sevk ediyor ve yeniden üretemediği belirsiz "uygulama yavaş" şikâyetleri almaya devam ediyor. Takım birkaç hizmetine OpenTelemetry ekliyor ve uygulamadan her sıçramaya taşınan bir istek kimliğiyle yapılandırılmış JSON günlüklere geçiyor. Bir sonraki yavaşlık raporu dakikalar içinde çözülüyor: tek bir iz, belirli bir sorguda siparişler tablosunda eksik bir veritabanı dizinini gösteriyor. Açık enstrümantasyonu erken seçtikleri için, sonradan hiçbir şeyi yeniden enstrümante etmeden ücretsiz katmandan ücretli bir arka uca geçiyorlar.

**Kurumsal.** Büyük bir e-ticaret platformu her hizmetini OpenTelemetry ile enstrümante ediyor ve müşterinin tarayıcısından ödemeye, tahsilata, stoğa ve kargoya bir iz kimliği yayıyor. Dönüşüm düştüğünde nöbetçi bir mühendis bir SLO yanma hızı uyarısından başlıyor, ödeme panosunun altın sinyallerini açıyor, bir bölgede yükselmiş gecikmeyi görüyor ve bir örnek izi izleyerek tek bir hizmetteki yavaş bir veritabanı çağrısına varıyor. Yüksek kardinaliteli nitelikler sorunun tek bir ürün kategorisiyle sınırlı olduğunu gösteriyor; bu da saatler yerine dakikalar içinde hedefli bir düzeltmeye yol açıyor.

**Kamu.** Ulusal bir sağlık hizmeti, sıkı denetim ve gizlilik kuralları altında bir hasta kayıtları platformu işletiyor. Yapılandırılmış günlükler kimin hangi kayda ne zaman eriştiğini yakalıyor ve hem güvenlik izlemeyi hem uyum raporlamayı besliyor; kişisel olarak tanımlanabilir alanlar ise telemetride gizleniyor ya da jetonlaştırılıyor. Herkese açık SLO panoları, vatandaşa dönük randevu alma için erişilebilirliği ve gecikmeyi gösteriyor. Açık enstrümantasyonda standartlaşarak kurum, onlarca yıl çalışması ve ömrü boyunca farklı satıcılarca yeniden satın alınması beklenen bir sistemde tescilli bağımlılıktan kaçınıyor.

## İş gerekçesi: motivasyonlar, YG ve TSM

Gözlemlenebilirliğin başlıca getirisi, olayları algılama ve çözme süresindeki dramatik düşüştür. Kesintinin maliyetli olduğu bir hizmet için ortalama çözüm süresini saatlerden dakikalara indirmek, tek bir büyük olayda araçların masrafını birçok kez çıkarır. Gözlemlenebilirlik, aksi halde tahmin etmeye, hataları yeniden üretmeye ve hangi takımın kusurlu olduğunu tartışmaya harcayacağınız mühendislik zamanından da tasarruf sağlar ve takımların güvenle sevk etmesini sağlayan geri bildirim döngüsünü kısaltır. Güvenlik ve uyum değeri de gerçektir: aynı telemetri izinsiz giriş tespitini ve denetim kanıtını destekler.

Toplam sahip olma maliyeti; enstrümantasyon çabasını, telemetri depolama ve sorgu maliyetlerini ve gürültüden sinyali ayıklama disiplinini içerir. Bu maliyetler görünür ve yinelenendir; bu da yönetimi yetersiz yatırıma özendirir. Benimsememenin maliyeti daha büyüktür ama görülmesi daha zordur: uzayan kesintiler, teşhis edilmemiş performans sorunları, geç ya da hiç bulunamayan güvenlik olayları ve hiçbir şey yapamadıkları uyarılar yüzünden tükenen mühendisler. Gerekçeyi somut olay verisiyle kurun. Yakın zamandaki kesintilerin çözüm süresini ve iş etkisini gösterin ve daha iyi telemetrinin sağlayacağı azalmayı öngörün. Gözlemlenebilirliği saf bir maliyet merkezi olarak değil, teslimatı da hızlandıran bir sigorta olarak çerçevelemek argümanı kazanır.

## Anti-kalıplar ve tuzaklar

- **Her şey için uyarmak.** Her anormallik için çağrı yapmak, müdahale edenleri uyarıları görmezden gelmeye alıştırır; gerçek olaylar da böylece gözden kaçar.
- **Neden tabanlı çağrı.** Kullanıcı belirtileri yerine iç nedenler üzerinden uyarmak, nöbeti gürültüyle boğar ve yeni arızaları kaçırır.
- **Yapılandırılmamış günlükler.** Sorgulanamayan ya da ilişkilendirilemeyen serbest metin günlükleri, olaylar sırasında yavaş, elle grep çekmeyi zorunlu kılar.
- **Üç silolu sütun.** Ortak kimlikler olmadan bağlantısız araçlardaki metrikler, günlükler ve izler, bir olayı uçtan uca izlemeyi engeller.
- **Pano çoğalması.** Küratörlüğü yapılmamış yüzlerce pano, sistemin sağlıklı olup olmadığını hangisinin gösterdiğini kimsenin bilmemesi demektir.
- **Kardinalite çöküşü.** Maliyeti düşürmek için yüksek kardinaliteli alanları sıyırmak, dar sorunları ayıklamak için gereken veriyi tam olarak ortadan kaldırır.
- **Satıcıya bağımlılık.** Her yerde tescilli ajanlar, arka uç değiştirmeyi yasaklayıcı derecede pahalı yapar ve verinizi rehin tutar.

## Olgunluk modeli

**Düzey 1, Başlangıç.** Gözlemlenebilirlik plansız ve reaktiftir. Temel çalışma süresi denetimleri ve yapılandırılmamış günlükler tek tek makinelerde yaşar, hata ayıklama sunuculara girip grep çekmek demektir ve ortak telemetri yoktur. Uyarılar gürültülü, neden tabanlı ve çoğunlukla görmezden gelinir; bu yüzden gerçek olaylar sinyallerle değil kullanıcı şikâyetleriyle ortaya çıkar.

**Düzey 2, Geliştirme.** Temel uygulamalar belirir ama takıma göre değişir. Bazı hizmetler metrik ve günlükleri merkezi bir yere iter, birkaç pano ve eşik uyarısı vardır; ama günlükler yalnızca yarı yapılandırılmıştır ve izler yok ya da kısmidir. Hizmetler arası ilişkilendirme elle yapılır ve bir mühendisin bir isteği uçtan uca izleyip izleyemeyeceği, hangi takımların işin içinde olduğuna bağlıdır.

**Düzey 3, Standartlaştırma.** Enstrümantasyon belgelenmiş ve kuruluş genelinde uygulanır. Yayılan bir iz ya da ilişkilendirme kimliğiyle hizmetler boyunca OpenTelemetry, tutarlı alan adlarıyla yapılandırılmış günlükleme, dağıtık izleme, küratörlüğü yapılmış altın sinyal panoları ve SLO tabanlı belirti uyarısı, her takımın izlediği standarttır. Her çağrı bir işletim kılavuzuna bağlanır ve bir SLO'ya bağlıdır; nöbet sürdürülebilirdir, tükenmişlik kaynağı değildir.

**Düzey 4, Yönetme.** Gözlemlenebilirlik yapısının kendisi temel çizgilere karşı ölçülür ve kontrol edilir. Hizmetler genelinde enstrümantasyon kapsamını ve iz bağlamı yayılma oranını, eyleme geçilen ile görmezden gelinen çağrıların payını, ortalama algılama ve çözme süresini, SLO tutturmayı ve hata bütçesi yanmasını ve hizmet başına telemetri maliyetini bir bütçeye karşı izlersiniz. Boşluklar ve uyarı gürültüsü, açık hedeflere doğru veriyle aşağı çekilir, hata ve yavaş kuyruk kayıtlarının hayatta kalması için örnekleme doğruluğu doğrulanır ve kapsam ile saklamaya ilişkin git ya da gitme kararları görüşe değil kanıta dayanır.

**Düzey 5, Orkestrasyon.** Gözlemlenebilirlik kurum genelinde sürekli iyileştirilir ve bütünleşmiştir. Yüksek kardinaliteli, olay açısından zengin telemetri herhangi bir dilimin plansız soruşturmasını sağlar, uyarı en az gürültüyle SLO yanma hızı güdümlüdür ve örnekleme ile saklama değişen maliyet ve riske uyum sağlar. Telemetri; kapasite planlamasını, güvenlik tespitini ve ürün kararlarını rutin olarak besler ve platform, sistem, tehdit tablosu ve düzenleyici yükümlülükler değiştikçe kendi sinyallerini, bütçelerini ve kapsamını yeniden ayarlar.

## Tartışma fikirleri

- En kritik hizmetleriniz için telemetri doğruluğu ile maliyet arasındaki doğru denge nerede?
- Neyin çağrıyı, neyin bileti, neyin yalnızca bir pano girdisini hak ettiğine nasıl karar veriyorsunuz?
- Kod tabanı ya da sürüm döngüsü paylaşmayan takımlar arasında ilişkilendirme kimliklerini yayma stratejiniz nedir?
- Gizlilik ve veri en azlaştırma gereksinimlerini karşılarken yüksek kardinaliteli hata ayıklama gücünü nasıl korursunuz?
- Gözlemlenebilirlik araçları merkezi olarak mı dayatılmalı yoksa takım başına mı seçilmeli ve her iki durumun sonuçları nedir?
- Telemetrinizin eksiksiz ve kurcalamaya karşı belirgin olduğunu denetçilere nasıl gösterirsiniz?

## Önemli çıkarımlar

- İzleme bilinen sorunları algılar; gözlemlenebilirlik bilinmeyenleri yeni kod sevk etmeden araştırmanıza izin verir.
- Metrikler, günlükler ve izler, silolara ayrılmadan ortak tanımlayıcılarla ilişkilendirildiğinde en değerlidir.
- Uzun sistem ömürleri boyunca üreticiden bağımsız ve taşınabilir kalmak için OpenTelemetry ve yapılandırılmış günlüklemede standartlaşın.
- SLO yanma hızları üzerinden kullanıcıya görünen belirtilere göre uyarın, her çağrıyı eyleme dönüştürülebilir yapın ve gürültüyü amansızca budayın.
- Panoları her metriği göstermek yerine altın sinyaller gibi net bir sağlık modeli etrafında küratörlüğünden geçirin.
- Yüksek kardinaliteli, olay açısından zengin telemetri, dar üretim sorunlarında hata ayıklamayı mümkün kılan şeydir.

## Kaynaklar ve ileri okuma

- Charity Majors, Liz Fong-Jones, George Miranda, *Observability Engineering: Achieving Production Excellence*
- Cindy Sridharan, *Distributed Systems Observability*
- Betsy Beyer et al., *Site Reliability Engineering* (chapters on monitoring and alerting)
- Brendan Gregg, *Systems Performance: Enterprise and the Cloud*
- OpenTelemetry project, specification and documentation (Cloud Native Computing Foundation)
- Google, *The Four Golden Signals* (Site Reliability Engineering, monitoring chapter)
