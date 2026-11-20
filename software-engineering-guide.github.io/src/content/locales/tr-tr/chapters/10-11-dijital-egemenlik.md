# 10.11 Dijital egemenlik

## Genel bakış ve motivasyon

[Dijital egemenlik](https://en.wikipedia.org/wiki/Digital_sovereignty), bir kuruluşun, ulusun ya da bloğun kendi verisi, yazılımı ve altyapısı üzerinde anlamlı bir denetimi ne ölçüde elinde tuttuğudur. Bu, verinin fiziksel olarak nerede bulunduğu, hangi yasaların ve hükümetlerin ona erişimi zorunlu kılabileceği ve kritik sistemlerin yabancı bir güce ya da tek bir tedarikçiye bağımlı olmadan çalışmaya devam edip edemeyeceği üzerindeki denetim demektir. Birkaç boyutu vardır: **[veri egemenliği](https://en.wikipedia.org/wiki/Data_sovereignty)** (verinin hangi yargı yetkisi ve yasalar tarafından yönetildiği), **operasyonel egemenlik** (sistemleri bir üçüncü tarafın izni ya da varlığı olmadan çalıştırma ve yönetme yeteneği), **yazılım egemenliği** (kaynağa ve onun evrimine erişim ve denetim) ve **tedarik zinciri egemenliği** (donanım, hizmetler ve bağımlılıklardaki boğaz noktalarından kurtulma özgürlüğü). Bu bölüm yönetim bölümünde yer alır, çünkü egemenlik özünde derin teknik sonuçları olan bir strateji, satın alma ve risk kararıdır (bölüm 10.1–10.3).

Motivasyon kuramsaldan acil olana geçti. [Bulut bilişim](https://en.wikipedia.org/wiki/Cloud_computing) dünya altyapısının büyük bölümünü, çoğunlukla tek bir ülkenin yargı yetkisi altındaki bir avuç sağlayıcıda topladı. ABD [CLOUD Act](https://en.wikipedia.org/wiki/CLOUD_Act) gibi ülke sınırlarını aşan yasalar (bir sağlayıcıyı, verinin nerede saklandığına bakmaksızın ifşaya zorlayabilir), AB'nin [GDPR](https://en.wikipedia.org/wiki/General_Data_Protection_Regulation) gibi rejimleriyle çatışır; bu gerilim, AB-ABD Gizlilik Kalkanı'nı geçersiz kılan *[Schrems II](https://en.wikipedia.org/wiki/Schrems_II)* kararıyla somutlaştı. Buna jeopolitik şokları, yaptırımları ve bir sağlayıcının bağlantısının kesilme riskini ekleyin; bağımlılık yalnızca tedarikçi yönetimine düşülmüş bir dipnot değil, stratejik bir kırılganlık olur. Egemenlik, en kritik sistemlerinizin ve verinizin o bağımlılığın ne kadarını güvenle taşıyabileceğine bilinçle karar verme disiplinidir.

Kurumsal yapılar ve özellikle kamu için bahisler doğrudandır. Çok uluslu şirketler çatışan veri koruma rejimlerini uzlaştırmak ve bir düzenleyicinin ya da jeopolitik bir olayın varoluşsal bir geçişe çevirebileceği kilitlenmeden kaçınmak zorundadır. Hükümetler, yabancı bir yargı yetkisine maruz kalması bir ulusal güvenlik ve kamu güveni meselesi olan verileri (sağlık kayıtları, vergi, savunma, vatandaş kimliği) tutar. "Egemen bulut" tekliflerinin, AB'nin [Gaia-X](https://en.wikipedia.org/wiki/Gaia-X) gibi girişimlerinin ve Fransa'nın SecNumCloud'u gibi ulusal sertifikaların ortaya çıkmasının nedeni budur. Amaç otarşi, yani tam kendi kendine yeterlilik değildir. Amaç, tehlikede olanın duyarlılığına uygun, orantılı denetimdir.

## Temel ilkeler

- **Egemenlik bir anahtar değil, bir tayftır.** Denetim derecesini verinin ve iş yükünün duyarlılığına uydurun.
- **Konum, yargı yetkisi değildir.** Yerelde saklanan veriye yine de yabancı bir hükümet yasal olarak erişebilir; yalnızca ikamet etmek egemenlik değildir.
- **Çıkış için tasarlayın.** Bir sağlayıcıdan ayrılabilme yeteneği egemenliğin en gerçek ölçüsüdür.
- **[Açık standartlar](https://en.wikipedia.org/wiki/Open_standard) ve [açık kaynak](https://en.wikipedia.org/wiki/Open-source_software) bağımlılığı azaltır:** bunlar yalnızca maliyet tasarrufu sağlayan şeyler değil, stratejik özerklik araçlarıdır.
- **Anahtarları denetleyin.** Şifreleme anahtarlarını kimin tuttuğu ve denetlediği, baytların nerede durduğundan çoğu zaman daha önemlidir.
- **Bir kilitlenmeyi başka bir kilitlenmeyle değiştirmeyin.** Tek bir "egemen" tedarikçi, bir hiper ölçekleyici kadar esir alıcı olabilir.
- **Orantılı olun.** Egemenliğin gerçek maliyetleri vardır; her yerde aşırıya kaçmak parayı israf eder ve teslimatı yavaşlatır.

## Öneriler

### Veriyi ve iş yüklerini egemenlik duyarlılığına göre sınıflandırın

Her şeyin aynı korumaya ihtiyacı yoktur. Veriyi ve sistemleri, yabancı yargı yetkisinin erişiminin ya da sağlayıcı kaybının sonucuna göre sınıflandırın. Kamuya açık ve düşük riskli iş yükleri ölçek ve maliyet için küresel hiper ölçekli altyapıda durabilir. Yüksek duyarlılıklı veri (ulusal güvenlik, sağlık, vatandaş kimliği, düzenlemeye tabi kayıtlar) daha güçlü egemenlik denetimleri gerektirir. Bölüm 4.5'teki veri sınıflandırmasıyla aynı risk temelli mantık olan bu katmanlama, egemenliği ödenebilir kılar: pahalı denetimleri her şeyi yerelleştirmek yerine haklı oldukları yere yoğunlaştırır.

### Yalnızca ikameti değil, yargı yetkisini anlayın

**Veri ikameti** (verinin saklandığı fiziksel ya da coğrafi konum) gereklidir ama yeterli değildir. Hukuken önemli olan *yargı yetkisidir*: hangi hükümetler, hangi yasalar uyarınca ifşayı zorunlu kılabilir. Merkezi yabancı bir ülkede olan bir sağlayıcının işlettiği ülke içindeki bir veri merkezinde tutulan bir veri kümesine, o sağlayıcının kendi ülkesinin yasası uyarınca yine de erişilebilir (CLOUD Act sorunu). Her sistemin hukuki maruziyetini haritalandırın: sağlayıcının merkezi, geçerli yasalar ve herhangi bir yeterlilik kararı ya da aktarım mekanizması (Standart Sözleşme Maddeleri, AB-ABD Veri Gizliliği Çerçevesi). Sonra bu hukuki haritayı mimarinin birinci sınıf bir parçası olarak ele alın (bölüm 4.5, 4.6).

### Taşınabilirlik ve geri döndürülebilirlik için tasarlayın

En dayanıklı egemenlik denetimi, inandırıcı bir çıkıştır. Açık standartları ve taşınabilir biçimleri tercih edin (bölüm 3.8). İş yüklerini taşınabilmeleri için konteynerleştirin. Bir ortam başka yerde yeniden kurulabilsin diye kod olarak altyapıyı koruyun (bölüm 8.2). En kritik sistemleriniz için tek bir sağlayıcının tescilli hizmetlerine derinlemesine bağımlı olmaktan kaçının. Bir çıkış planını sürdürün ve düzenli aralıklarla *sınayın*: verinin ve yapılandırmanın emanete alınması artı alternatif bir sağlayıcıya prova edilmiş bir yol; böylece "gerekirse ayrılabilirdik" bir umut değil, gösterilmiş bir olgu olur. Bu, **[tedarikçi kilitlenmesinin](https://en.wikipedia.org/wiki/Vendor_lock-in)**, yani engelleyici bir maliyet ya da aksama olmadan sağlayıcı değiştirememe durumunun panzehiridir.

### Gerekçe olan yerde egemen altyapı ve anahtar denetimi kullanın

En duyarlı katman için daha güçlü teknik denetimler vardır: **egemen bulut** teklifleri (yargı yetkisi içindeki kuruluşlarca işletilen ya da onlarla ortak çalışılan, bazen SecNumCloud gibi sertifikalı bulut bölgeleri), **[gizli hesaplama](https://en.wikipedia.org/wiki/Confidential_computing)** (veriyi işlenirken bile şifreli tutan donanım tabanlı güvenilir yürütme) ve müşteri denetimindeki şifreleme anahtarları: **kendi anahtarını getir (BYOK)** ve daha güçlüsü, sağlayıcının veriyi açan anahtarlara hiç erişemediği **kendi anahtarını tut (HYOK)**. Anahtarları denetlemek, paylaşılan altyapıda bile egemenliğin pratik yararının büyük kısmını sağlayabilir. Bir sağlayıcının şifresini çözemediği veri, onun anlamlı biçimde ifşa edemeyeceği veridir.

### Stratejik özerklik için açık kaynağı ve açık ekosistemleri tercih edin

Açık kaynak yazılım ve açık standartlar, tek tedarikçi kapatma düğmesini ortadan kaldırdıkları için en güçlü egemenlik kaldıraçları arasındadır. Kaynak, herhangi bir tedarikçiden bağımsız olarak çalıştırılabilir, denetlenebilir, çatallanabilir ve sürdürülebilir (bölüm 10.3, 3.8). Kamu sektörünün "kamu parası, kamu kodu" politikaları ve Gaia-X gibi girişimler bunu yansıtır. Açık kaynak kendiliğinden egemen değildir. Onu çalıştıracak ve destekleyecek yetenekli insanlara yine ihtiyaç duyar ve tedarik zincirinin güvenliğinin sağlanması gerekir (bölüm 4.2). Ama bir tedarikçiye bağımlılığı bir topluluğa ve kendi yeteneğinize bağımlılığa dönüştürür; bunu denetlemek çok daha kolaydır.

### Egemenliği mutlak değil, orantılı bir risk olarak yönetin

Diğer yönetişiminizin yanında bir egemenlik risk çerçevesi kurun (bölüm 10.2, 1.5). Başlıca platformların yoğunlaşma ve yargı yetkisi riskini değerlendirin. Her veri katmanı için hedef egemenlik düzeylerine karar verin ve bunları maliyet, yetenek ve teslimat hızıyla tartın. Amaç, savunulabilir, belgelenmiş bir duruştur ("bu iş yükleri hiper ölçekli bağımlılığı kabul eder; bunlar yargı yetkisi içinde denetim gerektirir; çıkış duruşumuz şudur"); jeopolitik ve düzenleme değiştikçe gözden geçirilen, bir kerelik mutlak bir tutum değil.

## Ödünleşimler: artılar ve eksiler

| Yaklaşım | Artılar | Eksiler |
|---|---|---|
| **Küresel hiper ölçekli bulut** | Ölçek, özellikler, düşük maliyet, hız | Yargı yetkisi maruziyeti; yoğunlaşma ve kilitlenme riski |
| **Egemen bulut / yargı yetkisi içindeki sağlayıcı** | Hukuki denetim; ulusal güvenliğe uygunluk; güven | Daha yüksek maliyet; daha az özellik; çoğu zaman daha küçük ölçek; yeni kilitlenme |
| **Paylaşılan altyapıda anahtar denetimi (BYOK/HYOK)** | Yararın büyük kısmı daha düşük maliyetle; ölçeği korur | Operasyonel karmaşıklık; anahtar yönetimi riski; mutlak değil |
| **Açık kaynak / kendi barındırma** | Denetlenebilirlik, çatallanabilirlik, tedarikçi kapatma düğmesi yok | Kurum içi yetenek gerektirir; operasyonlar ve güvenlik size aittir |
| **Veri yerelleştirme zorunlulukları** | Mevzuata uyum; siyasi güvence | Maliyetli; veriyi parçalar; dayanıklılığı ve kullanışlılığı azaltabilir |

Belirleyici gerilim **denetim ile yetenek ve maliyet** arasındadır. Azami egemenlik (kendi barındırma, yargı yetkisi içinde, açık kaynak, tamamen taşınabilir) küresel platformların ölçeğinden, özelliklerinden ve hızından ödün verir. Azami yetenek, bağımlılığı ve yargı yetkisi maruziyetini kabul eder. Çözüm katmanlamadır: sonucun haklı çıkardığı yerde egemenliğe ödeyin, haklı çıkarmadığı yerde pragmatik bağımlılığı kabul edin.

## Takımınızla tartışılacak sorular

1. **Veriyi ve iş yüklerini egemenlik duyarlılığına göre katmanlandırdık mı, böylece pahalı denetimler yalnızca haklı oldukları yere mi düşüyor?** Egemenlik bir anahtar değil bir tayftır ve her şeyi yerelleştirmek parayı yakar, yeteneği kaybettirir ve seçeneklerinizi daralttığı için dayanıklılığı bile azaltabilir. Her sistemi yabancı yargı yetkisinin erişiminin ya da sağlayıcı kaybının sonucuna göre sınıflandırın: kamuya açık ve düşük riskli iş yükleri küresel hiper ölçekli altyapıda durabilirken, ulusal güvenlik, sağlık ya da vatandaş kimliği verisi daha güçlü denetimler gerektirir. Bu, veri sınıflandırmasıyla aynı risk temelli mantıktır ve egemenliği ödenebilir tutan şeydir. Taç mücevheri sistemlerinizi ve mevcut barındırmalarını getirin ve korumanın duyarlılıkla örtüşüp örtüşmediğini sorun. Her şeyi eşit düzeyde koruyorsanız, neredeyse kesinlikle bir yerde fazla ödüyor, başka bir yerde de açıkta kalıyorsunuz.

2. **Açık standartlar ve açık kaynak egemenlik stratejimizin parçası mı, yoksa onlara yalnızca maliyet tasarrufu sağlayan şeyler olarak mı bakıyoruz?** Çalıştırabileceğiniz, denetleyebileceğiniz, çatallayabileceğiniz ve sürdürebileceğiniz kaynak, elinizdeki en güçlü özerklik kaldıraçlarından biri olan tek tedarikçi kapatma düğmesini ortadan kaldırır. Açık standartlar ve taşınabilir biçimler inandırıcı bir çıkışı mümkün kılan şeydir ve inandırıcı bir çıkış egemenliğin en gerçek ölçüsüdür. Daha ince tuzak, bir hiper ölçekleyiciden kaçıp çıkışı olmayan tek bir "egemen" tedarikçiye tümüyle esir düşmektir: bir kilitlenmeyi bir başkasıyla takas ettiniz. En kritik platformlarınızı getirin ve her birinin tek bir sağlayıcının tescilli hizmetlerine ne kadar sıkı bağlı olduğunu sorun. Cevap "çok" ise, açık standartlar ve konteynerleştirilmiş, yeniden kurulabilir ortamlar kavrayışı gevşetmenin en ucuz yoludur.

3. **Egemenlik risk çerçevemizin sahibi kim ve yasa ve jeopolitik değiştikçe duruşu ne sıklıkla yeniden gözden geçiriyoruz?** Bir kez belirlenip hiç gözden geçirilmeyen bir egemenlik duruşu, bir karar, yaptırım ya da yeni bir yasa geldiği anda kurgu olur ve bu şoklar artık düzenli olarak gelir. Diğer yönetişiminizin yanında canlı bir çerçeve kurun: başlıca platformların yoğunlaşma ve yargı yetkisi riskini değerlendirin, her veri katmanı için hedef egemenlik düzeylerini belirleyin ve bir düzenleyiciye gösterebileceğiniz savunulabilir bir duruşu belgeleyin. Sahibi ve gözden geçirme sıklığını adlandırın. Ana sağlayıcınıza karşı bir yaptırımın ya da olumsuz bir kararın kritik hizmetlerinizi gelecek hafta nasıl etkileyeceği sorusunu getirin; kimse yanıtlayamıyorsa çerçeve henüz yok demektir.

4. **En duyarlı verimizin şifreleme anahtarlarını kim tutuyor ve sağlayıcımız o veriyi okunabilir biçimde teslim etmeye zorlanabilir mi?** Operatör anahtarları elinde tutuyorsa, ikamet ve hatta bir "egemen" bölge çok az şey ifade eder; çünkü bir ifşa emri, baytlar nerede olursa olsun şifresi çözülmüş veriye ulaşır. Anahtarları kendiniz denetlemek, kendi anahtarını getir ya da sağlayıcının hiç görmediği daha güçlü kendi anahtarını tut yoluyla, çoğu zaman paylaşılan altyapıda egemenliğin pratik yararının büyük kısmını her şeyi taşımanın maliyetinin çok küçük bir bölümüyle sağlar. Karşıt husus operasyoneldir: anahtar yönetimi affetmezdir ve kaybedilen ya da kötü yönetilen bir anahtar sizi herhangi bir yaptırım kadar kesin biçimde kendi verinizin dışında bırakabilir. Hangi veri kümelerinin şifrelendiğinin, her anahtarı gerçekte kimin tuttuğunun ve bir anahtar kaybolursa kurtarma yolunuzun ne olduğunun bir envanterini getirin, sonra bunu egemenlik katmanlarınızla eşleştirin. Kurumsal yapılar ve kamu için anahtar saklamayı, yabancı bir ifşa emrinin şifreli metin mi yoksa açık metin mi döndüreceğini belirleyen sınır olarak ele alın ve bunu sonradan eklenen bir düzeltme değil, bir satın alma gereksinimi yapın.

5. **Birincil sağlayıcımızdan önemli bir zaman çerçevesinde gerçekten ayrılabilir miyiz ve bunu en son ne zaman prova ettik?** İnandırıcı bir çıkış egemenliğin en gerçek ölçüsüdür, ama çoğu çıkış planı kâğıt üzerinde yaşar ve hiç çalıştırılmamıştır; bu yüzden taşınabilirlik gösterilmiş bir olgu değil bir umut olarak kalır. Gerilim maliyet ve odaktır: bir çıkışı prova etmek, iş yüklerini konteynerleştirilmiş tutmak ve veri ile yapılandırmanın emanetini sürdürmek, teslimat baskısının başka yerde harcamak isteyeceği mühendislik dikkatini tüketir. En kritik sisteminizi, zorunlu bir geçişin ne kadar süreceğine dair dürüst bir tahmini, bağımlı olduğu tescilli hizmetlerin listesini ve (varsa) en son gerçek provanın tarihini getirin. Sözleşmede çok yıllı çıkış yükümlülükleri taşıyan büyük ya da kamusal bir kuruluş için prova edilmemiş bir çıkış, yasal olarak yerine getiremeyeceğiniz bir taahhüt olabilir; bu yüzden prova sıklığını sistemin işletme maliyetinin bir parçası olarak ele alın, isteğe bağlı bir alıştırma olarak değil.

6. **Her taç mücevheri sistemi için, veri fiziksel olarak nerede durursa dursun hangi hükümetlerin ona bugün yasal olarak erişimi zorunlu kılabileceğini biliyor muyuz?** Konum, yargı yetkisi değildir: ülke içindeki bir veri merkezindeki veriye, merkezi yabancı bir ülkede olan bir operatörün kendi ülkesinin yasası uyarınca yine de erişilebilir ve takımlar düzenli olarak ikameti hukuki koruma sanır. Zor olan, yanıtın yalnızca bir mimari diyagramı değil, hukuk ve satın alma girdisi gerektirmesidir ve yeterlilik kararları, hükümler ve aktarım mekanizmaları değiştikçe harita kayar. Her kritik veri kümesi için sağlayıcının merkezini, ona ulaşan yasaları ve dayandığınız aktarım mekanizmasını getirin ve gerçekten kimsenin bilmediği yerde dürüst olun. Düzenlemeye tabi ve kamusal ortamlarda, vatandaş ya da ulusal güvenlik verisi üzerinde haritalanmamış bir hukuki maruziyet bir sonraki denetimde bekleyen bir bulgudur; bu yüzden hukuki haritalamayı altyapıyı fonladığınız kadar açık biçimde fonlayın.

## Sektör merceği

**Girişim.** Hız ve nakit ömrü baskındır; bu yüzden kadrolayamayacağınız egemen bir yığın kurmak yerine egemenliği ince bir özellik olarak satın alın. Bir müşterinin yargı yetkisi kısıt ise, mevcut sağlayıcınızın bölge içi seçeneğine dağıtın, operatörün duyarlı kayıtların şifresini çözememesi için kendi şifreleme anahtarlarınızı tutun ve iş yükünü taşınabilir kalması için konteynerleştirilmiş tutun. Bu, anlaşmayı tohum aşaması maliyetiyle kapatır ve nakit ömrünüzün olmadığı bir yeniden mimariden kaçınır.

**Küçük işletme.** Egemenlik uzmanınız yok ve bütçeniz kısıtlı; bu yüzden bunu bir mühendislik programı değil, bir sözleşme gözden geçirme ve tedarikçi seçimi sorusu olarak ele alın. Yargı yetkisi içinde bölgeler, şeffaf veri işleme koşulları ve müşteri tarafından tutulan anahtarları standart özellik olarak sunan tedarikçileri tercih edin ve imzalamadan önce alt işleyici ve ifşa maddelerini okuyun. Egemenlik için kendi barındırma burada nadiren karşılığını verir: taşıyacak insanlarınız olmadan operasyon ve güvenlik yükünü devralırsınız.

**Kurumsal.** İş, birçok takım genelinde portföy yönetişimidir: veri için egemenlik duyarlılığına göre paylaşılan bir katmanlama, kritik yükün ne kadarının tek bir sağlayıcıda ya da tek bir yargı yetkisinde durduğuna dair bir yoğunlaşma riski görünümü ve standartlaştırılmış anahtar denetimi, taşınabilirlik ve çıkış provaları; böylece her grup kendi koordine edilmemiş bahsini yapmayı bırakır. Duyarlı katmanın daha yüksek maliyetini ve operasyonel yükünü açıkça bütçeleyin ve bir düzenleyiciye gösterebileceğiniz belgelenmiş, denetlenebilir bir duruşu koruyun. Egemenliği tek seferlik bir geçiş olarak değil, metrikleri ve gözden geçirme sıklığı olan canlı bir risk olarak yönetin.

**Kamu.** Satın alma kuralları, şeffaflık ve kamusal hesap verebilirlik her seçimi şekillendirir. Sertifikalı egemen altyapıyı (örneğin SecNumCloud tarzı niteleme), açık standartları ve açık kaynağı tercih edin; böylece platform herhangi bir tedarikçiden bağımsız sürdürülebilir ve sözleşmenin kendisinde taşınabilirlik ile hukuki maruziyetin ifşasını zorunlu kılın. Vatandaş verisinin nerede durduğuna ve ona kimlerin ulaşabildiğine dair sade dilde bir açıklama yayımlayın, pahalı egemen denetimleri gerçekten duyarlı katman için ayırın ve daha az duyarlı kamu hizmetlerini daha ucuz küresel altyapıda tutun.

## Örnekler

**Girişim.** Küçük bir sağlık teknolojisi girişimi Almanya'daki ilk hastane müşterisini kazanır; müşteri hasta verisinin AB yargı yetkisi altında kalmasını şart koşar. Karşılayamayacağı egemen bir yığını aşırı inşa etmek yerine kurucular, mevcut bulut sağlayıcılarının AB bölgesine dağıtır, sağlayıcı duyarlı kayıtların şifresini çözemesin diye kendi şifreleme anahtarlarını tutar ve iş yükünü taşınabilir kalması için konteynerleştirilmiş tutar. Bu, müşterinin ihtiyaç duyduğu egemenlik yararının çoğunu bir tohum aşaması takımının taşıyabileceği bir maliyetle sağlar ve anlaşmayı topyekûn bir yeniden mimari olmadan kapatır.

**Kurumsal.** Çok uluslu bir banka, belirli müşteri verilerini AB içinde ve yabancı ifşa yasasının erişimi dışında tutmak zorundadır. Küresel bulut sağlayıcısını terk etmek yerine yapısını katmanlandırır. Genel iş yükleri ölçek için hiper ölçekli bölgelerde kalır. Düzenlemeye tabi müşteri verisi, **kendi anahtarını tut** şifrelemesiyle (sağlayıcı şifresini çözemez) ve alternatif bir sağlayıcıya sınanmış bir çıkış planıyla AB bölgelerinde çalışır. Bu, düzenleyicileri ve bankanın kendi yoğunlaşma riski iştahını (bölüm 10.2) topyekûn, yeteneği yok eden bir geçiş olmadan tatmin eder.

**Kamu.** Bir ulusal sağlık hizmeti vatandaşların tıbbi kayıtlarını tutar ve yabancı yargı yetkisine maruziyeti kabul edilemez bulur. Egemen bir bulut satın alır; yani ulusal sertifikasyon altında ülke içindeki bir kuruluşun işlettiği altyapıyı (örneğin SecNumCloud tarzı), en duyarlı işleme için gizli hesaplamayla birlikte ve platformun herhangi bir tedarikçiden bağımsız sürdürülebilmesi için açık standartları (bölüm 3.8) ve açık kaynak bileşenleri zorunlu kılar. Daha yüksek maliyet ve daha dar özellik kümesi, ulusal güvenlik denetiminin ve kamu güveninin bedeli olarak kabul edilir. Bu arada daha az duyarlı hizmetler (kamuya açık bilgi portalı) daha ucuz küresel altyapıda kalır.

## İş gerekçesi: motivasyonlar, YG ve TSM

Dijital egemenliğin ekonomisi asimetriktir ve en iyi düşük olasılıklı, yüksek etkili olaylara karşı sigorta olarak çerçevelenir. Maliyetler görünür ve süreklidir: egemen ve yargı yetkisi içindeki altyapı tipik olarak daha pahalıdır, daha az yönetilen hizmet sunar ve daha fazla kurum içi operasyonel yetenek talep eder; bunların hepsi toplam sahip olma maliyetini yükseltir ve teslimatı yavaşlatabilir. Faydalar çoğunlukla önlenen felaketlerdir: *Schrems II* gibi bir kararın ardından düzenleyici cezalar ve zorunlu yeniden mimari, bir sağlayıcıya yaptırım uygulanırsa ya da bağlantısı kesilirse işi bitiren bir erişim kaybı ya da duyarlı verinin yabancı ifşasının itibar ve ulusal güvenlik zararı. Bu kuyruk riskleri ağır ve giderek daha olası olduğu için, egemenliğe yapılan orantılı yatırım, özellikle anahtar sahipliği, taşınabilirlik ve açık standartlar gibi ucuz ama güçlü denetimler, durağan durumdaki bir hesap tablosunda saf maliyet gibi görünse bile çoğu zaman güçlü biçimde pozitif beklenen değerdir.

Her iki yandaki tuzak orantısızlıktır. *Eksik* yatırım, kritik veri ve sistemleri çıkışı olmayan tek bir yargı yetkisine ya da tedarikçiye açık bırakır ve yönetilebilir bir riski varoluşsal bir riske çevirir. *Aşırı* yatırım, her şeyi yerelleştirerek ve tüm küresel platformları reddederek parayı yakar, yeteneği kaybettirir ve seçeneklerinizi daralttığı için dayanıklılığı *azaltabilir*. Davayı liderliğe anlatmak için egemenlik harcamasını bir veri ve iş yükü risk katmanlamasına bağlayın. Taç mücevheri sistemlerinin yoğunlaşma ve yargı yetkisi maruziyetini nicelleyin. Onları risksizleştiren ucuz denetimleri (anahtarlar, taşınabilirlik, çıkış provaları) fiyatlayın. Pahalı egemen altyapıyı gerçekten hak eden katman için ayırın.

## Anti-kalıplar ve tuzaklar

- **Egemenlik tiyatrosu:** merkezi yabancı bir ülkede olan bir sağlayıcı veriye yasal erişimini korurken ülke içi veri ikametini ilan etmek.
- **Şifrelemeyi egemenlikle karıştırmak:** veriyi şifrelemek ama anahtarları sağlayıcının tutmasına izin vermek; böylece sağlayıcı yine de şifreyi çözmeye zorlanabilir.
- **Aşırıya kaçmak:** duyarlılığa bakmaksızın her şeyi yıkıcı bir maliyetle ve azalan yetenekle yerelleştirmek ve kendi barındırmak.
- **Yeni tekil kilitlenme:** çıkışı olmayan tek bir "egemen" tedarikçiye tümüyle esir düşerek bir hiper ölçekleyiciden kaçmak.
- **Sınanmamış çıkış:** kâğıt üzerinde var olan ama hiç prova edilmemiş bir çıkış planı; böylece taşınabilirlik kanıtlanmamıştır.
- **İnsan tedarik zincirini yok saymak:** açık kaynağın ya da kendi barındırmanın, onu çalıştıracak yetenekli insanlar olmadan egemenlik sağladığını varsaymak.
- **Durağan duruş:** bir egemenlik duruşunu bir kez belirleyip yasa ve jeopolitik değiştikçe hiç yeniden gözden geçirmemek.

## Olgunluk modeli

- **Düzey 1, Başlangıç:** Egemenlik düşünülmemiş ve tepkiseldir; veri ve kritik sistemler en ucuz yerde durur, yargı yetkisi ya da yoğunlaşma riskinin bir haritası ve bir sahibi yoktur.
- **Düzey 2, Geliştirme:** Veri ikameti bazı projelerde en bariz düzenlemeye tabi veri için ele alınır, ancak yargı yetkisi, anahtar denetimi ve çıkış sistematik olarak göz önüne alınmaz; uygulamalar takımdan takıma değişir ve tek sağlayıcılara güven sorgulanmaz.
- **Düzey 3, Standartlaştırma:** Veri ve iş yükleri, kuruluş genelinde uygulanan belgelenmiş bir politikayla egemenlik duyarlılığına göre katmanlandırılır; yargı yetkisi haritalandırılır; duyarlı katmanlarda anahtar denetimi, taşınabilirlik ve açık standartlar zorunludur; çıkış planları vardır ve isteğe bağlı değil zorunlu kılınmıştır.
- **Düzey 4, Yönetme:** Duruş temel çizgilere karşı ölçülür ve kontrol edilir: yoğunlaşma riski (kritik iş yüklerinin tek bir sağlayıcıda ya da yargı yetkisinde olan payı), duyarlı veri kümeleri genelinde anahtar sahipliği kapsamı, yargı yetkisi haritalama bütünlüğü ve prova edilmiş çıkış süreleri metrik olarak izlenir, yönetişime raporlanır ve eşiklere karşı uygulanır; böylece sürüklenen bir bağımlılık bir şoktan sonra değil, kanıta dayalı olarak eylemi tetikler.
- **Düzey 5, Orkestrasyon:** Egemenlik sürekli iyileştirilir ve kuruluş genelinde bütünleştirilmiştir: canlı risk çerçevesi varsayılan olarak mimariyi, satın almayı ve risk planlamasını besler, çıkışlar rutin olarak prova edilir ve kuruluş kararlar, yaptırımlar ve düzenleme değiştikçe katmanları uyarlanır biçimde yeniden kapsamlandırır, sağlayıcıları yeniden dengeler ve duruşunu gözden geçirir.

## Tartışma fikirleri

1. En duyarlı veri kümeniz için hangi hükümetler ona bugün yasal olarak erişimi zorunlu kılabilir ve bunu biliyor musunuz?
2. Veri ikametiniz gerçek egemenlik mi, yoksa merkezi yabancı bir ülkede olan bir sağlayıcı hâlâ anahtarları ve hukuki maruziyeti elinde mi tutuyor?
3. Gerekirse birincil bulut sağlayıcınızdan gerçekten ayrılabilir misiniz ve bunu hiç denediniz mi?
4. İş yüklerinizden hangileri gerçekten egemen altyapıya ihtiyaç duyuyor ve hangilerini gereksiz maliyetle aşırı koruyorsunuz?
5. Kendi şifreleme anahtarlarınızı denetlemek, egemenlik yararının çoğunu maliyetin çok küçük bir bölümüyle nerede sağlar?
6. Ana sağlayıcınıza karşı bir yaptırım, kesinti ya da hukuki karar kritik hizmetlerinizi gelecek hafta nasıl etkilerdi?

## Önemli çıkarımlar

- Dijital egemenlik, veri, operasyonel, yazılım ve tedarik zinciri boyutlarında verinizin, yazılımınızın ve altyapınızın orantılı denetimidir.
- **Konum, yargı yetkisi değildir:** yalnızca ikamet yabancı hukuki erişimi engellemez; ifşayı kimin zorunlu kılabileceğini haritalandırın.
- **Çıkış için tasarlayın** ve **anahtarlarınızı denetleyin:** taşınabilirlik ve anahtar sahipliği, en yüksek kaldıraçlı ve en düşük maliyetli denetimlerdir.
- **Açık standartlar ve açık kaynak** stratejik özerklik araçlarıdır; pahalı **egemen bulutu** onu hak eden katman için ayırın.
- Egemenliği **orantılı, canlı bir risk** olarak yönetin (bölüm 10.2, 10.3, 4.5, 4.6, 3.8); hem eksik korumadan hem de yıkıcı aşırıya kaçmaktan kaçının.
- YG, gerçek ve süregelen maliyete karşı fiyatlanan ağır kuyruk risklerine (düzenleyici, jeopolitik ve kilitlenme) karşı sigortadır.

## Kaynaklar ve ileri okuma

- European Court of Justice, *Data Protection Commissioner v. Facebook Ireland and Maximillian Schrems* ("Schrems II", 2020).
- Regulation (EU) 2016/679, *General Data Protection Regulation (GDPR)*; Regulation (EU) 2023/2854, *Data Act*.
- U.S. *Clarifying Lawful Overseas Use of Data (CLOUD) Act* (2018).
- ANSSI, *SecNumCloud* qualification framework (France).
- Gaia-X European Association for Data and Cloud (Gaia-X initiative).
- ENISA, reports on cloud security and EU cybersecurity certification (EUCS).
- Julia Pohle and Thorsten Thiel, "Digital Sovereignty" (*Internet Policy Review*, 2020).
- Bert Hubert, writings on European digital autonomy and dependency on foreign providers.
- Kai Zenner and others, analyses of EU digital sovereignty policy (for context; verify current sources).
