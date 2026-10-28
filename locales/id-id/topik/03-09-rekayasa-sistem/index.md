# 3.9 Rekayasa sistem

## Tinjauan dan motivasi

[Rekayasa sistem](https://en.wikipedia.org/wiki/Systems_engineering) adalah disiplin merekayasa seluruh sistem kompleks dari ujung ke ujung, agar semua bagiannya bekerja bersama memenuhi kebutuhan nyata. Bagian-bagiannya mencakup jauh lebih banyak daripada perangkat lunak. Sistem modern biasanya memadukan perangkat lunak, perangkat keras, manusia, data, dan proses, dan ia harus beroperasi di dunia nyata yang berantakan. Rekayasa sistem menjaga semuanya tetap selaras sepanjang seluruh hidup sistem.

Ini berbeda dari arsitektur perangkat lunak. Arsitektur perangkat lunak (bab 3.1) memutuskan bagaimana komponen perangkat lunak distrukturkan dan bagaimana mereka berbicara satu sama lain. Rekayasa sistem berada satu tingkat di atasnya. Ia bertanya apa yang harus dilakukan sistem secara keseluruhan, bagaimana perangkat lunak, perangkat keras, dan operator manusia membagi pekerjaan, dan bagaimana Anda akan membuktikan barang jadi itu berfungsi. Rumah profesionalnya adalah [INCOSE](https://en.wikipedia.org/wiki/International_Council_on_Systems_Engineering), International Council on Systems Engineering, dan standar jangkarnya adalah [ISO/IEC/IEEE 15288](https://en.wikipedia.org/wiki/ISO/IEC_15288), yang mendefinisikan proses untuk hidup sistem.

Ini penting bagi program enterprise dan pemerintah besar karena sistem mereka besar, berumur panjang, dan kritis keselamatan atau kritis misi. Platform pertahanan, sistem lalu lintas udara, atau konstelasi satelit memadukan perangkat keras khusus, komponen pihak ketiga, perangkat lunak tertanam dan cloud, serta operator manusia, dan tak ada satu tim pun yang dapat memegang keseluruhannya di kepala. Anda juga sering membangun [sistem dari sistem](https://en.wikipedia.org/wiki/System_of_systems): banyak sistem independen, masing-masing berguna sendiri, yang harus bekerja sama menghasilkan kemampuan yang lebih besar.

Bab ini terhubung dengan persyaratan perangkat lunak (bab 2.8), dasar-dasar arsitektur (bab 3.1), model dan metode perangkat lunak (bab 2.12), interoperabilitas dan standar terbuka (bab 3.8), dan manajemen proyek (bab 10.6).

## Prinsip utama

- **Rekayasakan keseluruhan, bukan bagian-bagiannya.** Sistem berhasil atau gagal sebagai satu kesatuan, sehingga mengoptimalkan satu subsistem secara terpisah dapat memperburuk keseluruhan.
- **Ikuti siklus hidup.** Sistem punya hidup dari konsep pertama hingga pensiun terakhir. Rencanakan semuanya, bukan hanya pembangunan.
- **Telusuri setiap persyaratan.** Setiap kebutuhan harus terpetakan ke persyaratan, elemen desain, dan tes. Jika tidak dapat ditelusuri, Anda tidak dapat membuktikannya.
- **Kelola antarmuka dengan sengaja.** Kebanyakan kegagalan terjadi di batas antarbagian, sehingga antarmuka layak mendapat kepemilikan dan kendali eksplisit.
- **Verifikasi dan validasi secara terpisah.** Membangun benda dengan benar (verifikasi) dan membangun benda yang benar (validasi) adalah pertanyaan berbeda, dan Anda butuh kedua jawabannya.
- **Harapkan perilaku emergen.** Menggabungkan bagian menciptakan perilaku yang tak ditunjukkan bagian tunggal mana pun. Sebagian adalah tujuannya, sebagian kejutan buruk.
- **Rekayasakan perangkat keras dan lunak bersama.** Ketika keduanya khusus, keputusan di satu membatasi yang lain, jadi rencanakan bersama.

## Rekomendasi

### Kelola siklus hidup sistem penuh

Perlakukan sistem sebagai memiliki hidup yang utuh, dan rencanakan setiap tahap. Siklus hidup umum berjalan: **konsep** (pahami kebutuhan dan jelajahi opsi), **persyaratan** (nyatakan dengan tepat apa yang harus dilakukan sistem), **desain** (putuskan arsitektur dan bagian-bagiannya), **integrasi** (satukan bagian-bagiannya), **verifikasi dan validasi** (buktikan ia berfungsi dan merupakan sistem yang tepat), **operasi** (jalankan dan pelihara), dan **pensiun** (nonaktifkan dengan aman, termasuk data dan pembuangan). ISO/IEC/IEEE 15288 memberi Anda kerangka proses untuk ini. Tahap-tahap tidak perlu berupa waterfall kaku; Anda dapat beriterasi, membuat prototipe, dan mengirim increment. Intinya Anda menangani setiap tahap dengan sadar, termasuk tahap-tahap lanjut yang mahal yang sering diabaikan rencana awal.

### Tangkap kebutuhan pemangku kepentingan dan alokasikan persyaratan dengan keterlacakan

Mulai dari orang-orang yang peduli pada sistem: pengguna, operator, pemilik, regulator, dan publik. Kumpulkan **kebutuhan** mereka dalam bahasa sederhana, lalu ubah kebutuhan itu menjadi **persyaratan** terekayasa yang spesifik dan dapat diuji (lihat bab 2.8). Berikutnya **alokasi persyaratan**: menetapkan setiap persyaratan tingkat sistem ke subsistem tertentu, agar Anda tahu bagian mana yang bertanggung jawab memenuhinya. Simpan **matriks [keterlacakan](https://en.wikipedia.org/wiki/Requirements_traceability)**, catatan hidup yang menghubungkan setiap kebutuhan ke persyaratannya, ke elemen desain yang memenuhinya, dan ke tes yang memverifikasinya. Ia memungkinkan Anda membuktikan kapan saja bahwa setiap kebutuhan tercakup dan setiap bagian ada karena suatu alasan.

### Kelola antarmuka secara eksplisit

Antarmuka adalah tempat bagian-bagian bertemu, dan tempat sistem paling sering rusak. Antarmuka dapat berupa konektor fisik, protokol jaringan, format data, atau prosedur manusia. Untuk masing-masing, tulis **Interface Control Document** (ICD): spesifikasi yang disepakati tentang persis bagaimana dua bagian terhubung dan bertukar informasi. Beri setiap antarmuka pemilik yang jelas di setiap sisi. Bersandar pada spesifikasi bersama yang dipublikasikan alih-alih konektor sekali pakai membuat integrasi jauh lebih mudah, yaitu argumen interoperabilitas dalam bab 3.8. Bekukan antarmuka lebih awal di tempat Anda bisa, karena perubahan terlambat beriak ke setiap bagian yang menyentuhnya.

### Integrasikan lalu verifikasi dan validasi

**Integrasi sistem** menggabungkan subsistem menjadi keseluruhan yang berfungsi, biasanya bertahap alih-alih sekaligus, agar Anda menemukan masalah selagi masih kecil. Setelah integrasi datang **[verifikasi dan validasi](https://en.wikipedia.org/wiki/Verification_and_validation)** (V&V), dua pemeriksaan yang berbeda. **Verifikasi** bertanya: apakah kita membangun sistem dengan benar, artinya apakah ia memenuhi persyaratan yang ditetapkan? Anda memverifikasi lewat inspeksi, analisis, demonstrasi, dan tes. **Validasi** bertanya: apakah kita membangun sistem yang benar, artinya apakah ia memenuhi kebutuhan nyata pemangku kepentingan dalam pemakaian nyata? Sistem dapat lulus verifikasi (memenuhi spesifikasi) namun gagal validasi (spesifikasinya keliru). Rencanakan keduanya sejak awal, dan tulis persyaratan serta antarmuka agar dapat diverifikasi sejak awal.

### Adopsi rekayasa sistem berbasis model

Rekayasa sistem tradisional menghasilkan gunungan dokumen yang menyimpang dari sinkronisasi. **[Rekayasa sistem berbasis model](https://en.wikipedia.org/wiki/Model-based_systems_engineering)** (MBSE) menggantikan tumpukan itu dengan satu model formal bersama tentang sistem, tempat tampilan dan laporan dihasilkan. Bahasa pemodelan yang umum adalah **[SysML](https://en.wikipedia.org/wiki/Systems_Modeling_Language)** (Systems Modelling Language), bahasa grafis untuk mendeskripsikan persyaratan, struktur, perilaku, dan kendala sistem. Karena semuanya hidup dalam satu model yang terhubung, perubahan memperbarui di mana-mana, dan keterlacakan menjadi kueri alih-alih pengejaran manual. MBSE terhubung dengan gagasan pemodelan dalam bab 2.12. Adopsi secara bertahap, mulai dari bagian berisiko tertinggi di mana model bersama membuahkan hasil tercepat.

### Terapkan berpikir sistem pada perilaku emergen

Praktikkan [berpikir sistem](https://en.wikipedia.org/wiki/Systems_thinking): bernalar tentang keseluruhan dan hubungan antarbagian, bukan hanya bagian satu per satu. Inilah cara Anda mengantisipasi **[perilaku emergen](https://en.wikipedia.org/wiki/Emergence)**: properti yang muncul hanya ketika bagian-bagian bergabung dan tak ditunjukkan bagian tunggal mana pun. Emergensi yang baik sering kali tujuan sistem (kawanan drone menutupi area yang tak dapat ditutupi satu drone). Emergensi yang buruk adalah kegagalan mengejutkan (dua subsistem aman berinteraksi menciptakan keadaan berbahaya). Anda tidak dapat menguji emergensi keluar dari sistem yang tak pernah Anda modelkan, jadi pakai simulasi dan analisis bahaya terstruktur untuk menemukannya sebelum operasi.

### Rekayasakan perangkat keras dan lunak bersama

Ketika sistem menyertakan perangkat keras khusus, rekayasakan perangkat keras dan lunak bersama, praktik yang disebut **[desain bersama perangkat keras/lunak](https://en.wikipedia.org/wiki/Hardware/software_co-design)**. Keputusan saling mengikat: perangkat keras menetapkan batas waktu, memori, dan daya yang harus dihidupi perangkat lunak, dan kebutuhan perangkat lunak membentuk apa yang harus disediakan perangkat keras. Lead time perangkat keras yang panjang juga menggerakkan jadwal. Putuskan lebih awal fungsi mana yang hidup di perangkat keras dan mana di perangkat lunak, dan tinjau ulang pembagian itu seiring munculnya kendala.

## Trade-off: kelebihan dan kekurangan

| Pendekatan | Kelebihan | Kekurangan / biaya |
|---|---|---|
| Ketelitian rekayasa sistem penuh | Lebih sedikit kejutan terlambat, keterlacakan kuat, lebih aman dan dapat diaudit | Biaya awal tinggi, mulai lebih lambat, proses berat |
| Pendekatan ringan / hanya perangkat lunak | Cepat, murah, fleksibel untuk cakupan kecil | Runtuh pada sistem multidisiplin besar, melewatkan antarmuka dan emergensi |
| Berbasis model (MBSE) | Satu sumber kebenaran, keterlacakan mudah, tampilan konsisten | Biaya perkakas dan pelatihan, perubahan budaya, kurva belajar |
| Rekayasa sistem berbasis dokumen | Familier, biaya perkakas rendah, mudah dibagikan | Dokumen menyimpang dari sinkronisasi, keterlacakan manual dan rawan galat |

Trade-off pusatnya adalah ketelitian versus kecepatan. Rekayasa sistem penuh memuat upaya di depan pada konsep, persyaratan, dan pekerjaan antarmuka. Upaya itu membayar dirinya berkali-kali lipat pada sistem besar, berumur panjang, dan kritis keselamatan, di mana cacat yang ditemukan dalam operasi dapat berbiaya ribuan kali lipat dibanding cacat yang sama yang ditemukan dalam persyaratan. Pada produk kecil, berumur pendek, dan hanya perangkat lunak, ketelitian itu berlebihan. Cocokkan bobot proses Anda dengan ukuran, umur, dan risiko sistem. Mode kegagalannya adalah menerapkan kebiasaan proyek sekali pakai pada sistem yang akan berjalan tiga puluh tahun dan membawa risiko dunia nyata.

## Pertanyaan untuk didiskusikan dengan tim Anda

1. **Di mana Anda membangun persis apa yang dituntut spesifikasi namun tetap mengirim sistem yang salah, dan apa yang akan menangkapnya?** Verifikasi (apakah kita membangunnya dengan benar) dan validasi (apakah kita membangun hal yang benar) menjawab pertanyaan berbeda, dan sistem dapat lulus setiap tes verifikasi sementara gagal validasi karena spesifikasinya sendiri keliru. Pada program besar keduanya dilebur menjadi "pengujian", sehingga tak ada yang memvalidasi terhadap kebutuhan operator nyata sampai terlambat, ketika perbaikan berbiaya ribuan kali lipat dibanding perubahan persyaratan. Bawa contoh masa lalu di mana sistem yang diserahkan memenuhi persyaratannya namun meleset dari kebutuhan sebenarnya, dan tanyakan aktivitas validasi apa (simulasi dengan operator nyata, prototipe awal di lapangan) yang akan memunculkannya lebih cepat. Rencanakan kedua pemeriksaan sejak awal, dan tulis persyaratan serta antarmuka agar dapat diverifikasi sama sekali. Pembedaan itu menentukan di mana Anda membelanjakan upaya tinjauan yang langka.

2. **Bagaimana Anda memburu perilaku emergen yang buruk sebelum sistem beroperasi, bukan sesudahnya?** Menggabungkan subsistem aman dapat menciptakan keadaan berbahaya yang tak ditunjukkan bagian tunggal mana pun, dan Anda tidak dapat menguji emergensi keluar dari sistem yang tak pernah Anda modelkan. Untuk program kritis keselamatan atau kritis misi, interaksi mengejutkan adalah yang melukai seseorang atau menggagalkan misi, sehingga harus ditemukan sebelum operasi langsung. Bawa pendekatan Anda memodelkan keseluruhan (simulasi, analisis bahaya terstruktur, model SysML yang menangkap interaksi) dan tanyakan perilaku lintas subsistem mana yang benar-benar telah Anda jelajahi versus yang Anda asumsikan hilang. Emergensi yang baik sering kali tujuan sistem dan layak dirancang menujunya; emergensi yang buruk adalah kegagalan yang harus Anda rekayasakan penangkalnya. Jika satu-satunya strategi integrasi Anda adalah mengkabel bagian bersama dan melihat apa yang terjadi, Anda merencanakan menemukan emergensi di produksi.

3. **Kapan keputusan perangkat keras berlead-time panjang harus dibekukan, dan bagaimana tenggat itu menggerakkan jadwal perangkat lunak Anda?** Ketika sistem menyertakan perangkat keras khusus, keduanya harus direkayasa bersama: chip menetapkan batas atas waktu, memori, dan daya yang dihidupi perangkat lunak, dan lead time perangkat keras sering mendominasi seluruh jadwal. Tim yang memperlakukan perangkat lunak sebagai terpisah mengoptimalkan secara lokal lalu bertabrakan dengan kendala perangkat keras saat integrasi, kehilangan berbulan-bulan. Bawa lead time perangkat keras dan tanggal paling lambat pembagian fungsi perangkat keras/lunak harus diputuskan, dan tinjau ulang pembagian itu seiring kendala muncul alih-alih membekukannya secara buta. Semakin awal Anda memutuskan fungsi mana yang hidup di silikon dan mana di perangkat lunak, semakin sedikit pembalikan mahal yang Anda hadapi. Antarmuka antara keduanya layak mendapat Interface Control Document dan pemilik di setiap sisi, karena perubahan terlambat di sana beriak melalui segala yang menyentuhnya.

4. **Dapatkah Anda menelusuri satu kebutuhan pemangku kepentingan sampai ke persyaratan, elemen desain, dan tes yang membuktikannya, dan siapa yang menjaga tautan itu tetap hidup?** Keterlacakan memungkinkan Anda menunjukkan kapan saja bahwa setiap kebutuhan tercakup dan setiap bagian ada karena suatu alasan, namun pada program besar matriks membusuk begitu tak seorang pun memilikinya. Tarikan yang bersaing nyata: insinyur mengalami keterlacakan sebagai beban birokrasi, dan matriks yang dipelihara dengan tangan menyimpang lebih cepat daripada desain berubah. Bawa satu benang asli dari program saat ini dan coba telusuri dari ujung ke ujung di ruangan, dari kebutuhan pemangku kepentingan yang dinamai, ke persyaratan yang dialokasikan, ke subsistem dan elemen desain yang memenuhinya, ke tes verifikasi, dan catat di mana rantai putus. Putuskan siapa yang memiliki matriks dan apakah ia harus hidup dalam model di mana keterlacakan adalah kueri alih-alih pengejaran manual. Untuk program enterprise dan pemerintah, matriks juga artefak audit yang dituntut regulator dan otoritas akuisisi, sehingga rantai putus melakukan lebih dari memperlambat rekayasa; ia dapat menghentikan sertifikasi atau pembayaran.

5. **Apakah pendekatan berbasis model sepadan dengan biaya perkakas dan budayanya bagi Anda, atau akan menjadi shelfware mahal?** Rekayasa sistem berbasis dokumen familier dan murah diberi perkakas, tetapi dokumennya menyimpang dari sinkronisasi dan keterlacakannya manual serta rawan galat; MBSE menggantikan tumpukan itu dengan satu model terhubung, dengan harga perkakas, pelatihan, dan perubahan budaya yang sejati. Kedua ekstrem mahal: lewati MBSE pada program multidisiplin besar dan Anda membayar dengan kejutan integrasi, adopsi tanpa disiplin menjaga model tetap mutakhir dan ia membusuk menjadi shelfware yang lebih buruk daripada tanpa model. Bawa pembacaan jujur tentang kematangan perkakas Anda, siapa di tim yang benar-benar dapat menulis dan memelihara model SysML, dan satu subsistem berisiko tinggi mana yang dapat menjadi percontohan di tempat model bersama membuahkan hasil tercepat. Putuskan secara bertahap alih-alih mewajibkan seluruh organisasi sekaligus. Untuk program enterprise atau pemerintah besar dengan banyak pemasok, timbang apakah model bersama satu-satunya cara realistis menjaga persyaratan, antarmuka, dan tes tetap konsisten lintas kontraktor yang kalau tidak akan bertukar dokumen basi.

6. **Apakah rencana siklus hidup Anda sungguh-sungguh mendanai operasi dan pensiun, atau diam-diam berhenti di peluncuran?** Tahap yang mendominasi total biaya sistem berumur panjang, menjalankannya selama puluhan tahun dan menonaktifkannya dengan aman, adalah yang rutin diabaikan rencana awal, karena tekanan selalu untuk mengirim. Pertimbangan yang bersaing adalah bahwa uang dan perhatian paling langka tepat ketika tahap-tahap lanjut ini terasa paling jauh, sehingga operasi, pemeliharaan, migrasi data, dan pembuangan ditunda sampai menjadi perebutan yang mahal dan berisiko. Bawa rencana siklus hidup saat ini dan periksa apakah ia menamai pemilik, anggaran, dan kriteria keluar untuk operasi dan pensiun, atau memperlakukan peluncuran sebagai garis finis. Tanyakan apa yang terjadi pada data dan perangkat keras di akhir masa pakai, dan siapa yang membayar bertahun-tahun pemeliharaan di antaranya. Untuk sistem enterprise dan pemerintah yang harus berjalan dua puluh atau tiga puluh tahun lalu pensiun di bawah pengawasan publik, penonaktifan tak terencana dapat melanggar kewajiban regulasi, lingkungan, atau retensi catatan, sehingga pensiun termasuk dalam rencana dan anggaran sejak tinjauan konsep pertama.

## Lensa sektor

**Startup.** Tim kecil tidak dapat menjalankan program rekayasa sistem formal dan tidak boleh mencobanya, tetapi tetap dapat memperlakukan firmware, aplikasi, dan cloud sebagai satu sistem alih-alih tiga proyek terpisah. Tulis satu dokumen antarmuka singkat yang mengunci bagaimana bagian-bagian berbicara, simpan tabel sederhana yang menghubungkan setiap kebutuhan pelanggan ke bagian yang memenuhinya, dan lewati proses berat. Sumber daya Anda yang paling langka adalah perhatian rekayasa, jadi belanjakan upaya keterlacakan hanya di tempat asumsi yang salah pada batas akan diam-diam merusak produk di lapangan.

**Bisnis kecil.** Tanpa insinyur sistem khusus dan dengan anggaran ketat, bersandarlah pada standar yang dipublikasikan dan subsistem yang dibeli alih-alih integrasi pesanan yang harus Anda rancang dan verifikasi sendiri. Pilih vendor yang mengekspos spesifikasi antarmuka yang jelas agar bagian-bagian cocok tanpa konektor khusus yang harus Anda miliki selamanya. Bingkai pilihan membangun-versus-membeli di sekitar antarmuka mana yang secara realistis dapat Anda kendalikan dan verifikasi sepanjang umur produk, dan beli sisanya.

**Enterprise.** Pada skala besar masalahnya konsistensi di banyak tim dan pemasok: proses siklus hidup bersama yang selaras dengan ISO/IEC/IEEE 15288, Interface Control Document dan pemilik bernama untuk setiap batas pemasok, dan keterlacakan ujung ke ujung agar perubahan satu komponen tidak memicu perebutan seluruh program. Investasikan pada MBSE di tempat model bersama menjaga persyaratan, antarmuka, dan tes tetap selaras lintas kontraktor. Atur proses agar verifikasi dan validasi tetap berbeda dan setiap persyaratan dialokasikan ke bagian yang bertanggung jawab.

**Pemerintah.** Aturan pengadaan, transparansi, dan akuntabilitas publik membentuk setiap pilihan. Tetapkan proses rekayasa sistem, keterlacakan, dan bukti V&V dalam kontrak, wajibkan pemasok menyerahkan dokumen kendali antarmuka dan artefak siklus hidup yang dapat Anda audit, dan sisihkan validasi keselamatan dan misi untuk tinjauan independen dengan operator nyata sebelum cut-over langsung apa pun. Rencanakan dan danai operasi serta pensiun secara eksplisit, karena program publik bertanggung jawab atas siklus hidup penuh, termasuk penonaktifan aman dan retensi catatan.

## Contoh

**Startup.** Sebuah startup perangkat keras beranggotakan empat orang yang membangun sensor terhubung tidak mampu program rekayasa sistem formal, tetapi tetap memperlakukan produk sebagai satu sistem firmware, aplikasi seluler, dan backend cloud alih-alih tiga proyek terpisah. Mereka menulis satu dokumen antarmuka singkat yang mengunci bagaimana perangkat, aplikasi, dan server berbicara (format pesan, satuan, kode galat) dan menyimpan tabel sederhana yang menghubungkan setiap kebutuhan pelanggan ke bagian yang memenuhinya. Ketika chip sensor yang lebih murah memaksa perubahan firmware, antarmuka bersama itu segera menunjukkan apa yang harus disesuaikan aplikasi dan backend, sehingga pergantian komponen tidak diam-diam merusak produk di lapangan.

**Enterprise.** Sebuah produsen otomotif global membangun platform kendaraan listrik baru: sistem perangkat lunak (manajemen baterai, bantuan pengemudi, infotainmen), perangkat keras (motor, sensor, chip), dan faktor manusia, ditambah banyak pemasok yang masing-masing menyerahkan subsistem. Perusahaan menjalankan program rekayasa sistem. Kebutuhan pemangku kepentingan mengalir ke persyaratan yang dialokasikan, setiap antarmuka pemasok punya Interface Control Document, dan model SysML mengikat persyaratan ke desain ke tes. Ketika pemasok sel baterai mengubah komponen, model keterlacakan menunjukkan persis persyaratan, antarmuka, dan tes mana yang terpengaruh, sehingga perubahan terkandung alih-alih memicu perebutan seluruh program.

**Pemerintah.** Otoritas navigasi udara nasional memodernisasi sistem manajemen lalu lintas udaranya, sistem dari sistem kritis keselamatan yang mencakup radar, stasiun kerja pengendali, komunikasi, dan perangkat lunak, dioperasikan sepanjang waktu. Program mengikuti ISO/IEC/IEEE 15288 sepanjang siklus hidup penuh. Verifikasi membuktikan setiap subsistem memenuhi spesifikasinya, dan validasi lewat simulasi dengan pengendali nyata membuktikan sistem terintegrasi mendukung operasi aman sebelum lalu lintas langsung bergantung padanya. V&V yang ketat memungkinkan otoritas melakukan cut-over bertahap, dengan cadangan di setiap langkah, karena di sini kegagalan emergen yang tak teruji adalah peristiwa keselamatan publik.

## Kasus bisnis: motivasi, ROI, dan TCO

Motivasinya adalah bahwa cacat menjadi secara eksponensial lebih mahal semakin terlambat ditemukan. Galat persyaratan yang tertangkap pada tahap persyaratan nyaris tak berbiaya untuk diperbaiki. Galat yang sama yang tertangkap dalam operasi dapat berbiaya ribuan kali lipat, dan pada sistem kritis keselamatan dapat merenggut nyawa, penarikan produk, atau misi yang gagal. Rekayasa sistem menggeser penemuan cacat ke tahap awal yang murah.

Untuk **imbal hasil investasi** (ROI, nilai yang diperoleh dibanding biaya yang dikeluarkan), imbalannya adalah pengerjaan ulang yang dihindari, lebih sedikit kegagalan integrasi, dan program yang mencapai jadwal dan anggaran alih-alih melampauinya. Studi industri atas program besar berulang kali menemukan bahwa upaya rekayasa sistem yang kuat berkorelasi dengan kelebihan yang lebih kecil. Untuk **total biaya kepemilikan** (TCO, biaya seumur hidup penuh membangun, menjalankan, dan memensiunkan sistem), rekayasa sistem memperhitungkan tahap operasi dan pensiun yang mendominasi biaya jangka panjang namun diabaikan proyek ad hoc. Merancang untuk kemudahan pemeliharaan, antarmuka, dan pembuangan sejak awal menurunkan biaya puluhan tahun yang dihabiskan sistem dalam layanan. Lihat manajemen proyek (bab 10.6).

## Anti-pola dan jebakan

- **Desain besar di muka tanpa iterasi.** Memperlakukan siklus hidup sebagai waterfall satu arah yang kaku, sehingga Anda baru tahu persyaratan keliru setelah membangun semuanya.
- **Persyaratan tanpa keterlacakan.** Tumpukan persyaratan yang tak dihubungkan siapa pun ke desain atau tes, sehingga Anda tak dapat membuktikan cakupan atau membenarkan bagian mana pun.
- **Mengabaikan antarmuka.** Mengasumsikan subsistem akan cocok begitu saja, lalu kehilangan berbulan-bulan saat integrasi karena ketidakcocokan batas yang tak dimiliki siapa pun.
- **Verifikasi tanpa validasi.** Membuktikan sistem memenuhi spesifikasinya sambil tak pernah memeriksa apakah spesifikasi cocok dengan kebutuhan nyata, lalu mengirim sistem yang salah.
- **Memperlakukan perangkat lunak sebagai terpisah.** Tim perangkat lunak mengoptimalkan secara lokal sambil mengabaikan kendala perangkat keras, waktu, dan operator manusia.
- **MBSE sebagai shelfware.** Membangun model sekali, lalu membiarkannya membusuk tak sinkron sehingga lebih buruk daripada tanpa model.
- **Melewatkan perencanaan pensiun.** Tanpa rencana untuk penonaktifan, migrasi data, atau pembuangan, sehingga akhir masa pakai menjadi perebutan yang mahal dan berisiko.

## Model kematangan

**Tingkat 1: Memulai.** Rekayasa sistem ad hoc dan reaktif. Persyaratan hidup di dokumen yang tersebar, antarmuka ditemukan saat integrasi, dan verifikasi adalah pengujian apa pun yang kebetulan sempat dilakukan. Program besar rutin melampaui jadwal dan mengejutkan tim di akhir.

**Tingkat 2: Mengembangkan.** Praktik dasar ada pada program utama. Persyaratan ditangkap dan di-baseline, antarmuka kunci punya dokumen kendali, dan ada rencana verifikasi. Praktik tidak konsisten antartim dan bergantung pada individu alih-alih metode bersama.

**Tingkat 3: Membakukan.** Rekayasa sistem adalah disiplin terdokumentasi seluruh organisasi yang selaras dengan ISO/IEC/IEEE 15288 dan ditegakkan lintas tim. Siklus hidup penuh direncanakan, keterlacakan dipelihara ujung ke ujung, antarmuka dikendalikan secara formal, dan verifikasi serta validasi berbeda dan terencana. MBSE dipakai pada program kompleks.

**Tingkat 4: Mengelola.** Rekayasa sistem diukur dan dikendalikan dengan data. Organisasi melacak metrik terhadap garis dasar: volatilitas persyaratan dan cakupan keterlacakan, cacat antarmuka yang ditemukan saat integrasi, tingkat lulus verifikasi dan validasi, serta kebocoran cacat menurut tahap siklus hidup (berapa banyak cacat lolos dari setiap tahap untuk tertangkap kelak dengan biaya lebih tinggi). Tinjauan mengarahkan program berdasarkan angka ini, dan ambang memicu tindakan korektif alih-alih pemadaman kebakaran setelah kejadian.

**Tingkat 5: Mengorkestrasi.** Rekayasa sistem terus diperbaiki dan terintegrasi di seluruh organisasi. Model MBSE yang hidup adalah satu sumber kebenaran, keterlacakan otomatis, simulasi memprediksi perilaku emergen sebelum dibangun, dan metrik dari program lalu memberi masukan ke program berikutnya. Perangkat keras dan lunak direkayasa bersama sebagai hal yang wajar, dan proses beradaptasi seiring bergesernya program, pemasok, dan risiko.

## Gagasan untuk didiskusikan

- Di mana garis antara rekayasa sistem dan arsitektur perangkat lunak di organisasi Anda, dan siapa yang memiliki ruang di antaranya?
- Pada program terbesar Anda, dapatkah Anda menelusuri satu kebutuhan pemangku kepentingan sampai ke tes yang memverifikasinya? Jika tidak, apa yang diperlukan?
- Kegagalan terbaru Anda yang mana yang terjadi pada antarmuka, dan siapa yang memilikinya?
- Akankah MBSE membuahkan hasil bagi Anda, atau menjadi shelfware mahal mengingat budaya dan perkakas Anda?
- Apakah rencana siklus hidup Anda sungguh-sungguh menangani operasi dan pensiun, atau diam-diam berhenti di peluncuran?

## Poin-poin utama

- Rekayasa sistem merekayasakan seluruh sistem (perangkat lunak, perangkat keras, manusia, dan proses) dari ujung ke ujung, dan berbeda dari arsitektur perangkat lunak.
- Rencanakan siklus hidup penuh, dari konsep lewat persyaratan, desain, integrasi, V&V, operasi, dan pensiun.
- Telusuri setiap kebutuhan ke persyaratan, elemen desain, dan tes, dan alokasikan setiap persyaratan ke bagian yang bertanggung jawab.
- Kelola antarmuka secara eksplisit dengan kepemilikan jelas dan dokumen kendali, karena batas adalah tempat sistem rusak.
- Verifikasi (membangunnya dengan benar) dan validasi (membangun hal yang benar) adalah pemeriksaan berbeda, dan Anda butuh keduanya.
- Pakai MBSE dan SysML untuk satu sumber kebenaran terhubung, dan pakai berpikir sistem untuk mengantisipasi perilaku emergen.
- Cocokkan bobot proses Anda dengan ukuran, umur, dan risiko sistem.

## Referensi dan bacaan lanjutan

- INCOSE, *INCOSE Systems Engineering Handbook: A Guide for System Life Cycle Processes and Activities*
- ISO/IEC/IEEE 15288, *Systems and Software Engineering: System Life Cycle Processes*
- ISO/IEC/IEEE 29148, *Systems and Software Engineering: Requirements Engineering*
- Sanford Friedenthal, Alan Moore, dan Rick Steiner, *A Practical Guide to SysML: The Systems Modelling Language*
- NASA, *NASA Systems Engineering Handbook* (NASA/SP-2016-6105)
- Andrew P. Sage dan William B. Rouse, *Handbook of Systems Engineering and Management*
- Dennis M. Buede dan William D. Miller, *The Engineering Design of Systems: Models and Methods*
- Donella H. Meadows, *Thinking in Systems: A Primer*
- Eberhardt Rechtin dan Mark W. Maier, *The Art of Systems Architecting*
- U.S. Department of Defence, *Defence Acquisition Guidebook* (panduan rekayasa sistem)
