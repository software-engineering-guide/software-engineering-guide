# 12.1 Sözlük

Bu sözlük, kılavuz boyunca kullanılan terimleri ve kısaltmaları tanımlar. Maddeler alfabetik olarak gruplanmıştır ve sıralama İngilizce başlık sözcüklerine göredir. Bir maddenin yaygın bir kısaltması varsa parantez içinde gösterilir; varsa Türkçe karşılık başlık sözcüğünün ardından parantez içinde verilir. Tanımlar bilerek kısa tutulmuştur; ayrıntılı ele alış için ilgili bölüme bakın.

## A

**[ABAC (Attribute-Based Access Control)](https://en.wikipedia.org/wiki/Attribute-based_access_control) (öznitelik tabanlı erişim denetimi)**: Erişimi sabit roller yerine kullanıcının, kaynağın, eylemin ve ortamın değerlendirilen özniteliklerine (örneğin departman, yetki seviyesi, günün saati) göre veren bir yetkilendirme modeli. İnce taneli, ilke güdümlü denetim sunar; bedeli RBAC'ten daha fazla karmaşıklıktır.

**[Accessibility (a11y)](https://en.wikipedia.org/wiki/Computer_accessibility) (erişilebilirlik)**: Yazılımı, engelli kişilerin onu algılayabileceği, anlayabileceği, içinde gezinebileceği ve onunla etkileşebileceği biçimde tasarlama ve inşa etme pratiği. "a11y" sayısal kısaltması, "a" ile "y" arasındaki 11 harfi kısaltır.

**ADR (Architecture Decision Record) (mimari karar kaydı)**: Tek bir önemli mimari ya da teknik kararı, bağlamını, değerlendirilen seçenekleri ve sonuçlarını kaydeden kısa, sürümlenmiş bir belge. ADR'ler, bir sistemin neden bu hâlde olduğuna dair kalıcı ve gözden geçirilebilir bir tarihçe oluşturur.

**Aggregate (küme, bütünleşik nesne)**: Alan odaklı tasarımda (Domain-Driven Design), veri değişiklikleri için tek bir birim olarak ele alınan ve değişmezleri (invariants) uygulatan tek bir varlığın küme kökü olarak görev yaptığı alan nesneleri topluluğu. Kümeler, tutarlılık ve işlem sınırlarını belirler.

**[API (Application Programming Interface)](https://en.wikipedia.org/wiki/API) (uygulama programlama arayüzü)**: Bir yazılım parçasının bir diğerinden hizmet ya da veri istediği tanımlı bir sözleşme. İyi tasarlanmış API'ler uygulama ayrıntısını gizler ve kararlı, sürümlenmiş arayüzler sunar.

**API-first (API öncelikli)**: API sözleşmesinin uygulamadan önce tasarlandığı ve üzerinde uzlaşıldığı bir geliştirme yaklaşımı; böylece tüketiciler ve sağlayıcılar ortak bir belirtim üzerinden paralel çalışabilir.

**arc42**: Yazılım mimarisini belgelemek için açık, şablon tabanlı bir yapı; bağlam, kısıtlar, yapı taşları, çalışma zamanı, dağıtım ve kararları kapsayan on iki bölüm içerir.

**[ARIA (Accessible Rich Internet Applications)](https://en.wikipedia.org/wiki/WAI-ARIA) (erişilebilir zengin internet uygulamaları)**: Dinamik ve özel web bileşenlerini ekran okuyucular gibi yardımcı teknolojiler için anlaşılır kılan rolleri, durumları ve özellikleri tanımlayan bir W3C belirtimi.

**ASR (Architecturally Significant Requirement) (mimari açıdan önemli gereksinim)**: Performans, erişilebilirlik (availability), güvenlik ya da düzenleyici kısıt gibi, mimari üzerinde ölçülebilir ve geniş kapsamlı etkisi olan bir gereksinim. ASR'ler en sonuç doğurucu tasarım kararlarını yönlendirir.

**ASVS (Application Security Verification Standard)**: Güvenli uygulamaları tasarlamak, inşa etmek ve doğrulamak için dereceli bir güvenlik gereksinimleri ve testleri kontrol listesi sunan bir OWASP standardı.

**[Autoscaling](https://en.wikipedia.org/wiki/Autoscaling) (otomatik ölçekleme)**: Çalışan işlem örneklerinin sayısının (ya da boyutunun) yüke göre otomatik ayarlanması; böylece kapasite elle müdahale olmadan talebi izler. Bilinçli kapasite planlamasını tamamlar ama onun yerini almaz.

**[Availability](https://en.wikipedia.org/wiki/Availability) (erişilebilirlik, hizmet sürekliliği)**: Bir sistemin çalışır durumda olduğu ve istekleri karşılayabildiği zaman oranı; çoğunlukla "dokuzlar" ile (örneğin %99,9) ifade edilir. SLO'larda ve SLA'larda kodlanan temel bir güvenilirlik hedefidir.

## B

**Backpressure (geri basınç)**: Yük altındaki bir bileşenin, yukarı akıştaki üreticilere yavaşlamaları için sinyal verdiği, böylece sınırsız kuyrukları ve zincirleme başarısızlığı önleyen bir akış denetimi mekanizması. Güvenilir akış ve ileti güdümlü sistemler için merkezidir.

**[BDD (Behavior-Driven Development)](https://en.wikipedia.org/wiki/Behavior-driven_development) (davranış güdümlü geliştirme)**: Gereksinimleri, aynı zamanda otomatik kabul testi olarak da işleyen somut, insan tarafından okunabilir davranış örnekleriyle (çoğunlukla Given/When/Then biçiminde) ifade eden iş birliğine dayalı bir pratik.

**BFF (Backend for Frontend)**: Belirli bir ön yüz ya da istemci türü için ayrılmış bir arka uç hizmetinin inşa edildiği ve veri şekillendirmeyi ve toplamayı o istemcinin ihtiyaçlarına göre uyarladığı bir mimari kalıp.

**[BI (Business Intelligence) (iş zekâsı)](https://en.wikipedia.org/wiki/Business_intelligence)**: Raporlamayı, panoları ve karar vermeyi desteklemek için iş verilerini toplama, bütünleştirme ve çözümlemeye yönelik araçlar, süreçler ve pratikler.

**Blameless postmortem (suçlamasız olay sonrası inceleme)**: İnsanların sahip oldukları bilgi ve teşvikler göz önüne alındığında makul davrandığı önermesiyle, bireysel kusur yerine sistemik nedenlere ve öğrenmeye odaklanan bir olay incelemesi.

**[Blue-green deployment](https://en.wikipedia.org/wiki/Blue-green_deployment) (mavi-yeşil dağıtım)**: İki özdeş üretim ortamını ("mavi" ve "yeşil") çalıştıran, trafiği birine yönlendirirken diğerini güncelleyen ve neredeyse anında geçişe ve geri almaya imkân veren bir yayın stratejisi.

**[BM25](https://en.wikipedia.org/wiki/Okapi_BM25)**: Tam metin araması için yaygın kullanılan bir sıralama işlevi; bir belgenin bir sorguyla ne kadar iyi eşleştiğini terim sıklığı, ters belge sıklığı ve belge uzunluğu ile puanlar. Birçok arama motorunda sözcüksel sıralamanın varsayılanıdır.

**Bounded context (sınırlı bağlam)**: Alan odaklı tasarımda, belirli bir alan modelinin ve onun her yerde geçerli dilinin (ubiquitous language) tutarlı biçimde uygulandığı açık bir sınır. Büyük bir sistemin farklı bölümlerinde kavramların birbirine karıştırılmasını önler.

**Build cache (derleme önbelleği)**: Daha önce hesaplanmış derleme çıktılarının, onları üreten girdilere göre anahtarlanarak saklandığı bir depo; böylece değişmemiş iş yeniden derlenmek yerine yeniden kullanılır. Paylaşılan uzak bir derleme önbelleği, tüm bir takımın ve onun CI'sının birbirinin sonuçlarını yeniden kullanmasını sağlar.

**[Bus factor](https://en.wikipedia.org/wiki/Bus_factor) (otobüs faktörü)**: Temel bilgi eksikliği yüzünden bir proje durmadan önce kaybedilmesi gereken (mecazen "otobüsün çarptığı") kişi sayısı. Düşük bir otobüs faktörü, yoğunlaşmış ve belgelenmemiş uzmanlığa ve kurumsal riske işaret eder.

## C

**[Cache eviction policy](https://en.wikipedia.org/wiki/Cache_replacement_policies) (önbellek tahliye ilkesi)**: Bir önbelleğin dolduğunda hangi girdiyi çıkaracağına karar vermek için kullandığı kural; örneğin en az yakın zamanda kullanılan (LRU) ya da en az sık kullanılan (LFU). İlke, isabet oranını ve onunla birlikte önbelleğin değerini şekillendirir.

**[Cache invalidation](https://en.wikipedia.org/wiki/Cache_invalidation) (önbellek geçersizleştirme)**: Altta yatan kaynak değiştiğinde önbelleğe alınmış verinin kaldırılması ya da güncellenmesi sorunu; böylece okuyucular bayat değerler görmez. Bilgi işlemin en zor sorunlarından biri olarak ünlüdür.

**[Cache stampede](https://en.wikipedia.org/wiki/Cache_stampede) (önbellek izdihamı)**: Birçok istemcinin aynı anahtar için aynı anda önbelleği ıskalayıp hep birlikte kaynağa yüklenerek onu bunalttığı bir başarısızlık kipi. İstek birleştirme ve kademeli son kullanma bunu önler. Thundering herd olarak da bilinir.

**Canary release (kanarya yayını)**: Yeni bir sürümü önce küçük bir kullanıcı ya da trafik alt kümesine açan, sorunları izleyen ve metrikler sağlıklı kaldıkça yayını kademeli olarak genişleten bir dağıtım tekniği.

**[CAP theorem](https://en.wikipedia.org/wiki/CAP_theorem) (CAP teoremi)**: Dağıtık bir veri deposunun Tutarlılık (Consistency), Erişilebilirlik (Availability) ve Bölünme toleransı (Partition tolerance) üçlüsünden aynı anda en fazla ikisini garanti edebileceğini söyleyen bir ilke; bölünmeler kaçınılmaz olduğundan, tasarımcılar bölünmeler sırasında fiilen tutarlılıkla erişilebilirlik arasında ödünleşim yapar.

**[C4 model](https://en.wikipedia.org/wiki/C4_model) (C4 modeli)**: Yazılım mimarisini dört soyutlama düzeyinde görselleştirmeye yönelik hafif bir yaklaşım: Sistem Bağlamı (System Context), Kapsayıcılar (Containers), Bileşenler (Components) ve Kod (Code).

**[CD (Continuous Delivery / Continuous Deployment)](https://en.wikipedia.org/wiki/Continuous_delivery) (sürekli teslim / sürekli dağıtım)**: Sürekli teslim (Continuous Delivery), yazılımı her an elle onayla dağıtılabilecek yayınlanabilir durumda tutar; sürekli dağıtım (Continuous Deployment) ise iş hattından geçen her değişikliği otomatik olarak yayınlar.

**[CDN (Content Delivery Network)](https://en.wikipedia.org/wiki/Content_delivery_network) (içerik dağıtım ağı)**: İçeriği kullanıcılara yakın önbelleğe alan ve sunan, coğrafi olarak dağıtık bir uç sunucu ağı; gecikmeyi azaltır ve kaynak altyapısının yükünü hafifletir.

**Chain-of-thought prompting (düşünce zinciri istemi)**: Bir dil modelinden nihai cevabı vermeden önce ara akıl yürütme adımlarından geçmesini isteyen bir istem tekniği; çok adımlı problemlerde performansı artırır, bedeli daha uzun ve yavaş çıktıdır.

**[CI (Continuous Integration)](https://en.wikipedia.org/wiki/Continuous_integration) (sürekli entegrasyon)**: Geliştiricilerin değişikliklerini sık sık ortak bir ana hatta birleştirme, her birleştirmeyi entegrasyon sorunlarını erken saptamak için otomatik bir derleme ve test takımıyla doğrulama pratiği.

**[CI/CD](https://en.wikipedia.org/wiki/CI/CD)**: Yazılımı derlemeyi, test etmeyi ve yayınlamayı otomatikleştiren, Sürekli Entegrasyon ile Sürekli Teslim/Dağıtımın birleşik iş hattı.

**CMMC (Cybersecurity Maturity Model Certification)**: Federal sözleşme bilgilerini ve kontrollü sınıflandırılmamış bilgileri işleyen yüklenicilerin siber güvenlik olgunluğunu belgelendiren bir ABD Savunma Bakanlığı programı.

**[Cohesion](https://en.wikipedia.org/wiki/Cohesion_(computer_science)) (bağdaşım)**: Bir modülün içindeki öğelerin birbirine ne ölçüde ait olduğu ve tek, iyi tanımlı bir amaca hizmet ettiği. Düşük bağlaşımla eşleşen yüksek bağdaşım, bakımı kolay tasarımın bir göstergesidir.

**Context window (bağlam penceresi)**: Bir dil modelinin girdisi ve çıktısı dahil olmak üzere aynı anda göz önünde bulundurabildiği, token olarak ölçülen en fazla metin miktarı. İstem ve bağlam tasarımının bilinçli biçimde yönetmesi gereken kıt bir bütçedir.

**[Conway's Law](https://en.wikipedia.org/wiki/Conway's_law) (Conway Yasası)**: Bir sistemin yapısının, onu inşa eden kurumun iletişim yapısını yansıtma eğiliminde olduğu gözlemi. "Ters Conway manevrası", istenen mimariyi üretmek için takımları bilerek şekillendirir.

**Core Web Vitals**: Google tarafından tanımlanan, yüklemeyi, etkileşimi ve görsel kararlılığı ölçen kullanıcı merkezli bir web performansı metrikleri kümesi (Largest Contentful Paint, Interaction to Next Paint ve Cumulative Layout Shift gibi).

**[Cost of delay](https://en.wikipedia.org/wiki/Cost_of_delay) (gecikme maliyeti)**: Bir şeyin henüz bitmemiş olmasının, birim zaman başına kaybedilen değer olarak ifade edilen ekonomik maliyeti. Bunu açık hâle getirmek önceliklendirmeyi görüşten aritmetiğe çevirir ve ağırlıklı en kısa iş önce (weighted shortest job first) gibi sıralama kurallarının temelini oluşturur.

**[Coupling](https://en.wikipedia.org/wiki/Coupling_(computer_programming)) (bağlaşım)**: Modüller ya da hizmetler arasındaki karşılıklı bağımlılık derecesi. Gevşek bağlaşım, değişimin dalga etkisini sınırlar ve iyi mimarinin merkezi bir hedefidir.

**CQRS (Command Query Responsibility Segregation)**: Durumu değiştirmek için kullanılan modeli (komutlar) durumu okumak için kullanılan modelden (sorgular) ayıran, her birinin bağımsız olarak iyileştirilmesine ve ölçeklenmesine imkân veren bir kalıp.

**[CVE (Common Vulnerabilities and Exposures)](https://en.wikipedia.org/wiki/Common_Vulnerabilities_and_Exposures)**: Açıklanmış güvenlik açıklarının, her birine benzersiz bir tanımlayıcı atanmış olarak tutulduğu herkese açık bir katalog; böylece araçlar ve takımlar aynı kusura belirsizlik olmadan başvurabilir.

**CWV**: Bkz. Core Web Vitals.

## D

**[DAST (Dynamic Application Security Testing)](https://en.wikipedia.org/wiki/Dynamic_application_security_testing) (dinamik uygulama güvenlik testi)**: Çalışan bir uygulamayı kaynak koda erişmeden dışarıdan yoklayarak çalışma zamanında ortaya çıkan açıkları bulan güvenlik testi.

**Data-ink ratio (veri-mürekkep oranı)**: Edward Tufte'ye ait, bir grafiğin mürekkebinin çoğunu verinin kendisine, azını süslemeye harcaması gerektiğini; bilgi vermeyen kılavuz çizgilerini, kenarlıkları ve grafik süslerini (chartjunk) kaldırmayı savunan bir ilke.

**[Data mesh](https://en.wikipedia.org/wiki/Data_mesh) (veri ağı)**: Veriyi alan takımlarının sahip olduğu bir ürün olarak ele alan, self-servis platform altyapısı ve federe yönetişimle desteklenen, merkezsiz bir veri mimarisi ve işletim modeli.

**[Data visualization](https://en.wikipedia.org/wiki/Data_and_information_visualization) (veri görselleştirme)**: Verinin görsel biçimde (konum, uzunluk, renk ve benzeri) kodlanması pratiği; böylece örüntüler, karşılaştırmalar ve eğilimler algılanabilir olur ve kararlar daha iyi bilgilendirilir.

**[DDD (Domain-Driven Design)](https://en.wikipedia.org/wiki/Domain-driven_design) (alan odaklı tasarım)**: Modeli iş alanı etrafında merkezleyen; ortak bir her yerde geçerli dil (ubiquitous language), sınırlı bağlamlar ve varlıklar, değer nesneleri ve kümeler gibi yapı taşları kullanan bir yazılım tasarımı yaklaşımı.

**Design tokens (tasarım token'ları)**: Tasarım kararlarını kodlayan, adlandırılmış ve platformdan bağımsız değerler (renkler, boşluklar, tipografi ve benzeri); böylece bir tasarım sistemi ve birden çok ürün arasında tutarlı biçimde paylaşılabilir.

**DevEx / DevX (Developer Experience) (geliştirici deneyimi)**: Bir geliştiricinin araçlar, platformlar ve süreçlerle gündelik etkileşiminin genel kalitesi; sürtünmeyi, geri bildirim hızını ve bilişsel yükü kapsar.

**[DevOps](https://en.wikipedia.org/wiki/DevOps)**: Teslim döngülerini kısaltmak, dağıtım sıklığını artırmak ve güvenilirliği otomasyon ve ortak sahiplenmeyle iyileştirmek için yazılım geliştirme ile operasyonu birleştiren bir kültür ve pratikler kümesi.

**DORA (DevOps Research and Assessment)**: Yazılım teslim performansını kıyaslamak için kullanılan bir araştırma programı ve onun yaygın kullanılan dört teslim metriği (dağıtım sıklığı, değişiklikler için hazırlık süresi, değişiklik başarısızlık oranı ve hizmeti geri getirme süresi).

**DPIA (Data Protection Impact Assessment) (veri koruma etki değerlendirmesi)**: GDPR kapsamında yüksek riskli işleme için gerekli olan, bir proje ilerlemeden önce gizlilik risklerini belirleyip azaltan yapılandırılmış bir değerlendirme.

**Drift (configuration) (yapılandırma kayması)**: Bir sistemin gerçek durumunun bildirilen ya da amaçlanan durumundan, genellikle elle yapılan değişikliklerle, giderek sapması; kod olarak altyapı ve GitOps bunu saptamayı ve düzeltmeyi hedefler.

**Drift (model) (model kayması)**: Makine öğrenmesinde, girdi verisinin istatistiksel özellikleri (veri kayması) ya da modellenen ilişki (kavram kayması) değiştikçe model performansının zamanla bozulması.

**[DR (Disaster Recovery)](https://en.wikipedia.org/wiki/Disaster_recovery) (felaket kurtarma)**: Büyük bir yıkıcı olaydan sonra hizmeti ve veriyi geri getirmek için strateji, prosedürler ve altyapı; tipik olarak RTO ve RPO hedefleriyle yönetilir.

**[DRY (Don't Repeat Yourself)](https://en.wikipedia.org/wiki/Don't_repeat_yourself) (kendini tekrar etme)**: Her bilgi parçasının tek ve yetkili bir temsili olması gerektiğini söyleyen, tekrarı ve tutarsız güncelleme riskini azaltan bir tasarım ilkesi.

## E

**East-west traffic (doğu-batı trafiği)**: Bir sistemin ya da veri merkezinin içindeki hizmetler arasındaki ağ trafiği; sistem ile dış istemciler arasındaki kuzey-güney trafiğinin karşıtı. Doğu-batı trafiğini tipik olarak bir hizmet ağı (service mesh) yönetir.

**[Edge computing](https://en.wikipedia.org/wiki/Edge_computing) (uç bilişim)**: Gecikmeyi ve bant genişliğini azaltmak için hesaplama ve depolamanın merkezi bir yerde değil, verinin üretildiği ya da tüketildiği yere yakın çalıştırılması. İçerik dağıtım ağları erken ve yaygın bir biçimidir.

**[Elasticity](https://en.wikipedia.org/wiki/Elasticity_(cloud_computing)) (esneklik)**: Bir sistemin değişen talebe yanıt olarak kaynakları otomatik edinip bırakabilme yeteneği; böylece kapasite yükü yakından izler.

**[ELT (Extract, Load, Transform)](https://en.wikipedia.org/wiki/Extract,_load,_transform)**: Ham veriyi önce hedef depoya yükleyen ve dönüşümü orada yapan, modern ambarların ve göl evlerinin (lakehouse) ölçeğinden yararlanan bir veri entegrasyonu kalıbı.

**[Embedding](https://en.wikipedia.org/wiki/Word_embedding) (gömme)**: Metnin, görüntülerin ya da diğer verilerin, benzer öğelerin birbirine yakın durması için konumlandırılmış yoğun bir sayısal vektör olarak temsili. Gömmeler anlamsal ve vektör aramasına ve geri getirme destekli üretime (retrieval-augmented generation) güç verir.

**[EN 301 549](https://en.wikipedia.org/wiki/EN_301_549)**: BİT ürünleri ve hizmetleri için erişilebilirlik gereksinimlerini belirleyen, AB genelinde kamu alımlarında başvurulan ve WCAG ile uyumlu Avrupa standardı.

**Error budget (hata bütçesi)**: Bir dönem boyunca bir SLO'nun izin verdiği kabul edilebilir güvenilmezlik miktarı; tükendiğinde takımlar yeni özellikler yerine güvenilirlik çalışmasına öncelik verir. Hız ile kararlılık arasındaki gerilimi uzlaştırır.

**[ETL (Extract, Transform, Load)](https://en.wikipedia.org/wiki/Extract,_transform,_load)**: Veriyi kaynaklardan çıkaran, hedef biçime dönüştüren ve bir ambar gibi bir hedefe yükleyen bir veri entegrasyonu kalıbı.

**[EU AI Act](https://en.wikipedia.org/wiki/Artificial_Intelligence_Act) (AB Yapay Zekâ Yasası)**: Yapay zekâ sistemlerini riske göre sınıflandıran ve buna göre yükümlülükler getiren, bazı kullanımları yasaklayan ve yüksek riskli sistemleri sıkı biçimde düzenleyen Avrupa Birliği düzenlemesi.

**[Eventual consistency](https://en.wikipedia.org/wiki/Eventual_consistency) (nihai tutarlılık)**: Dağıtık sistemlerde, kopyaların geçici olarak ayrışabildiği ama güncellemeler yayılmayı bıraktığında aynı duruma yakınsadığı bir tutarlılık modeli.

## F

**[Feature flag / feature toggle](https://en.wikipedia.org/wiki/Feature_toggle) (özellik bayrağı / özellik anahtarı)**: Yeniden dağıtım yapmadan işlevselliği çalışma zamanında açıp kapatma mekanizması; kademeli yayınlar, deneyler ve operasyonel denetim için kullanılır.

**Feature store (özellik deposu)**: Makine öğrenmesi özelliklerini hem eğitim hem çıkarım için tutarlı biçimde tanımlayan, saklayan ve sunan merkezi bir sistem; tekrarı ve eğitim/sunum sapmasını (training/serving skew) azaltır.

**[FedRAMP (Federal Risk and Authorization Management Program)](https://en.wikipedia.org/wiki/FedRAMP)**: Federal kurumların kullandığı bulut hizmetleri için güvenlik değerlendirmesini, yetkilendirmeyi ve sürekli izlemeyi standartlaştıran bir ABD hükümeti programı.

**Few-shot prompting (az örnekli istem)**: Bir dil modeline, istenen görevi ve çıktı biçimini göstermek için istemde bir avuç çalışılmış örnek verme; örneksiz talimat veren sıfır örnekli (zero-shot) istemin karşıtıdır.

**FinOps**: Değişken bulut harcamasına mali sorumluluk getiren, mühendislik, finans ve iş takımlarına maliyetin ve değerin ortak sahipliğini veren bir disiplin ve kültürel pratik.

**[FISMA (Federal Information Security Modernization Act)](https://en.wikipedia.org/wiki/Federal_Information_Security_Management_Act)**: Federal kurumların bilgi güvenliği programlarını uygulamasını, belgelemesini ve izlemesini zorunlu kılan, büyük ölçüde NIST kılavuzluğuyla işletilen ABD mevzuatı.

**Flow efficiency (akış verimliliği)**: Bir iş öğesinin toplam hazırlık süresinin, beklemek yerine etkin biçimde üzerinde çalışılarak geçirdiği oranı; değer katan sürenin toplam hazırlık süresine bölünmesiyle hesaplanır. Çoğu sistemde şaşırtıcı biçimde düşüktür, çoğunlukla yüzde 15'in altındadır.

**Four-eyes principle (dört göz ilkesi)**: Önemli bir eylemin en az iki kişi tarafından gözden geçirilmesini ya da onaylanmasını gerektiren, hata ya da kötüye kullanım ihtimalini azaltan bir denetim.

**[Fuzz testing (fuzzing)](https://en.wikipedia.org/wiki/Fuzzing) (fuzz testi)**: Çökmeleri, güvenlik kusurlarını ve uç durum hatalarını ortaya çıkarmak için bir programa bozuk, rastgele ya da beklenmedik girdiler besleyen otomatik bir test tekniği.

## G

**[GDPR (General Data Protection Regulation)](https://en.wikipedia.org/wiki/General_Data_Protection_Regulation) (Genel Veri Koruma Tüzüğü)**: Kişisel verilerin işlenmesini düzenleyen, bireylere haklar tanıyan ve veri sorumlularına ile işleyenlere yükümlülükler getiren, uyumsuzluk için önemli yaptırımlar içeren Avrupa Birliği düzenlemesi.

**GitOps**: Bildirimsel altyapı ve uygulamalar için tek doğruluk kaynağı olarak Git'i kullanan, otomasyonun canlı sistemi sürekli olarak işlenmiş (committed) duruma uzlaştırdığı bir işletim modeli.

**Golden path / paved road (altın yol / döşenmiş yol)**: Bir kurum içinde yazılım inşa etmenin ve yayınlamanın, iyi desteklenen, görüş sahibi varsayılan bir yolu; güvenli, uyumlu ve güvenilir seçimi en kolay seçim yapmak üzere tasarlanır.

**Golden record (altın kayıt)**: Ana veri yönetiminde, bir iş varlığının (örneğin bir müşterinin) birden çok kaynak sistemden eşleştirme ve hayatta kalma kurallarıyla derlenen tek, uzlaştırılmış, yetkili sürümü.

**[Gradual typing](https://en.wikipedia.org/wiki/Gradual_typing) (kademeli tiplendirme)**: Statik ve dinamik tiplemenin tek bir kod tabanında bir arada bulunmasına izin veren bir tip sistemi yaklaşımı; böylece dinamik tipli bir programa tipler aşamalı olarak eklenebilir. Tip ipuçları ve isteğe bağlı tip denetleyicileri yaygın örneklerdir.

**[GraphQL](https://en.wikipedia.org/wiki/GraphQL)**: İstemcilerin, güçlü tipli bir şema kullanarak tam olarak ihtiyaç duydukları veriyi tek bir çağrıyla istemesini sağlayan bir API sorgu dili ve çalışma zamanı.

**[gRPC](https://en.wikipedia.org/wiki/gRPC)**: Verimli hizmetten hizmete iletişim için HTTP/2'yi ve tipik olarak Protocol Buffers'ı kullanan, yüksek performanslı, sözleşme öncelikli bir uzak yordam çağrısı çatısı.

## H

**Hermetic build (hermetik derleme)**: Yalnızca açıkça bildirilmiş girdilere bağlı olan ve konak ortamdan yalıtılmış bir derleme; böylece her yerde aynı çıktıyı üretir. Hermetiklik, yeniden üretilebilir derlemelerin ve güvenilir önbelleklemenin temelidir.

**[HSM (Hardware Security Module)](https://en.wikipedia.org/wiki/Hardware_security_module) (donanım güvenlik modülü)**: Kriptografik anahtarları üreten, saklayan ve kullanan, kurcalamaya dayanıklı bir donanım aygıtı; yalnızca yazılıma dayalı yaklaşımlardan daha güçlü anahtar koruması sağlar.

**[HIPAA (Health Insurance Portability and Accountability Act)](https://en.wikipedia.org/wiki/Health_Insurance_Portability_and_Accountability_Act)**: Diğer konuların yanı sıra korunan sağlık bilgilerinin (PHI) güvence altına alınmasına ilişkin gereksinimleri belirleyen ve kullanımını ve ifşasını düzenleyen ABD mevzuatı.

**Horizontal scaling (yatay ölçekleme)**: Tek bir düğümü daha güçlü yapmak yerine daha fazla örnek ya da düğüm ekleyerek ("dışa ölçekleme") kapasiteyi artırma. Büyük ölçekli ve dayanıklı mimarilerin çoğunun temelidir.

## I

**[IaC (Infrastructure as Code) (kod olarak altyapı)](https://en.wikipedia.org/wiki/Infrastructure_as_code)**: Altyapıyı elle yapılan süreçler yerine makine tarafından okunabilir, sürüm denetimli yapılandırmayla tanımlama ve hazırlama pratiği; tekrarlanabilirliği ve gözden geçirmeyi mümkün kılar.

**[IAM (Identity and Access Management)](https://en.wikipedia.org/wiki/Identity_management) (kimlik ve erişim yönetimi)**: Doğru kimliklerin doğru kaynaklara doğru zamanlarda doğru erişime sahip olmasını güvence altına alan ilkeler ve teknolojiler çerçevesi.

**IDP / IdP**: "IDP" genellikle Dahili Geliştirici Platformu (Internal Developer Platform) anlamına gelir; ürün takımları için altyapıyı soyutlayan self-servis araç katmanıdır. "IdP" ise kullanıcıları doğrulayan ve doğrulama beyanları (assertions) düzenleyen bir hizmet olan Kimlik Sağlayıcısı (Identity Provider) anlamına gelir. İkisini bağlam ayırt eder.

**[Idempotency](https://en.wikipedia.org/wiki/Idempotence) (eş güçlülük)**: Bir işlemi birçok kez yapmanın onu bir kez yapmakla aynı etkiyi doğurduğu özellik; dağıtık sistemlerde ve API'lerde güvenli yeniden denemeler için vazgeçilmezdir.

**[i18n (Internationalization)](https://en.wikipedia.org/wiki/Internationalization_and_localization) (uluslararasılaştırma)**: Yazılımı, mühendislik değişikliği gerektirmeden farklı dillere, bölgelere ve kültürel geleneklere uyarlanabilecek biçimde tasarlama ve inşa etme. Sayısal kısaltma, "i" ile "n" arasındaki 18 harfi kısaltır.

**Immutable artefact (değişmez yapıt)**: Üretilip sürümlendikten sonra asla değiştirilmeyen bir derleme çıktısı; her değişiklik yeni bir sürüm doğurur. Değişmezlik yayınları yeniden üretilebilir kılar ve bir kez derleyip aynı yapıtı ortamlar arasında yükseltmenizi sağlar.

**InnerSource**: Açık kaynak geliştirme pratiklerinin (şeffaflık, paylaşılan depolar ve takımlar arası katkı) tek bir kurumun içinde uygulanması.

**IaC drift**: Bkz. Drift (configuration).

**[Inverted index](https://en.wikipedia.org/wiki/Inverted_index) (ters dizin)**: Bir arama motorunun çekirdek veri yapısı; her terimi onu içeren belgelerin listesine eşler, böylece sorgular her belgeyi taramadan yanıtlanabilir.

**[ISO/IEC 27001](https://en.wikipedia.org/wiki/ISO/IEC_27001)**: Bir Bilgi Güvenliği Yönetim Sistemi (ISMS) için gereksinimleri belirleyen, bilgi güvenliği riskini yönetmek için belgelendirilebilir bir çerçeve sunan uluslararası standart.

**ISO/IEC 42001**: Bir Yapay Zekâ Yönetim Sistemi için gereksinimleri belirleyen, kurumlara yapay zekânın geliştirilmesini ve kullanımını sorumlu biçimde yönetmek için belgelendirilebilir bir çerçeve sunan uluslararası standart.

## J

**[JWT (JSON Web Token)](https://en.wikipedia.org/wiki/JSON_Web_Token)**: Taraflar arasında hak iddialarını (claims) iletmek için kullanılan, kompakt, imzalı (ve isteğe bağlı olarak şifreli) bir token biçimi; web ve API sistemlerinde yaygın olarak kimlik doğrulama ve yetkilendirme için kullanılır.

## K

**[Kanban](https://en.wikipedia.org/wiki/Kanban_(development))**: İşi bir panoda görselleştiren, devam eden işi sınırlayan ve verimi ile öngörülebilirliği artırmak için akışı yöneten yalın bir iş akışı yöntemi.

**[KISS (Keep It Simple, Stupid)](https://en.wikipedia.org/wiki/KISS_principle) (basit tut)**: Gereksiz karmaşıklığın maliyeti ve riski artırdığı gerekçesiyle, ihtiyacı karşılayan en basit çözümü tercih eden bir tasarım ilkesi.

**KMS (Key Management Service) (anahtar yönetim hizmeti)**: Kriptografik anahtarları oluşturan, saklayan, döndüren ve erişimlerini denetleyen, çoğunlukla donanım güvenlik modülleriyle desteklenen bir sistem.

**[KPI (Key Performance Indicator)](https://en.wikipedia.org/wiki/Performance_indicator) (temel performans göstergesi)**: Belirli bir iş ya da operasyonel hedefe doğru ilerlemeyi izlemek için kullanılan nicelleştirilebilir bir ölçü.

## L

**Lakehouse (göl evi)**: Bir veri gölünün düşük maliyetli ve esnek depolamasını, bir veri ambarının yönetim, işlem ve performans özellikleriyle birleştiren bir veri mimarisi.

**[Lead time](https://en.wikipedia.org/wiki/Lead_time) (hazırlık süresi)**: Bir değişikliğin istenmesinden (ya da işlenmesinden) üretime teslim edilmesine kadar geçen süre; temel bir DORA teslim metriğidir.

**[Least privilege](https://en.wikipedia.org/wiki/Principle_of_least_privilege) (en az ayrıcalık)**: Her kullanıcıya, sürece ya da sisteme yalnızca işlevini yerine getirmek için gereken asgari erişimi veren, ele geçirilmenin ya da hatanın verdiği zararı sınırlayan bir güvenlik ilkesi.

**[Little's Law](https://en.wikipedia.org/wiki/Little's_law) (Little Yasası)**: Kuyruk kuramından, kararlı bir sistemdeki ortalama öğe sayısının ortalama varış hızı ile her öğenin sistemde geçirdiği ortalama sürenin çarpımına eşit olduğunu söyleyen bir sonuç. Devam eden işi, verimi ve hazırlık süresini birbirine bağlar.

**[LLM (Large Language Model)](https://en.wikipedia.org/wiki/Large_language_model) (büyük dil modeli)**: Dili tahmin etmek ve üretmek için çok büyük metin derlemleri üzerinde eğitilmiş, özetleme, çeviri ve kod üretimi gibi görevlere muktedir bir makine öğrenmesi modeli.

**[l10n (Localization)](https://en.wikipedia.org/wiki/Language_localisation) (yerelleştirme)**: Uluslararasılaştırılmış yazılımı çeviri, biçimlendirme ve kültürel gelenekler dahil belirli bir yerel ayara uyarlama. Sayısal kısaltma, "l" ile "n" arasındaki 10 harfi kısaltır.

## M

**[MDM (Master Data Management)](https://en.wikipedia.org/wiki/Master_data_management) (ana veri yönetimi)**: Çekirdek iş varlıklarının (örneğin müşterilerin ya da ürünlerin) sistemler arasında tek, yetkili ve tutarlı bir görünümünü oluşturma ve sürdürme disiplini ve araçları.

**MITRE ATT&CK**: Gerçek dünyadaki saldırgan taktiklerinin ve tekniklerinin, kırmızı takım tatbikatlarını planlamak, tespit mühendisliğine yön vermek ve tehditleri ortak bir sözcük dağarcığıyla anlatmak için yaygın kullanılan, derlenmiş, herkese açık bilgi tabanı.

**Mean Time to Recovery (MTTR) (ortalama kurtarma süresi)**: Bir başarısızlıktan sonra hizmeti geri getirmek için geçen ortalama süre; yaygın bir güvenilirlik ve olay yönetimi metriğidir.

**[Mob programming](https://en.wikipedia.org/wiki/Mob_programming) (sürü programlama)**: Bütün bir takımın, bilgiyi paylaşmak ve kararları ortaklaşa vermek için kimin yazacağını dönüşümlü olarak değiştirerek aynı bilgisayarda aynı görev üzerinde birlikte çalıştığı bir pratik.

**[MLOps (Machine Learning Operations)](https://en.wikipedia.org/wiki/MLOps) (makine öğrenmesi operasyonları)**: Makine öğrenmesi modellerini üretimde güvenilir ve verimli biçimde dağıtan, izleyen ve sürdüren, DevOps ilkelerini ML yaşam döngüsüne genişleten pratikler kümesi.

**[Monorepo](https://en.wikipedia.org/wiki/Monorepo) (tek depo)**: Birçok projenin ya da tüm kurumun kodunu tutan tek bir sürüm denetimi deposu; ortak araçlamayı ve projeler arası atomik değişiklikleri mümkün kılar, bedeli özelleşmiş ölçekleme araçlarıdır.

**mTLS (mutual TLS) (karşılıklı TLS)**: Her iki tarafın sertifika sunduğu ve doğruladığı, böylece her birinin diğerini doğruladığı bir Transport Layer Security yapılandırması. Hizmet ağında (service mesh) ve sıfır güven ağlarında hizmetten hizmete trafik için bir varsayılandır. Ayrıca bkz. [mutual authentication](https://en.wikipedia.org/wiki/Mutual_authentication).

**[Mutation testing](https://en.wikipedia.org/wiki/Mutation_testing) (mutasyon testi)**: Test takımının onları saptayıp saptamadığını denetlemek için koda bilerek küçük kusurlar ("mutantlar") yerleştiren, takımın gerçek etkinliğini ölçen bir teknik.

## N

**[NDCG (Normalized Discounted Cumulative Gain)](https://en.wikipedia.org/wiki/Discounted_cumulative_gain)**: Yüksek düzeyde ilgili sonuçları sonuç listesinin tepesine yakın yerleştirmeyi ödüllendiren, puanların sorgular arasında karşılaştırılabilir olması için normalleştirilmiş bir sıralama kalitesi metriği. Arama ilgililiği değerlendirmesinin temel taşıdır.

**[NIST (National Institute of Standards and Technology)](https://en.wikipedia.org/wiki/National_Institute_of_Standards_and_Technology)**: Özel Yayınları ve çerçeveleri siber güvenlik, gizlilik ve yapay zekâ için yaygın biçimde başvurulan standartlar olan bir ABD federal kurumu.

**NIST AI RMF (AI Risk Management Framework)**: Yapay zekâ sistemleriyle ilişkili riskleri yaşam döngüleri boyunca belirlemek, değerlendirmek ve yönetmek için, Govern, Map, Measure ve Manage işlevleri etrafında örgütlenmiş, gönüllü bir NIST çerçevesi.

**[NIST SP 800-53](https://en.wikipedia.org/wiki/NIST_Special_Publication_800-53)**: Federal bilgi sistemleri için güvenlik ve gizlilik denetimlerinin bir NIST kataloğu; devletin çok ötesinde de bir temel çizgi olarak yaygın kullanılır.

**NIST SP 800-171**: Federal olmayan sistemlerde kontrollü sınıflandırılmamış bilgilerin (CUI) korunması için gereksinimleri belirleyen, savunma yüklenicisi uyumluluğunun merkezinde yer alan bir NIST yayını.

**[NFR (Non-Functional Requirement)](https://en.wikipedia.org/wiki/Non-functional_requirement) (işlevsel olmayan gereksinim)**: Bir sistemin hangi işlevleri yerine getirdiğini değil, nasıl davranması gerektiğini (performans, güvenlik, güvenilirlik ya da kullanılabilirlik gibi niteliklerini) tanımlayan bir gereksinim.

**North-south traffic (kuzey-güney trafiği)**: Bir sistem ile dış istemcileri arasındaki (veri merkezine ya da kümeye girip çıkan) ağ trafiği; iç hizmetler arasındaki doğu-batı trafiğinin karşıtı. Kuzey-güney trafiğini tipik olarak bir API ağ geçidi yönetir.

## O

**Observability (gözlemlenebilirlik)**: Bir sistemin iç durumunun dış çıktılarından ne ölçüde çıkarsanabildiği; tipik olarak telemetriyle elde edilir: metrikler, günlükler ve izler.

**[OKR (Objectives and Key Results)](https://en.wikipedia.org/wiki/OKR) (hedefler ve anahtar sonuçlar)**: Bir kurumu hizalamak ve odaklamak için niteliksel bir hedefi birkaç ölçülebilir anahtar sonuçla eşleştiren bir hedef belirleme çerçevesi.

**OpenTelemetry (OTel)**: Yazılımdan telemetri verisi (izler, metrikler ve günlükler) üretmek, toplamak ve dışa aktarmak için, satıcıdan bağımsız, açık bir standart ve araç kümesi.

**OPA (Open Policy Agent)**: Yığın genelinde yetkilendirme ve yapılandırma kurallarını uygulatmak için (Rego dilinde yazılmış) ilkeleri değerlendiren, ilkeyi kod olarak (policy as code) mümkün kılan, açık kaynaklı, genel amaçlı bir ilke motoru.

**OSPO (Open Source Program Office) (açık kaynak program ofisi)**: Açık kaynak stratejisini, yönetişimi, uyumluluğu ve topluluk katılımını koordine eden, hem tüketimi hem katkıyı yöneten bir kurumsal işlev.

**[OWASP (Open Worldwide Application Security Project)](https://en.wikipedia.org/wiki/OWASP)**: OWASP Top Ten ve ASVS dahil, yaygın kullanılan ve serbestçe erişilebilen uygulama güvenliği kaynakları üreten kâr amacı gütmeyen bir topluluk.

## P

**[PACELC](https://en.wikipedia.org/wiki/PACELC_theorem)**: CAP teoreminin, bir Bölünme (Partition) varsa sistemin Erişilebilirlik (Availability) ile Tutarlılık (Consistency) arasında, yoksa (Else, normal işleyişte) Gecikme (Latency) ile Tutarlılık arasında ödünleşim yaptığını söyleyen bir uzantısı.

**[PCI DSS (Payment Card Industry Data Security Standard)](https://en.wikipedia.org/wiki/Payment_Card_Industry_Data_Security_Standard)**: Ödeme kartı sektörü tarafından sürdürülen, kart sahibi verisini saklayan, işleyen ya da ileten kurumlar için gereksinimleri belirleyen bir güvenlik standardı.

**[Penetration testing](https://en.wikipedia.org/wiki/Penetration_test) (sızma testi)**: Gerçek saldırganlardan önce sömürülebilir açıkları bulmak ve göstermek için yetkin test uzmanlarının bir sisteme yetkili, simüle edilmiş saldırısı; öncelikli, eyleme dönüştürülebilir bulgular olarak teslim edilir.

**[PII (Personally Identifiable Information)](https://en.wikipedia.org/wiki/Personal_data) (kişisel olarak tanımlanabilir bilgi)**: Belirli bir bireyi tek başına ya da başka verilerle birlikte tanımlayabilen bilgi; ele alınışı gizlilik yasaları ve iç ilkelerle yönetilir.

**Platform engineering (platform mühendisliği)**: Bilişsel yükü azaltan ve ürün takımlarını hızlandıran dahili self-servis platformları ve altın yolları inşa etme ve işletme disiplini.

**POUR**: Web İçeriği Erişilebilirlik Yönergeleri'nin dört yol gösterici ilkesi: içerik Algılanabilir (Perceivable), İşletilebilir (Operable), Anlaşılabilir (Understandable) ve Sağlam (Robust) olmalıdır.

**Production readiness review (üretim hazırlığı incelemesi)**: Bir hizmet canlıya çıkmadan ya da nöbet sahipliğini üstlenmeden önce yürütülen, gözlemlenebilirlik, güvenilirlik, güvenlik, işletim kılavuzları ve operasyonel destek standartlarını karşıladığını doğrulayan yapılandırılmış bir denetim.

**[Prompt engineering](https://en.wikipedia.org/wiki/Prompt_engineering) (istem mühendisliği)**: Bir dil modeline verilen talimatları, bağlamı ve örnekleri, güvenilir ve yüksek kaliteli çıktı almak için tasarlama ve iyileştirme pratiği; deneme yanılma yerine sürümlenmiş, test edilmiş bir mühendislik disiplini olarak ele alınır.

**[Prompt injection](https://en.wikipedia.org/wiki/Prompt_injection) (istem enjeksiyonu)**: Özenle hazırlanmış girdinin bir dil modelinin amaçlanan talimatlarını yok sayıp saldırganın talimatlarını izlemesine yol açtığı, enjeksiyon kusurlarının yapay zekâ çağındaki karşılığı bir saldırı. LLM uygulamalarının merkezi bir güvenlik riskidir.

**Property-based testing (özellik tabanlı test)**: Yalnızca elle seçilmiş örneklere güvenmek yerine, belirtilen özelliklerin otomatik üretilen birçok girdi üzerinde geçerli olduğunu denetleyen bir test tekniği.

**Pull request (PR) / merge request (MR) (çekme isteği / birleştirme isteği)**: Paylaşılan bir dala birleştirilmeden önce gözden geçirme ve tartışma için sunulan önerilmiş bir değişiklikler kümesi; çoğu iş akışında kod incelemenin temel birimidir.

**Purple team (mor takım)**: Saldırgan (kırmızı) ve savunmacı (mavi) güvenlik takımlarının gerçek zamanlı olarak birlikte çalıştığı, saldırıların ve onları yakalamak için tasarlanan tespitlerin birbirine karşı ayarlandığı iş birliğine dayalı bir tatbikat.

## Q

**Quality gate (kalite kapısı)**: Bir değişikliğin ilerleyebilmesi için geçilmesi gereken (örneğin kapsama, güvenlik ya da performans eşiklerini karşılamak gibi), bir iş hattındaki otomatik denetim noktası.

**[Quorum](https://en.wikipedia.org/wiki/Quorum_(distributed_computing)) (çoğunluk, yeter sayı)**: Dağıtık sistemlerde, bir işlemin (okuma ya da yazma gibi) başarılı sayılması için hemfikir olması gereken asgari düğüm sayısı; başarısızlıklara rağmen tutarlılığı sürdürmek için kullanılır.

## R

**[RACI](https://en.wikipedia.org/wiki/Responsibility_assignment_matrix)**: Bir görevdeki ya da kararlardaki her katılımcıyı Sorumlu (Responsible), Hesap Verebilir (Accountable), Danışılan (Consulted) ya da Bilgilendirilen (Informed) olarak etiketleyen bir sorumluluk atama modeli.

**[RAG (Retrieval-Augmented Generation)](https://en.wikipedia.org/wiki/Retrieval-augmented_generation) (geri getirme destekli üretim)**: Bir dil modelinin çıktısını, önce ilgili belgeleri ya da verileri geri getirip bağlam olarak sunarak temellendiren, doğruluğu artıran ve halüsinasyonu azaltan bir teknik.

**[RBAC (Role-Based Access Control)](https://en.wikipedia.org/wiki/Role-based_access_control) (rol tabanlı erişim denetimi)**: İzinleri rollere ve rolleri kullanıcılara atayan, erişimi rol düzeyinde yöneterek yönetimi basitleştiren bir yetkilendirme modeli.

**[Red team](https://en.wikipedia.org/wiki/Red_team) (kırmızı takım)**: Gerçekçi bir düşmanı, çoğunlukla savunucuları uyarmadan tüm bir kuruma karşı taklit eden, yalnızca açıkları sıralamak yerine tespiti ve müdahaleyi sınayan bir grup. Mavi (savunmacı) takımla karşılaştırın.

**[Reference data](https://en.wikipedia.org/wiki/Reference_data) (referans verisi)**: Ülke kodları, para birimleri ve durum değerleri gibi diğer verileri sınıflandırmak için kullanılan, kontrollü, yavaş değişen kod listeleri ve sınıflandırmalar. Bunu paylaşılan, sürümlenmiş bir sözcük dağarcığı olarak yönetmek sistemleri tutarlı tutar.

**Rego**: Open Policy Agent'ın yetkilendirme ve yapılandırma kararları için kuralları ifade etmekte kullandığı bildirimsel ilke dili.

**[REST (Representational State Transfer)](https://en.wikipedia.org/wiki/REST)**: Adreslenebilir kaynaklar üzerinde HTTP üzerinden durumsuz işlemler kullanan, sadeliği ve geniş araç desteğiyle değerli görülen, ağa bağlı uygulamalar için bir mimari üslup.

**[Reverse proxy](https://en.wikipedia.org/wiki/Reverse_proxy) (ters vekil)**: Bir ya da daha fazla arka uç hizmetinin önünde duran ve istemci isteklerini onlara ileten, yaygın olarak TLS sonlandırma, yük dengeleme, önbellekleme ve tek bir giriş noktası sağlayan bir sunucu.

**[RFC (Request for Comments)](https://en.wikipedia.org/wiki/Request_for_Comments) (yorum talebi)**: Önemli bir teknik karardan ya da değişiklikten önce geri bildirim için dolaştırılan, şeffaflığı ve ortak sahiplenmeyi destekleyen yazılı bir öneri. (Terim aynı zamanda İnternet standartları belge serisini de adlandırır.)

**[ROI (Return on Investment)](https://en.wikipedia.org/wiki/Return_on_investment) (yatırım getirisi)**: Bir yatırımdan elde edilen değerin maliyetine göre ölçüsü; mühendislik ve teknoloji kararlarını gerekçelendirmek ve önceliklendirmek için kullanılır.

**[RPA (Robotic Process Automation)](https://en.wikipedia.org/wiki/Robotic_process_automation) (robotik süreç otomasyonu)**: Mevcut kullanıcı arayüzleriyle ve sistemlerle bir insan gibi etkileşerek tekrarlayan, kural tabanlı görevleri otomatikleştiren yazılım "robotları".

**RPO (Recovery Point Objective) (kurtarma noktası hedefi)**: Zamanla ölçülen, kabul edilebilir azami veri kaybı miktarı (örneğin "en fazla beş dakika"); verinin ne sıklıkla korunması gerektiğini tanımlar.

**RTO (Recovery Time Objective) (kurtarma süresi hedefi)**: Bir kesintiden sonra hizmeti geri getirmek için kabul edilebilir azami süre; felaket kurtarma tasarımına ve yatırımına yön verir.

## S

**Saga**: Yerel işlemleri sıralayarak ve bir adım başarısız olduğunda telafi edici eylemler yayınlayarak, dağıtık bir işlemde hizmetler arasında veri tutarlılığını yönetmeye yönelik bir kalıp.

**[SAFe (Scaled Agile Framework)](https://en.wikipedia.org/wiki/Scaled_agile_framework)**: Çevik ve yalın pratikleri büyük kurumlar genelinde uygulayan, birçok takımı koordine eden bir çerçeve; yapısıyla değerli bulunur, olası ağırlığı nedeniyle eleştirilir.

**[SAST (Static Application Security Testing)](https://en.wikipedia.org/wiki/Static_application_security_testing) (statik uygulama güvenlik testi)**: Açıkları geliştirmenin erken aşamasında bulmak için kaynak kodu, bayt kodunu ya da ikili dosyaları çalıştırmadan çözümleyen güvenlik testi.

**SBOM (Software Bill of Materials) (yazılım malzeme listesi)**: Bir yazılım parçasındaki bileşenlerin ve bağımlılıkların, tedarik zinciri ve güvenlik açığı riskini yönetmek için kullanılan, resmî ve makine tarafından okunabilir envanteri.

**SCA (Software Composition Analysis) (yazılım bileşim analizi)**: Bir kod tabanındaki açık kaynak ve üçüncü taraf bileşenleri belirleyen ve bilinen açıkları ve lisans risklerini işaretleyen araçlar.

**[Scrum](https://en.wikipedia.org/wiki/Scrum_(software_development))**: İşi, değer artışlarını teslim etmek için tanımlı roller, olaylar ve yapıtlarla sabit uzunlukta yinelemelere (sprint'lere) örgütleyen çevik bir çerçeve.

**[Section 508](https://en.wikipedia.org/wiki/Section_508_Amendment_to_the_Rehabilitation_Act_of_1973)**: Federal kurumların elektronik ve bilgi teknolojilerini engelli kişilere erişilebilir kılmasını zorunlu kılan, pratikte WCAG ile uyumlu bir ABD yasası.

**Semantic search (anlamsal arama)**: Tam anahtar sözcükler yerine anlama göre eşleşen arama; tipik olarak sorgunun ve belgelerin gömmelerini karşılaştırarak yapılır. Çoğunlukla melez bir yaklaşımda sözcüksel aramayla birleştirilir.

**[Service mesh](https://en.wikipedia.org/wiki/Service_mesh) (hizmet ağı)**: Genellikle yan araç (sidecar) vekilleriyle uygulanan, karşılıklı TLS, yeniden denemeler, zaman aşımları, trafik kaydırma ve gözlemlenebilirlik gibi hizmetten hizmete iletişim kaygılarını ele alan ve onları uygulama kodunun dışında tutan özel bir altyapı katmanı.

**Sidecar (yan araç)**: Ana bir uygulama örneğinin yanında dağıtılan, uygulamanın kendisini değiştirmeden destekleyici yetenekler (örneğin bir hizmet ağı vekili) sağlayan yardımcı bir süreç ya da kapsayıcı.

**[SIEM (Security Information and Event Management)](https://en.wikipedia.org/wiki/Security_information_and_event_management) (güvenlik bilgisi ve olay yönetimi)**: Tespiti, uyarı vermeyi ve soruşturmayı mümkün kılmak için bir ortam genelinde güvenlik günlüklerini ve olaylarını toplayan ve ilişkilendiren bir sistem.

**[SLA (Service Level Agreement)](https://en.wikipedia.org/wiki/Service-level_agreement) (hizmet düzeyi sözleşmesi)**: Bir hizmet sağlayıcı ile müşterileri arasında beklenen hizmet düzeylerini ve bunlar karşılanmadığında doğacak sonuçları belirleyen resmî bir taahhüt.

**SLI (Service Level Indicator) (hizmet düzeyi göstergesi)**: İstek gecikmesi ya da hata oranı gibi hizmet kalitesinin bir yönünün, SLO'lara girdi sağlayan nicel ölçüsü.

**SLO (Service Level Objective) (hizmet düzeyi hedefi)**: İstenen güvenilirlik düzeyini tanımlayan, hata bütçelerinin temelini oluşturan bir SLI için hedef değer ya da aralık.

**SLSA (Supply-chain Levels for Software Artifacts)**: Yazılım yapıtlarının bütünlüğünü ve kökenini (provenance) derleme ve yayın süreci boyunca iyileştirmek için dereceli güvenlik gereksinimlerinden oluşan bir çerçeve.

**SOAR (Security Orchestration, Automation, and Response)**: Hız ve tutarlılığı artırmak için triyaj ve müdahale oyun kitapları gibi güvenlik operasyonlarını otomatikleştiren ve koordine eden araçlar ve pratikler.

**SOC 2 (System and Organization Controls 2)**: Bir hizmet kuruluşunun güvenlik, erişilebilirlik, işleme bütünlüğü, gizlilik ve mahremiyet denetimlerini değerlendiren, AICPA Trust Services Criteria'ya dayalı bir denetim çerçevesi ve raporu.

**[SOLID](https://en.wikipedia.org/wiki/SOLID)**: Bakımı kolay, esnek kodu teşvik eden beş nesne yönelimli tasarım ilkesi (Tek Sorumluluk, Açık/Kapalı, Liskov Yerine Geçme, Arayüz Ayrımı ve Bağımlılığın Tersine Çevrilmesi).

**[SOX (Sarbanes-Oxley Act)](https://en.wikipedia.org/wiki/Sarbanes-Oxley_Act)**: Halka açık şirketlerde mali raporlama ve iç denetimler için gereksinimler getiren, mali veriyi destekleyen BT sistemleri üzerinde de etkileri olan ABD mevzuatı.

**SPACE**: Geliştirici verimliliğini beş boyutta ölçen bir çerçeve: Memnuniyet ve iyi oluş (Satisfaction and well-being), Performans (Performance), Etkinlik (Activity), İletişim ve iş birliği (Communication and collaboration) ve Verimlilik ve akış (Efficiency and flow); tek metrikli ölçümlere karşı uyarır.

**[SRE (Site Reliability Engineering)](https://en.wikipedia.org/wiki/Site_reliability_engineering) (site güvenilirlik mühendisliği)**: Yazılım mühendisliği yaklaşımlarını operasyona uygulayan, güvenilir sistemleri ölçekte işletmek için SLO'ları, hata bütçelerini ve otomasyonu kullanan bir disiplin.

**SSDF (Secure Software Development Framework)**: NIST'in, kurumu hazırlamayı, yazılımı korumayı, iyi güvenceli yazılım üretmeyi ve açıklara yanıt vermeyi kapsayan yüksek düzeyli güvenli geliştirme pratikleri çerçevesi (SP 800-218).

**[Static analysis](https://en.wikipedia.org/wiki/Static_program_analysis) (statik analiz)**: Kaynak kodu, bayt kodunu ya da ikili dosyaları çalıştırmadan inceleyerek kusurları, stil ihlallerini ve güvenlik kusurlarını bulma; tipik olarak düzenleyiciye ve iş hattına bağlanan linter'lar, tip denetleyicileri ve özel çözümleyicilerle yapılır.

**[STRIDE](https://en.wikipedia.org/wiki/STRIDE_model)**: Tehditleri Spoofing, Tampering, Repudiation, Information disclosure, Denial of service ve Elevation of privilege olarak kategorilere ayıran bir tehdit modelleme sınıflandırması.

## T

**[TCO (Total Cost of Ownership)](https://en.wikipedia.org/wiki/Total_cost_of_ownership) (toplam sahip olma maliyeti)**: Yalnızca ilk fiyatı değil, edinmeyi, işletmeyi, bakımı ve nihai emekliliği de içeren, bir sistemin ya da kararın tüm ömrü boyunca maliyeti.

**[TDD (Test-Driven Development)](https://en.wikipedia.org/wiki/Test-driven_development) (test güdümlü geliştirme)**: Tasarımı yönlendirmek ve kapsamı güvence altına almak için kısa, tekrarlanan döngülerde, onu geçirecek koddan önce başarısız bir otomatik test yazma, sonra yeniden düzenleme pratiği.

**[Technical debt](https://en.wikipedia.org/wiki/Technical_debt) (teknik borç)**: Daha uzun sürecek daha iyi bir çözüm yerine şimdi pratik bir çözümü seçmenin ima ettiği gelecekteki maliyet; bilinçsizce biriktirilmek yerine bilerek yönetilmelidir.

**TF-IDF (Term Frequency-Inverse Document Frequency)**: Bir terimin bir belge için önemini, orada ne kadar sık göründüğüne göre puanlayan ve tüm derlemde ne kadar yaygın olduğuyla dengeleyen klasik bir ağırlıklandırma şeması. Sözcüksel arama sıralamasının büyük bölümünün temelindedir.

**[Theory of constraints](https://en.wikipedia.org/wiki/Theory_of_constraints) (kısıtlar kuramı)**: Bir sistemin veriminin herhangi bir anda tek bir darboğazla sınırlı olduğunu, bu yüzden iyileştirme çabalarının o kısıt başka yere kayana kadar ona odaklanması gerektiğini savunan bir yönetim yaklaşımı.

**[Threat modeling](https://en.wikipedia.org/wiki/Threat_model) (tehdit modelleme)**: Savunmaların erken aşamada tasarlanabilmesi için bir sisteme yönelik olası tehditleri belirleme, sıralama ve önceliklendirme yapılandırılmış pratiği.

**Toil (angarya)**: SRE'de, bir hizmetle doğrusal olarak ölçeklenen ve kalıcı değer sağlamayan manuel, tekrarlayan, otomatikleştirilebilir operasyonel iş; onu azaltmak mühendislik için kapasite açar.

**Trunk-based development (ana gövde tabanlı geliştirme)**: Geliştiricilerin küçük değişiklikleri sık sık tek bir paylaşılan dala entegre ettiği, uzun ömürlü dalları ve birleştirme acısını en aza indiren bir kaynak denetimi pratiği.

**[Type inference](https://en.wikipedia.org/wiki/Type_inference) (tip çıkarımı)**: İfadelerin tiplerini otomatik olarak çıkaran, her tipin elle yazılmasını gerektirmeden statik tiplemenin güvenliğinin büyük kısmını sağlayan bir dil özelliği.

**[Type system](https://en.wikipedia.org/wiki/Type_system) (tip sistemi)**: Bir dilin tipleri atamak ve denetlemek için kullandığı kurallar kümesi; program çalışmadan önce bütün hata sınıflarını yakalar ve niyeti belgeler. Tip sistemleri dinamikten statiğe ve zayıftan güçlüye uzanır.

## U

**Ubiquitous language (her yerde geçerli dil)**: Alan odaklı tasarımda, geliştiriciler ve alan uzmanları tarafından tutarlı biçimde kullanılan ve doğrudan kodda ile modellerde yansıtılan ortak, kesin bir sözcük dağarcığı.

**[UAT (User Acceptance Testing)](https://en.wikipedia.org/wiki/Acceptance_testing) (kullanıcı kabul testi)**: Bir sistemin yayın için kabul edilmeden önce iş ihtiyaçlarını karşıladığını doğrulamak için son kullanıcılar ya da temsilcileri tarafından yapılan test.

**[UX / UI (User Experience / User Interface)](https://en.wikipedia.org/wiki/User_experience) (kullanıcı deneyimi / kullanıcı arayüzü)**: Kullanıcı deneyimi, bir kişinin bir ürünle etkileşiminin genel kalitesidir; kullanıcı arayüzü ise bu etkileşimin gerçekleştiği belirli görsel ve etkileşimli yüzeydir.

## V

**[Value object](https://en.wikipedia.org/wiki/Value_object) (değer nesnesi)**: Alan odaklı tasarımda, ayrı bir kimlikle değil tamamen öznitelikleriyle tanımlanan değişmez bir nesne; örneğin bir para tutarı ya da bir tarih aralığı.

**[Value stream mapping](https://en.wikipedia.org/wiki/Value-stream_mapping) (değer akışı haritalama)**: Fikirden teslim edilen değere her adımı çizen, değer katan süreyi bekleme süresinden ayıran, böylece darboğazların, devir teslimlerin ve yeniden iş döngülerinin görünür ve iyileştirilebilir olmasını sağlayan bir teknik.

**[Vector database](https://en.wikipedia.org/wiki/Vector_database) (vektör veritabanı)**: Yüksek boyutlu gömme vektörlerini benzerliğe göre dizinlemek ve aramak için iyileştirilmiş bir veri deposu; anlamsal aramanın ve geri getirme destekli üretimin yaygın bir omurgasıdır.

**Vertical scaling (dikey ölçekleme)**: Tek bir düğümü daha güçlü yaparak ("yukarı ölçekleme") kapasiteyi artırma; basittir ama sonuçta mevcut en büyük makineyle sınırlıdır.

**[VCS (Version Control System)](https://en.wikipedia.org/wiki/Version_control) (sürüm denetim sistemi)**: Geçmişin gözden geçirilebilmesi, dalların sürdürülebilmesi ve işin koordine edilebilmesi için dosyalardaki değişiklikleri zaman içinde kaydeden, Git gibi bir araç.

**[Vulnerability scanning](https://en.wikipedia.org/wiki/Vulnerability_scanner) (güvenlik açığı taraması)**: Sistemlerin, kapsayıcıların ya da kodun bilinen zayıflıklar ve yanlış yapılandırmalar veritabanlarına karşı otomatik incelenmesi. Geniş ve ucuzdur, manuel sızma testinin derinliğini tamamlar.

## W

**[WCAG (Web Content Accessibility Guidelines)](https://en.wikipedia.org/wiki/Web_Content_Accessibility_Guidelines) (web içeriği erişilebilirlik yönergeleri)**: Web içeriğini erişilebilir kılmak için POUR ilkeleri ve A, AA ve AAA uyum düzeyleri etrafında örgütlenmiş, uluslararası kabul görmüş bir W3C yönergeleri kümesi.

**Wardley map (Wardley haritası)**: Yetenekleri kullanıcılara değerine ve evrimsel olgunluğuna göre konumlandıran, inşa et/satın al ve yatırım kararlarına bilgi sağlayan görsel bir strateji tekniği.

**Work in progress (WIP) limit (devam eden iş sınırı)**: Bir iş akışının belirli bir aşamasında aynı anda kaç öğenin bulunabileceğine konan üst sınır; darboğazları açığa çıkararak ve çok fazla paralel işin yükünü kısarak akışı iyileştiren temel bir Kanban pratiğidir.

**WSJF (Weighted Shortest Job First) (ağırlıklı en kısa iş önce)**: İşi, gecikme maliyetini tahmini süresine bölerek sıralayan bir önceliklendirme yöntemi; böylece en kısa, en zamana duyarlı, en yüksek değerli öğeler önce yapılır.

## X

**[XSS (Cross-Site Scripting)](https://en.wikipedia.org/wiki/Cross-site_scripting) (siteler arası betik çalıştırma)**: Bir saldırganın diğer kullanıcıların tarayıcılarında çalışan kötü amaçlı betikler enjekte ettiği, olası olarak veri çalan ya da oturum ele geçiren bir web açığı.

## Y

**[YAGNI (You Aren't Gonna Need It)](https://en.wikipedia.org/wiki/You_aren't_gonna_need_it) (buna ihtiyacın olmayacak)**: Beklenen ihtiyaçların çoğu zaman gerçekleşmediği ve maliyet ile karmaşıklık eklediği gerekçesiyle, işlevselliği tahmin üzerine inşa etmeye karşı öneride bulunan bir ilke.

## Z

**[Zero trust](https://en.wikipedia.org/wiki/Zero_trust_security_model) (sıfır güven)**: Ağ konumuna dayalı örtük güven varsaymayan ve her erişim isteğini kimliğe, aygıta ve bağlama karşı sürekli doğrulayan, "asla güvenme, her zaman doğrula" özdeyişini izleyen bir güvenlik modeli.
