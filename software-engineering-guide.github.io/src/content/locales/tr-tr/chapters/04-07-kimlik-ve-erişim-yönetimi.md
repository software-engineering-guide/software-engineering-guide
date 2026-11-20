# 4.7 Kimlik ve erişim yönetimi

## Genel bakış ve motivasyon

Sistemlerinize gelen her istek örtük bir iddia taşır: *Bunu yapmama izin var*. Kimlik ve erişim yönetimi (IAM), bu iddianın doğru olup olmadığına karar verme disiplinidir. İnsanların sürekli birbirine karıştırdığı iki ayrı soruyu cevaplar. [Kimlik doğrulama](https://en.wikipedia.org/wiki/Authentication) kim olduğunuzu kanıtlar. [Yetkilendirme](https://en.wikipedia.org/wiki/Authorization) ise bunu kanıtladıktan sonra ne yapabileceğinize karar verir. Bu iki fikri kafanızda ayrı tutarsanız, bu alandaki karışıklığın yarısı ortadan kalkar.

Büyük takımlar için kimlik, sessizce sahip olduğunuz en önemli kontrol haline geldi. Bölüm 4.3 kimliğin yeni çevre olduğunu vurgular ve bölüm 4.1 sıfır güveni onun üzerine kurar: ağa güvenmeyi bıraktığınızda güvenilecek tek şey doğrulanmış bir kimlik ve açık bir politikadır. Bu kayma, zayıf bir parola sıfırlama akışının ya da unutulmuş bir hizmet hesabının artık küçük bir hata olmadığı anlamına gelir. O ön kapıdır. Gerçek ihlallerin çoğu bellek güvenliği kusurlarının zekice sömürülmesi değildir; çalınmış kimlik bilgileri, aşırı geniş izinler ve aylar önce kapatılması gereken hesaplardır.

Bahisler kurumsal ve kamu ortamlarında yükselir. Küresel bir kurum onlarca örtüşen dizini, ayda binlerce işe başlayanı ve ayrılanı ve sistemlerinizin bir dilimine kapsamlı erişim isteyen iş ortaklarını idare eder. Bir kamu kurumu bunun üzerine akıllı kart kimlik bilgilerini, zorunlu kimlik güvence düzeylerini ve belirli bir günde belirli bir kayda tam olarak kimin dokunabildiğini yazılı olarak soracak denetçileri ekler. Bu bölüm, insanlarınızı durma noktasına getirmeden bu soruları iyi cevaplayan bir kimlik katmanının nasıl kurulacağı konusunda fikir sahibidir.

## Temel ilkeler

- **Kimlik doğrulama ve yetkilendirme farklı problemlerdir.** Kimliği kanıtlamak ve izin vermek ayrı tasarımlar ve ayrı gözden geçirmeler gerektirir.
- **Tek kimlik, birçok sistem.** Her kimlik nüfusu için tek bir doğruluk kaynağında birleşin; dizin yayılması bir güvenlik hatasıdır.
- **Varsayılan olarak en az ayrıcalık.** Sıfır erişimden başlayın ve bilinçli ekleyin; insanlar ve makineler için aynı şekilde.
- **Her kimlik bilgisi geçicidir.** Uzun ömürlü gizli bilgiler yerine kısa ömürlü, otomatik düzenlenen kimlik bilgilerini tercih edin.
- **Erişimi kaldırmak, vermek kadar önemlidir.** İhtiyacından uzun yaşayan erişim saf risktir.
- **Kimlik avına dayanıklı olan, akılda kalandan iyidir.** Kimlik doğrulamayı geçiş anahtarlarına ve donanım destekli faktörlere doğru taşıyın.
- **Makineler de kimliktir.** İş yükleri, hatlar ve hizmetler paylaşılan statik anahtarlara değil, yönetilen kimliğe ihtiyaç duyar.
- **Erişim bir olay değil, bir yaşam döngüsüdür.** Verin, gözden geçirin ve bir takvimle iptal edin; yaptığınızı da kanıtlayın.

## Öneriler

### Kimlik doğrulamayı yetkilendirmeden ayırın ve ikisini de merkezileştirin

Kimliği doğrulayan ve diğer sistemlerin güvendiği belirteçleri düzenleyen bir sistem olan tek bir kimlik sağlayıcı (IdP) üzerinden kimlik doğrulayın. Sonra her uygulamanın yetkilendirme kararlarını, o belirteçte taşınan kimlikten ve niteliklerden kendisinin vermesine izin verin. Bu ayrım, kimlik doğrulamayı herkes için bir kez güçlendirirken, ince taneli izin mantığını koruduğu verinin yakınında tutmanızı sağlar. İnsanlarınızın kırk zayıf giriş yerine bir güçlü girişi olması için, tek bir kimlik doğrulamanın birçok uygulamaya erişim sağladığı [tek oturum açmayı](https://en.wikipedia.org/wiki/Single_sign-on) (SSO) benimseyin. Federasyon aynı güveni kurumsal sınırlar boyunca genişletir; bir iş ortağının kimliklerinin, parolalarını siz yönetmeden sistemlerinize erişmesine izin verir.

### Modern protokolleri gerçekte ne için olduklarına göre kullanın

Üç standart işin çoğunu yapar ve her birinin bir görevi vardır. **OpenID Connect (OIDC)**, [OAuth](https://en.wikipedia.org/wiki/OAuth) 2.0 üzerine kurulu bir kimlik katmanıdır; web ve mobil oturum açma için *bu kullanıcı kim* sorusunu cevaplamakta kullanın. **OAuth 2.0**, devredilmiş erişim için bir yetkilendirme çerçevesidir; bir uygulamanın parolasını hiç görmeden bir kullanıcı adına bir API'yi çağırmasına izin vermek için kullanın (bölüm 2.3). **Security Assertion Markup Language (SAML)**, daha eski XML tabanlı federasyon standardıdır; yerleşik iş uygulamalarına kurumsal SSO için hâlâ iş atıdır. Yaygın bir hata, kimlik doğrulamayı doğrudan yapmak için OAuth'a uzanmaktır. OAuth kaynaklara erişim verir; OIDC kimliği belirlemek için onun üzerinde durur. Yeni kullanıcıya dönük oturum açma için OIDC'yi seçin, kurumsal kataloğunuzun gerektirdiği yerde SAML'yi tutun ve kendi belirteç biçiminizi icat etmeyin.

### Kimlik doğrulamayı kimlik avına dayanıklı yapın

Yalnızca parolalar ölçekte savunulamaz. Bildiğiniz bir şeyi, sahip olduğunuz bir şeyi ve olduğunuz bir şeyi birleştiren çok faktörlü kimlik doğrulamayı (MFA) her insan hesabı için istisnasız zorunlu kılın. Sonra zayıf faktörlerin ötesine geçin: SMS üzerinden tek kullanımlık kodlar oltalanabilir ve SIM takasına açıktır. Güçlü varış noktası [geçiş anahtarları](https://en.wikipedia.org/wiki/Passkey) ve altındaki WebAuthn standardıdır (açık anahtarlı kimlik doğrulama için bir tarayıcı API'si); bunlar bir girişi donanımda tutulan bir özel anahtara ve gerçek sitenin kökenine bağlar, böylece sahte bir sayfa çalmaya değer hiçbir şey toplayamaz. Geçiş anahtarları aynı zamanda parolasızdır; kullanıcılarınız buna teşekkür edecektir. Hesap kurtarmayı ve parola sıfırlamayı kimlik doğrulama yüzeyinin parçası sayın, çünkü MFA'nızı yenemeyen bir saldırgan bunun yerine sıfırlama akışına saldıracaktır.

### İşe başlayan-rol değiştiren-ayrılan yaşam döngüsünü yönetin ve erişimi hızla kaldırın

Kimlik bir yaşam döngüsüdür. **İşe başlayan** ilk gün doğru erişime ihtiyaç duyar. Rol değiştiren **rol değiştirenin** yeni erişime ve, kritik olarak, eski erişimin kaldırılmasına ihtiyacı vardır; yoksa yavaş yavaş binanın tüm anahtarlarını biriktirir. **Ayrılan** tüm sistemlerde, ideal olarak son gününden sonraki dakikalar içinde, tüm erişimini hemen kaybetmelidir. Bunu yetkili bir kaynaktan, genellikle insan kaynakları sisteminden yürütün; böylece oradaki bir durum değişikliği aşağı akıştaki erişimi otomatik olarak verir ve kaldırır. Otomatikleştirin. Elle yapılan çıkış kontrol listeleri her zaman bir şeyi kaçırır ve kaçırdıkları hesap olay raporunda ortaya çıkan hesaptır.

### Bir yetkilendirme modeli seçin ve onu kod olarak politika biçiminde ifade edin

İzinleri, iş işlevi rollerine izin atayıp insanları rollere atadığınız [rol tabanlı erişim kontrolüyle](https://en.wikipedia.org/wiki/Role-based_access_control) (RBAC) verin, çünkü üzerinde akıl yürütmek basit ve denetlemek kolaydır. Departman, veri sınıflandırması, konum ya da günün saati gibi niteliklere dayalı bağlama duyarlı kararlara ihtiyaç duyduğunuz yerde [nitelik tabanlı erişim kontrolüne](https://en.wikipedia.org/wiki/Attribute-based_access_control) (ABAC) başvurun. Çoğu olgun kurum bir hibrit işletir: kaba yetkiler için RBAC, ince koşullar için ABAC. Hangisini seçerseniz seçin, yetkilendirmeyi **kod olarak politika** biçiminde ifade edin: bir konsola tıklanmış kurallar yerine sürüm kontrollü, test edilebilir, gözden geçirilebilir biçimde yazılmış kurallar. Kod olarak politika erişim kararlarını denetlenebilir, farkı alınabilir ve ortamlar arasında tutarlı kılar ve bir izin değişikliğini canlıya çıkmadan önce test etmenizi sağlar.

### En az ayrıcalığı tam zamanında erişim ve PAM ile uygulayın

[En az ayrıcalık ilkesini](https://en.wikipedia.org/wiki/Principle_of_least_privilege) uygulayın: her kimlik ihtiyaç duyduğu asgari erişimi alır ve fazlasını almaz. Kalıcı ayrıcalık düşmandır, çünkü kalıcı olarak verilen bir izin, o hesaba herhangi bir anda inen herhangi bir saldırganın kullanımına açıktır. Bir kişinin sınırlı bir pencere için yükseltilmiş hak talep ettiği, onaydan sonra aldığı ve pencere kapandığında otomatik olarak kaybettiği **tam zamanında (JIT) erişimi** tercih edin. En tehlikeli hesaplarınız için **ayrıcalıklı erişim yönetimini (PAM)** benimseyin: yönetici kimlik bilgilerini kasaya alan, ayrıcalıklı oturumlara aracılık edip kaydeden ve talep üzerine yükseltme veren bir sistem. Hedef sıfır kalıcı yönetici erişimidir; böylece tamamen ele geçirilmiş bir dizüstü bile kalıcı hiçbir şey vermez.

### Makinelere ve iş yüklerine gerçek kimlik verin

İnsanlar kimliklerinizin yalnızca yarısıdır. Hizmetler, hatlar, konteynerler ve işlevlerin hepsi bir şeye karşı kimlik doğrular ve çok sık bunu bir yapılandırma dosyasına yapıştırılmış uzun ömürlü bir gizli bilgiyle yaparlar. Statik anahtarları yönetilen **iş yükü kimliğiyle** değiştirin: bir iş yüküne çalıştığı yere ve ne olduğuna göre otomatik verilen kısa ömürlü kimlik bilgileri. Hizmetten hizmete kimlik doğrulama için bir bağlantının her iki tarafının da sertifika sunduğu karşılıklı TLS'yi (mTLS) kullanın. Kalan gizli bilgileri döndürme özellikli özel bir gizli bilgi yöneticisinde tutun; asla kaynak kodda ya da imajlarda değil (bölüm 4.2). Kısa ömürlü, otomatik döndürülen iş yükü kimlik bilgileri, bulut kimlik bilgisi sızıntılarının en yaygın tek nedenini ortadan kaldırır.

### Kimliği kontrol düzlemi yapın ve erişimi sürekli gözden geçirin

Sıfır güven mimarisinde (bölüm 4.1) kimlik, politikanın karara bağlandığı ve uygulandığı yerdir; bu yüzden oraya buna göre yatırım yapın. Sonra döngüyü **erişim gözden geçirmeleriyle**, diğer adıyla yeniden onaylamayla kapatın: bir takvimle her sistemin sahibi, erişimi olan her kişinin ve makinenin hâlâ buna ihtiyaç duyduğunu doğrular ve gerekçelendiremediklerini iptal eder. Her kimlik doğrulama ve yetkilendirme olayını *kim neye, ne zaman ve hangi politika altında eriştiği* sorusunu cevaplayan bir denetim izine besleyin (bölüm 4.6). Erişim gözden geçirmeleri, ayrıcalık sürünmesiyle, yani hiçbir tekil verilişin makul görünmediği ama birlikte bir hesabı fazlasıyla güçlü yapan izinlerin yavaş birikimiyle savaşma yolunuzdur.

## Ödünleşimler: artılar ve eksiler

| Karar | Artılar | Eksiler |
|---|---|---|
| SSO'lu merkezi IdP | Tek güçlü giriş, tutarlı politika, kolay denetim | Tek hata noktası; kesinti herkesi dışarıda bırakır |
| RBAC | Basit, denetlenebilir, tanıdık | Rol patlaması; bağlama duyarlı ihtiyaçlar için kaba |
| ABAC | İnce taneli, bağlama duyarlı, niteliklerle ölçeklenir | Tasarlaması, test etmesi ve üzerinde akıl yürütmesi daha zor |
| Geçiş anahtarları / WebAuthn | Kimlik avına dayanıklı, parolasız, güçlü | Kurtarma ve cihaz kaybı akışları dikkatli tasarım ister |
| Tam zamanında erişim | Neredeyse sıfır kalıcı ayrıcalık | Sürtünme; hızlı, güvenilir onay yolları gerekir |
| İş ortaklarıyla federasyon | Dış parola yönetimi yok; kapsamlı güven | Güven ortağın kendi hijyenine bağlı |
| Uzun ömürlü hizmet anahtarları | Kurması çok kolay | Sızmaya yatkın; kimlik bilgisi ihlallerinin başlıca nedeni |

Temel gerilim güvenlik ile sürtünme arasındadır. Saldırı yüzeyini daraltan her kontrol (her şeyde MFA, JIT yükseltme, kısa kimlik bilgisi ömürleri) aynı zamanda birinin gününe bir adım ekler ve insanlar çok acıtan kontrollerin etrafından dolanır. Bunu güvenli yolu kolay yol yaparak çözün: güçlü kimlik doğrulama tek dokunuş olsun diye SSO, yazılacak parola olmasın diye geçiş anahtarları ve doğru erişim kendiliğinden belirsin diye otomatik yetkilendirme. Sürtünme bütçenizi etki alanının en geniş olduğu yerde, ayrıcalıklı ve üretim erişiminde harcayın ve gündelik erişimi neredeyse sürtünmesiz tutun.

## Takımınızla tartışılacak sorular

1. **Bugün ayrılan biri için tüm erişimi gerçekte ne kadar hızlı iptal edebilirsiniz ve işe yaradığını nasıl bilirsiniz?** Erişimi kaldırma hızı kimlik olgunluğunuzun doğrudan bir ölçüsüdür, çünkü erişimi sürüp giden bir ayrılan, gerçek izinleri olan izlenmeyen bir hesaptır. Onlarca bağlantısız sistemi olan büyük bir kurumda dürüst cevap çoğu zaman "emin değiliz"dir ve boşluk genellikle merkezi kimlik sağlayıcıya hiç bağlanmamış uygulamalardır. Yakın zamandaki gerçek bir ayrılışı getirin ve dokunabildiği her sistemi izleyin, her erişimin gerçekte ne zaman bittiğine dair zaman damgalarını kontrol edin. İnsan kaynakları durum değişikliğinden sonra bir saat içinde tam iptal gibi bir hedef belirleyin ve umut etmek yerine kanıtlayabilmek için ölçümleyin. Herhangi bir sistem birinin elle yapılan bir adımı hatırlamasına dayanıyorsa, gelecekteki bir ihlalin kullanacağı hesap odur.

2. **Hâlâ nerede kalıcı ayrıcalıklı erişiminiz ve uzun ömürlü statik kimlik bilgileriniz var ve bunları ortadan kaldırmak için ne gerekir?** Kalıcı yönetici hakları ve kalıcı hizmet anahtarları saldırganların en çok istediği iki varlıktır, çünkü kalıcı ve güçlüdürler. Her zaman açık üretim ya da yönetim erişimi olan her insanı ve statik bir anahtarla kimlik doğrulayan her hizmeti envantere alın, sonra bunlardan hangilerinin tam zamanında yükseltmeye ya da kısa ömürlü iş yükü kimliğine taşınabileceğini dürüstçe sorun. Rekabet eden husus operasyonel korkudur: takımlar kalıcı erişimi tutar, çünkü acil durum anları onunla daha güvenli hissettirir; bu yüzden kalıcı hakları almadan önce acil yükseltmeyi hızlı ve güvenilir kılmalısınız. Listeyi tartışmaya getirin ve öğeleri etki alanına göre sıralayın; önce üretim ve yönetim erişimini hedefleyin. Hedeflenecek son durum, sıfır kalıcı yönetici erişimi ve tek bir dağıtımdan uzun yaşayan hiçbir statik anahtardır.

3. **Kişi başına ve iş yükü başına tek yetkili kimliğiniz mi var yoksa birkaç mı ve yayılma size neye mal oluyor?** Aynı insanın drift eden niteliklerle beş sistemde beş hesap olarak var olduğu dizin yayılması, erişimi kaldırma boşluklarının ve sahipsiz erişimin doğduğu yerdir. Her kimlik nüfusu için tek bir doğruluk kaynağında birleşmek büyük bir takımın yapabileceği en yüksek kaldıraçlı yatırımlardan biridir, çünkü her aşağı akış kontrolü iki kaydın aynı kişi olduğunu bilmeye bağlıdır. Kimlik depolarınızın bir envanterini getirin ve hangilerinin yetkili, hangilerinin kimsenin yönetmediği kullanışlı kopyalar olduğunu eşleyin. Ödünleşim, birleştirmenin özellik işiyle ilgi için rekabet eden büyük, gösterişsiz bir göç olmasıdır. Yayılmanın süregelen maliyetinin, denetim acısı ve ihlal riski olarak, bu göçü bir sonraki olaydan sonra değil şimdi finanse etmeyi haklı kılıp kılmadığına karar verin.

4. **En güçlü kimlik doğrulama faktörleriniz gerçekten kimlik avına dayanıklı mı ve parolaları kalıcı olarak emekliye ayırmanızı ne engelliyor?** Bir saldırganın oltalayamadığı faktör, kimlik bilgisi hırsızlığını baskın ihlal yolunuz olmaktan çıkarandır ve WebAuthn'a bağlı geçiş anahtarları bu çıtayı aşan, yaygın biçimde dağıtılabilir tek seçenektir. Büyük bir kurumda dürüst tablo genellikle karışıktır: bazıları için geçiş anahtarları, bazıları için SMS üzerinden tek kullanımlık kodlar ve hâlâ yalnızca parola kabul eden eski uygulamaların uzun bir kuyruğu. Rekabet eden husus gerçektir, çünkü geçiş anahtarları zor problemi kurtarmaya ve cihaz kaybına kaydırır ve beceriksiz bir kurtarma akışı saldırganın basitçe yöneldiği yeni yumuşak hedef olur. Faktör türüne göre kapsam sayılarını, hâlâ parolaya düşen uygulamaların listesini ve kararlı bir sosyal mühendislik girişimine karşı güveneceğiniz tasarlanmış bir hesap kurtarma yolunu getirin. Kurumsal ve kamu ortamlarında hedefi zorunlu herhangi bir güvence düzeyine bağlayın, çünkü hâlâ oltalanabilir bir faktöre izin veren yüksek güvenceli bir sistemin güvenlik boşluğunun yanı sıra bir uyum boşluğu da vardır.

5. **Her kimliğin hangi erişimi alacağına nasıl karar veriyorsunuz ve bu kararı canlıya çıkmadan önce karşılaştırabilir, test edebilir ve kanıtlayabilir misiniz?** "Biri izinleri bir konsola tıkladı" ile "gözden geçirilmiş, sürüm kontrollü bir politika" arasındaki fark, denetleyebileceğiniz bir erişim modeli ile yalnızca özür dileyebileceğiniz bir model arasındaki farktır. Büyük bir takım için baskı, her uygulamanın kendi özel kurallarını geliştirmesine izin vermektir; bu da RBAC tarafında sessizce rol patlaması, ABAC tarafında test edilemez koşullar üretir ve sonunda kimse belirli bir verilişin gerçekte neye izin verdiğini söyleyemez. Rekabet eden husus teslimat hızıdır, çünkü yetkilendirmeyi kod olarak politika biçiminde ifade etmek bir konsol tıklamasının yapmadığı bir gözden geçirme adımı ekler ve son teslim tarihi altındaki takımlar ilk başarısız denetim ya da aşırı geniş verilişe kadar bu sürtünmeye içerler. Gerçek bir izin değişikliğini getirin ve nasıl önerileceğini, test edileceğini, gözden geçirileceğini ve geri alınacağını izleyin; ayrıca kaç rolünüz olduğunu ve kaçını kimsenin açıklayamadığını sayın. Kurumsal ve kamu ortamlarında bir denetçi sizden belirli bir günde bir kayda tam olarak kimin hangi kuralla erişebildiğini göstermenizi isteyecektir ve bunu yalnızca farkı alınabilir, test edilebilir bir politika telaşsız cevaplar.

6. **Bir erişim gözden geçirmesi en son ne zaman gerçek bir şeyi iptal etti ve ayrıcalık sürünmesi denetlenmeden kaldığında kim hesap verebilir?** Erişim gözden geçirmeleri, hiçbir tekil verilişin makul görünmediği izinlerin yavaş birikimiyle savaşan kontroldür ve hiçbir şeyi iptal etmeyen bir gözden geçirme, güvenlik yerine evrak üreten gözden geçirme tiyatrosudur. Büyük bir kurumda başarısızlık biçimi lastik damgadır: sistem sahipleri yüzlerce girdiyi tek oturumda yeniden onaylar ve hepsini onaylar, çünkü her birini gerçekten değerlendirmek sıkıcıdır ve erişimi akıtma teşviki kesme teşvikinden güçlüdür. Rekabet eden husus, anlamlı gözden geçirmelerin sahip zamanına mal olması ve sessizce dayandıkları erişim kaybolduğunda zaman zaman birinin iş akışını bozmasıdır; bu yüzden gözden geçirmeyi ayrımsız bir liste değil, hedefli ve riske dayalı yapmalısınız. Son döngüden iptal oranını, kişi başına ortalama hak sayısını ve her sistemin yeniden onaylamasının sahibinin kim olduğuna dair kanıtı getirin. Kurumsal ve kamu ortamlarında her gözden geçirme için hesap verebilir yetkiliyi ve bağlı tutuldukları ritmi adlandırın, çünkü kimsenin yakalamaktan sorumlu olmadığı ayrıcalık sürünmesi, denetçilerin ve saldırganların ikisinin de sömürdüğü tam koşuldur.

## Sektör merceği

**Girişim.** Kimliği satın alın, kurmayın. SSO'lu, geçiş anahtarları zorunlu ve tek tıkla çıkışı olan tek bir barındırılan kimlik sağlayıcı, bir avuç mühendise koltuk başına bir ücretle kurumsal düzeyde bir duruş verir. Hattınızda tek bir uzun ömürlü bulut anahtarı olmasın diye sağlayıcının yerleşik iş yükü kimliğine yaslanın ve sürdürmeye gücünüzün yetmeyeceği belirteç işlemeyi icat etmek yerine OIDC ve OAuth 2.0'ı hazır kullanın.

**Küçük işletme.** Kadroda kimlik uzmanı yoksa, ödediğiniz araçlara zaten paketlenmiş SSO ve MFA'yı tercih edin ve ayrı bir platform aramak yerine onları açın. İşe başlayan-rol değiştiren-ayrılan problemini, işe almanın sahibine bağlı kısa yazılı bir kontrol listesi olarak ele alın ve geçiş anahtarlarını tercih edin, çünkü kimseyi ayıramayacağınız parola sıfırlama yardım masası yükünü ortadan kaldırırlar. Paylaşılan girişlerden kaçının; çünkü bunlar sonradan atfı ve iptali imkânsız kılan ucuz alışkanlıktır.

**Kurumsal.** İş, birçok dizin ve takım arasında birleştirme ve yönetişimdir: insan kaynakları sistemi tarafından yönlendirilen tek bir yetkili kimlik sağlayıcı, otomatik işe başlayan-rol değiştiren-ayrılan akışları, iş işlevleri için RBAC ve bağlam için ABAC ve oturum kaydı olan ayrıcalıklı erişim yönetimi. Değişikliklerin farkı alınabilir ve test edilebilir olması için yetkilendirmeyi kod olarak politika biçiminde ifade edin, gerçekten iptal eden zamanlanmış erişim gözden geçirmeleri yürütün ve her uygulamanın kendi girişini geliştirmesi yerine merkezi kimliğe bağlanması için arayüzü standartlaştırın.

**Kamu.** Tedarik kuralları, şeffaflık ve kamusal hesap verebilirlik tasarımı yönlendirir. Kimlik doğrulamayı PIV ya da CAC akıllı kartları gibi donanım kimlik bilgilerine bağlayın, daha yüksek riskli sistemlerin daha yüksek güvenceli faktörler talep etmesi için kimlik güvence düzeylerini NIST SP 800-63'e göre belirleyin ve kimin neye ne zaman eriştiğini tam olarak cevaplayan değiştirilemez denetim günlükleri tutun. Vatandaşa dönük kimliğin işlenmesini sade dille yayımlayın, müşteri ve iş gücü kimlik yığınlarını ayrı tutun ve hassas bir sistemdeki her ayrıcalıklı eylemin soracak denetçiler için aracılık edilip kaydedilmesini sağlayın.

## Örnekler

**Girişim.** Yirmi kişilik bir girişim kimlik takımı kadrolayamaz, bu yüzden bir tane satın alır. Her çalışan e-postaya, kod barındırmaya, bulut konsoluna ve dahili uygulamaya SSO'lu tek bir barındırılan kimlik sağlayıcı üzerinden girer ve oltalanacak parola olmasın diye geçiş anahtarları zorunludur. Çıkış tek tıktır: kişiyi kimlik sağlayıcıda devre dışı bırakmak erişimi her yerde bir kerede keser. Kendi ürünleri için kullanıcı oturum açma için OIDC'yi ve entegrasyonların API'lerini kapsamlı belirteçlerle çağırması için OAuth 2.0'ı kullanırlar. Hizmetten buluta kimlik doğrulama sağlayıcının yerleşik iş yükü kimliğini kullanır; böylece hatlarında hiçbir yerde tek bir uzun ömürlü bulut anahtarı yoktur. Bu mütevazı bir koltuk başı ücrete mal olur ve onlara birçok kurumsal yapının işlettiğinden daha güçlü bir kimlik duruşu sağlar.

**Kurumsal.** Çok uluslu bir banka on yılı dört dizin ve yüzlerce uygulama biriktirerek geçirmiştir; bazıları SAML ile federe, bazıları kendi yerel girişlerine sahip. Bir birleştirme programını finanse eder: insan kaynakları sistemi tarafından yönlendirilen tek bir yetkili kimlik sağlayıcı, işe alımda erişim veren ve fesihten sonraki dakikalar içinde iptal eden otomatik işe başlayan-rol değiştiren-ayrılan akışları. RBAC standart iş işlevlerini kapsar, ABAC ise sınır ötesi erişim için veri yerleşimi ve güvenlik izni kurallarını uygular. Yöneticilerin kalıcı üretim erişimi yoktur; her oturumu kaydeden bir ayrıcalıklı erişim yönetimi sistemi üzerinden tam zamanında yükseltme talep ederler. Üç aylık erişim gözden geçirmeleri sistem sahiplerini yeniden onaylamaya ya da iptal etmeye zorlar ve her karar kod olarak politika biçiminde ifade edilir; böylece denetçiler tam olarak neyin ne zaman değiştiğinin farkını alabilir.

**Kamu.** Federal bir kurum iş gücüne kişisel kimlik doğrulama (PIV) akıllı kartlarını ve askeri eşdeğeri olan ortak erişim kartını (CAC) verir; böylece kimlik doğrulama bir parolaya değil, bir donanım kimlik bilgisine bağlıdır. Kimlik programı federal kimlik, kimlik bilgisi ve erişim yönetimi (FICAM) yaklaşımını izler ve daha yüksek riskli sistemler daha yüksek güvenceli kimlik bilgileri talep etsin diye kimlik güvence düzeylerini Ulusal Standartlar ve Teknoloji Enstitüsü kılavuzu NIST SP 800-63'e göre belirler. Vatandaşa dönük hizmetler, güçlü MFA ile daha düşük bir güvence düzeyinde ayrı bir müşteri kimlik yığını kullanır. Erişim gözden geçirmeleri ve değiştirilemez denetim günlükleri doğrudan kurumun sürekli yetkilendirme kanıtını besler (bölüm 4.6) ve gizli bir sistemdeki her ayrıcalıklı eylem aracılık edilir ve kaydedilir.

## İş gerekçesi: motivasyonlar, YG ve TSM

Kimlik yatırımının getirisi, baskın ihlal vektörünüzü tehlike bölgesinden çıkarmaktan gelir. Çalınmış kimlik bilgileri ve aşırı izinli hesaplar gerçek olayların büyük bir payını yönlendirir ve her biri ağır bir kuyruk taşır: olay müdahalesi, düzenleyici cezalar, ihlal bildirimi ve kalıcı itibar zararı. Yalnızca kimlik avına dayanıklı MFA en yaygın sızma yolunu ortadan kaldırır ve otomatik erişim kaldırma, sıradan bir ayrılışı bir maruziyete çeviren sahipsiz hesap boşluğunu kapatır. Bunlar harcanan dolar başına mevcut en ucuz risk azaltmalar arasındadır.

Toplam sahip olma maliyeti (TSM) gerçektir ama sınırlıdır. Kimlik sağlayıcı lisanslamasını, bir ayrıcalıklı erişim yönetimi ve gizli bilgi platformunu, her uygulamayı merkezi kimliğe bağlamak için mühendisliği ve erişim gözden geçirmelerinin süregelen emeğini içerir. Daha büyük maliyet kurumsaldır: dizinleri birleştirmek ve eski uygulamalara sonradan SSO eklemek, özelliklerle rekabet eden yavaş, gösterişsiz bir iştir. Bunu alternatife karşı tartın. Parçalanmış kimlik, aynı parayı sonsuza dek elle çıkış, denetim telaşları ve yardım masası parola sıfırlamaları biçiminde harcar; ayrıca parçalanmanın olası kıldığı ihlalin nihai maliyetini ekler. Liderliğe gerekçeyi sunarken kimliği sıfır güvenin kontrol düzlemi olarak çerçeveleyin: birleştirme ve otomasyon, hem ihlal riskini hem de denetimlerin, çıkışın ve erişim desteğinin yinelenen maliyetini düşüren bir kerelik yatırımdır.

## Anti-kalıplar ve tuzaklar

- **Sahipsiz hesaplar.** Kişiden ya da amaçtan uzun yaşayan erişim; özellikle izlenmeyen hizmet hesapları ve unutulmuş yükleniciler.
- **Her yerde kalıcı yönetici.** Tam zamanında yükseltme yerine her zaman açık ayrıcalıklı erişim; ele geçirilmiş herhangi bir yönetici hesabına kalıcı güç verir.
- **Uzun ömürlü statik anahtarlar.** Yapılandırmaya ya da CI'ya yapıştırılmış, asla süresi dolmayan ve eninde sonunda sızan hizmet kimlik bilgileri.
- **Dizin yayılması.** Aynı kişinin birçok yönetilmeyen hesap olması; böylece hiçbir değişiklik tam olarak yayılmaz.
- **Paylaşılan hesaplar.** Birkaç kişi tarafından kullanılan kimlik bilgileri; atfı yok eder ve iptali imkânsız kılar.
- **Güçlü faktörünüz olarak SMS.** Oltalanabilir, SIM takasına açık tek kullanımlık kodları yeterli MFA saymak.
- **Rol patlaması.** O kadar çok dar RBAC rolü ki model denetlenemez hale gelir ve kimse bir rolün neye izin verdiğini bilmez.
- **Elle bir kontrol listesi olarak erişim kaldırma.** Önemli olan hesabı kaçınılmaz olarak kaçıran insan çıkış adımları.
- **Kimlik doğrulama için kullanılan OAuth.** OIDC kullanmak yerine bir erişim belirtecini kimlik kanıtı saymak.
- **Gözden geçirme tiyatrosu.** İhtiyacı kimsenin gerçekten değerlendirmeden lastik damgayla onaylanan erişim yeniden onaylamaları.

## Olgunluk modeli

- **Düzey 1, Başlangıç:** Her uygulamanın kendi girişi vardır. Tutarlı MFA olmayan parolalar. Yetkilendirme ve çıkış elle, tepkisel ve yavaştır; sahipsiz hesaplar birikir. Hizmet kimlik bilgileri uzun ömürlü statik anahtarlardır. Erişim gözden geçirmesi yoktur; izinler verilir ve bir daha ele alınmaz.
- **Düzey 2, Geliştirme:** SSO, merkezi bir kimlik sağlayıcı üzerinden başlıca uygulamaları kapsar, ama kapsam takımlar arasında eşitsizdir. MFA çoğu insan erişimi için zorunludur. Temel RBAC vardır. İşe başlayan-rol değiştiren-ayrılan kısmen insan kaynakları sisteminden otomatikleştirilmiştir. Bazı ayrıcalıklı hesaplar kasaya alınmıştır. Erişim gözden geçirmeleri ara sıra ve tutarsız yapılır.
- **Düzey 3, Standartlaştırma:** Birleştirilmiş bir kimlik sağlayıcı iş gücü için yetkilidir; otomatik yetkilendirme ve hızlı erişim kaldırma kurum genelinde uygulanır. Kimlik avına dayanıklı MFA standarttır ve belgelenmiştir. RBAC artı ABAC kod olarak politika biçiminde ifade edilir. Oturum kaydı olan ayrıcalıklı erişim yönetimi yerindedir. İş yükü kimliği statik anahtarların çoğunun yerini alır. Zamanlanmış erişim gözden geçirmeleri, her takımın izlediği yazılı bir politikaya göre uygulanır ve denetlenir.
- **Düzey 4, Yönetme:** Kimlik programı taban çizgilerine karşı ölçülür ve veriyle kontrol edilir. İnsan kaynakları durum değişikliğinden tam iptale erişim kaldırma süresini, nüfusa göre MFA ve geçiş anahtarı kapsamını, kalıcı ayrıcalıklı erişimi olan hesapların sayısını, hâlâ kullanımda olan uzun ömürlü statik anahtarların sayısını, sahipsiz hesap sayılarını ve erişim gözden geçirme iptal oranlarını izlersiniz. Metrikler bir saat içinde tam iptal ve sıfır net yeni kalıcı yönetici verilişi gibi hedefler taşır ve bir eşiğin aşılması omuz silkmek yerine soruşturmayı tetikler. Yetkilendirme değişiklikleri hatta test edilir ve bir erişim verilişine ilişkin her git/gitme kararı alışkanlıkla değil kanıtla yönlendirilir.
- **Düzey 5, Orkestrasyon:** Kimlik, sıfır güven için sürekli iyileştirilen kontrol düzlemidir; kurum genelinde güvenlik, risk ve işe başlayan-rol değiştiren-ayrılan planlamasıyla bütünleşiktir. Geçiş anahtarları varsayılandır ve parolalar emekliye ayrılmaktadır. Sıfır kalıcı ayrıcalık tam zamanında yükseltmeyle sağlanır ve tüm iş yükleri kısa ömürlü, otomatik döndürülen kimlik bilgileri ve mTLS kullanır. Yetkilendirme tamamen kod olarak politikadır. Erişim gözden geçirmeleri sürekli ve riske dayalıdır, erişimi kaldırma neredeyse anlıktır ve her karar denetim kanıtını otomatik üretir. Model, risk sinyalleri değiştikçe uyum sağlar; erişimi sabit bir ritimle değil dinamik olarak sıkılaştırır ya da gevşetir.

## Tartışma fikirleri

1. Sıfır kalıcı yönetici erişimine ulaşmak için ne gerekir ve bunu güvenli kılacak hangi acil durum yolu olurdu?
2. Ortamınızda ABAC karmaşıklığına nerede değer, nerede sade RBAC'ta kalmak daha iyi?
3. Parolaları geçiş anahtarları lehine ne kadar agresif emekliye ayırmalısınız ve onların yerini hangi kurtarma akışı alır?
4. Hangi uygulamalar hâlâ merkezi kimlik sağlayıcınızın dışında ve onları orada tutan ne?
5. İş ortaklarına ve müşterilere, onların güvenlik hijyenini devralmadan kapsamlı erişimi nasıl verirsiniz?
6. Erişimi kaldırma hızınızı en iyi hangi tek metrik yakalar ve bugün onu ölçüyor musunuz?

## Önemli çıkarımlar

- Kimlik doğrulama kim olduğunuzu kanıtlar; yetkilendirme ne yapabileceğinize karar verir. Bunları ayrı tasarlayın ve gözden geçirin.
- SSO'lu tek bir yetkili kimlik sağlayıcıda birleşin; dizin yayılması bir kolaylık değil, bir güvenlik kusurudur.
- İşe başlayan-rol değiştiren-ayrılan yaşam döngüsünü otomatikleştirin ve erişimi kaldırmayı hızlı ve kanıtlanabilir yapın.
- Kullanıcı oturum açma için OIDC'yi, devredilmiş API erişimi için OAuth 2.0'ı ve kurumsal kataloğun gerektirdiği yerde SAML'yi kullanın; OAuth'u kimlik doğrulama olarak kullanmayın.
- Kimlik doğrulamayı kimlik avına dayanıklı geçiş anahtarlarına ve WebAuthn'a doğru taşıyın; her yerde MFA zorunlu kılın ve zayıf faktörleri geçici çözüm sayın.
- En az ayrıcalığı tam zamanında erişim ve ayrıcalıklı erişim yönetimiyle uygulayın; sıfır kalıcı yönetici hakkını hedefleyin.
- Makinelere kısa ömürlü iş yükü kimlik bilgileri ve mTLS ile gerçek kimlik verin; uzun ömürlü statik anahtarları ortadan kaldırın.
- Kimliği sıfır güven için kontrol düzlemi yapın (bölüm 4.1) ve döngüyü sürekli erişim gözden geçirmeleri ve denetim kanıtıyla kapatın (bölüm 4.6).

## Kaynaklar ve ileri okuma

- National Institute of Standards and Technology, *SP 800-63: Digital Identity Guidelines* (identity assurance, authentication, and federation levels)
- National Institute of Standards and Technology, *SP 800-207: Zero Trust Architecture*
- National Institute of Standards and Technology, *SP 800-162: Guide to Attribute Based Access Control (ABAC) Definition and Considerations*
- National Institute of Standards and Technology, *SP 800-53: Security and Privacy Controls*, Access Control (AC) and Identification and Authentication (IA) families
- The OAuth 2.0 Authorisation Framework, IETF RFC 6749, and the OAuth 2.0 Security Best Current Practice
- OpenID Connect Core 1.0 specification, OpenID Foundation
- Security Assertion Markup Language (SAML) 2.0 specification, OASIS
- Web Authentication (WebAuthn) Level 2, W3C Recommendation, and FIDO2 / FIDO Alliance passkey specifications
- Federal Identity, Credential, and Access Management (FICAM) architecture and playbooks, U.S. General Services Administration
- FIPS 201, *Personal Identity Verification (PIV) of Federal Employees and Contractors*
- Open Policy Agent (OPA) documentation, Cloud Native Computing Foundation (policy-as-code for authorisation)
