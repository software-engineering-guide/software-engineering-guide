# 9.3 Olay yönetimi

## Genel bakış ve motivasyon

[Olay yönetimi](https://en.wikipedia.org/wiki/Incident_management), hizmette planlanmamış kesintileri algılama, onlara müdahale etme, onları çözme ve onlardan öğrenme disiplinidir. Önemsiz olmayan her sistem eninde sonunda arızalanır; bu yüzden soru olayların olup olmadığı değil, onları ne kadar iyi yönettiğinizdir. İyi olay yönetimi, kesintilerin etkisini ve süresini küçük tutar, baskı altındaki insanları koordine eder, etkilenenlerle dürüstçe iletişim kurar ve her arızayı kalıcı bir iyileştirmeye çevirir. Operasyonel hazırlığı, net rolleri, sakin iletişimi ve öğrenme kültürünü birleştirir.

Büyük takımlar için olay yönetimi, kurumun karmaşıklığının gerçekten ısırdığı yerdir. Ciddi bir olay; birçok hizmeti, birkaç takımı, yöneticileri, müşterileri, düzenleyicileri ve kamuoyunu aynı anda, zaman baskısı altında ve eksik bilgiyle içine alabilir. Ortak bir yapı olmadan müdahale kaosa düşer: çakışan çaba, birbiriyle çelişen kararlar, paydaşlara karşı sessizlik ve insanları tüketen kahramanlıklar. İyi tanımlanmış bir olay süreci herkese bilinen bir katılım yolu, tek bir doğruluk kaynağı ve net bir karar yetkisi verir; böylece büyük bir grup krizde tutarlı hareket edebilir.

Kurumsal ve kamu alanındaki bahisler yüksektir. Finansal hizmetler, büyük kesintiler için düzenleyici raporlama son tarihleriyle karşılaşır. Sağlık olayları hasta güvenliğini etkileyebilir. Devlet hizmeti arızaları vatandaşların yardımlara erişmesini, vergi beyan etmesini ya da acil hizmetlere ulaşmasını engelleyebilir. Kamusal hesap verebilirlik, kesintilerin görünür ve mercek altında olması demektir. Sürdürülebilir nöbet uygulamaları da bir özen yükümlülüğüdür: yetersiz kadrolu, kötü yönetilen rotasyonlar, sonunda güvenilirliği daha da kötüleştiren [tükenmişliğe](https://en.wikipedia.org/wiki/Occupational_burnout) ve işten ayrılmalara yol açar. Olay yönetimi bu yüzden operasyonel mükemmellik, insan refahı ve kurumsal güvenin buluştuğu yerde durur.

*Ayrıca bakınız:* bölüm 9.1 (site güvenilirliği mühendisliği), bölüm 9.2 (gözlemlenebilirlik ve izleme) ve bölüm 1.1 (mühendislik kültürü: suçlamasız, öğrenme odaklı olay kültürü).

## Temel ilkeler

- **Yapı, kahramanlığı yener.** Tanımlı bir komuta yapısı birçok kişinin eşgüdümüne izin verir; bir avuç kahramana güvenmek ölçeklenmez ve onları tüketir.
- **Unvanlar değil, roller.** Bir olayda olay komutanı ve iletişim sorumlusu gibi net roller, kurumsal rütbeden daha önemlidir.
- **Erken ve sık iletişim kurun.** Paydaşlara sık ve dürüst güncellemeler, haber kötü olsa bile güven inşa eder; sessizlik onu yok eder.
- **Koordinasyonu soruşturmadan ayırın.** Olayı yöneten kişi aynı zamanda başı eğik hata ayıklamamalıdır.
- **Nöbet sürdürülebilir olmalı.** Rotasyonlar, ücretlendirme ve yük sınırları, sistemi koruyan insanları korur.
- **Varsayılan olarak suçlamasız.** İnsanlar bildiklerine göre makul davranır; suçlama gerçek, sistemik nedenleri gizler.
- **Mesele öğrenmektir.** Kalıcı bir iyileştirme üretmeyen bir olay, boşa giden bir acıydı.
- **Kurumsal belleği koruyun.** [Olay sonrası incelemeler](https://en.wikipedia.org/wiki/Postmortem_documentation) ve eylemleri bulunabilir ve yeniden kullanılır olmalı, bir hafta sonra kaybolmamalıdır.

## Öneriler

### Sürdürülebilir nöbet rotasyonları işletin

Nöbeti insancıl ve etkili olacak biçimde tasarlayın. Rotasyonları kimse çok sık nöbette olmayacak kadar büyük tutun, birincil ve ikincil (yükseltme) katman sağlayın ve onaylama ile yanıt süreleri için net beklentiler koyun. Nöbeti, ister ücretle ister izinle, adil biçimde karşılayın ve gerçek iş olarak görün. Vardiya başına uyarı yükünü izleyin ve gürültülü, uykuyu mahveden bir rotasyonu normal değil, yanlış çağrıları keserek düzeltilecek bir hata olarak görün. Mümkün olduğunda zaman dilimleri boyunca güneşi izleyin; böylece insanlar uyanık oldukları saatlerde nöbette olur. Her nöbetçi mühendisin [işletim kılavuzlarına](https://en.wikipedia.org/wiki/Runbook), erişime ve harekete geçme yetkisine sahip olduğundan ve vardiya devirlerinin bağlamı bilinçle aktardığından emin olun.

### Olay komutasını ve ciddiyet düzeylerini oluşturun

Acil durum müdahalesinden esinlenen bir [olay komuta sistemi](https://en.wikipedia.org/wiki/Incident_Command_System) benimseyin. **Olay komutanı** teknik düzeltmenin değil, koordinasyonun ve kararların sahibidir. Görev devreder, eylemleri izler ve müdahaleyi akışta tutar. Destekleyici roller arasında uygulamalı soruşturmayı yöneten bir **operasyon ya da teknik lider**, iç ve dış güncellemeleri yürüten bir **iletişim sorumlusu** ve zaman çizelgesini kaydeden bir **kâtip** vardır. **Ciddiyet düzeylerini** (örneğin kritik, yaygın ya da güvenliği etkileyen kesintiler için SEV1'den küçük sorunlar için SEV3'e) net ölçütlerle tanımlayın; çünkü ciddiyet, kimin çağrılacağını, ne kadar hızlı çağrılacağını ve kurumun ne kadarının seferber olacağını belirler. Herkes bir olay ilan edebilmeli ve ilan etmekten yana yanılmalısınız.

### Olaylar sırasında iç ve kamusal iletişim kurun

Doğruluk kaynağı olarak tek bir koordinasyon kanalı kurun ve güncelleme yalnızca "hâlâ araştırılıyor" olsa bile güncellemeleri sabit bir ritimle paylaşın. İçeride, müdahale edenler yarıda kesilmesin diye yönetimi ve etkilenen takımları iletişim sorumlusu aracılığıyla bilgilendirin. Dışarıda bir durum sayfası ve önemli olaylar için etki ve beklenen çözüm konusunda dürüst, aşırı söz vermeyen müşteri ya da kamu bildirimleri kullanın. Düzenlenen ve kamu hizmetlerinde zorunlu raporlama yükümlülüklerinizi ve son tarihlerinizi önceden bilin ve şablonları hazır tutun. Amaç, paydaşların sizden her zaman söylentilerden daha fazlasını duymasıdır.

### Suçlamasız olay sonrası incelemeler yapın ve düzeltici eylemleri yürütün

Her önemli olaydan sonra **suçlamasız bir olay sonrası inceleme** yazın: olgusal bir zaman çizelgesi, etki, katkıda bulunan etkenler, neyin iyi gittiği, neyin kötü gittiği ve nerede şanslı olduğunuz. Suçlamasız olmak, kimin cezalandırılacağına değil, sistemin ve sürecin arızaya nasıl izin verdiğine odaklanmak demektir; çünkü dürüst anlatımları ve gerçek öğrenmeyi üreten şey [psikolojik güvenliktir](https://en.wikipedia.org/wiki/Psychological_safety). Her olay sonrası inceleme, sahipleri ve bitiş tarihleri olan, gelecekteki riske etkisine göre önceliklendirilmiş **düzeltici eylemler** üretir. Bunları normal mühendislik iş listesinde tamamlanana kadar izleyin. Eylemleri hiç bitmeyen bir olay sonrası inceleme, tiyatrodan ibarettir.

### Olaylardan öğrenin ve kurumsal bellek oluşturun

Tek tek olay sonrası incelemeler gereklidir ama tek başlarına yetmez. Yinelenen temaları, sistemik zayıflıkları ve yapısal bir düzeltmeyi hak eden arıza sınıflarını bulmak için olayları toplu olarak gözden geçirin. Dersler takım sınırlarını aşsın diye olay sonrası incelemeleri aranabilir yapın ve geniş paylaşın. Öğrendiklerinizi işletim kılavuzlarına, eğitime, mimari incelemelere ve üretim hazırlığı çıtalarına geri besleyin. Müdahaleyi prova eden ve gerçek bir olay boşlukları ortaya çıkarmadan önce onları yüzeye çıkaran dönemsel güvenilirlik incelemelerini ve oyun günlerini ya da [kaos tatbikatlarını](https://en.wikipedia.org/wiki/Chaos_engineering) düşünün. Olay birikiminizi, zor kazanılmış operasyonel bilgiyi yakalayan stratejik bir varlık olarak görün.

## Ödünleşimler: artılar ve eksiler

| Karar | Artılar | Eksiler |
|---|---|---|
| Resmi olay komutası | Koordineli, ölçeklenebilir müdahale | Küçük olaylar için ek yük |
| İlan etmek için düşük çıta | Sorunları erken yakalar | Ara sıra yanlış alarm |
| Herkese açık durum şeffaflığı | Güven inşa eder, söylentiyi azaltır | Arızaları açığa çıkarır, mercek çeker |
| Suçlamasız olay sonrası incelemeler | Dürüst öğrenme, güvenlik | Yanlış kullanılırsa hesap verebilirlik yokmuş gibi hissettirebilir |
| Büyük nöbet rotasyonları | Sürdürülebilir, daha az tükenmişlik | Daha çok eğitilmiş personel gerekir, bağlamı seyreltir |

Merkezi ödünleşim, süreç yükü ile koordinasyon faydası arasındadır. Ağır bir olay yapısı, birçok takımı kapsayan bir SEV1'de paha biçilmezdir ama küçük bir aksama için gereğinden fazladır; bu yüzden süreci ciddiyete göre ayarlayın. Şeffaflık, kısa vadeli utancı uzun vadeli güvenle takas eder. Kesintiler sırasında açıkça iletişim kuran kurumlar, genellikle susanlardan daha fazla iyi niyet korur. Suçlamasızlık bazen hesap verebilirlik eksikliği olarak yanlış okunur, ama talep ettiği hesap verebilirlik kolektif ve sistemiktir: takım, arızaya izin veren koşulları düzeltmenin sahibidir ve bu, bir bireyi günah keçisi yapmaktan çok daha iyi çalışır.

## Takımınızla tartışılacak sorular

1. **Kaç kişi olay komutanı olarak bir olayı yönetebilir ve üst düzey yönetici olmayan üç kişinin adını verebilir misiniz?** Her olayı kurtarmak için bir ya da iki kahramana bağlı olmak kırılgandır ve onların tükenmesini garanti eder; olay komutanı rolü teknik rütbeyle değil koordinasyonla ilgilidir, bu yüzden her seferinde aynı kıdemli kişilere varsayılan olarak düşmemelidir. Tartışmaya listeyi getirin: komutan rolünü üstlenmek üzere eğitilmiş herkesi ve en son ne zaman gerçekten bir olay yönettiklerini sıralayın. Büyük bir kurumda ciddi bir olay sabaha karşı 3'te birçok takıma yayılabilir ve uyuyan tek bir uzman değil, her zaman diliminde hazır eğitimli bir komutana ihtiyacınız vardır. Beceri yayılsın diye rolü döndürün ve yeni komutanları oyun günlerinden geçirin. Yanıt, müdahalenizin kurumla ölçeklenip ölçeklenmediğini ya da en iyi kişiniz ulaşılamaz olduğu anda çöküp çökmediğini söyler.

2. **Zorunlu kesinti raporlama son tarihlerinizi biliyor musunuz ve şablonlar ile sahipler bir sonraki SEV1'den önce hazır mı?** Finansal hizmetler büyük kesintiler için düzenleyici raporlama son tarihleriyle karşılaşır, sağlık olayları hasta güvenliğine dokunur ve devlet arızaları vatandaşların yardımlara ya da acil hizmetlere erişimini engeller; bu yüzden kaçırılan bir raporlama penceresi teknik bir kesintiyi hukuki bir soruna çevirir. Bir SEV1'in ortası, bir düzenleyiciyi bilgilendirmek için dört saatiniz olduğunu ve şablonunuzun olmadığını keşfetmek için en kötü andır. Gerçek yükümlülükleri getirin: hangi düzenleyiciler, hangi eşikler bir rapor tetikler, son tarih nedir ve dosyalamaya kim yetkilidir. Müdahale edenler bir başvuru taslağı yazmak için asla düzeltmeden çekilmesin diye bunu önceden iletişim sorumlusu rolüne atayın. Yanıt; hazır şablonlar, adı konmuş bir sahip ve raporlama saatini otomatik olarak başlatan bir ciddiyet düzeyi üretmelidir.

3. **Büyük bir olayı en son ne zaman bir oyun günüyle prova ettiniz ve bu hangi boşluğu ortaya çıkardı?** Oyun günleri ve kaos tatbikatları müdahaleyi prova eder ve gerçek bir olay boşlukları ortaya çıkarmadan önce onları yüzeye çıkarır; bu bölümdeki olgun son durum, baskı altında uydurulan değil, pürüzsüz, iyi prova edilmiş müdahaledir. Hiç uygulanmamış bir plan kırık varsayımları gizler: eskimiş işletim kılavuzları, eksik erişim, çıkmaz sokağa varan bir yükseltme yolu, kimsenin güncelleyemediği bir durum sayfası. Son tatbikatın bulgularını getirin; hiç tatbikat yapılmadıysa bunu bulgu sayın. Kesintilerin kamuca mercek altına alındığı kurumsal ve kamu sistemlerinde prova, vatandaşların ve düzenleyicilerin önünde doğaçlama yapmak yerine yetkinliğinizi gösterme yoludur. Yanıt, oyun günleri için bir ritim belirlemeli ve ortaya çıkan her boşluğu işletim kılavuzlarına, erişim incelemelerine ve üretim hazırlığı çıtalarına geri beslemelidir.

4. **En yoğun rotasyonunuzdaki gerçek uyarı yükü nedir ve o çağrı cihazını kendiniz taşımaya razı olur muydunuz?** Gürültülü, uykuyu mahveden bir rotasyon bir onur nişanı değil, bir hatadır; uyarı yorgunluğu da müdahale edenlerin gerçek acil durumu kaçırdığı ya da geç onayladığı yerdir, bu yüzden insancıl soru ile güvenilirlik sorusu aynı sorudur. Rakip baskı şudur: çağrıları kesmek uyanıklığı düşürmek gibi hissettirir, oysa pratikte bir yanlış çağrı seli onu çok daha fazla düşürür. Rakamları getirin: vardiya başına çağrı, kaçının mesai saati dışında tetiklendiği, kaçının eyleme dönüştürülebilir olduğu ve önemli olanlar için onaylama süreleri. Vardiya başına çağrılar için açık bir tavan koyun ve onu aşan her rotasyonu, uyarıları ayarlayarak ya da silerek düzeltilecek iş olarak görün. Büyük ya da kamu kuruluşunda sürdürülebilir nöbet bir özen yükümlülüğü ve bir elde tutma kaldıracıdır; çünkü yeri doldurulamaz sistem bilgisini taşıyan deneyimli mühendisler, acımasız bir rotasyonun tam da uzaklaştırdığı kişilerdir ve o bilgiyi yeniden kurmak rotasyonu insancıl biçimde kadrolamaktan çok daha pahalıdır.

5. **Geçen çeyreğin düzeltici eylemlerinin ne kadarı gerçekten bitti ve bitmediğinde hesap verecek olan kim?** Eylemleri hiç tamamlanmayan bir olay sonrası inceleme aynı olayı yeniden üretir; bu yüzden gerçek öğrenmeyi tiyatrodan ayıran disiplin, yazıların iyi okunup okunmaması değil, düzeltmelerin sevk edilip edilmemesidir. Gerilim şudur: düzeltici eylemler aynı iş listesinde özellik işiyle yarışır ve adı konmuş bir sahip, bir bitiş tarihi ve bir inceleme ritmi olmadan her önceliklendirme kavgasını sessizce kaybeder. Defteri getirin: son olay sonrası incelemelerden her eylem, sahibi, bitiş tarihi ve durumu, ayrıca bir düzeltme tıkandığı için yinelenen olayların sayısı. Bunları normal mühendislik iş listesinde izleyin ve tamamlanmayı bir temel çizgiye karşı metrik olarak gözden geçirin; böylece yaşlanan ya da bırakılan eylemler kaybolmak yerine yüzeye çıkar. Kurumsal ve kamu ortamlarında raporlanan bir kesintiden sonra tamamlanmamış bir düzeltici eylem, bir denetçinin ya da gözetim kurumunun üzerine atladığı türden bir bulgudur; bu yüzden tamamlanma hem bir mühendislik güvencesi hem de gösterilebilir hesap verebilirlik meselesidir.

6. **Herkes bir olayı erken ilan etmekte ve olay sonrası incelemede dürüstçe konuşmakta kendini güvende hissediyor mu, yoksa suçlanma korkusu onları yavaşlatıyor mu?** Suçlamasız kültür, sistemik nedenleri ortaya çıkaran dürüst anlatımları üretir ve ilan için düşük çıta, sorunları küçükken yakalar; yani ikisi de insanların el kaldırmanın aleyhlerine kullanılacağından korkmamasına bağlıdır. Rakip endişe, suçlamasızlığın hesap verebilirlik eksikliği gibi okunmasıdır; ama talep ettiği hesap verebilirlik kolektiftir: takım, en son dokunanı günah keçisi yapmak yerine arızaya izin veren koşulları düzeltmenin sahibidir. Gerçekten gözlemleyebileceğiniz kanıt getirin: olayların ne kadar çabuk ilan edildiği ile sorunların önce ne kadar kaynadığı, genç mühendislerin hiç ilan edip etmediği ve olay sonrası incelemelerin katkıda bulunan koşulları mı adlandırdığı yoksa sessizce bir kişiyi mi. Büyük ya da kamusal bir kurumda psikolojik güvenlik kırılgandır ve suçlamaya dayalı tek bir inceleme ya da habere cezalandıran tek bir lider tarafından kolayca bozulur; bu yüzden insanların süreci dolanıyor olduğu sinyaline dikkat edin ve dürüst erken ilanı yönetilecek bir risk olarak değil, korunacak bir davranış olarak görün.

## Sektör merceği

**Girişim.** Bir avuç mühendisiniz varsa ve boş kaynağınız yoksa süreci tek sayfada tutun: kim fark ederse ilan eder, bir kişi koordine eder, bir kişi araştırır, bir kişi müşterilere söyler ve başka kimse üretime dokunmaz. Resmi ciddiyet katmanlarını ve kadrolayamayacağınız özel rolleri atlayın, ama suçlamasız tek sayfalık yazıyı mutlaka yazın; çünkü sizin büyüklüğünüzde tek bir yinelenen arıza sizi batırabilir. Koordinasyon araçları kurmak yerine barındırılan bir durum sayfasına ve çağrı aracına yaslanın.

**Küçük işletme.** Özel bir güvenilirlik uzmanınız yok ve bütçeniz kısıtlı; bu yüzden kendi araçlarınızı kurmak yerine zaten ödediğiniz izleme ve çağrı hizmetlerine gömülü olay araçlarını satın alın. Nöbeti, sistemi anlayan bir ya da iki kişiyi tüketmesin diye net, insancıl sınırlarla ortak bir görev olarak görün. Kısa olay sonrası incelemeler yazın ve düzeltmeleri gerçekten tamamlayın; çünkü küçük bir takımda tekrarlayan bir kesinti, kolayca yerini dolduramayacağınız müşterilere mal olur.

**Kurumsal.** Zorluk, baskı altında birçok takımı koordine etmektir; bu yüzden hizmetleri kapsayan bir SEV1 parçalanmasın diye bir olay komuta sistemini, ortak ciddiyet ölçütlerini ve tek bir doğruluk kaynağını standartlaştırın. Her zaman diliminde eğitilmiş komutanlara yatırım yapın, olay sonrası incelemeleri aranabilir bir kurumsal belleğe toplayın ve düzeltici eylemleri sahipler ve denetim izleriyle tamamlanana kadar yönetin. Hiçbir rotasyon sessizce insanlık dışı hale gelmesin diye nöbet yükünü filo genelinde bir metrik olarak yönetin.

**Kamu.** Satın alma kuralları, şeffaflık ve kamusal hesap verebilirlik müdahaleyi şekillendirir. Zorunlu kesinti raporlama son tarihlerinizi ve eşiklerinizi önceden bilin, başvuru şablonlarını ve adı konmuş yetkili bir sahibi hazır tutun ve vatandaşlar asla tahmin yürütmek zorunda kalmasın diye dürüst durum güncellemeleri ve çağrı merkezi metinleri yayımlayın. Olay sonrası incelemeleri kurum genelinde paylaşın, zirve dönemleri için dayanıklılık planlamasını beslemelerini sağlayın ve geçmiş olayların kaydını, arızaların kalıcı düzeltmeler ürettiğine dair gözetim kurumlarına gösterebileceğiniz kanıt olarak görün.

## Örnekler

**Girişim.** Altı kişilik bir girişim, API'sinin hata döndürdüğünü görerek uyanıyor ve herkes aynı anda aynı sohbet dizisine doluyor. Kaostan yanan ekip, olay temellerinin tek sayfasını yazıyor: kim fark ederse olayı ilan eder ve koordinatör olur, bir kişi araştırır, bir kişi müşterilere sade bir güncelleme yazar ve başka kimse üretime dokunmaz. Bir sonraki kesinti sakin geçiyor ve kırk dakikada çözülüyor. Kısa bir suçlamasız yazı, yedekleme adımı olmadan çalışmış bir geçişi buluyor ve takım bu denetimi aynı gün dağıtım betiğine ekliyor.

**Kurumsal.** Büyük bir hizmet olarak yazılım sağlayıcısı, mesai saatlerinde kısmi bir kesintiyle karşılaşıyor. Nöbetçi mühendis bir SEV1 ilan ediyor ve bir olay komutanı koordinasyonu devralırken teknik lider araştırıyor, iletişim sorumlusu da herkese açık durum sayfasına yirmi dakikada bir güncelleme yazıyor. Yöneticiler müdahale edenleri yarıda kesmek yerine bir yönetim kanalını izliyor. Hizmet doksan dakikada geri geliyor. Ertesi haftaki suçlamasız bir olay sonrası inceleme, bir dağıtım işlem hattında eksik bir güvence buluyor ve sahipleri olan üç düzeltici eylem üretiyor. Sonraki toplu inceleme, bunun o çeyrekteki dağıtımla ilgili üçüncü olay olduğunu gösteriyor; bu da daha güvenli sürümlere yapısal bir yatırım tetikliyor.

**Kamu.** Bir yardım kurumunun ödeme sistemi yoğun bir günde arızalanıyor ve vatandaşların destek almasını engelliyor. Kurumun olay süreci bir komutanı, teknik müdahale edenleri ve kamuya mesajları koordine eden ve büyük kesintileri sabit bir pencerede raporlama yönündeki düzenleyici gerekliliği karşılayan bir iletişim sorumlusunu seferber ediyor. Bir durum sayfası ve çağrı merkezi metinleri vatandaşları ve personeli bilgili tutuyor. Kurum genelinde paylaşılan suçlamasız olay sonrası inceleme dersleri işletim kılavuzlarına ve bir üretim hazırlığı incelemesine akıtıyor; geçmiş olaylar birikimi de zirve dönemleri için bir sonraki yılın kapasite ve dayanıklılık planlamasına bilgi veriyor.

## İş gerekçesi: motivasyonlar, YG ve TSM

Olgun olay yönetiminin getirisi, olay başına azalan etki ve daha az tekrarlayan olay olarak görünür. Daha hızlı, daha iyi koordine edilmiş bir müdahale kesintileri kısaltır; bu da geliri, cezaları ve onarım maliyetini doğrudan korur. Disiplinli olay sonrası incelemeler ve düzeltici eylemler, tüm arıza sınıflarını istikrarla ortadan kaldırır; böylece olay oranı zamanla düşer. Sürdürülebilir nöbet, değiştirilmesi pahalı olan ve yeri doldurulamaz sistem bilgisi taşıyan deneyimli mühendisler arasındaki tükenmişliğin ve işten ayrılmanın büyük, çoğu zaman gizli maliyetini azaltır.

Benimseme maliyetleri faydanın yanında mütevazıdır: olay komutası eğitimi, koordinasyon ve durum iletişimi için araçlar, olay sonrası incelemelere harcanan zaman ve insancıl rotasyonlar için gereken kadro. Benimsememenin maliyeti ağır ve yinelenendir: kesintileri uzatan kaotik müdahaleler, müşteri ve kamu güvenini aşındıran sessizlik, kaçırılan raporlama için düzenleyici cezalar, kimsenin bitirmediği eylemlerden tekrarlayan olaylar ve moralsiz bir nöbet kadrosu. Gerekçeyi yönetime sunmak için son olayları süre ve etkiye göre sayısallaştırın, koordinasyonun ve tamamlanmış düzeltici eylemlerin onları nasıl kısaltacağını ya da tekrarını nasıl önleyeceğini gösterin ve sürdürülebilir nöbeti şımartma değil, elde tutma ve risk yönetimi olarak çerçeveleyin.

## Anti-kalıplar ve tuzaklar

- **Kahraman kültürü.** Her olayı kurtarmak için bir ya da iki kişiye bağımlı olmak kırılgandır ve onların tükenmesini garanti eder.
- **Net bir komutan yok.** Koordinasyonun sahibi biri olmadan müdahale edenler işi tekrarlar, çelişir ve zaman çizelgesini kaybeder.
- **Susmak.** Bir kesinti sırasında güncellemeleri esirgemek söylentiyi, paniği ve kalıcı güvensizliği doğurur.
- **Suçlama oyunları.** Bireyleri cezalandırmak dürüstlüğü yeraltına iter ve düzeltmeniz gereken sistemik nedenleri gizler.
- **Olay sonrası inceleme tiyatrosu.** Düzeltici eylemleri hiç tamamlanmayan olay sonrası incelemeler yazmak aynı olayı yeniden üretir.
- **Uyarı yorgunu nöbet.** Gürültülü rotasyonlar müdahale edenleri tüketir; böylece gerçek acil durumu kaçırırlar ya da geç onaylarlar.
- **Ciddiyet karmaşası.** Tanımsız ya da tutarsız uygulanan ciddiyet düzeyleri, ciddi olaylara yetersiz, önemsizlere aşırı müdahaleye yol açar.

## Olgunluk modeli

**Düzey 1, Başlangıç.** Olaylar, fark eden kim varsa tarafından plansız ele alınır ve müdahale reaktif ve doğaçlamadır. Tanımlı roller, ciddiyet düzeyleri ya da olay sonrası incelemeler yoktur. Nöbet, varsa bile gayriresmi ve stresli; kalıcı hiçbir şey öğrenilmediği için aynı arızalar yinelenir.

**Düzey 2, Geliştirme.** Temel nöbet rotasyonları ve ciddiyet tanımları vardır ve bazı olaylar için olay sonrası inceleme yapılır, ama uygulama takımlar arasında tutarsızdır. Müdahale sırasında roller belirsizdir, bir takım disiplinli bir olay yürütürken sonraki kaosa sürüklenebilir ve düzeltici eylemler varsa gelişigüzel izlenir.

**Düzey 3, Standartlaştırma.** Net rolleri ve ciddiyet ölçütleri olan resmi bir olay komuta sistemi belgelenmiş ve kurum genelinde tutarlı biçimde kullanılır. Önemli olaylar için suçlamasız olay sonrası incelemeler standarttır, düzeltici eylemler sahipleri ve bitiş tarihleriyle kaydedilir, nöbet karşılanır ve tek bir koordinasyon kanalı ile durum sayfası uygulaması her takıma bırakılmak yerine kurum genelinde uygulanır.

**Düzey 4, Yönetme.** Olay programı temel çizgilere karşı ölçülür ve kontrol edilir. Algılama süresini, onaylama süresini, çözme süresini, vardiya başına çağrıyı, düzeltici eylem tamamlanma oranını ve tekrarlayan olay oranını izler ve gerilemeleri yakalamak için bu metrikleri bir ritimle gözden geçirirsiniz. Ciddiyet düzeyleri verinin güvenilir olacağı kadar tutarlı uygulanır, uyarı yükü açık bir tavanın altında tutulur ve olaylar sırasında ve sonrasında git ya da gitme kararları içgüdüyle değil kanıtla yönlendirilir.

**Düzey 5, Orkestrasyon.** Olay yönetimi sürekli iyileştirilir ve kurum genelinde bütünleşmiştir. Müdahale düzenli oyun günleriyle pürüzsüz ve iyi provalıdır, toplu analiz tüm arıza sınıflarını ortadan kaldıran yapısal yatırımı yönlendirir ve olay sonrası incelemeler işletim kılavuzlarını, eğitimi, mimari incelemeleri ve kapasite planlamasını besleyen aranabilir bir kurumsal bellek oluşturur. Sistem büyüdükçe uyum sağlar ve olay oranı ile etkisi zamanla düşer.

## Tartışma fikirleri

- Ciddiyet düzeylerinizi hangi ölçütler ayırt ediyor ve herkes onları tutarlı biçimde uyguluyor mu?
- Sistem büyürken sürekli insan eklemeden nöbeti nasıl sürdürülebilir tutarsınız?
- Canlı bir olay sırasında yük devretme ya da geri alma gibi maliyetli kararları verme yetkisi kimde?
- Bir kesinti sırasında müşterilere ve kamuoyuna ne kadar şeffaf olmalısınız ve sınırlar nerede?
- Düzeltici eylemlerin bir iş listesinde çürümek yerine gerçekten tamamlanmasını nasıl sağlarsınız?
- Olay sonrası inceleme koleksiyonunuzu gerçekten yeniden kullanılabilir bir kurumsal belleğe dönüştürmek için ne gerekir?

## Önemli çıkarımlar

- Her sistem arızalanır; olgunluk, tüm olaylardan kaçınmakla değil, ne kadar iyi müdahale edip öğrendiğinizle ölçülür.
- Tanımlı rolleri ve ciddiyet düzeyleri olan net bir olay komuta yapısı, büyük grupların baskı altında eşgüdüm sağlamasına izin verir.
- İç ve dış paydaşlarla erken, sık ve dürüstçe iletişim kurun; sessizlik güveni yok eder.
- Nöbeti adil rotasyonlar, ücretlendirme ve gürültülü uyarıların amansız azaltılmasıyla sürdürülebilir tutun.
- Sahipli, izlenen düzeltici eylemler üreten suçlamasız olay sonrası incelemeler yapın ve onları tamamlayın.
- Toplu öğrenme ve aranabilir kurumsal bellek, tekil olayları kalıcı iyileştirmeye dönüştürür.

## Kaynaklar ve ileri okuma

- Betsy Beyer et al., *Site Reliability Engineering* (chapters on incident management and postmortems)
- Betsy Beyer et al., *The Site Reliability Workbook* (on-call and incident response practices)
- John Allspaw, *Blameless PostMortems and a Just Culture* (Etsy engineering)
- Sidney Dekker, *The Field Guide to Understanding Human Error*
- Charles Perrow, *Normal Accidents: Living with High-Risk Technologies*
- U.S. Federal Emergency Management Agency, *Incident Command System (ICS)* reference materials
- PagerDuty, *Incident Response Documentation* (open-sourced practices)
