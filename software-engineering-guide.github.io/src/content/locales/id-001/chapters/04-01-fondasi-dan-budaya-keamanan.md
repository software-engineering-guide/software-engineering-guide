# 4.1 Fondasi dan budaya keamanan

## Tinjauan dan motivasi

Keamanan bukan fitur yang Anda tempelkan di akhir, dan bukan tugas satu tim khusus yang duduk terpisah dari rekayasa. Dalam organisasi besar, keamanan adalah properti dari cara seluruh sistem dirancang, dibangun, dioperasikan, dan diatur. Ketika ribuan insinyur merilis kode di ratusan layanan, mata rantai terlemah menentukan seberapa besar kerusakan yang dapat ditimbulkan insiden. Satu bucket penyimpanan yang salah konfigurasi, satu dependensi yang belum ditambal, atau satu akun layanan dengan hak istimewa berlebih dapat mengekspos jutaan catatan. Fondasi dan budaya adalah yang mencegah hal itu terjadi pada skala besar.

Bagi enterprise, taruhannya finansial dan reputasional: biaya pembobolan, denda regulasi, pelanggan yang hilang, dan valuasi yang tertekan. Bagi pemerintah, taruhannya meluas hingga keamanan nasional, kepercayaan publik, dan kesinambungan layanan esensial. Kedua pengaturan berbagi kebenaran pahit: Anda tidak dapat menegakkan keamanan murni lewat kendali dan gerbang. Ia harus diinternalisasi oleh orang yang mengerjakannya. Budaya di mana insinyur memahami ancaman, merasa memiliki, dan dihargai karena menyuarakan kekhawatiran menghasilkan hasil jauh lebih baik daripada yang bersandar pada tim keamanan yang kelelahan berperan sebagai penjaga gawang.

Bab ini memaparkan model mental dan praktik budaya yang mendasari setiap bab keamanan lain dalam panduan ini. Ia mencakup menjadikan keamanan tugas semua orang, [pemodelan ancaman](https://en.wikipedia.org/wiki/Threat_model), siklus hidup pengembangan aman, prinsip arsitektural fondasional seperti [pertahanan berlapis](https://en.wikipedia.org/wiki/Defense_in_depth_(computing)) dan [zero trust](https://en.wikipedia.org/wiki/Zero_trust_security_model), dan cara memprioritaskan pekerjaan keamanan berdasarkan risiko nyata alih-alih ketakutan atau mode.

*Lihat juga:* bab 4.2 (keamanan aplikasi), bab 4.3 (keamanan infrastruktur dan cloud), bab 4.4 (operasi keamanan), dan bab 4.6 (kepatuhan dan tata kelola) dibangun di atas fondasi ini.

## Prinsip utama

- **Keamanan adalah tugas semua orang.** Setiap insinyur, manajer produk, dan operator memiliki keamanan dari apa yang mereka bangun. Tim keamanan memampukan, menasihati, dan mengaudit; ia tidak dan tidak bisa mengerjakan semuanya sendiri.
- **Asumsikan pembobolan.** Rancang seolah penyerang sudah berada di dalam. Minimalkan apa yang dapat dijangkau komponen yang terkompromi.
- **Pertahanan berlapis.** Tak ada kendali tunggal yang cukup. Lapisi kendali independen agar kegagalan satu tidak berarti kegagalan semuanya.
- **[Hak istimewa paling sedikit](https://en.wikipedia.org/wiki/Principle_of_least_privilege).** Beri akses minimum yang dibutuhkan, untuk waktu minimum, dan cabut secara otomatis ketika tak lagi dibutuhkan.
- **Geser ke kiri (shift left).** Temukan dan perbaiki masalah sedini mungkin, ketika paling murah diperbaiki.
- **Prioritisasi berbasis risiko.** Belanjakan upaya di tempat kombinasi kemungkinan dan dampak paling tinggi, dipandu triad CIA (kerahasiaan, integritas, dan ketersediaan), bukan pada apa pun yang jadi berita minggu ini.
- **Pembelajaran tanpa menyalahkan.** Perlakukan insiden keamanan dan nyaris-insiden sebagai peluang belajar, bukan kesempatan menghukum.

## Rekomendasi

### Dirikan program security champion

Tanamkan security champion yang ditunjuk di setiap tim rekayasa. Champion bukan spesialis keamanan penuh waktu. Mereka insinyur dengan pelatihan ekstra dan jalur langsung ke tim keamanan pusat. Mereka meninjau desain, menriase temuan, menjawab pertanyaan rekan, dan membawa konteks keamanan ke perencanaan. Ini menskalakan keahlian keamanan di seluruh organisasi tanpa merekrut spesialis untuk setiap tim, dan membangun kepercayaan, karena nasihat datang dari rekan yang benar-benar mengenal basis kode.

Beri champion dukungan nyata: forum rutin untuk berbagi apa yang mereka pelajari, anggaran untuk pelatihan dan konferensi, pengakuan dalam penilaian kinerja, dan waktu yang disisihkan dari komitmen pengiriman mereka. Program champion yang hanya ada di atas kertas tidak menghasilkan apa-apa.

### Praktikkan pemodelan ancaman secara rutin

Pemodelan ancaman adalah kebiasaan disiplin bertanya "apa yang bisa salah?" sebelum Anda membangun. Lakukan untuk layanan baru, fitur besar, dan setiap perubahan pada batas kepercayaan. Jaga cukup ringan agar benar-benar sering terjadi.

- **[STRIDE](https://en.wikipedia.org/wiki/STRIDE_model)** adalah daftar periksa praktis yang dipetakan ke properti keamanan: Spoofing (autentikasi), Tampering (integritas), Repudiation (non-repudiasi), Information disclosure (kerahasiaan), Denial of service (ketersediaan), dan Elevation of privilege (otorisasi). Telusuri setiap aliran data dan tanyakan bagaimana setiap kategori berlaku.
- **PASTA** (Process for Attack Simulation and Threat Analysis) adalah metode tujuh tahap yang lebih berat dan berpusat risiko yang mengikat ancaman teknis ke dampak bisnis; gunakan untuk sistem bernilai tinggi.
- **[Pohon serangan](https://en.wikipedia.org/wiki/Attack_tree)** menguraikan tujuan ("curi data pelanggan") menjadi langkah bercabang yang akan diambil penyerang, membantu Anda menemukan dan memangkas jalur.

Simpan model ancaman sebagai dokumen hidup di samping kode, dan tinjau ulang setiap kali arsitektur berubah.

### Bangun siklus hidup pengembangan perangkat lunak yang aman

Jalin keamanan ke setiap fase alih-alih memperlakukannya sebagai gerbang terakhir:

- **Persyaratan:** tangkap persyaratan keamanan dan privasi bersama yang fungsional.
- **Desain:** modelkan ancaman dan tinjau batas kepercayaan.
- **Implementasi:** tegakkan standar pengodean aman, tinjauan kode, dan pemindaian rahasia sebelum komit.
- **Pengujian:** jalankan [SAST](https://en.wikipedia.org/wiki/Static_application_security_testing) (static application security testing), [DAST](https://en.wikipedia.org/wiki/Dynamic_application_security_testing) (dynamic application security testing), dan pemindaian dependensi dalam pipeline (lihat bab 4.4).
- **Rilis:** verifikasi asal-usul, tanda tangani artefak, dan periksa konfigurasi.
- **Operasi:** pantau, tambal, dan tanggapi.

Inti shift-left bukan menumpuk semua pekerjaan lebih awal dan membebani insinyur. Melainkan menangkap jenis cacat yang jauh lebih murah diperbaiki di awal.

### Adopsi prinsip arsitektur zero-trust

Keamanan perimeter tradisional mengasumsikan segala yang di dalam jaringan dapat dipercaya. Asumsi itu gagal begitu penyerang mendapat pijakan. Zero trust menggantikan kepercayaan jaringan implisit dengan verifikasi eksplisit dan berkelanjutan: autentikasi dan otorisasi setiap permintaan berdasarkan identitas, postur perangkat, dan konteks, dari mana pun asalnya di jaringan. Padukan identitas kuat, otorisasi hak istimewa paling sedikit, mikrosegmentasi, dan [enkripsi](https://en.wikipedia.org/wiki/Encryption) di mana-mana. Zero trust adalah perjalanan, bukan produk, jadi dekati selangkah demi selangkah.

### Prioritaskan menurut risiko memakai triad CIA

Bingkai setiap aset dan kendali di sekitar **Kerahasiaan** (Confidentiality), **Integritas** (Integrity), dan **Ketersediaan** (Availability). Tidak semua data membutuhkan perlindungan yang sama: halaman pemasaran publik dan basis data rekam medis punya kebutuhan kerahasiaan yang sangat berbeda. Klasifikasikan aset Anda, perkirakan kemungkinan dan dampak kompromi, dan arahkan upaya keamanan yang langka ke kombinasi berisiko tertinggi. Tuliskan keputusan risiko Anda agar orang lain dapat meninjau dan mempertahankannya kelak.

## Trade-off: kelebihan dan kekurangan

| Pendekatan | Kelebihan | Kekurangan |
|---|---|---|
| Tim keamanan pusat memiliki semua keamanan | Keahlian dalam, standar konsisten | Hambatan, insinyur menjauh, tidak berskala |
| Keamanan terdistribusi (champion) | Berskala, membangun rasa memiliki, umpan balik lebih cepat | Butuh investasi, keterampilan tak merata, butuh koordinasi |
| Pemodelan ancaman berat di muka untuk semuanya | Teliti, menangkap cacat desain | Memperlambat pengiriman, dapat menjadi centang kotak |
| Pemodelan ancaman ringan, bertarget risiko | Cepat, berfokus pada yang penting | Mungkin melewatkan ancaman di sistem "berisiko rendah" |
| Gerbang ketat memblokir rilis | Menegakkan kepatuhan | Gesekan, mendorong siasat |

Ketegangan pusatnya adalah antara kecepatan dan jaminan. Condong terlalu jauh ke gerbang dan kendali pusat, dan Anda menciptakan gesekan yang dihindari insinyur, melahirkan shadow IT dan kebencian. Condong terlalu jauh ke otonomi tanpa dukungan, dan Anda mendapat keamanan yang tidak konsisten dan tak diaudit. Jawaban yang berkelanjutan adalah budaya kuat dengan pagar pembatas yang memampukan: otomatis di tempat Anda bisa, manusia di tempat penilaian dibutuhkan, dan selalu dijelaskan alih-alih sekadar dipaksakan.

## Pertanyaan untuk didiskusikan dengan tim Anda

1. **Sistem Anda yang mana yang layak mendapat pemodelan ancaman berat, dan siapa yang memutuskan tingkatnya?** Dalam properti besar Anda tidak dapat menjalankan analisis PASTA tujuh tahap pada setiap layanan, jadi Anda butuh aturan eksplisit kapan satu putaran STRIDE 30 menit cukup dan kapan sistem bernilai tinggi layak pemodelan mendalam yang digerakkan dampak bisnis. Tambatkan keputusan pada klasifikasi CIA Anda: sistem yang menyimpan catatan teregulasi, alur pembayaran, atau logika autentikasi berada di puncak, dan halaman pemasaran publik tidak. Untuk pekerjaan enterprise dan pemerintah, auditor akan meminta Anda membela mengapa sistem tertentu dimodelkan seperti itu, jadi tuliskan kriteria pentahapan dan namai pemilik yang menerapkannya. Bawa klasifikasi aset Anda saat ini dan daftar layanan tanpa model ancaman ke rapat, karena kesenjangan di antaranya adalah risiko nyata Anda. Jika Anda tidak dapat bersepakat tentang standarnya, Anda akan bawaan memodelkan semuanya secara ringan atau tidak ada yang secara mendalam, dan keduanya mengecewakan Anda.

2. **Ketika security champion dan tenggat pengiriman bertabrakan, siapa yang benar-benar dapat menghentikan rilis?** Program champion hanya mengubah hasil jika champion membawa wewenang nyata, bukan sekadar pelatihan ekstra dan niat baik. Putuskan sebelumnya apakah champion dapat memblokir rilis, apakah mereka mengeskalasi ke tim AppSec pusat, dan tingkat keparahan temuan apa yang membenarkan menghentikan pengiriman versus melacaknya. Ini paling penting di bawah tekanan, ketika manajer produk ingin mengesampingkan cacat desain seminggu sebelum peluncuran, yang persis ketika cacat yang tak tertangani paling mahal diperbaiki. Bawa contoh terbaru di mana kekhawatiran keamanan bertemu tenggat dan telusuri siapa yang memutuskan dan bagaimana, karena kisah itu mengungkap jalur eskalasi Anda yang sebenarnya. Jika jawaban jujurnya adalah pengiriman selalu menang, champion Anda dekoratif dan Anda harus memperbaiki insentif sebelum menambah lebih banyak.

3. **Apa yang secara konkret diubah "asumsikan pembobolan" dalam tinjauan desain Anda berikutnya?** Prinsip ini mudah diangguki dan sulit dioperasionalkan, jadi kaitkan dengan komitmen spesifik: batas kepercayaan mana yang akan Anda kencangkan, di mana Anda akan menambah mikrosegmentasi, dan bagaimana Anda akan mengecilkan apa yang dapat dijangkau satu akun layanan terkompromi. Bagi tim besar, imbalannya adalah pengurangan radius ledakan, sehingga penyerang yang mendarat di satu layanan tidak dapat berputar ke penyimpanan data di belakangnya. Dalam pengaturan enterprise dan pemerintah ini juga membentuk keputusan hak istimewa paling sedikit dan kredensial berumur pendek, yang murah dirancang masuk dan menyakitkan dipasang belakangan. Bawa satu diagram layanan nyata dan tanyakan apa yang dilakukan penyerang setelah menguasai tingkat web, lalu berkomitmen pada dua perubahan penahanan kuartal ini. Kesepakatan samar bahwa pembobolan terjadi tak berharga kecuali ia menggeser izin, aturan jaringan, atau masa hidup kredensial.

4. **Bagaimana Anda akan tahu budaya keamanan Anda benar-benar membaik, dan metrik mana yang akan Anda pertahankan di hadapan dewan?** Tingkat penyelesaian pelatihan dan jumlah tiket mudah dikumpulkan dan nyaris tak berguna, karena mengukur aktivitas alih-alih pengurangan risiko, dan organisasi besar tenggelam di dalamnya. Pilih metrik hasil yang benar-benar akan Anda pertaruhkan anggarannya: median waktu memperbaiki temuan keparahan tinggi, bagian layanan yang membawa model ancaman terkini, pecahan insiden yang tertangkap sebelum produksi, dan tingkat nyaris-insiden yang dilaporkan sendiri, yang harus naik seiring kepercayaan tumbuh alih-alih turun. Pertimbangan yang bersaing adalah bahwa setiap metrik yang baik dapat dimanipulasi, jadi pasangkan masing-masing dengan kontra-metrik dan tinjau tren alih-alih potret. Bawa dasbor Anda saat ini dan tanyakan angka mana yang akan berubah jika keamanan benar-benar memburuk; yang tidak berubah adalah dekorasi. Dalam pengaturan enterprise dan pemerintah, regulator atau komite audit akan meminta bukti bahwa kendali berfungsi, jadi pilih metrik yang dapat Anda pertahankan di bawah pengawasan alih-alih yang sekadar tampak hijau.

5. **Apa yang sebenarnya terjadi ketika insinyur berikutnya melaporkan kesalahan, dan apakah proses Anda tanpa menyalahkan dalam praktik atau hanya di slide?** Pembelajaran tanpa menyalahkan adalah prinsip yang paling sering diakui dan paling jarang dihidupi, karena insiden serius pertama menguji apakah pimpinan sungguh-sungguh. Putuskan sebelumnya bagaimana Anda memisahkan akuntabilitas memperbaiki masalah dari hukuman karena menyebabkannya, dan siapa yang memimpin tinjauan pasca-insiden agar tetap tentang sistem yang rusak alih-alih individu yang disebut namanya. Ketegangannya nyata: pemangku kepentingan ingin seseorang dimintai tanggung jawab, namun menghukum pelapor menjamin kesalahan berikutnya tetap tersembunyi sampai menjadi pembobolan. Bawa dua tinjauan insiden terakhir Anda dan periksa apakah mereka menyalahkan orang atau kendali, dan apakah insinyur yang membunyikan alarm diberi terima kasih atau diam-diam disisihkan. Untuk pemerintah dan enterprise teregulasi, aturan pengungkapan pembobolan wajib menaikkan taruhan lebih jauh, karena budaya yang menyembunyikan kesalahan juga akan melewatkan tenggat pelaporan yang membawa penalti hukum.

6. **Siapa yang memiliki gesekan perkakas shift-left Anda, dan apakah Anda membelinya, membangunnya, atau tenggelam di dalamnya?** Analisis statis dan dinamis otomatis, pemindaian dependensi, dan pemindaian rahasia adalah tulang punggung siklus hidup pengembangan aman, tetapi pipeline yang membanjiri insinyur dengan positif palsu mengajari mereka mengabaikan keluaran keamanan, yang lebih buruk daripada tanpa pemindaian sama sekali. Putuskan siapa yang menyetel perkakas, siapa yang menriase temuan, dan apakah Anda membeli platform terintegrasi atau merakit pemindai sumber terbuka yang kemudian harus Anda pelihara sendiri. Pertimbangan yang bersaing adalah cakupan versus derau dan kendali versus biaya: pemindai murah yang berteriak serigala membakar kepercayaan yang dibangun program champion selama bertahun-tahun. Bawa tingkat positif palsu Anda saat ini, waktu rata-rata insinyur menunggu pemeriksaan pemblokir, dan daftar tim yang diam-diam menonaktifkan gerbang. Di enterprise besar dan pemerintah, tambahkan sudut pengadaan dan sebaran perkakas, karena sepuluh tim yang masing-masing membeli pemindai sendiri menghasilkan cakupan tidak konsisten yang tidak dapat direkonsiliasi auditor mana pun.

## Lensa sektor

**Startup.** Tanpa tim keamanan dan dengan landasan pendek, budaya adalah satu-satunya kendali yang terjangkau. Jadikan papan tulis pemodelan ancaman 30 menit sebagai kebiasaan sebelum fitur apa pun yang menyentuh autentikasi atau pembayaran, nyalakan hak istimewa paling sedikit dan MFA di mana-mana karena tak berbiaya, dan pelihara saluran tanpa menyalahkan di mana siapa pun dapat menandai kekhawatiran. Lewati proses dan perkakas berat; insinyur pendiri tidak dapat memeliharanya, dan disiplin yang Anda bangun sekarang adalah yang memungkinkan pembeli enterprise memercayai Anda kelak.

**Bisnis kecil.** Anda tidak punya spesialis keamanan khusus dan anggaran ketat, jadi bersandarlah pada bawaan aman dalam perkakas yang sudah Anda beli alih-alih mendirikan pipeline sendiri. Pilih platform terkelola yang menegakkan MFA, penambalan, dan hak istimewa paling sedikit untuk Anda, dan perlakukan keamanan sebagai pertanyaan kebersihan data: ketahui data sensitif apa yang Anda pegang dan siapa yang dapat menjangkaunya. Ketika harus memilih bangun versus beli, belilah, karena kendali terkelola yang Anda jaga mutakhir mengalahkan yang pesanan yang Anda biarkan membusuk.

**Enterprise.** Pada skala ratusan layanan dan ribuan insinyur, tantangannya konsistensi dan tata kelola di banyak tim. Jalankan program security champion, bakukan tingkat pemodelan ancaman yang terkait klasifikasi CIA, dan sediakan templat jalan-beraspal serta pemeriksaan pipeline otomatis agar setiap tim mewarisi bawaan yang baik. Lacak metrik remediasi dan cakupan terhadap garis dasar, dan simpan jejak audit yang menunjukkan mengapa setiap sistem dimodelkan dan dikendalikan seperti itu.

**Pemerintah.** Aturan pengadaan, kewajiban transparansi, dan akuntabilitas publik membentuk setiap pilihan. Prinsip zero-trust dan kredensial berumur pendek sering diwajibkan oleh kebijakan eksekutif, dan Anda harus dapat menunjukkan kepada auditor rasionalisasi berbasis risiko yang terdokumentasi tentang ke mana anggaran pengerasan pergi. Prioritaskan lebih dulu sistem yang menyimpan catatan warga paling sensitif, terbitkan pengamanan di tempat publik berhak tahu, dan wajibkan vendor mengungkap keterbatasan alih-alih menerima kotak hitam buram.

## Contoh

**Startup.** Sebuah startup sepuluh orang tidak punya tim keamanan dan tidak ada anggaran untuknya, jadi dua insinyur pendiri menjadikan pemodelan ancaman kebiasaan papan tulis 30 menit sebelum fitur apa pun yang menyentuh autentikasi atau pembayaran, bertanya apa yang bisa salah dan siapa yang menginginkannya terjadi. Mereka mengadopsi beberapa kebiasaan fondasional yang tak berbiaya: hak istimewa paling sedikit pada setiap peran cloud, MFA pada setiap akun, dan saluran tanpa menyalahkan di mana siapa pun dapat menyuarakan kekhawatiran tanpa takut disalahkan. Ketika kemudian menggalang putaran dan pembeli enterprise bertanya bagaimana mereka menangani keamanan, budaya awal itu memungkinkan mereka menjawab dengan jujur alih-alih kalang kabut menciptakannya.

**Enterprise.** Sebuah bank global dengan 6.000 insinyur menjalankan program security champion dengan satu champion terlatih per skuad. Champion menghadiri guild bulanan, menyelesaikan pelatihan kuartalan, dan memimpin pemodelan ancaman untuk setiap layanan baru memakai STRIDE. Tim AppSec pusat memelihara templat jalan-beraspal dan pemeriksaan pipeline otomatis. Selama dua tahun, median waktu memperbaiki temuan keparahan tinggi turun dari 45 hari menjadi 9, dan pemodelan ancaman tahap desain menangkap cacat otorisasi pada API pembayaran sebelum mencapai produksi, menghindari insiden yang kemungkinan harus dilaporkan.

**Pemerintah.** Sebuah otoritas pajak nasional yang memodernisasi sistem warisan mengadopsi prinsip zero-trust yang diwajibkan oleh kebijakan eksekutif. Setiap panggilan layanan internal diautentikasi dengan kredensial berumur pendek dan diotorisasi per permintaan; segmen jaringan tidak lagi memberi kepercayaan. Otoritas memodelkan ancaman setiap layanan yang menghadap warga terhadap pohon serangan yang berakar pada "eksfiltrasi catatan wajib pajak" dan "ubah pengajuan." Prioritisasi berbasis risiko, selaras dengan tingkat dampak CIA, memusatkan anggaran pengerasan lebih dulu pada sistem yang menyimpan catatan paling sensitif.

## Kasus bisnis: motivasi, ROI, dan TCO

Biaya membangun budaya keamanan nyata: waktu champion, pelatihan, perkakas, dan beban sederhana melakukan pemodelan ancaman dan tinjauan. Tetapi biaya itu kecil dibanding biaya tidak melakukannya. Rata-rata pembobolan data besar mencapai jutaan begitu Anda menghitung investigasi, notifikasi, remediasi, denda regulasi, paparan hukum, dan bisnis yang hilang. Pembobolan pemerintah menambah gangguan misi dan erosi kepercayaan publik yang tak sepenuhnya tertangkap faktur mana pun.

Imbal hasil investasi keamanan datang dari tiga tempat: **insiden yang dihindari** (pembobolan yang tak pernah terjadi), **biaya remediasi yang berkurang** (cacat yang diperbaiki pada waktu desain berbiaya sebagian kecil dari yang diperbaiki di produksi), dan **pengiriman lebih cepat** (jalan-beraspal dan pemeriksaan otomatis memungkinkan tim merilis dengan keyakinan alih-alih menunggu tinjauan manual). Ketika mengajukan kasus kepada pimpinan, bingkai keamanan sebagai manajemen risiko dengan label harga, bukan kebaikan abstrak. Tunjukkan kerugian yang diharapkan (kemungkinan kali dampak) dari risiko teratas, biaya untuk menguranginya, dan risiko yang masih tersisa. Eksekutif mendanai pengurangan risiko yang dapat mereka ukur.

## Anti-pola dan jebakan

- **Teater keamanan.** Kendali yang tampak mengesankan tetapi tidak mengurangi risiko nyata, diadopsi untuk memuaskan audit alih-alih melindungi apa pun.
- **Tim keamanan sebagai gerbang di akhir.** Menemukan cacat desain seminggu sebelum peluncuran, ketika paling mahal diperbaiki dan paling mungkin dikesampingkan.
- **Budaya menyalahkan.** Menghukum insinyur yang melaporkan kesalahan menjamin kesalahan berikutnya tetap tersembunyi.
- **Pemodelan ancaman centang kotak.** Mengisi templat yang tak dibaca siapa pun, menghasilkan dokumen yang terlepas dari arsitektur nyata.
- **Kendali satu-ukuran-untuk-semua.** Menerapkan proses berat yang sama pada situs web publik dan sistem pembayaran, membuang upaya dan melahirkan kebencian.
- **Prioritisasi digerakkan ketakutan.** Mengejar kerentanan apa pun yang sedang tren di berita alih-alih yang benar-benar mengancam aset Anda.
- **Champion hanya nama.** Menamai champion tanpa memberi mereka waktu, pelatihan, atau wewenang.

## Model kematangan

**Tingkat 1: Memulai.** Keamanan reaktif dan terpusat. Tinjauan terjadi terlambat jika ada, dan tidak ada pemodelan ancaman. Insiden menggerakkan perbaikan ad hoc. Insinyur melihat keamanan sebagai masalah orang lain, dan tak ada standar bersama.

**Tingkat 2: Mengembangkan.** Tim keamanan ada dan mendefinisikan standar, tetapi praktik tidak konsisten antartim. Sebagian pemodelan ancaman terjadi pada proyek besar dan tidak pada yang lain. Pelatihan dasar tersedia. Keamanan masih dianggap gerbang, dan shift-left bersifat aspirasional alih-alih nyata.

**Tingkat 3: Membakukan.** Security champion tertanam di setiap tim. Pemodelan ancaman rutin untuk layanan baru, bertingkat terhadap klasifikasi CIA, dan siklus hidup pengembangan aman terdokumentasi serta ditegakkan di seluruh organisasi. Prioritisasi berbasis risiko memandu pekerjaan, standar pengodean aman dan pemeriksaan pipeline adalah jalan-beraspal bawaan, dan tinjauan pasca-insiden tanpa menyalahkan adalah norma.

**Tingkat 4: Mengelola.** Hasil keamanan diukur dan dikendalikan terhadap garis dasar. Organisasi melacak median waktu memperbaiki temuan keparahan tinggi, cakupan model ancaman, bagian insiden yang tertangkap sebelum produksi, dan tingkat pelaporan nyaris-insiden, dirinci per tim. Wewenang champion menghentikan rilis ditetapkan dan benar-benar dilaksanakan. Keputusan risiko dikuantifikasi sebagai kemungkinan kali dampak, dicatat, dan ditinjau pada irama tetap, sehingga celah kendali muncul sebagai data alih-alih kejutan.

**Tingkat 5: Mengorkestrasi.** Keamanan benar-benar tugas semua orang dan terintegrasi dengan pengiriman, risiko, dan perencanaan bisnis. Pemodelan ancaman dan desain aman adalah kebiasaan dan ringan, dan prinsip zero-trust sebagian besar terwujud. Metrik menggerakkan perbaikan berkelanjutan, organisasi belajar dari nyaris-insiden lintas tim, dan kendali beradaptasi otomatis seiring gambaran ancaman dan arsitektur berubah.

## Gagasan untuk didiskusikan

1. Bagaimana Anda mengukur apakah budaya keamanan benar-benar membaik, di luar menghitung penyelesaian pelatihan?
2. Di mana batas yang tepat antara apa yang ditangani security champion dan apa yang dimiliki tim pusat?
3. Bagaimana Anda menjaga pemodelan ancaman tetap berharga tanpa membiarkannya menjadi centang kotak birokratis?
4. Apakah arsitektur zero-trust penuh realistis untuk properti warisan Anda, dan jika tidak, apa subset pragmatisnya?
5. Bagaimana pekerjaan keamanan harus diprioritaskan terhadap pengiriman fitur ketika keduanya bersaing untuk insinyur yang sama?
6. Insentif apa yang benar-benar mengubah perilaku insinyur menuju kepemilikan keamanan?

## Poin-poin utama

- Keamanan adalah properti budaya organisasi besar, bukan tugas yang didelegasikan kepada satu tim.
- Security champion menskalakan keahlian dan rasa memiliki di seluruh rekayasa.
- Pemodelan ancaman (STRIDE, PASTA, pohon serangan) memunculkan cacat desain dengan awal dan murah.
- SDLC aman dan pola pikir shift-left menangkap cacat ketika biayanya paling kecil.
- Pertahanan berlapis, hak istimewa paling sedikit, dan zero trust adalah prinsip arsitektural fondasional.
- Triad CIA dan prioritisasi berbasis risiko mengarahkan upaya langka ke tempat yang paling penting.
- Biaya membangun budaya keamanan jauh lebih kecil daripada biaya pembobolan yang dicegahnya.

## Referensi dan bacaan lanjutan

- Adam Shostack, *Threat Modelling: Designing for Security*
- Ross Anderson, *Security Engineering: A Guide to Building Dependable Distributed Systems*
- Michael Howard dan Steve Lipner, *The Security Development Lifecycle*
- Betsy Beyer et al. (Google), *Building Secure and Reliable Systems*
- National Institute of Standards and Technology, *SP 800-207: Zero Trust Architecture*
- National Institute of Standards and Technology, *Secure Software Development Framework (SSDF), SP 800-218*
- OWASP, panduan *Threat Modelling* dan *Security Champions*
