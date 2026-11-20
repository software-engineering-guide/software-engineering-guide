# 6.6 Yapay zeka altyapısı ve operasyonları

## Genel bakış ve motivasyon

Yapay zeka altyapısı ve operasyonları; yapay zeka iş yüklerinin gerektirdiği özelleşmiş hesaplama, depolama ve sunum sistemlerini sağlama, zamanlama ve çalıştırma disiplinidir ve bunu uygun maliyetle, güvenilir ve gözlemlenebilir biçimde yapmayı hedefler. Modern yapay zekayı çalıştırmak pahalıdır. Büyük modelleri eğitmek ve sunmak kıt hızlandırıcılar ([GPU'lar](https://en.wikipedia.org/wiki/Graphics_processing_unit) ve [TPU'lar](https://en.wikipedia.org/wiki/Tensor_Processing_Unit)), yüksek bant genişlikli ağ, getirme için büyük ölçekli vektör depolama (benzer öğeler hızla bulunabilsin diye veriyi sayısal vektörler olarak indeksleme) ve gecikme ile işleme hızı için ayarlanmış sunum katmanları gerektirir. Bu altyapıyı doğru kurmak, sürdürülebilir biçimde ölçeklenen yapay zeka ile bütçeyi sessizce tüketip az teslim eden yapay zeka arasındaki farktır.

Büyük takımlar için temel sorunlar ölçek, kıtlık ve maliyettir. Hızlandırıcılar sınırlı ve pahalıdır; bu yüzden zamanlama ve kullanım oranı çok önemlidir. Boştaki GPU'lar yakılan paradır ve kötü gruplanmış çıkarım, istek başına maliyeti katlar. Getirme ağırlıklı uygulamalar büyürken hızlı kalan [vektör veritabanlarına](https://en.wikipedia.org/wiki/Vector_database) ihtiyaç duyar. Üretken yapay zeka uygulamaları güvenle işletilmek ve zamanla iyileşmek için istem sürümlemesine, değerlendirme işlem hatlarına ve gözlemlenebilirliğe (bazen LLMOps denir) ihtiyaç duyar. Ortak altyapı ve operasyonel disiplin olmadan her takım aynı savaşları verir ve maliyetler kontrolden çıkar.

Kamu ve düzenlemeye tabi kurumlar veri egemenliği, güvenlik ve öngörülebilir harcama konusunda gereksinimler ekler. Hassas veri ve modeller kontrollü sınırların dışına asla çıkmasın diye şirket içi ya da egemen bulut dağıtımına ihtiyaç duyabilirler. Altyapı harcamasını tahmin edip gerekçelendirmeleri ve güvenlik ile erişilebilirlik standartlarını karşılamaları gerekir. Bu ortamlarda yapay zeka altyapı kararları çok yıllık sonuçlar taşır; bu yüzden onları tedarik, güvenlik ve çıkış aklınızda olarak verin.

## Temel ilkeler

- Hızlandırıcı hesaplamayı, istiflenecek değil zamanlanıp kullanılacak kıt ve pahalı bir kaynak olarak ele alın.
- Ham kapasiteyi değil, yararlı iş birimi başına maliyeti optimize edin.
- Modelleri ve donanımı göreve uygun boyutlandırın; en büyük seçenek nadiren en uygun maliyetli olandır.
- Sunumu, gruplama ve önbelleklemeyi birinci sınıf teknikler olarak kullanarak gecikme ve işleme hızı için tasarlayın.
- Yapay zeka sistemlerini gözlemlenebilir yapın: maliyeti, gecikmeyi, kaliteyi ve hataları sürekli izleyin.
- İstemleri ve modelleri koddaki titizlikle sürümleyin ve değerlendirin.
- Altyapı ve sunum seçimlerinde taşınabilirliği planlayın ve kilitlenmeden kaçının.

## Öneriler

### Hızlandırıcı hesaplamayı planlayın ve denetleyin

Eğitim ve çıkarım için talebi ayrı ayrı tahmin edin, çünkü şekilleri farklıdır. Eğitim ani yükselişlidir ve zamanlanabilir; çıkarım süreklidir ve gecikmeye duyarlıdır. Kıt GPU'ları ve TPU'ları takımlar arasında paylaşmak, iş yüklerini önceliklendirmek ve kullanım oranını yükseltmek için zamanlayıcılar ve kotalar kullanın. Kullanım oranını ölçün ve kronik boşta kalmayı düzeltilecek bir sorun sayın. Maliyeti denetlemek için temel yük için ayrılmış kapasiteyi, ani yükselişler için isteğe bağlı ya da spot kapasiteyle karıştırın. Daha ucuz ya da daha küçük hızlandırıcıların ya da hafif modeller için CPU çıkarımının yeterli olup olmayacağını düşünün. Bulut, şirket içi ve hibrit arasında ölçeğinizdeki maliyete, veri egemenliği ihtiyaçlarına ve ani yükselme örüntülerine göre seçim yapın ve bir çıkış yolu tutun.

### Getirme altyapısını kurun: gömmeler ve vektör veritabanları

Getirme destekli üretim uygulamaları için [gömmeler](https://en.wikipedia.org/wiki/Word_embedding) (benzer öğeleri birbirine yakın yerleştiren sayısal vektör temsilleri) üretecek altyapıyı kurun ve onları, ölçeğinizde hızlı [yaklaşık en yakın komşu aramasını](https://en.wikipedia.org/wiki/Nearest_neighbor_search) (her birini tek tek karşılaştırmadan en benzer vektörleri bulmak) destekleyen bir vektör veritabanında saklayın. Üç şey için plan yapın: gömme üretiminin maliyeti ve gecikmesi, belgeler değiştikçe indeks güncelliği ve indeksleri tutarlı tutmanın operasyonel yükü. Ölçeğinize ve kilitlenme toleransınıza özel bir vektör veritabanının, mevcut bir veritabanının vektör destekli bir uzantısının ya da yönetilen bir hizmetin en uygun olup olmadığını değerlendirin. Getirme gecikmesini ve anımsamayı izleyin, çünkü getirme kalitesi doğrudan uygulama kalitesini belirler.

### Model sunumunu optimize edin: gruplama, önbellekleme ve gecikme

Sunum, çıkarım maliyetinin ve kullanıcı deneyiminin belirlendiği yerdir. Birden çok isteği birlikte işleyip hızlandırıcı işleme hızını yükseltmek için **gruplamayı** kullanın; grup boyutunu gecikmeyle dengeleyin. **Önbelleklemeyi** cesurca kullanın: aynı ya da anlamsal olarak benzer istekleri önbelleğe alın, gömmeleri önbelleğe alın ve paylaşılan bağlamı yeniden hesaplamaktan kaçınmak için platformun desteklediği yerde istem ya da önek önbelleklemesinden yararlanın. Net gecikme hedefleri koyun ve yalnızca ortalamaları değil, kuyruk gecikmesini ölçün. İstekleri uygun boyutlu modellere yönlendirin: kolay durumlar için küçük bir model, daha büyük olanı yalnızca gerektiğinde. Sunumu talebe göre otomatik ölçekleyin ve kapasitenizi ve maliyet eğrinizi bilmek için lansmandan önce yük testi yapın.

### LLMOps uygulayın: istem sürümleme, değerlendirme işlem hatları ve gözlemlenebilirlik

İstemleri kaynak kontrolünde, inceleme ve geri alma yeteneğiyle sürümlenmiş yapıtlar olarak ele alın. İstemler ya da modeller değiştiğinde çevrimdışı test takımlarını otomatik çalıştıran değerlendirme işlem hatları kurun; böylece gerilemeleri yayından önce yakalarsınız. Üretimi kapsamlı biçimde araçlandırın: girdileri, çıktıları, gecikmeyi, token kullanımını, maliyeti ve hataları örnekleme ve gizlilik güvenceleriyle günlüğe alın. Kalite sinyallerini ve kullanıcı geri bildirimini çevrimiçi izleyin. Bu gözlemlenebilirlik, bozulmayı yakalamanıza, maliyeti denetlemenize, başarısızlıkları ayıklamanıza ve sistemleri güvenle iyileştirmenize olanak verir: üretimdeki üretken yapay zekanın operasyonel omurgası.

### Maliyeti amansızca ve gözlemlenebilir biçimde yönetin

Yapay zeka harcamasını takımlara ve kullanım durumlarına atfedin; böylece maliyet görünür ve sahipli olur. Bütçeler ve uyarılar koyun, istek başına ve sonuç başına maliyeti izleyin ve en büyük maliyet etkenlerini düzenli olarak gözden geçirin. Elinizdeki kollara başvurun: model boyutunu uyarlama, önbellekleme, gruplama, istem ve bağlam kırpma ve gereksinimleri karşılayan en ucuz dağıtımı seçme. Yapay zeka maliyetleri kullanımla şaşırtıcı biçimlerde ölçeklenebilir; bu yüzden hoş olmayan sürprizlerden kaçınmak için sürekli maliyet gözlemlenebilirliği şarttır.

## Ödünleşimler: artılar ve eksiler

| Karar | Seçenek A | Seçenek B | Ödünleşim |
|---|---|---|---|
| Hesaplama konumu | Bulut | Şirket içi | Esneklik ve düşük başlangıç maliyeti ile kontrol, egemenlik ve kararlı durum ekonomisi |
| Kapasite | Ayrılmış | İsteğe bağlı/spot | Öngörülebilir maliyet ile esneklik ve kesinti riski |
| Grup boyutu | Büyük gruplar | Küçük gruplar | İşleme hızı ve maliyet ile gecikme |
| Model boyutu | Büyük model | Küçük model | Kalite ile maliyet ve hız |
| Vektör deposu | Özel veritabanı | Mevcut veritabanı uzantısı | Ölçekte performans ile sadelik ve daha az sistem |
| Önbellekleme | Cesur | Asgari | Daha düşük maliyet ve gecikme ile güncellik ve karmaşıklık |

Baskın ödünleşim, maliyet ile gecikme ve kalite arasındadır. Gruplama, önbellekleme ve daha küçük modeller maliyeti keser ama gecikme ekleyebilir ya da kaliteyi düşürebilir. Doğru denge uygulamanızın toleransına bağlıdır. Şirket içi ile bulut, kontrol ve kararlı durum ekonomisini esnekliğe ve düşük taahhüde karşı takas eder; veri egemenliği ihtiyaçları ve ölçekle ağır biçimde şekillenen bir karardır.

## Takımınızla tartışılacak sorular

1. **Bugün yararlı sonuç başına maliyetimiz nedir ve hangi kol onu en çok oynatır?** Ham kapasite ve istek başına ortalamalar önemli rakamı gizler: gerçek bir değer birimini teslim etmenin maliyeti ve bunun kullanımla nasıl ölçeklendiği. Büyük bir takım için optimize edilmiş ve edilmemiş bir dağıtım arasındaki fark harcamada çoğu zaman birkaç katıdır; bu yüzden bu soru, faturaya dair belirsiz bir endişeyi sıralı bir düzeltme listesine çevirir. Takıma ve kullanım durumuna göre mevcut maliyet atfını, istek başına ve sonuç başına eğilimleri ve en büyük maliyet etkenlerini getirin. Kolları getiri sırasına göre tartışın: model boyutunu uyarlama, önbellekleme (önek ve anlamsal önbellekleme dahil), gruplama ve istem ya da bağlam kırpma. Kamuda, çok yıllı harcamayı tahmin etme ve gerekçelendirme baskısını ekleyin. Cevap, en büyük her maliyet etkenine bir omuz silkme değil, bir sahip ve bir kol atamalıdır.

2. **Mevcut çıkarım sağlayıcımız fiyatını ikiye katlasa ya da yarın çökse, ne kadar hızlı geçiş yapabiliriz?** Sessiz kilitlenmeyi kurmak kolay, ondan çıkmak acı vericidir ve sunum yığınları onun en derine saklandığı yerdir. Kurumlar ve özellikle kamu için taşınabilirlik bir incelik değil, bir tedarik ve süreklilik gereksinimidir. Mimarinizi getirin: modellerin bir iç arayüzün arkasında olup olmadığı, istemlerin ve değerlendirme takımlarının taşınabilir olup olmadığı ve ne kadar sağlayıcıya özgü sunum davranışına bağımlı olduğunuz. İzlenecek sinyal, değerlendirme takımınızı hiç ikinci bir sağlayıcıya ya da ikinci bir dağıtım hedefine karşı çalıştırıp çalıştırmadığınızdır. Geçiş aylar alacak ve çekirdek yolları yeniden yazdıracaksa, bunu şimdi ele alınacak bir tasarım kusuru sayın; çünkü egemen ve şirket içi seçenekler kısa bir uyarıyla zorunlu hale gelebilir.

3. **Şu anda hızlandırıcı kullanım oranımız nedir ve boştaki GPU'lar ve gruplanmamış çıkarım ne kadar yakıyor?** Hızlandırıcılar kıt ve pahalıdır; bu yüzden kronik boşta kalma ve istek başına sunum, daha fazla yeteneği finanse edebilecek bütçeleri sessizce boşaltır. GPU'ları takımlar arasında paylaşan büyük bir kurum için bu soru, zamanlamanın, kotaların ve önceliklerin kullanım oranını gerçekten yüksek tutup tutmadığını ya da istiflenmiş, az kullanılan donanımın norm olup olmadığını açığa çıkarır. Gerçek kullanım sayılarını, gruplama ve önbellekleme duruşunuzu ve yalnızca ortalamaları değil kuyruk gecikmesi ölçümlerinizi getirin, çünkü kullanıcılar yavaş kuyruğu hisseder. Eğitim ve çıkarım talebinin, farklı şekilleri göz önüne alınarak ayrı ayrı tahmin edilip edilmediğini ve hafif durumlar için daha küçük bir modelin ya da CPU çıkarımının yeterli olup olmayacağını tartışın. Cevap, geri kazanılacak belirli boşta kapasiteyi ve gruplanacak ya da uygun boyutlu bir modele yönlendirilecek belirli istekleri göstermelidir.

4. **Bir istem ya da model değişikliği yayına girdiğinde, sessiz bir kalite ya da maliyet gerilemesinin kullanıcılara ulaşmasını ne engeller?** Bir sunum yığını gecikme ve çalışma süresi açısından sağlıklı görünürken, döndürdüğü cevaplar sessizce kötüleşebilir ya da yeni bir istem istek başına token kullanımını ikiye katlayabilir. Birçok grubun istemleri düzenlediği ve modelleri bağımsız değiştirdiği büyük bir takım için kapısız bir değişiklik, bir üretim olayının beklemesidir ve etki alanı paylaşılan platformdaki her takımla büyür. Değerlendirme kapsamınızı getirin: hangi istemlerin ve modellerin çevrimdışı test takımları var, bu takımların her değişiklikte otomatik çalışıp çalışmadığı, bir yayını hangi kalite ve maliyet eşiklerinin kapıladığı ve ne kadar hızlı geri alabildiğiniz. İstemlerin inceleme ile kaynak kontrolünde yaşayıp yaşamadığını ya da birinin canlı bir sistem istemini hâlâ elle düzenleyip düzenleyemediğini tartışın. Kurumsal ve kamu ortamlarında her değişikliği bir denetim izine ve isimli bir onaylayıcıya bağlayın, çünkü "bunu kim değiştirdi ve ne test ettiniz" diye soran bir düzenleyicinin ihtiyacı olan cevap hatırlanan değil, kayıtlı olmalıdır.

5. **Bulut, şirket içi ve egemen dağıtım arasında nasıl karar veriyoruz ve pilotu değil, gerçek kararlı durum ekonomisini fiyatladık mı?** Hesaplama konumu seçimi yıllarca maliyet eğrinizi, veri egemenliği duruşunuzu ve çıkış seçeneklerinizi belirler; yine de çoğu zaman ölçekte üretime hiç benzemeyen bir pilotun bulut faturasına göre yapılır. Büyük bir kurum için esnek bulut kapasitesi başlamak için ucuzdur ve çıkarım sürekli çalışmaya başladığında tek büyük kalem olabilir; şirket içi ise düşük taahhüdü kontrol ve kararlı durum ekonomisiyle takas eder. Tahmini eğitim ve çıkarım hacimlerini, ayrılmış ya da sahip olunan donanımın isteğe bağlıyı geçtiği başabaş noktasını, veri ikameti ve güvenlik kısıtlarınızı ve hibriti savunan ani yükselme örüntülerini getirin. Kamu ve düzenlemeye tabi ortamlarda, kısa bir uyarıyla zorunlu hale gelebilecek egemen bulut ya da şirket içi gereksinimlerini tartın ve zorunlu bir geçişin çekirdek yolları yeniden yazdırmaması için mimarinin modelleri bir iç arayüzün arkasında tuttuğunu doğrulayın.

6. **Yapay zeka harcamamıza gerçekten sahip miyiz ve her takım kendi sürdürdüğü maliyeti görüp hesabını verebiliyor mu?** Yapay zeka maliyeti insanları şaşırtan biçimlerde kullanımla ölçeklenir ve atıf olmadan fatura, hiçbir takımın küçültmekten sorumlu hissetmediği tek bir opak sayı olarak düşer. Büyük bir kurumda kimsenin sahip olmadığı maliyeti kimse optimize etmez; bu yüzden soru, harcamanın bütçeler, uyarılar ve sonuç başına eğilimlerle takımlara ve kullanım durumlarına etiketlenip etiketlenmediği ya da yalnızca finans yükselttiğinde keşfedilip edilmediğidir. Maliyet atıf modelinizi, takım başına en büyük etkenleri ve her sahibin denetlediği kolları getirin: boyut uyarlama, önbellekleme, gruplama ve bağlam kırpma. Kurumsal ve kamu bütçeleri için çok yıllı altyapı harcamasını tahmin etme ve gerekçelendirme disiplinini ekleyin, çünkü hesaplama faturasını satır satır açıklayamayan bir kamu kurumu onu incelemede savunmakta zorlanır.

## Sektör merceği

**Girişim.** Kaçınabileceğiniz hiçbir altyapıya sahip olmayın. Barındırılan bir çıkarım API'sini çağırın, kolay istekleri küçük ucuz bir modele yönlendirin ve daha büyüğünü zor durumlara saklayın ve tekrarlanan istemlerin hiçbir şeye mal olmaması için cesurca önbelleğe alın. Kendi yönettiğiniz yerine yönetilen bir vektör veritabanı kullanın, istemleri git'te tutun ve her değişiklikten önce kısa bir değerlendirme betiği çalıştırın ve kontrolden çıkan bir fatura acıtmadan önce görünsün diye istek başına maliyeti günlüğe alın. En kıt kaynağınız mühendislik dikkatidir; bu yüzden işletilebilirliği satın alın ve geçişi ucuz tutun.

**Küçük işletme.** Platform takımınız yokken sunumu, getirmeyi ve gözlemlenebilirliği kadrolandırdığınız sistemler değil, zaten kullandığınız araçların içinde satın aldığınız şeyler olarak ele alın. Şeffaf, öngörülebilir fiyatlı yönetilen çıkarımı ve yönetilen vektör aramasını tercih edin ve ilk günden sert bir harcama tavanı ile bir fatura uyarısı koyun. Karar çerçevesini dürüstçe satın alma ya da inşa etme olarak kurun: GPU ya da bir vektör indeksi işletmek hacminizde nadiren karşılığını verir ve barındırılan bir API'nin arkasındaki küçük bir model genellikle ihtiyacı çabanın bir kesriyle karşılar.

**Kurumsal.** Sorun birçok takım arasında paylaşılan, asfaltlanmış yollu bir platformdur: kullanım oranını yükseltmek için zamanlayıcılar, kotalar ve önceliklerle havuzlanmış hızlandırıcılar, standart gruplama ve önbellekleme, uygun boyutlandırma yönlendiricileri ve her takıma ve kullanım durumuna atfedilen maliyet. İstem ve model değişikliklerini otomatik değerlendirme takımlarıyla kapılayın, sağlayıcılar ve dağıtım hedefleri değiştirilebilir kalsın diye arayüz katmanını standartlaştırın ve her grubun maliyetli, az kullanılan altyapıyı yeniden icat etmesi yerine sonuç başına maliyeti birinci sınıf bir metrik olarak yönetin.

**Kamu.** Veri egemenliği, güvenlik ve öngörülebilir harcama her seçimi şekillendirir. Hassas veri ve modeller kontrollü sınırların içinde kalsın diye şirket içi ya da egemen bulut dağıtımını tercih edin, kıt GPU'ları tedarikte gerekçelendirebileceğiniz kotalarla departmanlar arasında zamanlayın ve çok yıllı harcamayı satır satır savunmak için kapasiteyi tahmin edin. İstemleri ve modelleri kayıtlı bir denetim iziyle sürümleyin ve değerlendirin, maliyet ve kalite üzerinde kapsamlı gözlemlenebilirlik tutun ve yeni bir sağlayıcıya ya da egemen bir platforma zorunlu geçiş sizi mahsur bırakmasın diye modelleri bir iç arayüzün arkasında tutun.

## Örnekler

**Girişim.** Yapay zeka yazım özelliği çalıştıran küçük bir girişim, hiç GPU'su olmadan faturasını makul tuttu. Barındırılan bir çıkarım API'sini çağırdı, kolay istekleri daha ucuz küçük bir modele yönlendirdi ve daha büyüğünü zor durumlara sakladı ve tekrarlanan istemlerin cevaplarını önbelleğe aldı. İstemlerini her değişiklikten önce çalışan kısa bir değerlendirme betiğiyle git'te sakladı, getirme için kendisi işletmek zorunda kalmasın diye yönetilen bir vektör veritabanı kullandı ve kurucular harcamanın bir sürpriz haline gelmeden yükseldiğini görebilsin diye istek başına maliyeti günlüğe aldı.

**Kurumsal.** Yüksek trafikli bir LLM özelliği çalıştıran bir medya şirketi çıkarım maliyetlerini önemli ölçüde düşürdü. Kolay istekleri küçük bir modele yönlendirdi ve daha büyük bir modeli zor olanlara sakladı. Tekrarlanan sorguların yanıtlarını önbelleğe aldı ve paylaşılan sistem istemi için önek önbelleklemeyi etkinleştirdi. GPU'ları kullanım oranı yüksek kalsın diye paylaşılan bir zamanlayıcı üzerinden çalıştırdı, tüm istemleri değişiklikleri kapılayan otomatik bir değerlendirme takımıyla git'te sürümledi ve her ürün takımı kendi harcamasına sahip çıksın diye istek başına maliyeti araçlandırdı.

**Kamu.** Katı veri egemenliği kuralları olan bir ulusal kurum, hassas veri ve modeller kontrollü ortamından asla çıkmasın diye yapay zeka sistemlerini şirket içinde devreye aldı. Kıt GPU'ları departmanlar arasında kotalar ve önceliklerle zamanladı, çok yıllı tedariği gerekçelendirmek için kapasiteyi tahmin etti ve resmi belgeler üzerinde getirme için bir vektör arama platformu kurdu. İstemler ve modeller yayından önce sürümlendi ve değerlendirildi. Kapsamlı gözlemlenebilirlik maliyeti ve kaliteyi izledi ve mimari, bir çıkış yolunu korumak ve kilitlenmeden kaçınmak için modelleri bir iç arayüzün arkasında tuttu.

## İş gerekçesi: motivasyonlar, YG ve TSM

Disiplinli yapay zeka altyapısının motivasyonu açıktır. Ölçekte yapay zeka maliyetlidir ve optimize edilmiş ve edilmemiş bir dağıtım arasındaki fark harcamada çoğu zaman birkaç katıdır. YG, daha yüksek hızlandırıcı kullanım oranından, gruplama ve önbellekleme yoluyla daha düşük istek başına maliyetten, uygun boyutlu modellerden ve gereğinden fazla kaynak ayırmaktan kaçınmaktan gelir. Gözlemlenebilirlik ve değerlendirme işlem hatları, maliyetli olayları önleyerek ve güvenli yinelemeyi mümkün kılarak karşılığını verir.

TSM; hızlandırıcı hesaplamayı (birçok iş yükü için en büyük kalem), vektör depolamayı, sunum altyapısını, ağı ve onu çalıştıracak platform ve operasyon personelini kapsar. Bunu yatırım yapmamanın maliyetine karşı tartın: kontrolden çıkan çıkarım faturaları, benimsemeyi baltalayan kötü gecikme ve ölçeklenememe. Kamu için egemenlik ya da güvenlik gereksinimlerini karşılayamamanın maliyetini ekleyin. Gerekçeyi liderliğe, her takımın maliyetli, az kullanılan altyapıyı kendisinin kurması yerine, birçok takımın yapay zekayı verimli devreye almasını sağlayan sonuç başına maliyet eğilimlerini ve asfaltlanmış yollu bir platformu göstererek sunun.

## Anti-kalıplar ve tuzaklar

- **Boştaki hızlandırıcılar.** Kıt GPU'ları, onları az kullanan takımlara ayırmak.
- **Gruplama ya da önbellekleme yok.** Her isteği tek tek sunmak ve paylaşılan bağlamı yeniden hesaplamak.
- **Varsayılan olarak en büyük model.** Küçük bir modelin yeteceği yerde pahalı bir model kullanmak.
- **Maliyet körlüğü.** Fatura gelene kadar atıf, bütçe ya da istek başına maliyet görünürlüğü olmaması.
- **Sürümlenmemiş istemler.** İstemleri üretimde sürümleme ya da değerlendirme kapısı olmadan değiştirmek.
- **Kuyruk gecikmesini ihmal.** Kullanıcılar yavaş kuyruklardan muzdaripken ortalama gecikmeyi optimize etmek.
- **Sessiz kilitlenme.** Taşınabilirlik olmadan tek bir sağlayıcının sunum yığınının üzerine derinlemesine inşa etmek.

## Olgunluk modeli

- **Düzey 1, Başlangıç:** En yüksek sesle isteyene tepki veren gelişigüzel GPU tahsisi, gruplama ya da önbellekleme yok, fatura gelene kadar maliyet görünürlüğü yok, canlıda düzenlenen ve sürümlenmemiş istemler, asgari izleme.
- **Düzey 2, Geliştirme:** Bazı takımlar paylaşılan zamanlamayı, önbelleklemeyi ve sürüm kontrollü istemleri benimser, ama uygulama kurum genelinde tutarsızdır: bir grup gruplayıp değerlendirirken bir başkası hâlâ her isteği tek tek sunar ve istemleri elle değiştirir.
- **Düzey 3, Standartlaştırma:** Belgelenmiş, asfaltlanmış yollu bir platform kuruluş genelinde uygulanır: kotalar ve önceliklerle paylaşılan zamanlama, standart gruplama, önbellekleme ve uygun boyutlandırma, getirme için vektör altyapısı, her istem ya da model değişikliğini kapılayan otomatik değerlendirme işlem hatları ve takımlara ve kullanım durumlarına maliyet atfı.
- **Düzey 4, Yönetme:** Platform temel çizgilere karşı ölçülür ve kontrol edilir: hızlandırıcı kullanım oranı, yararlı sonuç başına maliyet, kuyruk gecikmesi, getirme anımsaması ve değişiklik başına kalite gerilemeleri uyarılar ve eşiklerle izlenir, maliyet her takım tarafından sahiplenilir ve bir değişiklik için git ya da gitme kararı sezgiye değil kanıta dayanır.
- **Düzey 5, Orkestrasyon:** Altyapı sürekli iyileşir ve uyum sağlar: yönlendirme, gruplama ve ölçekleme canlı maliyet ve kalite sinyallerine göre kendini ayarlar, talep ve kısıtlar değiştikçe kapasite takımlar arasında ve bulut, şirket içi ve egemen hedefler arasında yeniden dengelenir, taşınabilirlik prova edilir ve altyapı planlaması ürün, güvenlik ve tedarikle bütünleşir.

## Tartışma fikirleri

- Öncelikli iş yüklerini aç bırakmadan hızlandırıcı kullanım oranını nasıl yükseltirsiniz?
- Gecikme gereksinimleriniz için doğru gruplama ve önbellekleme dengesi nerede?
- Şirket içi ya da egemen dağıtım, buluta karşı maliyetini ne zaman haklı çıkarır?
- Yapay zeka harcamasını birçok takım arasında nasıl atfeder ve denetlersiniz?
- Bir istem ya da model değişikliğinin üretime ulaşmasını ne kapılamalı?
- Sağlayıcı değiştirebilecek kadar sunum altyapısını nasıl taşınabilir tutarsınız?

## Önemli çıkarımlar

- Hızlandırıcılar kıt ve pahalıdır; onları bilinçli zamanlayın, paylaşın ve kullanın.
- Gruplama, önbellekleme ve modelleri uygun boyutlandırma, maliyet ve gecikme için başlıca kollardır.
- Getirme uygulamaları iyi işletilen gömme ve vektör arama altyapısına ihtiyaç duyar.
- LLMOps (istem sürümleme, değerlendirme işlem hatları ve gözlemlenebilirlik), üretken yapay zekanın operasyonel omurgasıdır.
- Maliyeti gözlemlenebilir biçimde yönetin ve kilitlenmeden kaçınmak için taşınabilirliği koruyun.

## Kaynaklar ve ileri okuma

- Chip Huyen, *Designing Machine Learning Systems*.
- Google, *Site Reliability Engineering* (Beyer, Jones, Petoff, Murphy, editors).
- Jared Kaplan et al., *Scaling Laws for Neural Language Models*.
- Reza Yazdani Aminabadi et al., *DeepSpeed Inference: Enabling Efficient Inference of Transformer Models at Unprecedented Scale*.
- Woosuk Kwon et al., *Efficient Memory Management for Large Language Model Serving with PagedAttention* (vLLM).
- Andriy Burkov, *Machine Learning Engineering*.
