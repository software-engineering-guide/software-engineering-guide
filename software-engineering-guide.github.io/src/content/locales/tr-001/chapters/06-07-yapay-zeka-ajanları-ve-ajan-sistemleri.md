# 6.7 Yapay zeka ajanları ve ajan sistemleri

## Genel bakış ve motivasyon

Bir **yapay zeka ajanı**, bir döngüye sarılmış [büyük dil modelidir](https://en.wikipedia.org/wiki/Large_language_model) (LLM): ona bir hedef verilir, araçları çağırabilir, yaptıklarının bir kısmını hafızasında tutar ve hedef ulaşılana ya da pes edene kadar bir sonraki adımına kendisi karar verir. Bir ajanı, bölüm 6.3'teki düz istem-yanıt çağrılarından ayıran tek şey bu döngüdür. Tek bir çağrı bir soruyu yanıtlar. Bir ajan e-postasını okur, bir veritabanında arama yapar, bir bilet açar, sonucu kontrol eder ve yeniden dener. Model artık yalnızca metin üretmiyor; sistemlerinizde eylemleri seçiyor.

Bu kayma, mühendislik problemini değiştirir. Bir model yalnızca sözcük yazdığında kötü bir çıktı kötü bir cümledir. Bir model araçları yönettiğinde kötü bir çıktı yanlış bir mesaj gönderebilir, bir kaydı silebilir ya da para taşıyabilir. Bu yüzden bir [akıllı ajan](https://en.wikipedia.org/wiki/Intelligent_agent) en iyi, güvenilen bir sistemin içinde oturan güvenilmeyen bir planlayıcı olarak anlaşılır ve işinizin çoğu, o planlayıcının ne yapmasına izin verildiğini sınırlamaya gider. Bu bölüm doğrudan bölüm 6.3'ün LLM temellerine, bölüm 6.5'in güven ve hesap verebilirlik kaygılarına ve bölüm 6.6'nın platform uygulamalarına dayanır.

Büyük takımlar için bahisler teknik olduğu kadar kurumsaldır. Kurumlar ajanların gerçek iç sistemlere (biletleme, finans, müşteri kayıtları) bağlanmasını ister; bu da ajanların gerçek erişim denetimlerini ve gerçek değişiklik yönetimi yükümlülüklerini devralması demektir. Kamu ise kamusal hesap verebilirlik ekler: bir vatandaşı etkileyen otonom bir eylem açıklanabilir, gözetlenebilir ve sonradan denetlenebilir olmalıdır. Kalıp güçlüdür. Disiplin olmadan devreye alındığında, hataları otomatikleştirmenin hızlı bir yoludur.

## Temel ilkeler

- Bir ajan; bir model artı bir döngü, araçlar, hafıza ve bir hedeftir. Risk düzyazıda değil, döngüde yaşar.
- Özerkliği göreve göre sınırlayın. İşi yaptıran en küçük özgürlük miktarını verin.
- Adımlar biliniyorsa sabit bir iş akışını tercih edin. Açık uçlu özerkliğe yalnızca adımlar bilinmiyorsa başvurun.
- Her aracı saldırı yüzeyi sayın ve ona çalışabileceği en az ayrıcalığı verin.
- Sonuç doğuran ya da geri döndürülemez eylemler için döngüye bir insan koyun ve geri almayı ucuz yapın.
- Dökümün nasıl okunduğuna değil, görev başarısına göre değerlendirin.
- Her çalıştırmayı izleyin. Yeniden kurgulayamadığınız bir eylemi yönetemezsiniz.
- Çalışan en basit tasarım genellikle doğru olandır. Çoğu zaman bu bir ajan hiç değildir.

## Öneriler

### Bir iş akışıyla başlayın, özerkliği yalnızca zorunlu olduğu yerde ekleyin

En yaygın hata, sabit bir işlem hattının yeteceği yerde otonom bir ajana uzanmaktır. Adımları zaten biliyorsanız (alanları çıkar, doğrula, bir kaydı ara, bir yanıt taslağı hazırla), bunu modelin belirli yuvaları doldurduğu, düzenlenmiş bir iş akışı olarak yazın. Özerklik, yolun gerçekten önceden belirlenemediği durumlarda, örneğin açık uçlu araştırma ya da birçok olası araç arasında triyajda ekmeğini hak eder. Özerkliği göreve göre sınırlayın: adım sayısına tavan koyun, araç kümesini bu hedefin ihtiyaç duyduğuyla kısıtlayın ve net bir durma koşulu belirleyin. İyi bir kural, modele sorunun gerektirdiği kadar özgürlük vermek ve bir derece fazlasını vermemektir.

### Araç kullanımını çekirdek yetenek yapın ve güvenli kılın

Araç kullanımı (işlev çağırma da denir), bir modeli ajana dönüştüren şeydir. Her aracı kesin bir şemayla tanımlayın, modelin verdiği her argümanı doğrulayın ve [en az ayrıcalık ilkesini](https://en.wikipedia.org/wiki/Principle_of_least_privilege) uygulayın: salt okunur bir raporlama ajanı, kötüye kullanabileceği yazma erişimini asla değil, salt okunur kimlik bilgilerini alır. Kötü bir çağrı etki alanının ötesine ulaşamasın diye araçları bir [kum havuzunun](https://en.wikipedia.org/wiki/Sandbox_(computer_security)) içinde çalıştırın. Birkaç geniş araç yerine çok sayıda dar, tek amaçlı aracı tercih edin, çünkü dar bir aracı akıl yürütmek, izinlendirmek ve denetlemek daha kolaydır. Bu, bölüm 6.3'ün LLM araç kullanımı için öğütlediği aynı ölçülülüktür; burada merkeze alınmıştır.

### Açık akıl yürütme ve planlama kalıpları kullanın

Ajanlar, düşünceleri yapılandırıldığında daha iyi çalışır. Bir akıl yürüt ve harekete geç kalıbında (ReAct araştırmasıyla yaygınlaştı) model, durum hakkında akıl yürütme ve bir eylem yapma arasında gidip gelir, sonra yeniden akıl yürütmeden önce sonucu gözlemler. Daha zor hedefler için modelin önce planlamasını (alt görevlere ayırmasını) ve sonra yürütmesini sağlayın; böylece hiçbir araç çalışmadan önce planı inceleyebilir ve hatta onaylayabilirsiniz. Bu döngüleri gözlemlenebilir ve kesilebilir tutun. Okuyabildiğiniz bir planı durdurabilirsiniz.

### Sonuç doğuran eylemler için insanları döngüde tutun

Araç başına ve eylem başına, modelin tek başına davranıp davranamayacağına ya da önce sormak zorunda olup olmadığına karar verin. Geri döndürülebilir, düşük riskli eylemler (arama, taslak hazırlama) gözetimsiz çalışabilir. Sonuç doğuran ya da geri döndürülemez olanlar (dış iletişim göndermek, para taşımak, üretim verisini değiştirmek, bir vatandaşın dosyasına karar vermek) hayır deme konusunda gerçek yetkisi olan bir [döngüdeki insan](https://en.wikipedia.org/wiki/Human-in-the-loop) kapısına ihtiyaç duyar. Mümkün olan her yerde geri döndürülebilirlik için tasarlayın: bir değişikliği işlemek yerine hazırlamayı (staging) tercih edin ve geri almayı birinci sınıf bir özellik yapın; böylece hatalı bir eylem bir olaya değil, birkaç dakikaya mal olur.

### Güvenlik modelini düşmanca ele alın

Ajanlar, bölüm 4.2'de anlatılan saldırı yüzeyini genişletir. Başlıca tehdit [istem enjeksiyonudur](https://en.wikipedia.org/wiki/Prompt_injection): ajanın okuyup itaat ettiği bir web sayfasına, belgeye ya da e-postaya gizlenmiş kötü amaçlı talimatlar. Yakından ilişkili olan [karışık vekil problemidir](https://en.wikipedia.org/wiki/Confused_deputy_problem); burada bir saldırgan ayrıcalıklı bir ajanı kendi meşru erişimini kötüye kullanmaya kandırır, örneğin ajanın çağırmasına izin verilen bir araç üzerinden veri sızdırmak gibi. Ajanın içeri aldığı her içeriğin düşmanca olabileceğini varsayın. Güvenilen talimatları güvenilmeyen verilerden ayırın, ele geçirilmiş bir ajanın hassas sistemlere ulaşamaması için araçları kısıtlayın ve ham model çıktısının doğrulama olmadan geri döndürülemez bir eylemi tetiklemesine asla izin vermeyin.

### Görev başarısına göre değerlendirin ve belirlenimsizliği için gerileme testi yapın

Ajanları, dökümün zekice ses verip vermediğine değil, görevi başarıp başarmadığına göre yargılayın. Denetlenebilir başarı ölçütleri olan temsil edici hedeflerden oluşan bir değerlendirme kümesi oluşturun (bilet doğru önceliği aldı mı, iade politikayla eşleşti mi) ve her istem, model ya da araç değişikliğinde çalıştırın. Ajanlar belirlenimsiz olduğundan tek bir geçiş çok az şey kanıtlar: her durumu birkaç kez çalıştırın ve geçti ya da kaldı yerine bir başarı oranı izleyin. Bu, bölüm 6.3 ve 6.2'nin (makine öğrenmesi mühendisliği ve MLOps) çevrimdışı ve çevrimiçi değerlendirme disiplinini, çıktısı bir eylem dizisi olan sistemlere genişletir.

### Gözlemlenebilirlik, maliyet ve başarısızlık yönetimi için çalıştırmaları araçlandırın

Göremediğinizi yönetemezsiniz. Her ajan çalıştırmasını uçtan uca izleyin (bölüm 6.6): hedef, her akıl yürütme adımı, argümanları ve sonucuyla her araç çağrısı, harcanan token'lar ve nihai sonuç. Bu izleme aynı anda hata ayıklayıcınız, denetim iziniz ve maliyet ölçeriniz olur. Adımlar, süre ve harcama için sert bütçeler koyun, çünkü döngüye giren bir ajan gecikme ve parayı hızla yakabilir. Başarısızlığı açıkça ele alın: geçici araç hatalarını geri çekilmeyle yeniden deneyin, ama modelin başarısız bir eylemi tekrarladığı döngüleri tespit edin ve çırpınmak yerine güvenle başarısız olun.

## Ödünleşimler: artılar ve eksiler

| Seçim | Artılar | Eksiler | En iyi olduğu durum |
|---|---|---|---|
| Sabit iş akışı (model yuvaları doldurur) | Öngörülebilir, ucuz, test etmesi ve denetlemesi kolay | Katı; öngörülmemiş yollarda bozulur | Adımlar önceden bilinir |
| Otonom tek ajan | Esnek; açık uçlu hedefleri halleder | Denetlemesi, değerlendirmesi ve sınırlaması daha zor | Yol önceden belirlenemez |
| Çok ajanlı orkestrasyon | Paralellik; özelleşmiş roller | Koordinasyon maliyeti, birikmiş hatalar, daha yüksek harcama | Bir görev gerçekten bağımsız parçalara ayrışır |
| Gözetimsiz eylem | Hızlı, düşük sürtünme | Hatalar denetimsiz yürütülür | Eylemler geri döndürülebilir ve düşük risklidir |
| Döngüdeki insan kapısı | Güvenlik, hesap verebilirlik, geri döndürülebilirlik | Daha yavaş; inceleyici kapasitesi gerekir | Eylemler sonuç doğurur ya da geri döndürülemezdir |

Merkezi gerilim özerklik ile kontrol arasındadır. Daha fazla özerklik daha fazla durumu halleder ama daha fazla güvenlik bariyeri, daha fazla değerlendirme ve daha fazla para ister ve tahmin etmesi daha zor biçimlerde başarısız olur. Çok ajanlı tasarımlar takımları zarafetle ayartır, ama her ek ajan koordinasyon yükü ve küçük bir hatanın yanlış bir sonuca birikebileceği bir yer daha ekler. Gerilimi, sorunu çözen en az özerklikle başlayarak ve özgürlüğü yalnızca somut bir görev sizi zorladığında, her zaman eşleşen bir güvenlik bariyeriyle birlikte ekleyerek çözün.

## Takımınızla tartışılacak sorular

1. **Bu özellik gerçekten bir ajana ihtiyaç duyuyor mu, yoksa sabit bir iş akışı daha güvenli ve ucuz mu olurdu?** Özerklik ayartıcıdır, ama çoğu işin, düzenlenmiş bir işlem hattının çok daha az riskle hallettiği bilinebilir adımları vardır. Büyük bir takım için varsayılan olarak ajanları seçmek, her grubun daha basit bir tasarımın önleyeceği değerlendirme, izleme ve güvenlik yüklerini üstlenmesi demektir. Belirli görevi getirin ve adımlarının önceden belirlenip belirlenemeyeceğini sorun; belirlenebiliyorsa bir ajan büyük olasılıkla aşırı mühendisliktir. Açık uçlu özerkliği, yolun gerçekten duruma göre değiştiği hedeflere saklayın. Cevap, özelliklerin çoğunu bir iş akışına doğru itmeli ve küçük, bilinçli bir kümeyi gerçek ajanlar olarak bırakmalıdır.

2. **Ajanımızın çağırabildiği her araç için, ele geçirilmiş bir ajanın onunla yapabileceği en kötü şey nedir ve bunu ne engeller?** İstem enjeksiyonu ve karışık vekil saldırıları ajanın kendi meşru erişimini sizin aleyhinize çevirir; bu yüzden doğru mercek düşmancadır (bölüm 4.2). Her aracı, ayrıcalık kapsamını ve içeri alınan içerik içinden kaçırılmış kötü amaçlı bir talimatın ona ulaşıp ulaşamayacağını envantere alın. Ajanları iç sistemlere bağlayan kurumlar için en az ayrıcalığın, kum havuzunun ve geri döndürülemez eylemlerde insan kapılarının gerçek olduğu yer burasıdır. Araçların listesini ve her birinin tuttuğu kimlik bilgilerini getirin. Herhangi bir sonuç doğuran eyleme doğrulama ya da bir insan denetimi olmadan ulaşılabiliyorsa, düzeltilecek ilk şey budur.

3. **Her çalıştırma makul göründüğünde, bir ajanın başarı oranının düştüğünü nasıl anlarız?** Ajanlar belirlenimsizdir; bu yüzden iyi okunan bir döküm yine de yanlış eylemi yapmış olabilir ve tek bir yeşil çalıştırma hiçbir şey kanıtlamaz. Denetlenebilir sonuçları olan hedeflerden oluşan bir değerlendirme kümeniz olup olmadığını, tek bir geçiş yerine bir başarı oranı üretmek için her durum başına birçok kez çalıştırılıp çalıştırılmadığını sorun. Yüksek riskli ya da kamusal devreye almalar için, bir şey ters gittiğinde çalıştırma izlerinin tam olarak ne olduğunu yeniden kurgulamanıza nasıl izin verdiğini tartışın (bölüm 6.5 ve 6.6). Tek sinyaliniz kullanıcı şikâyetleriyse zaten çok geçtir. Cevap, bir olaydan sonra değil, ölçekten önce bir değerlendirme koşum takımını finanse etmelidir.

4. **Bu ajanın eylemlerinden hangileri gerçekten geri döndürülemez, bunları onaylama yetkisi kimde ve o kapıyı kadrolandıracak inceleyici kapasitemiz var mı?** Cazibe, modelin her yerde gözetimsiz hareket etmesine izin vermektir, ama bir insan kapısı yalnızca ajan sorduğunda hayır deme yetkisi olan isimli bir kişi hazır olduğunda gerçektir. Büyük bir takım için kimsenin sahip olmadığı bir onay kuyruğu sessizce bir onay mührüne dönüşür ve tasarladığınız güvenlik hacim altında buharlaşır. Ajanın yapabileceği eylemlerin tam listesini getirin, her birini geri döndürülebilir ya da geri döndürülemez olarak işaretleyin ve bir inceleyiciye düşecek düşük güvenli durumların günlük hacmini tahmin edin. Bir kapının sürtünmesini ve kadro maliyetini, gözetimsiz bir hatanın etki alanına karşı tartın ve geri döndürülemez bir eylemi bir inceleyici daha eklemek yerine, hazırlanmış ve geri alınabilir bir eyleme yeniden tasarlamayı tercih edin. Kurumsal ve kamu ortamlarında her sonuç doğuran eylemi hesap verebilir bir yetkiliye ve bir değişiklik yönetimi kaydına bağlayın, çünkü bir vatandaşı ya da müşteriyi etkileyen ve hiçbir insanın onaylamadığı otonom bir eylem, bir denetimin bulacağı tam da o başarısızlıktır.

5. **Çok ajanlı bir tasarıma görev gerçekten ayrıştığı için mi uzanıyoruz, yoksa zarif göründüğü için mi?** İşi özelleşmiş ajanlar arasında bölmek ayartıcıdır, ama her ekstra ajan koordinasyon yükü ve küçük bir hatanın yanlış bir sonuca biriktiği bir yer daha ekler. Büyük bir kurum için maliyet yalnızca harcama ve gecikme değildir: çok ajanlı bir sistemi izlemek, değerlendirmek ve başarısız olduğunda akıl yürütmek çok daha zordur; bu yüzden yönetişim yükü eklediğiniz her rolle katlanır. Görevi getirin ve hangi parçaların bağımsız ve paralel çalıştığını somut olarak gösterin, sonra çok ajanlı bir sürümün ölçülen başarı oranını ve maliyetini aynı değerlendirme kümesinde tek bir ajanla karşılaştırın. Tek ajan kazanır ya da berabere kalırsa, zarif tasarım aşırı mühendisliktir. Düzenlemeye tabi ya da kamusal devreye almalarda, zincirdeki her ajanın bir gözetim organının inceleyebilmesi gereken bir bileşen daha olduğunu unutmayın; bu yüzden gerekçelendiremediğiniz eklenmiş yapı, eklenmiş yükümlülüktür.

6. **Bir ajanın adımları, süresi ve harcaması üzerindeki sert bütçeler nedir ve döngüye giren bir ajan maliyet ya da gecikme biriktirmeden nasıl yakalanır?** Başarısız bir eylemi tekrarlayan bir ajan uyarı vermeden para ve zaman yakabilir; bu yüzden sınırsız özerklik bir güvenlik riski olduğu kadar mali bir risktir. Birçok ajan çalıştıran büyük bir takım için tek bir kötü davranan döngü bir bulut faturasını sivriltebilir ya da diğer her iş yükünü aç bırakan bir hız sınırını tüketebilir; bu da çalıştırma başına tavanları tek bir takımın değil, ortak bir operasyonel kaygı yapar. Her ajan için mevcut adım, süre ve token bütçelerini, aşıldığında tetiklenen uyarıyı ve çırpınmak yerine güvenle başarısız olan döngü tespitini getirin. Meşru biçimde zor bir görevi kesebilecek sıkı bütçeleri, maliyetin kontrolden çıkmasına izin veren gevşek olanlara karşı tartın. Harcamanın tahmin edilip gerekçelendirilmesi gereken kurumsal ve kamu ortamlarında, maliyeti sınırsız bir ajan, bir bütçe incelemesinde ya da bir denetimde savunamayacağınız bir kalemdir.

## Sektör merceği

**Girişim.** Çekirdek değerinize dokunan tek bir dar ajanı, barındırılan bir model üzerinde, işi yapan en küçük araç kümesiyle ve adımlar ile harcama üzerinde sert bir tavanla yayına alın. Çok ajanlı demoya direnin: kıt mühendislik dikkatiniz, sürdüremeyeceğiniz rolleri koordine etmekten çok, tek bir ajanın özerkliğini sınırlamaya ve çalıştırmalarını izlemeye harcanmaya değer. Her sonuç doğuran eylemi tek bir "taslak hazırla, asla gönderme" kapısının arkasında tutun; böylece bir hata bir olaya değil, geri almak için bir tıklamaya mal olur.

**Küçük işletme.** Bir değerlendirme koşum takımını ya da kum havuzunu çalıştıracak kimsenizin olmadığı yerde, zaten güvendiğiniz araçlara gömülü ajanları tercih edin ve yalnızca gözle denetleyebileceğiniz özerkliği açın. Sizin adınıza gönderebilen, ödeme yapabilen ya da silebilen her ajanı, bir kişi her eylemi onaylayana kadar kapalı tutulacak bir şey olarak ele alın, çünkü bir müşteriye giden yanlış otomatik bir mesaj size ilişkiyi kaybettirir. Ajanın ne yaptığını gösteren ve otomasyonu kapatmanıza izin veren satıcıları tercih edin.

**Kurumsal.** Sorun, ajanları birçok takım arasında yönetmektir: özerkliği sınırlamak için ortak kalıplar, en az ayrıcalıklı araç kimlik bilgileri, kum havuzu, döngüdeki insan kapıları ve hiçbir grubun güvenlik bariyerlerini yeniden icat etmemesi için uçtan uca izleme. Ajanları iç sistemlere bir insanın sahip olacağı aynı erişim denetimleri altında bağlayın, geri döndürülemez eylemleri isimli onaylayıcıların ve değişiklik yönetiminin arkasına kapılayın ve portföyü başarı oranı metrikleri, çalıştırma başına bütçeler ve düşmanca enjeksiyon testiyle yönetin. İzleme ve değerlendirme katmanını standartlaştırın; böylece herhangi bir ajanın davranışı yeniden kurgulanabilir ve denetlenebilir.

**Kamu.** Tedarik, şeffaflık ve kamusal hesap verebilirlik her seçimi sınırlar. Ajanları olguları toplamak ve taslak hazırlamakla sınırlı tutun ve bir vatandaşı etkileyen her kararı hesap verebilir bir insana saklayın, çünkü bir kamu sektörü kararının sorumluluğu bir modele devredilemez. Bir gözetim organı hangi kaynaklara başvurulduğunu ve ne yapıldığını görebilsin diye her çalıştırmayı günlüğe alın, satıcıların ajanın araçlarını ve sınırlamalarını açıklamasını isteyin ve ajanın sınırlı görev alanının ötesinde hareket etmeyi reddettiğini düşmanca bir değerlendirme kümesiyle kanıtlayın.

## Örnekler

**Girişim.** Beş kişilik bir analitik girişimi bir destek triyaj ajanı kurar. Gelen bir bileti okur, belgelerde arama yapar ve ya bir yanıt taslağı hazırlar ya da bileti bir insana yönlendirir; araç kümesinin tamamı budur. Kimlik bilgileri salt okunurdur, artı bir kişi gönder'e tıklamadan asla göndermeyen tek bir "taslak oluştur" eylemi. Kurucular bir biletin neden oraya yönlendirildiğini görebilsin diye her çalıştırma izlenir ve elli gerçek biletten oluşan gecelik bir değerlendirme kümesi, bir yönlendirme doğruluğu oranını izlemek için ajanı her biletle beş kez çalıştırır. Bir rakibin zekice çok ajanlı demosu onları ayarttığında, görevleri ayrışmadığı için tek ajanda kalırlar.

**Kurumsal.** Bir banka, operasyon personelinin başarısız ödemeleri mutabık kılmasına yardım eden bir ajan kurar. Ajan, bir insan memurun sahip olduğu aynı erişim denetimleri altında, yalnızca mutabakata kapsamlanmış en az ayrıcalıklı hizmet kimlik bilgileriyle iç sistemlere entegre olur. Ajan serbestçe araştırabilir (defterleri okuyabilir, işlem geçmişinde arama yapabilir), ama para taşıyan ya da bir kaydı düzenleyen her eylem hazırlanır ve değişiklik yönetimini karşılayan isimli bir insan onaylayıcı gerektirir. İçeri alınan belgeler istem enjeksiyonunu körletmek için güvenilmez sayılır, araçlar kum havuzunda çalışır ve her çalıştırma denetim için uçtan uca izlenir. Çevrimdışı bir değerlendirme kümesi her model ya da istem değişikliğini kapılar ve çalıştırma başına bütçeler adımları ve harcamayı sınırlar; böylece döngüye giren bir ajan maliyet ya da gecikme biriktiremez.

**Kamu.** Bir yardım kurumu, vaka çalışanlarının bir başvurunun olgularını bir araya getirmesine yardım eden bir ajanı pilot olarak dener: kayıtları çekmek, uygunluk kurallarını kontrol etmek ve bir özet taslağı hazırlamak. Kurum sert bir çizgi çeker: ajan toplar ve taslak hazırlar, ama bir vatandaşı etkileyen her kararı bir insan vaka çalışanı verir ve sahiplenir, çünkü kamu sektörü kararlarının hesap verebilirliği bir modele devredilemez (bölüm 6.5). Her çalıştırma tamamen günlüğe alınır; hangi kaynaklara başvurulduğunu ve neyin taslağının hazırlandığını göstererek bir gözetim organının herhangi bir dosyayı denetlemesine izin verir. Özerklik bilinçli olarak oku ve taslak hazırla ile sınırlıdır, araçlar en az ayrıcalıklı ve kum havuzludur ve düşmanca bir değerlendirme kümesi ajanın olguları toplamanın ötesinde hareket etmeyi reddettiğini doğrular.

## İş gerekçesi: motivasyonlar, YG ve TSM

Ajanlar, eskiden sistemler arasında tıklayan bir insan gerektiren çok adımlı işi otomatikleştirerek getiri sağlar: triyaj, mutabakat, araştırma ve rutin operasyonlar. Değer, her adımda bir insan olmadan tamamlanan iş, daha hızlı çevrim süreleri ve muhakeme ağırlıklı görevler için serbest kalan personel olarak görünür. Ajanlar mevcut LLM'ler ve araçlar üzerine kurulduğundan çalışan bir prototipe giden süre kısadır; takımların gereğinden fazla inşa etmesinin nedeni de tam olarak budur.

Toplam sahip olma maliyeti, ajanların düz LLM özelliklerinden ayrıldığı yerdir. Çıkarım maliyetinin üstüne araç entegrasyonları, kum havuzu ve izin tesisatı, değerlendirme koşum takımı, izleme ve gözlemlenebilirlik yığını (bölüm 6.6) ve onay kapılarını kadrolandıran insan inceleyiciler için ödeme yaparsınız. Döngüye giren ya da kötü sınırlanmış bir ajan, uyarı vermeden sivrilebilen değişken bir maliyet ekler; bu yüzden adımlar ve harcama üzerindeki bütçeler tasarımın bir parçasıdır, sonradan akla gelen bir şey değil. Benimsememenin maliyeti, rakiplerinizin otomatikleştirdiği daha yavaş operasyonlar ve elle yapılan angaryadır. Dikkatsizce benimsemenin maliyeti, yanlış mesaj gönderen, veri sızdıran ya da hesap verilemez bir karar veren otonom bir eylemdir. Gerekçeyi liderliğe, somut bir otomasyon hedefini güvenlik bariyerleri, değerlendirme ve insan gözetimi için somut bir planla eşleştirerek ve bariyerlerin maliyetin çoğunu oluşturduğu konusunda dürüst olarak sunun.

## Anti-kalıplar ve tuzaklar

- **İş akışının yeteceği yerde ajan.** Adımları bilinebilir bir görev için özerkliğin tüm riskini üstlenmek.
- **Aşırı geniş araçlar ve kimlik bilgileri.** Dar, en az ayrıcalıklı olanlar yerine tek bir "her şeyi yap" aracı.
- **İstem enjeksiyonu körlüğü.** Güvenilmeyen içeriği gerçek ayrıcalıkları olan bir ajana beslemek.
- **Geri döndürülemez eylemlerde insan kapısı yok.** Modelin denetimsiz göndermesine, ödemesine ya da silmesine izin vermek.
- **Çok ajanlı tiyatro.** Basit bir görevi ajanlar arasında bölüp bir kazanç olmadan koordinasyon maliyeti ödemek.
- **Hissiyata dayalı değerlendirme.** Görev başarı oranı yerine dökümün nasıl okunduğuyla yargılamak.
- **Sınırsız döngüler.** Adımlar, süre ya da harcama üzerinde tavan olmaması; sıkışan bir ajan para ve gecikme yakar.
- **İzlenmeyen çalıştırmalar.** Ajanın ne yaptığına dair kayıt olmaması; hata ayıklayamamak, denetleyememek ya da hesap verememek.

## Olgunluk modeli

- **Düzey 1, Başlangıç:** Ajanlar geniş araç erişimi ve hiçbir sınır olmadan gelişigüzel prototiplenir. Başarı, bir şey bozulduktan sonra reaktif olarak demolarla yargılanır. Değerlendirme kümesi, izleme ya da sonuç doğuran eylemlerde insan kapısı yoktur.
- **Düzey 2, Geliştirme:** Bazı ajanların sınırlı döngüleri ve en az ayrıcalıklı araçları vardır ve temel izleme mevcuttur, ama uygulama takımdan takıma değişir. Elle hazırlanmış bir değerlendirme kümesi birkaç projede ağır gerilemeleri yakalarken diğerlerinde hiç yoktur. İnsan onayı en bariz geri döndürülemez eylemleri korur, ama kapsam eşitsiz ve belgelenmemiştir.
- **Düzey 3, Standartlaştırma:** Ortak kalıplar özerkliği, araç izinlerini, kum havuzunu ve döngüdeki insan kapılarını yönetir; belgelenmiş ve her takımda uygulanmıştır. Her sonuç doğuran eylem kapılanır ya da doğrulanır, ajanlar uçtan uca izlenir ve başarı oranı puanlamalı otomatik bir değerlendirme kümesi her değişiklikte çalışır. İstem enjeksiyonu, tanımlı bir müdahaleyle kalıcı bir tehdit olarak ele alınır.
- **Düzey 4, Yönetme:** Ajan portföyü temel çizgilere karşı ölçülür ve kontrol edilir. Görev başına başarı oranı, istem enjeksiyonu savunma geçiş oranı, çalıştırma başına maliyet ve adım sayısı, insan onayı gecikmesi ve döngü ya da başarısızlık olayları metrik olarak izlenir; geri alma ve durdurma eşikleri şikâyetlere değil bu kanıta göre uygulanır. Adımlar, süre ve harcama üzerindeki çalıştırma başına bütçeler izlenir ve herhangi bir metrikteki gerileme, bir olaydan sonra değil ölçekten önce eylemi tetikler.
- **Düzey 5, Orkestrasyon:** Özerklik politikayla görev riskine uydurulur ve sonuçlar geldikçe sürekli ayarlanır. Süregelen çevrimdışı ve çevrimiçi değerlendirme, ajan davranışını iş sonuçlarına bağlar ve kurum, risk tablosu değiştikçe ajanları düzenli olarak emekliye ayırır, kapsamlarını yeniden belirler ya da izinlerini yeniden verir. İzleme, maliyet bütçeleri ve denetim izleri portföy genelinde tekdüzedir; enjeksiyon ve karışık vekil savunmaları düşmanca test edilir; otonom eylemler için hesap verebilirlik nettir ve denetlenebilir.

## Tartışma fikirleri

1. Mevcut LLM özelliklerinizden hangileri sessizce ajan haline geldi ve her birinin özerkliği bilerek sınırlandı mı?
2. Her ajan aracı için, bir saldırganın onu enjekte edilmiş içerik yoluyla kötüye kullanmasının en ucuz yolu nedir ve bunu ne engeller?
3. Çok ajanlı tasarımları nerede seçtiniz ve koordinasyon maliyetinin tek bir ajana kıyasla karşılığını verdiğini gösterebilir misiniz?
4. Ajan eylemlerinden hangileri gerçekten geri döndürülemez ve her biri geri döndürülebilir ya da hazırlanabilir olacak şekilde yeniden tasarlanabilir mi?
5. Bir ajan yarın zararlı bir eylem gerçekleştirse, tam olarak ne yaptığını ve kimin hesap vermesi gerektiğini yeniden kurgulayabilir miydiniz?

## Önemli çıkarımlar

- Bir ajan; araçlar, hafıza ve bir hedefle bir döngü içindeki bir LLM'dir. Risk metinde değil, döngüde ve araçlarda yaşar.
- Adımlar biliniyorsa sabit bir iş akışını tercih edin; özerkliği gerçekten açık uçlu hedeflere saklayın ve sıkı biçimde sınırlayın.
- Araç kullanımı çekirdek yetenektir. Her araca en az ayrıcalık, doğrulanmış bir şema ve bir kum havuzu verin.
- Sonuç doğuran ve geri döndürülemez eylemleri gerçek yetkisi olan bir insanın arkasına kapılayın ve ucuz geri alma için tasarlayın.
- Ajanları düşmanca ele alın: istem enjeksiyonuna ve karışık vekil istismarına karşı savunun (bölüm 4.2).
- Birçok çalıştırma boyunca görev başarı oranına göre değerlendirin ve her çalıştırmayı hata ayıklama, maliyet denetimi ve denetim için izleyin (bölüm 6.5 ve 6.6).
- Çoğu zaman doğru cevap hiç ajan kurmamaktır.

## Kaynaklar ve ileri okuma

- Shunyu Yao et al., *ReAct: Synergising Reasoning and Acting in Language Models*.
- Timo Schick et al., *Toolformer: Language Models Can Teach Themselves to Use Tools*.
- Anthropic, *Building Effective Agents* (engineering guidance on workflows versus agents).
- OWASP Foundation, *OWASP Top 10 for Large Language Model Applications* (including prompt injection and excessive agency).
- Simon Willison, writing on prompt injection and the "lethal trifecta" for AI agents.
- Norman Hardy, *The Confused Deputy* (the classic statement of the confused-deputy problem).
- Chip Huyen, *AI Engineering: Building Applications with Foundation Models*.
- Stuart Russell and Peter Norvig, *Artificial Intelligence: A Modern Approach* (intelligent agents and rational action).
