# 8.5 Test ve süreç otomasyonu

## Genel bakış ve motivasyon

Test ve süreç otomasyonu, tekrarlayan, elle yapılan mühendislik ve operasyon işlerini güvenilir, makine tarafından yürütülen iş akışlarıyla değiştirme pratiğidir. Test tarafında bu, [test otomasyonu](https://en.wikipedia.org/wiki/Test_automation) demektir: doğruluğu, performansı ve güvenliği doğrulamak için sürekli çalışan otomatik test paketleri. Süreç tarafında ise yazılım teslimi ve operasyonunun çevresindeki makineyi kapsar: uyum kanıtı toplamak, operasyonel çalışma kılavuzlarını yürütmek, bilinen sorunları gidermek ve yönetişim, güvenlik ve maliyet denetimlerini uygulatmak. Birleştirici fikir basittir. Tekrar tekrar ve öngörülebilir biçimde yapılan her şey kodlanmalıdır; böylece tutarlı, hızlı ve insan angaryası olmadan çalışır.

Büyük takımlar için otomasyon, kalite ve denetimin ölçek altında çökmesini önlemenin tek yoludur. Elle test, binlerce değişiklik yapan yüzlerce mühendise yetişemez. Darboğaza dönüşür ve kapsamı tutarsız ve güvenilmez olur. Elle operasyonel prosedürler de zarar görür. Bir hizmeti yeniden başlatmak, bir kimlik bilgisini döndürmek ve denetim kanıtı toplamak, yorgun insanlar bunları geniş bir varlık alanında baskı altında yaptığında yavaş ve hataya açık hale gelir. Bu işi otomatikleştirmek sonuçları tekrarlanabilir kılar. Ayrıca yetenekli mühendisleri, gerçekten insan sezgisi gerektiren, muhakeme yoğun sorunlara odaklanmaları için serbest bırakır.

Kurumsal ve kamu bağlamlarında otomasyon, uyumu sürdürülebilir kılmanın da anahtarıdır. Düzenlemeye tabi kurumlar, denetimlerin yerinde olduğunu ve kanıtın toplandığını sürekli olarak göstermek zorundadır. Bunu elle yapmak pahalı, yavaş ve boşluklara açıktır. Kanıt toplamayı ve denetim uygulamayı otomatikleştirmek, uyumu dönemsel bir yangın tatbikatından sistemin sürekli, doğrulanabilir bir özelliğine dönüştürür. Bu "kod olarak uyum" yaklaşımı hem maliyeti düşürür hem de denetçilerin ve düzenleyicilerin gerektirdiği güvenceyi güçlendirir.

## Temel ilkeler

- Tekrarlanan, öngörülebilir ve kural tabanlı işi otomatikleştirin; insan emeğini muhakemeye saklayın.
- Otomatik testleri hızlı, güvenilir ve deterministik yapın, yoksa görmezden gelinirler.
- Testleri paralel çalıştırın ve daha erken çekin ki paket büyürken geri bildirim hızlı kalsın.
- Operasyonel prosedürleri [çalışma kılavuzu](https://en.wikipedia.org/wiki/Runbook)-olarak-kod şeklinde kodlayın; böylece sürümlenir, test edilir ve yürütülebilir olur.
- Sistemlere dışarıdan eklenen kırılgan betikler yerine iyi bütünleşmiş otomasyonu tercih edin.
- Uyum kanıtını normal iş akışlarının bir yan ürünü olarak otomatik üretin.
- Yüksek riskli eylemlerde insanı döngüde tutun; önce güvenli ve rutin olanı otomatikleştirin.

## Öneriler

### Hızlı, güvenilir, paralel test altyapısı kurun

Bir test paketi ancak mühendisler ona güvenirse ve geri bildirimi hızlı dönerse değerlidir. Paketleri birçok işçide paralel çalıştıran test altyapısına yatırım yapın; böylece test sayısı binlere çıksa bile toplam duvar saati süresi düşük kalır. Paketi bir piramit olarak yapılandırın: çok sayıda hızlı [birim testi](https://en.wikipedia.org/wiki/Unit_testing), daha az entegrasyon testi ve az sayıda uçtan uca test. O zaman geri bildirimin çoğu saniyeler içinde gelir. Kararsız testleri amansızca ortadan kaldırın. Aralıklı başarısız olan bir test hiç test olmamasından kötüdür, çünkü mühendislere başarısızlıkları görmezden gelmeyi öğretir. Entegrasyon ve uçtan uca testlerin gerçekçi, yalıtılmış altyapıya karşı çalışması için geçici, isteğe bağlı test ortamları sağlayın.

### Sürüm, uyum ve kanıt toplamayı otomatikleştirin

Otomasyonu testin ötesine, sürüm ve uyum iş akışına genişletin. İşlem hattının denetçilerin ihtiyaç duyduğu yapıtları otomatik üretmesini sağlayın: bir değişikliği kimin onayladığının, hangi testlerin çalışıp geçtiğinin, güvenlik taramalarının neyi bulduğunun ve tam olarak hangi yapıtın dağıtıldığının kayıtları. Denetimleri kod olarak ele alın; böylece gerekli kontroller tekdüze uygulanır ve sonuçları günlüğe alınır. Bu "kod olarak uyum", kanıt toplamayı bir denetim öncesi elle telaştan sürekli, her zaman güncel bir kayda dönüştürür. Ayrıca sistemin uyum duruşunu her an gözlemlenebilir kılar.

### ChatOps ve kod olarak çalışma kılavuzlarını benimseyin

Operasyonel prosedürleri, zamanla eskiyen düzyazı belgeler yerine sürüm kontrolünde tutulan yürütülebilir çalışma kılavuzları olarak kodlayın. Bir prosedür güvenli ve iyi anlaşılmışsa, onu isteğe bağlı çalıştırabilen otomasyona bağlayın. ChatOps bu operasyonları ortak bir sohbet arayüzüne getirir; böylece operatörler otomatik eylemleri şeffaf, iş birlikçi, günlüğe alınan bir konuşmada tetikler ve izler. Bu, operasyonları tüm takıma görünür kılar ve yapılanın otomatik bir kaydını oluşturur. Ayrıca daha az deneyimli mühendislerin prosedürleri güvenle çalıştırma engelini düşürür, çünkü otomasyon doğru adımları kodlar.

### Otomatik gidermeyi dikkatle uygulayın

İyi anlaşılmış, yinelenen sorunlar için bir durumu algılayıp bilinen bir düzeltmeyi uygulayan otomatik giderme inşa edin: başarısız bir süreci yeniden başlatmak, yük altında ölçeği büyütmek, dolu bir diski temizlemek ya da bir bileşeni yük devretmek gibi. Düşük riskli, yüksek güvenli gidermelerle başlayın. Kayda değer etki alanı olan her şey için insan onayı isteyin. Otomatik giderme ortalama kurtarma süresini azaltır ve tekrarlayan alarm yorgunluğunu ortadan kaldırır. Ama sağlam algılama üzerine kurulmalı ve güvenlik önlemleri içermelidir, çünkü yanlış bir sinyale göre hareket eden otomasyon bir olayı büyütebilir. Her otomatik eylemi günlüğe alın ki operatörler tam görünürlüğü korusun ve devreye girebilsin.

### Robotik süreç otomasyonunu (RPA) doğru yere koyun

[Robotik süreç otomasyonu](https://en.wikipedia.org/wiki/Robotic_process_automation), bir insanın yapacağı tıklamaları ve tuş vuruşlarını taklit ederek mevcut kullanıcı arayüzlerini ve uygulamaları sürüp görevleri otomatikleştirir. RPA, API sunmayan ve başka hiçbir biçimde entegre edilemeyen eski ya da üçüncü taraf sistemler için bir köprü olarak meşru bir yere sahiptir. Bu tür durumlarda pragmatik kullanın, ama sınırlarını bilin. Arayüz güdümlü otomasyon doğası gereği kırılgandır: arayüz değiştiğinde bozulur ve altta yatan entegrasyon eksikliğini ele almaz. Uygun bir API ya da entegrasyon varsa onu tercih edin. RPA'yı stratejik bir temel değil taktik bir geçici çözüm olarak görün ve sistemler modernleştikçe onu değiştirmeyi planlayın.

### Yönetişimi, güvenliği ve maliyet denetimlerini otomatikleştirin

Kurumsal denetimleri sürekli çalışan otomatik kontroller olarak kodlayın: altyapı korkulukları için kod olarak politika, işlem hatlarında otomatik güvenlik taraması ve maliyet anormalliklerinin ve boşta kalan kaynakların otomatik algılanması. Yönetişimi otomatikleştirmek denetimleri tekdüze ve aşılamaz kılar ve elle incelemenin asla kapsayamayacağı bir değişiklik hacmine ölçeklenir. Bir güvenlik politikasını uygulatan aynı yaklaşım, kontrolden çıkmış bir bulut faturasını ya da eksik bir zorunlu etiketi de işaretleyebilir. Yönetişim, dönemsel elle denetimden sürekli otomatik bir korkuluğa kayar.

## Ödünleşimler: artılar ve eksiler

| Seçim | Artılar | Eksiler | En uygun durum |
|---|---|---|---|
| Geniş otomatik test | Hızlı, tutarlı geri bildirim; değişimi mümkün kılar | İnşa ve bakım maliyeti; kararsızlık riski | Ölçekteki tüm takımlar |
| Kod olarak uyum | Sürekli, denetime hazır kanıt | Denetimleri kodlamak için önden mühendislik | Düzenlemeye tabi kurumlar |
| Kod olarak çalışma kılavuzları + ChatOps | Tekrarlanabilir, görünür, günlüğe alınan operasyonlar | Kodlama ve sürdürme çabası | Gerçek operasyon yükü olan takımlar |
| Otomatik giderme | Daha hızlı kurtarma; daha az angarya | Algılama yanlışsa risk | İyi anlaşılmış yinelenen sorunlar |
| RPA (arayüz otomasyonu) | API'si olmayan sistemleri köprüler | Kırılgan; entegrasyon boşluklarını maskeler | Geçici çözüm olarak eski sistemler |
| Otomatik yönetişim | Tekdüze, aşılamaz denetimler | Politika yazma ve ayarlama çabası | Büyük, yönetilen varlık alanları |

Temel ödünleşim, önden yatırım ile süregelen angarya ve risk arasındadır. Otomasyonu inşa etmek ve sürdürmek her zaman çaba ister. Kararsız testler, kırılgan RPA ya da kötü sinyallerle tetiklenen giderme gibi kötü inşa edilmiş otomasyon hiç olmamasından kötü olabilir, çünkü güveni aşındırır ya da başarısızlıkları büyütür. Disiplin üç yönlüdür: gerçekten tekrarlanabilir ve güvenilir olanı otomatikleştirin, bu otomasyonu güvenilir kılmaya yatırım yapın ve muhakeme ya da yüksek risk gerektirdiğinde insanları döngüde tutun. İyi yapıldığında otomasyon kendini kat kat öder. Özensiz yapıldığında kendi başına bir yüke dönüşür.

## Takımınızla tartışılacak sorular

1. **Entegrasyon ve uçtan uca testleriniz gerçekçi, geçici ortamlara mı karşı çalışıyor, yoksa herkesin kavga ettiği ortak bir hazırlık kutusuna mı?** Her çekme isteği için isteğe bağlı yalıtılmış ortamlar, entegrasyon ve uçtan uca testlerin takımlar birbirini engellemeden ya da ortak durumu kirletmeden gerçekçi altyapıyı sınamasına izin verir. Tek bir ortak hazırlık ortamı, daha çok takım üşüştükçe bir darboğaza ve kararsız, sıraya bağımlı başarısızlıkların kaynağına dönüşür. Geçici ortamlar ayağa kaldırıp kaldıramayacağınıza, maliyetlerinin ne olduğuna ve hangi testlerin gerçekten bunlara, hangilerinin hızlı bir bellek içi yedeğe ihtiyaç duyduğuna karar verin. Veri getirin: hazırlık ortamının ne sıklıkla çekişmeli olduğu, kaç başarısızlığın ortak ortam girişimine dayandığı ve entegrasyon katmanının güncel duvar saati süresi. Cevap hem test güvenilirliğinizi hem de piramidin üst katmanlarının geri bildirimi ne kadar hızlı döndüreceğini şekillendirir.

2. **Operasyonel prosedürler kod olarak çalışma kılavuzlarına kodlanıp ChatOps üzerinden mi sunuluyor, yoksa hâlâ zamanla eskiyen düzyazı olarak mı duruyor?** Kodlanmış, sürüm kontrollü çalışma kılavuzları test edilebilir ve yürütülebilirdir; bunları ortak bir sohbet arayüzünden çalıştırmak her eylemi görünür ve otomatik günlüğe alınmış kılar. Bu, daha az deneyimli bir nöbetçi mühendisin güvenle harekete geçmesinin önünü açar, çünkü otomasyon, kabile hafızasına güvenmek yerine doğru adımları kodlar. Hangi prosedürlerin önce bağlanacak kadar güvenli ve iyi anlaşılmış olduğuna ve insanın devreye girebilmesini nasıl koruyacağınıza karar verin. Geniş bir varlık alanı için bu şeffaflık, kimin ne zaman ne yaptığının bir denetim kaydı olarak da işler. Güncel çalışma kılavuzlarınızı getirin, hangilerinin eskidiğini not edin ve ilk kodlanacak en çok çalıştırılan iki ya da üç prosedürü belirleyin.

3. **İşlem hattınızda hangi güvenlik taramaları ve politika denetimleri birleştirmeyi engelliyor, hangileri yalnızca uyarıyor?** Otomatik yönetişim ancak denetimler aşılamazsa inşa etmeye değer, çünkü yalnızca uyaran bir kontrol, tıpkı bir wiki politikası gibi, son teslim baskısı altında görmezden gelinir. Kontrol kontrol karar verin, neyin engellediğine ve neyin uyardığına: kritik bir güvenlik açığı ya da eksik bir şifreleme etiketi muhtemelen engeller, daha düşük önemdeki bir stil bulgusu uyarabilir. Ölçekte, hiçbir elle incelemenin kapsayamayacağı bir değişiklik hacminde güvenlik ve maliyet korkuluklarını tekdüze uygulatmanın yolu budur. Güncel kontrol envanterinizi getirin ve her birini engelleyici ya da danışmanlık olarak işaretleyin, sonra yanlış pozitif oranını tartışın, çünkü gürültülü bir engelleyici kontrol insanlara istisna talep etmeyi öğretir. Engelleme ile uyarma arasındaki çizgi, yönetişiminizin ya dişli olduğu ya da olmadığı yerdir.

4. **İnsan önce onaylamadan hareket etmelerine hangi otomatik gidermelere izin vermeye hazırız ve algılama yanlışsa etki alanı nedir?** Otomatik giderme kurtarma süresini ve alarm yorgunluğunu keser, ama yanlış bir sinyalle tetiklenen bir düzeltme küçük bir aksamayı tam bir kesintiye çevirebilir; bu yüzden neyin gözetimsiz çalışacağı bir kolaylık değil bir risk kararıdır. Karşıt çekimleri tartın: gözetimsiz eylem en hızlısı ama en riskli olanıdır, döngüde insan onayı ise daha güvenlidir ama kaldırmaya çalıştığınız gecikmeyi ve angaryayı geri getirir. Aday gidermeleri sıklığa ve en kötü durum etki alanına göre sıralı getirin; her birinin arkasındaki algılamanın geçmiş yanlış pozitif oranını ve her eylemin günlüğe alınıp alınmadığını ve geri alınabilir olup olmadığını da. Büyük bir kurumsal ya da kamu varlık alanı için, üretim verisine ya da vatandaşa dönük hizmetlere dokunan her şey için resmi bir değişiklik yetkilisi ve geri alma planı ekleyin, çünkü denetlenemeyen ya da geri alınamayan bir otomatik giderme, düzenleyicinin sizi kapatmaya zorlayacağı bir giderme olur.

5. **Otomasyonumuzun bakımını, bir yüke dönüşmesin diye nasıl fonlayıp sahiplendiririz?** Testler, çalışma kılavuzları, politika denetimleri ve RPA botlarının hepsi çevrelerindeki sistemler değiştikçe çürür ve ihmal edilmiş otomasyon hiç olmamasından kötüdür: eski bir çalışma kılavuzu krizde yanlış güven verir ve bozuk bir RPA botu işi sessizce düşürür. Gerilim şudur: bakım aynı mühendisler için özellik işiyle yarışır ve bir şey bozulana kadar görünmezdir; bu yüzden son teslim baskısı altında ilk kesilen şeydir. Otomasyon varlıklarının güncel envanterini, kararsız test ve bozuk bot birikimini ve bakıma zaten giden mühendis saatlerinin bütçelenenle karşılaştırılan dürüst bir tahminini getirin. Kurumsal ya da kamu ortamında her kritik otomasyon için hesap verebilir bir sahip belirleyin ve bakımını açık bir kalem olarak fonlayın, çünkü denetçiler ve olay incelemeleri, bakımsız bir kontrol sessizce başarısız olduğunda kimin sorumlu olduğunu soracaktır.

6. **RPA ile otomatikleştirdiğimiz her eski sistem için, o RPA'yı gerçek bir entegrasyon lehine emekliye ayırmanın somut planı ve tetikleyicisi nedir?** RPA, API sunmayan sistemler için meşru bir köprüdür, ama çıkış planı olmayan bir köprü sessizce kalıcı, kırılgan, her arayüz değişikliğinde bozulan ve aşmak için kurulduğu entegrasyon boşluğunu kökleştiren bir altyapıya dönüşür. Ödünleşim gerçektir: RPA şimdi hızlı ve ucuz değer sunar, uygun bir API entegrasyonu ise önden daha pahalıdır ama dayanıklıdır; bu yüzden disiplin RPA'yı bir satın alma değil, vadesi belli bir borç olarak görmektir. Üretimdeki RPA botlarının listesini, her birinin bağlı olduğu sistemleri, her birinin ne sıklıkla bozulduğunu ve alttaki sistem için bir modernizasyon ya da entegrasyon çalışmasının gerçekten fonlanıp planlanıp planlanmadığını getirin. On yıllık çekirdek uygulamalar taşıyan kurumsal ve kamu varlık alanları için her RPA botunu adı konmuş bir modernizasyon kilometre taşına bağlayın, çünkü emeklilik tarihi olmadan sessizce kritik hale gelmiş RPA, kazıdığı arayüzün değişmeye devam ettiği her yıl birikerek büyüyen teknik borçtur.

## Sektör merceği

**Girişim.** İki ya da üç mühendisle ve altyapı inşa edecek zaman olmadan, her değişiklikte birkaç dakikada çalışan küçük, hızlı bir test piramidi tutun ve her kararsız testi o hafta düzeltilecek ya da silinecek gerçek bir hata olarak görün. Henüz ihtiyacınız olmayan ağır uyum araçlarını ve kod olarak politikayı atlayın ve yalnızca en çok çalıştırılan iki ya da üç operasyonel düzeltmenizi sohbetten tetiklenen basit betikler olarak kodlayın. Günlük angaryayı kaldıranı otomatikleştirin ve bir yönetişim sorununuz olmadan yönetişim makinesi inşa etmeye direnin.

**Küçük işletme.** Özel bir test ya da platform uzmanı olmadan, zaten ödediğiniz araçlara gömülü otomasyona yaslanın: CI hizmetinin yerleşik test çalıştırıcıları, tarama eklentileri ve özel bir test altyapısı inşasından çok yönetilen ortamlar. Satın alma-ya-karşı-inşa seçimini gerçekçi biçimde sürdürebileceğiniz bakım üzerine kurun, çünkü kimsenin sürdüremediği zekice özel bir işlem hattı, daha sade bir barındırılan işlem hattından kötü bir sonuçtur. RPA'yı idareli ve yalnızca bir satıcı aracının başka türlü entegre edemeyeceğiniz bir sistemi köprülediği yerde kullanın.

**Kurumsal.** Birçok takım boyunca hedef, elle incelemenin kapsayamayacağı ölçekte tekdüze, aşılamaz denetimlerdir: geçici ortamlı ortak paralel test altyapısı, kod olarak politika korkulukları ve her işlem hattı çalışmasından otomatik üretilen uyum kanıtı. Arayüzleri standartlaştırın ki takımlar her biri kırılgan betikleri yeniden icat etmek yerine giderme ve çalışma kılavuzu araçlarını yeniden kullansın ve otomasyonu net bakım bütçeleri olan, sahipli ve fonlanmış bir portföy olarak yönetin. Bir takımda yalnızca uyaran bir kontrolün başka bir takımda engelleyici sayılmamasına dikkat edin, çünkü tutarsız uygulama, için ödeme yaptığınız güvenceyi baltalar.

**Kamu.** Tedarik kuralları, şeffaflık yükümlülükleri ve sürekli izleme zorunlulukları kod olarak uyumu neredeyse şart kılar: her işlem hattı çalışması, kontrol edilen denetimleri, yapılan taramaları ve verilen onayları kurcalamaya karşı belirgin, denetime hazır kanıt olarak kaydetmelidir. Gelecekteki bir sözleşmenin başka bir tedarikçiye geçebilmesi için tescilli kilitlenme yerine açık, taşınabilir otomasyonu tercih edin ve vatandaşa dönük hizmetlere dokunan her giderme için hesap verebilir bir insan tutun. On yıllık bir sistem RPA'yı zorunlu kıldığında, bunu kamuya açık bir modernizasyon planı olan bilinçli, geçici bir köprü olarak belgeleyin ve yönetişim kontrollerini her değişiklikte zorunlu güvenlik temeline göre tutun.

## Örnekler

**Girişim.** Yedi kişilik bir girişim, çoğunlukla hızlı birim testlerinden ve birkaç entegrasyon testinden oluşan yalın bir test piramidi tutar; hepsi paralel çalışır ve tam paket her çekme isteğinde üç dakikanın altında biter. Bir test kararsızlaşmaya başladığında, onu gerçek bir hata olarak görür ve o hafta düzeltir ya da silerler, çünkü bu kadar küçük bir takımda görmezden gelinen tek bir kırmızı derleme tüm paketin güvenini aşındırır. Ayrıca en yaygın iki operasyonel düzeltmelerini, takılmış bir işçiyi yeniden başlatmayı ve dolu bir diski temizlemeyi, Slack'ten tetiklenen küçük betikler olarak kodlarlar; böylece nöbetçi kim olursa, onları yazan tek mühendisi çağırmadan güvenle çalıştırabilir.

**Kurumsal.** Büyük bir e-ticaret şirketi, on binlerce testten oluşan bir test paketi çalıştırır; paket bir işçi filosuna paralelleştirilir ve tam paket dakikalar içinde tamamlanır. Gerçekçi entegrasyon testi için her çekme isteğinde geçici ortamlar ayağa kalkar. Operasyonlar ChatOps üzerinden yürür: nöbetçi mühendisler kodlanmış çalışma kılavuzlarını sohbetten tetikler ve aşırı yüklenmiş bir hizmet gibi yaygın başarısızlıklar, eylem inceleme için günlüğe alınarak otomatik giderilir. İşlem hattı güvenlik taraması ve onay kanıtını otomatik topladığı için yıllık denetim, elle kanıt avı yerine her zaman güncel bir kayda dayanır.

**Kamu.** Sıkı sürekli izleme gereksinimlerine tabi bir kamu kurumu kod olarak uyumu uygular. Her işlem hattı çalışması kontrol edilen denetimleri, yapılan taramaları ve verilen onayları kaydeder ve denetçileri istendiğinde tatmin eden, kurcalamaya karşı belirgin kanıt üretir. Çekirdek sistemlerinden biri API'si olmayan on yıllık bir uygulama olduğu için kurum, modernizasyon çalışması sürerken ona veri girişini otomatikleştirmek üzere RPA'yı bilinçli bir köprü olarak kullanır; uygun bir entegrasyon var olduğunda RPA'yı emekliye ayırmak için de açık bir planı vardır. Otomatik yönetişim kontrolleri her altyapı değişikliğinde zorunlu güvenlik temelini uygulatır.

## İş gerekçesi: motivasyonlar, YG ve TSM

Test ve süreç otomasyonunun YG'si, geri kazanılan mühendis zamanı, daha hızlı ve güvenli teslim, daha çabuk olay kurtarma ve dramatik biçimde düşük uyum maliyeti olarak görünür. Otomatik test, teslim performansının altında yatan hızlı ve güvenli değişimi mümkün kılar. Otomatik operasyonlar ve giderme, takımları ve bütçeleri tüketen angaryayı ve kesinti süresini keser. Kod olarak uyum, bir denetimi haftalarca elle hazırlıktan rutin bir sorguya çevirebilir; bu hem mali hem itibar açısından bir tasarruftur.

TSM karşılaştırması, otomasyonu inşa etmenin ve sürdürmenin gerçek, süregelen maliyetini otomatikleştirmemenin maliyetine karşı tartar. Elle test ve operasyon yalnızca harcanan saatlere mal olmaz. Kaçan hatalara, uzayan olaylara, uzman personeli tüketen denetimlere ve tekrarlayan angarya yapan mühendislerin tükenmişliğine de mal olur. Liderlik için argüman açıktır: otomasyon tekrarlayan operasyonel gideri ve riski ölçeklenen bir tek seferlik-artı-bakım yatırımına dönüştürür ve kaliteyi ve uyumu dönemsel değil sürekli kılar. Bir uyarı açıkça söylenmeye değer. Otomasyon sürdürülmeli ve güvenilir olmalıdır; fonlanmayan, ihmal edilen otomasyon bir yüke dönüşerek çürür.

## Anti-kalıplar ve tuzaklar

- **Hoşgörülen kararsız testler.** Aralıklı başarısızlıklar güveni yok eder ve mühendislere kırmızı sonuçları görmezden gelmeyi öğretir.
- **Bozuk bir süreci otomatikleştirmek.** Kötü bir iş akışını otomatikleştirmek karmaşanın yalnızca daha hızlı olmasını sağlar; önce süreci düzeltin.
- **Strateji olarak RPA.** Kırılgan arayüz otomasyonuna kalıcı bir çözüm olarak güvenmek entegrasyon boşluklarını maskeler ve kökleştirir.
- **Sağlam algılama olmadan giderme.** Kötü sinyallerle tetiklenen otomatik düzeltmeler bir olayı büyütebilir.
- **Eskimiş düzyazı olarak çalışma kılavuzları.** Güncelliğini yitirmiş belgelerde yaşayan prosedürler krizde yanlış güven verir.
- **Elle toplanan uyum kanıtı.** Dönemsel elle kanıt avları pahalıdır ve denetimler arasında boşluklar bırakır.
- **Yüksek riskli eylemlerde döngüde insan olmaması.** Tehlikeli operasyonların tam otomasyonu, felaketleri önleyen muhakemeyi ortadan kaldırır.

## Olgunluk modeli

**Düzey 1, Başlangıç.** Test ve operasyonlar büyük ölçüde elle ve tepkiseldir. Kapsam gelişigüzeldir, prosedürler insanların kafasında ya da eski belgelerde durur, giderme olaylar sırasında elle yapılır ve uyum kanıtı her denetimden önce telaş içinde derlenir.

**Düzey 2, Geliştirme.** Otomatik testler vardır ama yavaş, kararsız ya da tutarsız çalışır ve uygulamalar takımlar arasında büyük ölçüde değişir. Bazı operasyonel betikler ve çalışma kılavuzları ceplerde bulunur, ama giderme hâlâ elle yapılır ve yönetişim sürekli kontroller yerine dönemsel incelemeyle uygulanır.

**Düzey 3, Standartlaştırma.** Hızlı, paralel, güvenilir test altyapısı kurum genelinde belgelenmiş standarttır. Kod olarak çalışma kılavuzları ve ChatOps genel kullanımdadır, uyum kanıtı işlem hattı çalışmalarından otomatik üretilir ve yönetişim denetimleri takımlar arasında tutarlı uygulanan, zorunlu otomatik kontroller olarak çalışır.

**Düzey 4, Yönetme.** Otomasyonun kendisi başlangıç değerlerine karşı ölçülür ve kontrol edilir. Kararsız test oranını, paket duvar saati süresini, otomatik giderilen olaylar için ortalama kurtarma süresini, otomatik kanıtı olan denetimlerin payını ve engelleyici kontrollerdeki yanlış pozitif oranlarını izler ve her ölçütü üzerinde anlaşılmış bir hedefe bağlarsınız. Giderme ve kapsam kararları bu veriyle yönlendirilir ve her otomatik eylem günlüğe alınır; böylece eğilimler ve gerilemeler tahmin edilmek yerine görünür olur.

**Düzey 5, Orkestrasyon.** Otomasyon sürekli iyileştirilir ve kurum genelinde bütünleştirilir. Otomatik giderme rutin olayları kanıtlanmış güvenlik önlemleriyle halleder, uyum sürekli ve her zaman denetime hazırdır ve test, operasyon ve yönetişim araç zincirleri sistemler değiştikçe uyum sağlar; entegrasyonlar olgunlaştıkça RPA köprüleri etkin biçimde emekliye ayrılır. İnsanlar muhakemeye odaklanırken makineler tekrarlanabilir olanı halleder ve tüm sistem kanıta dayanarak yeniden dengelenir.

## Tartışma fikirleri

- Hangi operasyonel prosedürlerin tamamen otomatikleştirilmesi güvenlidir ve hangileri döngüde bir insan tutmalıdır?
- Büyük bir test paketini büyürken nasıl hızlı ve kararsızlıktan arınmış tutarsınız?
- RPA eski sistemleriniz için nerede haklı bir köprüdür ve onu emekliye ayırma planı nedir?
- Hangi denetimleri önce elle denetimden kod olarak sürekli uyuma dönüştürebilirsiniz?
- Büyütülmüş olay riskine girmeden otomatik gidermeye nasıl güven inşa edersiniz?
- Otomasyonun gerektirdiği süregelen bakımı, bir yüke dönüşmesin diye nasıl fonlarsınız?

## Önemli çıkarımlar

- Tekrarlanan, öngörülebilir ve kural tabanlı olanı otomatikleştirin; insan emeğini muhakemeye ve yüksek riskli kararlara saklayın.
- Otomatik testleri hızlı, paralel ve güvenilir yapın ve kararsızlığı amansızca ortadan kaldırın.
- Operasyonları kod olarak çalışma kılavuzlarına kodlayın ve görünürlük ve kayıt için ChatOps üzerinden sunun.
- Uyum kanıtını otomatik üretin ki denetimler sürekli, güncel bir kayda dayansın.
- RPA'yı yalnızca API'si olmayan sistemler için bilinçli, geçici bir köprü olarak kullanın ve emekliliğini planlayın.
- Yönetişim, güvenlik ve maliyet denetimlerini sürekli otomatik kontroller olarak uygulatın; riskli eylemleri insanlar gözetsin.

## Kaynaklar ve ileri okuma

- Lisa Crispin and Janet Gregory, *Agile Testing: A Practical Guide for Testers and Agile Teams*.
- Jez Humble and David Farley, *Continuous Delivery*.
- Betsy Beyer, Chris Jones, Jennifer Petoff, and Niall Richard Murphy (eds.), *Site Reliability Engineering* (see the chapter on eliminating toil).
- Gene Kim, Jez Humble, Patrick Debois, and John Willis, *The DevOps Handbook*.
- Nicole Forsgren, Jez Humble, and Gene Kim, *Accelerate*.
- NIST Special Publication 800-53 and 800-137 (continuous monitoring).
- Open Policy Agent documentation (policy as code).
