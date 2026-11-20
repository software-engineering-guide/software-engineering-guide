# 1.4 Çalışma biçimleri

## Genel bakış ve motivasyon

"Çalışma biçimleri", takımınızın gündelik olarak gerçekte nasıl eşgüdüm sağladığını, planladığını, iletişim kurduğunu ve teslim ettiğini tarif eder. İş nasıl parçalara bölünür? Kim kiminle ve ne zaman konuşur? İlerleme nasıl izlenir ve kararlar ile bilgi nasıl akar?

Çoğu kuruluş adı konmuş bir metodoloji, [Scrum](https://en.wikipedia.org/wiki/Scrum_(software_development)), [Kanban](https://en.wikipedia.org/wiki/Kanban_(development)) ya da bir ölçekleme çerçevesi benimser ve törenlerin altındaki değerle aynı şey olduğunu varsayar. Aynı değildir. Yazılım teslimatını dönüştüren metodolojiler, ağır, devir odaklı süreçlere karşı tepkiydi. Amaçları hızlı geri bildirim, küçük partiler ve yetkilendirilmiş takımlardı. Yalnızca ritüelleri, günlük toplantıları, sprintleri, hikaye puanlarını ilkeler olmadan benimserseniz, sürecin maliyetlerini faydaları olmadan elde edersiniz: [kargo kültü](https://en.wikipedia.org/wiki/Cargo_cult) çevikliği.

Büyük takımlar için iyi niyetlerin başarılı ya da başarısız olduğu yer burasıdır. Bin mühendis aynı odada olamaz, aynı toplantıya katılamaz ya da aynı örtük bağlamı paylaşamaz. Büyüdükçe toplantılara ve koridor sohbetlerine değil, yazılı iletişime, eşzamansız iş birliğine ve hafif eşgüdüme daha çok yaslanmanız gerekir. Ölçek fiziği değiştirir. Birlikte oturan sekiz kişi için harika çalışan uygulamalar, dağıtık seksen kişi için çökebilir. Bunu düzeltmeyi vaat eden ölçekleme çerçeveleri ise çoğu zaman [çevikliğin](https://en.wikipedia.org/wiki/Agile_software_development) kaldırmayı amaçladığı devirleri ve merkezileşmeyi yeniden getirir.

Kurumsal ve kamu kuruluşları bu baskıların her birini tam güçle hisseder. Birçok zaman dilimine yayılırlar, kadrolu personeli yüklenici ve tedarikçilerle harmanlarlar ve çoğu zaman zorunlu aşama kapıları ve raporlama taşırlar. Burada belge öncelikli, eşzamansız, çıktı odaklı bir çalışma biçimi bir nezaket değildir. Ölçeklenen tek şeydir. Aşağıdaki öneriler, çerçeveleri toptan ithal etmek yerine ilkeleri bağlama uyarlamayı ve büyük, dağıtık, karma iş gücünün gerçekten iş birliği yapmasını sağlayan yazılı, eşzamansız, şeffaf uygulamaları tercih eder.

## Temel ilkeler

- Ritüelleri değil ilkeleri benimseyin; bir uygulamayı kopyalamadan önce neden var olduğunu anlayın.
- Küçük partiler ve hızlı geri bildirim, büyük planları ve uzun döngüleri yener.
- Uygun olduğu yerde katı zaman kutulamaya göre akışı (yarım kalan işi sınırlamayı) tercih edin.
- Konuşmayı ve planlamayı mümkün kılmak için tahmin edin, sahte kesinlik üretmek için değil.
- Varsayılan olarak eşzamansız, yazılı iletişimi kullanın; eşzamanlı zamanı gerçekten ihtiyaç duyanlara saklayın.
- İşi ve kararları görünür ve belgelenmiş kılın ki herkes toplantısız yetişebilsin.
- Yapılan faaliyeti ya da kullanılan kapasiteyi değil, teslim edilen çıktıları optimize edin.

## Öneriler

### Çevikliği, Scrum'ı, Kanban'ı ve Lean'i bağlama uyarlayın

Bunları bir din değil, bir alet çantası olarak ele alın. Scrum'ın zaman kutulu sprintleri, düzenli bir planlama ve gözden geçirme ritminden yararlanan keşif işi olan takımlara uyar. Kanban'ın sürekli akışı ve açık yarım kalan iş sınırları, platform ve operasyonlar gibi öngörülemeyen, kesinti güdümlü işi olan takımlara uyar. [Lean](https://en.wikipedia.org/wiki/Lean_software_development)'in israfı ortadan kaldırma ve bekleme süresini kısaltma odağı ikisinin de temelinde yatar. Bilinçli seçin. Yardımcı olduğu yerde karıştırın; birçok takım "[Scrumban](https://en.wikipedia.org/wiki/Scrumban)" çalıştırır. Değer yaratan uygulamaları tutun ve boş ritüele dönüşen törenleri bırakın. Herhangi bir uygulamanın testi basittir. Geri bildirimi kısaltıyor, parti boyutunu azaltıyor ya da netliği artırıyor mu? Değilse, sorgulayın.

### Dikkatle ölçekleyin, kargo kültüyle değil

Ölçekleme çerçeveleri, [SAFe](https://en.wikipedia.org/wiki/Scaled_agile_framework) (Scaled Agile Framework), LeSS (Large-Scale Scrum), popülerleştirilmiş "Spotify modeli", birçok takımı eşgüdümlemeyi vaat eder. Onlara şüpheci bir gözle yaklaşın. SAFe yapı getirir ve kapsamlılığı ve eğitim ekosistemi nedeniyle büyük kurumsal ve kamu kuruluşları tarafından sıkça seçilir, ancak çevikliği baltalayan ağır planlamayı, hiyerarşiyi ve devirleri yeniden getirebilir. LeSS, lean ilkelere daha yakın kalır ama gerçek bir örgütsel değişiklik talep eder. Spotify "modeli" bir şirketin evrilen kültürünün anlık görüntüsüydü, asla bir şablon değildi ve Spotify bile onu insanların hayal ettiği gibi işletmedi. Ölçeklemeyi, parçalanmış bir yapıya bir eşgüdüm çerçevesi vidalamak yerine, önceki bölümdeki takım topolojileri aracılığıyla eşgüdüm ihtiyacını azaltarak yapmayı tercih edin.

### Dürüstçe ve hafifçe tahmin edin

Hikaye puanları ve hız, takımınızın kendi yakın vadeli işini planlamasına ve göreli karmaşıklık hakkında konuşmasına yardımcı olur. Bir verimlilik metriği, takımlar arası bir para birimi ya da bir söz değildir. Hızı asla bir hedefe çevirmeyin: puan enflasyonuyla oyunlaştırılacaktır. Daha uzun vadeli tahmin için, çoğu zaman tahminleri toplamaktan daha doğru olan verimi saymayı ve geçmiş döngü süresi verilerini kullanmayı tercih edin. Birçok olgun takım, işi benzer küçüklükte parçalara bölüp onları saymak yoluyla tahmin yükünü keser. Yöntem ne olursa olsun, tahminlerin belirsizlik altındaki öngörüler olduğunu, taahhüt olmadığını unutmayın. Onları aralıklar olarak iletin.

### Varsayılan olarak eşzamansız, belge öncelikli iletişimi kullanın

Büyük, dağıtık kuruluşlarda eşzamanlı toplantılar ölçeklenmez ve başka zaman dilimlerindeki insanları dışarıda bırakır. Yazıyı varsayılan yapın: tasarım belgeleri, [karar kayıtları](https://en.wikipedia.org/wiki/Architectural_decision), yazılı durum güncellemeleri ve canlı bir konuşma olmadan harekete geçmeye yetecek bağlam taşıyan kapsamlı biletler. Kaçınamadığınız toplantıları kaydedin ve özetleyin. Belge öncelikli bir kültür, başka bir zaman dilimindeki birinin tam katkı vermesine, yeni katılanların ve yüklenicilerin okuyarak uyum sağlamasına izin verir ve kalıcı bir kayıt bırakır. Eşzamanlı zamanı gerçek iş birliği, ilişki kurma ve belirsizliği hızla gidermek için saklayın. Büyük odaklanma bloklarını toplantı parçalanmasından koruyun.

### Zaman dilimleri, yükleniciler ve tedarikçiler arasında iyi çalışın

Dağıtık ve karma iş gücü, ölçekte normdur. Devirlerin sözlü değil, yazılı ve eksiksiz olduğu "[güneşi takip et](https://en.wikipedia.org/wiki/Follow-the-sun)" için tasarım yapın. İhtiyaç duyduğunuz eşzamanlı temas için birkaç örtüşen çekirdek saat belirleyin ve uygunsuz toplantı saatlerinin yükünü her zaman aynı bölgeye yüklemek yerine adil paylaşın. Yükleniciler ve tedarikçiler için yazılı bağlama, net arayüzlere ve paylaşılan araçlara ekstra yatırım yapın, çünkü kadrolu çalışanlarınızın biriktirdiği örtük bilgiden yoksundurlar. Tedarikçileri ayrı, opak bir kanalla yönetmek yerine aynı görünür panolara ve belgelere dahil edin. Mümkün olduğunda sözleşmeleri saatler yerine çıktılar etrafında yapılandırın.

## Ödünleşimler: artılar ve eksiler

| Yaklaşım | Artılar | Eksiler |
| --- | --- | --- |
| Çeviklik (paydaş etkileşimleri) | Yüksek iş birliği ve en hızlı değer | Güven ve esneklik gerektirir |
| Scrum (zaman kutulu sprintler) | Düzenli ritim, öngörülebilir tempo, yerleşik düşünme | Tören yükü; kesinti güdümlü işe uygun değil |
| Kanban (sürekli akış, yarım kalan iş sınırları) | Esnek, darboğazları ortaya çıkarır, operasyonlar için iyi | Daha az ritim; sınırlamak için disiplin gerekir |
| SAFe / ağır ölçekleme çerçevesi | Yapı, eğitim, büyük kuruluşlara ve kamuya tanıdık | Hiyerarşiyi ve devirleri yeniden getirir; çevikliği boğabilir |
| LeSS / hafif ölçekleme | Lean ilkelere yakın kalır | Derin örgütsel değişiklik gerektirir |
| Eşzamansız / belge öncelikli | Zaman dilimleri arasında ölçeklenir; kalıcı; kapsayıcı | Belirsiz konularda daha yavaş; yazı disiplini gerektirir |

Kapsayıcı ödünleşim eşgüdüm ile özerklik, yapı ile uyarlanabilirlik arasındadır. Daha fazla çerçeve ve daha fazla eşzamanlı eşgüdüm; hız, yük ve takım yetkilendirmesi pahasına öngörülebilirlik ve uyum satın alır. Daha az çerçeve hız ve sahiplik satın alır, birçok takım arasında olası uyumsuzluk pahasına. Çoğu büyük kuruluş için en iyi cevap, asgari bir paylaşılan ritim artı güçlü yazılı uygulamalardır. Bu, eşgüdüm yükünü daha ağır süreçle yönetmek yerine kaynağında azaltır.

## Takımınızla tartışılacak sorular

1. **Liderlik bir ölçekleme çerçevesinin vaat ettiği öngörülebilirliği istiyorsa, çevikliğin kaldırmayı amaçladığı devirleri yeniden getirmeden onlara bunu nasıl vereceksiniz?** Büyük kurumsal ve kamu programları, gözetim organları görebilecekleri tahminler ve eşgüdüm talep ettiği için çoğu zaman SAFe tarzı büyük oda planlamasını ve aşama kapısı raporlamasını zorunlu kılar. Karşıt değerlendirmeler gerçektir: liderliğin birçok takım arasında öngörülebilirliğe ve uyuma ihtiyacı vardır ve ağır çerçeveler bunu hız, yük ve teslimatı yavaşlatan devirler pahasına satın alır. Tartışmaya kanıt getirin; örneğin çalışma haftasının ne kadarının planlama etkinliklerinde ve takımlar arası bağımlılık eşgüdümünde kaybolduğu ve bu etkinliklerin bağımlılıkları ortadan kaldırıp kaldırmadığı ya da yalnızca ortaya çıkarıp çıkarmadığı. Daha güçlü hamle, takım topolojisi yoluyla eşgüdüm ihtiyacını azaltarak ölçeklemek, sonra raporlamayı planlama maratonlarından değil canlı panolardan ve yazılı arayüzlerden karşılamaktır. Hangi eşgüdümün gerçek, hangisinin tören olduğuna karar verin ve liderliğe ihtiyaç duyduğu tahmini bir çerçevenin yükünden değil, verim ve döngü süresi verilerinden verin.

2. **Hızın takımlar arası bir verimlilik metriğine dönüştürülmesini durdurmak için gerçekte ne yapacaksınız?** Hikaye puanları tek bir takımın kendi yakın vadeli işini planlamasına yardımcı olur ve takımlar arasında karşılaştırıldıkları ya da hedef olarak belirlendikleri anda değersiz hale gelir, çünkü puan enflasyonu rasyonel tepkidir. Büyük bir kuruluşta hızı yöneticilerin karşılaştırdığı bir panoya toplama çekimi güçlüdür ve takımların bağımlı olduğu tahminleri sessizce bozar. Kayma kanıtını getirin: puanlar zamanla enflasyona mı uğruyor, takımlar tahminleri şişiriyor mu, hıza göre sıralanan biri var mı? Takımdan çıkan herhangi bir tahmin için verimi saymayı ve geçmiş döngü süresi verilerini kullanmayı tercih edin ve tahminleri söz olarak değil, belirsizlik altında aralıklar olarak iletin. Cevap, hızın asla takımdan çıkmayacağına ve takımlar arası tahminin akış metriklerini kullanacağına dair açık bir anlaşma üretmelidir.

3. **"Yazıya dökülmüş"ün somut ölçütü nedir ve hangi kararlar gerçekten hâlâ eşzamanlı bir konuşma gerektirir?** Belge öncelikli varsayılan, zaman dilimleri, yükleniciler ve tedarikçiler arasında ölçeklenen şeydir ve henüz herkesin sahip olmadığı gerçek bir yazı disiplini gerektirir. Ölçüt konusunda somut olun: bir bilet canlı görüşme olmadan harekete geçmeye yetecek bağlam taşıyor mu, kararlar kalıcı bir kayda düşüyor mu, kaçınamadığınız toplantılar kaydedilip özetleniyor mu? Kadrolu personeli örtük bilgiden yoksun yüklenicilerle harmanlayan kurumsal ve kamu programları için yazılı bağlam, karma, dağıtık bir iş gücünün tam katkı vermesini sağlayan şeydir. Ödünleşim, belirsiz ya da tartışmalı konuların çoğu zaman eşzamanlı çözülmesinin daha hızlı olmasıdır; bu yüzden onları açıkça adlandırın ve kıt eşzamanlı zamanı onlara ayırın. Yazma alışkanlığını inşa etmenin ve uygunsuz toplantı saatlerinin bedelini kimin taşıdığına karar verin ve bunu her zaman aynı bölgeye yüklemek yerine adil paylaşın.

4. **Mevcut törenlerimizden hangisi, her birini yalnızca geri bildirimi kısaltıp kısaltmadığına, parti boyutunu küçültüp küçültmediğine ya da netliği artırıp artırmadığına göre yargılarsak hayatta kalırdı?** Törenler sessizce birikir: şurada bir günlük toplantı, burada bir iyileştirme oturumu, bir gözden geçirme ve bir retro ve bir planlama etkinliği, büyük bir takım haftasının daha çoğunu bu toplantıların hizmet etmesi gereken işten çok yinelenen toplantılarda harcayana kadar. Karşıt değerlendirmeler gerçektir, çünkü bir kişiye salt yük gibi gelen bir ritüel, dağıtık bir takımın ortak bağlam kurduğu ya da bir engeli ortaya çıkardığı tek yer olabilir. Tartışmaya kanıt getirin: kişi başına haftalık toplam yinelenen toplantı saatleri, her törende katılım ve ilgi ve her birinin yazılı bir güncellemeden gelemeyecek gerçekte hangi kararı ya da sinyali ürettiği. Her takımın aynı dayatılmış ritmi işlettiği bir kurumsal ya da kamu programı için bileşik maliyet muazzamdır; bu yüzden her törenin yerini korumak için geçmesi gereken açık bir test üzerinde anlaşın ve yalnızca alışkanlıkla devam edenleri kesmeye ya da birleştirmeye istekli olun.

5. **İş durduğunda gerçekte nerede beklediğini biliyor muyuz ve akışı mı yönetiyoruz yoksa yalnızca kadro mu sağlıyoruz?** Çoğu bilgi işinde bir görev ömrünün çok daha büyük kısmını aktif çalışılmak yerine kuyruklarda, devirlerde ve incelemede bekleyerek geçirir; yine de takımlar yavaş teslimata içgüdüsel olarak insan ekleyerek ya da daha yüksek kullanım için zorlayarak yanıt verir ve bu kuyrukları kısaltmak yerine uzatır. Gerilim, yarım kalan işi sınırlamanın kapasiteyi boş bırakmak gibi hissettirmesi ve boşta görünen insanların yöneticileri ve gözetim organlarını huzursuz etmesidir. Gerçeği ortaya çıkaran kanıtı getirin: döngü süresi dağılımları, aktif sürenin toplam bekleme süresine oranı, öğelerin panonuzda nerede bloke olarak durduğu ve uyguladığınızda yarım kalan iş sınırlarının (aynı anda uçuşta olan öğe sayısına bir tavan) verimi nasıl değiştirdiği. Personel kullanımıyla ölçülen büyük ya da kamu kuruluşu için bu, hedefi herkesi meşgul tutmaktan bitmiş işin akmasını sağlamaya yeniden çerçeveler ve bu kayma çoğu zaman teslimat hızı üzerindeki tek en büyük kaldıraçtır.

6. **Çalışma biçimimiz, çekirdek zaman diliminizde oturan kadrolu olmayan insanları, yüklenicileri, tedarikçileri ve merkez ofisten saatler farklı bölgeleri nasıl içine alacak?** Ölçekte karma, dağıtık bir iş gücü normdur ve birlikte oturan bir çekirdek takım için ayarlanmış uygulamalar herkesi sessizce dışarıda bırakır: özel kanalla yönetilen tedarikçi, örtük bağlamdan yoksun yüklenici, iş gününün hiçbir zaman bir karar toplantısıyla örtüşmediği bölge. Değerlendirmeler birbirine karşı çeker, çünkü daha sıkı yazılı arayüzler ve eksiksiz yazılı devirler gerçek disiplin gerektirir ve birlikte oturan bir grubun keyif aldığı hızlı gayriresmi eşgüdümü yavaşlatır. Kanıt getirin: kararların alındığı toplantılardan düzenli olarak kim yok, farklı bölgeler bir devir beklerken ne sıklıkla bloke oluyor ve tedarikçiler personelle aynı görünür panolarda mı yoksa ayrı opak bir hatta mı çalışıyor. Kadrolu personeli, yüklenicileri ve tedarikçileri zorunlu raporlama altında birçok zaman diliminde harmanlayan kurumsal ve kamu programları için yazılı, şeffaf, güneşi takip eden uygulamayı tüm iş gücünün katkı vermesini sağlayan temel olarak ele alın ve uygunsuz saatlerin yükünü her zaman aynı bölgeye dayatmak yerine paylaşın.

## Sektör merceği

**Girişim.** Bir avuç insan ve az pistle tören kataloğunu atlayın ve mümkün olan en hafif akışla çalışın: paylaşılan bir pano, kısa bir yazılı günlük güncelleme ve kararlar bir belgede yakalanır ki kimse bir takım arkadaşının uyanmasını beklerken bloke olmasın. Yazıyı ilk günden varsayılan yapın, çünkü eşzamansız alışkanlığı beş kişide kurmak, elli kişide sonradan eklemekten çok daha ucuzdur. Yıllarca ihtiyaç duymayacağınız bir ölçekleme çerçevesini benimsemeyin; avantajınız eşgüdümleyecek neredeyse hiçbir şeyinizin olmamasıdır, bunu koruyun.

**Küçük işletme.** Kadroda çeviklik koçu ya da teslimat yöneticisi olmadan ve sıkı bir bütçeyle, haklı çıkaramayacağınız eğitim ve sertifika maliyetleri taşıyan satın alınmış çerçeveler yerine hazır uygulamaları tercih edin. İşinize uyan tek bir metodoloji seçin; kesinti güdümlü hizmet işi için Kanban ya da proje işi için hafif bir Scrum ritmi; ve basit bir pano ve net biletler işi görürken ağır bir araç satın alma çekimine direnin. Kıt eşgüdüm çabanızı bir şeyleri yazıya dökmeye harcayın ki küçük bir takım tek bir kişinin hafızasına rehin düşmesin.

**Kurumsal.** Birçok takım arasında sorun eşgüdüm maliyeti ve tutarlılıktır: asgari bir paylaşılan ritim, "yazıya dökülmüş"ün ne demek olduğuna dair ortak bir tanım ve hızı takımlar arası bir hedefe dönüştürmeden yukarı toplanan akış metrikleri. Devirleri yeniden getiren bir çerçeveyi vidalamak yerine takım topolojisi yoluyla eşgüdüm ihtiyacını azaltarak ölçekleyin ve çalışma biçimini bir kerelik bir dağıtım değil, kanıttan ayarladığınız bir şey olarak yönetin. Arayüzleri ve raporlamayı standartlaştırın ki gözetim planlama maratonlarından değil canlı panolardan karşılansın.

**Kamu.** Tedarik kuralları, zorunlu aşama kapıları ve kamusal hesap verebilirlik her seçimi biçimlendirir ve kadrolu personel, yüklenici ve tedarikçilerden oluşan karma iş gücü, gerekli ilerleme raporlaması altında birçok zaman dilimine yayılır. Belge öncelikli, şeffaf bir çalışma biçimini tercih edin; burada her iş parçası, hem personel hem tedarikçiler tarafından görülebilen bir panoda tam yazılı bağlam taşır, böylece durum raporları ayrı toplantılardan değil doğrudan kayıttan gelir. Tedarikçi sözleşmelerini opak saatlik faturalama yerine çıktılar ve paylaşılan görünürlük etrafında yapılandırın ve yazılı, denetlenebilir izi bir yük değil, bir uyum varlığı olarak ele alın.

## Örnekler

**Girişim.** Dağıtık, sekiz kişilik bir girişim tam Scrum tören kataloğunu atlar ve paylaşılan bir Kanban panosu artı Slack'te kısa yazılı bir günlük güncelleme ile çalışır. İki kurucu farklı zaman dilimlerinde oturduğu için yazıyı ilk günden varsayılan yaparlar: her karar bir belgeye düşer, böylece kimse diğerinin uyanmasını beklerken bloke olmaz. Daha sonra üçüncü bir zaman diliminde işe aldıklarında, uyum çoğunlukla sadece okumaktır ve eşzamansız alışkanlık değişmeden ölçeklenir. Hiç benimsemedikleri uygulama, eşzamanlı durum toplantısı, hiç kaçırmadıkları şeydir.

**Kurumsal.** Çok uluslu bir banka, üç ayda bir büyük oda planlaması dahil olmak üzere yüzlerce takıma bir ölçekleme çerçevesi uyguladı. Uyum kağıt üzerinde iyileşti ama teslimat yavaşladı. Takımlar, çerçevenin ortaya çıkardığı ama kaldırmadığı takımlar arası bağımlılıkları eşgüdümleyerek günlerini planlama etkinliklerinde geçirdi. Banka yön düzeltti. Yalnızca gerçekten ihtiyaç duyduğu hafif takımlar arası uyumu tuttu, takımları değer akışlarına baştan sona sahip çıkacak şekilde yeniden yapılandırdı ve eşgüdümün çoğunu yazılı arayüzlere ve eşzamansız güncellemelere kaydırdı. Teslimat bekleme süresi düştü ve yorucu planlama maratonları odaklanmış, ara sıra senkronizasyonlara küçüldü.

**Kamu.** Vatandaş hizmetleri sunan bir kamu kurumu, bir bölgede kadrolu personel ve diğer iki bölgede yüklenici takımlarla, birçok zaman dilimine yayılarak, zorunlu ilerleme raporlaması altında çalıştı. Belge öncelikli, Kanban tabanlı bir çalışma biçimi benimsedi. Her iş parçası, hem personel hem tedarikçiler tarafından görülebilen paylaşılan bir panoda tam yazılı bağlam taşıdı. Bölgeler arasındaki devirler yazılı ve eksiksizdi. Gerekli durum raporları ayrı toplantılardan değil doğrudan panodan geldi. Bu, dağıtık, karma bir iş gücünün sürekli iş birliği yapmasına izin verdi, gözetim raporlamasını yan ürün olarak karşıladı ve kurumun zamanlaması zor zaman dilimleri arası toplantılara bağımlılığını azalttı.

## İş gerekçesi: motivasyonlar, YG ve TSM

Ekonomik argüman akış verimliliğine dayanır. Çoğu bilgi işinde bir iş biriminin aktif olarak çalışılarak geçirdiği süre, toplam bekleme süresinin küçük bir bölümüdür. Gerisi beklemedir: kuyruklarda, toplantılarda, devirlerde, zaman dilimi boşluklarında. Parti boyutunu küçülten, yarım kalan işi sınırlayan ve eşzamanlı darboğazları yazılı eşzamansız akışla değiştiren çalışma biçimleri bu beklemeye doğrudan saldırır. Kazanç, insan eklemeden daha kısa bekleme süreleri ve daha yüksek verimdir; artı daha az kusur, çünkü geri bildirim bağlam taze iken daha erken gelir.

Benimsemenin maliyetini mevcut durumun maliyetiyle tartın. Belge öncelikli, eşzamansız ve yalın akış çoğunlukla alışkanlıklarda bir değişiklik ve yazıya ve araçlara bir miktar başlangıç yatırımı maliyeti taşır. Pahalı lisanslara ihtiyaç duymazlar. Ağır ölçekleme çerçeveleri ise gerçek maliyet taşır: eğitim, sertifikasyon, özel roller ve büyük planlama etkinliklerinin süregelen yükü. Yalnızca gerçek eşgüdüm ihtiyaçları bunu haklı çıkarır. Hiçbir şey yapmamanın maliyeti toplantıyla doymuş takvimlerde, dışlanmış uzak katkıcılarda, sonuçları iyileştirmeden zaman tüketen kargo kültü törenlerinde ve yavaş teslimatta görünür. Liderliğe gerekçeyi sunmak için teslimat bekleme süresini, dağıtım sıklığını ve çalışma haftasının düşük değerli toplantılara kaybedilen kısmını ölçün. Büyük bir iş gücü genelinde akıştaki küçük iyileştirmeler büyük kapasite kazançlarına dönüşür.

## Anti-kalıplar ve tuzaklar

- Kargo kültü çevikliği: ardındaki ilkeler olmadan törenleri icra etmek.
- Hedef olarak hız: puan enflasyonunu davet eder ve metriğin yararlılığını yok eder.
- Çerçeve tapınması: uyuma bakmaksızın SAFe ya da bir "Spotify modeli" şablonunu dayatmak.
- Taahhüt olarak tahminler: belirsizlik altındaki öngörüleri bağlayıcı sözler olarak ele almak.
- Toplantı güdümlü kültür: diğer zaman dilimlerini dışlayan eşzamanlı çağrılara varsayılan olarak yönelmek.
- Belgelenmemiş kararlar: insanların kafalarında ve geçmiş konuşmalarda hapsolmuş bilgi.
- Tedarikçi kara kutuları: yüklenicileri ortak görünürlük yerine opak yan kanallardan yönetmek.
- Kullanım takıntısı: bitmiş işin akışı yerine herkesin meşguliyetini azamiye çıkarmak.

## Olgunluk modeli

- **Düzey 1, Başlangıç.** Süreç gelişigüzel ya da kargo kültüdür; takımlar ödünç alınmış törenleri ardındaki ilkeler olmadan icra eder ya da hiçbir paylaşılan yöntem olmadan doğaçlama yapar. İletişim toplantı güdümlü ve belgelenmemiştir, kararlar insanların kafalarında yaşar ve tahminler söz olarak ele alınır. Dağıtık katkıcılar, yükleniciler ve kaymış zaman dilimleri sözlü olarak eşgüdümlenir ve doğru kişi uyuduğunda bloke bırakılır.
- **Düzey 2, Geliştirme.** Tek tek takımlar Scrum ya da Kanban gibi adı konmuş bir metodolojiyi benimser ve bir ölçüde tutarlılıkla izler, ama uygulama takımdan takıma değişir ve törenler çoğu zaman ezberlenmiştir. Bazı takımlar tasarım belgeleri ve karar kayıtları yazarken diğerleri hâlâ toplantılara güvenir. Tahmin ve eşgüdüm gerçekleşir, ama "yazıya dökülmüş"ün ne demek olduğuna dair paylaşılan bir ölçüt olmadan bağlam yine sızar ve takımlar arası devirler ağır kalır.
- **Düzey 3, Standartlaştırma.** Uygulamalar işe uyacak şekilde bilinçli seçilir ve kuruluş genelinde bir beklenti olarak belgelenir: asgari bir paylaşılan ritim, biletlerde ve karar kayıtlarında yazılı bağlam için tanımlı bir ölçüt, varsayılan olarak eşzamansız belge öncelikli iletişim ve kontrol için değil konuşma için kullanılan tahmin. Standart tutarlı uygulanır, böylece herhangi bir takımdaki bir yüklenici ya da yeni katılan okuyarak uyum sağlayabilir ve tedarikçiler personelle aynı görünür panolarda çalışır.
- **Düzey 4, Yönetme.** Çalışma biçimi varsayılmak yerine temel çizgilere karşı ölçülür. Takımlar teslimat bekleme süresini, döngü süresi dağılımlarını, dağıtım sıklığını, verimi ve çalışma haftasının düşük değerli toplantılara kaybedilen kısmını izler ve hızın puan enflasyonuyla oyunlaştırılmasını gözler. Yarım kalan iş sınırları kanıta dayanarak uygulanır, kullanım yerine akış yönetilir ve hangi törenlerin yerini koruyacağına ve kuyrukların nerede uzadığına görüş değil veri karar verir. Liderliğe ve gözetim organlarına raporlama doğrudan bu canlı metriklerden gelir.
- **Düzey 5, Orkestrasyon.** Kuruluş çalışma biçimini akış metriklerinden ve retrospektif kanıttan sürekli ayarlar ve eşgüdüm ihtiyacı daha ağır süreçle yönetilmek yerine takım topolojisi yoluyla kaynağında en aza indirilir. Çalışma biçimleri, teslimat metrikleri ve örgütsel tasarım bütünleşir ve iş gücü, pazar ve düzenleyici tablo değiştikçe uyum sağlar; birçok zaman diliminde personel, yüklenici ve tedarikçilerden oluşan dağıtık, karma takımlar sorunsuz iş birliği yapar ve maliyetini hak etmeyi bırakan uygulamalar törensiz emekliye ayrılır.

## Tartışma fikirleri

- Törenlerimizden hangilerini yalnızca yarattıkları değere göre yargılasak tutardık?
- Bir çerçeve ekleyerek mi yoksa eşgüdüm ihtiyacını azaltarak mı ölçekliyoruz?
- Hızımız bir planlama yardımcısı mı yoksa sessizce oyunlaştırdığımız bir hedef mi?
- Hangi kararlar ve durum yalnızca toplantılarda ve insanların hafızasında yaşıyor ve yazılmalı?
- Eşzamanlı toplantılarımızın bedelini hangi zaman dilimi taşıyor ve bu adil mi?
- Yüklenicilerimiz ve tedarikçilerimiz personelimizle aynı görünür akışta mı çalışıyor?

## Önemli çıkarımlar

- Metodolojilerin yalnızca ritüellerini değil, ardındaki ilkeleri benimseyin.
- İşe uyacak şekilde Çeviklik, Kanban ya da bir karışım seçin; küçük partileri ve hızlı geri bildirimi tercih edin.
- Ölçekleme çerçevelerine şüpheyle yaklaşın; süreç ekleyerek değil, eşgüdümü azaltarak ölçekleyin.
- Tahminleri konuşma ve öngörü için kullanın, asla verimlilik hedefi ya da söz olarak değil.
- Büyük, dağıtık, karma takımların iş birliği yapabilmesi için varsayılan olarak eşzamansız, belge öncelikli iletişimi kullanın.
- Faaliyeti ya da kullanımı değil, çıktıları ve akışı optimize edin.

## Kaynaklar ve ileri okuma

- David J. Anderson, "Kanban: Successful Evolutionary Change for Your Technology Business"
- Donald Reinertsen, "The Principles of Product Development Flow"
- Mary and Tom Poppendieck, "Lean Software Development: An Agile Toolkit"
- Craig Larman and Bas Vodde, "Large-Scale Scrum (LeSS)"
- Nicole Forsgren, Jez Humble, Gene Kim, "Accelerate" (delivery metrics)
- The Agile Manifesto and its twelve principles
- Henrik Kniberg, "Scaling Agile @ Spotify" (with the caution that it is a snapshot, not a model)
- GitLab's public Handbook on asynchronous, remote-first working
