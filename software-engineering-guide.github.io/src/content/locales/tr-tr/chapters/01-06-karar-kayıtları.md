# 1.6 Karar kayıtları

## Genel bakış ve motivasyon

Bir **karar kaydı**, önemli bir kararı bağlamı ve sonuçlarıyla birlikte yakalayan bir belgedir. En bilinen biçimi **[mimari karar kaydıdır](https://en.wikipedia.org/wiki/Architectural_decision) (ADR)**; mimari açıdan önemli tek bir seçimi, neden yapıldığını ve ondan ne çıktığını kaydeden, tercihen değiştirilemez, kısa bir nottur. Bir projenin kayıtlarının tamamı onun **karar günlüğüdür (ADL)** ve onları tutma disiplini **mimari bilgi yönetiminin (AKM)** bir parçasıdır. Bu bölüm, bölüm 1.5'teki karar alma ve yönetişim uygulamalarının üzerine kurulur ve karar kayıtlarını ölçekte nasıl yazacağınıza, saklayacağınıza ve sürdüreceğinize odaklanır.

Motivasyon basittir ve zor yoldan öğrenmek acıdır. Uzun ömürlü herhangi bir sistemde en pahalı soru, aylar ya da yıllar sonra odada bulunmamış insanlar tarafından sorulan "bu neden böyle inşa edildi?" sorusudur. Kod sistemin *ne* yaptığını gösterir. Testler onun *çalıştığını* gösterir. Ama hiçbiri, değerlendirip reddettiğiniz alternatifler yerine bu yolu *neden* seçtiğinizi yakalamaz. Karar kayıtları olmadan bu gerekçe personel devriyle buharlaşır. Takımlar yerleşik soruları yeniden tartışır, iyi kararları kötü nedenlerle tersine çevirir ya da kötü kararları korkudan sürdürür. Bir karar kaydı, gerekçeyi koruyan ucuz bir geleceğe mektuptur.

Büyük takımlar için bu, bir hafıza yardımcısı kadar bir eşgüdüm aracıdır. Kurumsal kuruluşlar örtüşen seçimler yapan onlarca takım çalıştırır. Paylaşılan bir karar günlüğü, bir takımın zor kazanılmış gerekçesini yeniden kullanılabilir bir varlığa dönüştürür ve ayrışan, uyumsuz kararları önler. Kamu ve düzenlemeye tabi ortamlarda karar kayıtları neredeyse zorunludur. Denetçiler, gözetim organları ve halef yükleniciler, mimari açıdan önemli gereksinimleri onlara karşı yapılan seçimlere bağlayan izlenebilir bir gerekçeye ihtiyaç duyar. İyi tutulmuş bir karar günlüğü çoğu zaman güvence altına alıp denetleyebileceğiniz bir sistem ile alamayacağınız bir sistem arasındaki farktır.

## Temel ilkeler

- ***Ne*yi değil, *neden*i kaydedin.** Bağlam ve reddedilen alternatifler işin özüdür.
- **Kayıt başına bir karar.** Her kaydı belirli ve kendi içinde bütün tutun.
- **Küçük ve hafif, kapsamlı ve kullanılmayandan iyidir.** Var olan tek sayfalık bir kayıt, hiç yazılmayan bir rapordan iyidir.
- **Her şeye zaman damgası koyun.** Maliyetler, kısıtlar ve tedarikçiler değişir; her iddiayı tarihleyin.
- **Pragmatik olarak yaşayan bir günlüğü tercih edin.** Değiştirilemezlik idealdir; pratikte tarihli notlarla değiştirin.
- **Kısaltmalar yerine sözcükler.** "Kararlar", "ADR'lerden" daha fazla katkıyı davet eder.
- **Kararları bulunabilir ve mümkünse sınanabilir kılın.** Doğru kaydı doğru anda yüzeye çıkarın; uygunluk fonksiyonlarıyla güvence altına alın.

## Öneriler

### Temel yapıyı yakalayın

İyi bir karar kaydının birkaç temel bölümü vardır. Bir tane icat etmek yerine bilinen bir şablonu uyarlayın:

- **Başlık:** kısa, şimdiki zamanda emir cümlesi ("Defter için [PostgreSQL](https://en.wikipedia.org/wiki/PostgreSQL) kullan").
- **Durum:** önerildi, kabul edildi, yerine geçildi, kullanımdan kaldırıldı.
- **Bağlam:** bu kararı gerekli kılan durum, güçler, iş öncelikleri ve kısıtlar; ele aldığı mimari açıdan önemli gereksinimi dahil edin.
- **Karar:** yapılan seçim, açıkça ifade edilmiş.
- **Sonuçlar:** neyin kolaylaştığı ve neyin zorlaştığı, tetiklenen ardıl kararlar ve kabul edilen riskler.

Popüler şablonlar arasında Michael Nygard'ınki (basit ve yaygın benimsenmiş), Tyree ve Akerman'ınki (ağırlıklı alternatiflerle daha ayrıntılı), MADR (Markdown Any Decision Records, seçeneklerde ve artı/eksilerinde güçlü) ve Y-ifadeleri (tek cümlelik yapılandırılmış biçim) bulunur. Kayıtlar karşılaştırılabilir olsun diye kuruluş başına birinde standartlaşın. Kopyala-yapıştır şablon için bölüm 12.3'e bakın.

### Belirli, tarihli ve neredeyse değiştirilemez kayıtlar yazın

Her kaydı tam olarak bir karar hakkında tutun. Bireysel iddialara, özellikle kayan her şeye zaman damgası koyun: fiyatlandırma, ölçekleme sayıları, tedarikçi yetenekleri, lisans koşulları. Teoride bir kayıt değiştirilemez olmalıdır. Bir karar değiştiğinde, eskisinin yerine geçen *yeni* bir kayıt yazar, tarihçeyi korursunuz. Pratikte birçok takım **yaşayan belge** yaklaşımının daha iyi çalıştığını bulur: yeni bilgiyi, tarih damgası ve karardan sonra geldiğine dair bir notla mevcut kayda ekleyin. İkisi de meşrudur. Değiştirilemez biçim denetim izleri için daha güçlüdür; yaşayan biçim gündelik takım bilgisi için daha iyidir. Bilinçli seçin ve tutarlı olun.

### Kayıtları işin olduğu yerde saklayın

Karar kayıtlarını kodun yanında [sürüm kontrolüne](https://en.wikipedia.org/wiki/Version_control) koyun: karar başına bir tane olmak üzere, küçük harfli, tire ayrımlı emir kipi fiil öbeğiyle adlandırılmış [Markdown](https://en.wikipedia.org/wiki/Markdown) dosyalarından oluşan bir `decisions/` (ya da `adr/`) dizini (`choose-database.md`, `format-timestamps.md`). Bu size tarihçeyi, incelemeyi ve fark almayı bedavaya verir ve gerekçeyi açıkladığı şeyin yanında tutar. Takımınız [wiki'leri](https://en.wikipedia.org/wiki/Wiki), Google Docs'u ya da Jira tarzı bir izleyiciyi tercih ediyorsa onları kullanın. Araç alışkanlıktan çok daha az önemlidir. Hafif bir komut satırı aracı (`adr-tools` gibi) kayıtları iskeletleyebilir ve dizinleyebilir.

### Onlara "kararlar" adını verin ve mimarinin ötesine genişletin

Birçok takımdan pratik bir içgörü: etiket önemlidir. Bazı geliştiriciler ve yöneticiler "mimari" sözcüğünden tüylenir ve "kayıt" sonradan doldurulan evrak gibi hissettirebilir. Dizini yalnızca "decisions" diye yeniden adlandırmak çoğu zaman bir anahtarı çevirir. Takımlar aynı şablonla tedarikçi seçimlerini, planlama kararlarını, zamanlama kararlarını, veri ve uyum kararlarını kaydetmeye başlar. İnsanlar sözcüklerden kısaltmalardan daha hızlı öğrenir ve çerçeve "zorunlu formu doldur" yerine "gelecekteki takım arkadaşlarının düşünmesine yardım et" olduğunda daha çok katkıda bulunur.

### Yaşam döngüsünü ve yönetişimi tanımlayın

Karar kayıtlarının ölçeklenmesi için çevresindeki süreç üzerinde anlaşın (bölüm 1.5'in yönetişiminin uygulamayla buluştuğu yer burasıdır):

- **Kim açabilir ve neyi haklı kılar:** tipik olarak bilgili herhangi bir katkıcı; gelecekteki geliştiricilerin *neden*e ihtiyaç duyacağı zaman bir kayıt açın ve düşük riskli, kendi içinde bütün ya da zaten belgelenmiş seçimler için atlayın.
- **Yaşam döngüsü:** *Başlatma → Araştırma → Değerlendirme → Uygulama → Sürdürme → Sonlandırma* gibi basit bir akış ve aşamalar arasında geçiş için kabul ölçütleri (sorun ifade edilmiş, alternatifler değerlendirilmiş, ödünleşimler belgelenmiş, paydaşlara danışılmış).
- **Roller:** öneren, araştıran, inceleyen, onaylayan ve kaydı periyodik olarak (en az yılda bir) gözden geçiren ve nihai sonlandırmayı yürüten sorumlu bir bakımcı.
- **Yönetişim:** uzlaşmanın, çatışmanın, yükseltmenin ve vetonun nasıl işlediği ve herhangi bir uyum kısıtı. *Eyleme yönelik eğilim* ve *[katılmasan da bağlan](https://en.wikipedia.org/wiki/Disagree_and_commit)* gibi ilkelere yaslanın ve daha ağır süreci geri döndürülemez, geniş etki alanlı ("tek yönlü kapı") kararlara saklayın.

### Kararları sınanabilir ve bulunabilir kılın

Bir karar kaydı bir kararı *belgeler*; bir **uygunluk fonksiyonu** onu *güvence altına alır*: kararın hâlâ geçerli olduğunu doğrulayan, [sürekli entegrasyonda](https://en.wikipedia.org/wiki/Continuous_integration) (CI) çalışan otomatik bir kontrol ("tüm durum değişiklikleri olay yaymalıdır", "hiçbir modül bu sınırlar arasında içe aktarma yapmamalıdır", ArchUnit gibi araçlar kullanarak). Bu, yönetişimi periyodik manuel incelemeden sürekli, ölçeklenebilir uygulamaya çevirir; bu, özellikle düzenleyici ve denetim hedefleri için değerlidir (bölüm 3.1, 4.6, 8.5). Sonra *doğru* kaydı *doğru* anda yüzeye çıkarın. İlgili kararları, bir geliştirici onları yöneten koda dokunduğunda bir çekme isteğine ekleyen araçlar, insanların bir belge klasörünü okumasını ummaktan daha iyidir.

## Ödünleşimler: artılar ve eksiler

| Seçim | Artılar | Eksiler |
|---|---|---|
| **Hafif ADR'ler (Nygard/MADR)** | Yazması hızlı, gerçekten yazılır; düşük tören | Yüksek riskli, tartışmalı kararlar için daha az titizlik |
| **Ağır şablonlar (Tyree-Akerman)** | Ağırlıklı alternatifler; büyük, maliyetli seçimler için güçlü | Daha yavaş; rutin kaydı caydırabilir |
| **Değiştirilemez + yerine geçme** | Temiz denetim izi; tarihçe korunur | Daha çok kayıt; okuyucular zincirleri izlemek zorunda |
| **Yaşayan belge (tarihli değişiklikler)** | Tek güncel doğruluk kaynağı; sürdürmesi kolay | Daha zayıf denetim hikayesi; sessiz düzenleme riski |
| **Depoda Markdown** | Sürümlü, incelenebilir, kodun yanında | Geliştirici olmayanlar için daha az dostane |
| **Wiki / belge aracı** | Tüm rollere erişilebilir | Tarihçe ve inceleme daha zayıf; koddan sapar |

Temel gerilim **titizlik ile benimseme** arasındadır. Kimsenin kullanmadığı en titiz sistem hiçbir şey kaydetmez. Herkesin kullandığı en hafif sistem değerde bileşir. Hafif olanı varsayılan yapın ve daha ağır süreci pahalı ve geri döndürmesi zor birkaç karara saklayın.

## Takımınızla tartışılacak sorular

1. **Doğru karar kaydı, yöneten kodu dokunan bir geliştiriciye, kimsenin açmadığı bir klasörde durmak yerine o anda nasıl ulaşacak?** Yalnızca yazılan bir günlük, davranışı asla değiştirmeyen gerekçeyi kaydeder; bu, karar kayıtlarının en yaygın başarısız olma yoludur: var olurlar ve önemli olduğunda kimse onları okumaz. Karşıt değerlendirme çabadır, çünkü kayıtları otomatik olarak yüzeye çıkarmak (yönetilen kod düzenlendiğinde onları bir çekme isteğine eklemek) bir wiki ya da belge klasörünün gerektirmediği araç yatırımı gerektirir. Tartışmaya kanıt getirin: yakın zamanda biri yerleşik bir soruyu geri çevirdiğinde ya da yeniden tartıştığında, ilgili kayıt o anda bulunabilir miydi yoksa gömülü müydü? Onlarca takım çalıştıran büyük bir kuruluş için bulunabilirlik, bir takımın zor kazanılmış gerekçesini özel bir arşiv yerine yeniden kullanılabilir bir varlığa çeviren şeydir. Kayıtları kodun yanında sürüm kontrolünde saklayıp çekme isteği akışına bağlamaya karar verin, böylece kayıt işin olduğu yerde görünür.

2. **Her kayıt için sorumlu bakımcı kim ve günlüğünüzün kendinden emin yanlış bilgiye çürümesini ne engelliyor?** Bir karar günlüğünün tehlikeli başarısızlık biçimi boş bir klasör değil, maliyetleri, tedarikçi yetenekleri ve kısıtları yıllar önce sessizce eskimiş kayıtlarla dolu bir klasördür. Her kaydın onu bir ritimle (en az yılda bir) gözden geçiren ve yerine geçmeyi ya da sonlandırmayı yürüten sorumlu bir sahibe ihtiyacı vardır, aksi halde günlük, insanların seçici alıntıladığı ve az güvendiği folklora çürür. Kanıt getirin: kayıtlarınızdan kaçı tarihsiz, kaçı o zamandan beri değişmiş bir tedarikçiyi ya da fiyatı tarif ediyor ve her biri en son ne zaman gözden geçirildi. Kamu ve düzenlemeye tabi ortamlarda bu daha keskindir, çünkü değiştirilemez, yerine geçilmiş bir zincir tam da denetçilerin ve halef yüklenicilerin izlenebilir bir gerekçe için dayandığı şeydir. Yaşam döngünüzü açıkça belirleyin, kayan bireysel iddialara zaman damgası koyun ve bakımcıları atayın, böylece günlük bir mezarlık değil yaşayan bir varlık kalır.

3. **Tüm takımlarda tek bir şablonda standartlaşmalı mısınız ve en yüksek riskli kararlarınız gerçekte ne kadar titizliğe ihtiyaç duyar?** Karşılaştırılabilirlik gerçek bir faydadır: her takım aynı biçimi (Nygard, MADR ya da benzeri) kullandığında yeni bir takım üç önceki kaydı bulup gerekçeyi bir ay süren tartışma yerine bir öğleden sonra benimseyebilir. Temel gerilim titizlik ile benimseme arasındadır, çünkü kimsenin kullanmadığı en ağır şablon hiçbir şey kaydetmez, herkesin kullandığı en hafifi ise değerde bileşir. Kanıt getirin: kayıtlar gerçekten yazılıyor mu ve ayrıca, büyük, tartışmalı, pahalı kararlardan herhangi biri hafif biçim alternatifleri tartmayı atladığı için yetersiz analiz edildi mi? Takımlar arasında örtüşen seçimleri eşgüdümleyen kurumsal kuruluşlar için paylaşılan bir şablon artı aranabilir bir dizin, ayrışan, uyumsuz kararları önler. Yaygın durum için hafifi varsayılan yapın ve hangi tek yönlü kapı kararlarının ağırlıklı alternatiflerle daha ağır bir biçimi hak ettiğine önceden karar verin.

4. **Bir karar kaydı açmayı gerçekte ne haklı kılar ve bir seçimin ona ihtiyaç duymadığını söyleme yetkisi kimde?** Çıtayı çok yüksek koyarsanız sonuçlu seçimlerin ardındaki gerekçe buharlaşır; çok düşük koyarsanız günlük, insanların gerçekten ihtiyaç duyduğu kayıtları gömen önemsiz şeylerle dolar. Büyük bir kuruluş için belirsiz bir eşik, her takımın kendi eşiğini doğaçlamasına yol açar; böylece kapsam eşitsiz hale gelir ve kimse eksik bir kaydın önemsiz bir karara işaret ettiğine güvenemez. Tartışmaya kanıt getirin: kaydedilmiş ama gerekmeyen bir avuç yakın zamanlı karar ve kaydedilmemiş ve sonradan size yeniden keşfe mal olmuş acı verici olanlar. Basit bir test üzerinde anlaşın; örneğin gelecekteki bir geliştirici *neden*e ihtiyaç duyduğunda kaydetmek ve düşük riskli, kendi içinde bütün ya da zaten belgelenmiş seçimleri atlamak. Düzenlemeye tabi ve kamu ortamlarında hesap değişir, çünkü bir denetim yetkisi, takım yazmaya değer bulsun bulmasın her mimari açıdan önemli gereksinim için bir kayıt isteyebilir; bu yüzden hangi kararların pazarlık dışı olduğunu baştan adlandırın.

5. **Kayıtlarınız karar anında yakalanan gerçek gerekçe mi, yoksa bir zorunluluğu karşılamak için sonradan yazılan evrak mı?** Bilet kapatmak için sonradan üretilen bir kayıt, seçilen seçeneği aklamaya ve gerçekten tartılan alternatifleri sessizce atlamaya eğilimlidir; bu tam da gelecekteki bir okuyucunun en çok ihtiyaç duyduğu bilgidir. Karşıt baskı gerçektir: *neden*i bir kararın öncesinde ya da sırasında yazmak yayımlamaktan daha yavaş hissettirir ve reddedilen yolları yazılı olarak kabul etmek bazı takımların sahip olmadığı psikolojik güvenlik gerektirir. Masaya yakın zamandan bir kayıt örneği getirin ve bağlamın ve reddedilen alternatiflerin gerçek müzakere gibi mi yoksa sonradan yamanmış gerekçelendirme gibi mi okunduğunu dürüstçe sorun. Büyük bir takım için içi boş kayıtlar hiç olmamasından kötüdür, çünkü insanlara günlüğe güvenilemeyeceğini öğretir. Kurumsal ve kamu denetiminde bu ayrım keskindir: gözetim organları ve halef yükleniciler gerçekten değerlendirileni yansıtan bir gerekçeye dayanır ve tiyatro gibi okunan bir kayıt, günlüğün sağlamak için var olduğu güvenceyi baltalar.

6. **En yüksek riskli kararlarınızdan hangilerini, periyodik manuel incelemenin bir ihlali yakalayacağına güvenmek yerine otomatik bir uygunluk fonksiyonuyla güvence altına alabilirsiniz?** Bir karar kaydı bir seçimi belgeler, ama yalnızca sürekli entegrasyonda çalışan otomatik bir kontrol, onlarca geliştirici yıllar boyunca koda dokunurken o seçimin sessizce aşınmasını engeller. Ödünleşim yatırımdır, çünkü uygunluk fonksiyonları yazmak ve sürdürmek (ArchUnit gibi araçlarla) mühendislik zamanına mal olur ve birçok karar, özellikle süreç ya da tedarikçi seçimleri, mekanik olarak sınanabilir değildir. Kanıt getirin: hangi sınır kararları (modül bağımlılıkları, olay yayma, veri erişim kuralları) sessizce ihlal edildi ve yalnızca incelemede ya da üretimde geç yakalandı. Birçok takım çalıştıran bir kurumsal kuruluş için uygunluk fonksiyonları yönetişimi merkezi bir darboğazdan, herkesi yavaşlatmadan ölçeklenen sürekli uygulamaya çevirir. Düzenlemeye tabi ve kamu bağlamlarında otomatik, her zaman açık bir kontrol, bir incelemedeki imzadan çok daha güçlü denetim kanıtıdır, çünkü birinin bir zamanlar onayladığını değil, kararın bugün hâlâ geçerli olduğunu kanıtlar.

## Sektör merceği

**Girişim.** Alışkanlıkla ve başka hiçbir şeyle sınırlı tutun: ana deponuzda bir `decisions/` klasörü ve gelecekteki kendinizin sorgulayacağı bir karar verdiğinizde iki bölümlük bir not (bağlam ve seçim). Yaşam döngüsünü, rolleri ve onaylayıcıları tümüyle atlayın, çünkü sürdüremeyeceğiniz süreci terk edersiniz. İlk işe alımınızı sistemin neden böyle inşa edildiğini sormaktan kurtaran tek kayıt bütün uygulamanın bedelini zaten öder.

**Küçük işletme.** Özel bir mimar ve az zamanla, adanmış bir araç satın almak yerine kayıtları takımınızın zaten çalıştığı yere koyun; ister wiki, ister paylaşılan belge, ister depo olsun. Alışkanlık araçlardan çok daha önemlidir, bu yüzden engeli düşürün: dizini `adr` yerine `decisions` olarak adlandırın ve tedarikçi ile yap ya da satın al seçimlerini teknik olanlarla aynı nefeste yakalayın. Dış yüklenicilere yaslandığınızda, bir tedarikçiyi ya da platformu neden seçtiğinize dair kısa, tarihli bir kayıt, kimsenin sonradan açıklayamayacağı bir seçime kilitlenmeye karşı ucuz bir sigortadır.

**Kurumsal.** İş birçok takım arasında eşgüdümdür: tek bir şablonda standartlaşın, çapraz takım aranabilir bir dizin yayımlayın ve ihlaller incelemeyi beklemek yerine derlemeyi başarısız kılsın diye temel sınır kararlarını uygunluk fonksiyonlarıyla destekleyin. Günlüğün folklora çürümek yerine yaşayan bir varlık kalması için her kayda bir inceleme ritmiyle sorumlu bir bakımcı atayın. İyi yapıldığında bir takımın zor bir seçimdeki gerekçesi, bir sonraki takımın yeniden tartışmak yerine bir öğleden sonra benimsediği bir varlığa dönüşür.

**Kamu.** Tedarik kuralları, şeffaflık ve kamusal hesap verebilirlik karar kayıtlarını neredeyse zorunlu kılar. Mimari açıdan önemli her gereksinim için, her biri seçimi karşıladığı yetkiye ya da uyum kontrolüne bağlayan, değiştirilemez, yerine geçilmiş bir kayıt isteyin; böylece gözetim organları bir yeniden yapılandırma değil, izlenebilir bir gerekçe bulur. Kamu sistemleri çok yıllı, çok tedarikçili ömürlere yayıldığı için, iyi tutulmuş bir günlük çoğu zaman halef bir yüklenicinin sistemin neden öyle biçimlendiğini anlamasını ve yerleşik zemini yeniden tartışmadan işe devam etmesini sağlayan şeydir.

## Örnekler

**Girişim.** Beş kişilik bir girişim ana deposuna sade bir `decisions/` klasörü ekler; gelecekteki kendilerinin sorgulayacağı bir karar verildiğinde iki bölümlük bir not (bağlam ve seçim). Yaşam döngüsü yok, roller yok, onaylayıcılar yok: yalnızca *neden*i kodun yanına yazma alışkanlığı. İlk işe alımları altı ay sonra katıldığında bütün klasörü bir saatte okur ve "bu neden böyle inşa edildi?" diye sormayı bırakır. Hafif günlük giriş başına dakikalara mal olur ve onları bir takım büyümeden çok önce ısıran yeniden keşif vergisinden kurtarır.

**Kurumsal.** 30 mühendislik takımı olan bir perakendeci, her depoda MADR biçimli kayıtlar artı aranabilir merkezi bir dizin üzerinde standartlaşır. Yeni bir takım "[monorepo](https://en.wikipedia.org/wiki/Monorepo) ve çoklu depo" ikilemiyle karşılaştığında bağlam ve sonuçlarla üç önceki kayıt bulur ve gerekçeyi bir ay süren tartışma yerine bir öğleden sonra benimser. Temel sınır kararları (hizmet sahipliği, veri erişim kuralları) ArchUnit uygunluk fonksiyonlarıyla desteklenir, böylece ihlaller incelemede yakalanmak yerine derlemeyi başarısız kılar. Bu, merkezi darboğaz olmadan ölçeklenen yönetişimdir.

**Kamu.** Bir yardım sistemini modernize eden bir kurum, her mimari açıdan önemli gereksinim için bir ADR ister; her biri kararı karşıladığı yetkiye ya da uyum kontrolüne (erişilebilirlik, veri ikameti, denetlenebilirlik) bağlar. Kayıtlar değiştirilemez ve yerine geçilmiştir; bu, gözetim incelemesini karşılayan izlenebilir bir günlük üretir. Önemlisi, halef bir yüklenicinin sistemin neden öyle biçimlendiğini anlamasına da izin verir ve kamu programlarında tipik olan çok yıllı, çok tedarikçili ömürler boyunca sürekliliği korur (bölüm 4.6, 10.4).

## İş gerekçesi: motivasyonlar, YG ve TSM

Bir karar kaydının yazılması dakikalara, gözden geçirilmesi birkaç dakika daha eklemeye mal olur. Getiri, kaçınılan *yeniden karar* maliyeti ve kaçınılan *yanlış geri alma* maliyetidir; ikisi de uzun ömürlü sistemlerde büyük ve yinelenendir. Bir takım yerleşik bir soruyu her yeniden tartıştığında ya da kimsenin ardındaki kısıtı hatırlamadığı için sağlam bir seçimi tersine çevirdiğinde, kıdemli mühendis zamanıyla ve çoğu zaman bir olayla öder. Bir karar günlüğü bu yinelenen vergiyi bir kerelik bir yazıya dönüştürür.

**Toplam sahip olma maliyeti** açısından karar kayıtları, tutabileceğiniz en yüksek kaldıraçlı belgelendirmeler arasındadır, çünkü personel devrine en duyarlı tek varlığı hedefler: gerekçeyi. Uyum daha hızlıdır (yeni işe alınanlar yalnızca kodu değil, *neden*i okur). Modernizasyon daha güvenlidir (bölüm 3.6: temel kararları rastlantısal olanlardan ayırt edebilirsiniz). Denetimler daha ucuzdur (kanıt zaten vardır). Onları tutmamanın maliyeti hiçbir panoda görünmez ve her ayrılışla sessizce bileşir. Liderliği ikna etmek için yakın zamandaki pahalı bir yeniden keşfe ya da bir olaya yol açan tersine çevrilmiş bir karara işaret edin ve çözümün tesis edilmesinin neredeyse hiçbir şeye mal olmadığını belirtin.

## Anti-kalıplar ve tuzaklar

- ***Neden* olmadan *ne*yi kaydetmek:** bağlamı ve reddedilen alternatifleri, yani asıl noktayı atlamak.
- **Sonradan evrak:** düşünmek için değil bir zorunluluğu karşılamak için yazılan kayıtlar; içi boş okunurlar ve kimse onlara güvenmez.
- **Çok kararlı mega belgeler:** kimsenin gezinemediği ya da temiz biçimde yerine geçemediği dev bir sayfa.
- **Tarihsiz iddialar:** bir zamanlar doğru olan maliyetler ve kısıtlar, zamansız olarak sunulur.
- **Sessiz düzenlemeler:** tarihli bir not olmadan bir kararın tarihçesini değiştirmek, denetim izini yok etmek.
- **Yalnızca yazılan günlükler:** oluşturulan ve ilgili oldukları anda hiç yüzeye çıkarılmayan, bu yüzden davranışı etkilemeyen kayıtlar.
- **Kısaltma kapı bekçiliği:** "ADR" ve "mimari"de ısrar ederek katkıyı caydırmak.
- **Yaşam döngüsü yok:** hiç gözden geçirilmeyen, yerine geçilmeyen ya da sonlandırılmayan, yanlış bilgiye çürüyen kayıtlar.

## Olgunluk modeli

- **Düzey 1 (Başlangıç):** Kararlar insanların kafalarında, sohbet dizilerinde ve commit mesajlarında yaşar; yakalama reaktif ve gelişigüzeldir ve gerekçe personel devriyle rutin olarak kaybolur.
- **Düzey 2 (Geliştirme):** Bazı takımlar, bir birey hatırladığında, çeşitli biçim ve şablonlarda kayıt tutar; uygulama takımlar arasında tutarsızdır, paylaşılan günlük, adlandırma ya da süreç yoktur.
- **Düzey 3 (Standartlaştırma):** Tek bir şablon, depo içi saklama ve tanımlı bir yaşam döngüsü ve yönetişim (açma/atlama ölçütleri, roller, inceleme ritmi) belgelenmiş ve kuruluş genelinde tutarlı uygulanır; kayıtlar sessizce düzenlenmek yerine gözden geçirilir ve yerine geçilir.
- **Düzey 4 (Yönetme):** Karar günlüğü temel çizgilere karşı ölçülür: kapsam (kaydı olan mimari açıdan önemli kararların payı), tazelik (ritmi içinde gözden geçirilen kayıtların payı, artı tarihsiz ya da eskimiş iddiaların sayısı) ve bulunabilirlik (ilgili bir kaydın yönetilen kodu değiştiren geliştiriciye gerçekte ne sıklıkla ulaştığı). Sorumlu bakımcılar bu metriklere göre hareket eder; eskimiş kayıtların yerine geçer ve kapsam boşluklarını anekdot yerine kanıtla kapatır.
- **Düzey 5 (Orkestrasyon):** Çapraz takım aranabilir bir karar günlüğü gündelik işe entegre edilir: ilgili kayıtlar yönettikleri değişikliklerde otomatik yüzeye çıkar, temel kararlar sürekli entegrasyonda uygunluk fonksiyonlarıyla güvence altına alınır ve günlük uyum, modernizasyon ve denetim için yaşayan bir varlık olarak beslenir. Kuruluş uygulamanın kendisini sürekli iyileştirir; sistem ve kısıtları kaydıkça kayıtları emekliye ayırır, yerine geçer ve yeniden kapsamlandırır ve karar portföyü büyüdükçe titizliğe yatırım yaptığı yeri yeniden dengeler.

## Tartışma fikirleri

1. Takımınızın en son hangi kararı, kimse özgün gerekçeyi hatırlamadığı için tersine çevirdi ya da yeniden tartıştı?
2. `adr/` dizininizi `decisions/` olarak yeniden adlandırmak kimin katkı verdiğini ve neyin kaydedildiğini değiştirir miydi?
3. Kritik kararlarınızdan hangileri bugün otomatik bir uygunluk fonksiyonuyla güvence altına alınabilir?
4. Değiştirilemez-ve-yerine-geç mi yoksa yaşayan belge mi: hangisi denetim yükümlülüklerinize ve kültürünüze uyar ve neden?
5. Yeni bir işe alınan (ya da halef bir yüklenici) sisteminizin neden bu şekilde biçimlendiğini şu anda nasıl keşfeder?
6. Takımınızda bir karar kaydı açmayı ne haklı kılar ve açmamayı ne haklı kılar?

## Önemli çıkarımlar

- Bir karar kaydı, önemli bir kararı **bağlamı ve sonuçlarıyla** yakalar: yalnızca *ne*yi değil, *neden*i.
- Kayıtları **belirli, zaman damgalı ve hafif** tutun; tek bir şablonda (Nygard, MADR ya da benzeri) standartlaşın.
- Onları **kodun yanında sürüm kontrolünde** saklayın; katkıyı genişletmek için onlara "kararlar" demeyi düşünün.
- Bir **yaşam döngüsü ve yönetişim** tanımlayın (açma/atlama ölçütleri, roller, inceleme ritmi); ağır süreci tek yönlü kapı kararlarına saklayın.
- Kararları değişiklik anında **bulunabilir** ve mümkünse uygunluk fonksiyonlarıyla **sınanabilir** kılın.
- YG, kaçınılan yeniden keşif ve yanlış geri alma maliyetidir; TSM gerekçesi personel devri, modernizasyon ve denetimin en çok önem taşıdığı yerde en güçlüdür. Bölüm 1.5'e (karar alma ve yönetişim) ve bölüm 3.1'e (mimari temelleri) bakın.

## Kaynaklar ve ileri okuma

- Michael Nygard, "Documenting Architecture Decisions" (2011): the foundational lightweight ADR.
- MADR: Markdown Any Decision Records project (adr.github.io/madr).
- Jeff Tyree and Art Akerman, "Architecture Decisions: Demystifying Architecture" (*IEEE Software*, 2005).
- Olaf Zimmermann, "Y-Statements" and "Architectural Decision Making" (ozimmer.ch).
- Joel Parker Henderson, *Architecture Decision Record (ADR)*: templates, examples, and teamwork guidance (github.com/joelparkerhenderson/architecture-decision-record).
- ThoughtWorks Technology Radar: "Lightweight Architecture Decision Records."
- Neal Ford, Rebecca Parsons, Patrick Kua, Pramod Sadalage, *Building Evolutionary Architectures* (fitness functions).
- AWS Prescriptive Guidance, "ADR process"; Red Hat, "Why you should use ADRs."
- Wikipedia, "Architectural decision" and "Architecturally significant requirements."
