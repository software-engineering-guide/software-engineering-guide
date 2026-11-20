# 3.1 Mimari temelleri

## Genel bakış ve motivasyon

[Yazılım mimarisi](https://en.wikipedia.org/wiki/Software_architecture), değiştirilmesi maliyetli olan önemli tasarım kararlarının bütünüdür: ana bileşenlerin yapısı, aralarındaki ilişkiler ve sistemin bütün olarak sergilemesi gereken nitelikler. Onu, birçok insanın tek bir tutarlı ürün inşa etmesini sağlayan ortak zihinsel model olarak düşünün. Küçük bir takımda mimari birkaç kişinin kafasında yaşayabilir ve yol boyunca gelişebilir. Büyük bir kurumda (yüzlerce mühendis, düzinelerce takım, birden çok ürün, yıllarca süren yol haritası) mimari, herkesin eşgüdümünü sağlayan şeye dönüşür. Net olduğunda takımlar birbirine çarpmadan bağımsız ilerler. Belirsiz olduğunda her takımlar arası bağımlılık bir pazarlığa, her olay bir arkeoloji projesine dönüşür.

Kurumlar ve kamu için temeller daha da önemlidir, çünkü sistemler uzun ömürlüdür, ağır biçimde düzenlenmiştir ve birimler arasında paylaşılır. Bir vergi sistemi, bir yardım platformu, bir ulusal sağlık kaydı ya da bir bankanın çekirdek defteri, onu inşa edenlerin kariyerlerinden daha uzun yaşayacaktır. Bağlaşım, veri sahipliği ve [kalite nitelikleri](https://en.wikipedia.org/wiki/List_of_system_quality_attributes) hakkında bugün verdiğiniz kararlar, on yıl ya da daha uzun süre neyin mümkün olduğunu sınırlar. Düzenleyiciler ve denetçiler giderek daha fazla belgelenmiş, savunulabilir bir mimari bekliyor: güvenilirliğin, güvenliğin, gizliliğin ve erişilebilirliğin sonradan eklenmediğini, baştan tasarlandığını gösteren kanıt. Temelleri doğru kurmak akademik bir mesele değildir. Yeni yetkilere uyum sağlayan bir platform ile sıfırdan yeniden inşa edilmesi gereken bir platform arasındaki farktır.

Bu bölüm, teknoloji modasından sağ çıkan kalıcı temelleri ele alır: kalite nitelikleri ("-ilikler"), mimari açıdan önemli gereksinimler, uygunluk işlevleri ve evrimsel mimari, [C4](https://en.wikipedia.org/wiki/C4_model) ve arc42 ile hafif belgeleme ve yapılandırılmış ödünleşim analizi. Bunlar, büyük bir takımın mimari üzerine tesadüfen değil, bilerek akıl yürütmesini sağlayan araçlardır.

## Temel ilkeler

- **Mimari, doğru cevaplarla değil, ödünleşimlerle ilgilidir.** Her önemli karar bir niteliği başka biriyle takas eder; iş, bu takasları bilerek ve şeffaf biçimde yapmaktır.
- **Kalite nitelikleri gereksinimdir.** Performans, erişilebilirlik, güvenlik ve bakım yapılabilirlik, özelliklerle aynı titizlikle belirtilmelidir; aksi halde son tarih baskısı altında feda edilirler.
- **Her gereksinim mimari açıdan önemli değildir.** Kıt tasarım dikkatini yapıyı şekillendiren, değiştirilmesi zor ya da riski yüksek gereksinimlere odaklayın.
- **Mimari evrilebilmelidir.** Büyük ön tasarım başarısız olur, çünkü bilgi başlangıçta en düşüktür; artımlı tasarlayın ve temel nitelikleri otomatik kontrollerle koruyun.
- **Yalnızca diyagramları değil, kararları belgeleyin.** Bir seçimin ardındaki gerekçe (ve reddedilen seçenekler), sonucun bir resminden daha değerlidir.
- **Mimariyi onu yaratmamış olanlar için okunabilir kılın.** Yeni katılanlar, denetçiler ve gelecekteki bakımcılar niyeti yeniden kurabilmelidir.
- **Erteleyebileceğiniz kararları erteleyin, vermeniz gerekenleri verin.** Değişimin ucuz olduğu yerde seçenekleri açık tutun; yalnızca geç bağlanmanın pahalı olduğu yerde erken bağlanın.

## Öneriler

### Kalite niteliklerini ölçülebilir senaryolar olarak belirtin

"Sistem hızlı olmalı" ya da "yüksek erişilebilirlikli" gibi belirsiz hedefler sınanamaz ve uygulatılamaz. Bunun yerine her kalite niteliğini bir uyaran, bir bağlam ve ölçülebilir bir yanıtla somut bir senaryo olarak yazın: "Eşzamanlı kullanıcı sayısı en yüksek noktada 50.000'e ulaştığında, arama isteklerinin %95'i 300 ms içinde tamamlanır." Alanınız için önemli olan nitelikleri kapsayın: erişilebilirlik, performans, ölçeklenebilirlik, güvenlik, bakım yapılabilirlik, gözlemlenebilirlik, erişilebilirlik (engelsizlik), taşınabilirlik ve maliyet verimliliği. Onları yüksek sesle sıralayın, çünkü hepsini aynı anda en üst düzeye çıkaramazsınız. En yüksek tutarlılık için ayarlanmış bir sistem aynı zamanda en yüksek erişilebilirliğe sahip olamaz.

### Mimari açıdan önemli gereksinimleri (MÖG) belirleyin

MÖG'leri sıradan gereksinimlerden ayırmak için zaman ayırın. Bir gereksinim, birçok bileşene dokunuyorsa, karşılanması pahalıysa, katı bir kısıt getiriyorsa ya da teknik olarak riskliyse mimari açıdan önemlidir. Düzenleyici yetkiler (veri ikametgahı, saklama, denetlenebilirlik), yüksek yük senaryoları, eski kayıt sistemleriyle entegrasyon ve sert güvenlik sınırları genellikle MÖG'dür. Bunların kısa, yaşayan bir listesini tutun ve büyük tasarım kararlarını bu listeye kadar izleyin; böylece inceleyiciler mimarinin neden böyle göründüğünü görebilir.

### Evrimsel mimariyi ve uygunluk işlevlerini benimseyin

Mimariyi sabit bir plan olarak değil, yönlendirilmiş yönlerde adım adım değişen bir şey olarak ele alın. **Uygunluk işlevi**, belirli bir mimari niteliğin ayakta kaldığını gösteren otomatik, nesnel bir testtir: hiçbir modülün yasaklı bir katmandan içe aktarma yapmadığını doğrulayan bir derleme zamanı kontrolü, p99 gecikmesi gerilerse boru hattını başarısız kılan bir performans testi, bilinen güvenlik açığı olan bağımlılıkları engelleyen bir güvenlik taraması, hiçbir hizmetin başka bir hizmetin veritabanına doğrudan bağlantısı olmadığını doğrulayan bir test. Uygunluk işlevleri mimari niyeti sürekli uygulanan korkuluklara dönüştürür: bu niyeti büyük, değişen bir takım boyunca canlı tutmanın tek yolu.

### C4 ve arc42 ile belgeleyin

Yapıyı dört yakınlaştırma düzeyinde (Sistem Bağlamı, Kapsayıcılar, Bileşenler ve Kod) anlatmak için **C4 modelini** kullanın; böylece her hedef kitle kendine uygun düzeyi okur ve hiçbir tek diyagramın her şeyi söylemesi gerekmez. Çevreleyen anlatı için **arc42**'yi şablon olarak kullanın: hedefler, kısıtlar, bağlam, çözüm stratejisi, yapı taşları, çalışma zamanı senaryoları, dağıtım, kesen ilgi alanları, kararlar ve riskler. Bireysel kararları kısa **[Mimari Karar Kayıtları (MKK)](https://en.wikipedia.org/wiki/Architectural_decision)** olarak tutun: bağlam, karar, durum ve sonuçlar; karar başına bir dosya, kodla birlikte sürümlenmiş. Yalnızca bir belgeleme alışkanlığı benimseyecekseniz MKK'ları seçin: büyük takımlar için başka her şeyden fazla karşılığını verirler.

### Yapılandırılmış ödünleşim analizi yapın ve tasarımı riske göre yönlendirin

Yüksek riskli sistemlerde, aday mimarileri öncelik sırasına konmuş kalite niteliği senaryolarına göre tartmak için **[Mimari Ödünleşim Analiz Yöntemi (ATAM)](https://en.wikipedia.org/wiki/Architecture_tradeoff_analysis_method)** gibi bir yöntem kullanın. Duyarlılık noktalarını (bir kararın tek bir niteliği güçlü biçimde etkilediği yerler) ve ödünleşim noktalarını (birkaçını etkilediği yerler) ortaya çıkarır. Daha hafif bir yaklaşım için **riske dayalı tasarımı** benimseyin: tasarım çabasını riskle orantılı harcayın. Düşük riskli, iyi anlaşılmış parçalar az törene ihtiyaç duyar. Yeni, yüksek etkili ya da geri döndürülemez kararlar prototipleri, keşif çalışmalarını ve resmi incelemeyi hak eder.

## Ödünleşimler: artılar ve eksiler

| Yaklaşım | Artılar | Eksiler |
|---|---|---|
| Ağır ön mimari | Eşgüdüm netliği; sabit kapsamlı programlarda daha az geç sürpriz | Bilginin en düşük olduğu anda alınan kararlar; yavaş; değişime karşı kırılgan |
| Beliren / evrimsel mimari | Öğrenmeye uyum sağlar; daha az israf; hızlı teslimi destekler | Uygunluk işlevleri olmadan sapma riski; güçlü mühendislik disiplini gerektirir |
| Resmi ATAM tarzı değerlendirme | Titiz, denetlenebilir, gizli çatışmaları ortaya çıkarır | Zaman ve uzmanlık yoğun; küçük değişiklikler için gereğinden fazla |
| Hafif MKK + C4 | Ucuz, okunabilir, artımlı, çok sayıda takıma ölçeklenir | Güncel tutma disiplini kadar iyi |

Temel gerilim, kesinlik ile uyarlanabilirlik arasındadır. Sabit fiyatlı kamu programları ve güvenlik açısından kritik sistemler, geç değişimin ya da başarısızlığın maliyeti çok büyük olduğu için daha fazla ön titizliğe ve resmi değerlendirmeye yönelir. Hızlı hareket eden ürün kuruluşları, otomasyonla korunan evrimsel yaklaşımlara yönelir. Çoğu büyük kurum ikisine de ihtiyaç duyar: geri döndürülemez, yüksek etkili kararlar ve kesen ilgi alanları için daha ağır yönetişim, diğer her yerde daha hafif, beliren tasarım. İki uç da kendi yoluyla başarısız olur: aşırı mimari yıllar harcatır ve hiçbir şey teslim etmez, yetersiz mimari ise ölçeklenemeyen ya da denetlenemeyen bir karmaşa üretir.

## Takımınızla tartışılacak sorular

1. **Kalite niteliklerinizden ikisi yük altında çatıştığında hangisi kazanır ve bu öncelik sırasını yazıya döktünüz mü?** Her mimari ödünleşim zorlar: azami tutarlılık erişilebilirliği zayıflatır, sıkı güvenlik gecikme ekler, agresif önbellekleme denetlenebilirlikle çatışır. Büyük bir takımda tehlike, farklı ekiplerin sessizce farklı öncelikler varsaymasıdır; biri verim için optimize ederken diğeri sıkı tutarlılığı korur ve çatışma yalnızca bir olay sırasında yüzeye çıkar. Kurumsal ve kamu ortamlarında bir düzenleyici hangi niteliği neden koruduğunuzu soracaktır, bu yüzden sıralama halk bilgeliği değil, açık ve savunulabilir olmalıdır. Kalite niteliği senaryolarınızı getirin ve sıra belirsizliğini yitirene kadar çift çift yüksek sesle birbirine karşı sıralayın. Sonra kazananı bir uygunluk işlevi olarak kodlayın; böylece öncelik, son tarih baskısı altında aşınmak yerine ayakta kalır.

2. **Son kararlarınızdan hangileri tek yönlü kapılardı ve çift yönlü kapılardan daha fazla inceleme gördü mü?** Riske dayalı tasarım, tasarım çabasını bir kararın geri alınmasının ne kadar zor olduğuyla orantılı harcamayı söyler; ancak çoğu takım her değişikliği kabaca aynı törenle inceler. Bu, ucuz ve geri döndürülebilir seçimlere dikkat harcatırken geri döndürülemez olanların (yasal bir kayda gömülmüş bir veri modeli, herkese açık bir API sözleşmesi, çekirdek bir veri deposu) yeterince sorgulanmadan geçmesine yol açar. Geçen çeyreğin önemli kararlarını çekin ve geri döndürülebilirliğe göre sıralayın, ardından geri döndürülemez olanların prototip, keşif çalışması ya da resmi inceleme alıp almadığını sorun. Uzun ömürlü kurumsal ve kamu sistemlerinde yanlış bir tek yönlü kapının maliyeti on yıl boyunca birikir, bu yüzden ek titizlik kat kat karşılığını verir. Sürecinizin ağırlığını, farkın boyutuna değil, kararın geri döndürülebilirliğine uydurun.

3. **Bir sonraki yüksek riskli, geri alınması zor kararınız için odada kimler olmalı ve seçenekleri hangi senaryolara göre puanlayacaksınız?** ATAM tarzı yapılandırılmış bir ödünleşim incelemesi, bir karar geri döndürülemez olduğunda ve aynı anda birkaç kalite niteliğine dokunduğunda maliyetini çıkarır; gücü de orada bulunan insanlardan gelir: teslimat, güvenlik, operasyon ve sonuçları hisseden politika ya da iş sahipleri. Bu seslerden birini atlarsanız çatışmayı inşadan sonra keşfedersiniz; örneğin bir önbellekleme seçiminin sessizce bir denetlenebilirlik gereksinimini bozması gibi. Öncelik sırasına konmuş kalite niteliği senaryolarını puanlama rubriği olarak getirin ve bir seçeneğin tek bir niteliği sert biçimde salladığı duyarlılık noktalarını ve birkaçını birden oynattığı ödünleşim noktalarını arayın. İstediğiniz çıktı, reddettiğiniz seçenekleri ve nedenlerini kaydeden kısa bir MKK'dır; böylece gerekçe, onu üretenlerden daha uzun yaşar. Yaklaşan hiçbir karar buna değer görünmüyorsa, bunun kendisi kontrol etmeye değerdir; çünkü ufukta hiç geri döndürülemez kararı olmayan büyük bir program genellikle yeterince ileriye bakmıyordur.

4. **Yeni katılan biri ya da dış bir denetçi yalnızca yazılı mimarinize sahip olsa, sistemin neden bu biçimde olduğunu yeniden kurabilir mi ve bunu en son ne zaman sınadınız?** Birkaç kıdemli kişinin kafasında yaşayan mimari tek bir arıza noktasıdır: bu kişiler ayrıldığında, geri alınması zor her kararın ardındaki gerekçe de onlarla gider ve sonraki takım bunu olaylar yoluyla yeniden öğrenir. Büyük bir kurum için mimarinin okunabilirliği (gerçeği yansıtan C4 diyagramları, bir arc42 anlatısı, reddedilen seçenekleri kaydeden MKK'lar), düzinelerce takımın toplantı yapmadan aynı sistem hakkında akıl yürütmesini sağlayan şeydir. Yakın tarihli bir MKK'yı ve güncel bir diyagramı getirin, bileşeni inşa etmemiş birine verin ve bir insana sormak zorunda kalmadan ne kadar ilerlediğini izleyin. Kurumsal ve kamu ortamlarında bir denetçi tam olarak bu alıştırmayı yapacaktır ve geçen yılın sistemini anlatan belgeleme hiç olmamasından kötüdür, çünkü onu onaylaması gereken kişileri yanıltır. Yazılı kaydın tazeliğini ölçülebilir bir nitelik olarak ele alın ve onu doğru tutmanın arkasına bir uygunluk işlevi ya da bir inceleme takvimi koyun.

5. **Mimari niteliklerinizden hangileri bugün otomatik bir uygunluk işleviyle korunuyor ve hangileri hâlâ herkesin kuralı hatırlamasına güveniyor?** Yalnızca bir wiki sayfasında ya da bir inceleyicinin hafızasında yaşayan niyet, son tarih geldiği anda aşınır; çünkü katmanlama kuralı, ortak veritabanı olmayan sınır ve gecikme bütçesi tam olarak takımların baskı altındayken kıstığı şeylerdir. Büyük, hızlı değişen bir kod tabanında hayatta kalan tek niyet, bir derlemenin uygulattığı niyettir; bu yüzden iddia ettiğiniz nitelikler ile gerçekten denetlediğiniz nitelikler arasındaki boşluk, gerçek mimari riskinizdir. Önemli niteliklerinizi listeleyin, her birini uygulanan, elle incelenen ya da korumasız olarak işaretleyin ve bir incelemenin, bir uygunluk işlevinin daha erken yakalayabileceği bir sapmayı yakaladığı son üç durumu getirin. Düzenlenen ve kamusal sistemlerde bu iki kat önemlidir, çünkü bir düzenleyici veri ikametgahını ya da denetlenebilirliği niyetlenip niyetlemediğinizi değil, bunun sürekli korunduğunu nasıl kanıtladığınızı soracaktır ve yeşil bir boru hattı bir politika belgesinden çok daha güçlü bir cevaptır. Başarısızlığı hem olası hem pahalı olan nitelikleri otomatikleştirmeye öncelik verin ve bazılarının elle kalacağını kabul edin.

6. **Bir gereksinimin mimari açıdan önemli olup olmadığına karar verirken bu kararı kim veriyor ve MÖG listesinin her şey ya da hiçbir şey olmasını nasıl önlüyorsunuz?** Mimari açıdan önemli gereksinimleri adlandırmanın değeri seçiciliğinden gelir: her gereksinimi önemli saydığınızda tasarım durur, hiçbirini saymadığınızda yapısal, riskli ve değiştirmesi zor olanlar korumasız geçer. Büyük bir takımda eğilim, her ekibin yerel olarak karar vermesine izin vermektir; bu da tutarsız çıtalar ve bir grubun "küçük" seçiminin başka bir grubun yapısını kısıtladığı takımlar arası sürprizler üretir. Güncel MÖG listenizi, kullandığınız ölçütleri (birçok bileşene dokunur, karşılanması pahalıdır, katı kısıt, teknik olarak riskli) ve sınırı yüksek sesle sınamak için birkaç sınırda gereksinimi getirin. Kurumlar ve kamu için veri ikametgahı, saklama ve denetlenebilirlik gibi düzenleyici yetkiler neredeyse her zaman önemlidir ve pazarlık konusu değildir; bu yüzden listenin kime ait olduğunu, nasıl incelendiğini ve bir MÖG ekleme ya da çıkarma kararının nasıl kaydedildiğini belirtin, çünkü kimsenin yönetmediği bir MÖG, titiz incelemede kimsenin savunmayacağı bir gereksinimdir.

## Sektör merceği

**Girişim.** Töreni sıfıra yakın, kaydı eksiksize yakın tutun. Resmi ATAM çalıştaylarını ve ağır şablonları atlayın, ancak geri almanın acı vereceği seçimler (veri deposu, monolit ya da hizmetler, kimlik doğrulama sağlayıcısı) için yine de bir düzine kısa MKK yazın ve ilk müşterilerinizin gerçekten hissettiği iki üç kalite niteliği senaryosunu sabitleyin. Kıt kaynağınız mühendislik dikkatidir; bu yüzden yalnızca başarısızlığı sizi batıracak nitelikleri, örneğin kiracı yalıtımını koruyun ve geri kalan her şeyin beliren ve değiştirmesi ucuz kalmasına izin verin.

**Küçük işletme.** Özel bir mimar ve dar bir bütçe olmadan, neredeyse hiçbir şeye mal olmayan temellere yaslanın: bir avuç kalite niteliğinizi somut sayılar olarak adlandırın, geri almakta zorlanacağınız her şey için MKK yazın ve ağır yapısal kararları seçtiğiniz platformun ya da satıcının taşımasına izin verin. Özel altyapı inşa etmek yerine iyi desteklenen bir yığın satın almayı tercih edin ve satıcının belgelenmiş mimarisini sıfırdan yazmanız gereken bir şey değil, miras aldığınız bir kısıt olarak görün.

**Kurumsal.** Zorluk, birçok takım ve yıllarca süren yol haritası boyunca tutarlılıktır; bu yüzden paylaşılan makineye yatırım yapın: bir mimari loncası, ortak bir kalite niteliği senaryoları kümesi, kodun yanında saklanan MKK'lar ve hiçbir tek inceleyicinin ölçekte denetleyemeyeceği sınırları uygulatan CI'daki uygunluk işlevleri. Geri döndürülemez, kesen kararlar için yapılandırılmış ödünleşim analizi kullanın, C4 diyagramlarını tasarım incelemelerinde ortak harita olarak tutun ve MÖG listesini merkezden yönetin; böylece gruplar küresel düzeyde çarpışan yerel olarak makul seçimler yapmayı bırakır.

**Kamu.** Uzun ömürlü, düzenlenen sistemler, belgelenmiş ve savunulabilir mimariyi bir incelik değil, bir satın alma ve hesap verebilirlik gereksinimi yapar. Veri ikametgahını, saklamayı, denetlenebilirliği ve erişilebilirliği, denetçilerin doğrudan okuyabileceği bir arc42 tanımına yazılmış mimari açıdan önemli gereksinimler olarak ele alın ve çatışmaların (örneğin önbellekleme ile denetlenebilirlik) koddan önce kağıt üzerinde ortaya çıkması için politika ve güvenlik yetkililerini içeren hafif ödünleşim çalıştayları yapın. Gerekçe izini, hesap verebilir bir yetkilinin gereken özeni gösterebileceği kadar eksiksiz tutun ve bir kamu kurumunu on yıl boyunca tek bir satıcıya kilitleyenler yerine net çıkış seçenekleri olan mimarileri tercih edin.

## Örnekler

**Girişim.** Altı kişilik, tohum aşamasındaki bir SaaS takımı mimarisini resmi bir süreç yerine paylaşılan bir belgede tutuyor, ama geri almanın acı vereceği kararları yine de yazıya döküyor. Yaklaşık bir düzine MKK kaydediyorlar (neden bir belge deposu yerine Postgres, neden hizmetler yerine modüler bir monolit, neden o kimlik doğrulama sağlayıcısını seçtikleri) ve erken müşteriler için gerçekten önemli olan iki kalite niteliği senaryosunu sabitliyorlar: "bir kayıt iki saniyenin altında tamamlanır" ve "hiçbir müşteri başka bir kiracının verisini asla okuyamaz." Yedinci ve sekizinci mühendisleri işe aldıklarında, bu notlar yeni gelenlerin işlerin neden böyle olduğunu sormak için herkesi bölmek yerine ilk haftalarında sevkiyat yapmasını sağlıyor.

**Kurumsal.** Çok uluslu bir banka on iki bölgesel ödeme sistemini birleştiriyor ve küçük bir mimari loncası kuruyor. Lonca sekiz kalite niteliği senaryosu tanımlıyor (bunlar arasında "sıfır kayıp işlemle saniyede 10.000 işlem işle" ve "bir bölgeyi 15 dakika içinde kurtar" var), yaklaşık kırk MKK topluyor ve CI'da ([sürekli entegrasyon](https://en.wikipedia.org/wiki/Continuous_integration)) uygunluk işlevlerini uygulatıyor: hiçbir hizmet başka bir alanın veritabanına yazamaz, tüm hizmetler arası çağrılar izlenmelidir ve kritik bir [CVE](https://en.wikipedia.org/wiki/Common_Vulnerabilities_and_Exposures) (Common Vulnerabilities and Exposures) içeren herhangi bir bağımlılık derlemeyi başarısız kılar. C4 bağlam ve kapsayıcı diyagramları her tasarım incelemesinde ortak harita oluyor ve takımlar arası entegrasyon anlaşmazlıkları keskin biçimde azalıyor.

**Kamu.** Ulusal bir kurum bir yardım platformunu modernleştiriyor ve yasa ondan veri ikametgahını, yedi yıllık denetlenebilirliği ve erişilebilirlik uyumunu garanti etmesini istiyor. Mimarları bunları MÖG olarak ele alıp denetçilerin doğrudan incelediği bir arc42 tanımına yazıyor. İki aday mimariyi karşılaştırmak için teslimat takımları, güvenlik ve politika yetkilileriyle hafif bir ATAM çalıştayı yürütüyorlar ve tercih edilen tasarımın önbellekleme stratejisinin denetlenebilirlik gereksinimiyle çatıştığını keşfediyorlar. Bu ödünleşimi tek satır kod yazılmadan, kağıt üzerinde yakalamak aylarca süren yeniden işi önlüyor ve hesap verebilir bakana gereken özenin belgelenmiş kanıtını sağlıyor.

## İş gerekçesi: motivasyonlar, YG ve TSM

Mimari temellerin getirisi çoğunlukla kaçınılan maliyettir; bu da onları yetersiz finanse etmeyi kolay, atlamayı pahalı kılar. Benimsemenin maliyeti mütevazıdır: bir avuç deneyimli mimarın zamanı, birkaç çalıştay, bir belgeleme şablonu ve uygunluk işlevlerine biraz CI yatırımı; genellikle bir programın bütçesinin küçük, tek haneli bir yüzdesi. Benimsememenin maliyeti daha sonra ve ek bedelle gelir: belirtilmemiş bir kalite niteliği üretimde başarısız olduğunda yeniden iş, belgelenmemiş bir bağlaşım zorunlu bir değişikliği engellediğinde acil yeniden platformlama, kimse sistemi anlamadığı için uzayan olaylar ve teslimatı durduran ya da para cezası doğuran başarısız denetimler.

Yönetim için gerekçeyi seçenek değeri ve risk etrafında kurun. İyi mimari temeller, gelecekteki değişimin maliyetini düşürür (on yıllık bir sistem ömrü boyunca teslimat hızı ve toplam sahip olma maliyeti üzerinde doğrudan bir kaldıraç), ciddi olayların ne sıklıkta ve ne kadar uzun sürdüğünü azaltır ve düzenleyicilerin ve denetçilerin artık talep ettiği belgeleme izini üretir. MKK alışkanlığı tek başına, yeni bir yönetim ekibi "bunu neden böyle inşa ettik?" diye sorduğunda ve adli bir soruşturma yerine dakikalar içinde bir cevap aldığında ilk seferde karşılığını verir. Yapabildiğiniz yerde sayılarla destekleyin: kaçınılan bir büyük yeniden mimarinin ya da kaçınılan bir başarısız denetimin maliyetini, uygulamaların küçük süregelen maliyetiyle tartın.

## Anti-kalıplar ve tuzaklar

- **Fildişi kule mimarisi.** Diyagramlar üreten ama koda hiç dokunmayan ya da teslimat takımlarıyla konuşmayan mimarlar; tasarımları görmezden gelinir ya da inşa edilemez.
- **Sıfat olarak kalite nitelikleri.** Sayı yok, senaryo yok ve dolayısıyla doğrulama ya da takas yolu olmayan "ölçeklenebilir, güvenli, güvenilir".
- **Büyük ön tasarım.** Anlayışın en zayıf olduğu anda kararları kilitleyerek, ilk satır koddan önce her ayrıntıyı bağlamak.
- **Yalan söyleyen belgeleme.** Geçen yılın sistemini anlatan diyagramlar; yanılttıkları için hiç olmamasından kötü.
- **Özgeçmiş güdümlü tasarım.** Teknolojileri MÖG'leri karşılamak için değil, kariyer yapmak için seçmek.
- **Altın kaplama.** Gereksinimlerin hiç istemediği ölçek, esneklik ya da genellik için mühendislik yapmak; kalıcı olarak maliyet ve karmaşıklık eklemek.
- **Mimari korkuluk yokluğu.** Büyük bir takım boyunca yapıyı korumak için uygunluk işlevleri yerine iyi niyetlere güvenmek.

## Olgunluk modeli

- **Düzey 1, Başlangıç.** Mimari örtüktür ve bireylerin kafasında yaşar. Belgelenmiş kalite niteliği yok, MKK yok, paylaşılan diyagram yok. Yapı olaylar sırasında keşfedilir ve her takımlar arası bağımlılık sıfırdan yeniden pazarlık edilir.
- **Düzey 2, Geliştirme.** Bazı takımlar geri almanın acı vereceği kararları yazıya döker ve temel diyagramları çizer, ama uygulama tutarsızdır: bir ekip MKK tutarken diğeri hiç tutmaz, kalite nitelikleri ölçülebilir senaryolar yerine sıfatlarla adlandırılır ve belgeleme projeler arasında eskir.
- **Düzey 3, Standartlaştırma.** Kalite niteliği senaryoları ve mimari açıdan önemli gereksinimler, kurum geneli belgelenmiş bir standarda göre belirtilir ve önceliklendirilir. MKK'lar rutindir ve kodun yanında saklanır, C4 ve arc42 belgelemesi ortak bir şablona göre sürdürülür ve her takımda önemli kararlar için yapılandırılmış ödünleşim incelemeleri zorunludur.
- **Düzey 4, Yönetme.** Mimari, iddia edilmek yerine temel çizgilere göre ölçülür. CI'daki uygunluk işlevleri p99 gecikmesi, katman ihlalleri, izlenmeyen çağrılar ve savunmasız bağımlılıklar gibi nitelikleri raporlar; MKK kapsamı ve belgeleme tazeliği metrik olarak izlenir; ödünleşim incelemeleri seçenekleri öncelik sırasına konmuş senaryolara göre puanlar ve kararlaştırılan temel çizgilerden sapma bir sürpriz yerine tanımlı bir yanıtı tetikler. Denetçiler yalnızca anlatıya değil, ölçülmüş kanıta güvenebilir.
- **Düzey 5, Orkestrasyon.** Mimari, tüm kurum boyunca sürekli ve uyarlanabilir biçimde evrilir. Uygunluk işlevi ve olay verisi, hangi niteliklerin önemli olduğunu ve tasarım çabasının nereye gittiğini besler; MÖG listeleri, kalite niteliği öncelikleri ve korkuluklar yetkiler ve risk değiştikçe yeniden kapsamlandırılır; uygulama teslimat, güvenlik ve risk planlamasıyla bütünleşiktir, böylece platform sıfırdan yeniden inşa edilmek yerine yeni gereksinimlere uyum sağlar.

## Tartışma fikirleri

1. En kritik sisteminiz için hangi üç kalite niteliği gerçekten pazarlık konusu değil ve her birini bugün ölçülebilir bir senaryo olarak ifade edebilir misiniz?
2. Bir kararın bir MKK'yı hak edecek kadar "mimari açıdan önemli" olup olmadığına, yalnızca yapıp geçmeye karşı nasıl karar veriyorsunuz?
3. Uygunluk işlevleri, mevcut kod incelemenizin kaçırdığı sapmayı nerede yakalardı?
4. Kurumunuz aşırı mı yoksa yetersiz mi mimari yapıyor ve hangisi olduğunu hangi kanıt söylüyor?
5. Takımların takımı yapısında mimariden kim sorumlu ve hem fildişi kulelerden hem tam anarşiden nasıl kaçınıyorsunuz?
6. Dış bir denetçi, bugün yazılı olanlardan mimarinizin niyetini nasıl yeniden kurardı?

## Önemli çıkarımlar

- Mimari, tersine çevirmesi pahalı kararların bütünüdür; bu ödünleşimleri bilerek yapın ve kaydedin.
- Kalite niteliklerini ölçülebilir senaryolar olarak belirtin ve yapıyı şekillendiren mimari açıdan önemli gereksinimleri belirleyin.
- Artımlı tasarlayın ve temel mimari nitelikleri otomatik uygunluk işlevleriyle koruyun.
- C4 diyagramları, bir arc42 anlatısı ve kodun yanında tutulan karar başına MKK'larla hafif ama doğru biçimde belgeleyin.
- Titizliği riske uydurun: geri döndürülemez, yüksek etkili kararlar için ağır analiz; diğer her yerde hafif süreç.
- İş gerekçesi, kaçınılan yeniden iş, kısalan olaylar, daha hızlı gelecekteki değişim ve denetime hazır kanıttır.

## Kaynaklar ve ileri okuma

- Len Bass, Paul Clements, and Rick Kazman, *Software Architecture in Practice*
- Neal Ford, Rebecca Parsons, and Patrick Kua, *Building Evolutionary Architectures*
- Simon Brown, *Software Architecture for Developers* (and the C4 model)
- Mark Richards and Neal Ford, *Fundamentals of Software Architecture*
- George Fairbanks, *Just Enough Software Architecture: A Risk-Driven Approach*
- Michael Nygard, "Documenting Architecture Decisions" (the ADR pattern)
- Gernot Starke and Peter Hruschka, *arc42* documentation template
- Paul Clements et al., *Evaluating Software Architectures: Methods and Case Studies* (ATAM)
- ISO/IEC 25010, *Systems and software quality models*
