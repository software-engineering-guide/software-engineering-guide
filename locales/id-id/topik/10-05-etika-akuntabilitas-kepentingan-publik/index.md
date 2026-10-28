# 10.5 Etika, akuntabilitas, dan kepentingan publik

## Tinjauan dan motivasi

Perangkat lunak bukan lagi perkakas netral yang duduk di belakang keputusan manusia. Ia makin *menjadi* keputusan itu. Ia memutuskan siapa yang mendapat pinjaman, résumé mana yang dilihat perekrut, berapa lama klaim tunjangan memakan waktu, apakah bendera penipuan membekukan rekening, dan informasi apa yang mencapai jutaan orang. Ketika perangkat lunak membuat atau membentuk keputusan yang memengaruhi hak, uang, keselamatan, dan martabat orang, insinyur dan organisasi yang membangunnya memikul tanggung jawab melampaui kebenaran dan kinerja. Bab ini membahas tanggung jawab itu: [etika profesi](https://en.wikipedia.org/wiki/Professional_ethics), akuntabilitas atas apa yang dilakukan sistem, [aksesibilitas](https://en.wikipedia.org/wiki/Web_accessibility) dan kesetaraan sebagai kewajiban alih-alih fitur, transparansi algoritmik, [keberlanjutan](https://en.wikipedia.org/wiki/Sustainability), dan kewajiban melayani orang dengan keadilan dan martabat.

Bagi organisasi besar, skala dan kekuasaan menaikkan taruhan. Sistem enterprise atau pemerintah tidak memengaruhi satu orang. Ia memengaruhi jutaan. Satu pilihan desain (set pelatihan bias, formulir tak dapat diakses, penolakan otomatis yang buram) berulang di setiap dari mereka. Pemerintah memikul kewajiban lebih tinggi, karena sistemnya tidak opsional. Warga tak dapat memilih pesaing untuk otoritas pajak atau lembaga tunjangannya. Monopoli negara atas layanan tertentu berarti sistem yang dibangun buruk dapat menolak orang dari hak yang tak punya cara lain untuk dijalankan. Dengan jangkauan itu datang kewajiban setimpal untuk adil, transparan, dan akuntabel.

Etika dalam perangkat lunak sering diperlakukan sebagai topik lunak yang ditempelkan di akhir, atau diserahkan ke daftar periksa kepatuhan hukum. Bab ini berargumen sebaliknya. Pertimbangan etis adalah persyaratan rekayasa. Akuntabilitas harus dirancang masuk, bukan ditegaskan sesudahnya. Dan melayani orang dengan martabat adalah kewajiban moral sekaligus, seiring waktu, fondasi kepercayaan yang menjadi sandaran organisasi besar.

## Prinsip utama

- **Perangkat lunak membuat keputusan, jadi pembuatnya memikul tanggung jawab.** Anda akuntabel atas apa yang dilakukan sistem Anda kepada orang, bukan sekadar apakah ia memenuhi spesifikasi.
- **Aksesibilitas dan kesetaraan adalah kewajiban, bukan peningkatan.** Mengecualikan orang adalah cacat, dan sering kegagalan hukum dan moral.
- **Keputusan otomatis berdampak membutuhkan akuntabilitas.** Orang yang terdampak keputusan otomatis berhak atas penjelasan, pemulihan, dan tinjauan manusia.
- **Transparansi bawaan, kerahasiaan pengecualian.** Terutama di sektor publik, orang berhak memahami bagaimana keputusan tentang mereka dibuat.
- **Keadilan harus diperiksa, bukan diasumsikan.** Sistem mewarisi dan memperkuat bias dalam data dan desainnya kecuali Anda sengaja memeriksa.
- **Martabat adalah persyaratan desain.** Perlakukan setiap pengguna, termasuk yang rentan dan tak tipikal, sebagai pribadi yang layak dihormati.
- **Keberlanjutan dan dampak sosial dihitung.** Energi, sumber daya, dan efek masyarakat perangkat lunak adalah bagian dari biaya sejatinya.

## Rekomendasi

### Adopsi dan jalani etika profesi

Dasarkan organisasi pada kode perilaku profesional yang diakui, dan jadikan nyata alih-alih dekoratif. Insinyur harus memahami bahwa mereka punya kewajiban kepada publik, bukan sekadar kepada majikan. "Saya hanya mengikuti spesifikasi" bukan pembelaan ketika sistem merugikan orang. Ciptakan saluran sejati untuk mengangkat kekhawatiran etis: cara untuk mengatakan "kita tidak seharusnya membangun ini, atau tidak membangunnya dengan cara ini" yang tidak membutuhkan keberanian yang mengakhiri karier. Beri tim kosakata dan kedudukan untuk menimbang konsekuensi. Dukung itu dengan kepemimpinan yang memperlakukan keberatan etis sebagai sinyal berharga, bukan penghalang. Pelatihan etika membantu hanya jika organisasi terlihat bertindak atas apa yang diajarkannya.

### Perlakukan aksesibilitas dan kesetaraan sebagai kewajiban

Bangun untuk seluruh rentang kemampuan dan keadaan manusia sejak awal. Memasang aksesibilitas belakangan jauh lebih mahal dan biasanya lebih buruk. Ikuti standar aksesibilitas yang mapan (seperti [WCAG](https://en.wikipedia.org/wiki/Web_Content_Accessibility_Guidelines), Web Content Accessibility Guidelines), dan di banyak yurisdiksi penuhi persyaratan hukum yang mewajibkannya untuk layanan publik. Uji dengan [teknologi bantu](https://en.wikipedia.org/wiki/Assistive_technology) dan, di atas segalanya, dengan pengguna nyata yang punya disabilitas. Perluas kesetaraan melampaui disabilitas ke seluruh populasi yang Anda layani: orang dengan bandwidth rendah, dengan perangkat tua, dengan [literasi digital](https://en.wikipedia.org/wiki/Digital_literacy) terbatas, dalam bahasa minoritas, dan dalam keadaan hidup yang sulit. Untuk layanan yang tak dapat dihindari orang (terutama layanan pemerintah), merancang hanya untuk pengguna yang percaya diri, terhubung, dan tipikal adalah kegagalan melayani, bukan bawaan yang masuk akal.

### Bangun akuntabilitas algoritmik dan transparansi publik

Untuk sistem apa pun yang membuat atau secara material membentuk keputusan berdampak tentang orang, rancang akuntabilitas masuk. Jaga manusia secara bermakna [dalam lingkaran](https://en.wikipedia.org/wiki/Human-in-the-loop) untuk keputusan berisiko tinggi, alih-alih menunduk buta pada keluaran otomatis. Mampu menjelaskan, dalam istilah yang dapat dipahami orang terdampak, mengapa keputusan dibuat. Sediakan jalur nyata untuk menantangnya dan menjangkau manusia. Uji sistem untuk [bias](https://en.wikipedia.org/wiki/Algorithmic_bias) dan [dampak disparitas](https://en.wikipedia.org/wiki/Disparate_impact) di kelompok yang dilindungi dan rentan, sebelum dan selama deployment, dan pantau drift seiring waktu. Di sektor publik, terbitkan cara kerja sistem algoritmik (tujuan, data, dan logikanya pada tingkat yang sesuai) lewat mekanisme seperti register algoritma, agar warga dan badan pengawas dapat menelitinya. Dokumentasikan penggunaan yang dimaksudkan dan keterbatasan yang diketahui, agar sistem tidak diterapkan di tempat yang seharusnya tidak.

### Rancang untuk keadilan, martabat, dan pemulihan

Periksa sistem Anda untuk cara-cara ia dapat memperlakukan orang tidak adil atau tanpa martabat. Teliti data pelatihan dan aturan untuk bias tertanam. Ingat bahwa sistem yang dioptimalkan murni untuk efisiensi dapat kejam: filter penipuan yang disetel untuk meminimalkan negatif palsu dapat membekukan rekening ribuan orang tak bersalah, masing-masing pribadi nyata dalam kesulitan. Rancang untuk kasus kegagalan dari sudut pandang orang terdampak. Apa yang terjadi ketika sistem salah? Seberapa mudah mereka mendapat manusia, penjelasan, dan pemulihan? Tangani [data pribadi](https://en.wikipedia.org/wiki/Personal_data) dengan hormat dan menahan diri: kumpulkan hanya yang dibutuhkan, dan jujurlah tentang pemakaiannya. Perlakukan galat, penundaan, dan penolakan bukan sebagai kasus tepi tetapi sebagai momen di mana martabat paling berisiko.

### Perhitungkan keberlanjutan dan tanggung jawab sosial

Akui bahwa perangkat lunak punya biaya fisik dan sosial. Pusat data, proses pelatihan, dan sistem tidak efisien mengonsumsi energi nyata. Efisiensi adalah kebajikan lingkungan sekaligus finansial. Pertimbangkan efek lebih luas dari apa yang Anda bangun (pada tenaga kerja, pada wacana publik, pada kelompok rentan) dan bersedialah menolak atau membentuk ulang kerja yang kerugiannya melampaui manfaatnya. Untuk organisasi besar yang sistemnya membentuk masyarakat pada skala besar, tanggung jawab sosial bukan filantropi di samping bisnis. Ia bagian dari membangun secara bertanggung jawab, dan makin menjadi soal regulasi dan ekspektasi publik.

## Trade-off: kelebihan dan kekurangan

| Ketegangan | Satu sisi | Sisi lain |
|---|---|---|
| Otomasi vs. penilaian manusia | Skala, konsistensi, kecepatan, biaya lebih rendah | Akuntabilitas, nuansa, belas kasih, pemulihan |
| Transparansi vs. perlindungan | Pengawasan publik, kepercayaan, supervisi | Risiko akal-akalan, keamanan, privasi data |
| Investasi aksesibilitas vs. kecepatan | Melayani semua orang; kepatuhan hukum dan moral | Pengiriman awal lebih lambat; lebih banyak upaya desain |
| Efisiensi vs. keadilan | Hasil dioptimalkan; biaya lebih rendah | Risiko kekejaman terhadap individu di ekor |
| Personalisasi kaya data vs. privasi | Layanan lebih baik; pengalaman disesuaikan | Risiko pengawasan; kekhawatiran martabat dan persetujuan |
| Kecepatan inovasi vs. kehati-hatian | Nilai lebih cepat; keunggulan kompetitif | Kerugian tak diperiksa dikerahkan pada skala besar |

Trade-off tersulit adalah skala versus keadilan individual. Otomasi memberi konsistensi dan efisiensi atas jutaan. Tetapi galatnya juga dikirim pada skala besar, dan sistem yang dioptimalkan untuk agregat dapat diam-diam brutal terhadap individu di ekornya. Jawabannya bukan meninggalkan otomasi. Melainkan merancang untuk kasus kegagalan individual: jaga manusia dalam lingkaran di mana taruhan tinggi, jamin penjelasan dan pemulihan, dan ukur efek sistem pada yang paling kurang terlayani, bukan hanya rata-rata. Transparansi juga membawa ketegangan sejati, karena keterbukaan penuh dapat memungkinkan akal-akalan dan memaparkan data pribadi. Tetapi dalam layanan publik jawabannya condong kuat ke pengungkapan secara bawaan, hanya mengecualikan apa yang benar-benar harus dilindungi, alih-alih memperlakukan keburaman sebagai bawaan yang aman.

## Pertanyaan untuk didiskusikan dengan tim Anda

1. **Sistem Anda yang mana membuat atau secara material membentuk keputusan berdampak tentang orang, dan apakah masing-masing menawarkan penjelasan, tinjauan manusia, dan pemulihan hari ini?** Perangkat lunak makin menjadi keputusan itu: siapa mendapat pinjaman, résumé mana yang dilihat, apakah rekening dibekukan, berapa lama klaim memakan waktu. Untuk setiap sistem semacam itu, orang terdampak berhak atas penjelasan yang dapat mereka pahami, jalur nyata untuk menantangnya, dan manusia yang dapat mengintervensi, dan pada skala enterprise atau pemerintah satu cacat desain berulang di jutaan. Bawa bukti: inventarisasi keputusan otomatis berdampak Anda dan, untuk masing-masing, periksa apakah orang yang diperlakukan salah benar-benar dapat menjangkau manusia dan mendapat alasan bahasa sederhana. Di mana jawabannya tidak, itu cacat untuk diperbaiki, bukan fitur untuk ditambah nanti. Untuk layanan yang tak dapat dihindari orang, terutama layanan pemerintah, ini kewajiban alih-alih kesopanan.

2. **Apakah Anda memperlakukan aksesibilitas sebagai persyaratan pemblokir peluncuran yang diuji dengan pengguna disabilitas nyata, dan siapa yang saat ini Anda kecewakan?** Aksesibilitas dan kesetaraan adalah kewajiban, dan mengecualikan orang adalah cacat, sering kegagalan hukum dan moral, namun memasang aksesibilitas belakangan secara andal lebih lambat, lebih mahal, dan lebih buruk daripada merancangnya masuk sejak layar pertama. Ikuti WCAG, dan lewati pemeriksaan otomatis dengan menguji bersama teknologi bantu dan pengguna nyata yang punya disabilitas, plus orang dengan bandwidth rendah, perangkat tua, bahasa minoritas, dan literasi digital terbatas. Bawa bukti: jalankan alur terpenting Anda dengan pembaca layar dan pada koneksi yang dibatasi, dan lihat di mana ia patah. Jawabannya harus memutuskan apakah aksesibilitas adalah gerbang yang memblokir rilis atau butir backlog yang tak pernah naik, dan untuk layanan yang tak dapat dihindari orang, hanya gerbang yang dapat dipertahankan. Merancang hanya untuk pengguna yang percaya diri, terhubung, dan tipikal adalah kegagalan melayani.

3. **Apa proses tetap Anda untuk menguji sistem berdampak atas bias dan dampak disparitas, sebelum dan selama deployment?** Sistem mewarisi dan memperkuat bias dalam data dan desainnya kecuali Anda sengaja memeriksa, dan mengasumsikan keadilan karena tak ada yang berniat tidak adil adalah bias karena pengabaian. Filter penipuan yang disetel murni untuk meminimalkan negatif palsu dapat membekukan ribuan rekening tak bersalah, masing-masing pribadi nyata dalam kesulitan, sehingga efisiensi yang dioptimalkan tanpa memperhatikan keadilan dapat diam-diam kejam. Bawa bukti: untuk setiap model yang memengaruhi orang, tunjukkan uji dampak disparitas di kelompok dilindungi dan rentan, data terdokumentasi dan keterbatasan yang diketahui, dan pemantauan drift yang menguji ulang seiring populasi berubah. Jawabannya harus menjadikan pengujian bias rutin dan berkelanjutan alih-alih kotak centang pra-peluncuran sekali jalan, dan harus mengubah target optimasi Anda untuk menimbang kerugian pada individu, bukan hanya akurasi agregat. Rancang untuk kasus kegagalan dari sudut pandang orang terdampak.

4. **Ketika insinyur yakin Anda seharusnya tidak membangun sesuatu, atau tidak membangunnya dengan cara ini, apa yang sebenarnya terjadi pada keberatan itu?** Etika menjadi nyata hanya ketika "kita tidak seharusnya mengirim ini" adalah kalimat yang dapat diucapkan seseorang tanpa mengakhiri kariernya, dan pada skala besar orang yang paling dekat dengan kerugian sering yang paling junior di ruangan. Tekanan yang bersaing adalah pengiriman: keberatan yang diangkat memperlambat peta jalan, dan pimpinan di bawah tenggat dapat memperlakukannya sebagai penghalang alih-alih sinyal berharga. Bawa bukti: namai saluran persis yang akan dipakai insinyur, hitung berapa kekhawatiran diangkat tahun lalu, dan telusuri apa yang berubah akibatnya, karena saluran yang tak pernah menghentikan atau membentuk ulang kerja adalah dekoratif. Untuk badan enterprise atau pemerintah, kaitkan saluran dengan pemilik bernama dan tinjauan terdokumentasi, karena keberatan yang tak wajib didengar siapa pun adalah yang tak akan berani diangkat siapa pun, dan kerugian lalu muncul pertama sebagai skandal publik.

5. **Apakah Anda tahu biaya lingkungan dan sosial dari apa yang Anda jalankan, dan maukah Anda membentuk ulang atau menolak kerja yang kerugiannya melampaui manfaatnya?** Perangkat lunak punya biaya fisik dan sosial: pusat data, proses pelatihan, dan sistem tidak efisien mengonsumsi energi nyata, dan efek tingkat kedua pada tenaga kerja, wacana publik, dan kelompok rentan adalah bagian dari biaya sejati sistem. Ketegangannya adalah mengukur dan memangkas biaya ini bersaing dengan kecepatan fitur, dan menolak kerja berbahaya melepas pendapatan yang ada yang akuntabel atasnya. Bawa bukti: jejak energi atau komputasi sistem terbesar Anda, pembacaan jujur siapa yang menanggung efek hilir, dan setidaknya satu kasus konkret di mana Anda membentuk ulang atau menolak kerja atas dasar ini. Pada skala enterprise atau pemerintah, di mana sistem Anda membentuk masyarakat, perlakukan ini sebagai bagian dari membangun secara bertanggung jawab dan makin menjadi soal regulasi dan ekspektasi publik, bukan filantropi yang ditempelkan di samping bisnis.

6. **Seberapa banyak orang luar sebenarnya dapat mempelajari bagaimana sistem berdampak Anda memutuskan, dan apakah pengungkapan bawaan Anda atau pengecualian Anda?** Transparansi adalah tempat kepercayaan publik diperoleh atau hilang, karena orang berhak memahami bagaimana keputusan tentang mereka dibuat, dan di sektor publik hak itu sering undang-undang. Tekanan tandingan sejati adalah keterbukaan penuh dapat memungkinkan akal-akalan dan memaparkan data pribadi, sehingga pertanyaan nyata adalah di mana menarik garis alih-alih apakah mengungkap sama sekali. Bawa bukti: untuk setiap sistem berdampak, tunjukkan apa yang Anda terbitkan (tujuan, data, dan logika pada tingkat yang sesuai), apa yang Anda tahan beserta alasan spesifiknya, dan apakah deskripsi bahasa sederhana berdampingan dengan yang teknis. Untuk badan pemerintah, timbang mekanisme seperti register algoritma terhadap pengecualian sempit yang dapat dipertahankan, dan periksa bahwa pengungkapan Anda benar-benar menjelaskan alih-alih memberi tahu secara teknis sambil tak memberi tahu orang terdampak apa pun.

## Lensa sektor

**Startup.** Dengan segelintir orang dan sedikit runway, Anda tak dapat mengisi staf dewan etika, jadi tanamkan kebiasaan murah berdaya ungkit tinggi ke produk itu sendiri: alasan bahasa sederhana pada setiap penolakan otomatis, jalur satu-klik untuk menjangkau manusia, dan formulir yang dapat diakses sejak layar pertama karena memasangnya belakangan lebih lambat dan lebih buruk. Pilih satu tempat di mana perangkat lunak Anda membuat keputusan berdampak tentang seseorang dan benarkan penjelasan serta pemulihan di sana sebelum Anda menskalakan kerugiannya. Memperlakukan keadilan dan martabat sebagai persyaratan peluncuran, bukan poles belakangan, berbiaya kecil sekarang dan menghindari reputasi yang tak sanggup Anda hilangkan di awal.

**Bisnis kecil.** Anda mungkin tidak punya spesialis aksesibilitas atau keadilan dan anggaran ketat, jadi bersandarlah pada etika yang dibangun dalam perkakas yang Anda beli: pilih vendor yang memenuhi WCAG, mendokumentasikan bagaimana fitur otomatisnya memutuskan, dan membiarkan Anda menjaga manusia dalam lingkaran. Bingkai kewajiban Anda sendiri sebagai pertanyaan kebersihan data dan martabat, mengetahui data pribadi apa yang Anda pegang, mengumpulkan hanya yang Anda butuhkan, dan memastikan jawaban otomatis yang salah tidak mendamparkan pelanggan tanpa cara menjangkau Anda. Minta pemasok menunjukkan postur aksesibilitas dan biasnya sebelum Anda menandatangani, alih-alih menemukan celahnya setelah keluhan.

**Enterprise.** Pada skala besar masalahnya tata kelola lintas banyak tim: standar bersama tentang apa yang dihitung sebagai keputusan berdampak, gerbang pengujian aksesibilitas dan bias yang konsisten, dan jejak audit yang membuktikan penjelasan, tinjauan manusia, dan pemulihan ada di mana seharusnya. Dirikan tinjauan etis yang memblokir rilis alih-alih pelatihan yang tak mengubah apa pun, anggarkan kerja aksesibilitas dan dampak disparitas secara eksplisit, dan pantau model ter-deploy untuk drift agar keadilan berkelanjutan alih-alih kotak centang sekali jalan. Perlakukan satu cacat desain sebagai berulang di jutaan, karena pada jangkauan Anda memang begitu.

**Pemerintah.** Aturan pengadaan, kewajiban transparansi, dan akuntabilitas publik membentuk setiap pilihan, dan warga tak dapat menghindari layanan Anda dengan pergi ke pesaing. Terbitkan cara kerja sistem berdampak lewat mekanisme seperti register algoritma, wajibkan vendor lewat kontrak mengungkap praktik data dan keterbatasan yang diketahui, dan bangun setiap layanan publik hingga standar aksesibilitas yang diuji dengan pengguna disabilitas, koneksi bandwidth rendah, dan penutur bahasa minoritas. Jamin hak atas tinjauan manusia dan penjelasan bahasa sederhana pada setiap keputusan otomatis berdampak, dan jaga penentuan akhir yang harus berada pada pejabat akuntabel di luar otomasi penuh sepenuhnya.

## Contoh

**Startup.** Startup fintech tiga orang yang membangun fitur pinjaman otomatis memutuskan keadilan dan martabat adalah persyaratan, bukan poles belakangan. Sebelum peluncuran mereka menguji model untuk dampak disparitas di kelompok yang dapat mereka ukur, menuliskan data yang dipakainya dan di mana ia tak boleh dipercaya, dan memastikan setiap pemohon yang ditolak mendapat alasan bahasa sederhana dan jalur satu-klik untuk menjangkau pendiri manusia. Mereka membangun alur pendaftaran hingga standar aksesibilitas sejak layar pertama, karena memasangnya belakangan akan lebih lambat dan lebih buruk, dan mereka menambah kanal override cepat agar rekening yang salah dibekukan dapat dibuka dalam menit alih-alih meninggalkan orang nyata terdampar.

**Enterprise.** Sebuah bank yang men-deploy keputusan kredit otomatis memperlakukan keadilan sebagai persyaratan rekayasa. Sebelum peluncuran, ia menguji model untuk dampak disparitas di kelompok dilindungi, mendokumentasikan data dan keterbatasannya, dan membangun fasilitas penjelasan, sehingga setiap pemohon yang ditolak mendapat alasan yang dapat dipahami dan jalur jelas ke tinjauan manusia. Proses pemantauan mengawasi drift dan menguji ulang bias seiring populasi berubah. Ketika sistem deteksi penipuan mulai membekukan banyak rekening sah, bank menambah kanal tinjauan manusia cepat dan mengubah target optimasinya untuk menimbang kerugian pelanggan. Ia memperlakukan penderitaan pelanggan yang salah ditandai sebagai biaya nyata, bukan statistik yang dapat diterima.

**Pemerintah.** Sebuah pemerintah kota menerbitkan register algoritma. Ia mendaftar sistem otomatis yang dipakai kota dalam layanan publik, dan mendeskripsikan tujuan setiap sistem, data yang diandalkan, dan bagaimana keputusan dapat dipersoalkan. Layanan digital kota dibangun hingga standar aksesibilitas dan diuji dengan pengguna disabilitas, koneksi bandwidth rendah, dan penutur bahasa minoritas, dengan prinsip bahwa layanan yang tak dapat dihindari orang harus berfungsi bagi semua. Setiap keputusan otomatis berdampak membawa hak atas tinjauan manusia dan penjelasan bahasa sederhana, sehingga warga mempertahankan martabat dan pemulihan ketika perangkat lunak negara memutuskan sesuatu tentang hidup mereka.

## Kasus bisnis: motivasi, ROI, dan TCO

Kasus bisnis untuk etika dan akuntabilitas bertumpu pada kepercayaan, risiko, dan jangkauan. Kepercayaan adalah aset tahan lama. Organisasi yang sistemnya memperlakukan orang secara adil dan transparan memperoleh keyakinan yang membuat orang bersedia memakainya, dan lembaga publik khususnya bergantung pada legitimasi yang dapat dihancurkan satu sistem tidak adil berprofil tinggi. Risiko adalah pendorong jangka dekat. Sistem bias, tak dapat diakses, atau buram makin membawa penalti regulasi, litigasi, dan kerusakan reputasi yang dapat melampaui biaya membangun secara bertanggung jawab. Jangkauan memperkuat keduanya. Pada skala enterprise atau pemerintah, satu kegagalan etis berulang di jutaan dan menjadi berita utama.

Biaya adopsi nyata. Kerja aksesibilitas, pengujian bias, mekanisme penjelasan dan pemulihan, tinjauan manusia-dalam-lingkaran, dan waktu desain untuk mempertimbangkan konsekuensi semuanya menambah upaya, terutama di awal. Biaya *tidak* mengadopsi lebih besar dan makin tak opsional: liabilitas diskriminasi, pengecualian bagian besar populasi yang wajib Anda layani, biaya memasang aksesibilitas dan akuntabilitas belakangan setelah peluncuran, dan erosi kepercayaan yang, begitu hilang, mahal dan lambat dibangun kembali. Ketika Anda mengajukan kasus kepada pimpinan, bingkai etika sebagai manajemen risiko dan pembangunan kepercayaan, bukan altruisme. Catat lingkungan regulasi yang mengetat seputar [akuntabilitas algoritmik](https://en.wikipedia.org/wiki/Algorithmic_accountability) dan aksesibilitas. Tekankan total biaya kepemilikan: membangun secara bertanggung jawab sejak awal jauh lebih murah daripada memperbaiki sistem yang sudah merugikan orang pada skala besar. Untuk lembaga publik, tambahkan argumen paling sederhana: melayani warga secara adil adalah misi, bukan kendala atasnya.

## Anti-pola dan jebakan

- **Etika sebagai kotak centang.** Tinjauan atau pelatihan sekali jalan yang tak mengubah apa pun tentang bagaimana sistem sebenarnya dibangun.
- **Memasang aksesibilitas belakangan.** Memperlakukan aksesibilitas sebagai tambahan akhir, menghasilkan hasil lebih buruk dan lebih mahal daripada merancangnya masuk.
- **Algoritma tak akuntabel.** Keputusan otomatis berdampak tanpa penjelasan, tanpa tinjauan manusia, dan tanpa jalur untuk menantang.
- **Mengoptimalkan hingga kejam.** Menyetel murni untuk efisiensi agregat sampai sistem diam-diam brutal terhadap orang di ekornya.
- **Bias karena pengabaian.** Mengasumsikan sistem adil karena tak ada yang berniat tidak adil, tanpa pernah mengujinya.
- **"Komputer bilang tidak."** Staf garis depan dan pengguna tanpa kemampuan mengesampingkan atau mempertanyakan keputusan otomatis yang mereka lihat salah.
- **Merancang untuk pengguna percaya diri.** Membangun untuk pengguna tipikal, terhubung, dan melek dan mengecualikan semua orang lain, tak dapat dipertahankan untuk layanan yang tak dapat dihindari orang.
- **Teater transparansi.** Menerbitkan pengungkapan yang tak tertembus yang secara teknis menginformasikan tetapi tak benar-benar menjelaskan apa pun.

## Model kematangan

**Tingkat 1: Memulai.** Etika tak ditangani atau murni reaktif setelah skandal. Aksesibilitas diabaikan atau minimal. Keputusan otomatis buram, tanpa penjelasan dan tanpa pemulihan. Bias tak pernah diuji, dan keberlanjutan serta dampak sosial tak dipertimbangkan.

**Tingkat 2: Mengembangkan.** Kode perilaku ada dan sebagian standar aksesibilitas diikuti, sering terlambat. Keputusan otomatis berprofil tinggi mendapat sebagian pengawasan manusia, tetapi sebagian besar tidak. Bias diperiksa sesekali, kekhawatiran dapat diangkat lewat proses lemah, dan praktik sangat bervariasi dari satu tim ke tim lain.

**Tingkat 3: Membakukan.** Tinjauan etis adalah bagian terdokumentasi dari proses pengembangan dan ditegakkan di seluruh organisasi. Aksesibilitas dirancang masuk dan diuji dengan pengguna nyata. Keputusan otomatis berdampak membawa penjelasan, tinjauan manusia, dan pemulihan secara bawaan. Pengujian bias dan pemantauan drift rutin, sistem sektor publik menerbitkan cara kerjanya, dan keberlanjutan diukur menurut standar umum.

**Tingkat 4: Mengelola.** Organisasi mengukur dan mengendalikan postur etisnya dengan data terhadap garis dasar: skor kesesuaian aksesibilitas, metrik dampak disparitas yang dilacak di kelompok dilindungi seiring waktu, tingkat pemulihan dan waktu-ke-manusia untuk keputusan yang dipersoalkan, pangsa sistem berdampak yang membawa dokumentasi terbitan, dan jejak energi atau komputasi sistem utama. Metrik menggerbangi rilis, pelanggaran ambang memicu investigasi, dan pimpinan meninjau angka pada irama tetap alih-alih mengasumsikan praktik diikuti.

**Tingkat 5: Mengorkestrasi.** Tanggung jawab tertanam dalam cara organisasi membangun dan beradaptasi. Aksesibilitas dan kesetaraan adalah bawaan tak dapat ditawar yang diverifikasi untuk seluruh populasi yang dilayani, akuntabilitas algoritmik (transparansi, pengujian keadilan, pemulihan, pengawasan manusia) adalah standar dan dipantau terus-menerus, dan kekhawatiran etis dihargai sebagai sinyal yang membentuk ulang atau menghentikan kerja. Organisasi memperlakukan kepercayaan, keadilan, dan martabat sebagai inti misinya, mengintegrasikan etika dengan keputusan produk, risiko, dan pengadaan, dan menentukan ulang cakupan atau memensiunkan sistem seiring ekspektasi dan bukti berevolusi.

## Gagasan untuk didiskusikan

- Di mana garis antara keputusan yang boleh sepenuhnya diotomatisasi dan yang harus menjaga manusia secara bermakna dalam lingkaran?
- Seberapa banyak transparansi algoritmik cukup, dan bagaimana Anda mengungkap secara bermakna tanpa memungkinkan akal-akalan atau melanggar privasi?
- Siapa yang akuntabel ketika sistem otomatis merugikan seseorang: insinyur, manajer, organisasi, atau vendor?
- Bagaimana Anda membuat mengangkat keberatan etis benar-benar aman alih-alih membatasi karier?
- Kewajiban apa yang dimiliki organisasi kepada pengguna yang tidak dirancangnya, dan seberapa jauh kesetaraan harus meluas?
- Bagaimana biaya lingkungan komputasi harus memengaruhi keputusan arsitektur dan produk?

## Poin-poin utama

- Ketika perangkat lunak membuat keputusan berdampak tentang orang, pembuatnya bertanggung jawab atas apa yang dilakukannya, bukan sekadar apakah ia memenuhi spesifikasi.
- Aksesibilitas dan kesetaraan adalah kewajiban dan cacat ketika absen, bukan peningkatan opsional, terutama untuk layanan yang tak dapat dihindari orang.
- Keputusan otomatis berdampak membutuhkan penjelasan, tinjauan manusia, pemulihan, dan pengujian bias berkelanjutan; rancang akuntabilitas masuk alih-alih menegaskannya sesudahnya.
- Efisiensi yang dioptimalkan tanpa memperhatikan keadilan dapat diam-diam kejam; rancang untuk kasus kegagalan individual, bukan hanya agregat.
- Di sektor publik, transparansi tentang cara kerja sistem algoritmik harus menjadi bawaan, dengan kerahasiaan sebagai pengecualian sempit.
- Kasus bisnisnya kepercayaan dan risiko: membangun secara bertanggung jawab sejak awal jauh lebih murah daripada memperbaiki kerugian pada skala besar, dan bagi lembaga publik, keadilan adalah misinya.

## Referensi dan bacaan lanjutan

- ACM/IEEE-CS, *Software Engineering Code of Ethics and Professional Practice*
- ACM, *Code of Ethics and Professional Conduct*
- Cathy O'Neil, *Weapons of Maths Destruction*
- Virginia Eubanks, *Automating Inequality*
- Safiya Umoja Noble, *Algorithms of Oppression*
- Ruha Benjamin, *Race After Technology*
- Batya Friedman dan David G. Hendry, *Value Sensitive Design*
- World Wide Web Consortium (W3C), *Web Content Accessibility Guidelines (WCAG)*
- NIST, *AI Risk Management Framework*
- OECD, *Principles on Artificial Intelligence*
- European Union, *General Data Protection Regulation (GDPR)* dan *AI Act*
- UK Government, *Data Ethics Framework* dan *Algorithmic Transparency Recording Standard*
