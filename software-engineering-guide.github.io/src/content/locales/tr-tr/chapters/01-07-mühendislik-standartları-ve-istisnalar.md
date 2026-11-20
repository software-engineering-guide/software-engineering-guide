# 1.7 Mühendislik standartları ve istisnalar

## Genel bakış ve motivasyon

Bir **mühendislik standardı**, işin nasıl yapıldığına dair belgelenmiş, üzerinde anlaşılmış bir kuraldır. Örneğin, "tüm hizmetler bir sağlık kontrolü uç noktası sunmalıdır" ya da "tüm herkese açık web sayfaları **[WCAG](https://en.wikipedia.org/wiki/Web_Content_Accessibility_Guidelines) (Web Content Accessibility Guidelines) 2.2 AA düzeyini** karşılamalıdır". Bir standart bir öneri değildir ve salt bir gelenek de değildir. Kuruluşun kendini bağladığı, ideal olarak denetleyebileceğiniz bir taahhüttür. Bu bölüm, standartların tüm yaşam döngüsü, büyük bir kuruluşun onları nasıl **yazdığı, yayımladığı, benimsediği, uyguladığı ve geliştirdiği** ve en az onun kadar önemli olarak, onların dışında meşru biçimde kalan durumları yönetilen bir **istisna süreci** (**muafiyet süreci** olarak da bilinir) aracılığıyla nasıl ele aldığı hakkındadır: bir standarttan belirtilen bir nedenle sapmak için belgelenmiş, süre sınırlı bir izin.

Motivasyon, ölçekte gayriresmi normların işlemeyi bırakmasıdır. Beş mühendis bir odayı paylaştığında "burada işleri nasıl yaparız" konuşma ve kendiliğinden özümsemeyle seyahat eder. Beş bin mühendis onlarca takıma, üç zaman dilimine ve on yıllık personel devrine yayıldığında, o örtük bilgi yüzlerce uyumsuz yerel alışkanlığa parçalanır. Standartlar, zor kazanılmış derslerinizi bir kez yazıya dökme yoludur; böylece her takım her birini kendi kesintisi aracılığıyla yeniden öğrenmek yerine onları miras alır. [Bilişsel yükü](https://en.wikipedia.org/wiki/Cognitive_load) azaltırlar, [kod incelemelerini](https://en.wikipedia.org/wiki/Code_review) üslup yerine öz hakkında yaparlar, insanların takımlar arasında hareket etmesine izin verirler ve denetçilere ve düzenleyicilere değerlendirecekleri somut bir şey verirler.

Ama standartların kendi başarısızlık biçimi vardır: katılık. Hiçbir istisna kabul etmeyen bir standart er ya da geç meşru işi engeller: bir deney, bir tedarikçi kısıtı, yazarların asla hayal etmediği gerçekten yeni bir durum. Takımlar o zaman ya durur ya da daha kötüsü standardı sessizce görmezden gelir; bu, *her* standardın inandırıcılığını aşındırır. Çare eski özdeyiştir: "istisna kuralı doğrular." Görünür, ilkeli bir istisna süreci, standartları hem inandırıcı hem insancıl tutan şeydir. Bu bölüm karar almaya ve yönetişime (bölüm 1.5) ve karar kayıtlarına (bölüm 1.6) dayanır ve doğrudan kodlama standartlarını ve üslubu (bölüm 2.1), kontrol listelerini (bölüm 12.2) ve şablonları (bölüm 12.3) besler.

## Temel ilkeler

- **Bir standart bir sonucu ifade eder ve bir gerekçe verir.** Kural artı gerekçe; *neden* olmadan insanlar gerçekten ne zaman geçerli olduğunu yargılayamaz.
- **Denetlenemiyorsa henüz bir standart değildir.** Özlemler yerine sınanabilir ifadeleri tercih edin.
- **Standartlar yaşayan belgelerdir.** Sürümlenir, sahiplenilir, tarihlenir ve gözden geçirilir; taşa kazınıp terk edilmez.
- **Yapabildiğiniz yerde uygulamayı otomatikleştirin; insan incelemesini muhakemeye saklayın.** Makineler mekanik olanı, insanlar anlamlı olanı denetler.
- **Sapmalar beklenir, utanılacak şey değildir, ama görünür olmalıdır.** Dürüst bir muafiyet, sessiz uyumsuzluktan her zaman iyidir.
- **Her istisnayı süreyle sınırlayın.** Kalıcı bir istisna standartta bir kusurdur; onu yüzeye çıkarın ve standardı düzeltin.
- **Jargon ve zorunluluklar yerine sözcükler ve örnekler.** İnsanlar anladıkları ve kopyalayabildikleri standartlara uyar.

## Öneriler

### Net, sınanabilir ve gerekçelendirilmiş standartlar yazın

İyi bir standart, okuyucuların nereye bakacağını bilmesi için öngörülebilir bir biçime sahip kısa, kendi içinde bütün bir belgedir. Tek bir **standart şablonu** (bölüm 12.3) benimseyin ve her yerde kullanın. Temel bölümler şunlardır:

- **Başlık ve tanımlayıcı:** alıntı için sabit bir ad ve referans numarası.
- **Durum:** taslak, etkin, yerine geçilmiş ya da emekli, bir tarihle.
- **Kural:** bir sonuç olarak, düz ve belirsizliksiz ifade edilmiş ("must", "should", "may" bilinçli kullanılmış, gereksinim anahtar sözcükleri için **RFC 2119** kurallarına göre).
- **Gerekçe:** bu kural *neden* var; önlediği maliyet ya da risk.
- **Örnekler:** uyumlu bir örnek ve uyumsuz bir örnek; somut, soyuttan iyidir.
- **Nasıl denetlenir:** onu doğrulayan otomatik test, linter kuralı ya da inceleme adımı.
- **Sahibi ve gözden geçirme tarihi:** kim sürdürür ve ne zaman yeniden ele alınır.

Gerekçe ve "nasıl denetlenir" alanları gerçek bir standardı bir dilekten ayıran şeydir. Bir kuralın neden var olduğunu söyleyemiyorsanız, olması gerekip gerekmediğini sorgulayın. Uyumun nasıl doğrulandığını söyleyemiyorsanız, kural tutarsız uygulanır ve kızgınlık yaratır.

### Her standardı bir iyi uygulama kontrol listesiyle eşleştirin

Standartlar varış noktasını tanımlar. Bir **iyi uygulama kontrol listesi**, yani onaylanacak somut adımların ya da maddelerin kısa, sıralı bir listesi, insanların oraya varmasına yardım eder ve incelemeden önce kendi kendilerini doğrulamalarına izin verir. Kamu sektörü mühendislik el kitapları bu kalıbı yoğun kullanır. **[NHS Wales](https://en.wikipedia.org/wiki/NHS_Wales)** ve **Digital Health and Care Wales (DHCW)** mühendislik standartlarını pratik kontrol listeleriyle yayımlar ve **[UK Government Digital Service](https://en.wikipedia.org/wiki/Government_Digital_Service) (GDS)** Hizmet Standardı'nı ve Teknoloji Uygulama Kurallarını Hizmet Kılavuzu'nun uygulanabilir rehberliğiyle eşleştirir. Kontrol listesi kullanılabilir hale getirilmiş standarttır: "Bir erişilebilirlik denetimi eklediniz mi? Bir ekran okuyucuyla test ettiniz mi? Yalnızca klavyeyle gezinmeyi kapsadınız mı?" Kontrol listesi kalıbının tamamı için bölüm 12.2'ye bakın.

### Standartları insanların zaten çalıştığı yerde yayımlayın ve bulunabilir tutun

Standartları Markdown olarak **[sürüm kontrolünde](https://en.wikipedia.org/wiki/Version_control)** (bir kaynak deposunda) saklayın ve aranabilir bir dahili siteye dönüştürün; böylece çekme istekleri aracılığıyla tarihçe, inceleme ve farkları bedavaya alırlar; karar kayıtları için de aynı argüman geçerlidir (bölüm 1.6). Bir katalog, bir şablon, bir arama kutusu. Yüzeye çıkarmak, saklamak kadar önemlidir. İlgili standardı çekme isteği şablonundan, linter'ın hata mesajından ve hizmetin iskeletinden bağlayın, böylece doğru kural kimsenin uğramadığı bir klasörde değil, işin anında görünür.

### Önce otomasyonla, sonra insan incelemesiyle uygulayın

Bir standardı uygulamanın iki yolu vardır ve olgun kuruluşlar ikisini de bilinçli kullanır:

- **Otomatik uygulama:** [linter'lar](https://en.wikipedia.org/wiki/Lint_(software)), biçimlendiriciler, [statik analiz](https://en.wikipedia.org/wiki/Static_program_analysis), kod olarak politika (örneğin **Open Policy Agent (OPA)**), **[sürekli entegrasyon](https://en.wikipedia.org/wiki/Continuous_integration) (CI)** kapıları ve **mimari uygunluk fonksiyonları** (bir tasarım özelliğinin hâlâ geçerli olduğunu doğrulayan otomatik testler). Otomasyon tutarlı, yorulmaz, anlık ve tartışılmazdır; bu da onu standartların mekanik çoğunluğu (biçimlendirme, adlandırma, bağımlılık kuralları, gerekli meta veri) için ideal kılar.
- **İnsan incelemesi:** kod incelemesi, mimari inceleme kurulları ve güvenlik incelemesi; makinelerin yargılayamayacağı şeylere saklanır: bir soyutlamanın sağlam olup olmadığı, bir ödünleşimin akıllıca olup olmadığı, bir standardın harfi sakar olsa bile *amacının* karşılanıp karşılanmadığı.

Pratik kural: **denetlenebilir olanı otomatikleştirin ve kıt insan dikkatini muhakemeye harcayın.** İncelemeden CI'ye taşıyabildiğiniz her standart, incelemecileri yalnızca onların yapabileceği düşünmeyi yapmaya serbest bırakır.

### Sapmaları belgelenmiş bir istisna/muafiyet süreciyle yönetin

Hiçbir standart her duruma uymaz, bu yüzden kaçış kapısını bilerek tasarlayın. İyi bir istisna süreci şunları belirtir:

- **Muafiyeti kim verebilir:** riskle orantılı, adı konmuş, hesap verebilir bir yetki (düşük riskli bir üslup sapması için bir teknik lider; bir güvenlik kontrolü muafiyeti için bir mimari ya da güvenlik kurulu). Bu doğrudan bölüm 1.5'in yönetişim modeline bağlanır.
- **Neyin kaydedilmesi gerekir:** sapılan standart, belirli neden, kapsam, telafi edici kontroller ya da hafifletmeler ve kabul edilen risk. Bunu bir karar kaydı olarak yakalayın (bölüm 1.6) ki gerekçe korunsun.
- **Zorunlu bir son kullanma tarihi:** her muafiyet açık bir bitiş tarihiyle **süre sınırlıdır**. Bu en önemli tek kuraldır: geçici bir istisnanın sessizce kalıcı politikaya dönüşmesini önler.
- **Periyodik gözden geçirme:** bir sahip açık muafiyetleri bir ritimle gözden geçirir ve onları yeni gerekçeyle yeniler, iş uyumlu hale geldiğinde kapatır ya da aynı istisna tekrar edip duruyorsa bunu *standardın kendisinin* yanlış olduğunun kanıtı sayar ve onu revize eder.

Bu son nokta "istisna kuralı doğrular"ın özüdür. Tek bir standarda karşı sürekli bir muafiyet akışı bir disiplin başarısızlığı değildir. Veridir. Standardın yanlış kalibre edildiğini söyler ve çözüm istisnalar vermeyi sürdürmek değil, standardı geliştirmektir.

### Standartları net sahiplikle yaşayan belgeler olarak ele alın

Her standarda onu güncel tutmaktan sorumlu bir **sahip** (yalnızca bir kişi değil, bir rol) ve bir **gözden geçirme ritmi** (en az yılda bir) verin. Herkesin bir çekme isteği ya da bir **[RFC](https://en.wikipedia.org/wiki/Request_for_Comments) (yorum talebi)**, benimsemeden önce geri bildirim için dolaştırılan yazılı bir öneri, aracılığıyla bir değişiklik önermesi için hafif bir yol sağlayın. Standartları sürümleyin, açıkça kullanımdan kaldırın ve değişiklikleri duyurun. Hiç gözden geçirilmeyen bir standart kataloğu, insanların seçici alıntıladığı ve az güvendiği folklora çürür.

## Ödünleşimler: artılar ve eksiler

| Seçim | Artılar | Eksiler |
|---|---|---|
| **Çok sayıda ayrıntılı standart** | Tutarlılık, kolay uyum, denetime hazır | Katılık; bakım yükü; uygulamayı geçebilir |
| **Az sayıda üst düzey standart** | Esnek; düşük bakım | Tutarsızlık; takım başına daha çok yeniden tartışma |
| **Otomatik uygulama** | Tutarlı, anlık, yorulmaz, ölçeklenebilir | Başlangıç maliyeti; yanlış pozitifler; amaca kör |
| **İnsan incelemesiyle uygulama** | Amacı ve nüansı yargılar | Yavaş, tutarsız, ölçekte darboğaz |
| **Katı, istisnasız** | Basit mesaj; oyunlaştırılacak bir şey yok | Meşru işi engeller; sessiz uyumsuzluğu yönlendirir |
| **Yönetilen istisna süreci** | Standartları inandırıcı ve insancıl tutar | Yönetişim, kayıtlar ve takip gerektirir |

Temel gerilim **tutarlılık ile esneklik** arasındadır. Bir standart varyasyonu ortadan kaldırmak için vardır; bir istisna süreci gerçekten haklı olan varyasyonu kabul etmek için vardır. Katılığa çok yaslanırsanız insanlar standartlarınızı dolanır. Gevşekliğe çok yaslanırsanız standartlar hiçbir şey ifade etmez. İstisna süreci, sağlam bir çizgiyi tutmanıza *ve* gerçeklik konusunda dürüst kalmanıza izin veren basınç valfidir.

## Takımınızla tartışılacak sorular

1. **Ölçeğiniz için doğru standart sayısı nedir ve sizinkiler katılığa mı yoksa tutarsızlığa mı kayıyor?** Katalogun kendisi bir ödünleşimdir: çok sayıda ayrıntılı standart, katılık ve bakım yükü pahasına tutarlılık, kolay uyum ve denetime hazırlık satın alır; az sayıda üst düzey standart esnek kalır ama her takımın aynı soruları yeniden tartışmasına izin verir. Büyük bir kurumsal kuruluş ya da kamu organı için doğru boyut, gerçekte ne kadar varyasyona tahammül edebileceğinize karşı denetçilerinizin ve uyumunuzun ne kadarının sabitlenmesine ihtiyaç duyduğuna bağlıdır. Kanıt getirin: kaç etkin standardınız var, kaçı son yılda gözden geçirildi ve takımlar bir standardın çözebileceği şeyleri ne sıklıkla yeniden tartışıyor. Uygulamayı geçen bir katalog folklora dönüşür ve çok ince olan her takıma maliyet iter. Neyin bir standardı hak ettiğine bilinçli karar verin ve yerini hak etmeyenleri budayın.

2. **Bir standardın harfi otomatik geçerken amacı nerede sessizce ihlal ediliyor ve bunu nasıl yakalayacaksınız?** Otomasyon tutarlı, yorulmaz ve amaca kördür; bu, bir linter ya da politika kontrolünün gerçek hedef (sağlam bir soyutlama, akıllıca bir ödünleşim, gerçekten erişilebilir bir sayfa) kaçırılırken yeşile dönebileceği anlamına gelir. Pratik kural denetlenebilir olanı otomatikleştirmek ve kıt insan incelemesini muhakemeye harcamaktır ve zor kısım, hangi standartların hiçbir CI kapısının ileri süremeyeceği bir amaca sahip olduğu üzerinde anlaşmaktır. Örnekler getirin: insanların harfine uyup amacı bozdukları standartlar; örneğin hizmet bozukken sağlıklı bildiren bir sağlık kontrolü uç noktası ya da biçimlendiriciyi geçen ama anlamı gizleyen kod. Düzenlemeye tabi ortamlarda amaç en çok güvenlik ve emniyet kontrolleri için önemlidir; burada yeşil bir onay kutusu gerçek riski gizleyebilir. Hangi standartların özellikle amacı yargılamak için bir insan incelemecisi tuttuğuna karar verin ve o standartları sonuç etrafında ifade edin, böylece hem makine hem incelemeci aynı hedefe nişan alır.

3. **Muafiyetten standarda geri bildirim döngüsüne kim sahip ve tekrarlayan bir istisna kuralı değiştirmenize hangi noktada zorlar?** Tek bir standarda karşı sürekli bir muafiyet akışı veridir, disiplinsizlik değil ve sinyal, onu okuyup harekete geçmekten sorumlu biri olmadıkça boşa gider. Karşıt değerlendirme, bir standardı revize etmenin gerçek iş olmasıdır; bu yüzden onların altındaki yanlış kalibre edilmiş kuralı düzeltmektense muafiyetleri onaylamayı sürdürmek daha kolay kalır. Sayıları getirin: hangi standartlar en çok istisna üretiyor, muafiyetler gerçekten süre sınırlı mı ve bir ritimle gözden geçiriliyor mu ve kaçı sessizce kalıcı oldu. Kurumsal ve kamu alanındaki emniyet açısından kritik ve güvenlik açısından kritik standartlar için bir muafiyet telafi edici kontrolleri, bir hafifletmeyi, kabul edilen riski ve sert bir son kullanma tarihini kaydetmelidir; yoksa geçici bir sapma, bir sonraki denetimde yüzeye çıkan belgelenmemiş politikaya dönüşür. Açık muafiyetleri gözden geçirmek için bir sahip atayın, tekrarlayan istisnaların bir standart revizyonunu tetiklediği bir eşik belirleyin ve kalıcı bir istisnayı düzeltilecek bir standart kusuru olarak ele alın.

4. **Doğru standart iş anında görünüyor mu, yoksa kimsenin açmadığı bir klasörde mi yaşıyor?** Kimsenin bulamadığı bir standart şansla uygulanır ve ölçekte uyumsuzluğun çoğu meydan okuma değil cehalettir: bir mühendis kuralın var olduğunu hiç bilmedi ya da önemli olduğunda onu bulamadı. Karşıt değerlendirme çabadır, çünkü bir standardı çekme isteği şablonunda, linter'ın hata mesajında ve hizmet iskeletinde yüzeye çıkarmak, tek bir merkezi sitenin gerektirmediği gerçek entegrasyon işi maliyeti taşır. Bulunabilirlik hakkında kanıt getirin: mühendisler standartları bugün gerçekte nasıl buluyor, yeni bir işe alınan görevlerini yöneten erişilebilirlik ya da güvenlik kuralını bir dakikadan kısa sürede bulabiliyor mu ve incelemeciler yazarın sadece görmediği bir standardı ne sıklıkla alıntılıyor. Büyük bir kurumsal kuruluş ya da kamu organı için denetçiler giderek yalnızca bir standardın var olup olmadığını değil, karar anında iletilip erişilebilir olup olmadığını sorar; bu yüzden yüzeye çıkarmayı sonradan düşünülen bir şey değil, standardın parçası olarak ele alın ve insanların ihtiyaç duyduklarında kurala ulaşıp ulaşamadığını ölçün.

5. **Her etkin standardın sahibi kim, en son ne zaman gözden geçirildi ve sessizce folklora çürümüş olanları nasıl fark edersiniz?** Standartlar sessizce çürür: üç yıl önce artık kullanmadığınız bir çerçeve için yazılmış bir kural hâlâ katalogda durur, seçici alıntılanır ve az güvenilir, hâlâ doğru olan standartların inandırıcılığını aşağı çeker. Büyük bir kuruluş için sahipliğin maliyeti, bir kesinti ya da bir denetim gerçeklikle uyuşmayan bir standardı ortaya çıkarana kadar yük gibi hissettiren gözden geçirme ritminin kendisidir. Tartışmaya sayıları getirin: kaç standardın adı konmuş bir sahibi var (ayrılmış bir birey değil, bir rol), kaçı son yılda gözden geçirildi, kaçı resmen kullanımdan kaldırıldı ve kaçı sadece eskimiş ve hangileri en çok ve en az alıntılanıyor. Kurumsal ve kamu ortamlarında bir denetçi her standardın sürümlenmiş, tarihlenmiş ve kanıtlanabilir biçimde güncel olmasını bekler; bu yüzden asgari bir gözden geçirme ritmi üzerinde anlaşın, her standarda sorumlu bir sahip atayın ve yerini hak etmeyenleri, diğerlerine olan güveni zedelemeden önce emekliye ayırın.

6. **Bir muafiyeti verme yetkisi, muaf tutulan standardın riskiyle gerçekten orantılı mı?** Bir üslup sapması ile bir güvenlik kontrolü sapması aynı karar değildir; yine de birçok kuruluş ikisini de ağır bir kurula yönlendirir (bu, meşru işi durdurur) ya da ikisinin de tek bir teknik lider tarafından geçmesine izin verir (bu, ciddi bir riskin onu kabul etme yetkisi olmayan biri tarafından kabul edilmesine yol açar). Gerilim hız ile hesap verebilirlik arasındadır: çok fazla onay sürtünmesi sessiz uyumsuzluğu yönlendirir, çok azı ise sonuçlu sapmaların bir sohbet dizisinde geçiştirilmesi demektir. Standartlarınızın onay yetkililerine bir haritasını ve yakın zamanda verilen muafiyetlerin bir örneğini getirin ve birinin emniyet açısından kritik ya da güvenlik açısından kritik bir kontrolü karşılık gelen kurul, telafi edici kontrol, hafifletme ve kaydedilmiş risk kabulü olmadan muaf tutup tutmadığını kontrol edin. Kurumsal ve kamu alanı için bu, düzenleyicilerin doğrudan incelediği bir görev ayrılığı sorusudur; bu yüzden her standart sınıfını riskiyle orantılı adı konmuş bir yetkiye bağlayın ve riski kabul eden kişinin sonuçlardan gerçekten sorumlu olduğundan emin olun.

## Sektör merceği

**Girişim.** Katalogu küçük tutun: yalnızca yokluğu size gerçekten zarar verecek bir avuç kuralı yazın; örneğin bir biçimlendirici yapılandırması, bir sağlık kontrolü gereksinimi ve klavyeyle gezinilebilir sayfalar; ve her birini bir inceleme toplantısıyla değil, bir linter ya da CI kontrolüyle uygulayın. Muafiyet kurulunu tümüyle atlayın; koddaki tarihli bir TODO ve çekme isteğinde tek satırlık bir not bu ölçekte mükemmel bir süre sınırlı istisnadır. En kıt kaynağınız mühendislik dikkatidir, bu yüzden henüz sahip olmadığınız sorunlar için standart yazmaya direnin.

**Küçük işletme.** Özel bir standart sahibi ve sıkı bir bütçe olmadan standartlarınızı inşa etmek yerine satın alın: UK GDS Hizmet Standardı, OWASP güvenlik rehberliği ya da çerçevenizin önerilen lint kuralları gibi yayımlanmış temelleri benimseyin ve araçlarınıza ve barındırılan CI'ye zaten yerleşik kontrollere yaslanın. Yalnızca size özgü birkaç şey için yerel kuralların tek kısa bir sayfasını tutun. Mühendisliği kim yönetiyorsa istisnaları bilette bir son kullanma tarihiyle verir ve kaydeder; böylece hafif bir süreç bile dürüst kalır.

**Kurumsal.** İş birçok takım arasında yönetişimdir: bir katalog, bir şablon, her standart için gerekçe ve örnekler ve mekanik çoğunluk için boru hattını başarısız kılan kod olarak politika. Onay yetkisi riskle orantılı bir muafiyet süreci yürütün, her istisnayı süreyle sınırlayın, açık muafiyetleri bir ritimle gözden geçirin ve tekrarlayan muafiyetleri bir standardın değişmesi gerektiğinin sinyali olarak madenleyin. Otomatik uygulanan standartların payını ve açık muafiyetlerin hacmini ve yaşını ölçün ve her ikisini yönetişim işlevine raporlayın; böylece standartlar bir mezarlık değil yönetilen bir sistem kalır.

**Kamu.** Mühendislik standartlarınızı DHCW ve GDS geleneğinde açıkça yayımlayın ve her birini takımların bir hizmet değerlendirmesinden önce tamamladığı bir kontrol listesiyle eşleştirin; böylece uyum kamuya ve gözetim organlarına görünür olur. Sonuçlu muafiyetler için yetkiyi adı konmuş bir kıdemli sorumlu sahip yapın ve her istisnanın belirli ölçütü, telafi edici kontrolü ya da geçici hafifletmeyi, bir iyileştirme planını ve sert bir son kullanma tarihini kaydetmesini isteyin. Tedarik ve şeffaflık kuralları, standartlarınızın ve sapmalarınızın ikisinin de kamu kaydının parçası olduğu anlamına gelir; bu yüzden denetlenebilirliği ve izlenebilirliği baştan tasarım gereksinimleri olarak ele alın.

## Örnekler

**Girişim.** Yedi kişilik bir girişim tam olarak üç yazılı standart tutar (paylaşılan bir biçimlendirici yapılandırması, bir sağlık kontrolü uç noktası gereksinimi ve "tüm herkese açık sayfalar klavyeyle gezinilebilir olmalıdır"); her biri bir inceleme toplantısıyla değil, bir linter ya da CI kontrolüyle uygulanır. Bir mühendis sağlık kontrolü kuralını bozan geçici bir prototip yayımlaması gerektiğinde bir muafiyet kurulu yoktur: kodda tarihli bir TODO ve çekme isteğinde nedenini ve ne zaman düzelteceğini söyleyen tek satırlık bir not bırakır. Bu girişim ölçeğinde süre sınırlı bir istisnadır; süreç yükü olmadan dürüst ve görünür. Üç kontrol, kod incelemesini üslup yerine öz hakkında tutarak kendini öder.

**Kurumsal.** Küresel bir banka yaklaşık kırk etkin standarttan oluşan bir dahili mühendislik el kitabı tutar; her biri bir gerekçe, örnekler ve bağlantılı bir iyi uygulama kontrol listesiyle tek bir şablondadır. Yaklaşık %70'i otomatik uygulanır: biçimlendirme, bağımlılık politikası, zorunlu hizmet meta verisi ve CI boru hattını başarısız kılan kod olarak politika biçiminde kodlanmış güvenlik kontrolleri. Bir ödeme takımının, zorunlu bir şifreleme özelliğini henüz desteklemeyen bir veritabanında yayımlaması gerekir. Yayını engellemek yerine, standardı, telafi edici kontrolü (uygulama katmanı [şifreleme](https://en.wikipedia.org/wiki/Encryption)) ve 90 günlük son kullanma tarihini adlandıran bir muafiyet dosyalarlar. Güvenlik kurulu onu verir ve kaydeder. Doksan gün sonra gözden geçirme, platformun artık özelliği yerel olarak desteklediğini bulur ve muafiyet kapatılır. Standart tuttu, iş yayımlandı ve sapma bir sonraki denetim için tamamen izlenebilir.

**Kamu.** DHCW ve GDS yaklaşımına göre modellenmiş ulusal bir sağlık kurumu mühendislik standartlarını açıkça yayımlar; her biri takımların bir hizmet değerlendirmesinden önce tamamladığı bir kontrol listesiyle eşleşir. WCAG 2.2 AA'ya erişilebilirlik, CI'de otomatik bir denetim artı manuel bir değerlendirmeyle uygulanan sert bir standarttır. Eski bir klinik sistem, hasta güvenliği açısından kritik işlevselliği riske atmadan bir erişilebilirlik ölçütünü hemen karşılayamaz. Takım süre sınırlı bir istisna ister. Adı konmuş bir kıdemli sorumlu sahip onu verir ve belirli ölçütü, geçici hafifletmeyi (yardımlı erişim telefon hattı), iyileştirme planını ve altı aylık son kullanma tarihini kaydeder; gözetim organlarının talep ettiği izlenebilir, gözden geçirilebilir kanıtı tam olarak oluşturur (bölüm 4.6, 10.4).

## İş gerekçesi: motivasyonlar, YG ve TSM

Bir standart, onu yazmaya, kontrolünü otomatikleştirmeye ve sürdürmeye harcanan zamana mal olur. Getiri, kontrol her çalıştığında ve bir mühendis her yerleşik bir soruyu durup tartışmak zorunda kalmadığında ödenir. Standartlar yinelenen, dağıtık karar maliyetini bir kerelik yazma maliyetine çevirir; karar kayıtlarıyla (bölüm 1.6) aynı ekonomi, bir standart tek bir geçmiş seçimi değil binlerce gelecek örneği yönettiği için güçlenir.

**Toplam sahip olma maliyeti (TSM)**, yani bir sistemi inşa etmenin, işletmenin ve sürdürmenin tam ömür boyu maliyeti açısından standartlar en büyük kalemleri düşürür: uyum (yeni işe alınanlar tutarlılığı tersine mühendislikle çözmek yerine miras alır), bakım (tekdüze kod değiştirmesi daha ucuzdur) ve güvence (uyum makine tarafından denetlenebilir olduğunda ve sapmalar zaten belgelendiğinde denetimler daha ucuzdur). İstisna süreci bu getiriyi ana tehdidinden korur: standartların göz ardı edilen folklora çürümesi. İnandırıcı bir muafiyet süreci standartları güvenilir tutar ve güvenilir standartlar insanların gerçekten uyduğu standartlardır. Tüm bunları atlamanın maliyeti hiçbir panoda görünmez. Yavaş uyum, tutarsız kalite ve denetim bulguları olarak ortaya çıkar ve her yeni takım ve her ayrılışla bileşir.

## Anti-kalıplar ve tuzaklar

- **Gerekçesiz kurallar:** kimsenin anlamadığı bir standart, kimsenin doğru uygulayamayacağı ya da dürüstçe itiraz edemeyeceği bir standarttır.
- **Özlem düzeyinde, denetlenemeyen standartlar:** "kod sürdürülebilir olmalı" bir değerdir, standart değil; uygulanamaz ya da itiraz edilemez.
- **İstisna süreci yok:** meşru işi engellemek ile sessiz uyumsuzluğa tahammül etmek arasında sahte bir seçime zorlar.
- **Kalıcı istisnalar:** son kullanma tarihi olmayan, sessizce gerçek, belgelenmemiş politikaya dönüşen muafiyetler.
- **Kayıtsız muafiyetler:** koridorda ya da bir sohbet dizisinde verilen, sonraki denetime ve sonraki mühendise görünmez sapmalar.
- **Sinyali görmezden gelmek:** aynı istisnayı, standardın değişmesi gerektiğinin kanıtı olarak okumak yerine tekrar tekrar vermek.
- **Dırdırla uygulama:** bir linter'ın yakalaması gerekeni yakalamak için incelemecilere güvenmek, muhakemeyi mekanik olana harcamak.
- **Standart mezarlığı:** bir kez yazılmış, kimseye ait olmayan, hiç gözden geçirilmeyen, seçici alıntılanan, az kişinin güvendiği bir katalog.
- **Jargon kapı bekçiliği:** okuyucuları için değil yazarları için yazılmış, kopyalanacak örnekleri olmayan standartlar.

## Olgunluk modeli

- **Düzey 1 (Başlangıç):** Standartlar kıdemli mühendislerin kafalarındaki kabile bilgisidir ve reaktif uygulanır. Uygulama gelişigüzel kod incelemesi dırdırıdır; sapmalar görünmezdir; "bizim yaptığımız yol" takıma ve değişikliği kimin incelediğine göre değişir.
- **Düzey 2 (Geliştirme):** Bazı standartlar yazılıdır, tutarsız biçimlerde ve dağınık konumlarda ve benimseme takımdan takıma çok değişir. Uygulama çoğunlukla manueldir. İstisnalar kayıt ya da son kullanma tarihi olmadan gayriresmi gerçekleşir.
- **Düzey 3 (Standartlaştırma):** Tek bir katalog, tek bir şablon, her standart için gerekçe ve örnekler ve iyi uygulama kontrol listeleri, takımlar arasında tutarlı uygulanır. Mekanik çoğunluk için otomatik uygulama. Adı konmuş onaylayıcılar, kaydedilmiş gerekçe ve süre sınırlı muafiyetlerle belgelenmiş bir istisna süreci.
- **Düzey 4 (Yönetme):** Standart sistemi temel çizgilere karşı ölçülür. Otomatik ve insan incelemesiyle uygulanan standartların payını, standart başına muafiyet hacmini, kapanma süresini ve kaç muafiyetin açıkken sona erdiğini izlersiniz ve bunları yönetişim işlevine raporlarsınız. Onay yetkisi riskle orantılıdır ve denetlenir; gözden geçirme ritmi ve son kullanma tarihi iyi niyet yerine kanıtla uygulanır; muafiyet oranı üzerinde anlaşılan bir eşiği geçen bir standart revizyon için işaretlenir.
- **Düzey 5 (Orkestrasyon):** Standartlar iş anında yüzeye çıkarılır ve kod olarak politika ve uygunluk fonksiyonlarıyla uygulanır. Muafiyetler sinyal olarak madenlenir; böylece tekrarlayan istisnalar standartların sürekli evrilmesini yönlendirir ve katalog uygulama kaydıkça yeniden dengelenir. Standartlar, kontrol listeleri ve muafiyetler uyum, teslimat ve denetim boyunca bütünleşmiş tek bir uyarlanabilir yaşayan sistemdir.

## Tartışma fikirleri

1. Standartlarınızdan hangilerini hem sınanabilir bir kuralla *hem de* net bir gerekçeyle ifade edebilirsiniz ve hangileri gerçekte yalnızca özlem?
2. Standartlarınızın hangi payı otomatik olarak, hangi payı bir incelemecinin fark etmesiyle uygulanıyor? On tanesini daha CI'ye taşımak için ne gerekir?
3. Sapmalar bugün nerede gerçekleşiyor ve bilir miydiniz? Kaydediliyor ve süre sınırlı mı, yoksa sessiz mi?
4. En çok emniyet ya da güvenlik açısından kritik standardınıza karşı muafiyet vermeye kim yetkili ve bu yetki riskle orantılı mı?
5. En çok muaf tutulan standardınıza bakın. Bu bir disiplin sorunu mu, yoksa standart basitçe yanlış mı?
6. Her etkin standart en son ne zaman gözden geçirildi ve sahibi kim? Hangileri sessizce folklora dönüştü?

## Önemli çıkarımlar

- Bir mühendislik standardı, **bir gerekçe, örnekler ve onu denetlemenin bir yoluyla bir sonuç olarak ifade edilmiş kuraldır**: denetlenemiyorsa henüz bir standart değildir.
- İnsanların kendi kendilerini doğrulayabilmesi için her standardı bir **iyi uygulama kontrol listesiyle** eşleştirin; kamu sektörü el kitabı kalıbını izleyin (NHS Wales / DHCW, UK GDS).
- Standartları **sürüm kontrolünde** saklayın, adı konmuş sahipler ve gözden geçirme tarihleriyle **yaşayan** tutun ve iş anında yüzeye çıkarın.
- **Denetlenebilir olanı** linter'lar, kod olarak politika ve uygunluk fonksiyonlarıyla otomatikleştirin; **insan incelemesini** muhakemeye saklayın.
- Sapmaları **belgelenmiş, süre sınırlı bir istisna/muafiyet süreciyle** yönetin: adı konmuş onaylayıcı, kaydedilmiş gerekçe, zorunlu son kullanma tarihi, periyodik gözden geçirme.
- Tekrarlayan bir istisna, yalnızca muafiyet vermeyi sürdürmenin değil, **standardı düzeltmenin sinyalidir**: "istisna kuralı doğrular." Bölüm 1.5'e (yönetişim), 1.6'ya (karar kayıtları), 2.1'e (kodlama standartları), 12.2'ye (kontrol listeleri) ve 12.3'e (şablonlar) bakın.

## Kaynaklar ve ileri okuma

- UK Government Digital Service, *Government Service Standard*, *Technology Code of Practice*, and *GOV.UK Service Manual*.
- NHS Digital / NHS England, *Service Standard* and engineering guidance.
- Digital Health and Care Wales (DHCW) / NHS Wales, published engineering standards and good-practice checklists.
- Scott Bradner, *RFC 2119: Key Words for Use in RFCs to Indicate Requirement Levels* (IETF, 1997).
- World Wide Web Consortium (W3C), *Web Content Accessibility Guidelines (WCAG) 2.2*.
- Neal Ford, Rebecca Parsons, and Patrick Kua, *Building Evolutionary Architectures* (fitness functions as automated governance).
- Torin Sandall et al., *Open Policy Agent* documentation (policy-as-code).
- GitLab, *The GitLab Handbook*: a public example of living, version-controlled organizational standards.
- Google, *Software Engineering at Google* (Winters, Manshreck, Wright): standards, readability, and automated enforcement at scale.
- Atul Gawande, *The Checklist Manifesto*: the case for checklists as professional practice.
