# 3.1 Dasar-dasar arsitektur

## Tinjauan dan motivasi

[Arsitektur perangkat lunak](https://en.wikipedia.org/wiki/Software_architecture) adalah himpunan keputusan desain penting yang mahal untuk diubah: struktur komponen utama, hubungan di antaranya, dan sifat yang harus ditunjukkan seluruh sistem. Anggaplah sebagai model mental bersama yang memungkinkan banyak orang membangun satu produk yang koheren. Pada tim kecil, arsitektur dapat hidup di beberapa kepala dan berkembang seiring jalan. Dalam organisasi besar (ratusan insinyur, puluhan tim, banyak produk, bertahun-tahun peta jalan), arsitektur menjadi hal yang menjaga semua orang tetap terkoordinasi. Ketika jelas, tim bergerak secara independen tanpa bertabrakan. Ketika kabur, setiap dependensi lintas tim berubah menjadi negosiasi, dan setiap insiden berubah menjadi proyek arkeologi.

Bagi enterprise dan pemerintah, fundamental ini lebih penting lagi, karena sistemnya berumur panjang, sangat diatur, dan dibagikan lintas departemen. Sistem pajak, platform tunjangan, rekam medis nasional, atau buku besar inti bank akan hidup lebih lama daripada karier orang yang membangunnya. Keputusan yang Anda buat hari ini tentang kopling, kepemilikan data, dan [atribut kualitas](https://en.wikipedia.org/wiki/List_of_system_quality_attributes) membatasi apa yang mungkin selama satu dekade atau lebih. Regulator dan auditor makin mengharapkan arsitektur yang terdokumentasi dan dapat dipertanggungjawabkan: bukti bahwa keandalan, keamanan, privasi, dan aksesibilitas dirancang masuk, bukan ditempelkan belakangan. Mendapatkan fundamental dengan benar bukan soal akademis. Itu beda antara platform yang beradaptasi dengan mandat baru dan yang harus dibangun ulang dari nol.

Bab ini membahas fundamental tahan lama yang bertahan dari mode teknologi: atribut kualitas (si "-ilities"), persyaratan signifikan arsitektural, fitness function dan arsitektur evolusioner, dokumentasi ringan dengan [C4](https://en.wikipedia.org/wiki/C4_model) dan arc42, serta analisis trade-off terstruktur. Inilah perkakas yang memungkinkan tim besar bernalar tentang arsitektur dengan sengaja alih-alih kebetulan.

## Prinsip utama

- **Arsitektur adalah soal trade-off, bukan jawaban yang benar.** Setiap keputusan penting menukar satu kualitas dengan yang lain; tugasnya membuat pertukaran itu dengan sengaja dan transparan.
- **Atribut kualitas adalah persyaratan.** Kinerja, ketersediaan, keamanan, dan kemudahan pemeliharaan harus dispesifikasikan dengan ketelitian yang sama seperti fitur, atau akan dikorbankan di bawah tekanan tenggat.
- **Tidak setiap persyaratan signifikan secara arsitektural.** Fokuskan perhatian desain yang langka pada persyaratan yang membentuk struktur, sulit diubah, atau berisiko tinggi.
- **Arsitektur harus dapat berkembang.** Desain besar di muka gagal karena pengetahuan paling rendah di awal; rancang secara bertahap dan lindungi sifat kunci dengan pemeriksaan otomatis.
- **Dokumentasikan keputusan, bukan hanya diagram.** Alasan di balik suatu pilihan (dan opsi yang ditolak) lebih berharga daripada gambar hasilnya.
- **Buat arsitektur terbaca oleh mereka yang tidak menciptakannya.** Anggota baru, auditor, dan pemelihara masa depan harus dapat merekonstruksi maksudnya.
- **Tunda keputusan yang bisa, putuskan yang harus.** Jaga opsi tetap terbuka di mana perubahan murah; berkomitmen awal hanya di mana komitmen terlambat mahal.

## Rekomendasi

### Spesifikasikan atribut kualitas sebagai skenario terukur

Tujuan samar seperti "sistem harus cepat" atau "sangat tersedia" tidak dapat diuji atau ditegakkan. Sebagai gantinya, tulis setiap atribut kualitas sebagai skenario konkret dengan stimulus, konteks, dan respons terukur: "Ketika pengguna konkuren puncak mencapai 50.000, 95% permintaan pencarian selesai dalam 300 ms." Cakup atribut yang penting bagi domain Anda: ketersediaan, kinerja, skalabilitas, keamanan, kemudahan pemeliharaan, observabilitas, aksesibilitas, portabilitas, dan efisiensi biaya. Peringkatkan dengan lantang, karena Anda tidak dapat memaksimalkan semuanya sekaligus. Sistem yang disetel untuk konsistensi maksimum tidak akan sekaligus tersedia maksimum.

### Identifikasi persyaratan signifikan arsitektural (ASR)

Sisihkan waktu untuk memisahkan ASR dari persyaratan biasa. Persyaratan signifikan secara arsitektural jika menyentuh banyak komponen, mahal dipenuhi, memaksakan kendala ketat, atau berisiko secara teknis. Mandat regulasi (residensi data, retensi, kemampuan diaudit), skenario beban tinggi, integrasi dengan sistem pencatat warisan, dan batas keamanan keras biasanya ASR. Simpan daftar singkat dan hidup tentangnya, dan lacak keputusan desain utama kembali ke daftar itu, agar peninjau dapat melihat mengapa arsitektur tampak seperti adanya.

### Adopsi arsitektur evolusioner dan fitness function

Perlakukan arsitektur sebagai sesuatu yang berubah selangkah demi selangkah ke arah yang dipandu, bukan cetak biru tetap. **Fitness function** adalah tes otomatis dan objektif bahwa karakteristik arsitektural tertentu bertahan: pemeriksaan saat build bahwa tidak ada modul yang mengimpor dari lapisan terlarang, tes kinerja yang menggagalkan pipeline jika latensi p99 mundur, pemindaian keamanan yang memblokir dependensi rentan yang diketahui, tes yang mengonfirmasi tidak ada layanan yang memegang koneksi langsung ke basis data layanan lain. Fitness function mengubah maksud arsitektural menjadi pagar pembatas yang ditegakkan terus-menerus: satu-satunya cara menjaga maksud itu hidup di tim besar yang terus berubah.

### Dokumentasikan dengan C4 dan arc42

Gunakan **model C4** untuk menjelaskan struktur pada empat tingkat zoom (System Context, Containers, Components, dan Code) agar setiap audiens membaca tingkat yang cocok dan tak ada diagram tunggal yang harus mengatakan segalanya. Gunakan **arc42** sebagai templat untuk narasi di sekelilingnya: tujuan, kendala, konteks, strategi solusi, blok bangunan, skenario runtime, deployment, perhatian lintas bidang, keputusan, dan risiko. Catat keputusan individual sebagai **[Architecture Decision Record (ADR)](https://en.wikipedia.org/wiki/Architectural_decision)** singkat: konteks, keputusan, status, dan konsekuensi, satu berkas per keputusan, berversi bersama kode. Jika Anda hanya mengadopsi satu kebiasaan dokumentasi, jadikan ADR: mereka membayar lebih daripada apa pun bagi tim besar.

### Jalankan analisis trade-off terstruktur dan gerakkan desain berdasarkan risiko

Untuk sistem bertaruhan tinggi, gunakan metode seperti **[Architecture Tradeoff Analysis Method (ATAM)](https://en.wikipedia.org/wiki/Architecture_tradeoff_analysis_method)** untuk menimbang arsitektur kandidat terhadap skenario atribut kualitas yang diprioritaskan. Ia memunculkan titik sensitivitas (di mana keputusan sangat memengaruhi satu atribut) dan titik trade-off (di mana memengaruhi beberapa). Untuk sentuhan lebih ringan, adopsi **desain berbasis risiko**: belanjakan upaya desain sebanding dengan risiko. Bagian berisiko rendah dan dipahami baik membutuhkan sedikit upacara. Keputusan baru, berdampak tinggi, atau tak terbalikkan layak mendapat prototipe, spike, dan tinjauan formal.

## Trade-off: kelebihan dan kekurangan

| Pendekatan | Kelebihan | Kekurangan |
|---|---|---|
| Arsitektur besar di muka | Kejelasan koordinasi; lebih sedikit kejutan terlambat dalam program cakupan tetap | Keputusan dibuat saat pengetahuan paling rendah; lambat; rapuh terhadap perubahan |
| Arsitektur muncul / evolusioner | Beradaptasi dengan pembelajaran; lebih sedikit pemborosan; mendukung pengiriman cepat | Risiko penyimpangan tanpa fitness function; butuh disiplin rekayasa yang kuat |
| Evaluasi formal ala ATAM | Teliti, dapat diaudit, memunculkan konflik tersembunyi | Padat waktu dan keahlian; berlebihan untuk perubahan kecil |
| ADR ringan + C4 | Murah, terbaca, bertahap, berskala ke banyak tim | Hanya sebaik disiplin menjaganya mutakhir |

Ketegangan pusatnya adalah antara kepastian dan kemampuan beradaptasi. Program pemerintah berharga tetap dan sistem kritis keselamatan condong ke ketelitian di muka dan evaluasi formal yang lebih banyak, karena biaya perubahan terlambat atau kegagalan sangat besar. Organisasi produk yang bergerak cepat condong ke pendekatan evolusioner yang dijaga otomasi. Kebanyakan organisasi besar membutuhkan keduanya: tata kelola lebih berat pada keputusan tak terbalikkan dan berdampak tinggi serta perhatian lintas bidang, dan desain lebih ringan dan muncul di tempat lain. Kedua ekstrem gagal dengan caranya sendiri: terlalu banyak merancang membuang bertahun-tahun dan tidak menghasilkan apa-apa, sementara terlalu sedikit merancang menghasilkan kekusutan yang tidak dapat berskala atau diaudit.

## Pertanyaan untuk didiskusikan dengan tim Anda

1. **Ketika dua atribut kualitas Anda bertabrakan di bawah beban, mana yang menang, dan apakah Anda telah menuliskan urutan prioritas itu?** Setiap arsitektur memaksa pertukaran: konsistensi maksimum melemahkan ketersediaan, keamanan ketat menambah latensi, caching agresif melawan kemampuan diaudit. Pada tim besar bahayanya adalah skuad berbeda diam-diam mengasumsikan prioritas berbeda, sehingga satu mengoptimalkan throughput sementara yang lain menjaga konsistensi ketat, dan konflik hanya muncul selama insiden. Dalam lingkungan enterprise dan pemerintah regulator akan menanyakan atribut mana yang Anda lindungi dan mengapa, jadi peringkat harus eksplisit dan dapat dipertanggungjawabkan alih-alih cerita rakyat. Bawa skenario atribut kualitas Anda dan peringkatkan dengan lantang satu sama lain, pasangan demi pasangan, sampai urutannya tidak ambigu. Lalu kodekan pemenangnya sebagai fitness function agar prioritas bertahan di bawah tekanan tenggat alih-alih terkikis.

2. **Keputusan terbaru Anda yang mana yang merupakan pintu satu arah, dan apakah mereka mendapat pengawasan lebih daripada pintu dua arah?** Desain berbasis risiko mengatakan belanjakan upaya desain sebanding dengan seberapa sulit keputusan dibalik, namun kebanyakan tim meninjau setiap perubahan dengan upacara yang kira-kira sama. Itu membuang perhatian pada pilihan murah dan dapat dibalik sementara yang tak terbalikkan (model data yang dipanggang ke catatan hukum, kontrak API publik, penyimpanan data inti) lolos dengan tantangan terlalu sedikit. Tarik keputusan penting kuartal lalu dan pilah menurut keterbalikan, lalu tanyakan apakah yang tak terbalikkan mendapat prototipe, spike, atau tinjauan formal. Dalam sistem enterprise dan pemerintah berumur panjang biaya pintu satu arah yang keliru berlipat selama satu dekade, jadi ketelitian ekstra membayar kembali berkali-kali. Cocokkan bobot proses Anda dengan keterbalikan keputusan, bukan dengan ukuran diff.

3. **Untuk keputusan bertaruhan tinggi dan sulit dibalik berikutnya, siapa yang perlu berada di ruangan, dan terhadap skenario mana Anda akan menilai opsi?** Tinjauan trade-off terstruktur ala ATAM pantas biayanya ketika keputusan tak terbalikkan dan menyentuh beberapa atribut kualitas sekaligus, dan kekuatannya datang dari orang yang hadir: pengiriman, keamanan, operasi, dan pemilik kebijakan atau bisnis yang merasakan konsekuensinya. Lewatkan salah satu suara itu dan Anda menemukan konflik setelah pembangunan, seperti pilihan caching dapat diam-diam merusak persyaratan kemampuan diaudit. Bawa skenario atribut kualitas yang diprioritaskan sebagai rubrik penilaian, dan cari titik sensitivitas di mana satu opsi mengayunkan satu atribut keras dan titik trade-off di mana ia menggerakkan beberapa. Keluaran yang Anda inginkan adalah ADR singkat yang mencatat opsi yang Anda tolak dan alasannya, agar alasan itu bertahan melewati orang yang membuatnya. Jika tak ada keputusan mendatang yang tampak membenarkan ini, itu sendiri layak diperiksa, karena program besar tanpa keputusan tak terbalikkan di cakrawala biasanya tidak melihat cukup jauh.

4. **Jika anggota baru atau auditor eksternal hanya memiliki arsitektur tertulis Anda, dapatkah mereka merekonstruksi mengapa sistem berbentuk seperti itu, dan kapan terakhir kali Anda menguji itu?** Arsitektur yang hidup di beberapa kepala senior adalah titik kegagalan tunggal: ketika orang-orang itu berpindah, alasan di balik setiap keputusan sulit dibalik ikut pergi, dan tim berikutnya mempelajarinya lagi lewat insiden. Bagi organisasi besar keterbacaan arsitektur (diagram C4 yang cocok dengan kenyataan, narasi arc42, ADR yang mencatat opsi tertolak) adalah yang memungkinkan puluhan tim bernalar tentang sistem yang sama tanpa rapat. Bawa ADR terbaru dan diagram terkini, serahkan kepada seseorang yang tidak membangun komponen itu, dan saksikan sejauh mana mereka maju sebelum harus bertanya kepada seseorang. Dalam lingkungan enterprise dan pemerintah auditor akan melakukan latihan persis ini, dan dokumentasi yang menjelaskan sistem tahun lalu lebih buruk daripada tidak ada karena menyesatkan justru orang yang harus mensertifikasinya. Perlakukan kesegaran catatan tertulis sebagai sifat terukur, dan pasang fitness function atau irama tinjauan di belakang menjaganya tetap benar.

5. **Karakteristik arsitektural Anda yang mana yang dilindungi fitness function otomatis hari ini, dan mana yang masih bergantung pada semua orang mengingat aturannya?** Maksud yang hanya hidup di halaman wiki atau ingatan peninjau terkikis begitu tenggat tiba, karena aturan pelapisan, batas tanpa-basis-data-bersama, dan anggaran latensi adalah persis yang dipotong tim ketika di bawah tekanan. Pada basis kode besar yang cepat berubah, satu-satunya maksud yang bertahan adalah yang ditegakkan build, sehingga jarak antara karakteristik yang Anda klaim dan yang benar-benar Anda periksa adalah risiko arsitektural nyata Anda. Daftarkan karakteristik penting Anda, tandai masing-masing sebagai ditegakkan, ditinjau manual, atau tak terjaga, dan bawa tiga kali terakhir tinjauan menangkap penyimpangan yang dapat ditangkap fitness function lebih awal. Dalam sistem yang diatur dan publik ini penting dua kali lipat, karena regulator akan bertanya bukan apakah Anda bermaksud residensi data atau kemampuan diaudit melainkan bagaimana Anda membuktikan itu bertahan terus-menerus, dan pipeline hijau adalah jawaban yang jauh lebih kuat daripada dokumen kebijakan. Prioritaskan mengotomatiskan karakteristik yang kegagalannya sekaligus mungkin dan mahal, dan terima bahwa sebagian akan tetap manual.

6. **Ketika Anda memutuskan apakah persyaratan signifikan secara arsitektural, siapa yang membuat penilaian itu, dan bagaimana Anda menjaga daftar ASR agar tidak menjadi segalanya atau tidak sama sekali?** Nilai menamai persyaratan signifikan arsitektural datang dari selektivitas: perlakukan setiap persyaratan sebagai signifikan dan desain terhenti, perlakukan tak satu pun sebagai signifikan dan yang struktural, berisiko, dan sulit diubah lolos tanpa penjagaan. Pada tim besar godaannya adalah membiarkan setiap skuad memutuskan secara lokal, yang menghasilkan standar tidak konsisten dan kejutan lintas tim ketika pilihan "kecil" satu kelompok membatasi struktur kelompok lain. Bawa daftar ASR Anda saat ini, kriteria yang Anda pakai (menyentuh banyak komponen, mahal dipenuhi, kendala ketat, berisiko teknis), dan beberapa persyaratan batas untuk menguji batasnya dengan lantang. Untuk enterprise dan pemerintah, mandat regulasi seperti residensi data, retensi, dan kemampuan diaudit hampir selalu signifikan dan tak dapat ditawar, jadi namai siapa yang memiliki daftar itu, bagaimana ia ditinjau, dan bagaimana keputusan menambah atau menjatuhkan ASR dicatat, karena ASR yang tidak diatur siapa pun adalah persyaratan yang tak akan dibela siapa pun di bawah pengawasan.

## Lensa sektor

**Startup.** Jaga upacara mendekati nol dan catatan mendekati lengkap. Lewati lokakarya ATAM formal dan templat berat, tetapi tetap tulis selusin ADR singkat untuk pilihan yang akan menyakitkan diurai (penyimpanan data, monolit versus layanan, penyedia autentikasi) dan sematkan dua atau tiga skenario atribut kualitas yang benar-benar dirasakan pelanggan awal Anda. Sumber daya Anda yang langka adalah perhatian rekayasa, jadi lindungi hanya karakteristik yang kegagalannya akan menenggelamkan Anda, seperti isolasi tenant, dan biarkan yang lain tetap muncul dan murah diubah.

**Bisnis kecil.** Tanpa arsitek khusus dan dengan anggaran ketat, bersandarlah pada fundamental yang nyaris tidak berbiaya: namai segelintir atribut kualitas Anda sebagai angka konkret, tulis ADR untuk apa pun yang akan sulit Anda balik, dan biarkan platform atau vendor pilihan Anda memikul keputusan struktural berat. Pilih membeli tumpukan yang didukung baik daripada membangun infrastruktur khusus, dan perlakukan arsitektur terdokumentasi vendor sebagai kendala yang Anda warisi alih-alih yang harus Anda susun dari awal.

**Enterprise.** Tantangannya adalah koherensi di banyak tim dan bertahun-tahun peta jalan, jadi berinvestasilah pada mesin bersama: guild arsitektur, himpunan skenario atribut kualitas umum, ADR yang disimpan di samping kode, dan fitness function di CI yang menegakkan batas yang tak dapat dijaga satu peninjau pun pada skala besar. Gunakan analisis trade-off terstruktur untuk keputusan tak terbalikkan dan lintas bidang, simpan diagram C4 sebagai peta bersama dalam tinjauan desain, dan atur daftar ASR secara terpusat agar kelompok berhenti membuat pilihan yang masuk akal secara lokal yang bertabrakan secara global.

**Pemerintah.** Sistem berumur panjang dan diatur menjadikan arsitektur yang terdokumentasi dan dapat dipertanggungjawabkan sebagai persyaratan pengadaan dan akuntabilitas, bukan kesopanan. Perlakukan residensi data, retensi, kemampuan diaudit, dan aksesibilitas sebagai persyaratan signifikan arsitektural yang ditulis ke dalam deskripsi arc42 yang dapat dibaca langsung auditor, dan jalankan lokakarya trade-off ringan yang menyertakan pejabat kebijakan dan keamanan agar konflik (seperti caching versus kemampuan diaudit) muncul di atas kertas sebelum kode. Jaga jejak alasan cukup lengkap agar pejabat yang bertanggung jawab dapat menunjukkan uji tuntas, dan pilih arsitektur dengan opsi keluar yang jelas daripada yang mengunci badan publik pada satu vendor selama satu dekade.

## Contoh

**Startup.** Tim SaaS tahap benih enam orang menyimpan arsitekturnya dalam dokumen bersama alih-alih proses formal, tetapi tetap menuliskan keputusan yang akan menyakitkan dibalik. Mereka mencatat sekitar selusin ADR (mengapa Postgres daripada penyimpanan dokumen, mengapa monolit modular daripada layanan, mengapa mereka memilih penyedia autentikasi) dan menyematkan dua skenario atribut kualitas yang benar-benar penting bagi pelanggan awal: "pendaftaran selesai dalam kurang dari dua detik" dan "tak ada pelanggan yang pernah dapat membaca data tenant lain." Ketika mereka merekrut insinyur ketujuh dan kedelapan, catatan itu memungkinkan pendatang baru merilis pada minggu pertama alih-alih menginterupsi semua orang untuk bertanya mengapa segalanya seperti adanya.

**Enterprise.** Sebuah bank multinasional mengonsolidasikan dua belas sistem pembayaran regional, jadi ia mendirikan guild arsitektur kecil. Guild mendefinisikan delapan skenario atribut kualitas (termasuk "proses 10.000 transaksi per detik dengan nol transaksi hilang" dan "pulihkan satu wilayah dalam 15 menit"), menangkap sekitar empat puluh ADR, dan menegakkan fitness function di CI ([integrasi berkelanjutan](https://en.wikipedia.org/wiki/Continuous_integration)): tidak ada layanan yang boleh menulis ke basis data domain lain, semua panggilan antarlayanan harus dilacak, dan dependensi apa pun dengan [CVE](https://en.wikipedia.org/wiki/Common_Vulnerabilities_and_Exposures) (Common Vulnerabilities and Exposures) kritis menggagalkan build. Diagram konteks dan kontainer C4 menjadi peta bersama dalam setiap tinjauan desain, dan perselisihan integrasi lintas tim turun tajam.

**Pemerintah.** Sebuah lembaga nasional memodernisasi platform tunjangan, dan hukum mewajibkannya menjamin residensi data, kemampuan diaudit tujuh tahun, dan kesesuaian aksesibilitas. Arsiteknya memperlakukan ini sebagai ASR dan menuliskannya ke dalam deskripsi arc42 yang ditinjau langsung auditor. Mereka menjalankan lokakarya ATAM ringan dengan tim pengiriman, keamanan, dan pejabat kebijakan untuk membandingkan dua arsitektur kandidat, dan menemukan bahwa strategi caching desain pilihan bertentangan dengan persyaratan kemampuan diaudit. Menangkap trade-off itu di atas kertas, sebelum satu baris kode, menghemat berbulan-bulan pengerjaan ulang dan memberi menteri yang bertanggung jawab bukti terdokumentasi uji tuntas.

## Kasus bisnis: motivasi, ROI, dan TCO

Imbal hasil dasar-dasar arsitektur sebagian besar adalah biaya yang dihindari, yang membuatnya mudah kekurangan dana dan mahal dilewatkan. Biaya mengadopsi sederhana: waktu segelintir arsitek berpengalaman, beberapa lokakarya, templat dokumentasi, dan sedikit investasi CI dalam fitness function, biasanya persentase satu digit kecil dari anggaran program. Biaya *tidak* mengadopsinya tiba kemudian, dan dengan harga premium: pengerjaan ulang ketika atribut kualitas yang tak terspesifikasi gagal di produksi, re-platforming darurat ketika kopling tak terdokumentasi memblokir perubahan yang diwajibkan, insiden berkepanjangan karena tak seorang pun memahami sistem, dan audit gagal yang menghentikan pengiriman atau memicu denda.

Bagi pimpinan, bingkai kasus di sekitar opsionalitas dan risiko. Dasar-dasar arsitektur yang baik menurunkan biaya perubahan di masa depan (tuas langsung atas kecepatan pengiriman dan total biaya kepemilikan sepanjang umur sistem sedekade), mengurangi seberapa sering dan seberapa lama insiden parah berlangsung, dan menghasilkan jejak dokumentasi yang kini dituntut regulator dan auditor. Kebiasaan ADR saja membayar dirinya sendiri pertama kali tim pimpinan baru bertanya "mengapa kita membangunnya begini?" dan mendapat jawaban dalam menit alih-alih penyelidikan forensik. Beri angka di mana bisa: timbang biaya satu rearsitektur besar yang dihindari, atau satu audit gagal yang dihindari, terhadap biaya berkelanjutan kecil dari praktik itu.

## Anti-pola dan jebakan

- **Arsitektur menara gading.** Arsitek yang menghasilkan diagram tetapi tidak pernah menyentuh kode atau berbicara dengan tim pengiriman; desain mereka diabaikan atau tak dapat dibangun.
- **Atribut kualitas sebagai kata sifat.** "Skalabel, aman, andal" tanpa angka, tanpa skenario, dan karenanya tanpa cara memverifikasi atau menukarnya.
- **Desain besar di muka.** Berkomitmen pada setiap detail sebelum baris kode pertama, mengunci keputusan ketika pemahaman paling lemah.
- **Dokumentasi yang berbohong.** Diagram yang menjelaskan sistem tahun lalu; lebih buruk daripada tidak ada karena menyesatkan.
- **Desain berbasis resume.** Memilih teknologi untuk membangun karier alih-alih memenuhi ASR.
- **Pelapisan emas.** Merekayasa skala, fleksibilitas, atau generalitas yang tak pernah diminta persyaratan, menambah biaya dan kompleksitas secara permanen.
- **Tanpa pagar arsitektural.** Mengandalkan niat baik alih-alih fitness function untuk menjaga struktur di tim besar.

## Model kematangan

- **Tingkat 1: Memulai.** Arsitektur implisit dan hidup di kepala individu. Tidak ada atribut kualitas terdokumentasi, tidak ada ADR, tidak ada diagram bersama. Struktur ditemukan selama insiden, dan setiap dependensi lintas tim dinegosiasikan ulang dari awal.
- **Tingkat 2: Mengembangkan.** Beberapa tim menuliskan keputusan yang akan menyakitkan dibalik dan membuat sketsa diagram kunci, tetapi praktik tidak konsisten: satu skuad menyimpan ADR sementara yang lain tidak, atribut kualitas disebut sebagai kata sifat alih-alih skenario terukur, dan dokumentasi menyimpang antarproyek.
- **Tingkat 3: Membakukan.** Skenario atribut kualitas dan persyaratan signifikan arsitektural dispesifikasikan dan diprioritaskan menurut standar terdokumentasi seluruh organisasi. ADR rutin dan disimpan di samping kode, dokumentasi C4 dan arc42 dipelihara menurut templat umum, dan tinjauan trade-off terstruktur diwajibkan untuk keputusan penting di setiap tim.
- **Tingkat 4: Mengelola.** Arsitektur diukur terhadap garis dasar alih-alih ditegaskan. Fitness function di CI melaporkan karakteristik seperti latensi p99, pelanggaran pelapisan, panggilan tak terlacak, dan dependensi rentan; cakupan ADR dan kesegaran dokumentasi dilacak sebagai metrik; tinjauan trade-off menilai opsi terhadap skenario yang diprioritaskan; dan penyimpangan terhadap garis dasar yang disepakati memicu respons terdefinisi alih-alih kejutan. Auditor dapat mengandalkan bukti terukur, bukan hanya narasi.
- **Tingkat 5: Mengorkestrasi.** Arsitektur berkembang terus-menerus dan adaptif di seluruh organisasi. Data fitness function dan insiden memberi umpan balik ke karakteristik mana yang penting dan ke mana upaya desain pergi; daftar ASR, prioritas atribut kualitas, dan pagar pembatas diubah cakupannya seiring bergesernya mandat dan risiko; dan praktik terintegrasi dengan pengiriman, keamanan, dan perencanaan risiko sehingga platform beradaptasi dengan persyaratan baru alih-alih dibangun ulang dari nol.

## Gagasan untuk didiskusikan

1. Tiga atribut kualitas mana yang benar-benar tak dapat ditawar untuk sistem paling kritis Anda, dan dapatkah Anda menyatakan masing-masing sebagai skenario terukur hari ini?
2. Bagaimana Anda memutuskan kapan keputusan cukup signifikan secara arsitektural untuk layak mendapat ADR versus sekadar dikerjakan?
3. Di mana fitness function akan menangkap penyimpangan yang terlewat tinjauan kode Anda saat ini?
4. Apakah organisasi Anda terlalu banyak merancang atau terlalu sedikit merancang, dan bukti apa yang memberi tahu Anda mana?
5. Siapa yang bertanggung jawab atas arsitektur dalam struktur tim-dari-tim, dan bagaimana Anda menghindari menara gading maupun anarki total?
6. Bagaimana auditor eksternal akan merekonstruksi maksud arsitektur Anda dari apa yang tertulis hari ini?

## Poin-poin utama

- Arsitektur adalah himpunan keputusan yang mahal dibalik; buat pertukaran itu dengan sengaja dan catat.
- Spesifikasikan atribut kualitas sebagai skenario terukur dan identifikasi persyaratan signifikan arsitektural yang membentuk struktur.
- Rancang secara bertahap dan lindungi karakteristik arsitektural kunci dengan fitness function otomatis.
- Dokumentasikan secara ringan tetapi jujur memakai diagram C4, narasi arc42, dan ADR per keputusan yang disimpan di samping kode.
- Cocokkan ketelitian dengan risiko: analisis berat untuk keputusan tak terbalikkan dan berdampak tinggi; proses ringan di tempat lain.
- Kasus bisnisnya adalah pengerjaan ulang yang dihindari, insiden lebih singkat, perubahan mendatang lebih cepat, dan bukti siap-audit.

## Referensi dan bacaan lanjutan

- Len Bass, Paul Clements, dan Rick Kazman, *Software Architecture in Practice*
- Neal Ford, Rebecca Parsons, dan Patrick Kua, *Building Evolutionary Architectures*
- Simon Brown, *Software Architecture for Developers* (dan model C4)
- Mark Richards dan Neal Ford, *Fundamentals of Software Architecture*
- George Fairbanks, *Just Enough Software Architecture: A Risk-Driven Approach*
- Michael Nygard, "Documenting Architecture Decisions" (pola ADR)
- Gernot Starke dan Peter Hruschka, templat dokumentasi *arc42*
- Paul Clements et al., *Evaluating Software Architectures: Methods and Case Studies* (ATAM)
- ISO/IEC 25010, *Systems and software quality models*
