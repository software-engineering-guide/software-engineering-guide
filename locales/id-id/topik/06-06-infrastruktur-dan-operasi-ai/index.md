# 6.6 Infrastruktur dan operasi AI

## Tinjauan dan motivasi

Infrastruktur dan operasi AI adalah disiplin menyediakan, menjadwalkan, dan menjalankan sistem komputasi, penyimpanan, dan penyajian khusus yang dituntut beban kerja AI, dengan hemat biaya, andal, dan dapat diamati. AI modern mahal dijalankan. Melatih dan menyajikan model besar membutuhkan akselerator langka ([GPU](https://en.wikipedia.org/wiki/Graphics_processing_unit) dan [TPU](https://en.wikipedia.org/wiki/Tensor_Processing_Unit)), jaringan berbandwidth tinggi, penyimpanan vektor skala besar untuk pengambilan (mengindeks data sebagai vektor numerik agar item serupa dapat ditemukan cepat), dan lapisan penyajian yang disetel untuk latensi dan throughput. Memperbaiki infrastruktur ini adalah pembeda antara AI yang berskala secara berkelanjutan dan AI yang diam-diam menghabiskan anggaran sambil kurang memberikan.

Bagi tim besar, masalah intinya adalah skala, kelangkaan, dan biaya. Akselerator terbatas dan mahal, jadi penjadwalan dan pemanfaatan sangat penting. GPU menganggur adalah uang yang terbakar, dan inferensi yang di-batch buruk melipatgandakan biaya per permintaan. Aplikasi padat pengambilan butuh [basis data vektor](https://en.wikipedia.org/wiki/Vector_database) yang tetap cepat saat tumbuh. Aplikasi AI generatif butuh versioning prompt, pipeline evaluasi, dan observabilitas (kadang disebut LLMOps) untuk beroperasi dengan aman dan membaik seiring waktu. Tanpa infrastruktur bersama dan disiplin operasional, setiap tim berjuang dalam pertempuran yang sama dan biaya melonjak.

Organisasi pemerintah dan teregulasi menambah persyaratan seputar kedaulatan data, keamanan, dan pengeluaran yang dapat diprediksi. Mereka mungkin butuh deployment on-premises atau cloud berdaulat agar data sensitif dan model tak pernah meninggalkan batas terkendali. Mereka harus memperkirakan dan membenarkan pengeluaran infrastruktur, serta memenuhi standar keamanan dan ketersediaan. Keputusan infrastruktur AI dalam pengaturan ini membawa konsekuensi multitahun, jadi buatlah dengan pengadaan, keamanan, dan jalur keluar dalam pikiran.

## Prinsip utama

- Perlakukan komputasi akselerator sebagai sumber daya langka dan mahal untuk dijadwalkan dan dimanfaatkan, bukan ditimbun.
- Optimalkan biaya per unit kerja berguna, bukan kapasitas mentah.
- Sesuaikan ukuran model dan perangkat keras dengan tugas; opsi terbesar jarang yang paling hemat biaya.
- Rancang penyajian untuk latensi dan throughput dengan batching dan caching sebagai teknik kelas satu.
- Jadikan sistem AI dapat diamati: lacak biaya, latensi, kualitas, dan galat secara terus-menerus.
- Versikan dan evaluasi prompt dan model dengan ketelitian yang sama seperti kode.
- Rencanakan portabilitas dan hindari lock-in dalam pilihan infrastruktur dan penyajian.

## Rekomendasi

### Rencanakan dan kendalikan komputasi akselerator

Perkirakan permintaan untuk pelatihan dan inferensi secara terpisah, karena keduanya berbentuk berbeda. Pelatihan bersifat berlonjak dan dapat dijadwalkan; inferensi berkelanjutan dan peka latensi. Pakai penjadwal dan kuota untuk berbagi GPU dan TPU langka antartim, memprioritaskan beban kerja, dan mendorong pemanfaatan naik. Ukur pemanfaatan dan perlakukan keanggurannya yang kronis sebagai masalah untuk diperbaiki. Padukan kapasitas reservasi untuk beban dasar dengan kapasitas on-demand atau spot untuk lonjakan guna mengendalikan biaya. Pertimbangkan apakah akselerator lebih murah atau lebih kecil, atau inferensi CPU untuk model ringan, akan memadai. Pilih antara cloud, on-premises, dan hibrida berdasarkan biaya pada skala Anda, kebutuhan kedaulatan data, dan pola lonjakan, serta jaga jalur keluar.

### Bangun infrastruktur pengambilan: embedding dan basis data vektor

Untuk aplikasi retrieval-augmented, dirikan infrastruktur untuk menghasilkan [embedding](https://en.wikipedia.org/wiki/Word_embedding) (representasi vektor numerik yang menempatkan item serupa berdekatan) dan menyimpannya dalam basis data vektor yang mendukung [pencarian tetangga terdekat aproksimasi](https://en.wikipedia.org/wiki/Nearest_neighbor_search) (menemukan vektor paling mirip tanpa membandingkan setiap vektor secara menyeluruh) pada skala Anda. Rencanakan tiga hal: biaya dan latensi pembuatan embedding, kesegaran indeks seiring dokumen berubah, dan beban operasional menjaga indeks tetap konsisten. Evaluasi apakah basis data vektor khusus, ekstensi berkemampuan vektor dari basis data yang ada, atau layanan terkelola paling cocok dengan skala dan toleransi lock-in Anda. Pantau latensi dan recall pengambilan, karena kualitas pengambilan langsung menentukan kualitas aplikasi.

### Optimalkan penyajian model: batching, caching, dan latensi

Penyajian adalah tempat biaya inferensi dan pengalaman pengguna diputuskan. Pakai **batching** untuk memproses beberapa permintaan bersama dan menaikkan throughput akselerator, menyeimbangkan ukuran batch terhadap latensi. Pakai **caching** secara agresif: cache permintaan identik atau mirip secara semantik, cache embedding, dan manfaatkan caching prompt atau prefiks di mana platform mendukungnya untuk menghindari menghitung ulang konteks bersama. Tetapkan target latensi jelas, dan ukur latensi ekor, bukan hanya rata-rata. Rutekan permintaan ke model berukuran tepat: model kecil untuk kasus mudah, yang lebih besar hanya bila perlu. Skalakan otomatis penyajian sesuai permintaan, dan uji beban sebelum peluncuran agar Anda tahu kapasitas dan kurva biaya Anda.

### Praktikkan LLMOps: versioning prompt, pipeline evaluasi, dan observabilitas

Perlakukan prompt sebagai artefak berversi dalam kontrol sumber, dengan tinjauan dan kemampuan rollback. Bangun pipeline evaluasi yang menjalankan rangkaian uji offline secara otomatis setiap kali prompt atau model berubah, agar Anda menangkap regresi sebelum rilis. Instrumentasi produksi secara komprehensif: catat masukan, keluaran, latensi, pemakaian token, biaya, dan galat, dengan pengambilan sampel dan pengaman privasi. Lacak sinyal kualitas dan umpan balik pengguna secara online. Observabilitas ini memungkinkan Anda menangkap degradasi, mengendalikan biaya, men-debug kegagalan, dan memperbaiki sistem dengan aman: tulang punggung operasional AI generatif di produksi.

### Kelola biaya tanpa henti dan dapat diamati

Atribusikan pengeluaran AI ke tim dan kasus penggunaan agar biaya terlihat dan dimiliki. Tetapkan anggaran dan peringatan, pantau biaya per permintaan dan per hasil, dan tinjau pendorong biaya terbesar secara rutin. Tarik tuas yang Anda miliki: penyesuaian ukuran model, caching, batching, pemangkasan prompt dan konteks, dan memilih deployment termurah yang memenuhi persyaratan. Biaya AI dapat berskala dengan pemakaian secara mengejutkan, jadi observabilitas biaya berkelanjutan esensial untuk menghindari kejutan tidak menyenangkan.

## Trade-off: kelebihan dan kekurangan

| Keputusan | Opsi A | Opsi B | Trade-off |
|---|---|---|---|
| Lokasi komputasi | Cloud | On-premises | Elastisitas dan biaya awal rendah versus kendali, kedaulatan, dan ekonomi kondisi-mapan |
| Kapasitas | Reservasi | On-demand/spot | Biaya dapat diprediksi versus fleksibilitas dan risiko gangguan |
| Ukuran batch | Batch besar | Batch kecil | Throughput dan biaya versus latensi |
| Ukuran model | Model besar | Model kecil | Kualitas versus biaya dan kecepatan |
| Penyimpanan vektor | Basis data khusus | Ekstensi basis data yang ada | Kinerja pada skala besar versus kesederhanaan dan lebih sedikit sistem |
| Caching | Agresif | Minimal | Biaya dan latensi lebih rendah versus kesegaran dan kompleksitas |

Trade-off dominannya adalah biaya versus latensi dan kualitas. Batching, caching, dan model lebih kecil memangkas biaya tetapi dapat menambah latensi atau menurunkan kualitas. Keseimbangan yang tepat bergantung pada toleransi aplikasi Anda. On-premises versus cloud menukar kendali dan ekonomi kondisi-mapan terhadap elastisitas dan komitmen rendah, keputusan yang sangat dibentuk oleh kebutuhan kedaulatan data dan skala.

## Pertanyaan untuk didiskusikan dengan tim Anda

1. **Berapa biaya per hasil berguna kita hari ini, dan tuas mana yang paling menggeser angkanya?** Kapasitas mentah dan rata-rata per permintaan menyembunyikan angka yang penting: berapa biaya mengantarkan satu unit nilai nyata, dan bagaimana itu berskala dengan pemakaian. Bagi tim besar, kesenjangan antara deployment yang dioptimalkan dan tidak sering beberapa kali lipat dalam pengeluaran, jadi pertanyaan ini mengubah kekhawatiran samar tentang tagihan menjadi daftar perbaikan berperingkat. Bawa atribusi biaya saat ini menurut tim dan kasus penggunaan, tren per permintaan dan per hasil, dan pendorong biaya terbesar. Diskusikan tuas menurut urutan imbalan: penyesuaian ukuran model, caching (termasuk caching prefiks dan semantik), batching, dan pemangkasan prompt atau konteks. Di pemerintah, tambahkan tekanan untuk memperkirakan dan membenarkan pengeluaran multitahun. Jawabannya harus menetapkan setiap pendorong biaya teratas pada pemilik dan tuas, bukan angkat bahu.

2. **Jika penyedia inferensi kita saat ini menggandakan harga atau mati besok, secepat apa kita dapat berpindah?** Lock-in senyap mudah dibangun dan menyakitkan dilepaskan, dan tumpukan penyajian adalah tempat ia bersembunyi paling dalam. Bagi enterprise dan terutama pemerintah, portabilitas adalah persyaratan pengadaan dan kesinambungan, bukan kemewahan. Bawa arsitektur Anda: apakah model duduk di balik antarmuka internal, apakah prompt dan rangkaian evaluasi portabel, dan seberapa banyak perilaku penyajian khusus-penyedia yang Anda andalkan. Sinyal yang diawasi adalah apakah ada yang pernah menjalankan rangkaian evaluasi Anda terhadap penyedia kedua atau target deployment kedua. Jika berpindah akan memakan berbulan-bulan dan menulis ulang jalur inti, perlakukan itu sebagai cacat desain untuk ditangani sekarang, karena opsi berdaulat dan on-premises bisa menjadi wajib dengan pemberitahuan singkat.

3. **Berapa pemanfaatan akselerator kita saat ini, dan berapa banyak GPU menganggur dan inferensi tanpa batch yang membakar anggaran?** Akselerator langka dan mahal, jadi keanggurannya yang kronis dan penyajian per permintaan diam-diam menguras anggaran yang dapat mendanai kemampuan lebih. Bagi organisasi besar yang berbagi GPU antartim, pertanyaan ini mengungkap apakah penjadwalan, kuota, dan prioritas benar-benar menjaga pemanfaatan tinggi atau perangkat keras timbunan yang kurang dipakai adalah norma. Bawa angka pemanfaatan nyata, postur batching dan caching Anda, dan pengukuran latensi ekor, bukan hanya rata-rata, karena pengguna merasakan ekor yang lambat. Diskusikan apakah permintaan pelatihan dan inferensi diperkirakan terpisah, mengingat bentuknya berbeda, dan apakah model lebih kecil atau inferensi CPU akan memadai untuk kasus ringan. Jawabannya harus menunjuk kapasitas menganggur spesifik untuk direklamasi dan permintaan spesifik untuk di-batch atau dirutekan ke model berukuran tepat.

4. **Ketika perubahan prompt atau model dikirim, apa yang menghentikan regresi kualitas atau biaya senyap mencapai pengguna?** Tumpukan penyajian dapat tampak sehat pada latensi dan uptime sementara jawaban yang dikembalikannya diam-diam memburuk atau prompt baru menggandakan pemakaian token per permintaan. Bagi tim besar di mana banyak kelompok mengedit prompt dan menukar model secara independen, perubahan tanpa gerbang adalah insiden produksi yang menunggu terjadi, dan radius ledakannya tumbuh dengan setiap tim di platform bersama. Bawa cakupan evaluasi Anda: prompt dan model mana yang punya rangkaian uji offline, apakah rangkaian itu berjalan otomatis pada setiap perubahan, ambang kualitas dan biaya apa yang menggerbangi rilis, dan seberapa cepat Anda dapat rollback. Diskusikan apakah prompt tinggal dalam kontrol sumber dengan tinjauan, atau apakah seseorang masih dapat mengedit prompt sistem langsung dengan tangan. Dalam pengaturan enterprise dan pemerintah, kaitkan setiap perubahan dengan jejak audit dan penyetuju bernama, karena regulator yang bertanya "siapa yang mengubah ini dan apa yang Anda uji" membutuhkan jawaban yang tercatat, bukan diingat.

5. **Bagaimana kita memutuskan antara deployment cloud, on-premises, dan berdaulat, dan sudahkah kita menghargai ekonomi kondisi-mapan yang sebenarnya alih-alih percontohan?** Pilihan lokasi komputasi menetapkan kurva biaya, postur kedaulatan data, dan opsi keluar Anda selama bertahun-tahun, namun sering dibuat berdasarkan tagihan cloud percontohan yang tak mirip produksi pada skala besar. Bagi organisasi besar, kapasitas cloud elastis murah untuk dimulai dan dapat menjadi baris tunggal terbesar begitu inferensi berjalan terus-menerus, sementara on-premises menukar komitmen rendah dengan kendali dan ekonomi kondisi-mapan. Bawa perkiraan volume pelatihan dan inferensi, titik impas di mana perangkat keras reservasi atau milik sendiri mengalahkan on-demand, kendala residensi data dan keamanan Anda, dan pola lonjakan yang mendukung hibrida. Dalam pengaturan pemerintah dan teregulasi, timbang persyaratan cloud berdaulat atau on-premises yang bisa menjadi wajib dengan pemberitahuan singkat, dan pastikan arsitektur menjaga model di balik antarmuka internal agar perpindahan paksa tidak menulis ulang jalur inti.

6. **Apakah kita benar-benar memiliki pengeluaran AI kita, dan dapatkah setiap tim melihat dan mempertanggungjawabkan biaya yang didorongnya?** Biaya AI berskala dengan pemakaian dengan cara yang mengejutkan orang, dan tanpa atribusi tagihan mendarat sebagai satu angka buram yang tak dirasakan tim mana pun bertanggung jawab memperkecilnya. Dalam organisasi besar, biaya yang tak dimiliki siapa pun adalah biaya yang tak dioptimalkan siapa pun, jadi pertanyaannya apakah pengeluaran ditandai ke tim dan kasus penggunaan dengan anggaran, peringatan, dan tren per hasil, atau baru ditemukan ketika keuangan mengeskalasi. Bawa model atribusi biaya Anda, pendorong terbesar menurut tim, dan tuas yang dikendalikan tiap pemilik: penyesuaian ukuran, caching, batching, dan pemangkasan konteks. Untuk anggaran enterprise dan pemerintah, tambahkan disiplin memperkirakan dan membenarkan pengeluaran infrastruktur multitahun, karena badan publik yang tak dapat menjelaskan tagihan komputasinya baris demi baris akan kesulitan membelanya dalam tinjauan.

## Lensa sektor

**Startup.** Jangan memiliki infrastruktur yang dapat Anda hindari. Panggil API inferensi ter-hosting, rutekan permintaan mudah ke model kecil murah dan sisihkan yang lebih besar untuk kasus sulit, dan cache secara agresif agar prompt berulang tak berbiaya. Pakai basis data vektor terkelola alih-alih mengoperasikan sendiri, simpan prompt di git dengan skrip evaluasi singkat sebelum setiap perubahan, dan catat biaya per permintaan agar tagihan liar muncul sebelum melukai. Sumber daya Anda yang paling langka adalah perhatian rekayasa, jadi beli kemudahan operasi dan jaga berpindah tetap murah.

**Bisnis kecil.** Tanpa tim platform, perlakukan penyajian, pengambilan, dan observabilitas sebagai hal yang Anda beli di dalam perkakas yang sudah Anda pakai, bukan sistem yang Anda isi stafnya. Pilih inferensi terkelola dan pencarian vektor terkelola dengan harga transparan dan dapat diprediksi, dan tetapkan batas pengeluaran keras serta peringatan penagihan sejak hari pertama. Bingkai keputusan sebagai beli versus bangun dengan jujur: mengoperasikan GPU atau indeks vektor jarang terbayar pada volume Anda, dan model kecil di balik API ter-hosting biasanya memenuhi kebutuhan dengan sebagian kecil upaya.

**Enterprise.** Masalahnya platform jalan-beraspal bersama lintas banyak tim: akselerator terpool dengan penjadwal, kuota, dan prioritas untuk mendorong pemanfaatan naik, batching dan caching standar, router penyesuai ukuran, dan biaya diatribusikan ke setiap tim dan kasus penggunaan. Gerbangi perubahan prompt dan model dengan rangkaian evaluasi otomatis, bakukan lapisan antarmuka agar penyedia dan target deployment tetap dapat ditukar, dan kelola biaya per hasil sebagai metrik kelas satu alih-alih tiap kelompok menciptakan ulang infrastruktur mahal dan kurang dipakai.

**Pemerintah.** Kedaulatan data, keamanan, dan pengeluaran yang dapat diprediksi membentuk setiap pilihan. Pilih deployment on-premises atau cloud berdaulat agar data sensitif dan model tetap di dalam batas terkendali, jadwalkan GPU langka antardepartemen dengan kuota yang dapat Anda benarkan dalam pengadaan, dan perkirakan kapasitas untuk membela pengeluaran multitahun baris demi baris. Versikan dan evaluasi prompt dan model dengan jejak audit tercatat, jaga observabilitas komprehensif atas biaya dan kualitas, dan tahan model di balik antarmuka internal agar perpindahan paksa ke penyedia baru atau platform berdaulat tidak membuat Anda terdampar.

## Contoh

**Startup.** Startup kecil yang menjalankan fitur penulisan AI menjaga tagihannya waras tanpa memiliki GPU. Ia memanggil API inferensi ter-hosting, merutekan permintaan mudah ke model kecil lebih murah dan menyimpan yang lebih besar untuk kasus sulit, dan men-cache jawaban atas prompt berulang. Ia menyimpan prompt di git dengan skrip evaluasi singkat yang berjalan sebelum setiap perubahan, memakai basis data vektor terkelola untuk pengambilan agar tak perlu mengoperasikannya, dan mencatat biaya per permintaan agar para pendiri dapat melihat pengeluaran naik sebelum menjadi kejutan.

**Enterprise.** Sebuah perusahaan media yang menjalankan fitur LLM berlalu lintas tinggi memangkas biaya inferensi secara substansial. Ia merutekan permintaan mudah ke model kecil dan menyisihkan model lebih besar untuk yang sulit. Ia men-cache respons atas kueri berulang dan mengaktifkan caching prefiks untuk prompt sistem bersamanya. Ia menjalankan GPU melalui penjadwal bersama untuk menjaga pemanfaatan tinggi, memversikan semua prompt di git dengan rangkaian evaluasi otomatis yang menggerbangi perubahan, dan menginstrumentasi biaya per permintaan agar setiap tim produk memiliki pengeluarannya.

**Pemerintah.** Sebuah lembaga nasional dengan aturan kedaulatan data ketat men-deploy sistem AI-nya on-premises agar data sensitif dan model tak pernah meninggalkan lingkungan terkendalinya. Ia menjadwalkan GPU langka antardepartemen dengan kuota dan prioritas, memperkirakan kapasitas untuk membenarkan pengadaan multitahun, dan membangun platform pencarian vektor untuk pengambilan atas dokumen resmi. Prompt dan model diversikan dan dievaluasi sebelum rilis. Observabilitas komprehensif melacak biaya dan kualitas, dan arsitektur menjaga model di balik antarmuka internal untuk mempertahankan jalur keluar dan menghindari lock-in.

## Kasus bisnis: motivasi, ROI, dan TCO

Motivasi untuk infrastruktur AI yang disiplin lugas. AI pada skala besar mahal, dan kesenjangan antara deployment yang dioptimalkan dan tidak sering beberapa kali lipat dalam pengeluaran. ROI datang dari pemanfaatan akselerator lebih tinggi, biaya per permintaan lebih rendah lewat batching dan caching, model berukuran tepat, dan menghindari provisioning berlebih. Pipeline observabilitas dan evaluasi terbayar dengan mencegah insiden mahal dan memungkinkan iterasi aman.

TCO mencakup komputasi akselerator (baris terbesar untuk banyak beban kerja), penyimpanan vektor, infrastruktur penyajian, jaringan, dan staf platform dan operasi untuk menjalankannya. Timbang ini terhadap biaya tidak berinvestasi: tagihan inferensi liar, latensi buruk yang merusak adopsi, dan ketidakmampuan berskala. Untuk pemerintah, tambahkan biaya gagal memenuhi persyaratan kedaulatan atau keamanan. Ajukan kasus kepada pimpinan dengan menunjukkan tren biaya-per-hasil dan platform jalan-beraspal yang memungkinkan banyak tim men-deploy AI secara efisien, alih-alih tiap tim membangun infrastruktur mahal dan kurang dipakai.

## Anti-pola dan jebakan

- **Akselerator menganggur.** Mendedikasikan GPU langka kepada tim yang membiarkannya kurang dimanfaatkan.
- **Tanpa batching atau caching.** Menyajikan setiap permintaan secara individual dan menghitung ulang konteks bersama.
- **Model terbesar sebagai bawaan.** Memakai model mahal di mana yang kecil sudah cukup.
- **Buta biaya.** Tanpa atribusi, anggaran, atau visibilitas biaya per permintaan sampai tagihan tiba.
- **Prompt tanpa versi.** Mengubah prompt di produksi tanpa versioning atau gerbang evaluasi.
- **Mengabaikan latensi ekor.** Mengoptimalkan latensi rata-rata sementara pengguna menderita ekor lambat.
- **Lock-in senyap.** Membangun dalam di atas tumpukan penyajian satu penyedia tanpa portabilitas.

## Model kematangan

1. **Memulai.** Alokasi GPU ad hoc bereaksi terhadap siapa pun yang paling keras meminta, tanpa batching atau caching, tanpa visibilitas biaya sampai tagihan tiba, prompt diedit langsung dan tanpa versi, pemantauan minimal.
2. **Mengembangkan.** Sebagian tim mengadopsi penjadwalan bersama, caching, dan prompt terkontrol versi, tetapi praktik tidak konsisten di seluruh organisasi: satu kelompok melakukan batching dan evaluasi sementara yang lain masih menyajikan setiap permintaan secara individual dan mengubah prompt dengan tangan.
3. **Membakukan.** Platform jalan-beraspal terdokumentasi ditegakkan di seluruh organisasi: penjadwalan bersama dengan kuota dan prioritas, batching, caching, dan penyesuaian ukuran standar, infrastruktur vektor untuk pengambilan, pipeline evaluasi otomatis yang menggerbangi setiap perubahan prompt atau model, dan atribusi biaya ke tim dan kasus penggunaan.
4. **Mengelola.** Platform diukur dan dikendalikan terhadap garis dasar: pemanfaatan akselerator, biaya per hasil berguna, latensi ekor, recall pengambilan, dan regresi kualitas per perubahan dilacak dengan peringatan dan ambang, biaya dimiliki setiap tim, dan go atau no-go atas perubahan diputuskan atas bukti alih-alih intuisi.
5. **Mengorkestrasi.** Infrastruktur terus membaik dan beradaptasi: perutean, batching, dan penskalaan menyetel diri terhadap sinyal biaya dan kualitas langsung, kapasitas diseimbangkan ulang antartim dan antara target cloud, on-premises, dan berdaulat seiring permintaan dan kendala bergeser, portabilitas dilatih, dan perencanaan infrastruktur terintegrasi dengan produk, keamanan, dan pengadaan.

## Gagasan untuk didiskusikan

- Bagaimana Anda mendorong pemanfaatan akselerator naik tanpa mengorbankan beban kerja prioritas?
- Di mana keseimbangan batching dan caching yang tepat untuk persyaratan latensi Anda?
- Kapan deployment on-premises atau berdaulat membenarkan biayanya dibanding cloud?
- Bagaimana Anda mengatribusikan dan mengendalikan pengeluaran AI di banyak tim?
- Apa yang harus menggerbangi perubahan prompt atau model mencapai produksi?
- Bagaimana Anda menjaga infrastruktur penyajian cukup portabel untuk berpindah penyedia?

## Poin-poin utama

- Akselerator langka dan mahal; jadwalkan, bagikan, dan manfaatkan dengan sengaja.
- Batching, caching, dan penyesuaian ukuran model adalah tuas utama untuk biaya dan latensi.
- Aplikasi pengambilan membutuhkan infrastruktur embedding dan pencarian vektor yang dioperasikan dengan baik.
- LLMOps (versioning prompt, pipeline evaluasi, dan observabilitas) adalah tulang punggung operasional AI generatif.
- Kelola biaya secara dapat diamati dan jaga portabilitas untuk menghindari lock-in.

## Referensi dan bacaan lanjutan

- Chip Huyen, *Designing Machine Learning Systems*.
- Google, *Site Reliability Engineering* (Beyer, Jones, Petoff, Murphy, editor).
- Jared Kaplan et al., *Scaling Laws for Neural Language Models*.
- Reza Yazdani Aminabadi et al., *DeepSpeed Inference: Enabling Efficient Inference of Transformer Models at Unprecedented Scale*.
- Woosuk Kwon et al., *Efficient Memory Management for Large Language Model Serving with PagedAttention* (vLLM).
- Andriy Burkov, *Machine Learning Engineering*.
