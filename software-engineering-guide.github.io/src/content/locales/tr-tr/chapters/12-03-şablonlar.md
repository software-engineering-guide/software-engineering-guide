# 12.3 Şablonlar

Bu şablonlar kopyalayıp yapıştırmaya hazır başlangıç noktalarıdır. Herhangi bir şablonu wiki'nize, deponuza ya da bilet sisteminize taşıyın ve köşeli parantezli yer tutucuları doldurun. İtalik notlar ve satır içi yorumlar her bölüme neyin ait olduğunu açıklar; bölüm dolduktan sonra bunları silin. Şablonları hafif tutun: tamamlamaktan çok atlaması hızlı olan bir şablon kullanılmaz. Başlıkları ve bölümleri kurumunuza uyarlayın, ancak her parçanın amacını koruyun.

Aşağıda kullanılan birkaç gelenek:

- `[köşeli parantez]` içindeki metin, yerine yazılacak bir yer tutucudur.
- _İtalik_ ya da `<!-- yorumlar -->` biçimindeki metin, silinecek yönlendirmedir.
- Bitmiş belgeyi, sorularını yanıtlamaya devam ettiği sürece olabildiğince kısa tutun.

## Mimari karar kaydı (ADR)

```markdown
# ADR [NNNN]: [Kararın kısa başlığı]

- Durum: [Önerildi | Kabul edildi | Kullanımdan kaldırıldı | ADR-XXXX tarafından yerine geçildi]
- Tarih: [YYYY-AA-GG]
- Karar verenler: [adlar ya da roller]
- Danışılanlar: [adlar ya da roller]

## Bağlam

<!-- Bu kararı doğuran sorun, etki ya da kısıt nedir?
     Olguları ve gereksinimleri tarafsız biçimde belirtin. Yalnızca
     gelecekteki bir okuyucunun bir kararın neden gerekli olduğunu
     anlaması için gerekenleri ekleyin. -->

## Karar

<!-- Seçimi bir ya da iki net cümleyle belirtin: "... yapacağız." -->

## Değerlendirilen alternatifler

<!-- Tarttığınız gerçekçi seçenekleri ve her birinin neden seçildiğini
     ya da seçilmediğini sıralayın. Burada en az iki alternatif
     bulunmalıdır. -->

- Seçenek A: [özet]; [gerekçe] nedeniyle reddedildi.
- Seçenek B: [özet]; [gerekçe] nedeniyle reddedildi.
- Seçilen seçenek: [özet]; [gerekçe] nedeniyle seçildi.

## Sonuçlar

<!-- Kararın dürüst sonuçları, hem iyi hem kötü. -->

- Olumlu: [elde edilen faydalar]
- Olumsuz: [kabul edilen maliyetler, riskler ya da sınırlamalar]
- Takip: [bu kararın tetiklediği geçişler, yeni işler ya da kararlar]

## İlgili

<!-- Bununla ilgili önceki ADR'lere, RFC'lere, biletlere ya da belgelere
     bağlantılar. -->
```

## RFC / tasarım belgesi

```markdown
# RFC: [Başlık]

- Yazar(lar): [adlar]
- Durum: [Taslak | İncelemede | Onaylandı | Reddedildi | Uygulandı]
- İnceleyenler: [adlar ya da roller]
- Oluşturulma: [YYYY-AA-GG]
- Son güncelleme: [YYYY-AA-GG]
- Bilet / izleme: [bağlantı]

## Özet

<!-- Tek paragraf: bunun neyi önerdiği ve neden önemli olduğu. Bir okuyucu
     yalnızca bu bölümden özü kavrayabilmelidir. -->

## Sorun ve motivasyon

<!-- Hangi sorunu çözüyoruz? Kim etkileniyor? Hiçbir şey yapmazsak ne
     olur? İlgili arka planı ve kısıtları ekleyin. -->

## Hedefler ve hedef dışı olanlar

- Hedefler: [başarının neye benzediği, mümkün olduğunda ölçülebilir]
- Hedef dışı olanlar: [kapsam kaymasını önlemek için açıkça kapsam dışı olanlar]

## Önerilen tasarım

<!-- Belgenin çekirdeği. Yaklaşımı, mimariyi, veri modelini, arayüzleri
     ve temel akışları anlatın. Açıklığa yardımcı olduğunda diyagramlar
     kullanın. Yalnızca ne olduğunu değil, nasıl çalıştığını açıklayın. -->

## Değerlendirilen alternatifler

<!-- Diğer yaklaşımlar ve neden seçilmedikleri. Okuyucuya tasarım
     uzayının araştırıldığını gösterir. -->

## Etki ve riskler

- Güvenlik ve gizlilik: [etkiler ve azaltımlar]
- Performans ve ölçek: [beklenen yük ve davranış]
- İşletilebilirlik: [izleme, başarısızlık kipleri, kullanıma alma, geri alma]
- Maliyet: [altyapı ya da lisans etkisi]
- Geriye dönük uyumluluk: [geçiş ve kullanımdan kaldırma]

## Test ve kullanıma alma planı

<!-- Değişikliğin nasıl doğrulanacağı ve güvenle yayımlanacağı. -->

## Açık sorular

<!-- İncelemecilerin görüşünü almak istediğiniz çözülmemiş konular. -->
```

## Ölüm sonrası inceleme / olay incelemesi (suçlamasız)

```markdown
# Ölüm sonrası inceleme: [Olay başlığı]

- Olay kimliği: [KİMLİK]
- Olay tarihi: [YYYY-AA-GG]
- Yazarlar: [adlar]
- Durum: [Taslak | Nihai]
- Ciddiyet: [SEV1 | SEV2 | SEV3]

> Bu inceleme suçlamasızdır. Bireylere değil, sistemlere ve katkıda
> bulunan etkenlere odaklanırız. Amaç öğrenmek ve tekrarını önlemektir.

## Özet

<!-- İki ya da üç cümle: ne olduğu, etkisi ve çözümü; uzman olmayan biri
     tarafından okunabilir. -->

## Etki

- Süre: [başlangıç saatinden kurtarma saatine, saat dilimiyle birlikte]
- Etkilenen kullanıcılar: [kapsam ve sayı]
- İş etkisi: [gelir, SLA, itibar ya da diğer]

## Zaman çizelgesi

<!-- Zaman damgalı, olgusal olay sırası. Tespiti, yükseltmeyi, temel
     eylemleri ve kurtarmayı ekleyin. -->

- [SS:DD] [olay]
- [SS:DD] [olay]

## Katkıda bulunan etkenler

<!-- Olaya yol açan koşullar zinciri. Tek bir kök neden yerine
     "katkıda bulunan etkenleri" tercih edin. -->

## Tespit ve müdahale

- Nasıl tespit edildi? [uyarı, müşteri bildirimi vb.]
- Müdahaleye ne yardımcı oldu?
- Müdahaleyi ne yavaşlattı?

## İyi giden şeyler

<!-- Etkili eylemleri ve işe yarayan güvenceleri takdir edin. -->

## Eylem maddeleri

<!-- Belirli, sahibi olan ve tarihli. Önlemeyi, tespiti ve azaltımı
     ele alın. Bunları olağan iş listesinde izleyin. -->

| Eylem | Sahip | Bitiş tarihi | Tür (önle/tespit et/azalt) | Bilet |
|-------|-------|--------------|----------------------------|-------|
| [eylem] | [ad] | [tarih] | [tür] | [bağlantı] |

## Çıkarılan dersler

<!-- Daha geniş kurumun çıkarması gereken sonuçlar. -->
```

## Tehdit modeli (STRIDE tabanlı)

```markdown
# Tehdit modeli: [Sistem ya da özellik adı]

- Yazar(lar): [adlar]
- Tarih: [YYYY-AA-GG]
- İnceleyenler: [güvenlik irtibatı, sahipler]
- Kapsam: [nelerin kapsandığı ve kapsanmadığı]

## Sisteme genel bakış

<!-- Sistemin, amacının ve kullanıcılarının kısa tanımı. -->

## Varlıklar

<!-- Korumaya değer olanlar: veri, kimlik bilgileri, işlevsellik, itibar.
     Her birinin hassasiyetini not edin. -->

## Güven sınırları ve veri akışı

<!-- Bileşenleri, veri depolarını, dış varlıkları ve güvenin değiştiği
     sınırları anlatın ya da diyagramla gösterin. -->

## Tehditler (STRIDE)

<!-- Her öğe için STRIDE kategorilerini düşünün. Her inandırıcı tehdidi,
     riskini ve azaltımını ya da kabul edilen riski kaydedin. -->

| Tehdit | STRIDE kategorisi | Etkilenen öğe | Risk (D/O/Y) | Azaltım | Durum |
|--------|-------------------|---------------|--------------|---------|-------|
| [tehdit] | Spoofing | [öğe] | [risk] | [kontrol] | [açık/azaltıldı/kabul edildi] |
| [tehdit] | Tampering | [öğe] | [risk] | [kontrol] | [durum] |
| [tehdit] | Repudiation | [öğe] | [risk] | [kontrol] | [durum] |
| [tehdit] | Information disclosure | [öğe] | [risk] | [kontrol] | [durum] |
| [tehdit] | Denial of service | [öğe] | [risk] | [kontrol] | [durum] |
| [tehdit] | Elevation of privilege | [öğe] | [risk] | [kontrol] | [durum] |

## Varsayımlar ve bağımlılıklar

<!-- Dayanılan güvenlik varsayımları ve güvenilen dış kontroller. -->

## Açık konular ve takip

<!-- Daha fazla çalışma gerektiren, bilet olarak izlenen tehditler. -->
```

## Çalışma kılavuzu (runbook)

```markdown
# Runbook: [Görev ya da senaryo adı]

- Hizmet: [hizmet adı]
- Sahip: [takım]
- Son gözden geçirme: [YYYY-AA-GG]
- İlgili uyarılar: [uyarı adları]

## Amaç

<!-- Bu runbook'un ne zaman kullanılacağı ve neyi başardığı. -->

## Ön koşullar

<!-- Başlamadan önce gereken erişim, araçlar ve izinler. -->

## Tespit / belirtiler

<!-- Operatörün gözlemledikleri: uyarılar, hata imzaları, panolar. -->

## Tanı

<!-- Sorunu doğrulamak ve nedeni daraltmak için adım adım kontroller.
     Tam komutları, sorguları ya da pano bağlantılarını ekleyin. -->

1. [adım ve beklenen sonuç]
2. [adım ve beklenen sonuç]

## Çözüm

<!-- Düzeltmek ya da azaltmak için somut, sıralı adımlar. Riskli ya da
     geri döndürülemez her adımı ve başarının nasıl doğrulanacağını
     not edin. -->

1. [adım]
2. [kurtarmayı doğrula]

## Geri alma

<!-- Çözüm işleri daha da kötüleştirirse eylemlerin nasıl geri alınacağı. -->

## Yükseltme

<!-- Kiminle iletişime geçileceği ve ne zaman yükseltileceği. İkincil
     nöbetçi, sahip takım ve tedarikçi irtibatları. -->

## Kaynaklar

<!-- Panolar, ilgili runbook'lar, mimari belgeleri. -->
```

## Hizmet README'si / hizmet kataloğu girdisi

```markdown
# [Hizmet adı]

- Sahip takım: [takım]
- Nöbet: [rotasyon bağlantısı]
- Katman / kritiklik: [Katman 1 | 2 | 3]
- Depo: [bağlantı]
- Durum: [Etkin | Kullanımdan kaldırıldı]

## Ne yapar

<!-- Hizmetin sorumluluğu ve tüketicileri hakkında tek paragraf. -->

## Mimari

<!-- Temel bileşenler, bağımlılıklar (yukarı ve aşağı akış) ve tasarım
     belgesine ya da diyagrama bağlantı. -->

## Arayüzler

- API'ler / uç noktalar: [belirtime bağlantı]
- Yayımlanan / tüketilen olaylar: [konular]
- Veri depoları: [veritabanları, önbellekler, kovalar]

## Çalışma zamanı ve dağıtım

- Ortamlar: [geliştirme, hazırlık, üretim]
- Nasıl dağıtılır: [işlem hattı bağlantısı ve süreç]
- Yapılandırma ve özellik bayrakları: [nerede ve nasıl]

## Gözlemlenebilirlik

- Panolar: [bağlantılar]
- Uyarılar: [bağlantılar]
- Günlükler: [nerede bulunur]
- SLO'lar: [bağlantı]

## Operasyonlar

- Runbook'lar: [bağlantılar]
- Yaygın görevler: [ölçekleme, yeniden başlatma, geriye dönük doldurma]
- Bilinen sorunlar ve sınırlamalar: [notlar]

## Başlarken (yeni katkıda bulunanlar için)

<!-- Yerelde nasıl derlenir, test edilir ve çalıştırılır. -->

## İletişim

- Slack / sohbet kanalı: [bağlantı]
- Yükseltme: [yol]
```

## SLO / hata bütçesi politikası

```markdown
# SLO ve hata bütçesi politikası: [Hizmet ya da yolculuk adı]

- Sahip: [takım]
- Yürürlük tarihi: [YYYY-AA-GG]
- Gözden geçirme sıklığı: [örn. üç ayda bir]

## Hizmet düzeyi göstergeleri (SLI'lar)

<!-- Her SLI'ı kesin biçimde tanımlayın: ölçülen nicelik, nasıl ölçüldüğü
     ve nereden ölçüldüğü (ideal olarak kullanıcının bakış açısından). -->

| SLI | Tanım | Veri kaynağı |
|-----|-------|--------------|
| Erişilebilirlik | [örn. başarılı istekler / toplam istekler] | [kaynak] |
| Gecikme | [örn. X ms altındaki isteklerin oranı] | [kaynak] |

## Hedefler (SLO'lar)

| SLI | Hedef | Ölçüm penceresi |
|-----|-------|-----------------|
| Erişilebilirlik | [örn. %99,9] | [örn. kayan 28 gün] |
| Gecikme | [örn. %95'i 300 ms altında] | [kayan 28 gün] |

## Hata bütçesi

<!-- İzin verilen güvenilmezlik: pencere boyunca %100 eksi hedef.
     Bütçeyi somut terimlerle belirtin (örn. dakika/ay). -->

- Bütçe: [türetilmiş pay]

## Bütçe tükendiğinde politika

<!-- Üzerinde uzlaşılan sonuçlar. Bunları somut ve uygulanabilir yapın. -->

- [örn. Bütçe toparlanana kadar kritik olmayan özellik sürümlerini dondur.]
- [örn. Bir sonraki planlama döngüsünde güvenilirlik çalışmasına öncelik ver.]
- [örn. Art arda iki pencerede ihlal edilirse mühendislik liderliğine yükselt.]

## Bütçe sağlıklı olduğunda politika

<!-- Takımın alabileceği ek risk, örn. daha hızlı kullanıma alma. -->

## Uyarı

<!-- Bu SLO'ya bağlı tüketim hızı uyarıları ve eşikleri. -->
```

## Risk kaydı girdisi

```markdown
## Risk: [Kısa risk başlığı]

- Risk kimliği: [KİMLİK]
- Bildirilme tarihi: [YYYY-AA-GG]
- Sahip: [bu riski yönetmekten sorumlu ad ya da rol]
- Kategori: [güvenlik | operasyonel | uyum | finansal | teslimat | tedarikçi]
- Durum: [Açık | Azaltılıyor | Kabul edildi | Kapatıldı]

### Tanım

<!-- Riski şöyle belirtin: neden -> olay -> sonuç. Ne olabileceği ve
     neden önemli olduğu. -->

### Değerlendirme

- Olasılık: [Düşük | Orta | Yüksek]
- Etki: [Düşük | Orta | Yüksek]
- Genel derecelendirme: [olasılık x etkiden türetilmiş]

### Mevcut kontroller

<!-- Bugün bu riski zaten azaltan şeyler. -->

### Azaltım planı

<!-- Olasılığı ya da etkiyi azaltmak için sahipleri ve tarihleriyle
     planlanan eylemler. Riski kabul ediyorsanız, kimin ve neden kabul
     ettiğini kaydedin. -->

| Eylem | Sahip | Bitiş tarihi | Durum |
|-------|-------|--------------|-------|
| [eylem] | [ad] | [tarih] | [durum] |

### Gözden geçirme

- Sonraki gözden geçirme tarihi: [YYYY-AA-GG]
- Karar / notlar: [kabul onayı ya da değişiklik]
```

## Proje tek sayfası / ürün özeti

```markdown
# [Proje ya da ürün adı]: tek sayfa

- Sponsor: [ad]
- Lider: [ad]
- Tarih: [YYYY-AA-GG]
- Durum: [Fikir | Onaylandı | Devam ediyor | Yayımlandı]

## Sorun

<!-- Tek paragraf: müşteri ya da iş sorunu ve bunun gerçek ve çözmeye
     değer olduğuna dair kanıt. -->

## Hedef kitle

<!-- Bu sorun kimde var ve çözülmesinden kim yararlanır. -->

## Önerilen çözüm

<!-- Neyi inşa edeceğimizin ya da değiştireceğimizin kısa tanımı.
     Uygulama ayrıntısı değil, niyet düzeyinde tutun. -->

## Neden şimdi

<!-- Bunu daha sonra değil de şimdi yapmanın nedeni. -->

## Başarı ölçütleri

<!-- İşe yaradığını nasıl anlayacağız. Ölçülebilir sonuçları tercih edin. -->

- [ölçüt ve hedef]

## Kapsam

- Kapsam içi: [yapacaklarımız]
- Kapsam dışı: [yapmayacaklarımız]

## Riskler ve açık sorular

<!-- Başlıca belirsizlikler ve bağımlılıklar. -->

## Kabaca plan ve kilometre taşları

<!-- Üst düzey aşamalar ve yaklaşık zamanlama. -->

## Maliyet ve kaynaklar

<!-- Gereken insan, zaman ve bütçe. -->
```

## Nöbet devir notları

```markdown
# Nöbet devri: [YYYY-AA-GG]

- Devreden: [ad]
- Devralan: [ad]
- Hizmet(ler): [adlar]

## Genel durum

<!-- Tek satır: sakin, gürültülü ya da süren bir sorun. -->

## Açık olaylar

<!-- Sonraki müdahalecinin bilmesi gereken etkin ya da yakın zamanda
     çözülmüş olaylar, bağlantılarıyla. -->

- [olay, durum ve geriye kalanlar]

## Süren ya da planlanan değişiklikler

<!-- Uyarılara yol açabilecek, devam eden dağıtımlar, geçişler, bakım
     pencereleri ya da deneyler. -->

## Gürültülü ya da kararsız uyarılar

<!-- Tetiklenen uyarılar ve gerçek anlamları; böylece bir sonraki kişi
     yanıltılmaz. Geçici susturmaları ve sona erme zamanlarını not edin. -->

## İzlenecek öğeler

<!-- Endişe verici yönde ilerleyen ölçütler ya da sistemler. -->

## Bekleyen takipler

<!-- Sonraki vardiyaya devredilen görevler, biletlere bağlantılarla. -->

## Notlar

<!-- Yararlı başka her şey: erişim tuhaflıkları, tedarikçi sorunları, bağlam. -->
```

## Değişiklik talebi (düzenlemeye tabi değişiklik kontrolü için)

```markdown
# Değişiklik talebi: [Değişiklik başlığı]

- Değişiklik kimliği: [KİMLİK]
- Talep eden: [ad]
- Gönderilme tarihi: [YYYY-AA-GG]
- Tür: [Standart | Normal | Acil]
- Öncelik: [Düşük | Orta | Yüksek]
- Durum: [Gönderildi | Onaylandı | Reddedildi | Uygulandı | Kapatıldı]

## Değişikliğin tanımı

<!-- Neyin değiştiği ve nedeni. Bilete ya da gereksinime atıf yapın. -->

## Etkilenen sistemler ve bileşenler

<!-- Etkilenen hizmetler, veriler, ortamlar ve kullanıcılar. -->

## Gerekçe ve iş etkisi

<!-- Değişikliğin nedeni ve yapılmamasının etkisi. -->

## Risk değerlendirmesi

- Risk düzeyi: [Düşük | Orta | Yüksek]
- Değişiklik başarısız olursa olası etki: [tanım]
- Güvenlik, gizlilik ya da uyum üzerindeki etki: [tanım]

## Uygulama planı

<!-- Sıralı adımlar, sorumlu taraflar ve zamanlama. -->

## Test ve doğrulama planı

<!-- Başarının değişiklikten önce ve sonra nasıl doğrulanacağı. -->

## Geri çekme / geri alma planı

<!-- Başarısız olursa değişikliğin nasıl geri çevrileceği ve kurtarma süresi. -->

## Takvim

- Önerilen pencere: [başlangıç ve bitiş, saat dilimiyle birlikte]
- Beklenen kesinti: [süre ya da yok]

## Onaylar

| Rol | Ad | Karar | Tarih |
|-----|----|-------|-------|
| Değişiklik sahibi | [ad] | [onayla/reddet] | [tarih] |
| Teknik inceleyen | [ad] | [onayla/reddet] | [tarih] |
| Değişiklik danışma kurulu | [ad] | [onayla/reddet] | [tarih] |

## Uygulama sonrası inceleme

<!-- Sonuç, karşılaşılan sorunlar ve geri çekmenin gerekip gerekmediği. -->
```

## Veri Koruma Etki Değerlendirmesi (DPIA) taslağı

```markdown
# Veri Koruma Etki Değerlendirmesi: [İşleme faaliyetinin adı]

- Değerlendirici: [ad]
- Tarih: [YYYY-AA-GG]
- İnceleyenler: [DPO / gizlilik irtibatı]
- Durum: [Taslak | İncelendi | Onaylandı]

## 1. İşlemenin tanımı

<!-- Hangi kişisel verilerin, nasıl, kim tarafından ve hangi amaçla
     işlendiği. Toplamadan silmeye kadar veri akışlarını ekleyin. -->

- Veri sahipleri: [verinin kimler hakkında olduğu]
- Veri kategorileri: [kişisel veri türleri, özel kategorileri not edin]
- Amaçlar: [verinin neden işlendiği]
- Alıcılar ve işleyiciler: [veriyi kimin aldığı ya da ele aldığı]
- Saklama süresi: [verinin ne kadar süre tutulduğu ve silme yöntemi]
- Uluslararası aktarımlar: [varış noktaları ve aktarım mekanizması]

## 2. Gereklilik ve orantılılık

<!-- İşleme amaç için gerekli mi? En az müdahaleci seçenek mi? Hukuki
     dayanak ya da yetki nedir? -->

- Hukuki dayanak / yetki: [her amaç için dayanak]
- Veri minimizasyonu: [her alanın neden gerekli olduğu]
- Doğruluk ve saklama gerekçesi: [notlar]
- Veri sahibi haklarının nasıl desteklendiği: [erişim, silme vb.]

## 3. Danışma

<!-- Danışılan paydaşlar ve ilgili olduğunda veri sahipleri. -->

## 4. Bireyler için riskler

<!-- Gizlilik risklerini belirleyin ve her birini derecelendirin. -->

| Bireyler için risk | Olasılık | Ciddiyet | Genel |
|--------------------|----------|----------|-------|
| [örn. hassas verilere yetkisiz erişim] | [D/O/Y] | [D/O/Y] | [derecelendirme] |

## 5. Riski azaltma önlemleri

<!-- Her risk için azaltım ve sonrasında kalan artık risk. -->

| Risk | Önlem | Artık risk | Kabul eden |
|------|-------|------------|------------|
| [risk] | [kontrol] | [D/O/Y] | [ad] |

## 6. Sonuç ve onay

- Artık risk kabul edilebilir: [Evet | Hayır]
- Önlemleri onaylayan: [ad, rol]
- Denetim makamına danışılması gerekli: [Evet | Hayır]
- Gözden geçirme tarihi: [YYYY-AA-GG]
```
