# 10.6 Manajemen proyek

## Tinjauan dan motivasi

[Manajemen proyek](https://en.wikipedia.org/wiki/Project_management) adalah disiplin mengubah maksud menjadi hasil terkirim di bawah kendala. Anda mengoordinasikan orang, cakupan, jadwal, biaya, risiko, dan kualitas agar kerja benar-benar selesai dan menyampaikan nilai. Dalam perangkat lunak ia sering diperlakukan dengan kecurigaan, dikaitkan dengan rencana berat dan [bagan Gantt](https://en.wikipedia.org/wiki/Gantt_chart) yang diabaikan kenyataan. Tetapi kebutuhan mendasarnya tak pernah hilang. Seseorang harus memastikan kerja yang tepat terjadi dalam urutan yang tepat, dependensi dikelola, risiko muncul sejak dini, dan [pemangku kepentingan](https://en.wikipedia.org/wiki/Project_stakeholder) tahu apa yang diharapkan. Pertanyaannya bukan *apakah* mengelola proyek, tetapi *seberapa ringan dan adaptif* Anda dapat melakukannya sambil tetap memenuhi kewajiban Anda.

Mengapa memperlakukan ini secara eksplisit? Proyek perangkat lunak gagal pada laju mengkhawatirkan, dan mereka gagal jauh lebih sering karena alasan manajemen daripada alasan murni teknis: cakupan tak jelas, dependensi tak dikelola, risiko tak ditangani, pemangku kepentingan absen, dan fantasi estimasi jangka panjang yang presisi. Program besar terutama terpapar: dengan banyak tim, vendor, dan cakrawala multikuartal, kegagalan koordinasi kecil bertambah. Manajemen proyek yang baik sebagian besar adalah praktik membuat komitmen dengan jujur, memecah kerja secara masuk akal, dan menciptakan umpan balik cepat agar masalah muncul selagi masih murah diperbaiki.

Konteks enterprise dan pemerintah menaikkan taruhan dan mengubah kendala. Enterprise mengelola portofolio inisiatif yang saling mengunci terhadap strategi dan siklus anggaran (bab 10.1). Pemerintah menambah aturan pengadaan, apropriasi multitahun, manajemen kontraktor, dan akuntabilitas publik. Di sana, bawaan historis (kontrak [waterfall](https://en.wikipedia.org/wiki/Waterfall_model) besar dengan cakupan tetap) punya catatan panjang kegagalan mahal dan terlihat. Bab ini membahas dasar-dasar yang berlaku lintas pendekatan prediktif, adaptif, dan hibrida. Bab 10.7 (Agile) mendalami penyampaian adaptif, dan bab 10.1 membahas manajemen portofolio dan program di atas satu proyek.

## Prinsip utama

- **Kelola hasil, bukan aktivitas.** Selesai berarti nilai terkirim, bukan tugas ditutup.
- **Dekomposisi dan urutkan.** Kerja kecil, berurutan, dan sadar-dependensi mengalahkan rencana big-bang.
- **Estimasi adalah rentang, bukan janji.** Komunikasikan ketidakpastian dengan jujur.
- **Munculkan risiko sejak dini dan terus-menerus.** Masalah termurah adalah yang tertangkap pertama.
- **Cocokkan metode dengan kerja.** Prediktif, adaptif, atau hibrida: sesuaikan dengan ketidakpastian dan kendala.
- **Jadikan status transparan.** Aliran yang terlihat mengalahkan laporan menenangkan.
- **Pemangku kepentingan adalah bagian tim.** Ketiadaan pelanggan adalah risiko proyek.

## Rekomendasi

### Pilih prediktif, adaptif, atau hibrida dengan sengaja

Tak ada model penyampaian yang benar secara universal; ada kecocokan antara metode dan konteks:

- **Prediktif (digerakkan rencana, "waterfall"):** cakupan tetap di muka, lalu jadwal dan biaya diturunkan. Cocok untuk kerja dengan persyaratan yang benar-benar stabil dan dipahami baik serta kendala eksternal keras (sertifikasi regulasi, integrasi fisik). Mode kegagalannya berpura-pura persyaratan perangkat lunak stabil padahal tidak.
- **Adaptif ([agile](https://en.wikipedia.org/wiki/Agile_software_development)):** cakupan lentur; waktu dan biaya tetap dalam iterasi pendek yang mengirim perangkat lunak berfungsi dan menyerap pembelajaran. Cocok untuk sebagian besar kerja produk dan layanan digital, di mana persyaratan ditemukan (bab 11.1, 10.7).
- **Hibrida:** inti adaptif di dalam cangkang tata kelola prediktif, lazim dan sering tepat di enterprise dan pemerintah, di mana pendanaan, kepatuhan, dan kontrak menuntut tonggak dan audit sementara penyampaian diuntungkan oleh iterasi.

Kerangka seperti [PMBOK](https://en.wikipedia.org/wiki/Project_Management_Body_of_Knowledge) (Project Management Body of Knowledge, dari [Project Management Institute](https://en.wikipedia.org/wiki/Project_Management_Institute)) dan [PRINCE2](https://en.wikipedia.org/wiki/PRINCE2) (PRojects IN Controlled Environments) mengodifikasi praktik prediktif dan hibrida. Intinya meminjam disiplinnya (peran, risiko, gerbang tahap) tanpa mengimpor upacara yang tak dibutuhkan kerja.

### Kelola cakupan terhadap kendala segitiga tiga

Cakupan, jadwal, dan biaya bergerak bersama, dibatasi oleh kualitas: ["segitiga besi"](https://en.wikipedia.org/wiki/Project_management_triangle) klasik. Anda tak dapat menetapkan ketiganya dan menambah cakupan gratis. Sesuatu mengalah, dan berpura-pura sebaliknya adalah cara [death march](https://en.wikipedia.org/wiki/Death_march_(project_management)) dimulai. Jadikan trade-off eksplisit, dan putuskan variabel *mana* yang lentur. Metode adaptif menetapkan waktu dan biaya dan melenturkan cakupan. Kontrak harga tetap menetapkan cakupan dan biaya, dan dalam kenyataan melenturkan kualitas atau jadwal kecuali Anda mengelolanya. Kendalikan [scope creep](https://en.wikipedia.org/wiki/Scope_creep) dengan proses perubahan ringan (bab 12.3), dan pilih *mengurangi cakupan ke inti berharga* daripada menggeser segalanya.

### Estimasi dengan jujur, dalam rentang, dan perkirakan ulang

Estimasi adalah tempat proyek paling sering membohongi dirinya sendiri. Perlakukan estimasi sebagai rentang probabilistik, bukan angka tunggal, dan lebarkan untuk kerja jauh dan kurang dipahami (["kerucut ketidakpastian"](https://en.wikipedia.org/wiki/Cone_of_Uncertainty)). Pilih metode relatif dan empiris: throughput dan waktu siklus historis (bab 11.2, 11.3) meramalkan lebih baik daripada tebakan bottom-up heroik. Di mana bisa, ganti estimasi dengan *pengukuran*. Tim yang menutup 8 butir/minggu akan memakan sekitar 5 minggu untuk 40 butir, terlepas dari story point ([Hukum Little](https://en.wikipedia.org/wiki/Little%27s_law) lagi: throughput dan kerja dalam proses, bukan estimasi, yang menetapkan waktu pengiriman). Perkirakan ulang terus-menerus seiring kenyataan tiba. Rencana yang tak pernah berubah tidak sedang dikelola.

### Kelola dependensi dan jalur kritis

Pada skala besar, risiko dominan jarang velositas satu tim. Ia *dependensi antara tim dan vendor*. Petakan secara eksplisit, identifikasi [jalur kritis](https://en.wikipedia.org/wiki/Critical_path_method) (urutan yang menentukan selesai paling awal), dan serang dependensi terpanjang dan paling berisiko lebih dulu. Kurangi kopling di mana bisa (dependensi yang dihapus lebih berharga daripada dependensi yang dilacak) dan pakai antarmuka dan kontrak jelas agar tim dapat maju paralel (bab 1.2, 2.3). Untuk program lintas tim, sinkronisasi dependensi dan risiko reguler mengalahkan laporan status yang tak dibaca siapa pun.

### Jalankan register risiko hidup

Manajemen risiko adalah aktivitas manajemen proyek berdaya ungkit tertinggi, dan paling sering dilewati. Simpan **[register risiko](https://en.wikipedia.org/wiki/Risk_register)** hidup yang sederhana: setiap risiko dengan kemungkinan, dampak, pemilik, dan mitigasi atau kontinjensinya (bab 12.3). Tinjau secara rutin, pensiunkan risiko yang telah lewat, dan tambah yang baru seiring muncul. Bedakan risiko (mungkin terjadi) dari isu (sudah terjadi) dan keputusan (bab 1.6). Tujuannya bukan dokumen. Melainkan kebiasaan melihat ke depan, agar Anda mengantisipasi masalah alih-alih menemukannya di tenggat.

### Libatkan pemangku kepentingan dan berkomunikasi secara transparan

Sebagian besar kegagalan proyek "mengejutkan" terlihat sejak dini oleh seseorang yang tidak didengar. Identifikasi pemangku kepentingan, pahami kekhawatiran mereka, dan jaga mereka benar-benar terlibat. Ketiadaan pelanggan sendiri adalah risiko teratas. Komunikasikan status lewat *aliran transparan* (papan terlihat, bagan burn-up, perangkat lunak berfungsi yang didemokan) alih-alih laporan hijau-kuning-merah yang menghargai optimisme. Eskalasi dengan jujur dan dini. Proyek yang dijalankan baik membuat kabar buruk menjalar cepat.

## Trade-off: kelebihan dan kekurangan

| Pendekatan | Kelebihan | Kekurangan |
|---|---|---|
| **Prediktif / waterfall** | Cakupan dan biaya dapat diprediksi; ramah kontrak dan audit | Kurang cocok untuk persyaratan tak pasti; umpan balik terlambat; risiko big-bang |
| **Adaptif / agile** | Umpan balik cepat; menyerap perubahan; nilai dini | Lebih sulit menetapkan cakupan/biaya di muka; butuh pelanggan terlibat |
| **Hibrida** | Iterasi di dalam tata kelola; cocok enterprise/pemerintah | Ketegangan antar irama; dapat mewarisi kedua set overhead |
| **Estimasi di muka terperinci** | Kenyamanan bagi perencana dan pendana | Presisi namun salah; mahal dihasilkan; cepat membusuk |
| **Peramalan empiris (metrik aliran)** | Berlandaskan, mengoreksi diri | Butuh riwayat dan disiplin; tampak kurang "pasti" |
| **Upacara risiko/proses berat** | Menyeluruh; baik untuk program berisiko tinggi | Memperlambat tim kecil; dapat menjadi centang kotak |

Ketegangan sentralnya **keterprediksian versus kemampuan beradaptasi**. Pendana, kontrak, dan audit menginginkan komitmen tegas. Kerja perangkat lunak yang tak pasti butuh ruang untuk belajar. Selesaikan seperti Agile menyelesaikannya (bab 10.7): berkomitmen tegas pada hasil dan tenggat sambil membiarkan cakupan lentur, dan pakai tata kelola hibrida untuk memuaskan pengawasan tanpa membekukan penyampaian.

## Pertanyaan untuk didiskusikan dengan tim Anda

1. **Bagaimana Anda akan membungkus tim penyampaian adaptif dalam cangkang tata kelola prediktif tanpa mewarisi overhead keduanya?** Hibrida lazim dan sering tepat di enterprise dan pemerintah, di mana siklus pendanaan, kepatuhan, dan kontrak menuntut tonggak dan audit sementara penyampaian diuntungkan oleh iterasi. Risikonya nyata: hibrida yang dirancang buruk mewarisi dokumentasi berat waterfall dan upacara agile sekaligus, dan tim merasakan gesekan dua irama yang saling berkelahi. Bawa bukti: petakan di mana gerbang pendanaan, titik pemeriksaan kepatuhan, dan tonggak kontrak Anda sebenarnya jatuh, dan periksa apakah masing-masing menuntut dokumen yang tak dihasilkan kerja penyampaian. Jawabannya harus membiarkan iterasi memuaskan pengawasan alih-alih melawannya, dengan memberi makan kenaikan berfungsi yang didemokan dan register risiko hidup ke irama tata kelola alih-alih berhenti merakit laporan terpisah. Pinjam disiplin kerangka seperti PRINCE2 tanpa mengimpor upacara yang tak dibutuhkan kerja.

2. **Apakah status proyek Anda aliran transparan, atau laporan hijau-kuning-merah yang menghargai optimisme?** Sebagian besar kegagalan mengejutkan terlihat sejak dini oleh seseorang yang tak didengar, dan status semangka (hijau di luar, merah di dalam) adalah cara kabar buruk jujur tetap terkubur sampai tenggat. Ganti laporan menenangkan dengan papan terlihat, bagan burn-up, dan perangkat lunak berfungsi yang didemokan, dan jadikan eskalasi dini tindakan aman alih-alih risiko karier. Bawa bukti: lihat proyek bermasalah terakhir Anda dan tanyakan kapan tanda peringatan pertama ada versus kapan pimpinan mendengarnya. Ketiadaan pelanggan sendiri risiko teratas, jadi periksa apakah pemangku kepentingan terlibat benar-benar dalam lingkaran atau Anda membangun dengan yakin ke arah yang salah. Proyek yang dijalankan baik membuat kabar buruk menjalar cepat, dan perbaikannya budaya sebanyak perkakas.

3. **Apakah Anda tahu inti berharga minimum yang akan Anda kurangi cakupannya jika jadwal dan biaya berhenti bergerak?** Cakupan, jadwal, dan biaya bergerak bersama dibatasi kualitas, dan ketika pendana menetapkan ketiganya, kualitas menjadi katup pelepas senyap dan death march dimulai. Metode adaptif menetapkan waktu dan biaya dan melenturkan cakupan, yang hanya berfungsi jika Anda sudah memutuskan irisan mana yang menyampaikan nilai nyata dan fitur mana yang dapat dinegosiasikan. Bawa bukti: untuk rilis Anda saat ini, dapatkah Anda menamai inti yang harus dikirim dan daftar yang akan Anda potong lebih dulu, atau setiap fitur diam-diam diperlakukan wajib? Jawabannya harus memungkinkan Anda mengurangi cakupan ke inti berharga alih-alih menggeser segalanya, dan harus diselesaikan sebelum tekanan tiba, bukan diimprovisasi di tenggat. Kendalikan sisanya dengan proses perubahan ringan agar scope creep tidak memakan margin yang Anda andalkan.

4. **Dependensi lintas tim mana yang ada di jalur kritis Anda sekarang, dan siapa yang memiliki penghapusan atau pengurangan risikonya?** Pada skala besar ancaman dominan jarang velositas satu tim; ia urutan dependensi antara tim dan vendor yang menetapkan selesai paling awal yang mungkin. Jika tak ada yang dapat menamai dependensi jalur kritis saat ini, Anda mengelola kemajuan lokal sementara hal yang sebenarnya menentukan tanggal Anda melayang tanpa diawasi. Bawa bukti: peta dependensi yang menunjukkan serah terima mana memberi makan mana, di mana rantai terpanjang berjalan, dan tautan mana yang masih belum dibangun atau terblokir secara kontraktual, plus pemilik bernama untuk setiap tautan berisiko. Bidik menyerang dependensi terpanjang dan paling berisiko lebih dulu dan menghapus kopling di mana bisa, karena dependensi yang dihapus lebih berharga daripada dependensi yang dilacak. Dalam program enterprise dan pemerintah, tautan tersulit sering melintasi batas vendor atau lembaga, jadi namai pemilik akuntabel di kedua sisi dan pastikan kontrak memungkinkan mereka bertindak, atau dependensi akan tak terselesaikan sampai menjadi penundaan publik.

5. **Bagaimana Anda memperkirakan ulang seiring kenyataan tiba, dan seberapa cepat penggeseran menjadi terlihat bagi orang yang mendanai kerja?** Rencana yang tak pernah berubah tidak dikelola; ia dibela, dan tanggal angka tunggal yang dibela melampaui bukti adalah cara proyek tergelincir dalam diam sampai tenggat. Ganti estimasi dengan pengukuran di mana bisa, meramalkan dari throughput dan waktu siklus historis alih-alih tebakan bottom-up heroik, dan lebarkan rentang untuk kerja jauh dan kurang dipahami. Bawa bukti: laju penyelesaian mingguan aktual Anda, ukuran backlog saat ini, dan proyeksi selesai yang keluar darinya, dibandingkan dengan tanggal yang saat ini dipercaya pimpinan. Jawabannya harus memberi pendana proyeksi jujur dan menyempit yang mereka lihat setiap siklus alih-alih tanggal tetap yang bertahan sampai runtuh. Di pemerintah dan pengaturan terikat apropriasi lain, perkiraan yang memunculkan penggeseran dini memungkinkan Anda menentukan ulang cakupan atau mengatur ulang garis dasar dalam aturan, sedangkan penggeseran tersembunyi menjadi kegagalan pengawasan dan berita utama.

6. **Apa proses teringan yang masih memenuhi kewajiban sejati Anda, dan di mana upacara terlepas dari mengurangi risiko?** Baik kurang mengelola maupun terlalu mengelola membawa biaya nyata: kekacauan, pengerjaan ulang, dan dependensi terlewat di satu sisi, dan centang kotak yang memperlambat penyampaian tanpa menurunkan risiko di sisi lain. Ketegangannya adalah audit, kepatuhan, dan ketentuan kontrak memaksakan persyaratan nyata, namun tim cenderung menyimpan setiap ritual lama setelah ia berhenti layak tempatnya. Bawa bukti: untuk setiap laporan, gerbang, dan rapat berulang, namai kewajiban atau risiko spesifik yang ditanganinya, dan tandai yang tak dapat ditelusuri siapa pun ke salah satunya. Jawabannya harus memungkinkan Anda memensiunkan upacara yang hanya menghasilkan jaminan sambil mempertahankan artefak yang memuaskan auditor atau pendana nyata. Dalam konteks enterprise dan pemerintah, petakan setiap upacara ke aturan apropriasi, pengadaan, atau regulasi bernama yang dilayaninya, agar Anda dapat membela memotong sisanya kepada pengawasan alih-alih menebak apa yang dituntut kepatuhan.

## Lensa sektor

**Startup.** Kelola dengan nyaris tanpa upacara tetapi disiplin nyata. Pecah rilis menjadi irisan kecil berurutan, berkomitmen pada tanggal peluncuran sambil membiarkan cakupan lentur ke inti berharga, dan kutip rentang kepada para pendiri alih-alih satu tanggal, memperkirakan ulang setiap minggu dari berapa irisan yang benar-benar Anda tutup. Register risiko sepuluh baris di dokumen bersama yang menamai satu dependensi yang dapat menenggelamkan tanggal, dengan pemilik dan fallback, lebih berharga daripada perkakas mana pun, karena sumber daya Anda yang paling langka adalah perhatian dan penggeseran yang Anda lihat terlambat dapat mengakhiri perusahaan.

**Bisnis kecil.** Anda tidak punya manajer proyek dan sedikit kelonggaran, jadi bersandarlah pada perkakas yang sudah Anda jalankan alih-alih mendirikan kantor tata kelola. Lacak kerja di satu papan terlihat, simpan daftar risiko hidup singkat, dan pilih membeli produk penjadwalan atau tiket daripada membangun proses dari nol. Putuskan di muka fitur tunggal mana yang harus dikirim agar rilis layak dikerjakan, karena ketika jadwal mengetat Anda tak akan punya orang cadangan untuk menegosiasikan cakupan pada saat itu.

**Enterprise.** Masalahnya koordinasi lintas banyak tim, vendor, dan siklus pendanaan. Bungkus tim adaptif dalam cangkang tata kelola prediktif, beri makan kenaikan yang didemokan dan register risiko hidup ke irama tonggak alih-alih merakit laporan terpisah, dan pelihara peta dependensi lintas tim agar jalur kritis dikelola alih-alih ditemukan. Bakukan estimasi berbasis rentang dan diperkirakan ulang secara empiris di seluruh portofolio agar pimpinan membandingkan proyek pada proyeksi jujur dan menyempit alih-alih tanggal tetap optimistis.

**Pemerintah.** Aturan pengadaan, apropriasi multitahun, dan akuntabilitas publik membentuk setiap pilihan. Pilih kenaikan modular berbasis hasil yang disampaikan secara adaptif di bawah kerangka tata kelola yang memuaskan apropriasi dan pengawasan, daripada satu kontrak waterfall harga tetap, cakupan tetap dengan go-live yang jauh. Register risiko hidup dan kenaikan transparan yang didemokan memberi auditor dan legislator visibilitas nyata, dan melenturkan cakupan ke inti berharga dalam pendanaan tetap memungkinkan Anda mengirim kapabilitas berguna lebih awal alih-alih mempertaruhkan segalanya pada satu tanggal.

## Contoh

**Startup.** Startup tujuh orang yang berpacu mengirim produk berbayar pertamanya mengelola proyek dengan nyaris tanpa upacara tetapi disiplin nyata. Ia memecah rilis menjadi irisan kecil berurutan, berkomitmen pada tanggal peluncuran sambil membiarkan cakupan lentur ke inti berharga alih-alih menjanjikan setiap fitur, dan mengutip rentang kepada para pendiri alih-alih satu tanggal, memperkirakan ulang setiap minggu dari berapa irisan yang benar-benar ditutup tim. Register risiko sepuluh baris di dokumen bersama menamai satu dependensi yang dapat menenggelamkan tanggal, integrasi pembayaran yang belum selesai, dengan pemilik dan fallback, sehingga ancaman terbesar diawasi alih-alih ditemukan di tenggat.

**Enterprise.** Sebuah bank yang mengganti platform asal-usul pinjamannya menjalankan program hibrida: cangkang prediktif dengan tonggak pendanaan kuartalan dan gerbang kepatuhan, membungkus tim adaptif yang mengirim kenaikan berfungsi setiap dua minggu. Peta dependensi lintas tim mengungkap bahwa layanan identitas bersama ada di jalur kritis. Maka program mengurutkannya lebih dulu dan mengurangi risikonya, menghindari kaskade terlambat. Estimasi diekspresikan sebagai rentang dan diperkirakan ulang bulanan dari throughput aktual, sehingga pimpinan melihat proyeksi jujur dan menyempit alih-alih tanggal tetap yang diam-diam tergelincir.

**Pemerintah.** Sebuah lembaga meninggalkan satu kontrak waterfall harga tetap, cakupan tetap (pola di balik beberapa kegagalan publik) demi pengadaan modular: kenaikan lebih kecil berbasis hasil yang disampaikan secara adaptif di bawah kerangka tata kelola yang memuaskan apropriasi dan pengawasan. Register risiko hidup dan kenaikan transparan yang didemokan memberi auditor dan legislator visibilitas nyata. Karena cakupan lentur ke inti berharga dalam pendanaan tetap, program dapat mengirim kapabilitas berguna lebih awal alih-alih mempertaruhkan segalanya pada satu go-live yang jauh (bab 10.1, 10.3).

## Kasus bisnis: motivasi, ROI, dan TCO

Imbal hasil manajemen proyek yang baik didominasi **kegagalan yang dihindari**. Proyek perangkat lunak besar jauh lebih mungkin terlambat, melebihi anggaran, atau dibatalkan daripada mencapai rencana tetap awalnya, dan kerugiannya sangat besar: biaya tenggelam, plus nilai yang hilang, plus, di pemerintah, kerusakan publik dan politik. Disiplin di sini (estimasi jujur, manajemen dependensi, kerja risiko dini, pemangku kepentingan terlibat, dan cakupan adaptif) persis yang menggeser proyek dari kurva kegagalan. Bahkan pengurangan sederhana dalam kemungkinan pelampauan besar atau pembatalan melampaui biaya mengelola proyek dengan baik.

Pada **total biaya kepemilikan**, manajemen adaptif yang ringan menurunkan biaya sepanjang umur kerja. Umpan balik cepat menangkap kesalahan mahal sejak dini. Penyampaian inkremental mulai mengembalikan nilai lebih cepat, yang memperbaiki waktu ROI. Aliran transparan mengurangi overhead pelaporan yang dipaksakan tata kelola berat. Baik *kurang* mengelola (kekacauan, pengerjaan ulang, dependensi terlewat) maupun *terlalu* mengelola (upacara yang memperlambat penyampaian) membawa biaya nyata. Tujuannya proses teringan yang memenuhi kewajiban aktual Anda. Ajukan kasus kepada pimpinan dengan mengontraskan biaya terbebani penuh proyek bermasalah terbaru dengan biaya nyaris nol dari register risiko, peta dependensi, dan perkiraan berbasis rentang yang jujur.

## Anti-pola dan jebakan

- **Rencana tetap-semuanya:** cakupan, jadwal, dan biaya semuanya terkunci, dengan kualitas sebagai katup pelepas senyap.
- **Estimasi sebagai janji:** tanggal angka tunggal diperlakukan sebagai komitmen, lalu dibela melampaui bukti.
- **Mengabaikan dependensi:** mengelola velositas tiap tim sementara jalur kritis lintas tim tergelincir.
- **Teater register risiko:** dokumen yang dibuat sekali dan tak pernah ditinjau ulang.
- **Status semangka:** hijau di luar, merah di dalam; optimisme dihargai di atas kejujuran.
- **Pelanggan absen:** tanpa pemangku kepentingan terlibat, sehingga hal yang salah dibangun dengan yakin.
- **Penyampaian big-bang:** semuanya diintegrasikan dan dirilis di akhir, memaksimalkan risiko (kontraskan bab 11.2).
- **Proses demi proses:** upacara dan laporan yang menyita upaya tanpa mengurangi risiko.

## Model kematangan

- **Tingkat 1 (Memulai):** Proyek berjalan dengan kepahlawanan dan harapan; cakupan, risiko, dan dependensi dikelola ad hoc jika sama sekali; estimasi adalah angka tunggal yang dibela melampaui bukti; kejutan tiba di tenggat.
- **Tingkat 2 (Mengembangkan):** Perencanaan dasar, pelaporan status, dan daftar risiko ada pada sebagian proyek tetapi tidak yang lain; metode penyampaian dipilih berdasarkan kebiasaan alih-alih kecocokan; estimasi dan pelacakan dependensi bervariasi tim demi tim, sehingga praktik tidak konsisten di seluruh organisasi.
- **Tingkat 3 (Membakukan):** Pendekatan terdokumentasi ditegakkan di seluruh organisasi: metode penyampaian dipilih agar cocok dengan kerja, cakupan dikelola terhadap kendala segitiga tiga, register risiko hidup dan peta dependensi diharapkan pada setiap proyek, dan estimasi berbasis rentang dan diperkirakan ulang dengan pemangku kepentingan terlibat.
- **Tingkat 4 (Mengelola):** Penyampaian diukur dan dikendalikan terhadap garis dasar. Throughput, waktu siklus, akurasi perkiraan, laju penutupan dependensi dan risiko, serta varians jadwal dan biaya dilacak per proyek dan digulirkan di seluruh portofolio; proyeksi empiris dan menyempit; penggeseran muncul dini dan memicu penentuan ulang cakupan atau pengaturan ulang garis dasar atas bukti alih-alih optimisme.
- **Tingkat 5 (Mengorkestrasi):** Manajemen proyek terintegrasi dengan perencanaan portofolio, pendanaan, dan risiko serta terus diperbaiki. Tata kelola hibrida memuaskan pengawasan tanpa memperlambat penyampaian, dependensi lintas tim dan lintas vendor dikelola proaktif, retrospektif memberi makan perubahan terukur kembali ke praktik, dan organisasi menyesuaikan metodenya serta menyeimbangkan ulang kerja seiring kendala dan prioritas bergeser.

## Gagasan untuk didiskusikan

1. Metode penyampaian mana (prediktif, adaptif, hibrida) yang benar-benar dibutuhkan setiap inisiatif Anda saat ini, dan apakah cocok dengan yang Anda pakai?
2. Ketika terakhir Anda berkomitmen pada tanggal, apakah itu rentang atau angka tunggal, dan bagaimana itu membentuk ekspektasi?
3. Apa dependensi jalur kritis lintas tim Anda sekarang, dan siapa yang memiliki pengurangan risikonya?
4. Apakah register risiko Anda kebiasaan hidup atau dokumen sekali jalan?
5. Di mana kualitas diam-diam menyerap tekanan ketika cakupan, jadwal, dan biaya semuanya tetap?
6. Bagaimana perkiraan Anda akan berubah jika Anda mengganti estimasi dengan throughput terukur?

## Poin-poin utama

- Manajemen proyek mengubah maksud menjadi hasil terkirim di bawah kendala cakupan-jadwal-biaya-kualitas.
- **Cocokkan metode dengan kerja:** prediktif, adaptif, atau hibrida, dan pilih tata kelola hibrida di enterprise/pemerintah.
- Perlakukan **estimasi sebagai rentang**, perkirakan ulang dari **metrik aliran empiris**, dan jangan biarkan tanggal angka tunggal menjadi kebohongan.
- **Dependensi dan risiko** adalah mode kegagalan dominan pada skala besar: petakan dan kelola keduanya terus-menerus.
- Jaga **pemangku kepentingan terlibat** dan status **transparan**; buat kabar buruk menjalar cepat.
- ROI-nya kegagalan yang dihindari; proses teringan yang memenuhi kewajiban Anda menang. Lihat bab 10.7 (Agile), 10.1 (manajemen portofolio dan program), 11.2 (penyampaian), dan 11.3 (teori antrean).

## Referensi dan bacaan lanjutan

- Project Management Institute, *A Guide to the Project Management Body of Knowledge (PMBOK Guide)*.
- AXELOS, *Managing Successful Projects with PRINCE2*.
- Frederick Brooks, *The Mythical Man-Month* (mengapa menambah orang pada proyek terlambat membuatnya lebih terlambat).
- Tom DeMarco dan Timothy Lister, *Peopleware* dan *Waltzing with Bears* (manajemen risiko).
- Steve McConnell, *Software Estimation: Demystifying the Black Art*.
- Daniel Vacanti, *Actionable Agile Metrics for Predictability* (peramalan empiris).
- Standish Group, *CHAOS Report* (hasil proyek perangkat lunak, dibaca secara kritis).
- U.S. Digital Service, *Digital Services Playbook*; UK Government, *Government Service Standard* (penyampaian sektor publik modern).
- Bent Flyvbjerg dan Dan Gardner, *How Big Things Get Done* (penyampaian megaproyek).
