# 12.5 Kaynakça

Bu bölüm, kılavuzun başvuru aygıtını bir araya getirir: SWEBOK bilgi birikimine bir eşleme tablosu, kılavuz boyunca anılan standartların ve çerçevelerin bir dizini ve önerilen okumaların seçilmiş bir bibliyografyası. Bölüm başına kaynaklar da her bölümün sonundaki *Kaynaklar ve ileri okuma* kısmında yer alır.

---

# SWEBOK eşlemesi

Bu kılavuz, IEEE Computer Society'nin **SWEBOK V4.0** (Software Engineering Body of Knowledge) çalışmasıyla uyumludur. 18 bilgi alanının tamamı kapsanır; tablo her birini onu ele alan bölümlere eşler ve kılavuz bunun ardından SWEBOK'un çok ötesine, yapay zekâya, veriye, UX'e, DevOps'a, sürdürülebilirliğe, akışa ve kamu yararı teknolojisine uzanır.

| SWEBOK V4.0 bilgi alanı | Başlıca bölümler |
|---|---|
| 1. Software Requirements | 2.8, 11.1, 5.1 |
| 2. Software Architecture | 3.1, 3.2, 3.3 |
| 3. Software Design | 2.2, 3.1 |
| 4. Software Construction | 2.9, 2.1 |
| 5. Software Testing | 2.4, 8.5 |
| 6. Software Engineering Operations | 9.1, 9.2, 9.3, 8.1 |
| 7. Software Maintenance | 3.7, 3.6, 10.4 |
| 8. Software Configuration Management | 2.10, 2.6, 8.2 |
| 9. Software Engineering Management | 10.1, 10.6, 10.2 |
| 10. Software Engineering Process | 1.4, 10.7, 10.8 |
| 11. Software Engineering Models and Methods | 2.12, 3.1, 2.2 |
| 12. Software Quality | 2.11, 2.4, 3.1 |
| 13. Software Security | 4.1, 4.2, 4.3, 4.4 |
| 14. Software Engineering Professional Practice | 10.5, 1.1, 1.3 |
| 15. Software Engineering Economics | 10.10, 10.1, 9.4 |
| 16. Computing Foundations | 2.13, 3.3, 3.4 |
| 17. Mathematical Foundations | 2.13, 11.3 |
| 18. Engineering Foundations | 2.13, 3.1 |

---

# Standartlar ve çerçeveler

Bu ek, kılavuz boyunca anılan gerçek standartların, çerçevelerin ve düzenlemelerin düzenli bir dizinidir. Bir uyumluluk el kitabı değil, bir gezinti yardımıdır: güncel metin ve bağlamınıza uygulanabilirlik için her zaman yetkili kaynağa ve gerekirse nitelikli hukuk ya da denetim danışmanına başvurun.

Girdiler alana göre gruplanmıştır. Her biri standardın ya da çerçevenin adını, yayımlayan kurumu, tek satırlık kapsamını ve en ilgili olduğu bölümleri ya da alanları verir. Bir ad yaygın olarak kısaltılıyorsa kısaltma gösterilmiştir. Belge numaraları ve başlıklar yalnızca iyi yerleşmiş olduklarında verilir; URL eklenmemiştir.

## Bu ek nasıl kullanılır

- **Düzenlemeler** (örneğin GDPR, HIPAA) kendi yargı alanlarında ve sektörlerinde yasal olarak bağlayıcıdır. Yalnızca iyi uygulama değil, yükümlülük belirlerler.
- **Standartlar** (örneğin ISO/IEC 27001, WCAG) resmî, çoğunlukla sertifikalandırılabilir şartnamelerdir. Bazıları gönüllüdür; bazıları yasa ya da sözleşmeyle zorunlu kılınır.
- **Çerçeveler** (örneğin NIST CSF, NIST AI RMF) risk profilinize göre uyarladığınız, yapılandırılmış ve genellikle gönüllü rehberliklerdir.
- Uygulanabilirlik yargı alanına, sektöre, veri türlerine ve sözleşme şartlarına bağlıdır. Birçok kurum bunların birkaçını aynı anda karşılamak zorundadır.

## Güvenlik ve gizlilik

| Standart / çerçeve | Yayımlayan kurum | Kapsam (tek satır) | Başlıca bölümler / alanlar |
| --- | --- | --- | --- |
| ISO/IEC 27001 | ISO / IEC | Bilgi Güvenliği Yönetim Sistemi (ISMS) gereksinimleri. | 4.1–4.6 Güvenlik ve uyumluluk |
| ISO/IEC 27002 | ISO / IEC | ISO/IEC 27001'i destekleyen rehberlik ve kontrol kümesi. | 4.1–4.4 Güvenlik |
| ISO/IEC 27017 / 27018 | ISO / IEC | Buluta özgü güvenlik kontrolleri (27017) ve bulutta kişisel verilerin (PII) korunması (27018). | 4.3 Altyapı ve bulut güvenliği; 4.5 Gizlilik |
| NIST Cybersecurity Framework (CSF) | National Institute of Standards and Technology | Govern, Identify, Protect, Detect, Respond, Recover etrafında düzenlenmiş gönüllü çerçeve. | 4.1, 4.4 Güvenlik temelleri ve operasyonlar |
| NIST SP 800-53 | National Institute of Standards and Technology | Bilgi sistemleri için güvenlik ve gizlilik kontrolleri kataloğu. | 4.3, 4.6 Bulut güvenliği ve uyumluluk |
| NIST SP 800-63 | National Institute of Standards and Technology | Dijital kimlik ve kimlik doğrulama güvence rehberleri. | 4.2, 4.3 Uygulama ve altyapı güvenliği |
| OWASP Top Ten | Open Worldwide Application Security Project | En kritik web uygulaması güvenlik riskleri, düzenli olarak güncellenir. | 4.2 Uygulama güvenliği |
| OWASP ASVS | Open Worldwide Application Security Project | Uygulama güvenliğini doğrulamak için kademeli gereksinimler ve testler. | 2.4, 4.2 Test ve uygulama güvenliği |
| OWASP SAMM | Open Worldwide Application Security Project | Bir yazılım güvenliği programını oluşturmak ve değerlendirmek için olgunluk modeli. | 4.1 Güvenlik temelleri ve kültürü |
| STRIDE | Microsoft'ta ortaya çıktı | Tehditleri sınıflandırmak için tehdit modelleme taksonomisi. | 4.2 Uygulama güvenliği |
| MITRE ATT&CK | MITRE | Tespit ve savunma için saldırgan taktikleri ve tekniklerinin bilgi tabanı. | 4.4 Güvenlik operasyonları |
| SLSA | Open Source Security Foundation (OpenSSF) | Yazılım tedarik zinciri bütünlüğü ve kökeni için kademeli çerçeve. | 4.2, 8.1, 10.3 Tedarik zinciri ve teslimat |
| SBOM (SPDX / CycloneDX) | Linux Foundation (SPDX); OWASP (CycloneDX) | Yazılım malzeme listeleri için standart biçimler. | 4.2, 10.3 Uygulama güvenliği ve lisanslama |
| PCI DSS | PCI Security Standards Council | Ödeme kartı verilerini işlemek için güvenlik gereksinimleri. | 4.2, 4.5, 4.6 Güvenlik, gizlilik, uyumluluk |

## Uyumluluk ve kamu

### Amerika Birleşik Devletleri

| Düzenleme / çerçeve | Yayımlayan kurum | Kapsam (tek satır) | Başlıca bölümler / alanlar |
| --- | --- | --- | --- |
| HIPAA | US Dept. of Health and Human Services | Korunan sağlık bilgileri (PHI) için güvenceler. | 4.5, 4.6 Gizlilik ve uyumluluk |
| SOX (Sarbanes-Oxley Act) | US Congress / SEC | Halka açık şirketler için finansal raporlama ve iç kontrol gereksinimleri. | 4.6, 10.2 Uyumluluk ve denetim |
| FISMA | US Congress | Federal kurumlar için bilgi güvenliği programı gereksinimleri. | 4.3, 4.6 Bulut güvenliği ve uyumluluk |
| FedRAMP | US General Services Administration / FedRAMP PMO | Federal kurumların kullandığı bulut hizmetleri için standartlaştırılmış güvenlik yetkilendirmesi. | 4.3, 4.6 Bulut güvenliği ve uyumluluk |
| NIST SP 800-171 | National Institute of Standards and Technology | Federal olmayan sistemlerde kontrollü sınıflandırılmamış bilginin (CUI) korunması. | 4.6 Uyumluluk (savunma tedarik zinciri) |
| CMMC | US Department of Defense | Savunma yüklenicilerinin siber güvenlik olgunluğunun sertifikalandırılması. | 4.6 Uyumluluk (savunma) |
| FIPS 140-3 | National Institute of Standards and Technology | Kriptografik modüller için güvenlik gereksinimleri. | 4.3 Altyapı ve bulut güvenliği |
| CCPA / CPRA | State of California | Kaliforniya'da tüketici gizlilik hakları ve işletme yükümlülükleri. | 4.5 Gizlilik ve veri koruma |

### Avrupa Birliği ve Birleşik Krallık

| Düzenleme / standart | Yayımlayan kurum | Kapsam (tek satır) | Başlıca bölümler / alanlar |
| --- | --- | --- | --- |
| GDPR | European Union | Kişisel verilerin işlenmesine ilişkin kapsamlı düzenleme. | 4.5, 4.6 Gizlilik ve uyumluluk |
| UK GDPR / Data Protection Act 2018 | United Kingdom | Birleşik Krallık'ın Brexit sonrası veri koruma rejimi. | 4.5, 4.6 Gizlilik ve uyumluluk |
| eIDAS | European Union | Elektronik kimlik tanımlama ve güven hizmetleri çerçevesi. | 4.2, 4.3 Güvenlik |
| NIS2 Directive | European Union | Temel ve önemli kuruluşlar için siber güvenlik yükümlülükleri. | 4.4, 4.6 Güvenlik operasyonları ve uyumluluk |
| DORA (Digital Operational Resilience Act) | European Union | Finans sektörü için operasyonel dayanıklılık gereksinimleri. | 9.1, 10.2 Güvenilirlik ve denetim |
| EU AI Act | European Union | Yapay zekâ sistemlerinin riske dayalı düzenlenmesi (aşağıdaki yapay zekâ yönetişimine bakın). | 6.1, 6.5 Yapay zekâ stratejisi ve sorumlu yapay zekâ |

## Erişilebilirlik

| Standart | Yayımlayan kurum | Kapsam (tek satır) | Başlıca bölümler / alanlar |
| --- | --- | --- | --- |
| WCAG (2.1 / 2.2) | World Wide Web Consortium (W3C) | A/AA/AAA uyum düzeyleriyle erişilebilir web içeriği rehberleri. | 5.3 Erişilebilirlik; 5.1–5.6 UX ve ön yüz |
| WAI-ARIA | World Wide Web Consortium (W3C) | Erişilebilir zengin internet uygulamaları için roller, durumlar ve özellikler. | 5.3, 5.6 Erişilebilirlik ve ön yüz |
| Section 508 | US Access Board / US federal law | ABD federal BİT'i için WCAG ile uyumlu erişilebilirlik gereksinimleri. | 5.3 Erişilebilirlik (ABD kamusu) |
| EN 301 549 | ETSI / CEN / CENELEC | BİT tedariki için WCAG ile uyumlu Avrupa erişilebilirlik gereksinimleri. | 5.3 Erişilebilirlik (AB kamu sektörü) |
| ADA (Americans with Disabilities Act) | US Congress | Engelliliğe dayalı ayrımcılığı yasaklayan ve dijital hizmetlere uygulanan sivil haklar yasası. | 5.3 Erişilebilirlik |
| ISO/IEC 40500 | ISO / IEC | WCAG 2.0'ın resmî standart olarak uluslararası kabulü. | 5.3 Erişilebilirlik |

## Yapay zekâ yönetişimi

| Çerçeve / düzenleme | Yayımlayan kurum | Kapsam (tek satır) | Başlıca bölümler / alanlar |
| --- | --- | --- | --- |
| NIST AI Risk Management Framework (AI RMF) | National Institute of Standards and Technology | Yapay zekâ riskini yönetmek, haritalamak, ölçmek ve idare etmek için gönüllü çerçeve. | 6.1, 6.5 Yapay zekâ stratejisi ve sorumlu yapay zekâ |
| ISO/IEC 42001 | ISO / IEC | Yapay Zekâ Yönetim Sistemi (AIMS) gereksinimleri. | 6.1, 6.5 Yapay zekâ yönetişimi |
| ISO/IEC 23894 | ISO / IEC | Yapay zekâya özgü risk yönetimi rehberi. | 6.5 Sorumlu ve güvenilir yapay zekâ |
| EU AI Act | European Union | Yapay zekâ sistemlerinin sağlayıcıları ve dağıtıcıları için risk kademeli yasal yükümlülükler. | 6.1, 6.3, 6.5 Yapay zekâ uygulamaları ve yönetişim |
| OECD AI Principles | Organisation for Economic Co-operation and Development | Güvenilir yapay zekâ için değer temelli ilkeler, politikada etkili. | 6.5, 10.5 Sorumlu yapay zekâ ve etik |

## Kalite ve süreç

| Standart / çerçeve | Yayımlayan kurum | Kapsam (tek satır) | Başlıca bölümler / alanlar |
| --- | --- | --- | --- |
| ISO/IEC 25010 | ISO / IEC | Yazılım ürün kalitesi modeli (işlevsel uygunluk, güvenilirlik, güvenlik vb.). | 2.2, 2.4 Tasarım ve test |
| ISO/IEC/IEEE 12207 | ISO / IEC / IEEE | Yazılım yaşam döngüsü süreçleri. | 1.4, 10.1 Çalışma biçimleri ve program yönetimi |
| ISO 9001 | ISO | Genel bir Kalite Yönetim Sistemi gereksinimleri. | 10.2 Risk, denetim ve güvence |
| CMMI | ISACA / CMMI Institute | Süreç yeteneği ve iyileştirmesi için olgunluk modeli. | 10.1, 10.2 Program yönetimi ve güvence |
| DORA metrics | DevOps Research and Assessment (Google Cloud) | Yazılım takımları için dört temel teslimat performansı metriği. | 8.1, 8.4, 9.1 Teslimat, platform, güvenilirlik |
| SPACE framework | Microsoft / GitHub researchers | Geliştirici üretkenliğini ölçmek için çok boyutlu model. | 1.3, 8.4 Gelişim ve geliştirici deneyimi |
| ITIL | AXELOS / PeopleCert | BT hizmet yönetimi uygulamaları çerçevesi. | 9.1, 9.3 Güvenilirlik ve olay yönetimi |

## Mimari

| Standart / çerçeve | Yayımlayan kurum | Kapsam (tek satır) | Başlıca bölümler / alanlar |
| --- | --- | --- | --- |
| ISO/IEC/IEEE 42010 | ISO / IEC / IEEE | Mimari tanımı ve bakış açıları için standart. | 2.7, 3.1 Belgeleme ve mimari temelleri |
| TOGAF | The Open Group | Kurumsal mimari çerçevesi ve geliştirme yöntemi. | 3.1, 10.1 Mimari ve portföy yönetimi |
| C4 model | Topluluk (Simon Brown) | Yazılım mimarisini görselleştirmek için dört düzeyli yaklaşım. | 2.7, 3.1 Belgeleme ve mimari |
| arc42 | Topluluk (Starke / Hruschka) | Mimari belgelemeyi yapılandırmak için şablon. | 2.7, 3.1 Belgeleme ve mimari |
| ADRs | Topluluk uygulaması | Önemli mimari kararların hafif kayıtları. | 1.5, 2.7, 3.1 Karar verme ve belgeleme |

## Bulut ve DevOps

| Standart / çerçeve | Yayımlayan kurum | Kapsam (tek satır) | Başlıca bölümler / alanlar |
| --- | --- | --- | --- |
| CIS Benchmarks | Center for Internet Security | Sistemler ve bulut için uzlaşıya dayalı güvenli yapılandırma temel çizgileri. | 4.3, 8.2 Altyapı güvenliği ve kod olarak altyapı |
| CNCF landscape and projects | Cloud Native Computing Foundation | Bulut yerlisi bilişim için ekosistem ve standartlar (örn. Kubernetes). | 8.3 Konteynerler ve bulut yerlisi |
| OCI (Open Container Initiative) | Open Container Initiative (Linux Foundation) | Konteyner imajı ve çalışma zamanı biçimleri için açık standartlar. | 8.3 Konteynerler ve bulut yerlisi |
| OpenTelemetry | Cloud Native Computing Foundation | Telemetri (izler, metrikler, günlükler) için satıcıdan bağımsız standart. | 9.2 Gözlemlenebilirlik ve izleme |
| Open Policy Agent (OPA) | Cloud Native Computing Foundation | Kod olarak politika için genel amaçlı politika motoru. | 4.6, 8.2, 8.3 Uyumluluk, kod olarak altyapı, orkestrasyon |
| SRE practices | Google (yaygın olarak benimsenmiş) | Güvenilir hizmetleri işletmek için SLI/SLO/hata bütçesi temelli yaklaşım. | 9.1 Site güvenilirliği mühendisliği |
| FinOps Framework | FinOps Foundation | Bulut finansal yönetimi ve maliyet hesap verebilirliği uygulamaları. | 9.4 Maliyet, sürdürülebilirlik, yeşil yazılım |

## Veri

| Standart / çerçeve | Yayımlayan kurum | Kapsam (tek satır) | Başlıca bölümler / alanlar |
| --- | --- | --- | --- |
| DAMA-DMBOK | DAMA International | Veri yönetimi disiplinlerini düzenleyen bilgi birikimi. | 7.1 Veri stratejisi ve yönetişimi |
| ISO/IEC 38505 | ISO / IEC | Verinin kurumsal bir varlık olarak yönetişimi. | 7.1 Veri yönetişimi |
| ISO 8000 | ISO | Veri kalitesi ve ana veri standartları. | 7.1, 7.2 Veri yönetişimi ve mühendisliği |
| Data mesh | Topluluk (Zhamak Dehghani) | Veriye ürün olarak yaklaşan, merkeziyetsiz ve alan odaklı yaklaşım. | 7.1, 7.2 Veri stratejisi ve mühendisliği |
| DCAM | EDM Council | Veri yönetimi yetenek değerlendirme modeli. | 7.1 Veri stratejisi ve yönetişimi |

## Kapsam ve değişim üzerine notlar

Standartlar ve düzenlemeler gelişir. Sürüm numaraları (örneğin WCAG 2.1 ile 2.2 ya da ISO revizyon yılları) ve kontrol katalogları zamanla değişir; yeni yasalar (yapay zekâ ve dayanıklılığa ilişkin sektöre özgü düzenlemeler gibi) ortaya çıkmaya devam eder. Bu eki bir başlangıç haritası olarak ele alın: bir uyumluluk ya da satın alma kararı için herhangi bir girdiye güvenmeden önce güncel sürümü, yargı alanını ve uygulanabilirliği doğrulayın. Kılavuz bölümleri ile bu ek ayrıntıda farklılaştığında yetkili kaynak belge her zaman belirleyicidir.


---

# Önerilen okumalar

Bu ek, kılavuzun her alanını kapsayan, seçilmiş ve açıklamalı bir okuma listesidir. Ölçekte uygulamayı şekillendirmiş eserleri tercih eder: kabul görmüş klasikleri, titiz başvuru kaynaklarını ve büyük, kurumsal ve kamu takımlarının ölçüldüğü standartları ve raporları.

Her girdi başlığı ve yazar(lar)ı, ardından eserin neden önemli olduğunu anlatan tek bir cümle verir. Liste kitabın on bölümü altında düzenlenmiştir. Seçerek okuyun: tüm rafı değil, şu anki acınıza en yakın iki ya da üç eseri seçin. Bir eser birden çok alana yayılıyorsa en yararlı olduğu yere konmuştur; çoğu birkaç bölüme ait olabilir.

Standartlar üzerine bir not: NIST, OWASP, W3C/WCAG, ISO ve DORA programı gibi kuruluşlar düzenli olarak gözden geçirilen yaşayan belgeler yayımlar. Güncel sürümü alıntılayın ve okuyun; aşağıdaki açıklamalar onların kalıcı amacını tarif eder.

## Temeller: Kültür, İnsanlar ve Süreç

- **Accelerate: The Science of Lean Software and DevOps**. Nicole Forsgren, Jez Humble, Gene Kim. Teslimat performansının kurumsal performansı öngördüğünü gösteren ve bunu ölçen metrikleri (artık DORA denir) tanımlayan araştırma temeli.
- **The Phoenix Project**. Gene Kim, Kevin Behr, George Spafford. Akışı, devam eden işi ve DevOps'un "Üç Yol"unu liderler ve şüpheciler için sezgisel kılan bir iş romanı.
- **Team Topologies: Organizing Business and Technology Teams for Fast Flow**. Matthew Skelton and Manuel Pais. İyi yazılım üreten kurumlar tasarlamak için pratik bir söz dağarcığı (akışa hizalı, platform, etkinleştirici ve karmaşık alt sistem takımları).
- **An Elegant Puzzle: Systems of Engineering Management**. Will Larson. Takımları boyutlandırmak, kurumsal büyümeyi yönetmek ve mühendislik liderliğinin yinelenen kararlarını vermek için sahada denenmiş çerçeveler.
- **Staff Engineer: Leadership Beyond the Management Track**. Will Larson. Yönetici olmadan etki isteyenler için staff-plus arketiplerini ve teknik liderlik yolunu tanımlar.
- **The Manager's Path**. Camille Fournier. Teknik liderden yöneticiye aşama aşama bir rehber; kariyer merdivenlerini ve yönetime geçişi çıpalar.
- **The Staff Engineer's Path**. Tanya Reilly. Staff-plus literatürünün tamamlayıcısı; teknik liderliğin, etkinin ve yetkisiz yönlendirmenin günlük işine odaklanır.
- **Peopleware: Productive Projects and Teams**. Tom DeMarco and Timothy Lister. Yazılımın temel sorunlarının teknik değil, sosyolojik olduğuna dair kalıcı savunu.
- **The Mythical Man-Month**. Frederick P. Brooks Jr. Brooks Yasası'nın ve hâlâ kadrolamayı ve zaman çizelgesini yöneten özsel ve arızi karmaşıklık ayrımının kaynağı.
- **The Fearless Organization: Creating Psychological Safety in the Workplace**. Amy C. Edmondson. Suçlamasız kültürün ve başarısızlıktan öğrenmeyi mümkün kılan güvenliğin araştırma temeli.
- **Thinking, Fast and Slow**. Daniel Kahneman. Bilişsel yanlılığın kesin anlatımı; yapılandırılmış mülakatlar, kalibrasyon ve dürüst karar verme için vazgeçilmez.

## Programlama Zanaatı ve Kod Kalitesi

- **The Pragmatic Programmer: Your Journey to Mastery**. Andrew Hunt and David Thomas. Zanaatkârlığın ne demek olduğunu tanımlayan profesyonel alışkanlıkların (DRY, ortogonallik, iz mermileri) temel kataloğu.
- **Refactoring: Improving the Design of Existing Code**. Martin Fowler. Davranışı koruyan dönüşümlerin kanonik kataloğu ve sürekli, testle desteklenen kod iyileştirme disiplini.
- **Clean Code: A Handbook of Agile Software Craftsmanship**. Robert C. Martin. Adlandırma, işlevler ve okunabilirlik için yaygın olarak kullanılan (ve tartışılan) bir standart; birçok takımın inceleme beklentilerini şekillendirir.
- **Code Complete**. Steve McConnell. İnşa uygulamalarının kapsamlı, kanıta dayalı el kitabı; programlama kalitesi için hâlâ titiz bir temel çizgidir.
- **Test-Driven Development: By Example**. Kent Beck. Kırmızı-yeşil-yeniden düzenleme döngüsüne ve teste öncelikli tasarıma özgün, uygulamalı giriş.
- **Working Effectively with Legacy Code**. Michael Feathers. Hiç testi olmayan koda test eklemek ve onu güvenle değiştirmek için kesin araç takımı; uzun ömürlü sistemler için vazgeçilmez.
- **Growing Object-Oriented Software, Guided by Tests**. Steve Freeman and Nat Pryce. Dıştan içe TDD'nin, sahte nesnelerin ve bir tasarımı testlerle geliştirmenin uygulamalı gösterimi.
- **A Philosophy of Software Design**. John Ousterhout. Karmaşıklık, derin modüller ve bilgi gizleme üzerine keskin, görüş bildiren bir ele alış; bazı "temiz kod" ortodoksisine verimli biçimde meydan okur.

## Mimari ve Sistemler

- **Designing Data-Intensive Applications**. Martin Kleppmann. Depolama, çoğaltma, bölümleme, tutarlılık ve ölçekte akış işlemenin ödünleşimleri üzerine en iyi modern başvuru kaynağı.
- **Fundamentals of Software Architecture: An Engineering Approach**. Mark Richards and Neal Ford. Mimari stillerin, niteliklerin ve mimarın rolü ile karar vermesinin geniş, güncel bir taraması.
- **Software Architecture: The Hard Parts**. Neal Ford, Mark Richards, Pramod Sadalage, Zhamak Dehghani. Dağıtık mimari ödünleşimlerine, hizmet ayrıntı düzeyine ve veri sahipliğine karar odaklı bir ele alış.
- **Building Evolutionary Architectures**. Neal Ford, Rebecca Parsons, Patrick Kua. Uygunluk işlevlerini ve zaman içinde güvenle değişecek biçimde tasarlanmış mimariyi tanıtır.
- **Domain-Driven Design: Tackling Complexity in the Heart of Software**. Eric Evans. Sınırlı bağlamların, her yerde geçerli dilin ve kümelerin kaynağı: modern hizmet tasarımının söz dağarcığı.
- **Building Microservices: Designing Fine-Grained Systems**. Sam Newman. Ayrıştırma, hizmet sınırları, dağıtım ve mikro hizmetlerin kurumsal sonuçları için başvuru kaynağı.
- **Monolith to Microservices**. Sam Newman. Riskli büyük patlama yeniden yazımı olmadan, strangler fig ve soyutlamayla dal açma gibi kademeli ayrıştırma için bir kalıp kataloğu.
- **Patterns of Enterprise Application Architecture**. Martin Fowler. Kurumsal sistemlere ortak bir dil kazandıran adlandırılmış kalıp başvurusu (repository, unit of work ve daha fazlası).
- **Enterprise Integration Patterns**. Gregor Hohpe and Bobby Woolf. Olay güdümlü ve eşzamansız mimarilerin temelindeki mesajlaşma kalıplarının kesin kataloğu.
- **Release It! Design and Deploy Production-Ready Software**. Michael T. Nygard. Gerçek üretimde ayakta kalan sistemler için devre kesici, bölme (bulkhead) ve diğer kararlılık kalıplarının kaynağı.
- **Design Patterns: Elements of Reusable Object-Oriented Software**. Erich Gamma, Richard Helm, Ralph Johnson, John Vlissides ("Gang of Four"). Nesne yönelimli kalıpların tarihsel olarak belirleyici kataloğu ve ortak bir tasarım söz dağarcığı.

## Güvenlik, Gizlilik ve Güven

- **Threat Modeling: Designing for Security**. Adam Shostack. STRIDE'a ve yapılandırılmış tehdit modellemeye rutin bir mühendislik uygulaması olarak pratik, kapsamlı rehber.
- **Security Engineering: A Guide to Building Dependable Distributed Systems**. Ross Anderson. Gerçek sistemlerin nasıl başarısız olduğuna ve saldırıya direnenlerin nasıl inşa edileceğine dair ansiklopedik başvuru kaynağı.
- **The Tangled Web: A Guide to Securing Modern Web Applications**. Michal Zalewski. Tarayıcı güvenlik modelinin ve web platformlarının saf varsayımlara ihanet ettiği ince yolların titiz bir turu.
- **Cryptography Engineering**. Niels Ferguson, Bruce Schneier, Tadayoshi Kohno. Kriptografiyi doğru kullanmak ve yaygın, tehlikeli hatalardan kaçınmak için uygulayıcı rehberi.
- **Building Secure and Reliable Systems**. Heather Adkins et al. (Google). Google'ın, güvenliği ve güvenilirliği en başından tasarlanan iç içe özellikler olarak ele alan sentezi.
- **Zero Trust Networks**. Evan Gilman and Doug Barth. Asla güvenme, her zaman doğrula ağ mimarisinin ilkelerinin ve işleyişinin açık bir ele alışı.
- **OWASP Top 10**. OWASP Foundation. Politika ve denetimde dünya çapında başvurulan, en kritik web uygulaması güvenlik risklerinin uzlaşıya dayalı temel çizgisi.
- **OWASP Application Security Verification Standard (ASVS)**. OWASP Foundation. Sözleşmeler ve kabul ölçütleri için uygun, kademeli ve sınanabilir bir güvenlik gereksinimleri denetim listesi.
- **NIST SP 800-53: Security and Privacy Controls for Information Systems and Organizations**. NIST. ABD federal güvenliğinin merkezindeki kontrol kataloğu ve FedRAMP ile FISMA yetkilendirmesinin temeli.
- **NIST Cybersecurity Framework (CSF)**. NIST. Bir güvenlik programını düzenlemek için yaygın olarak benimsenen belirle-koru-tespit et-müdahale et-kurtar yapısı.
- **NIST SP 800-207: Zero Trust Architecture**. NIST. Çoğu kurumsal ve kamu sıfır güven programını çıpalayan başvuru tanımı ve başvuru mimarileri.

## UX, UI ve Ürün Tasarımı

- **The Design of Everyday Things**. Don Norman. Fiziksel nesnelerin çok ötesinde geçerli olan sunuş ipuçları, belirteçler, geri bildirim ve insan merkezli tasarım üzerine temel metin.
- **Don't Make Me Think, Revisited**. Steve Krug. Kendiliğinden anlaşılır kullanılabilirliğin ve ucuz, sık kullanılabilirlik testinin değerinin özlü, kalıcı savunusu.
- **About Face: The Essentials of Interaction Design**. Alan Cooper, Robert Reimann, David Cronin. Etkileşim tasarımı, personalar ve hedef odaklı tasarım üzerine kapsamlı başvuru kaynağı.
- **Design Systems: A Practical Guide**. Alla Kholmatova. Tutarlı, yeniden kullanılabilir bileşen sistemleri kurmanın ve arkasındaki ortak dilin sağlam bir anlatımı.
- **Refactoring UI**. Adam Wathan and Steve Schoger. Resmî eğitimi olmadan arayüz tasarlayan mühendisler için görsel cilaya dair pratik, örnek odaklı rehber.
- **Letting Go of the Words: Writing Web Content that Works**. Ginny Redish. Sade dilli, görev odaklı içerik tasarımı için kesin rehber.
- **Inclusive Design Patterns / Accessibility for Everyone**. Heydon Pickering; Laura Kalbag. İnsan yeteneklerinin tüm yelpazesi için çalışan arayüzler kurmaya yönelik pratik yoldaşlar.
- **A Web for Everyone: Designing Accessible User Experiences**. Sarah Horton and Whitney Quesenbery. Erişilebilirlik standartları ile iyi kullanıcı deneyimi arasında ilke odaklı bir köprü.
- **Web Content Accessibility Guidelines (WCAG) 2.2**. W3C. Çoğu erişilebilirlik yasasının arkasındaki, uluslararası alanda başvurulan standart (algılanabilir, işletilebilir, anlaşılabilir, sağlam).
- **U.S. Web Design System (USWDS)**. U.S. government. Kamu hizmetleri için ölçekte inşa edilmiş, erişilebilir ve standart temelli bir tasarım sisteminin çalışan örneği.

## Yapay Zekâ ve Makine Öğrenmesi

- **Designing Machine Learning Systems**. Chip Huyen. Üretim ML sistemlerini uçtan uca (veri, özellikler, dağıtım ve izleme) kurmak için önde gelen pratik rehber.
- **Reliable Machine Learning: Applying SRE Principles to ML in Production**. Cathy Chen et al. SRE disiplinini (SLO'lar, izleme, olay müdahalesi) makine öğrenmesi sistemlerine genişletir.
- **Deep Learning**. Ian Goodfellow, Yoshua Bengio, Aaron Courville. Modern sinir ağlarının altındaki kuram ve yöntemler için standart akademik başvuru kaynağı.
- **AI Engineering: Building Applications with Foundation Models**. Chip Huyen. Büyük temel modeller üzerine kurulu uygulamaları tasarlamak, değerlendirmek ve işletmek için güncel rehber.
- **Weapons of Math Destruction**. Cathy O'Neil. Algoritmik hesap verebilirlik ve sorgulanmamış modellerin gerçek dünyadaki zararları için canlı bir savunu; kamu sektörü yapay zekâsı için vazgeçilmez.
- **Interpretable Machine Learning**. Christoph Molnar. Modeller ve tahminleri için açıklanabilirlik yöntemleri üzerine kapsamlı, ücretsiz erişilebilir başvuru kaynağı.
- **NIST AI Risk Management Framework (AI RMF 1.0)**. NIST. Yapay zekâ riskini yönetmek, haritalamak, ölçmek ve idare etmek için başvuru çerçevesi; politika ve satın almada giderek daha çok anılıyor.

## Veri, Analitik ve İçgörü

- **The Data Warehouse Toolkit: The Definitive Guide to Dimensional Modeling**. Ralph Kimball and Margy Ross. Analitik için yıldız şemaları ve boyutsal modelleme üzerine kanonik başvuru kaynağı.
- **Trustworthy Online Controlled Experiments: A Practical Guide to A/B Testing**. Ron Kohavi, Diane Tang, Ya Xu. Ölçekte güvenilir, eyleme dönüştürülebilir sonuçlar veren deneyleri yürütmek için yetkili rehber.
- **Fundamentals of Data Engineering**. Joe Reis and Matt Housley. Modern veri yaşam döngüsünün ve arkasındaki mühendislik uygulamalarının satıcıdan bağımsız haritası.
- **Data Mesh: Delivering Data-Driven Value at Scale**. Zhamak Dehghani. Veriyi ölçekte düzenlemeye yönelik alan odaklı, ürün merkezli yaklaşımın kurucu metni.
- **Storytelling with Data**. Cole Nussbaumer Knaflic. Dürüst, açık veri görselleştirmesi ve içgörüyü karar vericilere iletmek için pratik rehber.
- **The Visual Display of Quantitative Information**. Edward R. Tufte. Grafik bütünlüğü, veri-mürekkep ve veriyi dürüstçe göstermenin etiği üzerine temel eser.
- **DAMA-DMBOK: Data Management Body of Knowledge**. DAMA International. Veri yönetişimi, sorumluluk, kalite ve kataloglama için kapsamlı başvuru çerçevesi.
- **The Book of Why**. Judea Pearl and Dana Mackenzie. Nedensel çıkarıma okunaklı bir giriş; korelasyondan savunulabilir kararlara geçmek için hayati.

## Otomasyon, DevOps ve Platform Mühendisliği

- **The DevOps Handbook**. Gene Kim, Jez Humble, Patrick Debois, John Willis. "Üç Yol"u akış, geri bildirim ve sürekli öğrenme için somut uygulamalara çeviren kapsamlı el kitabı.
- **Continuous Delivery: Reliable Software Releases through Build, Test, and Deployment Automation**. Jez Humble and David Farley. Dağıtım işlem hatları, otomasyon ve yazılımı güvenle ve sık yayımlamak üzerine temel metin.
- **Infrastructure as Code: Managing Servers in the Cloud**. Kief Morris. Altyapıya yazılım gibi davranma üzerine başvuru kaynağı: modüller, test, değişmezlik ve sapma.
- **Team Topologies**. Matthew Skelton and Manuel Pais. (Bkz. Temeller.) Platform takımlarını ve sundukları geliştirici deneyimini şekillendirmek için burada da vazgeçilmez.
- **Kubernetes Patterns**. Bilgin Ibryam and Roland Huß. Kubernetes üzerinde bulut yerlisi uygulamalar tasarlamak için yeniden kullanılabilir kalıplar kataloğu.
- **Software Engineering at Google**. Titus Winters, Tom Manshreck, Hyrum Wright. Test, inceleme, araçlar ve bağımlılık yönetimi gibi mühendislik uygulamalarının on yıllar boyunca on binlerce mühendise nasıl ölçeklendiği.
- **The Twelve-Factor App**. Adam Wiggins (Heroku). Taşınabilir, ölçeklenebilir, bulut yerlisi hizmetler kurmak için kısa, etkili manifesto.
- **DORA State of DevOps Report**. DORA / Google Cloud (annual). Dört temel teslimat metriğinin ve performansı yönlendiren yeteneklerin arkasındaki süregiden araştırma programı.

## Operasyon, Güvenilirlik ve Gözlemlenebilirlik

- **Site Reliability Engineering: How Google Runs Production Systems**. Betsy Beyer, Chris Jones, Jennifer Petoff, Niall Richard Murphy (eds.). SLI'ları, SLO'ları, hata bütçelerini ve güvenilirlik mühendisliği disiplinini tanımlayan temel metin.
- **The Site Reliability Workbook**. Betsy Beyer et al. (eds.). Pratik örnekler, işlenmiş SLO'lar ve uygulama rehberliği içeren uygulamalı tamamlayıcı.
- **Observability Engineering**. Charity Majors, Liz Fong-Jones, George Miranda. Gözlemlenebilirliğin, yüksek kardinaliteli verinin ve üretimde bilinmeyen bilinmeyenlerin hata ayıklamasının modern tanımı.
- **Implementing Service Level Objectives**. Alex Hidalgo. SLO'ları ve hata bütçelerini iyi tasarlamak, ölçmek ve kullanmak için kapsamlı, pratik rehber.
- **Release It!**. Michael T. Nygard. (Bkz. Mimari.) Üretim kararlılığı kalıpları ve dayanıklı sistemleri işletmek için burada da temeldir.
- **The Art of Capacity Planning**. Arun Kejariwal and John Allspaw. Büyüyen sistemler için talebi öngörmeye ve kapasite planlamaya veri odaklı bir yaklaşım.
- **Chaos Engineering: System Resiliency in Practice**. Casey Rosenthal and Nora Jones. Sistem dayanıklılığına güven oluşturmak için bilerek başarısızlık enjekte etmenin kesin ele alışı.
- **Google SRE Book, Chapter on Postmortems**. Google. Suçlamasız olay sonrası incelemeleri ve olaylardan öğrenme için yaygın biçimde örnek alınan model.

## Kurumsal, Kamu ve Kamu Yararı

- **Working in Public: The Making and Maintenance of Open Source Software**. Nadia Eghbal. Açık kaynağın gerçekte nasıl sürdürüldüğünün ve kurumların güvendiği bağımlılıkların arkasındaki bakımcı yükünün temel incelemesi.
- **Recoding America: Why Government Is Failing in the Digital Age and How We Can Do Better**. Jennifer Pahlka. Kamu sektörü teknolojisinin neden başarısız olduğunun ve teslimat odaklı reformun bunu nasıl düzeltebileceğinin gerçekçi anlatımı.
- **Digital Transformation at Scale: Why the Strategy Is Delivery**. Andrew Greenway et al. Birleşik Krallık Government Digital Service'ten, kamu hizmetlerini planlayarak değil teslim ederek dönüştürme dersleri.
- **Project to Product**. Mik Kersten. Büyük kurumları proje temelli finansmandan kalıcı ürün değer akışlarına geçirmek için Flow Framework.
- **Escaping the Build Trap**. Melissa Perri. Kurumların çıktıyı sonuçla nasıl karıştırdığı ve ürün yönetiminin bunu nasıl düzelttiği; portföy ve program yönetişimiyle doğrudan ilgili.
- **U.S. Digital Services Playbook**. U.S. Digital Service. Etkili, kullanıcı merkezli kamu dijital hizmetleri sunmak için özlü bir hamleler kümesi.
- **GOV.UK Service Manual and Service Standard**. UK Government Digital Service. İyi kamu hizmetleri kurmak için, diğer hükümetlerce yaygın biçimde örnek alınan çalışan, yayımlanmış bir standart.
- **NIST SP 800-37: Risk Management Framework**. NIST. ABD federal sistemlerinde işletme yetkisinin (ATO) ve sürekli izlemenin arkasındaki süreç çerçevesi.
- **The FinOps Foundation Framework**. FinOps Foundation. Finans ve mühendislik genelinde bulut maliyet görünürlüğü, optimizasyonu ve hesap verebilirliği için başvuru modeli.

## Bu liste nasıl kullanılır

- **Acınızla başlayın.** Dağıtımlar yavaş ve korkutucuysa başka bir şeyden önce *Accelerate*, *Continuous Delivery* ve *DORA* raporlarını okuyun.
- **Sprint için değil, on yıl için okuyun.** Belirli bir araç sürümüne bağlı olanlar yerine kalıcı ilkeleri açıklayan eserleri tercih edin.
- **Standartların güncel sürümünü doğrulayın.** NIST, OWASP, WCAG, ISO ve DORA yayınlarını revize eder; her zaman en son sürümden çalışın ve sürümü kendi politikalarınıza not edin.
- **Ortak bir raf kurun.** Bunlardan iki ya da üçünü birlikte okumuş bir takım daha az tartışır ve daha hızlı karar verir, çünkü ortak bir söz dağarcığı ve bir dizi başvuru noktası paylaşır.
- **Referans standartların ve çerçevelerin tam dizini için bölüm 12.5'e** ve bu eserlerin anlattığı uygulamaların benimsenmesini nasıl sıralayacağınız için **bölüm 12.6'ya** da bakın.
