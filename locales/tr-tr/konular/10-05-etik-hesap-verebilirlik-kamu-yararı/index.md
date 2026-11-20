# 10.5 Etik, hesap verebilirlik ve kamu yararı

## Genel bakış ve motivasyon

Yazılım artık insan kararlarının arkasında duran tarafsız bir araç değil. Giderek kararın kendisi oluyor. Kimin kredi alacağına, bir işe alımcının hangi özgeçmişi göreceğine, bir yardım başvurusunun ne kadar süreceğine, bir sahtecilik uyarısının bir hesabı dondurup dondurmayacağına ve milyonlarca kişiye hangi bilginin ulaşacağına yazılım karar veriyor. Yazılım insanların haklarını, parasını, güvenliğini ve onurunu etkileyen kararlar verdiğinde ya da bu kararları şekillendirdiğinde, onu inşa eden mühendisler ve kurumlar doğruluk ve performansın ötesinde sorumluluklar üstlenir. Bu bölüm o sorumluluklarla ilgilidir: [meslek etiği](https://en.wikipedia.org/wiki/Professional_ethics), sistemlerin yaptıklarının hesabını verebilme, özellik değil yükümlülük olarak [erişilebilirlik](https://en.wikipedia.org/wiki/Web_accessibility) ve hakkaniyet, algoritmik şeffaflık, [sürdürülebilirlik](https://en.wikipedia.org/wiki/Sustainability) ve insanlara adaletle ve onurla hizmet etme görevi.

Büyük kurumlar için ölçek ve güç bahisleri yükseltir. Bir kurumsal ya da kamu sistemi tek bir kişiyi etkilemez. Milyonları etkiler. Tek bir tasarım tercihi (önyargılı bir eğitim kümesi, erişilemeyen bir form, şeffaf olmayan otomatik bir ret) hepsinde tekrarlanır. Hükümetlerin görevi daha da ağırdır, çünkü sistemleri isteğe bağlı değildir. Bir vatandaş vergi dairesi ya da yardım kurumu için rakip seçemez. Devletin bazı hizmetlerdeki tekeli, kötü kurulmuş bir sistemin insanları başka türlü kullanamayacakları haklardan yoksun bırakabileceği anlamına gelir. Bu erişimle birlikte adil, şeffaf ve hesap verebilir olma görevi de gelir.

Yazılımda etik çoğu zaman sona eklenen yumuşak bir konu olarak görülür ya da bir hukuki uyum kontrol listesine devredilir. Bu bölüm tersini savunur. Etik değerlendirmeler mühendislik gereksinimleridir. Hesap verebilirlik sonradan ileri sürülmez, baştan tasarlanır. İnsanlara onurla hizmet etmek hem ahlaki bir görevdir hem de zamanla büyük kurumların dayandığı güvenin temelidir.

## Temel ilkeler

- **Yazılım karar verir, bu yüzden yapanlar sorumluluk taşır.** Sisteminizin insanlara yaptıklarından siz sorumlusunuz; yalnızca belirtime uyup uymadığından değil.
- **Erişilebilirlik ve hakkaniyet yükümlülüktür, süs değil.** İnsanları dışlamak bir kusurdur ve çoğu zaman hukuki ve ahlaki bir başarısızlıktır.
- **Sonuç doğuran otomatik kararlar hesap verebilirlik gerektirir.** Otomatik bir karardan etkilenen insanlar açıklamayı, başvuru yolunu ve insan incelemesini hak eder.
- **Şeffaflık varsayılan, gizlilik istisnadır.** Özellikle kamu sektöründe insanların kendileri hakkındaki kararların nasıl verildiğini anlama hakkı vardır.
- **Adillik varsayılmaz, incelenir.** Siz bilerek kontrol etmedikçe sistemler verilerindeki ve tasarımlarındaki önyargıları devralır ve büyütür.
- **Onur bir tasarım gereksinimidir.** Savunmasızlar ve tipik olmayanlar dahil her kullanıcıya saygıyı hak eden bir insan olarak davranın.
- **Sürdürülebilirlik ve toplumsal etki önemlidir.** Yazılımın enerjisi, kaynakları ve toplumsal etkileri gerçek maliyetinin parçasıdır.

## Öneriler

### Meslek etiğini benimseyin ve yaşayın

Kurumu tanınmış bir meslek davranış kuralına dayandırın ve bunu süs olmaktan çıkarıp gerçek kılın. Mühendisler yalnızca işverenlerine değil, kamuya karşı da yükümlülükleri olduğunu anlamalıdır. Bir sistem insanlara zarar verdiğinde "ben sadece belirtimi izledim" bir savunma değildir. Etik kaygıları dile getirmek için gerçek kanallar oluşturun: "Bunu yapmamalıyız ya da bu şekilde yapmamalıyız" diyebilmenin kariyer bitiren bir cesaret gerektirmediği bir yol. Takımlara sonuçları tartacak sözcük dağarcığını ve itibarı verin. Bunu, etik itirazları engel değil değerli sinyal sayan bir liderlikle destekleyin. Etik eğitimi ancak kurum öğrettiğini görünür biçimde uyguluyorsa işe yarar.

### Erişilebilirliği ve hakkaniyeti yükümlülük sayın

İnsan yeteneklerinin ve koşullarının tüm aralığı için en baştan inşa edin. Erişilebilirliği sonradan eklemek çok daha pahalıdır ve çoğu zaman daha kötü sonuç verir. Yerleşik erişilebilirlik standartlarını (Web İçeriği Erişilebilirlik Yönergeleri olan [WCAG](https://en.wikipedia.org/wiki/Web_Content_Accessibility_Guidelines) gibi) izleyin ve birçok yargı bölgesinde kamu hizmetleri için bunları zorunlu kılan yasal gereklilikleri karşılayın. [Yardımcı teknolojilerle](https://en.wikipedia.org/wiki/Assistive_technology) ve her şeyden önce engelli gerçek kullanıcılarla test edin. Hakkaniyeti engelliliğin ötesine, hizmet verdiğiniz tüm nüfusa yayın: düşük bant genişliğindeki, eski cihazlardaki, sınırlı [dijital okuryazarlığa](https://en.wikipedia.org/wiki/Digital_literacy) sahip, azınlık dillerini konuşan ve zor yaşam koşullarındaki insanlar. İnsanların vazgeçemeyeceği hizmetlerde (özellikle kamu hizmetlerinde) yalnızca kendinden emin, bağlantılı, tipik kullanıcı için tasarım yapmak makul bir varsayılan değil, hizmet etmekte başarısızlıktır.

### Algoritmik hesap verebilirlik ve kamusal şeffaflık kurun

İnsanlar hakkında sonuç doğuran kararlar veren ya da bunları ciddi biçimde şekillendiren her sistem için hesap verebilirliği tasarıma katın. Yüksek riskli kararlarda otomatik çıktıya körü körüne uymak yerine insanları anlamlı biçimde [döngünün içinde](https://en.wikipedia.org/wiki/Human-in-the-loop) tutun. Bir kararın neden verildiğini, etkilenen kişinin anlayacağı terimlerle açıklayabilin. Ona itiraz etmek ve bir insana ulaşmak için gerçek bir yol sağlayın. Sistemleri korunan ve savunmasız gruplar arasında [önyargı](https://en.wikipedia.org/wiki/Algorithmic_bias) ve [orantısız etki](https://en.wikipedia.org/wiki/Disparate_impact) açısından, devreye almadan önce ve devredeyken test edin ve zaman içindeki kaymayı izleyin. Kamu sektöründe algoritmik sistemlerin nasıl çalıştığını (amaçlarını, verilerini ve mantıklarını uygun düzeyde) algoritma kayıtları gibi mekanizmalarla yayımlayın; böylece vatandaşlar ve denetim organları onları inceleyebilir. Sistemlerin uygun olmayan yerlerde kullanılmaması için amaçlanan kullanımı ve bilinen sınırlılıkları belgeleyin.

### Adillik, onur ve başvuru yolu için tasarlayın

Sistemlerinizi insanlara haksız ya da onursuz davranabilecekleri yollar açısından inceleyin. Eğitim verilerini ve kuralları gömülü önyargı açısından mercek altına alın. Yalnızca verimlilik için optimize edilmiş bir sistemin acımasız olabileceğini unutmayın: yanlış negatifleri en aza indirmek için ayarlanmış bir sahtecilik filtresi, her biri sıkıntı içindeki gerçek bir insan olan binlerce masum kişinin hesabını dondurabilir. Başarısızlık durumlarını etkilenen kişinin bakış açısından tasarlayın. Sistem yanlış olduğunda ne olur? Bir insana, bir açıklamaya ve bir çözüme ne kadar kolay ulaşabilirler? [Kişisel verileri](https://en.wikipedia.org/wiki/Personal_data) saygıyla ve ölçülülükle ele alın: yalnızca gerekeni toplayın ve kullanımı konusunda dürüst olun. Hatayı, gecikmeyi ve reddi uç durumlar olarak değil, onurun en çok risk altında olduğu anlar olarak görün.

### Sürdürülebilirliği ve toplumsal sorumluluğu hesaba katın

Yazılımın fiziksel ve toplumsal maliyetleri olduğunu kabul edin. Veri merkezleri, eğitim çalıştırmaları ve verimsiz sistemler gerçek enerji tüketir. Verimlilik mali olduğu kadar çevresel bir erdemdir. İnşa ettiklerinizin daha geniş etkilerini (emek, kamusal tartışma ve savunmasız gruplar üzerindeki etkileri) düşünün ve zararları faydalarını aşan işleri reddetmeye ya da yeniden şekillendirmeye istekli olun. Sistemleri toplumu ölçekte şekillendiren büyük kurumlar için toplumsal sorumluluk, işin yanında yürüyen bir hayırseverlik değildir. Sorumlu inşanın parçasıdır ve giderek bir mevzuat ve kamuoyu beklentisi meselesidir.

## Ödünleşimler: artılar ve eksiler

| Gerilim | Bir yan | Diğer yan |
|---|---|---|
| Otomasyon ve insan yargısı | Ölçek, tutarlılık, hız, düşük maliyet | Hesap verebilirlik, incelik, merhamet, başvuru yolu |
| Şeffaflık ve koruma | Kamusal inceleme, güven, denetim | Oyunlama riski, güvenlik, verinin gizliliği |
| Erişilebilirlik yatırımı ve hız | Herkese hizmet eder; yasal ve ahlaki uyum | Daha yavaş ilk teslimat; daha fazla tasarım çabası |
| Verimlilik ve adillik | Optimize sonuçlar; düşük maliyet | Kuyruk uçlarındaki bireylere acımasızlık riski |
| Veri zengini kişiselleştirme ve gizlilik | Daha iyi hizmet; uyarlanmış deneyim | Gözetim riski; onur ve rıza kaygıları |
| Yenilik hızı ve ihtiyat | Daha hızlı değer; rekabet avantajı | Ölçekte devreye alınan incelenmemiş zararlar |

En zor ödünleşim ölçek ile bireysel adalet arasındadır. Otomasyon milyonlar boyunca tutarlılık ve verimlilik sağlar. Ama hataları da ölçekte teslim edilir ve toplam için optimize edilmiş bir sistem, kuyruk uçlarındaki bireylere sessizce acımasız olabilir. Cevap otomasyondan vazgeçmek değildir. Bireysel başarısızlık durumu için tasarlamaktır: riskin yüksek olduğu yerde insanları döngüde tutun, açıklamayı ve başvuru yolunu güvence altına alın ve sistemin etkisini yalnızca ortalamada değil, en az hizmet alanlar üzerinde ölçün. Şeffaflıkta da gerçek bir gerilim vardır, çünkü tam açıklık oyunlamaya yol açabilir ve özel verileri açığa çıkarabilir. Ama kamu hizmetlerinde cevap güçlü biçimde varsayılan olarak açıklamadan yanadır; yalnızca gerçekten korunması gerekenler muaf tutulur, opaklık güvenli varsayılan sayılmaz.

## Takımınızla tartışılacak sorular

1. **Hangi sistemleriniz insanlar hakkında sonuç doğuran kararlar veriyor ya da bunları ciddi biçimde şekillendiriyor ve her biri bugün açıklama, insan incelemesi ve başvuru yolu sunuyor mu?** Yazılım giderek kararın kendisi oluyor: kimin kredi alacağı, hangi özgeçmişin görüleceği, bir hesabın dondurulup dondurulmayacağı, bir başvurunun ne kadar süreceği. Bu tür her sistem için etkilenen kişi anlayabileceği bir açıklamayı, itiraz etmek için gerçek bir yolu ve devreye girebilecek bir insanı hak eder; kurumsal ya da kamu ölçeğinde tek bir tasarım kusuru milyonlarca kişide tekrarlanır. Kanıt getirin: sonuç doğuran otomatik kararlarınızın envanterini çıkarın ve her biri için haksız muamele gören bir kişinin gerçekten bir insana ulaşıp sade dilde bir gerekçe alıp alamayacağını kontrol edin. Cevap hayırsa bu, sonra eklenecek bir özellik değil, düzeltilecek bir kusurdur. İnsanların vazgeçemeyeceği hizmetlerde, özellikle kamu hizmetlerinde, bu bir incelik değil yükümlülüktür.

2. **Erişilebilirliği, engelli gerçek kullanıcılarla test edilen ve yayını durduran bir gereksinim olarak ele alıyor musunuz ve şu anda kimi başarısızlığa uğratıyorsunuz?** Erişilebilirlik ve hakkaniyet yükümlülüktür; insanları dışlamak bir kusurdur, çoğu zaman hukuki ve ahlaki bir başarısızlıktır. Yine de erişilebilirliği sonradan eklemek, ilk ekrandan itibaren tasarlamaktan güvenilir biçimde daha yavaş, daha pahalı ve daha kötüdür. WCAG'i izleyin ve otomatik kontrollerin ötesine geçerek yardımcı teknolojilerle ve engelli gerçek kullanıcılarla, ayrıca düşük bant genişliğindeki, eski cihazlardaki, azınlık dillerini konuşan ve sınırlı dijital okuryazarlığa sahip insanlarla test edin. Kanıt getirin: en önemli akışınızı bir ekran okuyucuyla ve kısıtlanmış bir bağlantıda çalıştırın ve nerede bozulduğunu görün. Cevap, erişilebilirliğin yayını engelleyen bir kapı mı yoksa hiç yükselmeyen bir iş listesi kalemi mi olduğuna karar vermelidir ve insanların vazgeçemeyeceği hizmetlerde savunulabilir olan yalnızca kapıdır. Yalnızca kendinden emin, bağlantılı, tipik kullanıcı için tasarım yapmak hizmet etmekte başarısızlıktır.

3. **Sonuç doğuran sistemleri devreye almadan önce ve devredeyken önyargı ve orantısız etki açısından test etmek için kalıcı süreciniz nedir?** Sistemler, siz bilerek kontrol etmedikçe verilerindeki ve tasarımlarındaki önyargıları devralır ve büyütür; kimse haksızlık amaçlamadı diye adaleti varsaymak ihmal yoluyla önyargıdır. Yanlış negatifleri en aza indirmek için ayarlanmış bir sahtecilik filtresi, her biri sıkıntı içindeki gerçek bir insan olan binlerce masum hesabı dondurabilir; yani adalet gözetilmeden optimize edilen verimlilik sessizce acımasız olabilir. Kanıt getirin: insanları etkileyen her model için korunan ve savunmasız gruplar arasındaki orantısız etki testini, belgelenmiş verileri ve bilinen sınırlılıkları, nüfus değiştikçe yeniden test eden kayma izlemesini gösterin. Cevap, önyargı testini tek seferlik bir lansman öncesi onay kutusu yerine rutin ve sürekli hale getirmeli ve optimizasyon hedefinizi yalnızca toplam doğruluğu değil, bireylere verilen zararı da tartacak biçimde değiştirmelidir. Başarısızlık durumunu etkilenen kişinin bakış açısından tasarlayın.

4. **Bir mühendis bir şeyi inşa etmemeniz gerektiğine ya da bu şekilde inşa etmemeniz gerektiğine inandığında, bu itirazın başına gerçekte ne geliyor?** Etik ancak "bunu yayınlamamalıyız" cümlesi kariyer bitirmeden söylenebilir olduğunda gerçek olur ve ölçekte bir zarara en yakın kişi çoğu zaman odadaki en kıdemsiz kişidir. Rakip baskı teslimattır: dile getirilen bir itiraz bir yol haritasını yavaşlatır ve teslim tarihi baskısındaki liderler onu değerli sinyal yerine engel sayabilir. Kanıt getirin: bir mühendisin kullanacağı kanalı tam olarak adlandırın, geçen yıl kaç kaygının dile getirildiğini sayın ve sonucunda neyin değiştiğini izleyin, çünkü işi hiç durdurmamış ya da yeniden şekillendirmemiş bir kanal süstür. Kurumsal ya da kamu kuruluşu için kanalı adı konmuş bir sahibe ve belgelenmiş bir incelemeye bağlayın; çünkü kimsenin dinlemekle yükümlü olmadığı bir itirazı kimse dile getirmeyi göze almaz ve zarar o zaman önce bir kamusal skandal olarak yüzeye çıkar.

5. **Çalıştırdığınız şeylerin çevresel ve toplumsal maliyetini biliyor musunuz ve zararları faydalarını aşan işi yeniden şekillendirir ya da reddeder miydiniz?** Yazılımın fiziksel ve toplumsal maliyetleri vardır: veri merkezleri, eğitim çalıştırmaları ve verimsiz sistemler gerçek enerji tüketir ve emek, kamusal tartışma ve savunmasız gruplar üzerindeki ikinci derece etkiler bir sistemin gerçek maliyetinin parçasıdır. Gerilim şudur: bu maliyetleri ölçmek ve azaltmak özellik hızıyla yarışır ve zararlı işi geri çevirmek, birinin hesabını vermekle yükümlü olduğu geliri gözden çıkarmak demektir. Kanıt getirin: en büyük sistemlerinizin enerji ya da hesaplama ayak izini, aşağı akış etkilerini kimin taşıdığına dair dürüst bir okumayı ve bu gerekçelerle işi yeniden şekillendirdiğiniz ya da reddettiğiniz en az bir somut vakayı. Sistemlerinizin toplumu şekillendirdiği kurumsal ya da kamu ölçeğinde bunu işin yanına eklenmiş bir hayırseverlik olarak değil, sorumlu inşanın ve giderek bir mevzuat ve kamuoyu beklentisi meselesinin parçası olarak görün.

6. **Dışarıdan biri sonuç doğuran sistemlerinizin nasıl karar verdiğini gerçekte ne kadar öğrenebilir ve açıklama sizin varsayılanınız mı yoksa istisnanız mı?** Şeffaflık, kamu güveninin kazanıldığı ya da kaybedildiği yerdir; çünkü insanların kendileri hakkındaki kararların nasıl verildiğini anlama hakkı vardır ve kamu sektöründe bu hak sıklıkla yasadır. Gerçek karşı baskı, tam açıklığın oyunlamaya yol açabilmesi ve özel verileri açığa çıkarabilmesidir; bu yüzden asıl soru açıklayıp açıklamamak değil, çizgiyi nereye çekeceğinizdir. Kanıt getirin: her sonuç doğuran sistem için neyi yayımladığınızı (amaç, veri ve mantık, uygun düzeyde), neyi ve hangi özel nedenle sakladığınızı ve teknik bir açıklamanın yanında sade dilde bir açıklama olup olmadığını gösterin. Bir kamu kurumu için algoritma kaydı gibi bir mekanizmayı dar ve savunulabilir muafiyetlerle karşılaştırın ve açıklamalarınızın gerçekten açıkladığını, teknik olarak bilgilendirip etkilenen kişiye hiçbir şey söylemediğini kontrol edin.

## Sektör merceği

**Girişim.** Birkaç kişi ve az bir pistle bir etik kurulu çalıştıramazsınız; bu yüzden ucuz, yüksek kaldıraçlı alışkanlıkları ürünün içine gömün: her otomatik retteki sade dilde gerekçe, bir insana ulaşmak için tek tıklık yol ve sonradan eklemek daha yavaş ve daha kötü olacağı için ilk ekrandan itibaren erişilebilir formlar. Yazılımınızın bir insan hakkında sonuç doğuran karar verdiği tek yeri seçin ve zararı ölçeklemeden önce açıklamayı ve başvuru yolunu orada doğru kurun. Adaleti ve onuru sonraki cilalama olarak değil, lansman gereksinimleri olarak ele almak şimdi az maliyetlidir ve erken dönemde kaybetmeyi göze alamayacağınız bir itibardan sizi korur.

**Küçük işletme.** Büyük olasılıkla erişilebilirlik ya da adalet uzmanınız yok ve bütçeniz dar; bu yüzden satın aldığınız araçlara gömülü etiğe yaslanın: WCAG'i karşılayan, otomatik özelliklerinin nasıl karar verdiğini belgeleyen ve döngüde bir insan tutmanıza izin veren tedarikçiler seçin. Kendi görevinizi bir veri hijyeni ve onur meselesi olarak çerçeveleyin: elinizde hangi kişisel verilerin olduğunu bilin, yalnızca ihtiyacınız olanı toplayın ve yanlış bir otomatik cevabın bir müşteriyi size ulaşamaz halde bırakmadığından emin olun. Eksikliği bir şikayetten sonra keşfetmek yerine, imzalamadan önce tedarikçilerden erişilebilirlik ve önyargı duruşlarını göstermelerini isteyin.

**Kurumsal.** Ölçekte sorun birçok takım boyunca yönetişimdir: sonuç doğuran kararın ne sayıldığına dair paylaşılan bir standart, tutarlı erişilebilirlik ve önyargı testi kapıları ve açıklamanın, insan incelemesinin ve başvuru yolunun olması gereken yerde var olduğunu kanıtlayan bir denetim izi. Hiçbir şeyi değiştirmeyen bir eğitim yerine yayını durduran bir etik inceleme kurun, erişilebilirlik ve orantısız etki çalışmasını açıkça bütçeleyin ve devredeki modelleri kayma için izleyin; böylece adillik tek seferlik bir onay kutusu değil sürekli olur. Tek bir tasarım kusurunu milyonlarca kişide tekrarlanmış sayın, çünkü erişiminizde öyledir.

**Kamu.** Satın alma kuralları, şeffaflık görevleri ve kamusal hesap verebilirlik her tercihi şekillendirir ve vatandaşlar bir rakibe giderek hizmetinizden vazgeçemez. Sonuç doğuran sistemlerin nasıl çalıştığını algoritma kaydı gibi bir mekanizmayla yayımlayın, tedarikçilerden sözleşmeyle veri uygulamalarını ve bilinen sınırlılıkları açıklamalarını isteyin ve her kamu hizmetini engelli kullanıcılarla, düşük bant genişliğiyle ve azınlık dili konuşanlarla test edilen erişilebilirlik standartlarına göre inşa edin. Sonuç doğuran her otomatik karar için insan incelemesi hakkını ve sade dilde bir açıklamayı güvence altına alın ve hesap verebilir bir görevlide kalması gereken nihai kararları tam otomasyonun dışında tutun.

## Örnekler

**Girişim.** Otomatik kredi özelliği geliştiren üç kişilik bir fintek girişimi, adaleti ve onuru sonraki cilalama değil, gereksinim sayar. Lansmandan önce modeli ölçebildikleri gruplar arasında orantısız etki açısından test eder, kullandığı verileri ve nerede güvenilmemesi gerektiğini yazıya döker ve reddedilen her başvuru sahibinin sade dilde bir gerekçe ve bir kurucuya ulaşmak için tek tıklık bir yol almasını sağlar. Kayıt akışını ilk ekrandan itibaren erişilebilirlik standartlarına göre kurarlar, çünkü sonradan eklemek daha yavaş ve daha kötü olurdu; ayrıca hızlı bir geçersiz kılma kanalı eklerler; böylece yanlışlıkla dondurulmuş bir hesap, gerçek bir insanı ortada bırakmak yerine dakikalar içinde açılabilir.

**Kurumsal.** Otomatik kredi kararı devreye alan bir banka adaleti bir mühendislik gereksinimi olarak ele alır. Lansmandan önce modeli korunan gruplar arasında orantısız etki açısından test eder, verileri ve sınırlılıklarını belgeler ve bir açıklama olanağı kurar; böylece reddedilen her başvuru sahibi anlaşılır bir gerekçe ve insan incelemesine giden net bir yol alır. Bir izleme süreci, nüfus değiştikçe kaymayı izler ve önyargıyı yeniden test eder. Sahtecilik tespit sistemi çok sayıda meşru hesabı dondurmaya başladığında banka hızlı bir insan inceleme kanalı ekledi ve optimizasyon hedefini müşteri zararını tartacak biçimde değiştirdi. Yanlış işaretlenen müşterilerin sıkıntısını kabul edilebilir bir istatistik değil, gerçek bir maliyet saydı.

**Kamu.** Bir şehir yönetimi bir algoritma kaydı yayımlar. Kayıt, şehrin kamu hizmetlerinde kullandığı otomatik sistemleri listeler ve her sistemin amacını, dayandığı verileri ve kararlara nasıl itiraz edilebileceğini anlatır. Şehrin dijital hizmetleri erişilebilirlik standartlarına göre inşa edilir ve engelli kullanıcılarla, düşük bant genişliğiyle ve azınlık dili konuşanlarla test edilir; ilke, insanların vazgeçemeyeceği bir hizmetin herkes için çalışması gerektiğidir. Sonuç doğuran her otomatik karar, insan incelemesi hakkını ve sade dilde bir açıklamayı taşır; böylece devletin yazılımı hayatları hakkında bir şeye karar verdiğinde vatandaşlar hem onuru hem başvuru yolunu korur.

## İş gerekçesi: motivasyonlar, YG ve TSM

Etik ve hesap verebilirlik için iş gerekçesi güvene, riske ve erişime dayanır. Güven kalıcı varlıktır. Sistemleri insanlara adil ve şeffaf davranan kurumlar, insanların onları kullanmaya istekli olmasını sağlayan güveni kazanır ve özellikle kamu kurumları, tek bir yüksek profilli haksız sistemin parçalayabileceği meşruiyete bağımlıdır. Risk yakın vadenin itici gücüdür. Önyargılı, erişilemeyen ya da şeffaf olmayan sistemler giderek düzenleyici cezalar, davalar ve sorumlu inşanın maliyetini gölgede bırakabilecek itibar zararı taşır. Erişim ikisini de büyütür. Kurumsal ya da kamu ölçeğinde tek bir etik başarısızlık milyonlarca kişide tekrarlanır ve manşet olur.

Benimseme maliyeti gerçektir. Erişilebilirlik çalışması, önyargı testi, açıklama ve başvuru mekanizmaları, döngüde insan incelemesi ve sonuçları düşünmek için tasarım zamanı, özellikle başta, çabayı artırır. Benimsememenin maliyeti daha büyüktür ve giderek isteğe bağlı olmaktan çıkıyor: ayrımcılık sorumluluğu, hizmet vermekle yükümlü olduğunuz nüfusun büyük bölümünün dışlanması, erişilebilirliği ve hesap verebilirliği lansmandan sonra sonradan eklemenin gideri ve bir kez kaybedildiğinde yeniden kurulması pahalı ve yavaş olan güven aşınması. Liderliğe gerekçeyi sunarken etiği fedakârlık olarak değil, risk yönetimi ve güven inşası olarak çerçeveleyin. [Algoritmik hesap verebilirlik](https://en.wikipedia.org/wiki/Algorithmic_accountability) ve erişilebilirlik çevresinde sıkılaşan düzenleyici ortama dikkat çekin. Toplam sahip olma maliyetini vurgulayın: baştan sorumlu inşa etmek, ölçekte insanlara zaten zarar vermiş bir sistemi düzeltmekten çok daha ucuzdur. Kamu kurumları için en sade argümanı ekleyin: vatandaşlara adil hizmet etmek görevin kendisidir, ona konmuş bir kısıt değil.

## Anti-kalıplar ve tuzaklar

- **Onay kutusu olarak etik.** Sistemlerin gerçekte nasıl inşa edildiğini hiç değiştirmeyen tek seferlik bir inceleme ya da eğitim.
- **Erişilebilirliği sonradan eklemek.** Erişilebilirliği geç bir eklenti olarak ele almak; tasarıma katmaktan daha kötü ve pahalı sonuçlar verir.
- **Hesap verilmeyen algoritma.** Açıklaması, insan incelemesi ve itiraz yolu olmayan sonuç doğuran otomatik kararlar.
- **Acımasızlığa optimize etmek.** Sistem kuyruk uçlarındaki insanlara sessizce zulmedene kadar yalnızca toplam verimlilik için ayar yapmak.
- **İhmal yoluyla önyargı.** Kimse haksızlık amaçlamadı diye bir sistemin adil olduğunu varsayıp onu hiç test etmemek.
- **"Bilgisayar hayır diyor."** Yanlış olduğunu görebildikleri otomatik bir kararı geçersiz kılma ya da sorgulama imkânı olmayan ön saf çalışanları ve kullanıcılar.
- **Kendinden emin kullanıcı için tasarım.** Tipik, bağlantılı, okuryazar kullanıcı için inşa edip herkesi dışarıda bırakmak; insanların vazgeçemeyeceği hizmetlerde savunulamaz.
- **Şeffaflık tiyatrosu.** Teknik olarak bilgilendiren ama gerçekte hiçbir şeyi açıklamayan anlaşılmaz açıklamalar yayımlamak.

## Olgunluk modeli

**Düzey 1, Başlangıç.** Etik ele alınmıyor ya da yalnızca bir skandaldan sonra tepkisel. Erişilebilirlik görmezden geliniyor ya da asgari düzeyde. Otomatik kararlar şeffaf değil; açıklama ve başvuru yolu yok. Önyargı hiç test edilmiyor ve sürdürülebilirlik ile toplumsal etki düşünülmüyor.

**Düzey 2, Geliştirme.** Bir davranış kuralı var ve bazı erişilebilirlik standartları, çoğu zaman geç, izleniyor. Yüksek profilli otomatik kararlar biraz insan gözetimi alıyor, ama çoğu almıyor. Önyargı ara sıra kontrol ediliyor, kaygılar zayıf bir süreçle dile getirilebiliyor ve uygulamalar takımdan takıma çok değişiyor.

**Düzey 3, Standartlaştırma.** Etik inceleme geliştirme sürecinin belgelenmiş bir parçası ve kurum genelinde uygulanıyor. Erişilebilirlik tasarıma katılıyor ve gerçek kullanıcılarla test ediliyor. Sonuç doğuran otomatik kararlar varsayılan olarak açıklama, insan incelemesi ve başvuru yolu taşıyor. Önyargı testi ve kayma izleme rutin, kamu sektörü sistemleri nasıl çalıştıklarını yayımlıyor ve sürdürülebilirlik ortak bir standarda göre ölçülüyor.

**Düzey 4, Yönetme.** Kurum etik duruşunu temel çizgilere göre veriyle ölçüyor ve kontrol ediyor: erişilebilirlik uyum puanları, korunan gruplar arasında zaman içinde izlenen orantısız etki metrikleri, itiraz edilen kararlar için başvuru oranları ve insana ulaşma süresi, yayımlanmış belgeleme taşıyan sonuç doğuran sistemlerin payı ve büyük sistemlerin enerji ya da hesaplama ayak izi. Metrikler yayınları kapıdan geçiriyor, eşik aşımları inceleme tetikliyor ve liderler uygulamaların izlendiğini varsaymak yerine rakamları sabit bir ritimle gözden geçiriyor.

**Düzey 5, Orkestrasyon.** Sorumluluk, kurumun nasıl inşa ettiğine ve uyum sağladığına gömülü. Erişilebilirlik ve hakkaniyet, hizmet verilen tüm nüfus için doğrulanan tartışılmaz varsayılanlar, algoritmik hesap verebilirlik (şeffaflık, adillik testi, başvuru yolu, insan gözetimi) standart ve sürekli izleniyor ve etik kaygılar işi yeniden şekillendiren ya da durduran değerli sinyal sayılıyor. Kurum güveni, adaleti ve onuru misyonunun özü olarak görüyor, etiği ürün, risk ve satın alma kararlarıyla bütünleştiriyor ve beklentiler ve kanıtlar geliştikçe sistemleri yeniden kapsamlandırıyor ya da emekliye ayırıyor.

## Tartışma fikirleri

- Tamamen otomatikleştirilebilecek kararlarla insanı anlamlı biçimde döngüde tutması gereken kararlar arasındaki çizgi nerede?
- Ne kadar algoritmik şeffaflık yeterli ve oyunlamaya yol açmadan ya da gizliliği ihlal etmeden anlamlı biçimde nasıl açıklarsınız?
- Otomatik bir sistem birine zarar verdiğinde kim hesap verebilir: mühendis, yönetici, kurum ya da tedarikçi?
- Etik bir itirazı dile getirmeyi kariyer sınırlayıcı olmaktan çıkarıp gerçekten güvenli nasıl kılarsınız?
- Bir kurumun tasarlamadığı kullanıcılara karşı yükümlülükleri nelerdir ve hakkaniyet ne kadar uzağa uzanmalı?
- Hesaplamanın çevresel maliyeti mimari ve ürün kararlarına nasıl yansımalı?

## Önemli çıkarımlar

- Yazılım insanlar hakkında sonuç doğuran kararlar verdiğinde, onu yapanlar yalnızca belirtime uyup uymadığından değil, yaptıklarından da sorumludur.
- Erişilebilirlik ve hakkaniyet yükümlülüktür ve yokluklarında kusurdur, isteğe bağlı iyileştirme değildir; özellikle insanların vazgeçemeyeceği hizmetlerde.
- Sonuç doğuran otomatik kararlar açıklama, insan incelemesi, başvuru yolu ve süregelen önyargı testi gerektirir; hesap verebilirliği sonradan ileri sürmek yerine tasarıma katın.
- Adalet gözetilmeden optimize edilen verimlilik sessizce acımasız olabilir; yalnızca toplam için değil, bireysel başarısızlık durumu için tasarlayın.
- Kamu sektöründe algoritmik sistemlerin nasıl çalıştığı konusunda şeffaflık varsayılan, gizlilik dar bir istisna olmalıdır.
- İş gerekçesi güven ve risktir: baştan sorumlu inşa etmek, ölçekte zararı gidermekten çok daha ucuzdur ve kamu kurumları için adalet görevin kendisidir.

## Kaynaklar ve ileri okuma

- ACM/IEEE-CS, *Software Engineering Code of Ethics and Professional Practice*
- ACM, *Code of Ethics and Professional Conduct*
- Cathy O'Neil, *Weapons of Maths Destruction*
- Virginia Eubanks, *Automating Inequality*
- Safiya Umoja Noble, *Algorithms of Oppression*
- Ruha Benjamin, *Race After Technology*
- Batya Friedman and David G. Hendry, *Value Sensitive Design*
- World Wide Web Consortium (W3C), *Web Content Accessibility Guidelines (WCAG)*
- NIST, *AI Risk Management Framework*
- OECD, *Principles on Artificial Intelligence*
- European Union, *General Data Protection Regulation (GDPR)* and the *AI Act*
- UK Government, *Data Ethics Framework* and the *Algorithmic Transparency Recording Standard*
