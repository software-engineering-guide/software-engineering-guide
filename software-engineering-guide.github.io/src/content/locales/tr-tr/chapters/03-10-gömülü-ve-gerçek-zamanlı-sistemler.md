# 3.10 Gömülü ve gerçek zamanlı sistemler

## Genel bakış ve motivasyon

[Gömülü sistem](https://en.wikipedia.org/wiki/Embedded_system), genel amaçlı bir bilgisayarda değil, bir cihazın üzerinde çalışan yazılımdır. Bir arabanın, bir kalp pilinin, bir termostatın, bir fabrika robotunun ya da bir güdüm biriminin içinde yaşar. Yazılım o cihaza adanmıştır ve cihazın belleğinde, işlem gücünde ve enerjisinde genellikle sıkı sınırlar vardır. Bir bulut konsolunda düğmeye tıklayarak her zaman daha fazla kaynak ekleyemezsiniz. Teslim ettiğiniz şey çoğu zaman yıllarca çalışacak olan şeydir.

[Gerçek zamanlı sistem](https://en.wikipedia.org/wiki/Real-time_computing), doğruluğun yalnızca doğru cevabı üretmeye değil, zamanlamaya da bağlı olduğu sistemdir. Mükemmel bir açılma komutunu bir saniye geç hesaplayan bir hava yastığı denetleyicisi tamamen başarısız olmuştur. Gerçek zamanlı çalışma her göreve zor bir soru ekler: bu, son tarihine kadar, her seferinde, en kötü durumda bile bitecek mi? Bu, web ve bulut yazılımında yaygın olan verim öncelikli düşünceden farklı bir disiplindir.

Büyük bir kuruluş için bu, ilk bakışta göründüğünden daha önemlidir. Kurumlar bağlantılı arabalar, tıbbi cihazlar, endüstriyel denetleyiciler ve milyarlarca [Nesnelerin İnterneti](https://en.wikipedia.org/wiki/Internet_of_things) (IoT) cihazı üretir. Hükümetler savunma platformları, aviyonik sistemler, elektrik şebekesi denetleyicileri ve tıbbi düzenleyiciler işletir. Bu alanlarda bir yazılım kusuru insanları yaralayabilir, bir üretim hattını durdurabilir ya da ulusal güvenliği tehlikeye atabilir. Buradaki kurallar daha sıkıdır, test daha zordur ve standartlar yasal olarak bağlayıcıdır. Bu bölüm, gerçek kısıtlar altında doğru, zamanında, güvenli ve emniyetli yazılım kurmanıza yardımcı olur. Yazılım inşası (bölüm 2.9), dağıtık sistemler (bölüm 3.3), ölçeklenebilirlik ve performans (bölüm 3.5), altyapı ve bulut güvenliği (bölüm 4.3) ve yazılım bakımı (bölüm 3.7) ile bağlantılıdır.

## Temel ilkeler

- **Zamanlama bir doğruluk gereksinimidir, performans için olsa iyi olacak bir özellik değil.** Geç bir cevap yanlış bir cevap olabilir.
- **Ortalama durum için değil, en kötü durum için tasarlayın.** Gerçek zamanlı garantiler tipik hıza değil, en kötü durum davranışına dayanır.
- **Belirlenimcilik ham hızı yener.** Son tarihini her zaman tutturan öngörülebilir bir sistem, bazen kaçıran daha hızlı bir sistemden iyidir.
- **Kaynaklar sınırlı ve sabittir.** Belleği, CPU döngülerini ve enerjiyi parayı bütçelediğiniz kadar bilinçli bütçeleyin.
- **Güvenlik ve emniyet sonradan eklenmez, baştan mühendisliğe konu edilir.** Düzenlenmiş alanlarda yalnızca kaliteyi iddia etmeyip yaptığınız işi göstermeniz gerekir.
- **Donanım sistemin parçasıdır.** Çipi, sensörleri ve fiziği düşünmeden yazılımı düşünemezsiniz.
- **Sahada güncelleme bir yaşam döngüsü yeteneğidir, sonradan akla gelen bir şey değil.** Dünyadaki cihazların düzeltmeleri almak için güvenli bir yola ihtiyacı vardır.

## Öneriler

### Her zamanlama gereksinimini katı, sıkı ya da yumuşak olarak sınıflandırın

Bütün son tarihler eşit değildir. Katı gerçek zamanlı bir son tarih asla kaçırılmamalıdır, çünkü kaçırmak sistem başarısızlığına ya da zarara yol açar: motor denetimini ya da uçuş yüzeylerini düşünün. Sıkı bir son tarih nadir kaçırmaları tolere eder, ama geç bir sonuç işe yaramaz ve atılır. Yumuşak gerçek zamanlı bir son tarih değeri zarifçe düşürür: biraz geç gelen bir video karesi kaliteyi düşürür ama felakete yol açmaz. Zamana duyarlı her görevi sınıfıyla etiketleyin, çünkü çaba, test titizliği ve maliyet çok farklıdır. İki özellik zamanlama davranışını betimler. [Gecikme](https://en.wikipedia.org/wiki/Latency_%28engineering%29), bir olay ile yanıt arasındaki gecikmedir. [Titreşim](https://en.wikipedia.org/wiki/Jitter) (jitter), o gecikmenin bir oluşumdan diğerine değişimidir. Katı gerçek zamanlı sistemler titreşimi sınırlamayı gecikmeyi düşürmek kadar önemser, çünkü bir son tarihin her zaman tutulduğunu kanıtlamanızı sağlayan şey öngörülebilirliktir.

### Yürütme temelinizi bilinçli seçin: RTOS ya da çıplak metal

İki ana temeliniz var. Çıplak metal bellenim, hiçbir işletim sistemi olmadan, basit bir döngü ve kesme işleyicileriyle doğrudan donanım üzerinde çalışır. En küçük ve en öngörülebilir seçenektir ve tek net işi olan minik cihazlara uyar. [Gerçek zamanlı işletim sistemi](https://en.wikipedia.org/wiki/Real-time_operating_system) (RTOS), görevleri önceliğe göre zamanlayan ve zamanlama sınırlarını garanti eden küçük bir işletim sistemidir. Size birden çok görev, bir zamanlayıcı ve zamanlayıcılar ile mesaj kuyrukları gibi hizmetler verirken zamanlamayı öngörülebilir tutar. Farklı son tarihleri olan birkaç eşzamanlı göreviniz varsa RTOS seçin. Cihaz çok kısıtlıysa ya da zamanlama kanıtlanabilir biçimde basit olmalıysa çıplak metal seçin. Katı gerçek zamanlı iş için kesintiye uğratabilen, öncelik tabanlı bir zamanlayıcıyı tercih edin ve görev kümesinin zamanlanabilir olduğunu kanıtlamanızı sağlayan, öncelikleri görev sıklığına göre atayan oran-monotonik zamanlama gibi bir yöntemle çözümleyin.

### Belleği, CPU'yu ve gücü birinci sınıf kaynaklar olarak bütçeleyin

Her kıt kaynağı katı bir tavanı olan bir bütçe olarak ele alın. Bellek için, öbek üzerinde dinamik tahsis yerine statik tahsisi tercih edin; çünkü dinamik bellek parçalanabilir ve en kötü anda öngörülemez biçimde başarısız olabilir. Birçok emniyet standardı tam da bu nedenle başlangıçtan sonra öbek kullanımını kısıtlar ya da yasaklar. CPU için, bir görevin alabileceği en uzun süre olan [en kötü durum yürütme süresini](https://en.wikipedia.org/wiki/Worst-case_execution_time) (WCET) ölçün ve ortalamaya göre değil, o sayıya göre zamanlayın. Güç için, birçok cihazın pille çalıştığını ya da enerji topladığını unutmayın; bu yüzden aylarca ya da yıllarca dayanması gereken bir enerji bütçesini tutturmak için görev döngülerini, uyku durumlarını ve uyanma olaylarını tasarlayın. Bu bütçeleri yazın ve herhangi bir gereksinim gibi inceleyin.

### Kesmeleri ve eşzamanlılığı sıkı bir disiplinle yönetin

[Kesme](https://en.wikipedia.org/wiki/Interrupt), mevcut işi durdurup bir işleyiciyi hemen çalıştıran bir donanım sinyalidir. Kesmeler cihazların dünyaya anında tepki verme biçimidir ve ince hataların büyük bir kaynağıdır. İşleyicileri mümkün olduğunca kısa tutun: olayı onaylayın, asgari veriyi saklayın ve gerçek işi normal bir göreve erteleyin. Bir kesme herhangi iki komut arasında tetiklenebileceğinden, paylaşılan veriyi [yarış durumlarından](https://en.wikipedia.org/wiki/Race_condition) dikkatle korumalısınız. Kilitsiz teknikler, kısa kritik bölgeler ya da iyi anlaşılmış ilkeller kullanın ve bir kilidi tutan düşük öncelikli bir görevin yüksek öncelikli olanı engellediği öncelik tersine dönmesine karşı korunun. Bu eşzamanlılık bölüm 3.3'ün muhakemesini paylaşır, ama daha sıkı zamanlamayla ve yeniden deneme payı olmadan.

### Donanım ayrıntısını yalıtan aygıt sürücüleri yazın

[Aygıt sürücüsü](https://en.wikipedia.org/wiki/Device_driver), belirli bir donanım parçasıyla konuşan yazılım katmanıdır: bir sensör, bir telsiz, bir motor denetleyicisi. Donanıma özgü kodu temiz bir arayüzün arkasında tutun; böylece yazılımınızın geri kalanı yazmaç adreslerine değil, kararlı bir soyutlamaya dayanır. Bu, kodu hedef cihaz dışında test edilebilir, bir çip stoktan kalktığında taşınması daha kolay ve üzerinde düşünmesi daha basit yapar. Zamanlama, bayt sırası ve donanım tuhaflıkları hakkındaki her varsayımı belgeleyin, çünkü sahada başarısızlıklara yol açan ayrıntılar bunlardır. Bu, yanlış bir bitin bir motoru durdurabildiği yerde uygulanan bölüm 2.9'un inşa disiplinidir.

### Alanınızı yöneten işlevsel emniyet standardını benimseyin

Cihazınız insanlara ya da mala zarar verebiliyorsa, büyük olasılıkla bir [işlevsel emniyet](https://en.wikipedia.org/wiki/Functional_safety) standardı geçerlidir ve çoğu zaman bu yasadır. IEC 61508 elektronik sistemlerin emniyeti için genel standarttır ve birkaç diğerinin atasıdır. [ISO 26262](https://en.wikipedia.org/wiki/ISO_26262) karayolu araçlarının emniyetini yönetir. [DO-178C](https://en.wikipedia.org/wiki/DO-178C) sivil havacılıkta havadaki yazılımı yönetir. IEC 62304 tıbbi cihaz yazılımını yönetir. Kodlama için [MISRA C](https://en.wikipedia.org/wiki/MISRA_C), kodu daha güvenli ve çözümlenebilir kılmak için riskli C dili özelliklerini kısıtlayan yaygın kullanılan bir kurallar kümesidir. Bu standartlar gereksinimden koda, koddan teste izlenebilirlik, tanımlı süreçler ve bir denetçiye ya da düzenleyiciye verebileceğiniz kanıt talep eder. Doğru olanı erken benimseyin, çünkü kâğıt izini sonradan eklemek acı vericidir ve bazen imkânsızdır.

### Simülasyon ve döngüde donanım ile test edin

Gömülü yazılımı bir web uygulamasını test ettiğiniz gibi test edemezsiniz. Katmanlı bir strateji kurun. Birim testlerini normal bir bilgisayarda, donanım soyutlama arayüzüne karşı çalıştırın. Gerçek donanım kıt olduğunda ya da çalıştırması tehlikeli olduğunda cihazı ve çevresini modellemek için simülasyon kullanın. Sonra, gerçek denetleyicinin denetlediği fiziksel sistemin simüle edilmiş bir sürümüne karşı çalıştığı [döngüde donanım](https://en.wikipedia.org/wiki/Hardware-in-the-loop_simulation) (HIL) testini kullanın; böylece takılı kalmış bir sensör ya da ani bir yük gibi arıza koşullarını güvenle test edebilirsiniz. Bu testleri hattınızda otomatikleştirin; böylece her değişiklik bir cihaza ulaşmadan önce gerçekçi koşullar altında denetlenir.

### Havadan güncellemeleri ve cihaz güvenliğini ilk günden tasarlayın

Sahadaki cihazların düzeltmelere ihtiyacı olacak; bu yüzden havadan (OTA) güncellemeleri planlayın: yeni bellenimi bir ağ üzerinden güvenle teslim etmenin bir yolu. Güvenli bir OTA tasarımı her güncellemeyi kriptografik olarak imzalar, kurmadan önce imzayı doğrular, atomik güncelleme yapar ve yenisi açılamazsa bilinen sağlam bir imaja geri dönebilir. Bunu, kısıtlı donanıma uyarlanmış bölüm 4.3'ün güvenlik ilkeleriyle eşleştirin. Yalnızca imzalı bellenimin çalışması için bir donanım güven kökü ve güvenli önyükleme kullanın. Veriyi aktarım sırasında ve beklerken şifreleyin. Varsayılan kimlik bilgilerini değiştirin ve kullanılmayan arayüzleri kapatın. Bir IoT filosu devasa bir saldırı yüzeyi olan dağıtık bir sistemdir ve tek bir zayıf varsayılan parola milyonlarca cihazı bir anda tehlikeye atabilir.

## Ödünleşimler: artılar ve eksiler

| Seçim | Artılar | Eksiler / maliyet |
|---|---|---|
| RTOS | Çoklu görev, öncelik zamanlaması, zamanlama hizmetleri | Ek yük, daha büyük ayak izi, öğrenme eğrisi |
| Çıplak metal | En küçük, en öngörülebilir, tam denetim | Çok sayıda göreve ölçeklemek zor, daha fazla elle iş |
| Statik tahsis | Öngörülebilir, parçalanma yok, emniyete uygun | Daha az esnek, her şeyi baştan boyutlandırmak gerekir |
| Resmî emniyet sertifikasyonu | Yasal pazar erişimi, titiz kanıt, daha yüksek güven | Büyük zaman ve para maliyeti, daha yavaş yineleme |
| OTA güncellemeleri | Sahadaki cihazları düzeltme ve iyileştirme, ömrü uzatma | Güncelleme altyapısı, güvenlik yükü, geri alma riski |

Ana ödünleşim, öngörülebilirlik ile esneklik arasındadır. Genel amaçlı bir sistemi rahat kılan her şey (dinamik bellek, arka plan çöp toplama, en iyi çaba zamanlaması, esnek kaynaklar), bir görevin sabit bir ayak izi içinde her zaman zamanında biteceği garantisine karşı çalışır. Gömülü ve gerçek zamanlı mühendislik, belirlenimciliği ve emniyeti satın almak için esnekliği bilerek feda eder. Beceri, bu ödünleşimi yalnızca son tarihin ya da riskin gerçekten gerektirdiği yerde harcamak ve esnek, daha hızlı ilerleyen parçaları (bir cihazın bulut arka ucu gibi) temiz bir sınırın diğer tarafında tutmaktır.

## Takımınızla tartışılacak sorular

1. **Zamanlama açısından kritik yollarınızda yalnızca ortalama gecikmeyi mi, yoksa titreşimi de ölçüyor musunuz?** Katı gerçek zamanlı doğruluk, yalnızca tipik gecikmeyi düşürmeye değil, yanıt süresindeki değişimi (titreşimi) sınırlamaya dayanır; çünkü bir son tarihin her zaman tutulduğunu kanıtlamanızı sağlayan şey öngörülebilirliktir. Ortalaması düşük ama ara sıra büyük sıçramaları olan bir denetim döngüsü yine de son tarihini kaçırıp zarara yol açabilir ve ortalama bunu gizler. Her zamanlama açısından kritik görev için, en kötü durum dahil yayılımın ölçümlerini getirin ve her birini katı, sıkı ya da yumuşak olarak etiketleyin ki test titizliği kaçırmanın sonucuyla eşleşsin. Genel amaçlı sistemlerde rahat olan her şey (dinamik bellek, çöp toplama, en iyi çaba zamanlaması) öngörülebilirliğe saldırır; bu yüzden katı yolun dışında kalır. Yalnızca ortalama bildiriyorsanız, katı bir son tarihin tutulduğunu dürüstçe iddia edemezsiniz.

2. **RTOS ya da çıplak metal seçiminiz hâlâ doğru mu ve görev kümesinin zamanlanabilir olduğunu kanıtlayabiliyor musunuz?** Yürütme temeli, cihaz büyüdükçe yeniden gözden geçirilecek bir karardır: çıplak metal tek net iş için en küçük ve en öngörülebilir olandır, RTOS ise farklı son tarihleri olan birkaç eşzamanlı görev olduğunda ek yükünü hak eder. Katı gerçek zamanlı iş için bölüm, görevlerin sığdığını umut etmek yerine kanıtlamanızı sağlayan oran-monotonik zamanlama gibi bir yöntemle çözümlenen, kesintiye uğratabilen, öncelik tabanlı bir zamanlayıcıya işaret eder. Mevcut görev kümesini, sıklıklarını ve en kötü durum yürütme sürelerini getirin ve zamanlanabilirliğin gerçekten geçerli olup olmadığını ya da görevlerin temelin garanti edebileceğinin ötesine sessizce birikip birikmediğini denetleyin. Bir kilidi tutan düşük öncelikli bir görevin yüksek öncelikli olanı durdurduğu öncelik tersine dönmesine karşı korunun. Temeli görev kümesine göre değil alışkanlıkla seçmek, zamanlama garantilerinin sessizce aşındığı yoldur.

3. **Belirlenimci cihaz ile esnek bulut arka ucu arasındaki sınır tam olarak nerede ve bir tarafta hızlı ilerlerken diğerini tehlikeye atmayacak kadar temiz mi?** Bölümün ana ödünleşimi belirlenimciliği ve emniyeti satın almak için esnekliği feda eder ve beceri, bu ödünleşimi yalnızca son tarihin ya da riskin gerçekten gerektirdiği yerde harcamaktır. Temiz bir sınır, emniyet açısından kritik bellenimin muhafazakâr ve sertifikalı kalmasına izin verirken bulut arka ucunun hızla yinelenmesini sağlar; böylece ikisi kendi güvenli hızlarında evrilir. Mimarinizi getirin ve o dikişi bulun: neyin belirlenimci olduğu kanıtlanmalı ve imzalı, doğrulanmış bir yolla güncellenmeli, neyin sunucuda haftalık değişebileceği. Çizgiyi bulanıklaştırmak bulut tarzı alışkanlıkları (dinamik tahsis, en iyi çaba zamanlaması) denetim yoluna sürükler ya da arka ucu gereksiz yere bellenimin temposuna yavaşlatır. Sınırı doğru kurmak hem emniyet kanıtını hem de teslim hızını sağlam tutan şeydir.

4. **Her ürünü hangi işlevsel emniyet standardı yönetiyor ve mevcut kanıt bir denetçinin kabul edeceğinden ne kadar uzak?** Standart (IEC 61508, karayolu araçları için ISO 26262, havadaki yazılım için DO-178C, tıbbi cihazlar için IEC 62304) çoğu zaman yasadır ve sonunda sahtesini yapamayacağınız, gereksinimden koda, koddan teste izlenebilirlik talep eder. Büyük bir takım için risk, grupların kâğıt izini eşitsiz benimsemesidir; böylece bir ürün hattı denetime hazırken bir diğeri sertifikasyonun ortasında gereksinimlerinin hiç izlenmediğini keşfeder. Rakip çekim hızdır: tam izlenebilirlik ve MISRA C uygulaması gündelik yinelemeyi yavaşlatır ve son tarih baskısı altındaki bir takım kanıtı "sonraya" ertelemeye meyleder. Mevcut izlenebilirlik matrisini, hâlâ açık olan statik analiz bulgularını ve hedef güvence düzeyine karşı dürüst bir boşluk analizini getirin. Kurumsal ve kamu bağlamlarında sertifikasyon hazırlık süresini ve denetçinin beklentilerini ekleyin; çünkü kanıtı tasarımdan sonra eklemek yavaş, maliyetli ve bazen imkânsızdır ve kayan bir sertifikasyon pazar erişimini tamamen engelleyebilir.

5. **Yarın sahadaki bir cihazda ciddi bir kusur bulunsaydı, bunu tüm filoda ne kadar hızlı ve güvenle düzeltebilirdiniz ve geri almayı prova ettiniz mi?** Yama atamadığınız bir cihaz kalıcı bir emniyet ve güvenlik yükümlülüğüne dönüşür ve fiziksel bir geri çağırma, imzalı bir havadan güncellemeden kat kat pahalıdır. Gerilim şudur: özensiz bir güncelleme mekanizmasının kendisi bir saldırı yüzeyi ve cihazı kullanılmaz hâle getirme riskidir: imzasız imajları kuran ya da kötü bir açılışı geri alamayan bir OTA yolu, tek bir kötü sürümü milyonlarca ölü birime çevirebilir. Güncelleme tasarımınızı (kriptografik imzalama, kurulumdan önce imza doğrulama, atomik kurulum, bilinen sağlam bir imaja otomatik geri alma), güvenli önyükleme ve donanım güven kökü durumunu ve birinin gerçek donanımda en son ne zaman bir geri almayı gerçekten uyguladığını getirin. Kurumsal ya da kamusal bir filo için, imzalama anahtarlarından kimin sorumlu olduğunu ve ele geçirilmiş birini nasıl iptal edeceğinizi ekleyin; çünkü sızmış bir anahtar ya da paylaşılan bir varsayılan kimlik bilgisi tüm filoyu bir anda tehlikeye atabilir.

6. **Bellek, CPU ve güç bütçeleriniz katı tavanlarla yazılı mı ve test stratejiniz hem simülasyonu hem gerçek donanımı sınıyor mu?** Gerçek zamanlı garantiler ortalama davranışa değil, en kötü durum yürütme süresine ve sabit kaynak ayak izine dayanır; bu yüzden bütçelenmemiş bir öbek tahsisi ya da sınanmamış bir en kötü durum yükü, belirlenimciliğin sessizce aşındığı yerdir. Büyük bir takım için tehlike sürüklenmedir: görevler birikir, bellek yavaşça yükselir ve haftalarca açık kaldıktan sonra bir cihaz sahada başarısız olana dek kimse bütçeye sahip çıkmaz. Ödünleşim kapsam ile maliyet arasındadır, çünkü takılı kalmış bir sensör gibi arızaları enjekte eden bir döngüde donanım düzeneği kurmak pahalıdır, salt simülasyon ise yalnızca gerçek çipte görünen zamanlama hatalarını gizler. Belgelenmiş bütçeleri, bunlara karşı ölçülmüş en kötü durum yürütme sürelerini ve hattınızın bir sürümden önce soyutlama katmanında birim testlerini, simülasyonu ve döngüde donanımı çalıştırdığına dair kanıtı getirin. Düzenlenmiş ve kamusal ortamlarda bunu standardın gerektirdiği yapısal test kapsamına bağlayın; çünkü bir denetçi ortalama durumun iyi göründüğüne dair bir güvence değil, arıza koşullarının sınandığına dair kanıt isteyecektir.

## Sektör merceği

**Girişim.** Hız ve hayatta kalma baskındır; bu yüzden hafif bir RTOS ya da basit bir çıplak metal döngü seçin, başlangıçtan sonra dinamik tahsisi yasaklayın ve sahip olmadığınız bir sertifikasyon bütçesinin peşinden koşmak yerine tek kritik döngünüzün en kötü durum süresini ölçün. Pazarınız sizi zorlamadıkça resmî işlevsel emniyet süreçlerini atlayın, ama otomatik geri almalı imzalı havadan güncellemeleri asla atlamayın: genç bir şirket sahadaki bir geri çağırmadan sağ çıkamaz ve uzaktan bir düzeltme, kötü bir gece ile ölü bir ürün arasındaki farktır. Kıt mühendislerinizin karşılayamayacakları bir hattı sürdürmemesi için cihaz bellenimini küçük ve muhafazakâr tutun.

**Küçük işletme.** Kadroda gömülü uzmanı olmadığında, kendi zamanlayıcınızı ya da önyükleyicinizi yazmak yerine kanıtlanmış modüllere, referans tasarımlara ve tedarikçi RTOS dağıtımlarına yaslanın. Yap-ya-da-satın-al seçimini, önümüzdeki on yıl cihaza kimin yama atacağı çerçevesine oturtun: güvenebileceğiniz satın alınmış bir güvenlik ve güncelleme yığını, sürdürebilecek kimsenin kalmadığı özel bir yığından iyidir. Varsayılan parolaları, açık hata ayıklama arayüzlerini ve imzasız güncellemeleri size en çok zarar verecek başarısızlıklar olarak ele alın, çünkü önlemesi ucuz, sahada keşfetmesi yıkıcıdır.

**Kurumsal.** Sorun, birçok ürün hattı ve takım arasında tutarlılıktır: ortak bir yürütme temeli politikası, ortak kaynak bütçesi şablonları, uygulanan MISRA C ve statik analiz ve her grubun yeniden icat etmemesi için sertifikalı tek bir havadan güncelleme ve güvenli önyükleme platformu. İşlevsel emniyet ve döngüde donanım yükünü açıkça bütçeleyin, bir çipin stoktan kalkması bir ürünü çaresiz bırakmasın diye donanım soyutlama arayüzünü standartlaştırın ve filonun zamanlama kanıtını, emniyet ürünlerini ve güvenlik duruşunu takım başına halk bilgisi olarak değil, yönetilen varlıklar olarak yönetin. Filo genelinde tek bir zayıf varsayılan kimlik bilgisi kurumsal ölçekte bir yükümlülüktür; bu yüzden kimlik bilgisi ve anahtar yönetimini merkezileştirin.

**Kamu.** İhale kuralları, şeffaflık ve kamusal hesap verebilirlik her seçimi şekillendirir. Tedarikçilerden havadaki, tıbbi ya da savunma yazılımını tehlikeyle eşleşen güvence düzeyinde yöneten standarda (DO-178C, IEC 62304, IEC 61508) göre geliştirmelerini ve denetçilerin inceleyeceği izlenebilirlik ve yapısal kapsam kanıtını teslim etmelerini isteyin. Güvenli önyükleme, bir donanım güven kökü ve denetimli, imzalı bir saha güncelleme süreci talep edin, çünkü bir uçuş ya da şebeke sistemine doğrulanmamış bir güncelleme kabul edilemez. Bir tedarikçinin iş kapatması, halkın on yıllarca bağımlı olduğu bir sistemi çaresiz bırakmasın diye kaynak, emniyet ürünleri üzerinde haklar ve ikinci bir tedarikçiyle yeniden sertifikalandırma imkânı tanıyan sözleşmeleri tercih edin.

## Örnekler

**Girişim.** Pille çalışan bir hava kalitesi monitörü geliştiren küçük bir donanım girişimi, bellenimini sabit bir görev kümesi olan ve başlangıçtan sonra dinamik tahsis içermeyen hafif bir RTOS'a karşı yazar; böylece teslim edilen cihaz, bir düğme pille yıllarca çalışan cihazdır. Sertifikasyon bütçesi olmasa bile takım, sensör okuma döngüsünün en kötü durum süresini ölçer ve birimi her sürümden önce bir tezgâh düzeneğinde enjekte edilmiş arıza koşullarına karşı sınar. Otomatik geri almalı imzalı havadan güncellemeler, sevk edilmiş her birimdeki bir kusuru düzeltmelerini sağlar; böylece sahada kötü bir okuma, genç şirketin atlatamayacağı bir geri çağırma anlamına gelmez.

**Kurumsal.** Bağlantılı araç üreticisi bir elektronik fren denetleyicisi geliştirir. Katı gerçek zamanlı denetim döngüsü, oran-monotonik zamanlama ve statik bellekle bir RTOS üzerinde çalışır ve her görev ölçülmüş bir en kötü durum yürütme süresi taşır. Takım, gereksinimden koda, koddan teste tam izlenebilirlikle ISO 26262'ye göre geliştirir ve her commit'te statik analizle MISRA C'yi uygular. Bir döngüde donanım düzeneği, herhangi bir bellenim sevk edilmeden önce enjekte edilmiş sensör arızaları dahil binlerce yol senaryosunu yeniden oynatır. İmzalı OTA güncellemeleri şirketin, bir araç yeni imajı açamazsa otomatik geri almayla, maliyetli bir geri çağırma olmadan tüm filodaki bir kusuru düzeltmesini sağlar.

**Kamu.** Ulusal bir havacılık otoritesi yeni bir uçuş yönetim bilgisayarını sertifikalandırır. Tedarikçi havadaki yazılımı tehlikeyle eşleşen güvence düzeyinde DO-178C'ye göre geliştirir ve denetçilerin inceleyeceği gereksinim kapsamı ve yapısal test kapsamı kanıtı üretir. Zamanlamanın en kötü durum yükü altında belirlenimci olduğu, sınırlı kesme gecikmesiyle ve başlangıçtan sonra dinamik tahsis olmadan kanıtlanır. Güvenli önyükleme ve bir donanım güven kökü, yalnızca imzalı, sertifikalı bellenimin çalışmasını sağlar. Saha güncellemeleri denetimli, imzalı bir süreci izler, çünkü bir uçuş sistemine doğrulanmamış bir güncelleme kabul edilemez.

## İş gerekçesi: motivasyonlar, YG ve TSM

İş gerekçesine, başarısızlığın maliyeti ve bir pazara erişimin maliyeti hükmeder. Düzenlenmiş alanlarda, emniyet sertifikasyonu olmadan ürünü hiç satamazsınız; bu yüzden süreç maliyeti yalnızca giriş bedelidir. Bunun ötesinde, sahadaki donanımdaki kusurlar olağanüstü pahalıdır: fiziksel bir geri çağırma bir bulut düzeltmesinden çok daha fazlaya mal olur ve bir emniyet olayı bir ürün hattını bitirebilecek sorumluluk, düzenleyici ceza ve itibar zararı taşır. Emniyeti, belirlenimciliği ve güncellenebilirliği baştan kurmak, yokluklarını sahada keşfetmeye kıyasla ucuzdur.

Yatırım getirisini önlenen geri çağırmalar, daha hızlı sertifikasyon ve daha uzun cihaz ömrü etrafında çerçeveleyin. Sağlam bir OTA yeteneği, olası birçok geri çağırmayı düşük maliyetli uzaktan düzeltmelere dönüştürür ve önlenen her geri çağırma tüm güncelleme programının bedelini ödeyebilir. Titiz WCET analizi ve kaynak bütçelemesi, güvenle daha ucuz donanımda sevk etmenizi sağlar ve büyük bir filoda birim başına maliyeti düşürür. Toplam sahip olma maliyeti için, bu cihazların yıllarca ya da on yıllarca yaşadığını unutmayın: bakım, güvenlik yaması ve destek yükü (bölüm 3.7) ilk inşayı gölgede bırakır. Güncellenebilirlik, net donanım soyutlaması ve belgelenmiş bütçeler için tasarım yapmak, bu uzun kuyruğu karşılanabilir tutan şeydir.

## Anti-kalıplar ve tuzaklar

- **Ortalama durum için eniyileme.** Son tarihi "genellikle" tutturmak, katı bir gerçek zamanlı gereksinimde başarısız olmaktır.
- **Denetim yolunda dinamik tahsis.** Öbek parçalanması, yalnızca haftalarca açık kaldıktan sonra beliren bir başarısızlığa yol açar.
- **Şişman kesme işleyicileri.** Bir kesmenin içine ağır işlem koymak zamanlama bütçenizi patlatır ve yarış durumları yaratır.
- **Denetime kadar standardı yok saymak.** İzlenebilirliği ve kanıtı geç eklemek yavaş, maliyetli ve bazen imkânsızdır.
- **Güncelleme yolu olmadan sevk etmek.** Yama atamadığınız bir cihaz kalıcı bir güvenlik ve emniyet yükümlülüğüne dönüşür.
- **Varsayılan parolalar ve açık arayüzler.** Tek bir zayıf kimlik bilgisi bir IoT filosunu botnete çevirir.
- **Yalnızca simülatörde ya da yalnızca donanımda test etmek.** Her biri diğerinin yakalayacağı hataları gizler; ikisine de ihtiyacınız var.
- **Donanımı başkasının sorunu saymak.** Burada zamanlama, bayt sırası ve sensör tuhaflıkları yazılım meseleleridir.

## Olgunluk modeli

- **Düzey 1, Başlangıç.** Zamanlama umut edilir, çözümlenmez. Bellek keyfe göre dinamik tahsis edilir. Hiçbir işlevsel emniyet standardı izlenmez. Test elle ve yalnızca cihaz üzerindedir. Cihazlar sevk edildikten sonra güncellenemez; bu yüzden sahadaki bir kusur geri çağırma ya da kalıcı bir yükümlülük demektir.
- **Düzey 2, Geliştirme.** Bazı görevlerin ölçülmüş zamanlaması vardır ve temel bir RTOS ya da yapılandırılmış bir döngü yerindedir, ama uygulama takımdan takıma değişir. Kodlama yönergeleri vardır ama uygulanmaz. Test bir miktar simülasyon içerir. Bazı ürünlerde elle yapılan, riskli bir güncelleme yolu vardır, bazılarında yoktur. İyi alışkanlıklar mevcuttur ama tutarsızdır ve bir sonraki ürün hattının bunları miras alacağını hiçbir şey garanti etmez.
- **Düzey 3, Standartlaştırma.** Zamanlama gereksinimleri katı, sıkı ya da yumuşak olarak sınıflandırılır ve en kötü durum yürütme süresi ile bir zamanlanabilirlik yöntemiyle çözümlenir; belgelenir ve kuruluş genelinde uygulanır. Bellek, CPU ve güç için kaynak bütçeleri katı tavanlarla yazılıdır. Yöneten işlevsel emniyet standardı, gereksinimden koda, koddan teste izlenebilirlikle izlenir ve MISRA C ya da eşdeğeri her commit'te statik analizle uygulanır. Döngüde donanım testi hatta çalışır. Geri almalı imzalı, atomik havadan güncellemeler ve güvenli önyükleme her yerde zorunlu temel çizgidir.
- **Düzey 4, Yönetme.** Kuruluş gömülü varlığını temel çizgilere karşı ölçer ve denetler. En kötü durum yürütme süresi marjlarını, titreşim dağılımlarını, son tarih kaçırma oranlarını, bellek ve güç payını, hâlâ açık statik analiz bulgularını, sertifikasyon kanıtı kapsamını ve havadan güncelleme başarı ile geri alma oranlarını izler ve bunları üzerinde uzlaşılmış hedeflerle karşılaştırır. Bir kaynak ya da zamanlama bütçesine karşı sürüklenme, cihaz sahada başarısız olmadan önce eylemi tetikler ve sürüm için git ya da gitme kararları anlık yargıya değil, bu veriye dayanır. Yöneticiler hangi ürün hatlarının denetime hazır olduğunu, hangilerinin kaçırılmış bir son tarihe ya da patlamış bir bütçeye doğru gittiğini görebilir.
- **Düzey 5, Orkestrasyon.** Belirlenimcilik, emniyet kanıtı ve güvenlik sürekli doğrulanır ve otomatikleştirilir. Arıza enjeksiyonu ve döngüde donanım her değişiklikte çalışır ve sertifikasyon ürünleri sürecin yan ürünü olarak üretilir. Filo, uzun bir hizmet ömrü boyunca ölçekte güvenle izlenir, yamalanır ve güncellenir. Kuruluş, çipler stoktan kalktıkça, tehditler evrildikçe ve düzenlemeler değiştikçe yürütme temellerini, kaynak bütçelerini ve standart benimsemesini uyarlar; her krize tek başına tepki vermek yerine cihazların tüm portföyünü kanıta dayanarak yeniden dengeler.

## Tartışma fikirleri

1. Cihazınızın görevlerinden hangileri gerçekten katı gerçek zamanlı ve her birinin son tarihini her zaman tuttuğunu kanıtlayabiliyor musunuz?
2. Kritik denetim döngünüzün en kötü durum yürütme süresini biliyor musunuz, yoksa yalnızca ortalamasını mı?
3. Ürününüzü hangi işlevsel emniyet standardı yönetiyor ve mevcut kanıtınız onun talep ettiğinden ne kadar uzak?
4. Yarın sahadaki bir cihazda ciddi bir kusur bulunsaydı, onu nasıl düzeltirdiniz ve ne kadar hızlı?
5. Denetim yolunuzda dinamik bellek tahsisi hâlâ nerede var ve 1000. saatte başarısız olursa ne olur?
6. IoT filonuz, tek bir paylaşılan varsayılan kimlik bilgisini bulan bir saldırgana nasıl dayanırdı?

## Önemli çıkarımlar

- Gömülü yazılım kısıtlı donanımda çalışır ve gerçek zamanlı doğruluk yalnızca doğru cevaba değil, zamanlamaya bağlıdır.
- Her son tarihi katı, sıkı ya da yumuşak olarak sınıflandırın ve ham hız yerine en kötü durum zamanlaması, sınırlı titreşim ve belirlenimcilik için tasarlayın.
- RTOS ya da çıplak metali bilinçli seçin ve belleği, CPU'yu ve gücü sabit, birinci sınıf kaynaklar olarak bütçeleyin.
- Kesme işleyicilerini minik tutun, paylaşılan veriyi koruyun ve donanımı temiz, test edilebilir sürücü arayüzlerinin arkasında yalıtın.
- Alanınızın gerektirdiği işlevsel emniyet standardını (IEC 61508, ISO 26262, DO-178C, IEC 62304, MISRA C) tam izlenebilirlikle erken benimseyin.
- Simülasyon ve döngüde donanım ile test edin ve güvenli, imzalı, geri almaya yetenekli OTA güncellemelerini ve cihaz güvenliğini ilk günden kurun.

## Kaynaklar ve ileri okuma

- IEC 61508, *Functional Safety of Electrical/Electronic/Programmable Electronic Safety-related Systems*
- ISO 26262, *Road Vehicles: Functional Safety*
- RTCA DO-178C, *Software Considerations in Airborne Systems and Equipment Certification*
- IEC 62304, *Medical Device Software: Software Life Cycle Processes*
- MISRA, *MISRA C: Guidelines for the Use of the C Language in Critical Systems*
- Michael Barr and Anthony Massa, *Programming Embedded Systems*
- Elecia White, *Making Embedded Systems*
- Jane W. S. Liu, *Real-Time Systems*
- Giorgio Buttazzo, *Hard Real-Time Computing Systems: Predictable Scheduling Algorithms and Applications*
- Colin Walls, *Embedded Software: The Works*
- Philip Koopman, *Better Embedded System Software*
- OWASP Internet of Things (IoT) security guidance
