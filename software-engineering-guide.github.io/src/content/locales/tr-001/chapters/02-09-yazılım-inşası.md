# 2.9 Yazılım inşası

## Genel bakış ve motivasyon

[Yazılım inşası](https://en.wikipedia.org/wiki/Software_construction), tasarımın çalışan koda dönüştüğü yerdir. Kodlamanın, doğrulamanın, [birim testinin](https://en.wikipedia.org/wiki/Unit_testing), [entegrasyon testinin](https://en.wikipedia.org/wiki/Integration_testing) ve [hata ayıklamanın](https://en.wikipedia.org/wiki/Debugging) ayrıntılı işidir. [Yazılım Mühendisliği Bilgi Birikimi](https://en.wikipedia.org/wiki/Software_Engineering_Body_of_Knowledge) (SWEBOK) Kılavuzu inşayı kendi bilgi alanı olarak ele alır ve bunun iyi bir nedeni var: günlük işinizin çoğu burada gerçekleşir. Satır satır yaptığınız seçimler (karmaşıklığı nasıl sınırladığınız, hataları nasıl ele aldığınız, işleri ne kadar okunabilir bıraktığınız) bir sistemin yıllarca anlaşılıp anlaşılamayacağını, değiştirilip değiştirilemeyeceğini ve güvenilip güvenilemeyeceğini belirler.

Büyük bir takımda inşa tek kişilik değil, bir grup çabasıdır. Yüzlerce mühendis, herhangi bir kişinin takımdaki süresinden uzun yaşayacak paylaşılan bir kod tabanına yazar. Bu yüzden çıta "bugün benim makinemde çalışıyor mu" değildir. "Bir yabancı bunu beş yıl sonra güvenle değiştirebilir mi"dir. İnşa yukarıya doğru, neyi inşa edeceğinizi ve biçimini söyleyen gereksinimlere (bölüm 2.8) ve tasarıma (bölüm 2.2) bağlanır. Yana doğru, işin nasıl ifade edildiğini, doğrulandığını ve denetlendiğini biçimlendiren kodlama standartlarına (bölüm 2.1), teste (bölüm 2.4) ve kod incelemesine (bölüm 2.5) bağlanır. İyi inşa, sağlam bir tasarımı sürdürülebilir bir varlığa dönüştürür. Kötü inşa, iyi bir tasarımı bile bir yükümlülüğe çevirir.

Kurumsal ve kamu ortamlarında inşa ek ağırlık taşır. Bu sistemler uzun ömürlü, ağır düzenlenmiş ve çoğu zaman güvenlik ya da vatandaş açısından kritiktir. [Savunmacı kodlama](https://en.wikipedia.org/wiki/Defensive_programming), disiplinli hata yönetimi ve bariz biçimde doğru kod burada incelikler değildir; onlar güvence, denetim ve on yıllar ve personel devri boyunca süreklilik için gereksinimlerdir. Amaç, niyetini ileten, başarısızlığa direnen ve doğrulanabilen koddur. Yalnızca çalışan kod yeterli değildir.

## Temel ilkeler

- Her şeyden önce karmaşıklığı en aza indirin; büyük ölçekli inşanın ana düşmanı kimsenin tam anlayamadığı koddur.
- Değişimi öngörün; olası gelecek değişikliklerin yerel ve ucuz olması için inşa edin.
- Doğrulama için inşa edin; doğruluğu testlerle, incelemeyle ve akıl yürütmeyle kontrol etmesi kolay kod yazın.
- Bilinçli yeniden kullanın; yeniden icat etmek yerine güvenilen mevcut bileşenler üzerine inşa edin, ama yanlış soyutlamalara bağlanmaktan kaçının.
- Standartları izleyin; bir kod tabanındaki tutarlılık her gelecek değişikliğin bilişsel maliyetini düşürür.
- Hataları ve geçersiz durumları açıkça ele alın; başarısızlık biçimlerini sessiz değil görünür kılın.
- Kodu okunabilir tutun; inşa önce gelecekteki bakımcılarla, sonra derleyiciyle iletişimdir.

## Öneriler

### Karmaşıklığı birincil disiplin olarak en aza indirin

Hem özsel hem kazara karmaşıklığı azaltmayı merkezi hedefiniz yapın. Küçük, tek amaçlı işlevler ve modüller yazın. Zekice numaralar yerine net adları tercih edin. İç içe geçmeyi sığ ve kontrol akışını doğrusal tutun. Kararları yerelleştirin; böylece bir kod parçasını anlamak tüm sistemi kafanızda tutmaya zorlamasın. Karmaşıklık, büyük kod tabanlarını değiştirmesi yavaş ve dokunması tehlikeli kılan şeydir; bu yüzden her seçimi karmaşıklık ekleyip eklemediğine ya da kaldırıp kaldırmadığına göre tartın. Bölüm 2.2'deki tasarım ilkelerini küçük ölçekte de uygulayın: yüksek bütünlük, düşük bağlaşım ve net [ilgilerin ayrılması](https://en.wikipedia.org/wiki/Separation_of_concerns) tek bir işlevde bir mimaride olduğu kadar önemlidir.

### Değişim ve doğrulama için inşa edin

En olası gelecek değişiklikleri (yeni iş kuralları, yeni entegrasyonlar, yeni düzenlemeler) önceden düşünün ve onları kararlı arayüzlerin ardında yalıtın; böylece değişim yerel kalır. Aynı zamanda doğrulaması kolay kod yazın: yapabildiğiniz yerde [saf işlevler](https://en.wikipedia.org/wiki/Pure_function) (aynı girdiler her zaman aynı çıktıyı verir, yan etki yok), asgari gizli durum ve testlerin yerlerine koyabilmesi için açık yapılmış bağımlılıklar. Test etmesi zor kod genellikle anlaması ve değiştirmesi zor koddur. Sınanabilirlik (bölüm 2.4) yalnızca bir kalite güvencesi kaygısı değil, bir tasarım sinyalidir.

### Bilinçli yeniden kullanın ve standartlaştırın

Temel mantığı yeniden yazmadan önce iyi sürdürülen, güvenilen kütüphanelere ve dahili bileşenlere uzanın ve onları net arayüzler aracılığıyla (bölüm 2.3) kullanın. Yeniden kullanılabilir bileşenleri yalnızca gerçek bir ikinci kullanım durumu olduğunda inşa edin, çünkü fazla erken genelleştirmek kendi başına bir karmaşıklık biçimidir. Kuruluşunuzun kodlama standartlarını ve üslubunu (bölüm 2.1) tekdüze uygulayın; ideal olarak otomatik biçimlendiriciler ve [linter'larla](https://en.wikipedia.org/wiki/Lint_(software)) zorlayın, böylece tüm kod tabanı tek bir özenli yazar yazmış gibi okunsun.

### Savunmacı programlamayı muhakemeyle uygulayın

Girdileri güven sınırlarında (dış istekler, dosya ve ağ G/Ç'si, kullanıcı girdisi) doğrulayın ve bu sınırları geçen her veriyi aksi kanıtlanana kadar düşmanca sayın. İyi test edilmiş bir modülün içinde ise her satırı mantığı gizleyen ve gerçek başarısızlıkları bastıran gereksiz kontrollere boğmayın. Kural basittir: sınırlarda savunun, içlerinde güvenin. Doğru bir programda asla yanlış olmaması gereken değişmezleri belgelemek ve uygulamak için [onaylamaları](https://en.wikipedia.org/wiki/Assertion_(software_development)) kullanın. Çalışma zamanında meşru olarak gerçekleşebilen koşullar için [istisnaları](https://en.wikipedia.org/wiki/Exception_handling) ve hata yönetimini kullanın. İkisini ayrı tutun: onaylamalar programcı varsayımlarını korur, hata yönetimi beklenen başarısızlığı yönetir.

### Hataları açıkça ele alın ve güvenli biçimde başarısız olun

Her hata için ne yapılacağına bilinçli karar verin: kurtar, yeniden dene, yay ya da hızlı başarısız ol. Bir istisnayı asla sessizce yutmayın ya da döndürülen bir hatayı görmezden gelmeyin; bastırılmış bir başarısızlık sonra gizemli bir kusur olarak geri gelir. Başarısızlıkların teşhis edilebilmesi için hata mesajlarınızda ve günlüklerinizde bağlamı koruyun. Güvenlik ve vatandaş açısından kritik sistemlerde, bozulmuş bir durumda devam etmek yerine güvenli, bilinen bir duruma başarısız olun. Hata yoluna mutlu yol kadar düşünce verin, çünkü üretimde güvenin kazanıldığı ya da kaybedildiği yer hata yoludur.

### İnşa sırasında kaliteyi içine kurun

Kalite sonradan denetlenerek değil, içine kurularak elde edilir. Birim testlerini kodla birlikte yazın, [statik analizi](https://en.wikipedia.org/wiki/Static_program_analysis) ve linter'ları sürekli çalıştırın ve işlevleri üzerinde akıl yürütülebilecek kadar küçük tutun. Yorumlarınız ne değil neden olduğunu açıklayabilsin diye kendini açıklayan adlar ve yapı kullanın. Kodu yaşanabilir tutmak için çalışırken [yeniden düzenleyin](https://en.wikipedia.org/wiki/Code_refactoring). Kod incelemesi (bölüm 2.5) insan güvencesidir, ama kalitenin çoğunun inceleme başlamadan önce orada olması gerekir.

### İnşa araçlarını seçin ve standartlaştırın

Her mühendisin tutarlı, yeniden üretilebilir bir ortamda çalışması için araç zincirini (derleyiciler, derleme sistemleri, biçimlendiriciler, linter'lar, statik çözümleyiciler, hata ayıklayıcılar, bağımlılık yöneticileri ve IDE yapılandırmaları) standartlaştırın. Kalite kontrollerinin isteğe bağlı olmaması için bu araçları hatta bağlayın. Yapay zeka destekli kodlama araçlarını bilinçli devreye alın ve çıktılarını, başka herhangi bir kodla aynı standartlardan, incelemeden ve testlerden geçmesi gereken bir taslak olarak ele alın.

## Ödünleşimler: artılar ve eksiler

| Uygulama | Artılar | Eksiler |
|---|---|---|
| Agresif karmaşıklık azaltma | Okunabilir, değiştirilebilir, düşük kusur oranı | Yavaş hissettirebilir; yanlış uygulanırsa aşırı soyutlama riski |
| Kapsamlı savunmacı kontroller | Kötü durumları erken yakalar, sağlam sınırlar | Mantığı dağıtır; aşırıya kaçılırsa gerçek hataları maskeleyebilir |
| Değişmezler için onaylamalar | Varsayımları belgeler ve uygular | Bazı üretim derlemelerinde devre dışı; hata yönetimi değildir |
| Kütüphanelerin yoğun yeniden kullanımı | Sahip olunacak daha az kod; daha hızlı teslimat | Bağımlılık riski, bağlaşım, tedarik zinciri maruziyeti |
| Katı standartlar ve linter denetimi | Tekdüze, düşük sürtünmeli kod tabanı | Baştan kurulum; bireylere katı hissettirebilir |
| Sınanabilirlik için inşa | Doğrulanabilir, değiştirilebilir kod | Bazılarının tören gördüğü dolaylılık ekleyebilir |

İnşadaki merkezi ödünleşim kısa vadeli hız ile uzun vadeli değiştirilebilirlik arasındadır. Köşeleri kesmek (hata yönetimini atlamak, karmaşıklığı hoş görmek, standartları görmezden gelmek) o anda daha hızlı hissettirir ve sistemin ömrü boyunca neredeyse her zaman daha pahalıdır. Ters başarısızlık aşırı mühendisliktir: çok fazla savunmacılık, spekülatif soyutlama ve kimsenin ihtiyaç duymadığı genellik. Ustalıklı inşa ortada yaşar: olabildiğince basit, sınırların gerektirdiği kadar savunmacı ve daha fazlası değil.

## Takımınızla tartışılacak sorular

1. **"Fazla karmaşık"ın ortak, somut tanımımız nedir ve onu birleştirmeden önce nerede uyguluyoruz?** "Karmaşıklığı en aza indir" inşanın merkezi disiplinidir, ama bir slogan olarak her tartışmayı bir son tarihe kaybeder. Yüzlerce kişinin tek bir kod tabanına yazdığı büyük bir takımda karmaşıklık ölçülebilir olmalıdır; bu yüzden gerçekten harekete geçeceğiniz sinyaller üzerinde anlaşın: işlev uzunluğu, iç içe geçme derinliği, döngüsel karmaşıklık ve bir okuyucunun tek bir değişikliği anlamak için kafasında tutması gereken şeylerin sayısı. Toplantıya en kötü örneğinizi getirin ve mevcut incelemenizin onu yakalayıp yakalamayacağını sorun. Cevap bir hat kapısına ya da inceleme kontrol listesi maddesine dönüşmelidir, çünkü bir araç tarafından uygulanan bir eşik, irade tarafından uygulanan bir ilkeden daha değerlidir ve bir sonraki işe alınanı kimsenin güvenle dokunamadığı kodun yavaş birikiminden kurtarır.

2. **Üretimde hata yollarımız tasarladığımız gibi davranıyor mu ve en son ne zaman birini bilerek çalıştırdık?** İnşa tavsiyesi hata yoluna mutlu yol kadar düşünce verin der; yine de hata yolu genellikle sahip olduğunuz en az test edilen koddur ve vatandaş açısından kritik ya da güvenlik açısından kritik bir sistemde güvenin kazanıldığı ya da kaybedildiği yerdir. Bastırılmış bir istisna ya da görmezden gelinen bir dönüş kodu haftalar sonra gizemli bir kusura dönüşür ve "güvenli bir duruma başarısız ol" olmasını hiç izlemediyseniz tutamayacağınız bir sözdür. Olay geçmişinizi getirin: geçmiş kesintilerin kaçı yutulmuş bir hataya ya da test edilmemiş bir kurtarma yoluna kadar izlendi? Eylem, başarısızlığı bilerek test etmek (reddedilen kartı, zaman aşımını, bozuk girdiyi enjekte edin) ve her hatanın ele alınmasını, bağlamla günlüklenmesini ya da yayılmasını, asla sessizce bırakılmamasını şart koşmaktır.

3. **Kod tabanımızın hangi parçalarını test etmek zor ve bu zorluk bize tasarım hakkında ne söylüyor?** Teste direnen kod neredeyse her zaman durumu gizleyen, yanlış bağımlılıklara bağlanan ya da çok şey yapan koddur; bu yüzden sınanabilirlik bir kalite güvencesi sonradan düşüncesi değil, bir tasarım sinyalidir. Uzun ömürlü bir kurumsal sistemde bu önemlidir, çünkü bugün test etmesi acı verici olan modüller, bir yabancının beş yıl sonra değiştirmekten korkacağı modüllerdir. Takımınızın test yazmaktan korktuğu sınıfı ya da hizmeti getirin ve nedenini sorun: durum mu gizli, bağımlılıklar yerine konulamaz mı, işlev üç iş mi yapıyor? Cevap yeniden düzenlemeyi saf işlevlere, açık bağımlılıklara ve küçük tek amaçlı birimlere doğru yönlendirmelidir, çünkü kodu doğrulanabilir kılmak, onu anlaşılır ve değiştirmesi ucuz kılmakla aynı iştir.

4. **Harici bir kütüphaneyi ne zaman yeniden kullanıyor, ne zaman yeteneği kendimiz inşa ediyoruz ve üstlendiğimiz tedarik zinciri riskinin sahibi kim?** Güvenilen bir kütüphaneye uzanmak temel mantığı yeniden icat etmekten hızlıdır; yine de eklediğiniz her bağımlılık kontrol etmediğiniz, kolayca denetleyemediğiniz ve ele geçirildiği gün yamalamanız gereken koddur. Büyük bir takımda tehlike, yüz mühendisin her birinin kendi geçişli bağımlılıklarını çekmesi ve sonunda kimsenin kod tabanının gerçekte ne çalıştırdığını söyleyememesidir. Bağımlılık envanterinizi getirin ve üç somut şey sorun: kaç kütüphane bakımsız, kaçı bilinen güvenlik açıkları taşıyor ve kaçı doğrudan sahiplenecek kadar basit mantığı sarıyor. Karşıt değerlendirme gerçektir, çünkü kendi şifrelemenizi ya da tarih işlemenizi yazmak neredeyse her zaman savaşta sınanmış bir kütüphaneden daha kötüdür; bu yüzden hedef toptan kaçınma değil, bilinçli bir yeniden kullanım politikasıdır. Kurumsal ve kamu ortamlarında tedarik ve lisans uyumu açısını ekleyin, çünkü incelenmemiş bir bağımlılık yükümlülüklerinizle uyumsuz bir lisans ya da hiçbir denetçinin kabul etmeyeceği bir kaynak taşıyabilir.

5. **Yapay zekanın ürettiği kodu insan yazımı kodla aynı inşa standartlarında nasıl tutuyoruz ve önemli olduğunda ikisini ayırt edebiliyor muyuz?** Yapay zeka kodlama asistanları inandırıcı taslakları hızla üretir ve cazibe, derlendiği ve deyimsel göründüğü için çıktılarını bitmiş saymaktır. Bölümün kuralı, üretilmiş kodun başka herhangi bir kodla aynı incelemeden, testlerden ve standartlardan geçmesidir ve büyük bir takımın bu kuralı arzu değil, uygulanabilir kılması gerekir. Yakın zamanda yayımlanan yapay zeka destekli değişikliklerden örnekler getirin ve her birinin test taşıyıp taşımadığını, statik analizi geçip geçmediğini ve onu gönderen insan tarafından gerçekten anlaşılıp anlaşılmadığını ya da güvenle geçirilip geçirilmediğini sorun. Karşıt baskı hızdır, çünkü bu asistanlar gerçekten verimlidir ve her öneriyi sürünmeye yavaşlatmak faydayı çöpe atar. Düzenlemeye tabi ve kamu bağlamlarında kaynak ve hesap verebilirlik açısını ekleyin, çünkü bir kod satırından kimin sorumlu olduğunu ve üretilmiş bir parçanın cevaplayamayacağınız bir lisans ya da telif hakkı sorusu taşıyıp taşımadığını onaylamanız gerekebilir.

6. **İnşa araç zincirimiz gerçekten standartlaştırılmış ve hatta uygulanıyor mu, yoksa bireyler hâlâ uyumsuz kurulumlarda mı çalışıyor?** Biçimlendirici, linter, statik çözümleyici, derleme sistemi ve bağımlılık yöneticisinden oluşan paylaşılan bir araç zinciri, kod tek ses gibi okunduğu ve kontroller her yerde aynı olduğu için bir mühendisin tanımadığı hizmetler arasında güvenle hareket etmesini sağlar. Kaydığında her takım kendi yapılandırmasını yeniden icat eder, inceleme zamanı üslup tartışmasıyla harcanır ve bir takımın çözümleyicisinin yakalayacağı kusurlar diğerinde sızar. Standart kontrolleri her commit'te çalıştırmayan depoların listesini getirin ve her birinin neden dışarıda kaldığını sorun. Gerilim, tek bir zorunlu kurulumun gerçekten farklı ihtiyaçları olan takımlara katı hissettirebilmesidir; bu yüzden tekdüzeliğin sürtünmeye nerede değdiğine ve belgelenmiş bir istisnanın nerede uygun olduğuna karar verin. Büyük bir kurum ya da kamu kuruluşu için bunu yeniden üretilebilirliğe ve denetime bağlayın, çünkü kontrollü bir araç zincirinden bayt bayt yeniden üretemediğiniz bir derleme, yıllar sonra bir değerlendiriciye savunamayacağınız bir derlemedir.

## Sektör merceği

**Girişim.** Hız kazanır; bu yüzden ilk günden paylaşılan bir biçimlendirici ve linter koyun, tek dış sınırınızda girdileri doğrulayın ve iç kodu her satırda savunmacı değil temiz tutun. Spekülatif soyutlamayı ve ağır süreci atlayın: iki üç mühendisle tüm takım kod tabanını kafasında tutar ve gerçek risk o paylaşılan hafızadan uzun yaşayan karmaşıklıktır. Temel her şey için güvenilen kütüphanelere yaslanın; böylece iyi sahip olabileceğiniz kadar az kod yazarsınız.

**Küçük işletme.** Özel bir derleme mühendisi ve sıkı bir bütçe olmadan, mevcut araçlarınızın bedavaya uyguladığı kurallara tercih verin: dille birlikte gelen bir biçimlendirici ve linter, makul varsayılanlar ve herkesin hatırlayabileceği küçük bir kural kümesi. Bakımını kadrolayamayacağınız altyapı kurmak yerine iyi sürdürülen kütüphaneleri satın alın ya da benimseyin. Sınırlı disiplininizi ihmal edildiğinde en çok acıtan iki şeye harcayın: sınırda girdiyi doğrulamak ve bir hatayı asla sessizce yutmamak.

**Kurumsal.** Yüzlerce mühendis paylaşılan koda yazarken öncelik tekdüzelik ve uygulamadır: hatta bağlı standart bir araç zinciri, statik analiz kapıları ve insanların hizmetler arasında güvenle hareket etmesi için her yerde uygulanan sınır doğrulama kuralları. Bağımlılık ve tedarik zinciri riskini takım başına doğaçlama yerine yönetilen bir süreç olarak yönetin ve her takım boyunca geçerli olması gereken alan değişmezlerini kodlamak için onaylamaları kullanın. İnşa standartlarını, bir kod tabanını on yıllar ve personel devri boyunca yaşanabilir tutan alt tabaka olarak ele alın.

**Kamu.** Uzun ömürlü, vatandaş açısından kritik sistemler disiplinli inşayı güvence ve hesap verebilirlik meselesi yapar. Mevzuat gibi değişken kuralları kararlı arayüzlerin ardında yalıtın; böylece değişim yerel ve gereksinimlere izlenebilir kalır, bozulmuş bir durumda devam etmek yerine güvenli, bilinen durumlara başarısız olun ve her modülü denetim kanıtı olarak da işlev gören testlerle gönderin. Tedarik ve şeffaflık yükümlülükleri araç zincirinizin, bağımlılıklarınızın ve hata yönetiminizin, yıllar sonra gelen bir memurun ya da dış bir denetçinin kodun doğru olduğunu doğrulayabileceği kadar iyi belgelenmesi gerektiği anlamına gelir.

## Örnekler

**Girişim.** Üç mühendislik bir girişim ilk günden paylaşılan bir biçimlendirici ve linter kurar ve her commit'te çalıştırır; böylece yüklenici eklerken bile kod tek ses gibi okunur. API sınırlarında girdileri doğrularlar ve dışarıdan gelen her şeyi düşmanca sayarlar, ama iç mantığı gereksiz kontrollerle boğmak yerine temiz tutarlar. Bir ödeme webhook'u başarısız olmaya başladığında düzeltme hızlıdır, çünkü hiçbir istisna sessizce yutulmamıştır ve hata mesajı nedene doğrudan işaret edecek kadar bağlam taşır. Tüm kurulum bir öğleden sonrasını aldı ve bir sonraki işe alınanın ilk haftasını sefil kılacak karmaşıklığın yavaş birikimini önledi.

**Kurumsal.** Küresel bir ödeme şirketi yüzlerce mühendis boyunca paylaşılan bir araç zinciri uygular: her commit'te otomatik biçimlendirme ve linter denetimi, hatta statik analiz kapıları ve tüm dış girdilerin hizmet sınırlarında doğrulanması kuralı. Alan mantığı "bir defter girdisi her zaman dengelidir" gibi değişmezleri uygulamak için onaylamalar kullanırken reddedilen kart gibi çalışma zamanı koşulları açık, günlüklenmiş sonuçlar olarak ele alınır. Standartlar tekdüze olduğu ve hatalar asla sessizce yutulmadığı için mühendisler tanımadıkları hizmetler arasında güvenle hareket eder ve üretim olayları doğrudan günlüklerden teşhis edilebilir.

**Kamu.** Ulusal bir vergi kurumu, değişen mevzuat altında on yıllarca çalışması beklenen uzun ömürlü bir tahakkuk sistemi inşa eder. İnşa her vergi kuralını kararlı bir arayüzün ardında yalıtır; böylece yıllık mevzuat değişiklikleri yerel ve gereksinimlere (bölüm 2.8) izlenebilir kalır. Savunmacı doğrulama vatandaşa dönük her girdiyi korur. Hata yolları, asla sessizce yanlış bir tahakkuk düzenlemeyen güvenli bir duruma başarısız olur. Her modül denetim kanıtı olarak birim testleriyle gönderilir. İnşa standartlaştırılmış ve iyi belgelenmiş olduğu için, yeni memurlar çoktan ayrılmış selefleri tarafından yazılan kodu güvenle sürdürebilir.

## İş gerekçesi: motivasyonlar, YG ve TSM

Disiplinli inşanın getirisi, yazılımı ucuz ve güvenle değiştirebilmenin kalıcı yeteneğidir ve bir sistemin toplam sahip olma maliyetinin çoğunun belirlendiği yer burasıdır. Yazılım ekonomisi çalışmaları tutarlı biçimde bir sistemin ömür boyu maliyetinin çoğunun bakım olduğunu ve bakım maliyetine kodun ne kadar anlaşılır ve değiştirilebilir olduğunun hâkim olduğunu gösterir. Karmaşıklığı en aza indirmek, hataları açıkça ele almak ve standartları izlemek her gelecek değişikliğin ve her üretim olayının maliyetini doğrudan düşürür.

Benimseme maliyeti mütevazıdır ve çoğunlukla baştadır: standartları belirlemek, linter'ları ve çözümleyicileri bağlamak ve doğrulanabilir, savunmacı kod yazma alışkanlığını oluşturmak. İhmalin maliyeti ise bileşiktir. Karmaşıklık, değiştirmesi yavaş ve dokunması riskli koda birikir. Sessiz hatalar pahalı üretim olaylarına dönüşür. Tutarsız üslup her incelemenin ve her uyumun çabasını çoğaltır. Gerekçeyi liderliğe sunmak için inşa kalitesini, inşa disiplininin doğrudan iyileştirdiği değişim başarısızlık oranına, ortalama kurtarma süresine, kusur kaçış oranına ve uyum süresine bağlayın.

## Anti-kalıplar ve tuzaklar

- **Karmaşıklık sürünmesi:** kimse anlayana kadar zekice, derin iç içe geçmiş ya da yayılan kod biriktirmek.
- **Sessiz hata yutma:** başarısızlıkları gelecekteki gizemlere çeviren boş catch blokları ve görmezden gelinen dönüş kodları.
- **Savunmacı programlama aşırılığı:** mantığı gömen ve gerçek kusurları maskeleyen her yerdeki gereksiz kontroller.
- **Onaylamaları hata yönetimiyle karıştırmak:** çalışma zamanı koşulları için onaylama, programcı değişmezleri için istisna kullanmak.
- **Kopyala-yapıştır inşa:** yeniden kullanmak yerine mantığı çoğaltmak; böylece düzeltmeler birçok yerde yapılmalıdır.
- **Spekülatif genellik:** hiç gelmeyen ihtiyaçlar için soyutlama ve yapılandırılabilirlik inşa etmek.
- **Standartları görmezden gelmek:** her mühendisin kendi yoluyla kodlaması; kod tabanı boyunca bilişsel yükü çoğaltmak.
- **Test edilmemiş inşa:** eşlik eden testler olmadan kod yazmak; doğrulamayı hiç gelmeyen bir aşamaya ertelemek.

## Olgunluk modeli

- **Düzey 1 (Başlangıç):** İnşa gelişigüzel ve reaktiftir; karmaşıklık ve hata yönetimi bireye göre değişir; az standart vardır ve sessiz başarısızlıklar yaygındır.
- **Düzey 2 (Geliştirme):** Kodlama standartları, biçimlendiriciler ve linter'lar vardır ve temel hata yönetimi ve birim testi beklenir, ama uygulama tutarsızdır ve her takım farklı uygular.
- **Düzey 3 (Standartlaştırma):** Karmaşıklığı azaltma, sınır doğrulama, açık hata yönetimi ve sınanabilirlik belgelenmiş ve kuruluş genelinde, hatta ve incelemede uygulanır; böylece tüm kod tabanı tek bir özenli yazar yazmış gibi okunur.
- **Düzey 4 (Yönetme):** İnşa kalitesi temel çizgilere karşı ölçülür; takım döngüsel karmaşıklığı, kusur kaçış oranını, değişim başarısızlık oranını, hata yolu test kapsamını ve kod inceleme bulgularını izler ve görüşe değil eğilimlere göre harekete geçer.
- **Düzey 5 (Orkestrasyon):** İnşa sürekli iyileştirilir ve kuruluş genelinde bütünleşir; savunmacı kalıplar, standartlar ve metrikler yeniden düzenlemeyi ve araçları besler; yapay zeka destekli araçlar aynı kalite kapıları altında çalışır ve uygulama diller, düzenlemeler ve riskler değiştikçe uyum sağlar.

## Tartışma fikirleri

- Kod tabanınızda kazara karmaşıklık en çok nerede birikiyor ve hangi inşa alışkanlıkları onu yaratıyor?
- Takımınızın girdileri nerede doğrulayıp nerede güveneceğine dair gerçek kuralı nedir?
- Mühendisleriniz onaylamaları hata yönetiminden ayırıyor mu ve bu ayrım tutarlı mı?
- Kalitenizin ne kadarı inşa sırasında içine kuruluyor, ne kadarı sonradan incelemede ya da testte yakalanıyor?
- Tedarik zinciri riski göz önüne alındığında bir kütüphaneyi yeniden kullanmaya mı yoksa inşa etmeye mi karar veriyorsunuz?
- Yapay zekanın ürettiği kod insan yazımı kodla aynı inşa standartlarında nasıl tutulmalı?

## Önemli çıkarımlar

- İnşa, tasarımın sürdürülebilir koda dönüştüğü yerdir; karmaşıklığı en aza indirmek merkezi disiplinidir.
- Değişim ve doğrulama için inşa edin: sınanabilir, değiştirilebilir kod anlaşılır koddur.
- Güven sınırlarında savunun, içlerinde güvenin ve hataları asla sessizce yutmayın.
- Değişmezler için onaylamaları, beklenen çalışma zamanı koşulları için hata yönetimini kullanın; karıştırmayın.
- Araçları ve üslubu standartlaştırın, bilinçli yeniden kullanın ve kaliteyi sonradan denetlemek yerine içine kurun.

## Kaynaklar ve ileri okuma

- IEEE Computer Society, *SWEBOK Guide (Guide to the Software Engineering Body of Knowledge)*, Software Construction knowledge area
- Steve McConnell, *Code Complete: A Practical Handbook of Software Construction*
- Robert C. Martin, *Clean Code: A Handbook of Agile Software Craftsmanship*
- Andrew Hunt and David Thomas, *The Pragmatic Programmer*
- Martin Fowler, *Refactoring: Improving the Design of Existing Code*
- John Ousterhout, *A Philosophy of Software Design*
