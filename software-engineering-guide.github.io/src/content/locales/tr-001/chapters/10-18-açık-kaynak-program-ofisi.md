# 10.18 Açık kaynak program ofisi (OSPO) ve yukarı akışa katkı

## Genel bakış ve motivasyon

Kurumunuz zaten [açık kaynak yazılım](https://en.wikipedia.org/wiki/Open-source_software) üzerinde çalışıyor: ürününüzü taşıyan işletim sistemleri, diller, veritabanları ve kütüphaneler çoğunlukla sizin için çalışmayan insanlar tarafından yazılıyor. Bölüm 10.3 satın almayı ve lisans uyumunu, bölüm 10.12 ise açık ile kapalı kararını ele alır. Bu bölüm, tüm bunları tutarlı kılan işlevle ilgilidir: [açık kaynak program ofisi](https://en.wikipedia.org/wiki/Open_Source_Program_Office) (OSPO), şirketin açık kaynağı nasıl tükettiğini, ona nasıl katkıda bulunduğunu ve onu nasıl yayımladığını sahiplenen takım. OSPO, `import` yazan her mühendise yayılmış olan bir ilişkinin ağırlık merkezidir.

Çoğu kurum açık kaynağa tek tek bağımlılıklarla, istemeden girer, sonra biriken riski bir anda keşfeder: bir devralma durum tespiti sırasında bir lisans sorusu, tek bir bitkin bakımcısı olan kritik bir kütüphane, kimsenin teslim ettiğini bilmediği kodda bir güvenlik duyurusu. OSPO bu telaşı yönetilen bir kabiliyete çevirir. Engellemek yerine olanak tanıyan bir tüketim politikası belirler, yukarı akışa katkının işe ne zaman hizmet ettiğine karar verir, yayımladığınız projelere bakıcılık eder ve açık işbirliğini şirketin içinde [InnerSource](https://en.wikipedia.org/wiki/Inner_source) aracılığıyla uygular. Bu, yazılım mühendisliği değerlerinize (bölüm 1.1) bağlı stratejik bir işlevdir, bir uyum onay kutusu değil.

Kurumlar için itici güç ölçektir: binlerce bağımlılık, yargı alanları arasında ihracat ve lisans yükümlülükleri ve her biri günlük küçük açık kaynak kararları veren yüzlerce mühendis. Tek bir ofis bu dağınıklığa bir omurga verir. Kamu için itici güç politika ve kamu güvenidir. "Varsayılan olarak açık kaynak" ve "kamu parası, kamu kodu" giderek yasa haline geliyor; bu yüzden kamu kurumlarının kodu güvenle yayımlayabilecek, kurumlar arasında yeniden kullanabilecek ve tedarikçileri açık standartlara bağlayabilecek birine ihtiyacı var. Her iki ortamda da OSPO, görünmez, fiyatlanmamış riski bilinçli, bütçelenmiş işe dönüştürerek kendini amorti eder.

## Temel ilkeler

- **Açık kaynak iki yönlü bir ilişkidir, bedava bir depo değil.** Tüketirsiniz, katkıda bulunursunuz ve yayımlarsınız; OSPO üçünü de sahiplenir.
- **Katkı stratejidir, hayırseverlik değil.** Yukarı akışa göndermek özel yamaları taşıma maliyetini azaltır ve size etki kazandırır.
- **Hızlı yolu mümkün kılın, kapıyı beklemeyin.** Kodu kopyalamaktan yavaş bir politika göz ardı edilir; bu yüzden uyumlu yolu en hızlı yol yapın.
- **Bağlı olduğunuz bakımcıları finanse edin.** Ortak kaynak kendi kendini sürdürmez ve en kritik kütüphanenizin ücretsiz çalışan tek bir yazarı olabilir.
- **Yayımladığınıza bakıcılık edin, ya da yayımlamayın.** Terk edilmiş bir proje, itibarınıza hiç proje olmamasından daha çok zarar verir.
- **İyileştirebilmek için etkileşimi ölçün.** Basın bültenlerini değil, katkıları, bağımlılık sağlığını ve onay süresini sayın.
- **Kamuda, varsayılan olarak açık olun ve varsayılan olarak yayımlayın.** Açıklık normdur; kapalılık belgelenmiş istisnadır.

## Öneriler

### Gerçekliğinize göre boyutlandırılmış bir OSPO kurun

Başlamak için büyük bir takıma ihtiyacınız yok. Bir girişimde OSPO, yazılı bir görevi ve haftada birkaç saati olan tek bir mühendis olabilir. Bir kurumda küçük bir merkezi grup artı ürün takımlarına yerleştirilmiş federe bir şampiyonlar ağıdır. Boyutu ne olursa olsun, ona dört sorumluluğu kapsayan net bir tüzük verin: tüketim politikası ve uyum, yukarı akışa katkı, kendi projelerinizi yayımlama ve onlara bakıcılık etme ve topluluk ile finansman ilişkileri. Onu hem mühendisliği hem hukuku görebileceği yere koyun; çoğu zaman CTO'ya ya da bir mühendislik başkan yardımcısına bağlı, hukuk ve güvenliğe noktalı bir hatla. Başarısızlık biçimi, tamamen hukukun içinde yaşayan ve bir frene dönüşen bir OSPO'dur; çözüm onu iş teslim eden mühendislerle kadrolamaktır ki rehberliği hizmet ettiği takımlarda itibar taşısın.

### Sorumlulukla tüketin ve güvenli yolu kolay yol yapın

Risk en çok tüketimle girer, bu yüzden iyi davranışı zahmetsiz kılın. Önceden incelenmiş bileşenlerden oluşan özenle seçilmiş bir iç katalog, hat içinde otomatik lisans ve güvenlik açığı taraması ve bir geliştiricinin bilet açmadan izleyebileceği net varsayılanlar sağlayın. Bölüm 10.3'teki lisans disiplinine ve bölüm 2.18'deki tedarik zinciri ve bağımlılık sağlığı pratiklerine yaslanın: sürümleri sabitleyin, yazılım malzeme listesi üretin, ele geçirilmiş ya da terk edilmiş paketler için [yazılım tedarik zincirini](https://en.wikipedia.org/wiki/Software_supply_chain) izleyin ve ömrünün sonunu bir geçişi zorlamadan önce takip edin. OSPO'nun işi her bağımlılığı elle onaylamak değildir. Seçimlerin yüzde doksan beşinin otomatik olarak güvenli olması ve yalnızca gerçekten alışılmadık vakaların bir insana ulaşması için korkuluklar kurmaktır.

### Yukarı akışa katkıda bulunun, çünkü karşılığını verir, hoş olduğu için değil

Yukarı akışa katkıyı ekonomik bir karar olarak ele alın. Bir bağımlılığa karşı taşıdığınız her özel yama, değişiklik yukarı akışa inene ya da çatal o kadar uzaklaşıp tamamen sizin olana kadar her yükseltmede sonsuza dek ödediğiniz bir vergidir. Düzeltmeyi geri katkılamak o vergiyi siler. Yukarı akışa göndermek ayrıca yönün üzerinde etki satın alır; böylece güvendiğiniz bir bileşenin yol haritası ihtiyaçlarınıza doğru eğilir ve işe almak istediğiniz mühendislere yetkinlik sinyali verir. Geliştiricilerinize hızlı, belgelenmiş bir yol verin: önceden onaylanmış bir katkıda bulunan lisans sözleşmesi ya da geliştirici menşe sertifikası, değişikliğin paylaşılmasının güvenli olduğunu doğrulayan hafif bir onay ve iş için bütçelenmiş yönetim zamanı. Alternatif, kontrol etmediğiniz bir projenin kalıcı bir [çatalını](https://en.wikipedia.org/wiki/Fork_(software_development)) sürdürmekse, geri katkılamak neredeyse her zaman daha ucuzdur.

### Kendi projelerinizi gerçek yönetişimle yayımlayın

Kendi yazdığınız yazılımı açık kaynak yaptığınızda bunu bilinçli yapın ya da hiç yapmayın. Önce kodun paylaşmaya değer bir meta mı yoksa kapalı tutmaya değer bir ayırt edici mi olduğuna, bölüm 10.12'deki muhakemeyi kullanarak karar verin. Yayımlarsanız, amacınıza uyan bir lisans seçin (benimsemeyi azamileştirmek için izin verici, ekosistemi karşılıklı tutmak için copyleft), kimin neye karar verdiğini yazılı bir yönetişim modeliyle belgeleyin ve kodu özgür tutarken kötüye kullanımdan koruyabilmek için proje adının [ticari markasını](https://en.wikipedia.org/wiki/Trademark) tescil ettirin. Gerçek bakıcılığa taahhüt edin: herkese açık bir sorun izleyici, bir katkı rehberi, bir davranış kuralları belgesi ve bildirenlerin size nasıl ulaşacağını bilmesi için koordineli ifşa içeren bir güvenlik politikası (bölüm 4.2). Bir bakımcı adlandırın ve zamanını bütçeleyin. Büyük bir gürültüyle başlatıp bir yıl içinde terk ettiğiniz proje, hiç yayımlamadığınız bir projeden itibarınıza daha çok zarar verir.

### Şirket içinde işbirliği için InnerSource uygulayın

Açık kaynağı çalıştıran alışkanlıklar (herkese açık depolar, net katkı rehberleri, liyakate göre inceleme, ilk yama için düşük engeller) güvenlik duvarının arkasında da aynı derecede iyi çalışır. InnerSource, her mühendisin herhangi bir iç projeyi bulabilmesi, kullanabilmesi ve iyileştirebilmesi, bilet açıp beklemek yerine takım sınırları boyunca bir çekme isteği göndermesi demektir. Bu, silolara son verir, kod yeniden kullanımını yayar ve insanlarınızı, dışarıya katkıda bulunduklarında kullanacakları iş akışının aynısında eğitir. OSPO, InnerSource için doğal yuvadır, çünkü araçların ve kültürel oyun kitabının zaten sahibidir. Birkaç yüksek değerli paylaşılan kütüphaneyle başlayın, katkı rehberlerini içeride yayımlayın ve dışarıdan gelen yamaları zarafetle kabul eden takımları ödüllendirin.

### Bağlı olduğunuz bakımcıları finanse edin ve sürdürün

Üretim sisteminiz, tek bir kişinin boş zamanında sürdürdüğü bir kütüphaneye dayanıyor olabilir. Bu bir tedarik zinciri riskidir ve dürüst cevap yükü taşımaya yardım etmektir. En kritik bağımlılıklarınızı malzeme listenizden belirleyin, ince bir bakımcı tabanı olanları bulun ve her biri için bir yanıt seçin: bakımcıyı doğrudan destekleyin, mühendislik zamanı katkılayın, projeyi finanse eden bir vakfa katılın ya da son çare olarak çatallamaya ya da değiştirmeye hazırlanın. Ortak kaynağı finanse etmek, çöküşünü izleyen acil duruma göre daha ucuzdur ve güvendiğiniz bileşenleri sağlıklı tutar ve etkileyebileceğiniz bir yönde ilerletir.

### Hızlı onaylayan bir katkı politikası belirleyin

Bir katkı politikası yavaşça hayır demek için değil, hızlıca evet demek için vardır. Bir mühendisin sormadan neye katkıda bulunabileceğini (hata düzeltmeleri, belgeler, zaten kullandığınız projelere küçük özellikler), neyin hafif bir kontrol gerektirdiğini (bir ayırt ediciye ya da bir patente dokunan her şey) ve fikri mülkiyet ile katkıda bulunan sözleşmelerinin katkı başına değil merkezi olarak bir kez nasıl ele alındığını açıkça yazın. Sıkıcı kısımları otomatikleştirin: lisans kontrolleri, önceden imzalanmış kurumsal bir katkıda bulunan sözleşmesi ve insan gözü gerektiren nadir gönderimleri işaretleyen bir bot. Onay süresini ölçün ve yavaş bir kuyruğu politikadaki bir hata olarak görün.

## Ödünleşimler: artılar ve eksiler

| Yaklaşım | Artılar | Eksiler |
| --- | --- | --- |
| Merkezi OSPO | Tutarlı politika, derin uzmanlık, net sahiplik | Yalnızca kapı bekler ve asla olanak tanımazsa darboğaza dönüşebilir |
| Federe OSPO (takımlarda şampiyonlar) | Ölçeklenir, kararları mühendislere yakın tutar | Güçlü koordinasyon gerektirir, yoksa politika dağılır |
| Yukarı akışa katkı | Özel yama vergisini siler, etki satın alır, işe almaya yardım eder | Süregelen efor, fikri mülkiyet incelemesi, başkasının takvimine bağlı iş |
| Özel çatalları taşımak | Tam kontrol, kendi zaman çizelgenizde teslim | Kalıcı bakım vergisi, yukarı akış güvenlik düzeltmelerinden uzaklaşır |
| Kendi projenizi yayımlamak | Ekosistem, itibar, paylaşılan bakım | Gerçek bakıcılık maliyeti; terk etmek itibara zarar verir |
| Bakımcıları finanse etmek | Kritik bağımlılıkları korur, iyi niyet kazandırır | Doğrudan maliyet ve kimi finanse edeceğini seçmek siyasidir |
| OSPO yok (plansız) | Sıfır kurulum maliyeti | Görünmez hukuki, güvenlik ve sürdürülebilirlik borcu |

Merkezdeki gerilim kontrol ile olanak tanıma arasındadır. Her bağımlılığı ve her katkıyı elle inceleyen bir OSPO güvenli hissettirir, ama mühendislerin etrafından dolaştığı şeye dönüşür; bu da önlemeye çalıştığınız görünmez gölge bağımlılıkları üretir. Hiçbir otomatik uygulama olmadan yalnızca neşeli rehberlik yayımlayan bir OSPO, son tarih yaklaştığı anda göz ardı edilir. Çözüm, bölüm 10.3'ten geçen aynı çözümdür: yaygın durumu otomatikleştirin ki uyumlu yol en hızlı yol olsun ve insan muhakemesini gerçekten yeni olana saklayın. Bu dengeyi doğru kurarsanız ofis bir kuvvet çarpanıdır; her iki yönde de yanlış kurarsanız ya bir fren ya da bir süs olur.

## Takımınızla tartışılacak sorular

1. **Bugün açık kaynakla ilişkinizi kim sahipleniyor ve yarın zor bir soruyu cevaplayabilir mi?** Olası bir devralıcının avukatları lisans envanterinizi isteseydi ya da bir gazeteci ödeme yolunuzda hangi bakımsız kütüphanenin durduğunu sorsaydı, cevabın yanında bir isim var mı? Çoğu kurum için dürüst cevap "hiç kimse"dir; bu da her mühendisin sessizce politika yaptığı ve toplamdan kimsenin sorumlu olmadığı anlamına gelir. Kanıtı toplantıya getirin: onaylı lisans listesini, yazılım malzeme listesini ve durum tespiti sırasında bir copyleft sorusunu karşılayacak kişiyi üretmeyi deneyin. Bu çıktılar yoksa ya da kimseye işaret etmiyorsa, ilk OSPO görevinizi bulmuşsunuz demektir. Verilecek karar, işleve sahip olup olmamak değil, onun kimde olduğu ve hangi görevi taşıdığıdır; ofis haftada bir günlük tek bir kişi olsa bile.

2. **Yukarı akışa gönderebileceğiniz özel yamalar taşıyor musunuz ve bu size neye mal oluyor?** Birçok takım bağımlılıklarına karşı sessiz bir yerel değişiklik yığını sürdürür, bunları her yükseltmede elle yeniden uygular ve birleştirme acısını doğa yasasıymış gibi sineye çeker. Bu yamaların her biri tekrar eden bir vergidir ve her biri vergi ortadan kalksın diye geri katkılanacak bir adaydır. Ayrıntıları getirin: derlemenizin gerçekte taşıdığı çatalları ve yerel yamaları listeleyin, her birinin yılda kaç mühendislik saatine mal olduğunu tahmin edin ve hangi yukarı akış projelerinin değişikliği büyük olasılıkla kabul edeceğini not edin. Rakip değerlendirme gerçektir, çünkü yukarı akışa göndermek şimdi efor ister ve bakımcının takvimine bağlıdır, ama karşılaştırma yama vergisini sonsuza dek ödemeyle yapılır. Cevap, "hep yeniden uyguluyoruz"u, mühendislerin kullanacağı kadar hızlı bir katkı yoluyla bilinçli bir seçime çevirmelidir.

3. **Bakımcısı çekip giderse en çok hangi bağımlılık acıtır ve bu konuda ne yapacaksınız?** Yığınınızın bir yerinde, bozulursa gelir ya da görev açısından kritik bir hizmeti durduracak, hiç finanse etmediğiniz ya da teşekkür etmediğiniz bir kişi ya da bir avuç kişi tarafından sürdürülen bir bileşen var. Ortak kaynak, artık öyle olmadığı ana kadar bedava hissettirir ve bu dersin pahalı sürümü, terk edilmenin ardından gelen telaş ya da yamalanmamış bir güvenlik açığıdır. Malzeme listenizi getirin ve bağımlılıkları patlama yarıçapına göre sıralayın, sonra ilk birkaçının bakımcı sayısını ve finansman durumunu not edin. Kritik ve ince kadrolu her biri için önceden destek mi olacağınıza, zaman mı katkılayacağınıza, bir vakfa mı katılacağınıza yoksa değiştirmeye mi hazırlanacağınıza karar verin. Bu, örtük bir tek hata noktasını, diğer her operasyonel risk gibi aynı standartta tutulan yönetilen bir ilişkiye çevirir (bölüm 2.18).

4. **Bir sonraki iç aracı açık kaynak yapmadan önce yıllarca ona bakıcılık etmeye hazır mısınız, yoksa bir lansman ve nihayetinde bir özür mü teslim ediyorsunuz?** Herkese açık bir yayın kalıcı bir taahhüttür: birinin ayıklaması gereken bir sorun izleyici, birinin izlemesi gereken bir güvenlik gelen kutusu ve birinin savunması gereken bir ad. Takımlar işe alıma ya da iyi niyete yardım için açık kaynağa uzanır, sonra eski sorunlarla terk edilmiş bir projenin, hiçbir şey yayımlamamaktan daha çok, inşa etmeyi umdukları itibara zarar verdiğini keşfeder. Kanıtı getirin: zaten yayımladığınız projeleri listeleyin ve her biri için açık sorun yaşını, adı konmuş bir bakımcının bütçelenmiş saatleri olup olmadığını, bir yönetişim modeli, tescilli bir ticari marka ve koordineli ifşa politikası olup olmadığını ve kodun paylaşmaya değer bir meta mı yoksa kapalı tutmanız gereken bir ayırt edici mi olduğunu gösterin (bölüm 10.12). Rakip değerlendirme, gerçek bakıcılığın ürüne harcayabileceğiniz mühendislik zamanına mal olmasıdır; bu yüzden dürüst seçim çoğu zaman daha az şey yayımlayıp onlara düzgün bakıcılık etmektir. Bir kurum için bu, lansmandan önce hukuki ve marka incelemesi demektir; kamu için, depo herkese açılmadan önce ticari markanın, ifşa kanalının ve varsayılan yayın istisna sürecinin netleşmiş olması demektir.

5. **Bir mühendisin bir bağımlılığı onaylatması ya da bir katkıyı temize çıkarması gerçekte ne kadar sürüyor ve bu, etrafınızdan dolaşmaktan daha mı yavaş?** Bir açık kaynak politikası, bir mühendisin bulabileceği en hızlı geçici çözümle doğrudan rekabet eder ve kodu kopyalamaktan yavaş her süreç bypass edilir; bu da ofisin önlemek için var olduğu görünmez gölge bağımlılıkları üretir. Gerilim kontrol ile olanak tanıma arasındadır: her elle inceleme bir denetim izi ekler ve nadir gerçek sorunu yakalar, ama aynı zamanda ortanca vakayı uyumlu yoldan iten gecikme ekler. Sayıları toplantıya getirin: standart bir bağımlılık ve standart bir katkı için ölçülmüş onay süresi, kararların otomatik ile insan tarafından ele alınan payı ve geçen çeyrekte gerçekten muhakeme gerektiren istisnaların sayısı. Her biri günlük küçük kararlar veren yüzlerce mühendisi olan bir kurumda iki günlük bir kuyruk sessizce binlerce bypass edilmiş incelemeye dönüşür; kamuda aynı gecikme, geçici çözümün atladığı kağıt izini gerektiren satın alma ve denetim yükümlülükleriyle çarpışır; bu yüzden çözüm daha büyük bir kapıyı kadrolamak değil, yaygın durumu otomatikleştirmektir.

6. **Hangi iç projeler InnerSource'tan en çok yararlanır ve bugün başka bir takımın size çekme isteği göndermesini ne engelliyor?** Açık kaynağı çalıştıran pratikler (herkese açık depolar, katkı rehberleri, liyakate göre inceleme, ilk yama için düşük engel), siloları kırarak, yeniden kullanımı yayarak ve insanları dışarıya katkıda bulunmak için kullanacakları iş akışının aynısında eğiterek güvenlik duvarının arkasında karşılığını verir. Rakip değerlendirme, bir iç projeyi açmanın bir katkı rehberi, yedek inceleme kapasitesi ve hangi kodun güvenlik ya da düzenleyici nedenlerle kısıtlı kalması gerektiğine dair bir karar talep etmesidir. Ayrıntıları getirin: yüksek değerli paylaşılan kütüphaneleri adlandırın, hangilerinin zaten bir iç katkı rehberi yayımladığını not edin ve bir takımlar arası çekme isteğinin bugün nasıl ele alındığını, karşılanıp karşılanmadığını ya da bir kuyrukta kaybolup kaybolmadığını anlatın. Bir kurum için getiri, birçok takım genelinde kaçınılan yinelenmiş iç yapımlarla ölçülür; kamu için aynı alışkanlık kurumlar arası yeniden kullanım olarak kurum sınırlarını aşar; böylece varsayılan yayın ve paylaşılan bileşenler kamu harcamasını çoğaltmak yerine yinelenmiş harcamayı azaltır.

## Sektör merceği

**Girişim.** Ofisi, komite değil tek sayfalık bir tüzükle haftada birkaç saatliğine adı konmuş tek bir mühendise verin. İzin verici lisansları varsayılan yapın, hatta bir tarayıcı kurun, yalnızca her yükseltmede gerçekten acıtan bir avuç özel yamayı yukarı akışa gönderin ve gerçekten vazgeçemeyeceğiniz, tek bakımcılı kütüphane için küçük bir aylık destek kurun. Burada hız kapsamdan daha önemlidir: kodu kopyalamaktan daha hızlı uyumlu bir yol, kimsenin izlemediği kapsamlı bir politikayı yener.

**Küçük işletme.** Özel bir OSPO kadrolamayacaksınız, bu yüzden zaten çalıştırdığınız araçlara gömülü kabiliyeti satın alın: lisans ve güvenlik açığı sorunlarını işaretleyen bir tarayıcı ve önceden incelenmiş bileşenlerden özenle seçilmiş bir katalog. İşi bir program olarak değil, lisans uyumu ve bağımlılık sağlığı hijyeni olarak çerçeveleyin: yazılım malzeme listenizde neyin olduğunu, her lisansın neyi gerektirdiğini ve hangi tek bakımcılı bağımlılığın ortadan kaybolursa acıtacağını bilin. Kendi tarama ve kataloglamanızı kurmak yerine satın almayı tercih edin.

**Kurumsal.** Küçük bir merkezi ofis ve ürün takımlarına yerleştirilmiş federe bir şampiyon ağı işletin; böylece politika tutarlı kalırken kararlar mühendislere yakın kalır. Lisans, güvenlik açığı ve ihracat taramasını otomatikleştirin, her mühendisi önceden onaylanmış bir katkıda bulunan sözleşmesiyle kapsayın ve onay süresini raporlanan bir metrik olarak izleyin. Kritik bağımlılıklarınızın arkasındaki vakıfları finanse edin, birçok depo genelinde InnerSource işletin ve tüm varlığı bireysel kararlar dağınıklığı olarak değil, sağlık ve etkileşim metrikleriyle bir portföy olarak yönetin.

**Kamu.** Varsayılan olarak açık kaynak ve kamu parası kamu kodu ilkesi altında çalışın: belgelenmiş bir güvenlik ya da gizlilik istisnası geçerli olmadıkça yeni hizmetleri herkese açık bir depoda yayımlayın. Takımlar inşa etmeden önce yeniden kullansın diye kurumlar arası bir katalog işletin, tedarikçilerin hakları saklı kalan yeniden kullanılabilir kod teslim etmesi için açık kaynak ve açık standart gereksinimlerini satın almaya yazın ve yayımladıklarınız için koordineli ifşayı ele alın. Birkaç kurumun bağlı olduğu paylaşılan kütüphanelerin bakımını finanse edin; böylece hiçbir tek takım tüm hükümetin güvendiği altyapıya sessizce sahip olmaz.

## Örnekler

**Girişim.** Yirmi kişilik bir girişim, baş platform mühendisini tek sayfalık bir tüzükle yarı zamanlı OSPO sahibi yapar. Basit bir tüketim politikası belirler (izin verici lisanslar önceden onaylı, copyleft incelenir, hatta bir tarayıcı), ve takımın açık kaynak bir kuyruk kütüphanesine karşı üç özel yama taşıdığını, her yükseltmede acılı biçimde yeniden uygulandığını fark eder. Üçünü de yukarı akışa gönderir; ikisi bir ay içinde kabul edilir ve yükseltme vergisini kalıcı olarak siler. Çoğunlukla mühendis çekmek için gerçek bir README, bir lisans ve bir güvenlik iletişim noktasıyla küçük bir iç aracı açık kaynak yapar ve ürünün bağlı olduğu tek bakımcılı ayrıştırıcı için aylık bir destek kurar. Bunların hiçbiri kadro gerektirmez, yalnızca adı konmuş bir sahip ve net bir görev gerektirir.

**Kurumsal.** Küresel bir banka, altı kişilik bir merkezi OSPO ve her ürün grubuna yerleştirilmiş federe bir açık kaynak şampiyonları ağı işletir. Merkezi takım politikayı, otomatik lisans ve ihracat uyumu taramasını ve her mühendisin ilk günden kapsandığı katkıda bulunan lisans sözleşmesini sahiplenir. Şampiyonlar yerel incelemeyi ele alır ve takımlarına katkı konusunda koçluk yapar. Banka, projeleri ticaret sistemlerinin temelini oluşturan birkaç vakfı finanse eder, bir çatalı sürdürmeyi bırakmak için yaygın kullanılan bir veri çerçevesine düzeltmeleri yukarı akışa katkılar ve her takımın bir diğerine çekme isteği gönderebilmesi için iki yüz iç depo genelinde InnerSource işletir. Standart bir katkı için onay süresi iki günün altındadır ve OSPO'nun üç ayda bir raporladığı bir metrik olarak izlenir.

**Kamu.** Ulusal bir dijital kurum, "varsayılan olarak açık kaynak" ve kamu parası kamu kodu yetkisi altında çalışır. OSPO'su, güvenlik ya da gizlilik için belgelenmiş bir istisna geçerli olmadıkça yeni hizmetleri herkese açık bir depoda yayımlar, kurumlar kodu inşa etmeden önce yeniden kullansın diye hükümetler arası bir katalog işletir ve hükümetin hakları saklı kalmak üzere tedarikçilerin yeniden kullanılabilir, iyi belgelenmiş kod teslim etmesi için açık kaynak ve açık standart gereksinimlerini satın almaya yazar. Ofis ayrıca yayımladığı kod için koordineli güvenlik ifşasını ele alır ve artık birkaç kurumun bağlı olduğu paylaşılan bir kimlik kütüphanesinin bakımını finanse eder; böylece hiçbir tek takım tüm hükümetin güvendiği bir bileşene sessizce sahip olmaz.

## İş gerekçesi: motivasyonlar, YG ve TSM

En net getiri, kaçınılabilir, pahalı sürprizlerin ortadan kaldırılmasıdır. Yönetilmeyen açık kaynak, kendi takvimlerinde gelen krizler üretir: bir devralma durum tespiti sırasında ortaya çıkan copyleft ihlali, ölü bir bileşenden acil geçiş, hiçbir envanterin listelemediği bir bağımlılığa kadar izlenen bir ihlal. OSPO bu düşük olasılıklı, yüksek maliyetli olayları düzenli, bütçelenmiş işe dönüştürür. Üstüne yukarı akışa göndermekten gelen tekrar eden tasarrufları ekleyin: emekli ettiğiniz her özel yama gelecekteki her yükseltmeyi vergilendirmeyi bırakır ve büyük bir varlık genelinde bu, ürün işine geri dönen gerçek mühendislik kapasitesine birikir.

[Toplam sahip olma maliyeti](https://en.wikipedia.org/wiki/Total_cost_of_ownership) defterinde ofis, koruduğu şeye göre ucuzdur. Maliyeti küçük bir takım, biraz tarama ve katalog aracı ve mütevazı bakımcı finansmanıdır. Bunu sahip olmamanın maliyetine karşı koyun: hukuki sorumluluk, başarısız ya da gecikmiş durum tespiti, güvenlik olayları, zaten açık kaynak olarak var olan şeylerin yinelenmiş iç yapımları ve kimsenin tutmayı seçmediği çatalların yavaş kanaması. Fiyatlandırması daha zor ama gerçek olan olumlu getiriler de var: bağlı olduğunuz bileşenlerin yönü üzerinde etki, inandırıcı bir açık kaynak varlığından gelen işe alım ve itibar avantajı ve mühendislerin yeniden inşa etmek yerine yeniden kullanması nedeniyle daha hızlı teslimat. Gerekçeyi liderliğe sunarken OSPO'yu, kod tabanınızın çoğunluğu için tedarik zinciri yönetimi olarak, üstüne stratejik bir temettüyle çerçeveleyin. Kamuda uyum boyutunu ekleyin, çünkü açıklık çoğu zaman zorunludur ve bunu iyi yapmak hem uyumsuzluktan hem de yinelenmiş kamu harcamasından kaçınır.

## Anti-kalıplar ve tuzaklar

- **Kapı olarak OSPO.** Yalnızca inceleyen ve engelleyen, asla olanak tanımayan bir ofis dolanılır; bu da önlemesi gereken gölge bağımlılıkları üretir.
- **Katkı tiyatrosu.** Onay sürecini kimsenin gerçekten katkıda bulunamayacağı kadar yavaş yaparken bir açık kaynak stratejisi duyurmak.
- **Terk edilmiş yayın.** Bir lansman blog yazısıyla bir proje yayımlamak, sonra hiçbir sorunu ayıklamamak; sessizlikten daha çok itibara zarar verir.
- **Çatalla ve unut.** Tek bir düzeltme için bir bağımlılığı çatallamak ve sonra onu sonsuza dek taşımak; yukarı akış güvenlik yamalarından uzaklaşmak.
- **Kırılgan bakımcılara bedavacılık.** Kritik tek bakımcılı bir kütüphaneye bağımlı olmak ve arkasındaki kişiyi asla finanse etmemek, teşekkür etmemek ya da ona yardım etmemek.
- **Ticari marka ihmali.** Bir projeyi adını korumadan yayımlamak, sonra bir çatalın ya da tedarikçinin itibarınız üzerinden ticaret yapmasını izlemek.
- **Yalnızca hukuk sahipliği.** OSPO'yu tamamen hukukta barındırmak; rehberliği mühendislik itibarı taşımaz ve takımlar onu dinlemeyi bırakır.
- **Gösteriş metrikleri.** Bağımlılık sağlığı, onay süresi ve emekli edilen özel yamalar yerine yıldızları ve basın anmalarını saymak.

## Olgunluk modeli

- **Düzey 1, Başlangıç:** Mühendisler açık kaynağı politika ve sahip olmadan ekler, yamalar ve ara sıra yayımlar. Tüketim, katkı ve yayın tepkisel ve plansızdır, bireysel girişime bağlıdır. Özel çatallar fark edilmeden birikir, hiç kimse hiçbir yukarı akış projesini finanse etmez ve durum tespiti sırasında bir lisans sorusunu kimse cevaplayamaz.
- **Düzey 2, Geliştirme:** Temel pratikler ortaya çıkar ama takıma göre değişir. Kaba bir tüketim politikası ve onaylı lisans listesi vardır ve birisi gevşekçe sorumludur, yine de katkı yavaştır ve vaka vakadır ve bazı gruplar diğerlerinden çok daha fazlasını yapar. Birkaç kritik bağımlılık bilinir, ama sürdürülebilirlik, yayınlar ve bakıcılık tutarsız kalır.
- **Düzey 3, Standartlaştırma:** Tüzüklü bir OSPO tüketimi, katkıyı, yayımlamayı ve topluluğu sahiplenir ve pratikler kurum genelinde belgelenmiş ve uygulanmıştır. Tarama ve yazılım malzeme listesi otomatiktir, önceden onaylanmış bir katkıda bulunan sözleşmesi ve hızlı bir onay yolu vardır, yayımlanan projeler gerçek yönetişim, ticari markalar ve güvenlik politikaları taşır ve InnerSource yayılmaktadır. Kamu takımları varsayılan olarak yayımlar.
- **Düzey 4, Yönetme:** Açık kaynak işlevi taban çizgilerine karşı ölçülür ve kontrol edilir. Onay süresi bir hedefe karşı izlenir, katkı hacmi ve yukarı akış kabul oranı raporlanır, bağımlılık sağlığı ve bakımcı sayısı panoları tek hata noktalarını işaretler, en riskli bağımlılıkların finanse edilmiş bakımcı kapsamı izlenir ve özel yamalar ile çatalların envanteri çeyrekten çeyreğe düşer. Yayımlanan projelerin ölçülmüş sorun yanıt süreleri vardır, istisnalar belirli bir ritimle gözden geçirilir ve yıldız gibi gösteriş metrikleri bunlar lehine bırakılır.
- **Düzey 5, Orkestrasyon:** Açık kaynak, mühendislik, hukuk, güvenlik ve satın alma planlamasıyla bütünleşmiş, sürekli uyarlanan yönetilen stratejik bir kabiliyettir. Katkı rutindir, kritik bakımcılar ve vakıflar finanse edilir, kurum iyi işleyen projelere bakıcılık eder ve bağlı olduğu ekosistemleri yönlendirir ve InnerSource normdur. Etkileşim ve sağlık metrikleri sürekli iyileştirmeyi besler ve portföy bağımlılıklar, riskler ve yetkiler değiştikçe yeniden dengelenir.

## Tartışma fikirleri

1. Olanak tanıyan bir OSPO ile kapı bekleyen bir OSPO arasındaki çizgi nerede ve hangisini kurduğunuzu dışarıdan nasıl anlarsınız?
2. Özel yamalarınızdan ya da çatallarınızdan hangilerini zorunluluktan değil alışkanlıktan taşıyorsunuz ve ilk üçünü yukarı akışa göndermek için ne gerekir?
3. Kritik bağımlılıkların listesi bütçeden uzun olduğunda hangi bakımcıları ve vakıfları finanse edeceğinize nasıl karar vermelisiniz?
4. Bir sonraki sürümünüzü ilk günden gerçek yönetişim, bir ticari marka ve koordineli ifşa politikasıyla yayımlamak zorunda olsaydınız gerçekte ne değişirdi?
5. Kamu okurları için, ilkeyi sessizce aşındırmadan kodu varsayılan yayından muaf tutmanın savunulabilir süreci nedir?
6. Hangi iç kütüphaneler InnerSource'tan en çok yararlanır ve bugün başka bir takımın size çekme isteği göndermesini ne engelliyor?

## Önemli çıkarımlar

- Bir OSPO, açık kaynakla tüm ilişkiyi sahiplenir: sorumlulukla tüketmek, yukarı akışa katkıda bulunmak, kendi projelerinizi yayımlamak ve bağlı olduğunuz bakımcıları sürdürmek.
- Yukarı akışa katkı stratejidir, hayırseverlik değil; özel yamaların tekrar eden vergisini siler, yön üzerinde etki satın alır ve işe almanıza yardım eder.
- Uyumlu yolu otomasyon ve özenle seçilmiş kataloglarla en hızlı yol yapın; böylece ofis mühendisleri kapı bekleyerek değil, olanak tanıyarak destekler.
- Kendi projelerinizi yalnızca gerçek yönetişim, seçilmiş bir lisans, korunan bir ticari marka ve koordineli güvenlik ifşasıyla yayımlayın, ya da hiç yayımlamayın.
- Üretim sisteminizin dayandığı kritik bakımcıları finanse edin ve onlara yardım edin, çünkü ortak kaynak kendi kendini sürdürmez.
- Açık kaynak işbirliğini şirket içine taşımak için InnerSource uygulayın ve kamuda varsayılan olarak açık olun, varsayılan olarak yayımlayın ve inşa etmeden önce yeniden kullanın.

## Kaynaklar ve ileri okuma

- Nadia Eghbal, *Working in Public: The Making and Maintenance of Open Source Software*
- Nadia Eghbal, *Roads and Bridges: The Unseen Labour Behind Our Digital Infrastructure*
- Karl Fogel, *Producing Open Source Software: How to Run a Successful Free Software Project*
- Danese Cooper and Klaas-Jan Stol (editors), *Adopting InnerSource: Principles and Case Studies*
- The Linux Foundation and TODO Group, *OSPO guides and Open Source Program Office resources*
- The Linux Foundation and TODO Group, *State of OSPOs and Open Source Management* (annual survey series)
- Heather Meeker, *Open (Source) for Business*
- Open Source Initiative, *The Open Source Definition* and approved-licence list
- Free Software Foundation Europe, *Public Money, Public Code* campaign materials
- U.S. Federal Source Code Policy and Code.gov guidance
