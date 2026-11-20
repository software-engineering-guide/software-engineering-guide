# 1.5 Karar alma ve yönetişim

## Genel bakış ve motivasyon

Her yazılım sistemi binlerce kararın toplamıdır: hangi [veritabanı](https://en.wikipedia.org/wiki/Database), hangi mimari, hangi kütüphane, inşa etmek mi satın almak mı, borca ne zaman girilir ve ne zaman ödenir. Yönetişim, bu kararları iyi ve tutarlı biçimde nasıl alacağınız, doğru insanları darboğaz yaratmadan nasıl dahil edeceğiniz ve gelecekteki takımlar aynı şeyi yeniden öğrenmeye mahkûm olmasın diye gerekçeyi nasıl koruyacağınızdır. Küçük bir takımda kararlar konuşmada alınır ve ortak hafızada yaşar. Ölçekte o hafıza buharlaşır. İnsanlar ayrılır, takımlar yeniden yapılanır ve kritik bir seçimin ardındaki "neden" kaybolur; halefler ya onu körü körüne taklit etmek ya da körü körüne sökmek zorunda kalır. İyi yönetişim, kararları büyük ve değişen bir kuruluşta görünür, bilinçli ve kalıcı kılan makinedir.

Büyük takımlar için temel zorluk özerklik ile uyum arasında denge kurmaktır. Tüm kararları merkezi bir kurula iterseniz tutarlılık elde edersiniz, ama felç edici darboğazlar ve yetkisizleştirilmiş takımlar pahasına. Tüm kararları aşağı iterseniz hız elde edersiniz, ama kaos pahasına: uyumsuz teknolojiler, yinelenen çaba ve tekrarlanan hatalar. Olgun cevap ne merkezileşme ne de anarşidir. Katmanlı bir modeldir. Takımlar çoğu şeyi iyi işaretlenmiş bir "asfalt yol" içinde yerel olarak karara bağlar; hafif, şeffaf bir süreç ise gerçekten kesişen ve geri döndürmesi zor seçimleri yönetir. Amaç iyi kararları kolay varsayılan yapmak ve kıt yönetişim dikkatini yalnızca gerçekten önemli olduğu yere harcamaktır.

Kurumsal ve kamu kuruluşları daha yüksek riskler taşır. Belgelenmiş, savunulabilir kararlar talep eden denetçileri, düzenleyicileri ve gözetim organlarını tatmin etmek zorundadırlar. Kötü bir mimari seçimin ya da yönetilmeyen bir [teknik borç](https://en.wikipedia.org/wiki/Technical_debt) yığınının onlara on yıl boyunca yük olabileceği uzun zaman ufuklarında çalışırlar. Ve tedarik ve uyum yükümlülükleri, yap ya da satın al kararlarını özellikle sonuçlu ve geri döndürülmesi zor kılar. Bu kuruluşlar için disiplinli, iyi kaydedilmiş karar alma kendi başına bir bürokrasi değildir. Risk yönetimi, kurumsal bellek ve hesap verebilirliğin temelidir.

## Temel ilkeler

- Kararları ve gerekçelerini kaydedin; gerekçesiz bir karar bir yükümlülüktür.
- Kararları, net korkuluklar içinde, bağlama sahip en alt düzeye itin.
- Sürecin ağırlığını kararın ağırlığı ve geri döndürülebilirliğiyle eşleştirin.
- Geri döndürülebilir ("iki yönlü kapı") ile geri döndürülemez ("tek yönlü kapı") kararları ayırt edin ve farklı yönetin.
- Vaka başına onaylar yerine asfalt yolları ve varsayılanları tercih edin.
- Teknik borcu gizlenecek ahlaki bir kusur değil, yönetilen bir portföy olarak ele alın.
- Yönetişimi şeffaf kılın; gizli karar alma güvensizlik ve yeniden iş doğurur.

## Öneriler

### Mimari Karar Kayıtlarını ve orantılı bir RFC sürecini benimseyin

[Mimari Karar Kaydı](https://en.wikipedia.org/wiki/Architectural_decision) (ADR), tek bir önemli kararı yakalayan kısa, değiştirilemez bir belgedir: bağlamı, değerlendirilen seçenekleri, yapılan seçimi ve sonuçları. ADR'leri sürüm kontrolünde kodun yanında saklayın, böylece gerekçe sistemle birlikte seyahat eder. Alınmadan önce girdi gerektiren kararlar için hafif bir [RFC](https://en.wikipedia.org/wiki/Request_for_Comments) (yorum talebi) süreci kullanın: bir öneri dolaştırın, sınırlı bir süre boyunca yorum çağrısı yapın, sonra karar verin ve kaydedin. İkisini de hafif tutun. Değer, ayrıntılı şablonlarda değil, düşünmede ve kalıcı kayıttadır. ADR'ler ve RFC'ler birlikte örtük, unutulmuş gerekçeyi aranabilir bir kurumsal belleğe dönüştürür.

### Kapı bekçileriyle değil, asfalt yollarla yönetin

Her kararı tek tek incelemek yerine bir "asfalt yol"a yatırım yapın: takımların az sürtünme ve bol destekle benimseyebileceği, kutsanmış, iyi desteklenen varsayılanlar kümesi; onaylı diller, çerçeveler, dağıtım hatları ve kalıplar. Asfalt yolda kalan takımlar az yönetişime ihtiyaç duyar, çünkü güvenli, uyumlu seçim aynı zamanda kolay olandır. Ayrılmak için gerçek bir nedeni olan takımlar ayrılabilir, ama ek sorumluluğu ve hafif bir incelemeyi üstlenirler. Bu "altın yol" modeli, her şeyi onaylayan merkezi bir kuruldan çok daha iyi ölçeklenir, çünkü yönetişimi vaka başına kapı bekçiliğinden iyi tasarlanmış varsayılanlara kaydırır.

### Mimari inceleme kurullarını ölçülü ve şeffaf kullanın

Bir mimari inceleme kurulunun ya da eşdeğerinin en büyük, en çok kesişen ya da en geri döndürülemez kararlar ve asfalt yolu tanımlayan standartları belirlemek için meşru bir rolü vardır. Kapsamını dar, ölçütlerini yayımlanmış ve sürecini hızlı ve danışmanlık niteliğinde tutun; rutin iş için zorunlu bir darboğaz yapmayın. Kurulun işi tutarlılığı gözetmek ve bilgiyi paylaşmaktır, her seçimi onaylamak değil. Bir kurul her projenin içinde beklemesi gereken bir kuyruğa dönüştüğünde başarısız olmuştur. Agresifçe yetki devredin ve merkezi incelemeyi gerçekten hak eden birkaç karara saklayın.

### Yap-satın al-benimse kararını bilinçli bir analiz haline getirin

Her önemli yetenek için üç yolu tartın: dahili olarak inşa etmek, ticari bir ürün satın almak ya da bir [açık kaynak](https://en.wikipedia.org/wiki/Open-source_software) çözüm benimsemek. Yetenek gerçek bir farklılaştırıcıysa ve misyonunuzun merkezindeyse inşa edin. Başkalarının daha iyi yaptığı ayrışmamış yetenekleri satın alın ya da benimseyin. Yalnızca başlangıç fiyatını değil, [toplam sahip olma maliyetini](https://en.wikipedia.org/wiki/Total_cost_of_ownership) (TSM) sayın. Satın almak lisans, entegrasyon ve [kilitlenme](https://en.wikipedia.org/wiki/Vendor_lock-in) maliyetleri doğurur. İnşa etmek sürekli bakım ve kadro doğurur. Açık kaynak benimsemek destek ve güvenlik takibi yükümlülükleri doğurur. Koşullar değiştiğinde yeniden ele alabilmek için kararı ve varsayımlarını bir ADR olarak kaydedin.

### Teknik borcu bir portföy olarak yönetin

Teknik borç doğası gereği kötü değildir. Bazen daha erken yayımlamak için onu üstlenmek doğru karardır. Kötü olan, yönetilmeyen, görünmez, unutulmuş borçtur. Önemli borcun açık bir envanterini tutun. Her madde için, getirdiği maliyeti (süregelen "faiz") ve düzeltme maliyetini not edin. Sonra onu bir finansal portföy gibi yönetin. Takımı her gün yavaşlatan yüksek faizli borcu ödeyin. Kararlı köşelerdeki düşük faizli borca tahammül edin. Borç kararlarını kazara değil bilinçli verin. Borcun krize bileşmemesi için kapasitenin sabit bir kesrini borç ödemeye ayırın.

### Geri döndürülebilir ve geri döndürülemez kararları ayırt edin

Tüm kararlar eşit müzakereyi hak etmez. Geri döndürülebilir "iki yönlü kapı" kararları kolayca geri alınır, bu yüzden onları hızlı ve yerel, takım tarafından, eyleme yönelik bir eğilimle verin. Onlar için kıvranmak zaman kaybettirir ve öğrenmeyi yavaşlatır. Geri döndürülemez ya da geri döndürmesi maliyetli "tek yönlü kapı" kararları, yani herkese açık bir [API](https://en.wikipedia.org/wiki/API) sözleşmesi, ölçekte bir veri modeli, çok yıllık bir tedarikçi taahhüdü, yavaş, dikkatli, kıdemli müzakere ve kaydedilmiş bir gerekçe hak eder. Kararları bu şekilde sınıflandırmak sahip olduğunuz en yüksek kaldıraçlı yönetişim alışkanlıklarından biridir. Kıt incelemeyi karşılığını verdiği yere yöneltir ve geri kalan her şeyin önünü açar.

## Ödünleşimler: artılar ve eksiler

| Yönetişim yaklaşımı | Artılar | Eksiler |
| --- | --- | --- |
| Hepsi için merkezi inceleme kurulu | Azami tutarlılık ve gözetim | Ağır darboğaz; takımları güçsüzleştirir; yavaş |
| Yerel özerklikle asfalt yol | Ölçeklenir, hızlı, güvenli varsayılan, takımları güçlendirir | Başlangıçta platform yatırımı gerektirir; yol dışına bir miktar sapma |
| Yönetişimsiz tam takım özerkliği | Hızlı, yüksek sahiplik | Parçalanma, yinelenme, tekrarlanan hatalar |
| ADR'ler / RFC'ler | Kalıcı hafıza, daha iyi kararlar, şeffaflık | Yazı yükü; bakımı yapılmazsa göz ardı edilir |

| Tedarik seçimi | Artılar | Eksiler |
| --- | --- | --- |
| İnşa | Tam kontrol, tam uyum, farklılaşabilir | Sürekli bakım ve kadro maliyeti |
| Satın al | Hızlı, destekli, bakımı başkası yapar | Lisans maliyeti, kilitlenme, kusurlu uyum |
| Benimse (açık kaynak) | Lisans ücreti yok, incelenebilir, topluluk | Destek ve güvenlik yükü size düşer |

Birleştirici ödünleşim kontrol ile hız ve merkezi tutarlılık ile yerel özerklik arasındadır. Her yönetişim seçimi bu yelpazede yer alır. Önerilen duruş, asfalt yollar artı geri döndürülebilirliğe dayalı yetki devri, özerkliğin hızının çoğunu önemli olan tutarlılığı koruyarak bilinçli olarak satın alır. Bunu uyumlu seçimi kolay seçim yaparak ve ağır süreci nadir geri döndürülemez karara saklayarak yapar.

## Takımınızla tartışılacak sorular

1. **Belirli bir kararın tek yönlü kapı olup olmadığına kim karar verir ve her iki yöndeki yanlış sınıflandırmaları nasıl yakalarsınız?** Kararları geri döndürülebilirliğe göre sınıflandırmak en yüksek kaldıraçlı yönetişim alışkanlıklarından biridir ve yanlış etiketlerseniz değeri çöker: geri döndürülebilir bir seçimi geri döndürülemez gibi ele alırsanız onu müzakerede boğarsınız, geri döndürülemez birini geri döndürülebilir gibi ele alırsanız ucuza geri alamayacağınız bir veri modelini ya da herkese açık API sözleşmesini yayımlarsınız. Karşıt risk, işe en yakın kişinin hıza meyilli, merkezi bir kurulun ise ihtiyata meyilli olabilmesidir. Tartışmaya somut örnekler getirin: her kararı geri döndürmek zaman ve parada gerçekte neye mal olurdu ve bu maliyeti kim taşıyor. Kurumsal ve kamu ortamlarında tedarik taahhütleri ve ölçekteki veri, başta geri döndürülebilir görünen birçok seçimi tek yönlü kapıya çevirir. Kimin sınıflandıracağı üzerinde anlaşın ve sınıra yakın her şey için hızlı bir ikinci görüş alışkanlığı kurun, böylece kıt inceleme geri alma gerçekten pahalı olduğu yere düşer.

2. **Asfalt yola kim sahip çıkıyor, finanse ediyor ve kadrolandırıyor ve onun bir kapı bekçisine dönüşmesini ne engelliyor?** Bir asfalt yol, yalnızca kutsanmış varsayılanlar gerçekten iyi destekleniyorsa ve alternatiflerden daha kolaysa çalışır ve bu, eksik finanse edilmesi kolay olan sürekli bir yatırım gerektirir. Ödünleşim çıplaktır: kaynağı yetersiz bir asfalt yol, destek olmadan bir zorunluluklar kümesine dönüşür; bu tam da modelin yerini almak üzere tasarlandığı kapı bekçiliğidir ve takımlar o zaman onu dolanır. Yolun sağlığına dair kanıt getirin: benimseme oranları, onaylı araçların ne kadar güncel olduğu, platform takımının ne kadar hızlı yanıt verdiği ve takımların yol dışına çıkmak için ne sıklıkla başvurduğu. Büyük ve düzenlemeye tabi kuruluşlar için asfalt yol aynı zamanda uyumlu seçimin kolay seçim olmasının yoludur, bu yüzden finansmanı yalnızca bir kolaylık değil, bir uyum yatırımıdır. Net bir sahibe ve sürekli bir bütçeye karar verin ve takımların yolu gerçekten en kolay yol olduğu için seçip seçmediğini ölçün.

3. **Takımlar yönetişiminizi nerede dolanıyor ve o gölge BT size ne söylüyor?** Takımlar onaylı yol dolanmaktan daha acı verici olduğunda ondan kaçar, bu yüzden yaygın gölge BT bir disiplin sorunundan çok yönetişiminize dair bir tasarım hükmüdür. Karşıt değerlendirmeler gerçektir: bazı kaçınma pervasızdır ve çoğu, haftalarca bir kuyruğa dönüşmüş bir inceleme kurulundan rasyonel kaçınmadır. Kanıtı getirin: hangi onaylar atlanıyor, hangi resmi olmayan araçlar sessizce yayıldı ve resmi yolun gerçekte ne kadar sürdüğü. Kurumsal ve kamu bağlamlarında riskler daha yüksektir, çünkü onaysız araçlar yasal ağırlık taşıyan denetim, güvenlik ve tedarik yükümlülüklerini ihlal edebilir. Kalıp insanların bir darboğazı dolandığını gösteriyorsa, çözüm daha fazla onay eklemek değil, asfalt yolu hızlandırıp genişletmek ve kurulun kapsamını birkaç kesişen, geri döndürülemez karara daraltmaktır.

4. **Teslimat kapasitemizin gerçekte ne kadarı teknik borç ödemeye gidiyor ve ilk hedeflemesi gereken en yüksek faizli maddeleri adlandırabilir miyiz?** Teknik borç bileşik faiz gibi davranır, her gelecek değişikliğe sessiz bir vergidir ve büyük bir kuruluş, kimse sistemin değiştirilmesi yavaş ve kırılgan hale geldiğini fark etmeden önce onu yıllarca taşıyabilir. Karşıt baskı çıplaktır: borca harcanan her saat, liderliğin görebildiği özelliklere harcanmayan bir saattir, bu yüzden bir teslim tarihi sıkıştığında ödeme ilk kesilen şeydir. Tartışmaya gerçek kanıt getirin: önemli borcun yazılı bir envanteri, her maddenin getirdiği süregelen maliyetin ve düzeltme maliyetinin dürüst bir tahmini ve yakın zamandaki kapasitenin yeni işe karşı ödemeye giden gerçek kesri. On yıllık zaman ufuklarındaki kurumsal ve kamu kuruluşları için yönetilmeyen borç sonunda maliyetli bir yeniden yazmayı ya da bir denetim bulgusunu zorlar; bu yüzden sürekli bir ödeme tahsisini risk yönetimi olarak ele alın ve takvimler kaydığında onu kimin koruduğuna karar verin.

5. **İki yıl önce alınan bir kararın ardındaki gerekçeye ihtiyaç duyduğumuzda onu gerçekten bulabiliyor muyuz ve bu kaydı canlı tutan biri var mı?** Mimari Karar Kaydı'nın bütün değeri, gerekçenin onu veren insanlardan uzun yaşamasıdır ve ADR'ler bir kez yazılır, hiç aranmaz ve sessizce eskirse bu değer çöker. Gerilim, karar anında bağlamı, seçenekleri ve sonuçları yakalamanın yazı disiplini ile sadece yayımlayıp ilerleme günlük baskısı arasındadır. Tartışmaya somut testler getirin: yakın zamanın üç önemli kararını seçin ve kimsenin kaydedilmiş gerekçeyi dakikalar içinde bulup bulamadığına bakın ve geçersiz kılınmış ADR'lerin mevcut uygulamayla sessizce çelişmek yerine öyle işaretlenip işaretlenmediğini kontrol edin. Kurumsal ve kamu ortamlarında, bu aranabilir kayıt tam da denetçilerin ve gözetim organlarının talep ettiği savunulabilir kanıttır; bu yüzden ADR'lerin nerede yaşadığına, kimin incelediğine ve bir kararı kaydetmeye değecek kadar önemli kılan şeyin ne olduğuna karar verin.

6. **Büyük bir yap-ya da-satın-al kararını en son ne zaman özgün varsayımlarına karşı yeniden açtık ve bu varsayımlar sona erdiğinde fark eder miydik?** Tedarik seçimleri aldığınız en pahalı ve geri döndürmesi en zor kararlar arasındadır ve ardındaki varsayımlar (bir tedarikçinin fiyatlandırması, kendi kadronuz, bir açık kaynak seçeneğinin olgunluğu) karar yerinde donmuş dururken sessizce eskir. Karşıt değerlendirmeler, geçişin batık maliyetini ve aksamasını kilitlenmenin, kusurlu uyumun ya da artık istemediğiniz bir bakım yükünün artan maliyetine karşı tartar. Özgün ADR'yi ve belirtilen varsayımlarını, lisans, entegrasyon, kadro ve çıkış maliyeti dahil her yol için güncel bir toplam sahip olma maliyeti tahminini ve bir öncülün kaydığına dair herhangi bir sinyali, bir fiyat değişikliğini ya da bir destek düşürmeyi getirin. Kamu ve düzenlemeye tabi alıcılar için tedarik kuralları ve çok yıllık sözleşmeler bu tek yönlü kapıları özellikle bağlayıcı kılar; bu yüzden körü körüne bir yenileme yerine bilinçli bir yeniden karara zorlayacak tetikleyicilerde ve ritimde önceden anlaşın.

## Sektör merceği

**Girişim.** Neredeyse hiçbir şeyi yönetmeyin ve hıza sıkıca yaslanın: geri döndürülebilir iki yönlü kapı seçimleri için masada karar verin ve devam edin. Tek yönetişim alışkanlığınızı birkaç tek yönlü kapıya, çekirdek bir veri modeline ya da temel bir tedarikçiye saklayın ve her birini tek bir paragrafta yakalayın ki gelecekteki bir takım arkadaşı konuyu sıfırdan yeniden tartışmasın. İnceleme kurullarını ve asfalt yolları tümüyle atlayın, çünkü boyutunuzda onlar karşılayamayacağınız yüklerdir ve bütün takım zaten aynı bağlamı paylaşır.

**Küçük işletme.** Kadroda mimar olmadan, yap ya da satın al sorusunu merkezi yönetişim sorunuz yapın ve tercih yerine toplam sahip olma maliyetine göre cevaplayın. Çekirdek farklılaştırıcınız olmayan her şey için iyi desteklenen araçları satın almaya ya da benimsemeye yönelin, çünkü sürekli bakım, taşıyabileceğiniz en az maliyettir. Az sayıdaki sonuçlu seçiminizin ardındaki gerekçe kilit bir kişi ayrıldığında hayatta kalsın diye tek bir hafif karar günlüğü tutun.

**Kurumsal.** Sorununuz birçok takım arasında özerklik ile uyum arasında denge kurmaktır, bu yüzden finanse edilmiş bir asfalt yola yatırım yapın ve dar, hızlı bir mimari inceleme kurulunu gerçekten kesişen ve geri döndürülemez kararlara ayırın. ADR'leri standartlaştırın ki gerekçe aranabilir kurumsal bellek olsun ve teknik borcu ve tedarik seçimlerini sürekli bütçelerle portföyler olarak yönetin. Takımların yolu en kolay olduğu için seçip seçmediğini ölçün ve bir kuyruğa çürümüş herhangi bir kurulu daraltın.

**Kamu.** Belgelenmiş, savunulabilir kararlar burada isteğe bağlı değildir: denetçiler ve gözetim organları gerekçeyi, tartılan seçenekleri ve her sonuçlu seçimin ardındaki varsayımları görmeyi bekler. Yap ya da satın al'ı kaydedilmiş bir toplam sahip olma maliyeti analizi olarak yürütün, tek kaynaklı kilitlenmeyi kısıtlayan tedarik kurallarına uyun ve ADR'leri denetime hazır kanıt izi olarak tutun. Uzun zaman ufuklarını ciddiye alın, çünkü bugün verilen bir veri modeli ya da tedarikçi taahhüdü kuruluşu on yıl bağlayabilir; bu yüzden onu tek yönlü kapı olarak sınıflandırın ve ona göre müzakere edin.

## Örnekler

**Girişim.** Dört kişilik bir girişim kararların çoğunu paylaşılan bir masada dakikalar içinde verir ve geri döndürülebilir iki yönlü kapı seçimleri için bu hız gerçek bir avantajdır, bu yüzden her yönetişim yüküne direnirler. Ama sonradan değiştirmesi acı verecek bir veritabanı ve veri modeli seçtiklerinde (tek yönlü bir kapı), tek paragraflık bir not yazmak için dururlar: seçenekler, seçim ve ardındaki varsayımlar. Bir yıl sonra, ölçekleme sınırlarına çarptıklarında, o tek not onları soruyu sıfırdan yeniden tartışmaktan kurtarır. Neredeyse hiçbir şeyi yönetmezler ve tek hafif alışkanlıklarını geri döndürmesi gerçekten maliyetli birkaç karara saklarlar.

**Kurumsal.** Büyük bir kurumsal firmanın platform takımları, her teknoloji seçimini onaylaması gereken ve haftalarca kuyruk yaratan bir mimari inceleme kurulu tarafından felç edilmişti. Firma yönetişimi bir asfalt yol etrafında yeniden yapılandırdı: takımların anında benimseyebileceği, onaylı ve tam desteklenen dillerden, veri depolarından ve hatlardan oluşan seçilmiş bir katalog. ADR'ler sapma kararlarını kaydetti ve hızlı, danışmanlık niteliğinde bir inceleme yalnızca yol dışı seçimleri ele aldı. Kurulun kapsamı standart belirlemeye ve gerçekten kesişen birkaç karara daraldı. Teslimat keskin biçimde hızlandı. Tutarlılık aslında iyileşti, çünkü kolay yol artık uyumlu olandı. Ve ADR arşivi kuruluşa her şeyin neden öyle inşa edildiğine dair aranabilir bir kayıt verdi.

**Kamu.** Bir kamu dairesi, sıkı tedarik ve denetim kuralları altında bir vaka yönetim platformu için büyük bir yap ya da satın al kararıyla karşı karşıya kaldı. Tercihle karar vermek yerine, üç seçenek arasında belgelenmiş bir toplam sahip olma maliyeti analizi yürüttü: özel inşa, ticari ürün satın almak ve açık kaynak bir temel benimsemek. Lisansı, entegrasyonu, uzun vadeli bakımı, kadroyu ve kilitlenmeyi tarttı ve kararı ve varsayımlarını bir ADR olarak kaydetti. Yıllar sonra, bir tedarikçinin koşulları değiştiğinde, daire o ADR'yi yeniden ele aldı, özgün varsayımlarının artık geçerli olmadığını buldu ve önceki gerekçenin tam bilgisiyle yeniden karar verdi; körü körüne ve maliyetli bir geçişten kaçındı. Kaydedilmiş gerekçe aynı zamanda denetçilerin talep ettiği savunulabilir kanıttı.

## İş gerekçesi: motivasyonlar, YG ve TSM

Kararlar, yazılımdaki en yüksek kaldıraçlı ve en az görünür maliyettir. Tek bir kötü, geri döndürülemez mimari ya da tedarik seçimi yıllarca sürükleme ya da dokuz haneli bir iyileştirme getirebilir. Onu iyi yönetmek, birkaç saatlik müzakere ve yazılı bir kayıt, bunun yanında neredeyse hiçbir şeye mal olmaz. ADR'lerin ve geri döndürülebilirliğe dayalı yetki devrinin getirisi iki kaynaktan gelir: tek yönlü kapı kararlarında pahalı hatalardan kaçınmak ve geri kalan her şeyde boşa giden müzakereden ve yeniden işten kaçınmak. Kaydedilmiş gerekçe ayrıca yerleşik soruları yeniden tartışmanın ve takımların miras sistemlerin ardındaki niyeti tersine mühendislikle çözmesinin yinelenen maliyetini keskin biçimde azaltır.

Teknik borç TSM argümanını somutlaştırır. Yönetilmeyen borç tam olarak bileşik faiz gibi davranır: sistem fiilen sürdürülemez hale gelip maliyetli bir yeniden yazma talep edene kadar her gelecek değişikliğe büyüyen bir vergi. Borcu bir portföy olarak, yüksek faizli kalemleri ödemek için sürekli bir kapasite tahsisiyle yönetmek, sonunda gelecek krizden çok daha ucuzdur. İyi yönetişimi benimsemek ucuzdur; çoğunlukla kararları yazıya dökme disiplini ve bir asfalt yola başlangıç yatırımı. Onu atlamak pahalıdır: kaçınılabilir yeniden yazmalarla, kilitlenme sürprizleriyle, denetim başarısızlıklarıyla ve kaybedilmiş kurumsal bellekle ödersiniz. Liderliği ikna etmek için yönetişimi onların dilinde çerçeveleyin: risk azaltma, kaçınılan yeniden iş, asfalt yol yoluyla daha hızlı teslimat ve denetime hazır savunulabilirlik. Amacın daha fazla süreç değil, daha iyi hedeflenmiş süreç olduğunu gösterin: geri alma maliyetli olduğunda ağır inceleme, başka her yerde sürtünmesiz hız.

## Anti-kalıplar ve tuzaklar

- Belgelenmemiş kararlar: gerekçe, onu veren insanlar ayrıldığı anda kaybolur.
- Onay kurulu darboğazı: her projenin arkasında kuyruk olduğu merkezi bir organ.
- Herkese tek beden süreç: önemsiz, geri döndürülebilir kararları ağır incelemeden geçirmek.
- Analiz felci: kolayca geri döndürülebilir iki yönlü kapı kararları için kıvranmak.
- [Gölge BT](https://en.wikipedia.org/wiki/Shadow_IT): onaylı yol çok acı verici olduğu için takımların yönetişimden tamamen kaçması.
- Görünmez teknik borç: hiç envantere alınmamış, hiç ödenmemiş, sessizce bileşen borç.
- Her şeyi inşa et ya da her şeyi satın al refleksleri: TSM analizi yerine alışkanlıkla tedarik.
- Yönetişim tiyatrosu: görüntü için var olan ama kararları şekillendirmeyen belgeler ve kurullar.

## Olgunluk modeli

- Düzey 1 (Başlangıç): Kararlar gelişigüzel ve kaydedilmemiştir; yönetişim ya yoktur ya da topyekûn bir darboğazdır; teknik borç görünmezdir ve seçimlerin ardındaki gerekçe insanlar ayrıldığında buharlaşır.
- Düzey 2 (Geliştirme): Bazı kararlar belgelenir ve bir miktar inceleme vardır, ama uygulama takımlar arasında tutarsızdır ve süreç çoğu zaman kararın ağırlığına ve geri döndürülebilirliğine uymaz.
- Düzey 3 (Standartlaştırma): ADR'ler, bir asfalt yol, geri döndürülebilirliğe dayalı yetki devri ve bir borç envanteri kuruluş genelinde belgelenir ve uygulanır; böylece uyumlu seçim kolay varsayılandır ve gerekçe aranabilirdir.
- Düzey 4 (Yönetme): Yönetişim temel çizgilere karşı ölçülür: asfalt yol benimsemesi, ADR kapsamı, karar döngü süresi, kapasitenin payı olarak borç ve yol dışı istisna oranları izlenir ve borcu ödeme ya da tedariği yeniden ele alma kararları kriz yerine bu kanıtla tetiklenir.
- Düzey 5 (Orkestrasyon): Yönetişim sürekli ayarlanır ve teslimat ve risk planlamasıyla bütünleşir; inceleme tam olarak geri döndürülemez kararlara yöneltilir; borç ve tedarik seçimleri portföyler olarak etkin biçimde yeniden dengelenir ve koşullar değiştikçe kanıta dayanarak yeniden karara bağlanır.

## Tartışma fikirleri

- En önemli yakın zamanlı kararlarımız için ardındaki kaydedilmiş gerekçeyi bulabilir miyiz?
- Yönetişimimiz nerede bir darboğaz ve ihtiyaç duyulduğunda nerede yok?
- Mevcut kararlarımızdan hangileri tek yönlü kapı ve onlara öyle davranıyor muyuz?
- Kapasitemizin ne kadarı teknik borç ödemeye gidiyor ve bu yeterli mi?
- Takımlarımız asfalt yolu gerçekten en kolay yol olduğu için mi izliyor, yoksa onu mu dolanıyor?
- Büyük bir yap ya da satın al kararını özgün varsayımlarına karşı en son ne zaman yeniden ele aldık?

## Önemli çıkarımlar

- Önemli kararları ve gerekçelerini ADR'lerle kaydedin; gerekçeyi kalıcı kılın.
- Vaka başına kapı bekçiliğiyle değil, asfalt yollar ve varsayılanlarla yönetin.
- Süreç ağırlığını karar ağırlığı ve geri döndürülebilirlikle eşleştirin; iki yönlü kapıları devredin, tek yönlü kapılar üzerinde müzakere edin.
- Yap-satın al-benimse kararını toplam sahip olma maliyeti üzerinden analiz edin ve varsayımları kaydedin.
- Teknik borcu sürekli bir ödeme tahsisiyle açık bir portföy olarak yönetin.
- Yönetişimi şeffaf ve hafif tutun; kıt incelemeyi geri almanın maliyetli olduğu yere yöneltin.

## Kaynaklar ve ileri okuma

- Michael Nygard, "Documenting Architecture Decisions" (the original ADR pattern)
- Gregor Hohpe, "The Software Architect Elevator" and "37 Things One Architect Knows"
- Amazon shareholder letters on Type 1 vs Type 2 (one-way vs two-way door) decisions
- Ward Cunningham, the original "technical debt" metaphor
- Martin Fowler, writings on technical debt and evolutionary architecture
- Neal Ford, Rebecca Parsons, Patrick Kua, "Building Evolutionary Architectures"
- Nicole Forsgren, Jez Humble, Gene Kim, "Accelerate" (loosely coupled architecture and autonomy)
- ISO/IEC/IEEE 42010 on architecture description
