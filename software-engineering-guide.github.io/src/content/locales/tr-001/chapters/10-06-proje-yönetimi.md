# 10.6 Proje yönetimi

## Genel bakış ve motivasyon

[Proje yönetimi](https://en.wikipedia.org/wiki/Project_management), niyeti kısıtlar altında teslim edilmiş sonuçlara çevirme disiplinidir. İşin gerçekten bitmesi ve değer sunması için insanları, kapsamı, takvimi, maliyeti, riski ve kaliteyi koordine edersiniz. Yazılımda çoğu zaman şüpheyle karşılanır; gerçekliğin umursamadığı ağır planlara ve [Gantt çizelgelerine](https://en.wikipedia.org/wiki/Gantt_chart) bağlanır. Ama altta yatan ihtiyaç hiç ortadan kalkmaz. Birinin doğru işin doğru sırayla yapıldığından, bağımlılıkların yönetildiğinden, risklerin erken yüzeye çıktığından ve [paydaşların](https://en.wikipedia.org/wiki/Project_stakeholder) ne bekleyeceğini bildiğinden emin olması gerekir. Soru projelerin yönetilip yönetilmeyeceği değil, yükümlülüklerinizi karşılarken bunu *ne kadar hafif ve uyarlanabilir* yapabileceğinizdir.

Bunu neden açıkça ele alalım? Yazılım projeleri çarpıcı oranlarda başarısız olur ve tamamen teknik nedenlerden çok daha sık yönetim nedenleriyle başarısız olur: belirsiz kapsam, yönetilmeyen bağımlılıklar, ele alınmayan risk, yokluğu hissedilen paydaşlar ve kesin uzun vadeli tahminler fantezisi. Büyük programlar özellikle açıktır: birçok takım, tedarikçi ve çok çeyreklik ufuklarla küçük koordinasyon aksaklıkları birikir. İyi proje yönetimi büyük ölçüde taahhütleri dürüstçe vermenin, işi mantıklı biçimde parçalamanın ve sorunlar düzeltmesi hâlâ ucuzken yüzeye çıksın diye hızlı geri bildirim yaratmanın uygulamasıdır.

Kurumsal ve kamu bağlamları bahisleri yükseltir ve kısıtları değiştirir. Kurumlar stratejiye ve bütçe döngülerine karşı birbirine geçmiş girişimlerin portföylerini yönetir (bölüm 10.1). Hükümetler satın alma kuralları, çok yıllı ödenekler, yüklenici yönetimi ve kamusal hesap verebilirlik ekler. Orada tarihsel varsayılan (büyük, sabit kapsamlı, [şelale](https://en.wikipedia.org/wiki/Waterfall_model) sözleşmeleri) pahalı ve görünür başarısızlıklarla dolu uzun bir sicile sahiptir. Bu bölüm öngörülü, uyarlanabilir ve melez yaklaşımların hepsi için geçerli temelleri kapsar. Bölüm 10.7 (Çeviklik) uyarlanabilir teslimata derinlemesine girer, bölüm 10.1 ise tek projenin üstündeki portföy ve program yönetimini kapsar.

## Temel ilkeler

- **Etkinliği değil, sonucu yönetin.** Bitti, teslim edilmiş değer demektir; kapatılmış görevler değil.
- **Parçalayın ve sıralayın.** Küçük, sıralı, bağımlılık farkındalıklı iş, büyük patlama planlarından iyidir.
- **Tahminler söz değil, aralıktır.** Belirsizliği dürüstçe iletin.
- **Riski erken ve sürekli yüzeye çıkarın.** En ucuz sorun ilk yakalanandır.
- **Yöntemi işe uydurun.** Öngörülü, uyarlanabilir ya da melez: belirsizliğe ve kısıtlara uyan.
- **Durumu şeffaf yapın.** Görünür akış, güven veren raporlardan iyidir.
- **Paydaşlar takımın parçasıdır.** Müşterinin yokluğu bir proje riskidir.

## Öneriler

### Öngörülü, uyarlanabilir ya da melezi bilinçli seçin

Evrensel olarak doğru bir teslimat modeli yoktur; yöntemle bağlam arasında bir uyum vardır:

- **Öngörülü (plan odaklı, "şelale"):** kapsam baştan sabitlenir, sonra takvim ve maliyet türetilir. Gerçekten kararlı, iyi anlaşılmış gereksinimleri ve sert dış kısıtları (düzenleyici sertifikasyon, fiziksel entegrasyon) olan işe uyar. Başarısızlık biçimi, yazılım gereksinimlerinin kararlı olmadığı hâlde kararlıymış gibi davranmaktır.
- **Uyarlanabilir ([çevik](https://en.wikipedia.org/wiki/Agile_software_development)):** kapsam esner; süre ve maliyet, çalışan yazılım teslim eden ve öğrenmeyi içine alan kısa iterasyonlarda sabittir. Gereksinimlerin keşfedildiği çoğu ürün ve dijital hizmet işine uyar (bölümler 11.1, 10.7).
- **Melez:** öngörülü bir yönetişim kabuğunun içinde uyarlanabilir bir çekirdek; finansmanın, uyumun ve sözleşmenin kilometre taşları ve denetim istediği, teslimatın ise iterasyondan fayda gördüğü kurumsal ve kamu ortamlarında yaygın ve çoğu zaman doğrudur.

[PMBOK](https://en.wikipedia.org/wiki/Project_Management_Body_of_Knowledge) (Proje Yönetimi Bilgi Birikimi, [Project Management Institute](https://en.wikipedia.org/wiki/Project_Management_Institute)'tan) ve [PRINCE2](https://en.wikipedia.org/wiki/PRINCE2) (PRojects IN Controlled Environments) gibi çerçeveler öngörülü ve melez uygulamayı kodlar. Amaç, işin ihtiyaç duymadığı törenleri almadan disiplinlerini (roller, risk, aşama kapıları) ödünç almaktır.

### Kapsamı üçlü kısıta karşı yönetin

Kapsam, takvim ve maliyet kaliteyle sınırlanarak birlikte hareket eder: klasik ["demir üçgen"](https://en.wikipedia.org/wiki/Project_management_triangle). Üçünü de sabitleyip bedavaya kapsam ekleyemezsiniz. Bir şey esner ve aksini varsaymak [ölüm yürüyüşlerinin](https://en.wikipedia.org/wiki/Death_march_(project_management)) nasıl başladığıdır. Ödünleşimleri açık yapın ve *hangi* değişkenin esneyeceğine karar verin. Uyarlanabilir yöntemler süre ve maliyeti sabitler, kapsamı esnetir. Sabit fiyatlı sözleşmeler kapsamı ve maliyeti sabitler ve gerçekte, yönetmedikçe kaliteyi ya da takvimi esnetir. [Kapsam kaymasını](https://en.wikipedia.org/wiki/Scope_creep) hafif bir değişiklik süreciyle (bölüm 12.3) denetleyin ve her şeyi kaydırmak yerine *değerli bir çekirdeğe kapsam daraltmayı* tercih edin.

### Dürüstçe, aralıklarla tahmin edin ve yeniden öngörün

Tahmin, projelerin kendilerine en sık yalan söylediği yerdir. Tahminleri tek sayı değil, olasılıksal aralık olarak ele alın ve uzak, kötü anlaşılmış iş için genişletin (["belirsizlik konisi"](https://en.wikipedia.org/wiki/Cone_of_Uncertainty)). Göreli ve ampirik yöntemleri tercih edin: geçmiş çıktı ve çevrim süresi (bölümler 11.2, 11.3), kahramanca alttan yukarı tahminlerden daha iyi öngörür. Yapabildiğiniz yerde tahmini *ölçümle* değiştirin. Haftada 8 kalem kapatan bir takım, hikâye puanlarından bağımsız olarak 40 kalem için yaklaşık 5 hafta harcar ([Little Yasası](https://en.wikipedia.org/wiki/Little%27s_law) yine: teslim süresini tahminler değil, çıktı ve devam eden iş belirler). Gerçeklik geldikçe sürekli yeniden öngörün. Hiç değişmeyen bir plan yönetilmiyordur.

### Bağımlılıkları ve kritik yolu yönetin

Ölçekte baskın risk nadiren tek bir takımın hızıdır. Risk, *takımlar ve tedarikçiler arasındaki bağımlılıklardır*. Bunları açıkça haritalayın, [kritik yolu](https://en.wikipedia.org/wiki/Critical_path_method) (en erken bitişi belirleyen diziyi) belirleyin ve en uzun ve en riskli bağımlılıklara önce saldırın. Yapabildiğiniz yerde bağlaşımı azaltın (kaldırılmış bir bağımlılık, izlenen bir bağımlılıktan daha değerlidir) ve takımların paralel ilerleyebilmesi için net arayüzler ve sözleşmeler kullanın (bölümler 1.2, 2.3). Takımlar arası programlarda düzenli bir bağımlılık ve risk senkronizasyonu, kimsenin okumadığı bir durum raporundan iyidir.

### Yaşayan bir risk kaydı tutun

Risk yönetimi en yüksek kaldıraçlı proje yönetimi etkinliğidir ve en sık atlananıdır. Basit, yaşayan bir **[risk kaydı](https://en.wikipedia.org/wiki/Risk_register)** tutun: her risk olasılığı, etkisi, sahibi ve hafifletme ya da olağanüstü durum planıyla (bölüm 12.3). Düzenli gözden geçirin, geçmiş riskleri kapatın ve ortaya çıktıkça yenilerini ekleyin. Riskleri (olabilir) sorunlardan (zaten oluyor) ve kararlardan (bölüm 1.6) ayırın. Amaç bir belge değildir. Amaç ileriye bakma alışkanlığıdır; böylece sorunları teslim tarihinde keşfetmek yerine önceden görürsünüz.

### Paydaşları dahil edin ve şeffaf iletişim kurun

"Sürpriz" proje başarısızlıklarının çoğu, dinlenmeyen birine erkenden görünürdü. Paydaşları belirleyin, kaygılarını anlayın ve onları gerçekten dahil tutun. Müşterinin yokluğu başlı başına en büyük risklerden biridir. Durumu, iyimserliği ödüllendiren yeşil-sarı-kırmızı raporlarla değil, *şeffaf akışla* (görünür panolar, birikimli yanma çizelgeleri, gösterilen çalışan yazılım) iletin. Dürüstçe ve erken yükseltin. İyi yönetilen bir proje kötü haberin hızlı yol almasını sağlar.

## Ödünleşimler: artılar ve eksiler

| Yaklaşım | Artılar | Eksiler |
|---|---|---|
| **Öngörülü / şelale** | Öngörülebilir kapsam ve maliyet; sözleşme ve denetim dostu | Belirsiz gereksinimlere kötü uyum; geç geri bildirim; büyük patlama riski |
| **Uyarlanabilir / çevik** | Hızlı geri bildirim; değişikliği içine alır; erken değer | Kapsam ve maliyeti baştan sabitlemek daha zor; ilgili bir müşteri gerekir |
| **Melez** | Yönetişim içinde iterasyon; kurumsal ve kamuya uyar | Ritimler arasında gerilim; iki yükün de ek yükünü devralabilir |
| **Ayrıntılı baştan tahminler** | Planlayıcılara ve fon verenlere rahatlık | Kesin biçimde yanlış; üretmesi pahalı; hızla eskir |
| **Ampirik öngörü (akış metrikleri)** | Zemine oturmuş, kendini düzelten | Geçmiş ve disiplin gerektirir; daha az "kesin" görünür |
| **Ağır risk/süreç töreni** | Kapsamlı; yüksek riskli programlar için iyi | Küçük takımları yavaşlatır; kutu işaretlemeye dönüşebilir |

Merkezî gerilim **öngörülebilirlik ile uyarlanabilirlik** arasındadır. Fon verenler, sözleşmeler ve denetimler kesin taahhütler ister. Belirsiz yazılım işi öğrenmek için alan ister. Bunu Çevik'in (bölüm 10.7) yaptığı gibi çözün: kapsamın esnemesine izin verirken sonuçlara ve teslim tarihlerine kesin taahhüt verin ve teslimatı dondurmadan denetimi tatmin etmek için melez yönetişim kullanın.

## Takımınızla tartışılacak sorular

1. **Uyarlanabilir teslimat takımlarını, ikisinin de ek yükünü devralmadan öngörülü bir yönetişim kabuğuna nasıl saracaksınız?** Melez, finansman döngülerinin, uyumun ve sözleşmenin kilometre taşları ve denetim istediği, teslimatın ise iterasyondan fayda gördüğü kurumsal ve kamu ortamlarında yaygın ve çoğu zaman doğrudur. Risk gerçektir: kötü tasarlanmış bir melez şelalenin ağır belgelemesini ve çevikliğin törenlerini aynı anda devralır ve takımlar iki ritmin birbiriyle savaşmasının sürtünmesini hisseder. Kanıt getirin: finansman kapılarınızın, uyum kontrol noktalarınızın ve sözleşme kilometre taşlarınızın gerçekte nereye düştüğünü haritalayın ve her birinin teslimat işinin başka türlü üretmediği bir belge isteyip istemediğini kontrol edin. Cevap, iterasyonun denetimle savaşmak yerine onu tatmin etmesini sağlamalıdır: ayrı raporlar derlemek için durmak yerine gösterilen çalışan artımları ve yaşayan bir risk kaydını yönetişim ritmine besleyin. PRINCE2 gibi bir çerçevenin disiplinini, işin ihtiyaç duymadığı tören olmadan ödünç alın.

2. **Proje durumunuz şeffaf akış mı yoksa iyimserliği ödüllendiren yeşil-sarı-kırmızı raporlar mı?** Sürpriz başarısızlıkların çoğu dinlenmeyen birine erkenden görünürdü ve karpuz durumu (dışı yeşil, içi kırmızı) dürüst kötü haberin teslim tarihine kadar gömülü kalmasının yoludur. Güven veren raporları görünür panolarla, birikimli yanma çizelgeleriyle ve gösterilen çalışan yazılımla değiştirin ve erkenden yükseltmeyi kariyer riski değil, güvenli bir eylem yapın. Kanıt getirin: en son sorunlu projenize bakın ve ilk uyarı işaretinin ne zaman var olduğunu, liderliğin ne zaman duyduğuyla karşılaştırarak sorun. Müşterinin yokluğu başlı başına en büyük risklerden biridir; bu yüzden gerçekten döngüde ilgili bir paydaşın olup olmadığını, yoksa yanlış şeye kendinden emin biçimde mi yöneldiğinizi kontrol edin. İyi yönetilen bir proje kötü haberin hızlı yol almasını sağlar ve çözüm araçlar kadar kültüreldir.

3. **Takvim ve maliyet hareket etmeyi bıraksa hangi asgari değerli çekirdeğe kapsam daraltacağınızı biliyor musunuz?** Kapsam, takvim ve maliyet kaliteyle sınırlanarak birlikte hareket eder ve fon verenler üçünü de sabitlediğinde kalite sessiz tahliye vanası olur ve ölüm yürüyüşleri başlar. Uyarlanabilir yöntemler süre ve maliyeti sabitler, kapsamı esnetir; bu ancak hangi diliminin gerçek değer sunduğuna ve hangi özelliklerin pazarlığa açık olduğuna önceden karar verdiyseniz işe yarar. Kanıt getirin: mevcut sürümünüz için yayınlanması gereken çekirdeği ve önce keseceğiniz listeyi adlandırabiliyor musunuz, yoksa her özellik sessizce zorunlu mu sayılıyor? Cevap her şeyi kaydırmak yerine değerli bir çekirdeğe kapsam daraltmanıza izin vermeli ve baskı gelmeden önce, teslim tarihinde doğaçlama değil, çözülmüş olmalıdır. Kalanını hafif bir değişiklik süreciyle denetleyin; böylece kapsam kayması güvendiğiniz payı yemez.

4. **Şu anda kritik yolunuzda hangi takımlar arası bağımlılık var ve onu kaldırmanın ya da riskini azaltmanın sahibi kim?** Ölçekte baskın tehdit nadiren tek bir takımın hızıdır; en erken olası bitişi belirleyen, takımlar ve tedarikçiler arasındaki bağımlılıklar dizisidir. Kimse mevcut kritik yol bağımlılığını adlandıramıyorsa, tarihinizi gerçekten belirleyen şey izlenmeden kayarken yerel ilerlemeyi yönetiyorsunuz demektir. Kanıt getirin: hangi devirlerin hangilerini beslediğini, en uzun zincirin nerede koştuğunu ve hangi halkaların hâlâ kurulmamış ya da sözleşmesel olarak engellenmiş olduğunu gösteren bir bağımlılık haritası ve her riskli halka için adı konmuş bir sahip. En uzun ve en riskli bağımlılıklara önce saldırmayı ve yapabildiğiniz yerde bağlaşımı kaldırmayı hedefleyin; çünkü silinmiş bir bağımlılık, izlenen bir bağımlılıktan daha değerlidir. Kurumsal ve kamu programlarında en zor halkalar çoğu zaman tedarikçi ya da kurum sınırlarını aşar; bu yüzden her iki tarafta hesap verebilir sahibi adlandırın ve sözleşmenin eylemelerine izin verdiğini doğrulayın, yoksa bağımlılık kamusal bir gecikmeye dönüşene kadar çözümsüz kalır.

5. **Gerçeklik geldikçe nasıl yeniden öngörüyorsunuz ve bir kayma işi finanse eden kişilere ne kadar çabuk görünür oluyor?** Hiç değişmeyen bir plan yönetilmiyor, savunuluyordur ve kanıtın ötesinde savunulan tek sayılık bir tarih, projelerin teslim tarihine kadar sessizce kaymasının yoludur. Yapabildiğiniz her yerde tahmini ölçümle değiştirin; kahramanca alttan yukarı tahminler yerine geçmiş çıktı ve çevrim süresinden öngörün ve uzak, kötü anlaşılmış iş için aralığı genişletin. Kanıt getirin: gerçek haftalık tamamlama hızınız, mevcut iş listesi boyutu ve bunlardan çıkan öngörülen bitiş, liderliğin şu an inandığı tarihle karşılaştırılmış olarak. Cevap fon verenlere çöküşe kadar tutan sabit bir tarih yerine her döngüde gördükleri dürüst, daralan bir projeksiyon vermelidir. Hükümet ve ödeneğe bağlı diğer ortamlarda kaymayı erken yüzeye çıkaran bir öngörü, kuralların içinde yeniden kapsamlandırmanıza ya da temel çizgiyi yeniden belirlemenize izin verir; gizli bir kayma ise bir denetim başarısızlığı ve manşet olur.

6. **Gerçek yükümlülüklerinizi yine de karşılayan en hafif süreç nedir ve tören riski azaltmaktan nerede kopmuştur?** Hem az yönetmenin hem çok yönetmenin gerçek maliyeti vardır: bir yanda kaos, yeniden iş ve kaçırılmış bağımlılıklar, öbür yanda riski düşürmeden teslimatı yavaşlatan kutu işaretleme. Gerilim şudur: denetim, uyum ve sözleşme şartları gerçek gereksinimler getirir, ama takımlar her ritüeli yeri hak etmeyi bıraktıktan çok sonra da tutma eğilimindedir. Kanıt getirin: tekrarlayan her rapor, kapı ve toplantı için ele aldığı belirli yükümlülüğü ya da riski adlandırın ve hiçbirine kimsenin izleyemediklerini işaretleyin. Cevap, yalnızca güvence üreten töreni emekliye ayırırken gerçek bir denetçiyi ya da fon vereni tatmin eden ürünleri korumanıza izin vermelidir. Kurumsal ve kamu bağlamlarında her töreni hizmet ettiği adı konmuş ödenek, satın alma ya da düzenleyici kurala eşleyin; böylece kalanını kesmeyi uyumun ne istediğini tahmin etmek yerine denetime karşı savunabilirsiniz.

## Sektör merceği

**Girişim.** Neredeyse hiç törensiz ama gerçek disiplinle yönetin. Sürümü küçük sıralı dilimlere bölün, kapsamın değerli bir çekirdeğe esnemesine izin verirken bir lansman tarihine söz verin ve kurucuları tek tarih yerine aralıkla bilgilendirip her hafta gerçekte kapattığınız dilim sayısından yeniden öngörün. Tarihi batırabilecek tek bağımlılığı sahibi ve yedek planıyla adlandıran, paylaşılan bir belgedeki on satırlık risk kaydı herhangi bir araçtan değerlidir; çünkü en kıt kaynağınız dikkattir ve geç fark ettiğiniz bir kayma şirketi bitirebilir.

**Küçük işletme.** Proje yöneticiniz ve payınız az; bu yüzden bir yönetişim ofisi kurmak yerine zaten kullandığınız araçlara yaslanın. İşi tek bir görünür panoda izleyin, kısa bir yaşayan risk listesi tutun ve süreci sıfırdan kurmak yerine bir zamanlama ya da bilet ürünü satın almayı tercih edin. Sürümün yapılmaya değer olması için hangi tek özelliğin yayınlanması gerektiğine baştan karar verin; çünkü takvim sıkıştığında kapsamı o anda pazarlık edecek boş insanlarınız olmayacak.

**Kurumsal.** Sorun birçok takım, tedarikçi ve finansman döngüsü boyunca koordinasyondur. Uyarlanabilir takımları öngörülü bir yönetişim kabuğuna sarın, ayrı raporlar derlemek yerine gösterilen artımları ve yaşayan bir risk kaydını kilometre taşı ritmine besleyin ve kritik yol keşfedilmek yerine yönetilsin diye takımlar arası bir bağımlılık haritası tutun. Liderliğin projeleri iyimser sabit tarihler yerine dürüst, daralan projeksiyonlar üzerinden karşılaştırabilmesi için aralık tabanlı, ampirik olarak yeniden öngörülen tahminleri portföy genelinde standartlaştırın.

**Kamu.** Satın alma kuralları, çok yıllı ödenekler ve kamusal hesap verebilirlik her tercihi şekillendirir. Uzak bir devreye almayla tek bir sabit fiyatlı, sabit kapsamlı şelale sözleşmesi yerine, ödenekleri ve denetimi tatmin eden bir yönetişim çerçevesi altında uyarlanabilir biçimde teslim edilen modüler, sonuç tabanlı artımları tercih edin. Yaşayan bir risk kaydı ve şeffaf, gösterilen artımlar denetçilere ve yasa koyuculara gerçek görünürlük verir ve sabit finansman içinde kapsamı değerli bir çekirdeğe esnetmek, her şeyi tek bir tarihe riske atmak yerine yararlı yeteneği erken yayınlamanıza izin verir.

## Örnekler

**Girişim.** İlk ücretli ürününü yayınlamak için yarışan yedi kişilik bir girişim, projeyi neredeyse hiç törensiz ama gerçek disiplinle yönetir. Sürümü küçük sıralı dilimlere böler, her özelliği vaat etmek yerine kapsamın değerli bir çekirdeğe esnemesine izin verirken bir lansman tarihine söz verir ve kurucuları tek tarih yerine aralıkla bilgilendirip takımın gerçekten kapattığı dilim sayısından her hafta yeniden öngörür. Paylaşılan bir belgedeki on satırlık risk kaydı, tarihi batırabilecek tek bağımlılığı, bitmemiş bir ödeme entegrasyonunu, bir sahip ve bir yedek planla adlandırır; böylece en büyük tehdit teslim tarihinde keşfedilmek yerine izlenir.

**Kurumsal.** Kredi başvuru platformunu değiştiren bir banka melez bir program yürütür: üç aylık finansman kilometre taşları ve uyum kapıları olan öngörülü bir kabuk, iki haftada bir çalışan artımlar teslim eden uyarlanabilir takımları sarar. Takımlar arası bir bağımlılık haritası, paylaşılan bir kimlik hizmetinin kritik yolda olduğunu ortaya çıkarır. Bu yüzden program onu ilk sıraya koyar ve riskini azaltır, geç bir çağlayanı önler. Tahminler aralık olarak ifade edilir ve gerçek çıktıdan aylık yeniden öngörülür; böylece liderlik sessizce kayan sabit bir tarih yerine dürüst, daralan bir projeksiyon görür.

**Kamu.** Bir kurum, tek bir sabit fiyatlı, sabit kapsamlı şelale sözleşmesini (birkaç kamusal başarısızlığın ardındaki kalıp) bırakıp modüler satın almaya geçer: ödenekleri ve denetimi tatmin eden bir yönetişim çerçevesi altında uyarlanabilir biçimde teslim edilen daha küçük, sonuç tabanlı artımlar. Yaşayan bir risk kaydı ve şeffaf, gösterilen artımlar denetçilere ve yasa koyuculara gerçek görünürlük verir. Kapsam sabit finansman içinde değerli bir çekirdeğe esnediği için program, her şeyi tek bir uzak devreye almaya riske atmak yerine yararlı yeteneği erken yayınlayabilir (bölümler 10.1, 10.3).

## İş gerekçesi: motivasyonlar, YG ve TSM

İyi proje yönetiminin getirisine **önlenen başarısızlık** hâkimdir. Büyük yazılım projelerinin geç kalma, bütçeyi aşma ya da iptal edilme olasılığı, özgün sabit planı tutturma olasılığından çok daha yüksektir ve kayıplar muazzamdır: batık maliyet, artı vazgeçilen değer, artı hükümette kamusal ve siyasi zarar. Buradaki disiplinler (dürüst tahmin, bağımlılık yönetimi, erken risk çalışması, ilgili paydaşlar ve uyarlanabilir kapsam) tam da bir projeyi başarısızlık eğrisinden çıkaranlardır. Büyük bir aşımın ya da iptalin olasılığındaki mütevazı bir düşüş bile projeyi iyi yönetmenin maliyetini gölgede bırakır.

**Toplam sahip olma maliyetinde**, hafif, uyarlanabilir yönetim işin ömrü boyunca maliyeti düşürür. Hızlı geri bildirim pahalı hataları erken yakalar. Artımlı teslimat değer getirmeye daha erken başlar ve bu YG zamanlamasını iyileştirir. Şeffaf akış, ağır yönetişimin getirdiği raporlama ek yükünü azaltır. Hem *az* yönetmenin (kaos, yeniden iş, kaçırılmış bağımlılıklar) hem *çok* yönetmenin (teslimatı yavaşlatan tören) gerçek maliyeti vardır. Amaç, gerçek yükümlülüklerinizi karşılayan en hafif süreçtir. Liderliğe gerekçeyi, yakın zamandaki sorunlu bir projenin tam yüklü maliyetini, bir risk kaydının, bir bağımlılık haritasının ve dürüst aralık tabanlı öngörülerin sıfıra yakın maliyetiyle karşılaştırarak sunun.

## Anti-kalıplar ve tuzaklar

- **Her şeyi sabitleyen planlar:** kapsam, takvim ve maliyet hepsi kilitli, kalite sessiz tahliye vanası.
- **Söz olarak tahminler:** tek sayılık tarihler taahhüt sayılıp sonra kanıtın ötesinde savunulur.
- **Bağımlılıkları görmezden gelmek:** her takımın hızını yönetirken takımlar arası kritik yol kayar.
- **Risk kaydı tiyatrosu:** bir kez oluşturulup hiç tekrar bakılmayan bir belge.
- **Karpuz durumu:** dışı yeşil, içi kırmızı; iyimserlik dürüstlükten çok ödüllendirilir.
- **Yok müşteri:** ilgili paydaş yok, bu yüzden yanlış şey kendinden emin biçimde inşa edilir.
- **Büyük patlama teslimat:** her şey sonda entegre edilip yayınlanır, riski azamiye çıkarır (bölüm 11.2 ile karşılaştırın).
- **Kendi uğruna süreç:** riski azaltmadan çaba tüketen tören ve raporlar.

## Olgunluk modeli

- **Düzey 1 (Başlangıç):** Projeler kahramanlık ve umutla yürür; kapsam, risk ve bağımlılıklar varsa gelişigüzel yönetilir; tahminler kanıtın ötesinde savunulan tek sayılardır; sürprizler teslim tarihinde gelir.
- **Düzey 2 (Geliştirme):** Temel planlama, durum raporlama ve bir risk listesi bazı projelerde var, bazılarında yok; teslimat yöntemi uyuma göre değil alışkanlıkla seçilir; tahmin ve bağımlılık izleme takımdan takıma değişir, bu yüzden uygulama kurum genelinde tutarsızdır.
- **Düzey 3 (Standartlaştırma):** Belgelenmiş bir yaklaşım kurum genelinde uygulanır: teslimat yöntemi işe uyacak biçimde seçilir, kapsam üçlü kısıta karşı yönetilir, her projede yaşayan bir risk kaydı ve bağımlılık haritası beklenir ve tahminler aralık tabanlıdır ve ilgili paydaşlarla yeniden öngörülür.
- **Düzey 4 (Yönetme):** Teslimat temel çizgilere göre ölçülür ve denetlenir. Çıktı, çevrim süresi, öngörü doğruluğu, bağımlılık ve risk kapatma oranları ile takvim ve maliyet sapması proje başına izlenir ve portföy genelinde toplanır; projeksiyonlar ampirik ve daralandır; kaymalar erken yüzeye çıkar ve iyimserlik yerine kanıta dayanarak yeniden kapsamlandırmayı ya da temel çizgiyi yeniden belirlemeyi tetikler.
- **Düzey 5 (Orkestrasyon):** Proje yönetimi portföy, finansman ve risk planlamasıyla bütünleşiktir ve sürekli iyileştirilir. Melez yönetişim teslimatı yavaşlatmadan denetimi tatmin eder, takımlar ve tedarikçiler arası bağımlılıklar öngörülü biçimde yönetilir, retrospektifler ölçülmüş değişikliği uygulamaya geri besler ve kurum kısıtlar ve öncelikler değiştikçe yöntemlerini uyarlar ve işi yeniden dengeler.

## Tartışma fikirleri

1. Mevcut girişimlerinizin her biri gerçekte hangi teslimat yöntemine (öngörülü, uyarlanabilir, melez) ihtiyaç duyuyor ve kullandığınızla örtüşüyor mu?
2. En son bir tarihe söz verdiğinizde bu bir aralık mıydı yoksa tek bir sayı mı ve bu beklentileri nasıl şekillendirdi?
3. Şu anda takımlarınız arasındaki kritik yol bağımlılığı nedir ve riskini azaltmanın sahibi kim?
4. Risk kaydınız yaşayan bir alışkanlık mı yoksa tek seferlik bir belge mi?
5. Kapsam, takvim ve maliyet hepsi sabitken kalite baskıyı nerede sessizce emiyor?
6. Tahmini ölçülmüş çıktıyla değiştirseniz öngörüleriniz nasıl değişirdi?

## Önemli çıkarımlar

- Proje yönetimi, niyeti kapsam-takvim-maliyet-kalite kısıtı altında teslim edilmiş sonuçlara çevirir.
- **Yöntemi işe uydurun:** öngörülü, uyarlanabilir ya da melez ve kurumsal/kamuda melez yönetişimi tercih edin.
- **Tahminleri aralık** olarak ele alın, **ampirik akış metriklerinden** yeniden öngörün ve tek sayılık tarihlerin yalana dönüşmesine izin vermeyin.
- **Bağımlılıklar ve risk** ölçekteki baskın başarısızlık biçimleridir: ikisini de sürekli haritalayın ve yönetin.
- **Paydaşları** dahil tutun ve durumu **şeffaf** yapın; kötü haberin hızlı yol almasını sağlayın.
- YG önlenen başarısızlıktır; yükümlülüklerinizi karşılayan en hafif süreç kazanır. Bkz. bölümler 10.7 (Çeviklik), 10.1 (portföy ve program yönetimi), 11.2 (teslimat) ve 11.3 (kuyruk kuramı).

## Kaynaklar ve ileri okuma

- Project Management Institute, *A Guide to the Project Management Body of Knowledge (PMBOK Guide)*.
- AXELOS, *Managing Successful Projects with PRINCE2*.
- Frederick Brooks, *The Mythical Man-Month* (why adding people to a late project makes it later).
- Tom DeMarco and Timothy Lister, *Peopleware* and *Waltzing with Bears* (risk management).
- Steve McConnell, *Software Estimation: Demystifying the Black Art*.
- Daniel Vacanti, *Actionable Agile Metrics for Predictability* (empirical forecasting).
- Standish Group, *CHAOS Report* (software project outcomes, read critically).
- U.S. Digital Service, *Digital Services Playbook*; UK Government, *Government Service Standard* (modern public-sector delivery).
- Bent Flyvbjerg and Dan Gardner, *How Big Things Get Done* (megaproject delivery).
