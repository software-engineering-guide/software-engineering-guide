# 2.3 API dan desain antarmuka

## Tinjauan dan motivasi

[API](https://en.wikipedia.org/wiki/API) (application programming interface) adalah kontrak tempat satu potong perangkat lunak menawarkan kemampuan kepada yang lain. Di sinilah tim, sistem, dan organisasi bertemu, dan ia adalah hal paling tahan lama dan paling mahal untuk dikerjakan dengan keliru. Anda dapat merefaktor tanda tangan fungsi internal dengan bebas. API yang diterbitkan berbeda: ia janji kepada konsumen yang mungkin tidak pernah Anda temui, dan melanggarnya merusak mereka. Ketika organisasi memecah [monolit](https://en.wikipedia.org/wiki/Monolithic_application) menjadi layanan dan membuka kemampuan kepada mitra dan publik, API menjadi permukaan produk utama dan risiko integrasi utama.

Bagi tim besar, API adalah yang memungkinkan orang bekerja secara independen. Antarmuka yang dirancang baik memungkinkan Anda mengubah bagian dalam tanpa berkoordinasi dengan setiap konsumen, yang merupakan inti dari batas layanan. Antarmuka yang buruk membocorkan detail internal, memaksa deployment serentak, dan mengubah sekumpulan layanan menjadi distributed monolith: layanan yang terpecah namun begitu berpasangan sehingga harus dibangun dan di-deploy bersama. Desain API Anda langsung menentukan seberapa independen tim Anda dapat bergerak.

Dalam konteks enterprise dan pemerintah, API juga membawa kewajiban kepatuhan, keamanan, dan umur panjang. API sektor publik mungkin diwajibkan mengikuti [standar terbuka](https://en.wikipedia.org/wiki/Open_standard), tetap stabil selama bertahun-tahun, dan melayani pengembang eksternal yang tidak dapat Anda koordinasikan. API enterprise menopang integrasi mitra dengan tingkat layanan kontraktual. Semua ini menaikkan standar disiplin pembuatan versi, [kompatibilitas mundur](https://en.wikipedia.org/wiki/Backward_compatibility), tata kelola, dan pengalaman pengembang.

## Prinsip utama

- Rancang kontrak lebih dulu. Antarmuka adalah keputusan produk yang disengaja, bukan hasil sampingan implementasi.
- Optimalkan untuk pengalaman konsumen, bukan kenyamanan Anda sendiri.
- Perlakukan kompatibilitas mundur sebagai janji. Perubahan yang merusak membutuhkan versi baru dan jalur migrasi.
- Buat hal yang mudah menjadi benar: bawaan yang masuk akal, galat yang dapat diprediksi, konvensi yang konsisten.
- Rancang untuk kegagalan. [Idempotensi](https://en.wikipedia.org/wiki/Idempotence) (permintaan berulang berefek sama dengan satu permintaan), retry, paginasi, dan [pembatasan laju](https://en.wikipedia.org/wiki/Rate_limiting) adalah perhatian kelas satu, bukan renungan belakangan.
- Pilih gaya protokol agar sesuai dengan interaksi, bukan mode.
- Atur API sebagai produk, dengan pemilik, siklus hidup, dan dokumentasi.

## Rekomendasi

### Bekerja API-dulu dan digerakkan kontrak

Definisikan dan tinjau kontrak API, termasuk sumber daya, operasi, skema, dan semantik galatnya, sebelum Anda menulis implementasi. Gunakan spesifikasi yang dapat dibaca mesin, agar kontrak dapat menghasilkan dokumentasi, stub klien dan server, server tiruan, dan validasi. Dengan begitu konsumen dapat mulai berintegrasi terhadap tiruan selagi Anda membangun, dan kontrak menjadi sumber kebenaran tunggal yang diuji kedua pihak.

### Pilih gaya interaksi dengan sengaja

Pilih di antara [REST](https://en.wikipedia.org/wiki/REST) (representational state transfer), [GraphQL](https://en.wikipedia.org/wiki/GraphQL), [gRPC](https://en.wikipedia.org/wiki/GRPC), dan [pesan berbasis peristiwa](https://en.wikipedia.org/wiki/Event-driven_architecture) berdasarkan interaksinya, bukan preferensi pribadi. Gunakan REST untuk antarmuka berorientasi sumber daya, interoperabel luas, dan dapat di-cache. Gunakan GraphQL ketika klien beragam membutuhkan pembacaan fleksibel dan teragregasi atas graf yang kaya. Gunakan gRPC untuk panggilan berkinerja tinggi dan bertipe kuat antarlayanan internal. Gunakan pesan berbasis peristiwa untuk alur kerja asinkron dan terpisah serta untuk menyebarkan perubahan status. Banyak sistem besar memakai beberapa gaya sekaligus, masing-masing di tempat yang cocok.

### Beri versi dan nyatakan usang dengan disiplin

Adopsi strategi pembuatan versi yang eksplisit dan kebijakan penghentian yang diterbitkan: bagaimana Anda mengklasifikasikan perubahan, berapa lama Anda mendukung versi lama, dan bagaimana Anda memberi tahu konsumen. Tarik garis yang jelas antara perubahan yang kompatibel mundur (menambah bidang opsional, endpoint baru) dan perubahan yang merusak (menghapus atau mengganti nama bidang, mengubah tipe atau semantik). Jangan pernah mengalihfungsikan makna bidang yang ada. Beri konsumen jendela tumpang-tindih untuk bermigrasi, dan komunikasikan jadwal jauh-jauh hari.

### Buat semantik galat konsisten dan dapat dibaca mesin

Kembalikan galat yang terstruktur dan dapat diprediksi: kode yang stabil dan dapat dibaca mesin, pesan yang dapat dibaca manusia, dan konteks yang cukup untuk ditindaklanjuti, tanpa membocorkan hal internal yang sensitif. Gunakan semantik status yang sama di setiap endpoint, agar klien dapat menangani galat secara seragam. Dokumentasikan setiap galat yang mungkin dihadapi konsumen.

### Bangun idempotensi, paginasi, dan pembatasan laju

Buat operasi tulis aman untuk di-retry dengan mendukung kunci idempotensi, sehingga klien yang mencoba ulang setelah timeout tidak menagih dua kali atau membuat ganda. Paginasi setiap endpoint daftar sejak hari pertama, dan pilih paginasi berbasis kursor untuk set data besar atau yang berubah. Terapkan dan dokumentasikan batas laju, dan kembalikan keadaan batas saat ini kepada klien agar mereka dapat mundur dengan anggun.

### Atur API dan berinvestasi pada pengalaman pengembang

Perlakukan setiap API sebagai produk, dengan pemilik, siklus hidup, dan entri katalog. Dirikan tinjauan desain atau dewan standar API agar antarmuka tetap konsisten antartim. Berinvestasilah pada pengalaman pengembang: dokumen rujukan yang akurat, panduan mulai cepat, contoh, sandbox, dan changelog. Dalam ekosistem besar, portal atau katalog yang membuat API dapat ditemukan sangatlah penting.

## Trade-off: kelebihan dan kekurangan

| Gaya | Terbaik untuk | Kelebihan | Kekurangan |
|---|---|---|---|
| REST / HTTP | API publik berorientasi sumber daya | Ada di mana-mana, dapat di-cache, sederhana, interoperabel | Pengambilan berlebih/kurang; banyak round trip; kontrak longgar kecuali dispesifikasikan |
| GraphQL | Pembacaan fleksibel untuk beragam klien | Kueri ditentukan klien; satu endpoint; skema kuat | Kompleksitas caching dan pembatasan laju; risiko biaya kueri; kompleksitas server |
| gRPC | Panggilan internal berkinerja tinggi | Cepat, ringkas, bertipe kuat, streaming | Dukungan browser buruk; kurang terbaca manusia; perkakas lebih berat |
| Berbasis peristiwa | Alur kerja asinkron dan terpisah | Kopling longgar; skalabel; tangguh | Lebih sulit dinalar; konsistensi akhirnya; kompleksitas operasional |

Strategi pembuatan versi menukar stabilitas dengan pemeliharaan. Mendukung banyak versi lama melindungi konsumen, tetapi melipatgandakan kode yang harus Anda pelihara dan uji. Kompatibilitas mundur menukar kebebasan Anda sendiri dengan stabilitas konsumen, biasanya pertukaran yang tepat untuk API yang dipakai luas. Gambaran besarnya: biaya keputusan API yang buruk dibayar oleh setiap konsumen sepanjang umur antarmuka. Jadi layak membelanjakan lebih banyak upaya desain pada batas daripada hampir di mana pun.

## Pertanyaan untuk didiskusikan dengan tim Anda

1. **Bagaimana Anda mengklasifikasikan perubahan sebagai kompatibel mundur versus merusak, dan pemeriksaan otomatis apa yang menangkap kerusakan diam-diam sebelum dirilis?** Bab ini menarik garis tegas: menambah bidang opsional dan endpoint baru aman, sementara menghapus atau mengganti nama bidang, mengubah tipe, atau mengalihfungsikan makna bidang merusak konsumen. Pada tim besar orang yang membuat perubahan sering tidak dapat melihat setiap konsumen, sehingga penyesuaian "kecil" dapat diam-diam merusak mitra yang tidak pernah Anda ajak bicara. Bawa sinyal konkret ke rapat: apakah Anda menjalankan pemeriksaan kompatibilitas kontrak otomatis di CI terhadap spesifikasi yang diterbitkan, atau mengandalkan seseorang mengingat aturannya. Dalam konteks enterprise dan pemerintah, di mana perubahan yang merusak memaksa migrasi terkoordinasi di setiap mitra dan dapat membentang melewati pergantian vendor dan pemerintahan, biayanya berskala dengan jumlah konsumen. Putuskan aturan klasifikasi dan pasang gerbang kompatibilitas, agar perubahan yang tidak kompatibel menggagalkan build alih-alih sebuah integrasi.

2. **Primitif keandalan mana, kunci idempotensi, paginasi, dan pembatasan laju, yang wajib pada setiap endpoint baru sejak hari pertama?** Bab ini menegaskan ini adalah perhatian kelas satu, karena menambahkan kunci idempotensi ke endpoint penagihan yang sudah hidup atau menambah paginasi ke daftar yang sudah dirilis itu sendiri adalah perubahan yang merusak. Ekosistem besar memperkuat ini: endpoint yang berfungsi dalam pengujian runtuh di bawah volume data nyata, dan tulis yang tidak idempoten mengubah satu gangguan jaringan menjadi tagihan ganda. Bawa bukti endpoint saat ini mana yang tidak memilikinya dan apa yang akan dilakukan badai retry. Jadikan bawaan itu tak dapat ditawar untuk endpoint baru: paginasi kursor pada setiap daftar, kunci idempotensi pada setiap tulis, batas laju terdokumentasi yang mengembalikan keadaannya saat ini. Itu mengubah migrasi paksa di masa depan menjadi kebiasaan desain sekali jalan.

3. **Apakah Anda benar-benar merancang dan meninjau kontrak sebelum menulis implementasi, atau antarmuka bocor keluar dari kode?** Rekomendasi API-dulu meminta spesifikasi yang dapat dibaca mesin, ditinjau di muka, yang menghasilkan dokumen, stub, dan tiruan dan memungkinkan konsumen berintegrasi terhadap tiruan selagi Anda membangun. Ketika kontrak tertinggal di belakang implementasi, antarmuka mengekspos struktur basis data internal dan bergeser setiap kali implementasi berubah, anti-pola teratas dalam bab ini. Sinyal yang perlu diperiksa: dapatkah konsumen mulai berintegrasi terhadap tiruan Anda hari ini, atau harus menunggu backend yang berjalan. Untuk API publik dan mitra, di mana antarmuka adalah permukaan produk dan hal paling mahal untuk dikerjakan keliru, menghabiskan sehari untuk kontrak menghemat berminggu-minggu gejolak dukungan. Jadikan tinjauan kontrak langkah wajib sebelum implementasi dimulai.

4. **Ketika dua tim perlu mengekspos kemampuan yang sama, gaya interaksi mana yang menang, dan siapa yang berwenang berkata tidak pada protokol keempat?** Bab ini meminta Anda memilih REST, GraphQL, gRPC, atau pesan berbasis peristiwa menurut kecocokan interaksi, tetapi pada skala besar risiko sebenarnya adalah setiap tim memilih favoritnya sendiri dan konsumen menghadapi konvensi berbeda di setiap endpoint. Organisasi besar membayar fragmentasi itu dalam pustaka klien, gateway, pemantauan, dan beban kognitif pada setiap integrator yang kini mempelajari empat idiom, bukan satu. Bawa inventaris protokol yang sudah ada di produksi, interaksi yang dilayani masing-masing, dan konsumen yang melintasi lebih dari satu. Pertimbangan yang bersaing itu sejati: bawaan bersama mengurangi penyebaran, namun mandat yang kaku memaksa masalah berbentuk gRPC ke lubang berbentuk REST. Namai badan standar atau tinjauan arsitektur yang memiliki proses pengecualian, karena di properti enterprise dan pemerintah perbanyakan gaya menjadi pajak permanen atas integrasi dan masalah yang sulit dibalik begitu mitra bergantung pada masing-masing.

5. **Apa kebijakan penghentian terbitan kita, dan dapatkah kita membuktikan bahwa kita benar-benar menghormati jendela dukungan yang kita iklankan?** Bab ini memperlakukan pembuatan versi dan penghentian sebagai disiplin: kebijakan tertulis tentang berapa lama versi lama hidup, bagaimana konsumen diberi tahu, dan tumpang-tindih apa yang mereka dapatkan untuk bermigrasi. Janji yang tidak dapat Anda tegakkan lebih buruk daripada tidak ada, karena ekosistem besar mencakup konsumen yang tidak pernah Anda ajak bicara yang akan terus memanggil versi yang dipensiunkan sampai rusak di produksi. Bawa bukti ke diskusi: berapa versi hidup yang Anda pikul hari ini, penggunaan nyata pada masing-masing, apakah Anda dapat melihat konsumen mana yang masih memanggil endpoint yang dinyatakan usang, dan seberapa jauh sebelumnya sunset terakhir Anda diumumkan. Tekanan yang bersaing adalah biaya pemeliharaan terhadap stabilitas konsumen, dan keduanya nyata. Untuk mitra enterprise di bawah tingkat layanan kontraktual dan API sektor publik yang harus bertahan melewati pemerintahan dan pergantian vendor, jendela dukungan adalah komitmen yang mungkin hidup lebih lama daripada tim yang membuatnya, jadi putuskan siapa yang memilikinya dan bagaimana sunset dibuktikan aman sebelum terjadi.

6. **Bagaimana kita tahu pengalaman pengembang kita baik, atau kita mengasumsikannya karena API berfungsi untuk kita?** Bab ini membingkai setiap API sebagai produk yang adopsinya bergantung pada dokumen rujukan akurat, panduan mulai cepat, contoh, sandbox, changelog, dan katalog yang dapat ditemukan. Tim rutin mengira "API berfungsi" sebagai "API dapat digunakan", dan jurangnya muncul sebagai tiket dukungan, integrasi yang gagal, dan konsumen yang diam-diam menyerah. Bawa sinyal terukur, bukan opini: waktu-hingga-panggilan-berhasil-pertama bagi integrator baru, volume tiket dukungan per endpoint, seberapa basi dokumen terbitan terhadap kontrak hidup, dan apakah pendatang baru dapat melayani diri dari portal tanpa mengirim email ke tim Anda. Ketegangannya adalah dokumentasi dan portal memakan upaya nyata yang bersaing dengan merilis fitur, namun dalam ekosistem besar pengalaman pengembang yang buruk mendorong biaya integrasi ke ratusan konsumen sekaligus. Di pemerintahan, di mana API terbuka melayani pengembang eksternal yang tidak dapat Anda koordinasikan dan transparansi sering diwajibkan, antarmuka yang dapat digunakan, terdokumentasi baik, dan dapat ditemukan adalah bagian dari kewajiban akuntabilitas publik, bukan hal yang bagus untuk dimiliki.

## Lensa sektor

**Startup.** Dengan dua atau tiga insinyur dan tanpa waktu untuk upacara, jaga kontrak ringan tetapi nyata: satu spesifikasi yang dapat dibaca mesin yang dapat diintegrasikan pelanggan mitra desain pertama Anda selagi Anda membangun. Jangan dirikan API gateway, katalog, atau dewan tata kelola dulu, tetapi kunci dua kebiasaan yang menyakitkan untuk ditambah belakangan, kunci idempotensi pada tulis dan paginasi kursor pada daftar, karena menambalnya ke endpoint hidup adalah perubahan yang merusak yang tidak sanggup Anda tanggung. Pilih satu gaya interaksi, hampir selalu REST, agar Anda tidak membawa penyebaran protokol ke tahun pertama.

**Bisnis kecil.** Tanpa spesialis API khusus dan dengan anggaran ketat, bersandarlah pada perkakas yang menghasilkan dokumen, tiruan, dan stub klien dari spesifikasi agar generalis dapat memelihara antarmuka tanpa keahlian protokol mendalam. Timbang beli versus bangun dengan keras: gateway siap pakai atau platform manajemen API memberi Anda pembatasan laju, kunci, dan portal pengembang yang jika tidak harus Anda racik sendiri. Jaga permukaan kecil dan konvensi konsisten, karena setiap endpoint tambahan dan setiap format galat sekali pakai adalah sesuatu yang harus didukung tim tipis selamanya.

**Enterprise.** Di banyak tim otonom, masalah utamanya adalah konsistensi tanpa menjadi hambatan: panduan gaya bersama, tinjauan standar API, katalog yang membuat antarmuka dapat ditemukan, dan pemeriksaan kompatibilitas mundur otomatis di CI agar kerusakan diam-diam menggagalkan build alih-alih sebuah integrasi. Atur setiap API sebagai produk dengan pemilik bernama, siklus hidup, dan kebijakan penghentian terbitan, dan ukur adopsi, beban dukungan, dan frekuensi perubahan yang merusak agar portofolio tetap sehat. Bakukan gaya interaksi dan aturan pembuatan versi di seluruh organisasi, karena pada skala ini fragmentasi adalah bawaan yang mahal.

**Pemerintah.** Aturan pengadaan, mandat standar terbuka, dan akuntabilitas publik membentuk setiap pilihan. Terbitkan kontrak secara terbuka, ikuti standar terbuka yang diwajibkan, dan sediakan sandbox serta dokumen rujukan agar pengembang eksternal yang tidak dapat Anda koordinasikan dapat melayani diri. Perlakukan kompatibilitas mundur jangka panjang sebagai persyaratan kebijakan, karena integrasi harus bertahan melewati pemerintahan dan pergantian vendor, dan jadikan perubahan yang merusak jarang, sangat diatur, dan diumumkan jauh-jauh hari. Jaga API dan dokumentasinya cukup transparan untuk bertahan dari pengawasan publik dan audit, dan hindari format proprietari yang akan menjebak pemerintahan mendatang.

## Contoh

**Startup.** Sebuah startup tahap awal yang merilis API publik pertamanya menulis kontrak sebagai spesifikasi yang dapat dibaca mesin sebelum membuat kode, agar dua pelanggan mitra desainnya dapat berintegrasi terhadap tiruan selagi backend masih dibangun. Bahkan dengan hanya segelintir konsumen, ia menambahkan kunci idempotensi ke endpoint penagihan dan paginasi kursor ke setiap daftar, karena menambalnya setelah mitra bergantung pada API berarti perubahan yang merusak yang tidak sanggup ditanggung. Kontrak di muka memakan sehari dan menghemat berminggu-minggu bolak-balik dukungan.

**Enterprise.** Sebuah perusahaan pembayaran besar mengekspos API REST publik kepada ribuan pedagang. Setiap endpoint tulis menerima kunci idempotensi, sehingga retry jaringan tidak pernah membuat tagihan ganda. Setiap endpoint daftar memakai paginasi kursor. Galat membawa kode stabil yang terdokumentasi dalam rujukan publik. Kebijakan penghentian formal menjamin jendela dukungan panjang untuk versi apa pun, dengan pemberitahuan di muka dan panduan migrasi. Disiplin ini adalah keunggulan kompetitif: integrator percaya API tidak akan rusak di bawah mereka.

**Pemerintah.** Layanan digital nasional menerbitkan API terbuka untuk data warga, mengikuti standar terbuka yang diwajibkan dan proses desain API-dulu. Kontrak dispesifikasikan dan ditinjau sebelum pembangunan, diterbitkan dalam katalog API pemerintah pusat, dan disajikan dengan sandbox, sehingga pengembang pihak ketiga, yang tidak dapat dikoordinasikan satu per satu, dapat berintegrasi sendiri. Kompatibilitas mundur jangka panjang adalah persyaratan kebijakan, karena integrasi harus bertahan melewati pemerintahan dan pergantian vendor. Jadi perubahan yang merusak jarang dan sangat diatur.

## Kasus bisnis: motivasi, ROI, dan TCO

Desain API yang baik menurunkan biaya integrasi, yang sering merupakan biaya terbesar dalam menghubungkan sistem dan mengorientasi mitra. Dengan API yang jelas, stabil, dan terdokumentasi baik, konsumen berintegrasi dalam hitungan hari tanpa satu pun tiket dukungan. API yang buruk menghasilkan beban dukungan tak berujung, integrasi yang gagal, dan kerusakan reputasi. Ketika API sendiri adalah produknya, pengalaman pengembang langsung mendorong adopsi dan pendapatan.

Biaya tersembunyi terbesar adalah perubahan yang merusak. Setiap perubahan yang merusak memaksa migrasi terkoordinasi di semua konsumen, tim internal dan mitra eksternal sama-sama, dan total biayanya berskala dengan jumlah konsumen serta seberapa sulit mereka bergerak serentak. Berinvestasi di muka pada desain kontrak-dulu, kompatibilitas mundur, dan disiplin pembuatan versi menghindari peristiwa migrasi mahal seluruh organisasi ini. Ketika berbicara dengan pimpinan, bingkai kualitas API sebagai titik daya ungkit untuk otonomi tim, pertumbuhan ekosistem mitra, dan menghindari migrasi paksa yang mahal. Lacak waktu integrasi, volume tiket dukungan, dan frekuensi perubahan yang merusak sebagai bukti Anda.

## Anti-pola dan jebakan

- **API implementasi-dulu:** antarmuka membocorkan struktur basis data internal dan berubah setiap kali implementasi berubah.
- **Perubahan merusak yang diam-diam:** mengalihfungsikan bidang atau memperketat validasi tanpa kenaikan versi merusak konsumen secara tak terduga.
- **Antarmuka cerewet:** desain yang membutuhkan banyak round trip untuk satu operasi logis, merugikan kinerja dan kegunaan.
- **Konvensi tidak konsisten:** setiap endpoint menciptakan penamaan, format galat, dan paginasi sendiri, sehingga klien tidak dapat menggeneralisasi.
- **Tanpa paginasi atau pembatasan laju:** endpoint yang berfungsi dalam pengujian dan runtuh di bawah volume data atau beban nyata.
- **Tulis tidak idempoten:** retry menyebabkan duplikat; satu gangguan jaringan merusak data.
- **Perbanyakan versi:** terlalu banyak versi hidup tanpa penghentian, melipatgandakan pemeliharaan sampai tak terkelola.
- **Dokumen sebagai renungan belakangan:** rujukan tak terdokumentasi atau usang yang mendorong semua biaya integrasi ke konsumen.

## Model kematangan

- **Tingkat 1, Memulai:** API muncul dari implementasi sebagai hasil sampingan; tidak ada konvensi bersama; antarmuka membocorkan struktur basis data internal; perubahan yang merusak umum, tidak diumumkan, dan ditemukan saat integrasi konsumen gagal.
- **Tingkat 2, Mengembangkan:** Beberapa tim mengikuti konvensi REST dasar, memberi versi secara informal, dan menulis dokumen dengan tangan, tetapi praktik tidak konsisten antartim; idempotensi, paginasi, dan pembatasan laju muncul pada sebagian endpoint dan tidak pada yang lain; konsumen masih mempelajari keanehan setiap API kasus per kasus.
- **Tingkat 3, Membakukan:** Desain kontrak-dulu dengan spesifikasi yang dapat dibaca mesin didokumentasikan dan ditegakkan di seluruh organisasi; kebijakan penghentian terbitan, semantik galat konsisten, serta idempotensi, paginasi kursor, dan pembatasan laju wajib berlaku untuk setiap endpoint baru; panduan gaya bersama dan tinjauan standar API menjaga antarmuka konsisten antartim.
- **Tingkat 4, Mengelola:** Portofolio API diukur dan dikendalikan terhadap garis dasar: pemeriksaan kompatibilitas mundur otomatis menggerbangi setiap perubahan di CI, dan Anda melacak waktu-hingga-panggilan-berhasil-pertama, volume tiket dukungan per endpoint, frekuensi perubahan yang merusak, jumlah versi hidup, dan penggunaan per endpoint sehingga keputusan penghentian dan desain bertumpu pada bukti alih-alih opini. Setiap API adalah produk yang diatur dalam katalog dengan pemilik bernama, dan metrik memicu tindakan ketika layanan menyimpang dari targetnya.
- **Tingkat 5, Mengorkestrasi:** Strategi API terus diperbaiki dan terintegrasi di seluruh organisasi; katalog, gateway, aturan pembuatan versi, dan gerbang kompatibilitas bekerja sebagai satu sistem; organisasi secara rutin mengakhiri, mengkonsolidasi, dan mengubah cakupan antarmuka berdasarkan adopsi dan biaya terukur; standar gaya interaksi dan pembuatan versi beradaptasi seiring bergesernya ekosistem, mitra, dan teknologi, dan perubahan yang merusak jarang dan dikelola dengan baik.

## Gagasan untuk didiskusikan

- Bagaimana Anda memutuskan kapan API internal cukup stabil untuk diterbitkan secara eksternal?
- Berapa jendela dukungan yang tepat untuk versi yang dinyatakan usang dalam konteks Anda, dan siapa yang membayarnya?
- Di mana GraphQL atau gRPC harus menggantikan REST secara internal, dan di mana mereka akan menambah lebih banyak kompleksitas daripada nilai?
- Bagaimana Anda menegakkan konsistensi API di banyak tim otonom tanpa menjadi hambatan?
- Bagaimana API yang dapat dikonsumsi AI dan antarmuka alat agen harus mengubah konvensi desain Anda?
- Pemeriksaan otomatis apa yang dapat menangkap perubahan yang tidak kompatibel mundur sebelum dirilis?

## Poin-poin utama

- Rancang kontrak lebih dulu; API adalah produk dan janji berumur panjang.
- Kompatibilitas mundur melindungi konsumen; perubahan yang merusak membutuhkan versi baru dan jalur migrasi.
- Pilih REST, GraphQL, gRPC, atau peristiwa menurut kecocokan interaksi, bukan mode.
- Bangun idempotensi, paginasi, pembatasan laju, dan galat yang konsisten sejak hari pertama.
- Atur API sebagai produk dengan pemilik, katalog, dan pengalaman pengembang yang kuat.

## Referensi dan bacaan lanjutan

- Roy Fielding, *Architectural Styles and the Design of Network-based Software Architectures* (disertasi)
- Arnaud Lauret, *The Design of Web APIs*
- Mike Amundsen, *RESTful Web APIs* dan *Design and Build Great Web APIs*
- Sam Newman, *Building Microservices*
- OpenAPI Specification; JSON Schema (sebagai standar rujukan)
- Martin Kleppmann, *Designing Data-Intensive Applications*
