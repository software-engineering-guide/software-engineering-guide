# 5.2 Arayüz tasarımı ve tasarım sistemleri

## Genel bakış ve motivasyon

[Kullanıcı arayüzü (UI) tasarımı](https://en.wikipedia.org/wiki/User_interface_design), insanların gördüğü ve dokunduğu şeyi biçimlendirme sanatıdır: yerleşim, [tipografi](https://en.wikipedia.org/wiki/Typography), renk, aralıklar, denetimler ve durumlar. Bir [tasarım sistemi](https://en.wikipedia.org/wiki/Design_system) bu sanatı alır ve onu paylaşılan, yeniden kullanılabilir, yönetilen bir varlığa dönüştürür: her takımın yararlandığı, belgelenmiş bir ilkeler, bileşenler, kalıplar ve belirteçler (token) kümesi; böylece bütün ürün tek bir ürün gibi görünür ve davranır. UI tasarımı, tek bir ekranın nasıl görüneceğine karar verir. Tasarım sistemi ise birçok takımdaki on bin ekranın nasıl tutarlı kalacağına karar verir.

Büyük bir kurum için tasarım sistemi, UI kalitesi ve teslimat hızı açısından tek başına en yüksek kaldıraçlı yatırımdır. Bu olmadan her takım düğmeleri, formları, kipleri (modal) ve hata yönetimini yeniden icat eder; her biri biraz farklıdır, ayrı ayrı bakımı yapılır, ayrı ayrı bozulur. Kullanıcılar bunun bedelini karışıklık ve güvensizlikle öder; iş ise tekrarlanan emek ve dengesiz kaliteyle. Bir tasarım sistemi tek seferlik tasarım kararlarını yeniden kullanılabilir sermayeye çevirir: [erişilebilirliği](https://en.wikipedia.org/wiki/Accessibility), [duyarlılığı](https://en.wikipedia.org/wiki/Responsive_web_design) ve markayı bir bileşende bir kez çözün, her takım sonucu devralır.

Kurumsal ve kamu alanı iki özel baskı ekler. Birincisi ölçektir: çoğu zaman tedarikçilerce geliştirilmiş ya da birleşmelerle edinilmiş yüzlerce uygulamanın hepsinin tek bir kurum gibi hissettirmesi gerekir. İkincisi ömür ve değişimdir: markalar yenilenir, kurumlar yeniden örgütlenir ve tek bir platformun aynı kod tabanından birkaç markaya ya da alt kuruma hizmet etmesi gerekebilir. Doğru tema ve belirteç yapısına sahip, iyi mimarilenmiş bir tasarım sistemi, bu kapsamlı değişiklikleri yıkıcı olmaktan çıkarıp yönetilebilir kılar.

## Temel ilkeler

- Tutarlılık [bilişsel yükü](https://en.wikipedia.org/wiki/Cognitive_load) azaltır; bir düğme her yerde aynı görünmeli ve aynı davranmalıdır.
- Tasarım kararları varlıktır: onları yeniden kullanılabilir bileşenler ve belirteçler olarak bir kez yakalayın.
- Görsel kararlar için tek doğru kaynak belirteçlerdir; bileşenler belirteçleri kullanır, asla koda gömülü değerleri değil.
- Erişilebilirlik ve duyarlılık, her ekrana sonradan eklenmez, bileşenlerin içine yerleştirilir.
- Tasarım sistemi, tek seferlik bir çıktı değil, kullanıcıları (geliştiriciler ve tasarımcılar) olan bir üründür.
- Görsel hiyerarşi dikkati yönlendirir: yazı, renk ve boşluk, önemi apaçık kılmalıdır.
- Yönetişim bir sistemi tutarlı tutar; katkı onu canlı tutar.

## Öneriler

### Sistemi katmanlara ayırın: belirteçler, bileşenler, kalıplar

Tasarım belirteçleri, renk, aralık, tipografi, köşe yarıçapı, yükselti ve hareket için adlandırılmış, platformdan bağımsız değerlerdir: atomik kararlar. Bunları kademeler halinde kurun: ilkel bir palet (ham değerler), anlam taşıyan anlamsal belirteçler (`color-action-primary`, `space-inset-md`) ve gerektiğinde bileşen düzeyinde belirteçler. Bileşenler anlamsal belirteçleri kullanır, böylece tek bir değişiklik her yere yayılır. Bileşenlerin üstünde kalıplar bulunur: bir veri tablosu, çok adımlı bir form ya da boş durum gibi kanıtlanmış kompozisyonlar. Üç katmanı da canlı örnekler ve kullanım yönergeleriyle tek bir yerde belgeleyin.

### Görsel temelleri doğru kurun

Net hiyerarşisi ve okunabilirlik için cömert satır aralığı olan bir tipografi ölçeği kurun ve sınırlı sayıda boyut ve ağırlık kullanın. Rengi, arayüze dağılmış ham tonlar yerine, erişilebilirlik için yeterli kontrastı (bkz. erişilebilirlik bölümü) ve anlamsal rolleri olan bir sistem olarak tanımlayın. Ekran başına tahmine gerek kalmadan hizalamanın ve ritmin tutarlı kalması için bir aralık ölçeği ve bir yerleşim ızgarası kullanın. Görsel hiyerarşi, birincil eylemi ve en önemli bilgiyi bir bakışta belli etmelidir.

### Duyarlı ve önce mobil tasarlayın

Önce makul en küçük görüntü alanı için tasarlayın, sonra daha büyük ekranlar için geliştirin. Bu, temel içeriği ve denetimleri önceliklendirmenizi zorunlu kılar. Arayüzlerin birkaç sabit kesme noktası arasında sıçramak yerine her ekrana uyum sağlaması için akışkan yerleşimler ve göreli birimler kullanın. Dokunma hedeflerini yeterince büyük yapın ve etkileşimlerin dokunma, fare ve klavyeyle çalıştığından emin olun. Özellikle kamuda, kullanıcılarınızın anlamlı bir bölümünün küçük, eski ya da ucuz cihazlarda olduğunu varsayın.

### Tasarımdan geliştirmeye devri ve eşliği birinci sınıf mesele yapın

Bir tasarım sistemi, ancak sevk edilen UI amaçlanan tasarımla eşleştiğinde ve eşleşmeye devam ettiğinde karşılığını verir. Tek bir doğru kaynak hedefleyin: tasarım aracından dışa aktarılan belirteçler doğrudan koda beslenir, böylece tasarımcılar ve mühendisler aynı değerlere başvurur. Mühendislerin gerçekten kullanacağı, tasarım bileşenleriyle aynı adlara ve özelliklere sahip kodlanmış bir bileşen kütüphanesi sağlayın. Sapmayı yakalamak için görsel gerileme testi (işlenmiş UI'nin onaylı temel görüntülerle otomatik karşılaştırılması) ve tasarım inceleme denetimleri kullanın. Ve "tasarım-kod eşliğini" açık bir sağlık ölçütü olarak ölçün: UI'nin sistem bileşenlerinden inşa edilen payı ile tek seferlik koddan inşa edilen payı.

### Kurumsal ölçekte temalamayı ve beyaz etiketlemeyi destekleyin

Gereksinim duyma ihtimaliniz varsa, baştan birden çok marka için mimari kurun. Bileşenler anlamsal belirteçleri kullandığı için tema yalnızca farklı bir belirteç değerleri kümesidir; bu yüzden bir marka yenilemesi ya da yeni bir alt marka, kod yeniden yazımı değil bir veri değişikliği olur. Açık ve koyu temaları, yüksek kontrast kiplerini ve kiracı başına markalamayı aynı mekanizmayla destekleyin. Markaya özgü mantığı bileşenlerin dışında tutun ve onu belirteç kümelerine ve yapılandırmaya itin.

### Sistemi bir ürün olarak yönetin

Tasarım sistemine özel bir takım, bir yol haritası, sürümleme, bir değişiklik günlüğü ve bir destek kanalı verin. Takımların yeni bileşenlere nasıl katkıda bulunacağını ve bunların nasıl incelenip terfi ettirileceğini açıkça yazın. Merkezi denetimi (tutarlılığı ve erişilebilirliği korumak için) ve bir katkı modelini (sistemin darboğaz olmak yerine gerçek ihtiyaçlarla evrilmesi için) dengeleyin. Kullanımdan kaldırmaları ve geçişleri açıkça duyurun ve kullanan takımlara yeterli hazırlık süresi verin.

## Ödünleşimler: artılar ve eksiler

| Karar | Artılar | Eksiler |
|---|---|---|
| Tasarım sistemi inşa etmek | Tutarlılık, hız, erişilebilirliği bir kez çözmek, kolay marka yenilemeleri | Başlangıç ve süregelen maliyet, özel bir takım gerektirir |
| Hazır bir sistemi benimsemek | Hızlı başlangıç, kanıtlanmış kalıplar | Genel bir görünüm, kendine özgü marka ve ihtiyaçlara uydurması daha zor |
| Sıkı merkezi yönetişim | Tutarlılık, kalite, erişilebilirlik güvencede | Takımlar için darboğaz olabilir, bürokratik hissettirebilir |
| Açık katkı modeli | Gerçek ihtiyaçlarla evrilir, ortak sahiplik | İnceleme olmazsa sapma ve tutarsızlık riski |
| Yoğun belirteçleme ve temalama | Ucuz marka yenilemeleri ve çok markalı destek | Daha fazla soyutlama, daha dik öğrenme eğrisi |

Tasarım sistemleri, başlangıç ve yönetişim maliyetini uzun vadeli tutarlılık ve hızla takas eder. Tek takımlı küçük bir ürün için bu yük karşılığını vermeyebilir. Birçok takımı ve uzun ömürlü ürünleri olan büyük bir kurum için soru, bir sisteme sahip olup olmamak değil, ne kadar yatırım yapılacağı ve nasıl yönetileceğidir. En sık görülen pişmanlık, yönetişime ve eşlik araçlarına az yatırım yapmaktır: sistem kâğıt üzerinde vardır ama takımlar sessizce ondan uzaklaşır.

## Takımınızla tartışılacak sorular

1. **Belirteç mimarimiz nasıl katmanlanmış ve bileşenlerin koda gömülü değer kullanması yasak mı?** Tasarım sisteminin bütün getirisi (ucuz marka yenilemeleri, çok markalı temalama, erişilebilirliği bir kez çözmek), bileşenlerin kod boyunca dağılmış ham tonlar ve piksel değerleri yerine `color-action-primary` gibi anlamsal belirteçleri kullanmasına dayanır. Kademelere şimdi karar verin: ilkel bir palet, anlam taşıyan anlamsal belirteçler ve yalnızca gerçekten gerektiği yerde bileşen düzeyinde belirteçler. Aşırı soyutlama gerçek bir risktir; bu yüzden kaç katmanın fazla olduğunda ve bir geliştiricinin doğru belirteci nasıl hızla bulacağında uzlaşın. Sapmanın kanıtı olarak kod tabanınızdaki koda gömülü renklerin ve aralıkların bir grep çıktısını getirin. Marka mantığı bileşenlere gömülmüşse, marka yenilemesi bir yapılandırma değişikliği yerine kod yeniden yazımı olur; belirteçlemenin önlemek için var olduğu felaket tam olarak budur.

2. **Tasarım-kod eşliğini nasıl ölçer ve savunuruz, sapmayı otomatik olarak hangi araçlar yakalar?** Yalnızca bir tasarım dosyası olarak var olan bir tasarım sistemi bir çıkartma sayfasıdır: mühendisler yine de her şeyi yeniden inşa eder ve sevk edilen UI zamanla amaçtan ayrışır. Açık bir eşlik ölçütü (UI'nin sistem bileşenlerinden inşa edilen payı ile tek seferlik koddan inşa edilen payı) üzerinde uzlaşın ve işlenmiş ekranların onaylı temel görüntülerle karşılaştırılması için görsel gerileme testini CI'a bağlayın. Bu, kurumsal ve kamu ölçeğinde önemlidir, çünkü çoğu zaman tedarikçilerce geliştirilmiş ya da birleşmelerle devralınmış yüzlerce uygulamanın hepsinin tek bir kurum gibi hissettirmesi gerekir. Güncel eşlik sayısını ve takımların sürekli yeniden inşa ettiği en önemli özel bileşenlerin bir listesini getirin. Ölçütün ya da gerileme paketinin sahibi yoksa, sapma sessizce kazanıyor demektir.

3. **Katkıyı, kullanımdan kaldırmayı ve geçişi nasıl yönetiriz ki sistem ne takımlar için darboğaz olsun ne de parçalansın?** Sıkı merkezi denetim tutarlılığı ve erişilebilirliği garanti eder ama tasarım sistemi takımını, takımların etrafından dolaştığı bir darboğaza dönüştürebilir; açık katkı ise sistemi canlı tutar ama inceleme olmadan ayrışan varyantlar riski taşır. Katkı yolunu belirleyin: bir takım yeni bir bileşeni nasıl önerir, kim inceler ve nasıl terfi ettirilir. Aynı şekilde, kırıcı değişiklikleri nasıl duyuracağınıza karar verin, çünkü geçiş desteği ve hazırlık süresi olmayan kullanımdan kaldırmalar, kullanan takımların durmasına ya da çatallanmasına yol açar. Takımların sistemin dışında inşa ettiği bileşen örneklerini getirin ve neden geri katkıda bulunmadıklarını sorun. Yanıt genellikle yönetişiminizin bir hizmet mi yoksa bir engel mi olduğunu gösterir.

4. **Erişilebilirliğin bileşenlerin içinde bir kez çözüldüğünü nasıl garanti ederiz ve bir takımın erişilemez bir tek seferlik bileşen sevk etmesini ne engeller?** Tasarım sistemi için en güçlü argüman, renk kontrastının, odak durumlarının, klavye kullanımının ve ekran okuyucu anlamsallığının bir kez çözülüp her yerde devralınmasıdır; ama takımlar kendi denetimlerini elle yazdığı anda bu söz çöker. Büyük bir kurum için en büyük yasal ve itibar riski buradadır, çünkü tek bir erişilemez ödeme formu ya da tarih seçici gerçek kullanıcıları engelleyebilir ve onu kopyalayan her üründe şikâyetleri tetikleyebilir. Merkezi uygulatmayı (erişilebilir bileşenler artı ham işaretlemeyi reddeden bir linter ya da inceleme kapısı) takım özerkliğiyle tartın ve sert çizginin nerede olduğuna karar verin. Bir erişilebilirlik denetiminin sonuçlarını, uyum durumlarıyla bileşenlerin bir listesini ve takımların sistemin dışında yeniden inşa ettiği özel denetimlerin sayısını getirin. Kurumsal ve kamu ortamlarında bu bir nezaket değildir: WCAG, Section 508 ve EN 301 549 gibi yükümlülükler uyumu bir tedarik ve denetim gereksinimi yapar; dolayısıyla belgelenmiş uyumu olan bir bileşen kütüphanesi başlı başına bir uyum varlığıdır.

5. **Bu sistem kaç markaya, kiracıya ve temaya hizmet etmeli ve belirteç katmanını sonradan uyarlamak yerine şimdi buna göre mimarilendik mi?** Temalama, buna göre tasarladıysanız ucuz, tasarlamadıysanız zalimdir; çünkü hiç öngörülmemiş bir marka ya da kiracı, marka mantığını bileşenlere geri iter ve belirteçlemenin bütün amacını boşa çıkarır. Büyük bir takım için bu karar yılların işini şekillendirir: birkaç markaya, açık ve koyu temaya, yüksek kontrast kipine ve kiracı başına markalamaya hizmet etmesi gereken bir platformun, temanın yalnızca farklı bir değerler kümesi olacağı kadar temiz bir anlamsal belirteç katmanına ihtiyacı vardır. Bu esnekliği aşırı soyutlamayla dengeleyin; kimsenin gezinemediği bir belirteç ağacı başlı başına bir başarısızlıktır. Öngörebildiğiniz marka ve kiracıların yol haritasını, bugün kullanımdaki tema sayısını ve markaya özgü mantığı şimdiden sızdıran bileşenleri getirin. Kurumsal ve kamu bağlamlarında birleşmeler, satın almalar ve kurum yeniden örgütlenmeleri planlamadığınız markalar ekler; bu yüzden baştan çok markalı mimari kurmak, bir veri değişikliği ile çok yıllık bir yeniden yazım arasındaki farktır.

6. **Eski ve tedarikçi yapımı uygulamaları sisteme nasıl geçirecek ve tasarım sistemi takımını bir sonraki bütçe döneminden sağ çıkaracak biçimde nasıl finanse edeceğiz?** Bir tasarım sistemi, getirisini ancak gerçek ürünler onu benimsediğinde sağlar; oysa dönüştürmesi en zor uygulamalar, ona en çok ihtiyaç duyan eski ve dışarıdan sağlanmış olanlardır ve sistemi sürdüren takım, bütçeler kısıldığında çoğu zaman kesilen ilk takımdır. Büyük bir kurum olarak büyük patlama geçişi ile artımlı geçiş arasında ve tedarikçilerin bileşenlerinizin etrafında değil üzerinde inşa etmesini nasıl sağlayacağınıza karar vermelisiniz. Mevcut eşlik puanlarıyla bir uygulama envanterini, uygulama başına bir geçiş çabası tahminini ve tedarikçiler üzerindeki sözleşmesel kaldıraçlarınızı getirin. Kurumsal ve kamu ortamlarında, yeni tedarikçi işinin varsayılan olarak sistemin üzerine inmesi için tasarım sistemi uyumunu tedarik şartlarına yazın ve bakımını yapan takımı kalıcı ortak altyapı olarak finanse edin; çünkü bir yeniden örgütlenmede bekçilerini kaybeden bir sistem bir yıl içinde yeniden parçalanmaya sürüklenir.

## Sektör merceği

**Girişim.** İki ya da üç mühendisle ve harcayacak zamanınız yokken yönetilen bir sistem kurmayın. Renk, aralık ve yazı için küçük bir anlamsal belirteç kümesi ile bir düzine ortak bileşeni tanımlamak için bir iki gün ayırın; hepsi bütün takımın başvurduğu tek bir dosyada olsun. Zor kısımlar için hazır bir ilkel kütüphaneye yaslanın ve hiçbir şeyi koda gömmeyin; böylece ilk gerçek marka yenilemeniz bir yeniden yazım değil, bir belirteç değişikliği olur.

**Küçük işletme.** Özel bir tasarımcınız ve dar bir bütçeniz yoksa, inşa etmek yerine satın alın: kanıtlanmış bir bileşen kütüphanesini ya da UI kitini benimseyin ve markanıza göre hafifçe temalayın. Amacınız, bir tasarım sistemi takımı çalıştırmadan tutarlı, erişilebilir bir ürün elde etmektir; bu yüzden erişilebilirliği ve duyarlılığı kutudan çıkan bir sistemi tercih edin. Onu çatallamak isteme dürtüsüne direnin, çünkü bakımını yapamayacağınız özelleştirilmiş bir kopya, üst proje ilerlediği anda bir yük olur.

**Kurumsal.** Sorun birçok takım ve uzun ömürlü ürünler arasında tutarlılıktır; bu yüzden tasarım sistemini özel bir takımı, sürümlemesi ve yol haritası olan, yönetilen ortak altyapı olarak ele alın. Tasarım-kod eşliğini gerçek bir ölçüt olarak izleyin, görsel gerileme testini CI'a bağlayın ve belirteç katmanını baştan birden çok marka ve tema için mimarileyin. Yönetişim ve geçiş maliyetini açıkça bütçeleyin ve takımların sisteme kendiliğinden kayacağını varsaymak yerine benimsemeyi bir portföy olarak yönetin.

**Kamu.** Tedarik kuralları, şeffaflık ve kamusal hesap verebilirlik her seçimi şekillendirir. WCAG, Section 508 ve EN 301 549 gibi standartlara erişilebilirlik uyumu bir tercih değil yasal gerekliliktir; bu yüzden belgelenmiş uyumu olan bir bileşen kütüphanesi bir uyum varlığı olur. Vatandaşların hizmetler arasında aynı kalıplarla karşılaşması için ortak bir kamu tasarım sistemini tercih edin ya da genişletin, tasarım sistemi kullanımını tedarikçi sözleşmelerine yazın ve kurumların ve tedarikçilerinin benimseyip bunlara bağlı kalabilmesi için bileşenlerinizi ve yönergelerinizi açıkça yayımlayın.

## Örnekler

**Girişim.** İki mühendisli bir girişim, her yeni ekranda düğmeleri ve form alanlarını biraz farklı yeniden inşa edip duruyordu ve ürün yama gibi görünmeye başlamıştı. Ağır bir sistem yerine iki gün harcayıp renk, aralık ve yazı için küçük bir anlamsal tasarım belirteci kümesi ile yaklaşık bir düzine ortak bileşeni, hepsi bütün takımın başvurduğu tek bir dosyada tanımladılar. Hiçbir şey koda gömülü olmadığı için, tasarım odaklı ilk işe alımları daha temiz bir palet önerdiğinde, yenileme ekran ekran bir sürüngenlik yerine bir öğleden sonra uygulamanın her yerine inen bir belirteç değişikliği oldu.

**Kurumsal.** Onlarca ürün takımı olan küresel bir yazılım şirketi, paylaşılan kodlanmış bir bileşen kütüphanesiyle belirteçlenmiş bir tasarım sistemi kurdu. Anlamsal belirteçler, bütün ürünlerde tam bir marka yenilemesini, takım başına çok yıllık bir uğraş yerine haftalar içinde sevk etmelerini sağladı; çünkü değişiklik, binlerce koda gömülü renk düzenlemesi yerine yeni bir belirteç kümesiydi. Bir pano ölçütü olarak izlenen tasarım-kod eşliği, takımlar özel bileşenleri değiştirdikçe yükseldi ve bu da tekrarlanan UI bakımını azalttı.

**Kamu.** Ulusal bir hükümet, kurumlar arasında zorunlu kılınan, kamu hizmetleri için ortak bir tasarım sistemi (paylaşılan bileşenler, kalıplar ve yerleşik erişilebilirlik) oluşturdu. Bir vergi hizmeti, bir sağlık hizmeti ve bir ruhsat hizmeti arasında geçen bir vatandaş aynı başlıkla, form denetimleriyle ve hata kalıplarıyla karşılaşır; bu güven oluşturur ve öğrenme eğrisini kısaltır. Kurumlar ve tedarikçileri daha hızlı ve daha erişilebilir biçimde sevk eder, çünkü zor sorunlar merkezi olarak çözülmüştür ve hükümet yönergeleri ya da erişilebilirlik düzeltmelerini bir kez güncelleyip her yere yayabilir.

## İş gerekçesi: motivasyonlar, YG ve TSM

Bir tasarım sisteminin YG'si, tekrarın kaldırılmasından ve teslimatın hızlanmasından gelir. Her takımın aynı bileşenleri tasarlayıp inşa etmesi yerine, paylaşılan bir kütüphaneden oluşturmaları teslimatı ölçülebilir biçimde hızlandırır ve tasarımcıları ile mühendisleri ürüne özgü işlere serbest bırakır. Bileşenlerde bir kez çözülen erişilebilirlik ve duyarlılık, sizi proje başına düzeltme maliyetinden kurtarır. Eskiden yıllar süren marka yenilemeleri ve temalamalar artık haftalar sürer.

TSM açısından benimseme maliyeti, özel bir takım, araçlar ve mevcut ürünlerin sisteme geçmesi için gereken emektir. Benimsememenin maliyeti sürekli ödenir: takımlar arasında tekrarlanan inşa ve bakım, destek ve yasal risk yaratan tutarsız ve erişilemez UI'lar ve yavaş, pahalı marka yenilemeleri. Tekrar birçok takımın bütçesine yayıldığı için gözden kaçırmak kolaydır: tasarım sistemi bu gizli maliyeti görünür kılar ve tek bir yerde toplar.

Liderliğe gerekçeyi sunmak için takımlar arasındaki tekrarlanan bileşen işini, kompozisyondan gelen pazara çıkış süresi kazancını ve son marka yenilemenizin maliyetini ve süresini, belirteçlenmiş bir sistemin izin vereceği şeyle karşılaştırarak sayısallaştırın. Sistemi, ölçülebilir bir benimseme ölçütü (eşlik yüzdesi) olan ortak altyapı olarak çerçeveleyin; böylece değeri yalnızca ileri sürülmek yerine zaman içinde izlenebilir.

## Anti-kalıplar ve tuzaklar

- **Çıkartma sayfası olarak tasarım sistemi**: kodlanmış bileşenleri olmayan, statik bir tasarım dosyası; mühendisler yine de her şeyi yeniden inşa eder.
- **Her yerde koda gömülü değerler**: kod boyunca dağılmış renkler ve aralıklar; temalamayı ve marka yenilemelerini imkânsız kılar.
- **Yönetişimsizlik**: takımlar ayrışan varyantlar ekledikçe sistem parçalanır; tutarlılık aşınır.
- **Katkısız yönetişim**: merkezi takım darboğaz olur ve takımlar onun etrafından dolaşır.
- **Eşliği görmezden gelmek**: kodlanmış UI tasarım amacından sapar ve kimse farkı ölçmez.
- **Aşırı soyutlama**: o kadar çok belirteç ve katman ki kimse doğrusunu bulamaz ya da kullanamaz.
- **Bileşenlere gömülü marka mantığı**: çok markalılığı ve temalamayı yapılandırma değişikliği yerine kod yeniden yazımı yapar.
- **Geçiş desteği olmayan kırıcı değişiklikler**: kullanan takımlar durur ya da sistemi çatallar.

## Olgunluk modeli

**Düzey 1, Başlangıç.** Her takım kendi UI'sını plansız ve tepkisel olarak inşa eder. Paylaşılan bileşen yoktur, görünüm ve davranış tutarsızdır, renkler ve aralıklar ekran başına koda gömülüdür. Her marka yenilemesi elle, ekran ekran bir uğraştır.

**Düzey 2, Geliştirme.** Paylaşılan bir stil kılavuzu ya da bileşen kütüphanesi vardır ama kısmidir, isteğe bağlıdır ve çoğu zaman tasarım ile kod arasında eşzamansızdır. Bazı takımlar kullanır, bazıları kullanmaz ve temel uygulamalar takımdan takıma çok değişir.

**Düzey 3, Standartlaştırma.** Bakımı yapılan kodlanmış bir kütüphanesi, belgeleri ve yönetişimi olan belirteçlenmiş bir tasarım sistemi belgelenmiştir ve bütün kurumda uygulanır. Bileşenler anlamsal belirteçleri kullanır, temalama desteklenir ve erişilebilirlik ile duyarlılık ekran başına sonradan eklenmek yerine yerleşiktir.

**Düzey 4, Yönetme.** Sistem, başlangıç değerlerine karşı veriyle ölçülür ve denetlenir. Tasarım-kod eşliği ürün başına hedeflerle açık bir ölçüt olarak izlenir, sapmayı yakalamak için görsel gerileme testi CI'da çalışır ve erişilebilirlik uyumu varsayılmak yerine standartlara karşı ölçülür. Benimseme panoları takım başına bileşen kapsamını gösterir; marka yenilemelerinin maliyeti ve süresi kaydedilir, böylece iyileşme zaman içinde görünür olur.

**Düzey 5, Orkestrasyon.** Tasarım sistemi, kurum genelinde bütünleşik ve değişime uyumlu, sürekli iyileşen bir üründür. Sürümlemesi, yol haritası ve işleyen bir katkı modeli vardır; böylece gerçek ihtiyaçlarla evrilir. Marka yenilemeleri ve yeni temalar rutin belirteç değişiklikleridir, çok markalı ve çok kiracılı temalama olağandır ve takım, kullanım verisinden gelen kanıta göre kalıpları emekliye ayırır, yeniden kapsamlar ve terfi ettirir; tasarım araçlarını ve teslimat hatlarını tek bir doğru kaynaktan besler.

## Tartışma fikirleri

- Merkezi yönetişimi takım özerkliğiyle, ne parçalanmaya ne de darboğaza yol açmadan nasıl dengelersiniz?
- "Tasarım-kod eşliği" için doğru ölçüt nedir ve onu nasıl dürüst tutarsınız?
- Bir takımın sistemi kullanmak yerine tek seferlik bir bileşen inşa etmesine ne zaman izin verilmelidir?
- Bir tasarım sistemini, bütçe dönemlerinden ve yeniden örgütlenmelerden sağ çıkacak biçimde nasıl finanse eder ve kadrolarsınız?
- Ne kadar temalama esnekliği, eklenen soyutlama maliyetine değer?
- Eski ve tedarikçi yapımı uygulamaları ortak bir sisteme nasıl geçirirsiniz?

## Önemli çıkarımlar

- Tasarım sistemi, tek seferlik tasarım kararlarını yeniden kullanılabilir, yönetilen sermayeye çevirir.
- Onu katmanlara ayırın (belirteçler, bileşenler, kalıplar); bileşenler anlamsal belirteçleri kullansın.
- Erişilebilirliği ve duyarlılığı bileşenlere yerleştirin ki her takım onları devralsın.
- Tasarım-kod eşliğini bir varsayım değil, ölçülebilir bir sağlık ölçütü olarak ele alın.
- Belirteçleme, marka yenilemelerini ve çok markalı temalamayı yeniden yazım değil veri değişikliği yapar.
- Sistemi bir yol haritası, sürümleme ve katkı modeli olan bir ürün olarak yönetin.
- Kurumsal ve kamu ölçeğinde ortak bir sistem, elde edilebilecek en yüksek kaldıraçlı UI yatırımıdır.

## Kaynaklar ve ileri okuma

- Brad Frost, *Atomic Design*
- Alla Kholmatova, *Design Systems: A Practical Guide to Creating Design Languages*
- Josef Müller-Brockmann, *Grid Systems in Graphic Design*
- Robert Bringhurst, *The Elements of Typographic Style*
- Ellen Lupton, *Thinking with Type*
- Luke Wroblewski, *Mobile First*
- Ethan Marcotte, *Responsive Web Design*
- Nathan Curtis, writings on design tokens and design system governance
- W3C Design Tokens Community Group, format specification
- Government design systems (e.g., UK Government Design System, U.S. Web Design System) as reference implementations
