# 5.2 Desain UI dan sistem desain

## Tinjauan dan motivasi

[Desain antarmuka pengguna (UI)](https://en.wikipedia.org/wiki/User_interface_design) adalah kerajinan membentuk apa yang dilihat dan disentuh orang: tata letak, [tipografi](https://en.wikipedia.org/wiki/Typography), warna, jarak, kontrol, dan keadaan. [Sistem desain](https://en.wikipedia.org/wiki/Design_system) mengambil kerajinan itu dan mengubahnya menjadi aset bersama, dapat dipakai ulang, dan diatur: himpunan prinsip, komponen, pola, dan token terdokumentasi yang ditarik dari setiap tim, sehingga seluruh produk tampak dan berperilaku sebagai satu. Desain UI memutuskan bagaimana satu layar harus tampak. Sistem desain memutuskan bagaimana sepuluh ribu layar lintas banyak tim tetap koheren.

Bagi organisasi besar, sistem desain adalah investasi berpengungkit tertinggi dalam kualitas UI dan kecepatan pengiriman. Tanpanya, setiap tim menciptakan ulang tombol, formulir, modal, dan penanganan galat, masing-masing sedikit berbeda, masing-masing dipelihara terpisah, masing-masing rusak terpisah. Pengguna membayarnya dalam kebingungan dan ketidakpercayaan; bisnis membayarnya dalam upaya terduplikasi dan kualitas tidak merata. Sistem desain mengubah keputusan desain sekali jalan menjadi modal yang dapat dipakai ulang: selesaikan [aksesibilitas](https://en.wikipedia.org/wiki/Accessibility), [responsivitas](https://en.wikipedia.org/wiki/Responsive_web_design), dan branding sekali dalam komponen, dan setiap tim mewarisi hasilnya.

Enterprise dan pemerintah menambah dua tekanan spesifik. Pertama, skala: ratusan aplikasi, banyak yang dibangun vendor atau diperoleh lewat merger, semuanya perlu terasa seperti satu organisasi. Kedua, umur panjang dan perubahan: merek disegarkan, lembaga direorganisasi, dan satu platform mungkin perlu melayani beberapa merek atau sublembaga dari satu basis kode. Sistem desain yang diarsiteki dengan baik, dengan tema dan tokenisasi yang tepat, membuat perubahan menyeluruh ini dapat diatasi alih-alih katastrofik.

## Prinsip utama

- Konsistensi menurunkan [beban kognitif](https://en.wikipedia.org/wiki/Cognitive_load); tombol harus tampak dan berperilaku sama di mana-mana.
- Keputusan desain adalah aset: tangkap sekali sebagai komponen dan token yang dapat dipakai ulang.
- Token adalah sumber kebenaran untuk keputusan visual; komponen mengonsumsi token, tidak pernah nilai yang dikodekan keras.
- Aksesibilitas dan responsivitas dibangun ke dalam komponen, tidak ditempelkan per layar.
- Sistem desain adalah produk dengan pengguna (pengembang dan desainer), bukan hasil serah sekali jalan.
- Hierarki visual memandu perhatian: tipe, warna, dan ruang harus membuat kepentingan jelas.
- Tata kelola menjaga sistem tetap koheren; kontribusi menjaganya tetap hidup.

## Rekomendasi

### Strukturkan sistem dalam lapisan: token, komponen, pola

Token desain adalah nilai bernama dan netral platform untuk warna, jarak, tipografi, radius, elevasi, dan gerak: keputusan atomik. Bangun dalam tingkatan: palet primitif (nilai mentah), token semantik (`color-action-primary`, `space-inset-md`) yang membawa makna, dan token tingkat komponen di tempat Anda butuh. Komponen mengonsumsi token semantik, sehingga satu perubahan merambat ke mana-mana. Di atas komponen berada pola: komposisi teruji seperti tabel data, formulir multilangkah, atau keadaan kosong. Dokumentasikan ketiga lapisan di satu tempat, dengan contoh hidup dan panduan penggunaan.

### Dapatkan dasar visual dengan benar

Siapkan skala tipografi dengan hierarki jelas dan jarak baris lega untuk keterbacaan, dan pertahankan himpunan terbatas ukuran dan bobot. Definisikan warna sebagai sistem, dengan kontras cukup untuk aksesibilitas (lihat bab aksesibilitas) dan peran semantik, alih-alih rona mentah yang tersebar di UI. Gunakan skala jarak dan grid tata letak agar perataan dan irama tetap konsisten tanpa tebakan per layar. Hierarki visual harus membuat tindakan utama dan informasi terpenting jelas sekilas.

### Rancang responsif dan mobile-first

Rancang untuk viewport terkecil yang masuk akal lebih dulu, lalu tingkatkan untuk layar lebih besar. Ini memaksa Anda memprioritaskan konten dan kontrol esensial. Gunakan tata letak cair dan satuan relatif agar antarmuka beradaptasi dengan layar apa pun, alih-alih melompat antara beberapa breakpoint tetap. Buat target sentuh cukup besar, dan pastikan interaksi berfungsi dengan sentuh, mouse, dan keyboard. Di pemerintah khususnya, asumsikan bagian berarti pengguna Anda memakai perangkat kecil, lama, atau murah.

### Jadikan serah terima desain-ke-dev dan paritas perhatian kelas satu

Sistem desain hanya membayar jika UI yang dikirim cocok dengan desain yang dimaksud dan terus cocok. Tuju satu sumber kebenaran: token yang diekspor dari perkakas desain mengalir langsung ke kode, sehingga desainer dan insinyur merujuk nilai yang sama. Sediakan pustaka komponen berkode yang benar-benar akan dipakai insinyur, dengan nama dan props yang sama seperti komponen desain. Gunakan pengujian regresi visual (perbandingan otomatis UI yang dirender terhadap citra baseline yang disetujui) dan pemeriksaan tinjauan desain untuk menangkap penyimpangan. Dan ukur "paritas desain-kode" sebagai metrik kesehatan eksplisit: bagian UI yang dibangun dari komponen sistem versus kode sekali pakai.

### Dukung tema dan white-labelling pada skala enterprise

Arsitekturkan untuk beberapa merek sejak awal jika ada kemungkinan Anda membutuhkannya. Karena komponen mengonsumsi token semantik, tema hanyalah himpunan nilai token berbeda, sehingga penyegaran merek atau submerek baru menjadi perubahan data, bukan penulisan ulang kode. Dukung tema terang dan gelap, mode kontras tinggi, dan branding per tenant lewat mekanisme yang sama. Jaga logika khusus merek di luar komponen, dan dorong ke himpunan token dan konfigurasi sebagai gantinya.

### Atur sistem sebagai produk

Beri sistem desain tim khusus, peta jalan, pembuatan versi, changelog, dan saluran dukungan. Jabarkan bagaimana tim menyumbang komponen baru, dan bagaimana itu ditinjau dan dipromosikan. Seimbangkan kendali pusat (untuk menjaga koherensi dan aksesibilitas) dengan model kontribusi (agar sistem berevolusi dengan kebutuhan nyata alih-alih menjadi hambatan). Komunikasikan deprekasi dan migrasi dengan jelas, dan beri tim konsumen lead time cukup.

## Trade-off: kelebihan dan kekurangan

| Keputusan | Kelebihan | Kekurangan |
|---|---|---|
| Bangun sistem desain | Konsistensi, kecepatan, aksesibilitas sekali, rebrand lebih mudah | Biaya di muka dan berkelanjutan, butuh tim khusus |
| Adopsi sistem siap pakai | Mulai cepat, pola teruji | Tampilan generik, lebih sulit menyesuaikan merek dan kebutuhan unik |
| Tata kelola pusat ketat | Koherensi, kualitas, aksesibilitas terjamin | Dapat menghambat tim, terasa birokratis |
| Model kontribusi terbuka | Berevolusi dengan kebutuhan nyata, kepemilikan bersama | Risiko penyimpangan dan inkonsistensi tanpa tinjauan |
| Tokenisasi dan tema berat | Rebrand murah dan dukungan multimerek | Lebih banyak abstraksi, kurva belajar lebih curam |

Sistem desain menukar biaya di muka dan tata kelola dengan konsistensi dan kecepatan jangka panjang. Untuk produk kecil dengan satu tim, bebannya mungkin tidak membayar. Untuk organisasi besar dengan banyak tim dan produk berumur panjang, pertanyaannya bukan apakah punya sistem melainkan seberapa banyak berinvestasi dan bagaimana mengaturnya. Penyesalan paling umum adalah kurang berinvestasi pada tata kelola dan perkakas paritas: sistem ada di atas kertas, tetapi tim diam-diam menjauh darinya.

## Pertanyaan untuk didiskusikan dengan tim Anda

1. **Bagaimana arsitektur token kita bertingkat, dan apakah komponen dilarang memakai nilai yang dikodekan keras?** Seluruh imbalan sistem desain (rebrand murah, tema multimerek, aksesibilitas diselesaikan sekali) bergantung pada komponen yang mengonsumsi token semantik seperti `color-action-primary` alih-alih rona mentah dan nilai piksel yang tersebar di kode. Putuskan tingkatan sekarang: palet primitif, token semantik yang membawa makna, dan token tingkat komponen hanya di tempat Anda benar-benar butuh. Abstraksi berlebihan adalah risiko nyata, jadi sepakati berapa banyak lapisan yang terlalu banyak dan bagaimana pengembang menemukan token yang tepat dengan cepat. Bawa grep warna dan jarak yang dikodekan keras di basis kode Anda sebagai bukti penyimpangan. Jika logika merek tertanam dalam komponen, rebrand menjadi penulisan ulang kode alih-alih perubahan konfigurasi, yang persis bencana yang dicegah tokenisasi.

2. **Bagaimana kita mengukur dan mempertahankan paritas desain-kode, dan perkakas apa yang menangkap penyimpangan secara otomatis?** Sistem desain yang hanya ada sebagai berkas desain adalah lembar stiker: insinyur membangun ulang segalanya juga dan UI yang dikirim perlahan menyimpang dari maksud. Sepakati metrik paritas eksplisit (bagian UI yang dibangun dari komponen sistem versus kode sekali pakai) dan hubungkan pengujian regresi visual ke CI agar layar yang dirender dibandingkan dengan baseline yang disetujui. Ini penting pada skala enterprise dan pemerintah karena ratusan aplikasi, banyak yang dibangun vendor atau diwarisi lewat merger, semuanya perlu terasa seperti satu organisasi. Bawa angka paritas saat ini dan daftar komponen bespoke teratas yang terus dibangun ulang tim. Jika tak ada yang memiliki metrik atau rangkaian regresi, penyimpangan sudah menang secara diam-diam.

3. **Bagaimana kita mengatur kontribusi, deprekasi, dan migrasi agar sistem tidak menghambat tim maupun terfragmentasi?** Kendali pusat ketat menjamin koherensi dan aksesibilitas tetapi dapat mengubah tim sistem desain menjadi hambatan yang disiasati tim; kontribusi terbuka menjaga sistem tetap hidup tetapi berisiko varian menyimpang tanpa tinjauan. Putuskan jalur kontribusi: bagaimana tim mengusulkan komponen baru, siapa yang meninjau, dan bagaimana ia dipromosikan. Sama pentingnya, sepakati bagaimana Anda mengomunikasikan perubahan yang merusak, karena deprekasi tanpa dukungan migrasi dan lead time menyebabkan tim konsumen macet atau mem-fork. Bawa contoh komponen yang dibangun tim di luar sistem dan tanyakan mengapa mereka tidak menyumbangkan kembali. Jawabannya biasanya mengungkap apakah tata kelola Anda layanan atau rintangan.

4. **Bagaimana kita menjamin aksesibilitas diselesaikan sekali di dalam komponen, dan apa yang mencegah tim mengirim komponen sekali pakai yang tak dapat diakses?** Argumen terkuat untuk sistem desain adalah bahwa kontras warna, keadaan fokus, pengoperasian keyboard, dan semantik pembaca layar diselesaikan sekali dan diwarisi di mana-mana, tetapi janji itu runtuh begitu tim membuat kontrol sendiri. Bagi organisasi besar di sinilah risiko hukum dan reputasi terbesar berada, karena satu formulir pembayaran atau pemilih tanggal yang tak dapat diakses dapat memblokir pengguna nyata dan memicu keluhan di setiap produk yang menyalinnya. Timbang penegakan pusat (komponen yang dapat diakses plus linter atau gerbang tinjauan yang menolak markup mentah) terhadap otonomi tim, dan putuskan di mana garis kerasnya. Bawa hasil audit aksesibilitas, daftar komponen beserta status kesesuaiannya, dan hitungan kontrol bespoke yang dibangun ulang tim di luar sistem. Dalam pengaturan enterprise dan pemerintah ini bukan basa-basi: kewajiban seperti WCAG, Section 508, dan EN 301 549 menjadikan kesesuaian persyaratan pengadaan dan audit, sehingga pustaka komponen dengan kesesuaian terdokumentasi sendiri adalah aset kepatuhan.

5. **Berapa banyak merek, tenant, dan tema yang harus dilayani sistem ini, dan sudahkah kita mengarsitekturkan lapisan token untuk itu sekarang alih-alih memasangnya belakangan?** Tema murah jika Anda merancang untuknya dan brutal jika tidak, karena merek atau tenant yang tak pernah diantisipasi memaksa logika merek kembali ke komponen dan membatalkan seluruh inti tokenisasi. Bagi tim besar keputusan ini membentuk kerja bertahun-tahun: platform yang harus melayani beberapa merek, tema terang dan gelap, mode kontras tinggi, dan branding per tenant membutuhkan lapisan token semantik yang cukup bersih sehingga tema hanyalah himpunan nilai berbeda. Seimbangkan fleksibilitas itu terhadap abstraksi berlebihan, karena pohon token yang tak dapat dinavigasi siapa pun adalah kegagalan tersendiri. Bawa peta jalan merek dan tenant yang dapat Anda duga, jumlah tema yang berjalan hari ini, dan komponen apa pun yang sudah membocorkan logika khusus merek. Dalam konteks enterprise dan pemerintah, merger, akuisisi, dan reorganisasi lembaga rutin menambah merek yang tidak Anda rencanakan, sehingga mengarsitekturkan untuk multimerek sejak awal adalah beda antara perubahan data dan penulisan ulang multitahun.

6. **Bagaimana kita akan memigrasikan aplikasi warisan dan buatan vendor ke sistem, dan bagaimana tim sistem desain didanai agar selamat dari siklus anggaran berikutnya?** Sistem desain hanya memberi imbal hasil ketika produk nyata mengadopsinya, namun aplikasi tersulit dikonversi adalah yang lama dan yang dialihdayakan yang paling membutuhkannya, dan tim yang memelihara sistem sering yang pertama dipotong ketika anggaran mengetat. Bagi organisasi besar Anda harus memutuskan antara migrasi big-bang dan inkremental, dan bagaimana membuat vendor membangun di atas komponen Anda alih-alih di sekitarnya. Bawa inventaris aplikasi beserta skor paritas saat ini, estimasi upaya migrasi per aplikasi, dan pengungkit kontraktual yang Anda pegang atas vendor. Dalam pengaturan enterprise dan pemerintah, tulis kesesuaian sistem desain ke dalam ketentuan pengadaan agar pekerjaan vendor baru mendarat di sistem secara bawaan, dan danai tim pemelihara sebagai infrastruktur bersama yang tahan lama, karena sistem yang kehilangan pengelolanya dalam reorganisasi hanyut kembali ke fragmentasi dalam setahun.

## Lensa sektor

**Startup.** Dengan dua atau tiga insinyur dan tanpa landasan tersisa, jangan bangun sistem yang diatur. Habiskan satu atau dua hari mendefinisikan himpunan kecil token semantik untuk warna, jarak, dan tipe, plus selusin komponen bersama, semuanya dalam satu berkas yang dirujuk seluruh tim. Bersandarlah pada pustaka primitif siap pakai untuk bagian sulit, dan jangan kodekan keras apa pun agar rebrand nyata pertama Anda adalah perubahan token alih-alih penulisan ulang.

**Bisnis kecil.** Tanpa desainer khusus dan dengan anggaran ketat, beli alih-alih bangun: adopsi pustaka komponen atau UI kit teruji dan beri tema ringan sesuai merek Anda. Tujuan Anda produk yang konsisten dan dapat diakses tanpa mengisi staf tim sistem desain, jadi pilih sistem yang mengirim aksesibilitas dan responsivitas langsung dalam kotak. Tahan dorongan untuk mem-fork, karena salinan khusus yang tak dapat Anda pelihara menjadi liabilitas begitu proyek hulu bergerak.

**Enterprise.** Masalahnya koherensi lintas banyak tim dan produk berumur panjang, jadi perlakukan sistem desain sebagai infrastruktur bersama yang diatur dengan tim khusus, pembuatan versi, dan peta jalan. Lacak paritas desain-kode sebagai metrik nyata, hubungkan pengujian regresi visual ke CI, dan arsitekturkan lapisan token untuk banyak merek dan tema sejak awal. Anggarkan biaya tata kelola dan migrasi secara eksplisit, dan kelola adopsi sebagai portofolio alih-alih mengasumsikan tim akan hanyut ke sistem sendiri.

**Pemerintah.** Aturan pengadaan, transparansi, dan akuntabilitas publik membentuk setiap pilihan. Kesesuaian aksesibilitas terhadap standar seperti WCAG, Section 508, dan EN 301 549 adalah persyaratan hukum, bukan preferensi, sehingga pustaka komponen dengan kesesuaian terdokumentasi menjadi aset kepatuhan. Pilih atau perluas sistem desain publik bersama agar warga bertemu pola yang sama lintas layanan, tulis penggunaan sistem desain ke dalam kontrak vendor, dan terbitkan komponen serta panduan Anda secara terbuka agar lembaga dan pemasoknya dapat mengadopsi dan dimintai pertanggungjawaban.

## Contoh

**Startup.** Startup dua insinyur terus membangun ulang tombol dan bidang formulir sedikit berbeda pada setiap layar baru, dan produk mulai tampak dijahit. Alih-alih sistem berat, mereka menghabiskan dua hari mendefinisikan himpunan kecil token desain semantik untuk warna, jarak, dan tipe, plus sekitar selusin komponen bersama, semuanya dalam satu berkas yang dirujuk seluruh tim. Karena tak ada yang dikodekan keras, ketika perekrutan berpikiran desain mereka yang pertama mengusulkan palet lebih bersih, penyegaran itu adalah perubahan token yang mendarat di seluruh aplikasi dalam satu sore alih-alih pekerjaan layar demi layar.

**Enterprise.** Sebuah perusahaan perangkat lunak global dengan puluhan tim produk membangun sistem desain bertoken dengan pustaka komponen berkode bersama. Token semantik memungkinkan mereka merilis penyegaran merek penuh di semua produk dalam hitungan minggu, alih-alih pekerjaan multitahun per tim, karena perubahan itu himpunan token baru alih-alih ribuan suntingan warna yang dikodekan keras. Paritas desain-kode, dilacak sebagai metrik dasbor, naik seiring tim mengganti komponen bespoke, yang memotong pemeliharaan UI terduplikasi.

**Pemerintah.** Sebuah pemerintah nasional membuat sistem desain umum untuk layanan publik (komponen bersama, pola, dan aksesibilitas bawaan) yang diwajibkan di seluruh lembaga. Warga yang berpindah antara layanan pajak, layanan kesehatan, dan layanan perizinan bertemu header, kontrol formulir, dan pola galat yang sama, yang membangun kepercayaan dan memperpendek kurva belajar. Lembaga dan vendornya merilis lebih cepat dan lebih dapat diakses karena masalah sulit diselesaikan secara terpusat, dan pemerintah dapat memperbarui panduan atau perbaikan aksesibilitas sekali dan membuatnya merambat ke mana-mana.

## Kasus bisnis: motivasi, ROI, dan TCO

ROI sistem desain datang dari menghapus duplikasi dan mempercepat pengiriman. Alih-alih setiap tim merancang dan membangun komponen yang sama, mereka menyusun dari pustaka bersama, yang terukur mempercepat pengiriman dan membebaskan desainer dan insinyur untuk kerja khusus produk. Aksesibilitas dan responsivitas, diselesaikan sekali dalam komponen, menghemat biaya remediasi per proyek. Rebrand dan tema yang dulu memakan bertahun-tahun kini memakan minggu.

Pada TCO, biaya adopsi adalah tim khusus, perkakas, dan upaya produk yang ada untuk bermigrasi ke sistem. Biaya tidak mengadopsi dibayar terus-menerus: pembangunan dan pemeliharaan terduplikasi lintas tim, UI yang tidak konsisten dan tak dapat diakses yang menciptakan risiko dukungan dan hukum, dan rebrand yang lambat dan mahal. Karena duplikasi tersebar di anggaran banyak tim, mudah terlewat: sistem desain membuat biaya tersembunyi itu terlihat dan menangkapnya di satu tempat.

Untuk mengajukan kasus kepada pimpinan, kuantifikasi pekerjaan komponen terduplikasi lintas tim, keuntungan waktu-ke-pasar dari komposisi, dan biaya serta durasi rebrand terakhir Anda versus apa yang akan diizinkan sistem bertoken. Bingkai sistem sebagai infrastruktur bersama dengan metrik adopsi terukur (persentase paritas), sehingga nilainya dapat dilacak seiring waktu alih-alih sekadar ditegaskan.

## Anti-pola dan jebakan

- **Sistem desain sebagai lembar stiker**: berkas desain statis tanpa komponen berkode, sehingga insinyur membangun ulang segalanya juga.
- **Nilai dikodekan keras di mana-mana**: warna dan jarak tersebar di kode, membuat tema dan rebrand mustahil.
- **Tanpa tata kelola**: sistem terfragmentasi seiring tim menambah varian menyimpang; konsistensi terkikis.
- **Tata kelola tanpa kontribusi**: tim pusat menjadi hambatan dan tim menyiasatinya.
- **Mengabaikan paritas**: UI berkode menyimpang dari maksud desain dan tak ada yang mengukur celahnya.
- **Abstraksi berlebihan**: begitu banyak token dan lapisan sehingga tak ada yang dapat menemukan atau memakai yang tepat.
- **Logika merek tertanam dalam komponen**: membuat multimerek dan tema menjadi penulisan ulang kode alih-alih perubahan konfigurasi.
- **Perubahan merusak tanpa dukungan migrasi**: tim konsumen macet atau mem-fork sistem.

## Model kematangan

**Tingkat 1: Memulai.** Setiap tim membangun UI-nya sendiri secara ad hoc dan reaktif. Tidak ada komponen bersama, tampilan dan perilaku tidak konsisten, warna dan jarak dikodekan keras per layar. Setiap rebrand adalah pekerjaan manual layar demi layar.

**Tingkat 2: Mengembangkan.** Panduan gaya atau pustaka komponen bersama ada tetapi parsial, opsional, dan sering tidak sinkron antara desain dan kode. Sebagian tim memakainya, yang lain tidak, dan praktik dasar sangat bervariasi dari tim ke tim.

**Tingkat 3: Membakukan.** Sistem desain bertoken dengan pustaka berkode yang dipelihara, dokumentasi, dan tata kelola terdokumentasi dan ditegakkan di seluruh organisasi. Komponen mengonsumsi token semantik, tema didukung, dan aksesibilitas serta responsivitas dibangun masuk alih-alih ditempelkan per layar.

**Tingkat 4: Mengelola.** Sistem diukur dan dikendalikan dengan data terhadap garis dasar. Paritas desain-kode dilacak sebagai metrik eksplisit dengan target per produk, pengujian regresi visual berjalan di CI untuk menangkap penyimpangan, dan kesesuaian aksesibilitas diukur terhadap standar alih-alih diasumsikan. Dasbor adopsi menunjukkan cakupan komponen menurut tim, dan biaya serta durasi rebrand dicatat agar perbaikan terlihat seiring waktu.

**Tingkat 5: Mengorkestrasi.** Sistem desain adalah produk yang terus diperbaiki, terintegrasi di seluruh organisasi, dan adaptif terhadap perubahan. Ia punya pembuatan versi, peta jalan, dan model kontribusi yang berfungsi, sehingga berevolusi dengan kebutuhan nyata. Rebrand dan tema baru adalah perubahan token rutin, tema multimerek dan multitenant normal, dan tim memensiunkan, menentukan ulang cakupan, dan mempromosikan pola atas bukti dari data penggunaan, memberi makan perkakas desain dan pipeline pengiriman dari satu sumber kebenaran.

## Gagasan untuk didiskusikan

- Bagaimana Anda menyeimbangkan tata kelola pusat terhadap otonomi tim tanpa memfragmentasi atau menghambat?
- Apa metrik yang tepat untuk "paritas desain-kode," dan bagaimana Anda menjaganya tetap jujur?
- Kapan tim boleh membangun komponen sekali pakai alih-alih memakai sistem?
- Bagaimana Anda mendanai dan mengisi staf sistem desain agar selamat dari siklus anggaran dan reorganisasi?
- Seberapa banyak fleksibilitas tema layak biaya abstraksi tambahan?
- Bagaimana Anda memigrasikan aplikasi warisan dan buatan vendor ke sistem bersama?

## Poin-poin utama

- Sistem desain mengubah keputusan desain sekali jalan menjadi modal yang dapat dipakai ulang dan diatur.
- Strukturkan dalam lapisan (token, komponen, pola), dengan komponen mengonsumsi token semantik.
- Bangun aksesibilitas dan responsivitas ke dalam komponen agar setiap tim mewarisinya.
- Perlakukan paritas desain-kode sebagai metrik kesehatan terukur, bukan asumsi.
- Tokenisasi menjadikan rebrand dan tema multimerek perubahan data, bukan penulisan ulang.
- Atur sistem sebagai produk dengan peta jalan, pembuatan versi, dan model kontribusi.
- Pada skala enterprise dan pemerintah, sistem bersama adalah investasi UI berpengungkit tertinggi yang tersedia.

## Referensi dan bacaan lanjutan

- Brad Frost, *Atomic Design*
- Alla Kholmatova, *Design Systems: A Practical Guide to Creating Design Languages*
- Josef Müller-Brockmann, *Grid Systems in Graphic Design*
- Robert Bringhurst, *The Elements of Typographic Style*
- Ellen Lupton, *Thinking with Type*
- Luke Wroblewski, *Mobile First*
- Ethan Marcotte, *Responsive Web Design*
- Nathan Curtis, tulisan tentang token desain dan tata kelola sistem desain
- W3C Design Tokens Community Group, spesifikasi format
- Sistem desain pemerintah (mis., UK Government Design System, U.S. Web Design System) sebagai implementasi rujukan
