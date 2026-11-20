# 6.5 Sorumlu ve güvenilir yapay zeka

## Genel bakış ve motivasyon

Sorumlu ve güvenilir yapay zeka; adil, şeffaf, hesap verebilir, güvenli ve mahremiyete saygılı yapay zeka sistemleri kurma ve işletme pratiğidir. Bunların hepsini etkilenen insanlara ve düzenleyicilere gösterebilmek de buna dahildir. Yapay zeka, insanların hayatını şekillendiren kararları (işe alım, kredi, yardıma uygunluk) üstlendikçe soru artık yalnızca "çalışıyor mu?" değil, "doğru mu ve gerekçelendirebilir miyiz?" haline geliyor. Ortalamada doğru olan bir sistem yine de bir alt gruba karşı haksız, etkilediği kişiye açıklanamaz ya da kötüye kullanıldığında güvensiz olabilir. Güveni, bu boyutları bilinçli biçimde ele alarak kazanırsınız; kendiliğinden hallolmalarını umarak değil.

Büyük takımlar için sorumlu yapay zeka tek bir kişinin işi ya da sonda işaretlenecek bir kutu olamaz. Onu sistemleri nasıl tasarladığınıza, değerlendirdiğinize, devreye aldığınıza ve yönettiğinize, net sahiplik ve yükseltme yollarıyla işleyin. Ölçekte küçük önyargılar ve gözetimdeki boşluklar çok sayıda insanı etkiler. Tek bir yüksek profilli başarısızlık itibarınıza zarar verebilir ve düzenlemeyi davet edebilir. Yönetişim çerçeveleri tam da gelişigüzel iyi niyetin ölçeklenmemesi nedeniyle vardır.

Kamu ve düzenlemeye tabi kurumlar bağlayıcı yükümlülüklerle karşı karşıyadır. [AB Yapay Zeka Yasası](https://en.wikipedia.org/wiki/Artificial_Intelligence_Act) gibi gelişen hukuk, riske göre derecelendirilmiş gereksinimler getirir. NIST Yapay Zeka Risk Yönetimi Çerçevesi ve ISO/IEC 42001 gibi standartlar bunları karşılamanız için yapılandırılmış yollar sunar. Kamu kurumları hukuka aykırı ayrımcılıktan kaçınmalı, otomatik kararlara itiraz için yollar sağlamalı ve kamu yetkisinin kullanımında yapay zekanın nasıl kullanıldığı konusunda şeffaf olmalıdır. Bu ortamlarda sorumlu yapay zeka hem etik bir görev hem hukuki bir zorunluluktur.

*Ayrıca bakın:* bölüm 6.1 (yapay zeka stratejisi ve hazırlık), bölüm 10.5 (etik, hesap verebilirlik ve kamu yararı) ve bölüm 4.5 (gizlilik ve veri koruma).

## Temel ilkeler

- Adalet, varsayılacak değil ölçülüp yönetilecek bir tasarım hedefidir.
- Yapay zeka kararlarından etkilenen insanlar bir açıklamayı ve bu kararlara itiraz yolunu hak eder.
- Hesap verebilirlik insanlarda ve kurumdadır; asla modelde değil.
- Gizlilik ve güvenlik, kötüye kullanıma ve istismara karşı korunma dahil, tasarıma yerleştirilmelidir.
- Yönetişim, savunulabilir ve denetlenebilir olması için tanınmış çerçeveleri izlemelidir.
- İnsan gözetimi, geçersiz kılma ve durdurma konusunda gerçek yetkiyle anlamlı olmalıdır.
- Yapay zekanın daha geniş maliyetlerini, çevresel ayak izi dahil, hesaba katın.

## Öneriler

### Önyargıyı ve haksızlığı tespit edip azaltın

Bağlamınız için adaletin ne anlama geldiğini tanımlayın. Birden çok, zaman zaman çelişen matematiksel tanım vardır ve doğru olan karara ve hukuka bağlıdır. Modelleri, temsil edici veri kullanarak korunan ve savunmasız gruplar arasındaki farklı performans açısından test edin. Bunu devreye almadan önce yapın ve sonrasında da sürdürün, çünkü nüfuslar kaydıkça [önyargı](https://en.wikipedia.org/wiki/Algorithmic_bias) ortaya çıkabilir. Daha iyi veriyle, yeniden ağırlıklandırmayla, kısıtlarla ya da sistemin kullanılış biçimini değiştirerek azaltın ve kabul ettiğiniz ödünleşimleri belgeleyin. Korunan bir özniteliği kaldırmak önyargıyı kaldırmaz, çünkü vekil değişkenler kalır. Adaleti tek seferlik bir onay olarak değil, sürekli bir ölçüm ve yönetim disiplini olarak ele alın.

### Açıklanabilirlik, yorumlanabilirlik ve şeffaflık sağlayın

Açıklamanın düzeyini riske ve hedef kitleye uydurun. Sonuç doğuran kararlarda etkilenen kişilere anlayıp harekete geçebilecekleri net, sade dilde bir gerekçe verin. İç yönetişim için sistemi hata ayıklayıp savunmaya yetecek kadar teknik [yorumlanabilirliği](https://en.wikipedia.org/wiki/Explainable_artificial_intelligence) koruyun. Riskin yüksek ve yorumlanabilirliğin ulaşılabilir olduğu yerlerde özünde yorumlanabilir modelleri tercih edin. Karmaşık modellerin gerekli olduğu yerlerde, sınırları konusunda dürüst olarak açıklama teknikleri kullanın. Yapay zekanın kullanıldığı konusunda, özellikle kamuyla etkileşimlerde, baştan şeffaf olun.

### Tanınmış çerçevelerle yönetin

Kendiniz icat etmek yerine yapılandırılmış bir yönetişim yaklaşımı benimseyin. **NIST Yapay Zeka Risk Yönetimi Çerçevesi** işi, yapay zeka riskini yönetme, haritalama, ölçme ve ele alma etrafında düzenler. **AB Yapay Zeka Yasası** sistemleri riske göre sınıflandırır ve buna göre yükümlülükler getirir; yüksek riskli kullanımlar için katı gereksinimler vardır. **ISO/IEC 42001** denetlenebilen ve sertifikalandırılabilen bir yapay zeka yönetim sistemi tanımlar. Sistemlerinizi bu çerçevelere eşleyin. Model ve veri kartları (bir modelin ya da veri kümesinin amacının, performansının ve sınırlarının standartlaştırılmış özetleri) gibi belgeleri sürdürün. Devreye almadan önce risk değerlendirmeleri yapın ve yapay zeka sistemlerinin risk düzeyleri ve sahipleriyle bir envanterini tutun. İyi yönetişim net roller, karar hakları ve yükseltme yolları atar.

### İnsan gözetimini, hesap verebilirliği ve itirazı sağlayın

Sonuç doğuran kararlarda bir insanı anlamlı biçimde kontrolde tutun; sistemi geçersiz kılmak için gerçek yetkisi ve gereken bilgisi olsun, bir onay mührü olmasın. Net hesap verebilirlik atayın: her sistemin davranışından sorumlu bir sahip belirleyin. Otomatik kararlardan etkilenen insanlara, açıklama hakkı ve sonucu değiştirebilecek bir insana itiraz etmek için uygulanabilir bir süreç tanıyın. İtirazları ve denetimleri adil ve çabuk ele alabilmeniz için kararları ve dayanaklarını günlüğe alın.

### Gizliliği, güvenliği ve kötüye kullanıma karşı korumayı sağlayın

Topladığınız ve kullandığınız kişisel veriyi en aza indirin, hukuki bir dayanak oluşturun ve ilgili hassasiyete uygun gizlilik teknikleri uygulayın. Sistemlerin manipüle edilebileceği, kısıtlarından kurtarılabileceği (jailbreak) ya da zarar vermek için kötüye kullanılabileceği yolları bulmak için sistemleri devreye almadan önce ve sonra [kırmızı takımla](https://en.wikipedia.org/wiki/Red_team) sınayın ve bulduklarınızı düzeltin. Zararlı içerik üretmeye, hassas veri sızdırmaya ya da istismara olanak vermeye karşı güvenceler kurun. Olaylara hazırlanın: izleme, müdahale ve açıklama. Yalnızca amaçlanan kullanımı değil, [çift kullanımı](https://en.wikipedia.org/wiki/Dual-use_technology) (aynı yeteneğin hem yararlı hem zararlı amaçlara hizmet etmesi) ve aşağı akış kötüye kullanımını da düşünün.

### Çevresel maliyeti hesaba katın

Büyük modelleri eğitmek ve sunmak önemli miktarda enerji ve su tüketir. Başlıca yapay zeka iş yüklerinin ayak izini ölçün ve raporlayın. İhtiyacı karşıladıkları yerde verimli modelleri ve donanımı tercih edin. Varsayılan olarak en büyük modeli seçmek yerine modelleri göreve uygun boyutlandırın ve çevresel maliyeti mimari ve tedarik kararlarına katın.

## Ödünleşimler: artılar ve eksiler

| Gerilim | Bir taraf | Diğer taraf |
|---|---|---|
| Doğruluk ve adalet | En yüksek ortalama doğruluk | Gruplar arasında hakkaniyetli sonuçlar |
| Performans ve yorumlanabilirlik | Karmaşık, güçlü modeller | Açıklanabilir, savunulabilir modeller |
| Otomasyon ve gözetim | Verimlilik ve ölçek | İnsan kontrolü ve hesap verebilirlik |
| Veri faydası ve gizlilik | Daha fazla veriden daha zengin modeller | Veri en aza indirme ve koruma |
| Yetenek ve güvenlik | Geniş, açık işlevsellik | Kısıtlı, korunan davranış |
| Hız ve yönetişim | Hızlı devreye alma | Kapsamlı inceleme ve belgeleme |

Bedava öğle yemeği nadiren vardır. Adaleti iyileştirmek biraz doğruluğa mal olabilir. Yorumlanabilirlik biraz performansa mal olabilir. Yönetişim zamana mal olur. Sorumlu yol, bu ödünleşimleri bilinçli yapmak, belgelemek ve riskin yüksek olduğu yerlerde etkilenen insanlar ve savunulabilirlik lehine seçmektir. Yönetişimi yeniliğin freni olarak çerçevelemek yanlış bir ikilemdir. Yönetilmeyen yapay zeka riski, sürdürülebilir yenilik için başlı başına bir tehdittir.

## Takımınızla tartışılacak sorular

1. **Devreye aldığımız yapay zeka sistemlerinden hangilerini AB Yapay Zeka Yasası yüksek riskli olarak sınıflandırırdı ve bugün bu yükümlülükleri karşılıyor muyuz?** Riske göre derecelendirilmiş hukuk artık varsayımsal değil, bağlayıcıdır ve işe alım, kredi ya da yardıma uygunluk kararı veren bir sistem, zaten ihlal ediyor olabileceğiniz katı gereksinimler taşıyabilir. Büyük bir kurum için bu soru, yönetişimin "halledildiği" yönünde rahat bir varsayım yerine dürüst bir envanteri zorunlu kılar. Yapay zeka sistemlerinin risk düzeyleri ve sahipleriyle listesini, ilgili olduğu yerde AB Yapay Zeka Yasası, NIST Yapay Zeka Risk Yönetimi Çerçevesi ve ISO/IEC 42001'e karşı eşlenmiş olarak getirin. İzlenecek sinyal; risk sınıflandırması, etki değerlendirmesi ve model ya da veri kartı olmayan her sonuç doğuran sistemdir. Kamu yetkisi kullanan kamu kurumları için eksik yükümlülükler bir birikmiş iş kalemi değil, hukuki risktir ve cevap, o sistemlerin gerektirdiği değerlendirmeleri ve belgeleri tetiklemelidir.

2. **Modellerimizden biri birini reddettiğinde, o kişi sade dilde bir gerekçe alabiliyor ve sonucu gerçekten tersine çevirebilecek bir insana ulaşabiliyor mu?** Açıklama hakkı ve uygulanabilir bir itiraz, hesap verebilir yapay zekayı, insanlara başvuru yolu bırakmadan zarar veren bir kara kutudan ayıran şeylerdir. Ortalamada ölçülen adalet yine de bir bireyi yarı yolda bırakabilir ve devreye aldıktan sonra seçilen yorumlanabilirlik çoğunlukla tiyatrodur. Devreye alınmış belirli bir kararı getirin ve izleyin: etkilenen kişinin aldığı gerekçe, itiraz kanalı ve öbür uçtaki insanın geçersiz kılmak için gerçek yetkisi ve günlüğe alınmış dayanağı olup olmadığı. Kamu ve düzenlemeye tabi ortamlarda itiraz yolu çoğu zaman bir nezaket değil, hukuki bir gerekliliktir. Gerekçe anlaşılmazsa ya da itiraz bir onay mührüne çıkıyorsa, bir sonraki sürümden önce kapatılacak boşluk budur.

3. **Bir model zarar verdiğinde hesap verecek tek isimli kişi kim ve onu durdurmak için gerçek yetkisi var mı?** Hesap verebilirlik insanlarda ve kurumdadır, asla modelde, ama bu ilke her sisteme bir isim bağlanıp o kişi gerçekten fişi çekebilene kadar boştur. Büyük bir takım için dağınık sahiplik, bir adalet başarısızlığı ya da jailbreak ortaya çıktığında herkesin başka birinin baktığını varsayması demektir. Sahiplik haritanızı, yükseltme yollarınızı ve gözetimin anlamlı olduğuna dair kanıtı getirin: isimli sahip sistemi geçersiz kılmak ya da durdurmak için bilgiye ve güce mi sahip, yoksa yalnızca onaylamak için mi? Henüz hayal etmediğiniz kötüye kullanım ve istismar için nasıl kırmızı takım yaptığınızı tartışın, çünkü yalnızca amaçlanan kullanımı test etmek, manşetlere çıkan başarısızlıkları kaçırır. Cevap, onu durdurabilecek hesap verebilir bir sahibi olmayan hiçbir sonuç doğuran sistem bırakmamalıdır.

4. **Sonuç doğuran her model için hangi adalet tanımını seçtik, kim onayladı ve alt grup metriklerimiz üretimde gerçekten tutuyor mu?** Adaletin birbiriyle çelişen birkaç matematiksel tanımı vardır; bu yüzden eşit yanlış pozitif oranlarını sağlayan bir model eşit sonuçları ihlal edebilir ve bir tanım seçmek, eğitim döngüsünü kim yazdıysa ona bırakılmaması gereken bir değer yargısıdır. Büyük bir takım için incelenmemiş bir varsayılan, seçimi kodun içine gizler ve her aşağı akış grubuna kimsenin tartışmadığı bir karar miras bırakır. Optimize ettiğiniz adalet metriğini, test ettiğiniz korunan ve savunmasız grupları, kullandığınız temsil edici veriyi ve lansmandan beri gördüğünüz kaymayı getirin; çünkü korunan bir özniteliği kaldırmak, önyargıyı canlı tutan vekil değişkenleri bırakır. Kurumsal ve kamu ortamlarında, bir adalet ödünleşimini kabul etme yetkisine sahip kişiyi belirleyin ve kaydedin, çünkü bir düzenleyici ya da bir ombudsman, kredi, yardım ya da iş reddedilen insanlar için bu adalet tanımının doğru olduğuna kimin karar verdiğini soracaktır. Devreye aldıktan sonra hiçbir alt grup metriği izlenmiyorsa, modeli adil değil ölçülmemiş sayın.

5. **Her sistem en az ne kadar kişisel veriyle çalışabilir ve düşünmek istemediğimiz kötüye kullanım ve çift kullanım için onu kırmızı takımla sınadık mı?** Gizlilik ve güvenlik tasarıma yerleştirilmelidir ve hem ihlal riskini hem istismar yüzeyini azaltmanın en ucuz yolu en baştan daha az veri toplamak ve tutmaktır; yine de takımlar girdileri düzenli olarak "belki sonra işe yarar" diye biriktirir. Büyük bir kurum için her ekstra alan bir hukuki dayanak sorusu, bir saklama yükümlülüğü ve bir saldırgan ya da jailbreak için daha büyük bir ödüldür. Her sistemin veri envanterini ve hukuki dayanağını, manipülasyon, sızıntı ve zararlı üretim için yapılan kırmızı takım sonuçlarını ve meşru bir kullanıcıya yardım eden aynı özelliğin kötü niyetle hareket eden birine de yardım ettiği çift kullanımlı yeteneklerin dürüst bir listesini getirin. Düzenlemeye tabi ve kamusal bağlamlarda bunu olay planınıza bağlayın: izleme, müdahale ve açıklama; çünkü hassas veri sızdıran ya da jailbreak yapılabilir bir sistem çıkaran bir kamu kurumu yalnızca utançla değil, yasal görevlerle karşılaşır. Kırmızı takım yalnızca amaçlanan yolu zorladıysa, sistemi değil demoyu test etmişsinizdir.

6. **Başlıca yapay zeka iş yüklerimizin çevresel ayak izini ölçüp sahipleniyor muyuz, yoksa "en büyük modeli kullan" fiyatlanmamış bir varsayılan mı?** Büyük modelleri eğitmek ve sunmak gerçek enerji ve su tüketir ve daha küçük bir modelin halledeceği görevlerde varsayılan olarak en büyük modeli seçmek, bir mühendislik kestirmesini kurumun hiçbir panoda görmediği yinelenen bir maliyete çevirir. Birçok iş yükü çalıştıran büyük bir takım için çağrı başına küçük verimsizlikler birikerek, açıklama beklentileri sıkıldıkça bir tedarik ve raporlama yükümlülüğüne dönüşen bir ayak izi oluşturur. En ağır iş yüklerinizin ölçülmüş ayak izini, model boyutlarının görevin gerçekten ihtiyaç duyduğu doğrulukla karşılaştırmasını ve uygun boyuta indirebileceğiniz donanım ve sunum seçimlerini getirin. Kurumsal ve kamu ortamlarında bunu sürdürülebilirlik taahhütlerine ve tedarik ölçütlerine bağlayın, çünkü kamu kurumları giderek çevresel etkiyi raporlamak ve harcamayı gerekçelendirmek zorunda ve ölçülmemiş bir ayak izi, bir gün üretmeniz istenecek ama üretemeyeceğiniz bir rakamdır. Çevresel maliyetin model seçiminde resmi bir girdi olup olmayacağına karar verin ya da bugün olmadığını kabul edin.

## Sektör merceği

**Girişim.** Bir yönetişim kurulunu kadrolandıramazsınız; bu yüzden yine de sayılan hafif sürümünü yapın. Karar sonuç doğurduğunda yorumlanabilir modelleri seçin, tek sayfalık bir model kartı yazın, ölçebildiğiniz gruplar arasında farklı sonuçlar için test edin ve büyüdükçe adalete geri dönebilmek için kararları günlüğe alın. Her olumsuz karara sade bir gerekçe ve bir insana giden bir yol verin. Bunu atlamak hız değildir; tek bir haksız karar basına ya da bir düzenleyiciye ulaşırsa karşılayamayacağınız bir yükümlülüktür.

**Küçük işletme.** Özel bir uzmanınız yokken sorumlu yapay zekayı bir satın alma sorusu olarak ele alın: adalet testlerini belgeleyen, model ve veri kartlarını açan ve yapay zekanın kullanıldığını müşterilere açıklamanıza izin veren satıcıları tercih edin. Araçlarınızın hangi kişisel veriyi topladığını ve onu kullanmak için hukuki dayanağınız olup olmadığını bilin. Yanlış bir otomatik cevabın bir müşteriye zarar verebileceği yerlerde, inceleyemeyeceğiniz ya da açıklayamayacağınız bir araca güvenmek yerine döngüde bir insan tutun.

**Kurumsal.** Görev, birçok takım arasında ölçekte yönetişimdir: her sistemi NIST Yapay Zeka Risk Yönetimi Çerçevesi, AB Yapay Zeka Yasası ve ISO/IEC 42001'e eşleyin, risk düzeyleri ve isimli sahiplerle bir envanter tutun ve lansmandan önce ve sonra adalet, güvenlik ve gizlilik testi isteyin. Gruplar tekerleği yeniden icat etmesin diye model ve veri kartlarını, kırmızı takımı ve itiraz süreçlerini standartlaştırın. Yönetişim, gözetim ve yorumlanabilirlik maliyetlerini açıkça bütçeleyin ve yönetilmeyen yapay zeka riskini faaliyet ruhsatı için bir tehdit sayın.

**Kamu.** Tedarik kuralları, şeffaflık ve kamusal hesap verebilirlik her seçimi şekillendirir. Sade dilde bir şeffaflık bildirimi yayımlayın, devreye almadan önce bir etki değerlendirmesi yapın ve bir vatandaşı etkileyen her eylem için uygulanabilir bir itiraz yoluyla anlamlı insan karar vermesini sürdürün. Satıcıların model sınırlamalarını açıklamasını ve veri taşınabilirliği sağlamasını isteyin, hukuka aykırı ayrımcılıktan kaçının, her sistem için hesap verecek bir yetkili belirleyin ve başlıca iş yüklerinin çevresel ayak izini raporlayın.

## Örnekler

**Girişim.** Erken bir kredi puanlama özelliği kuran küçük bir kredi girişimi bir yönetişim kurulunu kadrolandıramadı; bu yüzden yine de önemli olan hafif sürümünü yaptı. İki kurucu modeli birlikte onayladı, ölçebildikleri gruplar arasında farklı sonuçlar için test etti ve verisini, sınırlarını ve bilinen risklerini kapsayan kısa, tek sayfalık bir model kartı yazdı. Reddedilen her başvurana sade bir gerekçe ve bir insan incelemesine giden bir yol verebilmek için daha basit, daha yorumlanabilir bir model seçtiler ve büyüdükçe adalete geri dönebilmek için kararları günlüğe aldılar.

**Kurumsal.** Bir kredi modeli devreye alan bir banka, bir yapay zeka yönetişim kurulu kurdu, modeli yüksek riskli bir kategoriye eşledi ve lansmandan önce ve sonra demografik gruplar arasında adalet testi istedi. Modeli bir model kartında belgeledi. Reddedilen başvuru sahiplerine sade dilde bir gerekçe ve bir insan sigortacıya itiraz hakkı verdi ve sistemi manipülasyon için kırmızı takımla sınadı. Biraz daha az doğru ama daha yorumlanabilir bir model seçti, çünkü her kararı düzenleyicilere açıklamak ve savunmak zorundaydı.

**Kamu.** Denetim kaynaklarını tahsis etmeye yardım için yapay zeka kullanan bir kamu kurumu, programını NIST YZ RMF'ye ve geçerli yapay zeka hukukunun ilgili hükümlerine hizaladı. Sistemin nasıl çalıştığını ve güvencelerini anlatan bir şeffaflık bildirimi yayımladı. Devreye almadan önce bir etki değerlendirmesi yaptı, bir vatandaşı etkileyen her eylem için anlamlı insan karar vermesini sürdürdü ve bir itiraz süreci sağladı. Adalet sürekli izlendi, iş yükünün çevresel maliyeti raporlandı ve sistemden sorumlu olarak hesap verecek bir yetkili belirlendi.

## İş gerekçesi: motivasyonlar, YG ve TSM

Sorumlu yapay zeka değer yarattığı kadar değeri korur. YG büyük ölçüde kaçınılan maliyettir: daha az ayrımcılık iddiası, düzenleyici ceza ve itibar felaketi; daha pürüzsüz denetimler; ve benimsemeyi sürükleyen daha büyük kullanıcı ve kamu güveni. Güvenilir sistemler aynı zamanda daha dayanıklıdır, çünkü adaleti ve güvenliği üreten disiplin daha iyi mühendisliği de üretir.

TSM; yönetişim personelini, adalet ve güvenlik testini, belgelemeyi, kırmızı takımı, gözetim süreçlerini ve yorumlanabilirlik ya da adalet için bazen feda edilen performansı içerir. Bunu yatırım yapmamanın maliyetine karşı tartın: hukuki yükümlülük, zorunlu kapatmalar, kaybedilen kamu güveni ve bir başarısızlıktan sonra yönetişimi sonradan eklemenin çok daha yüksek maliyeti. Düzenlemeye tabi bağlamlarda sorumlu yapay zeka yatırımı giderek pazarlık konusu olmaktan çıkıyor. Gerekçeyi liderliğe risk yönetimi ve faaliyet ruhsatı olarak çerçeveleyerek sunun: yapay zekayı ölçekte devreye almanın ön koşulu.

## Anti-kalıplar ve tuzaklar

- **İhmalle adalet.** Bir modelin korunan öznitelikleri yok saydığı için adil olduğunu varsaymak.
- **Açıklanabilirlik tiyatrosu.** Kararların nasıl verildiğini gerçekte yansıtmayan açıklamalar üretmek.
- **Onay mührü gözetim.** Geçersiz kılmak için gerçek yetkisi ve bilgisi olmayan nominal insan incelemesi.
- **Sonradan akla gelen yönetişim.** Belgeleme ve incelemeyi tasarım ve devreye almadan sonra eklemek.
- **İtiraz yolu yok.** Etkilenen insanlara otomatik bir karara itiraz etme yolu bırakmamak.
- **Kötüye kullanımı görmezden gelmek.** Yalnızca amaçlanan kullanımı test edip jailbreak ve istismarı kaçırmak.
- **Ayak izi körlüğü.** Çevresel maliyeti hiç umursamadan varsayılan olarak en büyük modeli seçmek.

## Olgunluk modeli

- **Düzey 1, Başlangıç:** Adalet testi, açıklama ya da yönetişim yoktur; sorumluluk tanımsızdır; önyargı, kötüye kullanım ve gizlilik sorunları ancak zarardan sonra ortaya çıkar ve yapay zeka sistemlerinin ya da risklerinin bir envanteri yoktur.
- **Düzey 2, Geliştirme:** Bazı önyargı testi, model kartı ve kırmızı takım tek tek sistemlerde yapılır ama uygulama takımlar arasında tutarsızdır; gözetim gelişigüzeldir; NIST Yapay Zeka Risk Yönetimi Çerçevesi ve AB Yapay Zeka Yasası gibi çerçeveler bilinir ama yalnızca kısmen benimsenmiştir.
- **Düzey 3, Standartlaştırma:** Yönetişim belgelenmiş ve kuruluş genelinde uygulanır: sistemler tanınmış çerçevelere ve ISO/IEC 42001'e eşlenir, her birinin bir risk düzeyi ve isimli bir sahibi vardır; adalet, güvenlik ve gizlilik testi, model ve veri kartları, itiraz yolları ve yüksek riskli sistemler için kırmızı takım isteğe bağlı değil zorunludur.
- **Düzey 4, Yönetme:** Program veriyle ölçülür ve kontrol edilir: alt grup adalet metrikleri, güvenlik ve jailbreak bulguları, itiraz hacimleri ve tersine çevrilme oranları, gözetim geçersiz kılma oranları ve iş yükü ayak izi temel çizgilere ve eşiklere karşı izlenir; kayma ve farklı sonuçlar tanımlı eylemi tetikler; git ya da gitme kararları güvenceye değil kanıta dayanır.
- **Düzey 5, Orkestrasyon:** Sorumlu yapay zeka sürekli iyileştirilir ve kurum genelinde bütünleştirilir: adalet, güvenlik ve kötüye kullanım izleme üretimde çalışır, yönetişim teslimata yerleştirilmiştir, çevresel maliyet model seçiminde resmi bir girdidir ve kurum, hukuk, risk ve yetenek değiştikçe denetimlerini uyarlar; sorumluluk tek bir takıma değil herkese aittir.

## Tartışma fikirleri

- Belirli bir karar için hangi adalet tanımı geçerlidir ve kim karar verir?
- Adalet ya da yorumlanabilirlik için ne kadar doğruluk ya da performanstan vazgeçmek kabul edilebilir?
- İnsan gözetimini bir onay mührü olmaktan çıkarıp anlamlı kılan nedir?
- Otomatik kararlara itirazlar, adil ve zamanında olacak şekilde nasıl tasarlanmalı?
- Henüz hayal etmediğiniz kötüye kullanım için nasıl kırmızı takım yaparsınız?
- Çevresel maliyet model seçimini etkilemeli mi ve onu nasıl tartardınız?

## Önemli çıkarımlar

- Güvenilir yapay zeka tasarım gereği adil, açıklanabilir, hesap verebilir, güvenli ve mahremiyete saygılıdır.
- Adalet ve güvenlik, tek seferlik denetimler değil, sürekli ölçüm ve yönetim disiplinleridir.
- Savunulabilir ve denetlenebilir olmak için yönetişimi NIST YZ RMF, AB Yapay Zeka Yasası ve ISO/IEC 42001 ile hizalayın.
- Anlamlı insan gözetimini, net hesap verebilirliği ve gerçek bir itiraz hakkını koruyun.
- Gizlilik için ve kötüye kullanıma karşı mühendislik yapın ve çevresel maliyeti hesaba katın.

## Kaynaklar ve ileri okuma

- National Institute of Standards and Technology, *AI Risk Management Framework (AI RMF 1.0)*.
- European Union, *Artificial Intelligence Act (Regulation on Artificial Intelligence)*.
- ISO/IEC 42001, *Information technology, Artificial intelligence, Management system*.
- Solon Barocas, Moritz Hardt, and Arvind Narayanan, *Fairness and Machine Learning: Limitations and Opportunities*.
- Christoph Molnar, *Interpretable Machine Learning*.
- Cathy O'Neil, *Weapons of Maths Destruction*.
- Emma Strubell, Ananya Ganesh, and Andrew McCallum, *Energy and Policy Considerations for Deep Learning in NLP*.
