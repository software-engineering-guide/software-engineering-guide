# 5.5 Uluslararasılaştırma ve yerelleştirme

## Genel bakış ve motivasyon

[Uluslararasılaştırma](https://en.wikipedia.org/wiki/Internationalization_and_localization) (i18n), yazılımı kodu değiştirmeden her dile, bölgeye ve kültüre uyarlanabilecek biçimde inşa etme mühendisliğidir. Yerelleştirme (l10n) ardından gelen iştir: metni çevirerek, tarihleri ve sayıları biçimlendirerek, yerleşimi ayarlayarak ve kültürel beklentileri hesaba katarak bir ürünü belirli bir yerele gerçekten uyarlamak. İkisi farklıdır. Uluslararasılaştırma bir kez, mimaride yapılır. Yerelleştirme birçok kez, içerikte yapılır. Mimariyi baştan doğru kurarsanız her yerelleştirme ucuzdur. Yanlış kurarsanız her biri acı verici, hataya açık bir sonradan uyarlamaya dönüşür.

Büyük takımlar için i18n temel bir mimari karardır. Her katmana dokunur: veri depolama, dize işleme, yerleşim ve içerik hatları. Bunu erken kurup ortak kitaplıklar ve lint kurallarıyla zorlamazsanız takımlar İngilizce dizeleri koda gömer, çevrilmiş parçaları birleştirir ve Latin alfabesi varsayar. Ürün herhangi bir yeni pazara girmeden önce bu borcun çözülmesi gerekir. Ortak bir i18n çerçevesi ve yerelleştirme iş akışı, düzinelerce takımın her biri tesisatı yeniden icat etmeden ürünü birçok dilde yayına almasını sağlar.

Kurumsal ve kamu açısından ilgisi doğrudandır. Çok uluslu kuruluşlar ülkeler, diller ve düzenleyici rejimler arasında müşterilerine ve çalışanlarına hizmet vermek zorundadır. Hükümetler dilsel olarak çeşitli nüfuslara hizmet vermek zorundadır. Birçok ülke resmî olarak çok dillidir ve birçoğu yasal olarak [sağdan sola](https://en.wikipedia.org/wiki/Bidirectional_text) yazılan alfabeler ile yerli ya da azınlık dilleri dahil birden fazla dilde hizmet sunmak zorundadır. Kamu hizmetlerinde dile erişim bir eşitlik ve hukuk meselesidir: mevcut tek dili okuyamayan bir yurttaş fiilen hizmetten yoksun bırakılmış olur.

## Temel ilkeler

- Mimariyi bir kez uluslararasılaştırın; içeriği birçok kez yerelleştirin.
- Kullanıcıya dönük metni asla koda gömmeyin; tüm dizeleri yönetilen kaynaklara dışa alın.
- Her yerde [Unicode](https://en.wikipedia.org/wiki/Unicode) (UTF-8) kullanın; metnin herhangi bir alfabede olabileceğini varsayın.
- Çevrilmiş parçaları asla birleştirmeyin; dil bilgisi ve sözcük sırası dile göre değişir.
- Metin genişlemesi, sağdan sola alfabeler ve karmaşık çoğul ve cinsiyet kuralları için plan yapın.
- Tarihleri, sayıları, para birimlerini ve adları kodla değil, yerele göre biçimlendirin.
- Çevrilebilir içeriği koddan ayırın; böylece çevirmenler kaynağa hiç dokunmasın.
- Yerelleştirme yalnızca dilsel değil kültüreldir: renkler, görseller ve örnekler önemlidir.

## Öneriler

### Sağlam bir uluslararasılaştırma mimarisi kurun

Her alfabe temsil edilebilsin diye tüm metni uçtan uca (veritabanı, API'ler ve arayüz) Unicode (UTF-8) olarak saklayın ve işleyin. Her kullanıcıya dönük dizeyi, koda ya da işaretlemeye gömmek yerine, tanımlayıcıyla anahtarlanmış kaynak dosyalarına ya da bir ileti kataloğuna dışa alın. Bir yereli dil artı bölge (gerekirse alfabe) olarak temsil edin; böylece örneğin bir dilin ülkeler arasındaki çeşitlemelerini ayırt edebilirsiniz. Tarih, sayı ve para birimi biçimlendirmesini elle yazmak yerine biçimlendirme mantığını iyi sınanmış bir uluslararasılaştırma kitaplığında tutun. Veriyi nötr, belirsizliksiz biçimlerde (UTC zaman damgaları, ISO ülke ve para birimi kodları, temel birimler) saklayın ve yalnızca sunum katmanında biçimlendirin.

### Dil karmaşıklığını doğru ele alın

Metin uzunluğunu varsaymayın; bol yer bırakın, çünkü çeviriler genellikle İngilizceden çok daha uzun çıkar, ve kesmek ya da üst üste binmek yerine yeniden akan yerleşimler tasarlayın. Fiziksel yerine mantıksal yerleşim özellikleri kullanarak ve uygun yerde arayüzü yansıtarak çift yönlü (sağdan sola) alfabeleri destekleyin. Basit tekil/çoğul mantığı yerine, i18n kitaplığınız aracılığıyla yerelin çoğul kurallarını kullanın (dillerde bir ile altı arasında çoğul biçimi vardır). Dilin gerektirdiği yerde cinsiyeti ve dil bilgisel uyumu ele alın. Cümleleri asla birleştirerek kurmayın; çevirmenler sözcük sırasını denetlesin diye tam, parametreli ileti şablonları kullanın.

### Bir yerelleştirme iş akışı ve çeviri yönetimi kurun

Yerelleştirmeyi yayın öncesi bir toplu iş değil, sürekli bir hat olarak ele alın. Dizeleri otomatik çıkarın, bir [çeviri yönetim sistemine](https://en.wikipedia.org/wiki/Translation_management_system) gönderin ve tamamlanmış çevirileri geri çekin; ideal olarak CI ile bütünleştirin ki yeni dizeler işaretlensin ve yerelleştirilmiş sürümler senkron kalsın. Çevirmenlere bağlam verin: ekran görüntüleri, açıklamalar, karakter sınırları ve terminoloji ile tonu tutarlı tutmak için dil başına bir sözlük ve üslup rehberi. Önceki işi yeniden kullanmak ve maliyeti düşürmek için [çeviri belleği](https://en.wikipedia.org/wiki/Translation_memory) kullanın. [Makine çevirisinin](https://en.wikipedia.org/wiki/Machine_translation) nerede kabul edilebilir olduğuna (düşük riskli, yüksek hacimli içerik) ve nerede insan çevirisi ile incelemesi gerektiğine (hukuki, tıbbi, güvenlik, markaya kritik) bilinçli karar verin. Gerçek çeviri başlamadan önce kodlanmış dizeleri, kesilmeleri ve kodlama hatalarını yakalamak için erken [sahte yerelleştirme](https://en.wikipedia.org/wiki/Pseudolocalization) yapın; dizeleri uzatılmış, vurgulu yer tutucularla değiştirin.

### Yalnızca sözcükleri değil, biçimleri, kültürü ve içeriği yerelleştirin

Tarihleri, saatleri, sayıları, para birimlerini, adresleri, telefon numaralarını ve adları yerel geleneklere (tarih sırası, ondalık ve gruplama ayırıcıları, para birimi yerleşimi, ad sırası) saygı göstererek yerele göre biçimlendirin. Görselleri, simgeleri, renkleri, örnekleri ve metaforları yerel kültürel anlama uyarlayın, çünkü simgeler ve renkler kültürden kültüre farklı çağrışımlar taşır. Yerel yasal ve düzenleyici içerik farklarını hesaba katın. Küresel tutarlılığı (marka, çekirdek işlevsellik) bölgesel uyarlamadan (içerik, örnekler, uyum) ayırın ve hangi öğelerin sabit, hangilerinin esnek olduğuna açıkça karar verin.

### i18n'i ortak altyapı olarak yönetin

Takımların yanlışlıkla metin gömememesi için ortak bir i18n kitaplığı, dize dışa alma lint kuralları ve standart bir yerel çözümleme mekanizması sağlayın. Yerelleştirme hattının ve sözlüklerin sahipliğini belirleyin. Gerilemeler otomatik yakalansın diye CI'da, sağdan sola bir yerel ve uzun metinli bir sahte yerel dahil, birden çok yerelde test edin.

## Ödünleşimler: artılar ve eksiler

| Karar | Artılar | Eksiler |
|---|---|---|
| İlk günden uluslararasılaştırmak | Sonradan ucuz pazar girişi, sonradan uyarlama yok | İkinci bir yerel gerekmeden önce bile ön maliyet |
| i18n'i sonradan uyarlamak | Küresel ihtiyaç belirsizse maliyeti erteler | Gömülü varsayımları çözmek çok pahalı ve riskli |
| İnsan çevirisi | Yüksek kalite, kültürel olarak doğru | Daha yavaş ve daha maliyetli |
| Makine çevirisi | Hızlı, ucuz, çok büyük hacme ölçeklenir | Kalite ve doğruluk riski; yüksek riskli içerik için uygun değil |
| Sürekli yerelleştirme hattı | Yereller senkron kalır, yayın öncesi sıkışma yok | Araç ve süreç yatırımı |
| Bölge başına derin kültürel uyarlama | Daha iyi yerel uyum ve güven | Kurulacak ve sürdürülecek daha çok içerik çeşitlemesi |

Belirleyici ödünleşim, uluslararasılaştırmaya ne zaman yatırım yapılacağıdır. Gömülü, birleştirilmiş, Latin alfabesi varsayan kodla dolu bir ürüne i18n'i sonradan eklemek, ödenmesi en pahalı teknik borç biçimlerinden biridir. Makul uluslararası ya da çok dilli hedefleri olan her kuruluş için, ki bu hemen hemen tüm büyük kurumsal yapıları ve çok dilli hükümetleri içerir, mimariyi erken uluslararasılaştırmak, getirisi ertelenmiş olsa bile sonradan uyarlamaktan çok daha ucuzdur.

## Takımınızla tartışılacak sorular

1. **Dize dışa almayı lint kurallarıyla zorluyor muyuz ve sahte yerelleştirme herhangi bir gerçek çeviriden önce CI'da çalışıyor mu?** Uluslararasılaştırmayı pahalı yapan borç (gömülü İngilizce dizeler, birleştirilmiş cümle parçaları, Latin alfabesi varsayımları) araçlar commit anında durdurmadıkça sessizce birikir. Gömülü kullanıcı metnini işaretleyen lint kuralları ve CI'da çalışan uzun metinli, vurgulu bir sahte yerel, kesilme, üst üste binme ve kodlama hatalarını düzeltmesi ucuzken yakalar. Düzinelerce takımın, her biri tesisatı yeniden icat etmeden ya da sonradan bir son tarihe karşı varsayımları çözmeden, tek bir ürünü birçok dilde yayına almasını sağlayan budur. Gömülü dizeler için bir arama getirin ve herhangi bir takımın bugün yanlışlıkla bir tanesini yayına alıp alamayacağını sorun. Hiçbir şey onu yakalamayacaksa, kapatılacak ilk açık budur.

2. **Kanonik veriyi nerede saklıyoruz ve biçimlendirme sunum katmanıyla sınırlı mı?** Zaman damgalarını UTC, ülkeleri ve para birimlerini ISO kodları, tutarları temel birimlerle saklamak, her yerelin onları uçta doğru biçimlendirebilmesi demektir; veri katmanına gömülü biçimlendirme mantığı ise çözülmesi acı verici hatalar üretir. Tarihlerin, sayıların, para birimlerinin, adreslerin ve adların yalnızca sunumda, elle yazılmış kod yerine iyi sınanmış bir kitaplıkla biçimlendirilmesi konusunda anlaşın. Bu, bir yurttaşın kendi geleneğinde doğru tarih sırasını, ondalık ayırıcıları ve ad sırasını görmesi gereken çok uluslu kuruluşlar ve çok dilli hükümetler için önemlidir. Sisteminizin zaten biçimlendirilmiş olarak sakladığı bir değer örneği getirin ve yeni bir yerel onu farklı istediğinde neyin bozulduğunu izleyin. Veri ve sunum iç içeyse, yerel eklemeden önce bunları nasıl ayıracağınıza karar verin.

3. **Makine çevirisi tam olarak nerede kabul edilebilir ve yerelleştirme hattımızı toplu değil sürekli nasıl tutuyoruz?** Makine çevirisi düşük riskli, yüksek hacimli içerik için hızlı ve ucuzdur, ancak yanlış çevirinin gerçek zarar verdiği hukuki, tıbbi, güvenlik ya da markaya kritik metinler için uygun değildir; bu yüzden sınır, takım başına bir tahmin değil, açık bir politika olmalıdır. Aynı şekilde, yerelleştirmeyi yayın öncesi bir toplu iş olarak ele almak çeviri sıkışmasını garantiler; oysa dizeleri otomatik çıkarmak ve bir çeviri yönetim sistemiyle senkronlamak her yereli güncel tutar. Hattın, sözlüklerin ve yüksek riskli dizeler için insan inceleme kapısının sahibine karar verin. Yakın zamanda çıkmış bir sürüm getirin ve yeni dizelerinin her dilde görünmesinin ne kadar sürdüğünü sorun. Yereller sürümler arasında senkrondan çıkıyorsa, hattınız kılık değiştirmiş bir toplu iştir.

4. **Sağdan sola bir yereli ve uzun metinli bir sahte yereli otomatik test ediyor muyuz, yoksa sessizce Latin alfabelerini ve İngilizce uzunluğunda yerleşimleri mi varsayıyoruz?** Çift yönlü (sağdan sola) destek ve metin genişlemesi, yeni bir pazarda en görünür biçimde kırılan varsayımlardır: hiç yansıtılmamış yansıtılmış arayüzler ve Almancanın ya da Fincenin İngilizceden yüzde kırk daha uzun çıkmasıyla kesilen düğmeler. Karşıt çekim hızdır, çünkü fiziksel yerine mantıksal yerleşim özellikleri üzerine kurmak ve vurgulu bir sahte yereli sürekli bütünleştirmeye (CI) bağlamak, herhangi bir gerçek müşteri buna ihtiyaç duymadan önce emek gerektirir. En yoğun ekranlarınızın sağdan sola bir yerelde ve uzatılmış bir sahte yerelde işlenmiş ekran görüntüsünü getirin ve üst üste binmeleri, kırpılmış etiketleri ve takılı kalmış okları sayın. Sağdan sola ya da azınlık bir dile hizmet etmek zorunda olan çok uluslu bir kuruluş ya da hükümet için, yansıtamayan bir yerleşim kozmetik bir kusur değil, yeniden inşa etmeden karşılayamayacağınız bir pazar ya da yasal bir yükümlülüktür.

5. **Ürünün hangi parçaları küresel olarak sabit ve hangileri bölgeye göre esnek, ve karar yetkisi kimde?** Yerelleştirme yalnızca dilsel değil kültüreldir; renkler, görseller, örnekler, hitap biçimleri ve hatta hangi özelliklerin sunulduğu pazara göre değişebilir, ancak izin verdiğiniz her bölgesel çeşitleme sonsuza dek inşa edilecek, çevrilecek, incelenecek ve sürdürülecek bir yapıt daha demektir. Gerilim, güven ve dönüşüm kuran yerel uyum ile markayı tutarlı ve bakım yükünü sınırlı tutan tutarlılık arasındadır. Önerilen yeni bir yerelin çevrilmiş dizelerin ötesinde neyi değiştireceğinin somut bir listesini getirin ve her çeşitlemenin yalnızca ilk inşasını değil, süregelen bakımını fiyatlandırın. Büyük bir kurumda bu karar, bölgesel takımlar ürünü gelişigüzel çatallayamasın diye adı konmuş bir sahip gerektirir; kamuda ise yargı alanına göre değişen ve isteğe bağlı olmayan yasal ve erişilebilirlik içerik kurallarına saygı göstermelidir.

6. **Hangi yerellere gerçekten söz veriyoruz, aralarında terminolojiyi nasıl tutarlı tutuyoruz ve bu listeyi hangi kanıt belirliyor?** Bir dil eklemeyi vaat etmek kolay, sürdürmek pahalıdır, çünkü her biri bir sözlük, bir üslup rehberi, yüksek riskli dizeler için insan incelemesi ve çoğu dilde basit tekil-ya-da-çoğul mantığının yanlış yaptığı doğru çoğul ve cinsiyet işleme gerektirir. Karşıt değerlendirmeler erişim ve maliyettir: kötü hizmet verilen bir pazar ya da nüfus, hiç hizmet verilmeyenden daha kötü olabilir. Her aday yerelin arkasındaki nüfusu ya da geliri, kitaplığınızın onun için sağladığı çoğul kuralı ve biçimlendirme kapsamını ve sözlüğünün sahibini getirin. Çok uluslu bir kuruluş için itici güç, ulaşılabilir pazar ve dil başına destek maliyetidir; hükümet için ise yasal dil erişimi yükümlülüğü ve eşitliktir, yalnızca o dilde işlem yapabilen sakin sayısıyla nicelenir.

## Sektör merceği

**Girişim.** Ucuz mimari seçimleri ilk günden yapın ve orada durun: uçtan uca UTF-8, her kullanıcıya dönük dize bir ileti kataloğunda ve tarihler, sayılar ve para birimleri yerel farkındalığı olan bir kitaplıkla biçimlendirilmiş. Bunlar tek dilde yayın yaparken neredeyse hiçbir şeye mal olmaz ve ilk büyük müşteriniz ikinci bir dil istediğinde yeniden yazmaktan sizi kurtarır. Henüz kimsenin ödemediği yereller için bir çeviri hattı kurmayın ya da yerel desteklemeyin; kapıyı açık tutun, bütün evi döşemeyin.

**Küçük işletme.** Uluslararasılaştırma uzmanı olmadan ve dar bir bütçeyle, hatları kendiniz kurmak yerine çerçevenizde zaten bulunan i18n özelliklerine ve barındırılan bir çeviri yönetim hizmetine yaslanın. Makine çevirisini düşük riskli, yüksek hacimli içerik için kullanın ve insan çevirisi için yalnızca bir hatanın size müşteriye mal olacağı ya da bir kuralı ihlal edeceği yerlerde (hukuki, güvenlik ya da faturalama metni gibi) ödeme yapın. Bir yereli ancak belirli bir pazar süregelen çeviri ve inceleme maliyetini açıkça haklı çıkarıyorsa taahhüt edin.

**Kurumsal.** Sorun birçok takım arasında yönetişimdir: ortak bir i18n kitaplığı, gömülü dizeleri reddeden lint kuralları, çeviri belleği ve dil başına sözlüklerle sürekli bir yerelleştirme hattı ve sağdan sola ile uzun metinli bir sahte yerel içeren çok yerelli CI. Yerelleştirmeyi açık bir sahibi olan ortak altyapı olarak yürütün; gruplar tesisatı yeniden icat etmeyi ya da senkrondan çıkmayı bıraksın. Dil kapsamını, yerelleştirme kalitesini ve yeni bir yereli yayına alma süresini ölçün ve yerel portföyünü pazarları gelişigüzel açmak yerine bu sayılara göre yönetin.

**Kamu.** Dile erişim çoğu zaman yasal bir yükümlülüktür; resmî dilleri, sağdan sola alfabeleri ve yerli ya da azınlık dillerini kapsar, bu yüzden şeffaflık ve eşitlik her seçimi şekillendirir. Kurumlar arasında ortak bir i18n çerçevesi ve çeviri iş akışı kurun, hukuki ve güvenlik terminolojisi için insan incelemesi isteyin ve hizmetler arasında terimler tutarlı kalsın diye sözlükleri yayımlayın. Satın alma, sözleşmelerde yerel, sağdan sola ve erişilebilirlik desteğini talep etmelidir ve her dilde hizmet verilen nüfus, harcamayı kamuya karşı haklı çıkaran ölçüttür.

## Örnekler

**Girişim.** Yalnızca İngilizce yayın yapan küçük bir girişim yine de ilk günden birkaç ucuz mimari seçim yaptı: her yerde UTF-8, her kullanıcıya dönük dizenin koda gömülmek yerine bir ileti kataloğuna alınması ve tarihlerin ve para birimlerinin yerel farkındalığı olan bir kitaplıkla biçimlendirilmesi. Tek dilleri varken neredeyse hiçbir şeye mal olmadı. Bir yıl sonra en büyük potansiyel müşterileri Fransızca ve Almanca bir sürüm istediğinde, bu yerelleri eklemek çoğunlukla bir yükleniciye devredilen bir çeviri işiydi, yeniden yazma değil; anlaşmayı bir çeyrek mühendislik işi için ertelemek yerine haftalar içinde kapattılar.

**Kurumsal.** Küresel bir e-ticaret şirketi platformunu erken uluslararasılaştırdı: baştan sona UTF-8, dışa alınmış dizeler, yerel farkındalığı olan bir biçimlendirme kitaplığı ve çeviri belleği ile dil başına sözlükleri olan sürekli bir yerelleştirme hattı. Yeni bir pazara girmek bir mühendislik projesinden çok bir içerik işi (çevir, incele, görselleri ayarla) hâline geldi ve şirketin yeni yerellerde haftalar içinde yayına girmesini sağladı. Mantıksal yerleşim özellikleri üzerine kurulu sağdan sola desteği, Arapça ve İbranice pazarlarının az yeni arayüz işi gerektirmesi demekti.

**Kamu.** Sağdan sola bir alfabe ve azınlık dilleri dahil birkaç resmî dilde hizmet sunmak yasal olarak zorunlu olan ulusal bir hükümet, kurumlar arasında kullanılan ortak bir i18n çerçevesi ve çeviri iş akışı kurdu. CI'daki sahte yerelleştirme, yayından önce gömülü dizeleri ve kesilmeleri yakaladı; ortak bir sözlük hukuki terminolojiyi hizmetler ve diller arasında tutarlı tuttu. Yurttaşlar vergi, sağlık ve yardım işlemlerini kendi dillerinde, doğru tarih, sayı ve ad biçimlendirmesiyle tamamlayabiliyor; bu da dile erişim yasasını karşılıyor ve çoğunluk dili dışındaki konuşurlar için eşitliği iyileştiriyor.

## İş gerekçesi: motivasyonlar, YG ve TSM

Uluslararasılaştırmanın YG'si pazara erişim ve hızdır. İyi uluslararasılaştırılmış bir ürün yeni ülkelere ve dil pazarlarına hızlı ve ucuz girebilir; her yeni yereli büyük bir projeye değil, artımlı gelire ya da yurttaşa erişime dönüştürür. Yerelleştirme kalitesi her pazarda dönüşümü, güveni ve destek maliyetini belirler: ürün kullanıcının dilini doğru konuştuğunda ve geleneklerine saygı gösterdiğinde kullanıcılar daha çok işlem yapar ve desteğe daha az başvurur.

TSM açısından benimseme maliyeti, uluslararasılaştırmak için ön mühendislik artı süregelen çeviri ve hat maliyetleridir. Benimsememenin maliyeti pahalı sonradan uyarlamadır: çoğu zaman bir pazarın ya da yasal bir gerekliliğin dayattığı bir son tarihe karşı, tüm kod tabanında gömülü dizeleri, birleştirmeyi, kodlama hatalarını ve yerleşim varsayımlarını çözmek. Kötü yerelleştirmenin de gizli maliyetleri vardır: kötü hizmet verilen pazarlarda kaybedilen satışlar, kafa karıştırıcı biçimlerden doğan destek yükü ve yanlış çevrilmiş yüksek riskli içerikten doğan yasal ya da itibar zararı. Sürekli yerelleştirme, yayın öncesi maliyetli çeviri sıkışmalarını önler.

Liderliğe gerekçeyi kurmak için uluslararasılaştırmayı gelecekteki pazarlar üzerine bir opsiyon olarak çerçeveleyin. Bu, gelecekteki her pazar girişinin maliyetini ve süresini dramatik biçimde düşüren mütevazı bir ön yatırımdır. Kamu için itici güç, her dilde hizmet verilen nüfusla nicelenen yasal dil erişimi yükümlülüğü ve eşitliktir.

## Anti-kalıplar ve tuzaklar

- **Gömülü dizeler**: koda gömülmüş kullanıcı metni, yerel başına kod değişikliğini zorunlu kılar.
- **Dize birleştirme**: cümleleri parçalardan kurmak, dil bilgisini ve sözcük sırasını bozar.
- **Unicode olmayan varsayımlar**: kodlama hataları, [mojibake](https://en.wikipedia.org/wiki/Mojibake) (uyumsuz karakter kodlamalarından doğan bozuk metin) ve alfabeleri temsil edememe.
- **İngilizce metin uzunluğunu varsaymak**: çevrildiğinde kesilen ya da üst üste binen yerleşimler.
- **Sağdan solu görmezden gelmek**: yansıtılamayan fiziksel sol/sağ yerleşim kullanmak.
- **Saf çoğullaştırma**: çoğu dilde yanlış olan tekil/çoğul mantığı.
- **Yerele kör biçimlendirme**: gömülü tarih, sayı ve para birimi biçimleri.
- **Bağlamsız çeviri**: çevirmenlerin anlamı tahmin etmesi, hatalara yol açması.
- **Toplu, son dakika yerelleştirmesi**: sürekli hat yerine yayın öncesi sıkışma.
- **Kültürel duyarsızlık**: yerelde rahatsız eden ya da kafa karıştıran görseller, renkler ya da örnekler.

## Olgunluk modeli

**Düzey 1, Başlangıç.** Tek dil, gömülü dizeler, Unicode olmayan varsayımlar ve birleştirmeyle kurulmuş metin. Uluslararasılaştırma tepkiseldir: her yeni yerel kodu değiştirmek demektir ve kodlama ile yerleşim hataları üretimde tesadüfen bulunur.

**Düzey 2, Geliştirme.** Bazı dizeler dışa alınmış ve yer yer Unicode kullanılıyor, ancak uygulama takımlar arasında tutarsız. Yerelleştirme elle yapılan, toplu, yayın öncesi bir çabadır; biçimlendirme, çoğul işleme ve sağdan sola desteği bir takımdan ötekine farklı ele alınır (ya da hiç alınmaz).

**Düzey 3, Standartlaştırma.** Ortak bir i18n mimarisi ve yerel farkındalığı olan biçimlendirme kitaplığı, kurum genelinde belgelenmiş ve zorlanan standarttır. Dize dışa alma lint kurallarıyla denetlenir, sözlükler ve çeviri belleğiyle bir çeviri yönetim sistemi ve sürekli hat yerindedir ve sahte yerelleştirme ile çok yerelli test (sağdan sola ve uzun metinli bir yerel dahil) CI'da çalışır.

**Düzey 4, Yönetme.** Yerelleştirme programı taban değerlere karşı ölçülür ve denetlenir. Takımlar dil kapsamını, yerelleştirme kalitesini ve kusur oranlarını, commit'ten çevrilmiş sürüme dize senkron gecikmesini, sürüm başına yakalanan kesilme ve sağdan sola işleme kusurlarını, yerel başına çeviri maliyetini ve yeni bir yereli yayına alma süresini izler; bu ölçütler sürümleri kapılar ve insan incelemesi ile makine çevirisi arasında nereye yatırım yapılacağını yönlendirir.

**Düzey 5, Orkestrasyon.** Uluslararasılaştırma ve yerelleştirme sürekli iyileştirilir ve kurum genelinde bütünleşiktir. Yerelleştirme süreklidir, makine ve insan çevirisi içerik sınıfı başına bilinçli seçilir ve kültürel uyarlama sistematiktir. Kurum, pazar ve eşitlik kanıtına göre yereller ekler, emekliye ayırır ve kapsamlarını yeniden belirler; yeni yereller sonradan uyarlama olmadan hızla ve yüksek kalitede yayına girer.

## Tartışma fikirleri

- Uluslararası talep belirsizse bir ürün ne kadar erken uluslararasılaşmalı?
- Makine çevirisi nerede kabul edilebilir ve nerede insanlar incelemeli?
- Birçok dil ve takım arasında terminolojiyi nasıl tutarlı tutarsınız?
- Eklenen çeşitleme bakımına karşı ne kadar bölgesel kültürel uyarlama değer?
- Sağdan sola ve azınlık dili desteği nasıl önceliklendirilmeli ve test edilmeli?
- Çevirmenlere hattı yavaşlatmadan yeterli bağlamı nasıl verirsiniz?

## Önemli çıkarımlar

- Mimariyi bir kez uluslararasılaştırın; içeriği birçok kez yerelleştirin.
- Her yerde Unicode kullanın, tüm dizeleri dışa alın ve çevirileri asla birleştirmeyin.
- Metin genişlemesi, sağdan sola alfabeler ve yerele özgü çoğul ve biçimlendirme kuralları için plan yapın.
- Çeviri belleği, sözlükler ve bağlamla sürekli bir yerelleştirme hattı yürütün.
- Gerçek çeviriden önce i18n hatalarını yakalamak için CI'da erken sahte yerelleştirme yapın.
- Yerelleştirme yalnızca dilsel değil kültüreldir.
- Erken uluslararasılaştırma sonradan uyarlamadan çok daha ucuzdur; kamu için yasal bir eşitlik gerekliliğidir.

## Kaynaklar ve ileri okuma

- The Unicode Consortium, *The Unicode Standard* and Common Locale Data Repository (CLDR)
- W3C Internationalisation (i18n) Activity, techniques and best practices
- Richard Ishida, W3C internationalisation articles and tutorials
- Bert Esselink, *A Practical Guide to Localisation*
- John Yunker, *Beyond Borders: Web Globalisation Strategies*
- Unicode Technical Standard #35 (locale data markup) and ICU library documentation
- IETF BCP 47 language tags
- Government multilingual service and language-access guidance
- Nielsen Norman Group and W3C articles on RTL, text expansion, and localisation UX
