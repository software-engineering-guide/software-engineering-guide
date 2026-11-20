# 4.8 Şifreleme ve anahtar yönetimi

## Genel bakış ve motivasyon

Kurduğunuz hemen her sistem zaten [kriptografiye](https://en.wikipedia.org/wiki/Cryptography) dayanır. Kriptografi, bilgiyi matematiksel tekniklerle korumanın ve yalnızca hedeflenen tarafların onu okuyabilmesini ya da ona güvenebilmesini sağlamanın pratiğidir. Web trafiğiniz şifreli kanallardan geçer, parolalarınız özetlenir (hash), yazılım güncellemeleriniz imzalanır ve müşteri verileriniz diskte şifreli durur. Çoğu mühendis için iyi haber şu: bunların hiçbirini icat etmeniz beklenmiyor. Zor olan kısım matematik değildir. Zor olan, denenmiş yapı taşlarını doğru kullanmak ve her şeyden önce bu yapı taşlarının dayandığı anahtarları yönetmektir.

Bu bölüm, kriptograf olmayan mühendisler için yazıldı; yani hemen hepimiz için. Sağlam seçimler yapmaya, her aracın neyi garanti ettiğini bilmeye ve güçlü algoritmaları yanlış bir güven duygusuna çeviren hatalardan kaçınmaya yetecek kadar anlayışa ihtiyacınız var. Bölüm 4.3 (altyapı ve bulut güvenliği) şifrelemeden ve anahtar yönetiminden kısaca söz eder; burada neyin şifreleneceğine, nasıl şifreleneceğine ve bunu gerçeğe dönüştüren anahtar yaşam döngüsünün nasıl yürütüleceğine daha derinlemesine giriyoruz.

Büyük kurumlarda kriptografi binlerce hizmete, sertifikaya ve anahtara yayılır; süresi dolmuş tek bir sertifika ya da kaybolmuş tek bir anahtar kritik bir sistemi durdurabilir ya da bir veri deposunu sızdırabilir. Kamuda kriptografi çoğu zaman zorunlu tutulur, doğrulanır ve denetlenir; veri sınıflandırma kuralları hangi anahtarın hangi sırrı koruyacağını ve onu kimin elinde tutabileceğini tam olarak belirler. Her iki ortamda da yinelenen başarısızlık aynıdır: iyi algoritmalar, özensiz anahtar yönetimi yüzünden boşa gider.

## Temel ilkeler

- **Kendi kriptonuzu yazmayın.** Denenmiş, geniş çapta incelenmiş kütüphaneleri ve standart algoritmaları kullanın. Yeni icat edilen şemalar, ancak uzmanların yakalayabildiği biçimlerde çöker.
- **Algoritmalar kolay kısımdır; anahtarlar zor kısımdır.** Gerçek dünyadaki başarısızlıkların çoğu bir anahtarın yaşam döngüsünde yatar.
- **Her ilkelin neyi garanti ettiğini bilin.** Gizlilik, bütünlük ve kimlik doğruluğu farklı özelliklerdir ve farklı araçlar gerektirir.
- **Aktarım sırasında ve durağan halde varsayılan olarak şifreleyin.** Korumayı isteğe bağlı bir seçenek değil, standart hale getirin.
- **Anahtar saklama yetkisini veri erişiminden ayırın.** Bir anahtarı yöneten kişi, onun koruduğu veriyi otomatik olarak okuyabilmemelidir.
- **Değişime hazırlanın.** Algoritmalar zayıflar, anahtarlar sızar, standartlar evrilir. Döndürme ve geçişe ilk günden hazır olacak biçimde kurun.
- **Önemli olduğu yerde doğrulanmış gerçeklemeleri tercih edin.** Düzenlemeye tabi ve kamu işlerinde, tanınmış doğrulaması olan modülleri seçin.

## Öneriler

### Kendi kriptonuzu yazmayın

Bu altın kuraldır ve önce söylemeye değer. Kendi şifreleme algoritmanızı tasarlamayın, kendi protokolünüzü icat etmeyin, bir makaleden bir ilkeli elle gerçeklemeyin. Çalışan kriptografi basit görünür ama ancak yıllarca süren uzman incelemesinden sağ çıkabilen ince başarısızlık biçimlerini gizler (zamanlama yan kanalları, dolgu kehanetleri, zayıf rastgelelik). Platformunuzun standart kripto modülü ya da saygın bir kütüphane gibi yerleşik kütüphaneleri kullanın ve bunları mevcut en yüksek soyutlama düzeyinde kullanın. Düşük seviyeli parçaları kendiniz birleştirmek yerine, güvenli seçimi varsayılan yapan kimlik doğrulamalı şifreleme kiplerine ve "kolay" arayüzlere başvurun.

### İlkeli, ihtiyaç duyduğunuz garantiyle eşleştirin

Farklı araçlar farklı garantiler sunar ve bunları karıştırmak yaygın ve tehlikeli bir hatadır. Üç ana ailenin farkını öğrenin.

- **[Simetrik anahtarlı](https://en.wikipedia.org/wiki/Symmetric-key_algorithm) kriptografi**, hem şifrelemek hem de çözmek için tek bir paylaşılan gizli anahtar kullanır. Hızlıdır ve **gizliliği** korur, ancak her iki tarafın da anahtarı önceden paylaşmış olması gerekir. AES standart iş atıdır.
- **[Açık anahtarlı](https://en.wikipedia.org/wiki/Public-key_cryptography) kriptografi**, matematiksel olarak bağlı bir anahtar çifti kullanır: herkesin elinde tutabileceği bir açık anahtar ve sizin gizli tuttuğunuz bir özel anahtar. Anahtar dağıtımı sorununu çözer ve **dijital imzaları** mümkün kılar; imzalar **kimlik doğruluğunu** (kimin gönderdiğini) ve **bütünlüğü** (değiştirilmediğini) kanıtlar.
- Bir **[kriptografik özet işlevi](https://en.wikipedia.org/wiki/Cryptographic_hash_function)** veriden sabit boyutlu bir parmak izi üretir ve **bütünlük** denetimi sağlar. Özetleme tek yönlüdür ve şifreleme değildir. Parolaları saklamak için yavaş, tuzlanmış bir parola özetleme işlevi kullanın, asla düz, hızlı bir özet işlevi kullanmayın (uygulama güvenliğine dair bölüm 4.2'ye bakın).

Pratik ders şudur: şifreleme veriyi gizler ama kimin gönderdiğini kanıtlamaz; özet ise kurcalamayı fark eder ama hiçbir şeyi gizlemez. Gerçek sistemlerin çoğu bunları birleştirir ve işte bu yüzden bunları doğru biçimde bir arada sunan kütüphanelere yaslanmalısınız.

### Aktarım sırasında güncel TLS ile şifreleyin

Her ağ sıçramasını, verinin sistemler arasında hareket ederken güvenliğini sağlayan protokol olan [Taşıma Katmanı Güvenliği](https://en.wikipedia.org/wiki/Transport_Layer_Security) (TLS) ile koruyun. Modern TLS sürümlerini zorunlu kılın, eskimiş olanları kapatın, güçlü şifre takımları seçin ve sertifikaları "çalışsın diye" denetimleri kapatmak yerine düzgünce doğrulayın. Yalnızca herkese açık kenarı değil, iç hizmetten hizmete trafiği de şifreleyin; çünkü sıfır güven duruşu iç ağın düşmanca olduğunu varsayar. Sertifika düzenlemeyi ve yenilemeyi otomatikleştirin ki TLS her yerde zahmetsiz varsayılan olsun.

### Durağan halde zarf şifrelemesi ile şifreleyin

Saklanan veriyi varsayılan olarak şifreleyin: veritabanları, nesne depolama, yedekler ve günlükler. Standart kalıp **zarf şifrelemesidir**: gerçek veriyi bir **veri şifreleme anahtarı (DEK)** şifreler, DEK'i ise bir anahtar yönetim hizmetinde tutulan **anahtar şifreleme anahtarı (KEK)** şifreler. Bu, terabaytlarca veriyi yeniden şifrelemeden ana anahtarı döndürmenizi sağlar ve güçlü kök anahtarı sertleştirilmiş bir sınırın içinde tutar. Verinin yanında yalnızca sarmalanmış DEK'i saklayın; kullanım anında onu getirip açın.

### Anahtar yaşam döngüsünü bilinçli yürütün

Bir anahtarın yaşam döngüsü kriptografinin gerçekten zor kısmıdır ve ihlallerin ve kesintilerin çoğunun çıktığı yerdir. Her aşamayı bilerek yönetin:

- **Üretim:** anahtarları güçlü bir rastgelelik kaynağından, uygun güçte üretin.
- **Dağıtım:** anahtarları ihtiyaç duyan sistemlere, kodda, yapılandırma dosyalarında ya da sohbette ifşa etmeden ulaştırın.
- **Döndürme:** anahtarları bir takvime göre değiştirin ve şüpheli ele geçirilmede hızlı döndürebilin.
- **İptal:** ele geçirilmiş bir anahtarı ya da sertifikayı hızla geçersiz kılın ve sistemlerin iptale uyduğundan emin olun.
- **İmha:** eski anahtar malzemesini geri getirilemeyecek biçimde güvenle emekliye ayırın.

Bunu merkezileştirmek için bir **anahtar yönetim hizmeti (KMS)** kullanın; en yüksek güvence gerektiren anahtarlarınız için ise anahtarları üreten ve koruyan, böylece anahtarların düz metin olarak asla dışarı çıkmadığı kurcalamaya dayanıklı bir cihaz olan [donanım güvenlik modülü](https://en.wikipedia.org/wiki/Hardware_security_module) (HSM) kullanın. Anahtarları kimin yönetebildiğini, korunan veriyi kimin okuyabildiğinden ayırın; böylece anahtar saklama yetkisi görevler ayrılığını güvence altına alır. Bu, doğrudan bölüm 4.5'teki (gizlilik ve veri koruma) veri sınıflandırma ve saklama kurallarına bağlanır.

### Gizli bilgi yönetimini anahtar yönetiminden ayırın

Bunlar örtüşür ama aynı şey değildir. **Anahtar yönetimi**, kriptografik anahtarları ve yaşam döngülerini yönetir; genellikle sizin yerinize kripto işlemlerini yapan bir KMS ya da HSM içinde gerçekleşir, böylece ham anahtar asla dışarı çıkmaz. **Gizli bilgi yönetimi** ise hizmetlerin düz metin olarak alıp kullanması gereken uygulama kimlik bilgilerini (veritabanı parolaları, API belirteçleri, sertifikalar) yönetir; genellikle kısa ömürlü ve denetlenen erişim sunan bir gizli bilgi kasasından. Anahtarlar için bir KMS, kimlik bilgileri için bir gizli bilgi yöneticisi kullanın ve hiçbirini kaynak koda ya da sürüm kontrolüne işlenen ortam dosyalarına yapıştırmayın.

### PKI ve sertifika yaşam döngülerini otomatikleştirin

**Açık anahtar altyapısı (PKI)**, açık anahtarları kimliklere bağlayan sertifika otoriteleri, sertifikalar ve güven zincirleri sistemidir. Ölçekte baskın PKI riski, bir hizmeti durduran sürpriz sertifika süresi dolmasıdır. Her sertifikanın envanterini tutun, son kullanma tarihlerini izleyin ve düzenlemeyi ile yenilemeyi otomatikleştirin ki hiçbir insanın hatırlaması gerekmesin. Otomatik yenilenen kısa ömürlü sertifikalar, elle bakılan uzun ömürlü olanlardan daha güvenlidir, çünkü otomasyon insana bağlı tek hata noktasını ortadan kaldırır. Buradaki standart protokoller, satıcılar arası birlikte çalışabilirliği destekler (birlikte çalışabilirlik ve açık standartlara dair bölüm 3.8).

### Kriptografik çeviklik ve kuantum sonrasına geçiş için kurun

Algoritmalar zamanla zayıflar ve standartlar yer değiştirir. **Kriptografik çeviklik**, sistemleri acı verici bir yeniden yazım gerektirmeden algoritmaları ve anahtar boyutlarını değiştirebileceğiniz biçimde tasarlamak demektir: kriptoyu küçük bir arayüzün arkasına soyutlayın, şifreli verilerinizi sürümleyin ki hangi algoritmanın ürettiğini bilin ve neyi nerede kullandığınızın bir kripto envanterini tutun. Bu bugün önemlidir, çünkü [kuantum sonrası kriptografi](https://en.wikipedia.org/wiki/Post-quantum_cryptography), gelecekteki kuantum bilgisayarlara direnmek üzere tasarlanmış yeni algoritma ailesidir. Saldırganlar şifreli veriyi bugün toplayıp sonra çözebilir; bu yüzden uzun ömürlü gizli bilgilerin bir geçiş planına ihtiyacı vardır. Paniğe kapılmanıza gerek yok, ama envanterinizi bilmeniz ve standartlaştırılmış kuantum sonrası algoritmaları platformlar sunmaya başladıkça benimsemeye hazır olmanız gerekir.

### Gereken yerde doğrulanmış gerçeklemeleri tercih edin

Düzenlemeye tabi ve kamu sistemlerinde güçlü bir algoritma kullanmak yetmez; gerçekleme doğrulanmış olmalıdır. **FIPS 140** (Federal Bilgi İşleme Standardı 140), kriptografik modülleri doğrulamaya yönelik ABD standardıdır ve birçok sözleşme FIPS doğrulamalı kripto şart koşar. Kamu işleri ayrıca, gizli sistemler için NSA'nın Commercial National Security Algorithm (CNSA) paketi gibi ulusal rehberliği de izleyebilir. İnşa etmeden önce hangi rejimin geçerli olduğunu kontrol edin, çünkü doğrulanmış modülleri sonradan eklemek pahalıdır. Bu, uyum kanıtlarına ve yönetişime bağlanır (bölüm 4.6).

## Ödünleşimler: artılar ve eksiler

| Karar | Artılar | Eksiler |
|---|---|---|
| Sağlayıcı tarafından yönetilen KMS | Kolay, entegre, düşük operasyonel yük | Saklama yetkisi sağlayıcıda; daha az doğrudan denetim |
| Müşteri tarafından yönetilen anahtarlar / HSM | Tam saklama yetkisi, katı zorunlulukları karşılar | Operasyonel yük, anahtarları kaybetme riski |
| Otomatik kısa ömürlü sertifikalar | Sürpriz süre dolması yok, hızlı iptal | Baştan otomasyon yatırımı gerektirir |
| Uzun ömürlü sertifikalar | Basit, daha az hareketli parça | İnsan yönetimli süre dolmaları kesintilere yol açar |
| Zarf şifrelemesi | Ucuz anahtar döndürme, ana anahtarı korur | Anlaşılması gereken daha fazla hareketli parça |
| Baştan kriptografik çeviklik | Ucuz gelecek geçişleri | Şimdi ek soyutlama ve tasarım çabası |
| Erken kuantum sonrası benimseme | Uzun ömürlü gizli bilgileri korur | Olgunlaşmamış araçlar, daha büyük anahtarlar, bir miktar risk |

Temel gerilim, denetim ile operasyonel yük arasındadır. Anahtarlarınızı bir HSM'de tutmak azami saklama yetkisi verir ve en katı zorunlulukları karşılar, ama uzmanlık gerektirir ve yeni bir felaket riski yaratır: anahtarı kaybederseniz veriyi geri dönülmez biçimde kaybedersiniz. Sağlayıcı tarafından yönetilen hizmetler bu yükü kaldırır ama saklama yetkisini sağlayıcıya verir. Bunu katmanlayarak çözün: sistemlerin çoğu için makul varsayılanlara sahip yönetilen hizmetleri kullanın; müşteri tarafından yönetilen anahtarları ve HSM'leri, ek denetimin maliyete ve riske değdiği en yüksek sınıflandırmadaki veriye ayırın.

## Takımınızla tartışılacak sorular

1. **Anahtarlarınızın, sertifikalarınızın ve dayandığınız algoritmaların eksiksiz bir envanteri var mı?** Göremediğinizi döndüremez, taşıyamaz ya da denetleyemezsiniz; çoğu kurum, hizmetlere dağılmış, kimsenin takip ettiğinden çok daha fazla kriptografik malzemesi olduğunu keşfeder. Envanter, sonraki her kararın ön koşuludur: sertifika süresi izleme, anahtar döndürme, FIPS kapsamı belirleme ve kuantum sonrası planlama hepsi ona bağlıdır. Mevcut sertifikalarınızın ve son kullanma tarihlerinin bir listesini getirin; her birinin sahibini ve süresi dolduğunda neyin bozulduğunu sorun. Büyük bir yapıda dürüst cevap genellikle tek bir doğruluk kaynağının bulunmadığıdır ve bir tane kurmak en yüksek kaldıraçlı ilk adımdır. Bugün kriptonuzu sayamıyorsanız, çeviklik ve döndürme birer yetenek değil, birer arzudur.

2. **Ele geçirilmiş bir anahtarı hızlıca döndürebilir ya da iptal edebilir misiniz ve bunu hiç denediniz mi?** Döndürme ve iptal, anahtar yaşam döngüsünün yalnızca baskı altında önem kazanan parçalarıdır; takımlar bir olay sırasında bir anahtarın düzine yerde sabit kodlanmış olduğunu ya da iptalin gerçekte yayılmadığını sık sık keşfeder. Bir anahtarı döndürme ve bir sertifikayı iptal etme hedef sürenizi belirleyin, sonra ihtiyaç duymadan önce prova edin. Son kimlik bilgisi ifşanızın hikâyesini getirin ve döndürmenin pratikte neler gerektirdiğini adım adım gözden geçirin. Kurumsal ve kamu sistemlerinde, prova edilmemiş bir döndürme, uzun süren bir ifşa ile kendi kendine yol açılmış bir kesinti arasında seçim yapmak anlamına gelebilir. Döndürme hiç sınanmadıysa, çalışmadığını varsayın.

3. **Anahtar saklama yetkisi nerede duruyor ve görevler ayrılığını uyguluyor mu?** Bir anahtarı yönetebilen kişi ile onun koruduğu veriyi okuyabilen kişi aynı olmamalıdır, çünkü bu yetkileri birleştirmek durağan halde şifrelemenin amacını sessizce boşa çıkarır. Bu tercih ayrıca sağlayıcı tarafından yönetilen anahtarları, müşteri tarafından yönetilen anahtarları ya da HSM'leri kullanıp kullanmayacağınızı belirler; her birinin denetimi ve operasyonel riski farklıdır. Mevcut anahtar politikalarınızı getirin ve herhangi bir tek kimliğin hem bir anahtarı yönetip hem de arkasındaki düz metne erişip erişemediğini kontrol edin; bu yaygın bir sessiz açıktır. Düzenlemeye tabi ve gizli veriler için saklama kuralları, veri sınıflandırması (bölüm 4.5) ve zorunluluklar tarafından dayatılabilir. Saklama ve erişim ayrılmamışsa, şifrelemeniz sizi gösterge panosunun düşündürdüğünden daha az koruyor demektir.

4. **Zarf şifrelemenizi koruyan ana anahtar kaybolsa ya da yok edilse nasıl kurtarırdınız?** Müşteri tarafından yönetilen anahtarlar ve HSM'ler size saklama yetkisi verir, ama yeni bir felaket hata kipi de getirir: anahtar şifreleme anahtarını kaybederseniz, onun sardığı her veri şifreleme anahtarı ve arkasındaki veri kalıcı olarak okunamaz hale gelir. Bunu, çözmeye çalıştığınız saklama sorununu sessizce yeniden yaratan aşırı geniş bir yedeğin karşıt riskiyle tartın. Mevcut anahtar yedekleme ve emanet düzenlemelerinizi, her ana anahtarın etki alanını ve bir geri yüklemenin yalnızca belgelenmekle kalmayıp gerçekten yapıldığına dair kanıtı getirin. Kurumsal ve kamu yapılarında bunu veri sınıflandırma kurallarınıza bağlayın: en hassas anahtarlar çoğu zaman gelişigüzel kopyaları yasaklar; bu yüzden kurtarma bilinçli olarak tasarlanmalı, bir takvimle sınanmalı ve emekliye ayrılan anahtar malzemesinin imha edildiğini kanıtlama yönündeki herhangi bir düzenleyici gereklilikle uzlaştırılmalıdır.

5. **Sistemleriniz kuantum sonrası geçişe ne kadar hazır ve hangi uzun ömürlü gizli bilgileri önce taşırdınız?** Saldırganlar şifreli trafiği ve arşivleri bugün toplayıp kuantum bilgisayarlar olgunlaştığında çözebilir; bu yüzden yıllarca gizli kalması gereken her gizli bilgi, göremediğiniz bir geleceğe zaten açıktır. Rakip baskı şudur: kuantum sonrası araçlar hâlâ genç, anahtarlar daha büyük ve çok erken geçmek, yerleşmeden değişen bir algoritmaya bahis oynama riski taşır. Kripto envanterinizi, gizli kalma süresine göre sıralanmış bir gizli bilgi listesini ve mimarinizin yeniden yazım olmadan algoritma değiştirip değiştiremeyeceğine dair dürüst bir değerlendirmeyi getirin. Kamu ve düzenlemeye tabi işlerde, onlarca yıllık gizlilik zorunlulukları olan kayıtlar bunu kuramsal olmaktan çıkarıp somut kılar ve tedarik yakında belgelenmiş bir geçiş planı ve standartlaştırılmış kuantum sonrası algoritmalar için destek isteyebilir.

6. **Düzenleme doğrulanmış kriptografi gerektirdiğinde, hangi modüllerin kapsamda olduğunu ve bunların uygun olup olmadığını tam olarak biliyor musunuz?** Güçlü bir algoritma kullanmak, doğrulanmış bir gerçekleme kullanmakla aynı şey değildir ve takımlar, bir kütüphanenin, bir dil çalışma zamanının ya da bir bulut hizmetinin sözleşmenin şart koştuğu FIPS 140 sınırı kapsamında olmadığını geç fark eder. Gerilim şudur: doğrulanmış modüller özellik ve hız açısından güncel kütüphanelerin gerisinde kalabilir; bu yüzden onları seçmek yığınızı mühendislik açısından önemli biçimlerde kısıtlar. Düzenlemeye tabi her sistemin gerçekte çağırdığı kriptografik modüllerin listesini, bunları kapsayan doğrulama sertifikalarını ve geçerli olan özel zorunluluğu (FIPS 140, CNSA ya da bir sektör kuralı) getirin. Kurumsal ve kamu programlarında bunu inşa etmeden önce karara bağlayın; çünkü doğrulanmış modülleri sonradan eklemek ve bir sistemi yeniden yetkilendirmek pahalıdır, yavaştır ve çoğu zaman bitti sandığınız bileşenlerin yeniden tasarlanmasını gerektirir.

## Sektör merceği

**Girişim.** Tamamen platformunuzun denenmiş varsayılanlarına yaslanın ve özel kripto için sıfır mühendislik zamanı harcayın. Yönetilen durağan şifrelemeyi açın, TLS'yi otomatik yenilenen sertifikalarla sonlandırın, parolaları standart bir yavaş işlevle özetleyin ve gizli bilgileri depoda değil platformun gizli bilgi yöneticisinde tutun. Tek tasarım kararınız, uygulamada şifrelediğiniz birkaç alanın etrafında ince bir arayüzdür; böylece ileride sağlayıcı yönetimli anahtarlardan ayrılmak bir yeniden yazım olmaz.

**Küçük işletme.** Bir kriptografınız ve bir HSM işletme isteğiniz yok; bu yüzden saklama yetkisini kurmak yerine satın alın: bulutunuzla ya da SaaS araçlarınızla gelen sağlayıcı yönetimli KMS'yi ve gizli bilgi yöneticisini kullanın. İşi hijyen olarak çerçeveleyin: kodda anahtar yok, her yerde varsayılan olarak açık şifreleme ve hiçbir şey sürpriz biçimde bitmesin diye izlenen sertifika süreleri. Müşteri tarafından yönetilen anahtarları, bir sözleşmenin ya da düzenleyicinin gerçekten gerektirdiği nadir veriye ayırın.

**Kurumsal.** Sorun, binlerce hizmet, sertifika ve anahtar boyunca ölçek ve tutarlılıktır. Zarf şifrelemeli merkezi bir KMS çalıştırın, tüm sertifika yaşam döngüsünü otomatikleştirin ki hiçbir süre dolması elle bakılmasın ve döndürmeyi, FIPS kapsamını ve kuantum sonrası planlamayı besleyen tek bir kripto envanteri tutun. Anahtar saklama yetkisini veri erişiminden kurum çapında bir denetim olarak ayırın ve şifrelemeyi her takımın yeniden icat ettiği bir iş yerine, her takımın devraldığı bir platform yeteneği haline getirin.

**Kamu.** Tedarik, doğrulama ve denetim her seçimi şekillendirir. FIPS 140 doğrulamalı modüller kullanın ve gizli sistemler için CNSA gibi ulusal rehberliği izleyin; anahtar saklama yetkisini veri sınıflandırmasına bağlayın ki en hassas anahtarlar sıkı görevler ayrılığı altında yetkili personelin elinde dursun ve süregelen yetkilendirme için doğrulanmış kriptoya dair sürekli kanıt üretin. Onlarca yıl gizli kalması gereken kayıtlar için belgelenmiş bir kuantum sonrası geçiş planı hazırlayın ve satıcılardan, taahhütte bulunmadan önce hangi modüllerin doğrulanmış olduğunu açıklamalarını isteyin.

## Örnekler

**Girişim.** Bir sağlık takibi uygulaması geliştiren küçük bir takım tamamen denenmiş varsayılanlara yaslanır. TLS'yi otomatik yenilenen sertifikalarla sonlandırır, yönetilen veritabanında ve nesne depolamada sağlayıcının KMS'siyle durağan şifrelemeyi açar ve parolaları standart bir kütüphaneden yavaş, tuzlanmış bir işlevle özetler. Kendileri hiç kripto yazmak yerine, uygulamada şifrelemeleri gereken tek alan için üst düzey bir kimlik doğrulamalı şifreleme çağrısı kullanırlar. Gizli bilgiler platformun gizli bilgi yöneticisinde durur, asla depoda değil. Bunun maliyeti birkaç öğleden sonradır ve bütün bir felaket hataları kategorisini ortadan kaldırır.

**Kurumsal.** Küresel bir banka, merkezi bir KMS ve bir HSM filosu çalıştırır; binlerce hizmet boyunca her anahtarı ve sertifikayı izleyen bir kripto envanteri vardır. Zarf şifrelemesi müşteri verisini korur; veri anahtarları, veri yerinde dururken bir takvimle dönen ana anahtarlarla sarmalanır. Sertifika düzenleme ve yenileme, herkese açık bir kesinti tek bir süresi dolmuş sertifikanın maliyetini öğrettikten sonra tamamen otomatikleştirilmiştir. Anahtar yöneticileri uygulama mühendislerinden ayrı bir takımdır; böylece saklama yetkisi görevler ayrılığını güvence altına alır ve bir kriptografik çeviklik katmanı, uzun ömürlü arşivler için kuantum sonrası algoritmaları denemeye başlamalarını sağlar.

**Kamu.** Gizli kayıtları işleyen ulusal bir kurum yalnızca FIPS 140 doğrulamalı kriptografik modüller kullanır ve en yüksek sınıflandırmadaki sistemleri için NSA CNSA rehberliğini izler. Anahtarlar, düz metin anahtar malzemesini asla vermeyen HSM'lerde üretilir ve tutulur; saklama yetkisi veri sınıflandırmasına bağlıdır, böylece en hassas anahtarlar sıkı görevler ayrılığı altında yetkili personelin elinde durur. Sertifikalar, otomatik yaşam döngüleriyle yönetilen bir iç PKI üzerinde çalışır ve doğrulanmış kriptoya dair sürekli kanıt, kurumun süregelen yetkilendirmesini besler. Belgelenmiş bir kuantum sonrası geçiş planı, onlarca yıl gizli kalması gereken kayıtları korur.

## İş gerekçesi: motivasyonlar, YG ve TSM

Kriptografi, mütevazı bir yatırımın felaket boyutundaki, manşetlere çıkan kayıpları önlediği bir başka alandır. Toplam sahip olma maliyeti (TSM), bir KMS ya da HSM'yi, gizli bilgi ve sertifika yönetimi araçlarını ve yaşam döngülerini tasarlamak ve envanteri güncel tutmak için gereken mühendislik zamanını içerir. Bu maliyetler gerçektir ama sınırlıdır. Bunlardan kaçınmanın maliyeti ise şifrelenmemiş verinin ihlali, süresi dolmuş bir sertifikadan kaynaklanan saatler süren bir kesinti ya da yanlış yönetilmiş bir anahtardan doğan geri getirilemez bir veri kaybıdır; her biri düzenleyici cezalar, bildirim maliyetleri ve kalıcı itibar zararı getirir.

En güçlü yatırım getirisi (YG) otomasyondan ve yeniden kullanımdan gelir. Otomatik sertifika yaşam döngüleri, kendi kendine yol açılan en yaygın kesintiyi ortadan kaldırır. Makul varsayılanlara sahip merkezi anahtar yönetimi, her yeni hizmetin takım başına çaba harcamadan aktarım sırasında ve durağan halde şifrelemeyi devralması demektir; böylece kriptografi yinelenen bir vergiden bir platform yeteneğine dönüşür. Düzenlemeye tabi ve kamu işlerinde, doğrulanmış modüller ve otomatik kanıt, denetimlerin ve yetkilendirmenin maliyetini de düşürür. Liderliğe gerekçeyi anlatırken sade tutun: algoritmalar ücretsiz ve kanıtlanmıştır, risk anahtar yönetiminde ve sertifika operasyonlarında yaşar ve orada küçük, otomatik bir yatırım pahalı başarısızlıkları önler.

## Anti-kalıplar ve tuzaklar

- **Kendi kriptonuzu yazmak.** İnce, yalnızca uzmanların fark ettiği biçimlerde başarısız olan özel algoritmalar ya da elle yapılmış protokoller.
- **Koda gömülü anahtarlar ve gizli bilgiler.** Kaynak koda, yapılandırma dosyalarına ya da sohbete yapıştırılan, sızan ve döndürülemeyen kimlik bilgileri.
- **Anahtar disiplini olmadan şifreleme.** Şifrelemeyi açıp anahtar erişimini ardına kadar açık bırakmak ya da hiç döndürmemek.
- **Özetlemeyi şifrelemeyle karıştırmak.** Bir özeti geri döndürülebilir saymak ya da parolaları yavaş, tuzlanmış bir işlev yerine hızlı bir özetle saklamak.
- **Sertifika ruleti.** Envanter yok, süre izleme yok ve bir sertifika bitince periyodik sürpriz kesintiler.
- **Birleşmiş anahtar saklama yetkisi ve veri erişimi.** Hem bir anahtarı yönetip hem de onun koruduğu veriyi okuyabilen tek bir kimlik.
- **Döndürme planı olmaması.** Hiç döndürülmemiş ve baskı altında hızla döndürülemeyen anahtarlar.
- **Çevikliği olmayan kripto.** O kadar derine gömülmüş algoritmalar ki onları değiştirmek yeniden yazım gerektirir ve her gelecek geçişi engeller.
- **Doğrulama zorunluluklarını görmezden gelmek.** FIPS ya da benzeri doğrulamanın gerektiği yerde, doğrulanmamış modüllerde güçlü algoritmalar kullanmak.

## Olgunluk modeli

- **Düzey 1, Başlangıç:** Şifreleme tutarsızdır ve çoğunlukla yoktur; biri bir açığı fark ettiğinde tepkisel olarak uygulanır. Anahtarlar ve gizli bilgiler koda gömülüdür ya da sohbet ve yapılandırma dosyaları üzerinden gayriresmî biçimde paylaşılır. Envanter, döndürme yoktur, sertifikalar sürpriz biçimde sona erer ve takımlar ara sıra kendi kriptolarını yazar.
- **Düzey 2, Geliştirme:** TLS ve durağan şifreleme büyük sistemlerde açıktır ve bir KMS ya da gizli bilgi yöneticisi vardır, ama benimseme eşitsizdir ve takımdan takıma değişir. Bazı sertifikalar izlenirken bazıları izlenmez, döndürme elle ve seyrektir ve hepsini bir araya getiren eksiksiz bir kripto envanteri yoktur.
- **Düzey 3, Standartlaştırma:** Aktarım sırasında ve durağan halde şifreleme, kurum genelinde uygulanan belgelenmiş varsayılandır. Anahtarlar, zamanlanmış döndürme ve zarf şifrelemesiyle bir KMS'de yaşar, anahtar saklama yetkisi veri erişiminden ayrılmıştır, sertifika yaşam döngüleri otomatiktir, bir kripto envanteri tutulur ve düzenlemenin gerektirdiği her yerde doğrulanmış modüller kullanılır.
- **Düzey 4, Yönetme:** Kripto yapısı temel çizgilere göre ölçülür ve denetlenir. Sertifika süresi dolma öncesi süreyi, takvime göre döndürülen anahtarların yüzdesini, ele geçirilmiş bir anahtarı iptal etmenin ortalama süresini, dönem başına koddaki gizli bilgi tespitlerini ve envanter kapsamını izlersiniz ve bu metrikleri hedeflere karşı gözden geçirirsiniz. Döndürme ve iptal, kaydedilmiş sürelerle belirli aralıklarla prova edilir ve sapmalar fark edilmeden geçmek yerine düzeltici eylemi tetikler.
- **Düzey 5, Orkestrasyon:** Kriptografi, her hizmetin varsayılan olarak devraldığı bir platform yeteneğidir ve kurum genelinde sürekli iyileştirilip bütünleştirilir. Döndürme ve iptal hızlıdır ve rutin olarak uygulanır, HSM'ler en yüksek güvence gerektiren anahtarları korur ve kriptografik çeviklik ile etkin bir kuantum sonrası geçiş planı, algoritmalar ve zorunluluklar değiştikçe yapıyı uyumlu tutar. Uyum kanıtı otomatik üretilir ve süregelen yetkilendirmeyi besler.

## Tartışma fikirleri

1. Operasyonel maliyetleri ve felaket boyutundaki kayıp riskleri göz önüne alındığında, yapınızdaki hangi sistemler müşteri tarafından yönetilen anahtarları ya da HSM'leri haklı çıkarır?
2. Sahip olduğunuz her anahtar ve sertifika için tek bir doğruluk kaynağını nasıl kurar ve sürdürürdünüz?
3. Bugün ele geçirilmiş bir anahtarı döndürmenin gerçekçi süresi nedir ve onu yavaş yapan nedir?
4. Mimariniz bir kriptografik algoritmayı değiştirmeyi nerede zorlaştırıyor ve zorunlu bir geçişten önce bunu nasıl düzeltirdiniz?
5. Bir saldırgan bugün ele geçirip yıllar sonra çözseydi, uzun ömürlü gizli bilgilerinizden hangileri önem taşırdı?
6. Gizli bilgiler ve anahtarlar hiç koda, yapılandırmaya ya da günlüklere düşüyor mu ve bunu nasıl anlardınız?

## Önemli çıkarımlar

- **Kendi kriptonuzu yazmayın.** Denenmiş kütüphaneleri ve standart algoritmaları, güvenli olan en yüksek soyutlamada kullanın.
- **Algoritmalar kolay; anahtar yönetimi zor.** Bir anahtarın yaşam döngüsü (üretim, dağıtım, döndürme, iptal, imha) gerçek başarısızlıkların yaşadığı yerdir.
- **Garantilerinizi bilin:** simetrik ve açık anahtarlı şifreleme gizliliği korur, imzalar kimlik doğruluğunu ve bütünlüğü kanıtlar, özetleme ise kurcalamayı fark eder ama şifreleme değildir.
- **Aktarım sırasında güncel TLS ile, durağan halde zarf şifrelemesi ile şifreleyin;** her sistem için varsayılan olarak.
- **Anahtar saklama yetkisini veri erişiminden ayırın,** anahtarlar için bir KMS, kimlik bilgileri için bir gizli bilgi yöneticisi kullanın ve hiçbirini koda gömmeyin.
- **Sertifika yaşam döngülerini otomatikleştirin** ki sürpriz süre dolması kesintisi ortadan kalksın ve bir kripto envanteri tutun.
- **Kriptografik çeviklik için kurun** ve uzun ömürlü gizli bilgiler için bir kuantum sonrası geçiş planı başlatın.
- **Düzenleme ya da sınıflandırma gerektirdiği yerde doğrulanmış gerçeklemeleri tercih edin** (FIPS 140 ve geçerli ulusal rehberlik).

## Kaynaklar ve ileri okuma

- National Institute of Standards and Technology, *FIPS 140-3: Security Requirements for Cryptographic Modules*.
- National Institute of Standards and Technology, *SP 800-57: Recommendation for Key Management*.
- National Institute of Standards and Technology, *SP 800-131A: Transitioning the Use of Cryptographic Algorithms and Key Lengths*.
- National Institute of Standards and Technology, post-quantum cryptography standards (FIPS 203, 204, and 205).
- Niels Ferguson, Bruce Schneier, and Tadayoshi Kohno, *Cryptography Engineering*.
- Jean-Philippe Aumasson, *Serious Cryptography*.
- David Wong, *Real-World Cryptography*.
- Internet Engineering Task Force, *RFC 8446: The Transport Layer Security (TLS) Protocol Version 1.3*.
- Open Web Application Security Project, *Cryptographic Storage Cheat Sheet* and *Transport Layer Protection Cheat Sheet*.
- National Security Agency, *Commercial National Security Algorithm (CNSA) Suite* guidance.
