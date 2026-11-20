# 7.8 Veri kalitesi ve gözlemlenebilirlik

## Genel bakış ve motivasyon

[Veri kalitesi](https://en.wikipedia.org/wiki/Data_quality) kullanıma uygunluktur: verinin, ona dayanan kararlara, ürünlere ve raporlara ne ölçüde hizmet ettiği. Bir veri kümesi soyut olarak iyi ya da kötü değildir. Bir amaç için yeterince iyidir ya da değildir. Bir pazarlama sayımı için gayet yeterli olan bir müşteri adresi, bir yasal tebligat için uygunsuz olabilir. Bu çerçeve önemlidir, çünkü sohbeti "verimiz kusursuz mu" (asla) sorusundan "verimiz onunla yapmak üzere olduğumuz iş için uygun mu" (cevaplanabilir ve sınanabilir) sorusuna taşır. Klasik boyutlar doğruluk, bütünlük (eksiksizlik), tutarlılık, güncellik, geçerlilik ve tekillik olarak sıralanır; gerçek sorunların çoğu bunlardan birine indirgenir.

Büyük takımlar için rahatsız edici gerçek şudur: kötü veri, hiç veri olmamasından daha kötüdür. Veriniz olmadığında bunu bilirsiniz ve uygun bir dikkatle ilerlersiniz. Doğru görünen yanlış veriniz olduğunda, ona yanlış bir güvenle dayanarak harekete geçersiniz. Kötü veri sessizce bozar. Bir yöneticinin güvendiği bir panoya, onunla eğitilip hatalarını içine işleyen bir [makine öğrenmesi](https://en.wikipedia.org/wiki/Machine_learning) modeline ve rakam tam ekranda durduğu için kimsenin sorgulamayı düşünmediği kararlara akar. Zarar dağınık ve gecikmelidir, tam da bu yüzden pahalıdır. Biri fark ettiğinde yanlış rakam bir yönetim kurulu sunumunda, bir düzenleyici bildirimde ya da kamuya açık bir istatistikte çoktan alıntılanmıştır.

Veri gözlemlenebilirliği, bunu tüketicileriniz fark etmeden yakalayan disiplindir. Yazılım gözlemlenebilirliği ve telemetrisinin (bölüm 9.2) doğrudan karşılığıdır: istek gecikmesini ve hata oranlarını izlemenizi söyleyen içgüdü, veri güncelliğini, hacmini, şemasını ve dağılımını da izlemenizi söyler. Bu bölüm veri stratejisi ve yönetişimi (bölüm 7.1) ile veri mühendisliği (bölüm 7.2) üzerine kurulur; veri modelleme ve anlamsal katmanı (bölüm 7.7) ile sorumlu ve güvenilir yapay zekayı (bölüm 6.5) besler. Birçok kaynak sistemi uzlaştıran kurumsal yapılar ve yasal istatistikler yayımlayan kamu kurumları için veri güvenilirliğini sahipleri ve hizmet düzeyleri olan bir mühendislik sorunu olarak ele almak, güven ile çok görünür bir düzeltme arasındaki farktır.

## Temel ilkeler

- Veri kalitesi kullanıma uygunluktur, mükemmellik değil; onu amaca göre tanımlayın.
- Kötü veri hiç veri olmamasından daha kötüdür, çünkü kararları sessizce bozar.
- Veriyi kodu sınadığınız gibi sınayın: işlem hattında doğrulamalar, beklentiler ve şema denetimleri.
- Üretici ile tüketici arasındaki sözleşmeler beklentileri açık ve uygulanabilir kılar.
- Güncelliği, hacmi, şemayı ve dağılımı hizmetleri gözlemlediğiniz gibi gözlemleyin.
- Soy ağacı (lineage), "bir şey yanlış" ifadesini "şu bozuldu ve şunları etkiliyor" ifadesine çevirir.
- Veri olaylarına üretim olayları gibi davranın: sahiplik, ciddiyet ve hizmet düzeyleriyle.
- Sorunları girdikleri yerde yakalayın, üç katman aşağıda bir panoda değil.

## Öneriler

### Kaliteyi boyutlara göre tanımlayın ve ölçün

Belirsiz kalite hedefleri belirsiz sonuçlar üretir. Kaliteyi ölçülebilir boyutlara ayırın ve her birine somut denetimler bağlayın. Doğruluk, değerlerin gerçeği yansıtıp yansıtmadığını sorar (kaydedilen bu gelir kaynak defterle uyuşuyor mu). Bütünlük (eksiksizlik), beklenen kayıtların ve alanların mevcut olup olmadığını sorar (eksik günler var mı, zorunlu sütunlar boş mu). Tutarlılık, aynı olgunun sistemler arasında uyuşup uyuşmadığını sorar (finanstaki müşteri sayısı ambardaki sayıyla aynı mı). Güncellik, verinin yararlı olacak kadar zamanında gelip gelmediğini sorar (dünün verisi sabah raporundan önce hazır mı). Geçerlilik, değerlerin kurallara ve biçimlere uyup uymadığını sorar (tüm para birimi kodları gerçek mi, tarihler aralık içinde mi). Tekillik, varlıkların bir kez görünüp görünmediğini sorar (toplamı şişiren yinelenen siparişler var mı). Her veri kümesi için önemli olan boyutları seçin, eşikler koyun ve bunları zaman içinde izleyin. Ölçmediğiniz kalite, tahmin yürüttüğünüz kalitedir.

### İşlem hatlarını doğrulamalar ve beklentilerle sınayın

Veri, uygulama kodu kadar titiz sınanmayı hak eder. Her aşamada [veri doğrulamasını](https://en.wikipedia.org/wiki/Data_validation) kullanın: bir değişmez ihlal edildiğinde işlem hattını durduran doğrulama (assertion) tabanlı testler ve bir tablo için "normal"in neye benzediğini bildirip sapmaları işaretleyen beklenti tabanlı testler. Birincil anahtarların tekil ve boş olmadığını, yabancı anahtarların çözümlendiğini, kategorik sütunların yalnızca kabul edilen değerleri içerdiğini, sayısal sütunların makul aralıklarda kaldığını ve satır sayılarının beklenen bir bantta olduğunu doğrulayın. Yukarı akışta bir sütun eklendiğinde, silindiğinde, yeniden adlandırıldığında ya da türü değiştiğinde yüksek sesle başarısız olan şema denetimleri ekleyin. Bu denetimleri sürekli tümleştirmede çalıştırın ki kötü bir dönüşüm birleştirmeden önce yakalansın; ardından üretimde canlı veriye karşı yeniden çalıştırın ki kötü bir kaynak tüketicilere ulaşmadan yakalansın. Amaç erken ve yüksek sesle başarısız olmaktır, çünkü bozulmuş bir işlem hattı sessizce yanlış olandan daha güvenlidir.

### Üretici ve tüketici arasında veri sözleşmeleri kurun

Veri kalitesi olaylarının çoğu yukarı akışta başlar: üretici bir takım, kimin buna dayandığını bilmeden bir şemayı, bir anlamsal anlamı ya da bir değer kuralını değiştirir. Bir [veri sözleşmesi](https://en.wikipedia.org/wiki/Data_contract) arayüzü açık hale getirerek bunu çözer: şema, her alanın anlamı, izin verilen değerler, güncellik garantileri ve değişiklik yapma süreci. Üretici sözleşmeye bağlanır, tüketici ona göre inşa eder ve uyumsuz bir değişiklik, pazartesi günü sessiz bir sürpriz yerine sürümleme ve önceden bildirim gerektirir. Sözleşmeleri mümkün olduğunda mekanik olarak uygulayın: gelen veriyi sınırda sözleşmeye göre doğrulayın, ihlalleri reddedin ya da karantinaya alın. Sözleşmeler örtük ve kırılgan bir bağımlılığı açık ve pazarlıkla belirlenmiş birine çevirir. Ayrıca sahipliği görünür kılar; bu, ölçekte savaşın yarısıdır.

### Veri gözlemlenebilirliğinin dört sinyalini izleyin

Veri gözlemlenebilirliği, çalışan bir hizmeti izleme biçiminize doğrudan paralel olarak (bölüm 9.2) dört sinyali izler. Güncellik: veri olması gerektiği kadar yeni mi, yoksa işlem hattı durdu mu. Hacim: satır sayısı beklenen aralıkta mı, yoksa bir tablo yarı boş ya da çift yüklenmiş olarak mı geldi. Şema: yapı beklenmedik biçimde değişti mi. Dağılım: değerlerin kendisi kaydı mı; yani yüzde 2 boş olan bir sütun birden yüzde 40 boş mu oldu, ya da bir ortalama yukarı akıştaki bir hataya işaret edecek biçimde mi kaydı. Önemli tablolarınızda bu sinyalleri ölçün, normal örüntülerini öğrenin ve ihlallerde uyarı verin. "Bir yönetici panonun yanlış göründüğünü fark etti" durumunu "sahip takım arıza noktasında çağrıldı" durumuyla değiştirmenin yolu budur. Bir veri sorununun olabilecek en kötü dedektörü, rakama güvenen aşağı akıştaki bir insandır.

### Anomali tespiti ekleyin, ama uyarı yorgunluğuna karşı ayarlayın

Statik eşikler bariz başarısızlıkları yakalar. Daha ince kaymalar için her ölçütün normal mevsimsel örüntüsünü öğrenen ve istatistiksel olarak olağandışı sapmaları işaretleyen [anomali tespiti](https://en.wikipedia.org/wiki/Anomaly_detection) ekleyin; böylece yavaş bir sızıntıyı sel olmadan yakalarsınız. Bu konuda disiplinli olun. Gürültülü anomali uyarıları insanlara uyarıları görmezden gelmeyi öğretir; bu, hiç uyarı olmamasından daha kötüdür. En değerli tablolarınızla başlayın, yalnızca bir insanın harekete geçmesi gereken şeylerde uyarı verin, her uyarıyı adı belli bir sahibe yönlendirin ve acımasızca ayarlayın. Kimsenin harekete geçmediği bir uyarı, izlemenizdeki bir hatadır, bir özellik değil.

### Etki analizi ve kök neden için soy ağacını izleyin

Bir şey bozulduğunda hemen iki soru önem kazanır: buna ne sebep oldu ve neyi etkiliyor. [Veri soy ağacı](https://en.wikipedia.org/wiki/Data_lineage), verinin kaynaktan her dönüşüm boyunca her aşağı akış tablosuna, panoya ve modele nasıl aktığını haritalayarak ikisini de yanıtlar. Kök neden için kötü bir rakamı yukarı akışta onu getiren dönüşüme ya da kaynağa kadar izlersiniz. Etki analizi için ileriye doğru izleyerek kötü bir yüklemeden etkilenen her tüketiciyi görürsünüz; böylece onlara haber verebilir ve zararı yayılmadan karantinaya alabilirsiniz. Soy ağacını, elle bir diyagram tutmak yerine dönüşüm ve orkestrasyon araçlarınızdan otomatik olarak yakalayın; çünkü elle çizilmiş bir diyagram çizdiğiniz günün ertesi günü yanlıştır. Çok kaynaklı kurumlarda soy ağacını bir veri kataloğuna yayımlayın; böylece her tüketici bir alanın nereden geldiğini görebilir ve ona göre güvenebilir.

### Veri olaylarına üretim olayları gibi davranın

Hizmetleri güvenilir tutan uygulamalar veriye doğrudan uygulanır. Her önemli veri kümesine bir sahip verin. "Veri kesintisi" için, yani verinin eksik, yanlış ya da geç olduğu dönemler için ciddiyet düzeyleri tanımlayın. Hizmet düzeyleri belirleyin: güncellik hedefleri, kabul edilebilir bir hata bütçesi ve hedeflenen tespit ve çözüm süresi. En kritik işlem hatlarının arkasına veri nöbet çizelgeleri koyun, çalıştırma kılavuzları (runbook) yazın ve olaylardan sonra aynı başarısızlık tekrarlanmasın diye suçlamasız olay sonrası incelemeler yapın. Bir ödeme tablosu geç kaldığında ya da kamuya açık bir ölçüt yanlış olduğunda bu bir olaydır ve bir kesinti kadar ciddiyeti hak eder. Tüm araçların karşılığını vermesini sağlayan kültürel değişim budur.

### Sürekli profilleyin ve uzlaştırın

Profilleme, verinizin biçimini düzenli olarak incelemek demektir: değer dağılımları, boş oranları, kardinalite, en küçük ve en büyük değerler ve biçim örüntüleri. Doğrulamayı akıl etmediğiniz sorunları yüzeye çıkarır ve "normal"in neye benzediğini söyler; böylece iyi beklentiler koyabilirsiniz. Uzlaştırma, bağımsız kaynakların uyuşup uyuşmadığını denetlemek demektir: ambar toplamı kayıt sistemiyle eşleşiyor mu, parçaların toplamı bütüne eşit mi. Kritik sistemler arasındaki uzlaştırmayı otomatikleştirin ve ayrışmada uyarı verin; çünkü bir uzlaştırma kopukluğu çoğu zaman yukarı akışta bir şeylerin ters gittiğine dair en erken ve en net sinyaldir.

## Ödünleşimler: artılar ve eksiler

| Yaklaşım | Artılar | Eksiler | En uygun yer |
|---|---|---|---|
| Doğrulama testleri (sert başarısızlık) | Kötü veriyi hemen durdurur, net değişmezler | Küçük sorunlarda işlem hatlarını engelleyebilir | Kritik anahtarlar, referans bütünlüğü |
| Beklenti testleri (yumuşak işaret) | Kaymayı yakalar, daha az kırılgan | Ayar gerektirir, görmezden gelinebilir | Dağılımlar, hacim bantları |
| Veri sözleşmeleri | Yukarı akış sürprizlerini önler, net sahiplik | Koordinasyon ve yönetişim yükü | Takımlar arası üretici ve tüketici sınırları |
| Anomali tespiti | İnce, öngörülmemiş kaymayı yakalar | Uyarı yorgunluğu, yanlış pozitifler | Yüksek değerli tablolar, mevsimsel ölçütler |
| Elle örnek denetimleri | Başlamak ucuz, araç gerekmez | Ölçeklenmez, sessiz hataları kaçırır | Yalnızca çok erken aşama |
| Tam gözlemlenebilirlik platformu | Geniş kapsam, soy ağacı, uyarı | Maliyet, kurulum, işletilecek bir sistem daha | Çok kaynak, düzenlemeye tabi raporlama |

Temel gerilim kapsam ile gürültü arasındadır. Hiçbir şeyi ölçmezseniz sorunlar önce tüketicilerinize ulaşır, bu da güveni yok eder. Her şeyi kıl payı hassasiyetli uyarılarla ölçerseniz takımınızı yanlış pozitiflerde boğarsınız; sonunda kanalı susturur ve yine sorunlar tüketicilere ulaşır. Bunu, verilerinizi etki alanına göre sıralayarak çözün. Yönetim kurulu ölçütlerini, müşteriye dönük ürünleri, düzenleyici raporları ve makine öğrenmesi modellerini besleyen tablolar tam muameleyi görür: sözleşmeler, sert doğrulamalar, gözlemlenebilirlik ve nöbetçi sahiplik. Keşif amaçlı tabloların uzun kuyruğu hafif profilleme alır. Güvenilirlik bütçenizi yanlış verinin en çok zarar vereceği yerde harcayın ve başka her yerde bilerek tutumlu olun.

## Takımınızla tartışılacak sorular

1. **Kötü veri üretime ulaştığında bunu önce kim, nasıl öğreniyor?** Bu, veri güvenilirliğiniz hakkındaki en açıklayıcı sorudur, çünkü dürüst cevap genellikle "bir tüketici, tesadüfen"dir. Bir analist, bir yönetici ya da bir müşteri sizin tespit sisteminizse, ortalama tespit süreniz günlerle ölçülür ve itibarınız her seferinde zarar görür. Alternatif, kötü rakam yayılmadan, arıza noktasında sahip takımı çağıran ölçümlemedir. Gerçek sayılar getirin: son on veri olayınızdan kaçı izleme ile yakalandı, kaçı aşağı akıştaki bir insan tarafından bildirildi ve her biri ne kadar süre fark edilmeden kaldı. Cevap, gözlemlenebilirliğiniz mi yoksa yalnızca umudunuz mu olduğunu söyler ve güncellik, hacim, şema ve dağılım denetimlerine önce nerede yatırım yapacağınızı doğrudan belirlemelidir.

2. **Hangi veri kümelerinin sahibi, sözleşmesi ve hizmet düzeyi var, hangileri sahipsiz?** Ölçekte veri kalitesi başarısızlıklarının çoğu sahipsiz bir arayüze çıkar: bir üretici takım, hiçbir sözleşme söylemediği için kimin buna dayandığını bilmeden bir şeyi değiştirmiştir. Sahiplik; sözleşmeleri, uyarı yollarını ve olay müdahalesini mümkün kılan temeldir ve sahipsiz veri kümeleri sessiz bozulmanın yaşadığı yerlerdir. En önemli tablolarınızı tek tek gözden geçirin ve her biri için kimin sorumlu olduğunu, üreticinin neyi taahhüt ettiğini ve tüketicilere hangi güncellik ve doğruluğun vaat edildiğini sorun. Soy ağacınızı getirin: en büyük aşağı akış etki alanına sahip tablolar buna en çok ihtiyaç duyanlardır ve çoğu zaman en çok eksik olanlardır. "Önemli" ile "sahipli" arasındaki boşluk, gelecek çeyreğin öncelik listenizdir.

3. **Bir veri kalitesi olayının bize gerçek maliyeti nedir ve buna göre mi davranıyoruz?** Takımlar veri kalitesine az yatırım yapar, çünkü kötü verinin maliyeti dağınık ve gecikmelidir, hiçbir zaman bir kalem olarak görünmez; kalite araçlarını inşa etmenin maliyeti ise somut ve anlıdır. Gerçek bir olayı uçtan uca fiyatlandırarak yeniden çerçeveleyin: yanlış karar, yeniden iş, soy ağacı olmadan kök nedeni izlemeye harcanan mühendis saatleri, insanların sessizce kendi gölge veri kümelerini yeniden kurmasına yol açan aşınmış güven ve düzenlemeye tabi ya da kamuya dönük ortamlarda düzeltme bildirimi ile itibar zararı. Geçen yıldan belirli bir örnek getirin ve dürüstçe toplayın. Bir ödeme ya da kamu istatistiği işlem hattındaki tek bir sessiz başarısızlık bir yıllık gözlemlenebilirlik aracından daha pahalıya mal olabiliyorsa, iş gerekçesi kendiliğinden ortaya çıkar ve sohbet yatırım yapıp yapmamaktan nereye yapılacağına kayar.

4. **Veri kümelerimizi etki alanına göre sıraladık mı ve izleme yatırımımız gerçekten bu sıralamayı izliyor mu?** Ölçekte temel başarısızlık biçimi, güvenilirlik çabasını eşit dağıtmaktır: kimsenin güvenmediği keşif tablosu, yönetim kurulu ölçütlerini besleyen tabloyla aynı ilgiyi görür; düşük değerli bir tabloda kıl payı hassasiyetli bir uyarı ise insanlara kritik çağrıyı da taşıyan kanalı susturmayı öğretir. Her şeyi ölçümleyip gürültüde boğulamazsınız ve hiçbir şeyi ölçümlemeyip sorunların önce tüketicilere ulaşmasına izin veremezsiniz; yani asıl karar, tam muamelenin (sözleşmeler, sert doğrulamalar, gözlemlenebilirlik ve nöbetçi sahiplik) nereye gideceği ve hafif profillemenin nerede yeteceğidir. Tablolarınızın, kendilerine neyin dayandığına göre etiketlenmiş bir envanterini getirin: yönetim kurulu ölçütleri, müşteriye dönük ürünler, düzenleyici raporlar ve makine öğrenmesi modelleri. Ardından bu sıralamayı denetimlerinizin ve uyarılarınızın bugün gerçekte nerede durduğuyla karşılaştırın. Birçok kaynağı uzlaştıran bir kurum ya da yasal rakamlar yayımlayan bir kamu kurumu için yasal ya da kamusal riski olan tablolar listenin başında yer almalıdır; "yanlışsa en çok zarar verecek" ile "en çok izlenen" arasındaki herhangi bir boşluk, şimdi düzeltilmesi gereken bir önceliklendirme hatasıdır.

5. **Hangi makine öğrenmesi modelleri ve analizler hiç doğrulamadığımız veriye dayanarak karar veriyor ve içlerine sessizce hangi hataları işliyor olabilirler?** Bir pano, sorgulayabilecek tek bir insana yanlış bir rakam gösterir; ama bir model yanlış özniteliklerle eğitilir ve bu hataları yaptığı her tahmine işler; üstelik zararın fark edilmesini ya da geri alınmasını çok daha zorlaştıran bir ölçek ve donuklukla. Karşıt baskı hızdır: veri bilimi takımları yeni özniteliklerde hızlı ilerlemek ister ve her beslemeye doğrulama, sözleşme ve güncellik garantisi eklemek, yukarı akıştaki bir sütun kayıp bir model sessizce bozulana kadar sürtünme gibi hissettirir. Üretimdeki modellerinizin ve analizlerinizin, her birinin tükettiği veri kümelerinin envanterini ve bu beslemelerden hangilerinin testlere, sözleşmelere ve gözlemlenebilirliğe sahip, hangilerinin korumasız olduğunun dürüst bir işaretlemesini getirin. Bir modelin kredi, yardım ya da yaptırım kararlarını etkilediği kurumsal ya da kamu ortamında doğrulanmamış eğitim verisi, bir kalite riskinin üstüne denetim ve adalet yükümlülüğü haline gelir; bu yüzden hangi beslemelerin bir model sürümünü kapıladığı sorusunun bir sahibi ve belgelenmiş bir cevabı olmalıdır (bölüm 6.5).

6. **Bir kalite hatası haftalar sonra ortaya çıktığında gerçekten yeniden işleyip uzlaştırabiliyor muyuz, yoksa ihtiyaç duyacağımız şeyi çoktan atmış mıyız?** Birçok kalite başarısızlığı yükleme anında görünmezdir ve ancak bir uzlaştırma kopukluğu ya da şüpheli bir eğilim birinin bakmasına yol açtığında netleşir; o zamana kadar bunu temiz biçimde düzeltebilmek, çok daha önce yaptığınız seçimlere bağlıdır: değişmez ham kayıtları tuttunuz mu, bağımsız kaynaklar uzlaştırılabiliyor mu ve soy ağacı kötü rakamı kaynağına kadar izlemenize izin veriyor mu. Gerilim, maliyet ve sadelik ile yeniden üretilebilirlik arasındadır; çünkü ham veriyi saklamak ve sistemler arasında sürekli uzlaştırma çalıştırmak bedava değildir ve dönüştürülmüş tablolar doğru göründüğünde ham girdileri silmek cazip gelir. Ham veri için saklama ve değişmezlik politikanızı, otomatik uzlaştırdığınız kritik sistem çiftlerinin listesini ve yeniden işleyerek içinden çıkabildiğiniz ya da çıkamadığınız gerçek bir hata örneğini getirin. Yayımlanan herhangi bir rakamı kaynak kayıtlara kadar izleme yasal yükümlülüğü altındaki bir kamu kurumu ya da düzenleyici bir yeniden beyanla karşı karşıya olan bir kurum için değişmez ham veri ve otomatik uzlaştırma isteğe bağlı hijyen değil, bir düzeltmeyi savunulabilir kılan mekanizmadır.

## Sektör merceği

**Girişim.** Hız ve güven, kapsamdan daha önemlidir. Dönüşüm aracınıza bir avuç hafif test koyun (anahtarlarda tekillik ve boş olmama, anlam taşıyan sütunlarda kabul edilen değerler, kaynak başına bir satır sayısı bandı) ve güncellik ile hacim izlemeyi yalnızca şirket ölçütlerini besleyen birkaç tabloya ekleyin. Her uyarıyı bir mühendisin sahip olduğu tek bir kanala yönlendirin ve gerekçelendirecek tablolara ya da takıma sahip olmadan bir gözlemlenebilirlik platformu satın almaya direnin. Amaç her şeyi ölçümlemek değil, yanlış etiketlenmiş bir alanı, kurucuların alıntıladığı bir rakamı şişirmeden önce fark etmektir.

**Küçük işletme.** Veri mühendisi olmadan ve dar bir bütçeyle, ayrı bir yığın kurmak yerine ödediğiniz ambarda, BI aracında ya da SaaS platformlarında zaten yerleşik olan kalite özelliklerine yaslanın. Çabanızı gerçekte kararları yönlendiren birkaç rakama (gelir, satış hattı, stok) odaklayın, bunları düzenli aralıklarla bağımsız bir kaynakla kontrol edin ve bir satıcının güncellik ve şema uyarıları varsa onları yeterince iyi sayın. Zaten çalıştırdığınız araçlara gömülü kalite satın almak, bakımını yapacak kimsenizin olmadığı bir işlem hattı kurmaktan iyidir.

**Kurumsal.** Sorun, birçok takım ve binlerce tablo boyunca güvenilirliktir; bu yüzden arayüzü standartlaştırın: her üretici sınırında veri sözleşmeleri, güncelliği, hacmi, şemayı ve dağılımı izleyen bir gözlemlenebilirlik platformu ve etki analizi için bir kataloğa yayımlanan soy ağacı. Veri kümelerini etki alanına göre sıralayın, yüksek değerli olanlara anomali tespiti ve nöbetçi sahiplik koyun ve veri olaylarını hizmet kesintileriyle aynı ciddiyet ve olay sonrası inceleme sürecinden geçirin. Düzenleyici raporları ve yönetici panolarını besleyen işlem hatlarındaki hizmet düzeyleri, veri güvenilirliğini bir arzudan ölçülen ve yönetilen bir taahhüde çevirir.

**Kamu.** Yasal doğruluk ve kamusal hesap verebilirlik çıtayı belirler: değişmez ham anket ve idari kayıtları yükleyin, bunları katmanlı ve sınanmış aşamalarda dönüştürün ve her adımda kaynak toplamlarına karşı uzlaştırın. Yayımlanan her rakam denetim için kaynak kayıtlara kadar izlenebilsin diye tam soy ağacını tutun ve her yayını geçerlilik, bütünlük ve önceki dönemlerle tutarlılık doğrulamasının arkasına kapılayın. Araç tedariki şeffaflık ve veri taşınabilirliği talep etmelidir; yanlış bir kamu istatistiği ciddi bir olay olarak ele alınmalıdır, resmi rakamlara duyulan kamu güveninin gerektirdiği ağırlıkla.

## Örnekler

**Girişim.** Yirmi kişilik bir şirket pazara çıkış çalışmasını ürün olayları ve bir ödeme sağlayıcısı tarafından beslenen bir ambar üzerinde yürütür. Erken dönemde yanlış etiketlenmiş bir para birimi alanı, kimse fark etmeden iki hafta boyunca bildirilen geliri sessizce şişirdi ve bu, takımın her panoya olan güvenini sarstı. Dönüşüm aracında hafif bir test kümesiyle karşılık verdiler: anahtarlarda tekillik ve boş olmama, para birimi ve durum sütunlarında kabul edilen değer denetimleri ve kaynak başına bir satır sayısı bandı. Şirket ölçütlerini besleyen birkaç tabloya temel güncellik ve hacim izleme eklediler ve bunu bir mühendisin sahip olduğu tek bir Slack kanalına yönlendirdiler. Mütevazı, ama önemli başarısızlıkları yakalıyor ve kurucular rakamlara yeniden güveniyor.

**Kurumsal.** Çok uluslu bir banka, müşteri ve işlem verisini onlarca kaynak sistemden, düzenleyici raporları, risk modellerini ve yönetici panolarını besleyen yönetilen bir ambarda uzlaştırır. Her üretici sınırında veri sözleşmeleri çalıştırır; böylece yukarı akıştaki bir şema değişikliği tüketicilerin üzerine boşaltılmak yerine sürümlenir ve pazarlıkla belirlenir. Bir gözlemlenebilirlik platformu binlerce tabloda güncelliği, hacmi, şemayı ve dağılımı izler; yüksek değerli tablolarda anomali tespiti çalışır ve soy ağacı etki analizi için bir veri kataloğuna yayımlanır. Veri olayları, düzenleyici başvuruları besleyen işlem hatlarında hizmet düzeyleriyle birlikte, hizmet kesintileriyle aynı ciddiyet ve nöbet sürecini izler. Bir kaynak sistem kaydığında sahip takım çağrılır ve etkilenen aşağı akış raporlar dakikalar içinde bilinir; bir düzenleyici tarafından keşfedilmez.

**Kamu.** Bir ulusal istatistik kurumu, piyasaların, politika yapıcıların ve kamuoyunun yetkili saydığı ekonomik göstergeler yayımlar; bu yüzden doğruluk yasal bir yükümlülüktür ve yayımlanan her rakam denetlenebilir olmalıdır. İşlem hatları değişmez ham anket ve idari kayıtları yükler, ardından bunları katmanlı ve sınanmış aşamalarda dönüştürür ve her adımda kaynak toplamlarıyla uzlaştırır. Tam soy ağacı, analistlerin yayımlanan herhangi bir rakamı kaynak kayıtlara kadar izlemesine olanak tanır; bu hem bir kalite aracı hem de yasal bir gerekliliktir. Yayından önce rakamlar, geçerlilik, bütünlük ve önceki dönemlerle tutarlılık için doğrulama kapılarından geçer ve her anomali yayımlanmak yerine incelenir ve belgelenir. Yanlış bir kamu istatistiği ciddi bir olaydır; bu yüzden kurum veri kesintisine, kamu güveninin gerektirdiği ağırlıkla yaklaşır.

## İş gerekçesi: motivasyonlar, YG ve TSM

Veri kalitesi ve gözlemlenebilirliğin getirisi; korunan güvenden, kısalan olaylardan ve önlenen kötü kararlardan gelir. Güvenilir veri, aşağı akıştaki her analitik, iş zekası ve yapay zeka yatırımının gerçekten karşılık vermesini sağlayan temeldir, çünkü bir model ya da pano altındaki veri kadar iyidir. Kalite denetimleri kötü bir yüklemeyi sınırda yakaladığında, yanlış bir rakamın bir karara, bir müşteriye ya da bir başvuruya ulaşmasının çok daha büyük maliyetinden kaçınırsınız. Soy ağacı, kök neden araştırmasını günlerce süren elle izlemeden dakikalara indirir; bu, saf biçimde geri kazanılmış mühendislik zamanıdır. Gözlemlenebilirlik, ortalama tespit süresini "bir tüketici şikayet ettiğinde" noktasından "işlem hattı başarısız olduğunda" noktasına çeker; güven zararının çoğunun önlendiği yer burasıdır.

Toplam sahip olma maliyeti (TSM); test, gözlemlenebilirlik ve kataloglama araçlarını, işlem hatlarını ölçümlemek için gereken mühendislik zamanını ve sahip atama ile sözleşme yazma gibi örgütsel işi içerir. Bu gerçektir, ama yapmamanın maliyetiyle tartın: yöneticilerin keşfettiği sessiz bozulma, kötü özniteliklerle eğitilip hataları ölçekte işleyen makine öğrenmesi modelleri, artık resmi olanlara güvenmedikleri için gölge veri kümelerini sessizce yeniden kuran analistler ve düzenlemeye tabi ya da kamusal ortamlarda yıllarca itibarı zedeleyen düzeltme bildirimleri. Liderliğe veri kalitesini, kurumun yaptığı her veriye dayalı karar üzerindeki bir sigorta olarak sunun. Prim mütevazı ve öngörülebilirdir. Sigortasız kayıp, yani tek bir yüksek profilli yanlış rakam, ne mütevazıdır ne öngörülebilir.

## Anti-kalıplar ve tuzaklar

- Veri kalitesine süregelen bir mühendislik uygulaması yerine tek seferlik bir temizlik projesi olarak yaklaşmak.
- Başarısızlıkları arıza noktasındaki izlemeyle değil, aşağı akıştaki tüketicilerden keşfetmek.
- Veri kümesi sahipliğinin olmaması; böylece bir şey bozulduğunda kimsenin hesap vermemesi ve kimsenin çağrılmaması.
- Üreticilerin sözleşme olmadan şemaları ya da anlamsal anlamları değiştirip her tüketiciyi sessizce bozması.
- Takımın kanalı susturup gerçek olayı kaçıracağı kadar gürültülü anomali uyarıları.
- Doğrulanmamış veriyi doğrudan makine öğrenmesi modellerine besleyip hataları ölçekte işlemek (bölüm 6.5).
- Soy ağacını, çizildiği günün ertesi günü yanlış olan elle çizilmiş bir diyagram olarak tutmak.
- Önemli tablolarda kullanıma uygun kalite yerine her yerde mükemmel verinin peşinden koşmak.
- Ham veriyi silmek; böylece bir kalite hatası sonradan ortaya çıktığında yeniden işleyememek ya da uzlaştıramamak.

## Olgunluk modeli

- **Düzey 1, Başlangıç:** Kalite kimsenin işi değildir. Sorunları tüketiciler bulur, genellikle yanlış bir rakam bir rapora ulaştıktan sonra. Test, izleme ya da sahiplik yoktur. Düzeltmeler elle yangın söndürmedir ve aynı başarısızlıklar tekrarlanır.
- **Düzey 2, Geliştirme:** Bazı takımlar kritik tablolarına temel testler (anahtarlar, boşluklar, kabul edilen değerler) ve en çok önem verdikleri veri kümelerine biraz güncellik ve hacim izleme ekler. Uygulamalar bulundukları yerde işe yarar, ama kapsam ve titizlik takımdan takıma değişir, hiçbir şey standartlaştırılmamıştır ve olaylar hâlâ tepkisel biçimde ele alınır.
- **Düzey 3, Standartlaştırma:** Kalite boyutları eşiklerle tanımlanır ve aynı beklentiler, bir işlem hattını kimin kurduğuna bağlı kalmadan takımlar arasında geçerlidir. Veri sözleşmeleri temel üretici sınırlarını yönetir, gözlemlenebilirlik önemli tablolarda güncelliği, hacmi, şemayı ve dağılımı kapsar ve soy ağacı etki analizini destekler. Her önemli veri kümesinin adı belli bir sahibi vardır ve veri olayları kurum genelinde belgelenmiş bir ciddiyet ve müdahale sürecini izler.
- **Düzey 4, Yönetme:** Kalite ve güvenilirlik, temel çizgilere karşı ölçülür ve denetlenir. Veri kesintisi gerçek ölçütlerle izlenir: ortalama tespit süresi, ortalama çözüm süresi, üzerinde anlaşılmış hizmet düzeylerine karşı güncellik ve doğruluk ve bir veri kümesinin harekete geçmeden önce harcayabileceği hata bütçeleri. Uzlaştırma kopukluğu oranları, test geçme oranları ve anomali yanlış pozitif oranları zaman içinde eğilim olarak izlenir, uyarılar tahminle değil bu sayılara göre ayarlanır ve bir veri yayını için git ya da gitme kararları umutla değil, temel çizgiye karşı ölçülen kaliteyle verilir.
- **Düzey 5, Orkestrasyon:** Kalite ve gözlemlenebilirlik yaygın, otomatik ve uyarlanabilirdir. Anomali tespiti ince kaymayı yakalar, sözleşmeler mekanik olarak uygulanır ve soy ağacı otomatik olarak yakalanıp bir kataloğa yayımlanır. Veri, üretim hizmetleri gibi hizmet düzeylerine ve nöbetçi sahipliğe sahiptir, uzlaştırma sürekli çalışır ve suçlamasız olay sonrası incelemeler veri kesintisinde istikrarlı bir azalmayı besler. Kalite; veri yönetişimi, makine öğrenmesi ve iş planlamasıyla bütünleşir ve kurum, veri ortamı değiştikçe eşikleri, kapsamı ve sahipliği sürekli yeniden belirler.

## Tartışma fikirleri

1. Hangi tablolarınız bir hafta boyunca sessizce yanlış olsa en çok zarara yol açar ve bunlar en çok izlediğiniz tablolar mı?
2. Son yukarı akış kaynaklı olayınızı bir veri sözleşmesi nerede önlerdi ve neden yoktu?
3. Tipik bir kök neden araştırması bugün ne kadar mühendislik zamanı alıyor ve otomatik soy ağacı ne kadarını kurtarırdı?
4. Makine öğrenmesi modellerinizden herhangi biri doğrulamadığınız veriyle mi eğitiliyor ve hangi hataları içine işliyor olabilir?
5. Uyarılarınız herkesin her uyarıya harekete geçeceği kadar iyi ayarlı mı, yoksa biri kanalı sustu mu?
6. En önemli tüketicileriniz hangi güncellik ve doğruluk hizmet düzeylerini gerçekten kabul ederdi ve bugün bunları karşılayabilir misiniz?

## Önemli çıkarımlar

- Veri kalitesi; doğruluk, bütünlük, tutarlılık, güncellik, geçerlilik ve tekillik boyunca kullanıma uygunluktur.
- Kötü veri hiç veri olmamasından daha kötüdür, çünkü kararları ve modelleri sessizce bozar.
- Veriyi kod gibi sınayın: CI'da ve üretimde doğrulama ve beklenti testleri ile şema denetimleri.
- Üretici ve tüketici beklentilerini açık ve uygulanabilir kılmak için veri sözleşmeleri kullanın.
- Güncelliği, hacmi, şemayı ve dağılımı, yazılım gözlemlenebilirliğine paralel olarak (bölüm 9.2) gözlemleyin.
- Hızlı kök neden ve etki analizi için soy ağacını yakalayın ve tüketiciler için yayımlayın.
- Veri olaylarına üretim olayları gibi davranın: sahiplik, ciddiyet ve hizmet düzeyleriyle.
- Yanlış verinin en çok zarar vereceği yerde ölçümleme yapın; her yerde mükemmellik değil, kullanıma uygun kalite hedefleyin.

## Kaynaklar ve ileri okuma

- Barr Moses, Lior Gavish, and Molly Vorwerck, "Data Quality Fundamentals."
- Jacek Majchrzak, Sven Balnojan, and Marian Siwiak, "Data Contracts."
- Danette McGilvray, "Executing Data Quality Projects."
- Thomas C. Redman, "Data Driven: Profiting from Your Most Important Business Asset."
- Laura Sebastian-Coleman, "Measuring Data Quality for Ongoing Improvement."
- Joe Reis and Matt Housley, "Fundamentals of Data Engineering."
- DAMA International, "DAMA-DMBOK: Data Management Body of Knowledge."
- ISO/IEC 25012, "Data quality model."
