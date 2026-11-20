# 2.4 Test stratejisi

## Genel bakış ve motivasyon

Bir [test](https://en.wikipedia.org/wiki/Software_testing) stratejisi, takımınızın kodu bozmadan hızlı değiştirebilmesi için neyin, hangi düzeyde, ne kadar otomatik ve hangi güven düzeyinde test edileceğine dair bilinçli seçimler kümesidir. Testler, büyük bir kuruluşun sık ve güvenle dağıtım yapmasını sağlayan şeydir. Beklenen davranışı kodlar, gerilemeleri yakalar ve mühendislere [yeniden düzenleme](https://en.wikipedia.org/wiki/Code_refactoring) güveni verir. Tutarlı bir strateji olmadan test genellikle iki kötü yoldan birine gider: yok (korku güdümlü, yavaş ilerleyen geliştirme) ya da şişkin (kimsenin güvenmediği binlerce yavaş, kararsız test).

Büyük bir takım için strateji, herhangi tek bir testten daha önemlidir. Paylaşılan bir kod tabanında çalışan yüzlerce mühendis hızlı, güvenilir bir güvenlik ağına ihtiyaç duyar. Bu olmadan her değişiklik risklidir ve her sürüm elle yapılan bir çileye dönüşür. Testler ayrıca amaçlanan davranışın çalıştırılabilir belgesi olarak da iş görür; özgün yazarlar ayrıldıktan sonra paha biçilmezdir. Strateji, test takımınızın teslimatı hızlandıran bir varlık mı yoksa yavaşlatan bir yük mü olacağına karar verir.

Kurumsal ve kamu bağlamlarında test ek ağırlık taşır. Düzenlemeler belgelenmiş test kapsamı ve kanıt gerektirebilir. Güvenlik açısından kritik ve vatandaşa dönük sistemler yüksek güvence ister. Erişilebilirlik ve güvenlik testi yasal olarak zorunlu olabilir. Bu yüzden strateji hızı, güveni, maliyeti ve uyumu dengelemeli ve kapsamı oyunlaştırılacak bir hedef değil, bir sinyal olarak ele almalıdır.

## Temel ilkeler

- Bir sayıya ulaşmak için değil, değiştirme güveni kazanmak için test edin.
- Hızlı, güvenilir, yalıtılmış testleri tercih edin. Yavaş ya da kararsız testler, bir takımı yararlı kılan güveni aşındırır.
- Testleri gerçek güven veren en düşük düzeye itin ve yavaş, geniş testleri gerçek entegrasyon riskine saklayın.
- Kararsız bir test bozuk bir testtir. Kararsızlığı birinci sınıf kusur olarak ele alın.
- Kapsam bir sinyaldir, hedef değil. Önemsiz kodun yüksek kapsamı çok az şey kanıtlar.
- Testleriniz yeniden düzenlemeden sağ çıksın diye gerçekleştirim ayrıntılarını değil, davranışı ve sözleşmeleri test edin.
- İşlevsel olmayan testi (erişilebilirlik, performans, güvenlik) stratejinin parçası yapın, sonradan düşünce değil.

## Öneriler

### Test piramidini varsayılan olarak kullanın ve eleştirilerini bilin

Çok sayıda hızlı [birim testi](https://en.wikipedia.org/wiki/Unit_testing), daha az [entegrasyon testi](https://en.wikipedia.org/wiki/Integration_testing) ve az sayıda uçtan uca test varsayılan olsun; çünkü kapsam büyüdükçe maliyet ve kırılganlık artar. Eleştirileri de bilin: biçim dogmayı değil mimarinizi izlemeli. Hizmet ağırlıklı bir sistem daha büyük bir entegrasyon katmanı gerektirebilir ("test kupası") ve gerçek amaç belirli bir siluet değil, maliyet ve hız birimi başına güvendir. Ne yaparsanız yapın, çoğunlukla yavaş uçtan uca testlerden oluşan ters piramitten kaçının.

### TDD, BDD ve belirtim güdümlü geliştirmeyi yardımcı oldukları yerde benimseyin

Tasarımı yönlendirmek ve sınanabilirliği garanti etmek için, özellikle karmaşık mantıkta, [test güdümlü geliştirmeyi](https://en.wikipedia.org/wiki/Test-driven_development) (TDD) kullanın. Bir test disiplini kadar bir tasarım disiplinidir. Testleri paydaşlarla paylaştığınız alan dilinde ifade etmek için [davranış güdümlü geliştirmeyi](https://en.wikipedia.org/wiki/Behavior-driven_development) (BDD) kullanın; bu, düzenlemeye tabi ya da gereksinim ağırlıklı ortamlarda kabul ölçütleri için değerlidir. Belirtim güdümlü geliştirme bir adım daha ileri gider: çalıştırılabilir bir belirtimi (örneklerle ifade edilen üzerinde uzlaşılmış davranış) hem gerçekleştirimi yönlendiren hem doğrulayan tek doğruluk kaynağı olarak ele alır. Bu, gereksinimlerin kabul kanıtına izlenebilir olması gereken yerlerde, kamu ve düzenlemeye tabi programlarda olduğu gibi parlar. Üçüyle de ilgili olan **[sola kaydırılmış test](https://en.wikipedia.org/wiki/Shift-left_testing)**: doğrulamayı yaşam döngüsünün mümkün olduğunca erken bir noktasına taşımak, testleri kodla birlikte ya da önce yazmak ve sürekli çalıştırmak; böylece kusurları, geç test aşamalarında ya da üretimde değil, düzeltmesi en ucuz olduğu zaman yakalarsınız. Bunların hiçbiri her yerde zorunlu değildir. Netlik kattıkları yerde uygulayın.

### Yüksek değerli kod için gelişmiş teknikler kullanın

Çok sayıda üretilmiş girdi üzerinde değişmezleri denetlemek için özellik tabanlı testi kullanın; örnek tabanlı testlerin kaçırdığı uç durumları yakalar. Çökmeleri ve güvenlik kusurlarını bulmak için ayrıştırıcılarda ve güvenilmeyen girdi sınırlarında [bulanık testi](https://en.wikipedia.org/wiki/Fuzzing) kullanın. Testlerinizin enjekte edilmiş hataları gerçekten algılayıp algılamadığını ölçmek için [mutasyon testini](https://en.wikipedia.org/wiki/Mutation_testing) kullanın; ham kapsamdan çok daha iyi bir kalite sinyalidir. Serileştirilmiş çıktı için anlık görüntü testini ölçülü kullanın ve anlık görüntüleri körü körüne yeniden onaylama tuzağına dikkat edin.

### Test verisini yönetin ve sentetik veri kullanın

Testleri kontrollü, yalıtılmış test verisiyle deterministik yapın ve testleri birbirine bağlayan paylaşılan değişken fikstürlerden kaçının. Gerçek kişisel bilgiyi açığa çıkarmadan üretim özelliklerini yansıtan [sentetik veri](https://en.wikipedia.org/wiki/Synthetic_data) üretin; gizlilik kurallarının üretim verisinin test ortamlarında kullanılmasını yasakladığı yerde bu şarttır. Her testin tam ihtiyaç duyduğu veriyi inşa edebilmesi için fabrikalar ya da oluşturucular sağlayın.

### Kararsız testleri kusur olarak ele alın

Kararsızlığı otomatik algılayın, kararsız testleri engelleyici yoldan çıkarın ve bir son tarihe kadar düzeltin ya da silin. Rastgele başarısız olan bir takım, mühendisleri hataları görmezden gelmeye alıştırır; bu da bütün değerini yok eder. Kararsızlık oranlarını izleyin ve güvenilirliği test takımının kendisi için açık bir kalite metriği yapın.

### Kapsamı sinyal olarak kullanın ve işlevsel olmayan test ekleyin

Test edilmemiş alanları bulmak için kapsamı ölçün, ama onu iddiasız testlerle oyunlaştırmayı davet eden katı bir hedefe dönüştürmeyin. Derinlik için mutasyon testiyle tamamlayın. Erişilebilirlik testini (otomatik kontroller artı elle denetimler), performans testini (yük ve gecikme temel çizgileri ve gerileme algılama) ve güvenlik testini (bağımlılık taraması, [statik analiz](https://en.wikipedia.org/wiki/Static_program_analysis) ve dinamik test) hatta yerleştirin.

## Ödünleşimler: artılar ve eksiler

| Test türü / uygulama | Artılar | Eksiler |
|---|---|---|
| Birim testleri | Hızlı, kesin, ucuz, kararlı | Entegrasyon ve sistem düzeyi hataları kaçırır |
| Entegrasyon testleri | Arayüz ve bağlantı kusurlarını yakalar | Daha yavaş; daha çok kurulum; daha kırılgan |
| Uçtan uca testler | Gerçek davranışta en yüksek güven | Yavaş, kararsız, sürdürmesi pahalı |
| TDD | Daha iyi tasarım, garantili sınanabilirlik | Öğrenme eğrisi; başta yavaş hissettirir |
| Özellik tabanlı test | Uç durumları bulur, değişmezleri kodlar | Özellik düşünmeyi gerektirir; yazması daha zor |
| Mutasyon testi | Test etkinliğinin gerçek ölçüsü | Hesaplama açısından pahalı; çalışması yavaş |
| Yüksek kapsam hedefi | Test edilmemiş kodu görünür kılar | Oyunlaştırılabilir; düşük değerli testleri özendirebilir |

Merkezi ödünleşim güven ile hız ve maliyet arasındadır. Daha geniş testler daha fazla güven verir ama daha yavaş çalışır ve daha sık bozulur. Daha dar testler hızlı ve kararlıdır ama sistem düzeyi kusurları kaçırır. Doğru karışım, geri bildirimin saniyesi ve bakımın saati başına güveni en üst düzeye çıkarır. Ve aşırı test gerçek bir başarısızlık biçimidir: gereksiz, yavaş, kırılgan testlerden oluşan şişkin bir takım, önlediği hatalardan daha pahalıya mal olabilir.

## Takımınızla tartışılacak sorular

1. **Hangi işlevsel olmayan testler, erişilebilirlik, performans ve güvenlik, bir sürümü engellemeli ve hangileri yalnızca raporlamalı?** Bu bölüm işlevsel olmayan testin sonradan düşünce olarak değil stratejinin içinde olması gerektiğini savunur ve erişilebilirliğin yasal olarak zorunlu olabileceğini, güvenlik testinin çalışma yetkisi kanıtının parçası olabileceğini not eder. Büyük ya da vatandaşa dönük bir sistem için engelleyen bir kapı teslimatı yavaşlatır, ama üretimde bulunan bir erişilebilirlik ya da güvenlik kusurunun düzeltme, itibar ve yasal maliyeti testi gölgede bırakır. Karar veren sinyalleri getirin: düzenleyici maruziyetiniz, sistemin vatandaşa dönük olup olmadığı ve bu kusurların şu anda ne sıklıkla üretime kaçtığı. Yasal olarak zorunlu kontrolleri engelleyici yapın ve daha düşük riskli kontrollerin bir eğilimle raporlamasına izin verin; böylece kapı dogmayı değil gerçek riski yansıtsın. Cevap neyin birleşip neyin birleşemeyeceğini doğrudan belirler.

2. **Kapı olarak sabit bir kapsam yüzdesi belirliyor musunuz ve belirliyorsanız mühendislerin onu iddiasız testlerle oyunlaştırmasını ne engeller?** Bölüm kapsamın bir sinyal olduğu, hedef olmadığı, önemsiz kodun yüksek kapsamının çok az şey kanıtladığı ve sabit bir hedefin oyunlaştırmayı davet ettiği konusunda katıdır. Büyük bir kuruluşa dayatılan tek bir sayı güvenilir biçimde hiçbir şey iddia etmeden kodu çalıştıran testler üretir; bu da metriği yükseltir ve gerçek güveni düşürür. Tartışmaya daha iyi bir sinyal getirin: testlerin enjekte edilmiş hataları gerçekten algılayıp algılamadığını ölçen, en yüksek değerli modülleriniz üzerinde bir mutasyon testi puanı. Test edilmemiş alanları bulmak için kapsamı, derinlik için mutasyon testini kullanın ve ikisinden birini liderliğin tek başına izlediği bir hedefe dönüştürmeye direnin. Sayının nerede gerçekten yardımcı olduğuna ve nerede yalnızca tiyatroyu davet ettiğine karar verin.

3. **Test takımı mühendislerin beklemeyeceği kadar yavaşladığında politikanız nedir?** Bu bölümün merkezi ödünleşimi güven ile hız ve maliyet arasındadır ve aşırı testi, şişkin, gereksiz, yavaş bir takımın önlediği hatalardan daha pahalıya mal olduğu gerçek bir başarısızlık biçimi olarak adlandırır. Büyük bir takımda takım çalışma süresi her değişiklikte ödenen paylaşılan bir vergidir ve insanların aşmayı öğrendiği bir takım tüm değerini kaybeder. Kanıtı getirin: CI duvar saati süresi, en yavaş testler ve gereksiz uçtan uca kapsamın daha ucuz birim testlerini ne kadar kopyaladığı. Testleri gerçek güven veren en düşük düzeye itin, paralelleştirin ve gereksiz yavaş testleri bir son tarihe kadar silin. Amaç ham test sayısı değil, geri bildirimin saniyesi başına güveni optimize etmektir.

4. **Bir test kararsızlaştığında kimin sorumluluğunda, ne kadar hızlı düzeltilmesi ya da silinmesi gerekir ve bu son tarihi ne zorlar?** Bu bölüm kararsız bir testi bozuk bir test, birinci sınıf bir kusur olarak ele alır; çünkü rastgele başarısız olan bir takım büyük bir takımı kırmızı derlemeleri görmezden gelmeye alıştırır ve herkesin bağımlı olduğu güvenlik ağını sessizce yok eder. Karşıt baskı gerçektir: kararsız bir testi karantinaya almak teslimatı bugün serbest bırakır ama gerçek bir aralıklı hatayı maskeleme riski taşır; üzerinde engellemek ise saf gürültü olabilecek bir başarısızlık yüzünden yüzlerce mühendisi durdurur. Meseleyi çözen kanıtı getirin: mevcut kararsızlık oranınız, testlerin biri dokunmadan önce ne kadar süre karantinada durduğu ve karantinaya alınan kaç testin gerçek bir kusuru gizlediği. Karantinadaki her teste bir sahip atayın, düzeltme ya da silme için kesin bir son tarih koyun ve güvenilirliği takımın kendisi için açık bir metrik olarak izleyin. Yeşil bir derlemenin sürüm kanıtının parçası olduğu kurumsal ve kamu ortamlarında, yönetilmeyen bir karantina yığını aynı zamanda bir denetim yükümlülüğüdür, çünkü özel olarak güvenmemeyi kabul ettiğiniz bir sinyalle yayımlıyorsunuz.

5. **Test ortamlarında üretim verisi kullanmanıza izin var mı ve yoksa gerçek kusurları yakalayacak kadar sadık sentetik veriyi nasıl üreteceksiniz?** Bölüm, gizlilik kurallarının çoğu zaman testte gerçek kişisel veriyi yasakladığı ve sentetik verinin üretim özelliklerini yansıtması gerektiği, aksi halde testlerinizin yanlış güven verdiği konusunda doğrudandır. Büyük bir kuruluş için gerilim sadakat ile uyum arasındadır: üretim verisi sentetik verinin kaçırdığı dağınık uç durumları yakalar, ama her kopyası maruziyetinizi ve yükümlülüklerinizi çoğaltır. Ayrıntıları getirin: hangi veri kümeleri kişisel ya da düzenlemeye tabi veri taşıyor, gizlilik ve veri ikameti kurallarınızın gerçekte ne gerektirdiği ve mevcut fikstürlerinizin üretimde görülen dağılımları ve uç durumları ne kadar iyi yeniden ürettiği. Her testin tam ihtiyaç duyduğu veriyi inşa etmesi için fabrikaları ya da oluşturucuları standartlaştırın ve gerçek demografik ve hacim dağılımlarıyla eşleşen sentetik üretime yatırım yapın. Kamu ve düzenlemeye tabi programlarda vatandaş verisini bir test ortamında kullanmak bir kısayol değil, raporlanabilir bir ihlaldir; bu yüzden veri stratejisi ilk ortam kurulmadan önce çözülmelidir.

6. **TDD, BDD ya da belirtim güdümlü geliştirme nerede isteğe bağlı değil, beklenen olmalı ve kim karar verir?** Bu bölüm bunları her kod satırı için zorunluluklar değil, netlik kattıkları yerde uygulanacak disiplinler olarak sunar; yine de büyük bir takım paylaşılan bir varsayılandan yararlanır ki uygulama takım takım parçalanmasın. Ödünleşim, tasarım ve izlenebilirlik faydaları (politika uzmanlarının inceleyebileceği çalıştırılabilir belirtimler, yeniden düzenlemeden sağ çıkan testler) ile genel bir zorunluluğun ters tepmesine yol açan gerçek öğrenme eğrisi ve baştaki yavaşlık arasındadır. Kapsamı belirlemek için kanıt getirin: hangi modüller karmaşık mantık ya da yüksek değişim başarısızlık oranı taşıyor, kabul ölçütlerinin gereksinimlere nerede izlenebilir olması gerekiyor ve bunları zaten uygulayan takımların hız ve kusur oranları hakkında ne bildirdiği. Beklentiyi karmaşık mantık ve gereksinim ağırlıklı alanlara ayırın ve daha basit kodun kendi seçimini yapmasına izin verin. Yazılımın uyguladığı yasaya izlenebilir olması gereken düzenlemeye tabi ve kamu programlarında, çalıştırılabilir kabul kanıtıyla belirtim güdümlü geliştirme bir tercihten çok çalışma yetkinize giden bir yoldur; bu yüzden nerede gerekli olduğunu açıkça adlandırın.

## Sektör merceği

**Girişim.** Küçük bir takım kalite güvencesini kadroya alamaz; bu yüzden takımın kendini kanıtlamasını sağlayın: her commit'te hızlı birim testleri ve faturaları ödeyen tek yol üzerinde birkaç uçtan uca test; sürdürmeyeceğiniz hiçbir şey olmasın. Kapsam hedeflerini atlayın ve en çok bozulmasından korktuğunuz mantığı test edin; böylece elle gerileme geçişi olmadan günde birkaç kez yayımlayabilirsiniz. Kararsız bir testi aynı gün düzeltin, çünkü bu aşamada takımın görmezden gelmeyi öğrendiği bir takım hiç takımın olmamasından kötüdür.

**Küçük işletme.** Özel bir test mühendisi ve sıkı bir bütçe olmadan, destekleyemeyeceğiniz özel bir donanım yerine zaten çalıştırdığınız çerçevelere ve araçlara yerleşik teste yaslanın. Geliri ve müşteri güvenini koruyan bir avuç kontrole öncelik verin ve derleme altyapısını kendiniz sürdürmemek için barındırılan CI kullanın. Erişilebilirlik ve güvenlik taramasını inşa etmek yerine hizmet olarak satın almayı tercih edin; çünkü tek bir kaçırılmış kusur aracın bir yıllık maliyetinden fazlasına mal olabilir.

**Kurumsal.** Birçok takım boyunca strateji sorunu tutarlılıktır: paylaşılan bir piramit varsayılanı, otomatik kararsız test karantinası ve her yerde aynı anlama gelen işlevsel olmayan kapılar; böylece yeşil bir derleme kim üretmiş olursa olsun güvenilirdir. Takım çalışma süresini paylaşılan bir vergi olarak bütçeleyin ve agresifçe paralelleştirin, çünkü CI duvar saati süresini her mühendis her değişiklikte öder. Kapsam ve mutasyon puanlarını liderliğin tek başına izlediği sayılar olarak değil, net sahipliği olan portföy sinyalleri olarak yönetin.

**Kamu.** Tedarik ve gözetim, testi yalnızca mühendislik hijyeni değil, kanıt yapar. Uygunluk ve politika kurallarını alan uzmanlarınca incelenen çalıştırılabilir belirtimler olarak ifade edin; böylece yazılımı uyguladığı yasaya izleyebilirsiniz ve erişilebilirlik ile güvenlik testini engelleyici yapın, çünkü yasal olarak zorunludurlar ve çalışma yetkisi kanıtının parçasıdırlar. Gerçek dağılımlarla eşleşecek biçimde üretilmiş sentetik veri kullanın, çünkü bir test ortamındaki vatandaş verisi raporlanabilir bir ihlaldir ve harici bir inceleyicinin tam olarak neyin doğrulandığını teyit edebilmesi için test yapıtlarını denetlenebilir tutun.

## Örnekler

**Girişim.** Beş kişilik bir girişim kalite güvence takımını karşılayamaz; bu yüzden her commit'te çalışan hızlı bir birim testi takımına ve faturaları ödeyen kayıttan ödemeye yolunu kapsayan birkaç uçtan uca teste yaslanır. Kurucular kapsamlı kapsamı atlar ve bunun yerine en çok bozulmasından korktukları mantığı test eder; bu da elle gerileme geçişi olmadan günde birkaç kez yayımlamalarına izin verir. Kararsız bir test rastgele başarısız olmaya başladığında aynı gün düzeltirler, çünkü güvenin her şey olduğu aşamada takımın görmezden gelmeyi öğrendiği bir takım hiç takımın olmamasından kötüdür.

**Kurumsal.** Büyük bir e-ticaret platformu her commit'te dakikalar içinde çalışan binlerce hızlı birim testini, ödeme ve envanter sınırları etrafında odaklı bir entegrasyon testi kümesini ve kritik ödeme yolculukları için küçük bir uçtan uca test takımını sürdürür. Kararsız uçtan uca testler otomatik karantinaya alınır ve onarım için atanır. Mühendisler takıma güvendiği için, kırmızı bir derlemenin gerçek bir sorun anlamına geldiğinden emin olarak günde birçok kez dağıtım yaparlar.

**Kamu.** Düzenleyici gözetim altında çalışan ulusal bir yardım sistemi, uygunluk kurallarını politika uzmanlarınca incelenen çalıştırılabilir belirtimler olarak ifade etmek için BDD kullanır; bu, yazılımın yasayı uyguladığına dair izlenebilir kanıt verir. Gizlilik kuralları test ortamlarında vatandaş verisini yasakladığı için gerçek demografik dağılımlarla eşleşecek biçimde üretilmiş sentetik veri kullanır. Hizmet tüm vatandaşlarca kullanılabilir olmalı olduğundan erişilebilirlik testi zorunludur ve sürümü engeller. Güvenlik testi ise çalışma yetkisi (ATO) kanıtının, yani sistemi üretimde çalıştırmak için resmi onayın parçasıdır.

## İş gerekçesi: motivasyonlar, YG ve TSM

Testin getirisi, sürdürülebilir teslimat hızının temeli olan yazılımı hızlı ve güvenle değiştirebilmektir. Güvenilir bir otomatik takım, yavaş, pahalı elle [gerileme testinin](https://en.wikipedia.org/wiki/Regression_testing) yerini alır ve kusurları düzeltmesi en ucuz olduğu zaman, üretimde değil sürümden önce yakalar. Düzenlemeye tabi ya da vatandaşa dönük bir sistemde, bir üretim kusurunun maliyeti (düzeltme, itibar ve olası yasal maruziyet) onu yakalayacak testlerin maliyetini gölgede bırakır.

Benimseme maliyeti gerçektir: testleri yazar ve sürdürürsünüz ve [sürekli entegrasyon](https://en.wikipedia.org/wiki/Continuous_integration) (CI) altyapısı kurarsınız. Ama test etmemenin maliyeti daha yüksektir ve bileşiktir: yavaşlayıp sürünen korku güdümlü geliştirme, sık gerilemeler ve ölçeklenemeyen elle sürüm süreçleri. Aşırı testin de bir maliyeti vardır; bu yüzden argüman en çok sayıda test için değil, iyi tasarlanmış bir strateji içindir. Gerekçeyi liderliğe sunmak için takımı dağıtım sıklığına, değişim başarısızlık oranına ve ortalama kurtarma süresine bağlayın ve yerini aldığı elle test çabasını ve önlediği üretim olaylarını nicelleştirin.

## Anti-kalıplar ve tuzaklar

- **Dondurma külahı testi:** ince bir birim tabanı üzerinde çoğunlukla yavaş uçtan uca testler; yavaş, kararsız, pahalı.
- **Hedef olarak kapsam:** hiçbir şey kanıtlamayan iddiasız ya da önemsiz testlerle bir yüzdenin peşinden koşmak.
- **Gerçekleştirim ayrıntılarını test etmek:** iç yapıya bağlı, her yeniden düzenlemede bozulan ve değişimi caydıran testler.
- **Hoşgörülen kararsızlık:** takımı kırmızı derlemeleri görmezden gelmeye alıştıran rastgele başarısızlıklar.
- **Paylaşılan değişken test verisi:** birbirine karışan ve öngörülemez biçimde başarısız olan testler.
- **Testte üretim verisi kullanmak:** gerçekleşmeyi bekleyen bir gizlilik ve uyum ihlali.
- **Atlanan işlevsel olmayan test:** erişilebilirlik, performans ve güvenliğin yalnızca üretimde keşfedilmesi.
- **Güvenilmeyen takım:** mühendislerin onu rutin olarak yeniden çalıştırdığı ya da aştığı kadar güvenilmez; amacını geçersiz kılar.

## Olgunluk modeli

- **Düzey 1, Başlangıç:** Test elle yapılır ve reaktiftir; otomatik kapsam asgaridir; gerilemeler sık ve geç yakalanır, çoğu zaman takım tarafından değil kullanıcılar tarafından.
- **Düzey 2, Geliştirme:** Otomatik birim ve bazı entegrasyon testleri vardır, ama takım yavaş ya da kararsızdır, güven düşüktür ve uygulama bir takımdan diğerine büyük ölçüde değişir.
- **Düzey 3, Standartlaştırma:** Dengeli, hızlı, güvenilir bir takım her değişikliği kapıya koyar; belgelenmiş bir piramit varsayılanı, bir kararsız test politikası ve işlevsel olmayan test (erişilebilirlik, performans, güvenlik) takımlar arasında tutarlı uygulanır.
- **Düzey 4, Yönetme:** Takım sağlığı temel çizgilere karşı ölçülür ve kontrol edilir; kararsızlık oranı, CI duvar saati süresi, yüksek değerli modüllerde mutasyon puanı ve kaçan kusur oranı izlenir ve gözden geçirilir; kapsam birkaç sinyalden biridir ve kapılar görüşe değil kanıta dayanarak tetiklenir.
- **Düzey 5, Orkestrasyon:** Gelişmiş teknikler (özellik tabanlı, mutasyon, bulanık) yüksek değerli kodu hedefler; test, dağıtım sıklığı, değişim başarısızlık oranı ve ortalama kurtarma süresi gibi teslimat metrikleriyle bütünleşir; kuruluş takımı sürekli mimarisine ve riskine göre yeniden biçimlendirir, gereksiz testleri emekliye ayırır ve kanıtın kusurların hâlâ kaçtığını gösterdiği yere yatırım yapar.

## Tartışma fikirleri

- Test dağılımınız gerçekte hangi biçimi alıyor ve mimarinize ve riskinize uyuyor mu?
- Bir kod parçasının örnek testlere karşı özellik tabanlı ya da mutasyon testini ne zaman hak ettiğine nasıl karar verirsiniz?
- Kararsız testler için politikanız nedir ve gerçekten uygulanıyor mu?
- Hassas bilgileri sızdırmadan gerçekçi sentetik veriyi nasıl üretirsiniz?
- Kapsam size nerede gerçekten yardımcı oluyor ve nerede oyunlaştırıldı?
- Yapay zekanın ürettiği testler, gürültü değil güven katmaları için nasıl incelenmeli?

## Önemli çıkarımlar

- Değiştirme güveni kazanmak için test edin; hız ve maliyet birimi başına güveni optimize edin.
- Piramidi varsayılan olarak kullanın ama testi mimarinize göre biçimlendirin.
- Kararsız testleri kusur, kapsamı hedef değil sinyal olarak ele alın.
- Gelişmiş teknikleri değerin maliyeti haklı çıkardığı yerde uygulayın.
- Erişilebilirlik, performans ve güvenlik testini stratejiye dahil edin ve gizliliği korumak için sentetik veri kullanın.

## Kaynaklar ve ileri okuma

- Kent Beck, *Test-Driven Development: By Example*
- Lisa Crispin and Janet Gregory, *Agile Testing: A Practical Guide for Testers and Agile Teams*
- Gerard Meszaros, *xUnit Test Patterns: Refactoring Test Code*
- Michael Feathers, *Working Effectively with Legacy Code*
- Nicole Forsgren, Jez Humble, Gene Kim, *Accelerate: The Science of Lean Software and DevOps*
- Martin Fowler, articles on the Test Pyramid and test-related patterns
