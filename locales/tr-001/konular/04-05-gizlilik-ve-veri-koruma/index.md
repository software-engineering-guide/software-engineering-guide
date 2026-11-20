# 4.5 Gizlilik ve veri koruma

## Genel bakış ve motivasyon

Güvenlik, veriyi yetkisiz erişimden korur. Gizlilik ise farklı bir soru sorar: o veriyi toplamalı, kullanmalı ve saklamalı mısınız, ve verinin anlattığı insanların bu konuda söz hakkı var mı? İkisi örtüşür ama aynı şey değildir. Mükemmel biçimde güvenli olup yine de gizliliği ihlal edebilirsiniz. Bunu, elinizde tutmaya hakkınız olmayan veriyi biriktirerek, insanların asla onaylamadığı amaçlar için kullanarak ya da yasanın yasakladığı biçimlerde sınırlar ötesine taşıyarak yaparsınız. Büyük takımlar için gizlilik bir tasarım kısıtıdır. Kişisel bilgiyi işleyen her hizmeti etkiler; bugün bu, neredeyse hepsi demektir.

Bahisler yüksek ve artıyor. Gizlilik düzenlemesi dünya çapında yayıldı. Cezaları gelirle birlikte büyür ve bireylere verileri üzerinde uygulanabilir haklar tanır. Kurumsal tarafta kişisel verinin kötü işlenmesi düzenleyici işlemi, toplu davaları ve yeniden kazanması pahalı müşteri güveni kaybını davet eder. Kamu için görev daha da ağırdır. Vatandaşlar vergi, sağlık ya da yardım verileri için başka bir sağlayıcı seçemez; bu yüzden devlet onlara özel bir özen borcu taşır. Üstelik gizlilik başarısızlıkları, kamunun dayandığı kamusal güveni aşındırır.

Bu bölüm gizliliği bir mühendislik disiplini olarak ele alır. Baştan gizliliğe göre tasarlamayı, veriyi sorumlu biçimde en aza indirmeyi ve saklamayı, [PII](https://en.wikipedia.org/wiki/Personally_identifiable_information) ve [PHI](https://en.wikipedia.org/wiki/Protected_health_information) gibi hassas kategorileri sınıflandırıp korumayı, rıza ve hukuki dayanağı yönetmeyi ve mimariyi giderek daha fazla şekillendiren sınır ötesi aktarım ve veri yerleşimi gereksinimlerini yönetmeyi kapsarız.

*Ayrıca bakın:* bölüm 4.6 (uyum ve yönetişim), bölüm 7.1 (veri stratejisi ve yönetişimi) ve bölüm 4.1 (güvenlik temelleri ve kültürü).

## Temel ilkeler

- **[Tasarımla ve varsayılan olarak gizlilik](https://en.wikipedia.org/wiki/Privacy_by_design).** Gizliliği en başından içeri işleyin ve gizliliği en çok koruyan ayarı varsayılan yapın.
- **[Veri minimizasyonu](https://en.wikipedia.org/wiki/Data_minimization).** Yalnızca gerçekten ihtiyaç duyduğunuzu toplayın, yalnızca ihtiyaç duyduğunuz süre saklayın ve yalnızca gerektiği kadar paylaşın.
- **Amaçla sınırlılık.** Veriyi yalnızca toplandığı sırada açıklanan belirli amaçlar için kullanın.
- **Hukuki dayanak.** Her işleme faaliyeti için geçerli bir hukuki gerekçeniz olsun.
- **Bireysel haklar.** İnsanların verilerine erişme, düzeltme, silme ve taşıma haklarına saygı gösterin.
- **Şeffaflık.** İnsanlara neyi, neden topladığınızı ve kimlerle paylaştığınızı açıkça söyleyin.
- **Hesap verebilirlik.** Uyumu yalnızca iddia etmekle kalmayıp gösterebilir olun.

## Öneriler

### Baştan gizlilik için tasarlayın

Bitmiş bir sisteme sonradan eklenen gizlilik pahalıdır ve eksik kalır. Baştan içine işleyin.

- Kişisel veriyi ölçekte işleyen ya da daha yüksek risk taşıyan yeni sistemler ve özellikler için **[Veri Koruma Etki Değerlendirmeleri](https://en.wikipedia.org/wiki/Data_protection_impact_assessment) (DPIA)** yapın; gizlilik risklerini inşa etmeden önce belirleyin ve azaltın.
- Varsayılanları gizliliği koruyan yapın: temel olmayan işleme için opt-out yerine opt-in, asgari veri alanları ve makul olan en kısa saklama.
- Gizlilik uzmanlığını tasarıma erken, güvenlik tehdit modellemesiyle birlikte dahil edin; böylece ikisi de güven sınırı aşamasında göz önüne alınır.
- Bir **veri haritası ya da envanteri** tutun: hangi kişisel veriyi tuttuğunuz, nerede yaşadığı, neden ve nereye aktığı. Göremediğiniz veriyi koruyamaz ya da hesabını veremezsiniz.

### Sorumlu biçimde en aza indirin, saklayın ve silin

Elinizde tuttuğunuz her kişisel veri parçası bir varlık olduğu kadar bir yüktür.

- **Toplamayı en aza indirin:** her alanı sorgulayın. Belirtilmiş bir amaç için gerekmiyorsa toplamayın.
- Veri türüne ve amaca göre **saklama takvimleri belirleyin** ve bunları otomatik silmeyle uygulayın. "Her ihtimale karşı" saklanan veri, ihlal edilmeyi ya da celp edilmeyi bekleyen verilerdir.
- **Silinme hakkını destekleyin:** bir bireyin verisini yedekler ve aşağı akış kopyaları dahil tüm sistemlerde, yasal süreler içinde bulup silme yeteneğini kurun. Bu, sonradan eklemektense tasarıma baştan koyulduğunda çok daha kolaydır.
- Analitik ve test için veriyi **[anonimleştirin](https://en.wikipedia.org/wiki/Data_anonymization) ya da toplulaştırın**; böylece kimliği belirlenebilir veri ikincil ortamlara yayılmaz.

### Hassas veriyi sınıflandırın ve koruyun

Her kişisel veri aynı riski taşımaz ve bazı kategoriler özel bir hukuki ağırlık taşır.

- Veriyi kademelere ayırarak sınıflandırın: **PII** (kişisel olarak tanımlanabilir bilgi), **PHI** (korunan sağlık bilgisi), finansal veri ve gelişmiş hukuki koruma taşıyan özel kategoriler (ırk, din, sağlık, biyometri ya da cinsel yönelim gibi) arasında ayrım yapın.
- Korumayı hassasiyetle orantılı uygulayın: en hassas kademeler için daha güçlü erişim kontrolleri, şifreleme ve izleme.
- Hassas değerleri (kart numaraları ya da ulusal kimlik numaraları gibi) hassas olmayan belirteçlerle değiştirmek için **[belirteçleme](https://en.wikipedia.org/wiki/Tokenization_(data_security))** kullanın; böylece ham veriye dokunan sistemleri ve dolayısıyla uyum kapsamını daraltırsınız.
- Bir kaydın kimlik belirleyicilerini geri kalanından ayırmak için **[takma adlandırma](https://en.wikipedia.org/wiki/Pseudonymization)** kullanın; veri daha az doğrudan atfedilebilir olur, yarar korunurken risk azalır.
- Hassas veriyi günlüklerde, hata iletilerinde, analitikte ve üretim dışı ortamlarda maskeleyin.

### Rızayı ve hukuki dayanağı doğru yönetin

Kişisel veriyi işlemek geçerli bir hukuki temel gerektirir ve rıza bunlardan yalnızca biridir.

- Her işleme faaliyeti için **hukuki dayanağı** belirleyin ve belgeleyin: uygulanan rejime bağlı olarak rıza, sözleşme, hukuki yükümlülük, hayati çıkarlar, kamu görevi ya da meşru menfaatler.
- Dayanak rıza olduğunda onu **özgürce verilmiş, belirli, bilgilendirilmiş ve açık** yapın; geri çekmenin de eşit derecede kolay bir yolu olsun. Önceden işaretlenmiş kutular ve paketlenmiş rıza geçerli değildir.
- Rızayı kaydedin: kişinin neyi, ne zaman ve hangi koşullarla onayladığı; böylece bunu gösterebilirsiniz.
- **Amaçla sınırlılığa** saygı gösterin: veriyi, yeni bir dayanak olmadan, toplanma nedeniyle bağdaşmayan bir şey için yeniden kullanmayın.
- Yasaların gerektirdiği yerde [Do Not Track](https://en.wikipedia.org/wiki/Do_Not_Track) / [Global Privacy Control](https://en.wikipedia.org/wiki/Global_Privacy_Control) gibi sinyallere ve opt-out taleplerine uyun.

### Sınır ötesi aktarımı ve veri yerleşimini yönetin

Verinin fiziksel olarak nerede yaşadığı ve nereye taşındığı artık birinci derece bir mimari kaygıdır.

- **Veri yerleşimi** gereksinimlerini anlayın: bazı yargı bölgeleri belirli verinin ulusal sınırlar içinde kalmasını ister ve bazı kamu verileri belirli egemen ya da akredite ortamlarda kalmalıdır.
- **Sınır ötesi aktarımlar** için geçerli bir hukuki mekanizmanın (yeterlilik kararları, standart sözleşme maddeleri ya da eşdeğeri) mevcut ve belgelenmiş olduğundan emin olun.
- Baştan yerleşim için mimari kurun: bölgeye sabitlenmiş depolama, veri yerelleştirme ve yedeklerin, günlüklerin ve analitik verisinin nereye aktığının dikkatli kontrolü; çünkü bunlar çoğu zaman veriyi fark edilmeden sınırlar ötesine sızdırır.
- Alt işleyicileri ve üçüncü tarafları izleyin; veriyi yurt dışına taşıyan bir tedarikçi, sizin adınıza yerleşim yükümlülüklerini ihlal edebilir.

## Ödünleşimler: artılar ve eksiler

| Karar | Artılar | Eksiler |
|---|---|---|
| Agresif veri minimizasyonu | Daha az risk, daha küçük ihlal etkisi, daha basit uyum | Analitiği ve gelecekteki ürün seçeneklerini sınırlayabilir |
| Uzun saklama | Analitik, ML ve uyuşmazlıklar için zengin geçmiş | Daha büyük yük, ihlal maruziyeti, silme karmaşıklığı |
| Belirteçleme | Uyum kapsamını daraltır, ham veriyi korur | Sistem karmaşıklığı artar, güvenceye alınacak bir belirteç kasası |
| Opt-in varsayılanlar | Daha güçlü güven, net uyum | Daha düşük veri hacimleri, daha zor büyüme metrikleri |
| Bölgesel veri yerleşimi | Yasal zorunlulukları karşılar, egemenlik güveni kurar | Mimari karmaşıklık, daha yüksek maliyet, çoğaltılmış altyapı |
| Merkezi veri gölü | Analitik gücü, tek kaynak | Yoğunlaşmış risk, amaçla sınırlılığı sağlamak daha zor |

Temel gerilim, işin veri iştahı ile verinin temsil ettiği yük arasındadır. Ürün ve analitik takımları doğal olarak daha fazla toplamak ve daha uzun saklamak ister. Gizlilik disiplini ters yöne çeker. Olgun çözüm, veriyi biriktirilecek bir varlık değil, gerekçelendirilmesi gereken bir yük olarak yeniden çerçeveler. Her toplama ve saklama kararı, yarattığı riske karşı yerini hak etmelidir. Veri yerleşimi bir maliyet-uyum boyutu ekler. Egemenlik gereksinimlerini karşılamak altyapıyı katlayabilir, ama bazı pazarlarda ve kamu bağlamlarında pazarlık konusu bile değildir.

## Takımınızla tartışılacak sorular

1. **Her kişisel veri sınıfı için saklama takviminiz nedir ve silmeyi ne uygulatır?** "Her ihtimale karşı" saklanan veri, ihlal edilmeyi ya da celp edilmeyi bekleyen verilerdir; bu yüzden her alanın ve her kaydın amacına bağlı tanımlı bir ömrü olmalıdır. Takvimi veri türüne göre belirleyin, sonra kimsenin hatırlamasına güvenmek yerine otomatik silmeyle uygulayın. Kurumsal tarafta bu, ihlal maruziyetini ve depolama maliyetini aynı anda küçültür; kamuda ise vatandaş verisini yasanın izin verdiğinden uzun tutmama yönündeki yasal yükümlülüklerle örtüşür. En eski saklanan kayıtlarınızdan bir örnek getirin ve hâlâ kimin, hangi dayanakla bunlara ihtiyaç duyduğunu sorun; çünkü dürüst cevap çoğu zaman hiç kimse. Silme elle yapılıyorsa ya da hiç yoksa veri sonsuza kadar birikir ve yükünüz bilançoda sessizce büyür.

2. **Hangi hassas alanları belirteçleyebilir ya da takma adlandırabilirsiniz ki hem riski hem uyum kapsamını küçültesiniz?** Kart numaralarını ya da ulusal kimlik numaralarını belirteçlerle değiştirmek, ham değerleri küçük ve sıkı kontrol edilen bir kasaya hapseder; bu da PCI-DSS gibi denetimlerde kapsamdaki sistemleri keskin biçimde azaltır. Takma adlandırma, bir kaydın kimlik belirleyicilerini geri kalanından ayırır; veri analitik ve test için yararlı kalırken risk düşer. Hangi yüksek hassasiyetli değerlerin bir belirteç kasasını (ek karmaşıklık, güvenceye alınacak bir kasa) hak ettiğine ve hangilerinin yalnızca günlüklerde ve üretim dışında maskelenmesi gerektiğine karar verin. Ham hassas değerlerin bugün nereden aktığını gösteren bir harita getirin, çünkü onlara dokunan her sistem korumanız ve denetlemeniz gereken bir sistemdir. Düzenlemeye tabi ve kamu verisi için bu kapsam daraltma, maliyeti ve riski birlikte düşüren az sayıdaki hamleden biridir; bu yüzden önce en hassas alanlarınızı hedefleyin.

3. **Bir sonraki özellik canlıya çıkmadan önce neyin Veri Koruma Etki Değerlendirmesini tetikler ve onu kim yürütür?** Bitmiş bir sisteme sonradan eklenen gizlilik pahalıdır ve eksik kalır; bu yüzden DPIA erken, güvenlik tehdit modellemesiyle birlikte, tasarımı hâlâ ucuza değiştirebildiğiniz zamanda yapılmalıdır. Tetikleyiciyi (ölçekte yeni işleme, özel kategoride veri, yeni bir amaç) belirleyin ve değerlendirmenin teslimat baskısı altında gözden kaçmaması için sahibini adlandırın. Gerçek bir DPIA, canlıya çıkmadan önce aşırı toplamayı yakalayabilir; örneğin ürün kaybı olmadan kesin konumdan kaba bölge verisine geçmek. Yaklaşan bir özelliği getirin ve üzerinden geçin: hangi kişisel veriyi topluyor, neden ve daha az müdahaleci bir tasarım aynı hedefe ulaşır mı. Vatandaşların vazgeçemediği kamu hizmetlerinde bu erken kontrol özen borcunun parçasıdır; bu yüzden onu sonradan akla gelen bir şey değil, bir kapı yapın.

4. **Kişisel veri, yedekler, günlükler ve alt işleyiciler dahil bir sınırı geçtiğinde, her geçişi hangi hukuki mekanizma kapsıyor ve bunu kanıtlayabilir misiniz?** Yerleşim ve aktarım kuralları artık mimariyi herhangi bir performans gereksinimi kadar şekillendiriyor ve takımları yakalayan geçişler nadiren bariz olanlardır: yurt dışındaki bir gözlemlenebilirlik aracına gönderilen bir günlük, daha ucuz bir bölgeye çoğaltılan bir yedek ya da veriyi sessizce yurt dışına taşıyan bir alt işleyici. Büyük bir kurum için rekabet eden baskılar gerçektir, çünkü bölgeye sabitlenmiş altyapı daha pahalıdır ve operasyonları katlar; yine de tek bir hukuka aykırı aktarım bir pazara girişi geçersiz kılabilir ya da bir icra emrini tetikleyebilir. Kişisel verinin fiziksel olarak durduğu ya da seyahat ettiği her yeri adlandıran güncel bir veri akış haritası, geçtiği her sınır için hukuki mekanizmayı (yeterlilik kararı, standart sözleşme maddeleri ya da eşdeğeri) ve alt işleyicilerin konumlarıyla birlikte listesini getirin. Kamu ve egemen veri bağlamlarında yerleşimi bir sözleşme maddesi değil, katı bir mimari kısıt olarak ele alın; çünkü bazı kayıtlar akredite ulusal ortamların dışına asla çıkmamalıdır ve hesap verebilir kurum bu görevi bir tedarikçiye devredemez.

5. **Her işleme faaliyetini hangi hukuki dayanak destekliyor ve bu seçimi yarın bir düzenleyiciye savunabilir misiniz?** Rıza birkaç hukuki temelden yalnızca biridir ve takımlar çoğu zaman sözleşme, hukuki yükümlülük, kamu görevi ya da meşru menfaatler hem daha dürüst hem daha dayanıklı olacakken varsayılan olarak ona yönelir. Bu ölçekte önemlidir, çünkü zayıf ya da yanlış seçilmiş bir dayanak tüm bir hattı geçersiz kılabilir ve yapmaya hakkınız olmayan işlemeyi çözmek, baştan doğru dayanağı seçmekten çok daha pahalıdır. Rekabet eden hususları açıkça tartın: rıza bireylere kontrol verir ama geri çekilebilir ve özgürce verilmiş, belirli ve paketlenmemiş olmalıdır; meşru menfaatler gibi bir dayanak ise rıza yorgunluğunu önler ama belgelenmiş bir denge testi talep eder. Her işleme faaliyetini iddia edilen dayanağına, onu destekleyen kanıta ve itiraz edilirse nasıl geri çekeceğinize ya da değiştireceğinize eşleyen bir kayıt getirin. Kamuda temel işlemenin çoğu rızaya değil kamu görevine dayanır; bu yüzden isteğe bağlı, geri çekilebilir rızanın nerede başladığı konusunda kesin olun, çünkü ikisini bulanıklaştırmak, vatandaşların uzatmaktan başka seçeneği olmayan güveni aşındırır.

6. **Bir kişi bugün erişim, silme ya da taşınabilirlik hakkını kullansa, bunu yasal süre içinde her sistemde karşılayabilir miydiniz?** Bireysel hakları bir gizlilik politikasında vaat etmek kolaydır, ama kişisel verinin kopyalarını yedeklere, önbelleklere, analitik depolarına ve aşağı akış hizmetlerine dağıtmış bir mimaride yerine getirmek zordur. Büyük bir takım için bu, soyut uyumun somut bir mühendislik sınamasına dönüştüğü andır; kaçırılan bir yasal süre hem bildirilebilir bir başarısızlık hem de kendi verinizi gerçekten göremediğinizin işaretidir. Rekabet eden husus maliyet ve karmaşıklıktır, çünkü gerçek sistemler arası silme ve dışa aktarma kurmak gerçek iştir; ama alternatif elle yürütülen, yavaş, hataya açık, ölçeklenmeyen ve sessizce yasayı çiğneyen bir yerine getirmedir. Yedeklere ve üçüncü taraflara nasıl ulaşıldığı dahil, girişten tamamlanmaya kadar gerçek bir talebin dürüst bir izini getirin ve yasal süreye karşı zamanlayın. İnsanların ayrılamadığı kamu hizmetlerinde, self servis, eksiksiz ve denetlenebilir hak yerine getirmeyi sonraya ertelenecek bir özellik değil, özen borcunun parçası sayın.

## Sektör merceği

**Girişim.** Küçük bir takım ve az bir pistle, gizliliği kadrolayamayacağınız bir program değil, ucuz bir sigorta olarak ele alın. Yalnızca çekirdek özelliğinizin ihtiyaç duyduğu alanları toplayın, bir silme talebine gerçekten cevap verebilmek için hafif bir elektronik tablo veri haritası tutun ve e-postaları ve belirteçleri günlüklerinizden uzak tutun. Net bir rıza akışı ve gerçek silme şimdi bir öğleden sonraya mal olur; ilk kurumsal müşteri ya da düzenleyici sorduktan sonra bunları sonradan eklemek çok daha pahalıdır ve aşırı toplanmış veri, elinizde tutmaktan hiçbir şey kazanmadığınız bir yüktür.

**Küçük işletme.** Özel bir gizlilik uzmanı ve sıkı bir bütçeniz yoksa, satın aldığınız araçlara zaten yerleşik gizlilik kontrollerine yaslanın ve veri işlemeyi şeffaf, yerleşimi net kılan tedarikçileri tercih edin. Kararı satın alma-ya-da-kurma olarak çerçeveleyin: belirteçlemeyi ya da hak yerine getirmeyi neredeyse hiçbir zaman kendiniz kurmazsınız; bu yüzden saklama kurallarını, dışa aktarmayı ve silmeyi kutudan çıktığı gibi sunan platformları seçin. Hangi kişisel veriyi nerede tuttuğunuzu ve yanlış ya da kaybolmuş bir kaydın size hangi müşteriye mal olacağını bilin ve belge kısa olsa bile her kullanım için bir hukuki dayanak yazın.

**Kurumsal.** Ölçekte sorun birçok takım arasındaki tutarlılıktır: paylaşılan bir veri haritası, standartlaştırılmış sınıflandırma kademeleri ve hiçbir grubun en zayıf halka olmaması için uygulanan saklama. Sistemler arası silme, belirteç kasaları ve yerleşime duyarlı mimari için mühendisliği açıkça bütçeleyin ve alt işleyicileri merkezi olarak yönetin; böylece tek bir tedarikçi sizin adınıza bir aktarım yükümlülüğünü ihlal edemez. DPIA'ları teslimat sürecinde bir kapı yapın ve gizlilik duruşunu ölçün, çünkü denetçiler ve düzenleyiciler sizden uyumu yalnızca ileri sürmenizi değil, göstermenizi isteyecektir.

**Kamu.** Tedarik kuralları, şeffaflık görevleri ve kamusal hesap verebilirlik her seçimi şekillendirir ve vatandaşlar vergi, sağlık ya da yardım verilerini başka yere götüremez; bu yüzden özen borcu artmıştır. Hassas kayıtları yedekler ve analitik dahil akredite ulusal ortamlara sabitleyin, her tedarikçiyi aynı yerleşim ve silme yükümlülüklerine sözleşmeyle bağlayın ve temel işleme için bir hukuki dayanak (çoğu zaman kamu görevi) belgeleyin; isteğe bağlı kullanımları ayrı, geri çekilebilir rızada tutun. Neyi neden topladığınızın sade dille açıklamalarını yayımlayın ve hak yerine getirmeyi yasal süreler içinde güvenilir kılın, çünkü buradaki bir gizlilik başarısızlığı hizmetin dayandığı kamusal güveni aşındırır.

## Örnekler

**Girişim.** Erken aşamadaki bir tüketici uygulaması yalnızca gerçekten ihtiyaç duyduğu veriyi toplar, çünkü her fazladan alan sonradan savunmak istemeyeceği bir yüktür. Bir silme talebine gerçekten cevap verebilmek için kişisel verinin nerede yaşadığını gösteren basit bir elektronik tablo veri haritası tutar, e-postaları ve belirteçleri günlüklerinden uzak tutar ve çoktan ölmüş hesapların verisini temizlemek için temel bir saklama kuralı koyar. Net bir rıza akışı ve gerçek silme kurmak şimdi bir öğleden sonraya mal olur; ilk kurumsal müşteri ya da düzenleyici sorduktan sonra sonradan eklemek çok daha pahalıdır.

**Kurumsal.** Küresel bir tüketici uygulaması yeni bir öneri özelliğini yayınlamadan önce bir DPIA yürütür ve gereksiz yere kesin konum toplayacağını keşfeder; takım kaba bölge verisine geçer ve ürün kaybı olmadan riski azaltır. Kart numaraları belirteçlenir; böylece yalnızca küçük, sıkı kontrol edilen bir kasa ham değerleri tutar ve şirketin [PCI](https://en.wikipedia.org/wiki/Payment_Card_Industry_Data_Security_Standard) (ödeme kartı endüstrisi) kapsamını dramatik biçimde daraltır. Otomatik saklama kuralları etkin olmayan hesapların verisini takvimine göre temizler ve self servis bir akış kullanıcıların verilerini, yedekler dahil tüm sistemlerde, yasal süre içinde dışa aktarmasını ve silmesini sağlar.

**Kamu.** Ulusal bir sağlık hizmeti tüm hasta kayıtlarını PHI ve özel kategoride veri olarak sınıflandırır; sıkı erişim kontrolleri, şifreleme ve denetim günlüğü uygular. Veri yerleşimi politikası yedekler ve analitik dahil tüm kayıtları ulusal sınırlar içinde tutar ve her tedarikçi sözleşmeyle aynısına bağlıdır. Temel işleme için belgelenmiş bir hukuki dayanak (kamu görevi) vardır; isteğe bağlı araştırma kullanımları ise kaydedilen ve gözetilen ayrı, geri çekilebilir rıza gerektirir. Bir veri haritası, erişim ve silme taleplerine yasal süreler içinde cevap verebilme yeteneğinin temelini oluşturur.

## İş gerekçesi: motivasyonlar, YG ve TSM

Gizlilik yatırımı çoğu zaman salt uyum maliyeti olarak çerçevelenir, ama bu onu eksik anlatır. Toplam sahip olma maliyeti (TSM) DPIA süreçlerini, veri haritalama ve envanter araçlarını, belirteçleme ve saklama altyapısını ve bireysel hakları ve yerleşimi destekleyecek mühendisliği içerir. Bunu yatırım yapmamanın maliyetine karşı tartın; bu maliyet ağırdır ve giderek daha olasıdır. Gizlilik cezaları artık küresel gelirin yüzdelerine ulaşıyor, büyük ihlallerin ardından toplu davalar geliyor ve düzenleyiciler harekete geçeceklerini gösterdi. Cezaların ötesinde, kötü yönetilen gizlilik geliri ayakta tutan müşteri güvenini yok eder. Üstelik bir gizlilik başarısızlığını sonradan düzeltmek (silmeyi sonradan eklemek, hukuka aykırı veri akışlarını çözmek) baştan içine işlemekten çok daha pahalıdır.

Yatırım getirisinin (YG) de gerçek bir artı yanı vardır. Güçlü gizlilik rekabetçi bir farklılaştırıcıdır ve düzenlemeye tabi ve kamu pazarlarında iş kazanmanın ön koşuludur. Veri minimizasyonu ihlal maruziyetini ve depolama maliyetini doğrudan azaltır ve belirteçleme PCI-DSS gibi denetimlerin pahalı kapsamını daraltır. Liderliğe gerekçeyi sunarken gizliliği iki biçimde sunun: gerçek düzenleyici maruziyeti olan riske göre ayarlanmış yük yönetimi olarak ve pazarları açan bir güven varlığı olarak. Tasarımla gizliliğin, davayla gizliliğe kıyasla ucuz olduğunu ve amaçsız biriktirilen verinin bilançoda duran, gerçekleşmeyi bekleyen bir yük olduğunu vurgulayın.

## Anti-kalıplar ve tuzaklar

- **Her şeyi topla, sonra karar ver.** Amaçsız veri biriktirmek; fayda olmadan yükü en üst düzeye çıkarmak.
- **İhmalle saklama.** Takvim olmadığı için hiçbir şeyi silmemek; veri sonsuza kadar birikir.
- **Rıza tiyatrosu.** Önceden işaretlenmiş kutular, paketlenmiş rıza ya da hukuken geçersiz olan ve güveni aşındıran karanlık kalıplar.
- **Yedekleri kaçıran silme.** Birincil depodan silip yedeklerde, günlüklerde ve analitikte kopyaları bırakmak.
- **Günlüklerde ve test verisinde PII.** Hassas veriyi az kontrol edilen, kolayca açığa çıkabilen ortamlara yaymak.
- **Veri akışlarını görmezden gelmek.** Günlüklerin, yedeklerin, analitiğin ve alt işleyicilerin veriyi sınırlar ötesine taşıdığını gözden kaçırmak.
- **Yalnızca hukuki bir kaygı olarak gizlilik.** Onu bir mühendislik tasarım kısıtı değil, evrak işi olarak ele almak.
- **Veri haritası yok.** Kişisel verinin nerede yaşadığını cevaplayamamak; bu da hak taleplerini ve ihlal yanıtını imkânsız kılar.

## Olgunluk modeli

**Düzey 1, Başlangıç.** Gizlilik, varsa tepkisel biçimde ele alınır. Kişisel veri envanter, minimizasyon ya da saklama sınırı olmadan serbestçe toplanır. Rıza sonradan akla gelen bir şeydir, erişim ya da silme talepleri için süreç yoktur ve verinin fiziksel olarak nerede yaşadığı düşünülmez.

**Düzey 2, Geliştirme.** Temel pratikler ortaya çıkar ama takıma göre değişir. Bir gizlilik politikası vardır ve temel rıza alınır; saklama konusunda biraz farkındalık vardır. Hak talepleri elle ve yavaş ele alınır, veri sınıflandırması gayriresmidir ve bir takım verisini haritalarken bir diğeri serbestçe toplayabilir. Kurum genelinde hiçbir şey tutarlı biçimde uygulanmaz.

**Düzey 3, Standartlaştırma.** Tasarımla gizlilik belgelenmiş ve kurum genelinde uygulanır. Daha yüksek riskli projeler için DPIA'lar yürütülür, veri kademelere haritalanır ve sınıflandırılır ve saklama takvimleri otomatik silmeyle uygulanır. Her işleme faaliyeti için bir hukuki dayanak belgelenir, geçerli rıza mekanizmaları yerindedir, hak talepleri sürelerinde yerine getirilir ve düzenlemeye tabi veri için yerleşim ele alınır.

**Düzey 4, Yönetme.** Gizlilik programı taban çizgilerine karşı ölçülür ve kontrol edilir. Hak talebi yerine getirme süresini yasal sürelere karşı, saklama politikası kapsamını ve en eski kayıtların yaşını, kapsamdaki kişisel veri alanlarının sayısını ve kaçının belirteçlendiğini ya da takma adlandırıldığını, uygun özellikler için DPIA tamamlama oranlarını ve denetimlerde bulunan yönetilmeyen sınır ötesi akışların sayısını izlersiniz. Metrikler tanımlı eşikleri besler; böylece bir hedefin aşılması (süresine yaklaşan bir hak talebi, beklenmedik bir aktarım, saklama kayması) fark edilmeden geçmek yerine belgelenmiş bir yanıtı tetikler.

**Düzey 5, Orkestrasyon.** Gizlilik, sürekli iyileşen ve kurum genelinde entegre olan varsayılan bir mühendislik kısıtıdır. Minimizasyon, belirteçleme ve otomatik saklama standarttır, hak talepleri self servistir ve yedekler dahil tüm sistemlerde eksiksizdir, veri akışları ve yerleşim sürekli izlenir ve uygulanır. Gizlilik duruşu düzenleme, pazarlar ve mimari değiştikçe uyum sağlar; dersleri tasarıma geri besler, böylece taban çizgisi yalnızca korunmak yerine yükselmeyi sürdürür.

## Tartışma fikirleri

1. Daha fazla veri isteyen analitik takımları ile daha azını isteyen gizlilik arasındaki gerilimi nasıl çözersiniz?
2. Birincil depolar, yedekler ve aşağı akış kopyaları boyunca silmeye saygı göstermek için gerçekçi bir mimari nedir?
3. İşleme faaliyetlerinizin her birine hangi hukuki dayanak uyar ve seçimi savunabilir misiniz?
4. Hata ayıklamayı engellemeden kişisel veriyi günlüklerden ve üretim dışı ortamlardan nasıl uzak tutarsınız?
5. Pazarlarınıza hangi veri yerleşimi gereksinimleri uygulanır ve yedekler ile analitik bunları nasıl karmaşıklaştırır?
6. Gizlilik ve güvenlik tehdit modellemesi tek bir tasarım faaliyetinde nasıl birleştirilmeli?

## Önemli çıkarımlar

- Gizlilik, kişisel veriyi kullanıp kullanmayacağınızı ve nasıl kullanacağınızı yönetir; güvenlikten ayrıdır ve onu tamamlar.
- Gizliliği baştan DPIA'lar ve gizliliği koruyan varsayılanlarla tasarıma içeri işleyin.
- Toplamayı en aza indirin, saklama takvimlerini uygulayın ve gerçek silme yeteneği kurun.
- PII, PHI ve özel kategorileri sınıflandırın ve belirteçleme ve maskeleme ile orantılı biçimde koruyun.
- Bir hukuki dayanak belirleyin ve belgeleyin; rızayı özgürce verilmiş, belirli ve geri çekilebilir yapın.
- Veri yerleşimini ve sınır ötesi aktarımı birinci derece mimari kısıtlar olarak ele alın.
- Veri bir varlık olduğu kadar bir yüktür; amaçsız biriktirmek gerçekleşmeyi bekleyen risktir.

## Kaynaklar ve ileri okuma

- Ann Cavoukian, *Privacy by Design: The 7 Foundational Principles*
- European Union, *General Data Protection Regulation (GDPR)* text and guidance
- National Institute of Standards and Technology, *Privacy Framework* and *SP 800-122* (Guide to Protecting PII)
- ISO/IEC 27701, *Privacy Information Management*
- Daniel Solove, *Understanding Privacy*
- OECD, *Privacy Guidelines* and *Fair Information Practice Principles (FIPPs)*
- California Consumer Privacy Act (CCPA/CPRA) statutory text and regulator guidance
