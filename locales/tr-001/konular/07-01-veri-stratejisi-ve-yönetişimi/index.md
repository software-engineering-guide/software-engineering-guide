# 7.1 Veri stratejisi ve yönetişimi

## Genel bakış ve motivasyon

Veri stratejisi, veriyi bir varlık olarak ele almak için yaptığınız bilinçli plandır: veri nasıl üretilir, tanımlanır, sahiplenilir, korunur, paylaşılır ve değer yaratmak için tüketilir. [Veri yönetişimi](https://en.wikipedia.org/wiki/Data_governance) ise stratejiyi gerçeğe dönüştüren işletim sistemidir: veriyi zaman içinde güvenilir ve uyumlu tutan roller, politikalar, standartlar ve denetimler. Küçük takımlarda bu konular çoğu zaman örtüktür, birkaç mühendisin kafasında taşınır. Büyük geliştirici kurumlarında, kurumsal şirketlerde ve kamu kurumlarında bu gayriresmîlik çöker. Yüzlerce takım binlerce tablo üretir. Düzinelerce sistem "gerçek" müşteri kaydını kendisinin tuttuğunu iddia eder. Ve bir yönetim kurulu sunumunda ya da kamuya açık bir raporda hangi sayının doğru olduğunu kimse güvenle söyleyemez.

Büyük takımlar için kötü veri yönetişiminin maliyeti soyut değildir. Düzenleyiciler; [GDPR](https://en.wikipedia.org/wiki/General_Data_Protection_Regulation) (AB Genel Veri Koruma Tüzüğü), [HIPAA](https://en.wikipedia.org/wiki/Health_Insurance_Portability_and_Accountability_Act) (ABD Sağlık Sigortası Taşınabilirlik ve Sorumluluk Yasası) ve sektöre özgü kurallar gibi rejimler altında kişisel, finansal ve sağlık verileri üzerinde gösterilebilir köken ve denetim bekler. Kurumsal şirketler yanlış raporlanan metriklerden, başarısız denetimlerden ve çoğalmış veri platformlarından doğrudan mali risk taşır. Kamu kurumları ise kayıt saklama, bilgi edinme hakkı kapsamında erişim, kamuya karşı hesap verebilirlik ve vatandaşlara eşit muamele konularında ek yükümlülükler taşır. Bu ortamların hepsinde güvenemediğiniz veri, hiç veri olmamasından daha kötüdür, çünkü kendinden emin ama yanlış kararlara yol açar.

Ölçekte ilerlemeyi sağlayan fikir basittir: veriyi bir ürün olarak ele alın. Veri, uygulamaların egzozundan çıkan bir yan ürün olmak yerine, her önemli veri kümesinin bir sahibi, belgelenmiş bir arayüzü, kalite garantileri ve müşteri gibi görülen tüketicileri olur. Bu bölüm, bu ürün zihniyetini klasik yönetişim disiplinleriyle birlikte ele alır: veri sorumluluğu (stewardship), kataloglama, [ana veri yönetimi](https://en.wikipedia.org/wiki/Master_data_management) ve kalite. Ayrıca hangi modelin takımınıza uyacağını belirleyen örgütsel seçimleri de kapsar: [veri ağı](https://en.wikipedia.org/wiki/Data_mesh) (ürün olarak yayımlanan, alan sahipliğinde, merkezsiz veri), veri gölevi (esnek bir [veri gölünün](https://en.wikipedia.org/wiki/Data_lake) üzerine eklenmiş ambar tarzı yönetim ve yönetişim) ve [veri ambarı](https://en.wikipedia.org/wiki/Data_warehouse) (modellenmiş, sorguya hazır verinin yönetilen merkezî deposu).

*Ayrıca bakın:* bölüm 4.5 (gizlilik ve veri koruma), bölüm 7.2 (veri mühendisliği) ve bölüm 4.6 (uyum ve yönetişim).

## Temel ilkeler

- Veri, uygulamaların atılabilir bir yan ürünü değil, sahipleri olan kalıcı bir varlıktır.
- Her önemli veri kümesinin adı belli, hesap verebilir bir sahibi ve belgelenmiş bir sözleşmesi vardır.
- Yönetişim güvenilir kullanımı mümkün kılar; yalnızca hayır diyen bürokratik bir kapı değildir.
- Her kritik iş varlığı için tek bir yetkili kaynak olmalıdır.
- Kalite, gizlilik ve köken sonradan denetlenerek değil, baştan tasarımla sağlanır.
- Veri tüketicileri, ürünü şekillendiren müşterilerdir.
- Politikalar, mümkün olan her yerde iyi niyete bırakılmaz, kodlanır ve otomatik olarak uygulanır.
- Kurum büyüdükçe birleşik (federe) sahiplik, tek bir merkezî takımdan daha iyi ölçeklenir.

## Öneriler

### Veriyi bir ürün olarak ele alın

Her önemli veri kümesine, kullanıma uygunluğundan sorumlu bir ürün sahibi verin. Bir veri ürününün adı, belgelenmiş bir şeması, anlamının ve kaynağının açıklaması, tanımlı bir yenileme temposu ve yayımlanmış kalite beklentileri vardır. Tüketicileriniz onu üreten takıma tek bir soru sormadan keşfedebilmeli, anlayabilmeli ve ona güvenebilmelidir. Yazılım API'lerine uyguladığınız disiplini uygulayın: sürümleme, kullanımdan kaldırma duyuruları, değişiklik günlükleri ve geriye dönük uyumluluk.

### Veri sözleşmeleri ve SLA'lar oluşturun

Veri sözleşmesi, bir üretici ile tüketicileri arasındaki açık ve makinece denetlenebilir bir anlaşmadır. Şemayı, anlamı, tazeliği, hacmi ve izin verilen değişiklikleri kapsar. Sözleşmeleri hatta uygulayın; böylece yukarı akıştaki bozucu bir değişiklik, haftalar sonra aşağı akıştaki raporları sessizce bozmak yerine kaynağında hızla başarısız olur. Sözleşmeleri hizmet düzeyi anlaşmaları ve hedefleriyle eşleştirin. Örneğin: "müşteri boyutu her gün 06:00'ya kadar yenilenir, günlerin %99,5'inde, iş anahtarlarının %0,1'inden azı boş olacak şekilde." Bunları yayımlayın ve ihlallerde uyarı verin.

### Veri sorumluluğu ve bir yönetişim işletim modeli kurun

Hesap verebilirliği yürütmeden ayrı tutun. Veri sahipleri (çoğu zaman iş liderleri) bir alandan hesap verebilir. Veri sorumluları (konu uzmanları) tanımları sürdürür, kalite sorunlarını çözer ve erişimi onaylar. Hafif bir veri yönetişim konseyi, kesişen standartları belirler ve anlaşmazlıkları çözer. Modeli birleşik tutun: merkezî bir destek takımı araçları, standartları ve koçluğu sağlar, alan takımları ise kendi verilerinin sahibidir. Bu, tam merkezileşmenin darboğazından da, hiç yönetişim olmamasının kaosundan da kaçınmanızı sağlar.

### Bir veri kataloğuna ve köken izlemeye yatırım yapın

Aranabilir bir katalog, veri varlığınızın ön kapısıdır. İş sözlüklerini, teknik şemaları, sahipliği, hassasiyet sınıflandırmalarını, kalite puanlarını ve kaynak sistemden dönüşümler üzerinden panolara uzanan uçtan uca kökeni içermelidir. Üstünden hızla çürüyen elle belgelemeye güvenmek yerine üst veri toplamayı otomatikleştirin. Köken, etki analizi, olay müdahalesi, denetim ve veri öznesi erişim ile silme gibi düzenleyici talepler için şarttır.

### Ana veri yönetimi ve tek doğruluk kaynağı

Çekirdek varlıklar (müşteri, vatandaş, ürün, tedarikçi, çalışan) için çoğaltılmış ve çelişen kayıtları tek bir altın kayıtta uzlaştırmak üzere ana veri yönetimini kullanın. Merkezin ne kadar yetkili olması gerektiğine göre bir mimari seçin (kayıt defteri, birleştirme, bir arada var olma ya da merkezî). Eşleştirme ve hayatta kalma kurallarını açıkça tanımlayın ve denetlenebilir kılın. [Tek doğruluk kaynağı](https://en.wikipedia.org/wiki/Single_source_of_truth), finans, satış ve operasyonun her birinin farklı gelir bildirdiği klasik başarısızlığı önler.

### Veri kalitesini boyutlar boyunca ölçün

Kaliteyi adlandırılmış boyutlar üzerinden yönetin: doğruluk, bütünlük (eksiksizlik), tutarlılık, güncellik, geçerlilik ve benzersizlik. Hatları otomatik testlerle ve sürekli veri gözlemlenebilirliğiyle (tazelik, hacim, şema kayması ve dağılım denetimleri) donatın; böylece anormallikleri tüketiciler etkilenmeden yakalarsınız. Veri olaylarına, tespit, önceliklendirme, kök neden analizi ve olay sonrası incelemelerle üretim kesintileri gibi davranın.

### Sınıflandırın, koruyun ve erişimi denetleyin

Veriyi hassasiyetine göre sınıflandırın ve denetimleri orantılı uygulayın: şifreleme, maskeleme, belirteçleme (tokenisation), satır ve sütun düzeyinde güvenlik ve düzenli gözden geçirilen en az ayrıcalık erişimi. Hem azaltma (minimizasyon) gereksinimlerini hem de kayıt saklama hukukunu karşılayan bir saklama ve silme takvimi tutun. Kamu bağlamlarında şeffaflık yükümlülüklerini gizlilik korumalarıyla vaka vaka değil, bilinçli olarak uzlaştırın.

## Ödünleşimler: artılar ve eksiler

| Yaklaşım | Artılar | Eksiler | En uygun olduğu yer |
|---|---|---|---|
| Merkezî yönetişim takımı | Tutarlı standartlar, net hesap verebilirlik | Darboğaz, alanlardan kopuk | Küçük ya da yüksek düzeyde düzenlenmiş kurumlar |
| Birleşik (federe) yönetişim | Ölçeklenir, alan uzmanlığı, sahiplik | Güçlü araç ve kültür gerektirir | Büyük, çok alanlı kurumsal şirketler |
| Veri ambarı | Olgun, yönetilen, performanslı SQL | Katı, yapısal olmayan veri için pahalı | Kararlı, iş zekası ağırlıklı iş yükleri |
| Veri gölevi | Esnek, birleşik, her veri türünü işler | Daha genç araçlar, yönetişim çabası | Karma analitik ve makine öğrenmesi |
| Veri ağı | Alan sahipliği, örgütsel olarak ölçeklenir | Yüksek olgunluk eşiği, eşgüdüm maliyeti | Çok büyük, merkezsiz kurumlar |

Yönetişim her zaman hızı güvenle takas eder. Hafif yönetişim takımların hızlı ilerlemesine izin verir; bir denetim, ihlal ya da utandırıcı bir yanlış raporlama pahalı bir hesaplaşmayı zorunlu kılana kadar. Ağır yönetişim güveni korur ama denemeyi boğabilir ve takımları gölge sistemlere itebilir. Kalıcı cevap, yönetişimi otomatik, self servis korkuluklar olarak kodlamaktır; böylece uyumlu yol aynı zamanda kolay yol olur. Mimari olarak ambarlar yönetilen sadeliği, ağ örgütsel ölçeği tercih eder, gölevler ise ikisinin ortasında durur. Doğru seçim, herhangi bir teknik kıyaslamadan çok kurumunuzun yapısını izler.

## Takımınızla tartışılacak sorular

1. **Hangi veri mimarisi (ambar, gölev ya da ağ) kurumunuzun yapılanmasına gerçekten uyuyor ve her birinin istediği olgunluk eşiği konusunda dürüst müsünüz?** Ödünleşim tablosu bu seçimin kıyaslamaları değil kurum yapısını izlediğini vurgular: ambar kararlı, iş zekası ağırlıklı iş yüklerini ödüllendirir, gölev karma analitik ve makine öğrenmesini işler, ağ ise birçok özerk alana ölçeklenir ama yüksek olgunluk ve güçlü araç ister. Düzinelerce alanı olan büyük bir kurumsal şirket ya da kamu kurumu için, self servis platformlarınız ve bir yönetişim kültürünüz olmadan ağa atlamak, merkezsizlik kılığına girmiş bir kaos üretir. Somut işaretler getirin: kaç alan veri üretiyor, merkezî takımlar zaten bir darboğaz mı, alan takımlarının ürünlerin sahibi olacak beceri ve teşviki var mı. Bugün birleşik araçlarınız yoksa dürüst cevap, şimdilik yönetilen bir ambar ya da gölev, daha sonra bir ağ olabilir. İnsanlarınızın gerçekten işletebileceği modeli seçin, sonra bir sonraki modelin ihtiyaç duyduğu olgunluğa yatırım yapın.

2. **Bugün bir silme talebini uçtan uca yerine getirebilir misiniz ve köken kayıtlarınız bir kişisel kaydın her kopyasının nereye gittiğini kanıtlıyor mu?** GDPR ve benzeri rejimler altında bir veri öznesinin silme ya da erişim talebi, kesin son tarihleri olan yasal bir yükümlülüktür; veriyi köken izlemesi olmadan geniş çapta kopyalamak bunu karşılamayı imkânsız kılar. Büyük takımlar veriyi düzenli olarak veri martlarına, çıktılara, önbelleklere ve elektronik tablolara dağıtır; dolayısıyla asıl soru, aslı silebilip silemeyeceğiniz değil, her kopyayı izleyip ona ulaşıp ulaşamayacağınızdır. Kanıt getirin: gerçek bir müşteri ya da vatandaş seçin ve verisinin bulunduğu her yeri sıralamayı deneyin. Yapamıyorsanız bu boşluk hem bir uyum riski hem de bir ihlal etki alanı sorunudur. Cevap, otomatik köken izlemeye ve denetimsiz kopyalamaya getirilecek daha sıkı kontrollere yatırımı yönlendirmelidir, çünkü uyumlu yol, talep gelmeden önce kurulmak zorundadır.

3. **Yönetişiminiz kolay yol mu, yoksa insanların etrafından dolaştığı bir kapı mı; bunu kanıtlayan gölge sistemler nerede?** Bölümün kalıcı cevabı, yönetişimi otomatik, self servis korkuluklar olarak kodlamaktır; böylece uyumlu yol aynı zamanda en hızlı yol olur, çünkü ağır elle yönetişim takımları gölge elektronik tablolara ve yönetilmeyen kopyalara iter. Kurumsal şirketler ve kamu kurumları için ihlaller, yanlış sayılar ve başarısız denetimler tam da kimse izlemediği için gölge sistemlerde doğar. Somut bir envanter getirin: hangi takımlar kendi kopyalarını tutuyor, hangi raporlar kataloğu atlıyor, insanlar resmî sürecin nerede fazla yavaş olduğunu söylüyor. Her gölge sistem, yönetilen yolun çözüm yoldan daha pahalıya geldiğinin işaretidir. Bir politika daha yayımlamak yerine sürtünmeyi giderin; böylece onaylı veriyi ve sözleşmeleri kullanmak, onları dolaşmaktan gerçekten daha kolay olur.

4. **Hangi kritik iş varlığının tek bir yetkili kaynağa en çok ihtiyacı var ve altın kaydından bugün adıyla kim hesap verebilir?** Ana veri yönetimi, finans, satış ve operasyonun her birinin farklı bir müşteri ya da farklı bir gelir rakamı bildirmesini önlemek için vardır; ölçekte tek bir yetkili kaynağın yokluğu, alanlar arası her sayıyı bir tartışmaya çevirir. Rakip kaygılar, merkezin ne kadar yetkili olması gerektiği (kayıt defteri, birleştirme, bir arada var olma ya da tamamen merkezî) ve ne kadar eşleştirme ve hayatta kalma mantığı kurup denetlemeye razı olduğunuzdur; çünkü daha ağır bir merkez daha pahalıdır ama daha çok çelişkiyi çözer. En çok rapor içinde görünen varlıkları (müşteri, vatandaş, ürün, tedarikçi, çalışan), her biri için gerçek kaydı tuttuğunu iddia eden sistem sayısını ve bugün kullandığınız eşleştirme kurallarını, varsa, getirin. Bir banka ya da ulusal bir kurum için, hesap verebilir sahibi ve hayatta kalma kurallarını açıkça adlandırın; çünkü bir rakamı kamuya açık rapordan kaynağa kadar izleyen bir düzenleyici, hangi kopyanın kazanacağına kimin karar verdiğini soracaktır ve "kimse" bir denetimden sağ çıkan bir cevap değildir.

5. **Kritik bir veri kümesinin kullanıma uygun olduğunu, bir tüketici bozuk olduğunu keşfetmeden önce nasıl bilirsiniz?** Olgunlaşmamış veri varlıklarında kalite, panosu bozulan analist ya da yönetim kurulu sayısı yanlış çıkan yönetici tarafından bulunur; bu, olabilecek en pahalı tespit noktasıdır. Gerilim, kaliteyi ölçümleme maliyeti (testler, tazelik ve hacim denetimleri, doğruluk, bütünlük ve geçerlilik gibi adlandırılmış boyutlar üzerinde dağılım ve şema kayması izleme) ile önlediğiniz olayların maliyeti arasındadır; takımlar bu yatırımı düzenli olarak eksik yapar, çünkü başarısızlıklar felakete dönüşene kadar görünmez kalır. Son üç veri olayını, nasıl tespit edildiklerini ve kimse fark etmeden önce ne kadar sürdüklerini, ayrıca bugün gerçekte yayımlayıp uyarı verdiğiniz kalite SLA'larını getirin. Kurumsal ve kamu raporlaması için her kritik veri ürününü açık kalite eşiklerine bağlayın ve bir ihlale önceliklendirme ve olay sonrası incelemeyle bir üretim kesintisi gibi davranın; çünkü bir düzenleyici beyannamesindeki ya da kamuya açık bir istatistikteki yanlış rakamın yasal ve itibar maliyeti, izleme faturasını cüceleştirir.

6. **Yönetişiminiz gerçekten alan sahipliğiyle birleşik (federe) mi, yoksa anlamadığı veriden hesap verebilir tutulan merkezî bir takım mı?** Bölüm, merkezî destekle birleşik sahipliğin, saf merkezileşmenin darboğaza girdiği ve saf merkezsizliğin kaosa sürüklendiği yerde ölçeklendiğini savunur; yine de birçok kurum federasyon iddia ederken, alan bilgisi olmadığı binlerce tablodan nominal olarak küçük bir merkezî takım hesap verebilir durumdadır. Rakip çekim gerçektir: merkezî takımlar tutarlılık ve tek muhatap sağlar, alan sahipliği ise uzmanlık ve hesap verebilirlik sağlar ama iş sahiplerinin istemeyebilecekleri sorumluluğu kabul etmesini gerektirir. En önemli alanlarınız için, kimin hesap verebilir olduğuna karşı tanımları fiilen kimin sürdürdüğünü ve kalite sorunlarını kimin çözdüğünü gösteren dürüst bir harita getirin; ayrıca sorumluların rolün gerektirdiği yetkiye ve zamana sahip olup olmadığını. Büyük bir kurumsal şirkette ya da kurumda sahipliğin, hem alan bilgisine hem de hayır deme yetkisine sahip kişilerde olduğunu doğrulayın; çünkü yetkisiz bir merkezî takıma verilen yönetişim, kimsenin uymadığı politikalar ve hiçbir şeyi çözmeyen bir konsey üretir.

## Sektör merceği

**Girişim.** Hız ve hayatta kalma, süreci yener. Her çekirdek veri kümesi için bir sahip belirleyin ve "aktif müşteri" gibi varlıklar için bir depoyu tek doğruluk kaynağı yapın; kataloğu, konseyi ve ağı tümüyle atlayın. Elinizdeki bir avuç kritik tablo için tek sayfalık bir sözleşme (şema, yenileme zamanı, tek bir kalite beklentisi), "kimin sayısı doğru" tartışmasını bir öğleden sonrada bitirir. Karşılayamayacağınız bir işlevi kadrolandırmak yerine ambarınıza zaten yerleşik yönetişimden yararlanın.

**Küçük işletme.** Özel bir veri uzmanınız ve dar bir bütçeniz yoksa yönetişimi bir platform projesi olarak değil, veri hijyeni olarak ele alın: hangi kişisel verileri tuttuğunuzu, nerede durduğunu ve ona kimin dokunabileceğini bilin. Köken, erişim denetimi ve saklamayı kutudan çıktığı gibi sağlayan yönetilen bir ambar ya da iş zekası aracını tercih edin; böylece yönetişimi inşa etmek yerine zaten çalıştırdığınız araçlara gömülü olarak satın alırsınız. Özel bir hattı, işi gerçekten yürüten tek veri kümesine saklayın.

**Kurumsal.** Birçok takımı kapsayan ölçekte iş, merkezî destekle birleşik sahiplik demektir: otomatik köken izlemeli ortak bir katalog, uygulanan veri sözleşmeleri, çekirdek varlıklar için ana veri ve taban çizgilerine karşı ölçülen kalite SLA'ları. Yönetişimi self servis korkuluklar olarak kodlayın; böylece uyumlu yol aynı zamanda hızlı yol olsun, ve veriyi adı belli sahipleri olan bir ürün portföyü olarak yönetin. Böylece denetçiler herhangi bir rakamı rapordan kaynağa kadar izleyebilir ve gruplar aynı hatları ve tanımları yeniden icat etmeyi bırakır.

**Kamu.** Satın alma kuralları, şeffaflık ve kamuya karşı hesap verebilirlik her seçimi şekillendirir. Yayımlanan göstergeleri belgelenmiş metodoloji, sürümlenmiş yayınlar ve kalite eşikleriyle veri ürünleri olarak ele alın; bilgi edinme ve açık veri yükümlülüklerini gizlilik ve azaltmayla vaka vaka değil, bilinçli olarak uzlaştırın. Kilitlenmeyi önlemek için tedarikçi sözleşmelerinde veri taşınabilirliği ve köken ifşası talep edin, savunulabilir bir saklama ve silme takvimi tutun ve ortak tanımları bir sorumlular konseyine tutturun; böylece "hane" ya da "işsizlik" her bakanlıkta aynı anlama gelir.

## Örnekler

**Girişim.** Tohum aşamasındaki bir SaaS şirketi, faturalama elektronik tablosunun, satış aracının ve ürün veritabanının her birinin farklı bir müşteri sayısı bildirdiğini ve yatırımcı güncellemesi için hangisinin doğru olduğunu kimsenin söyleyemediğini fark etti. Dört kişilik takım her çekirdek veri kümesi için bir sahip belirledi, ambarı "aktif müşteri" için tek kaynak yaptı ve şemayı ile günlük yenileme zamanını anlatan tek sayfalık bir sözleşme yazdı. Bir öğleden sonra sürdü ve hangi sayıya güvenileceğine dair haftalık tartışmayı bitirdi.

**Kurumsal.** Çok uluslu bir banka, perakende, kredi ve servet bölümlerindeki düzinelerce çelişen müşteri kaydını, hayatta kalma kuralları ve bir altın kaydı olan bir ana veri yönetimi merkezinde birleştirdi. Her alan, sözleşmeleri ve tazelik SLA'larıyla veri ürünleri yayımladı; bunlar köken izlemeli merkezî bir katalogda görünür kılındı. Düzenleyici raporlama süresi keskin biçimde düştü, çünkü denetçiler artık herhangi bir rakamı rapordan kaynağa kadar izleyebiliyordu. Banka ayrıca gereksiz birkaç raporlama platformunu emekliye ayırdı.

**Kamu.** Ulusal bir istatistik kurumu yayımladığı göstergeleri belgelenmiş metodoloji, sürümlenmiş yayınlar ve sıkı kalite eşikleriyle veri ürünleri olarak ele alır. Bir sorumlular konseyi bakanlıklar arası tanımları uzlaştırır; böylece "işsizlik" ya da "hane" her yerde aynı anlama gelir. Sınıflandırma ve denetimli erişim, katılımcıların gizliliğini korurken, kamuya açık bir katalog şeffaflığı ve bilgi edinme yükümlülüklerini destekler.

## İş gerekçesi: motivasyonlar, YG ve TSM

Veri yönetişiminin motivasyonu, kabaca eşit ölçüde risk azaltma ve değer yaratmadır. Risk tarafında kaçınılan maliyetler arasında düzenleyici cezalar, ihlal yükümlülüğü, başarısız denetimler ve yanlış sayılar yayımlamanın itibar kaybı yer alır. Değer tarafında ise güvenilir, keşfedilebilir veri, aşağı akıştaki her analitik ve makine öğrenmesi çabasını hızlandırır, çoğalmış hatları azaltır ve sorudan cevaba geçen süreyi kısaltır.

Benimseme maliyeti gerçektir: katalog ve kalite araçları, sorumluların ve sahiplerin zamanı ve sahipliğin yerleşmesi için gereken örgütsel değişim. TSM'yi (toplam sahip olma maliyeti) benimsememenin maliyetiyle tartın; bu maliyet genellikle daha büyüktür, yalnızca gizlidir. Ölçülmediğinde bu maliyet, zamanının çoğunu veri bulmaya ve temizlemeye harcayan analistler, aynı hatları yeniden kuran takımlar ve kimsenin savunamayacağı rakamlara dayanarak karar veren yöneticiler olarak ortaya çıkar. Gerekçeyi liderliğe kendi dillerinde anlatın: yönetişim, veriyi sınırsız aşağı yönlü riski olan bir yükümlülükten bileşik getirisi olan bir varlığa dönüştürür ve güvenilir yapay zekanın ön koşuludur. Değeri hızla gösterebilmek için acının ve düzenleyici riskin en yüksek olduğu yerden başlayın.

## Anti-kalıplar ve tuzaklar

- Otomasyonu olmayan, kimsenin uymadığı politikalar üreten komiteyle yönetişim.
- Gerçekten önemli olan veri kümeleri yerine her şeyi bir anda kataloglamak.
- Okyanusu kaynatmaya çalışan ve hiç altın kayıt çıkarmayan ana veri projeleri.
- [Veri kalitesini](https://en.wikipedia.org/wiki/Data_quality) sürekli gözlemlenebilirlik yerine tek seferlik bir temizlik olarak görmek.
- Alan bilgisi ya da yetkisi olmayan merkezî bir takıma verilen sahiplik.
- Wiki'lerde belgelenmiş ama hatlarda uygulanmayan sözleşmeler.
- Veriyi köken izlemesi olmadan geniş çapta kopyalamak ve silme taleplerini yerine getirilemez kılmak.
- Bir araç satın alıp ona strateji demek; işletim modeli olmayan araç başarısız olur.

## Olgunluk modeli

1. Düzey 1, Başlangıç: Veri belgelenmemiş ve sahipsizdir, tesadüfi ve tepkisel biçimde ele alınır. Tanımlar takımlar arasında çelişir. Kaliteyi, raporlar bozulduğunda tüketiciler keşfeder. Katalog ya da köken izleme yoktur.
2. Düzey 2, Geliştirme: Temel uygulamalar belirir ama takımlar arasında tutarsızdır. Bazı veri kümelerinin sahipleri ve belgeleri vardır, kısmi bir katalog bulunur. Kalite denetimleri elle ve tepkiseldir. Bir yönetişim politikası yazılmıştır ama zayıf ve eşitsiz uygulanır.
3. Düzey 3, Standartlaştırma: Sahiplik, sözleşmeler ve SLA'lar belgelenmiş ve kurum genelinde uygulanmaktadır. Kritik veri ürünlerinin adı belli sahipleri vardır; otomatik köken izlemeli bir katalog temel alanları kapsar; çekirdek varlıklar için ana veri bulunur; yönetişim merkezî destekle birleşiktir ve takım takım değil tutarlı biçimde uygulanır.
4. Düzey 4, Yönetme: Veri varlığı taban çizgilerine karşı ölçülür ve denetlenir. Kalite boyutları (doğruluk, bütünlük, güncellik, geçerlilik, benzersizlik) yayımlanmış SLA hedeflerine karşı izlenir; sözleşme ihlali oranları, köken ve katalog kapsamı, tazelik ve bir silme talebini yerine getirme süresi panolarda raporlanır; gözlemlenebilirlik şema kaymasında ve hacim anormalliklerinde uyarı verir; olaylar önceliklendirme, kök neden analizi ve olay sonrası incelemeden geçer; erişim ve devam/durdurma kararları görüşe değil, taban çizgilerine karşı metriklere dayanır.
5. Düzey 5, Orkestrasyon: Yönetişim sürekli iyileştirilir ve kurum genelinde bütünleşiktir. Ürün olarak veri, alanlar arasında olağan durumdur; sözleşmeler otomatik uygulanır ve bozucu değişiklikler hızla başarısız olur; self servis korkuluklar politikayı kodlar; kalite ve köken proaktif risk yönetimini besler; tanımlara kurum genelinde güvenilir ve düzenlenmiş raporlamayı ve yapay zekayı destekler. Kurum sahipliği düzenli olarak yeniden dengeler, gereksiz platformları emekliye ayırır ve iş ile düzenleme değiştikçe yönetişimi uyarlar.

## Tartışma fikirleri

- İş varlıklarınızdan hangisinin tek bir doğruluk kaynağına en acil ihtiyacı var ve bugün neden parçalanmış durumda?
- Uygulanan veri sözleşmeleri yakın tarihli bir olayı nerede önlerdi?
- Kurumunuz birleşik sahiplik için mi yapılandırılmış, yoksa şu anda merkezileşme daha mı uyardı?
- Kamunun şeffaflık yükümlülüklerini gizlilik ve azaltmayla nasıl uzlaştırıyorsunuz?
- Analistlerinizin zamanının yüzde kaçı veri bulmaya ve temizlemeye gidiyor ve bunu yarıya indirmek ne kadar değer taşırdı?
- En önemli veri kümenizden adıyla kim hesap verebilir ve bunu biliyor mu?

## Önemli çıkarımlar

- Veriyi uygulama egzozu olarak değil, sahipleri, sözleşmeleri ve SLA'ları olan bir ürün olarak ele alın.
- Merkezî destekle birleşik yönetişim, saf merkezileşmeden daha iyi ölçeklenir.
- Otomatik köken izlemeli bir katalog, güvenilir bir veri varlığının ön kapısıdır.
- Ana veri yönetimiyle çekirdek varlıklar için tek bir doğruluk kaynağı kurun.
- Kaliteyi adlandırılmış boyutlar üzerinden gözlemlenebilirlik ve olay müdahalesiyle sürekli yönetin.
- Yönetişimi otomatik korkuluklar olarak kodlayın; uyumlu yol kolay yol olsun.
- Ambar, gölev ya da ağı, abartıya göre değil kurumunuza uygun olarak seçin.

## Kaynaklar ve ileri okuma

- DAMA International, "DAMA-DMBOK: Data Management Body of Knowledge."
- Zhamak Dehghani, "Data Mesh: Delivering Data-Driven Value at Scale."
- Ralph Kimball and Margy Ross, "The Data Warehouse Toolkit."
- Piethein Strengholt, "Data Management at Scale."
- David Loshin, "Master Data Management."
- Chad Sanderson and colleagues, writings on data contracts.
- ISO/IEC 38505, "Governance of data."
- ISO 8000, "Data quality" standard series.
