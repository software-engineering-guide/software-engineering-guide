# 2.7 Belgeleme

## Genel bakış ve motivasyon

[Belgeleme](https://en.wikipedia.org/wiki/Software_documentation), insanların anlayışı yalnızca koddan derlemek zorunda kalmadan yazılımı kullanmasını, işletmesini ve değiştirmesini sağlayan yazılı bilgidir. Birçok türde gelir: nasıl başlanır, bir görev nasıl yapılır, bir sistem nasıl yapılandırılmıştır, bir olaya nasıl yanıt verilir, bir [API](https://en.wikipedia.org/wiki/API) neyi kabul eder ve neyi döndürür. Her biri farklı bir ihtiyacı olan farklı bir okuyucuya hizmet eder. İyi belgeleme isteğe bağlı değildir. Büyük bir kuruluş genelinde ölçeklenen bilgi ile yalnızca birkaç kişinin kafasında yaşayan bilgi arasındaki farktır.

Büyük takımlar için belgeleme, kilit kişi riskine (kritik bilginin yalnızca bir ya da birkaç kişide olması tehlikesi) karşı en iyi savunmanız ve yeni gelenleri uyumlandırmanın en hızlı yoludur. Yüzlerce mühendis kendi inşa etmedikleri sistemlere bağımlı olduğunda ve insanlar sürekli katıldığında, taşındığında ve ayrıldığında, kuruluş yalnızca bilgi yazıldığında ve bulunması kolay olduğunda işleyebilir. Belgelenmemiş sistemler kırılgan hale gelir: onları yalnızca yazarları güvenle değiştirebilir ve o yazarlar ayrıldığında kuruluş kendi yazılımını sürdürme yeteneğini kaybeder. Bu, ölçekte en yaygın ve en pahalı başarısızlıklardan biridir.

Kurumsal ve kamu bağlamları bahsi daha da yükseltir. Sistemler uzun yaşar; bu yüzden belgelemeniz özgün takım gittikten yıllar, hatta on yıllar sonra bakımcılara hizmet etmelidir. Düzenleme ve denetim rejimleri çoğu zaman kontrolün kanıtı olarak belirli belgeleri zorunlu kılar: mimari kayıtlar, [işletim el kitapları](https://en.wikipedia.org/wiki/Runbook) (adım adım operasyonel ve olay müdahale prosedürleri) ve karar günlükleri. Satıcılar arasında devredilen kamu sistemleri, bilgiyi sözleşme sınırları boyunca taşımak için tamamen belgelemeye güvenir. Ve yine de belgeleme çürümeye ünlü biçimde yatkındır; bu yüzden asıl zorluk, yazılım değiştikçe onu doğru tutmaktır.

## Temel ilkeler

- Belirli bir ihtiyacı olan belirli bir okuyucu için yazın; farklı belgeleme türleri farklı amaçlara hizmet eder.
- Belgelemeyi koda yakın tutun ve kod gibi ele alın (kod olarak belgeler).
- Doğruluk eksiksizliği yener; az miktarda güvenilir belgeleme, çok miktarda yanlış olandan iyidir.
- Üretilebileni üretin; bir aracın doğruluk kaynağından üretebileceğini elle sürdürmeyin.
- Belgeleme çürümesiyle aktif savaşın; bayat belgeler yanılttığı için hiç olmamasından kötüdür.
- Belgelemeyi keşfedilebilir yapın; bulunamayan bilgi fiilen yoktur.
- Yalnızca mevcut durumu değil, kararları ve gerekçelerini kaydedin.

## Öneriler

### Kod olarak belgeleri benimseyin

Belgelemeyi, tarif ettiği kodun hemen yanında [sürüm kontrolünde](https://en.wikipedia.org/wiki/Version_control) tutun, düz metin işaretlemesiyle yazın ve aynı çekme isteği süreciyle inceleyin. Bu onu sürümlü, incelenebilir ve koda yakın tutar; böylece ikisini birlikte güncelleyebilirsiniz. En güncel sürüm her zaman erişilebilir olsun diye onu otomatik bir hat aracılığıyla yayımlayın. Belgeleri kod gibi ele almak, kodu güvenilir tutan aynı disiplini getirir: inceleme, geçmiş ve otomasyon.

### İçeriği Diátaxis çerçevesiyle yapılandırın

Belgelemeyi dört ayrı türe bölün, çünkü onları karıştırmak hiçbir okuyucuya iyi hizmet etmez: öğreticiler (öğrenme odaklı, yeni gelenler için), nasıl yapılır kılavuzları (görev odaklı, belirli bir hedef için), başvuru (bilgi odaklı, kesin ve eksiksiz) ve açıklama (anlama odaklı, nedeni ve bağlamı). Bunları ayrı tutun ve her şey yazması, gezinmesi ve sürdürmesi daha kolay hale gelir, çünkü her sayfanın tek net bir işi ve tek net bir hedef kitlesi vardır.

### Temel operasyonel belgeleri sürdürün

Her depoya ön kapısı olarak net bir [README](https://en.wikipedia.org/wiki/README) verin: ne olduğu, nasıl derlenip çalıştırılacağı ve nereye gidileceği. Nöbetteki herkes harekete geçebilsin, yalnızca uzmanlar değil, diye operasyonel görevler ve olay müdahalesi için işletim el kitapları yazın. Sistemin yapısını ve temel bileşenlerini açıklayan mimari belgeleme tutun. Ve yeni bir mühendisi hızla verimli kılan uyum belgeleri sağlayın. Bunlar, yokken en çok özlediğiniz belgelerdir.

### API belgelerini ve değişiklik günlüklerini doğruluk kaynağından üretin

API başvuru belgelerinizi makine tarafından okunabilir sözleşmeden ya da kod ek açıklamalarından üretin; böylece gerçek arayüzden sapamaz. İdeal olarak yapılandırılmış commit'lerden ya da sürüm notlarından üretilen bir [değişiklik günlüğü](https://en.wikipedia.org/wiki/Changelog) tutun; böylece tüketiciler sürümler arasında neyin değiştiğini görebilir. Bunları otomatikleştirmek, çürümeye en yatkın elle sürdürülen belgeleri omzunuzdan alır ve güvenilir tutar.

### Mimari kararları kaydedin

Önemli mimari ve tasarım kararlarını bağlamı, kararı ve sonuçlarını belirten hafif, tarihli kayıtlar olarak yakalayın. Bu karar kayıtları aksi halde kaybolacak gerekçeyi korur; böylece gelecekteki bakımcılar sistemin neden böyle olduğunu görebilir, onu sorgulamaz ya da eski hataları tekrarlamaz. Özellikle kurumsal ve kamu sistemlerinin uzun ömründe karşılığını verirler.

### Belgeleme çürümesiyle bilinçli savaşın

Bayat belgelemeyi kusur olarak ele alın. Belgeleri davranışı değiştiren aynı değişikliğin parçası olarak güncelleyin ve bunu bir inceleme beklentisi yapın. Her önemli belgenin sorumlu bir kişisi olması için sahiplik atayın. Yüksek değerli belgelemeyi zaman zaman doğruluk için gözden geçirin, eskiyeni budayın ve artık güvenmediğiniz her şeyi kaldırın ya da açıkça işaretleyin. En az çürüyen belgeleme yaşayan belgelemedir: sistemin kendisine karşı üretilmiş ya da test edilmiş.

### Bilgi yönetimine ve keşfedilebilirliğe yatırım yapın

İnsanlar birine sormak zorunda kalmadan ihtiyaç duyduklarını bulabilsin diye belgelemeyi iyi arama, net gezinme ve bilinen bir ev aracılığıyla bulunabilir yapın. Onun çok sayıda bağlantısız viki ve araç arasında parçalanmasına izin vermeyin. Ve sohbet dizilerinde ve insanların kafalarında yaşayan gayriresmi anlayış olan [örtük bilgiyi](https://en.wikipedia.org/wiki/Tacit_knowledge) kaybolmadan önce kalıcı, bulunabilir biçimde yakalayın.

## Ödünleşimler: artılar ve eksiler

| Yaklaşım | Artılar | Eksiler |
|---|---|---|
| Kod olarak belgeler | Sürümlü, incelenebilir, koda yakın; düşük çürüme | Mühendis disiplini gerektirir; teknik olmayan yazarlara daha az dostça |
| Viki / bilgi tabanı | Düzenlemesi kolay; herkese erişilebilir | Koddan sapar; parçalanır; sessizce çürür |
| Üretilmiş belgeler (API, değişiklik günlüğü) | Her zaman doğru; düşük bakım | Kaynağın ifade ettiğiyle sınırlı; araç gerektirir |
| Elle yazılmış açıklama | Makinelerin üretemediği zengin bağlam ve gerekçe | Emek yoğun; bayatlamaya yatkın |
| Diátaxis yapısı | Sayfa başına net amaç; gezinmesi ve sürdürmesi daha kolay | Baştan yapılandırma çabası; yazar disiplini gerektirir |

Merkezi ödünleşim çaba ile doğruluk ve dayanıklılık arasındadır. Yazması en ucuz belgeleme, hızlı bir viki sayfası, aynı zamanda çürümeye ve parçalanmaya en yatkın olandır. En dayanıklı belgeleme, kaynaktan üretilen ya da kod gibi incelenen, baştan daha fazla disipline mal olur ama güvenilir kalır. İyi bir pratik kural: üretebildiğinizi üretin, gerisini koda yakın tutun ve kod gibi inceleyin ve emek yoğun elle yazılmış açıklamayı yalnızca insanların sağlayabileceği gerekçeye saklayın.

## Takımınızla tartışılacak sorular

1. **Belgeleriniz okuyucu ihtiyacına göre ayrılmış mı, yoksa öğreticiler, başvuru ve açıklama tek bir sayfada mı karışıyor?** Bu bölüm öğreticilere, nasıl yapılır kılavuzlarına, başvuruya ve açıklamaya Diátaxis bölünmesini önerir ve türleri karıştırmayı hiçbir okuyucuya iyi hizmet etmeyen bir anti-kalıp olarak listeler. Ölçekte, sistemi öğrenen bir yeni gelen ile kesin bir bilgi arayan nöbetçi mühendisin farklı sayfalara ihtiyacı vardır ve tek karışık sayfa ikisini de yavaşlatır. Sinyali getirin: en çok ziyaret edilen belgelerinizi seçin ve her birinin tek net bir işi ve tek net bir hedef kitlesi olup olmadığını kontrol edin. En kötü örnekleri ayrı türlere yeniden yapılandırın; böylece her sayfa yazması, gezinmesi ve güncel tutması daha kolay olsun. Kuruluş büyüdükçe belgelemeyi sürdürülebilir kılan yapı budur.

2. **Önemli mimari kararları gerekçeleriyle mi yoksa yalnızca mevcut durumla mı yakalıyorsunuz?** Bölüm bağlamı, kararı ve sonuçları belirten hafif, tarihli karar kayıtlarını önerir ve özellikle kurumsal ve kamu sistemlerinin uzun ömründe karşılığını verdiklerini not eder. Onlar olmadan yıllar sonraki bir bakımcı sistemin neden böyle olduğunu göremez; bu yüzden sağlam seçimleri sorgular ya da eski hataları tekrarlar. Somut sinyal olarak, gerekçesi şimdi yalnızca bir sohbet dizisinde ya da birinin hafızasında yaşayan yakın tarihli zor bir kararı getirin. Kısa bir karar kaydı biçimi benimseyin ve bir tane yazmayı herhangi bir önemli tasarım değişikliğinin parçası yapın. Gerekçe tam olarak yalnızca insanların sağlayabileceği ve yazılmadığında en hızlı çürüyen bilgidir.

3. **Herhangi bir nöbetçi mühendis, sistemi inşa eden kişiyi çağırmadan yalnızca işletim el kitaplarınızdan bir olaya yanıt verebilir mi?** Bu bölüm işletim el kitaplarını, nöbetteki herkes harekete geçebilsin diye, yalnızca uzmanlar değil, temel bir operasyonel belge olarak adlandırır ve bilgiyi bir sözleşme sınırı boyunca taşıyan işletim el kitapları sayesinde bir sistemi miras alabilen bir kamu takımını tarif eder. Kilit kişi riski bunun karşı koruduğu başarısızlıktır: tek uzman ulaşılamaz ya da gittiğinde, belgelenmemiş bir kurtarma prosedürü rutin bir olayı kesintiye çevirir. Kanıtı getirin: yakın tarihli bir olay alın ve yalnızca işletim el kitabının onu çözüp çözmeyeceğini kontrol edin. İnsanların çekindiği prosedürler için işletim el kitapları yazın ve test edin ve tek başına ayakta duramayan bir işletim el kitabını kusur olarak ele alın. Bu, gece 2'deki bir kurtarma ile gece 2'deki bir yükseltme arasındaki farktır.

4. **API başvurularınızdan ve değişiklik günlüklerinizden hangileri doğruluk kaynağından üretiliyor ve hangileri hâlâ elle sürdürülüp sessizce sapıyor?** Bu bölüm başvuru belgelemesini makine tarafından okunabilir sözleşmeden ya da kod ek açıklamalarından üretmenizi söyler; böylece gerçek arayüzden ayrışamaz ve üretilebilir içeriği elle sürdürmeyi bir anti-kalıp olarak listeler. Büyük bir takım için gerçek arayüzün gerisinde kalan elle yazılmış bir API belgesi hiç olmamasından kötüdür: ona güvenen her tüketici bozuk bir entegrasyon yazar ve başarısızlık, onu doğuran bayat sayfadan çok uzakta ortaya çıkar. Somut sinyali getirin: en çok kullanılan birkaç arayüzünüzden örnek alın ve her birinin ne kadar saptığını görmek için yayımlanmış başvuruyu gerçek sözleşmeyle karşılaştırın. Sapma bulduğunuz yerde başvuruyu derlemeye bağlayın ki her değişiklikte yeniden üretilsin ve elle tutulan kopyayı emekliye ayırın. Arayüzlerin takımlar, satıcılar ve hiç görmediğiniz sözleşme sınırları arasında tüketildiği kurumsal ve kamu ortamlarında, yetkili üretilmiş bir başvuru çoğu zaman entegratörlerin kurguya karşı inşa etmesini engelleyen tek şeydir.

5. **Her yüksek değerli belgenin sahibi kim ve bugün biri bayatlasa nasıl fark ederdiniz?** Bölüm bayat belgelemeyi bir kusur olarak ele alır ve sahipsiz belgelerin, güncellemek kimsenin işi olmadığı için çürüdüğünü, güncel diye sunulan bayat belgelerin tüm belgelemenize güveni yok ettiğini uyarır. Ölçekte tehlike tek bir yanlış sayfa değil, güvenin yavaş aşınmasıdır: okuyucular eskimiş talimatlarla bir kez yandıklarında tüm külliyata güvenmeyi bırakır ve insanları bölmeye geri dönerler. En kritik belgelerinizin bir sahiplik haritasını ve çürümenin nasıl algılandığına, ister inceleme temposuyla, üretimle, sisteme karşı testlerle ya da saf şansla, dürüst bir cevap getirin. Önemli olan her belgeye adı konmuş bir sahip atayın ve bayatlığın utanmış bir okuyucu yerine mekanik olarak ortaya çıkması için üretilmiş ya da test edilmiş yaşayan belgelemeyi tercih edin. Özgün takımlarından uzun yaşayan kurumsal ve kamu sistemleri için, sahipsiz belgeleme bir denetçinin ya da devralan bir satıcının eninde sonunda size fatura keseceği bir yükümlülüktür.

6. **Belgelemeniz ne kadar keşfedilebilir ve kaç kritik bilgi hâlâ yalnızca sohbet dizilerinde ve insanların kafalarında yaşıyor?** Bu bölüm bulunamayan bilginin fiilen yok olduğunu söyler, belgelemeyi çok sayıda bağlantısız viki ve araç arasında parçalamaya karşı uyarır ve örtük bilgiyi kaybolmadan önce kalıcı, bulunabilir biçimde yakalamanızı ister. Büyük bir kuruluşta aynı olgu, kimse nerede yazıldığını bulamadığı için yüzlerce kez yeniden keşfedilir, yeniden sorulur ve yeniden cevaplanır ve her ayrılış yeri doldurulamaz bağlamı kapıdan dışarı götürür. Kanıtı getirin: kaç ayrı belgeleme evi sürdürdüğünüzü sayın, üç önemli olguyu yalnızca aramayla bulmaya çalışın ve gerçek cevapların nerede birinin hafızasında ya da gömülü bir mesajda yaşadığını not edin. Gerçek arama ve net gezinmeyle bilinen bir eve doğru birleştirin ve örtük bilgiyi yakalamayı kahramanca bir kurtarma yerine işin rutin bir parçası yapın. Sistemlerin sözleşmeyle satıcılar ve takımlar arasında geçtiği kamu sektörü ve yoğun dış kaynaklı bağlamlarda, devirden sağ çıkan tek şey keşfedilebilir yazılı bilgidir.

## Sektör merceği

**Girişim.** Bir avuç mühendis ve harcayacak pist olmadan, yalnızca gece 2'deki bir kesintinin ya da yeni bir işe alınanın gerçekten ihtiyaç duyacağı şeyi belgeleyin: hizmet başına gerçek bir README, herkesin çekindiği dağıt ve kurtar prosedürü için test edilmiş tek bir işletim el kitabı ve aksi halde unutacağınız kararlar üzerine birkaç tarihli not. API belgelerini sözleşmeden üretin ki onları asla elle sürdürmeyesiniz. Bir belgeleme platformu kurmaya direnin; gerçek acıyı hissedene kadar kodun yanında sürümlü bir işaretleme klasörü yeterlidir.

**Küçük işletme.** Teknik yazar ve sıkı bir bütçe olmadan, kadrolu bir program yerine araçlarınızın zaten ürettiği belgelemeye ve hafif kod olarak belgelere yaslanın. Seçimi satın alma ve inşa etme olarak çerçeveleyin: elle bakmanız gereken bir viki yerine kendi güncel başvurusunu ve aranabilir bilgi tabanını üreten platformları tercih edin. Kıt çabanızı yokluğu işi durduracak iki üç belgeye harcayın ve yanlış ya da eksik bir sayfanın sahipliği düzeltmenin tetikleyicisi olmasına izin verin.

**Kurumsal.** Birçok takım boyunca sorun tutarlılık ve keşfedilebilirliktir: paylaşılan bir kod olarak belgeler hattı, Diátaxis gibi ortak bir yapı, üretilmiş API başvuruları ve değişiklik günlükleri ve bilginin onlarca viki arasında parçalanmaması için her yerde aynı biçimde uygulanan karar kayıtları. Her yüksek değerli belge için sahiplik atayın ve yalnızca varlığı değil, doğruluğu ölçün. Mimari kayıtları, işletim el kitaplarını ve karar günlüklerini denetim kanıtı olarak ele alın ve bir kontrol incelemesinin telaş değil, belgelenmiş, savunulabilir bir iz bulması için nasıl üretildiklerini standartlaştırın.

**Kamu.** Tedarik kuralları ve kamusal hesap verebilirlik belgelemeyi bir nezaket değil, bir teslimat yapar. Bilgi bir satıcı geçişinden sağ çıksın ve sistemi miras alan herkes işletebilsin diye mimari belgelemeyi, işletim el kitaplarını ve karar kayıtlarını zorunlu yapıtlar olarak sözleşmelere yazın ve doğruluk için inceleyin. Yetkili herhangi bir operatörün bir olaya yalnızca işletim el kitabından yanıt verebilmesini isteyin ve seçimlerin neden yapıldığının şeffaf bir kamusal kaydı olarak karar günlüklerini tutun. Burada ince belgeleme özel bir rahatsızlık değildir; vergi mükellefinin finanse ettiği maliyetli tersine mühendisliğe dönüşür.

## Örnekler

**Girişim.** Beş kişilik bir girişim her hizmet için gerçek bir README ve herkesin çekindiği tek dağıt ve kurtar prosedürü için kısa bir işletim el kitabı yazar; böylece gece 2'deki bir kesinti sistemi bilen tek kurucuyu uyandırmaya bağlı kalmaz. API belgelerini elle yazmak yerine sözleşmeden üretirler ve veritabanlarını ve kimlik doğrulama yaklaşımlarını neden seçtiklerini açıklayan birkaç tarihli not yazarlar. Hafif kalır, ama altıncı ve yedinci işe alınanların herkesi bölmek yerine belgelerden uyum sağlaması anlamına gelir.

**Kurumsal.** Büyük bir yazılım şirketi tüm belgelemesini kodla aynı depolarda tutar; işaretlemeyle yazılır ve tarif ettikleri değişikliklerin hemen yanında çekme isteklerinde incelenir. API başvuruları hizmet sözleşmelerinden üretilir; bu yüzden asla sapmazlar. Değişiklik günlükleri yapılandırılmış commit'lerden üretilir ve mimari karar kayıtları büyük seçimlerin ardındaki akıl yürütmeyi korur. Yayımlanmış bir belgeleme sitesi her birleştirmede otomatik derlenir. Yeni mühendisler hızla verimli olur çünkü uyum kılavuzları ve işletim el kitapları güncel ve bulunabilirdir ve nöbetçi mühendisler özgün yazarları çağırmak yerine işletim el kitaplarına yaslanır.

**Kamu.** Ulusal bir kurum, ayrılan bir yüklenicinin sistemini miras alır ve bilgiyi sözleşme sınırı boyunca taşımak için tamamen belgelemeye bağımlıdır. Önceki satıcı mimari belgelemeyi, işletim el kitaplarını ve karar kayıtlarını zorunlu teslimatlar olarak sürdürdüğü için, yeni takım özgün yazarlar olmadan sistemi işletebilir ve değiştirebilir. Belgelemenin ince olduğu yerde kurum maliyetli tersine mühendislikle karşılaşır. Bu deneyim yeni bir politikayı yönlendirir: belgeleme sözleşmesel bir teslimattır, sonradan düşünce olarak değil doğruluk için incelenir ve işletim el kitapları yetkili herhangi bir operatörün olaylara yanıt vermesine izin vermelidir.

## İş gerekçesi: motivasyonlar, YG ve TSM

Belgeleme size daha kısa uyum süresi, daha az kilit kişi riski, daha hızlı olay müdahalesi ve bir sistemin ömrü boyunca daha düşük değişim maliyetiyle geri öder. Yeni mühendislerin haftalar yerine günlerde verimliliğe ulaşması, nöbetçi personelin yükseltmek yerine bir işletim el kitabından olayları çözmesi, bakımcıların bir sistemi inşa edildikten yıllar sonra güvenle değiştirmesi: bunlar büyük bir kuruluş ve uzun bir sistem ömrü boyunca bileşik hale gelen büyük, yinelenen tasarruflardır.

Belgelemenin maliyeti nedir? Yazma ve bakım çabası. Belgelememenin maliyeti nedir? Sürekli ödersiniz: yavaş uyumda, tekrarlanan sorularda, kilit kişi darboğazlarında, daha yavaş olay kurtarmada ve uç noktada kimsenin güvenle değiştiremediği sistemlerde; bu da pahalı yeniden yazmaları ya da tersine mühendisliği zorlar. Satıcı geçişi ve denetim senaryolarında eksik belgeleme doğrudan sözleşmesel ve uyum maliyetleri taşıyabilir. Gerekçeyi liderliğe sunmak için uyum süresine, olay müdahale süresine ve kaç kritik bilginin bireysel kafalarda durduğuna sayı koyun. Sonra kod olarak belgeleri ve üretimi, eşleşen bir bakım yükü olmadan kalıcı belgeleme elde etmenin yolları olarak çerçeveleyin. Ve yanlış belgelemenin bir yükümlülük olduğunu vurgulayın; bu yüzden yatırım onu güncel tutmayı içermelidir.

## Anti-kalıplar ve tuzaklar

- **Güncel diye sunulan bayat belgeleme:** okuyucuları yanıltır ve tüm belgelemeye güveni yok eder.
- **Bir kez yazılan viki:** oluşturulup hiç güncellenmeyen, sessizce gerçeklikten sapan sayfalar.
- **Belgeleme parçalanması:** hiçbir şeyin bulunamaması için birçok araç ve viki arasına dağılmış bilgi.
- **Belgeleme türlerini karıştırmak:** öğreticiler, başvuru ve açıklamanın tek sayfada karışması; hiçbir okuyucuya hizmet etmez.
- **Üretilebilir içeriği elle sürdürmek:** kaçınılmaz olarak gerçek arayüzden ayrışan elle yazılmış API belgeleri.
- **Kabile bilgisi:** yalnızca insanların kafalarında ve sohbet geçmişinde tutulan kritik anlayış; ayrıldıklarında kaybolur.
- **Sonradan düşünce olarak belgeleme:** değişikliğin yanında değil, hiç yazılıyorsa sonunda yazılır.
- **Sahiplik yok:** sorumlu sahibi olmayan belgeler, güncellemek kimsenin işi olmadığı için çürür.

## Olgunluk modeli

- **Düzey 1, Başlangıç.** Belgeleme seyrek, dağınık ve bayattır ve bilgi insanların kafasında yaşar. Var olan, bir kez yazılmış ve bir daha dokunulmamıştır; bu yüzden bir kesinti ya da bir ayrılış sistemi tersine mühendislikle çözmek demektir.
- **Düzey 2, Geliştirme.** README'ler ve birkaç işletim el kitabı gibi kilit belgeler vardır, ama tutarsız sürdürülür ve bulunması zordur. Bazı takımlar iyi belgelerken diğerleri neredeyse hiç belgelemez ve bir deponun neyi taşıması ya da nerede yaşaması gerektiğine dair paylaşılan beklenti yoktur.
- **Düzey 3, Standartlaştırma.** Kod olarak belgeler kuruluş genelinde normdur: Diátaxis gibi ortak bir yapı, üretilmiş API başvuruları ve değişiklik günlükleri, karar kayıtları ve incelemede belgelerin tarif ettikleri kodla birlikte değişmesi beklentisi. Her yüksek değerli belgenin adı konmuş bir sahibi ve gerçek aramalı tek bir bilinen evi vardır.
- **Düzey 4, Yönetme.** Belgeleme yalnızca mevcut değil, ölçülür. Temel belgelerin kapsamını, belge değişim oranını kod değişim oranına karşı, uyum süresini, yalnızca işletim el kitaplarından olay çözümünü ve tanımlı bir bayatlık eşiğine karşı tazeliği izlersiniz ve bu metrikleri temel çizgilere karşı gözden geçirirsiniz. Çürüme üretim, sisteme karşı testler ve bağlantı ve doğruluk kontrolleriyle mekanik olarak yakalanır ve bayat sayfalar şansla değil kanıtla işaretlenir ya da budanır.
- **Düzey 5, Orkestrasyon.** Belgeleme sürekli iyileştirilir ve kuruluş genelinde bütünleşir: yaşayan, büyük ölçüde üretilmiş ya da sisteme karşı test edilmiş, sahipli, keşfedilebilir ve uyarlanabilir. Metrikler nereye yatırım yapılacağını besler, örtük bilgi yakalama işin rutin parçası olarak gerçekleşir ve külliyat sistemler, takımlar ve okuyucular değiştikçe aktif yeniden dengelenir ve budanır.

## Tartışma fikirleri

- Yarın kaybolsa kuruluşunuza en çok zarar verecek belgeleme hangisi ve şu anda var mı ve güncel kalıyor mu?
- Belgeleri güncellemeyi ayrı bir angarya değil, kodu değiştirmenin doğal bir parçası nasıl yaparsınız?
- Elle yazılmış belgelemeyi doğruluk kaynağına bağlı üretilmiş belgelemeyle nerede değiştirebilirsiniz?
- Belgelemenizin yalnızca mevcut değil, doğru ve kullanılmış olduğunu nasıl ölçersiniz?
- Yapay zeka asistanları belgeleri nasıl yazdığınızı, sürdürdüğünüzü ve aradığınızı nasıl değiştirmeli ve inandırıcı ama yanlış içeriği nerede getirebilirler?
- Örtük bilgiyi tutan insanlar ayrılmadan önce nasıl yakalarsınız?

## Önemli çıkarımlar

- Belgelemeyi kod gibi ele alın: sürümlü, incelenmiş, kaynağa yakın ve otomatik yayımlanan.
- İçeriği okuyucu ihtiyacına göre öğreticiler, nasıl yapılır kılavuzları, başvuru ve açıklama olarak yapılandırın.
- Yüksek değerli temelleri sürdürün: README'ler, işletim el kitapları, mimari belgeler, uyum ve karar kayıtları.
- API belgelerini ve değişiklik günlüklerini doğruluk kaynağından sapamayacak şekilde üretin.
- Çürümeyle sahiplik, inceleme beklentileri ve budamayla savaşın; yanlış belgeleme hiç olmamasından kötüdür.

## Kaynaklar ve ileri okuma

- Daniele Procida, *Diátaxis* documentation framework
- Andrew Etter, *Modern Technical Writing*
- Anne Gentle, *Docs Like Code*
- Google, *Developer Documentation Style Guide* and Season of Docs guidance (as reference exemplars)
- Michael Nygard, *Documenting Architecture Decisions* (architecture decision records)
- Andrew Hunt and David Thomas, *The Pragmatic Programmer* (on knowledge and documentation)
- *Keep a Changelog* (as a reference convention)
