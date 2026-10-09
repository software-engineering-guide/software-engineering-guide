# 2.15 Debugging dan pemecahan masalah

## Tinjauan dan motivasi

Debugging adalah pekerjaan disiplin untuk mencari tahu mengapa sebuah sistem melakukan sesuatu yang tidak semestinya, dan pemecahan masalah (troubleshooting) adalah keterampilan yang sama yang diarahkan pada sistem produksi yang berjalan di bawah tekanan waktu. Keduanya adalah [metode ilmiah](https://en.wikipedia.org/wiki/Scientific_method) yang diterapkan pada cacat: Anda mengamati perilaku yang mengejutkan, membentuk hipotesis tentang penyebabnya, merancang eksperimen yang akan mengonfirmasi atau menyangkalnya, dan membiarkan bukti, bukan firasat Anda, memberi tahu apa yang harus diubah. Dilakukan dengan cara ini, debugging adalah keterampilan rekayasa yang dapat dipelajari dan diajarkan. Dilakukan sebagai cerita rakyat, ia menjadi takhayul: mengubah baris acak, me-restart server, dan berharap.

Bagi tim besar, bedanya mahal. Satu cacat sulit dapat menarik insinyur di beberapa layanan, memakan jam on-call, dan menghentikan rilis. Ketika setiap orang melakukan debugging berdasarkan naluri, upaya itu tidak berlipat, karena tak seorang pun dapat mereproduksi atau menjelaskan apa yang dicoba orang lain. Ketika tim berbagi metode (reproduksi dulu, isolasi lewat pencarian, tangkap bug dalam tes yang gagal, lalu perbaiki), upaya yang sama berubah menjadi proses yang dapat diulang dan rangkaian tes regresi yang tumbuh. Debugging terhubung erat dengan strategi pengujian (bab 2.4), kualitas perangkat lunak (bab 2.11), dan kebiasaan konstruksi (bab 2.9) yang membuat kode dapat didiagnosis sejak awal.

Dalam konteks enterprise dan pemerintah, taruhannya naik. Cacat enterprise melintasi batas layanan dan tim, sehingga orang yang melihat gejala jarang orang yang memiliki penyebabnya. Sistem pemerintah menambahkan kendala yang jarang dijumpai kebanyakan insinyur: lingkungan terisolasi atau terbatas di mana Anda tidak dapat memasang debugger ke produksi, build yang dapat direproduksi yang harus didiagnosis dari artefak, dan jejak audit yang harus mencatat apa yang Anda ubah dan mengapa. Dalam ketiganya, tujuannya sama: ganti tebakan dengan bukti.

## Prinsip utama

- **Reproduksi sebelum berteori.** Bug yang tidak dapat Anda picu sesuai permintaan adalah desas-desus, bukan cacat.
- **Debugging adalah pengujian hipotesis.** Nyatakan apa yang Anda yakini, lalu rancang eksperimen termurah yang dapat membuktikan Anda keliru.
- **Baca galat dan stack trace lebih dulu.** Sistem biasanya memberi tahu di mana ia rusak sebelum Anda mengubah satu baris.
- **Cari ruang masalah, jangan pindai.** Bagi dua wilayah tersangka di setiap langkah alih-alih membaca dari atas ke bawah.
- **Kurangi sampai minimum.** Lucuti kasus sampai hanya pemicu esensial yang tersisa.
- **Satu perubahan sekali waktu.** Suntingan serampangan menghancurkan bukti yang akan memberi tahu perubahan mana yang penting.
- **Tangkap bug dalam tes yang gagal sebelum memperbaiki.** Perbaikan baru terbukti ketika tes itu hijau dan tetap hijau.
- **Temukan akar penyebab, bukan gejala terdekat.** Tambalan yang menyembunyikan gejala membiarkan cacat kembali.

## Rekomendasi

### Reproduksi cacat dengan andal sebelum mengubah apa pun

Tugas pertama Anda adalah reproduksi yang andal: serangkaian langkah atau kasus otomatis yang memicu bug sesuai permintaan. Tanpanya Anda tidak dapat membedakan perbaikan sejati dari kebetulan, karena gejala dapat datang dan pergi karena alasan yang tidak pernah Anda kendalikan. Pastikan masukan, lingkungan, versi, dan waktunya. Jika bug bersifat intermiten, buru variabel tersembunyi yang membuatnya muncul (catatan data tertentu, batas jam, permintaan konkuren) sampai reproduksi dapat diandalkan. Reproduksi yang andal adalah artefak tunggal paling berharga dalam debugging, karena segala sesuatu sesudahnya menjadi terukur.

### Baca galat, log, dan stack trace sebelum menyentuh kode

Sebelum membentuk satu teori pun, baca apa yang sudah dikatakan sistem. [Stack trace](https://en.wikipedia.org/wiki/Stack_trace) (catatan rantai panggilan pada saat kegagalan) biasanya menyebut berkas, baris, dan urutan yang gagal. Pesan exception, baris log di sekitarnya, dan nilai dalam cakupan mempersempit pencarian sebelum Anda mengubah apa pun. Insinyur membuang berjam-jam berteori tentang penyebab yang sudah disingkirkan traceback di baris pertama. Perlakukan keluaran galat sebagai saksi pertama, baca dengan cermat dan lengkap, dan baru kemudian putuskan apa yang diselidiki.

### Isolasi dengan pencarian biner atas ruang masalah

Jangan pindai kode dari atas ke bawah. Cari. Gunakan [pencarian biner](https://en.wikipedia.org/wiki/Binary_search_algorithm): temukan titik di mana keadaan masih baik dan titik di mana sudah buruk, lalu periksa titik tengahnya, dan ulangi, membagi dua wilayah tersangka setiap kali. Ini mengubah pencarian seribu baris menjadi sepuluh pertanyaan. Ketika regresi muncul dalam rentang commit, terapkan gagasan yang sama pada riwayat dengan bisection: `git bisect` menelusuri rentang commit, dan Anda menandai setiap revisi baik atau buruk sampai ia menyebut perubahan persis yang memperkenalkan cacat. Otomatiskan tes baik-atau-buruk dan bisection berjalan sendiri.

### Kurangi menjadi contoh minimal yang dapat direproduksi

Begitu Anda dapat memicu bug, kecilkan. [Contoh minimal yang dapat direproduksi](https://en.wikipedia.org/wiki/Minimal_reproducible_example) adalah masukan dan jalur kode terkecil yang masih gagal: hapus data, fitur, dan langkah sampai pengurangan lebih lanjut membuat bug lenyap. Reduksi bukan kerja sia-sia; setiap elemen yang Anda singkirkan adalah penyebab yang telah Anda coret, sehingga kasus minimal sering menunjuk langsung ke cacat. Ketika masukan besar atau terstruktur, otomatiskan penyusutan dengan [delta debugging](https://en.wikipedia.org/wiki/Delta_debugging), algoritma yang secara sistematis menghapus potongan masukan yang gagal untuk menemukan himpunan bagian gagal minimal. Reproduksi kecil yang berdiri sendiri juga laporan bug terbaik yang dapat diserahkan kepada tim lain.

### Instrumentasi dengan log, lalu pakai debugger interaktif

Cocokkan perkakas dengan bug. Logging dan instrumentasi terarah paling baik ketika Anda perlu melihat perilaku dari waktu ke waktu, lintas proses, atau di lingkungan yang tidak dapat Anda jeda. Debugger interaktif, yang memungkinkan Anda menetapkan breakpoint, melangkah baris demi baris, dan memeriksa status hidup, paling baik ketika Anda dapat menjalankan kode secara lokal dan perlu mengamati satu eksekusi dengan cermat. Tambahkan instrumentasi sebagai eksperimen yang disengaja yang terikat pada hipotesis, bukan pernyataan print yang tersebar, dan hapus atau promosikan menjadi logging terstruktur permanen begitu bug terpecahkan. Di produksi, bersandarlah pada debugging berbasis observabilitas: event berkardinalitas tinggi dan pelacakan terdistribusi (bab 9.2) memungkinkan Anda mengikuti satu permintaan melintasi banyak layanan, yang sering satu-satunya cara men-debug sistem terdistribusi yang tidak dapat Anda pasangi debugger.

### Tulis tes yang gagal yang menangkap bug sebelum memperbaiki

Sebelum menulis perbaikan, tulis tes yang gagal karena bug. Ini melakukan tiga hal sekaligus: membuktikan Anda benar-benar memahami penyebabnya, mendefinisikan persis apa arti "diperbaiki," dan menjadi penjaga permanen. Lalu buat perbaikan dan saksikan tes menjadi hijau. Tes itu kini bergabung dengan rangkaian Anda sebagai penjaga [pengujian regresi](https://en.wikipedia.org/wiki/Regression_testing), sehingga cacat yang sama tidak dapat kembali tanpa diketahui. Praktik ini mengikat debugging langsung dengan strategi pengujian Anda (bab 2.4): setiap bug sulit yang Anda pecahkan meninggalkan rangkaian lebih kuat daripada saat ditemukan, dan tes yang goyah mendapat perlakuan sama (reproduksi nondeterminisme, lalu jaga) alih-alih anotasi retry.

### Temukan akar penyebab, dan jaga analisis tetap tanpa menyalahkan

Memperbaiki gejala bukan memperbaiki bug. Telusuri kegagalan kembali ke asal sebenarnya, bertanya mengapa di setiap lapisan sampai Anda mencapai penyebab yang dapat Anda hilangkan alih-alih tutupi. Untuk cacat yang mencapai produksi, jalankan analisis akar penyebab tanpa menyalahkan sebagai bagian dari manajemen insiden (bab 9.3): fokus pada kondisi sistem dan proses yang membiarkan bug dirilis dan bertahan, tidak pernah pada individu yang menulis barisnya. Penyalahan mendorong informasi ke bawah tanah, dan debugging berjalan di atas informasi. Keluarannya adalah perbaikan sekaligus perubahan pada cara kelas cacat itu tertangkap lebih awal kelak.

## Trade-off: kelebihan dan kekurangan

| Pendekatan | Kelebihan | Kekurangan |
|---|---|---|
| Logging dan instrumentasi | Bekerja di produksi dan sistem terdistribusi; menangkap perilaku dari waktu ke waktu | Derau, biaya, dan log yang menjamur; dapat mengganggu bug waktu |
| Debugger interaktif | Pemeriksaan status hidup yang presisi; cepat untuk bug lokal | Tak berguna di produksi terbatas atau terisolasi; dapat menyembunyikan bug konkurensi |
| Disiplin reproduksi-dulu | Mengubah tebakan menjadi pengukuran; memungkinkan tes yang gagal | Lambat di awal; sebagian bug sungguh sulit dipicu |
| Pencarian biner dan bisection | Isolasi cepat, bahkan di kode asing | Perlu tes baik-atau-buruk yang andal; sulit bila bug berinteraksi |
| Reduksi delta debugging | Menyusutkan masukan raksasa ke pemicu secara otomatis | Biaya persiapan; mengasumsikan kegagalan deterministik |
| Perbaiki gejala sekarang | Memulihkan layanan cepat di bawah tekanan | Membiarkan akar penyebab kembali; menumpuk utang |

Ketegangan pusatnya adalah kecepatan versus kepastian. Di bawah insiden produksi Anda mungkin perlu menghentikan pendarahan dulu (rollback atau tambalan gejala) untuk memulihkan layanan, dan itu sah. Kesalahannya adalah berhenti di situ. Selesaikan ketegangan dengan memisahkan dua tugas: mitigasi cepat untuk melindungi pengguna, lalu reproduksi, temukan akar penyebab, dan tambahkan penjaga regresi sebelum Anda menganggap cacat selesai. Perbaikan gejala tanpa tindak lanjut adalah bug yang telah Anda setujui untuk ditemui lagi.

## Pertanyaan untuk didiskusikan dengan tim Anda

1. **Ketika seseorang menemui bug sulit, apa hal pertama yang mereka lakukan, dan apakah itu reproduksi atau menebak?** Jawaban jujur mengungkap apakah tim Anda punya metode bersama atau ruangan penuh cerita rakyat pribadi. Minta orang menceritakan cacat sulit terakhir mereka dengan lantang: apakah mereka mendapat reproduksi yang andal lebih dulu, atau mulai mengubah kode dan me-restart hal-hal? Tim yang mereproduksi lebih dulu dapat menyerahkan bug antarorang, karena reproduksi ikut berpindah; tim yang menebak tidak dapat, karena setiap upaya tidak dapat diulang. Ini makin penting seiring tim tumbuh, karena orang yang melihat gejala makin sering bukan orang yang dapat memperbaikinya. Jika bawaannya menebak, sepakati reproduksi-dulu sebagai norma dan jadikan reproduksi bersih sebagai harga tiket masuk ke tiket bug.

2. **Apakah bug yang kita perbaiki kembali, dan akankah kita tahu jika kembali?** Cacat yang kembali adalah cacat yang akar penyebabnya tidak pernah dihilangkan dan perbaikannya tidak pernah dijaga oleh tes. Tarik insiden dan tiket yang dibuka kembali kuartal terakhir Anda dan hitung berapa yang merupakan pengulangan atau sepupu dekat bug sebelumnya. Setiap pengulangan adalah bukti bahwa tim menambal gejala, melewatkan tes yang gagal, atau menghentikan analisis akar penyebab terlalu dini. Perbaikannya adalah aturan: tak ada bug yang ditutup sampai tes yang gagal pada perilaku lama lolos pada perilaku baru dan bergabung ke rangkaian. Bawa satu bug berulang terbaru dan tanyakan penjaga apa yang akan menangkapnya, karena penjaga itu yang Anda lewatkan.

3. **Dapatkah kita men-debug sistem produksi kita sama sekali, mengingat bagaimana kita diizinkan menyentuhnya?** Di lingkungan enterprise dan terutama pemerintah, Anda sering tidak dapat memasang debugger, tidak dapat mereproduksi dengan data nyata, dan tidak dapat mengubah sistem yang berjalan tanpa jejak audit. Jika satu-satunya teknik debugging Anda adalah debugger interaktif lokal, Anda buta persis di tempat bug tersulit hidup. Tanyakan bukti apa yang sebenarnya ditinggalkan kegagalan produksi: log terstruktur, pelacakan terdistribusi (bab 9.2), core dump, atau artefak build yang dapat direproduksi. Putuskan sekarang apa yang harus Anda tangkap secara bawaan agar insiden mendatang dapat didiagnosis, karena Anda tidak dapat menambah instrumentasi pada kegagalan yang sudah terjadi. Dalam lingkungan yang diatur, pastikan jejak yang sama juga memenuhi kewajiban audit Anda.

4. **Ketika insiden produksi memaksa kita menghentikan pendarahan dengan cepat, bagaimana kita memastikan akar penyebab tetap ditemukan sesudahnya?** Di bawah insiden, rollback atau tambalan gejala adalah langkah pertama yang tepat untuk melindungi pengguna, tetapi bahayanya adalah tiket ditutup begitu layanan kembali dan cacat yang mendasarinya tidak pernah didiagnosis. Bagi tim besar di sinilah utang menumpuk tanpa terlihat, karena kelas kegagalan yang sama muncul kembali pada layanan berbeda dan insinyur on-call berbeda berbulan-bulan kemudian. Bawa beberapa insiden severity-satu terakhir Anda dan periksa masing-masing: apakah reproduksi, analisis akar penyebab, dan penjaga regresi menyusul mitigasi, atau ceritanya berakhir di "layanan dipulihkan"? Sepakati aturan eksplisit bahwa insiden yang dimitigasi tetap terbuka sampai akar penyebab dipahami dan dijaga, dan namai siapa yang memiliki tindak lanjut itu. Dalam konteks enterprise dan pemerintah, kaitkan ini dengan proses manajemen insiden Anda (bab 9.3) agar tinjauan pascainsiden menjadi langkah wajib yang dapat diaudit, bukan kesopanan yang tergelincir ketika kebakaran berikutnya dimulai.

5. **Seberapa banyak kegagalan yang sebenarnya dapat kita rekonstruksi setelah kejadian, dan siapa yang memutuskan apa yang kita tangkap secara bawaan?** Anda tidak dapat memasang instrumentasi pada kegagalan yang sudah terjadi, sehingga kemampuan didiagnosis insiden apa pun ditetapkan sebelumnya oleh log, jejak, metrik, dan dump yang Anda pilih untuk dikeluarkan. Pertimbangan yang bersaing adalah biaya dan derau: event berkardinalitas tinggi dan pelacakan penuh tidak gratis, dan log berlebihan mengubur sinyal sambil membengkakkan penyimpanan dan, dalam konteks yang diatur, paparan retensi data Anda. Bawa insiden nyata terbaru dan tanyakan bukti apa yang ditinggalkannya, lalu kerjakan mundur ke apa yang Anda harap telah Anda tangkap dan berapa biaya menyimpannya. Putuskan dengan sengaja sinyal mana yang aktif secara bawaan versus disampel atau opt-in, dan catat keputusan itu agar menjadi kebijakan, bukan kecelakaan. Untuk sistem enterprise atau pemerintah, tambahkan siapa yang bertanggung jawab atas anggaran observabilitas itu dan apakah jejak yang ditangkap juga memenuhi kewajiban audit, privasi, dan residensi data.

6. **Apakah kita memperlakukan debugging sebagai keterampilan yang diajarkan dan terukur, atau insinyur baru menyerapnya lewat penyerapan?** Debugging dapat dipelajari, namun sebagian besar tim tidak pernah mengajarkannya secara eksplisit, sehingga junior mewarisi cerita rakyat mana pun yang terdekat, dan metode reproduksi-dulu menyebar tidak merata atau tidak sama sekali. Ketegangannya adalah bahwa pengajaran yang disengaja (berpasangan pada bug sulit, menulis temuan pascainsiden, melacak metrik) memakan waktu senior yang selalu terasa dibutuhkan di tempat lain. Bawa dua angka ke diskusi: tingkat cacat berulang dan waktu-hingga-diagnosis Anda, karena jika Anda tidak dapat mengukurnya Anda tidak dapat mengatakan apakah metode Anda membaik atau memburuk. Pertimbangkan apakah orientasi mencakup latihan debugging nyata dan apakah temuan akar penyebab benar-benar memberi makan deteksi lebih awal. Dalam organisasi besar atau publik, praktik debugging yang terdokumentasi dan terukur juga menjadi bukti ketelitian rekayasa yang makin diharapkan dilihat auditor, regulator, dan badan pengawas.

## Lensa sektor

**Startup.** Dengan segelintir insinyur dan tanpa kelonggaran, tujuan Anda adalah membuat bug murah direproduksi dan mustahil dilupakan, bukan membangun proses berat. Bersandarlah pada `git bisect`, reproduksi lokal yang cepat, dan satu tes yang gagal per bug yang diperbaiki, karena kebiasaan itu memakan menit dan menghentikan Anda membayar ulang cacat yang sama selagi mencoba merilis. Lewati postmortem formal, tetapi jangan pernah lewati tes regresi: itu satu artefak yang cukup kecil untuk selalu terjangkau dan cukup berharga untuk selalu disimpan.

**Bisnis kecil.** Anda kemungkinan tidak punya spesialis keandalan atau observabilitas dan anggaran perkakas ketat, jadi pilih apa yang sudah diberikan tumpukan Anda: stack trace yang terbaca, log terstruktur, dan pelacakan yang tertanam dalam kerangka kerja dan layanan hosting yang telah Anda beli. Ketika mengevaluasi platform baru, timbang seberapa dapat didiagnosisnya kegagalan, karena perkakas murah yang menyembunyikan apa yang salah memakan biaya jauh lebih besar dalam waktu menebak daripada lisensi yang dihemat. Reproduksi-dulu dan satu-perubahan-sekali-waktu adalah disiplin gratis yang paling cepat membuahkan hasil ketika tak seorang pun punya jam luang.

**Enterprise.** Bug sulit Anda melintasi batas layanan dan tim, sehingga orang yang melihat gejala jarang memiliki penyebabnya, dan metode bersama lebih penting daripada keterampilan individu mana pun. Bakukan reproduksi-dulu, isolasi pencarian biner, tes yang gagal sebelum perbaikan, dan postmortem tanpa menyalahkan di seluruh tim, dan berinvestasilah pada pelacakan terdistribusi (bab 9.2) agar satu permintaan dapat diikuti lintas layanan. Kelola debugging sebagai kemampuan terukur: lacak tingkat cacat berulang dan waktu-hingga-diagnosis, dan salurkan temuan akar penyebab kembali ke deteksi lebih awal agar kelas kegagalan yang sama tidak berkeliling peta layanan Anda.

**Pemerintah.** Aturan pengadaan, lingkungan terbatas, dan akuntabilitas publik membentuk bagaimana Anda boleh men-debug sama sekali. Anda sering tidak dapat memasang debugger ke produksi atau menyalin data warga ke laptop, jadi rancang untuk diagnosis dari apa yang diizinkan: build yang dapat direproduksi, catatan sintetis dalam enklaf terisolasi, serta log dan jejak terstruktur yang ditangkap secara bawaan. Catat setiap langkah diagnostik dan setiap perubahan dalam jejak audit, dan wajibkan vendor mengekspos telemetri dan keterreproduksian build yang cukup agar Anda dapat menyelidiki kegagalan secara independen alih-alih bergantung pada kata pemasok.

## Contoh

**Startup.** Tim empat insinyur terus melihat checkout gagal untuk sebagian pengguna, tetapi tidak pernah dalam pengujian. Alih-alih menebak, satu insinyur menangkap reproduksi yang andal dengan memutar ulang payload permintaan yang gagal persis, lalu membaca stack trace yang selama ini diabaikan, yang menunjuk ke panggilan penguraian tanggal. `git bisect` cepat atas commit seminggu menyebut perubahan yang mengganti pustaka tanggal. Mereka menulis tes yang gagal dengan stempel waktu yang bermasalah, memperbaiki parser, menyaksikan tes menjadi hijau, dan menyimpannya dalam rangkaian. Seluruh penyelidikan memakan satu sore karena mereka mereproduksi sebelum berteori, dan bug tidak pernah kembali.

**Enterprise.** Platform pembayaran melihat timeout intermiten yang tidak dapat dijelaskan satu tim pun, karena gejala muncul di checkout tetapi penyebabnya hidup tiga layanan jauhnya. Insinyur on-call memakai pelacakan terdistribusi (bab 9.2) untuk mengikuti satu permintaan yang gagal melintasi batas layanan dan menemukan panggilan hilir yang kadang deadlock di bawah beban konkuren, [race condition](https://en.wikipedia.org/wiki/Race_condition) klasik di mana hasil bergantung pada waktu yang tidak beruntung antarthread. Mereka mereproduksinya dengan tes beban, menangkapnya dalam tes integrasi yang gagal, memperbaiki penguncian, dan menjalankan postmortem tanpa menyalahkan (bab 9.3) yang menambah span pelacakan dan peringatan agar kemunculan berikutnya tertangkap dalam menit, bukan hari.

**Pemerintah.** Sebuah lembaga tunjangan menjalankan sistem kasusnya di lingkungan terisolasi di mana insinyur tidak dapat memasang debugger ke produksi dan tidak dapat menyalin data warga ke laptop mereka. Cacat perhitungan muncul dalam rekonsiliasi. Tim men-debug dari apa yang diizinkan lingkungan: log terstruktur, build yang dapat direproduksi yang dapat mereka dirikan di enklaf uji terisolasi, dan catatan sintetis yang menciptakan ulang kasus yang gagal. Setiap langkah diagnostik dicatat dalam jejak audit, perbaikan dikirim dengan tes gagal-lalu-lolos sebagai bukti, dan analisis akar penyebab memberi makan pemeriksaan pra-rilis baru. Karena reproduksi memakai data sintetis, tak ada catatan warga yang meninggalkan batas.

## Kasus bisnis: motivasi, ROI, dan TCO

Imbal hasil debugging yang disiplin diukur dalam jam insinyur yang tidak dihabiskan menebak dan dalam cacat yang tidak berulang. Bug intermiten yang tidak terdiagnosis dapat memakan berhari-hari waktu senior dan eskalasi on-call berulang; metode reproduksi-dulu mengubahnya menjadi tugas terbatas yang dapat didelegasikan, dan kebiasaan tes yang gagal menghentikan cacat yang sama menagih Anda lagi kuartal depan. Di organisasi besar, efek majemuk tidak pernah membayar ulang bug yang sama itu besar, dan langsung memperbaiki tingkat kegagalan perubahan dan waktu rata-rata pemulihan yang sudah dilacak pimpinan.

Total biaya kepemilikannya sebagian besar pelatihan dan perkakas, dan sederhana. Anda membutuhkan konvensi bersama (reproduksi dulu, satu perubahan sekali waktu, tes yang gagal sebelum perbaikan), debugger dan pelacakan yang sudah umum dalam toolchain, dan investasi observabilitas yang dijelaskan di bab 9.2. Biaya tersembunyi yang lebih besar adalah alternatifnya: budaya takhayul di mana insinyur menerapkan perubahan serampangan, gejala ditambal dan kembali, dan beban on-call tumbuh tanpa batas. Mengurangi pekerjaan rutin on-call saja sering membenarkan investasi, dan kasus bagi pimpinan paling sederhana dinyatakan sebagai insiden berulang yang lebih sedikit dan pemulihan lebih cepat untuk biaya sekali jalan dalam kebiasaan dan instrumentasi.

## Anti-pola dan jebakan

- **Debugging serampangan:** mengubah banyak hal sekaligus, sehingga bahkan perbaikan tidak mengajari Anda apa pun tentang penyebabnya.
- **Memperbaiki tanpa mereproduksi:** menyatakan kemenangan atas bug yang tidak pernah dapat Anda picu sesuai permintaan.
- **Mengabaikan keluaran galat:** berteori tentang penyebab yang sudah disingkirkan stack trace.
- **Menambal gejala:** membungkam gejala sementara akar penyebab bertahan untuk kembali.
- **Print-statement menjamur:** keluaran debug tersebar yang ditinggalkan di kode, menambah derau alih-alih eksperimen yang terikat pada hipotesis.
- **Melewatkan tes regresi:** memperbaiki bug tetapi tidak meninggalkan penjaga, sehingga dapat diam-diam kembali.
- **Mencoba ulang tes goyah:** menyembunyikan nondeterminisme dengan retry alih-alih men-debug race condition atau [heisenbug](https://en.wikipedia.org/wiki/Heisenbug) yang mendasarinya, bug yang berubah atau lenyap begitu Anda mencoba mengamatinya.
- **Postmortem yang menyalahkan:** menghukum penulis, yang mendorong ke bawah tanah informasi yang diandalkan debugging.

## Model kematangan

- **Tingkat 1, Memulai:** Debugging adalah cerita rakyat individual dan reaksi. Insinyur menebak, menerapkan perubahan serampangan, dan me-restart hal-hal. Bug diperbaiki pada gejala, reproduksi jarang, dan cacat yang sama berulang. Produksi nyaris tidak dapat didiagnosis, dan tak seorang pun dapat menyerahkan bug kepada siapa pun karena tak ada upaya yang dapat diulang.
- **Tingkat 2, Mengembangkan:** Beberapa insinyur mereproduksi dengan andal, membaca stack trace, dan memakai debugger, tetapi praktik tidak konsisten dan bervariasi dari orang ke orang dan tim ke tim. Logging ada tetapi berisik dan tak terstruktur. Perbaikan kadang dikirim dengan tes yang gagal, sering tidak, dan analisis akar penyebab terjadi hanya ketika seseorang bersikeras.
- **Tingkat 3, Membakukan:** Reproduksi-dulu, isolasi pencarian biner, satu perubahan sekali waktu, dan tes yang gagal sebelum perbaikan adalah norma tim terdokumentasi yang ditegakkan di seluruh organisasi. Bisection dan reduksi delta debugging adalah praktik umum. Produksi memiliki logging dan pelacakan terstruktur (bab 9.2), dan postmortem tanpa menyalahkan (bab 9.3) adalah respons baku untuk setiap cacat yang lolos.
- **Tingkat 4, Mengelola:** Praktik debugging diukur dan dikendalikan terhadap garis dasar. Tingkat cacat berulang, waktu-hingga-diagnosis, jumlah tiket yang dibuka kembali, dan persentase perbaikan yang dikirim dengan tes regresi dilacak per tim dan ditinjau secara berkala. Reproduksi dan penyelesaian akar penyebab diperlakukan sebagai gerbang alih-alih niat baik, dan tren terhadap garis dasar menentukan di mana Anda berinvestasi pada perkakas, pelatihan, dan observabilitas.
- **Tingkat 5, Mengorkestrasi:** Debugging adalah keterampilan yang diajarkan dan terintegrasi dengan kualitas (bab 2.11) dan manajemen insiden (bab 9.3), dan seluruh lingkaran beradaptasi terus-menerus. Observabilitas dirancang masuk sehingga sebagian besar bug produksi dapat didiagnosis tanpa debugger, setiap bug yang terpecahkan memperkuat rangkaian regresi, dan temuan akar penyebab memberi makan deteksi lebih awal sehingga kelas cacat dicegah alih-alih didiagnosis ulang. Organisasi menyeimbangkan kembali upaya seiring berkembangnya sistem dan mode kegagalannya, dan tingkat cacat berulang terus turun.

## Gagasan untuk didiskusikan

1. Berapa persen bug terbaru Anda yang direproduksi dengan andal sebelum ada yang mengubah kode, dan apa yang dikatakan persentase itu tentang metode Anda?
2. Ketika regresi muncul, apakah tim Anda meraih bisection, atau membaca kode dengan tangan sampai seseorang melihatnya?
3. Seberapa dapat didiagnosisnya sistem produksi Anda hari ini, dan apa yang akan Anda berikan untuk memiliki tangkapan tentang kegagalan yang sudah terjadi?
4. Apakah perbaikan Anda secara konsisten dikirim dengan tes gagal-lalu-lolos, dan jika tidak, di mana disiplin itu patah?
5. Bagaimana Anda menangani tes goyah: men-debug nondeterminisme, atau menutupinya dengan retry?
6. Apakah debugging diajarkan dengan sengaja kepada insinyur baru, atau mereka dibiarkan menyerap cerita rakyat lewat penyerapan?

## Poin-poin utama

- Debugging adalah pengujian hipotesis: reproduksi dengan andal, baca galat dan stack trace, lalu isolasi dengan pencarian biner dan bisection alih-alih memindai.
- Kurangi kegagalan menjadi contoh minimal yang dapat direproduksi, memakai delta debugging untuk masukan besar, karena setiap elemen yang disingkirkan adalah penyebab yang dicoret.
- Cocokkan perkakas dengan bug: instrumentasi dan pelacakan untuk produksi dan sistem terdistribusi (bab 9.2), debugger interaktif untuk penyelidikan lokal.
- Tulis tes yang gagal yang menangkap bug sebelum memperbaiki, agar perbaikan terbukti dan cacat dijaga selamanya (bab 2.4).
- Temukan dan hilangkan akar penyebab, jalankan postmortem tanpa menyalahkan (bab 9.3), dan perlakukan debugging sebagai keterampilan yang dapat dipelajari, bukan cerita rakyat.
- Ubah satu hal sekali waktu; perubahan serampangan dan tambalan gejala menghancurkan bukti dan mengundang bug kembali.

## Referensi dan bacaan lanjutan

- David J. Agans, *Debugging: The 9 Indispensable Rules for Finding Even the Most Elusive Software and Hardware Problems*
- Andreas Zeller, *Why Programs Fail: A Guide to Systematic Debugging*
- Andreas Zeller dan Ralf Hildebrandt, "Simplifying and Isolating Failure-Inducing Input" (algoritma delta debugging)
- Brian W. Kernighan dan Rob Pike, *The Practice of Programming* (bab tentang debugging)
- Andrew Hunt dan David Thomas, *The Pragmatic Programmer* (bab tentang debugging dan asersi)
- Steve McConnell, *Code Complete: A Practical Handbook of Software Construction* (bab debugging)
- John Regehr, "Reducers Are Fuzzers" dan tulisan terkait tentang reduksi kasus tes
- Charity Majors, Liz Fong-Jones, dan George Miranda, *Observability Engineering* (men-debug produksi dengan telemetri berkardinalitas tinggi dan pelacakan)
- Betsy Beyer, Chris Jones, Jennifer Petoff, dan Niall Richard Murphy, eds., *Site Reliability Engineering* (postmortem tanpa menyalahkan dan debugging produksi)
