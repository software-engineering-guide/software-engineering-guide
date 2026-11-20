# 6.1 Yapay zeka stratejisi ve hazırlık

## Genel bakış ve motivasyon

[Yapay zeka](https://en.wikipedia.org/wiki/Artificial_intelligence), bir araştırma merakı olmaktan çıkıp büyük kurumlardan sorumlu biçimde ve ölçekte hayata geçirmeleri beklenen çekirdek bir yetkinliğe dönüştü. Kurumsal firmalar ve kamu kurumları için asıl soru artık yapay zekanın bir gösterimde etkileyici bir şey yapıp yapamayacağı değil. Asıl soru, belirli bir yatırımın gerçek bir sorunu alternatiflerinden daha iyi çözüp çözmediği, yıllarca güvenle işletilip işletilemeyeceği ve denetime, tedarik sürecine ve kamuoyu incelemesine dayanıp dayanamayacağıdır. Yapay zeka stratejisi; yapay zekanın nerede uygulanacağına, nerede kaçınılacağına ve ilk model üretime çıkmadan önce hangi temellere ihtiyacınız olduğuna karar verme disiplinidir.

Büyük takımlarda ölçek ve atalet bahisleri yükseltir. Kötü çerçevelenmiş bir girişim bütçeleri eritebilir, yetenekli mühendisleri oyalayabilir ve kamuoyunun önünde başarısız olduğunda düzenleyicilerin ve vatandaşların güvenini aşındırabilir. İyi seçilmiş bir girişim ise angaryayı otomatikleştirebilir, daha önce hiç ulaşamayacağınız verilerden içgörü çıkarabilir ve nitelikli insanları daha değerli işlere ayırabilir. Aradaki fark nadiren modelin kendisidir. Her şey, sorunu ne kadar iyi çerçevelediğinize, verinizin ve yeteneğinizin ne kadar hazır olduğuna ve iş gerekçenizin ne kadar dürüst olduğuna bağlıdır.

Kamu ve düzenlemeye tabi bağlamlar daha fazla kısıt getirir. Kamu kurumları harcamalarını gerekçelendirmek, şeffaflığı garanti etmek, hukuka aykırı ayrımcılıktan kaçınmak ve seçilmiş yetkililere ve kamuoyuna karşı hesap verebilir kalmak zorundadır. Tedarik kuralları tek kaynağa bağımlılığı yasaklayabilir, açıklanabilirlik talep edebilir ve satıcıların model davranışını görünür kılmasını zorunlu tutabilir. Burada uyumu, denetlenebilirliği ve çıkış seçeneklerini sonradan akla gelen konular olarak değil, birinci sınıf gereksinimler olarak ele alın.

## Temel ilkeler

- Bir kullanım arayan bir teknolojiden değil, çözülmeye değer bir sorundan yola çıkın.
- İhtiyacı karşılayan en basit yaklaşımı tercih edin; yapay zeka pek çok seçenekten yalnızca biridir ve çoğu zaman en iyisi değildir.
- Veri hazırlığını, yeteneği ve platform olgunluğunu sonra çözülecek paralel iş akışları olarak değil, önkoşullar olarak görün.
- Yap ya da satın al kararlarını açıkça verin ve pazar ile yetkinlikleriniz değiştikçe yeniden gözden geçirin.
- Toplam sahip olma maliyetini (TSM) hesaplayın: yalnızca lisansı ya da pilotu değil, işletmeyi, izlemeyi ve nihai değiştirmeyi de kapsasın.
- İlk günden çıkışı tasarlayın: satıcı ya da model değiştirmeyi aşırı pahalı kılan mimarilerden kaçının.
- Düzenlemeye tabi ve kamusal ortamlarda şeffaflığı, tedarik uyumunu ve hesap verebilirliği tasarım kısıtları olarak ele alın.
- Harekete geçmenin maliyetinin yanında harekete *geçmemenin* maliyetini de ölçün.

## Öneriler

### Teknolojiyi seçmeden önce sorunu çerçeveleyin

Tek sayfalık bir sorun tanımı yazın. İyileştirmek istediğiniz kararı ya da görevi, mevcut referans düzeyini, istediğiniz ölçülebilir sonucu ve sistem yanlış yaptığında ne olacağını adlandırın. Sonra sorunun yapay zekaya uygun olup olmadığını sorun. Yeterli ilgili veri var mı? Görev kural tabanlı değil, örüntü tabanlı mı? Olasılıksal yanıtlara tahammül edebilir misiniz? Bir insan çıktıyı denetleyebilir mi? Pek çok sorun belirlenimci yazılımla, daha iyi süreç tasarımıyla ya da basitçe daha iyi veri hijyeniyle çözülür. Yapay zekanın nerede *uygun olmadığını* açıkça yazın: örneğin yasa gereği kusursuz açıklanabilir olması gereken kararlar ya da nadir bir hatanın maliyetinin yıkıcı olduğu ve yakalanmasının imkansız olduğu durumlar.

### Komut ver, ince ayar yap, satın al ya da inşa et karar ağacını kullanın

En ucuz ve en hızlıdan en pahalı ve en kontrollüye doğru ilerleyin:

1. **Mevcut bir barındırılan modele komut verin.** Genel amaçlı bir model (Anthropic'in Claude'u ya da diğer sağlayıcıların benzer ürünleri gibi) özenli istem yazımı ve erişimle sorunu çözüyorsa önce bunu yapın. En düşük maliyet, en hızlı yineleme, eğitim altyapısı yok.
2. **Erişim ya da araçlarla destekleyin.** Boşluk bilgide ya da eylemlerdeyse, model ağırlıklarına dokunmadan önce [erişimle artırılmış üretim](https://en.wikipedia.org/wiki/Retrieval-augmented_generation) (RAG; ilgili belgeleri sorgu anında getirip modele bağlam olarak sunar) ve araç kullanımı ekleyin.
3. **İnce ayar yapın ya da uyarlayın.** İstem yazımı gereken doğruluğu, üslubu ya da biçimi tutarlı biçimde sağlayamıyorsa, verileriniz üzerinde daha küçük bir modele [ince ayar](https://en.wikipedia.org/wiki/Fine-tuning_(deep_learning)) yapın: yani önceden eğitilmiş bir modeli örneklerinizle ek olarak eğitip uzmanlaştırın. Bu, bir [MLOps](https://en.wikipedia.org/wiki/MLOps) (makine öğrenimi operasyonları) hattı karşılığında kontrol kazandırır.
4. **Özelleşmiş bir ürün satın alın.** İyi tanımlanmış alanlarda (belge işleme, sahtecilik puanlama) olgun bir satıcı ürünü, sizin inşa edeceğiniz her şeyden daha iyi olabilir.
5. **Sıfırdan inşa edin.** [Temel modellerin](https://en.wikipedia.org/wiki/Foundation_model) (geniş verilerle önceden eğitilmiş ve birçok göreve uyarlanabilen büyük modeller) eğitimini; benzersiz verisi, derin yeteneği ve stratejik gerekçeleri olan kurumlara bırakın. Kurumsal firmaların ve kamu kurumlarının neredeyse tamamı için bu yanlış seçimdir.

### Veri, yetenek ve platform önkoşullarını oluşturun

Verinizi erişilebilirlik, kalite, etiketleme, köken ve kullanım için hukuki dayanak açısından denetleyin. Bunu yapay zeka için kullanma hakkınızın gerçekten olduğunu, kişisel ya da üçüncü taraf veriler dahil, doğrulayın. Yeteneği dürüstçe değerlendirin: veri bilimcilere ihtiyacınız var, ayrıca ML mühendislerine, veri mühendislerine, olasılıksal sistemleri anlayan ürün yöneticilerine ve çıktıları değerlendirebilen incelemecilere de. Ölçeklemeden önce bir platform tabanı kurun: deney izleme, bir model kayıt defteri (eğitilmiş model sürümlerinin ve onay durumlarının kayıt sistemi), izleme ve güvenli sunum; böylece her yeni kullanım örneği işletmeyi yeniden icat etmek zorunda kalmaz.

### Düzenlemeye tabi ve kamu bağlamlarını bilinçli biçimde ele alın

Tedarik, hukuk ve risk takımlarını erken devreye alın. Satıcılardan model kökenini, eğitim verisi uygulamalarını, değerlendirme sonuçlarını ve bilinen sınırlamaları açıklamalarını isteyin. Verilerinizin ve istemlerinizin taşınabilirliğini veren sözleşmeleri tercih edin ve sizi tuzağa düşüren tescilli biçimlerden kaçının. Uygun olduğunda, kamuya dönük yapay zeka sistemlerinin amacını ve güvencelerini yayımlayın ve insanlara otomatik kararlara itiraz edebilecekleri bir kanal sunun. Denetimler belgelenmiş, savunulabilir bir süreç bulsun diye tanınmış çerçevelere uyum sağlayın (bkz. bölüm 6.5).

### Toplam sahip olma maliyetini hesaplayın ve bağımlılığa karşı korunun

Tüm yaşam döngüsü maliyetini modelleyin: çıkarım ya da lisanslama, veri hatları, insan incelemesi, izleme, yeniden eğitim, olay müdahalesi ve hizmetten çıkarma. Bunu mevcut durumun ve alternatiflerin maliyetiyle karşılaştırın. Modeli bir iç arayüzün arkasına koyarak, istemlerinizi ve değerlendirme veri kümelerinizi taşınabilir tutarak ve zaman zaman ikinci bir sağlayıcıyı test ederek bağımlılığı azaltın.

## Ödünleşimler: artılar ve eksiler

| Yaklaşım | Artılar | Eksiler | En uygun olduğu durum |
|---|---|---|---|
| Barındırılan modele komut vermek | Hızlı, ucuz, altyapı gerekmez, geçiş kolay | Daha az kontrol, çağrı başına maliyet, veri paylaşımı soruları | Prototipler, geniş görevler, belirsiz gereksinimler |
| Erişimle destekleme | Yanıtları verinize dayandırır, güncellenebilir | Erişim kalitesi zordur, altyapı ekler | Bilgi ağırlıklı görevler |
| Daha küçük modele ince ayar | Kontrol, ölçekte daha düşük çağrı başına maliyet, şirket içi seçeneği | MLOps, veri ve bakım gerektirir | Kararlı, yüksek hacimli, özelleşmiş görevler |
| Ürün satın almak | Kanıtlanmış, desteklenen, değere hızlı ulaşır | Lisans maliyeti, bağımlılık, sınırlı uyum | İyi tanımlanmış, sıradanlaşmış sorunlar |
| Temel model inşa etmek | Azami kontrol ve farklılaşma | Muazzam maliyet, nadir yetenek, yüksek risk | Öncü laboratuvarlar dışında neredeyse hiçbir zaman |

Baskın ödünleşim, kontrol ile maliyet ve hız arasındadır. Komut vermek size en çok hız ve esneklik, en az kontrolü verir; inşa etmek en çok kontrolü verir ama çok az kurumun harcaması gereken kaynakları ister. Çoğu büyük takım ortada yaşamalıdır: önce komut verin ve erişimle destekleyin, ince ayarı seçici yapın ve sıradanlaşmış ihtiyaçlar için satın alın. Bağımlılık, kısa vadeli rahatlığı uzun vadeli riskle takas eder ve bu özellikle çok yıllı çıkış yükümlülüklerinin yaygın olduğu kamuda önemlidir.

## Takımınızla tartışılacak sorular

1. **İlk üç aday kullanım örneğimizin her biri komut ver, sonra eriş, sonra ince ayar yap, sonra satın al, sonra inşa et merdiveninin neresinde duruyor ve onu bir basamak oynatmak için hangi kanıt gerekir?** Bu önemlidir, çünkü boşa giden yapay zeka harcamasının çoğu bir basamak yukarıdan başlamaktan gelir: özenli istem yazımı işe yarayacakken bir model eğitmek. Büyük bir takımda merdiveni ortak varsayılan olarak kabul etmek, her grubun pahalı bir hattı yeniden icat etmesini önler. Her aday için tek sayfalık sorun tanımını, mevcut referans düzeyini ve boşluğun bilgide (erişim), tutarlılıkta (ince ayar) ya da çözülmüş bir sıradan ihtiyaçta (satın alma) olup olmadığına dair dürüst bir değerlendirmeyi getirin. Kurumsal ve kamu ortamlarında her basamağın tedarik ve denetim maliyetini ekleyin, çünkü ince ayar yapılmış bir model, barındırılan bir çağrının taşımadığı bir MLOps yükünü beraberinde sürükler. Yanıt, o odada aşırı kapsamlı en az bir projeyi sonlandırmanıza ya da küçültmenize izin vermelidir.

2. **En çok bağımlı olduğumuz satıcı ya da model için somut çıkış planımız nedir ve onu gerçekten test ettik mi?** Bağımlılığı kabul etmek ucuz, çözmek pahalıdır ve kamuda hiç prova etmediyseniz karşılayamayacağınız çok yıllı çıkış yükümlülükleri taşıyor olabilirsiniz. Güvendiğiniz tescilli özelliklerin listesini, istemlerin ve değerlendirme veri kümelerinin taşınabilir olup olmadığını ve modelin bir iç arayüzün arkasında nasıl durduğunu (ya da durmadığını) getirin. İzlenecek işaret, değerlendirme paketinizi hiç ikinci bir sağlayıcıya karşı çalıştırıp çalıştırmadığınızdır; çalıştırmadıysanız çıkış planınız bir plan değil, bir umuttur. Dürüst yanıt, geçişin aylar süreceği ve çekirdek kodu yeniden yazmayı gerektireceği ise bunu aşılacak bir köprü olarak değil, şimdi düzeltilecek bir tasarım kusuru olarak görün.

3. **Dürüst bir hazırlık puan kartı veri haklarımız hakkında ne söylüyor ve bugün hangi kullanım örneklerini eliyor?** Veri hazırlığını atlamak, pilotları sessizce batıran başarısızlıktır: model çalışır, ama veriyi kullanmak için hiç hukuki dayanağınız olmamıştır ya da veri etiketsiz ve kökensizdir. Büyük bir kurumda kişisel ve üçüncü taraf verileri, yargı alanına ve veri kümesine göre değişen rıza ve sözleşme sınırlarını gündeme getirir. Her aday için erişilebilirlik, kalite, etiketleme, köken ve hukuki dayanak denetimini getirin ve veri temelleri oluşana kadar bazı kullanım örneklerini engellenmiş olarak işaretlemeye istekli olun. Düzenlemeye tabi ve kamusal ortamlarda kullanılamaz bir hukuki dayanak bir gecikme değil, kesin bir duruştur; hazırlık çalışmasını fonlamak, sonradan akla gelen bir şey olarak değil, planda açık bir kalem olmalıdır.

4. **Canlı bir yapay zeka kullanım örneğinin gerçekten işe yaradığını nasıl anlayacağız ve onu sonlandırmamıza hangi kanıt yol açar?** Çoğu yapay zeka portföyü zombiler biriktirir: yayına çıkmış, birilerini etkilemiş ve şimdi maliyetini hâlâ karşılayıp karşılamadığını kimsenin denetlemediği sonsuza dek çalışan pilotlar. Lansmandan önce referans düzeyini ve başarı ölçütünü kararlaştırın, sonra açık bir sonlandırma eşiği belirleyin; böylece durma kararı o anda savunulmak yerine önceden verilmiş olur. Mevcut ölçütü, sonuç başına insan gözetimi maliyetini ve lansmandan beri gördüğünüz kaymayı getirin. Kurumsal ve kamu portföylerinde her sistemi sabit bir sıklıkla kimin incelediğini ve onu emekliye ayırma yetkisinin kimde olduğunu adlandırın; incelenmesinden kimsenin sorumlu olmadığı bir kullanım örneğini hiç kimse kapatmayacaktır.

5. **İnsan nerede döngüde kalıyor, bu gözetim ne kadara mal oluyor ve bunu gerçekten bütçelendirdik mi?** En ucuz görünen yapay zeka kullanım örnekleri, sessizce tam otomasyonu varsayanlardır; sonra gerçeğin geri soktuğu inceleme, düzeltme ve yükseltme yoluyla maliyet sızdırırlar. Hangi kararları bir kişinin onaylaması gerektiğine, hangilerini modelin tek başına alabileceğine ve hangilerini asla alamayacağına bilinçli olarak karar verin, sonra bunun ima ettiği insan zamanını fiyatlandırın. Düşük güvenli vakaların hacmini, yanlış bir yanıtın maliyetini ve mevcut yükseltme yolunu getirin. Düzenlemeye tabi ve kamusal ortamlarda her otomatik kararı hesap verebilir bir yetkiliye ve bir itiraz yoluna bağlayın, çünkü anlatamadığınız gözetim, sahip olmadığınız gözetimdir.

6. **Önerdiğimiz şeyi işletecek yeteneğe ve platforma sahip miyiz, yoksa sessizce sahip olmadığımız bir kapasiteyi mi varsayıyoruz?** Hırslı yapay zeka planları, modelden çok gösterişsiz temellerde başarısız olur: hattı bakımda tutacak kimse yok, çıktıları değerlendirebilecek kimse yok, üzerine dağıtılacak platform yok. Her aday kullanım örneğini gerçekten ihtiyaç duyduğu becerilerle ve altyapıyla eşleştirin ve boşluğun bir işe alım, bir ortak ya da inşa etmemek için bir neden olduğu yerlerde dürüst olun. Üretimde her sistemin sahibi olabilecek kişilerin, üzerinde çalışacağı platformun ve satın almanız gereken yetkinliklerin envanterini getirin. Büyük ya da kamusal bir kurum için tedarik ve işe alım bekleme sürelerini ekleyin; ilgili zaman diliminde işe alamayacağınız bir yeteneğe dayanan bir plan, eksik teslim etme planıdır.

## Sektör merceği

**Girişim.** Hız ve hayatta kalma baskındır. Çekirdek değerinize dokunan dar bir kullanım örneği seçin, ince bir arayüzün arkasında barındırılan bir modelle yayına alın ve harcamayı sıkı biçimde sınırlayın. Altyapı kurmaktan ya da model eğitmekten kaçının: en kıt kaynağınız mühendislik dikkatidir ve bakımını yapamayacağınız ince ayarlı bir hat, bir hendek değil bir yüktür. Hızlı hareket eden bir pazarı takip edebilmek için geçişi ucuz tutun.

**Küçük işletme.** Büyük olasılıkla veri bilimcileriniz yok ve bütçeniz dar; bu yüzden yapay zekayı kadro kurduğunuz bir program olarak değil, zaten kullandığınız araçlara gömülü olarak satın aldığınız bir şey olarak görün. Hazırlığı bir makine öğrenimi projesi olarak değil, bir veri hijyeni ve gizlilik sorusu olarak çerçeveleyin: hangi müşteri verisini tuttuğunuzu, onunla ne yapmanıza izin verildiğini ve yanlış bir otomatik yanıtın size nerede bir müşteriye mal olacağını bilin. Yapay zekayı isteğe bağlı, şeffaf ve kapatması kolay tutan satıcıları tercih edin.

**Kurumsal.** Sorun, birçok takım arasında portföy yönetişimidir: ortak bir yap ya da satın al merdiveni, tutarlı hazırlık değerlendirmeleri ve gruplar pahalı hatları yeniden icat etmeyi bıraksın diye bağımlılık ve toplam maliyet analizi. MLOps ve insan gözetimi yükünü açıkça bütçelendirin, sağlayıcılar değiştirilebilir kalsın diye arayüz katmanını standartlaştırın ve yapay zeka kullanım örneklerini bir pilot dağınıklığı olarak değil, net ölçütleri ve sonlandırma ölçütleri olan bir portföy olarak yönetin.

**Kamu.** Şeffaflık, tedarik kuralları ve hesap verebilirlik her seçimi şekillendirir. Politika üretmek yerine resmi kaynaklara atıf yapan sistemleri tercih edin, sonuçları ağır kararlar için bir insanı sorumlu tutun ve sözleşmelerde veri taşınabilirliğini ve model sınırlamalarının açıklanmasını talep edin. Sade dilde bir tanım ve bir itiraz yolu yayımlayın, imzaladığınız çok yıllı çıkış yükümlülüklerine uyun ve yapay zekayı, hesap verebilir bir yetkiliye ait olması gereken nihai değerlendirme kararlarının dışında tutun.

## Örnekler

**Girişim.** Beş kişilik bir randevu çizelgeleme girişimi, iki mühendisini çekirdek üründen almadan doğal dilde "bana bir toplantı ayarla" özelliği eklemek istedi. Önemli olan en küçük sorunu seçti, yani bir isteği önerilen bir zamana ayrıştırmayı, ve daha sonra sağlayıcı değiştirebilmek için ince bir iç API'nin arkasında barındırılan bir modelle yayına aldı. Takım sıkı bir aylık harcama sınırı koydu, kullanıcıların önerilen zamanları kabul edip etmediğini izledi ve ince ayarlı bir modele ancak hacim ek işi haklı çıkarırsa geri dönmeyi kararlaştırdı.

**Kurumsal.** Çok uluslu bir sigortacı, hasar triyajını hızlandırmak istedi. Özel bir model eğitmek yerine sorunu dar biçimde çerçeveledi (gelen hasarları yönlendirmek ve özetlemek), barındırılan bir model ile poliçe belgeleri üzerinde erişimle prototip yaptı ve insan işleme süresine ve doğruluğa karşı ölçtü. Değeri kanıtladıktan sonra, çağrı başına maliyeti düşürmek için yalnızca en yüksek hacimli hasar türü için daha küçük bir modele ince ayar yaptı. Sağlayıcıları değiştirebilmek için modeli bir iç API'nin arkasında tuttu ve düşük güvenli vakaların insan incelemesini kapsayan üç yıllık bir TSM modelledi.

**Kamu.** Ulusal bir vergi idaresi, personelin vatandaş sorgularını yanıtlamasına yardım edecek bir yapay zeka yardımcısı düşündü. Bu yanıtlar yasal yükümlülüklere dokunduğundan kurum şeffaflıkta ısrar etti: sistem yalnızca atıflarla resmi rehberliği ortaya çıkarabilir, asla politika uyduramazdı ve bir insan, dışarı çıkmadan önce her otomatik öneriyi inceledi. Tedarik, satıcının model sınırlamalarını açıklamasını ve veri taşınabilirliği vermesini şart koştu ve kurum sistemin sade dilde bir tanımını ve bir itiraz yolunu yayımladı. Yapay zekayı nihai değerlendirme kararlarının tamamen dışında tuttu ve bunları hesap verebilir yetkililere ayırdı.

## İş gerekçesi: motivasyonlar, YG ve TSM

Yapay zeka stratejisi, birbirinin aynadaki yansıması iki başarısızlıktan kaçınmanıza yardımcı olmak için vardır: hiç karşılığını vermeyen yapay zekaya aşırı yatırım yapmak ve rakipler ya da emsal kurumlar öne geçerken yeterince yatırım yapmamak. YG (yatırım getirisi); tasarruf edilen emekten, kısalan döngü süresinden, düşen hata oranlarından ve olanak kazanan yeni yetkinliklerden gelir. Bunları gerçek bir referans düzeyine karşı ölçün ve nadiren ortadan kalkan insan gözetiminin gerçek maliyeti için indirim yapın.

TSM, gösterişsiz kalemleri içermelidir: veri hatları, izleme, dünya kaydıkça yeniden eğitim, güvenlik incelemesi ve nihai hizmetten çıkarma. Ucuz görünen bir pilot, yıllarca ölçekte çalıştığında pahalıya dönüşebilir. Benimsememenin maliyetini de sunun: daha yavaş hizmet, daha yüksek manuel maliyet ve stratejik sapma. Gerekçeyi liderliğe bir portföy görünümüyle sunun: birkaç yüksek güvenli bahis, net başarı ölçütleri, başarısızlıklar için sonlandırma ölçütleri ve veri ile yetenek temellerinin var olduğunu gösteren bir hazırlık değerlendirmesi. Liderlerden hazırlığı açıkça fonlamalarını isteyin; atlarsanız pahalı yeniden işi garantilemiş olursunuz.

## Anti-kalıplar ve tuzaklar

- **Sorun arayan çözüm.** Emsaller aldı diye yapay zeka satın almak, sonra bir kullanım örneği avlamak.
- **Veri hazırlığını atlamak.** Modelleri erişilemeyen, etiketsiz ya da hukuken kullanılamaz veriler üzerinde yayına almak.
- **Gösterim güdümlü kararlar.** Üretim kalitesinde bir değerlendirme olmadan cilalı bir gösterime dayanarak taahhütte bulunmak.
- **İnsan döngüsünü yok saymak.** Tam otomasyon varsaymak ve maliyetin çoğunun saklandığı incelemeyi eksik bütçelendirmek.
- **Sessiz bağımlılık.** Çıkış planı olmadan tek bir satıcının tescilli özellikleri üzerine derinlemesine inşa etmek.
- **İşletmeyi hafife almak.** Dağıtımı, bir bakım yükümlülüğünün başlangıcı olarak değil, bitiş çizgisi olarak görmek.
- **Sonradan akla gelen uyum.** Şeffaflığı ve denetlenebilirliği tasarımdan sonra, birkaç kat maliyetle eklemek.

## Olgunluk modeli

1. **Düzey 1, Başlangıç.** Geçici deneyler, ortak strateji yok, kararlar abartı ve bireysel hevesle yönlendiriliyor.
2. **Düzey 2, Geliştirme.** Bazı projeler için sorun çerçeveleme var; ilk platform tabanı ortaya çıkıyor; yap ya da satın al tartışılıyor ama tutarsız.
3. **Düzey 3, Standartlaştırma.** Net ölçütleri olan bir yapay zeka kullanım örnekleri portföyü, belgelenmiş bir karar ağacı, hazırlık değerlendirmeleri ve takımlar arasında tutarlı biçimde uygulanan bağımlılık ve TSM analizi.
4. **Düzey 4, Yönetme.** Portföy ölçülür: hazırlık, YG, TSM ve insan gözetimi maliyeti referans düzeylere karşı izlenir; sonlandırma ölçütleri kanıta dayalı olarak uygulanır; teslimat ve kalite etkisi her devam ya da durdur kararını yönlendirir.
5. **Düzey 5, Orkestrasyon.** Yapay zeka stratejisi iş ve risk planlamasıyla bütünleşir; hazırlık sürekli sürdürülür; kurum, pazar ve risk tablosu değiştikçe portföyü yeniden dengeleyerek yapay zeka sistemlerini kanıta dayalı olarak rutin biçimde emekliye ayırır, değiştirir ve yeniden kapsamlandırır.

## Tartışma fikirleri

- Bir sorunun yapay zekaya gerçekten uygun olmadığına nasıl karar verirsiniz ve hayır deme yetkisi kimde?
- Bir projeyi pilottan üretime geçirmek için hangi hazırlık eşiği kapı olmalı?
- Değere daha hızlı ulaşma karşılığında ne kadar bağımlılık kabul edilebilir?
- Kamuda, şeffaflık yükümlülükleri yap ya da satın al seçimini nasıl şekillendirmeli?
- Satıcıların ve meraklıların bunları düşük göstermek için teşvikleri varken TSM tahminlerini nasıl dürüst tutarsınız?
- Yapay zeka portföyü kimin ve sonlandırma kararları nasıl veriliyor?

## Önemli çıkarımlar

- Strateji, bir teknolojiyle değil, gerçek bir sorunla ve dürüst bir referans düzeyiyle başlar.
- En basit seçeneği tercih edin: önce komut verin, sonra erişin, sonra ince ayar yapın, sonra satın alın ve nadiren sıfırdan inşa edin.
- Veri, yetenek ve platform hazırlığı önkoşullardır; onları fonlamak planın parçasıdır.
- Düzenlemeye tabi ve kamu bağlamları tasarım gereği şeffaflık, tedarik uyumu ve çıkış seçenekleri ister.
- Tam TSM'yi ve eylemsizliğin maliyetini modelleyin ve ilk mimari kararından itibaren satıcı bağımlılığına karşı korunun.

## Kaynaklar ve ileri okuma

- Ajay Agrawal, Joshua Gans, and Avi Goldfarb, *Prediction Machines: The Simple Economics of Artificial Intelligence*.
- Eric Siegel, *The AI Playbook: Mastering the Rare Art of Machine Learning Deployment*.
- Andriy Burkov, *The Hundred-Page Machine Learning Book*.
- National Institute of Standards and Technology, *AI Risk Management Framework (AI RMF 1.0)*.
- Organisation for Economic Co-operation and Development, *OECD AI Principles*.
- Thomas H. Davenport, *The AI Advantage: How to Put the Artificial Intelligence Revolution to Work*.
