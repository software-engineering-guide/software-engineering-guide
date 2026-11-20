# 10.15 Tahmin ve öngörü

## Genel bakış ve motivasyon

Her yazılım takımına aynı soru sorulur: ne zaman biter? Bu sorunun arkasında [yazılım geliştirme eforu tahmini](https://en.wikipedia.org/wiki/Software_development_effort_estimation) yatar: bir işin ne kadar emek alacağını, henüz yapmadan önce öngörme pratiği. Yaptığımız en zor işlerden biridir ve kötü yapılması en kolay olanlardan biridir. Sorun, yazılımın bir keşif işi olmasıdır. Daha önce hiç var olmamış bir şey inşa ediyorsunuz ve problem hakkında öğreneceğiniz şeylerin çoğu ancak inşa ederken görünür hale geliyor. Öğrenmenin eforunu öngörmek, bilinen bir görevi tekrarlamanın eforunu öngörmekten gerçekten farklıdır.

Neden bunu proje yönetiminin (bölüm 10.6) bir köşesi olarak değil, ayrı bir disiplin olarak ele alıyoruz? Çünkü başarısızlıklar çok tutarlı ve çok pahalı. Takımlar düzenli olarak kanıtları olmayan tek tarihlere söz veriyor, sonra gerçeklik bu tarihleri çürüttükten çok sonra bile onları savunuyor. Liderler bir tahmini bir sözle karıştırıyor. Sözleşmeler bir öğleden sonra üretilmiş bir sayıyı dondurup insanları bir yıl boyunca ona bağlıyor. Sonuç geç teslimat, aşınan güven ve kimsenin gerçekte neye inandığını söylemediği bir kültür. Bunu doğru yapmak daha iyi matematikten çok dürüstlükle ilgilidir: bildiğinizi umduğunuzdan ayırmak ve belirsizliği belirsizlik olarak iletmek.

Bahisler kurumsal ve kamu ortamlarında keskin biçimde yükselir. Kurumlar iç içe geçmiş girişimlerden oluşan portföyleri yıllık bütçelere karşı finanse eder ve sermayeyi dağıtmak için kesin rakamlar bekler (bölüm 10.1). Hükümetler ödenek kuralları çerçevesinde kamuoyuna taahhütlerde bulunur, sabit fiyatlı sözleşmeler imzalar ve bir tarih kaydığında yasama organlarına hesap verir. Her iki dünyada da kendinden emin tek bir sayı üretme baskısı çok büyüktür ve o sayıyı güvenilmez kılan derin belirsizlik, önemli biri kesinlik istediği için ortadan kalkmaz. Bu bölüm farklı bir duruşu savunur: karar vermenize yardım ettiğinde tahmin edin, iyimserlik yerine kanıtla öngörün ve aralık hakkında doğruyu söyleyin.

## Temel ilkeler

- **Tahmin bir öngörüdür, söz değildir.** Onu hedeflerden ve taahhütlerden ayrı tutun.
- **Belirsizlik gerçektir, o yüzden ifade edin.** Olasılıklı bir aralık, sahte tek bir tarihten iyidir.
- **Geçmiş, geleceği iyimserlikten daha iyi öngörür.** Taze tahminler yerine ölçülmüş geçmişi tercih edin.
- **Anlamak için ayrıştırın, taahhüt etmek için öngörün.** Küçük dilimler hem riski hem de tahmin etme ihtiyacını azaltır.
- **Dış bakışı benimseyin.** İç hikayenize güvenmeden önce benzer geçmiş çabalarla karşılaştırın.
- **Sürekli yeniden öngörün.** Bir kez yapılıp hiç güncellenmeyen bir öngörü süstür.
- **Yalnızca cevap bir kararı değiştirecekse tahmin edin.** Aksi halde israftır.

## Öneriler

### Tahmini, hedefi ve taahhüdü birbirinden ayırın

Bu bölümdeki en yararlı hamle hiçbir şeye mal olmaz: üç fikri ayrı tutun. **Tahmin**, bir işin ne kadar süreceğine dair belirsizliğiyle birlikte dürüst öngörünüzdür. **Hedef**, vurmak istediğiniz bir iş amacıdır; bir fuar lansmanı ya da düzenleyici bir son tarih gibi. **Taahhüt**, bir başkasına verdiğiniz ve tutmayı düşündüğünüz sözdür. Bunlar üç ayrı şeydir ve bunları tek şeye indirgemek projelerin kendilerine yalan söylemeye başlamasının yoludur. Bir lider "üç ila beş ay civarı" duyup "üç ay" yazdığında ve satış ekibi bir müşteriye "on iki hafta" sözü verdiğinde, kimse riski kabul etmeye karar vermeden bir tahmin sessizce bir taahhüde dönüşmüştür.

Her seferinde hangisini verdiğinizi söyleyin. Bir tarih istenirse aralık olarak ifade edilmiş bir tahminle cevap verin, sonra işin bu tahmine karşı bir hedef koymasına ve neyi taahhüt edeceğine bilinçli olarak karar vermesine izin verin. Bir taahhüt, tahminin belirsizliğini kaçırmanın maliyetiyle tartan, gözü açık verilmiş bir seçim olmalıdır. Bu disiplin, kurumunuzun kararları nasıl aldığı ve kaydettiğiyle (bölüm 1.5) doğrudan bağlantılıdır: bir taahhüt bir karardır ve koridorda verilmiş bir baş selamı değil, bir kararın titizliğini hak eder.

### Tahminlerin neden yanlış olduğunu ve hangi yönde yanlış olduğunu anlayın

Yazılım tahminleri rastgele yanlış değildir. Öngörülebilir, sistematik biçimlerde yanlıştırlar ve örüntüyü bilmek düzeltme yapmanıza izin verir. Her çabanın başında [belirsizlik konisinin](https://en.wikipedia.org/wiki/Cone_of_Uncertainty) içindesiniz: başlangıçta tahmininiz her iki yönde de kolayca dört kat sapabilir ve aralık ancak inşa edip öğrendikçe daralır. Koninin geniş ağzında kesin bir sayıya taahhüt etmek, henüz destekleyemeyeceğiniz bir rakama taahhüt etmektir.

Bu yapısal belirsizliğin üstüne insani bir yanlılık biner. [Planlama safsatası](https://en.wikipedia.org/wiki/Planning_fallacy), en iyi senaryoyu hayal ederken kendi planlarımızın süresini, maliyetini ve riskini olduğundan düşük tahmin etme yönündeki güvenilir eğilimimizdir. Mutlu yolu gözümüzde canlandırır, kesintileri, entegrasyon sürprizlerini ve hasta günlerini unutur ve hiçbir şeyin ters gitmeyeceğini varsayan bir sayı üretiriz. Pay eklemek olağan savunma tepkisidir, ama sezgiyle eklenen pay, ilk tahminin üzerine konmuş ikinci bir tahmindir ve takvimler sıkıştığı anda pazarlıkta eriyip gider. Çare daha fazla irade değil, yöntemdir. Öngörülerinizi bu işin içeriden nasıl hissettirdiğine değil, benzer işlerin gerçekte ne kadar sürdüğüne dayandırın.

### Ayrıştırma ve uzman yargısını kullanın, sınırlarını da bilin

Ana çalışma teknikleri bilmeye de sınırlamaya da değer. **Ayrıştırma**, büyük bir çıktıyı üzerinde akıl yürütebileceğiniz daha küçük parçalara böler, sonra parçaları toplar. İşe yarar, çünkü insanlar küçük ve tanıdık şeyleri büyük ve belirsiz olanlardan çok daha iyi tahmin eder ve birçok bağımsız kalemi toplamak bazı fazla tahminlerin bazı eksik tahminleri dengelemesini sağlar. Sınırı, ayrıştırmanın kutular arasındaki işi kaçırmasıdır: entegrasyon, koordinasyon ve listelemeyi düşünmediğiniz görevler. **Uzman yargısı** ve **benzetme** yoluyla tahmin ("bu geçen yıl yaptığımız raporlama modülüne benziyor, o iki ay sürmüştü") hızlıdır ve çoğu zaman şaşırtıcı biçimde iyidir, ama tahmin edenin iyimserliğini ve kör noktalarını devralır.

Bir sayı koymak zorunda olduğunuz her şey için [üç noktalı tahmini](https://en.wikipedia.org/wiki/Three-point_estimation) tercih edin; bu yöntem iyimser, en olası ve kötümser bir rakam ister ve bunları birleştirir, çoğu zaman PERT ağırlıklı ortalaması olarak (iyimser artı dört kat en olası artı kötümser, altıya bölünür). Değer, kesin formülde değildir. Üç noktalı tahminin belirsizliğinizi yüksek sesle söylemeye zorlaması ve sahte bir nokta yerine bir aralık üretmesindedir. **Hikaye puanları** ve **tişört bedenleri** (küçük, orta, büyük, çok büyük) gibi göreli boyutlandırma yöntemleri, kesin saatleri öngörme tuzağını kalemleri birbiriyle karşılaştırarak aşar. Sıralama ve kaba kapasite için iyi çalışırlar, ama onları bir öngörünün girdisi olarak görün, para birimi olarak değil. Puanlar saat değildir ve hızı puanlarla çarparak bir tarih üretmek, göreli boyutlandırmanın kaçınmak için tasarlandığı her sorunu geri getirir.

### Kendi akış verinizden olasılıksal öngörü yapın

Her şeyi değiştiren geçiş şudur: insanlardan işin ne kadar süreceğini tahmin etmelerini istemeyi bırakın ve takımınızın işi gerçekte ne kadar hızlı bitirdiğini ölçmeye başlayın. Teslimat hattınız (bölüm 11.2) ihtiyacınız olan veriyi zaten üretiyor. [Verimi](https://en.wikipedia.org/wiki/Throughput), yani takımınızın haftada tamamladığı kalem sayısını izlerseniz, geleceği umuttan değil geçmişten öngörebilirsiniz. Son üç aydır haftada altı ila on bir kalem kapatmış bir takım, yüksek olasılıkla kalan kırk kalemi bitirmek için kabaca dört ila yedi hafta harcayacaktır. Bu öngörü kanıta dayanır ve yeni veri geldikçe her hafta kendini günceller.

Titiz sürüm bir [Monte Carlo yöntemi](https://en.wikipedia.org/wiki/Monte_Carlo_method) simülasyonu çalıştırır: olası bitiş tarihlerinin bir dağılımını oluşturmak için tarihsel haftalık veriminizden binlerce kez örnekleme yapın, sonra cevabı bir olasılık olarak okuyun. "14 Mart'a kadar bitirme olasılığımız yüzde 85, 28 Şubat'a kadar yüzde 50" ifadesi, "1 Mart'ta bitmiş olacak" ifadesinden çok daha yararlı ve çok daha dürüsttür. Bu yaklaşım kuyruk kuramıyla (bölüm 11.3) doğrudan bağlantılıdır: teslim süresi, süren işin verime bölünmesine eşittir; yani işin nasıl aktığını yöneten akış metrikleri, işin ne zaman varacağını da yönetir. Olasılıksal öngörü, geçmiş veri ve makul ölçüde kararlı bir süreç gerektirir; işte bu yüzden işi küçük ve akışı düzenli tutan takımları ödüllendirir. Ayrıca tahmin törenlerinin çoğunu sessizce ortadan kaldırır, çünkü grubun ne zaman ineceğini bilmek için artık her kalemi boyutlandırmanıza gerek kalmaz.

### Büyük programlarda dış bakışı benimseyin

Büyük, uzun ve pahalı programlarda bireysel tahminler ve hatta akış öngörüleri bile yanıltabilir, çünkü yeni bir programın henüz bir verim geçmişi yoktur ve iç hikayesi tam da planlama safsatasının en sert ısırdığı yerdir. Çare [referans sınıfı öngörüsüdür](https://en.wikipedia.org/wiki/Reference_class_forecasting): benzer tamamlanmış çabalardan oluşan bir referans sınıfı bulun, gerçekte ne kadar sürdüklerine ve ne kadar tuttuklarına bakın ve kendi alttan yukarı planınıza güvenmeden önce programınızı bu dağılımın içine yerleştirin. Şirketinizdeki benzer platform değişimleri başlangıç tahminlerini ortalama yüzde 60 aşmışsa, bu sayı sizinkiyle ilgili olarak ekibinizin az önce topladığı derli toplu plandan daha iyi bir kanıttır. Dış bakış moral bozucu hissettirir ve değeri tam da buradadır: her taze planın taşıdığı iyimserliğe karşı koyar. Sistematik bir aşımın maliyetinin milyonlarla ve itibarla ölçüldüğü portföy finansmanı ve dev program bütçelemesinde (bölüm 10.1) kullanın.

### Daha küçük dilimleyerek daha az tahmin edin ve gecikme maliyetine göre sıralayın

Bazen doğru tahmin miktarı neredeyse hiçtir. **#NoEstimates** argümanı, makul çekirdeğinde şunu gözlemler: işi her biri bir iki gün süren küçük parçalara dilimlerseniz, tek bir parçanın tahmini önemini yitirir. Basitçe verimi sayar ve öngörüyü bu sayımdan yaparsınız. Dilimler düzgün ve küçük olduğunda ayrıntılı boyutlandırma israftır: öngörünün ihtiyaç duymadığı bir kesinliği üretmek için emek harcar. Bu, önceden düşünmeye karşı bir argüman değildir. Tek tek öngörüleri, tek tek parçaları küçük yaparak ucuzlatmanın argümanıdır.

Hâlâ karar gerektiren şey sıradır. Her şeyi aynı anda yapamadığınızda **gecikme maliyetine** göre sıralayın: belirli bir işin geciktiği her zaman birimi için kaybettiğiniz değer. Gelecek çeyrekte büyük bir sözleşmeyi açan bir özellik yüksek gecikme maliyetine sahiptir ve hiçbiri olmayan "olsa iyi olur" bir işin önüne geçmelidir, o iş daha kolay olsa bile. Gecikme maliyetini eforla tartmak (yalın düşünceden gelen "ağırlıklı en kısa iş önce" sezgisi), bir sonraki adımın ne olduğunu iç güdüyle sıralanmış bir birikimden çok daha güvenilir biçimde söyler. Bunun tüm konuşmayı yeniden çerçevelediğine dikkat edin: sahte kesinliği davet eden "her şey ne zaman bitecek" yerine, gerçekten cevaplayabileceğiniz "bitirilecek bir sonraki en değerli şey nedir" diye sorarsınız.

## Ödünleşimler: artılar ve eksiler

| Yaklaşım | Artılar | Eksiler |
|---|---|---|
| **Tek tarihli tahmin** | Basit; paydaşların istediği şey | Kesin biçimde yanlış; riski gizler; kazara bir taahhüde dönüşür |
| **Üç noktalı / PERT tahmini** | Belirsizliği açığa çıkarır; ucuz | Hâlâ bir tahmin; formül sahte bir titizlik izlenimi verir |
| **Hikaye puanları / tişört bedenleri** | Hızlı; sıralama ve kaba kapasite için iyi | Saat değil; hız matematiği tek tarihleri geri sokar |
| **Olasılıksal akış öngörüsü** | Kanıta dayalı; kendini günceller; dürüst aralıklar | Geçmiş ve kararlı akış gerektirir; daha az "kesin" görünür |
| **Referans sınıfı öngörüsü** | Büyük programlardaki iyimserliği düzeltir | Karşılaştırılabilir geçmiş çabalar gerektirir; duyması moral bozucu |
| **#NoEstimates (küçük dilimler)** | İsrafı kaldırır; sayarak öngörür | Disiplinli dilimleme gerektirir; bir sayı isteyen finansörleri rahatsız eder |

Merkezdeki gerilim, **insanların istediği kesinlik ile işin gerektirdiği dürüstlük** arasındadır. Finansörler, yöneticiler, sözleşmeler ve yasama organları kesin tek bir tarih ister, çünkü tek bir tarihin bütçelenmesi, vaat edilmesi ve savunulması kolaydır. Yazılım nadiren buna elverir. Gerilimi kesinlik uydurarak ya da cevap vermeyi reddederek değil, olasılığın para biriminde cevap vererek çözün: güven düzeyleri olan bir aralık, kanıt geldikçe yeniden öngörülür. Bunu küçük dilimlerle eşleştirin ki erken ve gerçek teslimatlar, uzak ve hayali olanların yerine insanların güvendiği şey olsun. Gösterilen bir artım, herhangi bir tahminden daha değerlidir.

## Takımınızla tartışılacak sorular

1. **Biri sizden bir tarih istediğinde bir tahmin mi, bir hedef mi, bir taahhüt mü veriyorsunuz ve odadaki herkes hangisi olduğunu biliyor mu?** Bu, en az çabayla en çok zararı önleyen sorudur. Çoğu kurumda bu üçü, takımın ağzından çıktığı anda tek bir sayıya çöker ve bir öngörünün söze dönüşmesi riskini kabul etmeye kimse karar vermemiştir. Gerçek bir örnek getirin: en son taahhüt ettiğiniz son tarihi alın, ilk söylendiği konuşmaya kadar geriye doğru izleyin ve takım elbise giymiş umutlu bir tahminden başka bir şey olup olmadığını sorun. Cevap dilinizi kalıcı olarak değiştirmelidir: tahminler aralık olarak çıkar, hedefler iş istekleri olarak adlandırılır ve taahhütler belirsizlik tartılarak ve bir karar olarak kaydedilerek (bölüm 1.5) bilinçli biçimde verilir. Takımınız bir taahhüdün bilinçli olarak nerede kabul edildiğini gösteremiyorsa, kazara söz veriyorsunuz demektir.

2. **Bir sonraki sürümünüzü taze tahminler yerine ölçülmüş verimden öngörebilir misiniz ve sizi ne engelliyor?** Çoğu takımın, "ne zaman biter" sorusuna deneysel olarak cevap verecek veri zaten var, işlerini izleyen araçta kullanılmadan duruyor. Takımınızın son çeyrek boyunca haftada kaç kalem tamamladığını biliyorsanız, bir bitiş tarihi dağılımı simüle edebilir ve bir dilek yerine bir olasılık söyleyebilirsiniz. Gerçek verim geçmişinizi ve kalan kalem sayınızı getirin ve akış tabanlı öngörüyü takımın sezgiyle tahmin ettiği tarihle karşılaştırın; aradaki fark genellikle öğreticidir. Engel, kalemlerinizin boyutlarının çok farklı olması ya da akışınızın düzensiz olmasıysa, bu başlı başına bulgudur, çünkü kararsız akış her halükarda düzeltmeye değer bir teslimat sorunudur (bölüm 11.2, 11.3). Tahminden ölçüme geçmek çoğu zaman bir araç değişikliğinden çok, kendi geçmişinize iyimserliğinizden daha fazla güvenme kararıdır.

3. **En büyük mevcut programınız için dış bakışı benimsediniz mi, yoksa yalnızca bir iç plan mı kurdunuz?** Büyük programlar, iyimserliğin pahalı aşımlara dönüştüğü ve kendinden emin alttan yukarı planın en çekici ve en az güvenilir olduğu yerlerdir. Disiplin şudur: kurumunuzun içinden ya da dışından benzer tamamlanmış çabalardan oluşan bir referans sınıfı adlandırın, gerçekte neye mal olduklarını ve gerçekte ne kadar sürdüklerini bulun ve kendi sayılarınızı savunmadan önce programınızı bu dağılımın içine dürüstçe yerleştirin. Veriyi getirin: buradaki karşılaştırılabilir girişimler ilk tahminlerini nasıl aştı ve mevcut planınız sessizce hepsini geçeceğinizi mi varsayıyor? Varsayıyorsa, istisnai olmaya bahis oynuyorsunuz demektir ve bu, temel oranların güvenilir biçimde kaybettirdiği bir bahistir. Dış bakış tahmininizi daha az gurur okşayıcı ve verdiğiniz sayıyı hatırlayacak finansörler ve denetçiler karşısında çok daha savunulabilir kılacaktır (bölüm 10.1).

4. **Bir finansör, bir sözleşme ya da bir yasa koyucu tek bir sabit tarih talep ettiğinde, ne yalan söyleyerek ne de reddederek nasıl cevap verirsiniz?** Baskının en sert olduğu ve dürüst takımların en sık pes ettiği yer burasıdır, çünkü "Eylül'e kadar yüzde 70 olasılıkla" ifadesi, bir rakibin kendinden emin "Eylül" demesinin yanında kaçamak gibi duyulur. Büyük bir kurum için bahisler katlanır: tek bir sabit tarih bütçelere, bağımlı programlara ve kamusal vaatlere yayılır; rahatlık için seçilmiş bir sayı, kaydığı anda sistemik bir yük haline gelir. Gerçekten kullanmayı planladığınız dili, güven düzeyleri olan bir aralığın uygulamalı örneğini ve kesin olarak taahhüt edebileceğiniz küçük bir erken artımı getirin; sonraki kapsamı finanse edilmiş bir aralık olarak bırakın. Rakip değerlendirme gerçektir, çünkü bazı son tarihler (düzenleyici bir geçiş, bir fuar lansmanı) gerçekten sabittir ve orada doğru hamle, eforun kesin olduğunu varsaymak yerine tarihi sabitleyip kapsamı esnetmektir. Kurumsal ve kamu ortamlarında bunu sözleşmenin biçimiyle ilişkilendirin: modüler, artım finansmanlı bir anlaşma değerli bir çekirdeğe dürüstçe taahhüt etmenizi sağlar; uzak bir kilometre taşına demirlenmiş tek bir sabit fiyatlı, sabit kapsamlı sözleşme ise aşıma ve manşete yol açan sahte kesinliği tam olarak zorlar.

5. **Takımınız bir sonraki neyi inşa edeceğine nasıl karar veriyor ve gecikme maliyetine göre açıkça sıralamak sırayı değiştirir mi?** Çoğu birikim, iç güdü, en yüksek sesle bağıran kişi ve kaba eforun bir karışımıyla sıralanır; bu da değerli olanlardan çok kolay kazanımlar için sessizce optimize eder. Bir işin geciktiği her zaman birimi için kaybettiğiniz değer olan gecikme maliyeti, soruyu "her şey ne zaman bitecek"ten, kanıtla gerçekten cevaplayabileceğiniz "bitirilecek bir sonraki en değerli şey nedir"e çevirir. Üç ya da dört gerçek birikim kalemini, her birinin açtığı değere ve bu değerin ne zaman sona erdiğine dair dürüst bir tahminle getirin, sonra bunları eforla karşılaştırarak haftalık kaybedilen değere göre sıralayın ve bu sırayı mevcut planınızla karşılaştırın; yeniden sıralama genellikle şaşırtıcıdır ve karşı çıkması zordur. Rakip değerlendirme, gecikme maliyetinin kendisinin de bir tahmin olması ve kendi kalemini öne almak isteyen biri tarafından oyuna getirilebilmesidir; bu yüzden sayıların kime ait olduğunu ve nasıl sorgulandığını belirleyin. Bir kurumsal portföy ya da bir kamu programı için bu disiplin, her biri kendi girişiminin önce gelmesi gerektiğine inanan paydaşlara sıralama kararlarını savunmanızı sağlar, çünkü sıra siyasete değil, ifade edilmiş değere dayanır.

6. **Kim yeniden öngörür, ne sıklıkla ve öngörü hareket ettiğinde harekete geçmekten kim sorumludur?** Başlangıçta bir kez yapılıp bir daha ele alınmayan bir öngörü süstür ve en pahalı kaymalar, canlı bir öngörünün son tarih onları inkâr edilemez kılmadan aylar önce göstereceği kaymalardır. Büyük bir takım için başarısızlık nadiren verinin yokluğudur ve çoğunlukla kalıcı bir ritmin ve adı konmuş bir sahibin yokluğudur: verim kayar, bitiş tarihi dağılımı sağa kayar ve fark etmek işi olan kimse bakmaz. Gerçek yeniden öngörü ritminizi (ya da hiç olmadığını kabul edin), bir öngörünün en son bir kararı ne zaman değiştirdiğini ve mevcut taahhüt belirlendiğinden beri gördüğünüz kaymayı getirin. Rakip değerlendirme öngörü yorgunluğudur, çünkü çok gürültülü yeniden öngörü çalkantıyı davet eder ve güveni aşındırır; bu yüzden her dalgalanmaya tepki vermek yerine makul bir aralık ve yükseltmeyi tetikleyen bir eşik üzerinde anlaşın. Kurumsal ve kamu bağlamlarında bunu denetimle ilişkilendirin: yönetişim organlarına güncellenmiş olasılık aralığını sabit bir takvimde sunun; böylece bir kayma, kilometre taşında ortaya çıkan bir sürpriz olarak değil, liderlerin harekete geçebileceği yönetilen bir yeniden öngörü olarak görünür.

## Sektör merceği

**Girişim.** Tahmin törenini neredeyse tamamen atlayın. İşi bir ila iki günlük parçalara dilimleyin, her hafta bitirdiklerinizi sayın ve kurucu ortaklara ve yatırımcılara kahramanca tek bir tarih yerine daralan bir aralık söyleyin. Geçmişiniz kısa ve süreciniz değişken, bu yüzden belirsizlik konisine bir mazeret olarak değil dürüst bir açıklama olarak yaslanın ve resim netleştikçe her Cuma yeniden öngörün.

**Küçük işletme.** Bir tahmin uzmanınız ve boyutlandırma toplantılarına iştahınız yok, o yüzden zaten kullandığınız araçların işi yapmasına izin verin: çoğu görev izleyici verimi bedavaya sunar ve bundan çıkan hafif bir öngörü, tahmin edilmiş bir son tarihten iyidir. Kadro sağlayamayacağınız ağır planlama yazılımı satın alma dürtüsüne direnin; tamamlanan kalemlerin basit bir haftalık sayımı ve sade bir aralık, müşterilere gerçekten verdiğiniz taahhütler için "ne zaman biter" sorusunu yeterince iyi cevaplar.

**Kurumsal.** Sorun, yıllık bir sermaye döngüsüne karşı bir portföyü finanse eden birçok takım arasında tutarlılıktır (bölüm 10.1). Tek tarihler yerine güven düzeyleri olan aralıklar üzerinde standartlaşın, büyük programlar için referans sınıfı karşılaştırmaları isteyin ve bir çeyrek içinde tahminlerin yerini verim tabanlı öngörülere bırakması için akış metriklerini kurun. Tahmini, tahmin, hedef ve taahhüdün net tanımlarıyla ortak bir pratik olarak yönetin; böylece bir bölümde üretilen sayı yönetim kuruluna ulaştığında aynı anlama gelsin.

**Kamu.** Satın alma kuralları ve kamusal hesap verebilirlik her şeyi şekillendirir. Kaçırılan bir kamusal tarih bir manşete ve bir denetim bulgusuna dönüşür; bu yüzden uzak bir kilometre taşına demirlenmiş tek bir sabit fiyatlı, sabit kapsamlı taahhüt yerine modüler, artım finansmanlı sözleşmeleri tercih edin. Denetim organlarına olasılıksal öngörüleri ve referans sınıfı kanıtlarını sade bir dille sunun, güven düzeylerini dürüstçe yayımlayın ve bir yüklenicinin iyimser bir plan üzerindeki imzası yerine, gösterilen çalışan artımların halkın ve denetçilerin güvendiği kanıt olmasına izin verin.

## Örnekler

**Girişim.** A Serisi demosuna hazırlanan dokuz kişilik bir girişim, kilit bir entegrasyonun hazır olup olmayacağını bilmek zorunda. Kurucuların yatırımcılara bir tarih vaat etmesine izin vermek yerine lider, tahmini bir aralık olarak söyler ve arkasındaki belirsizlik konisini açıklar. Takım haftada beş ila dokuz birikim kalemi kapatıyor; bu yüzden kalan iş üzerinde hızlı bir Monte Carlo öngörüsü çalıştırıp "çeyreğin üçüncü haftasına kadar yüzde 80 olasılıkla, bir hafta önce olma ihtimali yarı yarıya" diye bildirirler. Entegrasyonu iki günlük parçalara dilimlerler ki hiçbir tek tahmin çok önemli olmasın, yatırımcıya görünen yolu önce inşa etmek için gecikme maliyetine göre sıralarlar ve her Cuma yeniden öngörürler. Yatırımcılar, kayacak olan kendinden emin bir sayı yerine dürüst ve daralan bir projeksiyon alır.

**Kurumsal.** Sipariş yönetimi platformunu değiştiren bir perakendeci, programı bir sayı talep eden yıllık sermaye döngüsü üzerinden finanse etmek zorundadır. Program ofisi derli toplu alttan yukarı planı savunma dürtüsüne direnir ve bunun yerine ikisi şirket içi, biri kamuya belgelenmiş üç karşılaştırılabilir platform değişiminden bir referans sınıfı oluşturur; bunlar başlangıç tahminlerini yüzde 50 ile 80 arasında aşmıştır. Dış bakış rakamına karşı finanse ederler, takvimi sabit bir canlıya geçiş yerine olasılık aralığı olarak ifade ederler ve ilk teslim eden takımdan akış metriklerini kurarlar; böylece bir çeyrek içinde tahmin, aylık güncellenen verim tabanlı bir öngörüyle değişir. Bir iş akışı aşırı ısındığında yeniden öngörü bunu erkenden gösterir ve liderlik kaymayı son tarihte keşfetmek yerine dengeyi yeniden kurar.

**Kamu.** Bir yardım sistemini modernize eden bir kurum, kaçırılan kamusal bir tarihin manşet olduğu ödenekler ve kamu denetimi altında çalışır. Tek bir uzak kilometre taşına demirlenmiş tek bir sabit fiyatlı, sabit kapsamlı sözleşme yerine modüler artımları satın alır ve erken teslim edilen değerli bir çekirdeği kamuoyuna taahhüt eder; sonraki kapsam söz olarak değil, finanse edilmiş bir aralık olarak ifade edilir. Program liderleri denetim organlarına olasılıksal öngörüler ve referans sınıfı karşılaştırmalarıyla bilgi verir ve güven düzeylerini sade bir dille açıklar; böylece "Eylül'e kadar yüzde 70" tam da bu olarak anlaşılır. Gösterilen çalışan artımlar, bir yüklenicinin imzalayabileceği herhangi bir tahminden daha sağlam olan, halkın güvendiği kanıt olur.

## İş gerekçesi: motivasyonlar, YG ve TSM

Dürüst tahmin ve öngörünün getirisine felaketten kaçınma hakimdir. Büyük yazılım çabaları, özgün sabit bir planı tutturmaktan çok daha sık aşar ya da başarısız olur ve kayıplar birikir: batık maliyet, geç teslimattan vazgeçilen değer, toparlanmak için acil harcama ve bozulan bir kamusal taahhüdün ardından gelen güven kaybı. Buradaki pratikler (tahmini taahhütten ayırmak, gerçek verimden öngörmek, büyük programlarda dış bakışı benimsemek) bir programı o başarısızlık eğrisinden uzaklaştıranlardır. Daha isabetli bir kristal küre satın almıyorsunuz. Nerede durduğunuza dair daha erken ve daha doğru bilgi satın alıyorsunuz; bu da düzeltme hâlâ ucuzken düzeltmenize olanak tanır.

Toplam sahip olma maliyeti açısından, tahmin töreninden ölçülmüş öngörüye geçiş genellikle maliyeti artırmaz, düşürür. Ayrıntılı baştan tahmin üretmesi pahalıdır ve iş başlar başlamaz çürür; verim tabanlı bir öngörü ise teslimat hattınız veriyi yayınladığında neredeyse bedavadır. Her iki uç da para kaybettirir: aşırı tahmin (kimsenin kullanmadığı kesinlik üreten bitmeyen boyutlandırma toplantıları) ve yetersiz öngörü (körlemesine taahhüt edip aşımı sonradan ödemek). Liderliğe gerekçeyi sunmak için, son büyük aşımınızın tam yüklenmiş maliyetini, verimi izlemenin ve aralıklar söylemenin sıfıra yakın maliyetinin yanına koyun ve bir dış bakış öngörüsünün en baştan nasıl finanse edilebilir bir beklenti belirleyeceğini gösterin.

## Anti-kalıplar ve tuzaklar

- **Tek tarihli taahhütler:** tek bir sayıya çökertilmiş ve kanıtın ötesinde savunulan bir aralık.
- **Tahmin aklama:** umutlu bir tahminin zincirde yukarı taşınıp sözleşmesel bir söze dönüşene kadar sertleşmesi.
- **Hızı takvim motoru yapmak:** kesin bir tarih üretmek için hikaye puanlarını hızla çarpmak.
- **Sezgiyle pay eklemek:** ilkinin üzerine konmuş, baskı altında pazarlıkta giden ikinci bir tahmin.
- **Yalnızca iç bakış:** benzer programların gerçekte ne kadar sürdüğünü görmezden gelip taze bir alttan yukarı plana güvenmek.
- **Her şeyi tahmin etmek:** tek tek tahminleri hiçbir kararı değiştirmeyen küçük, düzgün dilimleri boyutlandırmak.
- **Donmuş öngörüler:** başlangıçta bir kez yapılıp gerçeklik ortaya çıktıkça güncellenmeyen bir öngörü.
- **Kesinlik tiyatrosu:** belirsizlik konisinin geniş ağzında saatleri iki ondalık basamakla söylemek.

## Olgunluk modeli

- **Düzey 1, Başlangıç:** Tahminler iç güdüyle üretilmiş ve söz gibi görülen tek tarihlerdir; tahmin, hedef ve taahhüt arasında ayrım yoktur; öngörü tepkisel ve plansızdır; aşımlar herkesi şaşırtır ve suç takıma atılır.
- **Düzey 2, Geliştirme:** Bazı yapılandırılmış tahmin vardır (ayrıştırma, hikaye puanları, üç noktalı rakamlar), ama pratik takımdan takıma değişir; tahminler hâlâ çoğunlukla tek sayılardır; tarihleri öngörmek için hız kullanılır; öngörüler başlangıçta bir kez yapılır ve nadiren yeniden ele alınır.
- **Düzey 3, Standartlaştırma:** Kurum genelinde uygulanan belgelenmiş bir standart vardır: tahminler belirtilmiş belirsizlikle aralıklar olarak ifade edilir, tahmin, hedef ve taahhüt tanım gereği ayrı tutulur, takımlar verimi izler ve belirli bir ritimle yeniden öngörür, büyük programların referans sınıfı karşılaştırmaları kullanması zorunludur.
- **Düzey 4, Yönetme:** Pratik veriyle ölçülür ve kontrol edilir. Öngörü doğruluğu gerçek sonuçlara karşı izlenir ve kalibrasyon denetlenir; böylece "yüzde 80 olasılıkla şu tarihe kadar" dediğiniz tarihlerin gerçekten on kezde sekizinde tutup tutmadığını söyleyebilirsiniz; verim ve çevrim süresi taban çizgileri korunur; gecikme maliyeti nicelleştirilir; öngörü kayması eşiklere karşı izlenir ve yükseltmeyi tetikler; taahhütler iyimserliğe karşı değil kanıta karşı verilir.
- **Düzey 5, Orkestrasyon:** Akış verisinden olasılıksal öngörü süreklidir ve kalibrasyon geçmişi dürüstlüğünü kanıtladığı için güvenilirdir; taahhütler güveni maliyetle tartan bilinçli kararlardır; iş, tahminin asgariye indiği kadar küçük dilimlenir ve sırayı gecikme maliyeti belirler; tahmin portföy finansmanı ve risk planlamasıyla bütünleşir ve kurum, öngörüler hareket ettikçe düzenli olarak kapsamı yeniden belirler ve dengeyi yeniden kurar; planı özgün sayıyı savunmak yerine kanıta uyarlar.

## Tartışma fikirleri

1. Her tahminin güven düzeyi olan bir aralık olarak takımdan çıkması zorunlu olsaydı ve tek tarihler yasak olsaydı, kurumunuzda ne değişirdi?
2. Sayarak öngörülebilecek kadar küçük ve düzgün olan işleri tahmin etmek için nerede efor harcıyorsunuz?
3. Son iki çeyreğin verimini bir Monte Carlo simülasyonuna verseydiniz, öngörü gerçekte taahhüt ettiğiniz tarihlerle uyuşur muydu?
4. En büyük programınız için dürüst referans sınıfı nedir ve temel oran mevcut planınızla ne kadar çelişiyor?
5. Takımınız bugün sırayı nasıl belirliyor ve gecikme maliyetine göre açıkça sıralamak bir sonraki neyi inşa edeceğinizi değiştirir mi?
6. Kurumunuzda bir taahhüt kabul edildiğinde belirsizlik kararın bir parçası olarak kaydediliyor mu, yoksa tarih yazıldığı anda ortadan mı kayboluyor?

## Önemli çıkarımlar

- **Tahmini, hedefi ve taahhüdü** ayrı tutun; bunları çökertmek projelerin kendilerine yalan söylemeye başlamasının yoludur.
- Tahminler bilinen yönlerde sistematik olarak yanlıştır: **belirsizlik konisi** erken işi genişletir ve **planlama safsatası** iyimserliği varsayılan yapar.
- Taze tahminler yerine **ölçülmüş verimden olasılıksal öngörüyü** tercih edin; aralıklar ve güven düzeyleri söyleyin ve sürekli yeniden öngörün.
- İyimserliğin en pahalı olduğu büyük programlarda referans sınıfı öngörüsüyle **dış bakışı** benimseyin (bölüm 10.1).
- Tek tek tahminler önemini yitirsin diye **küçük dilimleyin** ve iç güdü yerine **gecikme maliyetine göre sıralayın**.
- Yalnızca bir kararı değiştiriyorsa tahmin edin; aksi halde israftır. Bkz. bölümler 10.6 (proje yönetimi), 11.2 (teslimat), 11.3 (kuyruk kuramı) ve 1.5 (karar verme ve yönetişim).

## Kaynaklar ve ileri okuma

- Steve McConnell, *Software Estimation: Demystifying the Black Art*.
- Daniel Vacanti, *Actionable Agile Metrics for Predictability* and *When Will It Be Done?* (probabilistic forecasting from flow data).
- Troy Magennis, *Forecasting and Simulating Software Development Projects* (Monte Carlo methods).
- Bent Flyvbjerg and Dan Gardner, *How Big Things Get Done* (reference class forecasting and megaprojects).
- Daniel Kahneman, *Thinking, Fast and Slow* (the planning fallacy and the outside view).
- Donald Reinertsen, *The Principles of Product Development Flow* (cost of delay and queue economics).
- Vasco Duarte, *NoEstimates: How to Measure Project Progress Without Estimating*.
- Frederick Brooks, *The Mythical Man-Month* (why software schedules go wrong).
- Todd Little, "Schedule Estimation and Uncertainty Surrounding the Cone of Uncertainty" (*IEEE Software*, 2006).
