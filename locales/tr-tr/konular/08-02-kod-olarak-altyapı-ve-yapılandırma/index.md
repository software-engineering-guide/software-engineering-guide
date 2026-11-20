# 8.2 Kod olarak altyapı ve yapılandırma

## Genel bakış ve motivasyon

[Kod olarak altyapı](https://en.wikipedia.org/wiki/Infrastructure_as_code) (IaC), altyapıyı (ağlar, sunucular, veritabanları, yük dengeleyiciler, izinler) elle konsol tıklamalarıyla ya da geçici betiklerle değil, makine tarafından okunabilir tanım dosyalarıyla tanımlamak ve hazırlamak demektir. [Yapılandırma yönetimi](https://en.wikipedia.org/wiki/Configuration_management) aynı fikri, sistemler var olduktan sonra onların ayarlarına ve durumuna taşır. Birlikte, altyapıyı elle yapılmış, kırılgan bir ürün olmaktan çıkarıp, uygulama kodu için kullandığınız aynı mühendislik disiplininin sürümlenmiş, gözden geçirilebilir ve yeniden üretilebilir bir ürününe dönüştürürler.

Büyük takımlar için IaC bir kolaylık değil, bir zorunluluktur. Yüzlerce mühendisin ortama ihtiyacı olduğunda ve binlerce kaynağın bölgeler ve hesaplar arasında tutarlı kalması gerektiğinde, elle hazırlama yetişemez ve doğru kalamaz. İnsan eliyle yapılandırılan altyapı er ya da geç, kimsenin tam olarak anlamadığı ve bir arızadan sonra güvenilir biçimde yeniden kurulamayan benzersiz "kar tanesi" sunuculara kayar. Altyapıyı kodlamak onu tutarlı, denetlenebilir ve atılabilir kılar. Her ortam tanımından yeniden oluşturulabilir ve her değişiklik gözden geçirilebilir bir fark olur.

Kurumsal ve kamu kuruluşları bir fayda daha elde eder, hem de belirleyici olanı: uygulanabilir yönetişim. Dinlenme halinde şifreleme, ağ bölümleme, onaylı bölgeler ve maliyet dağıtımı için etiketleme gibi güvenlik ve uyum gereksinimleri doğrudan koda gömülebilir ve hiçbir şey hazırlanmadan önce otomatik olarak denetlenebilir. Altyapıyı sonradan denetleyip ihlallerin peşinden koşmak yerine, uyumsuz altyapının hiç var olmasını önlersiniz. Algılamadan önlemeye bu geçiş, IaC'nin modern platform uygulamasının temeli haline gelmesinin asıl nedenidir.

## Temel ilkeler

- Adımları anlatan zorunlu betikler yerine istenen durumu anlatan bildirimsel tanımları tercih edin.
- Bütün altyapı tanımlarını sürüm denetiminde saklayın ve diğer kodlar gibi gözden geçirin.
- Altyapıya değişmez davranın: yerinde değiştirmek yerine değiştirin (yenisini kurup eskisini kaldırın).
- Hazırlamayı eş güçlü yapın; böylece aynı tanımı tekrar tekrar uygulamak aynı sonucu verir.
- Kaymayı (canlı ortamın bildirilen tanımından ayrışması) sürekli algılayın ve uzlaştırın; doğru kaynak, canlı sistem değil koddur.
- Altyapıyı kopyala-yapıştır yerine yeniden kullanılabilir, sürümlenmiş modüllerden oluşturun.
- Politikayı kod olarak kodlayın (kurumsal kurallar makinece denetlenebilir kod olarak ifade edilir); böylece korkuluklar tavsiye değil otomatik olur.
- Sırları tanımların dışında tutun; ayrılmış bir sır yöneticisinden başvurun.

## Öneriler

### Bildirimsel araçları seçin ve modüller etrafında yapılandırın

[Terraform](https://en.wikipedia.org/wiki/Terraform_(software)), Pulumi ya da CloudFormation gibi bulut yerlisi bir seçenek gibi bildirimsel bir IaC aracı benimseyin ve parçalı bir araç manzarasından kaçınmak için kurum genelinde onda standartlaşın. Anahtar mimari uygulama modülerliktir: yaygın kalıpları (uyumlu bir ağ, sertleştirilmiş bir veritabanı, standart bir hizmet) yakalayan küçük, iyi belgelenmiş, sürümlenmiş modüller kurun. Takımlar sonra ortamlarını ham kaynaklar yazmak yerine bu modüllerden oluşturur. Bu, iyi varsayılanları ve güvenlik ayarlarını otomatik yayar ve tekrarı büyük ölçüde azaltır.

### Durumu bilinçli yönetin

Bildirimsel araçlar, kod ile gerçek kaynaklar arasındaki eşlemeyi bir durum dosyasında izler. Durumu uzaktan, ortak, şifreli, erişimi denetlenen bir arka uçta saklayın ve eşzamanlı değişikliklerin onu bozmaması için kilitleme kullanın. Durumu asla bir dizüstü bilgisayarda tutmayın ve son çare kurtarma eylemi dışında asla elle düzenlemeyin. Durum hassastır, çünkü kaynak üst verisi ve sırlar içerebilir; ona göre koruyun.

### Altın imajlarla değişmez altyapı kurun

Çalışan sunuculara yama yapmak yerine, sürümlenmiş bir "altın imaj" (önceden yapılandırılmış, sertleştirilmiş bir makine ya da kapsayıcı imajı) hazırlayın ve ondan yeni örnekler dağıtın. Bir değişikliğe ya da yamaya ihtiyaç duyduğunuzda yeni bir imaj üretin ve yayın, eski örnekleri emekliye ayırın. Bu, yapılandırma kaymasını ortadan kaldırır, geri almayı önemsizleştirir ve her örneği özdeş ve bilinen iyi bir derlemeye kadar izlenebilir tutar. Otomatik imaj işlem hatları güvenlik sertleştirmesini ve taramasını içermelidir; böylece uyum imaj düzeyinde yerleşik olur.

### Yapılandırma kaymasını algılayın ve uzlaştırın

Kayma, canlı ortam tanımından ayrıştığında olur; genellikle birinin acil bir elle değişiklik yapması yüzünden. Gerçek durumu bildirilen durumla karşılaştıran ve farkları işaretleyen düzenli kayma algılaması çalıştırın. Kaymaya bir kusur gibi davranın: elle yapılan değişikliği yerinde bırakarak değil, kodu güncelleyip yeniden uygulayarak uzlaştırın. Sürekli yapılandırma uygulaması gereken sistemler için, ana makineleri bildirilen durumlarına sürekli yakınsatan bir yapılandırma yönetimi aracı kullanın.

### GitOps ve çekmeye dayalı dağıtımı benimseyin

GitOps modelinde bir Git deposu sistemin bildirilen istenen durumunu tutar ve hedef ortamın içinde çalışan otomatik bir ajan bu durumu sürekli çeker ve canlı sistemi onunla eşleşecek biçimde uzlaştırır. Bu, geleneksel itme modelini tersine çevirir. Hiçbir dış sistemin ortamı değiştirmek için kalıcı kimlik bilgilerine ihtiyacı yoktur, çünkü ortam kendi yapılandırmasını kendisi çeker. GitOps size eksiksiz bir denetim izi (her değişiklik bir commit'tir), kolay geri alma (commit'i geri çevirin) ve güçlü kayma düzeltmesi (ajan istenen durumu sürekli yeniden dayatır) verir. [Kubernetes](https://en.wikipedia.org/wiki/Kubernetes) için ve tek, gözden geçirilebilir bir doğru kaynak isteyen kurumlar için özellikle güçlüdür.

### Korkulukları kod olarak politikayla uygulayın

İzin verilen bölgeler, zorunlu şifreleme, gerekli etiketler ve yasaklanmış herkese açık maruziyet gibi kurumsal kuralları, Open Policy Agent (OPA) gibi bir araçla ya da Sentinel gibi platforma özgü bir politika motoruyla makinece denetlenebilir politikalar olarak ifade edin. Bu denetimleri hazırlamadan önce işlem hattında çalıştırın; böylece ihlaller otomatik engellenir. Kod olarak politika, bir güvenlik takımının niyetini yürütülebilir, tek tip uygulanan bir denetime dönüştürür ve elle gözden geçirmenin asla olamayacağı biçimde binlerce değişikliğe ölçeklenir.

## Ödünleşimler: artılar ve eksiler

| Seçim | Artılar | Eksiler | En uygun olduğu yer |
|---|---|---|---|
| Bildirimsel IaC (Terraform/Pulumi) | Yeniden üretilebilir, gözden geçirilebilir, kayma algılanabilir | Öğrenme eğrisi; durum yönetimi karmaşıklığı | Ölçekteki hemen hemen tüm takımlar |
| Zorunlu betikler | Tanıdık; tek seferlik işler için esnek | Eş güçlü değil; denetlemesi ve tekrarı zor | Dar, geçiş dönemi durumları |
| Değişmez + altın imajlar | Kayma yok; önemsiz geri alma | İmaj derleme işlem hattı yükü | Tutarlılık gereken filolar |
| Değişken yapılandırma yönetimi | İnce taneli süregelen denetim | Kayma riski; daha yavaş yakınsama | Eski ya da uzun ömürlü ana makineler |
| GitOps (çekmeye dayalı) | Güçlü denetim izi; kendi kendini iyileştirme | Küme içi ajan ve Git disiplini gerekir | Kubernetes ve bulut yerlisi |
| Kod olarak politika | Otomatik, tek tip korkuluklar | Başlangıçta politika yazma emeği | Düzenlemeye tabi ortamlar |

Ana gerilim esneklik ile denetim arasındadır. Elle ve zorunlu yaklaşımlar tek bir değişiklik için daha hızlı hissettirir ama ölçekte sakatlayıcı hale gelen gizli tutarsızlık biriktirir. Bildirimsel, değişmez, politikayla yönetilen altyapı, daha fazla başlangıç yatırımı ve gerçek bir kültürel dönüşüm ister, çünkü mühendislerin hızlı konsol değişiklikleri yapmayı bırakması gerekir; ama bu yatırımı güvenilirlik, denetlenebilirlik ve her şeyi isteğe bağlı olarak yeniden kurabilme yeteneği olarak kat kat geri öder.

## Takımınızla tartışılacak sorular

1. **Ortak modül kitaplığının sahibi kim ve bir modüldeki iyileştirme onu kullanan her takıma nasıl ulaşır?** Modüller ancak düzeltmeler ve sertleştirilmiş varsayılanlar yayılırsa karşılığını verir ve bu, herkesin kopyaladığı bir klasör değil, net sahiplik ve gerçek sürümleme gerektirir. Uyumlu ağ ve sertleştirilmiş veritabanı modüllerini kimin sürdüreceğine, onları nasıl sürümleyeceğinize (değişiklik günlüğüyle anlamsal sürümleme) ve takımların yükseltmeleri bir yangın tatbikatı olmadan nasıl çekeceğine karar verin. Ölçekte bu, yanlış bir yapılandırmayı bir kez düzeltmekle onu binlerce elle düzenlenmiş kaynakta kovalamak arasındaki farktır. Kanıt getirin: aynı kalıbın bugün kaç ayrı kopyası var, bir güvenlik düzeltmesinin her ortama ulaşması ne kadar sürüyor ve takımlar modül sürümlerini sabitliyor mu yoksa kayan mı bırakıyor. Kritik bir yama bütün yapıya günler içinde ulaşamıyorsa, modülerliğiniz kozmetiktir.

2. **Kayma algılama sıklığınız nedir ve kayma bulunduğunda gerçekte ne olur?** Kayma, canlı ortamın bildirilen durumundan sessizce ayrışmasıdır; genellikle acil bir konsol değişikliğinden gelir ve onu hoş görmek kodunuzu kurguya çevirir. Gerçek durumu bildirilen durumla ne sıklıkla karşılaştıracağınıza karar verin (geceleyin makul bir varsayılandır) ve daha önemlisi yanıtı belirleyin: elle yapılan değişikliği yerinde bırakarak değil, kodu güncelleyip yeniden uygulayarak uzlaştırın. Düzenlemeye tabi ortamlarda bu bir denetim gereksinimidir, çünkü denetçilerin bildirilen durumun gerçekle sürekli eşleşmesine ihtiyacı vardır. Mevcut sayılarınızı getirin: her hafta kaç kaynak kayıyor, ne kadar süre kaymış kalıyor ve kapatmaktan kim sorumlu. Her kaymaya sahibi olan bir kusur gibi davranın; yoksa doğru kaynak garantisi, kimse koda güvenmeyene kadar aşınır.

3. **GitOps ve çekmeye dayalı uzlaştırmaya geçtiniz mi, yoksa üretimi değiştirmek için hâlâ bir dış sistem kalıcı kimlik bilgileri mi tutuyor?** Çekme modelinde hedef ortamın içindeki bir ajan canlı sistemi sürekli Git'e uzlaştırır; bu, herhangi bir dış sistemin yazma erişimi tutma ihtiyacını ortadan kaldırır ve istenen durumu yeniden dayattığı için kayma kendi kendine düzelir. Bu güçlü bir güvenlik ve denetim duruşudur, çünkü her değişiklik bir commit'tir ve hiçbir operatörün kalıcı üretim kimlik bilgilerine ihtiyacı yoktur. Maliyet gerçektir: çalıştırılacak bir küme içi ajan ve sıkı Git disiplini; bu yüzden mevcut itmeye dayalı otomasyonunuzla tartın. Şu anda üretimi doğrudan kimin ve neyin değiştirebildiğinin listesini ve bu değişikliklerin hangi denetim izini bıraktığını getirin. Kubernetes ve yüksek güvenceli kapalı alanlar için bu geçiş genellikle buna değer; bir avuç statik kaynak için gereğinden fazla olabilir.

4. **Altyapı durumunuz nasıl saklanıyor, kilitleniyor ve erişimi denetleniyor; ve bozulduğu ya da kaybolduğu gün ne olur?** Durum, kodunuzla gerçek kaynaklar arasındaki haritadır; bu yüzden kaybolan ya da hasar gören bir durum dosyası, bir aracı kendi yarattığı kaynaklara karşı kör bırakabilir ve birini yıkıcı bir yeniden uygulamaya itebilir. Büyük bir takım için risk katlanır, çünkü paylaşılan duruma karşı uygulama yapan birçok mühendisin, eşzamanlı çalışmaların birbirini ezmemesi için uzak, şifreli, kilitli bir arka uca ihtiyacı vardır. Tek büyük durumun rahatlığını yarattığı etki alanıyla tartın ve tek bir hatanın her şeyi çökertememesi için durumu ortam ya da alan başına bölmeyi düşünün. Gerçekleri getirin: durum bugün nerede duruyor, kilitleme zorunlu mu, onu kim okuyabilir (sır içerebilir) ve bir kurtarmayı hiç prova ettiniz mi. Kurumsal ve kamu ortamlarında durum arka ucuna kendi yedeği, denetim günlüğü ve kurtarma çalışma kitabı olan hassas, erişimi denetlenen bir varlık gibi davranın; çünkü onu kaybetmek, nelerin var olduğuna dair kaydınızı kaybetmektir.

5. **Gerçek bir acil durum elle değişiklik gerektirdiğinde onaylı cam kır (break-glass) yolu nedir ve bu değişiklik koda nasıl geri katılır?** Olgun her IaC uygulaması er ya da geç bir işlem hattını beklemenin kabul edilemez olduğu o sabaha karşı üçteki olayla karşılaşır; dürüst soru elle değişikliklerin olup olmadığı değil, onları nasıl sınırladığınızdır. İşlem hattını kimin atlayabileceğine, nelere dokunmalarına izin verildiğine, eylemin nasıl kaydedileceğine ve değişikliğin koda uzlaştırılması ya da geri alınması gereken son tarihe önceden karar verin. Bu anlaşma olmadan acil durum istisnası sessizce günlük alışkanlığa dönüşür ve ClickOps arka kapıdan geri gelir. Kanıt getirin: geçen çeyrekte kaç bant dışı değişiklik oldu, her biri ne kadar uzlaştırılmadan kaldı ve kayma algılaması bunları gerçekten yakaladı mı. Düzenlemeye tabi ve kamu kuruluşlarında, otomatik kayıtlı belgelenmiş bir cam kır prosedürü çoğu zaman bir denetim gereksinimidir; çünkü denetçiler hem acil durumların mümkün olmasını hem de her birinin bir iz bırakıp sistemi bildirilen durumuna döndürmesini bekler.

6. **Güvenlik ve uyum temelinizin ne kadarı kötü bir değişikliği otomatik engelleyen politika olarak ifade ediliyor, ne kadarı bir belgede duran ve birinin hatırlamasına dayanan kurallar?** Wiki'de düzyazı olarak yazılan korkuluklar rutin olarak ihlal edilir, çünkü her mühendisin onları son tarih baskısı altında okuyup uygulamasına bağlıdır; aynı kurallar kod olarak politika biçiminde ifade edildiğinde uyumsuz bir değişikliği hiç hazırlanmadan reddeder. Büyük bir kurum için bu, bir güvenlik takımının niyetinin bir gözden geçirme darboğazı olmadan binlerce değişikliğe ölçeklenmesinin tek yoludur. Politikaları yazmanın ve sürdürmenin başlangıç maliyetini, elle gözden geçirmenin ve sonradan düzeltmenin yinelenen maliyetiyle tartın ve hangi denetimlerin (şifreleme, onaylı bölgeler, zorunlu etiketler, herkese açık maruziyet yok) sert kapı olarak uygulanacak kadar pazarlık dışı olduğuna karar verin. Mevcut temel kurallarınızın listesini getirin ve hangilerinin otomatik, hangilerinin tavsiye olduğunu, ayrıca her birinin pratikte ne sıklıkla ihlal edildiğini işaretleyin. Kurumsal ve kamu bağlamlarında otomatik politika, bir denetimi haftalarca süren elle kanıt toplamadan, uygulanan denetimlere karşı bir sorguya çevirir ve uyumu algılamadan önlemeye dönüştürür.

## Sektör merceği

**Girişim.** Hız kazanır; bu yüzden bütün yığınınızı tek bir bildirimsel depoya koyun (Terraform yaygın bir varsayılandır), durumu yönetilen şifreli bir arka uçta tutun ve üç kişilik bir takımda bile her değişikliği bir çekme isteğinden geçirin. Ağır platform aygıtından kaçının: merkezî modül takımı yok, henüz politika motoru yok, yalnızca sürüm denetimi ve konsolda asla tıklamama disiplini. Bu tek başına, maliyeti düşürmek için yıkabileceğiniz ve bir sonraki demo için yeniden kurabileceğiniz yeniden üretilebilir ortamlar verir.

**Küçük işletme.** Özel bir platform uzmanı yoksa, bakımını yapamayacağınız özel araçlar kurmak yerine yönetilen hizmetlere ve bulut sağlayıcınızın ya da satıcınızın zaten desteklediği IaC'ye yaslanın. Çalıştıracak kimsenizin olmadığı bir altın imaj işlem hattı kurmak yerine, makul varsayılanları (şifreleme, yedekler, yamalama) sizin için halledilen barındırılan bir platformu satın almayı tercih edin. Hedefi dar çerçeveleyin: bir avuç kritik kaynağınızı koda alın; böylece bir arızadan ya da ayrılan bir yükleniciden sonra onları yeniden kurabilirsiniz.

**Kurumsal.** Temel sorun birçok takım, hesap ve bölge arasında tutarlılıktır; bu yüzden sürümlü ortak bir modül kitaplığına, uzak kilitli duruma ve işlem hattında uygulanan kod olarak politikaya yatırım yapın. Merkezî bir platform takımı sertleştirilmiş modüller ve korkuluklar yayımlar, ürün takımları bunların içinde self servis çalışır ve kayma algılaması sürekli çalışarak binlerce kaynağı bilinen bir durumda tutar. Modülleri ve politikaları sürdürmenin süregelen maliyetini bütçeleyin, çünkü değerleri bir düzeltmenin ya da sertleştirilmiş bir varsayılanın her yere aynı anda yayılmasından gelir.

**Kamu.** Tedarik kuralları, akreditasyon ve kamusal hesap verebilirlik sizi değişmez altyapıya, imzalı commit'lere ve akredite edilmiş bir kapalı alanın içinde GitOps uzlaştırmasına iter; böylece hiçbir operatör üretimi değiştirmek için kalıcı kimlik bilgilerine sahip olmaz. Gereken güvenlik temelini altın imajlara ve kod olarak politikaya kodlayın ve commit geçmişinin kurcalanmaya karşı belirgin, sürekli erişilebilir denetim kanıtı olarak hizmet etmesine izin verin. Sizi hapseden tescilli biçimler yerine açık, taşınabilir araçları tercih edin ve cam kır prosedürünü ve kaydını açık kılın; böylece acil değişiklikler de yapılandırma denetimi gereksinimlerini karşılar.

## Örnekler

**Girişim.** Beş kişilik bir girişim, VPC'si, veritabanı ve kapsayıcı hizmeti dahil bütün AWS kurulumunu, durumu şifreli bir S3 arka ucunda ve kilitlemesi DynamoDB ile tutulan tek bir Terraform deposunda tanımlar. Her değişiklik bir çekme isteğinden geçer; bu yüzden tek başına nöbet tutan bir mühendis bile apply çalıştırmadan önce tam olarak neyin değişeceğini görebilir. Büyük bir demo için yeni bir hazırlık ortamına ihtiyaç duyduklarında küçük bir modülü kopyalayıp dakikalar içinde ayağa kaldırırlar ve bulut faturasını düşük tutmak için aynı hızda yıkarlar.

**Kurumsal.** Çok uluslu bir perakendeci, birkaç bulut hesabı ve bölge boyunca altyapıyı yönetir. Merkezî bir platform takımı uyumlu ağlar, veritabanları ve hizmet iskeleleri için sürümlü Terraform modülleri yayımlar ve şifrelemesi ya da maliyet dağıtımı etiketleri olmayan her kaynağı reddeden OPA politikaları uygular. Ürün takımları kendi ortamlarını self servis hazırlar, ama her değişiklik politikanın otomatik denetlendiği işlem hattından akar. Kayma algılaması geceleri çalışır ve her elle değişiklik için bilet açar; bu, binlerce kaynağı sürekli bilinen, uyumlu bir durumda tutar.

**Kamu.** Yüksek güvenceli bir ortamda çalışan bir savunma kurumu, gereken güvenlik temelini gömen sertleştirilmiş altın imajlar kurar ve yalnızca bu imajlardan değişmez örnekler dağıtır. Bütün altyapı Git'te bildirilir ve akredite edilmiş kapalı alanın içindeki bir GitOps ajanı tarafından uzlaştırılır; böylece hiçbir operatör üretimi doğrudan değiştirmek için kalıcı kimlik bilgilerine sahip olmaz. Her değişiklik imzalı bir commit'tir. Bu, denetçilere eksiksiz, kurcalanmaya karşı belirgin bir geçmiş verir ve elle kanıt toplamadan sürekli izleme ve yapılandırma denetimi gereksinimlerini karşılar.

## İş gerekçesi: motivasyonlar, YG ve TSM

IaC'nin YG'si hız, güvenilirlik ve risk azaltmadan gelir. Bir zamanlar haftalarca bilet güdümlü elle hazırlama gerektiren ortamlar dakikalar içinde yaratılabilir; bu mühendisleri serbest bırakır ve projeleri hızlandırır. Yeniden üretilebilirlik, arızalardan sonra kurtarma süresini büyük ölçüde azaltır, çünkü her ortam koddan yeniden kurulabilir. Otomatik politika uygulaması, güvenlik olaylarının ve denetim bulgularının sıklığını ve maliyetini düşürür; düzenlemeye tabi kurumlar için bu önemli olabilir.

TSM defterinde benimseme maliyetleri arasında araçlar, eğitim, bir modül ve politika kitaplığı kurmak ve elle değişiklik yapmayı bırakma disiplini yer alır. Benimsememenin maliyeti daha diktir ve zamanla bileşik büyür: kimsenin yeniden kuramadığı kar tanesi altyapı, yavaş ve hataya açık hazırlama, ihlallere yol açan güvenlik yanlış yapılandırmaları ve haftalarca elle emek tüketen denetimler. Yönetim için IaC'yi, altyapıyı yönetilmeyen bir yükümlülükten yönetilen, yeniden üretilebilir bir varlığa dönüştürmek ve güvenliği ile uyumu hedef olmaktan çıkarıp otomatik kılan mekanizma olarak çerçeveleyin.

## Anti-kalıplar ve tuzaklar

- **Üretimde ClickOps.** Konsolda elle değişiklik yapmak kaymayı garanti eder ve yeniden üretilebilirliği yok eder.
- **Kodda sırlar.** Kimlik bilgilerini tanım dosyalarına gömmek onları sürüm geçmişine ve duruma sızdırır.
- **Monolitik, modülsüz tanımlar.** Kimsenin değiştirmeye cesaret edemediği dev bir yapılandırma, yerini aldığı elle kurulum kadar kırılgan hale gelir.
- **Yönetilmeyen durum.** Yerel ya da kilitlenmemiş durum dosyaları bozulmaya ve kaybolan altyapıya yol açar.
- **Hoş görülen kayma.** Elle değişiklikleri yerinde bırakmak, kod kurguya dönene kadar doğru kaynak garantisini aşındırır.
- **Belge olarak politika.** Otomatik bir denetim yerine wiki'de duran kurallar rutin olarak ihlal edilir.
- **Kopyala-yapıştır çoğalması.** Yapılandırmayı takımlar arasında çoğaltmak, düzeltmelerin ve iyileştirmelerin asla yayılmaması demektir.

## Olgunluk modeli

**Düzey 1, Başlangıç.** Altyapı konsol ve geçici betiklerle elle hazırlanır. Ortamlar tutarsız, belgelenmemiş ve güvenilir biçimde yeniden üretilemez; arızadan kurtarma yavaş ve belirsizdir.

**Düzey 2, Geliştirme.** Altyapının bir kısmı kodlanmıştır ama uygulamalar takıma göre değişir. Durum yönetimi tutarsızdır, kayma yaygındır, sırlar bazen tanımlara sızar ve politika, varsa, elle gözden geçirmeyle uygulanır.

**Düzey 3, Standartlaştırma.** Bildirimsel IaC, yönetilen, uzak, kilitli durumla paylaşılan sürümlü modüllerden kurulu olarak kurum genelinde belgelenmiş standarttır. Kod olarak politika korkulukları işlem hattında uygular, sırlara ayrılmış bir yöneticiden başvurulur ve kayma algılaması düzenli aralıklarla çalışır.

**Düzey 4, Yönetme.** Uygulama temel çizgilere göre ölçülür. Kayma oranını ve ortalama uzlaştırma süresini, takımlar arasında modül sürümü benimsemeyi, engellenen ve kaçan politika ihlallerini, hazırlama teslim süresini ve gerçekten kod altında olan kaynakların payını izlersiniz. Bu ölçütler değişiklikleri kapılar ve yatırımı yönlendirir; böylece kararlar anekdota değil kanıta dayanır.

**Düzey 5, Orkestrasyon.** Altyapı değişmez ve GitOps güdümlüdür, kaymaya karşı kendi kendini iyileştirir ve uyum kanıtı otomatik üretilir. Modül ve politika kitaplığı gerçek kullanımdan ve olaylardan sürekli iyileşir; altyapı uygulaması güvenlik, maliyet ve teslimat planlamasıyla bütünleşir; böylece gereksinimler kaydıkça bütün yapı uyum sağlar.

## Tartışma fikirleri

- Merkezî olarak yönetilen modüller ile takımların özel altyapı tanımlama özerkliği arasındaki çizgi nerede durmalı?
- İşlem hattını atlaması gereken gerçek acil değişikliği, ClickOps'u olağanlaştırmadan nasıl ele alırsınız?
- Durumu birçok hesap ve takım arasında yönetmek ve korumak için doğru strateji nedir?
- Değişken yapılandırma yönetimi ne zaman hâlâ haklı, ne zaman tümüyle değişmez altyapı?
- Kod olarak politika kitaplığını gelişen güvenlik ve düzenleyici gereksinimlerle nasıl uyumlu tutarsınız?
- IaC'den önce var olan eski altyapı için gerçekçi bir geçiş yolu nasıl görünür?

## Önemli çıkarımlar

- Altyapıyı bildirimsel tanımlayın, sürümleyin ve gözden geçirilebilir, yeniden üretilebilir kod olarak ele alın.
- İyi varsayılanları yaymak ve tekrarı ortadan kaldırmak için küçük, sürümlü modüllerden kurun.
- Kaymayı ortadan kaldırmak ve geri almayı basitleştirmek için değişmez altyapıyı ve altın imajları tercih edin.
- Durumu bilinçli yönetin ve sırları tanımların dışında tutun.
- Güçlü bir denetim izi ve kendi kendini iyileştiren uzlaştırma için GitOps'u benimseyin.
- Korkulukları kod olarak politikayla uygulayın; böylece uyum sonradan denetlenmek yerine var olmaması sağlanarak önlenir.

## Kaynaklar ve ileri okuma

- Kief Morris, *Infrastructure as Code: Dynamic Systems for the Cloud Age*.
- Yevgeniy Brikman, *Terraform: Up & Running*.
- Betsy Beyer, Chris Jones, Jennifer Petoff, and Niall Richard Murphy (eds.), *Site Reliability Engineering*.
- Gene Kim, Jez Humble, Patrick Debois, and John Willis, *The DevOps Handbook*.
- Weaveworks, "GitOps" foundational writings (Alexis Richardson et al.).
- Open Policy Agent documentation and the Rego policy language.
- NIST Special Publication 800-53, security and privacy controls (configuration management family).
