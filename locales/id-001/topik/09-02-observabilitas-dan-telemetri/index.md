# 9.2 Observabilitas dan telemetri

## Tinjauan dan motivasi

[Telemetri](https://en.wikipedia.org/wiki/Telemetry) adalah data yang dipancarkan sistem tentang perilakunya sendiri: metrik, log, trace, dan peristiwa yang dikumpulkan dari perangkat lunak yang berjalan. Pemantauan menjawab pertanyaan yang sudah Anda tahu untuk diajukan dari telemetri itu. Apakah disk penuh? Apakah tingkat galat di atas ambang? Apakah layanan hidup? [Observabilitas](https://en.wikipedia.org/wiki/Observability_(software)) lebih luas. Ia adalah kemampuan mengajukan pertanyaan baru tentang keadaan internal sistem dari luar, tanpa mengirim kode baru, agar Anda dapat memahami perilaku yang tak pernah diantisipasi. Seiring sistem tumbuh menjadi arsitektur terdistribusi, [microservice](https://en.wikipedia.org/wiki/Microservices), dan [berbasis peristiwa](https://en.wikipedia.org/wiki/Event-driven_architecture), kegagalan yang paling menyakitkan adalah yang tak diduga siapa pun, dan observabilitas adalah yang memungkinkan Anda men-debug-nya. Pemantauan memberi tahu bahwa ada yang salah. Observabilitas membantu Anda mencari tahu mengapa.

Bagi tim besar, perbedaan ini menentukan. Anda dapat memahami monolit dengan membaca log di satu mesin. Platform modern mencakup ratusan layanan, banyak tim, beberapa wilayah, dan dependensi pihak ketiga, di mana satu permintaan pengguna dapat menyentuh puluhan komponen. Tak seorang pun memegang seluruh sistem di kepalanya. Telemetri bersama berkualitas tinggi menjadi jaringan penghubung yang memungkinkan insinyur mana pun mengikuti permintaan melintasi batas, menyelaraskan gejala di seluruh layanan, dan bernalar tentang sistem yang tak sepenuhnya dimiliki siapa pun. Tanpanya, insiden berlarut-larut, saling menyalahkan antartim, dan akar masalah tetap tersembunyi.

Sistem enterprise dan pemerintah menaikkan taruhan dengan kepatuhan, kemampuan diaudit, dan akuntabilitas publik. Regulator mungkin mewajibkan bukti siapa mengakses apa dan kapan. Tim keamanan membutuhkan telemetri untuk mendeteksi intrusi. Layanan menghadap warga harus menunjukkan mereka memenuhi komitmen kinerja terbitannya. Observabilitas yang baik melayani semuanya sekaligus: ia perkakas rekayasa, kontrol keamanan, dan mekanisme akuntabilitas dalam satu. Membakukan pada instrumentasi terbuka menghindari lock-in pada agen proprietari satu vendor, yang sangat penting ketika sistem harus bertahan puluhan tahun dan melewati siklus pengadaan.

*Lihat juga:* bab 9.1 (site reliability engineering dan SLO), bab 9.3 (manajemen insiden), dan bab 3.3 (sistem terdistribusi).

## Prinsip utama

- **Instrumentasi untuk pertanyaan yang tak diketahui.** Rancang telemetri agar Anda dapat menyelidiki kegagalan baru, di luar yang Anda prediksi.
- **Tiga pilar, satu cerita.** Metrik, log, dan trace adalah pandangan yang saling melengkapi; nilainya berlipat ketika dikorelasikan, bukan disilokan.
- **Strukturkan segalanya.** Telemetri terstruktur yang dapat diurai mesin mengalahkan teks bebas yang hanya dapat dibaca manusia.
- **Korelasikan dengan pengenal bersama.** ID trace dan permintaan yang dipropagasi di mana-mana memungkinkan Anda menjahit satu peristiwa lintas layanan.
- **Beri peringatan atas gejala, bukan penyebab.** Panggil manusia untuk masalah terlihat pengguna; biarkan dasbor dan investigasi memunculkan penyebab yang mendasarinya.
- **Setiap panggilan harus dapat ditindaklanjuti.** Peringatan yang tak membutuhkan tindakan manusia adalah derau yang mengikis kepercayaan dan menyebabkan kelelahan.
- **Kardinalitas tinggi adalah fitur.** Kemampuan mengiris menurut pengguna, permintaan, wilayah, dan versi yang membuat debugging di produksi mungkin.
- **Miliki instrumentasi Anda.** Bakukan pada telemetri terbuka dan netral vendor agar Anda mengendalikan data dan dapat berganti backend.

## Rekomendasi

### Bangun di atas tiga pilar dan lebih

**Metrik** adalah deret waktu numerik, murah disimpan dan ideal untuk dasbor, tren, dan ambang peringatan. **Log** adalah catatan peristiwa diskret berstempel waktu, kaya detail dan esensial untuk investigasi forensik. **[Trace](https://en.wikipedia.org/wiki/Tracing_(software))** mengikuti satu permintaan saat bergerak melalui layanan, menunjukkan latensi dan dependensi di graf panggilan terdistribusi. Di luar ini, pertimbangkan **peristiwa** (perubahan keadaan bermakna seperti deploy), **profil** (di mana kode menghabiskan CPU dan memori), dan **[real user monitoring](https://en.wikipedia.org/wiki/Real_user_monitoring)** atas pengalaman klien yang sebenarnya. Tak ada satu pilar pun yang cukup sendiri. Tujuannya bergerak lancar di antara mereka selama investigasi.

### Bakukan pada OpenTelemetry dan logging terstruktur

Adopsi [OpenTelemetry](https://en.wikipedia.org/wiki/OpenTelemetry) sebagai standar netral vendor untuk menghasilkan dan mengumpulkan metrik, log, dan trace. Ia memisahkan instrumentasi dari backend analisis, sehingga Anda dapat berganti vendor tanpa menginstrumentasi ulang ratusan layanan. Properti itu kritis untuk sistem enterprise dan pemerintah berumur panjang. Pancarkan log sebagai catatan terstruktur (misalnya JSON) dengan nama bidang konsisten untuk cap waktu, keparahan, layanan, dan pengenal. Propagasikan ID trace atau korelasi dari tepi melalui setiap panggilan hilir, dan sertakan dalam setiap baris log dan exemplar metrik, agar tiga pilar terhubung otomatis.

### Rancang peringatan untuk kemampuan ditindaklanjuti dan derau rendah

Filosofi peringatan Anda menentukan apakah on-call berkelanjutan. Beri peringatan terutama atas gejala yang dirasakan pengguna, diekspresikan sebagai burn rate SLO ([service level objective](https://en.wikipedia.org/wiki/Service-level_objective)). Panggil ketika Anda menghabiskan anggaran galat (kekurangan yang diizinkan dari tujuan itu) cukup cepat untuk melanggarnya, memakai peringatan burn-rate multi-jendela untuk menyeimbangkan deteksi cepat terhadap alarm palsu. Sisihkan panggilan untuk masalah yang membutuhkan tindakan manusia segera, dan alirkan sisanya ke tiket atau dasbor. Pangkas peringatan yang menyala tanpa membutuhkan tindakan, tanpa ampun, karena kelelahan peringatan adalah penyebab utama insiden nyata yang terlewat dan kelelahan on-call. Setiap peringatan harus terhubung ke runbook.

### Modelkan kesehatan dengan dasbor dan pemantauan SLO

Bangun dasbor di sekitar model kesehatan yang jelas, bukan dinding setiap metrik yang Anda punya. Kerangka awal yang baik adalah "empat sinyal emas": latensi, lalu lintas, galat, dan saturasi. Buat dasbor tingkat layanan yang menunjukkan status SLO dan sisa anggaran galat sekilas, plus dasbor tingkat lebih tinggi yang memodelkan kesehatan sistem dan perjalanan pengguna secara keseluruhan. Kurasi dengan sengaja, karena dasbor yang menunjukkan segalanya mengomunikasikan ketiadaan. Jaga dekat dengan peringatan dan runbook, agar penanggap bergerak cepat dari sinyal ke konteks ke tindakan.

### Aktifkan debugging di produksi dengan kardinalitas tinggi

Masalah produksi tersulit mengenai irisan sempit: satu pelanggan, satu wilayah, satu versi API, satu jenis perangkat. Untuk menyelidikinya Anda butuh telemetri **kardinalitas tinggi**, kemampuan mengelompokkan dan memfilter menurut bidang dengan banyak nilai berbeda seperti ID pengguna atau ID permintaan. Peristiwa lebar dengan atribut kaya yang membawa banyak dimensi per catatan memungkinkan Anda mengajukan pertanyaan sembarang setelah kejadian. Jaga kardinalitas dan fidelitas sampling yang cukup untuk mengisolasi pencilan, dan pilih trace tertaut exemplar agar lonjakan pada metrik mengarahkan Anda langsung ke permintaan lambat yang representatif.

### Kelola biaya, retensi, dan sampling

Volume telemetri tumbuh bersama sistem dan dapat berubah menjadi pengeluaran besar. Tetapkan kebijakan retensi menurut kelas data: simpan data resolusi tinggi sebentar dan agregat lebih lama. Terapkan sampling cerdas pada trace, condong ke menyimpan galat dan permintaan lambat, agar Anda mempertahankan ekor menarik tanpa membayar untuk setiap keberhasilan rutin. Tinjau pengeluaran telemetri Anda secara rutin, karena biaya observabilitas tak terkelola dapat menyaingi infrastruktur yang diamatinya.

## Trade-off: kelebihan dan kekurangan

| Keputusan | Kelebihan | Kekurangan |
|---|---|---|
| Peristiwa kardinalitas tinggi | Debugging kuat, tanyakan apa saja | Biaya penyimpanan dan kueri lebih tinggi |
| Sampling agresif | Biaya lebih rendah, derau lebih sedikit | Dapat melewatkan peristiwa langka |
| Peringatan berbasis gejala | Panggilan lebih sedikit dan dapat ditindaklanjuti | Membutuhkan SLO baik agar berfungsi |
| Standar OpenTelemetry | Netral vendor, portabel | Upaya migrasi, perkakas masih matang |
| Retensi log panjang | Forensik dan audit lebih baik | Biaya penyimpanan, paparan privasi |

Keputusan observabilitas bermuara pada ketegangan antara fidelitas dan biaya. Menangkap segalanya pada resolusi penuh memberi Anda pandangan belakang sempurna, tetapi pada skala besar sangat mahal. Memotong agresif menghemat uang, tetapi Anda mungkin membuang satu catatan yang akan menjelaskan pemadaman. Sampling dan tingkatan retensi adalah cara tim matang menapaki garis ini, menyimpan galat dan pencilan sambil menipiskan data rutin. Trade-off peringatan antara sensitivitas dan derau: terlalu banyak peringatan menyebabkan kelelahan dan insiden terlewat, terlalu sedikit membiarkan masalah membusuk. Peringatan berbasis gejala yang digerakkan SLO menyelesaikan sebagian besar ini, tetapi hanya jika Anda punya SLO bermakna.

## Pertanyaan untuk didiskusikan dengan tim Anda

1. **Apa rencana Anda memindahkan layanan warisan ke OpenTelemetry, dan bagaimana Anda menghindari membayar dua tumpukan instrumentasi selama transisi?** Instrumentasi netral vendor adalah properti yang memungkinkan Anda berganti backend tanpa menginstrumentasi ulang ratusan layanan, dan ia paling penting untuk sistem enterprise dan pemerintah berumur panjang yang melampaui kontrak vendor mana pun. Migrasi adalah tempat niat baik macet: properti yang setengah terinstrumentasi meninggalkan celah persis di mana permintaan melintas dari layanan baru ke lama, mematahkan trace ujung ke ujung. Bawa inventaris ke diskusi: layanan mana yang memancarkan data agen proprietari, mana yang memancarkan OpenTelemetry, dan di mana konteks trace dijatuhkan di batas. Putuskan urutan yang mengikuti jalur permintaan nyata alih-alih bagan organisasi, dan anggarkan untuk jendela di mana Anda menjalankan kedua kolektor. Jawabannya menentukan apakah Anda benar-benar memiliki telemetri Anda atau tetap terkunci pada agen satu vendor.

2. **Kapan terakhir Anda mengaudit setiap peringatan untuk kemampuan ditindaklanjuti, dan berapa panggilan bulan lalu yang tidak membutuhkan tindakan manusia?** Kelelahan peringatan adalah penyebab utama insiden nyata yang terlewat dan kelelahan on-call, jadi panggilan yang tak membutuhkan tindakan bukan derau tak berbahaya, ia aktif mengikis respons yang Anda andalkan. Bawa buktinya: tarik panggilan bulan lalu, tandai masing-masing ditindaklanjuti atau diabaikan, dan hitung berapa yang terpetakan ke runbook. Bagi tim besar yang mencakup banyak layanan, peringatan berisik dari satu tim membuat on-call bersama mati rasa bagi semua orang. Tetapkan standar bahwa setiap panggilan terhubung ke runbook dan terikat pada burn rate SLO, lalu hapus sisanya tanpa ampun. Hasil audit ini harus langsung memangkas volume panggilan Anda dan memberi tahu layanan mana yang tak punya SLO bermakna di balik peringatannya.

3. **Apa strategi sampling trace Anda, dan seberapa yakin Anda bahwa ia menyimpan galat dan ekor lambat?** Volume telemetri tumbuh bersama sistem dan biaya observabilitas tak terkelola dapat menyaingi infrastruktur yang diamatinya, jadi Anda akan melakukan sampling, dan pertanyaannya apakah Anda melakukan sampling secara cerdas. Melucuti kardinalitas atau melakukan sampling secara buta menghilangkan persis catatan yang dibutuhkan untuk men-debug masalah sempit yang mengenai satu pelanggan, satu wilayah, atau satu versi API. Bawa tingkatan retensi dan aturan sampling Anda saat ini: apakah Anda condong ke menyimpan galat dan permintaan lambat, memakai trace tertaut exemplar agar lonjakan metrik mengarah ke permintaan lambat yang representatif? Untuk sistem teraudit dan terikat privasi, rekonsiliasikan retensi dengan aturan minimisasi data agar Anda tidak menimbun data pribadi untuk men-debug. Jawabannya menetapkan di mana Anda membelanjakan anggaran telemetri dan apakah pemadaman keras berikutnya dapat dijelaskan atau menjadi misteri.

4. **SLO Anda yang mana adalah komitmen perjalanan pengguna nyata, dan mana metrik proksi yang tak dipercaya siapa pun di luar tim pemiliknya?** Peringatan berbasis gejala hanya berfungsi ketika gejala terpetakan ke hal yang benar-benar dirasakan pengguna, sehingga peringatan yang dikaitkan pada ambang CPU atau target ketersediaan karangan memanggil orang untuk masalah yang mungkin tak penting sambil diam pada yang penting. Bagi organisasi besar, SLO juga kontrak yang memungkinkan tim independen berbagi rotasi on-call tanpa mendebat ulang keparahan selama setiap insiden. Bawa katalog SLO saat ini, perjalanan pengguna yang dimaksudkan dilindungi setiap tujuan, dan pelanggaran kuartal lalu beserta apakah pelanggan benar-benar mengeluh. Dalam pengaturan enterprise dan pemerintah, kaitkan SLO paling terlihat dengan komitmen kinerja terbitan yang dipegang layanan, agar sinyal burn-rate yang sama yang memanggil insinyur juga bukti yang Anda tunjukkan kepada regulator atau badan pengawas. Diskusi harus memensiunkan metrik proksi dan meninggalkan Anda daftar pendek tujuan yang dikenali non-insinyur sebagai janji kepada pengguna.

5. **Siapa yang memiliki tata kelola data telemetri, dan dapatkah Anda membuktikan data pribadi disunting sebelum mendarat di backend observabilitas Anda?** Peristiwa kardinalitas tinggi dan retensi log panjang adalah persis fitur yang membuat debugging mungkin, dan persis yang mengubah penyimpanan observabilitas menjadi salinan data pribadi pengguna Anda yang tak dikelola. Tarikan yang bersaing nyata: insinyur menginginkan atribut lebih kaya dan retensi lebih panjang, sementara privasi dan hukum menginginkan minimisasi data dan umur pendek. Bawa peta aliran data yang menunjukkan bidang mana membawa data pribadi atau sensitif, di mana penyuntingan atau tokenisasi terjadi dalam pipeline, dan tingkatan retensi Anda per kelas data. Untuk sistem teregulasi dan publik, namai pemilik akuntabel, petakan retensi ke dasar hukum dan aturan minimisasi data yang Anda operasikan, dan bersiaplah menunjukkan kepada auditor bahwa akses ke telemetri itu sendiri dicatat dan dikendalikan. Jawabannya memutuskan apakah platform observabilitas Anda aset atau pelanggaran tetap yang menunggu ditemukan.

6. **Ketika insiden melintasi layanan beberapa tim, apakah telemetri Anda memungkinkan satu penanggap mengikuti permintaan ujung ke ujung, atau jejak patah di setiap batas kepemilikan?** Seluruh janji telemetri berkorelasi dengan ID terpropagasi adalah bahwa satu insinyur dapat bernalar tentang sistem yang tak sepenuhnya dimiliki siapa pun, dan janji itu runtuh persis di batas di mana konteks trace dijatuhkan atau di mana dua tim memakai pengenal dan perkakas yang tidak kompatibel. Timbang tarikan menuju otonomi per tim dalam memilih perkakas observabilitas terhadap biaya bersama properti terfragmentasi di mana setiap serah terima adalah jalan buntu selama pemadaman. Bawa linimasa insiden lintas tim terbaru dan tandai di mana penanggap kehilangan benang, plus inventaris layanan mana yang mempropagasi ID korelasi umum dan mana yang tidak. Untuk enterprise besar atau platform pemerintah yang dirakit dari banyak vendor dan sistem berumur panjang, putuskan seberapa banyak yang Anda wajibkan secara terpusat, standar konteks trace bersama dan skema ID umum, versus apa yang Anda serahkan kepada tim, karena komponen yang Anda beli ulang selama puluhan tahun masih harus berinteroperasi pada permintaan yang sama. Jawabannya memberi tahu apakah insiden multitim berikutnya adalah investigasi terkoordinasi atau babak saling tuding.

## Lensa sektor

**Startup.** Dengan segelintir layanan dan tanpa tangan cadangan, instrumentasi dengan OpenTelemetry sejak hari pertama dan kirim log JSON terstruktur yang membawa satu ID permintaan ujung ke ujung. Investasi kecil itu mengubah "aplikasinya lambat" menjadi trace yang dapat Anda baca, dan menjaga Anda bebas berpindah dari tingkat gratis ke backend berbayar kelak tanpa menginstrumentasi ulang. Lewati dasbor rumit dan mesin SLO sampai Anda punya pengguna yang pengalamannya benar-benar dapat Anda ukur.

**Bisnis kecil.** Anda tidak punya spesialis observabilitas dan anggaran ketat, jadi bersandarlah pada backend terkelola di mana instrumentasi, penyimpanan, dan dasbor datang terbundel alih-alih merakit tumpukan sendiri. Keputusan beli-versus-bangun mendukung membeli hampir selalu di sini; perhatian langka Anda lebih baik dihabiskan untuk dua atau tiga peringatan sinyal-emas yang memberi tahu layanan mati daripada menjalankan pipeline telemetri. Tetapkan batas retensi keras agar biaya telemetri tidak diam-diam melampaui infrastruktur yang diawasinya.

**Enterprise.** Pekerjaannya tata kelola lintas banyak tim: standar OpenTelemetry bersama, skema ID korelasi umum, dan dasbor SLO terkurasi agar satu penanggap dapat mengikuti permintaan melintasi puluhan layanan. Kelola telemetri sebagai pusat biaya dengan tingkatan retensi dan kebijakan sampling, bakukan peringatan pada burn rate SLO untuk menjaga on-call bersama berkelanjutan, dan pangkas peringatan berisik secara terpusat agar kelelahan satu tim tidak membuat semua orang mati rasa. Perlakukan lapisan instrumentasi sebagai infrastruktur netral vendor yang melampaui kontrak backend mana pun.

**Pemerintah.** Aturan pengadaan, transparansi, dan akuntabilitas publik membentuk desain. Bakukan pada instrumentasi terbuka agar sistem yang diharapkan berjalan puluhan tahun selamat dari pengadaan ulang oleh vendor berbeda tanpa disandera agen proprietari, dan wajibkan portabilitas itu dalam kontrak. Pakai log audit terstruktur untuk menunjukkan siapa mengakses catatan mana dan kapan, sunting atau tokenisasi data pribadi sebelum mencapai penyimpanan telemetri, dan rekonsiliasikan retensi dengan hukum minimisasi data. Terbitkan dasbor SLO untuk layanan menghadap warga agar sinyal yang sama yang diawasi insinyur Anda menjadi bukti terlihat dari komitmen yang Anda pegang.

## Contoh

**Startup.** Startup empat orang mengirim backend seluler dan terus menerima keluhan samar "aplikasinya lambat" yang tak dapat direproduksinya. Tim menambah OpenTelemetry ke segelintir layanannya dan beralih ke log JSON terstruktur dengan ID permintaan yang dibawa dari aplikasi melalui setiap lompatan. Laporan lambat berikutnya terselesaikan dalam menit: satu trace menunjukkan indeks basis data yang hilang pada tabel pesanan di bawah kueri tertentu. Karena memilih instrumentasi terbuka sejak awal, mereka kelak berpindah dari tingkat gratis ke backend berbayar tanpa menginstrumentasi ulang apa pun.

**Enterprise.** Sebuah platform e-commerce besar menginstrumentasi setiap layanan dengan OpenTelemetry, mempropagasi ID trace dari browser pelanggan melalui checkout, pembayaran, inventaris, dan pengiriman. Ketika konversi turun, insinyur on-call memulai dari peringatan burn-rate SLO, membuka sinyal emas dasbor checkout, melihat latensi meningkat di satu wilayah, dan mengikuti trace exemplar ke panggilan basis data lambat di satu layanan. Atribut kardinalitas tinggi menunjukkan masalah terbatas pada satu kategori produk, yang memandu perbaikan terarah dalam menit alih-alih jam.

**Pemerintah.** Sebuah layanan kesehatan nasional menjalankan platform catatan pasien di bawah aturan audit dan privasi ketat. Log terstruktur menangkap siapa mengakses catatan mana dan kapan, memberi makan pemantauan keamanan dan pelaporan kepatuhan, sementara bidang yang dapat mengidentifikasi pribadi disunting atau ditokenisasi dalam telemetri. Dasbor SLO publik menunjukkan ketersediaan dan latensi untuk pemesanan janji temu menghadap warga. Dengan membakukan pada instrumentasi terbuka, lembaga menghindari lock-in proprietari di sistem yang diharapkan berjalan puluhan tahun dan dibeli ulang oleh vendor berbeda selama hidupnya.

## Kasus bisnis: motivasi, ROI, dan TCO

Imbal hasil utama observabilitas adalah penurunan dramatis waktu untuk mendeteksi dan menyelesaikan insiden. Untuk layanan di mana downtime mahal, memangkas mean time to resolution dari jam menjadi menit membayar perkakas berkali-kali lipat dalam satu insiden besar. Observabilitas juga menghemat waktu rekayasa yang kalau tidak dihabiskan menebak, mereproduksi bug, dan berdebat tim mana yang bersalah, dan ia mempersingkat loop umpan balik yang memungkinkan tim mengirim dengan percaya diri. Nilai keamanan dan kepatuhan juga nyata: telemetri yang sama mendukung deteksi intrusi dan bukti audit.

Total biaya kepemilikan mencakup upaya instrumentasi, biaya penyimpanan dan kueri telemetri, dan disiplin mengkurasi sinyal dari derau. Biaya ini terlihat dan berulang, yang menggoda pimpinan untuk kurang berinvestasi. Biaya tidak mengadopsi lebih besar tetapi lebih sulit dilihat: pemadaman berkepanjangan, masalah kinerja tak terdiagnosis, insiden keamanan ditemukan terlambat atau tak pernah, dan insinyur kelelahan oleh peringatan yang tak dapat mereka lakukan apa-apa. Ajukan kasus dengan data insiden konkret. Tunjukkan waktu penyelesaian dan dampak bisnis pemadaman terbaru, dan proyeksikan pengurangan yang akan dihasilkan telemetri lebih baik. Membingkai observabilitas sebagai asuransi yang juga mempercepat pengiriman, alih-alih pusat biaya murni, memenangkan argumen.

## Anti-pola dan jebakan

- **Peringatan atas segalanya.** Memanggil untuk setiap anomali melatih penanggap mengabaikan peringatan, sehingga insiden nyata lolos.
- **Panggilan berbasis penyebab.** Memberi peringatan atas penyebab internal alih-alih gejala pengguna membanjiri on-call dengan derau dan melewatkan kegagalan baru.
- **Log tak terstruktur.** Log teks bebas yang tak dapat dikueri atau dikorelasikan memaksa grepping manual yang lambat selama insiden.
- **Tiga pilar tersilo.** Metrik, log, dan trace dalam perkakas terputus tanpa ID bersama mencegah mengikuti peristiwa ujung ke ujung.
- **Sebaran dasbor.** Ratusan dasbor tak terkurasi berarti tak ada yang tahu mana yang menunjukkan apakah sistem sehat.
- **Keruntuhan kardinalitas.** Melucuti bidang kardinalitas tinggi untuk menghemat biaya menghilangkan persis data yang dibutuhkan untuk men-debug masalah sempit.
- **Lock-in vendor.** Agen proprietari di mana-mana membuat berganti backend sangat mahal dan menyandera data Anda.

## Model kematangan

**Tingkat 1, Memulai.** Observabilitas ad hoc dan reaktif. Pemeriksaan uptime dasar dan log tak terstruktur hidup di mesin individual, debugging berarti masuk ke server untuk grep, dan tak ada telemetri bersama. Peringatan berisik, berbasis penyebab, dan sering diabaikan, sehingga insiden nyata muncul lewat keluhan pengguna alih-alih sinyal.

**Tingkat 2, Mengembangkan.** Praktik dasar muncul tetapi bervariasi menurut tim. Sebagian layanan mendorong metrik dan log ke tempat pusat, beberapa dasbor dan peringatan ambang ada, tetapi log hanya semi-terstruktur dan trace absen atau parsial. Korelasi lintas layanan manual, dan apakah insinyur dapat mengikuti permintaan ujung ke ujung bergantung pada tim mana yang kebetulan terlibat.

**Tingkat 3, Membakukan.** Instrumentasi didokumentasikan dan ditegakkan di seluruh organisasi. OpenTelemetry di seluruh layanan dengan ID trace atau korelasi terpropagasi, logging terstruktur dengan nama bidang konsisten, tracing terdistribusi, dasbor sinyal-emas terkurasi, dan peringatan gejala berbasis SLO adalah standar yang diikuti setiap tim. Setiap panggilan terhubung ke runbook dan terikat pada SLO, dan on-call berkelanjutan alih-alih sumber kelelahan.

**Tingkat 4, Mengelola.** Properti observabilitas itu sendiri diukur dan dikendalikan terhadap garis dasar. Anda melacak cakupan instrumentasi dan tingkat propagasi konteks trace di seluruh layanan, pangsa panggilan yang ditindaklanjuti versus diabaikan, mean time to detect dan resolve, pencapaian SLO dan burn anggaran galat, dan biaya telemetri per layanan terhadap anggaran. Celah dan derau peringatan ditekan dengan data menuju target eksplisit, fidelitas sampling diverifikasi agar catatan galat dan ekor lambat selamat, dan keputusan go atau no-go atas cakupan dan retensi dibuat atas bukti alih-alih opini.

**Tingkat 5, Mengorkestrasi.** Observabilitas terus diperbaiki dan terintegrasi di seluruh organisasi. Telemetri kaya peristiwa dan kardinalitas tinggi memungkinkan investigasi ad hoc atas irisan mana pun, peringatan digerakkan burn-rate SLO dengan derau minimal, dan sampling serta retensi beradaptasi dengan biaya dan risiko yang berubah. Telemetri memberi makan perencanaan kapasitas, deteksi keamanan, dan keputusan produk secara rutin, dan platform menyetel ulang sinyal, anggaran, dan cakupannya sendiri seiring sistem, gambaran ancaman, dan kewajiban regulasi bergeser.

## Gagasan untuk didiskusikan

- Di mana keseimbangan yang tepat antara fidelitas telemetri dan biaya untuk layanan paling kritis Anda?
- Bagaimana Anda memutuskan apa yang layak mendapat panggilan versus tiket versus hanya entri dasbor?
- Apa strategi Anda mempropagasi ID korelasi lintas tim yang tidak berbagi basis kode atau siklus rilis?
- Bagaimana Anda mempertahankan daya debugging kardinalitas tinggi sambil memenuhi persyaratan privasi dan minimisasi data?
- Haruskah perkakas observabilitas diwajibkan secara terpusat atau dipilih per tim, dan apa konsekuensinya di kedua arah?
- Bagaimana Anda akan mendemonstrasikan kepada auditor bahwa telemetri Anda lengkap dan tahan-rusak?

## Poin-poin utama

- Pemantauan mendeteksi masalah yang diketahui; observabilitas memungkinkan Anda menyelidiki yang tak diketahui tanpa mengirim kode baru.
- Metrik, log, dan trace paling berharga ketika dikorelasikan lewat pengenal bersama, bukan disilokan.
- Bakukan pada OpenTelemetry dan logging terstruktur agar tetap netral vendor dan portabel sepanjang umur sistem yang panjang.
- Beri peringatan atas gejala terlihat pengguna lewat burn rate SLO, jadikan setiap panggilan dapat ditindaklanjuti, dan pangkas derau tanpa henti.
- Kurasi dasbor di sekitar model kesehatan yang jelas seperti sinyal emas alih-alih menampilkan setiap metrik.
- Telemetri kaya peristiwa dan kardinalitas tinggi adalah yang membuat debugging masalah produksi sempit mungkin.

## Referensi dan bacaan lanjutan

- Charity Majors, Liz Fong-Jones, George Miranda, *Observability Engineering: Achieving Production Excellence*
- Cindy Sridharan, *Distributed Systems Observability*
- Betsy Beyer et al., *Site Reliability Engineering* (bab tentang pemantauan dan peringatan)
- Brendan Gregg, *Systems Performance: Enterprise and the Cloud*
- Proyek OpenTelemetry, spesifikasi dan dokumentasi (Cloud Native Computing Foundation)
- Google, *The Four Golden Signals* (Site Reliability Engineering, bab pemantauan)
