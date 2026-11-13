# 9.4 Biaya, keberlanjutan, dan perangkat lunak hijau

## Tinjauan dan motivasi

Perangkat lunak berjalan di infrastruktur fisik yang mengonsumsi uang, listrik, air, dan material. Sepanjang sebagian besar sejarah komputasi, biaya ini adalah masalah orang lain: anggaran modal menyembunyikan perangkat keras, dan energi tak terlihat oleh insinyur. [Komputasi awan](https://en.wikipedia.org/wiki/Cloud_computing) mengubah itu. Ia membuat konsumsi granular, sesuai permintaan, dan dapat diatribusikan langsung, yang mengubah biaya, dan makin karbon, menjadi perhatian rekayasa. Bab ini membahas dua disiplin yang saling berkelindan: **FinOps**, praktik membawa akuntabilitas finansial pada pengeluaran cloud yang variabel, dan **[perangkat lunak hijau](https://en.wikipedia.org/wiki/Green_computing)**, praktik membangun sistem yang mengerjakan pekerjaan sama dengan energi lebih sedikit dan emisi karbon lebih rendah. Keduanya tumpang tindih besar, karena perangkat lunak efisien biasanya lebih murah sekaligus lebih bersih.

Bagi tim besar, angkanya sangat besar. Tagihan cloud untuk enterprise besar dapat mencapai puluhan atau ratusan juta per tahun, dan beberapa poin pemborosan mewakili uang nyata yang dapat mendanai headcount atau produk. [Jejak karbon](https://en.wikipedia.org/wiki/Carbon_footprint) properti digital besar juga material, dan organisasi menghadapi tekanan yang tumbuh dari regulator, investor, pelanggan, dan karyawan sendiri untuk mengukur dan menguranginya. Ketika ratusan tim masing-masing membuat keputusan independen tentang ukuran instans, retensi data, dan arsitektur, ketidakefisienan kecil bertambah menjadi biaya dan emisi besar. Tata kelola yang membuat biaya dan karbon terlihat dan akuntabel esensial untuk menjaga keduanya terkendali.

Relevansi enterprise dan pemerintah langsung. Organisasi sektor publik membelanjakan uang pembayar pajak dan makin terikat mandat keberlanjutan dan komitmen net-zero, sehingga mendemonstrasikan operasi efisien dan rendah karbon adalah kewajiban fiskal dan kebijakan. Enterprise menghadapi pengawasan investor atas kinerja lingkungan dan tekanan kompetitif pada margin. Dalam kedua pengaturan, biaya dan keberlanjutan telah bergeser dari renungan belakangan menjadi perhatian tingkat dewan. Pilihan rekayasa adalah tempat perhatian itu akhirnya terwujud atau terlewat.

## Prinsip utama

- **Jadikan konsumsi terlihat.** Anda tak dapat mengoptimalkan apa yang tak dapat Anda lihat; biaya dan karbon harus diatribusikan ke tim dan layanan yang menyebabkannya.
- **Akuntabilitas berada pada pemilik.** Insinyur yang menyediakan sumber daya harus melihat dan memiliki dampak biaya dan karbonnya.
- **Efisiensi melayani biaya dan karbon bersama.** Mengerjakan pekerjaan sama dengan sumber daya lebih sedikit biasanya menghemat uang dan emisi sekaligus.
- **Sesuaikan ukuran secara berkelanjutan.** Permintaan berubah, jadi penyediaan harus ditinjau ulang, bukan ditetapkan sekali lalu dilupakan.
- **Karbon punya waktu dan tempat.** Komputasi yang sama memancarkan lebih banyak atau lebih sedikit tergantung kapan dan di mana listrik dihasilkan.
- **Seimbangkan segitiga.** Biaya, kinerja, dan keandalan saling menukar; optimalkan dengan sengaja, bukan secara buta.
- **Rancang untuk efisiensi sejak awal.** Pilihan arsitektur mendominasi biaya dan karbon jangka panjang jauh lebih daripada penyetelan tahap akhir.

## Rekomendasi

### Tetapkan visibilitas, optimasi, dan akuntabilitas FinOps

FinOps berjalan dalam tiga fase iteratif. **Informasikan**: bangun visibilitas lewat penandaan, alokasi, dan dasbor, agar setiap biaya diatribusikan ke tim, layanan, dan tujuan bisnis, dan biaya bersama dibagi adil. **Optimalkan**: hilangkan pemborosan (sumber daya menganggur dan yatim), sesuaikan ukuran layanan berlebih-sediaan, adopsi diskon berbasis komitmen seperti reservasi atau savings plan untuk beban dasar tetap, dan pakai kapasitas spot atau preemptible untuk pekerjaan yang dapat diinterupsi. **Operasikan**: tanamkan biaya ke praktik rekayasa normal dengan anggaran, peringatan anomali, perkiraan, dan tinjauan rutin. Di atas segalanya, taruh data biaya di depan insinyur yang menciptakannya. Jadikan efisiensi tujuan bersama rekayasa, keuangan, dan produk, bukan perhatian keuangan saja.

### Bangun perangkat lunak sadar-karbon dan hemat energi

Mengurangi karbon punya tiga tuas. **Efisiensi energi**: tulis dan konfigurasikan perangkat lunak agar mengerjakan pekerjaan sama dengan siklus CPU, memori, dan perpindahan data lebih sedikit, lewat algoritma lebih baik, caching, dan menghindari komputasi tak perlu. **Efisiensi perangkat keras**: pakai sumber daya sepenuhnya lewat pemanfaatan lebih tinggi, konsolidasi, dan perangkat keras modern yang efisien, karena kapasitas menganggur tetap menyerap daya dan mengandung karbon manufaktur. **Kesadaran karbon**: geser beban kerja fleksibel dalam waktu dan ruang ke kapan dan di mana jaringan lebih bersih, misalnya menjalankan pekerjaan batch ketika pembangkitan terbarukan tinggi, atau di wilayah dengan listrik rendah karbon. Ukur memakai pendekatan yang diakui seperti spesifikasi Software Carbon Intensity. Pilih penyedia dan wilayah dengan komitmen terbarukan kuat dan pelaporan transparan.

### Rancang arsitektur berkelanjutan dan sesuaikan ukuran

Arsitektur menentukan lantai untuk biaya dan karbon. Pilih desain elastis yang berskala ke permintaan aktual dan berskala ke nol saat menganggur, agar Anda tak pernah membayar untuk menjaga kapasitas tak terpakai tetap berjalan. [Serverless](https://en.wikipedia.org/wiki/Serverless_computing) dan [autoscaling](https://en.wikipedia.org/wiki/Autoscaling) mengurangi pemborosan untuk beban kerja berlonjak, dan layanan terkelola dapat memperbaiki pemanfaatan lewat [multitenansi](https://en.wikipedia.org/wiki/Multitenancy). Sesuaikan ukuran komputasi, penyimpanan, dan basis data terhadap pemakaian nyata alih-alih penyediaan berlebih karena ketakutan. Tetapkan kebijakan siklus hidup data agar data dingin berpindah ke tingkatan lebih murah dan hemat energi atau dihapus. Mengurangi volume data dan transfer jaringan memangkas biaya penyimpanan dan energi memindahkan bit. Perlakukan efisiensi sebagai persyaratan desain, ditinjau di samping kinerja dan keandalan.

### Seimbangkan biaya, kinerja, dan keandalan dengan sengaja

Biaya, kinerja, dan keandalan membentuk segitiga. Dorong satu keras, dan Anda biasanya memajaki yang lain: redundansi lebih banyak dan latensi lebih rendah berbiaya lebih, dan sering mengonsumsi lebih banyak energi. Jadikan trade-off ini eksplisit dan kaitkan dengan nilai bisnis. Pakai SLO ([service level objective](https://en.wikipedia.org/wiki/Service-level_objective)) untuk mendefinisikan seberapa banyak keandalan dan kinerja yang sebenarnya dibutuhkan layanan, lalu sediakan sesuai target itu alih-alih menyepuh emas semuanya secara seragam. Beban kerja non-kritis dan internal dapat menerima konfigurasi lebih murah, kurang redundan, dan lebih fleksibel karbon. Sisihkan penyediaan premium untuk yang benar-benar layak.

### Atur tanpa mencekik

Sediakan guardrail, bukan gerbang. Tim platform pusat dapat menawarkan bawaan efisien, penegakan penandaan, peringatan anggaran, dan dasbor swalayan, sambil menyerahkan keputusan harian kepada tim yang memiliki beban kerja. Tetapkan target seluruh organisasi untuk efisiensi biaya dan pengurangan karbon, laporkan kemajuan secara transparan, dan rayakan penghematan. Hindari birokrasi persetujuan berat yang memperlambat pengiriman. Tujuannya menjadikan pilihan efisien sebagai bawaan yang mudah.

## Trade-off: kelebihan dan kekurangan

| Keputusan | Kelebihan | Kekurangan |
|---|---|---|
| Diskon komitmen | Penghematan besar pada beban dasar | Lock-in, risiko jika permintaan bergeser |
| Kapasitas spot/preemptible | Komputasi termurah, memakai cadangan jaringan | Interupsi, kompleksitas tambahan |
| Penyesuaian ukuran agresif | Biaya dan karbon lebih rendah | Risiko kurang sediaan saat lonjakan |
| Penjadwalan sadar-karbon | Emisi lebih rendah | Pekerjaan tertunda, upaya rekayasa |
| Redundansi multi-wilayah | Keandalan lebih tinggi | Biaya, energi, dan karbon lebih |

Trade-off pemersatunya adalah keandalan dan kinerja maksimum jarang bertepatan dengan biaya dan karbon minimum. Sistem redundan, selalu hidup, dan berlatensi rendah mahal dan haus energi, sehingga penyepuhan emas seragam memboroskan uang dan emisi pada beban kerja yang tak membutuhkannya. Disiplinnya adalah menyesuaikan ambisi dengan nilai bisnis memakai SLO, membelanjakan sumber daya premium hanya di mana penting. Diskon komitmen dan kapasitas spot menawarkan penghematan nyata, tetapi memperkenalkan lock-in dan risiko interupsi yang harus Anda kelola. Penjadwalan sadar-karbon menghemat emisi, tetapi hanya cocok untuk beban kerja yang toleran terhadap penundaan atau relokasi.

## Pertanyaan untuk didiskusikan dengan tim Anda

1. **Berapa pangsa pengeluaran cloud Anda yang benar-benar ditandai dan diatribusikan ke tim hari ini?** Fase inform FinOps adalah fondasi: Anda tak dapat mengoptimalkan apa yang tak dapat Anda lihat, dan pengeluaran tak bertanda dan tak teralokasi berarti tak ada yang memiliki pemborosan. Bawa angka cakupan nyata ke diskusi, bukan aspirasi, dan daftar butir baris tak bertanda terbesar. Bagi organisasi besar di mana ratusan tim masing-masing menyediakan secara independen, tingkat atribusi rendah berarti ketidakefisienan bersama bertambah tak terlihat menjadi jutaan. Dalam pengaturan pemerintah dan enterprise, atribusi juga cara Anda membela pengeluaran pembayar pajak atau pemegang saham dan cara Anda mengalokasikan biaya porsi-adil platform bersama. Jawabannya menetapkan langkah pertama Anda: jika cakupan rendah, penegakan penandaan dan alokasi datang sebelum penyesuaian ukuran apa pun, karena optimasi tanpa visibilitas adalah menebak.

2. **Berapa banyak beban dasar Anda yang tercakup diskon komitmen, dan apa yang terjadi pada komitmen itu jika permintaan bergeser?** Reservasi dan savings plan memberi penghematan besar pada beban dasar tetap, tetapi memperkenalkan lock-in, sehingga membeli terlalu agresif mengubah diskon menjadi liabilitas ketika produk dihentikan atau bermigrasi. Bawa angkanya: persentase cakupan komitmen Anda, tren beban dasar Anda, dan beban kerja yang paling mungkin berubah bentuk dalam setahun ke depan. Disiplinnya adalah berkomitmen hanya pada lantai yang Anda yakin bertahan, menutup lapisan variabel dengan on-demand atau spot, dan meninjau ulang seiring permintaan berevolusi. Bagi enterprise besar ini keputusan gaya perbendaharaan dengan paparan finansial nyata, sehingga keuangan dan rekayasa harus memilikinya bersama alih-alih salah satu pihak saja. Jawabannya harus memisahkan beban dasar tahan lama dari permintaan tak pasti dan menakar komitmen sesuai yang pertama.

3. **Berapa banyak armada Anda yang menganggur, dan apakah Anda menghitung karbon manufaktur tertanam atau hanya energi yang dibakarnya saat berjalan?** Kapasitas menganggur tetap menyerap daya dan membawa karbon manufaktur yang sudah dikeluarkan untuk membangun perangkat keras, sehingga berfokus hanya pada energi berjalan sambil menyediakan berlebih melewatkan bagian nyata dari jejak. Bawa data pemanfaatan: rata-rata dan puncak, celah antara yang disediakan dan dipakai, dan di mana skala-ke-nol atau konsolidasi mungkin. Pemanfaatan lebih tinggi melayani biaya dan karbon sekaligus, yang merupakan benang merah bab ini, jadi pemborosan menganggur adalah kemenangan terbersih yang Anda punya. Untuk organisasi di bawah mandat net-zero, ukuran karbon jujur yang mencakup emisi tertanam adalah yang memisahkan kemajuan nyata dari greenwashing yang mengundang reaksi regulasi dan reputasi. Jawabannya harus menyasar beban kerja berpemanfaatan terendah Anda untuk konsolidasi, autoscaling, atau skala-ke-nol, dan menetapkan pendekatan pengukuran yang tidak diam-diam mengabaikan karbon manufaktur.

4. **Apakah insinyur Anda melihat biaya dan karbon layanan mereka sendiri, dan adakah yang bertindak atas apa yang mereka lihat?** Visibilitas hanya terbayar ketika mencapai orang yang menyediakan sumber daya dan mengubah perilaku mereka, jadi dasbor yang ditinjau keuangan bulanan tetapi tak pernah dibuka insinyur adalah hiasan, bukan akuntabilitas. Tarikan yang bersaing nyata: tim platform menginginkan kendali pusat dan pelaporan bersih, sementara tim pengiriman membenci apa pun yang terasa seperti pengawasan atau gerbang lain pada pengiriman. Bawa bukti siapa yang benar-benar melihat data biaya dan karbon, seberapa sering, dan apakah ada penyesuaian ukuran atau pembersihan yang mengikuti dalam kuartal terakhir. Bagi organisasi besar di mana ratusan tim menyediakan secara independen, beda antara sinyal yang dimiliki insinyur dan laporan yang diabaikan adalah beda antara penghematan yang bertambah dan pemborosan yang bertambah. Dalam pengaturan enterprise dan pemerintah, taruh ekonomi satuan (biaya dan karbon per permintaan, per pelanggan, atau per kasus) di depan tim pemilik, karena angka agregat membela anggaran tetapi angka per satuan mengubah keputusan desain.

5. **Beban kerja Anda yang mana benar-benar fleksibel dalam waktu atau wilayah, dan apa yang dibutuhkan untuk menjadwalkannya di mana jaringan lebih bersih?** Penjadwalan sadar-karbon menggeser pekerjaan fleksibel ke kapan dan di mana listrik rendah karbon, tetapi hanya cocok untuk pekerjaan yang toleran terhadap penundaan atau relokasi, jadi tugas pertama adalah memisahkan pekerjaan batch yang benar-benar dapat ditunda dari apa pun yang menghadap pengguna atau terikat latensi. Trade-off-nya adalah memindahkan pekerjaan lintas wilayah atau jendela di luar jam sibuk menambah upaya rekayasa, biaya transfer data, dan kadang risiko residensi data yang dapat melampaui emisi yang dihemat. Bawa daftar kandidat pekerjaan batch dan analitik, toleransi latensinya, kendala residensi datanya, dan intensitas karbon wilayah tempat Anda dapat menjalankannya secara legal. Bagi enterprise ini optimasi sederhana di atas penyesuaian ukuran, jadi urutkan setelah dasar-dasar biaya alih-alih sebelumnya. Di pemerintah, aturan residensi data dan kedaulatan dapat melarang memindahkan data warga lintas batas terlepas dari kebersihan jaringan, sehingga pilihan wilayah adalah pertanyaan hukum sebelum pertanyaan karbon.

6. **Target efisiensi dan keberlanjutan apa yang telah Anda tetapkan, dan apakah ditulis sehingga mencapainya tak dapat diam-diam merusak keandalan?** Target memfokuskan upaya, tetapi tujuan biaya atau karbon yang kasar mengundang perilaku salah: tim menyediakan kurang, melucuti redundansi, atau menunda pekerjaan dengan cara yang menukar penghematan kecil dengan insiden besar. Ketegangannya antara angka ambisius dari atas yang dapat dilaporkan pimpinan dan target dari bawah yang berlandaskan SLO aktual setiap layanan, sehingga keduanya harus direkonsiliasi alih-alih dipaksakan. Bawa target Anda saat ini, garis dasar yang menjadi ukurannya, dan guardrail keandalan yang menghentikan optimasi memotong apa yang benar-benar dibutuhkan layanan. Bagi organisasi besar, target agregat harus terurai adil ke tim yang beban kerjanya berbeda, sehingga layanan pembayaran menghadap pelanggan dan pekerjaan pelaporan internal tidak boleh memikul ekspektasi efisiensi yang sama. Dalam konteks enterprise dan pemerintah di mana angka keberlanjutan muncul dalam pengungkapan publik, kaitkan setiap angka terlapor dengan metode pengukuran yang dapat diaudit, karena target yang tak dapat Anda pertahankan di bawah pengawasan adalah liabilitas, bukan pencapaian.

## Lensa sektor

**Startup.** Biaya adalah runway, jadi satu sore penandaan dan satu peringatan anggaran dapat membeli satu bulan lagi sebelum Anda menggalang dana lagi. Lewati proses FinOps dan akuntansi karbon sepenuhnya; cukup awasi tagihan, bunuh sumber daya menganggur, dan pilih platform terkelola yang berskala ke nol agar Anda membayar untuk beban alih-alih kapasitas yang siap menunggu. Sumber daya Anda yang paling langka adalah perhatian rekayasa, jadi otomatiskan pemborosan yang jelas dan lanjutkan.

**Bisnis kecil.** Anda tidak punya spesialis FinOps dan anggaran ketat, jadi bersandarlah pada perkakas biaya yang sudah diberikan penyedia cloud Anda alih-alih membeli platform khusus. Tetapkan peringatan anggaran bulanan, aktifkan rekomendasi penyesuaian ukuran penyedia, dan pilih layanan terkelola dan serverless yang melipat efisiensi operasional ke dalam harga. Perlakukan keberlanjutan sebagai memilih wilayah rendah karbon dan bawaan efisien, bukan program pelaporan yang harus Anda isi stafnya.

**Enterprise.** Masalahnya tata kelola lintas banyak tim: penandaan konsisten, alokasi adil biaya platform bersama, strategi diskon komitmen yang dimiliki bersama keuangan dan rekayasa, dan biaya serta karbon dimunculkan sebagai sinyal yang dilihat setiap tim. Bakukan bawaan efisien dan metode pengukuran agar ratusan keputusan penyediaan independen tidak bertambah menjadi pemborosan, dan kelola pengeluaran cloud serta emisi sebagai portofolio dengan target, peringatan anomali, dan pelaporan transparan alih-alih sebaran optimasi lokal.

**Pemerintah.** Aturan pengadaan, transparansi, dan akuntabilitas publik membentuk setiap pilihan. Anda membelanjakan uang pembayar pajak dan sering terikat mandat net-zero, jadi Anda harus menunjukkan kehati-hatian fiskal dan kemajuan emisi teraudit, yang berarti ukuran karbon jujur yang mencakup perangkat keras tertanam alih-alih greenwashing. Aturan residensi data dan kedaulatan dapat membatasi wilayah mana yang dapat Anda pakai terlepas dari kebersihan jaringan, dan metrik efisiensi serta emisi mungkin perlu diterbitkan untuk pengawasan publik, jadi pilih metode pengukuran yang dapat Anda pertahankan di bawah audit.

## Contoh

**Startup.** Startup tahap benih menyaksikan tagihan cloud-nya berlipat dua dalam dua bulan dan tak dapat mengatakan mengapa. Seorang pendiri menghabiskan satu sore menandai setiap sumber daya menurut fitur dan mengaktifkan peringatan anggaran sederhana. Tag mengungkap klaster staging yang terlupakan dan basis data berlebih ukuran yang berjalan sepanjang waktu untuk pekerjaan malam. Mematikan klaster dan memindahkan pekerjaan ke jadwal di luar jam sibuk pada instans lebih kecil memangkas tagihan sepertiga, yang membeli tim satu bulan runway lagi.

**Enterprise.** Sebuah pengecer multinasional dengan properti cloud besar dan menyebar mendirikan praktik FinOps. Ia menegakkan penandaan, mengalokasikan setiap biaya ke tim produk, dan memunculkan pengeluaran di dasbor yang dilihat insinyur setiap hari. Dalam setahun ia menghapus sumber daya menganggur, menyesuaikan ukuran layanan berlebih-sediaan, dan membeli savings plan untuk beban dasar tetap, memangkas pengeluaran cloud kira-kira seperempat. Ia kemudian menjadwalkan pekerjaan batch analitik malam untuk berjalan di wilayah lebih rendah karbon dan jam di luar puncak, mengurangi biaya dan emisi, dan melaporkan penghematan karbon dalam pengungkapan keberlanjutan tahunannya.

**Pemerintah.** Sebuah lembaga pemerintah yang mengoperasikan layanan warga di bawah mandat net-zero nasional harus menunjukkan kehati-hatian fiskal dengan uang pembayar pajak dan kemajuan menuju target emisi. Ia menyesuaikan ukuran dan mengonsolidasikan beban kerja, menetapkan kebijakan retensi data yang memindahkan catatan jarang diakses ke penyimpanan dingin hemat energi, dan memilih wilayah cloud bertenaga pangsa tinggi listrik terbarukan. Ia mengukur intensitas karbon layanan utamanya dan menerbitkan metrik efisiensi dan emisi untuk akuntabilitas publik. Bawaan efisien dan dasbor swalayan memungkinkan puluhan tim pengiriman membuat pilihan berkelanjutan tanpa hambatan pusat.

## Kasus bisnis: motivasi, ROI, dan TCO

Imbal hasilnya luar biasa langsung. Optimasi FinOps umumnya mengurangi pengeluaran cloud seperlima hingga sepertiga dengan upaya disiplin, penghematan yang mengalir langsung ke laba bersih, atau ke pendanaan kerja baru. Pengurangan karbon makin membawa nilai finansial juga, lewat penetapan harga karbon yang dihindari, kelayakan untuk kontrak dengan persyaratan keberlanjutan, dan risiko regulasi serta reputasi yang berkurang. Karena efisiensi menurunkan biaya dan karbon sekaligus, satu investasi pada visibilitas dan penyesuaian ukuran terbayar pada kedua dimensi.

Total biaya kepemilikan harus menghitung biaya adopsi: perkakas untuk visibilitas biaya dan karbon, staf FinOps atau platform untuk menjalankan praktik, dan waktu rekayasa untuk menyesuaikan ukuran dan merancang ulang. Ini sederhana dibanding penghematan, dan menyusut seiring bawaan efisien tertanam. Biaya tidak mengadopsi bertambah diam-diam: tagihan cloud liar yang tumbuh lebih cepat daripada bisnis, pemborosan yang tak pernah muncul karena tak ada yang memilikinya, dan paparan regulasi, investor, dan reputasi yang menumpuk atas keberlanjutan. Untuk mengajukan kasus kepada pimpinan, sajikan pengeluaran saat ini dan lintasan pertumbuhannya, perkiraan pemborosan, dan penghematan tolok ukur dari adopsi FinOps. Lalu pasangkan dengan pengurangan emisi dan nilai kepatuhan. Bingkai biaya dan keberlanjutan sebagai inisiatif efisiensi yang sama dilihat melalui dua lensa, agar bisnis tak perlu memilih antara menghemat uang dan memangkas karbon.

## Anti-pola dan jebakan

- **Tanpa atribusi biaya.** Pengeluaran tak bertanda dan tak teralokasi berarti tak ada yang memiliki pemborosan dan tak ada yang dapat mengoptimalkannya.
- **Penyediaan set-and-forget.** Menakar sumber daya sekali dan tak pernah meninjau ulang menjamin penyimpangan ke penyediaan berlebih.
- **FinOps hanya keuangan.** Memperlakukan biaya sebagai perhatian belakang kantor alih-alih sinyal rekayasa gagal, karena insinyur yang membuat keputusan yang mendorong pengeluaran.
- **[Greenwashing](https://en.wikipedia.org/wiki/Greenwashing).** Mengklaim keberlanjutan tanpa pengukuran mengundang reaksi regulasi dan reputasi.
- **Efisiensi dengan mengorbankan keandalan.** Memotong begitu agresif sehingga layanan gagal di bawah beban menukar penghematan kecil dengan insiden besar.
- **Mengabaikan karbon tertanam.** Berfokus hanya pada energi berjalan sambil menyediakan berlebih perangkat keras menganggur melewatkan jejak manufaktur.
- **Gerbang birokratis.** Proses persetujuan berat untuk pengeluaran memperlambat pengiriman dan mendorong tim mengakali tata kelola.

## Model kematangan

**Tingkat 1, Memulai.** Biaya cloud adalah kejutan pada tagihan bulanan. Tak ada penandaan, alokasi, atau kesadaran karbon, dan penyediaan longgar serta jarang ditinjau ulang. Pemborosan tak terlihat karena tak ada yang memilikinya, dan pembersihan apa pun yang terjadi adalah reaksi terhadap kejutan tagihan alih-alih praktik.

**Tingkat 2, Mengembangkan.** Visibilitas biaya dasar dan penandaan ada, dan sebagian penyesuaian ukuran dan pembersihan sumber daya menganggur terjadi, tetapi cakupan dan ketelitian sangat bervariasi antartim. Beberapa kelompok mengawasi pengeluaran dan mencoba wilayah rendah karbon; yang lain tidak. Keberlanjutan diakui tetapi tak diukur, dan kebiasaan baik bergantung pada inisiatif individu alih-alih ekspektasi bersama.

**Tingkat 3, Membakukan.** Praktik FinOps didokumentasikan dan diterapkan di seluruh organisasi: penandaan ditegakkan, biaya bersama dialokasikan dengan metode yang disepakati, dan anggaran, perkiraan, serta peringatan anomali adalah standar. Diskon komitmen dan penyesuaian ukuran mengikuti playbook terdefinisi, dan karbon diukur untuk layanan utama memakai metode yang diakui seperti spesifikasi Software Carbon Intensity, dengan pilihan wilayah dan penjadwalan dipertimbangkan konsisten alih-alih kasus per kasus.

**Tingkat 4, Mengelola.** Biaya dan karbon diukur dan dikendalikan terhadap garis dasar. Tim melacak ekonomi satuan (biaya dan karbon per permintaan, per pelanggan, atau per kasus), pemanfaatan termasuk estimasi menganggur dan karbon tertanam, cakupan komitmen terhadap beban dasar, dan akurasi perkiraan, semuanya dilaporkan terhadap target organisasi. Anomali memicu investigasi, efisiensi dan kepatuhan SLO ditinjau bersama agar optimasi tidak diam-diam mengikis keandalan, dan keputusan go atau no-go atas penyediaan dibuat dari data ini alih-alih intuisi.

**Tingkat 5, Mengorkestrasi.** Biaya dan karbon adalah sinyal rekayasa berkelanjutan yang dimiliki dan dijalin ke praktik harian. Bawaan efisien, penyesuaian ukuran otomatis, dan penjadwalan sadar-karbon adalah norma, dan organisasi terus menyeimbangkan ulang propertinya seiring permintaan, harga, dan intensitas jaringan bergeser. Biaya, kinerja, dan keandalan ditukar dengan sengaja lewat SLO, metrik keberlanjutan memberi makan pelaporan publik dan investor dengan metode yang dapat diaudit, dan praktik beradaptasi seiring bisnis, pasar, dan regulasi berevolusi.

## Gagasan untuk didiskusikan

- Siapa yang harus memiliki biaya cloud di organisasi Anda: keuangan, tim FinOps pusat, atau tim rekayasa yang menyediakan sumber daya?
- Bagaimana Anda mengatribusikan biaya platform bersama secara adil ke banyak tim konsumen?
- Di mana keseimbangan yang tepat antara penghematan biaya dan keandalan atau kinerja yang mungkin Anda korbankan untuk mendapatkannya?
- Bagaimana Anda akan mengukur jejak karbon layanan Anda, dan seberapa Anda memercayai data yang tersedia?
- Beban kerja Anda yang mana cukup fleksibel untuk penjadwalan sadar-karbon dalam waktu atau wilayah?
- Bagaimana Anda menetapkan target efisiensi dan keberlanjutan yang memotivasi tim tanpa mendorong penyediaan kurang yang berisiko?

## Poin-poin utama

- Cloud menjadikan biaya dan karbon perhatian rekayasa; visibilitas dan kepemilikan adalah fondasi mengendalikan keduanya.
- FinOps bekerja dalam tiga fase: informasikan (visibilitas), optimalkan (sesuaikan ukuran dan diskon), dan operasikan (tanamkan dalam praktik).
- Perangkat lunak efisien biasanya menghemat uang dan karbon bersama, jadi perlakukan sebagai satu inisiatif dengan dua lensa.
- Kurangi karbon lewat efisiensi energi, pemanfaatan perangkat keras lebih tinggi, dan penjadwalan sadar-karbon dalam waktu dan tempat.
- Arsitektur dan penyesuaian ukuran mendominasi biaya dan karbon jangka panjang; rancang untuk elastisitas dan skala-ke-nol.
- Seimbangkan biaya, kinerja, dan keandalan dengan sengaja memakai SLO, dan atur dengan guardrail alih-alih gerbang.

## Referensi dan bacaan lanjutan

- J.R. Storment, Mike Fuller, *Cloud FinOps: Collaborative, Real-Time Cloud Financial Management*
- FinOps Foundation, dokumentasi *FinOps Framework*
- Green Software Foundation, *Principles of Green Software Engineering* dan *Software Carbon Intensity (SCI) Specification*
- Anne Currie, Sarah Hsu, Sara Bergman, *Building Green Software*
- Adrian Cockcroft, tulisan tentang efisiensi dan keberlanjutan cloud
- The Shift Project, *Lean ICT: Towards Digital Sobriety*
