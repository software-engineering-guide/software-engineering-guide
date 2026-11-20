# 5.7 Mobil uygulama geliştirme

## Genel bakış ve motivasyon

[Mobil uygulama geliştirme](https://en.wikipedia.org/wiki/Mobile_app_development), telefonlar ve tabletler için yazılım inşa etme disiplinidir. Birçok insan için telefon artık sahip olduğu birincil ya da tek bilgisayardır. Bu da mobil uygulamayı hizmetinizin ön kapısı, çoğu zaman da kullanıcıların tüm kurumunuzu yargıladığı yüzey yapar.

Mobil, web ya da masaüstünün küçük bir sürümü değil, ayrı bir mühendislik ortamıdır. Cihaz bir cepte, pille ve gelip giden bağlantılarla çalışır. Ekranlar küçüktür. Uygulamanızın neler yapabileceğini işletim sistemi denetler. İki baskın platform vardır (Apple'ın [iOS](https://en.wikipedia.org/wiki/IOS)'u ve Google'ın [Android](https://en.wikipedia.org/wiki/Android_%28operating_system%29)'i); her birinin kendi dilleri, tasarım kuralları ve mağazası vardır. İstediğiniz zaman bir güncelleme yayımlayamazsınız, çünkü önce bir mağaza onu inceler ve kullanıcılar ne zaman kuracaklarına kendileri karar verir. Bu bölüm ön yüz mühendisliği (bölüm 5.6), kullanıcı deneyimi temelleri (bölüm 5.1) ve erişilebilirlik (bölüm 5.3) üzerine kuruludur ve uygulama güvenliğine (bölüm 4.2) ile CI/CD ve teslimata (bölüm 8.1) yaslanır.

Kurumsal ve kamu açısından ilgisi yüksektir. Kurumlar müşteri uygulamaları ve kendi iş gücü için iç uygulamalar yayımlar; bunlar çoğu zaman [mobil cihaz yönetimiyle](https://en.wikipedia.org/wiki/Mobile_device_management) (MDM: şirket cihazlarını yapılandıran ve güvenceye alan merkezî yazılım) yönetilir. Hükümetler yardım, sağlık, kimlik ve ödemeler için yurttaşa dönük uygulamalar kurar ve erişilebilirlik yasaları uyarınca eski cihazlardaki ve yavaş bağlantılardaki insanlar dahil herkese hizmet etmek zorundadır. Her iki ortamda da mobil ciddi, uzun ömürlü bir taahhüttür; bu yüzden ona diğer her üretim sistemine verdiğiniz titizliği verin.

## Temel ilkeler

- Cihaz için tasarlayın: küçük ekran, pil ve gelip giden bir ağ.
- Aralıklı bağlantıyı varsayın; önce çevrimdışı çalışın ve yapabildiğinizde senkronlayın.
- Her platformun tasarım ve etkileşim geleneklerine saygı gösterin.
- Sürüm zamanlamasını siz denetlemezsiniz; mağaza ve kullanıcı denetler.
- Parçalanma normaldir; gerçek bir cihaz ve işletim sistemi sürümü aralığını destekleyin.
- Cihazlar kaybolur ve çalınır; veriyi cihazda güvenle saklayın.
- Erişilebilirlik bir gerekliliktir, bitiş cilası değil.
- Yapı yaklaşımını yalnızca yayın gününe değil, uygulamanın tüm ömrüne göre seçin.

## Öneriler

### Yapı yaklaşımını bilinçli seçin

Üç geniş yaklaşım vardır ve her biri farklı ihtiyaçlara uyar.

[Yerel geliştirme](https://en.wikipedia.org/wiki/Mobile_app_development), her platform için kendi araçlarıyla ayrı ayrı yazmak demektir: iOS için Swift, Android için Kotlin. İki kod tabanı inşa edip sürdürmenin bedeline karşılık en iyi performansı, cihaz özelliklerine en tam erişimi ve platforma en sadık hissi elde edersiniz.

[Çapraz platform çerçeveleri](https://en.wikipedia.org/wiki/Cross-platform_software) tek bir kod tabanının iki platformu da hedeflemesine izin verir. [React Native](https://en.wikipedia.org/wiki/React_Native) JavaScript kullanır ve gerçek yerel bileşenleri işler. [Flutter](https://en.wikipedia.org/wiki/Flutter_%28software%29) Dart dilini kullanır ve kendi bileşenlerini çizer. Bunlar yinelenen emeği azaltır ve teslimatı hızlandırabilir, ancak çerçevenin sağlığına bir bağımlılık ekler ve en yeni platform özelliklerinin gerisinde kalabilir.

[Aşamalı web uygulaması](https://en.wikipedia.org/wiki/Progressive_web_app) (PWA: kurulabilen ve çevrimdışı çalışabilen bir web sitesi) mağaza gerektirmez ve anında güncellenir, ancak bazı cihaz özelliklerine erişimi sınırlıdır ve ana ekranda daha zayıf bir varlığı vardır.

Gereken cihaz özelliklerine, performans profiline, bakım ufkuna, işe alabileceğiniz becerilere ve ihtiyaç duyduğunuz erişime göre seçin. Yüksek performanslı bir tüketici uygulaması yerel geliştirmeyi haklı çıkarabilir. Küçük bir takımın içerik ve form uygulaması çapraz platforma ya da bir PWA'ya iyi uyabilir.

### Platform tasarım yönergelerini izleyin

Her platformun yayımlanmış, ayrıntılı gelenekleri vardır. Apple [Human Interface Guidelines](https://en.wikipedia.org/wiki/Human_interface_guidelines) sağlar, Google ise [Material Design](https://en.wikipedia.org/wiki/Material_Design) sağlar. Bunlar gezinmeyi, hareketleri, tipografiyi, boşluğu ve sistem davranışlarını kapsar. Onları izlemek uygulamanızı tanıdık hissettirir ve kullanıcıların öğrenmeye harcadığı emeği azaltır. Onlarla savaşmak uygulamayı yabancı ve beceriksiz hissettirir. Çapraz platform bir kod tabanı, bir platformun görünümünü ötekine dayatmak yerine, farklı oldukları yerlerde platform başına geleneklere yine de saygı göstermelidir.

### Mobil kısıtlar için tasarlayın

Önce çevrimdışı inşa edin: çekirdek görevler bağlantısız çalışsın, değişiklikler yerelde saklansın ve ağ döndüğünde senkronlansın. Aynı veri iki yerde değiştiğinde çakışmaları düşünerek ele alın. Pil ve veri konusunda tutumlu olun: ağ çağrılarını toplu yapın, sürekli konum ya da arka plan işinden kaçının, yükleri sıkıştırın ve kullanıcının veri tasarrufu ayarlarına saygı gösterin. Parçalanmaya, yani ekran boyutlarının, cihaz gücünün ve işletim sistemi sürümlerinin geniş yelpazesine plan yapın. Gerçek kullanım verisine dayanarak bir destek aralığı seçin ve yalnızca amiral gemisi modellerde değil, mütevazı donanımda test edin. Küçük ekranlar için net hiyerarşi, büyük dokunma hedefleri ve farklı boyutlara ve yönelimlere uyum sağlayan içerikle tasarlayın.

### Dağıtımı, sürümlemeyi ve güncellemeleri planlayın

Yayımlama, bir sürümü geciktirebilecek ya da reddedebilecek inceleme süreçleri ve politikaları olan [Apple App Store](https://en.wikipedia.org/wiki/App_Store_%28Apple%29) ve [Google Play](https://en.wikipedia.org/wiki/Google_Play) üzerinden geçer. İnceleme süresini takviminize ekleyin ve politikaları erken okuyun. Kullanıcılar ne zaman güncelleyeceklerine kendileri karar verdiği için sahada her zaman birçok sürüm aynı anda bulunur. Uygulamanızı eski istemcilerle geriye uyumlu tutun ve eski bir uygulama çalışmaya devam etsin diye API'lerinizi (bölüm 2.3) sürümleyin. Gerektiğinde güncellemeyi zorunlu kılmanın bir yolunu sağlayın, örneğin bir sürüm güvensiz ya da desteksiz olduğunda zorunlu güncelleme istemi, ve bunu idareli kullanın. Kurumlar iç uygulamaları herkese açık mağazalar yerine MDM ya da özel kanallar üzerinden de dağıtabilir.

### Anlık bildirimleri ve derin bağlantıları özenle kullanın

[Anlık bildirimler](https://en.wikipedia.org/wiki/Push_technology), uygulamanız kapalıyken kullanıcılara ulaşmanıza izin verir. Bunları gerçek değer için kullanın, kullanıcının rızasına ve platform izinlerine saygı gösterin ve gürültüden kaçının, çünkü insanlar haddini aşan uygulamaların bildirimlerini kapatır. [Derin bağlantılar](https://en.wikipedia.org/wiki/Deep_linking) kullanıcıyı bir bağlantıdan ya da bildirimden doğrudan belirli bir ekrana gönderir. Bir bağlantının uygulamada doğru yeri açması ve uygulama kurulu olmadığında zarifçe web'e düşmesi için bunları yapılandırın.

### Uygulamayı ve verisini güvenceye alın

Cihazı güvenilmez ve muhtemelen kayıp sayın. Hassas veriyi düz dosyalarda asla değil, platformun güvenli depolamasında ([iOS Keychain](https://en.wikipedia.org/wiki/Keychain_%28software%29) ya da Android Keystore) saklayın. Hassas eylemlerin kilidini açmak için, bir parola ile desteklenmiş [biyometrik kimlik doğrulama](https://en.wikipedia.org/wiki/Biometrics) (parmak izi ya da yüz) sunun. Yüksek değerli bağlantılar için [sertifika sabitlemeyi](https://en.wikipedia.org/wiki/Public_key_pinning) (sunucunun beklenen bir sertifika sunduğunu denetlemek) düşünün ve bu sertifikaları döndürmeyi planlayın. Cihazda sakladığınızı en aza indirin, sırları koruyun ve uygulama güvenliğindeki (bölüm 4.2) daha geniş rehberliği izleyin.

### Gerçek bir test ve teslimat hattı kurun

[Emülatörlerde](https://en.wikipedia.org/wiki/Emulator) ve simülatörlerde değil, gerçek cihazlarda test edin, çünkü donanım, sensörler ve performans farklıdır. Temsilî bir model ve işletim sistemi sürümü yelpazesini kapsamak için bir cihaz laboratuvarı ya da bulut cihaz çiftliği kullanın. Derlemeleri, testleri, imzalamayı ve mağazaya gönderimi, herkese açık sürümden önce test edenlere beta dağıtımı dahil, [sürekli bütünleştirme ve teslimat](https://en.wikipedia.org/wiki/CI/CD) (bölüm 8.1) ile otomatikleştirin. İmzalama anahtarlarını ve mağaza kimlik bilgilerini güvenle yönetmek bu hattın parçasıdır.

### Erişilebilirliği bir gereklilik yapın

Her platformun erişilebilirlik özelliklerini destekleyin: ekran okuyucular (iOS'ta [VoiceOver](https://en.wikipedia.org/wiki/VoiceOver), Android'de [TalkBack](https://en.wikipedia.org/wiki/Google_TalkBack)), dinamik metin boyutlandırma, yeterli renk karşıtlığı ve büyük dokunma hedefleri. Yardımcı teknolojinin tanımlayabilmesi için denetimleri etiketleyin. Yalnızca otomatik denetimlerle değil, gerçek yardımcı araçlarla test edin. Özellikle kamu için erişilebilirlik yasal bir zorunluluktur ve ayrıntılar erişilebilirlikte (bölüm 5.3) yaşar.

## Ödünleşimler: artılar ve eksiler

| Yaklaşım | Artılar | Eksiler |
|---|---|---|
| Yerel (Swift, Kotlin) | En iyi performans, tam cihaz erişimi, gerçek platform hissi | İki kod tabanı, daha yüksek maliyet, daha çok personel |
| React Native | Tek JavaScript kod tabanı, gerçek yerel bileşenler, hızlı yineleme | Çerçeve bağımlılığı, köprüleme karmaşıklığı, özellik gecikmesi |
| Flutter | Tek kod tabanı, tutarlı arayüz, güçlü performans | Dart becerileri daha az yaygın, daha büyük uygulama boyutu, kendi bileşen modeli |
| Aşamalı web uygulaması | Mağaza yok, anında güncelleme, tek web kod tabanı | Sınırlı cihaz özellikleri, daha zayıf varlık, platform sınırları |
| Zorunlu güncellemeler | Güvensiz eski sürümleri hızla kaldırır | Aşırı kullanılırsa kullanıcıları rahatsız eder; erişimi engelleyebilir |
| Sertifika sabitleme | Araya girmeye karşı güçlü koruma | Sertifikalar uygulama güncellemesi olmadan dönerse bozulur |

Yinelenen ödünleşim, erişim ve teslimat hızı ile derinlik ve sadakat arasındadır. Yerel geliştirme en zengin, en sadık deneyimi verir ancak inşa etmesi ve sürdürmesi en pahalıdır. Çapraz platform ve PWA yaklaşımları emekten tasarruf eder ve erişimi genişletir; bunun bedeli platform hissinden ya da cihaz erişiminden biraz taviz vermektir. Form ve içerik yayımlayan küçük bir takım için kod tabanını paylaşmak çoğu zaman akıllıcadır. Zorlu bir tüketici uygulaması için yerel geliştirmenin derinliği fiyatına değebilir. Yalnızca yayına değil, uygulamanın tüm ömrüne bakarak karar verin.

## Takımınızla tartışılacak sorular

1. **Sahadaki eski istemcileri ne kadar süre destekliyoruz ve API'miz onları çalışır tutmak için sürümlenmiş mi?** Kullanıcılar ne zaman güncelleyeceklerine kendileri karar verdiği için uygulamanın birçok sürümü her zaman aynı anda kuruludur ve herkesin güncel olduğunu varsayan bir arka uç değişikliği eski istemcilerin uzun kuyruğunu bozar. Geriye uyumluluk pencerenize karar verin, eski bir uygulama çalışmaya devam etsin diye API'lerinizi sürümleyin ve gerçekten güvensiz olan sürümler için nadiren kullanılan bir zorunlu güncelleme yolu tutun. Bu, eski cihazlardaki insanların sizin takviminize göre yükseltemediği ya da yükseltmediği hem kamu yurttaş uygulamaları hem kurumsal iş gücü uygulamaları için önemlidir. Güncel sürüm dağılımı verilerinizi getirin ve gerçek kullanımdaki en eski istemci için neyin bozulduğunu sorun. O dağılımı bilmiyorsanız, bir sonraki uyumsuz değişikliğinizi yayımlamadan önce ölçümleyin.

2. **Anlık bildirim göndermenin eşiği nedir ve bir kullanıcıyı kesmeye değip değmediğine kim karar verir?** Anlık bildirimler uygulama kapalıyken insanlara ulaşır; bu onları güçlü ve kötüye kullanılmaya açık yapar ve kullanıcılar haddini aşan ürünlerin bildirimlerini kapatır (ya da uygulamayı siler). Neyin gerçek değer sayıldığı, kullanıcıların sıklığı ve kanalı nasıl denetlediği ve izin için ısrar etmek yerine platform rızasına nasıl saygı gösterdiğiniz konusunda anlaşın. Ortak bir eşik olmadan, ulaşması gereken bir ölçütü olan her takım bir anlık bildirime uzanır ve tüm kanal gürültüye dönüşür. Son bir ayda gönderdiğiniz bildirimleri getirin ve hangileri için kullanıcının size teşekkür edeceğini sorun. Çoğu tanıtım amaçlıysa, çıkış oranı bunu sizin yerinize yapmadan önce politikayı sıkılaştırın.

3. **Mobil teslimat hattımız gerçek mi, yani imzalamayı, bir cihaz çiftliğini ve beta dağıtımını kapsıyor mu, yoksa sürüm stresli bir elle telaş mı?** Mobil, web'de olmayan tehlikeler ekler: mağaza incelemesi bir sürümü geciktirebilir ya da reddedebilir, imzalama anahtarları ve mağaza kimlik bilgileri güvenle ele alınmalıdır ve donanım ile sensörler emülatörlerin gerçek sorunları gizleyeceği kadar farklıdır. Derlemeleri, testleri, imzalamayı ve mağaza gönderimini beta dağıtımı ve kullanıcılarınızın gerçekte taşıdığı modelleri kapsayan bir bulut cihaz çiftliğiyle CI/CD üzerinden otomatikleştirmek, sürümleri kahramanlıktan rutine çeviren şeydir. Hattın ve imzalama anahtarlarının sahibini ve mağaza inceleme süresinin her sürüm planına nasıl eklendiğini kararlaştırın. Son sürümünüzün hikâyesini getirin ve elle yapılan adımları sayın. Her biri, son tarih baskısı altında stresli bir sürümün ters gidebileceği bir yerdir.

4. **Yerel, çapraz platform ya da aşamalı web uygulamasını bu ürünün tüm ömrü için mi seçtik, yoksa yalnızca yayın günü için mi?** Yapı yaklaşımı, yıllarca bir mobil uygulamanın maliyeti ve yeteneği üzerindeki en büyük kaldıraçtır ve hızlı yayımlamak için yapılan bir seçim sizi tuzağa düşürebilir: yerel geliştirme, iki kod tabanı ve iki beceri kümesi karşılığında en zengin cihaz erişimini ve platform hissini satın alır; çapraz platform ve PWA ise kod paylaşır ancak bir çerçeve bağımlılığı ekler ya da bazı cihaz özelliklerine erişimi kaybeder. Büyük bir takım için bu karar işe alımı, bakım bütçesini ve her yıllık işletim sistemi sürümünü ne kadar hızlı benimseyebileceğinizi belirler; bu yüzden ilk prototipi yazan kişinin belirlediği bir varsayılan yerine açık bir sahibi hak eder. Gereken cihaz özelliklerini, performans profilini, bakım ufkunu ve gerçekten işe alabileceğiniz becerileri getirin ve her seçenekte hangi platform özelliklerinden vazgeçeceğiniz konusunda dürüst olun. Kurumsal ve kamu ortamlarında, uygulamanın personel değişimine ve on yıllık platform değişimine dayanması gereken uzun ömürlü bir taahhüt olup olmadığını tartın ve ileride bir takım kod tabanının neden böyle göründüğünü tahmin etmek zorunda kalmasın diye kararı ve gerekçesini kaydedin.

5. **Gerçek kullanıcılarımızın hangi cihaz ve işletim sistemi sürümü destek aralığına ihtiyacı var ve masalarımızdaki telefonlarda değil, onların gerçekte taşıdığı donanımda mı test ediyoruz?** Parçalanma mobilin normal durumudur: kullanıcılar geniş bir ekran boyutu, cihaz gücü ve işletim sistemi sürümü yelpazesine yayılır ve takımın amiral gemilerinde ayarlanmış bir uygulama, kitlenizin büyük kısmının sahip olduğu mütevazı donanımda ağır ya da bozuk yayına girer. Bir destek aralığı belirlemek erişim ile emek arasında bir ödünleşimdir, çünkü desteklemeyi vaat ettiğiniz her eski model ve işletim sistemi sürümü test matrisini ve bakım yükünü genişletir; bu yüzden aralık varsayımdan değil gerçek kullanım verisinden gelmelidir. Cihaz ve işletim sistemi sürümü dağılımınızı, bir bulut cihaz çiftliğinin ya da laboratuvarın şu an kapsadığı modelleri ve yalnızca simülatörlerde değil, düşük uç donanımda ölçtüğünüz performansı getirin. Kamu yurttaş uygulamaları için bu neredeyse pazarlıksızdır, çünkü erişilebilirlik yükümlülükleri uyarınca eski cihazlardaki ve yavaş bağlantılardaki insanlar dahil herkese hizmet etmelisiniz; kurumsal filolar için ise genel bir örnek yerine personelin taşıdığı sağlam el cihazlarını tam olarak test etmelisiniz.

6. **Cihazda hangi hassas veri yaşıyor ve her biri kaybolmuş, çalınmış ya da başkasının elindeki bir telefona karşı korunuyor mu?** Mobil bir cihaz cepte gezer ve kaybolur ya da çalınır; bu yüzden düz bir dosyada saklanan her veri ya da sır, kaybolmuş bir telefon kadar ifşaya yakındır ve etki alanı her kullanıcıyla büyür. Değerlendirmeler birbirine zıt çeker: veriyi cihazda önbelleklemek çevrimdışı öncelikli çalışmayı mümkün kılan ve uygulamayı hızlı tutan şeydir, ancak her önbelleğe alınmış öğe bir yükümlülüktür; platformun güvenli depolamasında (iOS Keychain ya da Android Keystore) durmalı, en aza indirilmeli ve ideal olarak biyometri ya da parola ardında kapılanmalıdır. Uygulamanın yerelde tam olarak neyi kalıcılaştırdığının, her öğenin nerede saklandığının, onu neyin açtığının ve yüksek değerli bağlantıların uygulanabilir bir döndürme planıyla sertifika sabitleme kullanıp kullanmadığının bir envanterini getirin. Kurumsal ortamlarda bunu mobil cihaz yönetimi politikasına ve uzaktan silmeye bağlayın; kamu ortamlarında cihazdaki kişisel veriyi, haklı çıkarılması, belgelenmesi ve denetimde savunulabilir olması gereken bir gizlilik ve yasal risk olarak ele alın.

## Sektör merceği

**Girişim.** Küçük bir takım ve az nakit ömrüyle, iki yerel kod tabanını ya da iki beceri kümesini nadiren karşılayabilirsiniz; bu yüzden tek kod tabanından her iki mağazaya ulaşan bir çapraz platform çerçevesi ya da hatta bir PWA genellikle kazanır. Önemli olan tek çekirdek görev için önce çevrimdışı yayımlayın, belirteçleri düz bir dosyada değil güvenli depolamada tutun ve bir reddin yayın tarihini bozmaması için her sürüme mağaza inceleme süresini ekleyin. Gerçek kullanım haklı çıkarana kadar zorunlu güncellemeleri, sertifika sabitlemeyi ve cihaz çiftliğini atlayın.

**Küçük işletme.** Özel bir mobil uzmanı olmadan ve dar bir bütçeyle, yapmak yerine satın almaya güçlü biçimde yönelin: kodsuz bir uygulama oluşturucu, satış noktası ya da rezervasyon satıcınızdan beyaz etiketli bir uygulama ya da mevcut web sitenizden çıkan iyi yapılmış bir PWA, çoğu zaman sürdüremeyeceğiniz özel bir uygulamayı geçer. Bir uygulama ısmarlarsanız, bir yüklenicinin varlığınızı rehin tutamaması için imzalama anahtarlarının ve mağaza hesaplarının sahibi kendiniz olun ve sözleşmede erişilebilirlik ve cihazda güvenli depolama konusunda ısrar edin. Kapsamı müşterilerin telefonda gerçekten yaptığı bir ya da iki görevle sınırlı tutun.

**Kurumsal.** Ölçekte uygulama, birçok takım arasında uzun ömürlü bir taahhüttür; bu yüzden yapı yaklaşımını, güvenli depolama kalıbını, CI/CD hattını ve API sürümleme politikasını her ürünün yeniden icat etmesine izin vermek yerine standartlaştırın. İç iş gücü uygulamaları genellikle kurulum, yapılandırma, uzaktan silme ve politika için mobil cihaz yönetiminden akar; müşteri uygulamaları ise gerçek kullanımı kapsayan bir cihaz çiftliğine ve denetlenmiş erişilebilirlik ve güvenliğe ihtiyaç duyar. Kritik bir arka uç değişikliğinin eski istemcilerin uzun kuyruğunu çaresiz bırakmaması için imzalama anahtarlarını, mağaza kimlik bilgilerini ve sürüm zamanlamasını merkezden yönetin.

**Kamu.** Satın alma kuralları, şeffaflık ve kamusal hesap verebilirlik her seçimi şekillendirir. Eski cihazlardaki ve yavaş bağlantılardaki insanlar dahil herkese hizmet etmelisiniz; bu yüzden erişilebilirlik gerçek yardımcı araçlarla doğrulanan yasal bir zorunluluktur ve geniş bir cihaz destek aralığı neredeyse pazarlıksızdır. Satıcıya kilitlenmeyi önleyen yaklaşımları ve sözleşmeleri tercih edin, veriyi taşınabilir tutun ve kamunun uygulamanın verileriyle ne yaptığını denetlemesine izin verin; cihazdaki kişisel veriyi denetimde haklı çıkarmanız ve belgelemeniz gereken bir risk olarak ele alın.

## Örnekler

**Girişim.** Alışkanlık takip uygulaması geliştiren üç kişilik bir girişimin hem iOS'a hem Android'e ulaşması gerekiyordu, ancak iki yerel kod tabanını ya da iki beceri kümesini karşılayamıyordu. Küçük bir takım her iki mağazaya da yayın yapabilsin diye bir çapraz platform çerçevesi seçtiler ve bir kullanıcı metroda sinyalsiz bir alışkanlığı kaydedip sonra senkronlayabilsin diye en baştan önce çevrimdışı tasarladılar. Giriş belirtecini düz bir dosyada değil platformun güvenli depolamasında tuttular, her sürüm planına mağaza inceleme süresini eklediler ve kendi telefonlarının yanında birkaç ucuz eski telefonda test ettiler; bu, aksi hâlde yayına gidecek ağır performansı yakaladı.

**Kurumsal.** Bir lojistik şirketi sürücüleri ve depo personeli için bir iç uygulama kurdu. Depolarda ve teslimat rotalarında sinyal dalgalı olduğu için takım önce çevrimdışı bir tasarım seçti: taramalar ve durum güncellemeleri yerelde kaydedilir ve bağlantı döndüğünde senkronlanır. Küçük bir takımla her iki platforma tek kod tabanından hizmet vermek için bir çapraz platform çerçevesi kullandılar. Uygulama herkese açık mağazalar yerine mobil cihaz yönetimi üzerinden dağıtılır; böylece BT, şirket cihazlarında kurulumu, yapılandırmayı ve güvenlik politikasını denetler. Hassas kimlik bilgileri platformun güvenli depolamasında yaşar ve uygulamanın kilidini biyometri açar. Bir bulut cihaz çiftliği, personelin gerçekte taşıdığı sağlam el cihazlarının temsilî bir yelpazesini test eder.

**Kamu.** Ulusal bir kurum kimlik ve yardımlar için yurttaşa dönük bir uygulama yayımladı. Erişilebilirlik ilk günden sert bir gereklilikti: tam ekran okuyucu desteği, dinamik metin boyutlandırma ve güçlü karşıtlık, yasayı karşılamak için gerçek yardımcı araçlarla test edildi. Yurttaşlar çok geniş bir cihaz yelpazesi kullandığı için takım eski modellerden ve yavaş bağlantılardan oluşan geniş bir bandı destekledi ve çekirdek görevleri çevrimdışı çalışır tuttu. Hassas veri güvenli cihaz depolamasında kalır, biyometri erişimi korur ve yüksek değerli bağlantılar planlı bir döndürme süreciyle sertifika sabitleme kullanır. API sürümleme eski kurulu uygulamaların çalışmasını sürdürür ve güvenlik düzeltmeleri için nadiren kullanılan bir zorunlu güncelleme yolu vardır. Mağaza inceleme süreleri her sürüm planına eklenmiştir.

## İş gerekçesi: motivasyonlar, YG ve TSM

Mobil, birçok kullanıcının hizmetinizle buluştuğu yerdir; bu yüzden uygulama, kurumunuz için önemli olan görevlerin benimsenmesini, memnuniyetini ve tamamlanmasını etkiler. Hızlı, güvenilir, iyi tasarlanmış bir uygulama kullanımı artırır ve destek yükünü azaltır. Kurumlar için bir iç mobil uygulama, mobil bir iş gücünü ölçülebilir biçimde daha üretken yapabilir ve evrak işini azaltabilir. Hükümetler için kullanışlı bir yurttaş uygulaması erişimi genişletir ve çağrı merkezi ile yüz yüze talebi azaltır.

Toplam sahip olma maliyeti (TSM) açısından yaklaşım seçimi en büyük kaldıraçtır. Yerel geliştirme, uygulamanın tüm ömrü boyunca iki kod tabanı ve iki beceri kümesi için ödeme yapmak demektir. Çapraz platform bunun bir kısmını güncel tutmanız gereken bir bağımlılıkla takas eder. Kodun ötesinde mağaza ücretleri ve inceleme döngüleri, bir cihaz test laboratuvarı ya da bulut çiftliği, platformlar yıllık sürüm çıkardıkça süregelen işletim sistemi sürümü desteği ve mobilin gerektirdiği güvenlik çalışması için bütçe ayırın. Yetersiz yatırımın maliyeti desteklenmeyen cihazlardaki çökmelerde, korumasız cihaz içi veriden doğan güvenlik olaylarında, reddedilen ya da geciken sürümlerde ve yavaş ya da beceriksiz bir uygulamayı terk eden kullanıcılarda ortaya çıkar.

Liderliğe gerekçeyi kurmak için uygulamayı somut sonuçlara bağlayın: görev tamamlama, elde tutma, iş gücü verimliliği ya da azalan destek maliyeti. Yaklaşım kararını yalnızca ilk sürümü değil, uygulamanın ömrü boyunca fiyatlandırın ve ciddi bir mobil pratiğinin azalttığı riskleri (güvenlik, erişilebilirlik yasası, mağaza reddi) adlandırın.

## Anti-kalıplar ve tuzaklar

- **Mobili küçültülmüş bir web sitesi olarak görmek**: dokunmayı, hareketleri ve platform geleneklerini görmezden gelmek.
- **Kusursuz bir ağ varsaymak**: çevrimdışı yönetim yok, bu yüzden sinyal düştüğü anda uygulama bozulur.
- **Yalnızca en yeni amiral gemisinde test**: gerçek kullanıcıların taşıdığı cihazlardaki zayıf performansı gizler.
- **Sırları düz dosyalarda saklamak**: bir cihaz kaybolduğunda ya da çalındığında hassas veri açığa çıkar.
- **Bildirim yağmuru**: çok fazla anlık bildirim, kullanıcılar uygulamayı susturur ya da siler.
- **Mağaza inceleme süresini görmezden gelmek**: anında yayımlama varsayan ve sonra kayan sürüm planları.
- **Zorunlu güncelleme yolu olmaması**: güvensiz eski sürümler onları emekliye ayıracak bir yol olmadan yaşamayı sürdürür.
- **Pil ve veri tüketmek**: kullanıcıların fark ettiği sürekli arka plan işi ve geveze ağ trafiği.
- **Sonradan akla gelen erişilebilirlik**: kullanıcıları dışlar ve kamuda yasayı çiğner.
- **Her yerde aynı görünmeye zorlanan tek kod tabanı**: her iki platformda da yabancı hisseden bir uygulama.

## Olgunluk modeli

**Düzey 1, Başlangıç.** Mobil geçici ve tepkiseldir. Uygulama bir web sitesi gibi kurulur, takımın kendi telefonlarında test edilir ve çoğu zaman çevrimdışıyken bozulur. Güvenli depolamaya, erişilebilirliğe ya da mağaza inceleme takvimlerine az düşünce verilir. Sürümler stresli bir elle telaştır ve yapı yaklaşımının ya da imzalama anahtarlarının sahibi yoktur.

**Düzey 2, Geliştirme.** Temel pratikler ortaya çıkar, ancak takımlar ve ürünler arasında tutarsızdır. Belirli bir uygulama için bir yapı yaklaşımı seçilir, platform temellerini izler ve birkaç gerçek cihazda test edilir; biraz çevrimdışı yönetim ve güvenli depolama vardır. Derlemeler kısmen otomatiktir ve mağaza gönderimlerinin bir sahibi vardır, ancak başka bir takımın uygulaması bunların hepsini hâlâ farklı yapıyor ya da hiç yapmıyor olabilir.

**Düzey 3, Standartlaştırma.** İyi pratik belgelenmiş ve kurum genelinde zorlanıyor. Önce çevrimdışı varsayılandır, belgelenmiş bir cihaz destek aralığı bir cihaz laboratuvarında ya da bulut çiftliğinde test edilir ve platform tasarım yönergeleri ile erişilebilirlik izlenir ve gerçek yardımcı araçlarla doğrulanır. Güvenli depolama, biyometri ve API sürümleme standarttır, CI/CD derlemeleri, testleri, imzalamayı ve beta dağıtımını otomatikleştirir ve mağaza inceleme süresi her sürüme planlanır.

**Düzey 4, Yönetme.** Mobil kalite taban değerlere karşı ölçülür ve denetlenir. Çökmeler, soğuk başlangıç ve ekran işleme performansı, pil ve veri kullanımı ve görev tamamlama oranları gerçek cihazlardan sürekli yakalanır ve hedeflere karşı izlenir; model ve işletim sistemi sürümü başına kırılımlarla, böylece düşük uç donanımdaki bir gerileme yayına gitmez, yakalanır. Erişilebilirlik ve güvenlik varsayılmak yerine denetlenir, bildirim çıkış ve güncelleme benimseme oranları izlenir ve destek aralığı ile yapı yaklaşımı bu kanıta göre gözden geçirilir. Bir sürüm için durdur ya da düzelt kararları, uygulamanın liderin telefonunda nasıl hissettirdiğine değil ölçütlere dayanır.

**Düzey 5, Orkestrasyon.** Mobil sürekli iyileştirilir ve kurum genelinde bütünleşiktir; cihaz manzarası değiştikçe uyum sağlar. Sertifika döndürme, zorunlu güncelleme yolları ve geri alma rutindir, destek aralığı ve yapı yaklaşımı platformlar yıllık sürüm çıkardıkça kanıta göre yeniden kapsamlanır ve kullanıcıların ve cihazların tüm yelpazesi birinci sınıf sayılır. Mobil planlama güvenlik, erişilebilirlik, API ve teslimat pratiğiyle birleştirilmiştir; bir işletim sistemi değişikliği, yeni bir cihaz katmanı ya da politika kayması acil durum olarak değil rutin iş olarak sindirilir.

## Tartışma fikirleri

- Belirli bir ürün için yerel, çapraz platform ve aşamalı web uygulaması arasında nasıl karar verirsiniz?
- Gerçek kullanıcı verilerinize hangi cihaz ve işletim sistemi sürümü destek aralığı uyar ve onu nasıl güncel tutarsınız?
- Uygulamanızda önce çevrimdışı nerede şarttır ve senkron çakışmalarını nasıl ele alacaksınız?
- Zorunlu güncelleme ne zaman haklıdır ve kullanıcıları haksız yere engellemekten nasıl kaçınırsınız?
- Kullanıcılarınızı yansıtan bir ölçekte gerçek cihazlarda nasıl test edeceksiniz?
- Cihazda hangi hassas veri yaşıyor ve her biri nasıl korunuyor?
- Ortak bir kod tabanından her platformun geleneklerine nasıl saygı gösterirsiniz?

## Önemli çıkarımlar

- Yapı yaklaşımını (yerel, çapraz platform ya da PWA) uygulamanın tüm ömrü için seçin.
- Uygulama tanıdık hissetsin ve kullanıcı emeğini azaltsın diye platform tasarım yönergelerini izleyin.
- Mobil kısıtlar için tasarlayın: önce çevrimdışı, tutumlu pil ve veri, parçalanma, küçük ekranlar.
- Sürüm zamanlamasını siz denetlemezsiniz; mağaza incelemesini, sürümlemeyi ve zorunlu güncellemeleri planlayın.
- Anlık bildirimleri ve derin bağlantıları ölçülü ve rızayla kullanın.
- Cihazdaki veriyi güvenli depolama, biyometri ve gerekli yerde sertifika sabitlemeyle güvenceye alın.
- Gerçek cihazlarda test edin ve mobil hattı CI/CD ile otomatikleştirin.
- Erişilebilirliği bir gereklilik yapın; kamu için bu yasal bir zorunluluktur.

## Kaynaklar ve ileri okuma

- Apple, *Human Interface Guidelines*
- Google, *Material Design* guidelines
- Apple, *App Store Review Guidelines*
- Google, *Google Play developer policies and Android developer documentation*
- OWASP, *Mobile Application Security Verification Standard (MASVS)* and *Mobile Security Testing Guide*
- React Native project documentation
- Flutter project documentation
- Google, *web.dev* guidance on progressive web apps
- U.S. Section 508 and WCAG (Web Content Accessibility Guidelines) references for mobile accessibility
- NIST, *Guidelines on mobile device security and management*
