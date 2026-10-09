# 7.9 Manajemen data induk dan data referensi

## Tinjauan dan motivasi

Tanyakan kepada lima sistem berapa banyak pelanggan yang dimiliki organisasi, dan Anda mendapat lima angka berbeda. Satu menghitung alamat email, satu menghitung kontrak, satu menghitung login, dan dua berselisih tentang apakah "Acme Corp" dan "ACME Corporation" perusahaan yang sama. [Manajemen data induk](https://en.wikipedia.org/wiki/Master_data_management) (MDM) adalah disiplin merekonsiliasi entitas inti yang dibagi bisnis Anda, pelanggan, produk, pemasok, karyawan, lokasi, menjadi satu versi otoritatif yang dapat dipercaya setiap sistem.

Mulailah dengan memilah data Anda menjadi tiga jenis, karena mereka butuh perlakuan berbeda. Data induk mendeskripsikan kata benda bisnis Anda: orang, tempat, dan hal yang dirujuk banyak proses. Data referensi adalah kosakata terkendali yang dipakai proses itu: kode mata uang, kode negara, daftar satuan ukur, kategori produk. Data transaksional mencatat kata kerja: pesanan dibuat, pembayaran dilakukan, kiriman dikirim. Data induk dan referensi bervolume lebih rendah daripada transaksi tetapi dirujuk di mana-mana, sehingga galat di dalamnya mencemari segalanya di hilir.

Biaya salah menatanya konkret. Ketika pelanggan yang sama ada sebagai empat catatan yang sedikit berbeda, Anda mengirim empat katalog, Anda tak dapat melihat satu hubungan yang layak dipertahankan, dan angka pendapatan-per-pelanggan Anda diam-diam salah. [Golden record](https://en.wikipedia.org/wiki/Single_source_of_truth), versi tepercaya tunggal suatu entitas yang dirakit dari banyak sumber, adalah yang menggantikan salinan bertentangan itu, sehingga setiap integrasi berhenti menyelesaikan ulang masalah pencocokan yang sama.

Bagi enterprise yang merekonsiliasi sistem yang menumpuk selama puluhan tahun pertumbuhan dan akuisisi, MDM adalah beda antara pandangan pelanggan yang koheren dan pajak rekonsiliasi permanen. Bagi pemerintah, taruhannya naik: warga yang muncul sebagai tiga orang berbeda di tiga lembaga dapat ditolak tunjangan, dipajaki dua kali, atau hilang di antara departemen. Bab ini melengkapi strategi dan tata kelola data (bab 7.1), yang menetapkan kepemilikan dan kebijakan; pemodelan data dan lapisan semantik (bab 7.7), yang mendefinisikan apa arti entitas; dan kualitas dan observabilitas data (bab 7.8), yang menjaga catatan tetap bersih seiring waktu.

## Prinsip utama

- Pilah data Anda menjadi induk, referensi, dan transaksional; masing-masing butuh penanganan berbeda.
- Satu golden record per entitas dunia nyata, dirakit dengan sengaja, bukan ditemukan secara kebetulan.
- Pilih gaya arsitektur MDM agar sesuai kebutuhan kendali dan latensi Anda, bukan tren.
- Pencocokan dan survivorship adalah aturan bisnis, jadi tuliskan dan biarkan steward menyetelnya.
- Data referensi adalah kosakata bersama; versikan dan terbitkan seperti API.
- Tata kelola dan kepengurusan adalah mesin MDM; perangkat lunak hanya perkakasnya.
- Propagasikan golden record sebagai peristiwa agar sistem hilir tetap tersinkron, bukan basi.
- Ukur MDM dari keputusan yang diperbaiki dan duplikat yang dihapus, bukan catatan yang dimuat.

## Rekomendasi

### Klasifikasikan data induk, referensi, dan transaksional lebih dulu

Anda tak dapat mengelola apa yang belum Anda pilah, jadi mulailah dengan mengklasifikasikan ranah data Anda. Ujian berguna untuk data induk adalah apakah nilai salah merambat: jika satu alamat buruk beriak ke penagihan, pengiriman, dan pemberitahuan hukum, Anda sedang melihat data induk. Ini mengarahkan investasi Anda: Anda membangun mesin pencocokan untuk entitas pelanggan, bukan butir baris pesanan. Namai ranah secara eksplisit, peringkat menurut seberapa banyak nyeri yang ditimbulkan duplikasinya, dan mulailah dengan satu atau dua yang paling menyakitkan, biasanya pelanggan dan produk karena langsung menyentuh pendapatan.

### Pilih gaya arsitektur MDM dengan sengaja

Ada empat gaya arsitektur umum, dan yang tepat bergantung pada seberapa banyak otoritas yang dapat Anda pusatkan dan seberapa cepat perubahan harus merambat. Gaya registry membiarkan data di sistem sumber dan hanya membangun indeks pengenal yang cocok, sehingga ia dapat menjawab "kelima catatan ini adalah pelanggan yang sama" tanpa memindahkan data apa pun; murah dan berisiko rendah, tetapi hanya-baca, sehingga tak dapat memperbaiki sumber. Gaya konsolidasi menarik salinan ke hub pusat dan menggabungkannya menjadi golden record untuk pelaporan, tetapi tidak mendorong koreksi kembali, sehingga sumber tetap berantakan. Gaya koeksistensi melangkah lebih jauh: ia menyinkronkan nilai bersih kembali ke sistem sumber, sehingga sumber membaik seiring waktu sambil tetap beroperasi mandiri. Gaya hub terpusat atau transaksional menjadikan hub MDM sistem pencatat itu sendiri, di mana entitas dibuat dan disunting langsung dan setiap sistem lain mengonsumsi darinya; ini memberi konsistensi dan kendali terkuat, dan yang tersulit diadopsi karena mengubah di mana pekerjaan terjadi. Banyak organisasi berkembang dari registry yang membuktikan nilai menuju koeksistensi seiring kepercayaan tumbuh, dan menjalankan lebih dari satu gaya di ranah berbeda.

### Cocokkan, gabungkan, dan tetapkan aturan survivorship secara eksplisit

Inti MDM adalah memutuskan kapan dua catatan mendeskripsikan hal dunia nyata yang sama. Ini adalah [record linkage](https://en.wikipedia.org/wiki/Record_linkage), jarang sesederhana kecocokan kunci eksak karena data nyata penuh salah ketik, singkatan, dan bidang hilang. Pencocokan deterministik memakai aturan eksak pada bidang terpilih (ID pajak sama, atau email sama plus kode pos). Pencocokan probabilistik menilai kemiripan di banyak bidang memakai [pencocokan string aproksimasi](https://en.wikipedia.org/wiki/Approximate_string_matching) dan bobot, sehingga "Bob Smith, 12 Main St" dan "Robert Smith, 12 Main Street" dapat dinilai kemungkinan cocok di atas ambang. Memutuskan catatan mana yang merujuk entitas yang sama disebut resolusi identitas, dan ia menggerakkan segalanya dari pandangan pelanggan hingga deteksi penipuan.

Begitu catatan cocok, Anda harus memutuskan nilai mana yang bertahan ke golden record. Aturan survivorship ini adalah logika bisnis, jadi buat eksplisit: pilih nilai terbaru untuk nomor telepon, nilai terlengkap untuk alamat, sumber paling tepercaya untuk nama hukum. Tetapkan pita ambang di mana kecocokan digabung otomatis, pita lebih rendah di mana ditolak otomatis, dan pita tengah di mana manusia memutuskan, yang di sanalah kepengurusan tinggal. Jaga setiap penggabungan dapat dibalik dan tercatat, karena penggabungan salah yang menyatukan dua pelanggan nyata lebih buruk daripada kecocokan yang terlewat.

### Perlakukan data referensi sebagai kosakata bersama berversi

Data referensi adalah kosakata bersama yang dituturkan sistem Anda, dan kosakata yang menyimpang menyebabkan misalignment senyap: ketika satu sistem memakai kode negara ISO "GB" dan yang lain "UK," join gagal dan hitungan menyimpang. Pelihara setiap daftar referensi di satu tempat teratur, terbitkan untuk setiap konsumen, dan, yang krusial, versikan. Kode ditambah, dipensiunkan, dipecah, dan digabung seiring waktu, dan jika Anda menimpa daftar di tempat, Anda merusak laporan historis yang benar di bawah kode lama.

Perlakukan dataset referensi seperti API dengan kontrak. Terbitkan dengan tanggal efektif agar konsumen dapat bertanya "apa kode wilayah yang valid pada tanggal ini," simpan kode yang dipensiunkan alih-alih menghapusnya, dan catat pemetaan ketika kode berubah makna. Pilih standar eksternal yang diakui di mana ada, seperti kode negara dan mata uang ISO, karena standar memberi interoperabilitas gratis dan terhubung dengan disiplin standar terbuka di bab 3.8.

### Modelkan hierarki dan hubungan, bukan hanya catatan datar

Data induk bukan tumpukan baris independen; ia jaring hubungan. Pelanggan termasuk dalam rumah tangga dan induk korporat. Produk bergulir ke kategori dan merek. Hierarki ini membawa makna bisnis nyata: gulirkan penjualan menurut induk korporat dan gambaran berubah sepenuhnya dibanding menggulirkan menurut akun individual. Modelkan hubungan ini secara eksplisit agar konsumen menelusurinya secara konsisten alih-alih tiap tim menciptakan rollup sendiri.

Waspadai kasus di mana satu entitas membutuhkan beberapa hierarki sekaligus. Produk dapat bergulir satu cara untuk keuangan dan cara lain untuk merchandising, dan keduanya sah, jadi dukung beberapa hierarki bernama alih-alih memaksa satu pohon sejati. Hubungan antar ranah juga penting, seperti pemasok mana menyediakan produk mana.

### Sambungkan golden record ke lapisan semantik dan kualitas data

Golden record yang dihasilkan MDM adalah entitas tepercaya yang dirujuk lapisan semantik bab 7.7 ketika mendefinisikan metrik: "pelanggan aktif" bermakna hanya ketika "pelanggan" tidak ambigu. Beri makan golden record Anda ke lapisan semantik agar setiap metrik menghitung entitas terdeduplikasi dan terselesaikan yang sama.

MDM dan kualitas data (bab 7.8) adalah dua sisi satu koin: pemeriksaan kualitas mendeteksi duplikat, null, dan pelanggaran format yang kemudian diselesaikan MDM, dan pencocokan MDM memunculkan masalah kualitas yang terlewat pemeriksaan. Jalankan pemantauan kualitas berkelanjutan pada data induk Anda secara khusus: tingkat duplikat, distribusi keyakinan kecocokan, kelengkapan bidang kunci, dan ukuran antrean tinjauan, agar drift muncul sebelum konsumen melihatnya.

### Propagasikan golden record lewat peristiwa

Golden record yang tak terlihat sistem hilir mana pun tak membantu siapa pun. Pola terkuat adalah propagasi berbasis peristiwa: ketika entitas dibuat, digabung, atau dikoreksi, hub MDM menerbitkan peristiwa perubahan, dan sistem pelanggan memperbarui salinan lokal mereka. Ini dibangun di atas [arsitektur berbasis peristiwa](https://en.wikipedia.org/wiki/Event-driven_architecture) dan pola streaming bab 7.2, menjaga puluhan sistem tetap konsisten tanpa sinkronisasi batch malam yang rapuh yang membuat semua orang basi sehari.

Terbitkan peristiwa dengan konteks cukup agar berguna: pengenal entitas, apa yang berubah, nilai bertahan yang baru, dan versi agar konsumen dapat mengurutkan pembaruan dan mendeteksi yang terlewat. Jadikan konsumen idempoten agar memutar ulang peristiwa tak merugikan, dan tawarkan API untuk sistem yang tak dapat berlangganan. Prinsip dari arsitektur data dan penyimpanan (bab 3.4) berlaku: rancang agar golden record mengalir, karena yang tak dikonsumsi siapa pun hanyalah spreadsheet mahal.

### Tetapkan kepengurusan dan tata kelola sebelum perkakas

MDM gagal sebagai proyek teknologi dan berhasil sebagai proyek tata kelola. Peran kritisnya adalah [steward data](https://en.wikipedia.org/wiki/Data_steward), orang yang akuntabel atas kualitas dan aturan ranah tertentu, yang menyelesaikan kecocokan ambigu, menyetel aturan survivorship, dan menengahi ketika dua departemen berselisih tentang arti "pemasok." Steward biasanya orang bisnis dengan pengetahuan ranah mendalam, bukan insinyur, dan mereka butuh wewenang nyata dan waktu yang dialokasikan, karena kepengurusan paruh waktu tanpa mandat menghasilkan persis penyimpangan yang hendak dihentikan MDM.

Bungkus steward dalam struktur tata kelola dari bab 7.1: pemilik data yang akuntabel untuk setiap ranah, dewan untuk menyelesaikan sengketa lintas ranah, dan kebijakan jelas tentang siapa yang boleh membuat atau menggabungkan catatan induk. Dokumentasikan keputusan, karena aturan mencocokkan pelanggan adalah pengetahuan institusional yang harus selamat dari pergantian staf. Perkakas melayani tata kelola; membeli platform MDM sebelum Anda menamai steward Anda adalah membeli mesin tanpa pengemudi.

## Trade-off: kelebihan dan kekurangan

| Gaya MDM | Kelebihan | Kekurangan |
|---|---|---|
| Registry (hanya indeks) | Murah, berisiko rendah, sumber tak tersentuh | Hanya-baca; tak dapat memperbaiki data sumber |
| Konsolidasi (salinan pusat) | Catatan bersih untuk analitik dengan cepat | Sumber tetap berantakan; tanpa writeback |
| Koeksistensi (sinkron kembali ke sumber) | Sumber membaik; kendali seimbang | Lebih banyak integrasi; konflik sinkron untuk dikelola |
| Hub terpusat / transaksional | Konsistensi dan kendali terkuat | Biaya tertinggi; mengubah di mana pekerjaan terjadi |
| Pencocokan deterministik | Dapat diprediksi, dapat dijelaskan, dapat diaudit | Melewatkan salah ketik, varian, dan data berantakan |
| Pencocokan probabilistik | Menangkap variasi dunia nyata | Butuh penyetelan; penggabungan salah jika ceroboh |

Ketegangan sentral dalam MDM adalah kendali versus gangguan. Gaya yang memberi data paling bersih dan paling konsisten (koeksistensi dan hub terpusat) justru yang paling mengintrusi cara kerja sistem sumber dan pemiliknya, dan intrusi itulah tempat program MDM macet. Jalur pragmatis adalah memperoleh kepercayaan dengan gaya berisiko rendah dan bergerak menuju kendali lebih kuat hanya di mana kasus bisnis jelas. Trade-off pencocokan paralel: aturan deterministik dapat diaudit tetapi rapuh, penilaian probabilistik kuat tetapi menuntut kepengurusan dan toleransi terhadap penggabungan salah sesekali. Sebagian besar program matang memadukan keduanya.

## Pertanyaan untuk didiskusikan dengan tim Anda

1. **Ranah data induk mana yang benar-benar menyebabkan nyeri bagi kita, dan sudahkah kita memeringkatnya menurut biaya alih-alih memperlakukan semuanya sekaligus?** Banyak program MDM runtuh di bawah ambisinya sendiri, mencoba menguasai setiap entitas di enterprise sekaligus dan tak menghasilkan apa-apa selama dua tahun. Langkah produktif adalah menemukan satu atau dua ranah di mana duplikasi dan konflik berbiaya uang atau kepercayaan nyata, biasanya pelanggan atau produk, dan mengkuantifikasi biaya itu: surat kiriman terbuang, jam rekonsiliasi, angka pendapatan salah, temuan audit. Bawa contoh konkret entitas yang sama muncul dalam berbagai cara di seluruh sistem Anda, dan biarkan peringkat itu memberi tahu dari mana memulai, karena kemenangan sempit dan terukur membangun kredibilitas yang Anda butuhkan untuk berekspansi.

2. **Siapa yang memiliki setiap ranah data induk, dan apakah steward kita punya wewenang dan waktu untuk benar-benar mengerjakannya?** Perkakas MDM tanpa kepengurusan yang diberdayakan adalah mobil tanpa pengemudi, dan mode kegagalan paling umum adalah menamai steward di slide sambil tak memberi mandat nyata dan jam yang dialokasikan. Orang yang menyelesaikan kecocokan ambigu dan menyelesaikan sengketa "apa yang dihitung sebagai pelanggan" butuh keahlian ranah, wewenang keputusan, dan waktu terlindungi. Bawa bagan organisasi Anda dan tanyakan, untuk ranah teratas Anda, persis siapa yang memutuskan kapan dua catatan adalah orang yang sama dan siapa yang menengahi ketika penjualan dan keuangan berselisih. Jika Anda tak dapat menamai orang itu dan menunjuk waktu yang dialokasikan baginya, Anda telah menemukan celah yang akan menenggelamkan program.

3. **Ketika kita menggabungkan dua catatan menjadi golden record, dapatkah kita menjelaskan dan membalikkan keputusan itu, dan dari mana nilai bertahan berasal?** Aturan survivorship adalah logika bisnis yang belum pernah dituliskan sebagian besar tim, yang berarti penggabungan terjadi karena kebetulan urutan muat atau bawaan perkakas, dan penggabungan salah yang menyatukan dua pelanggan nyata menyakitkan untuk diurai. Bawa catatan tergabung nyata dan telusuri setiap bidang bertahan kembali ke sumber dan aturannya: mengapa alamat ini, mengapa nama ini, mengapa nomor telepon ini. Pastikan setiap penggabungan tercatat dan dapat dibalik, dan bahwa pita tengah kecocokan tak pasti diteruskan ke manusia alih-alih digabung otomatis. Jika Anda tak dapat menjelaskan golden record spesifik, steward Anda tak dapat mempertahankannya di depan auditor atau pelanggan yang dirugikan.

4. **Gaya arsitektur MDM mana yang cocok untuk setiap ranah yang kita rencanakan untuk dikuasai, dan dapatkah kita mempertahankan pilihan itu terhadap gangguan yang ditimbulkannya pada pemilik sistem sumber?** Gaya yang Anda pilih menentukan seberapa banyak Anda dapat membersihkan data dan seberapa banyak Anda mengintrusi tim yang memiliki sumber, dan memilih berdasarkan tren atau pitch vendor alih-alih realitas kendali-versus-gangguan adalah cara program macet di tengah jalan. Registry membuktikan nilai dengan murah tetapi tak pernah memperbaiki sumber; hub terpusat memberi konsistensi terkuat tetapi memindahkan di mana catatan dibuat, yang merupakan perubahan organisasi yang menyamar sebagai teknis. Bawa, untuk setiap ranah kandidat, pembacaan jujur seberapa banyak otoritas yang benar-benar Anda pegang atas pemilik sumber, seberapa segar salinan hilir harus, dan apa yang akan dirusak writeback dalam alur kerja yang ada. Dalam pengaturan enterprise dan pemerintah, tambahkan biaya migrasi dan manajemen perubahan memindahkan sistem pencatat, karena tim yang kerja hariannya berpindah akan menolak hub yang tidak mereka konsultasikan, dan peluncuran koeksistensi yang macet lebih mahal daripada registry sederhana yang terkirim.

5. **Bagaimana kita menyetel ambang pencocokan, dan sudahkah kita menyepakati laju penggabungan salah dan kecocokan terlewat yang dapat kita terima di setiap ranah?** Setiap mesin pencocokan probabilistik menukar penggabungan salah (menyatukan dua entitas nyata) dengan kecocokan terlewat (membiarkan satu entitas terpecah), dan keseimbangannya adalah keputusan bisnis, bukan bawaan yang ditinggalkan seseorang dalam perkakas. Tetapkan pita gabung-otomatis dan tolak-otomatis terlalu lebar dan Anda diam-diam merusak golden record; terlalu sempit dan antrean tinjauan manusia tumbuh lebih cepat daripada yang dapat dibersihkan steward. Bawa distribusi keyakinan saat ini, ukuran dan usia antrean tinjauan, dan contoh galat kedua jenis agar ruangan dapat melihat biaya nyata setiap arah. Dalam ranah identitas pemerintah, condonglah keras ke kecocokan terlewat dan tinjauan manusia, karena penggabungan salah dapat menolak tunjangan atau memaparkan data satu warga kepada warga lain, dan biaya banding dan audit galat itu melampaui biaya duplikat yang diselesaikan steward minggu depan.

6. **Bagaimana sistem hilir mengetahui golden record berubah, dan seberapa basi masing-masing boleh sebelum keputusan salah?** Golden record yang terselesaikan sempurna yang tak dikonsumsi sistem mana pun adalah spreadsheet mahal, dan mekanisme propagasi, entah peristiwa perubahan, API langganan, atau batch malam, diam-diam menetapkan seberapa mutakhir setiap keputusan yang bergantung. Propagasi berbasis peristiwa menjaga puluhan konsumen hampir real-time tetapi menuntut konsumen idempoten dan peristiwa berversi; sinkronisasi malam lebih sederhana tetapi membuat semua orang basi sehari, yang mungkin baik untuk daftar pemasaran dan berbahaya untuk pemeriksaan penipuan. Bawa daftar sistem konsumen, kesegaran yang benar-benar dibutuhkan masing-masing, dan bagaimana konsumen yang melewatkan pembaruan hari ini pulih. Untuk organisasi besar atau publik, namai siapa yang memiliki kontrak untuk peristiwa ini dan bagaimana pelanggan mendeteksi pesan yang terjatuh, karena perubahan entitas yang diam-diam gagal mencapai satu lembaga menciptakan ulang persis fragmentasi yang didanai MDM untuk dihilangkan.

## Lensa sektor

**Startup.** Dengan segelintir insinyur dan tanpa runway tersisa, jangan membeli platform MDM. Kuasai satu entitas yang merusak angka Anda, biasanya pelanggan yang terduplikasi antara pendaftaran swalayan dan penjualan, dengan pekerjaan pencocokan di warehouse yang sudah Anda jalankan dan satu orang meninjau kecocokan tak pasti setiap minggu. Jaga setiap penggabungan tercatat dan dapat dibalik agar aturan buruk berbiaya satu sore, bukan hubungan pelanggan, dan tinjau ulang perkakas lebih berat hanya ketika antrean tinjauan manual melampaui satu peninjau.

**Bisnis kecil.** Anda tidak punya steward data dan anggaran ketat, jadi perlakukan ini sebagai keputusan beli-bukan-bangun dan bersandarlah pada standar yang Anda dapat gratis. Pilih perkakas yang sudah mendeduplikasi kontak dan berbicara kode negara dan mata uang ISO daripada hub pesanan yang tak dapat Anda pelihara, dan pilih satu ranah, biasanya pelanggan atau produk, di mana duplikat berbiaya uang nyata. Tetapkan akuntabilitas kepada pemilik bernama bahkan jika itu sebagian kecil dari satu minggu kerja seseorang, karena kosakata yang menyimpang tanpa ada yang mengawasi adalah yang diam-diam merusak laporan Anda.

**Enterprise.** Di selusin sistem ERP dan CRM yang menumpuk lewat akuisisi, pekerjaannya tata kelola portofolio: peringkat ranah menurut biaya duplikasinya, dirikan steward berdaya di bisnis, dan bakukan aturan survivorship dan versioning data referensi agar kelompok berhenti menyelesaikan ulang masalah pencocokan yang sama. Anggarkan biaya integrasi dan kepengurusan permanen secara eksplisit, propagasikan golden record sebagai peristiwa berversi agar sumber membaik seiring waktu, dan kelola MDM sebagai program terukur dengan tingkat duplikat dan metrik antrean tinjauan alih-alih pembersihan sekali jalan.

**Pemerintah.** Aturan pengadaan, hukum berbagi data yang ketat, dan akuntabilitas publik membentuk setiap pilihan. Kuncikan entitas orang pada pengenal nasional teratur, versikan data referensi menurut tanggal efektif agar catatan historis tetap benar, dan jadikan resolusi identitas sengaja konservatif: kecocokan tak pasti diteruskan ke steward terlatih, tidak pernah penggabungan otomatis, karena penggabungan salah dapat menolak tunjangan atau membocorkan data satu warga ke warga lain. Catat setiap pencocokan untuk audit dan banding, tuntut portabilitas data dan logika pencocokan yang diungkap dari vendor, dan jaga seluruh kemampuan di dalam standar interoperabilitas yang sudah dikomitmenkan sektor publik.

## Contoh

**Startup.** Perusahaan perangkat lunak yang tumbuh cepat menjual lewat pendaftaran swalayan dan tim penjualan, dan kedua kanal menciptakan pelanggan yang sama dua kali dengan nama perusahaan yang sedikit berbeda. Pendapatan-per-akun tampak salah dan tim penjualan terus menelepon dingin pengguna yang sudah ada. Alih-alih membeli platform berat, mereka memulai dengan registry ringan: pekerjaan pencocokan di warehouse data mereka yang menautkan catatan lewat domain email dan nama perusahaan ternormalisasi, dengan satu steward paruh waktu meninjau kecocokan tak pasti setiap minggu. Biayanya kecil, memperbaiki galat pelaporan, dan membuktikan nilai yang membenarkan investasi lebih besar seiring mereka tumbuh.

**Enterprise.** Produsen global telah tumbuh lewat akuisisi dan menjalankan selusin sistem ERP dan CRM, masing-masing dengan catatan pemasoknya sendiri, sehingga pemasok yang sama muncul lima belas cara dan perusahaan tak dapat bernegosiasi sebagai satu pembeli atau melihat pengeluaran sebenarnya. Ia mendirikan hub MDM gaya koeksistensi untuk ranah pemasok dan produk, memakai pencocokan deterministik pada pengenal pajak dan registrasi plus penilaian probabilistik pada nama dan alamat. Steward bernama di pengadaan menyetel aturan survivorship dan mengerjakan antrean tinjauan, dan golden record diterbitkan sebagai peristiwa perubahan yang mengalir kembali ke setiap ERP sehingga data bersih memperbaiki sumber. Visibilitas pengeluaran terkonsolidasi membuka ketentuan kontrak lebih baik, dan pajak rekonsiliasi yang menghabiskan keuangan setiap kuartal turun tajam.

**Pemerintah.** Pemerintah nasional ingin lembaga memperlakukan warga sebagai satu orang alih-alih orang asing di setiap loket, sambil menghormati batas hukum ketat atas berbagi data. Ia membangun hub data induk terpusat untuk entitas orang, berkunci pada pengenal nasional teratur, dengan data referensi diversikan menurut tanggal efektif agar catatan historis tetap benar. Resolusi identitas sengaja konservatif: kecocokan tak pasti diteruskan ke steward terlatih alih-alih penggabungan otomatis, karena penggabungan salah dapat menolak tunjangan seseorang atau memaparkan datanya, dan setiap kecocokan dicatat untuk audit dan banding. Imbalannya catatan terduplikasi lebih sedikit, penipuan dari identitas terpecah lebih sedikit, dan warga yang tak perlu membuktikan siapa dirinya di setiap pintu, dalam standar interoperabilitas bab 3.8.

## Kasus bisnis: motivasi, ROI, dan TCO

Imbal hasil MDM datang dari menghilangkan pajak yang dibayar sebagian besar organisasi tanpa menamainya. Catatan duplikat dan bertentangan berbiaya uang dengan cara yang jelas (pemasaran terbuang kepada orang yang sama lima kali, galat pengiriman dari alamat basi, diskon volume yang terlewat) dan dengan cara yang kurang jelas (analis merekonsiliasi hitungan, eksekutif memutuskan atas angka yang diam-diam salah, auditor menagih jam untuk mengurai catatan mana yang nyata). Pandangan pemasok terkonsolidasi sering membayar seluruh program lewat ketentuan kontrak yang lebih baik saja.

Total biaya kepemilikan punya tiga bagian: platform atau bangunan, integrasi ke sumber dan konsumen, dan, terbesar dalam jangka panjang, kepengurusan berkelanjutan. Biaya integrasi mudah diremehkan, karena menghubungkan selusin sistem sumber yang menua adalah tempat program MDM berdarah jadwal dan anggaran, dan biaya kepengurusan mudah dilupakan, karena ia pengeluaran operasi permanen, bukan bangunan sekali jalan. Untuk mengajukan kasus kepada pimpinan, kaitkan MDM dengan angka yang sudah mereka lacak: akurasi pendapatan, efisiensi pemasaran, penghematan pengadaan, biaya audit, dan risiko regulasi, lalu mulai sempit dan biarkan kemenangan terukur pada satu ranah nyeri tinggi mendanai ekspansi.

## Anti-pola dan jebakan

- **Cakupan merebus lautan:** menguasai setiap ranah sekaligus, tak menghasilkan apa-apa selama bertahun-tahun, dan kehilangan sponsor sebelum kemenangan pertama.
- **Perkakas sebelum tata kelola:** membeli platform MDM sebelum menamai steward dan pemilik, sehingga mesin tak punya pengemudi.
- **Steward paruh waktu tanpa wewenang:** menetapkan kepengurusan di slide sambil tak memberi mandat nyata atau waktu terlindungi.
- **Survivorship senyap:** menggabungkan catatan lewat bawaan perkakas atau urutan muat, tanpa aturan tertulis dan tanpa cara menjelaskan golden record.
- **Penggabungan tak dapat dibalik:** menggabung otomatis kecocokan tak pasti tanpa undo, sehingga fusi salah dua entitas nyata menjadi kerusakan permanen.
- **Data referensi ditimpa di tempat:** menyunting daftar kode tanpa versioning, merusak setiap laporan historis yang benar di bawah kode lama.
- **Golden record yang tak dikonsumsi siapa pun:** membangun hub murni yang tak dilanggani sistem hilir mana pun, sehingga data bersih tak pernah mencapai keputusan.
- **Menciptakan ulang kode standar:** mencetak daftar negara atau mata uang sendiri ketika standar ISO ada, dan kehilangan interoperabilitas tanpa alasan.

## Model kematangan

- **Tingkat 1, Memulai:** Data induk dan referensi tak dikelola. Entitas yang sama ada berkali-kali tanpa versi otoritatif, daftar kode menyimpang, pencocokan manual dan reaktif, dan tak ada yang memiliki masalahnya, sehingga hitungan entitas inti tidak sepakat dan tak ada yang bisa mengatakan mana yang benar.
- **Tingkat 2, Mengembangkan:** Ranah kunci dikenali dan seseorang mendeduplikasinya, sering di warehouse untuk pelaporan. Pencocokan deterministik dasar ada, daftar referensi dikumpulkan, dan beberapa orang bertindak sebagai steward informal, tetapi praktik bervariasi tim demi tim, sumber tetap berantakan, dan aturan hidup di kepala orang alih-alih di atas kertas.
- **Tingkat 3, Membakukan:** MDM adalah program teratur yang diterapkan konsisten di seluruh organisasi. Ranah induk punya pemilik bernama dan steward berdaya, aturan pencocokan dan survivorship didokumentasikan dan ditegakkan, golden record dihasilkan dan dipropagasi ke konsumen, dan data referensi diversikan serta diterbitkan dengan tanggal efektif seperti API.
- **Tingkat 4, Mengelola:** Program diukur dan dikendalikan terhadap garis dasar. Tingkat duplikat, distribusi keyakinan kecocokan, tingkat penggabungan salah dan kecocokan terlewat, kelengkapan bidang kunci, serta ukuran dan usia antrean tinjauan dilacak sebagai metrik; ambang disetel terhadap angka-angka itu alih-alih perasaan; dan nilai MDM (akurasi pendapatan, penghematan pengadaan, biaya tinjauan) dikuantifikasi dan dilaporkan kepada pemilik pada irama tetap.
- **Tingkat 5, Mengorkestrasi:** Golden record mengalir sebagai peristiwa berversi hampir real-time, memberi makan lapisan semantik, dan dipercaya di seluruh organisasi. Pencocokan terus diperbaiki terhadap hasil terukur, penguasaan meluas ke ranah baru sebagai kemampuan berulang, dan MDM terintegrasi dengan tata kelola dan perencanaan risiko sehingga program beradaptasi seiring sumber, standar, dan lanskap entitas bergeser.

## Gagasan untuk didiskusikan

1. Jika dua sistem Anda tidak sepakat tentang berapa banyak pelanggan yang Anda miliki, mana yang benar, dan bagaimana Anda membuktikannya?
2. Ranah data induk mana yang akan memberi kemenangan terukur terbesar jika Anda menguasainya lebih dulu, dan berapa nilai kemenangan itu?
3. Di mana pencocokan probabilistik akan membantu Anda hari ini, dan apakah Anda nyaman dengan penggabungan salah sesekali yang disiratkannya?
4. Bagaimana Anda memversikan data referensi Anda, dan apa yang rusak dalam laporan historis Anda ketika kode berubah makna?
5. Siapa steward bernama untuk entitas terpenting Anda, dan apakah mereka punya wewenang dan waktu untuk benar-benar mengerjakannya?
6. Ketika golden record berubah, bagaimana sistem hilir Anda mengetahuinya, dan seberapa basi mereka boleh sebelum merugikan?

## Poin-poin utama

- Pilah data Anda menjadi induk, referensi, dan transaksional; investasikan pencocokan dan tata kelola di mana duplikasi paling mahal.
- Hasilkan satu golden record per entitas dunia nyata, dirakit oleh aturan survivorship yang eksplisit, dapat dibalik, dan tercatat.
- Pilih gaya arsitektur MDM (registry, konsolidasi, koeksistensi, atau hub terpusat) agar sesuai selera Anda terhadap kendali dan gangguan.
- Perlakukan data referensi sebagai kosakata bersama berversi, pilih standar yang diakui, dan jangan pernah menimpa daftar kode di tempat.
- MDM berhasil karena tata kelola dan kepengurusan, bukan perkakas; propagasikan golden record sebagai peristiwa dan ukur program dari keputusan yang diperbaiki.

## Referensi dan bacaan lanjutan

- David Loshin, *Master Data Management*
- Alex Berson dan Larry Dubov, *Master Data Management and Data Governance*
- Dan Power, *The Definitive Guide to Master Data Management*
- John Talburt, *Entity Resolution and Information Quality*
- Peter Christen, *Data Matching: Concepts and Techniques for Record Linkage, Entity Resolution, and Duplicate Detection*
- Ivan P. Fellegi dan Alan B. Sunter, "A Theory for Record Linkage," *Journal of the American Statistical Association*
- DAMA International, *DAMA-DMBOK: Data Management Body of Knowledge*
- Ralph Kimball dan Margy Ross, *The Data Warehouse Toolkit*
