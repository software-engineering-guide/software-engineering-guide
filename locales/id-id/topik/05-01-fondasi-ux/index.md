# 5.1 Fondasi UX

## Tinjauan dan motivasi

[Pengalaman pengguna](https://en.wikipedia.org/wiki/User_experience) (UX) adalah tentang memahami orang (tujuan mereka, konteks mereka, kendala mereka) lalu membentuk perangkat lunak agar membantu mereka berhasil dengan gesekan sekecil mungkin. Ia bukan dekorasi yang Anda terapkan di akhir. Ia cara bekerja yang dimulai sebelum baris kode pertama dan berlanjut jauh setelah rilis. Bab ini membahas praktik riset, pemodelan, dan [design thinking](https://en.wikipedia.org/wiki/Design_thinking) yang memungkinkan organisasi besar membuat keputusan produk dari bukti alih-alih dari tebakan.

Bagi tim besar, UX sama-sama masalah koordinasi dan kerajinan. Ketika puluhan skuad merilis ke satu produk bersama, model mental yang tidak cocok, alur terduplikasi, dan terminologi yang bertentangan menumpuk menjadi keseluruhan membingungkan yang tak dimiliki satu tim pun. Fondasi UX bersama, dibangun dari persona umum, peta perjalanan yang disepakati, dan [arsitektur informasi](https://en.wikipedia.org/wiki/Information_architecture) terdokumentasi, memberi setiap tim peta pengguna yang sama, sehingga keputusan terpisah mereka berjumlah menjadi pengalaman koheren. Tanpanya, setiap tim mengoptimalkan secara lokal dan produk secara keseluruhan tidak masuk akal.

Enterprise dan pemerintah menaikkan taruhan. Perangkat lunak enterprise sering punya pengguna terikat yang tidak dapat pergi, sehingga UX buruk dibayar dalam pelatihan, tiket dukungan, galat, dan produktivitas hilang alih-alih orang pergi. Layanan pemerintah sering menjangkau seluruh publik, termasuk orang dalam krisis, pada perangkat lama, dengan kepercayaan diri digital rendah, atau tanpa penyedia alternatif. Di sini kualitas UX adalah soal kesetaraan dan kepercayaan sipil: aplikasi tunjangan yang dirancang buruk dapat menolak seseorang makanan atau tempat tinggal, bukan karena mereka tidak memenuhi syarat, tetapi karena mereka tidak dapat menyelesaikan formulir.

## Prinsip utama

- Rancang untuk orang nyata yang mengerjakan tugas nyata dalam kondisi nyata, bukan untuk pengguna ideal dengan koneksi cepat dan perhatian penuh.
- Riset mengurangi risiko. Waktu termurah menemukan asumsi yang salah adalah sebelum Anda membangun di atasnya.
- Pengguna tidak dapat dengan andal memberi tahu apa yang akan mereka lakukan; amati perilaku, bukan hanya preferensi yang dinyatakan.
- Fokus pada pekerjaan yang ingin diselesaikan pengguna, bukan fitur yang ingin Anda kirim.
- Konsistensi adalah fitur: model mental yang koheren di seluruh produk menurunkan beban kognitif.
- [Aksesibilitas](https://en.wikipedia.org/wiki/Accessibility) dan inklusi adalah bagian UX yang baik sejak awal, bukan putaran kepatuhan belakangan.
- Metode kualitatif dan kuantitatif menjawab pertanyaan berbeda; gunakan keduanya.
- Riset kecil dan sering mengalahkan studi berat yang jarang.

## Rekomendasi

### Dirikan riset berkelanjutan dan multimetode

Tuju praktik riset yang ringan tetapi berkelanjutan alih-alih studi besar sesekali. Wawancara mengungkap motivasi dan model mental. [Uji kegunaan](https://en.wikipedia.org/wiki/Usability_testing) mengungkap di mana desain patah; lima sampai delapan peserta per putaran memunculkan sebagian besar isu parah. Survei mengukur sikap pada skala besar tetapi tidak dapat menjelaskan "mengapa." Analitik dan instrumentasi menunjukkan apa yang benar-benar dilakukan orang di seluruh populasi. Padukan metode kualitatif (mengapa) dengan kuantitatif (berapa banyak), agar temuan sekaligus dijelaskan dan diukur. Dan simpan repositori riset, agar wawasan tetap dapat dicari dan dipakai ulang lintas tim alih-alih hilang di slide satu skuad.

### Modelkan pengguna dengan persona, peta perjalanan, dan jobs-to-be-done

Bangun himpunan kecil persona berbasis bukti yang menangkap tujuan, konteks, dan kendala, bukan karikatur demografis. Bingkai kebutuhan sebagai jobs-to-be-done, hasil mendasar yang ingin dicapai pengguna alih-alih fitur ("ketika saya kehilangan pekerjaan, saya ingin cepat memahami dukungan apa yang saya layak terima, agar saya bisa terus membayar sewa"). Ini menjaga fokus pada hasil alih-alih fitur. Peta perjalanan memetakan seluruh pengalaman lintas kanal dan seiring waktu, mengungkap celah dan serah terima yang tak diungkap satu layar pun. Untuk layanan dengan operasi panggung belakang berat (pusat panggilan, petugas kasus, pemenuhan pesanan), pakai [service blueprint](https://en.wikipedia.org/wiki/Service_blueprint) untuk menghubungkan pengalaman panggung depan dengan sistem dan staf di baliknya.

### Rancang arsitektur informasi dengan sengaja

Arsitektur informasi (IA) adalah bagaimana konten, fitur, dan navigasi distrukturkan dan dilabeli. Pakai [card sorting](https://en.wikipedia.org/wiki/Card_sorting) dan tree testing untuk menurunkan struktur itu dari model mental pengguna alih-alih dari bagan organisasi Anda. Kegagalan umum di organisasi besar adalah mengekspos batas departemen internal sebagai navigasi tingkat atas. Tetapkan kosakata terkendali agar konsep yang sama punya nama yang sama di mana-mana. [Desain interaksi](https://en.wikipedia.org/wiki/Interaction_design) lalu mendefinisikan perilaku saat-ke-saat: keadaan, umpan balik, pemulihan galat, dan alur antarlangkah.

### Terapkan design thinking secara pragmatis

Model berlian ganda (menyebar lalu menyempit untuk mendefinisikan masalah yang tepat, lalu menyebar dan menyempit untuk merancang solusi yang tepat) adalah bingkai yang berguna. Perlakukan sebagai pola pikir, namun, bukan proses berpintu yang kaku. Dalam praktik, jalankan putaran ketat: bingkai hipotesis, sketsa, uji dengan segelintir pengguna, dan belajar dalam hitungan hari. Simpan penemuan yang lebih berat untuk masalah yang benar-benar baru atau berisiko tinggi. Dan waspadai "teater inovasi," di mana lokakarya menghasilkan sticky note tetapi tak ada perubahan yang dikirim.

### Integrasikan UX ke pengiriman

Tanamkan desainer dan peneliti dalam tim pengiriman alih-alih menjalankan "departemen UX" terpisah yang menyerahkan spesifikasi melewati tembok. Jadikan temuan riset masukan tetap bagi prioritisasi. Taruh gerbang kualitas UX, seperti tolok ukur kegunaan dan pemeriksaan aksesibilitas, dalam definisi selesai. Dan lacak metrik hasil (keberhasilan tugas, waktu pada tugas, tingkat galat, kepuasan) tepat di samping metrik pengiriman Anda.

## Trade-off: kelebihan dan kekurangan

| Pendekatan | Kelebihan | Kekurangan |
|---|---|---|
| Riset penemuan berkelanjutan | Menangkap masalah lebih awal, membangun pemahaman bersama | Biaya berkelanjutan, butuh jalur perekrutan dan staf terampil |
| Riset berat di muka | Wawasan dalam sebelum investasi besar | Lambat, dapat menunda pembelajaran yang hanya diungkap pengiriman |
| Keputusan hanya-analitik | Berskala, objektif, murah setelah diinstrumentasi | Menjelaskan apa tetapi bukan mengapa; buta terhadap non-pengguna dan kasus tepi |
| Persona dan peta perjalanan | Menyelaraskan banyak tim pada satu model pengguna | Menjadi basi, dapat menjadi fiksi jika tak disegarkan dengan data |
| Desainer tertanam | Umpan balik cepat, kepemilikan bersama | Lebih sulit menjaga kerajinan konsisten lintas banyak tim |

Setiap organisasi menyeimbangkan investasi riset terhadap kecepatan pengiriman. Kekeliruannya memperlakukan ini sebagai salah satu-atau. Sikap yang produktif adalah proporsional: belanjakan lebih banyak penemuan pada keputusan yang mahal dibalik (IA inti, alur utama, pilihan platform), dan lebih sedikit pada detail yang mudah Anda ubah kelak. Biaya riset hampir selalu kecil dibanding biaya membangun hal yang salah dengan baik.

## Pertanyaan untuk didiskusikan dengan tim Anda

1. **Siapa yang memiliki arsitektur informasi dan kosakata terkendali bersama, dan apa yang terjadi ketika tim ingin menyimpang?** Pada skala besar kegagalan paling umum adalah membiarkan setiap skuad mengekspos struktur bagan organisasinya sendiri dan namanya sendiri untuk konsep yang sama, sehingga produk berakhir dengan tiga kata untuk satu hal dan navigasi yang mencerminkan departemen alih-alih tugas pengguna. Putuskan sekarang apakah IA dan kosakata dimiliki secara terpusat, diturunkan dari card sorting dan tree testing alih-alih politik internal, dan bagaimana tim meminta perubahan. Ini lebih penting di enterprise dan pemerintah karena pengguna terikat tidak dapat pergi, sehingga inkoherensi dibayar dalam pelatihan, tiket dukungan, dan galat alih-alih churn. Bawa daftar istilah duplikat dan alur yang bertentangan saat ini sebagai bukti. Jika Anda tidak dapat menamai pemilik, itu butir tindakan pertama Anda.

2. **Apa jalur perekrutan kita untuk peserta riset, dan apakah ia menjangkau pengguna assisted-digital, berkepercayaan diri rendah, dan non-digital?** Penemuan berkelanjutan hanya berfungsi jika Anda dapat berhadapan dengan pengguna nyata setiap minggu, dan orang yang paling sulit direkrut sering yang paling membutuhkan layanan: orang dalam krisis, pada perangkat lama, atau yang biasanya mengandalkan bantuan. Menguji hanya sukarelawan yang percaya diri dan terhubung memberi Anda pembacaan yang memuji tetapi palsu, terutama untuk layanan publik di mana kesetaraan akses adalah seluruh intinya. Sepakati siapa yang menjalankan perekrutan, insentif apa yang Anda tawarkan, dan bagaimana Anda mengamati sesi assisted-digital tanpa menambah beban orang yang rentan. Bawa demografi peserta dari tiga studi terakhir Anda dan periksa terhadap basis pengguna Anda yang sebenarnya. Jika condong ke pengguna yang mudah dijangkau, perbaiki jalurnya sebelum Anda memercayai temuan.

3. **Gerbang kualitas UX mana yang termasuk dalam definisi selesai kita, dan bagaimana kita mencegahnya menjadi teater?** Menanamkan desainer dan peneliti hanya membayar jika riset adalah masukan tetap bagi prioritisasi dan jika pemeriksaan kegunaan serta aksesibilitas benar-benar memblokir story agar tidak dikirim, bukan dek slide yang diangguki semua orang lalu diabaikan. Pilih metrik hasil konkret yang akan Anda lacak di samping metrik pengiriman: keberhasilan tugas, waktu pada tugas, tingkat galat, dan kepuasan. Risikonya riset dijalankan untuk membenarkan keputusan yang sudah dibuat, jadi sepakati siapa yang dapat memveto peluncuran pada gerbang UX dan bukti apa yang mengalahkan opini eksekutif. Bawa satu fitur terbaru dan tanyakan apakah risetnya mengubah keputusan atau sekadar menghiasinya. Jika temuan tak pernah menggeser peta jalan, gerbang Anda kosmetik.

4. **Bagaimana kita menjaga persona, peta perjalanan, dan IA agar tidak meluruh menjadi fiksi begitu riset yang menghasilkannya berusia setahun?** Model bersama adalah yang memungkinkan puluhan tim merancang menuju satu pengalaman koheren, tetapi mereka hanya berfungsi selama masih menggambarkan pengguna nyata, dan begitu persona menjadi artefak yang dikutip orang untuk memenangkan argumen alih-alih ringkasan bukti, ia melakukan bahaya aktif. Putuskan siapa yang memiliki penyegaran setiap model, pada irama apa, dan terhadap data apa (wawancara baru, analitik, tema dukungan), dan sepakati tanggal "terakhir divalidasi" yang terlihat agar model basi tampak jelas. Pertimbangan yang bersaing adalah biaya: menyegarkan segalanya terus-menerus itu boros, jadi kaitkan frekuensi penyegaran dengan seberapa cepat bagian basis pengguna atau perjalanan itu benar-benar berubah. Bawa asal-usul persona teratas Anda saat ini dan tanyakan kapan masing-masing terakhir diperiksa terhadap pengguna nyata. Di enterprise dan pemerintah, di mana basis pengguna terikat atau publik bergeser lambat namun berdampak (populasi menua, tunjangan baru, transisi perangkat), model yang diam-diam menyimpang kedaluwarsa dapat mengarahkan investasi bertahun-tahun ke pengguna yang tak lagi ada.

5. **Di mana aksesibilitas hidup dalam proses kita, dan dapatkah kita membuktikan rilis memenuhinya sebelum dikirim alih-alih setelah keluhan?** Memperlakukan aksesibilitas sebagai putaran kepatuhan terlambat adalah kegagalan paling umum sekaligus paling mahal, karena memasang semantik, urutan fokus, dan kontras ke antarmuka yang sudah dibangun berbiaya jauh lebih besar daripada merancangnya masuk. Putuskan standar mana yang Anda pegang (misalnya WCAG, Web Content Accessibility Guidelines), apakah kesesuaian adalah gerbang pemblokir dalam definisi selesai, dan siapa yang bertanggung jawab ketika fitur yang tak dapat diakses mencapai produksi. Ketegangannya kecepatan versus inklusi, dan tim di bawah tekanan tenggat diam-diam akan melepas pemeriksaan yang tidak ditegakkan. Bawa audit terakhir Anda, cakupan otomatis dan manual di baliknya, dan jumlah isu aksesibilitas yang ditemukan setelah rilis alih-alih sebelum. Untuk pemerintah khususnya ini bukan kesopanan opsional: ia sering kewajiban hukum dan soal kesetaraan, karena layanan publik yang mengecualikan pengguna disabilitas atau assisted-digital telah gagal pada tujuan intinya, bukan yang sekunder.

6. **Ketika analitik dan riset kualitatif kita tidak sepakat, bagaimana kita memutuskan mana yang dipercaya, dan siapa yang menengahi?** Organisasi besar mengumpulkan baik dasbor yang menunjukkan apa yang dilakukan ribuan pengguna maupun wawancara yang menjelaskan mengapa segelintir berperilaku demikian, dan keduanya rutin menunjuk arah berlawanan: alur dengan tingkat penyelesaian tinggi yang diam-diam mempermalukan orang, atau fitur yang dipuji pengguna dalam sesi tetapi tak pernah disentuh pada skala besar. Sepakati di muka bagaimana Anda melakukan triangulasi, pertanyaan mana yang dipercayakan kepada tiap metode (analitik untuk besaran dan jangkauan, riset untuk sebab dan makna), dan siapa yang berwenang memutuskan ketika keduanya berkonflik. Risikonya memilih-milih sumber mana pun yang menyanjung rencana yang sudah dipilih. Bawa ketidaksepakatan konkret terbaru dan telusuri bagaimana ia benar-benar diselesaikan. Dalam pengaturan enterprise dan publik taruhannya dipertajam karena analitik secara sistematis menghitung kurang orang yang paling penting: non-pengguna, yang meninggalkan, dan pengguna teknologi bantu jarang muncul di funnel, sehingga memercayai angka saja dapat membuat yang terkecualikan tak terlihat.

## Lensa sektor

**Startup.** Anda tidak punya peneliti dan tak ada waktu untuk repositori, jadi jadikan riset kebiasaan pendiri: duduk di samping lima pengguna nyata selama satu sore sebelum membangun hal berikutnya. Lewati persona dan peta perjalanan formal; pemahaman bersama tentang satu pekerjaan yang Anda selesaikan, disegarkan dengan menonton orang setiap minggu, mengalahkan dokumentasi yang tak dipelihara siapa pun. Keunggulan Anda adalah seluruh tim dapat menyerap wawasan pada hari yang sama ia muncul, jadi lindungi kecepatan itu dan tahan upacara.

**Bisnis kecil.** Tanpa spesialis UX dan dengan anggaran ketat, bersandarlah pada konvensi yang sudah dikenal pengguna Anda alih-alih menciptakan sendiri, dan beli perkakas dengan bawaan masuk akal alih-alih merancang alur dari nol. Lakukan sendiri riset murah bernilai tinggi: segelintir sesi kegunaan lewat panggilan video dan pembacaan tiket dukungan Anda akan memunculkan sebagian besar masalah parah. Perlakukan dasar aksesibilitas (kontras, label, akses keyboard) sebagai taruhan meja yang Anda dapat dari pustaka komponen yang baik alih-alih proyek yang Anda isi stafnya.

**Enterprise.** Masalah inti adalah koherensi lintas banyak tim, jadi investasikan pada fondasi bersama: persona yang dimiliki, peta perjalanan yang dipelihara, kosakata terkendali, dan arsitektur informasi terdokumentasi yang dirancang menuju oleh skuad alih-alih disiasati. Tanamkan desainer dan peneliti dalam tim pengiriman, tetapi atur kerajinan secara terpusat agar produk tidak pecah menjadi dialek tidak konsisten. Danai repositori riset dan gerbang kualitas dalam definisi selesai, dan lacak metrik hasil UX sebagai portofolio agar optimasi lokal tim mana pun tidak menurunkan keseluruhan.

**Pemerintah.** Aksesibilitas dan kesetaraan akses adalah kewajiban, bukan preferensi, jadi tahan rilis pada standar terbit dan lakukan riset dengan seluruh rentang publik, termasuk pengguna assisted-digital, berkepercayaan diri rendah, dan non-digital. Pengadaan dan transparansi membentuk pengiriman: terbitkan prinsip desain dan metode riset Anda, strukturkan layanan di sekitar peristiwa hidup warga alih-alih departemen internal, dan simpan bukti pengujian untuk audit. Karena pengguna sering tak punya penyedia alternatif, alur yang tak dapat mereka selesaikan menolak layanan, jadi perlakukan penyelesaian oleh pengguna tersulit dijangkau sebagai ukuran keberhasilan sejati.

## Contoh

**Startup.** Sebuah startup empat orang yang membangun perkakas penjadwalan untuk klinik kecil punya pendapat kuat tentang apa yang dibutuhkan resepsionis, tetapi tanpa bukti. Sebelum menulis lebih banyak fitur, para pendiri duduk di samping lima resepsionis selama satu sore masing-masing dan menyaksikan mereka bekerja. Mereka belajar bahwa rasa sakit sebenarnya bukan kecepatan pemesanan melainkan pemesanan ganda yang disebabkan tampilan kalender yang membingungkan, sesuatu yang tak terpikir untuk disebut siapa pun dalam panggilan penjualan sebelumnya. Membingkai ulang produk di sekitar satu pekerjaan itu, dan menyketsa serta menguji perbaikan dengan kelima orang yang sama selama seminggu, mengubah uji coba yang macet menjadi pelanggan berbayar pertama mereka.

**Enterprise.** Sebuah bank multinasional mengonsolidasikan tujuh perkakas asal-usul pinjaman internal regional menjadi satu platform. Alih-alih menggabungkan himpunan fitur, tim menjalankan pemetaan perjalanan dan service blueprinting dengan underwriter lintas wilayah. Mereka menemukan bahwa "perbedaan regional" yang diasumsikan semua orang sebagian besar adalah terminologi dan urutan layar yang tidak konsisten, bukan perbedaan proses sejati. IA terpadu dan kosakata bersama memotong waktu pelatihan underwriter secara substansial dan mengurangi galat pemrosesan, karena staf kini berbagi satu model mental.

**Pemerintah.** Sebuah otoritas pajak nasional yang mendesain ulang layanan pengajuan daringnya menjalankan uji kegunaan termoderasi dengan wajib pajak lintas usia, perangkat, dan tingkat kepercayaan diri digital, ditambah pengamatan assisted-digital terhadap orang yang biasanya mengandalkan bantuan. Pengujian mengungkap bahwa judul bagian yang sarat jargon membuat orang meninggalkan atau salah mengajukan. Membingkai ulang konten di sekitar jobs-to-be-done wajib pajak, dan menyusun ulang IA di sekitar peristiwa hidup alih-alih kode pajak internal, meningkatkan penyelesaian swalayan yang berhasil dan mengurangi volume pusat panggilan, langsung menurunkan biaya melayani sambil memperbaiki kesetaraan akses.

## Kasus bisnis: motivasi, ROI, dan TCO

Imbal hasil UX datang dari tiga tuas: lebih banyak keberhasilan (lebih banyak pengguna menyelesaikan tugas bernilai), biaya melayani lebih rendah (lebih sedikit kontak dukungan, lebih sedikit pelatihan, lebih sedikit galat), dan lebih sedikit pengerjaan ulang (menangkap arah salah sebelum dibangun). Dalam pengaturan enterprise di mana pengguna terikat, imbalannya muncul sebagai produktivitas dan galat lebih sedikit alih-alih konversi; beberapa detik yang dihemat per transaksi, di ribuan karyawan, berlipat menjadi penghematan tahunan besar.

Total biaya kepemilikan harus menimbang biaya mengadopsi terhadap biaya tidak mengadopsi. Biaya adopsi mudah terlihat: peneliti dan desainer, perekrutan dan insentif untuk peserta, perkakas, dan waktu dalam jadwal. Biaya tidak mengadopsi lebih besar tetapi lebih sulit dikenali: transaksi yang ditinggalkan, beban dukungan dan pelatihan, desain ulang terlambat yang mahal, peluncuran gagal, dan paparan reputasi atau hukum ketika layanan publik mengecualikan orang. Karena biaya ini tersebar di anggaran dukungan, pelatihan, dan operasi alih-alih lini produk, pimpinan sering meremehkannya.

Untuk mengajukan kasus kepada pimpinan, kaitkan UX dengan metrik yang sudah dilacak eksekutif: tingkat penyelesaian dan konversi, biaya per transaksi, volume tiket dukungan, hari pelatihan, dan tingkat galat serta pengerjaan ulang. Jalankan percontohan kecil yang diinstrumentasi yang menunjukkan sebelum-dan-sesudah terukur, lalu ekstrapolasikan di seluruh portofolio. Membingkai riset sebagai pengurangan risiko pada keputusan tak terbalikkan cenderung menggema dengan pemangku kepentingan keuangan dan tata kelola.

## Anti-pola dan jebakan

- **Desain digerakkan HiPPO**: keputusan dibuat oleh opini orang berbayaran tertinggi alih-alih bukti.
- **Teater riset**: studi dijalankan untuk membenarkan keputusan yang sudah dibuat, temuan diabaikan.
- **Persona sebagai fiksi**: profil ciptaan yang tak pernah divalidasi terhadap pengguna nyata, dipakai untuk memenangkan argumen.
- **Bagan organisasi sebagai IA**: navigasi yang mencerminkan departemen internal alih-alih tugas pengguna.
- **Riset big-bang**: studi mahal yang jarang yang tiba terlalu terlambat untuk mengubah apa pun.
- **Menguji hanya jalur bahagia**: mengabaikan keadaan galat, kasus tepi, dan pengguna di bawah tekanan.
- **Desain sebagai lapisan cat terakhir**: membawa UX hanya untuk membuat build jadi "tampak bagus."
- **Mengabaikan pengguna assisted dan non-digital**: merancang hanya untuk pengguna yang percaya diri dan terhubung.

## Model kematangan

**Tingkat 1: Memulai.** Tidak ada praktik UX khusus. Keputusan dibuat oleh opini dan naluri orang berbayaran tertinggi. Riset, jika terjadi sama sekali, ad hoc dan reaktif, dipicu oleh peluncuran yang berjalan buruk. Alur dan terminologi tidak konsisten lintas tim, dan tak seorang pun memiliki pengalaman keseluruhan.

**Tingkat 2: Mengembangkan.** Beberapa tim punya desainer dan menjalankan uji kegunaan sesekali, dan beberapa persona atau peta perjalanan ada, tetapi praktik sangat bervariasi antarskuad dan tidak dipelihara. UX diperlakukan sebagai fase alih-alih disiplin berkelanjutan, dan sering dilewati di bawah tekanan jadwal. Kerja baik terjadi di kantong-kantong tetapi tidak berjumlah di seluruh produk.

**Tingkat 3: Membakukan.** Riset multimetode berkelanjutan memberi makan prioritisasi, dan persona bersama, peta perjalanan, dan IA kosakata-terkendali terdokumentasi dan dipakai lintas tim. Gerbang kualitas UX, termasuk tolok ukur kegunaan dan pemeriksaan aksesibilitas, berada dalam definisi selesai dan ditegakkan di seluruh organisasi. Repositori riset yang dapat dicari menjaga wawasan dapat dipakai ulang alih-alih terperangkap di slide satu skuad.

**Tingkat 4: Mengelola.** Praktik diukur terhadap garis dasar alih-alih sekadar dilakukan. Anda melacak keberhasilan tugas, waktu pada tugas, tingkat galat, kepuasan, dan kesesuaian aksesibilitas sebagai metrik yang disepakati, menetapkan target, dan mengawasinya sepanjang rilis. Sampel peserta riset diperiksa terhadap basis pengguna nyata agar temuan representatif, gerbang kualitas melaporkan tingkat lulus alih-alih opini, dan biaya riset ditimbang terhadap pengurangan terukur dalam kontak dukungan, pelatihan, dan pengerjaan ulang. Keputusan kirim atau tahan bertumpu pada bukti terhadap garis dasar itu.

**Tingkat 5: Mengorkestrasi.** Riset berkelanjutan, terkait hasil, dan terintegrasi dengan perencanaan produk, bisnis, dan risiko di seluruh organisasi. Tim menjalankan eksperimen terkendali, menutup lingkaran dari wawasan ke perubahan yang dikirim ke efek terukur, dan memensiunkan atau menentukan ulang cakupan model pengguna seiring populasi dan perjalanannya bergeser. Fondasi UX beradaptasi terus-menerus: persona, perjalanan, IA, dan standar disegarkan atas bukti, dan organisasi menyeimbangkan ulang di mana ia berinvestasi penemuan seiring keterbalikan dan risiko berubah.

## Gagasan untuk didiskusikan

- Berapa banyak penemuan yang "cukup" sebelum berkomitmen pada arah, dan siapa yang memutuskan?
- Bagaimana Anda menjaga persona dan peta perjalanan tetap hidup alih-alih membiarkannya menjadi artefak basi?
- Ketika analitik kuantitatif dan riset kualitatif tidak sepakat, mana yang Anda percayai dan mengapa?
- Bagaimana organisasi besar harus menyeimbangkan standar UX pusat dengan otonomi setiap tim?
- Apa cara yang tepat meriset layanan yang dipakai orang dalam krisis tanpa menambah beban mereka?
- Bagaimana Anda mengukur ROI riset yang mencegah kesalahan yang karenanya tak pernah Anda buat?

## Poin-poin utama

- UX adalah cara bekerja sejak awal, bukan dekorasi di akhir.
- Padukan metode kualitatif (mengapa) dengan metode kuantitatif (berapa banyak).
- Modelkan pengguna dengan persona berbasis bukti, peta perjalanan, jobs-to-be-done, dan service blueprint.
- Strukturkan informasi di sekitar model mental pengguna, bukan bagan organisasi.
- Perlakukan design thinking sebagai pola pikir pragmatis dengan putaran pembelajaran ketat, bukan proses kaku.
- Biaya riset kecil dibanding biaya membangun hal yang salah.
- Dalam enterprise dan pemerintah, kualitas UX langsung berarti produktivitas, biaya melayani, dan kesetaraan akses.

## Referensi dan bacaan lanjutan

- Don Norman, *The Design of Everyday Things*
- Steve Krug, *Don't Make Me Think*
- Erika Hall, *Just Enough Research*
- Kim Goodwin, *Designing for the Digital Age*
- Louis Rosenfeld, Peter Morville, dan Jorge Arango, *Information Architecture: For the Web and Beyond*
- Clayton Christensen et al., *Competing Against Luck* (jobs-to-be-done)
- Alan Cooper, *The Inmates Are Running the Asylum*
- Jakob Nielsen, *Usability Engineering*
- UK Government Digital Service, *Service Manual* dan *Design Principles*
- U.S. General Services Administration, *18F Methods* dan panduan riset *U.S. Web Design System*
- Nielsen Norman Group, artikel dan laporan metode riset
