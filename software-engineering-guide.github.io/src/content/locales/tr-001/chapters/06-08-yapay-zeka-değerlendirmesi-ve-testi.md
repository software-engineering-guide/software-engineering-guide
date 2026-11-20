# 6.8 Yapay zeka değerlendirmesi ve testi

## Genel bakış ve motivasyon

Sıradan yazılımı test etmek rahatlatıcı bir varsayıma dayanır: aynı girdi verildiğinde program aynı çıktıyı döndürür ve bu çıktının ne olması gerektiğini tam olarak doğrulayabilirsiniz. Yapay zeka bu varsayımı bozar. Bir model aynı soruya iki farklı biçimde cevap verebilir ve ikisi de kabul edilebilir olabilir. Geçti ya da kaldı yerine yanlıştan harikaya uzanan bir ölçekte notlanabilir. Üstelik karşısında doğrulama yapacağınız tek bir doğru cevap çoğu zaman yoktur. Bu yüzden değerlendirme disiplini, yani tek bir çıktıyı tek bir beklenen değerle karşılaştırmak yerine bir modelin birçok temsilî durumda ne kadar iyi davrandığını ölçmek, güvenilir her yapay zeka sisteminin omurgası olur. Takımlar kendilerini utandıran yapay zeka özellikleri yayımladığında kök neden hemen her zaman, yayından önce kaliteyi ölçmenin ciddi bir yolunun olmamasıdır.

Büyük takımlar için değerlendirme, değişikliği güvenli kılan şeydir. Modelleri değiştireceksiniz, istemleri yeniden yazacaksınız, erişimi ayarlayacaksınız ve araçlar ekleyeceksiniz; bu değişikliklerin her biri sağlam sandığınız davranışları sessizce bozabilir. Kaliteyi ölçmenin tekrarlanabilir bir yolu olmadan her değişiklik bir kumardır ve her gerileme bir kullanıcı tarafından keşfedilir. Bu bölüm, inşa bölümlerinin ölçüm tarafındaki eşlikçisidir: üretken yapay zeka ve LLM uygulamaları (bölüm 6.3), yapay zeka ajanları ve ajan tabanlı sistemler (bölüm 6.7) ve makine öğrenmesi mühendisliği ve MLOps (bölüm 6.2). Genel test stratejinizi (bölüm 2.4) olasılıksal dünyaya taşır.

Kurumsal ve kamu ortamları bahsi daha da yükseltir. Onlarca yapay zeka özelliği çalıştıran bir kuruluşun, her takımın notlandırmayı sıfırdan icat etmemesi için ortak bir değerlendirme platformuna ihtiyacı vardır. Bir kamu kurumunun belgelenmiş ve denetlenebilir bir değerlendirmeye ihtiyacı vardır, çünkü "test ettik" sözü "işte kanıt, veri kümesi, metrik ve onay" haline gelmelidir. Değerlendirme, sorumlu ve güvenilir yapay zekanın (bölüm 6.5) bir değer beyanı olmaktan çıkıp bir düzenleyiciye gösterebileceğiniz bir şeye dönüştüğü yerdir.

## Temel ilkeler

- Değerlendirmeyi, lansmandan önce eklenen bir son düşünce olarak değil, birinci sınıf bir ürün olarak ele alın.
- Modele pohpohlayan oyuncak örnekler yerine gerçek kullanımı yansıtan temsilî verilerle ölçün.
- Hızlı yineleme için çevrimdışı değerlendirmeyi, gerçek referans için çevrimiçi değerlendirmeyi birleştirin.
- İnsan yargısını çapanız yapın ve her otomatik notlayıcıyı ona göre kalibre edin.
- Değerlendirme kümelerinizi kirlenmeden koruyun, yoksa sayılarınız size yalan söyler.
- Değerlendirmeleri sürekli entegrasyona kapı olarak bağlayın; böylece kalite sessizce gerileyemez.
- Üretimde ölçmeye devam edin, çünkü kodunuz değişmese bile kalite kayar.

## Öneriler

### Değerlendirme güdümlü geliştirmeyi benimseyin

Bir istemi ayarlamadan ya da bir model seçmeden önce değerlendirmeyi yazın. Bu, test güdümlü geliştirmeyi yansıtır: "iyi"nin ne demek olduğunu ölçülebilir terimlerle tanımlar, sonra ona doğru inşa edersiniz. Burada değerlendirme, girdilerden oluşan bir veri kümesi ile her çıktı için bir sayı ya da not döndüren bir puanlama yönteminin birleşimi demektir. Küçük başlayın. Gerçek kullanıcı niyetini yansıtan yirmi özenle seçilmiş durum, rastgele bin durumdan iyidir. Sistemin nerede başarısız olduğunu öğrendikçe kümeyi büyütün, her üretim başarısızlığını kalıcı bir durum olarak geri ekleyin; böylece aynı hata fark edilmeden geri dönemez.

Değerlendirme güdümlü geliştirme takım davranışını değiştirir. İyinin tanımı yazılı ve çalıştırılabilir olduğunda, bir değişikliğin işe yarayıp yaramadığı tartışması bir zevk meselesi olmaktan çıkıp denetlenebilir hale gelir. Değerlendirme kümesini, ölçtüğü istemlerin ve kodun hemen yanında, sürüm kontrolünde gözden geçirilen bir yapıt yapın.

### Çevrimdışı ve çevrimiçi değerlendirmeyi ayırın ve ikisini de kullanın

Çevrimdışı değerlendirme, sabit bir veri kümesini kontrollü bir ortamda sisteminizden geçirir; hızlı, ucuz ve tekrarlanabilirdir, böylece hiçbir şey yayımlanmadan önce sürümleri karşılaştırabilirsiniz. Çevrimiçi değerlendirme ise canlı sistemi gerçek kullanıcılarla ölçer: görev tamamlama, yükseltme oranı, beğen ve beğenme geri bildirimleri ve sonraki iş sonuçları gibi metriklerle. Çevrimdışı, bir değişikliğin güvenli olma ihtimalini söyler; çevrimiçi, gerçekten işe yarayıp yaramadığını söyler. İkisine de ihtiyacınız var, çünkü çevrimdışı kümeler gerçekliği hiçbir zaman tam yakalamaz ve çevrimiçi sinyaller tek korkuluğunuz olamayacak kadar geç gelir.

İkisini bir döngüye bağlayın. Çevrimiçi metrikler düştüğünde ya da bir kullanıcı kötü bir cevabı işaretlediğinde o durumu yakalayın, etiketleyin ve çevrimdışı kümeye katın. Deneyleri, herhangi bir ürün değişikliği için kullandığınız aynı kontrollü karşılaştırmadan geçirin; bu, ürün analitiği ve deneylerin (bölüm 7.4) alanıdır. Yeni bir modelin görev başarısını artırdığını gösteren bir A/B testi, herhangi bir çevrimdışı puandan daha değerlidir; ama testi çalıştırmaya cesaret etmenizi sağlayan, çevrimdışı puandır.

### Temsilî değerlendirme kümeleri kurun ve kirlenmeye karşı korunun

Değerlendirmeniz yalnızca verisi kadar dürüsttür. Altın veri kümeleri kurun: kullanıcıların gerçekte sorduklarının dağılımını yansıtan, doğrulanmış beklenen çıktılar ya da puanlama rubrikleriyle girdilerden oluşan özenle seçilmiş koleksiyonlar. Yaygın durumları, nadir ama kritik durumları, saldırgan durumları ve sisteminizin şu anda yanlış yaptığı durumları kapsasın. Kaliteyi vasat bir ortalamanın içine saklanan başarısız bir kategori olarak değil, segment başına okuyabilmek için bunları katmanlayın. Beklenen cevapları alan uzmanlarına doğrulatın, çünkü yanlış cevaplar üzerine kurulmuş bir altın küme hiç olmamasından kötüdür.

Sonra bu veriyi kirlenmeden koruyun. Test kümesi kirlenmesi, değerlendirme örneklerinizin bir modelin eğitim verisine ya da istemin kendisine sızmasıyla olur; model cevapları fiilen görmüş olduğu için iyi performans gösteriyor gibi görünür. Bir modelin genel bir kıyaslamada parlak puan alıp sizin gerçek trafiğinizde tökezlemesinin nedeni budur. Değerlendirme verinizin bir kısmını özel tutun ve güvenmediğiniz bir üçüncü tarafa asla göndermeyin. Kümeleri zamanla yenileyin. Geliştiricilerin istemleri puan anlamsızlaşana dek değerlendirme kümesine karşı elle ayarladığı daha ince sızıntıya dikkat edin; bu gerçek bir iyileşme değil, teste aşırı uyumdur. Yalnızca ara sıra baktığınız taze bir bekletilmiş küme ayırın.

### Göreve uyan metrikler seçin

Ölçümünüzü çıktının biçimine uydurun. Doğru bir etiketin bulunduğu sınıflandırma ve çıkarım için klasik metrikler geçerlidir: [kesinlik ve duyarlılık](https://en.wikipedia.org/wiki/Precision_and_recall) (işaretlediğiniz öğelerin kaçı doğruydu ve doğru öğelerin kaçını buldunuz), ikisini dengeleyen [F-skoru](https://en.wikipedia.org/wiki/F-score) ve tam eşleşme doğruluğu. Güvenli bir olasılığın önemli olduğu her durumda [kalibrasyonu](https://en.wikipedia.org/wiki/Calibration_(statistics)) ölçün; yani belirtilen yüzde 80 güvenin zamanın yaklaşık yüzde 80'inde doğru olup olmadığını. Çünkü ne zaman emin olmadığını bilen iyi kalibre edilmiş bir model, aşırı özgüvenli olandan çok daha güvenlidir.

Üretken çıktılar daha zordur. Aslen makine çevirisi ve özetleme için geliştirilen [BLEU](https://en.wikipedia.org/wiki/BLEU) ve ROUGE gibi referans tabanlı metrikler, üretilen metni referans metinle örtüşen sözcükleri ve ifadeleri sayarak karşılaştırır. Ucuz ve tekrarlanabilirdirler, ama kalite için zayıf vekillerdir: yüzey örtüşmesini ödüllendirir, referanstan farklı ifade edilmiş doğru bir cevabı cezalandırırlar. Onları kaba gerileme sinyalleri olarak kullanın, iyinin tanımınız olarak değil. Açık uçlu görevlerde rubrik tabanlı puanlama daha iyi çalışır: açık ölçütleri (dayanaklı mı, eksiksiz mi, güvenli mi, doğru biçimlendirilmiş mi) tanımlayın ve her birini puanlayın. Rubrikler öznel kaliteyi okunur ve gözden geçirilebilir kılar.

### LLM-hakem kullanın, ama insanlara göre kalibre edin

Üretken çıktıyı elle notlandırmak ölçeklenmez; bu yüzden takımlar giderek daha fazla güçlü bir [büyük dil modelini](https://en.wikipedia.org/wiki/Large_language_model) otomatik hakem olarak kullanıyor: ona girdiyi, çıktıyı ve bir rubriği verip puanlamasını istiyor. Bu LLM-hakem yaklaşımı hızlıdır ve şaşırtıcı biçimde yetkindir, ama yönetmeniz gereken gerçek yanlılıklar taşır. Hakemler daha uzun cevapları tercih etme, ikili karşılaştırmada ilk gösterilen seçeneği kayırma (konum yanlılığı), kendi yazım üslubunu ödüllendirme eğilimindedir ve akıcı ama yanlış bir akıl yürütmeden etkilenebilir. Denetlenmezse yanlı bir hakem size kendinden emin, kesin ve yanlış sayılar verir.

Hakemi insan etiketlerine göre kalibre edin. İnsanlara bir örneklemi notlandırtın, sonra model hakemin onlarla ne kadar uyuştuğuna bakın ve uyum güvenmeye yetecek kadar yüksek olana dek hakem istemini ayarlamayı sürdürün. Bilinen yanlılıkları bilinçli olarak azaltın: seçeneklerin sırasını rastgeleleştirin, uzunluğu kontrol edin ve çıplak bir sayı yerine gerekçeli, rubriğe çapalı bir puan isteyin. Hakemi sabit bir kehanet olarak değil, periyodik yeniden kalibrasyon gerektiren bir ölçüm aleti olarak görün. Hakemi kurarken eldeki en yetenekli modeli varsayılan alın, çünkü zayıf bir hakem zayıf bir cetveldir.

### Gerçek referans için insanları döngüde tutun

İnsan değerlendirmesi, her otomatik metriğin ölçüldüğü çapa olmaya devam eder; bu yüzden onu iyi yapmaya yatırım yapın. Açık not alma yönergeleri yazın, not vericilerinizi eğitin ve değerlendiriciler arası uyumu ölçün: bağımsız gözden geçirenlerin aynı duruma aynı notu verme derecesi. Düşük uyum genellikle rubriğinizin belirsiz olduğu anlamına gelir, gözden geçirenlerin özensiz olduğu değil; bu yüzden rubriği düzeltin. Yüksek riskli alanlarda, hukuki ya da tıbbi bir cevabı yargılayacak bağlamdan yoksun kitle çalışanları yerine nitelikli uzmanlar kullanın.

### Güvenlik ve saldırgan dayanıklılık için kırmızı takım çalışması yapın

Standart değerlendirme kümeleri, sistemin makul girdilerde doğru şeyi yapıp yapmadığını ölçer. [Kırmızı takım çalışması](https://en.wikipedia.org/wiki/Red_team), yani kendi sisteminize kasıtlı olarak saldırıp nerede yanlış davrandığını bulmak, baskı altında ne olduğunu ölçer. İstem enjeksiyonunu, jailbreak'leri, güvenli olmayan içeriği, gizlilik sızıntılarını ve yanlı çıktıları yoklayın. Bunu tek seferlik bir alıştırma değil, tekrarlanabilir bir paket yapın: her başarılı saldırıyı kalıcı bir gerileme durumuna çevirin ki düzeltilmiş bir açık düzeltilmiş kalsın. Bu çalışma doğrudan sorumlu ve güvenilir yapay zekaya (bölüm 6.5) bağlanır ve düzenlemeye tabi ortamlarda çoğu zaman bir güvenlik incelemesini tatmin eden kanıttır.

### Ajanları uçtan uca görev başarısıyla değerlendirin

Birçok adım boyunca plan yapan ve eylemde bulunan ajanlar tek tek çıktılarla yargılanamaz. Önemli olan görevin tamamının başarılı olup olmadığıdır: ajan toplantıyı ayarladı mı, talebi çözdü mü ya da iş akışını doğru ve güvenli biçimde tamamladı mı. Ajanın gerçekçi ama güvenli test verilerine karşı eylemde bulunabileceği yalıtılmış bir ortamda görev düzeyinde değerlendirmeler kurun ve nihai sonuçları artı yörüngeyi, yani oraya varmak için izlediği adımlar ve araç çağrıları dizisini puanlayın. Tehlikeli ya da savurgan bir yoldan varılan doğru bir cevap yine de bir sorundur. Bu, tek bir yanlış eylemin gerçek sonuçlar doğurabileceği yapay zeka ajanları ve ajan tabanlı sistemler (bölüm 6.7) için hayatîdir.

### Değerlendirmeleri CI'a bağlayın ve üretimi izleyin

Değerlendirmeyi otomatik yapın. Çevrimdışı paketinizi her istem, model ya da erişim değişikliğinde [sürekli entegrasyonda](https://en.wikipedia.org/wiki/Continuous_integration) (CI) çalıştırın ve birleştirmeleri tıpkı birim testlerinde olduğu gibi buna bağlayın; bu uygulama daha geniş test stratejinizde (bölüm 2.4) kök salmıştır. Puanlar gürültülü olduğu için kusursuz bir koşu talep etmek yerine eşiklere ve eğilimlere göre kapı koyun; kilit bir metrik tabanının altına düştüğünde ya da belirlenen payı aşan biçimde gerilediğinde derlemeyi başarısız kılın. Sonra üretimde izlemeyi sürdürün: çevrimdışı testlerin kaçırdığı yavaş bozulmayı yakalamak için kalite sinyallerini, çıktı dağılımlarını ve girdi kaymasını izleyin; bu, makine öğrenmesi mühendisliğinin ve MLOps'un (bölüm 6.2) gözlemlenebilirlik uygulamalarına bağlanır. Lansmanda doğru olan bir model, tanımladığı dünya altında değiştikçe çürüyebilir.

## Ödünleşimler: artılar ve eksiler

| Değerlendirme yaklaşımı | Artılar | Eksiler | En uygun olduğu durum |
|---|---|---|---|
| İnsan değerlendirmesi | En yüksek doğruluk, nüansı yakalar | Yavaş, pahalı, ölçeklemesi zor | Gerçek referans, yüksek riskli işler, hakemleri kalibre etme |
| LLM-hakem | Hızlı, ucuz, büyük kümelere ölçeklenir | Yanlı, kalibrasyon gerektirir | Üretken çıktıda sık çevrimdışı koşular |
| Referans tabanlı metrikler (BLEU, ROUGE) | Ucuz, belirlenimci, tekrarlanabilir | Gerçek kalite için zayıf vekil | Kaba gerileme sinyalleri, nihai hüküm değil |
| Klasik metrikler (kesinlik, duyarlılık, F-skoru) | Nesnel, iyi anlaşılmış | Yalnızca doğru etiketli görevlere uyar | Sınıflandırma, çıkarım, erişim |
| Genel kıyaslamalar | Modeller arası karşılaştırılabilir, kurulum gerektirmez | Kirlenme, görevinize zayıf uyum | Erken model kısa listesi, yayın kapısı değil |
| Çevrimiçi değerlendirme (A/B, geri bildirim) | Gerçek kullanıcıları ve sonuçları yansıtır | Yavaş, maruz kalındıktan sonra gelir | Bir değişikliğin gerçekten işe yaradığını doğrulama |

Merkezî gerilim hız ile doğruluk arasındadır. İnsan değerlendirmesi en güvenilir ve en az ölçeklenebilir olandır; otomatik notlandırma bunun tersidir. Çözüm bunları katmanlamaktır: sürekli yineleme için hızlı, ucuz yöntemler kullanın, bu yöntemleri düzenli kalibrasyonla insan yargısına çapalayın ve tam insan incelemesini en yüksek riskli kararlara ve ucuz metriklerinizin hâlâ gerçeği izleyip izlemediğini kontrole saklayın. İkinci gerilim, çevrimdışı kolaylık ile çevrimiçi gerçek arasındadır. Çevrimdışı kümeler hızlı hareket etmenizi sağlar ama üretimi hiçbir zaman tam yansıtmaz; bu yüzden güçlü bir çevrimdışı puanı, işinizin bittiğinin kanıtı değil, özenli bir çevrimiçi test çalıştırma izni olarak görün.

## Takımınızla tartışılacak sorular

1. **"Yeterince iyi" çıtamız nedir ve onu tanımlayan değerlendirme kümesinin sahibi kim?** Her yapay zeka özelliğinin örtük bir kalite eşiği vardır ve örtük kaldığında her mühendis kendi eşiğini hisle belirler, anlaşmazlıkları da odadaki en kıdemli kişi çözer. Çıtayı, segment başına hedef puanları olan çalıştırılabilir bir değerlendirme kümesi olarak yazmak bu anlaşmazlıkları ölçülebilir sorulara çevirir. Başarı için mevcut tanımınızı, arkasındaki veriyi ve onu gerçekte kimin sürdürdüğüne dair dürüst bir anlatımı getirin; çünkü sahipsiz bir değerlendirme kümesi, bakımsız her kod kadar hızlı çürür. Çıtanın risk katmanına göre değişip değişmediğine karar verin: halka dönük bir hukuki cevap, dahili bir beyin fırtınası yardımcısından daha yüksek bir çıtayı geçmelidir. Cevap, şu anda herhangi birinin kendisiyle kullanıcılar arasında hiçbir ölçüm durmadan bir yapay zeka değişikliği yayımlayıp yayımlayamadığını söylemelidir.

2. **Değerlendirme sayılarımızın kirlenmiş ya da aşırı uyumlu değil, dürüst olduğunu nasıl biliriz?** Bir puan yalnızca gerçek dünya kalitesini öngördüğü sürece yararlıdır ve bunu yapmayı bırakmasının birçok yolu vardır: kıyaslama verisinin eğitime sızması, geliştiricilerin istemleri sayı anlamsızlaşana dek test kümesine karşı ayarlaması ya da hiç doğrulanmamış cevaplar üzerine kurulmuş bir altın veri kümesi. Değerlendirme verinizin nereden geldiğine, ne kadarının özel tutulduğuna ve ne sıklıkla yenilendiğine dair kanıt getirin. Nadiren baktığınız taze bir bekletilmiş kümeniz olup olmadığını tartışın; böylece en azından kimsenin kendisine göre optimize etmediği bir sayınız olur. Puanlarınızın modelin hiç etkilemediği verilerde neden geçerli kalacağını açıklayamıyorsanız, kendi yansımanızı ölçüyorsunuz demektir.

3. **İnsanlar döngüde nerede kalıyor ve otomatik hakemlerimizi onlara göre nasıl kalibre tutuyoruz?** LLM-hakem ve referans metrikler büyük ölçekte notlandırmanıza izin verir ve kontrol etmedikçe görünmez biçimlerde insan yargısından kayarlar. Otomatik notlandırma ile insan incelemesi arasındaki mevcut uyum oranınızı, bunu en son ne zaman ölçtüğünüzü ve hangi yanlılıkları (uzunluk, konum, üslup) test ettiğinizi getirin. Maliyetten bağımsız olarak hangi kararların bir insan notlandırıcı gerektirdiğine karar verin; genellikle en yüksek riskli olanlar ve otomatik hakemi yeniden kalibre etmek için kullanılanlar. Not alma kalitesini de konuşun, çünkü tutarsız insan etiketlerine göre kalibre edilmiş bir hakem bu tutarsızlığı miras alır. Cevap, tek seferlik bir onay değil, bir yeniden kalibrasyon takvimi üretmelidir.

4. **Bugün hangi yapay zeka değişiklikleri değerlendirmeye kapılı ve hangileri hâlâ yalnızca birinin özgüveniyle kullanıcılara ulaşıyor?** Bazı değişikliklerde çalışıp diğerlerinde çalışmayan bir kapı size güvenlik yanılsaması verir, gerçek gerilemelerin kapısız yoldan geçmesine izin verir: sessiz bir istem ince ayarı, bir erişim ayarlaması, kimsenin değişiklik saymadığı bir model sürüm artışı. Büyük bir takımda tehlike, bir isteme dokunabilen insan sayısıyla büyür, çünkü her kapısız yol, hiçbir veri kümesinin görmediği bir gerilemeyi yayımlamanın bir yoludur. Sürekli entegrasyonda çevrimdışı paketi tetikleyen değişiklik türlerinin listesini, tetiklemeyenleri ve kapısız bir değişikliğe izlenen son birkaç olayı getirin. Kapının hangi eşiği ve eğilimi uyguladığına karar verin; çünkü gürültülü bir puan, kusursuz bir koşu talebi değil, bir taban ve bir gerileme payı gerektirir. Kurumsal ve kamu ortamlarında kapıyı yayın kaydının kendisine bağlayın; böylece bir değişikliğin ölçüldüğüne dair kanıt, birinin bir kez aldığı bir ekran görüntüsü değil, denetim izinin parçası olur.

5. **Değerlendirmeye ne kadar harcıyoruz ve bu harcama her özelliğin riskiyle eşleşiyor mu?** Değerlendirme bedava değildir: not alma emeği, otomatik hakemlerin her koşuda yaktığı hesaplama ve altın veri kümelerini temsilî tutmanın süregelen işi gerçek para harcar; bu maliyetleri hiç adlandırmayan bir takım ya yüksek riskli bir özelliğe yetersiz yatırım yapar ya da harcanabilir bir özelliği altınla kaplar. Karşıt çekim doğruluk ile bütçe arasındadır, çünkü en güvenilir yöntem olan uzman insan incelemesi aynı zamanda en az ölçeklenebilir olandır; bu yüzden her yerde karşılayamazsınız ve karşılığını nerede aldığına karar vermelisiniz. Odanın paranın nereye gittiğini tehlikenin nerede yaşadığıyla karşılaştırabilmesi için değerlendirme koşusu başına mevcut maliyeti, özellik başına not alma saatlerini ve her sistem için dürüst bir risk katmanını getirin. Bir kurumsal yapı için bu, not almayı ve hesaplamayı birçok takıma yayan ortak bir değerlendirme platformunun en güçlü argümanıdır; bir kamu kurumu için risk katmanı, bir denetim organının sonradan talep edeceği kanıt derinliğine doğrudan karşılık gelmelidir.

6. **Daha iyi bir model geldiğinde yardımcı olup olmadığını ne kadar hızlı kanıtlayabiliriz ve geçişi yapmasına kim izinli?** Bir değerlendirme paketinin değeri en keskin biçimde daha güçlü bir modelin çıktığı gün gerçekleşir; çünkü altın veri kümelerini ve kırmızı takım paketini yeni modele karşı bir öğleden sonra içinde çalıştırabilen bir takım, elle notlandıran bir takımın aylarca kaçıracağı iyileştirmeleri benimseyebilir. Gerilim hız ile ihtiyat arasındadır: daha iyi bir model göründüğü gün harekete geçmek istersiniz ve bir geçişin, ortalama puanınızın gizlediği bir cevap kategorisini sessizce bozmasına izin veremezsiniz. Yeni bir sağlayıcıya karşı tam bir çevrimdışı karşılaştırma çalıştırmanın şu anda ne kadar sürdüğünü, değerlendirme kümelerinizin modeller arasında taşınabilir olup olmadığını ve bir gerilemenin en çok önem taşıyacağı segmentleri getirin. Düzenlemeye tabi ve kamusal ortamlarda bir model değişikliğini onaylama yetkisinin kimde olduğunu ve hangi belgelenmiş kanıtı talep ettiklerini adlandırın; çünkü vatandaşa dönük bir kararın arkasındaki modelin belgesiz değiştirilmesi, bir denetçinin sizden gerekçelendirmenizi isteyeceği türden bir değişikliktir.

## Sektör merceği

**Girişim.** Yapabileceğiniz en küçük dürüst değerlendirmeyi kurun ve ürünle birlikte büyümesine izin verin. Her biri doğrulanmış beklenen cevaba sahip yirmi ila kırk gerçek durumdan oluşan bir elektronik tablo, her birleştirmeden önce bir betikle çalıştırıldığında, nişiniz için herhangi bir genel kıyaslamadan iyidir ve neredeyse hiçbir şeye mal olmaz. Elle notlandırma gerçekten acıtana kadar ortak platformu ve LLM-hakemi atlayın; ama kullanıcının bildirdiği her başarısızlığı ilk günden kümeye geri ekleyin, çünkü aynı utancı iki kez yaşamanızı önleyen refleks budur.

**Küçük işletme.** Muhtemelen değerlendirme uzmanınız yok ve yapay zekanızı araçlara gömülü olarak satın alıyorsunuz; yani işiniz kanıt kurmak değil, kanıt talep etmek. Her satıcıya kaliteyi nasıl ölçtüklerini, sizinkine benzeyen veriler üzerinde test edip etmediklerini ve seçmediğiniz bir güncellemeden sonra bir gerilemeyi nasıl fark edeceğinizi sorun. Aracı kendiniz kontrol etmek için kendi gerçek durumlarınızdan oluşan küçük bir özel küme tutun; çünkü bir müşteriye ulaşan yanlış otomatik cevap size bu kontrolün dakikalarından çok daha pahalıya mal olur.

**Kurumsal.** Ödül, bir düzine takımın her birinin notlandırmayı yeniden icat etmemesi için ortak bir değerlendirme platformudur: altın veri kümeleri için ortak bir depo, sürekli entegrasyonda kapılanmış çevrimdışı paketler, kalibrasyon puanlarıyla kaydedilmiş LLM-hakem istemleri ve özellik başına çevrimiçi metrikler. Üzerine, gereken çıtayı ve yayından önceki onayı belirleyen risk katmanlarıyla yönetişim ekleyin; böylece yüksek riskli bir özellik dahili bir yardımcıdan daha yüksek bir kapıyı geçer. Platform, not almayı ve hesaplamayı takımlara yayar; bu, her grubun doğaçlama yapmasına izin vermek yerine bir tane kurmanın en güçlü nedenidir.

**Kamu.** Değerlendirme yalnızca yapılmış değil, denetlenebilir olmalıdır; bu yüzden her yayın için hesap verebilirlik kanıtı olarak veri kümesi sürümünü, metrikleri, gözden geçirenin adını ve onayı arşivleyin. Bir kırmızı takım paketi, sistemin kaynaklarında bulunmayan politikayı ya da eyalet yasasını uydurmayı reddettiğini kanıtlamalı ve tedarik, satıcılardan modeli nasıl değerlendirdiklerini açıklamalarını ve değerlendirme verinizin taşınabilirliğini sağlamalarını şart koşmalıdır. Bir denetim organı aracın güvenli olduğunu nasıl bildiğinizi sorduğunda cevap bir güvence değil, tarihli bir kayıt olmalıdır.

## Örnekler

**Girişim.** Yapay zeka sözleşme inceleme asistanı geliştiren dört kişilik bir şirket, şirket içi avukatlarının her birine işaretlenmesi gereken riski etiketlediği kırk gerçek maddelik bir elektronik tabloyla başladı. Her istem değişikliği birleştirmeden önce bir betikle bu kümeye karşı çalıştırıldı ve puan çekme isteğinde yazdırıldı. Kullanıcılar kaçırılmış bir maddeyi işaretlediğinde, doğrudan tabloya girdi; böylece küme ürünle birlikte büyüdü. Hacim arttıkça açıklama kalitesini notlandırmak için bir LLM-hakem eklediler, ama yalnızca bir örneklemde avukatla uyuştuğunu kontrol ettikten sonra. Ucuz, özel ve dürüst olan, nişleri için herhangi bir genel kıyaslamayı yendi.

**Kurumsal.** Büyük bir banka destek, arama ve dahili araçlar genelinde bir düzine yapay zeka özelliği çalıştırıyordu ve her takım farklı notlandırıyordu. Ortak bir değerlendirme platformu kurdular: altın veri kümelerini saklamak, çevrimdışı paketleri CI'da çalıştırmak, LLM-hakem istemlerini kalibrasyon puanlarıyla kaydetmek ve özellik başına çevrimiçi metrikleri izlemek için ortak bir yer. Yönetişim üstte duruyordu: gereken çıtayı ve yayından önce gereken onayı belirleyen risk katmanlarıyla. Yeni bir dolandırıcılık açıklama özelliği, değerlendirme kümesi gözden geçirilmeden, kırmızı takım paketi geçmeden ve hesap verebilir sahibi sonuçları imzalamadan yayımlanamadı. Platformu yeniden kullanmak, takımların ölçümün nasıl yapılacağını değil, kendi alanlarını tartışması anlamına geldi.

**Kamu.** Bir halk sağlığı kurumu, personelin onaylı rehberlikten yardım sorularını yanıtlamasına yardımcı olan bir asistan devreye aldı. Yanlış bir cevap birinin hak edişini etkileyebileceğinden değerlendirme denetlenebilir olmak zorundaydı. Her yayın; yaygın soruları, uç durumları ve saldırgan istemleri kapsayan belgelenmiş bir değerlendirme kümesiyle çalıştırıldı ve sonuçlar, veri kümesi sürümü, metrikler ve gözden geçirenin adı hesap verebilirlik kanıtı olarak arşivlendi. Bir kırmızı takım paketi, sistemin kaynaklarında bulunmayan politikayı ya da eyalet yasasını uydurmayı reddettiğini kontrol etti. Bir denetim organı kurumun aracın güvenli olduğunu nasıl bildiğini sorduğunda, cevap bir güvence değil, tarihli bir kayıttı.

## İş gerekçesi: motivasyonlar, YG ve TSM

Değerlendirme, diğer her yapay zeka yatırımını daha güvenli ve daha hızlı kılarak kendini amorti eder. Yatırım getirisi (YG), daha az üretim olayı, takımların istemleri ve modelleri güvenle değiştirebilmesi sayesinde daha hızlı yineleme ve daha iyi modellerin yardımcı olup olmadığını kanıtlayabildiğiniz için geldikleri gün benimseyebilme olarak görünür. Değerini ölçmenin en net yolu yokluğunun maliyetidir: tek bir halka açık halüsinasyon, yanlı çıktı ya da veri sızıntısı, düzeltme, kaybedilen güven ve düzenleyici maruziyet olarak yıllarca süren değerlendirme altyapısından çok daha pahalıya mal olabilir. Bu, bir gerilemeyi CI'da bedavaya bulmak ile gazetede bulmak arasındaki farktır.

Toplam sahip olma maliyeti (TSM) gerçektir ve adlandırmaya değer. Not alma emeği, otomatik hakemlerin tükettiği hesaplama ve kullanım değiştikçe değerlendirme kümelerini temsilî tutmanın süregelen işi için ödersiniz. Kurumsal ölçekte ortak bir platform bunun çoğunu birçok takıma yayar; bu, her grubun doğaçlama yapmasına izin vermek yerine bir tane kurmanın en güçlü argümanıdır. Liderliğe gerekçeyi somut bir riski (alanınızda tek bir kötü halka açık cevabın maliyeti) somut bir yetenekle (her yeni modeli güvenle benimseme hızı) eşleştirerek ve değerlendirmeyi, kuruluşun pervasızca hareket etmeden hızlı hareket etmesini sağlayan kontrol olarak çerçeveleyerek kurun.

## Anti-kalıplar ve tuzaklar

- **Hislere göre yayımlama.** Yapay zeka değişikliklerini, veri kümesi ve tekrarlanabilir puan olmadan, elle birkaç istem deneyerek yargılamak.
- **Kıyaslama tiyatrosu.** Güçlü bir genel kıyaslama puanını, kirlenmeyi ve dağılım uyumsuzluğunu görmezden gelerek, sistemin görevinize uyduğunun kanıtı saymak.
- **Değerlendirme kümesine aşırı uyum.** İstemleri aynı sabit kümeye karşı, sayı yüksek ve anlamsız olana dek, taze bir bekletilmiş küme olmadan ayarlamak.
- **Kalibre edilmemiş hakemler.** Bir LLM-hakem devreye alıp insan not vericilerle uyumunu hiç kontrol etmeden puanlarına güvenmek.
- **Metrik tapınması.** BLEU ya da ROUGE'u kaliteymiş gibi optimize etmek ve referans metinle örtüşen daha kötü cevaplar yayımlamak.
- **Tek seferlik kırmızı takım çalışması.** Sisteme lansmandan önce bir kez saldırıp bulguları kalıcı gerileme testlerine hiç çevirmemek.
- **Yalnızca çevrimdışı özgüven.** İyi bir çevrimdışı puanın özelliğin çalıştığı anlamına geldiğine inanmak, gerçek sonuçların çevrimiçi ölçümü olmadan.
- **Yetim değerlendirme kümeleri.** Kimsenin sahip olmadığı, üretim başarısızlıklarını hiç özümsemeyen ve yavaş yavaş gerçekliği yansıtmayı bırakan veri kümeleri.

## Olgunluk modeli

- **Düzey 1, Başlangıç:** Yapay zeka değişiklikleri birkaç örnek üzerinde elle, tepkisel olarak, biri endişelendiğinde yargılanır. Veri kümesi, tekrarlanabilir puan ve kapı yoktur. Gerilemeleri kullanıcılar bulur ve kimse sistemin geçen aydan daha iyi mi daha kötü mü olduğunu söyleyemez.
- **Düzey 2, Geliştirme:** Bazı takımlar küçük altın veri kümeleri tutar ve bunları büyük değişikliklerden önce elle çalıştırır; birkaç klasik ya da referans tabanlı puan vardır. İnsan incelemesi önemli özellikler için yapılır, ama notlandırma takımlar arasında tutarsızdır, değerlendirme otomatik ya da kapılı değildir ve her grup farklı yapar.
- **Düzey 3, Standartlaştırma:** Çevrimdışı paketler her istem, model ya da erişim değişikliğinde sürekli entegrasyonda çalışır ve birleştirmelere kapı koyar; kuruluş genelinde tek bir belgelenmiş uygulamayı izler. LLM-hakem insan etiketlerine göre kalibre edilir, kırmızı takım çalışması tekrarlanabilir bir pakettir ve veri kümeleri sahiplidir, sürümlüdür ve üretim başarısızlıklarıyla beslenir; kirlenme etkin biçimde korunur.
- **Düzey 4, Yönetme:** Değerlendirme, temel çizgilere karşı veriyle ölçülür ve kontrol edilir. Hakem-insan uyum oranları, kırmızı takım geçme oranları, segment başına puanlar, çevrimiçi görev başarısı ve kayma zaman içinde izlenir ve birleştirmeler tek bir kusursuz koşu yerine eşiklere ve gerileme paylarına göre kapılanır. Not alma maliyeti ve koşu başına hesaplama özellik başına bütçelenir, yeniden kalibrasyon bir takvime göre yapılır ve her sonuç hesap verebilir bir sahip ve onay taşır.
- **Düzey 5, Orkestrasyon:** Ortak bir değerlendirme platformu tüm kuruluşa hizmet eder ve çevrimdışı ile çevrimiçi değerlendirme iş sonuçlarına bağlı sürekli bir döngü oluşturur. Yeni modeller geldikleri gün taşınabilir değerlendirme kümelerine karşı kanıtlanır, portföy kullanım ve risk değiştikçe uyum sağlar, değerlendirme kanıtı düzenleyiciler ve denetim için denetlenebilirdir ve bir takımın başarısızlıklarından çıkan dersler her takımın veri kümelerine akar.

## Tartışma fikirleri

1. Bir çevrimdışı puanın bir çevrimiçi deneyi haklı çıkaracak kadar güçlü olduğuna ne zaman karar verirsiniz, ne zaman vermezsiniz?
2. Risk profiliniz için insan değerlendirmesinin otomatik notlandırmaya doğru oranı nedir ve bunu ne sıklıkla yeniden gözden geçirmelisiniz?
3. Bir genel kıyaslama ile özel değerlendirme kümeniz hangi modelin daha iyi olduğu konusunda aynı fikirde olmadığında hangisine güvenirsiniz ve neden?
4. Kullanıcı davranışı kaydıkça bir değerlendirme kümesini, CI'da çalıştırılamayacak kadar yavaş bir şeye dönüşmesine izin vermeden nasıl temsilî tutarsınız?
5. Alanınız için bir kırmızı takım paketinde ne olmalı ve saldırıları tasarlamaya kim nitelikli?
6. Her adımı notlandırmanın maliyetinde boğulmadan, bir ajanın yalnızca nihai cevabını değil yörüngesini nasıl değerlendirirsiniz?

## Önemli çıkarımlar

- Yapay zeka değerlendirmesi yazılım testinden farklıdır, çünkü çıktılar belirlenimci değildir ve nadiren tek bir doğru cevap vardır; bu yüzden tam değerleri doğrulamak yerine kaliteyi temsilî durumlar boyunca ölçersiniz.
- Değerlendirme güdümlü geliştirmeyi uygulayın: önce ölçülebilir kaliteyi tanımlayın, sonra ona doğru inşa edin ve her üretim başarısızlığını kümeye geri katın.
- Yöntemleri hız ve doğruluğa göre katmanlayın: sürekli yineleme için ucuz otomatik notlandırma, çapa olarak insan yargısı ve ikisini hizalı tutmak için kalibrasyon.
- Kirlenmeye ve aşırı uyuma karşı korunun, yoksa sayılarınız size pohpohlarken gerçek sistem kullanıcıları hayal kırıklığına uğratır.
- Çevrimdışı değerlendirmeyi CI'da kapı olarak bağlayın ve üretimde kaliteyi ve kaymayı ölçmeye devam edin, çünkü lansmanda iyi olan bir model çürüyebilir.

## Kaynaklar ve ileri okuma

- Chip Huyen, *AI Engineering: Building Applications with Foundation Models*.
- Lianmin Zheng et al., *Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena*.
- Kishore Papineni et al., *BLEU: A Method for Automatic Evaluation of Machine Translation*.
- Chin-Yew Lin, *ROUGE: A Package for Automatic Evaluation of Summaries*.
- Percy Liang et al., *Holistic Evaluation of Language Models (HELM)*.
- Deep Ganguli et al., *Red Teaming Language Models to Reduce Harms: Methods, Scaling Behaviours, and Lessons Learned*.
- OWASP Foundation, *OWASP Top 10 for Large Language Model Applications*.
- National Institute of Standards and Technology, *AI Risk Management Framework*.
