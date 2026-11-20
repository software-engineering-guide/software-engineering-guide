# 7.5 Karar bilimi ve veriye dayalı kültür

## Genel bakış ve motivasyon

Karar bilimi, belirsizlik altında insanların iyi seçim yapmasına yardımcı olmak için istatistikten, davranış biliminden ve yargıdan yararlanarak veriyi gerçek kararlara bağlama pratiğidir. Veriye dayalı kültür ise bunun varsayılan olarak gerçekleştiği kurumsal durumdur: insanlar kanıta başvurur, neden-sonuç ilişkisi üzerine dikkatle akıl yürütür, belirsizliği dürüstçe iletir ve veri gerektirdiğinde inançlarını günceller. Bu bölüm bilerek veri dizisinin doruk noktasıdır, çünkü ondan önceki tüm strateji, mühendislik, analitik ve deney, kararları daha iyiye değiştirmiyorsa değersizdir.

Büyük takımlar için veri yatırımlarının en sık başarısız olduğu yer burasıdır; boru hatlarında değil, içgörüden eyleme giden son kilometrede. Kurumlar platformlara ve panolara çok para harcar, yine de büyük kararları hiyerarşiyle, alışkanlıkla ya da en kendinden emin sunucuyla verir. Yaygın bir başarısızlık biçimi veri tiyatrosudur: gerçek karar önceden verilmişken ve veri onu haklı çıkarmak için ayıklanmışken titiz görünmek için üretilen ayrıntılı panolar ve çözümlemeler. Kamu buna yüksek bahisler ve sıkı denetim ekler. Zayıf nedensel iddialarla gerekçelendirilen politika kararları kamu parasını yanlış dağıtabilir ve vatandaşlara zarar verebilir; hesap verebilirlik talebi, kanıt hakkında dürüstçe akıl yürütmeyi yalnızca iyi pratik değil, bir yurttaşlık yükümlülüğü yapar.

Buradaki zor sorunlar teknik değil, bilişsel ve kültüreldir. İnsanlar [korelasyonu nedensellikle](https://en.wikipedia.org/wiki/Correlation_does_not_imply_causation) karıştırır, [karıştırıcı değişkenleri](https://en.wikipedia.org/wiki/Confounding) (hem varsayılan nedeni hem etkiyi yönlendiren gizli değişkenler) görmezden gelir, gördükleri ilk sayıya çapa atar ve nokta tahminlerini kesinlik olarak okur. Üstelik veriye dayalı olma gayretinde kuruluşlar gözetime kayabilir: bireyleri o kadar müdahaleci ölçerler ki güveni yok eder ve oyunlamayı tetiklerler. Gerçek bir ölçüm kültürü kurmak, akıl yürütmeyi doğru yapmak, belirsizliği sadakatle iletmek ve veriyi insanlar üzerinde bir denetim aracına çevirmeden sistemleri ve çıktıları ölçmek demektir.

## Temel ilkeler

- Verinin amacı rapor üretmek değil, daha iyi kararlardır.
- Veriye bakmadan önce fikrinizi neyin değiştireceğine karar verin.
- Korelasyon nedensellik değildir; harekete geçmeden önce karıştırıcı değişkenleri sorgulayın.
- Belirsizliği dürüstçe iletin; aralıksız bir nokta tahmini yanıltır.
- Veriye dayalı olun, veri tarafından köleleştirilmeyin; yargı ve bağlam hâlâ önemlidir.
- Sistemleri öğrenmek ve iyileştirmek için ölçün, bireyleri gözetlemek ve cezalandırmak için değil.
- Kanıt gerektirdiğinde inançları güncelleyin; fikir değiştirmek bir güçtür.
- [Psikolojik güvenlik](https://en.wikipedia.org/wiki/Psychological_safety) dürüst çözümleme ve itirazın ön koşuludur.

## Öneriler

### Veriyi kararlara bağlayın ve veri tiyatrosundan kaçının

Çözümlemeyi baştan belirli bir karara bağlayın: bulduğumuz şeye göre ne farklı yapacağız? Veri toplamadan önce kararı, seçenekleri ve hangi kanıtın hangisini destekleyeceğini, tercihen hangi sonucun fikrinizi değiştireceğini belirtin. Bu, çözümlemenin yalnızca önceden verilmiş bir kararı süslediği veri tiyatrosuna karşı korur. Gerçekçi hiçbir bulgu seçimi değiştirmeyecekse çözümlemeye harcama yapmayın. Yargı kararını dürüstçe verin ve bunu söyleyin. Sunumların bir grafik turuyla değil, karar ve önerisiyle başlamasında ısrar edin.

### Nedensellik üzerine dikkatle akıl yürütün

Çoğu iş ve politika sorusu nedenseldir (bu eylem bu sonucu doğuracak mı), ama eldeki verilerin çoğu gözlemseldir ve karıştırıcı değişkenlerle doludur. Takımlara korelasyon ile nedensellik arasındaki farkı ve tuzakları öğretin: karıştırıcı değişkenler, [seçilim yanlılığı](https://en.wikipedia.org/wiki/Selection_bias), ters nedensellik ve sahte korelasyon. Uygun olan yerde nedensel iddialar için rastgele deneyleri tercih edin. Deneylerin imkânsız olduğu yerde dikkatli [nedensel çıkarım](https://en.wikipedia.org/wiki/Causal_inference) teknikleri kullanın ve "ile ilişkili"den "neden olur"a kaymak yerine varsayımlarınızı açıkça belirtin. Tek bir korelasyon üzerine kurulmuş ikna edici bir hikâyeye özellikle şüpheyle yaklaşın.

### Belirsizliği paydaşlara iletin

Kesin nokta tahminleri olarak sunulan sayılar yanlış özgüveni davet eder. Aralıkları, güven ya da inanılırlık aralıklarını ve herhangi bir rakamın ardındaki temel varsayımları iletin. Karar vericilerin bilinenleri ve bilinmeyenleri kavraması için sade bir dil ve dürüst görseller (hata çubukları, aralıklar, senaryo bantları) kullanın. Verinin neyi gösterdiğini, neyi çıkarsadığınızı ve neyi varsaydığınızı ayırt edin. Güveni kanıta göre kalibre edin: ince veriden çıkan bir tahmini tam da olduğu gibi sunun. Dürüstçe iletilen belirsizlik, sahte kesinlikten daha fazla güven kurar, çünkü gerçeklikle temasa dayanır.

### Gözetim olmadan bir ölçüm kültürü kurun

Takımların başarı metriklerini düzenli olarak tanımladığı, çıktıları ölçtüğü ve onlardan öğrendiği bir ortam yaratın, ama ölçümü bireyleri izlemeye değil, sistemlere, süreçlere ve çıktılara yöneltin. İnsanları gözetlemek ve sıralamak için kullanılan metrikler oyunlanır, korku doğurur ve iyi kararların gerektirdiği dürüstlüğü yok eder (bunu [Goodhart yasası](https://en.wikipedia.org/wiki/Goodhart's_law) özetler: hedef haline gelen bir ölçü iyi bir ölçü olmaktan çıkar). Toplu, çıktı odaklı metrikleri tercih edin. Takımları kendi ölçülerini seçmeye dahil edin ve öğrenme metriklerini performans değerlendirmesinden ayırın. İnsanların kötü haberi ve itirazı erken dile getirmesi için psikolojik güvenliği koruyun.

### Sağlıklı veri alışkanlıkları ve okuryazarlığı besleyin

İnsanların bir grafiği eleştirel okuyabilmesi, bir metriğin tanımını sorgulayabilmesi ve yanıltıcı bir iddiayı fark edebilmesi için veri okuryazarlığını geniş çapta yükseltin. "Bunu nereden biliyoruz?" ve "Fikrimizi ne değiştirir?" sorularını olağanlaştırın. İnsanları kanıt ışığında görüşlerini güncelledikleri ve bilgilendirici biçimde başarısız olan deneyler yürüttükleri için ödüllendirin. Kesinlik uydurmak yerine "veri bize bunu söylemiyor" demeyi güvenli kılın. Tonu liderler belirler: kanıta dayanarak kararlarını değiştirdiklerinde ve belirsizliği kabul ettiklerinde kültür onları izler.

### Yanlılığa ve kötüye kullanıma karşı korunun

Öngörülebilir yanlılıklara dikkat edin: destekleyici veriyi seçerken [doğrulama yanlılığı](https://en.wikipedia.org/wiki/Confirmation_bias), eksik olanı görmezden gelirken [hayatta kalma yanlılığı](https://en.wikipedia.org/wiki/Survivorship_bias), ilk sayıya çapa atma ve olay sonrası incelemelerde geriye dönük yanlılık. Şeytanın avukatı incelemesi, ne bulmayı beklediğinizin önceden kaydedilmesi ve önemli çözümlemelerde çeşitli bakış açıları kurgulayın. Veri etiğini (adalet, şeffaflık ve zarardan kaçınma) ciddiye alın; özellikle kararlar insanların geçimini, yardımlarını ya da haklarını etkilediğinde.

## Ödünleşimler: artılar ve eksiler

| Seçim | Artılar | Eksiler | En uygun |
|---|---|---|---|
| Veri güdümlü (veri karar verir) | Yanlılığı azaltır, tutarlı | Bağlamı yok sayar, oyunlanır, kırılgan | İyi anlaşılmış alanlar |
| Veriye dayalı (veri artı yargı) | Kanıt ile bağlamı dengeler | Daha yavaş, yargı gerektirir | Karmaşık ya da yeni kararlar |
| Nedensellik için deney | Güçlü nedensel kanıt | Maliyetli, yavaş, her zaman uygulanabilir değil | Yüksek riskli, geri alınabilir seçimler |
| Gözlemsel çıkarım | Eldeki veriyi kullanır | Karıştırıcı değişken riski, daha zayıf iddialar | Deneyler imkânsızken |
| Çıktı/sistem metrikleri | İyileşmeyi yönlendirir, düşük oyunlanma | Daha az bireysel hesap verebilirlik | Öğrenme kültürleri |
| Bireysel gözetim | Ayrıntılı görünürlük | Oyunlanma, korku, aşınan güven | Nadiren haklı çıkarılabilir |

Belirleyici gerilim, titizlik ile hız ve uygulanabilirlik arasındadır. Rastgele deneyler en güçlü nedensel kanıtı verir, ama zamana mal olurlar ve tek seferlik stratejik ya da politika seçimleri için çoğu zaman imkânsızdırlar; orada karıştırıcı değişkenler hakkında dikkatli yargı ve açık varsayımlar yeterli olmalıdır. İkinci gerilim ölçüm ile güven arasındadır: bireyleri ne kadar ayrıntılı ölçerseniz o kadar çok görürsünüz ve o kadar az dürüst davranış elde edersiniz. Olgun bir kültür veriye dayalı yargıya ve çıktı odaklı, toplu ölçüme yönelir. Biraz daha az görünür kesinliği, ayakta kalan kararlar ve doğruyu söyleyen bir iş gücü karşılığında kabul eder.

## Takımınızla tartışılacak sorular

1. **Veriye bakmadan önce fikrinizi neyin değiştireceğini belirtiyor musunuz ve bu soru karar belgelerinize yazılı mı?** Bölümün veri tiyatrosuna karşı en güçlü korunması, veri toplamadan önce kararı, seçenekleri ve her birini destekleyecek kanıtı, tercihen seçiminizi tersine çevirecek sonucu adlandırmaktır. Gerçekçi hiçbir bulgu kararı değiştirmeyecekse dürüst hamle, çözümlemeyi atlamak ve yargı kararını açıkça vermektir. Tek bir stratejik ya da politika seçiminin bütün bir analitik programın maliyetinden fazlasını boşa harcayabildiği kurumlar ve kuruluşlar için bu disiplin yüksek kaldıraçlıdır. Yakın tarihli bir kararı getirin ve herhangi bir bulgunun onu değiştirip değiştiremeyeceğini, ya da grafiklerin yalnızca varılmış bir sonucu süsleyip süslemediğini sorun. "Fikrimizi ne değiştirir?" karar belgelerinizde standart bir istem değilse onu standart yapın ve sunumların bir grafik turuyla değil, öneriyle başlamasında ısrar edin.

2. **İkna edici bir korelasyon ortaya çıktığında harekete geçmeden önce karıştırıcı değişkenleri nasıl sorguluyorsunuz ve uygulanabildiği yerde deneyi tercih ediyor musunuz?** Bölüm, çoğu iş ve politika sorusunun nedensel, çoğu mevcut verinin ise gözlemsel ve karıştırıcı değişkenlerle, seçilim yanlılığıyla ve ters nedensellikle dolu olduğunu uyarır. Kendi örnekleri tek bir tuzağı tekrarlar: ilgili müşteriler kendiliğinden bir özelliğe ya da programa seçilir, bu yüzden daha düşük müşteri kaybı ya da daha yüksek iş bulma ile ham korelasyon, kontrollü bir karşılaştırmada kaybolur. O korelasyona göre hareket etmek, maliyetli ve yanlış yönlendirilmiş bir kampanya ya da politika demektir. Tek bir korelasyona dayanan yakın tarihli bir kararı getirin ve her iki tarafı da hangi gizli değişkenin yönlendirebileceğini sorun. Deney uygulanabiliyorsa onu tercih edin; değilse dikkatli nedensel çıkarım yöntemleri kullanın ve "ile ilişkili"den "neden olur"a kaymak yerine varsayımlarınızı açıkça belirtin.

3. **Metrikleriniz sistemleri ve çıktıları iyileştirmeyi mi, yoksa bireyleri izlemeyi mi hedefliyor ve öğrenme metriklerini performans değerlendirmesinden ayırdınız mı?** Bölüm keskin bir çizgi çeker: insanlara yöneltilen ölçüm oyunlanır, korku doğurur ve iyi kararların gerektirdiği dürüstlüğü yok eder; bu, bir ölçü hedef haline geldiğinde Goodhart yasasının öngördüğü bir dinamiktir. Toplu, çıktı odaklı metrikleri, takımları kendi ölçülerini seçmeye dahil etmeyi ve insanların kötü haberi erken dile getirmesi için psikolojik güvenliği korumayı tercih eder. Kamu ve kurumsal ortamlarda, ön saf çalışanlarını gözetlemek, doğru veriyi baştan mümkün kılan güveni aşındırır. Somut soruyu getirin: metriklerinizden hangileri bireyleri sıralamak ya da cezalandırmak için kullanılabilir ve insanlar baskı altında onları oyunlar mı? Öğrenme metrikleri ve performans değerlendirmesi birbirine karışmışsa ayırın; böylece ölçüm savunmacı davranışı değil, iyileşmeyi yönlendirir.

4. **Bir sayı karar vericiye ulaştığında varsayımlarıyla birlikte bir aralık olarak mı gelir, yoksa yanlış özgüveni davet eden bir nokta tahmini olarak mı?** Bölüm, dürüstçe iletilen belirsizliğin sahte kesinlikten daha fazla güven kurduğunu, çünkü gerçeklikle temasa dayandığını savunur; yine de bir lider temiz bir yanıt istediğinde tek bir kendinden emin rakama yönelim güçlüdür. Büyük bir takım için karşıt baskı gerçektir: aralıklar ve hata çubukları kararlılığı ödüllendiren yöneticilere kaçamak gelebilir, bu yüzden analistler duyulmak için uyarıları ayıklamayı öğrenir. Yakın tarihli bir raporu getirin ve verinin neyi gösterdiğini, neyi çıkarsadığınızı ve neyi varsaydığınızı ayırt edip etmediğini, ince veriye dayanan bir tahminin tam da öyle etiketlenip etmediğini kontrol edin. Bir rakamın yönetim kurulu paketine, bütçe başvurusuna ya da kamuya açık ifadeye girebildiği kurumsal ve kamu ortamlarında, kesinlik olarak sunulan bir nokta tahmini bir yükümlülüktür; bu yüzden sonuç doğuran sayıların bir aralık, temel varsayımlar ve güvenin sade bir ifadesini taşıdığı bir ev standardı üzerinde anlaşın.

5. **Burada "veri bize bunu söylemiyor" demek gerçekten güvenli mi ve bir metriğin nasıl tanımlandığına kimin itiraz etmesine izin var?** Bölüm veri okuryazarlığını ve psikolojik güvenliği ön koşul olarak ele alır: insanların bir grafiği eleştirel okuması, "bunu nereden biliyoruz?" diye sorması ve belirsizliği ceza almadan kabul etmesi gerekir, yoksa kültür varsayılan olarak sahte kesinlik üretir. Büyük bir kuruluş için gerilim şudur: geniş okuryazarlık gerçek eğitim süresi ve bütçe ister ve kıdemli birinin tercih ettiği metriği sorgulamak kariyere zarar verici hissedilebilir, bu yüzden sorgulanmamış sayılar yukarı doğru itirazsız yol alır. Bir metriğin tanımını ve kaynağını odadaki kimin gerçekten sorgulayabildiğine dair kanıt getirin ve son olarak birinin görüşünü güncellediği ya da bilgilendirici bir başarısızlığı raporladığı için cezalandırılmak yerine ödüllendirildiği zamanı hatırlayın. Kötü tanımlanmış bir ölçünün finansmanı ya da kamuya raporlamayı yönlendirebildiği kurumsal ve kamu kuruluşlarında, bir metriği sorgulama yetkisinin kimde olduğunu açıkça adlandırın ve bunu kullandıklarında onları koruyun.

6. **Önemli çözümlemeleri öngörülebilir yanlılığa karşı nasıl koruyorsunuz ve itirazı karardan sonra değil, önce kurguluyor musunuz?** Bölüm kanıtı sessizce bozan tuzakları sıralar: destekleyici veri seçerken doğrulama yanlılığı, eksik olanı görmezden gelirken hayatta kalma yanlılığı, ilk sayıya çapa atma ve olay sonrası incelemelerde geriye dönük yanlılık. Karşıt husus hızdır, çünkü şeytanın avukatı incelemesi, ne bulmayı beklediğinizin önceden kaydedilmesi ve çeşitli bakış açılarının hepsi bir kararı yavaşlatır ve son teslim baskısı altında ilk kesilen şeylerdir. Yakın tarihli yüksek riskli bir çözümlemeyi getirin ve birisi karşıt görüşü savunmakla görevlendirilseydi neyin yüzeye çıkacağını ve takımın sonuçları görmeden önce beklentilerini yazıp yazmadığını sorun. Kararların insanların geçimini, yardımlarını ya da haklarını etkilediği kurumsal ve özellikle kamu bağlamlarında, veri etiğini ve yapılandırılmış itirazı, yoğun bir çeyreğin sessizce bırakabileceği ekstralar olarak değil, sonuç doğuran çözümlemelerde kalıcı gereklilikler olarak ele alın.

## Sektör merceği

**Girişim.** Analist yokken ve bahis başına yalnızca birkaç haftalık pist varken, karar biliminiz bir işlev değil, tek bir alışkanlıktır: büyük bir taahhütten önce hangi sonucun fikrinizi değiştireceğini ve ucuz bir deneyin bunu bir toplantıdan daha hızlı yanıtlayıp yanıtlayamayacağını sorun. Çeyreği tek bir gösterişli korelasyona bahse yatırmaya karşı sıkı korunun, çünkü minik bir takım yanlış yönlendirilmiş bir yol haritasından toparlanamaz. Hafif tutun: hiç yapmayacağınız resmî bir inceleme değil, karar belgesinde durmanızı sağlayacak sinyali adlandıran yazılı bir satır.

**Küçük işletme.** Büyük olasılıkla bir veri uzmanınız yok ve analitiği zaten kullandığınız araçların içinden satın alıyorsunuz; bu yüzden risk, bir metriğin nasıl tanımlandığını ya da karşılaştırmasının adil olup olmadığını sorgulamadan bir tedarikçi panosuna güvenmektir. Kıt dikkatinizi araçlara değil, akıl yürütmeye harcayın: işi gerçekten ilerleten bir ya da iki kararda korelasyonu nedensellikten ayırın ve geri alamayacağınız parayı taahhüt etmeden önce dürüst aralığı kendinize söyleyin. Bir araç bir kararı otomatikleştirmeyi önerdiğinde, yanlış bir çağrının size bir müşteriye mal olacağı her yerde döngüde bir insan tutun.

**Kurumsal.** Birçok takım arasında sorun tutarlılık ve yönetişimdir: çözümlemelerin kararı ve bırakma ölçütlerini baştan adlandırdığı, nedensel iddiaların varsayımlarını belirttiği ve sonuç doğuran sayıların yönetim kurulu paketlerine ve denetimlere aralıklarla girdiği ortak bir beklenti. Ölçümün gözetime ve oyunlamaya dönüşmemesi için öğrenme metriklerini performans değerlendirmesinden kuruluş genelinde ayırın. Geniş veri okuryazarlığına ve şeytanın avukatlığı ile önceden kayıt gibi inceleme pratiklerine yatırım yapın; böylece kendinden emin bir sunucu ölçekte kanıtın yerini alamaz.

**Kamu.** Satın alma, şeffaflık ve kamusal hesap verebilirlik her nedensel iddiada bahisleri yükseltir, çünkü sahte bir korelasyonla gerekçelendirilen bir politika kamu parasını yanlış dağıtır ve vatandaşlara zarar verebilir. Program değerlendirmesi için titiz karşılaştırma tasarımlarını tercih edin, etkileri denetim organlarına belirtilmiş varsayımlarla aralıklar olarak iletin ve bir denetimin izleyebilmesi için akıl yürütmeyi belgeleyin. Ölçümü vaka görevlilerini gözetlemeye değil, program çıktılarına yöneltin ve kamuya, kanıtın kararı nasıl şekillendirdiğinin net bir anlatımını verin.

## Örnekler

**Girişim.** Seri A öncesi bir girişim, topluluk forumuna katılan kullanıcıların çok daha az müşteri kaybettiğini fark etti ve kurucular bütün yol haritasını forum özelliklerine yöneltmeye hazırdı. Taahhütten önce biri fikirlerini neyin değiştireceğini sordu ve hızlı bir bakış, zaten bağlı müşterilerin foruma katılma zahmetine girenler olduğunu gösterdi. Çeyreği bir korelasyona bahse yatırmak yerine küçük bir deney yürüttüler ve "fikrimizi ne değiştirir?" sorusunu karar belgelerinde standart bir soru yaptılar.

**Kurumsal.** Bir finansal hizmetler şirketi, belirli bir özelliği kullanan müşterilerin çok daha düşük müşteri kaybına sahip olduğunu fark etti ve herkesi o özelliğe itecek maliyetli bir kampanyayı neredeyse başlatıyordu. Bir karar bilimi incelemesi bariz karıştırıcı değişkeni işaretledi: zaten ilgili müşteriler kendiliğinden o özelliğe seçilmişti. Kontrollü bir deney sonra özelliğin müşteri kaybı üzerinde nedensel etkisinin az olduğunu gösterdi. Şirket büyük bir yanlış yönlendirilmiş yatırımdan kaçındı ve liderlik büyük harcamalardan önce "fikrimizi ne değiştirir?" sorusunu standart bir soru olarak benimsedi.

**Kamu.** Bir istihdam programını değerlendiren bir kamu kurumu, katılımcıların yüksek oranda iş bulduğu ham istatistikten başarı iddia etmeye direndi; motive olmuş insanların bu tür programlara kendiliğinden seçildiğini fark etmişti. Titiz bir karşılaştırma tasarımı kullandı ve tahmini etkiyi belirtilmiş varsayımlarla bir aralık olarak denetim organlarına iletti. Ölçüm, vaka görevlilerini gözetlemek yerine program çıktılarına odaklandı; bu, hesap verebilirliği ve iyileşmeyi yine de yönlendirirken ön saf güvenini korudu.

## İş gerekçesi: motivasyonlar, YG ve TSM

Karar biliminin YG'si, kendinden emin yanlış kararların önlenen maliyeti ve bir kuruluşun binlerce kez verdiği kararların iyileşen kalitesidir. Sahte bir korelasyonla gerekçelendirilen tek bir büyük stratejik ya da politika seçimi, iyi karar pratikleri kurmanın bütün maliyetinden çok daha fazlasını boşa harcayabilir. Daha iyi kalibrasyon (neyi bildiğinizi ve neyi bilmediğinizi bilmek) bahisleri uygun büyüklüğe getirmenize ve hem pervasız taahhütlerden hem felçten kaçınmanıza olanak verir. Toplamda veriye dayalı bir kültür bileşik getiri sağlar: her takımın biraz daha iyi, daha iyi akıl yürütülmüş kararlar vermesi muazzam bir kaldıraçtır.

Benimseme maliyeti çoğunlukla kültürel ve eğitseldir: veri okuryazarlığı eğitimi, dikkatli çözümleme ve inceleme için zaman ve liderliğin kararlarını değiştirme ve belirsizliği kabul etme isteği. Önceki bölümlerin platformlarından dolar olarak daha ucuzdur ama kurması daha zordur, çünkü güçlü insanlardan kanıtla yönetilmelerini ister. Bunu benimsememenin maliyetiyle tartın: analitik emeği boşa harcayan veri tiyatrosu, en kendinden emin sesin yönlendirdiği kararlar, gerçeklikle temasta çöken nedensel iddialar ve gözetimin yerleştiği yerde metrikleri oyunlayan ve kötü haberi saklayan bir iş gücü. Liderliğe gerekçe basittir. Önceki tüm veri yatırımı yalnızca içgörüden karara giden son kilometre sağlamsa karşılığını verir ve karar bilimi o son kilometredir.

## Anti-kalıplar ve tuzaklar

- Veri tiyatrosu: önceden verilmiş bir kararı haklı çıkarmak için üretilen çözümleme.
- Karıştırıcı değişkenleri sorgulamadan "ile ilişkili"den "neden olur"a kaymak.
- Nokta tahminlerini kesinlik olarak sunmak, belirsizlik aralığını gizlemek.
- Doğrulama yanlılığı: yalnızca tercih edilen sonucu destekleyen veriyi aramak.
- En yüksek ücretli kişinin görüşünün kanıtı ezdiği HiPPO kararları.
- Metrikleri bireysel gözetime çevirmek, oyunlanma ve korku doğurmak.
- Goodhart yasası iş başında: önemli olanı ölçmeyi bırakan hedef metrik.
- İnsanları bilgilendirici başarısızlıklar için cezalandırmak, dürüstlüğü ve deneyi öldürmek.

## Olgunluk modeli

- **Düzey 1, Başlangıç:** Kararlar hiyerarşi ve sezgiyle yürür ve en yüksek sesli ya da en kıdemli kişi kazanır. Korelasyon serbestçe nedensellik sayılır, belirsizlik görmezden gelinir ve kullanımdaki az sayıdaki metrik bireyleri gözetler ve oyunlanır.
- **Düzey 2, Geliştirme:** Bazı takımlar veriye başvurur ve nedensel tuzakların farkındadır, ama çözümleme çoğu zaman seçicidir ve önceden verilmiş bir kararı haklı çıkarmak için üretilir. Belirsizlik nadiren iletilir ve ölçüm pratikleri takımdan takıma tutarsızdır.
- **Düzey 3, Standartlaştırma:** Kuruluş ortak pratiği belgeler ve uygular: çözümlemeler önceden belirlenmiş ölçütlerle adlandırılmış bir karara bağlanır, takımlar korelasyon ile nedenselliği ayırt eder ve nedensel iddialar için deneyleri tercih eder, sayılar aralıklar ve belirtilmiş varsayımlar taşır ve ölçüm bireylere değil çıktılara yöneltilir; psikolojik güvenlik korunur.
- **Düzey 4, Yönetme:** Karar kalitesi temel çizgilere karşı ölçülür ve kontrol edilir. Kuruluş, çözümlemelerin veri gelmeden önce kaç kez bir bırakma sinyali adlandırdığını, sonuç doğuran rakamların kaçının iletilmiş bir aralıkla çıktığını, kaç nedensel iddianın çıplak korelasyon yerine deneylere dayandığını ve kararların kanıt üzerine tersine dönüp dönmediğini izler. Önceden kayıt ve şeytanın avukatı incelemesi gibi yanlılık koruma pratikleri denetlenir ve oyunlanmaya başlayan metrikler yakalanıp emekli edilir.
- **Düzey 5, Orkestrasyon:** Sağlam akıl yürütme sürekli iyileştirilir ve kuruluş genelinde bütünleşir. "Fikrimizi ne değiştirir?" her büyük karardan önce rutindir, nedensel titizlik ve dürüst belirsizlik kültürel normlardır ve liderler kanıta göre görünür biçimde güncelleme yapar ve neyin bilinmediğini kabul eder. Ölçüm gözetim olmadan öğrenmeyi yönlendirir, karar pratikleri kuruluş ve riskleri değiştikçe uyum sağlar ve sonuç olarak her düzey daha iyi karar verir.

## Tartışma fikirleri

- Kuruluşunuzda veri, önceden verilmiş kararları süslemek için nerede kullanılıyor?
- Hangi yakın tarihli karar, nedensel olmayabilecek bir korelasyona dayanıyordu?
- Raporlarınız belirsizliği ne kadar dürüst iletiyor ve aralıklara kim direniyor?
- Metrikleriniz sistemleri iyileştirmeyi mi yoksa bireyleri izlemeyi mi hedefliyor?
- Bir lider en son ne zaman veri yüzünden görünür biçimde bir kararı değiştirdi?
- Ölçüm arayışının gözetime kaymasını nasıl önlüyorsunuz?

## Önemli çıkarımlar

- Verinin amacı daha iyi kararlardır; veri tiyatrosuna karşı korunun.
- Veriye bakmadan önce fikrinizi neyin değiştireceğini belirtin.
- Korelasyonu asla nedensellikle karıştırmayın; karıştırıcı değişkenleri sorgulayın ve deneyleri tercih edin.
- Belirsizliği dürüstçe iletin; sahte kesinlik başarısız olduğunda güveni yok eder.
- Veriye dayalı olun, veri tarafından köleleştirilmeyin; yargı ve bağlam hâlâ önemlidir.
- Öğrenmek için sistemleri ve çıktıları ölçün, gözetlemek için bireyleri değil.
- İnsanların inançlarını güncellemesi ve kötü haberi dile getirmesi için psikolojik güvenliği koruyun.

## Kaynaklar ve ileri okuma

- Daniel Kahneman, "Thinking, Fast and Slow."
- Judea Pearl and Dana Mackenzie, "The Book of Why."
- Douglas W. Hubbard, "How to Measure Anything."
- Nate Silver, "The Signal and the Noise."
- Cathy O'Neil, "Weapons of Maths Destruction."
- Darrell Huff, "How to Lie with Statistics."
- Philip Tetlock and Dan Gardner, "Superforecasting."
- Charles Wheelan, "Naked Statistics."
