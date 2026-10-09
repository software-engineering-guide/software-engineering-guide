# 2.2 Prinsip desain perangkat lunak

## Tinjauan dan motivasi

Prinsip desain perangkat lunak adalah heuristik untuk menata kode agar Anda dapat memahami, mengubah, dan memperluasnya seiring waktu. Prinsip ini mencakup akronim bernama ([SOLID](https://en.wikipedia.org/wiki/SOLID) untuk lima prinsip desain [berorientasi objek](https://en.wikipedia.org/wiki/Object-oriented_programming), [DRY](https://en.wikipedia.org/wiki/Don%27t_repeat_yourself) untuk jangan-ulangi-diri-sendiri, [KISS](https://en.wikipedia.org/wiki/KISS_principle) untuk buat-tetap-sederhana, [YAGNI](https://en.wikipedia.org/wiki/You_aren%27t_gonna_need_it) untuk kamu-tidak-akan-membutuhkannya), konsep struktural ([kopling](https://en.wikipedia.org/wiki/Coupling_(computer_programming)), [kohesi](https://en.wikipedia.org/wiki/Cohesion_(computer_science)), [pemisahan perhatian](https://en.wikipedia.org/wiki/Separation_of_concerns)), [pola desain](https://en.wikipedia.org/wiki/Software_design_pattern) yang terkatalog, pendekatan pemodelan tingkat lebih tinggi seperti [Domain-Driven Design](https://en.wikipedia.org/wiki/Domain-driven_design) (memodelkan perangkat lunak dalam bahasa domain bisnis), dan pilihan antara gaya berorientasi objek, [fungsional](https://en.wikipedia.org/wiki/Functional_programming), dan [berorientasi data](https://en.wikipedia.org/wiki/Data-oriented_design). Tak satu pun ini hukum. Semuanya adalah pengalaman yang dipadatkan, dan Anda harus menerapkannya dengan penilaian.

Bagi tim besar, nilai prinsip bersama adalah koordinasi. Ketika ratusan insinyur mengerjakan sistem yang sama, mereka membutuhkan kosakata bersama untuk diskusi desain dan seperangkat bawaan bersama agar modul yang ditulis secara independen saling cocok. Desain yang baik adalah yang memungkinkan banyak orang mengubah sistem secara paralel tanpa bertabrakan terus-menerus. Ia juga yang menjaga sistem tetap dapat diubah sepuluh tahun kemudian, umur normal sistem enterprise dan pemerintah, jauh melewati masa kerja penulis aslinya.

Keterampilan kritisnya bukan menghafal prinsip. Melainkan mengetahui kapan masing-masing menyesatkan Anda. Setiap prinsip punya mode kegagalan: DRY dapat menghasilkan abstraksi yang salah, SOLID dapat menghasilkan indireksi yang tidak perlu, YAGNI dapat membuat kelaparan perluasan yang sebenarnya Anda butuhkan. Bab ini memperlakukan prinsip sebagai perkakas dengan ranah penerapan, dan menekankan kopling serta kohesi sebagai sifat yang lebih dalam yang hendak dilayani oleh akronim itu.

## Prinsip utama

- Kelola kopling dan kohesi lebih dulu; sebagian besar prinsip bernama adalah cara tidak langsung untuk memperbaiki kedua sifat ini.
- Optimalkan untuk perubahan: desain yang baik meminimalkan biaya perubahan yang akan benar-benar Anda perlukan.
- Pilih desain paling sederhana yang berfungsi sekarang, tetapi pertahankan batas di tempat perubahan kemungkinan terjadi.
- Duplikasi lebih murah daripada abstraksi yang salah; tunggu sampai polanya jelas.
- Buat dependensi eksplisit dan arahkan ke hal-hal yang stabil.
- Modelkan domain dalam bahasa domain; selaraskan batas perangkat lunak dengan batas bisnis.
- Pilih paradigma sesuai masalah, bukan ideologi; sebagian besar sistem besar bercampur secara pragmatis.

## Rekomendasi

### Gunakan SOLID sebagai lensa, bukan daftar periksa

Terapkan tanggung jawab tunggal untuk menjaga modul tetap kohesif, pembalikan dependensi untuk mengarahkan dependensi ke abstraksi di tempat batas benar-benar ada, dan terbuka-tertutup di tempat titik perluasan nyata. Jangan memproduksi antarmuka, factory, dan lapisan hanya untuk memuaskan akronim padahal hanya ada satu implementasi dan tidak ada yang kedua di depan mata. Indireksi punya biaya, dan Anda membayarnya pada setiap pembacaan.

### Terapkan DRY pada pengetahuan, bukan pada teks

DRY adalah tentang tidak menduplikasi satu bagian *pengetahuan* yang berwenang. Bukan tentang menghilangkan baris yang sekadar tampak mirip. Dua potong kode yang tampak serupa tetapi berubah karena alasan berbeda harus tetap terpisah. Pilih sedikit duplikasi daripada abstraksi bersama yang prematur yang mengopel hal-hal tak terkait. Ekstrak abstraksi setelah pola nyata muncul dua atau tiga kali.

### Biarkan KISS dan YAGNI menahan spekulasi

Bangun untuk persyaratan yang Anda miliki, bukan yang Anda bayangkan. Hindari generalitas spekulatif, seperti kerangka kerja yang dapat dikonfigurasi, sistem plugin, dan titik perluasan yang tidak diminta siapa pun. Penyeimbangnya adalah bahwa sebagian fleksibilitas memang lebih murah dibangun lebih awal, seperti antarmuka yang stabil atau sambungan yang bersih. YAGNI menentang *implementasi* spekulatif, bukan batas yang dipikirkan dengan matang.

### Rancang untuk kopling rendah dan kohesi tinggi secara eksplisit

Buat setiap modul mengerjakan satu hal yang terdefinisi baik (kohesi), dan bergantung pada sesedikit mungkin modul lain, melalui antarmuka sempit (kopling rendah). Ketika Anda meninjau desain, tanyakan perubahan mana yang beriak melintasi batas modul. Riak itu adalah ukuran sebenarnya dari kopling. Pemisahan perhatian adalah gagasan yang sama yang diterapkan pada lapisan dan perhatian lintas bidang.

### Gunakan pola desain sebagai kosakata, terapkan anti-pola sebagai peringatan

Pola adalah nama bersama yang berguna untuk solusi yang berulang. Raihlah satu ketika masalahnya benar-benar cocok. Jangan memaksakan pola agar tampak canggih, karena kode yang sarat pola sering menjadi tanda rekayasa berlebihan. Pelajari [anti-pola](https://en.wikipedia.org/wiki/Anti-pattern) yang umum (god object, model anemik di tempat yang tidak semestinya, big ball of mud, distributed monolith) sebagai label diagnostik.

### Adopsi Domain-Driven Design di tempat domain rumit

Untuk sistem dengan aturan bisnis yang kaya, gunakan perkakas taktis dan strategis DDD: bahasa ubikuitas yang dibagikan dengan pakar domain, bounded context yang memotong sistem menjadi bagian yang dimodelkan secara independen, dan context map yang menjelaskan bagaimana bagian-bagian itu berhubungan. Bounded context sangat bernilai pada skala enterprise, karena menyelaraskan kepemilikan tim dengan batas model. DDD berlebihan untuk sistem [CRUD](https://en.wikipedia.org/wiki/Create,_read,_update_and_delete) (create, read, update, delete) yang sederhana.

### Pilih paradigma menurut kecocokan

Gunakan orientasi objek untuk mengenkapsulasi perilaku berstatus dan memodelkan domain. Gunakan gaya fungsional untuk transformasi, konkurensi, dan keterprediksian lewat [imutabilitas](https://en.wikipedia.org/wiki/Immutable_object). Gunakan desain berorientasi data di tempat kinerja dan perilaku cache mendominasi. Sistem besar mencampur ketiganya. Buat pilihan per komponen, dan jaga batas antargaya tetap bersih.

## Trade-off: kelebihan dan kekurangan

| Prinsip / pendekatan | Diterapkan dengan baik | Mode kegagalan |
|---|---|---|
| SOLID | Sambungan jelas di tempat perubahan terjadi; unit dapat diuji | Perbanyakan antarmuka dan lapisan; indireksi tanpa imbalan |
| DRY | Sumber kebenaran tunggal untuk pengetahuan nyata | Abstraksi salah yang mengopel kode tak terkait |
| KISS / YAGNI | Sistem ramping dan dapat dipahami | Sambungan kurang dirancang; retrofit mahal untuk fleksibilitas yang dibutuhkan |
| Pola desain | Kosakata bersama; struktur teruji | Kultus kargo pola; kompleksitas aksidental |
| Domain-Driven Design | Model dan tim selaras; kompleksitas dijinakkan | Upacara berat pada domain sederhana; batas konteks salah tempat |
| Fungsional / imutabel | Keterprediksian; konkurensi lebih aman | Kecocokan canggung untuk masalah yang pada dasarnya berstatus; kejutan kinerja |

Ketegangan yang berulang adalah antara kurang-desain dan kelebihan-desain. Sistem yang kurang dirancang menumpuk kopling dan menjadi kaku. Sistem yang terlalu dirancang tenggelam dalam abstraksi yang harus dipahami dan dipelihara seseorang. Jawabannya bukan titik tetap. Melainkan disiplin: tunda keputusan sampai Anda punya cukup informasi, sambil mempertahankan sambungan yang memungkinkan Anda mengubah pikiran.

## Pertanyaan untuk didiskusikan dengan tim Anda

1. **Apa ambang konkret Anda untuk mengekstrak abstraksi bersama, dan bagaimana Anda mencegah DRY menghasilkan yang salah?** Bab ini terus terang bahwa duplikasi lebih murah daripada abstraksi yang salah, dan bahwa Anda harus menunggu sampai pola muncul dua atau tiga kali sebelum mengekstrak. Pada tim besar bahayanya adalah seseorang memfaktorkan dua potongan yang tampak serupa ke modul bersama melintasi batas tim, lalu setiap perubahan mendatang pada satu pemanggil beriak ke yang lain. Sinyal yang perlu dibawa adalah apakah duplikat berubah karena alasan yang sama atau sekadar tampak serupa saat ini. Sepakati aturan tiga, dan wajibkan agar abstraksi kandidat benar-benar pernah berubah bersama sebelum Anda mengopel pemanggilnya. Satu kesepakatan itu mencegah kelas kopling yang mahal diurai begitu banyak tim bergantung padanya.

2. **Bagaimana Anda membuat kopling dan kohesi terlihat dalam tinjauan desain alih-alih menyerahkannya pada firasat?** Prinsip utama menempatkan kopling dan kohesi di atas setiap akronim, dan mendefinisikan kopling sebagai perubahan yang beriak melintasi batas modul. Intuisi tidak berskala di ratusan insinyur yang masing-masing hanya melihat sudutnya dari sistem. Bawa bukti yang dapat dihasilkan mesin: graf dependensi, dan data co-change yang menunjukkan modul mana yang terus disunting bersama dalam commit yang sama. Tambahkan pertanyaan tinjauan eksplisit yang menanyakan batas modul mana yang dipaksa dilintasi suatu perubahan. Ketika dua modul selalu berubah bersama, itu isyarat bagi Anda untuk menggabungkannya atau memperbaiki batas di antaranya.

3. **Di mana garis dalam sistem Anda antara domain yang cukup kaya untuk membenarkan Domain-Driven Design dan aplikasi CRUD biasa di mana itu berlebihan?** Bab ini merekomendasikan bounded context DDD justru karena menyelaraskan kepemilikan tim dengan batas model, dan memperingatkan bahwa DDD berlebihan untuk sistem create-read-update-delete sederhana dan merosot menjadi upacara tanpa pemodelan nyata. Keliru ke arah mana pun mahal: DDD berat pada domain tipis mengubur aplikasi sederhana dalam upacara, sementara model bersama yang melebar di banyak tim memaksa koordinasi lintas tim terus-menerus. Bawa sinyal yang benar-benar menentukan: kepadatan aturan bisnis, dan berapa banyak tim yang perlu memiliki bagian secara independen. Sisakan mesin strategis untuk inti yang kompleks, dan biarkan tepi yang sederhana tetap sederhana. Itu menjauhkan Anda dari teater DDD dan big ball of mud.

4. **Kapan abstraksi, antarmuka, atau pola desain sepadan dengan indireksi yang ditambahkannya, dan siapa yang berwenang menyebut desain terlalu direkayasa?** Bab ini eksplisit bahwa indireksi punya biaya yang Anda bayar pada setiap pembacaan, dan bahwa memproduksi antarmuka, factory, dan lapisan untuk memuaskan SOLID atau agar tampak canggih adalah mode kegagalan. Pada tim besar tekanan berjalan ke arah sebaliknya: peninjau meloloskan abstraksi tambahan karena tampak disiplin, dan tak seorang pun mau menjadi orang yang berargumen untuk struktur lebih sedikit. Pertimbangan yang bersaing itu nyata, karena sebagian sambungan memang pantas dipertahankan dan menghapusnya kemudian mahal. Bawa bukti konkret ke diskusi: berapa implementasi yang sebenarnya dimiliki antarmuka hari ini, seberapa sering titik perluasan pernah ditekuk, dan berapa berkas yang harus dibuka pembaca untuk mengikuti satu jalur kode. Sepakati bahwa satu implementasi tanpa yang kedua di depan mata adalah alasan bawaan untuk di-inline, dan namai siapa yang dapat melabeli desain terlalu direkayasa tanpa terbaca sebagai hinaan. Dalam sistem enterprise dan pemerintah yang hidup lebih lama daripada penulisnya selama satu dekade, indireksi yang tak beralasan adalah pajak yang dibayar setiap pemelihara mendatang, jadi perlakukan "apa yang dibeli abstraksi ini untuk kita" sebagai pertanyaan tinjauan tetap, bukan tantangan pribadi.

5. **Bagaimana Anda memutuskan paradigma apa yang dipakai setiap komponen, berorientasi objek, fungsional, atau berorientasi data, dan bagaimana Anda menjaga batas di antaranya tetap bersih?** Bab ini berargumen bahwa sistem besar bercampur secara pragmatis dan Anda harus memilih per komponen menurut kecocokan, memakai orientasi objek untuk domain berstatus, gaya fungsional untuk transformasi dan konkurensi, dan desain berorientasi data di tempat kinerja serta perilaku cache mendominasi. Jika tidak dikelola, pilihan paradigma menjadi soal siapa yang menulis modul lebih dulu, dan status mutabel bocor ke transformasi yang seharusnya murni, atau kemurnian fungsional melawan masalah yang pada dasarnya berstatus. Bukti yang layak dibawa adalah di mana rasa sakit Anda yang sebenarnya: komponen mana yang sulit diuji karena status tersembunyi, jalur panas mana yang terikat cache, dan di mana gaya saat ini memaksa solusi darurat yang canggung. Putuskan paradigma bawaan untuk setiap lapisan dengan sengaja dan tuliskan di mana sambungan antargaya jatuh, agar inti fungsional dan tepi imperatif tidak saling merembes. Untuk sistem yang diatur atau pemerintah di mana perhitungan harus dapat diaudit dan direproduksi untuk periode tertentu, inti fungsional yang imutabel sering merupakan persyaratan kepatuhan, bukan selera, dan kendala itu harus menggerakkan batas alih-alih mengikutinya.

6. **Bagaimana Anda menjaga prinsip-prinsip ini agar tidak mengeras menjadi dogma, dan di mana Anda mencatat alasan di balik keputusan desain agar tim masa depan dapat meninjaunya kembali?** Setiap prinsip dalam bab ini punya ranah penerapan dan mode kegagalan, dan seluruh pembingkaan memperlakukannya sebagai perkakas yang diterapkan dengan penilaian alih-alih hukum yang ditegakkan. Pada tim besar prinsip diam-diam menjadi aturan: DRY melarang duplikasi apa pun, SOLID mewajibkan satu antarmuka per kelas, dan pengecualian pragmatis diblokir dalam tinjauan oleh orang yang mengutip akronim alih-alih hasilnya. Ketegangannya adalah bahwa sedikit konsistensi memang membantu ratusan insinyur berkoordinasi, jadi Anda tidak dapat begitu saja menyatakan setiap prinsip opsional. Bawa contoh di mana mengikuti prinsip secara harfiah menghasilkan desain yang lebih buruk, dan bawa catatan keputusan, jika ada, yang menjelaskan mengapa batas atau abstraksi tertentu ada. Sepakati bahwa prinsip adalah bawaan yang boleh disimpangi insinyur dengan alasan tercatat, dan tangkap pilihan desain penting dalam catatan keputusan arsitektur singkat agar tim berikutnya mewarisi alasannya, bukan hanya kodenya. Dalam sistem enterprise dan sektor publik, di mana penulis aslinya sudah lama pergi dan audit menanyakan mengapa sistem berbentuk demikian, jejak tertulis itu adalah beda antara desain yang dapat diubah dengan aman oleh tim masa depan dan desain yang mereka takut sentuh.

## Lensa sektor

**Startup.** Pilih desain paling sederhana yang dirilis dan pertahankan satu modul yang terfaktor baik sampai kasus penggunaan kedua yang nyata memaksa sambungan. Sumber daya Anda yang paling langka adalah perhatian rekayasa, jadi antarmuka, lapisan, dan kerangka spekulatif yang prematur adalah biaya murni. Ikuti aturan tiga sebelum mengekstrak abstraksi bersama apa pun, dan biarkan YAGNI mematikan titik perluasan yang belum diminta siapa pun.

**Bisnis kecil.** Tanpa arsitek dan dengan anggaran ketat, bersandarlah pada desain yang sudah tertanam dalam kerangka kerja dan pustaka yang Anda beli alih-alih menciptakan pola sendiri. Sisakan upaya desain kustom untuk segelintir aturan yang benar-benar bisnis Anda, dan jaga yang lain tetap konvensional agar kontraktor atau karyawan baru dapat membacanya. Sedikit duplikasi yang Anda pahami mengalahkan abstraksi cerdik yang hanya dapat dipelihara penulisnya.

**Enterprise.** Imbalan prinsip bersama adalah koordinasi di banyak tim: kosakata bersama untuk tinjauan desain, dan bounded context yang menyelaraskan batas model dengan kepemilikan tim agar kelompok berkembang secara independen. Kelola kopling dan kohesi secara eksplisit dengan data dependensi dan co-change, dan catat keputusan desain penting agar sistem tetap dapat diubah lama setelah penulisnya berpindah. Jaga sama-sama dari abstraksi salah yang mengopel tim dan rekayasa berlebihan yang memajaki setiap pembaca.

**Pemerintah.** Kemampuan diaudit dan keterreproduksian sering menentukan desain. Inti fungsional yang imutabel memungkinkan Anda mereproduksi perhitungan historis persis untuk periode tertentu, yang tidak dapat dijamin graf objek kusut dengan status mutabel tersembunyi. Pilih kontrak terbitan eksplisit daripada tabel bersama pada batas konteks, dan jaga desain serta catatan keputusannya terbaca oleh auditor dan oleh tim mana pun yang mewarisi sistem sepuluh tahun kemudian.

## Contoh

**Startup.** Sebuah startup tiga insinyur yang membangun produk pertamanya menahan dorongan untuk memecah setiap fitur menjadi lapisan antarmuka dan factory, mempertahankan satu modul yang terfaktor baik sampai kasus penggunaan kedua yang nyata muncul. Ketika logika yang sama muncul untuk ketiga kalinya di alur pendaftaran dan penagihan, mereka mengekstrak satu fungsi bersama kecil alih-alih kerangka kerja spekulatif. Ini menjaga basis kode cukup kecil sehingga siapa pun dari mereka dapat memegangnya di kepala, dan beberapa sambungan yang mereka gambar jatuh di tempat produk paling mungkin berubah.

**Enterprise.** Sebuah platform asuransi besar memodelkan polis, klaim, dan penagihan sebagai bounded context terpisah, masing-masing dimiliki tim khusus dengan model data dan batas layanannya sendiri. Di tempat konteks bertemu, seperti ketika klaim merujuk polis, mereka berbicara lewat kontrak terbitan eksplisit alih-alih tabel basis data bersama. Ini memungkinkan ketiga tim berkembang secara independen, dan bahasa ubikuitas menjaga percakapan dengan penjamin dan aktuaris tetap tepat. Versi sebelumnya berbagi satu model yang melebar, dan setiap perubahan memerlukan koordinasi lintas tim.

**Pemerintah.** Sistem pemrosesan pajak nasional dengan sengaja memilih inti berorientasi data dan fungsional untuk mesin perhitungannya. Aturan pajak diekspresikan sebagai transformasi murni atas catatan masukan imutabel, yang membuatnya dapat diaudit, diuji, dan direproduksi untuk tahun pajak tertentu. Bagian imperatif dan berstatus (alur kerja, notifikasi) dijaga di tepi. Auditor dapat menunjuk versi aturan tertentu dan mereproduksi perhitungan historis apa pun persis, yang merupakan persyaratan hukum yang tidak dapat dijamin graf objek kusut dengan status mutabel tersembunyi.

## Kasus bisnis: motivasi, ROI, dan TCO

Kualitas desain adalah investasi pada *kemampuan berubah* sebuah sistem, dan kemampuan berubah mendominasi total biaya kepemilikan. Sebagian besar biaya sistem jatuh setelah rilis pertamanya, dalam modifikasi dan perluasan. Sistem yang dirancang baik menjaga biaya perubahan kira-kira datar seiring waktu. Yang dirancang buruk melihat biaya setiap perubahan naik sampai sistem pada dasarnya tidak dapat diubah dan harus ditulis ulang, hasil termahal dari semuanya.

Biaya adopsi terutama keterampilan dan disiplin tinjauan: mengajarkan prinsip, dan menghabiskan waktu desain di muka. Biaya tidak mengadopsinya adalah penumpukan lambat [utang teknis](https://en.wikipedia.org/wiki/Technical_debt), velocity pengiriman yang turun, tingkat cacat yang naik, dan penulisan ulang yang akhirnya mahal. Untuk meyakinkan pimpinan, hubungkan disiplin desain dengan keterprediksian pengiriman dan menghindari program penulisan ulang, dan lacak indikator awal seperti tingkat kegagalan perubahan dan waktu mengimplementasikan fitur sebanding dari waktu ke waktu. Waspadai juga kegagalan sebaliknya: berinvestasi berlebihan dalam desain untuk masa depan yang tidak pasti juga menghancurkan nilai. Jadi argumennya adalah untuk desain yang *sepadan*, dikalibrasi terhadap seberapa mungkin dan seberapa mahal perubahan di masa depan.

## Anti-pola dan jebakan

- **Generalitas spekulatif:** membangun keterluasan untuk persyaratan yang dibayangkan yang tidak pernah tiba.
- **Abstraksi yang salah:** memaksa kode tak terkait bersatu demi memuaskan DRY, menciptakan kopling yang lebih buruk daripada duplikasi.
- **Kultus kargo pola:** menerapkan pola desain demi pola itu sendiri, menambah indireksi tanpa manfaat.
- **Objek anemik atau god object:** model tanpa perilaku, atau objek yang mengerjakan segalanya; keduanya menandakan tanggung jawab yang salah tempat.
- **Distributed monolith:** layanan terpecah secara fisik tetapi tetap berpasangan erat, menggabungkan biaya kedua pendekatan.
- **Big ball of mud:** tidak ada struktur yang dapat dikenali; setiap perubahan mempertaruhkan segalanya.
- **Teater DDD:** mengadopsi kosakata dan struktur folder tanpa pemodelan domain yang memberinya nilai.

## Model kematangan

- **Tingkat 1, Memulai:** Desain ad hoc dan reaktif; kopling menumpuk tanpa kendali; prinsip tidak dikenal atau dipanggil sebagai slogan, dan abstraksi muncul atau lenyap menurut kebiasaan individu.
- **Tingkat 2, Mengembangkan:** Tim mengenal prinsip dan menerapkannya, tetapi tidak konsisten dan sering dogmatis; sebagian kelompok mengelola kopling dan kohesi dengan sengaja sementara yang lain tidak, dan tidak ada kosakata bersama di seluruh organisasi.
- **Tingkat 3, Membakukan:** Kosakata desain bersama, aturan tiga untuk mengekstrak abstraksi, analisis kopling dan kohesi, serta bounded context yang selaras dengan tim didokumentasikan dan diharapkan di seluruh organisasi, diterapkan secara konsisten dalam tinjauan desain alih-alih diserahkan pada selera individu.
- **Tingkat 4, Mengelola:** Kesehatan desain diukur terhadap garis dasar: data kopling dan co-change, tingkat kegagalan perubahan, dan waktu mengimplementasikan fitur sebanding dilacak dari waktu ke waktu, sehingga abstraksi dan batas ditambah, dipertahankan, atau dihapus berdasarkan bukti, dan rekayasa berlebihan serta abstraksi yang salah tertangkap oleh data alih-alih opini.
- **Tingkat 5, Mengorkestrasi:** Disiplin desain terintegrasi dengan perencanaan pengiriman dan risiko di seluruh organisasi; prinsip diterapkan dengan nuansa dan mode kegagalan yang diketahui; pilihan paradigma dan batas disengaja dan terus ditinjau kembali, dan organisasi secara rutin merefaktor, mengubah cakupan, dan mengakhiri abstraksi seiring bergesernya domain dan bukti.

## Gagasan untuk didiskusikan

- Bagaimana Anda membedakan sambungan yang dibutuhkan dari generalitas spekulatif sebelum Anda memiliki persyaratan masa depan?
- Kapan DRY membawa tim Anda ke abstraksi yang salah, dan bagaimana Anda mengenalinya?
- Di mana batas bounded context harus jatuh, dan seberapa dekat mereka harus mencerminkan bagan organisasi?
- Berapa banyak desain yang harus mendahului kode dalam konteks Anda, dan bagaimana Anda mencatat keputusannya?
- Bagian sistem Anda mana yang akan diuntungkan oleh gaya yang lebih fungsional atau berorientasi data?
- Bagaimana Anda menjaga prinsip desain agar tidak mengeras menjadi dogma yang menolak pengecualian pragmatis?

## Poin-poin utama

- Kopling dan kohesi adalah sifat yang penting; akronim adalah sarana menuju tujuan itu.
- Setiap prinsip punya mode kegagalan; ketahui kapan masing-masing menyesatkan.
- Pilih sedikit duplikasi daripada abstraksi yang prematur atau salah.
- Gunakan DDD dan bounded context untuk menyelaraskan domain kompleks dengan kepemilikan tim.
- Pilih paradigma menurut kecocokan; sistem besar bercampur secara pragmatis.
- Rancang untuk perubahan yang benar-benar akan Anda perlukan, menghindari kurang-desain maupun kelebihan-desain.

## Referensi dan bacaan lanjutan

- Robert C. Martin, *Clean Architecture* dan *Agile Software Development, Principles, Patterns, and Practices*
- Eric Evans, *Domain-Driven Design: Tackling Complexity in the Heart of Software*
- Vaughn Vernon, *Implementing Domain-Driven Design*
- Erich Gamma, Richard Helm, Ralph Johnson, John Vlissides, *Design Patterns: Elements of Reusable Object-Oriented Software*
- Martin Fowler, *Refactoring: Improving the Design of Existing Code* dan *Patterns of Enterprise Application Architecture*
- David L. Parnas, *On the Criteria to Be Used in Decomposing Systems into Modules*
- Sandi Metz, *Practical Object-Oriented Design*
