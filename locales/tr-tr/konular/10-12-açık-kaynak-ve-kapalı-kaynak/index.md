# 10.12 Açık kaynak ve kapalı kaynak

## Genel bakış ve motivasyon

Hemen her modern sistem, sizin yazdığınız, satın aldığınız ve bedavaya aldığınız yazılımın bir karışımıdır. Bu üç türden ikisi temel bir seçimle gelir: yazılım **açık kaynak** mı yoksa **kapalı kaynak** mı? **[Açık kaynak yazılım](https://en.wikipedia.org/wiki/Open-source_software) (AKY)**, kaynak kodunu, yani programı tanımlayan insan tarafından okunabilir yönergeleri, herkesin kullanma, inceleme, değiştirme ve yeniden dağıtma hakkını veren bir lisansla dağıtılır. **[Tescilli yazılım](https://en.wikipedia.org/wiki/Proprietary_software)** olarak da adlandırılan **kapalı kaynak yazılım**, kaynak kodunu tedarikçinin gizli tuttuğu bitmiş bir ürün olarak dağıtılır. Onu bir lisans altında çalıştırma hakkını alırsınız, ama nasıl çalıştığını inceleme ya da değiştirme hakkını almazsınız. Orta bir kategori olan **[kaynağı erişilebilir yazılım](https://en.wikipedia.org/wiki/Source-available_software)**, kaynağı okunmak üzere yayımlar ama kullanımı, değiştirilmesini ya da yeniden dağıtımı kısıtlar. Standart tanıma göre *görünürdür* ama *açık* değildir.

Karşılaştırmadan önce iki açıklama önemlidir. Birincisi, "özgür" belirsiz bir sözcüktür. Topluluk **özgürlük anlamında özgür** (değiştirme ve paylaşma serbestliği, bazen "libre" diye yazılır) ile **fiyat anlamında özgür** (sıfır maliyet, "gratis") arasında ayrım yapar. Açık kaynak özgürlükle ilgilidir, fiyatla zorunlu olarak değil. İkincisi, açık kaynak lisansları iki aileye ayrılır. **[Serbest (permissive) lisanslar](https://en.wikipedia.org/wiki/Permissive_software_license)** ([MIT](https://en.wikipedia.org/wiki/MIT_License), BSD ve Apache 2.0 gibi) kodu kapalı bir ürüne gömmek dahil hemen her şeyi yapmanıza izin verir. **[Copyleft](https://en.wikipedia.org/wiki/Copyleft) lisansları** ([GNU Genel Kamu Lisansı](https://en.wikipedia.org/wiki/GNU_General_Public_License), GPL gibi), dağıttığınız türev eserlerin de aynı açık koşullar altında yayımlanmasını şart koşar; eleştirmenlerin bazen "bulaşıcı", savunucularının "aynı koşullarla paylaş" dediği bir karşılıklılık kuralıdır.

Bu bölüm seçime iki taraftan bakar. Bir **tüketici** olarak açık kaynak mı yoksa tescilli bir bileşen mi benimseyeceğinize karar verirsiniz. Bir **üretici** olarak inşa ettiğiniz yazılımı açık kaynak yapıp yapmayacağınıza karar verirsiniz. Büyük kurumsal yapılar ve özellikle kamu için her iki karar da lisans dosyasının çok ötesinde ağırlık taşır. Satın alma (bölüm 10.3), dijital egemenlik (bölüm 10.11), tedarik zinciri güvenliği (bölüm 4.2), birlikte çalışabilirlik (bölüm 3.8) ve inşa-ya-da-satın-al hesabına (bölüm 6.1) dokunurlar.

## Temel ilkeler

- **"Açık"ı fiyat değil, lisans tanımlar.** Lisansı okuyun; bedava olmak ile açık kaynak olmak farklı iddialardır.
- **Hiçbir model doğası gereği daha güvenli değildir.** İkisi de mükemmel ya da ihmalkâr olabilir; kodun etrafındaki uygulamalar, açıklığından daha önemlidir.
- **Açıklık bir bağımlılık azaltma kaldıracıdır.** Kaynağa erişim, [tedarikçi kilitlenmesine](https://en.wikipedia.org/wiki/Vendor_lock-in) karşı nihai korumadır.
- **Operasyonel yük her zaman sizindir.** Edinmesi bedava olan, çalıştırması hiçbir zaman bedava değildir; gerçek hikâyeyi [toplam sahip olma maliyeti](https://en.wikipedia.org/wiki/Total_cost_of_ownership) anlatır.
- **Ayırt ediciler kapalı kalır; olağan olanlar açılabilir.** Sizi ayırt etmeyeni açık kaynak yapın; ayırt edeni koruyun.
- **Copyleft'in sonuçları vardır.** Dağıttığınız bir ürüne copyleft kodu gömmeden önce karşılıklılık yükümlülüklerini anlayın.
- **Canlı bir topluluk bir varlıktır; terk edilmiş bir depo bir yükümlülüktür.** Yalnızca lisansı değil, projeyi yargılayın.

## Öneriler

### Bir bileşeni yalnızca lisansa göre değil, projeye göre değerlendirin

Herhangi bir bağımlılığı, açık kaynak ya da tescilli, benimsemeden önce sağlığını değerlendirin: sürüm temposu, bakımcıların sayısı ve çeşitliliği, güvenlik raporlarına yanıt verme hızı ve benimsenmenin genişliği. Tek bakımcılı bir açık kaynak kütüphane ile küçük bir tescilli tedarikçi aynı **otobüs faktörü riskini** (bir ya da birkaç kilit kişi ayrılırsa projenin çökme tehlikesi) taşır. Geniş bir katkıcı tabanı ya da mali açıdan sağlam bir tedarikçisi olan bileşenleri tercih edin ve değerlendirmeyi durum tespitinin bir parçası olarak kaydedin (bölüm 10.2, 4.2).

### Lisansları birinci sınıf bir yükümlülük olarak okuyun ve izleyin

Her bileşenin ve lisansının bir envanterini tutun ve hangi lisans ailelerinin hangi kullanımlar için kabul edilebilir olduğuna dair bir politika uygulayın. Kritik ayrım copyleft'tir. **Serbest** kod (MIT, Apache 2.0) genellikle kapalı ürünlere özgürce gömülebilir. **Güçlü copyleft** (GPL), dağıtılan türev eserinizi aynı koşullarla yayımlamanızı gerektirebilir. Bağımlılıklarınızı tarayarak bileşenleri, lisansları ve bilinen güvenlik açıklarını belirleyen araçlar olan otomatik **yazılım bileşen analizi (YBA)** kullanın ve bir üründeki her bileşenin resmî bir listesi olan **yazılım malzeme listesi (YML)** üretin (bölüm 10.3, 4.2).

### Güvenliği açıklığa göre değil, uygulamaya göre yargılayın

**"Çok göz" argümanı** ([Linus Yasası](https://en.wikipedia.org/wiki/Linus%27s_law): "yeterince göz olursa tüm hatalar sığdır") yüzünden açık kaynağın güvenli olduğunu varsaymayın. Ve tescilli kodun **[gizlilik yoluyla güvenlik](https://en.wikipedia.org/wiki/Security_through_obscurity)** (kaynağı gizlemenin kusurları gizlediği yönündeki hatalı inanç) sayesinde güvenli olduğunu da varsaymayın. Çok göz yalnızca nitelikli insanlar gerçekten baktığında işe yarar ve yaygın kullanılan birçok proje zayıf biçimde bakım görür. İki model de **tedarik zinciri riski** taşır: açık kaynak ele geçirilmiş ya da terk edilmiş bağımlılıklar yoluyla, tescilli ise inceleyemeyeceğiniz opak kod ve güncelleme kanalları yoluyla. Modelden bağımsız olarak sürümleri sabitleyin, kaynağı doğrulayın, sürekli tarayın ve duyuruları izleyin (bölüm 4.2).

### Çıkış ve birlikte çalışabilirlik için tasarlayın

Daha sonra değiştirebilmeniz için açık standartlar ve taşınabilir veri biçimleri konuşan bileşenleri tercih edin (bölüm 3.8, 10.11). Açık kaynakla nihai çıkışı elde edersiniz: bir proje durursa onu **[çatallayabilirsiniz](https://en.wikipedia.org/wiki/Fork_(software_development))** (kendi kopyanızı oluşturup sürdürebilirsiniz). Tescilli yazılımla korumaları baştan müzakere edin: açık biçimlerde veri dışa aktarma, belgelenmiş API'ler ve **[kaynak kodu emaneti](https://en.wikipedia.org/wiki/Source_code_escrow)** (tedarikçinin kaynağı bir üçüncü tarafa yatırdığı ve tedarikçi başarısız olursa size teslim edilen hukuki bir düzenleme). Hiçbir tekil bileşenin, iki türden hiçbirinin sisteminizi rehin alamayacağı biçimde tasarlayın.

### Etiket fiyatını değil, toplam sahip olma maliyetini tartın

Seçenekleri yalnızca lisans ücretlerine göre değil, edinme, entegrasyon, işletme, destek, eğitim, yükseltme ve nihai değiştirmeyi içeren tam ömür boyu maliyet olan **toplam sahip olma maliyeti (TSM)** üzerinden karşılaştırın. Açık kaynak çoğu zaman lisans maliyetini daha yüksek işletme ve personel maliyetiyle takas eder. Tescilli yazılım çoğu zaman öngörülebilir abonelik ücretlerini kilitlenme ve daha az denetimle takas eder. Modelin kendisinin maliyetini de ekleyin: kendi kendini destekleyen açık kaynak kurum içi beceri gerektirir, tescilli yazılım ise tedarikçi yönetimi kapasitesi gerektirir.

### Üretici olarak, sizi ayırt etmeyeni açık kaynak yapın

Kendi yazılımınızı rekabet ya da misyon avantajı sağlayan ile ayırt edici olmayan tesisat işi olarak sınıflandırın. Ayırt edicileri tescilli tutun. Bir topluluğun bakımı ve iyileştirmeyi paylaşabileceği olağan altyapıyı açık kaynak yapmayı düşünün. Kamu için **"kamu parası, kamu kodu"** ilkesini (vergi mükellefleri tarafından fonlanan yazılımın varsayılan olarak kamuya açık olması gerektiği ilkesi) şeffaflığın, yeniden kullanımın ve egemenliğin itici gücü olarak tartın (bölüm 10.5, 10.11). Lisansı bilinçle seçin: benimsemeyi azamileştirmek için serbest, ekosistemi açık tutmak için copyleft.

## Ödünleşimler: artılar ve eksiler

| Boyut | Açık kaynak | Kapalı / tescilli |
|---|---|---|
| **Edinme maliyeti** | Genellikle edinmesi sıfır | Lisans ya da abonelik ücreti |
| **Toplam sahip olma maliyeti** | Maliyet operasyonlara ve personele kayar | Daha öngörülebilir, ama kilitlenme primi |
| **Denetim ve özelleştirme** | Tam: kaynağı okuyabilir ve değiştirebilirsiniz | Tedarikçinin açtığıyla sınırlı |
| **Destek ve hesap verebilirlik** | Topluluk ya da ücretli üçüncü taraf; tek bir sorumlu muhatap yok | Sözleşmeli destek ve net bir hesap verebilir taraf |
| **Güvenlik duruşu** | Denetlenebilir; gerçekten bakım görüyorsa "çok göz" | Tedarikçi tarafından yönetilir; opak; gizlilik koruma değildir |
| **Ömür / terk edilme** | Bakım görüyorsa çatallanabilir; yine de solabilir | Tedarikçinin sürdürülebilirliğine ve yol haritasına bağlı |
| **Tedarikçi kilitlenmesi** | Düşük: kaynak ve açık biçimler çıkışı mümkün kılar | Standartlar ve emanetle hafifletilmedikçe yüksek |
| **Ekosistem** | Açık topluluk ve birlikte çalışabilirlik | Derlenmiş, bütünleşik, bazen duvarlı |

Süregelen gerilim **denetim ile kolaylık ve hesap verebilirlik** arasındadır. Açık kaynak denetimi, denetlenebilirliği ve kilitlenmeden özgürlüğü azamileştirir, ama yeteneği, entegrasyonu ve desteği sizin sağlamanızı ister. Tescilli yazılım, zorlayabileceğiniz bir sözleşmesi olan destekli, bütünleşik, hesap verebilir bir ürün sunar, ama denetimden vazgeçer ve kilitlenmeyi davet eder. Çözüm nadiren ya hep ya hiçtir. Çoğu olgun yapı, destek, hesap verebilirlik ya da özel yeteneğin ödünleşimi haklı çıkardığı yerlerde açık kaynak temelleri tescilli sistemlerle karıştırır.

## Takımınızla tartışılacak sorular

1. **Hattımızda otomatik YBA ve YML'lerle bir lisans politikası uyguluyor muyuz, özellikle güçlü copyleft'i gönderilmeden yakalamak için?** Dağıtılan tescilli bir ürüne GPL bir kütüphane gömmek, kendi kaynağınızı yayımlamanızı gerektirebilir ve bu sürpriz genellikle geç, geri almanın pahalı olduğu bir anda ortaya çıkar. Her bileşenin ve lisansının bir envanterini tutun, hangi lisans ailelerinin hangi kullanımlar için kabul edilebilir olduğunu uygulayın ve yazılım bileşen analizini otomatik çalıştırın; böylece ihlalleri bir avukat gönderim anında değil, hat engellesin. YML'yi olağan bir iş olarak üretin. Büyük ya da kamusal bir yapı için bu aynı zamanda tedarik zinciri hijyenidir ve çoğu zaman bir satın alma gereksinimidir. Mevcut lisans envanterinizi ya da envanterinizin olmadığı gerçeğini getirin ve politikanın sahibini belirleyin.

2. **Bir bağımlılığı benimserken, durum tespiti olarak proje sağlığını ve otobüs faktörünü değerlendiriyor muyuz?** Tek bakımcılı bir açık kaynak kütüphane ile küçük bir tescilli tedarikçi aynı riski taşır: bir ya da birkaç kilit kişi ayrılırsa proje çöker. Herhangi bir şeyi benimsemeden önce sürüm temposunu, bakımcıların sayısını ve çeşitliliğini, güvenlik raporlarına yanıt verme hızını ve benimsenmenin genişliğini değerlendirin ve değerlendirmeyi kaydedin. Hiçbir model varsayılan olarak daha güvenli değildir; "çok göz" yalnızca nitelikli insanlar gerçekten baktığında işe yarar ve yaygın kullanılan birçok proje zayıf biçimde bakım görür. Ürününüzün en çok dayandığı üç ya da dört bağımlılığı getirin ve her biri için, sorun sizin olmadan önce kaç kişinin işi bırakması gerektiğini sorun. Yanıtlayamıyorsanız, kendinize borçlu olduğunuz değerlendirme budur.

3. **Tescilli satın alırken çıkış korumalarını baştan güvence altına alıyor muyuz?** Tescilli yazılım denetim karşılığında hesap verebilirlik ve kolaylık sunar ve gizli maliyet kilitlenmedir: geçiş maliyetleri, bir tedarikçinin fiyatları artırmasına ya da hizmeti çok az başvuru yoluyla bozmasına izin verir. Korumaları imzalamadan önce, hâlâ koz elinizdeyken müzakere edin: açık biçimlerde veri dışa aktarma, belgelenmiş API'ler ve tedarikçi başarısız olursa kaynağı serbest bırakan kaynak kodu emaneti. Açık kaynakla çıkışınız çatallama yeteneğidir; tescilliyle çıkışı sözleşmeye yazmalısınız. En kritik tescilli sistemlerinizi getirin ve tedarikçi fiyatı ikiye katlarsa ya da batarsa gerçekte ne olacağını sorun. Yanıt "sıkıştık" ise, yenilemede sözleşmeyi düzeltin.

4. **Kendimiz inşa ettiğimiz yazılım için neyin açık kaynak yapılacağına, neyin kapalı tutulacağına nasıl karar veriyoruz ve bu kararı verme yetkisi kimde?** Bunu bir yönde yanlış yaparsanız sizi ayırt eden kodu bedavaya verirsiniz; diğer yönde yanlış yaparsanız bakımını bir topluluğun seve seve paylaşacağı olağan tesisatı biriktirirsiniz. Karşıt baskılar gerçektir: mühendisler kamuya açık bir deponun işe alım ve itibar avantajını ister, ürün ve hukuk ise rakiplere avantaj vermekten ya da güvenlik açısından duyarlı bir sezgisel yöntemi açığa çıkarmaktan endişe eder. Sistemlerinizin misyonu ayırt eden ile ayırt edici olmayan altyapı olarak dürüst bir sınıflandırmasını getirin ve bir yayını onaylayan kişiyi ya da kurulu adlandırın; çünkü depoyu kim yüklediyse onun verdiği ad hoc bir karar, taç mücevherlerinin sızma biçimidir. Büyük bir kurumsal yapı için soru portföy stratejisidir, kamu için ise vergi mükellefi tarafından fonlanan yazılımın varsayılan olarak kamuya açık olması ilkesi olan "kamu parası, kamu kodu" ile çarpışır; bu yüzden hangi istisnaların (ulusal güvenlik, dolandırıcılık tespiti, kişisel veri) kodun kapalı tutulmasını haklı çıkaracağına önceden karar verin.

5. **İnşa-ya-da-satın-al karşılaştırmalarımız tam toplam sahip olma maliyetini yakalıyor mu, yoksa sıfır lisans ücretini hâlâ sıfır maliyet olarak mı görüyoruz?** Açık kaynakla en yaygın finansal hata, "edinmesi bedava"yı "çalıştırması bedava" diye okumak, sonra entegrasyonun, operasyonların, güvenlik müdahalesinin ve ücretli desteğin kaçındığınız herhangi bir lisansı gölgede bıraktığını keşfetmektir. Gerilim şudur: tescilli bir abonelik faturada pahalı görünürken bir kilitlenme primini gizler, açık bir bileşen faturada bedava görünürken maliyeti kendi personelinize kaydırır. İki ya da üç gerçek karar için birebir karşılaştırılabilir bir TSM modeli getirin: edinme, entegrasyon, işletme, destek, eğitim, yükseltme, güvenlik müdahalesi ve nihai değiştirme; ilk yıl yerine tam ömür boyunca fiyatlanmış. Kurumsal ya da kamusal bir yapıda, işletim modelinin kendisinin maliyetini ekleyin; çünkü kendi kendini destekleyen açık kaynak, işe almanız ve elinizde tutmanız gereken kurum içi beceri gerektirir; bu kalemleri atlayan bir karşılaştırmayı analiz değil, kanıt olarak değerlendirin.

6. **Bir bileşenin güvenliğini uygulamalarına göre mi yargılıyoruz, yoksa açıklık etiketine, ister "çok göz" ister kapalı kodun gizliliği olsun, mi yaslanıyoruz?** İki varsayılan da tuzaktır: "çok göz" yalnızca nitelikli insanlar kodu gerçekten gözden geçirdiğinde sizi korur ve yaygın kullanılan birçok açık proje tükenmiş tek bir bakımcıyla yürür; saldırganların görmemesine dayanan kapalı kaynak ise bir denetim değil, gizlilik yoluyla güvenliktir. Tartışma önemlidir çünkü kıt güvenlik çabanızı nereye harcayacağınızı değiştirir ve dürüst yanıt, iki modelin de tedarik zinciri riski taşıdığıdır: açık kaynak ele geçirilmiş ya da terk edilmiş bağımlılıklar yoluyla, tescilli ise inceleyemeyeceğiniz opak güncelleme kanalları yoluyla. En kritik bileşenleriniz için kanıt getirin: bunları gerçekte kim gözden geçiriyor, duyurular ne kadar hızlı yamalanıyor, sürümler sabitlenip kaynak doğrulanıyor mu ve bir YML üretiyor musunuz. Büyük ya da kamusal bir yapı için bunu satın alma ve sürekli tarama yükümlülüklerine bağlayın; çünkü bir düzenleyici kaynağın kamuya açık olup olmadığını değil, neyi incelediğinizi soracaktır.

## Sektör merceği

**Girişim.** Az nakit ömrüyle açık kaynak temeller üzerine inşa edersiniz, çünkü lisans ücretlerini karşılayamazsınız ve bir proje durursa çatallama özgürlüğünü istersiniz. Göndermeden önce bir bileşen analizi taraması çalıştırın; böylece güçlü copyleft'e sahip bir kütüphane sessizce kendi kaynağınızı yayımlamanızı zorunlu kılmaz ve tek gerçek ayırt edicinizi kesinlikle kapalı tutun. İşe alıma yardımcı olacaksa küçük, kritik olmayan bir aracı açık kaynak yapın, ama taşıyamayacağınız bir bakım yükünü kadrolamayın.

**Küçük işletme.** Kurum içi hukuk ya da platform uzmanınız yok; bu yüzden lisansı ustalaşabileceğiniz bir konu olarak değil, yanlış okumamanız gereken bir risk olarak ele alın. Yama ve hesap verebilirliğin tedarikçide olduğu desteklenen tescilli araçları ya da ticari açık kaynak dağıtımlarını tercih edin; çünkü işletemeyeceğiniz bir yığını kendi başınıza desteklemek yanlış bir ekonomidir. Bedava bir bileşeni benimsediğinizde, lisansının kullanımınıza izin verdiğini ve projenin terk edilmemiş, gerçekten bakım gördüğünü kontrol edin.

**Kurumsal.** Ölçekte sorun birçok takım genelinde tutarlılıktır: yazılı bir lisans politikası, her hatta otomatik yazılım bileşen analizi ve YML üretimi ve takım başına alışkanlık yerine TSM temelli inşa-ya-da-satın-al kararları. Açık ve tescilli yazılımı tek bir portföy olarak yönetin, satın almada açık biçimler ve kaynak kodu emaneti gibi çıkış korumalarını standartlaştırın ve kritik bağımlılıkların sağlığını izleyin; böylece terk edilmiş tek bir proje olaya dönüşmez. Üretici tarafını da kuruluşun neyi açık kaynak yaptığı ve neyi kapalı tuttuğuna dair net bir kuralla yönetin.

**Kamu.** Satın alma kuralları, şeffaflık yükümlülükleri ve kamusal hesap verebilirlik her seçimi şekillendirir. Kurumlar arası yeniden kullanımı ve dijital egemenliği ilerletmek için vergi mükellefi tarafından fonlanan yazılımın varsayılan olarak kamuya açık olması ilkesi olan "kamu parası, kamu kodu"nu tartın; güvenlik açısından duyarlı ya da kişisel veri içeren kod için dar istisnalar bırakın. Her tescilli tedarikçiden açık biçimlerde veri dışa aktarma ve kaynak kodu emaneti isteyin; böylece bir tedarikçi başarısızlığı bir kamu hizmetini ortada bırakmaz ve vatandaşlar kendilerini yöneten kuralları denetleyebilsin diye hassas olmayan kaynağı yayımlayın.

## Örnekler

**Girişim.** Üç kurucu bir girişim, lisans ücretlerini karşılayamadığı ve bir proje durursa çatallama özgürlüğünü istediği için ürününün tamamını açık kaynak temeller (Linux, bir açık kaynak veritabanı, bir web çatısı) üzerine inşa eder. Göndermeden önce kuruculardan biri bir bileşen analizi taraması çalıştırır ve tescilli eşleştirme algoritmalarını yayımlamalarını zorunlu kılacak güçlü copyleft'e sahip bir kütüphaneyi yakalar; bu yüzden onu serbest lisanslı bir eşdeğerle değiştirirler. Tek ayırt edicileri olan o algoritmayı kesinlikle kapalı tutarlar ve yalnızca iyi niyet kazanmak ve mühendisleri çekmek için küçük bir dahili günlükleme aracını açık kaynak yaparlar.

**Kurumsal.** Büyük bir sigortacı çekirdek platformunu açık kaynak temeller üzerinde çalıştırır: Linux, yaygın kullanılan bir açık kaynak veritabanı ve bir konteyner orkestratörü. Ama tescilli bir aktüeryal modelleme paketi satın alır; çünkü tedarikçinin alan uzmanlığı, düzenleyici sertifikaları ve destek sözleşmesi ücrete değer ve karşılaştırılabilir bir açık alternatif yoktur. Tesisat üzerinde hesap verebilirlik ve yamalar almak için **ticari açık kaynağa** (açık bileşenlerin tedarikçi destekli dağıtımları) abonelik öder; ayırt edici fiyatlama algoritmasını ise kesinlikle tescilli ve kurum içinde tutar. Her seçimi ideoloji değil TSM analizi (bölüm 10.10) yönlendirir.

**Kamu.** Ulusal bir vergi kurumu, "kamu parası, kamu kodu" politikası altında yeni bir yardım hak edişi hizmetini açık kaynak bileşenler ve açık standartlar (bölüm 3.8) üzerine inşa eder; böylece diğer kurumlar onu yeniden kullanabilir ve vatandaşlar kuralları denetleyebilir. Hassas olmayan kodu kamuya açık bir depoda yayımlar, güvenlik nedeniyle yalnızca dolandırıcılık tespit sezgisellerini kapalı bırakır. Bu, tedarikçi kilitlenmesini azaltır ve dijital egemenliği (bölüm 10.11) ilerletir. Satın alma kuralları (bölüm 10.3), tedarikçi başarısız olursa sürekliliği garanti etmek için her tescilli bileşenden açık biçimlerde veri dışa aktarma ve kaynak kodu emaneti sağlamasını şart koşar.

## İş gerekçesi: motivasyonlar, YG ve TSM

Açık kaynağın finansal cazibesi, lisans ücretinin olmaması, davanın en az güvenilir kısmıdır; çünkü edinme TSM'nin küçük bir bölümüdür. Dayanıklı getiriler stratejiktir: kilitlenmeden özgürlük (bir tedarikçiyi yeniden mimari kurmadan değiştirme ya da bırakma yeteneği), güvenlik ve uyum için denetlenebilirlik, mühendisler taahhüt etmeden önce deneyebildiği için daha hızlı benimseme ve olağan kodun bakımının tüm bir sektör genelinde paylaşılması. Dengeleyici maliyetler gerçektir. Entegrasyonu, operasyonları, güvenlik müdahalesini ve çoğu zaman ücretli desteği sizin sağlamanız gerekir ve kötü seçilmiş, bakımı yapılmayan bir proje olaylarda herhangi bir lisansın maliyetinden fazlasına mal olabilir.

Tescilli yazılımın iş gerekçesi hesap verebilirlik ve kolaylıktır: üründen sorumlu tek bir tedarikçi, zorlayabileceğiniz bir destek sözleşmesi, bütünleşik özellikler ve öngörülebilir bütçeleme. Gizli maliyeti kilitlenmedir: bir tedarikçinin fiyatları artırmasına ya da hizmeti çok az başvuru yoluyla bozmasına izin veren geçiş maliyetleri, artı tedarikçinin ödeme gücüne ve yol haritasına bağımlılık. Yaygın **iş modelleri** çizgiyi bulanıklaştırır: **[açık çekirdek](https://en.wikipedia.org/wiki/Open-core_model)** (tescilli ücretli eklentileri olan açık bir taban), **çift lisanslama** (aynı kodun hem bir copyleft hem de ücretli bir ticari lisans altında sunulması), **[hizmet olarak yazılım](https://en.wikipedia.org/wiki/Software_as_a_service) (SaaS)** (yazılımın kiraladığınız barındırılan bir hizmet olarak çalışması; ikili dosyaya hiç sahip olmadığınız için kaynak ilgisiz olabilir) ve aksi halde bedava kodun etrafında hizmet satan **destek/abonelik** modelleri.

Bir üretici için **ayırt edici olmayan kendi yazılımınızı açık kaynak yapmanın** YG'si büyük olabilir. Dış katkıcılar bakım yükünüzü azaltır. Proje bir işe alım ve itibar varlığı olur. Dış benimseme sizin standardınızı fiilî standart yapar. Kamu için kamu sektörü genelinde şeffaflık ve yeniden kullanım sağlar. Stratejik kural basittir: maliyetini paylaşmak ve bir ekosistem büyütmek için olağan olanı açık kaynak yapın, geri kalan her şeyi fonlayan avantajı korumak için ayırt ediciyi kapalı tutun.

## Anti-kalıplar ve tuzaklar

- **"Bedava bedavadır":** sıfır edinme maliyetini sıfır TSM saymak, sonra işletmeyi ve desteği eksik fonlamak.
- **Lisans körlüğü:** dağıtılan tescilli bir ürüne güçlü copyleft kodu gömüp hiç planlamadığınız yükümlülükleri tetiklemek.
- **"Çok göz" inancı:** tek bir fazla yüklü bakımcısı ve güvenlik incelemesi olmayan açık bir projenin denetlendiğini varsaymak.
- **Gizlilik yoluyla güvenlik:** kapalı kaynağın yalnızca saldırganlar okuyamadığı için güvenli olduğuna inanmak.
- **İdeolojik mutlakçılık:** bileşen başına değer ve TSM'ye göre seçmek yerine "hepsi açık" ya da "hepsi tescilli" demek.
- **Kaynağı yok saymak:** YML, sürüm sabitleme ya da tedarik zinciri doğrulaması olmadan bağımlılık çekmek (bölüm 4.2).
- **Taç mücevherlerini açık kaynak yapmak:** sizi ayırt eden kodu yayımlayıp avantajınızı bedavaya vermek.
- **Çatalla ve unut:** terk edilmiş bir projeyi, çatalı gerçekten sürdürme kapasitesi olmadan çatallamak.

## Olgunluk modeli

**Düzey 1, Başlangıç.** Açık kaynak ve tescilli bileşenler yapıya ad hoc girer. Lisanslar okunmaz, envanter ya da YML yoktur ve modeller arasındaki seçim alışkanlıkla ya da yalnızca fiyatla yapılır. Terk edilme ve lisans riski yalnızca bir şey bozulduğunda ortaya çıkar ve her takım kendi başına tepki verir.

**Düzey 2, Geliştirme.** Bazı takımlar temel uygulamalara başlar: bir bileşen ve lisans envanteri, kabul edilebilir lisanslara dair kaba bir görünüm ve ara sıra yazılım bileşen analizi. İnşa-ya-da-satın-al ve açık-ya-da-kapalı kararları yazıya dökülür, ama disiplin yamalıdır ve takımdan takıma tutarsızdır; bu yüzden alışkanlığın yerleşmediği yerde bir copyleft ya da otobüs faktörü sürprizi yine de sızabilir.

**Düzey 3, Standartlaştırma.** Belgelenmiş bir çerçeve hem tüketimi hem üretimi kuruluş genelinde yönetir. Bileşenler TSM'ye ve proje sağlığına göre seçilir, lisanslar hatta otomatik olarak uygulanır ve ihlaller bir derlemeyi engeller, YML'ler olağan bir iş olarak üretilir ve açık bir politika kuruluşun neyi açık kaynak yaptığını, neyi kapalı tuttuğunu belirtir. Açık biçimler ve kaynak kodu emaneti gibi çıkış korumaları satın almada standarttır ve her takım kendi kurallarını değil aynı kuralları izler.

**Düzey 4, Yönetme.** Program temel çizgilere karşı ölçülür ve kontrol edilir. Kuruluş, ürünler genelinde YML kapsamı, politikayı ihlal eden bağımlılıkların payı, açıklanan bir bağımlılık güvenlik açığını yamalama için ortalama süre, kritik projeler için otobüs faktörü ve sağlık puanları ve her seçimi gerekçelendiren tahmine karşı gerçekleşen TSM gibi metrikleri izler. Eşikler eylemi tetikler: bakımı duran ya da yama gecikmesi hedefi aşan bir bileşen kanıta dayalı olarak değiştirilmek üzere işaretlenir ve açık-ya-da-kapalı ile inşa-ya-da-satın-al kararları alışkanlıkla savunulmak yerine sayılara karşı gözden geçirilir.

**Düzey 5, Orkestrasyon.** Açık kaynak stratejisi kasıtlı bir iş yeteneğidir, kuruluş genelinde bütünleşiktir ve sürekli iyileştirilir. Kuruluş bağımlı olduğu projelere katkıda bulunur ve bazen onları yönetir, ayırt edici olmayan yazılımını olağan bir iş olarak açık kaynak yapar ve bağımlılık sağlığı ile TSM verisini satın alma, güvenlik ve ürün planlamasına geri besler. Açık ve tescilli yazılım portföyünü rutin olarak yeniden dengeler; maliyet, risk, egemenlik ve stratejik avantajdaki kaymalara, bir krize zorlanmadan önce uyum sağlar.

## Tartışma fikirleri

- Yapınızın neresinde tek bir tedarikçiyi ya da bakımcıyı kaybetmek varoluşsal olur ve çıkış planınız nedir?
- Kendi sistemlerinizden hangileri açık kaynak yapabileceğiniz olağan şeyler, hangileri korunacak gerçek ayırt edicilerdir?
- Kuruluşunuz "çok göz"ü gerçek bir güvenlik denetimi olarak mı yoksa sorgulanmamış bir varsayım olarak mı ele alıyor?
- Kamu sektörü okurları için: "kamu parası, kamu kodu" varsayılanı bir sonraki satın almanızda neyi değiştirirdi?
- TSM karşılaştırmalarınız, açık kaynağın size kaydırdığı operasyonel ve destek maliyetlerini ne kadar iyi yakalıyor?

## Önemli çıkarımlar

- **Açık ve kapalı ayrımını fiyat değil lisans tanımlar**; özgürlük anlamında özgür ile fiyat anlamında özgür arasındaki ve serbest ile copyleft arasındaki farkı bilin.
- **Hiçbir model doğası gereği daha güvenli ya da daha ucuz değildir.** Açıklık etiketini değil, projenin uygulamalarını ve tam TSM'sini yargılayın.
- **Açıklık kilitlenmeye karşı en güçlü panzehirdir** ve denetlenebilirlik, taşınabilirlik ve çatallama yeteneği sağlar; tescilli yazılım denetim karşılığında hesap verebilirlik ve kolaylık sunar.
- **Bileşen başına değere göre karar verin** ve modelleri ideolojiyle değil, bilinçle karıştırın.
- **Üretici olarak olağan olanı açık kaynak yapın ve ayırt ediciyi kapalı tutun**; kamuda ise şeffaflık, yeniden kullanım ve egemenlik için "kamu parası, kamu kodu"nu tartın.

## Kaynaklar ve ileri okuma

- Eric S. Raymond, *The Cathedral and the Bazaar*
- Nadia Eghbal, *Working in Public: The Making and Maintenance of Open Source Software*
- Karl Fogel, *Producing Open Source Software: How to Run a Successful Free Software Project*
- Adrian Cockcroft and others, various O'Reilly titles on open-source strategy and operations
- Free Software Foundation, *The Free Software Definition* (and the GNU General Public Licence texts)
- Open Source Initiative, *The Open Source Definition* and approved-licence list
- Free Software Foundation Europe, *Public Money, Public Code* campaign materials
- Yochai Benkler, *The Wealth of Networks*
