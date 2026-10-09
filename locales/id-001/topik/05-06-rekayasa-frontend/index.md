# 5.6 Rekayasa frontend

## Tinjauan dan motivasi

Rekayasa frontend adalah disiplin membangun lapisan perangkat lunak yang menghadap klien: kode yang berjalan di peramban atau di perangkat dan mengubah desain, konten, dan data menjadi antarmuka yang berfungsi. Ia mencakup pilihan kerangka kerja dan arsitektur, strategi render, manajemen status, kinerja, dan ketahanan di seluruh keragaman luar biasa peramban, perangkat, dan kondisi jaringan di dunia nyata. Frontend adalah tempat semua kerja hulu (UX, desain, konten, aksesibilitas, internasionalisasi) entah mencapai pengguna dengan berhasil atau runtuh.

Bagi tim besar, frontend secara unik menantang, karena ia terpapar pada lingkungan yang tidak dikendalikan organisasi. Peramban, perangkat, koneksi, dan pengaturan pengguna sangat bervariasi, dan platform (web) berevolusi terus-menerus. Pada skala besar, pilihan arsitektural berlipat. Kerangka kerja yang dipilih hari ini membatasi perekrutan, kinerja, dan kemudahan pemeliharaan selama bertahun-tahun, dan ribuan keputusan kecil tentang ukuran bundle dan render berjumlah menjadi pengalaman yang benar-benar didapat pengguna. Standar bersama, pustaka komponen, anggaran kinerja, dan pola arsitektural adalah yang menjaga banyak tim independen agar tidak menghasilkan keseluruhan yang lambat, tidak konsisten, dan rapuh.

Relevansi enterprise dan pemerintah akut. Enterprise memelihara aplikasi berumur panjang di mana umur panjang kerangka kerja dan kemudahan pemeliharaan lebih penting daripada kebaruan, dan di mana banyak tim harus berinteroperasi. Pemerintah melayani seluruh publik, termasuk orang pada perangkat lama, koneksi lambat atau berkuota, dan teknologi bantu. Itu membuat kinerja, [peningkatan progresif](https://en.wikipedia.org/wiki/Progressive_enhancement), dan ketahanan bukan polesan opsional melainkan beda antara layanan yang berfungsi untuk semua orang dan yang mengecualikan yang paling tak beruntung. Layanan pemerintah yang hanya berfungsi pada ponsel terbaru dengan koneksi cepat gagal pada mandatnya.

## Prinsip utama

- Frontend berjalan di lingkungan yang tidak Anda kendalikan; rancang untuk variabilitas dan kegagalan.
- Pilih teknologi membosankan dan tahan lama untuk sistem berumur panjang; optimalkan kemudahan pemeliharaan dan perekrutan.
- Kinerja adalah fitur dan, bagi banyak pengguna, prasyarat akses.
- Peningkatan progresif: sampaikan pengalaman inti yang berfungsi lebih dulu, lalu lapisi peningkatan.
- Kirim lebih sedikit kode; kode tercepat dan terandal adalah kode yang tidak Anda kirim.
- Cocokkan strategi render dengan jenis konten dan kebutuhan pengguna, bukan mode.
- Ketahanan: antarmuka harus merosot dengan anggun, bukan rusak, ketika sesuatu salah.
- Standar dan fitur platform hidup lebih lama daripada kerangka kerja; bersandarlah pada platform.

## Rekomendasi

### Pilih kerangka kerja untuk umur panjang dan kecocokan, bukan sensasi

Pilih teknologi frontend berdasarkan masalah, tim, cakrawala pemeliharaan, dan pasar perekrutan, bukan apa yang sedang tren. Untuk sistem enterprise dan pemerintah berumur panjang, pilih teknologi matang dan didukung baik dengan kolam talenta besar, praktik rilis stabil, dan jalur peningkatan yang jelas. Timbang total biaya churn kerangka kerja: penulisan ulang mahal dan berisiko. Pilih pendekatan yang bersandar pada [standar web](https://en.wikipedia.org/wiki/Web_standards) agar investasi Anda selamat dari pergantian kerangka kerja, dan isolasi kode khusus kerangka kerja di balik batas agar aplikasi tidak tersandera siklus hidup satu pustaka.

### Cocokkan strategi render dengan kebutuhan

Strategi render utama masing-masing cocok untuk konten berbeda. Server-side rendering (SSR) menghasilkan first paint cepat dan SEO ([optimasi mesin pencari](https://en.wikipedia.org/wiki/Search_engine_optimization)) yang baik serta berfungsi tanpa JavaScript klien, cocok untuk halaman padat konten dan menghadap publik. [Static site generation](https://en.wikipedia.org/wiki/Static_site_generator) (SSG) pra-render saat build untuk kecepatan dan kemampuan cache maksimum, ideal untuk konten yang jarang berubah. Client-side rendering (CSR) cocok untuk pengalaman sangat interaktif ala aplikasi di balik autentikasi. Streaming dan hidrasi progresif mengirim dan mengaktifkan halaman secara bertahap agar pengguna melihat dan memakai konten lebih cepat. Banyak sistem besar memadukan ini per rute alih-alih memilih satu secara global. Kelola status dengan sengaja: jaga status server, status URL, dan status UI lokal tetap berbeda, dan hindari mensentralisasi segalanya ke satu penyimpanan global yang berat.

### Perlakukan kinerja sebagai disiplin yang dianggarkan dan diukur

Adopsi anggaran kinerja (batas eksplisit pada ukuran bundle, jumlah permintaan, dan metrik kunci) dan tegakkan di CI agar regresi menggagalkan build. Lacak Core Web Vitals (pemuatan, interaktivitas, dan stabilitas visual) memakai pemantauan pengguna nyata dari perangkat dan jaringan sebenarnya, bukan hanya tes lab pada mesin cepat. Kurangi JavaScript secara agresif: code-split dan [lazy-load](https://en.wikipedia.org/wiki/Lazy_loading) agar pengguna mengunduh hanya apa yang dibutuhkan tampilan tertentu, tunda pekerjaan nonkritis, dan pilih kemampuan platform daripada pustaka berat. Optimalkan gambar dan font, cache secara efektif, dan ukur pada perangkat kelas bawah representatif dan koneksi lambat.

### Bangun dengan peningkatan progresif dan ketahanan

Mulai dari garis dasar yang berfungsi dengan HTML semantik dan JavaScript minimal atau tanpa, lalu tingkatkan untuk klien yang mumpuni. Ini memastikan tugas inti tetap mungkin ketika skrip gagal dimuat, perangkat sudah tua, atau jaringan goyah, kenyataan umum alih-alih kasus tepi. Tangani galat dengan anggun: tampilkan keadaan berguna untuk kondisi memuat, kosong, galat, dan offline alih-alih layar kosong atau spinner tak berujung. Untuk layanan yang diandalkan orang, pertimbangkan teknik offline-first agar aplikasi tetap dapat dipakai melalui konektivitas terputus-putus, menyinkronkan ketika koneksi kembali.

### Pastikan kompatibilitas lintas peramban, lintas perangkat, dan teknologi bantu

Uji di seluruh peramban, perangkat, dan teknologi bantu yang benar-benar dimiliki pengguna Anda, diinformasikan oleh analitik nyata alih-alih mesin tim sendiri. Gunakan peningkatan progresif dan deteksi fitur alih-alih mengasumsikan fitur platform terbaru tersedia di mana-mana. Bangun secara [responsif](https://en.wikipedia.org/wiki/Responsive_web_design) (lihat bab sistem desain) agar satu basis kode melayani ponsel hingga desktop. Integrasikan aksesibilitas dan internasionalisasi ke arsitektur frontend sejak awal, bukan sebagai putaran belakangan.

### Atur frontend sebagai infrastruktur bersama

Sediakan pustaka komponen bersama, linting, pemformatan, dan perkakas build agar tim konsisten dan produktif. Tetapkan panduan arsitektural (cara menyusun aplikasi, mengelola status, dan memecah bundle) dan anggaran kinerja yang ditegakkan di CI. Untuk frontend yang sangat besar, pertimbangkan arsitektur modular atau micro-frontend yang memungkinkan tim men-deploy secara independen, tetapi timbang dengan hati-hati kompleksitas tambahan dan biaya kinerja, karena tidak gratis.

## Trade-off: kelebihan dan kekurangan

| Keputusan | Kelebihan | Kekurangan |
|---|---|---|
| Kerangka kerja populer yang matang | Kolam talenta besar, stabil, didukung | Mungkin membawa beban warisan; lebih lambat mengadopsi fitur terbaru |
| Kerangka kerja terbaru | Fitur modern, peningkatan kinerja | Risiko churn, kolam talenta kecil, umur panjang tak pasti |
| SSR / SSG | First paint cepat, SEO, berfungsi tanpa JS | Kompleksitas server atau build, tantangan caching |
| CSR (SPA) | Interaktivitas kaya, nuansa ala aplikasi | Muat pertama lambat, bergantung JS, biaya SEO dan ketahanan |
| JavaScript klien berat | Fitur kaya | Kinerja buruk pada perangkat kelas bawah, rapuh |
| Peningkatan progresif | Tangguh, inklusif, berfungsi di mana-mana | Lebih banyak upaya desain mendefinisikan garis dasar yang berfungsi |
| Micro-frontend | Deploy tim independen, skala | Kompleksitas, dependensi terduplikasi, beban kinerja |

Trade-off yang berulang adalah kekayaan dan kenyamanan pengembang versus jangkauan, kinerja, dan ketahanan. Pendekatan sisi klien berat menyenangkan dibangun dan didemokan pada mesin cepat, tetapi mengecualikan pengguna pada perangkat dan jaringan lemah. Untuk audiens enterprise dan terutama pemerintah, condongkan keseimbangan ke kinerja, peningkatan progresif, dan ketahanan, karena biaya mengecualikan pengguna tinggi dan sering tak dapat ditawar.

## Pertanyaan untuk didiskusikan dengan tim Anda

1. **Bagaimana kita mengisolasi kode khusus kerangka kerja agar aplikasi tidak tersandera siklus hidup satu pustaka?** Untuk sistem enterprise dan pemerintah berumur panjang, churn kerangka kerja adalah pengeluaran terbesar yang dapat dihindari: penulisan ulang mahal dan berisiko, dan pustaka tren hari ini membatasi perekrutan dan pemeliharaan selama bertahun-tahun. Bersandar pada standar web dan menaruh kode khusus kerangka kerja di balik batas yang jelas berarti logika bisnis dan konten Anda selamat dari pergantian kerangka kerja berikutnya. Putuskan di mana sambungan itu berada dan apakah insinyur baru dapat membedakan kode platform dari kode kerangka kerja. Bawa estimasi biaya migrasi kerangka kerja terakhir Anda, atau biaya yang akan datang. Jika logika inti Anda melekat pada API satu pustaka, hargai kopling itu sebelum membela pilihan kerangka kerja.

2. **Apakah kita mencocokkan strategi render per rute, atau memaksakan satu strategi pada seluruh produk?** Server-side rendering memberi first paint cepat dan berfungsi tanpa JavaScript klien untuk konten publik, static generation memaksimalkan kecepatan untuk halaman yang jarang berubah, dan client rendering cocok untuk permukaan interaktif ala aplikasi di balik login. Memaksakan satu secara global entah memperlambat halaman publik dengan JavaScript berat atau merekayasa berlebihan halaman konten sederhana. Ini pertanyaan jangkauan bagi pemerintah, di mana layanan yang hanya berfungsi setelah bundle besar dimuat mengecualikan pengguna pada perangkat lama dan koneksi lambat. Bawa rute kunci Anda dan beri label masing-masing dengan strategi yang benar-benar dipakai hari ini. Jika halaman menghadap publik butuh JavaScript untuk menampilkan kontennya, putuskan apakah itu pilihan sengaja atau kecelakaan.

3. **Seberapa disiplin manajemen status kita, dan apakah kita mensentralisasi segalanya ke satu penyimpanan global berat?** Menjaga status server, status URL, dan status UI lokal tetap berbeda mencegah kopling dan badai render ulang yang membuat frontend besar lambat dan rapuh, namun bawaan yang menggoda adalah menumpahkan segalanya ke satu penyimpanan global. Ini berlipat pada skala besar, di mana banyak tim menyentuh satu penyimpanan bersama menciptakan dependensi tersembunyi dan kinerja tak terduga. Sepakati di mana setiap jenis status berada dan apa yang tidak termasuk dalam penyimpanan global. Bawa komponen yang merender ulang lebih dari seharusnya dan telusuri mengapa. Jika jawabannya penyimpanan pusat yang membengkak, putuskan batasnya sebelum kopling mengeras.

4. **Apa anggaran kinerja kita, apakah menggagalkan build di CI, dan apakah diukur pada perangkat yang benar-benar dimiliki pengguna kita?** Anggaran yang tak ditegakkan siapa pun adalah angan-angan, dan anggaran yang diukur hanya pada laptop cepat tim menggambarkan pengguna yang tidak ada. Bagi organisasi besar, anggaran adalah satu-satunya mekanisme yang menjaga ukuran bundle dan Core Web Vitals terkendali seiring puluhan tim menambah fitur ke permukaan bersama, karena tak ada peninjau tunggal yang dapat menangkap setiap regresi dengan mata. Tekanan yang bersaing adalah kecepatan pengiriman: kegagalan build keras atas beberapa kilobyte terasa menghalangi sampai Anda menghargai pengabaian yang dicegahnya. Bawa anggaran Anda saat ini, data pemantauan pengguna nyata dari perangkat kelas bawah dan koneksi lambat, dan daftar rilis di mana regresi lolos. Di pemerintah, di mana mandatnya melayani seluruh publik termasuk orang di ponsel lama dan data berkuota, kaitkan anggaran dengan sepersepuluh pengguna terlambat Anda alih-alih median, dan jadikan gerbang CI tak dapat ditawar.

5. **Layanan mana milik kita yang harus tetap berfungsi tanpa JavaScript klien, dan sudahkah kita benar-benar menguji jalur itu?** Peningkatan progresif mudah diklaim dan mudah dirusak diam-diam, karena jalur yang ditingkatkan adalah yang dipakai pengembang setiap hari sementara garis dasar membusuk tak teruji. Memutuskan ini dengan sengaja penting pada skala besar, karena banyak tim yang merilis ke satu platform masing-masing akan mengasumsikan skrip selalu dimuat kecuali standar bersama mengatakan sebaliknya, dan satu dependensi keras dapat merusak tugas inti bagi siapa pun yang bundle-nya gagal. Pertukarannya nyata: garis dasar tanpa JavaScript yang berfungsi memakan upaya desain dan membatasi cara Anda membangun interaktivitas. Bawa perjalanan pengguna kritis Anda, tes yang memuat masing-masing dengan skrip dimatikan atau gagal, dan bukti seberapa sering skrip benar-benar gagal dimuat di lapangan. Untuk layanan publik, formulir tunjangan atau pajak yang runtuh ketika satu skrip timeout bukan pengalaman yang merosot, melainkan warga yang tak dapat menyelesaikan kewajiban hukum, jadi perlakukan garis dasar sebagai persyaratan kepatuhan, bukan basa-basi.

6. **Kapan micro-frontend benar-benar membayar kompleksitasnya, dan siapa yang memutuskan sebelum tim meraihnya?** Deploy tim independen menarik, tetapi micro-frontend membawa kompleksitas sistem terdistribusi, dependensi terduplikasi, dan pajak kinerja yang dibayar pengguna dalam muat lebih lambat. Tanpa titik keputusan bersama, tim ambisius mengadopsinya demi kenyamanan organisasi jauh sebelum skala membenarkan biayanya, dan seluruh produk mewarisi bebannya. Pertimbangan yang bersaing adalah otonomi: tim yang merilis pada satu basis kode bersama dapat saling memblokir, dan pada skala sejati kopling itu masalah mahal tersendiri. Bawa jumlah tim yang menyentuh permukaan, pertengkaran deploy yang benar-benar Anda alami hari ini, dan estimasi terukur duplikasi muatan yang akan diperkenalkan pemecahan. Untuk platform enterprise dan pemerintah, di mana keputusan arsitektur mengikat banyak tim selama bertahun-tahun dan harus selamat dari audit dan serah terima, wajibkan ambang terdokumentasi eksplisit dan pemilik yang menyetujui langkah itu, alih-alih membiarkan setiap tim memutuskan sendiri.

## Lensa sektor

**Startup.** Kecepatan dan jangkauan sama-sama penting ketika setiap pendaftaran berarti, jadi tahan diri dari single-page app berat untuk halaman publik. Server-render pemasaran dan alur pendaftaran Anda agar dimuat cepat pada ponsel kelas menengah dan data tersendat yang dipakai pelanggan awal Anda, dan sisihkan interaktivitas sisi klien untuk aplikasi di balik login. Tetapkan satu anggaran ukuran bundle sederhana di CI agar dependensi ceroboh tidak diam-diam membengkakkan halaman, dan bersandarlah pada standar web agar basis kode kecil tetap mudah dipelihara seiring Anda merekrut.

**Bisnis kecil.** Tanpa spesialis frontend khusus dan dengan anggaran ketat, pilih kerangka kerja arus utama yang didukung baik atau pembangun situs ter-hosting daripada apa pun yang pesanan, agar Anda merekrut dari kolam talenta besar dan membeli pemeliharaan alih-alih mengisi stafnya. Bingkai pilihan sebagai ketahanan: opsi termurah adalah yang tidak dipaksa Anda tulis ulang dalam dua tahun. Desak halaman cepat, ramah seluler, dan markup yang dapat diakses secara bawaan, karena checkout yang lambat atau rusak membuat Anda kehilangan pelanggan yang tak sanggup Anda lepas.

**Enterprise.** Masalahnya konsistensi lintas banyak tim: pustaka komponen bersama, pola arsitektural yang disepakati, linting dan perkakas build, dan anggaran kinerja yang ditegakkan di CI agar tak ada tim yang dapat diam-diam meregresi keseluruhan. Pilih kerangka kerja untuk umur panjang dan perekrutan alih-alih kebaruan, isolasi kode khusus kerangka kerja di balik batas untuk selamat dari migrasi berikutnya, dan cocokkan strategi render per permukaan. Kelola frontend sebagai infrastruktur bersama dengan pemantauan pengguna nyata, tata kelola, dan catatan teraudit mengapa setiap pilihan arsitektural dibuat.

**Pemerintah.** Anda melayani seluruh publik, termasuk orang pada perangkat lama, koneksi lambat atau berkuota, dan teknologi bantu, sehingga peningkatan progresif dan kinerja adalah kewajiban, bukan polesan. Jadikan garis dasar tanpa JavaScript yang berfungsi sebagai aturan keras untuk layanan yang menghadap warga, anggarkan halaman untuk pengguna terlambat alih-alih median, dan jaga tugas inti dapat diselesaikan ketika skrip gagal. Pengadaan dan transparansi berlaku: pilih teknologi tahan lama yang condong ke standar yang menghindari lock-in satu vendor, dokumentasikan persyaratan aksesibilitas dan kinerja dalam kontrak, dan mampu menunjukkan bahwa layanan berfungsi untuk pengguna paling tak beruntung, bukan hanya perangkat demo.

## Contoh

**Startup.** Startup tahap benih tergoda membangun situs pemasaran dan alur pendaftarannya sebagai single-page app berat, tetapi pelanggan targetnya pembeli yang sering memakai ponsel kelas menengah dengan data seluler tersendat. Kedua pendiri sebagai gantinya menyajikan halaman publik dengan server-render agar dimuat cepat dan berfungsi sebelum JavaScript berjalan, dan menyisihkan interaktivitas sisi klien untuk aplikasi di balik login. Mereka menetapkan anggaran ukuran bundle sederhana di CI agar dependensi ceroboh tidak diam-diam membengkakkan halaman. Muat pertama yang ramping dan cepat terukur meningkatkan pendaftaran, dan bersandar pada standar web menjaga basis kode kecil mereka mudah dipelihara seiring mereka merekrut.

**Enterprise.** Sebuah firma layanan keuangan memodernisasi serangkaian aplikasi internal dan pelanggan yang luas dengan membakukan pada kerangka kerja matang, pustaka komponen bersama, dan anggaran kinerja yang ditegakkan di CI. Strategi render dipilih per permukaan: halaman server-render yang dapat di-cache untuk pemasaran dan konten publik, dan aplikasi client-render di balik login untuk dasbor interaktif. Anggaran bundle dan pemantauan pengguna nyata menangkap regresi sebelum rilis, menjaga waktu muat tetap cepat di banyak tim firma dan mengurangi risiko churn kerangka kerja yang sebelumnya memaksa penulisan ulang mahal.

**Pemerintah.** Sebuah tim layanan digital nasional membangun layanan yang menghadap warga dengan peningkatan progresif sebagai aturan keras: setiap layanan berfungsi dengan HTML semantik dan server-render lebih dulu, dan JavaScript hanya meningkatkan. Ini menjamin layanan berfungsi pada ponsel lama, koneksi pedesaan lambat, dan teknologi bantu, populasi yang tak dapat dikecualikan pemerintah. Anggaran kinerja menjaga halaman ringan dan cepat pada perangkat kelas bawah, dan degradasi anggun berarti skrip yang gagal tidak pernah memblokir seseorang menyelesaikan permohonan tunjangan. Hasilnya layanan yang cepat, tangguh, dapat diakses, dan dapat dipakai seluruh publik.

## Kasus bisnis: motivasi, ROI, dan TCO

Pilihan rekayasa frontend menggerakkan pendapatan, jangkauan, dan biaya. Kinerja terkait langsung dengan konversi, keterlibatan, dan penyelesaian tugas. Pengalaman lebih cepat terukur mengungguli yang lebih lambat, dan bagi pengguna pada perangkat lemah, kinerja adalah garis antara memakai layanan dan meninggalkannya. Peningkatan progresif dan dukungan lintas perangkat memperluas audiens yang dapat dijangkau, yang bagi pemerintah adalah mandat dan bagi enterprise pangsa pasar. Pilihan kerangka kerja dan arsitektur yang sehat mengurangi frekuensi dan biaya penulisan ulang, pengeluaran terbesar yang dapat dihindari dalam rekayasa frontend.

Pada TCO, biaya adopsi adalah disiplin anggaran kinerja dan pengujian, upaya peningkatan progresif, dan investasi pada perkakas bersama dan pustaka komponen. Biaya tidak mengadopsi dibayar dalam pengalaman lambat yang kehilangan pengguna dan pendapatan, pengecualian pengguna kelas bawah dan teknologi bantu (dengan paparan hukum di pemerintah), aplikasi rapuh yang rusak di lapangan, dan churn kerangka kerja serta penulisan ulang mahal yang digerakkan mengejar tren. Masalah frontend muncul sebagai pengabaian dan beban dukungan yang menyebar alih-alih satu butir baris, sehingga mudah kurang diinvestasikan.

Untuk mengajukan kasus kepada pimpinan, kaitkan Core Web Vitals dan waktu muat dengan funnel konversi dan penyelesaian, kuantifikasi pengguna yang dikecualikan oleh pendekatan sisi klien berat, dan hargai biaya penulisan ulang masa lalu atau yang membayangi terhadap stabilitas arsitektur tahan lama dan condong ke standar. Bingkai anggaran kinerja dan peningkatan progresif sebagai pengurangan risiko dan perluasan jangkauan.

## Anti-pola dan jebakan

- **Mengejar kerangka kerja**: menulis ulang pada pustaka terbaru, menimbulkan churn tanpa manfaat pengguna.
- **Pengalaman hanya-JavaScript**: tidak ada yang berfungsi sampai bundle besar dimuat dan berjalan, mengecualikan banyak pengguna.
- **Menguji hanya di perangkat cepat**: laptop unggulan tim menyembunyikan pengalaman pengguna nyata.
- **Mengabaikan ukuran bundle**: pertumbuhan dependensi tak terbatas sampai halaman lambat di mana-mana.
- **Tanpa anggaran kinerja**: regresi menumpuk diam-diam rilis demi rilis.
- **Kegagalan layar kosong**: tanpa keadaan memuat, kosong, galat, atau offline; permintaan gagal merusak halaman.
- **Status global terlalu terpusat**: segalanya dalam satu penyimpanan, menciptakan kopling dan badai render ulang.
- **Micro-frontend prematur**: kompleksitas sistem terdistribusi dan muatan terduplikasi tanpa skala yang membenarkan.
- **Mengabaikan aksesibilitas dan i18n dalam arsitektur**: menempelkannya belakangan dengan biaya tinggi.

## Model kematangan

**Tingkat 1: Memulai.** Frontend ad hoc dibangun per tim tanpa standar bersama. Kode sisi klien berat, tanpa anggaran kinerja, diuji hanya di perangkat tim sendiri. Pilihan kerangka kerja dibuat karena preferensi atau sensasi, dan skrip yang gagal dapat membuat pengguna menatap layar kosong.

**Tingkat 2: Mengembangkan.** Beberapa tim mengadopsi perkakas bersama dan pustaka komponen, tetapi praktik tidak konsisten di seluruh organisasi. Kinerja diukur sesekali alih-alih dianggarkan atau ditegakkan. Strategi render sering seragam terlepas dari jenis konten, dan pengujian lintas perangkat terbatas dan manual.

**Tingkat 3: Membakukan.** Kerangka kerja dan arsitektur dipilih dengan sengaja untuk umur panjang, dan pilihan itu terdokumentasi dan ditegakkan di seluruh organisasi. Strategi render dicocokkan per permukaan, peningkatan progresif dan degradasi anggun adalah standar, dan pustaka komponen bersama, linting, dan perkakas build berlaku bagi setiap tim. Lintas peramban, aksesibilitas, dan internasionalisasi dibangun masuk alih-alih ditempelkan.

**Tingkat 4: Mengelola.** Frontend diukur dan dikendalikan dengan data. Anggaran kinerja ditegakkan di CI agar regresi menggagalkan build, dan Core Web Vitals dilacak dengan pemantauan pengguna nyata dari perangkat kelas bawah dan koneksi lambat sebenarnya terhadap garis dasar eksplisit. Ukuran bundle, cakupan keadaan galat dan offline, dan bagian pengguna yang dilayani pada koneksi paling lambat dilaporkan dan ditinjau, sehingga keputusan bertumpu pada bukti alih-alih opini.

**Tingkat 5: Mengorkestrasi.** Kinerja, ketahanan, dan jangkauan terus diperbaiki dan terkait hasil bisnis di seluruh organisasi. Frontend bersandar pada standar web untuk ketahanan, mengisolasi dependensi kerangka kerja agar migrasi murah, dan mengembangkan arsitektur secara adaptif seiring perangkat, platform, dan data pengguna nyata bergeser. Seluruh publik dan semua perangkat adalah kelas satu, dan praktik frontend terintegrasi dengan desain, aksesibilitas, dan perencanaan produk alih-alih diperlakukan sebagai perhatian terpisah.

## Gagasan untuk didiskusikan

- Bagaimana Anda memutuskan kapan migrasi kerangka kerja layak biaya dan risikonya?
- Core Web Vitals dan anggaran bundle apa yang harus menjadi ambang yang menggagalkan build?
- Di mana peningkatan progresif esensial, dan di mana aplikasi sisi klien dapat diterima?
- Bagaimana Anda menjaga arsitektur frontend konsisten lintas banyak tim otonom?
- Kapan micro-frontend benar-benar membayar kompleksitasnya?
- Bagaimana pengujian perangkat nyata dan jaringan lambat harus dibangun ke dalam pipeline?

## Poin-poin utama

- Frontend berjalan di lingkungan yang tidak Anda kendalikan: rancang untuk variabilitas dan kegagalan.
- Pilih teknologi tahan lama dan didukung baik untuk sistem berumur panjang; bersandarlah pada standar web.
- Cocokkan strategi render (SSR, SSG, CSR, streaming) dengan konten dan kebutuhan, sering dipadukan per rute.
- Perlakukan kinerja sebagai disiplin yang dianggarkan dan diukur yang ditegakkan di CI dengan data pengguna nyata.
- Bangun dengan peningkatan progresif agar pengalaman inti berfungsi di mana-mana.
- Kirim lebih sedikit JavaScript; code-split, lazy-load, dan pilih kemampuan platform.
- Khususnya untuk pemerintah, kinerja dan ketahanan adalah prasyarat akses yang adil.

## Referensi dan bacaan lanjutan

- Jeremy Keith, *Resilient Web Design*
- Aaron Gustafson, *Adaptive Web Design* (peningkatan progresif)
- Steve Souders, *High Performance Web Sites*
- Ilya Grigorik, *High Performance Browser Networking*
- Addy Osmani, tulisan tentang kinerja, code-splitting, dan biaya JavaScript
- Google, *Web Vitals* dan panduan kinerja web.dev
- MDN Web Docs, rujukan platform web dan peningkatan progresif
- Alex Russell, esai tentang biaya JavaScript dan keragaman perangkat
- UK Government Digital Service, panduan peningkatan progresif dan frontend
- WHATWG HTML Living Standard dan spesifikasi platform web W3C
