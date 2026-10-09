# 2.14 Struktur proyek dan repositori

## Tinjauan dan motivasi

Struktur proyek dan repositori adalah organisasi fisik sebuah basis kode: folder, berkas, dan konvensi penamaan yang menentukan di mana segala sesuatu berada. *Repositori* (sering disingkat "repo") adalah wadah [berkontrol versi](https://en.wikipedia.org/wiki/Version_control) yang memegang berkas proyek dan riwayatnya. *Proyek*, kadang disebut *solusi* ketika mengelompokkan beberapa komponen terkait, adalah satuan logis perangkat lunak yang sedang Anda bangun. Struktur adalah peta yang Anda pakai untuk menemukan, memahami, dan mengubah perangkat lunak itu.

Pada tim kecil, satu orang dapat memegang seluruh tata letak di kepalanya. Pada tim besar, dengan ratusan atau ribuan insinyur, perpindahan sering antartim, dan kontraktor yang datang dan pergi, setiap repositori yang diorganisasi secara berbeda membebankan pajak kognitif baru. Ketika Anda membuka repo yang asing, Anda harus dapat menebak di mana sumber, tes, dokumentasi, dan konfigurasi deployment berada, tanpa membaca manual. Ketika setiap repo menjawab pertanyaan itu dengan cara yang sama, mobilitas murah dan orientasi cepat. Ketika setiap repo adalah kepingan salju, setiap peralihan konteks berubah menjadi proyek riset kecil.

Dalam konteks enterprise dan pemerintah, struktur yang konsisten juga perhatian kendali dan jaminan. Auditor, peninjau keamanan, dan pemelihara jangka panjang, yang sering bekerja bertahun-tahun setelah penulis aslinya pergi, perlu menemukan dengan andal dokumen spesifikasi, berkas lisensi, kebijakan keamanan, dan definisi build. Tata letak yang dapat diprediksi juga memungkinkan perkakas otomatis (pemindai, penganalisis dependensi, pemeriksaan kepatuhan) bekerja dengan cara yang sama di seluruh portofolio sistem. Jadi bab ini memperlakukan struktur sebagai konvensi yang Anda putuskan sekali dan terapkan di mana-mana. Ia berkaitan erat dengan standar pengodean dan gaya (bab 2.1), kontrol versi dan manajemen sumber (bab 2.6), dan dokumentasi (bab 2.7).

## Prinsip utama

- Ikuti *[prinsip paling sedikit kejutan](https://en.wikipedia.org/wiki/Principle_of_least_astonishment)*: tata letak harus cocok dengan yang diharapkan insinyur berpengalaman, agar tidak ada yang perlu dihafal.
- Konsistensi lintas repositori mengalahkan kecerdikan lokal; struktur yang cukup seragam di mana-mana lebih bernilai daripada struktur sempurna di satu tempat.
- [README](https://en.wikipedia.org/wiki/README) adalah pintu depan; pendatang baru harus dapat mengorientasikan diri dari README saja.
- Buat struktur menjelaskan dirinya lewat penamaan, agar folder dan berkas mengumumkan tujuannya.
- Tegakkan struktur dengan scaffolding dan templat, bukan dengan kemauan dan komentar tinjauan.
- Pisahkan perhatian secara fisik: sumber, tes, dokumen, build, dan deployment berada di tempat yang berbeda dan dapat diprediksi.
- Organisasikan dependensi agar mengalir satu arah, dari inti stabil menuju tepi yang mudah berubah.

## Rekomendasi

### Adopsi tata letak tingkat atas yang konsisten

Definisikan seperangkat baku folder tingkat atas yang dipakai setiap repositori bila berlaku, dan dokumentasikan untuk apa masing-masing. Konvensi umum yang netral vendor mencakup: folder sumber (sering `src`) untuk kode produksi; folder tes (sering `test` atau `tests`) untuk tes otomatis; folder `docs` untuk dokumentasi; folder `build` untuk definisi dan keluaran build; folder `deploy` untuk deployment dan *[infrastruktur sebagai kode](https://en.wikipedia.org/wiki/Infrastructure_as_code)* (definisi server, jaringan, dan layanan yang dapat dibaca mesin, dibahas di bab 8.2); folder `scripts` untuk otomasi dan perkakas pengembang; folder `examples` untuk contoh yang dapat dijalankan; dan folder `spec` atau `specification` untuk persyaratan dan spesifikasi desain. Tidak setiap repo membutuhkan setiap folder, tetapi di mana suatu perhatian ada, ia harus berada di tempat yang diharapkan dengan nama yang diharapkan.

### Jadikan README sebagai titik masuk

Wajibkan berkas README di akar repositori sebagai titik awal tunggal yang kanonik. Ia harus menyatakan apa proyeknya, cara membangun dan menjalankannya, cara menjalankan tes, di mana menemukan dokumentasi lebih dalam, siapa pemiliknya, dan cara berkontribusi. README bukan seluruh kumpulan dokumentasi; ia indeks yang menunjuk ke sisanya (bab 2.7). Perlakukan README yang hilang atau basi sebagai cacat, karena itu hal pertama yang dibaca setiap insinyur baru, auditor, atau integrator.

### Bakukan berkas editor dan konfigurasi

Check-in konfigurasi editor dan perkakas bersama ke repositori agar setiap kontributor mendapat perilaku yang konsisten secara otomatis. Berkas `.editorconfig` (berkas sederhana yang tak bergantung editor yang mendefinisikan aturan spasi, indentasi, dan akhir baris) menjaga format dasar seragam di berbagai editor dan sistem operasi. Tambahkan berkas ignore untuk sistem kontrol versi (agar keluaran build dan artefak lokal tidak pernah di-commit), bersama konfigurasi formatter dan linter bersama yang dijelaskan di bab 2.1. Berkas ini membuat konvensi repositori aktif, bukan sekadar terdokumentasi.

### Definisikan konvensi penamaan dan folder

Sepakati konvensi untuk menamai folder dan berkas (huruf, pemisah, tunggal versus jamak, dan akhiran wajib seperti yang menandai tes) dan terapkan secara seragam. Nama harus mengungkap maksud dan cocok dengan kosakata domain yang dipakai di tempat lain dalam organisasi. Tujuannya sederhana: jalur harus mengomunikasikan makna, sehingga membaca nama folder atau berkas memberi tahu Anda apa isinya tanpa membukanya.

### Organisasikan lapisan dan dependensi dengan sengaja

Strukturkan basis kode agar lapisan arsitekturalnya tampak dalam tata letak folder, dan agar dependensi mengalir dalam satu arah yang masuk akal. Kebijakan tingkat lebih tinggi tidak boleh bergantung pada detail tingkat rendah. Kode bersama yang stabil harus berada di tempat banyak modul dapat menjangkaunya tanpa menciptakan siklus. Ketika Anda membuat lapisan menjadi fisik, tercermin dalam pohon direktori, insinyur lebih mungkin menghormatinya, dan pelanggaran lebih mudah dilihat dalam tinjauan dan dalam pemeriksaan dependensi otomatis.

### Tegakkan struktur dengan scaffolding dan templat

Sediakan *[scaffolding](https://en.wikipedia.org/wiki/Scaffold_%28programming%29)*, pembuatan otomatis proyek awal, agar repositori baru dimulai dalam keadaan sudah benar. *Templat* atau *cookiecutter* (kerangka proyek berparameter yang menghasilkan repositori siap pakai dari jawaban atas beberapa pertanyaan) mengkodekan tata letak baku, README, berkas konfigurasi, dan penyiapan [CI](https://en.wikipedia.org/wiki/Continuous_integration) di satu tempat. Ketika insinyur membuat layanan baru dari templat bersama, konsistensi menjadi bawaan alih-alih aspirasi, dan perbaikan pada templat mengalir ke proyek mendatang.

### Jaga struktur tetap konsisten di banyak repositori pada skala besar

Perlakukan tata letak itu sendiri sebagai standar yang diatur: dipelihara secara terpusat seperti standar rekayasa lain (bab 1.7), dan diberi versi seperti kode (bab 2.6). Terbitkan, sediakan templat yang mengimplementasikannya, dan izinkan penyimpangan hanya lewat proses pengecualian terdokumentasi, agar "standar" tetap bermakna. Pada skala portofolio, hampir semua nilai struktur datang dari keseragamannya lintas repositori, jadi penyimpangan adalah risiko utama untuk dikelola.

### Biarkan struktur menginformasikan pilihan monorepo versus multi-repo

Kaitkan struktur dengan keputusan batas repositori yang dibahas di bab 2.6. *[Monorepo](https://en.wikipedia.org/wiki/Monorepo)* (satu repositori yang memegang banyak proyek) membutuhkan konvensi internal yang jelas untuk memisahkan proyek dan kode bersamanya, agar pohon tunggal tetap dapat dinavigasi. Pendekatan *multi-repo* (banyak repositori kecil, satu per proyek atau layanan) membutuhkan konsistensi lintas repo yang kuat, agar setiap repo terasa akrab meskipun berdiri sendiri. Bagaimanapun, struktur yang terdokumentasi dan bertemplat adalah yang menjaga navigasi tetap dapat diprediksi. Pilihan batas mengubah di mana Anda menerapkan konvensi, bukan apakah Anda membutuhkannya.

## Trade-off: kelebihan dan kekurangan

| Pilihan | Kelebihan | Kekurangan |
|---|---|---|
| Tata letak baku ketat seluruh organisasi | Keakraban instan; insinyur portabel; perkakas seragam | Kadang kurang cocok untuk proyek tak lazim; butuh tata kelola |
| Kebebasan tata letak per tim | Optimasi lokal; otonomi tinggi | Fragmentasi; peralihan konteks mahal; perkakas tidak konsisten |
| Scaffolding dan templat | Repo benar secara bawaan; perubahan merambat | Pemeliharaan templat; risiko menyimpang dari repo hasil generate |
| Hierarki folder dalam dan berlapis | Struktur eksplisit; batas jelas | Beban navigasi; jalur panjang; risiko rekayasa berlebihan |
| Tata letak datar dan dangkal | Mudah dipindai; upacara rendah | Pemisahan buruk; runtuh seiring proyek tumbuh |

Trade-off dominan adalah keseragaman versus otonomi. Tata letak baku tunggal menghilangkan gesekan bagi banyak insinyur yang berpindah antarbasis kode, dengan biaya sesekali proyek yang kebutuhannya tidak pas dengan cetakan. Dalam organisasi besar, keuntungan kolektif dari keakraban hampir selalu melampaui kerugian lokal itu. Itulah mengapa sikap yang direkomendasikan adalah standar bawaan yang kuat ditambah jalur pengecualian terdokumentasi (bab 1.7), bukan keseragaman kaku maupun kebebasan tak terkelola. Trade-off sekunder adalah kedalaman versus kesederhanaan: cukup struktur untuk memisahkan perhatian nyata, tetapi tidak begitu banyak sehingga navigasi berubah menjadi pendakian melalui folder kosong.

## Pertanyaan untuk didiskusikan dengan tim Anda

1. **Ketika insinyur berpindah ke repo kita yang asing, berapa lama sampai mereka dapat menemukan tes, konfigurasi deploy, dan pemiliknya?** Ini pajak navigasi yang hendak dihilangkan struktur, dan pada skala portofolio ia dibayar ribuan kali setahun dalam kenaikan kecil yang berjumlah menjadi hilangnya waktu rekayasa yang serius. Inti prinsip paling sedikit kejutan adalah insinyur berpengalaman harus dapat menebak di mana sumber, tes, dokumen, dan deployment berada tanpa membaca manual, jadi ujian jujurnya adalah apakah tebakan itu berhasil di seluruh repo Anda. Bawa angka nyata ke rapat: ukur waktu Anda mengorientasikan diri di dua atau tiga repositori internal yang asing, atau tarik data orientasi tentang berapa lama karyawan baru membuat perubahan pertama. Jika jawabannya diukur dalam hari riset alih-alih menit pengenalan, Anda telah mengkuantifikasi biaya repo kepingan salju, dan itu membenarkan investasi sekali jalan dalam tata letak baku yang dibagikan setiap repo.

2. **Apakah lapisan arsitektural kita tampak dalam pohon folder, atau siklus dependensi bersembunyi dalam tata letak datar?** Struktur lebih dari soal kemudahan ditemukan: ketika Anda membuat lapisan fisik, insinyur menghormatinya dan peninjau serta pemeriksaan dependensi otomatis dapat melihat pelanggaran, sedangkan tumpukan datar membiarkan kopling tidak semestinya dan siklus menyelinap tanpa disadari sampai perubahan menjadi berbahaya. Pada sistem besar berumur panjang inilah yang menjaga kebijakan tingkat lebih tinggi agar tidak diam-diam bergantung pada detail tingkat rendah, dan ini erosi persis yang murah dicegah dan mahal diurai. Bawa graf dependensi Anda atau jalankan pemeriksaan cepat: apakah ada siklus, dan apakah ada yang stabil bergantung pada sesuatu yang mudah berubah? Jawabannya harus mendorong Anda mencerminkan lapisan dalam direktori dan menambahkan pemeriksaan arah dependensi otomatis, agar batas terlihat di pohon dan ditegakkan di pipeline alih-alih hanya hidup di model mental seseorang.

3. **Apakah repositori baru kita dimulai dalam keadaan benar dari templat, atau kita mengandalkan halaman wiki dan niat baik?** Struktur yang ditegakkan scaffolding adalah bawaan; struktur yang dijelaskan dalam dokumen menyimpang, karena kenyataan mengikuti apa yang menghasilkan repo, bukan apa yang dikatakan halaman tentang seperti apa seharusnya. Bagi organisasi besar atau yang diatur ini juga perhatian jaminan: ketika setiap repo dihasilkan dari templat bersama, pemindai keamanan, penganalisis dependensi, dan auditor menemukan lisensi, kebijakan keamanan, spesifikasi, dan definisi build di tempat yang sama setiap kali, lintas vendor dan lintas tahun. Bawa buktinya: berapa banyak repo terbaru Anda yang di-scaffold dari templat baku versus dirakit tangan, dan seberapa jauh yang bertemplat telah menyimpang sejak itu? Tindakannya adalah menjadikan templat satu-satunya cara mudah memulai repo, mengaturnya sebagai standar berversi dengan jalur pengecualian terdokumentasi, dan mendeteksi penyimpangan secara otomatis, karena keseragaman adalah tempat hampir semua nilai struktur hidup.

4. **Sudahkah kita memutuskan apakah standar kita mencakup monorepo atau banyak repositori terpisah, dan apakah konvensi yang sama benar-benar berlaku di kedua sisi batas itu?** Pilihan batas repositori mengubah di mana Anda menerapkan konvensi, bukan apakah Anda membutuhkannya, dan keliru berarti satu pohon raksasa yang tidak dapat dinavigasi siapa pun atau sebaran repo yang masing-masing terasa asing. Monorepo membutuhkan konvensi internal yang jelas untuk memisahkan proyek dan kode bersamanya agar satu pohon tetap dapat dinavigasi, sementara pendekatan multi-repo membutuhkan konsistensi lintas repo yang kuat agar setiap repo berdiri sendiri tetap terasa akrab. Bawa inventaris saat ini: berapa banyak repo Anda, bagaimana kode bersama dipisahkan di dalam monorepo mana pun, dan uji berwaktu apakah insinyur dapat menemukan proyek di dalam pohon besar secepat menemukannya di repo mandiri. Untuk enterprise besar atau program pemerintah di mana vendor berbeda menyerahkan repositori terpisah, putuskan dengan sengaja bagian konvensi mana yang universal dan mana yang khusus batas, karena auditor dan perkakas platform harus bekerja dengan cara yang sama entah kode tiba sebagai satu pohon atau lima puluh.

5. **Siapa yang memiliki standar struktur kita, dan apa yang sebenarnya terjadi ketika proyek benar-benar tidak cocok dengannya?** Pada skala portofolio hampir semua nilai struktur datang dari keseragaman, jadi risiko nyatanya adalah standar tanpa pemilik yang membusuk dan jalur pengecualian begitu samar sehingga setiap tim diam-diam menciptakan tata letaknya sendiri. Ketegangannya antara keseragaman kaku yang tidak cocok dengan proyek tak lazim mana pun dan kebebasan tak terkelola yang memfragmentasi segalanya, dan jawaban sehatnya adalah bawaan kuat ditambah proses pengecualian terdokumentasi yang dapat diaudit, diatur pemilik bernama dan diberi versi seperti kode. Bawa buktinya: apakah ada satu pemilik yang bertanggung jawab, dokumen standar berversi dengan changelog, log pengecualian yang diberikan dan mengapa, dan hitungan penyimpangan tak terdokumentasi yang dapat Anda temukan di alam liar. Dalam lingkungan enterprise dan pemerintah, pengecualian yang tidak dicatat siapa pun adalah celah kendali, jadi kaitkan setiap penyimpangan dengan pembenaran tertulis dan tanggal tinjauan, dan pastikan kontrak pengadaan yang mewajibkan tata letak juga menamai siapa yang boleh menyetujui penyimpangan darinya.

6. **Apakah README dan berkas konfigurasi yang di-check-in membuat konvensi kita aktif, atau hanya dekoratif?** README adalah pintu depan dan `.editorconfig`, berkas ignore, serta konfigurasi linter yang di-check-in adalah yang membuat konvensi menegakkan diri sendiri, namun ini hal pertama yang menjadi basi dan terakhir yang diperhatikan siapa pun sampai auditor atau karyawan baru tidak dapat membangun proyek. Ketegangannya antara README ramping yang tetap mutakhir dan yang menyeluruh yang menyimpang, dan antara memercayai orang memformat kode dengan benar dan membiarkan konfigurasi bersama menegakkannya secara otomatis. Bawa sampel: tarik lima repo dan periksa berapa banyak README yang benar-benar menyatakan apa proyeknya, cara membangun, menguji, dan menjalankannya, serta siapa pemiliknya, dan berapa banyak yang membawa berkas konfigurasi bersama alih-alih mengandalkan kebiasaan individu. Bagi organisasi besar atau yang diatur, di mana integrator, peninjau keamanan, dan pemelihara jangka panjang membaca README sebelum apa pun, perlakukan pintu depan yang hilang atau basi sebagai cacat dengan pemilik, dan periksa keberadaan berkas konfigurasi secara otomatis agar kepatuhan tidak bergantung pada niat baik.

## Lensa sektor

**Startup.** Kecepatan menang, jadi sepakati satu tata letak sederhana dan cukup datar untuk repo pertama Anda (src, test, docs, scripts, README yang terisi, `.editorconfig`, dan berkas ignore) dan simpan sebagai templat ringan pada sore yang sama. Hasilkan layanan kedua darinya agar kedua repo terasa akrab dan kontraktor baru mengorientasikan diri dalam hitungan jam alih-alih merekayasa balik kepingan salju. Tahan diri dari hierarki dalam dan tata kelola berat yang belum Anda butuhkan; seluruh imbal hasil di sini adalah dua pendiri dan seorang kontraktor berbagi satu peta.

**Bisnis kecil.** Tanpa spesialis platform dan dengan anggaran ketat, adopsi tata letak konvensional yang sudah diasumsikan bahasa atau kerangka kerja Anda alih-alih menciptakan sendiri, agar perkakas siap pakai dan karyawan baru mana pun tiba sudah terlatih padanya. Beli scaffolding (generator kerangka kerja atau templat cookiecutter) alih-alih membangun sendiri, dan belanjakan upaya langka Anda menjaga README yang terisi tetap mutakhir. README itu asuransi termurah yang Anda miliki untuk hari ketika satu orang yang mengetahui tata letak berpindah.

**Enterprise.** Di banyak tim dan ratusan repositori tujuannya adalah keseragaman: terbitkan standar struktur berversi, hasilkan setiap layanan baru dari templat bersama, deteksi penyimpangan secara otomatis, dan izinkan penyimpangan hanya lewat proses pengecualian terdokumentasi. Karena setiap repo tampak sama, insinyur yang dipindahkan ke tim baru produktif dalam hitungan jam dan pemindai keamanan serta dependensi seluruh portofolio menemukan lisensi, kebijakan keamanan, dan definisi build di tempat yang sama setiap kali. Anggarkan pemeliharaan templat dan deteksi penyimpangan secara eksplisit, karena pemeliharaan itu yang menjaga standar tetap bermakna pada skala besar.

**Pemerintah.** Pengadaan, transparansi, dan akuntabilitas jangka panjang membentuk tata letak, jadi wajibkan struktur umum dalam standar pengiriman yang mengikat setiap vendor. Wajibkan folder `specification` yang menautkan kode ke persyaratan yang disetujui, berkas lisensi dan kebijakan keamanan di akar, dan folder `deploy` yang memegang definisi infrastruktur sebagai kode, agar auditor menemukan artefak kepatuhan dengan cara yang sama di setiap sistem. Karena kontraktor dari vendor berbeda mengikuti satu peta, pemeliharaan setelah kontrak berakhir memakan biaya jauh lebih sedikit, dan publik memperoleh jejak yang dapat dipertanggungjawabkan dan diperiksa dari persyaratan ke kode yang berjalan.

## Contoh

**Startup.** Sebuah startup tiga orang menyepakati tata letak baku sederhana untuk repo pertamanya (src, test, docs, scripts, README yang terisi, .editorconfig, dan berkas ignore) dan menyimpannya sebagai templat ringan. Ketika mereka menyiapkan layanan kedua sebulan kemudian, mereka menghasilkannya dari templat itu, sehingga kedua repo sudah terasa akrab dan kontraktor baru mengorientasikan diri dalam satu sore. Mereka menolak hierarki folder dalam yang belum dibutuhkan, menjaga pohon cukup datar untuk dipindai sekilas. Biayanya satu sore persiapan, dan menyelamatkan mereka dari sebaran kepingan salju yang jika tidak akan menjadikan setiap repo masa depan proyek riset kecil.

**Enterprise.** Sebuah pengecer multinasional menjalankan ratusan layanan di beberapa bahasa. Tim platformnya menerbitkan standar struktur repositori berversi dan seperangkat templat proyek yang mengimplementasikannya. Setiap layanan baru dihasilkan dari templat, sehingga tiba dengan folder baku `src`, `test`, `docs`, `deploy`, dan `scripts`, README yang terisi, `.editorconfig`, berkas ignore, dan pipeline CI yang berfungsi. Karena setiap repositori tampak sama, insinyur yang dipindahkan ke tim baru produktif dalam hitungan jam, dan pemindai keamanan serta dependensi seluruh organisasi berjalan seragam karena selalu menemukan berkas di tempat yang diharapkan.

**Pemerintah.** Sebuah lembaga nasional yang memodernisasi sistem warisan mewajibkan tata letak repositori umum sebagai bagian dari standar pengirimannya bagi semua vendor. Setiap repositori harus berisi folder `specification` yang menautkan kode ke persyaratan yang disetujui, README terdokumentasi, berkas lisensi dan kebijakan keamanan di akar, dan folder `deploy` yang memegang definisi infrastruktur sebagai kode (bab 8.2). Karena kontraktor dari vendor berbeda semuanya mengikuti struktur yang sama, auditor lembaga dapat menemukan artefak kepatuhan dengan cara yang sama di setiap sistem, dan pemeliharaan jangka panjang setelah kontrak berakhir memakan biaya jauh lebih sedikit karena pemelihara yang datang sudah mengenal petanya.

## Kasus bisnis: motivasi, ROI, dan TCO

Biaya mengadopsi standar struktur sebagian besar sekali jalan: menyepakati tata letak, membangun templat, dan mendokumentasikan konvensi. Biaya berulangnya rendah, terkonsentrasi pada memelihara templat dan mengatur pengecualian. Biaya *tidak* memiliki standar berulang dan berlipat: setiap insinyur yang membuka repo asing membayar pajak navigasi, setiap orientasi berjalan lebih lambat, dan perkakas otomatis harus dikonfigurasi per repo karena tidak ada yang berada di tempat yang Anda harapkan. Di organisasi besar, gesekan kecil ini berlipat menjadi kerugian waktu rekayasa yang serius.

Imbal hasilnya tampak sebagai orientasi lebih cepat, mobilitas antartim yang lebih murah, sinyal lebih tinggi dari perkakas seluruh portofolio, dan, di lingkungan yang diatur, biaya audit dan pemeliharaan jangka panjang yang lebih rendah, karena artefak selalu dapat ditemukan. *Total biaya kepemilikan* (TCO, artinya biaya seumur hidup penuh membangun, menjalankan, dan memelihara sistem) turun paling banyak pada sistem berumur panjang, di mana pemelihara yang diuntungkan struktur yang dapat diprediksi biasanya bukan penulis yang menciptakannya. Untuk meyakinkan pimpinan, bingkai struktur sebagai standar berbiaya rendah berdaya ungkit tinggi yang memperbaiki produktivitas pengembang dan kesiapan audit, dan beri angka pada biaya inkonsistensi hari ini memakai data waktu orientasi dan upaya yang dihabiskan mencari sesuatu di repositori asing.

## Anti-pola dan jebakan

- **Repositori kepingan salju:** setiap repo diorganisasi berbeda, sehingga masing-masing harus dipelajari dari awal.
- **README yang hilang atau basi:** tanpa pintu depan, memaksa pendatang baru merekayasa balik cara membangun dan menjalankan proyek.
- **Struktur lewat dokumen, bukan lewat templat:** halaman wiki menjelaskan tata letak baku, tetapi tak ada yang menghasilkan atau menegakkannya, sehingga kenyataan menyimpang darinya.
- **Penyimpangan templat:** repositori yang dihasilkan dari templat menyimpang seiring waktu dan perbaikan templat tidak pernah mencapai mereka.
- **Hierarki rekayasa berlebihan:** sarang dalam folder nyaris kosong yang menambah upacara tanpa membantu navigasi.
- **Perhatian bercampur:** sumber, tes, keluaran build, dan rahasia tercampur tanpa pemisahan jelas.
- **Keluaran build dan artefak lokal yang di-commit:** berkas hasil generate di-check-in karena aturan ignore tidak pernah disiapkan, mencemari riwayat dan diff.
- **Pelanggaran lapisan yang disembunyikan struktur datar:** tanpa batas fisik, sehingga siklus dependensi dan kopling tidak semestinya menyelinap tanpa disadari.

## Model kematangan

- **Tingkat 1 (Memulai):** Setiap repositori diorganisasi ad hoc oleh penulisnya, bereaksi terhadap apa pun yang dibutuhkan saat itu; tata letak sangat bervariasi; README hilang atau tidak andal; pendatang baru harus dituntun melalui setiap repo dengan tangan.
- **Tingkat 2 (Mengembangkan):** Konvensi dasar ada secara informal dan banyak repo menyerupai satu sama lain; sebagian tim menyimpan tata letak awal sendiri; tetapi tidak ada standar berwenang, tidak ada scaffolding bersama, dan struktur menyimpang terasa dari satu tim ke tim berikutnya.
- **Tingkat 3 (Membakukan):** Standar struktur terdokumentasi dan berversi ditegakkan di seluruh organisasi; repositori baru dihasilkan dari templat bersama yang membawa tata letak baku, README, berkas konfigurasi, dan CI; penyimpangan melalui proses pengecualian terdokumentasi alih-alih terjadi diam-diam.
- **Tingkat 4 (Mengelola):** Kepatuhan pada standar diukur dan dikendalikan dengan data: pemeriksaan otomatis melaporkan persentase repo yang cocok dengan tata letak, seberapa jauh repo bertemplat telah menyimpang, kelengkapan README, dan pelanggaran arah dependensi, semuanya dilacak terhadap garis dasar; waktu orientasi dan navigasi diukur; pengecualian dicatat dan ditinjau, dan perubahan templat disetujui berdasarkan bukti alih-alih opini.
- **Tingkat 5 (Mengorkestrasi):** Struktur terus diperbaiki dan adaptif: perbaikan templat merambat secara otomatis ke repositori yang ada, tata kelola struktur terintegrasi dengan perkakas keamanan, kepatuhan, dan platform, dan standar berkembang dengan sengaja seiring bergesernya bahasa, arsitektur, dan portofolio, menjaga keseragaman tetap tinggi sementara organisasi berubah di sekitarnya.

## Gagasan untuk didiskusikan

- Folder tingkat atas mana yang harus benar-benar universal di organisasi Anda, dan mana yang opsional?
- Bagaimana Anda menjaga repositori yang dihasilkan dari templat agar tidak menyimpang darinya seiring waktu?
- Di mana garis antara hierarki berlapis yang membantu dan upacara folder yang direkayasa berlebihan?
- Bagaimana standar struktur Anda harus berbeda, jika ada, antara pendekatan monorepo dan multi-repo?
- Apa proses pengecualian yang tepat untuk proyek yang kebutuhan sejatinya tidak cocok dengan tata letak baku?
- Berapa banyak struktur Anda yang dapat diperiksa secara otomatis, dan apa yang masih bergantung pada tinjauan manusia?
- Siapa yang memiliki standar struktur dan templatnya, dan bagaimana perubahan diusulkan dan diluncurkan?

## Poin-poin utama

- Organisasikan setiap repositori agar insinyur mana pun dapat menavigasi basis kode mana pun menurut ekspektasi, mengikuti prinsip paling sedikit kejutan.
- Adopsi tata letak tingkat atas yang konsisten (sumber, tes, dokumen, build, deploy, skrip, contoh, spesifikasi) dan jadikan README sebagai titik masuk.
- Check-in konfigurasi editor dan perkakas (seperti `.editorconfig`) agar konvensi aktif, bukan sekadar tertulis.
- Tegakkan struktur dengan scaffolding dan templat agar repositori baru benar secara bawaan.
- Pada skala besar, nilainya ada pada keseragaman: atur standar, kelola penyimpangan, dan izinkan penyimpangan hanya lewat pengecualian terdokumentasi.

## Referensi dan bacaan lanjutan

- Robert C. Martin, *Clean Architecture: A Craftsman's Guide to Software Structure and Design*
- Steve McConnell, *Code Complete: A Practical Handbook of Software Construction*
- Andrew Hunt dan David Thomas, *The Pragmatic Programmer*
- Titus Winters, Tom Manshreck, dan Hyrum Wright (eds.), *Software Engineering at Google*
- Scott Chacon dan Ben Straub, *Pro Git*
- Dokumentasi proyek EditorConfig (sebagai standar rujukan untuk konfigurasi editor)
