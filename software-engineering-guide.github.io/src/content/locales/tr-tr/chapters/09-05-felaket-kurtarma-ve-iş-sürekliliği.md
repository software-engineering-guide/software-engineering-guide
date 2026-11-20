# 9.5 Felaket kurtarma ve iş sürekliliği

## Genel bakış ve motivasyon

Er ya da geç, planlamadığınız bir şey bir sistemi çökertecek: bölge çapında bir bulut kesintisi, parmağı kayan bir `DROP TABLE`, bir veri merkezindeki sel, patlayan bir fidye yazılımı ya da bir gecede ortadan kaybolan bir tedarikçi. Soru, aksamanın gelip gelmeyeceği değil; ne kadar hızlı toparlandığınız ve bu süreçte ne kadarını kaybettiğinizdir. Bu bölüm, kötü gün gelmeden önce ona hazır olmakla ilgilidir.

Bu hazırlığa iki disiplin cevap verir ve bunlar aynı şey değildir. [İş sürekliliği planlaması](https://en.wikipedia.org/wiki/Business_continuity_planning) (BCP), bir aksama boyunca kurumun tamamını işler tutar: insanlar, ofisler, iletişim, maaşlar ve müşterilerin dayandığı kritik iş süreçleri. [Felaket kurtarma](https://en.wikipedia.org/wiki/Disaster_recovery) (DR), BT sistemlerini ve verilerini çöktükten sonra geri getirmenin daha dar, teknik işidir. Süreklilik hedeftir; kurtarma araçlardan biridir. Her sunucuyu geri getirebilir ve yine de müşterilerinizi yarı yolda bırakabilirsiniz; çünkü kimse felaketi kimin ilan edebileceğini ya da onlara nasıl ulaşılacağını bilmiyordur. Bu bölüm DR'yi bir mühendislik pratiği, BCP'yi ise onun hizmet ettiği iş çerçevesi olarak ele alır.

Büyük takımlar için riskler sizinle birlikte büyür. Bir kurum; düzenleyici kurtarma yükümlülükleri, çok bölgeli ayak izleri ve bir avuç tedarikçide yoğunlaşma riski taşır. Kamu, temel işlevleri vatandaşlar için sürdürme yasal görevini taşır; bu, işlerin sürekliliği (continuity of operations) olarak kodlanmıştır. İkisi de, denenmemiş bir planın en kötü anda keşfedeceğiniz bir yükümlülük olduğu bir denetim altında çalışır. Kurtarma, güvenilirliğin (bölüm 9.1) ve olay müdahalesinin (bölüm 9.3), tasarımla ortadan kaldıramayacağınız başarısızlıklardan sağ çıkma gibi daha zor soruyla buluştuğu yerdir.

## Temel ilkeler

- **Süreklilik, kurtarmadan geniştir.** Sunucuları geri getirmek, işin çalışmaya devam etmesiyle aynı şey değildir.
- **İki rakam her şeyi belirler.** İş etkisinden belirlenen kurtarma süresi hedefi (RTO) ve kurtarma noktası hedefi (RPO), her kararı boyutlandırır.
- **Denenmemiş yedek yedek değildir.** Hiç yapmadığınız bir geri yükleme bir yetenek değil, bir umuttur.
- **Yedeğin bir hedef olduğunu varsayın.** Fidye yazılımı ilk yedeklerinizi avlar; bu yüzden kopyaları değiştirilemez ve çevrimdışı tutun.
- **Hafızadan değil, koddan yeniden kurun.** Altyapıyı kaynaktan yeniden yaratamıyorsanız onu güvenilir biçimde kurtaramazsınız.
- **Neye bağlı olduğunuzu haritalayın.** En yavaş üst akış bağımlılığınız kadar hızlı kurtarırsınız.
- **Kurtarmayı başka herhangi bir sistem gibi ölçün.** Bir slayda yazdığınız rakamlar değil, gerçek tatbikatlardan çıkan gerçek RTO ve RPO.

## Öneriler

### RTO ve RPO'yu bir iş etkisi analizinden belirleyin

Her kurtarma kararı iki rakamdan türer; bu yüzden önce onları doğru belirleyin. **Kurtarma süresi hedefi (RTO)**, bir sistemin zararın kabul edilemez hale gelmesinden önce ne kadar süre kapalı kalabileceğidir. **Kurtarma noktası hedefi (RPO)**, ne kadar veri kaybetmeyi göze alabileceğinizdir; geri dönebileceğiniz son sağlam kopyanın yaşı olarak ölçülür. Bir ödeme defteri dakikalar mertebesinde bir RTO ve sıfıra yakın bir RPO isteyebilir; iç bir analitik panosu her ikisinden de bir günü tolere edebilir. Bunları mühendislik içinde belirleyemezsiniz. Onları, iş süreçlerini aksamalarının maliyetine göre sıralayan ve her birini ihtiyaç duyduğu sistemlere ve verilere kadar izleyen bir [iş etkisi analizinden](https://en.wikipedia.org/wiki/Business_impact_analysis) (BIA) türetin. Daha sıkı hedefler daha pahalıdır; bu yüzden BIA, önemsiz bir hizmeti gereğinden fazla donatmanızı ve kritik bir hizmeti yetersiz korumanızı engelleyen şeydir.

### Yedeklemeyi doğru yapın: 3-2-1 kuralı, değiştirilemezlik ve test

Yedekler her kurtarma stratejisinin altındaki tabandır ve çoğu kurum bunu sandığından kötü yapar. **3-2-1 kuralı** olarak bilinen [yedekleme](https://en.wikipedia.org/wiki/Backup) disiplinini izleyin: verinizin en az üç kopyasını, iki farklı ortamda ya da sistemde ve bir kopya saha dışında tutun. Modern tehditler iki gereksinim daha ekler. En az bir kopyayı **değiştirilemez** (bir saklama penceresi boyunca bir kez yazılan, silinemeyen) ve ideal olarak **çevrimdışı ya da hava boşluklu** tutun; çünkü fidye yazılımı artık kendini duyurmadan önce ulaşılabilir yedekleri kasıtlı olarak şifreliyor ya da siliyor. Hepsinden önemlisi, geri yüklemeleri bir takvime göre test edin. Denenmemiş bir yedek yedek değil, denenmemiş bir varsayımdır; ve bir tatbikatta bulduğunuz başarısızlıklar (bozuk arşivler, eksik şifreleme anahtarları, yanlış birimin yedekleri) gerçek bir olayda sizi bitirecek olanların tam kendisidir.

### Maliyete karşı hız yelpazesi boyunca bir DR stratejisi seçin

DR stratejileri parayı kurtarma hızıyla takas eder ve herkes için tek bir katman satın almak yerine, her sistem için RTO ve RPO'suna göre seçmelisiniz. Yelpazeyi dört kalıp sabitler. **Yedekle ve geri yükle** en ucuz ve en yavaş olanıdır: felaket vurduğunda yedeklerden yeniden kurarsınız; RTO saatlerden günlere uzanır. **Pilot ışığı** minimal bir çekirdeği (çoğaltılan veritabanları, yerinde çekirdek yapılandırma) ısıtılmış ama küçültülmüş halde tutar, genişlemeye hazırdır. **Sıcak bekleme**, yük devrinde büyüttüğünüz, tam yığının daha küçük, her zaman açık bir kopyasını çalıştırır ve RTO'yu dakikalara indirir. **Çok siteli aktif-aktif**, canlı trafiğe hizmet eden iki ya da daha fazla konumda tam kapasite çalıştırır; en yüksek maliyet ve karmaşıklıkla sıfıra yakın RTO verir. Katmanı, iş biriminin onayladığı rakama eşleyin ve pilot ışığına tahammül eden bir sistem için aktif-aktif fiyatı ödemeyin.

### Veriyi tutarlılık ödünleşimini aklınızda tutarak çoğaltın

Kurtarma hızı, bekleme verinizin ne kadar güncel olduğuna bağlıdır ve burada [dağıtık sistemlerin](https://en.wikipedia.org/wiki/Distributed_computing) (bölüm 3.3) zor problemlerini devralırsınız. **Eşzamanlı çoğaltma**, her yazmayı onaylamadan önce ikinci bir konumda doğrular; artan yazma gecikmesi ve mesafede sert bir sınır pahasına sıfıra yakın bir RPO verir. **Eşzamansız çoğaltma** yerelde onaylar ve değişiklikleri sonra gönderir; bu yüzden hızlı ve coğrafi olarak esnektir ama yük devrinde kaybedeceğiniz bir çoğaltma gecikmesi penceresi bırakır. Bedava bir seçim yoktur: daha güçlü tutarlılık gecikmeye, daha zayıf tutarlılık veriye mal olur. Her veri deposu için RPO'sundan karar verin ve tipik çoğaltma gecikmenizi bilin; çünkü kötü bir günde gerçek RPO'nuz, tasarım belgesindeki rakam değil, o gecikmedir.

### Kod olarak altyapıyla koddan yeniden kurun

Elle sağladığınız bir ortamı güvenilir biçimde kurtaramazsınız, çünkü kimse her tıklamayı hatırlamaz. Ortamlarınızı [kod olarak altyapı](https://en.wikipedia.org/wiki/Infrastructure_as_code) (bölüm 8.2) biçiminde tanımlayın; böylece tüm bir yığın, sürüm kontrollü kaynaktan bilinen sağlam bir durumda yeniden yaratılabilir. Bu, kurtarmayı bir arkeoloji projesinden tekrarlanabilir bir işlem hattı çalıştırmasına çevirir, bekleme bölgenizi dürüst tutar (ikisi aynı koddan kurulduğunda daha az kayar) ve bir ele geçirilmeden sonra yeni bir hesapta ya da bölgede kurtarma altyapısı ayağa kaldırmanın temiz bir yolunu verir. Kodu, gizli bilgi referanslarını ve çalışma kitaplarını birincil ortamınızın kaybından sağ çıkacak bir yerde saklayın.

### İhtiyaç duymadan önce bağımlılıkları haritalayın

Sistemler birbirinden bağımsız değil, ağlar halinde çöker ve kurtarma, unuttuğunuz bağımlılıkta tıkanır. Her kritik sistemin çalışmak için neye ihtiyaç duyduğunu haritalayın: üst akış hizmetleri, DNS, kimlik ve kimlik doğrulama, sertifika otoriteleri, mesaj kuyrukları ve üçüncü taraf API'ler ile SaaS sağlayıcıları. Kurtarma sırasını not edin; çünkü bir uygulamayı veritabanından ya da kimlik sağlayıcısından önce ayağa kaldırmak yalnızca ikinci bir kesinti üretir. Dış tedarikçilere özellikle dikkat edin; çünkü kurtarmanız onlarınkiyle sınırlıdır ve buna dair hiçbir görünürlüğünüz olmayabilir. Bu haritalama doğrudan dayanıklılığa ve zarif bozulmaya (bölüm 3.5) bağlanır: bir sistemin ne kadar az sert bağımlılığı varsa o kadar hızlı geri gelir.

### Kurtarmayı bir olay değil, bir pratik olarak test edin

Uygulamadığınız bir DR planı kurgudur. Bir test merdiveni kurun. Bir **masa başı tatbikatı**, roller, kararlar ve iletişimdeki boşlukları bulmak için takımı bir senaryodan kâğıt üzerinde geçirir. Bir **oyun günü**, canlıya benzer bir ortama gerçek, kontrollü bir başarısızlık enjekte eder. Bir **tam yük devri tatbikatı** gerçekten kurtarma sitesine geçer ve onun üzerinde çalışır. Bunları bir ritimle çalıştırın, senaryoları döndürün (kilit bir kişinin ya da tedarikçinin kaybı dahil) ve sonucu ölçün: elde ettiğiniz **gerçek RTO ve RPO'yu** kaydedin ve hedefle karşılaştırın. Ölçülen ve vaat edilen kurtarma arasındaki fark, sahip olduğunuz en dürüst güvenilirlik metriğidir ve onu kapatmak tatbikatın bütün amacıdır.

### Siber kurtarmayı kendi senaryosu olarak planlayın

Fidye yazılımı ve yıkıcı siber saldırılar sıradan DR'nin varsayımlarını bozar; bu yüzden onları ayrı ele alın. Doğal bir felakette verileriniz başka bir yerde sağlamdır; bir [fidye yazılımı](https://en.wikipedia.org/wiki/Ransomware) olayında verileriniz ve çoğu zaman yedekleriniz silahtır ve kurtarma ortamınızın kendisi de ele geçirilmiş olabilir. Bir **temiz oda kurtarması** planlayın: değiştirilemez kopyalardan geri yüklediğiniz, sızmayı taradığınız ve herhangi bir şeyi yeniden bağlamadan önce kimliği ve kimlik bilgilerini yeniden kurduğunuz yalıtılmış, güvenilir bir ortam. Bilinen son temiz noktanızın hangi yedek olduğunu bilin ve onu bulmanın, olağan RTO'nuzun hiç bütçelemediği adli analiz zamanı aldığını bekleyin. Değiştirilemez, çevrimdışı kopyaların maliyetini hak ettiği yer burasıdır ve bu, olay yönetimine (bölüm 9.3) ve ihlal ele alma için uyum ve yönetişim yükümlülüklerine (bölüm 4.6) sıkıca bağlanır.

## Ödünleşimler: artılar ve eksiler

| DR stratejisi | Artılar | Eksiler |
|---|---|---|
| Yedekle ve geri yükle | En ucuz; basit; düşük süregelen maliyet | Yavaş RTO (saatlerden günlere); daha büyük RPO |
| Pilot ışığı | Düşük maliyet; çekirdek veri sıcak ve hazır | Elle büyütme; kurtarma yine de gerçek zaman alır |
| Sıcak bekleme | Hızlı RTO (dakikalar); tam yığın kanıtlanmış | Çalışan ikinci bir ortamın süregelen maliyeti |
| Çok siteli aktif-aktif | Sıfıra yakın RTO; tek site arızası yok | En yüksek maliyet ve karmaşıklık; tutarlılık zor |
| Eşzamanlı çoğaltma | Sıfıra yakın RPO | Yazma gecikmesi; mesafeyle sınırlı; daha sıkı bağlaşım |
| Eşzamansız çoğaltma | Hızlı, esnek, coğrafi olarak özgür | Çoğaltma gecikmesine eşit veri kaybı penceresi |

Temel gerilim, kurtarma hızının ve veri tazeliğinin ikisinin de para ve karmaşıklığa mal olması ve hiçbir katmanda hiçbirinin bedava olmamasıdır. Bunu kurum başına değil, sistem başına çözün: iş etkisi analizinin her kritik sisteme bir RTO ve RPO atamasına izin verin, sonra tam olarak onu karşılayan stratejiyi satın alın. Aktif-aktif parasını bir raporlama aracına harcamak, buna ihtiyaç duyan defteri aç bırakır; tersi ise ihmaldir. Disiplin, harcamayı iş biriminin sahip olduğu rakamla eşleştirmek ve sistemlerin önemi değiştikçe bu eşleşmeyi yeniden gözden geçirmektir.

## Takımınızla tartışılacak sorular

1. **Kritik sistemlerinizin her birinin RTO ve RPO'su nedir ve bunları iş tarafında kim onayladı?** Bu rakamları yalnızca mühendislik uydurduysa bunlar tahmindir ve tahminler ya fazla cömert ya da hiç finanse edilmez. Kurtarma süresi ve kurtarma noktası hedefleri, süreçleri aksamalarının maliyetine göre sıralayan bir iş etkisi analizinden çıkmalıdır; böylece defter dakikalar, iç wiki ise bir gün alır. Mevcut katmanlamanızı getirin ve her iş sürecinden sorumlu kişinin, tasarladığınız veri kaybını ve kesinti süresini gerçekten kabul edip etmeyeceğini sorun. Büyük bir kurumda bu konuşma, her şeyi eşit korumanın, yani hiçbir şeyi iyi korumamanın pahalı hatasını önleyen şeydir. Mühendislik dışında kimse rakamları söyleyemiyorsa henüz hedefleriniz yok, umutlarınız var demektir.

2. **En son ne zaman gerçek bir geri yükleme yaptınız ve elde ettiğiniz gerçek RTO ve RPO'yu ölçtünüz mü?** Hiç geri yüklemediğiniz bir yedek denenmemiş bir varsayımdır ve sizi öldüren hata biçimleri (bozuk arşivler, kaybolan şifreleme anahtarları, yanlış birimin anlık görüntüsü, ayağa kalkmayan bir bağımlılık) yalnızca denediğinizde ortaya çıkar. Son masa başı tatbikatınızın değil, son tam yük devri tatbikatınızın tarihini ve sonucunu, ayrıca elde ettiğiniz kurtarma ile vaat ettiğiniz kurtarma arasındaki farkı getirin. Büyük bir takım için tek bir sistemin tek bir başarılı geri yüklemesi diğerlerini kanıtlamaz; bu yüzden kritik sistemlerin geçen yıl içinde uçtan uca kurtarılan kesrini sorun. Ölçülen fark en dürüst güvenilirlik rakamınızdır ve onu söyleyemiyorsanız planınız, aksi kanıtlanana kadar kurgudur.

3. **Fidye yazılımı bu gece üretiminizi şifreleyip yedeklerinize ulaşsaydı, bilinen son temiz kopyanız hangisi olurdu ve nerede yeniden kurardınız?** Olağan felaket kurtarma verinizin başka bir yerde güvende olduğunu varsayar ve yıkıcı bir siber saldırı, verinizi ve yedeklerinizi silaha çevirerek tam da bu varsayımı bozar. En az bir yedek kopyanın değiştirilemez ve çevrimdışı olup olmadığını, son temiz geri yükleme noktasını nasıl belirleyeceğinizi ve üretimin kendisi ele geçirildiğinde güvenilir bir temiz oda ortamının nereden geleceğini sorun. Bu senaryo, normal RTO'nuzun hiç bütçelemediği adli analiz zamanına ihtiyaç duyar; bu yüzden temiz bir nokta bulmanın gerçekte ne kadar sürdüğüne dair dürüst bir tahmin getirin. Kurumsal ve kamu takımları için bu aynı zamanda bir uyum olayıdır (bölüm 4.6) ve ihlal bildirim saatleri paralel işler. Cevap "en son yedeği geri yükleriz" ise bunun için hiç plan yapmamışsınız demektir.

4. **Hangi sisteminiz iş etkisi analizinin haklı çıkarmadığı bir kurtarma katmanına para ödüyor ve hangisi tehlikeli biçimde yetersiz korunuyor?** Kurtarma hızı ve veri tazeliği her katmanda para tutar; bu yüzden toptan bir ilke ya bir raporlama aracına aktif-aktif bütçesi harcar ya da gerçekten buna ihtiyaç duyan defteri aç bırakır. Rekabet eden çekim gerçektir: tek bir standart katmanı birçok takımın işletmesi çok daha basittir; sistem başına katmanlama ise harcamayı değerle eşleştirir ama bir sistemin önemi kaydıkça sürekli bakım ister. Her kritik sistem için mevcut DR stratejisini, hedeflediği RTO ve RPO'yu, bekleme ve çoğaltmasının aylık maliyetini ve katmanlamanın taze bir etki analizine karşı en son ne zaman gözden geçirildiğini getirin. Kurumsal ya da kamu ortamında uyumsuz bir katman bölgeler boyunca çoğalır ve denetim hem harcadığınız parayı hem kabul ettiğiniz maruziyeti haklı çıkarmanızı ister; bu yüzden açıklanamayan bir aktif-aktif fatura ile korumasız bir kritik hizmet eşit derecede savunması zordur.

5. **Kritik sistemlerinizin kurtarma sırasını ve kurtarmanızın test edemediğiniz tedarikçilere ne kadar bağlı olduğunu gerçekten biliyor musunuz?** Sistemler birbirinden bağımsız değil, ağlar halinde çöker ve kurtarma, kimsenin haritalamadığı bağımlılıkta tıkanır: bir uygulamayı veritabanından, kimlik sağlayıcısından ya da DNS'ten önce ayağa kaldırırsanız yalnızca ikinci bir kesinti üretirsiniz. Bağımlılıkları haritalamak sıkıcıdır ve harita eskir, ama alternatif kurtarma sırasını bir yük devri sırasında canlı keşfetmektir; ve bir avuç SaaS sağlayıcısındaki yoğunlaşma riski, hepsi birlikte çökene ve kurtarmanızı onlarınkiyle sınırlayana kadar görünmez kalır. Güncel bir bağımlılık haritası, belgelenmiş kurtarma sırası ve dış tedarikçilerin beyan ettiği kurtarma taahhütleriyle bunlardan herhangi birini hiç doğrulayıp doğrulamadığınızı gösteren bir liste getirin. Büyük ya da kamusal bir kurum için tedarikçi sürekliliği ve yoğunlaşma riski giderek bir tedarik ve düzenleme meselesidir; bu yüzden bu kurtarma yükümlülükleri bir satıcının pazarlama metninde değil, sözleşmede denetleyebileceğiniz bir biçimde yer almalıdır.

6. **Bu gece her sunucuyu geri yükleseydiniz iş gerçekten çalışmaya devam eder miydi ve felaketi ilan etmeye kim yetkili?** Felaket kurtarma BT'yi geri getirir, ama iş sürekliliği kurumu işler tutar: insanlar, iletişim, maaşlar ve bir kişinin onları verme yetkisine bağlı kararlar. Her sistemi kurtarabilir ve yine de müşterilerinizi yarı yolda bırakabilirsiniz; çünkü kimse felaketi kimin ilan edebileceğini ya da normal kanallar da çökmüşken personele nasıl ulaşılacağını bilmiyordur. Kurtarma mühendisliğe aittir, ama süreklilik tesisleri, İK'yı, iletişimi ve liderlik halefiyetini kapsar ve bölümler arasındaki bu dikişler bir planın sessizce çürüdüğü yerlerdir. İlan yetkisini ve yükseltme zincirini, yedek iletişim planını, adı konmuş halefleri ve alternatif tesisleri ve iş tarafının (yalnızca BT'nin değil) planı en son ne zaman uyguladığının tarihini getirin. Kamu, adı konmuş halefler ve temel işlevlerle yasal bir işlerin sürekliliği görevi taşır ve kurumlar düzenleyici süreklilik yükümlülükleriyle karşılaşır; bu yüzden ikisi de yalnızca sunucuların değil, işin kötü günden sağ çıkıp çıkmadığına göre yargılanır.

## Sektör merceği

**Girişim.** Minik bir takım ve az pistle sıcak bir ikinci bölgeyi karşılayamazsınız; bu yüzden sizi yine de kurtaran ucuz kısımlar konusunda bilinçli olun. Tek bir dürüst kurtarma katmanı belirleyin, otomatik anlık görüntülerle 3-2-1 kuralını izleyin ve kendi yöneticilerinizin silemeyeceği en az bir değiştirilemez kopya tutun; tüm ortamı kaynaktan yeniden kurabilmek için kod olarak altyapı biçiminde tutun. Ayrıntılı planı atlayın; bunun yerine her çeyrek bir geçici ortama gerçek bir geri yükleme yapın, çünkü zamanlanmış tek bir tatbikat size kimsenin okumadığı bir klasörden daha çok şey öğretir.

**Küçük işletme.** Özel bir süreklilik uzmanı ve sıkı bir bütçeyle kurtarmayı inşa ettiğiniz bir şey olarak değil, satın aldığınız bir şey olarak ele alın. Özel DR altyapısı kurmak yerine bulut sağlayıcınızın yönetilen yedekleme, anlık görüntü ve bölgeler arası çoğaltmasına yaslanın ve yedekleri değiştirilemez olan ve geri yükleme sürecini kendiniz çalıştırabileceğiniz satıcıları seçin. Tüm çalışmayı, uzman olmadan cevaplayabileceğiniz iki soru etrafında çerçeveleyin: ne kadar veri kaybedebiliriz ve ne kadar süre kapalı kalabiliriz; ve güvenmeden önce bir geri yüklemenin çalıştığını kanıtlayın.

**Kurumsal.** Ölçekte sorun, birçok takım arasında portföy yönetişimidir: her hizmete bir RTO ve RPO atayan bir iş etkisi analizi, yedekle ve geri yükle'den aktif-aktife kadar katmanlanmış kurtarma stratejileri ve yoğunlaşma riski dahil üst akış ve tedarikçi bağımlılıklarının merkezi bir görünümü. Bekleme, çoğaltma ve değiştirilemez kopya maliyetlerini açıkça bütçeleyin, düzenleyici tanıklığında tam yük devirlerini bir ritimle çalıştırın ve gerçek kurtarmayı hedefe karşı izlenen bir güvenilirlik metriği olarak ölçün. Siber kurtarmayı, değiştirilemez kasa kopyaları ve bir temiz oda çalışma kitabıyla kendi programı olarak yürütün ve doğal felaket tatbikatlarından bağımsız test edin.

**Kamu.** Tedarik kuralları, şeffaflık ve kamusal hesap verebilirlik her seçimi şekillendirir ve süreklilik çoğu zaman bir tercih değil yasal bir görevdir. Temel işlevleri belirleyen, kurtarmalarını sıralayan ve kararların yetkili bir kişinin yokluğundan takılmaması için halefleri ve alternatif tesisleri adlandıran bir işlerin sürekliliği programı kurun; bunu FISMA yükümlülüklerini destekleyen NIST SP 800-34 gibi tanınmış rehberliğe hizalayın. Hava boşluklu yedek kopyalar tutun, alternatif bir bölgede yeniden kurmak için kod olarak altyapı tanımlayın ve temel hizmetlerin ayakta kaldığının kanıtı olarak ölçülen sonuçlarını gözetim kurullarına raporladığınız yıllık tam bir tatbikat ile fidye yazılımı masa başı tatbikatları yürütün.

## Örnekler

**Girişim.** On iki kişilik bir SaaS şirketi sıcak bir ikinci bölgeyi karşılayamaz; bu yüzden ucuz kısımlar konusunda bilinçlidir. Tek bir dürüst katman belirler: müşteri veritabanı için dört saatlik RTO, on beş dakikalık RPO. 3-2-1 kuralını otomatik anlık görüntülerle izler; bir kopya ikinci bir bulut bölgesine çoğaltılır ve bir kopya, kendi yöneticilerinin silemeyeceği kilitli bir saklama penceresine sahip değiştirilemez kopyadır. Tüm ortamı kod olarak altyapıdır (bölüm 8.2); bu yüzden kaynaktan yeni bir yığın ayağa kaldırabilir. Her çeyrek bir Cuma öğleden sonrası geçici bir ortama gerçek bir geri yükleme yapar, zamanlar ve kısa bir not düşer. İlk tatbikat dokuz saat sürdü ve eksik bir geçiş adımı buldu; düzeltme, bir sonrakinin neden üç saat sürdüğünün nedenidir.

**Kurumsal.** Çok uluslu bir banka, kritik hizmetler için test edilmiş süreklilik şart koşan düzenleyici kurtarma gereksinimleri altında çalışır. Çekirdek bankacılık platformu için ikinci bir bölgede sıcak bekleme çalıştırır; sıfıra yakın RPO için bir metro çifti içinde eşzamanlı çoğaltma, bölgesel felaketten sağ çıkmak için uzak bir bölgeye eşzamansız çoğaltma kullanır. Bir iş etkisi analizi her hizmete bir RTO ve RPO atar ve merkezi bir takım, yoğunlaşma riski olarak işaretlenmiş iki SaaS sağlayıcısı dahil üst akış bağımlılıklarını haritalar. Yılda iki kez düzenleyici tanıklığında tam yük devri yapar, gerçeği hedefle karşılaştırarak ölçer ve boşlukları sonraki döngüye aktarır. Ayrı bir siber kurtarma programı, değiştirilemez kasa kopyalarını ve bir temiz oda çalışma kitabını tutar ve bunları doğal felaket tatbikatlarından bağımsız test eder.

**Kamu.** Sosyal yardım sağlayan ulusal bir kurum, temel işlevlerini her aksama boyunca sürdürmek üzere kurulmuş bir işlerin sürekliliği (COOP) programı yürütür. [İşlerin sürekliliği](https://en.wikipedia.org/wiki/Continuity_of_Operations) pratiğini ve FISMA yükümlülüklerini destekleyen NIST SP 800-34 acil durum planlama rehberliğini izleyerek temel işlevleri belirler, kurtarmalarını sıralar ve kararların yetkili bir kişinin yokluğundan takılmaması için halefleri ve alternatif tesisleri adlandırır. Vatandaşa dönük sistemlerin belgelenmiş RTO ve RPO'su vardır, yedekler hava boşluklu kopyalarla 3-2-1 kuralını izler ve altyapı alternatif bir bölgede yeniden kurulmak üzere kod olarak tanımlanır. Yıllık tam bir tatbikat ve bir fidye yazılımı senaryosu için masa başı tatbikatları planı ölçülen kurtarmaya karşı test eder ve sonuçlar, temel hizmetlerin kötü günden sağ çıktığının kanıtı olarak gözetim kurullarına raporlanır.

## İş gerekçesi: motivasyonlar, YG ve TSM

DR ve sürekliliğin getirisi, önlenen felakettir; bu, ihtiyaç duyana kadar değerlemesi gerçekten zordur ve ihtiyaç duyduğunuzda acı verecek kadar somuttur. Bunu risk yönetimi olarak çerçeveleyin: bir aksamanın beklenen maliyeti olasılığı çarpı etkisidir ve büyük bir kurum için etki, kesinti saati başına kaybedilen gelirden düzenleyici cezalara, ihlal bildirim maliyetlerine ve kesintiden uzun yaşayan itibar zararına uzanır. Kurtarılamayan tek bir fidye yazılımı olayı şirketleri bitirmiş ve kamu sektöründe temel vatandaş hizmetlerini haftalarca çevrimdışı bırakmıştır. Buna karşı, test edilmiş bir kurtarma yeteneğinin maliyeti mütevazı ve bilinebilirdir.

Toplam sahip olma maliyeti (TSM) gerçek ve süreklidir: bekleme altyapısı, çoğaltma bant genişliği, yedek depolama (değiştirilemez ve çevrimdışı kopyalarla çarpılmış) ve otomasyon kurmak ve tatbikatlar yürütmek için mühendislik zamanı. Aktif-aktifi her yerde satın almak yerine RTO ve RPO'ya göre katmanlamanızın nedeni tam olarak budur; böylece harcama toptan bir ilkeyi değil, her sistemin değerini izler. Liderliğe gerekçeyi sunmak için planı onların diline çevirin: bugün hayatta kalabileceğimiz kesinti süresi ve veri kaybı budur, hedeflerimize olan fark budur, onu kapatmanın maliyeti budur ve kapatmazsak maruziyet budur. En ikna edici ürün ölçülmüş bir tatbikattır; çünkü gösterdiğiniz bir kurtarma liderliğin güvenebileceği bir rakamdır ve denenmemiş bir plan, varlık kılığına girmiş bir yükümlülüktür.

## Anti-kalıplar ve tuzaklar

- **Denenmemiş yedekler.** Hiç yapmadığınız bir geri yükleme bir umuttur; bozulmayı, eksik anahtarı ve yanlış birimi bulduğunuz yer tatbikattır.
- **Üretimden ulaşılabilir yedekler.** Fidye yazılımı yedeklerinizi şifreleyebiliyor ya da silebiliyorsa üç değil, tek kopyanız var demektir. Birini değiştirilemez ve çevrimdışı tutun.
- **Her şey için tek RTO ve RPO.** Toptan katmanlar önemsizi gereğinden fazla, kritik olanı yetersiz korur; katmanlamayı bir iş etkisi analizinden yapın.
- **DR ile BCP'yi karıştırmak.** Kimsenin felaketi kimin ilan ettiğini ya da personele nasıl ulaşılacağını bilmediği bir durumda her sunucuyu geri yüklemek, kurtarılmış bir sistem ve başarısız bir iştir.
- **Elle kurulmuş kurtarma ortamları.** Koddan yeniden kuramadığınız altyapı kayar ve kayma yük devri sırasında keşfedilir.
- **Göz ardı edilen bağımlılıklar.** Bir uygulamayı veritabanından, kimlik sağlayıcısından ya da DNS'ten önce kurtarmak yalnızca ikinci bir kesinti üretir.
- **Plan çürümesi.** Bir kez yazılıp hiç uygulanmayan bir klasör, artık var olmayan bir sistemi anlatır.
- **Tedarikçi kör noktaları.** Kurtarmanız, kritik tedarikçilerinizin kurtarmasıyla sınırlıdır ve yoğunlaşma riski, hepsi birlikte çökene kadar görünmezdir.

## Olgunluk modeli

- **Düzey 1, Başlangıç:** Kurtarma geçici ve tepkiseldir. Yedekler çalışıyor olabilir ama geri yüklemeler denenmemiştir. Üzerinde anlaşılmış RTO ya da RPO yoktur, iş etkisi analizi yoktur ve kurtarma olay sırasında doğaçlama yapılır. Ciddi bir veri kaybı ya da fidye yazılımı olayı büyük olasılıkla kurtarılamaz olur.
- **Düzey 2, Geliştirme:** Temel pratikler vardır ama takımlar arasında tutarsızdır. Bazı kritik sistemlerin 3-2-1 kuralını izleyen yedekleri ve en önemli hizmetler için belgelenmiş RTO ve RPO'su vardır; temel bir DR planı mevcuttur ve geri yüklemeler ara sıra test edilir. Kapsam kısmidir, bağımlılıklar haritalanmamıştır, tatbikatlar geçicidir ve bir takımın disiplini bir sonrakinin disiplinini ima etmez.
- **Düzey 3, Standartlaştırma:** Kurtarma pratiği belgelenmiş ve kurum genelinde zorunlu kılınmıştır. Bir iş etkisi analizi sistemler arasında katmanlı RTO ve RPO'yu yönlendirir, kurtarma stratejileri bu katmanlarla eşleştirilir, ortamlar kod olarak altyapıdır, bağımlılıklar ve kurtarma sırası haritalanmıştır ve planlanmış tatbikatlar (masa başı, oyun günü ve yük devri) tanımlı bir ritimle çalışır. Değiştirilemez, çevrimdışı kopyalarla bir siber kurtarma planı belgelenmiş ve bireysel takımlara bırakılmak yerine tutarlı biçimde uygulanmıştır.
- **Düzey 4, Yönetme:** Kurtarma taban çizgilerine karşı ölçülür ve kontrol edilir. Her tatbikat elde edilen gerçek RTO ve RPO'yu kaydeder ve hedefe olan farkı izler; geri yükleme başarı oranı, kritik sistemlerin geçen yıl içinde uçtan uca kurtarılan kesri, yedek kapsamı ve değiştirilemezliği ile gerçek RPO olarak izlenen çoğaltma gecikmesi gibi metrikler panolarda raporlanır. Sapmalar eylemi tetikler, katmanlama sistemlerin gerçekte nasıl kullanıldığına dair verilerden yeniden türetilir ve uygula ya da uygulama kararları bir slayda yazılmış rakamlara değil kanıta dayanır.
- **Düzey 5, Orkestrasyon:** Kurtarma sürekli iyileştirilir, kurum genelinde bütünleşiktir ve uyarlanabilirdir. Yük devri ve siber kurtarma temiz oda geri yüklemeleri rutin olarak prova edilir, tedarikçi ve yoğunlaşma riski etkin biçimde yönetilir ve süreklilik; güvenilirlik (bölüm 9.1) ve olay müdahalesiyle (bölüm 9.3) bütünleştirilir; böylece kurum hiç görmediği başarısızlıklardan öngörülebilir biçimde toparlanır ve sistem manzarası ile tehdit tablosu kaydıkça kurtarma duruşunu yeniden kapsamlar.

## Tartışma fikirleri

1. Kritik sistemlerinizden hangisi hiç uçtan uca geri yüklenmedi ve bunun yapılabildiğini kanıtlamak için neler gerekir?
2. Birincil bulut bölgenizi tam bir gün kaybetseydiniz hangi iş süreçleri durur ve sistemleri hangi sırayla geri getirirdiniz?
3. Kurtarmanızın ne kadarı, kendi kurtarmalarını göremediğiniz ya da test edemediğiniz tedarikçilere bağlı?
4. İş etkisi analizinin haklı çıkarmadığı bir kurtarma katmanına nerede para ödüyorsunuz ve nerede yetersiz koruyorsunuz?
5. Yedekleriniz bu gece ulaşılabilir ve şifreli olsaydı gerçek bilinen son temiz geri yükleme noktanız nedir?
6. Vaat ettiğiniz RTO ve RPO ile son tatbikatınızın gerçekten elde ettikleri arasındaki dürüst fark nedir?

## Önemli çıkarımlar

- **Süreklilik hedeftir; kurtarma bir araçtır.** İş sürekliliği planlaması kurumu işler tutar; felaket kurtarma, onun dayandığı BT sistemlerini geri getirir.
- **RTO ve RPO her şeyi belirler** ve ikisi de mühendislik tahmininden değil, bir iş etkisi analizinden gelir. Sistemleri hepsini eşit korumak yerine katmanlara ayırın.
- **Denenmemiş yedek yedek değildir.** 3-2-1 kuralını izleyin, fidye yazılımına karşı en az bir değiştirilemez ve çevrimdışı kopya tutun ve geri yüklemeleri bir takvime göre test edin.
- **DR stratejisini rakamla eşleyin:** yedekle ve geri yükle, pilot ışığı, sıcak bekleme ya da aktif-aktif; her sistemin RTO ve RPO'suna göre seçilir.
- **Çoğaltma, tutarlılığı tazelikle takas eder** (bölüm 3.3); gerçek RPO'nuz tasarım belgeniz değil, çoğaltma gecikmenizdir.
- **Kod olarak altyapıyla koddan yeniden kurun** (bölüm 8.2) ve ihtiyaç duymadan önce bağımlılıklarınızı haritalayın.
- **Masa başı tatbikatları, oyun günleri ve tam yük devri tatbikatlarıyla test edin** ve gerçek RTO ile RPO'yu hedefe karşı ölçün.
- **Siber kurtarmayı temiz oda geri yüklemesiyle ayrıca planlayın** ve tüm pratiği güvenilirliğe (bölüm 9.1), olay müdahalesine (bölüm 9.3) ve uyuma (bölüm 4.6) bağlayın.

## Kaynaklar ve ileri okuma

- ISO 22301, *Security and resilience: Business continuity management systems: Requirements* (the international standard for BCP).
- National Institute of Standards and Technology, *SP 800-34 Rev. 1: Contingency Planning Guide for Federal Information Systems* (RTO, RPO, and recovery strategies for government systems).
- National Institute of Standards and Technology, *SP 800-61 Rev. 2: Computer Security Incident Handling Guide* (incident and cyber-recovery handling).
- U.S. Federal Emergency Management Agency, *Continuity Guidance Circular* and federal COOP guidance (essential functions and continuity of operations).
- Federal Financial Institutions Examination Council (FFIEC), *Business Continuity Management* booklet (regulatory recovery expectations for financial institutions).
- Betsy Beyer, Chris Jones, Jennifer Petoff, Niall Richard Murphy, eds., *Site Reliability Engineering: How Google Runs Production Systems* (reliability and disaster testing).
- Kelly Shortridge and Aaron Rinehart, *Security Chaos Engineering* (deliberately exercising failure and recovery).
- Cybersecurity and Infrastructure Security Agency (CISA), *#StopRansomware Guide* (ransomware prevention and recovery practice).
