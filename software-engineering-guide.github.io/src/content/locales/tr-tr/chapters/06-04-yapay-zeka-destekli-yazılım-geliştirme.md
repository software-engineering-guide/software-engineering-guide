# 6.4 Yapay zeka destekli yazılım geliştirme

## Genel bakış ve motivasyon

Yapay zeka kodlama asistanları artık kod üretebiliyor, işlevleri tamamlayabiliyor, test yazabiliyor, tanımadığınız sistemleri açıklayabiliyor ve [yeniden düzenleme](https://en.wikipedia.org/wiki/Code_refactoring) yapmanıza yardım edebiliyor. İyi kullanıldığında rutin işi hızlandırırlar. Tanımadığınız dillere ve çerçevelere girişin önündeki engeli düşürürler. Basmakalıp kodun angaryasını ortadan kaldırırlar.

Kötü kullanıldığında gerçek zarar verirler. Bir kod tabanını makul görünen ama ince biçimde yanlış kodla doldurabilirler. Güvenlik açıkları ekleyebilir, lisans riski yaratabilir ve onlara yaslanan mühendislerin becerilerini aşındırabilirler. Yapay zeka destekli geliştirme aynı anda hem gerçek bir üretkenlik aracı hem de gerçek bir risktir. Aradaki fark neredeyse tamamen çevresindeki mühendislik disiplininden gelir.

Büyük takımlar için asıl zorluk, ölçekte tutarlılık ve güvenliktir. Yüzlerce geliştirici yapay zeka asistanı kullandığında, küçük bireysel alışkanlıklar toplanıp kurumsal sonuçlara dönüşür. Herkes önerileri eleştirmeden kabul ederse inceleme yükü ve kusur oranları artar. Net normlar, iyi varsayılanlar ve güçlü doğrulama sağlarsanız, aynı araçlar kaliteyi düşürmeden verimi yükseltir. Üretkenlik hikâyesi de satıcıların iddia ettiğinden daha nüanslıdır. Gerçek kazanımlar göreve göre çok değişir ve kabul edilen önerileri saymak gibi saf ölçümler sizi yanıltır.

Kurumsal ve kamu ortamları daha keskin kısıtlar getirir. Düzenlemeye tabi sistemlere dokunan, hassas veri işleyen ya da kritik altyapı çalıştıran koda, bir yapay zeka ürettiği için güvenilemez. Üretilen kod, kısıtlayıcı lisanslar altındaki eğitim verisini yankılayabiliyorsa lisans kaynağı önem kazanır. Bazı kurumlar kaynak kodunu şirket içinde tutmak zorundadır ve onu hiçbir dış hizmete gönderemez. Yapay zeka desteği için net, uygulanabilir normlar koymak artık sorumlu mühendislik liderliğinin parçasıdır. Mevcut asistanlar arasında Anthropic'in Claude modelleri üzerine kurulu araçlar, diğerlerinin yanında önde gelen seçeneklerden biridir; aşağıdaki uygulamalar hangisini benimserseniz benimseyin geçerlidir.

*Ayrıca bakın:* bölüm 2.5 (kod inceleme ve iş birliği), bölüm 2.4 (test stratejisi) ve bölüm 6.5 (sorumlu ve güvenilir yapay zeka).

## Temel ilkeler

- Commit edilen her satırdan asistan değil, mühendis sorumludur.
- Yapay zekanın ürettiği kod, incelenip doğrulanması gereken bir taslaktır; asla güvenilecek bitmiş bir ürün değildir.
- Doğrulama çabası, çıktının ne kadar kendinden emin göründüğüne değil, kodun riskine göre ölçeklenmelidir.
- Üretkenliği öneri sayılarıyla değil, önemli sonuçlarla (teslim edilen değer, kalite, çevrim süresi) ölçün.
- Üretilen kodla gelen güvenlik ve lisans risklerine karşı korunun.
- İnsan mühendislik becerisini koruyun ve geliştirin; asistanların onu içten boşaltmasına izin vermeyin.
- Yapay zeka desteğinin nerede ve nasıl kullanıldığı konusunda şeffaf olun.

## Öneriler

### Yapay zeka eşli programlamayı taslak çıkarma ve keşif aracı olarak kullanın

Asistanları, parladıkları ve hataların yakalanmasının ucuz olduğu işlere yönlendirin: basmakalıp kod, test iskeleleri, biçim dönüşümleri, tanımadığınız kodu açıklama ve yaklaşımları keşfetme. Çıktılarını ilk taslak sayın. Direksiyonda kalın. Her öneriyi otomatik pilotla kabul etmek yerine okuyun, anlayın ve düzenleyin. Tanımadığınız alanlarda asistanı öğrenmek için kullanın, ama iddialarını yetkili belgelerle karşılaştırın. Asistanlar API uydurabilir ve davranışı büyük bir özgüvenle yanlış aktarabilir.

### Yapay zekanın ürettiği kodu güvenilmeyen girdi olarak inceleyin, test edin ve doğrulayın

Yapay zekanın ürettiği koda, yeni bir takım üyesinden gelen koda göstereceğiniz özeni, hatta daha fazlasını gösterin. İnceleyen kişi onu açıklayıp sürdürebilecek kadar iyi anlamalıdır. "Yapay zeka yazdı" hiçbir zaman "bu neden çalışıyor?" sorusuna kabul edilebilir bir cevap değildir. Testlerde ısrar edin ve amaçlanan davranışı değil de yalnızca mevcut davranışı doğrulayan yapay zeka testlerine dikkat edin. [Statik analiz](https://en.wikipedia.org/wiki/Static_program_analysis), güvenlik taraması ve bağımlılık denetimleri çalıştırın. Yüksek riskli kod için (kimlik doğrulama, [kriptografi](https://en.wikipedia.org/wiki/Cryptography), finansal mantık, güvenlik sistemleri) yapay zeka çıktısını uzman insan doğrulaması gerektiren bir başlangıç noktası sayın, asla yetkili kabul etmeyin.

### Üretkenliği dürüstçe ölçün ve gerçekçi beklentiler koyun

Kabul oranı ya da üretilen satır sayısı gibi gösteriş metriklerini bırakın. Bunun yerine zaman içindeki teslimat ve kalite sinyallerine bakın: çevrim süresi, değişiklik başarısızlık oranı, kusur kaçış oranı ve geliştiricilerin bildirdiği etkililik. Kazanımlar gerçektir ama eşitsizdir: bazı görevlerde büyük, bazılarında önemsiz ya da olumsuz. Kod yazarken kazanılan zaman, onu incelerken ve hata ayıklarken yeniden kaybedilebilir. Yatırımın abartıya değil kanıta dayanması ve takımların bir metriği tutturmak için güvensiz önerileri kabul etmeye zorlanmaması için, beklentileri liderlikle buna göre belirleyin.

### Güvenlik ve lisans risklerini yönetin

Üretilen kodu açıklar ve güvensiz kalıplar için tarayın. Asistanlar güvensiz deyimleri eğitim verilerinden yeniden üretebilir. Gizli bilgileri, kimlik bilgilerini ya da hassas verileri asla dış hizmetlere giden istemlere yapıştırmayın. Veri işleme gereksinimlerinize uyan araçları tercih edin; kaynak kodun ortamdan çıkamadığı yerlerde şirket içi ya da özel dağıtım dahil. Lisanslamayı da ele alın. Üretilen kod lisanslı eğitim verisine benzeyebilir; bu yüzden bu riski azaltan araçlar ve politikalar kullanın, mümkün olduğunda kaynak izini tutun ve şüpheli her şeyi hukuki incelemeye yönlendirin. Asistanın önerdiği bağımlılıkların kaynağını izleyin; terk edilmiş ya da kötü amaçlı paketler önerebilir.

### Takım normlarını, açıklamayı ve beceri korumayı belirleyin

Yapay zeka desteğinin ne zaman ve nasıl kullanılabileceği, hangi verilerin asla paylaşılamayacağı ve her risk düzeyinin hangi doğrulamayı gerektirdiği konusunda net rehberlik yayımlayın. İnceleme ve hesap verebilirlik açısından önemli olduğu yerlerde yapay zeka destekli katkılar konusunda şeffaflığı teşvik edin. İnsan becerilerini bilerek keskin tutun. Mühendislerin, özellikle kıdemsizlerin, anlamayı dışarıya devretmek yerine temelleri öğrenmeye devam ettiğinden emin olun. İnsanları derin uzmanlık oluşturan işlerde dönüşümlü çalıştırın ve aşırı bağımlılığı takımın yetkinliği için gerçek bir uzun vadeli risk olarak görün.

## Ödünleşimler: artılar ve eksiler

| Boyut | Yapay zeka desteğinin faydası | Yapay zeka desteğinin riski |
|---|---|---|
| Hız | Daha hızlı basmakalıp kod ve taslak | Yanlış kodu incelerken kaybedilen zaman |
| Ekibe katılım | Yeni dillere/çerçevelere daha kolay giriş | Yüzeysel anlayış, uydurma API'ler |
| Kalite | Daha fazla test, daha hızlı yeniden düzenleme | Makul ama ince biçimde yanlış kod |
| Güvenlik | Düzeltme ve tarama önerebilir | Güvenlik açıkları ekleyebilir |
| Beceriler | Daha yüksek değerli işe zaman açar | Aşırı kullanılırsa temelleri aşındırır |
| Lisanslama | Yaygın kalıpların daha hızlı yeniden kullanımı | Kaynak izi ve lisans riski |

Merkezi ödünleşim hız ile doğrulama arasındadır. Yapay zeka çabayı yazmaktan incelemeye kaydırır. Net kazanç, inceleme ve doğrulama uygulamalarınızın asistanın yanlış yaptığını yakalayacak kadar güçlü olup olmadığına bağlıdır. Zayıf inceleme kalite düşüşüne yol açar. Güçlü inceleme ve net normlar kazancı yakalar.

## Takımınızla tartışılacak sorular

1. **Kod tabanımızın hangi bölümleri yapay zeka desteğine tamamen kapalı ve bu sınırı nasıl uygulatıyoruz?** Tekdüze güven bir tuzaktır: kimlik doğrulama, kriptografi, finansal mantık ve güvenlik sistemlerine, basmakalıp koda uyguladığınız aynı hafif incelemeyi uygulamak, ince ve kendinden emin hataların kritik yollara ulaşmasının yoludur. Büyük bir takım için, dışlanmış ya da yalnızca uzman incelemesine açık modüllerin açık bir listesi bireysel yargıyı kurumsal bir güvenceye dönüştürür. Kod tabanınızın risk haritasını, varsa mevcut politikanızı ve üretilen kodun kısıtlı bir modüle inmesini gerçekte nasıl durduracağınızı getirin: işlem hattı denetimleri, sahiplik kuralları ya da inceleme kapıları. Savunma, düzenlemeye tabi ve güvenlik açısından kritik ortamlarda bazı modüller yapay zeka desteğini tümüyle dışarıda bırakmalıdır. Cevap, doğrulama çabasını çıktının ne kadar kendinden emin göründüğüne değil, kodun riskine göre ölçeklemelidir.

2. **Asistanları benimsediğimizden beri gerçek değişiklik başarısızlık ve kusur kaçış eğilimlerimiz neler; bunları ölçüyor muyuz yoksa tahmin mi ediyoruz?** Satıcıların üretkenlik iddiaları ve kabul oranı sayıları yanıltıcı gösteriş metrikleridir, çünkü kod yazarken kazanılan zaman incelerken ve hata ayıklarken yeniden kaybedilebilir. Liderliğin abartıya değil kanıta yatırım yapabilmesi için zaman içinde teslimat ve kalite sinyallerine ihtiyacınız var: çevrim süresi, değişiklik başarısızlık oranı, kusur kaçış oranı ve geliştiricilerin bildirdiği etkililik. Elinizdeki gerçek sayıları getirin ve hiç olmadığı yerde dürüst olun. İzlenecek risk, takımların bir metriği tutturmak için güvensiz önerileri kabul etmeye zorlanmasıdır. Cevap, öneri sayılarının yerine sonuç ölçülerini koymalı ve kazanımların gerçek ama eşitsiz olduğu, bazı görevlerde büyük, bazılarında olumsuz olduğu beklentisini belirlemelidir.

3. **Üretilen kod kısıtlayıcı lisanslı eğitim verisini yankılarsa ya da riskli bir bağımlılık getirirse, bunu kim ve ne zaman yakalar?** Üretilen kod lisanslı materyale benzeyebilir ya da terk edilmiş veya kötü amaçlı paketler önerebilir ve bu risk, kimse fark etse de etmese de ürününüze iner. Kurumlar ve kamu için lisans kaynağı ve tedarik zinciri riski, "yapay zeka yazdı" omuz silkmesinin kaldıramayacağı bir hukuki ağırlık taşır. Mevcut gizli bilgi taramanızı, lisans denetimlerinizi ve bağımlılık kaynak izleme yönteminizi getirin ve her birinin işlem hattında nerede çalıştığını belirleyin. Şüpheli kodu neyin hukuki incelemeye yönlendirdiğini ve bu kararın kimde olduğunu tartışın. Gizli bilgiler dış araçlara yapıştırılabiliyorsa ya da incelenmemiş paketler itiraz edilmeden birleştirilebiliyorsa, asistan kullanımını takım genelinde ölçeklemeden önce bu boşlukları kapatın.

4. **Mühendislerin, özellikle kıdemsizlerin, anlamayı asistana dışarıdan yaptırmak yerine temelleri öğrenmeye devam etmesini nasıl sağlıyoruz?** Beceri aşınması, bu çeyreğin hızında hiç görünmeyen yavaş bir risktir; yıllar sonra bir istem olmadan hata ayıklayamayan, tasarlayamayan ya da inceleyemeyen bir takım olarak ortaya çıkar. Büyük bir kurum için karşıt çekim gerçektir: asistanlar kıdemsiz mühendislerin bugün daha hızlı ürün çıkarmasını sağlar ve teslimat hedeflerini tutturma baskısı, derin uzmanlık kurmanın daha yavaş işiyle çekişir. İnsanlarınızın gerçekte nasıl geliştiğine dair kanıt getirin: kıdemsizlerin ne kadarı birleştirdiği kodu açıklayabiliyor, ekibe katılım süreciniz hâlâ ne kadar yardımsız problem çözme gerektiriyor ve incelemeler yüzeysel anlayışı mı yakalıyor yoksa çalışan çıktıyı mı onaylıyor. İnsanları ustalık kuran işlerde bilerek dönüşümlü çalıştırın ve aşırı bağımlılığı kişisel bir kusur değil, bir yetkinlik riski olarak görün. Kamuda ve uzun ömürlü kritik sistemlerde iş gücünün sistemleri onlarca yıl satıcı araçları olmadan inşa edip doğrulaması gerekebilir; bu yüzden temel bilgileri doğrudan garantileyen bir eğitim yolu bir incelik değil, süreklilik gereksinimidir.

5. **Kaynak kodumuzun ve verimizin nerede kalması gerektiği düşünüldüğünde hangi asistanları kullanmamıza gerçekten izin var ve bir gizli bilginin bir istemin içine girmesini nasıl önleriz?** Veri işleme kısıtlamaları, üretkenlikten önce aracı belirler: kaynağınızı dış bir hizmete akıtan bir asistan, yetenekleri ne olursa olsun tümüyle elenebilir. Büyük bir takım için gerilim, en iyi barındırılan aracın rahatlığı ile tescilli kodun, kimlik bilgilerinin ve hassas verinin sınırınızı asla terk etmemesi gereksinimi arasındadır. Veri sınıflandırma haritanızı, her aday aracın sunduğu dağıtım seçeneklerini (barındırılan, özel, şirket içi) ve gizli bilgileri istemlerden uzak tutan somut denetimleri getirin: commit öncesi tarama, istem filtreleme ve mühendis eğitimi. Hangi araçların hangi kod sınıfları için izinli olduğuna karar verin ve sınırı salt tavsiye değil uygulanabilir yapın. Düzenlemeye tabi, savunma ve gizli ortamlarda şirket içi ya da hava boşluklu bir dağıtım tek yasal seçenek olabilir; kaynağı herhangi bir dış hizmete göndermek yalnızca caydırılmamalı, yasaklanmalı ve teknik olarak engellenmelidir.

6. **Dağınık bireysel alışkanlıkları tutarlı kurum çapında normlara nasıl dönüştürürüz ve araçlar evrildikçe politikanın sahibi kim olur?** Yüzlerce geliştirici kendi yaklaşımını doğaçlama yaptığında, küçük alışkanlıklar birikip kurumsal sonuçlara dönüşür ve tutarsız doğrulama kusurların ve riskin sızdığı yerdir. Karşıt husus özerkliktir: takımlar ağır merkezi dayatmalardan hoşlanmaz, ama başıboşluk eşitsiz kalite ve ortak bir güvence yokluğu üretir. Mevcut rehberliğinizi (varsa), ne kadar tekdüze izlendiğine dair kanıtı ve güvenli yolun kolay yol olması için işlem hattına yerleştirilmiş iyi varsayılanlar önerisini getirin. Asistanlar birkaç ayda bir değişirken politikayı güncel tutacak bir sahip ve gözden geçirenlerin yapay zeka desteğinin bir katkıyı ne zaman şekillendirdiğini bilmesi için bir açıklama normu belirleyin. Bir kurum ya da kamu kuruluşu için normları denetim ve hesap verebilirliğe bağlayın: bir denetçinin inceleyebileceği belgelenmiş, uygulanan bir standart, takımdan takıma değişen ve kilit bir kişi ayrılınca kaybolan bir halk pratiğinden iyidir.

## Sektör merceği

**Girişim.** Bir avuç mühendisle ve boşa harcayacak pisti olmadan, basmakalıp kod, testler ve tanımadığınız çerçeveler için barındırılan asistanlara yaslanın ve rutin işi hızlandırmalarına izin verin. Tek pazarlık edilemez kural koyun: değişikliği anlayan bir insan her birleştirmeyi incelesin, çünkü beş kişilik bir kod tabanında ince bir yanlış satırın saklanacak yeri ve onu yakalayacak başka kimsesi yoktur. Erken bir gizli bilgi tarayıcısı ve bir lisans denetimi ekleyin; ucuzdurlar ve sonradan temizlemeyi göze alamayacağınız pahalı hataları önlerler.

**Küçük işletme.** Muhtemelen güvenlik uzmanınız yok ve bütçeniz kısıtlı; bu yüzden bakımını yapmanız gereken özel bir kurulum yerine zaten güvendiğiniz araçlara gömülü asistanları tercih edin. Riski sade terimlerle çerçeveleyin: müşteri verisini ya da kimlik bilgilerini asla dış bir isteme yapıştırmayın ve faturalamaya ya da kimlik doğrulamaya dokunan üretilmiş kodu bitmiş bir cevap değil, doğrulanacak bir taslak sayın. Veri işleme koşullarını gerçekten okuyabileceğiniz ve yapay zeka özelliklerini kötü davrandıklarında kapatabileceğiniz satıcıları seçin.

**Kurumsal.** Sorun birçok takım arasında tutarlılık ve güvenliktir: risk düzeyine göre ortak normlar, işlem hattında zorunlu inceleme ve tarama ve kabul sayıları yerine dürüst teslimat ve kalite metrikleri. Tescilli kod sınırınızın içinde kalsın diye araç seçimlerini ve dağıtım modelini standartlaştırın, asistanların inceleyenlere kaydırdığı inceleme ve düzeltme maliyetini bütçeleyin ve yüksek riskli modülleri açıkça hariç tutun ya da kapıyla koruyun. Yapay zeka desteğini bireysel alışkanlıkların dağınıklığı olarak değil, bir sahibi olan yönetilen bir yetenek olarak yönetin.

**Kamu.** Tedarik kuralları, şeffaflık ve kamusal hesap verebilirlik her seçimi şekillendirir. Kaynak kodun ve hassas verinin ortamdan çıkamadığı yerlerde şirket içi ya da özel dağıtımı tercih edin, kodun dış hizmetlere gönderilmesini yasaklayın ve kararlar denetlenebilir kalsın diye yapay zeka destekli katkıların açıklanmasını isteyin. Üretilen tüm kodda güvenlik ve lisans taramalarını zorunlu kılın, güvenlik açısından kritik ve gizli modülleri yapay zeka desteğinin dışında tutun ve kamu iş gücünün sahip olduğu sistemlerin uzun ömrü boyunca bunları satıcı araçları olmadan inşa edip doğrulayabilmesini sağlayan bir eğitim yolu sürdürün.

## Örnekler

**Girişim.** Altı mühendislik bir SaaS girişimi, rutin işte daha hızlı ilerlemek için yapay zeka kodlama asistanlarını benimsedi. Basmakalıp kod, testler ve tanımadığı çerçeve kodu için onlara yaslandı, ama değişikliği anlayan bir insanın her çekme isteğini incelemesi gerektiği yönünde kesin bir kural koydu ve işlem hattına bir gizli bilgi tarayıcısı ile bir lisans denetimi ekledi. Faturalama ve kimlik doğrulama kodunda mühendisler yapay zeka çıktısına güvenmek yerine onu satır satır doğrulanacak kaba bir taslak olarak ele aldı. Kabul edilen önerileri saymak yerine çevrim süresini ve kaçan kusurları izlediler ve kaliteyi düşürmeden kazanımları korudular.

**Kurumsal.** Büyük bir e-ticaret şirketi yapay zeka kodlama asistanlarını güvenlik bariyerleriyle devreye aldı. İstemlerde gizli bilgileri yasakladı. İnsan incelemesini zorunlu kıldı ve inceleyenin kodu anlamasını bekledi. İşlem hattına güvenlik taraması ekledi ve tescilli kod ortamından asla çıkmasın diye özel bir dağıtım seçti. Etkiyi kabul sayıları yerine çevrim süresi ve değişiklik başarısızlık oranıyla ölçtü. Basmakalıp kod ve testlerde sağlam kazanımlar buldu, ama yapay zeka çıktısını güvenilmez saydığı ödeme kodu için uzman incelemesinde ısrar etti.

**Kamu.** Bir savunma yazılımı kuruluşu, yapay zeka desteğine yalnızca gizli ve hassas kodu sınırı içinde tutan şirket içi bir araçla izin verdi. Kaynağın herhangi bir dış hizmete gönderilmesini yasakladı. Kod incelemesinde yapay zeka destekli katkıların açıklanmasını istedi ve üretilen tüm kodda güvenlik ve lisans taramalarını zorunlu kıldı. Bazı güvenlik açısından kritik modülleri yapay zeka desteğinin tümüyle dışında tuttu. Kıdemsiz mühendisler temelleri doğrudan öğrenmelerini sağlayan bir eğitim yolu izledi; böylece iş gücü sistemleri yardımsız inşa edip doğrulama yeteneğini kaybetmeyecekti.

## İş gerekçesi: motivasyonlar, YG ve TSM

Motivasyon daha hızlı teslimat ve daha az angaryadır; böylece kıt mühendislik yeteneğiniz tasarıma, yargıya ve zor problemlere odaklanabilir. YG, uygun görevlerde azalan çevrim süresi ve gelişen geliştirici deneyimi olarak görünür, ama yalnızca doğrulamanın kaliteyi yüksek tuttuğu yerlerde. Öneri sayılarına dayanan saf YG iddiaları yanıltıcıdır ve onları reddetmelisiniz.

TSM; araç lisanslarını, güvenli ya da şirket içi dağıtımı, güvenlik ve lisans taramasını ve yapay zeka çıktısını incelemenin ve düzeltmenin çoğu zaman hafife alınan maliyetini içerir. Benimsememenin maliyeti rekabetçidir: rakipler daha hızlı teslim edebilir ve modern araçlar bekleyen yetenekleri çekebilir. Dikkatsizce benimsemenin maliyeti kalite aşınması, güvenlik olayları ve hukuki risktir. Liderliğe gerekçeyi, gerçek teslimat ve kalite sonuçlarını ölçen bir pilotla, normlar, doğrulama ve veri koruma için somut bir planla birlikte sunun.

## Anti-kalıplar ve tuzaklar

- **Otomatik pilot kabul.** Önerileri okumadan ya da anlamadan commit etmek.
- **Gösteriş metrikleri.** Başarıyı kabul oranı ya da üretilen satır sayısıyla yargılamak.
- **İstemlerde gizli bilgiler.** Kimlik bilgilerini ya da hassas veriyi dış araçlara yapıştırmak.
- **Yapay zeka testlerine güvenmek.** Amaçlanan davranışı değil mevcut davranışı kilitleyen üretilmiş testleri kabul etmek.
- **Kaynak izini görmezden gelmek.** Üretilen koddaki lisans ve bağımlılık risklerini gözden kaçırmak.
- **Beceri aşınması.** Kıdemsizlerin anlamayı dışarıya devretmesine ve temelleri hiç öğrenmemesine izin vermek.
- **Tekdüze güven.** Güvenlik açısından kritik koda, basmakalıp koda uygulanan aynı düşük özeni uygulamak.

## Olgunluk modeli

- **Düzey 1, Başlangıç:** Bireyler asistanları gelişigüzel ve reaktif biçimde kullanır; politika yoktur, ölçüm yoktur; gizli bilgiler ve fikri mülkiyet risk altındadır ve üretilen kod, herkesin o an uyguladığı özenle birleştirilir.
- **Düzey 2, Geliştirme:** Temel kullanım rehberliği ve veri kuralları vardır ve bazı güvenlik taramaları çalışır, ama uygulama takımlar arasında tutarsızdır: doğrulama derinliği kişiye göre değişir, üretkenlik iddiaları anekdotsaldır ve yüksek riskli kod güvenilir biçimde kapıyla korunmaz.
- **Düzey 3, Standartlaştırma:** Risk düzeyine göre normlar belgelenmiş ve kuruluş genelinde uygulanır: zorunlu insan incelemesi, işlem hattında güvenlik ve lisans taramaları, gereken yerde güvenli ya da şirket içi dağıtım, açıklama uygulamaları ve dışlanmış ya da yalnızca uzman incelemesine açık modüllerin açık bir listesi.
- **Düzey 4, Yönetme:** Uygulama temel çizgilere karşı ölçülür ve kontrol edilir: çevrim süresi, değişiklik başarısızlık oranı ve kusur kaçış oranı benimsemeden önce ve sonra izlenir, inceleme ve düzeltme maliyeti nicelendirilir, gizli bilgi sızıntısı ve lisans riski olayları sayılır ve araçlar ile genişleme hakkındaki git ya da gitme kararları satıcı iddialarına değil bu kanıta dayanır.
- **Düzey 5, Orkestrasyon:** Yapay zeka desteği sürekli iyileştirilir ve kurum genelinde bütünleştirilir: doğrulama varsayılan yol olarak işlem hattına yerleştirilmiştir, beceri gelişimi bilinçli ve izlenir, araçlar birkaç ayda bir değişirken politika uyum sağlar ve kurum, kanıt ile risk tablosu değiştikçe asistanları düzenli olarak yeniden değerlendirir, değiştirir ve kapsamlarını yeniden belirler.

## Tartışma fikirleri

- Doğrulama gereksinimleri basmakalıp kod ile güvenlik açısından kritik kod arasında nasıl farklılaşmalı?
- Sizin bağlamınızda hangi üretkenlik metrikleri yapay zeka desteğinden gelen değeri gerçekten yansıtır?
- Yapay zeka destekli katkılar ne zaman, varsa, açıklanmalı?
- Beceri aşınmasını, özellikle kıdemsiz mühendisler için, nasıl önlersiniz?
- Hangi veri işleme kısıtlamaları hangi araçları kullanabileceğinizi belirler?
- Üretilen koddan gelen lisans ve kaynak izi riskini nasıl yönetirsiniz?

## Önemli çıkarımlar

- Sorumluluk mühendiste kalır; yapay zeka çıktısı doğrulanması gereken güvenilmeyen bir taslaktır.
- Doğrulamayı riske göre ölçekleyin ve güvenlik açısından kritik yapay zeka koduna uzman incelemesi olmadan asla güvenmeyin.
- Öneri sayılarını değil, gerçek teslimat ve kalite sonuçlarını ölçün.
- Güvenlik, veri sızıntısı ve lisans risklerine karşı politika ve araçlarla korunun.
- Net normlar belirleyin ve insan mühendislik becerisini bilinçli olarak koruyun.

## Kaynaklar ve ileri okuma

- Nicole Forsgren, Jez Humble, and Gene Kim, *Accelerate: The Science of Lean Software and DevOps*.
- Andrew Ng, *Machine Learning Yearning* (on realistic expectations and measurement).
- OWASP Foundation, *OWASP Top 10 for Large Language Model Applications*.
- Peter Naur, *Programming as Theory Building* (on understanding versus code artifacts).
- Titus Winters, Tom Manshreck, and Hyrum Wright, *Software Engineering at Google*.
- GitClear and related industry studies on AI-assisted code quality trends.
