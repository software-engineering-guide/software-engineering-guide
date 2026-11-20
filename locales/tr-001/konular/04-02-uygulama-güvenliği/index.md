# 4.2 Uygulama güvenliği

## Genel bakış ve motivasyon

Uygulama güvenliği, soyut tehditlerin somut kodla buluştuğu yerdir. Manşetlere çıkan ihlallerin çoğu uygulama katmanındaki bir kusura dayanır: bir enjeksiyon, bozuk bir kimlik doğrulama akışı, açığa çıkmış bir sır ya da ele geçirilmiş bir bağımlılık. Çok sayıda hizmet sevk eden büyük takımlar için zor olan, bu kusurların var olduğunu bilmek değildir. Zor olan, yıllar içinde binlerce elin yazdığı geniş bir kod tabanında bunları tutarlı biçimde önlemektir.

Kurumlar için uygulama güvenliği, müşteri güveni ve düzenleyici yükümlülük meselesidir. Bir oturum açma akışındaki ya da ödeme yolundaki kusur sahtekârlığı, cezaları ve zorunlu ihlal bildirimini tetikleyebilir. Kamu sistemleri aynı teknik risklerle, daha yüksek bahisli verilerle karşılaşır: yardım uygunluğu, vergi kayıtları, ceza adaleti verileri ve ulusal altyapı. Her iki ortamda da uygulama ön kapıdır ve saldırganlar onu sürekli ve otomatik olarak yoklar.

Bu bölüm, uygulamaları dayanıklı tutan uygulamaları kapsar: yaygın açık sınıflarını bilmek ve onlara karşı savunma yapmak, girdiyi doğrulamak ve çıktıyı kodlamak, kimlik doğrulama ve yetkilendirmeyi doğru yapmak, sırları yönetmek ve gerçek saldırı yüzeyinizi giderek daha fazla belirleyen yazılım tedarik zincirini güvenceye almak.

*Ayrıca bakın:* bölüm 4.1 (güvenlik temelleri, tehdit modelleme ve güvenli geliştirme yaşam döngüsü), bölüm 10.3 (açık kaynak tedarik zinciri ve lisanslama) ve bölüm 10.2 (SBOM'lar, risk ve güvence).

## Temel ilkeler

- **Girdiye asla güvenmeyin.** Bir güven sınırını geçen tüm veriyi, doğrulanana kadar düşmanca kabul edin.
- **Güvenli varsayılanlar.** Güvenli yol kolay yol olmalıdır; güvensiz davranış kasıtlı ve görünür çaba gerektirmelidir.
- **Kapalı kalarak başarısız olun.** Bir güvenlik kontrolü tamamlanamadığında erişime izin vermek yerine reddedin.
- **Uygulama katmanında derinlemesine savunma.** Doğrulamayı, kodlamayı, parametreleştirmeyi ve çerçeve korumalarını birleştirin; birine güvenmeyin.
- **Kimlikler ve belirteçler için en az ayrıcalık.** Kimlik bilgilerini dar kapsamlı tutun ve hızla süresini doldurun.
- **Bağımlılıklarınız sizin kodunuzdur.** Üçüncü taraf ve açık kaynak bileşenler dahil, sevk ettiğiniz her şeyin güvenliğinden siz sorumlusunuz.
- **İmprovizasyon yerine standartlar.** Kendi güvenlik kontrollerinizi icat etmek yerine [OWASP](https://en.wikipedia.org/wiki/OWASP) (Open Worldwide Application Security Project) ASVS gibi denetlenmiş çerçeveleri kullanın.

## Öneriler

### OWASP İlk 10'u bilin ve savunun, ASVS ile doğrulayın

OWASP İlk 10, en kritik web uygulaması risklerinin sektör taban çizgisi listesidir: bozuk erişim denetimi, kriptografik hatalar, enjeksiyon, güvensiz tasarım, güvenlik yanlış yapılandırması, açığı olan bileşenler, kimlik doğrulama hataları, veri bütünlüğü hataları, günlükleme hataları ve sunucu tarafı istek sahteciliği. Onu rafa kaldırılacak bir uyum başvurusu olarak değil, her mühendis için gerekli bilgi olarak ele alın.

Titiz, test edilebilir bir standart için **OWASP Uygulama Güvenliği Doğrulama Standardını (ASVS)** benimseyin. ASVS güvenlik gereksinimlerini üç güvence düzeyinde tanımlar ve size karşısında tasarlayıp test edebileceğiniz somut, denetlenebilir kontroller verir. Her uygulamanın riskine uyan düzeyi seçin ve ona göre doğrulayın.

### Girdiyi doğrulayın ve çıktıyı kodlayın

Enjeksiyon kusurları, tam da eklemesi bu kadar kolay olduğu için en zarar verici olanlar arasında kalır. Katmanlı kontrollerle savunun:

- **Girdiyi** katı izin listelerine (beklenen tür, uzunluk, biçim, aralık) karşı **doğrulayın**. Mümkün olduğunda temizlemek yerine reddedin.
- Tüm veritabanı erişimi için **parametreli sorgular** ve [hazırlanmış ifadeler](https://en.wikipedia.org/wiki/Prepared_statement) kullanın; SQL'i asla dize birleştirmeyle kurmayın. Güvenli sorgu oluşturucuları ve ORM'leri (nesne-ilişkisel eşleyiciler) doğru kullanın.
- Çıktıyı bağlama göre **kodlayın**. HTML, HTML öznitelikleri, JavaScript, URL'ler ve CSS'in her biri farklı kodlama gerektirir. Çerçevenin otomatik kaçışına güvenin ve sınırlarını anlayın.
- İkinci bir katman olarak çıktı kodlaması ile güçlü bir İçerik Güvenliği Politikasını birleştirerek [siteler arası betik çalıştırmayı](https://en.wikipedia.org/wiki/Cross-site_scripting) (XSS) **önleyin**.
- Güvenilmeyen veriyle kabuk komutu çalıştırmaktan kaçınarak ve mantıksız ya da korumalı alanlı şablonlar kullanarak **komut ve şablon enjeksiyonunu önleyin**.

### Kimlik doğrulama ve yetkilendirmeyi doğru yapın

Kimlik doğrulama bir kullanıcının kim olduğunu kanıtlar. Yetkilendirme ne yapabileceğine karar verir. İkisi de sık başarısız olur; bu yüzden onları doğru yapın.

- Yerleşik protokolleri tercih edin: devredilmiş yetkilendirme için **[OAuth 2.0](https://en.wikipedia.org/wiki/OAuth)** ve kimlik doğrulama için **[OpenID Connect](https://en.wikipedia.org/wiki/OpenID_Connect) (OIDC)**. Bunları sıfırdan inşa etmeyin.
- Özellikle ayrıcalıklı ve yönetimsel erişim için **[çok faktörlü kimlik doğrulamayı](https://en.wikipedia.org/wiki/Multi-factor_authentication) (MFA)** zorunlu kılın.
- Parolaları yalnızca modern, yavaş, bellek yoğun bir algoritma ([Argon2](https://en.wikipedia.org/wiki/Argon2) ya da [bcrypt](https://en.wikipedia.org/wiki/Bcrypt) gibi) kullanılarak tuzlanmış özetler olarak saklayın. Düz metin kimlik bilgilerini asla saklamayın ya da günlüğe yazmayın.
- **Oturumları** dikkatle yönetin: kriptografik olarak güçlü belirteçler üretin, secure ve HttpOnly çerez bayraklarını ayarlayın, ayrıcalık değişiminde yenileyin ve boştaki oturumların süresini doldurun.
- **Yetkilendirmeyi her istek için sunucuda** uygulayın ve kimliği doğrulanmış öznenin belirli kaynağa sahip olduğunu ya da erişebileceğini denetleyin. Bozuk nesne düzeyi yetkilendirme (bir kimliği değiştirerek başka bir kullanıcının kaydına erişmek), en yaygın ve en ciddi API kusurlarından biridir.
- Politikanın tutarlı ve denetlenebilir olması için yetkilendirme mantığını uygun olduğu yerde merkezileştirin.

### Sırları yönetin ve anahtarları döndürün

Kaynak koddaki sabit kodlanmış sırlar, ihlallerin daimi bir nedenidir. Sır yönetimi etrafında disiplinli bir alışkanlık geliştirin:

- Sırları, kaynakta, yapılandırma dosyalarında ya da sürüm denetimine işlenmiş ortam değişkenlerinde değil, özel bir sır yöneticisinde ya da kasada saklayın.
- Commit'leri ve depoları sızmış sırlar için otomatik olarak tarayın ve bunları ekleyen birleştirmeleri engelleyin.
- Anahtarları ve kimlik bilgilerini düzenli olarak ve herhangi bir şüpheli açığa çıkmada hemen döndürün. Uzun ömürlü statik kimlik bilgileri yerine kısa ömürlü, otomatik olarak verilen kimlik bilgilerini tercih edin.
- Her sıra en az ayrıcalık uygulayın: tam olarak ihtiyaç duyduğu şeyle kapsamlandırın.
- Sırları beklemede ve aktarım sırasında şifreleyin ve onlara erişimi denetleyin.

### Yazılım tedarik zincirini güvenceye alın

Modern uygulamalar çoğunlukla üçüncü taraf bileşenlerden bir araya getirilir; bu da tedarik zincirini birincil saldırı yüzeyi yapar.

- Tam olarak neyi sevk ettiğinizi bilmek ve yeni bir açık ortaya çıktığında hızla yanıt verebilmek için her uygulama için bir **[Yazılım Malzeme Listesi](https://en.wikipedia.org/wiki/Software_bill_of_materials) (SBOM)** tutun.
- Bağımlılıkları sürekli tarayın (Yazılım Bileşim Analizi ya da SCA) ve bilinen açığı olan bileşenleri hızla giderin.
- Bağımlılık sürümlerini sabitleyin ve doğrulayın; kilit dosyaları ve güvenilir kayıt defterleri kullanın.
- Derleme bütünlüğünü yükseltmek için **SLSA**'yı (Supply-chain Levels for Software Artifacts) benimseyin ve yapıtların nasıl derlendiğini anlatan **kaynak** (provenance) tasdiklerini üretin.
- Çalışanın inşa ettiğiniz şey olduğuna güvenebilmek için dağıtımdan önce **yapıtları imzalayın** ve imzaları doğrulayın.
- Derleme sisteminin kendisini güvenceye alın; ele geçirilmiş bir CI hattı, aşağı akıştaki her tüketiciye kötü amaçlı kod enjekte edebilir.

## Ödünleşimler: artılar ve eksiler

| Karar | Artılar | Eksiler |
|---|---|---|
| Kimlik sağlayıcı satın al/benimse (OIDC) | Savaşta sınanmış, MFA yerleşik, güvence altına alınacak daha az kod | Satıcı bağımlılığı, entegrasyon çabası, maliyet |
| Özel kimlik doğrulama inşa et | Tam denetim, dış bağımlılık yok | Yanlış yapması son derece kolay, yüksek bakım |
| Katı izin listesi doğrulaması | Tüm açık sınıflarını engeller | Meşru uç durumları bozabilir, daha çok peşin iş |
| Kısa ömürlü kimlik bilgileri | Küçük ihlal penceresi, otomatik iptal | Sağlam bir verme altyapısı gerektirir |
| Agresif bağımlılık güncellemeleri | Daha az bilinen açık | Karmaşa, olası kırıcı değişiklikler, test yükü |
| SBOM + imzalama + kaynak | Hızlı olay müdahalesi, doğrulanabilir güven | Araç ve süreç yatırımı, kültürel değişim |

Yinelenen ödünleşim, peşin titizlik ile sürekli maruziyet arasındadır. Özel kimlik doğrulama inşa etmek ya da bağımlılık hijyenini atlamak bugün daha hızlı hissettirir ve sonra size muazzam bedel ödetir. Denetlenmiş standartları ve otomatik tedarik zinciri kontrollerini benimsemek şimdi çaba harcatır, ama sınırsız, öngörülemez bir riski yönetilen, sınırlı bir riske çevirir. Büyük takımlar için en çok otomasyon çarpanı önemlidir: asfalt yol şablonunda bir kez uygulanan bir kontrol, onu kullanan her hizmeti korur.

## Takımınızla tartışılacak sorular

1. **Mühendisler bedavaya alsın diye hangi ASVS kontrollerini asfalt yol çerçevenize gömeceksiniz?** Büyük bir takım için en yüksek kaldıraçlı hamle güvenli yolu varsayılan yapmaktır; böylece paylaşılan bir çerçevede bir kez yazılan kontrol, onu benimseyen her hizmeti korur. Hangi ASVS gereksinimlerinin (parametreli sorgular, çıktı kodlaması, güvenli oturum bayrakları, sunucu tarafı yetkilendirme kontrolleri) her mühendisin hafızasında değil şablonda olması gerektiğine karar verin. Kurumsal ve kamu portföyleri için ayrıca hangi uygulamaların ASVS Düzey 2'ye, hangilerinin Düzey 3'e ihtiyaç duyduğuna karar verin ve bunu her birinin dokunduğu verinin hassasiyetine bağlayın. Hizmetlerinizin bir listesini getirin ve hangilerinin bu varsayılanları zaten miras aldığını, hangilerinin güvenliği elle yeniden uyguladığını işaretleyin; çünkü enjeksiyon ve bozuk erişim denetimi elle yazılmış olanlarda saklanır. Güvenli varsayılanlar yalnızca bir wiki sayfasında yaşıyorsa teslimat baskısı altında atlanacaktır; bu yüzden onları koda koyun.

2. **Yalnızca yeni olanlarda değil, her API'de bozuk nesne düzeyi yetkilendirmeyi nasıl bulup düzelteceksiniz?** Bir kimliği değiştirerek başka bir kullanıcının kaydına erişmek en yaygın ve en ciddi API kusurlarından biridir ve mevcut standartlarınızdan önce yazılmış eski uç noktalarda saklanır. Her istekte ve her nesnede sunucu tarafı yetkilendirme kuraldır, ama zor olan, bunun birçok elin yazdığı, yıllık, geniş bir kod tabanında geçerli olduğunu doğrulamaktır. Yetkilendirme mantığını merkezileştirip merkezileştirmeyeceğinize, kiracılar arası erişimi deneyen otomatik testler ekleyip eklemeyeceğinize ya da önce en yüksek riskli API'lerinizde hedefli test yapıp yapmayacağınıza karar verin. Nesne tanımlayıcıları açığa çıkaran uç noktaların envanterini getirin ve bunları döndürdükleri şeyin hassasiyetine göre sıralayın. Kasıtlı bir tarama olmadan bu kusuru sevk etmeye devam eder ve onu yalnızca bir araştırmacı ya da saldırgan keşfettiğinde fark edersiniz.

3. **Bir sonraki yaygın bağımlılık açığı için planınız nedir: etkilenen her hizmeti ne kadar hızlı bulup yamalayabilirsiniz?** Popüler bir kütüphanede kritik bir kusur ortaya çıktığında, doğru bir SBOM'u olan şirketler etkilenen hizmetleri saatler içinde belirlerken diğerleri haftalarca arar ve bu hız farkı ne kadar zarar göreceğinizi belirler. Her yapıt için bir Yazılım Malzeme Listesi üretip üretmediğinize, bağımlılık taramasının her hatta çalışıp çalışmadığına ve acil yama kararının sahibinin kim olduğuna şimdiden karar verin. Düzenlemeye tabi ve kamu alıcıları için SBOM'lar ve imzalı kaynak bilgisi giderek iş yapmanın bir koşuludur; bu yüzden bu hazırlık geliri de korur. Bir tatbikatın dürüst cevabını getirin: yaygın kullandığınız bir kütüphane seçin ve onu sevk eden her hizmeti listelemenin ne kadar sürdüğünü ölçün. Cevap günlerle ölçülüyorsa, bir sonraki olay sizi zorlamadan önce envantere ve imzalamaya yatırım yapın.

4. **Uzun ömürlü statik sırlardan kısa ömürlü, otomatik verilen kimlik bilgilerine nasıl geçeceksiniz ve bugün hangi sistemler bunu engelliyor?** Sabit kodlanmış ve uzun ömürlü sırlar daimi bir ihlal nedenidir ve çözüm olan, talep üzerine verilen kısa ömürlü kimlik bilgileri, eski sistemlerin çoğu zaman kullanamadığı bir verme altyapısına bağlıdır. Büyük bir takım için tehlike eşitsiz benimsemedir: modern bir platform anahtarları saatlik döndürürken eski bir hizmet hâlâ bir yapılandırma dosyasında statik bir veritabanı parolası sevk eder. Hangi iş yüklerinin bir sır yöneticisini ya da iş yükü kimliği sistemini şimdi kullanabileceğine, hangilerinin önce yatırıma ihtiyaç duyduğuna ve bir anahtarın sızdığından şüphelenildiği anda döndürme çalışma kılavuzunun sahibinin kim olduğuna karar verin. Kullanımdaki her kimlik bilgisinin, ömrünün, açığa çıkarsa patlama yarıçapının ve commit taramasının onu birleştirmeden önce yakalayıp yakalamayacağının envanterini getirin. Kurumsal ve kamu ortamlarında bunu denetime bağlayın: denetçiler her sır için döndürme, kapsamlı erişim ve erişim günlüğü kanıtı beklemektedir ve kesinti olmadan döndüremeyeceğiniz statik bir kimlik bilgisi, yazılmayı bekleyen bir bulgudur.

5. **Hâlâ nerede ev yapımı ya da tutarsız kimlik doğrulama çalıştırıyorsunuz ve denetlenmiş protokoller üzerinde birleşme planı nedir?** Kimlik doğrulama inşa etmek, ince, istismar edilebilir kusurlar eklemenin en kolay yollarından biridir; yine de çoğu büyük envanter, OAuth 2.0 ve OIDC üzerinde standartlaşma kararından önceye dayanan en az bir eski oturum açma akışı taşır. Rakip baskılar gerçektir: eski bir akışı taşımak mevcut kullanıcıları ve entegrasyonları bozma riski taşırken, onu yerinde bırakmak yüksek değerli bir hedefi yetersiz savunulmuş tutar. Tek bir kimlik sağlayıcı üzerinde birleşip birleşmeyeceğinize, MFA'yı tekdüze zorunlu kılıp kılmayacağınıza ve her özel akışı emekliye ayırmak için bir son tarih koyup koymayacağınıza ya da telafi edici kontrollerle belgelenmiş istisnaları kabul edip etmeyeceğinize karar verin. Filodaki her kimlik doğrulama yolunun, hangilerinin MFA uyguladığının, hangilerinin parolaları modern bir bellek yoğun özetle sakladığının ve hangilerinin özel olduğunun bir haritasını getirin. Kurumsal ve kamu portföyleri için uyum açısını ekleyin: NIST SP 800-63 gibi standartlar kimlik güvencesi için somut beklentiler koyar ve bunları gösteremeyen ev yapımı bir akış bir denetimden ya da işletme yetkisi incelemesinden sağ çıkamaz.

6. **Bu kontrollerin üretimde gerçekten geçerli olduğunu nasıl doğruluyorsunuz ve bunu iddia yerine kanıtla ispatlayabiliyor musunuz?** Güvenli bir varsayılan yazmak, her hizmetin hâlâ ona uyduğunu bilmekle aynı şey değildir; kod değiştikçe, istisnalar biriktikçe ve yeni uç noktalar sevk edildikçe kontroller sessizce çürür. Büyük bir takım için soru kapsamdır: hangi hizmetler statik analiz, bağımlılık taraması ve dinamik ya da sızma testi çalıştırıyor ve bunları atlayanların en yüksek riskli uygulamalarınız olmadığını nasıl biliyorsunuz? Hatta hangi doğrulamanın zorunlu, hangisinin dönemsel olduğuna, bulguları kimin önceliklendireceğine ve bir kontrolün belirli bir tarihte test edildiğini ve geçtiğini göstermek için hangi kanıtı sakladığınıza karar verin. Mevcut kapsam haritanızı, önem düzeyine göre ortalama giderme sürenizi ve yakın zamanda testi olmayan uygulamaların listesini getirin. Düzenlemeye tabi ve kamu bağlamlarında bu kanıt isteğe bağlı değildir: denetçiler, yetkilendirme görevlileri ve ihlal soruşturmacıları kontrollerin doğrulandığına dair kanıt ister ve test kaydı olmayan bir politika onları nadiren tatmin eder.

## Sektör merceği

**Girişim.** İki ya da üç mühendisle ve güvenlik uzmanı olmadan kaldıraç noktanız güvenliği inşa etmek yerine miras almaktır: yönetilen bir OIDC kimlik sağlayıcısı benimseyin, ORM'i sorguları varsayılan olarak parametreleştiren bir çerçeveye yaslanın ve sırları, bir takım arkadaşının kazara commit edebileceği `.env` dosyaları yerine platformunuzun sır yöneticisinde tutun. Yama pull request'leri açan otomatik bağımlılık taramasını açın ve şimdilik bunu yeterli sayın. Özel kimlik doğrulama ya da kriptografi inşa etmeyin, çünkü enjekte edilmiş tek bir sorgu ya da sızmış tek bir anahtar, şirket daha müşteri bulmadan onu bitirebilir.

**Küçük işletme.** Büyük olasılıkla bir uygulama güvenliği uzmanınız ve dar bir bütçeniz var; bu yüzden özel bir işlev için kadro çıkarmak yerine zaten ödediğiniz araç ve platformlara gömülü kontrolleri satın alın. MFA'nın dahil olduğu barındırılan bir kimlik sağlayıcı, sizi parametreli erişime yönlendiren yönetilen bir veritabanı ve commit'leri kutudan çıkar çıkmaz sızmış sırlar için tarayan bir depo sağlayıcısı seçin. Kıt dikkatinizi gerçek dünyadaki ihlallerin çoğuna yol açan OWASP İlk 10 temellerine yoğunlaştırın ve rastgele kapatamayacağınız güvenli varsayılanlar sevk eden satıcıları tercih edin.

**Kurumsal.** Birçok takım arasında zorluk tutarlılıktır: ASVS kontrollerini asfalt yol çerçevelerine gömün ki her yeni hizmet parametreli sorguları, çıktı kodlamasını, güvenli oturumları ve sunucu tarafı yetkilendirmeyi bedavaya miras alsın. Bir sonraki yaygın kütüphane açığının haftalar değil saatler meselesi olması için doğru SBOM'lar ve filo çapında bağımlılık taraması çalıştırın ve kiracılar arası erişimin test edilebilir olması için yetkilendirme politikasını merkezileştirin. MFA'nın zorunlu kılındığı tek bir kimlik sağlayıcıda standartlaşın ve uygulama güvenliğini riske göre katmanlanmış ASVS düzeyleri ve denetlenmiş kanıtla yönetilen bir portföy olarak yönetin.

**Kamu.** Tedarik kuralları, şeffaflık ve kamusal hesap verebilirlik, yalnızca uygulamanız gereken değil gösterebilmeniz gereken kontrolleri şekillendirir. Vatandaşa dönük hizmetleri veri hassasiyetine uygun bir düzeyde OWASP ASVS'ye karşı doğrulayın, tedarik zinciri yetkilerini karşılamak için dağıtılan her yapıtı imzalayın ve kaynağını SLSA'ya göre tasdik edin ve merkezi bir kasadan tam erişim günlüğüyle kısa ömürlü kimlik bilgileri verin. Denetçilere ve yetkilendirme görevlilerine kaynaktan üretime belgelenmiş bir gözetim zinciri göstermeyi ve kimlik güvencesini NIST SP 800-63 gibi yayımlanmış standartlarla hizalamayı bekleyin.

## Örnekler

**Girişim.** Üç mühendisli bir SaaS takımı kendi oturum açma sistemini kurmayı atlar ve ilk günden yönetilen bir OIDC sağlayıcısı benimser; yanlış yapmayı göze alamayacağı güvenlik açısından kritik kod yazmadan MFA ve güvenli parola sıfırlama kazanır. Sorguların varsayılan olarak parametreli olması için çerçevenin ORM'ine güvenir, sırları bir takım arkadaşının kazara commit edebileceği `.env` dosyalarında değil platformun sır yöneticisinde tutar ve bir kütüphanenin yamaya ihtiyacı olduğunda pull request açan otomatik bağımlılık taramasını açar. Bunların hiçbiri takımı yavaşlatmaz ve bu, sızmış tek bir anahtarın ya da enjekte edilmiş tek bir sorgunun şirketi daha müşteri bulamadan bitirmediği anlamına gelir.

**Kurumsal.** On milyonlarca alışverişçiye hizmet veren bir perakende platformu, kimlik doğrulamayı tek bir kimlik sağlayıcı üzerinden OIDC'de standartlaştırır; personel için MFA ve yüksek değerli hesap değişiklikleri için kademeli doğrulama uygular. Tüm veritabanı erişimi, sorguları parametreleştirecek biçimde yapılandırılmış bir ORM üzerinden geçer ve bir İçerik Güvenliği Politikası çıktı kodlamasını destekler. Popüler bir günlükleme kütüphanesindeki geniş çapta duyurulan bir açığın ardından şirketin SBOM'u etkilenen her hizmeti saatler içinde belirlemesini ve iki günde yamalamasını sağlarken, envanteri olmayan rakipler haftalarca aradı.

**Kamu.** Federal bir yardım kurumu, vatandaşa dönük hizmetleri OWASP ASVS Düzey 2'ye karşı doğrulanmış olarak inşa eder; en hassas kayıtları işleyen bileşenler için Düzey 3 kullanır. Sırlar, kısa ömürlü kimlik bilgileri veren merkezi bir kasada yaşar; commit taraması sızmış her anahtarı engeller. Dağıtılan her yapıt imzalanır ve kaynağı SLSA'ya göre tasdik edilir; bu, doğrulanabilir yazılım tedarik zincirleri için bir federal yetkiyi karşılar ve denetçilere kaynaktan üretime net bir gözetim zinciri sağlar.

## İş gerekçesi: motivasyonlar, YG ve TSM

Uygulama güvenliği harcaması, ihlallerin en olası ve en pahalı kategorisinin bedelini düşürür. Toplam sahip olma maliyeti; araçları (tarayıcılar, sır yöneticileri, kimlik sağlayıcılar), bulguları gidermek için mühendis zamanını ve güvenli varsayılanların hafif sürtünmesini içerir. Buna karşın, atlamanın maliyetini tartın: enjeksiyon ve bozuk erişim denetimi ihlalleri düzenli olarak milyonlarca kaydı açığa çıkarır; düzenleyici cezaları, zorunlu bildirimi, sahtekârlık kayıplarını, giderme sprintlerini ve yıllarca geliri baskılayan itibar zararını tetikler.

YG, kontroller otomatik ve yeniden kullanılabilir olduğunda en güçlüdür. İyi yapılandırılmış tek bir kimlik entegrasyonu, paylaşılan bir çerçevedeki tek bir sertleştirilmiş sorgu katmanı ve açığı olan bağımlılıkları engelleyen tek bir hat, tüm filoyu hizmet başına marjinal maliyetle korur. Özellikle tedarik zinciri kontrolleri isteğe bağlıdan vazgeçilmeze geldi: ele geçirilmiş bir bağımlılık her müşterinizi bir kurbana çevirebilir ve düzenleyiciler ile kurumsal alıcılar giderek SBOM'ları ve imzalı kaynak bilgisini iş yapmanın koşulu olarak talep ediyor. Liderliğe gerekçeyi sunarken yatırımı belirli, adlandırılmış risklere ve karşılamazsanız geliri engelleyen tedarik ve uyum gereksinimlerine bağlayın.

## Anti-kalıplar ve tuzaklar

- **Kendi kriptografinizi ya da kimlik doğrulamanızı yazmak.** Hemen her zaman ince, istismar edilebilir kusurlar üretir.
- **Yalnızca istemci tarafı doğrulama.** Çok kolay atlanır; sunucu her şeyi yeniden doğrulamalıdır.
- **Engelleme listesiyle temizleme.** İyi karakterleri izin listesine almak yerine "kötü" karakterleri ayıklamaya çalışmak; saldırganlar boşlukları bulur.
- **Kaynakta ya da ortam dosyalarında sırlar.** Kimlik bilgisi sızıntılarının en yaygın tek nedeni.
- **Nesne erişiminde yetkilendirmeyi görmezden gelmek.** Kimliği doğrulanmış bir kullanıcının, kimliğini tahmin edebildiği her nesneye erişebileceğini varsaymak.
- **Ayarla ve unut bağımlılıklar.** Bir ihlal zorlayana kadar üçüncü taraf bileşenleri asla güncellememek.
- **İlk 10'u bitiş çizgisi saymak.** O bir zemindir, kapsamlı bir standart değil; derinlik için ASVS kullanın.
- **Hassas veriyi günlüğe yazmak.** Günlüklerdeki parolalar, belirteçler ve KTB (kişisel olarak tanımlanabilir bilgi), olmayı bekleyen bir ihlale dönüşür.

## Olgunluk modeli

**Düzey 1, Başlangıç.** Uygulama güvenliği bireysel geliştirici bilgisine bağlıdır ve yalnızca olaylardan sonra tepki verir. Standart kontrol yoktur. Sırlar kaynaktadır. Bağımlılıklar nadiren güncellenir. Kimlik doğrulama özel ve geçicidir; enjeksiyon ya da bozuk erişim denetimi kusurları süreçle değil şansla bulunur.

**Düzey 2, Geliştirme.** Temel uygulamalar ortaya çıkar ama takımdan takıma değişir. OWASP İlk 10 farkındalığı yayılır, bazı çerçeve düzeyi korumalar yerindedir ve bir sır yöneticisi vardır ama eşitsiz kullanılır. Bağımlılık taraması ara sıra çalışır. Yeni sistemler standart bir kimlik sağlayıcıyı benimserken eski hizmetler ev yapımı oturum açma akışlarını olduğu gibi tutar.

**Düzey 3, Standartlaştırma.** Kontroller kurum genelinde belgelenmiş ve zorunlu kılınmıştır. ASVS tabanlı gereksinimler risk katmanına göre belirlenir, parametreli sorgular ve çıktı kodlaması norm haline gelir ve MFA'lı merkezi bir kimlik sağlayıcı zorunludur. Sırlar otomatik yönetilir ve taranır, SBOM'lar üretilir ve bağımlılık taraması her hatta çalışır.

**Düzey 4, Yönetme.** Uygulama ölçülür ve taban çizgilerine göre kontrol edilir. Tarama ve test kapsamı, önem düzeyine göre ortalama giderme süresi, asfalt yol varsayılanlarını miras alan hizmetlerin payı, kimlik bilgisi ve sır döndürme yaşı ve ASVS uyumu panolarda izlenir. İstisnalar sona erme tarihleriyle kaydedilir, taban çizgisinden sapma eylemi tetikler ve yayınlar yargı kararlarına değil tanımlı güvenlik eşiklerine bağlanır.

**Düzey 5, Orkestrasyon.** Güvenlik sürekli iyileştirilir ve kurum genelinde bütünleşiktir. Güvenli varsayılanlar asfalt yol çerçevelerine gömülüdür, böylece güvenli yol otomatiktir; her yerde kısa ömürlü kimlik bilgileri kullanılır ve imzalama ile kaynak bilgisini (SLSA) içeren tam tedarik zinciri güvencesi standarttır. Doğrulama süreklidir, yeni açıklara yanıt hızlı ve ölçülüdür ve her olay paylaşılan şablonlara geri beslenir; böylece tek bir düzeltme tüm filoyu sertleştirir.

## Tartışma fikirleri

1. Yetkilendirme mantığı, birçok hizmet arasında hem tutarlı hem bakımı yapılabilir olması için nerede yaşamalı?
2. Maruziyet ile karmaşa arasındaki ödünleşim göz önüne alındığında bağımlılıkları ne kadar agresif güncellemelisiniz?
3. Portföyünüzdeki her uygulama sınıfı için hangi ASVS düzeyi uygundur?
4. Kırılgan verme altyapısı yaratmadan uzun ömürlü sırları nasıl ortadan kaldırırsınız?
5. Kurumunuzun her yapıt için SBOM ve kaynak bilgisi üretmesi ve tüketmesi için ne gerekir?
6. Güvenli varsayılanların teslimat baskısı altında kapatılmasını nasıl önlersiniz?

## Önemli çıkarımlar

- OWASP İlk 10 temel bilgidir; ASVS test edilebilir standardı sağlar.
- Enjeksiyonu ve XSS'i yenmek için girdi doğrulamayı, parametreleştirmeyi ve çıktı kodlamasını katmanlayın.
- Denetlenmiş protokolleri (OAuth 2.0, OIDC) kullanın ve MFA'yı zorunlu kılın; kimlik doğrulamayı asla sıfırdan inşa etmeyin.
- Yetkilendirmeyi her istek ve her nesne için sunucu tarafında uygulayın.
- Sırları kaynaktan uzak tutun, merkezi yönetin ve kısa ömürlü kimlik bilgilerine döndürün.
- Tedarik zinciri birincil saldırı yüzeyidir; SBOM, SCA, imzalama ve kaynak bilgisi (SLSA) kullanın.
- Otomatik, yeniden kullanılabilir kontroller tüm filoyu hizmet başına marjinal maliyetle korur.

## Kaynaklar ve ileri okuma

- OWASP, *Top 10 Web Application Security Risks*
- OWASP, *Application Security Verification Standard (ASVS)*
- OWASP, *Cheat Sheet Series* (Input Validation, Authentication, Authorisation, Secrets Management)
- Dafydd Stuttard and Marcus Pinto, *The Web Application Hacker's Handbook*
- Aaron Parecki, *OAuth 2.0 Simplified*
- National Institute of Standards and Technology, *SP 800-63: Digital Identity Guidelines*
- Cloud Native Computing Foundation and OpenSSF, *SLSA framework* and *Supply-chain Security guidance*
