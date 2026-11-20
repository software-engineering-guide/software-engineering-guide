# 4.3 Altyapı ve bulut güvenliği

## Genel bakış ve motivasyon

Uygulamalar altyapı üzerinde çalışır ve bu altyapı günümüzde büyük ölçüde bulut tabanlı, yazılım tanımlı ve sürekli değişen bir yapıdır. Tek bir mühendis artık tek bir komutla bir veritabanı hazırlayabilir, bir ağ yolu açabilir ya da bir izin verebilir; üstelik bunu geleneksel değişiklik denetiminin hiç öngörmediği bir ölçekte ve hızda yapar. Bulut ihlallerinin önde gelen nedeninin egzotik istismarlar değil yanlış yapılandırma olmasının tam sebebi bu güçtür. Yanlışlıkla herkese açık bırakılmış bir depolama kovası ya da fazla geniş bir erişim rolü, bir kurumun tüm verisini saniyeler içinde açığa çıkarabilir.

Büyük kurumlarda bulut altyapısı birden çok sağlayıcıyı, binlerce hesabı ve yönetilen hizmetlerin, konteynerlerin ve sunucusuz işlevlerin bir karışımını kapsar. Saldırı yüzeyi durağan bir çevre değildir. Yaşayan, genişleyen bir kaynak ve kimlik topluluğudur. Kamu için aynı karmaşıklık, her mimari tercihi şekillendiren katı yetkilendirme rejimleri, veri ikametgâhı zorunlulukları ve sınıflandırma sınırlarıyla buluşur. Her ikisinde de kimlik katmanı yeni çevre haline gelmiştir: kim, hangi kaynakta, hangi koşullar altında ne yapabilir.

Bu bölüm, o temelin nasıl güvenceye alınacağını kapsar: [kimlik ve erişim yönetimi](https://en.wikipedia.org/wiki/Identity_management) (IAM), [ağ bölümlendirme](https://en.wikipedia.org/wiki/Network_segmentation), [şifreleme](https://en.wikipedia.org/wiki/Encryption) ve [anahtar yönetimi](https://en.wikipedia.org/wiki/Key_management), konteynerlerin ve [sunucusuz](https://en.wikipedia.org/wiki/Serverless_computing) iş yüklerinin güvenliği ve hızla hareket eden bir bulut varlığının tehlikeye sürüklenmesini önleyen sürekli duruş yönetimi.

## Temel ilkeler

- **Kimlik çevredir.** Erişim kararları ağ konumuna değil, güçlü kimliğe ve ince taneli yetkilendirmeye dayanır.
- **Her zaman en az ayrıcalık.** Her kimlik, insan ya da makine, ihtiyaç duyduğu asgari izinleri alır, fazlasını değil.
- **Kapsamak için bölümlendirin.** Ağları ve iş yüklerini, bir alandaki ele geçirilmenin serbestçe yayılamayacağı biçimde bölün.
- **Her yerde şifreleyin.** Veriyi aktarım sırasında ve beklemede, iyi yönetilen anahtarlarla varsayılan olarak koruyun.
- **Değişmez ve bildirimsel.** Altyapıyı kod olarak (IaC) tanımlayın, değişmez biçimde dağıtın ve sapmayı bir kusur sayın.
- **Sürekli doğrulama.** Duruş tek seferlik bir denetim değildir; sürekli tarayın ve uygulatın.
- **Güvenli varsayılan yapılandırma.** Herhangi bir kaynağın varsayılan durumu açık değil, kilitli olmalıdır.

## Öneriler

### Kimlik ve erişim yönetimini bilinçli tasarlayın

IAM, bulut güvenliğinin en önemli parçasıdır ve en sık yanlış yönetilen parçasıdır.

- İzinleri iş işlevine göre vermek için **[rol tabanlı erişim denetimini](https://en.wikipedia.org/wiki/Role-based_access_control) (RBAC)**, daha ince ve bağlama duyarlı kararların gerektiği yerde (etiketlere, ortama, veri sınıflandırmasına ya da zamana dayalı) **[öznitelik tabanlı erişim denetimini](https://en.wikipedia.org/wiki/Attribute-based_access_control) (ABAC)** kullanın.
- Uzun ömürlü statik kimlik bilgilerini ortadan kaldırıp yerine kısa ömürlü, otomatik olarak verilen belirteçleri ve iş yükü kimliği federasyonunu koyun.
- Tüm insan erişimi için [MFA](https://en.wikipedia.org/wiki/Multi-factor_authentication)'yı (çok faktörlü kimlik doğrulama) zorunlu kılın ve ayrıcalıklı eylemler için güçlü kimlik doğrulama isteyin.
- En az ayrıcalığı titizlikle uygulayın: sıfırdan başlayın ve izinleri bilinçli biçimde ekleyin. Kullanılmayan izinleri düzenli olarak gözden geçirip budayın; erişim birikme eğilimindedir.
- Görevleri ayırın; böylece hiçbir tek kimlik hassas değişiklikleri hem yapıp hem onaylayamaz.
- Ortamlar (üretim, hazırlık, geliştirme) arasında ve iş birimleri arasında sert sınırlar oluşturmak için özel hesaplar ya da projeler kullanın.

### Ağları bölümlendirin ve iş yüklerini mikro bölümlendirin

Düz ağlar, saldırganların içeri girdikten sonra yanlara doğru dolaşmasına izin verir. Bölün ve kapsayın.

- Ağ düzeyinde katmanlara ve bölgelere bölümlendirin ve yalnızca her katmanın meşru olarak ihtiyaç duyduğu trafiğe izin verin.
- Tek tek iş yüklerinin yalnızca gerek duydukları belirli eşlerle iletişim kurması için, geniş alt ağ kuralları yerine kimliğe duyarlı politikayla uygulanan **mikro bölümlendirme** uygulayın.
- Doğu-batı trafiğini varsayılan olarak reddedin; açık izin kuralları isteyin.
- Hassas veri depolarını doğrudan internete açık olmayan, yalnızca denetlenen yollardan erişilen özel alt ağlara yerleştirin.
- Mümkün olduğunda yönetilen hizmetlere genel internet üzerinden yönlendirmek yerine özel bağlantı kullanın.

### Veriyi şifreleyin ve anahtarları doğru yönetin

Şifreleme, arkasındaki anahtar yönetimi kadar güçlüdür.

- **Aktarım sırasında**, dahili hizmetten hizmete trafik dahil her yerde güncel [TLS](https://en.wikipedia.org/wiki/Transport_Layer_Security) (Transport Layer Security) ile şifreleyin.
- Tüm depolama, veritabanı ve yedekler için **beklemede** varsayılan olarak şifreleyin.
- Anahtarları bir **Anahtar Yönetim Hizmeti (KMS)** ile yönetin ve en yüksek güvenceli anahtarlar ile düzenleyici gereksinimler için bir **[Donanım Güvenlik Modülü](https://en.wikipedia.org/wiki/Hardware_security_module) (HSM)** kullanın.
- Anahtarları bir takvime göre döndürün ve şüpheli ele geçirilmede hızlı döndürmeyi destekleyin.
- Anahtarları kimin kullanıp yönetebileceğini, veriye kimin erişebileceğinden ayrı olarak denetleyin ve izleyin; böylece anahtar saklama görevler ayrılığını uygulatır.
- Düzenleme ya da sözleşmeye dayalı güven, anahtarları sağlayıcının değil kurumun tutmasını gerektiriyorsa müşteri tarafından yönetilen anahtarları düşünün.

### Konteynerleri, Kubernetes'i ve sunucusuzu güvenceye alın

Her hesaplama modeli kendi risklerini getirir.

- **Konteynerler:** asgari, güvenilir temel imajlardan inşa edin; imajları dağıtımdan önce açıklar için tarayın; root olmayan kullanıcı olarak çalıştırın; mümkün olan yerde dosya sistemlerini salt okunur yapın; ve sırları asla imajlara gömmeyin.
- **[Kubernetes](https://en.wikipedia.org/wiki/Kubernetes):** RBAC'ı etkinleştirin ve hizmet hesaplarını sıkı biçimde kapsamlandırın; mikro bölümlendirme için ağ politikaları uygulayın; standartları uygulatmak için kabul denetleyicileri ve politika motorları kullanın; ayrıcalıklı konteynerleri kısıtlayın; hassas iş yüklerini yalıtın; ve denetim düzlemini ve düğümleri yamalı tutun.
- **Sunucusuz:** her işlevin yürütme rolüne en az ayrıcalık uygulayın (aşırı izinlendirmenin yaygın bir kaynağı); tüm olay girdilerini doğrulayın; sırları platformun sır deposu üzerinden yönetin; ve anormal çağrı örüntülerini izleyin.

Model ne olursa olsun, çalışma zamanını yamalı ve imajları taze tutun. Bir konteyner, içindeki yazılım kadar güvenlidir.

### Bulut güvenlik duruşunu sürekli yönetin

Bulut, periyodik elle denetimlerin yetişemeyeceği kadar hızlı değişir.

- Hesaplar genelinde yanlış yapılandırmaları, herkese açık maruziyeti ve politika ihlallerini sürekli saptamak için **Bulut Güvenlik Duruşu Yönetimi (CSPM)** araçlarını benimseyin.
- Güvenlik politikasını kod olarak tanımlayın ve dağıtım zamanında uygulatın; böylece kötü yapılandırmalar yerine oturmadan engellenir.
- Tespite (olaydan sonra uyarılar) göre önlemeyi (yanlış yapılandırmayı durduran korkuluklar) tercih edin ve ikisini birleştirin.
- Kaynakların ve kimliklerin doğru bir envanterini tutun; göremediğinizi güvenceye alamazsınız.
- Bildirilen altyapı-kod hali ile gerçekte çalışan durum arasındaki sapmayı izleyin ve giderin.

## Ödünleşimler: artılar ve eksiler

| Karar | Artılar | Eksiler |
|---|---|---|
| RBAC | Basit, anlaşılır, denetlemesi kolay | Kaba, ölçekte rol patlaması |
| ABAC | İnce taneli, bağlama duyarlı, etiketlerle ölçeklenir | Tasarlaması ve üzerine akıl yürütmesi karmaşık |
| Sağlayıcı yönetimli anahtarlar (KMS) | Kolay, entegre, düşük operasyonel yük | Saklama sağlayıcıda; daha az denetim |
| Müşteri yönetimli anahtarlar/HSM | Tam denetim, katı zorunlulukları karşılar | Operasyonel yük, anahtar kaybetme riski |
| Önleyici korkuluklar | Yanlış yapılandırmayı olmadan durdurur | Meşru işi engelleyebilir, ayar gerektirir |
| Yalnızca dedektif CSPM | Esnek, engellemez | Tespitten önce zarar oluşabilir |
| Mikro bölümlendirme | Güçlü yanal hareket kapsama | Operasyonel karmaşıklık, politika yayılması |

Baskın ödünleşim, denetim ile operasyonel yük arasındadır. Daha sıkı kontroller (müşteri yönetimli anahtarlar, katı mikro bölümlendirme, ABAC) riski azaltır, ama küçük takımların sürdürmekte zorlandığı uzmanlık ve bakım ister. Doğru düzey, verinin ne kadar hassas olduğuna ve hangi düzenlemelerin geçerli olduğuna bağlıdır. Pragmatik bir yaklaşım, herkes için güçlü güvenli varsayılanları katmanlar, ek titizliği en yüksek riskli sistemlere ayırır ve güvenli seçimi elle disiplin yerine varsayılan kılan otomatik korkulukları yeğler.

## Takımınızla tartışılacak sorular

1. **Sert hesap ya da proje sınırlarını nerede çizeceksiniz ve her birinin içine ne ait olacak?** Özel hesaplar ve projeler bulutun sunduğu en güçlü kapsamayı yaratır; böylece geliştirmedeki bir ele geçirilme üretime ulaşamaz ve bir iş birimi bir başkasının verisine dokunamaz. Varlığınız binlerce hesaba büyümeden önce sınır şemanıza karar verin, çünkü düz bir yapıya yalıtımı sonradan eklemek yavaş ve risklidir. Kurumsal ve kamu işleri için bu sınırlar ayrıca ortam ayrımına, veri sınıflandırmasına ve denetçilerin görmeyi beklediği patlama yarıçapı sınırlarına düzgünce eşlenir. Bugün hangi iş yüklerinin bir hesabı paylaştığını gösteren güncel bir diyagram getirin ve tek bir fazla geniş rolün üretim ile üretim dışını kapsadığı yerleri işaretleyin. Hassas veri deneysel iş yükleriyle aynı hesapta duruyorsa, önce düzeltilecek sınır budur.

2. **Anahtarları kimin yönetebileceği ile şifrelenmiş veriye kimin erişebileceği için standardınız nedir?** Şifreleme, anahtar yönetimi kadar güçlüdür ve anahtar saklamayı veri erişiminden ayırmak KMS'inizi görevler ayrılığı için bir uygulama noktasına çevirir. Anahtarları kimin oluşturabileceğine, döndürebileceğine ve kullanabileceğine karar verin ve bu kümenin, o anahtarların koruduğu veriyi okuyabilen kişilerle örtüşmediğinden emin olun. Düzenlemeye tabi ve kamu sistemleri için bu, çoğu zaman sağlayıcı yönetimli anahtarlar ile daha fazla denetim ve anahtar kaybetme gibi daha fazla operasyonel risk taşıyan müşteri yönetimli anahtarlar ya da HSM'ler arasındaki seçimi belirler. Mevcut anahtar politikalarınızı getirin ve herhangi bir tek kimliğin hem bir anahtarı yönetip hem de arkasındaki veriyi okuyup okuyamadığını denetleyin; çünkü bu yaygın bir sessiz boşluktur. Saklama ve erişim ayrılmamışsa, beklemede şifreleme sizi pano gösterdiğinden daha az koruyordur.

3. **Güvenli varsayılanları, yalnızca önerilmiş olmak yerine yerleşim bölgenizde kaçınılmaz nasıl kılacaksınız?** Bulut ihlallerinin önde gelen nedeni egzotik istismarlar değil yanlış yapılandırmadır ve çözüm, herkese açık bir veritabanını ya da şifrelenmemiş bir kovayı olaydan sonraki uyarılar değil, oturmadan önce engelleyen önleyici korkuluklardır. Hangi politikaları dağıtım zamanında uygulatacağınıza (herkese açık depolama yok, varsayılan olarak şifreleme açık, zorunlu etiketler) ve hangilerini yalnızca saptayıp raporlayacağınıza karar verin. Büyük bir takım için bunları yerleşim bölgelerine ve altyapı-kod şablonlarına kodlamak, her yeni hesabın takım başına çaba olmadan korumayı miras almasını sağlar ve güvenliği yinelenen bir vergiden tek seferlik bir yatırıma çevirir. Geçen ayın yanlış yapılandırma bulgularını getirin ve hangilerini bir önleyici korkuluğun tümden durduracağını sorun. Duruş yönetiminiz yalnızca dedektifse, uyarıyı kimse görmeden zarar oluşabilir; bu yüzden en yüksek etkili kontrolleri önlemeye taşıyın.

4. **Sessizce onlara bağımlı olan otomasyonu bozmadan uzun ömürlü statik kimlik bilgilerini nasıl ortadan kaldıracaksınız?** Hiç süresi dolmayan gömülü erişim anahtarları bulut ihlallerinin en yaygın nedenleri arasındadır, çünkü bir betikte, günlükte ya da depoda sızan tek bir anahtar saldırgana kalıcı erişim verir. Karşıt çekim operasyoneldir: eski CI işleri, cron görevleri ve üçüncü taraf entegrasyonlar çoğu zaman statik bir anahtarın var olduğunu varsayar ve onu kısa ömürlü belirteçlere ya da iş yükü kimliği federasyonuna geçirmek kimsenin planlamadığı mühendislik zamanı alır. Büyük bir takım için ortak bir geçiş yolu (belirteçleri otomatik verin, bir son kullanma standardı koyun ve her yeni uzun ömürlü anahtarda alarm verin), her grubun kendi daha zayıf yanıtını icat etmesini önler. Kullanımdaki her statik kimlik bilgisinin, yaşının, patlama yarıçapının ve beslediği sistemin bugün federe kimliği kabul edip edemeyeceğinin envanterini getirin. Kurumsal ve kamu ortamlarında son tarihi denetim ve yetkilendirme döngülerine bağlayın; çünkü onu oluşturan kişiden daha uzun yaşayan bir kimlik bilgisi, sürekli yetkilendirmeyi tam olarak durduran bulgudur.

5. **Bir kaynak yanlış yapılandırıldığında ya da bir anahtar ele geçirildiğinde onu ne kadar hızlı saptayıp, kapsayıp ve giderebilirsiniz ve bunu ölçtünüz mü?** Herkese açık bir kova ya da fazla geniş bir rol, ancak açık kaldığı pencere kadar tehlikelidir; bu yüzden ortalama saptama ve giderme süresi, maruziyetinizi gerçekten sınırlayan sayıdır. Gerilim, hatayı dağıtım zamanında durduran önleyici korkuluklar ile kaçanı yakalayan dedektif duruş yönetimi arasındadır ve korkulukların her şeyi kapsadığına dair rahatlatıcı bir varsayım yerine ikisi için de dürüst rakamlara ihtiyacınız vardır. Son çeyreğin yanlış yapılandırma ve sapma bulgularını zaman damgalarıyla, ortaya çıkıştan gidermeye kadar medyan süreyi ve bir anahtar ele geçirilmesi döndürmesinin prova kaydını getirin. Binlerce hesaba yayılan kurumsal ve kamu varlıkları için, kimsenin takımının açıkça sahip olmadığı bir bulgunun giderilmesinin kime ait olduğu üzerinde anlaşın; çünkü hesap verebilir bir yanıtlayıcısı olmayan bir uyarı, bir olaya dönüşerek yaşlanan bir uyarıdır.

6. **Güvenlik duruşunu, herkesi ağır çekime almadan birden çok bulut, hesap ve takım arasında nasıl tutarlı tutacaksınız?** Çoklu bulut ve çoklu hesap varlıkları hızla parçalanır: her sağlayıcının kendi IAM modeli, kendi varsayılanları ve kendi duruş araçları vardır; bu yüzden bir yerde uygulanan politika başka bir yerde sessizce geçersiz kalır. Ödünleşim, tutarlılığı garanti eden merkezi denetim ile takımların hızlı hareket etmesini sağlayan yerel özerklik arasındadır ve herhangi bir yöne fazla yaslanmak ya teslimatı darboğaza sokar ya da standartların sapmasına izin verir. Mevcut kapsam haritanızı getirin: hangi hesaplar yerleşim bölgesi korkuluklarını miras alıyor, hangileri yönetilmiyor ve aynı kontrolün sağlayıcılar arasında nerede üç farklı biçimde ifade edildiği. Büyük ya da kamusal bir kurum için denetim açısını ekleyin, çünkü denetçiler her yerde uygulanan tek bir savunulabilir standart bekler ve birincil bulutunuzda olup ikincil bulutunuzda olmayan bir kontrol, kararlı bir saldırganın ya da değerlendiricinin önce bulacağı bir boşluktur.

## Sektör merceği

**Girişim.** Hız ve hayatta kalma kazanır; bu yüzden tamamen bedavaya gelen güvenli varsayılanlara yaslanın: beklemede şifreleme açık, bir insan açmadıkça özel depolama, kök hesapta MFA ve yapıştırılmış erişim anahtarları yerine sağlayıcının yerleşik iş yükü kimliği. Bir CSPM platformu kurmayın ya da sürdüremeyeceğiniz mikro bölümlendirmeyi elle yapmayın; internete açılmış bir veritabanını engelleyen tek bir korkuluk, bir öğleden sonralık işle korumanın çoğunu sağlar. Sertleştirme sizinle birlikte ölçeklenip sonradan bir yeniden yazıma dönüşmesin diye her şeyi baştan altyapı-kod olarak tutun.

**Küçük işletme.** Özel bir güvenlik mühendisi ve dar bir bütçe olmadan, kendi KMS disiplininizi kurmak yerine varsayılanları zaten sertleştirilmiş ve anahtar yönetimi sizin için halledilmiş yönetilen hizmetleri tercih edin. Bulut güvenliğini bir yapılandırma hijyeni sorusu olarak ele alın: hangi kovaların ve veritabanlarının var olduğunu bilin, onları özel tutun, MFA isteyin ve sağlayıcının ek maliyetsiz gelen yerel duruş denetimlerini açın. Araç satın alırken, herkese açık maruziyeti ve şifrelenmemiş depolamayı kutudan çıkar çıkmaz işaretleyenleri yeğleyin; çünkü kaçınılabilir ihlallerin çoğuna bu iki hata yol açar.

**Kurumsal.** Asıl sorun binlerce hesap ve birçok takım arasında tutarlılıktır; bu yüzden iş platform işidir: her hesabı sertleştirilmiş hazırlayan yerleşim bölgeleri, politika-kod olarak uygulanan korkuluklar ve sapma için sürekli tarayan CSPM. Gruplar daha zayıf sürümleri yeniden icat etmeyi bıraksın diye IAM modelini, anahtar saklama kurallarını ve bölümlendirme taban çizgisini standartlaştırın ve her takımın sözüne güvenmek yerine duruşu varlık genelinde ölçün. Sağlayıcılar hizmet ekledikçe ve varlık büyüdükçe politikaları güncel tutacak süregelen mühendisliği bütçeleyin.

**Kamu.** Tedarik kuralları, veri ikametgâhı zorunlulukları ve yetkilendirme rejimleri her tercihi şekillendirir; bu yüzden güvenlik kontrolleri denetim kanıtı olarak da iş görür. Saklaması veri erişiminden ayrılmış FIPS onaylı anahtar yönetimini, verileri ulusal sınırlar içinde tutan yalıtılmış bölgeleri ve imzalı, taranmış, sıkı kabul denetimli konteyner imajlarını yeğleyin. Yayımlayabileceğiniz güvenceleri yayımlayın, sürekli duruş yönetimini doğrudan süregelen yetkilendirmeye besleyin ve satıcılardan yapılandırma varsayılanlarını açıklamalarını ve sınıflandırma sınırlarınızın gerektirdiği bölümlendirme ve anahtar saklama kontrollerini desteklemelerini isteyin.

## Örnekler

**Girişim.** Küçük bir girişim her şeyi tek bir bulut hesabında çalıştırır ve bir platform takımı kadrolayamaz; bu yüzden güvenli gelen varsayılanlara yaslanır: varsayılan olarak beklemede şifreleme açık, bir insan açıkça açmadıkça özel depolama kovaları ve kök hesapta zorunlu MFA. CI'a yapıştırılmış uzun ömürlü erişim anahtarları yerine, hattın kısa ömürlü kimlik bilgilerini otomatik alması için sağlayıcının yerleşik iş yükü kimliğini kullanır. İnternete açılan her veritabanını işaretleyen tek bir ücretsiz korkuluk, onları en yaygın ve en pahalı bulut hatasından, kurulum için bir öğleden sonralık bedelle kurtarır.

**Kurumsal.** İki bulut sağlayıcısında binlerce hesap çalıştıran bir medya şirketi bir yerleşim bölgesi örüntüsü uygular: her hesap, varsayılan olarak beklemede şifreleme açık, depolamada herkese açık erişim yok, zorunlu etiketler ve bir korkuluk politikası taban çizgisi içeren bir şablondan hazırlanır. CSPM sapma için sürekli tarar ve iş yükü kimliği federasyonu CI sistemleri için uzun ömürlü anahtarları ortadan kaldırmıştır. Bir geliştirici yanlışlıkla bir veritabanını internete açmaya kalkıştığında, önleyici bir politika değişikliği engeller ve otomatik olarak bir bilet açar.

**Kamu.** Savunma yanlısı bir kurum, hiçbir verinin ulusal sınırları terk etmemesi için veri ikametgâhının politikayla uygulandığı yalıtılmış bir bulut bölgesinde çalışır. En hassas anahtarlar, anahtar saklaması görevler ayrılığını uygulatmak üzere veri erişiminden ayrılmış FIPS onaylı (Federal Information Processing Standards) HSM'lerde yaşar. Kubernetes kümeleri katı ağ politikaları ve kabul denetimleri kullanır; her konteyner imajı çalışmasına izin verilmeden önce taranır ve imzalanır. Sürekli duruş yönetimi doğrudan kurumun süregelen yetkilendirme kanıtına beslenir.

## İş gerekçesi: motivasyonlar, YG ve TSM

Bulut altyapısı güvenliği, küçük bir yatırımın yıkıcı, manşetlik kayıpları önlediği yerdir. Toplam sahip olma maliyeti; CSPM araçlarını, anahtar yönetim hizmetlerini, en az ayrıcalıklı IAM ve bölümlendirmeyi tasarlamak için mühendislik zamanını ve politikaları güncel tutmak için süregelen çabayı içerir. Bu maliyetler gerçektir ama mütevazıdır. Onları atlamanın maliyeti, tüm bir müşteri veritabanını açığa çıkaran tek bir yanlış yapılandırılmış kaynak ve ardından gelen düzenleyici cezalar, bildirim maliyetleri ve kalıcı marka zararıdır. Bulut yanlış yapılandırma ihlalleri sektörde en yaygın ve en çok önlenebilir olaylar arasındadır.

Otomasyon ve yeniden kullanım YG'yi güçlendirir. Güvenli varsayılanları yerleşim bölgelerine ve altyapı-kod şablonlarına kodlayın; böylece her yeni hesap ve iş yükü, takım başına çaba olmadan korumayı miras alır ve güvenlik yinelenen elle bir vergiden tek seferlik bir platform yatırımına dönüşür. Kamu ve düzenlemeye tabi kurumlar için güçlü duruş yönetimi ayrıca kanıtı otomatik üreterek denetimlerin ve sürekli yetkilendirmenin maliyetini düşürür. Liderliğe gerekçeyi sunarken, kimlik ve yapılandırma katmanının artık birincil ihlal vektörü olduğunu, yanlış yapılandırmanın önlenebilir olduğunu ve korkulukların hem riski hem de elle incelemenin sürtünmesini azalttığını vurgulayın.

## Anti-kalıplar ve tuzaklar

- **Joker karakter izinleri.** "İşler yürüsün diye" geniş `*` erişimi verip onu hiç sıkılaştırmamak.
- **Uzun ömürlü statik anahtarlar.** Betiklere ve CI'a gömülü, hiç süresi dolmayan ve sonunda sızan erişim anahtarları.
- **Düz ağlar.** Bölümlendirme yok; böylece ele geçirilmiş tek bir ana makine her şeye ulaşır.
- **Kazara herkese açık.** Varsayılan ya da özensiz ayarlarla internete açılmış depolama ve veritabanları.
- **Anahtar disiplini olmadan şifreleme.** Şifrelemeyi etkinleştirip anahtar erişimini ardına kadar açık bırakmak ya da anahtarları hiç döndürmemek.
- **İmajlara gömülü sırlar.** Konteyner imajlarına gömülen ve imajın çalıştığı her yere yayılan kimlik bilgileri.
- **Aşırı izinli sunucusuz roller.** Kapsamlandırma atlandığı için ihtiyaçlarından çok daha fazlası verilmiş işlevler.
- **Yalnızca denetim duruşu.** Yanlış yapılandırmaları dağıtım zamanında önlemek yerine olaydan sonra saptamak.
- **Sapmayı görmezden gelmek.** Çalışan ortamın, gerçek durumu kimse bilmeyene kadar altyapı-koddan ayrışmasına izin vermek.

## Olgunluk modeli

**Düzey 1, Başlangıç.** Bir kaynağa kimin ihtiyacı varsa onun yönlendirdiği elle hazırlama. Geniş joker karakter izinleri ve uzun ömürlü statik anahtarlar. Bölümlendirmesiz düz ağlar. Şifreleme tutarsız uygulanır, uygulanıyorsa. Duruş yönetimi yoktur; yanlış yapılandırmalar ancak bir olay soruyu zorlayınca ortaya çıkar.

**Düzey 2, Geliştirme.** Bazı IAM rolleri ve MFA ortaya çıkar, büyük depolar için beklemede şifreleme açılır, ama uygulama takımdan takıma değişir. Varsayılan reddi olmayan temel ağ katmanları vardır. Yapılandırma incelemeleri periyodik ve elle yapılır. Altyapı kısmen kod olarak tanımlanmıştır; bu yüzden sertleştirme hesabı hangi grubun hazırladığına bağlıdır.

**Düzey 3, Standartlaştırma.** Kısa ömürlü kimlik bilgileriyle en az ayrıcalıklı RBAC ve ABAC belgelenmiş ve kurum genelinde uygulanmıştır. Bölümlendirme varsayılan reddeden doğu-batı kullanır. Aktarım sırasında ve beklemede şifreleme varsayılan olarak açıktır; anahtarlar bir döndürme takvimiyle KMS'tedir ve saklama veri erişiminden ayrılmıştır. Konteyner ve Kubernetes sertleştirmesi bir standarttır ve CSPM her hesapta tutarlı uygulanan tanımlı politikalara karşı çalışır.

**Düzey 4, Yönetme.** Duruş varsayılmaz, ölçülür. Adlandırılmış metrikleri taban çizgilerine ve hedeflere karşı izlersiniz: en az ayrıcalık taban çizgisi içindeki kimliklerin payı, yanlış yapılandırmaları ve sapmayı saptama ve giderme için ortalama süre, hesaplar genelinde korkuluk ve CSPM kapsamı, anahtar döndürme uyumu ve hayatta kalan uzun ömürlü kimlik bilgilerinin sayısı. Bulgular patlama yarıçapına göre önceliklendirilir, gidermenin bir sahibi ve bir hizmet düzeyi hedefi vardır ve bu sayılardaki eğilim verisi bir sonraki sertleştirme çabasının nereye gideceğini belirler.

**Düzey 5, Orkestrasyon.** Güvenli varsayılanlar yerleşim bölgelerine ve altyapı-koda gömülüdür; böylece her kaynak sertleştirilmiş doğar ve kontroller varlık ile tehdit tablosu değiştikçe uyum sağlar. Mikro bölümlendirme kimliğe duyarlı politika kullanır; müşteri yönetimli anahtarlar ve HSM'ler, saklama ayrımıyla en yüksek güvenceli sistemleri korur. Önleyici korkuluklar yanlış yapılandırmayı dağıtım zamanında engeller, sapma otomatik saptanır ve giderilir ve duruş kanıtı sürekli yetkilendirmeye otomatik beslenir. Güvenlik teslimat ve risk planlamasıyla bütünleşiktir ve kurum, sağlayıcılar, hizmetler ve düzenlemeler değiştikçe kontrolleri düzenli olarak emekliye ayırır ve yeniden kapsamlandırır.

## Tartışma fikirleri

1. Sizin ortamınızda ABAC, karmaşıklığına nerede değer ve RBAC'a yapışmak nerede daha iyidir?
2. Eski otomasyonu bozmadan uzun ömürlü kimlik bilgilerini nasıl ortadan kaldırırsınız?
3. Önleyici korkuluklar ile dedektif duruş yönetimi arasındaki doğru bölüşüm nedir?
4. Operasyonel maliyetleri göz önüne alındığında hangi sistemler müşteri yönetimli anahtarları ya da HSM'leri haklı çıkarır?
5. En az ayrıcalıklı izinlerin sessizce yeniden aşırı ayrıcalığa birikmesini nasıl önlersiniz?
6. Çoklu bulut karmaşıklığı, tutarlı duruş ve politika yaklaşımınızı nasıl değiştirmeli?

## Önemli çıkarımlar

- Kimlik yeni çevredir; kısa ömürlü kimlik bilgileriyle en az ayrıcalıklı IAM'e yatırım yapın.
- Ele geçirilmeyi kapsamak için ağları bölümlendirin ve iş yüklerini mikro bölümlendirin.
- Aktarım sırasında ve beklemede varsayılan olarak şifreleyin ve anahtarları KMS/HSM ve saklama ayrımıyla yönetin.
- Konteynerleri, Kubernetes'i ve sunucusuzu sertleştirin; çalışma zamanlarını ve imajları yamalı tutun.
- Olaydan sonra tespit yerine önleyici korkulukları tercih edin ve duruşu sürekli yönetin.
- Koruma otomatik ölçeklensin diye güvenli varsayılanları yerleşim bölgelerine ve altyapı-koda gömün.
- Bulut ihlallerinin önde gelen nedeni egzotik istismarlar değil yanlış yapılandırmadır ve o önlenebilir.

## Kaynaklar ve ileri okuma

- National Institute of Standards and Technology, *SP 800-207: Zero Trust Architecture*
- Centre for Internet Security, *CIS Benchmarks* (cloud providers, Kubernetes, Docker)
- Cloud Security Alliance, *Cloud Controls Matrix* and *Security Guidance for Cloud Computing*
- NIST, *SP 800-190: Application Container Security Guide*
- Liz Rice, *Container Security*
- Marco Lancini and others, *Cloud security posture and detection* engineering literature
- Provider Well-Architected security pillars (as vendor-neutral architectural guidance)
