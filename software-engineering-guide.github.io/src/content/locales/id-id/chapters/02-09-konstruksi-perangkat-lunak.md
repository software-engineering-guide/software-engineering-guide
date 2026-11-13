# 2.9 Konstruksi perangkat lunak

## Tinjauan dan motivasi

[Konstruksi perangkat lunak](https://en.wikipedia.org/wiki/Software_construction) adalah tempat desain menjadi kode yang berjalan. Ini pekerjaan terperinci dari pengodean, verifikasi, [pengujian unit](https://en.wikipedia.org/wiki/Unit_testing), [pengujian integrasi](https://en.wikipedia.org/wiki/Integration_testing), dan [debugging](https://en.wikipedia.org/wiki/Debugging). Panduan [Software Engineering Body of Knowledge](https://en.wikipedia.org/wiki/Software_Engineering_Body_of_Knowledge) (SWEBOK) memperlakukan konstruksi sebagai area pengetahuan tersendiri, dan dengan alasan yang baik: di sinilah sebagian besar pekerjaan harian Anda terjadi. Pilihan yang Anda buat baris demi baris (bagaimana Anda menahan kompleksitas, bagaimana Anda menangani galat, seberapa terbaca Anda meninggalkan sesuatu) menentukan apakah sebuah sistem dapat dipahami, diubah, dan dipercaya selama bertahun-tahun mendatang.

Pada tim besar, konstruksi adalah upaya kelompok, bukan solo. Ratusan insinyur menulis ke dalam basis kode bersama yang akan hidup lebih lama daripada masa kerja siapa pun di tim. Jadi standarnya bukan "apakah berfungsi di mesin saya hari ini." Melainkan "dapatkah orang asing mengubah ini dengan aman lima tahun lagi." Konstruksi terhubung ke atas dengan persyaratan (bab 2.8) dan desain (bab 2.2), yang memberi tahu Anda apa yang dibangun dan bentuknya. Ia terhubung ke samping dengan standar pengodean (bab 2.1), pengujian (bab 2.4), dan tinjauan kode (bab 2.5), yang membentuk bagaimana pekerjaan diekspresikan, diverifikasi, dan diperiksa. Konstruksi yang baik mengubah desain yang sehat menjadi aset yang dapat dipelihara. Konstruksi yang buruk mengubah bahkan desain yang baik menjadi liabilitas.

Dalam konteks enterprise dan pemerintah, konstruksi membawa bobot ekstra. Sistem ini berumur panjang, sangat diatur, dan sering kritis bagi keselamatan atau warga. [Pengodean defensif](https://en.wikipedia.org/wiki/Defensive_programming), penanganan galat yang disiplin, dan kode yang jelas benar bukan kemewahan di sini; mereka adalah persyaratan untuk jaminan, audit, dan kesinambungan melintasi puluhan tahun dan pergantian staf. Tujuannya adalah kode yang mengomunikasikan maksudnya, menolak kegagalan, dan dapat diverifikasi. Kode yang sekadar berjalan tidak cukup.

## Prinsip utama

- Minimalkan kompleksitas di atas segalanya; musuh utama konstruksi berskala besar adalah kode yang tak dapat dipahami sepenuhnya oleh siapa pun.
- Antisipasi perubahan; bangun agar modifikasi masa depan yang mungkin terjadi bersifat lokal dan murah.
- Bangun untuk verifikasi; tulis kode yang kebenarannya mudah diperiksa lewat tes, tinjauan, dan penalaran.
- Pakai ulang dengan sengaja; bangun di atas komponen tepercaya yang ada alih-alih menciptakan ulang, tetapi hindari kopling ke abstraksi yang salah.
- Ikuti standar; konsistensi di seluruh basis kode mengurangi biaya kognitif setiap perubahan mendatang.
- Tangani galat dan keadaan tidak valid secara eksplisit; buat mode kegagalan terlihat alih-alih diam.
- Jaga kode tetap terbaca; konstruksi adalah komunikasi dengan pemelihara masa depan lebih dulu dan kompiler kedua.

## Rekomendasi

### Minimalkan kompleksitas sebagai disiplin utama

Jadikan pengurangan kompleksitas, baik esensial maupun aksidental, tujuan sentral Anda. Tulis fungsi dan modul kecil berfungsi tunggal. Pilih nama yang jelas daripada trik cerdik. Jaga nesting tetap dangkal dan alur kendali linier. Lokalkan keputusan agar memahami satu potong kode tidak memaksa Anda memegang seluruh sistem di kepala. Kompleksitas adalah yang membuat basis kode besar lambat diubah dan berbahaya disentuh, jadi timbang setiap pilihan berdasarkan apakah ia menambah kompleksitas atau menghilangkannya. Terapkan prinsip desain di bab 2.2 pada skala kecil juga: kohesi tinggi, kopling rendah, dan [pemisahan perhatian](https://en.wikipedia.org/wiki/Separation_of_concerns) yang jelas sama pentingnya dalam satu fungsi seperti dalam satu arsitektur.

### Bangun untuk perubahan dan untuk verifikasi

Pikirkan ke depan tentang perubahan yang paling mungkin datang (aturan bisnis baru, integrasi baru, regulasi baru) dan isolasi di balik antarmuka stabil agar perubahan tetap lokal. Pada saat yang sama, tulis kode yang mudah diverifikasi: [fungsi murni](https://en.wikipedia.org/wiki/Pure_function) (masukan sama selalu menghasilkan keluaran sama, tanpa efek samping) di tempat Anda bisa, status tersembunyi minimal, dan dependensi dibuat eksplisit agar tes dapat menggantinya. Kode yang sulit diuji biasanya kode yang sulit dipahami dan diubah. Kemampuan diuji (bab 2.4) adalah sinyal desain, bukan sekadar urusan QA.

### Pakai ulang dengan sengaja dan bakukan

Raih pustaka dan komponen internal yang terpelihara baik dan tepercaya sebelum menulis ulang logika fondasional, dan gunakan lewat antarmuka yang jelas (bab 2.3). Bangun komponen yang dapat dipakai ulang hanya ketika kasus penggunaan kedua yang sejati ada, karena menggeneralisasi terlalu dini adalah bentuk kompleksitasnya sendiri. Terapkan standar pengodean dan gaya organisasi Anda (bab 2.1) secara seragam, idealnya ditegakkan oleh formatter dan [linter](https://en.wikipedia.org/wiki/Lint_(software)) otomatis, agar seluruh basis kode terbaca seolah satu penulis cermat yang menulisnya.

### Praktikkan pemrograman defensif dengan penilaian

Validasi masukan pada batas kepercayaan (permintaan eksternal, I/O berkas dan jaringan, masukan pengguna) dan perlakukan data apa pun yang melintasi batas itu sebagai bermusuhan sampai terbukti sebaliknya. Di dalam modul yang teruji baik, jangan selimuti setiap baris dengan pemeriksaan redundan yang menyembunyikan logika dan menekan kegagalan nyata. Aturannya sederhana: bertahan di batas, percaya di dalamnya. Gunakan [asersi](https://en.wikipedia.org/wiki/Assertion_(software_development)) untuk mendokumentasikan dan menegakkan invarian yang tidak pernah boleh salah dalam program yang benar. Gunakan [exception](https://en.wikipedia.org/wiki/Exception_handling) dan penanganan galat untuk kondisi yang sah dapat terjadi saat runtime. Pisahkan keduanya: asersi menjaga asumsi programmer, penanganan galat mengelola kegagalan yang diharapkan.

### Tangani galat secara eksplisit dan gagal dengan aman

Untuk setiap galat, putuskan dengan sengaja apa yang dilakukan: pulih, coba ulang, teruskan, atau gagal cepat. Jangan pernah menelan exception secara diam-diam atau mengabaikan galat yang dikembalikan; kegagalan yang ditekan kembali sebagai cacat misterius kemudian. Pertahankan konteks dalam pesan galat dan log Anda agar kegagalan dapat didiagnosis. Dalam sistem kritis keselamatan dan warga, gagal ke keadaan aman yang dikenal alih-alih melanjutkan dalam keadaan rusak. Beri jalur galat sama banyak pemikiran seperti jalur bahagia, karena di produksi jalur galat adalah tempat kepercayaan dimenangkan atau hilang.

### Bangun kualitas selama konstruksi

Kualitas dibangun masuk, bukan diperiksa masuk sesudahnya. Tulis tes unit bersamaan dengan kode, jalankan [analisis statis](https://en.wikipedia.org/wiki/Static_program_analysis) dan linter terus-menerus, dan jaga fungsi cukup kecil untuk dinalar. Gunakan nama dan struktur yang menjelaskan diri sendiri agar komentar Anda dapat menjelaskan mengapa, bukan apa. [Refaktor](https://en.wikipedia.org/wiki/Code_refactoring) selagi jalan untuk menjaga kode tetap layak huni. Tinjauan kode (bab 2.5) adalah penopang manusia, tetapi sebagian besar kualitas perlu ada sebelum tinjauan bahkan dimulai.

### Pilih dan bakukan perkakas konstruksi

Bakukan toolchain (kompiler, sistem build, formatter, linter, penganalisis statis, debugger, pengelola dependensi, dan konfigurasi IDE) agar setiap insinyur bekerja di lingkungan yang konsisten dan dapat direproduksi. Pasang perkakas ini ke pipeline agar pemeriksaan kualitas tidak opsional. Bawa masuk perkakas pengodean berbantuan AI dengan sengaja, dan perlakukan keluarannya sebagai draf yang harus lolos standar, tinjauan, dan tes yang sama seperti kode lain.

## Trade-off: kelebihan dan kekurangan

| Praktik | Kelebihan | Kekurangan |
|---|---|---|
| Minimalisasi kompleksitas agresif | Terbaca, dapat diubah, tingkat cacat rendah | Bisa terasa lambat; berisiko abstraksi berlebihan bila disalahterapkan |
| Pemeriksaan defensif ekstensif | Menangkap keadaan buruk lebih awal, batas kokoh | Mengotori logika; bisa menutupi bug nyata bila berlebihan |
| Asersi untuk invarian | Mendokumentasikan dan menegakkan asumsi | Dinonaktifkan di sebagian build produksi; bukan penanganan galat |
| Pemakaian ulang pustaka yang berat | Lebih sedikit kode untuk dimiliki; pengiriman lebih cepat | Risiko dependensi, kopling, paparan rantai pasok |
| Standar dan linting ketat | Basis kode seragam, gesekan rendah | Persiapan di muka; bisa terasa kaku bagi individu |
| Membangun untuk kemampuan diuji | Kode dapat diverifikasi dan diubah | Dapat menambah indireksi yang dianggap sebagian orang sebagai upacara |

Trade-off pusat dalam konstruksi adalah kecepatan jangka pendek versus kemampuan berubah jangka panjang. Memotong sudut (melewatkan penanganan galat, menoleransi kompleksitas, mengabaikan standar) terasa lebih cepat saat itu, dan hampir selalu lebih mahal sepanjang umur sistem. Kegagalan sebaliknya adalah rekayasa berlebihan: terlalu banyak sikap defensif, abstraksi spekulatif, dan generalitas yang tak dibutuhkan siapa pun. Konstruksi yang terampil hidup di tengah: sesederhana mungkin, sedefensif yang dituntut batas, dan tidak lebih.

## Pertanyaan untuk didiskusikan dengan tim Anda

1. **Apa definisi bersama kita yang konkret tentang "terlalu kompleks," dan di mana kita menegakkannya sebelum penggabungan?** "Minimalkan kompleksitas" adalah disiplin sentral konstruksi, tetapi sebagai slogan ia kalah dalam setiap argumen melawan tenggat. Pada tim besar di mana ratusan orang menulis ke satu basis kode, kompleksitas harus terukur, jadi sepakati sinyal yang benar-benar akan Anda tindak: panjang fungsi, kedalaman nesting, kompleksitas siklomatik, dan jumlah hal yang harus dipegang pembaca di kepalanya untuk memahami satu perubahan. Bawa pelanggar terburuk Anda ke rapat dan tanyakan apakah tinjauan Anda saat ini akan menangkapnya. Jawabannya harus menjadi gerbang pipeline atau butir daftar periksa tinjauan, karena ambang yang ditegakkan perkakas lebih bernilai daripada prinsip yang ditegakkan kemauan, dan menyelamatkan karyawan berikutnya dari akresi lambat kode yang tak dapat disentuh siapa pun dengan aman.

2. **Di produksi, apakah jalur galat kita berperilaku seperti yang kita rancang, dan kapan terakhir kali kita menjalankan salah satunya dengan sengaja?** Nasihat konstruksi mengatakan beri jalur galat sama banyak pemikiran seperti jalur bahagia, namun jalur galat biasanya kode paling sedikit teruji yang Anda miliki, dan dalam sistem kritis warga atau keselamatan di situlah kepercayaan dimenangkan atau hilang. Exception yang ditekan atau kode kembali yang diabaikan menjadi cacat misterius berminggu-minggu kemudian, dan "gagal ke keadaan aman" adalah janji yang tidak dapat Anda tepati jika Anda belum pernah melihatnya terjadi. Bawa riwayat insiden Anda: berapa banyak pemadaman masa lalu yang ditelusuri ke galat yang ditelan atau jalur pemulihan yang tak teruji? Tindakannya adalah menguji kegagalan dengan sengaja (suntikkan kartu yang ditolak, timeout, masukan cacat) dan mewajibkan setiap galat ditangani, dicatat dengan konteks, atau diteruskan, tidak pernah dijatuhkan diam-diam.

3. **Bagian mana dari basis kode kita yang sulit diuji, dan apa yang dikatakan kesulitan itu tentang desain?** Kode yang menolak pengujian hampir selalu kode yang menyembunyikan status, berkopling ke dependensi yang salah, atau mengerjakan terlalu banyak, sehingga kemampuan diuji adalah sinyal desain, bukan renungan belakangan QA. Pada sistem enterprise berumur panjang ini penting karena modul yang menyakitkan untuk diuji hari ini adalah yang akan ditakuti orang asing untuk diubah lima tahun lagi. Bawa kelas atau layanan yang ditakuti tim Anda untuk ditulis tesnya dan tanyakan mengapa: apakah statusnya tersembunyi, apakah dependensinya mustahil diganti, apakah fungsi mengerjakan tiga tugas? Jawabannya harus menggerakkan refaktoring menuju fungsi murni, dependensi eksplisit, dan unit kecil berfungsi tunggal, karena membuat kode dapat diverifikasi adalah pekerjaan yang sama dengan membuatnya dapat dipahami dan murah diubah.

4. **Kapan kita memakai ulang pustaka eksternal versus membangun kemampuan sendiri, dan siapa yang memiliki risiko rantai pasok yang kita ambil?** Meraih pustaka tepercaya lebih cepat daripada menciptakan ulang logika fondasional, namun setiap dependensi yang Anda tambah adalah kode yang tidak Anda kendalikan, tidak mudah Anda audit, dan harus Anda tambal pada hari ia dikompromikan. Pada tim besar bahayanya adalah seratus insinyur masing-masing menarik dependensi transitif sendiri sampai tak seorang pun dapat mengatakan apa yang sebenarnya dijalankan basis kode. Bawa inventaris dependensi Anda dan tanyakan tiga hal konkret: berapa pustaka yang tidak terpelihara, berapa yang membawa kerentanan yang diketahui, dan berapa yang membungkus logika yang cukup sederhana untuk dimiliki sepenuhnya. Pertimbangan yang bersaing itu nyata, karena menulis kriptografi atau penanganan tanggal sendiri hampir selalu lebih buruk daripada pustaka yang teruji, jadi tujuannya adalah kebijakan pemakaian ulang yang disengaja alih-alih penghindaran menyeluruh. Dalam konteks enterprise dan pemerintah, tambahkan sudut pengadaan dan kepatuhan lisensi, karena dependensi yang tidak diperiksa dapat membawa lisensi yang tidak kompatibel dengan kewajiban Anda atau asal-usul yang tidak akan diterima auditor mana pun.

5. **Bagaimana kita menahan kode buatan AI pada standar konstruksi yang sama dengan kode tulisan manusia, dan dapatkah kita membedakan keduanya ketika penting?** Asisten pengodean AI menghasilkan draf yang masuk akal dengan cepat, dan godaannya adalah memperlakukan keluarannya sebagai selesai karena dikompilasi dan tampak idiomatis. Aturan bab ini adalah bahwa kode hasil generate lolos tinjauan, tes, dan standar yang sama dengan apa pun lainnya, dan tim besar harus menjadikan aturan itu operasional alih-alih aspirasional. Bawa contoh perubahan berbantuan AI yang baru dirilis dan tanyakan apakah masing-masing membawa tes, lolos analisis statis, dan benar-benar dipahami manusia yang menyerahkannya, atau diloloskan atas dasar kepercayaan. Tekanan yang bersaing adalah kecepatan, karena asisten ini memang produktif dan memperlambat setiap saran hingga merangkak membuang manfaatnya. Dalam konteks yang diatur dan pemerintah, tambahkan sudut asal-usul dan akuntabilitas, karena Anda mungkin harus mengattestasi siapa yang bertanggung jawab atas sebaris kode dan apakah fragmen hasil generate membawa pertanyaan lisensi atau hak cipta yang tidak dapat Anda jawab.

6. **Apakah toolchain konstruksi kita benar-benar dibakukan dan ditegakkan di pipeline, atau individu masih bekerja dalam pengaturan yang tidak kompatibel?** Toolchain bersama berisi formatter, linter, penganalisis statis, sistem build, dan pengelola dependensi memungkinkan insinyur berpindah dengan percaya diri lintas layanan yang asing, karena kode terbaca sebagai satu suara dan pemeriksaannya identik di mana-mana. Ketika menyimpang, setiap tim menciptakan ulang konfigurasinya sendiri, waktu tinjauan dihabiskan berdebat gaya, dan cacat yang akan ditangkap penganalisis satu tim lolos di tim lain. Bawa daftar repositori yang tidak menjalankan pemeriksaan baku pada setiap commit dan tanyakan mengapa masing-masing memilih keluar. Ketegangannya adalah bahwa satu pengaturan wajib dapat terasa kaku bagi tim dengan kebutuhan yang benar-benar berbeda, jadi putuskan di mana keseragaman sepadan dengan gesekan dan di mana pengecualian terdokumentasi tidak masalah. Untuk enterprise besar atau badan publik, kaitkan ini dengan keterreproduksian dan audit, karena build yang tidak dapat Anda reproduksi byte demi byte dari toolchain terkendali adalah build yang tidak dapat Anda pertahankan di hadapan penilai bertahun-tahun kemudian.

## Lensa sektor

**Startup.** Kecepatan menang, jadi pasang formatter dan linter bersama pada hari pertama, validasi masukan pada satu batas eksternal Anda, dan jaga kode internal bersih alih-alih defensif di setiap baris. Lewati abstraksi spekulatif dan proses berat: dengan dua atau tiga insinyur seluruh tim memegang basis kode di kepala mereka, dan risiko sebenarnya adalah kompleksitas yang hidup lebih lama daripada ingatan bersama itu. Bersandarlah pada pustaka tepercaya untuk apa pun yang fondasional agar Anda menulis sesedikit mungkin kode yang dapat Anda miliki dengan baik.

**Bisnis kecil.** Tanpa insinyur build khusus dan dengan anggaran ketat, pilih konvensi yang sudah ditegakkan perkakas Anda secara gratis: formatter dan linter yang datang bersama bahasa, bawaan yang masuk akal, dan seperangkat kecil aturan yang dapat diingat semua orang. Beli atau adopsi pustaka yang terpelihara baik daripada membangun infrastruktur yang tidak sanggup Anda isi stafnya untuk memelihara. Belanjakan disiplin terbatas Anda pada dua hal yang paling menyakitkan bila diabaikan, memvalidasi masukan di batas dan tidak pernah menelan galat secara diam-diam.

**Enterprise.** Dengan ratusan insinyur menulis ke kode bersama, prioritasnya adalah keseragaman dan penegakan: toolchain baku yang dipasang ke pipeline, gerbang analisis statis, dan aturan validasi batas yang diterapkan di mana-mana agar orang berpindah dengan percaya diri antarlayanan. Kelola risiko dependensi dan rantai pasok sebagai proses yang diatur alih-alih improvisasi per tim, dan gunakan asersi untuk mengkodekan invarian domain yang harus berlaku di setiap tim. Perlakukan standar konstruksi sebagai substrat yang menjaga basis kode tetap layak huni melintasi puluhan tahun dan pergantian staf.

**Pemerintah.** Sistem berumur panjang yang kritis bagi warga menjadikan konstruksi yang disiplin soal jaminan dan akuntabilitas. Isolasi aturan yang mudah berubah seperti legislasi di balik antarmuka stabil agar perubahan tetap lokal dan dapat dilacak ke persyaratan, gagal ke keadaan aman yang dikenal alih-alih melanjutkan dalam keadaan rusak, dan kirim setiap modul dengan tes yang sekaligus menjadi bukti audit. Kewajiban pengadaan dan transparansi berarti toolchain, dependensi, dan penanganan galat Anda harus didokumentasikan cukup baik agar pegawai negeri yang tiba bertahun-tahun kemudian, atau auditor eksternal, dapat memverifikasi bahwa kodenya benar.

## Contoh

**Startup.** Sebuah startup tiga insinyur memasang formatter dan linter bersama pada hari pertama dan menjalankannya pada setiap commit, sehingga basis kode terbaca sebagai satu suara bahkan saat mereka menambah kontraktor. Mereka memvalidasi masukan pada batas API dan memperlakukan semua yang datang dari luar sebagai bermusuhan, tetapi menjaga logika internal tetap bersih alih-alih menyelimutinya dengan pemeriksaan redundan. Ketika webhook pembayaran mulai gagal, perbaikannya cepat karena tidak ada exception yang pernah ditelan diam-diam dan pesan galat membawa konteks cukup untuk menunjuk langsung ke penyebabnya. Seluruh pengaturan memakan satu sore dan menyelamatkan mereka dari akresi lambat kompleksitas yang akan membuat minggu pertama karyawan berikutnya menyengsarakan.

**Enterprise.** Sebuah perusahaan pembayaran global menegakkan toolchain bersama di ratusan insinyur: format dan linting otomatis pada setiap commit, gerbang analisis statis di pipeline, dan aturan bahwa semua masukan eksternal divalidasi pada batas layanan. Logika domain memakai asersi untuk menegakkan invarian seperti "entri buku besar selalu seimbang," sementara kondisi runtime seperti kartu yang ditolak ditangani sebagai hasil eksplisit yang dicatat. Karena standar seragam dan galat tidak pernah ditelan diam-diam, insinyur berpindah dengan percaya diri lintas layanan yang asing, dan insiden produksi dapat didiagnosis langsung dari log.

**Pemerintah.** Sebuah lembaga pajak nasional membangun sistem penilaian berumur panjang yang diharapkan berjalan puluhan tahun di bawah legislasi yang berubah. Konstruksi mengisolasi setiap aturan pajak di balik antarmuka stabil, sehingga perubahan legislasi tahunan tetap lokal dan dapat dilacak ke persyaratan (bab 2.8). Validasi defensif menjaga setiap masukan yang menghadap warga. Jalur galat gagal ke keadaan aman yang tidak pernah menerbitkan penilaian keliru secara diam-diam. Setiap modul dikirim dengan tes unit sebagai bukti audit. Karena konstruksinya dibakukan dan terdokumentasi baik, pegawai negeri baru dapat memelihara dengan aman kode yang ditulis pendahulu yang sudah lama pergi.

## Kasus bisnis: motivasi, ROI, dan TCO

Imbal hasil konstruksi yang disiplin adalah kemampuan abadi untuk mengubah perangkat lunak dengan murah dan aman, dan di situlah sebagian besar total biaya kepemilikan sebuah sistem ditentukan. Studi ekonomi perangkat lunak secara konsisten menunjukkan bahwa sebagian besar biaya seumur hidup sistem adalah pemeliharaan, dan biaya pemeliharaan didominasi oleh seberapa dapat dipahami dan diubah kodenya. Meminimalkan kompleksitas, menangani galat secara eksplisit, dan mengikuti standar langsung menurunkan biaya setiap perubahan mendatang dan setiap insiden produksi.

Biaya mengadopsi sederhana dan sebagian besar di muka: tetapkan standar, pasang linter dan penganalisis, dan bangun kebiasaan menulis kode yang dapat diverifikasi dan defensif. Biaya pengabaian, di sisi lain, berlipat. Kompleksitas menumpuk menjadi kode yang lambat diubah dan berisiko disentuh. Galat diam berubah menjadi insiden produksi mahal. Gaya tidak konsisten melipatgandakan upaya setiap tinjauan dan setiap orientasi. Untuk meyakinkan pimpinan, hubungkan kualitas konstruksi dengan tingkat kegagalan perubahan, waktu rata-rata pemulihan, tingkat cacat yang lolos, dan waktu orientasi, semuanya langsung diperbaiki oleh disiplin konstruksi.

## Anti-pola dan jebakan

- **Rayapan kompleksitas:** menumpuk kode cerdik, bersarang dalam, atau melebar sampai tak seorang pun memahaminya.
- **Menelan galat secara diam-diam:** blok catch kosong dan kode kembali yang diabaikan yang mengubah kegagalan menjadi misteri masa depan.
- **Berlebihan dalam pemrograman defensif:** pemeriksaan redundan di mana-mana yang mengubur logika dan menutupi cacat nyata.
- **Mencampuradukkan asersi dengan penanganan galat:** memakai asersi untuk kondisi runtime, atau exception untuk invarian programmer.
- **Konstruksi salin-tempel:** menduplikasi logika alih-alih memakai ulang, sehingga perbaikan harus dibuat di banyak tempat.
- **Generalitas spekulatif:** membangun abstraksi dan konfigurabilitas untuk kebutuhan yang tidak pernah tiba.
- **Mengabaikan standar:** setiap insinyur mengode dengan caranya sendiri, melipatgandakan beban kognitif di seluruh basis kode.
- **Konstruksi tanpa tes:** menulis kode tanpa tes pendamping, menunda verifikasi ke fase yang tidak pernah tiba.

## Model kematangan

- **Tingkat 1 (Memulai):** Konstruksi ad hoc dan reaktif; kompleksitas dan penanganan galat bervariasi menurut individu; sedikit standar ada, dan kegagalan diam-diam umum.
- **Tingkat 2 (Mengembangkan):** Standar pengodean, formatter, dan linter ada, dan penanganan galat dasar serta pengujian unit diharapkan, tetapi praktik tidak konsisten dan setiap tim menerapkannya secara berbeda.
- **Tingkat 3 (Membakukan):** Minimalisasi kompleksitas, validasi batas, penanganan galat eksplisit, dan kemampuan diuji didokumentasikan dan ditegakkan di seluruh organisasi, di pipeline dan dalam tinjauan, sehingga seluruh basis kode terbaca seolah satu penulis cermat yang menulisnya.
- **Tingkat 4 (Mengelola):** Kualitas konstruksi diukur terhadap garis dasar; tim melacak kompleksitas siklomatik, tingkat cacat yang lolos, tingkat kegagalan perubahan, cakupan tes jalur galat, dan temuan tinjauan kode, dan bertindak atas tren alih-alih opini.
- **Tingkat 5 (Mengorkestrasi):** Konstruksi terus diperbaiki dan terintegrasi di seluruh organisasi; pola defensif, standar, dan metrik memberi umpan balik ke refaktoring dan perkakas; perkakas berbantuan AI berjalan di bawah gerbang kualitas yang sama, dan praktik beradaptasi seiring berubahnya bahasa, regulasi, dan risiko.

## Gagasan untuk didiskusikan

- Di mana kompleksitas aksidental paling banyak menumpuk dalam basis kode Anda, dan kebiasaan konstruksi apa yang menciptakannya?
- Apa aturan sebenarnya tim Anda tentang di mana memvalidasi masukan dan di mana memercayai?
- Apakah insinyur Anda membedakan asersi dari penanganan galat, dan apakah perbedaan itu konsisten?
- Seberapa banyak kualitas Anda dibangun selama konstruksi versus tertangkap kemudian dalam tinjauan atau pengujian?
- Bagaimana Anda memutuskan kapan memakai ulang pustaka versus membangun, mengingat risiko rantai pasok?
- Bagaimana kode buatan AI harus ditahan pada standar konstruksi yang sama dengan kode tulisan manusia?

## Poin-poin utama

- Konstruksi adalah tempat desain menjadi kode yang dapat dipelihara; meminimalkan kompleksitas adalah disiplin sentralnya.
- Bangun untuk perubahan dan untuk verifikasi: kode yang dapat diuji dan diubah adalah kode yang dapat dipahami.
- Bertahan di batas kepercayaan, percaya di dalamnya, dan jangan pernah menelan galat secara diam-diam.
- Gunakan asersi untuk invarian dan penanganan galat untuk kondisi runtime yang diharapkan; jangan campur keduanya.
- Bakukan perkakas dan gaya, pakai ulang dengan sengaja, dan bangun kualitas masuk alih-alih memeriksanya sesudahnya.

## Referensi dan bacaan lanjutan

- IEEE Computer Society, *SWEBOK Guide (Guide to the Software Engineering Body of Knowledge)*, area pengetahuan Software Construction
- Steve McConnell, *Code Complete: A Practical Handbook of Software Construction*
- Robert C. Martin, *Clean Code: A Handbook of Agile Software Craftsmanship*
- Andrew Hunt dan David Thomas, *The Pragmatic Programmer*
- Martin Fowler, *Refactoring: Improving the Design of Existing Code*
- John Ousterhout, *A Philosophy of Software Design*
