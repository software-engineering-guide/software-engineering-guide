# 3.2 Gaya dan pola arsitektural

## Tinjauan dan motivasi

Gaya arsitektural adalah bentuk luas yang dapat dipakai ulang untuk mengorganisasi sistem: bagaimana ia diuraikan, bagaimana bagian-bagiannya berkomunikasi, dan di mana batas-batasnya jatuh. Memilih salah satunya termasuk keputusan paling berdampak (dan paling disalahpahami) yang dibuat organisasi besar. Terlalu sering pilihan mengikuti mode ("semua orang memakai [mikroservis](https://en.wikipedia.org/wiki/Microservices)") alih-alih kendala nyata tim, domain, dan kenyataan operasional. Anda berakhir dengan salah satu dari dua kekacauan: sistem terdistribusi yang tidak sanggup dioperasikan organisasi, atau [monolit](https://en.wikipedia.org/wiki/Monolithic_application) kusut yang tidak dapat diubah siapa pun dengan aman. Keduanya bukan salah gaya. Keduanya datang dari mencocokkan gaya dengan situasi secara keliru.

Bagi tim pengembang besar, gaya penting terutama karena [Hukum Conway](https://en.wikipedia.org/wiki/Conway%27s_law): struktur sistem cenderung mencerminkan struktur komunikasi organisasi yang membangunnya. Jadi gaya arsitektural juga keputusan desain organisasi. Membagi sistem menjadi layanan sesungguhnya keputusan tentang membagi tim, kepemilikan, dan tanggung jawab on-call. Enterprise dengan ratusan insinyur dapat membiayai (dan sering membutuhkan) layanan berbutir halus dengan deployment independen, karena independensi itu cara banyak tim merilis tanpa saling memblokir. Paksakan pola yang sama pada satu tim kecil, dan ia mewarisi semua pajak operasional tanpa manfaat organisasi.

Lingkungan pemerintah dan enterprise menambah lebih banyak kendala: umur sistem yang panjang, kendali perubahan ketat, siklus pengadaan, integrasi dengan sistem pencatat yang mapan, dan kemampuan diaudit. Ini mendukung gaya yang menjaga batas eksplisit dan dependensi mudah diperiksa. Bab ini meninjau gaya utama: dari monolit hingga mikroservis, [arsitektur berbasis peristiwa](https://en.wikipedia.org/wiki/Event-driven_architecture) dengan [CQRS](https://en.wikipedia.org/wiki/Command_Query_Responsibility_Segregation) dan event sourcing, pola [service mesh](https://en.wikipedia.org/wiki/Service_mesh) dan gateway, [serverless](https://en.wikipedia.org/wiki/Serverless_computing), serta disiplin internal arsitektur [heksagonal](https://en.wikipedia.org/wiki/Hexagonal_architecture_(software)) dan bersih. Lebih penting lagi, bab ini membantu Anda mengetahui kapan masing-masing cocok.

*Lihat juga:* bab 2.2 (prinsip desain perangkat lunak, termasuk [Domain-Driven Design](https://en.wikipedia.org/wiki/Domain-driven_design)), bab 3.1 (dasar-dasar arsitektur), dan bab 3.3 (sistem terdistribusi).

## Prinsip utama

- **Gaya mengikuti gaya-gaya (forces), bukan mode.** Pilih berdasarkan ukuran tim, kompleksitas domain, beban, dan kematangan operasional, tidak pernah karena teknologi populer.
- **Kopling adalah musuh sebenarnya, bukan jumlah deployable.** Monolit yang dimodularisasi dengan baik mengalahkan big ball of mud terdistribusi.
- **Distribusi adalah biaya yang Anda bayar untuk independensi.** Pecah hanya ketika nilai deployment, penskalaan, atau isolasi kegagalan independen melebihi biaya panggilan jaringan, kegagalan parsial, dan konsistensi data lintas layanan.
- **Batas harus mengikuti domain bisnis.** Selaraskan layanan dan modul dengan bounded context (masing-masing model domain mandiri dengan batas eksplisitnya sendiri), bukan dengan lapisan teknis.
- **Rancang bagian dalam dengan baik terlepas dari bagian luar.** Pelapisan heksagonal/bersih menjaga logika bisnis independen dari kerangka kerja dan infrastruktur di setiap gaya.
- **Hukum Conway tak terhindarkan, jadi gunakan.** Rancang batas tim dan arsitektur bersama.
- **Mulai lebih sederhana daripada yang Anda kira perlu.** Anda dapat mengekstrak layanan dari monolit modular yang baik; menghapus distribusi dari kekacauan mikroservis prematur jauh lebih sulit.

## Rekomendasi

### Jadikan monolit modular sebagai bawaan; pecah dengan bukti

Mulai sebagian besar sistem sebagai satu unit yang dapat di-deploy dengan batas modul internal yang kuat: antarmuka jelas, tidak menjangkau data modul lain, dan aturan dependensi yang ditegakkan. Anda mendapat transaksi sederhana, refaktoring mudah, dan satu hal untuk di-deploy dan diamati. Pecah modul menjadi layanan sendiri hanya ketika Anda punya alasan konkret: bagian yang harus berskala sendiri, tim yang perlu men-deploy dengan irama sendiri, domain kegagalan yang harus diisolasi, atau persyaratan teknologi yang berbeda dari sisanya. Ketika Anda memecah, pecah sepanjang garis bounded context agar setiap layanan memiliki datanya dan mengekspos kontrak stabil.

### Ketahui kapan mikroservis layak dipertahankan

Mikroservis memberi Anda kemampuan deployment independen, penskalaan independen, isolasi kegagalan, dan kebebasan mencampur teknologi. Sebagai imbalannya mereka menuntut CI/CD (integrasi berkelanjutan dan pengiriman berkelanjutan) yang matang, infrastruktur otomatis, pelacakan terdistribusi, penemuan layanan, dan budaya on-call. Tanyakan pada diri sendiri dengan jujur: dapatkah organisasi Anda menjalankan puluhan layanan yang di-deploy independen di produksi dengan andal? Jika platform dan kematangan operasional belum ada, mikroservis hanya melipatgandakan mode kegagalan tanpa memberikan manfaatnya. Banyak organisasi paling berhasil dengan segelintir layanan berbutir kasar yang selaras dengan domain utama daripada sekawanan layanan kecil.

### Gunakan arsitektur berbasis peristiwa di tempat pemisahan dan asinkronitas membuahkan hasil

Arsitektur berbasis peristiwa memungkinkan produsen memancarkan fakta tanpa mengetahui siapa yang mengonsumsinya. Itu membeli kopling longgar, penyangga untuk lonjakan beban, dan cara mudah menambah konsumen baru. Pakai di tempat alur kerja secara alami asinkron dan reaktif. **CQRS** (Command Query Responsibility Segregation) memisahkan model tulis dari satu atau lebih model baca, yang membantu ketika beban atau bentuk baca dan tulis berbeda tajam. **Event sourcing** menyimpan status sebagai log peristiwa append-only alih-alih sebagai status saat ini, memberi Anda jejak audit sempurna dan perjalanan waktu. Itu ampuh bagi keuangan dan pemerintah, di mana "bagaimana kita sampai ke nilai ini?" adalah pertanyaan hukum, tetapi menambah kompleksitas nyata dalam pembuatan versi peristiwa, membangun ulang proyeksi, dan bernalar tentang konsistensi akhirnya. Raih ini dengan sengaja, bukan secara bawaan.

### Terapkan pola gateway, BFF, dan mesh untuk mengelola banyak layanan

**API gateway** memberi klien eksternal satu titik masuk, menangani autentikasi, pembatasan laju, perutean, dan terminasi [TLS](https://en.wikipedia.org/wiki/Transport_Layer_Security) (Transport Layer Security). **Backend-for-Frontend (BFF)** memberi setiap jenis klien (web, seluler, API mitra) lapisan agregasi yang disesuaikan sendiri, agar Anda menghindari API serba-sama yang membengkak. **Service mesh** memindahkan perhatian lintas bidang (mutual TLS, retry, timeout, pergeseran lalu lintas, dan telemetri) ke lapisan infrastruktur sidecar, sehingga tim aplikasi tidak perlu mengimplementasikan ulang. Tambahkan mesh hanya ketika jumlah layanan membuat penanganan perhatian ini per layanan tak terkelola. Untuk beberapa layanan, mesh lebih berat operasionalnya daripada sepadan.

### Timbang serverless dengan jujur

Function-as-a-service dan platform serverless terkelola mengambil pengelolaan server dari piring Anda, berskala ke nol, dan menagih per pemakaian, yang bagus untuk beban kerja berlonjak, berbasis peristiwa, atau berdasar rendah dan untuk tim kecil. Trade-off-nya nyata: latensi cold-start, batas waktu eksekusi dan sumber daya, pengujian lokal lebih sulit, kemungkinan lock-in vendor, dan biaya yang dapat melebihi infrastruktur yang disediakan pada volume tinggi berkelanjutan. Pakai serverless di tempat ekonomi dan kesederhanaan operasionalnya jelas menang. Jangan paksa sistem inti berthroughput tinggi yang stabil ke dalamnya karena antusiasme.

### Jaga logika bisnis tetap bersih di dalam setiap layanan

Apa pun gaya luarnya, jaga bagian dalam tetap bersih dengan **heksagonal (ports and adapters)** atau **arsitektur bersih**: aturan bisnis di pusat, hanya bergantung pada abstraksi; kerangka kerja, basis data, dan pesan di tepi sebagai adaptor yang dapat diganti. Ini menjaga logika domain Anda yang berharga dapat diuji tanpa infrastruktur dan portabel melintasi perubahan teknologi: keunggulan menentukan bagi sistem pemerintah dan enterprise berumur panjang yang akan hidup lebih lama daripada beberapa generasi kerangka kerja.

## Trade-off: kelebihan dan kekurangan

| Gaya | Terbaik ketika | Kelebihan | Kekurangan |
|---|---|---|---|
| Monolit modular | Sebagian besar sistem, terutama di awal | Operasi sederhana, transaksi dan refaktoring mudah | Satu unit deploy; berskala sebagai satu; risiko erosi |
| Mikroservis | Banyak tim, skala tinggi, platform matang | Deploy/skala independen, isolasi kegagalan | Kompleksitas terdistribusi, konsistensi data, biaya ops tinggi |
| Berbasis peristiwa / CQRS / event sourcing | Alur kerja asinkron, kebutuhan audit, baca/tulis berbeda | Kopling longgar, kemampuan diaudit, pembacaan berskala | Konsistensi akhirnya, pembuatan versi peristiwa, debugging lebih sulit |
| Serverless | Kerja berlonjak atau berdasar rendah, berbasis peristiwa | Tanpa pengelolaan server, skala ke nol, bayar-per-pakai | Cold start, batas, lock-in, biaya pada beban stabil tinggi |

Tema berulangnya: Anda membeli fleksibilitas dan independensi dengan kompleksitas operasional dan kognitif. Gaya terdistribusi dan berbasis peristiwa melepas kesederhanaan satu tumpukan panggilan dan satu transaksi sebagai ganti kemampuan berskala, men-deploy, dan gagal secara independen. Pertukaran itu membuahkan hasil pada skala besar dan dengan platform matang. Tanpa itu, merusak. Disiplin internal (heksagonal/bersih) hampir selalu sepadan, karena murah dan menjaga opsi Anda terbuka untuk mengganti gaya kelak.

## Pertanyaan untuk didiskusikan dengan tim Anda

1. **Sebelum memecah layanan berikutnya, apakah Anda akan memecah tim yang memilikinya, dan siapa yang berwenang melakukannya?** Hukum Conway berarti batas layanan sesungguhnya batas tim, sehingga pemecahan yang tidak didukung bagan organisasi menghasilkan monolit terdistribusi: dua deployable, satu kereta rilis, on-call bersama. Dalam enterprise besar wewenang membentuk ulang tim biasanya berada di atas rekayasa, pada garis pelaporan, keuangan, dan SDM, itulah mengapa arsitektur dan desain organisasi harus diputuskan bersama. Bawa bukti ke diskusi: apakah layanan yang diusulkan punya tim yang dapat memilikinya dari ujung ke ujung, mengisi on-call-nya sendiri, dan men-deploy dengan irama sendiri? Jika jawabannya tidak, danai tim itu atau pertahankan kemampuan sebagai modul dalam monolit. Memecah kode tanpa memecah kepemilikan membeli setiap biaya distribusi dan tak satu pun independensi.

2. **Dapatkah Anda men-deploy setiap layanan secara independen hari ini, atau diam-diam mereka dirilis serentak?** Monolit terdistribusi adalah hasil terburuk dalam bab ini: Anda membayar panggilan jaringan, kegagalan parsial, dan konsistensi data lintas layanan, namun tetap tidak dapat merilis satu tanpa yang lain. Tanda-tandanya adalah basis data bersama, pustaka bersama yang memaksa peningkatan terkoordinasi, dan tes integrasi yang harus menjalankan seluruh properti bersama. Bagi tim besar ini diam-diam membatasi throughput, karena setiap tim mengantre di belakang satu rilis padahal diagram menunjukkan independensi. Ambil satu perubahan terbaru dan hitung berapa layanan yang harus di-deploy bersama agar aman; jika angkanya lebih dari satu untuk perubahan yang menyentuh satu kemampuan, batas Anda keliru. Perbaikannya biasanya memberi setiap layanan datanya sendiri dan kontrak stabil berversi, bukan menambah lebih banyak layanan.

3. **Pemecahan layanan Anda yang ada mana yang berhenti membuahkan hasil, dan akankah Anda mengonsolidasikannya kembali?** Kebiasaan paling maju bab ini adalah memperlakukan keputusan gaya sebagai dapat dibalik: ekstrak ketika pendorong muncul, dan gabung kembali ketika pendorong lenyap. Kebanyakan organisasi hanya memecah, sehingga nanoservis dan layanan entitas yang cerewet menumpuk sampai orkestrasi dan beban jaringan melampaui pekerjaan yang dilakukan setiap layanan. Cari layanan yang selalu di-deploy bersama, yang ada karena tabel basis data alih-alih kemampuan bisnis, atau yang lompatan jaringannya kini mendominasi latensi permintaan. Dalam properti enterprise dan pemerintah, di mana jumlah personel dan anggaran diteliti, melipat dua layanan tipis kembali menjadi satu layanan berbutir kasar adalah langkah yang sah dan menghemat biaya, bukan pengakuan kegagalan. Letakkan konsolidasi ulang di meja sama terbukanya dengan ekstraksi, dan putuskan keduanya dengan bukti yang sama.

4. **Apakah platform dan kematangan on-call Anda benar-benar mendukung gaya yang Anda usulkan, dan dapatkah Anda menyebut celah spesifiknya sebelum berkomitmen?** Mikroservis, mesh, dan tulang punggung berbasis peristiwa hanya memberikan manfaatnya di atas CI/CD yang matang, pelacakan terdistribusi, penemuan layanan, dan budaya on-call yang dapat bernalar tentang kegagalan parsial. Organisasi besar cenderung memutuskan gaya target dalam forum arsitektur dan menemukan platform yang hilang belakangan, ketika puluhan layanan sudah di produksi dan setiap insiden memakan jam untuk didiagnosis. Timbang daya tarik deployment dan penskalaan independen terhadap pertanyaan sadar tentang siapa yang menjalankannya pukul 3 pagi: pemecahan yang sama yang membebaskan tim merilis paralel juga melipatgandakan mode kegagalan yang harus dipahami setiap tim. Bawa inventaris jujur ke diskusi: frekuensi deployment saat ini, waktu rata-rata pemulihan, apakah Anda punya pelacakan lintas batas layanan, dan berapa banyak layanan yang secara realistis dapat dioperasikan satu tim. Dalam lingkungan enterprise dan pemerintah, tambahkan lead time pengadaan dan perekrutan untuk kemampuan platform yang tidak Anda miliki, karena gaya yang mengasumsikan mesh dan tim platform yang belum Anda danai adalah rencana menjalankan properti yang tidak dapat didukung.

5. **Untuk bagian domain mana jejak audit event-sourced penuh merupakan kebutuhan hukum alih-alih kenyamanan, dan siapa yang berwenang memutuskan?** Event sourcing dan CQRS membeli Anda riwayat sempurna yang dapat direkonstruksi dan model baca yang berskala sendiri, tetapi memakan biaya pembuatan versi peristiwa, pembangunan ulang proyeksi, dan penalaran tentang konsistensi akhirnya sepanjang umur sistem. Diterapkan pada domain yang tidak pernah membutuhkan jejak audit, kompleksitas itu pajak murni; ditahan dari domain di mana "bagaimana kita sampai ke nilai ini?" adalah pertanyaan hukum, ketiadaannya adalah kegagalan kepatuhan. Pertimbangan yang bersaing adalah kemampuan diaudit dan skalabilitas kueri di satu sisi, dan kesulitan debugging serta beban kognitif pengembang di sisi lain, sehingga keputusan menjadi milik orang yang memahami kewajiban regulasi dan beban operasional, bukan siapa pun yang paling antusias pada pola. Bawa persyaratan retensi dan rekonstruksi hukum atau kontraktual yang spesifik, volume peristiwa yang diharapkan, dan estimasi jujur pekerjaan pembuatan versi dan proyeksi. Di bidang keuangan, pajak, dan pemerintah, di mana merekonstruksi keputusan bertahun-tahun kemudian bisa menjadi kewajiban undang-undang, namai pemilik yang bertanggung jawab yang menandatangani bahwa bounded context tertentu memerlukan, atau tidak memerlukan, log peristiwa tak berubah.

6. **Bagaimana Anda akan menghentikan monolit modular dari erosi agar ekstraksi kelak tetap murah, dan apa yang akan menegakkan batas?** Seluruh kasus memulai dengan monolit modular bertumpu pada janji bahwa batas internal yang bersih membuat ekstraksi layanan kelak terjangkau, namun batas itu membusuk diam-diam begitu tenggat menggoda satu modul menjangkau data modul lain. Bagi tim besar dengan banyak kontributor, niat baik dan tinjauan kode saja tidak akan menjaga garis; tanpa mekanisme penegak, monolit diam-diam menjadi big ball of mud yang hendak dihindari gaya ini. Timbang gesekan aturan dependensi dan antarmuka modul yang ditegakkan terhadap biaya menemukan, bertahun-tahun kemudian, bahwa tak ada batas yang nyata dan setiap ekstraksi berarti mengurai status bersama. Bawa bukti: apakah batas modul ditegakkan oleh perkakas build, analisis statis, atau struktur paket, atau hanya konvensi terdokumentasi yang diabaikan enam penggabungan terakhir? Dalam sistem enterprise dan pemerintah berumur panjang yang harus bertahan dari kendali perubahan ketat dan beberapa generasi kerangka kerja, perlakukan penegakan batas sebagai kontrol yang dapat diaudit, agar opsi untuk mendistribusikan kelak adalah yang benar-benar Anda jaga alih-alih yang Anda asumsikan masih Anda pegang.

## Lensa sektor

**Startup.** Jadikan satu monolit modular sebagai bawaan dan tahan tarikan mikroservis, karena sumber daya Anda yang paling langka adalah perhatian rekayasa dan sekawanan layanan adalah pajak operasional yang tidak sanggup Anda bayar sebelum kecocokan produk-pasar. Jaga batas modul bersih agar Anda dapat mengekstrak kelak, dan raih serverless di tempat skala-ke-nol dan bayar-per-pakai cocok dengan beban Anda yang berlonjak dan berdasar rendah. Pecah tepat satu hal hanya ketika pendorong konkret muncul, seperti pengirim notifikasi yang berlonjak, dan tidak lebih awal.

**Bisnis kecil.** Tanpa tim platform dan dengan anggaran ketat, pilih monolit atau segelintir layanan berbutir kasar pada platform terkelola, dan beli infrastruktur ter-hosting alih-alih membangun mesh, pelacakan, dan penemuan layanan sendiri. Timbang serverless dan basis data terkelola sebagai cara menghindari menjalankan server sama sekali, dan waspadai desain terdistribusi yang beban operasionalnya tidak ada orang untuk memikulnya. Arsitektur yang tepat adalah yang dapat benar-benar di-deploy, diamati, dan dipulihkan oleh satu atau dua orang.

**Enterprise.** Masalah nyatanya adalah banyak tim dan Hukum Conway: selaraskan layanan berbutir kasar dengan bounded context dan kepemilikan tim, dan berinvestasilah dengan sengaja pada platform (CI/CD, pelacakan, mesh, dan penemuan layanan) yang membuat distribusi aman. Bakukan pola gateway, BFF, dan arsitektur bersih internal agar kelompok berhenti menciptakannya ulang, dan atur ekstraksi serta konsolidasi ulang sebagai keputusan portofolio berbasis bukti alih-alih preferensi lokal. Anggarkan biaya operasional setiap pemecahan secara eksplisit, karena pada skala Anda kegagalan monolit terdistribusi mahal dan lambat diurai.

**Pemerintah.** Umur sistem yang panjang, kendali perubahan ketat, siklus pengadaan, dan kemampuan diaudit membentuk pilihan: pilih gaya dengan batas eksplisit yang dapat diperiksa dan kontrak tahan lama yang hidup lebih lama daripada vendor dan generasi kerangka kerja. Event sourcing layak kompleksitasnya di tempat merekonstruksi keputusan yang menghadap warga adalah kewajiban undang-undang, jadi pakai dengan sengaja untuk buku besar inti dan jaga arsitektur bersih di dalam setiap layanan untuk mengisolasi aturan yang berubah setiap anggaran. Perlakukan portabilitas dan jalan keluar dari serverless atau platform vendor proprietari sebagai persyaratan pengadaan, bukan renungan belakangan.

## Contoh

**Startup.** Sebuah startup empat orang yang membangun produk penjadwalan merasa tertekan memulai dengan mikroservis karena pesaing menulis blog tentangnya, tetapi menolak. Mereka merilis satu monolit modular dengan batas internal jelas (penjadwalan, penagihan, notifikasi) sebagai modul terpisah dalam satu deployable, sehingga satu insinyur dapat menjalankan seluruhnya secara lokal dan rilis adalah satu dorongan. Seiring produk menemukan daya tarik, hanya pengirim notifikasi, yang menyebar ke email dan SMS di bawah beban berlonjak, yang ditarik ke layanannya sendiri. Mereka tidak mewarisi pajak operasional selusin layanan selagi masih berburu kecocokan produk-pasar.

**Enterprise.** Sebuah perusahaan e-commerce besar mulai sebagai monolit modular. Seiring lalu lintas tumbuh dan tim berlipat, ia menarik domain berbeban tertinggi dan paling independen berkembang (katalog, keranjang, checkout, dan pencarian) ke layanan terpisah, masing-masing memiliki datanya. Checkout memancarkan peristiwa yang dikonsumsi inventaris, pemenuhan pesanan, dan analitik lewat tulang punggung peristiwa, sehingga konsumen baru (deteksi penipuan, loyalitas) dapat terpasang tanpa menyentuh checkout. API gateway menangani autentikasi dan pembatasan laju, dan BFF menyesuaikan payload untuk seluler. Domain berlalu lintas lebih rendah yang tersisa tetap di monolit, yang menghindari fragmentasi yang tidak perlu.

**Pemerintah.** Otoritas pajak membangun platform penilaian di atas event sourcing untuk buku besar inti, karena setiap perubahan pada kewajiban wajib pajak harus dapat direkonstruksi dan diaudit secara hukum selama bertahun-tahun. Perintah (ajukan pengembalian, terapkan pembayaran, terbitkan penyesuaian) menghasilkan peristiwa tak berubah, dan model baca memproyeksikan saldo saat ini untuk petugas dan warga. CQRS memungkinkan sisi kueri yang menghadap publik berskala sendiri untuk musim pengajuan puncak tanpa mempertaruhkan sisi tulis. Di dalam, setiap layanan mengikuti arsitektur bersih, sehingga aturan penilaian, yang berubah setiap anggaran, tetap terisolasi dari teknologi persistensi dan pesan.

## Kasus bisnis: motivasi, ROI, dan TCO

Uang yang dipertaruhkan dalam pilihan gaya sangat besar, karena keputusan itu mahal dibalik. Adopsi mikroservis terlalu dini dan Anda menggelembungkan total biaya kepemilikan lewat pembangunan platform, infrastruktur terduplikasi, debugging terdistribusi, dan beban operasi lebih berat: biaya yang tetap bersama Anda sepanjang umur sistem. Menolak memecah monolit yang benar-benar kelebihan beban membatasi throughput pengiriman: tim mengantre di belakang rilis bersama, dan setiap perubahan mempertaruhkan seluruh sistem. Percakapan ROI sesungguhnya tentang mencocokkan belanja operasional dengan kebutuhan organisasi.

Ajukan kasus kepada pimpinan dalam hal throughput dan risiko, bukan teknologi. Kemampuan deployment independen berarti lebih banyak tim merilis secara paralel dan lead time lebih singkat: kecepatan bisnis terukur. Isolasi kegagalan berarti lebih sedikit pemadaman total dan radius ledakan lebih kecil: ketersediaan terukur dan perlindungan reputasi. Tetapi sama jujurnya tentang investasi platform yang dituntut setiap gaya: mesh, pelacakan, dan kematangan CI/CD adalah prasyarat, bukan tambahan opsional, dan biayanya termasuk dalam TCO. Bagi banyak organisasi jalur termurah adalah monolit yang dimodularisasi dengan baik sekarang, dengan batas internal bersih yang membuat ekstraksi kelak murah. Itu membeli opsi untuk mendistribusikan tanpa membayarnya sebelum Anda membutuhkannya.

## Anti-pola dan jebakan

- **Monolit terdistribusi.** Layanan yang harus di-deploy bersama dan berbagi basis data: semua biaya distribusi, tanpa independensi.
- **Nanoservis.** Layanan sangat berbutir halus sehingga orkestrasi dan beban jaringan melampaui pekerjaan yang dilakukannya.
- **Mikroservis tanpa platform.** Memecah sebelum Anda punya CI/CD, pelacakan, dan kematangan on-call; mode kegagalan berlipat.
- **Layanan entitas.** Memecah menurut tabel basis data ("layanan User," "layanan Order") alih-alih kemampuan bisnis, memaksa panggilan lintas layanan yang cerewet untuk setiap operasi.
- **Event sourcing di mana-mana.** Menerapkannya pada domain yang tidak membutuhkan jejak audit, membayar pajak kompleksitas tanpa manfaat.
- **Gateway sebagai monolit.** Menaruh logika bisnis di API gateway, menciptakan ulang titik sempit pusat.
- **Inti terkopel kerangka kerja.** Logika bisnis kusut dengan kerangka kerja web atau ORM (object-relational mapping), membuat pengujian dan perubahan teknologi menyakitkan.

## Model kematangan

- **Tingkat 1: Memulai.** Gaya dipilih karena mode atau kebetulan. Anda punya satu monolit kusut atau kekacauan terdistribusi tidak sengaja, batas mengikuti lapisan teknis atau sejarah alih-alih domain, dan pemecahan terjadi secara reaktif ketika sesuatu rusak.
- **Tingkat 2: Mengembangkan.** Beberapa tim menggambar batas modul yang disengaja di dalam monolit atau mendirikan beberapa layanan berbutir kasar, dan sebagian perhatian lintas bidang ditangani konsisten. Praktik tidak merata: satu kelompok menyelaraskan layanan dengan bounded context sementara yang lain masih memecah menurut tabel basis data, dan ekstraksi tetap ad hoc.
- **Tingkat 3: Membakukan.** Pendekatan terdokumentasi ditegakkan di seluruh organisasi: layanan selaras dengan bounded context dan memiliki datanya, pola gateway dan BFF dipakai bila sesuai, pelapisan bersih atau heksagonal internal adalah standar, dan setiap pemecahan memerlukan pendorong yang dinyatakan. Batas modul ditegakkan perkakas, bukan hanya konvensi.
- **Tingkat 4: Mengelola.** Keputusan gaya diukur dan dikendalikan terhadap garis dasar. Anda melacak frekuensi deployment dan lead time per layanan, waktu rata-rata pemulihan, berapa banyak layanan yang harus di-deploy bersama untuk perubahan tipikal, dan latensi lompatan jaringan, dan membandingkan biaya setiap pemecahan terhadap independensi yang hendak dibelinya. Bukti, bukan preferensi, menentukan apakah batas bertahan, dan penyimpangan menuju monolit terdistribusi tertangkap metrik alih-alih pemadaman.
- **Tingkat 5: Mengorkestrasi.** Arsitektur terintegrasi dengan desain organisasi dan terus beradaptasi. Platform matang (CI/CD, pelacakan, dan mesh bila beralasan) membuat distribusi dan konsolidasi ulang murah, tim rutin mengekstrak ketika pendorong muncul dan melipat layanan kembali ketika satu lenyap, dan pilihan gaya diseimbangkan ulang seiring bergesernya topologi tim, beban, dan gambaran risiko di seluruh properti.

## Gagasan untuk didiskusikan

1. Di mana dalam sistem Anda monolit sebenarnya kekuatan, dan di mana ia hambatan sejati?
2. Pendorong konkret apa yang akan membenarkan ekstraksi layanan berikutnya, dan dapatkah Anda menyebutnya sebelum membangun?
3. Apakah organisasi Anda memiliki kematangan operasional yang dituntut mikroservis? Apa yang hilang?
4. Untuk bagian domain Anda yang mana jejak audit event-sourced penuh merupakan kebutuhan hukum atau bisnis versus sekadar bagus untuk dimiliki?
5. Seberapa baik batas layanan Anda saat ini mencerminkan batas tim Anda, dan apakah keselarasan itu membantu atau merugikan?
6. Jika Anda harus mengganti kerangka kerja web atau basis data tahun depan, berapa banyak logika bisnis Anda yang harus ditulis ulang?

## Poin-poin utama

- Pilih gaya arsitektural dari gaya-gaya nyata (ukuran tim, domain, beban, kematangan operasional), bukan dari mode.
- Monolit modular adalah bawaan yang tepat untuk sebagian besar sistem; ekstrak layanan hanya dengan pendorong konkret dan sepanjang garis bounded context.
- Mikroservis menukar kompleksitas operasional dan kognitif dengan deployment, penskalaan, dan isolasi kegagalan independen; mereka membutuhkan platform matang.
- Berbasis peristiwa, CQRS, dan event sourcing menawarkan pemisahan dan kemampuan diaudit dengan biaya konsistensi akhirnya dan kompleksitas pembuatan versi; adopsi dengan sengaja.
- Gateway, BFF, dan mesh menjinakkan properti banyak layanan tetapi menambah bobot; perkenalkan ketika skala menuntut, bukan sebelumnya.
- Terapkan arsitektur heksagonal/bersih di dalam setiap layanan untuk menjaga logika bisnis berharga dapat diuji dan tahan lama melintasi perubahan teknologi.

## Referensi dan bacaan lanjutan

- Sam Newman, *Building Microservices* dan *Monolith to Microservices*
- Chris Richardson, *Microservices Patterns*
- Eric Evans, *Domain-Driven Design*
- Vaughn Vernon, *Implementing Domain-Driven Design*
- Robert C. Martin, *Clean Architecture*
- Alistair Cockburn, "Hexagonal Architecture (Ports and Adapters)"
- Gregor Hohpe dan Bobby Woolf, *Enterprise Integration Patterns*
- Martin Fowler, *Patterns of Enterprise Application Architecture* (dan artikel tentang CQRS dan Event Sourcing)
- Matthew Skelton dan Manuel Pais, *Team Topologies*
