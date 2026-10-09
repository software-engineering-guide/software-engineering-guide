# 8.5 Otomasi pengujian dan proses

## Tinjauan dan motivasi

Otomasi pengujian dan proses adalah praktik mengganti kerja rekayasa dan operasional yang berulang dan manual dengan alur kerja andal yang dieksekusi mesin. Di sisi pengujian, ini berarti [otomasi pengujian](https://en.wikipedia.org/wiki/Test_automation): rangkaian uji otomatis yang berjalan terus-menerus untuk memverifikasi kebenaran, kinerja, dan keamanan. Di sisi proses, ia meluas ke mesin di sekitar pengiriman dan operasi perangkat lunak: mengumpulkan bukti kepatuhan, mengeksekusi runbook operasional, meremediasi masalah yang diketahui, dan menegakkan kontrol tata kelola, keamanan, dan biaya. Gagasan pemersatunya sederhana. Apa pun yang dilakukan berulang dan dapat diprediksi harus dikodifikasi, agar berjalan konsisten, cepat, dan tanpa kerja membosankan manusia.

Bagi tim besar, otomasi adalah satu-satunya cara menjaga kualitas dan kendali agar tidak runtuh di bawah skala. Pengujian manual tidak dapat mengimbangi ratusan insinyur yang membuat ribuan perubahan. Ia menjadi hambatan, dan cakupannya menjadi tidak konsisten dan tak andal. Prosedur operasional manual juga menderita. Memulai ulang layanan, merotasi kredensial, dan mengumpulkan bukti audit semuanya menjadi lambat dan rawan galat ketika manusia lelah melakukannya di bawah tekanan di properti besar. Mengotomatisasi pekerjaan ini membuat hasil dapat diulang. Ia juga membebaskan insinyur terampil untuk berfokus pada masalah padat penilaian yang benar-benar membutuhkan wawasan manusia.

Dalam konteks enterprise dan pemerintah, otomasi juga kunci untuk membuat kepatuhan berkelanjutan. Organisasi teregulasi harus terus-menerus mendemonstrasikan bahwa kontrol ada dan bukti dikumpulkan. Melakukannya dengan tangan mahal, lambat, dan rawan celah. Mengotomatisasi pengumpulan bukti dan penegakan kontrol mengubah kepatuhan dari latihan kebakaran berkala menjadi properti sistem yang berkelanjutan dan dapat diverifikasi. Pendekatan "compliance as code" ini mengurangi biaya sekaligus memperkuat jaminan yang dibutuhkan auditor dan regulator.

## Prinsip utama

- Otomatiskan pekerjaan yang berulang, dapat diprediksi, dan berbasis aturan; sisihkan upaya manusia untuk penilaian.
- Jadikan uji otomatis cepat, andal, dan deterministik, atau mereka akan diabaikan.
- Jalankan uji secara paralel dan geser lebih awal agar umpan balik tetap cepat seiring rangkaian tumbuh.
- Kodifikasi prosedur operasional sebagai [runbook](https://en.wikipedia.org/wiki/Runbook)-as-code agar berversi, dapat diuji, dan dapat dieksekusi.
- Pilih otomasi yang terintegrasi baik daripada skrip rapuh yang ditempel ke sistem dari luar.
- Hasilkan bukti kepatuhan secara otomatis sebagai produk sampingan alur kerja normal.
- Jaga manusia dalam lingkaran untuk tindakan berisiko tinggi; otomatiskan yang aman dan rutin lebih dulu.

## Rekomendasi

### Bangun infrastruktur uji yang cepat, andal, dan paralel

Rangkaian uji hanya berharga jika insinyur memercayainya dan ia mengembalikan umpan balik dengan cepat. Berinvestasilah pada infrastruktur uji yang menjalankan rangkaian secara paralel di banyak pekerja, agar total waktu jam dinding tetap rendah bahkan ketika jumlah uji tumbuh hingga ribuan. Susun rangkaian sebagai piramida: banyak [unit test](https://en.wikipedia.org/wiki/Unit_testing) cepat, lebih sedikit uji integrasi, dan sejumlah kecil uji ujung ke ujung. Maka sebagian besar umpan balik tiba dalam hitungan detik. Hapuskan uji flaky tanpa ampun. Uji yang gagal sesekali lebih buruk daripada tanpa uji, karena melatih insinyur mengabaikan kegagalan. Sediakan lingkungan uji efemeral sesuai permintaan agar uji integrasi dan ujung ke ujung berjalan terhadap infrastruktur realistis dan terisolasi.

### Otomatiskan rilis, kepatuhan, dan pengumpulan bukti

Perluas otomasi melampaui pengujian ke alur kerja rilis dan kepatuhan. Minta pipeline otomatis menghasilkan artefak yang dibutuhkan auditor: catatan siapa yang menyetujui perubahan, uji apa yang berjalan dan lolos, apa yang ditemukan pemindaian keamanan, dan persis artefak mana yang di-deploy. Perlakukan kontrol sebagai kode, agar pemeriksaan wajib ditegakkan seragam dan hasilnya dicatat. "Compliance as code" ini mengubah pengumpulan bukti dari kerepotan manual sebelum audit menjadi catatan berkelanjutan yang selalu mutakhir. Ia juga membuat postur kepatuhan sistem dapat diamati kapan saja.

### Adopsi ChatOps dan runbook-as-code

Kodifikasi prosedur operasional sebagai runbook yang dapat dieksekusi dan disimpan dalam kontrol versi, alih-alih dokumen prosa yang menyimpang. Di mana prosedur aman dan dipahami baik, sambungkan ke otomasi yang dapat menjalankannya sesuai permintaan. ChatOps membawa operasi ini ke antarmuka obrolan bersama, agar operator memicu dan mengamati tindakan otomatis dalam percakapan yang transparan, kolaboratif, dan tercatat. Ini membuat operasi terlihat oleh seluruh tim dan menciptakan catatan otomatis tentang apa yang dilakukan. Ia juga menurunkan hambatan bagi insinyur kurang berpengalaman untuk menjalankan prosedur dengan aman, karena otomasi mengodekan langkah yang benar.

### Terapkan remediasi otomatis dengan hati-hati

Untuk masalah berulang yang dipahami baik, bangun remediasi otomatis yang mendeteksi kondisi dan menerapkan perbaikan yang diketahui, seperti memulai ulang proses gagal, menskalakan ke atas di bawah beban, membersihkan disk penuh, atau failover komponen. Mulailah dengan remediasi berisiko rendah dan berkeyakinan tinggi. Wajibkan konfirmasi manusia untuk apa pun dengan radius ledakan signifikan. Remediasi otomatis mengurangi mean time to recovery dan menghilangkan kelelahan peringatan berulang. Tetapi ia harus dibangun di atas deteksi yang solid dan menyertakan pengaman, karena otomasi yang bertindak atas sinyal palsu dapat memperkuat insiden. Catat setiap tindakan otomatis, agar operator mempertahankan visibilitas penuh dan dapat turun tangan.

### Tempatkan robotic process automation (RPA) dengan tepat

[Robotic process automation](https://en.wikipedia.org/wiki/Robotic_process_automation) menggerakkan antarmuka pengguna dan aplikasi yang ada untuk mengotomatisasi tugas, meniru klik dan ketikan yang akan dilakukan manusia. RPA punya tempat sah sebagai jembatan untuk sistem warisan atau pihak ketiga yang tak mengekspos API dan tak dapat diintegrasikan dengan cara lain. Pakai secara pragmatis untuk kasus semacam itu, tetapi ketahui batasnya. Otomasi berbasis UI secara inheren rapuh: ia patah setiap kali antarmuka berubah, dan tidak menangani kurangnya integrasi yang mendasarinya. Di mana API atau integrasi yang layak tersedia, pilih itu. Perlakukan RPA sebagai penyumbat taktis, bukan fondasi strategis, dan rencanakan menggantinya seiring sistem dimodernisasi.

### Otomatiskan kontrol tata kelola, keamanan, dan biaya

Kodekan kontrol organisasi sebagai pemeriksaan otomatis yang berjalan terus-menerus: policy-as-code untuk guardrail infrastruktur, pemindaian keamanan otomatis dalam pipeline, dan deteksi otomatis anomali biaya dan sumber daya menganggur. Mengotomatisasi tata kelola membuat kontrol seragam dan tak dapat dilewati, dan berskala ke volume perubahan yang tak pernah dapat dicakup tinjauan manual. Pendekatan yang sama yang menegakkan kebijakan keamanan dapat menandai tagihan cloud liar atau tag wajib yang hilang. Tata kelola bergeser dari audit manual berkala menjadi guardrail otomatis berkelanjutan.

## Trade-off: kelebihan dan kekurangan

| Pilihan | Kelebihan | Kekurangan | Paling cocok |
|---|---|---|---|
| Pengujian otomatis luas | Umpan balik cepat dan konsisten; memungkinkan perubahan | Biaya bangun dan pemeliharaan; risiko flakiness | Semua tim pada skala besar |
| Compliance as code | Bukti berkelanjutan dan siap audit | Rekayasa di muka untuk mengodifikasi kontrol | Organisasi teregulasi |
| Runbook-as-code + ChatOps | Operasi dapat diulang, terlihat, dan tercatat | Upaya mengodifikasi dan memelihara | Tim dengan beban ops nyata |
| Remediasi otomatis | Pemulihan lebih cepat; kerja membosankan lebih sedikit | Risiko jika deteksi salah | Masalah berulang yang dipahami baik |
| RPA (otomasi UI) | Menjembatani sistem tanpa API | Rapuh; menutupi celah integrasi | Sistem warisan sebagai penyumbat |
| Tata kelola otomatis | Kontrol seragam dan tak dapat dilewati | Upaya penulisan dan penyetelan kebijakan | Properti besar yang diatur |

Trade-off sentralnya adalah investasi di muka versus kerja membosankan dan risiko berkelanjutan. Otomasi selalu memakan upaya untuk dibangun dan dipelihara. Otomasi yang dibangun buruk, entah uji flaky, RPA rapuh, atau remediasi yang dipicu sinyal buruk, dapat lebih buruk daripada tanpa otomasi, karena mengikis kepercayaan atau memperkuat kegagalan. Disiplinnya tiga lipat: otomatiskan yang benar-benar dapat diulang dan andal, berinvestasilah membuat otomasi itu tepercaya, dan jaga manusia dalam lingkaran di mana penilaian atau risiko tinggi menuntut. Dilakukan dengan baik, otomasi terbayar berkali-kali lipat. Dilakukan sembrono, ia menjadi liabilitas tersendiri.

## Pertanyaan untuk didiskusikan dengan tim Anda

1. **Apakah uji integrasi dan ujung ke ujung Anda berjalan terhadap lingkungan realistis dan efemeral, atau terhadap kotak staging bersama yang diperebutkan semua orang?** Lingkungan terisolasi sesuai permintaan per pull request memungkinkan uji integrasi dan ujung ke ujung memakai infrastruktur realistis tanpa tim saling memblokir atau mencemari status bersama. Satu lingkungan staging bersama menjadi hambatan dan sumber kegagalan flaky yang bergantung urutan seiring lebih banyak tim menumpuk. Putuskan apakah Anda dapat menyalakan lingkungan efemeral, berapa biayanya, dan uji mana yang benar-benar membutuhkannya versus pengganti dalam-memori yang cepat. Bawa data: seberapa sering staging diperebutkan, berapa kegagalan ditelusuri ke interferensi lingkungan bersama, dan waktu jam dinding saat ini untuk tingkat integrasi. Jawabannya membentuk baik keandalan uji Anda maupun seberapa cepat lapisan atas piramida mengembalikan umpan balik.

2. **Apakah prosedur operasional dikodifikasi sebagai runbook-as-code dan dimunculkan lewat ChatOps, atau masih hidup sebagai prosa yang menyimpang?** Runbook terkodifikasi dan terkontrol versi dapat diuji dan dieksekusi, dan menjalankannya lewat antarmuka obrolan bersama membuat setiap tindakan terlihat dan tercatat otomatis. Itu menurunkan hambatan bagi insinyur on-call yang kurang berpengalaman untuk bertindak dengan aman, karena otomasi mengodekan langkah yang benar alih-alih bergantung pada pengetahuan suku. Putuskan prosedur mana yang cukup aman dan dipahami baik untuk disambungkan lebih dulu, dan bagaimana Anda menjaga manusia tetap mampu turun tangan. Untuk properti besar transparansi ini berfungsi ganda sebagai catatan audit tentang siapa melakukan apa dan kapan. Bawa runbook Anda saat ini, catat mana yang basi, dan identifikasi dua atau tiga prosedur yang paling sering dijalankan untuk dikodifikasi lebih dulu.

3. **Dalam pipeline Anda, pemindaian keamanan dan pemeriksaan kebijakan mana yang memblokir merge, dan mana yang hanya memperingatkan?** Tata kelola otomatis layak dibangun hanya jika kontrolnya tak dapat dilewati, karena pemeriksaan yang hanya memperingatkan diabaikan di bawah tekanan tenggat persis seperti kebijakan wiki. Putuskan, kontrol demi kontrol, apa yang memblokir dan apa yang memperingatkan: kerentanan kritis atau tag enkripsi yang hilang mungkin memblokir, sementara temuan gaya berkeparahan lebih rendah mungkin memperingatkan. Pada skala besar inilah cara Anda menegakkan guardrail keamanan dan biaya secara seragam atas volume perubahan yang tak dapat dicakup tinjauan manual. Bawa inventaris pemeriksaan Anda saat ini dan tandai masing-masing sebagai memblokir atau anjuran, lalu diskusikan tingkat positif palsu, karena pemeriksaan pemblokir yang berisik melatih orang menuntut pengecualian. Garis antara blokir dan peringatan adalah di mana tata kelola Anda punya gigi atau tidak.

4. **Remediasi otomatis mana yang bersedia kita biarkan bertindak tanpa konfirmasi manusia lebih dulu, dan apa radius ledakannya jika deteksi salah?** Remediasi otomatis memangkas waktu pemulihan dan kelelahan peringatan, tetapi perbaikan yang dipicu sinyal palsu dapat mengubah gangguan kecil menjadi pemadaman penuh, sehingga keputusan apa yang berjalan tanpa pengawasan adalah keputusan risiko, bukan kenyamanan. Timbang tarikan yang bersaing: tindakan tanpa pengawasan tercepat tetapi paling berisiko, sementara konfirmasi manusia-dalam-lingkaran lebih aman tetapi memperkenalkan kembali penundaan dan kerja membosankan yang hendak Anda hilangkan. Bawa remediasi kandidat yang diperingkat menurut frekuensi dan radius ledakan terburuk, tingkat positif palsu historis deteksi di balik masing-masing, dan apakah setiap tindakan tercatat dan dapat dibalik. Untuk properti enterprise atau pemerintah besar, tambahkan otoritas perubahan formal dan rencana rollback untuk apa pun yang menyentuh data produksi atau layanan menghadap warga, karena remediasi otomatis yang tak dapat diaudit atau dibatalkan adalah yang akan dipaksa regulator untuk Anda matikan.

5. **Bagaimana kita mendanai dan menetapkan kepemilikan untuk memelihara otomasi kita agar tidak membusuk menjadi liabilitas?** Uji, runbook, pemeriksaan kebijakan, dan bot RPA semuanya membusuk seiring sistem di sekitarnya berubah, dan otomasi yang terabaikan lebih buruk daripada tanpa otomasi: runbook basi memberi keyakinan palsu dalam krisis dan bot RPA yang rusak diam-diam menjatuhkan pekerjaan. Ketegangannya adalah pemeliharaan bersaing dengan kerja fitur untuk insinyur yang sama, dan ia tak terlihat sampai sesuatu rusak, sehingga menjadi yang pertama dipotong di bawah tekanan tenggat. Bawa inventaris aset otomasi saat ini, tumpukan uji flaky dan bot rusak, dan perkiraan jujur jam-insinyur yang sudah tercurah untuk pemeliharaan versus yang dianggarkan. Dalam pengaturan enterprise atau pemerintah, namai pemilik akuntabel untuk setiap otomasi kritis dan danai pemeliharaannya sebagai butir baris eksplisit, karena auditor dan tinjauan insiden akan bertanya siapa yang bertanggung jawab ketika kontrol tak terpelihara gagal secara senyap.

6. **Untuk setiap sistem warisan yang kita otomatisasi dengan RPA, apa rencana konkret dan pemicu untuk memensiunkan RPA itu demi integrasi nyata?** RPA adalah jembatan sah untuk sistem yang tak mengekspos API, tetapi jembatan tanpa rencana keluar diam-diam mengeras menjadi infrastruktur permanen yang rapuh yang patah pada setiap perubahan UI dan mengakarkan celah integrasi yang dimaksudkan untuk dijembatani. Trade-off-nya nyata: RPA memberi nilai cepat dan murah sekarang, sedangkan integrasi API yang layak berbiaya lebih di muka tetapi tahan lama, jadi disiplinnya adalah memperlakukan RPA sebagai pinjaman bertanggal, bukan pembelian. Bawa daftar bot RPA di produksi, sistem yang diandalkan masing-masing, seberapa sering masing-masing rusak, dan apakah upaya modernisasi atau integrasi benar-benar didanai dan dijadwalkan untuk sistem yang mendasarinya. Untuk properti enterprise dan pemerintah yang memikul aplikasi inti berusia puluhan tahun, kaitkan setiap bot RPA dengan tonggak modernisasi bernama, karena RPA yang diam-diam menjadi kritis tanpa tanggal pensiun adalah utang teknis yang bertambah setiap tahun antarmuka yang dikikisnya terus berubah.

## Lensa sektor

**Startup.** Dengan dua atau tiga insinyur dan tanpa waktu membangun infrastruktur, jaga piramida uji kecil dan cepat yang berjalan dalam beberapa menit pada setiap perubahan, dan perlakukan uji flaky mana pun sebagai bug nyata untuk diperbaiki atau dihapus minggu itu. Lewati perkakas kepatuhan berat dan policy-as-code yang belum Anda butuhkan, dan kodifikasi hanya dua atau tiga perbaikan operasional yang paling sering dijalankan sebagai skrip sederhana yang dipicu dari obrolan. Otomatiskan apa yang menghilangkan kerja membosankan harian, dan tahan godaan membangun mesin tata kelola sebelum Anda punya masalah tata kelola.

**Bisnis kecil.** Tanpa spesialis uji atau platform khusus, bersandarlah pada otomasi yang tertanam dalam perkakas yang sudah Anda bayar: pelari uji bawaan layanan CI, add-on pemindaiannya, dan lingkungan terkelola alih-alih pembangunan infrastruktur uji pesanan. Bingkai pilihan beli-versus-bangun di sekitar pemeliharaan yang dapat Anda pertahankan secara realistis, karena pipeline kustom cerdas yang tak dapat dipelihara siapa pun adalah hasil lebih buruk daripada yang lebih polos dan ter-hosting. Pakai RPA hemat dan hanya di mana perkakas vendor menjembatani sistem yang tak dapat Anda integrasikan dengan cara lain.

**Enterprise.** Lintas banyak tim tujuannya kontrol seragam dan tak dapat dilewati pada skala yang tak dapat dicakup tinjauan manual: infrastruktur uji paralel bersama dengan lingkungan efemeral, guardrail policy-as-code, dan bukti kepatuhan yang dihasilkan otomatis dari setiap proses pipeline. Bakukan antarmuka agar tim memakai ulang perkakas remediasi dan runbook alih-alih masing-masing menciptakan ulang skrip rapuh, dan kelola otomasi sebagai portofolio yang dimiliki dan didanai dengan anggaran pemeliharaan jelas. Waspadai agar pemeriksaan yang hanya memperingatkan di satu tim tidak diperlakukan sebagai memblokir di tim lain, karena penegakan tidak konsisten merusak jaminan yang Anda bayar.

**Pemerintah.** Aturan pengadaan, kewajiban transparansi, dan mandat pemantauan berkelanjutan menjadikan compliance as code nyaris esensial: setiap proses pipeline harus mencatat kontrol yang diperiksa, pemindaian yang dilakukan, dan persetujuan yang diberikan sebagai bukti siap audit yang tahan-rusak. Pilih otomasi terbuka dan portabel daripada lock-in proprietari agar kontrak mendatang dapat pindah ke pemasok lain, dan jaga manusia akuntabel untuk remediasi apa pun yang menyentuh layanan menghadap warga. Di mana sistem berusia puluhan tahun memaksa RPA, dokumentasikan sebagai jembatan sengaja dan sementara dengan rencana modernisasi publik, dan pegang pemeriksaan tata kelola pada baseline keamanan wajib pada setiap perubahan.

## Contoh

**Startup.** Startup tujuh orang menjaga piramida uji ramping yang sebagian besar uji unit cepat plus beberapa uji integrasi, semuanya berjalan paralel sehingga rangkaian penuh selesai dalam kurang dari tiga menit pada setiap pull request. Ketika uji mulai flaky, mereka memperlakukannya sebagai bug nyata dan memperbaiki atau menghapusnya minggu itu, karena dengan tim sekecil itu satu build merah yang diabaikan akan mengikis kepercayaan pada seluruh rangkaian. Mereka juga mengodifikasi dua perbaikan operasional tersering, memulai ulang worker macet dan membersihkan disk penuh, sebagai skrip kecil yang dipicu dari Slack, sehingga siapa pun yang on-call dapat menjalankannya dengan aman tanpa memanggil satu insinyur yang menulisnya.

**Enterprise.** Sebuah perusahaan e-commerce besar menjalankan rangkaian uji puluhan ribu uji, diparalelkan di armada pekerja sehingga rangkaian penuh selesai dalam menit. Lingkungan efemeral menyala per pull request untuk pengujian integrasi realistis. Operasi berjalan lewat ChatOps: insinyur on-call memicu runbook terkodifikasi dari obrolan, dan kegagalan umum seperti layanan kelebihan beban diremediasi otomatis, dengan tindakan dicatat untuk ditinjau. Pipeline mengumpulkan bukti pemindaian keamanan dan persetujuan secara otomatis, sehingga audit tahunan bersumber dari catatan yang selalu mutakhir alih-alih perburuan bukti manual.

**Pemerintah.** Sebuah lembaga publik yang tunduk pada persyaratan pemantauan berkelanjutan ketat menerapkan compliance as code. Setiap proses pipeline mencatat kontrol yang diperiksa, pemindaian yang dilakukan, dan persetujuan yang diberikan, menghasilkan bukti tahan-rusak yang memuaskan auditor sesuai permintaan. Karena salah satu sistem intinya adalah aplikasi berusia puluhan tahun tanpa API, lembaga memakai RPA sebagai jembatan sengaja untuk mengotomatisasi entri data ke dalamnya sementara upaya modernisasi berjalan, dengan rencana eksplisit untuk memensiunkan RPA begitu integrasi yang layak ada. Pemeriksaan tata kelola otomatis menegakkan baseline keamanan wajib pada setiap perubahan infrastruktur.

## Kasus bisnis: motivasi, ROI, dan TCO

ROI otomasi pengujian dan proses tampak sebagai waktu insinyur yang direklamasi, pengiriman lebih cepat dan aman, pemulihan insiden lebih cepat, dan biaya kepatuhan yang turun dramatis. Pengujian otomatis memungkinkan perubahan cepat dan percaya diri yang menopang kinerja pengiriman. Operasi dan remediasi otomatis memangkas kerja membosankan dan downtime yang menguras tim dan anggaran. Compliance as code dapat mengubah audit dari berminggu-minggu persiapan manual menjadi kueri rutin, penghematan finansial sekaligus reputasi.

Perbandingan TCO menimbang biaya berkelanjutan nyata membangun dan memelihara otomasi terhadap biaya tidak mengotomatisasi. Pengujian dan operasi manual tidak hanya berbiaya jam yang dihabiskan. Mereka juga berbiaya cacat yang lolos, insiden yang berjalan lama, audit yang menghabiskan staf spesialis, dan kelelahan insinyur yang mengerjakan kerja membosankan berulang. Bagi pimpinan, argumennya lugas: otomasi mengubah pengeluaran operasional dan risiko berulang menjadi investasi sekali-ditambah-pemeliharaan yang berskala, dan membuat kualitas serta kepatuhan berkelanjutan alih-alih episodik. Satu catatan layak dinyatakan terang-terangan. Otomasi harus dipelihara dan dipercaya; otomasi tak didanai dan terabaikan membusuk menjadi liabilitas.

## Anti-pola dan jebakan

- **Uji flaky ditoleransi.** Kegagalan sesekali menghancurkan kepercayaan dan melatih insinyur mengabaikan hasil merah.
- **Mengotomatisasi proses rusak.** Mengotomatisasi alur kerja buruk hanya membuat kekacauan terjadi lebih cepat; perbaiki prosesnya dulu.
- **RPA sebagai strategi.** Mengandalkan otomasi UI rapuh sebagai solusi permanen menutupi dan mengakarkan celah integrasi.
- **Remediasi tanpa deteksi solid.** Perbaikan otomatis yang dipicu sinyal buruk dapat memperkuat insiden.
- **Runbook sebagai prosa basi.** Prosedur yang hidup di dokumen usang memberi keyakinan palsu dalam krisis.
- **Bukti kepatuhan dikumpulkan manual.** Perburuan bukti manual berkala mahal dan meninggalkan celah di antara audit.
- **Tanpa manusia dalam lingkaran untuk tindakan berisiko tinggi.** Otomasi penuh operasi berbahaya menyingkirkan penilaian yang mencegah bencana.

## Model kematangan

**Tingkat 1, Memulai.** Pengujian dan operasi sebagian besar manual dan reaktif. Cakupan ad hoc, prosedur hidup di kepala orang atau dokumen basi, remediasi terjadi dengan tangan selama insiden, dan bukti kepatuhan dirakit dalam kerepotan sebelum setiap audit.

**Tingkat 2, Mengembangkan.** Uji otomatis ada tetapi lambat, flaky, atau berjalan tidak konsisten, dan praktik sangat bervariasi antartim. Beberapa skrip operasional dan runbook ada di kantong-kantong, tetapi remediasi masih manual dan tata kelola ditegakkan lewat tinjauan berkala alih-alih pemeriksaan berkelanjutan.

**Tingkat 3, Membakukan.** Infrastruktur uji yang cepat, paralel, dan andal adalah standar terdokumentasi seluruh organisasi. Runbook-as-code dan ChatOps dipakai umum, bukti kepatuhan dihasilkan otomatis dari proses pipeline, dan kontrol tata kelola berjalan sebagai pemeriksaan otomatis yang ditegakkan dan diterapkan konsisten lintas tim.

**Tingkat 4, Mengelola.** Otomasi itu sendiri diukur dan dikendalikan terhadap garis dasar. Anda melacak tingkat uji flaky, waktu jam dinding rangkaian, mean time to recovery untuk insiden yang diremediasi otomatis, pangsa kontrol dengan bukti otomatis, dan tingkat positif palsu pada pemeriksaan pemblokir, dan Anda memegang setiap metrik pada target yang disepakati. Keputusan remediasi dan cakupan digerakkan data ini, dan setiap tindakan otomatis dicatat agar tren dan regresi terlihat alih-alih ditebak.

**Tingkat 5, Mengorkestrasi.** Otomasi terus diperbaiki dan terintegrasi di seluruh organisasi. Remediasi otomatis menangani insiden rutin dengan pengaman terbukti, kepatuhan berkelanjutan dan selalu siap audit, dan rantai perkakas uji, ops, dan tata kelola beradaptasi seiring sistem berubah, dengan jembatan RPA aktif dipensiunkan seiring integrasi matang. Manusia berfokus pada penilaian sementara mesin menangani yang dapat diulang, dan seluruh sistem menyeimbangkan ulang atas bukti.

## Gagasan untuk didiskusikan

- Prosedur operasional mana yang aman untuk diotomatisasi penuh, dan mana yang harus menjaga manusia dalam lingkaran?
- Bagaimana Anda menjaga rangkaian uji besar tetap cepat dan bebas flake seiring ia tumbuh?
- Di mana RPA adalah jembatan yang dibenarkan untuk sistem warisan Anda, dan apa rencana memensiunkannya?
- Kontrol apa yang dapat Anda konversi dari audit manual ke compliance as code berkelanjutan lebih dulu?
- Bagaimana Anda membangun kepercayaan pada remediasi otomatis tanpa berisiko memperkuat insiden?
- Bagaimana Anda mendanai pemeliharaan berkelanjutan yang dibutuhkan otomasi agar tidak membusuk menjadi liabilitas?

## Poin-poin utama

- Otomatiskan yang berulang, dapat diprediksi, dan berbasis aturan; sisihkan upaya manusia untuk penilaian dan keputusan berisiko tinggi.
- Jadikan uji otomatis cepat, paralel, dan andal, dan hapuskan flakiness tanpa ampun.
- Kodifikasi operasi sebagai runbook-as-code dan munculkan lewat ChatOps untuk visibilitas dan catatan.
- Hasilkan bukti kepatuhan secara otomatis agar audit bersumber dari catatan berkelanjutan dan mutakhir.
- Pakai RPA hanya sebagai jembatan sengaja dan sementara untuk sistem tanpa API, dan rencanakan pensiunnya.
- Tegakkan kontrol tata kelola, keamanan, dan biaya sebagai pemeriksaan otomatis berkelanjutan, dengan manusia mengawasi tindakan berisiko.

## Referensi dan bacaan lanjutan

- Lisa Crispin dan Janet Gregory, *Agile Testing: A Practical Guide for Testers and Agile Teams*.
- Jez Humble dan David Farley, *Continuous Delivery*.
- Betsy Beyer, Chris Jones, Jennifer Petoff, dan Niall Richard Murphy (ed.), *Site Reliability Engineering* (lihat bab tentang menghilangkan toil).
- Gene Kim, Jez Humble, Patrick Debois, dan John Willis, *The DevOps Handbook*.
- Nicole Forsgren, Jez Humble, dan Gene Kim, *Accelerate*.
- NIST Special Publication 800-53 dan 800-137 (pemantauan berkelanjutan).
- Dokumentasi Open Policy Agent (policy as code).
