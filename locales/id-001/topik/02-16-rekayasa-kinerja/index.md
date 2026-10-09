# 2.16 Rekayasa kinerja

## Tinjauan dan motivasi

Rekayasa kinerja adalah keterampilan membuat kode cukup cepat, dengan sengaja, memakai pengukuran alih-alih naluri. Bab ini bekerja pada tingkat kode dan komponen: fungsi, loop, struktur data, kueri, alokasi, dan cara satu layanan menghabiskan waktunya. Ia pendamping bab 3.5, yang menangani kinerja pada tingkat sistem (menskalakan keluar, penyeimbangan beban, kapasitas, dan ketahanan). Ketika sistem lambat, bab 3.5 bertanya berapa banyak mesin yang Anda butuhkan; bab ini bertanya mengapa satu mesin mengerjakan begitu banyak sejak awal. Anda biasanya membutuhkan keduanya, dan pandangan tingkat kode adalah tempat sebagian besar biaya dan latensi yang mengejutkan sebenarnya bersembunyi.

Bagi tim besar, disiplin ini penting karena kinerja membusuk secara diam-diam. Tak satu commit pun membuat layanan lambat, tetapi seribu commit kecil, masing-masing menambah panggilan basis data atau loop tak terbatas, akan membuatnya lambat. Tanpa metode bersama untuk mengukur, menganggarkan, dan menggerbangi kinerja, Anda menemukan pembusukan hanya ketika pelanggan mengeluh atau peluncuran meleleh. Metode mengubah kinerja dari pemadaman kebakaran heroik menjadi sifat rutin yang Anda lindungi.

Bagi enterprise, kinerja adalah uang: kode yang lebih cepat berarti lebih sedikit mesin, tagihan cloud lebih rendah, dan kemampuan memenuhi [perjanjian tingkat layanan](https://en.wikipedia.org/wiki/Service-level_agreement) (SLA) atas latensi tanpa penyediaan berlebihan. Bagi pemerintah, kinerja adalah akses: halaman yang dimuat di ponsel lama melalui koneksi seluler lemah adalah beda antara warga yang menyelesaikan klaim tunjangan dan yang menyerah. Sistem publik juga membutuhkan bukti tolok ukur yang dapat direproduksi, karena pengadaan dan badan pengawas akan meminta Anda membuktikan angkanya, bukan sekadar menegaskannya.

## Prinsip utama

- **Ukur sebelum mengoptimalkan.** Hambatan hampir tidak pernah di tempat Anda menebak. Profil, lalu bertindak.
- **Hindari optimasi prematur.** Peringatan Donald Knuth berlaku: mengoptimalkan kode yang tidak penting memakan kejelasan dan tidak membeli apa-apa.
- **Definisikan "cukup cepat" sebagai angka.** Anggaran kinerja dengan target dan persentil mengubah opini menjadi lulus atau gagal.
- **Rata-rata berbohong; persentil berkata jujur.** Ekor (p99) yang dirasakan pengguna, bukan rata-rata.
- **Kemenangan algoritmik mengalahkan penyetelan mikro.** Kelas kompleksitas yang lebih baik mengungguli kecerdikan faktor konstanta sebanyak apa pun.
- **Latensi dan throughput adalah tujuan yang berbeda.** Memperbaiki satu dapat memperburuk yang lain; ketahui mana yang Anda beli.
- **Lakukan tolok ukur dengan jujur atau jangan sama sekali.** Pemanasan, varians, dan beban kerja representatif memisahkan angka nyata dari fiksi.
- **Gerbangi kinerja di CI, awasi di produksi.** Regresi yang tertangkap sebelum penggabungan murah; yang tertangkap pengguna, mahal.

## Rekomendasi

### Ukur lebih dulu, dan profil sebelum menyentuh satu baris

Aturan tertua di bidang ini adalah yang paling diabaikan: temukan hambatan sebelum mengoptimalkan. Raih [profiler](https://en.wikipedia.org/wiki/Profiling_(computer_programming)), perkakas yang mengambil sampel atau menginstrumentasi program yang berjalan untuk menunjukkan di mana ia menghabiskan waktu dan memori. Profil CPU (fungsi mana yang membakar siklus), memori dan alokasi (apa yang dialokasikan dan seberapa sering, karena gejolak alokasi mendorong jeda garbage collection), dan I/O (waktu yang dihabiskan menunggu disk, jaringan, atau basis data). [Flame graph](https://en.wikipedia.org/wiki/Flame_graph), visualisasi bertumpuk di mana setiap kotak adalah fungsi dan lebarnya adalah waktu yang dihabiskan, membuat biaya dominan jelas sekilas: cari kotak terlebar, bukan tumpukan terdalam. Optimalkan biaya terbesar lebih dulu, ukur ulang, dan berhenti ketika Anda mencapai anggaran. Ini terhubung dengan praktik observabilitas bab 9.2, karena profil produksi mengalahkan tebakan apa pun dari laptop.

Jaga juga dari kekeliruan sebaliknya. Kalimat lengkap Knuth adalah bahwa optimasi prematur adalah akar banyak kejahatan, dan ia memaksudkannya tentang inefisiensi kecil yang menggoda Anda mengorbankan kode terbaca demi kecepatan yang dibayangkan. Tulis versi yang jelas lebih dulu, ukur, dan optimalkan hanya kode yang didakwa profiler.

### Definisikan arti "cukup cepat" dengan anggaran kinerja

Kecepatan bukan kebajikan secara abstrak; ia target yang Anda penuhi atau luput. Tetapkan **anggaran kinerja**: batas konkret seperti "latensi checkout p99 di bawah 300 ms" atau "endpoint ini mengalokasikan kurang dari 1 MB per permintaan." Kaitkan dengan sesuatu yang dirasakan pengguna atau bisnis, dan ekspresikan sebagai **persentil**, bukan rata-rata, karena rata-rata menyembunyikan ekor lambat tempat pengguna nyata hidup. Jika 1% permintaan memakan 5 detik, rata-rata Anda mungkin tampak baik sementara sebagian bermakna pelanggan menderita. Anggaran memberi tim definisi selesai yang dibagikan dan tak terbantahkan serta garis yang jelas dilintasi regresi.

### Raih efisiensi algoritmik sebelum optimasi mikro

Kemenangan terbesar dan termurah datang dari [efisiensi algoritmik](https://en.wikipedia.org/wiki/Algorithmic_efficiency), bagaimana pekerjaan tumbuh seiring masukan tumbuh, dijelaskan dengan [notasi Big O](https://en.wikipedia.org/wiki/Big_O_notation) (cara mengklasifikasikan laju pertumbuhan, sehingga pengurutan O(n log n) berskala jauh lebih baik daripada O(n kuadrat)). Loop bersarang yang tak terlihat pada sepuluh butir menjadi bencana pada sepuluh ribu. Sebelum Anda menyetel fungsi panas dengan tangan, tanyakan apakah ia pada dasarnya mengerjakan terlalu banyak: kueri N+1 yang tidak disengaja, pemindaian linier yang seharusnya pencarian hash, atau pekerjaan berulang yang dapat dimemoisasi. Ini terkait dengan fondasi algoritmik di bab 2.13. Penyetelan faktor konstanta sebanyak apa pun tidak menyelamatkan kelas kompleksitas yang salah.

### Bedakan latensi dari throughput, dan hormati ekor

**Latensi** adalah berapa lama satu operasi berlangsung; **throughput** adalah berapa banyak operasi selesai per satuan waktu. Keduanya bukan tujuan yang sama, dan mengoptimalkan satu dapat merugikan yang lain. Batching meningkatkan throughput tetapi menambah latensi pada butir pertama dalam batch; menambah pekerja paralel menaikkan throughput tetapi dapat memperburuk latensi ekor lewat perebutan. Putuskan mana yang benar-benar dibutuhkan pengguna Anda. Dan selalu awasi ekor: latensi p95 dan p99, 5% dan 1% permintaan terlambat, karena pada skala besar pengguna membuat banyak permintaan dan sering mengenai ekor. Laporkan persentil, beri peringatan atasnya, dan anggarkan untuknya.

### Ketahui batas paralelisme

Ketika Anda memparalelkan, ingat [hukum Amdahl](https://en.wikipedia.org/wiki/Amdahl%27s_law): percepatan dari menambah prosesor dibatasi oleh bagian pekerjaan yang harus berjalan serial. Jika 10% pekerjaan pada dasarnya berurutan, tak ada jumlah inti yang membawa Anda melewati percepatan 10x. Konkurensi (menstrukturkan pekerjaan agar tugas dapat maju secara independen) dan paralelisme (benar-benar mengeksekusinya pada saat yang sama) menambah kompleksitas nyata, dari race condition hingga beban koordinasi. Ukur bagian serial sebelum Anda mengira lebih banyak thread akan menyelamatkan Anda, dan jujurlah bahwa versi benar paling sederhana sering cukup cepat.

### Gunakan caching dan lokalitas data, dan hormati biayanya

[Cache](https://en.wikipedia.org/wiki/Cache_(computing)), penyimpanan cepat untuk hasil yang baru atau mahal dihitung, adalah perkakas kinerja paling ampuh yang Anda miliki dan yang paling berbahaya. Kelakar Phil Karlton bahwa dua hal sulit dalam ilmu komputer adalah invalidasi cache dan penamaan adalah peringatan: cache basi menyajikan jawaban keliru, dan logika invalidasi adalah tempat bug halus berkembang biak. Cache dengan sengaja, tetapkan kedaluwarsa, dan ketahui cerita kebenaran Anda sebelum mengoptimalkan tingkat hit. Pada tingkat terendah, [lokalitas referensi](https://en.wikipedia.org/wiki/Locality_of_reference), menjaga data yang dipakai bersama tetap dekat di memori, memanfaatkan hierarki cache CPU dan dapat membuat kode beberapa kali lebih cepat tanpa perubahan algoritmik, dengan mengubah cache miss menjadi hit. Array bersebelahan mengalahkan struktur pengejar-pointer karena alasan ini. Ini bersinggungan dengan pilihan tata letak data di bab 3.4.

### Lakukan tolok ukur dengan jujur dan curigai mikrotolok ukur

Tolok ukur yang berbohong lebih buruk daripada tidak ada, karena memberi keyakinan palsu. Panaskan sebelum mengukur, agar Anda mengukur perilaku keadaan tunak, bukan startup sekali jalan dan kompilasi just-in-time. Jalankan banyak iterasi dan laporkan varians, bukan satu angka beruntung. Gunakan beban kerja representatif dengan ukuran dan distribusi data yang realistis, karena mikrotolok ukur pada masukan mainan sering mengukur kemampuan kompiler menghapus tes Anda alih-alih kecepatan nyata kode. Waspadai jebakan klasik: nilai yang dibuktikan optimizer tidak terpakai dan dihapus, loop yang diangkat runtime, atau cache yang hangat dalam tolok ukur dan dingin di produksi. Bila ragu, ukur seluruh jalur, bukan fungsi yang terisolasi.

### Gerbangi kinerja di CI dan amati di produksi

Jadikan kinerja sifat yang dilindungi pipeline. Tambahkan tes kinerja ke strategi bab 2.4, dengan gerbang regresi yang menggagalkan build ketika tolok ukur atau anggaran kunci memburuk melewati ambang. Ini menangkap rayapan lambat sebelum digabung. Lalu tutup lingkaran di produksi dengan telemetri bab 9.2: lacak persentil latensi nyata, laju alokasi, dan kueri lambat terhadap anggaran Anda, karena lalu lintas produksi menemukan kasus yang tidak pernah dibayangkan tolok ukur Anda.

## Trade-off: kelebihan dan kekurangan

| Pendekatan | Kelebihan | Kekurangan |
|---|---|---|
| Optimalkan sekarang, berdasarkan intuisi | Terasa produktif; sesekali kemenangan beruntung | Biasanya menyetel kode yang salah; menambah kompleksitas tanpa keuntungan |
| Ukur dulu, lalu optimalkan | Menargetkan hambatan nyata; berbasis bukti | Butuh perkakas dan disiplin; lebih lambat memulai |
| Caching | Keuntungan latensi dan throughput besar | Bug invalidasi; data basi; biaya memori |
| Lebih banyak paralelisme | Throughput lebih tinggi pada pekerjaan paralel | Batas Amdahl; perebutan; bug konkurensi |
| Optimasi mikro | Memeras faktor konstanta | Langit-langit kecil; merugikan keterbacaan; sering derau |
| Perbaikan algoritmik | Kemenangan berskala dengan ukuran masukan | Perlu analisis; kadang penulisan ulang lebih besar |
| Gerbang kinerja CI | Menghentikan regresi lebih awal dan murah | Tolok ukur goyah mengikis kepercayaan; perlu lingkungan stabil |

Ketegangan pusatnya adalah upaya versus imbalan, dan penyelesaiannya adalah pengukuran. Pekerjaan kinerja punya imbal hasil yang menurun tajam: perbaikan pertama berpemandu profil mungkin membelah dua latensi, yang kesepuluh mungkin memangkas satu persen sambil menggandakan kompleksitas kode. Anda menyelesaikannya dengan menolak mengoptimalkan tanpa angka di tangan dan anggaran untuk dicapai. Ukur untuk menemukan perbaikan yang layak dibuat, dan berhenti begitu Anda melewati anggaran alih-alih mengejar kecepatan demi kecepatan.

## Pertanyaan untuk didiskusikan dengan tim Anda

1. **Apakah Anda punya anggaran kinerja tertulis untuk jalur kritis Anda, dan apakah diekspresikan sebagai persentil?** Banyak tim punya perasaan samar bahwa segalanya harus "cepat" tetapi tidak ada angka yang bisa digagalkan siapa pun, artinya kinerja bukan tugas siapa pun sampai rusak. Anggaran seperti "p99 di bawah 300 ms" membuat target konkret, memberi peninjau sesuatu untuk ditegakkan, dan mengubah regresi menjadi peristiwa yang terlihat alih-alih kemerosotan perlahan. Ini paling penting pada tim besar, di mana latensi merayap lewat banyak tangan dan tak ada penulis tunggal yang melihat biaya kumulatif. Bawa data latensi Anda saat ini dan tanyakan apakah Anda melaporkan rata-rata, yang menyanjung Anda, atau persentil, yang berkata jujur. Jika Anda tidak dapat mengatakan arti "cukup cepat" sebagai angka, itu hal pertama yang diperbaiki.

2. **Ketika terakhir Anda mengoptimalkan sesuatu, apakah profiler yang memberi tahu di mana harus melihat, atau Anda menebak?** Hambatan terkenal berada di tempat selain yang diharapkan insinyur berpengalaman, dan waktu yang dihabiskan menyetel kode yang salah hilang dua kali, sekali dalam pekerjaan dan sekali dalam kompleksitas tambahan. Budaya yang memprofil lebih dulu membelanjakan upayanya di tempat yang membuahkan hasil dan membiarkan kode yang jelas. Minta tim Anda mengingat tiga perbaikan kinerja terakhir dan apakah masing-masing dimulai dari pengukuran atau firasat. Pertimbangkan apakah Anda dapat memprofil di produksi, atau lingkungan staging yang realistis, karena profil laptop dapat menyesatkan parah. Jawabannya mengungkap apakah pekerjaan kinerja Anda rekayasa atau cerita rakyat.

3. **Apa yang menghentikan regresi kinerja mencapai produksi hari ini?** Pada tim yang tumbuh, jawaban jujurnya sering "keluhan pelanggan," artinya pengguna adalah tes regresi Anda. Gerbang CI yang menggagalkan build ketika tolok ukur atau anggaran memburuk menangkap masalah selagi murah diperbaiki dan penulis masih ingat perubahannya. Diskusikan apakah tolok ukur Anda cukup stabil untuk digerbangi, karena tes kinerja goyah yang berteriak serigala akan diabaikan atau dinonaktifkan. Bicarakan juga apa yang Anda awasi di produksi, karena sebagian regresi hanya muncul di bawah lalu lintas dan data nyata. Tujuannya adalah menjadikan kinerja sifat yang dipertahankan sistem secara otomatis, bukan yang Anda temukan ulang dalam insiden.

4. **Apakah Anda mengoptimalkan latensi atau throughput di setiap jalur kritis, dan adakah yang menuliskan pilihan itu?** Ini tujuan berbeda yang saling menarik ke arah berlawanan: batching dan pekerja paralel mengangkat throughput tetapi dapat menambah latensi pada permintaan individual, sehingga tim yang mengoptimalkan berdasarkan naluri sering membeli sumbu yang salah dan membuat pengguna menunggu demi menghemat waktu mesin yang tidak kekurangan siapa pun. Pada tim besar bahayanya berlipat, karena satu kelompok menyetel layanan bersama untuk throughput massal sementara yang lain bergantung padanya untuk latensi interaktif, dan tak satu pun tahu target yang lain. Bawa pola penggunaan aktual setiap jalur (permintaan interaktif versus batch latar belakang), latensi persentil saat ini, dan throughput berkelanjutan yang Anda butuhkan, lalu putuskan sumbunya secara eksplisit alih-alih membiarkan bawaan muncul. Untuk sistem enterprise atau pemerintah di bawah SLA, namai metrik mana yang menjadi dasar penulisan perjanjian, karena mengoptimalkan sumbu yang tak terukur dapat melanggar kontrak sementara dasbor Anda tampak sehat.

5. **Bagaimana Anda tahu tolok ukur Anda mengukur pekerjaan nyata alih-alih optimizer menghapus tes Anda?** Tolok ukur yang berbohong lebih buruk daripada tidak ada, karena menyerahkan keyakinan palsu kepada tim dan lalu regresi tetap dirilis. Tim rutin melaporkan satu angka beruntung dari eksekusi dingin pada masukan mainan, yang mengukur startup, kompilasi just-in-time, dan kemampuan kompiler menghapus kode tak terpakai alih-alih perilaku yang sebenarnya dialami pengguna. Bawa contoh tolok ukur dan interogasi: apakah ia memanaskan, menjalankan banyak iterasi, melaporkan varians, memakai ukuran dan distribusi data representatif, dan mengalahkan penghapusan kode mati pada hasilnya. Tarikan yang bersaing adalah bahwa tolok ukur jujur lebih lambat ditulis dan dijalankan daripada mikrotolok ukur cepat, jadi sepakati di mana pendekatan murah dapat diterima dan di mana Anda menuntut ketelitian. Dalam konteks publik atau yang diatur di mana pengadaan dan badan pengawas akan meminta Anda mereproduksi angkanya, tangkap perangkat, beban kerja, dan lingkungan bersama hasilnya agar klaim dapat diverifikasi alih-alih sekadar ditegaskan.

6. **Ketika pekerjaan kinerja bersaing dengan fitur untuk insinyur yang sama, bagaimana Anda memutuskan, dan siapa yang memegang wewenang anggaran?** Kinerja punya imbal hasil yang menurun tajam, sehingga perbaikan pertama berpemandu profil mungkin membelah dua latensi sementara yang kesepuluh memangkas satu persen dengan kompleksitas kode dua kali lipat, dan tanpa aturan suara paling lantang atau tenggat terdekat menang. Pertimbangan yang bersaing itu nyata: utang kinerja yang tak diperbaiki berlipat secara diam-diam dan makin mahal dipasang belakangan, namun mengejar kecepatan melewati anggaran membuat peta jalan kelaparan dan menambah kompleksitas yang memperlambat kerja mendatang. Bawa status anggaran saat ini untuk setiap jalur kritis, estimasi biaya status quo dalam mesin atau konversi yang hilang, dan imbalan marjinal optimasi berikutnya, agar trade-off dibuat berdasarkan bukti alih-alih tekanan. Untuk enterprise besar atau program pemerintah, namai siapa yang memiliki anggaran kinerja dan siapa yang dapat mengotorisasi pembelanjaan waktu rekayasa terhadapnya, karena target yang tak seorang pun bertanggung jawab membelanya adalah yang diam-diam terkikis.

## Lensa sektor

**Startup.** Kecepatan pengiriman mengalahkan proses, jadi tahan diri dari penulisan ulang dan kerangka kinerja besar. Habiskan satu sore dengan profiler pada jalur yang benar-benar dikeluhkan pengguna, perbaiki biaya terbesar (sering kueri N+1 atau pemindaian linier yang tidak disengaja), dan tambahkan satu anggaran persentil ringan ke CI agar kemenangan itu tidak dapat diam-diam mundur. Sisakan optimasi mendalam untuk saat angka nyata, bukan firasat, mengatakan kode terlalu lambat.

**Bisnis kecil.** Tanpa spesialis kinerja dan dengan anggaran ketat, bersandarlah pada perkakas yang sudah Anda bayar: profiler di runtime Anda, persentil latensi di dasbor hosting Anda, dan penganalisis kueri bawaan di basis data Anda. Tetapkan satu atau dua anggaran sederhana yang terikat pada sesuatu yang dirasakan pelanggan, seperti waktu muat halaman atau checkout, dan perlakukan pelanggaran sebagai sinyal untuk membeli tingkat lebih cepat atau memperbaiki kueri terburuk alih-alih meluncurkan proyek penyetelan yang tidak sanggup Anda isi stafnya.

**Enterprise.** Pada skala armada, kinerja adalah biaya langsung, jadi atur sebagai disiplin bersama: perkakas pemrofilan baku, anggaran persentil yang terikat pada metrik bisnis, dan gerbang regresi CI yang diterapkan konsisten agar rayapan lambat satu tim tidak menggelembungkan seluruh tagihan cloud. Lacak latensi, alokasi, dan throughput terhadap garis dasar di seluruh layanan, dan simpan bukti tolok ukur yang dapat direproduksi, karena pengurangan CPU 30% pada armada besar adalah penghematan berulang yang layak diaudit dan dibela terhadap penalti SLA.

**Pemerintah.** Kinerja adalah jaminan akses: halaman yang dimuat di ponsel lama melalui koneksi lemah menentukan apakah warga menyelesaikan klaim tunjangan. Tetapkan anggaran eksplisit terhadap perangkat kelas rendah yang realistis dan jaringan yang dibatasi, dan terbitkan hasil tolok ukur yang dapat direproduksi yang menangkap perangkat, jaringan, dan beban kerja, agar pengadaan dan badan pengawas dapat memverifikasi angkanya alih-alih menerimanya atas dasar kepercayaan. Pilih pengukuran yang transparan dan dapat diaudit daripada pernyataan vendor, dan tahan pemasok pada bukti yang dapat direproduksi yang sama.

## Contoh

**Startup.** Tim SaaS kecil memperhatikan dasbor mereka terasa lamban dan tergoda menulis ulang dalam kerangka kerja yang lebih cepat. Sebagai gantinya mereka menghabiskan satu sore dengan profiler dan flame graph, yang menunjukkan 70% waktu permintaan adalah satu endpoint yang menerbitkan satu kueri basis data per baris, pola N+1 klasik. Mereka menggantinya dengan satu kueri batch, latensi turun dari 1,2 detik menjadi 90 milidetik, dan mereka menambahkan anggaran p99 200 ms ke tolok ukur CI ringan agar perbaikan tidak dapat diam-diam mundur. Tanpa penulisan ulang, satu sore, kemenangan sepuluh kali lipat.

**Enterprise.** Platform ritel menjalankan ribuan instans, dan tagihan cloud-nya didominasi satu layanan rekomendasi. Kampanye pemrofilan menemukan gejolak alokasi berat yang menyebabkan jeda garbage collection yang sering, ditambah cache dengan tingkat hit buruk. Menyetel struktur data untuk lokalitas dan memperbaiki kunci cache memangkas CPU per permintaan 40%, yang memungkinkan tim menjalankan lalu lintas yang sama pada 40% lebih sedikit mesin. Penghematan itu membayar upaya rekayasa dalam hitungan minggu, dan SLA latensi p99 yang kadang dilanggar kini bertahan dengan nyaman, menghindari penalti kontraktual.

**Pemerintah.** Otoritas pajak nasional harus melayani warga di perangkat lama dan koneksi pedesaan yang lambat. Tim menetapkan anggaran eksplisit: halaman pengajuan harus menjadi interaktif dalam waktu kurang dari 3 detik pada ponsel kelas rendah melalui profil 3G yang dibatasi. Mereka memprofil halaman, memangkas pekerjaan penghalang interaktif, dan menerbitkan hasil tolok ukur yang dapat direproduksi, menangkap perangkat, jaringan, dan beban kerja, agar badan pengawas dan auditor aksesibilitas dapat memverifikasi klaim alih-alih menerimanya atas dasar kepercayaan. Kinerja di sini bukan tuas biaya melainkan jaminan akses yang menjaga layanan dapat digunakan semua orang.

## Kasus bisnis: motivasi, ROI, dan TCO

Imbal hasil rekayasa kinerja muncul di tiga buku besar. Yang pertama adalah biaya infrastruktur: kode lebih cepat mengerjakan pekerjaan yang sama pada lebih sedikit mesin, dan untuk armada besar pengurangan CPU 30% adalah penghematan langsung dan berulang yang melampaui upaya rekayasa sekali jalan. Yang kedua adalah pendapatan dan kepuasan: latensi berkorelasi dengan konversi, pengabaian, dan kepercayaan pengguna, jadi memangkas ekor adalah tuas pertumbuhan, bukan sekadar tugas kebersihan. Yang ketiga adalah risiko yang dihindari: pelanggaran SLA membawa penalti, dan peluncuran yang meleleh di bawah beban membawa kerusakan reputasi dan biaya pemadaman kebakaran.

Total biaya kepemilikannya sederhana dan terkonsentrasi di muka. Anda berinvestasi pada perkakas pemrofilan, lingkungan tolok ukur yang stabil, dan gerbang CI, ditambah disiplin menulis anggaran dan membaca profil. Biaya tersembunyi yang lebih besar adalah alternatifnya: utang kinerja berlipat secara diam-diam, dan memasang kecepatan ke dalam sistem lambat setelah peluncuran jauh lebih mahal daripada melindunginya terus-menerus. Ajukan kasus kepada pimpinan dalam satuan mereka sendiri. Terjemahkan latensi menjadi konversi atau tingkat penyelesaian warga, terjemahkan CPU menjadi belanja cloud bulanan, dan terjemahkan gerbang regresi menjadi insiden yang dihindari. Argumen terkuat adalah bahwa kinerja murah dilindungi commit demi commit dan merusak untuk dipulihkan setelah membusuk.

## Anti-pola dan jebakan

- **Mengoptimalkan tanpa memprofil.** Menyetel kode yang bukan hambatan sementara biaya nyata tidak tersentuh.
- **Optimasi prematur.** Mengorbankan kejelasan demi kecepatan yang dibayangkan yang tidak akan pernah ditandai profiler.
- **Melaporkan rata-rata.** Menyembunyikan ekor yang menyakitkan di balik rata-rata yang nyaman; pengguna merasakan p99, bukan rata-rata.
- **Teater mikrotolok ukur.** Angka dari beban kerja mainan yang setengah dihapus optimizer, tanpa pemanasan atau varians yang dilaporkan.
- **Cache tanpa cerita invalidasi.** Mengejar tingkat hit sambil menyajikan data basi atau keliru.
- **Mengira lebih banyak thread membantu.** Mengabaikan hukum Amdahl dan bagian serial, lalu tenggelam dalam perebutan.
- **Tanpa gerbang regresi.** Membiarkan pengguna menjadi tes kinerja karena tidak ada apa pun di CI yang menjaga anggaran.
- **Mengoptimalkan sumbu yang salah.** Membeli throughput dengan batching ketika pengguna membutuhkan latensi rendah, atau sebaliknya.

## Model kematangan

- **Tingkat 1, Memulai:** Kinerja ditangani hanya ketika sesuatu rusak. Tidak ada anggaran, tidak ada kebiasaan memprofil, tidak ada tolok ukur. Optimasi adalah tebakan yang digerakkan intuisi, dan rata-rata adalah satu-satunya metrik yang dilaporkan siapa pun.
- **Tingkat 2, Mengembangkan:** Beberapa tim memprofil selama insiden dan menyimpan beberapa tolok ukur, tetapi praktik tidak konsisten dan bergantung pada antusiasme individu. Anggaran ada secara informal untuk satu atau dua jalur kritis, dan persentil muncul di sebagian dasbor, namun tak ada yang menggerbangi regresi sebelum dirilis dan setiap tim menciptakan ulang pendekatannya sendiri.
- **Tingkat 3, Membakukan:** Jalur kritis membawa anggaran persentil tertulis, dan pemrofilan adalah langkah pertama yang terdokumentasi dan diharapkan sebelum siapa pun mengoptimalkan. CI mencakup tes kinerja dengan gerbang regresi, aturan tolok ukur jujur (pemanasan, varians, data representatif) ditulis dan ditegakkan di seluruh organisasi, dan setiap tim mengikuti metode yang sama alih-alih metodenya sendiri.
- **Tingkat 4, Mengelola:** Organisasi mengukur kinerja sebagai sifat terkendali. Persentil latensi, throughput, laju alokasi, dan jumlah kueri lambat dilacak terhadap garis dasar eksplisit di produksi dan CI, regresi dikuantifikasi terhadap ambang alih-alih diperdebatkan, dan anggaran terikat pada metrik bisnis seperti konversi atau belanja cloud sehingga pelanggaran memicu keputusan berbasis data. Bukti tolok ukur dapat direproduksi dan ditangkap dengan perangkat, beban kerja, dan lingkungannya untuk audit.
- **Tingkat 5, Mengorkestrasi:** Kinerja terus diperbaiki dan terintegrasi di seluruh organisasi. Anggaran, pemrofilan, tolok ukur jujur, dan analisis flame graph adalah keterampilan rutin, gerbang regresi stabil dan tepercaya, dan data produksi serta CI menutup lingkaran secara otomatis. Organisasi menyesuaikan anggaran seiring bergesernya lalu lintas, perangkat keras, dan prioritas bisnis, menyeimbangkan kembali upaya ke jalur dengan imbalan tertinggi, dan membela kinerja sebagai sifat tetap alih-alih kampanye berkala.

## Gagasan untuk didiskusikan

1. Jalur kritis Anda yang mana yang memiliki anggaran tertulis berbasis persentil hari ini, dan mana yang dilindungi hanya oleh harapan?
2. Kapan profiler terakhir mengejutkan Anda, dan apa yang diajarkannya tentang di mana Anda mengira waktu dihabiskan?
3. Apakah tolok ukur Anda memanaskan, melaporkan varians, dan memakai data representatif, atau sedang mengukur optimizer?
4. Di mana Anda membelanjakan mesin untuk menutupi kode yang dapat dibuat lebih murah oleh kampanye pemrofilan?
5. Untuk beban kerja Anda yang paling diparalelkan, berapa bagian serialnya, dan apakah hukum Amdahl membatasi percepatan yang Anda kejar?
6. Jika rekan menggabungkan perubahan yang menggandakan latensi p99, berapa lama sampai ada yang menyadarinya, dan bagaimana mereka akan mengetahuinya?

## Poin-poin utama

- Ukur sebelum mengoptimalkan; hambatan jarang di tempat Anda menebak, dan optimasi prematur memakan kejelasan tanpa keuntungan.
- Definisikan "cukup cepat" sebagai anggaran persentil, karena rata-rata menyembunyikan ekor tempat pengguna nyata hidup.
- Pilih kemenangan algoritmik (kelas Big O yang lebih baik) daripada penyetelan mikro, dan ketahui apakah Anda butuh latensi atau throughput.
- Hormati batas paralelisme (hukum Amdahl) dan bahaya caching (invalidasi dan kebasian).
- Lakukan tolok ukur dengan jujur memakai pemanasan, varians, dan beban kerja representatif, dan curigai mikrotolok ukur.
- Gerbangi kinerja di CI (bab 2.4) dan amati di produksi (bab 9.2); lengkapi dengan pandangan tingkat sistem di bab 3.5.
- Kinerja adalah biaya bagi enterprise, akses bagi pemerintah, murah dilindungi terus-menerus tetapi mahal dipasang belakangan.

## Referensi dan bacaan lanjutan

- Brendan Gregg, *Systems Performance: Enterprise and the Cloud* (pemrofilan, flame graph, dan metode).
- Brendan Gregg, *BPF Performance Tools* (observabilitas dan pemrofilan praktis di Linux).
- Donald E. Knuth, "Structured Programming with go to Statements" (*ACM Computing Surveys*, 1974): sumber pepatah optimasi prematur.
- Donald E. Knuth, *The Art of Computer Programming* (analisis algoritmik dan kompleksitas).
- Thomas H. Cormen, Charles E. Leiserson, Ronald L. Rivest, dan Clifford Stein, *Introduction to Algorithms* (Big O dan efisiensi algoritmik).
- Gene M. Amdahl, "Validity of the Single Processor Approach to Achieving Large-Scale Computing Capabilities" (1967): asal hukum Amdahl.
- Ulrich Drepper, "What Every Programmer Should Know About Memory" (hierarki memori dan lokalitas data).
- Martin Kleppmann, *Designing Data-Intensive Applications* (latensi, throughput, dan perilaku ekor dalam sistem).
- Aleksey Shipilev, "JMH and the pitfalls of microbenchmarking" (praktik tolok ukur jujur pada runtime terkelola).
- Ilya Grigorik, *High Performance Browser Networking* (kinerja sisi klien dan jaringan bagi pengguna berbandwidth rendah).
