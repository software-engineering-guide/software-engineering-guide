# 7.3 Analitik ve iş zekası

## Genel bakış ve motivasyon

Analitik ve iş zekası, yönetilen ve mühendislikle hazırlanmış veriyi anlayışa ve eyleme dönüştürür. [İş zekası](https://en.wikipedia.org/wiki/Business_intelligence) (BI) geleneksel olarak, insanların işte neler olup bittiğini görmesini sağlayan raporlama, panolar ve self servis araçları anlatır. Analitik ise daha geniş bir uygulamadır: geçmişin basit betimlemelerinden, bundan sonra ne yapılacağını öneren modellere kadar veriyle soru sorup cevaplamak. İkisi birlikte, bir kurumun kendini nasıl gördüğüdür.

Büyük takımlar için bu katman, verinin ya hakkını verdiği ya da kafa karışıklığı kaynağına dönüştüğü yerdir. Binlerce çalışan kendi raporunu kurabildiğinde risk çok az bilgi değil, çok fazla çelişen bilgidir: üç farklı gelir rakamı gösteren üç pano, her biri savunulabilir, hiçbiri yetkili değil. Kurumsal şirketler, yönetim kurulu sunumlarındaki ve düzenleyici beyannamelerdeki rakamlarla yaşar ve ölür. Kamu kurumları yasama organlarına, denetim kurullarına ve kamuya rapor verir. İkisinde de farklı insanlar için farklı şeyler ifade eden bir metrik bir yükümlülüktür. Masum bile olsa yanıltıcı bir grafik, maliyetli yanlış kararlara yol açabilir ya da kamu güvenini aşındırabilir.

Bunu ölçekte evcilleştirmenin anahtar fikri [anlamsal katmandır](https://en.wikipedia.org/wiki/Semantic_layer): her aracın ve raporun beslendiği, metriklerin ve boyutların yönetilen merkezî tanımı; böylece "aktif müşteri" ya da "aylık gelir" her yerde üzerinde anlaşılmış tek bir biçimde hesaplanır. Bu fikrin çevresinde dürüst görselleştirme, bilinçli pano tasarımı ve self servisin kaçınılmaz olarak ürettiği dağınıklığı yönetme disiplinleri yer alır. Bu bölüm, tek bir doğruluk sürümünden vazgeçmeden insanlara veriye geniş erişimi nasıl vereceğinizi gösterir.

## Temel ilkeler

- Her önemli metriğin, her yerde kullanılan, yönetilen tek bir tanımı olmalıdır.
- Analitik türünü soruya uydurun: betimle, teşhis et, tahmin et ya da reçete yaz.
- Self servis güçlüdür ama metrik dağınıklığını önlemek için yönetilmelidir.
- Grafikler dürüst olmalıdır; amaç çarpıtmayla ikna etmek değil, anlamaktır.
- Panolar yalnızca veri göstermemeli, kararları yönlendirmelidir.
- Güvenilir içeriği onaylayın; tüketiciler neye güveneceklerini bilsin.
- Düzenleyin ve emekliye ayırın; daha fazla pano daha fazla içgörü demek değildir.
- Analitiği yalnızca ayrı bir BI portalına değil, kararların alındığı yerlere gömün.

## Öneriler

### Dört analitik türünü anlayın

Betimleyici analitik ne olduğunu raporlar. Teşhis edici analitik bunun neden olduğunu açıklar. [Öngörücü analitik](https://en.wikipedia.org/wiki/Predictive_analytics) neyin olası olduğunu tahmin eder. [Reçeteleyici analitik](https://en.wikipedia.org/wiki/Prescriptive_analytics) bu konuda ne yapılacağını önerir. Çoğu kurum betimleyici panolara fazla, teşhise ve eyleme az yatırım yapar. Çalışmanızı bu merdivenden bilerek yukarı taşıyın. Her önemli metriği nedenlere inme yeteneğiyle eşleştirin ve tahminleri somut kararlara ve müdahalelere bağlayın. Böylece analitik davranışı yalnızca betimlemek yerine değiştirir.

### Bir anlamsal katman kurun ve metrikleri yönetin

Metrikleri ve boyutları bir kez, merkezî bir anlamsal katmanda tanımlayın ve her BI aracının, defterin ve gömülü raporun bu tanımlardan hesaplama yapmasını sağlayın. Bu, ayrışan sayılar gibi klasik sorunu ortadan kaldırır. Ayrıca metrik mantığını sürüm denetimli, test edilebilir ve gözden geçirilebilir kılar. Metrikleri bir API gibi yönetin: onaylı her metriğin bir sahibi, net bir tanımı ve bir değişiklik günlüğü vardır. Onaylı metrikleri deneysel olanlardan ayrı tutun; tüketiciler neyin yetkili olduğunu bilsin.

### Self servisi korkuluklar içinde etkinleştirin

Analistlere ve iş kullanıcılarına veriyi keşfetmek için self servis erişim verin. Merkezî BI takımları her soruyu cevaplayamaz ve darboğazlar insanları yalnızca elektronik tablolara iter. Ama korkuluklar sağlayın: seçilmiş onaylı veri kümeleri, tutarlı metrikler için anlamsal katman, şablonlar ve eğitim. Amaç basittir: kolay yolu yönetilen tanımları kullanan yol yapın. İçeriği kademelere ayırın (onaylı, takım destekli ve kişisel); keşfetme özgürlüğü resmî gerçeklik gibi görünmesin.

### Panoları kararlar için tasarlayın

Her panoya, desteklediği karardan ve o kararı verecek kitleden başlayın. Önemli olan birkaç metrikle öne çıkın. Sayıların yorumlanabilir olması için bağlam (hedefler, eğilimler, karşılaştırmalar) sağlayın ve teşhis için ayrıntıya inmeyi mümkün kılın. Mevcut her grafiği tek sayfaya tıkıştırma dürtüsüne direnin. "Yolda mıyız, değilsek nereye bakmalıyım?" sorusunu cevaplayan bir pano, kimsenin göre hareket etmediği elli metriği gösterenden çok daha değerlidir.

### Dürüst veri görselleştirmesi uygulayın

Veriye uyan grafik türlerini seçin: zaman içindeki eğilimler için çizgiler, kategoriler arası karşılaştırmalar için çubuklar. Birkaç dilimin ötesindeki herhangi bir şey için pasta grafiklerden kaçının. Çubuk grafik eksenlerini sıfırdan başlatın, ölçekleri tutarlı tutun ve sahte korelasyonlar üreten çift eksenlerden kaçının. Rengi süs olarak değil, amaçlı ve erişilebilir biçimde kullanın. Açıkça etiketleyin ve önemli olan yerlerde belirsizliği gösterin. Sınav basittir: bilgili bir izleyici verinin desteklediği sonuca mı varır, yoksa tasarım onu farklı bir sonuca mı itmiştir?

### İçeriği düzenleyin ve dağınıklıkla savaşın

Düzenleme olmadan self servis, binlerce bayat, çoğaltılmış ve terk edilmiş pano üretir. Yaşam döngüsü yönetimini yerine koyun: kullanımı izleyin, kullanılmayan içeriği arşivleyin, kopyaları kaldırın ve kalanı düzenli aralıklarla yeniden onaylayın. Onaylı kataloğu bulunması kolay kılın; insanlar güvenilir içeriği yeniden kurmak yerine yeniden kullansın. Daha küçük, güvenilir ve iyi bakımlı bir pano kümesi, yayılmış bir mezarlıktan iyidir.

### Analitiği ve operasyonel raporlamayı gömün

Bütün analitik ayrı bir portala ait değildir. İlgili metrikleri ve raporları, insanların zaten çalıştığı operasyonel uygulamalara, örneğin CRM'e ([müşteri ilişkileri yönetimi](https://en.wikipedia.org/wiki/Customer_relationship_management) sistemi), vaka yönetimi sistemine ya da bilet aracına doğrudan gömün; böylece içgörü karar noktasına ulaşır. Sıkı gecikme ya da biçim gereksinimleri olan operasyonel raporlama (faturalar, ekstreler, düzenleyici beyannameler) için amaca yönelik raporlama kullanın. Etkileşimli panoları, kötü uyduğu bir işi yapmaya zorlamayın.

## Ödünleşimler: artılar ve eksiler

| Seçim | Artılar | Eksiler | En uygun olduğu yer |
|---|---|---|---|
| Merkezî BI takımı | Tutarlı, yönetilen, kalite denetimli | Darboğaz, yavaş tepki | Düzenlenen raporlama |
| Self servis BI | Hızlı, ölçeklenebilir, kullanıcıları güçlendirir | Dağınıklık, tutarsız metrikler | Geniş keşif |
| Anlamsal katman | Tek doğru, yeniden kullanılabilir, yönetilen | Baştan modelleme ve bakım | Küçük ölçeğin ötesindeki her kurum |
| Gömülü analitik | Karar noktasında içgörü | Mühendislik maliyeti, yönetmesi daha zor | Operasyonel iş akışları |
| Zengin panolar | Kapsamlı görünüm | Bunaltıcı, düşük eyleme dönüşme oranı | Nadiren ideal |
| Odaklı panolar | Kararları yönlendirir | Editoryal disiplin gerektirir | Çoğu kullanım |

Temel gerilim, erişim ile tutarlılık arasındadır. BI'ı merkezî bir takımın içine kilitlemek tutarlı sayıları garanti eder, ama kurumu zamanında cevaplardan yoksun bırakır ve gölge elektronik tablolar doğurur. Tam self servis herkesi güçlendirir, ama çelişen metrikleri ve bayat içeriği çoğaltır. Bir taraf seçmek zorunda değilsiniz. Geniş self servis erişimi, yönetilen bir anlamsal katman ve onayla birleştirin; insanlar keşfetmekte özgür olurken önemli sayılar tekil ve güvenilir kalır.

## Takımınızla tartışılacak sorular

1. **Bir anlamsal katmana yatırım yaptınız mı ve her onaylı metriği, bir sahibi, bir tanımı ve bir değişiklik günlüğü olan bir API gibi yönetiyor musunuz?** Bölümün merkezî fikri, her aracın, defterin ve gömülü raporun hesaplama yaptığı, her metriğin yönetilen tek bir tanımıdır; bu, üç panonun üç gelir rakamı göstermesi gibi klasik sorunu ortadan kaldırır. Yönetim kurulu sunumları ve düzenleyici beyannameleri tek bir rakama bağlı olan kurumsal şirketler ve kamuya açık yayınları iç sayılarla eşleşmek zorunda olan kurumlar için, ayrışan bir metrik doğrudan bir yükümlülüktür. Ödünleşim gerçektir: anlamsal katman baştan modelleme ve süregelen bakım ister. Kanıt getirin: en önemli metriğinizin bugün kaç tanımı olduğunu ve bir uzlaştırmanın şu anda kaç analist saatine mal olduğunu sayın. Sayı birden büyükse anlamsal katman kendini amorti eder ve metrikleri sahipler ve değişiklik günlükleriyle yönetmek onu zaman içinde tekil tutar.

2. **Self servis özgürlüğü ile metrik dağınıklığı arasındaki çizgi nerede ve hangi korkuluklar kolay yolu yönetilen yol olarak tutar?** Bölüm, kilitli merkezî BI ile sınırsız self servis arasında seçim yapmamanız gerektiğini savunur: merkezî takımlar insanları elektronik tablolara iten darboğazlara dönüşür, tam self servis ise çelişen metrikleri ve bayat panoları çoğaltır. Çözüm, onaylı veri kümeleri, anlamsal katman, şablonlar ve net içerik kademeleri (onaylı, takım destekli, kişisel) üzerine kurulu geniş erişimdir; böylece keşif resmî gerçeklik gibi görünmez. Somut işaretler getirin: kaç pano var, kaçı gerçekten kullanılıyor ve tüketiciler güvenilir içeriği deneylerden ayırt edebiliyor mu. İnsanlar ayırt edemiyorsa onay ve yaşam döngüsü yönetimi (kullanımı izlemek, kullanılmayanı arşivlemek, kalanı yeniden onaylamak) kalıcı uygulama olmalıdır; çünkü daha küçük güvenilir bir küme, yayılmış bir mezarlıktan iyidir.

3. **Grafikleriniz incelemeden sağ çıkacak kadar dürüst mü ve tasarımın verinin gerçekten haklı kıldığı sonucu desteklediğini kim kontrol ediyor?** Bölüm net bir sınav koyar: bilgili bir izleyici verinin desteklediği sonuca mı varır, yoksa tasarım onu başka yere mi itmiştir? Kısaltılmış eksenler, sahte korelasyon üreten çift eksenler ve 3 boyutlu pastalar adı konmuş tuzaklardır. Vatandaşlara yönelik kamu yayınları ve düzenlenen beyannameler için masum biçimde yanıltıcı bir grafik, kamu güvenini aşındırır ya da bir bulguya davetiye çıkarır; yani buradaki dürüstlük yalnızca bir zevk değil, bir yönetişim meselesidir. Kurumunuzda bir grafiğin izleyicisini yanılttığı bir örnek getirin ve yayımlanan içerikte uygulanan görselleştirme standartlarına (sıfırdan başlayan çubuk eksenleri, tutarlı ölçekler, gösterilen belirsizlik) ihtiyacınız olup olmadığına karar verin. Cevap, binanın dışına çıkan her şey için gözden geçirme beklentilerini belirlemelidir.

4. **Panolarınızdan hangileri gerçekten bir kararı değiştiriyor ve değiştirmeyeni emekliye ayırmak için ölçütünüz nedir?** Bölüm, bir panonun desteklediği kararla başlaması gerektiğinde ısrar eder; ama çoğu büyük kurum, izlenen ama hiç göre hareket edilmeyen, veriye dayalı kültürle karıştırılan gösteriş panoları biriktirir. Bu ölçekte önemlidir, çünkü her panonun gizli bir maliyeti vardır: bakımının yapılması, metriklerinin anlamsal katmanla tutarlı tutulması ve varlığının, gerçekten eyleme yol açan raporlardan dikkati dağıtması. Rakip çekim, insanların daha fazla görünürlükle kendini daha güvende hissetmesi ve hiçbir takımın panosunun arşivlenmesinden hoşlanmamasıdır. Kullanım telemetrisini (her panoyu kim açıyor, ne sıklıkla ve ardından herhangi bir eylem geliyor mu) ve en önemli panolarınızın hangi kararlara bilgi vermesi gerektiğine dair açık sözlü bir liste getirin. Kurumsal şirketler için bu portföy düzenlemesini ve lisans maliyeti denetimini besler; bir kamu kurumu için ise raporlama harcamasının kimsenin okumadığı ekranlar yerine ölçülebilir operasyonel değer üretip üretmediğine dair denetim sorularını da yanıtlar.

5. **Değer teşhiste, tahminde ve reçetede dururken geçmişi betimlemeye fazla mı yatırım yaptınız ve bir temel metriği bu merdivende yukarı ne taşırdı?** Bölüm dört analitik türünü (betimleyici, teşhis edici, öngörücü, reçeteleyici) çerçeveler ve çoğu kurumun, sonuçları gerçekten değiştiren teşhise ve eyleme az yatırım yaparken betimleyici panolar yığdığı konusunda uyarır. Büyük bir takım için betimlemede takılı kalmak, analistlerin zamanlarını herkesin zaten bildiğini yeniden raporlamakla geçirmesi, bunun neden olduğu ve bundan sonra ne yapılacağı gibi daha zor sorunun ise cevapsız kalması demektir. Gerilim, teşhis ve tahmin çalışmasının daha derin veri mühendisliği, model yönetişimi ve analist becerisi gerektirmesidir; bu yüzden bir pano daha finanse etmek daha kolaydır. Analitik çabanızın dört tür arasındaki mevcut dağılımını ve nedenlere inmenin ya da tahmin yapmanın bir kararı gözle görülür biçimde değiştireceği bir metriği getirin. Bir kurumsal şirkette bu, analitiği marj ve riskle ilişkilendirir; bir kamu kurumunda ise öngörücü ve reçeteleyici çalışmalar (örneğin bir hizmete olan talebi tahmin etmek), vatandaşlarla ilgili kararlara bilgi vermeden önce açıklanabilirlik ve adalet güvencelerini de taşımalıdır.

6. **İçgörünün insanların zaten çalıştığı araçların içine nerede ulaşması gerekiyor ve nerede bir pano yerine amaca uygun operasyonel raporlama kullanmalısınız?** Bölüm etkileşimli BI'ı gömülü analitikten ve faturalar, ekstreler ve düzenleyici beyannameler gibi amaca yönelik operasyonel raporlamadan ayırır; bir panoyu kötü uyduğu bir işi yapmaya zorlamaya karşı uyarır. Bu, büyük takımlar için önemlidir, çünkü ön saftaki personel ayrı bir BI portalına danışmak için nadiren CRM'inden ya da vaka yönetimi sisteminden çıkar; bu yüzden yalnızca bir portalda yaşayan içgörü karar anında kullanılmadan kalır. Rakip düşünceler mühendislik maliyeti ve yönetişimdir: metrikleri operasyonel uygulamalara gömmek kurması daha zor ve onaylı tanımlarla tutarlı tutması daha zordur; piksel mükemmelliğindeki raporlama ise pano aracının garanti edemeyeceği sıkı gecikme ve biçim ister. Kararların gerçekte nerede alındığına ve hangilerinin şu anda birinin sayıyı bulmak için araç değiştirmesini gerektirdiğine dair bir harita getirin. Bir kurumsal şirket için bu, mühendislik çabasını nereye yatıracağını şekillendirir; bir kamu kurumu için ise yasal beyannameler ve vatandaşa dönük ekstrelerin çoğu zaman amaca yönelik raporlamayı isteğe bağlı değil zorunlu kılan yasal biçim ve saklama kuralları vardır.

## Sektör merceği

**Girişim.** Birkaç çekirdek metriğinizi, hafif bir araçta bile olsa bir kez tanımlayın; böylece yönetim kurulu sunumu ve ürün panosu asla ayrışmaz. Ağır bir anlamsal katman platformunu atlayın: takım küçükken tek bir ortak tanım kaynağı ve güvenilir panoların kısa bir listesi yeter. Burada hız, cilalamadan önemlidir; bu yüzden inşa etmeniz gereken herhangi bir şeyden çok, ambarınıza bugün yönlendirebileceğiniz barındırılan bir BI aracını tercih edin.

**Küçük işletme.** Özel bir BI uzmanınız yoksa ayrı bir platform kurmak yerine CRM'iniz ya da muhasebe yazılımınız gibi sahip olduğunuz araçlara zaten gömülü analitiğe yaslanın. Seçimi satın al ya da kur diye çerçeveleyin ve varsayılan olarak satın almanın kazanmasına izin verin; riskiniz herkesin farklı bir "gelir" sayısı taşıdığı bir elektronik tablo kültürüdür, bu yüzden önemli olan birkaç tanım üzerinde anlaşın ve yazın. Onaylı raporların paylaşılmasını kolay, yanlışlıkla çatallanmasını zor kılan araçları tercih edin.

**Kurumsal.** Temel sorun birçok takım arasında tutarlılıktır: yönetilen bir anlamsal katmana yatırım yapın, güvenilir içeriği onaylayın ve pano dağınıklığını sahipleri, kullanım takibi ve yeniden onayı olan sürekli bir yaşam döngüsü olarak yönetin. Her onaylı metriğe bir tanımı, sahibi ve değişiklik günlüğü olan bir API gibi davranın ve onaylı içeriği deneysel olandan ayırın; self servis resmî gerçeklik gibi görünmesin. Modelleme ve düzenleme çabasını açıkça bütçeleyin, çünkü ölçekte alternatif, analistlerin ayrışan sayıları süresiz uzlaştırmasıdır.

**Kamu.** Yayımlanan rakamlar iç rakamlarla eşleşmeli ve kamusal ve yasama denetiminden sağ çıkmalıdır; bu yüzden yönetilen bir anlamsal katman ve uygulanan görselleştirme standartları (sıfırdan başlayan eksenler, dürüst ölçekler, gösterilen belirsizlik) incelik değil hesap verebilirlik gereksinimleridir. Satın alma kuralları hangi BI araçlarını alabileceğinizi kısıtlayabilir ve veri taşınabilirliği talep edebilir; bu yüzden tek bir tedarikçinin tescilli metrik mantığına kilitlenmekten kaçının. Onaylı kamuya açık yayınları deneysel analizden ayrı tutun ve vatandaşlara, bilgili bir izleyicinin verinin gerçekten haklı kıldığı sonuca varacağı kadar dürüst grafikler verin.

## Örnekler

**Girişim.** Erken aşamadaki bir pazar yerinde iki kurucu, "aylık gelir" için ayrı elektronik tablolar tutuyordu ve yönetim kurulu sunumunu hazırlarken sayılar hiçbir zaman tam tutmuyordu. Metriği küçük bir anlamsal katmanda bir kez tanımladılar, tek bir BI aracını ona yönlendirdiler ve kısa bir pano listesini herkesin kullanması gereken güvenilirler olarak işaretlediler. Raporlama, bir pazar gecesi uzlaştırmasından, güvenle açabilecekleri bir bağlantıya dönüştü.

**Kurumsal.** Bir telekomünikasyon şirketi, finans, pazarlama ve operasyonun her birinin farklı "aktif abone" sayıları bildirmesinden muzdaripti. Her çekirdek metriği bir kez tanımlayan bir anlamsal katman getirdi, panoları ondan hesaplayacak biçimde taşıdı ve binlerce bayat panoyu arşivlerken seçilmiş güvenilir raporlar kümesini onayladı. Yönetim kurulu raporlaması bir uzlaştırma alıştırması olmaktan çıktı ve insanlar sayılara güvendiği için self servis benimsemesi arttı.

**Kamu.** Bir halk sağlığı dairesi, yönetilen bir anlamsal katmandan beslenen onaylı panolar kurdu; böylece vaka sayıları ve oranları iç karar almada ve kamuya açık yayınlarda aynı biçimde hesaplanıyor. Görselleştirme standartları, vatandaşlara yayımlanan grafikleri dürüst tutuyor (sıfırdan başlayan eksenler, net belirsizlik bantları) ve bu, kamu güvenini koruyor. Gömülü raporlar, yerel metrikleri ön saftaki personelin zaten kullandığı vaka yönetimi araçlarının içinde görünür kılıyor.

## İş gerekçesi: motivasyonlar, YG ve TSM

İyi işletilen analitik ve BI'ın YG'si, daha hızlı ve daha iyi kararlardan ve israfı kesmekten gelir. İnsanlar tek bir sayı kümesine güvendiğinde toplantılar kimin elektronik tablosunun doğru olduğuna dair tartışmalar olmaktan çıkar, ne yapılacağına dair konuşmalara dönüşür. Self servis, merkezî takımlardaki birikmiş işi azaltır ve anlamsal katman, ayrışan metrikleri uzlaştırmanın yinelenen maliyetini önler. Dürüst, karar odaklı panolar içgörünün eyleme dönüşme oranını yükseltir.

Benimseme maliyeti BI platformu lisanslamasını, anlamsal katmanı kurma ve sürdürmeyi, düzenleme çabasını ve eğitimi içerir. Bunu benimsememenin maliyetiyle tartın: çelişen rakamları uzlaştırmak için saatler harcayan analistler ve yöneticiler, yanıltıcı grafiklere dayanarak verilen kararlar, bakımsız panoların birikmesi ve kamusal ortamlarda yayımlanan sayılar birbiriyle çeliştiğinde aşınan güven. Liderliğe argüman basittir. Yönetilen bir anlamsal katman artı düzenlenmiş self servis, verinin herkesin güvendiği bir varlık olmasıyla sürekli bir kafa karışıklığı ve yeniden iş kaynağı olması arasındaki farktır.

## Anti-kalıplar ve tuzaklar

- Her takımın temel metrikleri kendi yöntemiyle hesaplayıp çelişen sayılar üretmesi.
- Bir kararı desteklemek yerine her şeyi göstermek için kurulan panolar.
- Sonuçları çarpıtan yanıltıcı grafikler (kısaltılmış eksenler, çift eksenler, 3 boyutlu pastalar).
- Self servisi yönetişimi tamamlamak yerine onun yerine koymak.
- Yaşam döngüsü yönetimi olmayan, binlerce bayat, çoğaltılmış pano.
- Kimsenin göre hareket etmediği, veriye dayalı kültürle karıştırılan gösteriş panoları.
- Etkileşimli BI'ı piksel mükemmelliğinde düzenleyici belgeler üretmeye zorlamak.
- Onay yok; tüketiciler güvenilir içeriği deneylerden ayırt edemiyor.

## Olgunluk modeli

1. **Düzey 1, Başlangıç.** Raporlar elektronik tablolarda tesadüfen kurulur, metrikler tutarsız tanımlanır ve grafikler çoğu zaman yanıltıcıdır. Anlamsal katman, onay ve düzenleme yoktur; bu yüzden ayrışan sayılar olağandır.
2. **Düzey 2, Geliştirme.** Bir BI aracı yerindedir ve bazı ortak panolar vardır, ama metrik tanımları takımlar arasında hâlâ ayrışır. Self servis denetimsizdir ve dağınıklık başlar; birkaç grup metrikleri özenle modelleyebilir, ama uygulama tutarsızdır ve kurum genelinde hiçbir şey zorunlu kılınmamıştır.
3. **Düzey 3, Standartlaştırma.** Bir anlamsal katman çekirdek metrikleri bir kez tanımlar, belgeler ve her araç ve raporda uygular. Onaylı içerik deneysel olandan ayrılır, self servis korkuluklar içinde işler, görselleştirme standartları yayımlanır ve içerik yaşam döngüsü yönetimi ara sıra yapılan bir temizlik değil, kalıcı bir uygulamadır.
4. **Düzey 4, Yönetme.** Analitik varlığı taban çizgilerine karşı ölçülür. Pano kullanımı izlenir, kullanılmayan içerik nicelendirilir ve belirli aralıklarla emekliye ayrılır; temel metriklerin ayrışan tanımlarının sayısı bire doğru izlenir; grafik gözden geçirme uyumu, self servis benimsemesi ve cevaba ulaşma süresi takip edilir; uzlaştırma maliyeti ve metrik değişikliği hazırlık süresi ölçülür, böylece onaylı tanımlardan sapma kanıta dayanarak yakalanır ve düzeltilir.
5. **Düzey 5, Orkestrasyon.** Metrikler sahipleri ve değişiklik günlükleri olan API'ler gibi yönetilir, analitik betimleyiciden reçeteleyiciye uzanır ve somut eyleme bağlanır, raporlar karar noktalarına gömülüdür. Kurum her yerde tek bir doğruluk sürümüne güvenir, dağınıklığı etkin biçimde sınırlar ve iş ile soruları değiştikçe analitiğini sürekli yeniden kapsamlandırıp yeniden onaylar.

## Tartışma fikirleri

- En önemli metriğinizin bugün kaç farklı tanımı var?
- Panolarınızdan hangileri gerçekten bir kararı değiştiriyor ve hangileri yalnızca izleniyor?
- Kurumunuzda bir grafik izleyicisini nerede, masumca ya da değil, yanılttı?
- Geçmişi betimlemeye, teşhis edip eyleme geçmeye kıyasla fazla mı yatırım yapıyorsunuz?
- İçerik için bir onay kademesi, kurumunuzda güveni ve yeniden kullanımı nasıl etkilerdi?
- Vatandaşların ya da düzenleyicilerin dürüst grafik ihtiyacı ile ikna edici olanlara doğru çekimi nasıl dengeliyorsunuz?

## Önemli çıkarımlar

- Her önemli metriği, her yerde kullanılan yönetilen bir anlamsal katmanda bir kez tanımlayın.
- Analitiği betimleyiciden teşhis edici, öngörücü ve reçeteleyiciye merdivenden yukarı taşıyın.
- Self servisi korkuluklar içinde etkinleştirin; güvenilir içeriği onaylayın.
- Panoları mevcut veri çevresinde değil, kararlar çevresinde tasarlayın.
- Her grafiği dürüst yapın; amaç ikna değil, anlamaktır.
- Acımasızca düzenleyin ve dağınıklıkla savaşmak için bayat içeriği emekliye ayırın.
- Analitiği karar noktasına gömün ve amaca uygun operasyonel raporlama kullanın.

## Kaynaklar ve ileri okuma

- Edward Tufte, "The Visual Display of Quantitative Information."
- Stephen Few, "Show Me the Numbers" and "Information Dashboard Design."
- Cole Nussbaumer Knaflic, "Storytelling with Data."
- Alberto Cairo, "How Charts Lie."
- Ralph Kimball and Margy Ross, "The Data Warehouse Toolkit."
- Darrell Huff, "How to Lie with Statistics."
- Benn Stancil and others, writings on the semantic layer and metrics stores.
