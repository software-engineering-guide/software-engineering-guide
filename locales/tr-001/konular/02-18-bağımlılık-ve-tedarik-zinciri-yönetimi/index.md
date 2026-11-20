# 2.18 Bağımlılık ve tedarik zinciri yönetimi

## Genel bakış ve motivasyon

Projenizin kilit dosyasını açın ve paketleri sayın. Çoğu takım gibiyseniz, yazdığınız kod, sizin yazmadığınız, tam anlamadığınız ve kolayca denetleyemediğiniz yüzlerce ya da binlerce [bağımlılığın](https://en.wikipedia.org/wiki/Coupling_(computer_programming)) üzerindeki ince bir katmandır. Modern bir web hizmeti bir çerçeve, bir veritabanı sürücüsü, bir günlük kütüphanesi ve bir serileştirme biçimi çeker ve bunların her biri daha fazlasını çeker. Sonuç, çalışan yazılımınızın çoğunun, çoğu zaman büyük çoğunluğunun, internetteki yabancılardan gelmesidir. Bu bir başarısızlık değildir. Küçük bir takımın bir zamanlar yıllar süren şeyi haftalarda yayımlamasını sağlayan anlaşmadır. Mesele anlaşmayı gözleriniz açık yapmaktır.

O ödünç kodu iyi yönetmek başlı başına bir mühendislik disiplinidir ve bu bölüm onun zanaatıyla ilgilidir: bağımlılıkları nasıl seçersiniz, sabitlersiniz, güncellersiniz, derlemelerinizi nasıl yeniden üretirsiniz ve tüm çizgeyi büyürken nasıl okunabilir tutarsınız. Bir saldırganın o çizgeyi kasıtlı zehirlediği güvenlik tehdidi tarafı, uygulama güvenliği üzerine bölüm 4.2'de tam ele alınır. Burada kaygı gündelik mühendisliktir: sürüm kısıtları, kilit dosyaları, geçişli çatışmalar, güncelleme temposu ve yazılımınızda neyin olduğunu bilmek. Bunu doğru yapın ve güvenlik çok daha kolay hale gelir, çünkü göremediğiniz bir tedarik zincirini savunamazsınız.

Büyük takımlar ve özellikle kurumsal ve kamu için bahisler ölçekle yükselir. Beş yüz depo her biri kendi kütüphanelerini seçtiğinde, aynı günlük çerçevesinin beş yüz biraz farklı sürümünü, kimsenin onaylamadığı bir lisansı ve ciddi bir güvenlik açığı ortaya çıktığında "etkilendik mi?" sorusuna cevap verecek bir yol olmadan kalırsınız. Kurumlar buna onaylı kütüphaneler ve paylaşılan kayıt defterleriyle cevap verir. Hükümetler giderek zorunluluklarla cevap verir: Amerika Birleşik Devletleri 14028 sayılı Başkanlık Kararnamesi, satın aldıkları yazılım için bir [yazılım malzeme listesini](https://en.wikipedia.org/wiki/Software_supply_chain) (SBOM) ve derleme kaynağını temel şart haline getirdi. Bir sonraki bağımlılık krizinde sakin kalan kuruluşlar, bu işi ihtiyaç duymadan önce yapanlardır.

## Temel ilkeler

- Yazılımınızın çoğu sizin yazmadığınız koddur; yazmamış olsanız da sorumluluğu üstlenin.
- Her bağımlılık bir varlık kadar kalıcı bir yükümlülüktür; onları refleksle değil bilinçli ekleyin.
- Derlemelerin "o gün en yeni olan her neyse" değil, yeniden üretilebilir ve belirlenimci olması için sürümleri kilit dosyalarıyla sabitleyin.
- Nadir korkutucu sıçramalarla değil, kararlı bir tempoda, küçük otomatik artışlarla güncelleyin.
- Yazılımınızda tam olarak ne olduğunu bilin; sayamadığınızı güvenceye alamaz ya da lisanslayamazsınız.
- Çok sayıda kullanışlı bağımlılık yerine daha az, iyi sürdürülen bağımlılığı tercih edin.
- Paketlerin nereden geldiğini kontrol edin; doğrulanmamış bir kayıt defteri açık bir kapıdır.

## Öneriler

### Sürümlemeyi anlayın ve bilinçli kısıtlayın

Ekosisteminizin sürümleri nasıl ifade ettiğini öğrenin, çünkü güncelleme davranışınız tamamen ona biner. Çoğu paket yöneticisi bir tür [anlamsal sürümleme](https://en.wikipedia.org/wiki/Software_versioning) (SemVer) kullanır; burada bir sürüm MAJOR.MINOR.PATCH olarak okunur: bir yama artışı yalnızca hata düzeltmeleri vaat eder, bir küçük artış geriye dönük uyumlu özellikler ekler ve bir büyük artış bozucu değişiklikleri işaret eder. Bağımlılık bildirimleriniz sonra "4.x ile uyumlu" ya da "en az 2.3.0" gibi bir kısıt belirler; bu, çözücüye sürüm seçerken ne kadar dolaşabileceğini söyler.

O kısıtların ne kadar gevşek ya da sıkı olduğu konusunda bilinçli olun. Gevşek aralıklar düzeltmeleri otomatik alır, bedeli hiç gözden geçirmediğiniz bir küçük sürümün üretime kaymasına izin vermektir; sıkı sabitlemeler kontrol verir, bedeli elle çabadır. Çoğu takım için pragmatik cevap, bildiriminizde makul ölçüde izin veren aralıklar bildirmek, sonra tam çözümlenmiş sürümleri bir kilit dosyasında dondurmaktır; böylece aralık yalnızca bilerek güncellediğinizde yeniden değerlendirilir. SemVer'i bakımcıların tutmaya çalıştığı bir söz olarak, her zaman tutmadıkları bir garanti olarak değil ele alın; bir "yama" sürümü yine de sizi bozabilir ve güncellemelere güvenmek yerine test etmenizin nedeni tam olarak budur.

### Kilit dosyalarını commit'leyin ve yeniden üretilebilir derlemeler talep edin

Bir kilit dosyası bağımlılık çizgenizdeki, doğrudan ve geçişli her paketin tam sürümünü ve şifreleme özetini kaydeder. Onu sürüm kontrolüne (bölüm 2.6) commit'leyin ve kaynağınızın birinci sınıf bir parçası olarak ele alın. İşi, derlemenizi bir fonksiyon yapmaktır: aynı girdiler her makinede, bu yıl ve gelecek yıl her seferinde aynı çıktıyı üretir. Onsuz, bir hafta arayla "install" çalıştıran iki mühendis farklı kod alabilir ve üretimde ortaya çıkan bir hatayı onu derleyen dizüstü bilgisayarda yeniden üretmek imkansız olabilir.

Verilen bir commit'in her zaman davranışça aynı yapıtı ürettiği gerçekten [yeniden üretilebilir derlemeleri](https://en.wikipedia.org/wiki/Reproducible_builds) hedefleyin. Sürekli entegrasyonda (bölüm 8.1) sessizce yeni sürümler çözümlemek yerine yalnızca kilit dosyasından kurun ve kilit dosyası ile bildirim uyuşmadığında derlemeyi başarısız kılın. Kilit dosyasındaki özetler çifte iş görür: davranışı sabitlerler ve kurcalamayı algılarlar, çünkü içeriği artık kayıtlı özetiyle eşleşmeyen bir paket kurulmaz. Yeniden üretilebilirlik, bu bölümdeki her şeyin üzerinde durduğu temeldir.

### Geçişli bağımlılıkları ve elmas çatışmalarını bilinçli yönetin

Doğrudan bağımlılıklarınız yalnızca adını verdiklerinizdir. Onların altında, paketlerinizin bağımlı olduğu paketlerin çok daha büyük bir geçişli bağımlılık çizgesi yatar ve riskinizin ve sürprizlerinizin çoğunun yaşadığı yer orasıdır. Klasik bir başarısızlık elmas bağımlılıktır: A kütüphanesi paylaşılan bir yardımcının 1. sürümüne ihtiyaç duyar, B kütüphanesi 2. sürümüne ve şimdi çözücü imkansız bir isteği uzlaştırmalıdır. Bazı ekosistemler birden fazla sürümün bir arada var olmasına izin verir, huzur için disk ve belleği takas eder; diğerleri tek bir sürümü zorlar ve çatışmayı arabuluculuk yapmanızı size bırakır.

Bu çatışmaları çürümeye bırakmak yerine görünür kılın. Tam bağımlılık ağacını yazdırmak ve belirli bir paketin neden var olduğunu ve onu kimin çektiğini açıklamak için araçlarınızı kullanın. Bir çatışma ortaya çıktığında bilinçli çözün: geride kalanı yükseltin, bir geçersiz kılma sabitleyin ya da taleplerini karşılayamadığınız bir bağımlılığı bırakın. Çizgenin zaman içindeki büyümesini izleyin, çünkü geçişli bağımlılıklardaki denetimsiz yayılma, sonunda çözülemez bir yükseltme ya da yeniden yazma olmadan yamalayamayacağınız bir güvenlik açığı olarak ortaya çıkan [teknik borcun](https://en.wikipedia.org/wiki/Technical_debt) yavaş birikimidir.

### Otomatik çekme istekleriyle kararlı bir tempoda güncelleyin

En riskli güncelleme stratejisi çoğu takımın kazara sürüklendiği olandır: hiç güncellememek, sonra kritik bir güvenlik açığı elinizi zorladığında acil durum baskısı altında her şeyi birden güncellemek. O zamana kadar yıllarca gerisindesinizdir, değişiklik günlükleri bir duvardır ve yükseltme rutin bir angarya yerine haftalar süren bir projedir. Çözüm temporadır. Bir bağımlılığın yeni bir sürümü olduğunda, değişiklik günlüğü ve test sonuçlarınız ekli bir çekme isteği açan otomatik bir bağımlılık güncelleyicisi (Dependabot ve Renovate araçları yaygın örneklerdir) benimseyin.

Sonra akışı sizi boğmak yerine yardım edecek biçimde ayarlayın. Her sabah tek tek çekme isteği yağmuru insanları hepsini görmezden gelmeye alıştırır; bu hiç otomasyon olmamasından kötüdür. Yama sürümleri gibi düşük riskli güncellemeleri toplu işleyin, testler geçtiğinde otomatik birleşmelerine izin verin ve insan dikkatini büyük sürüm artışlarına ve hassas bir kütüphaneye dokunan her şeye saklayın. Takımın sürdürebileceği bir ritim belirleyin, belki haftalık bir inceleme; böylece güncelleme nadir acı veren bir fatura değil, küçük kararlı bir vergi olarak kalsın. Güçlü bir test stratejisinin (bölüm 2.4) karşılığını verdiği tam olarak burasıdır, çünkü otomatik güncellemeler yalnızca testleriniz neyi bozduklarını yakalayabiliyorsa güvenlidir.

### Ayak izinizi en aza indirin ve benimsemeden önce değerlendirin

Eklediğiniz her bağımlılık kalıcı bir taahhüttür: hatalarına, güvenlik açıklarına, lisansına, bakımcısının süregelen ilgisine ve kendi büyüyen alt bağımlılık çizgesine. Yönetmesi en ucuz bağımlılık, eklemediğinizdir. Bir pakete uzanmadan önce, özellikle önemsiz işlevsellik için, kendi birkaç düzine satır kodunuzun yeterli olup olmayacağını sorun. Paket ekosistemlerinin tarihi, küçük, geniş biçimde bağımlı olunan bir paketin kaldırıldığı ya da ele geçirildiği ve internetin yarısını bozduğu uyarıcı hikâyelerle doludur.

Benimsediğinizde, adayı olduğu uzun vadeli ilişki gibi değerlendirin. Bakım sağlığını kontrol edin: yakın tarihli commit'ler, duyarlı bakımcılar, gerçek bir sürüm geçmişi ve anahtarlara sahip birden fazla kişi. Lisansı kontrol edin ve onaylı listenizde olduğunu doğrulayın (bölüm 10.3). Güvenlik sicilini, boyutunu ve kendi geçişli ayak izini kontrol edin, çünkü küçük bir özellik yüz paket sürüklemeye değmez. Bu ölçütleri yazın; böylece "bunu eklemeli miyiz?" tüm takımın tutarlı uyguladığı bir kontrol listesi olsun, bir ruh hali değil.

### Bir SBOM üretin ve derleme kaynağını yakalayın

Yazılımınızda ne olduğunu zaten bilmiyorsanız "bu güvenlik açığından etkilendik mi?" sorusuna hızla cevap veremezsiniz. SBOM cevaptır: SPDX ya da CycloneDX gibi standart bir biçimde, bir derlemedeki her bileşenin sürümleri ve lisanslarıyla makine tarafından okunabilir bir envanteri. Onu derleme hattınızın parçası olarak otomatik üretin, yapıtın yanında saklayın ve o yapıt herhangi bir yerde çalıştığı sürece tutun. Bir sonraki manşet güvenlik açığı düştüğünde SBOM'larınıza karşı bir sorgu, bir haftalık çılgın grep'i beş dakikalık bir rapora çevirir.

Bir adım daha ileri gidin ve kaynağı yakalayın: bir yapıtın nasıl, hangi kaynak commit'ten, hangi hat tarafından derlendiğinin imzalı, kurcalamaya karşı kanıtlı kaydı. [Açık kaynaklı yazılım](https://en.wikipedia.org/wiki/Open-source_software) topluluğu tam olarak bunun için dereceli bir model olarak SLSA çerçevesinde (Yazılım Yapıtları için Tedarik Zinciri Düzeyleri) buluştu; "derlememizi tarif edebiliriz"den "kanıtlayabiliriz ve kanıt ele geçirilmiş bir derleme sistemine direnir"e doğru ilerler. Doğrulama, bir tüketicinin bir yapıtın gerçekten hattınızdan geldiğini doğrulamasını sağlar. Kamu işi için bu giderek isteğe bağlı değildir; kaynak ve SBOM tedarik zorunluluklarının içinde yer alır; bu yüzden yeteneği erken kurmak ihaleye girmeye uygun kalmanızı sağlar.

### Kaynaklarınızı kayıt defterleri, aynalar ve vendor'lama ile kontrol edin

Paketlerinizin nereden geldiği, hangi paketleri seçtiğiniz kadar önemlidir. Her derlemede doğrudan kamusal internetten çekin ve onun kesintilerini, çekilmiş sürümlerini ve saldırganlarını miras alırsınız. Kamusal ekosistemi vekil eden dahili bir paket kayıt defteri ya da önbellekleme aynası kurun; böylece derlemeler hızlı, tekrarlanabilir ve akış yukarısının kaybolmasından yalıtılmış olur. Kayıt defteri ayrıca politikayı uygulamak için doğal yer olur: bilinen kötü sürümleri engelleyin, yeni sürümleri kısa bir bekleme için karantinaya alın ve lisans ya da güvenlik kapılarınızı geçemeyen paketleri reddedin.

İki belirli tuzaktan kaçınmak için o kayıt defterini dikkatle yapılandırın. Bağımlılık karışıklığı, bir derleme aracına hem özel bir dahili paket hem aynı adlı bir kamusal paket sunulduğunda saldırganın kamusal olanı çekmesidir; dahili adları kapsamlayarak ve dahili paketleri açıkça dahili kaynağa sabitleyerek karşı koyarsınız. [Yazım hatası kapmacılığı](https://en.wikipedia.org/wiki/Typosquatting), kötü niyetli bir paketin popüler bir paketten bir tuş uzakta bir ad kullanması ve şişman bir parmağı beklemesidir; bir izin listesi olan derlenmiş bir kayıt defteri onu kapıda engeller. Küçük bir kritik ya da yavaş hareket eden bağımlılık kümesi için vendor'lamayı, gerçek bağımlılık kaynağını kendi deponuza commit'lemeyi düşünün; böylece derlemenizin hiç dış bağımlılığı olmaz. Güncelleme rahatlığını tam kontrolle takas eder, bu bazen tam olarak doğrudur.

## Ödünleşimler: artılar ve eksiler

| Yaklaşım | Artılar | Eksiler |
| --- | --- | --- |
| Gevşek sürüm aralıkları | Otomatik düzeltmeler; düşük elle çaba | İncelenmemiş kod üretime ulaşır; kilit dosyası olmadan belirlenimsiz |
| Sıkı sabitleme artı kilit dosyası | Yeniden üretilebilir, denetlenebilir derlemeler | Bilinçli güncelleme işi gerektirir; düzeltmelerde geride kalabilir |
| Agresif güncelleme temposu | Küçük, güvenli adımlar; her zaman günceye yakın | Sürekli çalkantı; kararlı inceleyici dikkati gerekir |
| Nadir, toplu büyük yükseltmeler | Gün gün daha az kesinti | Zorlandığında korkutucu, riskli, pahalı |
| Çok sayıda kullanışlı bağımlılık | Özellik inşası hızlı | Geniş saldırı yüzeyi; ağır bakım yükü |
| Asgari ayak izi artı vendor'lama | Kontrol, küçük yüzey, akış yukarısı riski yok | Sahip olunan daha fazla kod; güncellemeleri kendiniz taşırsınız |
| Doğrudan kamusal kayıt defteri | Sıfır kurulum | Kesintiler, çekilmeler, karışıklık ve yazım hatası kapmacılığı maruziyeti |
| Dahili kayıt defteri ve ayna | Hız, politika uygulaması, yalıtım | Çalıştırılacak ve sürdürülecek altyapı |

Merkezi gerilim hız ile kontrol arasındadır. Yukarıdaki her seçim, farklı bir açıdan görülen aynı kadrandır: ödünç kodunuzun ne kadarını etkin yöneteceksiniz ve ne kadarının güvenle içeri akmasına izin vereceksiniz? Kontrole fazla yaslanın ve elle incelemede boğulur, güvenlik düzeltmelerinde geride kalır ve bağımlılıkların hızlandırması gereken takımı yavaşlatırsınız. Hıza fazla yaslanın ve bir gün denetlenemeyen, yükseltilemeyen bir çizge ve avukata açıklayamadığınız bir lisans ihlaliyle uyanırsınız. Çözüm bir duruştur, sabit bir nokta değil: her şeyi kilitleyin ve yeniden üretin, küçük adımlarla sürekli güncelleyin, üstlendiğinizi en aza indirin ve politikayı kontrol ettiğiniz bir darboğazda uygulayın. Bu birleşim size hem hız hem güvenlik satın alır; ölçekte yapmaya değer takas budur.

## Takımınızla tartışılacak sorular

1. **Gerçek güncelleme temponuz nedir ve zorunlu bir acil yükseltme saatler mi yoksa haftalar mı sürerdi?** Çoğu takım kritik bir güvenlik açığı konuyu zorlayana kadar buna dürüstçe cevap veremez. Bölüm kararlı, otomatik, küçük adımlı güncellemeyi güvenli yol ve nadir büyük patlamalı yükseltmeyi tehlikeli yol olarak ele alır, çünkü açık bıraktığınız boşluk, sonra baskı altında koşmanız gereken boşluktur. Kanıtı getirin: bağımlılıklarınızın kaçı bir büyük sürümden fazla geride ve son önemli yükseltmenizin gerçekte ne kadar sürdüğü. Otomatik bir güncelleyici benimseyip benimseyemeyeceğinizi, insanların kapanmaması için düşük riskli değişiklikleri nasıl toplu işleyeceğinizi ve otomatik birleştirmenin güvenli olması için hangi teste ihtiyaç duyduğunuzu tartışın. Cevap mühendislik zamanını nasıl bütçelediğinizi değiştirmelidir; nadir bir krizi rutin haftalık bir vergiye çevirerek. Dürüst cevap "haftalar" ise, bu bir olay ortasında keşfedilecek değil, şimdi adlandırılacak bir risktir.

2. **Yaygın bir kütüphanede ciddi bir güvenlik açığı şu an duyurulsa, çalıştırdığınız her etkilenen yapıtı ne kadar hızlı listeleyebilirdiniz?** Bu, bir SBOM'un cevaplamak için var olduğu sorudur ve cevabınızın hızı tedarik zinciri olgunluğunuzun doğrudan ölçüsüdür. Envanter olmadan depoları grep'lemeye ve takımlarla görüşmeye indirgenirsiniz; bu, saat işlerken sahip olmayabileceğiniz günler alır. Somut sinyali getirin: derleme başına bir SBOM üretiyor musunuz, nerede saklanıyor ve bugün hepsi arasında gerçekten sorgulayabilir misiniz? Yalnızca doğrudan bağımlılıkları değil, geçişli çizgeyi de bilip bilmediğinizi tartışın, çünkü savunmasız paket genellikle hiç adını vermediğiniz paketlerden biridir. Cevap bir sonraki olayınızın bir sorgu mu yoksa bir yangın tatbikatı mı olacağını belirler ve ihtiyaç duymadan önce yeteneği kurmaya değer. Hükümetler bunu tam da bu nedenle şimdi zorunlu kılıyor.

3. **Yeni bir bağımlılığı benimsemeye değip değmeyeceğine nasıl karar veriyorsunuz ve herkes aynı çıtayı uyguluyor mu?** Bölüm her bağımlılığın bir rahatlık kadar kalıcı bir yükümlülük olduğunu ve yönetmesi en ucuz olanın hiç eklenmeyen olduğunu savunur. Yine de çoğu takımda karar görünmezdir: bir mühendis bir özelliğe ihtiyaç duyar, bir paket bulur ve bakımına, lisansına, güvenlik geçmişine ya da ayak izine dair hiçbir inceleme olmadan öğle yemeğine kadar kilit dosyasındadır. Çizgenizden kimsenin benimsediğini hatırlamadığı ve bugün savunamayacağı paket örnekleri getirin. Yazılı bir değerlendirme kontrol listesinin ve onaylı kütüphane listesinin (bölüm 10.3) yardımcı mı yoksa yalnızca sürtünme mi ekleyeceğini ve kendiniz yazmanız gereken önemsiz yardımcılarla bağımlı olmaya değer gerçek altyapı arasındaki çizginin nerede olduğunu tartışın. Cevap, takımınızın taşıdığı uzun vadeli ağırlığı, tek bir küçük karar ile biçimlendirir.

4. **Yalnızca adını verdiklerinizi mi yoksa geçişli bağımlılıklarınızı da gerçekten yönetiyor musunuz?** Riskinizin çoğu bir seviye aşağıda, paketlerinizin çektiği paketlerde yaşar ve iki kütüphanenin paylaşılan bir yardımcının uyumsuz sürümlerini talep ettiği bir elmas çatışması, bir yükseltmeyi mümkün olan en kötü anda engelleyebilir. Bu ölçekte önemlidir, çünkü tek bir yamalanamayan geçişli paket yüzlerce depo boyunca bir güvenlik düzeltmesini dondurabilir ve rakip çekim gerçektir: tam çizgeyi ortaya çıkarmak ve sabitlemek süregelen çabaya mal olurken, onu görmezden gelmek o çabayı çözülemez bir yükseltme olarak ortaya çıkan yavaş bir borç birikimiyle takas eder. Kanıtı getirin: araçlarınız tam ağacı yazdırıp belirli bir paketin neden var olduğunu ve onu kimin çektiğini açıklayabiliyor mu ve en yaygın kütüphanelerinizin kaç farklı sürümü bugün bir arada var? Kurumsal ve kamu için envanterinizin ve politikanızın geçişli bileşenlere ulaşıp ulaşmadığını ekleyin, çünkü çizgenin yarısı size görünmezse yazılımınızda ne olduğunu bilme zorunluluğu anlamsızdır. Cevap bir sonraki zorunlu yükseltmenizin rutin bir birleştirme mi yoksa çok takımlı bir kazı mı olacağını söyler.

5. **Paketleriniz gerçekte nereden geliyor ve bir saldırganın birini sokmasını ne engelliyor?** Doğrudan kamusal internetten çeken her derleme onun kesintilerini, çekilmiş sürümlerini ve iki belirli saldırıyı miras alır: bir derleme aracının özel paketinizi gölgeleyen bir kamusal paketi çektiği bağımlılık karışıklığı ve kötü niyetli bir paketin popüler bir adın bir tuş yanında durduğu yazım hatası kapmacılığı. Bu büyük bir takım için önemlidir, çünkü tek bir zehirli çekme kimse fark etmeden tüm varlığınız boyunca yayılabilir ve ödünleşim gerçektir: dahili bir kayıt defteri ya da önbellekleme aynası size bir politika darboğazı ve akış yukarısından yalıtım verir, ama birinin çalıştırması ve güncel tutması gereken altyapıdır. Somut sinyali getirin: dahili paket adları açıkça kapsamlanıp dahili kaynağa sabitleniyor mu, bir izin listesi var mı ve herhangi bir yeni sürüm kullanılmadan önce kısa bir karantina alıyor mu? Kamu ve düzenlemeye tabi alıcılar için bunu tedarikin giderek talep ettiği onaylı yazılım listesi ve doğrudan internet olmayan duruşa bağlayın ve mevcut kurulumunuzun bugün o çıtayı geçip geçmeyeceği konusunda dürüst olun.

6. **Yapıtlarınızın nasıl derlendiğini gerçekten yeniden üretebilir ve kanıtlayabilir misiniz?** Şifreleme özetli commit'lenmiş bir kilit dosyası derlemenizi bir fonksiyon yapmalıdır; aynı girdiler her makinede bu yıl ve gelecek yıl aynı çıktıyı verir ve kaynak, herkesin bir yapıtın gerçekten hattınızdan ve kaynak commit'inizden geldiğini doğrulamasını sağlamalıdır. Bu önemlidir, çünkü yeniden üretilemeyen bir derleme bir üretim hatasını çözülemez bir gizeme çevirir ve kurcalamanın gerçekleşmediğini kanıtlayamamanıza yol açar ve rakip değerlendirme çaba ile güvencedir: katı kilit dosyası kurulumları, imzalı doğrulama ve SLSA'ya hizalı kaynak, "sadece en yeniyi kur" akışının kaçındığı kurulum ve disipline mal olur. Kanıtı getirin: sürekli entegrasyon kilit dosyası ile bildirim uyuşmadığında başarısız oluyor mu, derleme başına bir SBOM ve imzalı bir kaynak kaydı üretip saklıyor musunuz ve hiç kimse birini doğruladı mı? Kurumsal ve özellikle kamu işi için kaynak ve SBOM giderek tedarik zorunluluklarının içinde yer alıyor; bu yüzden buradaki dürüst cevap ihaleye girmeye uygun kalıp kalmadığınızı ya da dışlanıp dışlanmadığınızı belirler.

## Sektör merceği

**Girişim.** Küçük bir takım ve platform grubu olmadan, süreç yerine varsayılanlara ve otomasyona yaslanın. Kilit dosyalarını ilk günden commit'leyin, yama sürümlerini toplu işleyen ve yeşil testlerde otomatik birleştiren otomatik bir güncelleyici açın ve paket eklemek için tek hafif bir kural tutun: sıkıcı, iyi sürdürülen kütüphaneleri tercih edin ve küçük olanlar için iki kez düşünün. Henüz dahili bir kayıt defteri kurmayacaksınız ve bu iyidir, ama commit'lenmiş özetler tek başına sizi zaten korur: zehirli bir sürüm basitçe kurulmaz.

**Küçük işletme.** Bağımlılık uzmanınız yok ve bütçeniz sıkı; bu yüzden disiplini inşa etmek yerine satın alın. Barındırma ve kod platformunuzun zaten sağladığı güncelleme otomasyonuna yaslanın, yükseltmelerin ucuz kalması için küçük bir olgun kütüphane kümesini tercih edin ve "etkilendik mi?" sorusuna kadrolamadan cevap verebilmek için hattınızda ücretsiz bir SBOM üreteci kullanın. Kıt dikkatinizi lisans kontrollerine ve bir düzine satırda kendiniz yazabileceğiniz önemsiz paketleri benimsememeye harcayın.

**Kurumsal.** Sorun birçok takım boyunca tutarlılıktır: kamusal ekosistemi yansıtan ve lisans, kaynak ve sürüm politikasını tek bir darboğazda uygulayan paylaşılan bir dahili kayıt defteri, artı varsayılan olarak seçilmiş bir altın kütüphane kümesi ve başka her şey için belgelenmiş bir istisna yolu. Tüm varlık boyunca maruziyetinizi tek bir sorgunun cevaplaması için derleme başına merkezi bir depoya bir SBOM yayımlayın, koordineli yükseltmeleri otomatik çekme istekleriyle yayın ve bağımlılık sağlığını depo başına bir kaza değil, ölçülen, yönetilen bir portföy olarak ele alın.

**Kamu.** Tedarik kuralları ve kamusal hesap verebilirlik her şeyi biçimlendirir. Satıcıların her sürümle makine tarafından okunabilir bir SBOM ve SLSA'ya hizalı derleme kaynağı teslim etmesini isteyin, dahili olarak yalnızca kamusal internete doğrudan yolu olmayan bir aynanın sunduğu onaylı bir yazılım listesinden kurun ve bir sistem on beş yıl çalışabileceği ve hepsi boyunca yamalanabilir olması gerektiği için istikrarlı bakımı ve net lisanslaması olan bağımlılıkları tercih edin. Kullanım ömrü sonu geçişlerini acil durumlar olarak değil bilinçli planlayın ve bir denetçinin gönderilen herhangi bir yapıtı kaynağına izlemesini sağlayan kayıtları tutun.

## Örnekler

**Girişim.** Altı kişilik bir girişim, bir çerçeve, bir ödeme kütüphanesi ve hiç incelemedikleri yaklaşık dokuz yüz geçişli paket üzerine kurulu bir web uygulaması yayımlar. Bir platform takımını karşılayamazlar; bu yüzden otomasyona yaslanırlar: ilk günden commit'lenen kilit dosyaları, yama sürümlerini toplu işleyen ve yeşil testlerde birleştiren otomatik bir güncelleyici ve biriken büyük sürüm artışlarını gözden geçirmek için aylık bir saat. Bağımlılık eklemek için tek paragraflık kuralları çoğunlukla "sıkıcı, iyi sürdürülen kütüphaneleri tercih edin ve küçük olanlar için iki kez düşünün"dür. Popüler bir paket ele geçirildiğinde, commit'lenmiş kilit dosyası özetleri zehirli sürümün basitçe kurulmayacağı anlamına geldi ve olayı yaşamak yerine okudular.

**Kurumsal.** Dört yüz deposu olan bir banka, kamusal ekosistemi yansıtan ve politikayı o darboğazda uygulayan dahili bir paket kayıt defteri işletir. Seçilmiş bir altın kütüphane kümesi, tek onaylı günlük çerçevesi, tek HTTP istemcisi, tek JSON ayrıştırıcısı varsayılandır ve başka her şey belgelenmiş bir istisna gerektirir. Bir iç kaynak modeli, her takımın bu paylaşılan kütüphanelere katkıda bulunmasına izin verirken küçük bir platform grubu onların sağlığına sahip olur. Koordineli yükseltmeler bir güvenlik yamasını dört yüz deponun tamamına otomatik çekme istekleriyle günler içinde yayar ve her derleme merkezi bir depoya bir SBOM yayımlar. Kritik bir güvenlik açığı duyurulduğunda tek bir sorgu çalıştırır ve haber döngüsü bitmeden maruziyetlerini bilirler.

**Kamu.** Bir federal kurum, 14028 sayılı Başkanlık Kararnamesi'ne izlenebilen kaynak ve SBOM gereksinimleri altında yazılım satın alır. Satıcılar her sürümle makine tarafından okunabilir bir SBOM teslim etmeli ve SLSA çerçevesine hizalı derleme kaynağı göstermelidir; böylece kurum her yapıtın iddia edilen kaynaktan geldiğini doğrulayabilir. Dahili olarak geliştiriciler yalnızca kamusal internete doğrudan yolu olmayan dahili bir aynanın sunduğu onaylı bir yazılım listesinden kurabilir. Uzun vadeli desteklenebilirlik seçimleri yönlendirir: bir sistem on beş yıl çalışabileceği ve hepsi boyunca yamalanabilir olması gerektiği için istikrarlı bakımı ve net lisanslaması olan bağımlılıkları tercih ederler. Bir bileşen kullanım ömrü sonuna ulaştığında, bir acil durum yerine planlı bir geçiş onun yerini alır.

## İş gerekçesi: motivasyonlar, YG ve TSM

Bağımlılık disiplininin getirisi çoğunlukla yaşanmayan felaketlerle ölçülür. Commit'lenmiş bir kilit dosyası ve yeniden üretilebilir bir derleme benimsemesi neredeyse bedavadır ve her biri günlerce kıdemli mühendislik zamanı yakabilen "benim makinemde çalışıyor" kusurlarının ve yeniden üretilemeyen üretim hatalarının tüm bir sınıfını ortadan kaldırır. Otomatik bir güncelleme temposu, bir yol haritasını durduran ve bir takımı tüketen, ara sıra haftalar süren acil yükseltmeyi, küçük birleştirilmiş değişikliklerin kararlı, düşük bir uğultusuna çevirir. Birçok depodan oluşan bir portföy boyunca nadir ve devasadan sık ve küçüğe kayma, bir mühendislik kuruluşuna açık en yüksek kaldıraçlı süreç değişikliklerinden biridir.

Toplam sahip olma maliyeti argümanı, bu sprint harcadığınızı değil yıllar boyunca taşıdığınızı ilgilendirir. Yönetilmeyen bağımlılıklar sessizce birikir: yeniden yazma olmadan artık yükseltilemeyen eskimiş sürümler, kimsenin fiyatlamadığı yasal maruziyet yaratan lisanslar ve tek bir gerekli yamanın bozucu değişikliklerin basamaklanmasını tetiklediği o kadar dolaşık bir çizge. Bunu yapmamanın maliyeti hepsi bir anda ve en kötü zamanda, bir güvenlik olayı ya da denetim ya da zorunlu bir geçiş sırasında gelir; yıllarca ertelenmiş bakımın faturası faiziyle ödenmeye geldiğinde. Gerekçeyi liderliğe sunmak için onların diliyle çerçeveleyin: yeniden üretilebilir derlemeler olay maliyetini azaltır, SBOM'lar güvenlik açığı müdahale süresini günlerden dakikalara indirir ve onaylı kütüphaneler artı kaynak aksi halde dışlanacağınız düzenlenen ve kamu sözleşmelerine girmeye uygun kalmanızı sağlar.

## Anti-kalıplar ve tuzaklar

- **Kilit dosyası yok ya da commit'lenmemiş:** derlemeler her seferinde yeniden çözümlenir; bu yüzden kimse neyin yayımlandığını ya da neyin bozulduğunu güvenle yeniden üretemez.
- **Üretimde kayan "latest":** kayıt defterinin o dakika sunduğu her şey sürümünüz olur; incelenmemiş ve izlenemez.
- **Zorlanana kadar asla güncellememek:** yıllarca sürüklenme, güvenlik açığı baskısı altında tek korkutucu, yüksek riskli bir acil yükseltmeye çöker.
- **Güncelleme botu yorgunluğu:** toplu işlenmemiş çekme isteği yağmuru, takımı acil olanlar dahil hepsini görmezden gelmeye alıştırır.
- **Bağımlılık yayılması:** önemsiz özellikler için paketleri refleksle eklemek; sürdürülemez bir çizge ve geniş bir saldırı yüzeyi büyütür.
- **Envanter yok:** SBOM olmadan "etkilendik mi?" sorusuna cevap vermek, depolar boyunca günlerce elle arkeoloji demektir.
- **Kamusal kayıt defterine körü körüne güvenmek:** doğrudan çekmeler sizi kesintilere, çekilmiş sürümlere, bağımlılık karışıklığına ve yazım hatası kapmacılığına maruz bırakır.
- **Geçişli bağımlılıkları görmezden gelmek:** riskin çoğu bir seviye aşağıda saklanırken yalnızca adını verdiğinizi yönetmek.
- **İncelenmemiş lisanslar:** lisansı sizin gönderme biçiminizle çatışan kodu içeri çekmek; yalnızca bir denetim ya da satın alma sırasında keşfedilir.

## Olgunluk modeli

- **Düzey 1, Başlangıç:** Bağımlılıklar değerlendirme olmadan serbestçe eklenir. Commit'lenmiş kilit dosyası yoktur, derlemeler yeniden üretilebilir değildir, güncellemeler yalnızca zorunlu acil durumlarda olur ve kimse yazılımın neyi içerdiğini sayamaz.
- **Düzey 2, Geliştirme:** Bazı takımlar kilit dosyalarını commit'ler ve çoğunlukla yeniden üretilebilir derlemeler elde eder ve biraz otomasyon güncelleme çekme istekleri açar, ama uygulama depodan depoya tutarsızdır. Lisans ve geçişli risk farkındalığı gayriresmidir; paylaşılan politika, envanter ya da paketlerin nereden geldiği üzerinde kontrol yoktur.
- **Düzey 3, Standartlaştırma:** Uygulamalar belgelenir ve kuruluş genelinde uygulanır. Otomatik bir güncelleyici makul toplu işlemeyle kararlı bir tempoda çalışır, derlemeler yalnızca kilit dosyalarından kurulur ve kilit dosyası ile bildirim uyuşmadığında başarısız olur, derleme başına bir SBOM üretilir, dahili bir kayıt defteri kaynak ve lisans politikasını uygular ve yeni bağımlılıklar her takımın uyguladığı yazılı bir kontrol listesine karşı değerlendirilir.
- **Düzey 4, Yönetme:** Bağımlılık varlığı temel çizgilere karşı veriyle ölçülür ve kontrol edilir. Sürüm gecikmesini (bir büyük sürümden fazla geride kaç bağımlılık olduğu), tüm yapıtlar boyunca kritik bir güvenlik açığını yamalamak için ortalama süreyi, otomatik güncelleme birleştirme oranlarını, gönderilen derlemelerin yüzdesi olarak SBOM kapsamını ve çözülmemiş elmas çatışmalarının ve politika istisnalarının sayısını izlersiniz. Bu metrikler sürümleri kapıya koyar ve çabayı nereye harcayacağınızı yönlendirir; böylece yükseltmeler ve düzeltmeler en yüksek sesle bağıranla değil kanıtla yönetilir.
- **Düzey 5, Orkestrasyon:** Bağımlılık yönetimi sürekli iyileştirilir ve kuruluş genelinde bütünleşir. Derleme kaynağı ve doğrulaması yakalanır ve doğrulanır, SBOM'lar anlık güvenlik açığı müdahalesi için tüm portföy boyunca sorgulanabilir, koordineli yükseltmeler birçok depo boyunca otomatik yayılır, altın kütüphaneler seçilir ve iç kaynak yapılır ve sistemin tamamı ekosistem, tehditler ve tedarik zorunlulukları kaydıkça uyum sağlar.

## Tartışma fikirleri

1. Takımınız için küçük bir yardımcıyı kendiniz yazmakla onun için bir bağımlılık üstlenmek arasındaki doğru çizgi nerede?
2. Sürüm kısıtlarınız ne kadar gevşek ya da sıkı olmalı ve cevap uygulamalar ile yayımlanmış kütüphaneler için farklılaşıyor mu?
3. Düşük riskli yama güncellemeleri yeşil testlerde otomatik birleşmeli mi ve bunu güvenli kılmak için test takımınızın neye ihtiyacı olurdu?
4. Dahili bir kayıt defteri ya da ayna, kuruluşunuzun boyutu ve risk profili için operasyonel maliyete değer mi?
5. Maksimum kontrol için hangi bağımlılıkları vendor'lamayı ve hangilerini kamusal kayıt defterinde bırakmayı önceliklendirirdiniz?
6. Gönderdiğiniz her yapıt için bir SBOM üretmek ve gerçekten kullanmak, bu çeyrekten başlayarak ne gerektirirdi?

## Önemli çıkarımlar

- Yazılımınızın çoğu ödünç koddur; onu iyi yönetmek bir sonradan düşünce değil, temel bir mühendislik disiplinidir.
- Kilit dosyalarını commit'leyin ve aynı girdilerin her zaman aynı çıktıyı üretmesi için yeniden üretilebilir, belirlenimci derlemeler talep edin.
- Nadir, zorunlu, korkutucu sıçramalar yerine küçük otomatik adımlarla sürekli güncelleyin.
- Bağımlılıkları yazılı bir çıtaya karşı bilinçli ekleyin; yönetmesi en ucuz olan, hiç üstlenmediğinizdir.
- Yazılımınızda neyin olduğunu ve nereden geldiğini her zaman bilmeniz için bir SBOM üretin ve derleme kaynağını yakalayın.
- Karışıklığa, yazım hatası kapmacılığına ve akış yukarısı başarısızlığına karşı savunmak için kaynaklarınızı bir dahili kayıt defteriyle kontrol edin.

## Kaynaklar ve ileri okuma

- U.S. Executive Order 14028, *Improving the Nation's Cybersecurity* (2021)
- National Institute of Standards and Technology (NIST), *Secure Software Development Framework* (SP 800-218)
- SLSA (Supply-chain Levels for Software Artifacts) framework specification, Open Source Security Foundation
- OWASP CycloneDX specification and the SPDX specification, for SBOM formats
- Tom Preston-Werner, *Semantic Versioning Specification (SemVer)*
- The Reproducible Builds project documentation
- Nicole Forsgren, Jez Humble, Gene Kim, *Accelerate: The Science of Lean Software and DevOps*
