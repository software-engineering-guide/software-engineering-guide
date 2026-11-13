# 2.8 Persyaratan perangkat lunak

## Tinjauan dan motivasi

[Persyaratan perangkat lunak](https://en.wikipedia.org/wiki/Software_requirements) adalah pernyataan tentang kemampuan atau kondisi yang harus disediakan, dipenuhi, atau dimiliki sebuah sistem agar dapat diterima oleh para pemangku kepentingannya. [Rekayasa persyaratan](https://en.wikipedia.org/wiki/Requirements_engineering), pekerjaan disiplin menggali, menganalisis, menspesifikasikan, memvalidasi, dan mengelola pernyataan itu, berada tepat di awal rantai nilai. Segala sesuatu di hilir, dari arsitektur hingga kode hingga [pengujian penerimaan](https://en.wikipedia.org/wiki/Acceptance_testing), adalah upaya memenuhi persyaratan. Jadi ketika persyaratan keliru, tidak lengkap, atau ambigu, semua upaya yang dihabiskan membangun hal yang salah dengan benar adalah pemborosan murni, dan itu pemborosan termahal yang ada, karena Anda menemukannya paling akhir. Area pengetahuan Software Requirements dalam [Software Engineering Body of Knowledge](https://en.wikipedia.org/wiki/Software_Engineering_Body_of_Knowledge) (SWEBOK) memperlakukan ini sebagai disiplin rekayasa sejati, bukan pendahuluan klerikal bagi pekerjaan sebenarnya.

Bagi tim besar, persyaratan adalah pemahaman bersama yang memungkinkan banyak orang membangun satu sistem yang koheren. Satu pengembang dapat memegang maksud di kepalanya; ratusan orang di banyak tim tidak. Persyaratan menjadi kontrak antara mereka yang membutuhkan kemampuan dan mereka yang membangunnya, dasar untuk membagi pekerjaan antartim, dan tolok ukur untuk menilai kapan sesuatu "selesai." Mereka terhubung langsung dengan penemuan (bab 11.1), tempat masalah dan peluang muncul; dengan fondasi UX (bab 5.1), tempat Anda memahami kebutuhan pengguna; dengan API dan desain antarmuka (bab 2.3), tempat kewajiban antarmuka ditetapkan; dengan arsitektur dan atribut kualitas (bab 3.1), tempat persyaratan nonfungsional menggerakkan struktur; dan dengan manajemen proyek (bab 10.6), tempat cakupan, biaya, dan jadwal direncanakan di sekitarnya.

Dalam konteks enterprise dan pemerintah, persyaratan membawa bobot hukum, kontraktual, dan keselamatan. Sistem yang diatur harus menunjukkan bahwa setiap kewajiban yang diwajibkan (aksesibilitas, privasi, keamanan, retensi catatan, kendali keuangan) ditangkap sebagai persyaratan, diimplementasikan, dan diverifikasi dengan bukti. Pengadaan pemerintah sering dibangun di sekitar spesifikasi persyaratan, dan pembayaran, audit, serta sertifikasi semuanya bergantung pada pelacakan setiap persyaratan ke bukti bahwa ia terpenuhi. Di sini, persyaratan lebih dari praktik baik: mereka adalah tulang punggung akuntabilitas.

## Prinsip utama

- Persyaratan mengekspresikan kebutuhan atau kendala, bukan solusi; ia menyatakan apa dan mengapa, bukan bagaimana.
- Setiap persyaratan harus perlu, tidak ambigu, dapat diverifikasi, layak, dan dapat dilacak.
- Persyaratan ditemukan dan dinegosiasikan dengan pemangku kepentingan, tidak diciptakan secara terpisah.
- Persyaratan nonfungsional dan kendala membentuk arsitektur sama banyaknya dengan fungsionalitas.
- Persyaratan berkembang; kelola perubahan dengan sengaja alih-alih membekukan atau mengabaikannya.
- Keterlacakan, dari kebutuhan ke persyaratan ke desain ke tes ke bukti, adalah jaringan penghubung akuntabilitas.
- Tingkat formalitas yang tepat bergantung pada risiko, skala, dan konteks regulasi, bukan kebiasaan.

## Rekomendasi

### Definisikan persyaratan dengan jelas dan kategorikan

Namai kategori dengan sengaja. **[Persyaratan fungsional](https://en.wikipedia.org/wiki/Functional_requirement)** menyatakan apa yang harus dilakukan sistem: perilaku, transformasi, dan layanan yang disediakannya. **[Persyaratan nonfungsional](https://en.wikipedia.org/wiki/Non-functional_requirement)** (atribut kualitas) menyatakan seberapa baik ia harus melakukannya: kinerja, ketersediaan, keamanan, kegunaan, aksesibilitas, kemudahan pemeliharaan, dan lainnya; ini terikat erat dengan arsitektur (bab 3.1). **Kendala** adalah batas yang tak dapat ditawar pada solusi: teknologi yang diwajibkan, standar, anggaran, aturan hukum, atau antarmuka ke sistem yang ada. Dan pisahkan **persyaratan bisnis** (mengapa organisasi menginginkan sistem) dari **persyaratan pengguna** (apa yang perlu dicapai pengguna) dari **persyaratan sistem** (apa yang karenanya harus dilakukan perangkat lunak). Kaburkan tingkat ini bersama-sama dan kebingungan cakupan segera menyusul.

### Gali dari sumber nyata, bukan asumsi

Penggalian adalah penemuan aktif. Tarik persyaratan dari pemangku kepentingan lewat wawancara, lokakarya, observasi, [prototipe](https://en.wikipedia.org/wiki/Software_prototyping), dan analisis sistem serta dokumen yang ada. Temukan setiap pemangku kepentingan yang relevan, termasuk yang mudah terlewat: operator, auditor, staf dukungan, dan orang yang terdampak sistem yang tidak pernah menggunakannya secara langsung. Kaitkan penggalian dengan pipeline penemuan (bab 11.1) dan riset UX (bab 5.1), agar keinginan yang dinyatakan dapat dilacak kembali ke kebutuhan yang mendasarinya. Catat sumber dan alasan setiap persyaratan, karena mengetahui mengapa persyaratan ada adalah persis yang memungkinkan Anda mengubahnya dengan aman kelak.

### Analisis, negosiasikan, dan prioritaskan

Kebutuhan mentah yang digali saling bertentangan, tumpang-tindih, dan berjumlah lebih dari yang layak. Analisis adalah cara Anda mendamaikannya: mengklasifikasi persyaratan, menemukan konflik, menimbang kelayakan dan risiko, dan menegosiasikan prioritas dengan pemangku kepentingan. Prioritaskan secara terbuka, misalnya dengan pembedaan must/should/could atau peringkat nilai-versus-biaya, agar ketika waktu menipis, Anda memotong cakupan yang tepat. Dan modelkan persyaratan di mana pun model menambah kejelasan: alur proses, diagram status, model data, dan definisi antarmuka memunculkan celah yang disembunyikan prosa.

### Spesifikasikan pada tingkat formalitas yang tepat

Tuliskan persyaratan dalam bentuk yang sesuai dengan risiko dan audiens. Sistem pemerintah berjaminan tinggi mungkin membenarkan spesifikasi formal yang distrukturkan menurut standar seperti IEEE 29148; tim produk yang bergerak cepat dapat menangkap persyaratan sebagai [user story](https://en.wikipedia.org/wiki/User_story) dengan kriteria penerimaan dalam backlog. Bagaimanapun, setiap persyaratan harus atomik, dapat diverifikasi, dan bebas dari kata licin seperti "cepat," "ramah pengguna," atau "dll." Lampirkan kriteria penerimaan, agar Anda mendefinisikan cara memverifikasi persyaratan pada saat yang sama Anda menulisnya. Dan simpan satu sumber berwenang, alih-alih membiarkan persyaratan tersebar di email, tiket, dan slide.

### Validasi sebelum membangun

Validasi memastikan bahwa persyaratan yang telah Anda spesifikasikan adalah yang benar dan saling padu. Tinjau bersama pemangku kepentingan, telusuri skenario, dan bila bisa, gunakan prototipe untuk membuat pernyataan abstrak menjadi konkret. Validasi lebih murah daripada koreksi apa pun kemudian: cacat yang tertangkap dalam tinjauan persyaratan memakan sebagian kecil dari cacat yang sama yang tertangkap di produksi.

### Kelola persyaratan dan pertahankan keterlacakan

Persyaratan berubah. Tugas Anda mengendalikan perubahan itu, bukan menolaknya. Dirikan proses perubahan: timbang setiap perubahan yang diusulkan untuk dampak, biaya, dan efek hilir sebelum Anda menerimanya. Baselinekan persyaratan pada titik yang disepakati dan beri versi. Pertahankan **[keterlacakan dua arah](https://en.wikipedia.org/wiki/Requirements_traceability)** yang menautkan setiap persyaratan maju ke desain, kode, dan tes, dan mundur ke kebutuhan asalnya. Keterlacakan menjawab dua pertanyaan yang menjadi pegangan tim besar: jika kebutuhan ini berubah, apa yang terdampak; dan untuk fitur yang dikirim ini, kebutuhan mana yang membenarkannya? Dalam konteks yang diatur, perluas jejak sampai ke bukti penerimaan (hasil tes, catatan audit, pengesahan) agar Anda dapat mendemonstrasikan kepatuhan, bukan sekadar menegaskannya.

### Beradaptasi dengan konteks agile dan berbasis rencana

Dalam program berbasis rencana dan yang diatur, Anda menspesifikasikan dan membaselinekan persyaratan cukup awal, dengan kendali perubahan formal. Dalam konteks agile, persyaratan hidup sebagai backlog berprioritas yang berkembang, dielaborasi tepat sebelum implementasi dan divalidasi terus-menerus lewat perangkat lunak yang berfungsi. Kegiatan dasarnya sama di keduanya; hanya waktu, formalitas, dan artefaknya yang berbeda. Organisasi besar sering memadukan keduanya: mereka menspesifikasikan dan melacak kewajiban stabil berjaminan tinggi secara formal, sambil mengelaborasi perilaku produk secara iteratif. Pilih keseimbangannya berdasarkan risiko, bukan ideologi.

## Trade-off: kelebihan dan kekurangan

| Pendekatan | Terbaik untuk | Kelebihan | Kekurangan |
|---|---|---|---|
| Spesifikasi formal di muka | Kontrak berjaminan tinggi, diatur, cakupan tetap | Keterlacakan kuat; dasar penerimaan jelas; dapat diaudit | Lambat berubah; berisiko menspesifikasikan berlebihan sebelum belajar |
| Backlog agile | Produk berkembang dengan pemangku kepentingan yang terlibat | Umpan balik cepat; beradaptasi dengan pembelajaran; lebih sedikit pemborosan pada cakupan yang tak dibangun | Keterlacakan jangka panjang lebih lemah; lebih sulit diaudit dan dikontrakkan |
| Hibrida (kendala formal + perilaku agile) | Enterprise dengan kewajiban campuran | Ketelitian di tempat penting, fleksibilitas di tempat lain | Memerlukan penilaian tentang bagian mana yang mana |

Ketegangan pusatnya adalah antara stabilitas dan pembelajaran. Mengunci persyaratan lebih awal membeli dasar penerimaan yang kokoh dan kemampuan diaudit, tetapi memakan kemampuan beradaptasi dengan apa yang Anda pelajari selama membangun. Menundanya membeli kemampuan beradaptasi, tetapi memakan keterlacakan jangka panjang dan kejelasan kontraktual. Berinvestasi lebih banyak dalam rekayasa persyaratan juga menukar kecepatan jangka pendek dengan lebih sedikit pengerjaan ulang kelak: pertukaran yang membuahkan hasil seiring skala, umur panjang, dan konsekuensi kegagalan sistem naik. Proyek terbesar dan yang paling diatur berada tegas di sisi investasi tinggi. Perkakas internal berisiko rendah tidak.

## Pertanyaan untuk didiskusikan dengan tim Anda

1. **Siapa yang dihitung sebagai pemangku kepentingan untuk sistem berisiko tertinggi kita, dan siapa yang terus kita tinggalkan sampai penerimaan?** Pada program besar orang yang terlewat jarang pengguna yang jelas: mereka adalah operator yang menjalankannya pukul 3 pagi, auditor yang harus mensertifikasinya, staf dukungan yang menangani kegagalannya, dan non-pengguna terdampak yang tidak pernah masuk tetapi datanya Anda pegang. Lewatkan mereka dan Anda menemukan persyaratan mereka pada saat paling mahal, selama penerimaan atau setelah regulator bertanya. Bawa peta pemangku kepentingan konkret ke rapat dan uji ketahanannya: untuk setiap kewajiban yang diwajibkan (aksesibilitas, privasi, retensi catatan, keamanan) namai orang yang memilikinya dan persyaratan yang menangkapnya. Jika Anda tidak dapat menyebut pemilik, Anda telah menemukan celah, dan perbaikannya adalah menambahkan pemangku kepentingan itu ke penggalian sekarang alih-alih menambal kebutuhan mereka ke arsitektur yang sudah tetap kelak.

2. **Ketika persyaratan berubah, dapatkah kita menjawab apa yang terdampak sebelum kita menyetujui perubahan itu?** Ini ujian praktis apakah keterlacakan dua arah Anda nyata atau dekoratif. Dalam sistem besar atau yang diatur, satu perubahan aturan dapat beriak ke desain, kode, tes, dan bukti penerimaan, dan menyetujuinya secara buta adalah cara Anda merilis sistem yang tampak patuh yang diam-diam melanggar aturan yang dulu dipenuhinya. Bawa permintaan perubahan terbaru dan coba lacak maju di rapat: jika memakan sore penuh arkeologi, keterlacakan Anda tidak menjalankan tugasnya. Jawabannya harus membentuk ulang proses perubahan Anda, agar penilaian dampak adalah kueri cepat terhadap jejak hidup alih-alih perburuan manual, dan agar baseline serta pembuatan versi memberi titik stabil untuk berubah.

3. **Di mana sumber berwenang tunggal persyaratan kita berada, dan seberapa banyak kebenaran tersebar di luarnya?** Persyaratan yang menjamur (spesifikasi nyata yang hidup di email, tiket, slide, dan ingatan seseorang) adalah salah satu kegagalan paling umum pada tim besar, dan fatal dalam sistem teraudit di mana Anda harus menunjukkan apa yang disepakati. Putuskan, dengan lantang, sistem pencatat mana yang kanonik, dan perlakukan apa pun yang dinyatakan di tempat lain sebagai draf sampai mendarat di sana dengan sumber dan alasannya terlampir. Bawa bukti: hitung berapa sengketa cakupan terbaru yang berujung pada dua orang mengutip versi "final" yang berbeda. Jika hitungannya lebih dari nol, tindakannya adalah mengonsolidasikan ke satu sumber dan menuliskan alasan setiap persyaratan, karena mengetahui mengapa persyaratan ada adalah persis yang memungkinkan Anda mengubah atau membuangnya dengan aman kelak.

4. **Apakah persyaratan nonfungsional kita ditangkap cukup awal untuk menggerakkan arsitektur, atau kita terus menemukannya setelah struktur ditetapkan?** Kewajiban kinerja, ketersediaan, keamanan, dan aksesibilitas membentuk arsitektur lebih daripada kebanyakan fitur, dan pada program besar mereka adalah persyaratan yang paling sering muncul terlambat, ketika struktur yang harus memenuhinya sudah dicor menjadi beton. Tarikan yang bersaing itu nyata: perilaku fungsional adalah yang diminta pemangku kepentingan dengan lantang dan baik didemokan, sementara persyaratan "respons di bawah satu detik pada beban puncak" atau "kesesuaian aksesibilitas WCAG" tak terlihat sampai dilanggar. Bawa daftar persyaratan nonfungsional saat ini untuk sistem berisiko tertinggi Anda, titik dalam lini waktu saat masing-masing ditulis, dan apakah arsitektur (bab 3.1) menerimanya sebagai pendorong eksplisit atau menyimpulkannya. Dalam konteks enterprise dan pemerintah, tambahkan kewajiban kualitas yang diwajibkan (enkripsi, retensi catatan, hukum aksesibilitas) dan periksa bahwa masing-masing adalah persyaratan tertulis yang terukur yang diserahkan ke desain alih-alih asumsi, karena menambal atribut kualitas setelah penerimaan adalah tempat anggaran dan jadwal diam-diam mati.

5. **Tingkat formalitas mana yang tepat untuk setiap sistem yang kita miliki, dan apakah kita memilihnya berdasarkan risiko atau kebiasaan?** Satu organisasi besar biasanya menjalankan rentang sistem, dari perkakas internal sekali pakai hingga platform yang diatur terkait nyawa atau keselamatan, dan menerapkan satu upacara pada semuanya entah mengubur pekerjaan berisiko rendah dalam administrasi atau membiarkan pekerjaan berisiko tinggi kurang terspesifikasi. Ketegangannya antara kemampuan diaudit dan dasar penerimaan yang kokoh dari spesifikasi formal di muka dan umpan balik cepat serta pemborosan yang berkurang dari backlog yang berkembang, dan jawaban jujur bagi kebanyakan enterprise adalah perpaduan yang disengaja: formalkan dan lacak kewajiban stabil berjaminan tinggi sambil mengelaborasi perilaku produk secara iteratif. Bawa inventaris singkat sistem Anda yang diperingkat menurut konsekuensi kegagalan, paparan regulasi, dan laju perubahan, dan untuk masing-masing namai formalitas yang sebenarnya Anda pakai versus formalitas yang dibenarkan risiko. Untuk program pemerintah yang berlabuh pada solicitation dan standar seperti IEEE 29148, formalitas sebagian ditentukan kontrak, jadi diskusinya adalah di mana Anda dapat melapiskan elaborasi agile di atasnya tanpa merusak keterlacakan yang bergantung pada audit.

6. **Dapatkah setiap persyaratan dalam sistem berisiko tertinggi kita diverifikasi, dan apakah masing-masing membawa kriteria penerimaan yang ditulis pada saat persyaratan itu ditulis?** Persyaratan yang tidak dapat Anda verifikasi bukan persyaratan, melainkan angan-angan, dan kata licin seperti "cepat," "aman," atau "ramah pengguna" lolos tinjauan justru karena tak seorang pun dapat menggagalkannya. Bagi tim besar ini penting dua kali lipat: persyaratan yang tidak dapat diverifikasi menghasilkan sengketa cakupan saat penerimaan, dan membuat mustahil mengatakan kapan fitur benar-benar selesai. Pertimbangan yang bersaing adalah kecepatan, karena melampirkan kriteria terukur dan metode verifikasi pada setiap persyaratan lebih lambat di muka daripada menulis prosa, tetapi itu pertahanan termurah terhadap pengerjaan ulang terlambat yang paling mahal. Bawa sampel persyaratan terbaru dan uji masing-masing terhadap tolok ukur sederhana: apakah atomik, apakah terukur, dan apakah menyebut bagaimana ia akan diperiksa. Dalam konteks yang diatur dan pemerintah, perluas ujian ke bukti: persyaratan tanpa bukti penerimaan yang terlacak dan lolos tidak dianggap terkirim apa pun yang tampaknya dilakukan perangkat lunak, jadi kriteria penerimaan adalah benih catatan kepatuhan yang akhirnya harus Anda hasilkan.

## Lensa sektor

**Startup.** Dengan tim mungil dan runway terbatas, jaga persyaratan seringan mungkin yang bisa Anda lolos: user story dengan kriteria penerimaan dalam satu backlog bersama, bukan dokumen spesifikasi. Disiplin yang membuahkan hasil bahkan di sini adalah berbicara dengan pengguna nyata sebelum membangun dan mencatat sumber serta alasan setiap story, sehingga minggu yang akan Anda sia-siakan membangun fitur yang salah adalah minggu yang Anda hemat. Lewati keterlacakan formal, tetapi jangan pernah lewati percakapan yang memberi tahu Anda apa kebutuhan sebenarnya.

**Bisnis kecil.** Anda kemungkinan tidak punya analis bisnis atau spesialis persyaratan, jadi pekerjaan jatuh pada siapa pun yang paling dekat dengan pelanggan, dan pertanyaan beli-versus-bangun mendominasi. Bingkai persyaratan sebagai daftar singkat berprioritas tentang hasil yang Anda butuhkan, lalu gunakan untuk mengevaluasi perkakas siap pakai alih-alih menspesifikasikan pembangunan khusus. Tegaslah memisahkan kebutuhan mendasar dari daftar fitur vendor, karena persyaratan yang ditulis sebagai "kita butuh produk X" diam-diam menutup opsi lebih murah yang akan memenuhi kebutuhan sebenarnya.

**Enterprise.** Skala menjadikan persyaratan sebagai kontrak yang memungkinkan banyak tim membangun satu sistem yang koheren, jadi prioritasnya adalah proses baku yang diterapkan konsisten: kategori terdefinisi, keterlacakan dua arah dari kebutuhan ke tes, satu sumber berwenang, dan perubahan terkendali dengan baseline. Pisahkan persyaratan bisnis, pengguna, dan sistem secara eksplisit dan serahkan persyaratan nonfungsional ke arsitektur sebagai pendorong, agar kewajiban cakupan dan kualitas tidak tersebar antartim. Padukan spesifikasi formal untuk kewajiban stabil berjaminan tinggi dengan elaborasi agile atas perilaku produk, dan atur keseimbangannya berdasarkan risiko, bukan preferensi satu tim.

**Pemerintah.** Aturan pengadaan sering membangun seluruh kontrak di sekitar spesifikasi persyaratan, kerap distrukturkan menurut standar seperti IEEE 29148, sehingga presisi dan kelengkapan bersifat kontraktual, bukan opsional. Pelihara matriks keterlacakan persyaratan yang menautkan setiap persyaratan ke desain, kasus tes, dan bukti penerimaan, karena pembayaran vendor, audit, dan authority to operate semuanya bergantung pada cakupan yang terdemonstrasi. Transparansi dan akuntabilitas publik menaikkan standar lebih jauh: kewajiban yang diwajibkan untuk aksesibilitas, privasi, dan retensi catatan masing-masing harus muncul sebagai persyaratan eksplisit yang dapat diverifikasi, dan persyaratan tanpa bukti yang terlacak dan lolos sederhananya tidak terkirim.

## Contoh

**Startup.** Sebuah startup empat orang yang membangun aplikasi penjadwalan menangkap persyaratan sebagai user story dengan kriteria penerimaan dalam backlog bersama, bukan spesifikasi formal. Sebelum menulis fitur sinkronisasi kalender, pendiri menghabiskan sore berbicara dengan lima calon pelanggan dan mengetahui bahwa kebutuhan sebenarnya adalah menghindari pemesanan ganda di dua perkakas, bukan sinkronisasi yang mereka asumsikan. Satu percakapan itu membingkai ulang story dan menghemat seminggu membangun hal yang salah. Bahkan pada skala ini mereka menuliskan sumber dan alasan setiap story, sehingga ketika prioritas bergeser mereka dapat membuang atau mengerjakan ulang cakupan tanpa mengadili ulang mengapa ia ada.

**Enterprise.** Sebuah bank multinasional mengganti platform asal-usul pinjamannya. Tim persyaratan memisahkan persyaratan bisnis (mengurangi waktu persetujuan, memenuhi regulasi pemberian pinjaman), persyaratan pengguna (petugas pinjaman perlu membandingkan penawaran dalam satu tampilan), dan persyaratan sistem (platform harus terintegrasi dengan tiga sistem inti). Persyaratan nonfungsional (respons di bawah satu detik untuk kueri umum, ketersediaan 99,95%, enkripsi data pribadi) ditangkap secara eksplisit dan diserahkan ke arsitektur (bab 3.1) sebagai pendorong. Setiap persyaratan dilacak melalui backlog ke tes penerimaan otomatis. Jadi ketika regulator bertanya bagaimana aturan pinjaman tertentu ditegakkan, tim cukup mengikuti jejak dari aturan ke tes yang memverifikasinya.

**Pemerintah.** Sebuah lembaga nasional mengadakan sistem kelayakan tunjangan lewat solicitation formal. Kontrak berlabuh pada spesifikasi persyaratan yang distrukturkan menurut IEEE 29148, mencakup aturan kelayakan fungsional, kesesuaian aksesibilitas yang diwajibkan, kendala privasi dan retensi catatan, serta kontrol keamanan. Matriks keterlacakan persyaratan menautkan setiap persyaratan ke elemen desain, kasus tes, dan bukti penerimaan. Pembayaran vendor dan authority to operate (persetujuan formal untuk menjalankan sistem di produksi) keduanya bergantung pada cakupan yang terdemonstrasi. Persyaratan tanpa bukti penerimaan yang terlacak dan lolos sederhananya tidak dianggap terkirim, apa pun yang tampaknya dilakukan perangkat lunak.

## Kasus bisnis: motivasi, ROI, dan TCO

Argumen ekonomi untuk rekayasa persyaratan bertumpu pada biaya memperbaiki cacat terlambat. Studi industri secara konsisten menemukan bahwa cacat persyaratan termasuk penyebab kegagalan proyek yang paling umum dan paling mahal, dan bahwa biaya memperbaiki cacat naik berorde-orde besaran dari fase persyaratan ke produksi. Jadi uang yang dihabiskan untuk menjernihkan dan memvalidasi persyaratan sesungguhnya adalah daya ungkit: investasi sederhana di awal menyelamatkan Anda dari membangun, menguji, dan mengoperasikan hal yang salah.

Total biaya kepemilikan persyaratan mencakup upaya berkelanjutan penggalian, spesifikasi, perkakas, dan manajemen perubahan sepanjang seluruh umur sistem; bukan biaya sekali jalan. Terhadapnya berdiri biaya persyaratan yang buruk: pengerjaan ulang, sengketa cakupan, keterlambatan jadwal, penerimaan yang gagal, penalti kontraktual, dan, di lingkungan yang diatur, denda atau hilangnya otorisasi. Untuk pimpinan, bingkai kematangan persyaratan sebagai pengurangan risiko dan keterprediksian. Lacak volatilitas persyaratan, asal cacat, dan persentase pekerjaan terkirim yang dapat dilacak ke kebutuhan tervalidasi, dan hubungkan dengan perkiraan manajemen proyek (bab 10.6). Imbal hasilnya tidak muncul sebagai fitur. Ia muncul sebagai kegagalan dan pengerjaan ulang yang tidak pernah terjadi.

## Anti-pola dan jebakan

- **Solusi yang menyamar sebagai persyaratan:** menspesifikasikan teknologi pilihan atau tata letak layar alih-alih kebutuhan mendasar, menutup opsi yang lebih baik.
- **Bahasa ambigu:** "cepat," "aman," "intuitif" tanpa kriteria terukur, membuat persyaratan tidak dapat diverifikasi.
- **[Gold-plating](https://en.wikipedia.org/wiki/Gold_plating_(software_engineering)):** menangkap persyaratan yang tidak benar-benar dibutuhkan pemangku kepentingan mana pun, menggelembungkan cakupan dan biaya.
- **Persyaratan nonfungsional yang hilang:** menemukan kewajiban kinerja, keamanan, atau aksesibilitas hanya setelah arsitektur ditetapkan.
- **Persyaratan yang menjamur:** kebenaran tersebar di email, tiket, dan slide tanpa sumber berwenang.
- **Perubahan beku atau tak terkendali:** entah menolak semua perubahan atau menerima setiap perubahan tanpa penilaian dampak.
- **Tanpa keterlacakan:** ketidakmampuan menjawab apa yang terdampak suatu perubahan atau mengapa suatu fitur ada, fatal dalam sistem teraudit.
- **Kelumpuhan analisis:** spesifikasi tak berujung yang menunda pembelajaran dari perangkat lunak yang berfungsi.
- **Pemangku kepentingan yang diabaikan:** operator, auditor, dan non-pengguna terdampak dibiarkan keluar sampai penerimaan.

## Model kematangan

- **Tingkat 1, Memulai.** Persyaratan implisit atau lisan, ditangkap tidak konsisten dan reaktif. Sengketa cakupan dan pengerjaan ulang umum; tidak ada keterlacakan, tidak ada kriteria penerimaan, dan tidak ada proses terdefinisi.
- **Tingkat 2, Mengembangkan.** Beberapa tim menuliskan persyaratan dan melacaknya per proyek, dengan prioritisasi dasar dan penanganan perubahan ad hoc. Praktik ada tetapi bervariasi menurut tim dan orang, sehingga kategori, formalitas, dan kualitas tidak konsisten di seluruh organisasi.
- **Tingkat 3, Membakukan.** Proses persyaratan baku didokumentasikan dan ditegakkan di seluruh organisasi: kategori terdefinisi, praktik penggalian dan validasi, kriteria penerimaan dilampirkan pada saat penulisan, satu sumber berwenang, dan keterlacakan dua arah dari kebutuhan ke tes, disesuaikan secara konsisten dengan konteks agile atau berbasis rencana.
- **Tingkat 4, Mengelola.** Proses diukur dan dikendalikan dengan data. Volatilitas persyaratan, asal cacat, cakupan keterlacakan, dan persentase pekerjaan terkirim yang dapat dilacak ke kebutuhan tervalidasi dilacak terhadap garis dasar; keterlacakan meluas ke bukti penerimaan dan kepatuhan; dan metrik persyaratan memberi masukan pada perkiraan proyek (bab 10.6), sehingga keputusan perubahan dan kualitas bertumpu pada bukti alih-alih opini.
- **Tingkat 5, Mengorkestrasi.** Praktik persyaratan terus diperbaiki dan terintegrasi di seluruh organisasi. Formalitas disetel secara adaptif menurut risiko dan hasil, perkakas penggalian dan keterlacakan terhubung ke penemuan, arsitektur, dan pengiriman, dan organisasi memakai riwayat pengukurannya sendiri untuk mencegah cacat persyaratan yang berulang sebelum mencapai kode.

## Gagasan untuk didiskusikan

- Bagaimana Anda membedakan persyaratan sejati dari solusi prematur ketika pemangku kepentingan senior menyatakannya sebagai solusi?
- Tingkat formalitas persyaratan mana yang tepat untuk sistem berisiko tertinggi Anda versus yang berisiko terendah, dan siapa yang memutuskan?
- Bagaimana Anda menjaga keterlacakan dua arah tetap mutakhir dalam backlog agile yang bergerak cepat tanpa menjadi beban birokrasi?
- Persyaratan nonfungsional mana yang paling sering ditemukan terlalu terlambat di organisasi Anda, dan mengapa?
- Dalam program yang diatur, apa yang merupakan bukti penerimaan yang cukup bahwa persyaratan terpenuhi?
- Bagaimana perkakas penggalian dan spesifikasi berbantuan AI harus mengubah praktik persyaratan Anda, dan risiko baru apa yang dibawanya?

## Poin-poin utama

- Persyaratan menyatakan kebutuhan dan kendala, bukan solusi; mereka harus perlu, tidak ambigu, dapat diverifikasi, dan dapat dilacak.
- Pisahkan persyaratan fungsional, nonfungsional, dan kendala, serta tingkat bisnis, pengguna, dan sistem.
- Gali dari pemangku kepentingan nyata, analisis dan prioritaskan, spesifikasikan pada formalitas yang sesuai, validasi sebelum membangun, dan kelola perubahan.
- Keterlacakan dua arah dari kebutuhan ke bukti penerimaan adalah tulang punggung akuntabilitas, terutama dalam konteks yang diatur.
- Konteks agile dan berbasis rencana berbagi kegiatan yang sama; mereka berbeda dalam waktu, formalitas, dan artefak, jadi pilih menurut risiko.
- Biaya persyaratan yang buruk dibayar terlambat dan berlipat; berinvestasi lebih awal adalah daya ungkit terhadap pengerjaan ulang dan penerimaan yang gagal.

## Referensi dan bacaan lanjutan

- IEEE dan ISO/IEC, *Guide to the Software Engineering Body of Knowledge (SWEBOK)*, area pengetahuan Software Requirements
- Karl Wiegers dan Joy Beatty, *Software Requirements*
- ISO/IEC/IEEE 29148, *Systems and software engineering: Life cycle processes: Requirements engineering*
- Suzanne Robertson dan James Robertson, *Mastering the Requirements Process*
- Dean Leffingwell, *Agile Software Requirements*
- Mike Cohn, *User Stories Applied*
- Ian Sommerville, *Software Engineering* (bab rekayasa persyaratan)
