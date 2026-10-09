# 8.3 Kontainer, orkestrasi, dan cloud-native

## Tinjauan dan motivasi

[Kontainer](https://en.wikipedia.org/wiki/OS-level_virtualization) mengemas aplikasi bersama dependensinya ke dalam satu unit portabel dan terisolasi. Ia berjalan dengan cara yang sama di laptop, di lingkungan uji, dan di produksi. Platform orkestrasi, yang paling menonjol [Kubernetes](https://en.wikipedia.org/wiki/Kubernetes), menjadwalkan dan mengelola kontainer dalam jumlah besar di armada mesin. Mereka menangani penempatan, penskalaan, kesehatan, jaringan, dan pemulihan. [Cloud-native](https://en.wikipedia.org/wiki/Cloud-native_computing) adalah gaya arsitektur lebih luas yang dibangun di atas fondasi ini: aplikasi yang dirancang sebagai layanan longgar-terkait, dapat di-deploy mandiri, dan dapat diskalakan horizontal yang mengasumsikan infrastruktur dinamis yang menyembuhkan diri.

Bagi tim besar, kontainer dan orkestrasi menyelesaikan satu masalah sulit. Anda perlu menjalankan banyak layanan, dibangun banyak tim, secara andal dan efisien di infrastruktur bersama. Kontainer memberi setiap tim kontrak pengemasan dan runtime yang konsisten, yang memensiunkan kelas kegagalan "berfungsi di mesin saya." Orkestrasi menyembunyikan mesin individual di balik substrat umum, sehingga tim men-deploy ke platform alih-alih ke server. Standardisasi ini yang memungkinkan Anda mengoperasikan ratusan atau ribuan layanan tanpa setiap tim menciptakan ulang deployment, penskalaan, dan ketahanan.

Pengadopsi enterprise dan pemerintah mendapat portabilitas, ketahanan, dan jalan menjauh dari lock-in. Sebagai gantinya, mereka mewarisi kompleksitas nyata dan tanggung jawab keamanan baru. Platform kontainer kuat justru karena dapat diprogram dan dinamis, yang berarti Anda harus mengaturnya dengan cermat. Asal-usul citra, isolasi multitenansi, kebijakan jaringan, dan biaya semuanya menjadi perhatian tingkat platform. Pengadopsi sektor publik makin menambah persyaratan kedaulatan: kendali atas di mana data berada dan siapa yang dapat mengaksesnya. Itu menjadikan kemampuan menjalankan beban kerja konsisten di lingkungan pilihan sebagai kapabilitas strategis, bukan sekadar detail teknis.

## Prinsip utama

- Kemas aplikasi sebagai citra kontainer kecil, berfungsi tunggal, dan tak berubah.
- Praktikkan kebersihan citra: citra dasar minimal, versi disematkan, dipindai kerentanan, dan bertanda tangan.
- Rancang aplikasi agar tanpa status dan dapat diskalakan horizontal sedapat mungkin, dengan mengeksternalisasi status.
- Perlakukan model keadaan-diinginkan platform orkestrasi sebagai sumber kebenaran dan biarkan ia menyembuhkan diri.
- Tegakkan isolasi dan hak istimewa paling sedikit antara tenant, beban kerja, dan namespace.
- Ikuti prinsip [twelve-factor](https://en.wikipedia.org/wiki/Twelve-Factor_App_methodology), metodologi membangun aplikasi sekali pakai, konfigurasi-eksternal, dan dapat diskalakan horizontal, dan perluas untuk kenyataan sistem terdistribusi.
- Jadikan biaya perhatian rekayasa kelas satu yang terlihat, bukan renungan belakangan.
- Pilih abstraksi portabel berbasis standar untuk menjaga fleksibilitas strategis.

## Rekomendasi

### Praktikkan kebersihan citra yang ketat

Citra kontainer adalah unit dasar kepercayaan dan deployment Anda, jadi perlakukan demikian. Mulailah dari citra dasar minimal dan tepercaya untuk menyusutkan permukaan serangan. Sematkan versi dependensi dan citra dasar untuk reprodusibilitas. Pindai setiap citra untuk kerentanan yang diketahui dalam pipeline build, dan blokir yang punya temuan kritis. Tandatangani citra dan verifikasi tanda tangan saat deploy, agar hanya citra yang disetujui dan tak termodifikasi yang berjalan. Simpan registri internal terkurasi berisi citra dasar yang diperkeras tempat tim membangun. Itu menyebarkan bawaan keamanan baik secara otomatis.

### Gunakan pola Kubernetes alih-alih menciptakannya ulang

Kubernetes menghargai tim yang mengadopsi pola mapannya, dan menghukum tim yang melawan modelnya. Pakai manifes deklaratif untuk keadaan yang diinginkan. Tambahkan probe kesehatan agar platform dapat mendeteksi dan mengganti instans tak sehat. Tetapkan resource request dan limit agar penjadwal dapat mengemas beban kerja dengan aman. Pakai autoscaling horizontal untuk permintaan elastis. Untuk logika operasional yang harus berjalan terus-menerus, seperti mengelola basis data, merotasi sertifikat, atau merekonsiliasi sumber daya kustom, pakai pola operator, yang mengodekan pengetahuan operasional manusia ke dalam perangkat lunak yang mengawasi keadaan dan bertindak. Tahan dorongan membangun orkestrasi pesanan di atas platform. Pilih konstruksi asli.

### Rancang multitenansi dengan sengaja

Ketika banyak tim berbagi klaster, isolasi adalah persyaratan keamanan dan keandalan, bukan kemewahan. Pakai namespace sebagai batas tenansi. Tegakkan kuota sumber daya agar tak ada tenant yang dapat membuat yang lain kelaparan. Terapkan kebijakan jaringan untuk membatasi lalu lintas pada apa yang diizinkan secara eksplisit. Pakai [kontrol akses berbasis peran](https://en.wikipedia.org/wiki/Role-based_access_control) (RBAC) untuk membatasi apa yang dapat dilakukan setiap tim. Untuk beban kerja dengan kebutuhan isolasi lebih kuat, pertimbangkan klaster terpisah atau sandboxing lebih kuat. Putuskan sejak awal apakah model Anda multitenansi lunak (tim internal tepercaya) atau multitenansi keras (beban kerja yang saling tak percaya), karena keduanya menuntut kontrol yang sangat berbeda.

### Bangun cloud-native, twelve-factor dan lebih

Metodologi twelve-factor, dengan dependensi eksplisit, konfigurasi dalam lingkungan, proses tanpa status, kemudahan dibuang, dan seterusnya, tetap baseline yang sangat baik untuk layanan yang berkembang di platform dinamis. Perluas untuk kenyataan tambahan sistem terdistribusi. Rancang untuk kegagalan parsial. Jadikan operasi idempoten dan dapat dicoba ulang. Ekspos kesehatan dan telemetri. Perlakukan observabilitas sebagai fitur bawaan alih-alih tambahan. Eksternalisasi semua status ke layanan data terkelola, agar instans aplikasi tetap sekali pakai dan dapat diskalakan horizontal.

### Rencanakan strategi multi-cloud, hibrida, dan berdaulat secara pragmatis

Portabilitas berharga, tetapi kejarlah dengan mata terbuka. Bakukan pada abstraksi portabel seperti kontainer, Kubernetes, dan API terbuka, agar beban kerja dapat berpindah jika perlu. Tetapi hindari jebakan menolak setiap layanan terkelola, yang menukar produktivitas nyata dengan portabilitas hipotetis. Untuk persyaratan hibrida dan berdaulat, rancang agar beban kerja dan pipeline yang sama dapat berjalan di wilayah pilihan, pusat data privat, atau cloud berdaulat yang memenuhi aturan yurisdiksi dan residensi data. Jadikan batas kedaulatan dan residensi eksplisit dalam arsitektur dan kebijakan.

### Jadikan biaya terlihat dengan FinOps

Dalam lingkungan cloud elastis, biaya adalah konsekuensi langsung keputusan rekayasa, jadi beri insinyur visibilitas dan akuntabilitas. Tandai sumber daya untuk alokasi biaya. Atribusikan pengeluaran ke tim dan layanan. Tunjukkan data biaya di samping metrik kinerja. Sesuaikan ukuran beban kerja, pakai autoscaling untuk mencocokkan permintaan, dan reklamasi sumber daya menganggur. Tetapkan praktik FinOps yang menyatukan rekayasa, keuangan, dan produk, agar pengeluaran cloud menjadi tanggung jawab bersama yang berkelanjutan alih-alih kejutan triwulanan.

## Trade-off: kelebihan dan kekurangan

| Pilihan | Kelebihan | Kekurangan | Paling cocok |
|---|---|---|---|
| Kubernetes | Kuat, portabel, ekosistem besar | Kompleksitas curam; beban operasional | Banyak layanan pada skala besar |
| Layanan kontainer terkelola | Beban ops lebih rendah; mulai lebih cepat | Sebagian lock-in; kendali lebih sedikit | Tim yang menginginkan kesederhanaan |
| Satu klaster bersama | Penggunaan sumber daya efisien | Isolasi lebih sulit; radius ledakan | Tenant internal tepercaya |
| Klaster per tenant | Isolasi kuat | Biaya dan overhead lebih tinggi | Beban kerja saling tak percaya atau teregulasi |
| Portabilitas multi-cloud | Fleksibilitas; menghindari lock-in | Layanan penyebut-bersama terendah | Mitigasi risiko strategis |
| Layanan terkelola single-cloud mendalam | Produktivitas maksimum | Ketergantungan vendor | Tim yang berfokus kecepatan |

Trade-off menyeluruhnya adalah kemampuan versus kompleksitas. Kubernetes dan arsitektur cloud-native memberi elastisitas, ketahanan, dan kecepatan. Tetapi mereka memaksakan beban operasional dan kognitif substansial yang rutin diremehkan tim kecil. Dengan cara yang sama, mengejar portabilitas [multi-cloud](https://en.wikipedia.org/wiki/Multicloud) penuh menukar produktivitas dengan opsionalitas. Jawaban yang tepat bergantung pada skala dan risiko. Organisasi besar dengan banyak tim dan kebutuhan tata kelola kuat biasanya membenarkan investasi itu. Upaya lebih kecil sering lebih baik dilayani layanan terkelola yang menyembunyikan kompleksitas.

## Pertanyaan untuk didiskusikan dengan tim Anda

1. **Apakah Anda menandatangani citra dan memverifikasi tanda tangan saat deploy, dan apakah kerentanan kritis benar-benar memblokir build?** Citra adalah unit kepercayaan Anda, jadi rantai pasok di sekitarnya layak mendapat gerbang keras, bukan peringatan. Putuskan apakah hanya citra bertanda tangan dan terverifikasi yang boleh berjalan, apakah pemindaian memblokir temuan kritis atau sekadar mencatatnya, dan siapa yang memelihara registri terkurasi berisi citra dasar yang diperkeras tempat tim membangun. Untuk beban kerja enterprise dan pemerintah ini sering persyaratan kepatuhan, dan ia juga pertahanan terbaik Anda terhadap dependensi teracuni yang mencapai produksi. Bawa keadaan saat ini: berapa pecahan citra berjalan yang berasal dari dasar yang diperkeras, berapa yang membawa CVE kritis tak ditambal, dan apakah citra tak bertanda tangan mana pun saat ini dapat dijadwalkan. Jika temuan kritis tidak menghentikan deploy, pemindai Anda hanya hiasan.

2. **Bagaimana resource request, limit, dan kuota mencegah satu beban kerja membuat tetangganya kelaparan, tanpa membiarkan kapasitas mahal menganggur?** Pada klaster bersama, beban kerja tanpa limit dapat membuat crash atau melambatkan segala yang di sekitarnya, dan kuota yang ditetapkan terlalu longgar memboroskan keuntungan pemanfaatan yang membenarkan platform. Putuskan bawaan masuk akal, siapa yang menyetelnya, dan bagaimana Anda menangkap beban kerja tanpa request sama sekali. Pada skala besar ini kontrol keandalan sekaligus kontrol biaya, karena penyesuaian ukuran adalah tempat banyak penghematan FinOps tinggal. Bawa data: pemanfaatan klaster saat ini, seberapa sering beban kerja digusur atau dilambatkan, dan namespace mana yang tak punya kuota. Tujuannya pengemasan padat dan aman, jadi perlakukan limit yang hilang sebagai cacat yang ditolak platform.

3. **Status apa yang boleh hidup di dalam kontainer, dan ke mana semua yang lain pergi?** Ketahanan cloud-native bergantung pada instans sekali pakai yang dapat dijadwalkan ulang platform sesuka hati, dan itu hanya berlaku jika status penting hidup di layanan data terkelola alih-alih di disk lokal kontainer. Putuskan aturannya secara eksplisit, karena status yang tersimpan dalam kontainer secara tak sengaja menjadi kehilangan data pada penjadwalan ulang berikutnya. Bagi tim yang memigrasikan aplikasi lama ini sering bagian tersulit, karena layanan warisan mengasumsikan filesystem lokal yang stabil. Bawa inventaris: layanan mana yang menulis status lokal, mana yang bergantung pada sesi lengket atau afinitas node, dan apa yang dibutuhkan untuk mengeksternalisasi masing-masing. Sampai status eksternal, Anda punya kontainer yang tampak elastis tetapi sebenarnya tak dapat dipindahkan.

4. **Ketika banyak tim berbagi klaster, apakah model isolasi Anda dipilih dengan sengaja sebagai multitenansi lunak atau keras, dan apakah kontrol cocok dengan pilihan itu?** Namespace memisahkan tim internal tepercaya, tetapi tidak menahan beban kerja yang aktif bermusuhan atau terkompromi, dan memperlakukan tenansi lunak seolah keras adalah insiden keamanan yang menunggu terjadi. Putuskan per beban kerja apakah tenant sekadar butuh berbagi secara adil atau harus diasumsikan saling tak percaya, lalu cocokkan kontrol: namespace, kuota, kebijakan jaringan, dan RBAC untuk kasus lunak, klaster terpisah atau sandboxing lebih kuat untuk kasus keras. Bagi organisasi besar keputusan ini langsung mendorong biaya, karena klaster per tenant jauh lebih mahal daripada namespace bersama, jadi Anda ingin membelanjakan anggaran isolasi hanya di mana model ancaman menuntutnya. Bawa inventaris tenant: beban kerja mana yang berbagi klaster hari ini, mana yang menangani lalu lintas teregulasi atau menghadap eksternal, dan di mana kebijakan jaringan masih default-izinkan. Dalam pengaturan enterprise dan pemerintah, mencampur beban kerja saling tak percaya di bawah tenansi lunak adalah persis temuan yang akan ditandai auditor, jadi namai batasnya sebelum mereka.

5. **Berapa banyak Anda membayar untuk portabilitas multi-cloud, dan akankah Anda benar-benar pernah memakainya?** Membakukan pada kontainer, Kubernetes, dan API terbuka menjaga beban kerja dapat dipindahkan, tetapi menolak setiap layanan terkelola untuk mempertahankan opsi itu menukar produktivitas harian nyata dengan portabilitas yang mungkin tak pernah dilaksanakan organisasi. Putuskan di mana portabilitas adalah persyaratan sejati, seperti kewajiban kedaulatan atau keluar yang telah Anda tandatangani, versus di mana ia selimut kenyamanan yang memperlambat setiap tim. Pertimbangan yang bersaing adalah kecepatan: layanan terkelola mendalam mengirim fitur lebih cepat, dan arsitektur penyebut-bersama terendah adalah pajak tetap bagi setiap tim. Bawa buktinya: layanan terkelola mana yang telah Anda hindari dan berapa biayanya dalam waktu rekayasa, apakah Anda pernah memindahkan beban kerja antarpenyedia, dan apa yang sebenarnya diwajibkan kontrak Anda. Untuk pengadopsi pemerintah dan teregulasi, aturan residensi data dan cloud berdaulat dapat menjadikan portabilitas tak dapat ditawar, jadi rancang agar manifes dan pipeline yang sama berjalan di wilayah berdaulat dan enklave privat, tetapi jujurlah bahwa ini biaya kepatuhan, bukan asuransi gratis.

6. **Dapatkah setiap tim melihat apa yang dibelanjakannya, dan adakah yang memiliki tagihan sebelum menjadi kejutan?** Dalam platform elastis, biaya adalah keluaran langsung keputusan rekayasa, namun tanpa tag alokasi biaya dan dasbor yang terlihat pengeluaran terkumpul ke kolam bersama yang tak dirasakan siapa pun bertanggung jawab sampai keuangan mengeskalasi. Putuskan bagaimana Anda mengatribusikan biaya ke tim dan layanan, siapa yang meninjaunya, dan apakah insinyur melihat biaya di samping metrik kinerja atau hanya mendengarnya sekali triwulan. Ketegangannya antara akuntabilitas dan gesekan: dorong biaya terlalu keras dan setiap keputusan menjadi negosiasi anggaran, abaikan dan beban kerja menganggur dan terlalu besar diam-diam bertumpuk. Bawa angkanya: pengeluaran saat ini menurut tim, berapa banyak kapasitas menganggur atau terlalu besar, dan seberapa cepat beban kerja liar akan diperhatikan. Untuk anggaran enterprise dan pemerintah, pengeluaran cloud tak teratribusi adalah kegagalan tata kelola sekaligus risiko finansial nyata, jadi dirikan praktik FinOps yang menaruh rekayasa, keuangan, dan produk dalam percakapan yang sama alih-alih merekonsiliasi setelah kejadian.

## Lensa sektor

**Startup.** Raih layanan kontainer terkelola daripada klaster Kubernetes self-hosted: dengan dua layanan dan tanpa insinyur platform, control plane adalah gangguan yang tak sanggup Anda tanggung. Kemas citra kecil dari dasar minimal, sematkan versi, tambahkan satu pemindaian kerentanan ke build, dan dorong semua status ke basis data terkelola agar instans tetap sekali pakai. Lewati namespace, operator, dan portabilitas multi-cloud sampai Anda benar-benar punya layanan dan orang yang membenarkannya.

**Bisnis kecil.** Tanpa spesialis platform khusus dan anggaran ketat, bersandarlah keras pada layanan terkelola dan biarkan penyedia menjalankan orkestrasi yang kalau tidak harus Anda isi stafnya. Perlakukan dasar-dasar kontainer sebagai lantai keamanan Anda: citra minimal, penyematan versi, dan pemindaian dalam pipeline memberi sebagian besar perlindungan dengan upaya kecil. Pilih membeli platform yang didukung daripada membangunnya, dan jaga portabilitas secukupnya, kontainer standar dan API terbuka, agar Anda tidak terjebak jika harga atau ketentuan berubah.

**Enterprise.** Tugasnya tata kelola platform lintas banyak tim: tim platform pusat menyediakan citra dasar yang diperkeras, gerbang penandatanganan dan pemindaian, tenansi namespace dengan kuota, kebijakan jaringan, dan RBAC, plus tag alokasi biaya dan dasbor FinOps. Bakukan kontrak deployment agar ratusan layanan beroperasi dengan cara yang sama, dan kelola keamanan, multitenansi, dan biaya secara terpusat sementara tim melayani deployment sendiri. Danai tim platform dengan layak, karena platform kekurangan sumber daya menjadi hambatan yang ditunggu seluruh organisasi.

**Pemerintah.** Kedaulatan, residensi data, dan akuntabilitas publik membentuk arsitektur. Jalankan beban kerja pada kontainer standar dan Kubernetes agar pipeline yang sama berjalan di wilayah berdaulat dan enklave on-premises terakreditasi, dan kodekan batas residensi dan akses sebagai kebijakan alih-alih konvensi. Ambil citra dari registri internal yang diperkeras, terapkan multitenansi keras pada data paling sensitif, dan jaga portabilitas yang memberi Anda ketahanan dan daya tawar, karena aturan pengadaan sering melarang lock-in satu vendor.

## Contoh

**Startup.** Startup enam orang mengemas dua layanannya sebagai citra kontainer kecil yang dibangun dari dasar minimal, dan menjalankannya di layanan kontainer terkelola alih-alih klaster Kubernetes self-hosted, sehingga tak ada yang harus menjaga control plane. Mereka menyematkan versi citra dasar dan menambah pemindaian kerentanan ke build mereka, tetapi sengaja melewatkan fitur orkestrasi lebih berat sampai mereka benar-benar punya lebih dari segelintir layanan. Status hidup di Postgres terkelola, yang menjaga kontainer sekali pakai dan memungkinkan platform memulai ulang atau menskalakannya tanpa kehilangan data.

**Enterprise.** Sebuah perusahaan telekomunikasi menjalankan beberapa ratus [microservice](https://en.wikipedia.org/wiki/Microservices) di klaster Kubernetes bersama. Tim platform menyediakan citra dasar yang diperkeras, menegakkan penandatanganan citra dan gerbang kerentanan, dan mengisolasi unit bisnis ke dalam namespace dengan kuota, kebijakan jaringan, dan RBAC. Tag alokasi biaya dan dasbor FinOps mengatribusikan pengeluaran ke setiap lini produk, dan autoscaling menyesuaikan kapasitas dengan permintaan. Tim produk men-deploy puluhan kali sehari ke platform yang konsisten tanpa mengelola server. Perusahaan menjaga kendali pusat atas keamanan dan biaya.

**Pemerintah.** Sebuah layanan kesehatan nasional harus menjaga data warga dalam batas nasional dan di bawah kendali hukum nasional. Ia menjalankan beban kerjanya di wilayah cloud berdaulat memakai kontainer standar dan Kubernetes, sehingga pipeline dan manifes yang sama juga berjalan di lingkungan on-premises terakreditasi untuk data paling sensitif. Batas residensi data dan akses dikodekan sebagai kebijakan, citra diambil dari registri internal yang diperkeras, dan multitenansi keras mengisolasi beban kerja sensitif. Portabilitas antara wilayah berdaulat dan enklave privat memberi layanan ketahanan dan daya tawar tanpa mengorbankan kepatuhan.

## Kasus bisnis: motivasi, ROI, dan TCO

ROI kontainer dan orkestrasi datang dari pemanfaatan sumber daya lebih tinggi, deployment lebih cepat dan andal, penskalaan elastis yang mencocokkan pengeluaran dengan permintaan, dan ketahanan yang membaik lewat penyembuhan diri. Membakukan pada platform umum mengurangi upaya terduplikasi antartim dan mempercepat onboarding, karena setiap layanan mengikuti kontrak deployment dan operasional yang sama.

Analisis TCO harus jujur tentang beban operasional. Biaya adopsi mencakup staf rekayasa platform, pelatihan, perkakas keamanan untuk citra dan klaster, dan upaya berkelanjutan menjalankan platform itu sendiri. Biaya tidak mengadopsi mencakup deployment pesanan tidak konsisten antartim, pemanfaatan buruk infrastruktur mahal, penskalaan manual yang rapuh, dan kesulitan memenuhi persyaratan ketahanan dan kedaulatan. Bagi pimpinan, kasus bertumpu pada skala. Di bawah jumlah layanan tertentu kompleksitas mungkin tidak terbayar, dan layanan terkelola lebih bijak. Tetapi pada skala enterprise dan pemerintah, platform cloud-native teratur biasanya fondasi paling hemat biaya dan tangguh, asalkan Anda mendanai tim platform untuk menjalankannya dengan benar.

## Anti-pola dan jebakan

- **Citra gemuk tak terpindai.** Citra menggelembung dari dasar tak tepercaya membawa kerentanan tak perlu dan memperlambat segalanya.
- **Kubernetes untuk segalanya.** Mengadopsi orkestrator kompleks untuk segelintir layanan sederhana membeli kompleksitas tanpa imbalan.
- **Mengabaikan batas sumber daya.** Tanpa request dan limit, satu beban kerja dapat membuat tetangganya kelaparan atau crash.
- **Tenansi lunak untuk beban kerja bermusuhan.** Mengandalkan namespace saja untuk mengisolasi tenant yang saling tak percaya adalah insiden keamanan yang menunggu terjadi.
- **Kontainer berstatus tak sengaja.** Menyimpan status penting dalam kontainer sekali pakai menyebabkan kehilangan data saat dijadwalkan ulang.
- **Buta biaya.** Memperlakukan pengeluaran cloud sebagai overhead tetap alih-alih keluaran rekayasa menyebabkan tagihan liar.
- **Teater portabilitas.** Menolak semua layanan terkelola demi portabilitas yang tak akan pernah benar-benar dipakai organisasi.

## Model kematangan

**Tingkat 1: Memulai.** Kontainer dipakai ad hoc, jika sama sekali. Citra dibangun tangan dan tak terpindai, deployment manual dan reaktif, dan tak ada platform bersama, visibilitas biaya, atau model isolasi.

**Tingkat 2: Mengembangkan.** Tim mengontainerisasi aplikasi dan mengadopsi orkestrator, tetapi praktik bervariasi antarkelompok. Pemindaian citra, batas sumber daya, dan penandatanganan tidak konsisten, dan biaya serta multitenansi tidak diatur secara sistematis.

**Tingkat 3: Membakukan.** Platform terbakukan didokumentasikan dan ditegakkan di seluruh organisasi: citra dasar yang diperkeras, gerbang penandatanganan dan pemindaian, tenansi berbasis namespace dengan kuota dan kebijakan jaringan, RBAC, dan alokasi biaya. Pola cloud-native dan twelve-factor adalah norma yang diharapkan alih-alih pilihan lokal.

**Tingkat 4: Mengelola.** Platform diukur dan dikendalikan terhadap garis dasar. Anda melacak pemanfaatan klaster, pangsa citra berjalan yang dibangun dari dasar yang diperkeras, kerentanan kritis tak ditambal, frekuensi deployment dan tingkat kegagalan perubahan, tingkat penggusuran dan pelambatan, serta biaya per tim dan layanan terhadap anggaran. Gerbang ditegakkan atas bukti ini: limit sumber daya yang hilang dan citra tak bertanda tangan ditolak otomatis, dan penyimpangan dari standar memicu tindakan alih-alih peringatan.

**Tingkat 5: Mengorkestrasi.** Platform swalayan dan menyembuhkan diri, terintegrasi di seluruh organisasi dan adaptif. FinOps terus menyesuaikan ukuran dan mereklamasi kapasitas, arsitektur portabel mendukung persyaratan hibrida dan berdaulat, dan platform terus membaik dari pemakaian terukur, memensiunkan dan mengganti komponen seiring beban kerja, biaya, dan gambaran risiko bergeser.

## Gagasan untuk didiskusikan

- Pada skala apa mengadopsi Kubernetes berhenti menjadi kompleksitas demi kompleksitas dan mulai terbayar?
- Di mana batas yang tepat antara multitenansi lunak dan keras untuk beban kerja Anda?
- Seberapa banyak Anda harus berinvestasi pada portabilitas multi-cloud versus produktivitas layanan terkelola mendalam?
- Bagaimana Anda memberi insinyur akuntabilitas biaya nyata tanpa mengubah setiap keputusan menjadi negosiasi anggaran?
- Apa model tata kelola Anda untuk citra dasar, dan siapa yang memelihara registri yang diperkeras?
- Bagaimana persyaratan kedaulatan dan residensi data membentuk arsitektur platform Anda?

## Poin-poin utama

- Kontainer membakukan pengemasan dan runtime; orkestrasi membakukan operasi pada skala besar.
- Kebersihan citra, yaitu citra minimal, tersemat, terpindai, dan bertanda tangan, adalah keamanan fondasional.
- Pakai pola Kubernetes asli dan operator alih-alih membangun orkestrasi pesanan.
- Pilih model multitenansi dengan sengaja berdasarkan seberapa besar beban kerja saling memercayai.
- Ikuti twelve-factor dan perluas untuk kenyataan sistem terdistribusi seperti kegagalan parsial dan observabilitas.
- Perlakukan biaya sebagai keluaran rekayasa dan kelola terus-menerus lewat FinOps.

## Referensi dan bacaan lanjutan

- Adam Wiggins, *The Twelve-Factor App* (metodologi).
- Brendan Burns, Joe Beda, dan Kelsey Hightower, *Kubernetes Up & Running*.
- Bilgin Ibryam dan Roland Huß, *Kubernetes Patterns*.
- Cornelia Davis, *Cloud Native Patterns*.
- J.R. Storment dan Mike Fuller, *Cloud FinOps*.
- Liz Rice, *Container Security*.
- Cloud Native Computing Foundation (CNCF), definisi dan lanskap cloud-native.
