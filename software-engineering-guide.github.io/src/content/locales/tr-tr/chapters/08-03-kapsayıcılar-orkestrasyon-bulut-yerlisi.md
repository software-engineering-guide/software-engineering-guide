# 8.3 Kapsayıcılar, orkestrasyon ve bulut yerlisi

## Genel bakış ve motivasyon

Bir [kapsayıcı](https://en.wikipedia.org/wiki/OS-level_virtualization), bir uygulamayı bağımlılıklarıyla birlikte tek, taşınabilir, yalıtılmış bir birim halinde paketler. Bir dizüstü bilgisayarda, bir test ortamında ve üretimde aynı biçimde çalışır. Orkestrasyon platformları, en başta [Kubernetes](https://en.wikipedia.org/wiki/Kubernetes), çok sayıda kapsayıcıyı makine filoları üzerinde zamanlar ve yönetir. Yerleştirmeyi, ölçeklemeyi, sağlığı, ağ iletişimini ve kurtarmayı onlar üstlenir. [Bulut yerlisi](https://en.wikipedia.org/wiki/Cloud-native_computing), bu temellerin üzerine kurulu daha geniş mimari üsluptur: gevşek bağlı, bağımsız dağıtılabilir, yatay ölçeklenebilir hizmetler olarak tasarlanmış ve dinamik, kendi kendini iyileştiren bir altyapıyı varsayan uygulamalar.

Büyük takımlar için kapsayıcılar ve orkestrasyon tek bir zor sorunu çözer. Birçok takımın yazdığı birçok hizmeti ortak altyapıda güvenilir ve verimli biçimde çalıştırmanız gerekir. Kapsayıcılar her takıma tutarlı bir paketleme ve çalışma zamanı sözleşmesi verir; bu, "benim makinemde çalışıyor" türü hataları ortadan kaldırır. Orkestrasyon, tek tek makineleri ortak bir zeminin arkasına gizler; böylece takımlar sunuculara değil bir platforma dağıtım yapar. Bu standartlaştırma, her takımın dağıtımı, ölçeklemeyi ve dayanıklılığı yeniden icat etmesine gerek kalmadan yüzlerce ya da binlerce hizmeti işletmenizi sağlar.

Kurumsal ve kamu benimseyicileri taşınabilirlik, dayanıklılık ve kilitlenmeden uzaklaşan bir yol kazanır. Karşılığında gerçek bir karmaşıklığı ve yeni güvenlik sorumluluklarını devralırlar. Bir kapsayıcı platformu tam da programlanabilir ve dinamik olduğu için güçlüdür; bu da onu dikkatle yönetmeniz gerektiği anlamına gelir. İmaj kökeni, çok kiracılı yalıtım, ağ politikası ve maliyet platform düzeyinde kaygılar haline gelir. Kamu sektörü benimseyicileri giderek egemenlik gereksinimleri de ekler: verinin nerede bulunduğu ve ona kimin erişebileceği üzerinde denetim. Bu, tutarlı iş yüklerini seçilmiş ortamlarda çalıştırabilme yeteneğini yalnızca teknik bir ayrıntı değil, stratejik bir yetkinlik yapar.

## Temel ilkeler

- Uygulamaları küçük, tek amaçlı, değişmez kapsayıcı imajları olarak paketleyin.
- İmaj hijyenini uygulayın: asgari temel imajlar, sabitlenmiş sürümler, güvenlik açıkları için taranmış ve imzalı.
- Uygulamaları mümkün olduğunca durumsuz ve yatay ölçeklenebilir tasarlayın; durumu dışa alın.
- Orkestrasyon platformunun istenen durum modelini doğru kaynak sayın ve onun kendi kendini iyileştirmesine izin verin.
- Kiracılar, iş yükleri ve ad alanları arasında yalıtımı ve en az ayrıcalığı uygulayın.
- [On iki faktör](https://en.wikipedia.org/wiki/Twelve-Factor_App_methodology) ilkelerini (atılabilir, yapılandırması dışarıda tutulan, yatay ölçeklenebilir uygulamalar kurma yöntemi) izleyin ve onları dağıtık sistemlerin gerçeklerine göre genişletin.
- Maliyeti sonradan akla gelen bir şey değil, birinci sınıf, görünür bir mühendislik kaygısı yapın.
- Stratejik esnekliği korumak için taşınabilir, standartlara dayalı soyutlamaları tercih edin.

## Öneriler

### Titiz imaj hijyeni uygulayın

Kapsayıcı imajı temel güven ve dağıtım biriminizdir; ona öyle davranın. Saldırı yüzeyini küçültmek için asgari, güvenilir temel imajlardan başlayın. Yeniden üretilebilirlik için bağımlılık ve temel imaj sürümlerini sabitleyin. Her imajı derleme işlem hattında bilinen güvenlik açıkları için tarayın ve kritik bulguları olanları engelleyin. İmajları imzalayın ve imzaları dağıtım sırasında doğrulayın; böylece yalnızca onaylı, değiştirilmemiş imajlar çalışır. Takımların üzerine kurduğu sertleştirilmiş temel imajların özenle seçilmiş bir iç kayıt defterini tutun. Bu, iyi güvenlik varsayılanlarını otomatik yayar.

### Kalıpları yeniden icat etmek yerine Kubernetes kalıplarını kullanın

Kubernetes, yerleşik kalıplarını benimseyen takımları ödüllendirir ve modeliyle savaşanları cezalandırır. İstenen durum için bildirimsel bildirimleri (manifest) kullanın. Platformun sağlıksız örnekleri algılayıp değiştirebilmesi için sağlık yoklamaları ekleyin. Zamanlayıcının iş yüklerini güvenle paketleyebilmesi için kaynak istekleri ve sınırları belirleyin. Elastik talep için yatay otomatik ölçekleme kullanın. Bir veritabanını yönetmek, sertifikaları döndürmek ya da özel kaynakları uzlaştırmak gibi sürekli çalışması gereken operasyonel mantık için, insan operasyonel bilgisini durumu izleyip harekete geçen yazılıma kodlayan operatör kalıbını kullanın. Platformun üzerine özel orkestrasyon kurma dürtüsüne direnin. Yerel yapıları tercih edin.

### Çok kiracılığı bilinçli tasarlayın

Birçok takım bir kümeyi paylaştığında yalıtım bir incelik değil, güvenlik ve güvenilirlik gereksinimidir. Ad alanlarını kiracılık sınırı olarak kullanın. Hiçbir kiracının diğerlerini aç bırakamaması için kaynak kotalarını uygulayın. Trafiği açıkça izin verilenle sınırlamak için ağ politikaları uygulayın. Her takımın neler yapabileceğini sınırlamak için [rol tabanlı erişim denetimi](https://en.wikipedia.org/wiki/Role-based_access_control) (RBAC) kullanın. Daha güçlü yalıtım ihtiyacı olan iş yükleri için ayrı kümeleri ya da daha güçlü kum havuzlamayı düşünün. Modelinizin yumuşak çok kiracılık (güvenilir iç takımlar) mi yoksa sert çok kiracılık (birbirine güvenmeyen iş yükleri) mi olduğuna erken karar verin, çünkü ikisi çok farklı denetimler ister.

### Bulut yerlisi, on iki faktör ve ötesini kurun

Açık bağımlılıkları, ortamdaki yapılandırması, durumsuz süreçleri, atılabilirliği vb. ile on iki faktör yöntemi, dinamik bir platformda gelişen hizmetler için mükemmel bir temel olmayı sürdürür. Onu dağıtık sistemlerin ek gerçekleri için genişletin. Kısmi arızaya göre tasarlayın. İşlemleri eş güçlü ve yeniden denenebilir yapın. Sağlığı ve telemetriyi açığa çıkarın. Gözlemlenebilirliği sonradan eklenen bir şey değil, yerleşik bir özellik olarak ele alın. Uygulama örneklerinin atılabilir ve yatay ölçeklenebilir kalması için bütün durumu yönetilen veri hizmetlerine dışa alın.

### Çoklu bulut, melez ve egemen stratejileri gerçekçi biçimde planlayın

Taşınabilirlik değerlidir, ama onu açık gözle izleyin. İş yükleri gerekirse taşınabilsin diye kapsayıcılar, Kubernetes ve açık API'ler gibi taşınabilir soyutlamalarda standartlaşın. Ama her yönetilen hizmeti reddetme tuzağından kaçının; bu, gerçek verimliliği varsayımsal taşınabilirlikle takas eder. Melez ve egemenlik gereksinimleri için, aynı iş yüklerinin ve işlem hatlarının seçilmiş bir bölgede, özel bir veri merkezinde ya da yargı yetkisi ve veri ikametgâhı kurallarını karşılayan egemen bir bulutta çalışabilmesini sağlayacak biçimde tasarlayın. Egemenlik ve ikametgâh sınırlarını mimaride ve politikada açık kılın.

### FinOps ile maliyeti görünür kılın

Elastik bulut ortamlarında maliyet, mühendislik kararlarının doğrudan sonucudur; bu yüzden mühendislere görünürlük ve hesap verebilirlik verin. Kaynakları maliyet dağıtımı için etiketleyin. Harcamayı takımlara ve hizmetlere atfedin. Maliyet verisini performans ölçütlerinin yanında gösterin. İş yüklerini doğru boyutlandırın, talebe uymak için otomatik ölçekleme kullanın ve boşta kalan kaynakları geri alın. Mühendisliği, finansı ve ürünü bir araya getiren bir FinOps uygulaması kurun; böylece bulut harcaması üç ayda bir sürpriz yerine ortak, sürekli bir sorumluluk olur.

## Ödünleşimler: artılar ve eksiler

| Seçim | Artılar | Eksiler | En uygun olduğu yer |
|---|---|---|---|
| Kubernetes | Güçlü, taşınabilir, devasa ekosistem | Dik karmaşıklık; operasyonel yük | Ölçekte birçok hizmet |
| Yönetilen kapsayıcı hizmeti | Daha az operasyon yükü; daha hızlı başlangıç | Bir miktar kilitlenme; daha az denetim | Sadelik isteyen takımlar |
| Tek ortak küme | Verimli kaynak kullanımı | Yalıtımı daha zor; etki alanı | Güvenilir iç kiracılar |
| Kiracı başına küme | Güçlü yalıtım | Daha yüksek maliyet ve yük | Birbirine güvenmeyen ya da düzenlemeye tabi iş yükleri |
| Çoklu bulut taşınabilirliği | Esneklik; kilitlenmeyi önler | En düşük ortak payda hizmetler | Stratejik risk azaltma |
| Derin tek bulut yönetilen hizmetleri | En yüksek verimlilik | Satıcıya bağımlılık | Hıza odaklı takımlar |

Kapsayan ödünleşim yetenek ile karmaşıklık arasındadır. Kubernetes ve bulut yerlisi mimariler elastikiyet, dayanıklılık ve hız sunar. Ama küçük takımların rutin olarak hafife aldığı ciddi bir operasyonel ve bilişsel yük getirirler. Aynı şekilde, tam [çoklu bulut](https://en.wikipedia.org/wiki/Multicloud) taşınabilirliğinin peşinden koşmak verimliliği seçenekle takas eder. Doğru cevap ölçeğe ve riske bağlıdır. Çok takımlı ve güçlü yönetişim ihtiyacı olan büyük kurumlar yatırımı genellikle haklı çıkarır. Daha küçük girişimlere karmaşıklığı gizleyen yönetilen hizmetler çoğu zaman daha iyi hizmet eder.

## Takımınızla tartışılacak sorular

1. **İmajları imzalıyor ve imzaları dağıtım sırasında doğruluyor musunuz ve kritik bir güvenlik açığı derlemeyi gerçekten engelliyor mu?** İmaj güven biriminizdir; bu yüzden etrafındaki tedarik zinciri uyarıları değil, sert kapıları hak eder. Yalnızca imzalı ve doğrulanmış imajların çalışıp çalışamayacağına, taramanın kritik bulguları engelleyip engellemediğine ya da yalnızca kaydedip kaydetmediğine ve takımların üzerine kurduğu sertleştirilmiş temel imajların özenle seçilmiş kayıt defterini kimin sürdürdüğüne karar verin. Kurumsal ve kamu iş yükleri için bu çoğu zaman bir uyum gereksinimidir ve ayrıca zehirlenmiş bir bağımlılığın üretime ulaşmasına karşı en iyi savunmanızdır. Mevcut durumu getirin: çalışan imajların ne kadarı sertleştirilmiş temelinizden geliyor, kaçında yamalanmamış kritik CVE'ler var ve imzasız bir imaj şu anda zamanlanabilir mi. Kritik bir bulgu bir dağıtımı durdurmuyorsa, tarayıcınız süstür.

2. **Kaynak istekleri, sınırları ve kotaları, pahalı kapasiteyi boşta bırakmadan bir iş yükünün komşularını aç bırakmasını nasıl önler?** Ortak bir kümede sınırı olmayan bir iş yükü çevresindeki her şeyi çökertebilir ya da kısabilir ve fazla cömert belirlenen kotalar, platformu haklı çıkaran kullanım kazançlarını boşa harcar. Makul varsayılanlara, onları kimin ayarlayacağına ve hiç istek belirlenmemiş iş yüklerini nasıl yakalayacağınıza karar verin. Ölçekte bu hem bir güvenilirlik hem de bir maliyet denetimidir, çünkü doğru boyutlandırma FinOps tasarrufunun büyük kısmının yaşadığı yerdir. Veri getirin: mevcut küme kullanımı, iş yüklerinin ne sıklıkla tahliye edildiği ya da kısıldığı ve hangi ad alanlarında kota olmadığı. Amaç yoğun ama güvenli bir paketlemedir; bu yüzden eksik sınırlara platformun reddettiği bir kusur gibi davranın.

3. **Bir kapsayıcının içinde hangi durumun yaşamasına izin veriliyor ve geri kalan her şey nereye gidiyor?** Bulut yerlisi dayanıklılık, platformun istediği zaman yeniden zamanlayabileceği atılabilir örneklere bağlıdır ve bu ancak önemli durum kapsayıcının yerel diskinde değil yönetilen veri hizmetlerinde yaşıyorsa geçerlidir. Kuralı açıkça belirleyin, çünkü kazara bir kapsayıcıda saklanan durum, bir sonraki yeniden zamanlamada veri kaybına dönüşür. Eski uygulamaları taşıyan takımlar için bu çoğu zaman en zor kısımdır, çünkü eski hizmetler kararlı bir yerel dosya sistemi varsayar. Bir envanter getirin: hangi hizmetler yerel durum yazıyor, hangileri yapışkan oturumlara ya da düğüm yakınlığına dayanıyor ve her birini dışa almak için ne gerekir. Durum dışarıda olana kadar, elastik görünen ama gerçekte taşınamayan kapsayıcılarınız vardır.

4. **Birçok takım bir kümeyi paylaştığında yalıtım modeliniz bilinçli olarak yumuşak ya da sert çok kiracılık olarak seçildi mi ve denetimler bu seçimle uyuşuyor mu?** Ad alanları güvenilir iç takımları ayırır, ama aktif olarak düşmanca ya da ele geçirilmiş bir iş yükünü kapsamazlar ve yumuşak kiracılığa sert kiracılıkmış gibi davranmak olmayı bekleyen bir güvenlik olayıdır. İş yükü başına, kiracıların yalnızca adil paylaşıma mı ihtiyacı olduğuna yoksa birbirine güvenmediklerinin varsayılması gerektiğine karar verin, sonra denetimleri eşleyin: yumuşak durum için ad alanları, kotalar, ağ politikaları ve RBAC; sert durum için ayrı kümeler ya da daha güçlü kum havuzlama. Büyük bir kurum için bu karar maliyeti doğrudan belirler, çünkü kiracı başına bir küme paylaşılan ad alanlarından çok daha pahalıdır; bu yüzden yalıtım bütçesini yalnızca tehdit modelinin gerektirdiği yerde harcamak istersiniz. Kiracı envanterini getirin: bugün hangi iş yükleri bir kümeyi paylaşıyor, hangileri düzenlemeye tabi ya da dış dünyaya dönük trafik taşıyor ve ağ politikası nerede hâlâ varsayılan olarak izin veriyor. Kurumsal ve kamu ortamlarında birbirine güvenmeyen iş yüklerini yumuşak kiracılık altında karıştırmak, bir denetçinin işaretleyeceği bulgunun ta kendisidir; sınırı onlardan önce adlandırın.

5. **Çoklu bulut taşınabilirliği için ne kadar ödüyorsunuz ve onu gerçekten kullanacak mısınız?** Kapsayıcılarda, Kubernetes'te ve açık API'lerde standartlaşmak iş yüklerini taşınabilir tutar, ama bu seçeneği korumak için her yönetilen hizmeti reddetmek, kurumun hiç kullanmayabileceği taşınabilirlik için gerçek, günlük verimliliği takas eder. Taşınabilirliğin gerçek bir gereksinim olduğu yeri (örneğin imzaladığınız bir egemenlik ya da çıkış yükümlülüğü), her takımı yavaşlatan bir güvenlik battaniyesi olduğu yerden ayırarak karar verin. Rekabet eden husus hızdır: derin yönetilen hizmetler özellikleri daha hızlı sevk eder ve en düşük ortak payda mimarisi her takımın üzerinde süregelen bir vergidir. Kanıt getirin: hangi yönetilen hizmetlerden kaçındınız ve bunun mühendislik zamanına maliyeti ne oldu, bir iş yükünü hiç sağlayıcılar arasında taşıdınız mı ve sözleşmeleriniz gerçekte neyi gerektiriyor. Kamu ve düzenlemeye tabi benimseyiciler için veri ikametgâhı ve egemen bulut kuralları taşınabilirliği pazarlık dışı yapabilir; bu yüzden aynı bildirimlerin ve işlem hatlarının egemen bir bölgede ve özel bir kapalı alanda çalışacağı biçimde tasarlayın, ama bunun bedava sigorta değil bir uyum maliyeti olduğu konusunda dürüst olun.

6. **Her takım ne harcadığını görebiliyor mu ve fatura sürpriz olmadan önce onun sahibi olan biri var mı?** Elastik bir platformda maliyet mühendislik kararlarının doğrudan çıktısıdır; ama maliyet dağıtım etiketleri ve görünür panolar olmadan harcama, finans konuyu üst makama taşıyana kadar kimsenin kendini sorumlu hissetmediği ortak bir havuzda birikir. Maliyeti takımlara ve hizmetlere nasıl atfedeceğinize, onu kimin gözden geçireceğine ve mühendislerin maliyeti performans ölçütlerinin yanında mı gördüğüne yoksa yalnızca üç ayda bir mi duyduğuna karar verin. Gerilim, hesap verebilirlik ile sürtünme arasındadır: maliyeti fazla zorlarsanız her karar bir bütçe pazarlığına dönüşür; görmezden gelirseniz boşta duran, aşırı büyük iş yükleri sessizce bileşik büyür. Sayıları getirin: takım başına mevcut harcama, ne kadar kapasitenin boşta ya da aşırı büyük olduğu ve kontrolden çıkmış bir iş yükünün ne kadar çabuk fark edileceği. Kurumsal ve kamu bütçeleri için atfedilmemiş bulut harcaması hem bir yönetişim başarısızlığı hem de gerçek bir mali risktir; bu yüzden olay sonrasında uzlaşmak yerine mühendisliği, finansı ve ürünü aynı konuşmaya koyan bir FinOps uygulaması kurun.

## Sektör merceği

**Girişim.** Kendi barındırdığınız bir Kubernetes kümesi yerine yönetilen bir kapsayıcı hizmetine uzanın: birkaç hizmetle ve platform mühendisi olmadan, kontrol düzlemleri karşılayamayacağınız bir dikkat dağıtıcıdır. Asgari bir temelden küçük imajlar paketleyin, sürümleri sabitleyin, derlemeye tek bir güvenlik açığı taraması ekleyin ve bütün durumu yönetilen bir veritabanına itin; böylece örnekler atılabilir kalır. Gerçekten gerekçelendirecek hizmetleriniz ve insanlarınız olana kadar ad alanlarını, operatörleri ve çoklu bulut taşınabilirliğini atlayın.

**Küçük işletme.** Özel bir platform uzmanı ve sıkı bir bütçe yoksa, yönetilen hizmetlere sıkıca yaslanın ve aksi halde kadrolamanız gerekecek orkestrasyonu sağlayıcının işletmesine izin verin. Kapsayıcı temellerini güvenlik tabanınız sayın: asgari imajlar, sürüm sabitleme ve işlem hattında bir tarama, az emekle korumanın çoğunu sağlar. Bir platform kurmak yerine desteklenen bir platform satın almayı tercih edin ve fiyatlandırma ya da şartlar değişirse tuzağa düşmemeniz için yeterli taşınabilirliği, standart kapsayıcıları ve açık API'leri koruyun.

**Kurumsal.** Görev, birçok takım arasında platform yönetişimidir: sertleştirilmiş temel imajlar, imzalama ve tarama kapıları, kotalı ad alanı kiracılığı, ağ politikası ve RBAC sağlayan merkezî bir platform takımı; ayrıca maliyet dağıtım etiketleri ve bir FinOps panosu. Yüzlerce hizmetin aynı biçimde işlemesi için dağıtım sözleşmesini standartlaştırın; takımlar dağıtımı self servis yaparken güvenliği, çok kiracılığı ve maliyeti merkezî yönetin. Platform takımını gerektiği gibi fonlayın, çünkü yetersiz kaynaklı bir platform bütün kurumun beklediği darboğaza dönüşür.

**Kamu.** Egemenlik, veri ikametgâhı ve kamusal hesap verebilirlik mimariyi şekillendirir. İş yüklerini standart kapsayıcılar ve Kubernetes üzerinde çalıştırın; böylece aynı işlem hatları egemen bir bölgede ve akredite edilmiş bir şirket içi kapalı alanda çalışır ve ikametgâh ile erişim sınırlarını gelenek yerine politika olarak kodlayın. İmajları iç sertleştirilmiş bir kayıt defterinden çekin, en hassas veriye sert çok kiracılık uygulayın ve size dayanıklılık ile pazarlık gücü veren taşınabilirliği koruyun; çünkü tedarik kuralları çoğu zaman tek satıcıya kilitlenmeyi yasaklar.

## Örnekler

**Girişim.** Altı kişilik bir girişim, iki hizmetini asgari bir temelden derlenmiş küçük kapsayıcı imajları olarak paketler ve onları kendi barındırdığı bir Kubernetes kümesi yerine yönetilen bir kapsayıcı hizmetinde çalıştırır; böylece kimsenin kontrol düzlemlerine bakıcılık yapması gerekmez. Temel imaj sürümlerini sabitler ve derlemelerine bir güvenlik açığı taraması ekler, ama bir avuçtan fazla hizmetleri olana kadar daha ağır orkestrasyon özelliklerini bilerek atlarlar. Durum yönetilen bir Postgres veritabanında yaşar; bu, kapsayıcıları atılabilir tutar ve platformun onları veri kaybı olmadan yeniden başlatmasına ya da ölçeklemesine izin verir.

**Kurumsal.** Bir telekomünikasyon şirketi, ortak Kubernetes kümelerinde birkaç yüz [mikro hizmet](https://en.wikipedia.org/wiki/Microservices) çalıştırır. Bir platform takımı sertleştirilmiş temel imajlar sağlar, imaj imzalamayı ve güvenlik açığı kapılarını zorunlu kılar ve iş birimlerini kotalar, ağ politikaları ve RBAC ile ad alanlarına ayırır. Maliyet dağıtım etiketleri ve bir FinOps panosu harcamayı her ürün hattına atfeder ve otomatik ölçekleme kapasiteyi talebe göre boyutlandırır. Ürün takımları sunucuları yönetmeden tutarlı bir platforma günde düzinelerce kez dağıtım yapar. Şirket güvenlik ve maliyet üzerinde merkezî denetimi elinde tutar.

**Kamu.** Ulusal bir sağlık hizmeti, vatandaş verisini ulusal sınırlar içinde ve ulusal yasal denetim altında tutmak zorundadır. İş yüklerini standart kapsayıcılar ve Kubernetes kullanarak egemen bir bulut bölgesinde çalıştırır; böylece aynı işlem hatları ve bildirimler en hassas veri için şirket içi akredite edilmiş bir ortamda da çalışır. Veri ikametgâhı ve erişim sınırları politika olarak kodlanır, imajlar iç sertleştirilmiş bir kayıt defterinden çekilir ve sert çok kiracılık hassas iş yüklerini yalıtır. Egemen bölge ile özel kapalı alan arasındaki taşınabilirlik, hizmete uyumdan ödün vermeden dayanıklılık ve pazarlık gücü verir.

## İş gerekçesi: motivasyonlar, YG ve TSM

Kapsayıcıların ve orkestrasyonun YG'si, daha yüksek kaynak kullanımından, daha hızlı ve daha güvenilir dağıtımlardan, harcamayı talebe uyduran elastik ölçeklemeden ve kendi kendini iyileştirmeyle artan dayanıklılıktan gelir. Ortak bir platformda standartlaşmak, takımlar arasındaki yinelenen emeği azaltır ve işe alıştırmayı hızlandırır, çünkü her hizmet aynı dağıtım ve operasyon sözleşmesini izler.

TSM analizi operasyonel yük konusunda dürüst olmalıdır. Benimseme maliyetleri arasında platform mühendisliği personeli, eğitim, imajlar ve kümeler için güvenlik araçları ve platformu işletmenin süregelen emeği yer alır. Benimsememenin maliyeti, takımlar arasında tutarsız özel dağıtımı, pahalı altyapının kötü kullanımını, kırılgan elle ölçeklemeyi ve dayanıklılık ile egemenlik gereksinimlerini karşılamadaki zorluğu içerir. Yönetim için gerekçe ölçeğe dayanır. Belirli bir hizmet sayısının altında karmaşıklık karşılığını vermeyebilir ve yönetilen bir hizmet daha akıllıca olur. Ama kurumsal ve kamu ölçeğinde, yönetilen bir bulut yerlisi platform, platform takımını düzgün işletmesi için fonladığınız sürece genellikle en maliyet etkin ve dayanıklı temeldir.

## Anti-kalıplar ve tuzaklar

- **Şişman, taranmamış imajlar.** Güvenilmeyen temellerden derlenen şişkin imajlar gereksiz güvenlik açıkları taşır ve her şeyi yavaşlatır.
- **Her şey için Kubernetes.** Bir avuç basit hizmet için karmaşık bir orkestratör benimsemek, karşılığı olmayan karmaşıklık satın almaktır.
- **Kaynak sınırlarını görmezden gelmek.** İstekler ve sınırlar olmadan bir iş yükü komşularını aç bırakabilir ya da çökertebilir.
- **Düşmanca iş yükleri için yumuşak kiracılık.** Birbirine güvenmeyen kiracıları yalıtmak için yalnızca ad alanlarına güvenmek, olmayı bekleyen bir güvenlik olayıdır.
- **Kazara durumlu kapsayıcılar.** Önemli durumu atılabilir kapsayıcıların içinde saklamak yeniden zamanlamada veri kaybına yol açar.
- **Maliyet körlüğü.** Bulut harcamasını bir mühendislik çıktısı yerine sabit genel gider saymak, kontrolden çıkan faturalara yol açar.
- **Taşınabilirlik tiyatrosu.** Kurumun asla gerçekten kullanmayacağı taşınabilirliği korumak için bütün yönetilen hizmetleri reddetmek.

## Olgunluk modeli

**Düzey 1, Başlangıç.** Kapsayıcılar, varsa, geçici biçimde kullanılır. İmajlar elle derlenir ve taranmaz, dağıtım elle ve tepkiseldir ve ortak bir platform, maliyet görünürlüğü ya da yalıtım modeli yoktur.

**Düzey 2, Geliştirme.** Takımlar uygulamaları kapsayıcılaştırır ve bir orkestratör benimser, ama uygulamalar gruplar arasında değişir. İmaj taraması, kaynak sınırları ve imzalama tutarsızdır; maliyet ve çok kiracılık sistematik biçimde yönetilmez.

**Düzey 3, Standartlaştırma.** Standartlaştırılmış bir platform kurum genelinde belgelenir ve uygulanır: sertleştirilmiş temel imajlar, imzalama ve tarama kapıları, kota ve ağ politikalı ad alanı tabanlı kiracılık, RBAC ve maliyet dağıtımı. Bulut yerlisi ve on iki faktör kalıpları yerel bir seçim değil beklenen norm olur.

**Düzey 4, Yönetme.** Platform temel çizgilere göre ölçülür ve denetlenir. Küme kullanımını, çalışan imajların sertleştirilmiş temelden derlenen payını, yamalanmamış kritik güvenlik açıklarını, dağıtım sıklığını ve değişiklik başarısızlık oranını, tahliye ve kısma oranlarını ve takım ile hizmet başına maliyeti bütçeye karşı izlersiniz. Kapılar bu kanıta göre uygulanır: eksik kaynak sınırları ve imzasız imajlar otomatik reddedilir ve standarttan kayma bir uyarı yerine eylemi tetikler.

**Düzey 5, Orkestrasyon.** Platform self servis ve kendi kendini iyileştiren, kurum genelinde bütünleşik ve uyarlanabilirdir. FinOps kapasiteyi sürekli doğru boyutlandırır ve geri alır, taşınabilir mimari melez ve egemenlik gereksinimlerini destekler ve platform ölçülen kullanımdan sürekli iyileşir; iş yükleri, maliyet ve risk tablosu değiştikçe bileşenleri emekliye ayırıp değiştirir.

## Tartışma fikirleri

- Kubernetes benimsemek hangi ölçekte kendi içinde bir karmaşıklık olmaktan çıkıp karşılığını vermeye başlar?
- İş yükleriniz için yumuşak ve sert çok kiracılık arasındaki doğru sınır nerededir?
- Çoklu bulut taşınabilirliğine, derin yönetilen hizmetlerin verimliliğine kıyasla ne kadar yatırım yapmalısınız?
- Her kararı bir bütçe pazarlığına dönüştürmeden mühendislere gerçek maliyet hesap verebilirliğini nasıl verirsiniz?
- Temel imajlar için yönetişim modeliniz nedir ve sertleştirilmiş kayıt defterini kim sürdürür?
- Egemenlik ve veri ikametgâhı gereksinimleri platform mimarinizi nasıl şekillendirir?

## Önemli çıkarımlar

- Kapsayıcılar paketlemeyi ve çalışma zamanını standartlaştırır; orkestrasyon operasyonu ölçekte standartlaştırır.
- İmaj hijyeni, yani asgari, sabitlenmiş, taranmış, imzalı imajlar, temel güvenliktir.
- Özel orkestrasyon kurmak yerine yerel Kubernetes kalıplarını ve operatörleri kullanın.
- Çok kiracılık modelini, iş yüklerinin birbirine ne kadar güvendiğine göre bilinçli seçin.
- On iki faktörü izleyin ve kısmi arıza ve gözlemlenebilirlik gibi dağıtık sistem gerçekleri için genişletin.
- Maliyeti bir mühendislik çıktısı sayın ve FinOps ile sürekli yönetin.

## Kaynaklar ve ileri okuma

- Adam Wiggins, *The Twelve-Factor App* (methodology).
- Brendan Burns, Joe Beda, and Kelsey Hightower, *Kubernetes Up & Running*.
- Bilgin Ibryam and Roland Huß, *Kubernetes Patterns*.
- Cornelia Davis, *Cloud Native Patterns*.
- J.R. Storment and Mike Fuller, *Cloud FinOps*.
- Liz Rice, *Container Security*.
- Cloud Native Computing Foundation (CNCF), cloud-native definition and landscape.
