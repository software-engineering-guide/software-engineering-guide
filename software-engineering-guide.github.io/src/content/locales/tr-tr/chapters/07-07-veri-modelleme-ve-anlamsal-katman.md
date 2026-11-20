# 7.7 Veri modelleme ve anlamsal katman

## Genel bakış ve motivasyon

[Veri modeli](https://en.wikipedia.org/wiki/Data_model), verinizin ne anlama geldiğine dair, verinin nerede yaşayacağına karar vermeden önce verilen bir karardır. İşinizin önemsediği şeyleri, onları tanımlayan öznitelikleri ve aralarındaki ilişkileri adlandırır. Depolama, dizinler, dosya biçimleri ve sorgu motorlarının hepsi daha sonra gelir. Bu sıralama önemlidir, çünkü verinizin anlamı, onu tutmak için kullandığınız her teknolojiden uzun yaşar. Ambarlar değiştirilir, tablo biçimleri değişir ve sorgu motorları gelip geçer, ama "müşteri", "sipariş" ve "etkin kullanıcı" hepsinde yıllarca aynı anlama gelmelidir.

Küçük bir takım için modelleme çoğu zaman örtüktür. Bir mühendis bütün şemayı kafasında tutar ve "gelir"in ortak anlaşılması, anlaşmazlığa düşecek yalnızca üç kişi olduğu için sürer. Büyük geliştirici kuruluşlarının, kurumların ve kamu kurumlarının ölçeğinde bu gayriresmîlik, bölüm 7.1'de (veri stratejisi ve yönetişimi) anlatılan şekilde çöker. Düzinelerce takım yüzlerce tablo kurar; her birinin "oturum"un ne olduğu ya da bir kullanıcının ne zaman "etkin" sayıldığı konusunda kendi fikri vardır. İki pano aynı hafta için iki farklı sayı gösterir ve bir liderlik toplantısı, sonraki adımın ne olacağı yerine kimin sorgusunun doğru olduğu üzerine bir tartışmaya dönüşür. Kötü modelleme kendini duyurmaz. Aylar sonra uzlaştırma işi, başarısız denetimler ve kimsenin savunamadığı rakamlar üzerine verilmiş kararlar olarak ortaya çıkar.

Bu bölüm o işi bilinçli yapmakla ilgilidir. Kavramsal, mantıksal ve fiziksel modelleri; varlık-ilişki modellemesini; ne zaman normalleştirip ne zaman denormalleştireceğinizi; modellemenin işlemsel ve analitik iş yükleri için nasıl farklılaştığını; olgular ve boyutlarla boyutsal modellemeyi; ve her iş metriğinin tek yönetilen tanımını tutan anlamsal katmanı ele alır. Getirisi kendi başına bir zarafet değildir. "Etkin kullanıcı" ve "gelir"in her yerde tek bir anlama gelmesidir; böylece takımlarınız sayılara güvenebilir ve bu sayede daha hızlı hareket edebilir.

*Ayrıca bakınız:* bölüm 3.4 (veri mimarisi ve depolama), bölüm 7.3 (analitik ve iş zekâsı) ve bölüm 11.5 (kilit performans göstergeleri).

## Temel ilkeler

- Verinin nerede yaşayacağına karar vermeden önce ne anlama geldiğine karar verin.
- Üç düzeyde modelleyin: kavramsal (iş), mantıksal (yapı), fiziksel (uygulama).
- İşlemsel sistemlerde doğruluğu korumak için normalleştirin; analitik hız için bilinçli denormalleştirin.
- Modeli iş yüküyle eşleştirin: işlemler ve analitik zıt ihtiyaçlara sahiptir.
- Her iş metriğinin tam olarak bir yönetilen tanımı vardır ve o anlamsal katmanda yaşar.
- Uyumlu boyutlar, bağımsız takımların veriyi güvenle birleştirmesine ve karşılaştırmasına olanak verir.
- Tanecik, bir sorgunun kazası değil, bilerek verdiğiniz bir tasarım kararıdır.
- Modeller yaşayan varlıklardır: onları iyi adlandırın, belgeleyin ve evrilebilir tutun.

## Öneriler

### Üç düzeyde, sırayla modelleyin

Anlamdan dışarıya doğru çalışın. Kavramsal bir modelle başlayın: işinizin önemsediği varlıklar ve nasıl ilişkili oldukları, bir alan uzmanının kontrol edebileceği sade bir dilde yazılmış. "Bir müşteri birçok sipariş verir; bir sipariş birçok sipariş kalemi içerir; her sipariş kalemi bir ürüne atıfta bulunur." Henüz anahtar yok, tür yok, tablo yok. Sonra yapı ekleyen mantıksal bir model kurun: öznitelikler, birincil ve yabancı anahtarlar, bire-çok ilişkileri ve kısıtlar; hâlâ belirli bir veritabanından bağımsız. [Varlık-ilişki modellemesi](https://en.wikipedia.org/wiki/Entity%E2%80%93relationship_model) buradaki standart gösterimdir ve bir varlık-ilişki diyagramı hem mühendisler hem iş paydaşlarıyla birlikte gözden geçirdiğiniz üründür. Fiziksel modeli ancak o zaman üretin: seçtiğiniz motor için gerçek tablolar, sütunlar, veri türleri, dizinler, bölümler ve depolama düzeni. Doğrudan fiziksel tasarıma atlamak en yaygın modelleme hatasıdır, çünkü bugünün teknoloji seçimlerini onlardan uzun yaşaması gereken kararlara gömer.

### İşlemsel sistemleri normalleştirin, analitik olanları bilerek denormalleştirin

İşlemleri kaydeden sistemler için [veritabanı normalleştirmesini](https://en.wikipedia.org/wiki/Database_normalization) tercih edin. Normal formlar fazlalığı kaldırır; böylece her olgu bir kez saklanır, bu da güncelleme anomalilerini önler ve birçok kullanıcı veriyi eşzamanlı değiştirdiğinde yazmaları doğru tutar. Bu, eşzamanlı yazmalar altında doğruluğun herhangi bir tek analitik sorgunun hızından daha önemli olduğu [çevrimiçi işlem işleme](https://en.wikipedia.org/wiki/Online_transaction_processing) (OLTP) için doğru varsayılandır. Analitik sistemlerin öncelikleri zıttır. Okuma ağırlıklıdırlar, çok büyük aralıkları tarar ve toplulaştırırlar ve sorgu anında düzinelerce normalleştirilmiş tabloyu birleştirmek yavaş ve üzerinde akıl yürütmesi zordur. Orada sorgular daha basit ve hızlı olsun diye ilişkili öznitelikleri bir araya getirerek bilerek denormalleştirirsiniz. Disiplin, fazlalığın kazara sızmasına izin vermek yerine belgelenmiş bir nedenle, bilinçli denormalleştirmektir. Bölüm 3.4 (veri mimarisi ve depolama), her kalıbı performanslı kılan motorları ele alır.

### Analitik için boyutsal modelleme kullanın

Analitik iş yükleri için Ralph Kimball'ın yaygınlaştırdığı yaklaşım olan [boyutsal modellemeyi](https://en.wikipedia.org/wiki/Dimensional_modeling) benimseyin. Dünyayı olgulara ve boyutlara bölersiniz. Bir olgu tablosu bir iş sürecinin ölçümlerini tutar: bir satışın tutarı, bir çağrının süresi, sevk edilen miktar. Boyut tabloları, filtrelediğiniz ve gruplandırdığınız betimleyici bağlamı tutar: müşteri, ürün, mağaza, tarih. Bir olgu tablosunu boyutlarıyla çevrelerseniz bir [yıldız şeması](https://en.wikipedia.org/wiki/Star_schema) elde edersiniz; analistlerin anlaması kolay, motorların sorgulaması hızlıdır. O boyutları alt tablolara normalleştirirseniz bir kar tanesi şeması elde edersiniz; bu biraz depolama tasarrufu sağlar ama daha fazla birleştirme ve karmaşıklık pahasınadır; somut bir nedeniniz yoksa yıldızı tercih edin. Denetlenebilirliğin ve kaynak izlemenin baskın olduğu çok büyük, yüksek düzeyde düzenlenmiş ortamlarda bir veri kasası (data vault) yaklaşımı, geçmişi ve soyağacını agresif biçimde yakalamak için merkezleri, bağlantıları ve uyduları modeller; bedeli daha fazla tablo ve daha dik bir öğrenme eğrisidir. Çoğu takım Kimball tarzı yıldızlarla başlamalı ve veri kasasına yalnızca denetim gereksinimleri haklı çıkardığında başvurmalıdır.

### Taneciği sabitleyin ve değişen boyutları açıkça ele alın

Bir olgu tablosuna tek bir sütun eklemeden önce taneciğini belirtin: bir satırın tam olarak neyi temsil ettiği. "Sipariş kalemi başına bir satır." "Kullanıcı başına gün başına bir satır." Tanecik doğru bir modelin temelidir, çünkü her ölçü ve her boyut ya o taneciğe uyar ya da tabloya ait değildir. Tanecikleri karıştırmak çift sayılan gelirin nasıl ortaya çıktığıdır. Sonra boyutların zaman içinde nasıl değiştiğine karar verin. Bir müşteri yeni bir şehre taşınır; eski değeri üzerine mi yazarsınız, tam bir geçmiş mi tutarsınız, yoksa yalnızca güncel ve önceki değeri mi izlersiniz? Bunlar standart [yavaş değişen boyut](https://en.wikipedia.org/wiki/Slowly_changing_dimension) kalıplarıdır ve yanlış seçmek, geçmiş raporlarınızın geçmişi sessizce yeniden yazması demektir. Taneciğe ve değişim stratejisine baştan karar verin, bunları modelin belgelerine yazın ve incelemede çizgiyi koruyun.

### Her metriğin tek tanımı olarak tek bir anlamsal katman kurun

Bölümün tamamının karşılığını veren öneri budur. Bir [anlamsal katman](https://en.wikipedia.org/wiki/Semantic_layer), fiziksel tablolarınız ile onları tüketen her araç arasında durur ve her iş metriğinin tek yönetilen tanımını tutar. "Etkin kullanıcı" bir kez, kod olarak, kesin mantığıyla tanımlanır: hangi olaylar sayılır, hangi pencerede, hangi iç hesaplar hariç. "Gelir" bir kez tanımlanır; iadelerin, indirimlerin ve para birimi dönüşümünün nasıl ele alındığı dahil. Her pano, defter, rapor ve ters-ETL işi, onu özel bir sorguda yeniden uygulamak yerine o tanımı okur. Tanım değiştiğinde tek yerde değişir ve her tüketici birlikte güncellenir. Yönetilen metrik tanımlarını beyan olmaktan çıkarıp gerçek kılan mekanizma budur ve bölüm 11.5'in (kilit performans göstergeleri) istediğinin doğrudan uygulanmasıdır. Metrik tanımlarını, bölüm 7.1'in verinin bir ürün olarak ele alınmasını istediği gibi, sahipleri, incelemesi ve testleri olan sürümlenmiş kod olarak ele alın.

### Kurallar, adlandırma ve belgelendirme oluşturun

Tutarlılık bir özelliktir. Adlandırma kurallarını benimseyin ve uygulayın: tablo adları için bir kural, anahtarlar için bir kural, tarih sütunları için bir standart, bir olguyu bir boyuttan ayırt işaretlemek için bir kural. Varlık adlarında tekil mi çoğul mu kullanacağınıza bir kez karar verin ve asla karıştırmayın. Her modeli onu kullananların bakacağı yerde belgeleyin: her tablonun anlamı, her olgunun taneciği, her metriğin tanımı ve her birinin sahibi. İyi adlandırma ve belgelendirme, yeni bir analistin takımı bölmek yerine kendi kendine hizmet almasını sağlayan şeydir ve bir denetçinin bir yönetim kurulu sunumundaki bir sayıyı rehberli tur olmadan kaynağına kadar izlemesini sağlayan şeydir.

### Modelleri evrilebilir tutun

Modeliniz değişecek, bu yüzden değişime göre tasarlayın. Mevcut sütunların amacını değiştirmek yerine sütun ekleyin. Bir kaynak sistemin doğal anahtarındaki değişimin ambarınız boyunca yayılmaması için vekil anahtarlar kullanın. Metrik tanımlarını çalışan panoların altında sessizce değiştirmek yerine sürümleyin ve bildirimle kullanımdan kaldırın. Dönüşümleri sürüm kontrolünde, test edilmiş ve gözden geçirilmiş tutun; böylece "etkin kullanıcı"nın anlamındaki bir değişiklik, bir BI aracındaki sessiz bir düzenleme değil, bir farkı ve bir onaylayanı olan bir çekme isteğidir. Güvenle evrilemeyen bir model, insanların etrafından dolaştığı bir model olur ve gölge tanımlar tek doğruluk kaynağının nasıl öldüğüdür.

## Ödünleşimler: artılar ve eksiler

| Yaklaşım | Artılar | Eksiler | En uygun |
|---|---|---|---|
| Normalleştirilmiş (3NF) | Doğru yazmalar, fazlalık yok, esnek | Yavaş analitik birleştirmeler, karmaşık sorgular | OLTP ve operasyonel sistemler |
| Yıldız şeması (Kimball) | Hızlı, sezgisel, analist dostu | Bir miktar fazlalık, bakımı yapılacak ETL | Çoğu analitik ve BI |
| Kar tanesi şeması | Daha az depolama, daha temiz boyutlar | Daha fazla birleştirme, daha fazla karmaşıklık | Büyük, sıkı yönetilen boyutlar |
| Veri kasası | Tam geçmiş, denetlenebilir, çevik yüklemeler | Çok sayıda tablo, dik öğrenme eğrisi | Yüksek düzeyde düzenlenmiş, denetim ağırlıklı |
| Modellerin üzerinde anlamsal katman | Her yerde tek tanım, araçtan bağımsız | Baştan kurulum, sahiplik gerektirir | Çok takımlı, çok araçlı kuruluşlar |

Merkezi gerilim, tek bir sorgunun hızı ile bütün mülk genelinde doğruluk ve esneklik arasındadır. Normalleştirme doğruluğu korur ve bedelini sorgu karmaşıklığıyla öder; boyutsal modeller sorgu hızı ve netliği satın alır ve bedelini ETL ve bir miktar yönetilen fazlalıkla öder. Evrensel bir kazanan yoktur, bu yüzden bir favori seçmek yerine modeli iş yüküyle eşleştirirsiniz. Anlamsal katman, çok sayıda takım ile çok sayıda araç arasındaki ikinci gerilimi, metrik tanımını bunların herhangi birinden bağımsız kılarak çözer. Hata, bunları ideolojik kamplar olarak görmektir. Sağlıklı bir kuruluş normalleştirilmiş OLTP sistemlerini, onlardan beslenen boyutsal analitik modelleri ve üstte tek bir anlamsal katmanı çalıştırır; her biri iyi olduğu işi yapar.

## Takımınızla tartışılacak sorular

1. **İki pano aynı metrik için farklı sayılar gösterdiğinde kimin tanımı kazanıyor ve o tanım fiziksel olarak nerede yaşıyor?** Bu soru, gerçekten tek bir doğruluk kaynağınız olup olmadığını mı yoksa yalnızca olduğuna mı inandığınızı ortaya çıkarır. Çoğu büyük takımda dürüst yanıt, "etkin kullanıcı"nın bir düzine farklı sorguda yeniden tanımlandığı ve kazananın toplantıda en yüksek sesle tartışan olduğudur. Gerçek kanıt getirin: bir metrik seçin, hesaplandığı her yeri bulun ve mantığı satır satır karşılaştırın. Neredeyse kesinlikle pencereler, dışlamalar ve uç durumlar konusunda sessiz anlaşmazlıklar bulacaksınız. Yanıt, her metriğin bir kez, gözden geçirilmiş kod olarak tanımlandığı bir anlamsal katman kurma kararını yönlendirmelidir; böylece soru insanlarla ilgili olmaktan çıkar ve sürümlenmiş bir ürünle ilgili olur. O tanımın tek bir fiziksel evi olana kadar her uzlaştırma geçicidir.

2. **En önemli olgu tablonuzun taneciği nedir ve odadaki herkes bunu aynı şekilde söyleyebiliyor mu?** Tanecik, çoğu modelleme başarısızlığının izinin sürüldüğü sessiz temeldir. Takımın yarısı "sipariş başına bir satır", diğer yarısı "kalem başına bir satır" diyorsa, bir gelir raporunda ortaya çıkmayı bekleyen bir çift sayım hatanız var demektir. Gerçek tabloyu getirin ve herkesten bir satırı tek cümleyle anlatmasını isteyin. Buradaki anlaşmazlık yumuşatılacak bir iletişim sorunu değildir; üzerine daha fazla ölçü yığılmadan önce düzeltilecek bir tasarım kusurudur. Yanıt modelin belgelerine yazılmalı ve incelemede uygulanmalıdır, çünkü analistler belirsiz bir tanecik üzerine sorgu kurdukları anda belirsizlik, düzeltebileceğinizden hızlı yayılır.

3. **Bu model değişimi nasıl özümseyecek ve bir tanım kaydığında geçen yılın raporlarına ne olacak?** Her model değişen kaynak sistemlerle, değişen iş kurallarıyla ve değişen metrik tanımlarıyla karşılaşır; bu yüzden asıl soru, değişimin kontrollü bir çekme isteği mi yoksa geçmişi yeniden yazan sessiz bir düzenleme mi olduğudur. Yakın tarihli bir örnek getirin: tanımı değişen bir metrik ya da adı değişen bir kaynak anahtar ve mevcut panolara ne olduğunu izleyin. Yavaş değişen bir boyut üzerine yazarak ele alındıysa, geçmiş raporlarınız geçmiş değerlerini sessizce değiştirmiş olabilir; bu, eğilim çözümlemesi ya da düzenlenmiş raporlama yapan herkes için ciddi bir sorundur. Yanıt sizi vekil anahtarlara, sürümlenmiş metrik tanımlarına, açık değişim stratejilerine ve incelemeyle sürüm kontrolünde tutulan dönüşümlere itmelidir. Kimsenin güvenle değiştiremediği bir model, insanların terk ettiği bir model olur.

4. **Hangi boyutlar her takımda aynı anlama gelmeli ve her birinin sahipliğinden kim sorumlu?** Uyumlu boyutlar, pazarlama, finans ve operasyonun verilerini birleştirmesini ve karşılaştırılabilir yanıtlar almasını sağlayan şeydir; ancak bu yalnızca "müşteri", "ürün", "bölge" ve "tarih" takım başına özel bir kopya yerine tek bir üzerinde anlaşılmış tanım taşıdığında olur. Karşıt çekim özerkliktir: her takım kendi dünyasını kendi hızında modellemek ister ve ortak bir boyutu zorlamak kısa vadede onları yavaşlatırken mülk genelinde karşılığını verir. En çok takımlar arası raporda görünen iki ya da üç boyutu getirin, her birinin bugün var olan her sürümünü listeleyin ve anahtarlarının ve özniteliklerinin gerçekte ne kadar ayrıştığına bakın. Her uyumlu boyut için bir sahip adlandırın, çünkü sahipsiz ortak bir boyut bir çeyrek içinde özel kopyalara geri kayar. Bir bölümden gelen bir rakamın kamuya açık biçimde bir başkasıyla karşılaştırıldığı kurumsal ve kamu ortamlarında, uyumsuz bir boyut dürüst bir karşılaştırma ile kazara bir yanlışlık arasındaki farktır; bu yüzden hangi boyutların merkezi olarak yönetildiğine ve hangilerinin yerel kaldığına erken karar verin.

5. **Normalleştirilmiş işlemsel sistemleriniz ile denormalleştirilmiş analitik modelleriniz arasındaki sınır nerede ve her denormalleştirme bilinçli bir karar mı?** Modeli iş yüküyle eşleştirmek çekirdek disiplindir, ama sınır tam olarak bulanıklaştığı yerdir: bir analist hız için bir ambar tablosunu denormalleştirir, bir mühendis alışkanlıktan bir raporlama tablosunu normalleştirir ve kimse her seçimin hangi tarafa ait olduğunu yazmaz. Gerilim, tek bir sorgunun hızı ile her şey genelinde doğruluk ve esneklik arasındadır ve makul insanlar yazmaları mı okumaları mı sahiplendiklerine bağlı olarak farklı sonuçlara varır. En yavaş analitik sorgunuzu ve en çekişmeli işlemsel tablonuzu getirin ve her fazlalık sütun için fazlalığın belgelenmiş bir nedenle mi seçildiğini yoksa kazara mı sızdığını sorun. Amaç, denormalleştirmeye ne zaman izin verildiğine ve kimin onayladığına dair yazılı bir kuraldır, bir saflık yarışması değil. Büyük ya da düzenlenmiş kuruluşlarda bu sınır aynı zamanda kişisel verinin nerede çoğaltıldığını da belirler; bu yüzden belgelenmemiş bir denormalleştirme hem bir performans sorusu hem de birinin eninde sonunda bir denetçiye açıklamak zorunda kalacağı bir veri yönetişimi maruziyetidir.

6. **Anlamsal katmanı kurmalı mısınız yoksa satın mı almalısınız ve var olduktan sonra her metrik tanımını güncel tutmaktan kim sorumlu?** Bir anlamsal katman yalnızca sahiplenildiğinde ve bakımı yapıldığında tek doğruluk kaynağı sağlar; bu yüzden araç seçimi, "gelir"in anlamındaki bir değişikliği kimin incelediği ve bir tanım bayatladığında kimin sorumlu olduğu sorusunun yanıtından daha az önemlidir. Karşıt hususlar gerçektir: kurmak size denetim verir ve yığınınıza uyar ama mühendislik yükü ekler; bir metrik aracı satın almak daha hızlıdır ama kilitlenme ve tam denetleyemediğiniz bir tanım dili riski taşır. En yüksek riskli birkaç metriğinizi, onları bugün tüketen araçları ve bu tanımlara şu anda sahip olan biri olup olmadığına ya da onların yalnızca var olup olmadığına dair dürüst bir okumayı getirin. Tanımların adlandırılmış sahipler ve testlerle sürümlenmiş kod olarak mı yaşayacağına baştan karar verin, çünkü kimsenin bakmadığı bir anlamsal katman, yerine geçmesi gereken dağınık tanımlara çürür. Kamuya açık bir panodaki bir metriğin belgelenmiş, gözden geçirilmiş bir tanıma izlenebilir olması gereken kurumsal ve kamu raporlamasında, bu sahiplik ve bir sayının soyağacını kanıtlayabilme yeteneği, anlamsal katmanı bir kolaylıktan denetlenebilir bir kontrole dönüştüren şeydir.

## Sektör merceği

**Girişim.** Modelleme bekleyebilir, ama tanımlar bekleyemez. İki mühendisle ve bir ambar kurmaya pisti olmadan, dönüştürme aracınıza küçük bir anlamsal katman koyun ve yönetim kurulunuzun gerçekten izlediği iki ya da üç metriği, "etkin kullanıcı" ve "gelir"i, bir kez, test edilmiş kod olarak tanımlayın. Veri kasasını ve ayrıntılı boyutsal şemaları atlayın; ince bir yıldız ve bir avuç yönetilen tanım, teslimatı yavaşlatmadan tutarlı sayılar satın alır. Getirisi, yönetim kurulu hazırlığının kimin sorgusunun doğru olduğu üzerine bir tartışma olmaktan çıkmasıdır.

**Küçük işletme.** Veri modelleyiciniz ve bir metrik platformu için bütçeniz yok, bu yüzden zaten kullandığınız araçlara yerleşik tanımlara yaslanın ve önemli olan azını herkesin okuduğu tek bir paylaşılan belgeye yazın. Kadrolayamayacağınız bir ambar kurmak yerine mevcut yazılımınıza gömülü analitiği satın almayı tercih edin. Modellediğiniz yerde basit tutun ve şeyleri tutarlı adlandırın, çünkü gelecek yıl bakımı yapan kişi, "müşteri"nin neden iki anlama geldiğini hatırlayamayan kişi olabilir. Tutarlılık uzlaştırmadan ucuzdur.

**Kurumsal.** Sorun, birçok takımın ve birçok aracın özel tanımlara sürüklenmesidir; bu yüzden uyumlu boyutlara, tek yönetilen bir anlamsal katmana ve sahipleri ve incelemesi olan sürümlenmiş kod olarak tutulan metrik tanımlarına yatırım yapın. Bir araçtaki sayının başka bir araçtaki aynı sayıyla eşleşmesi için adlandırmayı, tanecik beyanlarını ve yavaş değişen boyut stratejilerini mülk genelinde standartlaştırın. Anlamsal katmanı bir yol haritası ve sahip bir takımı olan bir ürün olarak ele alın ve ne kadar uzlaştırma süresini ortadan kaldırdığını ölçün. Getiri, iş genelinde güvenilen sayılar ve bir yönetim kurulu sunumundan kaynağa temiz biçimde izlenen denetimlerdir.

**Kamu.** Şeffaflık ve kurumlar arası karşılaştırılabilirlik işi şekillendirir: coğrafya ve demografi için kanonik referans veri, çekirdek göstergelerin yönetilen tanımları ve halkın herhangi bir rakamı belgelenmiş bir tanıma izleyebilmesi için sürümlü yayınlarla yayımlanmış metodoloji. Satın alma kuralları modellerinizin ve tanımlarınızın taşınabilir ve tedarikçiden bağımsız kalmasını gerektirebilir; bu yüzden tek bir tescilli araca kilitli bir anlamsal katmandan kaçının. Bireysel kurumları, operasyonel verilerini modellemekte özgür bırakırken ulusal düzeyde raporlanan her şey için ortak boyutlara uymalarını sağlayın. Sürümlü bir tanıma izlenemeyen yayımlanmış bir gösterge, bir veri sorunu olduğu kadar bir hesap verebilirlik başarısızlığıdır.

## Örnekler

**Girişim.** Bir Seri A şirketinin "etkin kullanıcı" için üç farklı yerde yaşayan üç tanımı vardı: ürün analitiği aracı, finans tablosu ve yatırımcı sunumu. Sayılar hiç eşleşmedi ve her yönetim kurulu hazırlığı bir telaşa dönüştü. İki mühendis dönüştürme araçlarında küçük bir anlamsal katman getirdi; "etkin kullanıcı" ve "aylık yinelenen gelir"i bir kez, test edilmiş kod olarak, tam pencereleri ve dışlamaları yazılı olarak tanımladılar. Her pano artık bu tanımları okuyor. Yönetim kurulu hazırlığı tartışması ortadan kalktı ve yeni bir analisti işe alıştırmak bir haftalık kabile bilgisinden tek bir belgelenmiş modeli okumaya indi. Bu, bölüm 7.4'te (ürün analitiği ve deney) anlatılan disiplinle doğrudan bağlantılıdır; orada "etkin"in kararlı bir tanımı deney sonuçlarını karşılaştırılabilir kılan şeydir.

**Kurumsal.** Küresel bir perakendeci pazarlama, finans, tedarik zinciri, ürün yönetimi ve mağazalar arasında beş iş zekâsı aracı çalıştırıyordu ve her biri "brüt marj"ı biraz farklı yeniden icat etmişti. Uyumlu boyutlarla Kimball tarzı bir ambarın üzerine tek bir anlamsal katman kurdular; böylece "ürün", "mağaza" ve "tarih" her olgu tablosunda ve her araçta aynı anlama geldi. Her metrik bir kez tanımlandı ve her yerde tüketildi. Çeyrek başına günler yiyen uzlaştırma toplantıları çoğunlukla ortadan kalktı ve finans iadelerin marjı nasıl etkilediğini değiştirdiğinde, değişiklik beş araca birden yayıldı. Uyumlu boyutlar, bağımsız takımların verilerini şüpheyle değil güvenle birleştirmesini sağlayan şeydi.

**Kamu.** Bir ulusal hükûmetin, her biri tarihsel olarak "hane", "bölge" ve "istihdam"ı kendine göre tanımlayan sağlık, iş gücü ve eğitim kurumları arasında karşılaştırılabilir raporlamaya ihtiyacı vardı. Kurumlar arası bir organ ortak referans veri ve standart tanımlar oluşturdu: coğrafya ve demografi için kanonik boyut tabloları ve çekirdek göstergelerin, metodoloji ve sürümlü yayınlarla birlikte yayımlanan yönetilen tanımları. Bireysel kurumlar kendi operasyonel verilerini modeller ama ulusal düzeyde raporlanan her şey için ortak boyutlara ve tanımlara uyar. Sonuç, bir kurumdan gelen bir rakamın bir başkasıyla dürüstçe karşılaştırılabilmesi ve halkın yayımlanmış her göstergeyi belgelenmiş bir tanıma izleyebilmesidir; bu, bölüm 7.1'de ele alınan şeffaflık yükümlülüklerini destekler.

## İş gerekçesi: motivasyonlar, YG ve TSM

İyi modellemenin ve bir anlamsal katmanın getirisi çoğunlukla geri kazanılan zaman ve önlenen hatadır. Birçok kuruluşta analistler zamanlarının çoğunu veriyi bulmaya, çelişen sayıları uzlaştırmaya ve başkalarının zaten yazdığı tanımları yeniden kurmaya harcar. Her metriğin tek yönetilen tanımı, bu tekrarlanan işi tek seferlik bir yatırıma çevirir. Aynı zamanda bütün bir pahalı başarısızlık kategorisini ortadan kaldırır: bir yönetim kurulu sunumundaki yanlış sayı, bir denetim bulgusunu tetikleyen yanlış raporlanmış rakam, yalnızca iki takım "geliri" farklı tanımladığı için var olan çeyrek uzunluğundaki uzlaştırma projesi. Tanım gözden geçirilmiş tek bir yerde yaşadığında bu başarısızlıklar büyük ölçüde sona erer.

Maliyet gerçektir ve adlandırmaya değer. Kavramsal ve mantıksal modellemeye, anlamsal katmanı kurmaya ve doldurmaya ve tanımları güncel tutan süregelen sahipliğe baştan yatırım yaparsınız. Toplam sahip olma maliyeti (TSM) araçları, modelleme ve analitik mühendisliği zamanını ve modelin kaymasını önlemek için yönetişimi içerir. Bunu yapmamanın maliyetine karşı tartın; bu daha büyüktür ama gizlidir: yinelenen boru hatları, insan uzlaştırma motoru olarak analistler ve kimsenin savunamadığı rakamlara dayanarak kendinden emin kararlar veren yöneticiler olarak ortaya çıkar. Gerekçeyi liderliğe kendi terimleriyle sunun. Her metriğin tek güvenilir tanımı, iş genelinde karşılaştırma yapmalarını, panolara güvenmelerini ve düzenleyicileri alarm tatbikatı olmadan yanıtlamalarını sağlayan şeydir. Uzlaştırma acısının en kötü olduğu yerden başlayın, o birkaç metriği bir kez tanımlayın ve geri kazanılan zamanın gerisini finanse etmesine izin verin.

## Anti-kalıplar ve tuzaklar

- Doğrudan fiziksel tablolara atlamak, bugünün teknolojisini onlardan uzun yaşaması gereken kararlara gömmek.
- Aynı metriği her panoda bağımsız tanımlamak; böylece hiçbir iki sayı uyuşmaz.
- Taneciği belirtmeden bırakmak, sonra bir gelir raporunda çift sayılan ölçüler keşfetmek.
- Analitik tabloları belgelenmiş karar yerine kazara denormalleştirmek.
- Bir analitik ambarı, her sorgu kimsenin anlamadığı on iki tablolu bir birleştirme olana kadar normalleştirmek.
- Yavaş değişen boyutları üzerine yazarak ele almak; böylece geçmiş raporlar geçmişi sessizce yeniden yazar.
- Her yerde doğal anahtar kullanmak; böylece bir kaynak sistem anahtar değişikliği tüm ambara yayılır.
- Sahibi olmayan bir anlamsal katman kurmak; böylece tanımlar kayar ve güven aşınır.
- Modeli, evrilebilir kalması gereken yaşayan bir varlık yerine lansmanda bitmiş saymak.

## Olgunluk modeli

- **Düzey 1, Başlangıç:** Modelleme örtük ve tepkiseldir. Tablolar, onlara ihtiyaç duyan kişi tarafından önce-fiziksel tasarlanır. Metrikler her raporda yeniden tanımlanır ve sayılar rutin olarak çelişir. Tanecik belgelenmemiştir ve tanımlara kimse sahip değildir.
- **Düzey 2, Geliştirme:** Bazı analitik tablolar boyutsal bir kalıbı izler ve birkaç kilit metriğin yazılı tanımı vardır, ama bunlar bir wiki'de yaşar ve uygulanmaz. Adlandırma kuralları kâğıt üzerinde vardır. Pratik takımdan takıma değişir ve uzlaştırma hâlâ sık ve elle yapılır.
- **Düzey 3, Standartlaştırma:** Kavramsal, mantıksal ve fiziksel modeller ayrıdır ve gözden geçirilir. Bir anlamsal katman çekirdek metrikleri bir kez, sahipleri olan sürümlenmiş kod olarak tanımlar. Uyumlu boyutlar takımların güvenle birleştirmesini sağlar. Tanecik ve yavaş değişen boyut stratejileri belgelenir ve kuruluş genelinde incelemede uygulanır.
- **Düzey 4, Yönetme:** Model mülkü temel çizgilere karşı ölçülür. Metrik tanımı kapsamını (raporlanan metriklerin anlamsal katman tarafından sunulan payı), hâlâ kullanımda olan yinelenen ya da gölge tanımların sayısını, çeyrek başına harcanan uzlaştırma saatlerini ve incelemede ile üretimde yakalanan tanecik ve soyağacı kusurlarının oranını izlersiniz. Tanım değişiklikleri testlerle gözden geçirilmiş çekme istekleri üzerinden akar ve tazelik, test geçme oranları ve kayma panolarda izlenir. Bir metrik ayrıştığında ya da bir boyut uyumu bıraktığında, ölçüm bunu bir yönetim kurulu toplantısından önce yüzeye çıkarır.
- **Düzey 5, Orkestrasyon:** Her önemli metriğin tüm araçlar ve takımlar tarafından tüketilen tek bir yönetilen tanımı vardır ve anlamsal katman analitik, deney ve düzenlenmiş raporlamayla bütünleşmiştir. Modeller tasarım gereği evrilebilirdir ve sürekli iyileştirilir; tanımlar kuruluş genelinde güvenilir; uzlaştırma işi büyük ölçüde ortadan kalkmıştır. Kuruluş, iş değiştikçe yeni boyutları rutin olarak kullanımdan kaldırır, yeniden kapsamlandırır ve uyumlar; model mülkünü uyarlanabilir bir varlık olarak yeniden dengeler.

## Tartışma fikirleri

1. En önemli üç metriğinizi seçin. Bugün araçlarınız arasında her birinin kaç farklı tanımı var ve onları bire indirmek için ne gerekir?
2. Belirtilmemiş bir tanecik nerede gerçek bir raporlama hatasına yol açtı ve fark edilmesi ne kadar sürdü?
3. Boyutlarınızdan hangileri takımlar arasında önce uyumlu hale getirilmeli ve sahipleri kim?
4. Metrik tanımlarınız incelemeyle sürüm kontrolünde mi, yoksa bir BI aracının içinde sessizce düzenlenebilir mi?
5. Yavaş değişen bir boyut geçmişinizi en son ne zaman kimse fark etmeden yeniden yazdı ve bir dahaki sefere bunu nasıl yakalarsınız?
6. Ambar motorunuzu yarın değiştirseniz, modelinizin anlamının ne kadarı taşınmadan sağ çıkardı?

## Önemli çıkarımlar

- Veri modelleme, verinin ne anlama geldiğine karar vermektir ve bu anlam seçtiğiniz her depolama teknolojisinden uzun yaşar.
- Üç düzeyde sırayla modelleyin: önce kavramsal, sonra mantıksal, sonra fiziksel.
- İşlemsel sistemleri doğruluk için normalleştirin; analitik olanları hız için bilinçli denormalleştirin.
- Analitik için olgular, boyutlar ve belirtilmiş bir tanecikle boyutsal modelleme kullanın.
- Her iş metriğinin her yerde tek bir yönetilen tanımı olması için tek bir anlamsal katman kurun.
- Uyumlu boyutlar bağımsız takımların verilerini güvenle birleştirmesini ve karşılaştırmasını sağlar.
- İyi adlandırın, belgeleyin, vekil anahtarlar kullanın ve model evrilebilir kalsın diye tanımları sürümleyin.

## Kaynaklar ve ileri okuma

- Ralph Kimball and Margy Ross, *The Data Warehouse Toolkit: The Definitive Guide to Dimensional Modelling*.
- Bill Inmon, *Building the Data Warehouse*.
- Dan Linstedt and Michael Olschimke, *Building a Scalable Data Warehouse with Data Vault 2.0*.
- Peter Chen, "The Entity-Relationship Model: Toward a Unified View of Data," ACM Transactions on Database Systems.
- E. F. Codd, "A Relational Model of Data for Large Shared Data Banks," Communications of the ACM.
- C. J. Date, *An Introduction to Database Systems*.
- Lars Rönnbäck and colleagues, writings on anchor modelling.
- DAMA International, *DAMA-DMBOK: Data Management Body of Knowledge*.
