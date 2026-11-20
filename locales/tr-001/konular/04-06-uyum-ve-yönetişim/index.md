# 4.6 Uyum ve yönetişim

## Genel bakış ve motivasyon

Uyum, kurumunuzun yasal, sözleşmesel ve etik yükümlülüklerini yerine getirdiğini denetçilere, düzenleyicilere, müşterilere ve vatandaşlara kanıtlama disiplinidir. Yönetişim ise uyumu kahramanca bir yıllık telaş değil, kurumun tekrarlanabilir bir özelliği yapan politikalar, roller ve kontroller yapısıdır. Büyük kurumlar için ve özellikle kamu için uyum isteğe bağlı bir yük değildir. Çoğu zaman faaliyet ruhsatının kendisidir. Doğru sertifikalar ve yetkilendirmeler olmadan düzenlemeye tabi sektörlere satış yapamaz, kamu sözleşmelerini kazanamaz ve belirli veri türlerini yasal olarak işleyemezsiniz.

Uyum manzarası geniş ve katmanlıdır. Kurumlar veri koruma yasaları (GDPR, CCPA), sektör kuralları (sağlık için HIPAA, ödeme kartları için PCI-DSS, finansal raporlama için SOX) ve gönüllü ama beklenen sertifikalar (ISO 27001, SOC 2) arasında yol bulur. Kamu ve yüklenicileri ek bir evrenle karşılaşır: FedRAMP ve FISMA yetkilendirmeleri, NIST 800-53 ve 800-171 kontrol katalogları, savunma tedarik zinciri için CMMC, etki düzeyi sınıflandırmaları, erişilebilirlik yükümlülükleri (Section 508, ADA, WCAG, EN 301 549) ve FOIA dahil kayıt yükümlülükleri. Bunların hepsini elle yönetmek ölçeklenmez. Modern cevap, kontrollerin otomatikleştirildiği ve kanıtın normal operasyonların yan ürünü olarak üretildiği sürekli uyumdur.

Bu bölüm başlıca çerçeveleri, ağır ağırlık taşıyan kamuya özgü rejimleri, yasal bir yükümlülük olarak erişilebilirliği ve dönemsel denetimlerden sürekli, kanıta dayalı uyuma ve sağlam yönetişime geçişi kapsar.

## Temel ilkeler

- **Uyum iyi mühendisliğin yan ürünüdür.** Güçlü kontrollere sahip iyi işletilen sistemler kanıtı doğal olarak üretir; uyum tiyatrosu üretmez.
- **Kontrolleri bir kez eşleyin, birçok çerçeveyi karşılayın.** Tek bir kontrol çoğu zaman birden fazla standardın gereksinimlerini karşılar; birleşik bir kontrol kümesi yönetin.
- **Dönemselden çok sürekli.** Uyum denetim öncesi bir telaş değil, her zaman açık olsun diye kanıt toplamayı otomatikleştirin.
- **Yönetişim hesap verebilirliği tanımlar.** Politikaların, kontrollerin ve risklerin net sahipliği uyumu sürdürülebilir kılar.
- **Erişilebilirlik bir gerekliliktir, nezaket değil.** Kamu için ve giderek kurumsal tarafta yasal olarak zorunludur.
- **Kayıtlar yükümlülüktür.** Kayıtların saklanması, elden çıkarılması ve açıklanması, özellikle kamuda yasal güç taşır.
- **Denetçi için tasarlayın.** Net, değiştirilemez kanıt üreten sistemlerin denetimi daha ucuz, güvenilmesi daha kolaydır.

## Öneriler

### Geçerli çerçeveleri bilin ve kontrolleri bir kez eşleyin

Önce kurumunuzu hangi rejimlerin bağladığını belirleyin, sonra her kontrolü karşıladığı her gereksinime eşleyen birleşik bir kontrol çerçevesi kurun.

- **GDPR / CCPA:** AB'nin [Genel Veri Koruma Tüzüğü](https://en.wikipedia.org/wiki/General_Data_Protection_Regulation) ve [Kaliforniya Tüketici Gizliliği Yasası](https://en.wikipedia.org/wiki/California_Consumer_Privacy_Act) kapsamında veri koruma ve gizlilik hakları (bkz. bölüm 4.5).
- **HIPAA:** ABD sağlık sektöründe korunan sağlık bilgisi için güvenceler gerektiren [Sağlık Sigortası Taşınabilirliği ve Hesap Verebilirliği Yasası](https://en.wikipedia.org/wiki/Health_Insurance_Portability_and_Accountability_Act).
- **PCI-DSS:** ödeme kartı verisini işlemek için güvenlik kontrollerini zorunlu kılan [Ödeme Kartı Endüstrisi Veri Güvenliği Standardı](https://en.wikipedia.org/wiki/Payment_Card_Industry_Data_Security_Standard); kapsam daraltma (belirteçleme) maliyeti keskin biçimde düşürür.
- **SOX:** finansal raporlama üzerinde kontroller gerektiren, değişiklik yönetimini, erişim kontrolünü ve denetim izlerini vurgulayan [Sarbanes-Oxley Yasası](https://en.wikipedia.org/wiki/Sarbanes%E2%80%93Oxley_Act).
- **[ISO 27001](https://en.wikipedia.org/wiki/ISO/IEC_27001):** sertifikalandırılabilir, riske dayalı kontrollere sahip bir bilgi güvenliği yönetim sistemi (BGYS).
- **SOC 2:** güvenlik, erişilebilirlik, gizlilik, işleme bütünlüğü ve mahremiyet etrafındaki kontrollerin bir Sistem ve Kurum Kontrolleri doğrulaması; kurumsal alıcılar tarafından yaygın biçimde beklenir.
- **[NIST Siber Güvenlik Çerçevesi](https://en.wikipedia.org/wiki/NIST_Cybersecurity_Framework) (CSF):** Ulusal Standartlar ve Teknoloji Enstitüsü'nden (NIST) güvenliği Tanımla, Koru, Tespit Et, Yanıtla, Kurtar (ve Yönet) olarak düzenleyen esnek, gönüllü bir çerçeve.

Bu çerçevelere çapraz eşlenmiş tek bir kontrol kütüphanesi tutun; böylece bir kontrolü uygulamak (örneğin erişim gözden geçirmesi) SOC 2, ISO 27001 ve diğerleri için aynı anda kanıt üretir. Bu çapraz eşleme, kurumsal uyumdaki en yüksek kaldıraçlı hamledir.

### Kamuya özgü rejimleri titizlikle karşılayın

Kamu işi, ayrı ve pazarlık edilemez gereksinimler getirir.

- **[FISMA](https://en.wikipedia.org/wiki/Federal_Information_Security_Management_Act_of_2002)** (Federal Bilgi Güvenliği Yönetimi Yasası) federal bilgi güvenliğini yönetir; **[NIST SP 800-53](https://en.wikipedia.org/wiki/NIST_Special_Publication_800-53)** federal sistemler için sistem kategorizasyonuna (düşük/orta/yüksek etki) göre seçilen kontrol kataloğunu sağlar.
- **[FedRAMP](https://en.wikipedia.org/wiki/FedRAMP)** (Federal Risk ve Yetkilendirme Yönetimi Programı) bulut hizmetlerinin federal kullanım için yetkilendirilmesini standartlaştırır; etki düzeylerine bağlı taban çizgileri ve hedef olarak bir Faaliyet Yetkisi (ATO) vardır.
- **NIST SP 800-171**, federal olmayan sistemlerde Kontrollü Sınıflandırılmamış Bilgiyi (CUI) korur ve yüklenicileri bağlar.
- **CMMC** (Siber Güvenlik Olgunluk Modeli Sertifikasyonu), savunma sanayi tabanı yüklenicilerinin gerekli kontrolleri kademeli düzeylerde uyguladığını doğrular.
- **Etki Düzeyleri (IL)** veri hassasiyetini sınıflandırır (örneğin Savunma Bakanlığı (DoD) IL2'den IL6'ya kademeleri) ve gereken ortamı ve kontrolleri belirler.

Bunlara belgelenmiş bir **Sistem Güvenlik Planı (SSP)**, boşluklar için bir **Eylem ve Kilometre Taşları Planı (POA&M)** ve ATO'yu bir kerelik olay saymak yerine yetkiyi sürdürmek için sürekli izlemeyle yaklaşın.

### Erişilebilirliği yasal bir yükümlülük olarak ele alın

Erişilebilirlik hem etik bir görevdir hem de birçok yargı bölgesinde yasadır.

- **[Section 508](https://en.wikipedia.org/wiki/Section_508_Amendment_to_the_Rehabilitation_Act_of_1973)** ABD federal sistemlerinin (ve çoğu zaman yüklenicilerinin) erişilebilir olmasını gerektirir; **[ADA](https://en.wikipedia.org/wiki/Americans_with_Disabilities_Act_of_1990)** (Engelli Amerikalılar Yasası) yükümlülükleri giderek ticari dijital hizmetlere uzanır; **EN 301 549** kamu sektörü tedariki için Avrupa standardıdır.
- Genellikle AA düzeyindeki **[Web İçeriği Erişilebilirlik Yönergeleri](https://en.wikipedia.org/wiki/Web_Content_Accessibility_Guidelines) (WCAG)**, bu yükümlülüklerin atıf yaptığı teknik ölçüttür.
- Erişilebilirliği bir düzeltme turu olarak değil, tasarıma ve teste içeri işleyin: anlamsal işaretleme, klavye gezintisi, yeterli kontrast, ekran okuyucu desteği ve altyazılar.
- Otomatik araçlarla ve gerçek yardımcı teknoloji kullanıcılarıyla test edin ve uyumu belgeleyin (örneğin bir erişilebilirlik uyum raporu aracılığıyla; buna Voluntary Product Accessibility Template ya da VPAT de denir).

### Denetime hazırlığı ve sürekli uyumu kurun

Dönemsel telaştan her zaman hazır duruşa geçin.

- **Kanıt toplamayı otomatikleştirin:** kontrol kanıtını (erişim gözden geçirmeleri, tarama sonuçları, değişiklik onayları, yedekler) her denetimden önce elle toplamak yerine otomatik ve sürekli çekin.
- Kontrolleri dağıtım anında uygulamak ve doğrulamak için **kod olarak uyum** ve politika motorları kullanın; kanıt yan etki olarak üretilir.
- Durumu ve boşlukları gösteren canlı bir kontrol panosu tutun; böylece kurum her an denetime hazırdır.
- İstisnaları ve risk kabullerini sahipleri ve son kullanma tarihleriyle açıkça yönetin; boşlukların sessizce sürmesine izin vermeyin.

### Kayıt yönetimini ve açıklamayı yönetin

Kayıtlar, özellikle kamuda, ayrı yasal yükümlülükler taşır.

- **Kayıt yönetimi** politikası belirleyin: neyin kayıt sayıldığı, her sınıfın ne kadar saklandığı ve nasıl elden çıkarıldığı; yasal takvimlerle hizalı.
- Kayıtların özgün, eksiksiz ve kurcalamaya karşı belirgin olduğundan, denetim izleriyle birlikte emin olun.
- Kamu için **[FOIA](https://en.wikipedia.org/wiki/Freedom_of_Information_Act_(United_States))** (Bilgi Edinme Özgürlüğü Yasası ve eşdeğer şeffaflık yasaları) için hazırlanın: kayıtları yasal süreler içinde bulma, gözden geçirme, karartma ve yayımlama yeteneği.
- Çatışabilen kayıt saklama yükümlülüklerini gizlilik silme haklarıyla bağdaştırın; kurumun bu gerilimi nasıl çözdüğünü belgeleyin.

## Ödünleşimler: artılar ve eksiler

| Karar | Artılar | Eksiler |
|---|---|---|
| Çok sayıda sertifika peşinde koşmak | Pazarları açar, güven kurar | Maliyetli, süregelen denetim yükü |
| Birleşik kontrol çerçevesi | Verimli, bir kez eşle birçoğunu karşıla | Çapraz eşlemeyi kurmak için baştan emek |
| Sürekli uyum otomasyonu | Her zaman denetime hazır, denetim başına daha düşük maliyet | Araç yatırımı, mühendislik emeği |
| Yalnızca belirli an denetimleri | Daha düşük anlık maliyet | Telaş, denetimler arası sapma, daha yüksek risk |
| Kurum içi uyum takımı | Derin bağlam, kontrol | Pahalı, tüm uzmanlıkları kadrolamak zor |
| GRC platformu / danışmanlar | Uzmanlık, araçlar, hız | Maliyet, tedarikçi bağımlılığı |
| FedRAMP/ATO peşinde koşmak | Federal pazara erişim | Uzun, pahalı, ağır belgeleme |

Her şeyi kapsayan ödünleşim, maliyet ve emek ile pazar erişimi ve risk azaltma arasındadır. Sertifikalar ve yetkilendirmeler pahalı ve yavaştır, ama birçok kurum için bütün pazarlara giriş biletidir: FedRAMP yoksa federal bulut işi yok; SOC 2 yoksa kurumsal anlaşma yok. Verimli yol, birleşik ve otomatik bir kontrol çerçevesine bir kez yatırım yapar; böylece her ek sertifikanın marjinal maliyeti düşük kalır. Sürekli uyum, son dakika denetim telaşından baştan daha pahalıya gelir, ama zaman içinde dramatik biçimde daha ucuz ve daha az risklidir. Uyumu tekrarlayan bir krizden kararlı durum özelliğine dönüştürür.

## Takımınızla tartışılacak sorular

1. **Kontrol kütüphanenizdeki hangi kontroller en çok çerçeveye eşleniyor ve bunların kanıtını otomatik mi topluyorsunuz?** Kurumsal uyumdaki en yüksek kaldıraçlı hamle, tek bir kontrolü uygulamanın (örneğin erişim gözden geçirmeleri) SOC 2, ISO 27001, HIPAA ve daha fazlası için aynı anda kanıt üretmesini sağlayan çapraz eşlenmiş birleşik bir kontrol kümesidir. Hangi kontrollerin bu çok çerçeveli ağırlığı taşıdığına karar verin ve kanıtlarını otomatikleştirmeyi önceliklendirin, çünkü bunlar her denetimde karşılığını verir. Sürekli, otomatik kanıt her denetimi pahalı bir yangın tatbikatından canlı bir depoya karşı rutin bir kontrole çevirir ve bir sonraki sertifikayı eklemenin marjinal maliyetini keskin biçimde düşürür. Mevcut kontrol listenizi getirin ve hangilerinin hâlâ her denetimden önce toplanan elle alınmış ekran görüntülerine dayandığını işaretleyin; çünkü bunlar sapma ve telaş riskinizdir. Her çerçeveyi kendi silosunda yönetiyorsanız, tek bir çapraz eşlemenin ortadan kaldıracağı emeği çoğaltıyorsunuz.

2. **Hedefiniz bir FedRAMP ATO ya da benzer bir yetkilendirmeyse, yalnızca elde etmeyi değil, sürdürmeyi de başarabilir misiniz?** Kamu yetkilendirmeleri sözleşmenin kapısıdır ve ATO'yu bir kerelik saymak klasik bir başarısızlıktır, çünkü kapıyı açık tutan sürekli izlemedir. Canlı bir Sistem Güvenlik Planı sürdürme, boşluklar için bir Eylem ve Kilometre Taşları Planı yürütme ve NIST SP 800-53 kontrollerini sisteminizin etki kategorizasyonuna göre seçme disiplinine sahip olup olmadığınıza karar verin. Bu rejimler titiz ve pazarlık edilemezdir; belgeleme ve izleme yükü önemli ve süreklidir, bir lansman günü atağı değildir. Yetkilendirmeyi gerektiren hattı getirin ve onu sürdürmenin gerçek maliyetine karşı tartın; böylece yatırım bilinçli bir iş kararı olur. Kontrollü Sınıflandırılmamış Bilgi kapsamdaysa, NIST SP 800-171'i ve geçerli CMMC düzeyini de karşıladığınızı doğrulayın, çünkü ikisinden birini kaçırmak sizi diskalifiye edebilir.

3. **Erişilebilirlik uyumu tamamlanma tanımınızda mı, yoksa bir denetimde başarısız olmayı bekleyen bir düzeltme turu mu?** Erişilebilirlik yasal bir yükümlülüktür, nezaket değil: Section 508 ABD federal sistemlerini ve çoğu zaman yüklenicilerini bağlar, ADA yükümlülükleri giderek ticari dijital hizmetlere uzanır ve EN 301 549 Avrupa kamu sektörü tedarikini yönetir. WCAG AA'yı geç aşamada eklemek yerine (bu zayıf, uyumsuz sonuçlar ve yasal maruziyet üretir) tasarıma ve teste içeri işleyin (anlamsal işaretleme, klavye gezintisi, yeterli kontrast, ekran okuyucu desteği, altyazılar). Otomatik araçların yanı sıra gerçek yardımcı teknoloji kullanıcılarıyla test edip etmeyeceğinize ve bunu isteyen alıcılar için uyumu bir VPAT'ta belgeleyip belgelemeyeceğinize karar verin. Yayındaki bir arayüzü getirin ve toplantıda yalnızca klavyeyle ve ekran okuyucuyla bir tur atın, çünkü bulduğunuz boşluklar aksi halde daha sonra alacağınız denetim bulgularıdır. Kamu işinde bu uyum bir tedarik ön koşuludur; bu yüzden onu bir temizlik görevi değil, bir kapı olarak ele alın.

4. **Her kontrolün ve her risk kabulünün sahibi kim ve istisnalarınızın sahipleri ve son kullanma tarihleri var mı?** Yönetişim, uyumu yıllık bir telaştan kalıcı bir özelliğe çeviren şeydir ve bir kontrolün belgeleri olup hesap verebilir bir sahibi olmadığında ya da "geçici olarak" verilen bir risk kabulü yıllarca sürdüğünde sessizce başarısız olur. Her kontrolü kimin onayladığına, istisnaları kimin gözden geçirdiğine ve boşlukların bir elektronik tabloda sessizce sürmek yerine nasıl sahip ve son tarih aldığına karar verin. Rekabet eden çekim hız ile hesap verebilirlik arasındadır: sahip adlandırmak ve son kullanma tarihini uygulamak insanları yavaşlatır, ama sahipsiz kontroller sapar ve sınırsız istisnalar denetimi batıran bulguya dönüşür. Mevcut istisna kayıt defterinizi getirin ve kaç girdinin adlandırılmış bir sahibi ve geçerli bir son kullanma tarihi olduğuna bakın, çünkü boşluklar biriken riskinizdir. Büyük bir kurum için bu birçok takım arasında denetim alanıdır; kamu için ise hesap verebilir yetkili ve belgelenmiş risk kabulü, bir gözden geçirenin talep edeceği denetim eserleridir.

5. **Kayıt saklama yükümlülükleri gizlilik silme haklarıyla çatıştığında bu çatışmayı nasıl çözüyorsunuz ve çözüm yazılı mı?** Bu görevler gerçekten çatışır: yasa bir kaydı yıllarca saklamanızı gerektirirken veri sahibi unutulma hakkını kullanabilir ve doğaçlama silme yapan bir mühendis, aşırı geniş bir tutma kadar kolaylıkla saklama takvimini ihlal edebilir ya da gizlilik yasasını çiğneyebilir. Öncelik kurallarını önceden, kayıt sınıfı sınıfı belirleyin ve bir yasal tutmanın, bir karartmanın ya da hukuki dayanak istisnasının bir silme talebini nasıl geçersiz kıldığını belgeleyin. Tartılacak gerilim, şeffaflık ve bireysel haklar ile yasal saklama ve bir FOIA ya da keşif talebine yasal bir zaman çizelgesinde cevap verebilme yeteneği arasındadır. Saklama takviminizi ve gerçek bir silme talebini getirin ve toplantıda gerçek karar yolunu adım adım izleyin. Kamu için bahisler en yüksektir, çünkü FOIA cevap süreleri, kayıt elden çıkarma yasası ve gizlilik hakları aynı anda yasal güç taşır ve uzlaştırma birden fazla düzenleyiciye karşı savunulabilir olmalıdır.

6. **Uyum yeteneğini kurum içinde mi kuruyorsunuz yoksa satın mı alıyorsunuz ve bu seçim gelirinizi gerçekten kapılayan sertifikalarla örtüşüyor mu?** Sürekli uyumun gösterişsiz temeli kadro ve araçlardır ve planlar çerçeveden çok, GRC platformunu işletecek, kontrollerin kanıtını sunacak ya da yeni bir rejimi yorumlayacak kimsenin olmamasından başarısız olur. Hangi kısımları kurum içinde kadrolayacağınıza, hangilerini bir yönetişim, risk ve uyum platformu olarak satın alacağınıza ve belirli bir yetkilendirme için nerede danışman getireceğinize bilinçli karar verin, sonra bunu gerçek satış hattını açan sertifikalarla eşleştirin. Ödünleşim, tam bir uyum işlevinin gerektirdiği maliyet ve nadir uzmanlara karşı derin kurum içi bağlam ve kontrol ile satın alırsanız tedarikçi bağımlılığı ve yinelenen ücretler arasındadır. Açık anlaşmalara bağlı sertifikaların listesini, elle yapılan bir denetim telaşının gerçek maliyetini ve mevcut kadro boşluklarınızı getirin. Kurumsal tarafta bu birçok denetim arasında portföy ekonomisidir; kamuda ise yetkilendirme ve güvenlik izninin uzun hazırlık süreleri, ilgili pencerede kadrolayamayacağınız bir yeteneğin kazanamayacağınız bir sözleşme olduğu anlamına gelir.

## Sektör merceği

**Girişim.** Yalnızca önünüzdeki anlaşmayı açan sertifikanın peşinden gidin, genellikle SOC 2, ve ona işe alımla değil bir uyum otomasyon aracıyla ulaşın. Gerçekten sürdürebileceğiniz bir avuç kontrolü yazın, kanıt toplamayı ilk günden bulutunuza ve kodunuza bağlayın ve henüz hiçbir müşterinin istemediği çerçeveleri atlayın. Gerçek alışkanlıklardan kazanılmış bir Tip I raporu, asla uymayacağınız hevesli politikalardan oluşan bir klasörden iyidir.

**Küçük işletme.** Özel bir uyum uzmanı ve sıkı bir bütçeniz yoksa, bir işlev kurmak yerine bir yönetişim, risk ve uyum platformuna ya da kısmi zamanlı bir danışmana yaslanın. Bir logo duvarı yerine alıcılarınızın gerçekten talep ettiği sertifikaları tercih edin ve kayıt saklamayı ve erişilebilirliği bir program değil somut kontrol listeleri olarak ele alın. Çapraz eşlemeyi ve kanıt otomasyonunu kurmak yerine satın alın, çünkü kıt mühendislik zamanınız ürüne daha iyi harcanır.

**Kurumsal.** İş, birçok takım arasında portföy yönetişimidir: SOC 2, ISO 27001, HIPAA ve PCI-DSS'e çapraz eşlenmiş tek bir birleşik kontrol kütüphanesi, kanıt paylaşılan bir depoya otomatik toplanır. Her kontrol ve risk kabulü için sahip adlandırın, istisnalarda son kullanma tarihini uygulayın ve sertifikaları bir portföy olarak yönetin; böylece bir sonrakini eklemek düşük maliyetli olur. GRC araçlarını ve denetim takvimini açıkça bütçeleyin ve uyumu yıllık bir yangın tatbikatı değil, kararlı durum özelliği olarak koruyun.

**Kamu.** Tedarik kuralları, şeffaflık ve kamusal hesap verebilirlik her seçimi şekillendirir. FedRAMP ya da FISMA yetkisini lansman günü atağı değil, canlı bir Sistem Güvenlik Planı ve sürekli izlemeyle sürdürülen bir yükümlülük olarak ele alın ve WCAG AA uyumunu ve Section 508'i tedarik kapıları olarak tutun. Kayıt elden çıkarma ve FOIA sürelerini yasal zaman çizelgelerinde karşılayın, bunları gizlilik silme haklarıyla yazılı olarak uzlaştırın ve her sonuç doğurucu kontrol için hesap verebilir bir yetkili adlandırılmış tutun.

## Örnekler

**Girişim.** Tohum aşamasındaki bir SaaS girişimi ilk kurumsal anlaşmasının elinde olmayan bir SOC 2 raporuna takıldığını görür; bu yüzden küçük başlar: bulutunu ve kodunu izleyen bir uyum otomasyon aracını açar ve görmezden geleceği hevesli politikalar yerine gerçekten sürdürebileceği bir avuç kontrolü yazar. Erişim gözden geçirmeleri, yedekler ve değişiklik onayları dahil kanıtı baştan otomatik toplayarak, panik dolu bir çeyrek ekran görüntüsü yerine haftalar içinde bir Tip I raporuna ulaşır. Bu kontrolleri denetim tiyatrosu yerine gerçek alışkanlıklar olarak ele almak, sertifikanın takımın gerçekte nasıl çalıştığını yansıttığı ve peşinde oldukları geliri açtığı anlamına gelir.

**Kurumsal.** Bir bulut yazılım tedarikçisi SOC 2, ISO 27001, HIPAA ve PCI-DSS'e çapraz eşlenmiş tek bir kontrol çerçevesi kurar. Kanıt (erişim gözden geçirmeleri, zafiyet taramaları, değişiklik onayları, yedek doğrulaması) bir GRC (yönetişim, risk ve uyum) platformuna otomatik toplanır; böylece her yıllık denetim, çılgınca geçen bir ekran görüntüsü ayı yerine canlı bir kanıt deposundan beslenir. Kontroller çerçeveler arasında eşlendiği için SOC 2'den sonra ISO 27001'i eklemek az ek emek gerektirdi ve şirket kurumsal alıcılara talep üzerine güncel bir doğrulama sunarak satış döngülerini kısaltabiliyor.

**Kamu.** Federal bir bulut dağıtımının peşindeki bir yüklenici sistemini FISMA orta olarak kategorize eder, ilgili NIST SP 800-53 kontrollerini seçer ve bir Sistem Güvenlik Planı ve kalan boşlukları izleyen bir POA&M ile FedRAMP yetkisine doğru çalışır. Kontrollü Sınıflandırılmamış Bilgiyi işlediği için savunma işi için NIST SP 800-171'i ve geçerli CMMC düzeyini de karşılar. Vatandaşa dönük her arayüz Section 508'i karşılamak için WCAG AA'ya uyar ve bir VPAT'ta belgelenir. Kayıtlar yasal saklama takvimlerini izler ve FOIA cevap sürelerini karşılamak için aranabilir durumdadır; sürekli izleme yetkiyi zaman içinde korur.

## İş gerekçesi: motivasyonlar, YG ve TSM

Uyum, güvenlik yatırımları arasında olağandışıdır, çünkü yatırım getirisi (YG) çoğu zaman yalnızca önlenen kayıp değil, doğrudan gelirdir. Doğru sertifikalar ve yetkilendirmeler olmadan bütün pazarlar kapalıdır. SOC 2 kurumsal anlaşmaları, FedRAMP federal olanları, HIPAA ve PCI-DSS sağlık ve ödeme işlerini açar. Toplam sahip olma maliyeti (TSM) denetim ücretlerini, GRC araçlarını, uyum kadrosunu ya da danışmanları ve kontrolleri uygulamak ve kanıtlamak için mühendislik zamanını, ayrıca kamu yetkilendirmelerinin peşinde koşmanın çok önemli maliyetini içerir. Ama uyumsuz olmanın maliyeti işi tamamen kaybetmektir; buna ihlalleri izleyen, gelirin önemli bir yüzdesine ulaşabilen cezalar, yaptırımlar ve sözleşme feshi eklenir.

Verimlilik kaldıracı, sürekli ve otomatik kanıtlı birleşik kontrol çerçevesidir. Her ek sertifikanın marjinal maliyetini keskin biçimde düşürür ve denetimleri pahalı yangın tatbikatlarından canlı bir kanıt deposuna karşı rutin kontrollere çevirir. Liderliğe gerekçeyi sunarken uyumu gelir sağlayıcı ve risk azaltıcı olarak birlikte çerçeveleyin. Her sertifikayı gerektiren hattı, başarısız bir denetimin ya da kaybedilen bir yetkinin maliyetini ve otomasyonun, sonsuz elle telaşlara karşı sağladığı tasarrufu sayılaştırın. Kamu yüklenicileri için yetkilendirmenin sözleşmeye giden kapı olduğunu ve kapıyı açık tutanın sürekli izleme olduğunu vurgulayın.

## Anti-kalıplar ve tuzaklar

- **Denetim güdümlü telaşlar.** Bir denetim yaklaşana kadar hiçbir şey yapmamak, sonra kanıtı panik içinde toplamak ve kontrollerin denetimler arasında sapmasına izin vermek.
- **Belirli an uyumu.** Denetimi geçmek, sonra kontrolleri gelecek yıla kadar terk etmek.
- **Çerçeve silolari.** Her sertifikayı ayrı yönetmek; kontrolleri bir kez eşlemek yerine emeği çoğaltmak.
- **Uyum tiyatrosu.** Bir denetçiyi tatmin eden ama gerçek hiçbir kontrolü yansıtmayan belgeler ve ekran görüntüleri.
- **Sonradan akla gelen erişilebilirlik.** Erişilebilirliği geç eklemek; zayıf ve uyumsuz sonuçlar ve yasal maruziyet üretmek.
- **Kayıt yükümlülüklerini görmezden gelmek.** Yasal bir talep boşluğu ortaya çıkarana kadar saklama ve FOIA görevlerini ihmal etmek.
- **ATO'yu bir kerelik saymak.** Yetki almak, sonra yetkiyi geçerli tutan sürekli izlemeyi ihmal etmek.
- **Uyumu güvenlikle karıştırmak.** Bir denetimi geçmek güvenli olmakla aynı şey değildir; uyum bir tavan değil, bir tabandır.

## Olgunluk modeli

**Düzey 1, Başlangıç.** Uyum tepkisel ve gelişigüzeldir. Kontrol çerçevesi yoktur. Kanıt, çerçeve çerçeve, süre baskısı altında elle toplanır. Erişilebilirlik ve kayıt yükümlülükleri büyük ölçüde görmezden gelinir. Bulgular ve ramak kala durumlar sıktır ve her denetim yeni bir telaştır.

**Düzey 2, Geliştirme.** Temel çerçeveler belirlenmiştir ve bazı kontroller ve politikalar belgelenmiştir, ama uygulama takımlar arasında tutarsızdır: bir grup erişim gözden geçirmeleri yaparken bir diğeri yapmaz. Denetimler geçilir, ama yalnızca ağır elle emekle. Erişilebilirlik geç düşünülür ve temel kayıt saklama birleşik bir takvim olmadan cepler halinde vardır.

**Düzey 3, Standartlaştırma.** Tek bir kontrol kütüphanesi belgelenmiştir ve başlıca standartlara çapraz eşlenir; böylece bir kontrolü uygulamak birkaçının kanıtını aynı anda sağlar ve takım takım değil kurum genelinde uygulanır. Erişilebilirlik tasarıma ve teste içeri işlenir ve uyum bir VPAT'ta belgelenir. Kayıt yönetimi ve kamu için FOIA hazırlığı kurulmuştur ve yetkilendirmeler bir Sistem Güvenlik Planı ve bir POA&M ile peşinden gidilir.

**Düzey 4, Yönetme.** Uyum programı yalnızca belgelenmekle kalmaz, taban çizgilerine ve hedeflere karşı ölçülür. Kurum kontrol kapsamını, kanıt tazeliğini, kanıt toplama süresini, açık denetim bulgularını ve yaşlarını, istisna sayısını ve son kullanma uyumunu, bir boşluğu gidermenin ortalama süresini ve erişilebilirlik uyum oranlarını izler, sonra bunları önceki dönem taban çizgilerine karşı gözden geçirir. Risk kabullerinin sahipleri, son kullanma tarihleri ve metrikleri vardır; sapma denetimde keşfedilmek yerine panodan tespit edilir ve yeni bir sertifikaya git/gitme kararları ölçülmüş hazırlığa dayanır.

**Düzey 5, Orkestrasyon.** Sürekli uyum kararlı durumdur; otomatik, her zaman açık kanıt ve kontrolleri dağıtım anında uygulayan ve doğrulayan kod olarak uyum korkulukları vardır. Yeni bir sertifika eklemek düşük maliyetlidir, çünkü birleşik çerçeve zaten büyük kısmını kapsar. Sürekli izleme yetkileri kesintisiz sürdürür, uyum iş ve risk planlamasıyla bütünleşir ve kurum düzenlemeler ve tehditler değiştikçe kontrolleri proaktif biçimde uyarlar; her an denetime hazır kalır.

## Tartışma fikirleri

1. Kurumunuz için hangi sertifikalar gerçekten geliri açıyor ve hangi öncelik sırasıyla?
2. Birleşik bir kontrol çapraz eşlemesini kendi bürokratik yüküne dönüşmeden nasıl kurarsınız?
3. Kurumunuzu denetim zamanında değil, her an denetime hazır yapmak için ne gerekir?
4. Çatıştıklarında kayıt saklama yükümlülüklerini gizlilik silme haklarıyla nasıl bağdaştırırsınız?
5. Uyumun, denetçileri tatmin eden ama gerçek hiçbir kontrolü yansıtmayan tiyatroya dönüşmesini nasıl önlersiniz?
6. Kamu işinde yetkilerin asla kesintiye uğramaması için sürekli izlemeyi nasıl sürdürürsünüz?

## Önemli çıkarımlar

- Uyum çoğu zaman faaliyet ruhsatıdır: onsuz bütün pazarlar kapalıdır.
- Birçok standarda çapraz eşlenmiş tek bir birleşik kontrol çerçevesi kurun ve kontrolleri bir kez eşleyin.
- Kamu rejimleri (FISMA, FedRAMP, NIST 800-53/171, CMMC, etki düzeyleri) titiz ve pazarlık edilemezdir.
- Erişilebilirlik (Section 508, ADA, WCAG, EN 301 549) yasal bir yükümlülüktür, isteğe bağlı bir nezaket değil.
- Dönemsel denetim telaşından otomatik kanıtla sürekli uyuma geçin.
- Kayıt yönetimi ve FOIA, özellikle kamuda, gerçek yasal yükümlülükler taşır.
- Bir denetimi geçmek bir tabandır, güvenliğin kanıtı değil; uyum ve güvenlik ilişkili ama ayrıdır.

## Kaynaklar ve ileri okuma

- National Institute of Standards and Technology, *SP 800-53: Security and Privacy Controls*
- National Institute of Standards and Technology, *SP 800-171: Protecting Controlled Unclassified Information*
- National Institute of Standards and Technology, *Cybersecurity Framework (CSF)*
- ISO/IEC 27001, *Information Security Management Systems*
- AICPA, *SOC 2 Trust Services Criteria*
- PCI Security Standards Council, *Payment Card Industry Data Security Standard*
- US General Services Administration, *FedRAMP* documentation; *Section 508* standards
- W3C, *Web Content Accessibility Guidelines (WCAG)*; ETSI *EN 301 549*
