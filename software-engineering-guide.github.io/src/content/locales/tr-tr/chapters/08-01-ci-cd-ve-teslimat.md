# 8.1 CI/CD ve teslimat

## Genel bakış ve motivasyon

[Sürekli bütünleştirme](https://en.wikipedia.org/wiki/Continuous_integration) ve [sürekli teslimat](https://en.wikipedia.org/wiki/Continuous_delivery) (CI/CD), kod yazmakla onu kullanıcıların önüne güvenle koymak arasındaki bağ dokusudur. Sürekli bütünleştirme, her değişikliğin sık sık ortak bir ana hatta birleştirilmesi, ardından otomatik olarak derlenip test edilmesi demektir; böylece bütünleştirme sorunları uzun bir sürüm döngüsünün sonunda değil, dakikalar içinde ortaya çıkar. Sürekli teslimat, işlem hattından geçen her değişikliğin dağıtılabilir durumda tutulması demektir; böylece üretime çıkmak bir mühendislik telaşı olmaktan çıkıp bir iş kararı haline gelir. [Sürekli dağıtım](https://en.wikipedia.org/wiki/Continuous_deployment) bir adım daha ileri gider ve geçen her değişikliği, hiçbir insan kapısı olmadan otomatik olarak yayımlar.

Büyük takımlar için bu ayrımlar çok önemlidir. Yüzlerce mühendis örtüşen sistemlere commit attığında, elle bütünleştirmenin ve elle testin maliyeti doğrusal olmayan biçimde artar. Ortak, otomatik bir işlem hattı, çok sayıda katkıcıya hızlı ve güvenilir geri bildirim vermenin ve bir takımın değişikliğinin diğerininkini sessizce bozmasını önlemenin tek pratik yoludur. İşlem hattı, yazılımın sağlıklı olup olmadığı konusundaki tek doğru kaynak olur ve ölçekte hiçbir belgenin ya da iyi niyetin garanti edemeyeceği bir tutarlılığı dayatır.

Kurumsal ve kamu bağlamları bir boyut daha ekler: denetlenebilirlik ve değişiklik denetimi. Düzenleyicilerin, güvenlik görevlilerinin ve denetçilerin, değişikliklerin gözden geçirildiğine, test edildiğine ve onaylandığına, ayrıca üretimde çalışan yapıtın tam olarak derlenip incelenen yapıt olduğuna dair kanıta ihtiyacı vardır. İyi tasarlanmış bir CI/CD işlem hattı, bu uyum yükümlülüklerini evrak külfetinden normal mühendislik iş akışının otomatik bir yan ürününe dönüştürür. İyi yapıldığında teslimat aynı anda hem daha hızlı hem daha güvenli olur; yönetim için en çok önem taşıyan sonuç budur.

*Ayrıca bakın:* bölüm 8.4 (platform mühendisliği ve geliştirici deneyimi), bölüm 8.5 (test ve süreç otomasyonu) ve aşamalı teslimatın (bir değişikliği kademeli olarak yayımlarken sağlık ölçütlerini otomatik izlemek) mümkün kıldığı [özellik bayrağı](https://en.wikipedia.org/wiki/Feature_toggle) (işlevselliği yeniden dağıtım yapmadan kullanıcılara açan çalışma zamanı anahtarları) ve deney uygulamaları için bölüm 7.4 (ürün analitiği ve deneyler).

## Temel ilkeler

- Küçük değişiklikleri sık sık bütünleştirin; uzun ömürlü dallar sürekli bütünleştirmenin düşmanıdır.
- Yapıtı bir kez derleyin ve aynı yapıtı her ortamdan geçirerek terfi ettirin.
- İşlem hattını yetkili kapı yapın: yeşilse değişiklik sevk edilebilir; kırmızıysa düzeltilene kadar iş durur.
- Hızlı geri bildirim için amansızca optimizasyon yapın; böylece geliştiriciler akışta kalır ve kusurlar bağlam tazeyken yakalanır.
- Tekrarlanan her şeyi otomatikleştirin: testler, güvenlik taramaları, hazırlama ve dağıtım dahil.
- İşlem hattı tanımlarına, tıklanarak yapılan konsol yapılandırması olarak değil, gözden geçirmeye tabi, sürüm denetimindeki kod olarak davranın.
- Güvenli, geri alınabilir sürümler için tasarım yapın; böylece her dağıtım hızla geri alınabilir.
- Özellik bayraklarını kullanarak dağıtımı (kodun kurulması) yayımlamadan (kullanıcılara açılması) ayırın.

## Öneriler

### İşlem hattını bir dizi kalite kapısı olarak tasarlayın

İşlem hattını ucuz ve hızlı olandan pahalı ve kapsamlı olana doğru ilerleyen aşamalara bölün: önce derleme ve birim testleri, sonra bütünleştirme testleri, güvenlik ve lisans taramaları, en sonunda hazırlık ve üretim ortamlarına dağıtım. Her aşama, bir değişikliğin geçmesi gereken bir kapıdır. Kapıları, en hızlı ve en çok başarısız olması muhtemel denetimler önce çalışacak biçimde sıralayın; bu, geliştiricilere mümkün olan en kısa sürede geri bildirim verir. Commit aşamasındaki geri bildirim döngüsünü mümkün olduğunca on dakikanın altında tutun. Bunun ötesinde geliştiriciler bağlam değiştirir ve verimlilik düşer.

### Bir kez derleyin, her yerde terfi ettirin

Derleme aşamasında tek bir değişmez yapıt üretin ve tam olarak o yapıtı test, hazırlık ve üretimden geçirerek terfi ettirin. Ortam başına asla yeniden derlemeyin, çünkü yeniden derleme farkları sessizce içeri sokabilir. Ortama göre değişen yapılandırma, ayrı derlemelere gömülmemeli, dağıtım sırasında enjekte edilmelidir. Bu uygulama aynı zamanda bir denetçiye, kesin olarak, üretimdeki ikilinin her kapıdan geçmiş olan ikili olduğunu söyleyebilmenizi sağlar.

### İşlem hattını politikanın uygulama noktası yapın

Gerekli denetimleri (kod gözden geçirme onayı, test kapsamı eşikleri, güvenlik taraması sonuçları, imzalı commit'ler) doğrudan işlem hattına ve dal koruma kurallarına kodlayın. Bir wiki'de duran elle uygulanan politika, son tarih baskısı altında rutin olarak atlanır. İşlem hattına kodlanmış politika ise her değişikliğe tek tip ve otomatik olarak uygulanır.

### Ana hattı her zaman yayımlanabilir tutun

Tek bir ortak dalda birleştirmeyi, az sayıda uzun ömürlü dalla ya da hiç olmadan sağlayan gövde tabanlı geliştirmeyi kullanın ya da kısa ömürlü özellik dalları kullanın ve bitmemiş işi uzun ömürlü dallar yerine özellik bayraklarının arkasına saklayın. Bu, birleştirme çakışmalarını küçük tutar ve ana hattı her zaman dağıtılabilir durumda tutar; gerçek sürekli teslimatın ön koşulu budur.

### Dağıtım stratejilerini bilinçli seçin

Dağıtım stratejisini hizmetin riskine ve etki alanına göre eşleştirin:

- **Kademeli (rolling)** dağıtımlar örnekleri yavaş yavaş değiştirir ve durumsuz hizmetler için makul bir varsayılandır.
- **[Mavi-yeşil](https://en.wikipedia.org/wiki/Blue-green_deployment)**, iki özdeş ortam bulundurur ve trafiği bir seferde değiştirir; anında geri alma yolu sağlar.
- **Kanarya** sürümleri trafiğin küçük bir yüzdesini yeni sürüme yönlendirir, sağlık ölçütlerini izler ve ancak sinyaller iyiyse genişler.
- **Özellik bayrakları** yayımlamayı dağıtımdan ayırır; yeniden dağıtım yapmadan işlevselliği belirli kullanıcılar ya da kohortlar için açmanıza izin verir.

### Otomatik geri almayla aşamalı teslimatı benimseyin

Aşamalı teslimat, kanarya sürümlerini hata oranı, gecikme ve doygunluk gibi ölçütlerin otomatik analiziyle birleştirir. Nesnel sağlık ölçütlerini önceden tanımlayın, ardından sistemin bu sinyallere göre otomatik olarak terfi ettirmesine ya da geri almasına izin verin. Otomatik geri alma, küçük bir olayı büyük bir olaya çeviren insani tereddüdü ortadan kaldırır.

### Düzenlemeye tabi ortamlar için sürüm yönetimi ve değişiklik denetimi sağlayın

Düzenlemeye tabi ortamlarda hafif ama gerçek bir değişiklik yönetimi kaydı tutun. Her değişikliği kimin onayladığını, hangi testlerin çalıştığını ve hangi yapıtın dağıtıldığını otomatik olarak yakalayın. Değişiklik danışma süreçlerini yalnızca gerçekten yüksek riskli değişiklikler için kullanın, yalnızca onlara ayırın. Her rutin değişikliği haftalık bir kuruldan geçirmek, otomasyonun değerini yok eder. Bunun yerine, işlem hattından törensiz akan standart, önceden onaylanmış değişiklik türlerini hedefleyin.

## Ödünleşimler: artılar ve eksiler

| Yaklaşım | Artılar | Eksiler | En uygun olduğu yer |
|---|---|---|---|
| Sürekli teslimat (elle yayımlama kapısı) | Zamanlamayı iş tarafı denetler; düzenlemeye tabi yayımlama pencereleri için güçlü | Ana hattı sevk edilebilir tutmak için disiplin gerektirir | Değişiklik pencereleri olan kurumlar |
| Sürekli dağıtım (tümüyle otomatik) | En hızlı geri bildirim; en küçük gruplar | Olgun testler ve gözlemlenebilirlik ister | Yüksek güvenli, yüksek sıklıklı takımlar |
| Mavi-yeşil | Anında geri alma; basit zihinsel model | Geçiş sırasında ortam maliyetini ikiye katlar | Hızlı geri dönüş gereken kritik hizmetler |
| Kanarya + aşamalı teslimat | Etki alanını sınırlar; veri güdümlü | Kurması karmaşık; iyi ölçütler gerekir | Büyük ölçekli, kullanıcıya dönük sistemler |
| Özellik bayrakları | Dağıtımı yayımlamadan ayırır | Temizlenmezse bayrak borcu doğar | Bitmemiş işi güvenle sevk eden takımlar |

Merkezî ödünleşim hız ile denetim arasındadır, ancak bu çoğu zaman yanlış bir seçimdir. Olgun otomasyon ikisini birden sunar: sürümler daha küçük oldukları için daha hızlı, her biri doğrulanıp geri alınabilir olduğu için daha güvenlidir. Gerçek maliyet, test kapsamına, gözlemlenebilirliğe ve işlem hattı mühendisliğine yapılan başlangıç yatırımı ile bunları sağlıklı tutmak için gereken süregelen disiplindir. Bu yatırımdan kaçınan kurumlar güvenliği olmayan bir hız elde eder; bu da yavaş bir elle sürecten daha kötüdür.

## Takımınızla tartışılacak sorular

1. **Commit aşaması geri bildirim süresi hedefiniz nedir ve test takımı on dakikayı aştığında neyi keseceksiniz?** Yavaş bir commit aşaması sürekli bütünleştirmeyi sessizce öldürür, çünkü geliştiriciler yeşili beklemeyi bırakıp değişiklikleri biriktirmeye başlar. Sayıyı şimdi belirleyin (bu bölüm on dakikanın altını savunur) ve onu tutma mekanizmasını da belirleyin: paralel çalışanlar, sıkı bir test piramidi ve yavaş bütünleştirme denetimlerini sonraki bir aşamaya taşımak. Kurumsal ölçekte bu bir platform kararıdır; çünkü yüzlerce mühendis aynı işlem hattını paylaşır ve eklenen her dakika her commit'te çarpılır. Toplantıya gerçek veri getirin: mevcut p50 ve p95 işlem hattı süresi, en yavaş on test ve insanların beklemek yerine ne sıklıkla yeniden çalıştırdığı. Hedefi söyleyip sayılarla savunamıyorsanız, işlem hattınız CI kılığına girmiş bir toplu sürece doğru kayıyor demektir.

2. **Her hizmet hangi dağıtım stratejisini kullanıyor ve bu seçimden kim sorumlu?** Kademeli, mavi-yeşil ve kanarya birbirinin yerine geçmez: maliyeti, geri alma hızını ve karmaşıklığı farklı biçimde ödünleştirirler ve doğru seçim hizmetin etki alanına bağlıdır. Mavi-yeşil, geçiş sırasında ikiye katlanan bir ortam bedeliyle anında geri alma satın alır; bu bir ödeme sistemi için buna değer, bir iç pano için israftır. Kanarya maruziyeti sınırlar ama iyi sağlık ölçütleri ve daha fazla işlem hattı mühendisliği ister. Büyük ya da düzenlemeye tabi bir yapıda bunu her takımın alışkanlığına bırakmak, bir olay sırasında ortaya çıkan tutarsızlık üretir; bu yüzden hizmet katmanı başına varsayılanlar üzerinde anlaşın ve kararı kaydedin. Hizmet kataloğunuzu getirin ve her hizmeti stratejisi, geri alma yolu ve bu kararın sahibi olan kişiyle etiketleyin.

3. **Üretimdeki yapıtın her kapıdan geçen yapıtın tam olarak aynısı olduğunu nasıl kanıtlarsınız?** Bir kez derleyip aynı yapıtı terfi ettirmek, denetlenebilirliğin bütün meselesidir ve biri ortam başına yeniden derlediği ya da çalışan bir makineye yama yaptığı anda bozulur. Kurumsal ve kamu ortamlarında bir denetçi, çalışan bir ikiliyi commit'ine, gözden geçirmesine ve onaylarına kadar izlemenizi isteyecektir ve bu cevabın bir hafta değil saniyeler sürmesini istersiniz. Bunu nasıl zorunlu kılacağınıza karar verin: değişmez yapıtlar, imzalı imajlar, dağıtım sırasında imza doğrulaması ve ayrı derlemelere gömülmek yerine dağıtım sırasında enjekte edilen yapılandırma. Mevcut boşlukları masaya getirin: yeniden derleme yapan herhangi bir aşama, elle acil düzeltme yolu ve yapılandırmanın yapıtı çatalladığı yerler. Cevap, uyum kanıtlarınızın işlem hattının bir yan ürünü mü yoksa her denetimden önce elle yapılan bir telaş mı olacağını belirler.

4. **Ana hat kırmızıya döndüğünde gerçekte ne durur ve kararsız (flaky) testleri nasıl ele alırsınız?** Bir işlem hattı, ancak kırmızı bir derleme işi gerçekten durduruyorsa yetkili bir kapıdır; oysa birçok kurum bozuk bir ana hattı ve aralıklı hata birikimini sessizce hoş görür. Bu, geliştiricileri yeşil olana kadar yeniden çalıştırmaya ve hataların üzerine sevk etmeye alıştırır. Büyük bir takım için bu çürüme bileşik etkiyle büyür, çünkü bir takımın görmezden geldiği kararsız test herkesin kapıyı atlama bahanesi olur ve işlem hattına olan güveni korumak, yeniden kurmaktan çok daha ucuzdur. Karşıt çekimleri tartın: sıkı bir hattı durdurma kuralı kaliteyi korur ama tek bir kötü commit yüzünden yüzlerce mühendisi bloke edebilir; gevşek bir politika verimi korur ve kapıyı aşındırır. Tartışmaya kanıt getirin: mevcut ana hat kırmızı kalma süresi, karantinaya alınmış ya da kararsız testlerin sayısı, yeniden çalıştırma oranı ve değişikliklerin başarısız bir denetimin üzerinden ne sıklıkla birleştirildiği. Kurumsal ve kamu ortamlarında kararsız test ayıklamasının kimin sorumluluğunda olduğunu ve birleştirmeleri dondurma yetkisinin kimde bulunduğunu adlandırın, çünkü kimsenin uygulamaktan sorumlu olmadığı bir kapının rutin olarak aşıldığını denetçiler bulur.

5. **Özellik bayrakları için yaşam döngünüz nedir ve onları emekliye ayırmaktan kim sorumlu?** Bayraklar, dağıtımı yayımlamadan ayırmanızı ve bitmemiş işi saklamanızı sağlayan şeydir; ama her bayrak, kodunuzda kendi kendine asla temizlenmeyen bir daldır ve yönetilmeyen bayraklar, kimsenin dokunmaya cesaret edemediği koşullu karmaşıklık olarak birikir. Büyük bir yapıda bu borç tehlikelidir, çünkü eskimiş bir bayrak bir güvenlik düzeltmesini sessizce kapatabilir ya da test edilmemiş kod yollarını üretime açabilir ve bayrağı yaratan kişi çoğu zaman başka işe geçmiştir. Gerilimi dengeleyin: bayraklar size güvenli, artımlı teslimat kazandırdı; dolayısıyla amaç daha az bayrak değil, sahibi, son kullanma beklentisi ve eskiyenleri ortaya çıkaran araçları olan disiplinli bir yaşam döngüsüdür. Toplantıya mevcut envanteri getirin: kaç bayrak canlı, en eskisi kaç yaşında, hangilerinin sahibi yok ve uzun ömürlü herhangi bir bayrak artık başka yerde durması gereken kalıcı bir yapılandırma işlevi görüyor mu. Düzenlemeye tabi ortamlar için ekleyin: üretimde bir bayrağı kim değiştirebilir ve bu değişiklik, bir dağıtım kadar titizlikle kaydediliyor mu; çünkü bir bayrak çevirmek, işlem hattı hiç çalışmasa bile bir yayımlamadır.

6. **İnsan kapılı sürekli teslimat ile tam sürekli dağıtım arasındaki sınır nerede ve geri alma eşiklerini kim belirler?** Sürekli teslimat yayımlama zamanlamasını bir insanın denetiminde tutar; bu, yasal değişiklik pencerelerine ve etki alanı yüksek sistemlere uygundur. Sürekli dağıtım ise geçen her değişikliği otomatik sevk eder ve güvenli olmak için olgun testler, gözlemlenebilirlik ve otomatik geri alma gerektirir. Büyük ya da düzenlemeye tabi bir kurum için cevap nadiren tektir: pazarlama siteniz sürekli dağıtım yapabilirken ödeme çekirdeğiniz belgelenmiş bir insan kapısı tutar ve bu çizgiyi hizmet katmanı başına çekmek hem gereksiz sürtünmeyi hem de pervasız otomasyonu önler. Rekabet eden hususlar, hız ve grup boyutu ile denetim ve denetlenebilirlik ve ayrıca otomatik geri almanın gerektirdiği sağlık ölçütlerinin mühendislik maliyetidir. Kanıtı getirin: hizmet başına değişiklik başarısızlık oranı, ortalama kurtarma süresi, mevcut yayımlama temposu ve insan olmadan terfi ettirmek ya da geri almak için güveneceğiniz nesnel sinyaller (hata oranı, gecikme, doygunluk). Kamu ve kurumsal ortamlarda her katmanı, geri alma eşiklerinin sahibine ve kapılı bir yayımlamadan tam otomasyona geçişi kimin onayladığına bağlayın; böylece karar savrulmak yerine bilinçli olur.

## Sektör merceği

**Girişim.** İlk günden yönetilen CI/CD'ye yaslanın: barındırılan bir çalıştırıcı, tek bir işlem hattı, tek bir değişmez imaj ve birleştirmede hazırlık ortamına otomatik dağıtım. Sonra bakımını yapmak zorunda kalacağınız işlem hattı altyapısı kurmayın. Özellik bayrakları iki üç mühendisin yarım kalmış işi güvenle birleştirmesine ve günde birkaç kez sevk etmesine izin verir; ölçek daha fazlasını zorunlu kılana kadar tek tıkla üretim dağıtımı ve hızlı bir bayrak kapatma, ihtiyaç duyacağınız tüm değişiklik denetimidir.

**Küçük işletme.** Özel bir platform ya da sürüm mühendisi yoksa, özel bir çözüm yerine kaynak barındırıcınızın sunduğu işlem hattını (yerleşik Actions ya da eşdeğeri) ve onun varsayılan dağıtım stratejisini tercih edin. Satın alma ya da kurma seçimini dürüstçe çerçeveleyin: yönetilen bir işlem hattı ve yerleşik geri alması olan bir barındırma platformu, özel bir kurulumun tükettiği mühendis saatinden daha ucuza gelir. Temelleri koruyun: bir kez derleyin, aynı yapıtı terfi ettirin ve kolay bir geri dönüş. Hacim gerekçelendirene kadar aşamalı teslimat mekanizmasını atlayın.

**Kurumsal.** Temel sorun birçok takım arasında tutarlılıktır: gözden geçirmeyi, taramayı, imzalı değişmez yapıtları ve katman başına dağıtım stratejilerini zorunlu kılan ortak bir işlem hattı şablonunu standartlaştırın; böylece kalite takımdan takıma değişmez. İşlem hattı tanımlarına gözden geçirilen kod olarak davranın, değişiklik denetimi kanıtını otomatik yakalayın ve özellik bayraklarını ile geri alma eşiklerini her takımın özel alışkanlığı değil, yönetilen varlıklar olarak ele alın. Karşılığı, daha hızlı teslimat ve üç ayda bir yaşanan telaş yerine bir yan ürün olarak üretilen denetim kanıtıdır.

**Kamu.** Tedarik kuralları, yasal değişiklik pencereleri ve kamusal hesap verebilirlik işlem hattını şekillendirir. Sonuçları ağır sistemlerde tam otomasyon yerine belgelenmiş bir insan yayımlama kapılı sürekli teslimatı tercih edin, rutin işi önceden onaylanmış standart değişiklikler olarak sınıflandırın ve vatandaşların dar yıllık pencerelerde bağlı olduğu hizmetler için anında bir geri alma yolu (mavi-yeşil ya da otomatik kanarya) tutun. İşlem hattının her değişikliği kimin onayladığını, hangi testlerin çalıştığını ve hangi yapıtın dağıtıldığını kaydettiğinden emin olun; böylece şeffaflık ve denetim yükümlülükleri elle evrak yerine normal iş akışıyla karşılanır.

## Örnekler

**Girişim.** Dört kişilik bir SaaS girişimi, birim testlerini çalıştıran, tek bir Docker imajı derleyen ve main'e her birleştirmede aynı imajı hazırlık ortamına otomatik dağıtan tek bir GitHub Actions işlem hattı kurar. Üretim dağıtımı tek bir tıktır ve kurucular özellik bayraklarına yaslanır; böylece bir dalı haftalarca canlı tutmak yerine yarım kalmış işi bir bayrağın arkasında birleştirebilirler. Kötü bir sürüm sızdığında bayrağı saniyeler içinde kapatıp sakince düzeltirler; bu, özel bir operasyon kişisi olmadan küçük takımlarının günde birkaç kez sevk etmesini sağlar.

**Kurumsal.** Küresel bir banka, düzinelerce takıma özel Jenkins işini her ürün takımının devraldığı standartlaştırılmış bir işlem hattı şablonunda birleştirir. Şablon, statik analizi, bağımlılık taramasını ve imzalı, değişmez bir yapıtı zorunlu kılar; hata oranı ve gecikme eşiklerine bağlı otomatik geri almayla kanarya yoluyla dağıtım yapar. Aynı yapıt testten üretime terfi ettirildiği ve her kapı kaydedildiği için bankanın denetçileri herhangi bir üretim ikilisini commit'ine, gözden geçirmesine ve onayına saniyeler içinde izleyebilir; bu, üç ayda bir yapılan elle kanıt toplama çalışmasının yerini alır.

**Kamu.** Bir dosyalama sistemini modernleştiren ulusal bir vergi idaresi, beyan sezonunda yasal değişiklik pencerelerine saygı gösterebilmek için açık bir insan yayımlama kapılı sürekli teslimat benimser. Rutin değişiklikler, hazırlık ortamına otomatik akan standart, önceden onaylanmış değişiklikler olarak sınıflandırılır. Üretim yayımı, işlem hattının kaydettiği tek bir belgelenmiş onay gerektirir. Mavi-yeşil dağıtım, bir kusur üretime ulaşırsa idareye anında geri alma yolu verir; milyonlarca vatandaşın dar bir yıllık pencerede hizmete bağlı olduğu durumda bu kritiktir.

## İş gerekçesi: motivasyonlar, YG ve TSM

CI/CD yatırımının getirisi; değişiklikler için kısalan teslim süresinde, düşen değişiklik başarısızlık oranında ve olaylar yaşandığında daha hızlı kurtarmada görünür: araştırmaların hem teslimat performansı hem de kurumsal sonuçlarla tutarlı biçimde ilişkilendirdiği ölçütler. Daha hızlı, daha küçük sürümler, ölçekte mühendislik kapasitesini tüketen eşgüdüm yükünü azaltır; otomatik doğrulama ise üretim kusurlarıyla yangın söndürmenin pahalı ve moral bozucu işini azaltır.

Toplam sahip olma maliyeti (TSM), benimseme maliyetini benimsememenin maliyetiyle tartar. Benimseme maliyetleri arasında işlem hatlarını kurmak ve sürdürmek, test kapsamını büyütmek, gözlemlenebilirliğe ve platform personeline yatırım yapmak yer alır. Benimsememenin maliyeti daha büyük ama daha az görünürdür: yavaş elle sürümler, bütünleştirme acısı, itibara zarar veren üretim olayları ve düzenlemeye tabi ortamlarda başarısız denetimler ile düzeltme çalışmaları. Yönetim için argüman en iyi risk azaltma ve kapasite açısından çerçevelenir. Otomasyon, kıt kıdemli mühendis zamanını tekrarlayan sürüm angaryasından ürün işine çevirirken kesintileri daha seyrek ve daha kısa hale getirir.

## Anti-kalıplar ve tuzaklar

- **Kar tanesi işlem hatları.** Her takım kendine özgü bir işlem hattını elle kurar; bu yüzden iyileştirmeler ve düzeltmeler paylaşılamaz ve kalite çılgınca değişir.
- **Ortam başına yeniden derleme.** Her aşama için yeniden derlemek "bir kez derle" garantisini bozar ve ince farkların üretime ulaşmasına izin verir.
- **Görmezden gelinen kırmızı derlemeler.** Sürekli bozuk bir ana hattı hoş görmek işlem hattına güveni yok eder ve hataların üzerine sevk etmeyi olağanlaştırır.
- **Ele alınmayan kararsız testler.** Aralıklı hatalar geliştiricileri yeşil olana kadar yeniden çalıştırmaya alıştırır ve kapının amacını boşa çıkarır.
- **Elle onay tiyatrosu.** Her şeyi mühürleyen bir değişiklik danışma kurulu, güvenlik katmadan gecikme ekler.
- **Bayrak borcu.** Hiç kaldırılmayan özellik bayrakları, sürdürülemez bir koşullu karmaşıklık olarak birikir.
- **Dağıtım eşittir yayımlama.** İkisini birbirine bağlamak, kullanıcıya dönük her değişikliğin riskli bir yeniden dağıtım gerektirmesi demektir.

## Olgunluk modeli

**Düzey 1, Başlangıç.** Derlemeler ve dağıtımlar büyük ölçüde elle, geçici ve tepkiseldir. Bütünleştirme geç yapılır, sürümler seyrek ve stresli geçer, geri alma eski bir sürümü elle yeniden dağıtmak anlamına gelir ve işlem hattı kapısı diye ortak bir kavram yoktur.

**Düzey 2, Geliştirme.** Otomatik derlemeler ve birim testleri her commit'te çalışır ama uygulamalar takımdan takıma değişir. Dağıtımlar betiklenmiştir ancak hâlâ elle tetiklenir ve gözetlenir, bazı ortamlar tutarlıdır ve yapıtlar hâlâ aşama başına yeniden derlenebilir. Bir işlem hattı varsa çoğu zaman paylaşılamayan bir kar tanesidir.

**Düzey 3, Standartlaştırma.** Belgelenmiş, standartlaştırılmış bir işlem hattı şablonu takımlar arasında uygulanır. Tek bir değişmez yapıtı bütün ortamlardan geçirerek terfi ettirir, otomatik kalite ve güvenlik kapıları uygular, gözden geçirme onayı ve tarama sonuçları gibi gerekli denetimleri kodlar ve değişiklik kayıtlarını otomatik yakalar. Kanarya ya da mavi-yeşil gibi dağıtım stratejileri hizmet katmanı başına bilinçli seçilir.

**Düzey 4, Yönetme.** Teslimat, temel çizgilere göre ölçülür ve denetlenir. Kurum, değişiklikler için teslim süresini, dağıtım sıklığını, değişiklik başarısızlık oranını ve ortalama kurtarma süresini, ayrıca işlem hattı p50 ve p95 süresini, kararsız test ve yeniden çalıştırma oranlarını ve özellik bayrağı yaşını izler. Geri alma eşikleri gözlenen hata oranı, gecikme ve doygunluk verisinden belirlenir, kapılar alışkanlık yerine kanıta göre uygulanır ve her ölçütün, hedeften saptığında harekete geçen bir sahibi vardır.

**Düzey 5, Orkestrasyon.** Teslimat sürekli iyileşir ve kurum genelinde bütünleşiktir. Otomatik, ölçüt güdümlü geri almayla aşamalı teslimat norm haline gelir, yayımlama iyi yönetilen bayraklarla dağıtımdan ayrılır ve uyum kanıtı bir yan ürün olarak otomatik üretilir. İşlem hattı yapı değiştikçe uyum sağlar ve teslimat ölçütleri iş ve risk planlamasını besler; böylece yatırım en yüksek kaldıraçlı iyileştirmelere akar.

## Tartışma fikirleri

- En kritik sistemleriniz için insan kapılı sürekli teslimat ile tam sürekli dağıtım arasındaki doğru sınır nerededir?
- Zorunlu bir değişiklik yönetimi sürecini, onu mühür basma tiyatrosuna dönüştürmeden nasıl anlamlı tutarsınız?
- Otomatik geri almayı hangi nesnel sağlık ölçütleri yönetmeli ve eşiklerinin sahibi kimdir?
- Platform takımları, standartlaştırılmış işlem hattı şablonlarını olağandışı gereksinimleri olan takımların meşru ihtiyaçlarıyla nasıl dengelemelidir?
- Özellik bayraklarını borca dönüşmeden önce emekliye ayırmak için politikanız ve araçlarınız nedir?
- Daha hızlı teslimatın yalnızca daha çok şey sevk etmek yerine iş sonuçlarını gerçekten iyileştirip iyileştirmediğini nasıl ölçersiniz?

## Önemli çıkarımlar

- CI, CD ve sürekli dağıtım ayrı şeylerdir; risk toleransınıza ve olgunluğunuza uyan otomasyon düzeyini seçin.
- Yapıtı bir kez derleyin ve aynı yapıtı her ortamdan geçirerek terfi ettirin.
- İşlem hattını hızlı geri bildirim için optimize edilmiş, sıralı kalite kapıları olarak tasarlayın ve onu yetkili sevk kararı sayın.
- Dağıtım stratejilerini bilinçli seçin ve etki alanını sınırlamak için otomatik geri almalı aşamalı teslimatı benimseyin.
- Yayımlamayı dağıtımdan özellik bayraklarıyla ayırın ve bayrak borcunu yönetin.
- Düzenlemeye tabi ortamlarda değişiklik denetimi kanıtını elle evrak yerine otomatik yakalayın.

## Kaynaklar ve ileri okuma

- Jez Humble and David Farley, *Continuous Delivery: Reliable Software Releases through Build, Test, and Deployment Automation*.
- Nicole Forsgren, Jez Humble, and Gene Kim, *Accelerate: The Science of Lean Software and DevOps*.
- Gene Kim, Jez Humble, Patrick Debois, and John Willis, *The DevOps Handbook*.
- Gene Kim, Kevin Behr, and George Spafford, *The Phoenix Project*.
- Betsy Beyer, Chris Jones, Jennifer Petoff, and Niall Richard Murphy (eds.), *Site Reliability Engineering*.
- Pete Hodgson, "Feature Toggles (Feature Flags)" (essay).
- ITIL (Information Technology Infrastructure Library), change management guidance.
